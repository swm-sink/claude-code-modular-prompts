#!/usr/bin/env python3
"""
🛡️ PERMISSION FORTRESS - Bulletproof Protection System
Never lose permissions again. Self-healing, auto-correcting, battle-tested.
"""

import json
import os
import time
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set

class PermissionFortress:
    """Ultimate permission protection system"""
    
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
        self.log_file = self.claude_dir / "permission_fortress.log"
        
        # Create backup directory
        self.backup_dir.mkdir(exist_ok=True)
        
    def log(self, message: str, level: str = "INFO"):
        """Log with timestamp"""
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        # Console output
        color = {"INFO": "\033[94m", "SUCCESS": "\033[92m", "WARNING": "\033[93m", "ERROR": "\033[91m"}.get(level, "")
        print(f"{color}{log_entry}\033[0m", end="")
        
        # File logging
        with open(self.log_file, "a") as f:
            f.write(log_entry)
    
    def check_symlink_health(self) -> bool:
        """Verify symlink is intact and pointing correctly"""
        if not self.local_settings.exists():
            self.log("❌ Local settings file missing!", "ERROR")
            return False
            
        if not self.local_settings.is_symlink():
            self.log("❌ Local settings is not a symlink!", "ERROR")
            return False
            
        # Get the raw symlink target
        try:
            raw_target = os.readlink(self.local_settings)
            self.log(f"📍 Symlink target: {raw_target}", "INFO")
            
            # Detect temp directory hijacking
            if '/tmp/' in raw_target or '/var/folders/' in raw_target or '/T/' in raw_target:
                self.log(f"🚨 CRITICAL: Symlink hijacked to temp directory: {raw_target}", "ERROR")
                self.log("🔧 Forcing symlink repair...", "WARNING")
                return False
        except Exception as e:
            self.log(f"⚠️ Could not read symlink target: {e}", "WARNING")
            
        # Compare resolved paths to handle path variations
        target = self.local_settings.resolve()
        expected = self.global_settings.resolve()
        
        if target != expected:
            self.log(f"❌ Symlink points to wrong target: {target}", "ERROR")
            self.log(f"📍 Expected: {expected}", "INFO")
            return False
            
        self.log("✅ Symlink healthy", "SUCCESS")
        return True
    
    def validate_permissions(self, settings_path: Path) -> Dict[str, any]:
        """Check if settings have all required permissions"""
        try:
            with open(settings_path) as f:
                settings = json.load(f)
            
            current_allow = set(settings.get("permissions", {}).get("allow", []))
            current_deny = set(settings.get("permissions", {}).get("deny", []))
            
            missing = self.REQUIRED_PERMISSIONS - current_allow
            missing_deny = self.DENY_PERMISSIONS - current_deny
            
            return {
                "valid": len(missing) == 0 and len(missing_deny) == 0,
                "missing_allow": missing,
                "missing_deny": missing_deny,
                "current_allow": current_allow,
                "current_deny": current_deny,
                "settings": settings
            }
        except Exception as e:
            return {
                "valid": False,
                "error": str(e),
                "missing_allow": self.REQUIRED_PERMISSIONS,
                "missing_deny": self.DENY_PERMISSIONS
            }
    
    def repair_symlink(self):
        """Recreate symlink if broken"""
        self.log("🔧 Repairing symlink...", "WARNING")
        
        # Remove broken symlink or file
        try:
            if self.local_settings.exists() or self.local_settings.is_symlink():
                self.local_settings.unlink()
        except Exception as e:
            self.log(f"⚠️ Error removing old file: {e}", "WARNING")
        
        # Create new symlink
        try:
            self.local_settings.symlink_to(self.global_settings)
            self.log("✅ Symlink repaired", "SUCCESS")
        except Exception as e:
            self.log(f"❌ Failed to create symlink: {e}", "ERROR")
    
    def repair_permissions(self, settings_path: Path, validation_result: Dict):
        """Fix missing permissions"""
        self.log(f"🔧 Repairing permissions in {settings_path}...", "WARNING")
        
        # Create backup first
        backup_path = self.backup_dir / f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        if settings_path.exists():
            with open(settings_path) as f:
                backup_data = f.read()
            with open(backup_path, "w") as f:
                f.write(backup_data)
            self.log(f"📦 Backup created: {backup_path}", "INFO")
        
        # Build correct settings
        settings = validation_result.get("settings", {})
        if "permissions" not in settings:
            settings["permissions"] = {}
        
        # Ensure all required permissions
        settings["permissions"]["allow"] = list(self.REQUIRED_PERMISSIONS)
        settings["permissions"]["deny"] = list(self.DENY_PERMISSIONS)
        
        # Preserve other settings
        if "env" not in settings:
            settings["env"] = {"CLAUDE_CODE_ENABLE_TELEMETRY": "1"}
        if "model" not in settings:
            settings["model"] = "opus"
        
        # Write repaired settings
        with open(settings_path, "w") as f:
            json.dump(settings, f, indent=2)
        
        self.log("✅ Permissions repaired", "SUCCESS")
    
    def fortress_check(self) -> bool:
        """Complete fortress integrity check"""
        self.log("🏰 PERMISSION FORTRESS CHECK", "INFO")
        
        all_good = True
        
        # 1. Check symlink health
        if not self.check_symlink_health():
            self.repair_symlink()
            all_good = False
        
        # 2. Validate global permissions
        global_validation = self.validate_permissions(self.global_settings)
        if not global_validation["valid"]:
            self.log("❌ Global permissions incomplete", "ERROR")
            self.repair_permissions(self.global_settings, global_validation)
            all_good = False
        else:
            self.log("✅ Global permissions valid", "SUCCESS")
        
        # 3. Re-check after repairs
        if not all_good:
            self.log("🔄 Re-validating after repairs...", "INFO")
            
            # Check symlink again
            if not self.check_symlink_health():
                self.log("❌ CRITICAL: Symlink repair failed!", "ERROR")
                return False
            
            # Check permissions again
            global_validation = self.validate_permissions(self.global_settings)
            if not global_validation["valid"]:
                self.log("❌ CRITICAL: Permission repair failed!", "ERROR")
                return False
        
        self.log("✅ FORTRESS SECURE - All systems operational", "SUCCESS")
        return True
    
    def monitor_mode(self, interval: int = 5):
        """Continuous monitoring with auto-repair"""
        self.log(f"🛡️ FORTRESS MONITOR ACTIVE - Checking every {interval}s", "INFO")
        self.log("Press Ctrl+C to stop monitoring", "INFO")
        
        check_count = 0
        repair_count = 0
        
        try:
            while True:
                check_count += 1
                
                # Quick symlink check
                if not self.local_settings.exists() or not self.local_settings.is_symlink():
                    self.log(f"⚡ Quick repair needed (check #{check_count})", "WARNING")
                    self.repair_symlink()
                    repair_count += 1
                
                # Full check every 10 iterations
                if check_count % 10 == 0:
                    if not self.fortress_check():
                        repair_count += 1
                
                # Status update every 100 checks
                if check_count % 100 == 0:
                    self.log(f"📊 Monitor stats: {check_count} checks, {repair_count} repairs", "INFO")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            self.log(f"\n🛑 Monitor stopped. Total: {check_count} checks, {repair_count} repairs", "INFO")
    
    def nuclear_option(self):
        """Complete permission system reset - use only in emergencies"""
        self.log("☢️  NUCLEAR OPTION ACTIVATED - Complete permission reset", "WARNING")
        
        response = input("⚠️  This will completely reset all permissions. Continue? (yes/no): ")
        if response.lower() != "yes":
            self.log("❌ Nuclear option cancelled", "INFO")
            return
        
        # Create comprehensive backup
        backup_dir = self.backup_dir / f"nuclear_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        backup_dir.mkdir(exist_ok=True)
        
        # Backup all settings files
        for settings_file in [self.global_settings, self.local_settings, self.claude_dir / "settings.json"]:
            if settings_file.exists():
                backup_path = backup_dir / settings_file.name
                with open(settings_file) as f:
                    content = f.read()
                with open(backup_path, "w") as f:
                    f.write(content)
                self.log(f"📦 Backed up {settings_file} to {backup_path}", "INFO")
        
        # Remove all settings files
        for settings_file in [self.local_settings, self.claude_dir / "settings.json"]:
            if settings_file.exists():
                settings_file.unlink()
                self.log(f"🗑️  Removed {settings_file}", "INFO")
        
        # Create fresh global settings
        perfect_settings = {
            "permissions": {
                "allow": list(self.REQUIRED_PERMISSIONS),
                "deny": list(self.DENY_PERMISSIONS)
            },
            "env": {
                "CLAUDE_CODE_ENABLE_TELEMETRY": "1"
            },
            "model": "opus"
        }
        
        # Ensure global directory exists
        self.global_settings.parent.mkdir(exist_ok=True)
        
        # Write global settings
        with open(self.global_settings, "w") as f:
            json.dump(perfect_settings, f, indent=2)
        self.log("✅ Created fresh global settings", "SUCCESS")
        
        # Create symlink
        self.local_settings.symlink_to(self.global_settings)
        self.log("✅ Created fresh symlink", "SUCCESS")
        
        # Final validation
        if self.fortress_check():
            self.log("✅ NUCLEAR RESET SUCCESSFUL - Permissions restored", "SUCCESS")
        else:
            self.log("❌ NUCLEAR RESET FAILED - Manual intervention required", "ERROR")


def main():
    """CLI interface"""
    fortress = PermissionFortress()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "check":
            fortress.fortress_check()
        elif command == "monitor":
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 5
            fortress.monitor_mode(interval)
        elif command == "nuclear":
            fortress.nuclear_option()
        else:
            print("Usage: permission_fortress.py [check|monitor|nuclear]")
    else:
        # Default: single check
        fortress.fortress_check()


if __name__ == "__main__":
    main()