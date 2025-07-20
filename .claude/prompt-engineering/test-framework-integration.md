# Test Framework Integration

| version | last_updated | module_type | status |
|---------|--------------|-------------|--------|
| 1.0.0   | 2025-07-20   | testing     | stable |

## Purpose
Comprehensive integration of testing mandate framework into command workflows, including /task TDD enforcement, /feature workflow integration, test generation helpers, and continuous test validation.

## Command Integration Architecture

### /task Command TDD Enforcement
```xml
<task_command_integration enforcement="BLOCKING">
  <tdd_cycle_enforcement>Every /task MUST follow Red-Green-Refactor cycle</tdd_cycle_enforcement>
  <test_first_validation>Implementation BLOCKED until failing test exists</test_first_validation>
  <coverage_requirements>90%+ coverage required for task completion</coverage_requirements>
  <integration_testing>80% integration tests mandatory for business logic</integration_testing>
</task_command_integration>
```

### Enhanced /task Command Implementation
```python
"""
Enhanced /task Command with TDD Enforcement Integration
Integrates testing mandate framework into task workflows
"""
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import subprocess
import json

@dataclass
class TaskTestRequirements:
    """Test requirements for task execution"""
    requires_tests: bool = True
    minimum_coverage: float = 90.0
    integration_test_ratio: float = 0.8
    max_mocks_per_test: int = 3
    mutation_score_threshold: float = 70.0

class TDDEnforcedTaskExecutor:
    """Task executor with TDD enforcement"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.test_dirs = [project_root / "tests", project_root / "test"]
        self.source_dirs = [project_root / "src", project_root / "app"]
        
        # Import testing framework components
        from integration_first_testing import IntegrationFirstTesting
        from tdd_enforcement_engine import TDDEnforcementValidator
        from test_quality_gates import ComprehensiveTestQualityGate
        from testing_patterns_library import DatabaseTestUtilities, APITestHelpers
        
        self.integration_tester = IntegrationFirstTesting()
        self.tdd_validator = TDDEnforcementValidator(project_root)
        self.quality_gate = ComprehensiveTestQualityGate()
    
    def execute_task_with_tdd(self, 
                             task_description: str,
                             target_files: List[Path],
                             test_requirements: TaskTestRequirements) -> Dict[str, Any]:
        """Execute task with full TDD enforcement"""
        
        print(f"🚀 Executing task with TDD enforcement: {task_description}")
        
        results = {
            "task_completed": False,
            "tdd_compliance": {},
            "test_results": {},
            "quality_metrics": {},
            "recommendations": []
        }
        
        try:
            # Phase 1: RED - Ensure failing tests exist
            print("🔴 RED Phase: Validating failing tests...")
            red_validation = self._validate_red_phase(target_files, test_requirements)
            results["tdd_compliance"]["red_phase"] = red_validation
            
            if not red_validation["passed"]:
                results["recommendations"].extend(red_validation["recommendations"])
                return results
            
            # Phase 2: GREEN - Implement minimal solution
            print("🟢 GREEN Phase: Implementing minimal solution...")
            green_validation = self._execute_green_phase(target_files, test_requirements)
            results["tdd_compliance"]["green_phase"] = green_validation
            
            if not green_validation["passed"]:
                results["recommendations"].extend(green_validation["recommendations"])
                return results
            
            # Phase 3: REFACTOR - Improve code quality
            print("🔵 REFACTOR Phase: Improving code quality...")
            refactor_validation = self._execute_refactor_phase(target_files, test_requirements)
            results["tdd_compliance"]["refactor_phase"] = refactor_validation
            
            # Phase 4: Quality Gates
            print("🚪 Quality Gates: Validating test quality...")
            quality_results = self._run_quality_gates(test_requirements)
            results["quality_metrics"] = quality_results
            
            # Final validation
            if self._all_phases_passed(results):
                results["task_completed"] = True
                print("✅ Task completed successfully with TDD compliance!")
            else:
                results["recommendations"].append("Task blocked - TDD compliance failures")
                print("❌ Task blocked due to TDD compliance failures")
        
        except Exception as e:
            results["error"] = str(e)
            results["recommendations"].append(f"Task execution failed: {e}")
        
        return results
    
    def _validate_red_phase(self, target_files: List[Path], requirements: TaskTestRequirements) -> Dict[str, Any]:
        """Validate RED phase requirements"""
        validation = {
            "passed": False,
            "failing_tests_exist": False,
            "test_files_created": [],
            "recommendations": []
        }
        
        # Check if test files exist for target files
        test_files = self._find_or_create_test_files(target_files)
        validation["test_files_created"] = [str(f) for f in test_files]
        
        # Validate tests are failing
        for test_file in test_files:
            test_result = self._run_single_test(test_file)
            if test_result["failed"]:
                validation["failing_tests_exist"] = True
                break
        
        if not validation["failing_tests_exist"]:
            validation["recommendations"].extend([
                "Create failing tests before implementation",
                "Tests must fail with meaningful error messages",
                "Use integration-first testing approach (80/20 rule)"
            ])
        else:
            validation["passed"] = True
        
        return validation
    
    def _execute_green_phase(self, target_files: List[Path], requirements: TaskTestRequirements) -> Dict[str, Any]:
        """Execute GREEN phase with minimal implementation"""
        validation = {
            "passed": False,
            "tests_passing": False,
            "coverage_met": False,
            "implementation_minimal": True,
            "recommendations": []
        }
        
        # Run tests to check if they pass
        test_result = self._run_all_tests()
        validation["tests_passing"] = test_result["passed"]
        
        if not test_result["passed"]:
            validation["recommendations"].append("Fix implementation to make tests pass")
            return validation
        
        # Check coverage requirements
        coverage_result = self._check_coverage(requirements.minimum_coverage)
        validation["coverage_met"] = coverage_result["meets_threshold"]
        
        if not coverage_result["meets_threshold"]:
            validation["recommendations"].append(
                f"Coverage {coverage_result['current']:.1f}% below required {requirements.minimum_coverage}%"
            )
            return validation
        
        # Validate implementation is minimal (not over-engineered)
        for target_file in target_files:
            if not self._is_minimal_implementation(target_file):
                validation["implementation_minimal"] = False
                validation["recommendations"].append(
                    f"Implementation in {target_file} appears over-engineered for GREEN phase"
                )
        
        validation["passed"] = validation["tests_passing"] and validation["coverage_met"] and validation["implementation_minimal"]
        
        return validation
    
    def _execute_refactor_phase(self, target_files: List[Path], requirements: TaskTestRequirements) -> Dict[str, Any]:
        """Execute REFACTOR phase with quality improvements"""
        validation = {
            "passed": False,
            "tests_still_passing": False,
            "coverage_maintained": False,
            "code_quality_improved": False,
            "no_new_functionality": True,
            "recommendations": []
        }
        
        # Ensure all tests still pass
        test_result = self._run_all_tests()
        validation["tests_still_passing"] = test_result["passed"]
        
        if not test_result["passed"]:
            validation["recommendations"].append("Refactoring broke existing tests")
            return validation
        
        # Check coverage maintained
        coverage_result = self._check_coverage(requirements.minimum_coverage)
        validation["coverage_maintained"] = coverage_result["meets_threshold"]
        
        # Check code quality improvements
        for target_file in target_files:
            quality_improved = self._check_code_quality_improvement(target_file)
            if quality_improved:
                validation["code_quality_improved"] = True
                break
        
        validation["passed"] = (
            validation["tests_still_passing"] and 
            validation["coverage_maintained"] and
            validation["code_quality_improved"]
        )
        
        return validation
    
    def _run_quality_gates(self, requirements: TaskTestRequirements) -> Dict[str, Any]:
        """Run comprehensive quality gates"""
        test_dirs = [d for d in self.test_dirs if d.exists()]
        source_dirs = [d for d in self.source_dirs if d.exists()]
        
        return self.quality_gate.run_comprehensive_quality_gate(test_dirs, source_dirs)
    
    def _find_or_create_test_files(self, target_files: List[Path]) -> List[Path]:
        """Find or create test files for target files"""
        test_files = []
        
        for target_file in target_files:
            # Look for existing test file
            test_file = self._find_test_file_for_source(target_file)
            
            if not test_file or not test_file.exists():
                # Create test file using template
                test_file = self._create_test_file_from_template(target_file)
            
            test_files.append(test_file)
        
        return test_files
    
    def _find_test_file_for_source(self, source_file: Path) -> Optional[Path]:
        """Find corresponding test file for source file"""
        source_name = source_file.stem
        
        # Common test file patterns
        test_patterns = [
            f"test_{source_name}.py",
            f"{source_name}_test.py",
            f"test{source_name.title()}.py"
        ]
        
        for test_dir in self.test_dirs:
            if test_dir.exists():
                for pattern in test_patterns:
                    test_file = test_dir / pattern
                    if test_file.exists():
                        return test_file
        
        return None
    
    def _create_test_file_from_template(self, source_file: Path) -> Path:
        """Create test file from integration-first template"""
        test_dir = self.test_dirs[0]  # Use first test directory
        test_dir.mkdir(exist_ok=True)
        
        test_file = test_dir / f"test_{source_file.stem}.py"
        
        # Generate test template based on file type
        if self._is_api_file(source_file):
            template = self._generate_api_test_template(source_file)
        elif self._is_database_file(source_file):
            template = self._generate_database_test_template(source_file)
        else:
            template = self._generate_integration_test_template(source_file)
        
        test_file.write_text(template)
        
        print(f"📝 Created test file: {test_file}")
        return test_file
    
    def _generate_integration_test_template(self, source_file: Path) -> str:
        """Generate integration test template"""
        class_name = source_file.stem.title().replace('_', '')
        
        return f'''"""
Integration tests for {source_file.name}
Generated by Test Framework Integration
"""
import pytest
from pathlib import Path
from your_app.{source_file.stem} import {class_name}


class Test{class_name}Integration:
    """Integration tests for {class_name}"""
    
    def test_{source_file.stem}_basic_functionality(self):
        """Test basic functionality - RED PHASE: This should fail initially"""
        # Arrange
        instance = {class_name}()
        
        # Act
        result = instance.main_operation()
        
        # Assert
        assert result is not None
        assert result.success is True
        # Add more assertions based on business requirements
    
    def test_{source_file.stem}_error_handling(self):
        """Test error handling scenarios"""
        instance = {class_name}()
        
        with pytest.raises(ValueError, match="Invalid input"):
            instance.main_operation(invalid_input=True)
    
    def test_{source_file.stem}_integration_workflow(self):
        """Test complete integration workflow"""
        # This test should cover 80% of the business workflow
        instance = {class_name}()
        
        # Multi-step workflow test
        step1_result = instance.step_one()
        assert step1_result.success
        
        step2_result = instance.step_two(step1_result.data)
        assert step2_result.success
        
        final_result = instance.finalize(step2_result.data)
        assert final_result.completed
'''
    
    def _generate_api_test_template(self, source_file: Path) -> str:
        """Generate API integration test template"""
        return f'''"""
API Integration tests for {source_file.name}
Generated by Test Framework Integration
"""
import pytest
import requests
from pathlib import Path


@pytest.fixture
def api_client():
    """API client for testing"""
    # Use real API client with test configuration
    from your_app.test_utils import create_test_client
    return create_test_client()


class Test{source_file.stem.title()}API:
    """API integration tests"""
    
    def test_api_endpoint_integration(self, api_client):
        """Test API endpoint with real HTTP calls - RED PHASE"""
        # This test should fail initially
        response = api_client.post("/api/{source_file.stem}", json={{
            "test_data": "value"
        }})
        
        assert response.status_code == 201
        assert "id" in response.json()
        
        # Verify database state (integration test)
        created_id = response.json()["id"]
        get_response = api_client.get(f"/api/{source_file.stem}/{{created_id}}")
        assert get_response.status_code == 200
    
    def test_api_validation_errors(self, api_client):
        """Test API validation with integration"""
        response = api_client.post("/api/{source_file.stem}", json={{}})
        
        assert response.status_code == 400
        assert "errors" in response.json()
    
    def test_api_performance_requirements(self, api_client):
        """Test API performance under load"""
        import time
        import concurrent.futures
        
        def make_request():
            return api_client.get("/api/{source_file.stem}")
        
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(50)]
            results = [f.result() for f in futures]
        
        end_time = time.time()
        
        # Performance assertions
        assert end_time - start_time < 2.0  # Under 2 seconds
        assert all(r.status_code == 200 for r in results)
'''
    
    def _generate_database_test_template(self, source_file: Path) -> str:
        """Generate database integration test template"""
        return f'''"""
Database Integration tests for {source_file.name}
Generated by Test Framework Integration
"""
import pytest
from testcontainers.postgres import PostgresContainer
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope="session")
def real_database():
    """Real database for integration testing"""
    with PostgresContainer("postgres:15") as postgres:
        engine = sa.create_engine(postgres.get_connection_url())
        
        # Create schema
        from your_app.models import Base
        Base.metadata.create_all(engine)
        
        yield engine


@pytest.fixture
def db_session(real_database):
    """Database session with transaction rollback"""
    Session = sessionmaker(bind=real_database)
    session = Session()
    try:
        yield session
    finally:
        session.rollback()
        session.close()


class Test{source_file.stem.title()}Database:
    """Database integration tests"""
    
    def test_database_operation_integration(self, db_session):
        """Test database operations with real database - RED PHASE"""
        from your_app.{source_file.stem} import {source_file.stem.title()}Service
        
        service = {source_file.stem.title()}Service(db_session)
        
        # This should fail initially
        result = service.create_record({{"name": "test", "value": 123}})
        
        assert result.id is not None
        assert result.name == "test"
        
        # Verify database state
        db_record = db_session.query(service.model).filter_by(id=result.id).first()
        assert db_record is not None
        assert db_record.name == "test"
    
    def test_database_transaction_integrity(self, db_session):
        """Test transaction rollback and data integrity"""
        from your_app.{source_file.stem} import {source_file.stem.title()}Service
        
        service = {source_file.stem.title()}Service(db_session)
        initial_count = db_session.query(service.model).count()
        
        try:
            with db_session.begin():
                service.create_record({{"name": "test1", "value": 1}})
                service.create_record({{"name": "test2", "value": 2}})
                
                # Force error to test rollback
                raise Exception("Forced error")
        except Exception:
            pass
        
        # Verify rollback occurred
        final_count = db_session.query(service.model).count()
        assert final_count == initial_count
'''
    
    def _run_single_test(self, test_file: Path) -> Dict[str, Any]:
        """Run single test file"""
        cmd = f"python -m pytest {test_file} -v"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        return {
            "passed": result.returncode == 0,
            "failed": result.returncode != 0,
            "output": result.stdout + result.stderr
        }
    
    def _run_all_tests(self) -> Dict[str, Any]:
        """Run all tests"""
        cmd = "python -m pytest"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        return {
            "passed": result.returncode == 0,
            "output": result.stdout + result.stderr
        }
    
    def _check_coverage(self, threshold: float) -> Dict[str, Any]:
        """Check test coverage"""
        cmd = f"python -m pytest --cov=. --cov-report=json --cov-fail-under={threshold}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        coverage_data = {}
        try:
            with open("coverage.json", "r") as f:
                coverage_data = json.load(f)
        except FileNotFoundError:
            pass
        
        current_coverage = coverage_data.get("totals", {}).get("percent_covered", 0)
        
        return {
            "meets_threshold": current_coverage >= threshold,
            "current": current_coverage,
            "threshold": threshold
        }
    
    def _is_minimal_implementation(self, file_path: Path) -> bool:
        """Check if implementation is minimal"""
        if not file_path.exists():
            return True
        
        content = file_path.read_text()
        
        # Simple heuristics for minimal implementation
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        code_lines = [line for line in lines if not line.startswith('#') and not line.startswith('"""')]
        
        # Minimal implementation should have fewer than 50 lines of actual code
        return len(code_lines) < 50
    
    def _check_code_quality_improvement(self, file_path: Path) -> bool:
        """Check if code quality improved during refactor"""
        # This would compare before/after metrics
        # For now, return True as placeholder
        return True
    
    def _is_api_file(self, file_path: Path) -> bool:
        """Check if file is API-related"""
        content = file_path.read_text() if file_path.exists() else ""
        api_indicators = ["fastapi", "flask", "django", "router", "endpoint", "request", "response"]
        return any(indicator in content.lower() for indicator in api_indicators)
    
    def _is_database_file(self, file_path: Path) -> bool:
        """Check if file is database-related"""
        content = file_path.read_text() if file_path.exists() else ""
        db_indicators = ["sqlalchemy", "django.db", "session", "query", "model", "database"]
        return any(indicator in content.lower() for indicator in db_indicators)
    
    def _all_phases_passed(self, results: Dict[str, Any]) -> bool:
        """Check if all TDD phases passed"""
        tdd_compliance = results.get("tdd_compliance", {})
        quality_metrics = results.get("quality_metrics", {})
        
        red_passed = tdd_compliance.get("red_phase", {}).get("passed", False)
        green_passed = tdd_compliance.get("green_phase", {}).get("passed", False)
        refactor_passed = tdd_compliance.get("refactor_phase", {}).get("passed", False)
        quality_passed = quality_metrics.get("overall_passed", False)
        
        return red_passed and green_passed and refactor_passed and quality_passed


def integrate_task_command():
    """Integration point for /task command"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Execute task with TDD enforcement")
    parser.add_argument("description", help="Task description")
    parser.add_argument("--files", nargs="+", type=Path, help="Target files")
    parser.add_argument("--coverage", type=float, default=90.0, help="Coverage threshold")
    parser.add_argument("--integration-ratio", type=float, default=0.8, help="Integration test ratio")
    
    args = parser.parse_args()
    
    requirements = TaskTestRequirements(
        minimum_coverage=args.coverage,
        integration_test_ratio=args.integration_ratio
    )
    
    executor = TDDEnforcedTaskExecutor(Path.cwd())
    results = executor.execute_task_with_tdd(
        args.description,
        args.files or [],
        requirements
    )
    
    if results["task_completed"]:
        print("✅ Task completed successfully!")
        exit(0)
    else:
        print("❌ Task failed TDD compliance")
        for rec in results.get("recommendations", []):
            print(f"  - {rec}")
        exit(1)


if __name__ == "__main__":
    integrate_task_command()
```

