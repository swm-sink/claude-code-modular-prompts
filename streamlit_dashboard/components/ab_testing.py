"""
A/B Testing Framework for Prompt Variations
Provides comprehensive testing and analysis capabilities for prompt optimization
"""

import streamlit as st
import json
import time
import hashlib
import uuid
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Union
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta
from collections import defaultdict, deque
import threading
import statistics
import math
import random
from enum import Enum
import numpy as np
from scipy import stats
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


class TestStatus(Enum):
    """Enumeration of test statuses"""
    DRAFT = "draft"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    FAILED = "failed"


class EvaluationMethod(Enum):
    """Enumeration of evaluation methods"""
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    HYBRID = "hybrid"


@dataclass
class PromptVariant:
    """Represents a prompt variant for A/B testing"""
    
    variant_id: str
    name: str
    description: str
    prompt_content: str
    template_variables: Dict[str, Any] = field(default_factory=dict)
    expected_outcomes: List[str] = field(default_factory=list)
    success_criteria: Dict[str, float] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate variant data after initialization"""
        if not self.variant_id or self.variant_id.strip() == "":
            raise ValueError("Variant ID cannot be empty")
        
        if not self.prompt_content or self.prompt_content.strip() == "":
            raise ValueError("Prompt content cannot be empty")
    
    def render(self, context: Dict[str, Any] = None) -> str:
        """Render the prompt with template variables"""
        content = self.prompt_content
        
        # Use template variables first, then context
        variables = {**self.template_variables}
        if context:
            variables.update(context)
        
        # Simple template variable replacement
        for key, value in variables.items():
            placeholder = f"{{{key}}}"
            content = content.replace(placeholder, str(value))
        
        return content
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert variant to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PromptVariant':
        """Create variant from dictionary"""
        return cls(**data)


@dataclass
class TestResult:
    """Represents a single test result"""
    
    result_id: str
    test_id: str
    variant_id: str
    timestamp: str
    execution_time: float
    success: bool
    score: float
    metrics: Dict[str, float] = field(default_factory=dict)
    output: str = ""
    error_details: Optional[str] = None
    context: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate result data"""
        if not (0.0 <= self.score <= 1.0):
            raise ValueError("Score must be between 0.0 and 1.0")
        
        if self.execution_time < 0:
            raise ValueError("Execution time cannot be negative")
    
    def get_average_metric(self) -> float:
        """Get average of all metrics"""
        if not self.metrics:
            return 0.0
        return statistics.mean(self.metrics.values())
    
    def get_quality_score(self) -> float:
        """Calculate quality score based on metrics and success"""
        if not self.success:
            return 0.0
        
        # Weight score and metrics
        quality = self.score * 0.6
        if self.metrics:
            quality += self.get_average_metric() * 0.4
        
        return min(quality, 1.0)
    
    def get_performance_score(self) -> float:
        """Calculate performance score based on execution time"""
        # Assume 2 seconds is the baseline, with diminishing returns
        if self.execution_time <= 1.0:
            return 1.0
        elif self.execution_time <= 2.0:
            return 0.8
        elif self.execution_time <= 5.0:
            return 0.6
        elif self.execution_time <= 10.0:
            return 0.4
        else:
            return 0.2
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TestResult':
        """Create result from dictionary"""
        return cls(**data)


