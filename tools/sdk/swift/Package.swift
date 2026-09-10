// swift-tools-version:5.9
import PackageDescription

// Swift 声明面提取器：用 SwiftParser 纯语法解析 .swiftinterface（快照 L0），
// 逐 public decl 输出 JSONL（kind/name/qualified/signature/@available/行号）。
// 由 tools/extract/apple-swift.ts 编排调用。
let package = Package(
    name: "apple-swift-extract",
    platforms: [.macOS(.v13)],
    dependencies: [
        .package(url: "https://github.com/swiftlang/swift-syntax.git", from: "600.0.0"),
    ],
    targets: [
        .executableTarget(
            name: "apple-swift-extract",
            dependencies: [
                .product(name: "SwiftSyntax", package: "swift-syntax"),
                .product(name: "SwiftParser", package: "swift-syntax"),
            ]
        ),
    ]
)
