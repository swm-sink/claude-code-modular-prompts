import Foundation

// MARK: - Voice Recognition Types

public enum VoiceRecognitionState {
    case idle
    case preparing
    case listening
    case processing
    case error(VoiceRecognitionError)
}

public enum VoiceRecognitionError: Error, Equatable {
    case permissionDenied
    case microphoneUnavailable
    case speechRecognitionUnavailable
    case networkError
    case processingTimeout
    case unknownError
}

// MARK: - Voice Command Types

public enum VoiceCommandAction: String, CaseIterable {
    case createComponent = "create"
    case addComponent = "add"
    case deleteComponent = "delete"
    case modifyComponent = "modify"
}

public enum ComponentType: String, CaseIterable {
    case button = "button"
    case navigation = "navigation"
    case view = "view"
    case label = "label"
    case textField = "textfield"
    case imageView = "imageview"
}

public enum VoiceCommandError: Error, Equatable {
    case unrecognizedCommand
    case securityViolation
    case invalidParameters
    case processingError
}

// MARK: - Voice Command Intent

public struct VoiceCommandIntent {
    public let action: VoiceCommandAction
    public let componentType: ComponentType
    public let parameters: [String: String]
    public let confidence: Double
    public let timestamp: Date
    
    public init(
        action: VoiceCommandAction,
        componentType: ComponentType,
        parameters: [String: String] = [:],
        confidence: Double = 1.0,
        timestamp: Date = Date()
    ) {
        self.action = action
        self.componentType = componentType
        self.parameters = parameters
        self.confidence = confidence
        self.timestamp = timestamp
    }
}

// MARK: - Result Types

public typealias VoiceRecognitionResult = Result<Void, VoiceRecognitionError>
public typealias VoiceCommandResult = Result<VoiceCommandIntent, VoiceCommandError>
public typealias PermissionResult = (Bool) -> Void