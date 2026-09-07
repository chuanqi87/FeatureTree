"""Shared emitter for author_*.py scripts (build-time only)."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
NEW = {"disposition": "new", "sources": []}


def kept(srcs):
    return {"disposition": "kept", "sources": srcs}


def renamed(srcs):
    return {"disposition": "renamed_from", "sources": srcs}


def merged(srcs):
    return {"disposition": "merged_from", "sources": srcs}


def L(fid, parent, axis, zh, en, definition, includes, excludes, a, i, h, leg=None, priv="none", level="L3"):
    return (fid, parent, axis, zh, en, definition, includes, excludes, a, i, h, leg or NEW, priv, level)


def emit(name, axis, l1, l2_list, leaves_by_parent):
    lines = []
    lines.append("#!/usr/bin/env python3")
    lines.append(f'"""Author the {name} domain taxonomy."""')
    lines.append("")
    lines.append("import _bootstrap  # noqa: F401")
    lines.append("from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain")
    lines.append("")
    lines.append("")
    lines.append("def A(symbol, url, kind=\"class\"):")
    lines.append("    return bind(\"android\", kind, symbol, url)")
    lines.append("")
    lines.append("")
    lines.append("def I(symbol, url, kind=\"framework\"):")
    lines.append("    return bind(\"ios\", kind, symbol, url)")
    lines.append("")
    lines.append("")
    lines.append("def H(symbol, url, kind=\"module\"):")
    lines.append("    return bind(\"harmonyos\", kind, symbol, url)")
    lines.append("")
    lines.append("")
    lines.append(f'AXIS_L2 = "{axis}"')
    lines.append("")
    lines.append("")
    lines.append("def B(a=None, i=None, h=None):")
    lines.append("    parts = []")
    lines.append("    if a:")
    lines.append("        parts.append(A(a[0], a[1], a[2] if len(a) > 2 else \"class\"))")
    lines.append("    else:")
    lines.append("        parts.append(pending(\"android\"))")
    lines.append("    if i:")
    lines.append("        parts.append(I(i[0], i[1], i[2] if len(i) > 2 else \"framework\"))")
    lines.append("    else:")
    lines.append("        parts.append(pending(\"ios\"))")
    lines.append("    if h:")
    lines.append("        parts.append(H(h[0], h[1], h[2] if len(h) > 2 else \"module\"))")
    lines.append("    else:")
    lines.append("        parts.append(pending(\"harmonyos\"))")
    lines.append("    return merge_bindings(*parts)")
    lines.append("")
    lines.append("")
    lines.append("def leaf(f, fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy=None, level=\"L3\", privacy=\"none\"):")
    lines.append("    f.append(feature(")
    lines.append("        fid, parent=parent, level=level, zh=zh, en=en, definition=definition,")
    lines.append("        includes=includes, excludes=excludes, sibling_axis=axis,")
    lines.append("        granularity=\"atomic\", bindings=bindings,")
    lines.append("        legacy=legacy or {\"disposition\": \"new\", \"sources\": []},")
    lines.append("        privacy_class=privacy,")
    lines.append("    ))")
    lines.append("")
    lines.append("")
    lines.append("def build() -> list[dict]:")
    lines.append("    f: list[dict] = []")
    zh, en, definition, includes, excludes, legacy = l1
    lines.append("    f.append(feature(")
    lines.append(f'        "{name}", parent=None, level="L1",')
    lines.append(f'        zh="{zh}", en="{en}",')
    lines.append(f'        definition="{definition}",')
    lines.append(f"        includes={includes!r},")
    lines.append(f"        excludes={excludes!r},")
    lines.append(f"        legacy={legacy!r},")
    lines.append("    ))")
    lines.append("    l2 = [")
    for item in l2_list:
        lines.append(f"        {item!r},")
    lines.append("    ]")
    lines.append("    for fid, zh, en, definition, includes, excludes, sources in l2:")
    lines.append("        f.append(feature(")
    lines.append(f'            fid, parent="{name}", level="L2", zh=zh, en=en, definition=definition,')
    lines.append("            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,")
    lines.append('            legacy={"disposition": "kept" if sources else "new", "sources": sources},')
    lines.append("        ))")
    lines.append("")
    for parent, axis, rows in leaves_by_parent:
        lines.append(f"    # --- {parent} ---")
        for row in rows:
            if row[0] == "BRANCH":
                _, fid, zh, en, definition, includes, excludes, leg = row
                lines.append("    f.append(feature(")
                lines.append(f'        "{fid}", parent="{parent}", level="L3",')
                lines.append(f'        zh="{zh}", en="{en}", definition="{definition}",')
                lines.append(f"        includes={includes!r}, excludes={excludes!r}, sibling_axis=\"{axis}\",")
                lines.append(f"        legacy={leg!r},")
                lines.append("    ))")
            else:
                fid, p, ax, zh, en, definition, includes, excludes, a, i, h, leg, priv, level = row
                lines.append(f'    leaf(f, "{fid}", "{p}", "{ax}", "{zh}", "{en}",')
                lines.append(f'         "{definition}", {includes!r}, {excludes!r},')
                lines.append(f'         B({a!r}, {i!r}, {h!r}), {leg!r}, level="{level}", privacy="{priv}")')
        lines.append("")
    lines.append("    return f")
    lines.append("")
    lines.append("")
    lines.append("def main():")
    lines.append("    nodes = build()")
    lines.append("    dedup = {}")
    lines.append("    for node in nodes:")
    lines.append("        dedup[node[\"id\"]] = node")
    lines.append("    nodes = list(dedup.values())")
    lines.append(f'    path = write_domain("{name}", nodes)')
    lines.append('    print(f"wrote {len(nodes)} nodes -> {path}")')
    lines.append("")
    lines.append("")
    lines.append('if __name__ == "__main__":')
    lines.append("    main()")
    lines.append("")
    path = ROOT / f"author_{name}.py"
    path.write_text("\n".join(lines))
    print("wrote", path)
