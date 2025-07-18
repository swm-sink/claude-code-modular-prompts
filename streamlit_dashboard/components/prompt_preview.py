"""
Real-time Prompt Preview Component for Claude Code Modular Prompts Framework
Provides syntax highlighting, live composition, and interactive preview
"""

import streamlit as st
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import html
from collections import defaultdict


class PromptHighlighter:
    """Handles syntax highlighting for framework prompts"""
    
    def __init__(self):
        """Initialize PromptHighlighter"""
        self.command_pattern = r'/\w+'
        self.module_pattern = r'(?:modules|system|commands)/[^)\s,]+\.md'
        self.quality_pattern = r'\b(?:\d+%|\d+ms|enforced|blocking|critical)\b'
        
        # Color scheme for highlighting
        self.colors = {
            'command': '#0066cc',       # Blue for commands
            'module': '#009900',        # Green for modules
            'quality': '#cc6600',       # Orange for quality metrics
            'keyword': '#9900cc',       # Purple for keywords
            'error': '#cc0000'          # Red for errors
        }
    
    def highlight_framework_syntax(self, text: str) -> str:
        """Apply comprehensive framework syntax highlighting"""
        highlighted = html.escape(text)
        
        # Highlight commands first
        highlighted = self.highlight_commands(highlighted)
        
        # Highlight module references
        highlighted = self.highlight_module_references(highlighted)
        
        # Highlight quality metrics
        highlighted = self.highlight_quality_metrics(highlighted)
        
        # Highlight framework keywords
        highlighted = self.highlight_keywords(highlighted)
        
        return highlighted
    
    def highlight_commands(self, text: str) -> str:
        """Highlight command syntax (/task, /auto, etc.)"""
        def replace_command(match):
            command = match.group(0)
            return f'<span style="color: {self.colors["command"]}; font-weight: bold;">{command}</span>'
        
        return re.sub(self.command_pattern, replace_command, text)
    
    def highlight_module_references(self, text: str) -> str:
        """Highlight module file references"""
        def replace_module(match):
            module = match.group(0)
            return f'<span style="color: {self.colors["module"]}; font-style: italic;">{module}</span>'
        
        return re.sub(self.module_pattern, replace_module, text)
    
    def highlight_quality_metrics(self, text: str) -> str:
        """Highlight quality metrics and thresholds"""
        def replace_quality(match):
            metric = match.group(0)
            return f'<span style="color: {self.colors["quality"]}; font-weight: bold;">{metric}</span>'
        
        return re.sub(self.quality_pattern, replace_quality, text, flags=re.IGNORECASE)
    
    def highlight_keywords(self, text: str) -> str:
        """Highlight framework keywords"""
        keywords = [
            'TDD', 'RED', 'GREEN', 'REFACTOR', 
            'Quality Gates', 'Coverage', 'Performance',
            'Uses modules', 'Dependencies', 'Implementation'
        ]
        
        for keyword in keywords:
            pattern = r'\b' + re.escape(keyword) + r'\b'
            replacement = f'<span style="color: {self.colors["keyword"]}; font-weight: bold;">{keyword}</span>'
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        return text


