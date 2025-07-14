#!/usr/bin/env python3
"""
XML Framework Validation Tool
Validates Claude Code XML framework structure and performance
"""

import xml.etree.ElementTree as ET
import os
import sys
import json
import time
from typing import Dict, List, Tuple, Optional
from pathlib import Path
import re

class XMLFrameworkValidator:
    """Validates XML framework structure and performance"""
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.claude_dir = self.project_root / ".claude"
        self.validation_results = {
            "structure_validation": {},
            "performance_metrics": {},
            "quality_assessment": {},
            "compliance_check": {}
        }
    
    def validate_xml_structure(self, xml_file: Path) -> Dict:
        """Validate XML structure and syntax"""
        results = {
            "file": str(xml_file),
            "valid_xml": False,
            "element_count": 0,
            "max_depth": 0,
            "attributes_count": 0,
            "text_content_length": 0,
            "issues": []
        }
        
        try:
            # Parse XML file
            with open(xml_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract XML content from markdown
            xml_match = re.search(r'```xml\s*\n(.*?)\n```', content, re.DOTALL)
            if not xml_match:
                results["issues"].append("No XML content found in markdown")
                return results
            
            xml_content = xml_match.group(1)
            
            # Parse XML
            root = ET.fromstring(xml_content)
            results["valid_xml"] = True
            
            # Count elements and analyze structure
            def analyze_element(element, depth=0):
                count = 1
                max_d = depth
                attr_count = len(element.attrib)
                text_len = len(element.text or "")
                
                for child in element:
                    child_count, child_depth, child_attrs, child_text = analyze_element(child, depth + 1)
                    count += child_count
                    max_d = max(max_d, child_depth)
                    attr_count += child_attrs
                    text_len += child_text
                
                return count, max_d, attr_count, text_len
            
            results["element_count"], results["max_depth"], results["attributes_count"], results["text_content_length"] = analyze_element(root)
            
            # Validate command structure
            if root.tag == "command":
                results["command_structure"] = self._validate_command_structure(root)
            elif root.tag == "module":
                results["module_structure"] = self._validate_module_structure(root)
            
        except ET.ParseError as e:
            results["issues"].append(f"XML parsing error: {e}")
        except Exception as e:
            results["issues"].append(f"Validation error: {e}")
        
        return results
    
    def _validate_command_structure(self, root: ET.Element) -> Dict:
        """Validate command XML structure"""
        structure = {
            "has_delegation": False,
            "has_pattern_integration": False,
            "has_thinking_pattern": False,
            "has_tdd_integration": False,
            "checkpoint_count": 0,
            "pattern_count": 0,
            "issues": []
        }
        
        # Check for required elements
        delegation = root.find("delegation")
        if delegation is not None:
            structure["has_delegation"] = True
            if not delegation.get("target"):
                structure["issues"].append("Delegation missing target attribute")
        
        pattern_integration = root.find("pattern_integration")
        if pattern_integration is not None:
            structure["has_pattern_integration"] = True
            patterns = pattern_integration.findall("uses_pattern")
            structure["pattern_count"] = len(patterns)
            
            for pattern in patterns:
                if not pattern.get("from"):
                    structure["issues"].append("Pattern missing 'from' attribute")
        
        thinking_pattern = root.find("thinking_pattern")
        if thinking_pattern is not None:
            structure["has_thinking_pattern"] = True
            checkpoints = thinking_pattern.findall("checkpoint")
            structure["checkpoint_count"] = len(checkpoints)
            
            for checkpoint in checkpoints:
                if not checkpoint.get("id"):
                    structure["issues"].append("Checkpoint missing id attribute")
                if not checkpoint.get("enforcement"):
                    structure["issues"].append("Checkpoint missing enforcement attribute")
        
        tdd_integration = root.find("tdd_integration")
        if tdd_integration is not None:
            structure["has_tdd_integration"] = True
        
        return structure
    
    def _validate_module_structure(self, root: ET.Element) -> Dict:
        """Validate module XML structure"""
        structure = {
            "has_purpose": False,
            "has_trigger_conditions": False,
            "has_implementation": False,
            "has_integration_points": False,
            "phase_count": 0,
            "issues": []
        }
        
        # Check for required elements
        purpose = root.find("purpose")
        if purpose is not None:
            structure["has_purpose"] = True
        
        trigger_conditions = root.find("trigger_conditions")
        if trigger_conditions is not None:
            structure["has_trigger_conditions"] = True
        
        implementation = root.find("implementation")
        if implementation is not None:
            structure["has_implementation"] = True
            phases = implementation.findall("phase")
            structure["phase_count"] = len(phases)
        
        integration_points = root.find("integration_points")
        if integration_points is not None:
            structure["has_integration_points"] = True
        
        return structure
    
    def calculate_performance_metrics(self, xml_file: Path) -> Dict:
        """Calculate performance metrics for XML file"""
        metrics = {
            "file_size_bytes": 0,
            "estimated_tokens": 0,
            "parsing_complexity": "unknown",
            "parallel_opportunities": 0,
            "optimization_score": 0.0
        }
        
        try:
            # File size
            metrics["file_size_bytes"] = xml_file.stat().st_size
            
            # Token estimation (rough: 1 token ≈ 4 characters)
            with open(xml_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metrics["estimated_tokens"] = len(content) // 4
            
            # Parsing complexity based on nesting depth
            xml_match = re.search(r'```xml\s*\n(.*?)\n```', content, re.DOTALL)
            if xml_match:
                xml_content = xml_match.group(1)
                try:
                    root = ET.fromstring(xml_content)
                    
                    def calculate_depth(element, current_depth=0):
                        max_depth = current_depth
                        for child in element:
                            child_depth = calculate_depth(child, current_depth + 1)
                            max_depth = max(max_depth, child_depth)
                        return max_depth
                    
                    depth = calculate_depth(root)
                    if depth <= 3:
                        metrics["parsing_complexity"] = "low"
                    elif depth <= 6:
                        metrics["parsing_complexity"] = "medium"
                    else:
                        metrics["parsing_complexity"] = "high"
                    
                    # Count parallel opportunities
                    parallel_hints = len(re.findall(r'parallel', xml_content, re.IGNORECASE))
                    batch_hints = len(re.findall(r'batch', xml_content, re.IGNORECASE))
                    metrics["parallel_opportunities"] = parallel_hints + batch_hints
                    
                    # Calculate optimization score (0-100)
                    optimization_score = 100
                    if depth > 6:
                        optimization_score -= 20
                    if metrics["estimated_tokens"] > 15000:
                        optimization_score -= 20
                    if metrics["parallel_opportunities"] == 0:
                        optimization_score -= 30
                    if len(re.findall(r'enforcement="MANDATORY"', xml_content)) < 3:
                        optimization_score -= 10
                    
                    metrics["optimization_score"] = max(0, optimization_score)
                    
                except ET.ParseError:
                    metrics["parsing_complexity"] = "error"
            
        except Exception as e:
            metrics["error"] = str(e)
        
        return metrics
    
    def validate_tdd_compliance(self, xml_file: Path) -> Dict:
        """Validate TDD compliance in XML structure"""
        compliance = {
            "has_tdd_integration": False,
            "has_red_phase": False,
            "has_green_phase": False,
            "has_refactor_phase": False,
            "has_blocking_conditions": False,
            "quality_gates_count": 0,
            "compliance_score": 0.0,
            "issues": []
        }
        
        try:
            with open(xml_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            xml_match = re.search(r'```xml\s*\n(.*?)\n```', content, re.DOTALL)
            if xml_match:
                xml_content = xml_match.group(1)
                
                # Check for TDD elements
                if 'tdd_integration' in xml_content:
                    compliance["has_tdd_integration"] = True
                
                if 'red_phase' in xml_content:
                    compliance["has_red_phase"] = True
                
                if 'green_phase' in xml_content:
                    compliance["has_green_phase"] = True
                
                if 'refactor_phase' in xml_content:
                    compliance["has_refactor_phase"] = True
                
                if 'blocking_conditions' in xml_content:
                    compliance["has_blocking_conditions"] = True
                
                # Count quality gates
                quality_gates = len(re.findall(r'quality_gate', xml_content, re.IGNORECASE))
                compliance["quality_gates_count"] = quality_gates
                
                # Calculate compliance score
                score = 0
                if compliance["has_tdd_integration"]:
                    score += 20
                if compliance["has_red_phase"]:
                    score += 20
                if compliance["has_green_phase"]:
                    score += 20
                if compliance["has_refactor_phase"]:
                    score += 20
                if compliance["has_blocking_conditions"]:
                    score += 10
                if quality_gates > 0:
                    score += min(10, quality_gates * 2)
                
                compliance["compliance_score"] = score
                
                # Check for issues
                if not compliance["has_tdd_integration"]:
                    compliance["issues"].append("Missing TDD integration")
                if not (compliance["has_red_phase"] and compliance["has_green_phase"] and compliance["has_refactor_phase"]):
                    compliance["issues"].append("Incomplete TDD cycle phases")
                
        except Exception as e:
            compliance["error"] = str(e)
        
        return compliance
    
    def run_validation(self) -> Dict:
        """Run complete validation of XML framework"""
        print("Starting XML Framework Validation...")
        
        # Find all XML files in commands and modules
        command_files = list((self.claude_dir / "commands").glob("*.md"))
        module_files = list((self.claude_dir / "modules").rglob("*.md"))
        
        print(f"Found {len(command_files)} command files and {len(module_files)} module files")
        
        # Validate each file
        for xml_file in command_files + module_files:
            print(f"Validating {xml_file.name}...")
            
            # Structure validation
            structure_result = self.validate_xml_structure(xml_file)
            self.validation_results["structure_validation"][xml_file.name] = structure_result
            
            # Performance metrics
            performance_result = self.calculate_performance_metrics(xml_file)
            self.validation_results["performance_metrics"][xml_file.name] = performance_result
            
            # TDD compliance (for commands)
            if xml_file.parent.name == "commands":
                tdd_result = self.validate_tdd_compliance(xml_file)
                self.validation_results["compliance_check"][xml_file.name] = tdd_result
        
        # Generate summary
        self.validation_results["summary"] = self._generate_summary()
        
        return self.validation_results
    
    def _generate_summary(self) -> Dict:
        """Generate validation summary"""
        summary = {
            "total_files": 0,
            "valid_files": 0,
            "total_issues": 0,
            "average_optimization_score": 0.0,
            "tdd_compliance_average": 0.0,
            "recommendations": []
        }
        
        total_files = len(self.validation_results["structure_validation"])
        valid_files = sum(1 for result in self.validation_results["structure_validation"].values() if result["valid_xml"])
        total_issues = sum(len(result["issues"]) for result in self.validation_results["structure_validation"].values())
        
        optimization_scores = [result["optimization_score"] for result in self.validation_results["performance_metrics"].values() if "optimization_score" in result]
        avg_optimization = sum(optimization_scores) / len(optimization_scores) if optimization_scores else 0
        
        tdd_scores = [result["compliance_score"] for result in self.validation_results["compliance_check"].values() if "compliance_score" in result]
        avg_tdd = sum(tdd_scores) / len(tdd_scores) if tdd_scores else 0
        
        summary.update({
            "total_files": total_files,
            "valid_files": valid_files,
            "total_issues": total_issues,
            "average_optimization_score": avg_optimization,
            "tdd_compliance_average": avg_tdd
        })
        
        # Generate recommendations
        if avg_optimization < 80:
            summary["recommendations"].append("Consider XML structure optimization for better performance")
        if avg_tdd < 80:
            summary["recommendations"].append("Improve TDD compliance in command structures")
        if total_issues > 0:
            summary["recommendations"].append("Address XML structure issues identified")
        
        return summary
    
    def save_results(self, output_file: str):
        """Save validation results to JSON file"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.validation_results, f, indent=2, ensure_ascii=False)
        print(f"Validation results saved to {output_file}")

def main():
    """Main validation function"""
    if len(sys.argv) < 2:
        print("Usage: python xml_validator.py <project_root>")
        sys.exit(1)
    
    project_root = sys.argv[1]
    
    # Create validator
    validator = XMLFrameworkValidator(project_root)
    
    # Run validation
    start_time = time.time()
    results = validator.run_validation()
    end_time = time.time()
    
    # Print summary
    summary = results["summary"]
    print(f"\n=== XML Framework Validation Summary ===")
    print(f"Validation completed in {end_time - start_time:.2f} seconds")
    print(f"Total files validated: {summary['total_files']}")
    print(f"Valid XML files: {summary['valid_files']}")
    print(f"Total issues found: {summary['total_issues']}")
    print(f"Average optimization score: {summary['average_optimization_score']:.1f}/100")
    print(f"Average TDD compliance: {summary['tdd_compliance_average']:.1f}/100")
    
    if summary["recommendations"]:
        print("\nRecommendations:")
        for rec in summary["recommendations"]:
            print(f"  - {rec}")
    
    # Save results
    validator.save_results("xml_validation_results.json")
    
    # Exit with appropriate code
    exit_code = 0 if summary["valid_files"] == summary["total_files"] and summary["total_issues"] == 0 else 1
    sys.exit(exit_code)

if __name__ == "__main__":
    main()