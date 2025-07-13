#!/usr/bin/env python3
"""
Wildcard Pattern Detector for Claude Code Settings
Agent V27: Settings Protection Auditor

This script detects broken wildcard patterns in Claude Code settings files.
These patterns are known to cause permission loops and failures.
"""

import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Broken wildcard patterns to detect
BROKEN_PATTERNS = [
    r'Bash\([^)]*:\*\)',  # Matches Bash(command:*)
    r'Bash\(\*\)',        # Matches Bash(*)
    r'Bash\(\*:\*\)',     # Matches Bash(*:*)
]

# Common working patterns for reference
WORKING_PATTERNS = [
    'Bash(git)',
    'Bash(git add)',
    'Bash(ls)',
    'Bash(python)',
]

class WildcardDetector:
    """Detects wildcard patterns in Claude Code settings."""
    
    def __init__(self):
        self.broken_pattern_regex = [re.compile(pattern) for pattern in BROKEN_PATTERNS]
        self.findings = []
        
    def scan_file(self, filepath: Path) -> List[Dict]:
        """Scan a file for broken wildcard patterns."""
        file_findings = []
        
        try:
            if filepath.suffix == '.json':
                # Handle JSON files
                with open(filepath, 'r') as f:
                    content = f.read()
                    lines = content.split('\n')
                    
                for line_num, line in enumerate(lines, 1):
                    for pattern_idx, regex in enumerate(self.broken_pattern_regex):
                        matches = regex.findall(line)
                        for match in matches:
                            file_findings.append({
                                'file': str(filepath),
                                'line': line_num,
                                'pattern': BROKEN_PATTERNS[pattern_idx],
                                'match': match,
                                'content': line.strip()
                            })
                            
            else:
                # Handle text files
                with open(filepath, 'r') as f:
                    lines = f.readlines()
                    
                for line_num, line in enumerate(lines, 1):
                    for pattern_idx, regex in enumerate(self.broken_pattern_regex):
                        matches = regex.findall(line)
                        for match in matches:
                            file_findings.append({
                                'file': str(filepath),
                                'line': line_num,
                                'pattern': BROKEN_PATTERNS[pattern_idx],
                                'match': match,
                                'content': line.strip()
                            })
                            
        except Exception as e:
            print(f"Error scanning {filepath}: {e}")
            
        return file_findings
    
    def scan_directory(self, directory: Path, extensions: List[str] = None) -> None:
        """Scan directory for files with broken wildcard patterns."""
        if extensions is None:
            extensions = ['.json', '.md', '.xml', '.yml', '.yaml']
            
        for ext in extensions:
            for filepath in directory.rglob(f'*{ext}'):
                # Skip certain directories
                if any(skip in str(filepath) for skip in ['node_modules', '.git', '__pycache__']):
                    continue
                    
                findings = self.scan_file(filepath)
                self.findings.extend(findings)
                
    def generate_report(self) -> str:
        """Generate a report of findings."""
        report = []
        report.append("# Wildcard Pattern Detection Report")
        report.append("=" * 50)
        report.append(f"\nTotal broken patterns found: {len(self.findings)}\n")
        
        if self.findings:
            report.append("## Broken Patterns Found:")
            report.append("-" * 30)
            
            # Group by file
            by_file = {}
            for finding in self.findings:
                file_path = finding['file']
                if file_path not in by_file:
                    by_file[file_path] = []
                by_file[file_path].append(finding)
                
            for file_path, file_findings in by_file.items():
                report.append(f"\n### File: {file_path}")
                report.append(f"Found {len(file_findings)} broken patterns:\n")
                
                for finding in file_findings:
                    report.append(f"  Line {finding['line']}: {finding['match']}")
                    report.append(f"  Pattern: {finding['pattern']}")
                    report.append(f"  Content: {finding['content']}")
                    report.append("")
                    
        else:
            report.append("✅ No broken wildcard patterns found!")
            
        report.append("\n## Recommended Actions:")
        report.append("-" * 30)
        report.append("1. Replace all wildcard patterns with individual command permissions")
        report.append("2. Use format: \"Bash(command)\" or \"Bash(command subcommand)\"")
        report.append("3. Never use colons or asterisks in permission patterns")
        report.append("4. Test permissions after any changes to avoid loops")
        
        report.append("\n## Working Pattern Examples:")
        report.append("-" * 30)
        for pattern in WORKING_PATTERNS:
            report.append(f"  ✅ \"{pattern}\"")
            
        return "\n".join(report)
    
    def validate_settings_file(self, filepath: Path) -> Tuple[bool, List[str]]:
        """Validate a settings file for wildcard patterns."""
        findings = self.scan_file(filepath)
        
        if findings:
            errors = []
            for finding in findings:
                errors.append(f"Line {finding['line']}: {finding['match']} - BROKEN PATTERN")
            return False, errors
        else:
            return True, []

def main():
    """Main entry point."""
    detector = WildcardDetector()
    
    # Default to current directory
    scan_path = Path.cwd()
    
    if len(sys.argv) > 1:
        scan_path = Path(sys.argv[1])
        
    print(f"Scanning {scan_path} for broken wildcard patterns...")
    
    if scan_path.is_file():
        findings = detector.scan_file(scan_path)
        detector.findings = findings
    else:
        detector.scan_directory(scan_path)
        
    # Generate and print report
    report = detector.generate_report()
    print(report)
    
    # Check specific settings files
    settings_files = [
        Path('.claude/settings.local.json'),
        Path('config/settings.json'),
    ]
    
    print("\n" + "=" * 50)
    print("Settings File Validation:")
    print("=" * 50)
    
    for settings_file in settings_files:
        if settings_file.exists():
            valid, errors = detector.validate_settings_file(settings_file)
            if valid:
                print(f"\n✅ {settings_file}: VALID - No wildcard patterns")
            else:
                print(f"\n❌ {settings_file}: INVALID - Contains broken patterns:")
                for error in errors:
                    print(f"   {error}")
                    
    # Exit with error code if findings
    sys.exit(1 if detector.findings else 0)

if __name__ == "__main__":
    main()