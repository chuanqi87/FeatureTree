# 命令兼容入口

这里的 Python 文件都是薄入口，业务代码在 `featuretree/cli/` 及对应领域包。旧命令继续可用，新增逻辑不要放在此目录。

推荐从统一命令查看用途：

```bash
.venv/bin/python -m featuretree --help
.venv/bin/python -m featuretree workflow --help
.venv/bin/python -m featuretree console
```

完整的 [命令对照和代码地图](../docs/architecture/code-map.md)。`_bootstrap.py` 只让从任意目录执行旧脚本时能够找到项目包。
