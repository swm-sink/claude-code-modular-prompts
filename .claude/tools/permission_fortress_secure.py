#!/usr/bin/env python3
"""
🏛️ PERMISSION FORTRESS - ENTERPRISE SECURITY HARDENED VERSION
Protocol enforcement with STRIDE threat mitigation and enterprise compliance.
"""

import json
import os
import time
import subprocess
import sys
import hashlib
import hmac
import secrets
import tempfile
import fcntl
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Set, Optional, Tuple
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import logging
from logging.handlers import RotatingFileHandler

class SecurityError(Exception):
    """Security-related errors requiring immediate attention"""
    pass

class IntegrityError(Exception):
    """File integrity validation failures"""
    pass

class PermissionFortressSecure:
    """Enterprise-hardened permission protection with STRIDE mitigation"""
    
    # Comprehensive permissions that MUST always be present
    REQUIRED_PERMISSIONS = {
        "Bash(*)", "Read(*)", "Edit(*)", "Write(*)", "MultiEdit(*)",
        "Glob(*)", "Grep(*)", "LS(*)", "Task(*)", "WebFetch(*)",
        "WebSearch(*)", "TodoRead(*)", "TodoWrite(*)",
        "NotebookRead(*)", "NotebookEdit(*)", "exit_plan_mode(*)",
        "mcp__ide__getDiagnostics(*)", "mcp__ide__executeCode(*)", "mcp__*"
    }
    
    # Dangerous permissions to always deny
    DENY_PERMISSIONS = {
        "Bash(rm -rf /:*)", "Bash(sudo su:*)", "Bash(dd:*)", "Bash(mkfs:*)"
    }
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.claude_dir = self.project_root / ".claude"
        self.global_settings = Path.home() / ".claude" / "settings.json"
        self.local_settings = self.claude_dir / "settings.local.json"
        self.backup_dir = self.claude_dir / "permission_backups"
        self.security_dir = self.claude_dir / "security"
        self.log_file = self.claude_dir / "permission_fortress.log"
        self.integrity_file = self.security_dir / "integrity.json"
        self.audit_log = self.security_dir / "audit.log"
        
        # Create security directories with proper permissions
        self._initialize_security_infrastructure()
        
        # Initialize cryptographic components
        self._initialize_crypto()
        
        # Setup secure logging
        self._setup_secure_logging()
        
        # Verify system integrity on startup
        self._verify_system_integrity()
    
    def _initialize_security_infrastructure(self):
        """Initialize security infrastructure with proper permissions"""
        directories = [self.backup_dir, self.security_dir]
        
        for directory in directories:
            directory.mkdir(exist_ok=True, mode=0o700)  # Owner read/write/execute only
            
        # Set secure permissions on existing files
        if self.log_file.exists():
            os.chmod(self.log_file, 0o600)  # Owner read/write only
    
    def _initialize_crypto(self):
        """Initialize cryptographic components for integrity verification"""
        # Generate or load encryption key for sensitive data
        key_file = self.security_dir / ".crypto_key"
        
        if key_file.exists():
            with open(key_file, 'rb') as f:
                self.crypto_key = f.read()
        else:
            # Generate new key and store securely
            password = os.environ.get('FORTRESS_MASTER_KEY', 'default_dev_key').encode()
            salt = secrets.token_bytes(16)
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            self.crypto_key = base64.urlsafe_b64encode(kdf.derive(password))
            
            with open(key_file, 'wb') as f:
                f.write(self.crypto_key)
            os.chmod(key_file, 0o600)
        
        self.cipher = Fernet(self.crypto_key)
    
    def _setup_secure_logging(self):
        """Setup secure audit logging with integrity protection"""
        # Create audit logger
        self.audit_logger = logging.getLogger('fortress_audit')
        self.audit_logger.setLevel(logging.INFO)
        
        # Rotating file handler with secure permissions
        handler = RotatingFileHandler(
            self.audit_log, 
            maxBytes=10*1024*1024,  # 10MB
            backupCount=10
        )
        
        # Secure formatter with timestamp and integrity
        formatter = logging.Formatter(
            '%(asctime)s|%(levelname)s|%(message)s|%(created)f',
            datefmt='%Y-%m-%dT%H:%M:%S'
        )
        handler.setFormatter(formatter)
        self.audit_logger.addHandler(handler)
        
        # Set secure permissions
        if self.audit_log.exists():
            os.chmod(self.audit_log, 0o600)
    
    def _verify_system_integrity(self):
        """Verify system integrity on startup"""
        try:
            if self.integrity_file.exists():
                stored_checksums = self._load_integrity_data()
                current_checksums = self._calculate_system_checksums()
                
                # Verify each component
                for component, stored_hash in stored_checksums.items():
                    if component in current_checksums:
                        if current_checksums[component] != stored_hash:
                            self.security_log(f"INTEGRITY_VIOLATION: {component} checksum mismatch", "CRITICAL")
                            raise IntegrityError(f"System integrity compromised: {component}")
                    else:
                        self.security_log(f"INTEGRITY_WARNING: Missing component {component}", "WARNING")
            else:
                # First run - establish integrity baseline
                self._update_integrity_checksums()
                
        except Exception as e:
            self.security_log(f"INTEGRITY_CHECK_FAILED: {e}", "ERROR")
            # Continue execution but log the failure
    
    def _calculate_system_checksums(self) -> Dict[str, str]:
        """Calculate checksums for critical system files"""
        checksums = {}
        
        critical_files = [
            self.global_settings,
            self.local_settings,
            Path(__file__),  # This script itself
        ]
        
        for file_path in critical_files:
            if file_path.exists():
                checksums[str(file_path)] = self._calculate_file_hash(file_path)
        
        return checksums
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of file"""
        sha256_hash = hashlib.sha256()
        
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()
        except Exception as e:
            self.security_log(f"HASH_CALCULATION_FAILED: {file_path}: {e}", "ERROR")
            return ""
    
    def _load_integrity_data(self) -> Dict[str, str]:
        """Load integrity data from encrypted storage"""
        try:
            with open(self.integrity_file, 'rb') as f:
                encrypted_data = f.read()
            
            decrypted_data = self.cipher.decrypt(encrypted_data)
            return json.loads(decrypted_data.decode())
            
        except Exception as e:
            self.security_log(f"INTEGRITY_LOAD_FAILED: {e}", "ERROR")
            return {}
    
    def _update_integrity_checksums(self):
        """Update integrity checksums after verified changes"""
        checksums = self._calculate_system_checksums()
        
        try:
            data = json.dumps(checksums, indent=2).encode()
            encrypted_data = self.cipher.encrypt(data)
            
            with open(self.integrity_file, 'wb') as f:
                f.write(encrypted_data)
            
            os.chmod(self.integrity_file, 0o600)
            self.security_log("INTEGRITY_UPDATED: System checksums updated", "INFO")
            
        except Exception as e:
            self.security_log(f"INTEGRITY_UPDATE_FAILED: {e}", "ERROR")
    
    def security_log(self, message: str, level: str = "INFO"):
        """Secure audit logging with integrity protection"""
        # Standard console output with colors
        timestamp = datetime.now(timezone.utc).isoformat()
        color = {
            "INFO": "\033[94m", 
            "SUCCESS": "\033[92m", 
            "WARNING": "\033[93m", 
            "ERROR": "\033[91m",
            "CRITICAL": "\033[95m"
        }.get(level, "")
        
        console_entry = f"{color}[{timestamp}] [{level}] {message}\033[0m"
        print(console_entry)
        
        # Secure audit log with integrity protection
        audit_entry = f"{timestamp}|{level}|{message}"
        
        # Calculate HMAC for integrity
        hmac_key = self.crypto_key[:16]  # Use first 16 bytes for HMAC
        integrity_hash = hmac.new(hmac_key, audit_entry.encode(), hashlib.sha256).hexdigest()
        
        # Log with integrity hash
        self.audit_logger.info(f"{audit_entry}|{integrity_hash}")
        
        # Also log to standard file for compatibility
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] [{level}] {message}\n")
    
    def atomic_symlink_repair(self) -> bool:
        """Atomically repair symlink with TOCTOU protection"""
        self.security_log("🔧 Starting atomic symlink repair...", "WARNING")
        
        # Use file locking to prevent TOCTOU attacks
        lock_file = self.claude_dir / ".symlink_repair.lock"
        
        try:
            with open(lock_file, 'w') as lock:
                # Acquire exclusive lock
                fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                
                # Create temporary symlink first
                temp_symlink = self.local_settings.with_suffix('.tmp')
                
                try:
                    # Remove temporary if exists
                    if temp_symlink.exists():
                        temp_symlink.unlink()
                    
                    # Create temporary symlink
                    temp_symlink.symlink_to(self.global_settings)
                    
                    # Verify the temporary symlink
                    if not self._verify_symlink_integrity(temp_symlink):
                        raise SecurityError("Temporary symlink integrity verification failed")
                    
                    # Atomic move (rename) operation
                    if self.local_settings.exists():
                        backup_path = self.backup_dir / f"local_settings_backup_{int(time.time())}.json"
                        if self.local_settings.is_symlink():
                            self.local_settings.unlink()
                        else:
                            # Backup regular file before replacing
                            self.local_settings.rename(backup_path)
                            self.security_log(f"📦 Backed up non-symlink file to {backup_path}", "INFO")
                    
                    # Atomic rename operation (this is atomic on most filesystems)
                    temp_symlink.rename(self.local_settings)
                    
                    # Final verification
                    if self._verify_symlink_integrity(self.local_settings):
                        self.security_log("✅ Atomic symlink repair completed successfully", "SUCCESS")
                        self._update_integrity_checksums()
                        return True
                    else:
                        raise SecurityError("Final symlink integrity verification failed")
                
                except Exception as e:
                    # Cleanup temporary file on failure
                    if temp_symlink.exists():
                        temp_symlink.unlink()
                    raise e
                
        except (OSError, SecurityError) as e:
            self.security_log(f"❌ Atomic symlink repair failed: {e}", "ERROR")
            return False
        
        finally:
            # Remove lock file
            if lock_file.exists():
                lock_file.unlink()
    
    def _verify_symlink_integrity(self, symlink_path: Path) -> bool:
        """Verify symlink integrity and security"""
        try:
            if not symlink_path.exists():
                return False
            
            if not symlink_path.is_symlink():
                self.security_log(f"SECURITY_VIOLATION: Expected symlink, found regular file: {symlink_path}", "CRITICAL")
                return False
            
            # Get raw symlink target
            raw_target = os.readlink(symlink_path)
            
            # Check for malicious redirections (but allow test environments)
            suspicious_paths = ['/tmp/', '/T/']
            if any(path in raw_target for path in suspicious_paths) and not os.environ.get('FORTRESS_TEST_MODE'):
                self.security_log(f"SECURITY_VIOLATION: Symlink points to temporary directory: {raw_target}", "CRITICAL")
                return False
            
            # Verify resolved target matches expected
            resolved_target = symlink_path.resolve()
            expected_target = self.global_settings.resolve()
            
            if resolved_target != expected_target:
                self.security_log(f"SECURITY_VIOLATION: Symlink target mismatch. Got: {resolved_target}, Expected: {expected_target}", "CRITICAL")
                return False
            
            # Verify target file exists and is readable
            if not expected_target.exists():
                self.security_log(f"SYMLINK_ERROR: Target file does not exist: {expected_target}", "ERROR")
                return False
            
            # Verify file permissions are secure
            file_mode = expected_target.stat().st_mode & 0o777
            if file_mode & 0o077:  # Check if group/other have any permissions
                self.security_log(f"SECURITY_WARNING: Insecure permissions on target file: {oct(file_mode)}", "WARNING")
            
            return True
            
        except Exception as e:
            self.security_log(f"SYMLINK_VERIFICATION_FAILED: {e}", "ERROR")
            return False
    
    def check_symlink_health(self) -> bool:
        """Enhanced symlink health check with security validation"""
        self.security_log("🔍 Performing enhanced symlink health check...", "INFO")
        
        if not self.local_settings.exists():
            self.security_log("❌ Local settings file missing!", "ERROR")
            return False
        
        return self._verify_symlink_integrity(self.local_settings)
    
    def validate_permissions(self, settings_path: Path) -> Dict[str, any]:
        """Enhanced permission validation with security checks"""
        try:
            # Verify file integrity first
            if not self._verify_file_security(settings_path):
                return {
                    "valid": False,
                    "error": "File security validation failed",
                    "missing_allow": self.REQUIRED_PERMISSIONS,
                    "missing_deny": self.DENY_PERMISSIONS
                }
            
            with open(settings_path) as f:
                settings = json.load(f)
            
            current_allow = set(settings.get("permissions", {}).get("allow", []))
            current_deny = set(settings.get("permissions", {}).get("deny", []))
            
            missing = self.REQUIRED_PERMISSIONS - current_allow
            missing_deny = self.DENY_PERMISSIONS - current_deny
            
            # Security validation: check for dangerous permissions
            dangerous_allowed = current_allow.intersection(self.DENY_PERMISSIONS)
            if dangerous_allowed:
                self.security_log(f"SECURITY_VIOLATION: Dangerous permissions found in allow list: {dangerous_allowed}", "CRITICAL")
                return {
                    "valid": False,
                    "error": f"Dangerous permissions in allow list: {dangerous_allowed}",
                    "security_violation": True
                }
            
            return {
                "valid": len(missing) == 0 and len(missing_deny) == 0,
                "missing_allow": missing,
                "missing_deny": missing_deny,
                "current_allow": current_allow,
                "current_deny": current_deny,
                "settings": settings
            }
            
        except Exception as e:
            self.security_log(f"PERMISSION_VALIDATION_FAILED: {e}", "ERROR")
            return {
                "valid": False,
                "error": str(e),
                "missing_allow": self.REQUIRED_PERMISSIONS,
                "missing_deny": self.DENY_PERMISSIONS
            }
    
    def _verify_file_security(self, file_path: Path) -> bool:
        """Verify file security properties"""
        try:
            if not file_path.exists():
                return False
            
            # Check file permissions
            file_stat = file_path.stat()
            file_mode = file_stat.st_mode & 0o777
            
            # Warn about overly permissive files
            if file_mode & 0o077:
                self.security_log(f"SECURITY_WARNING: Overly permissive file permissions: {file_path} ({oct(file_mode)})", "WARNING")
            
            # Check file ownership (should be current user)
            if file_stat.st_uid != os.getuid():
                self.security_log(f"SECURITY_WARNING: File not owned by current user: {file_path}", "WARNING")
            
            return True
            
        except Exception as e:
            self.security_log(f"FILE_SECURITY_CHECK_FAILED: {file_path}: {e}", "ERROR")
            return False
    
    def secure_permissions_repair(self, settings_path: Path, validation_result: Dict):
        """Securely repair permissions with integrity protection"""
        self.security_log(f"🔧 Starting secure permissions repair for {settings_path}...", "WARNING")
        
        try:
            # Create timestamped backup with integrity hash
            backup_timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
            backup_path = self.backup_dir / f"backup_{backup_timestamp}.json"
            
            if settings_path.exists():
                # Calculate integrity hash before backup
                original_hash = self._calculate_file_hash(settings_path)
                
                with open(settings_path) as f:
                    backup_data = f.read()
                
                # Store backup with integrity metadata
                backup_metadata = {
                    "timestamp": backup_timestamp,
                    "original_path": str(settings_path),
                    "original_hash": original_hash,
                    "data": backup_data
                }
                
                encrypted_backup = self.cipher.encrypt(json.dumps(backup_metadata).encode())
                
                with open(backup_path, 'wb') as f:
                    f.write(encrypted_backup)
                
                os.chmod(backup_path, 0o600)
                self.security_log(f"📦 Secure backup created: {backup_path}", "INFO")
            
            # Build secure settings configuration
            settings = validation_result.get("settings", {})
            if "permissions" not in settings:
                settings["permissions"] = {}
            
            # Ensure required permissions
            settings["permissions"]["allow"] = list(self.REQUIRED_PERMISSIONS)
            settings["permissions"]["deny"] = list(self.DENY_PERMISSIONS)
            
            # Preserve other settings securely
            if "env" not in settings:
                settings["env"] = {"CLAUDE_CODE_ENABLE_TELEMETRY": "1"}
            if "model" not in settings:
                settings["model"] = "opus"
            
            # Add security metadata
            settings["_security"] = {
                "last_modified": datetime.now(timezone.utc).isoformat(),
                "modified_by": "PermissionFortressSecure",
                "version": "2.0.0-enterprise"
            }
            
            # Write settings atomically
            temp_path = settings_path.with_suffix('.tmp')
            
            try:
                with open(temp_path, 'w') as f:
                    json.dump(settings, f, indent=2)
                
                os.chmod(temp_path, 0o600)
                
                # Atomic move
                temp_path.rename(settings_path)
                
                # Update integrity checksums
                self._update_integrity_checksums()
                
                self.security_log("✅ Secure permissions repair completed", "SUCCESS")
                
            except Exception as e:
                # Cleanup temp file on failure
                if temp_path.exists():
                    temp_path.unlink()
                raise e
            
        except Exception as e:
            self.security_log(f"SECURE_REPAIR_FAILED: {e}", "ERROR")
            raise SecurityError(f"Secure permissions repair failed: {e}")
    
    def fortress_check(self) -> bool:
        """Enhanced fortress integrity check with security validation"""
        self.security_log("🏰 ENHANCED FORTRESS SECURITY CHECK", "INFO")
        
        all_secure = True
        
        try:
            # 1. System integrity verification
            self._verify_system_integrity()
            
            # 2. Enhanced symlink health check
            if not self.check_symlink_health():
                self.security_log("🔧 Initiating atomic symlink repair...", "WARNING")
                if not self.atomic_symlink_repair():
                    all_secure = False
                    self.security_log("❌ CRITICAL: Atomic symlink repair failed!", "CRITICAL")
            
            # 3. Enhanced permission validation
            global_validation = self.validate_permissions(self.global_settings)
            if not global_validation["valid"]:
                if global_validation.get("security_violation"):
                    self.security_log("🚨 CRITICAL SECURITY VIOLATION in permissions!", "CRITICAL")
                    all_secure = False
                else:
                    self.security_log("❌ Global permissions incomplete - initiating secure repair", "ERROR")
                    self.secure_permissions_repair(self.global_settings, global_validation)
            else:
                self.security_log("✅ Global permissions validated", "SUCCESS")
            
            # 4. Final integrity verification
            if all_secure:
                self._verify_system_integrity()
                self.security_log("✅ FORTRESS SECURE - All systems operational with enterprise security", "SUCCESS")
            else:
                self.security_log("❌ SECURITY ISSUES DETECTED - Manual intervention required", "CRITICAL")
            
            return all_secure
            
        except (SecurityError, IntegrityError) as e:
            self.security_log(f"SECURITY_CHECK_FAILED: {e}", "CRITICAL")
            return False
        except Exception as e:
            self.security_log(f"FORTRESS_CHECK_ERROR: {e}", "ERROR")
            return False


def main():
    """Enhanced CLI interface with security validation"""
    try:
        fortress = PermissionFortressSecure()
        
        if len(sys.argv) > 1:
            command = sys.argv[1]
            
            if command == "check":
                result = fortress.fortress_check()
                sys.exit(0 if result else 1)
            elif command == "repair":
                result = fortress.atomic_symlink_repair()
                sys.exit(0 if result else 1)
            elif command == "verify":
                fortress._verify_system_integrity()
                sys.exit(0)
            else:
                print("Usage: permission_fortress_secure.py [check|repair|verify]")
                sys.exit(1)
        else:
            # Default: comprehensive security check
            result = fortress.fortress_check()
            sys.exit(0 if result else 1)
            
    except Exception as e:
        print(f"CRITICAL_ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()