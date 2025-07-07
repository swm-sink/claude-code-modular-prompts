import XCTest
@testable import VoiceIOSBuilder
@testable import VoiceModule
@testable import CodegenModule
@testable import SimulatorModule

final class IntegrationTests: XCTestCase {
    
    func testAppCoordinatorIntegration() async throws {
        // Test that AppCoordinator can be initialized with real modules
        let coordinator = AppCoordinator()
        
        XCTAssertEqual(coordinator.currentState, .idle)
        XCTAssertTrue(coordinator.recentProjects.isEmpty)
        XCTAssertFalse(coordinator.isProcessing)
    }
    
    func testVoiceModuleIntegration() throws {
        // Test that VoiceRecognition module can be instantiated
        let voiceRecognition = VoiceRecognition()
        
        XCTAssertFalse(voiceRecognition.isListening)
        XCTAssertEqual(voiceRecognition.recognitionState, .idle)
    }
    
    func testCodegenModuleIntegration() throws {
        // Test that SwiftCodeGenerator can generate code
        let codeGenerator = SwiftCodeGenerator()
        
        let buttonConfig = ButtonConfig(
            title: "Test Button",
            action: "testAction",
            style: .primary
        )
        
        let generatedCode = codeGenerator.generateButton(config: buttonConfig)
        
        XCTAssertFalse(generatedCode.isEmpty)
        XCTAssertTrue(generatedCode.contains("Test Button"))
        XCTAssertTrue(generatedCode.contains("testAction"))
        XCTAssertTrue(generatedCode.contains("Button"))
    }
    
    func testSimulatorModuleIntegration() async throws {
        // Test that SimulatorManager can list simulators
        let simulatorManager = SimulatorManager()
        
        let simulators = try await simulatorManager.listAvailableSimulators()
        
        XCTAssertFalse(simulators.isEmpty)
        XCTAssertTrue(simulators.contains { $0.name.contains("iPhone") })
    }
    
    @MainActor
    func testVoiceProcessingIntegration() async throws {
        // Test full voice processing pipeline
        let coordinator = AppCoordinator()
        
        await withCheckedContinuation { (continuation: CheckedContinuation<Void, Never>) in
            coordinator.processVoiceInput("Create a button") { result in
                switch result {
                case .success(let processedText):
                    XCTAssertEqual(processedText, "Create a button")
                case .failure(let error):
                    XCTFail("Voice processing failed: \(error)")
                }
                continuation.resume()
            }
        }
    }
    
    @MainActor
    func testCodeGenerationIntegration() async throws {
        // Test full code generation pipeline
        let coordinator = AppCoordinator()
        
        let request = VoiceRequest(
            originalText: "Create a save button",
            processedText: "Create a save button",
            intent: .createApp
        )
        
        await withCheckedContinuation { (continuation: CheckedContinuation<Void, Never>) in
            coordinator.triggerCodeGeneration(for: request) { result in
                switch result {
                case .success(let generatedCode):
                    XCTAssertFalse(generatedCode.isEmpty)
                    XCTAssertTrue(generatedCode.contains("struct GeneratedView"))
                    XCTAssertTrue(generatedCode.contains("VStack"))
                case .failure(let error):
                    XCTFail("Code generation failed: \(error)")
                }
                continuation.resume()
            }
        }
    }
}