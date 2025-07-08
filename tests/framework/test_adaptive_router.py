"""Test adaptive router functionality.

This test suite validates the adaptive router module that provides learning-based
command routing with pattern recognition and performance optimization.
"""

import pytest
from pathlib import Path
import xml.etree.ElementTree as ET


class TestAdaptiveRouter:
    """Test suite for adaptive router module."""
    
    @pytest.fixture
    def adaptive_router_path(self):
        """Get adaptive router module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "meta" / "adaptive-router.md"
    
    def test_adaptive_router_module_exists(self, adaptive_router_path):
        """Test that adaptive router module exists."""
        assert adaptive_router_path.exists(), \
            "adaptive-router.md module missing"
        assert adaptive_router_path.stat().st_size > 0, \
            "adaptive-router.md module is empty"
    
    def test_adaptive_router_has_learning_architecture(self, adaptive_router_path):
        """Test that adaptive router has learning architecture."""
        content = adaptive_router_path.read_text()
        assert "<learning_architecture" in content, \
            "Adaptive router missing learning_architecture section"
        assert "<usage_analysis>" in content, \
            "Adaptive router missing usage_analysis"
        assert "<pattern_detection>" in content, \
            "Adaptive router missing pattern_detection"
    
    def test_adaptive_router_has_enhanced_routing_logic(self, adaptive_router_path):
        """Test that adaptive router has enhanced routing logic."""
        content = adaptive_router_path.read_text()
        assert "<enhanced_routing_logic" in content, \
            "Adaptive router missing enhanced_routing_logic section"
        assert "<intelligent_analysis>" in content, \
            "Adaptive router missing intelligent_analysis"
        assert "<routing_optimization>" in content, \
            "Adaptive router missing routing_optimization"
    
    def test_adaptive_router_has_pattern_recognition_engine(self, adaptive_router_path):
        """Test that adaptive router has pattern recognition engine."""
        content = adaptive_router_path.read_text()
        assert "<pattern_recognition_engine" in content, \
            "Adaptive router missing pattern_recognition_engine section"
        assert "<usage_pattern_analysis>" in content, \
            "Adaptive router missing usage_pattern_analysis"
        assert "<failure_pattern_analysis>" in content, \
            "Adaptive router missing failure_pattern_analysis"
    
    def test_adaptive_router_has_performance_targets(self, adaptive_router_path):
        """Test that adaptive router has performance targets."""
        content = adaptive_router_path.read_text()
        assert "<performance_optimization" in content, \
            "Adaptive router missing performance_optimization section"
        assert "<efficiency_improvements>" in content, \
            "Adaptive router missing efficiency_improvements"
        assert "95%" in content, \
            "Adaptive router missing 95% accuracy target"
        assert "30%" in content, \
            "Adaptive router missing 30% efficiency target"
    
    def test_adaptive_router_has_safety_integration(self, adaptive_router_path):
        """Test that adaptive router has safety integration."""
        content = adaptive_router_path.read_text()
        assert "<safety_integration" in content, \
            "Adaptive router missing safety_integration section"
        assert "<boundary_enforcement>" in content, \
            "Adaptive router missing boundary_enforcement"
        assert "<learning_boundaries>" in content, \
            "Adaptive router missing learning_boundaries"
        assert "95% confidence" in content, \
            "Adaptive router missing confidence requirements"
    
    def test_adaptive_router_has_learning_integration(self, adaptive_router_path):
        """Test that adaptive router has learning integration."""
        content = adaptive_router_path.read_text()
        assert "<learning_integration" in content, \
            "Adaptive router missing learning_integration section"
        assert "<data_collection>" in content, \
            "Adaptive router missing data_collection"
        assert "<continuous_learning>" in content, \
            "Adaptive router missing continuous_learning"
    
    def test_adaptive_router_has_usage_examples(self, adaptive_router_path):
        """Test that adaptive router has usage examples."""
        content = adaptive_router_path.read_text()
        assert "<usage_examples>" in content, \
            "Adaptive router missing usage_examples section"
        assert "Learning from Success" in content, \
            "Adaptive router missing success example"
        assert "Failure Recovery" in content, \
            "Adaptive router missing failure recovery example"
    
    def test_adaptive_router_has_interface_contracts(self, adaptive_router_path):
        """Test that adaptive router has interface contracts."""
        content = adaptive_router_path.read_text()
        assert "<integration_contracts>" in content, \
            "Adaptive router missing integration_contracts section"
        assert "<input_requirements>" in content, \
            "Adaptive router missing input_requirements"
        assert "<output_specifications>" in content, \
            "Adaptive router missing output_specifications"
    
    def test_adaptive_router_has_dependencies(self, adaptive_router_path):
        """Test that adaptive router has proper dependencies."""
        content = adaptive_router_path.read_text()
        assert "<depends_on>" in content, \
            "Adaptive router missing depends_on section"
        assert "meta/safety-validator.md" in content, \
            "Adaptive router missing safety validator dependency"
        assert "meta/human-oversight.md" in content, \
            "Adaptive router missing human oversight dependency"
        assert "patterns/intelligent-routing.md" in content, \
            "Adaptive router missing intelligent routing dependency"


class TestAdaptiveRouterFunctionality:
    """Test suite for adaptive router functionality validation."""
    
    @pytest.fixture
    def adaptive_router_path(self):
        """Get adaptive router module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "meta" / "adaptive-router.md"
    
    def test_adaptive_routing_decision_tree_exists(self, adaptive_router_path):
        """Test that adaptive routing decision tree exists."""
        content = adaptive_router_path.read_text()
        assert "<adaptive_decision_tree>" in content, \
            "Adaptive router missing adaptive_decision_tree section"
        assert "<learning_factors>" in content, \
            "Adaptive router missing learning_factors"
        assert "<adaptive_thresholds>" in content, \
            "Adaptive router missing adaptive_thresholds"
    
    def test_adaptive_router_has_command_frequency_analysis(self, adaptive_router_path):
        """Test that adaptive router has command frequency analysis."""
        content = adaptive_router_path.read_text()
        assert "<command_frequency>" in content, \
            "Adaptive router missing command_frequency section"
        assert "/task (45%)" in content, \
            "Adaptive router missing task command frequency"
        assert "/query (25%)" in content, \
            "Adaptive router missing query command frequency"
    
    def test_adaptive_router_has_workflow_patterns(self, adaptive_router_path):
        """Test that adaptive router has workflow patterns."""
        content = adaptive_router_path.read_text()
        assert "<workflow_patterns>" in content, \
            "Adaptive router missing workflow_patterns section"
        assert "<common_sequences>" in content, \
            "Adaptive router missing common_sequences"
        assert "/query → /task" in content, \
            "Adaptive router missing research-then-implement pattern"
    
    def test_adaptive_router_has_confidence_scoring(self, adaptive_router_path):
        """Test that adaptive router has confidence scoring."""
        content = adaptive_router_path.read_text()
        assert "<confidence_scoring>" in content, \
            "Adaptive router missing confidence_scoring references"
        assert "80% confidence" in content, \
            "Adaptive router missing 80% confidence threshold"
        assert "95% confidence" in content, \
            "Adaptive router missing 95% confidence requirement"
    
    def test_adaptive_router_has_optimization_opportunities(self, adaptive_router_path):
        """Test that adaptive router has optimization opportunities."""
        content = adaptive_router_path.read_text()
        assert "<optimization_opportunities>" in content, \
            "Adaptive router missing optimization_opportunities section"
        assert "/research-task compound command" in content, \
            "Adaptive router missing compound command optimization"
        assert "automatic documentation generation" in content, \
            "Adaptive router missing auto-documentation optimization"
    
    def test_adaptive_router_has_evolutionary_features(self, adaptive_router_path):
        """Test that adaptive router has evolutionary features."""
        content = adaptive_router_path.read_text()
        assert "Self-Evolving" in content, \
            "Adaptive router missing self-evolving capabilities"
        assert "learning capabilities" in content, \
            "Adaptive router missing learning capabilities"
        assert "improves routing decisions" in content, \
            "Adaptive router missing routing improvement"


