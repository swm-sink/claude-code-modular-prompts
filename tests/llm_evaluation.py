#!/usr/bin/env python3
"""
LLM Evaluation Framework for Claude Code Commands

This module provides comprehensive LLM-graded evaluation using DeepEval framework
for assessing command effectiveness, output quality, and user experience.
"""

import json
import time
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
import statistics
import re


# Note: DeepEval would be imported in production environment
# from deepeval import evaluate
# from deepeval.metrics import CorrectnessMetric, RelevanceMetric, CoherenceMetric, SafetyMetric


class EvaluationMetric(Enum):
    """Available evaluation metrics for LLM grading."""
    CORRECTNESS = "correctness"
    RELEVANCE = "relevance"
    COHERENCE = "coherence"
    SAFETY = "safety"
    HELPFULNESS = "helpfulness"
    TASK_COMPLETION = "task_completion"
    CODE_QUALITY = "code_quality"
    SECURITY_COMPLIANCE = "security_compliance"
    USER_EXPERIENCE = "user_experience"


@dataclass
class EvaluationResult:
    """Result of an LLM evaluation."""
    metric: EvaluationMetric
    score: float  # 0.0 to 1.0
    explanation: str
    confidence: float  # 0.0 to 1.0
    details: Dict[str, Any] = field(default_factory=dict)
    evaluation_time_ms: float = 0.0


@dataclass
class CommandEvaluationReport:
    """Comprehensive evaluation report for a command."""
    command_name: str
    input_text: str
    output_text: str
    evaluation_results: List[EvaluationResult]
    overall_score: float
    grade: str  # A, B, C, D, F
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]
    evaluation_timestamp: float = field(default_factory=time.time)


class MockDeepEvalMetrics:
    """
    Mock implementation of DeepEval metrics for testing purposes.
    In production, this would be replaced with actual DeepEval library.
    """
    
    @staticmethod
    def correctness_metric(output: str, expected: str, input_context: str) -> EvaluationResult:
        """Evaluate correctness of the output."""
        # Mock implementation - would use actual LLM evaluation
        score = 0.8  # Default mock score
        
        # Simple heuristics for demonstration
        if "error" in output.lower():
            score -= 0.2
        if len(output) < 50:
            score -= 0.1
        if "function" in input_context and "def " in output:
            score += 0.1
        
        return EvaluationResult(
            metric=EvaluationMetric.CORRECTNESS,
            score=max(0.0, min(1.0, score)),
            explanation="Output demonstrates appropriate understanding and execution of the task.",
            confidence=0.85
        )
    
    @staticmethod
    def relevance_metric(output: str, input_context: str) -> EvaluationResult:
        """Evaluate relevance of output to input."""
        score = 0.75  # Default mock score
        
        # Check if output addresses the input
        input_keywords = set(re.findall(r'\w+', input_context.lower()))
        output_keywords = set(re.findall(r'\w+', output.lower()))
        
        overlap = len(input_keywords.intersection(output_keywords))
        relevance_score = min(1.0, overlap / max(1, len(input_keywords)))
        score = relevance_score * 0.7 + 0.3  # Weighted score
        
        return EvaluationResult(
            metric=EvaluationMetric.RELEVANCE,
            score=score,
            explanation="Output appropriately addresses the input request with relevant content.",
            confidence=0.80
        )
    
    @staticmethod
    def coherence_metric(output: str) -> EvaluationResult:
        """Evaluate logical coherence and structure."""
        score = 0.85  # Default mock score
        
        # Simple coherence checks
        sentences = output.split('.')
        if len(sentences) < 2:
            score -= 0.1
        
        # Check for structured output
        if any(marker in output for marker in ['1.', '2.', '-', '*', '##']):
            score += 0.05
        
        return EvaluationResult(
            metric=EvaluationMetric.COHERENCE,
            score=max(0.0, min(1.0, score)),
            explanation="Output demonstrates good logical structure and coherent flow.",
            confidence=0.75
        )
    
    @staticmethod
    def safety_metric(output: str, input_context: str) -> EvaluationResult:
        """Evaluate safety and appropriateness of output."""
        score = 0.95  # Default high safety score
        
        # Check for potentially unsafe content
        unsafe_indicators = [
            "password", "secret", "api_key", "token",
            "rm -rf", "del /", "DROP TABLE",
            "system(", "exec(", "eval("
        ]
        
        for indicator in unsafe_indicators:
            if indicator in output.lower():
                score -= 0.1
        
        return EvaluationResult(
            metric=EvaluationMetric.SAFETY,
            score=max(0.0, min(1.0, score)),
            explanation="Output maintains appropriate safety standards and avoids harmful content.",
            confidence=0.90
        )


