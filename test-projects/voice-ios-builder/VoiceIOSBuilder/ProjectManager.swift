import Foundation
import Combine

class ProjectManager: ObservableObject {
    
    // MARK: - Published Properties
    @Published var projects: [Project] = []
    @Published var isBuilding: Bool = false
    
    // MARK: - Private Properties
    private let fileManager = FileManager.default
    private let projectsDirectory: URL
    private var cancellables = Set<AnyCancellable>()
    
    // MARK: - Initialization
    init() {
        // Create projects directory in Documents
        let documentsPath = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first!
        projectsDirectory = documentsPath.appendingPathComponent("VoiceGeneratedProjects")
        
        createProjectsDirectoryIfNeeded()
        loadExistingProjects()
    }
    
    // MARK: - Project Creation
    func createProject(
        name: String,
        description: String,
        generatedCode: String,
        completion: @escaping (Result<Project, ProjectManagerError>) -> Void
    ) {
        let project = Project(
            name: name,
            description: description,
            generatedCode: generatedCode
        )
        
        DispatchQueue.global(qos: .userInitiated).async { [weak self] in
            guard let self = self else { return }
            
            do {
                try self.saveProjectToDisk(project)
                
                DispatchQueue.main.async {
                    self.projects.append(project)
                    completion(.success(project))
                }
            } catch {
                DispatchQueue.main.async {
                    completion(.failure(.fileSystemError(error.localizedDescription)))
                }
            }
        }
    }
    
    // MARK: - Project Management
    func getAllProjects() -> [Project] {
        return projects
    }
    
    func getProject(by id: UUID) -> Project? {
        return projects.first { $0.id == id }
    }
    
    func deleteProject(id: UUID, completion: @escaping (Result<Void, ProjectManagerError>) -> Void) {
        guard let projectIndex = projects.firstIndex(where: { $0.id == id }) else {
            completion(.failure(.projectNotFound))
            return
        }
        
        let project = projects[projectIndex]
        
        DispatchQueue.global(qos: .userInitiated).async { [weak self] in
            guard let self = self else { return }
            
            do {
                try self.deleteProjectFromDisk(project)
                
                DispatchQueue.main.async {
                    self.projects.remove(at: projectIndex)
                    completion(.success(()))
                }
            } catch {
                DispatchQueue.main.async {
                    completion(.failure(.fileSystemError(error.localizedDescription)))
                }
            }
        }
    }
    
    func updateProject(
        id: UUID,
        updatedCode: String,
        completion: @escaping (Result<Project, ProjectManagerError>) -> Void
    ) {
        guard let projectIndex = projects.firstIndex(where: { $0.id == id }) else {
            completion(.failure(.projectNotFound))
            return
        }
        
        var project = projects[projectIndex]
        project.updateCode(updatedCode)
        
        DispatchQueue.global(qos: .userInitiated).async { [weak self] in
            guard let self = self else { return }
            
            do {
                try self.saveProjectToDisk(project)
                
                DispatchQueue.main.async {
                    self.projects[projectIndex] = project
                    completion(.success(project))
                }
            } catch {
                DispatchQueue.main.async {
                    completion(.failure(.fileSystemError(error.localizedDescription)))
                }
            }
        }
    }
    
    // MARK: - Simulator Integration
    func openInSimulator(projectId: UUID, completion: @escaping (Result<Void, ProjectManagerError>) -> Void) {
        guard let project = getProject(by: projectId) else {
            completion(.failure(.projectNotFound))
            return
        }
        
        isBuilding = true
        
        DispatchQueue.global(qos: .userInitiated).async { [weak self] in
            guard let self = self else { return }
            
            // Simulate building and opening in simulator
            do {
                try self.buildProject(project)
                try self.launchInSimulator(project)
                
                DispatchQueue.main.async {
                    self.isBuilding = false
                    completion(.success(()))
                }
            } catch {
                DispatchQueue.main.async {
                    self.isBuilding = false
                    if let projectError = error as? ProjectManagerError {
                        completion(.failure(projectError))
                    } else {
                        completion(.failure(.buildFailed(error.localizedDescription)))
                    }
                }
            }
        }
    }
    
