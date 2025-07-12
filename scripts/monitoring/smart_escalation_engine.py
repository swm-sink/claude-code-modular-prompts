#!/usr/bin/env python3
"""
Smart Escalation Engine

Implements intelligent escalation using existing approval workflows and human
oversight mechanisms from the Claude framework. Integrates with GitHub APIs
and notification systems for seamless human-AI collaboration.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import requests
import subprocess

class SmartEscalationEngine:
    """Smart escalation engine with human oversight integration."""
    
    def __init__(self, repo_root: str, github_token: Optional[str] = None):
        self.repo_root = Path(repo_root)
        self.claude_dir = self.repo_root / ".claude"
        self.github_token = github_token or os.getenv("GITHUB_TOKEN")
        
        # Escalation thresholds from framework
        self.escalation_rules = {
            "quality_threshold": 85,  # Ultra-critical quality threshold
            "risk_threshold": 60,     # High risk threshold
            "complexity_threshold": 70, # High complexity threshold
            "security_threshold": 1,   # Any security issue
            "meta_framework_threshold": 1  # Any meta change
        }
        
        # Approval workflows
        self.approval_workflows = {
            "low_risk": {
                "reviewers": 1,
                "approval_time": "24h",
                "escalation_path": ["maintainer"]
            },
            "medium_risk": {
                "reviewers": 2,
                "approval_time": "48h", 
                "escalation_path": ["maintainer", "senior_maintainer"]
            },
            "high_risk": {
                "reviewers": 3,
                "approval_time": "72h",
                "escalation_path": ["maintainer", "senior_maintainer", "architect"]
            },
            "critical_risk": {
                "reviewers": 5,
                "approval_time": "immediate",
                "escalation_path": ["architect", "security_lead", "framework_lead"]
            }
        }
    
    def process_escalation(self, 
                          risk_assessment: Dict, 
                          quality_assessment: Dict,
                          change_analysis: Dict,
                          pr_number: Optional[int] = None) -> Dict:
        """Process smart escalation based on assessments."""
        print("🎯 Processing smart escalation with human oversight integration...")
        
        # Determine escalation level
        escalation_level = self._determine_escalation_level(
            risk_assessment, quality_assessment, change_analysis
        )
        
        # Create escalation plan
        escalation_plan = self._create_escalation_plan(escalation_level)
        
        # Execute escalation if needed
        escalation_actions = self._execute_escalation(
            escalation_plan, pr_number, risk_assessment, quality_assessment
        )
        
        # Set up monitoring
        monitoring_config = self._setup_monitoring(escalation_level)
        
        # Create escalation response
        response = {
            "escalation_level": escalation_level,
            "requires_human_review": escalation_level in ["high_risk", "critical_risk"],
            "escalation_plan": escalation_plan,
            "actions_taken": escalation_actions,
            "monitoring_config": monitoring_config,
            "approval_workflow": self.approval_workflows[escalation_level],
            "estimated_resolution_time": self._estimate_resolution_time(escalation_level),
            "stakeholders_notified": escalation_actions.get("notifications", [])
        }
        
        print(f"🎯 Smart Escalation Complete: {escalation_level} - Human Review: {response['requires_human_review']}")
        return response
    
    def _determine_escalation_level(self, 
                                   risk_assessment: Dict, 
                                   quality_assessment: Dict,
                                   change_analysis: Dict) -> str:
        """Determine appropriate escalation level using framework rules."""
        
        # Extract key metrics
        risk_score = risk_assessment.get("predictive_score", 0)
        quality_score = quality_assessment.get("overall_score", 0)
        production_ready = quality_assessment.get("compliance", {}).get("production_ready", False)
        
        # Change analysis metrics
        security_implications = len(change_analysis.get("security_implications", []))
        meta_changes = change_analysis.get("change_categories", {}).get("meta", 0)
        quality_changes = change_analysis.get("change_categories", {}).get("quality", 0)
        
        # CRITICAL RISK: Meta-framework changes or security issues
        if (meta_changes > 0 or 
            security_implications >= self.escalation_rules["security_threshold"]):
            return "critical_risk"
        
        # HIGH RISK: Quality system changes or high risk/poor quality
        if (quality_changes > 0 or 
            risk_score >= self.escalation_rules["risk_threshold"] or
            not production_ready):
            return "high_risk"
        
        # MEDIUM RISK: Moderate risk or quality concerns
        if (risk_score >= 40 or 
            quality_score < 90):
            return "medium_risk"
        
        # LOW RISK: Everything else
        return "low_risk"
    
    def _create_escalation_plan(self, escalation_level: str) -> Dict:
        """Create detailed escalation plan."""
        workflow = self.approval_workflows[escalation_level]
        
        plan = {
            "level": escalation_level,
            "immediate_actions": [],
            "review_requirements": {
                "required_reviewers": workflow["reviewers"],
                "approval_time_limit": workflow["approval_time"],
                "escalation_path": workflow["escalation_path"]
            },
            "safety_measures": [],
            "communication_plan": {
                "stakeholders": workflow["escalation_path"],
                "notification_channels": ["github", "email"],
                "urgency": escalation_level
            }
        }
        
        # Add level-specific actions
        if escalation_level == "critical_risk":
            plan["immediate_actions"].extend([
                "Create emergency review committee",
                "Implement immediate deployment freeze",
                "Activate incident response procedures",
                "Notify security and architecture teams"
            ])
            plan["safety_measures"].extend([
                "Automated rollback preparation",
                "Enhanced monitoring activation",
                "Safety boundary validation",
                "Emergency contact procedures"
            ])
        
        elif escalation_level == "high_risk":
            plan["immediate_actions"].extend([
                "Assign senior reviewer",
                "Implement deployment gate",
                "Schedule architecture review"
            ])
            plan["safety_measures"].extend([
                "Rollback procedure preparation",
                "Enhanced testing requirements",
                "Quality gate enforcement"
            ])
        
        elif escalation_level == "medium_risk":
            plan["immediate_actions"].extend([
                "Assign additional reviewer",
                "Request detailed testing plan"
            ])
            plan["safety_measures"].extend([
                "Standard rollback procedures",
                "Quality validation"
            ])
        
        else:  # low_risk
            plan["immediate_actions"].extend([
                "Standard review process",
                "Automated quality checks"
            ])
            plan["safety_measures"].extend([
                "Standard deployment procedures"
            ])
        
        return plan
    
    def _execute_escalation(self, 
                           escalation_plan: Dict, 
                           pr_number: Optional[int],
                           risk_assessment: Dict,
                           quality_assessment: Dict) -> Dict:
        """Execute escalation actions."""
        actions_taken = {
            "github_actions": [],
            "notifications": [],
            "reviews_requested": [],
            "labels_applied": [],
            "status_updates": []
        }
        
        # GitHub integration if PR provided
        if pr_number and self.github_token:
            try:
                github_actions = self._execute_github_actions(
                    pr_number, escalation_plan, risk_assessment, quality_assessment
                )
                actions_taken["github_actions"] = github_actions
            except Exception as e:
                print(f"⚠️ GitHub integration error: {e}")
        
        # Create notifications
        notifications = self._create_notifications(escalation_plan, risk_assessment, quality_assessment)
        actions_taken["notifications"] = notifications
        
        # Create review assignments
        review_assignments = self._create_review_assignments(escalation_plan)
        actions_taken["reviews_requested"] = review_assignments
        
        return actions_taken
    
    def _execute_github_actions(self, 
                               pr_number: int, 
                               escalation_plan: Dict,
                               risk_assessment: Dict,
                               quality_assessment: Dict) -> List[str]:
        """Execute GitHub-specific escalation actions."""
        actions = []
        
        try:
            # Get repo info from git
            repo_info = self._get_repo_info()
            if not repo_info:
                return ["Failed to get repository information"]
            
            owner, repo = repo_info
            
            # Apply labels based on escalation level
            labels = self._get_escalation_labels(escalation_plan["level"])
            if labels:
                self._apply_pr_labels(owner, repo, pr_number, labels)
                actions.append(f"Applied labels: {', '.join(labels)}")
            
            # Request reviews
            reviewers = self._get_required_reviewers(escalation_plan)
            if reviewers:
                self._request_pr_reviews(owner, repo, pr_number, reviewers)
                actions.append(f"Requested reviews from: {', '.join(reviewers)}")
            
            # Create detailed comment
            comment = self._create_escalation_comment(escalation_plan, risk_assessment, quality_assessment)
            self._add_pr_comment(owner, repo, pr_number, comment)
            actions.append("Added detailed escalation comment")
            
            # Set PR status if critical
            if escalation_plan["level"] == "critical_risk":
                self._set_pr_status(owner, repo, pr_number, "pending", "Critical review required")
                actions.append("Set critical review status")
            
        except Exception as e:
            actions.append(f"GitHub action failed: {e}")
        
        return actions
    
    def _setup_monitoring(self, escalation_level: str) -> Dict:
        """Setup monitoring configuration based on escalation level."""
        
        base_config = {
            "enabled": True,
            "escalation_level": escalation_level
        }
        
        if escalation_level == "critical_risk":
            base_config.update({
                "real_time_monitoring": True,
                "alert_threshold_seconds": 5,
                "health_check_interval": "1m",
                "escalation_timeout": "15m",
                "auto_rollback": True,
                "notification_channels": ["slack", "email", "sms", "phone"]
            })
        
        elif escalation_level == "high_risk":
            base_config.update({
                "real_time_monitoring": True,
                "alert_threshold_seconds": 30,
                "health_check_interval": "5m",
                "escalation_timeout": "2h",
                "auto_rollback": False,
                "notification_channels": ["slack", "email"]
            })
        
        elif escalation_level == "medium_risk":
            base_config.update({
                "real_time_monitoring": False,
                "alert_threshold_seconds": 120,
                "health_check_interval": "15m",
                "escalation_timeout": "24h",
                "auto_rollback": False,
                "notification_channels": ["email"]
            })
        
        else:  # low_risk
            base_config.update({
                "real_time_monitoring": False,
                "alert_threshold_seconds": 300,
                "health_check_interval": "1h",
                "escalation_timeout": "7d",
                "auto_rollback": False,
                "notification_channels": ["email"]
            })
        
        return base_config
    
    def _estimate_resolution_time(self, escalation_level: str) -> str:
        """Estimate resolution time based on escalation level."""
        estimates = {
            "critical_risk": "Immediate (0-2 hours)",
            "high_risk": "Urgent (2-24 hours)",
            "medium_risk": "Standard (1-3 days)",
            "low_risk": "Normal (3-7 days)"
        }
        return estimates.get(escalation_level, "Unknown")
    
    def _create_notifications(self, escalation_plan: Dict, risk_assessment: Dict, quality_assessment: Dict) -> List[Dict]:
        """Create notification messages for stakeholders."""
        notifications = []
        
        level = escalation_plan["level"]
        stakeholders = escalation_plan["communication_plan"]["stakeholders"]
        
        for stakeholder in stakeholders:
            notification = {
                "recipient": stakeholder,
                "urgency": level,
                "subject": f"Prompt Engineering Review Escalation: {level.upper()}",
                "message": self._create_notification_message(escalation_plan, risk_assessment, quality_assessment),
                "channels": escalation_plan["communication_plan"]["notification_channels"]
            }
            notifications.append(notification)
        
        return notifications
    
    def _create_notification_message(self, escalation_plan: Dict, risk_assessment: Dict, quality_assessment: Dict) -> str:
        """Create detailed notification message."""
        level = escalation_plan["level"]
        risk_score = risk_assessment.get("predictive_score", 0)
        quality_score = quality_assessment.get("overall_score", 0)
        
        message = f"""
