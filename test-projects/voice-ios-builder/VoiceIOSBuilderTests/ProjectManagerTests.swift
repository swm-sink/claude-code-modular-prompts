import XCTest
@testable import VoiceIOSBuilder

final class ProjectManagerTests: XCTestCase {
    
    var projectManager: ProjectManager!
    
    override func setUpWithError() throws {
        super.setUp()
        projectManager = ProjectManager()
    }
    
    override func tearDownWithError() throws {
        projectManager = nil
        super.tearDown()
    }
    
    // MARK: - Project Creation Tests
    
    func testProjectManagerCanCreateNewProject() throws {
        // RED: This will fail - no ProjectManager implementation yet
        let projectName = "TestCalculatorApp"
        let projectDescription = "A simple calculator app with basic arithmetic operations"
        
        let expectation = XCTestExpectation(description: "Project should be created")
        
        projectManager.createProject(
            name: projectName,
            description: projectDescription,
            generatedCode: "// Test code"
        ) { result in
            switch result {
            case .success(let project):
                XCTAssertEqual(project.name, projectName, "Project name should match")
                XCTAssertEqual(project.description, projectDescription, "Project description should match")
                XCTAssertNotNil(project.id, "Project should have an ID")
                expectation.fulfill()
            case .failure(let error):
                XCTFail("Project creation failed: \(error)")
            }
        }
        
        wait(for: [expectation], timeout: 5.0)
    }
    
    func testProjectManagerCanListProjects() throws {
        // RED: This will fail - no project listing yet
        let projects = projectManager.getAllProjects()
        XCTAssertNotNil(projects, "Projects list should not be nil")
        XCTAssertTrue(projects.isEmpty, "Projects list should be empty initially")
    }
    
    func testProjectManagerCanDeleteProject() throws {
        // RED: This will fail - no project deletion yet
        let projectId = UUID()
        let expectation = XCTestExpectation(description: "Project should be deleted")
        
        projectManager.deleteProject(id: projectId) { result in
            switch result {
            case .success:
                expectation.fulfill()
            case .failure(let error):
                // For now, we expect this to fail since project doesn't exist
                XCTAssertTrue(error is ProjectManagerError, "Should throw ProjectManagerError")
                expectation.fulfill()
            }
        }
        
        wait(for: [expectation], timeout: 2.0)
    }
    
    func testProjectManagerCanOpenProjectInSimulator() throws {
        // RED: This will fail - no simulator integration yet
        let projectId = UUID()
        let expectation = XCTestExpectation(description: "Project should open in simulator")
        
        projectManager.openInSimulator(projectId: projectId) { result in
            switch result {
            case .success:
                expectation.fulfill()
            case .failure(let error):
                XCTAssertTrue(error is ProjectManagerError, "Should throw ProjectManagerError")
                expectation.fulfill()
            }
        }
        
        wait(for: [expectation], timeout: 5.0)
    }
    
    func testProjectManagerCanUpdateProject() throws {
        // RED: This will fail - no project update functionality yet
        let projectId = UUID()
        let updatedCode = "// Updated test code"
        let expectation = XCTestExpectation(description: "Project should be updated")
        
        projectManager.updateProject(
            id: projectId,
            updatedCode: updatedCode
        ) { result in
            switch result {
            case .success:
                expectation.fulfill()
            case .failure(let error):
                XCTAssertTrue(error is ProjectManagerError, "Should throw ProjectManagerError")
                expectation.fulfill()
            }
        }
        
        wait(for: [expectation], timeout: 3.0)
    }
}