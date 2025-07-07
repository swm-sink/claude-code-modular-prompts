#!/usr/bin/env python3
"""
🛡️ PERMISSION MONITOR DAEMON - Continuous Protection
Detects and fixes permission issues before they impact your workflow
"""

import json
import os
import time
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Set, Optional
import signal
import argparse

class PermissionMonitorDaemon:
    """Advanced monitoring with predictive detection"""
    
    def __init__(self):
        self.fortress_path = Path(__file__).parent / "permission_fortress.py"
        self.alert_log = Path(__file__).parent.parent / "permission_alerts.log"
        self.global_settings = Path.home() / ".claude" / "settings.json"
        self.local_settings = Path.cwd() / ".claude" / "settings.local.json"
        self.running = True
        self.check_count = 0
        self.issue_count = 0
        self.last_repair = None
        
    def signal_handler(self, sig, frame):
        """Handle shutdown gracefully"""
        print("\n🛑 Shutting down monitor daemon...")
        self.running = False
        sys.exit(0)
        
    def log_alert(self, message: str, level: str = "INFO"):
        """Log alerts to dedicated file"""
        timestamp = datetime.now().isoformat()
        alert = f"[{timestamp}] [{level}] {message}\n"
        
        # Console output with colors
        colors = {
            "INFO": "\033[94m",
            "SUCCESS": "\033[92m", 
            "WARNING": "\033[93m",
            "CRITICAL": "\033[91m"
        }
        print(f"{colors.get(level, '')}{alert}\033[0m", end="")
        
        # File logging
        with open(self.alert_log, "a") as f:
            f.write(alert)
            
    def detect_permission_degradation(self) -> Dict[str, any]:
        """Detect early signs of permission issues"""
        issues = []
        
        # Check 1: Symlink existence and target
        if not self.local_settings.exists():
            issues.append({
                "type": "MISSING_SYMLINK",
                "severity": "CRITICAL",
                "message": "Local settings symlink missing"
            })
        elif self.local_settings.is_symlink():
            try:
                target = os.readlink(self.local_settings)
                if '/tmp/' in target or '/var/folders/' in target or '/T/' in target:
                    issues.append({
                        "type": "TEMP_HIJACK", 
                        "severity": "CRITICAL",
                        "message": f"Symlink hijacked to temp: {target}"
                    })
            except:
                pass
        elif self.local_settings.is_file():
            issues.append({
                "type": "NOT_SYMLINK",
                "severity": "CRITICAL", 
                "message": "Local settings is regular file, not symlink"
            })
            
        # Check 2: Permission count (early warning)
        try:
            if self.global_settings.exists():
                with open(self.global_settings) as f:
                    settings = json.load(f)
                    perm_count = len(settings.get("permissions", {}).get("allow", []))
                    if perm_count < 15:
                        issues.append({
                            "type": "LOW_PERMISSIONS",
                            "severity": "WARNING",
                            "message": f"Only {perm_count} permissions (expected 20+)"
                        })
        except:
            pass
            
        # Check 3: Recent modification detection
        try:
            if self.local_settings.exists() and not self.local_settings.is_symlink():
                mtime = self.local_settings.stat().st_mtime
                if time.time() - mtime < 60:  # Modified in last minute
                    issues.append({
                        "type": "RECENT_MODIFICATION",
                        "severity": "WARNING",
                        "message": "Local settings recently modified"
                    })
        except:
            pass
            
        return {
            "healthy": len(issues) == 0,
            "issues": issues,
            "check_time": datetime.now().isoformat()
        }
        
    def auto_repair(self, issues: list) -> bool:
        """Automatically fix detected issues"""
        repaired = False
        
        for issue in issues:
            if issue["severity"] == "CRITICAL":
                self.log_alert(f"🚨 Auto-repairing: {issue['message']}", "WARNING")
                
                # Run fortress repair
                try:
                    result = subprocess.run(
                        [sys.executable, str(self.fortress_path), "check"],
                        capture_output=True,
                        text=True
                    )
                    if result.returncode == 0:
                        self.log_alert("✅ Auto-repair successful", "SUCCESS")
                        repaired = True
                        self.last_repair = datetime.now()
                    else:
                        self.log_alert("❌ Auto-repair failed", "CRITICAL")
                except Exception as e:
                    self.log_alert(f"❌ Repair error: {e}", "CRITICAL")
                    
        return repaired
        
    def run_monitor(self, interval: int = 30, auto_fix: bool = True):
        """Main monitoring loop"""
        signal.signal(signal.SIGINT, self.signal_handler)
        
        self.log_alert("🛡️ PERMISSION MONITOR DAEMON STARTED", "INFO")
        self.log_alert(f"Checking every {interval} seconds, auto-fix: {auto_fix}", "INFO")
        
        while self.running:
            self.check_count += 1
            
            # Perform health check
            result = self.detect_permission_degradation()
            
            if not result["healthy"]:
                self.issue_count += 1
                self.log_alert(f"⚠️ Detected {len(result['issues'])} issues", "WARNING")
                
                for issue in result["issues"]:
                    self.log_alert(f"  - [{issue['severity']}] {issue['message']}", issue['severity'])
                
                if auto_fix:
                    if self.auto_repair(result["issues"]):
                        self.log_alert("🔧 Issues resolved automatically", "SUCCESS")
                    else:
                        self.log_alert("❌ Manual intervention required", "CRITICAL")
                        self.log_alert("Run: .claude/tools/emergency_permission_recovery.sh", "INFO")
            else:
                # Periodic health confirmation
                if self.check_count % 10 == 0:
                    self.log_alert(f"✅ All systems healthy (checks: {self.check_count})", "SUCCESS")
                    
            # Sleep until next check
            time.sleep(interval)
            
    def status_report(self):
        """Generate status report"""
        uptime = "N/A"
        if self.last_repair:
            uptime = str(datetime.now() - self.last_repair)
            
        report = f"""
🛡️ PERMISSION MONITOR STATUS
==========================
Checks performed: {self.check_count}
Issues detected: {self.issue_count}
Last repair: {self.last_repair or 'Never'}
Uptime since repair: {uptime}
Alert log: {self.alert_log}
"""
        return report

def main():
    parser = argparse.ArgumentParser(description='Permission Monitor Daemon')
    parser.add_argument('--interval', type=int, default=30, help='Check interval in seconds')
    parser.add_argument('--no-autofix', action='store_true', help='Disable automatic repairs')
    parser.add_argument('--status', action='store_true', help='Show status and exit')
    
    args = parser.parse_args()
    
    daemon = PermissionMonitorDaemon()
    
    if args.status:
        print(daemon.status_report())
    else:
        try:
            daemon.run_monitor(
                interval=args.interval,
                auto_fix=not args.no_autofix
            )
        except KeyboardInterrupt:
            print("\n🛑 Monitor stopped by user")

if __name__ == "__main__":
    main()