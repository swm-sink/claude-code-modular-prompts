#!/usr/bin/env python3
"""
Test-Driven Development (TDD) tests for SecureAPIKeyManager

This module implements comprehensive tests following TDD principles:
1. Red: Write failing tests first
2. Green: Implement minimal code to pass
3. Refactor: Improve code while keeping tests green
"""

import os
import json
import tempfile
import shutil
from pathlib import Path
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, mock_open
import pytest

# Import test utilities
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from test_utils import TestDataFactory, MockFactory, AssertionHelpers

# Import the module under test
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from secure_api_key_manager import SecureAPIKeyManager


class TestSecureAPIKeyManagerTDD:
    """TDD tests for SecureAPIKeyManager."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test files."""
        temp_path = tempfile.mkdtemp()
        original_cwd = os.getcwd()
        os.chdir(temp_path)
        yield Path(temp_path)
        os.chdir(original_cwd)
        shutil.rmtree(temp_path)
    
    @pytest.fixture
    def manager(self, temp_dir):
        """Create a SecureAPIKeyManager instance for testing."""
        # Use a fixed master key for testing
        test_master_key = "test-master-key-for-unit-tests"
        return SecureAPIKeyManager(
            master_key=test_master_key,
            key_store_path=str(temp_dir / "test_keys.json")
        )
    
    # Test 1: Manager Initialization
    def test_manager_initializes_with_master_key(self, temp_dir):
        """Test that manager initializes correctly with provided master key."""
        test_master_key = "test-master-key"
        manager = SecureAPIKeyManager(
            master_key=test_master_key,
            key_store_path=str(temp_dir / "test_keys.json")
        )
        
        assert manager.master_key == test_master_key
        assert manager.key_store_path == temp_dir / "test_keys.json"
        assert manager.cipher_suite is not None
    
    # Test 2: Master Key from Environment
    def test_manager_uses_environment_master_key(self, temp_dir):
        """Test that manager uses CLAUDE_MASTER_KEY from environment."""
        env_key = "env-master-key-12345"
        with patch.dict(os.environ, {'CLAUDE_MASTER_KEY': env_key}):
            manager = SecureAPIKeyManager(key_store_path=str(temp_dir / "test_keys.json"))
            assert manager.master_key == env_key
    
    # Test 3: Master Key Generation
    def test_manager_generates_master_key_when_missing(self, temp_dir):
        """Test that manager generates a new master key when none exists."""
        with patch.dict(os.environ, {}, clear=True):
            # Remove CLAUDE_MASTER_KEY from environment
            if 'CLAUDE_MASTER_KEY' in os.environ:
                del os.environ['CLAUDE_MASTER_KEY']
                
            manager = SecureAPIKeyManager(key_store_path=str(temp_dir / "test_keys.json"))
            
            # Check that master key was generated
            assert manager.master_key is not None
            assert len(manager.master_key) >= 32
            
            # Check that key file was created
            key_file = Path('.claude_master.key')
            assert key_file.exists()
            
            # Check file permissions (owner read/write only)
            stat_info = key_file.stat()
            assert stat_info.st_mode & 0o777 == 0o600
    
    # Test 4: Encrypt API Key
    def test_encrypt_api_key_stores_encrypted_data(self, manager, temp_dir):
        """Test that API keys are encrypted and stored correctly."""
        key_name = "openai"
        api_key = TestDataFactory.create_api_key("openai")
        metadata = {"provider": "OpenAI", "model": "gpt-4"}
        
        # Encrypt the API key
        key_id = manager.encrypt_api_key(key_name, api_key, metadata)
        
        # Verify key ID format
        assert key_id.startswith("key_")
        assert len(key_id) == 20  # "key_" + 16 hex chars
        
        # Verify key store was created
        assert manager.key_store_path.exists()
        
        # Load and verify key store contents
        with open(manager.key_store_path, 'r') as f:
            key_store = json.load(f)
        
        assert key_id in key_store['keys']
        stored_key = key_store['keys'][key_id]
        
        assert stored_key['name'] == key_name
        assert stored_key['status'] == 'active'
        assert 'encrypted_data' in stored_key
        assert 'created' in stored_key
        assert 'expires' in stored_key
        
        # Encrypted data should be base64 encoded
        import base64
        try:
            base64.b64decode(stored_key['encrypted_data'])
        except Exception:
            pytest.fail("Encrypted data is not valid base64")
    
    # Test 5: Decrypt API Key
    def test_decrypt_api_key_retrieves_original_key(self, manager):
        """Test that encrypted keys can be decrypted correctly."""
        key_name = "anthropic"
        api_key = TestDataFactory.create_api_key("anthropic")
        metadata = {"provider": "Anthropic", "model": "claude-3"}
        
        # Encrypt the key
        key_id = manager.encrypt_api_key(key_name, api_key, metadata)
        
        # Decrypt the key
        decrypted_data = manager.decrypt_api_key(key_id)
        
        assert decrypted_data['name'] == key_name
        assert decrypted_data['api_key'] == api_key
        assert decrypted_data['metadata'] == metadata
        assert decrypted_data['usage_count'] == 1  # Should increment on decrypt
        assert decrypted_data['last_used'] is not None
    
    # Test 6: Decrypt Non-existent Key
    def test_decrypt_non_existent_key_raises_error(self, manager):
        """Test that decrypting a non-existent key raises ValueError."""
        with pytest.raises(ValueError, match="not found"):
            manager.decrypt_api_key("key_nonexistent123")
    
    # Test 7: Decrypt Expired Key
    def test_decrypt_expired_key_raises_error(self, manager):
        """Test that decrypting an expired key raises ValueError."""
        key_name = "expired-key"
        api_key = "test-api-key"
        
        # Encrypt the key
        key_id = manager.encrypt_api_key(key_name, api_key)
        
        # Manually expire the key
        key_store = manager._load_key_store()
        past_date = (datetime.now() - timedelta(days=1)).isoformat()
        key_store['keys'][key_id]['expires'] = past_date
        manager._save_key_store(key_store)
        
        # Try to decrypt expired key
        with pytest.raises(ValueError, match="expired"):
            manager.decrypt_api_key(key_id)
    
    # Test 8: Rotate API Key
    def test_rotate_api_key_creates_new_key(self, manager):
        """Test that rotating a key creates a new key and archives the old one."""
        key_name = "rotate-test"
        old_api_key = "old-api-key-123"
        new_api_key = "new-api-key-456"
        
        # Create initial key
        old_key_id = manager.encrypt_api_key(key_name, old_api_key)
        
        # Rotate the key
        new_key_id = manager.rotate_api_key(old_key_id, new_api_key)
        
        # Verify new key was created
        assert new_key_id != old_key_id
        assert new_key_id.startswith("key_")
        
        # Verify old key was archived
        key_store = manager._load_key_store()
        assert key_store['keys'][old_key_id]['status'] == 'rotated'
        assert 'rotated_at' in key_store['keys'][old_key_id]
        
        # Verify new key is active
        assert key_store['keys'][new_key_id]['status'] == 'active'
        
        # Verify rotation history
        assert 'rotation_history' in key_store['metadata']
        assert len(key_store['metadata']['rotation_history']) == 1
        rotation = key_store['metadata']['rotation_history'][0]
        assert rotation['old_key_id'] == old_key_id
        assert rotation['new_key_id'] == new_key_id
    
    # Test 9: List API Keys
    def test_list_api_keys_returns_metadata_only(self, manager):
        """Test that listing keys returns metadata without actual keys."""
        # Create multiple keys
        keys = [
            ("openai", TestDataFactory.create_api_key("openai")),
            ("anthropic", TestDataFactory.create_api_key("anthropic")),
            ("google", TestDataFactory.create_api_key("google"))
        ]
        
        key_ids = []
        for name, api_key in keys:
            key_id = manager.encrypt_api_key(name, api_key)
            key_ids.append(key_id)
        
        # List all keys
        key_list = manager.list_api_keys()
        
        assert len(key_list) == 3
        
        for key_info in key_list:
            assert 'key_id' in key_info
            assert 'name' in key_info
            assert 'status' in key_info
            assert 'created' in key_info
            assert 'expires' in key_info
            # Actual API key should NOT be included
            assert 'api_key' not in key_info
            assert 'encrypted_data' not in key_info
    
    # Test 10: Revoke API Key
    def test_revoke_api_key_marks_as_revoked(self, manager):
        """Test that revoking a key marks it as revoked."""
        key_name = "revoke-test"
        api_key = "test-api-key"
        
        # Create a key
        key_id = manager.encrypt_api_key(key_name, api_key)
        
        # Revoke the key
        result = manager.revoke_api_key(key_id)
        assert result is True
        
        # Verify key is revoked
        key_store = manager._load_key_store()
        assert key_store['keys'][key_id]['status'] == 'revoked'
        
        # Try to decrypt revoked key
        with pytest.raises(ValueError, match="not active"):
            manager.decrypt_api_key(key_id)
    
    # Test 11: Cleanup Expired Keys
    def test_cleanup_expired_keys_removes_old_keys(self, manager):
        """Test that cleanup removes expired keys."""
        # Create keys with different expiration times
        current_time = datetime.now()
        
        # Active key
        active_id = manager.encrypt_api_key("active", "active-key")
        
        # Expired keys
        expired_ids = []
        for i in range(3):
            key_id = manager.encrypt_api_key(f"expired-{i}", f"expired-key-{i}")
            expired_ids.append(key_id)
            
            # Manually expire the keys
            key_store = manager._load_key_store()
            past_date = (current_time - timedelta(days=i+1)).isoformat()
            key_store['keys'][key_id]['expires'] = past_date
            manager._save_key_store(key_store)
        
        # Run cleanup
        removed_count = manager.cleanup_expired_keys()
        
        assert removed_count == 3
        
        # Verify expired keys are gone
        key_store = manager._load_key_store()
        for key_id in expired_ids:
            assert key_id not in key_store['keys']
        
        # Verify active key remains
        assert active_id in key_store['keys']
    
    # Test 12: Export Keys for Backup
    def test_export_keys_for_backup_without_keys(self, manager, temp_dir):
        """Test exporting key metadata for backup without actual keys."""
        # Create some keys
        key1_id = manager.encrypt_api_key("key1", "api-key-1")
        key2_id = manager.encrypt_api_key("key2", "api-key-2")
        
        # Export backup without keys
        backup_path = str(temp_dir / "backup.json")
        result = manager.export_keys_for_backup(backup_path, include_keys=False)
        
        assert result is True
        assert Path(backup_path).exists()
        
        # Load and verify backup
        with open(backup_path, 'r') as f:
            backup_data = json.load(f)
        
        assert 'metadata' in backup_data
        assert 'keys' in backup_data
        assert len(backup_data['keys']) == 2
        
        # Verify no actual keys are included
        for key_id, key_data in backup_data['keys'].items():
            assert 'encrypted_data' not in key_data
    
    # Test 13: Key Usage Tracking
    def test_key_usage_tracking_increments_correctly(self, manager):
        """Test that key usage is tracked correctly."""
        key_name = "usage-test"
        api_key = "test-api-key"
        
        # Create a key
        key_id = manager.encrypt_api_key(key_name, api_key)
        
        # Use the key multiple times
        for i in range(5):
            decrypted = manager.decrypt_api_key(key_id)
            assert decrypted['usage_count'] == i + 1
    
    # Test 14: Thread Safety
    def test_concurrent_key_operations(self, manager):
        """Test that concurrent operations don't corrupt the key store."""
        import threading
        import concurrent.futures
        
        def create_key(name):
            try:
                key_id = manager.encrypt_api_key(name, f"api-key-{name}")
                return key_id
            except Exception as e:
                return str(e)
        
        # Create keys concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(create_key, f"concurrent-{i}") for i in range(10)]
            results = [f.result() for f in concurrent.futures.as_completed(futures)]
        
        # Verify all keys were created
        successful_keys = [r for r in results if r.startswith("key_")]
        assert len(successful_keys) >= 8  # Allow some failures due to file locking
        
        # Verify key store integrity
        key_store = manager._load_key_store()
        assert 'keys' in key_store
        assert 'metadata' in key_store
    
    # Test 15: Error Handling
    def test_error_handling_with_corrupted_key_store(self, manager, temp_dir):
        """Test handling of corrupted key store."""
        # Create a valid key first
        key_id = manager.encrypt_api_key("test", "test-key")
        
        # Corrupt the key store
        with open(manager.key_store_path, 'w') as f:
            f.write("invalid json{")
        
        # Try to load keys - should handle gracefully
        key_list = manager.list_api_keys()
        assert isinstance(key_list, list)
        assert len(key_list) == 0  # Should return empty list on error


