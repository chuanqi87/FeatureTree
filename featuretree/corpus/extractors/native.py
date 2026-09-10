"""Clang declaration extraction for C/C++ and Apple Objective-C SDK headers."""

from pathlib import Path


def extract(path, options):
    import clang.cindex as clang
    language = options.get("language", "c")
    args = ["-x", {"objc": "objective-c", "cpp": "c++"}.get(language, "c"),
            "-I", str(options["sdk_root"]), *options.get("clang_args", [])]
    translation = clang.Index.create().parse(str(path), args=args,
                                            options=clang.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD)
    failures = [str(diagnostic) for diagnostic in translation.diagnostics if diagnostic.severity >= clang.Diagnostic.Error]
    kinds = {"FUNCTION_DECL": "function", "CXX_METHOD": "method", "CONSTRUCTOR": "constructor",
             "OBJC_INSTANCE_METHOD_DECL": "method", "OBJC_CLASS_METHOD_DECL": "method",
             "OBJC_INTERFACE_DECL": "class", "OBJC_PROTOCOL_DECL": "interface",
             "OBJC_PROPERTY_DECL": "property", "STRUCT_DECL": "struct", "UNION_DECL": "union",
             "CLASS_DECL": "class", "ENUM_DECL": "enum", "ENUM_CONSTANT_DECL": "enum_member",
             "FIELD_DECL": "field", "VAR_DECL": "variable", "TYPEDEF_DECL": "type",
             "TYPE_ALIAS_DECL": "type", "MACRO_DEFINITION": "macro"}
    records = []
    for cursor in translation.cursor.walk_preorder():
        if not cursor.location.file:
            continue
        if Path(cursor.location.file.name).resolve() != path.resolve():
            continue  # Include-expanded declarations belong to their own inventoried source file.
        # libclang 18's Python enum omits several public C attribute constants,
        # including FlagEnum=437. Attributes are metadata, not API declarations.
        # https://clang.llvm.org/doxygen/group__CINDEX.html
        if 400 <= cursor._kind_id <= 441:
            continue
        try:
            kind = cursor.kind.name
        except ValueError as error:
            failures.append(f"{path.name}:{cursor.location.line}: {error}")
            continue
        if kind not in kinds or not cursor.spelling:
            continue
        parents, parent = [], cursor.semantic_parent
        while parent and parent.kind.name != "TRANSLATION_UNIT":
            if parent.spelling:
                parents.append(parent.spelling)
            parent = parent.semantic_parent
        qualified = ".".join([options["module"], *reversed(parents), cursor.spelling])
        signature = cursor.type.spelling or cursor.displayname
        if kind in ("MACRO_DEFINITION", "TYPEDEF_DECL", "TYPE_ALIAS_DECL"):
            signature = " ".join(token.spelling for token in cursor.get_tokens())
        availability = str(cursor.availability).split(".")[-1].lower()
        private = cursor.access_specifier in (clang.AccessSpecifier.PRIVATE, clang.AccessSpecifier.PROTECTED)
        private |= any(segment in path.parts for segment in ("PrivateHeaders", "private", "@internal"))
        visibility = "nonpublic" if private or availability in ("not_accessible", "not_available") else "public"
        if failures and visibility == "public":
            visibility = "unknown"
        records.append({"qualified_name": qualified, "signature": signature, "kind": kinds[kind],
                        "visibility": visibility, "availability": {"clang_availability": availability,
                        "clang_usr": cursor.get_usr(), "module_id": options["module"],
                        "target": options.get("clang_args", []), "requires_platform_availability_audit": language == "objc"},
                        "source_line": cursor.location.line, "documentation": cursor.raw_comment or ""})
    if failures:
        records = [{**row, "visibility": "unknown" if row["visibility"] == "public" else row["visibility"]} for row in records]
    return records, failures
