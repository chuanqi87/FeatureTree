// Adapted from harmony-knowledge's TypeScript AST approach; no SDK version or path is hardcoded.
import ts from 'typescript';
import fs from 'node:fs';
const path = process.argv[2];
const original = fs.readFileSync(path, 'utf8');
const source = ts.createSourceFile(path, original.replace(/\bcomponent\s+(?=\w)/g, 'interface ').replace(/\bstruct\s+(?=\w)/g, 'class '), ts.ScriptTarget.Latest, true, ts.ScriptKind.TS);
const records = [];
function visit(node, parents = [], inheritedPrivate = false, inheritedTags = []) {
  const tags = ts.getJSDocTags(node).map(tag => ({ name: tag.tagName.text, value: typeof tag.comment === 'string' ? tag.comment : '' }));
  const allTags = [...inheritedTags, ...tags];
  const flags = ts.getCombinedModifierFlags(node);
  const privateApi = inheritedPrivate || !!(flags & (ts.ModifierFlags.Private | ts.ModifierFlags.Protected)) || allTags.some(tag => ['systemapi','internal'].includes(tag.name)) || path.includes('/@internal/');
  let kind = null;
  if (ts.isClassDeclaration(node)) kind = 'class';
  else if (ts.isInterfaceDeclaration(node)) kind = 'interface';
  else if (ts.isEnumDeclaration(node)) kind = 'enum';
  else if (ts.isEnumMember(node)) kind = 'enum_member';
  else if (ts.isFunctionDeclaration(node)) kind = 'function';
  else if (ts.isMethodDeclaration(node) || ts.isMethodSignature(node)) kind = 'method';
  else if (ts.isConstructorDeclaration(node)) kind = 'constructor';
  else if (ts.isPropertyDeclaration(node) || ts.isPropertySignature(node) || ts.isGetAccessor(node) || ts.isSetAccessor(node)) kind = 'property';
  else if (ts.isTypeAliasDeclaration(node)) kind = 'type';
  else if (ts.isVariableDeclaration(node)) kind = 'variable';
  const name = ts.isConstructorDeclaration(node) ? 'constructor' : node.name?.getText(source);
  if (kind && name) {
    let end = node.end;
    if (node.members) end = source.text.indexOf('{', node.getStart(source));
    else if (node.body) end = node.body.getStart(source);
    const signature = source.text.slice(node.getStart(source), end < node.getStart(source) ? node.end : end).trim();
    records.push({ qualified_name: [...parents, name].join('.'), signature, kind, visibility: privateApi ? 'nonpublic' : 'public', availability: { tags: allTags, since: allTags.find(tag => tag.name === 'since')?.value || null }, source_line: source.getLineAndCharacterOfPosition(node.getStart(source)).line + 1, documentation: (node.jsDoc || []).map(doc => doc.getText(source)).join('\n') });
  }
  const container = ts.isModuleDeclaration(node) || ts.isClassDeclaration(node) || ts.isInterfaceDeclaration(node) || ts.isEnumDeclaration(node);
  const context = container && name ? [...parents, name] : parents;
  if (container || ts.isSourceFile(node) || ts.isModuleBlock(node) || ts.isVariableStatement(node) || ts.isVariableDeclarationList(node)) ts.forEachChild(node, child => visit(child, context, privateApi, allTags));
}
visit(source);
process.stdout.write(JSON.stringify({ records, diagnostics: source.parseDiagnostics.map(error => ts.flattenDiagnosticMessageText(error.messageText, '\n')) }));
