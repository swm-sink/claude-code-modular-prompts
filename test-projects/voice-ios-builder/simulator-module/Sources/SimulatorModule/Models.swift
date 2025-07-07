import Foundation

// MARK: - Simulator Models

public struct Simulator {
    public let udid: String
    public let name: String
    public let deviceType: String
    public let runtime: String
    public let state: String
    
    public init(udid: String, name: String, deviceType: String, runtime: String, state: String) {
        self.udid = udid
        self.name = name
        self.deviceType = deviceType
        self.runtime = runtime
        self.state = state
    }
}

// MARK: - Build Models

public struct BuildResult {
    public let success: Bool
    public let appPath: String
    public let buildLog: String
    public let buildTime: TimeInterval
    
    public init(success: Bool, appPath: String, buildLog: String, buildTime: TimeInterval) {
        self.success = success
        self.appPath = appPath
        self.buildLog = buildLog
        self.buildTime = buildTime
    }
}

public struct DeployResult {
    public let success: Bool
    public let bundleIdentifier: String
    public let deployLog: String
    
    public init(success: Bool, bundleIdentifier: String, deployLog: String) {
        self.success = success
        self.bundleIdentifier = bundleIdentifier
        self.deployLog = deployLog
    }
}

public struct LaunchResult {
    public let success: Bool
    public let processId: String
    public let launchLog: String
    
    public init(success: Bool, processId: String, launchLog: String) {
        self.success = success
        self.processId = processId
        self.launchLog = launchLog
    }
}

public struct BuildConfiguration {
    public let projectPath: String
    public let scheme: String
    public let configuration: String
    public let architecture: String
    
    public init(projectPath: String, scheme: String, configuration: String, architecture: String) {
        self.projectPath = projectPath
        self.scheme = scheme
        self.configuration = configuration
        self.architecture = architecture
    }
}

public struct BuildProgress {
    public let phase: String
    public let percentage: Double
    public let message: String
    
    public init(phase: String, percentage: Double, message: String) {
        self.phase = phase
        self.percentage = percentage
        self.message = message
    }
}

// MARK: - Screenshot Models

public struct ScreenshotResult {
    public let success: Bool
    public let filePath: String
    public let metadata: ScreenshotMetadata?
    public let captureTime: TimeInterval
    
    public init(success: Bool, filePath: String, metadata: ScreenshotMetadata? = nil, captureTime: TimeInterval) {
        self.success = success
        self.filePath = filePath
        self.metadata = metadata
        self.captureTime = captureTime
    }
}

public struct ScreenshotMetadata {
    public let testCase: String
    public let timestamp: Date
    public let deviceInfo: String
    public let appVersion: String
    
    public init(testCase: String, timestamp: Date, deviceInfo: String, appVersion: String) {
        self.testCase = testCase
        self.timestamp = timestamp
        self.deviceInfo = deviceInfo
        self.appVersion = appVersion
    }
}

public struct ScreenshotValidationResult {
    public let isValid: Bool
    public let fileSize: Int64
    public let width: Int
    public let height: Int
    public let format: String
    
    public init(isValid: Bool, fileSize: Int64, width: Int, height: Int, format: String) {
        self.isValid = isValid
        self.fileSize = fileSize
        self.width = width
        self.height = height
        self.format = format
    }
}

// MARK: - Enums

public enum ScreenshotFormat {
    case png
    case jpeg
    case tiff
    
    public var fileExtension: String {
        switch self {
        case .png: return "png"
        case .jpeg: return "jpg"
        case .tiff: return "tiff"
        }
    }
}