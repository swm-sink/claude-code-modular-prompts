#!/usr/bin/env python3
"""
MCP Template Validator for Claude Code File Format Converter v2.0
Provides automated quality assurance and compliance checking for enhanced command templates.
"""

import json
import yaml
import re
import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import xml.etree.ElementTree as ET
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Results from template validation."""
    file_path: str
    is_valid: bool
    version: str
    issues: List[str]
    warnings: List[str]
    enhancements: List[str]
    metadata_score: int  # 0-100
    xml_tag_count: int


class MCPTemplateValidator:
    """Advanced template validator for Claude Code commands with v2.0 enhancements."""
    
    def __init__(self, project_root: str = None):
        self.project_root = Path(project_root or os.getcwd())
        self.commands_dir = self.project_root / ".claude" / "commands"
        
        # v2.0 Enhanced metadata requirements
        self.required_fields = [
            "command", "description", "category", "allowed-tools"
        ]
        
        self.v2_enhanced_fields = [
            "parameters", "usage_examples", "prerequisites", 
            "output_format", "tags", "version", "author", "last_updated"
        ]
        
        # XML semantic tags for v2.0
        self.semantic_xml_tags = [
            "context", "instructions", "examples", "workflow", 
            "task", "automation", "memory", "integration", "configuration"
        ]

    def validate_command(self, file_path: str) -> ValidationResult:
        """Validate a single command template."""
        path = Path(file_path)
        
        if not path.exists():
            return ValidationResult(
                file_path=file_path,
                is_valid=False,
                version="unknown",
                issues=[f"File not found: {file_path}"],
                warnings=[],
                enhancements=[],
                metadata_score=0,
                xml_tag_count=0
            )
        
        try:
            content = path.read_text(encoding='utf-8')
            return self._analyze_template(file_path, content)
        except Exception as e:
            return ValidationResult(
                file_path=file_path,
                is_valid=False,
                version="error",
                issues=[f"Failed to read file: {str(e)}"],
                warnings=[],
                enhancements=[],
                metadata_score=0,
                xml_tag_count=0
            )

    def _analyze_template(self, file_path: str, content: str) -> ValidationResult:
        """Comprehensive template analysis."""
        issues = []
        warnings = []
        enhancements = []
        
        # Extract YAML frontmatter
        frontmatter, body = self._extract_yaml_frontmatter(content)
        if not frontmatter:
            issues.append("Missing or invalid YAML frontmatter")
            return ValidationResult(
                file_path=file_path,
                is_valid=False,
                version="unknown",
                issues=issues,
                warnings=warnings,
                enhancements=enhancements,
                metadata_score=0,
                xml_tag_count=0
            )
        
        # Validate basic structure
        self._validate_required_fields(frontmatter, issues)
        
        # Check for v2.0 enhancements
        v2_score = self._check_v2_enhancements(frontmatter, warnings, enhancements)
        
        # Validate XML semantic structure
        xml_count = self._validate_xml_structure(body, warnings, enhancements)
        
        # Calculate metadata completeness score
        metadata_score = self._calculate_metadata_score(frontmatter, body)
        
        # Determine version
        version = frontmatter.get("version", "1.0")
        if v2_score >= 70 and xml_count >= 5:
            version = "2.0+"
        elif v2_score >= 40:
            version = "1.5"
        
        is_valid = len(issues) == 0
        
        return ValidationResult(
            file_path=file_path,
            is_valid=is_valid,
            version=version,
            issues=issues,
            warnings=warnings,
            enhancements=enhancements,
            metadata_score=metadata_score,
            xml_tag_count=xml_count
        )

    def _extract_yaml_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """Extract and parse YAML frontmatter."""
        if not content.startswith('---'):
            return {}, content
        
        try:
            parts = content.split('---', 2)
            if len(parts) < 3:
                return {}, content
            
            yaml_content = parts[1]
            body_content = parts[2]
            
            frontmatter = yaml.safe_load(yaml_content) or {}
            return frontmatter, body_content
        except yaml.YAMLError as e:
            return {}, content

    def _validate_required_fields(self, frontmatter: Dict, issues: List[str]):
        """Validate required metadata fields."""
        for field in self.required_fields:
            if field not in frontmatter:
                issues.append(f"Missing required field: {field}")
            elif not frontmatter[field]:
                issues.append(f"Empty required field: {field}")

    def _check_v2_enhancements(self, frontmatter: Dict, warnings: List[str], enhancements: List[str]) -> int:
        """Check for v2.0 enhancement features."""
        score = 0
        total_possible = len(self.v2_enhanced_fields) * 10
        
        for field in self.v2_enhanced_fields:
            if field in frontmatter and frontmatter[field]:
                score += 10
                if field == "parameters" and isinstance(frontmatter[field], list):
                    score += 5  # Bonus for proper parameter structure
                if field == "usage_examples" and len(frontmatter[field]) >= 3:
                    score += 5  # Bonus for multiple examples
            else:
                enhancements.append(f"Consider adding v2.0 field: {field}")
        
        percentage = (score / total_possible) * 100
        
        if percentage < 30:
            warnings.append("Template has minimal v2.0 enhancements")
        elif percentage < 60:
            warnings.append("Template partially enhanced for v2.0")
        
        return int(percentage)

    def _validate_xml_structure(self, body: str, warnings: List[str], enhancements: List[str]) -> int:
        """Validate XML semantic structure in body."""
        xml_count = 0
        found_tags = set()
        
        # Count XML tags
        xml_pattern = r'<(\w+)(?:\s+[^>]*)?>.*?</\1>|<(\w+)(?:\s+[^>]*)?/>'
        matches = re.findall(xml_pattern, body, re.DOTALL)
        
        for match in matches:
            tag = match[0] or match[1]
            found_tags.add(tag)
            xml_count += 1
        
        # Check for semantic XML tags
        semantic_found = found_tags.intersection(set(self.semantic_xml_tags))
        
        if xml_count == 0:
            enhancements.append("Consider adding XML semantic structure for v2.0")
        elif xml_count < 5:
            enhancements.append("Add more XML semantic tags for better structure")
        elif len(semantic_found) < 3:
            enhancements.append("Use more semantic XML tags: context, instructions, examples, workflow")
        
        # Validate XML syntax
        try:
            # Wrap in root element for parsing
            wrapped_xml = f"<root>{body}</root>"
            ET.fromstring(wrapped_xml)
        except ET.ParseError as e:
            warnings.append(f"XML syntax issue: {str(e)}")
        
        return xml_count

    def _calculate_metadata_score(self, frontmatter: Dict, body: str) -> int:
        """Calculate overall metadata completeness score."""
        score = 0
        
        # Basic metadata (30 points)
        for field in self.required_fields:
            if field in frontmatter and frontmatter[field]:
                score += 7.5
        
        # Enhanced metadata (50 points)
        for field in self.v2_enhanced_fields:
            if field in frontmatter and frontmatter[field]:
                score += 6.25
        
        # XML structure (20 points)
        xml_count = len(re.findall(r'<(\w+)', body))
        xml_score = min(20, xml_count * 2)
        score += xml_score
        
        return int(min(100, score))

    def check_compatibility(self, file_path: str) -> Dict[str, Any]:
        """Check Claude Code compatibility."""
        result = self.validate_command(file_path)
        
        compatibility = {
            "claude_code_compatible": result.is_valid,
            "version_detected": result.version,
            "metadata_completeness": f"{result.metadata_score}%",
            "enhancement_level": self._get_enhancement_level(result.metadata_score),
            "issues": result.issues,
            "recommendations": result.enhancements
        }
        
        return compatibility

    def suggest_improvements(self, file_path: str) -> Dict[str, Any]:
        """Suggest specific improvements for template."""
        result = self.validate_command(file_path)
        
        suggestions = {
            "priority_improvements": [],
            "enhancement_opportunities": result.enhancements,
            "xml_structure_suggestions": [],
            "metadata_suggestions": []
        }
        
        # Priority improvements based on issues
        for issue in result.issues:
            suggestions["priority_improvements"].append({
                "issue": issue,
                "priority": "high",
                "action": self._get_fix_suggestion(issue)
            })
        
        # XML structure suggestions
        if result.xml_tag_count < 5:
            suggestions["xml_structure_suggestions"] = [
                "Add <context> tag for project-specific information",
                "Add <instructions> tag for procedural guidance",
                "Add <examples> tag with structured input/output pairs",
                "Add <workflow> tag for implementation phases"
            ]
        
        # Metadata suggestions
        path = Path(file_path)
        if path.exists():
            content = path.read_text()
            frontmatter, _ = self._extract_yaml_frontmatter(content)
            
            for field in self.v2_enhanced_fields:
                if field not in frontmatter:
                    suggestions["metadata_suggestions"].append({
                        "field": field,
                        "suggestion": self._get_metadata_suggestion(field)
                    })
        
        return suggestions

    def _get_enhancement_level(self, score: int) -> str:
        """Get enhancement level description."""
        if score >= 90:
            return "fully_enhanced_v2"
        elif score >= 70:
            return "well_enhanced"
        elif score >= 50:
            return "partially_enhanced"
        elif score >= 30:
            return "minimally_enhanced"
        else:
            return "basic_v1"

    def _get_fix_suggestion(self, issue: str) -> str:
        """Get specific fix suggestion for an issue."""
        if "Missing required field" in issue:
            field = issue.split(": ")[1]
            return f"Add {field} to YAML frontmatter"
        elif "Empty required field" in issue:
            field = issue.split(": ")[1]
            return f"Provide value for {field} field"
        elif "YAML frontmatter" in issue:
            return "Add YAML frontmatter at the beginning of the file"
        else:
            return "Fix the identified issue"

    def _get_metadata_suggestion(self, field: str) -> str:
        """Get suggestion for missing metadata field."""
        suggestions = {
            "parameters": "Add parameter definitions with type and description",
            "usage_examples": "Add 3+ usage examples showing different use cases",
            "prerequisites": "List required dependencies and setup steps",
            "output_format": "Specify expected output format (text|code|json|structured)",
            "tags": "Add relevant tags for categorization and search",
            "version": "Add version number (2.0 for enhanced templates)",
            "author": "Add author or team attribution",
            "last_updated": "Add last update date (YYYY-MM-DD format)"
        }
        return suggestions.get(field, f"Add {field} field for better metadata")


def main():
    """MCP Server main function."""
    if len(sys.argv) < 2:
        print("Usage: python mcp_template_validator.py <command> [args]")
        sys.exit(1)
    
    command = sys.argv[1]
    validator = MCPTemplateValidator()
    
    if command == "validate_command" and len(sys.argv) > 2:
        file_path = sys.argv[2]
        result = validator.validate_command(file_path)
        print(json.dumps({
            "valid": result.is_valid,
            "version": result.version,
            "score": result.metadata_score,
            "xml_tags": result.xml_tag_count,
            "issues": result.issues,
            "warnings": result.warnings,
            "enhancements": result.enhancements
        }, indent=2))
    
    elif command == "check_compatibility" and len(sys.argv) > 2:
        file_path = sys.argv[2]
        result = validator.check_compatibility(file_path)
        print(json.dumps(result, indent=2))
    
    elif command == "suggest_improvements" and len(sys.argv) > 2:
        file_path = sys.argv[2]
        result = validator.suggest_improvements(file_path)
        print(json.dumps(result, indent=2))
    
    else:
        print("Available commands: validate_command, check_compatibility, suggest_improvements")
        sys.exit(1)


if __name__ == "__main__":
    main()