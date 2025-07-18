"""
TDD Tests for Prompt Testing Sandbox
RED PHASE: Write failing tests first
"""

import pytest
import json
import tempfile
import time
from pathlib import Path
from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch, mock_open
from typing import Dict, List, Any, Optional

# Import the components we're testing
try:
    from components.prompt_sandbox import (
        PromptSandbox,
        SandboxEnvironment,
        PromptTest,
        ExecutionResult,
        SafetyValidator,
        ResourceMonitor,
        execute_prompt_safely,
        validate_prompt_safety,
        get_execution_limits
    )
except ImportError:
    # These don't exist yet - we'll create them
    PromptSandbox = None
    SandboxEnvironment = None
    PromptTest = None
    ExecutionResult = None
    SafetyValidator = None
    ResourceMonitor = None
    execute_prompt_safely = None
    validate_prompt_safety = None
    get_execution_limits = None


class TestSandboxEnvironment:
    """Test the SandboxEnvironment class"""
    
    def test_sandbox_environment_creation(self):
        """Test SandboxEnvironment can be created with proper configuration"""
        if SandboxEnvironment is None:
            pytest.skip("SandboxEnvironment not implemented yet")
        
        env_config = {
            'environment_id': 'test_env_1',
            'name': 'Test Environment',
            'description': 'Test sandbox environment',
            'max_execution_time': 30.0,
            'max_memory_mb': 512,
            'max_output_length': 10000,
            'allowed_modules': ['json', 'datetime', 'math'],
            'blocked_modules': ['subprocess', 'os', 'sys'],
            'safety_level': 'strict',
            'isolation_level': 'high',
            'metadata': {'created_by': 'test_user'}
        }
        
        env = SandboxEnvironment(**env_config)
        assert env.environment_id == 'test_env_1'
        assert env.name == 'Test Environment'
        assert env.description == 'Test sandbox environment'
        assert env.max_execution_time == 30.0
        assert env.max_memory_mb == 512
        assert env.max_output_length == 10000
        assert env.allowed_modules == ['json', 'datetime', 'math']
        assert env.blocked_modules == ['subprocess', 'os', 'sys']
        assert env.safety_level == 'strict'
        assert env.isolation_level == 'high'
        assert env.metadata == {'created_by': 'test_user'}
    
    def test_sandbox_environment_validation(self):
        """Test SandboxEnvironment validation"""
        if SandboxEnvironment is None:
            pytest.skip("SandboxEnvironment not implemented yet")
        
        # Test invalid execution time
        with pytest.raises(ValueError):
            SandboxEnvironment(
                environment_id="test_env",
                name="Test",
                description="Test environment",
                max_execution_time=-1.0  # Invalid negative time
            )
        
        # Test invalid memory limit
        with pytest.raises(ValueError):
            SandboxEnvironment(
                environment_id="test_env",
                name="Test",
                description="Test environment",
                max_memory_mb=0  # Invalid zero memory
            )
        
        # Test invalid safety level
        with pytest.raises(ValueError):
            SandboxEnvironment(
                environment_id="test_env",
                name="Test",
                description="Test environment",
                safety_level="invalid_level"  # Invalid safety level
            )
    
    def test_sandbox_environment_presets(self):
        """Test predefined sandbox environment presets"""
        if SandboxEnvironment is None:
            pytest.skip("SandboxEnvironment not implemented yet")
        
        # Test development preset
        dev_env = SandboxEnvironment.create_development_preset()
        assert dev_env.name == "Development"
        assert dev_env.safety_level == "moderate"
        assert dev_env.max_execution_time > 0
        assert dev_env.max_memory_mb > 0
        
        # Test production preset
        prod_env = SandboxEnvironment.create_production_preset()
        assert prod_env.name == "Production"
        assert prod_env.safety_level == "strict"
        assert prod_env.max_execution_time <= dev_env.max_execution_time
        assert prod_env.max_memory_mb <= dev_env.max_memory_mb
        
        # Test research preset
        research_env = SandboxEnvironment.create_research_preset()
        assert research_env.name == "Research"
        assert research_env.safety_level == "permissive"
        assert research_env.max_execution_time >= dev_env.max_execution_time
        assert research_env.max_memory_mb >= dev_env.max_memory_mb
    
    def test_sandbox_environment_serialization(self):
        """Test SandboxEnvironment serialization"""
        if SandboxEnvironment is None:
            pytest.skip("SandboxEnvironment not implemented yet")
        
        env = SandboxEnvironment(
            environment_id="serialize_test",
            name="Serialize Test",
            description="Test serialization",
            max_execution_time=15.0,
            max_memory_mb=256,
            allowed_modules=['json'],
            blocked_modules=['os']
        )
        
        # Test to_dict
        env_dict = env.to_dict()
        assert isinstance(env_dict, dict)
        assert env_dict['environment_id'] == 'serialize_test'
        assert env_dict['name'] == 'Serialize Test'
        assert env_dict['max_execution_time'] == 15.0
        assert env_dict['max_memory_mb'] == 256
        assert env_dict['allowed_modules'] == ['json']
        assert env_dict['blocked_modules'] == ['os']
        
        # Test from_dict
        recreated_env = SandboxEnvironment.from_dict(env_dict)
        assert recreated_env.environment_id == env.environment_id
        assert recreated_env.name == env.name
        assert recreated_env.max_execution_time == env.max_execution_time
        assert recreated_env.max_memory_mb == env.max_memory_mb
        assert recreated_env.allowed_modules == env.allowed_modules
        assert recreated_env.blocked_modules == env.blocked_modules


