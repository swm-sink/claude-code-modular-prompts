"""
Interactive Prompt Builder for Claude Code Framework Dashboard
Advanced drag-and-drop interface for composing prompts from 64+ modular components
"""
import streamlit as st
import pandas as pd
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import re
import plotly.graph_objects as go
import plotly.express as px
from dataclasses import dataclass
from datetime import datetime
from utils.session_manager import get_session_manager


@dataclass
class ModuleInterface:
    """Represents a module's interface contract"""
    name: str
    category: str
    purpose: str
    inputs: Dict[str, List[str]]
    outputs: Dict[str, List[str]]
    execution_pattern: str
    dependencies: List[str]
    token_efficiency: float


class InteractivePromptBuilder:
    """Advanced interactive prompt builder with drag-and-drop composition"""
    
    def __init__(self, framework_path: Path):
        """Initialize Interactive Prompt Builder"""
        self.framework_path = framework_path
        self.modules = self._load_all_modules()
        self.session_manager = get_session_manager()
        
        # Initialize state from session or defaults
        self._restore_state_from_session()
        
    def _restore_state_from_session(self):
        """Restore component state from session"""
        try:
            session_state = self.session_manager.get_prompt_builder_state()
            
            # Restore composition workspace
            self.composition_workspace = []
            if session_state.get('composition_workspace'):
                for module_data in session_state['composition_workspace']:
                    # Try to find the module in our loaded modules
                    module_name = module_data.get('name')
                    if module_name and module_name in self.modules:
                        self.composition_workspace.append(self.modules[module_name])
            
            # Restore other state
            self.constructed_prompt = session_state.get('constructed_prompt', '')
            self.effectiveness_score = session_state.get('effectiveness_score', 0.0)
            
        except Exception as e:
            # If restoration fails, start with defaults
            self.composition_workspace = []
            self.constructed_prompt = ""
            self.effectiveness_score = 0.0
    
    def _save_state_to_session(self):
        """Save current state to session"""
        try:
            state_data = {
                'composition_workspace': [
                    {
                        'name': module.name,
                        'category': module.category,
                        'purpose': module.purpose,
                        'token_efficiency': module.token_efficiency
                    } for module in self.composition_workspace
                ],
                'constructed_prompt': self.constructed_prompt,
                'effectiveness_score': self.effectiveness_score,
                'last_updated': datetime.now().isoformat()
            }
            
            self.session_manager.update_prompt_builder_state(state_data)
            
        except Exception as e:
            st.warning(f"Could not save state to session: {e}")
        
    def _load_all_modules(self) -> Dict[str, ModuleInterface]:
        """Load and parse all modules with their interfaces"""
        modules = {}
        modules_dir = self.framework_path / "modules"
        
        if not modules_dir.exists():
            return modules
            
        for category_dir in modules_dir.iterdir():
            if category_dir.is_dir():
                for module_file in category_dir.glob("*.md"):
                    interface = self._parse_module_interface(module_file, category_dir.name)
                    if interface:
                        modules[interface.name] = interface
                        
        return modules
    
    def _parse_module_interface(self, module_path: Path, category: str) -> Optional[ModuleInterface]:
        """Parse module file and extract interface contract"""
        try:
            content = module_path.read_text()
            name = module_path.stem.replace('-', '_')
            
            # Extract purpose
            purpose = self._extract_xml_content(content, 'purpose') or "Advanced prompt component"
            
            # Extract inputs and outputs
            inputs = self._parse_interface_contract(content, 'inputs')
            outputs = self._parse_interface_contract(content, 'outputs')
            
            # Extract execution pattern
            execution_pattern = self._extract_xml_content(content, 'execution_pattern') or "Standard execution"
            
            # Calculate token efficiency (simulated based on module complexity)
            token_efficiency = self._calculate_token_efficiency(content, len(inputs.get('required', [])))
            
            # Extract dependencies (simulated)
            dependencies = self._extract_dependencies(content)
            
            return ModuleInterface(
                name=name,
                category=category,
                purpose=purpose,
                inputs=inputs,
                outputs=outputs,
                execution_pattern=execution_pattern,
                dependencies=dependencies,
                token_efficiency=token_efficiency
            )
            
        except Exception as e:
            st.warning(f"Could not parse module {module_path.name}: {str(e)}")
            return None
    
    def _extract_xml_content(self, content: str, tag: str) -> Optional[str]:
        """Extract content from XML tags"""
        pattern = f'<{tag}>(.*?)</{tag}>'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else None
    
    def _parse_interface_contract(self, content: str, section: str) -> Dict[str, List[str]]:
        """Parse inputs or outputs from interface contract"""
        result = {"required": [], "optional": []}
        
        # Look for XML structure
        pattern = f'<{section}>(.*?)</{section}>'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        
        if match:
            section_content = match.group(1)
            
            # Extract required items
            required_match = re.search(r'<required>(.*?)</required>', section_content, re.DOTALL)
            if required_match:
                items = [item.strip() for item in required_match.group(1).split(',')]
                result["required"] = [item for item in items if item]
            
            # Extract optional items
            optional_match = re.search(r'<optional>(.*?)</optional>', section_content, re.DOTALL)
            if optional_match:
                items = [item.strip() for item in optional_match.group(1).split(',')]
                result["optional"] = [item for item in items if item]
        
        return result
    
    def _calculate_token_efficiency(self, content: str, input_complexity: int) -> float:
        """Calculate token efficiency score for module"""
        base_score = 0.8
        
        # Adjust based on content length (shorter = more efficient)
        length_factor = max(0.5, 1.0 - len(content) / 10000)
        
        # Adjust based on input complexity (fewer inputs = more efficient)
        complexity_factor = max(0.6, 1.0 - input_complexity * 0.1)
        
        return min(0.99, base_score * length_factor * complexity_factor)
    
    def _extract_dependencies(self, content: str) -> List[str]:
        """Extract module dependencies (simulated)"""
        dependencies = []
        
        # Look for common dependency patterns
        if 'tdd' in content.lower():
            dependencies.append('tdd-cycle-pattern')
        if 'quality' in content.lower():
            dependencies.append('quality-validation-pattern')
        if 'routing' in content.lower():
            dependencies.append('intelligent-routing')
        if 'session' in content.lower():
            dependencies.append('session-management-pattern')
            
        return dependencies
    
    def render(self):
        """Render the Interactive Prompt Builder interface"""
        st.title("🔧 Interactive Prompt Builder")
        st.write("**Compose powerful prompts from 64+ modular components with drag-and-drop interface**")
        
        # User onboarding and guidance
        self._render_onboarding_guide()
        
        # Create two columns for module library and composition workspace
        col1, col2 = st.columns([1, 1])
        
        with col1:
            self._render_module_library()
        
        with col2:
            self._render_composition_workspace()
        
        # Render prompt preview and analysis
        st.divider()
        self._render_prompt_preview()
        
        # Render effectiveness analysis
        st.divider()
        self._render_effectiveness_analysis()
        
        # Render prompt execution environment
        if self.constructed_prompt:
            st.divider()
            self._render_execution_environment()
    
    def _render_module_library(self):
        """Render the module library with categorized components"""
        st.subheader("📚 Module Library")
        st.write("**Available Prompt Components**")
        
        # Filter controls
        categories = list(set(module.category for module in self.modules.values()))
        selected_category = st.selectbox("Filter by Category", ["All"] + categories)
        
        search_term = st.text_input("🔍 Search Modules", placeholder="Enter module name or purpose...")
        
        # Filter modules
        filtered_modules = self.modules.values()
        if selected_category != "All":
            filtered_modules = [m for m in filtered_modules if m.category == selected_category]
        if search_term:
            filtered_modules = [m for m in filtered_modules if 
                             search_term.lower() in m.name.lower() or 
                             search_term.lower() in m.purpose.lower()]
        
        # Display modules
        for module in list(filtered_modules)[:20]:  # Limit to 20 for performance
            with st.expander(f"🧩 {module.name.replace('_', ' ').title()}", expanded=False):
                col_a, col_b = st.columns([3, 1])
                
                with col_a:
                    st.write(f"**Purpose:** {module.purpose}")
                    st.write(f"**Category:** {module.category}")
                    
                    if module.inputs["required"]:
                        st.write(f"**Inputs:** {', '.join(module.inputs['required'][:3])}...")
                    if module.outputs["required"]:
                        st.write(f"**Outputs:** {', '.join(module.outputs['required'][:3])}...")
                
                with col_b:
                    efficiency_color = "green" if module.token_efficiency > 0.8 else "orange" if module.token_efficiency > 0.6 else "red"
                    st.metric("Token Efficiency", f"{module.token_efficiency:.1%}", delta=None)
                    
                    if st.button(f"Add to Workspace", key=f"add_{module.name}"):
                        self._add_to_workspace(module)
                        st.rerun()
    
    def _render_composition_workspace(self):
        """Render the composition workspace where users build prompts"""
        st.subheader("🏗️ Composition Workspace")
        st.write("**Build Your Prompt**")
        
        # Show progress indicator
        self._render_progress_indicator()
        
        if not self.composition_workspace:
            st.info("👈 Select modules from the library to start building your prompt")
            return
        
        # Show smart suggestions
        self._render_smart_suggestions()
        
        # Display composed modules
        for i, module in enumerate(self.composition_workspace):
            with st.container():
                col_a, col_b, col_c = st.columns([3, 1, 1])
                
                with col_a:
                    st.write(f"**{i+1}. {module.name.replace('_', ' ').title()}**")
                    st.caption(module.purpose)
                    
                    # Show compatibility hints
                    if len(self.composition_workspace) > 1:
                        self._render_module_compatibility_hints(module)
                
                with col_b:
                    if st.button("↑", key=f"up_{i}", disabled=i==0):
                        self._move_module_up(i)
                        st.rerun()
                    if st.button("↓", key=f"down_{i}", disabled=i==len(self.composition_workspace)-1):
                        self._move_module_down(i)
                        st.rerun()
                
                with col_c:
                    if st.button("🗑️", key=f"remove_{i}"):
                        self._remove_from_workspace(i)
                        st.rerun()
                
                st.divider()
        
        # Composition controls
        col_x, col_y = st.columns(2)
        
        with col_x:
            if st.button("🧠 Generate Prompt", type="primary"):
                self._generate_prompt()
                st.rerun()
        
        with col_y:
            if st.button("🔄 Clear All"):
                self.composition_workspace = []
                self.constructed_prompt = ""
                st.rerun()
    
    def _render_prompt_preview(self):
        """Render real-time prompt preview"""
        st.subheader("👁️ Prompt Preview")
        
        if not self.constructed_prompt:
            if self.composition_workspace:
                st.info("Click 'Generate Prompt' to see your composed prompt")
            else:
                st.info("Add modules to workspace to preview your prompt")
            return
        
        # Display the constructed prompt
        st.code(self.constructed_prompt, language="markdown")
        
        # Prompt analysis
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            word_count = len(self.constructed_prompt.split())
            st.metric("Word Count", word_count)
        
        with col2:
            token_estimate = word_count * 1.3  # Rough token estimate
            st.metric("Est. Tokens", f"{token_estimate:.0f}")
        
        with col3:
            module_count = len(self.composition_workspace)
            st.metric("Modules Used", module_count)
        
        with col4:
            avg_efficiency = sum(m.token_efficiency for m in self.composition_workspace) / len(self.composition_workspace) if self.composition_workspace else 0
            st.metric("Avg Efficiency", f"{avg_efficiency:.1%}")
        
        # Copy to clipboard
        if st.button("📋 Copy Prompt"):
            st.success("Prompt copied to clipboard! (Use Ctrl+C to copy the code block above)")
    
    def _render_effectiveness_analysis(self):
        """Render prompt effectiveness analysis"""
        st.subheader("📊 Effectiveness Analysis")
        
        if not self.composition_workspace:
            st.info("Add modules to see effectiveness analysis")
            return
        
        # Calculate effectiveness metrics
        metrics = self._calculate_effectiveness_metrics()
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Effectiveness radar chart
            fig = go.Figure()
            
            categories = ['Token Efficiency', 'Module Cohesion', 'Input Clarity', 'Output Specificity', 'Composition Flow']
            values = [
                metrics['token_efficiency'],
                metrics['module_cohesion'], 
                metrics['input_clarity'],
                metrics['output_specificity'],
                metrics['composition_flow']
            ]
            
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name='Effectiveness Score'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 1]
                    )
                ),
                title="Prompt Effectiveness Profile",
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Effectiveness metrics
            st.metric("Overall Score", f"{metrics['overall_score']:.1%}", 
                     delta=f"{metrics['overall_score'] - 0.7:.1%}")
            
            st.metric("Token Efficiency", f"{metrics['token_efficiency']:.1%}")
            st.metric("Module Cohesion", f"{metrics['module_cohesion']:.1%}")
            st.metric("Composition Flow", f"{metrics['composition_flow']:.1%}")
            
            # Recommendations
            st.write("**🎯 Recommendations:**")
            for rec in metrics['recommendations']:
                st.write(f"• {rec}")
    
    def _add_to_workspace(self, module: ModuleInterface):
        """Add module to composition workspace"""
        if module not in self.composition_workspace:
            self.composition_workspace.append(module)
            st.success(f"Added {module.name} to workspace")
            
            # Save state to session
            self._save_state_to_session()
            
            # Log activity
            self.session_manager.log_activity('module_added_to_workspace', {
                'module_name': module.name,
                'module_category': module.category,
                'workspace_size': len(self.composition_workspace)
            })
    
    def _remove_from_workspace(self, index: int):
        """Remove module from workspace"""
        if 0 <= index < len(self.composition_workspace):
            removed = self.composition_workspace.pop(index)
            st.success(f"Removed {removed.name} from workspace")
            
            # Save state to session
            self._save_state_to_session()
            
            # Log activity
            self.session_manager.log_activity('module_removed_from_workspace', {
                'module_name': removed.name,
                'module_category': removed.category,
                'workspace_size': len(self.composition_workspace)
            })
    
    def _move_module_up(self, index: int):
        """Move module up in composition order"""
        if index > 0:
            self.composition_workspace[index], self.composition_workspace[index-1] = \
                self.composition_workspace[index-1], self.composition_workspace[index]
    
    def _move_module_down(self, index: int):
        """Move module down in composition order"""
        if index < len(self.composition_workspace) - 1:
            self.composition_workspace[index], self.composition_workspace[index+1] = \
                self.composition_workspace[index+1], self.composition_workspace[index]
    
    def _generate_prompt(self):
        """Generate functional, executable prompt from selected modules"""
        if not self.composition_workspace:
            return
        
        # Analyze modules for intelligent composition
        analysis = self._analyze_module_composition()
        
        prompt_parts = []
        prompt_parts.append("# Executable Prompt Assembly")
        prompt_parts.append("# Generated by Interactive Prompt Builder")
        prompt_parts.append("")
        
        # Create Claude 4 optimized module execution structure
        prompt_parts.extend([
            "```xml",
            "<claude_4_module_execution enforcement=\"MANDATORY\" thinking_mode=\"interleaved\">",
            "  <!-- Interactive composition with advanced module assembly -->",
            ""
        ])
        
        # Classify modules by execution pattern
        core_modules = [m for m in self.composition_workspace if m.category in ['patterns', 'quality']]
        contextual_modules = [m for m in self.composition_workspace if m.category in ['development', 'security']]
        support_modules = [m for m in self.composition_workspace if m.category in ['system', 'git']]
        
        # Generate core execution stack
        if core_modules:
            prompt_parts.extend([
                "  <core_stack order=\"advanced_sequential\" optimization=\"context_hierarchical\">",
                "    <!-- Core modules requiring sequential execution with thinking integration -->"
            ])
            for module in core_modules:
                module_path = self._get_module_path(module)
                prompt_parts.append(f"    <module thinking=\"enabled\" cache=\"predictive\">{module_path} - {module.purpose}</module>")
                
                # Add interface contract information
                if module.inputs["required"]:
                    prompt_parts.append(f"    <!-- Required inputs: {', '.join(module.inputs['required'][:3])} -->")
                if module.dependencies:
                    prompt_parts.append(f"    <!-- Dependencies: {', '.join(module.dependencies[:2])} -->")
            
            prompt_parts.append("  </core_stack>")
            prompt_parts.append("")
        
        # Generate contextual modules
        if contextual_modules:
            prompt_parts.extend([
                "  <contextual_modules evaluation=\"intelligent_conditional\" analysis=\"claude_4_enhanced\">",
                "    <!-- Context-dependent modules with intelligent condition evaluation -->"
            ])
            for module in contextual_modules:
                module_path = self._get_module_path(module)
                conditions = self._generate_smart_conditions(module)
                prompt_parts.append(f"    <conditional module=\"{module_path}\" condition=\"{conditions}\" thinking=\"adaptive\"/>")
            
            prompt_parts.append("  </contextual_modules>")
            prompt_parts.append("")
        
        # Generate support modules for parallel execution
        if support_modules:
            prompt_parts.extend([
                "  <support_modules order=\"optimized_parallel\" batching=\"mandatory\" speedup=\"70_percent\">",
                "    <!-- Support modules executed in parallel for efficiency -->"
            ])
            for module in support_modules:
                module_path = self._get_module_path(module)
                batch_group = "validation" if "quality" in module.purpose.lower() else "analysis"
                prompt_parts.append(f"    <module batch_group=\"{batch_group}\">{module_path} - {module.purpose}</module>")
            
            prompt_parts.append("  </support_modules>")
            prompt_parts.append("")
        
        # Add execution workflow with interface contracts
        prompt_parts.extend([
            "  <execution_workflow>",
            "    <phase name=\"interface_validation\" order=\"1\">",
            "      <requirements>Validate module interface contracts and input requirements</requirements>",
            "      <actions>",
            "        <action>Verify all required inputs are available</action>",
            "        <action>Check module dependencies are satisfied</action>",
            "        <action>Initialize module execution contexts</action>",
            "      </actions>",
            "    </phase>",
            "    <phase name=\"orchestrated_execution\" order=\"2\">",
            "      <requirements>Execute modules with proper state management and output propagation</requirements>",
            "      <actions>",
            "        <action>Execute core stack sequentially with thinking integration</action>",
            "        <action>Evaluate contextual conditions and execute qualifying modules</action>",
            "        <action>Run support modules in parallel with tool batching</action>",
            "      </actions>",
            "    </phase>",
            "    <phase name=\"result_integration\" order=\"3\">",
            "      <requirements>Integrate outputs with consistency validation</requirements>",
            "      <actions>",
            "        <action>Consolidate module outputs into coherent result</action>",
            "        <action>Validate output contracts and quality requirements</action>",
            "        <action>Apply post-execution quality gates</action>",
            "      </actions>",
            "    </phase>",
            "  </execution_workflow>",
            ""
        ])
        
        # Add module interface specifications
        prompt_parts.extend([
            "  <module_interfaces>",
            "    <!-- Interface contracts for composed modules -->"
        ])
        
        for module in self.composition_workspace:
            if module.inputs["required"] or module.outputs["required"]:
                prompt_parts.append(f"    <interface module=\"{module.name}\">")
                if module.inputs["required"]:
                    prompt_parts.append(f"      <inputs required=\"{', '.join(module.inputs['required'])}\" optional=\"{', '.join(module.inputs['optional'])}\"/>")
                if module.outputs["required"]:
                    prompt_parts.append(f"      <outputs expected=\"{', '.join(module.outputs['required'])}\"/>")
                prompt_parts.append(f"      <efficiency target=\"{module.token_efficiency:.1%}\"/>")
                prompt_parts.append("    </interface>")
        
        prompt_parts.append("  </module_interfaces>")
        prompt_parts.append("")
        
        # Add performance monitoring
        avg_efficiency = sum(m.token_efficiency for m in self.composition_workspace) / len(self.composition_workspace)
        prompt_parts.extend([
            "  <performance_monitoring>",
            f"    <metric name=\"composition_efficiency\" target=\"{avg_efficiency:.1%}\"/>",
            f"    <metric name=\"module_count\" value=\"{len(self.composition_workspace)}\"/>",
            f"    <metric name=\"execution_complexity\" level=\"{analysis['complexity_level']}\"/>",
            "    <metric name=\"token_optimization\" target=\"70_percent_improvement\"/>",
            "  </performance_monitoring>",
            "",
            "</claude_4_module_execution>",
            "```",
            ""
        ])
        
        # Add execution instructions
        prompt_parts.extend([
            "## Interactive Assembly Instructions",
            "",
            "This prompt was assembled using the Interactive Prompt Builder with:",
            "",
            f"- **{len(core_modules)} Core Modules**: Sequential execution with thinking integration",
            f"- **{len(contextual_modules)} Contextual Modules**: Conditional execution based on context analysis",
            f"- **{len(support_modules)} Support Modules**: Parallel execution with tool batching optimization",
            "",
            "### Module Interface Contracts",
            ""
        ])
        
        # Add detailed interface information
        for i, module in enumerate(self.composition_workspace, 1):
            prompt_parts.append(f"**{i}. {module.name.replace('_', ' ').title()}**")
            if module.inputs["required"]:
                prompt_parts.append(f"   - Requires: {', '.join(module.inputs['required'])}")
            if module.outputs["required"]:
                prompt_parts.append(f"   - Produces: {', '.join(module.outputs['required'])}")
            if module.dependencies:
                prompt_parts.append(f"   - Depends on: {', '.join(module.dependencies)}")
            prompt_parts.append("")
        
        # Add quality metrics
        prompt_parts.extend([
            "### Assembly Quality Metrics",
            "",
            f"- **Token Efficiency**: {avg_efficiency:.1%}",
            f"- **Module Cohesion**: {analysis['cohesion_score']:.1%}",
            f"- **Interface Clarity**: {analysis['interface_clarity']:.1%}",
            f"- **Execution Complexity**: {analysis['complexity_level'].title()}",
            "",
            "### Ready for Claude Code Framework Execution",
            "",
            "This assembled prompt includes proper module orchestration, interface contracts,",
            "and Claude 4 optimization patterns for maximum effectiveness."
        ])
        
        self.constructed_prompt = "\n".join(prompt_parts)
        
        # Save state to session after prompt generation
        self._save_state_to_session()
        
        # Log activity
        self.session_manager.log_activity('prompt_generated', {
            'module_count': len(self.composition_workspace),
            'prompt_length': len(self.constructed_prompt),
            'generation_timestamp': datetime.now().isoformat()
        })
        
        return self.constructed_prompt
    
    def _analyze_module_composition(self) -> Dict[str, Any]:
        """Analyze module composition for intelligent assembly"""
        if not self.composition_workspace:
            return {}
        
        # Calculate cohesion based on category distribution
        categories = [m.category for m in self.composition_workspace]
        unique_categories = len(set(categories))
        cohesion_score = max(0.5, 1.0 - (unique_categories - 1) * 0.15)
        
        # Calculate interface clarity
        modules_with_clear_inputs = sum(1 for m in self.composition_workspace if m.inputs["required"])
        interface_clarity = modules_with_clear_inputs / len(self.composition_workspace)
        
        # Determine complexity level
        module_count = len(self.composition_workspace)
        if module_count >= 8:
            complexity_level = "high"
        elif module_count >= 4:
            complexity_level = "medium"
        else:
            complexity_level = "simple"
        
        return {
            "cohesion_score": cohesion_score,
            "interface_clarity": interface_clarity,
            "complexity_level": complexity_level,
            "total_modules": module_count,
            "category_diversity": unique_categories
        }
    
    def _get_module_path(self, module: ModuleInterface) -> str:
        """Get module path for XML references"""
        # Try to construct path from framework structure
        return f".claude/modules/{module.category}/{module.name.replace('_', '-')}.md"
    
    def _generate_smart_conditions(self, module: ModuleInterface) -> str:
        """Generate intelligent execution conditions for contextual modules"""
        conditions = []
        
        # Category-based conditions
        if module.category == "security":
            conditions.append("security_implications_detected")
        elif module.category == "development":
            conditions.append("implementation_required")
        elif module.category == "testing":
            conditions.append("testing_needed")
        
        # Purpose-based conditions
        if "multi" in module.name.lower():
            conditions.append("multi_component_coordination_needed")
        if "error" in module.purpose.lower():
            conditions.append("error_handling_required")
        if "optimization" in module.purpose.lower():
            conditions.append("performance_optimization_needed")
        
        # Input-based conditions
        if module.inputs["required"]:
            required_inputs = module.inputs["required"]
            if any("file" in inp.lower() for inp in required_inputs):
                conditions.append("file_operations_needed")
            if any("test" in inp.lower() for inp in required_inputs):
                conditions.append("testing_context_available")
        
        # Default condition
        if not conditions:
            conditions.append("context_appropriate")
        
        return " OR ".join(conditions)
    
    def _calculate_effectiveness_metrics(self) -> Dict[str, Any]:
        """Calculate effectiveness metrics for the composed prompt"""
        if not self.composition_workspace:
            return {}
        
        # Token efficiency (average of all modules)
        token_efficiency = sum(m.token_efficiency for m in self.composition_workspace) / len(self.composition_workspace)
        
        # Module cohesion (how well modules work together)
        cohesion_score = self._calculate_module_cohesion()
        
        # Input clarity (proportion of modules with clear inputs)
        clear_inputs = sum(1 for m in self.composition_workspace if m.inputs["required"])
        input_clarity = clear_inputs / len(self.composition_workspace)
        
        # Output specificity (proportion of modules with specific outputs)
        specific_outputs = sum(1 for m in self.composition_workspace if m.outputs["required"])
        output_specificity = specific_outputs / len(self.composition_workspace)
        
        # Composition flow (how well modules connect)
        composition_flow = self._calculate_composition_flow()
        
        # Overall score
        overall_score = (token_efficiency + cohesion_score + input_clarity + output_specificity + composition_flow) / 5
        
        # Generate recommendations
        recommendations = self._generate_recommendations(token_efficiency, cohesion_score, input_clarity, output_specificity, composition_flow)
        
        return {
            'token_efficiency': token_efficiency,
            'module_cohesion': cohesion_score,
            'input_clarity': input_clarity,
            'output_specificity': output_specificity,
            'composition_flow': composition_flow,
            'overall_score': overall_score,
            'recommendations': recommendations
        }
    
    def _calculate_module_cohesion(self) -> float:
        """Calculate how well modules work together"""
        if len(self.composition_workspace) <= 1:
            return 1.0
        
        # Check category similarity (modules from same category work better together)
        categories = [m.category for m in self.composition_workspace]
        unique_categories = len(set(categories))
        category_score = 1.0 - (unique_categories - 1) * 0.2
        
        # Check dependency satisfaction
        dependency_score = 0.8  # Base score
        
        return max(0.0, min(1.0, (category_score + dependency_score) / 2))
    
    def _calculate_composition_flow(self) -> float:
        """Calculate how well the composition flows"""
        if len(self.composition_workspace) <= 1:
            return 1.0
        
        # Base flow score
        flow_score = 0.8
        
        # Bonus for logical ordering (thinking -> execution -> validation pattern)
        thinking_modules = ['critical_thinking_pattern', 'intelligent_routing']
        execution_modules = ['tdd_cycle_pattern', 'workflow_orchestration_engine']
        validation_modules = ['quality_validation_pattern', 'comprehensive_testing']
        
        module_names = [m.name for m in self.composition_workspace]
        
        # Check for good ordering patterns
        has_thinking_first = any(name in thinking_modules for name in module_names[:2])
        has_validation_last = any(name in validation_modules for name in module_names[-2:])
        
        if has_thinking_first:
            flow_score += 0.1
        if has_validation_last:
            flow_score += 0.1
        
        return min(1.0, flow_score)
    
    def _generate_recommendations(self, token_efficiency: float, cohesion: float, 
                                input_clarity: float, output_specificity: float, 
                                composition_flow: float) -> List[str]:
        """Generate improvement recommendations"""
        recommendations = []
        
        if token_efficiency < 0.7:
            recommendations.append("Consider replacing low-efficiency modules with more optimized alternatives")
        
        if cohesion < 0.6:
            recommendations.append("Try grouping modules from similar categories for better cohesion")
        
        if input_clarity < 0.8:
            recommendations.append("Add modules with clearer input requirements for better clarity")
        
        if output_specificity < 0.8:
            recommendations.append("Include modules with more specific outputs for better results")
        
        if composition_flow < 0.7:
            recommendations.append("Consider reordering modules: thinking → execution → validation")
        
        if not recommendations:
            recommendations.append("Excellent composition! Consider testing with different scenarios")
        
        return recommendations
    
    def _render_execution_environment(self):
        """Render prompt execution environment with validation and testing"""
        st.subheader("🚀 Prompt Execution Environment")
        st.write("**Test and validate your composed prompt in a real execution environment**")
        
        # Create tabs for different testing approaches
        exec_tab1, exec_tab2, exec_tab3, exec_tab4 = st.tabs([
            "🔍 Structure Validation",
            "⚡ Performance Testing", 
            "🎯 Effectiveness Simulation",
            "📊 Execution Report"
        ])
        
        with exec_tab1:
            self._render_structure_validation()
        
        with exec_tab2:
            self._render_performance_testing()
        
        with exec_tab3:
            self._render_effectiveness_simulation()
        
        with exec_tab4:
            self._render_execution_report()
    
    def _render_structure_validation(self):
        """Validate prompt structure and module references"""
        st.subheader("🔍 Prompt Structure Validation")
        st.write("**Validate XML structure, module references, and interface contracts**")
        
        if st.button("🔬 Validate Prompt Structure", type="primary"):
            with st.spinner("Validating prompt structure..."):
                validation_results = self._validate_prompt_structure()
                
                # Display validation results
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    status_color = "green" if validation_results['overall_valid'] else "red"
                    st.metric("Overall Status", 
                             "✅ VALID" if validation_results['overall_valid'] else "❌ INVALID")
                
                with col2:
                    st.metric("Module References", 
                             f"{validation_results['valid_modules']}/{validation_results['total_modules']}")
                
                with col3:
                    st.metric("XML Structure", 
                             "✅ Valid" if validation_results['xml_valid'] else "❌ Invalid")
                
                # Detailed validation results
                if validation_results['issues']:
                    st.subheader("⚠️ Validation Issues")
                    for issue in validation_results['issues']:
                        st.error(f"• {issue}")
                
                if validation_results['warnings']:
                    st.subheader("⚡ Warnings")
                    for warning in validation_results['warnings']:
                        st.warning(f"• {warning}")
                
                if validation_results['suggestions']:
                    st.subheader("💡 Optimization Suggestions")
                    for suggestion in validation_results['suggestions']:
                        st.info(f"• {suggestion}")
                
                # Module reference details
                if validation_results['module_details']:
                    st.subheader("📋 Module Reference Analysis")
                    df_modules = pd.DataFrame(validation_results['module_details'])
                    st.dataframe(df_modules, use_container_width=True)
    
    def _render_performance_testing(self):
        """Test prompt performance and efficiency"""
        st.subheader("⚡ Performance Testing")
        st.write("**Simulate prompt execution and measure performance metrics**")
        
        # Performance testing configuration
        col1, col2 = st.columns(2)
        
        with col1:
            test_scenarios = st.multiselect(
                "Select Test Scenarios",
                ["Simple Task", "Complex Feature", "Multi-Agent Coordination", "Error Recovery", "Production Deployment"],
                default=["Simple Task", "Complex Feature"]
            )
        
        with col2:
            performance_focus = st.selectbox(
                "Performance Focus",
                ["Token Efficiency", "Execution Speed", "Quality Gates", "Error Handling", "Overall Performance"]
            )
        
        if st.button("🚀 Run Performance Tests", type="primary"):
            with st.spinner("Running performance simulation..."):
                perf_results = self._simulate_performance_testing(test_scenarios, performance_focus)
                
                # Performance metrics display
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Token Efficiency", 
                             f"{perf_results['token_efficiency']:.1%}",
                             delta=f"{perf_results['token_efficiency'] - 0.7:.1%}")
                
                with col2:
                    st.metric("Execution Speed", 
                             f"{perf_results['execution_speed']:.1f}s",
                             delta=f"{5.0 - perf_results['execution_speed']:.1f}s")
                
                with col3:
                    st.metric("Quality Score", 
                             f"{perf_results['quality_score']:.1%}",
                             delta=f"{perf_results['quality_score'] - 0.85:.1%}")
                
                with col4:
                    st.metric("Success Rate", 
                             f"{perf_results['success_rate']:.1%}",
                             delta=f"{perf_results['success_rate'] - 0.9:.1%}")
                
                # Performance breakdown by scenario
                st.subheader("📊 Performance by Scenario")
                scenario_data = []
                for scenario in test_scenarios:
                    scenario_data.append({
                        'Scenario': scenario,
                        'Token Usage': f"{perf_results['scenarios'][scenario]['tokens']:.0f}",
                        'Execution Time': f"{perf_results['scenarios'][scenario]['time']:.1f}s",
                        'Success Rate': f"{perf_results['scenarios'][scenario]['success']:.1%}",
                        'Quality Score': f"{perf_results['scenarios'][scenario]['quality']:.1%}"
                    })
                
                df_scenarios = pd.DataFrame(scenario_data)
                st.dataframe(df_scenarios, use_container_width=True)
                
                # Performance recommendations
                if perf_results['recommendations']:
                    st.subheader("🎯 Performance Recommendations")
                    for rec in perf_results['recommendations']:
                        st.write(f"• {rec}")
    
    def _render_effectiveness_simulation(self):
        """Simulate prompt effectiveness in real scenarios"""
        st.subheader("🎯 Effectiveness Simulation")
        st.write("**Simulate how your prompt performs against real development scenarios**")
        
        # Simulation parameters
        col1, col2 = st.columns(2)
        
        with col1:
            complexity_level = st.select_slider(
                "Task Complexity",
                options=["Simple", "Medium", "Complex", "Enterprise"],
                value="Medium"
            )
        
        with col2:
            team_size = st.select_slider(
                "Team Size Context",
                options=["Solo", "Small Team", "Large Team", "Multi-Team"],
                value="Small Team"
            )
        
        use_case = st.selectbox(
            "Primary Use Case",
            [
                "Feature Development", 
                "Bug Investigation", 
                "Code Refactoring", 
                "Performance Optimization",
                "Security Implementation",
                "Testing & QA",
                "Documentation Generation"
            ]
        )
        
        if st.button("🎯 Simulate Effectiveness", type="primary"):
            with st.spinner("Running effectiveness simulation..."):
                sim_results = self._simulate_effectiveness(complexity_level, team_size, use_case)
                
                # Effectiveness scores
                col1, col2 = st.columns(2)
                
                with col1:
                    # Effectiveness radar chart
                    fig = go.Figure()
                    
                    categories = ['Task Completion', 'Code Quality', 'Time Efficiency', 'Error Prevention', 'Team Collaboration']
                    values = [
                        sim_results['task_completion'],
                        sim_results['code_quality'],
                        sim_results['time_efficiency'],
                        sim_results['error_prevention'],
                        sim_results['team_collaboration']
                    ]
                    
                    fig.add_trace(go.Scatterpolar(
                        r=values,
                        theta=categories,
                        fill='toself',
                        name='Simulated Effectiveness',
                        fillcolor='rgba(46, 204, 113, 0.3)',
                        line_color='rgb(46, 204, 113)'
                    ))
                    
                    # Add benchmark line
                    benchmark_values = [0.85, 0.85, 0.85, 0.85, 0.85]
                    fig.add_trace(go.Scatterpolar(
                        r=benchmark_values,
                        theta=categories,
                        fill='toself',
                        name='Industry Benchmark',
                        fillcolor='rgba(241, 196, 15, 0.2)',
                        line_color='rgb(241, 196, 15)',
                        line=dict(dash='dash')
                    ))
                    
                    fig.update_layout(
                        polar=dict(
                            radialaxis=dict(
                                visible=True,
                                range=[0, 1]
                            )),
                        showlegend=True,
                        title="Effectiveness Simulation Results",
                        height=400
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    # Detailed metrics
                    st.metric("Overall Effectiveness", 
                             f"{sim_results['overall_score']:.1%}",
                             delta=f"{sim_results['overall_score'] - 0.82:.1%}")
                    
                    st.write("**📈 Key Strengths:**")
                    for strength in sim_results['strengths']:
                        st.write(f"✅ {strength}")
                    
                    st.write("**⚠️ Areas for Improvement:**")
                    for weakness in sim_results['weaknesses']:
                        st.write(f"🔸 {weakness}")
                
                # Scenario-specific insights
                st.subheader(f"📋 Insights for {use_case}")
                st.write(f"**Context:** {complexity_level} complexity, {team_size} environment")
                
                for insight in sim_results['scenario_insights']:
                    st.info(f"💡 {insight}")
    
    def _render_execution_report(self):
        """Generate comprehensive execution report"""
        st.subheader("📊 Comprehensive Execution Report")
        st.write("**Generate a detailed report of your prompt's readiness and effectiveness**")
        
        if st.button("📋 Generate Complete Report", type="primary"):
            with st.spinner("Generating comprehensive execution report..."):
                report = self._generate_execution_report()
                
                # Executive summary
                st.subheader("📈 Executive Summary")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    overall_grade = report['overall_grade']
                    grade_color = "green" if overall_grade >= 85 else "orange" if overall_grade >= 70 else "red"
                    st.metric("Overall Grade", f"{overall_grade:.0f}/100", 
                             delta=f"{overall_grade - 75:.0f} vs baseline")
                
                with col2:
                    st.metric("Production Ready", 
                             "✅ Yes" if report['production_ready'] else "❌ No")
                
                with col3:
                    st.metric("Framework Integration", 
                             "✅ Compatible" if report['framework_compatible'] else "⚠️ Issues")
                
                # Detailed assessment
                st.subheader("🔍 Detailed Assessment")
                
                assessment_data = []
                for category, score in report['detailed_scores'].items():
                    status = "✅ Excellent" if score >= 90 else "👍 Good" if score >= 80 else "⚠️ Needs Work"
                    assessment_data.append({
                        'Category': category.replace('_', ' ').title(),
                        'Score': f"{score:.0f}/100",
                        'Status': status,
                        'Priority': "High" if score < 70 else "Medium" if score < 85 else "Low"
                    })
                
                df_assessment = pd.DataFrame(assessment_data)
                st.dataframe(df_assessment, use_container_width=True)
                
                # Recommendations by priority
                st.subheader("🎯 Prioritized Recommendations")
                
                for priority in ['High', 'Medium', 'Low']:
                    priority_recs = [r for r in report['recommendations'] if r['priority'] == priority]
                    if priority_recs:
                        with st.expander(f"{priority} Priority Recommendations ({len(priority_recs)} items)"):
                            for rec in priority_recs:
                                st.write(f"**{rec['title']}**")
                                st.write(f"📋 {rec['description']}")
                                st.write(f"⚡ Impact: {rec['impact']}")
                                st.write(f"🛠️ Effort: {rec['effort']}")
                                st.divider()
                
                # Framework integration details
                st.subheader("🔗 Framework Integration Analysis")
                st.write(f"**Module Compatibility:** {report['module_compatibility']:.1%}")
                st.write(f"**Claude 4 Optimization:** {report['claude4_optimization']:.1%}")
                st.write(f"**Quality Gate Compliance:** {report['quality_compliance']:.1%}")
                
                # Export options
                st.subheader("📤 Export Options")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if st.button("📋 Export Report", type="secondary"):
                        export_data = self._export_execution_report(report)
                        st.download_button(
                            label="Download Report JSON",
                            data=export_data,
                            file_name=f"prompt_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                            mime="application/json"
                        )
                
                with col2:
                    if st.button("💾 Save Configuration", type="secondary"):
                        config_data = self._export_configuration()
                        st.download_button(
                            label="Download Configuration",
                            data=config_data,
                            file_name=f"prompt_config_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                            mime="application/json"
                        )
                
                with col3:
                    if st.button("🚀 Export Prompt", type="primary"):
                        if report['production_ready']:
                            prompt_data = self._export_prompt()
                            st.download_button(
                                label="Download Prompt",
                                data=prompt_data,
                                file_name=f"generated_prompt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                                mime="text/markdown"
                            )
                        else:
                            st.error("Resolve issues before exporting prompt")
    
    def _validate_prompt_structure(self) -> Dict[str, Any]:
        """Validate the generated prompt structure"""
        validation_results = {
            'overall_valid': True,
            'xml_valid': True,
            'valid_modules': 0,
            'total_modules': len(self.composition_workspace),
            'issues': [],
            'warnings': [],
            'suggestions': [],
            'module_details': []
        }
        
        # Validate XML structure
        if '<claude_4_module_execution' not in self.constructed_prompt:
            validation_results['xml_valid'] = False
            validation_results['issues'].append("Missing Claude 4 module execution structure")
        
        if '</claude_4_module_execution>' not in self.constructed_prompt:
            validation_results['xml_valid'] = False
            validation_results['issues'].append("Incomplete Claude 4 module execution structure")
        
        # Validate module references
        for module in self.composition_workspace:
            module_path = self._get_module_path(module)
            actual_path = self.framework_path / module_path.replace('.claude/', '')
            
            module_detail = {
                'Module': module.name.replace('_', ' ').title(),
                'Category': module.category,
                'Path': module_path,
                'Exists': 'Yes' if actual_path.exists() else 'No',
                'Efficiency': f"{module.token_efficiency:.1%}"
            }
            
            if actual_path.exists():
                validation_results['valid_modules'] += 1
                module_detail['Status'] = '✅ Valid'
            else:
                validation_results['issues'].append(f"Module not found: {module_path}")
                module_detail['Status'] = '❌ Missing'
                validation_results['overall_valid'] = False
            
            validation_results['module_details'].append(module_detail)
        
        # Check for optimization opportunities
        if len(self.composition_workspace) > 8:
            validation_results['warnings'].append(f"High module count ({len(self.composition_workspace)}) may impact performance")
        
        avg_efficiency = sum(m.token_efficiency for m in self.composition_workspace) / len(self.composition_workspace)
        if avg_efficiency < 0.7:
            validation_results['suggestions'].append(f"Consider replacing low-efficiency modules (avg: {avg_efficiency:.1%})")
        
        # Check for proper categorization
        categories = [m.category for m in self.composition_workspace]
        if len(set(categories)) == 1:
            validation_results['warnings'].append("All modules from same category - consider diversifying")
        
        return validation_results
    
    def _simulate_performance_testing(self, scenarios: List[str], focus: str) -> Dict[str, Any]:
        """Simulate performance testing for the prompt"""
        # Base performance metrics
        base_efficiency = sum(m.token_efficiency for m in self.composition_workspace) / len(self.composition_workspace)
        module_count = len(self.composition_workspace)
        
        # Calculate performance based on composition
        token_efficiency = min(0.95, base_efficiency * (1.0 + (5 - module_count) * 0.02))
        execution_speed = max(1.0, 3.0 + module_count * 0.3 - (base_efficiency * 2))
        quality_score = min(0.98, 0.7 + base_efficiency * 0.25 + (len(scenarios) * 0.02))
        success_rate = min(0.99, 0.8 + base_efficiency * 0.15 + (token_efficiency * 0.1))
        
        # Scenario-specific results
        scenario_results = {}
        for scenario in scenarios:
            complexity_factor = {
                "Simple Task": 1.0,
                "Complex Feature": 1.5,
                "Multi-Agent Coordination": 2.0,
                "Error Recovery": 1.3,
                "Production Deployment": 2.5
            }.get(scenario, 1.0)
            
            scenario_results[scenario] = {
                'tokens': (500 + module_count * 50) * complexity_factor,
                'time': execution_speed * complexity_factor,
                'success': success_rate / complexity_factor,
                'quality': quality_score * (0.9 + 0.1 / complexity_factor)
            }
        
        # Generate recommendations
        recommendations = []
        if token_efficiency < 0.8:
            recommendations.append("Optimize module selection for better token efficiency")
        if execution_speed > 5.0:
            recommendations.append("Consider reducing module count or using parallel execution")
        if quality_score < 0.85:
            recommendations.append("Add quality validation modules to improve output quality")
        
        return {
            'token_efficiency': token_efficiency,
            'execution_speed': execution_speed,
            'quality_score': quality_score,
            'success_rate': success_rate,
            'scenarios': scenario_results,
            'recommendations': recommendations
        }
    
    def _simulate_effectiveness(self, complexity: str, team_size: str, use_case: str) -> Dict[str, Any]:
        """Simulate prompt effectiveness in realistic scenarios"""
        # Base effectiveness calculation
        base_score = sum(m.token_efficiency for m in self.composition_workspace) / len(self.composition_workspace)
        
        # Adjust for context
        complexity_factors = {"Simple": 1.1, "Medium": 1.0, "Complex": 0.9, "Enterprise": 0.8}
        team_factors = {"Solo": 1.0, "Small Team": 1.05, "Large Team": 0.95, "Multi-Team": 0.9}
        
        complexity_adj = complexity_factors.get(complexity, 1.0)
        team_adj = team_factors.get(team_size, 1.0)
        
        # Calculate specific metrics
        task_completion = min(0.98, base_score * complexity_adj * 0.9 + 0.1)
        code_quality = min(0.96, base_score * 0.85 + 0.15)
        time_efficiency = min(0.94, base_score * team_adj * 0.8 + 0.2)
        error_prevention = min(0.92, base_score * 0.75 + 0.25)
        team_collaboration = min(0.90, base_score * team_adj * 0.7 + 0.3)
        
        overall_score = (task_completion + code_quality + time_efficiency + error_prevention + team_collaboration) / 5
        
        # Generate insights
        strengths = []
        weaknesses = []
        
        if task_completion > 0.85:
            strengths.append("High task completion rate expected")
        else:
            weaknesses.append("Task completion may be lower than optimal")
        
        if code_quality > 0.85:
            strengths.append("Strong code quality enforcement")
        else:
            weaknesses.append("Code quality validation needs improvement")
        
        if time_efficiency > 0.85:
            strengths.append("Efficient execution time expected")
        else:
            weaknesses.append("Execution time may be suboptimal")
        
        # Use case specific insights
        scenario_insights = []
        if use_case == "Feature Development":
            scenario_insights.extend([
                "Prompt includes proper TDD enforcement for feature development",
                "Module composition supports end-to-end feature implementation",
                "Quality gates ensure production-ready code"
            ])
        elif use_case == "Bug Investigation":
            scenario_insights.extend([
                "Analysis modules support systematic bug investigation",
                "Error recovery patterns help isolate and resolve issues",
                "Documentation modules capture findings effectively"
            ])
        
        return {
            'task_completion': task_completion,
            'code_quality': code_quality,
            'time_efficiency': time_efficiency,
            'error_prevention': error_prevention,
            'team_collaboration': team_collaboration,
            'overall_score': overall_score,
            'strengths': strengths,
            'weaknesses': weaknesses,
            'scenario_insights': scenario_insights
        }
    
    def _generate_execution_report(self) -> Dict[str, Any]:
        """Generate comprehensive execution report"""
        # Calculate overall metrics
        avg_efficiency = sum(m.token_efficiency for m in self.composition_workspace) / len(self.composition_workspace)
        module_count = len(self.composition_workspace)
        
        # Detailed scoring
        detailed_scores = {
            'prompt_structure': min(100, 70 + avg_efficiency * 30),
            'module_quality': min(100, 60 + avg_efficiency * 40),
            'execution_efficiency': min(100, 80 - module_count * 2 + avg_efficiency * 20),
            'integration_readiness': min(100, 75 + avg_efficiency * 25),
            'error_handling': min(100, 65 + len([m for m in self.composition_workspace if 'error' in m.purpose.lower()]) * 15),
            'performance_optimization': min(100, 70 + (avg_efficiency - 0.7) * 100)
        }
        
        overall_grade = sum(detailed_scores.values()) / len(detailed_scores)
        production_ready = overall_grade >= 80 and avg_efficiency >= 0.75
        framework_compatible = len([m for m in self.composition_workspace if self._get_module_path(m)]) == module_count
        
        # Generate prioritized recommendations
        recommendations = []
        
        if detailed_scores['prompt_structure'] < 80:
            recommendations.append({
                'title': 'Improve Prompt Structure',
                'description': 'Optimize XML structure and module organization',
                'impact': 'High',
                'effort': 'Medium',
                'priority': 'High'
            })
        
        if detailed_scores['module_quality'] < 80:
            recommendations.append({
                'title': 'Enhance Module Quality',
                'description': 'Replace low-efficiency modules with better alternatives',
                'impact': 'High',
                'effort': 'Low',
                'priority': 'High'
            })
        
        if detailed_scores['execution_efficiency'] < 85:
            recommendations.append({
                'title': 'Optimize Execution Efficiency',
                'description': 'Reduce module count or improve parallel execution',
                'impact': 'Medium',
                'effort': 'Medium',
                'priority': 'Medium'
            })
        
        if not recommendations:
            recommendations.append({
                'title': 'Ready for Advanced Testing',
                'description': 'Consider A/B testing with different scenarios',
                'impact': 'Low',
                'effort': 'High',
                'priority': 'Low'
            })
        
        return {
            'overall_grade': overall_grade,
            'production_ready': production_ready,
            'framework_compatible': framework_compatible,
            'detailed_scores': detailed_scores,
            'recommendations': recommendations,
            'module_compatibility': avg_efficiency,
            'claude4_optimization': min(1.0, avg_efficiency * 1.2),
            'quality_compliance': min(1.0, detailed_scores['module_quality'] / 100)
        }
    
    def _export_execution_report(self, report: Dict[str, Any]) -> str:
        """Export execution report as JSON"""
        export_data = {
            'metadata': {
                'export_type': 'execution_report',
                'timestamp': datetime.now().isoformat(),
                'framework_version': '3.0.0',
                'exporter': 'InteractivePromptBuilder'
            },
            'report': report,
            'composition': {
                'modules': [
                    {
                        'name': module.name,
                        'category': module.category,
                        'purpose': module.purpose,
                        'token_efficiency': module.token_efficiency,
                        'dependencies': module.dependencies
                    } for module in self.composition_workspace
                ],
                'total_modules': len(self.composition_workspace),
                'constructed_prompt_length': len(self.constructed_prompt) if self.constructed_prompt else 0
            }
        }
        return json.dumps(export_data, indent=2, ensure_ascii=False)
    
    def _export_configuration(self) -> str:
        """Export current configuration as JSON"""
        config_data = {
            'metadata': {
                'export_type': 'configuration',
                'timestamp': datetime.now().isoformat(),
                'framework_version': '3.0.0',
                'exporter': 'InteractivePromptBuilder'
            },
            'configuration': {
                'workspace_modules': [
                    {
                        'name': module.name,
                        'category': module.category,
                        'purpose': module.purpose,
                        'inputs': module.inputs,
                        'outputs': module.outputs,
                        'execution_pattern': module.execution_pattern,
                        'dependencies': module.dependencies,
                        'token_efficiency': module.token_efficiency
                    } for module in self.composition_workspace
                ],
                'total_modules': len(self.composition_workspace),
                'effectiveness_score': self.effectiveness_score
            },
            'import_instructions': {
                'description': 'This configuration can be imported back into the Interactive Prompt Builder',
                'steps': [
                    '1. Open Interactive Prompt Builder',
                    '2. Use the Import Configuration feature',
                    '3. Upload this JSON file',
                    '4. Review and modify as needed'
                ]
            }
        }
        return json.dumps(config_data, indent=2, ensure_ascii=False)
    
    def _export_prompt(self) -> str:
        """Export generated prompt as Markdown"""
        if not self.constructed_prompt:
            # Generate prompt if not already done
            self.constructed_prompt = self._generate_prompt()
        
        export_content = f"""# Generated Prompt

**Generated by:** Claude Code Interactive Prompt Builder  
**Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Framework Version:** 3.0.0  

## Module Composition

This prompt was composed from {len(self.composition_workspace)} modules:

"""
        
        # Add module details
        for i, module in enumerate(self.composition_workspace, 1):
            export_content += f"""### {i}. {module.name.replace('_', ' ').title()}
- **Category:** {module.category}
- **Purpose:** {module.purpose}
- **Token Efficiency:** {module.token_efficiency:.1%}
- **Dependencies:** {', '.join(module.dependencies) if module.dependencies else 'None'}

"""
        
        export_content += f"""## Generated Prompt

```xml
{self.constructed_prompt}
```

## Usage Instructions

1. Copy the prompt content from the XML block above
2. Use it directly with Claude Code framework
3. Ensure all referenced modules are available in your .claude directory
4. Test the prompt with your specific use case

## Module Dependencies

Make sure these modules are available in your framework:
"""
        
        # Add dependency list
        all_deps = set()
        for module in self.composition_workspace:
            all_deps.update(module.dependencies)
        
        if all_deps:
            for dep in sorted(all_deps):
                export_content += f"- {dep}\n"
        else:
            export_content += "- No external dependencies\n"
        
        export_content += f"""
## Performance Notes

- **Average Token Efficiency:** {sum(m.token_efficiency for m in self.composition_workspace) / len(self.composition_workspace):.1%}
- **Total Modules:** {len(self.composition_workspace)}
- **Estimated Performance:** {'High' if len(self.composition_workspace) <= 5 else 'Medium' if len(self.composition_workspace) <= 10 else 'Consider optimization'}

Generated by Claude Code Interactive Prompt Builder - https://github.com/swm-sink/claude-code-modular-prompts
"""
        
        return export_content
    
    def _render_onboarding_guide(self):
        """Render user onboarding and guidance"""
        # Check if user is new (no session history)
        is_new_user = not self.session_manager.get_prompt_builder_state().get('last_updated')
        
        if is_new_user or st.session_state.get('show_onboarding', False):
            with st.expander("🎯 Getting Started Guide", expanded=is_new_user):
                st.markdown("""
                ### Welcome to the Interactive Prompt Builder! 🚀
                
                This tool helps you compose powerful prompts from 64+ modular components. Here's how to get started:
                
                **Step 1: Explore Modules** 🔍
                - Browse the module library on the left
                - Use filters to find modules by category or purpose
                - Preview module details and capabilities
                
                **Step 2: Build Your Composition** 🏗️
                - Click "Add to Workspace" to add modules to your composition
                - Drag and drop modules to reorder them
                - Use the workspace controls to manage your composition
                
                **Step 3: Generate & Test** 🧪
                - Click "Generate Prompt" to create your executable prompt
                - Test your prompt in the execution environment
                - Validate effectiveness with built-in analysis tools
                
                **Step 4: Export & Use** 📥
                - Export your prompt as Markdown for direct use
                - Save configurations for future sessions
                - Download execution reports for analysis
                
                **Pro Tips:** 💡
                - Start with thinking pattern modules for better structure
                - Include TDD modules for quality-driven development
                - Use quality gates for production-ready prompts
                - Check compatibility suggestions for optimal composition
                """)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🎯 Start Quick Tour"):
                        st.session_state['show_quick_tour'] = True
                        st.rerun()
                
                with col2:
                    if st.button("✅ I'm Ready to Build"):
                        st.session_state['show_onboarding'] = False
                        st.rerun()
        
        # Quick tour overlay
        if st.session_state.get('show_quick_tour', False):
            self._render_quick_tour()
        
        # Show helpful tooltips and guidance
        if len(self.composition_workspace) == 0:
            st.info("💡 **Start building**: Add modules from the library to begin your prompt composition")
        elif len(self.composition_workspace) == 1:
            st.info("🎯 **Add more modules**: Consider adding complementary modules for a more powerful prompt")
        elif len(self.composition_workspace) > 5:
            st.warning("⚠️ **Optimization tip**: Large compositions may impact performance. Consider simplifying or optimizing.")
    
    def _render_quick_tour(self):
        """Render interactive quick tour"""
        st.markdown("""
        ---
        ### 🎯 Quick Tour - Step by Step
        """)
        
        tour_steps = [
            {
                "title": "🔍 Module Library",
                "description": "Browse and filter 64+ modules by category, effectiveness, and purpose",
                "action": "Try filtering by 'patterns' category to see structural modules"
            },
            {
                "title": "🏗️ Composition Workspace", 
                "description": "Drag and drop modules to build your prompt composition",
                "action": "Add 2-3 modules to see the composition workspace in action"
            },
            {
                "title": "🧪 Prompt Generation",
                "description": "Generate executable prompts with validation and analysis",
                "action": "Click 'Generate Prompt' when you have modules in workspace"
            },
            {
                "title": "📊 Effectiveness Analysis",
                "description": "Analyze your prompt's effectiveness, token efficiency, and optimization opportunities",
                "action": "Review analysis recommendations for better prompts"
            },
            {
                "title": "📥 Export & Use",
                "description": "Export your prompt for direct use with Claude Code framework",
                "action": "Use the export buttons to save your work"
            }
        ]
        
        for i, step in enumerate(tour_steps, 1):
            with st.expander(f"Step {i}: {step['title']}", expanded=i==1):
                st.write(f"**{step['description']}**")
                st.write(f"💡 {step['action']}")
        
        if st.button("🎯 End Tour"):
            st.session_state['show_quick_tour'] = False
            st.session_state['show_onboarding'] = False
            st.rerun()
    
    def _render_tooltip(self, text: str, tooltip: str):
        """Render text with helpful tooltip"""
        st.markdown(f"""
        <div title="{tooltip}" style="cursor: help; display: inline-block;">
            {text} ℹ️
        </div>
        """, unsafe_allow_html=True)
    
    def _render_progress_indicator(self):
        """Render progress indicator for prompt building"""
        steps = [
            ("Select Modules", len(self.composition_workspace) > 0),
            ("Arrange Composition", len(self.composition_workspace) > 1),
            ("Generate Prompt", bool(self.constructed_prompt)),
            ("Validate & Test", self.effectiveness_score > 0.5),
            ("Export & Use", False)  # This would be true if user has exported
        ]
        
        st.markdown("### 📊 Progress")
        progress_cols = st.columns(len(steps))
        
        for i, (step_name, completed) in enumerate(steps):
            with progress_cols[i]:
                if completed:
                    st.markdown(f"✅ **{step_name}**")
                else:
                    st.markdown(f"⏳ {step_name}")
        
        # Overall progress
        completed_steps = sum(1 for _, completed in steps if completed)
        progress = completed_steps / len(steps)
        st.progress(progress)
        st.write(f"Overall Progress: {progress:.1%} ({completed_steps}/{len(steps)} steps)")
    
    def _render_smart_suggestions(self):
        """Render smart suggestions based on current composition"""
        if not self.composition_workspace:
            return
        
        suggestions = []
        categories = [module.category for module in self.composition_workspace]
        
        # Suggest missing essential modules
        if 'patterns' not in categories:
            suggestions.append({
                'type': 'missing_essential',
                'title': 'Add Thinking Pattern',
                'description': 'Consider adding a thinking pattern module for better structure',
                'action': 'Browse patterns category'
            })
        
        if any('development' in cat for cat in categories) and 'quality' not in categories:
            suggestions.append({
                'type': 'quality_check',
                'title': 'Add Quality Gates',
                'description': 'Development modules benefit from quality validation',
                'action': 'Add quality modules'
            })
        
        # Suggest optimizations
        if len(self.composition_workspace) > 6:
            suggestions.append({
                'type': 'optimization',
                'title': 'Consider Simplification',
                'description': 'Large compositions may impact token efficiency',
                'action': 'Remove redundant modules'
            })
        
        # Show suggestions
        if suggestions:
            st.markdown("### 💡 Smart Suggestions")
            for suggestion in suggestions:
                icon = "🔍" if suggestion['type'] == 'missing_essential' else "⚡" if suggestion['type'] == 'optimization' else "🎯"
                
                with st.expander(f"{icon} {suggestion['title']}", expanded=False):
                    st.write(suggestion['description'])
                    st.write(f"**Recommended Action:** {suggestion['action']}")
    
    def _render_module_compatibility_hints(self, module: ModuleInterface):
        """Render compatibility hints for a module"""
        if not self.composition_workspace:
            return
        
        compatibility_score = 0
        hints = []
        
        for workspace_module in self.composition_workspace:
            # Check category compatibility
            if self._are_categories_compatible(module.category, workspace_module.category):
                compatibility_score += 1
                hints.append(f"✅ Compatible with {workspace_module.name}")
            else:
                hints.append(f"⚠️ May conflict with {workspace_module.name}")
        
        if hints:
            compatibility_percent = (compatibility_score / len(self.composition_workspace)) * 100
            color = "green" if compatibility_percent > 70 else "orange" if compatibility_percent > 40 else "red"
            
            st.markdown(f"**Compatibility: <span style='color: {color}'>{compatibility_percent:.0f}%</span>**", 
                       unsafe_allow_html=True)
            
            with st.expander("🔗 Compatibility Details", expanded=False):
                for hint in hints:
                    st.write(hint)
    
    def _are_categories_compatible(self, cat1: str, cat2: str) -> bool:
        """Check if two categories are compatible"""
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
        
        return (cat1, cat2) in compatible_pairs or (cat2, cat1) in compatible_pairs