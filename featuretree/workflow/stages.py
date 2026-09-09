"""Shared stage names, platform roles and required review checks."""


PLATFORMS = ("android", "ios", "harmonyos")


STAGES = ("scope", *PLATFORMS, "synthesize", "review", "anchors")


CHECKS = ("coverage", "axis", "boundaries", "granularity", "naming", "anchors", "dispositions")
