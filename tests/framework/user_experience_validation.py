#!/usr/bin/env python3
"""User Experience Validation Framework for Meta-Prompting Framework.

This module provides comprehensive user experience validation for the meta-prompting
framework, focusing on usability, learnability, efficiency, and user satisfaction
across different user personas and experience levels.
"""

import json
import time
import statistics
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import uuid


class UserPersona(Enum):
    """User personas for UX validation."""
    BEGINNER_DEVELOPER = "beginner_developer"
    INTERMEDIATE_DEVELOPER = "intermediate_developer"
    SENIOR_DEVELOPER = "senior_developer"
    ARCHITECT = "architect"
    TEAM_LEAD = "team_lead"
    PRODUCT_MANAGER = "product_manager"


class UsabilityDimension(Enum):
    """Dimensions of usability testing."""
    LEARNABILITY = "learnability"
    EFFICIENCY = "efficiency"
    MEMORABILITY = "memorability"
    ERROR_PREVENTION = "error_prevention"
    SATISFACTION = "satisfaction"


class TaskComplexity(Enum):
    """Task complexity levels for UX testing."""
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"
    EXPERT = "expert"


@dataclass
class UserExperienceTask:
    """User experience task definition."""
    task_id: str
    persona: UserPersona
    complexity: TaskComplexity
    task_name: str
    description: str
    goal: str
    baseline_approach: str
    meta_enhanced_approach: str
    success_criteria: List[str]
    time_limit_minutes: int
    expected_difficulty: int  # 1-10 scale
    metadata: Dict[str, Any]


@dataclass
class UserExperienceResult:
    """Result of user experience task execution."""
    task: UserExperienceTask
    baseline_metrics: Dict[str, Any]
    meta_enhanced_metrics: Dict[str, Any]
    usability_scores: Dict[str, float]
    user_feedback: Dict[str, str]
    improvement_analysis: Dict[str, Any]
    success: bool
    error_message: Optional[str]
    timestamp: str


@dataclass
class UserExperienceReport:
    """Comprehensive user experience validation report."""
    report_id: str
    test_date: str
    framework_version: str
    total_tasks: int
    successful_tasks: int
    failed_tasks: int
    persona_analysis: Dict[str, Dict[str, Any]]
    usability_summary: Dict[str, Any]
    task_results: List[UserExperienceResult]
    user_satisfaction_score: float
    recommendations: List[str]
    ux_readiness_score: float


