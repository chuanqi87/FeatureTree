"""Recover committed effects when the outer HTTP receipt lagged behind the pointer."""

from featuretree.core.content import digest, identifier
from featuretree.core.io import read_json


def recover_committed(app, parts, body, key):
    transaction_key = body.get("transaction_key") if parts == ["releases", "publish"] else key if parts == ["releases", "rollback"] else None
    if transaction_key:
        identifier(transaction_key)
        path = app.versions.directory / "transactions" / f"{transaction_key}.json"
        if path.exists():
            transaction = read_json(path)
            manifest = app.versions.get(transaction["release_id"])
            matching = transaction["expected"] == body["expected_release_id"]
            if parts[-1] == "rollback":
                matching = matching and manifest["rollback_target"] == body["target_release_id"]
            if matching and app.versions._contains(app.versions.current_id(), transaction["release_id"]):
                return True, app.releases.publish(transaction_key)
    if len(parts) == 3 and parts[0] == "reviews" and parts[2] == "decisions":
        prior = app.ledger.prior_request(body["article_ref"], body["decision"], key)
        if prior and prior["ticket_id"] == parts[1]:
            return True, app.reviews.submit(body["article_ref"], body["article_ref"], body["decision"], key)
    if parts == ["runs"]:
        run_id = "run_" + digest(key)[:24]
        if (app.runs.folder(run_id) / "plan.json").exists():
            return True, app.planner.create(body["request"], key)
    return False, None
