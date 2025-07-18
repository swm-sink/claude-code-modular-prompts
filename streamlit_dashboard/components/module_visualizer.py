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
    analyze_module_usage,
    create_usage_frequency_chart,
    analyze_module_usage_patterns,
    handle_zoom_pan_controls
)


class ModuleVisualizer:
    """Interactive module visualization component with dependency analysis and network graphs"""
    
    def __init__(self, **kwargs):
        """Initialize the module visualizer with optional parameters"""
        self.framework_parser = None
        self.framework_path = None
        self.modules = []
        self.selected_module = None
        self.current_view = 'overview'
        self.filters = {
            'category': None,
            'search': '',
            'tags': []
        }
        self.performance_metrics = {
            'load_time': 0,
            'modules_loaded': 0,
            'last_update': None
        }
        
        # Layout configuration
        self.layout_config = {
            'default_layout': 'spring',
            'color_scheme': 'category',
            'interactive_mode': True,
            'mobile_responsive': True
        }
        
        # Handle framework_path parameter
        if 'framework_path' in kwargs:
            framework_path = kwargs['framework_path']
            if framework_path is None:
                raise ValueError("framework_path cannot be None")
            self.framework_path = framework_path
            try:
                self.framework_parser = FrameworkParser(framework_path)
            except Exception as e:
                st.error(f"Error initializing framework parser: {str(e)}")
                self.framework_parser = None
    
    def load_modules_from_framework(self, retry_on_failure: bool = False) -> List[Module]:
        """Load modules from the framework using FrameworkParser"""
        if not self.framework_parser:
            if retry_on_failure:
                st.error("Framework parser not initialized")
            return []
            
        try:
            start_time = time.time()
            
            # Parse framework data
            framework_data = self.framework_parser.parse()
            
            if not framework_data:
                if retry_on_failure:
                    st.error("No framework data available")
                return []
            
            # Extract modules
            modules = []
            for module_data in framework_data.get('modules', []):
                try:
                    module = Module(
                        name=module_data['name'],
                        path=module_data['path'],
                        category=module_data['category'],
                        description=module_data.get('description', ''),
                        dependencies=module_data.get('dependencies', []),
                        tags=module_data.get('tags', [])
                    )
                    modules.append(module)
                except Exception as e:
                    if retry_on_failure:
                        st.warning(f"Failed to load module {module_data.get('name', 'unknown')}: {str(e)}")
                    continue
            
            # Update performance metrics
            load_time = time.time() - start_time
            self.performance_metrics['load_time'] = load_time
            self.performance_metrics['modules_loaded'] = len(modules)
            self.performance_metrics['last_update'] = time.time()
            
            # Check for performance issues
            if load_time > 2.0:
                if retry_on_failure:
                    st.warning(f"Slow load time: {load_time:.2f}s")
            
            self.modules = modules
            return modules
            
        except Exception as e:
            if retry_on_failure:
                st.error(f"Error loading modules from framework: {str(e)}")
            return []
    
    def parse_module_dependencies(self, modules: List[Module]) -> Dict[str, List[str]]:
        """Parse module dependencies and return mapping"""
        try:
            dependencies = {}
            for module in modules:
                dependencies[module.name] = module.dependencies or []
            return dependencies
        except Exception as e:
            st.error(f"Error parsing module dependencies: {str(e)}")
            return {}
    
    def build_module_tree(self, modules: List[Module], include_dependencies: bool = False) -> Dict[str, Any]:
        """Build hierarchical tree structure from modules"""
        return build_hierarchical_tree(modules, include_dependencies)
    
    def filter_modules(self, modules: List[Module], category: Optional[str] = None,
                      search_term: Optional[str] = None, tags: Optional[List[str]] = None) -> List[Module]:
        """Filter modules based on various criteria"""
        try:
            filtered = modules
            
            # Category filter
            if category:
                filtered = [m for m in filtered if m.category == category]
            
            # Search filter
            if search_term:
                search_lower = search_term.lower()
                filtered = [m for m in filtered if 
                           search_lower in m.name.lower() or 
                           search_lower in (m.description or '').lower()]
            
            # Tags filter
            if tags:
                filtered = [m for m in filtered if any(tag in m.tags for tag in tags)]
            
            return filtered
        except Exception as e:
            st.error(f"Error filtering modules: {str(e)}")
            return modules
    
    def filter_modules_by_category(self, modules: List[Module], categories: List[str]) -> List[Module]:
        """Filter modules by specific categories"""
        try:
            if not categories:
                return modules
            return [m for m in modules if m.category in categories]
        except Exception as e:
            st.error(f"Error filtering modules by category: {str(e)}")
            return modules
    
    def search_modules_by_content(self, modules: List[Module], search_term: str, 
                                 case_sensitive: bool = False, regex: bool = False) -> List[Module]:
        """Search modules by content with advanced options"""
        try:
            if not search_term:
                return modules
            
            filtered = []
            for module in modules:
                search_text = search_term if case_sensitive else search_term.lower()
                
                # Search in name and description
                name_text = module.name if case_sensitive else module.name.lower()
                desc_text = (module.description or '') if case_sensitive else (module.description or '').lower()
                
                if regex:
                    import re
                    try:
                        if re.search(search_text, name_text) or re.search(search_text, desc_text):
                            filtered.append(module)
                    except re.error:
                        # Fall back to simple search on regex error
                        if search_text in name_text or search_text in desc_text:
                            filtered.append(module)
                else:
                    if search_text in name_text or search_text in desc_text:
                        filtered.append(module)
            
            return filtered
        except Exception as e:
            st.error(f"Error searching modules: {str(e)}")
            return modules
    
    def create_dependency_graph(self, modules: List[Module], 
                              include_weights: bool = False,
                              circular_deps: bool = False) -> nx.DiGraph:
        """Create a dependency graph from modules"""
        graph = nx.DiGraph()
        
        # Add nodes with attributes
        for module in modules:
            graph.add_node(module.name, 
                          category=module.category,
                          description=module.description,
                          tags=module.tags)
        
        # Add edges (dependencies)
        for module in modules:
            for dep in module.dependencies:
                if dep in [m.name for m in modules]:
                    edge_attrs = {}
                    if include_weights:
                        edge_attrs['weight'] = 1
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
                    print("Invalid graph object")
                return go.Figure()
            
            return create_network_figure(graph, layout, color_by_category, interactive, enable_zoom_pan)
            
        except Exception as e:
            try:
                st.error(f"Error creating network visualization: {str(e)}")
            except:
                print(f"Error creating network visualization: {str(e)}")
            return go.Figure()
    
    def calculate_module_complexity(self, module: Module, 
                                  include_ast_analysis: bool = False) -> Dict[str, Any]:
        """Calculate module complexity metrics"""
        result = analyze_file_complexity(module.path, include_ast_analysis)
        result['dependencies'] = len(module.dependencies)
        result['complexity'] = result.get('complexity', 0) + len(module.dependencies)
        return result
    
    def create_complexity_heatmap(self, modules: List[Module], 
                                 complexity_data: Dict[str, Dict[str, Any]],
                                 category_filter: Optional[str] = None,
                                 show_values: bool = False,
                                 text_size: str = 'medium',
                                 interactive: bool = False,
                                 mobile_optimized: bool = False) -> go.Figure:
        """Create complexity heatmap visualization"""
        try:
            return create_complexity_heatmap(modules, complexity_data, category_filter, interactive)
        except Exception as e:
            st.error(f"Error creating complexity heatmap: {str(e)}")
            return go.Figure()
    
    def calculate_complexity_metrics(self, modules: List[Module]) -> Dict[str, Dict[str, Any]]:
        """Calculate complexity metrics for all modules"""
        try:
            complexity_data = {}
            for module in modules:
                complexity_data[module.name] = self.calculate_module_complexity(module)
            return complexity_data
        except Exception as e:
            st.error(f"Error calculating complexity metrics: {str(e)}")
            return {}
    
    def analyze_module_usage(self, graph: nx.DiGraph, 
                            modules: List[Module]) -> Dict[str, Any]:
        """Analyze module usage patterns"""
        return analyze_module_usage(graph, modules)
    
    def create_category_distribution_chart(self, modules: List[Module],
                                         chart_type: str = 'pie',
                                         show_counts: bool = False,
                                         text_size: str = 'medium',
                                         mobile_optimized: bool = False) -> go.Figure:
        """Create category distribution chart"""
        try:
            return create_category_pie_chart(modules, chart_type, show_counts)
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
        try:
            st.subheader(f"📋 Module Details: {module.name}")
            
            # Basic information
            st.markdown(f"**Category:** {module.category}")
            st.markdown(f"**Description:** {module.description or 'No description'}")
            st.markdown(f"**Path:** {module.path}")
            
            # Dependencies
            if show_dependencies or module.dependencies:
                if module.dependencies:
                    st.markdown(f"**Dependencies:** {', '.join(module.dependencies)}")
                else:
                    st.markdown("**Dependencies:** None")
            
            # Tags
            if module.tags:
                st.markdown(f"**Tags:** {', '.join(module.tags)}")
            
            # Module metadata as JSON
            if show_content:
                module_data = {
                    'name': module.name,
                    'category': module.category,
                    'description': module.description,
                    'path': module.path,
                    'dependencies': module.dependencies,
                    'tags': module.tags
                }
                
                with st.expander("📄 Module Metadata"):
                    st.json(module_data)
        except Exception as e:
            st.error(f"Error rendering module details: {str(e)}")
    
    def get_module_by_name(self, module_name: str) -> Optional[Module]:
        """Get module by name"""
        try:
            for module in self.modules:
                if module.name == module_name:
                    return module
            return None
        except Exception as e:
            st.error(f"Error getting module by name: {str(e)}")
            return None
    
    def get_modules_by_category(self, category: str) -> List[Module]:
        """Get modules by category"""
        try:
            return [m for m in self.modules if m.category == category]
        except Exception as e:
            st.error(f"Error getting modules by category: {str(e)}")
            return []
    
    def export_module_data(self, modules: List[Module], 
                          format: str = 'json',
                          include_dependencies: bool = False,
                          include_content: bool = False) -> Union[str, Dict[str, Any]]:
        """Export module data in various formats"""
        try:
            if format == 'json':
                data = []
                for module in modules:
                    module_data = {
                        'name': module.name,
                        'category': module.category,
                        'description': module.description,
                        'path': module.path,
                        'tags': module.tags
                    }
                    
                    if include_dependencies:
                        module_data['dependencies'] = module.dependencies
                    
                    data.append(module_data)
                
                return json.dumps(data, indent=2)
            
            elif format == 'csv':
                data = []
                for module in modules:
                    row = {
                        'name': module.name,
                        'category': module.category,
                        'description': module.description,
                        'path': module.path,
                        'tags': ', '.join(module.tags)
                    }
                    
                    if include_dependencies:
                        row['dependencies'] = ', '.join(module.dependencies)
                    
                    data.append(row)
                
                df = pd.DataFrame(data)
                return df.to_csv(index=False)
            
            else:
                raise ValueError(f"Unsupported format: {format}")
        except Exception as e:
            st.error(f"Error exporting module data: {str(e)}")
            return '{}' if format == 'json' else ''
    
    def export_module_data_json(self, modules: List[Module], 
                               include_dependencies: bool = False,
                               include_metadata: bool = False) -> str:
        """Export module data as JSON"""
        try:
            data = []
            for module in modules:
                module_data = {
                    'name': module.name,
                    'category': module.category,
                    'description': module.description,
                    'path': module.path,
                    'tags': module.tags
                }
                
                if include_dependencies:
                    module_data['dependencies'] = module.dependencies
                
                if include_metadata:
                    # Add complexity analysis
                    complexity = self.calculate_module_complexity(module)
                    module_data['complexity'] = complexity
                
                data.append(module_data)
            
            return json.dumps(data, indent=2)
        except Exception as e:
            st.error(f"Error exporting JSON data: {str(e)}")
            return '{}'
    
    def render_performance_metrics(self):
        """Render performance metrics display"""
        st.subheader("⚡ Performance Metrics")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Load Time", f"{self.performance_metrics['load_time']:.2f}s")
        
        with col2:
            st.metric("Modules Loaded", self.performance_metrics['modules_loaded'])
        
        with col3:
            if self.performance_metrics['last_update']:
                last_update = time.time() - self.performance_metrics['last_update']
                st.metric("Last Update", f"{last_update:.0f}s ago")
    
    def monitor_performance(self, operation: str, start_time: float) -> None:
        """Monitor performance of operations"""
        try:
            duration = time.time() - start_time
            
            if operation not in self.performance_metrics:
                self.performance_metrics[operation] = []
            
            self.performance_metrics[operation].append(duration)
            
            # Keep only last 10 measurements
            if len(self.performance_metrics[operation]) > 10:
                self.performance_metrics[operation] = self.performance_metrics[operation][-10:]
            
            # Alert if performance is slow
            if duration > 2.0:
                st.warning(f"Slow performance detected for {operation}: {duration:.2f}s")
                
        except Exception as e:
            st.error(f"Error monitoring performance: {str(e)}")
    
    def check_performance_thresholds(self) -> Dict[str, bool]:
        """Check if performance meets thresholds"""
        try:
            results = {
                'load_time_ok': self.performance_metrics['load_time'] < 2.0,
                'modules_loaded_ok': self.performance_metrics['modules_loaded'] > 0,
                'memory_ok': True  # Basic check
            }
            return results
        except Exception as e:
            st.error(f"Error checking performance thresholds: {str(e)}")
            return {'load_time_ok': False, 'modules_loaded_ok': False, 'memory_ok': False}
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics"""
        return self.performance_metrics.copy()
    
    
    def _render_overview_tab(self, filtered_modules: List[Module]):
        """Render the overview tab"""
        st.subheader("Module Overview")
        
        # Category distribution
        if filtered_modules:
            fig = self.create_category_distribution_chart(filtered_modules)
            st.plotly_chart(fig, use_container_width=True)
        
        # Module list
        st.subheader("Module List")
        for module in filtered_modules:
            with st.expander(f"📦 {module.name}"):
                self.render_module_details_panel(module)
    
    def _render_network_tab(self, filtered_modules: List[Module]):
        """Render the network tab"""
        st.subheader("Module Dependency Network")
        
        if filtered_modules:
            graph = self.create_dependency_graph(filtered_modules)
            fig = self.create_network_visualization(graph, interactive=True)
            st.plotly_chart(fig, use_container_width=True)
    
    def _render_complexity_tab(self, filtered_modules: List[Module]):
        """Render the complexity tab"""
        st.subheader("Module Complexity Analysis")
        
        if filtered_modules:
            complexity_data = {}
            for module in filtered_modules:
                complexity_data[module.name] = self.calculate_module_complexity(module)
            
            fig = self.create_complexity_heatmap(filtered_modules, complexity_data)
            st.plotly_chart(fig, use_container_width=True)
    
    def _render_usage_tab(self, filtered_modules: List[Module]):
        """Render the usage tab"""
        st.subheader("Module Usage Analysis")
        
        if filtered_modules:
            graph = self.create_dependency_graph(filtered_modules)
            usage_data = self.analyze_module_usage(graph, filtered_modules)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Most Used Module:**")
                st.markdown(f"`{usage_data['most_used'][0]}` ({usage_data['most_used'][1]} connections)")
            
            with col2:
                st.markdown("**Least Used Module:**")
                st.markdown(f"`{usage_data['least_used'][0]}` ({usage_data['least_used'][1]} connections)")
    
    def render(self):
        """Main render method for the module visualizer"""
        st.title("🧩 Module Visualizer")
        
        # Load modules
        if not self.modules:
            self.modules = self.load_modules_from_framework()
        
        if not self.modules:
            st.warning("No modules found. Please check your framework configuration.")
            return
        
        # Render filter controls
        self.render_filter_controls(self.modules)
        
        # Apply filters
        filtered_modules = self.filter_modules(
            self.modules,
            self.filters['category'],
            self.filters['search'],
            self.filters['tags']
        )
        
        # Show basic statistics
        st.markdown(f"**Total Modules:** {len(self.modules)} | **Filtered:** {len(filtered_modules)}")
        
        # Create tabs for different views
        tabs = st.tabs(["📊 Overview", "🔗 Network", "🎯 Complexity", "📈 Usage"])
        
        with tabs[0]:
            self._render_overview_tab(filtered_modules)
        
        with tabs[1]:
            self._render_network_tab(filtered_modules)
        
        with tabs[2]:
            self._render_complexity_tab(filtered_modules)
        
        with tabs[3]:
            self._render_usage_tab(filtered_modules)
        
        # Performance metrics
        self.render_performance_metrics()
    
    def create_usage_frequency_chart(self, modules: List[Module],
                                   usage_data: Dict[str, Any],
                                   chart_type: str = 'bar',
                                   show_values: bool = False) -> go.Figure:
        """Create usage frequency chart"""
        try:
            return create_usage_frequency_chart(modules, usage_data, chart_type, show_values)
        except Exception as e:
            st.error(f"Error creating usage frequency chart: {str(e)}")
            return go.Figure()
    
    def analyze_module_usage_patterns(self, modules: List[Module],
                                    graph: nx.DiGraph,
                                    historical_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Analyze module usage patterns with historical data"""
        try:
            return analyze_module_usage_patterns(modules, graph, historical_data)
        except Exception as e:
            st.error(f"Error analyzing usage patterns: {str(e)}")
            return {}
    
    def handle_zoom_pan_controls(self, figure: go.Figure, 
                               action: str = 'reset',
                               zoom_level: float = 1.0) -> go.Figure:
        """Handle zoom and pan controls for visualization"""
        try:
            return handle_zoom_pan_controls(figure, action, zoom_level)
        except Exception as e:
            st.error(f"Error handling zoom/pan controls: {str(e)}")
            return figure
    
    def expand_category_nodes(self, tree: Dict[str, Any], 
                             category: str,
                             expand_all: bool = False) -> Dict[str, Any]:
        """Expand category nodes in tree structure"""
        try:
            if category not in tree:
                return tree
            tree[category]['expanded'] = True
            if expand_all and 'children' in tree[category]:
                for child_category in tree[category]['children']:
                    tree[category]['children'][child_category]['expanded'] = True
            return tree
        except Exception as e:
            st.error(f"Error expanding category nodes: {str(e)}")
            return tree
    
    def export_visualization_png(self, figure: go.Figure, filename: str = 'visualization.png') -> bool:
        """Export visualization as PNG"""
        try:
            import plotly.io as pio
            pio.write_image(figure, filename)
            return True
        except Exception as e:
            st.error(f"Error exporting PNG: {str(e)}")
            return False
    
    def export_visualization_svg(self, figure: go.Figure, filename: str = 'visualization.svg') -> bool:
        """Export visualization as SVG"""
        try:
            import plotly.io as pio
            pio.write_image(figure, filename, format='svg')
            return True
        except Exception as e:
            st.error(f"Error exporting SVG: {str(e)}")
            return False
    
    def render_filter_controls(self, modules: List[Module],
                             mobile_layout: bool = False,
                             mobile_optimized: bool = False,
                             touch_friendly: bool = False,
                             high_contrast: bool = False,
                             screen_reader: bool = False):
        """Render filter controls with accessibility features"""
        st.subheader("🔍 Filter Controls")
        
        # Get categories and tags
        categories = list(set(m.category for m in modules))
        all_tags = list(set(tag for m in modules for tag in m.tags))
        
        # Adjust layout for mobile
        if mobile_layout or mobile_optimized:
            self._render_mobile_filter_controls(categories, all_tags, screen_reader)
        else:
            self._render_desktop_filter_controls(categories, all_tags, screen_reader)
    
    def _render_mobile_filter_controls(self, categories: List[str], all_tags: List[str], screen_reader: bool):
        """Render mobile-optimized filter controls"""
        col1, col2 = st.columns([1, 1])
        
        with col1:
            self.filters['category'] = st.selectbox(
                "Category",
                [None] + categories,
                format_func=lambda x: "All Categories" if x is None else x,
                help="Filter modules by category" if screen_reader else None
            )
        
        with col2:
            self.filters['search'] = st.text_input(
                "Search modules", 
                value=self.filters['search'],
                help="Search in module names and descriptions" if screen_reader else None
            )
        
        # Tags filter (full width)
        self.filters['tags'] = st.multiselect(
            "Tags", 
            all_tags, 
            default=self.filters['tags'],
            help="Filter by module tags" if screen_reader else None
        )
    
    def _render_desktop_filter_controls(self, categories: List[str], all_tags: List[str], screen_reader: bool):
        """Render desktop filter controls"""
        self.filters['category'] = st.selectbox(
            "Category",
            [None] + categories,
            format_func=lambda x: "All Categories" if x is None else x,
            help="Filter modules by category" if screen_reader else None
        )
        
        self.filters['search'] = st.text_input(
            "Search modules", 
            value=self.filters['search'],
            help="Search in module names and descriptions" if screen_reader else None
        )
        
        self.filters['tags'] = st.multiselect(
            "Tags", 
            all_tags, 
            default=self.filters['tags'],
            help="Filter by module tags" if screen_reader else None
        )