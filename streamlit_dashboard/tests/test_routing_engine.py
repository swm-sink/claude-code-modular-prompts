"""
TDD Tests for AI-Powered Routing Recommendation Engine
RED PHASE: Write failing tests first
"""

import pytest
from unittest.mock import MagicMock, patch
from typing import Dict, List, Any, Optional
from pathlib import Path

# Import the component we're going to build
try:
    from components.routing_engine import (
        RoutingEngine, 
        RoutingRecommendation, 
        UserContext, 
        ProjectAnalyzer,
        RoutingDecisionTree,
        RoutingRule
    )
except ImportError:
    # These don't exist yet - we'll create them
    RoutingEngine = None
    RoutingRecommendation = None
    UserContext = None
    ProjectAnalyzer = None
    RoutingDecisionTree = None
    RoutingRule = None


class TestRoutingRecommendation:
    """Test the RoutingRecommendation data class"""
    
    def test_recommendation_creation(self):
        """Test RoutingRecommendation can be created with proper data"""
        if RoutingRecommendation is None:
            pytest.skip("RoutingRecommendation not implemented yet")
        
        recommendation = RoutingRecommendation(
            command="/task",
            confidence=0.85,
            reasoning="Single file change detected with existing tests",
            context_factors=["file_count_low", "tests_exist", "clear_scope"],
            alternative_commands=["/feature", "/auto"],
            parameters={"file_focus": "src/utils.py"}
        )
        
        assert recommendation.command == "/task"
        assert recommendation.confidence == 0.85
        assert "Single file change" in recommendation.reasoning
        assert len(recommendation.context_factors) == 3
        assert "/feature" in recommendation.alternative_commands
        assert recommendation.parameters["file_focus"] == "src/utils.py"
    
    def test_recommendation_validation(self):
        """Test recommendation validation"""
        if RoutingRecommendation is None:
            pytest.skip("RoutingRecommendation not implemented yet")
        
        # Test invalid confidence
        with pytest.raises(ValueError):
            RoutingRecommendation(
                command="/task",
                confidence=1.5,  # Invalid - must be 0-1
                reasoning="Test"
            )
        
        # Test invalid command
        with pytest.raises(ValueError):
            RoutingRecommendation(
                command="task",  # Invalid - must start with /
                confidence=0.8,
                reasoning="Test"
            )
    
    def test_recommendation_serialization(self):
        """Test recommendation serialization"""
        if RoutingRecommendation is None:
            pytest.skip("RoutingRecommendation not implemented yet")
        
        recommendation = RoutingRecommendation(
            command="/task",
            confidence=0.85,
            reasoning="Test reasoning",
            context_factors=["test_factor"],
            alternative_commands=["/feature"],
            parameters={"test": "value"}
        )
        
        # Test to_dict
        data = recommendation.to_dict()
        assert isinstance(data, dict)
        assert data["command"] == "/task"
        assert data["confidence"] == 0.85
        
        # Test from_dict
        recreated = RoutingRecommendation.from_dict(data)
        assert recreated.command == recommendation.command
        assert recreated.confidence == recommendation.confidence
        assert recreated.reasoning == recommendation.reasoning


class TestUserContext:
    """Test the UserContext data class"""
    
    def test_user_context_creation(self):
        """Test UserContext can be created and populated"""
        if UserContext is None:
            pytest.skip("UserContext not implemented yet")
        
        context = UserContext(
            user_input="Fix the login bug in authentication service",
            project_type="web_application",
            file_count=25,
            test_coverage=85,
            recent_commands=["/task", "/query", "/feature"],
            project_complexity="medium",
            framework_usage={"react": True, "typescript": True},
            time_context="urgent"
        )
        
        assert "login bug" in context.user_input
        assert context.project_type == "web_application"
        assert context.file_count == 25
        assert context.test_coverage == 85
        assert len(context.recent_commands) == 3
        assert context.framework_usage["react"] is True
    
    def test_context_analysis_methods(self):
        """Test context analysis helper methods"""
        if UserContext is None:
            pytest.skip("UserContext not implemented yet")
        
        context = UserContext(
            user_input="Create a new user registration feature",
            project_type="web_application",
            file_count=5,
            test_coverage=95,
            recent_commands=["/task", "/task", "/query"],
            project_complexity="small"
        )
        
        assert context.is_small_project() is True
        assert context.has_high_test_coverage() is True
        assert context.get_dominant_recent_command() == "/task"
        assert context.indicates_new_feature() is True
    
    def test_context_from_project_analysis(self):
        """Test creating context from project analysis"""
        if UserContext is None:
            pytest.skip("UserContext not implemented yet")
        
        project_data = {
            "file_count": 50,
            "test_coverage": 70,
            "project_type": "api",
            "complexity": "medium",
            "frameworks": ["fastapi", "pytest"]
        }
        
        context = UserContext.from_project_analysis(
            user_input="Add authentication endpoint",
            project_data=project_data,
            recent_commands=["/feature", "/task"]
        )
        
        assert context.user_input == "Add authentication endpoint"
        assert context.file_count == 50
        assert context.test_coverage == 70
        assert context.project_type == "api"


