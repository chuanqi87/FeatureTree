// Swift 声明面提取器：SwiftParser 纯语法解析 .swiftinterface，逐 public decl 输出 JSONL。
// 输出字段：kind/name/qualified/signature/line/available[]（原始 @available 串，交 TS 侧解析）。
// #if 各分支都递归发符号；extension 成员归被扩展类型；不解释语义，只抽结构 + 签名文本。
import Foundation
import SwiftSyntax
import SwiftParser

struct Rec: Codable {
    let kind: String
    let name: String
    let qualified: String
    let signature: String
    let line: Int
    let available: [String]
    let inherited: [String]  // 继承子句的类型名（基类与协议准绳混合，Swift 语法不可分；TS 侧归入 implements[]）
    let modifiers: [String]
    let attributes: [String]
}

guard CommandLine.arguments.count >= 2 else {
    FileHandle.standardError.write("usage: apple-swift-extract <file.swiftinterface>\n".data(using: .utf8)!)
    exit(2)
}
let path = CommandLine.arguments[1]
guard let text = try? String(contentsOfFile: path, encoding: .utf8) else {
    FileHandle.standardError.write("cannot read \(path)\n".data(using: .utf8)!)
    exit(2)
}
let sourceBytes = Array(text.utf8)
let tree = Parser.parse(source: text)
if tree.hasError {
    FileHandle.standardError.write("SwiftSyntax parse error; file is incomplete\n".data(using: .utf8)!)
    exit(3)
}
let converter = SourceLocationConverter(fileName: path, tree: tree)

var records: [Rec] = []

func collapse(_ s: String) -> String {
    s.trimmingCharacters(in: .whitespacesAndNewlines)
}

// 签名 = decl 起点到 body/成员块 `{` 之间（无 body 则整体），折叠空白。
func headerSig(_ node: some SyntaxProtocol, bodyStart: AbsolutePosition?) -> String {
    let start = node.positionAfterSkippingLeadingTrivia.utf8Offset
    let end = (bodyStart ?? node.endPositionBeforeTrailingTrivia).utf8Offset
    guard start < end, end <= sourceBytes.count else { return collapse(node.trimmedDescription) }
    return collapse(String(decoding: sourceBytes[start..<end], as: UTF8.self))
}

func lineOf(_ node: some SyntaxProtocol) -> Int {
    node.startLocation(converter: converter).line
}

func availabilityStrings(_ attrs: AttributeListSyntax?) -> [String] {
    guard let attrs else { return [] }
    var out: [String] = []
    for a in attrs {
        guard let attr = a.as(AttributeSyntax.self) else { continue }
        if attr.attributeName.trimmedDescription == "available" {
            out.append(collapse(attr.trimmedDescription))
        }
    }
    return out
}

func modifierSet(_ mods: DeclModifierListSyntax?) -> Set<String> {
    guard let mods else { return [] }
    return Set(mods.map { $0.name.text })
}

func emit(_ kind: String, _ name: String, _ context: [String], _ sig: String, _ avail: [String], _ node: some SyntaxProtocol, _ inherited: [String] = []) {
    let qualified = (context + [name]).joined(separator: ".")
    let modifiers = node.asProtocol(WithModifiersSyntax.self)?.modifiers.map { $0.name.text } ?? []
    let attributes = node.asProtocol(WithAttributesSyntax.self)?.attributes.map { $0.trimmedDescription } ?? []
    records.append(Rec(kind: kind, name: name, qualified: qualified, signature: sig, line: lineOf(node), available: avail, inherited: inherited, modifiers: modifiers, attributes: attributes))
}

/// 类型名（去泛型实参，如 `Collection<Int>` → `Collection`；限定名如 `Swift.Equatable` 保留）。
func typeName(_ t: TypeSyntax) -> String {
    if let id = t.as(IdentifierTypeSyntax.self) { return id.name.text }
    return collapse(t.trimmedDescription)
}

/// 继承子句 → 类型名列表。Swift 语法不区分基类与协议准绳（`class Foo: Bar, Baz` 中 Bar 可能是基类或协议），
/// 故全部作为父类型交给 TS 侧归入 implements[]（extends∪implements 即完整父类型集）。
func inheritedNames(_ clause: InheritanceClauseSyntax?) -> [String] {
    guard let clause else { return [] }
    return clause.inheritedTypes.map { typeName($0.type) }
}

func members(of block: MemberBlockSyntax) -> [DeclSyntax] { block.members.map { $0.decl } }

func declsFromElements(_ syntax: Syntax) -> [DeclSyntax] {
    if let list = syntax.as(CodeBlockItemListSyntax.self) {
        return list.compactMap { $0.item.as(DeclSyntax.self) }
    }
    if let list = syntax.as(MemberBlockItemListSyntax.self) {
        return list.map { $0.decl }
    }
    return []
}