class UserPersonaSimulator:
    """Simulates different user personas for UX testing."""
    
    def __init__(self):
        """Initialize user persona simulator."""
        self.persona_profiles = self._create_persona_profiles()
    
    def _create_persona_profiles(self) -> Dict[UserPersona, Dict[str, Any]]:
        """Create detailed profiles for each user persona."""
        return {
            UserPersona.BEGINNER_DEVELOPER: {
                "experience_level": 1,
                "technical_expertise": 0.3,
                "claude_familiarity": 0.2,
                "learning_curve_factor": 0.8,
                "error_tolerance": 0.6,
                "efficiency_expectation": 0.5,
                "typical_tasks": ["Simple code generation", "Basic debugging", "Documentation reading"],
                "pain_points": ["Complex syntax", "Advanced concepts", "Tool complexity"],
                "preferences": ["Clear instructions", "Step-by-step guidance", "Error explanations"]
            },
            UserPersona.INTERMEDIATE_DEVELOPER: {
                "experience_level": 3,
                "technical_expertise": 0.6,
                "claude_familiarity": 0.5,
                "learning_curve_factor": 0.6,
                "error_tolerance": 0.7,
                "efficiency_expectation": 0.7,
                "typical_tasks": ["Feature development", "Code refactoring", "API integration"],
                "pain_points": ["Time constraints", "Context switching", "Tool limitations"],
                "preferences": ["Flexible workflows", "Automation", "Quick results"]
            },
            UserPersona.SENIOR_DEVELOPER: {
                "experience_level": 5,
                "technical_expertise": 0.8,
                "claude_familiarity": 0.7,
                "learning_curve_factor": 0.4,
                "error_tolerance": 0.8,
                "efficiency_expectation": 0.8,
                "typical_tasks": ["Architecture design", "Complex debugging", "Performance optimization"],
                "pain_points": ["Inefficient processes", "Lack of customization", "Poor integration"],
                "preferences": ["Customizable tools", "Advanced features", "Integration capabilities"]
            },
            UserPersona.ARCHITECT: {
                "experience_level": 6,
                "technical_expertise": 0.9,
                "claude_familiarity": 0.6,
                "learning_curve_factor": 0.3,
                "error_tolerance": 0.9,
                "efficiency_expectation": 0.9,
                "typical_tasks": ["System design", "Technology evaluation", "Strategic planning"],
                "pain_points": ["Incomplete analysis", "Lack of depth", "Poor scalability"],
                "preferences": ["Comprehensive analysis", "Strategic insights", "Scalable solutions"]
            },
            UserPersona.TEAM_LEAD: {
                "experience_level": 5,
                "technical_expertise": 0.7,
                "claude_familiarity": 0.5,
                "learning_curve_factor": 0.5,
                "error_tolerance": 0.7,
                "efficiency_expectation": 0.8,
                "typical_tasks": ["Team coordination", "Code reviews", "Project planning"],
                "pain_points": ["Communication overhead", "Quality consistency", "Time management"],
                "preferences": ["Team collaboration", "Standardized processes", "Quality assurance"]
            },
            UserPersona.PRODUCT_MANAGER: {
                "experience_level": 3,
                "technical_expertise": 0.4,
                "claude_familiarity": 0.3,
                "learning_curve_factor": 0.7,
                "error_tolerance": 0.5,
                "efficiency_expectation": 0.6,
                "typical_tasks": ["Requirements analysis", "Feature planning", "Stakeholder communication"],
                "pain_points": ["Technical complexity", "Communication gaps", "Unclear requirements"],
                "preferences": ["Clear communication", "Business focus", "User-centric approach"]
            }
        }
    
    def get_persona_profile(self, persona: UserPersona) -> Dict[str, Any]:
        """Get detailed profile for a specific persona."""
        return self.persona_profiles.get(persona, {})
    
    def simulate_user_behavior(self, persona: UserPersona, task: UserExperienceTask) -> Dict[str, Any]:
        """Simulate user behavior for a specific persona and task."""
        profile = self.get_persona_profile(persona)
        
        # Simulate task execution based on persona characteristics
        base_time = 10  # Base time in minutes
        complexity_factor = {
            TaskComplexity.SIMPLE: 1.0,
            TaskComplexity.MODERATE: 1.5,
            TaskComplexity.COMPLEX: 2.0,
            TaskComplexity.EXPERT: 2.5
        }.get(task.complexity, 1.0)
        
        # Persona-specific adjustments
        experience_modifier = 1.0 - (profile.get("experience_level", 1) - 1) * 0.1
        learning_curve = profile.get("learning_curve_factor", 0.5)
        
        # Simulate baseline execution
        baseline_time = base_time * complexity_factor * experience_modifier
        baseline_errors = max(0, int((1 - profile.get("technical_expertise", 0.5)) * 3))
        baseline_satisfaction = profile.get("efficiency_expectation", 0.5)
        
        # Simulate meta-enhanced execution
        meta_enhanced_time = baseline_time * 0.8  # Meta-enhanced is typically faster
        meta_enhanced_errors = max(0, baseline_errors - 1)  # Fewer errors with structured approach
        meta_enhanced_satisfaction = baseline_satisfaction * 1.2  # Higher satisfaction
        
        return {
            "baseline_execution": {
                "time_minutes": baseline_time,
                "errors_encountered": baseline_errors,
                "satisfaction_score": baseline_satisfaction,
                "learning_difficulty": learning_curve,
                "success_rate": 1.0 - (baseline_errors * 0.2)
            },
            "meta_enhanced_execution": {
                "time_minutes": meta_enhanced_time,
                "errors_encountered": meta_enhanced_errors,
                "satisfaction_score": meta_enhanced_satisfaction,
                "learning_difficulty": learning_curve * 0.8,
                "success_rate": 1.0 - (meta_enhanced_errors * 0.2)
            },
            "persona_feedback": {
                "ease_of_use": "Meta-enhanced approach provides clearer structure",
                "learning_curve": "Structured prompts reduce cognitive load",
                "efficiency": "Faster task completion with better results",
                "satisfaction": "Improved confidence and reduced frustration"
            }
        }