@dataclass
class TestMetrics:
    """Statistical metrics for A/B test analysis"""
    
    test_id: str
    variant_a_results: List[float]
    variant_b_results: List[float]
    sample_size_a: int
    sample_size_b: int
    significance_level: float = 0.05
    mean_a: float = 0.0
    mean_b: float = 0.0
    std_a: float = 0.0
    std_b: float = 0.0
    effect_size: float = 0.0
    confidence_interval: Tuple[float, float] = (0.0, 0.0)
    p_value: float = 1.0
    statistical_power: float = 0.0
    is_significant: bool = False
    winner: Optional[str] = None
    
    def calculate_statistics(self):
        """Calculate all statistical metrics"""
        if not self.variant_a_results or not self.variant_b_results:
            return
        
        # Basic statistics
        self.mean_a = statistics.mean(self.variant_a_results)
        self.mean_b = statistics.mean(self.variant_b_results)
        
        if len(self.variant_a_results) > 1:
            self.std_a = statistics.stdev(self.variant_a_results)
        if len(self.variant_b_results) > 1:
            self.std_b = statistics.stdev(self.variant_b_results)
        
        # Effect size (Cohen's d)
        pooled_std = math.sqrt(((self.std_a ** 2) + (self.std_b ** 2)) / 2)
        if pooled_std > 0:
            self.effect_size = abs(self.mean_a - self.mean_b) / pooled_std
        
        # T-test
        try:
            t_stat, self.p_value = stats.ttest_ind(
                self.variant_a_results, 
                self.variant_b_results
            )
            
            # Statistical significance
            self.is_significant = self.p_value < self.significance_level
            
            # Confidence interval
            diff = self.mean_a - self.mean_b
            se_diff = math.sqrt(
                (self.std_a ** 2 / self.sample_size_a) + 
                (self.std_b ** 2 / self.sample_size_b)
            )
            
            t_critical = stats.t.ppf(1 - self.significance_level / 2, 
                                   self.sample_size_a + self.sample_size_b - 2)
            
            margin_error = t_critical * se_diff
            self.confidence_interval = (
                diff - margin_error,
                diff + margin_error
            )
            
            # Determine winner
            if self.is_significant:
                self.winner = "variant_a" if self.mean_a > self.mean_b else "variant_b"
            else:
                self.winner = "variant_a" if self.mean_a > self.mean_b else "variant_b"  # Still show which performed better
            
        except Exception as e:
            st.error(f"Error calculating statistics: {str(e)}")
    
    def get_interpretation(self) -> Dict[str, Any]:
        """Get human-readable interpretation of results"""
        interpretation = {
            'winner': self.winner,
            'confidence': f"{(1 - self.significance_level) * 100:.0f}%",
            'effect_size_interpretation': self.get_effect_size_description(),
            'statistical_significance': self.is_significant,
            'p_value': self.p_value,
            'recommendation': self._get_recommendation()
        }
        
        return interpretation
    
    def get_effect_size_description(self) -> str:
        """Get effect size description"""
        if self.effect_size < 0.2:
            return "small"
        elif self.effect_size < 0.5:
            return "medium"
        elif self.effect_size < 0.8:
            return "large"
        else:
            return "very large"
    
    def get_confidence_description(self) -> str:
        """Get confidence level description"""
        if self.is_significant:
            return f"We can be {(1 - self.significance_level) * 100:.0f}% confident that {self.winner} is better."
        else:
            return "No statistically significant difference found."
    
    def _get_recommendation(self) -> str:
        """Get recommendation based on results"""
        if not self.is_significant:
            return "Continue testing or collect more data. No significant difference found."
        
        effect_desc = self.get_effect_size_description()
        winner_name = self.winner.replace("_", " ").title()
        
        if effect_desc in ["large", "very large"]:
            return f"Strong recommendation: Deploy {winner_name}. Effect size is {effect_desc}."
        elif effect_desc == "medium":
            return f"Moderate recommendation: Consider deploying {winner_name}. Effect size is {effect_desc}."
        else:
            return f"Weak recommendation: {winner_name} shows improvement but effect size is {effect_desc}."


@dataclass
class ABTest:
    """Represents an A/B test configuration and state"""
    
    test_id: str
    test_name: str
    description: str
    variant_a: PromptVariant
    variant_b: PromptVariant
    start_time: str
    end_time: str
    test_parameters: Dict[str, Any] = field(default_factory=dict)
    test_context: Dict[str, Any] = field(default_factory=dict)
    status: str = TestStatus.DRAFT.value
    results_count: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate test configuration"""
        if not self.test_id or self.test_id.strip() == "":
            raise ValueError("Test ID cannot be empty")
        
        if self.variant_a.variant_id == self.variant_b.variant_id:
            raise ValueError("Variants must have different IDs")
    
    def start_test(self):
        """Start the test"""
        self.status = TestStatus.RUNNING.value
        self.start_time = datetime.now().isoformat()
    
    def pause_test(self):
        """Pause the test"""
        self.status = TestStatus.PAUSED.value
    
    def resume_test(self):
        """Resume the test"""
        self.status = TestStatus.RUNNING.value
    
    def complete_test(self):
        """Complete the test"""
        self.status = TestStatus.COMPLETED.value
        self.end_time = datetime.now().isoformat()
    
    def cancel_test(self):
        """Cancel the test"""
        self.status = TestStatus.CANCELLED.value
    
    def add_result(self, variant_id: str, score: float, metrics: Dict[str, float]):
        """Add a test result"""
        self.results_count += 1
    
    def get_progress(self) -> float:
        """Get test progress as percentage"""
        target_sample_size = self.test_parameters.get('sample_size', 100)
        return min(self.results_count / target_sample_size, 1.0)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert test to dictionary for serialization"""
        data = asdict(self)
        data['variant_a'] = self.variant_a.to_dict()
        data['variant_b'] = self.variant_b.to_dict()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ABTest':
        """Create test from dictionary"""
        variant_a = PromptVariant.from_dict(data.pop('variant_a'))
        variant_b = PromptVariant.from_dict(data.pop('variant_b'))
        return cls(variant_a=variant_a, variant_b=variant_b, **data)


