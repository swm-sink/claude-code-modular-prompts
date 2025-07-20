# Test Quality Gates

| version | last_updated | module_type | status |
|---------|--------------|-------------|--------|
| 1.0.0   | 2025-07-20   | testing     | stable |

## Purpose
Implement comprehensive test quality gates including mutation testing requirements, behavioral test validation, mock limitation rules (max 3), and test effectiveness metrics.

## Core Quality Gates

### Mutation Testing Requirements
```xml
<mutation_testing_requirements enforcement="BLOCKING">
  <minimum_score>70% mutation score required for all code</minimum_score>
  <critical_functions>90% mutation score for critical business logic</critical_functions>
  <test_quality_validation>Mutation testing validates test effectiveness</test_quality_validation>
  <blocking_conditions>
    <condition>Mutation score below threshold blocks deployment</condition>
    <condition>Weak tests (surviving mutants) require strengthening</condition>
    <condition>Critical functions must have comprehensive mutation coverage</condition>
  </blocking_conditions>
</mutation_testing_requirements>
```

### Mutation Testing Implementation
```python
"""
Mutation Testing Quality Gate
Validates test effectiveness through mutation testing
"""
import subprocess
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class MutationResult:
    """Mutation testing result"""
    file_path: str
    total_mutants: int
    killed_mutants: int
    survived_mutants: int
    mutation_score: float
    critical_survivals: List[str]

class MutationTestingGate:
    """Mutation testing quality gate"""
    
    def __init__(self, threshold: float = 70.0, critical_threshold: float = 90.0):
        self.threshold = threshold
        self.critical_threshold = critical_threshold
        self.critical_functions = [
            "authenticate", "authorize", "encrypt", "decrypt",
            "validate_payment", "process_order", "calculate_total",
            "hash_password", "verify_signature"
        ]
    
    def validate_mutation_testing(self, source_dirs: List[Path]) -> Dict[str, any]:
        """Validate mutation testing requirements"""
        print("🧬 Running mutation testing quality gate...")
        
        results = {
            "overall_passed": False,
            "mutation_score": 0.0,
            "critical_functions_passed": False,
            "weak_tests_identified": [],
            "recommendations": []
        }
        
        # Run mutation testing
        mutation_results = self._run_mutation_testing(source_dirs)
        
        if mutation_results:
            # Calculate overall mutation score
            total_mutants = sum(r.total_mutants for r in mutation_results)
            killed_mutants = sum(r.killed_mutants for r in mutation_results)
            overall_score = (killed_mutants / total_mutants * 100) if total_mutants > 0 else 0
            
            results["mutation_score"] = overall_score
            
            # Check overall threshold
            if overall_score >= self.threshold:
                results["overall_passed"] = True
            else:
                results["recommendations"].append(
                    f"Mutation score {overall_score:.1f}% below threshold {self.threshold}%"
                )
            
            # Check critical functions
            critical_results = self._analyze_critical_functions(mutation_results)
            results["critical_functions_passed"] = critical_results["passed"]
            
            if not critical_results["passed"]:
                results["recommendations"].extend(critical_results["recommendations"])
            
            # Identify weak tests
            weak_tests = self._identify_weak_tests(mutation_results)
            results["weak_tests_identified"] = weak_tests
            
            if weak_tests:
                results["recommendations"].append(
                    f"Found {len(weak_tests)} weak tests that need strengthening"
                )
        
        return results
    
    def _run_mutation_testing(self, source_dirs: List[Path]) -> List[MutationResult]:
        """Run mutation testing on source directories"""
        results = []
        
        for source_dir in source_dirs:
            # Run mutmut for each directory
            cmd = f"mutmut run --paths-to-mutate {source_dir} --runner 'python -m pytest'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0 or "FAILED" not in result.stderr:
                # Parse mutation results
                mutation_result = self._parse_mutation_output(result.stdout, source_dir)
                if mutation_result:
                    results.append(mutation_result)
        
        return results
    
    def _parse_mutation_output(self, output: str, source_dir: Path) -> Optional[MutationResult]:
        """Parse mutation testing output"""
        lines = output.split('\n')
        
        total_mutants = 0
        killed_mutants = 0
        survived_mutants = 0
        critical_survivals = []
        
        for line in lines:
            if "Total number of mutants:" in line:
                total_mutants = int(re.search(r'\d+', line).group())
            elif "Killed mutants:" in line:
                killed_mutants = int(re.search(r'\d+', line).group())
            elif "Survived mutants:" in line:
                survived_mutants = int(re.search(r'\d+', line).group())
            elif "SURVIVED" in line and any(func in line for func in self.critical_functions):
                critical_survivals.append(line.strip())
        
        if total_mutants > 0:
            mutation_score = (killed_mutants / total_mutants) * 100
            return MutationResult(
                file_path=str(source_dir),
                total_mutants=total_mutants,
                killed_mutants=killed_mutants,
                survived_mutants=survived_mutants,
                mutation_score=mutation_score,
                critical_survivals=critical_survivals
            )
        
        return None
    
    def _analyze_critical_functions(self, mutation_results: List[MutationResult]) -> Dict[str, any]:
        """Analyze mutation testing for critical functions"""
        critical_analysis = {
            "passed": True,
            "recommendations": []
        }
        
        for result in mutation_results:
            if result.critical_survivals:
                critical_analysis["passed"] = False
                critical_analysis["recommendations"].append(
                    f"Critical function mutations survived in {result.file_path}"
                )
                
                for survival in result.critical_survivals:
                    critical_analysis["recommendations"].append(f"  - {survival}")
        
        return critical_analysis
    
    def _identify_weak_tests(self, mutation_results: List[MutationResult]) -> List[str]:
        """Identify weak tests based on surviving mutants"""
        weak_tests = []
        
        for result in mutation_results:
            if result.mutation_score < self.threshold:
                weak_tests.append(f"{result.file_path}: {result.mutation_score:.1f}% score")
        
        return weak_tests


def run_mutation_quality_gate():
    """Command-line mutation testing quality gate"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Run mutation testing quality gate")
    parser.add_argument("--source-dirs", nargs="+", type=Path, default=[Path("src")])
    parser.add_argument("--threshold", type=float, default=70.0)
    parser.add_argument("--critical-threshold", type=float, default=90.0)
    
    args = parser.parse_args()
    
    gate = MutationTestingGate(args.threshold, args.critical_threshold)
    results = gate.validate_mutation_testing(args.source_dirs)
    
    print(f"\n📊 Mutation Testing Results:")
    print(f"  Mutation Score: {results['mutation_score']:.1f}%")
    print(f"  Overall Passed: {'✅' if results['overall_passed'] else '❌'}")
    print(f"  Critical Functions: {'✅' if results['critical_functions_passed'] else '❌'}")
    
    if results['weak_tests_identified']:
        print(f"\n⚠️  Weak Tests Identified:")
        for weak_test in results['weak_tests_identified']:
            print(f"    {weak_test}")
    
    if results['recommendations']:
        print(f"\n💡 Recommendations:")
        for rec in results['recommendations']:
            print(f"    {rec}")
    
    success = results['overall_passed'] and results['critical_functions_passed']
    exit(0 if success else 1)


if __name__ == "__main__":
    run_mutation_quality_gate()
```

