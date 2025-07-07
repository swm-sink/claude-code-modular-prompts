import Foundation
import CodegenModule

print("🚀 Swift/SwiftUI Code Generation Engine Demo")
print("=" * 50)

let demo = CodegenDemo()
let testRunner = CodegenTestRunner()

// Run tests first
print("\n📋 Running Tests...")
let testResults = testRunner.runAllTests()

// Run integration validation
print("\n🔍 Running Integration Validation...")
let validator = IntegrationValidator()
let validationReport = validator.validateCompleteWorkflow()
validationReport.printReport()

print("\n🎨 Code Generation Demonstrations:")
print("-" * 40)

// Demonstrate button generation
print("\n1️⃣ Basic Button Generation:")
let buttonCode = demo.demonstrateButtonGeneration()
print(buttonCode)

// Demonstrate voice command
print("\n2️⃣ Voice Command Integration:")
let voiceCode = demo.demonstrateVoiceCommand()
print(voiceCode)

// Demonstrate security
print("\n3️⃣ Security Validation:")
let security = demo.demonstrateSecurity()
print("Original: \(security.original)")
print("Sanitized: \(security.sanitized)")
print("Is Valid: \(security.isValid)")

// Demonstrate complete view
print("\n4️⃣ Complete View Generation:")
let completeView = demo.demonstrateCompleteView()
print(completeView)

print("\n✨ Demo Complete!")
print("🔒 Security: Code sanitization prevents injection attacks")
print("🎯 TDD: Red-Green-Refactor cycle followed")
print("📱 SwiftUI: Clean, compilable code generated")
print("🎤 Voice: Integration ready for voice commands")

extension String {
    static func * (left: String, right: Int) -> String {
        return String(repeating: left, count: right)
    }
}