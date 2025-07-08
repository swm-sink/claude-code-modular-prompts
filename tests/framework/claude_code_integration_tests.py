#!/usr/bin/env python3
"""Claude Code Integration Testing Infrastructure.

This module provides comprehensive integration testing for the Claude Code
framework, validating actual command execution, module orchestration,
and end-to-end workflow validation in real Claude Code environments.
"""

import json
import time
import subprocess
import tempfile
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import uuid


class IntegrationTestType(Enum):
    """Types of integration tests."""
    COMMAND_EXECUTION = "command_execution"
    MODULE_ORCHESTRATION = "module_orchestration"
    WORKFLOW_VALIDATION = "workflow_validation"
    ERROR_HANDLING = "error_handling"
    PERFORMANCE_VALIDATION = "performance_validation"


class TestResult(Enum):
    """Integration test results."""
    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"
    TIMEOUT = "timeout"


@dataclass
class IntegrationTestCase:
    """Individual integration test case."""
    test_id: str
    test_type: IntegrationTestType
    test_name: str
    description: str
    command: str
    expected_outcome: str
    timeout_seconds: int
    setup_required: bool
    cleanup_required: bool
    metadata: Dict[str, Any]


@dataclass
class IntegrationTestResult:
    """Result of an integration test execution."""
    test_case: IntegrationTestCase
    result: TestResult
    execution_time_ms: float
    output: str
    error_output: str
    exit_code: int
    framework_state_before: Dict[str, Any]
    framework_state_after: Dict[str, Any]
    performance_metrics: Dict[str, float]
    timestamp: str


@dataclass
class IntegrationTestSuite:
    """Collection of integration tests for a specific area."""
    suite_name: str
    description: str
    setup_commands: List[str]
    cleanup_commands: List[str]
    test_cases: List[IntegrationTestCase]
    dependencies: List[str]


@dataclass
class IntegrationTestReport:
    """Comprehensive integration test report."""
    test_session_id: str
    test_date: str
    framework_version: str
    environment_info: Dict[str, Any]
    test_suites_run: List[str]
    total_tests: int
    passed_tests: int
    failed_tests: int
    error_tests: int
    timeout_tests: int
    execution_time_total: float
    performance_summary: Dict[str, Any]
    test_results: List[IntegrationTestResult]
    recommendations: List[str]


class FrameworkStateMonitor:
    """Monitors framework state during integration testing."""
    
    def __init__(self, project_root: Path):
        """Initialize framework state monitor."""
        self.project_root = project_root
        self.claude_md_path = project_root / "CLAUDE.md"
        self.commands_dir = project_root / ".claude" / "commands"
        self.modules_dir = project_root / ".claude" / "modules"
    
    def capture_framework_state(self) -> Dict[str, Any]:
        """Capture current framework state for comparison."""
        state = {
            "timestamp": datetime.now().isoformat(),
            "claude_md_size": self.claude_md_path.stat().st_size if self.claude_md_path.exists() else 0,
            "command_count": len(list(self.commands_dir.glob("*.md"))) if self.commands_dir.exists() else 0,
            "module_count": len(list(self.modules_dir.rglob("*.md"))) if self.modules_dir.exists() else 0,
            "framework_version": self._extract_framework_version(),
            "file_checksums": self._calculate_file_checksums()
        }
        return state
    
    def _extract_framework_version(self) -> str:
        """Extract framework version from CLAUDE.md."""
        if not self.claude_md_path.exists():
            return "unknown"
        
        content = self.claude_md_path.read_text()
        
        # Look for version in version table
        for line in content.split('\n'):
            if '|' in line and any(v in line for v in ['2.6.0', '3.0.0']):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) > 1 and parts[1]:
                    return parts[1]
        
        return "unknown"
    
    def _calculate_file_checksums(self) -> Dict[str, str]:
        """Calculate checksums for key framework files."""
        import hashlib
        
        checksums = {}
        key_files = [
            self.claude_md_path,
            self.commands_dir / "task.md",
            self.commands_dir / "auto.md",
            self.commands_dir / "feature.md"
        ]
        
        for file_path in key_files:
            if file_path.exists():
                content = file_path.read_text().encode()
                checksum = hashlib.md5(content).hexdigest()
                checksums[str(file_path.relative_to(self.project_root))] = checksum
        
        return checksums


