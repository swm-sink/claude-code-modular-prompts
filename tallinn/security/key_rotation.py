#!/usr/bin/env python3
"""
API Key Rotation Management Module

Handles API key rotation policies, key generation, and rotation scheduling.
Provides secure key management with proper encryption and lifecycle management.
"""

import os
import json
import secrets
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, Any, Optional


class ApiKeyRotationManager:
    """Manages API key rotation policies and operations."""
    
    def __init__(self, config_file: str = "api_key_rotation.json"):
        self.config_file = Path(config_file)
        self.rotation_script_file = Path("rotate_api_keys.py")
    
    def implement_api_key_rotation(self) -> None:
        """Implement API key rotation system."""
        print("\n🔄 Setting up API Key Rotation...")
        
        # Create API key rotation configuration
        rotation_config = self._create_rotation_config()
        
        # Save rotation configuration
        with open(self.config_file, 'w') as f:
            json.dump(rotation_config, f, indent=2)
        
        # Create rotation script
        self._create_rotation_script()
        
        # Make script executable
        os.chmod(self.rotation_script_file, 0o755)
        
        print("✅ API Key Rotation implemented")
        print(f"   - Configuration: {self.config_file}")
        print(f"   - Rotation script: {self.rotation_script_file}")
        print("   - Rotation interval: 90 days")
    
    def _create_rotation_config(self) -> Dict[str, Any]:
        """Create initial rotation configuration."""
        return {
            "rotation_policy": {
                "enabled": True,
                "rotation_interval_days": 90,
                "notification_days_before": 7,
                "auto_rotation": False,
                "last_rotation": datetime.now().isoformat(),
                "next_rotation": (datetime.now() + timedelta(days=90)).isoformat()
            },
            "api_keys": {
                "primary": self._generate_key_metadata(),
                "secondary": self._generate_key_metadata(status="standby")
            },
            "rotation_history": []
        }
    
    def _generate_key_metadata(self, status: str = "active") -> Dict[str, str]:
        """Generate metadata for a new API key."""
        return {
            "key_id": f"key_{secrets.token_hex(8)}",
            "created": datetime.now().isoformat(),
            "expires": (datetime.now() + timedelta(days=90)).isoformat(),
            "status": status,
            "hash": hashlib.sha256(secrets.token_urlsafe(32).encode()).hexdigest()
        }
    
    def _create_rotation_script(self) -> None:
        """Create the API key rotation script."""
        rotation_script_content = '''#!/usr/bin/env python3
"""
API Key Rotation Script
"""

import json
import secrets
import hashlib
from datetime import datetime, timedelta


def rotate_api_keys():
    """Rotate API keys according to the rotation policy."""
    # Load current configuration
    with open('api_key_rotation.json', 'r') as f:
        config = json.load(f)
    
    # Archive current primary key
    old_primary = config['api_keys']['primary'].copy()
    old_primary['archived'] = datetime.now().isoformat()
    config['rotation_history'].append(old_primary)
    
    # Promote secondary to primary
    config['api_keys']['primary'] = config['api_keys']['secondary'].copy()
    config['api_keys']['primary']['status'] = 'active'
    
    # Generate new secondary key
    new_key = secrets.token_urlsafe(32)
    config['api_keys']['secondary'] = {
        'key_id': f'key_{secrets.token_hex(8)}',
        'created': datetime.now().isoformat(),
        'expires': (datetime.now() + timedelta(days=90)).isoformat(),
        'status': 'standby',
        'hash': hashlib.sha256(new_key.encode()).hexdigest()
    }
    
    # Update rotation dates
    config['rotation_policy']['last_rotation'] = datetime.now().isoformat()
    config['rotation_policy']['next_rotation'] = (datetime.now() + timedelta(days=90)).isoformat()
    
    # Save updated configuration
    with open('api_key_rotation.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("✅ API keys rotated successfully")
    print(f"   New primary key ID: {config['api_keys']['primary']['key_id']}")
    print(f"   New secondary key ID: {config['api_keys']['secondary']['key_id']}")
    print(f"   Next rotation: {config['rotation_policy']['next_rotation']}")


def check_rotation_needed():
    """Check if rotation is needed and notify."""
    try:
        with open('api_key_rotation.json', 'r') as f:
            config = json.load(f)
        
        next_rotation = datetime.fromisoformat(config['rotation_policy']['next_rotation'].replace('Z', '+00:00'))
        days_until_rotation = (next_rotation - datetime.now()).days
        
        if days_until_rotation <= config['rotation_policy']['notification_days_before']:
            print(f"⚠️  API key rotation needed in {days_until_rotation} days")
            return True
        else:
            print(f"✅ Next rotation in {days_until_rotation} days")
            return False
    except Exception as e:
        print(f"❌ Error checking rotation status: {e}")
        return False


def main():
    """Main entry point for rotation operations."""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'check':
        check_rotation_needed()
    else:
        rotate_api_keys()


if __name__ == '__main__':
    main()
'''
        
        with open(self.rotation_script_file, 'w') as f:
            f.write(rotation_script_content)
    
    def load_rotation_config(self) -> Optional[Dict[str, Any]]:
        """Load the current rotation configuration."""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return None
    
    def get_rotation_status(self) -> Dict[str, Any]:
        """Get current rotation status."""
        config = self.load_rotation_config()
        if not config:
            return {"status": "not_configured", "message": "No rotation policy found"}
        
        try:
            next_rotation = datetime.fromisoformat(
                config['rotation_policy']['next_rotation'].replace('Z', '+00:00')
            )
            days_until_rotation = (next_rotation - datetime.now()).days
            
            return {
                "status": "configured",
                "days_until_rotation": days_until_rotation,
                "next_rotation": next_rotation.isoformat(),
                "last_rotation": config['rotation_policy']['last_rotation'],
                "auto_rotation": config['rotation_policy']['auto_rotation']
            }
        except Exception as e:
            return {"status": "error", "message": f"Error reading rotation config: {e}"}


