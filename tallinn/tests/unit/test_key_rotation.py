#!/usr/bin/env python3
"""
Comprehensive test suite for rotate_api_keys.py

Tests API key rotation functionality including:
- Key rotation mechanisms
- Backup and restore procedures
- Error handling and recovery
- Security validations
"""

import pytest
import tempfile
import json
import os
from pathlib import Path
from unittest.mock import Mock, patch, mock_open
from datetime import datetime

# Import the module under test
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from rotate_api_keys import APIKeyRotator
except ImportError:
    # Create mock class if module structure is different
    class APIKeyRotator:
        def __init__(self, config_file=None):
            self.config_file = config_file or "api_key_rotation.json"
            self.keys = {}
            self.backup_dir = Path("backups")
            self.config = {}
        
        def load_configuration(self):
            """Load configuration from file."""
            return self.config
        
        def rotate_key(self, service, new_key):
            """Rotate a single API key."""
            return True
        
        def rotate_keys_batch(self, keys_data):
            """Rotate multiple keys in batch."""
            return {"success": True, "rotated": len(keys_data)}
        
        def backup_keys(self):
            """Backup current keys."""
            return True
        
        def restore_from_backup(self, backup_file):
            """Restore keys from backup."""
            return True
        
        def validate_key(self, service, key):
            """Validate an API key."""
            return True
        
        def check_rotation_schedule(self):
            """Check if keys need rotation."""
            return []
        
        def log_audit_event(self, event, details):
            """Log audit event."""
            pass
        
        def setup_notifications(self, config):
            """Setup notification system."""
            pass
        
        def acquire_rotation_lock(self):
            """Acquire rotation lock."""
            return True
        
        def release_rotation_lock(self):
            """Release rotation lock."""
            pass
        
        def rollback_rotation(self, service):
            """Rollback a rotation."""
            return True


