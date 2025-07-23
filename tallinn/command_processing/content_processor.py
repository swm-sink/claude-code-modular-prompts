#!/usr/bin/env python3
"""
Content Processor Module

Handles processing and cleaning of prompt content, including XML tag removal,
argument injection, and content optimization.
"""

import re
from typing import List, Dict, Any
from pathlib import Path


class ContentProcessor:
    """Processes and cleans command content."""
    
    def __init__(self, source_dir: Path):
        self.source_dir = source_dir
        self.components_dir = source_dir.parent / "components"
        self.component_cache = {}
    
    def load_component(self, component_path: str) -> str:
        """Load and cache component content."""
        if component_path in self.component_cache:
            return self.component_cache[component_path]
            
        full_path = self.source_dir.parent / component_path
        if full_path.exists():
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.component_cache[component_path] = content
                return content
        else:
            return f"<!-- Component not found: {component_path} -->"
    
    def create_human_readable_prompt(self, prompt_content: str, components: List[str]) -> str:
        """Create clean, human-readable prompt with embedded essential logic."""
        
        # Remove XML comments and includes
        prompt_content = re.sub(r'<!--.*?-->', '', prompt_content, flags=re.DOTALL)
        prompt_content = re.sub(r'<include>.*?</include>', '', prompt_content)
        
        # Convert XML-style tags to clean markdown
        prompt_content = re.sub(r'<([^>/]+)>', r'\n**\1**:\n', prompt_content)
        prompt_content = re.sub(r'</[^>]+>', '', prompt_content)
        
        # Clean up excessive whitespace
        prompt_content = re.sub(r'\n\s*\n\s*\n+', '\n\n', prompt_content)
        prompt_content = re.sub(r'[ \t]+', ' ', prompt_content)
        prompt_content = prompt_content.strip()
        
        # Extract and embed essential component logic
        if components:
            essential_logic = self.extract_and_embed_component_logic(components)
            if essential_logic:
                prompt_content += "\n\n" + essential_logic
        
        # Add $ARGUMENTS usage patterns
        prompt_content = self.inject_arguments_usage(prompt_content)
        
        return prompt_content
    
    def extract_and_embed_component_logic(self, components: List[str]) -> str:
        """Extract and embed only essential component logic directly into prompt."""
        embedded_logic = "## Essential Component Logic\n\n"
        logic_added = False
        
        # Priority components that add the most value
        priority_components = [
            "validation/input-validation.md",
            "workflow/command-execution.md", 
            "workflow/error-handling.md",
            "reasoning/react-reasoning.md",
            "reasoning/tree-of-thoughts.md"
        ]
        
        # Process priority components first
        for comp_path in components:
            if any(priority in comp_path for priority in priority_components):
                comp_content = self.load_component(comp_path)
                if comp_content and comp_content != f"<!-- Component not found: {comp_path} -->":
                    logic = self.extract_essential_component_logic(comp_content)
                    
                    comp_name = comp_path.split('/')[-1].replace('.md', '').replace('-', ' ').title()
                    
                    if logic["core_process"] or logic["key_criteria"] or logic["implementation"]:
                        embedded_logic += f"### {comp_name}\n"
                        
                        if logic["core_process"]:
                            embedded_logic += logic["core_process"] + "\n\n"
                        if logic["key_criteria"]:
                            embedded_logic += "**Key Criteria**: " + logic["key_criteria"] + "\n\n"
                        if logic["implementation"]:
                            embedded_logic += "**Implementation**: " + logic["implementation"] + "\n\n"
                        
                        logic_added = True
                        
                        # Limit embedded logic to keep file size reasonable
                        if len(embedded_logic) > 1500:
                            break
        
        return embedded_logic if logic_added else ""
    
    def inject_arguments_usage(self, content: str) -> str:
        """Inject proper $ARGUMENTS usage patterns throughout the content."""
        # Common argument patterns to replace with $ARGUMENTS usage
        arg_patterns = [
            (r'\{([^}]+)\}', r'$\1'),  # {variable} -> $VARIABLE
            (r'\$([a-z_]+)', lambda m: f'${m.group(1).upper()}'),  # $var -> $VAR
            (r'argument[:\s]+([a-zA-Z_]+)', r'$\1'),  # argument: name -> $NAME
        ]
        
        for pattern, replacement in arg_patterns:
            if callable(replacement):
                content = re.sub(pattern, replacement, content)
            else:
                content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        # Add argument usage examples in context
        if '$' not in content and 'argument' in content.lower():
            content += "\n\n**Argument Usage**: Access user input via $ARGUMENT_NAME variables throughout execution."
        
        return content
    
    def extract_essential_component_logic(self, content: str) -> Dict[str, str]:
        """Extract only the most essential logic from component content."""
        logic = {
            "core_process": "",
            "key_criteria": "",
            "implementation": ""
        }
        
        # Remove XML wrappers and comments
        content = re.sub(r'</?prompt_component[^>]*>', '', content)
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        
        # Extract core process steps
        step_matches = re.findall(r'<step[^>]*name=["\']([^"\'>]+)["\'][^>]*>(.*?)</step>', content, re.DOTALL)
        if step_matches:
            steps = []
            for name, step_content in step_matches[:3]:  # Limit to 3 key steps
                clean_step = re.sub(r'<[^>]+>', '', step_content)
                clean_step = re.sub(r'\s+', ' ', clean_step).strip()
                if len(clean_step) > 20:  # Only meaningful steps
                    steps.append(f"**{name}**: {clean_step[:200]}..." if len(clean_step) > 200 else f"**{name}**: {clean_step}")
            logic["core_process"] = '\n'.join(steps)
        
        # Extract key criteria or validation rules
        self._extract_criteria(content, logic)
        
        # Extract implementation patterns
        self._extract_implementation(content, logic)
        
        return logic
    
    def _extract_criteria(self, content: str, logic: Dict[str, str]) -> None:
        """Extract key criteria from content."""
        criteria_patterns = [
            r'<criteria[^>]*>(.*?)</criteria>',
            r'<validation[^>]*>(.*?)</validation>',
            r'<requirements[^>]*>(.*?)</requirements>'
        ]
        
        for pattern in criteria_patterns:
            matches = re.findall(pattern, content, re.DOTALL)
            for match in matches[:2]:  # Limit to 2 key criteria
                clean_criteria = re.sub(r'<[^>]+>', '', match)
                clean_criteria = re.sub(r'\s+', ' ', clean_criteria).strip()
                if len(clean_criteria) > 20:
                    logic["key_criteria"] += clean_criteria[:150] + "...\n" if len(clean_criteria) > 150 else clean_criteria + "\n"
    
    def _extract_implementation(self, content: str, logic: Dict[str, str]) -> None:
        """Extract implementation patterns from content."""
        impl_patterns = [
            r'<implementation[^>]*>(.*?)</implementation>',
            r'<process[^>]*>(.*?)</process>',
            r'<algorithm[^>]*>(.*?)</algorithm>'
        ]
        
        for pattern in impl_patterns:
            matches = re.findall(pattern, content, re.DOTALL)
            for match in matches[:1]:  # Only 1 key implementation
                clean_impl = re.sub(r'<[^>]+>', '', match)
                clean_impl = re.sub(r'\s+', ' ', clean_impl).strip()
                if len(clean_impl) > 20:
                    logic["implementation"] = clean_impl[:200] + "..." if len(clean_impl) > 200 else clean_impl
                break