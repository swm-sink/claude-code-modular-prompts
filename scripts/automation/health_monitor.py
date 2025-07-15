#!/usr/bin/env python3
"""
Framework Health Monitoring for Claude Code Framework

Comprehensive health monitoring system that:
- Monitors framework component health and performance
- Tracks quality metrics and compliance
- Detects configuration drift and issues
- Provides real-time alerts and recommendations
- Generates health reports and trends
- Integrates with CI/CD for continuous monitoring

Author: Claude Code Framework - Phase 2.2 Automation
Version: 1.0.0
Date: 2025-07-15
"""

import os
import sys
import json
import time
import psutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union
import argparse
import logging
from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime, timedelta
import hashlib


class HealthStatus(Enum):
    """Health check status levels"""
    HEALTHY = "healthy"
    WARNING = "warning"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


class MonitoringCategory(Enum):
    """Categories of health monitoring"""
    FRAMEWORK = "framework"
    CONFIGURATION = "configuration"
    PERFORMANCE = "performance"
    QUALITY = "quality"
    SECURITY = "security"
    DEPENDENCIES = "dependencies"
    RESOURCES = "resources"


@dataclass
class HealthCheck:
    """Individual health check result"""
    name: str
    category: MonitoringCategory
    status: HealthStatus
    value: Union[str, int, float]
    threshold: Optional[Union[str, int, float]]
    message: str
    timestamp: datetime
    duration: float


@dataclass
class HealthReport:
    """Complete health monitoring report"""
    timestamp: datetime
    overall_status: HealthStatus
    checks: List[HealthCheck]
    summary: Dict[str, Any]
    recommendations: List[str]
    alerts: List[str]


