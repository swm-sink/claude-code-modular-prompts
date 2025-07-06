#!/usr/bin/env python3
"""
Pipeline Scheduler
Automated scheduling and execution of continuous improvement pipeline cycles.
"""

import json
import logging
import schedule
import time
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional
import subprocess
import threading
from dataclasses import dataclass

@dataclass
class ScheduleConfig:
    enabled: bool
    time: str
    timezone: str = "UTC"
    day: Optional[str] = None  # For weekly schedules
    day_of_month: Optional[int] = None  # For monthly schedules

class PipelineScheduler:
    """Automated scheduler for continuous improvement pipeline."""
    
    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or Path(".claude/pipeline_config.json")
        self.logs_path = Path(".claude/logs")
        self.logs_path.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.logs_path / 'scheduler.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Load configuration
        self.config = self._load_config()
        
        # Pipeline execution tracking
        self.execution_history = []
        self.running = False
        
    def _load_config(self) -> Dict[str, Any]:
        """Load scheduler configuration."""
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            return config.get('scheduling', {})
        except Exception as e:
            self.logger.error(f"Failed to load config: {e}")
            return self._default_config()
    
    def _default_config(self) -> Dict[str, Any]:
        """Return default scheduling configuration."""
        return {
            "daily_monitoring": {
                "enabled": True,
                "time": "02:00",
                "timezone": "UTC"
            },
            "weekly_optimization": {
                "enabled": True,
                "day": "Sunday",
                "time": "04:00", 
                "timezone": "UTC"
            },
            "monthly_analysis": {
                "enabled": True,
                "day": 1,
                "time": "06:00",
                "timezone": "UTC"
            }
        }
    
    def setup_schedules(self):
        """Setup all scheduled pipeline executions."""
        self.logger.info("Setting up pipeline schedules...")
        
        # Daily monitoring schedule
        daily_config = self.config.get('daily_monitoring', {})
        if daily_config.get('enabled', False):
            schedule_time = daily_config.get('time', '02:00')
            schedule.every().day.at(schedule_time).do(self._run_daily_monitoring)
            self.logger.info(f"Scheduled daily monitoring at {schedule_time}")
        
        # Weekly optimization schedule
        weekly_config = self.config.get('weekly_optimization', {})
        if weekly_config.get('enabled', False):
            schedule_day = weekly_config.get('day', 'sunday').lower()
            schedule_time = weekly_config.get('time', '04:00')
            
            if schedule_day == 'monday':
                schedule.every().monday.at(schedule_time).do(self._run_weekly_optimization)
            elif schedule_day == 'tuesday':
                schedule.every().tuesday.at(schedule_time).do(self._run_weekly_optimization)
            elif schedule_day == 'wednesday':
                schedule.every().wednesday.at(schedule_time).do(self._run_weekly_optimization)
            elif schedule_day == 'thursday':
                schedule.every().thursday.at(schedule_time).do(self._run_weekly_optimization)
            elif schedule_day == 'friday':
                schedule.every().friday.at(schedule_time).do(self._run_weekly_optimization)
            elif schedule_day == 'saturday':
                schedule.every().saturday.at(schedule_time).do(self._run_weekly_optimization)
            else:  # Default to Sunday
                schedule.every().sunday.at(schedule_time).do(self._run_weekly_optimization)
            
            self.logger.info(f"Scheduled weekly optimization on {schedule_day} at {schedule_time}")
        
        # Monthly analysis schedule
        monthly_config = self.config.get('monthly_analysis', {})
        if monthly_config.get('enabled', False):
            # Note: schedule library doesn't directly support monthly schedules
            # We'll check for monthly schedule in the daily monitoring
            self.logger.info("Monthly analysis will be checked during daily monitoring")
        
        self.logger.info("All schedules configured successfully")
    
    def _run_daily_monitoring(self):
        """Execute daily monitoring pipeline."""
        self.logger.info("Starting daily monitoring pipeline...")
        
        try:
            # Check if it's time for monthly analysis
            self._check_monthly_analysis()
            
            # Run metrics collection
            result = self._execute_pipeline_command(['--collect-metrics'])
            
            if result.returncode == 0:
                self.logger.info("Daily monitoring completed successfully")
                self._record_execution('daily_monitoring', 'success')
            else:
                self.logger.error(f"Daily monitoring failed: {result.stderr}")
                self._record_execution('daily_monitoring', 'failed')
                
        except Exception as e:
            self.logger.error(f"Daily monitoring error: {e}")
            self._record_execution('daily_monitoring', 'error')
    
    def _run_weekly_optimization(self):
        """Execute weekly optimization pipeline."""
        self.logger.info("Starting weekly optimization pipeline...")
        
        try:
            # Run full pipeline cycle
            result = self._execute_pipeline_command(['--run-cycle'])
            
            if result.returncode == 0:
                self.logger.info("Weekly optimization completed successfully")
                self._record_execution('weekly_optimization', 'success')
                
                # Parse results for reporting
                try:
                    output = json.loads(result.stdout)
                    self._generate_weekly_report(output)
                except json.JSONDecodeError:
                    self.logger.warning("Could not parse pipeline output for reporting")
                    
            else:
                self.logger.error(f"Weekly optimization failed: {result.stderr}")
                self._record_execution('weekly_optimization', 'failed')
                
        except Exception as e:
            self.logger.error(f"Weekly optimization error: {e}")
            self._record_execution('weekly_optimization', 'error')
    
    def _check_monthly_analysis(self):
        """Check if monthly analysis should be executed."""
        monthly_config = self.config.get('monthly_analysis', {})
        if not monthly_config.get('enabled', False):
            return
        
        now = datetime.now()
        target_day = monthly_config.get('day', 1)
        target_time = monthly_config.get('time', '06:00')
        
        # Check if today is the target day of the month
        if now.day == target_day:
            target_hour, target_minute = map(int, target_time.split(':'))
            
            # Check if we're within the target time window (±30 minutes)
            target_datetime = now.replace(hour=target_hour, minute=target_minute)
            time_diff = abs((now - target_datetime).total_seconds())
            
            if time_diff <= 1800:  # Within 30 minutes
                self._run_monthly_analysis()
    
    def _run_monthly_analysis(self):
        """Execute monthly analysis pipeline."""
        self.logger.info("Starting monthly analysis pipeline...")
        
        try:
            # Run trend analysis
            result = self._execute_pipeline_command(['--analyze-trends'])
            
            if result.returncode == 0:
                self.logger.info("Monthly analysis completed successfully")
                self._record_execution('monthly_analysis', 'success')
                
                # Generate comprehensive monthly report
                try:
                    trends_output = json.loads(result.stdout)
                    self._generate_monthly_report(trends_output)
                except json.JSONDecodeError:
                    self.logger.warning("Could not parse trends output for reporting")
                    
            else:
                self.logger.error(f"Monthly analysis failed: {result.stderr}")
                self._record_execution('monthly_analysis', 'failed')
                
        except Exception as e:
            self.logger.error(f"Monthly analysis error: {e}")
            self._record_execution('monthly_analysis', 'error')
    
    def _execute_pipeline_command(self, args: list) -> subprocess.CompletedProcess:
        """Execute pipeline command with given arguments."""
        pipeline_script = Path(".claude/tools/continuous_improvement_pipeline.py")
        
        cmd = [sys.executable, str(pipeline_script)] + args
        
        self.logger.info(f"Executing command: {' '.join(cmd)}")
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=3600  # 1 hour timeout
        )
        
        return result
    
    def _record_execution(self, execution_type: str, status: str):
        """Record pipeline execution for history tracking."""
        execution_record = {
            'type': execution_type,
            'status': status,
            'timestamp': datetime.now().isoformat(),
            'scheduler_version': '1.0.0'
        }
        
        self.execution_history.append(execution_record)
        
        # Save to file
        history_file = self.logs_path / 'execution_history.json'
        
        try:
            # Load existing history
            if history_file.exists():
                with open(history_file, 'r') as f:
                    all_history = json.load(f)
            else:
                all_history = []
            
            # Add new record
            all_history.append(execution_record)
            
            # Keep only last 1000 records
            if len(all_history) > 1000:
                all_history = all_history[-1000:]
            
            # Save updated history
            with open(history_file, 'w') as f:
                json.dump(all_history, f, indent=2)
                
        except Exception as e:
            self.logger.error(f"Failed to save execution history: {e}")
    
    def _generate_weekly_report(self, pipeline_results: Dict[str, Any]):
        """Generate weekly optimization report."""
        report = {
            'report_type': 'weekly_optimization',
            'generated_at': datetime.now().isoformat(),
            'period': self._get_week_period(),
            'pipeline_results': pipeline_results,
            'summary': {
                'improvements_executed': pipeline_results.get('improvements_executed', 0),
                'improvements_successful': pipeline_results.get('improvements_successful', 0),
                'improvements_failed': pipeline_results.get('improvements_failed', 0),
                'success_rate': 0
            }
        }
        
        # Calculate success rate
        total = report['summary']['improvements_executed']
        if total > 0:
            report['summary']['success_rate'] = report['summary']['improvements_successful'] / total
        
        # Save report
        reports_path = Path(".claude/reports")
        reports_path.mkdir(parents=True, exist_ok=True)
        
        week_str = datetime.now().strftime('%Y-W%W')
        report_file = reports_path / f"weekly_report_{week_str}.json"
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        self.logger.info(f"Weekly report generated: {report_file}")
        
        # Create GitHub issue with weekly summary
        self._create_weekly_github_issue(report)
    
    def _generate_monthly_report(self, trends_data: list):
        """Generate monthly analysis report."""
        report = {
            'report_type': 'monthly_analysis',
            'generated_at': datetime.now().isoformat(),
            'period': self._get_month_period(),
            'trends_analysis': trends_data,
            'summary': {
                'opportunities_identified': len(trends_data),
                'high_priority_opportunities': len([t for t in trends_data if t.get('priority') == 'high']),
                'critical_opportunities': len([t for t in trends_data if t.get('priority') == 'critical'])
            }
        }
        
        # Save report
        reports_path = Path(".claude/reports")
        reports_path.mkdir(parents=True, exist_ok=True)
        
        month_str = datetime.now().strftime('%Y-%m')
        report_file = reports_path / f"monthly_report_{month_str}.json"
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        self.logger.info(f"Monthly report generated: {report_file}")
        
        # Create GitHub issue with monthly summary
        self._create_monthly_github_issue(report)
    
    def _get_week_period(self) -> Dict[str, str]:
        """Get current week period."""
        now = datetime.now()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        
        return {
            'start': start_of_week.strftime('%Y-%m-%d'),
            'end': end_of_week.strftime('%Y-%m-%d')
        }
    
    def _get_month_period(self) -> Dict[str, str]:
        """Get current month period."""
        now = datetime.now()
        start_of_month = now.replace(day=1)
        
        # Get last day of month
        if now.month == 12:
            next_month = now.replace(year=now.year + 1, month=1)
        else:
            next_month = now.replace(month=now.month + 1)
        
        end_of_month = next_month - timedelta(days=1)
        
        return {
            'start': start_of_month.strftime('%Y-%m-%d'),
            'end': end_of_month.strftime('%Y-%m-%d')
        }
    
    def _create_weekly_github_issue(self, report: Dict[str, Any]):
        """Create GitHub issue with weekly report summary."""
        try:
            summary = report['summary']
            period = report['period']
            
            title = f"Weekly Optimization Report - {period['start']} to {period['end']}"
            
            body = f"""
# Weekly Continuous Improvement Report

**Period:** {period['start']} to {period['end']}
**Generated:** {report['generated_at']}

## Summary
- **Improvements Executed:** {summary['improvements_executed']}
- **Successful:** {summary['improvements_successful']}
- **Failed:** {summary['improvements_failed']}
- **Success Rate:** {summary['success_rate']:.1%}

## Pipeline Results
```json
{json.dumps(report['pipeline_results'], indent=2)}
```

---
*This report was automatically generated by the Continuous Improvement Pipeline Scheduler*
"""
            
            subprocess.run([
                'gh', 'issue', 'create',
                '--title', title,
                '--body', body,
                '--label', 'report',
                '--label', 'weekly',
                '--label', 'automated'
            ], check=True)
            
            self.logger.info("Weekly GitHub issue created successfully")
            
        except Exception as e:
            self.logger.warning(f"Failed to create weekly GitHub issue: {e}")
    
    def _create_monthly_github_issue(self, report: Dict[str, Any]):
        """Create GitHub issue with monthly report summary."""
        try:
            summary = report['summary']
            period = report['period']
            
            title = f"Monthly Analysis Report - {period['start']} to {period['end']}"
            
            body = f"""
# Monthly Continuous Improvement Analysis

**Period:** {period['start']} to {period['end']}
**Generated:** {report['generated_at']}

## Summary
- **Opportunities Identified:** {summary['opportunities_identified']}
- **High Priority:** {summary['high_priority_opportunities']}
- **Critical:** {summary['critical_opportunities']}

## Trend Analysis Results
```json
{json.dumps(report['trends_analysis'], indent=2)}
```

---
*This report was automatically generated by the Continuous Improvement Pipeline Scheduler*
"""
            
            subprocess.run([
                'gh', 'issue', 'create',
                '--title', title,
                '--body', body,
                '--label', 'report',
                '--label', 'monthly',
                '--label', 'analysis',
                '--label', 'automated'
            ], check=True)
            
            self.logger.info("Monthly GitHub issue created successfully")
            
        except Exception as e:
            self.logger.warning(f"Failed to create monthly GitHub issue: {e}")
    
    def run_scheduler(self):
        """Run the scheduler main loop."""
        self.logger.info("Starting pipeline scheduler...")
        self.running = True
        
        # Setup schedules
        self.setup_schedules()
        
        try:
            while self.running:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
                
        except KeyboardInterrupt:
            self.logger.info("Scheduler stopped by user")
        except Exception as e:
            self.logger.error(f"Scheduler error: {e}")
        finally:
            self.running = False
            self.logger.info("Pipeline scheduler stopped")
    
    def stop_scheduler(self):
        """Stop the scheduler."""
        self.running = False
    
    def get_status(self) -> Dict[str, Any]:
        """Get current scheduler status."""
        return {
            'running': self.running,
            'scheduled_jobs': len(schedule.jobs),
            'last_executions': self.execution_history[-5:] if self.execution_history else [],
            'next_run': str(schedule.next_run()) if schedule.jobs else None
        }

def main():
    """Main entry point for the pipeline scheduler."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Pipeline Scheduler")
    parser.add_argument('--config', type=Path, help="Configuration file path")
    parser.add_argument('--daemon', action='store_true', help="Run as daemon")
    parser.add_argument('--status', action='store_true', help="Show scheduler status")
    parser.add_argument('--test-weekly', action='store_true', help="Test weekly optimization")
    parser.add_argument('--test-monthly', action='store_true', help="Test monthly analysis")
    
    args = parser.parse_args()
    
    scheduler = PipelineScheduler(config_path=args.config)
    
    if args.status:
        status = scheduler.get_status()
        print(json.dumps(status, indent=2))
    elif args.test_weekly:
        scheduler._run_weekly_optimization()
    elif args.test_monthly:
        scheduler._run_monthly_analysis()
    elif args.daemon:
        scheduler.run_scheduler()
    else:
        print("Please specify an action: --daemon, --status, --test-weekly, or --test-monthly")
        sys.exit(1)

if __name__ == "__main__":
    main()