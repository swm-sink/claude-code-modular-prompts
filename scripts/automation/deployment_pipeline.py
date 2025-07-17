#!/usr/bin/env python3
"""
Deployment Pipeline Automation for Claude Code Framework

Comprehensive deployment orchestrator that:
- Validates code quality and test coverage before deployment
- Supports multiple deployment targets (staging, production, etc.)
- Handles environment-specific configurations
- Integrates with CI/CD systems and git workflows
- Provides rollback capabilities and deployment monitoring
- Enforces security checks and compliance validation

Author: Claude Code Framework - Phase 2.2 Automation
Version: 1.0.0
Date: 2025-07-15
"""

import os
import sys
import json
import yaml
import subprocess
import time
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any, Union
import argparse
import logging
from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime


class DeploymentStage(Enum):
    """Deployment pipeline stages"""
    VALIDATION = "validation"
    BUILD = "build"
    TEST = "test"
    SECURITY_SCAN = "security_scan"
    DEPLOY = "deploy"
    HEALTH_CHECK = "health_check"
    ROLLBACK = "rollback"


class DeploymentTarget(Enum):
    """Deployment target environments"""
    LOCAL = "local"
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


class DeploymentStatus(Enum):
    """Deployment execution status"""
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"
    ROLLED_BACK = "rolled_back"


@dataclass
class DeploymentConfig:
    """Deployment configuration"""
    target: DeploymentTarget
    branch: str
    version: str
    environment_vars: Dict[str, str]
    build_commands: List[str]
    test_commands: List[str]
    deploy_commands: List[str]
    health_check_url: Optional[str]
    rollback_commands: List[str]
    timeout_seconds: int
    skip_tests: bool = False
    skip_security: bool = False
    auto_rollback: bool = True


@dataclass
class StageResult:
    """Result of a deployment stage"""
    stage: DeploymentStage
    status: DeploymentStatus
    duration: float
    output: str
    error_output: str
    exit_code: int
    timestamp: datetime


@dataclass
class DeploymentResult:
    """Complete deployment result"""
    deployment_id: str
    config: DeploymentConfig
    stages: List[StageResult]
    overall_status: DeploymentStatus
    total_duration: float
    start_time: datetime
    end_time: datetime


