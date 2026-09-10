"""Read-only, packet-scoped source gateway exposed to OpenCode agents."""

import argparse
import json
from pathlib import Path
import sys

from featuretree.core.content import digest, timestamp
from featuretree.core.contracts import SchemaRegistry
from featuretree.core.io import file_lock, read_json, write_json
from featuretree.corpus.catalog import IndexedCatalog, SourceUnavailable
from featuretree.corpus.snapshots import SnapshotStore
from featuretree.workflow.implementation import verify_implementation


def query(catalog, packet, request):
    operation = request["operation"]
    access = packet["source_access"]
    selection = {}
    if access["platform"]:
        selection["platforms"] = [access["platform"]]
    if operation == "body":
        record = catalog.get(access["snapshot_id"], "documents", request["id"])
        if access["platform"] and record["platform"] != access["platform"]:
            raise ValueError("Platform researcher cannot read another platform's source")
        try:
            if request.get("query"):
                return catalog.find_body(access["snapshot_id"], request["id"], request["query"],
                                         request.get("offset", 0), min(request.get("limit", 3), 10))
            return catalog.read_body(access["snapshot_id"], request["id"],
                                     request.get("offset", 0), min(request.get("limit", 12000), 24000))
        except SourceUnavailable as error:
            return {"status": "needs_sources", "snapshot_id": access["snapshot_id"],
                    "document_id": request["id"], "url": record["url"], "reason": str(error)}
    kind = {"apis": "declarations", "topics": "topics", "documents": "documents"}.get(operation)
    if kind is None:
        raise ValueError("Unsupported source operation")
    if kind != "documents":
        selection["ids"] = access["api_ids" if kind == "declarations" else "topic_ids"]
    if request.get("query"):
        selection["query"] = request["query"]
    if request.get("id"):
        if "ids" in selection and request["id"] not in selection["ids"]:
            raise ValueError("Record is outside the work unit's complete input manifest")
        selection["ids"] = [request["id"]]
    return catalog.page(access["snapshot_id"], selection, request.get("cursor"),
                        min(request.get("limit", 20), 100), kind)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--packet", type=Path, required=True)
    args = parser.parse_args(argv)
    packet = read_json(args.packet)
    fingerprint = packet["input_hash"]
    if digest({key: value for key, value in packet.items() if key != "input_hash"}) != fingerprint:
        raise ValueError("Source tool packet was modified")
    request = json.load(sys.stdin)
    verify_implementation(packet["stage_id"], packet.get("implementation_files"))
    schemas = SchemaRegistry(args.root / "config/v2/schemas")
    snapshots = SnapshotStore(args.root / "data/sources", schemas)
    catalog = IndexedCatalog(snapshots, args.root / "data/indexes", args.root / "docs-raw/official")
    folder = args.packet.parent / "source_calls"
    with file_lock(folder / "calls.lock"):
        number = len(list(folder.glob("*.json"))) + 1
        if packet["limits"]["max_tool_calls"] is not None and number > packet["limits"]["max_tool_calls"]:
            raise ValueError("Source tool call budget exhausted; return explicit remaining gaps")
        try:
            result = query(catalog, packet, request)
        except (ValueError, KeyError, OSError) as error:
            result = {"status": "rejected", "error_type": type(error).__name__, "reason": str(error)}
        write_json(folder / f"{number:04d}.json", {"input_hash": fingerprint, "request": request,
                    "result_hash": digest(result), "returned_ids": [row["id"] for row in result.get("items", [])],
                    "next_cursor": result.get("next_cursor"), "created_at": timestamp()}, immutable=True)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
