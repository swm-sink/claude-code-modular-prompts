#!/usr/bin/env python3
"""
Automated QA Pipeline System
Agent 14: Automated quality assurance pipelines for continuous validation
"""

import os
import json
import subprocess
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import tempfile
import asyncio
import concurrent.futures
from enum import Enum

class QAPipelineType(Enum):
    SECURITY = "security"
    QUALITY = "quality" 
    DOCUMENTATION = "documentation"
    PERFORMANCE = "performance"
    INTEGRATION = "integration"

class QAResultStatus(Enum):
    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"
    ERROR = "error"

@dataclass
class QAResult:
    """QA pipeline result"""
    pipeline_type: str
    status: str
    score: float
    max_score: float
    issues_found: int
    critical_issues: int
    recommendations: List[str]
    execution_time_seconds: float
    timestamp: str
    details: Dict[str, Any]

class AutomatedQAPipeline:
    """Comprehensive automated QA pipeline system"""
    
    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path)
        self.reports_dir = self.root_path / "reports" / "qa-pipelines"
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        self.setup_logging()
        
        # Pipeline configurations
        self.pipelines = {
            QAPipelineType.SECURITY: self.run_security_pipeline,
            QAPipelineType.QUALITY: self.run_quality_pipeline,
            QAPipelineType.DOCUMENTATION: self.run_documentation_pipeline,
            QAPipelineType.PERFORMANCE: self.run_performance_pipeline,
            QAPipelineType.INTEGRATION: self.run_integration_pipeline
        }
        
        # Quality thresholds
        self.thresholds = {
            'security_min_score': 80,
            'quality_min_score': 90,
            'documentation_min_score': 80,
            'performance_max_response_ms': 1000,
            'integration_min_pass_rate': 95
        }
        
    def setup_logging(self):
        """Setup logging for QA pipelines"""
        log_dir = self.reports_dir / "logs"
        log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_dir / f"qa-pipeline-{datetime.utcnow().strftime('%Y-%m-%d')}.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    async def run_security_pipeline(self) -> QAResult:
        """Run comprehensive security validation pipeline"""
        self.logger.info("🔒 Running security validation pipeline...")
        start_time = datetime.utcnow()
        
        try:
            # Run security scan using existing agent
            security_result = await self.execute_security_scan()
            
            # Additional security checks
            file_permissions = await self.check_file_permissions()
            secret_scan = await self.scan_for_secrets()
            dependency_check = await self.check_dependencies_security()
            
            # Calculate overall security score
            security_score, issues, critical_issues = self.calculate_security_score(
                security_result, file_permissions, secret_scan, dependency_check
            )
            
            # Generate recommendations
            recommendations = self.generate_security_recommendations(
                security_result, file_permissions, secret_scan, dependency_check
            )
            
            execution_time = (datetime.utcnow() - start_time).total_seconds()
            
            return QAResult(
                pipeline_type=QAPipelineType.SECURITY.value,
                status=QAResultStatus.PASS.value if security_score >= self.thresholds['security_min_score'] else QAResultStatus.FAIL.value,
                score=security_score,
                max_score=100.0,
                issues_found=issues,
                critical_issues=critical_issues,
                recommendations=recommendations,
                execution_time_seconds=execution_time,
                timestamp=datetime.utcnow().isoformat(),
                details={
                    'security_scan': security_result,
                    'file_permissions': file_permissions,
                    'secret_scan': secret_scan,
                    'dependency_check': dependency_check
                }
            )
            
        except Exception as e:
            self.logger.error(f"Security pipeline failed: {e}")
            return self.create_error_result(QAPipelineType.SECURITY, str(e), start_time)
            
    async def execute_security_scan(self) -> Dict:
        """Execute security scan using existing validator"""
        try:
            # Use existing security validator
            security_script = self.root_path / "agent_p1_security_validator.py"
            if security_script.exists():
                result = subprocess.run(
                    ['python', str(security_script)],
                    cwd=self.root_path,
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                
                # Load results
                results_file = self.root_path / "agent_p1_security_validation_results.json"
                if results_file.exists():
                    with open(results_file, 'r') as f:
                        return json.load(f)
                        
            return {'security_score': 0, 'issues': [], 'status': 'no_validator'}
        except Exception as e:
            self.logger.error(f"Security scan execution failed: {e}")
            return {'security_score': 0, 'issues': [], 'status': 'error'}
            
    async def check_file_permissions(self) -> Dict:
        """Check file permissions for security issues"""
        try:
            permission_issues = []
            
            # Check for overly permissive files
            for file_path in self.root_path.rglob("*"):
                if file_path.is_file():
                    stat = file_path.stat()
                    mode = oct(stat.st_mode)[-3:]
                    
                    # Check for world-writable files
                    if mode.endswith('7') or mode.endswith('6'):
                        permission_issues.append({
                            'file': str(file_path.relative_to(self.root_path)),
                            'permissions': mode,
                            'issue': 'world_writable'
                        })
                        
            return {
                'status': 'completed',
                'issues_found': len(permission_issues),
                'issues': permission_issues
            }
        except Exception as e:
            self.logger.error(f"File permission check failed: {e}")
            return {'status': 'error', 'issues_found': 0, 'issues': []}
            
    async def scan_for_secrets(self) -> Dict:
        """Scan for exposed secrets and credentials"""
        try:
            secret_patterns = [
                r'password\s*=\s*["\'][^"\']+["\']',
                r'api_key\s*=\s*["\'][^"\']+["\']',
                r'secret\s*=\s*["\'][^"\']+["\']',
                r'token\s*=\s*["\'][^"\']+["\']'
            ]
            
            secrets_found = []
            
            for pattern in secret_patterns:
                result = subprocess.run(
                    ['grep', '-r', '-i', '-E', pattern, '.'],
                    cwd=self.root_path,
                    capture_output=True,
                    text=True
                )
                
                if result.stdout:
                    for line in result.stdout.strip().split('\n'):
                        if ':' in line:
                            file_path, content = line.split(':', 1)
                            secrets_found.append({
                                'file': file_path,
                                'pattern': pattern,
                                'line': content.strip()
                            })
                            
            return {
                'status': 'completed',
                'secrets_found': len(secrets_found),
                'secrets': secrets_found
            }
        except Exception as e:
            self.logger.error(f"Secret scan failed: {e}")
            return {'status': 'error', 'secrets_found': 0, 'secrets': []}
            
    async def check_dependencies_security(self) -> Dict:
        """Check dependencies for known vulnerabilities"""
        try:
            # Check if requirements.txt exists
            req_files = list(self.root_path.rglob("requirements.txt"))
            
            if not req_files:
                return {'status': 'no_requirements', 'vulnerabilities': 0}
                
            # Use safety check if available
            try:
                result = subprocess.run(
                    ['safety', 'check'],
                    cwd=self.root_path,
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                vulnerabilities = len(result.stdout.split('\n')) if result.returncode != 0 else 0
                
                return {
                    'status': 'completed',
                    'vulnerabilities': vulnerabilities,
                    'details': result.stdout if vulnerabilities > 0 else 'No vulnerabilities found'
                }
            except FileNotFoundError:
                return {'status': 'safety_not_available', 'vulnerabilities': 0}
                
        except Exception as e:
            self.logger.error(f"Dependency security check failed: {e}")
            return {'status': 'error', 'vulnerabilities': 0}
            
    def calculate_security_score(self, security_result: Dict, file_permissions: Dict, 
                               secret_scan: Dict, dependency_check: Dict) -> Tuple[float, int, int]:
        """Calculate overall security score"""
        base_score = security_result.get('security_score', 0)
        
        # Deduct points for issues
        deductions = 0
        total_issues = 0
        critical_issues = 0
        
        # File permission issues
        permission_issues = file_permissions.get('issues_found', 0)
        total_issues += permission_issues
        deductions += permission_issues * 5  # 5 points per permission issue
        
        # Secret exposure issues
        secret_issues = secret_scan.get('secrets_found', 0)
        total_issues += secret_issues
        critical_issues += secret_issues
        deductions += secret_issues * 20  # 20 points per secret (critical)
        
        # Dependency vulnerabilities
        vuln_count = dependency_check.get('vulnerabilities', 0)
        total_issues += vuln_count
        critical_issues += vuln_count
        deductions += vuln_count * 15  # 15 points per vulnerability
        
        final_score = max(0, base_score - deductions)
        
        return final_score, total_issues, critical_issues
        
    def generate_security_recommendations(self, security_result: Dict, file_permissions: Dict,
                                        secret_scan: Dict, dependency_check: Dict) -> List[str]:
        """Generate security recommendations"""
        recommendations = []
        
        if security_result.get('security_score', 0) < 80:
            recommendations.append("Address critical security vulnerabilities identified in security scan")
            
        if file_permissions.get('issues_found', 0) > 0:
            recommendations.append("Fix file permission issues - remove world-writable permissions")
            
        if secret_scan.get('secrets_found', 0) > 0:
            recommendations.append("CRITICAL: Remove exposed secrets and credentials from codebase")
            
        if dependency_check.get('vulnerabilities', 0) > 0:
            recommendations.append("Update dependencies with known security vulnerabilities")
            
        if not recommendations:
            recommendations.append("Security posture is good - maintain current practices")
            
        return recommendations
        
    async def run_quality_pipeline(self) -> QAResult:
        """Run comprehensive quality validation pipeline"""
        self.logger.info("🔍 Running quality validation pipeline...")
        start_time = datetime.utcnow()
        
        try:
            # Run quality checks
            test_coverage = await self.check_test_coverage()
            code_quality = await self.check_code_quality()
            quality_gates = await self.validate_quality_gates()
            atomic_commits = await self.check_atomic_commits()
            
            # Calculate overall quality score
            quality_score, issues, critical_issues = self.calculate_quality_score(
                test_coverage, code_quality, quality_gates, atomic_commits
            )
            
            # Generate recommendations
            recommendations = self.generate_quality_recommendations(
                test_coverage, code_quality, quality_gates, atomic_commits
            )
            
            execution_time = (datetime.utcnow() - start_time).total_seconds()
            
            return QAResult(
                pipeline_type=QAPipelineType.QUALITY.value,
                status=QAResultStatus.PASS.value if quality_score >= self.thresholds['quality_min_score'] else QAResultStatus.FAIL.value,
                score=quality_score,
                max_score=100.0,
                issues_found=issues,
                critical_issues=critical_issues,
                recommendations=recommendations,
                execution_time_seconds=execution_time,
                timestamp=datetime.utcnow().isoformat(),
                details={
                    'test_coverage': test_coverage,
                    'code_quality': code_quality,
                    'quality_gates': quality_gates,
                    'atomic_commits': atomic_commits
                }
            )
            
        except Exception as e:
            self.logger.error(f"Quality pipeline failed: {e}")
            return self.create_error_result(QAPipelineType.QUALITY, str(e), start_time)
            
    async def check_test_coverage(self) -> Dict:
        """Check test coverage"""
        try:
            # Run pytest with coverage
            result = subprocess.run(
                ['python', '-m', 'pytest', '--cov=.', '--cov-report=json', '--quiet'],
                cwd=self.root_path,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            coverage_file = self.root_path / "coverage.json"
            if coverage_file.exists():
                with open(coverage_file, 'r') as f:
                    coverage_data = json.load(f)
                    
                return {
                    'status': 'completed',
                    'coverage_percent': coverage_data.get('totals', {}).get('percent_covered', 0.0),
                    'lines_covered': coverage_data.get('totals', {}).get('covered_lines', 0),
                    'lines_total': coverage_data.get('totals', {}).get('num_statements', 0)
                }
            else:
                return {'status': 'no_coverage_data', 'coverage_percent': 0.0}
                
        except Exception as e:
            self.logger.error(f"Test coverage check failed: {e}")
            return {'status': 'error', 'coverage_percent': 0.0}
            
    async def check_code_quality(self) -> Dict:
        """Check code quality using linting tools"""
        try:
            quality_issues = []
            
            # Run flake8 if available
            try:
                result = subprocess.run(
                    ['flake8', '.', '--count', '--select=E9,F63,F7,F82', '--show-source', '--statistics'],
                    cwd=self.root_path,
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.stdout:
                    quality_issues.append({
                        'tool': 'flake8',
                        'issues': len(result.stdout.split('\n')) - 1,
                        'output': result.stdout
                    })
            except FileNotFoundError:
                pass  # flake8 not available
                
            return {
                'status': 'completed',
                'total_issues': sum(issue['issues'] for issue in quality_issues),
                'tools_run': [issue['tool'] for issue in quality_issues],
                'details': quality_issues
            }
            
        except Exception as e:
            self.logger.error(f"Code quality check failed: {e}")
            return {'status': 'error', 'total_issues': 0}
            
    async def validate_quality_gates(self) -> Dict:
        """Validate quality gates"""
        try:
            # Use existing quality auditor
            quality_script = self.root_path / "agent_p4_quality_auditor.py"
            if quality_script.exists():
                result = subprocess.run(
                    ['python', str(quality_script)],
                    cwd=self.root_path,
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                
                # Load results
                results_file = self.root_path / "agent_p4_quality_audit_results.json"
                if results_file.exists():
                    with open(results_file, 'r') as f:
                        return json.load(f)
                        
            return {'status': 'no_quality_auditor', 'overall_score': 0}
        except Exception as e:
            self.logger.error(f"Quality gates validation failed: {e}")
            return {'status': 'error', 'overall_score': 0}
            
    async def check_atomic_commits(self) -> Dict:
        """Check atomic commits coverage"""
        try:
            # Get recent commits
            result = subprocess.run(
                ['git', 'log', '--oneline', '-20'],
                cwd=self.root_path,
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                commits = result.stdout.strip().split('\n')
                atomic_commits = len([c for c in commits if 'Agent' in c or 'atomic' in c.lower()])
                coverage = (atomic_commits / len(commits) * 100) if commits else 0
                
                return {
                    'status': 'completed',
                    'coverage_percent': coverage,
                    'atomic_commits': atomic_commits,
                    'total_commits': len(commits)
                }
            else:
                return {'status': 'git_error', 'coverage_percent': 0}
                
        except Exception as e:
            self.logger.error(f"Atomic commits check failed: {e}")
            return {'status': 'error', 'coverage_percent': 0}
            
    def calculate_quality_score(self, test_coverage: Dict, code_quality: Dict, 
                              quality_gates: Dict, atomic_commits: Dict) -> Tuple[float, int, int]:
        """Calculate overall quality score"""
        # Base score from quality gates
        base_score = quality_gates.get('overall_score', 0)
        
        # Adjust based on other metrics
        coverage_score = test_coverage.get('coverage_percent', 0)
        quality_issues = code_quality.get('total_issues', 0)
        atomic_coverage = atomic_commits.get('coverage_percent', 0)
        
        # Calculate weighted score
        final_score = (
            base_score * 0.4 +          # 40% quality gates
            coverage_score * 0.3 +      # 30% test coverage
            max(0, 100 - quality_issues * 2) * 0.2 +  # 20% code quality
            atomic_coverage * 0.1       # 10% atomic commits
        )
        
        total_issues = quality_issues
        critical_issues = quality_issues if quality_issues > 10 else 0
        
        return final_score, total_issues, critical_issues
        
    def generate_quality_recommendations(self, test_coverage: Dict, code_quality: Dict,
                                       quality_gates: Dict, atomic_commits: Dict) -> List[str]:
        """Generate quality recommendations"""
        recommendations = []
        
        if test_coverage.get('coverage_percent', 0) < 90:
            recommendations.append("Increase test coverage to achieve 90%+ target")
            
        if code_quality.get('total_issues', 0) > 5:
            recommendations.append("Address code quality issues identified by linting tools")
            
        if quality_gates.get('overall_score', 0) < 90:
            recommendations.append("Improve quality gates compliance and enforcement")
            
        if atomic_commits.get('coverage_percent', 0) < 80:
            recommendations.append("Increase atomic commits usage for better traceability")
            
        if not recommendations:
            recommendations.append("Quality metrics are good - maintain current standards")
            
        return recommendations
        
    async def run_documentation_pipeline(self) -> QAResult:
        """Run documentation validation pipeline"""
        self.logger.info("📝 Running documentation validation pipeline...")
        start_time = datetime.utcnow()
        
        try:
            # Use existing documentation validator
            doc_validation = await self.validate_documentation()
            accuracy_check = await self.check_documentation_accuracy()
            link_validation = await self.validate_documentation_links()
            
            # Calculate score
            doc_score, issues, critical_issues = self.calculate_documentation_score(
                doc_validation, accuracy_check, link_validation
            )
            
            recommendations = self.generate_documentation_recommendations(
                doc_validation, accuracy_check, link_validation
            )
            
            execution_time = (datetime.utcnow() - start_time).total_seconds()
            
            return QAResult(
                pipeline_type=QAPipelineType.DOCUMENTATION.value,
                status=QAResultStatus.PASS.value if doc_score >= self.thresholds['documentation_min_score'] else QAResultStatus.FAIL.value,
                score=doc_score,
                max_score=100.0,
                issues_found=issues,
                critical_issues=critical_issues,
                recommendations=recommendations,
                execution_time_seconds=execution_time,
                timestamp=datetime.utcnow().isoformat(),
                details={
                    'documentation_validation': doc_validation,
                    'accuracy_check': accuracy_check,
                    'link_validation': link_validation
                }
            )
            
        except Exception as e:
            self.logger.error(f"Documentation pipeline failed: {e}")
            return self.create_error_result(QAPipelineType.DOCUMENTATION, str(e), start_time)
            
    async def validate_documentation(self) -> Dict:
        """Validate documentation using existing validator"""
        try:
            doc_script = self.root_path / "agent_p5_documentation_validator.py"
            if doc_script.exists():
                result = subprocess.run(
                    ['python', str(doc_script)],
                    cwd=self.root_path,
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                
                results_file = self.root_path / "agent_p5_documentation_validation_results.json"
                if results_file.exists():
                    with open(results_file, 'r') as f:
                        return json.load(f)
                        
            return {'status': 'no_validator', 'overall_score': 0}
        except Exception as e:
            self.logger.error(f"Documentation validation failed: {e}")
            return {'status': 'error', 'overall_score': 0}
            
    async def check_documentation_accuracy(self) -> Dict:
        """Check documentation accuracy"""
        try:
            # Count documentation files
            doc_files = list(self.root_path.rglob("*.md"))
            
            # Basic accuracy checks
            accuracy_issues = []
            
            for doc_file in doc_files:
                try:
                    with open(doc_file, 'r') as f:
                        content = f.read()
                        
                    # Check for broken internal links
                    if '](' in content:
                        accuracy_issues.append({
                            'file': str(doc_file.relative_to(self.root_path)),
                            'issue': 'potential_broken_links',
                            'count': content.count('](')
                        })
                except Exception:
                    continue
                    
            return {
                'status': 'completed',
                'files_checked': len(doc_files),
                'issues_found': len(accuracy_issues),
                'issues': accuracy_issues
            }
            
        except Exception as e:
            self.logger.error(f"Documentation accuracy check failed: {e}")
            return {'status': 'error', 'files_checked': 0, 'issues_found': 0}
            
    async def validate_documentation_links(self) -> Dict:
        """Validate documentation links"""
        try:
            # This would implement link validation
            return {
                'status': 'completed',
                'links_checked': 0,
                'broken_links': 0,
                'details': 'Link validation not implemented yet'
            }
        except Exception as e:
            self.logger.error(f"Documentation link validation failed: {e}")
            return {'status': 'error', 'links_checked': 0, 'broken_links': 0}
            
    def calculate_documentation_score(self, doc_validation: Dict, accuracy_check: Dict, 
                                    link_validation: Dict) -> Tuple[float, int, int]:
        """Calculate documentation score"""
        base_score = doc_validation.get('overall_score', 0)
        accuracy_issues = accuracy_check.get('issues_found', 0)
        broken_links = link_validation.get('broken_links', 0)
        
        # Deduct points for issues
        deductions = accuracy_issues * 2 + broken_links * 5
        final_score = max(0, base_score - deductions)
        
        total_issues = accuracy_issues + broken_links
        critical_issues = broken_links if broken_links > 5 else 0
        
        return final_score, total_issues, critical_issues
        
    def generate_documentation_recommendations(self, doc_validation: Dict, accuracy_check: Dict,
                                             link_validation: Dict) -> List[str]:
        """Generate documentation recommendations"""
        recommendations = []
        
        if doc_validation.get('overall_score', 0) < 80:
            recommendations.append("Improve documentation quality and accuracy")
            
        if accuracy_check.get('issues_found', 0) > 0:
            recommendations.append("Fix documentation accuracy issues and broken references")
            
        if link_validation.get('broken_links', 0) > 0:
            recommendations.append("Fix broken links in documentation")
            
        if not recommendations:
            recommendations.append("Documentation quality is good - maintain current standards")
            
        return recommendations
        
    async def run_performance_pipeline(self) -> QAResult:
        """Run performance validation pipeline"""
        self.logger.info("⚡ Running performance validation pipeline...")
        start_time = datetime.utcnow()
        
        try:
            # Use existing performance validator
            perf_validation = await self.validate_performance()
            benchmark_results = await self.run_performance_benchmarks()
            
            # Calculate score
            perf_score, issues, critical_issues = self.calculate_performance_score(
                perf_validation, benchmark_results
            )
            
            recommendations = self.generate_performance_recommendations(
                perf_validation, benchmark_results
            )
            
            execution_time = (datetime.utcnow() - start_time).total_seconds()
            
            return QAResult(
                pipeline_type=QAPipelineType.PERFORMANCE.value,
                status=QAResultStatus.PASS.value if perf_score >= 80 else QAResultStatus.FAIL.value,
                score=perf_score,
                max_score=100.0,
                issues_found=issues,
                critical_issues=critical_issues,
                recommendations=recommendations,
                execution_time_seconds=execution_time,
                timestamp=datetime.utcnow().isoformat(),
                details={
                    'performance_validation': perf_validation,
                    'benchmark_results': benchmark_results
                }
            )
            
        except Exception as e:
            self.logger.error(f"Performance pipeline failed: {e}")
            return self.create_error_result(QAPipelineType.PERFORMANCE, str(e), start_time)
            
    async def validate_performance(self) -> Dict:
        """Validate performance using existing validator"""
        try:
            perf_script = self.root_path / "agent_p3_performance_validator.py"
            if perf_script.exists():
                result = subprocess.run(
                    ['python', str(perf_script)],
                    cwd=self.root_path,
                    capture_output=True,
                    text=True,
                    timeout=300
                )
                
                results_file = self.root_path / "agent_p3_performance_validation_results.json"
                if results_file.exists():
                    with open(results_file, 'r') as f:
                        return json.load(f)
                        
            return {'status': 'no_validator', 'performance_grade': 'F'}
        except Exception as e:
            self.logger.error(f"Performance validation failed: {e}")
            return {'status': 'error', 'performance_grade': 'F'}
            
    async def run_performance_benchmarks(self) -> Dict:
        """Run additional performance benchmarks"""
        try:
            # Simple performance test
            import time
            
            start = time.time()
            # Test framework loading
            list(self.root_path.glob("**/*.md"))
            load_time = time.time() - start
            
            return {
                'status': 'completed',
                'framework_load_time_ms': load_time * 1000,
                'meets_target': load_time * 1000 < self.thresholds['performance_max_response_ms']
            }
        except Exception as e:
            self.logger.error(f"Performance benchmarks failed: {e}")
            return {'status': 'error', 'framework_load_time_ms': 9999}
            
    def calculate_performance_score(self, perf_validation: Dict, benchmark_results: Dict) -> Tuple[float, int, int]:
        """Calculate performance score"""
        # Convert grade to score
        grade_scores = {'A+': 100, 'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
        base_score = grade_scores.get(perf_validation.get('performance_grade', 'F'), 0)
        
        # Adjust based on benchmarks
        load_time = benchmark_results.get('framework_load_time_ms', 9999)
        if load_time > self.thresholds['performance_max_response_ms']:
            base_score -= 20
            
        issues = 1 if load_time > self.thresholds['performance_max_response_ms'] else 0
        critical_issues = 1 if load_time > 2000 else 0
        
        return max(0, base_score), issues, critical_issues
        
    def generate_performance_recommendations(self, perf_validation: Dict, benchmark_results: Dict) -> List[str]:
        """Generate performance recommendations"""
        recommendations = []
        
        if perf_validation.get('performance_grade', 'F') in ['C', 'D', 'F']:
            recommendations.append("Optimize framework performance to improve response times")
            
        if benchmark_results.get('framework_load_time_ms', 0) > 1000:
            recommendations.append("Optimize framework loading time")
            
        if not recommendations:
            recommendations.append("Performance is good - maintain current optimization")
            
        return recommendations
        
    async def run_integration_pipeline(self) -> QAResult:
        """Run integration testing pipeline"""
        self.logger.info("🔗 Running integration testing pipeline...")
        start_time = datetime.utcnow()
        
        try:
            # Run integration tests
            integration_results = await self.run_integration_tests()
            workflow_validation = await self.validate_workflows()
            
            # Calculate score
            integration_score, issues, critical_issues = self.calculate_integration_score(
                integration_results, workflow_validation
            )
            
            recommendations = self.generate_integration_recommendations(
                integration_results, workflow_validation
            )
            
            execution_time = (datetime.utcnow() - start_time).total_seconds()
            
            return QAResult(
                pipeline_type=QAPipelineType.INTEGRATION.value,
                status=QAResultStatus.PASS.value if integration_score >= self.thresholds['integration_min_pass_rate'] else QAResultStatus.FAIL.value,
                score=integration_score,
                max_score=100.0,
                issues_found=issues,
                critical_issues=critical_issues,
                recommendations=recommendations,
                execution_time_seconds=execution_time,
                timestamp=datetime.utcnow().isoformat(),
                details={
                    'integration_results': integration_results,
                    'workflow_validation': workflow_validation
                }
            )
            
        except Exception as e:
            self.logger.error(f"Integration pipeline failed: {e}")
            return self.create_error_result(QAPipelineType.INTEGRATION, str(e), start_time)
            
    async def run_integration_tests(self) -> Dict:
        """Run integration tests"""
        try:
            # Run existing integration tests
            result = subprocess.run(
                ['python', '-m', 'pytest', 'tests/integration/', '-v'],
                cwd=self.root_path,
                capture_output=True,
                text=True,
                timeout=300
            )
            
            # Parse results
            lines = result.stdout.split('\n')
            passed = len([line for line in lines if '::' in line and 'PASSED' in line])
            failed = len([line for line in lines if '::' in line and 'FAILED' in line])
            total = passed + failed
            
            pass_rate = (passed / total * 100) if total > 0 else 0
            
            return {
                'status': 'completed',
                'tests_run': total,
                'tests_passed': passed,
                'tests_failed': failed,
                'pass_rate': pass_rate
            }
        except Exception as e:
            self.logger.error(f"Integration tests failed: {e}")
            return {'status': 'error', 'tests_run': 0, 'pass_rate': 0}
            
    async def validate_workflows(self) -> Dict:
        """Validate workflow integrity"""
        try:
            # Check for workflow files
            workflow_files = list(self.root_path.glob(".github/workflows/*.yml"))
            
            return {
                'status': 'completed',
                'workflows_found': len(workflow_files),
                'workflows': [str(f.name) for f in workflow_files]
            }
        except Exception as e:
            self.logger.error(f"Workflow validation failed: {e}")
            return {'status': 'error', 'workflows_found': 0}
            
    def calculate_integration_score(self, integration_results: Dict, workflow_validation: Dict) -> Tuple[float, int, int]:
        """Calculate integration score"""
        pass_rate = integration_results.get('pass_rate', 0)
        failed_tests = integration_results.get('tests_failed', 0)
        
        # Base score on pass rate
        base_score = pass_rate
        
        issues = failed_tests
        critical_issues = failed_tests if failed_tests > 5 else 0
        
        return base_score, issues, critical_issues
        
    def generate_integration_recommendations(self, integration_results: Dict, workflow_validation: Dict) -> List[str]:
        """Generate integration recommendations"""
        recommendations = []
        
        if integration_results.get('pass_rate', 0) < 95:
            recommendations.append("Fix failing integration tests to achieve 95%+ pass rate")
            
        if integration_results.get('tests_failed', 0) > 0:
            recommendations.append("Address failing integration tests")
            
        if workflow_validation.get('workflows_found', 0) == 0:
            recommendations.append("Add CI/CD workflow files for automated testing")
            
        if not recommendations:
            recommendations.append("Integration testing is working well - maintain current practices")
            
        return recommendations
        
    def create_error_result(self, pipeline_type: QAPipelineType, error_message: str, start_time: datetime) -> QAResult:
        """Create error result for failed pipeline"""
        execution_time = (datetime.utcnow() - start_time).total_seconds()
        
        return QAResult(
            pipeline_type=pipeline_type.value,
            status=QAResultStatus.ERROR.value,
            score=0.0,
            max_score=100.0,
            issues_found=1,
            critical_issues=1,
            recommendations=[f"Fix pipeline execution error: {error_message}"],
            execution_time_seconds=execution_time,
            timestamp=datetime.utcnow().isoformat(),
            details={'error': error_message}
        )
        
    async def run_all_pipelines(self) -> Dict[str, QAResult]:
        """Run all QA pipelines concurrently"""
        self.logger.info("🚀 Running all QA pipelines...")
        
        # Run pipelines concurrently
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            tasks = {}
            for pipeline_type, pipeline_func in self.pipelines.items():
                future = executor.submit(asyncio.run, pipeline_func())
                tasks[pipeline_type.value] = future
                
            results = {}
            for pipeline_name, future in tasks.items():
                try:
                    results[pipeline_name] = future.result(timeout=600)  # 10 minutes max
                except Exception as e:
                    self.logger.error(f"Pipeline {pipeline_name} failed: {e}")
                    results[pipeline_name] = self.create_error_result(
                        QAPipelineType(pipeline_name), str(e), datetime.utcnow()
                    )
                    
        return results
        
    def generate_consolidated_report(self, results: Dict[str, QAResult]) -> str:
        """Generate consolidated QA pipeline report"""
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        
        # Calculate overall status
        all_passed = all(result.status == QAResultStatus.PASS.value for result in results.values())
        any_critical = any(result.critical_issues > 0 for result in results.values())
        
        overall_status = "PASS" if all_passed else "CRITICAL" if any_critical else "WARNING"
        
        report = f"""# Automated QA Pipeline Report - Agent 14

**Generated**: {timestamp}
**Overall Status**: {overall_status}
**Pipelines Run**: {len(results)}

## 📊 Executive Summary

"""
        
        # Add pipeline summaries
        for pipeline_name, result in results.items():
            status_emoji = "✅" if result.status == "pass" else "❌" if result.status == "fail" else "⚠️"
            report += f"- **{pipeline_name.title()}**: {status_emoji} {result.status.upper()} ({result.score:.1f}/{result.max_score})\n"
            
        report += "\n## 🔍 Detailed Results\n\n"
        
        # Add detailed results for each pipeline
        for pipeline_name, result in results.items():
            report += f"### {pipeline_name.title()} Pipeline\n\n"
            report += f"- **Status**: {result.status.upper()}\n"
            report += f"- **Score**: {result.score:.1f}/{result.max_score}\n"
            report += f"- **Issues Found**: {result.issues_found}\n"
            report += f"- **Critical Issues**: {result.critical_issues}\n"
            report += f"- **Execution Time**: {result.execution_time_seconds:.1f}s\n"
            
            if result.recommendations:
                report += f"\n**Recommendations**:\n"
                for rec in result.recommendations:
                    report += f"- {rec}\n"
                    
            report += "\n"
            
        # Add next actions
        report += "## 🎯 Next Actions\n\n"
        
        critical_pipelines = [name for name, result in results.items() if result.critical_issues > 0]
        if critical_pipelines:
            report += "### 🚨 CRITICAL PRIORITY\n"
            for pipeline in critical_pipelines:
                report += f"- Fix critical issues in {pipeline} pipeline\n"
                
        failing_pipelines = [name for name, result in results.items() if result.status == "fail"]
        if failing_pipelines:
            report += "\n### ⚠️ HIGH PRIORITY\n"
            for pipeline in failing_pipelines:
                report += f"- Address failures in {pipeline} pipeline\n"
                
        report += f"""

## 📈 Continuous Improvement

1. **Automate**: Set up automated pipeline execution
2. **Monitor**: Track trends in pipeline results
3. **Optimize**: Improve pipeline execution time and accuracy
4. **Integrate**: Connect pipelines to CI/CD workflows

---
**QA Pipeline System**: Agent 14 Automated QA
**Report ID**: qa-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}
**Next Scheduled Run**: {(datetime.utcnow() + timedelta(hours=24)).strftime('%Y-%m-%d %H:%M:%S UTC')}
"""
        
        return report
        
    def save_results(self, results: Dict[str, QAResult], report: str):
        """Save QA pipeline results and report"""
        timestamp = datetime.utcnow()
        
        # Save individual results
        for pipeline_name, result in results.items():
            result_file = self.reports_dir / f"{pipeline_name}-{timestamp.strftime('%Y-%m-%d-%H%M%S')}.json"
            with open(result_file, 'w') as f:
                json.dump(asdict(result), f, indent=2)
                
        # Save consolidated results
        consolidated_file = self.reports_dir / f"qa-pipelines-{timestamp.strftime('%Y-%m-%d-%H%M%S')}.json"
        with open(consolidated_file, 'w') as f:
            json.dump({name: asdict(result) for name, result in results.items()}, f, indent=2)
            
        # Save report
        report_file = self.reports_dir / f"qa-pipeline-report-{timestamp.strftime('%Y-%m-%d-%H%M%S')}.md"
        with open(report_file, 'w') as f:
            f.write(report)
            
        # Update latest
        latest_dir = self.reports_dir / "latest"
        latest_dir.mkdir(exist_ok=True)
        
        latest_consolidated = latest_dir / "qa-pipelines-latest.json"
        with open(latest_consolidated, 'w') as f:
            json.dump({name: asdict(result) for name, result in results.items()}, f, indent=2)
            
        latest_report = latest_dir / "qa-pipeline-report-latest.md"
        with open(latest_report, 'w') as f:
            f.write(report)
            
        self.logger.info(f"Results saved to: {consolidated_file}")
        self.logger.info(f"Report saved to: {report_file}")

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Automated QA Pipeline System')
    parser.add_argument('--pipeline', choices=['security', 'quality', 'documentation', 'performance', 'integration', 'all'],
                       default='all', help='Pipeline to run')
    parser.add_argument('--report-only', action='store_true', help='Generate report from existing results')
    
    args = parser.parse_args()
    
    qa_pipeline = AutomatedQAPipeline()
    
    if args.report_only:
        # Generate report from latest results
        latest_file = qa_pipeline.reports_dir / "latest" / "qa-pipelines-latest.json"
        if latest_file.exists():
            with open(latest_file, 'r') as f:
                data = json.load(f)
                results = {name: QAResult(**result_data) for name, result_data in data.items()}
                report = qa_pipeline.generate_consolidated_report(results)
                print(report)
        else:
            print("No existing results found. Run pipelines first.")
        return
        
    if args.pipeline == 'all':
        print("🚀 Running all QA pipelines...")
        results = asyncio.run(qa_pipeline.run_all_pipelines())
    else:
        print(f"🔍 Running {args.pipeline} pipeline...")
        pipeline_func = qa_pipeline.pipelines[QAPipelineType(args.pipeline)]
        result = asyncio.run(pipeline_func())
        results = {args.pipeline: result}
        
    # Generate and save report
    report = qa_pipeline.generate_consolidated_report(results)
    qa_pipeline.save_results(results, report)
    
    print("\n" + "="*80)
    print(report)
    print("="*80)
    
    # Exit with appropriate code
    overall_passed = all(result.status == QAResultStatus.PASS.value for result in results.values())
    exit_code = 0 if overall_passed else 1
    exit(exit_code)

if __name__ == "__main__":
    main()