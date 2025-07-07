import Foundation

/// Comprehensive integration validator to ensure all components work together
public class IntegrationValidator {
    
    private let codegen: CodegenModule
    
    public init() {
        self.codegen = CodegenModule()
    }
    
    /// Validates the complete workflow from voice command to generated code
    public func validateCompleteWorkflow() -> ValidationReport {
        var results: [ValidationResult] = []
        
        // Test 1: Voice command parsing and code generation
        results.append(validateVoiceToCodeGeneration())
        
        // Test 2: Security validation across all components
        results.append(validateSecurityAcrossComponents())
        
        // Test 3: Code quality and compilation readiness
        results.append(validateCodeQuality())
        
        // Test 4: Component integration
        results.append(validateComponentIntegration())
        
        // Test 5: Error handling and recovery
        results.append(validateErrorHandling())
        
        let passedCount = results.filter { $0.passed }.count
        let coveragePercentage = Double(passedCount) / Double(results.count) * 100
        
        return ValidationReport(
            results: results,
            overallPassed: passedCount,
            totalTests: results.count,
            coveragePercentage: coveragePercentage,
            meetsRequirement: coveragePercentage >= 95.0
        )
    }
    
    private func validateVoiceToCodeGeneration() -> ValidationResult {
        let testCases: [(VoiceCommand, [String])] = [
            (
                VoiceCommand(componentType: "button", parameters: ["title": "Save", "action": "save", "style": "primary"]),
                ["Button(\"Save\")", "save()", ".buttonStyle(.borderedProminent)"]
            ),
            (
                VoiceCommand(componentType: "form", parameters: ["fields": "email:email:Email,password:secure:Password"]),
                ["Form {", "TextField", "SecureField", ".keyboardType(.emailAddress)"]
            ),
            (
                VoiceCommand(componentType: "list", parameters: ["items": "A,B,C", "action": "select"]),
                ["List {", "ForEach", "select(item)"]
            )
        ]
        
        for (command, expectedPatterns) in testCases {
            let generated = codegen.generateFromVoiceCommand(command)
            
            for pattern in expectedPatterns {
                if !generated.contains(pattern) {
                    return ValidationResult(
                        testName: "Voice to Code Generation",
                        passed: false,
                        message: "Missing expected pattern: \(pattern) in generated code"
                    )
                }
            }
        }
        
        return ValidationResult(
            testName: "Voice to Code Generation",
            passed: true,
            message: "All voice commands correctly generate expected code patterns"
        )
    }
    
    private func validateSecurityAcrossComponents() -> ValidationResult {
        let maliciousInputs = [
            "test\"; system(\"rm -rf /\"); //",
            "<script>alert('hack')</script>",
            "eval(malicious_code)",
            "import Foundation; exec(\"hack\")"
        ]
        
        for input in maliciousInputs {
            let sanitized = codegen.sanitize(input: input)
            
            // Check that dangerous patterns are removed
            if sanitized.contains("system(") || 
               sanitized.contains("<script>") || 
               sanitized.contains("eval(") ||
               sanitized.contains("import Foundation") {
                return ValidationResult(
                    testName: "Security Validation",
                    passed: false,
                    message: "Failed to sanitize malicious input: \(input)"
                )
            }
        }
        
        return ValidationResult(
            testName: "Security Validation",
            passed: true,
            message: "All malicious inputs properly sanitized"
        )
    }
    
    private func validateCodeQuality() -> ValidationResult {
        let components: [UIComponent] = [
            .button(ButtonConfig(title: "Test", action: "test", style: .primary)),
            .navigation(NavigationConfig(title: "Nav", content: "Content()")),
            .form(FormConfig(fields: [FormField(name: "field", type: .text, placeholder: "Field")])),
            .list(ListConfig(items: ["Item"], rowAction: "action"))
        ]
        
        for component in components {
            let code = codegen.generate(component: component)
            
            // Validate syntax
            if !codegen.validate(code: code) {
                return ValidationResult(
                    testName: "Code Quality",
                    passed: false,
                    message: "Generated code failed validation for component: \(component)"
                )
            }
            
            // Check for proper SwiftUI structure
            if !code.contains("{") || !code.contains("}") {
                return ValidationResult(
                    testName: "Code Quality",
                    passed: false,
                    message: "Generated code lacks proper structure for component: \(component)"
                )
            }
        }
        
        return ValidationResult(
            testName: "Code Quality",
            passed: true,
            message: "All generated code meets quality standards"
        )
    }
    
    private func validateComponentIntegration() -> ValidationResult {
        let components: [UIComponent] = [
            .button(ButtonConfig(title: "Login", action: "login", style: .primary)),
            .button(ButtonConfig(title: "Cancel", action: "cancel", style: .secondary))
        ]
        
        let view = codegen.generateView(components: components)
        
        let requiredPatterns = [
            "struct GeneratedView: View",
            "var body: some View",
            "VStack {",
            "Button(\"Login\")",
            "Button(\"Cancel\")"
        ]
        
        for pattern in requiredPatterns {
            if !view.contains(pattern) {
                return ValidationResult(
                    testName: "Component Integration",
                    passed: false,
                    message: "Missing required pattern in integrated view: \(pattern)"
                )
            }
        }
        
        return ValidationResult(
            testName: "Component Integration",
            passed: true,
            message: "Components correctly integrate into complete view"
        )
    }
    
    private func validateErrorHandling() -> ValidationResult {
        // Test invalid voice commands
        let invalidCommand = VoiceCommand(componentType: "unknown", parameters: [:])
        let result = codegen.generateFromVoiceCommand(invalidCommand)
        
        if !result.contains("Unsupported component type") {
            return ValidationResult(
                testName: "Error Handling",
                passed: false,
                message: "Failed to handle invalid component type"
            )
        }
        
        // Test malformed input
        let malformedInput = "{ malformed \" code"
        let isValid = codegen.validate(code: malformedInput)
        
        if isValid {
            return ValidationResult(
                testName: "Error Handling", 
                passed: false,
                message: "Failed to detect malformed code"
            )
        }
        
        return ValidationResult(
            testName: "Error Handling",
            passed: true,
            message: "Error handling works correctly for invalid inputs"
        )
    }
}

// MARK: - Supporting Types

public struct ValidationReport {
    public let results: [ValidationResult]
    public let overallPassed: Int
    public let totalTests: Int
    public let coveragePercentage: Double
    public let meetsRequirement: Bool
    
    public func printReport() {
        print("🔍 Integration Validation Report")
        print(String(repeating: "=", count: 40))
        
        for result in results {
            let status = result.passed ? "✅" : "❌"
            print("\(status) \(result.testName): \(result.message)")
        }
        
        print("\n📊 Summary:")
        print("   Passed: \(overallPassed)/\(totalTests)")
        print("   Coverage: \(String(format: "%.1f", coveragePercentage))%")
        print("   Requirement Met: \(meetsRequirement ? "✅ YES" : "❌ NO")")
        
        if meetsRequirement {
            print("\n🎉 All integration tests passed! Module ready for production.")
        } else {
            print("\n⚠️  Some tests failed. Review and fix before deployment.")
        }
    }
}

public struct ValidationResult {
    public let testName: String
    public let passed: Bool
    public let message: String
}