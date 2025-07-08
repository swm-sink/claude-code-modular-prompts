"""Test safety validator functionality.

This test suite validates the safety validator module that provides
boundary enforcement and safety validation for the meta-framework.
"""

import pytest
from pathlib import Path
import xml.etree.ElementTree as ET


class TestSafetyValidator:
    """Test suite for safety validator module."""
    
    @pytest.fixture
    def safety_validator_path(self):
        """Get safety validator module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "meta" / "safety-validator.md"
    
    def test_safety_validator_module_exists(self, safety_validator_path):
        """Test that safety validator module exists."""
        assert safety_validator_path.exists(), \
            "safety-validator.md module missing"
        assert safety_validator_path.stat().st_size > 0, \
            "safety-validator.md module is empty"
    
    def test_safety_validator_has_boundary_enforcement(self, safety_validator_path):
        """Test that safety validator has boundary enforcement."""
        content = safety_validator_path.read_text()
        assert "<boundary_enforcement" in content, \
            "Safety validator missing boundary_enforcement section"
        assert "<core_stability>" in content, \
            "Safety validator missing core_stability"
        assert "<immutable_core>" in content, \
            "Safety validator missing immutable_core"
    
    def test_safety_validator_has_validation_system(self, safety_validator_path):
        """Test that safety validator has validation system."""
        content = safety_validator_path.read_text()
        assert "<validation_system" in content, \
            "Safety validator missing validation_system section"
        assert "<safety_checks>" in content, \
            "Safety validator missing safety_checks"
        assert "<validation_rules>" in content, \
            "Safety validator missing validation_rules"
        assert "<compliance_verification>" in content, \
            "Safety validator missing compliance_verification"
    
    def test_safety_validator_has_monitoring_system(self, safety_validator_path):
        """Test that safety validator has monitoring system."""
        content = safety_validator_path.read_text()
        assert "<monitoring_system" in content, \
            "Safety validator missing monitoring_system section"
        assert "<real_time_monitoring>" in content, \
            "Safety validator missing real_time_monitoring"
        assert "<safety_metrics>" in content, \
            "Safety validator missing safety_metrics"
        assert "<violation_detection>" in content, \
            "Safety validator missing violation_detection"
    
    def test_safety_validator_has_enforcement_mechanisms(self, safety_validator_path):
        """Test that safety validator has enforcement mechanisms."""
        content = safety_validator_path.read_text()
        assert "<enforcement_mechanisms" in content, \
            "Safety validator missing enforcement_mechanisms section"
        assert "<automatic_enforcement>" in content, \
            "Safety validator missing automatic_enforcement"
        assert "<manual_override>" in content, \
            "Safety validator missing manual_override"
        assert "<emergency_shutdown>" in content, \
            "Safety validator missing emergency_shutdown"
    
    def test_safety_validator_has_rollback_system(self, safety_validator_path):
        """Test that safety validator has rollback system."""
        content = safety_validator_path.read_text()
        assert "<rollback_system" in content, \
            "Safety validator missing rollback_system section"
        assert "<automatic_rollback>" in content, \
            "Safety validator missing automatic_rollback"
        assert "<state_restoration>" in content, \
            "Safety validator missing state_restoration"
        assert "<rollback_validation>" in content, \
            "Safety validator missing rollback_validation"
    
    def test_safety_validator_has_integration_points(self, safety_validator_path):
        """Test that safety validator has integration points."""
        content = safety_validator_path.read_text()
        assert "<integration_points>" in content, \
            "Safety validator missing integration_points section"
        assert "<depends_on>" in content, \
            "Safety validator missing depends_on"
        assert "<provides_to>" in content, \
            "Safety validator missing provides_to"


class TestSafetyValidatorBoundaries:
    """Test suite for safety validator boundaries validation."""
    
    @pytest.fixture
    def safety_validator_path(self):
        """Get safety validator module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "meta" / "safety-validator.md"
    
    def test_safety_validator_has_core_protection(self, safety_validator_path):
        """Test that safety validator has core protection."""
        content = safety_validator_path.read_text()
        assert "<core_protection>" in content, \
            "Safety validator missing core_protection section"
        assert "<immutable_components>" in content, \
            "Safety validator missing immutable_components"
        assert "<protected_operations>" in content, \
            "Safety validator missing protected_operations"
        assert "<stability_guarantees>" in content, \
            "Safety validator missing stability_guarantees"
    
    def test_safety_validator_has_change_validation(self, safety_validator_path):
        """Test that safety validator has change validation."""
        content = safety_validator_path.read_text()
        assert "<change_validation>" in content, \
            "Safety validator missing change_validation section"
        assert "<pre_change_validation>" in content, \
            "Safety validator missing pre_change_validation"
        assert "<post_change_validation>" in content, \
            "Safety validator missing post_change_validation"
        assert "<change_impact_analysis>" in content, \
            "Safety validator missing change_impact_analysis"
    
    def test_safety_validator_has_safety_boundaries(self, safety_validator_path):
        """Test that safety validator has safety boundaries."""
        content = safety_validator_path.read_text()
        assert "<safety_boundaries>" in content, \
            "Safety validator missing safety_boundaries section"
        assert "<framework_boundaries>" in content, \
            "Safety validator missing framework_boundaries"
        assert "<modification_limits>" in content, \
            "Safety validator missing modification_limits"
        assert "<capability_restrictions>" in content, \
            "Safety validator missing capability_restrictions"
    
    def test_safety_validator_has_human_oversight(self, safety_validator_path):
        """Test that safety validator has human oversight."""
        content = safety_validator_path.read_text()
        assert "<human_oversight>" in content, \
            "Safety validator missing human_oversight section"
        assert "meta/human-oversight.md" in content, \
            "Safety validator missing human oversight integration"
        assert "<escalation_protocols>" in content, \
            "Safety validator missing escalation_protocols"
    
    def test_safety_validator_has_approval_gates(self, safety_validator_path):
        """Test that safety validator has approval gates."""
        content = safety_validator_path.read_text()
        assert "<approval_gates>" in content, \
            "Safety validator missing approval_gates section"
        assert "<approval_required>" in content, \
            "Safety validator missing approval_required"
        assert "<approval_criteria>" in content, \
            "Safety validator missing approval_criteria"
        assert "<approval_process>" in content, \
            "Safety validator missing approval_process"


