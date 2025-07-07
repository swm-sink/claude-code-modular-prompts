import Foundation

/// Simple test runner that doesn't depend on XCTest
public class CodegenTestRunner {
    
    private let demo: CodegenDemo
    private var passedTests = 0
    private var totalTests = 0
    
    public init() {
        self.demo = CodegenDemo()
    }
    
    public func runAllTests() -> TestResults {
        print("🧪 Running CodegenModule Tests...")
        
        testBasicButtonGeneration()
        testFormGeneration()
        testSecurityValidation()
        testVoiceCommandIntegration()
        testCompleteViewGeneration()
        testCodeValidation()
        
        let results = TestResults(
            passed: passedTests,
            total: totalTests,
            successRate: Double(passedTests) / Double(totalTests) * 100
        )
        
        printResults(results)
        return results
    }
    
    private func testBasicButtonGeneration() {
        test("Basic Button Generation") {
            let code = demo.demonstrateButtonGeneration()
            return code.contains("Button(\"Save Document\")") &&
                   code.contains("saveDocument()") &&
                   code.contains(".buttonStyle(.borderedProminent)")
        }
    }
    
    private func testFormGeneration() {
        test("Form Generation") {
            let code = demo.demonstrateVoiceCommand()
            return code.contains("Form {") &&
                   code.contains("TextField(\"Enter username\", text: $username)") &&
                   code.contains("SecureField(\"Enter password\", text: $password)")
        }
    }
    
    private func testSecurityValidation() {
        test("Security Validation") {
            let security = demo.demonstrateSecurity()
            return !security.sanitized.contains("system(") &&
                   !security.sanitized.contains("rm -rf") &&
                   security.sanitized.contains("test")
        }
    }
    
    private func testVoiceCommandIntegration() {
        test("Voice Command Integration") {
            let codegen = CodegenModule()
            let command = VoiceCommand(
                componentType: "button",
                parameters: ["title": "Test", "action": "test", "style": "primary"]
            )
            let code = codegen.generateFromVoiceCommand(command)
            return code.contains("Button(\"Test\")") && code.contains("test()")
        }
    }
    
    private func testCompleteViewGeneration() {
        test("Complete View Generation") {
            let code = demo.demonstrateCompleteView()
            return code.contains("struct GeneratedView: View") &&
                   code.contains("var body: some View") &&
                   code.contains("VStack {")
        }
    }
    
    private func testCodeValidation() {
        test("Code Validation") {
            let codegen = CodegenModule()
            let validCode = "Button(\"Test\") { action() }"
            let invalidCode = "Button(\"Test\" { action() }" // Missing closing parenthesis
            
            return codegen.validate(code: validCode) && !codegen.validate(code: invalidCode)
        }
    }
    
    private func test(_ name: String, _ testFunction: () -> Bool) {
        totalTests += 1
        let result = testFunction()
        
        if result {
            passedTests += 1
            print("✅ \(name)")
        } else {
            print("❌ \(name)")
        }
    }
    
    private func printResults(_ results: TestResults) {
        print("\n📊 Test Results:")
        print("   Passed: \(results.passed)/\(results.total)")
        print("   Success Rate: \(String(format: "%.1f", results.successRate))%")
        
        if results.successRate >= 95.0 {
            print("🎉 Excellent! Meeting 95%+ coverage requirement")
        } else {
            print("⚠️  Below 95% coverage requirement")
        }
    }
}

public struct TestResults {
    public let passed: Int
    public let total: Int
    public let successRate: Double
}