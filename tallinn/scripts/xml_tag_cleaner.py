#!/usr/bin/env python3
"""
XML Tag Cleaner - Fix malformed closing tags

This script specifically addresses the issue where closing tags incorrectly 
repeat their attributes, e.g. </step name="..."> instead of </step>

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


def fix_malformed_closing_tags(file_path):
    """Fix closing tags that incorrectly include attributes."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix closing tags that have attributes (they shouldn't)
        # Pattern matches </tagname anything> and replaces with </tagname>
        pattern = r'</(\w+)[^>]*>'
        replacement = r'</\1>'
        
        content = re.sub(pattern, replacement, content)
        
        # Count fixes
        fixes_count = len(re.findall(pattern, original_content))
        
        if content != original_content:
            # Save backup
            backup_path = f"{file_path}.xml_backup"
            if not os.path.exists(backup_path):
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(original_content)
            
            # Save fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"Fixed {fixes_count} malformed closing tags in {file_path}")
            return True, fixes_count
        
        return False, 0
        
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        return False, 0


def process_critical_files():
    """Process all critical component files."""
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
    
    total_files = len(critical_files)
    files_fixed = 0
    total_fixes = 0
    
    logger.info(f"Processing {total_files} critical files...")
    
    for file_path in critical_files:
        path = Path(file_path)
        if path.exists():
            fixed, count = fix_malformed_closing_tags(path)
            if fixed:
                files_fixed += 1
                total_fixes += count
        else:
            logger.warning(f"File not found: {file_path}")
    
    logger.info(f"\n=== XML Tag Cleaning Summary ===")
    logger.info(f"Total files processed: {total_files}")
    logger.info(f"Files fixed: {files_fixed}")
    logger.info(f"Total malformed tags fixed: {total_fixes}")
    
    return files_fixed, total_fixes


def main():
    """Main execution function."""
    logger.info("Starting XML tag cleaning...")
    
    files_fixed, total_fixes = process_critical_files()
    
    # Process all component files if requested
    all_components = Path("claude_prompt_factory/components").rglob("*.md")
    additional_fixed = 0
    additional_fixes = 0
    
    for component in all_components:
        fixed, count = fix_malformed_closing_tags(component)
        if fixed:
            additional_fixed += 1
            additional_fixes += count
    
    logger.info(f"\n=== Final Summary ===")
    logger.info(f"Critical files fixed: {files_fixed}")
    logger.info(f"Additional files fixed: {additional_fixed}")
    logger.info(f"Total malformed tags fixed: {total_fixes + additional_fixes}")
    
    return 0


if __name__ == "__main__":
    exit(main())