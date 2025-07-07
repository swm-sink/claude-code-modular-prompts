import Foundation

// MARK: - App States
enum AppState: Equatable {
    case idle
    case recording
    case processing
    case generating
    case completed
    case error(String)
    
    static func == (lhs: AppState, rhs: AppState) -> Bool {
        switch (lhs, rhs) {
        case (.idle, .idle), (.recording, .recording), (.processing, .processing), 
             (.generating, .generating), (.completed, .completed):
            return true
        case (.error(let lhsMessage), .error(let rhsMessage)):
            return lhsMessage == rhsMessage
        default:
            return false
        }
    }
}

// MARK: - Voice Request Model
struct VoiceRequest {
    let id: UUID
    let originalText: String
    let processedText: String
    let intent: VoiceIntent
    let timestamp: Date
    
    init(originalText: String, processedText: String, intent: VoiceIntent) {
        self.id = UUID()
        self.originalText = originalText
        self.processedText = processedText
        self.intent = intent
        self.timestamp = Date()
    }
}

// MARK: - Voice Intent
enum VoiceIntent {
    case createApp
    case modifyApp
    case deleteApp
    case openApp
    case unknown
}

// MARK: - Project Model
struct Project {
    let id: UUID
    let name: String
    let description: String
    var generatedCode: String
    let createdAt: Date
    var updatedAt: Date
    var status: ProjectStatus
    
    init(name: String, description: String, generatedCode: String) {
        self.id = UUID()
        self.name = name
        self.description = description
        self.generatedCode = generatedCode
        self.createdAt = Date()
        self.updatedAt = Date()
        self.status = .created
    }
    
    // Helper initializer for tests
    init(id: UUID = UUID(), name: String, description: String, generatedCode: String, createdAt: Date = Date(), updatedAt: Date = Date(), status: ProjectStatus = .created) {
        self.id = id
        self.name = name
        self.description = description
        self.generatedCode = generatedCode
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.status = status
    }
    
    // Method to update code
    mutating func updateCode(_ newCode: String) {
        self.generatedCode = newCode
        self.updatedAt = Date()
    }
}

// MARK: - Project Status
enum ProjectStatus {
    case created
    case building
    case ready
    case running
    case error(String)
}

// MARK: - Error Types
enum ProjectManagerError: Error, LocalizedError {
    case projectNotFound
    case invalidProjectData
    case simulatorNotAvailable
    case buildFailed(String)
    case fileSystemError(String)
    
    var errorDescription: String? {
        switch self {
        case .projectNotFound:
            return "Project not found"
        case .invalidProjectData:
            return "Invalid project data"
        case .simulatorNotAvailable:
            return "iOS Simulator not available"
        case .buildFailed(let message):
            return "Build failed: \(message)"
        case .fileSystemError(let message):
            return "File system error: \(message)"
        }
    }
}

enum VoiceProcessingError: Error, LocalizedError {
    case recordingFailed
    case processingFailed
    case recognitionFailed
    case noPermission
    
    var errorDescription: String? {
        switch self {
        case .recordingFailed:
            return "Voice recording failed"
        case .processingFailed:
            return "Voice processing failed"
        case .recognitionFailed:
            return "Voice recognition failed"
        case .noPermission:
            return "Microphone permission not granted"
        }
    }
}

enum CodeGenerationError: Error, LocalizedError {
    case invalidRequest
    case generationFailed(String)
    case networkError
    case timeout
    
    var errorDescription: String? {
        switch self {
        case .invalidRequest:
            return "Invalid code generation request"
        case .generationFailed(let message):
            return "Code generation failed: \(message)"
        case .networkError:
            return "Network error during code generation"
        case .timeout:
            return "Code generation timed out"
        }
    }
}