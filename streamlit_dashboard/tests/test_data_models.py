"""
TDD RED: Tests for data models
These tests define the expected behavior of command and module data models
"""

import pytest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, List, Optional, Any
from datetime import datetime

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestDataModelsExistence:
    """Test cases for data model module existence"""
    
    def test_data_models_module_exists(self):
        """Test that data models module exists"""
        from data.models import Command, Module, Framework
        assert Command is not None
        assert Module is not None
        assert Framework is not None
    
    def test_data_models_file_size_constraint(self):
        """Test that models.py is under 500 lines"""
        models_path = Path(__file__).parent.parent / "data" / "models.py"
        assert models_path.exists(), "models.py should exist"
        
        with open(models_path, 'r') as f:
            lines = f.readlines()
        
        # Remove empty lines and comments for more accurate count
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        
        assert len(code_lines) < 500, f"models.py should be <500 lines of code, found {len(code_lines)}"


class TestCommandModel:
    """Test cases for Command data model"""
    
    def test_command_model_initialization(self):
        """Test Command model can be initialized"""
        from data.models import Command
        
        command = Command(
            name="auto",
            path="/commands/auto.md",
            category="command"
        )
        
        assert command.name == "auto"
        assert command.path == "/commands/auto.md"
        assert command.category == "command"
    
    def test_command_model_has_required_attributes(self):
        """Test Command model has all required attributes"""
        from data.models import Command
        
        command = Command(
            name="task",
            path="/commands/task.md",
            category="command"
        )
        
        # Required attributes
        assert hasattr(command, 'name'), "Command should have 'name' attribute"
        assert hasattr(command, 'path'), "Command should have 'path' attribute"
        assert hasattr(command, 'category'), "Command should have 'category' attribute"
        
        # Optional attributes
        assert hasattr(command, 'description'), "Command should have 'description' attribute"
        assert hasattr(command, 'usage'), "Command should have 'usage' attribute"
        assert hasattr(command, 'examples'), "Command should have 'examples' attribute"
        assert hasattr(command, 'modules'), "Command should have 'modules' attribute"
        assert hasattr(command, 'created_at'), "Command should have 'created_at' attribute"
        assert hasattr(command, 'updated_at'), "Command should have 'updated_at' attribute"
    
    def test_command_model_validation(self):
        """Test Command model validation"""
        from data.models import Command
        
        # Test invalid name
        with pytest.raises(ValueError, match="name cannot be empty"):
            Command(name="", path="/commands/empty.md", category="command")
        
        # Test invalid path
        with pytest.raises(ValueError, match="path cannot be empty"):
            Command(name="test", path="", category="command")
        
        # Test invalid category
        with pytest.raises(ValueError, match="category cannot be empty"):
            Command(name="test", path="/commands/test.md", category="")
    
    def test_command_model_to_dict(self):
        """Test Command model to_dict method"""
        from data.models import Command
        
        command = Command(
            name="feature",
            path="/commands/feature.md",
            category="command",
            description="Feature development command"
        )
        
        result = command.to_dict()
        
        assert isinstance(result, dict), "to_dict should return dictionary"
        assert result['name'] == "feature"
        assert result['path'] == "/commands/feature.md"
        assert result['category'] == "command"
        assert result['description'] == "Feature development command"
        assert 'created_at' in result
        assert 'updated_at' in result
    
    def test_command_model_from_dict(self):
        """Test Command model from_dict class method"""
        from data.models import Command
        
        data = {
            'name': 'swarm',
            'path': '/commands/swarm.md',
            'category': 'command',
            'description': 'Multi-agent coordination',
            'usage': '/swarm "task description"',
            'examples': ['Example 1', 'Example 2']
        }
        
        command = Command.from_dict(data)
        
        assert command.name == "swarm"
        assert command.path == "/commands/swarm.md"
        assert command.category == "command"
        assert command.description == "Multi-agent coordination"
        assert command.usage == '/swarm "task description"'
        assert command.examples == ['Example 1', 'Example 2']
    
    def test_command_model_str_representation(self):
        """Test Command model string representation"""
        from data.models import Command
        
        command = Command(
            name="query",
            path="/commands/query.md",
            category="command"
        )
        
        str_repr = str(command)
        assert "query" in str_repr
        assert "command" in str_repr
    
    def test_command_model_equality(self):
        """Test Command model equality comparison"""
        from data.models import Command
        
        command1 = Command(name="test", path="/commands/test.md", category="command")
        command2 = Command(name="test", path="/commands/test.md", category="command")
        command3 = Command(name="other", path="/commands/other.md", category="command")
        
        assert command1 == command2, "Commands with same name should be equal"
        assert command1 != command3, "Commands with different names should not be equal"
    
    def test_command_model_update_metadata(self):
        """Test Command model update_metadata method"""
        from data.models import Command
        
        command = Command(
            name="protocol",
            path="/commands/protocol.md",
            category="command"
        )
        
        original_updated_at = command.updated_at
        
        # Mock sleep to ensure time difference
        with patch('time.sleep'):
            command.update_metadata()
        
        assert command.updated_at != original_updated_at


