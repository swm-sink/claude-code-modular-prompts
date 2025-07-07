import Foundation

// MARK: - Module Entry Point

@available(macOS 13.0, *)
public final class SimulatorModule {
    
    public static let shared = SimulatorModule()
    
    public let simulatorManager: SimulatorManager
    public let buildValidator: BuildValidator
    public let screenshotCapture: ScreenshotCapture
    
    private init() {
        self.simulatorManager = SimulatorManager()
        self.buildValidator = BuildValidator()
        self.screenshotCapture = ScreenshotCapture()
    }
    
    // MARK: - Convenience Methods
    
    /// Complete build-deploy-capture automation cycle
    public func automatedBuildAndTest(
        projectPath: String,
        scheme: String,
        configuration: String = "Debug",
        testCaseName: String,
        screenshotsDirectory: String
    ) async throws -> AutomationResult {
        
        // 1. Validate build environment
        let environmentValid = try await buildValidator.validateXcodeBuildEnvironment()
        guard environmentValid else {
            throw BuildError.xcodebuildNotFound
        }
        
        // 2. Get available simulators
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let targetSimulator = simulators.first else {
            throw SimulatorError.simulatorNotFound
        }
        
        // 3. Launch simulator
        _ = try await simulatorManager.launchSimulator(udid: targetSimulator.udid)
        
        // 4. Build app
        let buildResult = try await buildValidator.buildAppForSimulator(
            projectPath: projectPath,
            scheme: scheme,
            configuration: configuration
        )
        
        guard buildResult.success else {
            throw BuildError.buildFailed("Build failed: \(buildResult.buildLog)")
        }
        
        // 5. Deploy app
        let deployResult = try await buildValidator.deployAppToSimulator(
            appPath: buildResult.appPath,
            simulatorUDID: targetSimulator.udid
        )
        
        guard deployResult.success else {
            throw BuildError.deploymentFailed("Deployment failed: \(deployResult.deployLog)")
        }
        
        // 6. Launch app
        let launchResult = try await buildValidator.launchAppOnSimulator(
            bundleIdentifier: deployResult.bundleIdentifier,
            simulatorUDID: targetSimulator.udid
        )
        
        guard launchResult.success else {
            throw BuildError.launchFailed("Launch failed: \(launchResult.launchLog)")
        }
        
        // 7. Wait for app to be ready
        try await Task.sleep(nanoseconds: 2_000_000_000) // 2 seconds
        
        // 8. Capture screenshots
        let screenshotPaths = try await screenshotCapture.captureScreenshots(
            simulatorUDID: targetSimulator.udid,
            count: 3,
            interval: 1.0,
            outputDirectory: screenshotsDirectory
        )
        
        // 9. Cleanup - shutdown simulator
        _ = try await simulatorManager.shutdownSimulator(udid: targetSimulator.udid)
        
        return AutomationResult(
            buildResult: buildResult,
            deployResult: deployResult,
            launchResult: launchResult,
            screenshotPaths: screenshotPaths,
            simulatorUsed: targetSimulator
        )
    }
}

// MARK: - Automation Result

public struct AutomationResult {
    public let buildResult: BuildResult
    public let deployResult: DeployResult
    public let launchResult: LaunchResult
    public let screenshotPaths: [String]
    public let simulatorUsed: Simulator
    
    public init(
        buildResult: BuildResult,
        deployResult: DeployResult,
        launchResult: LaunchResult,
        screenshotPaths: [String],
        simulatorUsed: Simulator
    ) {
        self.buildResult = buildResult
        self.deployResult = deployResult
        self.launchResult = launchResult
        self.screenshotPaths = screenshotPaths
        self.simulatorUsed = simulatorUsed
    }
}