#!/usr/bin/env python3
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