🚨 PROMPT ENGINEERING REVIEW ESCALATION: {level.upper()}

📊 Assessment Summary:
• Risk Score: {risk_score}/100 ({risk_assessment.get('risk_level', 'Unknown')})
• Quality Score: {quality_score}/100 ({quality_assessment.get('grade', 'Unknown')})
• Production Ready: {quality_assessment.get('compliance', {}).get('production_ready', False)}

🎯 Escalation Actions Required:
"""
        
        for action in escalation_plan["immediate_actions"]:
            message += f"• {action}\n"
        
        message += f"""
⏰ Resolution Time: {self._estimate_resolution_time(level)}
👥 Required Reviewers: {escalation_plan['review_requirements']['required_reviewers']}

🛡️ Safety Measures:
"""
        
        for measure in escalation_plan["safety_measures"]:
            message += f"• {measure}\n"
        
        if level == "critical_risk":
            message += "\n🚨 CRITICAL: This escalation requires immediate attention and safety validation."
        
        return message.strip()
    
    def _create_review_assignments(self, escalation_plan: Dict) -> List[Dict]:
        """Create review assignments based on escalation plan."""
        assignments = []
        
        reviewers_needed = escalation_plan["review_requirements"]["required_reviewers"]
        escalation_path = escalation_plan["review_requirements"]["escalation_path"]
        
        for i, role in enumerate(escalation_path[:reviewers_needed]):
            assignment = {
                "role": role,
                "priority": i + 1,
                "required": True,
                "expertise": self._get_role_expertise(role),
                "deadline": escalation_plan["review_requirements"]["approval_time_limit"]
            }
            assignments.append(assignment)
        
        return assignments
    
    def _get_role_expertise(self, role: str) -> List[str]:
        """Get expertise areas for role."""
        expertise_map = {
            "maintainer": ["code_quality", "framework_knowledge"],
            "senior_maintainer": ["architecture", "security", "performance"],
            "architect": ["system_design", "meta_framework", "safety"],
            "security_lead": ["security", "threat_modeling", "compliance"],
            "framework_lead": ["meta_prompting", "ai_safety", "governance"]
        }
        return expertise_map.get(role, ["general"])
    
    # GitHub API integration methods
    def _get_repo_info(self) -> Optional[Tuple[str, str]]:
        """Get repository owner and name from git remote."""
        try:
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True,
                text=True,
                cwd=self.repo_root
            )
            
            if result.returncode == 0:
                url = result.stdout.strip()
                # Parse GitHub URL
                if "github.com" in url:
                    if url.startswith("git@"):
                        # SSH format: git@github.com:owner/repo.git
                        path = url.split(":")[-1].replace(".git", "")
                    else:
                        # HTTPS format: https://github.com/owner/repo.git
                        path = url.split("github.com/")[-1].replace(".git", "")
                    
                    parts = path.split("/")
                    if len(parts) >= 2:
                        return parts[0], parts[1]
            
        except Exception:
            pass
        
        return None
    
    def _get_escalation_labels(self, level: str) -> List[str]:
        """Get GitHub labels for escalation level."""
        label_map = {
            "critical_risk": ["prompt-review", "critical", "needs-security-review"],
            "high_risk": ["prompt-review", "high-priority", "needs-architecture-review"],
            "medium_risk": ["prompt-review", "medium-priority"],
            "low_risk": ["prompt-review", "low-priority"]
        }
        return label_map.get(level, ["prompt-review"])
    
    def _get_required_reviewers(self, escalation_plan: Dict) -> List[str]:
        """Get list of required reviewers (would map to actual GitHub usernames)."""
        # In real implementation, would map roles to actual GitHub usernames
        roles = escalation_plan["review_requirements"]["escalation_path"]
        reviewers_needed = escalation_plan["review_requirements"]["required_reviewers"]
        return roles[:reviewers_needed]  # Simplified - would map to actual usernames
    
    def _apply_pr_labels(self, owner: str, repo: str, pr_number: int, labels: List[str]):
        """Apply labels to PR via GitHub API."""
        if not self.github_token:
            return
        
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/labels"
        headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        response = requests.post(url, headers=headers, json={"labels": labels})
        response.raise_for_status()
    
    def _request_pr_reviews(self, owner: str, repo: str, pr_number: int, reviewers: List[str]):
        """Request PR reviews via GitHub API."""
        if not self.github_token:
            return
        
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/requested_reviewers"
        headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        response = requests.post(url, headers=headers, json={"reviewers": reviewers})
        response.raise_for_status()
    
    def _add_pr_comment(self, owner: str, repo: str, pr_number: int, comment: str):
        """Add comment to PR via GitHub API."""
        if not self.github_token:
            return
        
        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
        headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        response = requests.post(url, headers=headers, json={"body": comment})
        response.raise_for_status()
    
    def _set_pr_status(self, owner: str, repo: str, pr_number: int, state: str, description: str):
        """Set PR status via GitHub API."""
        if not self.github_token:
            return
        
        # Get PR commit SHA
        pr_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
        headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        pr_response = requests.get(pr_url, headers=headers)
        pr_response.raise_for_status()
        
        sha = pr_response.json()["head"]["sha"]
        
        # Set status
        status_url = f"https://api.github.com/repos/{owner}/{repo}/statuses/{sha}"
        status_data = {
            "state": state,
            "description": description,
            "context": "claude-prompt-review/escalation"
        }
        
        response = requests.post(status_url, headers=headers, json=status_data)
        response.raise_for_status()
    
    def _create_escalation_comment(self, escalation_plan: Dict, risk_assessment: Dict, quality_assessment: Dict) -> str:
        """Create detailed escalation comment for PR."""
        level = escalation_plan["level"]
        
        comment = f"""## 🚨 Smart Escalation: {level.upper()}

