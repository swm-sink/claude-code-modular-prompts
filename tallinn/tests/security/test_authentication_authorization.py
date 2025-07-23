#!/usr/bin/env python3
"""
Authentication and Authorization Security Tests

Tests for:
- Authentication mechanisms
- Authorization controls
- Session management
- Access control enforcement
- Multi-factor authentication
- Role-based access control (RBAC)
"""

import pytest
import tempfile
import os
import sys
import json
import time
import hashlib
import hmac
from pathlib import Path
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


class TestAuthenticationMechanisms:
    """Test authentication mechanism security."""
    
    def test_password_hashing_security(self):
        """Test that passwords are securely hashed."""
        def secure_hash_password(password, salt=None):
            """Securely hash password with salt."""
            import hashlib
            import secrets
            
            if salt is None:
                salt = secrets.token_hex(16)
            
            # Use PBKDF2 with high iteration count
            iterations = 100000
            hash_value = hashlib.pbkdf2_hmac('sha256', 
                                           password.encode('utf-8'), 
                                           salt.encode('utf-8'), 
                                           iterations)
            
            return {
                'hash': hash_value.hex(),
                'salt': salt,
                'iterations': iterations,
                'algorithm': 'pbkdf2_sha256'
            }
        
        def verify_password(password, stored_hash_data):
            """Verify password against stored hash."""
            test_hash = secure_hash_password(password, stored_hash_data['salt'])
            return test_hash['hash'] == stored_hash_data['hash']
        
        # Test password hashing
        password = "test_password_123"
        hash_data = secure_hash_password(password)
        
        # Verify hash properties
        assert len(hash_data['hash']) == 64  # SHA256 hex length
        assert len(hash_data['salt']) == 32  # 16 bytes hex encoded
        assert hash_data['iterations'] >= 100000
        assert hash_data['algorithm'] == 'pbkdf2_sha256'
        
        # Verify password verification works
        assert verify_password(password, hash_data)
        assert not verify_password("wrong_password", hash_data)
        
        # Verify same password produces different hashes (different salts)
        hash_data2 = secure_hash_password(password)
        assert hash_data['hash'] != hash_data2['hash']
        assert hash_data['salt'] != hash_data2['salt']
    
    def test_weak_password_rejection(self):
        """Test rejection of weak passwords."""
        def validate_password_strength(password):
            """Validate password meets security requirements."""
            if len(password) < 8:
                return False, "Password too short"
            
            if not any(c.isupper() for c in password):
                return False, "Password must contain uppercase letter"
            
            if not any(c.islower() for c in password):
                return False, "Password must contain lowercase letter"
            
            if not any(c.isdigit() for c in password):
                return False, "Password must contain digit"
            
            if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
                return False, "Password must contain special character"
            
            # Check for common weak passwords
            common_weak = ['password', '123456', 'admin', 'qwerty', 'letmein']
            if password.lower() in common_weak:
                return False, "Password is too common"
            
            return True, "Password is strong"
        
        # Test weak passwords
        weak_passwords = [
            "123",                    # Too short
            "password",               # Common weak password
            "PASSWORD",               # No lowercase/digits/special
            "password123",            # No uppercase/special
            "Password",               # No digits/special
            "Password1",              # No special characters
        ]
        
        for weak_password in weak_passwords:
            valid, message = validate_password_strength(weak_password)
            assert not valid, f"Weak password accepted: {weak_password}"
        
        # Test strong passwords
        strong_passwords = [
            "MySecure123!",
            "Complex#Password2023",
            "S3cur3_P@ssw0rd",
            "Adm1n!str@t0r"
        ]
        
        for strong_password in strong_passwords:
            valid, message = validate_password_strength(strong_password)
            assert valid, f"Strong password rejected: {strong_password} - {message}"
    
    def test_authentication_timing_attack_prevention(self):
        """Test prevention of timing attacks in authentication."""
        def constant_time_compare(a, b):
            """Compare strings in constant time to prevent timing attacks."""
            import hmac
            return hmac.compare_digest(a, b)
        
        def authenticate_user(username, password, user_db):
            """Authenticate user with timing attack prevention."""
            import time
            import secrets
            
            # Always perform hash operation even if user doesn't exist
            # to prevent timing attacks
            if username in user_db:
                stored_hash = user_db[username]['password_hash']
                test_hash = hashlib.sha256(password.encode()).hexdigest()
                return constant_time_compare(stored_hash, test_hash)
            else:
                # Perform dummy hash to maintain constant timing
                dummy_hash = hashlib.sha256(password.encode()).hexdigest()
                dummy_stored = hashlib.sha256(secrets.token_bytes(32)).hexdigest()
                constant_time_compare(dummy_hash, dummy_stored)
                return False
        
        # Create test user database
        user_db = {
            'admin': {
                'password_hash': hashlib.sha256('correct_password'.encode()).hexdigest()
            }
        }
        
        # Test timing consistency
        times = []
        
        # Test with existing user, correct password
        start = time.time()
        result1 = authenticate_user('admin', 'correct_password', user_db)
        times.append(time.time() - start)
        assert result1 is True
        
        # Test with existing user, wrong password
        start = time.time()
        result2 = authenticate_user('admin', 'wrong_password', user_db)
        times.append(time.time() - start)
        assert result2 is False
        
        # Test with non-existing user
        start = time.time()
        result3 = authenticate_user('nonexistent', 'any_password', user_db)
        times.append(time.time() - start)
        assert result3 is False
        
        # Verify timing is reasonably consistent (within 50% variance)
        avg_time = sum(times) / len(times)
        for t in times:
            variance = abs(t - avg_time) / avg_time
            assert variance < 0.5, f"Timing attack vulnerability: {variance:.2%} variance"
    
    def test_brute_force_protection(self):
        """Test brute force attack protection."""
        class AuthenticationManager:
            def __init__(self):
                self.failed_attempts = {}
                self.lockout_time = 900  # 15 minutes
                self.max_attempts = 5
            
            def is_locked_out(self, username):
                """Check if user is locked out due to failed attempts."""
                if username not in self.failed_attempts:
                    return False
                
                attempts_data = self.failed_attempts[username]
                
                # Check if lockout period has expired
                if time.time() - attempts_data['last_attempt'] > self.lockout_time:
                    del self.failed_attempts[username]
                    return False
                
                return attempts_data['count'] >= self.max_attempts
            
            def record_failed_attempt(self, username):
                """Record a failed login attempt."""
                if username not in self.failed_attempts:
                    self.failed_attempts[username] = {'count': 0, 'last_attempt': 0}
                
                self.failed_attempts[username]['count'] += 1
                self.failed_attempts[username]['last_attempt'] = time.time()
            
            def reset_failed_attempts(self, username):
                """Reset failed attempts after successful login."""
                if username in self.failed_attempts:
                    del self.failed_attempts[username]
            
            def authenticate(self, username, password):
                """Authenticate user with brute force protection."""
                if self.is_locked_out(username):
                    return False, "Account locked due to too many failed attempts"
                
                # Simulate password check (simplified)
                if password == "correct_password":
                    self.reset_failed_attempts(username)
                    return True, "Authentication successful"
                else:
                    self.record_failed_attempt(username)
                    return False, "Invalid credentials"
        
        auth_manager = AuthenticationManager()
        
        # Test normal authentication
        success, msg = auth_manager.authenticate("user1", "correct_password")
        assert success
        
        # Test failed attempts leading to lockout
        for i in range(5):
            success, msg = auth_manager.authenticate("user2", "wrong_password")
            assert not success
            assert "Invalid credentials" in msg
        
        # Next attempt should be locked out
        success, msg = auth_manager.authenticate("user2", "wrong_password")
        assert not success
        assert "Account locked" in msg
        
        # Even correct password should be rejected when locked out
        success, msg = auth_manager.authenticate("user2", "correct_password")
        assert not success
        assert "Account locked" in msg


