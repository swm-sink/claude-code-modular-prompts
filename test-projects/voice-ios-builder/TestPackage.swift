// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "VoiceIOSBuilderTests",
    platforms: [
        .iOS(.v16),
        .macOS(.v13)
    ],
    products: [
        .executable(
            name: "SimpleTests",
            targets: ["SimpleTests"]
        )
    ],
    dependencies: [],
    targets: [
        .target(
            name: "VoiceIOSBuilder",
            dependencies: [],
            path: "VoiceIOSBuilder"
        ),
        .executableTarget(
            name: "SimpleTests",
            dependencies: ["VoiceIOSBuilder"],
            path: ".",
            sources: ["SimpleTests.swift"]
        )
    ]
)