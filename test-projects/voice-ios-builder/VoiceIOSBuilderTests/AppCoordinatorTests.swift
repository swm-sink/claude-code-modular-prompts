import XCTest
import SwiftUI
@testable import VoiceIOSBuilder

final class AppCoordinatorTests: XCTestCase {
    
    var appCoordinator: AppCoordinator!
    
    override func setUpWithError() throws {
        super.setUp()
        appCoordinator = AppCoordinator()
    }
    
    override func tearDownWithError() throws {
        appCoordinator = nil
        super.tearDown()
    }
    
    // MARK: - App Launch Tests
    
    func testAppCoordinatorInitialization() throws {
        // This test will FAIL initially - implementing TDD RED phase
        XCTAssertNotNil(appCoordinator, "AppCoordinator should be initialized")
        XCTAssertEqual(appCoordinator.currentState, .idle, "AppCoordinator should start in idle state")
    }
    
    func testAppCoordinatorCanStartVoiceRecording() throws {
        // RED: This will fail - no voice recording capability yet
        let expectation = XCTestExpectation(description: "Voice recording should start")
        
        appCoordinator.startVoiceRecording { success in
            XCTAssertTrue(success, "Voice recording should start successfully")
            expectation.fulfill()
        }
        
        wait(for: [expectation], timeout: 2.0)
        XCTAssertEqual(appCoordinator.currentState, .recording, "State should be recording")
    }
    
    func testAppCoordinatorCanProcessVoiceInput() throws {
        // RED: This will fail - no voice processing yet
        let testInput = "Create a simple calculator app"
        let expectation = XCTestExpectation(description: "Voice input should be processed")
        
        appCoordinator.processVoiceInput(testInput) { result in
            switch result {
            case .success(let processedInput):
                XCTAssertNotNil(processedInput, "Processed input should not be nil")
                XCTAssertFalse(processedInput.isEmpty, "Processed input should not be empty")
                expectation.fulfill()
            case .failure(let error):
                XCTFail("Voice processing failed: \(error)")
            }
        }
        
        wait(for: [expectation], timeout: 5.0)
    }
    
    func testAppCoordinatorCanTriggerCodeGeneration() throws {
        // RED: This will fail - no code generation integration yet
        let testRequest = VoiceRequest(
            originalText: "Create a simple calculator app",
            processedText: "Create a simple calculator app with basic arithmetic operations",
            intent: .createApp
        )
        
        let expectation = XCTestExpectation(description: "Code generation should be triggered")
        
        appCoordinator.triggerCodeGeneration(for: testRequest) { result in
            switch result {
            case .success(let generatedCode):
                XCTAssertNotNil(generatedCode, "Generated code should not be nil")
                XCTAssertFalse(generatedCode.isEmpty, "Generated code should not be empty")
                expectation.fulfill()
            case .failure(let error):
                XCTFail("Code generation failed: \(error)")
            }
        }
        
        wait(for: [expectation], timeout: 10.0)
    }
}