class TestPromptTest:
    """Test the PromptTest data class"""
    
    def test_prompt_test_creation(self):
        """Test PromptTest can be created with proper data"""
        if PromptTest is None:
            pytest.skip("PromptTest not implemented yet")
        
        test_data = {
            'test_id': 'test_123',
            'name': 'Code Analysis Test',
            'description': 'Test code analysis prompt',
            'prompt_content': 'Analyze this code: {code}',
            'test_inputs': [{'code': 'def hello(): pass'}],
            'expected_outputs': ['Function definition analysis'],
            'success_criteria': {'min_length': 50, 'keywords': ['function', 'definition']},
            'environment_id': 'dev_env',
            'timeout': 30.0,
            'max_retries': 3,
            'metadata': {'category': 'code_analysis', 'priority': 'high'}
        }
        
        test = PromptTest(**test_data)
        assert test.test_id == 'test_123'
        assert test.name == 'Code Analysis Test'
        assert test.description == 'Test code analysis prompt'
        assert test.prompt_content == 'Analyze this code: {code}'
        assert test.test_inputs == [{'code': 'def hello(): pass'}]
        assert test.expected_outputs == ['Function definition analysis']
        assert test.success_criteria == {'min_length': 50, 'keywords': ['function', 'definition']}
        assert test.environment_id == 'dev_env'
        assert test.timeout == 30.0
        assert test.max_retries == 3
        assert test.metadata == {'category': 'code_analysis', 'priority': 'high'}
    
    def test_prompt_test_validation(self):
        """Test PromptTest validation"""
        if PromptTest is None:
            pytest.skip("PromptTest not implemented yet")
        
        # Test empty test ID
        with pytest.raises(ValueError):
            PromptTest(
                test_id="",
                name="Test",
                description="Test description",
                prompt_content="Test prompt",
                test_inputs=[{'input': 'test'}]
            )
        
        # Test empty prompt content
        with pytest.raises(ValueError):
            PromptTest(
                test_id="test_123",
                name="Test",
                description="Test description",
                prompt_content="",
                test_inputs=[{'input': 'test'}]
            )
        
        # Test empty test inputs
        with pytest.raises(ValueError):
            PromptTest(
                test_id="test_123",
                name="Test",
                description="Test description",
                prompt_content="Test prompt",
                test_inputs=[]
            )
    
    def test_prompt_test_rendering(self):
        """Test prompt test rendering with variables"""
        if PromptTest is None:
            pytest.skip("PromptTest not implemented yet")
        
        test = PromptTest(
            test_id="render_test",
            name="Render Test",
            description="Test prompt rendering",
            prompt_content="Analyze this {content_type}: {content}",
            test_inputs=[{'content_type': 'code', 'content': 'def hello(): pass'}]
        )
        
        # Test rendering with first input
        rendered = test.render_prompt(test.test_inputs[0])
        expected = "Analyze this code: def hello(): pass"
        assert rendered == expected
        
        # Test rendering with custom input
        custom_input = {'content_type': 'text', 'content': 'Hello world'}
        rendered = test.render_prompt(custom_input)
        expected = "Analyze this text: Hello world"
        assert rendered == expected
    
    def test_prompt_test_success_criteria_evaluation(self):
        """Test success criteria evaluation"""
        if PromptTest is None:
            pytest.skip("PromptTest not implemented yet")
        
        test = PromptTest(
            test_id="criteria_test",
            name="Criteria Test",
            description="Test success criteria",
            prompt_content="Test prompt",
            test_inputs=[{'input': 'test'}],
            success_criteria={
                'min_length': 20,
                'max_length': 100,
                'keywords': ['analysis', 'function'],
                'forbidden_words': ['error', 'fail']
            }
        )
        
        # Test successful output
        success_output = "This is a comprehensive analysis of the function implementation."
        result = test.evaluate_success_criteria(success_output)
        assert result['success'] is True
        assert result['score'] > 0.8
        
        # Test failed output (too short)
        fail_output = "Short text"
        result = test.evaluate_success_criteria(fail_output)
        assert result['success'] is False
        assert result['score'] < 0.5
        
        # Test failed output (forbidden words)
        fail_output = "This analysis failed with an error in the function."
        result = test.evaluate_success_criteria(fail_output)
        assert result['success'] is False
        assert 'forbidden_words' in result['violations']