    // MARK: - Private Methods
    private func createProjectsDirectoryIfNeeded() {
        if !fileManager.fileExists(atPath: projectsDirectory.path) {
            try? fileManager.createDirectory(at: projectsDirectory, withIntermediateDirectories: true)
        }
    }
    
    private func loadExistingProjects() {
        do {
            let projectFiles = try fileManager.contentsOfDirectory(at: projectsDirectory, 
                                                                 includingPropertiesForKeys: nil)
            
            for projectFile in projectFiles where projectFile.pathExtension == "json" {
                if let project = loadProjectFromDisk(at: projectFile) {
                    projects.append(project)
                }
            }
        } catch {
            print("Failed to load existing projects: \(error)")
        }
    }
    
    private func saveProjectToDisk(_ project: Project) throws {
        let projectData = try JSONEncoder().encode(ProjectData(from: project))
        let projectFile = projectsDirectory.appendingPathComponent("\(project.id.uuidString).json")
        try projectData.write(to: projectFile)
        
        // Also save the Swift code to a separate file
        let codeFile = projectsDirectory.appendingPathComponent("\(project.id.uuidString).swift")
        try project.generatedCode.write(to: codeFile, atomically: true, encoding: .utf8)
    }
    
    private func loadProjectFromDisk(at url: URL) -> Project? {
        do {
            let data = try Data(contentsOf: url)
            let projectData = try JSONDecoder().decode(ProjectData.self, from: data)
            
            // Load the associated Swift code
            let codeFile = url.deletingPathExtension().appendingPathExtension("swift")
            let code = try String(contentsOf: codeFile)
            
            return Project(
                id: UUID(uuidString: projectData.id) ?? UUID(),
                name: projectData.name,
                description: projectData.description,
                generatedCode: code,
                createdAt: projectData.createdAt,
                updatedAt: projectData.updatedAt
            )
        } catch {
            print("Failed to load project from \(url): \(error)")
            return nil
        }
    }
    
    private func deleteProjectFromDisk(_ project: Project) throws {
        let projectFile = projectsDirectory.appendingPathComponent("\(project.id.uuidString).json")
        let codeFile = projectsDirectory.appendingPathComponent("\(project.id.uuidString).swift")
        
        try fileManager.removeItem(at: projectFile)
        try fileManager.removeItem(at: codeFile)
    }
    
    private func buildProject(_ project: Project) throws {
        // Simulate build process
        Thread.sleep(forTimeInterval: 2.0) // Simulate build time
        
        // In a real implementation, this would:
        // 1. Create a temporary Xcode project
        // 2. Write the generated code to appropriate files
        // 3. Build using xcodebuild
        // 4. Handle any build errors
        
        // For now, we'll just validate the code has basic Swift syntax
        guard project.generatedCode.contains("import SwiftUI") else {
            throw ProjectManagerError.buildFailed("Invalid SwiftUI code")
        }
    }
    
    private func launchInSimulator(_ project: Project) throws {
        // Simulate launching in simulator
        Thread.sleep(forTimeInterval: 1.0)
        
        // In a real implementation, this would:
        // 1. Use simctl to boot a simulator if needed
        // 2. Install the built app
        // 3. Launch the app
        
        // For now, just check if we can simulate launching
        // (In production, this might check if Xcode/Simulator is available)
    }
}

// MARK: - Supporting Data Structure
private struct ProjectData: Codable {
    let id: String
    let name: String
    let description: String
    let createdAt: Date
    let updatedAt: Date
    
    init(from project: Project) {
        self.id = project.id.uuidString
        self.name = project.name
        self.description = project.description
        self.createdAt = project.createdAt
        self.updatedAt = project.updatedAt
    }
}