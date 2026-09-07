#!/usr/bin/env python3
"""Launch the local, read-only FeatureTree browser."""

import argparse

from _bootstrap import ROOT
from featuretree.storage import Repository
from featuretree.viewer_server import create_server


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    web_root = ROOT / "web/dist"
    if not (web_root / "index.html").exists():
        parser.error("前端尚未构建。请先运行：cd web && npm ci && npm run build")
    server = create_server(Repository(), web_root, port=args.port)
    print(f"FeatureTree: http://127.0.0.1:{server.server_port}", flush=True)
    print("Read-only view of authored data and isolated expansion drafts. Press Ctrl+C to stop.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
