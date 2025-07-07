import Foundation

// MARK: - Simulator Errors

public enum SimulatorError: LocalizedError {
    case invalidUDID
    case simulatorNotFound
    case simulatorAlreadyRunning
    case simulatorNotRunning
    case launchFailed(String)
    case shutdownFailed(String)
    case commandExecutionFailed(String)
    case xcrunNotFound
    
    public var errorDescription: String? {
        switch self {
        case .invalidUDID:
            return "Invalid simulator UDID provided"
        case .simulatorNotFound:
            return "Simulator not found"
        case .simulatorAlreadyRunning:
            return "Simulator is already running"
        case .simulatorNotRunning:
            return "Simulator is not running"
        case .launchFailed(let message):
            return "Failed to launch simulator: \(message)"
        case .shutdownFailed(let message):
            return "Failed to shutdown simulator: \(message)"
        case .commandExecutionFailed(let message):
            return "Command execution failed: \(message)"
        case .xcrunNotFound:
            return "xcrun command not found. Xcode may not be installed or properly configured"
        }
    }
}

// MARK: - Build Errors

public enum BuildError: LocalizedError {
    case invalidProjectPath
    case invalidScheme
    case buildFailed(String)
    case deploymentFailed(String)
    case launchFailed(String)
    case xcodebuildNotFound
    case invalidConfiguration
    case missingBuildArtifacts
    case archiveNotFound
    
    public var errorDescription: String? {
        switch self {
        case .invalidProjectPath:
            return "Invalid project path provided"
        case .invalidScheme:
            return "Invalid scheme provided"
        case .buildFailed(let message):
            return "Build failed: \(message)"
        case .deploymentFailed(let message):
            return "Deployment failed: \(message)"
        case .launchFailed(let message):
            return "App launch failed: \(message)"
        case .xcodebuildNotFound:
            return "xcodebuild command not found. Xcode may not be installed or properly configured"
        case .invalidConfiguration:
            return "Invalid build configuration"
        case .missingBuildArtifacts:
            return "Build artifacts not found"
        case .archiveNotFound:
            return "Archive not found at expected location"
        }
    }
}

// MARK: - Screenshot Errors

public enum ScreenshotError: LocalizedError {
    case invalidSimulatorUDID
    case simulatorNotRunning
    case captureCommandFailed(String)
    case invalidOutputPath
    case fileCreationFailed
    case unsupportedFormat
    case validationFailed(String)
    case directoryCreationFailed
    
    public var errorDescription: String? {
        switch self {
        case .invalidSimulatorUDID:
            return "Invalid simulator UDID provided"
        case .simulatorNotRunning:
            return "Simulator is not running"
        case .captureCommandFailed(let message):
            return "Screenshot capture command failed: \(message)"
        case .invalidOutputPath:
            return "Invalid output path provided"
        case .fileCreationFailed:
            return "Failed to create screenshot file"
        case .unsupportedFormat:
            return "Unsupported screenshot format"
        case .validationFailed(let message):
            return "Screenshot validation failed: \(message)"
        case .directoryCreationFailed:
            return "Failed to create output directory"
        }
    }
}