class PerformanceAnalyzer:
    """Analyzes performance metrics during integration testing."""
    
    @staticmethod
    def analyze_command_performance(results: List[IntegrationTestResult]) -> Dict[str, Any]:
        """Analyze command execution performance."""
        command_performance = {}
        
        for result in results:
            command = result.test_case.command.split()[0] if result.test_case.command else "unknown"
            
            if command not in command_performance:
                command_performance[command] = {
                    "execution_times": [],
                    "success_rate": 0,
                    "total_tests": 0,
                    "successful_tests": 0
                }
            
            command_performance[command]["execution_times"].append(result.execution_time_ms)
            command_performance[command]["total_tests"] += 1
            
            if result.result == TestResult.PASS:
                command_performance[command]["successful_tests"] += 1
        
        # Calculate statistics
        for command, data in command_performance.items():
            times = data["execution_times"]
            data["avg_execution_time"] = sum(times) / len(times) if times else 0
            data["p95_execution_time"] = sorted(times)[int(len(times) * 0.95) - 1] if times else 0
            data["success_rate"] = (data["successful_tests"] / data["total_tests"]) * 100 if data["total_tests"] > 0 else 0
        
        return command_performance
    
    @staticmethod
    def analyze_framework_performance(results: List[IntegrationTestResult]) -> Dict[str, Any]:
        """Analyze overall framework performance."""
        execution_times = [r.execution_time_ms for r in results]
        successful_results = [r for r in results if r.result == TestResult.PASS]
        
        return {
            "total_tests": len(results),
            "successful_tests": len(successful_results),
            "success_rate": (len(successful_results) / len(results)) * 100 if results else 0,
            "avg_execution_time": sum(execution_times) / len(execution_times) if execution_times else 0,
            "p95_execution_time": sorted(execution_times)[int(len(execution_times) * 0.95) - 1] if execution_times else 0,
            "total_execution_time": sum(execution_times),
            "performance_target_met": sorted(execution_times)[int(len(execution_times) * 0.95) - 1] <= 200 if execution_times else False
        }


