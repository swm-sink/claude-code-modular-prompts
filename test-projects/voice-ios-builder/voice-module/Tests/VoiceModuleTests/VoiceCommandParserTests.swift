import XCTest
@testable import VoiceModule

final class VoiceCommandParserTests: XCTestCase {
    
    var parser: VoiceCommandParser!
    
    override func setUp() {
        super.setUp()
        parser = VoiceCommandParser()
    }
    
    override func tearDown() {
        parser = nil
        super.tearDown()
    }
    
    // MARK: - RED Phase Tests (These should FAIL initially)
    
    func testParserInitialization() {
        // RED: This test should fail because VoiceCommandParser class doesn't exist yet
        XCTAssertNotNil(parser)
        XCTAssertTrue(parser.supportedCommands.count > 0)
    }
    
    func testParseCreateButtonCommand() {
        // RED: This test should fail because parseCommand method doesn't exist
        let input = "create button"
        let result = parser.parseCommand(input)
        
        switch result {
        case .success(let intent):
            XCTAssertEqual(intent.action, .createComponent)
            XCTAssertEqual(intent.componentType, .button)
            XCTAssertNotNil(intent.parameters)
        case .failure:
            XCTFail("Should successfully parse 'create button' command")
        }
    }
    
    func testParseAddNavigationCommand() {
        // RED: This test should fail because parseCommand method doesn't exist
        let input = "add navigation"
        let result = parser.parseCommand(input)
        
        switch result {
        case .success(let intent):
            XCTAssertEqual(intent.action, .addComponent)
            XCTAssertEqual(intent.componentType, .navigation)
        case .failure:
            XCTFail("Should successfully parse 'add navigation' command")
        }
    }
    
    func testParseComplexCommand() {
        // RED: This test should fail because parseCommand method doesn't exist
        let input = "create red button with title hello world"
        let result = parser.parseCommand(input)
        
        switch result {
        case .success(let intent):
            XCTAssertEqual(intent.action, .createComponent)
            XCTAssertEqual(intent.componentType, .button)
            XCTAssertEqual(intent.parameters["color"], "red")
            XCTAssertEqual(intent.parameters["title"], "hello world")
        case .failure:
            XCTFail("Should successfully parse complex command")
        }
    }
    
    func testParseInvalidCommand() {
        // RED: This test should fail because parseCommand method doesn't exist
        let input = "xyz invalid command abc"
        let result = parser.parseCommand(input)
        
        switch result {
        case .success:
            XCTFail("Should not successfully parse invalid command")
        case .failure(let error):
            XCTAssertEqual(error, .unrecognizedCommand)
        }
    }
    
    func testInputSanitization() {
        // RED: This test should fail because sanitizeInput method doesn't exist
        let maliciousInput = "create button'; DROP TABLE users; --"
        let sanitized = parser.sanitizeInput(maliciousInput)
        
        XCTAssertFalse(sanitized.contains("DROP TABLE"))
        XCTAssertFalse(sanitized.contains("';"))
        XCTAssertFalse(sanitized.contains("--"))
        XCTAssertTrue(sanitized.contains("create button"))
    }
    
    func testCodeInjectionPrevention() {
        // RED: This test should fail because security validation doesn't exist
        let injectionAttempts = [
            "create button; system('rm -rf /')",
            "add view <script>alert('xss')</script>",
            "delete * from database",
            "eval(maliciousCode)",
            "import os; os.system('harmful')"
        ]
        
        for attempt in injectionAttempts {
            let result = parser.parseCommand(attempt)
            switch result {
            case .success:
                XCTFail("Should not parse malicious command: \(attempt)")
            case .failure(let error):
                XCTAssertEqual(error, .securityViolation)
            }
        }
    }
    
    func testSupportedCommandsList() {
        // RED: This test should fail because supportedCommands property doesn't exist
        let commands = parser.supportedCommands
        
        XCTAssertTrue(commands.contains("create"))
        XCTAssertTrue(commands.contains("add"))
        XCTAssertTrue(commands.contains("delete"))
        XCTAssertTrue(commands.contains("modify"))
        XCTAssertTrue(commands.contains("button"))
        XCTAssertTrue(commands.contains("navigation"))
        XCTAssertTrue(commands.contains("view"))
        XCTAssertTrue(commands.contains("label"))
    }
    
    func testParseConfidenceScore() {
        // RED: This test should fail because confidence scoring doesn't exist
        let input = "create button"
        let result = parser.parseCommand(input)
        
        switch result {
        case .success(let intent):
            XCTAssertGreaterThan(intent.confidence, 0.8)
            XCTAssertLessThanOrEqual(intent.confidence, 1.0)
        case .failure:
            XCTFail("Should successfully parse command and provide confidence")
        }
    }
    
    func testParsingPerformance() {
        // RED: Performance test should fail initially
        let commands = [
            "create button",
            "add navigation",
            "delete view",
            "modify label with text hello"
        ]
        
        measure {
            for command in commands {
                let startTime = CFAbsoluteTimeGetCurrent()
                _ = parser.parseCommand(command)
                let timeElapsed = CFAbsoluteTimeGetCurrent() - startTime
                
                // Target: <50ms per command parsing
                XCTAssertLessThan(timeElapsed, 0.05, "Command parsing should be under 50ms")
            }
        }
    }
    
    func testNaturalLanguageVariations() {
        // RED: This test should fail because natural language processing doesn't exist
        let variations = [
            "make a button",
            "I want to create a button",
            "please add a button for me",
            "can you create a new button",
            "add button component"
        ]
        
        for variation in variations {
            let result = parser.parseCommand(variation)
            switch result {
            case .success(let intent):
                XCTAssertEqual(intent.action, .createComponent)
                XCTAssertEqual(intent.componentType, .button)
            case .failure:
                XCTFail("Should parse natural language variation: \(variation)")
            }
        }
    }
}