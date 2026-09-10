"""The only write tool: immutable payload fragments inside the current attempt."""

import argparse
import json
from pathlib import Path
import sys

from featuretree.core.content import digest
from featuretree.core.io import read_json
from featuretree.workflow.backends.delivery import save_chunk, finalize_delivery
from featuretree.workflow.implementation import verify_implementation


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", type=Path, required=True)
    args = parser.parse_args()
    packet = read_json(args.packet)
    if digest({key: value for key, value in packet.items() if key != "input_hash"}) != packet["input_hash"]:
        raise ValueError("Payload tool packet was modified")
    verify_implementation(packet["stage_id"], packet.get("implementation_files"))
    request = json.load(sys.stdin)
    if "chunk_refs" in request:
        result = finalize_delivery(args.packet.parent, packet, request["chunk_refs"], request["outcome"],
                                   json.loads(request["issues_json"]), json.loads(request["source_requests_json"]))
    else:
        result = save_chunk(args.packet.parent, packet, request["path"], json.loads(request["value_json"]))
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