class TestSessionManagement:
    """Test session management security."""
    
    def test_secure_session_token_generation(self):
        """Test generation of secure session tokens."""
        def generate_session_token():
            """Generate cryptographically secure session token."""
            import secrets
            return secrets.token_urlsafe(32)
        
        # Generate multiple tokens
        tokens = [generate_session_token() for _ in range(100)]
        
        # Verify token properties
        for token in tokens:
            assert len(token) >= 32  # Sufficient length
            assert token.isascii()   # Valid ASCII characters
        
        # Verify tokens are unique
        assert len(set(tokens)) == len(tokens), "Session tokens are not unique"
        
        # Verify tokens are unpredictable (no common prefixes/suffixes)
        prefixes = [token[:4] for token in tokens[:10]]
        assert len(set(prefixes)) > 5, "Session tokens have predictable prefixes"
    
    def test_session_expiration(self):
        """Test session expiration mechanisms."""
        class SessionManager:
            def __init__(self):
                self.sessions = {}
                self.session_timeout = 3600  # 1 hour
            
            def create_session(self, user_id):
                """Create new session for user."""
                import secrets
                session_id = secrets.token_urlsafe(32)
                
                self.sessions[session_id] = {
                    'user_id': user_id,
                    'created': time.time(),
                    'last_activity': time.time(),
                    'active': True
                }
                
                return session_id
            
            def validate_session(self, session_id):
                """Validate session and update activity."""
                if session_id not in self.sessions:
                    return False, "Session does not exist"
                
                session = self.sessions[session_id]
                
                if not session['active']:
                    return False, "Session is inactive"
                
                # Check if session has expired
                if time.time() - session['last_activity'] > self.session_timeout:
                    session['active'] = False
                    return False, "Session has expired"
                
                # Update last activity
                session['last_activity'] = time.time()
                return True, session['user_id']
            
            def invalidate_session(self, session_id):
                """Invalidate session (logout)."""
                if session_id in self.sessions:
                    self.sessions[session_id]['active'] = False
                    return True
                return False
        
        session_manager = SessionManager()
        
        # Test session creation
        session_id = session_manager.create_session("user123")
        assert session_id is not None
        assert len(session_id) >= 32
        
        # Test valid session
        valid, user_id = session_manager.validate_session(session_id)
        assert valid
        assert user_id == "user123"
        
        # Test session invalidation
        success = session_manager.invalidate_session(session_id)
        assert success
        
        # Test invalid session after logout
        valid, msg = session_manager.validate_session(session_id)
        assert not valid
        assert "inactive" in msg
        
        # Test expired session
        new_session = session_manager.create_session("user456")
        session_manager.sessions[new_session]['last_activity'] = time.time() - 7200  # 2 hours ago
        
        valid, msg = session_manager.validate_session(new_session)
        assert not valid
        assert "expired" in msg
    
    def test_session_hijacking_prevention(self):
        """Test prevention of session hijacking."""
        class SecureSessionManager:
            def __init__(self):
                self.sessions = {}
            
            def create_session(self, user_id, user_agent, ip_address):
                """Create session with fingerprinting."""
                import secrets
                import hashlib
                
                session_id = secrets.token_urlsafe(32)
                
                # Create session fingerprint
                fingerprint_data = f"{user_agent}:{ip_address}"
                fingerprint = hashlib.sha256(fingerprint_data.encode()).hexdigest()
                
                self.sessions[session_id] = {
                    'user_id': user_id,
                    'created': time.time(),
                    'fingerprint': fingerprint,
                    'ip_address': ip_address,
                    'active': True
                }
                
                return session_id
            
            def validate_session(self, session_id, user_agent, ip_address):
                """Validate session with fingerprint checking."""
                if session_id not in self.sessions:
                    return False, "Invalid session"
                
                session = self.sessions[session_id]
                
                # Check session fingerprint
                fingerprint_data = f"{user_agent}:{ip_address}"
                current_fingerprint = hashlib.sha256(fingerprint_data.encode()).hexdigest()
                
                if current_fingerprint != session['fingerprint']:
                    # Potential session hijacking
                    session['active'] = False
                    return False, "Session security violation detected"
                
                return True, session['user_id']
        
        secure_session = SecureSessionManager()
        
        # Create session with specific user agent and IP
        session_id = secure_session.create_session(
            "user123", 
            "Mozilla/5.0 (Test Browser)", 
            "192.168.1.100"
        )
        
        # Test valid access with same fingerprint
        valid, user_id = secure_session.validate_session(
            session_id,
            "Mozilla/5.0 (Test Browser)",
            "192.168.1.100"
        )
        assert valid
        assert user_id == "user123"
        
        # Test session hijacking attempt (different IP)
        valid, msg = secure_session.validate_session(
            session_id,
            "Mozilla/5.0 (Test Browser)",
            "10.0.0.1"  # Different IP
        )
        assert not valid
        assert "security violation" in msg
        
        # Test session hijacking attempt (different user agent)
        valid, msg = secure_session.validate_session(
            session_id,
            "Evil Browser 1.0",  # Different user agent
            "192.168.1.100"
        )
        assert not valid
        assert "security violation" in msg


