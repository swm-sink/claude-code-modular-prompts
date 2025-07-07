import Foundation
import Combine
import VoiceModule
@preconcurrency import CodegenModule
import SimulatorModule

#if canImport(AVFoundation)
import AVFoundation
#endif

#if canImport(Speech)
import Speech
#endif

@MainActor
public class AppCoordinator: ObservableObject {
    
    // MARK: - Published Properties
    @Published var currentState: AppState = .idle
    @Published var currentProject: Project?
    @Published var recentProjects: [Project] = []
    @Published var feedbackMessage: String = ""
    @Published var isProcessing: Bool = false
    
    // MARK: - Private Properties
    private let projectManager: ProjectManager
    private let voiceRecognition: VoiceRecognition
    private let codeGenerator: SwiftCodeGenerator
    private let simulatorManager: SimulatorManager
    private var cancellables = Set<AnyCancellable>()
    
    #if canImport(AVFoundation) && !os(macOS)
    private var audioEngine: AVAudioEngine?
    #endif
    
    #if canImport(Speech)
    private var recognitionTask: SFSpeechRecognitionTask?
    #endif
    
    // MARK: - Initialization
    public init(projectManager: ProjectManager = ProjectManager()) {
        self.projectManager = projectManager
        self.voiceRecognition = VoiceRecognition()
        self.codeGenerator = SwiftCodeGenerator()
        self.simulatorManager = SimulatorManager()
        setupAudioSession()
    }
    
    // MARK: - Voice Recording
    public func startVoiceRecording(completion: @escaping (Bool) -> Void) {
        guard currentState == .idle else {
            completion(false)
            return
        }
        
        // Use real VoiceRecognition module
        voiceRecognition.requestMicrophonePermission { [weak self] micGranted in
            guard let self = self, micGranted else {
                DispatchQueue.main.async {
                    self?.currentState = .error("Microphone permission denied")
                    completion(false)
                }
                return
            }
            
            self.voiceRecognition.requestSpeechPermission { [weak self] speechGranted in
                guard let self = self, speechGranted else {
                    DispatchQueue.main.async {
                        self?.currentState = .error("Speech recognition permission denied")
                        completion(false)
                    }
                    return
                }
                
                DispatchQueue.main.async {
                    self.currentState = .recording
                    self.feedbackMessage = "Listening..."
                    self.isProcessing = true
                    
                    // Start real voice recognition
                    self.voiceRecognition.startListening { result in
                        DispatchQueue.main.async {
                            switch result {
                            case .success:
                                completion(true)
                                // Simulate some voice input for now - in real app this would come from recognition
                                self.simulateVoiceRecording()
                            case .failure(let error):
                                self.currentState = .error("Voice recognition failed: \(error)")
                                completion(false)
                            }
                        }
                    }
                }
            }
        }
    }
    
