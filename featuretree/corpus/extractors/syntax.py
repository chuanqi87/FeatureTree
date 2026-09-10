"""Process adapters for TypeScript/ArkTS AST and SwiftParser, with explicit failures."""

import json
import re
from pathlib import Path
import subprocess


def arkts(path, options):
    parser = options["project_root"] / "tools/sdk/arkts.mjs"
    result = subprocess.run(["node", str(parser), str(path)], capture_output=True, text=True, timeout=120)
    if result.returncode:
        return [], [result.stderr.strip() or "ArkTS parser failed"]
    output = json.loads(result.stdout)
    for record in output["records"]:
        record["qualified_name"] = options["module"] + "." + record["qualified_name"]
        record["availability"]["module_id"] = options["module"]
    return output["records"], output["diagnostics"]


def swift(path, options):
    executable = options["project_root"] / "tools/sdk/swift/.build/release/apple-swift-extract"
    if not executable.exists():
        return [], ["SwiftParser executable missing: swift build -c release --package-path tools/sdk/swift"]
    result = subprocess.run([str(executable), str(path)], capture_output=True, text=True, timeout=120)
    if result.returncode:
        return [], [result.stderr.strip() or "SwiftParser failed"]
    records, contexts = [], {}
    for line in result.stdout.splitlines():
        original = json.loads(line)
        signature = original["signature"]
        parent_name = original["qualified"].rsplit(".", 1)[0] if "." in original["qualified"] else ""
        parent = contexts.get(parent_name, {})
        modifiers = set(original["modifiers"])
        private = bool(modifiers & {"private", "fileprivate", "internal", "package"})
        private |= any(attribute.startswith("@_spi") for attribute in original["attributes"])
        private |= parent.get("visibility") == "nonpublic" or "PrivateHeaders" in path.parts
        explicit_public = bool(modifiers & {"public", "open"})
        implicit_public = parent.get("kind") in ("interface", "enum") and parent.get("visibility") == "public"
        visibility = "nonpublic" if private else "public" if explicit_public or implicit_public else "unknown"
        records.append({"qualified_name": options["module"] + "." + original["qualified"],
                        "signature": original["signature"], "kind": original["kind"],
                        "visibility": visibility, "availability": {"available": [*parent.get("available", []), *original["available"]],
                        "inherited": original["inherited"], "module_id": options["module"],
                        "conditional_compilation": "branches preserved; applicability requires audit"},
                        "source_line": original["line"], "documentation": ""})
        contexts[original["qualified"]] = {"kind": original["kind"], "visibility": visibility,
                                            "available": records[-1]["availability"]["available"]}
    return records, []