class TestAccessControl:
    """Test access control mechanisms."""
    
    def test_role_based_access_control(self):
        """Test RBAC implementation."""
        class RBACManager:
            def __init__(self):
                self.users = {}
                self.roles = {}
                self.permissions = set()
            
            def create_role(self, role_name, permissions):
                """Create role with permissions."""
                self.roles[role_name] = set(permissions)
                self.permissions.update(permissions)
            
            def assign_role(self, user_id, role_name):
                """Assign role to user."""
                if user_id not in self.users:
                    self.users[user_id] = {'roles': set()}
                
                if role_name in self.roles:
                    self.users[user_id]['roles'].add(role_name)
            
            def check_permission(self, user_id, required_permission):
                """Check if user has required permission."""
                if user_id not in self.users:
                    return False
                
                user_permissions = set()
                for role in self.users[user_id]['roles']:
                    if role in self.roles:
                        user_permissions.update(self.roles[role])
                
                return required_permission in user_permissions
            
            def get_user_permissions(self, user_id):
                """Get all permissions for user."""
                if user_id not in self.users:
                    return set()
                
                user_permissions = set()
                for role in self.users[user_id]['roles']:
                    if role in self.roles:
                        user_permissions.update(self.roles[role])
                
                return user_permissions
        
        rbac = RBACManager()
        
        # Create roles
        rbac.create_role('admin', ['read', 'write', 'delete', 'manage_users'])
        rbac.create_role('editor', ['read', 'write'])
        rbac.create_role('viewer', ['read'])
        
        # Assign roles to users
        rbac.assign_role('user1', 'admin')
        rbac.assign_role('user2', 'editor')
        rbac.assign_role('user3', 'viewer')
        
        # Test admin permissions
        assert rbac.check_permission('user1', 'read')
        assert rbac.check_permission('user1', 'write')
        assert rbac.check_permission('user1', 'delete')
        assert rbac.check_permission('user1', 'manage_users')
        
        # Test editor permissions
        assert rbac.check_permission('user2', 'read')
        assert rbac.check_permission('user2', 'write')
        assert not rbac.check_permission('user2', 'delete')
        assert not rbac.check_permission('user2', 'manage_users')
        
        # Test viewer permissions
        assert rbac.check_permission('user3', 'read')
        assert not rbac.check_permission('user3', 'write')
        assert not rbac.check_permission('user3', 'delete')
        assert not rbac.check_permission('user3', 'manage_users')
        
        # Test non-existent user
        assert not rbac.check_permission('user4', 'read')
    
    def test_principle_of_least_privilege(self):
        """Test principle of least privilege enforcement."""
        def create_minimal_permissions(user_role, requested_actions):
            """Create minimal permission set for user role."""
            role_permissions = {
                'guest': {'read'},
                'user': {'read', 'write_own'},
                'moderator': {'read', 'write_own', 'moderate'},
                'admin': {'read', 'write_any', 'delete', 'manage_users'}
            }
            
            if user_role not in role_permissions:
                return set()
            
            # Only grant permissions that are both requested and allowed for role
            allowed_permissions = role_permissions[user_role]
            granted_permissions = set(requested_actions) & allowed_permissions
            
            return granted_permissions
        
        # Test minimal permission granting
        guest_perms = create_minimal_permissions('guest', ['read', 'write_any', 'delete'])
        assert guest_perms == {'read'}
        
        user_perms = create_minimal_permissions('user', ['read', 'write_own', 'delete'])
        assert user_perms == {'read', 'write_own'}
        
        admin_perms = create_minimal_permissions('admin', ['read', 'write_any', 'delete'])
        assert admin_perms == {'read', 'write_any', 'delete'}
    
    def test_access_control_bypass_prevention(self):
        """Test prevention of access control bypass attempts."""
        class SecureAccessController:
            def __init__(self):
                self.user_permissions = {}
            
            def set_user_permissions(self, user_id, permissions):
                """Set permissions for user."""
                self.user_permissions[user_id] = set(permissions)
            
            def check_access(self, user_id, resource, action):
                """Check if user can perform action on resource."""
                # Always check authentication first
                if not user_id or user_id not in self.user_permissions:
                    return False, "Authentication required"
                
                required_permission = f"{action}:{resource}"
                user_perms = self.user_permissions[user_id]
                
                # Check exact permission match
                if required_permission in user_perms:
                    return True, "Access granted"
                
                # Check wildcard permissions carefully
                for perm in user_perms:
                    if perm.endswith(':*') and perm.startswith(action + ':'):
                        return True, "Access granted"
                
                return False, "Access denied"
            
            def secure_resource_access(self, user_id, resource_path, action):
                """Securely access resource with path validation."""
                import os
                
                # Validate resource path to prevent directory traversal
                normalized_path = os.path.normpath(resource_path)
                if normalized_path.startswith('../') or '/../' in normalized_path:
                    return False, "Invalid resource path"
                
                # Check access control
                allowed, message = self.check_access(user_id, resource_path, action)
                if not allowed:
                    return False, message
                
                return True, "Secure access granted"
        
        access_controller = SecureAccessController()
        
        # Set up user permissions
        access_controller.set_user_permissions('user1', ['read:document1', 'write:document1'])
        access_controller.set_user_permissions('admin', ['read:*', 'write:*', 'delete:*'])
        
        # Test normal access
        allowed, msg = access_controller.check_access('user1', 'document1', 'read')
        assert allowed
        
        # Test unauthorized access
        allowed, msg = access_controller.check_access('user1', 'document2', 'read')
        assert not allowed
        
        # Test admin wildcard access
        allowed, msg = access_controller.check_access('admin', 'any_document', 'read')
        assert allowed
        
        # Test unauthenticated access
        allowed, msg = access_controller.check_access(None, 'document1', 'read')
        assert not allowed
        assert "Authentication required" in msg
        
        # Test path traversal prevention
        allowed, msg = access_controller.secure_resource_access('admin', '../../../etc/passwd', 'read')
        assert not allowed
        assert "Invalid resource path" in msg
        
        # Test valid secure access
        allowed, msg = access_controller.secure_resource_access('admin', 'documents/report.txt', 'read')
        assert allowed


