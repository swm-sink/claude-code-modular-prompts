import XCTest
import Speech
import AVFoundation
@testable import VoiceModule

final class VoiceRecognitionTests: XCTestCase {
    
    var voiceRecognition: VoiceRecognition!
    
    override func setUp() {
        super.setUp()
        voiceRecognition = VoiceRecognition()
    }
    
    override func tearDown() {
        voiceRecognition = nil
        super.tearDown()
    }
    
    // MARK: - RED Phase Tests (These should FAIL initially)
    
    func testVoiceRecognitionInitialization() {
        // RED: This test should fail because VoiceRecognition class doesn't exist yet
        XCTAssertNotNil(voiceRecognition)
        XCTAssertFalse(voiceRecognition.isListening)
        XCTAssertEqual(voiceRecognition.recognitionState, .idle)
    }
    
    func testSpeechFrameworkPermissionRequest() {
        // RED: This test should fail because method doesn't exist
        let expectation = XCTestExpectation(description: "Permission request")
        
        voiceRecognition.requestSpeechPermission { authorized in
            XCTAssertTrue(authorized || !authorized) // Should receive a boolean response
            expectation.fulfill()
        }
        
        wait(for: [expectation], timeout: 5.0)
    }
    
    func testMicrophonePermissionRequest() {
        // RED: This test should fail because method doesn't exist
        let expectation = XCTestExpectation(description: "Microphone permission")
        
        voiceRecognition.requestMicrophonePermission { authorized in
            XCTAssertTrue(authorized || !authorized) // Should receive a boolean response
            expectation.fulfill()
        }
        
        wait(for: [expectation], timeout: 5.0)
    }
    
    func testStartListeningFailsWithoutPermissions() {
        // RED: This test should fail because startListening method doesn't exist
        let expectation = XCTestExpectation(description: "Start listening without permissions")
        
        voiceRecognition.startListening { result in
            switch result {
            case .success:
                XCTFail("Should not succeed without permissions")
            case .failure(let error):
                XCTAssertEqual(error, .permissionDenied)
            }
            expectation.fulfill()
        }
        
        wait(for: [expectation], timeout: 2.0)
    }
    
    func testStopListening() {
        // RED: This test should fail because stopListening method doesn't exist
        voiceRecognition.stopListening()
        XCTAssertFalse(voiceRecognition.isListening)
        XCTAssertEqual(voiceRecognition.recognitionState, .idle)
    }
    
    func testVoiceRecognitionStateTransitions() {
        // RED: This test should fail because state management doesn't exist
        XCTAssertEqual(voiceRecognition.recognitionState, .idle)
        
        // These should transition states
        voiceRecognition.prepareForRecognition()
        XCTAssertEqual(voiceRecognition.recognitionState, .preparing)
        
        // Simulate successful start
        voiceRecognition.onRecognitionStart()
        XCTAssertEqual(voiceRecognition.recognitionState, .listening)
        
        // Simulate stop
        voiceRecognition.stopListening()
        XCTAssertEqual(voiceRecognition.recognitionState, .idle)
    }
    
    func testPerformanceBenchmark() {
        // RED: Performance test should fail initially
        measure {
            let startTime = CFAbsoluteTimeGetCurrent()
            voiceRecognition.processAudioBuffer(mockAudioBuffer())
            let timeElapsed = CFAbsoluteTimeGetCurrent() - startTime
            
            // Target: <200ms processing time
            XCTAssertLessThan(timeElapsed, 0.2, "Voice processing should be under 200ms")
        }
    }
    
    // MARK: - Helper Methods
    
    private func mockAudioBuffer() -> AVAudioPCMBuffer {
        let format = AVAudioFormat(standardFormatWithSampleRate: 44100, channels: 1)!
        let buffer = AVAudioPCMBuffer(pcmFormat: format, frameCapacity: 1024)!
        buffer.frameLength = 1024
        return buffer
    }
}