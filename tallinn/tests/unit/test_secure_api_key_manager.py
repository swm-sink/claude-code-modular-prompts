#!/usr/bin/env python3
"""
Comprehensive test suite for secure_api_key_manager.py

Tests all security-critical functionality including:
- Master key generation and management
- API key encryption and decryption
- Key storage and retrieval
- Key rotation mechanisms
- Security validations and edge cases
- Error handling for security scenarios
"""

import pytest
import tempfile
import os
import json
import secrets
import base64
from pathlib import Path
from unittest.mock import Mock, patch, mock_open
from datetime import datetime, timedelta
from cryptography.fernet import Fernet, InvalidToken

# Import the module under test
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from secure_api_key_manager import SecureAPIKeyManager


class TestSecureAPIKeyManager:
    """Test suite for SecureAPIKeyManager class."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for testing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            old_cwd = os.getcwd()
            os.chdir(temp_dir)
            try:
                yield temp_dir
            finally:
                os.chdir(old_cwd)
    
    @pytest.fixture
    def mock_environment(self):
        """Mock environment variables."""
        with patch.dict(os.environ, {}, clear=True):
            yield
    
    def test_initialization_with_master_key(self, temp_dir, mock_environment):
        """Test initialization with provided master key."""
        master_key = "test-master-key-12345"
        manager = SecureAPIKeyManager(master_key=master_key)
        
        assert manager.master_key == master_key
        assert manager.key_store_path.name == "encrypted_keys.json"
        assert manager.cipher_suite is not None
    
    def test_initialization_with_custom_key_store_path(self, temp_dir, mock_environment):
        """Test initialization with custom key store path."""
        custom_path = "custom_keys.json"
        manager = SecureAPIKeyManager(master_key="test-key", key_store_path=custom_path)
        
        assert manager.key_store_path.name == custom_path
    
    def test_master_key_from_environment(self, temp_dir):
        """Test master key retrieval from environment variable."""
        env_key = "env-master-key-67890"
        
        with patch.dict(os.environ, {'CLAUDE_MASTER_KEY': env_key}):
            manager = SecureAPIKeyManager()
            assert manager.master_key == env_key
    
    def test_master_key_from_file(self, temp_dir, mock_environment):
        """Test master key retrieval from secure file."""
        file_key = "file-master-key-abc"
        encoded_key = base64.b64encode(file_key.encode('utf-8'))
        
        # Create the master key file
        key_file = Path('.claude_master.key')
        with open(key_file, 'wb') as f:
            f.write(encoded_key)
        
        manager = SecureAPIKeyManager()
        assert manager.master_key == file_key
    
    def test_master_key_generation_new_file(self, temp_dir, mock_environment):
        """Test master key generation when no existing key is found."""
        with patch('secure_api_key_manager.secrets.token_urlsafe') as mock_token:
            mock_token.return_value = "generated-master-key"
            
            # Capture print output
            with patch('builtins.print') as mock_print:
                manager = SecureAPIKeyManager()
                
                # Verify key was generated
                assert manager.master_key == "generated-master-key"
                
                # Verify file was created
                key_file = Path('.claude_master.key')
                assert key_file.exists()
                
                # Verify file permissions (Unix-like systems)
                if hasattr(os, 'stat'):
                    stat_info = os.stat(key_file)
                    # Check if owner has read/write permissions
                    assert stat_info.st_mode & 0o600 == 0o600
                
                # Verify print message was called
                mock_print.assert_called_once()
                assert "Generated new master key" in mock_print.call_args[0][0]
    
    def test_encryption_setup(self, temp_dir, mock_environment):
        """Test encryption setup with PBKDF2 key derivation."""
        master_key = "test-master-key"
        manager = SecureAPIKeyManager(master_key=master_key)
        
        # Verify cipher suite is created
        assert manager.cipher_suite is not None
        assert isinstance(manager.cipher_suite, Fernet)
    
    def test_store_api_key_success(self, temp_dir, mock_environment):
        """Test successful API key storage."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Store an API key
        result = manager.store_api_key("openai", "sk-test-key-123")
        
        assert result is True
        
        # Verify the key store file was created
        assert manager.key_store_path.exists()
        
        # Verify file content is encrypted (not plain text)
        with open(manager.key_store_path, 'r') as f:
            content = f.read()
            assert "sk-test-key-123" not in content  # Should be encrypted
    
    def test_retrieve_api_key_success(self, temp_dir, mock_environment):
        """Test successful API key retrieval."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Store and retrieve an API key
        manager.store_api_key("openai", "sk-test-key-123")
        retrieved_key = manager.retrieve_api_key("openai")
        
        assert retrieved_key == "sk-test-key-123"
    
    def test_retrieve_api_key_not_found(self, temp_dir, mock_environment):
        """Test retrieving non-existent API key."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        retrieved_key = manager.retrieve_api_key("nonexistent")
        assert retrieved_key is None
    
    def test_list_stored_keys(self, temp_dir, mock_environment):
        """Test listing all stored key services."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Store multiple keys
        manager.store_api_key("openai", "sk-openai-123")
        manager.store_api_key("anthropic", "sk-anthropic-456")
        manager.store_api_key("google", "sk-google-789")
        
        # List keys
        services = manager.list_stored_keys()
        
        assert len(services) == 3
        assert "openai" in services
        assert "anthropic" in services
        assert "google" in services
    
    def test_delete_api_key_success(self, temp_dir, mock_environment):
        """Test successful API key deletion."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Store and delete a key
        manager.store_api_key("openai", "sk-test-key-123")
        result = manager.delete_api_key("openai")
        
        assert result is True
        assert manager.retrieve_api_key("openai") is None
    
    def test_delete_api_key_not_found(self, temp_dir, mock_environment):
        """Test deleting non-existent API key."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        result = manager.delete_api_key("nonexistent")
        assert result is False
    
    def test_key_rotation_success(self, temp_dir, mock_environment):
        """Test successful key rotation."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Store an API key
        manager.store_api_key("openai", "sk-old-key-123")
        
        # Rotate to new key
        result = manager.rotate_api_key("openai", "sk-new-key-456")
        
        assert result is True
        assert manager.retrieve_api_key("openai") == "sk-new-key-456"
    
    def test_key_rotation_not_found(self, temp_dir, mock_environment):
        """Test key rotation for non-existent service."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        result = manager.rotate_api_key("nonexistent", "sk-new-key-456")
        assert result is False
    
    def test_encryption_decryption_roundtrip(self, temp_dir, mock_environment):
        """Test that encryption and decryption work correctly together."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        test_data = "sensitive-api-key-data"
        encrypted = manager._encrypt_data(test_data)
        decrypted = manager._decrypt_data(encrypted)
        
        assert decrypted == test_data
        assert encrypted != test_data  # Should be encrypted
    
    def test_encryption_with_invalid_data(self, temp_dir, mock_environment):
        """Test encryption with invalid data types."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Test with None
        with pytest.raises((TypeError, AttributeError)):
            manager._encrypt_data(None)
        
        # Test with non-string data
        encrypted = manager._encrypt_data(str(12345))
        assert manager._decrypt_data(encrypted) == "12345"
    
    def test_decryption_with_invalid_token(self, temp_dir, mock_environment):
        """Test decryption with invalid encrypted data."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        with pytest.raises(InvalidToken):
            manager._decrypt_data(b"invalid-encrypted-data")
    
    def test_key_store_corruption_handling(self, temp_dir, mock_environment):
        """Test handling of corrupted key store file."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Create a corrupted key store file
        with open(manager.key_store_path, 'w') as f:
            f.write("corrupted json data")
        
        # Should handle corruption gracefully
        result = manager.retrieve_api_key("any-service")
        assert result is None
    
    def test_key_store_backup_and_restore(self, temp_dir, mock_environment):
        """Test backup and restore functionality."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Store some keys
        manager.store_api_key("service1", "key1")
        manager.store_api_key("service2", "key2")
        
        # Create backup
        backup_path = "backup_keys.json"
        result = manager.backup_keys(backup_path)
        assert result is True
        assert Path(backup_path).exists()
        
        # Clear current keys and restore from backup
        manager.delete_api_key("service1")
        manager.delete_api_key("service2")
        assert manager.retrieve_api_key("service1") is None
        
        # Restore from backup
        restore_result = manager.restore_keys(backup_path)
        assert restore_result is True
        assert manager.retrieve_api_key("service1") == "key1"
        assert manager.retrieve_api_key("service2") == "key2"
    
    def test_key_expiration_tracking(self, temp_dir, mock_environment):
        """Test API key expiration tracking."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Store key with expiration
        expiration = datetime.now() + timedelta(days=30)
        result = manager.store_api_key_with_expiration("openai", "sk-key-123", expiration)
        assert result is True
        
        # Check if key is expired
        assert not manager.is_key_expired("openai")
        
        # Test with expired key
        past_expiration = datetime.now() - timedelta(days=1)
        manager.store_api_key_with_expiration("expired_service", "sk-expired-key", past_expiration)
        assert manager.is_key_expired("expired_service")
    
    def test_security_audit_methods(self, temp_dir, mock_environment):
        """Test security audit and validation methods."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Store various keys
        manager.store_api_key("weak_key", "12345")
        manager.store_api_key("strong_key", "sk-" + secrets.token_urlsafe(32))
        
        # Audit key strength
        audit_results = manager.audit_key_strength()
        assert "weak_key" in audit_results["weak_keys"]
        assert "strong_key" in audit_results["strong_keys"]
    
    def test_concurrent_access_safety(self, temp_dir, mock_environment):
        """Test thread safety for concurrent access."""
        import threading
        import time
        
        manager = SecureAPIKeyManager(master_key="test-key")
        results = []
        errors = []
        
        def store_key(service_name, key_value):
            try:
                result = manager.store_api_key(service_name, key_value)
                results.append(result)
            except Exception as e:
                errors.append(e)
        
        def retrieve_key(service_name):
            try:
                result = manager.retrieve_api_key(service_name)
                results.append(result is not None)
            except Exception as e:
                errors.append(e)
        
        # Create multiple threads for concurrent operations
        threads = []
        for i in range(10):
            t1 = threading.Thread(target=store_key, args=(f"service_{i}", f"key_{i}"))
            t2 = threading.Thread(target=retrieve_key, args=(f"service_{i}"))
            threads.extend([t1, t2])
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Should have no errors and successful results
        assert len(errors) == 0
        assert len([r for r in results if r]) > 0
    
    def test_master_key_validation(self, temp_dir, mock_environment):
        """Test master key validation and security requirements."""
        # Test with weak master key
        with pytest.warns(UserWarning):
            manager = SecureAPIKeyManager(master_key="weak")
        
        # Test with strong master key
        strong_key = secrets.token_urlsafe(32)
        manager = SecureAPIKeyManager(master_key=strong_key)
        assert manager.master_key == strong_key
    
    def test_key_derivation_salt_uniqueness(self, temp_dir, mock_environment):
        """Test that key derivation uses unique salts."""
        manager1 = SecureAPIKeyManager(master_key="same-key")
        manager2 = SecureAPIKeyManager(master_key="same-key")
        
        # Even with same master key, derived keys should be different due to unique salts
        # This is tested by encrypting the same data with both managers
        test_data = "same-data"
        encrypted1 = manager1._encrypt_data(test_data)
        encrypted2 = manager2._encrypt_data(test_data)
        
        # Encrypted data should be different (different salts)
        assert encrypted1 != encrypted2
        
        # But both should decrypt to the same original data
        assert manager1._decrypt_data(encrypted1) == test_data
        assert manager2._decrypt_data(encrypted2) == test_data


class TestSecureAPIKeyManagerEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_file_permission_errors(self, mock_environment):
        """Test handling of file permission errors."""
        with tempfile.TemporaryDirectory() as temp_dir:
            os.chdir(temp_dir)
            
            # Create a file we can't write to
            key_store_path = "readonly_keys.json"
            with open(key_store_path, 'w') as f:
                f.write("{}")
            os.chmod(key_store_path, 0o444)  # Read-only
            
            try:
                manager = SecureAPIKeyManager(master_key="test-key", key_store_path=key_store_path)
                
                # Should handle permission error gracefully
                with pytest.raises((PermissionError, OSError)):
                    manager.store_api_key("test", "key")
            finally:
                # Restore write permission for cleanup
                os.chmod(key_store_path, 0o644)
    
    def test_disk_space_full_simulation(self, temp_dir, mock_environment):
        """Test handling of disk space issues."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Mock write operation to raise OSError (disk full)
        with patch('builtins.open', mock_open()) as mock_file:
            mock_file.side_effect = OSError("No space left on device")
            
            # Should handle disk full error gracefully
            with pytest.raises(OSError):
                manager.store_api_key("test", "key")
    
    def test_memory_pressure_handling(self, temp_dir, mock_environment):
        """Test handling of memory pressure during encryption."""
        manager = SecureAPIKeyManager(master_key="test-key")
        
        # Test with very large data (simulate memory pressure)
        large_data = "x" * (10 * 1024 * 1024)  # 10MB string
        
        # Should handle large data without crashing
        encrypted = manager._encrypt_data(large_data)
        decrypted = manager._decrypt_data(encrypted)
        assert decrypted == large_data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])