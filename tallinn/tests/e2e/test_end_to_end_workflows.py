#!/usr/bin/env python3
"""
End-to-end tests for complete workflows.
"""

import unittest
from pathlib import Path
import time
import json

class TestEndToEndWorkflows(unittest.TestCase):
    """Test complete end-to-end workflows."""
    
    def setUp(self):
        """Set up test environment."""
        self.framework_root = Path("claude_prompt_factory")
        self.commands_dir = self.framework_root / "commands"
        self.components_dir = self.framework_root / "components"
    
    def test_development_workflow(self):
        """Test a complete development workflow from task to implementation."""
        workflow_steps = [
            {
                "step": "task_creation",
                "command": "development/task.md",
                "expected_components": ["validation/input-validation.md", "workflow/command-execution.md"]
            },
            {
                "step": "code_analysis",
                "command": "analysis/analyze-code.md",
                "expected_components": ["quality/anti-pattern-detection.md"]
            },
            {
                "step": "testing",
                "command": "testing/test-unit.md",
                "expected_components": ["testing/test-unit.md"]
            },
            {
                "step": "deployment",
                "command": "deployment/deploy.md",
                "expected_components": ["deployment/ci-cd-integration.md"]
            }
        ]
        
        workflow_success = True
        workflow_log = []
        
        for step_info in workflow_steps:
            step_result = {
                "step": step_info["step"],
                "command": step_info["command"],
                "status": "pending",
                "components_found": 0,
                "duration": 0
            }
            
            start_time = time.time()
            
            # Check command exists
            command_path = self.commands_dir / step_info["command"]
            if command_path.exists():
                step_result["status"] = "command_found"
                
                # Check expected components
                components_found = 0
                for component in step_info["expected_components"]:
                    comp_path = self.components_dir / component
                    if comp_path.exists():
                        components_found += 1
                
                step_result["components_found"] = components_found
                if components_found == len(step_info["expected_components"]):
                    step_result["status"] = "success"
                else:
                    step_result["status"] = "partial"
                    workflow_success = False
            else:
                step_result["status"] = "failed"
                workflow_success = False
            
            step_result["duration"] = time.time() - start_time
            workflow_log.append(step_result)
        
        # Validate workflow
        self.assertTrue(workflow_success, 
            f"Workflow failed. Log: {json.dumps(workflow_log, indent=2)}")
        
        # Check workflow performance
        total_duration = sum(step["duration"] for step in workflow_log)
        self.assertLess(total_duration, 1.0, "Workflow validation took too long")
    
    def test_security_audit_workflow(self):
        """Test security audit workflow."""
        security_steps = [
            {
                "step": "security_analysis",
                "command": "security/security-check.md",
                "validation": ["owasp", "security", "vulnerability"]
            },
            {
                "step": "compliance_check",
                "component": "security/owasp-compliance.md",
                "validation": ["compliance", "owasp", "security"]
            }
        ]
        
        for step in security_steps:
            if "command" in step:
                path = self.commands_dir / step["command"]
            else:
                path = self.components_dir / step["component"]
            
            if path.exists():
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                
                # Validate security keywords
                found_keywords = sum(1 for keyword in step["validation"] if keyword in content)
                self.assertGreaterEqual(found_keywords, 2, 
                    f"Not enough security keywords in {step['step']}")
            else:
                self.skipTest(f"Security file not found: {path}")
    
    def test_performance_optimization_workflow(self):
        """Test performance optimization workflow."""
        perf_workflow = [
            {
                "step": "performance_analysis",
                "command": "performance/analyze-performance.md"
            },
            {
                "step": "optimization",
                "component": "performance/framework-optimization.md"
            },
            {
                "step": "caching",
                "component": "performance/component-cache.md"
            }
        ]
        
        workflow_valid = True
        
        for step in perf_workflow:
            if "command" in step:
                path = self.commands_dir / step["command"]
            else:
                path = self.components_dir / step["component"]
            
            if not path.exists():
                workflow_valid = False
                break
        
        self.assertTrue(workflow_valid, "Performance optimization workflow incomplete")
    
    def test_git_workflow_integration(self):
        """Test Git workflow integration."""
        git_commands = [
            "git/git-commit.md",
            "git/git-pr.md",
            "git/git-merge.md"
        ]
        
        git_components_found = 0
        
        for git_cmd in git_commands:
            cmd_path = self.commands_dir / git_cmd
            if cmd_path.exists():
                git_components_found += 1
                
                # Check for Git integration patterns
                with open(cmd_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                git_patterns = ['git', 'commit', 'branch', 'repository']
                found_patterns = sum(1 for pattern in git_patterns if pattern in content.lower())
                
                self.assertGreaterEqual(found_patterns, 2, 
                    f"Not enough Git patterns in {git_cmd}")
        
        self.assertGreaterEqual(git_components_found, 2, 
            "Not enough Git workflow components found")
    
    def test_constitutional_ai_integration(self):
        """Test that constitutional AI is integrated throughout workflows."""
        sample_files = []
        
        # Sample commands and components
        for subdir in ["commands", "components"]:
            dir_path = self.framework_root / subdir
            if dir_path.exists():
                files = list(dir_path.rglob("*.md"))[:20]  # Sample 20 files
                sample_files.extend(files)
        
        files_with_constitutional = 0
        
        for file_path in sample_files:
            if file_path.name == "README.md":
                continue
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'constitutional' in content.lower() or 'safety-framework' in content:
                files_with_constitutional += 1
        
        integration_rate = files_with_constitutional / len(sample_files) if sample_files else 0
        
        self.assertGreaterEqual(integration_rate, 0.7, 
            f"Only {integration_rate*100:.1f}% of files integrate constitutional AI")

if __name__ == '__main__':
    unittest.main()