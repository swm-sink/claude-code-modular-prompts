#!/usr/bin/env python3
"""
Secure API Key Encryption System
Provides encrypted storage and management of API keys with rotation support.
"""

import os
import json
import secrets
import hashlib
import base64
from pathlib import Path
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class SecureAPIKeyManager:
    """Secure API key management with encryption at rest."""
    
    def __init__(self, master_key: str = None, key_store_path: str = "encrypted_keys.json"):
        self.key_store_path = Path(key_store_path)
        self.master_key = master_key or self._get_or_create_master_key()
        self.cipher_suite = self._setup_encryption()
        
    def _get_or_create_master_key(self) -> str:
        """Get or create master encryption key from environment or secure storage."""
        # First try environment variable
        master_key = os.environ.get('CLAUDE_MASTER_KEY')
        if master_key:
            return master_key
            
        # Check for secure key file
        key_file = Path('.claude_master.key')
        if key_file.exists():
            with open(key_file, 'rb') as f:
                return base64.b64decode(f.read()).decode('utf-8')
        
        # Generate new master key
        new_key = secrets.token_urlsafe(32)
        
        # Save to secure file with restricted permissions
        with open(key_file, 'wb') as f:
            f.write(base64.b64encode(new_key.encode('utf-8')))
        
        # Set restrictive permissions (owner read/write only)
        os.chmod(key_file, 0o600)
        
        print("🔑 Generated new master key. Store CLAUDE_MASTER_KEY environment variable securely.")
        print(f"   Master key: {new_key}")
        
        return new_key
    
    def _setup_encryption(self) -> Fernet:
        """Setup Fernet encryption with PBKDF2 key derivation."""
        # Generate salt for key derivation
        salt_file = Path('.claude_salt')
        if salt_file.exists():
            with open(salt_file, 'rb') as f:
                salt = f.read()
        else:
            salt = os.urandom(16)
            with open(salt_file, 'wb') as f:
                f.write(salt)
            os.chmod(salt_file, 0o600)
        
        # Derive encryption key from master key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.master_key.encode()))
        return Fernet(key)
    
    def encrypt_api_key(self, key_name: str, api_key: str, metadata: dict = None) -> str:
        """Encrypt and store an API key with metadata."""
        key_data = {
            'name': key_name,
            'api_key': api_key,
            'created': datetime.now().isoformat(),
            'expires': (datetime.now() + timedelta(days=90)).isoformat(),
            'last_used': None,
            'usage_count': 0,
            'metadata': metadata or {}
        }
        
        # Encrypt the key data
        encrypted_data = self.cipher_suite.encrypt(
            json.dumps(key_data).encode('utf-8')
        )
        
        # Generate unique key ID
        key_id = f"key_{hashlib.sha256(api_key.encode()).hexdigest()[:16]}"
        
        # Load existing key store or create new
        key_store = self._load_key_store()
        
        # Store encrypted key
        key_store['keys'][key_id] = {
            'name': key_name,
            'encrypted_data': base64.b64encode(encrypted_data).decode('utf-8'),
            'created': key_data['created'],
            'expires': key_data['expires'],
            'key_hash': hashlib.sha256(api_key.encode()).hexdigest(),
            'status': 'active'
        }
        
        # Update metadata
        key_store['metadata']['last_updated'] = datetime.now().isoformat()
        key_store['metadata']['total_keys'] = len(key_store['keys'])
        
        # Save key store
        self._save_key_store(key_store)
        
        return key_id
    
    def decrypt_api_key(self, key_id: str) -> dict:
        """Decrypt and retrieve an API key by ID."""
        key_store = self._load_key_store()
        
        if key_id not in key_store['keys']:
            raise ValueError(f"API key {key_id} not found")
        
        stored_key = key_store['keys'][key_id]
        
        if stored_key['status'] != 'active':
            raise ValueError(f"API key {key_id} is not active")
        
        # Check if key has expired
        expires = datetime.fromisoformat(stored_key['expires'])
        if datetime.now() > expires:
            raise ValueError(f"API key {key_id} has expired")
        
        # Decrypt the key data
        encrypted_data = base64.b64decode(stored_key['encrypted_data'])
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        key_data = json.loads(decrypted_data.decode('utf-8'))
        
        # Update usage tracking
        key_data['last_used'] = datetime.now().isoformat()
        key_data['usage_count'] += 1
        
        # Re-encrypt and save updated data
        self._update_key_usage(key_id, key_data)
        
        return key_data
    
    def rotate_api_key(self, key_id: str, new_api_key: str) -> str:
        """Rotate an API key with a new value."""
        key_store = self._load_key_store()
        
        if key_id not in key_store['keys']:
            raise ValueError(f"API key {key_id} not found")
        
        # Get existing key data
        old_key_data = self.decrypt_api_key(key_id)
        
        # Archive old key
        key_store['keys'][key_id]['status'] = 'rotated'
        key_store['keys'][key_id]['rotated_at'] = datetime.now().isoformat()
        
        # Create new key with rotated data
        new_key_data = old_key_data.copy()
        new_key_data['api_key'] = new_api_key
        new_key_data['created'] = datetime.now().isoformat()
        new_key_data['expires'] = (datetime.now() + timedelta(days=90)).isoformat()
        new_key_data['rotated_from'] = key_id
        
        # Encrypt new key
        new_key_id = self.encrypt_api_key(
            old_key_data['name'], 
            new_api_key, 
            new_key_data.get('metadata', {})
        )
        
        # Update rotation history
        if 'rotation_history' not in key_store['metadata']:
            key_store['metadata']['rotation_history'] = []
        
        key_store['metadata']['rotation_history'].append({
            'old_key_id': key_id,
            'new_key_id': new_key_id,
            'rotated_at': datetime.now().isoformat()
        })
        
        self._save_key_store(key_store)
        
        return new_key_id
    
    def list_api_keys(self) -> list:
        """List all API keys with their metadata (without actual keys)."""
        key_store = self._load_key_store()
        
        return [
            {
                'key_id': key_id,
                'name': key_data['name'],
                'created': key_data['created'],
                'expires': key_data['expires'],
                'status': key_data['status']
            }
            for key_id, key_data in key_store['keys'].items()
        ]
    
    def revoke_api_key(self, key_id: str) -> bool:
        """Revoke an API key."""
        key_store = self._load_key_store()
        
        if key_id not in key_store['keys']:
            return False
        
        key_store['keys'][key_id]['status'] = 'revoked'
        key_store['keys'][key_id]['revoked_at'] = datetime.now().isoformat()
        
        self._save_key_store(key_store)
        return True
    
    def cleanup_expired_keys(self) -> int:
        """Remove expired keys from storage."""
        key_store = self._load_key_store()
        removed_count = 0
        
        keys_to_remove = []
        for key_id, key_data in key_store['keys'].items():
            expires = datetime.fromisoformat(key_data['expires'])
            if datetime.now() > expires + timedelta(days=30):  # Grace period
                keys_to_remove.append(key_id)
        
        for key_id in keys_to_remove:
            del key_store['keys'][key_id]
            removed_count += 1
        
        if removed_count > 0:
            key_store['metadata']['last_cleanup'] = datetime.now().isoformat()
            self._save_key_store(key_store)
        
        return removed_count
    
    def _load_key_store(self) -> dict:
        """Load encrypted key store from disk."""
        if not self.key_store_path.exists():
            return {
                'version': '1.0',
                'created': datetime.now().isoformat(),
                'metadata': {
                    'total_keys': 0,
                    'last_updated': datetime.now().isoformat()
                },
                'keys': {}
            }
        
        with open(self.key_store_path, 'r') as f:
            return json.load(f)
    
    def _save_key_store(self, key_store: dict) -> None:
        """Save key store to disk with secure permissions."""
        with open(self.key_store_path, 'w') as f:
            json.dump(key_store, f, indent=2)
        
        # Set secure permissions
        os.chmod(self.key_store_path, 0o600)
    
    def _update_key_usage(self, key_id: str, key_data: dict) -> None:
        """Update key usage statistics."""
        key_store = self._load_key_store()
        
        # Re-encrypt updated key data
        encrypted_data = self.cipher_suite.encrypt(
            json.dumps(key_data).encode('utf-8')
        )
        
        key_store['keys'][key_id]['encrypted_data'] = base64.b64encode(encrypted_data).decode('utf-8')
        self._save_key_store(key_store)
    
    def export_keys_for_backup(self, backup_path: str, include_keys: bool = False) -> bool:
        """Export key metadata for backup (optionally include encrypted keys)."""
        key_store = self._load_key_store()
        
        backup_data = {
            'version': key_store['version'],
            'exported': datetime.now().isoformat(),
            'metadata': key_store['metadata'],
            'keys': {}
        }
        
        for key_id, key_data in key_store['keys'].items():
            backup_data['keys'][key_id] = {
                'name': key_data['name'],
                'created': key_data['created'],
                'expires': key_data['expires'],
                'status': key_data['status']
            }
            
            if include_keys:
                backup_data['keys'][key_id]['encrypted_data'] = key_data['encrypted_data']
                backup_data['keys'][key_id]['key_hash'] = key_data['key_hash']
        
        with open(backup_path, 'w') as f:
            json.dump(backup_data, f, indent=2)
        
        os.chmod(backup_path, 0o600)
        return True
    
    # Test compatibility aliases
    def store_api_key(self, key_name: str, api_key: str, metadata: dict = None) -> bool:
        """Store API key (simplified interface)."""
        try:
            self.encrypt_api_key(key_name, api_key, metadata)
            return True
        except Exception:
            return False
    
    def retrieve_api_key(self, key_name_or_id: str) -> str:
        """Retrieve API key by name or ID (simplified interface)."""
        try:
            # First try to find by name
            key_store = self._load_key_store()
            key_id = None
            
            # Look for key by name
            for kid, key_info in key_store.get('keys', {}).items():
                if key_info.get('name') == key_name_or_id:
                    key_id = kid
                    break
            
            # If not found by name, try using it as an ID
            if not key_id:
                key_id = key_name_or_id
            
            key_data = self.decrypt_api_key(key_id)
            return key_data.get('api_key') if key_data else None
        except Exception:
            return None
    
    def delete_api_key(self, key_id: str) -> bool:
        """Delete API key (alias for revoke_api_key)."""
        return self.revoke_api_key(key_id)


