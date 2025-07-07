import Foundation

public class UIComponentTemplates {
    
    private let validator: CodeValidator
    
    public init() {
        self.validator = CodeValidator()
    }
    
    /// Generates NavigationView SwiftUI code
    public func generateNavigationView(config: NavigationConfig) -> String {
        let sanitizedTitle = validator.sanitizeInput(config.title.isEmpty ? "Navigation" : config.title)
        let sanitizedContent = config.content.isEmpty ? "EmptyView()" : config.content
        
        let code = """
        NavigationView {
            \(sanitizedContent)
                .navigationTitle("\(sanitizedTitle)")
        }
        """
        
        return code
    }
    
    /// Generates Form SwiftUI code
    public func generateForm(config: FormConfig) -> String {
        var formFields = ""
        
        for field in config.fields {
            let sanitizedName = validator.sanitizeInput(field.name)
            let sanitizedPlaceholder = validator.sanitizeInput(field.placeholder)
            
            let fieldCode = generateFormField(
                name: sanitizedName,
                type: field.type,
                placeholder: sanitizedPlaceholder
            )
            
            formFields += "    \(fieldCode)\n"
        }
        
        let code = """
        Form {
        \(formFields.trimmingCharacters(in: .whitespacesAndNewlines))
        }
        """
        
        return code
    }
    
    /// Generates List SwiftUI code
    public func generateList(config: ListConfig) -> String {
        let sanitizedAction = validator.sanitizeInput(config.rowAction)
        let sanitizedItems = config.items.map { validator.sanitizeInput($0) }
        
        // Convert array to string representation for code generation
        let itemsString = sanitizedItems.map { "\"\($0)\"" }.joined(separator: ", ")
        
        let code = """
        List {
            ForEach([\(itemsString)], id: \\.self) { item in
                Text(item)
                    .onTapGesture {
                        \(sanitizedAction)(item)
                    }
            }
        }
        """
        
        return code
    }
    
    /// Generates VStack container
    public func generateVStack(spacing: CGFloat = 8, content: [String]) -> String {
        let sanitizedContent = content.map { validator.sanitizeInput($0) }
        let contentString = sanitizedContent.joined(separator: "\n    ")
        
        return """
        VStack(spacing: \(spacing)) {
            \(contentString)
        }
        """
    }
    
    /// Generates HStack container
    public func generateHStack(spacing: CGFloat = 8, content: [String]) -> String {
        let sanitizedContent = content.map { validator.sanitizeInput($0) }
        let contentString = sanitizedContent.joined(separator: "\n    ")
        
        return """
        HStack(spacing: \(spacing)) {
            \(contentString)
        }
        """
    }
    
    /// Generates Text view
    public func generateText(_ content: String, modifier: TextModifier? = nil) -> String {
        let sanitizedContent = validator.sanitizeInput(content)
        var code = "Text(\"\(sanitizedContent)\")"
        
        if let modifier = modifier {
            code += applyTextModifier(modifier)
        }
        
        return code
    }
    
    // MARK: - Private Helper Methods
    
    private func generateFormField(name: String, type: FieldType, placeholder: String) -> String {
        switch type {
        case .text:
            return "TextField(\"\(placeholder)\", text: $\(name))"
        case .secure:
            return "SecureField(\"\(placeholder)\", text: $\(name))"
        case .number:
            return "TextField(\"\(placeholder)\", text: $\(name))\n        .keyboardType(.numberPad)"
        case .email:
            return "TextField(\"\(placeholder)\", text: $\(name))\n        .keyboardType(.emailAddress)"
        }
    }
    
    private func applyTextModifier(_ modifier: TextModifier) -> String {
        switch modifier {
        case .title:
            return "\n    .font(.title)"
        case .headline:
            return "\n    .font(.headline)"
        case .body:
            return "\n    .font(.body)"
        case .caption:
            return "\n    .font(.caption)"
        case .bold:
            return "\n    .fontWeight(.bold)"
        }
    }
}

// MARK: - Supporting Types

public enum TextModifier {
    case title
    case headline
    case body
    case caption
    case bold
}