class TestExecutionResult:
    """Test the ExecutionResult data class"""
    
    def test_execution_result_creation(self):
        """Test ExecutionResult can be created with proper data"""
        if ExecutionResult is None:
            pytest.skip("ExecutionResult not implemented yet")
        
        result_data = {
            'result_id': 'result_123',
            'test_id': 'test_456',
            'environment_id': 'env_789',
            'timestamp': datetime.now().isoformat(),
            'execution_time': 2.5,
            'memory_used_mb': 64,
            'success': True,
            'output': 'Test output content',
            'error_message': None,
            'safety_violations': [],
            'resource_violations': [],
            'exit_code': 0,
            'metadata': {'execution_mode': 'safe', 'retries': 0}
        }
        
        result = ExecutionResult(**result_data)
        assert result.result_id == 'result_123'
        assert result.test_id == 'test_456'
        assert result.environment_id == 'env_789'
        assert result.execution_time == 2.5
        assert result.memory_used_mb == 64
        assert result.success is True
        assert result.output == 'Test output content'
        assert result.error_message is None
        assert result.safety_violations == []
        assert result.resource_violations == []
        assert result.exit_code == 0
        assert result.metadata == {'execution_mode': 'safe', 'retries': 0}
    
    def test_execution_result_validation(self):
        """Test ExecutionResult validation"""
        if ExecutionResult is None:
            pytest.skip("ExecutionResult not implemented yet")
        
        # Test negative execution time
        with pytest.raises(ValueError):
            ExecutionResult(
                result_id="result_123",
                test_id="test_456",
                environment_id="env_789",
                timestamp=datetime.now().isoformat(),
                execution_time=-1.0,  # Invalid negative time
                memory_used_mb=64,
                success=True,
                output="Test output"
            )
        
        # Test negative memory usage
        with pytest.raises(ValueError):
            ExecutionResult(
                result_id="result_123",
                test_id="test_456",
                environment_id="env_789",
                timestamp=datetime.now().isoformat(),
                execution_time=2.0,
                memory_used_mb=-32,  # Invalid negative memory
                success=True,
                output="Test output"
            )
    
    def test_execution_result_analysis(self):
        """Test execution result analysis methods"""
        if ExecutionResult is None:
            pytest.skip("ExecutionResult not implemented yet")
        
        result = ExecutionResult(
            result_id="analysis_test",
            test_id="test_456",
            environment_id="env_789",
            timestamp=datetime.now().isoformat(),
            execution_time=5.0,
            memory_used_mb=128,
            success=True,
            output="Test output with analysis results",
            safety_violations=[],
            resource_violations=['timeout_warning']
        )
        
        # Test performance score
        perf_score = result.get_performance_score()
        assert 0.0 <= perf_score <= 1.0
        
        # Test safety score
        safety_score = result.get_safety_score()
        assert 0.0 <= safety_score <= 1.0
        
        # Test overall score
        overall_score = result.get_overall_score()
        assert 0.0 <= overall_score <= 1.0
        
        # Test has violations
        assert result.has_violations() is True  # Due to resource violations
        
        # Test violation summary
        violations = result.get_violation_summary()
        assert isinstance(violations, dict)
        assert 'safety_violations' in violations
        assert 'resource_violations' in violations


