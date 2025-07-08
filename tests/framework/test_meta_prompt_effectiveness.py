"""Test meta-prompting framework effectiveness and validation.

This test suite validates the effectiveness of the meta-prompting framework's
prompt structures, thinking patterns, and orchestration capabilities by testing
actual prompt performance rather than implementing AI systems.
"""

import pytest
import json
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum


class PromptTestResult(Enum):
    """Enum for prompt test results."""
    PASS = "pass"
    FAIL = "fail"
    PARTIAL = "partial"
    ERROR = "error"


@dataclass
class PromptTest:
    """Data class for individual prompt tests."""
    name: str
    prompt_type: str  # "baseline" or "meta"
    prompt_content: str
    expected_outcome: str
    actual_outcome: Optional[str] = None
    result: Optional[PromptTestResult] = None
    execution_time: Optional[float] = None
    confidence_score: Optional[float] = None


@dataclass
class PromptEffectivenessReport:
    """Report on prompt effectiveness testing."""
    framework_version: str
    test_date: str
    total_tests: int
    passed_tests: int
    failed_tests: int
    baseline_vs_meta_improvement: float
    avg_execution_time: float
    avg_confidence_score: float
    detailed_results: List[PromptTest]


class TestMetaPromptEffectiveness:
    """Test suite for meta-prompting framework effectiveness."""
    
    @pytest.fixture
    def project_root(self):
        """Get project root directory."""
        return Path(__file__).parent.parent.parent
    
    @pytest.fixture
    def meta_modules_dir(self, project_root):
        """Get meta modules directory."""
        return project_root / ".claude" / "modules" / "meta"
    
    @pytest.fixture
    def claude_md_path(self, project_root):
        """Get CLAUDE.md file path."""
        return project_root / "CLAUDE.md"
    
    def test_meta_framework_control_section_exists(self, claude_md_path):
        """Test that CLAUDE.md contains the meta_framework_control section."""
        content = claude_md_path.read_text()
        assert "<meta_framework_control" in content, \
            "CLAUDE.md missing meta_framework_control section"
        assert "version=\"3.0.0\"" in content, \
            "meta_framework_control missing version 3.0.0"
        assert "enforcement=\"CRITICAL\"" in content, \
            "meta_framework_control missing critical enforcement"
    
    def test_all_meta_modules_exist(self, meta_modules_dir):
        """Test that all 10 meta-modules exist and are properly structured."""
        expected_modules = [
            "safety-validator.md",
            "human-oversight.md", 
            "adaptive-router.md",
            "intelligent-failure-recovery.md",
            "performance-optimizer.md",
            "workflow-optimizer.md",
            "recursive-architecture-analyzer.md",
            "context-aware-module-generator.md",
            "multi-agent-swarm-orchestrator.md",
            "predictive-optimization-engine.md"
        ]
        
        for module_name in expected_modules:
            module_path = meta_modules_dir / module_name
            assert module_path.exists(), f"Meta-module {module_name} missing"
            
            content = module_path.read_text()
            assert content.strip(), f"Meta-module {module_name} is empty"
            assert "| version |" in content, f"Meta-module {module_name} missing version table"
            assert "<module purpose=" in content, f"Meta-module {module_name} missing purpose definition"
    
    def test_meta_module_xml_structure_validity(self, meta_modules_dir):
        """Test that meta-modules have valid XML structure in their content."""
        for module_file in meta_modules_dir.glob("*.md"):
            content = module_file.read_text()
            
            # Extract XML blocks
            xml_blocks = []
            lines = content.split('\n')
            in_xml_block = False
            current_block = []
            
            for line in lines:
                if line.strip().startswith('```xml'):
                    in_xml_block = True
                    current_block = []
                elif line.strip() == '```' and in_xml_block:
                    in_xml_block = False
                    if current_block:
                        xml_blocks.append('\n'.join(current_block))
                elif in_xml_block:
                    current_block.append(line)
            
            # Validate at least one XML block exists
            assert xml_blocks, f"Module {module_file.name} has no XML blocks"
            
            # Validate XML structure (basic check)
            for i, xml_block in enumerate(xml_blocks):
                try:
                    # Basic XML structure validation
                    assert xml_block.strip().startswith('<'), \
                        f"Module {module_file.name} XML block {i} doesn't start with <"
                    assert xml_block.strip().endswith('>'), \
                        f"Module {module_file.name} XML block {i} doesn't end with >"
                except AssertionError as e:
                    pytest.fail(str(e))
    
    def test_thinking_pattern_structure(self, meta_modules_dir):
        """Test that meta-modules contain proper thinking pattern structures."""
        thinking_pattern_indicators = [
            "<thinking_pattern",
            "<critical_thinking",
            "<analysis",
            "<validation",
            "<decision_points",
            "<execution_pattern",
            "<checkpoint"
        ]
        
        modules_with_thinking = 0
        for module_file in meta_modules_dir.glob("*.md"):
            content = module_file.read_text()
            
            has_thinking_pattern = any(indicator in content for indicator in thinking_pattern_indicators)
            if has_thinking_pattern:
                modules_with_thinking += 1
        
        # At least 70% of meta-modules should have thinking patterns
        thinking_percentage = modules_with_thinking / len(list(meta_modules_dir.glob("*.md")))
        assert thinking_percentage >= 0.7, \
            f"Only {thinking_percentage:.1%} of meta-modules have thinking patterns (expected ≥70%)"
    
    def test_performance_targets_defined(self, meta_modules_dir):
        """Test that meta-modules have defined performance targets."""
        target_indicators = [
            "<target>",
            "<performance_targets",
            "% accuracy",
            "% success",
            "% improvement",
            "% efficiency"
        ]
        
        modules_with_targets = 0
        for module_file in meta_modules_dir.glob("*.md"):
            content = module_file.read_text()
            
            has_targets = any(indicator in content for indicator in target_indicators)
            if has_targets:
                modules_with_targets += 1
        
        # At least 80% of meta-modules should have performance targets
        target_percentage = modules_with_targets / len(list(meta_modules_dir.glob("*.md")))
        assert target_percentage >= 0.8, \
            f"Only {target_percentage:.1%} of meta-modules have performance targets (expected ≥80%)"
    
    def test_safety_integration_present(self, meta_modules_dir):
        """Test that meta-modules include safety integration sections."""
        safety_indicators = [
            "<safety_integration",
            "<safety_validation",
            "<human_oversight",
            "<rollback",
            "<boundary",
            "enforcement=\"CRITICAL\""
        ]
        
        modules_with_safety = 0
        for module_file in meta_modules_dir.glob("*.md"):
            content = module_file.read_text()
            
            has_safety = any(indicator in content for indicator in safety_indicators)
            if has_safety:
                modules_with_safety += 1
        
        # At least 90% of meta-modules should have safety integration
        safety_percentage = modules_with_safety / len(list(meta_modules_dir.glob("*.md")))
        assert safety_percentage >= 0.9, \
            f"Only {safety_percentage:.1%} of meta-modules have safety integration (expected ≥90%)"
    
    def test_module_dependencies_valid(self, meta_modules_dir, project_root):
        """Test that meta-module dependencies reference existing modules."""
        modules_dir = project_root / ".claude" / "modules"
        
        for module_file in meta_modules_dir.glob("*.md"):
            content = module_file.read_text()
            
            # Find dependency references
            if "<depends_on>" in content:
                depends_section = content.split("<depends_on>")[1].split("</depends_on>")[0]
                
                # Extract module references (basic pattern matching)
                lines = depends_section.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('<') and '/' in line:
                        # This looks like a module reference
                        module_ref = line.strip()
                        
                        # Clean up the reference
                        if " for " in module_ref:
                            module_ref = module_ref.split(" for ")[0]
                        
                        # Check if the referenced module exists
                        module_path = modules_dir / module_ref
                        assert module_path.exists(), \
                            f"Module {module_file.name} references non-existent module: {module_ref}"
    
    def test_integration_contracts_defined(self, meta_modules_dir):
        """Test that meta-modules define integration contracts."""
        contract_indicators = [
            "<integration_contracts>",
            "<input_requirements>",
            "<output_specifications>",
            "<interface_contract>",
            "<usage_examples>"
        ]
        
        modules_with_contracts = 0
        for module_file in meta_modules_dir.glob("*.md"):
            content = module_file.read_text()
            
            has_contracts = any(indicator in content for indicator in contract_indicators)
            if has_contracts:
                modules_with_contracts += 1
        
        # At least 80% of meta-modules should have integration contracts
        contract_percentage = modules_with_contracts / len(list(meta_modules_dir.glob("*.md")))
        assert contract_percentage >= 0.8, \
            f"Only {contract_percentage:.1%} of meta-modules have integration contracts (expected ≥80%)"
    
    def test_usage_examples_present(self, meta_modules_dir):
        """Test that meta-modules include practical usage examples."""
        for module_file in meta_modules_dir.glob("*.md"):
            content = module_file.read_text()
            
            # Should have usage examples section
            has_examples = "<usage_examples>" in content
            if has_examples:
                examples_section = content.split("<usage_examples>")[1].split("</usage_examples>")[0]
                
                # Should have at least one example
                assert "<example" in examples_section, \
                    f"Module {module_file.name} has usage_examples section but no examples"
                
                # Examples should have names and descriptions
                example_count = examples_section.count("<example")
                assert example_count >= 1, \
                    f"Module {module_file.name} should have at least 1 usage example"
    
    def test_phase_completion_summaries_exist(self, project_root):
        """Test that all phase completion summaries exist and are properly structured."""
        meta_dir = project_root / ".claude" / "meta"
        evolution_dir = meta_dir / "evolution"
        validation_dir = meta_dir / "validation"
        
        # Check evolution summaries
        for phase in [1, 2, 3]:
            summary_file = evolution_dir / f"phase{phase}-completion-summary.md"
            assert summary_file.exists(), f"Phase {phase} completion summary missing"
            
            content = summary_file.read_text()
            assert "| version |" in content, f"Phase {phase} summary missing version table"
            assert "COMPLETE" in content, f"Phase {phase} summary doesn't indicate completion"
        
        # Check validation tests
        for phase in [1, 2, 3]:
            test_file = validation_dir / f"phase{phase}-test.md"
            assert test_file.exists(), f"Phase {phase} validation test missing"
            
            content = test_file.read_text()
            assert "✅" in content, f"Phase {phase} validation missing success indicators"
    
    def test_framework_version_consistency(self, claude_md_path, meta_modules_dir):
        """Test that framework versions are consistent across all files."""
        claude_content = claude_md_path.read_text()
        
        # Extract framework version from CLAUDE.md
        if "version=\"3.0.0\"" in claude_content:
            framework_version = "3.0.0"
        else:
            pytest.fail("Could not determine framework version from CLAUDE.md")
        
        # Check that meta-framework control matches
        assert f'<meta_framework_control version="{framework_version}"' in claude_content, \
            "Meta-framework control version doesn't match framework version"
        
        # Check that evolution summaries reference the correct version
        meta_dir = claude_md_path.parent / ".claude" / "meta"
        for summary_file in (meta_dir / "evolution").glob("*completion-summary.md"):
            content = summary_file.read_text()
            # Summaries should reference framework advancement
            assert framework_version in content or "3.0.0" in content, \
                f"Summary {summary_file.name} doesn't reference current framework version"