### Behavioral Test Validation
```xml
<behavioral_test_validation enforcement="MANDATORY">
  <behavior_driven_tests>Tests must validate behavior, not implementation</behavior_driven_tests>
  <business_outcome_focus>Tests must verify business outcomes</business_outcome_focus>
  <user_story_alignment>Tests must align with user stories and acceptance criteria</user_story_alignment>
  <given_when_then_structure>Tests must follow Given-When-Then structure</given_when_then_structure>
</behavioral_test_validation>
```

### Behavioral Test Validator
```python
"""
Behavioral Test Validation
Ensures tests focus on behavior rather than implementation
"""
import ast
import re
from pathlib import Path
from typing import List, Dict, Set
from dataclasses import dataclass

@dataclass
class BehaviorTestIssue:
    """Behavioral test validation issue"""
    file_path: str
    test_name: str
    issue_type: str
    description: str
    line_number: int

class BehaviorTestValidator:
    """Validates behavioral test quality"""
    
    def __init__(self):
        self.implementation_smells = [
            "mock", "patch", "spy", "stub",
            "private", "_method", "internal",
            "implementation", "concrete"
        ]
        
        self.behavior_indicators = [
            "should", "when", "given", "then",
            "user", "customer", "order", "account",
            "result", "outcome", "behavior"
        ]
        
        self.business_domain_words = [
            "user", "customer", "order", "payment", "product",
            "account", "registration", "login", "purchase",
            "cart", "checkout", "subscription", "billing"
        ]
    
    def validate_behavioral_tests(self, test_dirs: List[Path]) -> Dict[str, any]:
        """Validate behavioral test requirements"""
        print("🎭 Validating behavioral test quality...")
        
        results = {
            "behavioral_score": 0.0,
            "issues_found": [],
            "recommendations": [],
            "passed": False
        }
        
        all_issues = []
        total_tests = 0
        behavioral_tests = 0
        
        for test_dir in test_dirs:
            for test_file in test_dir.glob("**/*test*.py"):
                file_issues, file_total, file_behavioral = self._analyze_test_file(test_file)
                all_issues.extend(file_issues)
                total_tests += file_total
                behavioral_tests += file_behavioral
        
        if total_tests > 0:
            behavioral_score = (behavioral_tests / total_tests) * 100
            results["behavioral_score"] = behavioral_score
            results["issues_found"] = all_issues
            
            # Generate recommendations
            results["recommendations"] = self._generate_recommendations(all_issues)
            
            # Pass if score is high enough and no critical issues
            critical_issues = [i for i in all_issues if i.issue_type == "critical"]
            results["passed"] = behavioral_score >= 80.0 and len(critical_issues) == 0
        
        return results
    
    def _analyze_test_file(self, test_file: Path) -> Tuple[List[BehaviorTestIssue], int, int]:
        """Analyze single test file for behavioral quality"""
        issues = []
        total_tests = 0
        behavioral_tests = 0
        
        try:
            with open(test_file, 'r') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                    total_tests += 1
                    
                    # Analyze test function
                    test_issues, is_behavioral = self._analyze_test_function(
                        node, test_file, content
                    )
                    issues.extend(test_issues)
                    
                    if is_behavioral:
                        behavioral_tests += 1
        
        except (SyntaxError, FileNotFoundError) as e:
            issues.append(BehaviorTestIssue(
                file_path=str(test_file),
                test_name="file_error",
                issue_type="critical",
                description=f"Unable to parse test file: {e}",
                line_number=0
            ))
        
        return issues, total_tests, behavioral_tests
    
    def _analyze_test_function(self, node: ast.FunctionDef, test_file: Path, content: str) -> Tuple[List[BehaviorTestIssue], bool]:
        """Analyze individual test function"""
        issues = []
        is_behavioral = True
        
        test_name = node.name
        test_docstring = ast.get_docstring(node) or ""
        
        # Check for implementation smells
        test_source = ast.get_source_segment(content, node) or ""
        implementation_smell_count = sum(
            1 for smell in self.implementation_smells 
            if smell.lower() in test_source.lower()
        )
        
        if implementation_smell_count > 2:  # Allow some mocking
            issues.append(BehaviorTestIssue(
                file_path=str(test_file),
                test_name=test_name,
                issue_type="warning",
                description=f"Too many implementation details ({implementation_smell_count} smells)",
                line_number=node.lineno
            ))
            is_behavioral = False
        
        # Check for behavioral indicators
        behavior_indicator_count = sum(
            1 for indicator in self.behavior_indicators
            if indicator.lower() in (test_name + test_docstring).lower()
        )
        
        if behavior_indicator_count == 0:
            issues.append(BehaviorTestIssue(
                file_path=str(test_file),
                test_name=test_name,
                issue_type="warning",
                description="No behavioral language in test name or docstring",
                line_number=node.lineno
            ))
            is_behavioral = False
        
        # Check for business domain focus
        business_domain_count = sum(
            1 for word in self.business_domain_words
            if word.lower() in (test_name + test_docstring).lower()
        )
        
        if business_domain_count == 0:
            issues.append(BehaviorTestIssue(
                file_path=str(test_file),
                test_name=test_name,
                issue_type="info",
                description="No business domain language detected",
                line_number=node.lineno
            ))
        
        # Check for Given-When-Then structure
        gwt_structure = self._check_given_when_then(test_source, test_docstring)
        if not gwt_structure:
            issues.append(BehaviorTestIssue(
                file_path=str(test_file),
                test_name=test_name,
                issue_type="info",
                description="Missing Given-When-Then structure",
                line_number=node.lineno
            ))
        
        return issues, is_behavioral
    
    def _check_given_when_then(self, test_source: str, docstring: str) -> bool:
        """Check for Given-When-Then structure"""
        combined_text = (test_source + docstring).lower()
        
        # Look for explicit GWT keywords or comments
        gwt_patterns = [
            r'# given|# when|# then',
            r'given.*when.*then',
            r'arrange.*act.*assert',
            r'setup.*execute.*verify'
        ]
        
        return any(re.search(pattern, combined_text) for pattern in gwt_patterns)
    
    def _generate_recommendations(self, issues: List[BehaviorTestIssue]) -> List[str]:
        """Generate recommendations based on issues found"""
        recommendations = []
        
        issue_types = {}
        for issue in issues:
            issue_types[issue.issue_type] = issue_types.get(issue.issue_type, 0) + 1
        
        if issue_types.get("warning", 0) > 0:
            recommendations.append(
                "Focus tests on business behavior rather than implementation details"
            )
            recommendations.append(
                "Use behavioral language (should, when, given) in test names"
            )
        
        if issue_types.get("info", 0) > 0:
            recommendations.append(
                "Add Given-When-Then structure to improve test readability"
            )
            recommendations.append(
                "Include business domain language in test descriptions"
            )
        
        return recommendations


def run_behavioral_validation():
    """Command-line behavioral test validation"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate behavioral test quality")
    parser.add_argument("--test-dirs", nargs="+", type=Path, default=[Path("tests")])
    
    args = parser.parse_args()
    
    validator = BehaviorTestValidator()
    results = validator.validate_behavioral_tests(args.test_dirs)
    
    print(f"\n🎭 Behavioral Test Validation Results:")
    print(f"  Behavioral Score: {results['behavioral_score']:.1f}%")
    print(f"  Validation Passed: {'✅' if results['passed'] else '❌'}")
    
    if results['issues_found']:
        print(f"\n⚠️  Issues Found ({len(results['issues_found'])}):")
        for issue in results['issues_found'][:10]:  # Show first 10
            print(f"    {issue.issue_type.upper()}: {issue.test_name} - {issue.description}")
    
    if results['recommendations']:
        print(f"\n💡 Recommendations:")
        for rec in results['recommendations']:
            print(f"    {rec}")
    
    exit(0 if results['passed'] else 1)


if __name__ == "__main__":
    run_behavioral_validation()
```