class TestModuleModel:
    """Test cases for Module data model"""
    
    def test_module_model_initialization(self):
        """Test Module model can be initialized"""
        from data.models import Module
        
        module = Module(
            name="tdd-cycle-pattern",
            path="/modules/patterns/tdd-cycle-pattern.md",
            category="patterns"
        )
        
        assert module.name == "tdd-cycle-pattern"
        assert module.path == "/modules/patterns/tdd-cycle-pattern.md"
        assert module.category == "patterns"
    
    def test_module_model_has_required_attributes(self):
        """Test Module model has all required attributes"""
        from data.models import Module
        
        module = Module(
            name="intelligent-routing",
            path="/modules/patterns/intelligent-routing.md",
            category="patterns"
        )
        
        # Required attributes
        assert hasattr(module, 'name'), "Module should have 'name' attribute"
        assert hasattr(module, 'path'), "Module should have 'path' attribute"
        assert hasattr(module, 'category'), "Module should have 'category' attribute"
        
        # Optional attributes
        assert hasattr(module, 'description'), "Module should have 'description' attribute"
        assert hasattr(module, 'version'), "Module should have 'version' attribute"
        assert hasattr(module, 'dependencies'), "Module should have 'dependencies' attribute"
        assert hasattr(module, 'tags'), "Module should have 'tags' attribute"
        assert hasattr(module, 'created_at'), "Module should have 'created_at' attribute"
        assert hasattr(module, 'updated_at'), "Module should have 'updated_at' attribute"
    
    def test_module_model_validation(self):
        """Test Module model validation"""
        from data.models import Module
        
        # Test invalid name
        with pytest.raises(ValueError, match="name cannot be empty"):
            Module(name="", path="/modules/patterns/empty.md", category="patterns")
        
        # Test invalid path
        with pytest.raises(ValueError, match="path cannot be empty"):
            Module(name="test", path="", category="patterns")
        
        # Test invalid category
        with pytest.raises(ValueError, match="category cannot be empty"):
            Module(name="test", path="/modules/patterns/test.md", category="")
    
    def test_module_model_to_dict(self):
        """Test Module model to_dict method"""
        from data.models import Module
        
        module = Module(
            name="security-validator",
            path="/modules/security/security-validator.md",
            category="security",
            description="Security validation module",
            version="1.0.0"
        )
        
        result = module.to_dict()
        
        assert isinstance(result, dict), "to_dict should return dictionary"
        assert result['name'] == "security-validator"
        assert result['path'] == "/modules/security/security-validator.md"
        assert result['category'] == "security"
        assert result['description'] == "Security validation module"
        assert result['version'] == "1.0.0"
        assert 'created_at' in result
        assert 'updated_at' in result
    
    def test_module_model_from_dict(self):
        """Test Module model from_dict class method"""
        from data.models import Module
        
        data = {
            'name': 'context-manager',
            'path': '/modules/context/context-manager.md',
            'category': 'context',
            'description': 'Context management module',
            'version': '2.1.0',
            'dependencies': ['base-module'],
            'tags': ['context', 'management']
        }
        
        module = Module.from_dict(data)
        
        assert module.name == "context-manager"
        assert module.path == "/modules/context/context-manager.md"
        assert module.category == "context"
        assert module.description == "Context management module"
        assert module.version == "2.1.0"
        assert module.dependencies == ['base-module']
        assert module.tags == ['context', 'management']
    
    def test_module_model_str_representation(self):
        """Test Module model string representation"""
        from data.models import Module
        
        module = Module(
            name="workflow-orchestration",
            path="/modules/patterns/workflow-orchestration.md",
            category="patterns"
        )
        
        str_repr = str(module)
        assert "workflow-orchestration" in str_repr
        assert "patterns" in str_repr
    
    def test_module_model_equality(self):
        """Test Module model equality comparison"""
        from data.models import Module
        
        module1 = Module(name="test", path="/modules/test.md", category="general")
        module2 = Module(name="test", path="/modules/test.md", category="general")
        module3 = Module(name="other", path="/modules/other.md", category="general")
        
        assert module1 == module2, "Modules with same name should be equal"
        assert module1 != module3, "Modules with different names should not be equal"
    
    def test_module_model_add_dependency(self):
        """Test Module model add_dependency method"""
        from data.models import Module
        
        module = Module(
            name="advanced-module",
            path="/modules/advanced/advanced-module.md",
            category="advanced"
        )
        
        module.add_dependency("base-module")
        module.add_dependency("helper-module")
        
        assert "base-module" in module.dependencies
        assert "helper-module" in module.dependencies
        assert len(module.dependencies) == 2
    
    def test_module_model_add_tag(self):
        """Test Module model add_tag method"""
        from data.models import Module
        
        module = Module(
            name="tagged-module",
            path="/modules/tagged/tagged-module.md",
            category="tagged"
        )
        
        module.add_tag("important")
        module.add_tag("experimental")
        
        assert "important" in module.tags
        assert "experimental" in module.tags
        assert len(module.tags) == 2


