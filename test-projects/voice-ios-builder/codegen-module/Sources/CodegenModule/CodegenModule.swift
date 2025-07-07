import Foundation

/// Main interface for the Swift code generation module
/// Provides secure, template-based code generation for SwiftUI components
public class CodegenModule {
    
    private let codeGenerator: SwiftCodeGenerator
    private let validator: CodeValidator
    private let templates: UIComponentTemplates
    
    public init() {
        self.validator = CodeValidator()
        self.templates = UIComponentTemplates()
        self.codeGenerator = SwiftCodeGenerator()
    }
    
    /// Generates Swift code for a single UI component
    public func generate(component: UIComponent) -> String {
        return codeGenerator.generateComponent(component)
    }
    
    /// Generates a complete SwiftUI view with multiple components
    public func generateView(components: [UIComponent]) -> String {
        return codeGenerator.generateView(components: components)
    }
    
    /// Validates that generated code is safe and syntactically correct
    public func validate(code: String) -> Bool {
        return validator.validateSwiftCode(code)
    }
    
    /// Sanitizes user input to prevent code injection
    public func sanitize(input: String) -> String {
        return validator.sanitizeInput(input)
    }
}

// MARK: - Voice Command Integration Interface

/// Interface for integrating with voice command system
public protocol VoiceCommandCodegenInterface {
    func generateFromVoiceCommand(_ command: VoiceCommand) -> String
    func validateVoiceInput(_ input: String) -> Bool
}

public struct VoiceCommand {
    public let componentType: String
    public let parameters: [String: String]
    public let action: String?
    
    public init(componentType: String, parameters: [String: String], action: String? = nil) {
        self.componentType = componentType
        self.parameters = parameters
        self.action = action
    }
}

extension CodegenModule: VoiceCommandCodegenInterface {
    
    public func generateFromVoiceCommand(_ command: VoiceCommand) -> String {
        let sanitizedType = validator.sanitizeInput(command.componentType.lowercased())
        
        switch sanitizedType {
        case "button":
            return generateButtonFromVoice(command)
        case "navigation", "nav":
            return generateNavigationFromVoice(command)
        case "form":
            return generateFormFromVoice(command)
        case "list":
            return generateListFromVoice(command)
        default:
            return "// Unsupported component type: \(sanitizedType)"
        }
    }
    
    public func validateVoiceInput(_ input: String) -> Bool {
        return validator.sanitizeInput(input) == input && input.count <= 1000
    }
    
    // MARK: - Private Voice Command Helpers
    
    private func generateButtonFromVoice(_ command: VoiceCommand) -> String {
        let title = validator.sanitizeInput(command.parameters["title"] ?? "Button")
        let action = validator.sanitizeInput(command.parameters["action"] ?? "handleTap")
        let styleString = command.parameters["style"] ?? "primary"
        
        let style: ButtonStyle = {
            switch styleString.lowercased() {
            case "secondary": return .secondary
            case "destructive", "delete": return .destructive
            default: return .primary
            }
        }()
        
        let config = ButtonConfig(title: title, action: action, style: style)
        return codeGenerator.generateButton(config: config)
    }
    
    private func generateNavigationFromVoice(_ command: VoiceCommand) -> String {
        let title = validator.sanitizeInput(command.parameters["title"] ?? "Navigation")
        let content = validator.sanitizeInput(command.parameters["content"] ?? "Text(\"Content\")")
        
        let config = NavigationConfig(title: title, content: content)
        return templates.generateNavigationView(config: config)
    }
    
    private func generateFormFromVoice(_ command: VoiceCommand) -> String {
        // Parse form fields from voice command
        let fieldsString = command.parameters["fields"] ?? ""
        let fields = parseFormFields(fieldsString)
        
        let config = FormConfig(fields: fields)
        return templates.generateForm(config: config)
    }
    
    private func generateListFromVoice(_ command: VoiceCommand) -> String {
        let itemsString = command.parameters["items"] ?? "Item 1,Item 2,Item 3"
        let items = itemsString.split(separator: ",").map { String($0).trimmingCharacters(in: .whitespaces) }
        let action = validator.sanitizeInput(command.parameters["action"] ?? "handleTap")
        
        let config = ListConfig(items: items, rowAction: action)
        return templates.generateList(config: config)
    }
    
    private func parseFormFields(_ fieldsString: String) -> [FormField] {
        let fields = fieldsString.split(separator: ",")
        return fields.compactMap { fieldString in
            let parts = fieldString.split(separator: ":")
            guard parts.count >= 2 else { return nil }
            
            let name = String(parts[0]).trimmingCharacters(in: .whitespaces)
            let typeString = String(parts[1]).trimmingCharacters(in: .whitespaces)
            let placeholder = parts.count > 2 ? String(parts[2]).trimmingCharacters(in: .whitespaces) : "Enter \(name)"
            
            let type: FieldType = {
                switch typeString.lowercased() {
                case "secure", "password": return .secure
                case "number": return .number
                case "email": return .email
                default: return .text
                }
            }()
            
            return FormField(name: name, type: type, placeholder: placeholder)
        }
    }
}