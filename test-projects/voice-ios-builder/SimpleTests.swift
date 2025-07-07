import Foundation
import VoiceIOSBuilder

// Simple test runner without XCTest dependency
class SimpleTestRunner {
    var testResults: [TestResult] = []
    
    struct TestResult {
        let testName: String
        let passed: Bool
        let message: String
    }
    
    func assert(_ condition: Bool, _ message: String, testName: String) {
        testResults.append(TestResult(testName: testName, passed: condition, message: message))
        if condition {
            print("✅ \(testName): \(message)")
        } else {
            print("❌ \(testName): \(message)")
        }
    }
    
    func printSummary() {
        let passed = testResults.filter { $0.passed }.count
        let total = testResults.count
        print("\n📊 Test Summary: \(passed)/\(total) tests passed")
        
        if passed == total {
            print("🎉 All tests passed!")
        } else {
            print("⚠️ Some tests failed")
        }
    }
}

// MARK: - App Coordinator Tests
@MainActor
class AppCoordinatorSimpleTests {
    let testRunner = SimpleTestRunner()
    
    func runAllTests() async {
        await testAppCoordinatorInitialization()
        await testAppCoordinatorCanStartVoiceRecording()
        await testAppCoordinatorCanProcessVoiceInput()
        await testAppCoordinatorCanTriggerCodeGeneration()
        
        testRunner.printSummary()
    }
    
    func testAppCoordinatorInitialization() async {
        let appCoordinator = AppCoordinator()
        
        testRunner.assert(
            appCoordinator.currentState == .idle,
            "AppCoordinator should start in idle state",
            testName: "testAppCoordinatorInitialization"
        )
    }
    
    func testAppCoordinatorCanStartVoiceRecording() async {
        let appCoordinator = AppCoordinator()
        
        await withCheckedContinuation { continuation in
            appCoordinator.startVoiceRecording { success in
                self.testRunner.assert(
                    success,
                    "Voice recording should start successfully",
                    testName: "testAppCoordinatorCanStartVoiceRecording"
                )
                continuation.resume()
            }
        }
        
        // Give some time for state to update
        try? await Task.sleep(nanoseconds: 100_000_000) // 0.1 seconds
        
        testRunner.assert(
            appCoordinator.currentState == .recording,
            "State should be recording",
            testName: "testAppCoordinatorCanStartVoiceRecording_State"
        )
    }
    
    func testAppCoordinatorCanProcessVoiceInput() async {
        let appCoordinator = AppCoordinator()
        let testInput = "Create a simple calculator app"
        
        await withCheckedContinuation { continuation in
            appCoordinator.processVoiceInput(testInput) { result in
                switch result {
                case .success(let processedInput):
                    self.testRunner.assert(
                        !processedInput.isEmpty,
                        "Processed input should not be empty",
                        testName: "testAppCoordinatorCanProcessVoiceInput"
                    )
                case .failure(let error):
                    self.testRunner.assert(
                        false,
                        "Voice processing failed: \(error)",
                        testName: "testAppCoordinatorCanProcessVoiceInput"
                    )
                }
                continuation.resume()
            }
        }
    }
    
    func testAppCoordinatorCanTriggerCodeGeneration() async {
        let appCoordinator = AppCoordinator()
        let testRequest = VoiceRequest(
            originalText: "Create a simple calculator app",
            processedText: "Create a simple calculator app with basic arithmetic operations",
            intent: .createApp
        )
        
        await withCheckedContinuation { continuation in
            appCoordinator.triggerCodeGeneration(for: testRequest) { result in
                switch result {
                case .success(let generatedCode):
                    self.testRunner.assert(
                        !generatedCode.isEmpty,
                        "Generated code should not be empty",
                        testName: "testAppCoordinatorCanTriggerCodeGeneration"
                    )
                    self.testRunner.assert(
                        generatedCode.contains("SwiftUI"),
                        "Generated code should contain SwiftUI",
                        testName: "testAppCoordinatorCanTriggerCodeGeneration_SwiftUI"
                    )
                case .failure(let error):
                    self.testRunner.assert(
                        false,
                        "Code generation failed: \(error)",
                        testName: "testAppCoordinatorCanTriggerCodeGeneration"
                    )
                }
                continuation.resume()
            }
        }
    }
}