class TestMultiFactorAuthentication:
    """Test multi-factor authentication mechanisms."""
    
    def test_totp_generation_validation(self):
        """Test TOTP (Time-based One-Time Password) implementation."""
        def generate_totp_secret():
            """Generate TOTP secret key."""
            import secrets
            import base64
            return base64.b32encode(secrets.token_bytes(20)).decode()
        
        def generate_totp_code(secret, timestamp=None):
            """Generate TOTP code for given secret and timestamp."""
            import hmac
            import hashlib
            import base64
            import struct
            
            if timestamp is None:
                timestamp = int(time.time())
            
            # 30-second time step
            time_step = timestamp // 30
            
            # Convert secret from base32
            key = base64.b32decode(secret.encode())
            
            # Generate HMAC
            time_bytes = struct.pack('>Q', time_step)
            hmac_hash = hmac.new(key, time_bytes, hashlib.sha1).digest()
            
            # Dynamic truncation
            offset = hmac_hash[-1] & 0x0f
            code = struct.unpack('>I', hmac_hash[offset:offset+4])[0]
            code &= 0x7fffffff
            code %= 1000000
            
            return f"{code:06d}"
        
        def validate_totp_code(secret, provided_code, window=1):
            """Validate TOTP code with time window tolerance."""
            current_time = int(time.time())
            
            # Check current time and surrounding windows
            for i in range(-window, window + 1):
                timestamp = current_time + (i * 30)
                expected_code = generate_totp_code(secret, timestamp)
                if hmac.compare_digest(expected_code, provided_code):
                    return True
            
            return False
        
        # Test TOTP functionality
        secret = generate_totp_secret()
        assert len(secret) == 32  # Base32 encoded 20 bytes
        
        # Generate current code
        current_code = generate_totp_code(secret)
        assert len(current_code) == 6
        assert current_code.isdigit()
        
        # Validate current code
        assert validate_totp_code(secret, current_code)
        
        # Test invalid code
        assert not validate_totp_code(secret, "000000")
        
        # Test time window tolerance
        old_timestamp = int(time.time()) - 25  # 25 seconds ago
        old_code = generate_totp_code(secret, old_timestamp)
        assert validate_totp_code(secret, old_code, window=1)
    
    def test_backup_codes_security(self):
        """Test security of backup authentication codes."""
        def generate_backup_codes(count=10):
            """Generate secure backup codes."""
            import secrets
            import string
            
            codes = []
            charset = string.ascii_uppercase + string.digits
            charset = charset.replace('0', '').replace('O', '').replace('1', '').replace('I')  # Remove confusing chars
            
            for _ in range(count):
                # Generate 8-character backup code
                code = ''.join(secrets.choice(charset) for _ in range(8))
                # Add hyphen for readability
                formatted_code = f"{code[:4]}-{code[4:]}"
                codes.append(formatted_code)
            
            return codes
        
        def hash_backup_codes(codes):
            """Hash backup codes for secure storage."""
            import hashlib
            import secrets
            
            hashed_codes = {}
            for code in codes:
                salt = secrets.token_hex(16)
                hash_value = hashlib.pbkdf2_hmac('sha256', 
                                               code.encode('utf-8'), 
                                               salt.encode('utf-8'), 
                                               100000)
                hashed_codes[code] = {
                    'hash': hash_value.hex(),
                    'salt': salt,
                    'used': False
                }
            
            return hashed_codes
        
        def validate_backup_code(provided_code, hashed_codes):
            """Validate and mark backup code as used."""
            import hashlib
            
            for stored_code, data in hashed_codes.items():
                if data['used']:
                    continue
                
                # Check if provided code matches stored code
                test_hash = hashlib.pbkdf2_hmac('sha256',
                                              provided_code.encode('utf-8'),
                                              data['salt'].encode('utf-8'),
                                              100000)
                
                if hmac.compare_digest(test_hash.hex(), data['hash']):
                    data['used'] = True  # Mark as used
                    return True
            
            return False
        
        # Test backup code generation
        backup_codes = generate_backup_codes(8)
        assert len(backup_codes) == 8
        
        for code in backup_codes:
            assert len(code) == 9  # 4 chars + hyphen + 4 chars
            assert '-' in code
            assert code.replace('-', '').isalnum()
        
        # Verify codes are unique
        assert len(set(backup_codes)) == len(backup_codes)
        
        # Test code hashing and validation
        hashed_codes = hash_backup_codes(backup_codes)
        
        # Test valid code
        test_code = backup_codes[0]
        assert validate_backup_code(test_code, hashed_codes)
        
        # Test that same code cannot be used twice
        assert not validate_backup_code(test_code, hashed_codes)
        
        # Test invalid code
        assert not validate_backup_code("INVALID-CODE", hashed_codes)


