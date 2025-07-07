// swift-tools-version: 5.9
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "SimulatorModule",
    platforms: [
        .macOS(.v13)
    ],
    products: [
        .library(
            name: "SimulatorModule",
            targets: ["SimulatorModule"]),
    ],
    dependencies: [
        // Dependencies declare other packages that this package depends on.
    ],
    targets: [
        .target(
            name: "SimulatorModule",
            dependencies: []),
        .testTarget(
            name: "SimulatorModuleTests",
            dependencies: ["SimulatorModule"]),
    ]
)