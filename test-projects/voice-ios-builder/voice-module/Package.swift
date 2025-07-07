// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "VoiceModule",
    platforms: [
        .iOS(.v15),
        .macOS(.v12)
    ],
    products: [
        .library(
            name: "VoiceModule",
            targets: ["VoiceModule"]
        ),
        .executable(
            name: "TestApp",
            targets: ["TestApp"]
        )
    ],
    dependencies: [
        // Add any external dependencies here if needed
    ],
    targets: [
        .target(
            name: "VoiceModule",
            dependencies: [],
            path: "Sources/VoiceModule"
        ),
        .executableTarget(
            name: "TestApp",
            dependencies: ["VoiceModule"],
            path: "Sources/TestApp"
        ),
        .testTarget(
            name: "VoiceModuleTests",
            dependencies: ["VoiceModule"],
            path: "Tests/VoiceModuleTests"
        )
    ]
)