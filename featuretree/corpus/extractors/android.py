"""Android api-versions.xml adapter, retaining removed entries as explicit dispositions."""

from lxml import etree


def extract(path, options):
    try:
        tree = etree.parse(str(path))
    except etree.XMLSyntaxError as error:
        return [], [str(error)]
    records = []
    for owner in tree.findall("class"):
        name = owner.attrib["name"].replace("/", ".").replace("$", ".")
        removed = owner.get("removed")
        for member in [owner, *list(owner)]:
            if member.tag not in ("class", "method", "field"):
                continue
            raw_name = member.attrib.get("name", "")
            member_name = raw_name.split("(", 1)[0]
            qualified = name if member is owner else name + "." + member_name
            signature = "class " + name if member is owner else raw_name
            availability = {"since": member.get("since", owner.get("since")),
                            "removed": member.get("removed", removed),
                            "deprecated_since": member.get("deprecated", owner.get("deprecated")),
                            "module_id": name.rsplit(".", 1)[0],
                            "sdk_extensions": member.get("sdks", owner.get("sdks")),
                            "inherited_types": [child.get("name") for child in owner if child.tag in ("extends", "implements")]}
            records.append({"qualified_name": qualified, "signature": signature,
                            "kind": member.tag, "visibility": "nonpublic" if availability["removed"] else "public",
                            "availability": availability, "source_line": member.sourceline or 0, "documentation": ""})
    return records, []