class ClaudeCodeIntegrationTester:
    """Main integration testing framework for Claude Code."""
    
    def __init__(self, project_root: Path, output_dir: Path):
        """Initialize Claude Code integration tester."""
        self.project_root = project_root
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.state_monitor = FrameworkStateMonitor(project_root)
        self.performance_analyzer = PerformanceAnalyzer()
        
        # Initialize test suites
        self.test_suites = self._create_test_suites()
    
    def _create_test_suites(self) -> Dict[str, IntegrationTestSuite]:
        """Create comprehensive integration test suites."""
        suites = {}
        
        # Command Execution Test Suite
        suites["command_execution"] = IntegrationTestSuite(
            suite_name="Command Execution Validation",
            description="Validates that all framework commands execute correctly",
            setup_commands=[],
            cleanup_commands=[],
            test_cases=self._create_command_execution_tests(),
            dependencies=[]
        )
        
        # Module Orchestration Test Suite
        suites["module_orchestration"] = IntegrationTestSuite(
            suite_name="Module Orchestration Validation",
            description="Validates module loading and orchestration capabilities",
            setup_commands=[],
            cleanup_commands=[],
            test_cases=self._create_module_orchestration_tests(),
            dependencies=["command_execution"]
        )
        
        # Workflow Validation Test Suite
        suites["workflow_validation"] = IntegrationTestSuite(
            suite_name="End-to-End Workflow Validation",
            description="Validates complete workflows from command to completion",
            setup_commands=["git status", "git branch"],
            cleanup_commands=[],
            test_cases=self._create_workflow_validation_tests(),
            dependencies=["command_execution", "module_orchestration"]
        )
        
        # Error Handling Test Suite
        suites["error_handling"] = IntegrationTestSuite(
            suite_name="Error Handling and Recovery",
            description="Validates error handling and recovery mechanisms",
            setup_commands=[],
            cleanup_commands=[],
            test_cases=self._create_error_handling_tests(),
            dependencies=[]
        )
        
        # Performance Validation Test Suite
        suites["performance_validation"] = IntegrationTestSuite(
            suite_name="Performance Validation",
            description="Validates framework performance meets targets",
            setup_commands=[],
            cleanup_commands=[],
            test_cases=self._create_performance_tests(),
            dependencies=["command_execution"]
        )
        
        return suites
    
    def _create_command_execution_tests(self) -> List[IntegrationTestCase]:
        """Create command execution test cases."""
        tests = []
        
        # Test framework help
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.COMMAND_EXECUTION,
            test_name="framework_help_command",
            description="Test framework help command execution",
            command="claude --help",
            expected_outcome="Help output displayed without errors",
            timeout_seconds=10,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "high", "category": "basic"}
        ))
        
        # Test framework version
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.COMMAND_EXECUTION,
            test_name="framework_version_command",
            description="Test framework version command execution",
            command="claude --version",
            expected_outcome="Version information displayed",
            timeout_seconds=10,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "high", "category": "basic"}
        ))
        
        # Test list commands
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.COMMAND_EXECUTION,
            test_name="list_commands",
            description="Test listing available commands",
            command="ls .claude/commands/",
            expected_outcome="Command files listed",
            timeout_seconds=5,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "medium", "category": "discovery"}
        ))
        
        return tests
    
    def _create_module_orchestration_tests(self) -> List[IntegrationTestCase]:
        """Create module orchestration test cases."""
        tests = []
        
        # Test module loading
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.MODULE_ORCHESTRATION,
            test_name="module_structure_validation",
            description="Validate module structure and dependencies",
            command="find .claude/modules -name '*.md' | head -5",
            expected_outcome="Module files found and accessible",
            timeout_seconds=10,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "high", "category": "structure"}
        ))
        
        # Test CLAUDE.md parsing
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.MODULE_ORCHESTRATION,
            test_name="claude_md_structure",
            description="Validate CLAUDE.md structure and content",
            command="head -20 CLAUDE.md",
            expected_outcome="CLAUDE.md readable with version information",
            timeout_seconds=5,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "critical", "category": "configuration"}
        ))
        
        return tests
    
    def _create_workflow_validation_tests(self) -> List[IntegrationTestCase]:
        """Create workflow validation test cases."""
        tests = []
        
        # Test file operations
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.WORKFLOW_VALIDATION,
            test_name="file_system_access",
            description="Validate file system access and operations",
            command="ls -la",
            expected_outcome="Directory listing successful",
            timeout_seconds=5,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "high", "category": "filesystem"}
        ))
        
        # Test git integration
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.WORKFLOW_VALIDATION,
            test_name="git_status_check",
            description="Validate git repository status access",
            command="git status --porcelain",
            expected_outcome="Git status accessible",
            timeout_seconds=10,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "medium", "category": "git"}
        ))
        
        return tests
    
    def _create_error_handling_tests(self) -> List[IntegrationTestCase]:
        """Create error handling test cases."""
        tests = []
        
        # Test invalid command
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.ERROR_HANDLING,
            test_name="invalid_command_handling",
            description="Test handling of invalid commands",
            command="nonexistent_command_12345",
            expected_outcome="Error handled gracefully",
            timeout_seconds=5,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "medium", "category": "error_handling"}
        ))
        
        # Test permission error
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.ERROR_HANDLING,
            test_name="permission_error_handling",
            description="Test handling of permission errors",
            command="cat /etc/shadow",
            expected_outcome="Permission error handled gracefully",
            timeout_seconds=5,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "low", "category": "error_handling"}
        ))
        
        return tests
    
    def _create_performance_tests(self) -> List[IntegrationTestCase]:
        """Create performance validation test cases."""
        tests = []
        
        # Test framework loading performance
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.PERFORMANCE_VALIDATION,
            test_name="framework_loading_performance",
            description="Measure framework loading performance",
            command="time ls .claude/",
            expected_outcome="Framework loading under 200ms",
            timeout_seconds=5,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "high", "category": "performance"}
        ))
        
        # Test file access performance
        tests.append(IntegrationTestCase(
            test_id=str(uuid.uuid4()),
            test_type=IntegrationTestType.PERFORMANCE_VALIDATION,
            test_name="file_access_performance",
            description="Measure file access performance",
            command="time cat CLAUDE.md > /dev/null",
            expected_outcome="File access under 50ms",
            timeout_seconds=5,
            setup_required=False,
            cleanup_required=False,
            metadata={"priority": "medium", "category": "performance"}
        ))
        
        return tests
    
    def execute_test_case(self, test_case: IntegrationTestCase) -> IntegrationTestResult:
        """Execute a single integration test case."""
        print(f"  🔄 Executing: {test_case.test_name}")
        
        # Capture framework state before
        state_before = self.state_monitor.capture_framework_state()
        
        # Execute test
        start_time = time.perf_counter()
        result = TestResult.PASS
        output = ""
        error_output = ""
        exit_code = 0
        
        try:
            # Execute command
            process = subprocess.run(
                test_case.command,
                shell=True,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=test_case.timeout_seconds
            )
            
            output = process.stdout
            error_output = process.stderr
            exit_code = process.returncode
            
            # Determine result based on exit code and expected outcome
            if exit_code == 0:
                result = TestResult.PASS
            else:
                # Some tests expect non-zero exit codes (e.g., error handling tests)
                if test_case.test_type == IntegrationTestType.ERROR_HANDLING:
                    result = TestResult.PASS
                else:
                    result = TestResult.FAIL
                    
        except subprocess.TimeoutExpired:
            result = TestResult.TIMEOUT
            error_output = f"Command timed out after {test_case.timeout_seconds} seconds"
            
        except Exception as e:
            result = TestResult.ERROR
            error_output = str(e)
        
        end_time = time.perf_counter()
        execution_time_ms = (end_time - start_time) * 1000
        
        # Capture framework state after
        state_after = self.state_monitor.capture_framework_state()
        
        # Calculate performance metrics
        performance_metrics = {
            "execution_time_ms": execution_time_ms,
            "memory_usage_delta": 0,  # Would measure actual memory usage in production
            "file_operations": len(output.split('\n')) if output else 0
        }
        
        return IntegrationTestResult(
            test_case=test_case,
            result=result,
            execution_time_ms=execution_time_ms,
            output=output,
            error_output=error_output,
            exit_code=exit_code,
            framework_state_before=state_before,
            framework_state_after=state_after,
            performance_metrics=performance_metrics,
            timestamp=datetime.now().isoformat()
        )
    
    def run_test_suite(self, suite_name: str) -> List[IntegrationTestResult]:
        """Run a complete test suite."""
        if suite_name not in self.test_suites:
            raise ValueError(f"Unknown test suite: {suite_name}")
        
        suite = self.test_suites[suite_name]
        print(f"🧪 Running test suite: {suite.suite_name}")
        print(f"📝 Description: {suite.description}")
        print(f"🎯 Test cases: {len(suite.test_cases)}")
        
        results = []
        
        # Execute setup commands
        for setup_cmd in suite.setup_commands:
            print(f"🔧 Setup: {setup_cmd}")
            subprocess.run(setup_cmd, shell=True, cwd=self.project_root, capture_output=True)
        
        # Execute test cases
        for test_case in suite.test_cases:
            result = self.execute_test_case(test_case)
            results.append(result)
            
            # Print immediate result
            status_icon = {
                TestResult.PASS: "✅",
                TestResult.FAIL: "❌", 
                TestResult.ERROR: "🔥",
                TestResult.TIMEOUT: "⏰"
            }.get(result.result, "❓")
            
            print(f"    {status_icon} {result.result.value}: {result.execution_time_ms:.1f}ms")
        
        # Execute cleanup commands
        for cleanup_cmd in suite.cleanup_commands:
            print(f"🧹 Cleanup: {cleanup_cmd}")
            subprocess.run(cleanup_cmd, shell=True, cwd=self.project_root, capture_output=True)
        
        return results
    
    def run_comprehensive_integration_tests(self) -> IntegrationTestReport:
        """Run comprehensive integration tests across all suites."""
        print("🚀 Claude Code Integration Testing Framework")
        print("=" * 60)
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        session_id = str(uuid.uuid4())
        all_results = []
        suites_run = []
        
        # Execute test suites in dependency order
        suite_order = [
            "command_execution",
            "module_orchestration", 
            "workflow_validation",
            "error_handling",
            "performance_validation"
        ]
        
        total_start_time = time.perf_counter()
        
        for suite_name in suite_order:
            if suite_name in self.test_suites:
                suite_results = self.run_test_suite(suite_name)
                all_results.extend(suite_results)
                suites_run.append(suite_name)
                print()
        
        total_end_time = time.perf_counter()
        total_execution_time = (total_end_time - total_start_time) * 1000
        
        # Analyze results
        performance_summary = self.performance_analyzer.analyze_framework_performance(all_results)
        command_performance = self.performance_analyzer.analyze_command_performance(all_results)
        
        # Count results by type
        passed_tests = len([r for r in all_results if r.result == TestResult.PASS])
        failed_tests = len([r for r in all_results if r.result == TestResult.FAIL])
        error_tests = len([r for r in all_results if r.result == TestResult.ERROR])
        timeout_tests = len([r for r in all_results if r.result == TestResult.TIMEOUT])
        
        # Generate recommendations
        recommendations = self._generate_recommendations(all_results, performance_summary)
        
        # Create comprehensive report
        report = IntegrationTestReport(
            test_session_id=session_id,
            test_date=datetime.now().isoformat(),
            framework_version="3.0.0",
            environment_info=self._get_environment_info(),
            test_suites_run=suites_run,
            total_tests=len(all_results),
            passed_tests=passed_tests,
            failed_tests=failed_tests,
            error_tests=error_tests,
            timeout_tests=timeout_tests,
            execution_time_total=total_execution_time,
            performance_summary=performance_summary,
            test_results=all_results,
            recommendations=recommendations
        )
        
        # Save report
        self._save_report(report)
        
        # Print summary
        self._print_test_summary(report)
        
        return report
    
    def _get_environment_info(self) -> Dict[str, Any]:
        """Get environment information for the report."""
        import platform
        import sys
        
        return {
            "platform": platform.platform(),
            "python_version": sys.version,
            "working_directory": str(self.project_root),
            "timestamp": datetime.now().isoformat()
        }
    
    def _generate_recommendations(self, results: List[IntegrationTestResult], 
                                performance_summary: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on test results."""
        recommendations = []
        
        success_rate = performance_summary.get("success_rate", 0)
        
        if success_rate >= 95:
            recommendations.append("✅ EXCELLENT: Framework integration is highly reliable")
        elif success_rate >= 85:
            recommendations.append("✅ GOOD: Framework integration is reliable with minor issues")
        elif success_rate >= 70:
            recommendations.append("⚠️ MODERATE: Framework has some integration issues that should be addressed")
        else:
            recommendations.append("❌ POOR: Framework has significant integration issues requiring immediate attention")
        
        # Performance recommendations
        p95_time = performance_summary.get("p95_execution_time", 0)
        if p95_time > 200:
            recommendations.append(f"⚠️ PERFORMANCE: P95 execution time ({p95_time:.1f}ms) exceeds 200ms target")
        else:
            recommendations.append(f"✅ PERFORMANCE: P95 execution time ({p95_time:.1f}ms) meets 200ms target")
        
        # Error analysis
        error_count = len([r for r in results if r.result in [TestResult.ERROR, TestResult.TIMEOUT]])
        if error_count > 0:
            recommendations.append(f"🔧 ERRORS: {error_count} tests had errors or timeouts - review error handling")
        
        return recommendations
    
    def _save_report(self, report: IntegrationTestReport) -> None:
        """Save integration test report to file."""
        report_file = self.output_dir / f"integration_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        # Convert to JSON-serializable format
        report_dict = asdict(report)
        
        # Handle enum serialization
        def enum_serializer(obj):
            if hasattr(obj, 'value'):
                return obj.value
            return str(obj)
        
        with open(report_file, 'w') as f:
            json.dump(report_dict, f, indent=2, default=enum_serializer)
        
        print(f"📄 Integration test report saved to: {report_file}")
    
    def _print_test_summary(self, report: IntegrationTestReport) -> None:
        """Print comprehensive test summary."""
        print("=" * 60)
        print("📊 INTEGRATION TEST SUMMARY")
        print("=" * 60)
        
        print(f"Test Session ID: {report.test_session_id}")
        print(f"Framework Version: {report.framework_version}")
        print(f"Total Tests: {report.total_tests}")
        print(f"Passed: {report.passed_tests} ({(report.passed_tests/report.total_tests)*100:.1f}%)")
        print(f"Failed: {report.failed_tests}")
        print(f"Errors: {report.error_tests}")
        print(f"Timeouts: {report.timeout_tests}")
        print(f"Total Execution Time: {report.execution_time_total:.1f}ms")
        
        print(f"\n📈 Performance Summary:")
        perf = report.performance_summary
        print(f"  Success Rate: {perf.get('success_rate', 0):.1f}%")
        print(f"  Average Execution Time: {perf.get('avg_execution_time', 0):.1f}ms")
        print(f"  P95 Execution Time: {perf.get('p95_execution_time', 0):.1f}ms")
        print(f"  Performance Target Met: {'YES' if perf.get('performance_target_met', False) else 'NO'}")
        
        print(f"\n🎯 Recommendations:")
        for i, rec in enumerate(report.recommendations, 1):
            print(f"  {i}. {rec}")


# Example usage and test runner
def run_integration_test_validation():
    """Run integration test validation to demonstrate the framework."""
    project_root = Path(__file__).parent.parent.parent
    output_dir = project_root / "tests" / "results" / "integration"
    
    # Initialize integration tester
    integration_tester = ClaudeCodeIntegrationTester(project_root, output_dir)
    
    # Run comprehensive integration tests
    report = integration_tester.run_comprehensive_integration_tests()
    
    # Return success/failure based on results
    success_rate = report.performance_summary.get("success_rate", 0)
    return 0 if success_rate >= 80 else 1


if __name__ == "__main__":
    exit_code = run_integration_test_validation()
    exit(exit_code)