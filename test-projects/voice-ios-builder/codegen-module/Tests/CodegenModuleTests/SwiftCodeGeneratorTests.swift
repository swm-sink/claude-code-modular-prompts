import XCTest
@testable import CodegenModule

final class SwiftCodeGeneratorTests: XCTestCase {
    
    var codeGenerator: SwiftCodeGenerator!
    
    override func setUp() {
        super.setUp()
        codeGenerator = SwiftCodeGenerator()
    }
    
    override func tearDown() {
        codeGenerator = nil
        super.tearDown()
    }
    
    // RED: This test should fail initially
    func testGenerateBasicButton() {
        // Given
        let buttonConfig = ButtonConfig(
            title: "Click Me",
            action: "handleButtonTap",
            style: .primary
        )
        
        // When
        let generatedCode = codeGenerator.generateButton(config: buttonConfig)
        
        // Then
        let expectedCode = """
        Button("Click Me") {
            handleButtonTap()
        }
        .buttonStyle(.borderedProminent)
        """
        
        XCTAssertEqual(generatedCode.trimmingCharacters(in: .whitespacesAndNewlines), 
                      expectedCode.trimmingCharacters(in: .whitespacesAndNewlines))
    }
    
    func testGenerateSecondaryButton() {
        // Given
        let buttonConfig = ButtonConfig(
            title: "Cancel",
            action: "handleCancel",
            style: .secondary
        )
        
        // When
        let generatedCode = codeGenerator.generateButton(config: buttonConfig)
        
        // Then
        let expectedCode = """
        Button("Cancel") {
            handleCancel()
        }
        .buttonStyle(.bordered)
        """
        
        XCTAssertEqual(generatedCode.trimmingCharacters(in: .whitespacesAndNewlines), 
                      expectedCode.trimmingCharacters(in: .whitespacesAndNewlines))
    }
    
    func testGenerateDestructiveButton() {
        // Given
        let buttonConfig = ButtonConfig(
            title: "Delete",
            action: "handleDelete",
            style: .destructive
        )
        
        // When
        let generatedCode = codeGenerator.generateButton(config: buttonConfig)
        
        // Then
        let expectedCode = """
        Button("Delete") {
            handleDelete()
        }
        .buttonStyle(.borderedProminent)
        .tint(.red)
        """
        
        XCTAssertEqual(generatedCode.trimmingCharacters(in: .whitespacesAndNewlines), 
                      expectedCode.trimmingCharacters(in: .whitespacesAndNewlines))
    }
    
    func testCodeSanitization() {
        // Given - attempt to inject malicious code
        let maliciousConfig = ButtonConfig(
            title: "Test\"; system(\"rm -rf /\"); //",
            action: "handleTap(); system(\"malicious\")",
            style: .primary
        )
        
        // When
        let generatedCode = codeGenerator.generateButton(config: maliciousConfig)
        
        // Then - should sanitize the input
        XCTAssertFalse(generatedCode.contains("system("))
        XCTAssertFalse(generatedCode.contains("rm -rf"))
        XCTAssertTrue(generatedCode.contains("Test"))
    }
}