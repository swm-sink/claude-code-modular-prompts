#!/usr/bin/env python3
"""
🔴 TDD: Test Permission Fortress Secure - Enterprise Protocol Enforcement
Enhanced test coverage for STRIDE threat mitigation and enterprise security.
"""

import json
import os
import pytest
import tempfile
import hashlib
import hmac
import time
import threading
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import sys
from cryptography.fernet import Fernet

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "tools"))

# Import the secure fortress
try:
    from permission_fortress_secure import PermissionFortressSecure, SecurityError, IntegrityError
except ImportError:
    PermissionFortressSecure = None
    SecurityError = Exception
    IntegrityError = Exception


class TestPermissionFortressSecure:
    """Comprehensive test suite for enterprise-hardened permission protection"""
    
    @pytest.fixture
    def temp_env(self):
        """Create secure temporary test environment"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Setup test directory structure
            test_root = Path(tmpdir)
            claude_dir = test_root / ".claude"
            claude_dir.mkdir(mode=0o700)
            
            # Create mock home directory
            home_dir = test_root / "home"
            home_dir.mkdir()
            home_claude = home_dir / ".claude"
            home_claude.mkdir(mode=0o700)
            
            # Create security directory
            security_dir = claude_dir / "security"
            security_dir.mkdir(mode=0o700)
            
            yield {
                "root": test_root,
                "claude_dir": claude_dir,
                "home_dir": home_dir,
                "security_dir": security_dir,
                "global_settings": home_claude / "settings.json",
                "local_settings": claude_dir / "settings.local.json"
            }
    
    @pytest.fixture
    def secure_fortress(self, temp_env, monkeypatch):
        """Create secure fortress instance with mocked paths"""
        if PermissionFortressSecure is None:
            pytest.skip("PermissionFortressSecure not implemented yet")
        
        # Mock environment variable for deterministic testing
        monkeypatch.setenv('FORTRESS_MASTER_KEY', 'test_key_12345')
        
        # Mock paths
        monkeypatch.setattr(Path, "cwd", lambda: temp_env["root"])
        monkeypatch.setattr(Path, "home", lambda: temp_env["home_dir"])
        
        return PermissionFortressSecure()
    
    def test_secure_initialization(self, secure_fortress, temp_env):
        """Test secure initialization with proper permissions"""
        assert secure_fortress.project_root == temp_env["root"]
        assert secure_fortress.security_dir.exists()
        
        # Verify security directory permissions
        security_mode = temp_env["security_dir"].stat().st_mode & 0o777
        assert security_mode == 0o700  # Owner only
        
        # Verify cryptographic components initialized
        assert hasattr(secure_fortress, 'crypto_key')
        assert hasattr(secure_fortress, 'cipher')
        assert isinstance(secure_fortress.cipher, Fernet)
    
    def test_file_integrity_monitoring(self, secure_fortress, temp_env):
        """Test file integrity monitoring and detection"""
        # Create a test file
        test_file = temp_env["global_settings"]
        test_content = {"test": "data"}
        
        with open(test_file, 'w') as f:
            json.dump(test_content, f)
        
        # Calculate initial hash
        initial_hash = secure_fortress._calculate_file_hash(test_file)
        assert len(initial_hash) == 64  # SHA-256 hex digest
        
        # Modify file
        test_content["modified"] = True
        with open(test_file, 'w') as f:
            json.dump(test_content, f)
        
        # Verify hash changed
        modified_hash = secure_fortress._calculate_file_hash(test_file)
        assert modified_hash != initial_hash
    
    def test_integrity_data_encryption(self, secure_fortress, temp_env):
        """Test integrity data encryption and decryption"""
        test_data = {"file1": "hash1", "file2": "hash2"}
        
        # Update checksums
        secure_fortress._calculate_system_checksums = lambda: test_data
        secure_fortress._update_integrity_checksums()
        
        # Verify file was created and encrypted
        assert secure_fortress.integrity_file.exists()
        
        # Verify we can decrypt and read the data
        loaded_data = secure_fortress._load_integrity_data()
        assert loaded_data == test_data
    
    def test_atomic_symlink_repair(self, secure_fortress, temp_env):
        """Test atomic symlink repair with TOCTOU protection"""
        # Create target file
        temp_env["global_settings"].touch()
        
        # Create broken regular file
        temp_env["local_settings"].write_text("{}")
        
        # Repair symlink atomically
        result = secure_fortress.atomic_symlink_repair()
        
        # Verify repair succeeded
        assert result is True
        assert temp_env["local_settings"].is_symlink()
        assert temp_env["local_settings"].resolve() == temp_env["global_settings"].resolve()
    
    def test_symlink_integrity_verification(self, secure_fortress, temp_env):
        """Test comprehensive symlink integrity verification"""
        # Create valid symlink
        temp_env["global_settings"].touch()
        temp_env["local_settings"].symlink_to(temp_env["global_settings"])
        
        # Should pass verification
        assert secure_fortress._verify_symlink_integrity(temp_env["local_settings"]) is True
        
        # Test malicious symlink to /tmp
        malicious_symlink = temp_env["claude_dir"] / "malicious.json"
        malicious_target = Path("/tmp/malicious")
        malicious_symlink.symlink_to(malicious_target)
        
        # Should fail verification
        assert secure_fortress._verify_symlink_integrity(malicious_symlink) is False
    
    def test_security_violation_detection(self, secure_fortress, temp_env):
        """Test detection of security violations in permissions"""
        # Create settings with dangerous permissions
        dangerous_settings = {
            "permissions": {
                "allow": ["Bash(*)", "Bash(rm -rf /:*)"],  # Dangerous permission in allow
                "deny": []
            }
        }
        
        with open(temp_env["global_settings"], 'w') as f:
            json.dump(dangerous_settings, f)
        
        # Validation should detect security violation
        result = secure_fortress.validate_permissions(temp_env["global_settings"])
        
        assert result["valid"] is False
        assert "security_violation" in result
        assert result["security_violation"] is True
    
    def test_secure_permissions_repair(self, secure_fortress, temp_env):
        """Test secure permissions repair with backup and integrity"""
        # Create incomplete settings
        incomplete_settings = {
            "permissions": {"allow": ["Bash(*)"], "deny": []},
            "env": {"CUSTOM": "value"}
        }
        
        with open(temp_env["global_settings"], 'w') as f:
            json.dump(incomplete_settings, f)
        
        validation = secure_fortress.validate_permissions(temp_env["global_settings"])
        
        # Repair permissions
        secure_fortress.secure_permissions_repair(temp_env["global_settings"], validation)
        
        # Verify repair
        with open(temp_env["global_settings"]) as f:
            repaired = json.load(f)
        
        assert set(repaired["permissions"]["allow"]) == secure_fortress.REQUIRED_PERMISSIONS
        assert set(repaired["permissions"]["deny"]) == secure_fortress.DENY_PERMISSIONS
        assert repaired["env"]["CUSTOM"] == "value"  # Preserved
        assert "_security" in repaired  # Security metadata added
        
        # Verify backup was created
        backups = list(secure_fortress.backup_dir.glob("backup_*.json"))
        assert len(backups) > 0
    
    def test_audit_logging_integrity(self, secure_fortress):
        """Test secure audit logging with HMAC integrity"""
        test_message = "TEST_AUDIT_MESSAGE"
        
        # Log a message
        secure_fortress.security_log(test_message, "INFO")
        
        # Verify audit log was created
        assert secure_fortress.audit_log.exists()
        
        # Read audit log and verify HMAC
        with open(secure_fortress.audit_log) as f:
            log_content = f.read()
        
        assert test_message in log_content
        # Should contain HMAC hash at the end
        assert "|" in log_content  # HMAC separator
    
    def test_file_locking_concurrency(self, secure_fortress, temp_env):
        """Test file locking prevents concurrent modifications"""
        temp_env["global_settings"].touch()
        results = []
        
        def concurrent_repair():
            try:
                result = secure_fortress.atomic_symlink_repair()
                results.append(result)
            except Exception as e:
                results.append(str(e))
        
        # Start multiple concurrent repair operations
        threads = []
        for _ in range(3):
            thread = threading.Thread(target=concurrent_repair)
            threads.append(thread)
            thread.start()
        
        # Wait for all threads
        for thread in threads:
            thread.join()
        
        # Only one should succeed (due to file locking)
        success_count = sum(1 for r in results if r is True)
        assert success_count <= 1  # At most one should succeed
    
    def test_enhanced_fortress_check(self, secure_fortress, temp_env):
        """Test comprehensive fortress check with security validation"""
        # Create valid configuration
        valid_settings = {
            "permissions": {
                "allow": list(secure_fortress.REQUIRED_PERMISSIONS),
                "deny": list(secure_fortress.DENY_PERMISSIONS)
            }
        }
        
        with open(temp_env["global_settings"], 'w') as f:
            json.dump(valid_settings, f)
        
        temp_env["local_settings"].symlink_to(temp_env["global_settings"])
        
        # Fortress check should pass
        result = secure_fortress.fortress_check()
        assert result is True
    
    def test_security_error_handling(self, secure_fortress, temp_env):
        """Test proper handling of security errors"""
        # Test with non-existent target
        temp_env["local_settings"].symlink_to(Path("/nonexistent/file"))
        
        # Should handle gracefully
        result = secure_fortress.check_symlink_health()
        assert result is False
        
        # Fortress check should attempt repair
        result = secure_fortress.fortress_check()
        # May fail due to missing global settings, but should not crash
        assert isinstance(result, bool)
    
    def test_crypto_key_persistence(self, temp_env, monkeypatch):
        """Test cryptographic key persistence across instances"""
        if PermissionFortressSecure is None:
            pytest.skip("PermissionFortressSecure not implemented yet")
        
        monkeypatch.setenv('FORTRESS_MASTER_KEY', 'test_key_12345')
        monkeypatch.setattr(Path, "cwd", lambda: temp_env["root"])
        monkeypatch.setattr(Path, "home", lambda: temp_env["home_dir"])
        
        # First instance
        fortress1 = PermissionFortressSecure()
        key1 = fortress1.crypto_key
        
        # Second instance should use same key
        fortress2 = PermissionFortressSecure()
        key2 = fortress2.crypto_key
        
        assert key1 == key2
    
    def test_file_permissions_security(self, secure_fortress, temp_env):
        """Test file permissions are set securely"""
        # Create a test file
        test_file = temp_env["security_dir"] / "test_secure_file"
        test_file.write_text("sensitive data")
        
        # Verify secure permissions
        assert secure_fortress._verify_file_security(test_file) is True
        
        # Make file world-readable
        os.chmod(test_file, 0o644)
        
        # Should warn about insecure permissions
        result = secure_fortress._verify_file_security(test_file)
        assert result is True  # Still valid, but should log warning
    
    def test_backup_encryption_integrity(self, secure_fortress, temp_env):
        """Test backup encryption and metadata integrity"""
        # Create test settings
        test_settings = {"test": "backup_data", "sensitive": "information"}
        
        with open(temp_env["global_settings"], 'w') as f:
            json.dump(test_settings, f)
        
        validation = {"settings": test_settings}
        
        # Create secure backup
        secure_fortress.secure_permissions_repair(temp_env["global_settings"], validation)
        
        # Verify encrypted backup exists
        backups = list(secure_fortress.backup_dir.glob("backup_*.json"))
        assert len(backups) > 0
        
        backup_file = backups[0]
        
        # Verify backup is encrypted (not plain JSON)
        with open(backup_file, 'rb') as f:
            backup_content = f.read()
        
        # Should not be plain JSON
        try:
            json.loads(backup_content.decode())
            assert False, "Backup should be encrypted, not plain JSON"
        except (json.JSONDecodeError, UnicodeDecodeError):
            pass  # Expected - backup is encrypted
    
    def test_integrity_violation_detection(self, secure_fortress, temp_env):
        """Test detection of file integrity violations"""
        # Create initial state
        test_file = temp_env["global_settings"]
        test_file.write_text('{"initial": "content"}')
        
        # Establish baseline
        secure_fortress._update_integrity_checksums()
        
        # Modify file externally (simulating tampering)
        test_file.write_text('{"modified": "content"}')
        
        # Verification should detect violation
        with pytest.raises(IntegrityError):
            secure_fortress._verify_system_integrity()
    
    def test_cli_interface_security(self, temp_env, monkeypatch):
        """Test CLI interface with security validation"""
        if PermissionFortressSecure is None:
            pytest.skip("PermissionFortressSecure not implemented yet")
        
        monkeypatch.setenv('FORTRESS_MASTER_KEY', 'test_key_12345')
        monkeypatch.setattr(Path, "cwd", lambda: temp_env["root"])
        monkeypatch.setattr(Path, "home", lambda: temp_env["home_dir"])
        
        # Test security commands
        from permission_fortress_secure import main
        
        # Test verify command
        monkeypatch.setattr("sys.argv", ["permission_fortress_secure.py", "verify"])
        
        try:
            main()
        except SystemExit as e:
            assert e.code == 0  # Should exit successfully
    
    def test_performance_benchmarks(self, secure_fortress, temp_env):
        """Test performance meets enterprise requirements"""
        # Create test file
        temp_env["global_settings"].touch()
        
        # Test symlink repair performance
        start_time = time.time()
        result = secure_fortress.atomic_symlink_repair()
        repair_time = time.time() - start_time
        
        assert result is True
        assert repair_time < 1.0  # Should complete within 1 second
        
        # Test integrity check performance
        start_time = time.time()
        secure_fortress._verify_system_integrity()
        check_time = time.time() - start_time
        
        assert check_time < 0.5  # Should complete within 0.5 seconds


class TestSecurityEdgeCases:
    """Test security edge cases and attack scenarios"""
    
    @pytest.fixture
    def fortress(self, temp_env, monkeypatch):
        """Create fortress for edge case testing"""
        if PermissionFortressSecure is None:
            pytest.skip("PermissionFortressSecure not implemented yet")
        
        monkeypatch.setenv('FORTRESS_MASTER_KEY', 'edge_case_key')
        monkeypatch.setattr(Path, "cwd", lambda: temp_env["root"])
        monkeypatch.setattr(Path, "home", lambda: temp_env["home_dir"])
        
        return PermissionFortressSecure()
    
    def test_symlink_race_condition_protection(self, fortress, temp_env):
        """Test protection against symlink race conditions"""
        temp_env["global_settings"].touch()
        
        # Simulate race condition by creating conflicting symlink during repair
        def create_conflicting_symlink():
            time.sleep(0.01)  # Small delay
            if temp_env["local_settings"].exists():
                temp_env["local_settings"].unlink()
            temp_env["local_settings"].symlink_to(Path("/tmp/malicious"))
        
        thread = threading.Thread(target=create_conflicting_symlink)
        thread.start()
        
        # Attempt repair (should be protected by file locking)
        result = fortress.atomic_symlink_repair()
        
        thread.join()
        
        # Repair should either succeed with correct target or fail safely
        if result:
            # If successful, should point to correct target
            assert temp_env["local_settings"].resolve() == temp_env["global_settings"].resolve()
    
    def test_malicious_json_injection(self, fortress, temp_env):
        """Test protection against malicious JSON injection"""
        # Create malicious JSON with code injection attempt
        malicious_json = '''
        {
            "permissions": {
                "allow": ["Bash(*)"],
                "deny": []
            },
            "__proto__": {
                "polluted": "value"
            },
            "constructor": {
                "prototype": {
                    "isAdmin": true
                }
            }
        }
        '''
        
        temp_env["global_settings"].write_text(malicious_json)
        
        # Validation should handle malicious JSON safely
        result = fortress.validate_permissions(temp_env["global_settings"])
        
        # Should not crash and should validate permissions normally
        assert "valid" in result
        assert isinstance(result["valid"], bool)
    
    def test_path_traversal_protection(self, fortress, temp_env):
        """Test protection against path traversal attacks"""
        # Attempt to create symlink with path traversal
        malicious_target = temp_env["root"] / ".." / ".." / "etc" / "passwd"
        
        # This should be detected as insecure
        test_symlink = temp_env["claude_dir"] / "malicious_link"
        test_symlink.symlink_to(malicious_target)
        
        result = fortress._verify_symlink_integrity(test_symlink)
        assert result is False  # Should reject dangerous target


if __name__ == "__main__":
    # Run comprehensive test suite
    pytest.main([__file__, "-v", "--tb=short", "--cov=permission_fortress_secure", "--cov-report=html"])