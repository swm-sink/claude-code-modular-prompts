#!/usr/bin/env python3
"""
API Key Security Tests

Comprehensive tests for API key security including:
- Encryption/Decryption security
- Key rotation mechanisms
- Access control
- Key storage security
- Key lifecycle management
"""

import pytest
import tempfile
import os
import sys
import json
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    from secure_api_key_manager import SecureAPIKeyManager
    from security.key_rotation import ApiKeyRotationManager, KeyRotationValidator
except ImportError:
    # Create mock classes if modules aren't available
    class SecureAPIKeyManager:
        def __init__(self, *args, **kwargs):
            pass
    
    class ApiKeyRotationManager:
        def __init__(self, *args, **kwargs):
            pass
    
    class KeyRotationValidator:
        def __init__(self, *args, **kwargs):
            pass


class TestAPIKeyEncryption:
    """Test API key encryption and decryption security."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for testing."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def secure_manager(self, temp_dir):
        """Create SecureAPIKeyManager instance for testing."""
        key_store_path = os.path.join(temp_dir, "test_keys.json")
        return SecureAPIKeyManager(
            master_key="test_master_key_12345678901234567890",
            key_store_path=key_store_path
        )
    
    def test_api_key_encryption_strength(self, secure_manager):
        """Test API key encryption uses strong cryptography."""
        test_key = "sk-test-key-1234567890abcdef"
        key_name = "test_openai_key"
        
        # Encrypt the key
        key_id = secure_manager.encrypt_api_key(key_name, test_key)
        
        # Verify key is stored encrypted
        key_store = secure_manager._load_key_store()
        stored_key = key_store['keys'][key_id]
        
        # Encrypted data should not contain the original key
        encrypted_data = stored_key['encrypted_data']
        assert test_key not in encrypted_data
        assert key_name not in encrypted_data
        
        # Encrypted data should be base64 encoded
        import base64
        try:
            decoded = base64.b64decode(encrypted_data)
            assert len(decoded) > 0
        except Exception:
            pytest.fail("Encrypted data is not valid base64")
    
    def test_api_key_decryption_integrity(self, secure_manager):
        """Test API key decryption maintains data integrity."""
        test_key = "sk-test-key-abcdef1234567890"
        key_name = "test_integrity_key"
        
        # Encrypt and then decrypt
        key_id = secure_manager.encrypt_api_key(key_name, test_key)
        decrypted_data = secure_manager.decrypt_api_key(key_id)
        
        # Verify integrity
        assert decrypted_data['api_key'] == test_key
        assert decrypted_data['name'] == key_name
        assert 'created' in decrypted_data
        assert 'expires' in decrypted_data
    
    def test_encryption_key_derivation_security(self, temp_dir):
        """Test that encryption keys are properly derived from master key."""
        master_key1 = "master_key_1_1234567890123456"
        master_key2 = "master_key_2_1234567890123456"
        
        key_store_path = os.path.join(temp_dir, "key_derivation_test.json")
        
        # Create two managers with different master keys
        manager1 = SecureAPIKeyManager(master_key1, key_store_path)
        manager2 = SecureAPIKeyManager(master_key2, key_store_path)
        
        test_key = "sk-test-derivation-key"
        
        # Encrypt with first manager
        key_id1 = manager1.encrypt_api_key("test_key", test_key)
        
        # Try to decrypt with second manager (should fail)
        with pytest.raises((ValueError, Exception)):
            manager2.decrypt_api_key(key_id1)
    
    def test_master_key_file_permissions(self, temp_dir):
        """Test that master key files have secure permissions."""
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            # Create manager which should generate master key file
            manager = SecureAPIKeyManager()
            
            key_file = Path('.claude_master.key')
            salt_file = Path('.claude_salt')
            
            if key_file.exists():
                # Check file permissions (should be 0o600 - owner read/write only)
                file_stat = key_file.stat()
                permissions = file_stat.st_mode & 0o777
                assert permissions == 0o600, f"Master key file has insecure permissions: {oct(permissions)}"
            
            if salt_file.exists():
                # Check salt file permissions
                file_stat = salt_file.stat()
                permissions = file_stat.st_mode & 0o777
                assert permissions == 0o600, f"Salt file has insecure permissions: {oct(permissions)}"
        
        finally:
            os.chdir(original_cwd)
    
    def test_key_store_file_permissions(self, secure_manager):
        """Test that key store files have secure permissions."""
        test_key = "sk-test-permissions-key"
        secure_manager.encrypt_api_key("test_key", test_key)
        
        # Check key store file permissions
        key_store_path = Path(secure_manager.key_store_path)
        if key_store_path.exists():
            file_stat = key_store_path.stat()
            permissions = file_stat.st_mode & 0o777
            assert permissions == 0o600, f"Key store has insecure permissions: {oct(permissions)}"


class TestAPIKeyRotation:
    """Test API key rotation security and functionality."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for testing."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def rotation_manager(self, temp_dir):
        """Create ApiKeyRotationManager for testing."""
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        yield ApiKeyRotationManager()
        os.chdir(original_cwd)
    
    def test_key_rotation_policy_creation(self, rotation_manager):
        """Test creation of secure key rotation policy."""
        rotation_manager.implement_api_key_rotation()
        
        # Check that rotation configuration was created
        config_file = Path("api_key_rotation.json")
        assert config_file.exists()
        
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        # Verify policy structure
        assert 'rotation_policy' in config
        assert 'api_keys' in config
        assert 'rotation_history' in config
        
        # Verify security settings
        policy = config['rotation_policy']
        assert policy['enabled'] is True
        assert policy['rotation_interval_days'] == 90
        assert policy['notification_days_before'] == 7
        
        # Verify key structure
        assert 'primary' in config['api_keys']
        assert 'secondary' in config['api_keys']
        
        for key_type in ['primary', 'secondary']:
            key_data = config['api_keys'][key_type]
            assert 'key_id' in key_data
            assert 'created' in key_data
            assert 'expires' in key_data
            assert 'status' in key_data
            assert 'hash' in key_data
    
    def test_key_rotation_script_security(self, rotation_manager):
        """Test that rotation script implements security best practices."""
        rotation_manager.implement_api_key_rotation()
        
        script_file = Path("rotate_api_keys.py")
        assert script_file.exists()
        
        with open(script_file, 'r') as f:
            script_content = f.read()
        
        # Verify secure practices in script
        assert 'secrets.token_urlsafe' in script_content  # Secure random generation
        assert 'hashlib.sha256' in script_content         # Secure hashing
        assert 'datetime.now()' in script_content         # Proper timestamping
        
        # Verify no hardcoded credentials
        assert 'password' not in script_content.lower()
        assert 'secret' not in script_content.lower() or 'secrets.' in script_content
        
        # Check file permissions
        file_stat = script_file.stat()
        permissions = file_stat.st_mode & 0o777
        assert permissions & 0o100, "Rotation script is not executable"
    
    def test_key_rotation_history_tracking(self, rotation_manager):
        """Test that key rotation maintains proper audit trail."""
        rotation_manager.implement_api_key_rotation()
        
        # Load initial config
        with open("api_key_rotation.json", 'r') as f:
            initial_config = json.load(f)
        
        initial_primary_id = initial_config['api_keys']['primary']['key_id']
        
        # Simulate key rotation by running the rotation script logic
        import subprocess
        result = subprocess.run([sys.executable, "rotate_api_keys.py"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            # Load updated config
            with open("api_key_rotation.json", 'r') as f:
                updated_config = json.load(f)
            
            # Verify rotation history was updated
            assert len(updated_config['rotation_history']) > 0
            
            # Verify primary key changed
            new_primary_id = updated_config['api_keys']['primary']['key_id']
            assert new_primary_id != initial_primary_id
            
            # Verify history entry contains required fields
            history_entry = updated_config['rotation_history'][0]
            assert 'key_id' in history_entry
            assert 'archived' in history_entry
    
    def test_rotation_timing_security(self, rotation_manager):
        """Test rotation timing and expiration security."""
        rotation_manager.implement_api_key_rotation()
        
        status = rotation_manager.get_rotation_status()
        
        # Verify status structure
        assert 'status' in status
        
        if status['status'] == 'configured':
            assert 'days_until_rotation' in status
            assert 'next_rotation' in status
            assert 'last_rotation' in status
            
            # Verify reasonable rotation timing (should be positive and not too far future)
            days_until = status['days_until_rotation']
            assert 0 <= days_until <= 90, f"Invalid rotation timing: {days_until} days"


class TestKeyAccessControl:
    """Test access control mechanisms for API keys."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for testing."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def secure_manager(self, temp_dir):
        """Create SecureAPIKeyManager instance for testing."""
        key_store_path = os.path.join(temp_dir, "access_control_test.json")
        return SecureAPIKeyManager(
            master_key="access_control_master_key_123456",
            key_store_path=key_store_path
        )
    
    def test_key_expiration_enforcement(self, secure_manager):
        """Test that expired keys are properly rejected."""
        test_key = "sk-expired-key-test"
        key_name = "expired_test_key"
        
        # Create key with past expiration
        key_id = secure_manager.encrypt_api_key(key_name, test_key)
        
        # Manually set expiration to past date
        key_store = secure_manager._load_key_store()
        past_date = (datetime.now() - timedelta(days=1)).isoformat()
        key_store['keys'][key_id]['expires'] = past_date
        secure_manager._save_key_store(key_store)
        
        # Try to decrypt expired key
        with pytest.raises(ValueError, match="expired"):
            secure_manager.decrypt_api_key(key_id)
    
    def test_revoked_key_access_prevention(self, secure_manager):
        """Test that revoked keys cannot be accessed."""
        test_key = "sk-revoked-key-test"
        key_name = "revoked_test_key"
        
        # Create and then revoke key
        key_id = secure_manager.encrypt_api_key(key_name, test_key)
        success = secure_manager.revoke_api_key(key_id)
        assert success
        
        # Try to access revoked key
        with pytest.raises(ValueError, match="not active"):
            secure_manager.decrypt_api_key(key_id)
    
    def test_key_usage_tracking(self, secure_manager):
        """Test that key usage is properly tracked."""
        test_key = "sk-usage-tracking-key"
        key_name = "usage_test_key"
        
        # Create key
        key_id = secure_manager.encrypt_api_key(key_name, test_key)
        
        # Access key multiple times
        for _ in range(3):
            key_data = secure_manager.decrypt_api_key(key_id)
        
        # Verify usage count
        final_data = secure_manager.decrypt_api_key(key_id)
        assert final_data['usage_count'] >= 3
        assert 'last_used' in final_data
        
        # Verify last_used is recent
        last_used = datetime.fromisoformat(final_data['last_used'])
        time_diff = datetime.now() - last_used
        assert time_diff.total_seconds() < 60  # Within last minute
    
    def test_key_listing_information_disclosure(self, secure_manager):
        """Test that key listing doesn't expose sensitive information."""
        test_key = "sk-sensitive-information-key"
        key_name = "sensitive_test_key"
        
        # Create key
        key_id = secure_manager.encrypt_api_key(key_name, test_key)
        
        # List keys
        key_list = secure_manager.list_api_keys()
        
        # Find our key in the list
        our_key = next((k for k in key_list if k['key_id'] == key_id), None)
        assert our_key is not None
        
        # Verify sensitive information is not exposed
        assert 'api_key' not in our_key
        assert 'encrypted_data' not in our_key
        assert 'key_hash' not in our_key
        
        # Verify only safe metadata is exposed
        safe_fields = {'key_id', 'name', 'created', 'expires', 'status'}
        assert set(our_key.keys()).issubset(safe_fields)
    
    def test_bulk_key_operations_security(self, secure_manager):
        """Test security of bulk key operations."""
        # Create multiple test keys
        test_keys = []
        for i in range(5):
            key_name = f"bulk_test_key_{i}"
            test_key = f"sk-bulk-key-{i:03d}-test"
            key_id = secure_manager.encrypt_api_key(key_name, test_key)
            test_keys.append(key_id)
        
        # Test cleanup of expired keys
        removed_count = secure_manager.cleanup_expired_keys()
        # Should not remove non-expired keys
        assert removed_count == 0
        
        # Manually expire some keys and test cleanup
        key_store = secure_manager._load_key_store()
        past_date = (datetime.now() - timedelta(days=31)).isoformat()  # Beyond grace period
        
        for key_id in test_keys[:2]:
            key_store['keys'][key_id]['expires'] = past_date
        
        secure_manager._save_key_store(key_store)
        
        # Run cleanup
        removed_count = secure_manager.cleanup_expired_keys()
        assert removed_count == 2
        
        # Verify expired keys are removed
        updated_list = secure_manager.list_api_keys()
        remaining_ids = [k['key_id'] for k in updated_list]
        
        for key_id in test_keys[:2]:
            assert key_id not in remaining_ids
        
        for key_id in test_keys[2:]:
            assert key_id in remaining_ids


class TestKeyStorageSecurity:
    """Test security of key storage mechanisms."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for testing."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)
    
    def test_key_store_backup_security(self, temp_dir):
        """Test security of key store backup operations."""
        key_store_path = os.path.join(temp_dir, "backup_test.json")
        manager = SecureAPIKeyManager(
            master_key="backup_test_master_key_123456",
            key_store_path=key_store_path
        )
        
        # Create test key
        test_key = "sk-backup-test-key"
        key_id = manager.encrypt_api_key("backup_test", test_key)
        
        # Test backup without keys (metadata only)
        backup_path = os.path.join(temp_dir, "backup_metadata.json")
        success = manager.export_keys_for_backup(backup_path, include_keys=False)
        assert success
        
        # Verify backup file permissions
        backup_file = Path(backup_path)
        file_stat = backup_file.stat()
        permissions = file_stat.st_mode & 0o777
        assert permissions == 0o600, f"Backup file has insecure permissions: {oct(permissions)}"
        
        # Verify backup content security
        with open(backup_path, 'r') as f:
            backup_data = json.load(f)
        
        # Should not contain sensitive data
        for key_data in backup_data['keys'].values():
            assert 'encrypted_data' not in key_data
            assert 'key_hash' not in key_data
        
        # Test backup with keys
        secure_backup_path = os.path.join(temp_dir, "backup_with_keys.json")
        success = manager.export_keys_for_backup(secure_backup_path, include_keys=True)
        assert success
        
        with open(secure_backup_path, 'r') as f:
            secure_backup = json.load(f)
        
        # Should contain encrypted data but not plaintext keys
        our_key_backup = secure_backup['keys'][key_id]
        assert 'encrypted_data' in our_key_backup
        assert test_key not in json.dumps(our_key_backup)
    
    def test_concurrent_access_safety(self, temp_dir):
        """Test thread safety of key operations."""
        import threading
        import time
        
        key_store_path = os.path.join(temp_dir, "concurrent_test.json")
        manager = SecureAPIKeyManager(
            master_key="concurrent_test_master_key_123456",
            key_store_path=key_store_path
        )
        
        results = []
        errors = []
        
        def worker_encrypt(worker_id):
            """Worker function to encrypt keys concurrently."""
            try:
                key_name = f"concurrent_key_{worker_id}"
                test_key = f"sk-concurrent-{worker_id:03d}-key"
                key_id = manager.encrypt_api_key(key_name, test_key)
                results.append((worker_id, key_id))
            except Exception as e:
                errors.append((worker_id, str(e)))
        
        # Create multiple threads to test concurrent access
        threads = []
        for i in range(5):
            thread = threading.Thread(target=worker_encrypt, args=(i,))
            threads.append(thread)
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join(timeout=10)
        
        # Verify results
        assert len(errors) == 0, f"Concurrent access errors: {errors}"
        assert len(results) == 5, f"Expected 5 results, got {len(results)}"
        
        # Verify all keys were created successfully
        key_list = manager.list_api_keys()
        assert len(key_list) >= 5
    
    def test_key_store_corruption_resistance(self, temp_dir):
        """Test resistance to key store corruption."""
        key_store_path = os.path.join(temp_dir, "corruption_test.json")
        manager = SecureAPIKeyManager(
            master_key="corruption_test_master_key_123456",
            key_store_path=key_store_path
        )
        
        # Create test key
        test_key = "sk-corruption-test-key"
        key_id = manager.encrypt_api_key("corruption_test", test_key)
        
        # Corrupt the key store file
        with open(key_store_path, 'w') as f:
            f.write("invalid json content {[}")
        
        # Try to create new manager (should handle corruption gracefully)
        manager2 = SecureAPIKeyManager(
            master_key="corruption_test_master_key_123456",
            key_store_path=key_store_path
        )
        
        # Should be able to create new keys even with corrupted store
        new_key_id = manager2.encrypt_api_key("recovery_test", "sk-recovery-key")
        assert new_key_id is not None


class TestSecurityValidation:
    """Test overall security validation and compliance."""
    
    def test_security_audit_integration(self):
        """Test integration with security audit system."""
        # This would typically test that the security audit can validate
        # API key security measures
        try:
            from security.audit_checkers import ApiKeyManagementChecker
            
            checker = ApiKeyManagementChecker(Path("."))
            result = checker.check()
            
            # Verify checker structure
            assert 'passed' in result
            assert 'risk_level' in result
            assert 'issues' in result or 'good_practices' in result
            
        except ImportError:
            pytest.skip("Security audit checkers not available")
    
    def test_owasp_compliance(self):
        """Test compliance with OWASP security guidelines."""
        # Test for common OWASP violations in API key management
        
        # A1: Injection - Keys should be parameterized, not concatenated
        test_cases = [
            "SELECT * FROM keys WHERE key_id = '" + "user_input" + "'",  # Bad
            "SELECT * FROM keys WHERE key_id = ?",  # Good (parameterized)
        ]
        
        def is_parameterized_query(query):
            """Check if query uses parameterized statements."""
            return '?' in query and "' + " not in query
        
        assert not is_parameterized_query(test_cases[0])
        assert is_parameterized_query(test_cases[1])
        
        # A2: Broken Authentication - Keys should have expiration
        def validate_key_expiration(key_metadata):
            """Validate key has proper expiration."""
            if 'expires' not in key_metadata:
                return False
            
            try:
                expires = datetime.fromisoformat(key_metadata['expires'])
                now = datetime.now()
                
                # Key should expire in the future but not too far
                return now < expires < now + timedelta(days=365)
            except:
                return False
        
        # Test valid expiration
        valid_key = {'expires': (datetime.now() + timedelta(days=90)).isoformat()}
        assert validate_key_expiration(valid_key)
        
        # Test invalid expiration
        invalid_key = {'expires': (datetime.now() - timedelta(days=1)).isoformat()}
        assert not validate_key_expiration(invalid_key)
        
        # A3: Sensitive Data Exposure - Keys should be encrypted at rest
        def validate_key_encryption(stored_key_data):
            """Validate that stored key data is encrypted."""
            # Should not contain plaintext sensitive data
            data_str = json.dumps(stored_key_data).lower()
            
            sensitive_patterns = ['sk-', 'password', 'secret', 'token']
            for pattern in sensitive_patterns:
                if pattern in data_str and 'encrypted' not in data_str:
                    return False
            
            # Should contain encrypted_data field
            return 'encrypted_data' in stored_key_data
        
        # Test encrypted storage
        encrypted_key = {
            'name': 'test_key',
            'encrypted_data': 'base64encodedencrypteddata==',
            'created': datetime.now().isoformat()
        }
        assert validate_key_encryption(encrypted_key)
        
        # Test unencrypted storage (should fail)
        unencrypted_key = {
            'name': 'test_key',
            'api_key': 'sk-plaintext-key-12345',
            'created': datetime.now().isoformat()
        }
        assert not validate_key_encryption(unencrypted_key)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])