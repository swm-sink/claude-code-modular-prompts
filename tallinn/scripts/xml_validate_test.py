#!/usr/bin/env python3
"""
Simple XML validation test to check if files are now parseable
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_xml_file(file_path):
    """Try to parse XML file and return if it's valid."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Wrap in root element for validation
        wrapped_content = f"<root>{content}</root>"
        ET.fromstring(wrapped_content)
        return True, None
    except ET.ParseError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def main():
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
    
    valid_count = 0
    invalid_count = 0
    
    logger.info(f"Validating {len(critical_files)} critical XML files...")
    
    for file_path in critical_files:
        path = Path(file_path)
        if path.exists():
            is_valid, error = validate_xml_file(path)
            if is_valid:
                valid_count += 1
            else:
                invalid_count += 1
                logger.error(f"❌ {file_path}: {error}")
        else:
            invalid_count += 1
            logger.error(f"❌ {file_path}: File not found")
    
    logger.info(f"\n=== XML Validation Summary ===")
    logger.info(f"Valid XML files: {valid_count}")
    logger.info(f"Invalid XML files: {invalid_count}")
    logger.info(f"Total critical issues remaining: {invalid_count}")
    
    if invalid_count < 5:
        logger.info("✅ SUCCESS: Less than 5 critical XML issues remain!")
        return 0
    else:
        logger.warning(f"⚠️ WARNING: {invalid_count} XML issues remain (target: <5)")
        return 1

if __name__ == "__main__":
    exit(main())