class PromptComposer:
    """Handles composing prompts from framework components"""
    
    def __init__(self, framework_path: Path):
        """Initialize PromptComposer"""
        self.framework_path = framework_path
        self.components = {}
        self._load_available_components()
    
    def _load_available_components(self):
        """Load available framework components"""
        self.components = {
            'commands': {},
            'modules': {},
            'system': {}
        }
        
        # Load commands
        commands_dir = self.framework_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.glob("*.md"):
                self.components['commands'][cmd_file.stem] = str(cmd_file.relative_to(self.framework_path))
        
        # Load modules
        modules_dir = self.framework_path / "modules"
        if modules_dir.exists():
            for module_file in modules_dir.rglob("*.md"):
                relative_path = str(module_file.relative_to(self.framework_path))
                self.components['modules'][module_file.stem] = relative_path
        
        # Load system components
        system_dir = self.framework_path / "system"
        if system_dir.exists():
            for system_file in system_dir.rglob("*.md"):
                relative_path = str(system_file.relative_to(self.framework_path))
                self.components['system'][system_file.stem] = relative_path
    
    def load_component_content(self, file_path: str) -> str:
        """Load content from a framework component file"""
        try:
            full_path = self.framework_path / file_path
            if full_path.exists():
                return full_path.read_text()
            else:
                return f"# Component not found: {file_path}"
        except Exception as e:
            return f"# Error loading component: {str(e)}"
    
    def compose_prompt_from_components(self, components: List[Dict[str, Any]]) -> str:
        """Compose a prompt from multiple components"""
        if not components:
            return "# Empty Prompt\n\nNo components selected."
        
        prompt_parts = []
        
        # Add header
        prompt_parts.append("# Composed Prompt")
        prompt_parts.append(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        prompt_parts.append("")
        
        # Process each component
        for component in components:
            file_path = component.get('file', '')
            if file_path:
                content = self.load_component_content(file_path)
                
                # Add section header
                prompt_parts.append(f"## {component.get('name', 'Unknown Component')}")
                prompt_parts.append(f"Type: {component.get('type', 'unknown')}")
                prompt_parts.append("")
                prompt_parts.append(content)
                prompt_parts.append("")
                prompt_parts.append("---")
                prompt_parts.append("")
        
        return "\n".join(prompt_parts)
    
    def resolve_component_dependencies(self, components: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Resolve dependencies between components"""
        resolved = list(components)  # Start with original components
        
        # Simple dependency resolution - add commonly used dependencies
        for component in components:
            if component.get('type') == 'command':
                # Commands typically need quality gates
                if not any(c.get('name') == 'universal-quality-gates' for c in resolved):
                    resolved.append({
                        'type': 'system',
                        'name': 'universal-quality-gates',
                        'file': 'system/quality/universal-quality-gates.md'
                    })
                
                # Commands often use TDD patterns
                if component.get('name') in ['task', 'feature'] and not any(c.get('name') == 'tdd-cycle-pattern' for c in resolved):
                    resolved.append({
                        'type': 'module', 
                        'name': 'tdd-cycle-pattern',
                        'file': 'modules/patterns/tdd-cycle-pattern.md'
                    })
        
        return resolved
    
    def validate_prompt_composition(self, components: List[Dict[str, Any]]) -> Tuple[bool, List[str]]:
        """Validate prompt composition for completeness"""
        errors = []
        
        for component in components:
            file_path = component.get('file', '')
            if not file_path:
                errors.append(f"Component {component.get('name', 'unknown')} missing file path")
                continue
            
            full_path = self.framework_path / file_path
            if not full_path.exists():
                errors.append(f"Component file not found: {file_path}")
        
        return len(errors) == 0, errors
    
    def optimize_prompt_structure(self, prompt: str) -> str:
        """Optimize prompt structure for clarity and effectiveness"""
        lines = prompt.split('\n')
        optimized_lines = []
        
        in_header = False
        
        for line in lines:
            stripped = line.strip()
            
            # Improve header formatting
            if stripped.startswith('#'):
                if optimized_lines and optimized_lines[-1].strip():
                    optimized_lines.append('')  # Add space before headers
                optimized_lines.append(line)
                in_header = True
                continue
            
            # Add spacing after headers
            if in_header and stripped:
                in_header = False
                optimized_lines.append('')
            
            optimized_lines.append(line)
        
        # Remove excessive blank lines
        final_lines = []
        blank_count = 0
        
        for line in optimized_lines:
            if not line.strip():
                blank_count += 1
                if blank_count <= 2:  # Max 2 consecutive blank lines
                    final_lines.append(line)
            else:
                blank_count = 0
                final_lines.append(line)
        
        return '\n'.join(final_lines)


class PromptPreview:
    """Main component for real-time prompt preview with syntax highlighting"""
    
    def __init__(self, framework_path: Path):
        """Initialize PromptPreview"""
        self.framework_path = framework_path
        self.highlighter = PromptHighlighter()
        self.composer = PromptComposer(framework_path)
    
    def generate_live_preview(self, components: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate live preview as user builds prompt"""
        if not components:
            return {
                'raw_prompt': "# Empty Prompt\n\nAdd components to build your prompt.",
                'highlighted_prompt': self.highlighter.highlight_framework_syntax("# Empty Prompt\n\nAdd components to build your prompt."),
                'metadata': {
                    'component_count': 0,
                    'character_count': 0,
                    'estimated_tokens': 0
                }
            }
        
        # Compose the prompt
        raw_prompt = self.composer.compose_prompt_from_components(components)
        
        # Optimize structure
        optimized_prompt = self.composer.optimize_prompt_structure(raw_prompt)
        
        # Apply syntax highlighting
        highlighted_prompt = self.highlighter.highlight_framework_syntax(optimized_prompt)
        
        # Calculate metrics
        metrics = self.calculate_prompt_metrics(optimized_prompt)
        
        return {
            'raw_prompt': optimized_prompt,
            'highlighted_prompt': highlighted_prompt,
            'metadata': {
                'component_count': len(components),
                'character_count': metrics['character_count'],
                'word_count': metrics['word_count'],
                'command_count': metrics['command_count'],
                'module_count': metrics['module_count'],
                'estimated_tokens': metrics['estimated_tokens'],
                'validation_errors': self.detect_syntax_errors(optimized_prompt)
            }
        }
    
    def calculate_prompt_metrics(self, prompt_text: str) -> Dict[str, int]:
        """Calculate prompt metrics (length, complexity, etc.)"""
        metrics = {
            'character_count': len(prompt_text),
            'word_count': len(prompt_text.split()),
            'line_count': len(prompt_text.split('\n')),
            'command_count': len(re.findall(r'/\w+', prompt_text)),
            'module_count': len(re.findall(r'(?:modules|system|commands)/[^)\s,]+\.md', prompt_text)),
            'estimated_tokens': self._estimate_tokens(prompt_text)
        }
        
        return metrics
    
    def _estimate_tokens(self, text: str) -> int:
        """Rough token estimation (1 token ≈ 4 characters for English)"""
        return len(text) // 4
    
    def detect_syntax_errors(self, prompt_text: str) -> List[str]:
        """Detect syntax errors in prompt composition"""
        errors = []
        
        # Check for malformed commands
        malformed_commands = re.findall(r'/\s+\w+', prompt_text)
        for cmd in malformed_commands:
            errors.append(f"Malformed command: '{cmd}' (space after /)")
        
        # Check for missing file extensions
        incomplete_modules = re.findall(r'(?:modules|system|commands)/[^)\s,]+(?<!\.md)', prompt_text)
        for module in incomplete_modules:
            if '.' not in module:
                errors.append(f"Module reference missing .md extension: '{module}'")
        
        return errors
    
    def get_completion_suggestions(self, text: str, cursor_position: int) -> List[Dict[str, str]]:
        """Get autocomplete suggestions based on current input"""
        suggestions = []
        
        # Get text up to cursor
        text_to_cursor = text[:cursor_position]
        
        # Suggest commands
        if text_to_cursor.endswith('/') or re.search(r'/\w*$', text_to_cursor):
            available_commands = list(self.composer.components['commands'].keys())
            current_cmd = re.search(r'/(\w*)$', text_to_cursor)
            if current_cmd:
                prefix = current_cmd.group(1).lower()
                for cmd in available_commands:
                    if cmd.lower().startswith(prefix):
                        suggestions.append({
                            'type': 'command',
                            'value': f'/{cmd}',
                            'description': f'Command: {cmd}'
                        })
        
        # Suggest modules
        if 'modules/' in text_to_cursor:
            module_match = re.search(r'modules/([^)\s,]*)$', text_to_cursor)
            if module_match:
                prefix = module_match.group(1).lower()
                for module_name, module_path in self.composer.components['modules'].items():
                    if module_name.lower().startswith(prefix):
                        suggestions.append({
                            'type': 'module',
                            'value': module_path,
                            'description': f'Module: {module_name}'
                        })
        
        return suggestions[:10]  # Limit to 10 suggestions
    
    def export_prompt_template(self, components: List[Dict[str, Any]], output_path: Path) -> bool:
        """Export composed prompt as reusable template"""
        try:
            template_data = {
                'name': f"Template {datetime.now().strftime('%Y%m%d_%H%M%S')}",
                'version': '1.0',
                'created': datetime.now().isoformat(),
                'components': components,
                'metadata': {
                    'framework_path': str(self.framework_path),
                    'component_count': len(components)
                }
            }
            
            with open(output_path, 'w') as f:
                json.dump(template_data, f, indent=2)
            
            return True
        except Exception as e:
            st.error(f"Error exporting template: {str(e)}")
            return False
    
    def import_prompt_template(self, template_path: Path) -> List[Dict[str, Any]]:
        """Import prompt template and return components"""
        try:
            with open(template_path, 'r') as f:
                template_data = json.load(f)
            
            return template_data.get('components', [])
        except Exception as e:
            st.error(f"Error importing template: {str(e)}")
            return []
    
    def validate_prompt_real_time(self, prompt_text: str) -> Dict[str, Any]:
        """Real-time validation as user types"""
        errors = self.detect_syntax_errors(prompt_text)
        metrics = self.calculate_prompt_metrics(prompt_text)
        
        # Basic validation rules
        is_valid = len(errors) == 0
        
        # Warning thresholds
        warnings = []
        if metrics['character_count'] > 5000:
            warnings.append("Prompt is very long (>5000 characters)")
        if metrics['command_count'] > 5:
            warnings.append("Many commands detected - consider simplifying")
        
        return {
            'is_valid': is_valid,
            'errors': errors,
            'warnings': warnings,
            'suggestions': self.get_completion_suggestions(prompt_text, len(prompt_text)),
            'metrics': metrics
        }
    
    def get_shareable_state(self, components: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Get current state for collaborative sharing"""
        return {
            'components': components,
            'timestamp': datetime.now().isoformat(),
            'framework_path': str(self.framework_path),
            'version': '1.0'
        }
    
    def apply_shared_state(self, state: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Apply shared state from collaborative editing"""
        return state.get('components', [])
    
    def render_prompt_preview_ui(self):
        """Render the prompt preview user interface"""
        st.title("🔍 Real-time Prompt Preview")
        
        # Initialize session state for components
        if 'prompt_components' not in st.session_state:
            st.session_state.prompt_components = []
        
        # Component selection interface
        st.sidebar.header("📝 Prompt Builder")
        
        # Add new component
        st.sidebar.subheader("Add Component")
        
        component_type = st.sidebar.selectbox(
            "Component Type",
            ["command", "module", "system"]
        )
        
        # Get available components of selected type
        available_components = list(self.composer.components[component_type].keys())
        
        if available_components:
            selected_component = st.sidebar.selectbox(
                f"Select {component_type.title()}",
                available_components
            )
            
            if st.sidebar.button(f"Add {component_type.title()}"):
                new_component = {
                    'type': component_type,
                    'name': selected_component,
                    'file': self.composer.components[component_type][selected_component]
                }
                st.session_state.prompt_components.append(new_component)
                st.rerun()
        
        # Current components
        if st.session_state.prompt_components:
            st.sidebar.subheader("Current Components")
            for i, component in enumerate(st.session_state.prompt_components):
                col1, col2 = st.sidebar.columns([3, 1])
                with col1:
                    st.write(f"**{component['name']}** ({component['type']})")
                with col2:
                    if st.button("🗑️", key=f"remove_{i}"):
                        st.session_state.prompt_components.pop(i)
                        st.rerun()
        
        # Clear all button
        if st.session_state.prompt_components and st.sidebar.button("Clear All"):
            st.session_state.prompt_components = []
            st.rerun()
        
        # Main preview area
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("🖥️ Live Preview")
            
            # Generate preview
            preview_data = self.generate_live_preview(st.session_state.prompt_components)
            
            # Display highlighted prompt
            if preview_data['highlighted_prompt']:
                st.markdown(
                    f'<div style="background-color: #f0f0f0; padding: 15px; border-radius: 5px; border: 1px solid #ddd;">'
                    f'{preview_data["highlighted_prompt"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )
            
            # Raw prompt in expandable section
            with st.expander("📄 Raw Prompt Text"):
                st.code(preview_data['raw_prompt'], language='markdown')
        
        with col2:
            st.subheader("📊 Prompt Analytics")
            
            metadata = preview_data['metadata']
            
            # Metrics
            st.metric("Components", metadata['component_count'])
            st.metric("Characters", metadata['character_count'])
            st.metric("Words", metadata.get('word_count', 0))
            st.metric("Est. Tokens", metadata['estimated_tokens'])
            
            # Validation status
            if metadata.get('validation_errors'):
                st.error("❌ Validation Errors:")
                for error in metadata['validation_errors']:
                    st.write(f"• {error}")
            else:
                st.success("✅ No validation errors")
        
        # Template management
        st.divider()
        st.subheader("💾 Template Management")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📥 Export Template"):
                if st.session_state.prompt_components:
                    template_file = Path(f"prompt_template_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
                    if self.export_prompt_template(st.session_state.prompt_components, template_file):
                        st.success(f"Template exported to {template_file}")
                else:
                    st.warning("No components to export")
        
        with col2:
            uploaded_file = st.file_uploader("📤 Import Template", type=['json'])
            if uploaded_file:
                template_data = json.load(uploaded_file)
                if 'components' in template_data:
                    st.session_state.prompt_components = template_data['components']
                    st.success("Template imported successfully")
                    st.rerun()
        
        with col3:
            if st.button("🔄 Auto-resolve Dependencies"):
                if st.session_state.prompt_components:
                    resolved = self.composer.resolve_component_dependencies(st.session_state.prompt_components)
                    st.session_state.prompt_components = resolved
                    st.success("Dependencies resolved")
                    st.rerun()
    
    def render(self):
        """Main render method for Prompt Preview"""
        self.render_prompt_preview_ui()