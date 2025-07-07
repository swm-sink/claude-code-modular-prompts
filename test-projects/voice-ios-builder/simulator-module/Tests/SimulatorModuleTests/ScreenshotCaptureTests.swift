import XCTest
@testable import SimulatorModule

final class ScreenshotCaptureTests: XCTestCase {
    
    var screenshotCapture: ScreenshotCapture!
    var simulatorManager: SimulatorManager!
    
    override func setUp() {
        super.setUp()
        screenshotCapture = ScreenshotCapture()
        simulatorManager = SimulatorManager()
    }
    
    override func tearDown() {
        screenshotCapture = nil
        simulatorManager = nil
        super.tearDown()
    }
    
    // MARK: - RED Phase: Failing Tests
    
    func testScreenshotCaptureInitialization() {
        XCTAssertNotNil(screenshotCapture)
    }
    
    func testCaptureScreenshotFromSimulator() async throws {
        // Test capturing screenshot from simulator
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        // Launch simulator
        _ = try await simulatorManager.launchSimulator(udid: firstSimulator.udid)
        
        // Wait for simulator to be ready
        try await Task.sleep(nanoseconds: 3_000_000_000) // 3 seconds
        
        // Capture screenshot
        let screenshotResult = try await screenshotCapture.captureScreenshot(
            simulatorUDID: firstSimulator.udid,
            outputPath: "/tmp/test_screenshot.png"
        )
        
        XCTAssertTrue(screenshotResult.success, "Screenshot capture should succeed")
        XCTAssertFalse(screenshotResult.filePath.isEmpty, "Screenshot file path should not be empty")
        XCTAssertTrue(screenshotResult.filePath.hasSuffix(".png"), "Screenshot should be PNG format")
        
        // Verify file exists
        let fileExists = FileManager.default.fileExists(atPath: screenshotResult.filePath)
        XCTAssertTrue(fileExists, "Screenshot file should exist")
        
        // Clean up
        try await simulatorManager.shutdownSimulator(udid: firstSimulator.udid)
        try? FileManager.default.removeItem(atPath: screenshotResult.filePath)
    }
    
    func testCaptureMultipleScreenshots() async throws {
        // Test capturing multiple screenshots in sequence
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        // Launch simulator
        _ = try await simulatorManager.launchSimulator(udid: firstSimulator.udid)
        
        // Wait for simulator to be ready
        try await Task.sleep(nanoseconds: 3_000_000_000) // 3 seconds
        
        // Capture multiple screenshots
        let screenshotPaths = try await screenshotCapture.captureScreenshots(
            simulatorUDID: firstSimulator.udid,
            count: 3,
            interval: 1.0, // 1 second between screenshots
            outputDirectory: "/tmp/test_screenshots/"
        )
        
        XCTAssertEqual(screenshotPaths.count, 3, "Should capture 3 screenshots")
        
        // Verify all files exist
        for path in screenshotPaths {
            let fileExists = FileManager.default.fileExists(atPath: path)
            XCTAssertTrue(fileExists, "Screenshot file should exist: \(path)")
        }
        
        // Clean up
        try await simulatorManager.shutdownSimulator(udid: firstSimulator.udid)
        for path in screenshotPaths {
            try? FileManager.default.removeItem(atPath: path)
        }
    }
    
    func testScreenshotWithCustomFormat() async throws {
        // Test capturing screenshot with custom format
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        // Launch simulator
        _ = try await simulatorManager.launchSimulator(udid: firstSimulator.udid)
        
        // Wait for simulator to be ready
        try await Task.sleep(nanoseconds: 3_000_000_000) // 3 seconds
        
        // Capture screenshot with custom format
        let screenshotResult = try await screenshotCapture.captureScreenshot(
            simulatorUDID: firstSimulator.udid,
            outputPath: "/tmp/test_screenshot.jpg",
            format: .jpeg,
            quality: 0.8
        )
        
        XCTAssertTrue(screenshotResult.success, "Screenshot capture should succeed")
        XCTAssertTrue(screenshotResult.filePath.hasSuffix(".jpg"), "Screenshot should be JPEG format")
        
        // Clean up
        try await simulatorManager.shutdownSimulator(udid: firstSimulator.udid)
        try? FileManager.default.removeItem(atPath: screenshotResult.filePath)
    }
    