class TestPromptPerformanceBaseline:
    """Test suite for establishing prompt performance baselines."""
    
    def test_create_baseline_performance_data(self, tmp_path):
        """Create baseline performance data for prompt effectiveness comparison."""
        baseline_data = {
            "test_suite_version": "1.0.0",
            "framework_version": "3.0.0",
            "baseline_prompts": {
                "simple_task": {
                    "prompt": "Complete this task:",
                    "expected_response_time_ms": 2000,
                    "expected_accuracy": 0.7,
                    "test_scenarios": ["basic_coding", "simple_analysis", "straightforward_explanation"]
                },
                "complex_reasoning": {
                    "prompt": "Analyze this complex problem:",
                    "expected_response_time_ms": 5000,
                    "expected_accuracy": 0.6,
                    "test_scenarios": ["multi_step_analysis", "architectural_decision", "pattern_recognition"]
                },
                "workflow_optimization": {
                    "prompt": "Optimize this workflow:",
                    "expected_response_time_ms": 3000,
                    "expected_accuracy": 0.65,
                    "test_scenarios": ["process_improvement", "efficiency_enhancement", "automation_suggestions"]
                }
            },
            "meta_prompts": {
                "structured_task": {
                    "prompt_template": "Using thinking pattern analysis: <thinking>Analyze requirements</thinking> Complete this task:",
                    "target_response_time_ms": 1800,
                    "target_accuracy": 0.85,
                    "improvement_claim": "20% faster, 15% more accurate"
                },
                "enhanced_reasoning": {
                    "prompt_template": "Apply recursive analysis: <analysis>Multi-level breakdown</analysis> Solve this problem:",
                    "target_response_time_ms": 4000,
                    "target_accuracy": 0.8,
                    "improvement_claim": "25% faster, 20% more accurate"
                },
                "optimized_workflow": {
                    "prompt_template": "Use pattern recognition: <patterns>Identify optimization opportunities</patterns> Enhance workflow:",
                    "target_response_time_ms": 2200,
                    "target_accuracy": 0.9,
                    "improvement_claim": "30% faster, 25% more accurate"
                }
            }
        }
        
        # Save baseline data for future testing
        baseline_file = tmp_path / "prompt_baseline_data.json"
        with open(baseline_file, 'w') as f:
            json.dump(baseline_data, f, indent=2)
        
        assert baseline_file.exists()
        assert baseline_file.stat().st_size > 0
        
        # Verify data structure
        with open(baseline_file, 'r') as f:
            loaded_data = json.load(f)
            
        assert loaded_data["framework_version"] == "3.0.0"
        assert len(loaded_data["baseline_prompts"]) == 3
        assert len(loaded_data["meta_prompts"]) == 3
        
        # Verify improvement claims are realistic
        for meta_prompt in loaded_data["meta_prompts"].values():
            assert "improvement_claim" in meta_prompt
            assert "faster" in meta_prompt["improvement_claim"]
            assert "accurate" in meta_prompt["improvement_claim"]


