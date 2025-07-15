#!/usr/bin/env python3
"""
Comprehensive Testing Automation for Claude Code Framework

Intelligent test runner that:
- Auto-detects testing frameworks and configuration
- Runs appropriate test suites with coverage
- Enforces quality gates and TDD compliance
- Provides detailed reporting and failure analysis
- Integrates with CI/CD pipelines
- Supports multiple languages and frameworks

Author: Claude Code Framework - Phase 2.2 Automation
Version: 1.0.0
Date: 2025-07-15
"""

import os
import sys
import json
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import argparse
import logging
from dataclasses import dataclass, asdict
from enum import Enum


class TestFramework(Enum):
    """Supported testing frameworks"""
    PYTEST = "pytest"
    UNITTEST = "unittest"
    JEST = "jest"
    MOCHA = "mocha"
    JUNIT = "junit"
    GO_TEST = "go test"
    CARGO_TEST = "cargo test"
    RSPEC = "rspec"
    PHPUNIT = "phpunit"
    UNKNOWN = "unknown"


class TestResult(Enum):
    """Test execution results"""
    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"
    SKIP = "skip"


@dataclass
class TestSuiteResult:
    """Results from a test suite execution"""
    framework: TestFramework
    command: str
    exit_code: int
    duration: float
    tests_total: int
    tests_passed: int
    tests_failed: int
    tests_skipped: int
    coverage_percentage: Optional[float]
    output: str
    error_output: str
    result: TestResult


@dataclass
class QualityGateResult:
    """Quality gate validation results"""
    gate_name: str
    required_threshold: float
    actual_value: float
    passed: bool
    message: str


class TestFrameworkDetector:
    """Detects and configures testing frameworks"""
    
    FRAMEWORK_PATTERNS = {
        TestFramework.PYTEST: {
            'files': ['pytest.ini', 'pyproject.toml', 'setup.cfg'],
            'commands': ['pytest'],
            'extensions': ['.py'],
            'dependencies': ['pytest']
        },
        TestFramework.UNITTEST: {
            'files': [],
            'commands': ['python -m unittest'],
            'extensions': ['.py'],
            'dependencies': []
        },
        TestFramework.JEST: {
            'files': ['jest.config.js', 'jest.config.json'],
            'commands': ['jest', 'npm test'],
            'extensions': ['.js', '.ts'],
            'dependencies': ['jest']
        },
        TestFramework.MOCHA: {
            'files': ['mocha.opts', '.mocharc.json'],
            'commands': ['mocha'],
            'extensions': ['.js', '.ts'],
            'dependencies': ['mocha']
        },
        TestFramework.GO_TEST: {
            'files': ['go.mod'],
            'commands': ['go test'],
            'extensions': ['.go'],
            'dependencies': []
        },
        TestFramework.CARGO_TEST: {
            'files': ['Cargo.toml'],
            'commands': ['cargo test'],
            'extensions': ['.rs'],
            'dependencies': []
        }
    }
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.logger = logging.getLogger(__name__)
    
    def detect_frameworks(self) -> List[TestFramework]:
        """Detect all available testing frameworks"""
        detected = []
        
        for framework, patterns in self.FRAMEWORK_PATTERNS.items():
            if self._check_framework(framework, patterns):
                detected.append(framework)
        
        # Default fallback based on language
        if not detected:
            detected = self._detect_by_language()
        
        return detected
    
    def _check_framework(self, framework: TestFramework, patterns: Dict) -> bool:
        """Check if a specific framework is available"""
        # Check for configuration files
        for file_pattern in patterns['files']:
            if (self.project_root / file_pattern).exists():
                return True
        
        # Check for dependencies
        if self._check_dependencies(patterns['dependencies']):
            return True
        
        # Check for test files with appropriate extensions
        test_dirs = ['tests', 'test', 'spec', '__tests__']
        for test_dir in test_dirs:
            test_path = self.project_root / test_dir
            if test_path.exists():
                for ext in patterns['extensions']:
                    if list(test_path.glob(f"**/*{ext}")):
                        return True
        
        return False
    
    def _check_dependencies(self, dependencies: List[str]) -> bool:
        """Check if dependencies are installed"""
        if not dependencies:
            return False
        
        # Check package.json
        package_json = self.project_root / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    data = json.load(f)
                    all_deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
                    return any(dep in all_deps for dep in dependencies)
            except:
                pass
        
        # Check requirements.txt
        requirements = self.project_root / "requirements.txt"
        if requirements.exists():
            try:
                with open(requirements) as f:
                    content = f.read()
                    return any(dep in content for dep in dependencies)
            except:
                pass
        
        return False
    
    def _detect_by_language(self) -> List[TestFramework]:
        """Fallback detection based on primary language"""
        if (self.project_root / "go.mod").exists():
            return [TestFramework.GO_TEST]
        elif (self.project_root / "Cargo.toml").exists():
            return [TestFramework.CARGO_TEST]
        elif (self.project_root / "package.json").exists():
            return [TestFramework.JEST]
        elif list(self.project_root.glob("**/*.py")):
            return [TestFramework.PYTEST]
        else:
            return [TestFramework.UNKNOWN]
    
    def get_test_command(self, framework: TestFramework, coverage: bool = True) -> List[str]:
        """Get the appropriate test command for a framework"""
        commands = {
            TestFramework.PYTEST: [
                'pytest', '--verbose', '--tb=short',
                '--cov=src' if coverage else '',
                '--cov-report=term-missing' if coverage else '',
                '--cov-report=xml' if coverage else '',
                '--cov-fail-under=90' if coverage else ''
            ],
            TestFramework.UNITTEST: [
                'python', '-m', 'unittest', 'discover', '-v'
            ],
            TestFramework.JEST: [
                'jest', '--verbose', '--passWithNoTests',
                '--coverage' if coverage else '',
                '--coverageThreshold={"global":{"lines":90}}' if coverage else ''
            ],
            TestFramework.MOCHA: [
                'mocha', '--recursive', 'tests/'
            ],
            TestFramework.GO_TEST: [
                'go', 'test', '-v', './...',
                '-cover' if coverage else ''
            ],
            TestFramework.CARGO_TEST: [
                'cargo', 'test', '--verbose'
            ]
        }
        
        command = commands.get(framework, ['echo', 'No test command configured'])
        return [cmd for cmd in command if cmd]  # Remove empty strings


