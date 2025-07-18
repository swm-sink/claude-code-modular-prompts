"""
Interactive Dependency Graph Component for Claude Code Modular Prompts Framework
Provides visualization of dependencies between commands, modules, and patterns
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict, field
import json
import re
from collections import defaultdict, deque
import networkx as nx
import math


@dataclass
class DependencyNode:
    """Represents a node in the dependency graph"""
    
    id: str
    type: str  # 'command', 'module', 'pattern', 'system'
    name: str
    title: str = ""
    category: str = ""
    file_path: str = ""
    dependencies: List[str] = field(default_factory=list)
    dependents: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Validate node data after initialization"""
        if not self.id or self.id.strip() == "":
            raise ValueError("Node ID cannot be empty")
        
        valid_types = ['command', 'module', 'pattern', 'system']
        if self.type not in valid_types:
            raise ValueError(f"Invalid node type: {self.type}. Must be one of {valid_types}")
        
        if not self.title:
            self.title = self.name
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DependencyNode':
        """Create node from dictionary"""
        return cls(**data)


@dataclass 
class DependencyEdge:
    """Represents an edge (dependency relationship) in the graph"""
    
    id: str
    source: str
    target: str
    relationship_type: str = "uses"  # 'uses', 'imports', 'extends', 'implements'
    strength: float = 1.0
    description: str = ""
    
    def __post_init__(self):
        """Validate edge data"""
        if not self.source or self.source.strip() == "":
            raise ValueError("Source node cannot be empty")
        
        if not self.target or self.target.strip() == "":
            raise ValueError("Target node cannot be empty")
        
        if not 0.0 <= self.strength <= 1.0:
            raise ValueError("Strength must be between 0.0 and 1.0")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert edge to dictionary"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DependencyEdge':
        """Create edge from dictionary"""
        return cls(**data)


