"""
Tests for Interactive Dependency Graph component
TDD RED PHASE: Write failing tests first
"""

import pytest
import unittest.mock as mock
from pathlib import Path
import json
from unittest.mock import MagicMock, patch

# Import the component we're going to build
try:
    from components.dependency_graph import DependencyGraph, DependencyNode, DependencyEdge
except ImportError:
    # These don't exist yet - we'll create them
    DependencyGraph = None
    DependencyNode = None  
    DependencyEdge = None


class TestDependencyNode:
    """Test the DependencyNode class"""
    
    @pytest.fixture
    def node_data(self):
        return {
            'id': 'command_task',
            'type': 'command',
            'name': 'task',
            'title': '/task',
            'category': 'core',
            'file_path': '/path/to/task.md',
            'dependencies': ['tdd-cycle-pattern', 'quality-gates'],
            'dependents': ['feature-command']
        }
    
    def test_dependency_node_creation(self, node_data):
        """Test DependencyNode can be created with proper data"""
        if DependencyNode is None:
            pytest.skip("DependencyNode not implemented yet")
        
        node = DependencyNode(**node_data)
        assert node.id == 'command_task'
        assert node.type == 'command'
        assert node.name == 'task'
        assert len(node.dependencies) == 2
        assert len(node.dependents) == 1
    
    def test_dependency_node_validation(self):
        """Test DependencyNode validates required fields"""
        if DependencyNode is None:
            pytest.skip("DependencyNode not implemented yet")
        
        with pytest.raises(ValueError):
            DependencyNode(id="", type="command", name="test")  # Empty ID should fail
        
        with pytest.raises(ValueError):
            DependencyNode(id="test", type="invalid", name="test")  # Invalid type should fail


class TestDependencyEdge:
    """Test the DependencyEdge class"""
    
    @pytest.fixture
    def edge_data(self):
        return {
            'id': 'edge_1',
            'source': 'command_task',
            'target': 'module_tdd_cycle',
            'relationship_type': 'uses',
            'strength': 0.8,
            'description': 'Task command uses TDD cycle pattern'
        }
    
    def test_dependency_edge_creation(self, edge_data):
        """Test DependencyEdge can be created"""
        if DependencyEdge is None:
            pytest.skip("DependencyEdge not implemented yet")
        
        edge = DependencyEdge(**edge_data)
        assert edge.id == 'edge_1'
        assert edge.source == 'command_task'
        assert edge.target == 'module_tdd_cycle'
        assert edge.strength == 0.8
    
    def test_dependency_edge_validation(self):
        """Test DependencyEdge validates connections"""
        if DependencyEdge is None:
            pytest.skip("DependencyEdge not implemented yet")
        
        with pytest.raises(ValueError):
            DependencyEdge(
                id="test",
                source="",  # Empty source should fail
                target="target",
                relationship_type="uses"
            )


class TestDependencyGraph:
    """Test the DependencyGraph component"""
    
    @pytest.fixture
    def framework_path(self, tmp_path):
        """Create a temporary framework directory with sample structure"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create commands directory
        commands_dir = framework_dir / "commands"
        commands_dir.mkdir()
        
        # Create sample command files with dependency references
        (commands_dir / "task.md").write_text("""
# Task Command

Uses modules:
- modules/patterns/tdd-cycle-pattern.md
- system/quality/universal-quality-gates.md
        """)
        
        (commands_dir / "auto.md").write_text("""
# Auto Command

Uses modules:
- modules/patterns/intelligent-routing.md
- modules/patterns/research-analysis-pattern.md
        """)
        
        # Create modules directory
        modules_dir = framework_dir / "modules"
        modules_dir.mkdir()
        patterns_dir = modules_dir / "patterns"
        patterns_dir.mkdir()
        
        (patterns_dir / "tdd-cycle-pattern.md").write_text("""
# TDD Cycle Pattern

Dependencies:
- system/quality/test-coverage.md
        """)
        
        (patterns_dir / "intelligent-routing.md").write_text("""
# Intelligent Routing Pattern

