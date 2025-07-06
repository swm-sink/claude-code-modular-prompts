#!/usr/bin/env python3
"""
Claude Code Permission Validation Tool
Monitors and validates permission configurations across all hierarchy levels.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class PermissionValidator:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.claude_dir = self.project_root / ".claude"
        self.home_dir = Path.home()
        
        # Required permissions for framework operation
        self.required_permissions = [
            "Bash(*)", "Read(*)", "Edit(*)", "Write(*)", "MultiEdit(*)",
            "Glob(*)", "Grep(*)", "LS(*)", "Task(*)", "WebFetch(*)", 
            "WebSearch(*)", "TodoRead(*)", "TodoWrite(*)", 
            "NotebookRead(*)", "NotebookEdit(*)", "exit_plan_mode(*)",
            "mcp__ide__getDiagnostics(*)", "mcp__ide__executeCode(*)"
        ]

    def get_settings_files(self) -> Dict[str, Path]:
        """Get all Claude Code settings files in precedence order."""
        return {
            "enterprise_macos": Path("/Library/Application Support/ClaudeCode/managed-settings.json"),
            "enterprise_linux": Path("/etc/claude-code/managed-settings.json"),
            "user_global": self.home_dir / ".claude" / "settings.json",
            "user_local": self.home_dir / ".claude" / "settings.local.json", 
            "main_global": self.home_dir / ".claude.json",
            "project_local": self.claude_dir / "settings.local.json",
            "project_shared": self.claude_dir / "settings.json"
        }

    def read_settings_file(self, file_path: Path) -> Optional[Dict]:
        """Safely read a settings file."""
        if not file_path.exists():
            return None
        
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, PermissionError) as e:
            print(f"⚠️  Error reading {file_path}: {e}")
            return None

    def validate_permissions(self, settings: Dict) -> Tuple[bool, List[str]]:
        """Validate that required permissions are present."""
        if "permissions" not in settings:
            return False, ["No permissions section found"]
        
        permissions = settings["permissions"]
        allowed = permissions.get("allow", [])
        
        missing = []
        
        # Check for dangerouslySkipPermissions (bypasses all restrictions)
        if settings.get("dangerouslySkipPermissions") or settings.get("dangerously-skip-permissions"):
            return True, ["Using dangerouslySkipPermissions - all tools allowed"]
        
        # Check for wildcard permissions
        if "Bash(*)" in allowed and "Read(*)" in allowed and "Write(*)" in allowed:
            return True, ["Comprehensive wildcard permissions found"]
        
        # Check individual required permissions
        for req_perm in self.required_permissions:
            if req_perm not in allowed:
                missing.append(req_perm)
        
        if missing:
            return False, missing
        
        return True, ["All required permissions present"]

    def check_permission_hierarchy(self) -> Dict[str, Dict]:
        """Check permissions across all hierarchy levels."""
        settings_files = self.get_settings_files()
        results = {}
        
        for level, file_path in settings_files.items():
            settings = self.read_settings_file(file_path)
            if settings is None:
                results[level] = {
                    "exists": False,
                    "valid": None,
                    "issues": ["File does not exist"]
                }
            else:
                valid, issues = self.validate_permissions(settings)
                results[level] = {
                    "exists": True,
                    "valid": valid,
                    "issues": issues,
                    "file_path": str(file_path)
                }
        
        return results

    def backup_settings(self) -> None:
        """Create backup of current settings."""
        backup_dir = self.claude_dir / "backups" / "permissions"
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        settings_files = self.get_settings_files()
        
        for level, file_path in settings_files.items():
            if file_path.exists():
                backup_path = backup_dir / f"{level}_backup.json"
                import shutil
                shutil.copy2(file_path, backup_path)
                print(f"✅ Backed up {level} to {backup_path}")

    def restore_project_permissions(self) -> bool:
        """Restore comprehensive permissions to project settings."""
        project_settings_path = self.claude_dir / "settings.local.json"
        
        comprehensive_config = {
            "permissions": {
                "allow": self.required_permissions,
                "deny": []
            }
        }
        
        try:
            with open(project_settings_path, 'w') as f:
                json.dump(comprehensive_config, f, indent=2)
            print(f"✅ Restored comprehensive permissions to {project_settings_path}")
            return True
        except Exception as e:
            print(f"❌ Failed to restore permissions: {e}")
            return False

    def create_monitoring_report(self) -> Dict:
        """Generate comprehensive permission monitoring report."""
        hierarchy_check = self.check_permission_hierarchy()
        
        # Determine overall status
        has_valid_permissions = False
        highest_valid_level = None
        
        # Check in precedence order (enterprise to project)
        precedence_order = [
            "enterprise_macos", "enterprise_linux", 
            "user_global", "user_local", "main_global",
            "project_local", "project_shared"
        ]
        
        for level in precedence_order:
            if hierarchy_check[level]["exists"] and hierarchy_check[level]["valid"]:
                has_valid_permissions = True
                highest_valid_level = level
                break
        
        report = {
            "timestamp": __import__('datetime').datetime.now().isoformat(),
            "overall_status": "✅ PROTECTED" if has_valid_permissions else "🚨 VULNERABLE",
            "highest_valid_level": highest_valid_level,
            "hierarchy_details": hierarchy_check,
            "recommendations": []
        }
        
        # Generate recommendations
        if not has_valid_permissions:
            report["recommendations"].append("🚨 CRITICAL: No valid permissions found - restore immediately")
            report["recommendations"].append("💡 Run: validate_permissions.py --restore")
        
        if hierarchy_check["project_local"]["exists"] and not hierarchy_check["project_local"]["valid"]:
            report["recommendations"].append("⚠️  Project settings vulnerable to auto-restriction")
            report["recommendations"].append("💡 Consider setting user global permissions")
        
        if not hierarchy_check["user_global"]["exists"]:
            report["recommendations"].append("💡 Create user global settings for stronger protection")
        
        return report

def main():
    validator = PermissionValidator()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--restore":
        print("🔧 Restoring project permissions...")
        validator.backup_settings()
        success = validator.restore_project_permissions()
        if success:
            print("✅ Permission restoration complete")
        else:
            print("❌ Permission restoration failed")
        return
    
    print("🛡️  Claude Code Permission Validation Report")
    print("=" * 50)
    
    report = validator.create_monitoring_report()
    
    print(f"📊 Overall Status: {report['overall_status']}")
    print(f"🎯 Highest Valid Level: {report['highest_valid_level']}")
    print()
    
    print("📋 Hierarchy Analysis:")
    for level, details in report["hierarchy_details"].items():
        status_icon = "✅" if details.get("valid") else "❌" if details["exists"] else "⚪"
        print(f"  {status_icon} {level:20} | {'EXISTS' if details['exists'] else 'MISSING':7} | {details['issues'][0] if details['issues'] else 'OK'}")
    
    if report["recommendations"]:
        print()
        print("💡 Recommendations:")
        for rec in report["recommendations"]:
            print(f"  {rec}")
    
    print()
    print("🔧 Usage:")
    print("  python validate_permissions.py           # Check status")
    print("  python validate_permissions.py --restore # Restore permissions")

if __name__ == "__main__":
    main()