class StatisticalAnalysis:
    """Utility class for statistical analysis"""
    
    @staticmethod
    def t_test(group_a: List[float], group_b: List[float]) -> Tuple[float, float]:
        """Perform independent t-test"""
        return stats.ttest_ind(group_a, group_b)
    
    @staticmethod
    def cohens_d(group_a: List[float], group_b: List[float]) -> float:
        """Calculate Cohen's d effect size"""
        mean_a = statistics.mean(group_a)
        mean_b = statistics.mean(group_b)
        
        if len(group_a) > 1 and len(group_b) > 1:
            std_a = statistics.stdev(group_a)
            std_b = statistics.stdev(group_b)
            pooled_std = math.sqrt((std_a ** 2 + std_b ** 2) / 2)
            
            if pooled_std > 0:
                return abs(mean_a - mean_b) / pooled_std
        
        return 0.0
    
    @staticmethod
    def confidence_interval(group_a: List[float], group_b: List[float], 
                          confidence: float = 0.95) -> Tuple[float, float]:
        """Calculate confidence interval for difference of means"""
        mean_a = statistics.mean(group_a)
        mean_b = statistics.mean(group_b)
        diff = mean_a - mean_b
        
        if len(group_a) > 1 and len(group_b) > 1:
            std_a = statistics.stdev(group_a)
            std_b = statistics.stdev(group_b)
            se_diff = math.sqrt(
                (std_a ** 2 / len(group_a)) + 
                (std_b ** 2 / len(group_b))
            )
            
            alpha = 1 - confidence
            t_critical = stats.t.ppf(1 - alpha / 2, len(group_a) + len(group_b) - 2)
            margin_error = t_critical * se_diff
            
            return (diff - margin_error, diff + margin_error)
        
        return (diff, diff)
    
    @staticmethod
    def calculate_power(effect_size: float, sample_size: int, 
                       significance_level: float = 0.05) -> float:
        """Calculate statistical power"""
        # Simplified power calculation
        z_alpha = stats.norm.ppf(1 - significance_level / 2)
        z_beta = effect_size * math.sqrt(sample_size / 2) - z_alpha
        power = stats.norm.cdf(z_beta)
        return max(0.0, min(1.0, power))
    
    @staticmethod
    def calculate_sample_size(effect_size: float, power: float = 0.8,
                            significance_level: float = 0.05) -> int:
        """Calculate required sample size"""
        z_alpha = stats.norm.ppf(1 - significance_level / 2)
        z_beta = stats.norm.ppf(power)
        
        sample_size = 2 * ((z_alpha + z_beta) / effect_size) ** 2
        return max(10, int(math.ceil(sample_size)))