class TestRunner:
    """Main test execution orchestrator"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path.cwd()
        self.detector = TestFrameworkDetector(self.project_root)
        self.logger = logging.getLogger(__name__)
        
        # Load project configuration
        self.config = self._load_project_config()
        
        # Quality gate thresholds
        self.quality_gates = {
            'test_coverage': self.config.get('test_coverage_threshold', 90),
            'test_pass_rate': 100,  # All tests must pass
            'performance_threshold': self.config.get('performance_threshold_ms', 5000)
        }
    
    def _load_project_config(self) -> Dict[str, Any]:
        """Load PROJECT_CONFIG.xml settings"""
        config_file = self.project_root / "PROJECT_CONFIG.xml"
        config = {}
        
        if config_file.exists():
            try:
                import xml.etree.ElementTree as ET
                tree = ET.parse(config_file)
                root = tree.getroot()
                
                # Extract test coverage threshold
                coverage_elem = root.find(".//test_coverage/threshold")
                if coverage_elem is not None:
                    config['test_coverage_threshold'] = int(coverage_elem.text)
                
                # Extract performance threshold
                perf_elem = root.find(".//performance/response_time_p95")
                if perf_elem is not None:
                    perf_text = perf_elem.text.replace('ms', '')
                    config['performance_threshold_ms'] = int(perf_text)
                
            except Exception as e:
                self.logger.warning(f"Could not parse PROJECT_CONFIG.xml: {e}")
        
        return config
    
    def run_all_tests(self, coverage: bool = True, fail_fast: bool = False) -> List[TestSuiteResult]:
        """Run all detected test frameworks"""
        frameworks = self.detector.detect_frameworks()
        
        if not frameworks or frameworks == [TestFramework.UNKNOWN]:
            print("⚠️  No testing frameworks detected")
            return []
        
        print(f"🧪 Running tests with frameworks: {[f.value for f in frameworks]}")
        
        results = []
        for framework in frameworks:
            result = self.run_framework_tests(framework, coverage)
            results.append(result)
            
            if fail_fast and result.result == TestResult.FAIL:
                print(f"💥 Fast failure: {framework.value} tests failed")
                break
        
        return results
    
    def run_framework_tests(self, framework: TestFramework, coverage: bool = True) -> TestSuiteResult:
        """Run tests for a specific framework"""
        print(f"\n📋 Running {framework.value} tests...")
        
        command = self.detector.get_test_command(framework, coverage)
        start_time = time.time()
        
        try:
            # Execute test command
            result = subprocess.run(
                command,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=600  # 10 minute timeout
            )
            
            duration = time.time() - start_time
            
            # Parse test results
            test_stats = self._parse_test_output(framework, result.stdout, result.stderr)
            coverage_pct = self._extract_coverage(framework, result.stdout)
            
            # Determine overall result
            overall_result = TestResult.PASS if result.returncode == 0 else TestResult.FAIL
            
            suite_result = TestSuiteResult(
                framework=framework,
                command=' '.join(command),
                exit_code=result.returncode,
                duration=duration,
                tests_total=test_stats['total'],
                tests_passed=test_stats['passed'],
                tests_failed=test_stats['failed'],
                tests_skipped=test_stats['skipped'],
                coverage_percentage=coverage_pct,
                output=result.stdout,
                error_output=result.stderr,
                result=overall_result
            )
            
            self._print_test_summary(suite_result)
            return suite_result
            
        except subprocess.TimeoutExpired:
            return TestSuiteResult(
                framework=framework,
                command=' '.join(command),
                exit_code=-1,
                duration=600,
                tests_total=0,
                tests_passed=0,
                tests_failed=0,
                tests_skipped=0,
                coverage_percentage=None,
                output="",
                error_output="Test execution timed out",
                result=TestResult.ERROR
            )
        except Exception as e:
            return TestSuiteResult(
                framework=framework,
                command=' '.join(command),
                exit_code=-1,
                duration=time.time() - start_time,
                tests_total=0,
                tests_passed=0,
                tests_failed=0,
                tests_skipped=0,
                coverage_percentage=None,
                output="",
                error_output=str(e),
                result=TestResult.ERROR
            )
    
    def _parse_test_output(self, framework: TestFramework, stdout: str, stderr: str) -> Dict[str, int]:
        """Parse test execution output to extract statistics"""
        stats = {'total': 0, 'passed': 0, 'failed': 0, 'skipped': 0}
        
        try:
            if framework == TestFramework.PYTEST:
                # Parse pytest output
                for line in stdout.split('\n'):
                    if 'passed' in line and 'failed' in line:
                        # Format: "=== 5 failed, 10 passed in 2.34s ==="
                        parts = line.split()
                        for i, part in enumerate(parts):
                            if part == 'passed' and i > 0:
                                stats['passed'] = int(parts[i-1])
                            elif part == 'failed' and i > 0:
                                stats['failed'] = int(parts[i-1])
                            elif part == 'skipped' and i > 0:
                                stats['skipped'] = int(parts[i-1])
                
                stats['total'] = stats['passed'] + stats['failed'] + stats['skipped']
            
            elif framework == TestFramework.JEST:
                # Parse Jest output
                for line in stdout.split('\n'):
                    if 'Tests:' in line:
                        # Format: "Tests: 2 failed, 3 passed, 5 total"
                        parts = line.split()
                        for i, part in enumerate(parts):
                            if part == 'passed,' and i > 0:
                                stats['passed'] = int(parts[i-1])
                            elif part == 'failed,' and i > 0:
                                stats['failed'] = int(parts[i-1])
                            elif part == 'total' and i > 0:
                                stats['total'] = int(parts[i-1])
            
            elif framework == TestFramework.GO_TEST:
                # Parse Go test output
                if 'PASS' in stdout:
                    lines = stdout.split('\n')
                    passed_count = len([l for l in lines if 'PASS:' in l])
                    failed_count = len([l for l in lines if 'FAIL:' in l])
                    stats.update({'passed': passed_count, 'failed': failed_count, 'total': passed_count + failed_count})
            
            # If we couldn't parse, make reasonable assumptions
            if stats['total'] == 0:
                if 'error' in stderr.lower() or 'failed' in stderr.lower():
                    stats = {'total': 1, 'passed': 0, 'failed': 1, 'skipped': 0}
                else:
                    stats = {'total': 1, 'passed': 1, 'failed': 0, 'skipped': 0}
                
        except Exception as e:
            self.logger.warning(f"Could not parse test output: {e}")
        
        return stats
    
    def _extract_coverage(self, framework: TestFramework, output: str) -> Optional[float]:
        """Extract coverage percentage from test output"""
        try:
            if framework == TestFramework.PYTEST:
                # Look for "TOTAL    xxx    yyy    ZZ%"
                for line in output.split('\n'):
                    if 'TOTAL' in line and '%' in line:
                        parts = line.split()
                        for part in parts:
                            if part.endswith('%'):
                                return float(part.rstrip('%'))
            
            elif framework == TestFramework.JEST:
                # Look for "All files   |   XX.XX"
                for line in output.split('\n'):
                    if 'All files' in line and '|' in line:
                        parts = line.split('|')
                        if len(parts) > 1:
                            coverage_part = parts[1].strip().split()[0]
                            return float(coverage_part)
            
            elif framework == TestFramework.GO_TEST:
                # Look for "coverage: XX.X% of statements"
                for line in output.split('\n'):
                    if 'coverage:' in line and '%' in line:
                        parts = line.split()
                        for part in parts:
                            if part.endswith('%'):
                                return float(part.rstrip('%'))
        
        except Exception as e:
            self.logger.warning(f"Could not extract coverage: {e}")
        
        return None
    
    def _print_test_summary(self, result: TestSuiteResult):
        """Print formatted test results"""
        icon = "✅" if result.result == TestResult.PASS else "❌"
        print(f"{icon} {result.framework.value}: {result.tests_passed}/{result.tests_total} passed")
        
        if result.coverage_percentage is not None:
            cov_icon = "✅" if result.coverage_percentage >= self.quality_gates['test_coverage'] else "⚠️"
            print(f"   {cov_icon} Coverage: {result.coverage_percentage:.1f}%")
        
        print(f"   ⏱️ Duration: {result.duration:.2f}s")
        
        if result.tests_failed > 0:
            print(f"   💥 {result.tests_failed} test(s) failed")
        
        if result.tests_skipped > 0:
            print(f"   ⏭️ {result.tests_skipped} test(s) skipped")
    
    def validate_quality_gates(self, results: List[TestSuiteResult]) -> List[QualityGateResult]:
        """Validate all quality gates"""
        gate_results = []
        
        # Test coverage gate
        coverage_values = [r.coverage_percentage for r in results if r.coverage_percentage is not None]
        if coverage_values:
            avg_coverage = sum(coverage_values) / len(coverage_values)
            gate_results.append(QualityGateResult(
                gate_name="Test Coverage",
                required_threshold=self.quality_gates['test_coverage'],
                actual_value=avg_coverage,
                passed=avg_coverage >= self.quality_gates['test_coverage'],
                message=f"Average coverage: {avg_coverage:.1f}% (required: {self.quality_gates['test_coverage']}%)"
            ))
        
        # Test pass rate gate
        total_tests = sum(r.tests_total for r in results)
        total_passed = sum(r.tests_passed for r in results)
        pass_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
        
        gate_results.append(QualityGateResult(
            gate_name="Test Pass Rate",
            required_threshold=self.quality_gates['test_pass_rate'],
            actual_value=pass_rate,
            passed=pass_rate >= self.quality_gates['test_pass_rate'],
            message=f"Pass rate: {pass_rate:.1f}% ({total_passed}/{total_tests} tests passed)"
        ))
        
        # Performance gate
        total_duration = sum(r.duration for r in results)
        gate_results.append(QualityGateResult(
            gate_name="Performance",
            required_threshold=self.quality_gates['performance_threshold'] / 1000,  # Convert to seconds
            actual_value=total_duration,
            passed=total_duration <= (self.quality_gates['performance_threshold'] / 1000),
            message=f"Total test duration: {total_duration:.2f}s (limit: {self.quality_gates['performance_threshold']/1000:.2f}s)"
        ))
        
        return gate_results
    
    def generate_report(self, results: List[TestSuiteResult], gate_results: List[QualityGateResult], 
                       output_file: Optional[Path] = None) -> str:
        """Generate comprehensive test report"""
        report_lines = [
            "# Test Execution Report",
            f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}",
            f"Project: {self.project_root.name}",
            "",
            "## Summary",
        ]
        
        # Overall statistics
        total_tests = sum(r.tests_total for r in results)
        total_passed = sum(r.tests_passed for r in results)
        total_failed = sum(r.tests_failed for r in results)
        total_skipped = sum(r.tests_skipped for r in results)
        total_duration = sum(r.duration for r in results)
        
        report_lines.extend([
            f"- **Total Tests**: {total_tests}",
            f"- **Passed**: {total_passed}",
            f"- **Failed**: {total_failed}",
            f"- **Skipped**: {total_skipped}",
            f"- **Duration**: {total_duration:.2f}s",
            ""
        ])
        
        # Framework results
        report_lines.append("## Test Framework Results")
        for result in results:
            status = "✅ PASS" if result.result == TestResult.PASS else "❌ FAIL"
            report_lines.extend([
                f"### {result.framework.value} {status}",
                f"- Command: `{result.command}`",
                f"- Tests: {result.tests_passed}/{result.tests_total} passed",
                f"- Duration: {result.duration:.2f}s",
            ])
            
            if result.coverage_percentage is not None:
                report_lines.append(f"- Coverage: {result.coverage_percentage:.1f}%")
            
            if result.tests_failed > 0:
                report_lines.append(f"- **Failures**: {result.tests_failed}")
            
            report_lines.append("")
        
        # Quality gates
        report_lines.append("## Quality Gates")
        all_gates_passed = all(gate.passed for gate in gate_results)
        overall_status = "✅ PASSED" if all_gates_passed else "❌ FAILED"
        report_lines.append(f"**Overall Status**: {overall_status}")
        report_lines.append("")
        
        for gate in gate_results:
            status = "✅ PASS" if gate.passed else "❌ FAIL"
            report_lines.extend([
                f"### {gate.gate_name} {status}",
                f"- {gate.message}",
                ""
            ])
        
        # Failure details
        failed_results = [r for r in results if r.result == TestResult.FAIL]
        if failed_results:
            report_lines.append("## Failure Details")
            for result in failed_results:
                report_lines.extend([
                    f"### {result.framework.value} Failures",
                    "```",
                    result.error_output or result.output,
                    "```",
                    ""
                ])
        
        report_content = "\n".join(report_lines)
        
        # Save to file if requested
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report_content)
            print(f"📄 Report saved to {output_file}")
        
        return report_content
    
    def enforce_quality_gates(self, gate_results: List[QualityGateResult]) -> bool:
        """Enforce quality gates - return False if any gate fails"""
        failed_gates = [gate for gate in gate_results if not gate.passed]
        
        if failed_gates:
            print(f"\n💥 Quality Gates Failed!")
            for gate in failed_gates:
                print(f"   ❌ {gate.gate_name}: {gate.message}")
            return False
        else:
            print(f"\n✅ All Quality Gates Passed!")
            return True


def main():
    """CLI interface for test runner"""
    parser = argparse.ArgumentParser(
        description="Claude Code Framework Test Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_runner.py                           # Run all tests with coverage
  python test_runner.py --no-coverage             # Run tests without coverage
  python test_runner.py --framework pytest       # Run specific framework
  python test_runner.py --fail-fast               # Stop on first failure
  python test_runner.py --report test_report.md  # Generate report file
        """
    )
    
    parser.add_argument('--project-root', help="Project root directory (default: current)")
    parser.add_argument('--framework', choices=['pytest', 'jest', 'go', 'cargo'], 
                       help="Run specific test framework only")
    parser.add_argument('--no-coverage', action='store_true', help="Skip coverage measurement")
    parser.add_argument('--fail-fast', action='store_true', help="Stop on first test failure")
    parser.add_argument('--report', help="Generate report file (markdown)")
    parser.add_argument('--enforce-gates', action='store_true', help="Fail if quality gates not met")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    try:
        runner = TestRunner(
            project_root=Path(args.project_root) if args.project_root else None
        )
        
        print(f"🧪 Claude Code Framework Test Runner")
        print(f"📁 Project: {runner.project_root.name}")
        
        # Run tests
        if args.framework:
            framework_map = {
                'pytest': TestFramework.PYTEST,
                'jest': TestFramework.JEST,
                'go': TestFramework.GO_TEST,
                'cargo': TestFramework.CARGO_TEST
            }
            
            framework = framework_map[args.framework]
            results = [runner.run_framework_tests(framework, not args.no_coverage)]
        else:
            results = runner.run_all_tests(not args.no_coverage, args.fail_fast)
        
        if not results:
            print("❌ No tests executed")
            return 1
        
        # Validate quality gates
        gate_results = runner.validate_quality_gates(results)
        
        # Generate report
        if args.report:
            runner.generate_report(results, gate_results, Path(args.report))
        
        # Print summary
        print(f"\n📊 Test Summary:")
        total_tests = sum(r.tests_total for r in results)
        total_passed = sum(r.tests_passed for r in results)
        success_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
        
        print(f"   Tests: {total_passed}/{total_tests} passed ({success_rate:.1f}%)")
        
        coverage_values = [r.coverage_percentage for r in results if r.coverage_percentage is not None]
        if coverage_values:
            avg_coverage = sum(coverage_values) / len(coverage_values)
            print(f"   Coverage: {avg_coverage:.1f}%")
        
        # Enforce quality gates if requested
        if args.enforce_gates:
            gates_passed = runner.enforce_quality_gates(gate_results)
            if not gates_passed:
                return 1
        
        # Return appropriate exit code
        all_tests_passed = all(r.result == TestResult.PASS for r in results)
        return 0 if all_tests_passed else 1
        
    except KeyboardInterrupt:
        print(f"\n⚠️  Test execution cancelled by user")
        return 1
    except Exception as e:
        logging.error(f"Test execution failed: {e}")
        return 1


if __name__ == "__main__":
    exit(main())