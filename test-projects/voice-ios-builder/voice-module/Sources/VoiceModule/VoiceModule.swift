import Foundation
import Speech
import AVFoundation

// MARK: - Main VoiceModule Public Interface

/// Main entry point for Voice Recognition and Command Parsing functionality
public class VoiceModule {
    
    // MARK: - Public Properties
    
    public let voiceRecognition: VoiceRecognition
    public let commandParser: VoiceCommandParser
    
    // MARK: - Initialization
    
    public init() {
        self.voiceRecognition = VoiceRecognition()
        self.commandParser = VoiceCommandParser()
    }
    
    // MARK: - Convenience Methods
    
    /// Request all necessary permissions for voice recognition
    public func requestAllPermissions(completion: @escaping (Bool) -> Void) {
        voiceRecognition.requestSpeechPermission { speechAuthorized in
            if speechAuthorized {
                self.voiceRecognition.requestMicrophonePermission { micAuthorized in
                    completion(micAuthorized)
                }
            } else {
                completion(false)
            }
        }
    }
    
    /// Start listening and processing voice commands
    public func startVoiceCommandRecognition(
        onCommandReceived: @escaping (VoiceCommandIntent) -> Void,
        onError: @escaping (Error) -> Void
    ) {
        voiceRecognition.startListening { result in
            switch result {
            case .success:
                // In a real implementation, this would be connected to the speech recognition delegate
                // For now, this is a minimal implementation
                break
            case .failure(let error):
                onError(error)
            }
        }
    }
    
    /// Stop voice command recognition
    public func stopVoiceCommandRecognition() {
        voiceRecognition.stopListening()
    }
}

// MARK: - Re-export Public Types

// Re-export all the types so users only need to import VoiceModule
public typealias VoiceModuleRecognitionState = VoiceRecognitionState
public typealias VoiceModuleRecognitionError = VoiceRecognitionError
public typealias VoiceModuleCommandAction = VoiceCommandAction
public typealias VoiceModuleComponentType = ComponentType
public typealias VoiceModuleCommandError = VoiceCommandError
public typealias VoiceModuleCommandIntent = VoiceCommandIntent