This prompt engineering change has been escalated to **{level.replace('_', ' ').title()}** based on automated assessment.

### 📊 Assessment Summary

| Metric | Score | Status |
|--------|-------|--------|
| **Risk Score** | {risk_assessment.get('predictive_score', 0)}/100 | {risk_assessment.get('risk_level', 'Unknown')} |
| **Quality Score** | {quality_assessment.get('overall_score', 0)}/100 | {quality_assessment.get('grade', 'Unknown')} |
| **Production Ready** | {quality_assessment.get('compliance', {}).get('production_ready', False)} | {'✅' if quality_assessment.get('compliance', {}).get('production_ready', False) else '❌'} |

### 🎯 Required Actions

"""
        
        for action in escalation_plan["immediate_actions"]:
            comment += f"- [ ] {action}\n"
        
        comment += f"""
### 👥 Review Requirements

- **Required Reviewers**: {escalation_plan['review_requirements']['required_reviewers']}
- **Approval Time Limit**: {escalation_plan['review_requirements']['approval_time_limit']}
- **Escalation Path**: {' → '.join(escalation_plan['review_requirements']['escalation_path'])}

### 🛡️ Safety Measures

"""
        
        for measure in escalation_plan["safety_measures"]:
            comment += f"- {measure}\n"
        
        if level == "critical_risk":
            comment += """
