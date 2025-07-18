"""
Interactive Decision Tree Visualizer for /auto Routing Logic
Provides visual representation of AI routing decision processes and command recommendations
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from pathlib import Path
import json
import re
from datetime import datetime
from collections import defaultdict, Counter


@dataclass
class DecisionNode:
    """Represents a decision node in the routing tree"""
    
    node_id: str
    name: str
    description: str
    node_type: str  # 'condition', 'command', 'analysis', 'recommendation'
    criteria: Dict[str, Any] = field(default_factory=dict)
    conditions: List[str] = field(default_factory=list)
    outcomes: List[str] = field(default_factory=list)
    confidence: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary for serialization"""
        return {
            'node_id': self.node_id,
            'name': self.name,
            'description': self.description,
            'node_type': self.node_type,
            'criteria': self.criteria,
            'conditions': self.conditions,
            'outcomes': self.outcomes,
            'confidence': self.confidence,
            'metadata': self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DecisionNode':
        """Create node from dictionary"""
        return cls(**data)


@dataclass
class DecisionPath:
    """Represents a complete decision path through the tree"""
    
    path_id: str
    nodes: List[DecisionNode]
    input_context: Dict[str, Any]
    final_recommendation: str
    confidence_score: float
    reasoning: List[str]
    alternatives: List[str] = field(default_factory=list)
    execution_time: float = 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert path to dictionary for serialization"""
        return {
            'path_id': self.path_id,
            'nodes': [node.to_dict() for node in self.nodes],
            'input_context': self.input_context,
            'final_recommendation': self.final_recommendation,
            'confidence_score': self.confidence_score,
            'reasoning': self.reasoning,
            'alternatives': self.alternatives,
            'execution_time': self.execution_time
        }


class DecisionTreeVisualizer:
    """Interactive decision tree visualizer for /auto routing logic"""
    
    def __init__(self, framework_path: Path):
        """Initialize the decision tree visualizer"""
        self.framework_path = framework_path
        self.decision_tree = self._build_decision_tree()
        self.sample_inputs = self._generate_sample_inputs()
        self.routing_history = []
        
        # Color scheme for different node types
        self.color_scheme = {
            'condition': '#3498db',    # Blue
            'command': '#2ecc71',      # Green
            'analysis': '#f39c12',     # Orange
            'recommendation': '#e74c3c',  # Red
            'default': '#95a5a6'       # Gray
        }
        
        # Initialize session state
        if 'decision_tree_state' not in st.session_state:
            st.session_state.decision_tree_state = {
                'current_path': None,
                'simulation_results': [],
                'selected_node': None,
                'tree_layout': 'hierarchical'
            }
    
    def _build_decision_tree(self) -> nx.DiGraph:
        """Build the decision tree structure for /auto routing"""
        tree = nx.DiGraph()
        
        # Root node - initial analysis
        tree.add_node('root', 
                      name='Input Analysis',
                      description='Analyze user request and context',
                      node_type='analysis',
                      criteria={'input_length': 'any', 'clarity': 'any'},
                      confidence=1.0)
        
        # First level - complexity analysis
        tree.add_node('complexity_check',
                      name='Complexity Assessment',
                      description='Determine request complexity and scope',
                      node_type='condition',
                      criteria={'lines_of_code': 'estimate', 'file_count': 'estimate'},
                      conditions=['simple', 'moderate', 'complex'],
                      confidence=0.9)
        
        tree.add_edge('root', 'complexity_check')
        
        # Simple path
        tree.add_node('simple_analysis',
                      name='Simple Request Analysis',
                      description='Handle straightforward, single-file requests',
                      node_type='analysis',
                      criteria={'file_scope': 'single', 'changes': 'minimal'},
                      confidence=0.85)
        
        tree.add_node('task_recommendation',
                      name='/task Command',
                      description='Recommend /task for focused, single-component work',
                      node_type='recommendation',
                      criteria={'scope': 'single_file', 'complexity': 'low'},
                      confidence=0.9)
        
        tree.add_edge('complexity_check', 'simple_analysis', condition='simple')
        tree.add_edge('simple_analysis', 'task_recommendation')
        
        # Moderate complexity path
        tree.add_node('scope_analysis',
                      name='Scope Analysis',
                      description='Analyze request scope and requirements',
                      node_type='analysis',
                      criteria={'research_needed': 'bool', 'feature_scope': 'size'},
                      confidence=0.8)
        
        tree.add_edge('complexity_check', 'scope_analysis', condition='moderate')
        
        # Research path
        tree.add_node('research_check',
                      name='Research Required?',
                      description='Check if research or understanding is needed',
                      node_type='condition',
                      criteria={'unknown_codebase': 'bool', 'documentation_needed': 'bool'},
                      conditions=['yes', 'no'],
                      confidence=0.85)
        
        tree.add_node('query_recommendation',
                      name='/query Command',
                      description='Recommend /query for research and analysis',
                      node_type='recommendation',
                      criteria={'purpose': 'research', 'modifications': 'none'},
                      confidence=0.9)
        
        tree.add_edge('scope_analysis', 'research_check')
        tree.add_edge('research_check', 'query_recommendation', condition='yes')
        
        # Feature development path
        tree.add_node('feature_check',
                      name='Feature Development?',
                      description='Check if this is new feature development',
                      node_type='condition',
                      criteria={'new_functionality': 'bool', 'requirements': 'clear'},
                      conditions=['yes', 'no'],
                      confidence=0.8)
        
        tree.add_node('feature_recommendation',
                      name='/feature Command',
                      description='Recommend /feature for new functionality',
                      node_type='recommendation',
                      criteria={'scope': 'feature', 'requirements': 'defined'},
                      confidence=0.85)
        
        tree.add_edge('research_check', 'feature_check', condition='no')
        tree.add_edge('feature_check', 'feature_recommendation', condition='yes')
        
        # Multi-component path
        tree.add_node('multi_component_check',
                      name='Multi-Component Work?',
                      description='Check if work spans multiple components',
                      node_type='condition',
                      criteria={'components': 'multiple', 'coordination': 'required'},
                      conditions=['yes', 'no'],
                      confidence=0.8)
        
        tree.add_node('swarm_recommendation',
                      name='/swarm Command',
                      description='Recommend /swarm for coordinated multi-component work',
                      node_type='recommendation',
                      criteria={'coordination': 'required', 'parallel_work': 'beneficial'},
                      confidence=0.8)
        
        tree.add_edge('feature_check', 'multi_component_check', condition='no')
        tree.add_edge('multi_component_check', 'swarm_recommendation', condition='yes')
        
        # Complex path
        tree.add_node('complexity_analysis',
                      name='Complex Request Analysis',
                      description='Handle complex, multi-faceted requests',
                      node_type='analysis',
                      criteria={'uncertainty': 'high', 'coordination': 'complex'},
                      confidence=0.7)
        
        tree.add_node('session_check',
                      name='Long-Running Work?',
                      description='Check if work requires session management',
                      node_type='condition',
                      criteria={'duration': 'long', 'context_preservation': 'important'},
                      conditions=['yes', 'no'],
                      confidence=0.75)
        
        tree.add_node('session_recommendation',
                      name='/session Command',
                      description='Recommend /session for long-running work',
                      node_type='recommendation',
                      criteria={'duration': 'extended', 'context': 'critical'},
                      confidence=0.8)
        
        tree.add_edge('complexity_check', 'complexity_analysis', condition='complex')
        tree.add_edge('complexity_analysis', 'session_check')
        tree.add_edge('session_check', 'session_recommendation', condition='yes')
        
        # Protocol path for production work
        tree.add_node('production_check',
                      name='Production Work?',
                      description='Check if work involves production systems',
                      node_type='condition',
                      criteria={'production_impact': 'bool', 'safety_critical': 'bool'},
                      conditions=['yes', 'no'],
                      confidence=0.9)
        
        tree.add_node('protocol_recommendation',
                      name='/protocol Command',
                      description='Recommend /protocol for production-critical work',
                      node_type='recommendation',
                      criteria={'safety': 'critical', 'validation': 'required'},
                      confidence=0.95)
        
        tree.add_edge('session_check', 'production_check', condition='no')
        tree.add_edge('multi_component_check', 'production_check', condition='no')
        tree.add_edge('production_check', 'protocol_recommendation', condition='yes')
        
        # Default fallback
        tree.add_node('auto_fallback',
                      name='Default Routing',
                      description='Fallback to intelligent routing analysis',
                      node_type='recommendation',
                      criteria={'fallback': 'true'},
                      confidence=0.6)
        
        tree.add_edge('production_check', 'auto_fallback', condition='no')
        
        return tree
    
    def _generate_sample_inputs(self) -> List[Dict[str, Any]]:
        """Generate sample inputs for testing the decision tree"""
        return [
            {
                'name': 'Simple Bug Fix',
                'description': 'Fix a small bug in user authentication',
                'context': {
                    'request': 'Fix the login validation issue',
                    'file_count': 1,
                    'lines_estimate': 10,
                    'complexity': 'simple',
                    'research_needed': False,
                    'production_impact': False
                },
                'expected_command': '/task'
            },
            {
                'name': 'New Feature Development',
                'description': 'Add user profile management feature',
                'context': {
                    'request': 'Implement user profile management with avatar upload',
                    'file_count': 5,
                    'lines_estimate': 200,
                    'complexity': 'moderate',
                    'research_needed': False,
                    'production_impact': True,
                    'new_functionality': True
                },
                'expected_command': '/feature'
            },
            {
                'name': 'Codebase Research',
                'description': 'Understand existing authentication system',
                'context': {
                    'request': 'Help me understand how the current auth system works',
                    'file_count': 0,
                    'lines_estimate': 0,
                    'complexity': 'moderate',
                    'research_needed': True,
                    'production_impact': False
                },
                'expected_command': '/query'
            },
            {
                'name': 'Multi-Component Refactor',
                'description': 'Refactor authentication across multiple services',
                'context': {
                    'request': 'Refactor authentication to use JWT across all services',
                    'file_count': 15,
                    'lines_estimate': 500,
                    'complexity': 'complex',
                    'research_needed': True,
                    'production_impact': True,
                    'coordination_required': True
                },
                'expected_command': '/swarm'
            },
            {
                'name': 'Production Deployment',
                'description': 'Deploy security updates to production',
                'context': {
                    'request': 'Deploy the security patches to production safely',
                    'file_count': 3,
                    'lines_estimate': 50,
                    'complexity': 'moderate',
                    'research_needed': False,
                    'production_impact': True,
                    'safety_critical': True
                },
                'expected_command': '/protocol'
            },
            {
                'name': 'Long-Running Project',
                'description': 'Migrate database schema with extensive testing',
                'context': {
                    'request': 'Migrate to new database schema with comprehensive testing',
                    'file_count': 20,
                    'lines_estimate': 800,
                    'complexity': 'complex',
                    'research_needed': True,
                    'production_impact': True,
                    'duration': 'extended'
                },
                'expected_command': '/session'
            }
        ]
    
    def simulate_routing_decision(self, input_context: Dict[str, Any]) -> DecisionPath:
        """Simulate routing decision through the decision tree"""
        path_nodes = []
        current_node = 'root'
        reasoning = []
        
        # Start traversal
        while current_node:
            node_data = self.decision_tree.nodes[current_node]
            node = DecisionNode(
                node_id=current_node,
                name=node_data['name'],
                description=node_data['description'],
                node_type=node_data['node_type'],
                criteria=node_data.get('criteria', {}),
                conditions=node_data.get('conditions', []),
                confidence=node_data.get('confidence', 0.0)
            )
            path_nodes.append(node)
            
            # Add reasoning
            reasoning.append(f"{node.name}: {node.description}")
            
            # Find next node based on conditions
            next_node = None
            successors = list(self.decision_tree.successors(current_node))
            
            if not successors:
                # Terminal node
                break
            elif len(successors) == 1:
                # Single path
                next_node = successors[0]
            else:
                # Multiple paths - choose based on conditions
                next_node = self._evaluate_conditions(current_node, input_context, successors)
            
            current_node = next_node
        
        # Determine final recommendation
        final_node = path_nodes[-1]
        if final_node.node_type == 'recommendation':
            recommendation = final_node.name
            confidence = final_node.confidence
        else:
            recommendation = '/auto'  # Fallback
            confidence = 0.5
        
        # Generate alternatives
        alternatives = self._generate_alternatives(input_context, recommendation)
        
        return DecisionPath(
            path_id=f"path_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            nodes=path_nodes,
            input_context=input_context,
            final_recommendation=recommendation,
            confidence_score=confidence,
            reasoning=reasoning,
            alternatives=alternatives,
            execution_time=0.1  # Simulated
        )
    
    def _evaluate_conditions(self, current_node: str, context: Dict[str, Any], successors: List[str]) -> str:
        """Evaluate conditions to choose next node"""
        node_data = self.decision_tree.nodes[current_node]
        
        # Simple rule-based evaluation
        if current_node == 'complexity_check':
            lines = context.get('lines_estimate', 0)
            files = context.get('file_count', 0)
            
            if lines <= 50 and files <= 1:
                return 'simple_analysis'
            elif lines <= 200 and files <= 5:
                return 'scope_analysis'
            else:
                return 'complexity_analysis'
        
        elif current_node == 'research_check':
            if context.get('research_needed', False):
                return 'query_recommendation'
            else:
                return 'feature_check'
        
        elif current_node == 'feature_check':
            if context.get('new_functionality', False):
                return 'feature_recommendation'
            else:
                return 'multi_component_check'
        
        elif current_node == 'multi_component_check':
            if context.get('coordination_required', False) or context.get('file_count', 0) > 10:
                return 'swarm_recommendation'
            else:
                return 'production_check'
        
        elif current_node == 'session_check':
            if context.get('duration') == 'extended':
                return 'session_recommendation'
            else:
                return 'production_check'
        
        elif current_node == 'production_check':
            if context.get('production_impact', False) or context.get('safety_critical', False):
                return 'protocol_recommendation'
            else:
                return 'auto_fallback'
        
        # Default to first successor
        return successors[0] if successors else None
    
    def _generate_alternatives(self, context: Dict[str, Any], primary: str) -> List[str]:
        """Generate alternative command recommendations"""
        alternatives = []
        
        # Basic alternatives based on context
        if context.get('research_needed', False) and primary != '/query':
            alternatives.append('/query')
        
        if context.get('new_functionality', False) and primary != '/feature':
            alternatives.append('/feature')
        
        if context.get('coordination_required', False) and primary != '/swarm':
            alternatives.append('/swarm')
        
        if context.get('production_impact', False) and primary != '/protocol':
            alternatives.append('/protocol')
        
        # Always include /auto as fallback
        if primary != '/auto':
            alternatives.append('/auto')
        
        return alternatives[:3]  # Limit to top 3
    
    def render_decision_tree_graph(self) -> go.Figure:
        """Render the decision tree as an interactive graph"""
        # Create positions for nodes
        pos = nx.spring_layout(self.decision_tree, k=2, iterations=50)
        
        # Extract node information
        node_trace = []
        edge_trace = []
        
        # Create edges
        for edge in self.decision_tree.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            
            edge_trace.append(
                go.Scatter(
                    x=[x0, x1, None],
                    y=[y0, y1, None],
                    mode='lines',
                    line=dict(width=2, color='#888'),
                    hoverinfo='none',
                    showlegend=False
                )
            )
        
        # Create nodes
        for node in self.decision_tree.nodes():
            x, y = pos[node]
            node_data = self.decision_tree.nodes[node]
            
            color = self.color_scheme.get(node_data['node_type'], self.color_scheme['default'])
            
            node_trace.append(
                go.Scatter(
                    x=[x],
                    y=[y],
                    mode='markers+text',
                    marker=dict(
                        size=20,
                        color=color,
                        line=dict(width=2, color='white')
                    ),
                    text=node_data['name'],
                    textposition="middle center",
                    textfont=dict(size=10, color='white'),
                    hovertemplate=(
                        f"<b>{node_data['name']}</b><br>"
                        f"{node_data['description']}<br>"
                        f"Type: {node_data['node_type']}<br>"
                        f"Confidence: {node_data.get('confidence', 0):.1%}"
                        "<extra></extra>"
                    ),
                    name=node_data['node_type'].title(),
                    showlegend=True
                )
            )
        
        # Create figure
        fig = go.Figure(data=edge_trace + node_trace)
        fig.update_layout(
            title="Decision Tree for /auto Routing Logic",
            showlegend=True,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40),
            annotations=[
                dict(
                    text="Interactive Decision Tree - Click nodes to explore",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002,
                    xanchor="left", yanchor="bottom",
                    font=dict(size=12, color="gray")
                )
            ],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=600
        )
        
        return fig
    
    def render_decision_path(self, path: DecisionPath) -> go.Figure:
        """Render a specific decision path"""
        # Create a simplified view showing just the path
        fig = go.Figure()
        
        # Add path nodes
        for i, node in enumerate(path.nodes):
            fig.add_trace(
                go.Scatter(
                    x=[i],
                    y=[0],
                    mode='markers+text',
                    marker=dict(
                        size=30,
                        color=self.color_scheme.get(node.node_type, self.color_scheme['default']),
                        line=dict(width=3, color='white')
                    ),
                    text=node.name,
                    textposition="bottom center",
                    textfont=dict(size=10),
                    hovertemplate=(
                        f"<b>{node.name}</b><br>"
                        f"{node.description}<br>"
                        f"Type: {node.node_type}<br>"
                        f"Confidence: {node.confidence:.1%}"
                        "<extra></extra>"
                    ),
                    showlegend=False
                )
            )
            
            # Add arrows between nodes
            if i < len(path.nodes) - 1:
                fig.add_annotation(
                    x=i + 0.5,
                    y=0,
                    ax=i,
                    ay=0,
                    xref='x',
                    yref='y',
                    axref='x',
                    ayref='y',
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=2,
                    arrowcolor='#666'
                )
        
        fig.update_layout(
            title=f"Decision Path: {path.final_recommendation} (Confidence: {path.confidence_score:.1%})",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=200,
            margin=dict(b=20, l=5, r=5, t=40)
        )
        
        return fig
    
    def render_confidence_analysis(self, paths: List[DecisionPath]) -> go.Figure:
        """Render confidence analysis for multiple paths"""
        if not paths:
            return go.Figure()
        
        commands = [path.final_recommendation for path in paths]
        confidences = [path.confidence_score for path in paths]
        
        fig = go.Figure(data=[
            go.Bar(
                x=commands,
                y=confidences,
                marker_color=[self.color_scheme.get('recommendation', self.color_scheme['default'])] * len(commands),
                text=[f"{conf:.1%}" for conf in confidences],
                textposition='auto'
            )
        ])
        
        fig.update_layout(
            title="Confidence Analysis for Command Recommendations",
            xaxis_title="Recommended Command",
            yaxis_title="Confidence Score",
            yaxis=dict(tickformat='.1%'),
            height=400
        )
        
        return fig
    
    def render(self):
        """Main render method for the decision tree visualizer"""
        st.title("🌳 Interactive Decision Tree Visualizer")
        st.subheader("Visualize /auto Routing Logic and Decision Processes")
        
        # Control panel
        st.sidebar.subheader("🎛️ Control Panel")
        
        # Visualization options
        visualization_mode = st.sidebar.selectbox(
            "Visualization Mode",
            ["Full Decision Tree", "Simulate Routing", "Path Analysis", "Confidence Analysis"]
        )
        
        if visualization_mode == "Full Decision Tree":
            self._render_full_tree()
        elif visualization_mode == "Simulate Routing":
            self._render_simulation()
        elif visualization_mode == "Path Analysis":
            self._render_path_analysis()
        elif visualization_mode == "Confidence Analysis":
            self._render_confidence_analysis()
    
    def _render_full_tree(self):
        """Render the full decision tree"""
        st.subheader("📊 Complete Decision Tree")
        
        # Tree statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Nodes", len(self.decision_tree.nodes))
        with col2:
            st.metric("Decision Points", len([n for n in self.decision_tree.nodes if self.decision_tree.nodes[n]['node_type'] == 'condition']))
        with col3:
            st.metric("Commands", len([n for n in self.decision_tree.nodes if self.decision_tree.nodes[n]['node_type'] == 'recommendation']))
        with col4:
            st.metric("Max Depth", len(nx.dag_longest_path(self.decision_tree)))
        
        # Render tree
        fig = self.render_decision_tree_graph()
        st.plotly_chart(fig, use_container_width=True)
        
        # Node details
        st.subheader("🔍 Node Details")
        
        selected_node = st.selectbox(
            "Select a node to explore:",
            list(self.decision_tree.nodes.keys()),
            format_func=lambda x: f"{self.decision_tree.nodes[x]['name']} ({x})"
        )
        
        if selected_node:
            node_data = self.decision_tree.nodes[selected_node]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Name:** {node_data['name']}")
                st.markdown(f"**Type:** {node_data['node_type']}")
                st.markdown(f"**Confidence:** {node_data.get('confidence', 0):.1%}")
                st.markdown(f"**Description:** {node_data['description']}")
            
            with col2:
                if node_data.get('criteria'):
                    st.markdown("**Criteria:**")
                    for key, value in node_data['criteria'].items():
                        st.markdown(f"- {key}: {value}")
                
                if node_data.get('conditions'):
                    st.markdown("**Conditions:**")
                    for condition in node_data['conditions']:
                        st.markdown(f"- {condition}")
            
            # Show connections
            predecessors = list(self.decision_tree.predecessors(selected_node))
            successors = list(self.decision_tree.successors(selected_node))
            
            if predecessors or successors:
                st.markdown("**Connections:**")
                if predecessors:
                    st.markdown(f"**From:** {', '.join(predecessors)}")
                if successors:
                    st.markdown(f"**To:** {', '.join(successors)}")
    
    def _render_simulation(self):
        """Render routing simulation interface"""
        st.subheader("🎮 Routing Simulation")
        
        # Input method selection
        input_method = st.radio(
            "Choose input method:",
            ["Sample Scenarios", "Custom Input", "Interactive Builder"]
        )
        
        if input_method == "Sample Scenarios":
            self._render_sample_scenarios()
        elif input_method == "Custom Input":
            self._render_custom_input()
        elif input_method == "Interactive Builder":
            self._render_interactive_builder()
    
    def _render_sample_scenarios(self):
        """Render sample scenario testing"""
        st.markdown("### 📝 Sample Scenarios")
        
        # Select scenario
        scenario_names = [sample['name'] for sample in self.sample_inputs]
        selected_scenario = st.selectbox("Select a scenario:", scenario_names)
        
        if selected_scenario:
            scenario = next(s for s in self.sample_inputs if s['name'] == selected_scenario)
            
            # Display scenario details
            st.markdown(f"**Description:** {scenario['description']}")
            st.markdown(f"**Expected Command:** {scenario['expected_command']}")
            
            # Show context
            with st.expander("Input Context"):
                st.json(scenario['context'])
            
            # Run simulation
            if st.button("🚀 Run Simulation"):
                path = self.simulate_routing_decision(scenario['context'])
                
                # Display results
                st.success(f"Recommended Command: **{path.final_recommendation}**")
                st.info(f"Confidence: {path.confidence_score:.1%}")
                
                # Show path visualization
                fig = self.render_decision_path(path)
                st.plotly_chart(fig, use_container_width=True)
                
                # Show reasoning
                st.markdown("### 💭 Decision Reasoning")
                for i, reason in enumerate(path.reasoning, 1):
                    st.markdown(f"{i}. {reason}")
                
                # Show alternatives
                if path.alternatives:
                    st.markdown("### 🔄 Alternative Commands")
                    for alt in path.alternatives:
                        st.markdown(f"- {alt}")
                
                # Compare with expected
                if path.final_recommendation == scenario['expected_command']:
                    st.success("✅ Matches expected recommendation!")
                else:
                    st.warning(f"⚠️ Expected {scenario['expected_command']}, got {path.final_recommendation}")
    
    def _render_custom_input(self):
        """Render custom input interface"""
        st.markdown("### ⚙️ Custom Input")
        
        # Custom input form
        with st.form("custom_input_form"):
            request_text = st.text_area("Request Description", height=100)
            
            col1, col2 = st.columns(2)
            
            with col1:
                file_count = st.number_input("Estimated File Count", min_value=0, value=1)
                lines_estimate = st.number_input("Estimated Lines of Code", min_value=0, value=50)
                complexity = st.selectbox("Complexity Level", ["simple", "moderate", "complex"])
            
            with col2:
                research_needed = st.checkbox("Research Required")
                new_functionality = st.checkbox("New Functionality")
                production_impact = st.checkbox("Production Impact")
                coordination_required = st.checkbox("Coordination Required")
                safety_critical = st.checkbox("Safety Critical")
            
            duration = st.selectbox("Expected Duration", ["short", "medium", "extended"])
            
            submitted = st.form_submit_button("🚀 Analyze Request")
            
            if submitted and request_text:
                # Build context
                context = {
                    'request': request_text,
                    'file_count': file_count,
                    'lines_estimate': lines_estimate,
                    'complexity': complexity,
                    'research_needed': research_needed,
                    'new_functionality': new_functionality,
                    'production_impact': production_impact,
                    'coordination_required': coordination_required,
                    'safety_critical': safety_critical,
                    'duration': duration
                }
                
                # Run simulation
                path = self.simulate_routing_decision(context)
                
                # Display results
                st.success(f"Recommended Command: **{path.final_recommendation}**")
                st.info(f"Confidence: {path.confidence_score:.1%}")
                
                # Show path visualization
                fig = self.render_decision_path(path)
                st.plotly_chart(fig, use_container_width=True)
                
                # Show reasoning
                st.markdown("### 💭 Decision Reasoning")
                for i, reason in enumerate(path.reasoning, 1):
                    st.markdown(f"{i}. {reason}")
                
                # Show alternatives
                if path.alternatives:
                    st.markdown("### 🔄 Alternative Commands")
                    for alt in path.alternatives:
                        st.markdown(f"- {alt}")
    
    def _render_interactive_builder(self):
        """Render interactive scenario builder"""
        st.markdown("### 🔧 Interactive Scenario Builder")
        
        # Guided questions
        st.markdown("Answer these questions to build your scenario:")
        
        # Question 1: What are you trying to do?
        purpose = st.radio(
            "What are you trying to do?",
            ["Fix a bug", "Add new feature", "Understand existing code", "Refactor code", "Deploy to production", "Other"]
        )
        
        # Question 2: How many files will be affected?
        file_scope = st.radio(
            "How many files will be affected?",
            ["1 file", "2-5 files", "6-10 files", "More than 10 files", "Not sure"]
        )
        
        # Question 3: Do you understand the existing code?
        understanding = st.radio(
            "Do you understand the existing code?",
            ["Yes, I know exactly what to do", "Mostly, but need some clarification", "No, I need to research first"]
        )
        
        # Question 4: Is this production-critical?
        criticality = st.radio(
            "Is this production-critical?",
            ["No, development only", "Yes, but low risk", "Yes, high risk", "Yes, safety critical"]
        )
        
        # Question 5: How long will this take?
        duration = st.radio(
            "How long will this take?",
            ["Quick (< 1 hour)", "Medium (1-4 hours)", "Long (> 4 hours)", "Multiple days"]
        )
        
        if st.button("🎯 Get Recommendation"):
            # Map answers to context
            context = self._map_answers_to_context(purpose, file_scope, understanding, criticality, duration)
            
            # Run simulation
            path = self.simulate_routing_decision(context)
            
            # Display results
            st.success(f"Recommended Command: **{path.final_recommendation}**")
            st.info(f"Confidence: {path.confidence_score:.1%}")
            
            # Show reasoning
            st.markdown("### 💭 Why this recommendation?")
            for i, reason in enumerate(path.reasoning, 1):
                st.markdown(f"{i}. {reason}")
            
            # Show alternatives
            if path.alternatives:
                st.markdown("### 🔄 You could also try:")
                for alt in path.alternatives:
                    st.markdown(f"- {alt}")
    
    def _map_answers_to_context(self, purpose: str, file_scope: str, understanding: str, criticality: str, duration: str) -> Dict[str, Any]:
        """Map interactive answers to context dictionary"""
        context = {}
        
        # Map purpose
        if purpose == "Fix a bug":
            context.update({'complexity': 'simple', 'new_functionality': False})
        elif purpose == "Add new feature":
            context.update({'complexity': 'moderate', 'new_functionality': True})
        elif purpose == "Understand existing code":
            context.update({'research_needed': True, 'complexity': 'simple'})
        elif purpose == "Refactor code":
            context.update({'complexity': 'moderate', 'coordination_required': True})
        elif purpose == "Deploy to production":
            context.update({'production_impact': True, 'safety_critical': True})
        
        # Map file scope
        if file_scope == "1 file":
            context.update({'file_count': 1, 'lines_estimate': 50})
        elif file_scope == "2-5 files":
            context.update({'file_count': 3, 'lines_estimate': 150})
        elif file_scope == "6-10 files":
            context.update({'file_count': 8, 'lines_estimate': 300, 'coordination_required': True})
        elif file_scope == "More than 10 files":
            context.update({'file_count': 15, 'lines_estimate': 500, 'coordination_required': True})
        
        # Map understanding
        if understanding == "No, I need to research first":
            context.update({'research_needed': True})
        elif understanding == "Mostly, but need some clarification":
            context.update({'research_needed': False, 'complexity': 'moderate'})
        
        # Map criticality
        if criticality in ["Yes, but low risk", "Yes, high risk", "Yes, safety critical"]:
            context.update({'production_impact': True})
        if criticality == "Yes, safety critical":
            context.update({'safety_critical': True})
        
        # Map duration
        if duration == "Quick (< 1 hour)":
            context.update({'duration': 'short'})
        elif duration in ["Medium (1-4 hours)", "Long (> 4 hours)"]:
            context.update({'duration': 'medium'})
        elif duration == "Multiple days":
            context.update({'duration': 'extended'})
        
        return context
    
    def _render_path_analysis(self):
        """Render path analysis interface"""
        st.markdown("### 📊 Path Analysis")
        
        if not hasattr(st.session_state, 'simulation_results') or not st.session_state.simulation_results:
            st.info("No simulation results available. Run some simulations first!")
            return
        
        # Analysis options
        analysis_type = st.selectbox(
            "Analysis Type",
            ["Path Comparison", "Node Frequency", "Confidence Distribution", "Decision Points"]
        )
        
        if analysis_type == "Path Comparison":
            self._render_path_comparison()
        elif analysis_type == "Node Frequency":
            self._render_node_frequency()
        elif analysis_type == "Confidence Distribution":
            self._render_confidence_distribution()
        elif analysis_type == "Decision Points":
            self._render_decision_points()
    
    def _render_path_comparison(self):
        """Render path comparison analysis"""
        st.markdown("#### 🔀 Path Comparison")
        # Implementation for path comparison
        st.info("Path comparison analysis - shows different paths taken for similar inputs")
    
    def _render_node_frequency(self):
        """Render node frequency analysis"""
        st.markdown("#### 📈 Node Frequency")
        # Implementation for node frequency
        st.info("Node frequency analysis - shows which nodes are visited most often")
    
    def _render_confidence_distribution(self):
        """Render confidence distribution analysis"""
        st.markdown("#### 📊 Confidence Distribution")
        # Implementation for confidence distribution
        st.info("Confidence distribution analysis - shows confidence levels across decisions")
    
    def _render_decision_points(self):
        """Render decision points analysis"""
        st.markdown("#### ⚡ Decision Points")
        # Implementation for decision points
        st.info("Decision points analysis - shows critical decision nodes in the tree")
    
    def _render_confidence_analysis(self):
        """Render confidence analysis interface"""
        st.markdown("### 🎯 Confidence Analysis")
        
        # Run all sample scenarios
        if st.button("🚀 Run All Sample Scenarios"):
            results = []
            progress_bar = st.progress(0)
            
            for i, sample in enumerate(self.sample_inputs):
                path = self.simulate_routing_decision(sample['context'])
                results.append(path)
                progress_bar.progress((i + 1) / len(self.sample_inputs))
            
            # Display confidence analysis
            fig = self.render_confidence_analysis(results)
            st.plotly_chart(fig, use_container_width=True)
            
            # Summary statistics
            st.subheader("📊 Summary Statistics")
            
            avg_confidence = sum(path.confidence_score for path in results) / len(results)
            command_counts = Counter(path.final_recommendation for path in results)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Average Confidence", f"{avg_confidence:.1%}")
            with col2:
                st.metric("Most Common Command", command_counts.most_common(1)[0][0])
            with col3:
                st.metric("Unique Commands", len(command_counts))
            
            # Detailed results
            st.subheader("📝 Detailed Results")
            
            results_data = []
            for i, (sample, path) in enumerate(zip(self.sample_inputs, results)):
                results_data.append({
                    'Scenario': sample['name'],
                    'Expected': sample['expected_command'],
                    'Recommended': path.final_recommendation,
                    'Confidence': f"{path.confidence_score:.1%}",
                    'Match': '✅' if path.final_recommendation == sample['expected_command'] else '❌'
                })
            
            st.table(results_data)
        
        # Individual scenario analysis
        st.subheader("🔍 Individual Scenario Analysis")
        
        scenario_names = [sample['name'] for sample in self.sample_inputs]
        selected_scenario = st.selectbox("Select scenario for detailed analysis:", scenario_names)
        
        if selected_scenario:
            scenario = next(s for s in self.sample_inputs if s['name'] == selected_scenario)
            path = self.simulate_routing_decision(scenario['context'])
            
            # Show detailed confidence breakdown
            st.markdown("#### Confidence Breakdown")
            
            for node in path.nodes:
                if node.confidence > 0:
                    st.markdown(f"**{node.name}**: {node.confidence:.1%}")
                    st.progress(node.confidence)