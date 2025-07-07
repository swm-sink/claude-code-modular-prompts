import XCTest
@testable import CodegenModule

final class CodeValidatorTests: XCTestCase {
    
    var validator: CodeValidator!
    
    override func setUp() {
        super.setUp()
        validator = CodeValidator()
    }
    
    override func tearDown() {
        validator = nil
        super.tearDown()
    }
    
    // RED: This test should fail initially
    func testSanitizeBasicString() {
        // Given
        let input = "Hello World"
        
        // When
        let sanitized = validator.sanitizeInput(input)
        
        // Then
        XCTAssertEqual(sanitized, "Hello World")
    }
    
    func testSanitizeCodeInjection() {
        // Given
        let maliciousInput = "test\"; system(\"rm -rf /\"); //"
        
        // When
        let sanitized = validator.sanitizeInput(maliciousInput)
        
        // Then
        XCTAssertFalse(sanitized.contains("system("))
        XCTAssertFalse(sanitized.contains("rm -rf"))
        XCTAssertTrue(sanitized.contains("test"))
    }
    
    func testSanitizeScriptTags() {
        // Given
        let input = "<script>alert('hack')</script>normal text"
        
        // When
        let sanitized = validator.sanitizeInput(input)
        
        // Then
        XCTAssertFalse(sanitized.contains("<script>"))
        XCTAssertFalse(sanitized.contains("alert"))
        XCTAssertTrue(sanitized.contains("normal text"))
    }
    
    func testValidateSwiftCode() {
        // Given
        let validCode = """
        Button("Click Me") {
            handleButtonTap()
        }
        .buttonStyle(.borderedProminent)
        """
        
        // When
        let isValid = validator.validateSwiftCode(validCode)
        
        // Then
        XCTAssertTrue(isValid)
    }
    
    func testValidateInvalidSwiftCode() {
        // Given
        let invalidCode = """
        Button("Click Me" {
            handleButtonTap()
        // Missing closing brace
        """
        
        // When
        let isValid = validator.validateSwiftCode(invalidCode)
        
        // Then
        XCTAssertFalse(isValid)
    }
    
    func testValidateCodeStructure() {
        // Given
        let wellStructuredCode = """
        struct ContentView: View {
            var body: some View {
                VStack {
                    Text("Hello")
                }
            }
        }
        """
        
        // When
        let isValid = validator.validateCodeStructure(wellStructuredCode)
        
        // Then
        XCTAssertTrue(isValid)
    }
    
    func testBlockDangerousOperations() {
        // Given
        let dangerousCode = """
        import Foundation
        system("rm -rf /")
        exec("malicious command")
        """
        
        // When
        let isValid = validator.validateSwiftCode(dangerousCode)
        
        // Then
        XCTAssertFalse(isValid)
    }
}