class TestProjectAnalyzer:
    """Test the ProjectAnalyzer component"""
    
    @pytest.fixture
    def project_path(self, tmp_path):
        """Create a temporary project structure"""
        project_dir = tmp_path / "test_project"
        project_dir.mkdir()
        
        # Create some files
        (project_dir / "src").mkdir()
        (project_dir / "src" / "main.py").write_text("print('hello')")
        (project_dir / "src" / "utils.py").write_text("def helper(): pass")
        
        (project_dir / "tests").mkdir()
        (project_dir / "tests" / "test_main.py").write_text("def test_main(): pass")
        
        (project_dir / "package.json").write_text('{"name": "test"}')
        
        return project_dir
    
    def test_project_analyzer_initialization(self, project_path):
        """Test ProjectAnalyzer can be initialized"""
        if ProjectAnalyzer is None:
            pytest.skip("ProjectAnalyzer not implemented yet")
        
        analyzer = ProjectAnalyzer(project_path)
        assert analyzer.project_path == project_path
        assert hasattr(analyzer, 'analyze_project_structure')
    
    def test_analyze_project_structure(self, project_path):
        """Test analyzing project structure"""
        if ProjectAnalyzer is None:
            pytest.skip("ProjectAnalyzer not implemented yet")
        
        analyzer = ProjectAnalyzer(project_path)
        analysis = analyzer.analyze_project_structure()
        
        assert isinstance(analysis, dict)
        assert "file_count" in analysis
        assert "test_coverage_estimate" in analysis
        assert "project_type" in analysis
        assert "complexity" in analysis
        assert analysis["file_count"] > 0
    
    def test_detect_project_type(self, project_path):
        """Test detecting project type"""
        if ProjectAnalyzer is None:
            pytest.skip("ProjectAnalyzer not implemented yet")
        
        analyzer = ProjectAnalyzer(project_path)
        project_type = analyzer.detect_project_type()
        
        assert project_type in ["web_application", "api", "library", "script", "unknown"]
    
    def test_analyze_complexity(self, project_path):
        """Test analyzing project complexity"""
        if ProjectAnalyzer is None:
            pytest.skip("ProjectAnalyzer not implemented yet")
        
        analyzer = ProjectAnalyzer(project_path)
        complexity = analyzer.analyze_complexity()
        
        assert complexity in ["small", "medium", "large", "enterprise"]
    
    def test_estimate_test_coverage(self, project_path):
        """Test estimating test coverage"""
        if ProjectAnalyzer is None:
            pytest.skip("ProjectAnalyzer not implemented yet")
        
        analyzer = ProjectAnalyzer(project_path)
        coverage = analyzer.estimate_test_coverage()
        
        assert isinstance(coverage, (int, float))
        assert 0 <= coverage <= 100
    
    def test_identify_frameworks(self, project_path):
        """Test identifying frameworks"""
        if ProjectAnalyzer is None:
            pytest.skip("ProjectAnalyzer not implemented yet")
        
        analyzer = ProjectAnalyzer(project_path)
        frameworks = analyzer.identify_frameworks()
        
        assert isinstance(frameworks, dict)
        # Should detect some frameworks based on files


class TestRoutingRule:
    """Test the RoutingRule component"""
    
    def test_routing_rule_creation(self):
        """Test RoutingRule can be created"""
        if RoutingRule is None:
            pytest.skip("RoutingRule not implemented yet")
        
        rule = RoutingRule(
            name="small_task_rule",
            conditions={
                "file_count": {"max": 10},
                "user_input_keywords": ["fix", "bug", "update"],
                "project_complexity": ["small", "medium"]
            },
            recommendation="/task",
            confidence_base=0.8,
            reasoning_template="Small project with {file_count} files, {keyword_match} indicates focused work"
        )
        
        assert rule.name == "small_task_rule"
        assert rule.recommendation == "/task"
        assert rule.confidence_base == 0.8
        assert "Small project" in rule.reasoning_template
    
    def test_rule_evaluation(self):
        """Test evaluating a rule against context"""
        if RoutingRule is None:
            pytest.skip("RoutingRule not implemented yet")
        
        rule = RoutingRule(
            name="task_rule",
            conditions={
                "file_count": {"max": 5},
                "user_input_keywords": ["fix", "bug"]
            },
            recommendation="/task",
            confidence_base=0.8,
            reasoning_template="Bug fix in small project"
        )
        
        # Context that matches
        matching_context = UserContext(
            user_input="Fix the login bug",
            file_count=3,
            project_complexity="small"
        )
        
        matches, confidence = rule.evaluate(matching_context)
        assert matches is True
        assert confidence > 0.7
        
        # Context that doesn't match
        non_matching_context = UserContext(
            user_input="Create comprehensive dashboard",
            file_count=50,
            project_complexity="large"
        )
        
        matches, confidence = rule.evaluate(non_matching_context)
        assert matches is False
        assert confidence < 0.3


