import Foundation

public class CodeValidator {
    
    private let dangerousPatterns: [String] = [
        "system(",
        "exec(",
        "rm -rf",
        "eval(",
        "<script>",
        "</script>",
        "javascript:",
        "import Foundation", // Block Foundation for security
        "import Darwin",     // Block low-level system access
        "NSTask",
        "Process(",
        "Shell",
        "Runtime"
    ]
    
    private let allowedCharacters = CharacterSet.alphanumerics
        .union(.whitespaces)
        .union(.punctuationCharacters)
        .union(.symbols)
        .subtracting(CharacterSet(charactersIn: ";<>"))
    
    public init() {}
    
    /// Sanitizes input by removing dangerous patterns and characters
    public func sanitizeInput(_ input: String) -> String {
        var sanitized = input
        
        // Remove dangerous patterns
        for pattern in dangerousPatterns {
            sanitized = sanitized.replacingOccurrences(
                of: pattern,
                with: "",
                options: .caseInsensitive
            )
        }
        
        // Remove script tags and their content
        sanitized = sanitized.replacingOccurrences(
            of: "<script[^>]*>.*?</script>",
            with: "",
            options: [.caseInsensitive, .regularExpression]
        )
        
        // Keep only allowed characters
        let filtered = sanitized.unicodeScalars.filter { allowedCharacters.contains($0) }
        sanitized = String(String.UnicodeScalarView(filtered))
        
        return sanitized.trimmingCharacters(in: .whitespacesAndNewlines)
    }
    
    /// Validates Swift code for basic syntax correctness
    public func validateSwiftCode(_ code: String) -> Bool {
        // Check for dangerous patterns first
        for pattern in dangerousPatterns {
            if code.lowercased().contains(pattern.lowercased()) {
                return false
            }
        }
        
        // Basic syntax validation
        return validateCodeStructure(code)
    }
    
    /// Validates basic code structure (balanced braces, etc.)
    public func validateCodeStructure(_ code: String) -> Bool {
        var braceCount = 0
        var parenCount = 0
        var bracketCount = 0
        
        for char in code {
            switch char {
            case "{":
                braceCount += 1
            case "}":
                braceCount -= 1
                if braceCount < 0 { return false }
            case "(":
                parenCount += 1
            case ")":
                parenCount -= 1
                if parenCount < 0 { return false }
            case "[":
                bracketCount += 1
            case "]":
                bracketCount -= 1
                if bracketCount < 0 { return false }
            default:
                break
            }
        }
        
        // All brackets should be balanced
        return braceCount == 0 && parenCount == 0 && bracketCount == 0
    }
}