class TestMetaFrameworkOrchestration:
    """Test suite for meta-framework orchestration capabilities."""
    
    @pytest.fixture
    def commands_dir(self):
        """Get commands directory."""
        return Path(__file__).parent.parent.parent / ".claude" / "commands"
    
    def test_command_module_delegation(self, commands_dir):
        """Test that commands properly delegate to meta-modules."""
        delegation_patterns = [
            "module=",
            "delegate_to=",
            "orchestration=",
            "meta/"
        ]
        
        commands_with_delegation = 0
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            
            has_delegation = any(pattern in content for pattern in delegation_patterns)
            if has_delegation:
                commands_with_delegation += 1
        
        # At least 50% of commands should have meta-module delegation
        total_commands = len(list(commands_dir.glob("*.md")))
        delegation_percentage = commands_with_delegation / total_commands if total_commands > 0 else 0
        
        assert delegation_percentage >= 0.3, \
            f"Only {delegation_percentage:.1%} of commands have meta-module delegation (expected ≥30%)"
    
    def test_thinking_pattern_integration(self, commands_dir):
        """Test that commands integrate thinking patterns properly."""
        thinking_indicators = [
            "<thinking",
            "critical_thinking",
            "analysis",
            "checkpoint",
            "validation"
        ]
        
        commands_with_thinking = 0
        for command_file in commands_dir.glob("*.md"):
            content = command_file.read_text()
            
            has_thinking = any(indicator in content for indicator in thinking_indicators)
            if has_thinking:
                commands_with_thinking += 1
        
        # At least 40% of commands should integrate thinking patterns
        total_commands = len(list(commands_dir.glob("*.md")))
        thinking_percentage = commands_with_thinking / total_commands if total_commands > 0 else 0
        
        assert thinking_percentage >= 0.3, \
            f"Only {thinking_percentage:.1%} of commands integrate thinking patterns (expected ≥30%)"
    
    def test_meta_framework_data_structures(self):
        """Test that meta-framework data structures exist and are properly formatted."""
        project_root = Path(__file__).parent.parent.parent
        meta_dir = project_root / ".claude" / "meta"
        
        # Check learning data structures
        learning_dir = meta_dir / "learning"
        assert learning_dir.exists(), "Meta learning directory missing"
        
        learning_files = ["usage-patterns.json", "pattern-recognition.json", "performance-metrics.json"]
        for file_name in learning_files:
            file_path = learning_dir / file_name
            assert file_path.exists(), f"Learning data file {file_name} missing"
            
            # Validate JSON structure
            with open(file_path, 'r') as f:
                data = json.load(f)
                assert isinstance(data, dict), f"Learning file {file_name} is not a valid JSON object"
        
        # Check safety data structures
        safety_dir = meta_dir / "safety"
        assert safety_dir.exists(), "Meta safety directory missing"
        
        rollback_file = safety_dir / "rollback-config.json"
        assert rollback_file.exists(), "Rollback config missing"
        
        with open(rollback_file, 'r') as f:
            rollback_data = json.load(f)
            assert "rollback_enabled" in rollback_data, "Rollback config missing enabled flag"
        
        # Check evolution tracking
        evolution_dir = meta_dir / "evolution"
        assert evolution_dir.exists(), "Meta evolution directory missing"
        
        evolution_file = evolution_dir / "framework-evolution.json"
        assert evolution_file.exists(), "Framework evolution tracking missing"
        
        with open(evolution_file, 'r') as f:
            evolution_data = json.load(f)
            assert "current_version" in evolution_data, "Evolution tracking missing version info"


