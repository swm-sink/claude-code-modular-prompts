#!/usr/bin/env python3
"""
Markdown Generator Module

Handles generation of clean, human-readable markdown from processed command data.
"""

from typing import Dict, List, Any
from pathlib import Path


class MarkdownGenerator:
    """Generates clean markdown from command data."""
    
    def __init__(self):
        self.stats = {
            "lines_reduced": 0
        }
    
    def generate_clean_markdown(self, file_path: Path, frontmatter: Dict[str, str], xml_data: Dict[str, Any], original_content: str) -> str:
        """Generate clean, human-readable markdown command (50-80 lines target)."""
        
        original_lines = len(original_content.splitlines())
        
        # Build clean YAML frontmatter
        clean_frontmatter = {
            "name": f"/{file_path.stem}",
            "description": frontmatter.get('description', xml_data['metadata'].get('purpose', 'Command description')),
        }
        
        if frontmatter.get('argument-hint'):
            clean_frontmatter["usage"] = f"/{file_path.stem} {frontmatter['argument-hint']}"
        if frontmatter.get('allowed-tools'):
            clean_frontmatter["tools"] = frontmatter['allowed-tools']
        
        # Start building simplified content
        simplified = "---\n"
        for key, value in clean_frontmatter.items():
            simplified += f"{key}: {value}\n"
        simplified += "---\n\n"
        
        # Add concise description and usage
        description = clean_frontmatter["description"]
        simplified += f"# {description}\n\n"
        
        # Add usage with $ARGUMENTS
        simplified += self._generate_usage_section(file_path, xml_data, clean_frontmatter)
        
        # Add key arguments with $ARGUMENTS format
        if xml_data['arguments']:
            simplified += self._generate_arguments_section(xml_data)
        
        # Add top examples only
        if xml_data['examples']:
            simplified += self._generate_examples_section(xml_data)
        
        # Add core logic
        if xml_data['prompt']:
            simplified += self._generate_core_logic_section(xml_data)
        
        # Add execution pattern with $ARGUMENTS
        simplified += self._generate_execution_pattern()
        
        # Track line reduction
        final_lines = len(simplified.splitlines())
        self.stats["lines_reduced"] += max(0, original_lines - final_lines)
        
        return simplified
    
    def _generate_usage_section(self, file_path: Path, xml_data: Dict[str, Any], clean_frontmatter: Dict[str, str]) -> str:
        """Generate usage section with arguments."""
        if xml_data['arguments']:
            arg_usage = " ".join([f"${arg['name'].upper()}" for arg in xml_data['arguments'][:3]])  # Limit to 3 main args
            return f"**Usage**: `/{file_path.stem} {arg_usage}`\n\n"
        elif clean_frontmatter.get("usage"):
            return f"**Usage**: `{clean_frontmatter['usage']}`\n\n"
        return ""
    
    def _generate_arguments_section(self, xml_data: Dict[str, Any]) -> str:
        """Generate key arguments section."""
        section = "## Key Arguments\n\n"
        for arg in xml_data['arguments'][:4]:  # Limit to 4 key arguments
            status = "required" if arg['required'] else "optional"
            desc = arg['description'][:80] + "..." if len(arg['description']) > 80 else arg['description']
            section += f"- **${arg['name'].upper()}** ({status}): {desc}\n"
        section += "\n"
        return section
    
    def _generate_examples_section(self, xml_data: Dict[str, Any]) -> str:
        """Generate examples section."""
        section = "## Examples\n\n"
        for example in xml_data['examples'][:2]:  # Limit to 2 key examples
            section += f"```bash\n{example['usage']}\n```\n*{example['description']}*\n\n"
        return section
    
    def _generate_core_logic_section(self, xml_data: Dict[str, Any]) -> str:
        """Generate core logic section."""
        from .content_processor import ContentProcessor
        
        # Create a temporary content processor for this operation
        processor = ContentProcessor(Path("."))
        core_logic = processor.create_human_readable_prompt(xml_data['prompt'], xml_data['components'])
        
        # Truncate if too long to maintain 50-80 line target
        lines = core_logic.split('\n')
        if len(lines) > 30:  # Limit core logic to ~30 lines
            core_logic = '\n'.join(lines[:30]) + "\n\n*[Additional logic optimized for execution...]*"
        
        section = "## Core Logic\n\n"
        section += core_logic
        section += "\n\n"
        return section
    
    def _generate_execution_pattern(self) -> str:
        """Generate execution pattern section."""
        return """## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

"""
    
    def get_stats(self) -> Dict[str, int]:
        """Get current statistics."""
        return self.stats.copy()
    
    def reset_stats(self) -> None:
        """Reset statistics."""
        self.stats = {"lines_reduced": 0}