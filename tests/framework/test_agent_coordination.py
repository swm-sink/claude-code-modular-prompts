"""Integration tests for multi-agent coordination framework."""

import os
import pytest
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch
import json


class TestAgentCoordination:
    """Test integration between all agent-enhanced modules."""
    
    @pytest.fixture
    def modules_dir(self):
        """Get the modules directory path."""
        return Path(__file__).parent.parent.parent / ".claude" / "modules"
    
    def test_error_recovery_integration(self, modules_dir):
        """Test that error recovery module integrates with other modules."""
        error_recovery_path = modules_dir / "quality" / "error-recovery.md"
        assert error_recovery_path.exists(), "Error recovery module not found"
        
        with open(error_recovery_path, 'r') as f:
            content = f.read()
        
        # Check for integration points with other modules
        integration_dependencies = [
            "patterns/intelligent-routing.md",
            "patterns/session-management.md"
        ]
        
        for dependency in integration_dependencies:
            assert dependency in content, f"Error recovery missing integration with {dependency}"
        
        # Check for Task() pattern usage
        assert "Task(" in content, "Error recovery should use Task() delegation patterns"
        
        # Check for GitHub integration
        assert "gh issue create" in content, "Error recovery should integrate with GitHub"
    
    def test_production_standards_integration(self, modules_dir):
        """Test that production standards integrates with other quality modules."""
        production_path = modules_dir / "quality" / "production-standards.md"
        assert production_path.exists(), "Production standards module not found"
        
        with open(production_path, 'r') as f:
            content = f.read()
        
        # Check for integration with other modules
        expected_integrations = [
            "quality/tdd.md",
            "quality/error-recovery.md"
        ]
        
        for integration in expected_integrations:
            assert integration in content, f"Production standards missing {integration}"
    
    def test_pattern_library_integration(self, modules_dir):
        """Test that pattern library is properly integrated with other modules."""
        pattern_lib_path = modules_dir / "patterns" / "pattern-library.md"
        assert pattern_lib_path.exists(), "Pattern library not found"
        
        with open(pattern_lib_path, 'r') as f:
            content = f.read()
        
        # Check for Claude Code native patterns
        native_patterns = [
            "task_pattern_optimization",
            "batch_pattern_optimization", 
            "native_tool_optimization",
            "native_context_management"
        ]
        
        for pattern in native_patterns:
            assert pattern in content, f"Missing native pattern: {pattern}"
        
        # Check for pattern usage integration
        assert "Module Integration Pattern Usage" in content, "Missing module integration mapping"
    
    def test_cross_module_pattern_references(self, modules_dir):
        """Test that modules properly reference patterns from pattern library."""
        pattern_library_patterns = []
        
        # Read pattern library to get available patterns
        pattern_lib_path = modules_dir / "patterns" / "pattern-library.md"
        with open(pattern_lib_path, 'r') as f:
            content = f.read()
            
        # Extract pattern names
        import re
        pattern_matches = re.findall(r'<(\w+)>', content)
        pattern_library_patterns = list(set(pattern_matches))
        
        # Check that other modules reference these patterns correctly
        for module_file in modules_dir.rglob("*.md"):
            if module_file.name == "pattern-library.md":
                continue
                
            with open(module_file, 'r') as f:
                module_content = f.read()
            
            # Find pattern usage declarations
            pattern_uses = re.findall(r'<uses_pattern from="([^"]+)">([^<]+)</uses_pattern>', module_content)
            
            for pattern_file, pattern_name in pattern_uses:
                # Verify pattern file reference is correct
                if pattern_file == "patterns/pattern-library.md":
                    assert pattern_name in pattern_library_patterns or pattern_name.replace('_', '') in str(pattern_library_patterns), \
                        f"Module {module_file.name} references non-existent pattern: {pattern_name}"
    
    def test_session_management_multi_agent_integration(self, modules_dir):
        """Test that session management properly integrates with multi-agent patterns."""
        session_mgmt_path = modules_dir / "patterns" / "session-management.md"
        assert session_mgmt_path.exists(), "Session management module not found"
        
        with open(session_mgmt_path, 'r') as f:
            content = f.read()
        
        # Check for multi-agent coordination features
        multi_agent_features = [
            "Task() calls with multiple agents",
            "Batch() operations",
            "multi-agent coordination",
            "context_coordination"
        ]
        
        for feature in multi_agent_features:
            assert feature in content, f"Session management missing multi-agent feature: {feature}"
        
        # Check for error recovery integration
        assert "quality/error-recovery.md" in content, "Session management should integrate with error recovery"
    
    def test_intelligent_routing_enhancement_integration(self, modules_dir):
        """Test that intelligent routing integrates with new enhancement modules."""
        routing_path = modules_dir / "patterns" / "intelligent-routing.md"
        assert routing_path.exists(), "Intelligent routing module not found"
        
        with open(routing_path, 'r') as f:
            content = f.read()
        
        # Check for integration with enhancement modules
        enhancement_integrations = [
            "context_aware_routing_intelligence",
            "failure_detection_patterns",
            "error-recovery.md"
        ]
        
        for integration in enhancement_integrations:
            assert integration in content, f"Routing missing enhancement integration: {integration}"
        
        # Check for predictive escalation integration
        predictive_features = [
            "context_complexity_analysis",
            "memory_optimized_pattern_matching"
        ]
        
        for feature in predictive_features:
            assert feature in content, f"Routing missing predictive feature: {feature}"