class DependencyGraph:
    """Interactive Dependency Graph component for visualizing framework dependencies"""
    
    def __init__(self, framework_path: Path):
        """Initialize Dependency Graph"""
        self.framework_path = framework_path
        self.nodes: List[DependencyNode] = []
        self.edges: List[DependencyEdge] = []
        self._dependency_patterns = [
            r'modules/[^)\s]+\.md',
            r'system/[^)\s]+\.md', 
            r'commands/[^)\s]+\.md',
            r'\.claude/[^)\s]+\.md'
        ]
    
    def parse_framework_structure(self) -> List[DependencyNode]:
        """Parse framework structure into dependency nodes"""
        nodes = []
        
        # Parse commands
        commands_dir = self.framework_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.glob("*.md"):
                node = DependencyNode(
                    id=f"command_{cmd_file.stem}",
                    type="command",
                    name=cmd_file.stem,
                    title=f"/{cmd_file.stem}",
                    category="commands",
                    file_path=str(cmd_file.relative_to(self.framework_path))
                )
                nodes.append(node)
        
        # Parse modules
        modules_dir = self.framework_path / "modules"
        if modules_dir.exists():
            for module_file in modules_dir.rglob("*.md"):
                relative_path = module_file.relative_to(modules_dir)
                category = relative_path.parts[0] if len(relative_path.parts) > 1 else 'misc'
                
                node = DependencyNode(
                    id=f"module_{category}_{module_file.stem}",
                    type="module",
                    name=module_file.stem,
                    title=module_file.stem.replace('-', ' ').title(),
                    category=category,
                    file_path=str(module_file.relative_to(self.framework_path))
                )
                nodes.append(node)
        
        # Parse system components
        system_dir = self.framework_path / "system"
        if system_dir.exists():
            for system_file in system_dir.rglob("*.md"):
                relative_path = system_file.relative_to(system_dir)
                category = relative_path.parts[0] if len(relative_path.parts) > 1 else 'misc'
                
                node = DependencyNode(
                    id=f"system_{category}_{system_file.stem}",
                    type="system",
                    name=system_file.stem,
                    title=system_file.stem.replace('-', ' ').title(),
                    category=category,
                    file_path=str(system_file.relative_to(self.framework_path))
                )
                nodes.append(node)
        
        self.nodes = nodes
        return nodes
    
    def extract_dependencies_from_content(self, content: str) -> List[str]:
        """Extract dependency references from file content"""
        dependencies = []
        
        for pattern in self._dependency_patterns:
            matches = re.findall(pattern, content)
            dependencies.extend(matches)
        
        return list(set(dependencies))  # Remove duplicates
    
    def build_dependency_edges(self, nodes: List[DependencyNode]) -> List[DependencyEdge]:
        """Build edges between dependency nodes"""
        edges = []
        
        # Create path to node mapping
        path_to_node = {node.file_path: node for node in nodes}
        
        for node in nodes:
            # Read file content to find dependencies
            file_path = self.framework_path / node.file_path
            if file_path.exists():
                try:
                    content = file_path.read_text()
                    dependencies = self.extract_dependencies_from_content(content)
                    
                    for dep_path in dependencies:
                        target_node = path_to_node.get(dep_path)
                        if target_node:
                            edge = DependencyEdge(
                                id=f"edge_{node.id}_to_{target_node.id}",
                                source=node.id,
                                target=target_node.id,
                                relationship_type="uses",
                                strength=self.calculate_dependency_strength(node.file_path, dep_path)
                            )
                            edges.append(edge)
                            
                            # Update node dependencies
                            if target_node.id not in node.dependencies:
                                node.dependencies.append(target_node.id)
                            if node.id not in target_node.dependents:
                                target_node.dependents.append(node.id)
                                
                except Exception as e:
                    # Skip files that can't be read
                    continue
        
        self.edges = edges
        return edges
    
    def calculate_dependency_strength(self, source_path: str, target_path: str) -> float:
        """Calculate dependency strength between two nodes"""
        # Simple heuristic: direct references are stronger
        try:
            source_file = self.framework_path / source_path
            if source_file.exists():
                content = source_file.read_text()
                count = content.count(target_path)
                # Normalize count to 0-1 range
                return min(count * 0.2, 1.0)
        except:
            pass
        
        return 0.5  # Default medium strength
    
    def detect_circular_dependencies(self, nodes: List[DependencyNode], edges: List[DependencyEdge]) -> List[List[str]]:
        """Detect circular dependencies in the graph"""
        # Build adjacency list
        graph = defaultdict(list)
        for edge in edges:
            graph[edge.source].append(edge.target)
        
        cycles = []
        visited = set()
        rec_stack = set()
        
        def dfs(node, path):
            if node in rec_stack:
                # Found a cycle
                cycle_start = path.index(node)
                cycles.append(path[cycle_start:] + [node])
                return
            
            if node in visited:
                return
            
            visited.add(node)
            rec_stack.add(node)
            
            for neighbor in graph[node]:
                dfs(neighbor, path + [node])
            
            rec_stack.remove(node)
        
        for node in [n.id for n in nodes]:
            if node not in visited:
                dfs(node, [])
        
        return cycles
    
    def get_dependency_metrics(self) -> Dict[str, Any]:
        """Calculate dependency metrics for the graph"""
        if not self.nodes:
            self.parse_framework_structure()
        if not self.edges:
            self.build_dependency_edges(self.nodes)
        
        # Calculate metrics
        node_dependencies = defaultdict(int)
        node_dependents = defaultdict(int)
        
        for edge in self.edges:
            node_dependencies[edge.source] += 1
            node_dependents[edge.target] += 1
        
        # Find most dependent nodes
        most_dependent = sorted(node_dependencies.items(), key=lambda x: x[1], reverse=True)[:5]
        most_depended_upon = sorted(node_dependents.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # Calculate max depth
        max_depth = self._calculate_max_depth()
        
        # Detect cycles
        cycles = self.detect_circular_dependencies(self.nodes, self.edges)
        
        return {
            'total_nodes': len(self.nodes),
            'total_edges': len(self.edges),
            'max_depth': max_depth,
            'circular_dependencies': len(cycles),
            'most_dependent_nodes': most_dependent,
            'most_depended_upon_nodes': most_depended_upon,
            'cycles': cycles
        }
    
    def _calculate_max_depth(self) -> int:
        """Calculate maximum dependency depth"""
        if not self.edges:
            return 0
        
        # Build graph
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for edge in self.edges:
            graph[edge.source].append(edge.target)
            in_degree[edge.target] += 1
        
        # Topological sort to find max depth
        queue = deque()
        depths = {}
        
        # Start with nodes that have no dependencies
        for node in self.nodes:
            if in_degree[node.id] == 0:
                queue.append(node.id)
                depths[node.id] = 0
        
        max_depth = 0
        
        while queue:
            current = queue.popleft()
            current_depth = depths[current]
            max_depth = max(max_depth, current_depth)
            
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                depths[neighbor] = max(depths.get(neighbor, 0), current_depth + 1)
                
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return max_depth
    
    def get_node_by_id(self, node_id: str) -> Optional[DependencyNode]:
        """Find node by ID"""
        return next((node for node in self.nodes if node.id == node_id), None)
    
    def get_dependencies_for_node(self, node_id: str) -> List[DependencyNode]:
        """Get all dependencies for a specific node (direct and transitive)"""
        node = self.get_node_by_id(node_id)
        if not node:
            return []
        
        dependencies = []
        visited = set()
        
        def collect_dependencies(current_id):
            if current_id in visited:
                return
            visited.add(current_id)
            
            current_node = self.get_node_by_id(current_id)
            if current_node:
                for dep_id in current_node.dependencies:
                    dep_node = self.get_node_by_id(dep_id)
                    if dep_node and dep_node not in dependencies:
                        dependencies.append(dep_node)
                        collect_dependencies(dep_id)
        
        collect_dependencies(node_id)
        return dependencies
    
    def get_dependents_for_node(self, node_id: str) -> List[DependencyNode]:
        """Get all nodes that depend on a specific node"""
        node = self.get_node_by_id(node_id)
        if not node:
            return []
        
        dependents = []
        for dependent_id in node.dependents:
            dependent_node = self.get_node_by_id(dependent_id)
            if dependent_node:
                dependents.append(dependent_node)
        
        return dependents
    
    def filter_nodes_by_type(self, node_type: str) -> List[DependencyNode]:
        """Filter nodes by type"""
        return [node for node in self.nodes if node.type == node_type]
    
    def calculate_graph_layout(self, algorithm: str = 'force-directed') -> Dict[str, Dict[str, float]]:
        """Calculate optimal graph layout positions"""
        if not self.nodes:
            return {}
        
        positions = {}
        
        if algorithm == 'force-directed':
            # Simple force-directed layout
            for i, node in enumerate(self.nodes):
                angle = 2 * math.pi * i / len(self.nodes)
                radius = 200
                positions[node.id] = {
                    'x': radius * math.cos(angle),
                    'y': radius * math.sin(angle)
                }
        elif algorithm == 'hierarchical':
            # Layer nodes by type
            command_nodes = self.filter_nodes_by_type('command')
            module_nodes = self.filter_nodes_by_type('module')
            system_nodes = self.filter_nodes_by_type('system')
            
            y_positions = {'command': 0, 'module': -100, 'system': -200}
            
            for node_type, nodes in [('command', command_nodes), ('module', module_nodes), ('system', system_nodes)]:
                for i, node in enumerate(nodes):
                    positions[node.id] = {
                        'x': i * 150 - (len(nodes) * 75),
                        'y': y_positions[node_type]
                    }
        
        return positions
    
    def create_plotly_graph(self) -> go.Figure:
        """Create interactive Plotly graph visualization"""
        if not self.nodes:
            self.parse_framework_structure()
        if not self.edges:
            self.build_dependency_edges(self.nodes)
        
        fig = go.Figure()
        
        if not self.nodes:
            fig.add_annotation(
                text="No framework components found",
                x=0.5, y=0.5,
                showarrow=False,
                font=dict(size=16, color="gray")
            )
            return fig
        
        # Calculate layout
        positions = self.calculate_graph_layout('force-directed')
        
        # Draw edges first
        for edge in self.edges:
            source_node = self.get_node_by_id(edge.source)
            target_node = self.get_node_by_id(edge.target)
            
            if source_node and target_node:
                source_pos = positions.get(edge.source, {'x': 0, 'y': 0})
                target_pos = positions.get(edge.target, {'x': 0, 'y': 0})
                
                fig.add_trace(go.Scatter(
                    x=[source_pos['x'], target_pos['x']],
                    y=[source_pos['y'], target_pos['y']],
                    mode='lines',
                    line=dict(color='lightgray', width=1 + edge.strength),
                    showlegend=False,
                    hovertemplate=f"{edge.relationship_type}: {source_node.name} → {target_node.name}<extra></extra>"
                ))
        
        # Draw nodes by type
        type_colors = {
            'command': 'lightblue',
            'module': 'lightgreen', 
            'system': 'lightcoral',
            'pattern': 'lightyellow'
        }
        
        for node_type, color in type_colors.items():
            type_nodes = self.filter_nodes_by_type(node_type)
            if type_nodes:
                x_coords = [positions.get(node.id, {'x': 0})['x'] for node in type_nodes]
                y_coords = [positions.get(node.id, {'y': 0})['y'] for node in type_nodes]
                names = [node.name for node in type_nodes]
                
                fig.add_trace(go.Scatter(
                    x=x_coords,
                    y=y_coords,
                    mode='markers+text',
                    marker=dict(size=20, color=color, line=dict(width=2, color='black')),
                    text=names,
                    textposition='middle center',
                    name=node_type.title(),
                    hovertemplate='<b>%{text}</b><br>Type: ' + node_type + '<extra></extra>'
                ))
        
        fig.update_layout(
            title="Framework Dependency Graph",
            showlegend=True,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=700,
            dragmode='pan'
        )
        
        return fig
    
    def export_dependency_data(self, output_path: Path, format: str = 'json') -> None:
        """Export dependency data to various formats"""
        if not self.nodes:
            self.parse_framework_structure()
        if not self.edges:
            self.build_dependency_edges(self.nodes)
        
        data = {
            'nodes': [node.to_dict() for node in self.nodes],
            'edges': [edge.to_dict() for edge in self.edges],
            'metadata': {
                'version': '1.0',
                'framework_path': str(self.framework_path),
                'total_nodes': len(self.nodes),
                'total_edges': len(self.edges)
            }
        }
        
        if format == 'json':
            with open(output_path, 'w') as f:
                json.dump(data, f, indent=2)
    
    def render_dependency_graph_ui(self):
        """Render the dependency graph user interface"""
        st.title("🔗 Framework Dependency Graph")
        
        # Initialize data if needed
        if not self.nodes:
            with st.spinner("Analyzing framework structure..."):
                self.parse_framework_structure()
                self.build_dependency_edges(self.nodes)
        
        # Metrics overview
        st.subheader("📊 Dependency Metrics")
        metrics = self.get_dependency_metrics()
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Nodes", metrics['total_nodes'])
        with col2:
            st.metric("Total Dependencies", metrics['total_edges'])
        with col3:
            st.metric("Max Depth", metrics['max_depth'])
        with col4:
            st.metric("Circular Dependencies", metrics['circular_dependencies'])
        
        # Main graph visualization
        st.subheader("🌐 Interactive Dependency Graph")
        
        # Layout controls
        col1, col2 = st.columns([3, 1])
        
        with col2:
            layout_algorithm = st.selectbox(
                "Layout Algorithm",
                ["force-directed", "hierarchical"]
            )
            
            show_node_types = st.multiselect(
                "Show Node Types",
                ["command", "module", "system", "pattern"],
                default=["command", "module"]
            )
        
        with col1:
            # Filter nodes if needed
            if show_node_types:
                filtered_nodes = []
                for node_type in show_node_types:
                    filtered_nodes.extend(self.filter_nodes_by_type(node_type))
                
                # Update positions for filtered view
                positions = self.calculate_graph_layout(layout_algorithm)
                
            # Create and display graph
            fig = self.create_plotly_graph()
            st.plotly_chart(fig, use_container_width=True)
        
        # Detailed analysis
        st.subheader("🔍 Detailed Analysis")
        
        tabs = st.tabs(["Most Dependent", "Most Depended Upon", "Circular Dependencies"])
        
        with tabs[0]:
            st.write("**Components with the most dependencies:**")
            for node_id, count in metrics['most_dependent_nodes']:
                node = self.get_node_by_id(node_id)
                if node:
                    st.write(f"• **{node.name}** ({node.type}): {count} dependencies")
        
        with tabs[1]:
            st.write("**Components that are most depended upon:**")
            for node_id, count in metrics['most_depended_upon_nodes']:
                node = self.get_node_by_id(node_id)
                if node:
                    st.write(f"• **{node.name}** ({node.type}): {count} dependents")
        
        with tabs[2]:
            if metrics['cycles']:
                st.warning(f"Found {len(metrics['cycles'])} circular dependencies:")
                for i, cycle in enumerate(metrics['cycles'], 1):
                    st.write(f"**Cycle {i}:** {' → '.join(cycle)}")
            else:
                st.success("✅ No circular dependencies detected")
        
        # Export functionality
        st.divider()
        if st.button("📥 Export Dependency Data"):
            export_path = Path("dependency_graph.json")
            self.export_dependency_data(export_path)
            st.success(f"Dependency data exported to {export_path}")
    
    def render(self):
        """Main render method for Dependency Graph"""
        self.render_dependency_graph_ui()