class TestRoutingDecisionTree:
    """Test the RoutingDecisionTree component"""
    
    def test_decision_tree_creation(self):
        """Test RoutingDecisionTree can be created"""
        if RoutingDecisionTree is None:
            pytest.skip("RoutingDecisionTree not implemented yet")
        
        tree = RoutingDecisionTree()
        assert hasattr(tree, 'rules')
        assert hasattr(tree, 'add_rule')
        assert hasattr(tree, 'evaluate')
    
    def test_add_and_evaluate_rules(self):
        """Test adding and evaluating rules"""
        if RoutingDecisionTree is None:
            pytest.skip("RoutingDecisionTree not implemented yet")
        
        tree = RoutingDecisionTree()
        
        # Clear default rules for clean test
        tree.rules = []
        
        # Add a rule
        rule = RoutingRule(
            name="test_rule",
            conditions={"file_count": {"max": 5}},
            recommendation="/task",
            confidence_base=0.8,
            reasoning_template="Small project"
        )
        
        tree.add_rule(rule)
        assert len(tree.rules) == 1
        
        # Evaluate
        context = UserContext(
            user_input="Fix bug",
            file_count=3
        )
        
        recommendations = tree.evaluate(context)
        assert isinstance(recommendations, list)
        assert len(recommendations) > 0
    
    def test_rule_priority_ordering(self):
        """Test that rules are evaluated in priority order"""
        if RoutingDecisionTree is None:
            pytest.skip("RoutingDecisionTree not implemented yet")
        
        tree = RoutingDecisionTree()
        
        # Add rules with different priorities
        high_priority_rule = RoutingRule(
            name="high_priority",
            conditions={"file_count": {"max": 10}},
            recommendation="/task",
            confidence_base=0.9,
            reasoning_template="High priority rule",
            priority=10
        )
        
        low_priority_rule = RoutingRule(
            name="low_priority",
            conditions={"file_count": {"max": 10}},
            recommendation="/feature",
            confidence_base=0.5,
            reasoning_template="Low priority rule",
            priority=1
        )
        
        tree.add_rule(low_priority_rule)
        tree.add_rule(high_priority_rule)
        
        # High priority rule should be evaluated first
        context = UserContext(user_input="Test", file_count=5)
        recommendations = tree.evaluate(context)
        
        assert len(recommendations) >= 1
        assert recommendations[0].command == "/task"  # High priority rule