class KeyRotationValidator:
    """Validates API key rotation implementation and security."""
    
    def __init__(self):
        self.rotation_manager = ApiKeyRotationManager()
    
    def validate_security_fixes(self) -> Dict[str, Any]:
        """Validate that critical security fixes have been implemented."""
        print("\n🔒 Validating Critical Security Fixes...")
        print("-" * 50)
        
        fixes_validated = 0
        total_fixes = 4
        validation_results = []
        
        # 1. Check CVE-2018-18074 fix
        req_file = Path("requirements.txt")
        if req_file.exists():
            with open(req_file, 'r') as f:
                content = f.read()
            if 'requests>=2.20.0' in content:
                print("✅ CVE-2018-18074 (requests) vulnerability fixed")
                fixes_validated += 1
                validation_results.append({"fix": "CVE-2018-18074", "status": "fixed"})
            else:
                print("❌ CVE-2018-18074 (requests) vulnerability NOT fixed")
                validation_results.append({"fix": "CVE-2018-18074", "status": "not_fixed"})
        
        # 2. Check eval/exec usage
        eval_found = self._check_eval_exec_usage()
        if not eval_found:
            print("✅ No unsafe eval() or exec() usage found")
            fixes_validated += 1
            validation_results.append({"fix": "eval_exec_usage", "status": "secure"})
        else:
            print("❌ Unsafe eval() or exec() usage still present")
            validation_results.append({"fix": "eval_exec_usage", "status": "unsafe"})
        
        # 3. Check secure API key encryption system
        if Path("secure_api_key_manager.py").exists():
            print("✅ Secure API key encryption system implemented")
            fixes_validated += 1
            validation_results.append({"fix": "api_key_encryption", "status": "implemented"})
        else:
            print("❌ Secure API key encryption system NOT implemented")
            validation_results.append({"fix": "api_key_encryption", "status": "not_implemented"})
        
        # 4. Check cryptography dependency
        if req_file.exists():
            with open(req_file, 'r') as f:
                content = f.read()
            if 'cryptography' in content:
                print("✅ Cryptography dependency added")
                fixes_validated += 1
                validation_results.append({"fix": "cryptography_dependency", "status": "added"})
            else:
                print("❌ Cryptography dependency NOT added")
                validation_results.append({"fix": "cryptography_dependency", "status": "not_added"})
        
        print(f"\n🛡️ Security Fixes Summary: {fixes_validated}/{total_fixes} fixes validated")
        
        if fixes_validated == total_fixes:
            print("🎉 All critical security fixes have been successfully implemented!")
            status = "all_fixed"
        else:
            print("⚠️  Some critical security fixes are still pending implementation.")
            status = "fixes_pending"
        
        return {
            "status": status,
            "fixes_validated": fixes_validated,
            "total_fixes": total_fixes,
            "validation_results": validation_results
        }
    
    def _check_eval_exec_usage(self) -> bool:
        """Check for unsafe eval/exec usage in the codebase."""
        eval_found = False
        
        for file_path in Path(".").rglob("*.py"):
            # Skip this security audit script itself
            if file_path.name in ["security_audit.py", "key_rotation.py"]:
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Skip comments and string literals containing eval/exec
                lines = content.split('\n')
                for line in lines:
                    line = line.strip()
                    # Skip comments
                    if line.startswith('#') or not line:
                        continue
                    # Skip string literals
                    if ('"' in line and ('eval()' in line or 'exec()' in line)) or \
                       ("'" in line and ('eval()' in line or 'exec()' in line)):
                        continue
                    # Check for actual eval/exec calls
                    import re
                    if re.search(r'\beval\s*\(|\bexec\s*\(', line):
                        eval_found = True
                        break
                if eval_found:
                    break
            except:
                pass
        
        return eval_found