class TestAdaptiveRouterIntegration:
    """Test suite for adaptive router integration validation."""
    
    @pytest.fixture
    def commands_dir(self):
        """Get the commands directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "commands"
    
    @pytest.fixture
    def auto_command_path(self):
        """Get auto command path."""
        return Path(__file__).parent.parent.parent / ".claude" / "commands" / "auto.md"
    
    @pytest.fixture
    def adaptive_router_path(self):
        """Get adaptive router module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "meta" / "adaptive-router.md"
    
    def test_auto_command_references_adaptive_router(self, auto_command_path):
        """Test that auto command references adaptive router."""
        content = auto_command_path.read_text()
        assert "adaptive" in content.lower() or "learning" in content.lower(), \
            "Auto command missing adaptive router integration"
    
    def test_auto_command_has_intelligence_routing(self, auto_command_path):
        """Test that auto command has intelligence routing."""
        content = auto_command_path.read_text()
        assert "intelligence" in content.lower() or "intelligent" in content.lower(), \
            "Auto command missing intelligent routing features"
    
    def test_adaptive_router_revolutionary_transformation(self, adaptive_router_path):
        """Test that adaptive router describes revolutionary transformation."""
        content = adaptive_router_path.read_text()
        assert "Revolutionary" in content, \
            "Adaptive router missing revolutionary description"
        assert "static `/auto` command" in content, \
            "Adaptive router missing static command reference"
        assert "learning, adaptive router" in content, \
            "Adaptive router missing learning transformation"