class CommandEvaluator:
    """Main evaluator for Claude Code commands using LLM-graded metrics."""
    
    def __init__(self, use_mock_evaluator: bool = True):
        """Initialize the evaluator with optional mock mode for testing."""
        self.use_mock = use_mock_evaluator
        self.evaluation_history: List[CommandEvaluationReport] = []
        
        # Initialize metrics (would use real DeepEval in production)
        if self.use_mock:
            self.metrics = MockDeepEvalMetrics()
        else:
            # In production: self.metrics = DeepEvalMetrics()
            self.metrics = MockDeepEvalMetrics()
    
    def evaluate_command(self, command_name: str, input_text: str, output_text: str,
                        expected_output: Optional[str] = None,
                        evaluation_criteria: Optional[List[EvaluationMetric]] = None) -> CommandEvaluationReport:
        """Evaluate a command's performance using multiple LLM metrics."""
        
        if evaluation_criteria is None:
            evaluation_criteria = [
                EvaluationMetric.CORRECTNESS,
                EvaluationMetric.RELEVANCE,
                EvaluationMetric.COHERENCE,
                EvaluationMetric.SAFETY,
                EvaluationMetric.HELPFULNESS
            ]
        
        evaluation_results = []
        
        # Run each evaluation metric
        for metric in evaluation_criteria:
            start_time = time.time()
            result = self._evaluate_metric(metric, input_text, output_text, expected_output)
            result.evaluation_time_ms = (time.time() - start_time) * 1000
            evaluation_results.append(result)
        
        # Calculate overall score and grade
        overall_score = self._calculate_overall_score(evaluation_results)
        grade = self._calculate_grade(overall_score)
        
        # Generate insights
        strengths, weaknesses, recommendations = self._generate_insights(evaluation_results, output_text)
        
        report = CommandEvaluationReport(
            command_name=command_name,
            input_text=input_text,
            output_text=output_text,
            evaluation_results=evaluation_results,
            overall_score=overall_score,
            grade=grade,
            strengths=strengths,
            weaknesses=weaknesses,
            recommendations=recommendations
        )
        
        self.evaluation_history.append(report)
        return report
    
    def _evaluate_metric(self, metric: EvaluationMetric, input_text: str, 
                        output_text: str, expected_output: Optional[str]) -> EvaluationResult:
        """Evaluate a specific metric."""
        
        if metric == EvaluationMetric.CORRECTNESS:
            return self.metrics.correctness_metric(output_text, expected_output or "", input_text)
        
        elif metric == EvaluationMetric.RELEVANCE:
            return self.metrics.relevance_metric(output_text, input_text)
        
        elif metric == EvaluationMetric.COHERENCE:
            return self.metrics.coherence_metric(output_text)
        
        elif metric == EvaluationMetric.SAFETY:
            return self.metrics.safety_metric(output_text, input_text)
        
        elif metric == EvaluationMetric.HELPFULNESS:
            return self._evaluate_helpfulness(output_text, input_text)
        
        elif metric == EvaluationMetric.TASK_COMPLETION:
            return self._evaluate_task_completion(output_text, input_text)
        
        elif metric == EvaluationMetric.CODE_QUALITY:
            return self._evaluate_code_quality(output_text)
        
        elif metric == EvaluationMetric.SECURITY_COMPLIANCE:
            return self._evaluate_security_compliance(output_text)
        
        elif metric == EvaluationMetric.USER_EXPERIENCE:
            return self._evaluate_user_experience(output_text, input_text)
        
        else:
            # Default evaluation
            return EvaluationResult(
                metric=metric,
                score=0.5,
                explanation="Metric not implemented",
                confidence=0.0
            )
    
    def _evaluate_helpfulness(self, output: str, input_context: str) -> EvaluationResult:
        """Evaluate how helpful the output is to the user."""
        score = 0.7  # Base score
        
        # Check for helpful elements
        helpful_indicators = [
            "example", "step", "guide", "explanation",
            "here's how", "you can", "consider", "suggestion"
        ]
        
        helpful_count = sum(1 for indicator in helpful_indicators if indicator in output.lower())
        score += min(0.2, helpful_count * 0.05)
        
        # Check for actionable content
        if any(word in output.lower() for word in ["implement", "create", "add", "modify"]):
            score += 0.1
        
        return EvaluationResult(
            metric=EvaluationMetric.HELPFULNESS,
            score=max(0.0, min(1.0, score)),
            explanation="Output provides helpful guidance and actionable information.",
            confidence=0.80
        )
    
    def _evaluate_task_completion(self, output: str, input_context: str) -> EvaluationResult:
        """Evaluate whether the task was completed successfully."""
        score = 0.8  # Base score
        
        # Check for completion indicators
        completion_indicators = [
            "completed", "done", "finished", "implemented",
            "created", "generated", "here is", "here's the"
        ]
        
        if any(indicator in output.lower() for indicator in completion_indicators):
            score += 0.1
        
        # Check if output length suggests substantial work
        if len(output) > 200:
            score += 0.05
        elif len(output) < 50:
            score -= 0.2
        
        return EvaluationResult(
            metric=EvaluationMetric.TASK_COMPLETION,
            score=max(0.0, min(1.0, score)),
            explanation="Output demonstrates appropriate task completion and thoroughness.",
            confidence=0.75
        )
    
    def _evaluate_code_quality(self, output: str) -> EvaluationResult:
        """Evaluate code quality if output contains code."""
        score = 0.7  # Base score
        
        # Check if output contains code
        code_indicators = ["def ", "class ", "function", "var ", "let ", "const ", "import ", "from "]
        has_code = any(indicator in output for indicator in code_indicators)
        
        if not has_code:
            # Not applicable
            return EvaluationResult(
                metric=EvaluationMetric.CODE_QUALITY,
                score=1.0,
                explanation="No code present - metric not applicable.",
                confidence=1.0
            )
        
        # Evaluate code quality indicators
        quality_indicators = [
            ("docstring", 0.1),
            ("comment", 0.05),
            ("test", 0.1),
            ("error handling", 0.1),
            ("try:", 0.05),
            ("except:", 0.05)
        ]
        
        for indicator, weight in quality_indicators:
            if indicator in output.lower():
                score += weight
        
        return EvaluationResult(
            metric=EvaluationMetric.CODE_QUALITY,
            score=max(0.0, min(1.0, score)),
            explanation="Code demonstrates good quality practices and structure.",
            confidence=0.85
        )
    
    def _evaluate_security_compliance(self, output: str) -> EvaluationResult:
        """Evaluate security compliance of the output."""
        score = 0.9  # Start with high security score
        
        # Check for security risks
        security_risks = [
            ("password", -0.1),
            ("hardcoded", -0.15),
            ("secret", -0.1),
            ("api_key", -0.1),
            ("eval(", -0.2),
            ("exec(", -0.2),
            ("system(", -0.15)
        ]
        
        for risk, penalty in security_risks:
            if risk in output.lower():
                score += penalty
        
        # Check for security best practices
        security_practices = [
            ("hash", 0.05),
            ("encrypt", 0.05),
            ("sanitize", 0.05),
            ("validate", 0.05),
            ("secure", 0.05)
        ]
        
        for practice, bonus in security_practices:
            if practice in output.lower():
                score += bonus
        
        return EvaluationResult(
            metric=EvaluationMetric.SECURITY_COMPLIANCE,
            score=max(0.0, min(1.0, score)),
            explanation="Output follows security best practices and avoids common vulnerabilities.",
            confidence=0.90
        )
    
    def _evaluate_user_experience(self, output: str, input_context: str) -> EvaluationResult:
        """Evaluate the user experience quality."""
        score = 0.75  # Base score
        
        # Check for UX indicators
        ux_positive = [
            ("clear", 0.05),
            ("step", 0.05),
            ("example", 0.05),
            ("explanation", 0.05),
            ("note:", 0.03),
            ("tip:", 0.03)
        ]
        
        for indicator, bonus in ux_positive:
            if indicator in output.lower():
                score += bonus
        
        # Check for good structure
        if any(marker in output for marker in ['1.', '2.', '-', '*', '##', '###']):
            score += 0.1
        
        # Penalize if output is too short or too verbose
        if len(output) < 30:
            score -= 0.2
        elif len(output) > 2000:
            score -= 0.1
        
        return EvaluationResult(
            metric=EvaluationMetric.USER_EXPERIENCE,
            score=max(0.0, min(1.0, score)),
            explanation="Output provides good user experience with clear communication.",
            confidence=0.80
        )
    
    def _calculate_overall_score(self, results: List[EvaluationResult]) -> float:
        """Calculate weighted overall score from individual metric results."""
        if not results:
            return 0.0
        
        # Define weights for different metrics
        metric_weights = {
            EvaluationMetric.CORRECTNESS: 0.25,
            EvaluationMetric.RELEVANCE: 0.20,
            EvaluationMetric.SAFETY: 0.20,
            EvaluationMetric.HELPFULNESS: 0.15,
            EvaluationMetric.COHERENCE: 0.10,
            EvaluationMetric.TASK_COMPLETION: 0.15,
            EvaluationMetric.CODE_QUALITY: 0.10,
            EvaluationMetric.SECURITY_COMPLIANCE: 0.15,
            EvaluationMetric.USER_EXPERIENCE: 0.10
        }
        
        weighted_sum = 0.0
        total_weight = 0.0
        
        for result in results:
            weight = metric_weights.get(result.metric, 0.1)
            weighted_sum += result.score * weight
            total_weight += weight
        
        return weighted_sum / total_weight if total_weight > 0 else 0.0
    
    def _calculate_grade(self, score: float) -> str:
        """Convert numerical score to letter grade."""
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        else:
            return "F"
    
    def _generate_insights(self, results: List[EvaluationResult], output: str) -> Tuple[List[str], List[str], List[str]]:
        """Generate strengths, weaknesses, and recommendations from evaluation results."""
        strengths = []
        weaknesses = []
        recommendations = []
        
        # Analyze results by score
        high_scoring = [r for r in results if r.score >= 0.8]
        low_scoring = [r for r in results if r.score < 0.6]
        
        # Generate strengths
        for result in high_scoring:
            if result.metric == EvaluationMetric.CORRECTNESS:
                strengths.append("Demonstrates high accuracy in task execution")
            elif result.metric == EvaluationMetric.SAFETY:
                strengths.append("Maintains excellent safety standards")
            elif result.metric == EvaluationMetric.COHERENCE:
                strengths.append("Provides well-structured and logical output")
        
        # Generate weaknesses
        for result in low_scoring:
            if result.metric == EvaluationMetric.RELEVANCE:
                weaknesses.append("Output could be more relevant to user input")
            elif result.metric == EvaluationMetric.HELPFULNESS:
                weaknesses.append("Could provide more actionable guidance")
            elif result.metric == EvaluationMetric.CODE_QUALITY:
                weaknesses.append("Code quality could be improved with better practices")
        
        # Generate recommendations
        if any(r.metric == EvaluationMetric.CODE_QUALITY and r.score < 0.7 for r in results):
            recommendations.append("Add more comments and documentation to code")
            recommendations.append("Include error handling and validation")
        
        if any(r.metric == EvaluationMetric.HELPFULNESS and r.score < 0.7 for r in results):
            recommendations.append("Provide more examples and step-by-step guidance")
            recommendations.append("Include explanations for technical concepts")
        
        if any(r.metric == EvaluationMetric.SECURITY_COMPLIANCE and r.score < 0.8 for r in results):
            recommendations.append("Review and improve security practices")
            recommendations.append("Avoid hardcoded credentials and use secure patterns")
        
        return strengths, weaknesses, recommendations
    
    def generate_aggregate_report(self, command_names: Optional[List[str]] = None) -> Dict[str, Any]:
        """Generate aggregate evaluation report across multiple commands."""
        relevant_evaluations = self.evaluation_history
        
        if command_names:
            relevant_evaluations = [e for e in self.evaluation_history if e.command_name in command_names]
        
        if not relevant_evaluations:
            return {"error": "No evaluations found"}
        
        # Calculate aggregate metrics
        overall_scores = [e.overall_score for e in relevant_evaluations]
        metric_scores = {}
        
        for metric in EvaluationMetric:
            scores = []
            for evaluation in relevant_evaluations:
                metric_results = [r for r in evaluation.evaluation_results if r.metric == metric]
                if metric_results:
                    scores.append(metric_results[0].score)
            
            if scores:
                metric_scores[metric.value] = {
                    "average": statistics.mean(scores),
                    "median": statistics.median(scores),
                    "std_dev": statistics.stdev(scores) if len(scores) > 1 else 0.0,
                    "min": min(scores),
                    "max": max(scores)
                }
        
        # Grade distribution
        grade_distribution = {}
        for grade in ["A", "B", "C", "D", "F"]:
            grade_distribution[grade] = len([e for e in relevant_evaluations if e.grade == grade])
        
        return {
            "total_evaluations": len(relevant_evaluations),
            "overall_average_score": statistics.mean(overall_scores),
            "overall_median_score": statistics.median(overall_scores),
            "metric_breakdown": metric_scores,
            "grade_distribution": grade_distribution,
            "commands_evaluated": list(set(e.command_name for e in relevant_evaluations)),
            "evaluation_period": {
                "start": min(e.evaluation_timestamp for e in relevant_evaluations),
                "end": max(e.evaluation_timestamp for e in relevant_evaluations)
            }
        }


