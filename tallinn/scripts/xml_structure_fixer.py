#!/usr/bin/env python3
"""
XML Structure Fixer - Fix empty tags and structural issues

This script fixes empty self-closing tags that should contain content,
and other structural XML issues.

Author: Deployment Agent
Date: 2025-07-22
"""

import os
import re
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def fix_empty_tags(content):
    """Fix empty tags that should contain content."""
    # Pattern to find empty tags followed by content
    # e.g., <description></description>\n    Content here
    pattern = r'<(\w+)><\/\1>\s*\n\s*([^<]+)'
    
    def replacer(match):
        tag = match.group(1)
        content_text = match.group(2).strip()
        return f'<{tag}>{content_text}</{tag}>'
    
    return re.sub(pattern, replacer, content, flags=re.MULTILINE)


def fix_self_closing_root_tags(content):
    """Fix self-closing tags that should wrap content."""
    # Fix <prompt_component></prompt_component> at the start
    if content.startswith('<prompt_component></prompt_component>'):
        # Find the matching closing tag at the end
        if '</prompt_component>' in content[100:]:  # Skip the first occurrence
            # Remove the empty tag at the start
            content = content.replace('<prompt_component></prompt_component>', '<prompt_component>', 1)
        else:
            # No closing tag found, wrap the entire content
            content = content.replace('<prompt_component></prompt_component>', '<prompt_component>')
            content = content.rstrip() + '\n</prompt_component>'
    
    return content


def fix_nested_empty_tags(content):
    """Fix nested structures with empty tags."""
    # Fix patterns like:
    # <tag></tag>
    #   Content
    # </tag>
    
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        # Check if this line has an empty tag
        empty_tag_match = re.match(r'^\s*<(\w+)><\/\1>\s*$', line)
        
        if empty_tag_match and i + 1 < len(lines):
            tag_name = empty_tag_match.group(1)
            next_line = lines[i + 1]
            
            # Check if next line has content (not another tag)
            if next_line.strip() and not next_line.strip().startswith('<'):
                # Combine the tag with its content
                indent = ' ' * (len(line) - len(line.lstrip()))
                fixed_lines.append(f'{indent}<{tag_name}>{next_line.strip()}</{tag_name}>')
                i += 2  # Skip the content line
                continue
        
        fixed_lines.append(line)
        i += 1
    
    return '\n'.join(fixed_lines)


def process_xml_file(file_path):
    """Process a single XML file to fix structural issues."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply fixes in order
        content = fix_self_closing_root_tags(content)
        content = fix_empty_tags(content)
        content = fix_nested_empty_tags(content)
        
        # Save if changes were made
        if content != original_content:
            # Create backup if it doesn't exist
            backup_path = f"{file_path}.structure_backup"
            if not os.path.exists(backup_path):
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(original_content)
            
            # Save fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"Fixed structural issues in {file_path}")
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main execution function."""
    critical_files = [
        "claude_prompt_factory/components/ecosystem/api-marketplace.md",
        "claude_prompt_factory/components/constitutional/constitutional-framework.md",
        "claude_prompt_factory/components/constitutional/safety-framework.md",
        "claude_prompt_factory/components/quality/framework-validation.md",
        "claude_prompt_factory/components/intelligence/cognitive-architecture.md",
        "claude_prompt_factory/components/learning/meta-learning.md",
        "claude_prompt_factory/components/learning/meta-learning-framework.md",
        "claude_prompt_factory/components/learning/examples-library.md",
        "claude_prompt_factory/components/optimization/opro-framework.md",
        "claude_prompt_factory/components/optimization/dspy-framework.md",
        "claude_prompt_factory/components/optimization/prompt-optimization.md",
        "claude_prompt_factory/components/optimization/autoprompt-framework.md",
        "claude_prompt_factory/components/optimization/textgrad-framework.md",
        "claude_prompt_factory/components/meta/component-loader.md",
        "claude_prompt_factory/components/reasoning/react-reasoning.md",
        "claude_prompt_factory/components/reasoning/tree-of-thoughts.md",
        "claude_prompt_factory/components/testing/mutation-testing.md",
        "claude_prompt_factory/components/user-experience/intelligent-help.md",
        "claude_prompt_factory/components/deployment/ci-cd-integration.md",
        "claude_prompt_factory/components/reliability/chaos-engineering.md",
        "claude_prompt_factory/components/actions/parallel-execution.md",
        "claude_prompt_factory/components/orchestration/agent-orchestration.md",
        "claude_prompt_factory/components/orchestration/dag-orchestrator.md",
        "claude_prompt_factory/components/orchestration/agent-swarm.md",
        "claude_prompt_factory/components/performance/framework-optimization.md",
        "claude_prompt_factory/components/performance/auto-scaling.md",
        "claude_prompt_factory/components/community/community-platform.md",
        "claude_prompt_factory/components/error/circuit-breaker.md",
        "claude_prompt_factory/components/validation/xml-structure.md",
        "claude_prompt_factory/components/validation/input-validation.md",
        "claude_prompt_factory/components/analytics/business-intelligence.md",
        "claude_prompt_factory/components/analytics/user-feedback.md"
    ]
    
    logger.info("Starting XML structure fixing...")
    
    fixed_count = 0
    for file_path in critical_files:
        path = Path(file_path)
        if path.exists():
            if process_xml_file(path):
                fixed_count += 1
        else:
            logger.warning(f"File not found: {file_path}")
    
    logger.info(f"\n=== XML Structure Fix Summary ===")
    logger.info(f"Files processed: {len(critical_files)}")
    logger.info(f"Files fixed: {fixed_count}")
    
    return 0


if __name__ == "__main__":
    exit(main())