class TestFrameworkModel:
    """Test cases for Framework data model"""
    
    def test_framework_model_initialization(self):
        """Test Framework model can be initialized"""
        from data.models import Framework
        
        framework = Framework(
            path="/path/to/.claude",
            commands=[],
            modules=[]
        )
        
        assert framework.path == "/path/to/.claude"
        assert framework.commands == []
        assert framework.modules == []
    
    def test_framework_model_has_required_attributes(self):
        """Test Framework model has all required attributes"""
        from data.models import Framework
        
        framework = Framework(
            path="/path/to/.claude",
            commands=[],
            modules=[]
        )
        
        # Required attributes
        assert hasattr(framework, 'path'), "Framework should have 'path' attribute"
        assert hasattr(framework, 'commands'), "Framework should have 'commands' attribute"
        assert hasattr(framework, 'modules'), "Framework should have 'modules' attribute"
        
        # Optional attributes
        assert hasattr(framework, 'name'), "Framework should have 'name' attribute"
        assert hasattr(framework, 'version'), "Framework should have 'version' attribute"
        assert hasattr(framework, 'description'), "Framework should have 'description' attribute"
        assert hasattr(framework, 'metadata'), "Framework should have 'metadata' attribute"
        assert hasattr(framework, 'created_at'), "Framework should have 'created_at' attribute"
        assert hasattr(framework, 'updated_at'), "Framework should have 'updated_at' attribute"
    
    def test_framework_model_validation(self):
        """Test Framework model validation"""
        from data.models import Framework
        
        # Test invalid path
        with pytest.raises(ValueError, match="path cannot be empty"):
            Framework(path="", commands=[], modules=[])
        
        # Test invalid commands type
        with pytest.raises(TypeError, match="commands must be a list"):
            Framework(path="/path", commands="not a list", modules=[])
        
        # Test invalid modules type
        with pytest.raises(TypeError, match="modules must be a list"):
            Framework(path="/path", commands=[], modules="not a list")
    
    def test_framework_model_add_command(self):
        """Test Framework model add_command method"""
        from data.models import Framework, Command
        
        framework = Framework(
            path="/path/to/.claude",
            commands=[],
            modules=[]
        )
        
        command = Command(
            name="test-command",
            path="/commands/test-command.md",
            category="command"
        )
        
        framework.add_command(command)
        
        assert len(framework.commands) == 1
        assert framework.commands[0].name == "test-command"
    
    def test_framework_model_add_module(self):
        """Test Framework model add_module method"""
        from data.models import Framework, Module
        
        framework = Framework(
            path="/path/to/.claude",
            commands=[],
            modules=[]
        )
        
        module = Module(
            name="test-module",
            path="/modules/test-module.md",
            category="test"
        )
        
        framework.add_module(module)
        
        assert len(framework.modules) == 1
        assert framework.modules[0].name == "test-module"
    
    def test_framework_model_get_command_by_name(self):
        """Test Framework model get_command_by_name method"""
        from data.models import Framework, Command
        
        framework = Framework(
            path="/path/to/.claude",
            commands=[],
            modules=[]
        )
        
        command = Command(
            name="findme",
            path="/commands/findme.md",
            category="command"
        )
        
        framework.add_command(command)
        
        found_command = framework.get_command_by_name("findme")
        assert found_command is not None
        assert found_command.name == "findme"
        
        not_found = framework.get_command_by_name("nonexistent")
        assert not_found is None
    
    def test_framework_model_get_module_by_name(self):
        """Test Framework model get_module_by_name method"""
        from data.models import Framework, Module
        
        framework = Framework(
            path="/path/to/.claude",
            commands=[],
            modules=[]
        )
        
        module = Module(
            name="findme",
            path="/modules/findme.md",
            category="test"
        )
        
        framework.add_module(module)
        
        found_module = framework.get_module_by_name("findme")
        assert found_module is not None
        assert found_module.name == "findme"
        
        not_found = framework.get_module_by_name("nonexistent")
        assert not_found is None
    
    def test_framework_model_get_modules_by_category(self):
        """Test Framework model get_modules_by_category method"""
        from data.models import Framework, Module
        
        framework = Framework(
            path="/path/to/.claude",
            commands=[],
            modules=[]
        )
        
        module1 = Module(name="pattern1", path="/modules/patterns/pattern1.md", category="patterns")
        module2 = Module(name="pattern2", path="/modules/patterns/pattern2.md", category="patterns")
        module3 = Module(name="security1", path="/modules/security/security1.md", category="security")
        
        framework.add_module(module1)
        framework.add_module(module2)
        framework.add_module(module3)
        
        patterns = framework.get_modules_by_category("patterns")
        assert len(patterns) == 2
        assert all(module.category == "patterns" for module in patterns)
        
        security = framework.get_modules_by_category("security")
        assert len(security) == 1
        assert security[0].category == "security"
        
        nonexistent = framework.get_modules_by_category("nonexistent")
        assert len(nonexistent) == 0
    
    def test_framework_model_to_dict(self):
        """Test Framework model to_dict method"""
        from data.models import Framework, Command, Module
        
        framework = Framework(
            path="/path/to/.claude",
            commands=[],
            modules=[],
            name="Test Framework",
            version="1.0.0"
        )
        
        command = Command(name="test-cmd", path="/commands/test-cmd.md", category="command")
        module = Module(name="test-mod", path="/modules/test-mod.md", category="test")
        
        framework.add_command(command)
        framework.add_module(module)
        
        result = framework.to_dict()
        
        assert isinstance(result, dict), "to_dict should return dictionary"
        assert result['path'] == "/path/to/.claude"
        assert result['name'] == "Test Framework"
        assert result['version'] == "1.0.0"
        assert len(result['commands']) == 1
        assert len(result['modules']) == 1
        assert 'created_at' in result
        assert 'updated_at' in result
    
    def test_framework_model_from_dict(self):
        """Test Framework model from_dict class method"""
        from data.models import Framework
        
        data = {
            'path': '/path/to/.claude',
            'name': 'Test Framework',
            'version': '2.0.0',
            'description': 'A test framework',
            'commands': [
                {'name': 'test-cmd', 'path': '/commands/test-cmd.md', 'category': 'command'}
            ],
            'modules': [
                {'name': 'test-mod', 'path': '/modules/test-mod.md', 'category': 'test'}
            ]
        }
        
        framework = Framework.from_dict(data)
        
        assert framework.path == '/path/to/.claude'
        assert framework.name == 'Test Framework'
        assert framework.version == '2.0.0'
        assert framework.description == 'A test framework'
        assert len(framework.commands) == 1
        assert len(framework.modules) == 1
        assert framework.commands[0].name == 'test-cmd'
        assert framework.modules[0].name == 'test-mod'
    
    def test_framework_model_statistics(self):
        """Test Framework model statistics method"""
        from data.models import Framework, Command, Module
        
        framework = Framework(
            path="/path/to/.claude",
            commands=[],
            modules=[]
        )
        
        # Add some commands and modules
        for i in range(3):
            command = Command(name=f"cmd{i}", path=f"/commands/cmd{i}.md", category="command")
            framework.add_command(command)
        
        for i in range(5):
            module = Module(name=f"mod{i}", path=f"/modules/mod{i}.md", category="test")
            framework.add_module(module)
        
        stats = framework.statistics()
        
        assert stats['total_commands'] == 3
        assert stats['total_modules'] == 5
        assert stats['total_components'] == 8
        assert 'commands_by_category' in stats
        assert 'modules_by_category' in stats
        assert stats['modules_by_category']['test'] == 5


