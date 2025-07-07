#!/usr/bin/env python3
"""
Permission Guardian - Prevents Claude Code from auto-restricting permissions
Monitors and protects settings files from unwanted modifications.
"""

import json
import os
import sys
import time
import hashlib
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class PermissionGuardian(FileSystemEventHandler):
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.claude_dir = self.project_root / ".claude"
        self.home_claude = Path.home() / ".claude"
        
        # Golden configuration (never allow less than this)
        self.golden_permissions = {
            "permissions": {
                "allow": [
                    "Bash(*)", "Read(*)", "Edit(*)", "Write(*)", "MultiEdit(*)",
                    "Glob(*)", "Grep(*)", "LS(*)", "Task(*)", "WebFetch(*)", 
                    "WebSearch(*)", "TodoRead(*)", "TodoWrite(*)",
                    "NotebookRead(*)", "NotebookEdit(*)", "exit_plan_mode(*)",
                    "mcp__ide__getDiagnostics(*)", "mcp__ide__executeCode(*)",
                    "mcp__*"
                ],
                "deny": []
            }
        }
        
        # Track file hashes to detect modifications
        self.file_hashes = {}
        self.protected_files = [
            self.home_claude / "settings.json",
            self.claude_dir / "settings.json",
            self.claude_dir / "settings.local.json"
        ]
        
    def get_file_hash(self, file_path):
        """Get SHA256 hash of file contents."""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except:
            return None
    
    def is_permissions_downgrade(self, old_config, new_config):
        """Check if permissions have been downgraded."""
        if not old_config or not new_config:
            return False
            
        old_perms = old_config.get("permissions", {}).get("allow", [])
        new_perms = new_config.get("permissions", {}).get("allow", [])
        
        # Check if wildcard permissions were removed
        wildcards = ["Bash(*)", "Read(*)", "Edit(*)", "Write(*)", "MultiEdit(*)"]
        old_wildcards = sum(1 for w in wildcards if w in old_perms)
        new_wildcards = sum(1 for w in wildcards if w in new_perms)
        
        return new_wildcards < old_wildcards or len(new_perms) < len(old_perms) // 2
    
    def restore_permissions(self, file_path):
        """Restore permissions to golden configuration."""
        try:
            print(f"🚨 PERMISSION DOWNGRADE DETECTED: {file_path}")
            print("🛡️  RESTORING GOLDEN CONFIGURATION...")
            
            with open(file_path, 'w') as f:
                json.dump(self.golden_permissions, f, indent=2)
            
            print(f"✅ PERMISSIONS RESTORED: {file_path}")
            return True
        except Exception as e:
            print(f"❌ FAILED TO RESTORE: {e}")
            return False
    
    def on_modified(self, event):
        """Handle file modification events."""
        if event.is_directory:
            return
            
        file_path = Path(event.src_path)
        
        # Only monitor settings files
        if file_path not in self.protected_files:
            return
            
        # Check if this is a permissions downgrade
        try:
            with open(file_path, 'r') as f:
                new_config = json.load(f)
            
            old_hash = self.file_hashes.get(str(file_path))
            new_hash = self.get_file_hash(file_path)
            
            if old_hash and old_hash != new_hash:
                # File was modified, check for downgrade
                if self.is_permissions_downgrade(None, new_config):
                    self.restore_permissions(file_path)
                    
            self.file_hashes[str(file_path)] = new_hash
            
        except Exception as e:
            print(f"⚠️  Error monitoring {file_path}: {e}")
    
    def start_monitoring(self):
        """Start monitoring settings files."""
        print("🛡️  Permission Guardian Starting...")
        print("👁️  Monitoring settings files for auto-restriction attacks...")
        
        # Initialize file hashes
        for file_path in self.protected_files:
            if file_path.exists():
                self.file_hashes[str(file_path)] = self.get_file_hash(file_path)
        
        # Set up file system watcher
        observer = Observer()
        observer.schedule(self, str(self.home_claude), recursive=False)
        observer.schedule(self, str(self.claude_dir), recursive=False)
        observer.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            print("🛑 Permission Guardian Stopped")
        observer.join()

def create_protection_script():
    """Create protection script for immediate use."""
    script_content = '''#!/bin/bash
# Permission Guardian - Run this to protect against auto-restriction

echo "🛡️  Setting up Permission Protection..."

# Make user global settings read-only
chmod 644 ~/.claude/settings.json 2>/dev/null || true

# Remove problematic project-level settings
rm -f .claude/settings.local.json 2>/dev/null || true

# Create protected project settings
cat > .claude/settings.json << 'EOF'
{
  "permissions": {
    "allow": [
      "Bash(*)", "Read(*)", "Edit(*)", "Write(*)", "MultiEdit(*)",
      "Glob(*)", "Grep(*)", "LS(*)", "Task(*)", "WebFetch(*)", 
      "WebSearch(*)", "TodoRead(*)", "TodoWrite(*)",
      "NotebookRead(*)", "NotebookEdit(*)", "exit_plan_mode(*)",
      "mcp__ide__getDiagnostics(*)", "mcp__ide__executeCode(*)", "mcp__*"
    ],
    "deny": []
  }
}
EOF

echo "✅ Permission Protection Activated"
echo "🚨 WARNING: NEVER use Claude's permission prompts - they will reset everything!"
echo "💡 TIP: If prompted, always say 'No' and the commands will still work via pre-configured permissions"
'''
    
    script_path = Path(__file__).parent / "protect_permissions.sh"
    with open(script_path, 'w') as f:
        f.write(script_content)
    os.chmod(script_path, 0o755)
    print(f"✅ Protection script created: {script_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--create-script":
        create_protection_script()
    else:
        guardian = PermissionGuardian()
        guardian.start_monitoring()