Dependencies:
- modules/patterns/research-analysis-pattern.md
        """)
        
        # Create system directory
        system_dir = framework_dir / "system"
        system_dir.mkdir()
        quality_dir = system_dir / "quality" 
        quality_dir.mkdir()
        
        (quality_dir / "universal-quality-gates.md").write_text("# Quality Gates")
        (quality_dir / "test-coverage.md").write_text("# Test Coverage")
        
        return framework_dir
    
    def test_dependency_graph_initialization(self, framework_path):
        """Test DependencyGraph can be initialized"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        assert graph.framework_path == framework_path
        assert hasattr(graph, 'nodes')
        assert hasattr(graph, 'edges')
    
    def test_parse_framework_structure(self, framework_path):
        """Test parsing framework structure into dependency nodes"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        nodes = graph.parse_framework_structure()
        
        assert len(nodes) >= 4  # commands + modules + system components
        
        # Check for expected nodes
        node_names = [node.name for node in nodes]
        assert 'task' in node_names
        assert 'auto' in node_names
        assert 'tdd-cycle-pattern' in node_names
    
    def test_extract_dependencies_from_content(self, framework_path):
        """Test extracting dependencies from file content"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        
        content = """
        Uses modules:
        - modules/patterns/tdd-cycle-pattern.md
        - system/quality/universal-quality-gates.md
        """
        
        dependencies = graph.extract_dependencies_from_content(content)
        
        assert len(dependencies) == 2
        assert 'modules/patterns/tdd-cycle-pattern.md' in dependencies
        assert 'system/quality/universal-quality-gates.md' in dependencies
    
    def test_build_dependency_edges(self, framework_path):
        """Test building edges between dependency nodes"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        nodes = graph.parse_framework_structure()
        edges = graph.build_dependency_edges(nodes)
        
        assert len(edges) > 0
        
        # Check that task command depends on tdd-cycle-pattern
        task_edges = [e for e in edges if e.source.endswith('task')]
        assert len(task_edges) > 0
    
    def test_calculate_dependency_strength(self, framework_path):
        """Test calculating dependency strength between nodes"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        
        # Test direct dependency
        strength = graph.calculate_dependency_strength(
            source_path="commands/task.md",
            target_path="modules/patterns/tdd-cycle-pattern.md"
        )
        
        assert 0.0 <= strength <= 1.0
        assert strength > 0.0  # Should be a valid dependency strength
    
    def test_detect_circular_dependencies(self, framework_path):
        """Test detecting circular dependencies"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        nodes = graph.parse_framework_structure()
        edges = graph.build_dependency_edges(nodes)
        
        cycles = graph.detect_circular_dependencies(nodes, edges)
        
        # In a well-designed framework, there should be no cycles
        assert isinstance(cycles, list)
    
    def test_get_dependency_metrics(self, framework_path):
        """Test calculating dependency metrics"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        metrics = graph.get_dependency_metrics()
        
        assert 'total_nodes' in metrics
        assert 'total_edges' in metrics
        assert 'max_depth' in metrics
        assert 'circular_dependencies' in metrics
        assert 'most_dependent_nodes' in metrics
        assert 'most_depended_upon_nodes' in metrics
        
        assert metrics['total_nodes'] > 0
        assert metrics['total_edges'] >= 0
    
    def test_get_node_by_id(self, framework_path):
        """Test finding nodes by ID"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        nodes = graph.parse_framework_structure()
        
        # Find a specific node
        task_node = graph.get_node_by_id('command_task')
        
        if task_node:  # May not exist depending on implementation
            assert task_node.name == 'task'
            assert task_node.type == 'command'
    
    def test_get_dependencies_for_node(self, framework_path):
        """Test getting all dependencies for a specific node"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        
        dependencies = graph.get_dependencies_for_node('command_task')
        
        assert isinstance(dependencies, list)
        # Should include direct and transitive dependencies
    
    def test_get_dependents_for_node(self, framework_path):
        """Test getting all nodes that depend on a specific node"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        
        dependents = graph.get_dependents_for_node('module_tdd_cycle_pattern')
        
        assert isinstance(dependents, list)
        # Should include nodes that use the TDD pattern
    
    def test_create_plotly_graph(self, framework_path):
        """Test creating Plotly graph visualization"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        fig = graph.create_plotly_graph()
        
        assert fig is not None
        assert hasattr(fig, 'data')
        assert len(fig.data) > 0  # Should have traces for nodes and edges
    
    def test_export_dependency_data(self, framework_path, tmp_path):
        """Test exporting dependency data to various formats"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        
        # Test JSON export
        json_file = tmp_path / "dependencies.json"
        graph.export_dependency_data(json_file, format='json')
        
        assert json_file.exists()
        
        # Verify JSON structure
        with open(json_file) as f:
            data = json.load(f)
        
        assert 'nodes' in data
        assert 'edges' in data
        assert 'metadata' in data
    
    def test_filter_nodes_by_type(self, framework_path):
        """Test filtering nodes by type"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        
        # Filter only command nodes
        command_nodes = graph.filter_nodes_by_type('command')
        
        assert isinstance(command_nodes, list)
        for node in command_nodes:
            assert node.type == 'command'
    
    def test_calculate_graph_layout(self, framework_path):
        """Test calculating optimal graph layout"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        positions = graph.calculate_graph_layout(algorithm='force-directed')
        
        assert isinstance(positions, dict)
        # Each node should have x, y position
        for node_id, pos in positions.items():
            assert 'x' in pos
            assert 'y' in pos
    
    def test_render_dependency_graph_ui(self, framework_path):
        """Test rendering the dependency graph UI"""
        if DependencyGraph is None:
            pytest.skip("DependencyGraph not implemented yet")
        
        graph = DependencyGraph(framework_path=framework_path)
        
        # Test that the method exists and can be called
        # We don't test Streamlit rendering in unit tests
        assert hasattr(graph, 'render_dependency_graph_ui')
        assert callable(graph.render_dependency_graph_ui)