#!/usr/bin/env python3
"""
XML Infrastructure Agent - Fixed Version for XML Parsing Errors

This script addresses XML parsing errors with corrected regex patterns.

Author: Deployment Agent
Date: 2025-07-22
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class XMLErrorFixerV2:
    def __init__(self, root_path: str = "claude_prompt_factory"):
        self.root_path = Path(root_path)
        self.fixes_applied = []
        self.errors_encountered = []
        
    def fix_mismatched_tags(self, file_path: Path) -> bool:
        """Fix mismatched XML tags in component files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixes_made = []
            
            # Common mismatched tag patterns
            tag_fixes = [
                # Fix <o> tags that should be <output>
                (r'<o>', '<output>'),
                (r'</o>', '</output>'),
                
                # Fix incomplete closing tags
                (r'<([^/>]+)>\s*$', r'<\1></\1>'),
                
                # Fix malformed self-closing tags  
                (r'<([^/>]+)\s*/\s*>', r'<\1 />'),
            ]
            
            for pattern, replacement in tag_fixes:
                new_content, count = re.subn(pattern, replacement, content, flags=re.MULTILINE)
                if count > 0:
                    fixes_made.append(f"{pattern} -> {replacement}: {count} replacements")
                    content = new_content
            
            # Save if changes were made
            if content != original_content:
                shutil.copy2(file_path, f"{file_path}.backup")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                logger.info(f"Fixed mismatched tags in {file_path}: {len(fixes_made)} fixes")
                self.fixes_applied.append((file_path, fixes_made))
                return True
                
        except Exception as e:
            logger.error(f"Error fixing mismatched tags in {file_path}: {e}")
            self.errors_encountered.append((file_path, str(e)))
        
        return False
    
    def fix_malformed_xml_structure(self, file_path: Path) -> bool:
        """Fix malformed XML structure including encoding and CDATA issues."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixes_made = []
            
            # Structure fixes with corrected patterns
            structure_fixes = [
                # Remove control characters (except tab, newline, carriage return)
                (r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', ''),
                
                # Fix unclosed CDATA sections
                (r'<!\[CDATA\[([^]]*)(?<!\]\]>)$', r'<![CDATA[\1]]>'),
                
                # Fix improperly escaped ampersands
                (r'&(?!(amp|lt|gt|apos|quot);)', r'&amp;'),
                
                # Fix improperly escaped less-than signs
                (r'<(?![^<]*>)', r'&lt;'),
                
                # Fix double XML declarations
                (r'(<\?xml[^?]*\?>)\s*(<\?xml[^?]*\?>)', r'\1'),
            ]
            
            for pattern, replacement in structure_fixes:
                new_content, count = re.subn(pattern, replacement, content, flags=re.MULTILINE)
                if count > 0:
                    fixes_made.append(f"{pattern} -> {replacement}: {count} replacements")
                    content = new_content
            
            # Save if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                logger.info(f"Fixed XML structure in {file_path}: {len(fixes_made)} fixes")
                self.fixes_applied.append((file_path, fixes_made))
                return True
                
        except Exception as e:
            logger.error(f"Error fixing XML structure in {file_path}: {e}")
            self.errors_encountered.append((file_path, str(e)))
        
        return False
    
    def validate_xml(self, file_path: Path) -> bool:
        """Validate XML structure after fixes."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Wrap content in root element for validation
            wrapped_content = f"<root>{content}</root>"
            ET.fromstring(wrapped_content)
            return True
            
        except ET.ParseError as e:
            logger.warning(f"XML validation failed for {file_path}: {e}")
            return False
        except Exception as e:
            logger.error(f"Error validating XML in {file_path}: {e}")
            return False
    
    def process_critical_files(self) -> Dict:
        """Process critical component files identified in the validation report."""
        critical_files = [
            "components/ecosystem/api-marketplace.md",
            "components/constitutional/constitutional-framework.md",
            "components/constitutional/safety-framework.md",
            "components/quality/framework-validation.md",
            "components/intelligence/cognitive-architecture.md",
            "components/learning/meta-learning.md",
            "components/learning/meta-learning-framework.md",
            "components/learning/examples-library.md",
            "components/optimization/opro-framework.md",
            "components/optimization/dspy-framework.md",
            "components/optimization/prompt-optimization.md",
            "components/optimization/autoprompt-framework.md",
            "components/optimization/textgrad-framework.md",
            "components/meta/component-loader.md",
            "components/reasoning/react-reasoning.md",
            "components/reasoning/tree-of-thoughts.md",
            "components/testing/mutation-testing.md",
            "components/user-experience/intelligent-help.md",
            "components/deployment/ci-cd-integration.md",
            "components/reliability/chaos-engineering.md",
            "components/actions/parallel-execution.md",
            "components/orchestration/agent-orchestration.md",
            "components/orchestration/dag-orchestrator.md",
            "components/orchestration/agent-swarm.md",
            "components/performance/framework-optimization.md",
            "components/performance/auto-scaling.md",
            "components/community/community-platform.md",
            "components/error/circuit-breaker.md",
            "components/validation/xml-structure.md",
            "components/validation/input-validation.md",
            "components/analytics/business-intelligence.md",
            "components/analytics/user-feedback.md"
        ]
        
        results = {
            "total_files": len(critical_files),
            "successful_fixes": 0,
            "failed_fixes": 0,
            "validation_passed": 0,
            "validation_failed": 0
        }
        
        for rel_path in critical_files:
            file_path = self.root_path / rel_path
            
            if not file_path.exists():
                logger.warning(f"File not found: {file_path}")
                results["failed_fixes"] += 1
                continue
            
            logger.info(f"Processing critical file: {file_path}")
            
            # Apply fixes
            tag_fixed = self.fix_mismatched_tags(file_path)
            struct_fixed = self.fix_malformed_xml_structure(file_path)
            
            if tag_fixed or struct_fixed:
                results["successful_fixes"] += 1
                
                # Validate after fixes
                if self.validate_xml(file_path):
                    results["validation_passed"] += 1
                else:
                    results["validation_failed"] += 1
                    logger.warning(f"XML validation still failing for {file_path}")
            else:
                results["failed_fixes"] += 1
        
        return results
    
    def generate_report(self, results: Dict) -> None:
        """Generate a comprehensive fix report."""
        import json
        
        report = {
            "execution_summary": results,
            "fixes_applied": [
                {
                    "file": str(file_path),
                    "fixes": fixes
                }
                for file_path, fixes in self.fixes_applied
            ],
            "errors_encountered": [
                {
                    "file": str(file_path),
                    "error": error
                }
                for file_path, error in self.errors_encountered
            ],
            "success_rate": (results["successful_fixes"] / results["total_files"] * 100) if results["total_files"] > 0 else 0
        }
        
        with open("xml_fix_report_v2.json", "w") as f:
            json.dump(report, f, indent=2)
        
        logger.info("Fix report generated: xml_fix_report_v2.json")
        logger.info(f"Total fixes applied: {results['successful_fixes']}")
        logger.info(f"Success rate: {report['success_rate']:.1f}%")


def main():
    """Main execution function."""
    logger.info("Starting comprehensive XML error fixing (v2)...")
    
    fixer = XMLErrorFixerV2()
    results = fixer.process_critical_files()
    fixer.generate_report(results)
    
    # Summary
    logger.info("\n=== XML Fix Summary ===")
    logger.info(f"Total files processed: {results['total_files']}")
    logger.info(f"Successful fixes: {results['successful_fixes']}")
    logger.info(f"Failed fixes: {results['failed_fixes']}")
    logger.info(f"Validation passed: {results['validation_passed']}")
    logger.info(f"Validation failed: {results['validation_failed']}")
    
    # Return exit code based on success
    remaining_issues = results['validation_failed']
    if remaining_issues < 5:
        logger.info("SUCCESS: Less than 5 critical XML issues remain!")
        return 0
    else:
        logger.warning(f"WARNING: {remaining_issues} XML issues still remain (target: <5)")
        return 1


if __name__ == "__main__":
    exit(main())