import Foundation

public class VoiceCommandParser {
    
    // MARK: - Public Properties
    
    public let supportedCommands: [String] = [
        "create", "add", "delete", "modify",
        "button", "navigation", "view", "label", "textfield", "imageview"
    ]
    
    // MARK: - Private Properties
    
    private let securityKeywords: [String] = [
        "DROP", "DELETE", "INSERT", "UPDATE", "SELECT",
        "system", "eval", "exec", "import", "require",
        "<script>", "</script>", "javascript:", "onload",
        "rm -rf", "sudo", "chmod", "passwd"
    ]
    
    // MARK: - Initialization
    
    public init() {}
    
    // MARK: - Public Methods
    
    public func parseCommand(_ input: String) -> VoiceCommandResult {
        // Security check first
        if containsSecurityViolation(input) {
            return .failure(.securityViolation)
        }
        
        let sanitized = sanitizeInput(input)
        let tokens = tokenize(sanitized)
        
        guard let intent = extractIntent(from: tokens) else {
            return .failure(.unrecognizedCommand)
        }
        
        return .success(intent)
    }
    
    public func sanitizeInput(_ input: String) -> String {
        var sanitized = input.lowercased()
        
        // Remove potential SQL injection patterns
        sanitized = sanitized.replacingOccurrences(of: "';", with: "")
        sanitized = sanitized.replacingOccurrences(of: "--", with: "")
        sanitized = sanitized.replacingOccurrences(of: "/*", with: "")
        sanitized = sanitized.replacingOccurrences(of: "*/", with: "")
        
        // Remove script tags and javascript
        sanitized = sanitized.replacingOccurrences(of: "<script>", with: "")
        sanitized = sanitized.replacingOccurrences(of: "</script>", with: "")
        sanitized = sanitized.replacingOccurrences(of: "javascript:", with: "")
        
        // Remove system commands
        sanitized = sanitized.replacingOccurrences(of: "system(", with: "")
        sanitized = sanitized.replacingOccurrences(of: "eval(", with: "")
        sanitized = sanitized.replacingOccurrences(of: "exec(", with: "")
        
        return sanitized.trimmingCharacters(in: .whitespacesAndNewlines)
    }
    
    // MARK: - Private Methods
    
    private func containsSecurityViolation(_ input: String) -> Bool {
        let lowercased = input.lowercased()
        return securityKeywords.contains { keyword in
            lowercased.contains(keyword.lowercased())
        }
    }
    
    private func tokenize(_ input: String) -> [String] {
        return input.components(separatedBy: .whitespacesAndNewlines.union(.punctuationCharacters))
            .filter { !$0.isEmpty }
    }
    
    private func extractIntent(from tokens: [String]) -> VoiceCommandIntent? {
        // Identify action
        guard let action = identifyAction(from: tokens) else {
            return nil
        }
        
        // Identify component type
        guard let componentType = identifyComponentType(from: tokens) else {
            return nil
        }
        
        // Extract parameters
        let parameters = extractParameters(from: tokens)
        
        // Calculate confidence based on how well we matched
        let confidence = calculateConfidence(tokens: tokens, action: action, componentType: componentType)
        
        return VoiceCommandIntent(
            action: action,
            componentType: componentType,
            parameters: parameters,
            confidence: confidence
        )
    }
    
    private func identifyAction(from tokens: [String]) -> VoiceCommandAction? {
        let actionSynonyms: [String: VoiceCommandAction] = [
            "create": .createComponent,
            "make": .createComponent,
            "build": .createComponent,
            "new": .createComponent,
            "add": .addComponent,
            "insert": .addComponent,
            "include": .addComponent,
            "delete": .deleteComponent,
            "remove": .deleteComponent,
            "destroy": .deleteComponent,
            "modify": .modifyComponent,
            "change": .modifyComponent,
            "update": .modifyComponent,
            "edit": .modifyComponent
        ]
        
        for token in tokens {
            if let action = actionSynonyms[token] {
                return action
            }
        }
        
        return nil
    }
    
    private func identifyComponentType(from tokens: [String]) -> ComponentType? {
        let componentSynonyms: [String: ComponentType] = [
            "button": .button,
            "btn": .button,
            "navigation": .navigation,
            "nav": .navigation,
            "menu": .navigation,
            "view": .view,
            "container": .view,
            "panel": .view,
            "label": .label,
            "text": .label,
            "title": .label,
            "textfield": .textField,
            "input": .textField,
            "field": .textField,
            "imageview": .imageView,
            "image": .imageView,
            "picture": .imageView,
            "photo": .imageView
        ]
        
        for token in tokens {
            if let componentType = componentSynonyms[token] {
                return componentType
            }
        }
        
        return nil
    }
    
    private func extractParameters(from tokens: [String]) -> [String: String] {
        var parameters: [String: String] = [:]
        
        // Look for color parameters
        let colors = ["red", "blue", "green", "yellow", "black", "white", "gray", "orange", "purple", "pink"]
        for color in colors {
            if tokens.contains(color) {
                parameters["color"] = color
                break
            }
        }
        
        // Look for "with title" or "with text" patterns
        if let titleIndex = tokens.firstIndex(where: { $0 == "title" || $0 == "text" }) {
            let remainingTokens = Array(tokens[(titleIndex + 1)...])
            if !remainingTokens.isEmpty {
                parameters["title"] = remainingTokens.joined(separator: " ")
            }
        }
        
        return parameters
    }
    
    private func calculateConfidence(tokens: [String], action: VoiceCommandAction, componentType: ComponentType) -> Double {
        var confidence = 0.5 // Base confidence
        
        // Increase confidence if we found exact matches
        if tokens.contains(action.rawValue) {
            confidence += 0.3
        }
        
        if tokens.contains(componentType.rawValue) {
            confidence += 0.3
        }
        
        // Decrease confidence for very short or very long commands
        if tokens.count < 2 {
            confidence -= 0.1
        } else if tokens.count > 10 {
            confidence -= 0.1
        }
        
        return min(1.0, max(0.0, confidence))
    }
}