class FrameworkHealthMonitor:
    """Main framework health monitoring system"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path.cwd()
        self.logger = logging.getLogger(__name__)
        
        # Health check configurations
        self.thresholds = {
            'config_completeness': 80,  # percentage
            'test_coverage': 90,        # percentage
            'performance_response': 200, # milliseconds
            'memory_usage': 80,         # percentage
            'disk_usage': 85,           # percentage
            'dependency_age': 365,      # days
            'file_count': 10000,        # maximum files
        }
        
        # Load project configuration
        self.project_config = self._load_project_config()
        
        # Update thresholds from project config
        self._update_thresholds_from_config()
    
    def _load_project_config(self) -> Dict[str, Any]:
        """Load PROJECT_CONFIG.xml settings"""
        config_file = self.project_root / "PROJECT_CONFIG.xml"
        config = {}
        
        if config_file.exists():
            try:
                import xml.etree.ElementTree as ET
                tree = ET.parse(config_file)
                root = tree.getroot()
                
                # Extract all configuration recursively
                def extract_config(element, path=""):
                    for child in element:
                        child_path = f"{path}.{child.tag}" if path else child.tag
                        if child.text and child.text.strip():
                            config[child_path] = child.text.strip()
                        extract_config(child, child_path)
                
                extract_config(root)
                
            except Exception as e:
                self.logger.warning(f"Could not parse PROJECT_CONFIG.xml: {e}")
        
        return config
    
    def _update_thresholds_from_config(self):
        """Update health thresholds from project configuration"""
        # Test coverage threshold
        if 'quality_standards.test_coverage.threshold' in self.project_config:
            try:
                self.thresholds['test_coverage'] = int(self.project_config['quality_standards.test_coverage.threshold'])
            except ValueError:
                pass
        
        # Performance threshold
        if 'quality_standards.performance.response_time_p95' in self.project_config:
            try:
                perf_text = self.project_config['quality_standards.performance.response_time_p95']
                self.thresholds['performance_response'] = int(perf_text.replace('ms', ''))
            except ValueError:
                pass
    
    def run_health_check(self, categories: Optional[List[MonitoringCategory]] = None) -> HealthReport:
        """Run comprehensive health check"""
        print("🏥 Running framework health check...")
        
        if categories is None:
            categories = list(MonitoringCategory)
        
        all_checks = []
        start_time = datetime.now()
        
        # Run health checks by category
        for category in categories:
            print(f"   📋 Checking {category.value}...")
            category_checks = self._run_category_checks(category)
            all_checks.extend(category_checks)
        
        # Calculate overall status
        overall_status = self._calculate_overall_status(all_checks)
        
        # Generate summary
        summary = self._generate_summary(all_checks)
        
        # Generate recommendations and alerts
        recommendations = self._generate_recommendations(all_checks)
        alerts = self._generate_alerts(all_checks)
        
        return HealthReport(
            timestamp=start_time,
            overall_status=overall_status,
            checks=all_checks,
            summary=summary,
            recommendations=recommendations,
            alerts=alerts
        )
    
    def _run_category_checks(self, category: MonitoringCategory) -> List[HealthCheck]:
        """Run health checks for a specific category"""
        if category == MonitoringCategory.FRAMEWORK:
            return self._check_framework_health()
        elif category == MonitoringCategory.CONFIGURATION:
            return self._check_configuration_health()
        elif category == MonitoringCategory.PERFORMANCE:
            return self._check_performance_health()
        elif category == MonitoringCategory.QUALITY:
            return self._check_quality_health()
        elif category == MonitoringCategory.SECURITY:
            return self._check_security_health()
        elif category == MonitoringCategory.DEPENDENCIES:
            return self._check_dependencies_health()
        elif category == MonitoringCategory.RESOURCES:
            return self._check_resources_health()
        else:
            return []
    
    def _check_framework_health(self) -> List[HealthCheck]:
        """Check framework-specific health"""
        checks = []
        
        # Check CLAUDE.md existence and validity
        claude_md = self.project_root / "CLAUDE.md"
        check_start = time.time()
        
        if claude_md.exists():
            try:
                with open(claude_md) as f:
                    content = f.read()
                
                # Check for framework indicators
                has_version = 'version' in content.lower()
                has_commands = any(cmd in content for cmd in ['/auto', '/task', '/feature'])
                has_config = 'PROJECT_CONFIG' in content
                
                if has_version and has_commands and has_config:
                    status = HealthStatus.HEALTHY
                    message = "CLAUDE.md framework file is properly configured"
                elif has_commands:
                    status = HealthStatus.WARNING
                    message = "CLAUDE.md exists but may be incomplete"
                else:
                    status = HealthStatus.CRITICAL
                    message = "CLAUDE.md exists but appears invalid"
            except Exception as e:
                status = HealthStatus.CRITICAL
                message = f"CLAUDE.md read error: {e}"
        else:
            status = HealthStatus.CRITICAL
            message = "CLAUDE.md not found - framework not initialized"
        
        checks.append(HealthCheck(
            name="Framework File",
            category=MonitoringCategory.FRAMEWORK,
            status=status,
            value="present" if claude_md.exists() else "missing",
            threshold="present",
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        # Check .claude directory structure
        check_start = time.time()
        claude_dir = self.project_root / ".claude"
        
        if claude_dir.exists():
            subdirs = ['modules', 'commands', 'system']
            existing_subdirs = [d.name for d in claude_dir.iterdir() if d.is_dir()]
            missing_subdirs = [d for d in subdirs if d not in existing_subdirs]
            
            if not missing_subdirs:
                status = HealthStatus.HEALTHY
                message = f"Framework directory structure complete ({len(existing_subdirs)} directories)"
            else:
                status = HealthStatus.WARNING
                message = f"Missing framework directories: {missing_subdirs}"
            
            value = f"{len(existing_subdirs)}/{len(subdirs)} directories"
        else:
            status = HealthStatus.WARNING
            message = "Framework directory structure not initialized"
            value = "missing"
        
        checks.append(HealthCheck(
            name="Framework Structure",
            category=MonitoringCategory.FRAMEWORK,
            status=status,
            value=value,
            threshold="complete",
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        return checks
    
    def _check_configuration_health(self) -> List[HealthCheck]:
        """Check configuration health"""
        checks = []
        
        # Check PROJECT_CONFIG.xml
        check_start = time.time()
        config_file = self.project_root / "PROJECT_CONFIG.xml"
        
        if config_file.exists():
            try:
                # Use the unified validator if available
                sys.path.append(str(self.project_root / "scripts" / "validation"))
                try:
                    from project_config_validator import UnifiedProjectConfigValidator
                    validator = UnifiedProjectConfigValidator(self.project_root)
                    result = validator.validate(enable_placeholder_testing=False)
                    
                    if result.is_valid:
                        status = HealthStatus.HEALTHY
                        message = f"Configuration valid (confidence: {result.confidence_score:.1%})"
                        value = f"{result.confidence_score:.1%}"
                    else:
                        error_count = len([i for i in result.issues if i.level.value == 'error'])
                        if error_count > 0:
                            status = HealthStatus.CRITICAL
                            message = f"Configuration has {error_count} errors"
                        else:
                            status = HealthStatus.WARNING
                            message = f"Configuration has {len(result.issues)} issues"
                        value = f"{len(result.issues)} issues"
                    
                except ImportError:
                    # Fallback to basic XML validation
                    import xml.etree.ElementTree as ET
                    tree = ET.parse(config_file)
                    status = HealthStatus.HEALTHY
                    message = "Configuration file is valid XML"
                    value = "valid"
                
            except Exception as e:
                status = HealthStatus.CRITICAL
                message = f"Configuration error: {e}"
                value = "invalid"
        else:
            status = HealthStatus.WARNING
            message = "PROJECT_CONFIG.xml not found - using defaults"
            value = "missing"
        
        checks.append(HealthCheck(
            name="Project Configuration",
            category=MonitoringCategory.CONFIGURATION,
            status=status,
            value=value,
            threshold="valid",
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        # Check configuration completeness
        check_start = time.time()
        required_sections = [
            'project_info.name',
            'project_info.primary_language',
            'project_structure.source_directory',
            'quality_standards.test_coverage.threshold'
        ]
        
        present_sections = sum(1 for section in required_sections if section in self.project_config)
        completeness = (present_sections / len(required_sections)) * 100
        
        if completeness >= self.thresholds['config_completeness']:
            status = HealthStatus.HEALTHY
        elif completeness >= 60:
            status = HealthStatus.WARNING
        else:
            status = HealthStatus.CRITICAL
        
        checks.append(HealthCheck(
            name="Configuration Completeness",
            category=MonitoringCategory.CONFIGURATION,
            status=status,
            value=completeness,
            threshold=self.thresholds['config_completeness'],
            message=f"Configuration {completeness:.0f}% complete",
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        return checks
    
    def _check_performance_health(self) -> List[HealthCheck]:
        """Check performance health"""
        checks = []
        
        # Check framework response time (simulate command execution)
        check_start = time.time()
        
        try:
            # Simple performance test - validate configuration
            start_time = time.time()
            config_file = self.project_root / "PROJECT_CONFIG.xml"
            if config_file.exists():
                import xml.etree.ElementTree as ET
                ET.parse(config_file)
            response_time = (time.time() - start_time) * 1000  # Convert to ms
            
            if response_time <= self.thresholds['performance_response']:
                status = HealthStatus.HEALTHY
            elif response_time <= self.thresholds['performance_response'] * 2:
                status = HealthStatus.WARNING
            else:
                status = HealthStatus.CRITICAL
            
            message = f"Framework response time: {response_time:.1f}ms"
            
        except Exception as e:
            response_time = 0
            status = HealthStatus.CRITICAL
            message = f"Performance test failed: {e}"
        
        checks.append(HealthCheck(
            name="Framework Response Time",
            category=MonitoringCategory.PERFORMANCE,
            status=status,
            value=response_time,
            threshold=self.thresholds['performance_response'],
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        # Check file system performance
        check_start = time.time()
        
        try:
            file_count = len(list(self.project_root.glob("**/*")))
            
            if file_count <= self.thresholds['file_count']:
                status = HealthStatus.HEALTHY
                message = f"Project size manageable: {file_count} files"
            elif file_count <= self.thresholds['file_count'] * 1.5:
                status = HealthStatus.WARNING
                message = f"Large project: {file_count} files (may impact performance)"
            else:
                status = HealthStatus.CRITICAL
                message = f"Very large project: {file_count} files (performance impact likely)"
            
        except Exception as e:
            file_count = 0
            status = HealthStatus.UNKNOWN
            message = f"File count check failed: {e}"
        
        checks.append(HealthCheck(
            name="Project Size",
            category=MonitoringCategory.PERFORMANCE,
            status=status,
            value=file_count,
            threshold=self.thresholds['file_count'],
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        return checks
    
    def _check_quality_health(self) -> List[HealthCheck]:
        """Check code quality health"""
        checks = []
        
        # Check test coverage if available
        check_start = time.time()
        
        try:
            # Try to find coverage report
            coverage_files = [
                self.project_root / "coverage.xml",
                self.project_root / ".coverage",
                self.project_root / "htmlcov" / "index.html",
                self.project_root / "coverage" / "lcov.info"
            ]
            
            coverage_found = any(f.exists() for f in coverage_files)
            
            if coverage_found:
                # Try to extract coverage percentage
                coverage_pct = self._extract_coverage_from_files(coverage_files)
                
                if coverage_pct is not None:
                    if coverage_pct >= self.thresholds['test_coverage']:
                        status = HealthStatus.HEALTHY
                    elif coverage_pct >= self.thresholds['test_coverage'] * 0.8:
                        status = HealthStatus.WARNING
                    else:
                        status = HealthStatus.CRITICAL
                    
                    message = f"Test coverage: {coverage_pct:.1f}%"
                    value = coverage_pct
                else:
                    status = HealthStatus.WARNING
                    message = "Coverage reports found but percentage unclear"
                    value = "unknown"
            else:
                status = HealthStatus.WARNING
                message = "No test coverage reports found"
                value = 0
                
        except Exception as e:
            status = HealthStatus.UNKNOWN
            message = f"Coverage check failed: {e}"
            value = 0
        
        checks.append(HealthCheck(
            name="Test Coverage",
            category=MonitoringCategory.QUALITY,
            status=status,
            value=value,
            threshold=self.thresholds['test_coverage'],
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        # Check for test files
        check_start = time.time()
        
        test_dirs = ['tests', 'test', '__tests__', 'spec']
        test_files_found = []
        
        for test_dir in test_dirs:
            test_path = self.project_root / test_dir
            if test_path.exists():
                test_files = list(test_path.glob("**/*.py")) + list(test_path.glob("**/*.js")) + list(test_path.glob("**/*.ts"))
                test_files_found.extend(test_files)
        
        if test_files_found:
            status = HealthStatus.HEALTHY
            message = f"Found {len(test_files_found)} test files"
            value = len(test_files_found)
        else:
            status = HealthStatus.WARNING
            message = "No test files found"
            value = 0
        
        checks.append(HealthCheck(
            name="Test Files",
            category=MonitoringCategory.QUALITY,
            status=status,
            value=value,
            threshold=1,
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        return checks
    
    def _check_security_health(self) -> List[HealthCheck]:
        """Check security health"""
        checks = []
        
        # Check for .gitignore
        check_start = time.time()
        gitignore = self.project_root / ".gitignore"
        
        if gitignore.exists():
            try:
                with open(gitignore) as f:
                    content = f.read()
                
                # Check for common security patterns
                security_patterns = [
                    '.env', '*.key', '*.pem', 'secrets', 'config.json',
                    'node_modules', '__pycache__', '*.log'
                ]
                
                patterns_found = sum(1 for pattern in security_patterns if pattern in content)
                coverage = (patterns_found / len(security_patterns)) * 100
                
                if coverage >= 70:
                    status = HealthStatus.HEALTHY
                    message = f"Good .gitignore coverage ({coverage:.0f}%)"
                elif coverage >= 40:
                    status = HealthStatus.WARNING
                    message = f"Partial .gitignore coverage ({coverage:.0f}%)"
                else:
                    status = HealthStatus.CRITICAL
                    message = f"Poor .gitignore coverage ({coverage:.0f}%)"
                
                value = coverage
                
            except Exception as e:
                status = HealthStatus.WARNING
                message = f"Could not read .gitignore: {e}"
                value = 0
        else:
            status = HealthStatus.WARNING
            message = ".gitignore not found"
            value = 0
        
        checks.append(HealthCheck(
            name="Git Security",
            category=MonitoringCategory.SECURITY,
            status=status,
            value=value,
            threshold=70,
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        # Check for exposed secrets (basic check)
        check_start = time.time()
        
        try:
            # Look for common secret patterns in tracked files
            secret_patterns = [
                'password', 'api_key', 'secret_key', 'token', 'private_key'
            ]
            
            git_files = subprocess.run(
                ['git', 'ls-files'],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )
            
            if git_files.returncode == 0:
                tracked_files = git_files.stdout.strip().split('\n')
                potential_secrets = 0
                
                for file_path in tracked_files[:50]:  # Check first 50 files
                    full_path = self.project_root / file_path
                    if full_path.exists() and full_path.suffix in ['.py', '.js', '.ts', '.json', '.yaml', '.yml']:
                        try:
                            with open(full_path, encoding='utf-8', errors='ignore') as f:
                                content = f.read().lower()
                                for pattern in secret_patterns:
                                    if f'{pattern}=' in content or f'{pattern}:' in content:
                                        potential_secrets += 1
                                        break
                        except:
                            continue
                
                if potential_secrets == 0:
                    status = HealthStatus.HEALTHY
                    message = "No obvious secrets detected in tracked files"
                elif potential_secrets <= 2:
                    status = HealthStatus.WARNING
                    message = f"Potential secrets detected in {potential_secrets} files"
                else:
                    status = HealthStatus.CRITICAL
                    message = f"Multiple potential secrets detected in {potential_secrets} files"
                
                value = potential_secrets
            else:
                status = HealthStatus.UNKNOWN
                message = "Could not check git files"
                value = 0
                
        except Exception as e:
            status = HealthStatus.UNKNOWN
            message = f"Secret scan failed: {e}"
            value = 0
        
        checks.append(HealthCheck(
            name="Secret Detection",
            category=MonitoringCategory.SECURITY,
            status=status,
            value=value,
            threshold=0,
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        return checks
    
    def _check_dependencies_health(self) -> List[HealthCheck]:
        """Check dependency health"""
        checks = []
        
        # Check Python dependencies
        if (self.project_root / "requirements.txt").exists():
            check = self._check_python_dependencies()
            checks.append(check)
        
        # Check Node.js dependencies
        if (self.project_root / "package.json").exists():
            check = self._check_nodejs_dependencies()
            checks.append(check)
        
        # Check Go dependencies
        if (self.project_root / "go.mod").exists():
            check = self._check_go_dependencies()
            checks.append(check)
        
        return checks
    
    def _check_python_dependencies(self) -> HealthCheck:
        """Check Python dependencies health"""
        check_start = time.time()
        
        try:
            with open(self.project_root / "requirements.txt") as f:
                deps = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            # Check if requirements are pinned
            pinned_deps = sum(1 for dep in deps if '==' in dep or '>=' in dep)
            pinning_ratio = (pinned_deps / len(deps)) * 100 if deps else 0
            
            if pinning_ratio >= 80:
                status = HealthStatus.HEALTHY
                message = f"Python dependencies well-pinned ({pinning_ratio:.0f}%)"
            elif pinning_ratio >= 50:
                status = HealthStatus.WARNING
                message = f"Some Python dependencies unpinned ({pinning_ratio:.0f}%)"
            else:
                status = HealthStatus.CRITICAL
                message = f"Many Python dependencies unpinned ({pinning_ratio:.0f}%)"
            
            value = f"{len(deps)} dependencies"
            
        except Exception as e:
            status = HealthStatus.UNKNOWN
            message = f"Could not check Python dependencies: {e}"
            value = "unknown"
        
        return HealthCheck(
            name="Python Dependencies",
            category=MonitoringCategory.DEPENDENCIES,
            status=status,
            value=value,
            threshold="pinned",
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        )
    
    def _check_nodejs_dependencies(self) -> HealthCheck:
        """Check Node.js dependencies health"""
        check_start = time.time()
        
        try:
            with open(self.project_root / "package.json") as f:
                package_data = json.load(f)
            
            deps = package_data.get('dependencies', {})
            dev_deps = package_data.get('devDependencies', {})
            total_deps = len(deps) + len(dev_deps)
            
            # Check for lock file
            has_lock = (self.project_root / "package-lock.json").exists() or (self.project_root / "yarn.lock").exists()
            
            if has_lock:
                status = HealthStatus.HEALTHY
                message = f"Node.js dependencies locked ({total_deps} total)"
            else:
                status = HealthStatus.WARNING
                message = f"Node.js dependencies not locked ({total_deps} total)"
            
            value = f"{total_deps} dependencies"
            
        except Exception as e:
            status = HealthStatus.UNKNOWN
            message = f"Could not check Node.js dependencies: {e}"
            value = "unknown"
        
        return HealthCheck(
            name="Node.js Dependencies",
            category=MonitoringCategory.DEPENDENCIES,
            status=status,
            value=value,
            threshold="locked",
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        )
    
    def _check_go_dependencies(self) -> HealthCheck:
        """Check Go dependencies health"""
        check_start = time.time()
        
        try:
            # Check go.mod and go.sum
            has_mod = (self.project_root / "go.mod").exists()
            has_sum = (self.project_root / "go.sum").exists()
            
            if has_mod and has_sum:
                status = HealthStatus.HEALTHY
                message = "Go dependencies properly managed"
                value = "managed"
            elif has_mod:
                status = HealthStatus.WARNING
                message = "Go mod file exists but no sum file"
                value = "partial"
            else:
                status = HealthStatus.CRITICAL
                message = "Go dependencies not managed"
                value = "unmanaged"
            
        except Exception as e:
            status = HealthStatus.UNKNOWN
            message = f"Could not check Go dependencies: {e}"
            value = "unknown"
        
        return HealthCheck(
            name="Go Dependencies",
            category=MonitoringCategory.DEPENDENCIES,
            status=status,
            value=value,
            threshold="managed",
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        )
    
    def _check_resources_health(self) -> List[HealthCheck]:
        """Check system resource health"""
        checks = []
        
        # Memory usage
        check_start = time.time()
        try:
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            
            if memory_percent <= self.thresholds['memory_usage']:
                status = HealthStatus.HEALTHY
            elif memory_percent <= 90:
                status = HealthStatus.WARNING
            else:
                status = HealthStatus.CRITICAL
            
            message = f"Memory usage: {memory_percent:.1f}%"
            
        except Exception as e:
            memory_percent = 0
            status = HealthStatus.UNKNOWN
            message = f"Memory check failed: {e}"
        
        checks.append(HealthCheck(
            name="Memory Usage",
            category=MonitoringCategory.RESOURCES,
            status=status,
            value=memory_percent,
            threshold=self.thresholds['memory_usage'],
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        # Disk usage
        check_start = time.time()
        try:
            disk = psutil.disk_usage(str(self.project_root))
            disk_percent = (disk.used / disk.total) * 100
            
            if disk_percent <= self.thresholds['disk_usage']:
                status = HealthStatus.HEALTHY
            elif disk_percent <= 95:
                status = HealthStatus.WARNING
            else:
                status = HealthStatus.CRITICAL
            
            message = f"Disk usage: {disk_percent:.1f}%"
            
        except Exception as e:
            disk_percent = 0
            status = HealthStatus.UNKNOWN
            message = f"Disk check failed: {e}"
        
        checks.append(HealthCheck(
            name="Disk Usage",
            category=MonitoringCategory.RESOURCES,
            status=status,
            value=disk_percent,
            threshold=self.thresholds['disk_usage'],
            message=message,
            timestamp=datetime.now(),
            duration=time.time() - check_start
        ))
        
        return checks
    
    def _extract_coverage_from_files(self, coverage_files: List[Path]) -> Optional[float]:
        """Extract coverage percentage from coverage files"""
        for coverage_file in coverage_files:
            if not coverage_file.exists():
                continue
            
            try:
                if coverage_file.name == "coverage.xml":
                    # Parse XML coverage report
                    import xml.etree.ElementTree as ET
                    tree = ET.parse(coverage_file)
                    root = tree.getroot()
                    
                    # Look for coverage percentage
                    for elem in root.iter():
                        if 'line-rate' in elem.attrib:
                            return float(elem.attrib['line-rate']) * 100
                
                elif coverage_file.name == "index.html":
                    # Parse HTML coverage report
                    with open(coverage_file) as f:
                        content = f.read()
                    
                    # Look for percentage patterns
                    import re
                    match = re.search(r'(\d+)%', content)
                    if match:
                        return float(match.group(1))
                
            except Exception:
                continue
        
        return None
    
    def _calculate_overall_status(self, checks: List[HealthCheck]) -> HealthStatus:
        """Calculate overall health status"""
        if not checks:
            return HealthStatus.UNKNOWN
        
        # Count status types
        status_counts = {}
        for check in checks:
            status_counts[check.status] = status_counts.get(check.status, 0) + 1
        
        # Determine overall status
        if status_counts.get(HealthStatus.CRITICAL, 0) > 0:
            return HealthStatus.CRITICAL
        elif status_counts.get(HealthStatus.WARNING, 0) > 0:
            return HealthStatus.WARNING
        elif status_counts.get(HealthStatus.HEALTHY, 0) > 0:
            return HealthStatus.HEALTHY
        else:
            return HealthStatus.UNKNOWN
    
    def _generate_summary(self, checks: List[HealthCheck]) -> Dict[str, Any]:
        """Generate health check summary"""
        summary = {
            'total_checks': len(checks),
            'by_status': {},
            'by_category': {},
            'total_duration': sum(check.duration for check in checks),
            'critical_issues': [],
            'warning_issues': []
        }
        
        # Count by status
        for status in HealthStatus:
            count = len([c for c in checks if c.status == status])
            summary['by_status'][status.value] = count
        
        # Count by category
        for category in MonitoringCategory:
            count = len([c for c in checks if c.category == category])
            summary['by_category'][category.value] = count
        
        # Collect issues
        for check in checks:
            if check.status == HealthStatus.CRITICAL:
                summary['critical_issues'].append(check.name)
            elif check.status == HealthStatus.WARNING:
                summary['warning_issues'].append(check.name)
        
        return summary
    
    def _generate_recommendations(self, checks: List[HealthCheck]) -> List[str]:
        """Generate health recommendations"""
        recommendations = []
        
        # Check for common issues and provide recommendations
        for check in checks:
            if check.status in [HealthStatus.CRITICAL, HealthStatus.WARNING]:
                if check.name == "Framework File" and check.status == HealthStatus.CRITICAL:
                    recommendations.append("Run project initialization: python scripts/automation/project_initializer.py")
                
                elif check.name == "Project Configuration" and check.status == HealthStatus.CRITICAL:
                    recommendations.append("Validate and fix configuration: python scripts/validation/project_config_validator.py")
                
                elif check.name == "Test Coverage" and check.status in [HealthStatus.WARNING, HealthStatus.CRITICAL]:
                    recommendations.append("Improve test coverage: python scripts/automation/test_runner.py")
                
                elif check.name == "Secret Detection" and check.status == HealthStatus.CRITICAL:
                    recommendations.append("Review and remove potential secrets from tracked files")
                
                elif "Dependencies" in check.name and check.status == HealthStatus.WARNING:
                    recommendations.append(f"Update dependency management for {check.name.lower()}")
                
                elif check.category == MonitoringCategory.RESOURCES and check.status == HealthStatus.CRITICAL:
                    recommendations.append(f"Address {check.name.lower()} resource constraint")
        
        # Add general recommendations
        if not any("Framework" in r for r in recommendations):
            recommendations.append("Regular health monitoring: python scripts/automation/health_monitor.py --schedule")
        
        return list(set(recommendations))  # Remove duplicates
    
    def _generate_alerts(self, checks: List[HealthCheck]) -> List[str]:
        """Generate health alerts"""
        alerts = []
        
        critical_checks = [c for c in checks if c.status == HealthStatus.CRITICAL]
        
        if critical_checks:
            alerts.append(f"🚨 {len(critical_checks)} critical health issues detected!")
        
        # Specific alerts
        for check in critical_checks:
            if check.name == "Framework File":
                alerts.append("❌ Framework not initialized - project may not work properly")
            elif check.name == "Project Configuration":
                alerts.append("❌ Configuration errors - framework may malfunction")
            elif check.name == "Secret Detection":
                alerts.append("🔒 Potential secrets detected - security risk")
            elif check.category == MonitoringCategory.RESOURCES:
                alerts.append(f"💾 {check.name} critically high - performance impact")
        
        return alerts
    
    def print_health_report(self, report: HealthReport, detailed: bool = False):
        """Print formatted health report"""
        # Overall status
        status_icons = {
            HealthStatus.HEALTHY: "✅",
            HealthStatus.WARNING: "⚠️",
            HealthStatus.CRITICAL: "❌",
            HealthStatus.UNKNOWN: "❓"
        }
        
        icon = status_icons[report.overall_status]
        print(f"\n🏥 Framework Health Report {icon}")
        print(f"Overall Status: {report.overall_status.value.upper()}")
        print(f"Timestamp: {report.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Checks: {report.summary['total_checks']}")
        print(f"Duration: {report.summary['total_duration']:.2f}s")
        
        # Status summary
        print(f"\n📊 Status Summary:")
        for status, count in report.summary['by_status'].items():
            if count > 0:
                icon = status_icons[HealthStatus(status)]
                print(f"   {icon} {status.title()}: {count}")
        
        # Alerts
        if report.alerts:
            print(f"\n🚨 Alerts:")
            for alert in report.alerts:
                print(f"   {alert}")
        
        # Category breakdown
        if detailed:
            print(f"\n📋 Category Breakdown:")
            for category, count in report.summary['by_category'].items():
                if count > 0:
                    print(f"   {category.title()}: {count} checks")
        
        # Critical and warning issues
        if report.summary['critical_issues']:
            print(f"\n❌ Critical Issues:")
            for issue in report.summary['critical_issues']:
                print(f"   • {issue}")
        
        if report.summary['warning_issues']:
            print(f"\n⚠️ Warning Issues:")
            for issue in report.summary['warning_issues']:
                print(f"   • {issue}")
        
        # Recommendations
        if report.recommendations:
            print(f"\n💡 Recommendations:")
            for rec in report.recommendations:
                print(f"   • {rec}")
        
        # Detailed check results
        if detailed:
            print(f"\n📝 Detailed Results:")
            for check in report.checks:
                icon = status_icons[check.status]
                print(f"   {icon} {check.name}: {check.message}")
                if isinstance(check.value, (int, float)) and check.threshold:
                    print(f"      Value: {check.value} (threshold: {check.threshold})")
    
    def save_health_report(self, report: HealthReport, output_file: Path):
        """Save health report to file"""
        report_data = {
            'timestamp': report.timestamp.isoformat(),
            'overall_status': report.overall_status.value,
            'summary': report.summary,
            'checks': [
                {
                    'name': check.name,
                    'category': check.category.value,
                    'status': check.status.value,
                    'value': check.value,
                    'threshold': check.threshold,
                    'message': check.message,
                    'timestamp': check.timestamp.isoformat(),
                    'duration': check.duration
                }
                for check in report.checks
            ],
            'recommendations': report.recommendations,
            'alerts': report.alerts
        }
        
        with open(output_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"📄 Health report saved to {output_file}")


def main():
    """CLI interface for health monitor"""
    parser = argparse.ArgumentParser(
        description="Claude Code Framework Health Monitor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python health_monitor.py                           # Full health check
  python health_monitor.py --category framework      # Check specific category
  python health_monitor.py --detailed                # Detailed output
  python health_monitor.py --report health.json     # Save report to file
        """
    )
    
    parser.add_argument('--project-root', help="Project root directory (default: current)")
    parser.add_argument('--category', choices=[c.value for c in MonitoringCategory],
                       action='append', help="Check specific categories only")
    parser.add_argument('--detailed', action='store_true', help="Show detailed results")
    parser.add_argument('--report', help="Save report to JSON file")
    parser.add_argument('--watch', type=int, metavar='SECONDS', 
                       help="Continuous monitoring with interval")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    try:
        monitor = FrameworkHealthMonitor(
            project_root=Path(args.project_root) if args.project_root else None
        )
        
        # Convert category arguments
        categories = None
        if args.category:
            categories = [MonitoringCategory(cat) for cat in args.category]
        
        if args.watch:
            # Continuous monitoring mode
            print(f"🔄 Starting continuous health monitoring (interval: {args.watch}s)")
            print("Press Ctrl+C to stop")
            
            try:
                while True:
                    report = monitor.run_health_check(categories)
                    monitor.print_health_report(report, args.detailed)
                    
                    if args.report:
                        # Append timestamp to filename for continuous monitoring
                        base_name = Path(args.report).stem
                        extension = Path(args.report).suffix
                        timestamp = report.timestamp.strftime('%Y%m%d_%H%M%S')
                        report_file = Path(f"{base_name}_{timestamp}{extension}")
                        monitor.save_health_report(report, report_file)
                    
                    time.sleep(args.watch)
                    
            except KeyboardInterrupt:
                print(f"\n⚠️ Monitoring stopped by user")
                return 0
        
        else:
            # Single health check
            report = monitor.run_health_check(categories)
            monitor.print_health_report(report, args.detailed)
            
            if args.report:
                monitor.save_health_report(report, Path(args.report))
            
            # Return appropriate exit code
            if report.overall_status == HealthStatus.CRITICAL:
                return 2
            elif report.overall_status == HealthStatus.WARNING:
                return 1
            else:
                return 0
        
    except KeyboardInterrupt:
        print(f"\n⚠️ Health check cancelled by user")
        return 1
    except Exception as e:
        logging.error(f"Health check failed: {e}")
        return 1


if __name__ == "__main__":
    exit(main())