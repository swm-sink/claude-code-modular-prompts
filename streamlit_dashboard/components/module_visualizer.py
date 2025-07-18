"""
Prompt Component Explorer for Claude Code Framework Dashboard
Transform modules into interactive prompt building blocks for functional prompt engineering
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import json
import re
from dataclasses import dataclass, asdict


@dataclass
class PromptModule:
    """Represents a module as a prompt engineering component"""
    name: str
    category: str
    purpose: str
    prompt_interface: Dict[str, Any]
    inputs: List[str]
    outputs: List[str]
    usage_example: str
    composition_rules: List[str]
    effectiveness_score: float
    token_efficiency: float
    file_path: str


class PromptComponentExplorer:
    """Transform modules into interactive prompt building blocks"""
    
    def __init__(self, framework_path: Path):
        """Initialize Prompt Component Explorer"""
        self.framework_path = framework_path
        self.prompt_modules = self._discover_prompt_modules()
        self.selected_modules = []
        self.composition_workspace = []
        
    def _discover_prompt_modules(self) -> List[PromptModule]:
        """Discover and parse modules as prompt engineering components"""
        modules = []
        modules_dir = self.framework_path / "modules"
        
        if not modules_dir.exists():
            return modules
            
        for category_dir in modules_dir.iterdir():
            if category_dir.is_dir():
                for module_file in category_dir.glob("*.md"):
                    module = self._parse_module_as_prompt_component(module_file, category_dir.name)
                    if module:
                        modules.append(module)
                        
        return modules
    
    def _parse_module_as_prompt_component(self, module_path: Path, category: str) -> Optional[PromptModule]:
        """Parse module file as a prompt engineering component"""
        try:
            content = module_path.read_text()
            name = module_path.stem.replace('-', '_')
            
            # Extract prompt engineering interface
            purpose = self._extract_xml_content(content, 'purpose') or "Prompt engineering component"
            
            # Parse prompt interface
            prompt_interface = self._parse_prompt_interface(content)
            
            # Extract inputs/outputs for prompt composition
            inputs = self._extract_prompt_inputs(content)
            outputs = self._extract_prompt_outputs(content)
            
            # Generate usage example
            usage_example = self._generate_usage_example(name, purpose, inputs)
            
            # Extract composition rules
            composition_rules = self._extract_composition_rules(content)
            
            # Calculate effectiveness scores
            effectiveness_score = self._calculate_effectiveness_score(content, inputs, outputs)
            token_efficiency = self._calculate_token_efficiency(content, len(inputs))
            
            return PromptModule(
                name=name,
                category=category,
                purpose=purpose,
                prompt_interface=prompt_interface,
                inputs=inputs,
                outputs=outputs,
                usage_example=usage_example,
                composition_rules=composition_rules,
                effectiveness_score=effectiveness_score,
                token_efficiency=token_efficiency,
                file_path=str(module_path)
            )
            
        except Exception as e:
            st.warning(f"Could not parse module {module_path.name}: {str(e)}")
            return None
    
    def _extract_xml_content(self, content: str, tag: str) -> Optional[str]:
        """Extract content from XML tags"""
        pattern = f'<{tag}>(.*?)</{tag}>'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else None
    
    def _parse_prompt_interface(self, content: str) -> Dict[str, Any]:
        """Parse prompt interface from module content"""
        interface = {
            "trigger_conditions": [],
            "thinking_patterns": [],
            "execution_steps": [],
            "quality_gates": []
        }
        
        # Extract trigger conditions
        triggers = self._extract_xml_content(content, 'trigger_conditions')
        if triggers:
            interface["trigger_conditions"] = [t.strip() for t in triggers.split('\n') if t.strip()]
        
        # Extract thinking patterns
        thinking = self._extract_xml_content(content, 'thinking_pattern')
        if thinking:
            interface["thinking_patterns"] = [t.strip() for t in thinking.split('\n') if t.strip()]
        
        # Extract execution steps
        execution = self._extract_xml_content(content, 'execution')
        if execution:
            interface["execution_steps"] = [e.strip() for e in execution.split('\n') if e.strip()]
        
        return interface
    
    def _extract_prompt_inputs(self, content: str) -> List[str]:
        """Extract input requirements for prompt composition"""
        inputs = []
        
        # Look for common input patterns
        patterns = [
            r'requires?:?\s*([^\n]+)',
            r'input:?\s*([^\n]+)',
            r'parameter:?\s*([^\n]+)',
            r'expects?:?\s*([^\n]+)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            inputs.extend([match.strip() for match in matches])
        
        # Remove duplicates and clean up
        return list(set([inp for inp in inputs if inp and len(inp) < 100]))
    
    def _extract_prompt_outputs(self, content: str) -> List[str]:
        """Extract output capabilities for prompt composition"""
        outputs = []
        
        # Look for common output patterns
        patterns = [
            r'produces?:?\s*([^\n]+)',
            r'output:?\s*([^\n]+)',
            r'generates?:?\s*([^\n]+)',
            r'delivers?:?\s*([^\n]+)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            outputs.extend([match.strip() for match in matches])
        
        # Add default outputs based on category
        if 'tdd' in content.lower():
            outputs.append("Test-driven development workflow")
        if 'quality' in content.lower():
            outputs.append("Quality validation and enforcement")
        if 'thinking' in content.lower():
            outputs.append("Structured thinking patterns")
        
        return list(set([out for out in outputs if out and len(out) < 100]))
    
    def _generate_usage_example(self, name: str, purpose: str, inputs: List[str]) -> str:
        """Generate usage example for prompt composition"""
        example_parts = [
            f"# Using {name.replace('_', ' ').title()}",
            f"Purpose: {purpose}",
            ""
        ]
        
        if inputs:
            example_parts.append("Required inputs:")
            for inp in inputs[:3]:  # Limit to 3 inputs for brevity
                example_parts.append(f"- {inp}")
        
        example_parts.extend([
            "",
            f"Example usage in prompt composition:",
            f"1. Include {name} module",
            f"2. Provide required inputs",
            f"3. Execute module workflow",
            f"4. Use outputs for next composition step"
        ])
        
        return "\n".join(example_parts)
    
    def _extract_composition_rules(self, content: str) -> List[str]:
        """Extract rules for composing this module with others"""
        rules = []
        
        # Default composition rules based on content analysis
        if 'tdd' in content.lower():
            rules.append("Must be used before implementation modules")
            rules.append("Requires test framework setup")
        
        if 'quality' in content.lower():
            rules.append("Should be composed after implementation")
            rules.append("Can be combined with testing modules")
        
        if 'thinking' in content.lower():
            rules.append("Use at beginning of prompt composition")
            rules.append("Can enhance any workflow module")
        
        if 'session' in content.lower():
            rules.append("Manages state across module compositions")
            rules.append("Use when workflow spans multiple steps")
        
        return rules or ["Can be composed with most other modules"]
    
    def _calculate_effectiveness_score(self, content: str, inputs: List[str], outputs: List[str]) -> float:
        """Calculate effectiveness score for prompt engineering"""
        base_score = 0.7
        
        # Boost for clear structure
        if re.search(r'<\w+>', content):
            base_score += 0.1
        
        # Boost for thinking patterns
        if 'thinking' in content.lower() or 'pattern' in content.lower():
            base_score += 0.1
        
        # Boost for clear inputs/outputs
        if inputs and outputs:
            base_score += 0.1
        
        # Cap at 0.95
        return min(0.95, base_score)
    
    def _calculate_token_efficiency(self, content: str, input_complexity: int) -> float:
        """Calculate token efficiency for prompt composition"""
        base_efficiency = 0.8
        
        # Adjust for content length (shorter = more efficient)
        length_factor = max(0.5, 1.0 - len(content) / 8000)
        
        # Adjust for complexity (fewer inputs = more efficient)
        complexity_factor = max(0.6, 1.0 - input_complexity * 0.05)
        
        return min(0.98, base_efficiency * length_factor * complexity_factor)
    
    def render(self):
        """Render the Prompt Component Explorer interface"""
        st.title("🔧 Prompt Component Explorer")
        st.markdown("**Explore 64+ modules as interactive prompt building blocks**")
        
        if not self.prompt_modules:
            st.error("No modules found. Please check your framework configuration.")
            return
        
        # Create tabs for different exploration modes
        tab1, tab2, tab3, tab4 = st.tabs([
            "🧩 Component Library", 
            "🔍 Component Search",
            "🏗️ Composition Workspace",
            "📊 Usage Analytics"
        ])
        
        with tab1:
            self._render_component_library()
        
        with tab2:
            self._render_component_search()
        
        with tab3:
            self._render_composition_workspace()
        
        with tab4:
            self._render_usage_analytics()
    
    def _render_component_library(self):
        """Render the interactive component library"""
        st.subheader("📚 Component Library")
        st.write(f"**{len(self.prompt_modules)} modules available as prompt components**")
        
        # Enhanced filters and controls
        col1, col2, col3 = st.columns(3)
        with col1:
            categories = list(set(module.category for module in self.prompt_modules))
            selected_category = st.selectbox("Filter by Category", ["All"] + categories)
        
        with col2:
            sort_by = st.selectbox("Sort by", ["Name", "Effectiveness", "Token Efficiency", "Category"])
        
        with col3:
            view_type = st.selectbox("View Type", ["Grid", "List", "Dependency Graph"])
        
        # Filter modules
        filtered_modules = self.prompt_modules
        if selected_category != "All":
            filtered_modules = [m for m in filtered_modules if m.category == selected_category]
        
        # Sort modules
        if sort_by == "Effectiveness":
            filtered_modules.sort(key=lambda m: m.effectiveness_score, reverse=True)
        elif sort_by == "Token Efficiency":
            filtered_modules.sort(key=lambda m: m.token_efficiency, reverse=True)
        elif sort_by == "Category":
            filtered_modules.sort(key=lambda m: m.category)
        else:
            filtered_modules.sort(key=lambda m: m.name)
        
        # Display based on view type
        if view_type == "Dependency Graph":
            self._render_dependency_graph(filtered_modules)
        elif view_type == "List":
            self._render_component_list(filtered_modules)
        else:
            self._render_component_grid(filtered_modules)
    
    def _render_dependency_graph(self, modules: List[PromptModule]):
        """Render interactive dependency graph"""
        st.subheader("🕸️ Module Dependency Graph")
        
        # Create network graph
        import networkx as nx
        import plotly.graph_objects as go
        
        G = nx.Graph()
        
        # Add nodes
        for module in modules[:20]:  # Limit for performance
            G.add_node(module.name, 
                      category=module.category,
                      effectiveness=module.effectiveness_score,
                      efficiency=module.token_efficiency,
                      purpose=module.purpose[:50])
        
        # Add edges based on category relationships and composition rules
        for module in modules[:20]:
            for other_module in modules[:20]:
                if module != other_module:
                    # Connect modules with compatible categories
                    if self._check_module_compatibility(module, other_module):
                        G.add_edge(module.name, other_module.name)
        
        # Create layout
        pos = nx.spring_layout(G, k=3, iterations=50)
        
        # Create traces
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        edge_trace = go.Scatter(x=edge_x, y=edge_y,
                              line=dict(width=0.5, color='#888'),
                              hoverinfo='none',
                              mode='lines')
        
        node_x = []
        node_y = []
        node_text = []
        node_color = []
        node_size = []
        
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            
            # Find module data
            module_data = next((m for m in modules if m.name == node), None)
            if module_data:
                node_text.append(f"{node}<br>Category: {module_data.category}<br>Effectiveness: {module_data.effectiveness_score:.1%}")
                
                # Color by category
                category_colors = {
                    'patterns': '#FF6B6B',
                    'development': '#4ECDC4', 
                    'quality': '#45B7D1',
                    'security': '#96CEB4',
                    'system': '#FFEAA7',
                    'git': '#DDA0DD',
                    'meta': '#F8C291'
                }
                node_color.append(category_colors.get(module_data.category, '#BDC3C7'))
                
                # Size by effectiveness
                node_size.append(20 + module_data.effectiveness_score * 30)
        
        node_trace = go.Scatter(x=node_x, y=node_y,
                              mode='markers+text',
                              hoverinfo='text',
                              text=[name.replace('_', ' ').title() for name in G.nodes()],
                              textposition="middle center",
                              hovertext=node_text,
                              marker=dict(size=node_size,
                                        color=node_color,
                                        line=dict(width=2)))
        
        # Create figure
        fig = go.Figure(data=[edge_trace, node_trace],
                       layout=go.Layout(
                           title='Module Dependency Network',
                           titlefont_size=16,
                           showlegend=False,
                           hovermode='closest',
                           margin=dict(b=20,l=5,r=5,t=40),
                           annotations=[ dict(
                               text="Module relationships based on compatibility and composition rules",
                               showarrow=False,
                               xref="paper", yref="paper",
                               x=0.005, y=-0.002 ) ],
                           xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                           yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Add legend
        st.info("**Graph Legend**: Node size = effectiveness score, Colors = module categories, Connections = compatibility")
    
    def _check_module_compatibility(self, module1: PromptModule, module2: PromptModule) -> bool:
        """Check if two modules are compatible for composition"""
        # Compatible categories
        compatible_pairs = [
            ('patterns', 'development'),
            ('patterns', 'quality'),
            ('development', 'quality'),
            ('development', 'system'),
            ('quality', 'system'),
            ('security', 'development'),
            ('git', 'development'),
            ('meta', 'patterns')
        ]
        
        category_pair = (module1.category, module2.category)
        reverse_pair = (module2.category, module1.category)
        
        return category_pair in compatible_pairs or reverse_pair in compatible_pairs
    
    def _render_component_list(self, modules: List[PromptModule]):
        """Render components in enhanced list view"""
        st.subheader("📋 Component List View")
        
        for module in modules[:20]:  # Limit for performance
            with st.expander(f"🧩 {module.name.replace('_', ' ').title()}", expanded=False):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.write(f"**Category:** {module.category}")
                    st.write(f"**Purpose:** {module.purpose}")
                    
                    # Progress bars for metrics
                    st.write("**Effectiveness:**")
                    st.progress(module.effectiveness_score)
                    st.write(f"{module.effectiveness_score:.1%}")
                    
                    st.write("**Token Efficiency:**")
                    st.progress(module.token_efficiency)
                    st.write(f"{module.token_efficiency:.1%}")
                
                with col2:
                    # Action buttons
                    if st.button(f"🔍 Analyze", key=f"analyze_{module.name}"):
                        self._show_module_analysis(module)
                    
                    if st.button(f"➕ Add to Workspace", key=f"add_list_{module.name}"):
                        if module not in self.composition_workspace:
                            self.composition_workspace.append(module)
                            st.success(f"Added {module.name}!")
                            st.rerun()
                    
                    if st.button(f"🔗 Find Compatible", key=f"compat_{module.name}"):
                        compatible = self._find_compatible_modules(module)
                        if compatible:
                            st.info(f"Compatible with: {', '.join([m.name for m in compatible[:3]])}")
    
    def _render_component_grid(self, modules: List[PromptModule]):
        """Render components in enhanced grid view"""
        st.subheader("🎯 Component Grid View")
        
        # Display modules in grid with enhanced cards
        cols = st.columns(3)
        for i, module in enumerate(modules[:15]):  # Limit for performance
            with cols[i % 3]:
                self._render_enhanced_component_card(module)
    
    def _render_enhanced_component_card(self, module: PromptModule):
        """Render enhanced component card with visual improvements"""
        # Create card with better styling
        card_style = f"""
        <div style="
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        ">
            <h4 style="margin: 0 0 10px 0; color: #2c3e50;">
                🧩 {module.name.replace('_', ' ').title()}
            </h4>
            <p style="margin: 5px 0; color: #7f8c8d;">
                <strong>Category:</strong> {module.category}
            </p>
            <p style="margin: 5px 0; color: #34495e; font-size: 0.9em;">
                {module.purpose[:80]}...
            </p>
        </div>
        """
        
        st.markdown(card_style, unsafe_allow_html=True)
        
        # Metrics with visual indicators
        col1, col2 = st.columns(2)
        with col1:
            effectiveness_color = "green" if module.effectiveness_score > 0.8 else "orange" if module.effectiveness_score > 0.6 else "red"
            st.metric("Effectiveness", f"{module.effectiveness_score:.1%}", 
                     delta=f"{(module.effectiveness_score - 0.7):.1%}", 
                     delta_color=effectiveness_color)
        
        with col2:
            efficiency_color = "green" if module.token_efficiency > 0.8 else "orange" if module.token_efficiency > 0.6 else "red"
            st.metric("Token Efficiency", f"{module.token_efficiency:.1%}",
                     delta=f"{(module.token_efficiency - 0.7):.1%}",
                     delta_color=efficiency_color)
        
        # Enhanced action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"📋 Details", key=f"details_{module.name}", type="secondary"):
                st.session_state[f"show_details_{module.name}"] = True
        
        with col2:
            if st.button(f"➕ Add", key=f"add_{module.name}", type="primary"):
                if module not in self.composition_workspace:
                    self.composition_workspace.append(module)
                    st.success(f"Added {module.name}!")
                    st.rerun()
                else:
                    st.info("Already in workspace")
        
        # Enhanced details view
        if st.session_state.get(f"show_details_{module.name}", False):
            with st.expander(f"📋 {module.name} Details", expanded=True):
                
                # Tabs for different detail views
                detail_tab1, detail_tab2, detail_tab3 = st.tabs(["📖 Usage", "🔧 Technical", "🔗 Compatibility"])
                
                with detail_tab1:
                    st.code(module.usage_example, language="markdown")
                
                with detail_tab2:
                    st.write("**Inputs:**")
                    for inp in module.inputs:
                        st.write(f"• {inp}")
                    
                    st.write("**Outputs:**")
                    for out in module.outputs:
                        st.write(f"• {out}")
                    
                    st.write("**Composition Rules:**")
                    for rule in module.composition_rules:
                        st.write(f"• {rule}")
                
                with detail_tab3:
                    compatible = self._find_compatible_modules(module)
                    if compatible:
                        st.write("**Compatible Modules:**")
                        for comp in compatible[:5]:
                            st.write(f"• {comp.name} ({comp.category})")
                    else:
                        st.write("No specific compatibility requirements")
                
                if st.button(f"✖️ Close", key=f"close_{module.name}"):
                    st.session_state[f"show_details_{module.name}"] = False
                    st.rerun()
    
    def _find_compatible_modules(self, module: PromptModule) -> List[PromptModule]:
        """Find modules compatible with the given module"""
        compatible = []
        for other_module in self.prompt_modules:
            if other_module != module and self._check_module_compatibility(module, other_module):
                compatible.append(other_module)
        return compatible
    
    def _show_module_analysis(self, module: PromptModule):
        """Show detailed analysis of a module"""
        st.subheader(f"🔍 Analysis: {module.name}")
        
        # Create analysis metrics
        analysis_data = {
            'Metric': ['Effectiveness', 'Token Efficiency', 'Complexity', 'Reusability'],
            'Score': [
                module.effectiveness_score,
                module.token_efficiency,
                min(1.0, len(module.inputs) * 0.2),  # Complexity based on inputs
                min(1.0, len(module.outputs) * 0.15)  # Reusability based on outputs
            ]
        }
        
        fig = px.bar(analysis_data, x='Metric', y='Score', 
                     title=f"{module.name} Analysis",
                     color='Score',
                     color_continuous_scale='Viridis')
        
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_component_card(self, module: PromptModule):
        """Render individual component card"""
        with st.container():
            st.markdown(f"### 🧩 {module.name.replace('_', ' ').title()}")
            st.write(f"**Category:** {module.category}")
            st.write(f"**Purpose:** {module.purpose[:100]}...")
            
            # Effectiveness metrics
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Effectiveness", f"{module.effectiveness_score:.1%}")
            with col2:
                st.metric("Token Efficiency", f"{module.token_efficiency:.1%}")
            
            # Inputs/Outputs
            if module.inputs:
                st.write(f"**Inputs:** {', '.join(module.inputs[:2])}...")
            if module.outputs:
                st.write(f"**Outputs:** {', '.join(module.outputs[:2])}...")
            
            # Action buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"📋 Details", key=f"details_{module.name}"):
                    st.session_state[f"show_details_{module.name}"] = True
            with col2:
                if st.button(f"➕ Add to Workspace", key=f"add_{module.name}"):
                    if module not in self.composition_workspace:
                        self.composition_workspace.append(module)
                        st.success(f"Added {module.name} to workspace!")
                        st.rerun()
            
            # Show details if requested
            if st.session_state.get(f"show_details_{module.name}", False):
                with st.expander(f"📋 {module.name} Details", expanded=True):
                    st.code(module.usage_example, language="markdown")
                    st.write("**Composition Rules:**")
                    for rule in module.composition_rules:
                        st.write(f"• {rule}")
                    if st.button(f"✖️ Close", key=f"close_{module.name}"):
                        st.session_state[f"show_details_{module.name}"] = False
                        st.rerun()
    
    def _render_component_search(self):
        """Render component search interface"""
        st.subheader("🔍 Intelligent Component Search")
        
        # Search controls
        col1, col2 = st.columns([3, 1])
        with col1:
            search_query = st.text_input("Search components by purpose, inputs, outputs...", 
                                       placeholder="e.g., 'testing', 'quality', 'thinking patterns'")
        with col2:
            search_type = st.selectbox("Search in", ["All", "Purpose", "Inputs", "Outputs"])
        
        if search_query:
            results = self._search_components(search_query, search_type)
            st.write(f"**Found {len(results)} matching components:**")
            
            for module in results:
                with st.expander(f"🧩 {module.name.replace('_', ' ').title()}", expanded=False):
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.write(f"**Purpose:** {module.purpose}")
                        st.write(f"**Category:** {module.category}")
                        if module.inputs:
                            st.write(f"**Inputs:** {', '.join(module.inputs)}")
                        if module.outputs:
                            st.write(f"**Outputs:** {', '.join(module.outputs)}")
                    with col2:
                        st.metric("Effectiveness", f"{module.effectiveness_score:.1%}")
                        st.metric("Token Efficiency", f"{module.token_efficiency:.1%}")
                        if st.button(f"➕ Add", key=f"search_add_{module.name}"):
                            if module not in self.composition_workspace:
                                self.composition_workspace.append(module)
                                st.success(f"Added {module.name}!")
                                st.rerun()
    
    def _search_components(self, query: str, search_type: str) -> List[PromptModule]:
        """Search components based on query and type"""
        query_lower = query.lower()
        results = []
        
        for module in self.prompt_modules:
            if search_type == "All":
                if (query_lower in module.purpose.lower() or 
                    any(query_lower in inp.lower() for inp in module.inputs) or
                    any(query_lower in out.lower() for out in module.outputs) or
                    query_lower in module.name.lower()):
                    results.append(module)
            elif search_type == "Purpose" and query_lower in module.purpose.lower():
                results.append(module)
            elif search_type == "Inputs" and any(query_lower in inp.lower() for inp in module.inputs):
                results.append(module)
            elif search_type == "Outputs" and any(query_lower in out.lower() for out in module.outputs):
                results.append(module)
        
        return results
    
    def _render_composition_workspace(self):
        """Render the composition workspace"""
        st.subheader("🏗️ Composition Workspace")
        
        if not self.composition_workspace:
            st.info("Add components from the library to start building your prompt composition")
            return
        
        st.write(f"**{len(self.composition_workspace)} components in workspace**")
        
        # Workspace controls
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔗 Analyze Composition"):
                self._analyze_composition()
        with col2:
            if st.button("🚀 Generate Prompt"):
                self._generate_prompt_from_composition()
        with col3:
            if st.button("🗑️ Clear Workspace"):
                self.composition_workspace = []
                st.rerun()
        
        # Display workspace components
        for i, module in enumerate(self.composition_workspace):
            with st.expander(f"{i+1}. {module.name.replace('_', ' ').title()}", expanded=False):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**Purpose:** {module.purpose}")
                    st.write(f"**Category:** {module.category}")
                    if module.composition_rules:
                        st.write("**Composition Rules:**")
                        for rule in module.composition_rules[:2]:
                            st.write(f"• {rule}")
                with col2:
                    if st.button(f"⬆️", key=f"up_{i}", disabled=i==0):
                        self.composition_workspace[i], self.composition_workspace[i-1] = \
                            self.composition_workspace[i-1], self.composition_workspace[i]
                        st.rerun()
                    if st.button(f"⬇️", key=f"down_{i}", disabled=i==len(self.composition_workspace)-1):
                        self.composition_workspace[i], self.composition_workspace[i+1] = \
                            self.composition_workspace[i+1], self.composition_workspace[i]
                        st.rerun()
                    if st.button(f"❌", key=f"remove_{i}"):
                        self.composition_workspace.pop(i)
                        st.rerun()
    
    def _analyze_composition(self):
        """Analyze the current composition for compatibility and effectiveness"""
        st.subheader("🔍 Composition Analysis")
        
        if len(self.composition_workspace) < 2:
            st.warning("Add at least 2 components to analyze composition")
            return
        
        # Calculate composition metrics
        avg_effectiveness = sum(m.effectiveness_score for m in self.composition_workspace) / len(self.composition_workspace)
        avg_efficiency = sum(m.token_efficiency for m in self.composition_workspace) / len(self.composition_workspace)
        
        # Display metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Composition Effectiveness", f"{avg_effectiveness:.1%}")
        with col2:
            st.metric("Token Efficiency", f"{avg_efficiency:.1%}")
        with col3:
            st.metric("Components", len(self.composition_workspace))
        
        # Composition recommendations
        st.write("**🎯 Composition Recommendations:**")
        recommendations = self._generate_composition_recommendations()
        for rec in recommendations:
            st.write(f"• {rec}")
    
    def _generate_composition_recommendations(self) -> List[str]:
        """Generate recommendations for improving the composition"""
        recommendations = []
        
        categories = [m.category for m in self.composition_workspace]
        
        # Check for missing thinking patterns
        if 'patterns' not in categories:
            recommendations.append("Consider adding a thinking pattern module for better structure")
        
        # Check for TDD workflow
        if any('implement' in m.purpose.lower() for m in self.composition_workspace):
            if not any('tdd' in m.name.lower() for m in self.composition_workspace):
                recommendations.append("Add TDD cycle pattern before implementation")
        
        # Check for quality gates
        if len(self.composition_workspace) > 3:
            if not any('quality' in m.purpose.lower() for m in self.composition_workspace):
                recommendations.append("Include quality validation for complex compositions")
        
        return recommendations or ["Composition looks well-balanced!"]
    
    def _generate_prompt_from_composition(self):
        """Generate a functional, executable prompt from the composition"""
        st.subheader("🚀 Generated Functional Prompt")
        
        if not self.composition_workspace:
            st.warning("Add components to workspace first")
            return
        
        # Analyze composition for module types and dependencies
        analysis = self._analyze_composition_for_execution()
        
        # Build executable prompt using module composition framework
        prompt_parts = [
            "# Executable Prompt Composition",
            "",
            "```xml",
            "<claude_4_module_execution enforcement=\"MANDATORY\" thinking_mode=\"interleaved\">",
            ""
        ]
        
        # Add core modules (sequential execution)
        core_modules = [m for m in self.composition_workspace if m.category in ['patterns', 'quality']]
        if core_modules:
            prompt_parts.extend([
                "  <core_stack order=\"advanced_sequential\" optimization=\"context_hierarchical\">",
                "    <!-- Critical modules requiring sequential execution -->"
            ])
            for module in core_modules:
                trigger_conditions = self._extract_module_triggers(module)
                prompt_parts.append(f"    <module thinking=\"enabled\" cache=\"predictive\">{module.file_path} - {module.purpose}</module>")
                if trigger_conditions:
                    prompt_parts.append(f"    <!-- Triggers: {', '.join(trigger_conditions[:2])} -->")
            prompt_parts.append("  </core_stack>")
            prompt_parts.append("")
        
        # Add contextual modules (conditional execution)  
        contextual_modules = [m for m in self.composition_workspace if m.category in ['development', 'security']]
        if contextual_modules:
            prompt_parts.extend([
                "  <contextual_modules evaluation=\"intelligent_conditional\" analysis=\"claude_4_enhanced\">",
                "    <!-- Context-dependent modules loaded based on conditions -->"
            ])
            for module in contextual_modules:
                conditions = self._generate_execution_conditions(module)
                prompt_parts.append(f"    <conditional module=\"{module.file_path}\" condition=\"{conditions}\" thinking=\"adaptive\"/>")
            prompt_parts.append("  </contextual_modules>")
            prompt_parts.append("")
        
        # Add support modules (parallel execution)
        support_modules = [m for m in self.composition_workspace if m.category in ['system', 'git']]
        if support_modules:
            prompt_parts.extend([
                "  <support_modules order=\"optimized_parallel\" batching=\"mandatory\" speedup=\"70_percent\">",
                "    <!-- Support modules executed in parallel for efficiency -->"
            ])
            for module in support_modules:
                batch_group = "validation" if "quality" in module.purpose.lower() else "analysis"
                prompt_parts.append(f"    <module batch_group=\"{batch_group}\">{module.file_path} - {module.purpose}</module>")
            prompt_parts.append("  </support_modules>")
            prompt_parts.append("")
        
        # Add execution workflow with real module integration
        prompt_parts.extend([
            "  <execution_workflow>",
            "    <phase name=\"discovery\" order=\"1\">",
            f"      <requirements>Validate {len(self.composition_workspace)} modules are available and compatible</requirements>",
            "      <action>Build dependency graph and execution order</action>", 
            "    </phase>",
            "    <phase name=\"loading\" order=\"2\">",
            "      <requirements>Load modules in dependency order with interface validation</requirements>",
            "      <action>Initialize module contexts and verify input contracts</action>",
            "    </phase>", 
            "    <phase name=\"orchestration\" order=\"3\">",
            "      <requirements>Execute modules with state management and quality gates</requirements>",
            "      <action>Coordinate module execution with parallel optimization</action>",
            "    </phase>",
            "    <phase name=\"integration\" order=\"4\">", 
            "      <requirements>Integrate results with consistency validation</requirements>",
            "      <action>Consolidate outputs and apply post-execution quality gates</action>",
            "    </phase>",
            "  </execution_workflow>",
            ""
        ])
        
        # Add quality gates from modules
        quality_gates = self._extract_quality_gates_from_composition()
        if quality_gates:
            prompt_parts.extend([
                "  <quality_gates>",
                "    <!-- Extracted from composed modules -->"
            ])
            for gate in quality_gates:
                prompt_parts.append(f"    <gate name=\"{gate['name']}\" severity=\"{gate['severity']}\">{gate['description']}</gate>")
            prompt_parts.append("  </quality_gates>")
            prompt_parts.append("")
        
        # Add thinking patterns integration
        thinking_patterns = self._extract_thinking_patterns_from_composition()
        if thinking_patterns:
            prompt_parts.extend([
                "  <thinking_integration>",
                "    <mode>interleaved</mode>",
                f"    <patterns>{', '.join(thinking_patterns)}</patterns>",
                "    <triggers>complex_dependencies, error_conditions, quality_validation</triggers>",
                "  </thinking_integration>",
                ""
            ])
        
        # Add performance monitoring
        avg_effectiveness = sum(m.effectiveness_score for m in self.composition_workspace) / len(self.composition_workspace)
        avg_efficiency = sum(m.token_efficiency for m in self.composition_workspace) / len(self.composition_workspace)
        
        prompt_parts.extend([
            "  <performance_monitoring>",
            f"    <metric name=\"composition_effectiveness\" target=\"{avg_effectiveness:.1%}\"/>",
            f"    <metric name=\"token_efficiency\" target=\"{avg_efficiency:.1%}\"/>",
            "    <metric name=\"execution_time\" target=\"70_percent_improvement\"/>",
            "  </performance_monitoring>",
            "",
            "</claude_4_module_execution>",
            "```",
            "",
            "## Execution Instructions",
            "",
            "This prompt composition implements the Claude Code framework's module composition pattern:",
            "",
            f"1. **Core Stack** ({len(core_modules)} modules): Sequential execution with thinking integration",
            f"2. **Contextual Modules** ({len(contextual_modules)} modules): Conditional based on context analysis", 
            f"3. **Support Modules** ({len(support_modules)} modules): Parallel execution with tool batching",
            "",
            "### Quality Enforcement",
            ""
        ])
        
        if 'tdd_cycle_pattern' in [m.name for m in self.composition_workspace]:
            prompt_parts.extend([
                "- **TDD Enforcement**: RED→GREEN→REFACTOR cycle with atomic commits",
                "- **Coverage Requirements**: 90% line coverage, 85% branch coverage",
                "- **Quality Gates**: Blocking enforcement on TDD violations"
            ])
        
        prompt_parts.extend([
            "",
            "### Expected Outputs",
            ""
        ])
        
        for module in self.composition_workspace:
            if module.outputs:
                prompt_parts.append(f"- **{module.name}**: {', '.join(module.outputs[:2])}")
        
        prompt_parts.extend([
            "",
            f"### Composition Effectiveness: {avg_effectiveness:.1%}",
            f"### Token Efficiency: {avg_efficiency:.1%}",
            "",
            "This prompt is ready for execution with Claude Code framework."
        ])
        
        generated_prompt = "\n".join(prompt_parts)
        st.code(generated_prompt, language="markdown")
        
        # Validation feedback
        validation_results = self._validate_prompt_composition(analysis)
        if validation_results['issues']:
            st.warning("**Composition Issues Detected:**")
            for issue in validation_results['issues']:
                st.write(f"⚠️ {issue}")
        
        if validation_results['recommendations']:
            st.info("**Optimization Recommendations:**")
            for rec in validation_results['recommendations']:
                st.write(f"💡 {rec}")
        
        # Download button with metadata
        metadata = {
            "composition_analysis": analysis,
            "effectiveness_score": avg_effectiveness,
            "token_efficiency": avg_efficiency,
            "modules_count": len(self.composition_workspace),
            "quality_gates": len(quality_gates)
        }
        
        st.download_button(
            label="📥 Download Executable Prompt",
            data=generated_prompt,
            file_name=f"executable_prompt_{len(self.composition_workspace)}_modules.md",
            mime="text/markdown"
        )
        
        # Show metadata
        with st.expander("📊 Composition Metadata", expanded=False):
            st.json(metadata)
    
    def _analyze_composition_for_execution(self) -> Dict[str, Any]:
        """Analyze composition for executable prompt generation"""
        analysis = {
            "total_modules": len(self.composition_workspace),
            "core_modules": [m for m in self.composition_workspace if m.category in ['patterns', 'quality']],
            "contextual_modules": [m for m in self.composition_workspace if m.category in ['development', 'security']],
            "support_modules": [m for m in self.composition_workspace if m.category in ['system', 'git']],
            "has_tdd": any('tdd' in m.name.lower() for m in self.composition_workspace),
            "has_thinking": any('thinking' in m.name.lower() for m in self.composition_workspace),
            "has_quality": any('quality' in m.purpose.lower() for m in self.composition_workspace),
            "execution_complexity": "high" if len(self.composition_workspace) > 5 else "medium" if len(self.composition_workspace) > 2 else "simple"
        }
        return analysis
    
    def _extract_module_triggers(self, module: PromptModule) -> List[str]:
        """Extract trigger conditions from module file content"""
        try:
            # Read actual module file to extract trigger conditions
            module_path = Path(module.file_path)
            if module_path.exists():
                content = module_path.read_text()
                # Extract trigger conditions from XML
                pattern = r'<trigger_conditions>(.*?)</trigger_conditions>'
                match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
                if match:
                    triggers_text = match.group(1)
                    # Extract individual conditions
                    condition_pattern = r'<condition[^>]*>(.*?)</condition>'
                    conditions = re.findall(condition_pattern, triggers_text, re.DOTALL | re.IGNORECASE)
                    return [cond.strip() for cond in conditions if cond.strip()]
        except Exception:
            pass
        
        # Fallback to default triggers based on module properties
        default_triggers = []
        if 'tdd' in module.name.lower():
            default_triggers.append("Any code implementation task")
        if 'quality' in module.purpose.lower():
            default_triggers.append("Quality validation required")
        if 'thinking' in module.name.lower():
            default_triggers.append("Complex analysis needed")
        
        return default_triggers or ["Module composition context"]
    
    def _generate_execution_conditions(self, module: PromptModule) -> str:
        """Generate intelligent execution conditions for contextual modules"""
        conditions = []
        
        # Module-specific conditions
        if 'security' in module.category:
            conditions.append("security_implications_detected")
        if 'development' in module.category:
            conditions.append("implementation_required")
        if 'multi' in module.name.lower():
            conditions.append("multi_component_coordination_needed")
        if 'error' in module.purpose.lower():
            conditions.append("failures_or_issues_occur")
        
        # Default condition based on module purpose
        if not conditions:
            if 'test' in module.purpose.lower():
                conditions.append("testing_required")
            elif 'analysis' in module.purpose.lower():
                conditions.append("analysis_needed")
            else:
                conditions.append("context_appropriate")
        
        return " OR ".join(conditions)
    
    def _extract_quality_gates_from_composition(self) -> List[Dict[str, str]]:
        """Extract quality gates from composed modules"""
        quality_gates = []
        
        for module in self.composition_workspace:
            try:
                # Read actual module file to extract quality gates
                module_path = Path(module.file_path)
                if module_path.exists():
                    content = module_path.read_text()
                    # Extract quality gates from XML
                    pattern = r'<quality_gates>(.*?)</quality_gates>'
                    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
                    if match:
                        gates_text = match.group(1)
                        # Extract individual gates
                        gate_pattern = r'<gate[^>]*name="([^"]*)"[^>]*severity="([^"]*)"[^>]*>(.*?)</gate>'
                        gates = re.findall(gate_pattern, gates_text, re.DOTALL | re.IGNORECASE)
                        for name, severity, description in gates:
                            quality_gates.append({
                                "name": name.strip(),
                                "severity": severity.strip(),
                                "description": description.strip(),
                                "source_module": module.name
                            })
            except Exception:
                continue
        
        # Add default quality gates for known module types
        if any('tdd' in m.name.lower() for m in self.composition_workspace):
            quality_gates.append({
                "name": "tdd_enforcement",
                "severity": "blocking", 
                "description": "Tests must be written before implementation",
                "source_module": "tdd_cycle_pattern"
            })
        
        if any('quality' in m.purpose.lower() for m in self.composition_workspace):
            quality_gates.append({
                "name": "coverage_requirements",
                "severity": "blocking",
                "description": "90% line coverage minimum required", 
                "source_module": "quality_validation"
            })
        
        return quality_gates
    
    def _extract_thinking_patterns_from_composition(self) -> List[str]:
        """Extract thinking patterns from composed modules"""
        thinking_patterns = []
        
        for module in self.composition_workspace:
            try:
                # Read actual module file to extract thinking patterns
                module_path = Path(module.file_path)
                if module_path.exists():
                    content = module_path.read_text()
                    # Extract thinking patterns from XML
                    pattern = r'<thinking_pattern>(.*?)</thinking_pattern>'
                    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
                    if match:
                        thinking_text = match.group(1)
                        # Extract pattern steps or components
                        thinking_patterns.extend([line.strip() for line in thinking_text.split('\n') if line.strip()])
            except Exception:
                continue
        
        # Add default patterns based on module types
        if any('critical' in m.name.lower() for m in self.composition_workspace):
            thinking_patterns.append("critical_thinking_analysis")
        if any('tdd' in m.name.lower() for m in self.composition_workspace):
            thinking_patterns.append("test_driven_reasoning")
        if any('quality' in m.purpose.lower() for m in self.composition_workspace):
            thinking_patterns.append("quality_validation_thinking")
        
        return list(set(thinking_patterns))  # Remove duplicates
    
    def _validate_prompt_composition(self, analysis: Dict[str, Any]) -> Dict[str, List[str]]:
        """Validate prompt composition and provide feedback"""
        issues = []
        recommendations = []
        
        # Check for missing essential modules
        if not analysis["has_thinking"]:
            issues.append("No thinking pattern module detected - composition may lack structured analysis")
        
        if analysis["has_tdd"] and not analysis["has_quality"]:
            issues.append("TDD module present but no quality validation - may lack proper enforcement")
        
        if analysis["total_modules"] > 8:
            issues.append("Large composition (>8 modules) may impact token efficiency")
        
        # Generate recommendations
        if analysis["execution_complexity"] == "high":
            recommendations.append("Consider parallel execution optimization for support modules")
        
        if not analysis["has_tdd"] and len(analysis["core_modules"]) > 1:
            recommendations.append("Add TDD cycle pattern for quality-driven development")
        
        if analysis["total_modules"] > 3 and len(analysis["support_modules"]) == 0:
            recommendations.append("Add support modules for enhanced functionality")
        
        return {
            "issues": issues,
            "recommendations": recommendations
        }
    
    def _render_usage_analytics(self):
        """Render usage analytics and insights"""
        st.subheader("📊 Component Usage Analytics")
        
        # Category distribution
        category_counts = {}
        for module in self.prompt_modules:
            category_counts[module.category] = category_counts.get(module.category, 0) + 1
        
        # Create pie chart
        fig_pie = px.pie(
            values=list(category_counts.values()),
            names=list(category_counts.keys()),
            title="Components by Category"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
        # Effectiveness distribution
        effectiveness_data = [m.effectiveness_score for m in self.prompt_modules]
        fig_hist = px.histogram(
            x=effectiveness_data,
            title="Effectiveness Score Distribution",
            nbins=10
        )
        st.plotly_chart(fig_hist, use_container_width=True)
        
        # Top performing components
        st.subheader("🏆 Top Performing Components")
        top_modules = sorted(self.prompt_modules, key=lambda m: m.effectiveness_score, reverse=True)[:5]
        
        for i, module in enumerate(top_modules, 1):
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.write(f"#{i}")
            with col2:
                st.write(f"**{module.name.replace('_', ' ').title()}**")
                st.write(f"{module.category} - {module.purpose[:50]}...")
            with col3:
                st.metric("Score", f"{module.effectiveness_score:.1%}")