func process(_ decls: [DeclSyntax], context: [String]) {
    for decl in decls {
        // #if / #elseif / #else：每个分支都递归（都是真 API）
        if let ifc = decl.as(IfConfigDeclSyntax.self) {
            for clause in ifc.clauses {
                if let el = clause.elements { process(declsFromElements(Syntax(el)), context: context) }
            }
            continue
        }
        handle(decl, context: context)
    }
}

func handle(_ decl: DeclSyntax, context: [String]) {
    switch decl.kind {
    case .structDecl:
        let n = decl.cast(StructDeclSyntax.self)
        emitType(n.name.text, "struct", n.attributes, n.modifiers, n.memberBlock, n, context, inheritedNames(n.inheritanceClause))
    case .classDecl:
        let n = decl.cast(ClassDeclSyntax.self)
        emitType(n.name.text, "class", n.attributes, n.modifiers, n.memberBlock, n, context, inheritedNames(n.inheritanceClause))
    case .actorDecl:
        let n = decl.cast(ActorDeclSyntax.self)
        emitType(n.name.text, "class", n.attributes, n.modifiers, n.memberBlock, n, context, inheritedNames(n.inheritanceClause))
    case .enumDecl:
        let n = decl.cast(EnumDeclSyntax.self)
        emitType(n.name.text, "enum", n.attributes, n.modifiers, n.memberBlock, n, context, inheritedNames(n.inheritanceClause))
    case .protocolDecl:
        let n = decl.cast(ProtocolDeclSyntax.self)
        emitType(n.name.text, "interface", n.attributes, n.modifiers, n.memberBlock, n, context, inheritedNames(n.inheritanceClause))
    case .extensionDecl:
        let n = decl.cast(ExtensionDeclSyntax.self)
        // extension 本身不发符号；成员归被扩展类型
        let ext = collapse(n.extendedType.trimmedDescription)
        process(members(of: n.memberBlock), context: context.isEmpty ? [ext] : context + [ext])
    case .functionDecl:
        let n = decl.cast(FunctionDeclSyntax.self)
        let kind = context.isEmpty ? "function" : "method"
        emit(kind, n.name.text, context, headerSig(n, bodyStart: n.body?.position), availabilityStrings(n.attributes), n)
    case .initializerDecl:
        let n = decl.cast(InitializerDeclSyntax.self)
        emit("constructor", "init", context, headerSig(n, bodyStart: n.body?.position), availabilityStrings(n.attributes), n)
    case .subscriptDecl:
        let n = decl.cast(SubscriptDeclSyntax.self)
        emit("method", "subscript", context, headerSig(n, bodyStart: n.accessorBlock?.position), availabilityStrings(n.attributes), n)
    case .variableDecl:
        let n = decl.cast(VariableDeclSyntax.self)
        let mods = modifierSet(n.modifiers)
        let isConst = context.isEmpty || mods.contains("static") || mods.contains("class")
        for b in n.bindings {
            guard let idp = b.pattern.as(IdentifierPatternSyntax.self) else { continue }
            let name = idp.identifier.text
            emit(isConst ? "constant" : "field", name, context, headerSig(n, bodyStart: b.accessorBlock?.position), availabilityStrings(n.attributes), n)
        }
    case .typeAliasDecl:
        let n = decl.cast(TypeAliasDeclSyntax.self)
        emit("type", n.name.text, context, headerSig(n, bodyStart: nil), availabilityStrings(n.attributes), n)
    case .associatedTypeDecl:
        let n = decl.cast(AssociatedTypeDeclSyntax.self)
        emit("type", n.name.text, context, headerSig(n, bodyStart: nil), availabilityStrings(n.attributes), n)
    case .enumCaseDecl:
        let n = decl.cast(EnumCaseDeclSyntax.self)
        let avail = availabilityStrings(n.attributes)
        for el in n.elements {
            emit("enum-member", el.name.text, context, collapse(el.trimmedDescription), avail, n)
        }
    case .macroDecl:
        let n = decl.cast(MacroDeclSyntax.self)
        emit("macro", n.name.text, context, headerSig(n, bodyStart: n.definition?.position), availabilityStrings(n.attributes), n)
    default:
        break
    }
}

func emitType(_ name: String, _ kind: String, _ attrs: AttributeListSyntax?, _ mods: DeclModifierListSyntax?,
              _ block: MemberBlockSyntax, _ node: some SyntaxProtocol, _ context: [String], _ inherited: [String] = []) {
    emit(kind, name, context, headerSig(node, bodyStart: block.position), availabilityStrings(attrs), node, inherited)
    process(members(of: block), context: context + [name])
}

process(tree.statements.compactMap { $0.item.as(DeclSyntax.self) }, context: [])

let encoder = JSONEncoder()
encoder.outputFormatting = [.withoutEscapingSlashes]
var buf = Data()
for r in records {
    buf.append(try! encoder.encode(r))
    buf.append(0x0a)
}
FileHandle.standardOutput.write(buf)
