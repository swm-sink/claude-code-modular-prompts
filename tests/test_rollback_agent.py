#!/usr/bin/env python3
"""
TDD Tests for Rollback Agent
RED Phase: Write failing tests FIRST
"""

import pytest
import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os
import subprocess
import time
from dataclasses import dataclass

# Add scripts to path
scripts_path = os.path.join(os.path.dirname(__file__), '..', 'scripts')
sys.path.insert(0, scripts_path)

from rollback_agent import (
    RollbackAgent,
    RollbackConfig,
    RollbackStatus,
    RollbackTrigger,
    RollbackState,
    RollbackResult
)

class TestRollbackAgent(unittest.TestCase):
    """TDD Tests for Rollback Agent"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.config = RollbackConfig(
            max_rollback_time=5,
            health_check_threshold=0.95,
            performance_threshold=0.192,
            auto_rollback_enabled=True,
            backup_retention_hours=24,
            notification_endpoints=["http://example.com/webhook"]
        )
        self.agent = RollbackAgent(self.config)
        
    def test_rollback_agent_initialization(self):
        """Test: Rollback agent initializes correctly"""
        self.assertEqual(self.agent.config.max_rollback_time, 5)
        self.assertEqual(self.agent.config.health_check_threshold, 0.95)
        self.assertEqual(self.agent.config.performance_threshold, 0.192)
        self.assertTrue(self.agent.config.auto_rollback_enabled)
        self.assertEqual(self.agent.status, RollbackStatus.READY)
        self.assertIsNotNone(self.agent.rollback_id)
        self.assertEqual(len(self.agent.rollback_log), 0)
        self.assertEqual(len(self.agent.state_snapshots), 0)
        
    def test_rollback_config_defaults(self):
        """Test: Rollback config has proper defaults"""
        config = RollbackConfig()
        
        self.assertEqual(config.max_rollback_time, 5)
        self.assertEqual(config.health_check_threshold, 0.95)
        self.assertEqual(config.performance_threshold, 0.192)
        self.assertTrue(config.auto_rollback_enabled)
        self.assertEqual(config.backup_retention_hours, 24)
        self.assertEqual(config.notification_endpoints, [])
        
    def test_log_event_creates_proper_entry(self):
        """Test: Log event creates proper log entry"""
        self.agent.log_event("test_event", {"key": "value"})
        
        self.assertEqual(len(self.agent.rollback_log), 1)
        log_entry = self.agent.rollback_log[0]
        
        self.assertEqual(log_entry["event"], "test_event")
        self.assertEqual(log_entry["rollback_id"], self.agent.rollback_id)
        self.assertEqual(log_entry["status"], RollbackStatus.READY.value)
        self.assertEqual(log_entry["details"], {"key": "value"})
        self.assertIsInstance(log_entry["timestamp"], float)
        
    @patch('subprocess.run')
    def test_create_state_snapshot_success(self, mock_run):
        """Test: State snapshot creation succeeds"""
        # Mock git command
        mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
        
        deployment_id = "test-deployment-123"
        snapshot = self.agent.create_state_snapshot(deployment_id)
        
        self.assertEqual(snapshot.deployment_id, deployment_id)
        self.assertEqual(snapshot.framework_version, "3.0.0")
        self.assertEqual(snapshot.git_commit, "abc123def456")
        self.assertIsInstance(snapshot.timestamp, float)
        self.assertIsInstance(snapshot.config_snapshot, dict)
        self.assertIsInstance(snapshot.performance_baseline, dict)
        self.assertIsInstance(snapshot.health_metrics, dict)
        self.assertIsInstance(snapshot.file_checksums, dict)
        
        # Verify snapshot is stored
        self.assertIn(deployment_id, self.agent.state_snapshots)
        self.assertEqual(self.agent.state_snapshots[deployment_id], snapshot)
        
    @patch('subprocess.run')
    def test_create_state_snapshot_git_failure(self, mock_run):
        """Test: State snapshot creation handles git failure"""
        # Mock git command failure
        mock_run.side_effect = subprocess.CalledProcessError(1, 'git')
        
        deployment_id = "test-deployment-123"
        snapshot = self.agent.create_state_snapshot(deployment_id)
        
        # Should still create snapshot with "unknown" git commit
        self.assertEqual(snapshot.git_commit, "unknown")
        
    def test_detect_rollback_trigger_none(self):
        """Test: No rollback trigger detected with healthy metrics"""
        current_metrics = {
            "health_status": "healthy",
            "performance_score": 0.25,
            "error_rate": 0.001
        }
        
        with patch.object(self.agent, '_check_health_metrics', return_value=True):
            with patch.object(self.agent, '_check_performance_metrics', return_value=True):
                with patch.object(self.agent, '_check_validation_status', return_value=True):
                    trigger = self.agent.detect_rollback_trigger(current_metrics)
                    
        self.assertIsNone(trigger)
        
    def test_detect_rollback_trigger_health_failure(self):
        """Test: Health check failure trigger detected"""
        current_metrics = {
            "health_status": "degraded",
            "performance_score": 0.25,
            "error_rate": 0.001
        }
        
        with patch.object(self.agent, '_check_health_metrics', return_value=False):
            trigger = self.agent.detect_rollback_trigger(current_metrics)
            
        self.assertEqual(trigger, RollbackTrigger.HEALTH_CHECK_FAILURE)
        
    def test_detect_rollback_trigger_performance_degradation(self):
        """Test: Performance degradation trigger detected"""
        current_metrics = {
            "health_status": "healthy",
            "performance_score": 0.10,
            "error_rate": 0.001
        }
        
        with patch.object(self.agent, '_check_health_metrics', return_value=True):
            with patch.object(self.agent, '_check_performance_metrics', return_value=False):
                trigger = self.agent.detect_rollback_trigger(current_metrics)
                
        self.assertEqual(trigger, RollbackTrigger.PERFORMANCE_DEGRADATION)
        
    def test_detect_rollback_trigger_validation_failure(self):
        """Test: Validation failure trigger detected"""
        current_metrics = {
            "health_status": "healthy",
            "performance_score": 0.25,
            "validation_status": "failed"
        }
        
        with patch.object(self.agent, '_check_health_metrics', return_value=True):
            with patch.object(self.agent, '_check_performance_metrics', return_value=True):
                with patch.object(self.agent, '_check_validation_status', return_value=False):
                    trigger = self.agent.detect_rollback_trigger(current_metrics)
                    
        self.assertEqual(trigger, RollbackTrigger.VALIDATION_FAILURE)
        
    def test_execute_rollback_success(self):
        """Test: Rollback execution succeeds"""
        deployment_id = "test-deployment-123"
        
        # Create a state snapshot first
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
            self.agent.create_state_snapshot(deployment_id)
            
        # Mock all rollback phases
        with patch.object(self.agent, '_stop_current_deployment', return_value=True):
            with patch.object(self.agent, '_restore_git_state', return_value=True):
                with patch.object(self.agent, '_restore_configuration', return_value=True):
                    with patch.object(self.agent, '_restart_services', return_value=True):
                        with patch.object(self.agent, '_validate_restoration', return_value=True):
                            result = self.agent.execute_rollback(deployment_id, RollbackTrigger.MANUAL_TRIGGER)
                            
        self.assertEqual(result.status, RollbackStatus.COMPLETED)
        self.assertEqual(result.trigger, RollbackTrigger.MANUAL_TRIGGER)
        self.assertEqual(result.previous_deployment_id, deployment_id)
        self.assertIsNotNone(result.restored_state)
        self.assertIsNone(result.error_message)
        self.assertLessEqual(result.duration, self.config.max_rollback_time)
        
    def test_execute_rollback_no_snapshot(self):
        """Test: Rollback execution fails without snapshot"""
        deployment_id = "nonexistent-deployment"
        
        result = self.agent.execute_rollback(deployment_id, RollbackTrigger.MANUAL_TRIGGER)
        
        self.assertEqual(result.status, RollbackStatus.FAILED)
        self.assertIsNone(result.restored_state)
        self.assertIsNotNone(result.error_message)
        self.assertIn("No state snapshot found", result.error_message)
        
    def test_execute_rollback_stop_deployment_failure(self):
        """Test: Rollback execution fails during stop deployment"""
        deployment_id = "test-deployment-123"
        
        # Create a state snapshot first
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
            self.agent.create_state_snapshot(deployment_id)
            
        # Mock stop deployment failure
        with patch.object(self.agent, '_stop_current_deployment', return_value=False):
            result = self.agent.execute_rollback(deployment_id, RollbackTrigger.MANUAL_TRIGGER)
            
        self.assertEqual(result.status, RollbackStatus.FAILED)
        self.assertIsNone(result.restored_state)
        self.assertIsNotNone(result.error_message)
        self.assertIn("Failed to stop current deployment", result.error_message)
        
    def test_execute_rollback_git_restore_failure(self):
        """Test: Rollback execution fails during git restore"""
        deployment_id = "test-deployment-123"
        
        # Create a state snapshot first
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
            self.agent.create_state_snapshot(deployment_id)
            
        # Mock git restore failure
        with patch.object(self.agent, '_stop_current_deployment', return_value=True):
            with patch.object(self.agent, '_restore_git_state', return_value=False):
                result = self.agent.execute_rollback(deployment_id, RollbackTrigger.MANUAL_TRIGGER)
                
        self.assertEqual(result.status, RollbackStatus.FAILED)
        self.assertIsNone(result.restored_state)
        self.assertIsNotNone(result.error_message)
        self.assertIn("Failed to restore git state", result.error_message)
        
    def test_execute_rollback_configuration_restore_failure(self):
        """Test: Rollback execution fails during configuration restore"""
        deployment_id = "test-deployment-123"
        
        # Create a state snapshot first
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
            self.agent.create_state_snapshot(deployment_id)
            
        # Mock configuration restore failure
        with patch.object(self.agent, '_stop_current_deployment', return_value=True):
            with patch.object(self.agent, '_restore_git_state', return_value=True):
                with patch.object(self.agent, '_restore_configuration', return_value=False):
                    result = self.agent.execute_rollback(deployment_id, RollbackTrigger.MANUAL_TRIGGER)
                    
        self.assertEqual(result.status, RollbackStatus.FAILED)
        self.assertIsNone(result.restored_state)
        self.assertIsNotNone(result.error_message)
        self.assertIn("Failed to restore configuration", result.error_message)
        
    def test_execute_rollback_service_restart_failure(self):
        """Test: Rollback execution fails during service restart"""
        deployment_id = "test-deployment-123"
        
        # Create a state snapshot first
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
            self.agent.create_state_snapshot(deployment_id)
            
        # Mock service restart failure
        with patch.object(self.agent, '_stop_current_deployment', return_value=True):
            with patch.object(self.agent, '_restore_git_state', return_value=True):
                with patch.object(self.agent, '_restore_configuration', return_value=True):
                    with patch.object(self.agent, '_restart_services', return_value=False):
                        result = self.agent.execute_rollback(deployment_id, RollbackTrigger.MANUAL_TRIGGER)
                        
        self.assertEqual(result.status, RollbackStatus.FAILED)
        self.assertIsNone(result.restored_state)
        self.assertIsNotNone(result.error_message)
        self.assertIn("Failed to restart services", result.error_message)
        
    def test_execute_rollback_validation_failure(self):
        """Test: Rollback execution fails during validation"""
        deployment_id = "test-deployment-123"
        
        # Create a state snapshot first
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
            self.agent.create_state_snapshot(deployment_id)
            
        # Mock validation failure
        with patch.object(self.agent, '_stop_current_deployment', return_value=True):
            with patch.object(self.agent, '_restore_git_state', return_value=True):
                with patch.object(self.agent, '_restore_configuration', return_value=True):
                    with patch.object(self.agent, '_restart_services', return_value=True):
                        with patch.object(self.agent, '_validate_restoration', return_value=False):
                            result = self.agent.execute_rollback(deployment_id, RollbackTrigger.MANUAL_TRIGGER)
                            
        self.assertEqual(result.status, RollbackStatus.FAILED)
        self.assertIsNone(result.restored_state)
        self.assertIsNotNone(result.error_message)
        self.assertIn("Failed to validate restoration", result.error_message)
        
    def test_rollback_time_constraint(self):
        """Test: Rollback time constraint is monitored"""
        deployment_id = "test-deployment-123"
        
        # Create a state snapshot first
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
            self.agent.create_state_snapshot(deployment_id)
            
        # Mock slow rollback phases
        def slow_operation():
            time.sleep(0.1)  # Simulate slow operation
            return True
            
        with patch.object(self.agent, '_stop_current_deployment', side_effect=slow_operation):
            with patch.object(self.agent, '_restore_git_state', side_effect=slow_operation):
                with patch.object(self.agent, '_restore_configuration', side_effect=slow_operation):
                    with patch.object(self.agent, '_restart_services', side_effect=slow_operation):
                        with patch.object(self.agent, '_validate_restoration', side_effect=slow_operation):
                            result = self.agent.execute_rollback(deployment_id, RollbackTrigger.MANUAL_TRIGGER)
                            
        self.assertEqual(result.status, RollbackStatus.COMPLETED)
        self.assertGreater(result.duration, 0.4)  # Should take at least 0.4 seconds
        
    @patch('subprocess.run')
    def test_restore_git_state_success(self, mock_run):
        """Test: Git state restoration succeeds"""
        mock_run.return_value = Mock(returncode=0)
        
        result = self.agent._restore_git_state("abc123def456")
        
        self.assertTrue(result)
        mock_run.assert_called_once_with(
            ["git", "checkout", "abc123def456"],
            check=True, capture_output=True
        )
        
    @patch('subprocess.run')
    def test_restore_git_state_failure(self, mock_run):
        """Test: Git state restoration fails"""
        mock_run.side_effect = subprocess.CalledProcessError(1, 'git')
        
        result = self.agent._restore_git_state("abc123def456")
        
        self.assertFalse(result)
        
    def test_get_rollback_status_structure(self):
        """Test: Rollback status has correct structure"""
        status = self.agent.get_rollback_status()
        
        self.assertIn("rollback_id", status)
        self.assertIn("status", status)
        self.assertIn("timestamp", status)
        self.assertIn("snapshots", status)
        self.assertIn("log", status)
        
        self.assertEqual(status["rollback_id"], self.agent.rollback_id)
        self.assertEqual(status["status"], RollbackStatus.READY.value)
        self.assertEqual(status["snapshots"], 0)
        self.assertIsInstance(status["timestamp"], float)
        self.assertIsInstance(status["log"], list)
        
    def test_trigger_manual_rollback(self):
        """Test: Manual rollback trigger works"""
        deployment_id = "test-deployment-123"
        
        # Create a state snapshot first
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
            self.agent.create_state_snapshot(deployment_id)
            
        # Mock rollback execution
        with patch.object(self.agent, 'execute_rollback') as mock_execute:
            mock_result = Mock()
            mock_execute.return_value = mock_result
            
            result = self.agent.trigger_manual_rollback(deployment_id)
            
        mock_execute.assert_called_once_with(deployment_id, RollbackTrigger.MANUAL_TRIGGER)
        self.assertEqual(result, mock_result)
        
    def test_rollback_state_structure(self):
        """Test: Rollback state has correct structure"""
        state = RollbackState(
            deployment_id="test-123",
            timestamp=time.time(),
            framework_version="3.0.0",
            config_snapshot={"key": "value"},
            performance_baseline={"response_time": 0.089},
            health_metrics={"status": "healthy"},
            git_commit="abc123def456",
            file_checksums={"file1.py": "hash123"}
        )
        
        self.assertEqual(state.deployment_id, "test-123")
        self.assertEqual(state.framework_version, "3.0.0")
        self.assertEqual(state.git_commit, "abc123def456")
        self.assertIsInstance(state.timestamp, float)
        self.assertIsInstance(state.config_snapshot, dict)
        self.assertIsInstance(state.performance_baseline, dict)
        self.assertIsInstance(state.health_metrics, dict)
        self.assertIsInstance(state.file_checksums, dict)
        
    def test_rollback_result_structure(self):
        """Test: Rollback result has correct structure"""
        result = RollbackResult(
            rollback_id="rollback-123",
            status=RollbackStatus.COMPLETED,
            trigger=RollbackTrigger.MANUAL_TRIGGER,
            timestamp=time.time(),
            duration=2.5,
            previous_deployment_id="deployment-456",
            restored_state=None,
            error_message=None
        )
        
        self.assertEqual(result.rollback_id, "rollback-123")
        self.assertEqual(result.status, RollbackStatus.COMPLETED)
        self.assertEqual(result.trigger, RollbackTrigger.MANUAL_TRIGGER)
        self.assertEqual(result.duration, 2.5)
        self.assertEqual(result.previous_deployment_id, "deployment-456")
        self.assertIsNone(result.restored_state)
        self.assertIsNone(result.error_message)

class TestRollbackIntegration(unittest.TestCase):
    """Integration tests for rollback flow"""
    
    def setUp(self):
        """Set up integration test fixtures"""
        self.config = RollbackConfig(
            max_rollback_time=5,
            auto_rollback_enabled=True
        )
        
    def test_end_to_end_rollback_flow(self):
        """Test: Complete end-to-end rollback flow"""
        agent = RollbackAgent(self.config)
        deployment_id = "test-deployment-123"
        
        # Create snapshot
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
            snapshot = agent.create_state_snapshot(deployment_id)
            
        # Execute rollback
        with patch.object(agent, '_stop_current_deployment', return_value=True):
            with patch.object(agent, '_restore_git_state', return_value=True):
                with patch.object(agent, '_restore_configuration', return_value=True):
                    with patch.object(agent, '_restart_services', return_value=True):
                        with patch.object(agent, '_validate_restoration', return_value=True):
                            result = agent.execute_rollback(deployment_id, RollbackTrigger.HEALTH_CHECK_FAILURE)
                            
        self.assertEqual(result.status, RollbackStatus.COMPLETED)
        self.assertEqual(result.trigger, RollbackTrigger.HEALTH_CHECK_FAILURE)
        self.assertLessEqual(result.duration, 5.0)
        self.assertEqual(result.restored_state, snapshot)
        
    def test_auto_rollback_detection_flow(self):
        """Test: Auto rollback detection and execution flow"""
        agent = RollbackAgent(self.config)
        deployment_id = "test-deployment-123"
        
        # Create snapshot
        with patch('subprocess.run') as mock_run:
            mock_run.return_value = Mock(returncode=0, stdout="abc123def456")
            agent.create_state_snapshot(deployment_id)
            
        # Simulate degraded metrics
        degraded_metrics = {
            "health_status": "degraded",
            "performance_score": 0.10,
            "error_rate": 0.10
        }
        
        # Detect trigger
        with patch.object(agent, '_check_health_metrics', return_value=False):
            trigger = agent.detect_rollback_trigger(degraded_metrics)
            
        self.assertEqual(trigger, RollbackTrigger.HEALTH_CHECK_FAILURE)
        
        # Execute rollback
        if trigger and agent.config.auto_rollback_enabled:
            with patch.object(agent, '_stop_current_deployment', return_value=True):
                with patch.object(agent, '_restore_git_state', return_value=True):
                    with patch.object(agent, '_restore_configuration', return_value=True):
                        with patch.object(agent, '_restart_services', return_value=True):
                            with patch.object(agent, '_validate_restoration', return_value=True):
                                result = agent.execute_rollback(deployment_id, trigger)
                                
        self.assertEqual(result.status, RollbackStatus.COMPLETED)

if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)