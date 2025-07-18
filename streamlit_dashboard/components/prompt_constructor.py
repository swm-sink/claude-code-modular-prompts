"""
Prompt Constructor Component for Claude Code Modular Prompts Framework
Allows users to build custom prompts by selecting and combining framework modules
"""
import streamlit as st
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import re


class PromptConstructor:
    """Component for building custom prompts from framework modules"""
    
    def __init__(self, framework_path: Path):
        """Initialize Prompt Constructor with framework path"""
        self.framework_path = framework_path
        self.available_modules = self.load_available_modules()
        self.selected_modules = []
        self.constructed_prompt = ""
    
    def load_available_modules(self) -> Dict[str, List[str]]:
        """Load all available modules from the framework"""
        modules = {}
        modules_dir = self.framework_path / "modules"
        
        if modules_dir.exists():
            for category_dir in modules_dir.iterdir():
                if category_dir.is_dir():
                    category_name = category_dir.name
                    modules[category_name] = []
                    
                    for module_file in category_dir.glob("*.md"):
                        modules[category_name].append(module_file.name)
        
        return modules
    
    def parse_module_content(self, module_path: Path) -> Dict[str, Any]:
        """Parse module content and extract metadata"""
        if not module_path.exists():
            return {}
        
        content = module_path.read_text()
        
        # Extract module name from filename
        name = module_path.stem
        
        # Extract purpose from content
        purpose = ""
        purpose_match = re.search(r'##?\s*Purpose\s*\n+(.*?)(?:\n\n|##)', content, re.IGNORECASE | re.DOTALL)
        if purpose_match:
            purpose = purpose_match.group(1).strip()
        
        # Extract sections
        sections = []
        section_pattern = r'^##?\s*(.+?)$'
        for match in re.finditer(section_pattern, content, re.MULTILINE):
            sections.append(match.group(1).strip())
        
        return {
            'name': name,
            'purpose': purpose,
            'content': content,
            'sections': sections
        }
    
    def add_module_to_prompt(self, category: str, module_name: str) -> bool:
        """Add a module to the prompt construction"""
        module_path = self.framework_path / "modules" / category / module_name
        
        if module_path.exists():
            module_data = self.parse_module_content(module_path)
            module_data['category'] = category
            module_data['name'] = module_name
            self.selected_modules.append(module_data)
            return True
        
        return False
    
    def remove_module_from_prompt(self, index: int) -> bool:
        """Remove a module from the prompt construction"""
        if 0 <= index < len(self.selected_modules):
            self.selected_modules.pop(index)
            return True
        return False
    
    def reorder_modules(self, from_index: int, to_index: int) -> bool:
        """Reorder modules in the prompt"""
        if (0 <= from_index < len(self.selected_modules) and 
            0 <= to_index < len(self.selected_modules) and 
            from_index != to_index):
            
            module = self.selected_modules.pop(from_index)
            self.selected_modules.insert(to_index, module)
            return True
        
        return False
    
    def construct_prompt(self, custom_instructions: str = "", include_metadata: bool = True) -> str:
        """Construct the final prompt from selected modules"""
        prompt_parts = []
        
        # Add header
        if include_metadata:
            prompt_parts.append("# Claude Code Modular Prompt")
            prompt_parts.append(f"# Modules: {len(self.selected_modules)}")
            prompt_parts.append("")
        
        # Add custom instructions if provided
        if custom_instructions:
            prompt_parts.append("## Custom Instructions")
            prompt_parts.append(str(custom_instructions))  # Convert to string in case of mock
            prompt_parts.append("")
        
        # Add each module
        for module in self.selected_modules:
            prompt_parts.append(f"## Module: {module['name']}")
            prompt_parts.append(f"Category: {module['category']}")
            prompt_parts.append("")
            prompt_parts.append(module['content'])
            prompt_parts.append("")
        
        self.constructed_prompt = "\n".join(prompt_parts)
        return self.constructed_prompt
    
    def validate_prompt(self, prompt: str) -> Dict[str, Any]:
        """Validate the constructed prompt"""
        validation = {
            'is_valid': True,
            'token_count': self.estimate_token_count(prompt),
            'warnings': [],
            'errors': []
        }
        
        # Check if prompt is empty
        if not prompt.strip():
            validation['is_valid'] = False
            validation['errors'].append("Prompt is empty")
        
        # Check token count
        if validation['token_count'] > 100000:
            validation['warnings'].append("Prompt may be too long for some models")
        
        # Check for required sections
        if len(self.selected_modules) == 0:
            validation['warnings'].append("No modules selected")
        
        return validation
    
    def export_prompt_template(self, file_path: Path, name: str, description: str) -> bool:
        """Export current prompt configuration as a template"""
        template = {
            'name': name,
            'description': description,
            'modules': [
                {
                    'category': module['category'],
                    'name': module['name']
                }
                for module in self.selected_modules
            ],
            'custom_instructions': ""
        }
        
        try:
            with open(file_path, 'w') as f:
                json.dump(template, f, indent=2)
            return True
        except Exception:
            return False
    
    def import_prompt_template(self, file_path: Path) -> bool:
        """Import prompt configuration from a template"""
        try:
            with open(file_path, 'r') as f:
                template = json.load(f)
            
            # Clear current selection
            self.selected_modules = []
            
            # Load modules from template
            for module_info in template.get('modules', []):
                self.add_module_to_prompt(
                    module_info['category'],
                    module_info['name']
                )
            
            return True
        except Exception:
            return False
    
    def estimate_token_count(self, text: str) -> int:
        """Estimate token count for the text"""
        # Simple estimation: ~4 characters per token
        return len(text) // 4
    
    def get_module_dependencies(self, module_path: Path) -> List[str]:
        """Get dependencies for a module"""
        dependencies = []
        
        if module_path.exists():
            content = module_path.read_text()
            
            # Look for dependency patterns
            dep_pattern = r'(?:requires?|depends? on|needs?|uses?)[:\s]+(.+?)(?:\n|$)'
            matches = re.finditer(dep_pattern, content, re.IGNORECASE)
            
            for match in matches:
                deps = match.group(1).strip()
                # Split by common separators
                for dep in re.split(r'[,;]', deps):
                    dep = dep.strip()
                    if dep:
                        dependencies.append(dep)
        
        return dependencies
    
    def render_module_selector(self):
        """Render the module selector UI"""
        st.subheader("Select Modules")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            category = st.selectbox(
                "Category",
                options=list(self.available_modules.keys()),
                key="module_category"
            )
        
        if category and self.available_modules.get(category):
            with col2:
                module = st.selectbox(
                    "Module",
                    options=self.available_modules[category],
                    key="module_name"
                )
            
            if st.button("Add Module", type="primary"):
                if self.add_module_to_prompt(category, module):
                    st.success(f"Added {module}")
                    st.rerun()
    
    def render_selected_modules(self):
        """Render the list of selected modules"""
        st.subheader("Selected Modules")
        
        if not self.selected_modules:
            st.info("No modules selected yet")
            return
        
        for i, module in enumerate(self.selected_modules):
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.text(f"{module['category']}/{module['name']}")
            
            with col2:
                if i > 0 and st.button("↑", key=f"up_{i}"):
                    self.reorder_modules(i, i - 1)
                    st.rerun()
            
            with col3:
                if st.button("×", key=f"remove_{i}"):
                    self.remove_module_from_prompt(i)
                    st.rerun()
    
    def render_prompt_preview(self):
        """Render prompt preview"""
        st.subheader("Prompt Preview")
        
        custom_instructions = st.text_area(
            "Custom Instructions (optional)",
            height=100,
            key="custom_instructions"
        )
        
        include_metadata = st.checkbox("Include metadata", value=True)
        
        prompt = self.construct_prompt(custom_instructions, include_metadata)
        validation = self.validate_prompt(prompt)
        
        # Show validation status
        col1, col2 = st.columns(2)
        with col1:
            if validation['is_valid']:
                st.success("✅ Valid prompt")
            else:
                st.error("❌ Invalid prompt")
        
        with col2:
            st.metric("Token Count", validation['token_count'])
        
        # Show warnings/errors
        for warning in validation['warnings']:
            st.warning(warning)
        
        for error in validation['errors']:
            st.error(error)
        
        # Show prompt preview
        st.code(prompt, language="markdown")
    
    def render_templates_tab(self):
        """Render templates management tab"""
        st.subheader("Prompt Templates")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Export Template")
            template_name = st.text_input("Template Name")
            template_desc = st.text_area("Description", height=100)
            
            if st.button("Export Current Configuration", type="primary"):
                if template_name:
                    file_path = Path(f"{template_name.lower().replace(' ', '_')}.json")
                    if self.export_prompt_template(file_path, template_name, template_desc):
                        st.success(f"Exported to {file_path}")
                    else:
                        st.error("Export failed")
        
        with col2:
            st.markdown("### Import Template")
            uploaded_file = st.file_uploader("Upload Template", type=["json"])
            
            if uploaded_file:
                # Save uploaded file temporarily
                import tempfile
                with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = Path(tmp.name)
                
                if st.button("Import Template", type="primary"):
                    if self.import_prompt_template(tmp_path):
                        st.success("Template imported successfully")
                        st.rerun()
                    else:
                        st.error("Import failed")
                
                # Clean up
                tmp_path.unlink()
    
    def render(self):
        """Main render method for the component"""
        st.title("🔨 Prompt Constructor")
        st.markdown("Build custom prompts by combining framework modules")
        
        tabs = st.tabs(["🔨 Constructor", "📚 Templates", "🔍 Preview"])
        
        with tabs[0]:
            self.render_module_selector()
            st.divider()
            self.render_selected_modules()
        
        with tabs[1]:
            self.render_templates_tab()
        
        with tabs[2]:
            self.render_prompt_preview()