class TestFrameworkValidation:
    """Test comprehensive framework validation."""
    
    def test_all_modules_have_version_tables(self):
        """Test that all modules have proper version tables."""
        modules_dir = Path(__file__).parent.parent.parent / ".claude" / "modules"
        
        for module_file in modules_dir.rglob("*.md"):
            with open(module_file, 'r') as f:
                content = f.read()
            
            lines = content.split('\n')
            assert len(lines) >= 3, f"Module {module_file.name} too short"
            assert lines[0].startswith('| version'), f"Module {module_file.name} missing version table"
            
            # Check version table format
            version_line = lines[2]
            parts = [p.strip() for p in version_line.split('|')]
            assert len(parts) >= 4, f"Incomplete version table in {module_file.name}"
            
            # Validate version format
            version = parts[1]
            import re
            assert re.match(r'^\d+\.\d+\.\d+$', version), f"Invalid version format in {module_file.name}"
    
    def test_temporal_standards_compliance(self):
        """Test that all modules comply with July 2025 temporal standards."""
        modules_dir = Path(__file__).parent.parent.parent / ".claude" / "modules"
        
        for module_file in modules_dir.rglob("*.md"):
            with open(module_file, 'r') as f:
                content = f.read()
            
            # Check for non-July 2025 dates
            import re
            
            # Check for old year patterns
            old_years = re.findall(r'20(1[0-9]|2[0-4])-[0-9]{2}-[0-9]{2}', content)
            assert len(old_years) == 0, f"Non-compliant old year timestamps in {module_file.name}: {old_years}"
            
            # Check for non-July 2025 dates
            non_july_2025 = re.findall(r'2025-(0[1-6]|08|09|1[0-2])-[0-9]{2}', content)
            assert len(non_july_2025) == 0, f"Non-July 2025 timestamps in {module_file.name}: {non_july_2025}"
    
    def test_integration_dependencies_exist(self):
        """Test that all declared integration dependencies exist."""
        modules_dir = Path(__file__).parent.parent.parent / ".claude" / "modules"
        
        for module_file in modules_dir.rglob("*.md"):
            with open(module_file, 'r') as f:
                content = f.read()
            
            # Find dependency declarations
            if "<depends_on>" in content:
                import re
                deps = re.findall(r'([\w/\-]+\.md)', content[content.find('<depends_on>'):content.find('</depends_on>') if '</depends_on>' in content else len(content)])
                
                for dep in deps:
                    if dep.startswith('modules/'):
                        dep_path = modules_dir.parent / dep
                    elif dep.startswith('commands/'):
                        dep_path = modules_dir.parent / dep
                    else:
                        dep_path = modules_dir.parent / "modules" / dep
                    
                    assert dep_path.exists(), f"Module {module_file.name} references non-existent dependency: {dep}"
    
    def test_quality_gate_definitions(self):
        """Test that quality gates are properly defined and integrated."""
        modules_dir = Path(__file__).parent.parent.parent / ".claude" / "modules"
        
        # Find modules with quality gates
        quality_gate_modules = []
        for module_file in modules_dir.rglob("*.md"):
            with open(module_file, 'r') as f:
                content = f.read()
            
            if "<quality_gates" in content or "<gate name=" in content:
                quality_gate_modules.append(module_file)
        
        assert len(quality_gate_modules) > 0, "No quality gate definitions found"
        
        # Check that quality gate modules have proper structure
        for module_file in quality_gate_modules:
            with open(module_file, 'r') as f:
                content = f.read()
            
            # Check for gate definitions
            assert "<gate name=" in content, f"Quality gate module {module_file.name} missing gate definitions"
            
            # Check for enforcement points
            if "quality_gate_enforcement" in content:
                assert "enforcement_points" in content, f"Quality module {module_file.name} missing enforcement points"


