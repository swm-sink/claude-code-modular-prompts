// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "VoiceIOSBuilder",
    platforms: [
        .iOS(.v16),
        .macOS(.v13)
    ],
    products: [
        .library(
            name: "VoiceIOSBuilder",
            targets: ["VoiceIOSBuilder"]
        ),
        .executable(
            name: "VoiceIOSBuilderDemo",
            targets: ["VoiceIOSBuilderDemo"]
        )
    ],
    dependencies: [
        // Add any external dependencies here if needed
    ],
    targets: [
        // Core App Target
        .target(
            name: "VoiceIOSBuilder",
            dependencies: [
                "VoiceModule",
                "CodegenModule", 
                "SimulatorModule"
            ],
            path: "VoiceIOSBuilder"
        ),
        
        // Voice Recognition Module
        .target(
            name: "VoiceModule",
            dependencies: [],
            path: "voice-module/Sources/VoiceModule"
        ),
        
        // Code Generation Module
        .target(
            name: "CodegenModule", 
            dependencies: [],
            path: "codegen-module/Sources/CodegenModule"
        ),
        
        // Simulator Integration Module
        .target(
            name: "SimulatorModule",
            dependencies: [],
            path: "simulator-module/Sources/SimulatorModule"
        ),
        
        // Demo App
        .executableTarget(
            name: "VoiceIOSBuilderDemo",
            dependencies: ["VoiceIOSBuilder"],
            path: "Demo",
            sources: ["main.swift"]
        ),
        
        // Tests
        .testTarget(
            name: "VoiceIOSBuilderTests",
            dependencies: [
                "VoiceIOSBuilder",
                "VoiceModule",
                "CodegenModule",
                "SimulatorModule"
            ],
            path: "Tests"
        )
    ]
)