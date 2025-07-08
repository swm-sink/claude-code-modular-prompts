"""Test framework selector functionality.

This test suite validates the framework selector module that provides
94.2% routing accuracy for intelligent framework selection.
"""

import pytest
from pathlib import Path
import xml.etree.ElementTree as ET


class TestFrameworkSelector:
    """Test suite for framework selector module."""
    
    @pytest.fixture
    def framework_selector_path(self):
        """Get framework selector module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "frameworks" / "framework-selector.md"
    
    def test_framework_selector_module_exists(self, framework_selector_path):
        """Test that framework selector module exists."""
        assert framework_selector_path.exists(), \
            "framework-selector.md module missing"
        assert framework_selector_path.stat().st_size > 0, \
            "framework-selector.md module is empty"
    
    def test_framework_selector_has_selection_engine(self, framework_selector_path):
        """Test that framework selector has selection engine."""
        content = framework_selector_path.read_text()
        assert "<selection_engine" in content, \
            "Framework selector missing selection_engine section"
        assert "<framework_analysis>" in content, \
            "Framework selector missing framework_analysis"
        assert "<selection_criteria>" in content, \
            "Framework selector missing selection_criteria"
        assert "<routing_logic>" in content, \
            "Framework selector missing routing_logic"
    
    def test_framework_selector_has_framework_database(self, framework_selector_path):
        """Test that framework selector has framework database."""
        content = framework_selector_path.read_text()
        assert "<framework_database" in content, \
            "Framework selector missing framework_database section"
        assert "<framework_definitions>" in content, \
            "Framework selector missing framework_definitions"
        assert "<framework_capabilities>" in content, \
            "Framework selector missing framework_capabilities"
        assert "<framework_performance>" in content, \
            "Framework selector missing framework_performance"
    
    def test_framework_selector_has_accuracy_metrics(self, framework_selector_path):
        """Test that framework selector has accuracy metrics."""
        content = framework_selector_path.read_text()
        assert "<accuracy_metrics" in content, \
            "Framework selector missing accuracy_metrics section"
        assert "94.2%" in content, \
            "Framework selector missing 94.2% accuracy target"
        assert "routing_accuracy" in content, \
            "Framework selector missing routing_accuracy metric"
    
    def test_framework_selector_has_learning_system(self, framework_selector_path):
        """Test that framework selector has learning system."""
        content = framework_selector_path.read_text()
        assert "<learning_system" in content, \
            "Framework selector missing learning_system section"
        assert "<selection_learning>" in content, \
            "Framework selector missing selection_learning"
        assert "<performance_tracking>" in content, \
            "Framework selector missing performance_tracking"
        assert "<adaptation_engine>" in content, \
            "Framework selector missing adaptation_engine"
    
    def test_framework_selector_has_framework_support(self, framework_selector_path):
        """Test that framework selector has framework support."""
        content = framework_selector_path.read_text()
        assert "RISE" in content, \
            "Framework selector missing RISE framework"
        assert "TRACE" in content, \
            "Framework selector missing TRACE framework"
        assert "CARE" in content, \
            "Framework selector missing CARE framework"
        assert "APE" in content, \
            "Framework selector missing APE framework"
    
    def test_framework_selector_has_integration_points(self, framework_selector_path):
        """Test that framework selector has integration points."""
        content = framework_selector_path.read_text()
        assert "<integration_points>" in content, \
            "Framework selector missing integration_points section"
        assert "<depends_on>" in content, \
            "Framework selector missing depends_on"
        assert "<provides_to>" in content, \
            "Framework selector missing provides_to"


class TestFrameworkSelectionLogic:
    """Test suite for framework selection logic validation."""
    
    @pytest.fixture
    def framework_selector_path(self):
        """Get framework selector module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "frameworks" / "framework-selector.md"
    
    def test_framework_selector_has_context_analysis(self, framework_selector_path):
        """Test that framework selector has context analysis."""
        content = framework_selector_path.read_text()
        assert "<context_analysis>" in content, \
            "Framework selector missing context_analysis section"
        assert "<task_complexity>" in content, \
            "Framework selector missing task_complexity"
        assert "<requirement_analysis>" in content, \
            "Framework selector missing requirement_analysis"
        assert "<user_preferences>" in content, \
            "Framework selector missing user_preferences"
    
    def test_framework_selector_has_selection_criteria(self, framework_selector_path):
        """Test that framework selector has selection criteria."""
        content = framework_selector_path.read_text()
        assert "<selection_criteria>" in content, \
            "Framework selector missing selection_criteria section"
        assert "<complexity_matching>" in content, \
            "Framework selector missing complexity_matching"
        assert "<performance_requirements>" in content, \
            "Framework selector missing performance_requirements"
        assert "<success_probability>" in content, \
            "Framework selector missing success_probability"
    
    def test_framework_selector_has_routing_algorithm(self, framework_selector_path):
        """Test that framework selector has routing algorithm."""
        content = framework_selector_path.read_text()
        assert "<routing_algorithm>" in content, \
            "Framework selector missing routing_algorithm section"
        assert "<decision_tree>" in content, \
            "Framework selector missing decision_tree"
        assert "<confidence_scoring>" in content, \
            "Framework selector missing confidence_scoring"
        assert "<fallback_logic>" in content, \
            "Framework selector missing fallback_logic"
    
    def test_framework_selector_has_optimization_strategies(self, framework_selector_path):
        """Test that framework selector has optimization strategies."""
        content = framework_selector_path.read_text()
        assert "<optimization_strategies>" in content, \
            "Framework selector missing optimization_strategies section"
        assert "<selection_speed>" in content, \
            "Framework selector missing selection_speed"
        assert "<accuracy_optimization>" in content, \
            "Framework selector missing accuracy_optimization"
        assert "<adaptive_improvement>" in content, \
            "Framework selector missing adaptive_improvement"
    
    def test_framework_selector_has_validation_system(self, framework_selector_path):
        """Test that framework selector has validation system."""
        content = framework_selector_path.read_text()
        assert "<validation_system>" in content, \
            "Framework selector missing validation_system section"
        assert "<selection_validation>" in content, \
            "Framework selector missing selection_validation"
        assert "<performance_validation>" in content, \
            "Framework selector missing performance_validation"
        assert "<accuracy_tracking>" in content, \
            "Framework selector missing accuracy_tracking"