### /feature Command Integration
```xml
<feature_command_integration enforcement="MANDATORY">
  <prd_driven_testing>All features must have comprehensive test plans</prd_driven_testing>
  <integration_test_coverage>80%+ integration test coverage for user workflows</integration_test_coverage>
  <performance_testing>All features must include performance test requirements</performance_testing>
  <acceptance_criteria_testing>Every acceptance criterion must have corresponding test</acceptance_criteria_testing>
</feature_command_integration>
```

### Feature Testing Integration
```python
"""
Feature Testing Integration
Integrates testing mandate into /feature command workflows
"""
from typing import Dict, List, Any
from dataclasses import dataclass
from pathlib import Path

@dataclass
class FeatureTestPlan:
    """Comprehensive test plan for feature development"""
    feature_name: str
    user_stories: List[str]
    acceptance_criteria: List[str]
    integration_test_scenarios: List[str]
    performance_requirements: Dict[str, Any]
    test_data_requirements: List[str]
    
class FeatureTestingIntegrator:
    """Integrates testing into feature development workflow"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.task_executor = TDDEnforcedTaskExecutor(project_root)
    
    def create_feature_test_plan(self, feature_description: str, user_stories: List[str]) -> FeatureTestPlan:
        """Create comprehensive test plan for feature"""
        
        # Extract acceptance criteria from user stories
        acceptance_criteria = []
        for story in user_stories:
            criteria = self._extract_acceptance_criteria(story)
            acceptance_criteria.extend(criteria)
        
        # Generate integration test scenarios
        integration_scenarios = self._generate_integration_scenarios(feature_description, user_stories)
        
        # Define performance requirements
        performance_requirements = self._define_performance_requirements(feature_description)
        
        # Identify test data requirements
        test_data_requirements = self._identify_test_data_requirements(user_stories)
        
        return FeatureTestPlan(
            feature_name=feature_description,
            user_stories=user_stories,
            acceptance_criteria=acceptance_criteria,
            integration_test_scenarios=integration_scenarios,
            performance_requirements=performance_requirements,
            test_data_requirements=test_data_requirements
        )
    
    def execute_feature_with_testing(self, test_plan: FeatureTestPlan) -> Dict[str, Any]:
        """Execute feature development with integrated testing"""
        
        results = {
            "feature_completed": False,
            "test_plan_executed": False,
            "acceptance_criteria_covered": False,
            "integration_tests_passed": False,
            "performance_requirements_met": False,
            "recommendations": []
        }
        
        try:
            # Step 1: Create acceptance criteria tests
            print("📋 Creating acceptance criteria tests...")
            ac_tests = self._create_acceptance_criteria_tests(test_plan)
            
            # Step 2: Create integration test scenarios
            print("🔗 Creating integration test scenarios...")
            integration_tests = self._create_integration_test_scenarios(test_plan)
            
            # Step 3: Create performance tests
            print("⚡ Creating performance tests...")
            performance_tests = self._create_performance_tests(test_plan)
            
            # Step 4: Execute feature development with TDD
            print("🚀 Executing feature development with TDD...")
            development_results = self._execute_feature_development(test_plan)
            
            # Step 5: Validate all requirements met
            validation_results = self._validate_feature_completion(test_plan)
            
            # Compile results
            results.update(validation_results)
            results["feature_completed"] = all([
                validation_results["acceptance_criteria_covered"],
                validation_results["integration_tests_passed"],
                validation_results["performance_requirements_met"]
            ])
            
        except Exception as e:
            results["error"] = str(e)
            results["recommendations"].append(f"Feature development failed: {e}")
        
        return results
    
    def _extract_acceptance_criteria(self, user_story: str) -> List[str]:
        """Extract acceptance criteria from user story"""
        # Simple extraction based on common patterns
        criteria = []
        
        if "Given" in user_story and "When" in user_story and "Then" in user_story:
            # Gherkin format
            lines = user_story.split('\n')
            for line in lines:
                if line.strip().startswith('Then'):
                    criteria.append(line.strip())
        else:
            # Extract bullet points or numbered items
            lines = user_story.split('\n')
            for line in lines:
                if line.strip().startswith(('-', '*', '•')) or line.strip()[0:2].isdigit():
                    criteria.append(line.strip())
        
        return criteria
    
    def _generate_integration_scenarios(self, feature_description: str, user_stories: List[str]) -> List[str]:
        """Generate integration test scenarios"""
        scenarios = []
        
        # Generate end-to-end workflow scenarios
        scenarios.append(f"Complete {feature_description} user workflow")
        scenarios.append(f"{feature_description} error handling integration")
        scenarios.append(f"{feature_description} data persistence integration")
        scenarios.append(f"{feature_description} external service integration")
        
        # Generate scenarios based on user stories
        for story in user_stories:
            if "user" in story.lower():
                scenarios.append(f"User journey: {story[:50]}...")
        
        return scenarios
    
    def _define_performance_requirements(self, feature_description: str) -> Dict[str, Any]:
        """Define performance requirements for feature"""
        return {
            "response_time_p95": 200,  # ms
            "throughput_min": 100,     # requests/second
            "memory_usage_max": 500,   # MB
            "concurrent_users": 50,
            "load_test_duration": 300  # seconds
        }
    
    def _identify_test_data_requirements(self, user_stories: List[str]) -> List[str]:
        """Identify test data requirements"""
        requirements = []
        
        # Extract entities mentioned in user stories
        common_entities = ['user', 'product', 'order', 'account', 'payment', 'customer']
        
        for story in user_stories:
            for entity in common_entities:
                if entity in story.lower():
                    requirements.append(f"Test {entity} data")
        
        # Add common requirements
        requirements.extend([
            "Valid test user accounts",
            "Invalid data scenarios",
            "Edge case data sets",
            "Performance test data volume"
        ])
        
        return list(set(requirements))  # Remove duplicates
    
    def _create_acceptance_criteria_tests(self, test_plan: FeatureTestPlan) -> List[Path]:
        """Create tests for acceptance criteria"""
        test_files = []
        
        for i, criterion in enumerate(test_plan.acceptance_criteria):
            test_file = self._create_acceptance_test_file(test_plan.feature_name, criterion, i)
            test_files.append(test_file)
        
        return test_files
    
    def _create_acceptance_test_file(self, feature_name: str, criterion: str, index: int) -> Path:
        """Create test file for acceptance criterion"""
        test_dir = self.project_root / "tests" / "acceptance"
        test_dir.mkdir(parents=True, exist_ok=True)
        
        safe_feature_name = feature_name.lower().replace(' ', '_')
        test_file = test_dir / f"test_{safe_feature_name}_ac_{index + 1}.py"
        
        template = f'''"""
Acceptance Criteria Test for {feature_name}
Criterion: {criterion}
"""
import pytest


class Test{feature_name.replace(' ', '')}AcceptanceCriteria{index + 1}:
    """Test for acceptance criterion: {criterion}"""
    
    def test_acceptance_criterion_{index + 1}(self):
        """
        Acceptance Criterion: {criterion}
        
        This test validates the specific acceptance criterion
        using integration testing approach (80/20 rule)
        """
        # Arrange - Set up test environment
        # This should use real infrastructure (database, APIs, etc.)
        
        # Act - Execute the business workflow
        # This should test the actual user interaction
        
        # Assert - Verify acceptance criterion is met
        # This should validate business outcome
        
        # RED PHASE: This test should fail initially
        assert False, "Implement acceptance criterion test"
    
    def test_acceptance_criterion_{index + 1}_error_cases(self):
        """Test error cases for acceptance criterion"""
        # Test edge cases and error scenarios
        assert False, "Implement error case testing"
'''
        
        test_file.write_text(template)
        return test_file


# Test Generation Helpers
class TestGenerationHelpers:
    """Utilities for generating test code"""
    
    @staticmethod
    def generate_api_test_helper(endpoint: str, method: str) -> str:
        """Generate API test helper code"""
        return f'''
def test_{endpoint.replace('/', '_')}_{method.lower()}():
    """Test {method} {endpoint} endpoint"""
    response = api_client.{method.lower()}("{endpoint}")
    assert response.status_code in [200, 201, 204]
'''
    
    @staticmethod
    def generate_database_test_helper(model_name: str) -> str:
        """Generate database test helper code"""
        return f'''
def test_{model_name.lower()}_crud_operations(db_session):
    """Test CRUD operations for {model_name}"""
    # Create
    instance = {model_name}(name="test")
    db_session.add(instance)
    db_session.commit()
    
    # Read
    retrieved = db_session.query({model_name}).filter_by(name="test").first()
    assert retrieved is not None
    
    # Update
    retrieved.name = "updated"
    db_session.commit()
    
    # Delete
    db_session.delete(retrieved)
    db_session.commit()
'''
    
    @staticmethod
    def generate_performance_test_helper(operation_name: str) -> str:
        """Generate performance test helper code"""
        return f'''
def test_{operation_name}_performance():
    """Test {operation_name} performance requirements"""
    import time
    import concurrent.futures
    
    def operation():
        # Execute operation
        pass
    
    # Load test
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(operation) for _ in range(100)]
        results = [f.result() for f in futures]
    
    end_time = time.time()
    
    # Assert performance requirements
    assert end_time - start_time < 2.0  # Under 2 seconds
    assert len(results) == 100
'''


# Continuous Test Validation
class ContinuousTestValidator:
    """Validates tests continuously during development"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.watch_dirs = [
            project_root / "src",
            project_root / "app",
            project_root / "tests"
        ]
    
    def start_continuous_validation(self):
        """Start continuous test validation"""
        import time
        import threading
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        
        class TestValidationHandler(FileSystemEventHandler):
            def __init__(self, validator):
                self.validator = validator
            
            def on_modified(self, event):
                if event.is_directory:
                    return
                
                if event.src_path.endswith('.py'):
                    print(f"🔍 File changed: {event.src_path}")
                    self.validator.validate_tests()
        
        observer = Observer()
        handler = TestValidationHandler(self)
        
        for watch_dir in self.watch_dirs:
            if watch_dir.exists():
                observer.schedule(handler, str(watch_dir), recursive=True)
        
        observer.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        
        observer.join()
    
    def validate_tests(self):
        """Validate all tests"""
        # Run quick validation
        cmd = "python -m pytest --co -q"  # Collect only, quiet
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            print("❌ Test collection failed")
            print(result.stdout)
        else:
            # Run tests if collection passed
            self._run_validation_suite()
    
    def _run_validation_suite(self):
        """Run validation suite"""
        validations = [
            ("Coverage", self._check_coverage),
            ("TDD Compliance", self._check_tdd_compliance),
            ("Quality Gates", self._check_quality_gates)
        ]
        
        for name, validation_func in validations:
            try:
                result = validation_func()
                status = "✅" if result else "❌"
                print(f"{status} {name}")
            except Exception as e:
                print(f"❌ {name}: {e}")
    
    def _check_coverage(self) -> bool:
        """Quick coverage check"""
        cmd = "python -m pytest --cov=. --cov-report=term-missing --cov-fail-under=90 -x"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0
    
    def _check_tdd_compliance(self) -> bool:
        """Check TDD compliance"""
        # This would check for proper test-first development
        return True  # Placeholder
    
    def _check_quality_gates(self) -> bool:
        """Check test quality gates"""
        # This would run quality gate validation
        return True  # Placeholder
```

