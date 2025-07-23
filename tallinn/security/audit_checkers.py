#!/usr/bin/env python3
"""
Security Audit Checkers Module

Contains all individual security check implementations for the security audit system.
Each checker is focused on a specific security concern and can be used independently.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Optional


class SecurityChecker:
    """Base class for security checkers."""
    
    def __init__(self, framework_root: Path):
        self.framework_root = framework_root
    
    def check(self) -> Dict:
        """Execute the security check. To be implemented by subclasses."""
        raise NotImplementedError


class SensitiveDataChecker(SecurityChecker):
    """Check for exposed sensitive data."""
    
    def check(self) -> Dict:
        """Check for exposed sensitive data."""
        issues = []
        patterns = [
            (r'api[_-]?key\s*=\s*["\']?[a-zA-Z0-9]{20,}', 'API key'),
            (r'password\s*=\s*["\']?[^\s"\']+', 'Password'),
            (r'secret\s*=\s*["\']?[a-zA-Z0-9]{20,}', 'Secret'),
            (r'token\s*=\s*["\']?[a-zA-Z0-9]{20,}', 'Token'),
            (r'private[_-]?key\s*=\s*["\']?[a-zA-Z0-9]{20,}', 'Private key')
        ]
        
        for file_path in self.framework_root.rglob("*.md"):
            if file_path.name == "README.md":
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for pattern, data_type in patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        issues.append(f"{file_path.name}: Potential {data_type} exposure")
            except:
                pass
        
        # Check .env files
        env_files = [".env", ".env.local", ".env.production"]
        for env_file in env_files:
            if Path(env_file).exists():
                issues.append(f"{env_file} found - should be in .gitignore")
        
        return {
            "passed": len(issues) == 0,
            "risk_level": "HIGH" if issues else "LOW",
            "issues": issues,
            "recommendations": [
                "Use environment variables for sensitive data",
                "Never commit secrets to version control",
                "Implement secret scanning in CI/CD"
            ]
        }


class InputValidationChecker(SecurityChecker):
    """Check input validation implementation."""
    
    def check(self) -> Dict:
        """Check input validation implementation."""
        validation_component = self.framework_root / "components" / "validation" / "input-validation.md"
        
        if validation_component.exists():
            with open(validation_component, 'r', encoding='utf-8') as f:
                content = f.read()
            
            validation_checks = [
                "sql injection",
                "command injection",
                "path traversal",
                "script injection",
                "xml injection"
            ]
            
            found_checks = sum(1 for check in validation_checks if check in content.lower())
            coverage = found_checks / len(validation_checks) * 100
            
            return {
                "passed": coverage >= 80,
                "risk_level": "LOW" if coverage >= 80 else "MEDIUM",
                "issues": [] if coverage >= 80 else ["Incomplete input validation coverage"],
                "details": {
                    "validation_coverage": f"{coverage:.0f}%",
                    "checks_found": found_checks,
                    "total_checks": len(validation_checks)
                }
            }
        else:
            return {
                "passed": False,
                "risk_level": "HIGH",
                "issues": ["Input validation component not found"],
                "recommendations": ["Implement comprehensive input validation"]
            }


class AuthenticationChecker(SecurityChecker):
    """Check authentication and authorization mechanisms."""
    
    def check(self) -> Dict:
        """Check authentication and authorization mechanisms."""
        auth_patterns = {
            "jwt": r'jwt|jsonwebtoken',
            "oauth": r'oauth[2]?',
            "api_key": r'api[_-]?key',
            "mfa": r'multi[_-]?factor|2fa|totp',
            "rbac": r'role[_-]?based|rbac|permissions'
        }
        
        auth_found = {}
        
        for auth_type, pattern in auth_patterns.items():
            found = False
            for file_path in self.framework_root.rglob("*.md"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        if re.search(pattern, f.read(), re.IGNORECASE):
                            found = True
                            break
                except:
                    pass
            auth_found[auth_type] = found
        
        auth_score = sum(auth_found.values()) / len(auth_found) * 100
        
        return {
            "passed": auth_score >= 60,
            "risk_level": "LOW" if auth_score >= 60 else "MEDIUM",
            "issues": [f"{auth} not implemented" for auth, found in auth_found.items() if not found],
            "details": auth_found
        }


class ApiKeyManagementChecker(SecurityChecker):
    """Check API key management practices."""
    
    def check(self) -> Dict:
        """Check API key management practices."""
        issues = []
        good_practices = []
        
        # Check for .env.template
        if Path(".env.template").exists():
            good_practices.append(".env.template exists for configuration")
        else:
            issues.append("No .env.template found")
        
        # Check for hardcoded API keys
        hardcoded_keys = []
        key_pattern = r'["\']?[a-zA-Z0-9]{32,}["\']?'
        
        for file_path in Path(".").rglob("*.py"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if re.search(r'api[_-]?key\s*=\s*' + key_pattern, content):
                    hardcoded_keys.append(file_path.name)
            except:
                pass
        
        if hardcoded_keys:
            issues.append(f"Hardcoded API keys found in: {', '.join(hardcoded_keys)}")
        
        # Check for key rotation and encryption
        if not Path("api_key_rotation.json").exists():
            issues.append("No API key rotation policy found")
        
        # Check for secure API key manager
        if Path("secure_api_key_manager.py").exists():
            good_practices.append("Secure API key encryption system implemented")
        else:
            issues.append("No secure API key encryption system found")
        
        return {
            "passed": len(issues) == 0,
            "risk_level": "HIGH" if hardcoded_keys else "MEDIUM" if issues else "LOW",
            "issues": issues,
            "good_practices": good_practices,
            "recommendations": [
                "Use secure API key encryption system",
                "Implement regular key rotation",
                "Store keys in encrypted format",
                "Use environment variables for runtime keys"
            ]
        }


class DependencyChecker(SecurityChecker):
    """Check for dependency vulnerabilities."""
    
    def check(self) -> Dict:
        """Check for dependency vulnerabilities."""
        req_file = Path("requirements.txt")
        
        if req_file.exists():
            with open(req_file, 'r') as f:
                dependencies = f.read().strip().split('\n')
            
            # Check for known vulnerable versions (simplified check)
            vulnerable_patterns = {
                'requests<2.20': 'CVE-2018-18074',
                'cryptography<3.4.8': 'Multiple CVEs',
                'django<2.2': 'Multiple vulnerabilities',
                'flask<1.0': 'Security issues'
            }
            
            vulnerabilities = []
            for dep in dependencies:
                dep_clean = dep.split('>=')[0].split('==')[0].split('<')[0].strip()
                for pattern, vuln in vulnerable_patterns.items():
                    pattern_name = pattern.split('<')[0]
                    if pattern_name == dep_clean:
                        # Check version constraint
                        required_version = pattern.split('<')[1]
                        if '>=' not in dep or not self._version_meets_requirement(dep, required_version):
                            vulnerabilities.append(f"{dep}: {vuln}")
            
            return {
                "passed": len(vulnerabilities) == 0,
                "risk_level": "HIGH" if vulnerabilities else "LOW",
                "issues": vulnerabilities,
                "details": {
                    "total_dependencies": len(dependencies),
                    "vulnerable": len(vulnerabilities)
                }
            }
        else:
            return {
                "passed": False,
                "risk_level": "MEDIUM",
                "issues": ["requirements.txt not found"],
                "recommendations": ["Create requirements.txt with version constraints"]
            }
    
    def _version_meets_requirement(self, dependency_line: str, min_version: str) -> bool:
        """Check if dependency version meets minimum requirement."""
        try:
            if '>=' in dependency_line:
                actual_version = dependency_line.split('>=')[1].strip()
                # Simple version comparison (works for most cases)
                actual_parts = [int(x) for x in actual_version.split('.')]
                min_parts = [int(x) for x in min_version.split('.')]
                
                for i in range(max(len(actual_parts), len(min_parts))):
                    actual = actual_parts[i] if i < len(actual_parts) else 0
                    minimum = min_parts[i] if i < len(min_parts) else 0
                    if actual > minimum:
                        return True
                    elif actual < minimum:
                        return False
                return True
            return False
        except:
            return False


class ConfigurationSecurityChecker(SecurityChecker):
    """Check configuration security."""
    
    def check(self) -> Dict:
        """Check configuration security."""
        config_issues = []
        
        # Check settings.local.json
        settings_file = Path("settings.local.json")
        if settings_file.exists():
            with open(settings_file, 'r') as f:
                settings = json.load(f)
            
            # Check for overly permissive settings
            if 'permissions' in settings:
                allows = settings['permissions'].get('allow', [])
                if any('*' in allow for allow in allows):
                    config_issues.append("Overly permissive wildcard in settings")
        
        # Check for secure defaults
        config_files = list(Path(".").glob("*config*.json"))
        if not config_files:
            config_issues.append("No configuration files found")
        
        return {
            "passed": len(config_issues) == 0,
            "risk_level": "LOW" if len(config_issues) == 0 else "MEDIUM",
            "issues": config_issues,
            "recommendations": [
                "Use least privilege principle",
                "Implement secure defaults",
                "Separate dev/prod configurations"
            ]
        }


class OWASPComplianceChecker(SecurityChecker):
    """Check OWASP compliance."""
    
    def check(self) -> Dict:
        """Check OWASP compliance."""
        owasp_component = self.framework_root / "components" / "security" / "owasp-compliance.md"
        
        if owasp_component.exists():
            with open(owasp_component, 'r', encoding='utf-8') as f:
                content = f.read()
            
            owasp_checks = [
                "injection",
                "broken authentication",
                "sensitive data",
                "xxe",
                "broken access",
                "security misconfiguration",
                "xss",
                "deserialization",
                "components with vulnerabilities",
                "logging"
            ]
            
            found = sum(1 for check in owasp_checks if check in content.lower())
            coverage = found / len(owasp_checks) * 100
            
            return {
                "passed": coverage >= 70,
                "risk_level": "LOW" if coverage >= 70 else "MEDIUM",
                "issues": [] if coverage >= 70 else ["Incomplete OWASP coverage"],
                "details": {
                    "coverage": f"{coverage:.0f}%",
                    "checks_found": found
                }
            }
        else:
            return {
                "passed": False,
                "risk_level": "HIGH",
                "issues": ["OWASP compliance component not found"],
                "recommendations": ["Implement OWASP Top 10 compliance"]
            }


class InjectionPreventionChecker(SecurityChecker):
    """Check code injection prevention measures."""
    
    def check(self) -> Dict:
        """Check code injection prevention measures."""
        injection_patterns = [
            r'eval\s*\(',
            r'exec\s*\(',
            r'os\.system\s*\(',
            r'subprocess\.call\s*\(',
            r'shell\s*=\s*True'
        ]
        
        dangerous_code = []
        
        for file_path in Path(".").rglob("*.py"):
            # Skip this security audit script itself
            if file_path.name == "security_audit.py":
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for pattern in injection_patterns:
                    if re.search(pattern, content):
                        dangerous_code.append(f"{file_path.name}: {pattern}")
            except:
                pass
        
        # Additional security features
        security_features = []
        
        # Check for secure API key manager
        if Path("secure_api_key_manager.py").exists():
            security_features.append("Secure API key encryption system present")
        
        return {
            "passed": len(dangerous_code) == 0,
            "risk_level": "HIGH" if dangerous_code else "LOW",
            "issues": dangerous_code,
            "security_features": security_features,
            "recommendations": [
                "Avoid eval() and exec()",
                "Use subprocess with shell=False",
                "Implement proper input sanitization",
                "Use secure API key management"
            ]
        }


class ErrorHandlingChecker(SecurityChecker):
    """Check error handling and information disclosure."""
    
    def check(self) -> Dict:
        """Check error handling and information disclosure."""
        error_patterns = {
            "stack_trace": r'traceback|stack[_-]?trace',
            "debug_mode": r'debug\s*=\s*True',
            "verbose_errors": r'verbose|detailed[_-]?error'
        }
        
        issues = []
        
        for pattern_name, pattern in error_patterns.items():
            for file_path in Path(".").rglob("*.py"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        if re.search(pattern, f.read(), re.IGNORECASE):
                            issues.append(f"{file_path.name}: Potential {pattern_name} exposure")
                except:
                    pass
        
        return {
            "passed": len(issues) <= 2,  # Allow some error handling
            "risk_level": "LOW" if len(issues) <= 2 else "MEDIUM",
            "issues": issues,
            "recommendations": [
                "Implement generic error messages for production",
                "Log detailed errors securely",
                "Disable debug mode in production"
            ]
        }


class LoggingSecurityChecker(SecurityChecker):
    """Check logging and monitoring security."""
    
    def check(self) -> Dict:
        """Check logging and monitoring security."""
        logging_checks = {
            "no_sensitive_logging": True,
            "secure_log_storage": False,
            "log_monitoring": False,
            "audit_trails": False
        }
        
        # Check for logging patterns
        for file_path in Path(".").rglob("*.py"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for sensitive data in logs
                if re.search(r'log.*password|log.*api[_-]?key|log.*secret', content, re.IGNORECASE):
                    logging_checks["no_sensitive_logging"] = False
                
                # Check for audit trails
                if re.search(r'audit[_-]?log|audit[_-]?trail', content, re.IGNORECASE):
                    logging_checks["audit_trails"] = True
            except:
                pass
        
        score = sum(logging_checks.values()) / len(logging_checks) * 100
        
        return {
            "passed": score >= 50,
            "risk_level": "LOW" if score >= 50 else "MEDIUM",
            "issues": [k.replace('_', ' ').title() for k, v in logging_checks.items() if not v],
            "details": logging_checks
        }