class TestSafetyValidatorIntegration:
    """Test suite for safety validator integration validation."""
    
    @pytest.fixture
    def safety_validator_path(self):
        """Get safety validator module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "meta" / "safety-validator.md"
    
    @pytest.fixture
    def meta_modules_dir(self):
        """Get the meta modules directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "meta"
    
    def test_safety_validator_has_meta_integration(self, safety_validator_path):
        """Test that safety validator has meta-framework integration."""
        content = safety_validator_path.read_text()
        assert "<meta_framework_integration>" in content, \
            "Safety validator missing meta_framework_integration section"
        assert "<framework_protection>" in content, \
            "Safety validator missing framework_protection"
        assert "<module_validation>" in content, \
            "Safety validator missing module_validation"
    
    def test_safety_validator_has_adaptive_integration(self, safety_validator_path):
        """Test that safety validator has adaptive integration."""
        content = safety_validator_path.read_text()
        assert "<adaptive_integration>" in content, \
            "Safety validator missing adaptive_integration section"
        assert "meta/adaptive-router.md" in content, \
            "Safety validator missing adaptive router integration"
        assert "<learning_safety>" in content, \
            "Safety validator missing learning_safety"
    
    def test_safety_validator_has_performance_integration(self, safety_validator_path):
        """Test that safety validator has performance integration."""
        content = safety_validator_path.read_text()
        assert "<performance_integration>" in content, \
            "Safety validator missing performance_integration section"
        assert "meta/performance-optimizer.md" in content, \
            "Safety validator missing performance optimizer integration"
        assert "<optimization_safety>" in content, \
            "Safety validator missing optimization_safety"
    
    def test_safety_validator_has_recovery_integration(self, safety_validator_path):
        """Test that safety validator has recovery integration."""
        content = safety_validator_path.read_text()
        assert "<recovery_integration>" in content, \
            "Safety validator missing recovery_integration section"
        assert "meta/intelligent-failure-recovery.md" in content, \
            "Safety validator missing failure recovery integration"
        assert "<recovery_safety>" in content, \
            "Safety validator missing recovery_safety"
    
    def test_safety_validator_has_command_integration(self, safety_validator_path):
        """Test that safety validator has command integration."""
        content = safety_validator_path.read_text()
        assert "<command_integration>" in content, \
            "Safety validator missing command_integration section"
        assert "<command_validation>" in content, \
            "Safety validator missing command_validation"
        assert "<workflow_safety>" in content, \
            "Safety validator missing workflow_safety"


class TestSafetyValidatorPerformance:
    """Test suite for safety validator performance validation."""
    
    @pytest.fixture
    def safety_validator_path(self):
        """Get safety validator module path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules" / "meta" / "safety-validator.md"
    
    def test_safety_validator_has_performance_targets(self, safety_validator_path):
        """Test that safety validator has performance targets."""
        content = safety_validator_path.read_text()
        assert "<performance_targets>" in content, \
            "Safety validator missing performance_targets section"
        assert "99.9%" in content, \
            "Safety validator missing 99.9% stability target"
        assert "validation_speed" in content, \
            "Safety validator missing validation_speed metric"
    
    def test_safety_validator_has_monitoring_metrics(self, safety_validator_path):
        """Test that safety validator has monitoring metrics."""
        content = safety_validator_path.read_text()
        assert "<monitoring_metrics>" in content, \
            "Safety validator missing monitoring_metrics section"
        assert "<safety_score>" in content, \
            "Safety validator missing safety_score"
        assert "<violation_rate>" in content, \
            "Safety validator missing violation_rate"
    
    def test_safety_validator_has_enforcement_effectiveness(self, safety_validator_path):
        """Test that safety validator has enforcement effectiveness."""
        content = safety_validator_path.read_text()
        assert "<enforcement_effectiveness>" in content, \
            "Safety validator missing enforcement_effectiveness section"
        assert "<prevention_rate>" in content, \
            "Safety validator missing prevention_rate"
        assert "<detection_accuracy>" in content, \
            "Safety validator missing detection_accuracy"
    
    def test_safety_validator_has_response_times(self, safety_validator_path):
        """Test that safety validator has response times."""
        content = safety_validator_path.read_text()
        assert "<response_times>" in content, \
            "Safety validator missing response_times section"
        assert "<validation_latency>" in content, \
            "Safety validator missing validation_latency"
        assert "<enforcement_speed>" in content, \
            "Safety validator missing enforcement_speed"
    
    def test_safety_validator_has_evolutionary_features(self, safety_validator_path):
        """Test that safety validator has evolutionary features."""
        content = safety_validator_path.read_text()
        assert "Safety Guardian" in content, \
            "Safety validator missing safety guardian capabilities"
        assert "boundary enforcement" in content, \
            "Safety validator missing boundary enforcement"
        assert "stability preservation" in content, \
            "Safety validator missing stability preservation"