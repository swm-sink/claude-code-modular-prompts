"""
Module Visualizer Component for Claude Code Modular Prompts Framework
Provides interactive module exploration, dependency visualization, and analysis
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx
from typing import Dict, List, Optional, Any, Union, Tuple
from pathlib import Path
import time
import json
import re
import ast
import traceback
from collections import defaultdict
from data.framework_parser import FrameworkParser
from data.models import Module, Framework
from components.module_visualizer_helpers import (
    create_network_figure,
    create_complexity_heatmap,
    analyze_file_complexity,
    build_hierarchical_tree,
    create_category_pie_chart,
    analyze_module_usage
)


class ModuleVisualizer:
    """Interactive module visualization component with dependency analysis and network graphs"""
    
    def __init__(self, **kwargs):
        """Initialize the module visualizer"""
        # Handle explicit None passed as keyword argument
        if 'framework_path' in kwargs:
            framework_path = kwargs['framework_path']
            if framework_path is None:
                raise ValueError("framework_path cannot be None")
            if not isinstance(framework_path, Path):
                raise TypeError("framework_path must be a Path object")
            self.framework_path = framework_path
        else:
            # Default to .claude directory
            self.framework_path = Path(__file__).parent.parent.parent / ".claude"
        
        # Initialize framework parser
        try:
            self.framework_parser = FrameworkParser(self.framework_path)
        except Exception as e:
            # Store error for later handling
            self.framework_parser = None
            self._init_error = str(e)
        
        # Initialize state
        self.selected_module: Optional[Module] = None
        self.filter_state: Dict[str, Any] = {}
        self.dependency_graph: Optional[nx.DiGraph] = None
        self.layout_config: Dict[str, Any] = {
            'algorithm': 'force_directed',
            'node_size': 'medium',
            'edge_width': 1.0,
            'zoom_level': 1.0,
            'pan_position': {'x': 0.0, 'y': 0.0},
            'color_scheme': 'default'
        }
    
    def load_modules_from_framework(self, retry_on_failure: bool = False) -> List[Module]:
        """Load modules from framework using the parser"""
        try:
            framework_data = self.framework_parser.parse()
            
            # Check if framework is valid
            if not framework_data.get('metadata', {}).get('is_valid', True):
                error_msg = framework_data.get('metadata', {}).get('error', 'Invalid framework')
                st.error(f"Framework error: {error_msg}")
                return []
            
            modules_data = framework_data.get('modules', [])
            
            modules = []
            for module_data in modules_data:
                try:
                    # Handle incomplete module data gracefully
                    if 'name' not in module_data:
                        st.warning(f"Module missing name field: {module_data}")
                        continue
                    
                    # Create Module object from data
                    module = Module(
                        name=module_data['name'],
                        path=module_data['path'],
                        category=module_data['category'],
                        description=module_data.get('description'),
                        version=module_data.get('version'),
                        dependencies=module_data.get('dependencies', []),
                        tags=module_data.get('tags', [])
                    )
                    modules.append(module)
                    
                except Exception as e:
                    st.warning(f"Error loading module {module_data.get('name', 'unknown')}: {str(e)}")
                    continue
            
            return modules
            
        except (ConnectionError, PermissionError) as e:
            if retry_on_failure:
                # Retry once on transient errors
                try:
                    return self.load_modules_from_framework(False)
                except:
                    pass
            raise e
        except FileNotFoundError:
            raise FileNotFoundError("Framework directory not found")
    
    def parse_module_dependencies(self, modules: List[Module]) -> Dict[str, Any]:
        """Parse module dependencies and return analysis"""
        nodes = []
        edges = []
        missing_dependencies = []
        circular_dependencies = []
        
        # Create a mapping of module names to modules
        module_map = {module.name: module for module in modules}
        
        # Build nodes and edges
        for module in modules:
            # Add node
            nodes.append({
                'id': module.name,
                'name': module.name,
                'category': module.category,
                'description': module.description or '',
                'dependencies_count': len(module.dependencies)
            })
            
            # Add edges for dependencies
            for dep in module.dependencies:
                if dep in module_map:
                    edges.append({
                        'source': module.name,
                        'target': dep,
                        'weight': 1.0
                    })
                else:
                    missing_dependencies.append(dep)
        
        # Detect circular dependencies
        graph = nx.DiGraph()
        for edge in edges:
            graph.add_edge(edge['source'], edge['target'])
        
        try:
            cycles = list(nx.simple_cycles(graph))
            for cycle in cycles:
                circular_dependencies.extend(cycle)
        except:
            pass
        
        return {
            'nodes': nodes,
            'edges': edges,
            'missing_dependencies': list(set(missing_dependencies)),
            'circular_dependencies': circular_dependencies
        }
    
    def filter_modules_by_category(self, modules: List[Module], 
                                  categories: Union[str, List[str]]) -> List[Module]:
        """Filter modules by category or categories"""
        if not modules:
            return []
        
        if isinstance(categories, str):
            categories = [categories]
        
        return [module for module in modules if module.category in categories]
    
    def filter_modules_by_type(self, modules: List[Module], 
                              complexity: str = None) -> List[Module]:
        """Filter modules by type/complexity"""
        if not modules or not complexity:
            return modules
        
        return [module for module in modules if complexity in module.tags]
    
    def search_modules_by_content(self, modules: List[Module], 
                                 search_term: str,
                                 search_file_content: bool = False,
                                 use_regex: bool = False) -> List[Module]:
        """Search modules by name, description, or file content"""
        if not modules or not search_term:
            return modules
        
        results = []
        
        for module in modules:
            # Search in name and description
            if use_regex:
                try:
                    pattern = re.compile(search_term, re.IGNORECASE)
                    if (pattern.search(module.name) or 
                        (module.description and pattern.search(module.description))):
                        results.append(module)
                        continue
                except:
                    # Fall back to simple search if regex fails
                    if (search_term.lower() in module.name.lower() or 
                        (module.description and search_term.lower() in module.description.lower())):
                        results.append(module)
                        continue
            else:
                if (search_term.lower() in module.name.lower() or 
                    (module.description and search_term.lower() in module.description.lower())):
                    results.append(module)
                    continue
            
            # Search in file content if requested
            if search_file_content:
                try:
                    with open(module.path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if use_regex:
                            try:
                                pattern = re.compile(search_term, re.IGNORECASE)
                                if pattern.search(content):
                                    results.append(module)
                            except:
                                if search_term.lower() in content.lower():
                                    results.append(module)
                        else:
                            if search_term.lower() in content.lower():
                                results.append(module)
                except:
                    continue
        
        return results
    
    def build_module_tree(self, modules: List[Module], 
                         include_dependencies: bool = False) -> Dict[str, Any]:
        """Build hierarchical module tree structure"""
        tree = {}
        
        for module in modules:
            # Handle nested categories
            if '/' in module.category:
                parts = module.category.split('/')
                current_level = tree
                
                # Navigate through nested structure
                for part in parts[:-1]:
                    if part not in current_level:
                        current_level[part] = {}
                    current_level = current_level[part]
                
                # Get the final category
                category = parts[-1]
                
                # Ensure the final category exists as a list
                if category not in current_level:
                    current_level[category] = []
                
                # Add module to the nested location
                module_entry = {
                    'name': module.name,
                    'path': module.path,
                    'description': module.description or '',
                    'tags': module.tags
                }
                
                if include_dependencies:
                    module_entry['dependencies'] = module.dependencies
                
                current_level[category].append(module_entry)
            else:
                # Simple category
                category = module.category
                
                # Add module to tree
                if category not in tree:
                    tree[category] = []
                
                module_entry = {
                    'name': module.name,
                    'path': module.path,
                    'description': module.description or '',
                    'tags': module.tags
                }
                
                if include_dependencies:
                    module_entry['dependencies'] = module.dependencies
                
                tree[category].append(module_entry)
        
        return tree
    
    def render_module_tree_navigation(self, tree_data: Dict[str, Any], 
                                    enable_search: bool = False):
        """Render module tree navigation UI"""
        if enable_search:
            search_term = st.text_input("Search modules:", placeholder="Type to search...")
        
        for category, modules in tree_data.items():
            with st.expander(f"📁 {category.title()} ({len(modules)} modules)"):
                if enable_search and 'search_term' in locals() and search_term:
                    # Filter modules based on search term
                    filtered_modules = [m for m in modules if search_term.lower() in m['name'].lower()]
                    modules = filtered_modules
                
                for module in modules:
                    if st.button(f"📄 {module['name']}", key=f"nav_{module['name']}"):
                        # Handle module selection
                        st.session_state.selected_module = module['name']
                
                # Add module selector
                if modules:
                    selected = st.selectbox(
                        f"Select from {category}:",
                        options=[m['name'] for m in modules],
                        key=f"select_{category}"
                    )
    
    def expand_category_nodes(self, tree_data: Dict[str, Any], 
                            category: str, 
                            filter_text: str = None) -> List[Dict[str, Any]]:
        """Expand category nodes and return filtered modules"""
        if category not in tree_data:
            return []
        
        modules = tree_data[category]
        
        if filter_text:
            modules = [m for m in modules if filter_text.lower() in m['name'].lower()]
        
        return modules
    
    def create_dependency_graph(self, modules: List[Module], 
                              include_weights: bool = False) -> nx.DiGraph:
        """Create NetworkX dependency graph"""
        graph = nx.DiGraph()
        
        # Add nodes
        for module in modules:
            graph.add_node(module.name, 
                          category=module.category,
                          description=module.description or '',
                          tags=module.tags)
        
        # Add edges
        for module in modules:
            for dep in module.dependencies:
                if graph.has_node(dep):
                    edge_attrs = {}
                    if include_weights:
                        edge_attrs['weight'] = 1.0
                    graph.add_edge(module.name, dep, **edge_attrs)
        
        return graph
    
    def create_network_visualization(self, graph: nx.DiGraph, 
                                   layout: str = 'spring',
                                   color_by_category: bool = False,
                                   interactive: bool = False,
                                   enable_zoom_pan: bool = False,
                                   mobile_optimized: bool = False,
                                   gesture_support: bool = False,
                                   high_contrast: bool = False) -> go.Figure:
        """Create interactive network visualization"""
        try:
            if not isinstance(graph, nx.DiGraph):
                try:
                    st.error("Invalid graph object")
                except:
                    # Handle case where Streamlit is not available (e.g., during testing)
                    print("Invalid graph object")
                # Return empty figure instead of None
                return go.Figure()
            
            # Calculate layout
            if layout == 'spring':
                pos = nx.spring_layout(graph)
            elif layout == 'circular':
                pos = nx.circular_layout(graph)
            elif layout == 'kamada_kawai':
                pos = nx.kamada_kawai_layout(graph)
            elif layout == 'planar':
                try:
                    pos = nx.planar_layout(graph)
                except:
                    pos = nx.spring_layout(graph)
            else:
                pos = nx.spring_layout(graph)
            
            # Create figure
            fig = go.Figure()
            
            # Add nodes first (so they are trace 0)
            node_trace = go.Scatter(
                x=[], y=[],
                mode='markers+text',
                hoverinfo='text',
                text=[],
                textposition="middle center",
                marker=dict(
                    showscale=True,
                    colorscale='Viridis',
                    reversescale=True,
                    color=[],
                    size=10,
                    colorbar=dict(
                        thickness=15,
                        len=0.5,
                        x=0.9,
                        xanchor="left",
                        title="Category"
                    ),
                    line=dict(width=2)
                )
            )
            
            # Set node positions and colors
            categories = list(set(graph.nodes[node].get('category', 'default') for node in graph.nodes()))
            category_colors = {cat: i for i, cat in enumerate(categories)}
            
            for node in graph.nodes():
                x, y = pos[node]
                node_trace['x'] += (x,)
                node_trace['y'] += (y,)
                node_trace['text'] += (node,)
                
                if color_by_category:
                    cat = graph.nodes[node].get('category', 'default')
                    node_trace['marker']['color'] += (category_colors.get(cat, 0),)
                else:
                    node_trace['marker']['color'] += (0,)
            
            # Add hover information
            if interactive:
                node_info = []
                for node in graph.nodes():
                    info = f"Module: {node}<br>"
                    info += f"Category: {graph.nodes[node].get('category', 'N/A')}<br>"
                    info += f"Dependencies: {len(list(graph.predecessors(node)))}<br>"
                    info += f"Dependents: {len(list(graph.successors(node)))}"
                    node_info.append(info)
                
                node_trace['hovertemplate'] = '<b>%{text}</b><br>' + \
                                            'Category: %{customdata}<br>' + \
                                            '<extra></extra>'
                node_trace['customdata'] = [graph.nodes[node].get('category', 'N/A') for node in graph.nodes()]
            
            fig.add_trace(node_trace)
            
            # Add edges second (so they are trace 1)
            edge_trace = go.Scatter(
                x=[], y=[], 
                line=dict(width=1, color='#888'),
                hoverinfo='none',
                mode='lines'
            )
            
            for edge in graph.edges():
                x0, y0 = pos[edge[0]]
                x1, y1 = pos[edge[1]]
                edge_trace['x'] += (x0, x1, None)
                edge_trace['y'] += (y0, y1, None)
            
            fig.add_trace(edge_trace)
            
            # Update layout
            layout_config = dict(
                title=dict(text='Module Dependency Network', font=dict(size=16)),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20, l=5, r=5, t=40),
                annotations=[
                    dict(
                        text="Module dependencies visualization",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002,
                        xanchor='left', yanchor='bottom',
                        font=dict(color='#999', size=12)
                    )
                ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
            )
            
            if interactive:
                layout_config['hovermode'] = 'closest'
                layout_config['clickmode'] = 'event+select'
            
            if enable_zoom_pan:
                layout_config['xaxis']['fixedrange'] = False
                layout_config['yaxis']['fixedrange'] = False
            
            fig.update_layout(**layout_config)
            
            return fig
            
        except Exception as e:
            try:
                st.error(f"Error creating network visualization: {str(e)}")
            except:
                # If Streamlit is not available (e.g., during testing), just print
                print(f"Error creating network visualization: {str(e)}")
            # Return empty figure instead of None
            return go.Figure()
    
    def calculate_module_complexity(self, module: Module, 
                                  include_ast_analysis: bool = False) -> Dict[str, Any]:
        """Calculate module complexity metrics"""
        try:
            with open(module.path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic metrics
            lines = content.split('\n')
            total_lines = len(lines)
            code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
            
            # Count functions/classes
            function_count = len(re.findall(r'def\s+\w+', content))
            class_count = len(re.findall(r'class\s+\w+', content))
            
            # Basic complexity score
            complexity = len(module.dependencies) + function_count + class_count
            
            result = {
                'complexity': complexity,
                'lines': total_lines,
                'code_lines': len(code_lines),
                'dependencies': len(module.dependencies),
                'functions': function_count,
                'classes': class_count
            }
            
            if include_ast_analysis:
                try:
                    # Try to parse as Python for AST analysis
                    python_code = re.findall(r'```python\n(.*?)\n```', content, re.DOTALL)
                    if python_code:
                        code_to_analyze = '\n'.join(python_code)
                        tree = ast.parse(code_to_analyze)
                        
                        # Calculate cyclomatic complexity
                        cyclomatic = self._calculate_cyclomatic_complexity(tree)
                        result['cyclomatic_complexity'] = cyclomatic
                        result['ast_complexity'] = complexity + cyclomatic
                    else:
                        result['cyclomatic_complexity'] = 0
                        result['ast_complexity'] = complexity
                except:
                    result['cyclomatic_complexity'] = 0
                    result['ast_complexity'] = complexity
            
            return result
            
        except (FileNotFoundError, PermissionError) as e:
            return {
                'complexity': 0,
                'lines': 0,
                'code_lines': 0,
                'dependencies': 0,
                'functions': 0,
                'classes': 0,
                'error': str(e)
            }
        except Exception as e:
            return {
                'complexity': 0,
                'lines': 0,
                'code_lines': 0,
                'dependencies': 0,
                'functions': 0,
                'classes': 0,
                'error': str(e)
            }
    
    def _calculate_cyclomatic_complexity(self, tree: ast.AST) -> int:
        """Calculate cyclomatic complexity from AST"""
        complexity = 1  # Base complexity
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.For, ast.While, ast.Try, ast.With)):
                complexity += 1
            elif isinstance(node, ast.ExceptHandler):
                complexity += 1
        
        return complexity
    
    def create_complexity_heatmap(self, modules: List[Module], 
                                group_by: str = 'module',
                                interactive: bool = False) -> go.Figure:
        """Create complexity heatmap visualization"""
        try:
            complexity_data = []
            
            for module in modules:
                complexity_info = self.calculate_module_complexity(module)
                complexity_data.append({
                    'module': module.name,
                    'category': module.category,
                    'complexity': complexity_info['complexity'],
                    'lines': complexity_info['lines'],
                    'dependencies': complexity_info['dependencies']
                })
            
            # Create heatmap
            if group_by == 'category':
                # Group by category
                df = pd.DataFrame(complexity_data)
                pivot_df = df.pivot_table(
                    values='complexity', 
                    index='category', 
                    columns='module',
                    fill_value=0
                )
                
                fig = go.Figure(data=go.Heatmap(
                    z=pivot_df.values,
                    x=pivot_df.columns,
                    y=pivot_df.index,
                    colorscale='Viridis'
                ))
            else:
                # Individual modules
                fig = go.Figure(data=go.Heatmap(
                    z=[[item['complexity'] for item in complexity_data]],
                    x=[item['module'] for item in complexity_data],
                    y=['Complexity'],
                    colorscale='Viridis'
                ))
            
            fig.update_layout(
                title='Module Complexity Heatmap',
                xaxis_title='Modules',
                yaxis_title='Categories' if group_by == 'category' else 'Metrics'
            )
            
            if interactive:
                fig.update_layout(hovermode='closest')
                # Add hover template
                fig.data[0].hovertemplate = '<b>%{x}</b><br>' + \
                                          'Category: %{y}<br>' + \
                                          'Complexity: %{z}<br>' + \
                                          '<extra></extra>'
            
            return fig
            
        except Exception as e:
            st.error(f"Error creating complexity heatmap: {str(e)}")
            return go.Figure()
    
    def create_usage_frequency_chart(self, modules: List[Module], 
                                   usage_data: Dict[str, int],
                                   chart_type: str = 'bar') -> go.Figure:
        """Create usage frequency chart"""
        try:
            # Prepare data
            names = []
            values = []
            
            for module in modules:
                names.append(module.name)
                values.append(usage_data.get(module.name, 0))
            
            # Create chart based on type
            if chart_type == 'bar':
                fig = go.Figure(data=[go.Bar(
                    x=names,
                    y=values,
                    name='Usage Frequency'
                )])
                fig.update_layout(
                    title='Module Usage Frequency',
                    xaxis_title='Modules',
                    yaxis_title='Usage Count'
                )
            elif chart_type == 'pie':
                fig = go.Figure(data=[go.Pie(
                    labels=names,
                    values=values,
                    name='Usage Frequency'
                )])
                fig.update_layout(title='Module Usage Distribution')
            else:
                # Default to bar chart
                fig = go.Figure(data=[go.Bar(
                    x=names,
                    y=values,
                    name='Usage Frequency'
                )])
                fig.update_layout(
                    title='Module Usage Frequency',
                    xaxis_title='Modules',
                    yaxis_title='Usage Count'
                )
            
            return fig
            
        except Exception as e:
            st.error(f"Error creating usage frequency chart: {str(e)}")
            return go.Figure()
    
    def analyze_module_usage_patterns(self, modules: List[Module],
                                    historical_data: Optional[Dict[str, List[int]]] = None) -> Dict[str, Any]:
        """Analyze module usage patterns"""
        try:
            # Count dependencies as usage indicator
            usage_count = defaultdict(int)
            
            for module in modules:
                for dep in module.dependencies:
                    usage_count[dep] += 1
            
            # Sort by usage
            sorted_usage = sorted(usage_count.items(), key=lambda x: x[1], reverse=True)
            
            # Basic analysis
            most_used = sorted_usage[0] if sorted_usage else ('none', 0)
            least_used = sorted_usage[-1] if sorted_usage else ('none', 0)
            
            # Category analysis
            usage_by_category = defaultdict(int)
            for module in modules:
                usage_by_category[module.category] += usage_count.get(module.name, 0)
            
            result = {
                'most_used': most_used,
                'least_used': least_used,
                'dependency_count': dict(usage_count),
                'usage_by_category': dict(usage_by_category)
            }
            
            # Add historical analysis if provided
            if historical_data:
                trends = {}
                growth_rate = {}
                
                for module_name, data_points in historical_data.items():
                    if len(data_points) >= 2:
                        # Calculate growth rate
                        growth = ((data_points[-1] - data_points[0]) / data_points[0]) * 100 if data_points[0] > 0 else 0
                        growth_rate[module_name] = growth
                        
                        # Simple trend analysis
                        if growth > 10:
                            trends[module_name] = 'increasing'
                        elif growth < -10:
                            trends[module_name] = 'decreasing'
                        else:
                            trends[module_name] = 'stable'
                
                result['trends'] = trends
                result['growth_rate'] = growth_rate
            
            return result
            
        except Exception as e:
            return {
                'most_used': ('error', 0),
                'least_used': ('error', 0),
                'dependency_count': {},
                'usage_by_category': {},
                'error': str(e)
            }
    
    def create_category_distribution_chart(self, modules: List[Module],
                                         chart_type: str = 'pie',
                                         show_counts: bool = False,
                                         text_size: str = 'medium',
                                         mobile_optimized: bool = False) -> go.Figure:
        """Create category distribution chart"""
        try:
            # Count modules by category
            category_counts = defaultdict(int)
            for module in modules:
                category_counts[module.category] += 1
            
            categories = list(category_counts.keys())
            counts = list(category_counts.values())
            
            # Create chart
            if chart_type == 'donut':
                fig = go.Figure(data=[go.Pie(
                    labels=categories,
                    values=counts,
                    hole=0.3,
                    name='Category Distribution'
                )])
            else:
                fig = go.Figure(data=[go.Pie(
                    labels=categories,
                    values=counts,
                    name='Category Distribution'
                )])
            
            # Configure text display
            if show_counts:
                fig.data[0].textinfo = 'label+percent+value'
            else:
                fig.data[0].textinfo = 'label+percent'
            
            fig.update_layout(
                title='Module Category Distribution',
                showlegend=True
            )
            
            return fig
            
        except Exception as e:
            st.error(f"Error creating category distribution chart: {str(e)}")
            return go.Figure()
    
    def handle_module_selection(self, module: Optional[Module], 
                               callback=None) -> bool:
        """Handle module selection with optional callback"""
        if module is None:
            self.selected_module = None
            return False
        
        if not isinstance(module, Module):
            raise TypeError("module must be a Module instance")
        
        self.selected_module = module
        
        # Execute callback if provided
        if callback:
            callback(module)
        
        return True
    
    def render_module_details_panel(self, module: Module,
                                   show_content: bool = False,
                                   show_dependencies: bool = False):
        """Render module details panel"""
        st.subheader(f"📋 Module Details: {module.name}")
        
        # Basic information
        st.markdown(f"**Category:** {module.category}")
        st.markdown(f"**Description:** {module.description or 'No description'}")
        st.markdown(f"**Path:** {module.path}")
        
        # Dependencies
        if module.dependencies:
            st.markdown(f"**Dependencies:** {', '.join(module.dependencies)}")
        else:
            st.markdown("**Dependencies:** None")
        
        # Tags
        if module.tags:
            st.markdown(f"**Tags:** {', '.join(module.tags)}")
        
        # Module metadata as JSON
        module_data = {
            'name': module.name,
            'category': module.category,
            'description': module.description,
            'dependencies': module.dependencies,
            'tags': module.tags,
            'path': module.path
        }
        st.json(module_data)
        
        # Show file content if requested
        if show_content:
            try:
                with open(module.path, 'r', encoding='utf-8') as f:
                    content = f.read()
                st.code(content, language='markdown')
            except Exception as e:
                st.error(f"Error reading file: {str(e)}")
        
        # Show dependencies visualization if requested
        if show_dependencies and module.dependencies:
            st.subheader("📊 Dependencies Visualization")
            
            # Create a simple dependency graph
            dep_graph = nx.DiGraph()
            dep_graph.add_node(module.name)
            for dep in module.dependencies:
                dep_graph.add_node(dep)
                dep_graph.add_edge(module.name, dep)
            
            fig = self.create_network_visualization(dep_graph)
            if fig:
                st.plotly_chart(fig, use_container_width=True)
    
    def render_filter_controls(self, categories: List[str],
                              enable_search: bool = False) -> Dict[str, Any]:
        """Render filter controls and return filter state"""
        filters = {}
        
        # Search functionality
        if enable_search:
            search_term = st.text_input("🔍 Search modules:", placeholder="Enter search term...")
            filters['search_term'] = search_term
        
        # Category filter
        selected_categories = st.multiselect(
            "📁 Filter by categories:",
            options=categories,
            default=categories
        )
        filters['categories'] = selected_categories
        
        # Complexity filter
        complexity_level = st.selectbox(
            "🎯 Complexity level:",
            options=['All', 'Simple', 'Medium', 'Complex'],
            index=0
        )
        filters['complexity'] = complexity_level.lower() if complexity_level != 'All' else None
        
        # Dependency count filter
        min_dependencies = st.slider(
            "📎 Minimum dependencies:",
            min_value=0,
            max_value=10,
            value=0
        )
        filters['min_dependencies'] = min_dependencies
        
        return filters
    
    def handle_zoom_pan_controls(self) -> Dict[str, float]:
        """Handle zoom and pan controls"""
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        
        with col1:
            zoom = st.slider("🔍 Zoom", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
        
        with col2:
            pan_x = st.slider("↔️ Pan X", min_value=-1.0, max_value=1.0, value=0.0, step=0.1)
        
        with col3:
            pan_y = st.slider("↕️ Pan Y", min_value=-1.0, max_value=1.0, value=0.0, step=0.1)
        
        with col4:
            if st.button("🔄 Reset View"):
                zoom = 1.0
                pan_x = 0.0
                pan_y = 0.0
        
        return {
            'zoom': zoom,
            'pan_x': pan_x,
            'pan_y': pan_y
        }
    
    def export_visualization_png(self, fig: go.Figure, **kwargs) -> Optional[bytes]:
        """Export visualization as PNG"""
        try:
            import plotly.io as pio
            
            # Default options
            options = {
                'format': 'png',
                'width': 1000,
                'height': 600,
                'scale': 1
            }
            options.update(kwargs)
            
            img_bytes = pio.to_image(fig, **options)
            return img_bytes
            
        except Exception as e:
            st.error(f"Error exporting PNG: {str(e)}")
            return None
    
    def export_visualization_svg(self, fig: go.Figure, **kwargs) -> Optional[bytes]:
        """Export visualization as SVG"""
        try:
            import plotly.io as pio
            
            # Default options
            options = {
                'format': 'svg',
                'width': 1000,
                'height': 600
            }
            options.update(kwargs)
            
            img_bytes = pio.to_image(fig, **options)
            return img_bytes
            
        except Exception as e:
            st.error(f"Error exporting SVG: {str(e)}")
            return None
    
    def export_module_data_json(self, modules: List[Module],
                              include_dependencies: bool = False,
                              metadata: Optional[Dict[str, Any]] = None) -> str:
        """Export module data as JSON"""
        try:
            if include_dependencies:
                # Include full dependency analysis
                dep_analysis = self.parse_module_dependencies(modules)
                
                data = {
                    'modules': [module.to_dict() for module in modules],
                    'dependencies': dep_analysis
                }
            else:
                # Simple module list
                data = [module.to_dict() for module in modules]
            
            # Add metadata if provided
            if metadata:
                if isinstance(data, list):
                    data = {
                        'modules': data,
                        'metadata': metadata
                    }
                else:
                    data['metadata'] = metadata
            
            return json.dumps(data, indent=2)
            
        except Exception as e:
            st.error(f"Error exporting JSON: {str(e)}")
            return "{}"
    
    def render(self):
        """Main render method for the module visualizer UI"""
        try:
            # Header
            st.title("🧩 Module Visualizer")
            st.markdown("Explore and analyze framework modules with interactive visualizations")
            
            # Check initialization
            if hasattr(self, '_init_error'):
                st.error(f"Framework initialization failed: {self._init_error}")
                return
            
            if self.framework_parser is None:
                st.error("Framework parser not initialized")
                return
            
            # Load modules
            try:
                modules = self.load_modules_from_framework()
                if not modules:
                    st.info("No modules found in the framework")
                    return
            except FileNotFoundError:
                st.error("Framework not found")
                return
            except Exception as e:
                st.error(f"Error loading modules: {str(e)}")
                return
            
            # Render main interface
            self._render_main_interface(modules)
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    def _render_main_interface(self, modules: List[Module]):
        """Render the main interface components"""
        # Sidebar filters
        with st.sidebar:
            st.header("🎛️ Filters")
            categories = list(set(module.category for module in modules))
            filters = self.render_filter_controls(categories, enable_search=True)
        
        # Apply filters
        filtered_modules = self._apply_filters(modules, filters)
        
        # Main content area
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Module tree navigation
            st.subheader("📁 Module Tree")
            tree_data = self.build_module_tree(filtered_modules)
            self.render_module_tree_navigation(tree_data, enable_search=True)
        
        with col2:
            # Module selector
            if filtered_modules:
                selected_module_name = st.selectbox(
                    "Select a module to explore:",
                    options=[module.name for module in filtered_modules],
                    key="module_selector"
                )
                
                if selected_module_name:
                    selected_module = next((m for m in filtered_modules if m.name == selected_module_name), None)
                    if selected_module:
                        self.handle_module_selection(selected_module)
                        self.render_module_details_panel(selected_module, show_content=True)
        
        # Visualizations
        st.subheader("📊 Module Visualizations")
        
        # Network visualization
        st.write("**Dependency Network**")
        graph = self.create_dependency_graph(filtered_modules)
        network_fig = self.create_network_visualization(graph, interactive=True)
        if network_fig:
            st.plotly_chart(network_fig, use_container_width=True)
        
        # Other visualizations
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            st.write("**Complexity Analysis**")
            complexity_fig = self.create_complexity_heatmap(filtered_modules)
            st.plotly_chart(complexity_fig, use_container_width=True)
        
        with viz_col2:
            st.write("**Category Distribution**")
            category_fig = self.create_category_distribution_chart(filtered_modules)
            st.plotly_chart(category_fig, use_container_width=True)
        
        # Export options
        st.subheader("📤 Export Options")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📁 Export PNG"):
                if network_fig:
                    png_data = self.export_visualization_png(network_fig)
                    if png_data:
                        st.download_button(
                            label="Download PNG",
                            data=png_data,
                            file_name="module_network.png",
                            mime="image/png"
                        )
        
        with col2:
            if st.button("📁 Export SVG"):
                if network_fig:
                    svg_data = self.export_visualization_svg(network_fig)
                    if svg_data:
                        st.download_button(
                            label="Download SVG",
                            data=svg_data,
                            file_name="module_network.svg",
                            mime="image/svg+xml"
                        )
        
        with col3:
            if st.button("📁 Export JSON"):
                json_data = self.export_module_data_json(filtered_modules, include_dependencies=True)
                st.download_button(
                    label="Download JSON",
                    data=json_data,
                    file_name="module_data.json",
                    mime="application/json"
                )
        
        # Statistics
        st.subheader("📈 Statistics")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Modules", len(modules))
        
        with col2:
            st.metric("Filtered Modules", len(filtered_modules))
        
        with col3:
            st.metric("Categories", len(set(module.category for module in modules)))
        
        with col4:
            total_deps = sum(len(module.dependencies) for module in modules)
            st.metric("Total Dependencies", total_deps)
    
    def _apply_filters(self, modules: List[Module], filters: Dict[str, Any]) -> List[Module]:
        """Apply filters to modules"""
        filtered = modules
        
        # Apply search filter
        if filters.get('search_term'):
            filtered = self.search_modules_by_content(filtered, filters['search_term'])
        
        # Apply category filter
        if filters.get('categories'):
            filtered = self.filter_modules_by_category(filtered, filters['categories'])
        
        # Apply complexity filter
        if filters.get('complexity'):
            filtered = self.filter_modules_by_type(filtered, complexity=filters['complexity'])
        
        # Apply dependency count filter
        if filters.get('min_dependencies', 0) > 0:
            filtered = [m for m in filtered if len(m.dependencies) >= filters['min_dependencies']]
        
        return filtered