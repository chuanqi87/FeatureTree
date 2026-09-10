"""Readable exports contain only already assessed assertions and their provenance."""


def article_markdown(projection, title):
    article = projection["article"]
    lines = [f"# {title}", "", f"发布版本：{projection['release_id']}",
             f"知识对象：{projection['article_ref']}",
             f"可信度：{article['overall_confidence']}；有效性：{projection['summary']['validity']}", ""]
    assessments = {row["claim_id"]: row for row in article["assessments"]}
    evidence = {row["id"]: row for row in article["evidence"]}
    for claim in article["claims"]:
        rating = assessments[claim["claim_id"]]
        lines.extend([f"## {' / '.join(claim['platforms'])} · {claim['dimension']}", "",
            f"{claim['statement']}", "", f"结论：{claim['result']}；可信度：{rating['level']}",
            f"结论 ID：{claim['claim_id']}", ""])
        for name, label in (("conditions", "条件"), ("alternative_paths", "替代路线"), ("gaps", "缺口"), ("premise_ids", "关键前提")):
            if claim[name]:
                lines.append(f"{label}：" + "；".join(claim[name]))
                lines.append("")
        if claim["coverage_note"]:
            lines.extend(["检查范围：" + claim["coverage_note"], ""])
        for reference in claim["evidence_refs"]:
            source = evidence[reference]
            lines.extend([f"依据 [{reference}]({source['url']})（正文 SHA-256：{source['body_sha256']}）", ""])
    return "\n".join(lines)