class ABTestingFramework:
    """Comprehensive A/B testing framework for prompt optimization"""
    
    def __init__(self, storage_path: Path):
        """Initialize A/B testing framework"""
        self.storage_path = storage_path
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        # Create subdirectories
        self.tests_dir = self.storage_path / "tests"
        self.results_dir = self.storage_path / "results"
        self.templates_dir = self.storage_path / "templates"
        
        for dir_path in [self.tests_dir, self.results_dir, self.templates_dir]:
            dir_path.mkdir(exist_ok=True)
        
        # In-memory storage
        self.active_tests: Dict[str, ABTest] = {}
        self.test_results: Dict[str, List[TestResult]] = {}
        self.test_templates: Dict[str, Dict[str, Any]] = {}
        
        # Configuration
        self.evaluators = {
            'accuracy': self._evaluate_accuracy,
            'completeness': self._evaluate_completeness,
            'relevance': self._evaluate_relevance,
            'coherence': self._evaluate_coherence
        }
        
        # Thread safety
        self.lock = threading.Lock()
        
        # Load existing data
        self._load_existing_tests()
        self._load_existing_results()
    
    def _load_existing_tests(self):
        """Load existing tests from storage"""
        try:
            for test_file in self.tests_dir.glob("*.json"):
                with open(test_file, 'r') as f:
                    test_data = json.load(f)
                
                test = ABTest.from_dict(test_data)
                self.active_tests[test.test_id] = test
        except Exception as e:
            st.error(f"Error loading existing tests: {str(e)}")
    
    def _load_existing_results(self):
        """Load existing results from storage"""
        try:
            for results_file in self.results_dir.glob("*.json"):
                with open(results_file, 'r') as f:
                    results_data = json.load(f)
                
                test_id = results_data.get('test_id')
                if test_id:
                    results = [TestResult.from_dict(r) for r in results_data.get('results', [])]
                    self.test_results[test_id] = results
        except Exception as e:
            st.error(f"Error loading existing results: {str(e)}")
    
    def create_ab_test(self, variant_a: PromptVariant, variant_b: PromptVariant,
                      test_config: Dict[str, Any]) -> str:
        """Create a new A/B test"""
        test_id = str(uuid.uuid4())
        
        # Create test configuration
        ab_test = ABTest(
            test_id=test_id,
            test_name=test_config.get('test_name', 'Unnamed Test'),
            description=test_config.get('description', ''),
            variant_a=variant_a,
            variant_b=variant_b,
            start_time=datetime.now().isoformat(),
            end_time=(datetime.now() + timedelta(days=test_config.get('duration_days', 7))).isoformat(),
            test_parameters={
                'sample_size': test_config.get('sample_size', 100),
                'confidence_level': test_config.get('confidence_level', 0.95),
                'power': test_config.get('power', 0.8),
                'effect_size': test_config.get('effect_size', 0.2),
                'evaluation_method': test_config.get('evaluation_method', 'automatic')
            },
            test_context=test_config.get('context', {}),
            metadata=test_config.get('metadata', {})
        )
        
        # Store test
        with self.lock:
            self.active_tests[test_id] = ab_test
            self.test_results[test_id] = []
            self._save_test(ab_test)
        
        return test_id
    
    def _save_test(self, test: ABTest):
        """Save test to storage"""
        try:
            test_file = self.tests_dir / f"{test.test_id}.json"
            with open(test_file, 'w') as f:
                json.dump(test.to_dict(), f, indent=2)
        except Exception as e:
            st.error(f"Error saving test: {str(e)}")
    
    def start_test(self, test_id: str):
        """Start a test"""
        if test_id in self.active_tests:
            test = self.active_tests[test_id]
            test.start_test()
            self._save_test(test)
    
    def pause_test(self, test_id: str):
        """Pause a test"""
        if test_id in self.active_tests:
            test = self.active_tests[test_id]
            test.pause_test()
            self._save_test(test)
    
    def resume_test(self, test_id: str):
        """Resume a test"""
        if test_id in self.active_tests:
            test = self.active_tests[test_id]
            test.resume_test()
            self._save_test(test)
    
    def complete_test(self, test_id: str):
        """Complete a test"""
        if test_id in self.active_tests:
            test = self.active_tests[test_id]
            test.complete_test()
            self._save_test(test)
    
    def run_test(self, test_id: str, test_inputs: List[Dict[str, Any]]) -> List[TestResult]:
        """Run A/B test with given inputs"""
        if test_id not in self.active_tests:
            raise ValueError(f"Test {test_id} not found")
        
        test = self.active_tests[test_id]
        if test.status != TestStatus.RUNNING.value:
            raise ValueError(f"Test {test_id} is not running")
        
        results = []
        
        for input_data in test_inputs:
            # Test variant A
            result_a = self._execute_variant_test(test, test.variant_a, input_data)
            results.append(result_a)
            
            # Test variant B
            result_b = self._execute_variant_test(test, test.variant_b, input_data)
            results.append(result_b)
            
            # Update test progress
            test.add_result(test.variant_a.variant_id, result_a.score, result_a.metrics)
            test.add_result(test.variant_b.variant_id, result_b.score, result_b.metrics)
        
        # Store results
        with self.lock:
            self.test_results[test_id].extend(results)
            self._save_results(test_id, results)
            self._save_test(test)
        
        return results
    
    def _execute_variant_test(self, test: ABTest, variant: PromptVariant, 
                            input_data: Dict[str, Any]) -> TestResult:
        """Execute a single variant test"""
        start_time = time.time()
        
        try:
            # Render prompt with input data
            rendered_prompt = variant.render(input_data)
            
            # Simulate execution (in real implementation, this would call the AI model)
            execution_time = time.time() - start_time
            
            # Evaluate result (simplified evaluation)
            score, metrics = self._evaluate_variant_result(
                variant, rendered_prompt, input_data, test.test_parameters
            )
            
            # Create result
            result = TestResult(
                result_id=str(uuid.uuid4()),
                test_id=test.test_id,
                variant_id=variant.variant_id,
                timestamp=datetime.now().isoformat(),
                execution_time=execution_time,
                success=True,
                score=score,
                metrics=metrics,
                output=rendered_prompt,
                context=input_data
            )
            
        except Exception as e:
            # Handle errors
            result = TestResult(
                result_id=str(uuid.uuid4()),
                test_id=test.test_id,
                variant_id=variant.variant_id,
                timestamp=datetime.now().isoformat(),
                execution_time=time.time() - start_time,
                success=False,
                score=0.0,
                metrics={},
                output="",
                error_details=str(e),
                context=input_data
            )
        
        return result
    
    def _evaluate_variant_result(self, variant: PromptVariant, output: str,
                                input_data: Dict[str, Any], test_params: Dict[str, Any]) -> Tuple[float, Dict[str, float]]:
        """Evaluate variant result"""
        # Simplified evaluation - in real implementation, this would be more sophisticated
        metrics = {}
        
        # Evaluate using configured evaluators
        for metric_name, evaluator in self.evaluators.items():
            try:
                score = evaluator(variant, output, input_data)
                metrics[metric_name] = score
            except Exception as e:
                st.warning(f"Error evaluating {metric_name}: {str(e)}")
                metrics[metric_name] = 0.0
        
        # Calculate overall score
        overall_score = statistics.mean(metrics.values()) if metrics else 0.0
        
        return overall_score, metrics
    
    def _evaluate_accuracy(self, variant: PromptVariant, output: str, 
                          input_data: Dict[str, Any]) -> float:
        """Evaluate accuracy of the output"""
        # Simplified accuracy evaluation
        return random.uniform(0.6, 0.95)
    
    def _evaluate_completeness(self, variant: PromptVariant, output: str,
                             input_data: Dict[str, Any]) -> float:
        """Evaluate completeness of the output"""
        # Simplified completeness evaluation
        return random.uniform(0.5, 0.9)
    
    def _evaluate_relevance(self, variant: PromptVariant, output: str,
                           input_data: Dict[str, Any]) -> float:
        """Evaluate relevance of the output"""
        # Simplified relevance evaluation
        return random.uniform(0.7, 0.95)
    
    def _evaluate_coherence(self, variant: PromptVariant, output: str,
                           input_data: Dict[str, Any]) -> float:
        """Evaluate coherence of the output"""
        # Simplified coherence evaluation
        return random.uniform(0.6, 0.9)
    
    def _save_results(self, test_id: str, results: List[TestResult]):
        """Save results to storage"""
        try:
            results_file = self.results_dir / f"{test_id}.json"
            
            # Load existing results
            existing_results = []
            if results_file.exists():
                with open(results_file, 'r') as f:
                    existing_data = json.load(f)
                    existing_results = existing_data.get('results', [])
            
            # Add new results
            all_results = existing_results + [result.to_dict() for result in results]
            
            # Save all results
            results_data = {
                'test_id': test_id,
                'results': all_results,
                'last_updated': datetime.now().isoformat()
            }
            
            with open(results_file, 'w') as f:
                json.dump(results_data, f, indent=2)
                
        except Exception as e:
            st.error(f"Error saving results: {str(e)}")
    
    def evaluate_results(self, test_id: str) -> Optional[Dict[str, Any]]:
        """Evaluate test results and provide statistical analysis"""
        if test_id not in self.test_results or not self.test_results[test_id]:
            return None
        
        results = self.test_results[test_id]
        
        # Separate results by variant
        variant_a_results = []
        variant_b_results = []
        
        for result in results:
            if result.variant_id == self.active_tests[test_id].variant_a.variant_id:
                variant_a_results.append(result.score)
            elif result.variant_id == self.active_tests[test_id].variant_b.variant_id:
                variant_b_results.append(result.score)
        
        if not variant_a_results or not variant_b_results:
            return {
                'error': 'Insufficient data for analysis',
                'variant_a_count': len(variant_a_results),
                'variant_b_count': len(variant_b_results)
            }
        
        # Create metrics object
        metrics = TestMetrics(
            test_id=test_id,
            variant_a_results=variant_a_results,
            variant_b_results=variant_b_results,
            sample_size_a=len(variant_a_results),
            sample_size_b=len(variant_b_results)
        )
        
        # Calculate statistics
        metrics.calculate_statistics()
        
        # Create evaluation summary
        evaluation = {
            'test_id': test_id,
            'variant_a_performance': {
                'mean': metrics.mean_a,
                'std': metrics.std_a,
                'sample_size': metrics.sample_size_a
            },
            'variant_b_performance': {
                'mean': metrics.mean_b,
                'std': metrics.std_b,
                'sample_size': metrics.sample_size_b
            },
            'statistical_significance': metrics.is_significant,
            'p_value': metrics.p_value,
            'confidence_interval': metrics.confidence_interval,
            'effect_size': metrics.effect_size,
            'effect_size_description': metrics.get_effect_size_description(),
            'winner': metrics.winner,
            'confidence_description': metrics.get_confidence_description(),
            'interpretation': metrics.get_interpretation(),
            'recommendation': metrics._get_recommendation()
        }
        
        return evaluation
    
    def get_test_status(self, test_id: str) -> Optional[Dict[str, Any]]:
        """Get test status and progress"""
        if test_id not in self.active_tests:
            return None
        
        test = self.active_tests[test_id]
        results_count = len(self.test_results.get(test_id, []))
        
        status = {
            'test_id': test_id,
            'test_name': test.test_name,
            'status': test.status,
            'progress': test.get_progress(),
            'results_count': results_count,
            'target_sample_size': test.test_parameters.get('sample_size', 100),
            'start_time': test.start_time,
            'end_time': test.end_time,
            'variant_a_id': test.variant_a.variant_id,
            'variant_b_id': test.variant_b.variant_id
        }
        
        return status
    
    def export_test_results(self, test_id: str) -> Optional[Dict[str, Any]]:
        """Export test results"""
        if test_id not in self.test_results:
            return None
        
        results = self.test_results[test_id]
        evaluation = self.evaluate_results(test_id)
        
        export_data = {
            'test_id': test_id,
            'export_timestamp': datetime.now().isoformat(),
            'results': [result.to_dict() for result in results],
            'summary': {
                'total_results': len(results),
                'variant_a_results': len([r for r in results if r.variant_id == self.active_tests[test_id].variant_a.variant_id]),
                'variant_b_results': len([r for r in results if r.variant_id == self.active_tests[test_id].variant_b.variant_id]),
                'success_rate': len([r for r in results if r.success]) / len(results) if results else 0.0,
                'average_score': statistics.mean([r.score for r in results]) if results else 0.0,
                'average_execution_time': statistics.mean([r.execution_time for r in results]) if results else 0.0
            },
            'evaluation': evaluation
        }
        
        return export_data
    
    def load_test_templates(self, template_file: Path):
        """Load test templates from file"""
        try:
            with open(template_file, 'r') as f:
                template_data = json.load(f)
            
            templates = template_data.get('templates', [])
            for template in templates:
                self.test_templates[template['name']] = template
                
        except Exception as e:
            st.error(f"Error loading test templates: {str(e)}")
    
    def render_ab_testing_interface(self):
        """Render the A/B testing interface"""
        st.title("🧪 A/B Testing Framework")
        
        # Main tabs
        tabs = st.tabs([
            "🎯 Create Test", "📊 Active Tests", "📈 Results & Analysis", "⚙️ Settings"
        ])
        
        tab1, tab2, tab3, tab4 = tabs
        
        with tab1:
            self._render_create_test_tab()
        
        with tab2:
            self._render_active_tests_tab()
        
        with tab3:
            self._render_results_analysis_tab()
        
        with tab4:
            self._render_settings_tab()
    
    def _render_create_test_tab(self):
        """Render create test tab"""
        st.subheader("🎯 Create New A/B Test")
        
        with st.form("create_ab_test"):
            # Test configuration
            test_name = st.text_input("Test Name", placeholder="e.g., Code Analysis Prompt Optimization")
            description = st.text_area("Description", placeholder="Describe the purpose of this test...")
            
            # Variant A
            st.markdown("### Variant A (Control)")
            variant_a_name = st.text_input("Variant A Name", value="Original")
            variant_a_description = st.text_area("Variant A Description", placeholder="Describe the control variant...")
            variant_a_content = st.text_area("Variant A Prompt", placeholder="Enter the control prompt content...")
            
            # Variant B
            st.markdown("### Variant B (Treatment)")
            variant_b_name = st.text_input("Variant B Name", value="Modified")
            variant_b_description = st.text_area("Variant B Description", placeholder="Describe the treatment variant...")
            variant_b_content = st.text_area("Variant B Prompt", placeholder="Enter the treatment prompt content...")
            
            # Test parameters
            st.markdown("### Test Parameters")
            col1, col2 = st.columns(2)
            
            with col1:
                sample_size = st.number_input("Sample Size", min_value=10, max_value=1000, value=100)
                confidence_level = st.selectbox("Confidence Level", [0.90, 0.95, 0.99], index=1)
            
            with col2:
                duration_days = st.number_input("Duration (days)", min_value=1, max_value=30, value=7)
                effect_size = st.number_input("Expected Effect Size", min_value=0.05, max_value=1.0, value=0.2, step=0.05)
            
            # Submit button
            submitted = st.form_submit_button("Create A/B Test")
            
            if submitted:
                if test_name and variant_a_content and variant_b_content:
                    try:
                        # Create variants
                        variant_a = PromptVariant(
                            variant_id=f"variant_a_{uuid.uuid4().hex[:8]}",
                            name=variant_a_name,
                            description=variant_a_description,
                            prompt_content=variant_a_content
                        )
                        
                        variant_b = PromptVariant(
                            variant_id=f"variant_b_{uuid.uuid4().hex[:8]}",
                            name=variant_b_name,
                            description=variant_b_description,
                            prompt_content=variant_b_content
                        )
                        
                        # Create test
                        test_config = {
                            'test_name': test_name,
                            'description': description,
                            'sample_size': sample_size,
                            'confidence_level': confidence_level,
                            'duration_days': duration_days,
                            'effect_size': effect_size
                        }
                        
                        test_id = self.create_ab_test(variant_a, variant_b, test_config)
                        
                        st.success(f"✅ A/B test created successfully! Test ID: {test_id}")
                        
                    except Exception as e:
                        st.error(f"❌ Error creating test: {str(e)}")
                else:
                    st.error("❌ Please fill in all required fields")
    
    def _render_active_tests_tab(self):
        """Render active tests tab"""
        st.subheader("📊 Active Tests")
        
        if not self.active_tests:
            st.info("No active tests found. Create your first test in the 'Create Test' tab.")
            return
        
        # Tests table
        for test_id, test in self.active_tests.items():
            with st.expander(f"🧪 {test.test_name} ({test.status})"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Status", test.status)
                    st.metric("Progress", f"{test.get_progress():.1%}")
                
                with col2:
                    st.metric("Results Count", test.results_count)
                    st.metric("Target Sample Size", test.test_parameters.get('sample_size', 'N/A'))
                
                with col3:
                    st.metric("Confidence Level", f"{test.test_parameters.get('confidence_level', 0.95):.0%}")
                    st.metric("Effect Size", f"{test.test_parameters.get('effect_size', 0.2):.2f}")
                
                # Test details
                st.markdown("**Description:**")
                st.write(test.description)
                
                st.markdown("**Variants:**")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"**Variant A:** {test.variant_a.name}")
                    st.code(test.variant_a.prompt_content[:200] + "..." if len(test.variant_a.prompt_content) > 200 else test.variant_a.prompt_content)
                
                with col2:
                    st.markdown(f"**Variant B:** {test.variant_b.name}")
                    st.code(test.variant_b.prompt_content[:200] + "..." if len(test.variant_b.prompt_content) > 200 else test.variant_b.prompt_content)
                
                # Action buttons
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    if test.status == TestStatus.DRAFT.value:
                        if st.button("▶️ Start", key=f"start_{test_id}"):
                            self.start_test(test_id)
                            st.experimental_rerun()
                
                with col2:
                    if test.status == TestStatus.RUNNING.value:
                        if st.button("⏸️ Pause", key=f"pause_{test_id}"):
                            self.pause_test(test_id)
                            st.experimental_rerun()
                
                with col3:
                    if test.status == TestStatus.PAUSED.value:
                        if st.button("▶️ Resume", key=f"resume_{test_id}"):
                            self.resume_test(test_id)
                            st.experimental_rerun()
                
                with col4:
                    if test.status in [TestStatus.RUNNING.value, TestStatus.PAUSED.value]:
                        if st.button("✅ Complete", key=f"complete_{test_id}"):
                            self.complete_test(test_id)
                            st.experimental_rerun()
    
    def _render_results_analysis_tab(self):
        """Render results analysis tab"""
        st.subheader("📈 Results & Analysis")
        
        if not self.test_results:
            st.info("No test results available yet. Run some tests to see results here.")
            return
        
        # Test selector
        test_options = list(self.test_results.keys())
        selected_test = st.selectbox("Select Test", test_options)
        
        if selected_test:
            # Get evaluation
            evaluation = self.evaluate_results(selected_test)
            
            if evaluation and 'error' not in evaluation:
                # Summary metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Winner", evaluation['winner'] or "No Winner")
                
                with col2:
                    st.metric("P-Value", f"{evaluation['p_value']:.4f}")
                
                with col3:
                    st.metric("Effect Size", f"{evaluation['effect_size']:.3f}")
                
                with col4:
                    st.metric("Significant", "Yes" if evaluation['statistical_significance'] else "No")
                
                # Performance comparison
                st.markdown("### Performance Comparison")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Variant A Performance**")
                    st.metric("Mean Score", f"{evaluation['variant_a_performance']['mean']:.3f}")
                    st.metric("Standard Deviation", f"{evaluation['variant_a_performance']['std']:.3f}")
                    st.metric("Sample Size", evaluation['variant_a_performance']['sample_size'])
                
                with col2:
                    st.markdown("**Variant B Performance**")
                    st.metric("Mean Score", f"{evaluation['variant_b_performance']['mean']:.3f}")
                    st.metric("Standard Deviation", f"{evaluation['variant_b_performance']['std']:.3f}")
                    st.metric("Sample Size", evaluation['variant_b_performance']['sample_size'])
                
                # Confidence interval
                st.markdown("### Statistical Analysis")
                ci_lower, ci_upper = evaluation['confidence_interval']
                st.write(f"**Confidence Interval:** [{ci_lower:.3f}, {ci_upper:.3f}]")
                st.write(f"**Effect Size:** {evaluation['effect_size_description']}")
                st.write(f"**Interpretation:** {evaluation['confidence_description']}")
                
                # Recommendation
                st.markdown("### Recommendation")
                st.info(evaluation['recommendation'])
                
                # Export results
                if st.button("📤 Export Results"):
                    export_data = self.export_test_results(selected_test)
                    if export_data:
                        export_file = self.storage_path / f"export_{selected_test}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                        with open(export_file, 'w') as f:
                            json.dump(export_data, f, indent=2)
                        st.success(f"Results exported to: {export_file}")
                
            else:
                st.warning("Insufficient data for statistical analysis or error occurred.")
                if evaluation and 'error' in evaluation:
                    st.error(f"Error: {evaluation['error']}")
    
    def _render_settings_tab(self):
        """Render settings tab"""
        st.subheader("⚙️ Settings")
        
        # Framework settings
        st.markdown("### Framework Settings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Storage Path:** {self.storage_path}")
            st.write(f"**Active Tests:** {len(self.active_tests)}")
            st.write(f"**Test Templates:** {len(self.test_templates)}")
        
        with col2:
            st.write(f"**Total Results:** {sum(len(results) for results in self.test_results.values())}")
            st.write(f"**Evaluators:** {len(self.evaluators)}")
        
        # Data management
        st.markdown("### Data Management")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🗑️ Clear All Data"):
                if st.checkbox("I understand this will delete all test data"):
                    self.active_tests.clear()
                    self.test_results.clear()
                    st.success("All data cleared!")
        
        with col2:
            if st.button("📊 Refresh Data"):
                self._load_existing_tests()
                self._load_existing_results()
                st.success("Data refreshed!")
        
        with col3:
            if st.button("📋 Show Statistics"):
                st.json({
                    'total_tests': len(self.active_tests),
                    'total_results': sum(len(results) for results in self.test_results.values()),
                    'running_tests': len([t for t in self.active_tests.values() if t.status == TestStatus.RUNNING.value]),
                    'completed_tests': len([t for t in self.active_tests.values() if t.status == TestStatus.COMPLETED.value])
                })
    
    def render(self):
        """Main render method for A/B Testing Framework"""
        self.render_ab_testing_interface()


