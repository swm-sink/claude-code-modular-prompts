"""
Helper functions for Module Visualizer Component
Provides utility functions for visualization and analysis
"""

import networkx as nx
import plotly.graph_objects as go
import ast
from typing import Dict, List, Any, Optional
from collections import defaultdict
import re


def create_network_figure(graph: nx.DiGraph, 
                         layout: str = 'spring',
                         color_by_category: bool = False,
                         interactive: bool = False,
                         enable_zoom_pan: bool = False) -> go.Figure:
    """Create interactive network visualization figure"""
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


def create_complexity_heatmap(modules: List[Any], 
                             complexity_data: Dict[str, Dict[str, Any]],
                             category_filter: Optional[str] = None,
                             interactive: bool = False) -> go.Figure:
    """Create complexity heatmap visualization"""
    # Filter modules by category if specified
    if category_filter:
        modules = [m for m in modules if m.category == category_filter]
    
    # Prepare data for heatmap
    module_names = [m.name for m in modules]
    complexity_scores = [complexity_data.get(m.name, {}).get('complexity', 0) for m in modules]
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=[complexity_scores],
        x=module_names,
        y=['Complexity'],
        colorscale='Viridis',
        showscale=True,
        hoverongaps=False
    ))
    
    # Update layout
    fig.update_layout(
        title='Module Complexity Heatmap',
        xaxis_title='Modules',
        yaxis_title='Metrics',
        xaxis=dict(tickangle=45),
        height=200
    )
    
    if interactive:
        fig.update_layout(
            hovermode='closest',
            clickmode='event+select'
        )
    
    return fig


def calculate_cyclomatic_complexity(tree: ast.AST) -> int:
    """Calculate cyclomatic complexity from AST"""
    complexity = 1  # Base complexity
    
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.While, ast.For, ast.AsyncFor)):
            complexity += 1
        elif isinstance(node, ast.ExceptHandler):
            complexity += 1
        elif isinstance(node, ast.With, ast.AsyncWith):
            complexity += 1
        elif isinstance(node, ast.BoolOp):
            complexity += len(node.values) - 1
    
    return complexity


