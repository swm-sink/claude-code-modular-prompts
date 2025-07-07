import XCTest
@testable import CodegenModule

final class VoiceCommandIntegrationTests: XCTestCase {
    
    var codegenModule: CodegenModule!
    
    override func setUp() {
        super.setUp()
        codegenModule = CodegenModule()
    }
    
    override func tearDown() {
        codegenModule = nil
        super.tearDown()
    }
    
    // RED: This test should fail initially
    func testVoiceCommandButtonGeneration() {
        // Given
        let voiceCommand = VoiceCommand(
            componentType: "button",
            parameters: [
                "title": "Save Document",
                "action": "saveDocument",
                "style": "primary"
            ]
        )
        
        // When
        let generatedCode = codegenModule.generateFromVoiceCommand(voiceCommand)
        
        // Then
        XCTAssertTrue(generatedCode.contains("Button(\"Save Document\")"))
        XCTAssertTrue(generatedCode.contains("saveDocument()"))
        XCTAssertTrue(generatedCode.contains(".buttonStyle(.borderedProminent)"))
    }
    
    func testVoiceCommandNavigationGeneration() {
        // Given
        let voiceCommand = VoiceCommand(
            componentType: "navigation",
            parameters: [
                "title": "User Profile",
                "content": "ProfileView()"
            ]
        )
        
        // When
        let generatedCode = codegenModule.generateFromVoiceCommand(voiceCommand)
        
        // Then
        XCTAssertTrue(generatedCode.contains("NavigationView"))
        XCTAssertTrue(generatedCode.contains(".navigationTitle(\"User Profile\")"))
        XCTAssertTrue(generatedCode.contains("ProfileView()"))
    }
    
    func testVoiceCommandFormGeneration() {
        // Given
        let voiceCommand = VoiceCommand(
            componentType: "form",
            parameters: [
                "fields": "username:text:Enter username,password:secure:Enter password,email:email:Enter email"
            ]
        )
        
        // When
        let generatedCode = codegenModule.generateFromVoiceCommand(voiceCommand)
        
        // Then
        XCTAssertTrue(generatedCode.contains("Form {"))
        XCTAssertTrue(generatedCode.contains("TextField(\"Enter username\", text: $username)"))
        XCTAssertTrue(generatedCode.contains("SecureField(\"Enter password\", text: $password)"))
        XCTAssertTrue(generatedCode.contains("TextField(\"Enter email\", text: $email)"))
        XCTAssertTrue(generatedCode.contains(".keyboardType(.emailAddress)"))
    }
    
    func testVoiceCommandListGeneration() {
        // Given
        let voiceCommand = VoiceCommand(
            componentType: "list",
            parameters: [
                "items": "Home,Settings,Profile,Logout",
                "action": "navigateToSection"
            ]
        )
        
        // When
        let generatedCode = codegenModule.generateFromVoiceCommand(voiceCommand)
        
        // Then
        XCTAssertTrue(generatedCode.contains("List {"))
        XCTAssertTrue(generatedCode.contains("ForEach([\"Home\", \"Settings\", \"Profile\", \"Logout\"]"))
        XCTAssertTrue(generatedCode.contains("navigateToSection(item)"))
    }
    
    func testVoiceInputValidation() {
        // Given - valid input
        let validInput = "Create a button with title Save"
        
        // When
        let isValid = codegenModule.validateVoiceInput(validInput)
        
        // Then
        XCTAssertTrue(isValid)
    }
    
    func testVoiceInputValidationMalicious() {
        // Given - malicious input
        let maliciousInput = "Create button; system(\"rm -rf /\");"
        
        // When
        let isValid = codegenModule.validateVoiceInput(maliciousInput)
        
        // Then
        XCTAssertFalse(isValid)
    }
    
    func testUnsupportedComponentType() {
        // Given
        let voiceCommand = VoiceCommand(
            componentType: "unsupported",
            parameters: [:]
        )
        
        // When
        let generatedCode = codegenModule.generateFromVoiceCommand(voiceCommand)
        
        // Then
        XCTAssertTrue(generatedCode.contains("// Unsupported component type"))
    }
    
    func testCompleteViewGeneration() {
        // Given
        let components: [UIComponent] = [
            .button(ButtonConfig(title: "Login", action: "handleLogin", style: .primary)),
            .button(ButtonConfig(title: "Cancel", action: "handleCancel", style: .secondary))
        ]
        
        // When
        let generatedView = codegenModule.generateView(components: components)
        
        // Then
        XCTAssertTrue(generatedView.contains("struct GeneratedView: View"))
        XCTAssertTrue(generatedView.contains("var body: some View"))
        XCTAssertTrue(generatedView.contains("VStack {"))
        XCTAssertTrue(generatedView.contains("Button(\"Login\")"))
        XCTAssertTrue(generatedView.contains("Button(\"Cancel\")"))
    }
}