class TestSafetyValidator:
    """Test the SafetyValidator class"""
    
    def test_safety_validator_creation(self):
        """Test SafetyValidator can be created"""
        if SafetyValidator is None:
            pytest.skip("SafetyValidator not implemented yet")
        
        validator = SafetyValidator(
            safety_level='strict',
            blocked_modules=['os', 'subprocess', 'sys'],
            blocked_functions=['exec', 'eval', 'open'],
            blocked_keywords=['import os', 'import subprocess'],
            max_code_length=10000
        )
        
        assert validator.safety_level == 'strict'
        assert validator.blocked_modules == ['os', 'subprocess', 'sys']
        assert validator.blocked_functions == ['exec', 'eval', 'open']
        assert validator.blocked_keywords == ['import os', 'import subprocess']
        assert validator.max_code_length == 10000
    
    def test_safety_validator_prompt_validation(self):
        """Test prompt safety validation"""
        if SafetyValidator is None:
            pytest.skip("SafetyValidator not implemented yet")
        
        validator = SafetyValidator(
            safety_level='strict',
            blocked_modules=['os', 'subprocess'],
            blocked_functions=['exec', 'eval'],
            blocked_keywords=['import os', 'import subprocess']
        )
        
        # Test safe prompt
        safe_prompt = "Please analyze this code: def hello(): return 'Hello World'"
        result = validator.validate_prompt(safe_prompt)
        assert result['is_safe'] is True
        assert len(result['violations']) == 0
        
        # Test unsafe prompt (blocked module)
        unsafe_prompt = "Please analyze this code: import os; os.system('ls')"
        result = validator.validate_prompt(unsafe_prompt)
        assert result['is_safe'] is False
        assert len(result['violations']) > 0
        assert any('blocked_module' in v['type'] for v in result['violations'])
        
        # Test unsafe prompt (blocked function)
        unsafe_prompt = "Please analyze this code: exec('print(hello)')"
        result = validator.validate_prompt(unsafe_prompt)
        assert result['is_safe'] is False
        assert len(result['violations']) > 0
        assert any('blocked_function' in v['type'] for v in result['violations'])
    
    def test_safety_validator_code_analysis(self):
        """Test code analysis for safety violations"""
        if SafetyValidator is None:
            pytest.skip("SafetyValidator not implemented yet")
        
        validator = SafetyValidator(safety_level='strict')
        
        # Test safe code
        safe_code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
        result = validator.analyze_code(safe_code)
        assert result['is_safe'] is True
        assert result['risk_level'] == 'low'
        
        # Test potentially unsafe code
        unsafe_code = """
import subprocess
result = subprocess.run(['ls', '-la'], capture_output=True)
"""
        result = validator.analyze_code(unsafe_code)
        assert result['is_safe'] is False
        assert result['risk_level'] in ['medium', 'high']
        assert len(result['violations']) > 0
    
    def test_safety_validator_presets(self):
        """Test predefined safety validator presets"""
        if SafetyValidator is None:
            pytest.skip("SafetyValidator not implemented yet")
        
        # Test strict preset
        strict_validator = SafetyValidator.create_strict_preset()
        assert strict_validator.safety_level == 'strict'
        assert len(strict_validator.blocked_modules) > 0
        assert len(strict_validator.blocked_functions) > 0
        
        # Test moderate preset
        moderate_validator = SafetyValidator.create_moderate_preset()
        assert moderate_validator.safety_level == 'moderate'
        assert len(moderate_validator.blocked_modules) < len(strict_validator.blocked_modules)
        
        # Test permissive preset
        permissive_validator = SafetyValidator.create_permissive_preset()
        assert permissive_validator.safety_level == 'permissive'
        assert len(permissive_validator.blocked_modules) < len(moderate_validator.blocked_modules)


