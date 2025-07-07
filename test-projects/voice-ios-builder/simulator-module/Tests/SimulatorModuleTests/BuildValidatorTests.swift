import XCTest
@testable import SimulatorModule

final class BuildValidatorTests: XCTestCase {
    
    var buildValidator: BuildValidator!
    var simulatorManager: SimulatorManager!
    
    override func setUp() {
        super.setUp()
        buildValidator = BuildValidator()
        simulatorManager = SimulatorManager()
    }
    
    override func tearDown() {
        buildValidator = nil
        simulatorManager = nil
        super.tearDown()
    }
    
    // MARK: - RED Phase: Failing Tests
    
    func testBuildValidatorInitialization() {
        XCTAssertNotNil(buildValidator)
    }
    
    func testValidateXcodeBuildEnvironment() async throws {
        // Test that Xcode build environment is properly configured
        let isValid = try await buildValidator.validateXcodeBuildEnvironment()
        XCTAssertTrue(isValid, "Xcode build environment should be valid")
    }
    
    func testBuildAppForSimulator() async throws {
        // Test building an app for simulator
        let projectPath = "/path/to/test/project"
        let buildResult = try await buildValidator.buildAppForSimulator(
            projectPath: projectPath,
            scheme: "TestApp",
            configuration: "Debug"
        )
        
        XCTAssertTrue(buildResult.success, "Build should succeed")
        XCTAssertFalse(buildResult.appPath.isEmpty, "App path should not be empty")
        XCTAssertTrue(buildResult.appPath.hasSuffix(".app"), "App path should end with .app")
    }
    
    func testDeployAppToSimulator() async throws {
        // Test deploying an app to simulator
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        // Launch simulator first
        _ = try await simulatorManager.launchSimulator(udid: firstSimulator.udid)
        
        // Deploy a test app
        let deployResult = try await buildValidator.deployAppToSimulator(
            appPath: "/path/to/TestApp.app",
            simulatorUDID: firstSimulator.udid
        )
        
        XCTAssertTrue(deployResult.success, "Deployment should succeed")
        XCTAssertFalse(deployResult.bundleIdentifier.isEmpty, "Bundle identifier should not be empty")
        
        // Clean up
        try await simulatorManager.shutdownSimulator(udid: firstSimulator.udid)
    }
    
    func testLaunchAppOnSimulator() async throws {
        // Test launching an app on simulator
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        // Launch simulator
        _ = try await simulatorManager.launchSimulator(udid: firstSimulator.udid)
        
        // Launch app
        let launchResult = try await buildValidator.launchAppOnSimulator(
            bundleIdentifier: "com.test.TestApp",
            simulatorUDID: firstSimulator.udid
        )
        
        XCTAssertTrue(launchResult.success, "App launch should succeed")
        XCTAssertFalse(launchResult.processId.isEmpty, "Process ID should not be empty")
        
        // Clean up
        try await simulatorManager.shutdownSimulator(udid: firstSimulator.udid)
    }
    
    func testValidateBuildConfiguration() async throws {
        // Test validating build configuration
        let config = BuildConfiguration(
            projectPath: "/path/to/project",
            scheme: "TestApp",
            configuration: "Debug",
            architecture: "x86_64"
        )
        
        let isValid = try await buildValidator.validateBuildConfiguration(config)
        XCTAssertTrue(isValid, "Build configuration should be valid")
    }
    
    func testBuildFailureHandling() async {
        // Test handling build failures
        let invalidProjectPath = "/invalid/path/to/project"
        
        do {
            _ = try await buildValidator.buildAppForSimulator(
                projectPath: invalidProjectPath,
                scheme: "TestApp",
                configuration: "Debug"
            )
            XCTFail("Should throw error for invalid project path")
        } catch BuildError.invalidProjectPath {
            // Expected error
        } catch {
            XCTFail("Should throw BuildError.invalidProjectPath, got: \(error)")
        }
    }
    
    func testBuildProgressTracking() async throws {
        // Test build progress tracking
        var progressUpdates: [BuildProgress] = []
        
        let projectPath = "/path/to/test/project"
        let buildResult = try await buildValidator.buildAppForSimulator(
            projectPath: projectPath,
            scheme: "TestApp",
            configuration: "Debug"
        ) { progress in
            progressUpdates.append(progress)
        }
        
        XCTAssertTrue(buildResult.success, "Build should succeed")
        XCTAssertFalse(progressUpdates.isEmpty, "Should receive progress updates")
    }
}