class TestAdaptiveRouterPerformance:
    """Test suite for adaptive router performance validation."""
    
    @pytest.fixture
    def adaptive_router_path(self):
        """Get adaptive router module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "meta" / "adaptive-router.md"
    
    def test_adaptive_router_has_efficiency_improvements(self, adaptive_router_path):
        """Test that adaptive router has efficiency improvements."""
        content = adaptive_router_path.read_text()
        assert "<efficiency_improvements>" in content, \
            "Adaptive router missing efficiency_improvements section"
        assert "30%" in content, \
            "Adaptive router missing 30% improvement target"
        assert "95%" in content, \
            "Adaptive router missing 95% accuracy target"
    
    def test_adaptive_router_has_user_experience_enhancement(self, adaptive_router_path):
        """Test that adaptive router has user experience enhancement."""
        content = adaptive_router_path.read_text()
        assert "<user_experience_enhancement>" in content, \
            "Adaptive router missing user_experience_enhancement section"
        assert "<intelligent_suggestions>" in content, \
            "Adaptive router missing intelligent_suggestions"
        assert "<context_awareness>" in content, \
            "Adaptive router missing context_awareness"
    
    def test_adaptive_router_has_predictive_capabilities(self, adaptive_router_path):
        """Test that adaptive router has predictive capabilities."""
        content = adaptive_router_path.read_text()
        assert "predictive" in content.lower(), \
            "Adaptive router missing predictive capabilities"
        assert "anticipate" in content.lower(), \
            "Adaptive router missing anticipation features"
        assert "pre-optimize" in content.lower(), \
            "Adaptive router missing pre-optimization features"
    
    def test_adaptive_router_has_learning_cycles(self, adaptive_router_path):
        """Test that adaptive router has learning cycles."""
        content = adaptive_router_path.read_text()
        assert "<learning_cycles>" in content, \
            "Adaptive router missing learning_cycles section"
        assert "short_term" in content, \
            "Adaptive router missing short-term learning"
        assert "medium_term" in content, \
            "Adaptive router missing medium-term learning"
        assert "long_term" in content, \
            "Adaptive router missing long-term learning"
        assert "meta_learning" in content, \
            "Adaptive router missing meta-learning"