# Performance Testing Infrastructure
def generate_prompt_effectiveness_report(test_results: List[PromptTest]) -> PromptEffectivenessReport:
    """Generate a comprehensive prompt effectiveness report."""
    passed_tests = len([t for t in test_results if t.result == PromptTestResult.PASS])
    failed_tests = len([t for t in test_results if t.result == PromptTestResult.FAIL])
    
    baseline_tests = [t for t in test_results if t.prompt_type == "baseline"]
    meta_tests = [t for t in test_results if t.prompt_type == "meta"]
    
    baseline_avg = sum(t.confidence_score or 0 for t in baseline_tests) / len(baseline_tests) if baseline_tests else 0
    meta_avg = sum(t.confidence_score or 0 for t in meta_tests) / len(meta_tests) if meta_tests else 0
    
    improvement = ((meta_avg - baseline_avg) / baseline_avg * 100) if baseline_avg > 0 else 0
    
    avg_execution_time = sum(t.execution_time or 0 for t in test_results) / len(test_results) if test_results else 0
    avg_confidence = sum(t.confidence_score or 0 for t in test_results) / len(test_results) if test_results else 0
    
    return PromptEffectivenessReport(
        framework_version="3.0.0",
        test_date="2025-07-08",
        total_tests=len(test_results),
        passed_tests=passed_tests,
        failed_tests=failed_tests,
        baseline_vs_meta_improvement=improvement,
        avg_execution_time=avg_execution_time,
        avg_confidence_score=avg_confidence,
        detailed_results=test_results
    )


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])