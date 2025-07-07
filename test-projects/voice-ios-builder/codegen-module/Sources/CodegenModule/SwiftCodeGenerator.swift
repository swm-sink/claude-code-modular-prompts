import Foundation

public class SwiftCodeGenerator {
    
    private let validator: CodeValidator
    private let templates: UIComponentTemplates
    
    public init() {
        self.validator = CodeValidator()
        self.templates = UIComponentTemplates()
    }
    
    /// Generates SwiftUI Button code from configuration
    public func generateButton(config: ButtonConfig) -> String {
        let sanitizedTitle = validator.sanitizeInput(config.title)
        let sanitizedAction = validator.sanitizeInput(config.action)
        
        let buttonStyle = styleString(for: config.style)
        let tintModifier = config.style == .destructive ? "\n.tint(.red)" : ""
        
        let code = """
        Button("\(sanitizedTitle)") {
            \(sanitizedAction)()
        }
        \(buttonStyle)\(tintModifier)
        """
        
        // Validate generated code before returning
        guard validator.validateSwiftCode(code) else {
            return generateFallbackButton()
        }
        
        return code
    }
    
    /// Generates complete SwiftUI view from multiple components
    public func generateView(components: [UIComponent]) -> String {
        var viewBody = "VStack {\n"
        
        for component in components {
            let componentCode = generateComponent(component)
            viewBody += "    \(componentCode.replacingOccurrences(of: "\n", with: "\n    "))\n"
        }
        
        viewBody += "}"
        
        let fullView = """
        struct GeneratedView: View {
            var body: some View {
                \(viewBody.replacingOccurrences(of: "\n", with: "\n        "))
            }
        }
        """
        
        return fullView
    }
    
    /// Generates code for individual UI component
    public func generateComponent(_ component: UIComponent) -> String {
        switch component {
        case .button(let config):
            return generateButton(config: config)
        case .navigation(let config):
            return templates.generateNavigationView(config: config)
        case .form(let config):
            return templates.generateForm(config: config)
        case .list(let config):
            return templates.generateList(config: config)
        }
    }
    
    private func styleString(for style: ButtonStyle) -> String {
        switch style {
        case .primary:
            return ".buttonStyle(.borderedProminent)"
        case .secondary:
            return ".buttonStyle(.bordered)"
        case .destructive:
            return ".buttonStyle(.borderedProminent)"
        }
    }
    
    private func generateFallbackButton() -> String {
        return """
        Button("Button") {
            // Action
        }
        .buttonStyle(.bordered)
        """
    }
}

// MARK: - UI Component Enum
public enum UIComponent {
    case button(ButtonConfig)
    case navigation(NavigationConfig)
    case form(FormConfig)
    case list(ListConfig)
}