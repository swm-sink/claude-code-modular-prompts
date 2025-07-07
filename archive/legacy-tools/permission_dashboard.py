#!/usr/bin/env python3
"""
📊 PERMISSION HEALTH DASHBOARD
Real-time visualization of permission system health
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from rich.layout import Layout
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.align import Align
import time

# Try to import permission_fortress
sys.path.insert(0, str(Path(__file__).parent))
try:
    from permission_fortress import PermissionFortress
except ImportError:
    print("❌ Could not import permission_fortress.py")
    sys.exit(1)


class PermissionDashboard:
    """Real-time permission health monitoring dashboard"""
    
    def __init__(self):
        self.console = Console()
        self.fortress = PermissionFortress()
        self.start_time = datetime.now()
        self.check_count = 0
        self.repair_count = 0
        self.last_check = None
        self.issues_found = []
        
    def create_header(self) -> Panel:
        """Create dashboard header"""
        uptime = datetime.now() - self.start_time
        header_text = f"""[bold cyan]🛡️ PERMISSION FORTRESS DASHBOARD[/bold cyan]
        
[dim]Uptime: {str(uptime).split('.')[0]} | Checks: {self.check_count} | Repairs: {self.repair_count}[/dim]"""
        
        return Panel(
            Align.center(header_text),
            border_style="bright_blue",
            padding=(1, 2)
        )
    
    def create_status_table(self) -> Table:
        """Create system status table"""
        table = Table(title="System Status", show_header=True)
        table.add_column("Component", style="cyan", width=30)
        table.add_column("Status", justify="center", width=15)
        table.add_column("Details", width=50)
        
        # Check symlink
        if self.fortress.local_settings.exists() and self.fortress.local_settings.is_symlink():
            symlink_status = "[green]✅ HEALTHY[/green]"
            symlink_details = f"→ {self.fortress.global_settings}"
        else:
            symlink_status = "[red]❌ BROKEN[/red]"
            symlink_details = "Symlink missing or not configured"
            
        table.add_row("Symlink Health", symlink_status, symlink_details)
        
        # Check global permissions
        global_validation = self.fortress.validate_permissions(self.fortress.global_settings)
        if global_validation["valid"]:
            perm_status = "[green]✅ COMPLETE[/green]"
            perm_details = f"{len(global_validation['current_allow'])} permissions active"
        else:
            perm_status = "[red]❌ INCOMPLETE[/red]"
            perm_details = f"Missing {len(global_validation['missing_allow'])} permissions"
            
        table.add_row("Global Permissions", perm_status, perm_details)
        
        # Check local settings
        if self.fortress.local_settings.exists():
            local_size = self.fortress.local_settings.stat().st_size
            local_status = "[green]✅ EXISTS[/green]"
            local_details = f"Size: {local_size} bytes"
        else:
            local_status = "[yellow]⚠️ MISSING[/yellow]"
            local_details = "Will be created on repair"
            
        table.add_row("Local Settings", local_status, local_details)
        
        # Overall health
        if symlink_status.find("HEALTHY") > 0 and perm_status.find("COMPLETE") > 0:
            overall_status = "[green]✅ FORTRESS SECURE[/green]"
            overall_details = "All systems operational"
        else:
            overall_status = "[red]❌ VULNERABLE[/red]"
            overall_details = "Immediate repair needed"
            
        table.add_row("[bold]Overall Health[/bold]", overall_status, overall_details)
        
        return table
    
    def create_permissions_panel(self) -> Panel:
        """Create permissions overview panel"""
        validation = self.fortress.validate_permissions(self.fortress.global_settings)
        
        if validation.get("error"):
            content = f"[red]Error reading permissions: {validation['error']}[/red]"
        else:
            allowed = validation.get("current_allow", set())
            denied = validation.get("current_deny", set())
            
            content = f"""[bold cyan]Active Permissions:[/bold cyan]
[green]✓[/green] {len(allowed)} allowed patterns
[red]✗[/red] {len(denied)} denied patterns

