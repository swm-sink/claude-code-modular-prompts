import Foundation
import Combine

#if canImport(AVFoundation)
import AVFoundation
#endif

#if canImport(Speech)
import Speech
#endif

@MainActor
class AppCoordinator: ObservableObject {
    
    // MARK: - Published Properties
    @Published var currentState: AppState = .idle
    @Published var currentProject: Project?
    @Published var recentProjects: [Project] = []
    @Published var feedbackMessage: String = ""
    @Published var isProcessing: Bool = false
    
    // MARK: - Private Properties
    private let projectManager: ProjectManager
    private var cancellables = Set<AnyCancellable>()
    
    #if canImport(AVFoundation) && !os(macOS)
    private var audioEngine: AVAudioEngine?
    #endif
    
    #if canImport(Speech)
    private var recognitionTask: SFSpeechRecognitionTask?
    #endif
    
    // MARK: - Initialization
    init(projectManager: ProjectManager = ProjectManager()) {
        self.projectManager = projectManager
        setupAudioSession()
    }
    
    // MARK: - Voice Recording
    func startVoiceRecording(completion: @escaping (Bool) -> Void) {
        guard currentState == .idle else {
            completion(false)
            return
        }
        
        #if canImport(AVFoundation) && !os(macOS)
        // Check microphone permissions on iOS
        AVAudioSession.sharedInstance().requestRecordPermission { [weak self] granted in
            DispatchQueue.main.async {
                guard let self = self else { return }
                
                if granted {
                    self.currentState = .recording
                    self.feedbackMessage = "Listening..."
                    self.isProcessing = true
                    
                    // Start actual recording (placeholder for now)
                    self.simulateVoiceRecording()
                    completion(true)
                } else {
                    self.currentState = .error("Microphone permission denied")
                    completion(false)
                }
            }
        }
        #else
        // For macOS and other platforms, simulate permission granted
        DispatchQueue.main.async { [weak self] in
            guard let self = self else { return }
            
            self.currentState = .recording
            self.feedbackMessage = "Listening..."
            self.isProcessing = true
            
            // Start simulated recording
            self.simulateVoiceRecording()
            completion(true)
        }
        #endif
    }
    
    func stopVoiceRecording() {
        currentState = .processing
        feedbackMessage = "Processing your request..."
        
        // Stop recording and process (placeholder)
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.0) {
            self.isProcessing = false
            self.currentState = .idle
            self.feedbackMessage = ""
        }
    }
    
    // MARK: - Voice Processing
    func processVoiceInput(_ input: String, completion: @escaping (Result<String, VoiceProcessingError>) -> Void) {
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
    func triggerCodeGeneration(for request: VoiceRequest, completion: @escaping (Result<String, CodeGenerationError>) -> Void) {
        currentState = .generating
        feedbackMessage = "Generating your app..."
        
        // Simulate code generation
        DispatchQueue.global(qos: .userInitiated).asyncAfter(deadline: .now() + 2.0) {
            let generatedCode = AppCoordinator.generateCodeForRequest(request)
            
            DispatchQueue.main.async {
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
    
    private static func generateCodeForRequest(_ request: VoiceRequest) -> String {
        // Placeholder code generation
        switch request.intent {
        case .createApp:
            return """
            import SwiftUI
            
            struct ContentView: View {
                var body: some View {
                    VStack {
                        Text("Generated App")
                            .font(.largeTitle)
                            .padding()
                        
                        Text("\(request.processedText)")
                            .multilineTextAlignment(.center)
                            .padding()
                    }
                }
            }
            
            struct ContentView_Previews: PreviewProvider {
                static var previews: some View {
                    ContentView()
                }
            }
            """
        default:
            return "// Generated code placeholder"
        }
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