class TestResourceMonitor:
    """Test the ResourceMonitor class"""
    
    def test_resource_monitor_creation(self):
        """Test ResourceMonitor can be created"""
        if ResourceMonitor is None:
            pytest.skip("ResourceMonitor not implemented yet")
        
        monitor = ResourceMonitor(
            max_execution_time=30.0,
            max_memory_mb=512,
            max_cpu_percent=80.0,
            max_output_length=10000,
            monitor_interval=1.0
        )
        
        assert monitor.max_execution_time == 30.0
        assert monitor.max_memory_mb == 512
        assert monitor.max_cpu_percent == 80.0
        assert monitor.max_output_length == 10000
        assert monitor.monitor_interval == 1.0
    
    def test_resource_monitor_execution_monitoring(self):
        """Test execution monitoring"""
        if ResourceMonitor is None:
            pytest.skip("ResourceMonitor not implemented yet")
        
        monitor = ResourceMonitor(
            max_execution_time=5.0,
            max_memory_mb=256,
            max_cpu_percent=90.0
        )
        
        # Test monitoring context
        with monitor.monitor_execution() as context:
            assert context is not None
            assert hasattr(context, 'start_time')
            assert hasattr(context, 'initial_memory')
            
            # Simulate some work
            time.sleep(0.1)
            
            # Check current usage
            current_usage = context.get_current_usage()
            assert 'execution_time' in current_usage
            assert 'memory_mb' in current_usage
            assert 'cpu_percent' in current_usage
            assert current_usage['execution_time'] > 0
    
    def test_resource_monitor_violation_detection(self):
        """Test resource violation detection"""
        if ResourceMonitor is None:
            pytest.skip("ResourceMonitor not implemented yet")
        
        monitor = ResourceMonitor(
            max_execution_time=0.1,  # Very short timeout
            max_memory_mb=32,  # Very low memory limit
            max_cpu_percent=10.0  # Very low CPU limit
        )
        
        # Test timeout violation
        with pytest.raises(TimeoutError):
            with monitor.monitor_execution():
                time.sleep(0.2)  # Exceed timeout
        
        # Test memory violation detection
        violations = monitor.check_violations({
            'execution_time': 0.05,
            'memory_mb': 64,  # Exceed memory limit
            'cpu_percent': 5.0
        })
        
        assert len(violations) > 0
        assert any('memory' in v['type'] for v in violations)
    
    def test_resource_monitor_reporting(self):
        """Test resource usage reporting"""
        if ResourceMonitor is None:
            pytest.skip("ResourceMonitor not implemented yet")
        
        monitor = ResourceMonitor(
            max_execution_time=10.0,
            max_memory_mb=512
        )
        
        # Test usage report generation
        usage_data = {
            'execution_time': 2.5,
            'memory_mb': 128,
            'cpu_percent': 45.0,
            'output_length': 1500
        }
        
        report = monitor.generate_usage_report(usage_data)
        
        assert isinstance(report, dict)
        assert 'summary' in report
        assert 'details' in report
        assert 'violations' in report
        assert 'efficiency_score' in report
        
        # Test efficiency score calculation
        efficiency = monitor.calculate_efficiency_score(usage_data)
        assert 0.0 <= efficiency <= 1.0