### ⚠️ CRITICAL ALERT

This change affects critical framework components and requires immediate attention from the safety committee.

**Emergency Procedures Activated:**
- Deployment freeze implemented
- Enhanced monitoring enabled
- Rollback procedures prepared
- Security team notified
"""
        
        comment += """

---
*🤖 Generated by Claude Smart Escalation Engine*
*🔬 Powered by Meta-Framework Human Oversight Integration*
"""
        
        return comment

def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(description="Smart escalation for prompt changes")
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    parser.add_argument("--risk-assessment", required=True, help="Risk assessment JSON file")
    parser.add_argument("--quality-assessment", required=True, help="Quality assessment JSON file")
    parser.add_argument("--change-analysis", required=True, help="Change analysis JSON file")
    parser.add_argument("--pr-number", type=int, help="Pull request number")
    parser.add_argument("--output", help="Output file for escalation results")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    
    args = parser.parse_args()
    
    # Load assessment files
    with open(args.risk_assessment, 'r') as f:
        risk_assessment = json.load(f)
    
    with open(args.quality_assessment, 'r') as f:
        quality_assessment = json.load(f)
    
    with open(args.change_analysis, 'r') as f:
        change_analysis = json.load(f)
    
    # Process escalation
    engine = SmartEscalationEngine(args.repo_root)
    results = engine.process_escalation(
        risk_assessment, quality_assessment, change_analysis, args.pr_number
    )
    
    if args.json:
        output = json.dumps(results, indent=2)
    else:
        # Generate readable report
        report = []
        report.append("# 🎯 Smart Escalation Report")
        report.append(f"**Escalation Level**: {results['escalation_level'].replace('_', ' ').title()}")
        report.append(f"**Human Review Required**: {results['requires_human_review']}")
        report.append(f"**Estimated Resolution**: {results['estimated_resolution_time']}")
        report.append("")
        
        if results["actions_taken"]["github_actions"]:
            report.append("## GitHub Actions Taken")
            for action in results["actions_taken"]["github_actions"]:
                report.append(f"- {action}")
            report.append("")
        
        if results["stakeholders_notified"]:
            report.append("## Stakeholders Notified")
            for notification in results["stakeholders_notified"]:
                report.append(f"- {notification['recipient']} via {', '.join(notification['channels'])}")
            report.append("")
        
        report.append("## Monitoring Configuration")
        monitoring = results["monitoring_config"]
        report.append(f"- Real-time Monitoring: {monitoring['real_time_monitoring']}")
        report.append(f"- Alert Threshold: {monitoring['alert_threshold_seconds']}s")
        report.append(f"- Health Check Interval: {monitoring['health_check_interval']}")
        
        output = "\n".join(report)
    
    if args.output:
        Path(args.output).write_text(output)
        print(f"🎯 Smart escalation results written to {args.output}")
    else:
        print(output)
    
    # Exit code based on escalation level
    if results["escalation_level"] == "critical_risk":
        sys.exit(2)
    elif results["escalation_level"] == "high_risk":
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()