class TestAuthorizationBypass:
    """Test prevention of authorization bypass vulnerabilities."""
    
    def test_direct_object_reference_prevention(self):
        """Test prevention of insecure direct object references."""
        class SecureObjectManager:
            def __init__(self):
                self.objects = {}
                self.user_objects = {}
            
            def create_object(self, user_id, obj_data):
                """Create object owned by user."""
                import secrets
                obj_id = secrets.token_hex(16)
                
                self.objects[obj_id] = {
                    'data': obj_data,
                    'owner': user_id,
                    'created': time.time()
                }
                
                if user_id not in self.user_objects:
                    self.user_objects[user_id] = set()
                self.user_objects[user_id].add(obj_id)
                
                return obj_id
            
            def access_object(self, user_id, obj_id):
                """Securely access object with ownership check."""
                # Check if object exists
                if obj_id not in self.objects:
                    return None, "Object not found"
                
                # Check ownership
                obj = self.objects[obj_id]
                if obj['owner'] != user_id:
                    return None, "Access denied - not object owner"
                
                return obj['data'], "Access granted"
            
            def list_user_objects(self, user_id):
                """List objects owned by user."""
                if user_id not in self.user_objects:
                    return []
                
                user_objs = []
                for obj_id in self.user_objects[user_id]:
                    if obj_id in self.objects:
                        user_objs.append({
                            'id': obj_id,
                            'data': self.objects[obj_id]['data']
                        })
                
                return user_objs
        
        obj_manager = SecureObjectManager()
        
        # Create objects for different users
        obj1_id = obj_manager.create_object('user1', 'User 1 data')
        obj2_id = obj_manager.create_object('user2', 'User 2 data')
        
        # Test legitimate access
        data, msg = obj_manager.access_object('user1', obj1_id)
        assert data == 'User 1 data'
        assert "Access granted" in msg
        
        # Test unauthorized access attempt
        data, msg = obj_manager.access_object('user1', obj2_id)
        assert data is None
        assert "Access denied" in msg
        
        # Test accessing non-existent object
        data, msg = obj_manager.access_object('user1', 'nonexistent')
        assert data is None
        assert "Object not found" in msg
        
        # Test user object listing
        user1_objects = obj_manager.list_user_objects('user1')
        assert len(user1_objects) == 1
        assert user1_objects[0]['data'] == 'User 1 data'
        
        user2_objects = obj_manager.list_user_objects('user2')
        assert len(user2_objects) == 1
        assert user2_objects[0]['data'] == 'User 2 data'
    
    def test_privilege_escalation_prevention(self):
        """Test prevention of privilege escalation attacks."""
        class PrivilegeManager:
            def __init__(self):
                self.users = {}
                self.admin_actions = {'create_user', 'delete_user', 'modify_permissions'}
                self.user_actions = {'read_own_data', 'modify_own_data'}
            
            def create_user(self, user_id, role):
                """Create user with specific role."""
                if role not in ['user', 'admin']:
                    raise ValueError("Invalid role")
                
                self.users[user_id] = {
                    'role': role,
                    'created': time.time(),
                    'permissions_modified': False
                }
            
            def check_action_allowed(self, user_id, action, target_user_id=None):
                """Check if user can perform action."""
                if user_id not in self.users:
                    return False, "User not found"
                
                user = self.users[user_id]
                
                # Admin can perform admin actions
                if user['role'] == 'admin' and action in self.admin_actions:
                    return True, "Admin access granted"
                
                # Users can perform user actions on themselves
                if user['role'] == 'user' and action in self.user_actions:
                    if target_user_id is None or target_user_id == user_id:
                        return True, "User access granted"
                
                return False, "Insufficient privileges"
            
            def modify_user_role(self, admin_user_id, target_user_id, new_role):
                """Modify user role (admin only)."""
                # Check admin privileges
                allowed, msg = self.check_action_allowed(admin_user_id, 'modify_permissions')
                if not allowed:
                    return False, msg
                
                # Prevent self-privilege modification unless explicitly allowed
                if admin_user_id == target_user_id:
                    return False, "Cannot modify own privileges"
                
                if target_user_id not in self.users:
                    return False, "Target user not found"
                
                if new_role not in ['user', 'admin']:
                    return False, "Invalid role"
                
                self.users[target_user_id]['role'] = new_role
                self.users[target_user_id]['permissions_modified'] = True
                
                return True, "Role modified successfully"
        
        priv_manager = PrivilegeManager()
        
        # Create users
        priv_manager.create_user('admin1', 'admin')
        priv_manager.create_user('user1', 'user')
        priv_manager.create_user('user2', 'user')
        
        # Test admin actions
        allowed, msg = priv_manager.check_action_allowed('admin1', 'create_user')
        assert allowed
        
        # Test user cannot perform admin actions
        allowed, msg = priv_manager.check_action_allowed('user1', 'create_user')
        assert not allowed
        assert "Insufficient privileges" in msg
        
        # Test privilege escalation prevention
        success, msg = priv_manager.modify_user_role('user1', 'user1', 'admin')
        assert not success
        assert "Insufficient privileges" in msg
        
        # Test admin cannot modify own privileges
        success, msg = priv_manager.modify_user_role('admin1', 'admin1', 'user')
        assert not success
        assert "Cannot modify own privileges" in msg
        
        # Test legitimate role modification
        success, msg = priv_manager.modify_user_role('admin1', 'user1', 'admin')
        assert success


if __name__ == "__main__":
    pytest.main([__file__, "-v"])