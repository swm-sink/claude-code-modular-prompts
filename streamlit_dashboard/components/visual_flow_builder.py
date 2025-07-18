"""
Visual Flow Builder Component for Claude Code Modular Prompts Framework
Provides drag-and-drop interface for building prompt workflows
"""

import streamlit as st
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from uuid import uuid4
import plotly.graph_objects as go
import plotly.express as px
from collections import defaultdict


@dataclass
class FlowNode:
    """Represents a node in the visual flow"""
    
    id: str
    type: str  # 'command', 'module', 'pattern'
    title: str
    content: str = ""
    position: Dict[str, int] = None
    inputs: List[Dict[str, str]] = None
    outputs: List[Dict[str, str]] = None
    
    def __post_init__(self):
        """Validate node data after initialization"""
        if not self.id or self.id.strip() == "":
            raise ValueError("Node ID cannot be empty")
        
        if self.type not in ['command', 'module', 'pattern']:
            raise ValueError(f"Invalid node type: {self.type}")
        
        if self.position is None:
            self.position = {'x': 0, 'y': 0}
        
        if self.inputs is None:
            self.inputs = []
        
        if self.outputs is None:
            self.outputs = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FlowNode':
        """Create node from dictionary"""
        return cls(**data)


@dataclass
class FlowConnection:
    """Represents a connection between nodes"""
    
    id: str
    source_node: str
    source_output: str
    target_node: str
    target_input: str
    
    def __post_init__(self):
        """Validate connection data"""
        if not self.source_node or self.source_node.strip() == "":
            raise ValueError("Source node cannot be empty")
        
        if not self.target_node or self.target_node.strip() == "":
            raise ValueError("Target node cannot be empty")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert connection to dictionary"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FlowConnection':
        """Create connection from dictionary"""
        return cls(**data)


