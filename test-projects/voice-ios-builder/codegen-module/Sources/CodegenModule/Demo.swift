import Foundation

/// Demonstration of the code generation capabilities
public class CodegenDemo {
    
    private let codegen: CodegenModule
    
    public init() {
        self.codegen = CodegenModule()
    }
    
    /// Demonstrates basic button generation
    public func demonstrateButtonGeneration() -> String {
        let buttonConfig = ButtonConfig(
            title: "Save Document",
            action: "saveDocument",
            style: .primary
        )
        
        return codegen.generate(component: .button(buttonConfig))
    }
    
    /// Demonstrates voice command integration
    public func demonstrateVoiceCommand() -> String {
        let voiceCommand = VoiceCommand(
            componentType: "form",
            parameters: [
                "fields": "username:text:Enter username,password:secure:Enter password"
            ]
        )
        
        return codegen.generateFromVoiceCommand(voiceCommand)
    }
    
    /// Demonstrates complete view generation
    public func demonstrateCompleteView() -> String {
        let components: [UIComponent] = [
            .navigation(NavigationConfig(
                title: "Login",
                content: "LoginForm()"
            )),
            .form(FormConfig(fields: [
                FormField(name: "email", type: .email, placeholder: "Enter email"),
                FormField(name: "password", type: .secure, placeholder: "Enter password")
            ])),
            .button(ButtonConfig(title: "Login", action: "handleLogin", style: .primary)),
            .button(ButtonConfig(title: "Cancel", action: "handleCancel", style: .secondary))
        ]
        
        return codegen.generateView(components: components)
    }
    
    /// Demonstrates security validation
    public func demonstrateSecurity() -> (original: String, sanitized: String, isValid: Bool) {
        let maliciousInput = "test\"; system(\"rm -rf /\"); //"
        let sanitized = codegen.sanitize(input: maliciousInput)
        let isValid = codegen.validate(code: sanitized)
        
        return (original: maliciousInput, sanitized: sanitized, isValid: isValid)
    }
}