[bold cyan]Critical Permissions:[/bold cyan]"""
            
            critical = ["Bash(*)", "Read(*)", "Write(*)", "Edit(*)"]
            for perm in critical:
                if perm in allowed:
                    content += f"\n[green]✓[/green] {perm}"
                else:
                    content += f"\n[red]✗[/red] {perm} [red]MISSING![/red]"
                    
        return Panel(content, title="Permission Status", border_style="cyan")
    
    def create_activity_log(self) -> Panel:
        """Create recent activity panel"""
        log_file = self.fortress.log_file
        recent_lines = []
        
        if log_file.exists():
            with open(log_file) as f:
                lines = f.readlines()
                recent_lines = lines[-10:]  # Last 10 entries
                
        if recent_lines:
            content = ""
            for line in recent_lines:
                if "[ERROR]" in line:
                    content += f"[red]{line.strip()}[/red]\n"
                elif "[WARNING]" in line:
                    content += f"[yellow]{line.strip()}[/yellow]\n"
                elif "[SUCCESS]" in line:
                    content += f"[green]{line.strip()}[/green]\n"
                else:
                    content += f"[dim]{line.strip()}[/dim]\n"
        else:
            content = "[dim]No recent activity[/dim]"
            
        return Panel(content.strip(), title="Recent Activity", border_style="blue")
    
    def create_recommendations(self) -> Panel:
        """Create recommendations panel"""
        recommendations = []
        
        # Check various conditions
        validation = self.fortress.validate_permissions(self.fortress.global_settings)
        
        if not validation["valid"]:
            recommendations.append("🚨 [red]Run 'fortress check' to repair permissions[/red]")
            
        if not self.fortress.local_settings.exists():
            recommendations.append("⚠️ [yellow]Local settings missing - will auto-repair[/yellow]")
            
        if not self.fortress.local_settings.is_symlink() and self.fortress.local_settings.exists():
            recommendations.append("❌ [red]Local settings is not a symlink! Run repair immediately[/red]")
            
        # Check for monitoring
        monitor_running = os.popen("pgrep -f 'permission_fortress.py monitor'").read().strip()
        if not monitor_running:
            recommendations.append("💡 [cyan]Consider starting monitor: 'fortress monitor'[/cyan]")
            
        if not recommendations:
            recommendations.append("✅ [green]All systems healthy - no action needed[/green]")
            
        content = "\n".join(recommendations)
        return Panel(content, title="Recommendations", border_style="yellow")
    
    def run_check(self):
        """Run a fortress check"""
        self.check_count += 1
        self.last_check = datetime.now()
        
        # Quick checks
        if not self.fortress.check_symlink_health():
            self.issues_found.append(f"[{self.last_check.strftime('%H:%M:%S')}] Symlink broken")
            self.repair_count += 1
            self.fortress.repair_symlink()
            
        validation = self.fortress.validate_permissions(self.fortress.global_settings)
        if not validation["valid"]:
            self.issues_found.append(f"[{self.last_check.strftime('%H:%M:%S')}] Permissions incomplete")
            self.repair_count += 1
            self.fortress.repair_permissions(self.fortress.global_settings, validation)
    
    def create_layout(self) -> Layout:
        """Create dashboard layout"""
        layout = Layout()
        
        layout.split_column(
            Layout(self.create_header(), size=5),
            Layout(name="main"),
            Layout(self.create_recommendations(), size=7)
        )
        
        layout["main"].split_row(
            Layout(self.create_status_table()),
            Layout(self.create_permissions_panel())
        )
        
        return layout
    
    def run_dashboard(self, refresh_interval: int = 5):
        """Run the dashboard with live updates"""
        self.console.print("\n[bold cyan]Starting Permission Dashboard...[/bold cyan]\n")
        
        with Live(self.create_layout(), refresh_per_second=1, console=self.console) as live:
            try:
                while True:
                    # Run check
                    self.run_check()
                    
                    # Update display
                    live.update(self.create_layout())
                    
                    # Wait for next check
                    time.sleep(refresh_interval)
                    
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Dashboard stopped by user[/yellow]")
                self.console.print(f"[dim]Total checks: {self.check_count} | Total repairs: {self.repair_count}[/dim]")


def main():
    """CLI entry point"""
    dashboard = PermissionDashboard()
    
    if len(sys.argv) > 1:
        try:
            interval = int(sys.argv[1])
        except ValueError:
            interval = 5
    else:
        interval = 5
        
    dashboard.run_dashboard(refresh_interval=interval)


if __name__ == "__main__":
    main()