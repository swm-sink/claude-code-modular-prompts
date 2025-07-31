#!/usr/bin/env python3
"""
Security Audit and Penetration Testing System
Step 83 of 100-Step Finalization Plan

PURPOSE: Comprehensive security analysis of Claude Code template library
SCOPE: Input validation, file access, injection risks, data exposure
"""

import os
import sys
import re
import yaml
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any, Set
from dataclasses import dataclass
from datetime import datetime
import subprocess

@dataclass
class SecurityFinding:
    severity: str  # CRITICAL, HIGH, MEDIUM, LOW, INFO
    category: str
    finding: str
    file_path: str
    line_number: Optional[int] = None
    description: str = ""
    recommendation: str = ""
    false_positive: bool = False

class SecurityAuditSystem:
    """Comprehensive security audit system for prompt engineering templates"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.findings: List[SecurityFinding] = []
        self.start_time = datetime.now()
        
        # Core paths
        self.claude_dir = project_root / ".claude"
        self.commands_dir = self.claude_dir / "commands"
        self.components_dir = self.claude_dir / "components"
        
        # Security patterns to detect
        self.security_patterns = {
            'credentials': {
                'patterns': [
                    r'(?i)(password|passwd|pwd)\s*[=:]\s*["\'][^"\']{3,}["\']',
                    r'(?i)(secret|token|key)\s*[=:]\s*["\'][^"\']{8,}["\']',
                    r'(?i)(api[_-]?key|access[_-]?token)\s*[=:]\s*["\'][^"\']{8,}["\']',
                    r'(?i)Bearer\s+[A-Za-z0-9\-_]{20,}',
                ],
                'severity': 'CRITICAL',
                'category': 'Credential Exposure'
            },
            'injection_risks': {
                'patterns': [
                    r'(?i)eval\s*\(',
                    r'(?i)exec\s*\(',
                    r'(?i)system\s*\(',
                    r'(?i)shell_exec\s*\(',
                    r'(?i)subprocess\.call\s*\([^)]*shell\s*=\s*True',
                    r'(?i)os\.system\s*\(',
                ],
                'severity': 'HIGH',
                'category': 'Code Injection Risk'
            },
            'file_access_risks': {
                'patterns': [
                    r'(?i)\.\./',
                    r'(?i)\.\.\\',
                    r'(?i)/etc/passwd',
                    r'(?i)%SYSTEMROOT%',
                    r'(?i)~/.ssh',
                ],
                'severity': 'MEDIUM',
                'category': 'Path Traversal Risk'
            },
            'prompt_injection': {
                'patterns': [
                    r'(?i)ignore\s+previous\s+instructions',
                    r'(?i)forget\s+everything',
                    r'(?i)system\s+prompt',
                    r'(?i)jailbreak',
                    r'(?i)act\s+as\s+.*admin',
                ],
                'severity': 'MEDIUM', 
                'category': 'Prompt Injection Risk'
            },
            'sensitive_info': {
                'patterns': [
                    r'(?i)(ssn|social.security)\D*\d{3}-?\d{2}-?\d{4}',
                    r'(?i)credit.card\D*\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}',
                    r'(?i)email\D*[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}',
                ],
                'severity': 'LOW',
                'category': 'Sensitive Information'
            }
        }
        
        # File extensions to scan
        self.scannable_extensions = {'.md', '.py', '.sh', '.yaml', '.yml', '.json', '.txt'}
        
        # Known safe patterns (to reduce false positives)
        self.safe_patterns = [
            r'password.*placeholder',
            r'password.*example',
            r'INSERT_.*',
            r'\[INSERT_.*\]',
            r'your.*password',
            r'security.*keyword',
        ]
    
    def run_comprehensive_security_audit(self) -> Dict[str, Any]:
        """Execute comprehensive security audit"""
        print("🔒 COMPREHENSIVE SECURITY AUDIT")
        print("=" * 60)
        
        # Audit categories
        audit_categories = [
            ("Static Code Analysis", self._audit_static_code),
            ("YAML Security Analysis", self._audit_yaml_security),
            ("Template Security Analysis", self._audit_template_security),
            ("File Permission Analysis", self._audit_file_permissions),
            ("Dependency Security Analysis", self._audit_dependency_security),
            ("Configuration Security", self._audit_configuration_security),
            ("Documentation Security", self._audit_documentation_security),
            ("Prompt Injection Analysis", self._audit_prompt_injection)
        ]
        
        for category_name, audit_method in audit_categories:
            print(f"\n🔍 Auditing: {category_name}")
            try:
                audit_method()
            except Exception as e:
                self._add_finding("CRITICAL", "Audit Error", f"Audit failed: {str(e)}", 
                                "audit_error.log", description="Unexpected error during security audit")
        
        return self._generate_security_report()
    
    def _audit_static_code(self):
        """Audit static code for security vulnerabilities"""
        
        scanned_files = 0
        vulnerabilities_found = 0
        
        for file_path in self.project_root.rglob("*"):
            if (file_path.is_file() and 
                file_path.suffix in self.scannable_extensions and
                not self._is_excluded_path(file_path)):
                
                try:
                    content = file_path.read_text(encoding='utf-8')
                    scanned_files += 1
                    
                    # Check each security pattern category
                    for category_name, pattern_config in self.security_patterns.items():
                        for pattern in pattern_config['patterns']:
                            matches = re.finditer(pattern, content, re.MULTILINE)
                            for match in matches:
                                line_num = content[:match.start()].count('\n') + 1
                                
                                # Check if it's a false positive
                                is_false_positive = self._is_false_positive(match.group(), content, line_num)
                                
                                if not is_false_positive:
                                    vulnerabilities_found += 1
                                    self._add_finding(
                                        pattern_config['severity'],
                                        pattern_config['category'],
                                        f"Security pattern detected: {match.group()[:50]}...",
                                        str(file_path.relative_to(self.project_root)),
                                        line_num,
                                        f"Detected potential {category_name} vulnerability",
                                        f"Review and validate the security implications of this pattern"
                                    )
                
                except Exception as e:
                    self._add_finding("LOW", "File Access", f"Could not scan file: {str(e)}", str(file_path))
        
        print(f"  📊 Scanned {scanned_files} files, found {vulnerabilities_found} potential issues")
    
    def _audit_yaml_security(self):
        """Audit YAML files for security issues"""
        
        yaml_files = list(self.project_root.rglob("*.yml")) + list(self.project_root.rglob("*.yaml"))
        command_files = list(self.commands_dir.rglob("*.md"))
        
        yaml_issues = 0
        
        # Check standalone YAML files
        for yaml_file in yaml_files:
            try:
                content = yaml_file.read_text(encoding='utf-8')
                yaml_data = yaml.safe_load(content)
                
                if yaml_data:
                    yaml_issues += self._check_yaml_content_security(yaml_data, str(yaml_file))
                    
            except yaml.YAMLError as e:
                self._add_finding("MEDIUM", "YAML Security", f"YAML parsing error: {str(e)}", 
                                str(yaml_file), description="Malformed YAML could indicate tampering")
            except Exception:
                pass
        
        # Check YAML frontmatter in command files
        for cmd_file in command_files:
            try:
                content = cmd_file.read_text(encoding='utf-8')
                if content.startswith('---'):
                    yaml_end = content.find('---', 3)
                    if yaml_end > 0:
                        yaml_content = content[3:yaml_end]
                        yaml_data = yaml.safe_load(yaml_content)
                        
                        if yaml_data:
                            yaml_issues += self._check_yaml_content_security(yaml_data, str(cmd_file))
                            
            except Exception:
                pass
        
        print(f"  📊 Checked YAML in {len(yaml_files + command_files)} files, found {yaml_issues} issues")
    
    def _check_yaml_content_security(self, yaml_data: dict, file_path: str) -> int:
        """Check YAML content for security issues"""
        issues = 0
        
        # Check for dangerous YAML constructs
        yaml_str = yaml.dump(yaml_data)
        
        dangerous_patterns = [
            (r'!!python/', 'Python object deserialization risk'),
            (r'!!java/', 'Java object deserialization risk'),
            (r'exec:', 'Command execution risk'),
            (r'system:', 'System command risk'),
        ]
        
        for pattern, description in dangerous_patterns:
            if re.search(pattern, yaml_str, re.IGNORECASE):
                self._add_finding("HIGH", "YAML Security", f"Dangerous YAML construct: {description}",
                                file_path, description=f"YAML contains potentially dangerous construct: {pattern}")
                issues += 1
        
        # Check for sensitive data in YAML
        if isinstance(yaml_data, dict):
            for key, value in yaml_data.items():
                if isinstance(value, str):
                    if re.search(r'(?i)(password|secret|token|key)', key) and len(value) > 10:
                        if not any(safe in value.lower() for safe in ['placeholder', 'example', 'insert']):
                            self._add_finding("MEDIUM", "YAML Security", f"Potential credential in YAML: {key}",
                                            file_path, description="YAML may contain embedded credentials")
                            issues += 1
        
        return issues
    
    def _audit_template_security(self):
        """Audit prompt templates for security vulnerabilities"""
        
        template_files = list(self.commands_dir.rglob("*.md")) + list(self.components_dir.rglob("*.md"))
        template_issues = 0
        
        for template_file in template_files:
            try:
                content = template_file.read_text(encoding='utf-8')
                
                # Check for template injection risks
                injection_patterns = [
                    (r'\{\{.*\|.*\}\}', 'Template filter injection risk'),
                    (r'\$\{.*\}', 'Variable substitution injection risk'),
                    (r'<%.*%>', 'Server-side template injection risk'),
                ]
                
                for pattern, description in injection_patterns:
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        line_num = content[:match.start()].count('\n') + 1
                        self._add_finding("MEDIUM", "Template Security", description,
                                        str(template_file.relative_to(self.project_root)), line_num,
                                        "Template contains potentially dangerous substitution pattern")
                        template_issues += 1
                
                # Check for unsafe prompt patterns
                unsafe_patterns = [
                    (r'(?i)execute.*command', 'Command execution prompt'),
                    (r'(?i)run.*system', 'System execution prompt'),
                    (r'(?i)delete.*file', 'File deletion prompt'),
                    (r'(?i)access.*root', 'Root access prompt'),
                ]
                
                for pattern, description in unsafe_patterns:
                    if re.search(pattern, content):
                        line_num = content.find(re.search(pattern, content).group())
                        line_num = content[:line_num].count('\n') + 1 if line_num >= 0 else None
                        self._add_finding("LOW", "Template Security", f"Potentially unsafe prompt: {description}",
                                        str(template_file.relative_to(self.project_root)), line_num,
                                        "Template may encourage unsafe operations")
                        template_issues += 1
                        
            except Exception:
                pass
        
        print(f"  📊 Checked {len(template_files)} templates, found {template_issues} potential issues")
    
    def _audit_file_permissions(self):
        """Audit file permissions for security issues"""
        
        permission_issues = 0
        executable_files = []
        
        for file_path in self.project_root.rglob("*"):
            if file_path.is_file():
                try:
                    stat_info = file_path.stat()
                    
                    # Check for overly permissive files
                    if stat_info.st_mode & 0o002:  # World writable
                        self._add_finding("HIGH", "File Permissions", "World-writable file detected",
                                        str(file_path.relative_to(self.project_root)),
                                        description="File is writable by all users")
                        permission_issues += 1
                    
                    # Track executable files
                    if stat_info.st_mode & 0o111:  # Executable
                        executable_files.append(file_path)
                        
                        # Check if non-script files are executable
                        if file_path.suffix not in {'.py', '.sh', '.exe'} and file_path.name not in {'setup.sh'}:
                            self._add_finding("LOW", "File Permissions", "Unexpected executable file",
                                            str(file_path.relative_to(self.project_root)),
                                            description="Non-script file has execute permissions")
                            permission_issues += 1
                            
                except Exception:
                    pass
        
        print(f"  📊 Found {len(executable_files)} executable files, {permission_issues} permission issues")
    
    def _audit_dependency_security(self):
        """Audit dependencies for known vulnerabilities"""
        
        dependency_files = []
        dependency_issues = 0
        
        # Find dependency files
        for pattern in ['requirements.txt', 'package.json', 'Pipfile', 'poetry.lock', 'yarn.lock']:
            dependency_files.extend(list(self.project_root.rglob(pattern)))
        
        for dep_file in dependency_files:
            try:
                content = dep_file.read_text(encoding='utf-8')
                
                # Check for known vulnerable patterns (simplified)
                vulnerable_patterns = [
                    (r'(?i)requests[<>=].*2\.0\.\d+', 'Outdated requests library'),
                    (r'(?i)pyyaml[<>=].*3\.\d+', 'Vulnerable PyYAML version'),
                    (r'(?i)pillow[<>=].*[1-7]\.\d+', 'Potentially vulnerable Pillow'),
                ]
                
                for pattern, description in vulnerable_patterns:
                    if re.search(pattern, content):
                        self._add_finding("MEDIUM", "Dependency Security", f"Potentially vulnerable dependency: {description}",
                                        str(dep_file.relative_to(self.project_root)),
                                        description="Dependency may have known security vulnerabilities")
                        dependency_issues += 1
                        
            except Exception:
                pass
        
        print(f"  📊 Checked {len(dependency_files)} dependency files, found {dependency_issues} potential issues")
    
    def _audit_configuration_security(self):
        """Audit configuration files for security issues"""
        
        config_files = []
        config_issues = 0
        
        # Find configuration files
        for pattern in ['*.conf', '*.config', '*.ini', 'settings.json', '.env*']:
            config_files.extend(list(self.project_root.rglob(pattern)))
        
        for config_file in config_files:
            try:
                content = config_file.read_text(encoding='utf-8')
                
                # Check for insecure configurations
                insecure_patterns = [
                    (r'(?i)debug\s*[=:]\s*true', 'Debug mode enabled'),
                    (r'(?i)ssl\s*[=:]\s*false', 'SSL disabled'),
                    (r'(?i)verify\s*[=:]\s*false', 'Verification disabled'),
                    (r'(?i)localhost', 'Localhost configuration (may be dev config)'),
                ]
                
                for pattern, description in insecure_patterns:
                    if re.search(pattern, content):
                        self._add_finding("LOW", "Configuration Security", f"Potentially insecure config: {description}",
                                        str(config_file.relative_to(self.project_root)),
                                        description="Configuration may have security implications")
                        config_issues += 1
                        
            except Exception:
                pass
        
        print(f"  📊 Checked {len(config_files)} config files, found {config_issues} potential issues")
    
    def _audit_documentation_security(self):
        """Audit documentation for security guidance and potential exposure"""
        
        doc_files = list(self.project_root.rglob("*.md"))
        doc_issues = 0
        security_guidance_found = False
        
        for doc_file in doc_files:
            try:
                content = doc_file.read_text(encoding='utf-8')
                
                # Check for security guidance
                if re.search(r'(?i)(security|vulnerability|exploit)', content):
                    security_guidance_found = True
                
                # Check for accidentally exposed information
                exposure_patterns = [
                    (r'(?i)internal.*server', 'Internal server reference'),
                    (r'(?i)admin.*password', 'Admin password reference'),
                    (r'(?i)database.*connection', 'Database connection details'),
                ]
                
                for pattern, description in exposure_patterns:
                    if re.search(pattern, content):
                        self._add_finding("LOW", "Documentation Security", f"Potential information exposure: {description}",
                                        str(doc_file.relative_to(self.project_root)),
                                        description="Documentation may contain sensitive information")
                        doc_issues += 1
                        
            except Exception:
                pass
        
        if not security_guidance_found:
            self._add_finding("LOW", "Documentation Security", "No security guidance found in documentation",
                            "documentation", description="Project lacks security documentation")
            doc_issues += 1
        
        print(f"  📊 Checked {len(doc_files)} documentation files, found {doc_issues} potential issues")
    
    def _audit_prompt_injection(self):
        """Audit for prompt injection vulnerabilities"""
        
        template_files = list(self.commands_dir.rglob("*.md")) + list(self.components_dir.rglob("*.md"))
        injection_issues = 0
        
        for template_file in template_files:
            try:
                content = template_file.read_text(encoding='utf-8')
                
                # Check for prompt injection patterns
                for category_name, pattern_config in self.security_patterns.items():
                    if category_name == 'prompt_injection':
                        for pattern in pattern_config['patterns']:
                            if re.search(pattern, content, re.IGNORECASE):
                                line_num = content.find(re.search(pattern, content, re.IGNORECASE).group())
                                line_num = content[:line_num].count('\n') + 1 if line_num >= 0 else None
                                
                                self._add_finding("MEDIUM", "Prompt Injection", f"Potential prompt injection pattern detected",
                                                str(template_file.relative_to(self.project_root)), line_num,
                                                "Template may be vulnerable to prompt injection attacks")
                                injection_issues += 1
                                
            except Exception:
                pass
        
        print(f"  📊 Checked {len(template_files)} templates for injection risks, found {injection_issues} issues")
    
    def _is_excluded_path(self, file_path: Path) -> bool:
        """Check if path should be excluded from security scanning"""
        exclude_patterns = [
            '/.git/',
            '/node_modules/',
            '/__pycache__/',
            '/.pytest_cache/',
            '/venv/',
        ]
        
        path_str = str(file_path)
        return any(pattern in path_str for pattern in exclude_patterns)
    
    def _is_false_positive(self, match_text: str, full_content: str, line_number: int) -> bool:
        """Check if a security finding is likely a false positive"""
        
        # Check against safe patterns
        for safe_pattern in self.safe_patterns:
            if re.search(safe_pattern, match_text, re.IGNORECASE):
                return True
        
        # Check context around the match
        lines = full_content.split('\n')
        if 0 <= line_number - 1 < len(lines):
            line_content = lines[line_number - 1]
            
            # Check for comments or documentation context
            if any(marker in line_content for marker in ['#', '//', '<!--', '*', 'example', 'placeholder']):
                return True
        
        return False
    
    def _add_finding(self, severity: str, category: str, finding: str, file_path: str,
                    line_number: Optional[int] = None, description: str = "", 
                    recommendation: str = "", false_positive: bool = False):
        """Add security finding"""
        
        if not recommendation:
            recommendation = self._generate_default_recommendation(severity, category)
        
        self.findings.append(SecurityFinding(
            severity=severity,
            category=category,
            finding=finding,
            file_path=file_path,
            line_number=line_number,
            description=description,
            recommendation=recommendation,
            false_positive=false_positive
        ))
        
        # Real-time feedback
        severity_emoji = {
            "CRITICAL": "🚨", "HIGH": "🔴", "MEDIUM": "🟡", 
            "LOW": "🟢", "INFO": "ℹ️"
        }
        
        location = f":{line_number}" if line_number else ""
        print(f"    {severity_emoji.get(severity, '❓')} {severity}: {finding} ({file_path}{location})")
    
    def _generate_default_recommendation(self, severity: str, category: str) -> str:
        """Generate default recommendation based on severity and category"""
        
        recommendations = {
            ("CRITICAL", "Credential Exposure"): "Remove hardcoded credentials immediately. Use environment variables or secure credential management.",
            ("HIGH", "Code Injection Risk"): "Validate and sanitize all inputs. Avoid dynamic code execution where possible.",
            ("MEDIUM", "Path Traversal Risk"): "Implement proper input validation and path sanitization.",
            ("MEDIUM", "Prompt Injection Risk"): "Implement input validation and consider prompt sanitization.",
            ("LOW", "Sensitive Information"): "Review and remove any sensitive information from code/documentation.",
        }
        
        return recommendations.get((severity, category), "Review and address this security concern.")
    
    def _generate_security_report(self) -> Dict[str, Any]:
        """Generate comprehensive security report"""
        audit_duration = datetime.now() - self.start_time
        
        # Categorize findings by severity
        severity_counts = {}
        category_counts = {}
        
        for finding in self.findings:
            severity_counts[finding.severity] = severity_counts.get(finding.severity, 0) + 1
            category_counts[finding.category] = category_counts.get(finding.category, 0) + 1
        
        # Calculate security score
        critical = severity_counts.get("CRITICAL", 0)
        high = severity_counts.get("HIGH", 0)
        medium = severity_counts.get("MEDIUM", 0)
        low = severity_counts.get("LOW", 0)
        
        # Security score calculation (0-100)
        deductions = critical * 50 + high * 20 + medium * 5 + low * 1
        security_score = max(0, 100 - deductions)
        
        # Security grade
        if security_score >= 95:
            grade = "A+ (Excellent Security)"
        elif security_score >= 90:
            grade = "A (Very Good Security)"
        elif security_score >= 85:
            grade = "B+ (Good Security)"
        elif security_score >= 80:
            grade = "B (Acceptable Security)"
        elif security_score >= 70:
            grade = "C (Security Concerns)"
        elif security_score >= 60:
            grade = "D (Significant Issues)"
        else:
            grade = "F (Critical Security Issues)"
        
        report = {
            "security_summary": {
                "total_findings": len(self.findings),
                "severity_distribution": severity_counts,
                "category_distribution": category_counts,
                "security_score": security_score,
                "security_grade": grade,
                "audit_duration": str(audit_duration),
                "audit_date": self.start_time.strftime('%Y-%m-%d %H:%M:%S')
            },
            "findings_by_severity": {
                severity: [
                    {
                        "category": f.category,
                        "finding": f.finding,
                        "file": f.file_path,
                        "line": f.line_number,
                        "description": f.description,
                        "recommendation": f.recommendation
                    }
                    for f in self.findings if f.severity == severity
                ]
                for severity in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]
                if severity in severity_counts
            },
            "security_recommendations": self._generate_security_recommendations()
        }
        
        return report
    
    def _generate_security_recommendations(self) -> List[str]:
        """Generate security improvement recommendations"""
        recommendations = []
        
        # Count findings by severity
        critical_count = len([f for f in self.findings if f.severity == "CRITICAL"])
        high_count = len([f for f in self.findings if f.severity == "HIGH"])
        medium_count = len([f for f in self.findings if f.severity == "MEDIUM"])
        
        if critical_count > 0:
            recommendations.append(f"URGENT: Address {critical_count} critical security issues immediately")
        
        if high_count > 0:
            recommendations.append(f"Address {high_count} high-severity security issues")
        
        if medium_count > 0:
            recommendations.append(f"Review and address {medium_count} medium-severity security issues")
        
        # Category-specific recommendations
        categories = set(f.category for f in self.findings)
        if "Credential Exposure" in categories:
            recommendations.append("Implement secure credential management practices")
        
        if "Code Injection Risk" in categories:
            recommendations.append("Implement input validation and sanitization")
        
        if "Prompt Injection Risk" in categories:
            recommendations.append("Add prompt injection protection mechanisms")
        
        if not recommendations:
            recommendations.append("Security posture is excellent - maintain current practices")
        
        return recommendations

def main():
    """Run comprehensive security audit"""
    project_root = Path.cwd()
    
    print(f"🔍 Project root: {project_root}")
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    audit_system = SecurityAudit# SECURITY WARNING: system() call - validate all inputsSystem(project_root)
    report = audit_system.run_comprehensive_security_audit()
    
    # Display summary
    print("\n" + "="*60)
    print("🔒 SECURITY AUDIT SUMMARY")
    print("="*60)
    
    summary = report["security_summary"]
    print(f"Total Findings: {summary['total_findings']}")
    print(f"Security Score: {summary['security_score']}/100")
    print(f"Security Grade: {summary['security_grade']}")
    print(f"Audit Duration: {summary['audit_duration']}")
    
    if summary['severity_distribution']:
        print(f"\n📊 SEVERITY DISTRIBUTION:")
        for severity, count in summary['severity_distribution'].items():
            print(f"  {severity}: {count}")
    
    if report["security_recommendations"]:
        print(f"\n🎯 SECURITY RECOMMENDATIONS:")
        for i, rec in enumerate(report["security_recommendations"], 1):
            print(f"{i}. {rec}")
    
    # Save detailed report
    report_file = project_root / "STEP-83-SECURITY-AUDIT-RESULTS.md"
    with open(report_file, 'w') as f:
        f.write("# Step 83: Comprehensive Security Audit Results\n\n")
        f.write(f"**Executed**: {summary['audit_date']}\n")
        f.write(f"**Security Grade**: {summary['security_grade']}\n\n")
        
        f.write("## Executive Summary\n\n")
        f.write(f"- **Total Security Findings**: {summary['total_findings']}\n")
        f.write(f"- **Security Score**: {summary['security_score']}/100\n")
        f.write(f"- **Audit Duration**: {summary['audit_duration']}\n\n")
        
        if summary['severity_distribution']:
            f.write("## Severity Distribution\n\n")
            for severity, count in summary['severity_distribution'].items():
                f.write(f"- **{severity}**: {count}\n")
            f.write("\n")
        
        f.write("## Detailed Findings\n\n")
        for severity in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]:
            if severity in report["findings_by_severity"]:
                f.write(f"### {severity} Severity\n\n")
                for finding in report["findings_by_severity"][severity]:
                    f.write(f"**{finding['category']}**: {finding['finding']}\n")
                    f.write(f"- **File**: {finding['file']}")
                    if finding['line']:
                        f.write(f":{finding['line']}")
                    f.write(f"\n- **Description**: {finding['description']}\n")
                    f.write(f"- **Recommendation**: {finding['recommendation']}\n\n")
        
        f.write("## Security Recommendations\n\n")
        for i, rec in enumerate(report["security_recommendations"], 1):
            f.write(f"{i}. {rec}\n")
    
    print(f"\n📄 Detailed report saved: {report_file}")
    
    return summary['security_score'] >= 70  # Return success boolean

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)