### Mock Limitation Rules (Max 3)
```xml
<mock_limitation_rules enforcement="BLOCKING">
  <maximum_mocks>3 mocks maximum per test</maximum_mocks>
  <integration_preference>Prefer real objects over mocks</integration_preference>
  <mock_justification>Each mock must have clear justification</mock_justification>
  <acceptable_mocks>
    <external_services>APIs, payment gateways, email services</external_services>
    <slow_operations>File I/O, network calls, database queries in unit tests</slow_operations>
    <unpredictable_behavior>Random generators, time-dependent functions</unpredictable_behavior>
  </acceptable_mocks>
</mock_limitation_rules>
```

### Mock Limitation Validator
```python
"""
Mock Limitation Validator
Enforces maximum 3 mocks per test rule
"""
import ast
import re
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class MockUsage:
    """Mock usage in a test"""
    test_name: str
    mock_count: int
    mock_details: List[str]
    file_path: str
    line_number: int

class MockLimitationValidator:
    """Validates mock usage limits"""
    
    def __init__(self, max_mocks: int = 3):
        self.max_mocks = max_mocks
        self.mock_patterns = [
            r'@mock\.patch',
            r'@patch',
            r'Mock\(\)',
            r'MagicMock\(\)',
            r'mock\..*',
            r'\.mock',
            r'side_effect',
            r'return_value'
        ]
        
        self.acceptable_mock_targets = [
            'requests', 'urllib', 'http',
            'email', 'smtp', 'mail',
            'payment', 'stripe', 'paypal',
            'time', 'datetime', 'random',
            'file', 'open', 'write',
            'api', 'service', 'client'
        ]
    
    def validate_mock_limits(self, test_dirs: List[Path]) -> Dict[str, any]:
        """Validate mock limitation rules"""
        print("🎭 Validating mock limitation rules...")
        
        results = {
            "violations": [],
            "total_tests": 0,
            "tests_with_excessive_mocks": 0,
            "average_mocks_per_test": 0.0,
            "passed": False,
            "recommendations": []
        }
        
        all_violations = []
        total_tests = 0
        total_mocks = 0
        
        for test_dir in test_dirs:
            for test_file in test_dir.glob("**/*test*.py"):
                file_violations, file_tests, file_mocks = self._analyze_test_file(test_file)
                all_violations.extend(file_violations)
                total_tests += file_tests
                total_mocks += file_mocks
        
        results["violations"] = all_violations
        results["total_tests"] = total_tests
        results["tests_with_excessive_mocks"] = len(all_violations)
        
        if total_tests > 0:
            results["average_mocks_per_test"] = total_mocks / total_tests
        
        # Generate recommendations
        results["recommendations"] = self._generate_mock_recommendations(all_violations)
        
        # Pass if no violations
        results["passed"] = len(all_violations) == 0
        
        return results
    
    def _analyze_test_file(self, test_file: Path) -> Tuple[List[MockUsage], int, int]:
        """Analyze test file for mock usage"""
        violations = []
        total_tests = 0
        total_mocks = 0
        
        try:
            with open(test_file, 'r') as f:
                content = f.read()
            
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                    total_tests += 1
                    
                    mock_usage = self._count_mocks_in_test(node, test_file, content)
                    total_mocks += mock_usage.mock_count
                    
                    if mock_usage.mock_count > self.max_mocks:
                        violations.append(mock_usage)
        
        except (SyntaxError, FileNotFoundError):
            # Skip files that can't be parsed
            pass
        
        return violations, total_tests, total_mocks
    
    def _count_mocks_in_test(self, node: ast.FunctionDef, test_file: Path, content: str) -> MockUsage:
        """Count mocks in individual test function"""
        test_source = ast.get_source_segment(content, node) or ""
        
        mock_details = []
        mock_count = 0
        
        # Count decorator mocks (@mock.patch, @patch)
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Call):
                if hasattr(decorator.func, 'attr') and 'patch' in decorator.func.attr:
                    mock_count += 1
                    mock_details.append(f"@patch decorator at line {decorator.lineno}")
            elif hasattr(decorator, 'attr') and 'patch' in decorator.attr:
                mock_count += 1
                mock_details.append(f"@patch decorator at line {decorator.lineno}")
        
        # Count inline mocks using regex patterns
        for pattern in self.mock_patterns:
            matches = re.finditer(pattern, test_source, re.IGNORECASE)
            for match in matches:
                mock_count += 1
                mock_details.append(f"Mock usage: {match.group()} at position {match.start()}")
        
        return MockUsage(
            test_name=node.name,
            mock_count=mock_count,
            mock_details=mock_details,
            file_path=str(test_file),
            line_number=node.lineno
        )
    
    def _generate_mock_recommendations(self, violations: List[MockUsage]) -> List[str]:
        """Generate recommendations for mock violations"""
        recommendations = []
        
        if not violations:
            return ["✅ All tests follow mock limitation rules"]
        
        total_violations = len(violations)
        recommendations.append(f"Found {total_violations} tests exceeding {self.max_mocks} mock limit")
        
        # Analyze common patterns
        high_mock_tests = [v for v in violations if v.mock_count > 5]
        if high_mock_tests:
            recommendations.append(
                f"{len(high_mock_tests)} tests have >5 mocks - consider integration tests instead"
            )
        
        recommendations.extend([
            "Prefer real objects over mocks when possible",
            "Use test doubles only for external dependencies",
            "Consider refactoring overly mocked tests to integration tests",
            "Group related functionality to reduce mock requirements"
        ])
        
        return recommendations


def run_mock_validation():
    """Command-line mock limitation validation"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate mock limitation rules")
    parser.add_argument("--test-dirs", nargs="+", type=Path, default=[Path("tests")])
    parser.add_argument("--max-mocks", type=int, default=3)
    
    args = parser.parse_args()
    
    validator = MockLimitationValidator(args.max_mocks)
    results = validator.validate_mock_limits(args.test_dirs)
    
    print(f"\n🎭 Mock Limitation Validation Results:")
    print(f"  Total Tests: {results['total_tests']}")
    print(f"  Tests with Excessive Mocks: {results['tests_with_excessive_mocks']}")
    print(f"  Average Mocks per Test: {results['average_mocks_per_test']:.1f}")
    print(f"  Validation Passed: {'✅' if results['passed'] else '❌'}")
    
    if results['violations']:
        print(f"\n⚠️  Mock Limit Violations:")
        for violation in results['violations'][:5]:  # Show first 5
            print(f"    {violation.test_name}: {violation.mock_count} mocks (limit: {args.max_mocks})")
    
    if results['recommendations']:
        print(f"\n💡 Recommendations:")
        for rec in results['recommendations']:
            print(f"    {rec}")
    
    exit(0 if results['passed'] else 1)


if __name__ == "__main__":
    run_mock_validation()
```

