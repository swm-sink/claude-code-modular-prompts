import Foundation

// MARK: - Button Configuration
public struct ButtonConfig {
    public let title: String
    public let action: String
    public let style: ButtonStyle
    
    public init(title: String, action: String, style: ButtonStyle) {
        self.title = title
        self.action = action
        self.style = style
    }
}

public enum ButtonStyle {
    case primary
    case secondary
    case destructive
}

// MARK: - Navigation Configuration
public struct NavigationConfig {
    public let title: String
    public let content: String
    
    public init(title: String, content: String) {
        self.title = title
        self.content = content
    }
}

// MARK: - Form Configuration
public struct FormConfig {
    public let fields: [FormField]
    
    public init(fields: [FormField]) {
        self.fields = fields
    }
}

public struct FormField {
    public let name: String
    public let type: FieldType
    public let placeholder: String
    
    public init(name: String, type: FieldType, placeholder: String) {
        self.name = name
        self.type = type
        self.placeholder = placeholder
    }
}

public enum FieldType {
    case text
    case secure
    case number
    case email
}

// MARK: - List Configuration
public struct ListConfig {
    public let items: [String]
    public let rowAction: String
    
    public init(items: [String], rowAction: String) {
        self.items = items
        self.rowAction = rowAction
    }
}