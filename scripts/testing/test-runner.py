#!/usr/bin/env python3
"""
Simple test runner to verify TDD cycle implementation
"""

import sys
import os
import importlib.util
import traceback

def load_module(module_name, file_path):
    """Load a module from file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_production_deployment():
    """Test production deployment agent"""
    print("Testing Production Deployment Agent...")
    
    try:
        # Load the module
        module = load_module("production_deployment", "scripts/production-deployment.py")
        
        # Test basic imports
        config = module.DeploymentConfig(
            source_branch="main",
            target_environment="production"
        )
        
        agent = module.ProductionDeploymentAgent(config)
        
        # Test basic functionality
        assert agent.config.source_branch == "main"
        assert agent.status == module.DeploymentStatus.PENDING
        
        # Test logging
        agent.log_event("test_event")
        assert len(agent.deployment_log) == 1
        
        print("✓ Production Deployment Agent basic tests passed")
        
    except Exception as e:
        print(f"✗ Production Deployment Agent tests failed: {e}")
        traceback.print_exc()
        return False
        
    return True

def test_rollback_agent():
    """Test rollback agent"""
    print("Testing Rollback Agent...")
    
    try:
        # Load the module
        module = load_module("rollback_agent", "scripts/rollback-agent.py")
        
        # Test basic imports
        config = module.RollbackConfig(
            max_rollback_time=5,
            auto_rollback_enabled=True
        )
        
        agent = module.RollbackAgent(config)
        
        # Test basic functionality
        assert agent.config.max_rollback_time == 5
        assert agent.status == module.RollbackStatus.READY
        
        # Test logging
        agent.log_event("test_event")
        assert len(agent.rollback_log) == 1
        
        print("✓ Rollback Agent basic tests passed")
        
    except Exception as e:
        print(f"✗ Rollback Agent tests failed: {e}")
        traceback.print_exc()
        return False
        
    return True

def test_monitoring_agent():
    """Test monitoring agent"""
    print("Testing Monitoring Agent...")
    
    try:
        # Load the module
        module = load_module("monitoring_agent", "scripts/monitoring-agent.py")
        
        # Test basic imports
        config = module.MonitoringConfig(
            health_check_interval=10,
            performance_improvement_target=0.192
        )
        
        agent = module.MonitoringAgent(config)
        
        # Test basic functionality
        assert agent.config.health_check_interval == 10
        assert agent.status == module.MonitoringStatus.INITIALIZING
        
        # Test logging
        agent.log_event("test_event")
        assert len(agent.monitoring_log) == 1
        
        print("✓ Monitoring Agent basic tests passed")
        
    except Exception as e:
        print(f"✗ Monitoring Agent tests failed: {e}")
        traceback.print_exc()
        return False
        
    return True

def test_validation_agent():
    """Test validation agent"""
    print("Testing Validation Agent...")
    
    try:
        # Load the module
        module = load_module("validation_agent", "scripts/validation-agent.py")
        
        # Test basic imports
        config = module.ValidationConfig(
            coverage_threshold=0.90,
            performance_threshold=0.192
        )
        
        agent = module.ValidationAgent(config)
        
        # Test basic functionality
        assert agent.config.coverage_threshold == 0.90
        assert agent.config.performance_threshold == 0.192
        
        # Test logging
        agent.log_event("test_event")
        assert len(agent.validation_log) == 1
        
        print("✓ Validation Agent basic tests passed")
        
    except Exception as e:
        print(f"✗ Validation Agent tests failed: {e}")
        traceback.print_exc()
        return False
        
    return True

def main():
    """Main test runner"""
    print("Running TDD Cycle Verification Tests...")
    print("=" * 50)
    
    tests = [
        test_production_deployment,
        test_rollback_agent,
        test_monitoring_agent,
        test_validation_agent
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
        
    print("=" * 50)
    print(f"Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("✓ All TDD cycle tests passed - GREEN phase achieved!")
        return 0
    else:
        print("✗ Some tests failed - Still in RED phase")
        return 1

if __name__ == "__main__":
    sys.exit(main())