class TestDataModelsIntegration:
    """Test cases for data models integration"""
    
    def test_models_work_with_framework_parser(self):
        """Test that models integrate with framework parser"""
        from data.models import Framework, Command, Module
        from data.framework_parser import FrameworkParser
        
        # This test should work with our existing parser
        # We're testing the integration between parser and models
        
        # Create mock parser data
        parser_data = {
            'commands': [
                {'name': 'auto', 'path': '/commands/auto.md', 'category': 'command'},
                {'name': 'task', 'path': '/commands/task.md', 'category': 'command'}
            ],
            'modules': [
                {'name': 'tdd-cycle', 'path': '/modules/patterns/tdd-cycle.md', 'category': 'patterns'},
                {'name': 'security', 'path': '/modules/security/security.md', 'category': 'security'}
            ]
        }
        
        # Create framework from parser data
        framework = Framework.from_dict({
            'path': '/path/to/.claude',
            'commands': parser_data['commands'],
            'modules': parser_data['modules']
        })
        
        assert len(framework.commands) == 2
        assert len(framework.modules) == 2
        assert framework.commands[0].name == 'auto'
        assert framework.modules[0].name == 'tdd-cycle'
    
    def test_models_follow_separation_of_concerns(self):
        """Test that models follow single responsibility principle"""
        from data.models import Command, Module, Framework
        import inspect
        
        # Check Command model methods
        command_methods = [name for name, obj in inspect.getmembers(Command) 
                          if inspect.ismethod(obj) or inspect.isfunction(obj)]
        
        # Should have focused responsibility - representing command data only
        public_command_methods = [m for m in command_methods if not m.startswith('_')]
        assert len(public_command_methods) <= 10, f"Command should have ≤10 public methods, found {len(public_command_methods)}"
        
        # Check Module model methods
        module_methods = [name for name, obj in inspect.getmembers(Module) 
                         if inspect.ismethod(obj) or inspect.isfunction(obj)]
        
        public_module_methods = [m for m in module_methods if not m.startswith('_')]
        assert len(public_module_methods) <= 12, f"Module should have ≤12 public methods, found {len(public_module_methods)}"
        
        # Check Framework model methods
        framework_methods = [name for name, obj in inspect.getmembers(Framework) 
                           if inspect.ismethod(obj) or inspect.isfunction(obj)]
        
        public_framework_methods = [m for m in framework_methods if not m.startswith('_')]
        assert len(public_framework_methods) <= 15, f"Framework should have ≤15 public methods, found {len(public_framework_methods)}"
    
    def test_models_have_minimal_imports(self):
        """Test that models.py has minimal imports"""
        models_path = Path(__file__).parent.parent / "data" / "models.py"
        with open(models_path, 'r') as f:
            source = f.read()
        
        # Should import only necessary modules
        assert "from typing import" in source, "Should import typing for type hints"
        assert "from datetime import" in source, "Should import datetime for timestamps"
        
        # Should NOT import UI or framework-specific modules
        forbidden_imports = [
            "import streamlit",
            "from components.",
            "from app import",
            "import plotly",
            "import pandas",
            "from data.framework_parser import"
        ]
        
        for forbidden in forbidden_imports:
            assert forbidden not in source, f"Models should not import framework-specific modules: {forbidden}"


