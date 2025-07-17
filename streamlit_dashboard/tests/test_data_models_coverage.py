"""
Additional tests to achieve 90% coverage for data models
These tests cover the missing lines and edge cases
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, patch
import time

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestDataModelsCoverage:
    """Test cases to improve coverage for data models"""
    
    def test_command_update_metadata_timing(self):
        """Test Command update_metadata changes timestamp"""
        from data.models import Command
        
        command = Command(
            name="timing-test",
            path="/commands/timing-test.md",
            category="command"
        )
        
        original_updated_at = command.updated_at
        
        # Small delay to ensure timestamp difference
        time.sleep(0.001)
        command.update_metadata()
        
        assert command.updated_at != original_updated_at
    
    def test_module_update_metadata_timing(self):
        """Test Module update_metadata changes timestamp"""
        from data.models import Module
        
        module = Module(
            name="timing-test",
            path="/modules/timing-test.md",
            category="test"
        )
        
        original_updated_at = module.updated_at
        
        # Small delay to ensure timestamp difference
        time.sleep(0.001)
        module.update_metadata()
        
        assert module.updated_at != original_updated_at
    
    def test_module_add_dependency_with_duplicates(self):
        """Test Module add_dependency doesn't add duplicates"""
        from data.models import Module
        
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test"
        )
        
        # Add same dependency twice
        module.add_dependency("test-dep")
        module.add_dependency("test-dep")
        
        assert len(module.dependencies) == 1
        assert module.dependencies[0] == "test-dep"
    
    def test_module_add_tag_with_duplicates(self):
        """Test Module add_tag doesn't add duplicates"""
        from data.models import Module
        
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test"
        )
        
        # Add same tag twice
        module.add_tag("test-tag")
        module.add_tag("test-tag")
        
        assert len(module.tags) == 1
        assert module.tags[0] == "test-tag"
    
    def test_framework_update_metadata_timing(self):
        """Test Framework update_metadata changes timestamp"""
        from data.models import Framework
        
        framework = Framework(
            path="/test/.claude",
            commands=[],
            modules=[]
        )
        
        original_updated_at = framework.updated_at
        
        # Small delay to ensure timestamp difference
        time.sleep(0.001)
        framework.update_metadata()
        
        assert framework.updated_at != original_updated_at
    
    def test_framework_add_command_updates_metadata(self):
        """Test Framework add_command updates metadata"""
        from data.models import Framework, Command
        
        framework = Framework(
            path="/test/.claude",
            commands=[],
            modules=[]
        )
        
        original_updated_at = framework.updated_at
        
        command = Command(
            name="test-cmd",
            path="/commands/test-cmd.md",
            category="command"
        )
        
        # Small delay to ensure timestamp difference
        time.sleep(0.001)
        framework.add_command(command)
        
        assert framework.updated_at != original_updated_at
    
    def test_framework_add_module_updates_metadata(self):
        """Test Framework add_module updates metadata"""
        from data.models import Framework, Module
        
        framework = Framework(
            path="/test/.claude",
            commands=[],
            modules=[]
        )
        
        original_updated_at = framework.updated_at
        
        module = Module(
            name="test-mod",
            path="/modules/test-mod.md",
            category="test"
        )
        
        # Small delay to ensure timestamp difference
        time.sleep(0.001)
        framework.add_module(module)
        
        assert framework.updated_at != original_updated_at
    
    def test_module_add_dependency_updates_metadata(self):
        """Test Module add_dependency updates metadata timestamp"""
        from data.models import Module
        
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test"
        )
        
        original_updated_at = module.updated_at
        
        # Small delay to ensure timestamp difference
        time.sleep(0.001)
        module.add_dependency("new-dep")
        
        assert module.updated_at != original_updated_at
    
    def test_module_add_tag_updates_metadata(self):
        """Test Module add_tag updates metadata timestamp"""
        from data.models import Module
        
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test"
        )
        
        original_updated_at = module.updated_at
        
        # Small delay to ensure timestamp difference
        time.sleep(0.001)
        module.add_tag("new-tag")
        
        assert module.updated_at != original_updated_at
    
    def test_framework_statistics_with_multiple_categories(self):
        """Test Framework statistics with multiple command and module categories"""
        from data.models import Framework, Command, Module
        
        framework = Framework(
            path="/test/.claude",
            commands=[],
            modules=[]
        )
        
        # Add commands with different categories
        cmd1 = Command(name="cmd1", path="/commands/cmd1.md", category="core")
        cmd2 = Command(name="cmd2", path="/commands/cmd2.md", category="core")
        cmd3 = Command(name="cmd3", path="/commands/cmd3.md", category="utility")
        
        framework.add_command(cmd1)
        framework.add_command(cmd2)
        framework.add_command(cmd3)
        
        # Add modules with different categories
        mod1 = Module(name="mod1", path="/modules/mod1.md", category="patterns")
        mod2 = Module(name="mod2", path="/modules/mod2.md", category="patterns")
        mod3 = Module(name="mod3", path="/modules/mod3.md", category="security")
        mod4 = Module(name="mod4", path="/modules/mod4.md", category="security")
        mod5 = Module(name="mod5", path="/modules/mod5.md", category="utilities")
        
        framework.add_module(mod1)
        framework.add_module(mod2)
        framework.add_module(mod3)
        framework.add_module(mod4)
        framework.add_module(mod5)
        
        stats = framework.statistics()
        
        assert stats['total_commands'] == 3
        assert stats['total_modules'] == 5
        assert stats['total_components'] == 8
        assert stats['commands_by_category']['core'] == 2
        assert stats['commands_by_category']['utility'] == 1
        assert stats['modules_by_category']['patterns'] == 2
        assert stats['modules_by_category']['security'] == 2
        assert stats['modules_by_category']['utilities'] == 1
    
    def test_command_equality_with_non_command_object(self):
        """Test Command equality with non-Command object returns False"""
        from data.models import Command
        
        command = Command(
            name="test-command",
            path="/commands/test-command.md",
            category="command"
        )
        
        # Test equality with non-Command object
        assert command != "not a command"
        assert command != 42
        assert command != None
        assert command != {}
    
    def test_module_equality_with_non_module_object(self):
        """Test Module equality with non-Module object returns False"""
        from data.models import Module
        
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test"
        )
        
        # Test equality with non-Module object
        assert module != "not a module"
        assert module != 42
        assert module != None
        assert module != {}
    
    def test_complete_workflow_integration(self):
        """Test complete workflow with all model interactions"""
        from data.models import Framework, Command, Module
        
        # Create framework
        framework = Framework(
            path="/test/.claude",
            commands=[],
            modules=[],
            name="Test Framework",
            version="1.0.0",
            description="Test framework for coverage"
        )
        
        # Create and add command
        command = Command(
            name="test-command",
            path="/commands/test-command.md",
            category="command",
            description="Test command",
            usage="/test-command 'example'",
            examples=["Example 1", "Example 2"],
            modules=["test-module"]
        )
        
        framework.add_command(command)
        
        # Create and add module
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test",
            description="Test module",
            version="1.0.0",
            dependencies=["base-module"],
            tags=["test", "example"]
        )
        
        framework.add_module(module)
        
        # Test all interactions
        found_command = framework.get_command_by_name("test-command")
        found_module = framework.get_module_by_name("test-module")
        test_modules = framework.get_modules_by_category("test")
        stats = framework.statistics()
        
        # Convert to dict and back
        framework_dict = framework.to_dict()
        restored_framework = Framework.from_dict(framework_dict)
        
        # Verify all data is preserved
        assert found_command.name == "test-command"
        assert found_module.name == "test-module"
        assert len(test_modules) == 1
        assert stats['total_commands'] == 1
        assert stats['total_modules'] == 1
        assert restored_framework.name == "Test Framework"
        assert len(restored_framework.commands) == 1
        assert len(restored_framework.modules) == 1