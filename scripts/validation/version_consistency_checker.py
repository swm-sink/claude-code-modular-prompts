#!/usr/bin/env python3
"""
Version Consistency Checker for Claude Code Modular Prompts Framework
Version: 1.0.0
Date: 2025-07-13

This script validates version consistency across the framework according to the versioning strategy:
- Framework version: 3.0.0
- Commands: Should align with framework version (3.0.0)
- Modules: Independent versioning (1.x.x)
- PROJECT_CONFIG.xml files: Schema version (1.0.0)
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class VersionInfo:
    """Information about a version found in a file."""
    file_path: str
    line_num: int
    version: str
    context: str
    component_type: str

class VersionConsistencyChecker:
    """Validates version consistency across the framework."""
    
    FRAMEWORK_VERSION = "3.0.0"
    CONFIG_SCHEMA_VERSION = "1.0.0"
    
    VERSION_PATTERNS = {
        'version_table': re.compile(r'^\|\s*(\d+\.\d+\.\d+)\s*\|'),
        'xml_version': re.compile(r'version\s*=\s*"(\d+\.\d+\.\d+)"'),
        'version_attr': re.compile(r'version:\s*(\d+\.\d+\.\d+)'),
        'version_badge': re.compile(r'version-(\d+\.\d+\.\d+)-'),
    }
    
    def __init__(self, root_path: str):
        """Initialize the checker with the project root path."""
        self.root_path = Path(root_path)
        self.results: Dict[str, List[VersionInfo]] = defaultdict(list)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def determine_component_type(self, file_path: Path) -> str:
        """Determine the type of component based on file path."""
        path_str = str(file_path.relative_to(self.root_path))
        
        if path_str == "CLAUDE.md":
            return "framework_control"
        elif "PROJECT_CONFIG" in path_str and path_str.endswith(".xml"):
            return "config_schema"
        elif ".claude/commands/" in path_str:
            return "command"
        elif ".claude/modules/" in path_str:
            return "module"
        elif path_str.endswith("README.md"):
            return "readme"
        elif "docs/" in path_str:
            return "documentation"
        elif "test" in path_str.lower():
            return "test"
        else:
            return "other"
            
    def check_file(self, file_path: Path) -> None:
        """Check a single file for version references."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.splitlines()
                
            component_type = self.determine_component_type(file_path)
            
            # Check each line for version patterns
            for i, line in enumerate(lines, 1):
                for pattern_name, pattern in self.VERSION_PATTERNS.items():
                    matches = pattern.findall(line)
                    for version in matches:
                        info = VersionInfo(
                            file_path=str(file_path),
                            line_num=i,
                            version=version,
                            context=line.strip(),
                            component_type=component_type
                        )
                        self.results[component_type].append(info)
                        
        except Exception as e:
            self.errors.append(f"Error reading {file_path}: {e}")
            
    def validate_versions(self) -> None:
        """Validate versions according to the framework rules."""
        # Validate framework control document
        for info in self.results.get('framework_control', []):
            if 'framework version' in info.context.lower() and info.version != self.FRAMEWORK_VERSION:
                self.errors.append(
                    f"Framework version mismatch in {info.file_path}:{info.line_num} - "
                    f"Expected {self.FRAMEWORK_VERSION}, found {info.version}"
                )
                
        # Validate commands (should be 3.0.0)
        for info in self.results.get('command', []):
            if info.line_num <= 3 and info.version != self.FRAMEWORK_VERSION:
                self.warnings.append(
                    f"Command version mismatch in {info.file_path}:{info.line_num} - "
                    f"Expected {self.FRAMEWORK_VERSION}, found {info.version}"
                )
                
        # Validate modules (should be 1.x.x according to strategy)
        for info in self.results.get('module', []):
            if info.line_num <= 3:  # Version header
                if info.version.startswith('3.'):
                    self.warnings.append(
                        f"Module using framework version in {info.file_path}:{info.line_num} - "
                        f"Modules should use independent 1.x.x versioning, found {info.version}"
                    )
                elif info.version.startswith('2.'):
                    self.warnings.append(
                        f"Module using outdated version in {info.file_path}:{info.line_num} - "
                        f"Found {info.version}"
                    )
                    
        # Validate PROJECT_CONFIG files (should be 1.0.0)
        for info in self.results.get('config_schema', []):
            if info.version != self.CONFIG_SCHEMA_VERSION:
                self.errors.append(
                    f"Config schema version mismatch in {info.file_path}:{info.line_num} - "
                    f"Expected {self.CONFIG_SCHEMA_VERSION}, found {info.version}"
                )
                
    def scan_directory(self, directory: Path, patterns: List[str]) -> None:
        """Recursively scan directory for files matching patterns."""
        for pattern in patterns:
            for file_path in directory.rglob(pattern):
                if file_path.is_file() and not any(part.startswith('.') for part in file_path.parts[:-1]):
                    self.check_file(file_path)
                    
    def generate_report(self) -> str:
        """Generate a detailed report of findings."""
        report = ["# Version Consistency Check Report", ""]
        report.append(f"**Framework Version**: {self.FRAMEWORK_VERSION}")
        report.append(f"**Date**: {os.popen('date +%Y-%m-%d').read().strip()}")
        report.append("")
        
        # Summary
        report.append("## Summary")
        report.append("")
        total_files = sum(len(set(info.file_path for info in infos)) for infos in self.results.values())
        total_versions = sum(len(infos) for infos in self.results.values())
        report.append(f"- Total files scanned: {total_files}")
        report.append(f"- Total version references found: {total_versions}")
        report.append(f"- Errors: {len(self.errors)}")
        report.append(f"- Warnings: {len(self.warnings)}")
        report.append("")
        
        # Component breakdown
        report.append("## Component Version Distribution")
        report.append("")
        
        for component_type, infos in sorted(self.results.items()):
            if infos:
                report.append(f"### {component_type.replace('_', ' ').title()}")
                version_counts = defaultdict(int)
                for info in infos:
                    if info.line_num <= 3 or component_type in ['framework_control', 'config_schema']:
                        version_counts[info.version] += 1
                        
                for version, count in sorted(version_counts.items(), key=lambda x: x[1], reverse=True):
                    report.append(f"- {version}: {count} occurrences")
                report.append("")
                
        # Errors
        if self.errors:
            report.append("## ❌ Errors (Must Fix)")
            report.append("")
            for error in self.errors:
                report.append(f"- {error}")
            report.append("")
            
        # Warnings
        if self.warnings:
            report.append("## ⚠️ Warnings (Should Review)")
            report.append("")
            for warning in self.warnings:
                report.append(f"- {warning}")
            report.append("")
            
        # Recommendations
        report.append("## 📋 Recommendations")
        report.append("")
        report.append("1. **Commands**: Ensure all command files use framework version 3.0.0")
        report.append("2. **Modules**: Consider migrating modules with 3.0.0 to independent 1.x.x versioning")
        report.append("3. **Documentation**: Update version tables to reflect current framework version")
        report.append("4. **Automation**: Run this script regularly to maintain version consistency")
        report.append("")
        
        return "\n".join(report)
        
    def run(self) -> Tuple[bool, str]:
        """Run the version consistency check."""
        print("🔍 Scanning for version references...")
        
        # Scan different file types
        patterns = ["*.md", "*.xml", "*.py", "*.json"]
        self.scan_directory(self.root_path, patterns)
        
        print("✓ Scan complete")
        print("🔍 Validating versions...")
        
        self.validate_versions()
        
        print("✓ Validation complete")
        
        report = self.generate_report()
        success = len(self.errors) == 0
        
        return success, report

def main():
    """Main entry point."""
    # Determine project root
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent.parent
    
    print(f"Claude Code Framework Version Consistency Checker")
    print(f"Project root: {project_root}")
    print()
    
    checker = VersionConsistencyChecker(project_root)
    success, report = checker.run()
    
    # Save report
    report_path = project_root / "internal" / "reports" / "validation" / "version_consistency_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_path, 'w') as f:
        f.write(report)
        
    print()
    print(f"📄 Report saved to: {report_path}")
    print()
    
    # Print summary
    if success:
        print("✅ Version consistency check passed!")
    else:
        print("❌ Version consistency issues found!")
        print(f"   - {len(checker.errors)} errors")
        print(f"   - {len(checker.warnings)} warnings")
        print()
        print("See the full report for details.")
        
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())