"""Dependency composition for local CLI/HTTP use cases; no implicit Repository state."""

from featuretree.reporting.workflow_activity import workflow_activity
from featuretree.workflow.backends.processes import identity
from featuretree.core.artifacts import FileArtifactStore
from featuretree.core.contracts import SchemaRegistry
from featuretree.core.requests import RequestStore
from featuretree.core.versions import VersionStore
from featuretree.corpus.catalog import IndexedCatalog
from featuretree.corpus.snapshots import SnapshotStore
from featuretree.knowledge.reviews import ReviewLedger, project_reviews
from featuretree.reporting.releases import ReleaseReader
from featuretree.reporting.tree_browser import TreeBrowser
from featuretree.workflow.backends.opencode import OpenCodeBackend
from featuretree.workflow.calibration import CalibrationService
from featuretree.workflow.observations import ObservationService
from featuretree.workflow.knowledge_planning import KnowledgePlanningService
from featuretree.workflow.source_supplement import SourceSupplementService
from featuretree.workflow.structure_revisions import StructureRevisionService
from featuretree.workflow.replanning import ReplanService
from featuretree.workflow.execution import AttemptExecutor
from featuretree.workflow.freezes import FreezeService
from featuretree.workflow.handlers import StageHandlers
from featuretree.workflow.planner import Planner
from featuretree.workflow.provenance import ExecutionProvenance
from featuretree.workflow.registry import PipelineRegistry
from featuretree.workflow.releases import LocalReleaseService
from featuretree.workflow.review_service import LocalReviewService
from featuretree.workflow.run_store import RunStore
from featuretree.workflow.runner import Runner


class Application:
    def __init__(self, root, backend=None):
        self.root = root.resolve()
        data = self.root / "data"
        self.schemas = SchemaRegistry(self.root / "config/v2/schemas")
        self.artifacts = FileArtifactStore(data / "objects")
        self.versions = VersionStore(data, self.artifacts)
        self.snapshots = SnapshotStore(data / "sources", self.schemas)
        self.catalog = IndexedCatalog(self.snapshots, data / "indexes", self.root / "docs-raw/official")
        self.registry = PipelineRegistry.load(self.root / "config/v2/pipelines.json")
        self.runs = RunStore(self.root / ".workflow/v2/runs")
        self.provenance = ExecutionProvenance(self.artifacts, self.runs)
        self.freezes = FreezeService(self.artifacts, self.schemas, self.snapshots, self.catalog, self.provenance, data / "freezes")
        self.planner = Planner(self.root, self.registry, self.schemas, self.artifacts, self.catalog, self.runs, self.freezes.validate)
        handlers = StageHandlers(self.artifacts, self.catalog)
        self.runner = Runner(self.runs, self.artifacts,
                             AttemptExecutor(self.root, self.artifacts, backend or OpenCodeBackend(runtime_directory=self.root / "tools/opencode"), handlers))
        self.ledger = ReviewLedger(data / "reviews", self.artifacts, self.schemas)
        self.replanning = ReplanService(self.planner, self.runs, self.artifacts, handlers, self.provenance)
        self.releases = LocalReleaseService(self.versions, self.artifacts, self.schemas,
                                            self.snapshots, self.catalog, self.ledger, self.freezes)
        self.reader = ReleaseReader(self.versions, self.artifacts)
        self.tree_browser = TreeBrowser(self.artifacts, self.versions, self.reader, self.catalog)
        self.structure_revisions = StructureRevisionService(self.artifacts, self.versions, self.planner, self.runs)
        self.reviews = LocalReviewService(self.ledger, self.artifacts, self.runner, self.releases, self.structure_revisions)
        self.requests = RequestStore(data / "requests")
        self.calibration = CalibrationService(data / "reviews/calibrations", self.artifacts, self.schemas)
        self.observations = ObservationService(self.artifacts, self.schemas)
        self.knowledge_planning = KnowledgePlanningService(self.artifacts, self.freezes, self.planner)
        self.source_supplement = SourceSupplementService(self.root, self.runs, self.planner, self.artifacts, self.snapshots)

    def candidates(self):
        rows = []
        for state in self.runs.list():
            for task in state["tasks"].values():
                if task["result_ref"] and task["stage_id"] in ("ft-check", "fk-assemble"):
                    response = self.artifacts.get(task["result_ref"])
                    extra = {}
                    if task["stage_id"] == "fk-assemble":
                        article = self.artifacts.get(response["payload"]["article_ref"])
                        extra["feature_name"] = self.artifacts.get(article["dependencies"]["feature_ref"])["name"]
                    rows.append({"run_id": state["run_id"], "work_id": task["work_id"],
                                 "stage_id": task["stage_id"], "result_ref": task["result_ref"],
                                 **response["payload"], **extra})
        return rows

    def review_queue(self):
        manifest = self.versions.pin()
        articles = {reference: self.artifacts.get(reference)
                    for reference in (manifest["knowledge_refs"].values() if manifest else [])}
        for row in self.candidates():
            if row.get("article_ref"):
                articles[row["article_ref"]] = self.artifacts.get(row["article_ref"])
        projection = project_reviews(articles, self.ledger.events())
        return {"release_id": manifest["release_id"] if manifest else None, **projection}

    def run_detail(self, run_id):
        plan, state = self.runs.load(run_id)
        return {"plan": plan, "state": state, "batch_progress": self.runs.batch_progress(state),
                "activity": workflow_activity(self.runs.folder(run_id), state, self.artifacts, identity)}
