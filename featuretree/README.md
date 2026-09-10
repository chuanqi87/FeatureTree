# Python 后端

模块边界及依赖见 docs/architecture/code-map.md。CLI/HTTP 通过 console/application.py 显式装配用例；底层不实例化全局 Repository。正式读取只经过 ReleaseReader，发布只经过 LocalReleaseService。旧实现保存在归档分支。