class VisualFlowBuilder:
    """Visual Flow Builder component for creating prompt workflows"""
    
    def __init__(self, framework_path: Path):
        """Initialize Visual Flow Builder"""
        self.framework_path = framework_path
        self.nodes: List[FlowNode] = []
        self.connections: List[FlowConnection] = []
        self._available_components = None
    
    def load_available_components(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load available commands and modules as flow components"""
        if self._available_components is not None:
            return self._available_components
        
        components = {
            'commands': [],
            'modules': []
        }
        
        # Load commands
        commands_dir = self.framework_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.glob("*.md"):
                components['commands'].append({
                    'name': cmd_file.stem,
                    'title': f"/{cmd_file.stem}",
                    'file_path': str(cmd_file),
                    'type': 'command'
                })
        
        # Load modules
        modules_dir = self.framework_path / "modules"
        if modules_dir.exists():
            for module_file in modules_dir.rglob("*.md"):
                # Get relative path for categorization
                relative_path = module_file.relative_to(modules_dir)
                category = relative_path.parts[0] if len(relative_path.parts) > 1 else 'misc'
                
                components['modules'].append({
                    'name': module_file.stem,
                    'title': module_file.stem.replace('-', ' ').title(),
                    'file_path': str(module_file),
                    'category': category,
                    'type': 'module'
                })
        
        self._available_components = components
        return components
    
    def create_node_from_component(self, component_type: str, component_name: str, position: Dict[str, int]) -> FlowNode:
        """Create a flow node from a framework component"""
        components = self.load_available_components()
        
        # Find the component
        component_list = components.get(f"{component_type}s", [])
        component = next((c for c in component_list if c['name'] == component_name), None)
        
        if not component:
            raise ValueError(f"Component {component_name} not found in {component_type}s")
        
        # Generate unique ID
        node_id = f"{component_type}_{component_name}_{uuid4().hex[:8]}"
        
        # Define inputs and outputs based on type
        inputs = []
        outputs = []
        
        if component_type == 'command':
            inputs = [{'name': 'request', 'type': 'string'}]
            outputs = [{'name': 'result', 'type': 'object'}]
            if component_name == 'auto':
                outputs.append({'name': 'routing_decision', 'type': 'string'})
        elif component_type == 'module':
            inputs = [{'name': 'context', 'type': 'object'}]
            outputs = [{'name': 'output', 'type': 'object'}]
        
        return FlowNode(
            id=node_id,
            type=component_type,
            title=component['title'],
            content=f"{component_type.title()}: {component['title']}",
            position=position,
            inputs=inputs,
            outputs=outputs
        )
    
    def add_node(self, node: FlowNode) -> None:
        """Add a node to the flow"""
        self.nodes.append(node)
    
    def create_connection(self, source_node: str, source_output: str, target_node: str, target_input: str) -> FlowConnection:
        """Create a connection between nodes"""
        connection_id = f"conn_{uuid4().hex[:8]}"
        
        return FlowConnection(
            id=connection_id,
            source_node=source_node,
            source_output=source_output,
            target_node=target_node,
            target_input=target_input
        )
    
    def add_connection(self, connection: FlowConnection) -> None:
        """Add a connection to the flow"""
        self.connections.append(connection)
    
    def validate_flow(self) -> Tuple[bool, List[str]]:
        """Validate the flow for cycles and invalid connections"""
        errors = []
        
        # Check for valid node references in connections
        node_ids = {node.id for node in self.nodes}
        
        for conn in self.connections:
            if conn.source_node not in node_ids:
                errors.append(f"Connection references non-existent source node: {conn.source_node}")
            
            if conn.target_node not in node_ids:
                errors.append(f"Connection references non-existent target node: {conn.target_node}")
        
        # Basic cycle detection using DFS
        if len(errors) == 0:
            graph = defaultdict(list)
            for conn in self.connections:
                graph[conn.source_node].append(conn.target_node)
            
            visited = set()
            rec_stack = set()
            
            def has_cycle(node):
                if node in rec_stack:
                    return True
                if node in visited:
                    return False
                
                visited.add(node)
                rec_stack.add(node)
                
                for neighbor in graph[node]:
                    if has_cycle(neighbor):
                        return True
                
                rec_stack.remove(node)
                return False
            
            for node_id in node_ids:
                if node_id not in visited:
                    if has_cycle(node_id):
                        errors.append("Flow contains cycles")
                        break
        
        return len(errors) == 0, errors
    
    def generate_prompt_from_flow(self) -> str:
        """Generate executable prompt from the flow"""
        if not self.nodes:
            return ""
        
        # Sort nodes by position (simple left-to-right ordering)
        sorted_nodes = sorted(self.nodes, key=lambda n: n.position['x'])
        
        prompt_parts = []
        
        for node in sorted_nodes:
            if node.type == 'command':
                prompt_parts.append(f"{node.title}")
            elif node.type == 'module':
                prompt_parts.append(f"Module: {node.title}")
        
        return " → ".join(prompt_parts)
    
    def save_flow(self, file_path: Path) -> None:
        """Save flow to JSON file"""
        flow_data = {
            'nodes': [node.to_dict() for node in self.nodes],
            'connections': [conn.to_dict() for conn in self.connections],
            'metadata': {
                'version': '1.0',
                'framework_path': str(self.framework_path)
            }
        }
        
        with open(file_path, 'w') as f:
            json.dump(flow_data, f, indent=2)
    
    def load_flow(self, file_path: Path) -> None:
        """Load flow from JSON file"""
        with open(file_path, 'r') as f:
            flow_data = json.load(f)
        
        self.nodes = [FlowNode.from_dict(node_data) for node_data in flow_data['nodes']]
        self.connections = [FlowConnection.from_dict(conn_data) for conn_data in flow_data['connections']]
    
    def handle_component_drop(self, drop_event: Dict[str, Any]) -> FlowNode:
        """Handle dropping a component onto the canvas"""
        return self.create_node_from_component(
            component_type=drop_event['component_type'],
            component_name=drop_event['component_name'],
            position=drop_event['position']
        )
    
    def handle_connection_create(self, connection_event: Dict[str, Any]) -> FlowConnection:
        """Handle creating a connection through UI"""
        connection = self.create_connection(
            source_node=connection_event['source_node'],
            source_output=connection_event['source_output'],
            target_node=connection_event['target_node'],
            target_input=connection_event['target_input']
        )
        
        self.add_connection(connection)
        return connection
    
    def create_flow_visualization(self) -> go.Figure:
        """Create interactive flow visualization using Plotly"""
        fig = go.Figure()
        
        if not self.nodes:
            # Empty state
            fig.add_annotation(
                text="Drop components here to build your flow",
                x=0.5, y=0.5,
                showarrow=False,
                font=dict(size=16, color="gray")
            )
        else:
            # Draw connections first (so they appear behind nodes)
            for conn in self.connections:
                source_node = next((n for n in self.nodes if n.id == conn.source_node), None)
                target_node = next((n for n in self.nodes if n.id == conn.target_node), None)
                
                if source_node and target_node:
                    fig.add_trace(go.Scatter(
                        x=[source_node.position['x'], target_node.position['x']],
                        y=[source_node.position['y'], target_node.position['y']],
                        mode='lines+markers',
                        line=dict(color='blue', width=2),
                        marker=dict(size=8, symbol='arrow-up'),
                        showlegend=False,
                        hovertemplate=f"{conn.source_output} → {conn.target_input}<extra></extra>"
                    ))
            
            # Draw nodes
            for node in self.nodes:
                color = 'lightblue' if node.type == 'command' else 'lightgreen'
                
                fig.add_trace(go.Scatter(
                    x=[node.position['x']],
                    y=[node.position['y']],
                    mode='markers+text',
                    marker=dict(size=30, color=color, line=dict(width=2, color='black')),
                    text=[node.title],
                    textposition='middle center',
                    name=node.title,
                    hovertemplate=f"<b>{node.title}</b><br>Type: {node.type}<br>ID: {node.id}<extra></extra>"
                ))
        
        fig.update_layout(
            title="Visual Flow Builder",
            showlegend=False,
            xaxis=dict(showgrid=True, zeroline=False, range=[-50, 500]),
            yaxis=dict(showgrid=True, zeroline=False, range=[-50, 300]),
            height=600,
            dragmode='select'
        )
        
        return fig
    
    def render_flow_builder_ui(self):
        """Render the flow builder user interface"""
        st.title("🎯 Visual Flow Builder")
        
        # Component palette
        st.sidebar.header("Component Palette")
        
        components = self.load_available_components()
        
        # Commands section
        st.sidebar.subheader("Commands")
        command_names = [cmd['name'] for cmd in components['commands']]
        if command_names:
            selected_command = st.sidebar.selectbox("Select Command", command_names)
            if st.sidebar.button("Add Command"):
                # In a real implementation, this would add to the flow
                st.sidebar.success(f"Added {selected_command}")
        
        # Modules section  
        st.sidebar.subheader("Modules")
        module_names = [mod['name'] for mod in components['modules']]
        if module_names:
            selected_module = st.sidebar.selectbox("Select Module", module_names)
            if st.sidebar.button("Add Module"):
                st.sidebar.success(f"Added {selected_module}")
        
        # Main canvas
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader("Flow Canvas")
            # Display flow visualization
            fig = self.create_flow_visualization()
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Flow Properties")
            
            # Display current flow info
            st.write(f"**Nodes:** {len(self.nodes)}")
            st.write(f"**Connections:** {len(self.connections)}")
            
            # Flow validation
            is_valid, errors = self.validate_flow()
            if is_valid:
                st.success("✅ Flow is valid")
            else:
                st.error("❌ Flow has errors:")
                for error in errors:
                    st.write(f"• {error}")
            
            # Generate prompt button
            if st.button("Generate Prompt"):
                prompt = self.generate_prompt_from_flow()
                if prompt:
                    st.code(prompt)
                else:
                    st.info("Add nodes to generate a prompt")
    
    def render(self):
        """Main render method for Visual Flow Builder"""
        self.render_flow_builder_ui()