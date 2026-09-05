"""Extract directory records from local source documents; do not infer SDK baselines."""

from __future__ import annotations

import json
import re

from .inventory import prepare_row
from .storage import ROOT, write_json

RAW = ROOT / "docs-raw"
BASE = dict.fromkeys(("android", "ios", "harmonyos"), "unversioned local mirror")


def entry(**kwargs) -> dict:
    kwargs.setdefault("parent", None)
    kwargs.setdefault("url", "")
    kwargs.setdefault("layer", "os")
    kwargs.setdefault("visibility", "public")
    kwargs.setdefault("mappings", [])
    kwargs.setdefault("notes", "")
    return kwargs


def harvest_android() -> list[dict]:
    rows: list[dict] = []
    pkg_md = RAW / "android" / "packages-index.md"
    text = pkg_md.read_text(encoding="utf-8", errors="ignore")
    # Prefer linked package names
    pkgs = sorted(set(re.findall(r"\[((?:android|androidx|java|javax|dalvik|kotlin|org\.xmlpull)[\w.]*)\]", text)))
    if not pkgs:
        pkgs = sorted(set(re.findall(r"\b((?:android|androidx)\.[\w.]+)\b", text)))
    for p in pkgs:
        layer = "os"
        vis = "public"
        # coarse filter: skip annotation-only noise later in mapping
        rows.append(
            entry(
                native_id=p,
                platform="android",
                title=p,
                kind="package",
                version=BASE["android"],
                url=f"https://developer.android.com/reference/{p.replace('.', '/')}/package-summary",
                layer=layer,
                visibility=vis,
                notes="harvested from packages-index.md",
            )
        )

    # Guide sitemap topics (english, no hl=)
    sm = RAW / "maps" / "android-guide-sitemap.txt"
    if sm.exists():
        for line in sm.read_text(encoding="utf-8", errors="ignore").splitlines():
            url = line.strip()
            if not url.startswith("http"):
                continue
            if "hl=" in url:
                continue
            if "/guide/" not in url:
                continue
            # path after /guide/
            path = url.split("/guide/", 1)[1].split("?", 1)[0].strip("/")
            if not path:
                continue
            top = path.split("/")[0]
            rows.append(
                entry(
                    native_id=f"guide:{path}",
                    platform="android",
                    title=path,
                    parent=f"guide:{top}" if "/" in path else None,
                    kind="guide",
                    version=BASE["android"],
                    url=url.split("?", 1)[0],
                    notes="harvested from android-guide-sitemap",
                )
            )
    return rows


def harvest_ios() -> list[dict]:
    roots = RAW / "ios/framework-roots.txt"
    names = sorted(set(line.strip() for line in roots.read_text().splitlines() if line.strip()))
    rows = []
    for name in names:
        page = RAW / "ios/frameworks" / (name.lower() + ".md")
        rows.append(entry(native_id=name, platform="ios", title=name, kind="framework",
                          version=BASE["ios"], url=f"https://developer.apple.com/documentation/{name.lower()}",
                          notes="Apple documentation catalog" + ("; local landing page available" if page.exists() else "")))
    return rows


def harvest_harmony() -> list[dict]:
    rows: list[dict] = []
    kit_dirs = RAW / "harmonyos" / "api-index" / "kit-dirs.txt"
    kits = [ln.strip() for ln in kit_dirs.read_text().splitlines() if ln.strip()]
    kit_files = RAW / "harmonyos" / "api-index" / "kits"

    module_re = re.compile(r"`?(@ohos\.[\w.]+|@kit\.[\w.]+)`?")

    for kit in kits:
        kit_name = kit.removeprefix("apis-")
        rows.append(
            entry(
                native_id=kit,
                platform="harmonyos",
                title=kit_name,
                kind="kit",
                version=BASE["harmonyos"],
                url=f"https://github.com/openharmony/docs/tree/master/zh-cn/application-dev/reference/{kit}",
                notes="OpenHarmony reference kit directory",
            )
        )
        readme = kit_files / f"{kit}-Readme-CN.md"
        if not readme.exists():
            readme = kit_files / f"{kit}-Readme.md"
        if not readme.exists():
            continue
        text = readme.read_text(encoding="utf-8", errors="ignore")
        modules = sorted(set(module_re.findall(text)))
        # Also capture js-apis / arkts-apis filenames as module proxies
        file_mods = sorted(
            set(
                re.findall(
                    r"\[([^\]]+)\]\((?:\.\/)?((?:js|arkts)-apis[\w\-]*\.md)\)",
                    text,
                )
            )
        )
        for mod in modules:
            links = sorted(fname for title, fname in file_mods if mod in title)
            public_links = [name for name in links if "-sys.md" not in name]
            selected = (public_links or links or [None])[0]
            module_url = (f"https://github.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/{kit}/{selected}"
                          if selected else f"https://github.com/openharmony/docs/tree/master/zh-cn/application-dev/reference/{kit}")
            rows.append(
                entry(
                    native_id=mod,
                    platform="harmonyos",
                    title=mod,
                    parent=kit,
                    kind="module",
                    version=BASE["harmonyos"],
                    visibility="system" if links and not public_links else "public",
                    url=module_url,
                    notes=f"extracted from {readme.name}",
                )
            )
        for title, fname in file_mods:
            nid = f"{kit}/{fname}"
            rows.append(
                entry(
                    native_id=nid,
                    platform="harmonyos",
                    title=title.strip(),
                    parent=kit,
                    kind="module",
                    version=BASE["harmonyos"],
                    url=f"https://github.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/{kit}/{fname}",
                    notes=f"readme link in {readme.name}",
                )
            )
    return rows


def dedupe(rows: list[dict]) -> list[dict]:
    seen = set()
    out = []
    for r in rows:
        key = (r["platform"], r["native_id"])
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def harvest():
    catalogs = {"android": dedupe(harvest_android()), "ios": dedupe(harvest_ios()),
                "harmonyos": dedupe(harvest_harmony())}
    for platform, fresh in catalogs.items():
        path = ROOT / f"inventory/{platform}/catalog.json"
        old = {r["native_id"]: r for r in json.loads(path.read_text())} if path.exists() else {}
        rows = [prepare_row(row, ROOT, old.get(row["native_id"])) for row in fresh]
        present = {r["native_id"] for r in rows}
        # A missing harvested record is a review item, never an implicit deletion.
        for native, previous in old.items():
            if native not in present:
                retained = dict(previous)
                retained.update(scope="pending", scope_reason="当前采集未再发现；保留映射与人工记录待复核")
                rows.append(retained)
        write_json(path, rows)
    write_json(ROOT / "inventory/harvest_meta.json", {
        "source": "docs-raw", "version_policy": "No fixed SDK version inferred from a live documentation index",
        "catalog_counts": {p: len(rows) for p, rows in catalogs.items()},
    })
    return {p: len(rows) for p, rows in catalogs.items()}
