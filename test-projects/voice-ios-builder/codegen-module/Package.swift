// swift-tools-version: 5.9
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "CodegenModule",
    platforms: [
        .iOS(.v16),
        .macOS(.v13)
    ],
    products: [
        .library(
            name: "CodegenModule",
            targets: ["CodegenModule"]
        ),
        .executable(
            name: "CodegenDemo",
            targets: ["CodegenDemo"]
        )
    ],
    dependencies: [
        // No external dependencies for security reasons
    ],
    targets: [
        .target(
            name: "CodegenModule",
            dependencies: []
        ),
        .executableTarget(
            name: "CodegenDemo",
            dependencies: ["CodegenModule"]
        ),
        .testTarget(
            name: "CodegenModuleTests",
            dependencies: ["CodegenModule"]
        )
    ]
)