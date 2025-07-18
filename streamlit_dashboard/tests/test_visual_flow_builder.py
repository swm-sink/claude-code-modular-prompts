"""
Tests for Visual Flow Builder component
TDD RED PHASE: Write failing tests first
"""

import pytest
import unittest.mock as mock
from pathlib import Path
import streamlit as st
import json
from unittest.mock import MagicMock, patch

# Import the component we're going to build
try:
    from components.visual_flow_builder import VisualFlowBuilder, FlowNode, FlowConnection
except ImportError:
    # These don't exist yet - we'll create them
    VisualFlowBuilder = None
    FlowNode = None
    FlowConnection = None


class TestFlowNode:
    """Test the FlowNode class"""
    
    @pytest.fixture
    def node_data(self):
        return {
            'id': 'node_1',
            'type': 'command',
            'title': '/task',
            'content': 'Task execution command',
            'position': {'x': 100, 'y': 200},
            'inputs': [{'name': 'request', 'type': 'string'}],
            'outputs': [{'name': 'result', 'type': 'object'}]
        }
    
    def test_flow_node_creation(self, node_data):
        """Test FlowNode can be created with proper data"""
        if FlowNode is None:
            pytest.skip("FlowNode not implemented yet")
        
        node = FlowNode(**node_data)
        assert node.id == 'node_1'
        assert node.type == 'command'
        assert node.title == '/task'
        assert node.position['x'] == 100
        assert len(node.inputs) == 1
        assert len(node.outputs) == 1
    
    def test_flow_node_serialization(self, node_data):
        """Test FlowNode can be serialized to/from JSON"""
        if FlowNode is None:
            pytest.skip("FlowNode not implemented yet")
        
        node = FlowNode(**node_data)
        serialized = node.to_dict()
        
        assert serialized['id'] == 'node_1'
        assert serialized['type'] == 'command'
        
        # Test deserialization
        new_node = FlowNode.from_dict(serialized)
        assert new_node.id == node.id
        assert new_node.type == node.type
    
    def test_flow_node_validation(self):
        """Test FlowNode validates required fields"""
        if FlowNode is None:
            pytest.skip("FlowNode not implemented yet")
        
        with pytest.raises(ValueError):
            FlowNode(id="", type="command", title="test")  # Empty ID should fail
        
        with pytest.raises(ValueError):
            FlowNode(id="test", type="invalid", title="test")  # Invalid type should fail


class TestFlowConnection:
    """Test the FlowConnection class"""
    
    @pytest.fixture
    def connection_data(self):
        return {
            'id': 'conn_1',
            'source_node': 'node_1',
            'source_output': 'result',
            'target_node': 'node_2', 
            'target_input': 'request'
        }
    
    def test_flow_connection_creation(self, connection_data):
        """Test FlowConnection can be created"""
        if FlowConnection is None:
            pytest.skip("FlowConnection not implemented yet")
        
        conn = FlowConnection(**connection_data)
        assert conn.id == 'conn_1'
        assert conn.source_node == 'node_1'
        assert conn.target_node == 'node_2'
    
    def test_flow_connection_validation(self):
        """Test FlowConnection validates connections"""
        if FlowConnection is None:
            pytest.skip("FlowConnection not implemented yet")
        
        with pytest.raises(ValueError):
            FlowConnection(
                id="test",
                source_node="",  # Empty source should fail
                source_output="out",
                target_node="target",
                target_input="in"
            )


