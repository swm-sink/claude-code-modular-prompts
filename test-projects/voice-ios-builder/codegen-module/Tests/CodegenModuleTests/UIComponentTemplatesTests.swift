import XCTest
@testable import CodegenModule

final class UIComponentTemplatesTests: XCTestCase {
    
    var templates: UIComponentTemplates!
    
    override func setUp() {
        super.setUp()
        templates = UIComponentTemplates()
    }
    
    override func tearDown() {
        templates = nil
        super.tearDown()
    }
    
    // RED: This test should fail initially
    func testNavigationViewTemplate() {
        // Given
        let navigationConfig = NavigationConfig(
            title: "Settings",
            content: "Text(\"Settings Content\")"
        )
        
        // When
        let generatedCode = templates.generateNavigationView(config: navigationConfig)
        
        // Then
        let expectedCode = """
        NavigationView {
            Text("Settings Content")
                .navigationTitle("Settings")
        }
        """
        
        XCTAssertEqual(generatedCode.trimmingCharacters(in: .whitespacesAndNewlines), 
                      expectedCode.trimmingCharacters(in: .whitespacesAndNewlines))
    }
    
    func testFormTemplate() {
        // Given
        let formConfig = FormConfig(
            fields: [
                FormField(name: "username", type: .text, placeholder: "Enter username"),
                FormField(name: "password", type: .secure, placeholder: "Enter password")
            ]
        )
        
        // When
        let generatedCode = templates.generateForm(config: formConfig)
        
        // Then
        let expectedCode = """
        Form {
            TextField("Enter username", text: $username)
            SecureField("Enter password", text: $password)
        }
        """
        
        XCTAssertEqual(generatedCode.trimmingCharacters(in: .whitespacesAndNewlines), 
                      expectedCode.trimmingCharacters(in: .whitespacesAndNewlines))
    }
    
    func testListTemplate() {
        // Given
        let listConfig = ListConfig(
            items: ["Item 1", "Item 2", "Item 3"],
            rowAction: "handleRowTap"
        )
        
        // When
        let generatedCode = templates.generateList(config: listConfig)
        
        // Then
        let expectedCode = """
        List {
            ForEach(["Item 1", "Item 2", "Item 3"], id: \\.self) { item in
                Text(item)
                    .onTapGesture {
                        handleRowTap(item)
                    }
            }
        }
        """
        
        XCTAssertEqual(generatedCode.trimmingCharacters(in: .whitespacesAndNewlines), 
                      expectedCode.trimmingCharacters(in: .whitespacesAndNewlines))
    }
    
    func testTemplateParameterValidation() {
        // Given - invalid navigation config
        let invalidConfig = NavigationConfig(
            title: "", // empty title
            content: ""  // empty content
        )
        
        // When/Then - should handle gracefully
        XCTAssertNoThrow(templates.generateNavigationView(config: invalidConfig))
        
        let result = templates.generateNavigationView(config: invalidConfig)
        XCTAssertTrue(result.contains("NavigationView"))
    }
}