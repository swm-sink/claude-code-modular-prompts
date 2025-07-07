import Foundation
import VoiceModule

// Simple test app to verify Voice Module functionality
print("🧪 Voice Module Test App Starting...")

// Test VoiceRecognition
print("\n📱 Testing VoiceRecognition...")
let voiceRecognition = VoiceRecognition()

print("Initial state: \(voiceRecognition.recognitionState)")
print("Is listening: \(voiceRecognition.isListening)")

// Test state transitions
voiceRecognition.prepareForRecognition()
print("After prepare: \(voiceRecognition.recognitionState)")

voiceRecognition.onRecognitionStart()
print("After start: \(voiceRecognition.recognitionState)")
print("Is listening: \(voiceRecognition.isListening)")

voiceRecognition.stopListening()
print("After stop: \(voiceRecognition.recognitionState)")
print("Is listening: \(voiceRecognition.isListening)")

// Test VoiceCommandParser
print("\n🗣️ Testing VoiceCommandParser...")
let parser = VoiceCommandParser()

print("Supported commands: \(parser.supportedCommands.joined(separator: ", "))")

// Test basic command
let basicCommand = "create button"
print("\nTesting command: '\(basicCommand)'")
let basicResult = parser.parseCommand(basicCommand)
switch basicResult {
case .success(let intent):
    print("✓ Success! Action: \(intent.action), Component: \(intent.componentType), Confidence: \(intent.confidence)")
case .failure(let error):
    print("✗ Failed: \(error)")
}

// Test complex command
let complexCommand = "create red button with title hello world"
print("\nTesting command: '\(complexCommand)'")
let complexResult = parser.parseCommand(complexCommand)
switch complexResult {
case .success(let intent):
    print("✓ Success! Action: \(intent.action), Component: \(intent.componentType)")
    print("  Parameters: \(intent.parameters)")
    print("  Confidence: \(intent.confidence)")
case .failure(let error):
    print("✗ Failed: \(error)")
}

// Test security
let maliciousCommand = "create button; DROP TABLE users"
print("\nTesting malicious command: '\(maliciousCommand)'")
let securityResult = parser.parseCommand(maliciousCommand)
switch securityResult {
case .success(let intent):
    print("✗ Should have been blocked! \(intent)")
case .failure(let error):
    print("✓ Security worked: \(error)")
}

// Test input sanitization
let dirtyInput = "create button'; DROP TABLE users; --"
let cleanInput = parser.sanitizeInput(dirtyInput)
print("\nSanitization test:")
print("Input:  '\(dirtyInput)'")
print("Output: '\(cleanInput)'")

// Test performance
print("\n⚡ Performance Testing...")
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
let totalTime = CFAbsoluteTimeGetCurrent() - startTime
print("Parsed \(commands.count) commands in \(String(format: "%.3f", totalTime))s")
print("Average: \(String(format: "%.3f", totalTime / Double(commands.count)))s per command")

// Test natural language variations
print("\n🗨️ Testing Natural Language Variations...")
let variations = [
    "make a button",
    "I want to create a button", 
    "please add a button for me",
    "can you create a new button"
]

for variation in variations {
    let result = parser.parseCommand(variation)
    switch result {
    case .success(let intent):
        print("✓ '\(variation)' → \(intent.action) \(intent.componentType)")
    case .failure:
        print("✗ Failed to parse: '\(variation)'")
    }
}

print("\n🎉 Voice Module Test Complete!")

// Run comprehensive benchmarks
print("\n" + String(repeating: "=", count: 60))
PerformanceBenchmark.runBenchmarks()
print(String(repeating: "=", count: 60))

// Run integration demo
let demo = IntegrationDemo()
demo.runDemo()