#!/usr/bin/env python3
"""
Agent P1: Production Security Validator
Mission: Comprehensive security audit for production deployment
Scope: 249 files, git history, permissions, secrets scanning
"""

import json
import subprocess
import re
import os
from pathlib import Path
from datetime import datetime
import hashlib

class AgentP1SecurityValidator:
    def __init__(self):
        self.base_path = Path(".")
        self.security_results = {
            'agent': 'Agent P1 - Production Security Validator',
            'timestamp': datetime.now().isoformat(),
            'mission': 'Comprehensive security audit for production deployment',
            'scope': {
                'files_scanned': 0,
                'git_commits_analyzed': 0,
                'security_patterns_checked': 0
            },
            'security_findings': {
                'critical_vulnerabilities': [],
                'medium_risks': [],
                'low_risks': [],
                'secrets_exposed': [],
                'file_permissions': [],
                'git_history_issues': []
            },
            'security_score': 0,
            'production_clearance': False,
            'recommendations': []
        }
        
        # Security patterns to detect
        self.security_patterns = {
            'secrets': [
                r'(?i)(password|passwd|pwd)\s*[=:]\s*["\']?[a-zA-Z0-9]+["\']?',
                r'(?i)(api[_-]?key|apikey)\s*[=:]\s*["\']?[a-zA-Z0-9]+["\']?',
                r'(?i)(secret|token)\s*[=:]\s*["\']?[a-zA-Z0-9]+["\']?',
                r'(?i)(private[_-]?key|privatekey)',
                r'sk-[a-zA-Z0-9]{32,}',  # OpenAI API keys
                r'ghp_[a-zA-Z0-9]{36}',  # GitHub personal access tokens
            ],
            'vulnerabilities': [
                r'eval\s*\(',
                r'exec\s*\(',
                r'subprocess\.call\s*\(',
                r'os\.system\s*\(',
                r'shell\s*=\s*True',
            ],
            'suspicious': [
                r'(?i)hack|exploit|backdoor|malware',
                r'rm\s+-rf\s+/',
                r'format\s+c:',
                r'(?i)delete.*system|destroy.*data',
            ]
        }
    
    def log_finding(self, severity, category, description, file_path=None, line_num=None):
        """Log security finding"""
        finding = {
            'severity': severity,
            'category': category,
            'description': description,
            'file_path': str(file_path) if file_path else None,
            'line_number': line_num,
            'timestamp': datetime.now().isoformat()
        }
        
        if severity == 'CRITICAL':
            self.security_results['security_findings']['critical_vulnerabilities'].append(finding)
        elif severity == 'MEDIUM':
            self.security_results['security_findings']['medium_risks'].append(finding)
        elif severity == 'LOW':
            self.security_results['security_findings']['low_risks'].append(finding)
        
        print(f"🔍 {severity}: {description}")
        if file_path:
            print(f"   📁 File: {file_path}:{line_num if line_num else 'N/A'}")
    
    def scan_file_content(self, file_path):
        """Scan individual file for security issues"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
            
            # Check for secrets
            for pattern in self.security_patterns['secrets']:
                matches = re.finditer(pattern, content, re.MULTILINE)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    self.log_finding('CRITICAL', 'SECRETS', 
                                   f"Potential secret exposed: {match.group()[:50]}...", 
                                   file_path, line_num)
            
            # Check for vulnerabilities
            for pattern in self.security_patterns['vulnerabilities']:
                matches = re.finditer(pattern, content, re.MULTILINE)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    self.log_finding('MEDIUM', 'VULNERABILITY',
                                   f"Potential vulnerability: {match.group()}", 
                                   file_path, line_num)
            
            # Check for suspicious patterns
            for pattern in self.security_patterns['suspicious']:
                matches = re.finditer(pattern, content, re.MULTILINE)
                for match in matches:
                    line_num = content[:match.start()].count('\n') + 1
                    self.log_finding('LOW', 'SUSPICIOUS',
                                   f"Suspicious pattern: {match.group()}", 
                                   file_path, line_num)
            
            return True
            
        except Exception as e:
            self.log_finding('LOW', 'SCAN_ERROR', f"Could not scan file: {e}", file_path)
            return False
    
    def scan_all_files(self):
        """Scan all framework files for security issues"""
        print("🔍 Agent P1: Scanning all framework files for security issues...")
        
        # Get all files to scan
        file_patterns = ['**/*.py', '**/*.md', '**/*.json', '**/*.xml', '**/*.yaml', '**/*.yml']
        all_files = []
        
        for pattern in file_patterns:
            all_files.extend(self.base_path.glob(pattern))
        
        # Remove duplicates and filter
        unique_files = list(set(all_files))
        framework_files = [f for f in unique_files if '.claude' in str(f) or f.name in ['CLAUDE.md', 'GETTING_STARTED.md']]
        
        scanned_count = 0
        for file_path in framework_files:
            if file_path.is_file():
                self.scan_file_content(file_path)
                scanned_count += 1
        
        self.security_results['scope']['files_scanned'] = scanned_count
        print(f"  📊 Scanned {scanned_count} files")
        
        return scanned_count
    
    def check_file_permissions(self):
        """Check file permissions for security issues"""
        print("🔍 Agent P1: Checking file permissions...")
        
        # Check for overly permissive files
        try:
            result = subprocess.run(['find', '.claude', '-type', 'f', '-perm', '+022'], 
                                  capture_output=True, text=True)
            if result.stdout.strip():
                files = result.stdout.strip().split('\n')
                for file_path in files:
                    self.log_finding('MEDIUM', 'PERMISSIONS', 
                                   f"File has overly permissive permissions", file_path)
        except Exception as e:
            self.log_finding('LOW', 'PERMISSION_CHECK', f"Could not check permissions: {e}")
    
    def analyze_git_history(self):
        """Analyze git history for security issues"""
        print("🔍 Agent P1: Analyzing git history for security issues...")
        
        try:
            # Check recent commits for potential issues
            result = subprocess.run(['git', 'log', '--oneline', '-20'], 
                                  capture_output=True, text=True)
            commits = result.stdout.strip().split('\n')
            
            # Look for suspicious commit messages
            suspicious_keywords = ['password', 'secret', 'key', 'token', 'hack', 'temp', 'debug']
            
            for commit in commits:
                commit_msg = commit.lower()
                for keyword in suspicious_keywords:
                    if keyword in commit_msg:
                        self.log_finding('LOW', 'GIT_HISTORY',
                                       f"Potentially sensitive commit message: {commit[:50]}...")
            
            # Check for large files that might contain secrets
            result = subprocess.run(['git', 'ls-files', '--', '.claude'], 
                                  capture_output=True, text=True)
            files = result.stdout.strip().split('\n')
            
            for file_path in files:
                if os.path.exists(file_path):
                    size = os.path.getsize(file_path)
                    if size > 1024 * 1024:  # > 1MB
                        self.log_finding('LOW', 'LARGE_FILE',
                                       f"Large file in framework: {size} bytes", file_path)
            
            self.security_results['scope']['git_commits_analyzed'] = len(commits)
            
        except Exception as e:
            self.log_finding('LOW', 'GIT_ANALYSIS', f"Git history analysis failed: {e}")
    
    def check_framework_integrity(self):
        """Check framework integrity and configuration"""
        print("🔍 Agent P1: Checking framework integrity...")
        
        # Check CLAUDE.md for security-related configurations
        claude_md = Path('CLAUDE.md')
        if claude_md.exists():
            try:
                content = claude_md.read_text()
                
                # Look for security configurations
                if 'security' not in content.lower():
                    self.log_finding('MEDIUM', 'SECURITY_CONFIG',
                                   "No security configuration found in CLAUDE.md")
                
                # Check for proper atomic commit configuration
                if 'atomic' in content.lower() and 'rollback' in content.lower():
                    print("  ✅ Atomic commits security feature found")
                else:
                    self.log_finding('MEDIUM', 'SAFETY_CONFIG',
                                   "Atomic commits safety configuration not clearly defined")
                
            except Exception as e:
                self.log_finding('LOW', 'CONFIG_CHECK', f"Could not check CLAUDE.md: {e}")
    
    def calculate_security_score(self):
        """Calculate overall security score"""
        critical_count = len(self.security_results['security_findings']['critical_vulnerabilities'])
        medium_count = len(self.security_results['security_findings']['medium_risks'])
        low_count = len(self.security_results['security_findings']['low_risks'])
        
        # Scoring: Start with 100, deduct points for issues
        base_score = 100
        score = base_score
        
        # Critical issues are blocking
        score -= critical_count * 30
        score -= medium_count * 10
        score -= low_count * 2
        
        # Ensure minimum score of 0
        score = max(0, score)
        
        self.security_results['security_score'] = score
        
        # Production clearance requires score >= 85 and zero critical issues
        clearance = score >= 85 and critical_count == 0
        self.security_results['production_clearance'] = clearance
        
        return score, clearance
    
    def generate_recommendations(self):
        """Generate security recommendations"""
        recommendations = []
        
        critical_count = len(self.security_results['security_findings']['critical_vulnerabilities'])
        medium_count = len(self.security_results['security_findings']['medium_risks'])
        
        if critical_count > 0:
            recommendations.append("CRITICAL: Address all critical vulnerabilities before production")
            recommendations.append("Review and remove any exposed secrets or credentials")
        
        if medium_count > 0:
            recommendations.append("MEDIUM: Review and mitigate medium-risk security issues")
        
        if critical_count == 0 and medium_count <= 3:
            recommendations.append("Security posture is acceptable for production deployment")
        
        recommendations.extend([
            "Implement regular security scanning in CI/CD pipeline",
            "Consider adding security headers and content validation",
            "Ensure atomic commits are used for all production changes"
        ])
        
        self.security_results['recommendations'] = recommendations
        return recommendations
    
    def execute_security_validation(self):
        """Execute complete security validation"""
        print("🚀 Agent P1: Starting Production Security Validation...")
        print("🎯 Mission: Comprehensive security audit for production deployment")
        
        # Execute all security checks
        file_count = self.scan_all_files()
        self.check_file_permissions()
        self.analyze_git_history()
        self.check_framework_integrity()
        
        # Calculate results
        score, clearance = self.calculate_security_score()
        recommendations = self.generate_recommendations()
        
        # Update scope
        self.security_results['scope']['security_patterns_checked'] = len(
            self.security_patterns['secrets'] + 
            self.security_patterns['vulnerabilities'] + 
            self.security_patterns['suspicious']
        )
        
        # Save results
        with open('agent_p1_security_validation_results.json', 'w') as f:
            json.dump(self.security_results, f, indent=2)
        
        # Report summary
        print("\n" + "="*80)
        print("🎯 AGENT P1 SECURITY VALIDATION - COMPLETE!")
        print("="*80)
        print(f"📊 Files Scanned: {file_count}")
        print(f"🔍 Security Patterns Checked: {self.security_results['scope']['security_patterns_checked']}")
        print(f"🚨 Critical Issues: {len(self.security_results['security_findings']['critical_vulnerabilities'])}")
        print(f"⚠️  Medium Issues: {len(self.security_results['security_findings']['medium_risks'])}")
        print(f"ℹ️  Low Issues: {len(self.security_results['security_findings']['low_risks'])}")
        print(f"📈 Security Score: {score}/100")
        print(f"🏭 Production Clearance: {'✅ APPROVED' if clearance else '❌ BLOCKED'}")
        
        if clearance:
            print("\n🎉 SECURITY VALIDATION PASSED!")
            print("Framework has security clearance for production deployment")
        else:
            print("\n⚠️  SECURITY ISSUES FOUND!")
            print("Address security issues before production deployment")
        
        return clearance

if __name__ == "__main__":
    agent_p1 = AgentP1SecurityValidator()
    agent_p1.execute_security_validation()