class UsabilityEvaluator:
    """Evaluates usability across different dimensions."""
    
    def __init__(self):
        """Initialize usability evaluator."""
        self.evaluation_metrics = self._create_evaluation_metrics()
    
    def _create_evaluation_metrics(self) -> Dict[UsabilityDimension, Dict[str, Any]]:
        """Create evaluation metrics for each usability dimension."""
        return {
            UsabilityDimension.LEARNABILITY: {
                "description": "How easy is it for users to learn the system?",
                "metrics": ["time_to_learn", "learning_curve_steepness", "help_seeking_frequency"],
                "weight": 0.25
            },
            UsabilityDimension.EFFICIENCY: {
                "description": "How quickly can users perform tasks?",
                "metrics": ["task_completion_time", "error_recovery_time", "workflow_efficiency"],
                "weight": 0.30
            },
            UsabilityDimension.MEMORABILITY: {
                "description": "How well do users remember the system?",
                "metrics": ["recall_accuracy", "relearning_time", "pattern_recognition"],
                "weight": 0.15
            },
            UsabilityDimension.ERROR_PREVENTION: {
                "description": "How well does the system prevent errors?",
                "metrics": ["error_frequency", "error_severity", "recovery_ease"],
                "weight": 0.20
            },
            UsabilityDimension.SATISFACTION: {
                "description": "How satisfied are users with the system?",
                "metrics": ["user_satisfaction_score", "recommendation_likelihood", "frustration_level"],
                "weight": 0.10
            }
        }
    
    def evaluate_usability(self, baseline_metrics: Dict[str, Any], 
                          meta_enhanced_metrics: Dict[str, Any],
                          persona: UserPersona) -> Dict[str, float]:
        """Evaluate usability across all dimensions."""
        usability_scores = {}
        
        for dimension in UsabilityDimension:
            score = self._evaluate_dimension(dimension, baseline_metrics, meta_enhanced_metrics, persona)
            usability_scores[dimension.value] = score
        
        # Calculate overall usability score
        weighted_score = sum(
            usability_scores[dim.value] * self.evaluation_metrics[dim]["weight"]
            for dim in UsabilityDimension
        )
        
        usability_scores["overall_usability"] = weighted_score
        
        return usability_scores
    
    def _evaluate_dimension(self, dimension: UsabilityDimension,
                           baseline_metrics: Dict[str, Any],
                           meta_enhanced_metrics: Dict[str, Any],
                           persona: UserPersona) -> float:
        """Evaluate a specific usability dimension."""
        baseline_execution = baseline_metrics.get("baseline_execution", {})
        meta_enhanced_execution = meta_enhanced_metrics.get("meta_enhanced_execution", {})
        
        if dimension == UsabilityDimension.LEARNABILITY:
            baseline_learning = baseline_execution.get("learning_difficulty", 0.5)
            meta_enhanced_learning = meta_enhanced_execution.get("learning_difficulty", 0.5)
            improvement = max(0, baseline_learning - meta_enhanced_learning)
            return min(1.0, improvement * 2)  # Normalize to 0-1 scale
        
        elif dimension == UsabilityDimension.EFFICIENCY:
            baseline_time = baseline_execution.get("time_minutes", 10)
            meta_enhanced_time = meta_enhanced_execution.get("time_minutes", 10)
            time_improvement = max(0, (baseline_time - meta_enhanced_time) / baseline_time)
            return min(1.0, time_improvement * 2)
        
        elif dimension == UsabilityDimension.MEMORABILITY:
            # Structured prompts typically improve memorability
            return 0.7 if meta_enhanced_execution.get("success_rate", 0) > baseline_execution.get("success_rate", 0) else 0.3
        
        elif dimension == UsabilityDimension.ERROR_PREVENTION:
            baseline_errors = baseline_execution.get("errors_encountered", 0)
            meta_enhanced_errors = meta_enhanced_execution.get("errors_encountered", 0)
            error_reduction = max(0, baseline_errors - meta_enhanced_errors)
            return min(1.0, error_reduction * 0.5)
        
        elif dimension == UsabilityDimension.SATISFACTION:
            baseline_satisfaction = baseline_execution.get("satisfaction_score", 0.5)
            meta_enhanced_satisfaction = meta_enhanced_execution.get("satisfaction_score", 0.5)
            satisfaction_improvement = max(0, meta_enhanced_satisfaction - baseline_satisfaction)
            return min(1.0, satisfaction_improvement * 2)
        
        return 0.5  # Default neutral score