    func testScreenshotMetadata() async throws {
        // Test capturing screenshot with metadata
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        // Launch simulator
        _ = try await simulatorManager.launchSimulator(udid: firstSimulator.udid)
        
        // Wait for simulator to be ready
        try await Task.sleep(nanoseconds: 3_000_000_000) // 3 seconds
        
        // Capture screenshot with metadata
        let screenshotResult = try await screenshotCapture.captureScreenshotWithMetadata(
            simulatorUDID: firstSimulator.udid,
            outputPath: "/tmp/test_screenshot_with_metadata.png",
            metadata: ScreenshotMetadata(
                testCase: "testScreenshotMetadata",
                timestamp: Date(),
                deviceInfo: firstSimulator.name,
                appVersion: "1.0.0"
            )
        )
        
        XCTAssertTrue(screenshotResult.success, "Screenshot capture should succeed")
        XCTAssertNotNil(screenshotResult.metadata, "Screenshot should have metadata")
        
        // Clean up
        try await simulatorManager.shutdownSimulator(udid: firstSimulator.udid)
        try? FileManager.default.removeItem(atPath: screenshotResult.filePath)
    }
    
    func testScreenshotValidation() async throws {
        // Test screenshot validation
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        // Launch simulator
        _ = try await simulatorManager.launchSimulator(udid: firstSimulator.udid)
        
        // Wait for simulator to be ready
        try await Task.sleep(nanoseconds: 3_000_000_000) // 3 seconds
        
        // Capture screenshot
        let screenshotResult = try await screenshotCapture.captureScreenshot(
            simulatorUDID: firstSimulator.udid,
            outputPath: "/tmp/test_screenshot_validation.png"
        )
        
        // Validate screenshot
        let validationResult = try await screenshotCapture.validateScreenshot(
            filePath: screenshotResult.filePath
        )
        
        XCTAssertTrue(validationResult.isValid, "Screenshot should be valid")
        XCTAssertGreaterThan(validationResult.fileSize, 0, "Screenshot file size should be greater than 0")
        XCTAssertGreaterThan(validationResult.width, 0, "Screenshot width should be greater than 0")
        XCTAssertGreaterThan(validationResult.height, 0, "Screenshot height should be greater than 0")
        
        // Clean up
        try await simulatorManager.shutdownSimulator(udid: firstSimulator.udid)
        try? FileManager.default.removeItem(atPath: screenshotResult.filePath)
    }
    
    func testScreenshotErrorHandling() async {
        // Test error handling for invalid simulator UDID
        do {
            _ = try await screenshotCapture.captureScreenshot(
                simulatorUDID: "invalid-udid",
                outputPath: "/tmp/test_screenshot_error.png"
            )
            XCTFail("Should throw error for invalid simulator UDID")
        } catch ScreenshotError.invalidSimulatorUDID {
            // Expected error
        } catch {
            XCTFail("Should throw ScreenshotError.invalidSimulatorUDID, got: \(error)")
        }
    }
    
    func testScreenshotDirectoryCreation() async throws {
        // Test automatic directory creation for screenshots
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        // Launch simulator
        _ = try await simulatorManager.launchSimulator(udid: firstSimulator.udid)
        
        // Wait for simulator to be ready
        try await Task.sleep(nanoseconds: 3_000_000_000) // 3 seconds
        
        // Capture screenshot to non-existent directory
        let outputPath = "/tmp/test_screenshots_new_dir/screenshot.png"
        let screenshotResult = try await screenshotCapture.captureScreenshot(
            simulatorUDID: firstSimulator.udid,
            outputPath: outputPath
        )
        
        XCTAssertTrue(screenshotResult.success, "Screenshot capture should succeed")
        
        // Verify directory was created
        let directoryExists = FileManager.default.fileExists(atPath: "/tmp/test_screenshots_new_dir")
        XCTAssertTrue(directoryExists, "Directory should be created automatically")
        
        // Clean up
        try await simulatorManager.shutdownSimulator(udid: firstSimulator.udid)
        try? FileManager.default.removeItem(atPath: "/tmp/test_screenshots_new_dir")
    }
}