class TestSecureAPIKeyManagerEdgeCases:
    """Edge case tests for SecureAPIKeyManager."""
    
    @pytest.fixture
    def manager(self):
        """Create a manager with in-memory storage."""
        return SecureAPIKeyManager(
            master_key="edge-case-test-key",
            key_store_path=":memory:"  # Special case for testing
        )
    
    def test_extremely_long_api_key(self, manager):
        """Test handling of extremely long API keys."""
        long_key = "x" * 10000  # 10KB key
        
        key_id = manager.encrypt_api_key("long-key", long_key)
        decrypted = manager.decrypt_api_key(key_id)
        
        assert decrypted['api_key'] == long_key
    
    def test_special_characters_in_key_name(self, manager):
        """Test handling of special characters in key names."""
        special_names = [
            "key with spaces",
            "key/with/slashes",
            "key\\with\\backslashes",
            "key:with:colons",
            "key|with|pipes",
            "key'with'quotes",
            'key"with"double"quotes',
            "key\nwith\nnewlines",
            "key\twith\ttabs"
        ]
        
        for name in special_names:
            key_id = manager.encrypt_api_key(name, "test-key")
            decrypted = manager.decrypt_api_key(key_id)
            assert decrypted['name'] == name
    
    def test_unicode_in_metadata(self, manager):
        """Test handling of Unicode in metadata."""
        metadata = {
            "emoji": "🔑🔐🔒",
            "chinese": "密钥管理",
            "arabic": "إدارة المفاتيح",
            "russian": "Управление ключами"
        }
        
        key_id = manager.encrypt_api_key("unicode-test", "test-key", metadata)
        decrypted = manager.decrypt_api_key(key_id)
        
        assert decrypted['metadata'] == metadata


if __name__ == "__main__":
    pytest.main([__file__, "-v"])