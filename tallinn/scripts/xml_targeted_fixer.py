#!/usr/bin/env python3
"""
Targeted XML fixer for specific malformation patterns in component files.
"""

import re
import logging
from pathlib import Path
from typing import List, Tuple, Dict
import defusedxml.ElementTree as ET

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger(__name__)


class TargetedXMLFixer:
    """Fix specific XML malformation patterns found in component files."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.components_dir = project_root / "claude_prompt_factory" / "components"
        self.fixes_applied = 0
        # Track specific files that need manual fixing
        self.problem_files = {
            "ecosystem/api-marketplace.md": self._fix_api_marketplace,
            "constitutional/constitutional-framework.md": self._fix_constitutional_framework,
            "orchestration/dag-orchestrator.md": self._fix_dag_orchestrator,
            "orchestration/agent-orchestration.md": self._fix_agent_orchestration,
            "orchestration/agent-swarm.md": self._fix_agent_swarm,
            "actions/parallel-execution.md": self._fix_parallel_execution,
            "quality/framework-validation.md": self._fix_framework_validation,
            "intelligence/cognitive-architecture.md": self._fix_cognitive_architecture,
            "performance/framework-optimization.md": self._fix_framework_optimization,
            "performance/auto-scaling.md": self._fix_auto_scaling,
            "community/community-platform.md": self._fix_community_platform,
            "error/circuit-breaker.md": self._fix_circuit_breaker,
            "validation/xml-structure.md": self._fix_xml_structure,
            "validation/input-validation.md": self._fix_input_validation,
            "analytics/business-intelligence.md": self._fix_business_intelligence,
            "analytics/user-feedback.md": self._fix_user_feedback,
            "reliability/chaos-engineering.md": self._fix_chaos_engineering,
            "deployment/ci-cd-integration.md": self._fix_ci_cd_integration
        }
        
    def _fix_api_marketplace(self, content: str) -> str:
        """Fix api-marketplace.md specific issues."""
        # Remove stray </name> tag on line 6
        content = re.sub(r'^</name>\s*', '', content, flags=re.MULTILINE)
        # Fix malformed comment
        content = re.sub(r'&lt;!-- API marketplace integration framework </ecosystem_integration>', 
                        '<!-- API marketplace integration framework --></ecosystem_integration>', content)
        # Ensure proper structure
        content = re.sub(r'<api_marketplace><ecosystem_integration>', 
                        '<api_marketplace>\n    <ecosystem_integration>', content)
        return content
    
    def _fix_constitutional_framework(self, content: str) -> str:
        """Fix constitutional-framework.md specific issues."""
        # Fix line 10 - move closing tag after parameters tag
        content = re.sub(r'</constitutional_approach>\s*<parameters>&lt;!-- Core Constitutional Design </parameters><constitutional_approach>',
                        '<parameters><!-- Core Constitutional Design --></parameters>\n      <constitutional_approach>', content)
        # Fix malformed comments
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        return content
    
    def _fix_dag_orchestrator(self, content: str) -> str:
        """Fix dag-orchestrator.md specific issues."""
        # Fix the complex comment issue on line 6
        content = re.sub(r'<dag_orchestrator><workflow_coordination></workflow_coordination><!-- <!-- Build DAG orchestrator.*?<!-- Build DAG orchestrator.*?\n',
                        '<dag_orchestrator>\n    <workflow_coordination><!-- Build DAG orchestrator for complex workflow coordination -->\n', 
                        content, flags=re.DOTALL)
        # Fix line 56 similar issue
        content = re.sub(r'<dynamic_execution></dynamic_execution><!-- Dynamic workflow execution.*?<!-- Dynamic workflow execution.*?\n',
                        '<dynamic_execution><!-- Dynamic workflow execution with real-time adaptation -->\n',
                        content, flags=re.DOTALL)
        # Fix line 113 
        content = re.sub(r'<enterprise_workflow_patterns></enterprise_workflow_patterns><!-- Enterprise-grade workflow patterns.*?<!-- Enterprise-grade workflow patterns.*?\n',
                        '<enterprise_workflow_patterns><!-- Enterprise-grade workflow patterns and templates -->\n',
                        content, flags=re.DOTALL)
        # Fix line 173
        content = re.sub(r'<integration_ecosystem></integration_ecosystem><!-- Integration with external systems.*?<!-- Integration with external systems.*?\n',
                        '<integration_ecosystem><!-- Integration with external systems and tools -->\n',
                        content, flags=re.DOTALL)
        return content
    
    def _fix_agent_orchestration(self, content: str) -> str:
        """Fix agent-orchestration.md specific issues."""
        # Similar pattern to dag-orchestrator
        content = re.sub(r'<(\w+)></\1><!--', r'<\1><!--', content)
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        return content
    
    def _fix_agent_swarm(self, content: str) -> str:
        """Fix agent-swarm.md specific issues."""
        content = re.sub(r'<(\w+)></\1><!--', r'<\1><!--', content)
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        return content
    
    def _fix_parallel_execution(self, content: str) -> str:
        """Fix parallel-execution.md specific issues."""
        content = re.sub(r'<(\w+)></\1>(?=<)', r'<\1>', content)
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        return content
    
    def _fix_framework_validation(self, content: str) -> str:
        """Fix framework-validation.md specific issues."""
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        content = re.sub(r'<(\w+)></\1><!--', r'<\1><!--', content)
        return content
    
    def _fix_cognitive_architecture(self, content: str) -> str:
        """Fix cognitive-architecture.md specific issues."""
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        content = re.sub(r'<(\w+)></\1><!--', r'<\1><!--', content)
        return content
    
    def _fix_framework_optimization(self, content: str) -> str:
        """Fix framework-optimization.md specific issues."""
        # Find and fix mismatched tags
        content = re.sub(r'</(\w+)>\s*<\1>', r'<\1>', content)
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        return content
    
    def _fix_auto_scaling(self, content: str) -> str:
        """Fix auto-scaling.md specific issues."""
        content = re.sub(r'<(\w+)></\1><!--', r'<\1><!--', content)
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        return content
    
    def _fix_community_platform(self, content: str) -> str:
        """Fix community-platform.md specific issues."""
        content = re.sub(r'</description>\s*</step>\s*<step>', r'</description>\n  </step>\n  <step>', content)
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        return content
    
    def _fix_circuit_breaker(self, content: str) -> str:
        """Fix circuit-breaker.md specific issues."""
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        content = re.sub(r'<(\w+)></\1><!--', r'<\1><!--', content)
        return content
    
    def _fix_xml_structure(self, content: str) -> str:
        """Fix xml-structure.md specific issues."""
        # Fix mismatched closing tags
        content = re.sub(r'</(\w+)>\s*</step>', r'</\1>\n  </step>', content)
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        return content
    
    def _fix_input_validation(self, content: str) -> str:
        """Fix input-validation.md specific issues."""
        # Find orphaned closing tags and remove them
        content = re.sub(r'^\s*</(\w+)>\s*$', '', content, flags=re.MULTILINE)
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        return content
    
    def _fix_business_intelligence(self, content: str) -> str:
        """Fix business-intelligence.md specific issues."""
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        content = re.sub(r'<(\w+)></\1><!--', r'<\1><!--', content)
        return content
    
    def _fix_user_feedback(self, content: str) -> str:
        """Fix user-feedback.md specific issues."""
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        content = re.sub(r'<(\w+)></\1><!--', r'<\1><!--', content)
        return content
    
    def _fix_chaos_engineering(self, content: str) -> str:
        """Fix chaos-engineering.md specific issues."""
        content = re.sub(r'</description>\s*</step>\s*<step>', r'</description>\n  </step>\n  <step>', content)
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        return content
    
    def _fix_ci_cd_integration(self, content: str) -> str:
        """Fix ci-cd-integration.md specific issues."""
        content = re.sub(r'&lt;!--', '<!--', content)
        content = re.sub(r'--&gt;', '-->', content)
        content = re.sub(r'<(\w+)></\1><!--', r'<\1><!--', content)
        return content
    
    def fix_file(self, file_path: Path, custom_fixer=None) -> bool:
        """Fix XML issues in a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply custom fixer if available
            if custom_fixer:
                content = custom_fixer(content)
            
            # Apply general fixes
            content = self._apply_general_fixes(content)
            
            if content != original_content:
                # Write fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.fixes_applied += 1
                
                # Validate the fixed content
                try:
                    ET.fromstring(content)
                    logger.info(f"✅ Successfully fixed and validated: {file_path}")
                    return True
                except ET.ParseError as e:
                    logger.error(f"❌ Fixed but still invalid: {file_path} - {e}")
                    return False
            else:
                logger.info(f"No changes needed: {file_path}")
                return True
                
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return False
    
    def _apply_general_fixes(self, content: str) -> str:
        """Apply general XML fixes."""
        # Fix escaped HTML entities in comments
        content = re.sub(r'&lt;', '<', content)
        content = re.sub(r'&gt;', '>', content)
        content = re.sub(r'&amp;', '&', content)
        
        # Ensure proper XML structure
        if not content.strip().startswith('<prompt_component>'):
            # Already has proper root, don't add another
            pass
        
        # Fix common tag issues
        content = re.sub(r'</(\w+)></\1>', r'</\1>', content)  # Remove duplicate closing tags
        content = re.sub(r'<(\w+)></\1>(?=<\w)', r'<\1>', content)  # Remove empty self-closing patterns
        
        return content
    
    def fix_problem_files(self) -> Tuple[int, int]:
        """Fix all known problem files with targeted fixes."""
        successful = 0
        failed = 0
        
        logger.info(f"Processing {len(self.problem_files)} problem files with targeted fixes")
        
        for relative_path, fixer_func in self.problem_files.items():
            file_path = self.components_dir / relative_path
            if file_path.exists():
                if self.fix_file(file_path, fixer_func):
                    successful += 1
                else:
                    failed += 1
            else:
                logger.warning(f"File not found: {file_path}")
                failed += 1
        
        return successful, failed


def main():
    """Main execution."""
    project_root = Path(__file__).parent.parent
    fixer = TargetedXMLFixer(project_root)
    
    logger.info("Starting targeted XML fix process...")
    successful, failed = fixer.fix_problem_files()
    
    logger.info(f"\n=== Targeted Fix Summary ===")
    logger.info(f"Files processed: {successful + failed}")
    logger.info(f"Successfully fixed: {successful}")
    logger.info(f"Failed to fix: {failed}")
    logger.info(f"Total fixes applied: {fixer.fixes_applied}")
    
    if failed > 0:
        logger.warning(f"⚠️ {failed} files still have issues and need manual review")
        return 1
    else:
        logger.info("✅ All problem files successfully fixed!")
        return 0


if __name__ == "__main__":
    exit(main())