class TestRoutingEngine:
    """Test the main RoutingEngine component"""
    
    @pytest.fixture
    def framework_path(self, tmp_path):
        """Create a temporary framework directory"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create some basic structure
        commands_dir = framework_dir / "commands"
        commands_dir.mkdir()
        (commands_dir / "task.md").write_text("# Task Command")
        (commands_dir / "feature.md").write_text("# Feature Command")
        (commands_dir / "auto.md").write_text("# Auto Command")
        
        return framework_dir
    
    @pytest.fixture
    def project_path(self, tmp_path):
        """Create a temporary project"""
        project_dir = tmp_path / "project"
        project_dir.mkdir()
        
        # Create basic project structure
        (project_dir / "src").mkdir()
        (project_dir / "src" / "main.py").write_text("print('hello')")
        (project_dir / "tests").mkdir()
        (project_dir / "tests" / "test_main.py").write_text("def test_main(): pass")
        
        return project_dir
    
    def test_routing_engine_initialization(self, framework_path, project_path):
        """Test RoutingEngine can be initialized"""
        if RoutingEngine is None:
            pytest.skip("RoutingEngine not implemented yet")
        
        engine = RoutingEngine(
            framework_path=framework_path,
            project_path=project_path
        )
        
        assert engine.framework_path == framework_path
        assert engine.project_path == project_path
        assert hasattr(engine, 'decision_tree')
        assert hasattr(engine, 'project_analyzer')
    
    def test_get_routing_recommendation(self, framework_path, project_path):
        """Test getting routing recommendation"""
        if RoutingEngine is None:
            pytest.skip("RoutingEngine not implemented yet")
        
        engine = RoutingEngine(
            framework_path=framework_path,
            project_path=project_path
        )
        
        # Test recommendation
        recommendation = engine.get_routing_recommendation(
            user_input="Fix the login bug in authentication",
            recent_commands=["/task", "/query"]
        )
        
        assert isinstance(recommendation, RoutingRecommendation)
        assert recommendation.command.startswith("/")
        assert 0 <= recommendation.confidence <= 1
        assert len(recommendation.reasoning) > 0
    
    def test_multiple_recommendations(self, framework_path, project_path):
        """Test getting multiple routing recommendations"""
        if RoutingEngine is None:
            pytest.skip("RoutingEngine not implemented yet")
        
        engine = RoutingEngine(
            framework_path=framework_path,
            project_path=project_path
        )
        
        # Test multiple recommendations
        recommendations = engine.get_multiple_recommendations(
            user_input="Create a new user management system",
            recent_commands=["/feature", "/task"],
            max_recommendations=3
        )
        
        assert isinstance(recommendations, list)
        assert len(recommendations) <= 3
        assert all(isinstance(r, RoutingRecommendation) for r in recommendations)
        
        # Should be sorted by confidence
        confidences = [r.confidence for r in recommendations]
        assert confidences == sorted(confidences, reverse=True)
    
    def test_learn_from_feedback(self, framework_path, project_path):
        """Test learning from user feedback"""
        if RoutingEngine is None:
            pytest.skip("RoutingEngine not implemented yet")
        
        engine = RoutingEngine(
            framework_path=framework_path,
            project_path=project_path
        )
        
        # Simulate user feedback
        feedback = {
            "user_input": "Fix login bug",
            "recommended_command": "/task",
            "actual_command": "/query",
            "user_rating": 2,  # Poor recommendation
            "context": {
                "file_count": 3,
                "project_complexity": "small"
            }
        }
        
        success = engine.learn_from_feedback(feedback)
        assert success is True
        
        # Engine should adjust future recommendations
        new_recommendation = engine.get_routing_recommendation(
            user_input="Fix login bug",
            recent_commands=[]
        )
        
        # Should have learned from feedback
        assert new_recommendation is not None
    
    def test_explain_recommendation(self, framework_path, project_path):
        """Test explaining recommendation logic"""
        if RoutingEngine is None:
            pytest.skip("RoutingEngine not implemented yet")
        
        engine = RoutingEngine(
            framework_path=framework_path,
            project_path=project_path
        )
        
        recommendation = engine.get_routing_recommendation(
            user_input="Add new feature for user profiles",
            recent_commands=["/feature"]
        )
        
        explanation = engine.explain_recommendation(recommendation)
        
        assert isinstance(explanation, dict)
        assert "decision_path" in explanation
        assert "context_factors" in explanation
        assert "alternative_paths" in explanation
        assert "confidence_breakdown" in explanation
    
    def test_get_available_commands(self, framework_path, project_path):
        """Test getting available commands"""
        if RoutingEngine is None:
            pytest.skip("RoutingEngine not implemented yet")
        
        engine = RoutingEngine(
            framework_path=framework_path,
            project_path=project_path
        )
        
        commands = engine.get_available_commands()
        
        assert isinstance(commands, list)
        assert len(commands) > 0
        assert "/task" in commands
        assert "/feature" in commands
        assert "/auto" in commands
    
    def test_render_routing_ui(self, framework_path, project_path):
        """Test rendering routing UI"""
        if RoutingEngine is None:
            pytest.skip("RoutingEngine not implemented yet")
        
        engine = RoutingEngine(
            framework_path=framework_path,
            project_path=project_path
        )
        
        # Test that the method exists and can be called
        assert hasattr(engine, 'render_routing_ui')
        assert callable(engine.render_routing_ui)
    
    def test_save_and_load_model(self, framework_path, project_path, tmp_path):
        """Test saving and loading routing model"""
        if RoutingEngine is None:
            pytest.skip("RoutingEngine not implemented yet")
        
        engine = RoutingEngine(
            framework_path=framework_path,
            project_path=project_path
        )
        
        # Train with some feedback
        feedback = {
            "user_input": "Fix bug",
            "recommended_command": "/task",
            "actual_command": "/task",
            "user_rating": 5,
            "context": {"file_count": 5}
        }
        engine.learn_from_feedback(feedback)
        
        # Save model
        model_path = tmp_path / "routing_model.json"
        success = engine.save_model(model_path)
        assert success is True
        assert model_path.exists()
        
        # Load model
        new_engine = RoutingEngine(
            framework_path=framework_path,
            project_path=project_path
        )
        success = new_engine.load_model(model_path)
        assert success is True
        
        # Should produce similar recommendations
        original_rec = engine.get_routing_recommendation("Fix bug", [])
        loaded_rec = new_engine.get_routing_recommendation("Fix bug", [])
        
        assert original_rec.command == loaded_rec.command