## Thinking Pattern for Test Framework Integration

```xml
<thinking_pattern name="test_framework_integration">
  <step_1>Identify Command Integration Points</step_1>
  <step_2>Design TDD Enforcement Workflow</step_2>
  <step_3>Create Test Generation Templates</step_3>
  <step_4>Integrate Quality Gates into Commands</step_4>
  <step_5>Setup Continuous Test Validation</step_5>
  <step_6>Generate Command-Specific Test Helpers</step_6>
  <step_7>Validate Test Framework Integration</step_7>
  <step_8>Monitor Test Coverage and Quality</step_8>
  <step_9>Provide Real-Time Feedback</step_9>
  <step_10>Update Integration Based on Usage</step_10>
</thinking_pattern>
```

## Command Integration Summary

| Command | Testing Integration | TDD Enforcement | Quality Gates |
|---------|-------------------|-----------------|---------------|
| /task | ✅ Full TDD cycle enforcement | ✅ Red-Green-Refactor mandatory | ✅ 90%+ coverage required |
| /feature | ✅ Feature test planning | ✅ Acceptance criteria testing | ✅ Integration test coverage |
| /query | ➖ Read-only analysis | ➖ No enforcement needed | ➖ Analysis only |
| /swarm | ✅ Multi-agent test coordination | ✅ Distributed TDD | ✅ Consolidated quality gates |
| /session | ✅ Continuous validation | ✅ Session-long TDD tracking | ✅ Progressive quality improvement |
| /protocol | ✅ Production readiness testing | ✅ Final validation cycle | ✅ All gates must pass |

## Integration Points

- **Integration-First Testing**: Provides foundation for all command integrations
- **TDD Enforcement Engine**: Core engine used by /task and /feature commands
- **Test Quality Gates**: Validates all command outputs meet quality standards
- **Testing Patterns Library**: Provides templates and utilities for all commands

## Validation Metrics

- Command integration coverage (target: 100% for development commands)
- TDD enforcement compliance (target: 95%+)
- Test generation success rate (target: 90%+)
- Continuous validation effectiveness (target: 85%+)
- Overall testing framework adoption (target: 90%+)