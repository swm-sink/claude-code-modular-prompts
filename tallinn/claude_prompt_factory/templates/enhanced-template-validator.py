#!/usr/bin/env python3
"""
Enhanced Template Validation System for Claude Code Prompt Factory
Provides strict compliance checking and detailed quality scoring.
"""

import os
import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Tuple, Optional
from pathlib import Path
import yaml
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EnhancedTemplateValidator:
    def __init__(self, root_path: str = "claude_prompt_factory"):
        self.root_path = Path(root_path)
        self.validation_rules = self._load_validation_rules()
        
    def _load_validation_rules(self) -> Dict:
        """Load enhanced validation rules."""
        return {
            "command": {
                "max_score": 100,
                "scoring": {
                    "yaml_frontmatter": 25,
                    "xml_structure": 30,
                    "component_includes": 20,
                    "dependencies_accuracy": 15,
                    "template_compliance": 10
                },
                "required_yaml_fields": [
                    "description", "argument-hint", "allowed-tools"
                ],
                "required_xml_elements": [
                    "metadata", "arguments", "claude_prompt", "dependencies"
                ],
                "quality_checks": [
                    "proper_cdata_usage",
                    "include_component_validation",
                    "argument_validation",
                    "usage_examples"
                ]
            },
            "component": {
                "max_score": 100,
                "scoring": {
                    "xml_structure": 30,
                    "component_structure": 25,
                    "output_format": 25,
                    "documentation_quality": 10,
                    "template_compliance": 10
                },
                "required_xml_elements": [
                    "step", "description", "output"
                ],
                "quality_checks": [
                    "output_format_compliance",
                    "behavioral_guidelines",
                    "integration_points",
                    "structured_content"
                ]
            }
        }
        
    def validate_command(self, file_path: Path) -> Dict[str, any]:
        """Enhanced command validation with detailed scoring."""
        result = {
            "file": str(file_path),
            "type": "command",
            "valid": True,
            "errors": [],
            "warnings": [],
            "score": 0,
            "max_score": 100,
            "detailed_scores": {},
            "quality_metrics": {},
            "compliance_level": "none"
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Enhanced validation components
            yaml_score = self._validate_yaml_frontmatter(content, result)
            xml_score = self._validate_xml_structure(content, result, "command")
            includes_score = self._validate_component_includes(content, result)
            deps_score = self._validate_dependencies_section(content, result)
            compliance_score = self._validate_template_compliance(content, result, "command")
            
            result["detailed_scores"] = {
                "yaml_frontmatter": yaml_score,
                "xml_structure": xml_score,
                "component_includes": includes_score,
                "dependencies_accuracy": deps_score,
                "template_compliance": compliance_score
            }
            
            result["score"] = sum(result["detailed_scores"].values())
            result["compliance_level"] = self._calculate_compliance_level(result["score"])
            
        except Exception as e:
            result["valid"] = False
            result["errors"].append(f"Validation error: {str(e)}")
            
        return result
        
    def validate_component(self, file_path: Path) -> Dict[str, any]:
        """Enhanced component validation with detailed scoring."""
        result = {
            "file": str(file_path),
            "type": "component",
            "valid": True,
            "errors": [],
            "warnings": [],
            "score": 0,
            "max_score": 100,
            "detailed_scores": {},
            "quality_metrics": {},
            "compliance_level": "none"
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Enhanced validation components
            xml_score = self._validate_xml_structure(content, result, "component")
            structure_score = self._validate_component_structure(content, result)
            output_score = self._validate_output_format(content, result)
            doc_score = self._validate_documentation_quality(content, result)
            compliance_score = self._validate_template_compliance(content, result, "component")
            
            result["detailed_scores"] = {
                "xml_structure": xml_score,
                "component_structure": structure_score,
                "output_format": output_score,
                "documentation_quality": doc_score,
                "template_compliance": compliance_score
            }
            
            result["score"] = sum(result["detailed_scores"].values())
            result["compliance_level"] = self._calculate_compliance_level(result["score"])
            
        except Exception as e:
            result["valid"] = False
            result["errors"].append(f"Validation error: {str(e)}")
            
        return result
        
    def _validate_yaml_frontmatter(self, content: str, result: Dict) -> int:
        """Enhanced YAML frontmatter validation."""
        score = 0
        max_score = self.validation_rules["command"]["scoring"]["yaml_frontmatter"]
        
        yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        
        if not yaml_match:
            result["errors"].append("Missing YAML frontmatter")
            return 0
            
        yaml_content = yaml_match.group(1)
        
        try:
            yaml_data = yaml.safe_load(yaml_content)
            score += 5  # Valid YAML structure
            
            # Check required fields
            required_fields = self.validation_rules["command"]["required_yaml_fields"]
            for field in required_fields:
                if field in yaml_data and yaml_data[field]:
                    score += 5
                    
                    # Quality checks
                    if field == "description" and len(str(yaml_data[field])) > 20:
                        score += 2  # Good description length
                    elif field == "allowed-tools" and isinstance(yaml_data[field], list):
                        score += 2  # Proper tools format
                else:
                    result["errors"].append(f"Missing or empty YAML field: {field}")
                    
            # Bonus for enhanced fields
            if "template-version" in yaml_data:
                score += 3
                
        except yaml.YAMLError as e:
            result["errors"].append(f"Invalid YAML syntax: {str(e)}")
            
        return min(score, max_score)
        
    def _validate_xml_structure(self, content: str, result: Dict, file_type: str) -> int:
        """Enhanced XML structure validation."""
        score = 0
        max_score = self.validation_rules[file_type]["scoring"]["xml_structure"]
        
        if file_type == "command":
            xml_match = re.search(r'<command_file>.*?</command_file>', content, re.DOTALL)
            if not xml_match:
                result["errors"].append("Missing <command_file> XML structure")
                return 0
            xml_content = xml_match.group(0)
        else:
            xml_content = content
            
        try:
            root = ET.fromstring(xml_content)
            score += 10  # Valid XML structure
            
            # Check required elements
            required_elements = self.validation_rules[file_type]["required_xml_elements"]
            for element in required_elements:
                if root.find(f".//{element}") is not None:
                    score += 3
                else:
                    result["errors"].append(f"Missing required XML element: <{element}>")
                    
            # Bonus checks
            if root.find(".//template_version") is not None:
                score += 2  # Has template version
                
            # Check XML formatting quality
            if self._has_proper_cdata_usage(xml_content):
                score += 3
                
        except ET.ParseError as e:
            result["errors"].append(f"XML Parse Error: {str(e)}")
            return 0
            
        return min(score, max_score)
        
    def _validate_component_includes(self, content: str, result: Dict) -> int:
        """Enhanced component includes validation."""
        score = 0
        max_score = self.validation_rules["command"]["scoring"]["component_includes"]
        
        includes = re.findall(r'<include component="([^"]+)" />', content)
        
        if includes:
            score += 8  # Has component includes
            
            valid_includes = 0
            for include_path in includes:
                full_path = self.root_path / include_path
                if full_path.exists():
                    valid_includes += 1
                    score += 1
                else:
                    result["warnings"].append(f"Component not found: {include_path}")
                    
            # Bonus for good include practices
            if valid_includes > 3:
                score += 3  # Good integration
            if "progress-reporting.md" in str(includes):
                score += 2  # Standard progress reporting
            if "error-handling.md" in str(includes):
                score += 2  # Standard error handling
                
        else:
            result["warnings"].append("No component includes found")
                    
        return min(score, max_score)
        
    def _validate_dependencies_section(self, content: str, result: Dict) -> int:
        """Enhanced dependencies section validation."""
        score = 0
        max_score = self.validation_rules["command"]["scoring"]["dependencies_accuracy"]
        
        deps_match = re.search(r'<includes_components>(.*?)</includes_components>', content, re.DOTALL)
        if deps_match:
            score += 5  # Has dependencies section
            
            deps_content = deps_match.group(1)
            actual_includes = set(re.findall(r'<include component="([^"]+)" />', content))
            listed_deps = set(re.findall(r'<component>([^<]+)</component>', deps_content))
            
            if actual_includes == listed_deps:
                score += 10  # Perfect match
            elif len(actual_includes & listed_deps) / len(actual_includes | listed_deps) > 0.8:
                score += 6  # Good match
                result["warnings"].append("Dependencies section has minor discrepancies")
            else:
                result["warnings"].append("Dependencies section doesn't match actual includes")
        else:
            result["errors"].append("Missing dependencies section")
            
        return min(score, max_score)
        
    def _validate_output_format(self, content: str, result: Dict) -> int:
        """Enhanced output format validation."""
        score = 0
        max_score = self.validation_rules["component"]["scoring"]["output_format"]
        
        if '<output>' in content:
            score += 15  # Has output section
            
            # Extract output content
            output_match = re.search(r'<output>(.*?)</output>', content, re.DOTALL)
            if output_match:
                output_content = output_match.group(1)
                
                # Quality checks
                if "**" in output_content:  # Has formatting
                    score += 3
                if "Status:" in output_content or "Results:" in output_content:
                    score += 3
                if "Behavioral Guidelines" in output_content:
                    score += 4
                    
        elif '<output_format>' in content:
            score += 10  # Has alternative format
            result["warnings"].append("Using <output_format> instead of <output>")
        else:
            result["errors"].append("Missing <output> section")
            
        return min(score, max_score)
        
    def _validate_template_compliance(self, content: str, result: Dict, file_type: str) -> int:
        """Validate compliance with template standards."""
        score = 0
        max_score = self.validation_rules[file_type]["scoring"]["template_compliance"]
        
        # Check for template version
        if 'template-version' in content or 'template_version' in content:
            score += 3
            
        # Check for proper structure
        if file_type == "command":
            if all(section in content for section in ["## Usage", "## Arguments", "## What It Does"]):
                score += 4
        else:
            if "<metadata>" in content:
                score += 2
            if "<integration_points>" in content:
                score += 2
                
        # Check for consistent formatting
        if re.search(r'\*\*[^*]+\*\*:', content):  # Bold labels
            score += 1
            
        return min(score, max_score)
        
    def _validate_component_structure(self, content: str, result: Dict) -> int:
        """Enhanced component structure validation."""
        score = 0
        max_score = self.validation_rules["component"]["scoring"]["component_structure"]
        
        try:
            root = ET.fromstring(content)
            
            # Check for required elements
            if root.find('.//step') is not None:
                score += 10
                
                # Check step has name attribute
                step_elem = root.find('.//step')
                if step_elem.get('name'):
                    score += 5
                else:
                    result["warnings"].append("Step element missing name attribute")
            else:
                result["errors"].append("Missing <step> element")
                
            if root.find('.//description') is not None:
                score += 10
                
                # Check description quality
                desc_elem = root.find('.//description')
                if desc_elem.text and len(desc_elem.text.strip()) > 50:
                    score += 3  # Good description length
            else:
                result["errors"].append("Missing <description> element")
                
        except ET.ParseError:
            pass  # Already handled in XML structure check
            
        return min(score, max_score)
        
    def _validate_documentation_quality(self, content: str, result: Dict) -> int:
        """Validate documentation quality in components."""
        score = 0
        max_score = self.validation_rules["component"]["scoring"]["documentation_quality"]
        
        # Check for comprehensive descriptions
        if len(content) > 500:  # Substantial content
            score += 3
            
        # Check for structured sections
        structured_sections = ["configuration", "integration_points", "validation"]
        for section in structured_sections:
            if f"<{section}>" in content:
                score += 2
                
        # Check for examples or usage patterns
        if "example" in content.lower() or "usage" in content.lower():
            score += 1
            
        return min(score, max_score)
        
    def _has_proper_cdata_usage(self, content: str) -> bool:
        """Check for proper CDATA usage."""
        cdata_sections = re.findall(r'<!\[CDATA\[(.*?)\]\]>', content, re.DOTALL)
        return len(cdata_sections) > 0
        
    def _calculate_compliance_level(self, score: int) -> str:
        """Calculate compliance level based on score."""
        if score >= 95:
            return "excellent"
        elif score >= 85:
            return "good"
        elif score >= 70:
            return "acceptable"
        elif score >= 50:
            return "poor"
        else:
            return "critical"
            
    def validate_all(self) -> Dict[str, any]:
        """Enhanced validation of all templates."""
        summary = {
            "total_files": 0,
            "valid_files": 0,
            "total_score": 0,
            "max_possible_score": 0,
            "files": [],
            "compliance_breakdown": {
                "excellent": 0,
                "good": 0,
                "acceptable": 0,
                "poor": 0,
                "critical": 0
            }
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
                    summary["compliance_breakdown"][result["compliance_level"]] += 1
                    
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
                    summary["compliance_breakdown"][result["compliance_level"]] += 1
                    
        return summary
        
    def generate_enhanced_report(self, summary: Dict) -> str:
        """Generate enhanced validation report."""
        report = []
        report.append("# Enhanced Template Validation Report")
        report.append(f"**Generated**: {__import__('datetime').datetime.now().isoformat()}")
        report.append("")
        
        # Executive Summary
        total_files = summary["total_files"]
        valid_files = summary["valid_files"]
        score_pct = (summary["total_score"] / summary["max_possible_score"] * 100) if summary["max_possible_score"] > 0 else 0
        
        report.append("## 📊 Executive Dashboard")
        report.append(f"- **Total Files**: {total_files}")
        valid_pct = (valid_files/total_files*100) if total_files > 0 else 0
        report.append(f"- **Valid Files**: {valid_files} ({valid_pct:.1f}%)")
        report.append(f"- **Overall Compliance Score**: {summary['total_score']}/{summary['max_possible_score']} ({score_pct:.1f}%)")
        report.append("")
        
        # Compliance Breakdown
        report.append("## 🎯 Compliance Level Distribution")
        for level, count in summary["compliance_breakdown"].items():
            percentage = (count / total_files * 100) if total_files > 0 else 0
            report.append(f"- **{level.title()}**: {count} files ({percentage:.1f}%)")
        report.append("")
        
        # Detailed Issues
        errors_by_file = [(f, len(f["errors"])) for f in summary["files"] if f["errors"]]
        if errors_by_file:
            report.append(f"## 🚨 Critical Issues ({sum(count for _, count in errors_by_file)} total)")
            for file_result, error_count in sorted(errors_by_file, key=lambda x: x[1], reverse=True):
                report.append(f"### {file_result['file']} ({error_count} errors)")
                for error in file_result["errors"]:
                    report.append(f"- ❌ {error}")
                report.append("")
                
        # Top Performers
        report.append("## 🏆 Excellence Tier (95%+ Compliance)")
        excellent_files = [f for f in summary["files"] if f["compliance_level"] == "excellent"]
        for file_result in excellent_files:
            score_pct = file_result["score"] / file_result["max_score"] * 100
            report.append(f"- **{file_result['file']}**: {file_result['score']}/{file_result['max_score']} ({score_pct:.1f}%)")
        
        if not excellent_files:
            report.append("*No files currently meet excellence criteria*")
        
        return "\n".join(report)

def main():
    """Main enhanced validation function."""
    validator = EnhancedTemplateValidator()
    summary = validator.validate_all()
    report = validator.generate_enhanced_report(summary)
    
    # Save report
    with open("enhanced_template_validation_report.md", "w") as f:
        f.write(report)
        
    score_pct = (summary['total_score'] / summary['max_possible_score'] * 100) if summary['max_possible_score'] > 0 else 0
    print(f"Enhanced template validation complete. Overall compliance: {score_pct:.1f}%")
    print("Report saved to enhanced_template_validation_report.md")

if __name__ == "__main__":
    main()