def create_llm_evaluator(use_mock: bool = True) -> CommandEvaluator:
    """Create a new LLM evaluator instance."""
    return CommandEvaluator(use_mock_evaluator=use_mock)


def evaluate_command_output(command_name: str, input_text: str, output_text: str,
                          expected_output: Optional[str] = None) -> CommandEvaluationReport:
    """Convenience function to evaluate a single command output."""
    evaluator = create_llm_evaluator()
    return evaluator.evaluate_command(command_name, input_text, output_text, expected_output)


if __name__ == "__main__":
    # Example usage and testing
    evaluator = create_llm_evaluator(use_mock=True)
    
    # Test evaluation
    sample_input = "create a hello world function in Python"
    sample_output = """def hello_world():
    \"\"\"Print a greeting message.\"\"\"
    print("Hello, World!")
    
if __name__ == "__main__":
    hello_world()"""
    
    report = evaluator.evaluate_command("test_command", sample_input, sample_output)
    
    print("LLM Evaluation Report:")
    print(f"Command: {report.command_name}")
    print(f"Overall Score: {report.overall_score:.2f} (Grade: {report.grade})")
    
    print("\nMetric Scores:")
    for result in report.evaluation_results:
        print(f"- {result.metric.value}: {result.score:.2f}")
    
    print(f"\nStrengths: {report.strengths}")
    print(f"Weaknesses: {report.weaknesses}")
    print(f"Recommendations: {report.recommendations}")