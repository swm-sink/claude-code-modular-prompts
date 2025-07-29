#!/usr/bin/env python3
"""
Template Validation System for Claude Code Prompt Factory

Validates that commands and components follow standardized templates and patterns.
Ensures consistency across the entire codebase for DRY principles.
"""

import os
import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Tuple, Optional
from pathlib import Path

class TemplateValidator:
    def __init__(self, root_path: str = "claude_prompt_factory"):
        self.root_path = Path(root_path)
        self.results = []
        
    def validate_command(self, file_path: Path) -> Dict[str, any]:
        """Validate a command file against the standard template."""
        result = {
            "file": str(file_path),
            "type": "command",
            "valid": True,
            "errors": [],
            "warnings": [],
            "score": 0,
            "max_score": 100
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check YAML frontmatter
            yaml_score = self._check_yaml_frontmatter(content, result)
            
            # Check XML structure 
            xml_score = self._check_xml_structure(content, result, "command")
            
            # Check component includes
            includes_score = self._check_component_includes(content, result)
            
            # Check dependencies section
            deps_score = self._check_dependencies_section(content, result)
            
            result["score"] = yaml_score + xml_score + includes_score + deps_score
            
        except Exception as e:
            result["valid"] = False
            result["errors"].append(f"File read error: {str(e)}")
            
        return result
        
    def validate_component(self, file_path: Path) -> Dict[str, any]:
        """Validate a component file against the standard template."""
        result = {
            "file": str(file_path),
            "type": "component", 
            "valid": True,
            "errors": [],
            "warnings": [],
            "score": 0,
            "max_score": 100
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check XML structure
            xml_score = self._check_xml_structure(content, result, "component")
            
            # Check component structure
            structure_score = self._check_component_structure(content, result)
            
            # Check output format
            output_score = self._check_output_format(content, result)
            
            result["score"] = xml_score + structure_score + output_score
            
        except Exception as e:
            result["valid"] = False
            result["errors"].append(f"File read error: {str(e)}")
            
        return result
        
    def _check_yaml_frontmatter(self, content: str, result: Dict) -> int:
        """Check YAML frontmatter in command files."""
        score = 0
        yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        
        if not yaml_match:
            result["errors"].append("Missing YAML frontmatter")
            return 0
            
        yaml_content = yaml_match.group(1)
        
        # Required fields
        required_fields = ["description:", "argument-hint:", "allowed-tools:"]
        for field in required_fields:
            if field in yaml_content:
                score += 8  # 24 points for required fields
            else:
                result["errors"].append(f"Missing required YAML field: {field}")
                
        return score
        
    def _check_xml_structure(self, content: str, result: Dict, file_type: str) -> int:
        """Check XML structure validity."""
        score = 0
        
        if file_type == "command":
            # Extract just the XML portion for commands
            xml_match = re.search(r'<command_file>.*?</command_file>', content, re.DOTALL)
            if not xml_match:
                result["errors"].append("Missing <command_file> XML structure")
                return 0
            xml_content = xml_match.group(0)
        else:
            # Components should be pure XML
            xml_content = content
            
        try:
            ET.fromstring(xml_content)
            score += 25  # Valid XML structure
        except ET.ParseError as e:
            result["errors"].append(f"XML Parse Error: {str(e)}")
            return 0
            
        return score
        
    def _check_component_includes(self, content: str, result: Dict) -> int:
        """Check component includes are properly formatted and exist."""
        score = 0
        
        # Find all component includes
        includes = re.findall(r'<include component="([^"]+)" />', content)
        
        if includes:
            score += 15  # Has component includes
            
            # Check if included components exist
            for include_path in includes:
                full_path = self.root_path / include_path
                if full_path.exists():
                    score += 2  # Each valid include
                else:
                    result["warnings"].append(f"Component not found: {include_path}")
                    
        return min(score, 25)  # Cap at 25 points
        
    def _check_dependencies_section(self, content: str, result: Dict) -> int:
        """Check dependencies section matches actual includes."""
        score = 0
        
        # Extract dependencies section
        deps_match = re.search(r'<includes_components>(.*?)</includes_components>', content, re.DOTALL)
        if deps_match:
            score += 10  # Has dependencies section
            
            # Check if dependencies match includes
            deps_content = deps_match.group(1)
            actual_includes = set(re.findall(r'<include component="([^"]+)" />', content))
            listed_deps = set(re.findall(r'<component>([^<]+)</component>', deps_content))
            
            if actual_includes == listed_deps:
                score += 15  # Dependencies match includes
            else:
                result["warnings"].append("Dependencies section doesn't match actual includes")
                
        return score
        
    def _check_component_structure(self, content: str, result: Dict) -> int:
        """Check component follows proper structure."""
        score = 0
        
        try:
            root = ET.fromstring(content)
            
            # Check for required elements
            if root.find('.//step') is not None:
                score += 25  # Has step element
            else:
                result["errors"].append("Missing <step> element")
                
            if root.find('.//description') is not None:
                score += 25  # Has description
            else:
                result["errors"].append("Missing <description> element")
                
        except ET.ParseError:
            pass  # Already handled in XML structure check
            
        return score
        
    def _check_output_format(self, content: str, result: Dict) -> int:
        """Check component has proper output format."""
        score = 0
        
        if '<output>' in content:
            score += 25  # Has output section
        elif '<output_format>' in content:
            score += 20  # Has alternative output format
            result["warnings"].append("Using <output_format> instead of <output>")
        else:
            result["errors"].append("Missing <output> section")
            
        return score
        
    def validate_all(self) -> Dict[str, any]:
        """Validate all commands and components."""
        summary = {
            "total_files": 0,
            "valid_files": 0,
            "total_score": 0,
            "max_possible_score": 0,
            "files": []
        }
        
        # Validate commands
        commands_dir = self.root_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.rglob("*.md"):
                if cmd_file.name != "README.md":
                    result = self.validate_command(cmd_file)
                    summary["files"].append(result)
                    summary["total_files"] += 1
                    if result["valid"]:
                        summary["valid_files"] += 1
                    summary["total_score"] += result["score"]
                    summary["max_possible_score"] += result["max_score"]
                    
        # Validate components
        components_dir = self.root_path / "components"
        if components_dir.exists():
            for comp_file in components_dir.rglob("*.md"):
                if comp_file.name != "README.md":
                    result = self.validate_component(comp_file)
                    summary["files"].append(result)
                    summary["total_files"] += 1
                    if result["valid"]:
                        summary["valid_files"] += 1
                    summary["total_score"] += result["score"]
                    summary["max_possible_score"] += result["max_score"]
                    
        return summary
        
    def generate_report(self, summary: Dict) -> str:
        """Generate a validation report."""
        report = []
        report.append("# Claude Code Prompt Factory Template Validation Report")
        report.append(f"**Generated**: {__import__('datetime').datetime.now().isoformat()}")
        report.append("")
        
        # Summary
        total_files = summary["total_files"]
        valid_files = summary["valid_files"]
        score_pct = (summary["total_score"] / summary["max_possible_score"] * 100) if summary["max_possible_score"] > 0 else 0
        
        report.append("## 📋 Executive Summary")
        report.append(f"- **Total Files**: {total_files}")
        valid_pct = (valid_files/total_files*100) if total_files > 0 else 0
        report.append(f"- **Valid Files**: {valid_files} ({valid_pct:.1f}%)")
        report.append(f"- **Overall Score**: {summary['total_score']}/{summary['max_possible_score']} ({score_pct:.1f}%)")
        report.append("")
        
        # Errors and warnings
        total_errors = sum(len(f["errors"]) for f in summary["files"])
        total_warnings = sum(len(f["warnings"]) for f in summary["files"])
        
        if total_errors > 0:
            report.append(f"## 🚨 Critical Issues ({total_errors} errors)")
            for file_result in summary["files"]:
                if file_result["errors"]:
                    report.append(f"### {file_result['file']}")
                    for error in file_result["errors"]:
                        report.append(f"- ❌ {error}")
                    report.append("")
                    
        if total_warnings > 0:
            report.append(f"## ⚠️ Warnings ({total_warnings} warnings)")
            for file_result in summary["files"]:
                if file_result["warnings"]:
                    report.append(f"### {file_result['file']}")
                    for warning in file_result["warnings"]:
                        report.append(f"- ⚠️ {warning}")
                    report.append("")
                    
        # Top scoring files
        report.append("## ✅ Top Performing Files")
        top_files = sorted(summary["files"], key=lambda x: x["score"], reverse=True)[:10]
        for file_result in top_files:
            score_pct = file_result["score"] / file_result["max_score"] * 100
            report.append(f"- **{file_result['file']}**: {file_result['score']}/{file_result['max_score']} ({score_pct:.1f}%)")
        
        return "\n".join(report)

def main():
    """Main validation function."""
    validator = TemplateValidator()
    summary = validator.validate_all()
    report = validator.generate_report(summary)
    
    # Save report
    with open("template_validation_report.md", "w") as f:
        f.write(report)
        
    print("Template validation complete. Report saved to template_validation_report.md")
    print(f"Overall score: {summary['total_score']}/{summary['max_possible_score']}")

if __name__ == "__main__":
    main()