// MARK: - Project Manager Tests
class ProjectManagerSimpleTests {
    let testRunner = SimpleTestRunner()
    
    func runAllTests() async {
        await testProjectManagerCanCreateNewProject()
        testProjectManagerCanListProjects()
        await testProjectManagerCanDeleteProject()
        await testProjectManagerCanUpdateProject()
        
        testRunner.printSummary()
    }
    
    func testProjectManagerCanCreateNewProject() async {
        let projectManager = ProjectManager()
        let projectName = "TestCalculatorApp"
        let projectDescription = "A simple calculator app with basic arithmetic operations"
        
        await withCheckedContinuation { continuation in
            projectManager.createProject(
                name: projectName,
                description: projectDescription,
                generatedCode: "// Test code"
            ) { result in
                switch result {
                case .success(let project):
                    self.testRunner.assert(
                        project.name == projectName,
                        "Project name should match",
                        testName: "testProjectManagerCanCreateNewProject_Name"
                    )
                    self.testRunner.assert(
                        project.description == projectDescription,
                        "Project description should match",
                        testName: "testProjectManagerCanCreateNewProject_Description"
                    )
                case .failure(let error):
                    self.testRunner.assert(
                        false,
                        "Project creation failed: \(error)",
                        testName: "testProjectManagerCanCreateNewProject"
                    )
                }
                continuation.resume()
            }
        }
    }
    
    func testProjectManagerCanListProjects() {
        let projectManager = ProjectManager()
        let projects = projectManager.getAllProjects()
        
        testRunner.assert(
            projects.isEmpty,
            "Projects list should be empty initially",
            testName: "testProjectManagerCanListProjects"
        )
    }
    
    func testProjectManagerCanDeleteProject() async {
        let projectManager = ProjectManager()
        let projectId = UUID()
        
        await withCheckedContinuation { continuation in
            projectManager.deleteProject(id: projectId) { result in
                switch result {
                case .success:
                    self.testRunner.assert(
                        false,
                        "Should not succeed deleting non-existent project",
                        testName: "testProjectManagerCanDeleteProject"
                    )
                case .failure:
                    self.testRunner.assert(
                        true,
                        "Should fail when deleting non-existent project",
                        testName: "testProjectManagerCanDeleteProject"
                    )
                }
                continuation.resume()
            }
        }
    }
    
    func testProjectManagerCanUpdateProject() async {
        let projectManager = ProjectManager()
        let projectId = UUID()
        let updatedCode = "// Updated test code"
        
        await withCheckedContinuation { continuation in
            projectManager.updateProject(
                id: projectId,
                updatedCode: updatedCode
            ) { result in
                switch result {
                case .success:
                    self.testRunner.assert(
                        false,
                        "Should not succeed updating non-existent project",
                        testName: "testProjectManagerCanUpdateProject"
                    )
                case .failure:
                    self.testRunner.assert(
                        true,
                        "Should fail when updating non-existent project",
                        testName: "testProjectManagerCanUpdateProject"
                    )
                }
                continuation.resume()
            }
        }
    }
}

// MARK: - Main Test Runner
@main
struct TestRunner {
    static func main() async {
        print("🧪 Running Voice iOS Builder Tests")
        print("==================================")
        
        print("\n📱 Testing AppCoordinator...")
        let appCoordinatorTests = AppCoordinatorSimpleTests()
        await appCoordinatorTests.runAllTests()
        
        print("\n📁 Testing ProjectManager...")
        let projectManagerTests = ProjectManagerSimpleTests()
        await projectManagerTests.runAllTests()
        
        print("\n🎯 All tests completed!")
    }
}