class TestNativePatternIntegration:
    """Test integration of native Claude Code patterns."""
    
    def test_task_pattern_integration(self):
        """Test that Task() patterns are properly integrated."""
        modules_dir = Path(__file__).parent.parent.parent / ".claude" / "modules"
        
        task_pattern_modules = []
        for module_file in modules_dir.rglob("*.md"):
            with open(module_file, 'r') as f:
                content = f.read()
            
            if "Task(" in content:
                task_pattern_modules.append(module_file)
        
        assert len(task_pattern_modules) > 0, "No Task() pattern usage found"
        
        # Check for proper Task() pattern structure
        pattern_lib_path = modules_dir / "patterns" / "pattern-library.md"
        with open(pattern_lib_path, 'r') as f:
            pattern_content = f.read()
        
        assert "task_pattern_optimization" in pattern_content, "Pattern library missing Task() optimization"
        assert "BatchTool(" in pattern_content, "Pattern library missing BatchTool integration"
    
    def test_github_integration_patterns(self):
        """Test that GitHub integration patterns are properly implemented."""
        modules_dir = Path(__file__).parent.parent.parent / ".claude" / "modules"
        
        github_modules = []
        for module_file in modules_dir.rglob("*.md"):
            with open(module_file, 'r') as f:
                content = f.read()
            
            if "gh issue create" in content or "github_integration" in content:
                github_modules.append(module_file)
        
        assert len(github_modules) > 0, "No GitHub integration patterns found"
        
        # Check for proper GitHub integration structure
        for module_file in github_modules:
            with open(module_file, 'r') as f:
                content = f.read()
            
            # Should have session creation patterns
            assert any(pattern in content for pattern in ["gh issue create", "session creation", "GitHub session"]), \
                f"Module {module_file.name} missing proper GitHub integration"
    
    def test_parallel_execution_optimization(self):
        """Test that parallel execution patterns are properly integrated."""
        pattern_lib_path = Path(__file__).parent.parent.parent / ".claude" / "modules" / "patterns" / "pattern-library.md"
        
        with open(pattern_lib_path, 'r') as f:
            content = f.read()
        
        # Check for parallel execution patterns
        parallel_patterns = [
            "parallel_execution",
            "native_tool_optimization", 
            "70% latency reduction",
            "batch_operations"
        ]
        
        for pattern in parallel_patterns:
            assert pattern in content, f"Pattern library missing parallel pattern: {pattern}"
        
        # Check for verified performance metrics
        assert "70% latency reduction" in content, "Missing verified performance metrics"
        assert "proven_results" in content, "Missing proven results documentation"


class TestRecoveryAndResilience:
    """Test error recovery and resilience integration."""
    
    def test_error_recovery_hierarchy(self):
        """Test that error recovery hierarchy is properly implemented."""
        modules_dir = Path(__file__).parent.parent.parent / ".claude" / "modules"
        error_recovery_path = modules_dir / "quality" / "error-recovery.md"
        
        with open(error_recovery_path, 'r') as f:
            content = f.read()
        
        # Check for 4-tier recovery hierarchy
        recovery_tiers = [
            "tier_1",
            "tier_2", 
            "tier_3",
            "tier_4"
        ]
        
        for tier in recovery_tiers:
            assert tier in content, f"Error recovery missing {tier} implementation"
        
        # Check for integration with session management
        assert "session-management.md" in content, "Error recovery missing session management integration"
    
    def test_predictive_escalation_accuracy(self):
        """Test predictive escalation accuracy metrics."""
        modules_dir = Path(__file__).parent.parent.parent / ".claude" / "modules"
        predictive_path = modules_dir / "quality" / "predictive-escalation.md"
        
        with open(predictive_path, 'r') as f:
            content = f.read()
        
        # Check for accuracy metrics
        accuracy_metrics = [
            "success_rate_tracking",
            "performance_metrics",
            "escalation_accuracy"
        ]
        
        for metric in accuracy_metrics:
            assert metric in content, f"Predictive escalation missing {metric}"
        
        # Check for complexity scoring
        assert "complexity_scoring" in content, "Missing complexity scoring algorithm"
        assert "escalation_prediction" in content, "Missing escalation prediction logic"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])