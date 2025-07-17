"""
Additional tests to cover missing lines in data models
These tests specifically target the uncovered code paths
"""

import pytest
import sys
import os
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestDataModelsMissingCoverage:
    """Test cases to cover missing lines in data models"""
    
    def test_module_remove_dependency_with_existing_dependency(self):
        """Test Module remove_dependency method with existing dependency"""
        from data.models import Module
        
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test",
            dependencies=["dep1", "dep2", "dep3"]
        )
        
        # Remove an existing dependency
        module.remove_dependency("dep2")
        
        assert "dep2" not in module.dependencies
        assert len(module.dependencies) == 2
        assert "dep1" in module.dependencies
        assert "dep3" in module.dependencies
    
    def test_module_remove_dependency_with_nonexistent_dependency(self):
        """Test Module remove_dependency method with nonexistent dependency"""
        from data.models import Module
        
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test",
            dependencies=["dep1", "dep2"]
        )
        
        # Try to remove a dependency that doesn't exist
        module.remove_dependency("nonexistent")
        
        # Should not change anything
        assert len(module.dependencies) == 2
        assert "dep1" in module.dependencies
        assert "dep2" in module.dependencies
    
    def test_module_remove_tag_with_existing_tag(self):
        """Test Module remove_tag method with existing tag"""
        from data.models import Module
        
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test",
            tags=["tag1", "tag2", "tag3"]
        )
        
        # Remove an existing tag
        module.remove_tag("tag2")
        
        assert "tag2" not in module.tags
        assert len(module.tags) == 2
        assert "tag1" in module.tags
        assert "tag3" in module.tags
    
    def test_module_remove_tag_with_nonexistent_tag(self):
        """Test Module remove_tag method with nonexistent tag"""
        from data.models import Module
        
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test",
            tags=["tag1", "tag2"]
        )
        
        # Try to remove a tag that doesn't exist
        module.remove_tag("nonexistent")
        
        # Should not change anything
        assert len(module.tags) == 2
        assert "tag1" in module.tags
        assert "tag2" in module.tags
    
    def test_framework_remove_command_with_existing_command(self):
        """Test Framework remove_command method with existing command"""
        from data.models import Framework, Command
        
        framework = Framework(
            path="/test/.claude",
            commands=[],
            modules=[]
        )
        
        # Add some commands
        cmd1 = Command(name="cmd1", path="/commands/cmd1.md", category="command")
        cmd2 = Command(name="cmd2", path="/commands/cmd2.md", category="command")
        cmd3 = Command(name="cmd3", path="/commands/cmd3.md", category="command")
        
        framework.add_command(cmd1)
        framework.add_command(cmd2)
        framework.add_command(cmd3)
        
        # Remove existing command
        result = framework.remove_command("cmd2")
        
        assert result is True
        assert len(framework.commands) == 2
        assert framework.get_command_by_name("cmd2") is None
        assert framework.get_command_by_name("cmd1") is not None
        assert framework.get_command_by_name("cmd3") is not None
    
    def test_framework_remove_command_with_nonexistent_command(self):
        """Test Framework remove_command method with nonexistent command"""
        from data.models import Framework, Command
        
        framework = Framework(
            path="/test/.claude",
            commands=[],
            modules=[]
        )
        
        # Add a command
        cmd1 = Command(name="cmd1", path="/commands/cmd1.md", category="command")
        framework.add_command(cmd1)
        
        # Try to remove nonexistent command
        result = framework.remove_command("nonexistent")
        
        assert result is False
        assert len(framework.commands) == 1
        assert framework.get_command_by_name("cmd1") is not None
    
    def test_framework_remove_module_with_existing_module(self):
        """Test Framework remove_module method with existing module"""
        from data.models import Framework, Module
        
        framework = Framework(
            path="/test/.claude",
            commands=[],
            modules=[]
        )
        
        # Add some modules
        mod1 = Module(name="mod1", path="/modules/mod1.md", category="test")
        mod2 = Module(name="mod2", path="/modules/mod2.md", category="test")
        mod3 = Module(name="mod3", path="/modules/mod3.md", category="test")
        
        framework.add_module(mod1)
        framework.add_module(mod2)
        framework.add_module(mod3)
        
        # Remove existing module
        result = framework.remove_module("mod2")
        
        assert result is True
        assert len(framework.modules) == 2
        assert framework.get_module_by_name("mod2") is None
        assert framework.get_module_by_name("mod1") is not None
        assert framework.get_module_by_name("mod3") is not None
    
    def test_framework_remove_module_with_nonexistent_module(self):
        """Test Framework remove_module method with nonexistent module"""
        from data.models import Framework, Module
        
        framework = Framework(
            path="/test/.claude",
            commands=[],
            modules=[]
        )
        
        # Add a module
        mod1 = Module(name="mod1", path="/modules/mod1.md", category="test")
        framework.add_module(mod1)
        
        # Try to remove nonexistent module
        result = framework.remove_module("nonexistent")
        
        assert result is False
        assert len(framework.modules) == 1
        assert framework.get_module_by_name("mod1") is not None