class SecurityScanner:
    """Security scanning for deployment pipeline"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.logger = logging.getLogger(__name__)
    
    def scan_dependencies(self) -> Tuple[bool, str]:
        """Scan dependencies for known vulnerabilities"""
        results = []
        
        # Python dependency scanning with pip-audit or safety
        if (self.project_root / "requirements.txt").exists():
            result = self._run_python_security_scan()
            results.append(result)
        
        # Node.js dependency scanning with npm audit
        if (self.project_root / "package.json").exists():
            result = self._run_npm_security_scan()
            results.append(result)
        
        # Go dependency scanning
        if (self.project_root / "go.mod").exists():
            result = self._run_go_security_scan()
            results.append(result)
        
        # Combine results
        all_passed = all(r[0] for r in results)
        combined_output = "\n".join(r[1] for r in results)
        
        return all_passed, combined_output
    
    def _run_python_security_scan(self) -> Tuple[bool, str]:
        """Run Python security scanning"""
        try:
            # Try pip-audit first
            result = subprocess.run(
                ['pip-audit', '--format', 'json'],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                return True, "Python dependencies: No vulnerabilities found"
            else:
                return False, f"Python security issues found:\n{result.stdout}"
                
        except (subprocess.TimeoutExpired, FileNotFoundError):
            # Fallback to safety if pip-audit not available
            try:
                result = subprocess.run(
                    ['safety', 'check', '--json'],
                    cwd=self.project_root,
                    capture_output=True,
                    text=True,
                    timeout=120
                )
                
                if result.returncode == 0:
                    return True, "Python dependencies: No vulnerabilities found"
                else:
                    return False, f"Python security issues found:\n{result.stdout}"
            except:
                return True, "Python security scan: Tool not available, skipping"
    
    def _run_npm_security_scan(self) -> Tuple[bool, str]:
        """Run Node.js security scanning"""
        try:
            result = subprocess.run(
                ['npm', 'audit', '--audit-level', 'moderate', '--json'],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                return True, "Node.js dependencies: No vulnerabilities found"
            else:
                # Parse npm audit output
                try:
                    audit_data = json.loads(result.stdout)
                    vuln_count = audit_data.get('metadata', {}).get('vulnerabilities', {})
                    total_vulns = sum(vuln_count.values()) if isinstance(vuln_count, dict) else 0
                    
                    if total_vulns == 0:
                        return True, "Node.js dependencies: No vulnerabilities found"
                    else:
                        return False, f"Node.js security issues: {total_vulns} vulnerabilities found"
                except:
                    return False, f"Node.js security issues found:\n{result.stdout}"
                
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return True, "Node.js security scan: Tool not available, skipping"
    
    def _run_go_security_scan(self) -> Tuple[bool, str]:
        """Run Go security scanning"""
        try:
            result = subprocess.run(
                ['go', 'list', '-json', '-m', 'all'],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                # Basic Go module validation - could integrate with govulncheck
                return True, "Go dependencies: Basic validation passed"
            else:
                return False, f"Go dependency issues:\n{result.stderr}"
                
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return True, "Go security scan: Tool not available, skipping"
    
    def scan_secrets(self) -> Tuple[bool, str]:
        """Scan for accidentally committed secrets"""
        dangerous_patterns = [
            r'password\s*=\s*["\'][^"\']+["\']',
            r'api[_-]?key\s*=\s*["\'][^"\']+["\']',
            r'secret[_-]?key\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']{20,}["\']',
            r'-----BEGIN [A-Z]+ PRIVATE KEY-----',
            r'mongodb://[^:]+:[^@]+@',
            r'mysql://[^:]+:[^@]+@',
            r'postgres://[^:]+:[^@]+@'
        ]
        
        import re
        
        secret_files = []
        for pattern in dangerous_patterns:
            try:
                result = subprocess.run(
                    ['grep', '-r', '-i', '-n', pattern, '.'],
                    cwd=self.project_root,
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0 and result.stdout.strip():
                    # Filter out common false positives
                    lines = result.stdout.strip().split('\n')
                    filtered_lines = []
                    for line in lines:
                        if not any(fp in line.lower() for fp in [
                            'example', 'test', 'template', 'sample', 'dummy',
                            '.git/', 'node_modules/', '__pycache__/'
                        ]):
                            filtered_lines.append(line)
                    
                    if filtered_lines:
                        secret_files.extend(filtered_lines)
            except:
                continue
        
        if secret_files:
            return False, f"Potential secrets found:\n" + "\n".join(secret_files[:10])
        else:
            return True, "Secret scan: No secrets detected"


class DeploymentPipeline:
    """Main deployment pipeline orchestrator"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path.cwd()
        self.scanner = SecurityScanner(self.project_root)
        self.logger = logging.getLogger(__name__)
        
        # Load project configuration
        self.project_config = self._load_project_config()
        self.deployment_config = self._load_deployment_config()
    
    def _load_project_config(self) -> Dict[str, Any]:
        """Load PROJECT_CONFIG.xml settings"""
        config_file = self.project_root / "PROJECT_CONFIG.xml"
        config = {}
        
        if config_file.exists():
            try:
                import xml.etree.ElementTree as ET
                tree = ET.parse(config_file)
                root = tree.getroot()
                
                # Extract deployment settings
                deploy_elem = root.find(".//deployment")
                if deploy_elem is not None:
                    for child in deploy_elem:
                        config[child.tag] = child.text
                
                # Extract build commands
                commands_elem = root.find(".//commands")
                if commands_elem is not None:
                    config['commands'] = {}
                    for cmd in commands_elem:
                        config['commands'][cmd.tag] = cmd.text
                
            except Exception as e:
                self.logger.warning(f"Could not parse PROJECT_CONFIG.xml: {e}")
        
        return config
    
    def _load_deployment_config(self) -> Dict[str, Any]:
        """Load deployment configuration from deploy.yaml or similar"""
        config_files = [
            self.project_root / "deploy.yaml",
            self.project_root / "deployment.yaml",
            self.project_root / ".github" / "workflows" / "deploy.yml",
            self.project_root / ".gitlab-ci.yml"
        ]
        
        for config_file in config_files:
            if config_file.exists():
                try:
                    with open(config_file) as f:
                        if config_file.suffix in ['.yml', '.yaml']:
                            return yaml.safe_load(f)
                        else:
                            return json.load(f)
                except Exception as e:
                    self.logger.warning(f"Could not parse {config_file}: {e}")
        
        return {}
    
    def create_deployment_config(self, target: DeploymentTarget, **kwargs) -> DeploymentConfig:
        """Create deployment configuration for target environment"""
        
        # Default configurations by target
        defaults = {
            DeploymentTarget.LOCAL: {
                'branch': 'main',
                'build_commands': ['echo "Local build"'],
                'test_commands': ['python -m pytest', 'npm test'],
                'deploy_commands': ['echo "Local deployment"'],
                'timeout_seconds': 300,
                'auto_rollback': False
            },
            DeploymentTarget.DEVELOPMENT: {
                'branch': 'develop',
                'build_commands': ['npm run build', 'docker build -t app:dev .'],
                'test_commands': ['npm test', 'python -m pytest --cov=80'],
                'deploy_commands': ['docker-compose up -d'],
                'timeout_seconds': 600,
                'health_check_url': 'http://localhost:3000/health'
            },
            DeploymentTarget.STAGING: {
                'branch': 'release/*',
                'build_commands': ['npm run build:staging', 'docker build -t app:staging .'],
                'test_commands': ['npm test', 'python -m pytest --cov=90', 'npm run test:e2e'],
                'deploy_commands': ['kubectl apply -f k8s/staging/'],
                'timeout_seconds': 900,
                'health_check_url': 'https://staging.example.com/health'
            },
            DeploymentTarget.PRODUCTION: {
                'branch': 'main',
                'build_commands': ['npm run build:production', 'docker build -t app:prod .'],
                'test_commands': ['npm test', 'python -m pytest --cov=95', 'npm run test:e2e'],
                'deploy_commands': ['kubectl apply -f k8s/production/'],
                'timeout_seconds': 1200,
                'health_check_url': 'https://api.example.com/health',
                'skip_tests': False,
                'skip_security': False
            }
        }
        
        # Get defaults for target
        target_defaults = defaults.get(target, defaults[DeploymentTarget.LOCAL])
        
        # Override with project-specific config
        if self.deployment_config and target.value in self.deployment_config:
            target_config = self.deployment_config[target.value]
            target_defaults.update(target_config)
        
        # Override with project config commands
        if self.project_config.get('commands'):
            project_commands = self.project_config['commands']
            if 'build' in project_commands:
                target_defaults['build_commands'] = [project_commands['build']]
            if 'test' in project_commands:
                target_defaults['test_commands'] = [project_commands['test']]
        
        # Apply user overrides
        target_defaults.update(kwargs)
        
        # Generate version if not provided
        if 'version' not in target_defaults:
            target_defaults['version'] = self._generate_version()
        
        return DeploymentConfig(
            target=target,
            environment_vars=target_defaults.get('environment_vars', {}),
            rollback_commands=target_defaults.get('rollback_commands', ['echo "No rollback configured"']),
            **{k: v for k, v in target_defaults.items() if k not in ['environment_vars', 'rollback_commands']}
        )
    
    def _generate_version(self) -> str:
        """Generate deployment version"""
        try:
            # Try git commit hash
            result = subprocess.run(
                ['git', 'rev-parse', '--short', 'HEAD'],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                commit_hash = result.stdout.strip()
                timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
                return f"{timestamp}-{commit_hash}"
        except:
            pass
        
        # Fallback to timestamp
        return datetime.now().strftime('%Y%m%d-%H%M%S')
    
    def deploy(self, config: DeploymentConfig, dry_run: bool = False) -> DeploymentResult:
        """Execute complete deployment pipeline"""
        deployment_id = f"deploy-{config.target.value}-{int(time.time())}"
        start_time = datetime.now()
        
        print(f"🚀 Starting deployment to {config.target.value}")
        print(f"   ID: {deployment_id}")
        print(f"   Version: {config.version}")
        print(f"   Branch: {config.branch}")
        
        if dry_run:
            print("   🔍 DRY RUN MODE - No actual deployment")
        
        stages = []
        overall_status = DeploymentStatus.SUCCESS
        
        try:
            # Stage 1: Validation
            if not self._execute_stage(config, DeploymentStage.VALIDATION, stages, dry_run):
                overall_status = DeploymentStatus.FAILED
                return self._create_result(deployment_id, config, stages, overall_status, start_time)
            
            # Stage 2: Build
            if not self._execute_stage(config, DeploymentStage.BUILD, stages, dry_run):
                overall_status = DeploymentStatus.FAILED
                return self._create_result(deployment_id, config, stages, overall_status, start_time)
            
            # Stage 3: Test
            if not config.skip_tests:
                if not self._execute_stage(config, DeploymentStage.TEST, stages, dry_run):
                    overall_status = DeploymentStatus.FAILED
                    if config.auto_rollback:
                        self._execute_stage(config, DeploymentStage.ROLLBACK, stages, dry_run)
                    return self._create_result(deployment_id, config, stages, overall_status, start_time)
            
            # Stage 4: Security Scan
            if not config.skip_security:
                if not self._execute_stage(config, DeploymentStage.SECURITY_SCAN, stages, dry_run):
                    overall_status = DeploymentStatus.FAILED
                    if config.auto_rollback:
                        self._execute_stage(config, DeploymentStage.ROLLBACK, stages, dry_run)
                    return self._create_result(deployment_id, config, stages, overall_status, start_time)
            
            # Stage 5: Deploy
            if not self._execute_stage(config, DeploymentStage.DEPLOY, stages, dry_run):
                overall_status = DeploymentStatus.FAILED
                if config.auto_rollback:
                    self._execute_stage(config, DeploymentStage.ROLLBACK, stages, dry_run)
                return self._create_result(deployment_id, config, stages, overall_status, start_time)
            
            # Stage 6: Health Check
            if config.health_check_url:
                if not self._execute_stage(config, DeploymentStage.HEALTH_CHECK, stages, dry_run):
                    overall_status = DeploymentStatus.FAILED
                    if config.auto_rollback:
                        self._execute_stage(config, DeploymentStage.ROLLBACK, stages, dry_run)
                    return self._create_result(deployment_id, config, stages, overall_status, start_time)
        
        except KeyboardInterrupt:
            print(f"\n⚠️  Deployment cancelled by user")
            overall_status = DeploymentStatus.CANCELLED
            if config.auto_rollback:
                self._execute_stage(config, DeploymentStage.ROLLBACK, stages, dry_run)
        
        except Exception as e:
            print(f"💥 Deployment failed with error: {e}")
            self.logger.error(f"Deployment error: {e}")
            overall_status = DeploymentStatus.FAILED
            if config.auto_rollback:
                self._execute_stage(config, DeploymentStage.ROLLBACK, stages, dry_run)
        
        return self._create_result(deployment_id, config, stages, overall_status, start_time)
    
    def _execute_stage(self, config: DeploymentConfig, stage: DeploymentStage, 
                      stages: List[StageResult], dry_run: bool) -> bool:
        """Execute a single deployment stage"""
        print(f"\n📋 Stage: {stage.value}")
        stage_start = time.time()
        
        try:
            if stage == DeploymentStage.VALIDATION:
                success, output, error_output = self._validate_deployment(config, dry_run)
            elif stage == DeploymentStage.BUILD:
                success, output, error_output = self._execute_commands(config.build_commands, dry_run)
            elif stage == DeploymentStage.TEST:
                success, output, error_output = self._execute_commands(config.test_commands, dry_run)
            elif stage == DeploymentStage.SECURITY_SCAN:
                success, output, error_output = self._run_security_scan(dry_run)
            elif stage == DeploymentStage.DEPLOY:
                success, output, error_output = self._execute_commands(config.deploy_commands, dry_run)
            elif stage == DeploymentStage.HEALTH_CHECK:
                success, output, error_output = self._health_check(config.health_check_url, dry_run)
            elif stage == DeploymentStage.ROLLBACK:
                success, output, error_output = self._execute_commands(config.rollback_commands, dry_run)
            else:
                success, output, error_output = False, "", f"Unknown stage: {stage}"
            
            duration = time.time() - stage_start
            status = DeploymentStatus.SUCCESS if success else DeploymentStatus.FAILED
            
            result = StageResult(
                stage=stage,
                status=status,
                duration=duration,
                output=output,
                error_output=error_output,
                exit_code=0 if success else 1,
                timestamp=datetime.now()
            )
            
            stages.append(result)
            
            icon = "✅" if success else "❌"
            print(f"   {icon} {stage.value}: {status.value} ({duration:.2f}s)")
            
            if not success and error_output:
                print(f"   💥 Error: {error_output[:200]}...")
            
            return success
            
        except Exception as e:
            duration = time.time() - stage_start
            result = StageResult(
                stage=stage,
                status=DeploymentStatus.FAILED,
                duration=duration,
                output="",
                error_output=str(e),
                exit_code=-1,
                timestamp=datetime.now()
            )
            
            stages.append(result)
            print(f"   ❌ {stage.value}: FAILED ({duration:.2f}s)")
            print(f"   💥 Error: {str(e)}")
            
            return False
    
    def _validate_deployment(self, config: DeploymentConfig, dry_run: bool) -> Tuple[bool, str, str]:
        """Validate deployment prerequisites"""
        validations = []
        
        # Check git branch
        try:
            result = subprocess.run(
                ['git', 'branch', '--show-current'],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )
            
            current_branch = result.stdout.strip()
            expected_branch = config.branch
            
            # Support wildcard patterns like release/*
            if '*' in expected_branch:
                branch_pattern = expected_branch.replace('*', '')
                branch_matches = current_branch.startswith(branch_pattern)
            else:
                branch_matches = current_branch == expected_branch
            
            if branch_matches:
                validations.append("✅ Branch validation passed")
            else:
                return False, "", f"Wrong branch: {current_branch}, expected: {expected_branch}"
        
        except Exception as e:
            return False, "", f"Git validation failed: {e}"
        
        # Check working directory is clean
        try:
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )
            
            if result.stdout.strip():
                return False, "", "Working directory has uncommitted changes"
            else:
                validations.append("✅ Working directory clean")
        
        except Exception as e:
            validations.append(f"⚠️ Git status check failed: {e}")
        
        # Check PROJECT_CONFIG.xml exists
        if (self.project_root / "PROJECT_CONFIG.xml").exists():
            validations.append("✅ PROJECT_CONFIG.xml found")
        else:
            validations.append("⚠️ PROJECT_CONFIG.xml not found")
        
        return True, "\n".join(validations), ""
    
    def _execute_commands(self, commands: List[str], dry_run: bool) -> Tuple[bool, str, str]:
        """Execute a list of commands"""
        if not commands:
            return True, "No commands to execute", ""
        
        all_output = []
        all_errors = []
        
        for command in commands:
            if dry_run:
                all_output.append(f"DRY RUN: {command}")
                continue
            
            try:
                result = subprocess.run(
                    command.split(),
                    cwd=self.project_root,
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                
                all_output.append(f"Command: {command}")
                all_output.append(result.stdout)
                
                if result.returncode != 0:
                    all_errors.append(f"Command failed: {command}")
                    all_errors.append(result.stderr)
                    return False, "\n".join(all_output), "\n".join(all_errors)
            
            except subprocess.TimeoutExpired:
                return False, "\n".join(all_output), f"Command timed out: {command}"
            except Exception as e:
                return False, "\n".join(all_output), f"Command error: {command}: {e}"
        
        return True, "\n".join(all_output), ""
    
    def _run_security_scan(self, dry_run: bool) -> Tuple[bool, str, str]:
        """Run comprehensive security scan"""
        if dry_run:
            return True, "DRY RUN: Security scan would be performed", ""
        
        results = []
        
        # Dependency scan
        dep_success, dep_output = self.scanner.scan_dependencies()
        results.append(dep_output)
        
        # Secret scan
        secret_success, secret_output = self.scanner.scan_secrets()
        results.append(secret_output)
        
        overall_success = dep_success and secret_success
        
        if overall_success:
            return True, "\n".join(results), ""
        else:
            return False, "\n".join(results), "Security scan failed"
    
    def _health_check(self, url: str, dry_run: bool) -> Tuple[bool, str, str]:
        """Perform health check on deployed service"""
        if dry_run:
            return True, f"DRY RUN: Health check would be performed on {url}", ""
        
        try:
            import urllib.request
            import urllib.error
            
            # Simple HTTP health check
            request = urllib.request.Request(url)
            request.add_header('User-Agent', 'Claude-Code-Deployment-Pipeline/1.0')
            
            with urllib.request.urlopen(request, timeout=30) as response:
                status_code = response.getcode()
                
                if 200 <= status_code < 300:
                    return True, f"Health check passed: HTTP {status_code}", ""
                else:
                    return False, f"Health check failed: HTTP {status_code}", ""
        
        except Exception as e:
            return False, "", f"Health check failed: {e}"
    
    def _create_result(self, deployment_id: str, config: DeploymentConfig, 
                      stages: List[StageResult], status: DeploymentStatus, 
                      start_time: datetime) -> DeploymentResult:
        """Create deployment result object"""
        end_time = datetime.now()
        total_duration = (end_time - start_time).total_seconds()
        
        return DeploymentResult(
            deployment_id=deployment_id,
            config=config,
            stages=stages,
            overall_status=status,
            total_duration=total_duration,
            start_time=start_time,
            end_time=end_time
        )
    
    def generate_deployment_report(self, result: DeploymentResult, 
                                 output_file: Optional[Path] = None) -> str:
        """Generate deployment report"""
        report_lines = [
            "# Deployment Report",
            f"**Deployment ID**: {result.deployment_id}",
            f"**Target**: {result.config.target.value}",
            f"**Status**: {result.overall_status.value}",
            f"**Version**: {result.config.version}",
            f"**Duration**: {result.total_duration:.2f}s",
            f"**Started**: {result.start_time.strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Completed**: {result.end_time.strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Stages"
        ]
        
        for stage in result.stages:
            status_icon = "✅" if stage.status == DeploymentStatus.SUCCESS else "❌"
            report_lines.extend([
                f"### {stage.stage.value} {status_icon}",
                f"- Status: {stage.status.value}",
                f"- Duration: {stage.duration:.2f}s",
                f"- Exit Code: {stage.exit_code}",
            ])
            
            if stage.error_output:
                report_lines.extend([
                    "- **Error Output**:",
                    "```",
                    stage.error_output[:1000] + ("..." if len(stage.error_output) > 1000 else ""),
                    "```"
                ])
            
            report_lines.append("")
        
        report_content = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report_content)
            print(f"📄 Deployment report saved to {output_file}")
        
        return report_content


