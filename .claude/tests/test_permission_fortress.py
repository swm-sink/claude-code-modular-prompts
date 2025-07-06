#!/usr/bin/env python3
"""
🔴 TDD: Test Permission Fortress - RED Phase
Write all tests BEFORE implementation
"""

import json
import os
import pytest
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "tools"))

# This will fail until we implement the module
try:
    from permission_fortress import PermissionFortress
except ImportError:
    PermissionFortress = None


class TestPermissionFortress:
    """Test suite for bulletproof permission protection"""
    
    @pytest.fixture
    def temp_env(self):
        """Create temporary test environment"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Setup test directory structure
            test_root = Path(tmpdir)
            claude_dir = test_root / ".claude"
            claude_dir.mkdir()
            
            # Create mock home directory
            home_dir = test_root / "home"
            home_dir.mkdir()
            home_claude = home_dir / ".claude"
            home_claude.mkdir()
            
            yield {
                "root": test_root,
                "claude_dir": claude_dir,
                "home_dir": home_dir,
                "global_settings": home_claude / "settings.json",
                "local_settings": claude_dir / "settings.local.json"
            }
    
    @pytest.fixture
    def fortress(self, temp_env, monkeypatch):
        """Create fortress instance with mocked paths"""
        if PermissionFortress is None:
            pytest.skip("PermissionFortress not implemented yet")
        
        # Mock paths
        monkeypatch.setattr(Path, "cwd", lambda: temp_env["root"])
        monkeypatch.setattr(Path, "home", lambda: temp_env["home_dir"])
        
        return PermissionFortress()
    
    def test_fortress_initialization(self, fortress, temp_env):
        """Test fortress sets up correctly"""
        assert fortress.project_root == temp_env["root"]
        assert fortress.claude_dir == temp_env["claude_dir"]
        assert fortress.global_settings == temp_env["global_settings"]
        assert fortress.local_settings == temp_env["local_settings"]
        assert fortress.backup_dir.exists()
    
    def test_required_permissions_complete(self, fortress):
        """Test all critical permissions are defined"""
        required = {
            "Bash(*)", "Read(*)", "Edit(*)", "Write(*)", "MultiEdit(*)",
            "Glob(*)", "Grep(*)", "LS(*)", "Task(*)", "WebFetch(*)",
            "WebSearch(*)", "TodoRead(*)", "TodoWrite(*)",
            "NotebookRead(*)", "NotebookEdit(*)", "exit_plan_mode(*)",
            "mcp__ide__getDiagnostics(*)", "mcp__ide__executeCode(*)", "mcp__*"
        }
        assert fortress.REQUIRED_PERMISSIONS == required
    
    def test_dangerous_permissions_blocked(self, fortress):
        """Test dangerous operations are denied"""
        dangerous = {
            "Bash(rm -rf /:*)", "Bash(sudo su:*)", 
            "Bash(dd:*)", "Bash(mkfs:*)"
        }
        assert fortress.DENY_PERMISSIONS == dangerous
    
    def test_check_symlink_health_missing_file(self, fortress):
        """Test symlink health check when file missing"""
        assert fortress.check_symlink_health() is False
    
    def test_check_symlink_health_not_symlink(self, fortress, temp_env):
        """Test symlink health check when file is not symlink"""
        # Create regular file instead of symlink
        with open(temp_env["local_settings"], "w") as f:
            f.write("{}")
        
        assert fortress.check_symlink_health() is False
    
    def test_check_symlink_health_wrong_target(self, fortress, temp_env):
        """Test symlink health check when pointing to wrong target"""
        # Create symlink to wrong location
        wrong_target = temp_env["claude_dir"] / "wrong.json"
        wrong_target.touch()
        temp_env["local_settings"].symlink_to(wrong_target)
        
        assert fortress.check_symlink_health() is False
    
    def test_check_symlink_health_correct(self, fortress, temp_env):
        """Test symlink health check when everything correct"""
        # Create correct symlink
        temp_env["global_settings"].touch()
        temp_env["local_settings"].symlink_to(temp_env["global_settings"])
        
        assert fortress.check_symlink_health() is True
    
    def test_validate_permissions_missing_file(self, fortress, temp_env):
        """Test permission validation with missing file"""
        result = fortress.validate_permissions(temp_env["global_settings"])
        
        assert result["valid"] is False
        assert "error" in result
        assert result["missing_allow"] == fortress.REQUIRED_PERMISSIONS
    
    def test_validate_permissions_incomplete(self, fortress, temp_env):
        """Test permission validation with incomplete permissions"""
        incomplete_settings = {
            "permissions": {
                "allow": ["Bash(*)", "Read(*)"],  # Missing many
                "deny": []  # Missing deny rules
            }
        }
        
        with open(temp_env["global_settings"], "w") as f:
            json.dump(incomplete_settings, f)
        
        result = fortress.validate_permissions(temp_env["global_settings"])
        
        assert result["valid"] is False
        assert len(result["missing_allow"]) > 0
        assert len(result["missing_deny"]) > 0
    
    def test_validate_permissions_complete(self, fortress, temp_env):
        """Test permission validation with complete permissions"""
        complete_settings = {
            "permissions": {
                "allow": list(fortress.REQUIRED_PERMISSIONS),
                "deny": list(fortress.DENY_PERMISSIONS)
            }
        }
        
        with open(temp_env["global_settings"], "w") as f:
            json.dump(complete_settings, f)
        
        result = fortress.validate_permissions(temp_env["global_settings"])
        
        assert result["valid"] is True
        assert len(result["missing_allow"]) == 0
        assert len(result["missing_deny"]) == 0
    
    def test_repair_symlink(self, fortress, temp_env):
        """Test symlink repair functionality"""
        # Create broken situation
        temp_env["local_settings"].touch()
        
        # Repair
        fortress.repair_symlink()
        
        # Verify fixed
        assert temp_env["local_settings"].is_symlink()
        assert temp_env["local_settings"].resolve() == temp_env["global_settings"].resolve()
    
    def test_repair_permissions_creates_backup(self, fortress, temp_env):
        """Test permission repair creates backup"""
        # Create bad settings
        bad_settings = {"permissions": {"allow": ["Bash(*)"], "deny": []}}
        with open(temp_env["global_settings"], "w") as f:
            json.dump(bad_settings, f)
        
        validation = fortress.validate_permissions(temp_env["global_settings"])
        fortress.repair_permissions(temp_env["global_settings"], validation)
        
        # Check backup created
        backups = list(fortress.backup_dir.glob("backup_*.json"))
        assert len(backups) == 1
        
        # Verify backup content
        with open(backups[0]) as f:
            backup_data = json.load(f)
        assert backup_data == bad_settings
    
    def test_repair_permissions_fixes_missing(self, fortress, temp_env):
        """Test permission repair adds missing permissions"""
        # Create incomplete settings
        incomplete = {
            "permissions": {"allow": ["Bash(*)"], "deny": []},
            "env": {"CUSTOM": "value"}
        }
        with open(temp_env["global_settings"], "w") as f:
            json.dump(incomplete, f)
        
        validation = fortress.validate_permissions(temp_env["global_settings"])
        fortress.repair_permissions(temp_env["global_settings"], validation)
        
        # Verify repaired
        with open(temp_env["global_settings"]) as f:
            repaired = json.load(f)
        
        assert set(repaired["permissions"]["allow"]) == fortress.REQUIRED_PERMISSIONS
        assert set(repaired["permissions"]["deny"]) == fortress.DENY_PERMISSIONS
        assert repaired["env"]["CUSTOM"] == "value"  # Preserved
    
    def test_fortress_check_repairs_all_issues(self, fortress, temp_env):
        """Test complete fortress check repairs everything"""
        # Create multiple problems
        # 1. No symlink
        # 2. Bad permissions in global settings
        bad_settings = {"permissions": {"allow": [], "deny": []}}
        with open(temp_env["global_settings"], "w") as f:
            json.dump(bad_settings, f)
        
        # Run fortress check
        result = fortress.fortress_check()
        
        # Verify everything fixed
        assert result is True
        assert temp_env["local_settings"].is_symlink()
        assert temp_env["local_settings"].resolve() == temp_env["global_settings"].resolve()
        
        # Verify permissions fixed
        with open(temp_env["global_settings"]) as f:
            settings = json.load(f)
        assert set(settings["permissions"]["allow"]) == fortress.REQUIRED_PERMISSIONS
    
    @patch("time.sleep", return_value=None)
    def test_monitor_mode_auto_repairs(self, mock_sleep, fortress, temp_env):
        """Test monitor mode detects and repairs issues"""
        # Setup correct state initially
        temp_env["global_settings"].touch()
        temp_env["local_settings"].symlink_to(temp_env["global_settings"])
        
        repair_count = 0
        
        def simulate_corruption():
            nonlocal repair_count
            repair_count += 1
            if repair_count == 2:
                # Corrupt symlink on second check
                temp_env["local_settings"].unlink()
                temp_env["local_settings"].touch()
            elif repair_count >= 5:
                # Stop monitoring after 5 checks
                raise KeyboardInterrupt()
        
        mock_sleep.side_effect = lambda x: simulate_corruption()
        
        # Run monitor
        fortress.monitor_mode(interval=1)
        
        # Verify it repaired the corruption
        assert temp_env["local_settings"].is_symlink()
    
    def test_nuclear_option_complete_reset(self, fortress, temp_env, monkeypatch):
        """Test nuclear option completely resets permissions"""
        # Mock user confirmation
        monkeypatch.setattr("builtins.input", lambda x: "yes")
        
        # Create corrupted state
        bad_settings = {"corrupted": True}
        with open(temp_env["global_settings"], "w") as f:
            json.dump(bad_settings, f)
        temp_env["local_settings"].touch()
        
        # Nuclear reset
        fortress.nuclear_option()
        
        # Verify complete reset
        assert temp_env["local_settings"].is_symlink()
        
        with open(temp_env["global_settings"]) as f:
            settings = json.load(f)
        
        assert set(settings["permissions"]["allow"]) == fortress.REQUIRED_PERMISSIONS
        assert set(settings["permissions"]["deny"]) == fortress.DENY_PERMISSIONS
        assert settings["model"] == "opus"
    
    def test_logging_creates_log_file(self, fortress):
        """Test logging functionality"""
        fortress.log("Test message", "INFO")
        
        assert fortress.log_file.exists()
        
        with open(fortress.log_file) as f:
            content = f.read()
        
        assert "Test message" in content
        assert "[INFO]" in content
    
    def test_cli_interface(self, temp_env, monkeypatch):
        """Test CLI command handling"""
        # Mock sys.argv and paths
        monkeypatch.setattr(Path, "cwd", lambda: temp_env["root"])
        monkeypatch.setattr(Path, "home", lambda: temp_env["home_dir"])
        
        # Test check command
        monkeypatch.setattr("sys.argv", ["permission_fortress.py", "check"])
        from permission_fortress import main
        
        # Should run without error
        main()


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v", "--tb=short"])