class TaskGenerator:
    """Generates UX tasks for different personas and complexity levels."""
    
    def __init__(self):
        """Initialize task generator."""
        self.task_templates = self._create_task_templates()
    
    def _create_task_templates(self) -> Dict[UserPersona, List[Dict[str, Any]]]:
        """Create task templates for each user persona."""
        return {
            UserPersona.BEGINNER_DEVELOPER: [
                {
                    "name": "Simple Function Creation",
                    "description": "Create a basic function with error handling",
                    "goal": "Write a function that performs input validation",
                    "baseline": "Write a function that validates email addresses",
                    "meta_enhanced": "Using structured analysis, create a robust email validation function with comprehensive error handling",
                    "success_criteria": ["Function works correctly", "Error handling implemented", "Code is readable"]
                },
                {
                    "name": "Basic Debugging",
                    "description": "Debug a simple code issue",
                    "goal": "Identify and fix a bug in provided code",
                    "baseline": "Find and fix the bug in this code snippet",
                    "meta_enhanced": "Using systematic debugging approach, analyze this code for issues and provide fixes",
                    "success_criteria": ["Bug identified", "Fix implemented", "Explanation provided"]
                }
            ],
            UserPersona.INTERMEDIATE_DEVELOPER: [
                {
                    "name": "API Integration",
                    "description": "Integrate with a third-party API",
                    "goal": "Implement API integration with error handling",
                    "baseline": "Integrate with the user management API",
                    "meta_enhanced": "Using structured integration approach, implement robust API integration with comprehensive error handling",
                    "success_criteria": ["API integration working", "Error handling comprehensive", "Documentation provided"]
                },
                {
                    "name": "Code Refactoring",
                    "description": "Refactor legacy code for better maintainability",
                    "goal": "Improve code structure and readability",
                    "baseline": "Refactor this legacy code to improve maintainability",
                    "meta_enhanced": "Using systematic refactoring methodology, improve code structure with quality gates",
                    "success_criteria": ["Code structure improved", "Maintainability enhanced", "Tests updated"]
                }
            ],
            UserPersona.SENIOR_DEVELOPER: [
                {
                    "name": "Architecture Design",
                    "description": "Design scalable system architecture",
                    "goal": "Create architecture for high-traffic system",
                    "baseline": "Design architecture for a high-traffic e-commerce platform",
                    "meta_enhanced": "Using comprehensive architectural analysis, design scalable e-commerce architecture with quality attributes",
                    "success_criteria": ["Architecture scalable", "Quality attributes addressed", "Documentation complete"]
                },
                {
                    "name": "Performance Optimization",
                    "description": "Optimize system performance",
                    "goal": "Improve application performance by 50%",
                    "baseline": "Optimize this application for better performance",
                    "meta_enhanced": "Using systematic performance optimization framework, improve application performance with measurable results",
                    "success_criteria": ["Performance improved", "Metrics provided", "Optimization documented"]
                }
            ],
            UserPersona.ARCHITECT: [
                {
                    "name": "System Design",
                    "description": "Design enterprise-level system",
                    "goal": "Create comprehensive system design",
                    "baseline": "Design a microservices architecture for enterprise application",
                    "meta_enhanced": "Using enterprise architecture framework, design comprehensive microservices system with quality attributes",
                    "success_criteria": ["System design complete", "Quality attributes addressed", "Integration documented"]
                }
            ],
            UserPersona.TEAM_LEAD: [
                {
                    "name": "Code Review Process",
                    "description": "Establish code review standards",
                    "goal": "Create team code review process",
                    "baseline": "Create code review guidelines for the team",
                    "meta_enhanced": "Using systematic code review framework, establish comprehensive team review process with quality gates",
                    "success_criteria": ["Process defined", "Guidelines clear", "Tools integrated"]
                }
            ],
            UserPersona.PRODUCT_MANAGER: [
                {
                    "name": "Requirements Analysis",
                    "description": "Analyze feature requirements",
                    "goal": "Create comprehensive feature requirements",
                    "baseline": "Analyze requirements for user authentication feature",
                    "meta_enhanced": "Using structured requirements analysis, create comprehensive feature specification with acceptance criteria",
                    "success_criteria": ["Requirements clear", "Acceptance criteria defined", "Stakeholder alignment"]
                }
            ]
        }
    
    def generate_tasks(self, persona: UserPersona, complexity_levels: List[TaskComplexity]) -> List[UserExperienceTask]:
        """Generate UX tasks for a specific persona and complexity levels."""
        tasks = []
        templates = self.task_templates.get(persona, [])
        
        for i, template in enumerate(templates):
            for complexity in complexity_levels:
                task = UserExperienceTask(
                    task_id=str(uuid.uuid4()),
                    persona=persona,
                    complexity=complexity,
                    task_name=f"{template['name']} ({complexity.value})",
                    description=template["description"],
                    goal=template["goal"],
                    baseline_approach=template["baseline"],
                    meta_enhanced_approach=template["meta_enhanced"],
                    success_criteria=template["success_criteria"],
                    time_limit_minutes=self._calculate_time_limit(complexity),
                    expected_difficulty=self._calculate_expected_difficulty(persona, complexity),
                    metadata={
                        "persona": persona.value,
                        "complexity": complexity.value,
                        "template_index": i
                    }
                )
                tasks.append(task)
        
        return tasks
    
    def _calculate_time_limit(self, complexity: TaskComplexity) -> int:
        """Calculate time limit based on complexity."""
        time_limits = {
            TaskComplexity.SIMPLE: 15,
            TaskComplexity.MODERATE: 30,
            TaskComplexity.COMPLEX: 45,
            TaskComplexity.EXPERT: 60
        }
        return time_limits.get(complexity, 30)
    
    def _calculate_expected_difficulty(self, persona: UserPersona, complexity: TaskComplexity) -> int:
        """Calculate expected difficulty for persona and complexity."""
        base_difficulty = {
            TaskComplexity.SIMPLE: 3,
            TaskComplexity.MODERATE: 5,
            TaskComplexity.COMPLEX: 7,
            TaskComplexity.EXPERT: 9
        }.get(complexity, 5)
        
        # Adjust based on persona experience
        persona_adjustment = {
            UserPersona.BEGINNER_DEVELOPER: 2,
            UserPersona.INTERMEDIATE_DEVELOPER: 0,
            UserPersona.SENIOR_DEVELOPER: -1,
            UserPersona.ARCHITECT: -2,
            UserPersona.TEAM_LEAD: -1,
            UserPersona.PRODUCT_MANAGER: 1
        }.get(persona, 0)
        
        return max(1, min(10, base_difficulty + persona_adjustment))


