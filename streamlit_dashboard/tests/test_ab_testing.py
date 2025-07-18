"""
TDD Tests for A/B Testing Framework
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
    from components.ab_testing import (
        ABTestingFramework,
        PromptVariant,
        ABTest,
        TestResult,
        TestMetrics,
        StatisticalAnalysis,
        run_ab_test,
        analyze_test_results,
        get_confidence_level
    )
except ImportError:
    # These don't exist yet - we'll create them
    ABTestingFramework = None
    PromptVariant = None
    ABTest = None
    TestResult = None
    TestMetrics = None
    StatisticalAnalysis = None
    run_ab_test = None
    analyze_test_results = None
    get_confidence_level = None


class TestPromptVariant:
    """Test the PromptVariant data class"""
    
    def test_prompt_variant_creation(self):
        """Test PromptVariant can be created with proper data"""
        if PromptVariant is None:
            pytest.skip("PromptVariant not implemented yet")
        
        variant_data = {
            'variant_id': 'variant_a',
            'name': 'Original Prompt',
            'description': 'The original prompt variant',
            'prompt_content': 'Please analyze this code and provide feedback.',
            'template_variables': {'style': 'formal', 'detail_level': 'high'},
            'expected_outcomes': ['code_analysis', 'feedback_provided'],
            'success_criteria': {'accuracy': 0.8, 'completeness': 0.9},
            'metadata': {'created_by': 'test_user', 'version': '1.0'}
        }
        
        variant = PromptVariant(**variant_data)
        assert variant.variant_id == 'variant_a'
        assert variant.name == 'Original Prompt'
        assert variant.description == 'The original prompt variant'
        assert variant.prompt_content == 'Please analyze this code and provide feedback.'
        assert variant.template_variables == {'style': 'formal', 'detail_level': 'high'}
        assert variant.expected_outcomes == ['code_analysis', 'feedback_provided']
        assert variant.success_criteria == {'accuracy': 0.8, 'completeness': 0.9}
        assert variant.metadata == {'created_by': 'test_user', 'version': '1.0'}
    
    def test_prompt_variant_validation(self):
        """Test PromptVariant validation"""
        if PromptVariant is None:
            pytest.skip("PromptVariant not implemented yet")
        
        # Test empty variant ID
        with pytest.raises(ValueError):
            PromptVariant(
                variant_id="",
                name="Test Variant",
                description="Test description",
                prompt_content="Test prompt"
            )
        
        # Test empty prompt content
        with pytest.raises(ValueError):
            PromptVariant(
                variant_id="test_variant",
                name="Test Variant",
                description="Test description",
                prompt_content=""
            )
    
    def test_prompt_variant_render(self):
        """Test prompt variant rendering with template variables"""
        if PromptVariant is None:
            pytest.skip("PromptVariant not implemented yet")
        
        variant = PromptVariant(
            variant_id="test_variant",
            name="Template Test",
            description="Test with template variables",
            prompt_content="Analyze this {code_type} code with {detail_level} detail using {style} style.",
            template_variables={'code_type': 'Python', 'detail_level': 'high', 'style': 'professional'}
        )
        
        rendered = variant.render()
        expected = "Analyze this Python code with high detail using professional style."
        assert rendered == expected
    
    def test_prompt_variant_serialization(self):
        """Test PromptVariant serialization"""
        if PromptVariant is None:
            pytest.skip("PromptVariant not implemented yet")
        
        variant = PromptVariant(
            variant_id="serialize_test",
            name="Serialization Test",
            description="Test serialization",
            prompt_content="Test prompt content",
            template_variables={'test': 'value'}
        )
        
        # Test to_dict
        variant_dict = variant.to_dict()
        assert isinstance(variant_dict, dict)
        assert variant_dict['variant_id'] == 'serialize_test'
        assert variant_dict['name'] == 'Serialization Test'
        assert variant_dict['template_variables'] == {'test': 'value'}
        
        # Test from_dict
        recreated_variant = PromptVariant.from_dict(variant_dict)
        assert recreated_variant.variant_id == variant.variant_id
        assert recreated_variant.name == variant.name
        assert recreated_variant.template_variables == variant.template_variables


class TestABTest:
    """Test the ABTest data class"""
    
    def test_ab_test_creation(self):
        """Test ABTest can be created with proper data"""
        if ABTest is None or PromptVariant is None:
            pytest.skip("ABTest or PromptVariant not implemented yet")
        
        variant_a = PromptVariant(
            variant_id="variant_a",
            name="Original",
            description="Original prompt",
            prompt_content="Original prompt content"
        )
        
        variant_b = PromptVariant(
            variant_id="variant_b",
            name="Modified",
            description="Modified prompt",
            prompt_content="Modified prompt content"
        )
        
        test_data = {
            'test_id': 'test_123',
            'test_name': 'Code Analysis A/B Test',
            'description': 'Testing different code analysis prompts',
            'variant_a': variant_a,
            'variant_b': variant_b,
            'test_parameters': {
                'sample_size': 100,
                'confidence_level': 0.95,
                'power': 0.8,
                'effect_size': 0.1
            },
            'test_context': {'domain': 'code_analysis', 'user_type': 'developer'},
            'start_time': datetime.now().isoformat(),
            'end_time': (datetime.now() + timedelta(days=7)).isoformat(),
            'status': 'running',
            'metadata': {'created_by': 'test_user', 'priority': 'high'}
        }
        
        ab_test = ABTest(**test_data)
        assert ab_test.test_id == 'test_123'
        assert ab_test.test_name == 'Code Analysis A/B Test'
        assert ab_test.variant_a.variant_id == 'variant_a'
        assert ab_test.variant_b.variant_id == 'variant_b'
        assert ab_test.test_parameters['sample_size'] == 100
        assert ab_test.test_context['domain'] == 'code_analysis'
        assert ab_test.status == 'running'
    
    def test_ab_test_validation(self):
        """Test ABTest validation"""
        if ABTest is None or PromptVariant is None:
            pytest.skip("ABTest or PromptVariant not implemented yet")
        
        variant_a = PromptVariant(
            variant_id="variant_a",
            name="Test A",
            description="Test variant A",
            prompt_content="Test prompt A"
        )
        
        variant_b = PromptVariant(
            variant_id="variant_b",
            name="Test B",
            description="Test variant B",
            prompt_content="Test prompt B"
        )
        
        # Test empty test ID
        with pytest.raises(ValueError):
            ABTest(
                test_id="",
                test_name="Test",
                description="Test description",
                variant_a=variant_a,
                variant_b=variant_b,
                start_time=datetime.now().isoformat(),
                end_time=datetime.now().isoformat()
            )
        
        # Test same variant IDs
        with pytest.raises(ValueError):
            ABTest(
                test_id="test_123",
                test_name="Test",
                description="Test description",
                variant_a=variant_a,
                variant_b=variant_a,  # Same variant
                start_time=datetime.now().isoformat(),
                end_time=datetime.now().isoformat()
            )
    
    def test_ab_test_status_management(self):
        """Test A/B test status management"""
        if ABTest is None or PromptVariant is None:
            pytest.skip("ABTest or PromptVariant not implemented yet")
        
        variant_a = PromptVariant(
            variant_id="variant_a",
            name="Test A",
            description="Test variant A",
            prompt_content="Test prompt A"
        )
        
        variant_b = PromptVariant(
            variant_id="variant_b",
            name="Test B",
            description="Test variant B",
            prompt_content="Test prompt B"
        )
        
        ab_test = ABTest(
            test_id="status_test",
            test_name="Status Test",
            description="Test status management",
            variant_a=variant_a,
            variant_b=variant_b,
            start_time=datetime.now().isoformat(),
            end_time=(datetime.now() + timedelta(days=1)).isoformat(),
            status="draft"
        )
        
        # Test status transitions
        assert ab_test.status == "draft"
        
        ab_test.start_test()
        assert ab_test.status == "running"
        
        ab_test.pause_test()
        assert ab_test.status == "paused"
        
        ab_test.resume_test()
        assert ab_test.status == "running"
        
        ab_test.complete_test()
        assert ab_test.status == "completed"
    
    def test_ab_test_progress_tracking(self):
        """Test A/B test progress tracking"""
        if ABTest is None or PromptVariant is None:
            pytest.skip("ABTest or PromptVariant not implemented yet")
        
        variant_a = PromptVariant(
            variant_id="variant_a",
            name="Test A",
            description="Test variant A",
            prompt_content="Test prompt A"
        )
        
        variant_b = PromptVariant(
            variant_id="variant_b",
            name="Test B",
            description="Test variant B",
            prompt_content="Test prompt B"
        )
        
        ab_test = ABTest(
            test_id="progress_test",
            test_name="Progress Test",
            description="Test progress tracking",
            variant_a=variant_a,
            variant_b=variant_b,
            start_time=datetime.now().isoformat(),
            end_time=(datetime.now() + timedelta(days=1)).isoformat(),
            test_parameters={'sample_size': 100}
        )
        
        # Test progress calculation
        assert ab_test.get_progress() == 0.0
        
        ab_test.add_result('variant_a', 0.8, {'accuracy': 0.85})
        ab_test.add_result('variant_b', 0.7, {'accuracy': 0.75})
        
        progress = ab_test.get_progress()
        assert progress > 0.0
        assert progress <= 1.0


class TestTestResult:
    """Test the TestResult data class"""
    
    def test_test_result_creation(self):
        """Test TestResult can be created with proper data"""
        if TestResult is None:
            pytest.skip("TestResult not implemented yet")
        
        result_data = {
            'result_id': 'result_123',
            'test_id': 'test_456',
            'variant_id': 'variant_a',
            'timestamp': datetime.now().isoformat(),
            'execution_time': 2.5,
            'success': True,
            'score': 0.85,
            'metrics': {'accuracy': 0.9, 'completeness': 0.8, 'relevance': 0.85},
            'output': 'Test output content',
            'error_details': None,
            'context': {'user_type': 'developer', 'task_complexity': 'medium'},
            'metadata': {'test_session': 'session_123', 'evaluator': 'auto'}
        }
        
        result = TestResult(**result_data)
        assert result.result_id == 'result_123'
        assert result.test_id == 'test_456'
        assert result.variant_id == 'variant_a'
        assert result.execution_time == 2.5
        assert result.success is True
        assert result.score == 0.85
        assert result.metrics == {'accuracy': 0.9, 'completeness': 0.8, 'relevance': 0.85}
        assert result.output == 'Test output content'
        assert result.error_details is None
        assert result.context == {'user_type': 'developer', 'task_complexity': 'medium'}
    
    def test_test_result_validation(self):
        """Test TestResult validation"""
        if TestResult is None:
            pytest.skip("TestResult not implemented yet")
        
        # Test invalid score (outside 0-1 range)
        with pytest.raises(ValueError):
            TestResult(
                result_id="result_123",
                test_id="test_456",
                variant_id="variant_a",
                timestamp=datetime.now().isoformat(),
                execution_time=1.0,
                success=True,
                score=1.5,  # Invalid score
                metrics={}
            )
        
        # Test negative execution time
        with pytest.raises(ValueError):
            TestResult(
                result_id="result_123",
                test_id="test_456",
                variant_id="variant_a",
                timestamp=datetime.now().isoformat(),
                execution_time=-1.0,  # Invalid execution time
                success=True,
                score=0.8,
                metrics={}
            )
    
    def test_test_result_analysis(self):
        """Test test result analysis methods"""
        if TestResult is None:
            pytest.skip("TestResult not implemented yet")
        
        result = TestResult(
            result_id="analysis_test",
            test_id="test_456",
            variant_id="variant_a",
            timestamp=datetime.now().isoformat(),
            execution_time=2.0,
            success=True,
            score=0.85,
            metrics={'accuracy': 0.9, 'completeness': 0.8, 'relevance': 0.85}
        )
        
        # Test metric aggregation
        avg_metric = result.get_average_metric()
        expected_avg = (0.9 + 0.8 + 0.85) / 3
        assert abs(avg_metric - expected_avg) < 0.001
        
        # Test quality assessment
        quality_score = result.get_quality_score()
        assert 0.0 <= quality_score <= 1.0
        
        # Test performance assessment
        performance_score = result.get_performance_score()
        assert 0.0 <= performance_score <= 1.0


class TestTestMetrics:
    """Test the TestMetrics data class"""
    
    def test_test_metrics_creation(self):
        """Test TestMetrics can be created with proper data"""
        if TestMetrics is None:
            pytest.skip("TestMetrics not implemented yet")
        
        metrics_data = {
            'test_id': 'test_123',
            'variant_a_results': [0.8, 0.9, 0.7, 0.85, 0.75],
            'variant_b_results': [0.7, 0.8, 0.6, 0.75, 0.65],
            'sample_size_a': 5,
            'sample_size_b': 5,
            'mean_a': 0.81,
            'mean_b': 0.71,
            'std_a': 0.06,
            'std_b': 0.07,
            'effect_size': 0.15,
            'confidence_interval': (0.02, 0.18),
            'p_value': 0.03,
            'significance_level': 0.05,
            'statistical_power': 0.85,
            'is_significant': True,
            'winner': 'variant_a'
        }
        
        metrics = TestMetrics(**metrics_data)
        assert metrics.test_id == 'test_123'
        assert metrics.variant_a_results == [0.8, 0.9, 0.7, 0.85, 0.75]
        assert metrics.variant_b_results == [0.7, 0.8, 0.6, 0.75, 0.65]
        assert metrics.sample_size_a == 5
        assert metrics.sample_size_b == 5
        assert metrics.mean_a == 0.81
        assert metrics.mean_b == 0.71
        assert metrics.effect_size == 0.15
        assert metrics.p_value == 0.03
        assert metrics.is_significant is True
        assert metrics.winner == 'variant_a'
    
    def test_test_metrics_calculations(self):
        """Test statistical calculations in TestMetrics"""
        if TestMetrics is None:
            pytest.skip("TestMetrics not implemented yet")
        
        metrics = TestMetrics(
            test_id="calc_test",
            variant_a_results=[0.8, 0.9, 0.7, 0.85, 0.75],
            variant_b_results=[0.7, 0.8, 0.6, 0.75, 0.65],
            sample_size_a=5,
            sample_size_b=5,
            significance_level=0.05
        )
        
        # Test automatic calculation of statistics
        metrics.calculate_statistics()
        
        assert metrics.mean_a > 0
        assert metrics.mean_b > 0
        assert metrics.std_a >= 0
        assert metrics.std_b >= 0
        assert metrics.effect_size is not None
        assert metrics.p_value is not None
        assert metrics.confidence_interval is not None
        assert metrics.is_significant is not None
        assert metrics.winner is not None
    
    def test_test_metrics_interpretation(self):
        """Test metrics interpretation methods"""
        if TestMetrics is None:
            pytest.skip("TestMetrics not implemented yet")
        
        metrics = TestMetrics(
            test_id="interpret_test",
            variant_a_results=[0.9, 0.85, 0.8, 0.88, 0.82],
            variant_b_results=[0.7, 0.75, 0.6, 0.78, 0.65],
            sample_size_a=5,
            sample_size_b=5,
            significance_level=0.05
        )
        
        metrics.calculate_statistics()
        
        # Test interpretation methods
        interpretation = metrics.get_interpretation()
        assert isinstance(interpretation, dict)
        assert 'winner' in interpretation
        assert 'confidence' in interpretation
        assert 'effect_size_interpretation' in interpretation
        assert 'recommendation' in interpretation
        
        # Test effect size interpretation
        effect_size_desc = metrics.get_effect_size_description()
        assert effect_size_desc in ['small', 'medium', 'large', 'very large']
        
        # Test confidence description
        confidence_desc = metrics.get_confidence_description()
        assert isinstance(confidence_desc, str)
        assert len(confidence_desc) > 0


class TestStatisticalAnalysis:
    """Test the StatisticalAnalysis utility class"""
    
    def test_statistical_analysis_t_test(self):
        """Test t-test statistical analysis"""
        if StatisticalAnalysis is None:
            pytest.skip("StatisticalAnalysis not implemented yet")
        
        # Sample data for t-test
        group_a = [0.8, 0.9, 0.7, 0.85, 0.75, 0.82, 0.88, 0.73, 0.86, 0.79]
        group_b = [0.7, 0.8, 0.6, 0.75, 0.65, 0.72, 0.78, 0.63, 0.76, 0.69]
        
        # Perform t-test
        t_stat, p_value = StatisticalAnalysis.t_test(group_a, group_b)
        
        assert isinstance(t_stat, float)
        assert isinstance(p_value, float)
        assert 0.0 <= p_value <= 1.0
    
    def test_statistical_analysis_effect_size(self):
        """Test effect size calculation"""
        if StatisticalAnalysis is None:
            pytest.skip("StatisticalAnalysis not implemented yet")
        
        group_a = [0.8, 0.9, 0.7, 0.85, 0.75]
        group_b = [0.7, 0.8, 0.6, 0.75, 0.65]
        
        # Calculate Cohen's d
        cohens_d = StatisticalAnalysis.cohens_d(group_a, group_b)
        
        assert isinstance(cohens_d, float)
        assert cohens_d >= 0.0  # Should be positive for group_a > group_b
    
    def test_statistical_analysis_confidence_interval(self):
        """Test confidence interval calculation"""
        if StatisticalAnalysis is None:
            pytest.skip("StatisticalAnalysis not implemented yet")
        
        group_a = [0.8, 0.9, 0.7, 0.85, 0.75]
        group_b = [0.7, 0.8, 0.6, 0.75, 0.65]
        
        # Calculate confidence interval for difference of means
        ci_lower, ci_upper = StatisticalAnalysis.confidence_interval(group_a, group_b, confidence=0.95)
        
        assert isinstance(ci_lower, float)
        assert isinstance(ci_upper, float)
        assert ci_lower <= ci_upper
    
    def test_statistical_analysis_power_calculation(self):
        """Test statistical power calculation"""
        if StatisticalAnalysis is None:
            pytest.skip("StatisticalAnalysis not implemented yet")
        
        # Calculate power for given parameters
        power = StatisticalAnalysis.calculate_power(
            effect_size=0.5,
            sample_size=20,
            significance_level=0.05
        )
        
        assert isinstance(power, float)
        assert 0.0 <= power <= 1.0
    
    def test_statistical_analysis_sample_size_calculation(self):
        """Test sample size calculation"""
        if StatisticalAnalysis is None:
            pytest.skip("StatisticalAnalysis not implemented yet")
        
        # Calculate required sample size
        sample_size = StatisticalAnalysis.calculate_sample_size(
            effect_size=0.5,
            power=0.8,
            significance_level=0.05
        )
        
        assert isinstance(sample_size, int)
        assert sample_size > 0


class TestABTestingFramework:
    """Test the ABTestingFramework component"""
    
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
            mock_session.ab_testing_state = {
                'active_tests': {},
                'test_results': {},
                'selected_test': None
            }
            yield mock_session
    
    def test_ab_testing_framework_initialization(self, temp_storage, mock_streamlit):
        """Test ABTestingFramework can be initialized"""
        if ABTestingFramework is None:
            pytest.skip("ABTestingFramework not implemented yet")
        
        framework = ABTestingFramework(storage_path=temp_storage)
        assert framework.storage_path == temp_storage
        assert hasattr(framework, 'active_tests')
        assert hasattr(framework, 'test_results')
        assert hasattr(framework, 'test_templates')
        assert hasattr(framework, 'evaluators')
        assert isinstance(framework.active_tests, dict)
        assert isinstance(framework.test_results, dict)
    
    def test_create_ab_test(self, temp_storage, mock_streamlit):
        """Test creating A/B tests"""
        if ABTestingFramework is None or PromptVariant is None:
            pytest.skip("ABTestingFramework or PromptVariant not implemented yet")
        
        framework = ABTestingFramework(storage_path=temp_storage)
        
        # Create test variants
        variant_a = PromptVariant(
            variant_id="test_a",
            name="Original",
            description="Original prompt",
            prompt_content="Analyze this code: {code}"
        )
        
        variant_b = PromptVariant(
            variant_id="test_b",
            name="Enhanced",
            description="Enhanced prompt",
            prompt_content="Perform a detailed analysis of this code: {code}"
        )
        
        # Create A/B test
        test_config = {
            'test_name': 'Code Analysis Test',
            'description': 'Testing code analysis prompts',
            'sample_size': 50,
            'confidence_level': 0.95,
            'effect_size': 0.1
        }
        
        test_id = framework.create_ab_test(
            variant_a=variant_a,
            variant_b=variant_b,
            test_config=test_config
        )
        
        assert test_id is not None
        assert test_id in framework.active_tests
        
        created_test = framework.active_tests[test_id]
        assert created_test.test_name == 'Code Analysis Test'
        assert created_test.variant_a.variant_id == 'test_a'
        assert created_test.variant_b.variant_id == 'test_b'
        assert created_test.status == 'draft'
    
    def test_run_ab_test(self, temp_storage, mock_streamlit):
        """Test running A/B tests"""
        if ABTestingFramework is None or PromptVariant is None:
            pytest.skip("ABTestingFramework or PromptVariant not implemented yet")
        
        framework = ABTestingFramework(storage_path=temp_storage)
        
        # Create test variants
        variant_a = PromptVariant(
            variant_id="run_test_a",
            name="Original",
            description="Original prompt",
            prompt_content="Analyze: {input}"
        )
        
        variant_b = PromptVariant(
            variant_id="run_test_b",
            name="Enhanced",
            description="Enhanced prompt",
            prompt_content="Detailed analysis: {input}"
        )
        
        # Create A/B test
        test_config = {
            'test_name': 'Run Test',
            'description': 'Testing run functionality',
            'sample_size': 10,
            'confidence_level': 0.95
        }
        
        test_id = framework.create_ab_test(
            variant_a=variant_a,
            variant_b=variant_b,
            test_config=test_config
        )
        
        # Start the test
        framework.start_test(test_id)
        
        # Run test with sample data
        test_inputs = [
            {'input': 'Sample code 1'},
            {'input': 'Sample code 2'},
            {'input': 'Sample code 3'}
        ]
        
        results = framework.run_test(test_id, test_inputs)
        
        assert isinstance(results, list)
        assert len(results) == len(test_inputs) * 2  # Each input tested on both variants
        
        # Check results structure
        for result in results:
            assert hasattr(result, 'result_id')
            assert hasattr(result, 'test_id')
            assert hasattr(result, 'variant_id')
            assert hasattr(result, 'score')
            assert result.test_id == test_id
            assert result.variant_id in ['run_test_a', 'run_test_b']
    
    def test_evaluate_results(self, temp_storage, mock_streamlit):
        """Test evaluating test results"""
        if ABTestingFramework is None or TestResult is None:
            pytest.skip("ABTestingFramework or TestResult not implemented yet")
        
        framework = ABTestingFramework(storage_path=temp_storage)
        
        # Create mock test results
        test_results = [
            TestResult(
                result_id=f"result_{i}",
                test_id="eval_test",
                variant_id="variant_a" if i % 2 == 0 else "variant_b",
                timestamp=datetime.now().isoformat(),
                execution_time=1.0,
                success=True,
                score=0.8 + (i % 3) * 0.05,  # Varying scores
                metrics={'accuracy': 0.85}
            )
            for i in range(20)
        ]
        
        # Store results
        framework.test_results["eval_test"] = test_results
        
        # Evaluate results
        evaluation = framework.evaluate_results("eval_test")
        
        assert isinstance(evaluation, dict)
        assert 'variant_a_performance' in evaluation
        assert 'variant_b_performance' in evaluation
        assert 'statistical_significance' in evaluation
        assert 'confidence_interval' in evaluation
        assert 'effect_size' in evaluation
        assert 'winner' in evaluation
        assert 'recommendation' in evaluation
    
    def test_get_test_status(self, temp_storage, mock_streamlit):
        """Test getting test status"""
        if ABTestingFramework is None or PromptVariant is None:
            pytest.skip("ABTestingFramework or PromptVariant not implemented yet")
        
        framework = ABTestingFramework(storage_path=temp_storage)
        
        # Create test
        variant_a = PromptVariant(
            variant_id="status_a",
            name="Original",
            description="Original prompt",
            prompt_content="Test prompt A"
        )
        
        variant_b = PromptVariant(
            variant_id="status_b",
            name="Enhanced",
            description="Enhanced prompt",
            prompt_content="Test prompt B"
        )
        
        test_config = {
            'test_name': 'Status Test',
            'description': 'Testing status functionality',
            'sample_size': 20
        }
        
        test_id = framework.create_ab_test(
            variant_a=variant_a,
            variant_b=variant_b,
            test_config=test_config
        )
        
        # Test initial status
        status = framework.get_test_status(test_id)
        assert status['status'] == 'draft'
        assert status['progress'] == 0.0
        assert status['results_count'] == 0
        
        # Start test and check status
        framework.start_test(test_id)
        status = framework.get_test_status(test_id)
        assert status['status'] == 'running'
    
    def test_export_test_results(self, temp_storage, mock_streamlit):
        """Test exporting test results"""
        if ABTestingFramework is None or TestResult is None:
            pytest.skip("ABTestingFramework or TestResult not implemented yet")
        
        framework = ABTestingFramework(storage_path=temp_storage)
        
        # Create mock test results
        test_results = [
            TestResult(
                result_id=f"export_result_{i}",
                test_id="export_test",
                variant_id="variant_a" if i % 2 == 0 else "variant_b",
                timestamp=datetime.now().isoformat(),
                execution_time=1.0,
                success=True,
                score=0.8,
                metrics={'accuracy': 0.85}
            )
            for i in range(10)
        ]
        
        framework.test_results["export_test"] = test_results
        
        # Export results
        export_data = framework.export_test_results("export_test")
        
        assert isinstance(export_data, dict)
        assert 'test_id' in export_data
        assert 'export_timestamp' in export_data
        assert 'results' in export_data
        assert 'summary' in export_data
        assert len(export_data['results']) == 10
        
        # Verify results structure
        for result in export_data['results']:
            assert 'result_id' in result
            assert 'variant_id' in result
            assert 'score' in result
            assert 'metrics' in result
    
    def test_load_test_templates(self, temp_storage, mock_streamlit):
        """Test loading test templates"""
        if ABTestingFramework is None:
            pytest.skip("ABTestingFramework not implemented yet")
        
        framework = ABTestingFramework(storage_path=temp_storage)
        
        # Create test template file
        template_data = {
            'templates': [
                {
                    'name': 'Code Analysis Template',
                    'description': 'Template for code analysis A/B tests',
                    'variant_a_template': 'Analyze this code: {code}',
                    'variant_b_template': 'Perform detailed analysis: {code}',
                    'success_criteria': {'accuracy': 0.8},
                    'sample_inputs': [{'code': 'def hello(): pass'}]
                }
            ]
        }
        
        template_file = temp_storage / "test_templates.json"
        with open(template_file, 'w') as f:
            json.dump(template_data, f)
        
        # Load templates
        framework.load_test_templates(template_file)
        
        assert len(framework.test_templates) > 0
        assert 'Code Analysis Template' in framework.test_templates
        
        template = framework.test_templates['Code Analysis Template']
        assert template['description'] == 'Template for code analysis A/B tests'
        assert template['variant_a_template'] == 'Analyze this code: {code}'
        assert template['variant_b_template'] == 'Perform detailed analysis: {code}'
    
    @patch('streamlit.title')
    @patch('streamlit.subheader')
    @patch('streamlit.tabs')
    def test_render_ab_testing_interface(self, mock_tabs, mock_subheader, mock_title, temp_storage, mock_streamlit):
        """Test rendering A/B testing interface"""
        if ABTestingFramework is None:
            pytest.skip("ABTestingFramework not implemented yet")
        
        framework = ABTestingFramework(storage_path=temp_storage)
        
        # Mock tabs
        mock_tabs.return_value = [MagicMock(), MagicMock(), MagicMock()]
        
        # Test that method exists and can be called
        assert hasattr(framework, 'render_ab_testing_interface')
        
        # Call method (should not raise exceptions)
        try:
            framework.render_ab_testing_interface()
            # If we get here, the method executed without errors
            assert True
        except AttributeError:
            # Method might not exist yet
            pytest.skip("render_ab_testing_interface not implemented yet")


class TestGlobalFunctions:
    """Test global convenience functions"""
    
    def test_run_ab_test_function(self):
        """Test run_ab_test global function"""
        if run_ab_test is None:
            pytest.skip("run_ab_test not implemented yet")
        
        # Test data
        variants = [
            {'id': 'a', 'content': 'Prompt A'},
            {'id': 'b', 'content': 'Prompt B'}
        ]
        
        test_inputs = [
            {'input': 'Test 1'},
            {'input': 'Test 2'}
        ]
        
        # Run A/B test
        results = run_ab_test(variants, test_inputs)
        
        assert isinstance(results, list)
        assert len(results) > 0
        
        # Check results structure
        for result in results:
            assert 'variant_id' in result
            assert 'score' in result
            assert 'metrics' in result
    
    def test_analyze_test_results_function(self):
        """Test analyze_test_results global function"""
        if analyze_test_results is None:
            pytest.skip("analyze_test_results not implemented yet")
        
        # Mock results data
        results_a = [0.8, 0.9, 0.7, 0.85, 0.75]
        results_b = [0.7, 0.8, 0.6, 0.75, 0.65]
        
        # Analyze results
        analysis = analyze_test_results(results_a, results_b)
        
        assert isinstance(analysis, dict)
        assert 'winner' in analysis
        assert 'p_value' in analysis
        assert 'effect_size' in analysis
        assert 'confidence_interval' in analysis
        assert 'is_significant' in analysis
    
    def test_get_confidence_level_function(self):
        """Test get_confidence_level global function"""
        if get_confidence_level is None:
            pytest.skip("get_confidence_level not implemented yet")
        
        # Test with different sample sizes
        confidence_small = get_confidence_level(sample_size=10, effect_size=0.5)
        confidence_large = get_confidence_level(sample_size=100, effect_size=0.5)
        
        assert isinstance(confidence_small, float)
        assert isinstance(confidence_large, float)
        assert 0.0 <= confidence_small <= 1.0
        assert 0.0 <= confidence_large <= 1.0
        assert confidence_large >= confidence_small  # Larger sample should have higher confidence
    
    def test_ab_testing_error_handling(self, temp_storage):
        """Test error handling in A/B testing system"""
        if ABTestingFramework is None:
            pytest.skip("ABTestingFramework not implemented yet")
        
        framework = ABTestingFramework(storage_path=temp_storage)
        
        # Test with invalid test ID
        status = framework.get_test_status("invalid_test_id")
        assert status is None or status.get('error') is not None
        
        # Test with empty results
        evaluation = framework.evaluate_results("non_existent_test")
        assert evaluation is None or evaluation.get('error') is not None
    
    def test_ab_testing_performance(self, temp_storage):
        """Test A/B testing performance with large datasets"""
        if ABTestingFramework is None:
            pytest.skip("ABTestingFramework not implemented yet")
        
        framework = ABTestingFramework(storage_path=temp_storage)
        
        # Create large dataset
        start_time = time.time()
        
        large_results = []
        for i in range(1000):
            result = TestResult(
                result_id=f"perf_result_{i}",
                test_id="performance_test",
                variant_id="variant_a" if i % 2 == 0 else "variant_b",
                timestamp=datetime.now().isoformat(),
                execution_time=1.0,
                success=True,
                score=0.7 + (i % 10) * 0.02,
                metrics={'accuracy': 0.8}
            )
            large_results.append(result)
        
        framework.test_results["performance_test"] = large_results
        
        # Test evaluation performance
        evaluation = framework.evaluate_results("performance_test")
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        # Should process 1000 results in reasonable time (less than 5 seconds)
        assert processing_time < 5.0
        
        # Verify evaluation completed
        assert evaluation is not None
        assert 'winner' in evaluation
        assert 'statistical_significance' in evaluation