"""
Data models for Claude Code Modular Prompts Framework Dashboard
Provides structured data representations for commands, modules, and framework components
"""

from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import time
from abc import ABC, abstractmethod


class BaseModel(ABC):
    """Abstract base class for all data models"""
    
    def __init__(self):
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary representation"""
        pass
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseModel':
        """Create model from dictionary data"""
        pass
    
    def update_metadata(self):
        """Update the updated_at timestamp"""
        self.updated_at = datetime.now().isoformat()


class Command(BaseModel):
    """Data model for framework commands"""
    
    def __init__(self, name: str, path: str, category: str, 
                 description: Optional[str] = None, 
                 usage: Optional[str] = None,
                 examples: Optional[List[str]] = None,
                 modules: Optional[List[str]] = None):
        """Initialize a Command model"""
        super().__init__()
        self._validate_required_fields(name, path, category)
        
        self.name = name
        self.path = path
        self.category = category
        self.description = description
        self.usage = usage
        self.examples = examples or []
        self.modules = modules or []
    
    def _validate_required_fields(self, name: str, path: str, category: str):
        """Validate required fields are not empty"""
        if not name:
            raise ValueError("name cannot be empty")
        if not path:
            raise ValueError("path cannot be empty")
        if not category:
            raise ValueError("category cannot be empty")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert Command to dictionary representation"""
        return {
            'name': self.name,
            'path': self.path,
            'category': self.category,
            'description': self.description,
            'usage': self.usage,
            'examples': self.examples,
            'modules': self.modules,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Command':
        """Create Command from dictionary data"""
        return cls(
            name=data['name'],
            path=data['path'],
            category=data['category'],
            description=data.get('description'),
            usage=data.get('usage'),
            examples=data.get('examples', []),
            modules=data.get('modules', [])
        )
    
    def __str__(self) -> str:
        """String representation of Command"""
        return f"Command({self.name}, {self.category})"
    
    def __eq__(self, other) -> bool:
        """Equality comparison based on name"""
        if not isinstance(other, Command):
            return False
        return self.name == other.name
    
    def __hash__(self) -> int:
        """Hash function for Command objects"""
        return hash(self.name)


class Module(BaseModel):
    """Data model for framework modules"""
    
    def __init__(self, name: str, path: str, category: str,
                 description: Optional[str] = None,
                 version: Optional[str] = None,
                 dependencies: Optional[List[str]] = None,
                 tags: Optional[List[str]] = None):
        """Initialize a Module model"""
        super().__init__()
        self._validate_required_fields(name, path, category)
        
        self.name = name
        self.path = path
        self.category = category
        self.description = description
        self.version = version
        self.dependencies = dependencies or []
        self.tags = tags or []
    
    def _validate_required_fields(self, name: str, path: str, category: str):
        """Validate required fields are not empty"""
        if not name:
            raise ValueError("name cannot be empty")
        if not path:
            raise ValueError("path cannot be empty")
        if not category:
            raise ValueError("category cannot be empty")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert Module to dictionary representation"""
        return {
            'name': self.name,
            'path': self.path,
            'category': self.category,
            'description': self.description,
            'version': self.version,
            'dependencies': self.dependencies,
            'tags': self.tags,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Module':
        """Create Module from dictionary data"""
        return cls(
            name=data['name'],
            path=data['path'],
            category=data['category'],
            description=data.get('description'),
            version=data.get('version'),
            dependencies=data.get('dependencies', []),
            tags=data.get('tags', [])
        )
    
    def __str__(self) -> str:
        """String representation of Module"""
        return f"Module({self.name}, {self.category})"
    
    def __eq__(self, other) -> bool:
        """Equality comparison based on name"""
        if not isinstance(other, Module):
            return False
        return self.name == other.name
    
    def __hash__(self) -> int:
        """Hash function for Module objects"""
        return hash(self.name)
    
    def add_dependency(self, dependency: str):
        """Add a dependency to the module"""
        if dependency not in self.dependencies:
            self.dependencies.append(dependency)
            self.update_metadata()
    
    def add_tag(self, tag: str):
        """Add a tag to the module"""
        if tag not in self.tags:
            self.tags.append(tag)
            self.update_metadata()
    
    def remove_dependency(self, dependency: str):
        """Remove a dependency from the module"""
        if dependency in self.dependencies:
            self.dependencies.remove(dependency)
            self.update_metadata()
    
    def remove_tag(self, tag: str):
        """Remove a tag from the module"""
        if tag in self.tags:
            self.tags.remove(tag)
            self.update_metadata()


class Framework(BaseModel):
    """Data model for the complete framework structure"""
    
    def __init__(self, path: str, commands: List[Command], modules: List[Module],
                 name: Optional[str] = None,
                 version: Optional[str] = None,
                 description: Optional[str] = None,
                 metadata: Optional[Dict[str, Any]] = None):
        """Initialize a Framework model"""
        super().__init__()
        self._validate_required_fields(path, commands, modules)
        
        self.path = path
        self.commands = commands
        self.modules = modules
        self.name = name
        self.version = version
        self.description = description
        self.metadata = metadata or {}
    
    def _validate_required_fields(self, path: str, commands: List[Command], modules: List[Module]):
        """Validate required fields"""
        if not path:
            raise ValueError("path cannot be empty")
        if not isinstance(commands, list):
            raise TypeError("commands must be a list")
        if not isinstance(modules, list):
            raise TypeError("modules must be a list")
    
    def add_command(self, command: Command):
        """Add a command to the framework"""
        self.commands.append(command)
        self.update_metadata()
    
    def add_module(self, module: Module):
        """Add a module to the framework"""
        self.modules.append(module)
        self.update_metadata()
    
    def get_command_by_name(self, name: str) -> Optional[Command]:
        """Get a command by name"""
        for command in self.commands:
            if command.name == name:
                return command
        return None
    
    def get_module_by_name(self, name: str) -> Optional[Module]:
        """Get a module by name"""
        for module in self.modules:
            if module.name == name:
                return module
        return None
    
    def get_modules_by_category(self, category: str) -> List[Module]:
        """Get all modules in a specific category"""
        return [module for module in self.modules if module.category == category]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert Framework to dictionary representation"""
        return {
            'path': self.path,
            'name': self.name,
            'version': self.version,
            'description': self.description,
            'commands': [command.to_dict() for command in self.commands],
            'modules': [module.to_dict() for module in self.modules],
            'metadata': self.metadata,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Framework':
        """Create Framework from dictionary data"""
        commands = [Command.from_dict(cmd_data) for cmd_data in data.get('commands', [])]
        modules = [Module.from_dict(mod_data) for mod_data in data.get('modules', [])]
        
        return cls(
            path=data['path'],
            commands=commands,
            modules=modules,
            name=data.get('name'),
            version=data.get('version'),
            description=data.get('description'),
            metadata=data.get('metadata', {})
        )
    
    def statistics(self) -> Dict[str, Any]:
        """Get framework statistics"""
        commands_by_category = self._count_by_category(self.commands)
        modules_by_category = self._count_by_category(self.modules)
        
        return {
            'total_commands': len(self.commands),
            'total_modules': len(self.modules),
            'total_components': len(self.commands) + len(self.modules),
            'commands_by_category': commands_by_category,
            'modules_by_category': modules_by_category
        }
    
    def _count_by_category(self, items: List[Union[Command, Module]]) -> Dict[str, int]:
        """Count items by category"""
        category_counts = {}
        for item in items:
            category = item.category
            if category not in category_counts:
                category_counts[category] = 0
            category_counts[category] += 1
        return category_counts
    
    def remove_command(self, command_name: str) -> bool:
        """Remove a command by name"""
        for i, command in enumerate(self.commands):
            if command.name == command_name:
                self.commands.pop(i)
                self.update_metadata()
                return True
        return False
    
    def remove_module(self, module_name: str) -> bool:
        """Remove a module by name"""
        for i, module in enumerate(self.modules):
            if module.name == module_name:
                self.modules.pop(i)
                self.update_metadata()
                return True
        return False