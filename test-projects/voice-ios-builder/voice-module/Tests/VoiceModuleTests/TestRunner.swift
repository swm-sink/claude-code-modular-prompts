import Foundation
@testable import VoiceModule

// Simple test runner for environments where XCTest might not be available
struct TestRunner {
    static func runAllTests() {
        print("🧪 Running Voice Module Tests...")
        
        runVoiceRecognitionTests()
        runVoiceCommandParserTests()
        runPerformanceTests()
        
        print("✅ All tests completed!")
    }
    
    static func runVoiceRecognitionTests() {
        print("\n📱 Testing VoiceRecognition...")
        
        let voiceRecognition = VoiceRecognition()
        
        // Test initialization
        assert(!voiceRecognition.isListening, "VoiceRecognition should not be listening initially")
        assert(voiceRecognition.recognitionState == .idle, "VoiceRecognition should start in idle state")
        print("✓ Initialization test passed")
        
        // Test state transitions
        voiceRecognition.prepareForRecognition()
        assert(voiceRecognition.recognitionState == .preparing, "State should be preparing")
        
        voiceRecognition.onRecognitionStart()
        assert(voiceRecognition.recognitionState == .listening, "State should be listening")
        assert(voiceRecognition.isListening, "Should be listening")
        
        voiceRecognition.stopListening()
        assert(voiceRecognition.recognitionState == .idle, "State should be idle after stopping")
        assert(!voiceRecognition.isListening, "Should not be listening after stopping")
        print("✓ State transition tests passed")
    }
    
    static func runVoiceCommandParserTests() {
        print("\n🗣️ Testing VoiceCommandParser...")
        
        let parser = VoiceCommandParser()
        
        // Test initialization
        assert(parser.supportedCommands.count > 0, "Should have supported commands")
        assert(parser.supportedCommands.contains("create"), "Should support 'create' command")
        assert(parser.supportedCommands.contains("button"), "Should support 'button' component")
        print("✓ Initialization test passed")
        
        // Test basic command parsing
        let result = parser.parseCommand("create button")
        switch result {
        case .success(let intent):
            assert(intent.action == .createComponent, "Should parse 'create' action")
            assert(intent.componentType == .button, "Should parse 'button' component")
            assert(intent.confidence > 0.5, "Confidence should be reasonable")
            print("✓ Basic command parsing test passed")
        case .failure:
            fatalError("Should successfully parse 'create button'")
        }
        
        // Test complex command parsing
        let complexResult = parser.parseCommand("create red button with title hello world")
        switch complexResult {
        case .success(let intent):
            assert(intent.action == .createComponent, "Should parse 'create' action")
            assert(intent.componentType == .button, "Should parse 'button' component")
            assert(intent.parameters["color"] == "red", "Should extract color parameter")
            assert(intent.parameters["title"] == "hello world", "Should extract title parameter")
            print("✓ Complex command parsing test passed")
        case .failure:
            fatalError("Should successfully parse complex command")
        }
        
        // Test input sanitization
        let maliciousInput = "create button'; DROP TABLE users; --"
        let sanitized = parser.sanitizeInput(maliciousInput)
        assert(!sanitized.contains("DROP TABLE"), "Should remove SQL injection attempt")
        assert(!sanitized.contains("';"), "Should remove SQL injection pattern")
        assert(!sanitized.contains("--"), "Should remove SQL comment pattern")
        assert(sanitized.contains("create button"), "Should preserve valid command")
        print("✓ Input sanitization test passed")
        
        // Test security violation detection
        let injectionAttempt = "create button; system('rm -rf /')"
        let securityResult = parser.parseCommand(injectionAttempt)
        switch securityResult {
        case .success:
            fatalError("Should not parse malicious command")
        case .failure(let error):
            assert(error == .securityViolation, "Should detect security violation")
            print("✓ Security violation detection test passed")
        }
        
        // Test invalid command
        let invalidResult = parser.parseCommand("xyz invalid command abc")
        switch invalidResult {
        case .success:
            fatalError("Should not parse invalid command")
        case .failure(let error):
            assert(error == .unrecognizedCommand, "Should return unrecognized command error")
            print("✓ Invalid command test passed")
        }
    }
    
    static func runPerformanceTests() {
        print("\n⚡ Testing Performance...")
        
        let parser = VoiceCommandParser()
        let voiceRecognition = VoiceRecognition()
        
        // Test command parsing performance
        let commands = [
            "create button",
            "add navigation",
            "delete view",
            "modify label with text hello"
        ]
        
        let startTime = CFAbsoluteTimeGetCurrent()
        for command in commands {
            _ = parser.parseCommand(command)
        }
        let parsingTime = CFAbsoluteTimeGetCurrent() - startTime
        
        assert(parsingTime < 0.2, "Command parsing should be fast (was \(parsingTime)s)")
        print("✓ Command parsing performance test passed (\(String(format: "%.3f", parsingTime))s)")
        
        // Test audio buffer processing performance (mock)
        let format = AVAudioFormat(standardFormatWithSampleRate: 44100, channels: 1)!
        let buffer = AVAudioPCMBuffer(pcmFormat: format, frameCapacity: 1024)!
        buffer.frameLength = 1024
        
        let bufferStartTime = CFAbsoluteTimeGetCurrent()
        voiceRecognition.processAudioBuffer(buffer)
        let bufferTime = CFAbsoluteTimeGetCurrent() - bufferStartTime
        
        assert(bufferTime < 0.2, "Audio buffer processing should be under 200ms (was \(bufferTime)s)")
        print("✓ Audio buffer processing performance test passed (\(String(format: "%.3f", bufferTime))s)")
    }
}

// Run tests if this file is executed directly
#if DEBUG
TestRunner.runAllTests()
#endif