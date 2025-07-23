#!/usr/bin/env python3
"""
Unit tests for Constitutional AI safety framework.
"""

import unittest
from pathlib import Path
import re

class TestConstitutionalAISafety(unittest.TestCase):
    """Test constitutional AI safety implementation."""
    
    def setUp(self):
        """Set up test environment."""
        self.framework_root = Path("claude_prompt_factory")
        self.safety_component = self.framework_root / "components" / "constitutional" / "safety-framework.md"
    
    def test_harmlessness_validation(self):
        """Test harmlessness principles are enforced."""
        if self.safety_component.exists():
            with open(self.safety_component, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for harmlessness principles
            self.assertIn('harmlessness', content.lower())
            self.assertIn('prevent harm', content.lower())
            self.assertIn('safety', content.lower())
            
            # Verify safety checks are present
            safety_patterns = [
                r'safety[_-]?check',
                r'harm[_-]?assessment',
                r'risk[_-]?evaluation'
            ]
            
            found_safety_check = False
            for pattern in safety_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    found_safety_check = True
                    break
            
            self.assertTrue(found_safety_check, "No safety check patterns found")
        else:
            self.skipTest(f"Safety component not found: {self.safety_component}")
    
    def test_helpfulness_balance(self):
        """Test that helpfulness is balanced with safety."""
        if self.safety_component.exists():
            with open(self.safety_component, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for helpfulness principles
            self.assertIn('helpful', content.lower())
            
            # Ensure there's a balance mechanism
            balance_patterns = [
                r'balance.*safety.*helpful',
                r'helpful.*without.*harm',
                r'maximize.*benefit.*minimize.*risk'
            ]
            
            found_balance = False
            for pattern in balance_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    found_balance = True
                    break
            
            self.assertTrue(found_balance, "No balance mechanism found between safety and helpfulness")
        else:
            self.skipTest(f"Safety component not found: {self.safety_component}")
    
    def test_honesty_principles(self):
        """Test honesty and transparency principles."""
        if self.safety_component.exists():
            with open(self.safety_component, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for honesty principles
            honesty_keywords = ['honest', 'truthful', 'transparent', 'accurate']
            found_honesty = any(keyword in content.lower() for keyword in honesty_keywords)
            
            self.assertTrue(found_honesty, "No honesty principles found in safety framework")
        else:
            self.skipTest(f"Safety component not found: {self.safety_component}")
    
    def test_constitutional_compliance_in_commands(self):
        """Test that commands include constitutional safety."""
        commands_dir = self.framework_root / "commands"
        
        if commands_dir.exists():
            # Sample a few command files
            sample_commands = list(commands_dir.rglob("*.md"))[:10]
            
            commands_with_safety = 0
            for cmd_path in sample_commands:
                if cmd_path.name == "README.md":
                    continue
                
                with open(cmd_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for safety framework inclusion
                if 'constitutional/safety-framework' in content or 'constitutional' in content:
                    commands_with_safety += 1
            
            # At least 80% should include safety
            safety_ratio = commands_with_safety / len(sample_commands) if sample_commands else 0
            self.assertGreaterEqual(safety_ratio, 0.8, 
                f"Only {safety_ratio*100:.1f}% of commands include constitutional safety")
        else:
            self.skipTest("Commands directory not found")
    
    def test_safety_validation_structure(self):
        """Test the structure of safety validation components."""
        validation_patterns = [
            r'<safety[_-]?validation>',
            r'<risk[_-]?assessment>',
            r'<harm[_-]?prevention>'
        ]
        
        if self.safety_component.exists():
            with open(self.safety_component, 'r', encoding='utf-8') as f:
                content = f.read()
            
            found_validation = False
            for pattern in validation_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    found_validation = True
                    break
            
            self.assertTrue(found_validation, "No safety validation structure found")
        else:
            self.skipTest(f"Safety component not found: {self.safety_component}")

if __name__ == '__main__':
    unittest.main()