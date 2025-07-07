import XCTest
@testable import SimulatorModule

final class SimulatorManagerTests: XCTestCase {
    
    var simulatorManager: SimulatorManager!
    
    override func setUp() {
        super.setUp()
        simulatorManager = SimulatorManager()
    }
    
    override func tearDown() {
        simulatorManager = nil
        super.tearDown()
    }
    
    // MARK: - RED Phase: Failing Tests
    
    func testSimulatorManagerInitialization() {
        // Test that SimulatorManager initializes successfully
        XCTAssertNotNil(simulatorManager)
        XCTAssertFalse(simulatorManager.isSimulatorRunning)
    }
    
    func testListAvailableSimulators() async throws {
        // Test that we can list available simulators
        let simulators = try await simulatorManager.listAvailableSimulators()
        
        // Should have at least one simulator available
        XCTAssertFalse(simulators.isEmpty, "Should have at least one iOS simulator available")
        
        // Each simulator should have required properties
        for simulator in simulators {
            XCTAssertFalse(simulator.udid.isEmpty, "Simulator UDID should not be empty")
            XCTAssertFalse(simulator.name.isEmpty, "Simulator name should not be empty")
            XCTAssertFalse(simulator.deviceType.isEmpty, "Simulator device type should not be empty")
        }
    }
    
    func testLaunchSimulator() async throws {
        // Test launching a simulator
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        let success = try await simulatorManager.launchSimulator(udid: firstSimulator.udid)
        XCTAssertTrue(success, "Should successfully launch simulator")
        XCTAssertTrue(simulatorManager.isSimulatorRunning, "Simulator should be running after launch")
        
        // Clean up
        try await simulatorManager.shutdownSimulator(udid: firstSimulator.udid)
    }
    
    func testShutdownSimulator() async throws {
        // Test shutting down a simulator
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        // First launch the simulator
        _ = try await simulatorManager.launchSimulator(udid: firstSimulator.udid)
        
        // Then shutdown
        let success = try await simulatorManager.shutdownSimulator(udid: firstSimulator.udid)
        XCTAssertTrue(success, "Should successfully shutdown simulator")
        XCTAssertFalse(simulatorManager.isSimulatorRunning, "Simulator should not be running after shutdown")
    }
    
    func testGetSimulatorStatus() async throws {
        // Test getting simulator status
        let simulators = try await simulatorManager.listAvailableSimulators()
        guard let firstSimulator = simulators.first else {
            XCTFail("No simulators available for testing")
            return
        }
        
        let status = try await simulatorManager.getSimulatorStatus(udid: firstSimulator.udid)
        XCTAssertTrue(["Shutdown", "Booted", "Booting"].contains(status), "Status should be one of the expected values")
    }
    
    func testInvalidSimulatorUDID() async {
        // Test handling invalid simulator UDID
        do {
            _ = try await simulatorManager.launchSimulator(udid: "invalid-udid")
            XCTFail("Should throw error for invalid UDID")
        } catch SimulatorError.invalidUDID {
            // Expected error
        } catch {
            XCTFail("Should throw SimulatorError.invalidUDID, got: \(error)")
        }
    }
}