class TestPromptSandbox:
    """Test the PromptSandbox component"""
    
    @pytest.fixture
    def temp_storage(self):
        """Create temporary storage directory"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            yield Path(tmp_dir)
    
    @pytest.fixture
    def mock_streamlit(self):
        """Mock Streamlit session state"""
        with patch('streamlit.session_state') as mock_session:
            mock_session.keys.return_value = ["test_key"]
            mock_session.__contains__ = MagicMock(return_value=False)
            mock_session.__setitem__ = MagicMock()
            mock_session.__getitem__ = MagicMock(return_value="test_value")
            mock_session.sandbox_state = {
                'active_tests': {},
                'execution_history': [],
                'selected_environment': 'development'
            }
            yield mock_session
    
    def test_prompt_sandbox_initialization(self, temp_storage, mock_streamlit):
        """Test PromptSandbox can be initialized"""
        if PromptSandbox is None:
            pytest.skip("PromptSandbox not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        assert sandbox.storage_path == temp_storage
        assert hasattr(sandbox, 'environments')
        assert hasattr(sandbox, 'active_tests')
        assert hasattr(sandbox, 'execution_history')
        assert hasattr(sandbox, 'safety_validator')
        assert hasattr(sandbox, 'resource_monitor')
        assert isinstance(sandbox.environments, dict)
        assert isinstance(sandbox.active_tests, dict)
        assert isinstance(sandbox.execution_history, list)
    
    def test_create_sandbox_environment(self, temp_storage, mock_streamlit):
        """Test creating sandbox environments"""
        if PromptSandbox is None or SandboxEnvironment is None:
            pytest.skip("PromptSandbox or SandboxEnvironment not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Create custom environment
        env_config = {
            'name': 'Custom Test Environment',
            'description': 'Custom environment for testing',
            'max_execution_time': 15.0,
            'max_memory_mb': 256,
            'safety_level': 'moderate'
        }
        
        env_id = sandbox.create_environment(env_config)
        
        assert env_id is not None
        assert env_id in sandbox.environments
        
        created_env = sandbox.environments[env_id]
        assert created_env.name == 'Custom Test Environment'
        assert created_env.description == 'Custom environment for testing'
        assert created_env.max_execution_time == 15.0
        assert created_env.max_memory_mb == 256
        assert created_env.safety_level == 'moderate'
    
    def test_create_prompt_test(self, temp_storage, mock_streamlit):
        """Test creating prompt tests"""
        if PromptSandbox is None or PromptTest is None:
            pytest.skip("PromptSandbox or PromptTest not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Create test
        test_config = {
            'name': 'Code Analysis Test',
            'description': 'Test code analysis prompt',
            'prompt_content': 'Analyze this code: {code}',
            'test_inputs': [
                {'code': 'def hello(): return "Hello World"'},
                {'code': 'class Calculator: def add(self, a, b): return a + b'}
            ],
            'expected_outputs': ['Function analysis', 'Class analysis'],
            'environment_id': 'development',
            'timeout': 30.0
        }
        
        test_id = sandbox.create_test(test_config)
        
        assert test_id is not None
        assert test_id in sandbox.active_tests
        
        created_test = sandbox.active_tests[test_id]
        assert created_test.name == 'Code Analysis Test'
        assert created_test.description == 'Test code analysis prompt'
        assert created_test.prompt_content == 'Analyze this code: {code}'
        assert len(created_test.test_inputs) == 2
        assert created_test.timeout == 30.0
    
    def test_execute_prompt_test(self, temp_storage, mock_streamlit):
        """Test executing prompt tests"""
        if PromptSandbox is None or PromptTest is None:
            pytest.skip("PromptSandbox or PromptTest not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Create test
        test_config = {
            'name': 'Simple Test',
            'description': 'Simple test execution',
            'prompt_content': 'Echo: {message}',
            'test_inputs': [{'message': 'Hello World'}],
            'environment_id': 'development'
        }
        
        test_id = sandbox.create_test(test_config)
        
        # Execute test
        results = sandbox.execute_test(test_id)
        
        assert isinstance(results, list)
        assert len(results) > 0
        
        # Check result structure
        for result in results:
            assert hasattr(result, 'result_id')
            assert hasattr(result, 'test_id')
            assert hasattr(result, 'success')
            assert hasattr(result, 'output')
            assert hasattr(result, 'execution_time')
            assert hasattr(result, 'memory_used_mb')
            assert result.test_id == test_id
    
    def test_execute_single_prompt(self, temp_storage, mock_streamlit):
        """Test executing single prompts"""
        if PromptSandbox is None:
            pytest.skip("PromptSandbox not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Execute single prompt
        prompt = "Please analyze this simple function: def add(a, b): return a + b"
        environment_id = "development"
        
        result = sandbox.execute_single_prompt(prompt, environment_id)
        
        assert hasattr(result, 'result_id')
        assert hasattr(result, 'success')
        assert hasattr(result, 'output')
        assert hasattr(result, 'execution_time')
        assert hasattr(result, 'memory_used_mb')
        assert hasattr(result, 'safety_violations')
        assert hasattr(result, 'resource_violations')
        assert result.execution_time > 0
        assert result.memory_used_mb > 0
    
    def test_sandbox_safety_enforcement(self, temp_storage, mock_streamlit):
        """Test safety enforcement in sandbox"""
        if PromptSandbox is None:
            pytest.skip("PromptSandbox not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Test unsafe prompt
        unsafe_prompt = "Please run this code: import os; os.system('rm -rf /')"
        environment_id = "development"
        
        result = sandbox.execute_single_prompt(unsafe_prompt, environment_id)
        
        # Should detect safety violations
        assert len(result.safety_violations) > 0
        assert result.success is False
        assert "safety violation" in result.error_message.lower()
    
    def test_sandbox_resource_monitoring(self, temp_storage, mock_streamlit):
        """Test resource monitoring in sandbox"""
        if PromptSandbox is None:
            pytest.skip("PromptSandbox not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Test long-running prompt (should timeout)
        long_prompt = "Please analyze this code that runs for a long time: import time; time.sleep(100)"
        environment_id = "development"
        
        result = sandbox.execute_single_prompt(long_prompt, environment_id)
        
        # Should detect timeout violations
        assert len(result.resource_violations) > 0 or result.success is False
        if not result.success:
            assert "timeout" in result.error_message.lower() or "time" in result.error_message.lower()
    
    def test_execution_history_tracking(self, temp_storage, mock_streamlit):
        """Test execution history tracking"""
        if PromptSandbox is None:
            pytest.skip("PromptSandbox not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Execute multiple prompts
        prompts = [
            "Analyze: def hello(): pass",
            "Analyze: class Test: pass",
            "Analyze: for i in range(10): print(i)"
        ]
        
        for prompt in prompts:
            sandbox.execute_single_prompt(prompt, "development")
        
        # Check history
        history = sandbox.get_execution_history()
        assert len(history) >= len(prompts)
        
        # Check history structure
        for entry in history:
            assert 'timestamp' in entry
            assert 'prompt' in entry
            assert 'result' in entry
            assert 'environment_id' in entry
    
    def test_sandbox_statistics(self, temp_storage, mock_streamlit):
        """Test sandbox statistics and reporting"""
        if PromptSandbox is None:
            pytest.skip("PromptSandbox not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Execute some tests
        for i in range(5):
            sandbox.execute_single_prompt(f"Test prompt {i}", "development")
        
        # Get statistics
        stats = sandbox.get_statistics()
        
        assert isinstance(stats, dict)
        assert 'total_executions' in stats
        assert 'successful_executions' in stats
        assert 'failed_executions' in stats
        assert 'average_execution_time' in stats
        assert 'average_memory_usage' in stats
        assert 'safety_violations_count' in stats
        assert 'resource_violations_count' in stats
        
        assert stats['total_executions'] >= 5
        assert stats['successful_executions'] >= 0
        assert stats['failed_executions'] >= 0
        assert stats['average_execution_time'] > 0
        assert stats['average_memory_usage'] > 0
    
    @patch('streamlit.title')
    @patch('streamlit.subheader')
    @patch('streamlit.tabs')
    def test_render_sandbox_interface(self, mock_tabs, mock_subheader, mock_title, temp_storage, mock_streamlit):
        """Test rendering sandbox interface"""
        if PromptSandbox is None:
            pytest.skip("PromptSandbox not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Mock tabs
        mock_tabs.return_value = [MagicMock(), MagicMock(), MagicMock(), MagicMock()]
        
        # Test that method exists and can be called
        assert hasattr(sandbox, 'render_sandbox_interface')
        
        # Call method (should not raise exceptions)
        try:
            sandbox.render_sandbox_interface()
            # If we get here, the method executed without errors
            assert True
        except AttributeError:
            # Method might not exist yet
            pytest.skip("render_sandbox_interface not implemented yet")


class TestGlobalFunctions:
    """Test global convenience functions"""
    
    def test_execute_prompt_safely_function(self):
        """Test execute_prompt_safely global function"""
        if execute_prompt_safely is None:
            pytest.skip("execute_prompt_safely not implemented yet")
        
        # Test safe execution
        prompt = "Please analyze this code: def hello(): return 'Hello'"
        environment_config = {
            'max_execution_time': 10.0,
            'max_memory_mb': 128,
            'safety_level': 'moderate'
        }
        
        result = execute_prompt_safely(prompt, environment_config)
        
        assert hasattr(result, 'success')
        assert hasattr(result, 'output')
        assert hasattr(result, 'execution_time')
        assert hasattr(result, 'safety_violations')
        assert hasattr(result, 'resource_violations')
        assert result.execution_time > 0
    
    def test_validate_prompt_safety_function(self):
        """Test validate_prompt_safety global function"""
        if validate_prompt_safety is None:
            pytest.skip("validate_prompt_safety not implemented yet")
        
        # Test safe prompt
        safe_prompt = "Please analyze this code: def add(a, b): return a + b"
        result = validate_prompt_safety(safe_prompt)
        
        assert isinstance(result, dict)
        assert 'is_safe' in result
        assert 'violations' in result
        assert 'risk_level' in result
        assert result['is_safe'] is True
        assert len(result['violations']) == 0
        
        # Test unsafe prompt
        unsafe_prompt = "Please run this: import os; os.system('dangerous command')"
        result = validate_prompt_safety(unsafe_prompt)
        
        assert result['is_safe'] is False
        assert len(result['violations']) > 0
    
    def test_get_execution_limits_function(self):
        """Test get_execution_limits global function"""
        if get_execution_limits is None:
            pytest.skip("get_execution_limits not implemented yet")
        
        # Test development limits
        dev_limits = get_execution_limits('development')
        assert isinstance(dev_limits, dict)
        assert 'max_execution_time' in dev_limits
        assert 'max_memory_mb' in dev_limits
        assert 'max_cpu_percent' in dev_limits
        assert 'max_output_length' in dev_limits
        
        # Test production limits
        prod_limits = get_execution_limits('production')
        assert isinstance(prod_limits, dict)
        assert prod_limits['max_execution_time'] <= dev_limits['max_execution_time']
        assert prod_limits['max_memory_mb'] <= dev_limits['max_memory_mb']
        
        # Test research limits
        research_limits = get_execution_limits('research')
        assert isinstance(research_limits, dict)
        assert research_limits['max_execution_time'] >= dev_limits['max_execution_time']
        assert research_limits['max_memory_mb'] >= dev_limits['max_memory_mb']
    
    def test_sandbox_error_handling(self, temp_storage):
        """Test error handling in sandbox system"""
        if PromptSandbox is None:
            pytest.skip("PromptSandbox not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Test with invalid environment
        result = sandbox.execute_single_prompt("Test prompt", "invalid_environment")
        assert result.success is False
        assert "environment" in result.error_message.lower()
        
        # Test with empty prompt
        result = sandbox.execute_single_prompt("", "development")
        assert result.success is False
        assert "prompt" in result.error_message.lower()
    
    def test_sandbox_performance(self, temp_storage):
        """Test sandbox performance with multiple executions"""
        if PromptSandbox is None:
            pytest.skip("PromptSandbox not implemented yet")
        
        sandbox = PromptSandbox(storage_path=temp_storage)
        
        # Execute multiple prompts
        start_time = time.time()
        
        for i in range(20):
            sandbox.execute_single_prompt(f"Test prompt {i}", "development")
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # Should handle 20 executions in reasonable time (less than 30 seconds)
        assert total_time < 30.0
        
        # Check that history is maintained
        history = sandbox.get_execution_history()
        assert len(history) >= 20
        
        # Check statistics
        stats = sandbox.get_statistics()
        assert stats['total_executions'] >= 20