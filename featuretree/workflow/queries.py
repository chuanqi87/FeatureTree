"""Turn verbose scope hints into bounded search keys while retaining their originals."""

import re

GENERAL = {"android", "ios", "harmonyos", "api", "sdk", "public", "reference", "framework",
           "google", "play", "services", "development", "kit"}


def compact_query(query):
    modules = re.findall(r"@?[a-z]\w*(?:\.[A-Za-z_]\w*)+", query)
    symbols = [word for word in re.findall(r"\b[A-Z][A-Za-z0-9_]+\b", query)
               if len(re.findall("[A-Z]", word)) >= 2 and any(c.islower() for c in word)
               and not word.endswith(("Kit", "OS"))]
    phrases = [word for word in re.findall(r"[\u4e00-\u9fff]+", query)
               if 4 <= len(word) <= 12 and word not in {"接口参考", "开发指南"}]
    if modules or symbols or phrases:
        return (modules + symbols + phrases)[0]
    words = query.split()
    if len(words) <= 8:
        return query
    selected, seen = [], set()
    for word in words:
        key = word.casefold()
        if key not in GENERAL and key not in seen and len(key) > 2:
            selected.append(word)
            seen.add(key)
    return " ".join(selected[:2]) or query