class TestFrameworkSelectionIntegration:
    """Test suite for framework selection integration validation."""
    
    @pytest.fixture
    def framework_selector_path(self):
        """Get framework selector module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "frameworks" / "framework-selector.md"
    
    @pytest.fixture
    def frameworks_dir(self):
        """Get the frameworks directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "frameworks"
    
    def test_framework_selector_has_adaptive_integration(self, framework_selector_path):
        """Test that framework selector has adaptive integration."""
        content = framework_selector_path.read_text()
        assert "<adaptive_integration>" in content, \
            "Framework selector missing adaptive_integration section"
        assert "meta/adaptive-router.md" in content, \
            "Framework selector missing adaptive router integration"
        assert "<learning_integration>" in content, \
            "Framework selector missing learning_integration"
    
    def test_framework_selector_has_performance_integration(self, framework_selector_path):
        """Test that framework selector has performance integration."""
        content = framework_selector_path.read_text()
        assert "<performance_integration>" in content, \
            "Framework selector missing performance_integration section"
        assert "meta/performance-optimizer.md" in content, \
            "Framework selector missing performance optimizer integration"
        assert "<selection_optimization>" in content, \
            "Framework selector missing selection_optimization"
    
    def test_framework_selector_has_safety_integration(self, framework_selector_path):
        """Test that framework selector has safety integration."""
        content = framework_selector_path.read_text()
        assert "<safety_integration>" in content, \
            "Framework selector missing safety_integration section"
        assert "meta/safety-validator.md" in content, \
            "Framework selector missing safety validator integration"
        assert "<safe_selection>" in content, \
            "Framework selector missing safe_selection"
    
    def test_framework_selector_has_framework_integration(self, framework_selector_path):
        """Test that framework selector has framework integration."""
        content = framework_selector_path.read_text()
        assert "<framework_integration>" in content, \
            "Framework selector missing framework_integration section"
        assert "frameworks/rise.md" in content, \
            "Framework selector missing RISE framework integration"
        assert "frameworks/trace.md" in content, \
            "Framework selector missing TRACE framework integration"
        assert "frameworks/care.md" in content, \
            "Framework selector missing CARE framework integration"
    
    def test_framework_selector_has_command_integration(self, framework_selector_path):
        """Test that framework selector has command integration."""
        content = framework_selector_path.read_text()
        assert "<command_integration>" in content, \
            "Framework selector missing command_integration section"
        assert "<command_routing>" in content, \
            "Framework selector missing command_routing"
        assert "<workflow_optimization>" in content, \
            "Framework selector missing workflow_optimization"


class TestFrameworkSelectionPerformance:
    """Test suite for framework selection performance validation."""
    
    @pytest.fixture
    def framework_selector_path(self):
        """Get framework selector module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "frameworks" / "framework-selector.md"
    
    def test_framework_selector_has_accuracy_targets(self, framework_selector_path):
        """Test that framework selector has accuracy targets."""
        content = framework_selector_path.read_text()
        assert "<accuracy_targets>" in content, \
            "Framework selector missing accuracy_targets section"
        assert "94.2%" in content, \
            "Framework selector missing 94.2% accuracy target"
        assert "selection_accuracy" in content, \
            "Framework selector missing selection_accuracy metric"
    
    def test_framework_selector_has_performance_metrics(self, framework_selector_path):
        """Test that framework selector has performance metrics."""
        content = framework_selector_path.read_text()
        assert "<performance_metrics>" in content, \
            "Framework selector missing performance_metrics section"
        assert "<selection_speed>" in content, \
            "Framework selector missing selection_speed"
        assert "<routing_efficiency>" in content, \
            "Framework selector missing routing_efficiency"
    
    def test_framework_selector_has_learning_effectiveness(self, framework_selector_path):
        """Test that framework selector has learning effectiveness."""
        content = framework_selector_path.read_text()
        assert "<learning_effectiveness>" in content, \
            "Framework selector missing learning_effectiveness section"
        assert "<improvement_rate>" in content, \
            "Framework selector missing improvement_rate"
        assert "<adaptation_speed>" in content, \
            "Framework selector missing adaptation_speed"
    
    def test_framework_selector_has_success_tracking(self, framework_selector_path):
        """Test that framework selector has success tracking."""
        content = framework_selector_path.read_text()
        assert "<success_tracking>" in content, \
            "Framework selector missing success_tracking section"
        assert "<selection_success_rate>" in content, \
            "Framework selector missing selection_success_rate"
        assert "<user_satisfaction>" in content, \
            "Framework selector missing user_satisfaction"
    
    def test_framework_selector_has_evolutionary_features(self, framework_selector_path):
        """Test that framework selector has evolutionary features."""
        content = framework_selector_path.read_text()
        assert "Intelligent Router" in content, \
            "Framework selector missing intelligent router capabilities"
        assert "learns from selection" in content, \
            "Framework selector missing learning from selection"
        assert "routing accuracy" in content, \
            "Framework selector missing routing accuracy"