class TestVisualFlowBuilder:
    """Test the VisualFlowBuilder component"""
    
    @pytest.fixture
    def framework_path(self, tmp_path):
        """Create a temporary framework directory"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create commands directory
        commands_dir = framework_dir / "commands"
        commands_dir.mkdir()
        
        # Create sample command files
        (commands_dir / "task.md").write_text("# Task Command")
        (commands_dir / "auto.md").write_text("# Auto Command")
        
        # Create modules directory
        modules_dir = framework_dir / "modules"
        modules_dir.mkdir()
        patterns_dir = modules_dir / "patterns"
        patterns_dir.mkdir()
        
        (patterns_dir / "tdd-cycle.md").write_text("# TDD Cycle Pattern")
        
        return framework_dir
    
    def test_visual_flow_builder_initialization(self, framework_path):
        """Test VisualFlowBuilder can be initialized"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        assert builder.framework_path == framework_path
        assert hasattr(builder, 'nodes')
        assert hasattr(builder, 'connections')
    
    def test_load_available_components(self, framework_path):
        """Test loading commands and modules as flow components"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        components = builder.load_available_components()
        
        assert 'commands' in components
        assert 'modules' in components
        assert len(components['commands']) == 2  # task.md, auto.md
        assert len(components['modules']) >= 1  # tdd-cycle.md
    
    def test_create_node_from_component(self, framework_path):
        """Test creating flow nodes from framework components"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        
        # Test creating command node
        node = builder.create_node_from_component(
            component_type='command',
            component_name='task',
            position={'x': 100, 'y': 200}
        )
        
        assert node.type == 'command'
        assert node.title == '/task'
        assert node.position == {'x': 100, 'y': 200}
    
    def test_add_node_to_flow(self, framework_path):
        """Test adding nodes to the flow"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        
        node = builder.create_node_from_component(
            component_type='command',
            component_name='task',
            position={'x': 100, 'y': 200}
        )
        
        builder.add_node(node)
        assert len(builder.nodes) == 1
        assert builder.nodes[0].id == node.id
    
    def test_create_connection(self, framework_path):
        """Test creating connections between nodes"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        
        # Create two nodes
        node1 = builder.create_node_from_component('command', 'auto', {'x': 0, 'y': 0})
        node2 = builder.create_node_from_component('command', 'task', {'x': 200, 'y': 0})
        
        builder.add_node(node1)
        builder.add_node(node2)
        
        # Create connection
        connection = builder.create_connection(
            source_node=node1.id,
            source_output='routing_decision',
            target_node=node2.id,
            target_input='request'
        )
        
        builder.add_connection(connection)
        assert len(builder.connections) == 1
    
    def test_validate_flow(self, framework_path):
        """Test flow validation (no cycles, valid connections)"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        
        # Create a valid flow
        node1 = builder.create_node_from_component('command', 'auto', {'x': 0, 'y': 0})
        node2 = builder.create_node_from_component('command', 'task', {'x': 200, 'y': 0})
        
        builder.add_node(node1)
        builder.add_node(node2)
        
        connection = builder.create_connection(
            source_node=node1.id,
            source_output='routing_decision',
            target_node=node2.id,
            target_input='request'
        )
        builder.add_connection(connection)
        
        # Should be valid
        is_valid, errors = builder.validate_flow()
        assert is_valid is True
        assert len(errors) == 0
    
    def test_generate_prompt_from_flow(self, framework_path):
        """Test generating executable prompt from flow"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        
        # Create a simple flow
        node1 = builder.create_node_from_component('command', 'auto', {'x': 0, 'y': 0})
        node2 = builder.create_node_from_component('command', 'task', {'x': 200, 'y': 0})
        
        builder.add_node(node1)
        builder.add_node(node2)
        
        connection = builder.create_connection(
            source_node=node1.id,
            source_output='routing_decision',
            target_node=node2.id,
            target_input='request'
        )
        builder.add_connection(connection)
        
        # Generate prompt
        prompt = builder.generate_prompt_from_flow()
        
        assert isinstance(prompt, str)
        assert len(prompt) > 0
        assert '/auto' in prompt or '/task' in prompt
    
    def test_save_and_load_flow(self, framework_path, tmp_path):
        """Test saving and loading flows"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        
        # Create a flow
        node = builder.create_node_from_component('command', 'task', {'x': 100, 'y': 200})
        builder.add_node(node)
        
        # Save flow
        flow_file = tmp_path / "test_flow.json"
        builder.save_flow(flow_file)
        
        assert flow_file.exists()
        
        # Load flow
        new_builder = VisualFlowBuilder(framework_path=framework_path)
        new_builder.load_flow(flow_file)
        
        assert len(new_builder.nodes) == 1
        assert new_builder.nodes[0].id == node.id
    
    def test_render_flow_builder_ui(self, framework_path):
        """Test rendering the flow builder UI"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        
        # Test that the method exists and can be called
        # We don't test Streamlit rendering in unit tests
        assert hasattr(builder, 'render_flow_builder_ui')
        assert callable(builder.render_flow_builder_ui)
    
    def test_drag_drop_interface(self, framework_path):
        """Test drag and drop interface functionality"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        
        # Test dropping a component onto the canvas
        drop_event = {
            'component_type': 'command',
            'component_name': 'task',
            'position': {'x': 150, 'y': 250}
        }
        
        node = builder.handle_component_drop(drop_event)
        
        assert node is not None
        assert node.type == 'command'
        assert node.position == {'x': 150, 'y': 250}
    
    def test_node_connection_interface(self, framework_path):
        """Test connecting nodes through UI interactions"""
        if VisualFlowBuilder is None:
            pytest.skip("VisualFlowBuilder not implemented yet")
        
        builder = VisualFlowBuilder(framework_path=framework_path)
        
        # Create two nodes
        node1 = builder.create_node_from_component('command', 'auto', {'x': 0, 'y': 0})
        node2 = builder.create_node_from_component('command', 'task', {'x': 200, 'y': 0})
        
        builder.add_node(node1)
        builder.add_node(node2)
        
        # Test connection creation through UI
        connection_event = {
            'source_node': node1.id,
            'source_output': 'routing_decision',
            'target_node': node2.id,
            'target_input': 'request'
        }
        
        connection = builder.handle_connection_create(connection_event)
        
        assert connection is not None
        assert connection.source_node == node1.id
        assert connection.target_node == node2.id