    public func stopVoiceRecording() {
        currentState = .processing
        feedbackMessage = "Processing your request..."
        
        // Stop real voice recognition
        voiceRecognition.stopListening()
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.0) {
            self.isProcessing = false
            self.currentState = .idle
            self.feedbackMessage = ""
        }
    }
    
    // MARK: - Voice Processing
    public func processVoiceInput(_ input: String, completion: @escaping (Result<String, VoiceProcessingError>) -> Void) {
        guard !input.isEmpty else {
            completion(.failure(.processingFailed))
            return
        }
        
        currentState = .processing
        feedbackMessage = "Understanding your request..."
        
        // Simulate voice processing
        DispatchQueue.global(qos: .userInitiated).asyncAfter(deadline: .now() + 1.0) {
            let processedInput = input.trimmingCharacters(in: .whitespacesAndNewlines)
            
            DispatchQueue.main.async {
                completion(.success(processedInput.isEmpty ? input : processedInput))
            }
        }
    }
    
    // MARK: - Code Generation
    public func triggerCodeGeneration(for request: VoiceRequest, completion: @escaping (Result<String, CodeGenerationError>) -> Void) {
        currentState = .generating
        feedbackMessage = "Generating your app..."
        
        // Use real code generation module
        Task { @MainActor in
            // Parse voice request into UI components
            let components = self.parseVoiceRequestToComponents(request)
            
            // Generate code using real module on main actor
            let generatedCode = self.codeGenerator.generateView(components: components)
            
            // Back on main actor
            if !generatedCode.isEmpty {
                completion(.success(generatedCode))
                self.currentState = .completed
                self.feedbackMessage = "App generated successfully!"
            } else {
                completion(.failure(.generationFailed("Failed to generate code")))
                self.currentState = .error("Code generation failed")
            }
        }
    }
    
    // MARK: - Project Management Integration
    func createProjectFromVoiceRequest(_ request: VoiceRequest, generatedCode: String) {
        let projectName = extractProjectName(from: request.processedText)
        let projectDescription = request.processedText
        
        projectManager.createProject(
            name: projectName,
            description: projectDescription,
            generatedCode: generatedCode
        ) { [weak self] result in
            DispatchQueue.main.async {
                switch result {
                case .success(let project):
                    self?.currentProject = project
                    self?.recentProjects.insert(project, at: 0)
                    self?.feedbackMessage = "Project '\(project.name)' created successfully!"
                case .failure(let error):
                    self?.currentState = .error(error.localizedDescription)
                }
            }
        }
    }
    
    // MARK: - Private Methods
    private func setupAudioSession() {
        #if canImport(AVFoundation) && !os(macOS)
        do {
            try AVAudioSession.sharedInstance().setCategory(.playAndRecord, mode: .measurement, options: .duckOthers)
            try AVAudioSession.sharedInstance().setActive(true, options: .notifyOthersOnDeactivation)
        } catch {
            print("Failed to setup audio session: \(error)")
        }
        #else
        // Audio session setup not needed on macOS
        print("Audio session setup skipped on macOS")
        #endif
    }
    
    private func simulateVoiceRecording() {
        // Simulate 3-second recording
        DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
            self.stopVoiceRecording()
            
            // Simulate processing a test voice command
            let testInput = "Create a simple calculator app"
            self.processVoiceInput(testInput) { result in
                switch result {
                case .success(let processedInput):
                    let request = VoiceRequest(
                        originalText: testInput,
                        processedText: processedInput,
                        intent: .createApp
                    )
                    
                    self.triggerCodeGeneration(for: request) { codeResult in
                        switch codeResult {
                        case .success(let code):
                            self.createProjectFromVoiceRequest(request, generatedCode: code)
                        case .failure(let error):
                            self.currentState = .error(error.localizedDescription)
                        }
                    }
                case .failure(let error):
                    self.currentState = .error(error.localizedDescription)
                }
            }
        }
    }
    
    private func parseVoiceRequestToComponents(_ request: VoiceRequest) -> [UIComponent] {
        var components: [UIComponent] = []
        let text = request.processedText.lowercased()
        
        // Simple parsing logic - in a real app this would be more sophisticated
        if text.contains("button") {
            let title = extractButtonTitle(from: text)
            let style: ButtonStyle = text.contains("primary") ? .primary : 
                                   text.contains("destructive") ? .destructive : .secondary
            
            components.append(.button(ButtonConfig(
                title: title,
                action: "buttonAction",
                style: style
            )))
        }
        
        if text.contains("calculator") {
            // Add calculator-specific buttons
            components.append(.button(ButtonConfig(title: "0", action: "numberPressed", style: .secondary)))
            components.append(.button(ButtonConfig(title: "1", action: "numberPressed", style: .secondary)))
            components.append(.button(ButtonConfig(title: "+", action: "operatorPressed", style: .primary)))
            components.append(.button(ButtonConfig(title: "=", action: "calculate", style: .primary)))
        }
        
        // Default to a simple button if no specific components detected
        if components.isEmpty {
            components.append(.button(ButtonConfig(
                title: "Get Started",
                action: "getStarted", 
                style: .primary
            )))
        }
        
        return components
    }
    
    private func extractButtonTitle(from text: String) -> String {
        // Simple title extraction
        if text.contains("save") { return "Save" }
        if text.contains("cancel") { return "Cancel" }
        if text.contains("submit") { return "Submit" }
        if text.contains("login") { return "Login" }
        return "Action"
    }
    
    private func extractProjectName(from text: String) -> String {
        // Simple name extraction - in reality this would use NLP
        let words = text.components(separatedBy: .whitespaces)
        if let appIndex = words.firstIndex(of: "app") {
            let nameWords = words[..<appIndex]
            return nameWords.joined(separator: " ").capitalized + " App"
        }
        return "Generated App"
    }
}