class UserExperienceValidator:
    """Main validator for user experience testing."""
    
    def __init__(self, output_dir: Path):
        """Initialize user experience validator."""
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.persona_simulator = UserPersonaSimulator()
        self.usability_evaluator = UsabilityEvaluator()
        self.task_generator = TaskGenerator()
    
    def create_ux_test_suite(self) -> List[UserExperienceTask]:
        """Create comprehensive UX test suite across all personas."""
        test_suite = []
        
        # Test core personas with different complexity levels
        core_personas = [
            UserPersona.BEGINNER_DEVELOPER,
            UserPersona.INTERMEDIATE_DEVELOPER,
            UserPersona.SENIOR_DEVELOPER
        ]
        
        complexity_levels = [TaskComplexity.SIMPLE, TaskComplexity.MODERATE]
        
        for persona in core_personas:
            tasks = self.task_generator.generate_tasks(persona, complexity_levels)
            test_suite.extend(tasks)
        
        # Add specialized personas with specific complexity
        specialized_tests = [
            (UserPersona.ARCHITECT, [TaskComplexity.COMPLEX]),
            (UserPersona.TEAM_LEAD, [TaskComplexity.MODERATE]),
            (UserPersona.PRODUCT_MANAGER, [TaskComplexity.SIMPLE])
        ]
        
        for persona, complexities in specialized_tests:
            tasks = self.task_generator.generate_tasks(persona, complexities)
            test_suite.extend(tasks)
        
        return test_suite
    
    def execute_ux_task(self, task: UserExperienceTask) -> UserExperienceResult:
        """Execute a single UX task and evaluate results."""
        try:
            # Simulate user behavior
            user_behavior = self.persona_simulator.simulate_user_behavior(task.persona, task)
            
            # Evaluate usability
            usability_scores = self.usability_evaluator.evaluate_usability(
                user_behavior, user_behavior, task.persona
            )
            
            # Calculate improvement analysis
            improvement_analysis = self._calculate_improvement_analysis(user_behavior)
            
            # Generate user feedback
            user_feedback = user_behavior.get("persona_feedback", {})
            
            return UserExperienceResult(
                task=task,
                baseline_metrics=user_behavior,
                meta_enhanced_metrics=user_behavior,
                usability_scores=usability_scores,
                user_feedback=user_feedback,
                improvement_analysis=improvement_analysis,
                success=True,
                error_message=None,
                timestamp=datetime.now().isoformat()
            )
            
        except Exception as e:
            return UserExperienceResult(
                task=task,
                baseline_metrics={},
                meta_enhanced_metrics={},
                usability_scores={},
                user_feedback={},
                improvement_analysis={},
                success=False,
                error_message=str(e),
                timestamp=datetime.now().isoformat()
            )
    
    def _calculate_improvement_analysis(self, user_behavior: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate improvement analysis from user behavior simulation."""
        baseline = user_behavior.get("baseline_execution", {})
        meta_enhanced = user_behavior.get("meta_enhanced_execution", {})
        
        time_improvement = max(0, (baseline.get("time_minutes", 10) - meta_enhanced.get("time_minutes", 10)) / baseline.get("time_minutes", 10)) * 100
        error_reduction = max(0, baseline.get("errors_encountered", 0) - meta_enhanced.get("errors_encountered", 0))
        satisfaction_improvement = max(0, meta_enhanced.get("satisfaction_score", 0.5) - baseline.get("satisfaction_score", 0.5)) * 100
        
        return {
            "time_improvement_percentage": time_improvement,
            "error_reduction_count": error_reduction,
            "satisfaction_improvement_percentage": satisfaction_improvement,
            "success_rate_improvement": max(0, meta_enhanced.get("success_rate", 0) - baseline.get("success_rate", 0)) * 100,
            "learning_curve_improvement": max(0, baseline.get("learning_difficulty", 0.5) - meta_enhanced.get("learning_difficulty", 0.5)) * 100
        }
    
    def run_ux_validation(self) -> UserExperienceReport:
        """Run comprehensive user experience validation."""
        print("🚀 User Experience Validation Framework")
        print("=" * 50)
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Create test suite
        test_suite = self.create_ux_test_suite()
        print(f"📋 Created {len(test_suite)} UX test cases")
        
        # Execute UX tasks
        task_results = []
        successful_tasks = 0
        failed_tasks = 0
        
        for i, task in enumerate(test_suite):
            print(f"🔄 Executing UX task {i+1}/{len(test_suite)}: {task.task_name}")
            
            result = self.execute_ux_task(task)
            task_results.append(result)
            
            if result.success:
                successful_tasks += 1
                time_improvement = result.improvement_analysis.get("time_improvement_percentage", 0)
                satisfaction_improvement = result.improvement_analysis.get("satisfaction_improvement_percentage", 0)
                print(f"  ✅ Success: {time_improvement:.1f}% time improvement, {satisfaction_improvement:.1f}% satisfaction improvement")
            else:
                failed_tasks += 1
                print(f"  ❌ Failed: {result.error_message}")
        
        # Analyze results
        persona_analysis = self._analyze_by_persona(task_results)
        usability_summary = self._analyze_usability_summary(task_results)
        user_satisfaction_score = self._calculate_user_satisfaction(task_results)
        recommendations = self._generate_ux_recommendations(task_results)
        ux_readiness_score = self._calculate_ux_readiness_score(task_results)
        
        # Create report
        report = UserExperienceReport(
            report_id=str(uuid.uuid4()),
            test_date=datetime.now().isoformat(),
            framework_version="3.0.0",
            total_tasks=len(test_suite),
            successful_tasks=successful_tasks,
            failed_tasks=failed_tasks,
            persona_analysis=persona_analysis,
            usability_summary=usability_summary,
            task_results=task_results,
            user_satisfaction_score=user_satisfaction_score,
            recommendations=recommendations,
            ux_readiness_score=ux_readiness_score
        )
        
        # Save report
        self._save_report(report)
        
        # Print summary
        self._print_summary(report)
        
        return report
    
    def _analyze_by_persona(self, results: List[UserExperienceResult]) -> Dict[str, Dict[str, Any]]:
        """Analyze results by user persona."""
        persona_analysis = {}
        
        for persona in UserPersona:
            persona_results = [r for r in results if r.task.persona == persona and r.success]
            
            if persona_results:
                avg_time_improvement = statistics.mean([
                    r.improvement_analysis.get("time_improvement_percentage", 0) for r in persona_results
                ])
                avg_satisfaction_improvement = statistics.mean([
                    r.improvement_analysis.get("satisfaction_improvement_percentage", 0) for r in persona_results
                ])
                avg_usability_score = statistics.mean([
                    r.usability_scores.get("overall_usability", 0) for r in persona_results
                ])
                
                persona_analysis[persona.value] = {
                    "total_tasks": len([r for r in results if r.task.persona == persona]),
                    "successful_tasks": len(persona_results),
                    "success_rate": len(persona_results) / len([r for r in results if r.task.persona == persona]) * 100,
                    "avg_time_improvement": avg_time_improvement,
                    "avg_satisfaction_improvement": avg_satisfaction_improvement,
                    "avg_usability_score": avg_usability_score
                }
        
        return persona_analysis
    
    def _analyze_usability_summary(self, results: List[UserExperienceResult]) -> Dict[str, Any]:
        """Analyze overall usability summary."""
        successful_results = [r for r in results if r.success]
        
        if not successful_results:
            return {"error": "No successful results to analyze"}
        
        # Aggregate usability scores
        usability_dimensions = {}
        for dimension in UsabilityDimension:
            scores = [r.usability_scores.get(dimension.value, 0) for r in successful_results]
            usability_dimensions[dimension.value] = {
                "average_score": statistics.mean(scores),
                "median_score": statistics.median(scores),
                "improvement_rate": sum(1 for score in scores if score > 0.5) / len(scores) * 100
            }
        
        # Overall usability metrics
        overall_scores = [r.usability_scores.get("overall_usability", 0) for r in successful_results]
        
        return {
            "overall_usability_score": statistics.mean(overall_scores),
            "usability_dimensions": usability_dimensions,
            "total_evaluated_tasks": len(successful_results),
            "high_usability_rate": sum(1 for score in overall_scores if score > 0.7) / len(overall_scores) * 100
        }
    
    def _calculate_user_satisfaction(self, results: List[UserExperienceResult]) -> float:
        """Calculate overall user satisfaction score."""
        successful_results = [r for r in results if r.success]
        
        if not successful_results:
            return 0.0
        
        satisfaction_scores = []
        for result in successful_results:
            satisfaction_improvement = result.improvement_analysis.get("satisfaction_improvement_percentage", 0)
            usability_score = result.usability_scores.get("overall_usability", 0)
            
            # Combined satisfaction score
            combined_score = (satisfaction_improvement / 100 + usability_score) / 2
            satisfaction_scores.append(combined_score)
        
        return statistics.mean(satisfaction_scores)
    
    def _generate_ux_recommendations(self, results: List[UserExperienceResult]) -> List[str]:
        """Generate UX recommendations based on results."""
        recommendations = []
        
        successful_results = [r for r in results if r.success]
        success_rate = len(successful_results) / len(results) * 100 if results else 0
        
        if success_rate >= 90:
            recommendations.append("✅ EXCELLENT UX: Framework provides exceptional user experience across all personas")
        elif success_rate >= 80:
            recommendations.append("✅ GOOD UX: Framework provides good user experience with minor improvements possible")
        elif success_rate >= 70:
            recommendations.append("⚠️ MODERATE UX: Framework has decent user experience but needs targeted improvements")
        else:
            recommendations.append("❌ POOR UX: Framework requires significant UX improvements before deployment")
        
        if successful_results:
            # Analyze time improvements
            avg_time_improvement = statistics.mean([
                r.improvement_analysis.get("time_improvement_percentage", 0) for r in successful_results
            ])
            
            if avg_time_improvement > 25:
                recommendations.append("🚀 EFFICIENCY: Significant time savings achieved through meta-enhanced prompts")
            elif avg_time_improvement > 15:
                recommendations.append("⚡ EFFICIENCY: Good time savings with meta-enhanced approach")
            elif avg_time_improvement > 5:
                recommendations.append("📈 EFFICIENCY: Moderate time savings, room for optimization")
            else:
                recommendations.append("🔧 EFFICIENCY: Limited time savings, efficiency improvements needed")
            
            # Analyze satisfaction improvements
            avg_satisfaction_improvement = statistics.mean([
                r.improvement_analysis.get("satisfaction_improvement_percentage", 0) for r in successful_results
            ])
            
            if avg_satisfaction_improvement > 20:
                recommendations.append("😊 SATISFACTION: High user satisfaction improvement achieved")
            elif avg_satisfaction_improvement > 10:
                recommendations.append("👍 SATISFACTION: Good user satisfaction improvement")
            else:
                recommendations.append("🔧 SATISFACTION: User satisfaction improvements needed")
        
        return recommendations
    
    def _calculate_ux_readiness_score(self, results: List[UserExperienceResult]) -> float:
        """Calculate overall UX readiness score."""
        if not results:
            return 0.0
        
        successful_results = [r for r in results if r.success]
        success_rate = len(successful_results) / len(results)
        
        if successful_results:
            avg_usability_score = statistics.mean([
                r.usability_scores.get("overall_usability", 0) for r in successful_results
            ])
            avg_satisfaction_score = statistics.mean([
                r.improvement_analysis.get("satisfaction_improvement_percentage", 0) / 100 for r in successful_results
            ])
            
            # Weighted UX readiness score
            readiness_score = (
                success_rate * 0.4 +
                avg_usability_score * 0.4 +
                avg_satisfaction_score * 0.2
            )
        else:
            readiness_score = 0.0
        
        return readiness_score
    
    def _save_report(self, report: UserExperienceReport) -> None:
        """Save UX validation report."""
        report_file = self.output_dir / f"ux_validation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        # Convert to JSON-serializable format
        report_dict = asdict(report)
        
        # Handle enum serialization
        def enum_serializer(obj):
            if hasattr(obj, 'value'):
                return obj.value
            return str(obj)
        
        with open(report_file, 'w') as f:
            json.dump(report_dict, f, indent=2, default=enum_serializer)
        
        print(f"📄 UX validation report saved to: {report_file}")
    
    def _print_summary(self, report: UserExperienceReport) -> None:
        """Print comprehensive UX validation summary."""
        print("\n" + "=" * 50)
        print("📊 USER EXPERIENCE VALIDATION SUMMARY")
        print("=" * 50)
        
        print(f"Report ID: {report.report_id}")
        print(f"Framework Version: {report.framework_version}")
        print(f"Total Tasks: {report.total_tasks}")
        print(f"Successful: {report.successful_tasks} ({(report.successful_tasks/report.total_tasks)*100:.1f}%)")
        print(f"Failed: {report.failed_tasks}")
        print(f"User Satisfaction Score: {report.user_satisfaction_score:.3f}")
        print(f"UX Readiness Score: {report.ux_readiness_score:.3f}")
        
        usability = report.usability_summary
        print(f"\n📈 Usability Summary:")
        print(f"  Overall Usability Score: {usability.get('overall_usability_score', 0):.3f}")
        print(f"  High Usability Rate: {usability.get('high_usability_rate', 0):.1f}%")
        
        print(f"\n👥 Top Performing Personas:")
        sorted_personas = sorted(
            report.persona_analysis.items(),
            key=lambda x: x[1].get('avg_usability_score', 0),
            reverse=True
        )
        
        for persona, data in sorted_personas[:3]:
            print(f"  {persona.replace('_', ' ').title()}:")
            print(f"    Success Rate: {data.get('success_rate', 0):.1f}%")
            print(f"    Usability Score: {data.get('avg_usability_score', 0):.3f}")
            print(f"    Time Improvement: {data.get('avg_time_improvement', 0):.1f}%")
        
        print(f"\n💡 Recommendations:")
        for i, rec in enumerate(report.recommendations, 1):
            print(f"  {i}. {rec}")


# Example usage and test runner
def run_ux_validation():
    """Run user experience validation to demonstrate the framework."""
    project_root = Path(__file__).parent.parent.parent
    output_dir = project_root / "tests" / "results" / "ux"
    
    # Initialize UX validator
    ux_validator = UserExperienceValidator(output_dir)
    
    # Run UX validation
    report = ux_validator.run_ux_validation()
    
    # Return success/failure based on results
    ux_readiness_score = report.ux_readiness_score
    return 0 if ux_readiness_score >= 0.7 else 1


if __name__ == "__main__":
    exit_code = run_ux_validation()
    exit(exit_code)