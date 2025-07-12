#!/usr/bin/env python3
"""
Intelligent Prompt Change Analyzer

Provides advanced analysis of prompt engineering changes including semantic 
validation, dependency checking, and risk assessment for the Claude Code framework.
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict
import difflib

class PromptChangeAnalyzer:
    """Advanced analyzer for prompt engineering changes in the Claude framework."""
    
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)
        self.claude_dir = self.repo_root / ".claude"
        self.analysis_results = {
            "semantic_issues": [],
            "dependency_impacts": [],
            "quality_concerns": [],
            "security_implications": [],
            "performance_impacts": [],
            "recommendations": []
        }
        
    def analyze_changes(self, changed_files: List[str]) -> Dict:
        """Main analysis entry point."""
        print("🔍 Starting comprehensive prompt change analysis...")
        
        # Categorize changes
        change_categories = self._categorize_changes(changed_files)
        
        # Analyze each category
        for category, files in change_categories.items():
            if files:
                print(f"📂 Analyzing {category} changes: {len(files)} files")
                
                if category == "commands":
                    self._analyze_command_changes(files)
                elif category == "modules":
                    self._analyze_module_changes(files)
                elif category == "quality":
                    self._analyze_quality_changes(files)
                elif category == "meta":
                    self._analyze_meta_changes(files)
                elif category == "claude_md":
                    self._analyze_claude_md_changes(files)
        
        # Cross-reference analysis
        self._analyze_cross_references(changed_files)
        
        # Generate recommendations
        self._generate_recommendations()
        
        return self.analysis_results
    
    def _categorize_changes(self, changed_files: List[str]) -> Dict[str, List[str]]:
        """Categorize changed files by type."""
        categories = {
            "commands": [],
            "modules": [],
            "quality": [],
            "meta": [],
            "claude_md": [],
            "other": []
        }
        
        for file_path in changed_files:
            if ".claude/commands/" in file_path:
                categories["commands"].append(file_path)
            elif ".claude/modules/" in file_path:
                categories["modules"].append(file_path)
            elif ".claude/system/quality/" in file_path:
                categories["quality"].append(file_path)
            elif ".claude/meta/" in file_path:
                categories["meta"].append(file_path)
            elif "CLAUDE.md" in file_path:
                categories["claude_md"].append(file_path)
            else:
                categories["other"].append(file_path)
        
        return categories
    
    def _analyze_command_changes(self, files: List[str]):
        """Analyze changes to command files."""
        for file_path in files:
            full_path = self.repo_root / file_path
            if not full_path.exists():
                continue
                
            # Read command content
            content = self._read_file_safely(full_path)
            if not content:
                continue
            
            # Check for command structure compliance
            self._validate_command_structure(file_path, content)
            
            # Check for proper module references
            self._validate_module_references(file_path, content)
            
            # Check for thinking pattern compliance
            self._validate_thinking_patterns(file_path, content)
    
    def _analyze_module_changes(self, files: List[str]):
        """Analyze changes to module files."""
        for file_path in files:
            full_path = self.repo_root / file_path
            if not full_path.exists():
                continue
                
            content = self._read_file_safely(full_path)
            if not content:
                continue
            
            # Validate module structure
            self._validate_module_structure(file_path, content)
            
            # Check interface contracts
            self._validate_interface_contracts(file_path, content)
            
            # Validate integration points
            self._validate_integration_points(file_path, content)
    
    def _analyze_quality_changes(self, files: List[str]):
        """Analyze changes to quality system files."""
        for file_path in files:
            if "tdd.md" in file_path or "production-standards.md" in file_path:
                self.analysis_results["quality_concerns"].append({
                    "file": file_path,
                    "severity": "HIGH",
                    "message": "Critical quality system component modified",
                    "recommendation": "Requires thorough testing and validation"
                })
    
    def _analyze_meta_changes(self, files: List[str]):
        """Analyze changes to meta-framework files."""
        for file_path in files:
            self.analysis_results["security_implications"].append({
                "file": file_path,
                "severity": "CRITICAL",
                "message": "Meta-framework modification detected",
                "recommendation": "Mandatory human review and safety validation required"
            })
    
    def _analyze_claude_md_changes(self, files: List[str]):
        """Analyze changes to CLAUDE.md."""
        for file_path in files:
            full_path = self.repo_root / file_path
            content = self._read_file_safely(full_path)
            
            if content:
                # Check for version changes
                version_match = re.search(r'version.*?(\d+\.\d+\.\d+)', content, re.IGNORECASE)
                if version_match:
                    self.analysis_results["semantic_issues"].append({
                        "file": file_path,
                        "severity": "MEDIUM",
                        "message": f"Framework version change detected: {version_match.group(1)}",
                        "recommendation": "Ensure all components are compatible with new version"
                    })
    
    def _validate_command_structure(self, file_path: str, content: str):
        """Validate command file structure."""
        required_sections = [
            "thinking_pattern",
            "implementation",
            "quality_gates",
            "integration_points"
        ]
        
        missing_sections = []
        for section in required_sections:
            if section not in content.lower():
                missing_sections.append(section)
        
        if missing_sections:
            self.analysis_results["semantic_issues"].append({
                "file": file_path,
                "severity": "MEDIUM",
                "message": f"Missing required sections: {', '.join(missing_sections)}",
                "recommendation": "Add missing sections for framework compliance"
            })
    
    def _validate_module_references(self, file_path: str, content: str):
        """Validate module references in commands."""
        # Find module references
        module_refs = re.findall(r'module = "([^"]+)"', content)
        
        for ref in module_refs:
            module_path = self.claude_dir / ref
            if not module_path.exists():
                self.analysis_results["dependency_impacts"].append({
                    "file": file_path,
                    "severity": "HIGH",
                    "message": f"Referenced module not found: {ref}",
                    "recommendation": "Fix module reference or create missing module"
                })
    
    def _validate_thinking_patterns(self, file_path: str, content: str):
        """Validate thinking pattern compliance."""
        if "thinking_pattern" in content:
            # Check for proper checkpoint structure
            if "checkpoint" not in content.lower():
                self.analysis_results["semantic_issues"].append({
                    "file": file_path,
                    "severity": "LOW",
                    "message": "Thinking pattern lacks checkpoint structure",
                    "recommendation": "Consider adding checkpoint-based thinking pattern"
                })
    
    def _validate_module_structure(self, file_path: str, content: str):
        """Validate module file structure."""
        required_elements = [
            "<module",
            "purpose>",
            "interface_contract>",
            "implementation>",
            "integration_points>"
        ]
        
        missing_elements = []
        for element in required_elements:
            if element not in content:
                missing_elements.append(element)
        
        if missing_elements:
            self.analysis_results["semantic_issues"].append({
                "file": file_path,
                "severity": "MEDIUM",
                "message": f"Module structure incomplete: missing {', '.join(missing_elements)}",
                "recommendation": "Complete module structure for framework compliance"
            })
    
    def _validate_interface_contracts(self, file_path: str, content: str):
        """Validate module interface contracts."""
        if "interface_contract" in content:
            if "inputs>" not in content or "outputs>" not in content:
                self.analysis_results["semantic_issues"].append({
                    "file": file_path,
                    "severity": "MEDIUM",
                    "message": "Interface contract missing inputs/outputs specification",
                    "recommendation": "Define clear inputs and outputs for module contract"
                })
    
    def _validate_integration_points(self, file_path: str, content: str):
        """Validate module integration points."""
        if "integration_points" in content:
            # Check for proper depends_on and provides_to structure
            if "depends_on" not in content and "provides_to" not in content:
                self.analysis_results["semantic_issues"].append({
                    "file": file_path,
                    "severity": "LOW",
                    "message": "Integration points lack dependency specification",
                    "recommendation": "Specify module dependencies and provisions"
                })
    
    def _analyze_cross_references(self, changed_files: List[str]):
        """Analyze cross-references between changed files."""
        print("🔗 Analyzing cross-references...")
        
        # Build reference map
        references = self._build_reference_map()
        
        # Check for broken references
        for file_path in changed_files:
            if file_path in references:
                for ref_file in references[file_path]:
                    ref_path = self.repo_root / ref_file
                    if not ref_path.exists():
                        self.analysis_results["dependency_impacts"].append({
                            "file": file_path,
                            "severity": "HIGH",
                            "message": f"References non-existent file: {ref_file}",
                            "recommendation": "Update reference or create missing file"
                        })
    
    def _build_reference_map(self) -> Dict[str, List[str]]:
        """Build a map of file references."""
        references = defaultdict(list)
        
        # Scan all .claude files for references
        for md_file in self.claude_dir.rglob("*.md"):
            content = self._read_file_safely(md_file)
            if content:
                # Find module references
                module_refs = re.findall(r'([a-zA-Z0-9_/-]+\.md)', content)
                rel_path = str(md_file.relative_to(self.repo_root))
                references[rel_path].extend(module_refs)
        
        return dict(references)
    
    def _generate_recommendations(self):
        """Generate specific recommendations based on analysis."""
        total_issues = (len(self.analysis_results["semantic_issues"]) + 
                       len(self.analysis_results["dependency_impacts"]) +
                       len(self.analysis_results["quality_concerns"]) +
                       len(self.analysis_results["security_implications"]))
        
        if total_issues == 0:
            self.analysis_results["recommendations"].append(
                "✅ No issues detected. Changes appear to be well-structured and compliant."
            )
        else:
            if self.analysis_results["security_implications"]:
                self.analysis_results["recommendations"].append(
                    "🔒 CRITICAL: Meta-framework changes require immediate human review and safety validation."
                )
            
            if len(self.analysis_results["dependency_impacts"]) > 0:
                self.analysis_results["recommendations"].append(
                    f"🔗 {len(self.analysis_results['dependency_impacts'])} dependency issues found. Validate all module references."
                )
            
            if len(self.analysis_results["semantic_issues"]) > 3:
                self.analysis_results["recommendations"].append(
                    "📝 Multiple structural issues detected. Consider comprehensive framework compliance review."
                )
            
            self.analysis_results["recommendations"].append(
                f"📊 Total issues: {total_issues}. Review and address before deployment."
            )
    
    def _read_file_safely(self, file_path: Path) -> Optional[str]:
        """Safely read file content."""
        try:
            return file_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"⚠️ Error reading {file_path}: {e}")
            return None
    
    def generate_report(self) -> str:
        """Generate a formatted analysis report."""
        report = []
        report.append("# 🔍 Prompt Change Analysis Report")
        report.append(f"**Generated**: {self._get_timestamp()}")
        report.append("")
        
        # Summary
        total_issues = sum(len(issues) for issues in [
            self.analysis_results["semantic_issues"],
            self.analysis_results["dependency_impacts"], 
            self.analysis_results["quality_concerns"],
            self.analysis_results["security_implications"]
        ])
        
        report.append(f"## 📊 Summary")
        report.append(f"- **Total Issues**: {total_issues}")
        report.append(f"- **Semantic Issues**: {len(self.analysis_results['semantic_issues'])}")
        report.append(f"- **Dependency Impacts**: {len(self.analysis_results['dependency_impacts'])}")
        report.append(f"- **Quality Concerns**: {len(self.analysis_results['quality_concerns'])}")
        report.append(f"- **Security Implications**: {len(self.analysis_results['security_implications'])}")
        report.append("")
        
        # Issues by category
        categories = [
            ("🔒 Security Implications", "security_implications"),
            ("⚠️ Quality Concerns", "quality_concerns"),
            ("🔗 Dependency Impacts", "dependency_impacts"),
            ("📝 Semantic Issues", "semantic_issues")
        ]
        
        for title, key in categories:
            issues = self.analysis_results[key]
            if issues:
                report.append(f"## {title}")
                for issue in issues:
                    severity_emoji = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🔵"}.get(issue["severity"], "⚪")
                    report.append(f"- {severity_emoji} **{issue['file']}**: {issue['message']}")
                    report.append(f"  - *Recommendation*: {issue['recommendation']}")
                report.append("")
        
        # Recommendations
        if self.analysis_results["recommendations"]:
            report.append("## 💡 Recommendations")
            for rec in self.analysis_results["recommendations"]:
                report.append(f"- {rec}")
            report.append("")
        
        return "\n".join(report)
    
    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(description="Analyze prompt engineering changes")
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    parser.add_argument("--changed-files", nargs="+", required=True, help="List of changed files")
    parser.add_argument("--output", help="Output file for analysis report")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    
    args = parser.parse_args()
    
    # Perform analysis
    analyzer = PromptChangeAnalyzer(args.repo_root)
    results = analyzer.analyze_changes(args.changed_files)
    
    if args.json:
        output = json.dumps(results, indent=2)
    else:
        output = analyzer.generate_report()
    
    if args.output:
        Path(args.output).write_text(output)
        print(f"📋 Analysis report written to {args.output}")
    else:
        print(output)
    
    # Exit with appropriate code
    total_issues = sum(len(issues) for issues in [
        results["semantic_issues"],
        results["dependency_impacts"],
        results["quality_concerns"],
        results["security_implications"]
    ])
    
    # Exit code indicates severity
    if results["security_implications"]:
        sys.exit(2)  # Critical issues
    elif total_issues > 5:
        sys.exit(1)  # Many issues
    else:
        sys.exit(0)  # Success

if __name__ == "__main__":
    main()