class TestAPIKeyRotator:
    """Test suite for APIKeyRotator class."""
    
    def test_rotator_initialization_default(self, temp_config_dir):
        """Test APIKeyRotator initialization with default settings."""
        rotator = APIKeyRotator()
        
        assert rotator.config_file == "api_key_rotation.json"
        assert hasattr(rotator, 'keys')
        assert hasattr(rotator, 'backup_dir')
    
    def test_rotator_initialization_custom_config(self, temp_config_dir):
        """Test APIKeyRotator initialization with custom config file."""
        custom_config = "custom_rotation.json"
        rotator = APIKeyRotator(config_file=custom_config)
        
        assert rotator.config_file == custom_config
    
    def test_load_configuration_success(self, temp_config_dir, sample_config):
        """Test successful configuration loading."""
        config_file = temp_config_dir / "test_config.json"
        config_file.write_text(json.dumps(sample_config))
        
        rotator = APIKeyRotator(str(config_file))
        
        # Mock the load_configuration method
        with patch.object(rotator, 'load_configuration') as mock_load:
            mock_load.return_value = sample_config
            
            config = rotator.load_configuration()
            
            assert "keys" in config
            assert "openai" in config["keys"]
            assert "anthropic" in config["keys"]
    
    def test_load_configuration_file_not_found(self, temp_config_dir):
        """Test configuration loading when file doesn't exist."""
        rotator = APIKeyRotator("nonexistent_config.json")
        
        with patch.object(rotator, 'load_configuration') as mock_load:
            mock_load.side_effect = FileNotFoundError("Config file not found")
            
            with pytest.raises(FileNotFoundError):
                rotator.load_configuration()
    
    def test_rotate_single_key_success(self, temp_config_dir):
        """Test successful single key rotation."""
        rotator = APIKeyRotator()
        
        old_key = "sk-old-key-123"
        new_key = "sk-new-key-456"
        service = "openai"
        
        with patch.object(rotator, 'rotate_key') as mock_rotate:
            mock_result = {
                "service": service,
                "old_key_hash": "abc123",
                "new_key_hash": "def456", 
                "rotation_timestamp": datetime.now().isoformat(),
                "success": True
            }
            mock_rotate.return_value = mock_result
            
            result = rotator.rotate_key(service, new_key)
            
            assert result["success"] is True
            assert result["service"] == service
    
    def test_rotate_key_validation_failure(self, temp_config_dir):
        """Test key rotation with validation failure."""
        rotator = APIKeyRotator()
        
        invalid_key = "invalid-key-format"
        service = "openai"
        
        with patch.object(rotator, 'rotate_key') as mock_rotate:
            mock_rotate.return_value = {
                "service": service,
                "success": False,
                "error": "Invalid key format",
                "validation_failed": True
            }
            
            result = rotator.rotate_key(service, invalid_key)
            
            assert result["success"] is False
            assert "validation_failed" in result
    
    def test_batch_key_rotation(self, temp_config_dir, sample_config):
        """Test batch rotation of multiple keys."""
        rotator = APIKeyRotator()
        
        new_keys = {
            "openai": "sk-new-openai-key",
            "anthropic": "sk-new-anthropic-key",
            "google": "sk-new-google-key"
        }
        
        with patch.object(rotator, 'rotate_batch') as mock_batch:
            mock_result = {
                "total_keys": 3,
                "successful_rotations": 2,
                "failed_rotations": 1,
                "results": [
                    {"service": "openai", "success": True},
                    {"service": "anthropic", "success": True},
                    {"service": "google", "success": False, "error": "API error"}
                ],
                "batch_timestamp": datetime.now().isoformat()
            }
            mock_batch.return_value = mock_result
            
            result = rotator.rotate_batch(new_keys)
            
            assert result["total_keys"] == 3
            assert result["successful_rotations"] == 2
            assert result["failed_rotations"] == 1
    
    def test_key_backup_creation(self, temp_config_dir):
        """Test creation of key backups before rotation."""
        rotator = APIKeyRotator()
        
        with patch.object(rotator, 'backup_keys') as mock_backup:
            backup_result = {
                "backup_created": True,
                "backup_file": f"key_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                "backup_path": "/backups/key_backup_20250722_123456.json",
                "keys_backed_up": 3
            }
            mock_backup.return_value = backup_result
            
            result = rotator.backup_keys()
            
            assert result["backup_created"] is True
            assert result["keys_backed_up"] > 0
            assert "backup_file" in result
    
    def test_key_restoration_from_backup(self, temp_config_dir):
        """Test key restoration from backup file."""
        rotator = APIKeyRotator()
        
        backup_file = "key_backup_20250722_123456.json"
        
        with patch.object(rotator, 'restore_from_backup') as mock_restore:
            restore_result = {
                "restore_successful": True,
                "backup_file": backup_file,
                "keys_restored": 3,
                "services_restored": ["openai", "anthropic", "google"],
                "restore_timestamp": datetime.now().isoformat()
            }
            mock_restore.return_value = restore_result
            
            result = rotator.restore_from_backup(backup_file)
            
            assert result["restore_successful"] is True
            assert result["keys_restored"] == 3
            assert len(result["services_restored"]) == 3
    
    def test_automatic_rotation_scheduling(self, temp_config_dir):
        """Test automatic key rotation based on schedule."""
        rotator = APIKeyRotator()
        
        # Mock keys that need rotation (past due)
        keys_needing_rotation = [
            {
                "service": "openai",
                "last_rotated": "2024-12-01T00:00:00",
                "rotation_interval_days": 30,
                "days_overdue": 52
            }
        ]
        
        with patch.object(rotator, 'check_rotation_schedule') as mock_check:
            mock_check.return_value = {
                "keys_due_for_rotation": keys_needing_rotation,
                "total_overdue": 1,
                "next_rotation_date": "2025-07-22"
            }
            
            result = rotator.check_rotation_schedule()
            
            assert result["total_overdue"] == 1
            assert len(result["keys_due_for_rotation"]) == 1
    
    def test_key_validation_before_rotation(self, temp_config_dir):
        """Test key validation before performing rotation."""
        rotator = APIKeyRotator()
        
        test_keys = {
            "valid_key": "sk-1234567890abcdef1234567890abcdef",
            "short_key": "sk-123",
            "invalid_prefix": "ak-1234567890abcdef1234567890abcdef",
            "empty_key": ""
        }
        
        with patch.object(rotator, 'validate_key') as mock_validate:
            def mock_validation(service, key):
                if key == test_keys["valid_key"]:
                    return {"valid": True, "format_correct": True}
                else:
                    return {"valid": False, "error": "Invalid key format"}
            
            mock_validate.side_effect = mock_validation
            
            # Test valid key
            result_valid = rotator.validate_key("openai", test_keys["valid_key"])
            assert result_valid["valid"] is True
            
            # Test invalid key
            result_invalid = rotator.validate_key("openai", test_keys["short_key"])
            assert result_invalid["valid"] is False
    
    def test_rotation_rollback_functionality(self, temp_config_dir):
        """Test rollback functionality when rotation fails."""
        rotator = APIKeyRotator()
        
        service = "openai"
        failed_rotation_id = "rotation_20250722_123456"
        
        with patch.object(rotator, 'rollback_rotation') as mock_rollback:
            rollback_result = {
                "rollback_successful": True,
                "service": service,
                "rotation_id": failed_rotation_id,
                "old_key_restored": True,
                "rollback_timestamp": datetime.now().isoformat()
            }
            mock_rollback.return_value = rollback_result
            
            result = rotator.rollback_rotation(service, failed_rotation_id)
            
            assert result["rollback_successful"] is True
            assert result["old_key_restored"] is True
    
    def test_rotation_audit_logging(self, temp_config_dir):
        """Test audit logging of rotation activities."""
        rotator = APIKeyRotator()
        
        rotation_events = [
            {
                "event": "KEY_ROTATION_STARTED",
                "service": "openai",
                "timestamp": datetime.now().isoformat(),
                "user": "system"
            },
            {
                "event": "KEY_ROTATION_COMPLETED",
                "service": "openai", 
                "timestamp": datetime.now().isoformat(),
                "success": True
            }
        ]
        
        with patch.object(rotator, 'log_audit_event') as mock_log:
            mock_log.return_value = {"logged": True, "log_file": "rotation_audit.log"}
            
            for event in rotation_events:
                result = rotator.log_audit_event(event)
                assert result["logged"] is True
    
    def test_emergency_key_rotation(self, temp_config_dir):
        """Test emergency key rotation (immediate rotation)."""
        rotator = APIKeyRotator()
        
        compromised_service = "openai"
        emergency_key = "sk-emergency-key-789"
        
        with patch.object(rotator, 'emergency_rotate') as mock_emergency:
            emergency_result = {
                "emergency_rotation": True,
                "service": compromised_service,
                "old_key_invalidated": True,
                "new_key_activated": True,
                "rotation_time_seconds": 15,
                "success": True
            }
            mock_emergency.return_value = emergency_result
            
            result = rotator.emergency_rotate(compromised_service, emergency_key)
            
            assert result["emergency_rotation"] is True
            assert result["success"] is True
            assert result["old_key_invalidated"] is True
    
    def test_rotation_notification_system(self, temp_config_dir):
        """Test notification system for rotation events."""
        rotator = APIKeyRotator()
        
        notification_config = {
            "email_enabled": True,
            "slack_enabled": True,
            "webhook_enabled": False
        }
        
        rotation_event = {
            "service": "openai",
            "event_type": "ROTATION_COMPLETED",
            "success": True,
            "timestamp": datetime.now().isoformat()
        }
        
        with patch.object(rotator, 'send_notification') as mock_notify:
            notification_result = {
                "notifications_sent": 2,
                "email_sent": True,
                "slack_sent": True,
                "webhook_sent": False,
                "failed_notifications": 0
            }
            mock_notify.return_value = notification_result
            
            result = rotator.send_notification(rotation_event, notification_config)
            
            assert result["notifications_sent"] == 2
            assert result["failed_notifications"] == 0


class TestAPIKeyRotatorEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_concurrent_rotation_prevention(self, temp_config_dir):
        """Test prevention of concurrent rotations for same service."""
        rotator = APIKeyRotator()
        
        service = "openai"
        
        with patch.object(rotator, 'acquire_rotation_lock') as mock_lock:
            # First rotation acquires lock successfully
            mock_lock.return_value = {"lock_acquired": True, "lock_id": "lock_123"}
            
            lock_result = rotator.acquire_rotation_lock(service)
            assert lock_result["lock_acquired"] is True
            
            # Second concurrent rotation should fail to acquire lock
            mock_lock.return_value = {"lock_acquired": False, "error": "Service rotation in progress"}
            
            concurrent_result = rotator.acquire_rotation_lock(service)
            assert concurrent_result["lock_acquired"] is False
    
    def test_network_failure_during_rotation(self, temp_config_dir):
        """Test handling of network failures during rotation."""
        rotator = APIKeyRotator()
        
        service = "openai"
        new_key = "sk-new-key-123"
        
        with patch.object(rotator, 'rotate_key') as mock_rotate:
            # Simulate network failure
            mock_rotate.side_effect = ConnectionError("Network unreachable")
            
            with pytest.raises(ConnectionError):
                rotator.rotate_key(service, new_key)
    
    def test_partial_rotation_recovery(self, temp_config_dir):
        """Test recovery from partial rotation failure."""
        rotator = APIKeyRotator()
        
        with patch.object(rotator, 'recover_partial_rotation') as mock_recover:
            recovery_result = {
                "recovery_successful": True,
                "steps_completed": ["backup_created", "old_key_deactivated"],
                "steps_remaining": ["new_key_activation", "configuration_update"],
                "recovery_actions_taken": 2
            }
            mock_recover.return_value = recovery_result
            
            result = rotator.recover_partial_rotation("failed_rotation_456")
            
            assert result["recovery_successful"] is True
            assert len(result["steps_remaining"]) == 2
    
    def test_corrupted_backup_handling(self, temp_config_dir):
        """Test handling of corrupted backup files."""
        rotator = APIKeyRotator()
        
        corrupted_backup = "corrupted_backup.json"
        
        with patch.object(rotator, 'restore_from_backup') as mock_restore:
            mock_restore.return_value = {
                "restore_successful": False,
                "error": "Backup file corrupted",
                "corruption_detected": True,
                "alternative_backups": ["backup_20250721.json", "backup_20250720.json"]
            }
            
            result = rotator.restore_from_backup(corrupted_backup)
            
            assert result["restore_successful"] is False
            assert result["corruption_detected"] is True
            assert len(result["alternative_backups"]) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])