"""Shared stage names, platform roles and required review checks."""


PLATFORMS = ("android", "ios", "harmonyos")


STAGES = (*PLATFORMS, "scope", "synthesize", "review", "anchors")


CHECKS = ("coverage", "axis", "boundaries", "granularity", "naming", "anchors", "dispositions")
