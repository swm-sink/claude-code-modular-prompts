#!/usr/bin/env python3
"""
Unit tests for component dependency resolution.
"""

import unittest
from pathlib import Path
import re
from collections import defaultdict

class TestComponentDependencyResolution(unittest.TestCase):
    """Test component dependency resolution and circular dependency detection."""
    
    def setUp(self):
        """Set up test environment."""
        self.framework_root = Path("claude_prompt_factory")
        self.components_dir = self.framework_root / "components"
        self.dependency_graph = defaultdict(set)
    
    def build_dependency_graph(self):
        """Build a graph of component dependencies."""
        if not self.components_dir.exists():
            return
        
        for component_file in self.components_dir.rglob("*.md"):
            if component_file.name == "README.md":
                continue
            
            component_name = str(component_file.relative_to(self.framework_root))
            
            with open(component_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all includes
            includes = re.findall(r'<include component="([^"]+)" />', content)
            
            for included in includes:
                # Normalize the path
                if included.startswith('components/'):
                    self.dependency_graph[component_name].add(included)
                else:
                    # Assume it's relative to components dir
                    self.dependency_graph[component_name].add(f"components/{included}")
    
    def test_no_circular_dependencies(self):
        """Test that there are no circular dependencies."""
        self.build_dependency_graph()
        
        def has_cycle(node, visited, rec_stack):
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in self.dependency_graph.get(node, []):
                if neighbor not in visited:
                    if has_cycle(neighbor, visited, rec_stack):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(node)
            return False
        
        visited = set()
        for node in self.dependency_graph:
            if node not in visited:
                rec_stack = set()
                if has_cycle(node, visited, rec_stack):
                    self.fail(f"Circular dependency detected starting from {node}")
    
    def test_all_dependencies_exist(self):
        """Test that all included components actually exist."""
        self.build_dependency_graph()
        
        missing_dependencies = []
        
        for component, dependencies in self.dependency_graph.items():
            for dep in dependencies:
                dep_path = self.framework_root / dep
                if not dep_path.exists():
                    # Try without .md extension
                    if not Path(str(dep_path) + '.md').exists():
                        missing_dependencies.append((component, dep))
        
        if missing_dependencies:
            error_msg = "Missing dependencies found:\n"
            for comp, dep in missing_dependencies[:5]:  # Show first 5
                error_msg += f"  {comp} -> {dep}\n"
            if len(missing_dependencies) > 5:
                error_msg += f"  ... and {len(missing_dependencies) - 5} more\n"
            self.fail(error_msg)
    
    def test_dependency_depth(self):
        """Test that dependency chains are not too deep."""
        self.build_dependency_graph()
        
        def get_max_depth(node, visited=None):
            if visited is None:
                visited = set()
            
            if node in visited:
                return 0  # Circular dependency, handled elsewhere
            
            visited.add(node)
            
            if node not in self.dependency_graph:
                return 1
            
            max_child_depth = 0
            for child in self.dependency_graph[node]:
                child_depth = get_max_depth(child, visited.copy())
                max_child_depth = max(max_child_depth, child_depth)
            
            return 1 + max_child_depth
        
        max_allowed_depth = 10
        deep_components = []
        
        for component in self.dependency_graph:
            depth = get_max_depth(component)
            if depth > max_allowed_depth:
                deep_components.append((component, depth))
        
        if deep_components:
            error_msg = f"Components with dependency depth > {max_allowed_depth}:\n"
            for comp, depth in deep_components[:3]:
                error_msg += f"  {comp}: depth {depth}\n"
            self.fail(error_msg)
    
    def test_core_components_minimal_dependencies(self):
        """Test that core components have minimal dependencies."""
        core_components = [
            "components/constitutional/safety-framework.md",
            "components/validation/input-validation.md",
            "components/workflow/command-execution.md"
        ]
        
        self.build_dependency_graph()
        
        for core_comp in core_components:
            if core_comp in self.dependency_graph:
                dep_count = len(self.dependency_graph[core_comp])
                self.assertLessEqual(dep_count, 3, 
                    f"Core component {core_comp} has too many dependencies: {dep_count}")
    
    def test_no_self_dependencies(self):
        """Test that no component includes itself."""
        self.build_dependency_graph()
        
        self_dependencies = []
        for component, dependencies in self.dependency_graph.items():
            if component in dependencies:
                self_dependencies.append(component)
        
        if self_dependencies:
            self.fail(f"Components with self-dependencies: {', '.join(self_dependencies)}")

if __name__ == '__main__':
    unittest.main()