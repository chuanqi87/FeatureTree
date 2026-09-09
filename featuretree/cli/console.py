#!/usr/bin/env python3
"""Launch the local FeatureTree management console."""

import argparse

from featuretree.core.storage import ROOT
from featuretree.core.storage import Repository
from featuretree.console.server import create_server


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args(argv)
    web_root = ROOT / "web/dist"
    if not (web_root / "index.html").exists():
        parser.error("前端尚未构建。请先运行：cd web && npm ci && npm run build")
    server = create_server(Repository(), web_root, port=args.port)
    print(f"FeatureTree: http://127.0.0.1:{server.server_port}", flush=True)
    print("Local tree management and node analysis workflows. Press Ctrl+C to stop the console.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
