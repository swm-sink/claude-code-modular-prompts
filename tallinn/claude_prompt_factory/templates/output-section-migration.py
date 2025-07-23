#!/usr/bin/env python3
"""
Output Section Migration Script for Claude Code Prompt Factory
Adds missing <output> sections to components based on intelligent analysis.
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OutputSectionMigrator:
    def __init__(self, root_path: str = "claude_prompt_factory"):
        self.root_path = Path(root_path)
        self.component_patterns = {
            'analysis': {
                'primary': 'Analysis Results',
                'format': 'Structured analysis report with findings, metrics, and recommendations',
                'categories': ['Findings', 'Metrics', 'Recommendations']
            },
            'context': {
                'primary': 'Context Information',
                'format': 'Contextualized data with relevance scoring and integration points',
                'categories': ['Context Data', 'Relevance Score', 'Integration Points']
            },
            'optimization': {
                'primary': 'Optimization Results',
                'format': 'Performance improvements with before/after metrics and implementation details',
                'categories': ['Performance Gains', 'Implementation Details', 'Validation Results']
            },
            'orchestration': {
                'primary': 'Orchestration Status',
                'format': 'Coordination results with agent statuses and workflow state',
                'categories': ['Agent Status', 'Workflow State', 'Coordination Results']
            },
            'testing': {
                'primary': 'Test Results',
                'format': 'Test execution results with coverage metrics and failure analysis',
                'categories': ['Test Results', 'Coverage Metrics', 'Issue Analysis']
            },
            'security': {
                'primary': 'Security Assessment',
                'format': 'Security analysis with vulnerability findings and remediation guidance',
                'categories': ['Security Status', 'Vulnerabilities', 'Remediation Plan']
            },
            'workflow': {
                'primary': 'Workflow Status',
                'format': 'Workflow execution status with step completion and next actions',
                'categories': ['Execution Status', 'Step Progress', 'Next Actions']
            },
            'deployment': {
                'primary': 'Deployment Status',
                'format': 'Deployment results with environment status and validation checks',
                'categories': ['Deployment Status', 'Environment Health', 'Validation Results']
            },
            'git': {
                'primary': 'Git Operation Results',
                'format': 'Version control operation results with commit details and status',
                'categories': ['Operation Status', 'Commit Details', 'Repository State']
            }
        }
        
    def analyze_component_type(self, file_path: Path, content: str) -> str:
        """Analyze component to determine its type and appropriate output pattern."""
        path_parts = file_path.parts
        
        # Determine type from directory structure
        for part in path_parts:
            if part in self.component_patterns:
                return part
                
        # Analyze content for type hints
        content_lower = content.lower()
        
        type_keywords = {
            'analysis': ['analyze', 'assess', 'evaluate', 'examine', 'review'],
            'context': ['context', 'memory', 'session', 'state', 'history'],
            'optimization': ['optimize', 'improve', 'enhance', 'performance', 'efficiency'],
            'orchestration': ['orchestrate', 'coordinate', 'agent', 'swarm', 'multi'],
            'testing': ['test', 'verify', 'validate', 'check', 'quality'],
            'security': ['secure', 'audit', 'vulnerability', 'compliance', 'owasp'],
            'workflow': ['workflow', 'pipeline', 'execution', 'schedule', 'flow'],
            'deployment': ['deploy', 'provision', 'infrastructure', 'environment'],
            'git': ['git', 'commit', 'merge', 'branch', 'repository']
        }
        
        for comp_type, keywords in type_keywords.items():
            if any(keyword in content_lower for keyword in keywords):
                return comp_type
                
        return 'analysis'  # Default fallback
        
    def generate_output_section(self, file_path: Path, content: str) -> str:
        """Generate an appropriate output section based on component analysis."""
        comp_type = self.analyze_component_type(file_path, content)
        pattern = self.component_patterns[comp_type]
        
        # Extract component name from step element if available
        comp_name = "Component Operation"
        step_match = re.search(r'<step name="([^"]+)">', content)
        if step_match:
            comp_name = step_match.group(1)
        
        output_section = f"""
    <output>
      {comp_name} completed with structured results:
      
      **{pattern['categories'][0]}**:
      - Status: [Success/Warning/Error] with detailed status information
      - Results: {pattern['format']}
      - Validation: Quality metrics and completion verification
      
      **{pattern['categories'][1]}**:
      - Metrics: Performance and efficiency measurements
      - Details: Comprehensive technical information and specifications
      - Context: Integration points and dependency information
      
      **{pattern['categories'][2]}**:
      - Recommendations: Next steps and optimization opportunities
      - Actions: Required follow-up tasks and integration steps
      - Quality Assurance: Validation checkpoints and success criteria
      
      **Behavioral Guidelines**:
      - Provide consistent, structured output matching the specified format
      - Include comprehensive metadata for downstream processing
      - Maintain clear status indicators (✅ Success, ⚠️ Warning, ❌ Error)
      - Always validate output completeness before finishing
    </output>"""
        
        return output_section
        
    def add_output_section(self, file_path: Path) -> Dict[str, any]:
        """Add missing output section to a component file."""
        result = {
            "file": str(file_path),
            "success": False,
            "action": "none",
            "errors": []
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if output section already exists
            if '<output>' in content or '<output_format>' in content:
                result["action"] = "already_exists"
                result["success"] = True
                return result
                
            # Find the insertion point (before closing tags)
            insertion_patterns = [
                (r'(\s*)</step>', r'\1OUTPUT_SECTION\1</step>'),
                (r'(\s*)</prompt_component>', r'\1OUTPUT_SECTION\1</prompt_component>'),
                (r'(\s*$)', r'\1OUTPUT_SECTION')
            ]
            
            output_section = self.generate_output_section(file_path, content)
            
            for pattern, replacement in insertion_patterns:
                if re.search(pattern.replace('OUTPUT_SECTION', ''), content):
                    new_content = re.sub(pattern, replacement.replace('OUTPUT_SECTION', output_section), content)
                    
                    # Write the updated content
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    result["success"] = True
                    result["action"] = "added"
                    logging.info(f"Added output section to {file_path}")
                    break
                    
            if not result["success"]:
                result["errors"].append("Could not find suitable insertion point")
                
        except Exception as e:
            result["errors"].append(f"Migration failed: {str(e)}")
            
        return result
        
    def migrate_all_missing_outputs(self) -> Dict[str, any]:
        """Add output sections to all components missing them."""
        summary = {
            "total_files_processed": 0,
            "sections_added": 0,
            "already_exists": 0,
            "failed": 0,
            "results": []
        }
        
        components_dir = self.root_path / "components"
        if components_dir.exists():
            for comp_file in components_dir.rglob("*.md"):
                if comp_file.name != "README.md":
                    result = self.add_output_section(comp_file)
                    summary["results"].append(result)
                    summary["total_files_processed"] += 1
                    
                    if result["action"] == "added":
                        summary["sections_added"] += 1
                    elif result["action"] == "already_exists":
                        summary["already_exists"] += 1
                    else:
                        summary["failed"] += 1
                        
        return summary
        
    def generate_migration_report(self, summary: Dict) -> str:
        """Generate output section migration report."""
        report = []
        report.append("# Output Section Migration Report")
        report.append(f"**Generated**: {__import__('datetime').datetime.now().isoformat()}")
        report.append("")
        
        # Summary
        report.append("## Executive Summary")
        report.append(f"- **Files Processed**: {summary['total_files_processed']}")
        report.append(f"- **Output Sections Added**: {summary['sections_added']}")
        report.append(f"- **Already Had Outputs**: {summary['already_exists']}")
        report.append(f"- **Failed Migrations**: {summary['failed']}")
        
        completion_rate = ((summary['sections_added'] + summary['already_exists']) / summary['total_files_processed'] * 100) if summary['total_files_processed'] > 0 else 0
        report.append(f"- **Completion Rate**: {completion_rate:.1f}%")
        report.append("")
        
        # Files with added sections
        if summary['sections_added'] > 0:
            report.append("## ✅ Output Sections Added")
            for result in summary["results"]:
                if result["action"] == "added":
                    report.append(f"- **{result['file']}**: Output section successfully added")
            report.append("")
            
        # Failed migrations
        if summary['failed'] > 0:
            report.append("## ❌ Failed Migrations")
            for result in summary["results"]:
                if result["action"] == "none" and result["errors"]:
                    report.append(f"### {result['file']}")
                    for error in result["errors"]:
                        report.append(f"- ❌ {error}")
                    report.append("")
        
        return "\n".join(report)

def main():
    """Main migration function."""
    migrator = OutputSectionMigrator()
    summary = migrator.migrate_all_missing_outputs()
    report = migrator.generate_migration_report(summary)
    
    # Save report
    with open("output_section_migration_report.md", "w") as f:
        f.write(report)
        
    print(f"Output section migration complete. {summary['sections_added']} sections added to components.")
    print("Report saved to output_section_migration_report.md")

if __name__ == "__main__":
    main()