# CLI interface for testing

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Secure API Key Manager')
    parser.add_argument('action', choices=['encrypt', 'decrypt', 'list', 'rotate', 'revoke', 'cleanup'])
    parser.add_argument('--name', help='Key name')
    parser.add_argument('--key', help='API key value')
    parser.add_argument('--key-id', help='Key ID')
    parser.add_argument('--new-key', help='New API key for rotation')
    
    args = parser.parse_args()
    
    manager = SecureAPIKeyManager()
    
    try:
        if args.action == 'encrypt':
            if not args.name or not args.key:
                print("Error: --name and --key required for encryption")
                exit(1)
            key_id = manager.encrypt_api_key(args.name, args.key)
            print(f"✅ API key encrypted with ID: {key_id}")
        
        elif args.action == 'decrypt':
            if not args.key_id:
                print("Error: --key-id required for decryption")
                exit(1)
            key_data = manager.decrypt_api_key(args.key_id)
            print(f"✅ API key: {key_data['api_key']}")
            print(f"   Name: {key_data['name']}")
            print(f"   Created: {key_data['created']}")
            print(f"   Usage count: {key_data['usage_count']}")
        
        elif args.action == 'list':
            keys = manager.list_api_keys()
            print(f"📋 Found {len(keys)} API keys:")
            for key in keys:
                print(f"   {key['key_id']}: {key['name']} ({key['status']})")
        
        elif args.action == 'rotate':
            if not args.key_id or not args.new_key:
                print("Error: --key-id and --new-key required for rotation")
                exit(1)
            new_key_id = manager.rotate_api_key(args.key_id, args.new_key)
            print(f"🔄 Key rotated. New ID: {new_key_id}")
        
        elif args.action == 'revoke':
            if not args.key_id:
                print("Error: --key-id required for revocation")
                exit(1)
            success = manager.revoke_api_key(args.key_id)
            if success:
                print(f"❌ Key {args.key_id} revoked")
            else:
                print(f"Error: Key {args.key_id} not found")
        
        elif args.action == 'cleanup':
            removed = manager.cleanup_expired_keys()
            print(f"🧹 Cleaned up {removed} expired keys")
    
    except Exception as e:
        print(f"Error: {e}")
        exit(1)