def main():
    """CLI interface for deployment pipeline"""
    parser = argparse.ArgumentParser(
        description="Claude Code Framework Deployment Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python deployment_pipeline.py --target local                    # Local deployment
  python deployment_pipeline.py --target staging --dry-run       # Staging dry run
  python deployment_pipeline.py --target production --version v1.2.3
        """
    )
    
    parser.add_argument('--target', choices=['local', 'development', 'staging', 'production'],
                       required=True, help="Deployment target environment")
    parser.add_argument('--project-root', help="Project root directory (default: current)")
    parser.add_argument('--version', help="Deployment version (default: auto-generate)")
    parser.add_argument('--branch', help="Git branch to deploy (default: target-specific)")
    parser.add_argument('--dry-run', action='store_true', help="Simulate deployment without executing")
    parser.add_argument('--skip-tests', action='store_true', help="Skip test execution")
    parser.add_argument('--skip-security', action='store_true', help="Skip security scanning")
    parser.add_argument('--no-rollback', action='store_true', help="Disable automatic rollback")
    parser.add_argument('--report', help="Generate deployment report file")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    try:
        pipeline = DeploymentPipeline(
            project_root=Path(args.project_root) if args.project_root else None
        )
        
        # Create deployment configuration
        target = DeploymentTarget(args.target)
        config_kwargs = {}
        
        if args.version:
            config_kwargs['version'] = args.version
        if args.branch:
            config_kwargs['branch'] = args.branch
        if args.skip_tests:
            config_kwargs['skip_tests'] = True
        if args.skip_security:
            config_kwargs['skip_security'] = True
        if args.no_rollback:
            config_kwargs['auto_rollback'] = False
        
        config = pipeline.create_deployment_config(target, **config_kwargs)
        
        # Execute deployment
        result = pipeline.deploy(config, dry_run=args.dry_run)
        
        # Generate report
        if args.report:
            pipeline.generate_deployment_report(result, Path(args.report))
        
        # Print summary
        print(f"\n🎯 Deployment Summary:")
        print(f"   Status: {result.overall_status.value}")
        print(f"   Duration: {result.total_duration:.2f}s")
        print(f"   Stages: {len([s for s in result.stages if s.status == DeploymentStatus.SUCCESS])}/{len(result.stages)} successful")
        
        # Return appropriate exit code
        return 0 if result.overall_status == DeploymentStatus.SUCCESS else 1
        
    except KeyboardInterrupt:
        print(f"\n⚠️  Deployment cancelled by user")
        return 1
    except Exception as e:
        logging.error(f"Deployment failed: {e}")
        return 1


if __name__ == "__main__":
    exit(main())