def analyze_file_complexity(file_path: str, include_ast: bool = False) -> Dict[str, Any]:
    """Analyze file complexity metrics"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic metrics
        lines = content.split('\n')
        total_lines = len(lines)
        code_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        
        # Count functions/classes
        function_count = len(re.findall(r'def\s+\w+', content))
        class_count = len(re.findall(r'class\s+\w+', content))
        
        # Basic complexity score
        complexity = function_count + class_count
        
        result = {
            'complexity': complexity,
            'lines': total_lines,
            'code_lines': len(code_lines),
            'functions': function_count,
            'classes': class_count
        }
        
        if include_ast:
            try:
                # Try to parse as Python for AST analysis
                python_code = re.findall(r'```python\n(.*?)\n```', content, re.DOTALL)
                if python_code:
                    code_to_analyze = '\n'.join(python_code)
                    tree = ast.parse(code_to_analyze)
                    
                    # Calculate cyclomatic complexity
                    cyclomatic = calculate_cyclomatic_complexity(tree)
                    result['cyclomatic_complexity'] = cyclomatic
                    result['ast_complexity'] = complexity + cyclomatic
                else:
                    result['cyclomatic_complexity'] = 0
                    result['ast_complexity'] = complexity
            except:
                result['cyclomatic_complexity'] = 0
                result['ast_complexity'] = complexity
        
        return result
        
    except (FileNotFoundError, PermissionError):
        return {
            'complexity': 0,
            'lines': 0,
            'code_lines': 0,
            'functions': 0,
            'classes': 0,
            'error': 'file_access_error'
        }
    except Exception as e:
        return {
            'complexity': 0,
            'lines': 0,
            'code_lines': 0,
            'functions': 0,
            'classes': 0,
            'error': str(e)
        }


def build_hierarchical_tree(modules: List[Any], include_dependencies: bool = False) -> Dict[str, Any]:
    """Build hierarchical tree structure from modules"""
    tree = {}
    
    for module in modules:
        # Handle nested categories (e.g., 'patterns/routing')
        parts = module.category.split('/')
        current_node = tree
        
        # Navigate/create nested structure
        for part in parts:
            if part not in current_node:
                current_node[part] = {'modules': [], 'children': {}}
            current_node = current_node[part]['children']
        
        # Add module to the final category
        final_category = parts[-1]
        if final_category not in tree:
            tree[final_category] = {'modules': [], 'children': {}}
        
        # Build tree path
        current_level = tree
        for part in parts[:-1]:
            current_level = current_level[part]['children']
        
        if final_category not in current_level:
            current_level[final_category] = {'modules': [], 'children': {}}
        
        module_data = {
            'name': module.name,
            'path': module.path,
            'category': module.category,
            'description': module.description or 'No description',
            'tags': module.tags or []
        }
        
        if include_dependencies:
            module_data['dependencies'] = module.dependencies or []
        
        current_level[final_category]['modules'].append(module_data)
    
    return tree


def handle_zoom_pan_controls(figure: go.Figure, 
                           action: str = 'reset',
                           zoom_level: float = 1.0) -> go.Figure:
    """Handle zoom and pan controls for visualization"""
    try:
        if action == 'reset':
            # Reset zoom and pan
            figure.update_layout(
                xaxis=dict(range=None),
                yaxis=dict(range=None)
            )
        elif action == 'zoom_in':
            # Zoom in by reducing axis ranges
            figure.update_layout(
                xaxis=dict(range=[-zoom_level, zoom_level]),
                yaxis=dict(range=[-zoom_level, zoom_level])
            )
        elif action == 'zoom_out':
            # Zoom out by expanding axis ranges
            figure.update_layout(
                xaxis=dict(range=[-zoom_level * 2, zoom_level * 2]),
                yaxis=dict(range=[-zoom_level * 2, zoom_level * 2])
            )
        
        return figure
        
    except Exception as e:
        return figure


def create_category_pie_chart(modules: List[Any], 
                             chart_type: str = 'pie',
                             show_counts: bool = False) -> go.Figure:
    """Create category distribution pie chart"""
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


def analyze_module_usage(graph: nx.DiGraph, modules: List[Any]) -> Dict[str, Any]:
    """Analyze module usage patterns"""
    try:
        # Calculate metrics
        usage_counts = {}
        for module in modules:
            # Count incoming dependencies (how many modules depend on this one)
            incoming = len(list(graph.predecessors(module.name))) if graph.has_node(module.name) else 0
            # Count outgoing dependencies (how many modules this one depends on)
            outgoing = len(list(graph.successors(module.name))) if graph.has_node(module.name) else 0
            usage_counts[module.name] = incoming + outgoing
        
        # Find most and least used modules
        if usage_counts:
            most_used = max(usage_counts.items(), key=lambda x: x[1])
            least_used = min(usage_counts.items(), key=lambda x: x[1])
        else:
            most_used = ('none', 0)
            least_used = ('none', 0)
        
        # Count dependencies by category
        dependency_count = defaultdict(int)
        usage_by_category = defaultdict(int)
        
        for module in modules:
            dependency_count[module.category] += len(module.dependencies)
            usage_by_category[module.category] += usage_counts.get(module.name, 0)
        
        return {
            'most_used': most_used,
            'least_used': least_used,
            'dependency_count': dict(dependency_count),
            'usage_by_category': dict(usage_by_category)
        }
        
    except Exception as e:
        return {
            'most_used': ('error', 0),
            'least_used': ('error', 0),
            'dependency_count': {},
            'usage_by_category': {},
            'error': str(e)
        }


def create_usage_frequency_chart(modules: List[Any], 
                                usage_data: Dict[str, Any],
                                chart_type: str = 'bar',
                                show_values: bool = False) -> go.Figure:
    """Create usage frequency chart"""
    try:
        # Extract usage data
        usage_counts = {}
        for module in modules:
            usage_counts[module.name] = usage_data.get('usage_by_category', {}).get(module.category, 0)
        
        names = list(usage_counts.keys())
        values = list(usage_counts.values())
        
        # Create chart based on type
        if chart_type == 'pie':
            fig = go.Figure(data=[go.Pie(
                labels=names,
                values=values,
                name='Usage Frequency'
            )])
        else:  # bar chart
            fig = go.Figure(data=[go.Bar(
                x=names,
                y=values,
                name='Usage Frequency'
            )])
        
        # Configure text display
        if show_values and chart_type == 'pie':
            fig.data[0].textinfo = 'label+percent+value'
        
        fig.update_layout(
            title='Module Usage Frequency',
            showlegend=True
        )
        
        return fig
        
    except Exception as e:
        return go.Figure()


def analyze_module_usage_patterns(modules: List[Any],
                                 graph: nx.DiGraph,
                                 historical_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Analyze module usage patterns with historical data"""
    try:
        # Basic usage analysis
        usage_analysis = analyze_module_usage(graph, modules)
        
        # Add patterns analysis
        patterns = {
            'high_usage_modules': [],
            'isolated_modules': [],
            'dependency_clusters': [],
            'usage_trends': {}
        }
        
        # Find high usage modules (top 20%)
        usage_counts = [(m.name, len(m.dependencies)) for m in modules]
        usage_counts.sort(key=lambda x: x[1], reverse=True)
        top_count = max(1, len(usage_counts) // 5)
        patterns['high_usage_modules'] = [name for name, count in usage_counts[:top_count]]
        
        # Find isolated modules (no dependencies)
        patterns['isolated_modules'] = [m.name for m in modules if not m.dependencies]
        
        # Historical trends if available
        if historical_data:
            patterns['usage_trends'] = historical_data.get('trends', {})
        
        return {
            **usage_analysis,
            'patterns': patterns
        }
        
    except Exception as e:
        return {
            'most_used': ('error', 0),
            'least_used': ('error', 0),
            'dependency_count': {},
            'usage_by_category': {},
            'patterns': {},
            'error': str(e)
        }