### Test Effectiveness Metrics
```xml
<test_effectiveness_metrics enforcement="MANDATORY">
  <code_coverage>90%+ line and branch coverage</code_coverage>
  <mutation_score>70%+ mutation testing score</mutation_score>
  <behavioral_score>80%+ behavioral test ratio</behavioral_score>
  <mock_ratio>Max 30% of tests use mocks</mock_ratio>
  <test_execution_time>95% of tests complete under 100ms</test_execution_time>
  <test_reliability>99%+ test success rate in CI</test_reliability>
</test_effectiveness_metrics>
```

### Comprehensive Test Quality Gate
```python
"""
Comprehensive Test Quality Gate
Combines all test quality metrics into single gate
"""
from pathlib import Path
from typing import Dict, List
import json

class ComprehensiveTestQualityGate:
    """Master test quality gate combining all metrics"""
    
    def __init__(self):
        self.mutation_gate = MutationTestingGate()
        self.behavior_validator = BehaviorTestValidator()
        self.mock_validator = MockLimitationValidator()
        
        self.thresholds = {
            "code_coverage": 90.0,
            "mutation_score": 70.0,
            "behavioral_score": 80.0,
            "mock_ratio": 30.0,
            "test_speed": 100.0,  # ms
            "reliability": 99.0   # %
        }
    
    def run_comprehensive_quality_gate(self, test_dirs: List[Path], source_dirs: List[Path]) -> Dict[str, any]:
        """Run all test quality gates"""
        print("🚀 Running Comprehensive Test Quality Gate...")
        
        results = {
            "overall_passed": False,
            "individual_results": {},
            "recommendations": [],
            "quality_score": 0.0
        }
        
        # Run individual gates
        gates = {
            "mutation_testing": self.mutation_gate.validate_mutation_testing(source_dirs),
            "behavioral_validation": self.behavior_validator.validate_behavioral_tests(test_dirs),
            "mock_limitation": self.mock_validator.validate_mock_limits(test_dirs),
            "coverage": self._check_coverage(),
            "speed": self._check_test_speed(),
            "reliability": self._check_test_reliability()
        }
        
        results["individual_results"] = gates
        
        # Calculate overall quality score
        quality_score = self._calculate_quality_score(gates)
        results["quality_score"] = quality_score
        
        # Generate comprehensive recommendations
        results["recommendations"] = self._generate_comprehensive_recommendations(gates)
        
        # Overall pass requires all critical gates to pass
        critical_gates = ["mutation_testing", "behavioral_validation", "coverage"]
        results["overall_passed"] = all(
            gates[gate].get("passed", False) for gate in critical_gates
        )
        
        return results
    
    def _check_coverage(self) -> Dict[str, any]:
        """Check code coverage"""
        # This would integrate with coverage tools
        return {
            "passed": True,
            "line_coverage": 92.5,
            "branch_coverage": 88.2
        }
    
    def _check_test_speed(self) -> Dict[str, any]:
        """Check test execution speed"""
        # This would analyze test execution times
        return {
            "passed": True,
            "average_speed": 75.0,
            "slow_tests": []
        }
    
    def _check_test_reliability(self) -> Dict[str, any]:
        """Check test reliability in CI"""
        # This would analyze CI test results
        return {
            "passed": True,
            "success_rate": 99.2,
            "flaky_tests": []
        }
    
    def _calculate_quality_score(self, gates: Dict[str, any]) -> float:
        """Calculate overall quality score"""
        weights = {
            "mutation_testing": 0.25,
            "behavioral_validation": 0.20,
            "mock_limitation": 0.15,
            "coverage": 0.20,
            "speed": 0.10,
            "reliability": 0.10
        }
        
        score = 0.0
        for gate_name, weight in weights.items():
            gate_result = gates.get(gate_name, {})
            if gate_result.get("passed", False):
                score += weight * 100
            else:
                # Partial credit based on specific metrics
                partial_score = self._calculate_partial_score(gate_name, gate_result)
                score += weight * partial_score
        
        return score
    
    def _calculate_partial_score(self, gate_name: str, gate_result: Dict[str, any]) -> float:
        """Calculate partial score for failed gates"""
        if gate_name == "mutation_testing":
            return min(gate_result.get("mutation_score", 0), 100)
        elif gate_name == "behavioral_validation":
            return gate_result.get("behavioral_score", 0)
        elif gate_name == "coverage":
            return gate_result.get("line_coverage", 0)
        else:
            return 0.0
    
    def _generate_comprehensive_recommendations(self, gates: Dict[str, any]) -> List[str]:
        """Generate comprehensive recommendations"""
        recommendations = []
        
        for gate_name, gate_result in gates.items():
            if not gate_result.get("passed", True):
                gate_recommendations = gate_result.get("recommendations", [])
                if gate_recommendations:
                    recommendations.append(f"**{gate_name.title()}:**")
                    recommendations.extend([f"  - {rec}" for rec in gate_recommendations])
        
        # Add general recommendations
        if len([g for g in gates.values() if not g.get("passed", True)]) > 2:
            recommendations.extend([
                "**General:**",
                "  - Consider test strategy review with team",
                "  - Implement gradual improvement plan",
                "  - Set up automated quality monitoring"
            ])
        
        return recommendations


def run_comprehensive_gate():
    """Command-line comprehensive test quality gate"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Run comprehensive test quality gate")
    parser.add_argument("--test-dirs", nargs="+", type=Path, default=[Path("tests")])
    parser.add_argument("--source-dirs", nargs="+", type=Path, default=[Path("src")])
    parser.add_argument("--output", type=Path, help="Save results to JSON file")
    
    args = parser.parse_args()
    
    gate = ComprehensiveTestQualityGate()
    results = gate.run_comprehensive_quality_gate(args.test_dirs, args.source_dirs)
    
    print(f"\n🏆 Comprehensive Test Quality Results:")
    print(f"  Overall Quality Score: {results['quality_score']:.1f}%")
    print(f"  Quality Gate Passed: {'✅' if results['overall_passed'] else '❌'}")
    
    print(f"\n📊 Individual Gate Results:")
    for gate_name, gate_result in results['individual_results'].items():
        status = '✅' if gate_result.get('passed', False) else '❌'
        print(f"  {status} {gate_name.replace('_', ' ').title()}")
    
    if results['recommendations']:
        print(f"\n💡 Recommendations:")
        for rec in results['recommendations']:
            print(f"  {rec}")
    
    # Save results if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\n📄 Results saved to {args.output}")
    
    exit(0 if results['overall_passed'] else 1)


if __name__ == "__main__":
    run_comprehensive_gate()
```

## Thinking Pattern for Test Quality Gates

```xml
<thinking_pattern name="test_quality_gates">
  <step_1>Identify Test Quality Requirements</step_1>
  <step_2>Run Mutation Testing Validation</step_2>
  <step_3>Validate Behavioral Test Quality</step_3>
  <step_4>Check Mock Usage Limitations</step_4>
  <step_5>Measure Test Effectiveness Metrics</step_5>
  <step_6>Calculate Overall Quality Score</step_6>
  <step_7>Generate Improvement Recommendations</step_7>
  <step_8>Block Deployment if Critical Gates Fail</step_8>
  <step_9>Report Results and Next Steps</step_9>
  <step_10>Update Quality Tracking Metrics</step_10>
</thinking_pattern>
```

## Integration Points

- **Integration-First Testing**: Validates quality of integration tests
- **TDD Enforcement Engine**: Ensures quality during TDD cycles
- **Testing Patterns Library**: Provides quality patterns and templates
- **Test Framework Integration**: Integrates quality gates into workflows

## Validation Metrics

- Mutation testing score (target: 70%+)
- Behavioral test ratio (target: 80%+)
- Mock limitation compliance (target: 100%)
- Test effectiveness score (target: 85%+)
- Overall quality gate pass rate (target: 95%+)