class TestDataModelsEdgeCases:
    """Test cases for edge cases and error conditions"""
    
    def test_command_model_with_none_values(self):
        """Test Command model handles None values appropriately"""
        from data.models import Command
        
        command = Command(
            name="test",
            path="/commands/test.md",
            category="command",
            description=None,
            usage=None
        )
        
        assert command.description is None
        assert command.usage is None
        
        # to_dict should handle None values
        result = command.to_dict()
        assert result['description'] is None
        assert result['usage'] is None
    
    def test_module_model_with_empty_lists(self):
        """Test Module model handles empty lists"""
        from data.models import Module
        
        module = Module(
            name="empty-module",
            path="/modules/empty-module.md",
            category="test",
            dependencies=[],
            tags=[]
        )
        
        assert module.dependencies == []
        assert module.tags == []
        
        # Adding to empty lists should work
        module.add_dependency("test-dep")
        module.add_tag("test-tag")
        
        assert len(module.dependencies) == 1
        assert len(module.tags) == 1
    
    def test_framework_model_with_duplicate_names(self):
        """Test Framework model handles duplicate names"""
        from data.models import Framework, Command, Module
        
        framework = Framework(
            path="/path/to/.claude",
            commands=[],
            modules=[]
        )
        
        command1 = Command(name="duplicate", path="/commands/duplicate1.md", category="command")
        command2 = Command(name="duplicate", path="/commands/duplicate2.md", category="command")
        
        framework.add_command(command1)
        framework.add_command(command2)
        
        # Should contain both commands
        assert len(framework.commands) == 2
        
        # get_command_by_name should return the first one
        found = framework.get_command_by_name("duplicate")
        assert found.path == "/commands/duplicate1.md"
    
    def test_data_models_cyclomatic_complexity(self):
        """Test that data models have acceptable cyclomatic complexity"""
        from data.models import Command, Module, Framework
        import ast
        import inspect
        import textwrap
        
        # Simple complexity check - count decision points (if, for, while, etc.)
        def count_decision_points(source):
            # Clean up indentation
            dedented_source = textwrap.dedent(source)
            tree = ast.parse(dedented_source)
            decision_nodes = (ast.If, ast.For, ast.While, ast.Try, ast.With)
            return sum(1 for node in ast.walk(tree) if isinstance(node, decision_nodes))
        
        # Check each model class
        for model_class in [Command, Module, Framework]:
            for method_name, method in inspect.getmembers(model_class, inspect.isfunction):
                if not method_name.startswith('_'):  # Only check public methods
                    try:
                        source = inspect.getsource(method)
                        complexity = count_decision_points(source)
                        assert complexity <= 10, f"{model_class.__name__}.{method_name} has complexity {complexity} > 10"
                    except (OSError, TypeError, IndentationError):
                        # Skip methods we can't get source for or parse
                        pass