# Global convenience functions
def run_ab_test(variants: List[Dict[str, Any]], test_inputs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Run A/B test with given variants and inputs"""
    results = []
    
    for input_data in test_inputs:
        for variant in variants:
            # Simulate test execution
            score = random.uniform(0.5, 1.0)
            metrics = {
                'accuracy': random.uniform(0.6, 0.95),
                'relevance': random.uniform(0.7, 0.9),
                'completeness': random.uniform(0.5, 0.85)
            }
            
            result = {
                'variant_id': variant['id'],
                'input': input_data,
                'score': score,
                'metrics': metrics,
                'timestamp': datetime.now().isoformat()
            }
            
            results.append(result)
    
    return results


def analyze_test_results(results_a: List[float], results_b: List[float]) -> Dict[str, Any]:
    """Analyze A/B test results"""
    # Create metrics object
    metrics = TestMetrics(
        test_id="analysis",
        variant_a_results=results_a,
        variant_b_results=results_b,
        sample_size_a=len(results_a),
        sample_size_b=len(results_b)
    )
    
    # Calculate statistics
    metrics.calculate_statistics()
    
    # Return analysis
    return {
        'winner': metrics.winner,
        'p_value': metrics.p_value,
        'effect_size': metrics.effect_size,
        'confidence_interval': metrics.confidence_interval,
        'is_significant': metrics.is_significant,
        'mean_a': metrics.mean_a,
        'mean_b': metrics.mean_b,
        'interpretation': metrics.get_interpretation()
    }


def get_confidence_level(sample_size: int, effect_size: float) -> float:
    """Get confidence level based on sample size and effect size"""
    # Calculate statistical power
    power = StatisticalAnalysis.calculate_power(effect_size, sample_size)
    
    # Convert power to confidence level (simplified)
    confidence = min(0.99, max(0.5, power))
    
    return confidence