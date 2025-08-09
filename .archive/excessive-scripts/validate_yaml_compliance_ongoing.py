#!/usr/bin/env python3
"""
Ongoing YAML Compliance Validator for Claude Code Commands
Use this script to verify compliance after any changes to command files
"""

import os
import yaml
import sys
from pathlib import Path

def validate_yaml_compliance(commands_dir=None):
    """Validate Claude Code YAML compliance for all command files"""
    
    if commands_dir is None:
        commands_dir = Path("/Users/smenssink/conductor/repo/claude-code-modular-prompts/.claude/commands")
    else:
        commands_dir = Path(commands_dir)
    
    if not commands_dir.exists():
        print(f"❌ Commands directory not found: {commands_dir}")
        return False
    
    print("🔍 CLAUDE CODE YAML COMPLIANCE CHECK")
    print("=" * 45)
    
    # Find all .md files
    md_files = list(commands_dir.rglob("*.md"))
    print(f"📁 Checking {len(md_files)} .md files...")
    
    # Track compliance
    compliant_files = []
    non_compliant_files = []
    files_with_errors = []
    report_files = []  # Files that are reports, not commands
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip files without YAML frontmatter
            if not content.startswith('---'):
                # Check if it's a report or documentation file
                filename = md_file.name.upper()
                if any(word in filename for word in ['REPORT', 'BASELINE', 'MATRICES', 'PERFORMANCE']):
                    report_files.append(md_file)
                    continue
                else:
                    files_with_errors.append((md_file, "No YAML frontmatter"))
                    continue
                    
            # Extract YAML frontmatter
            parts = content.split('---', 2)
            if len(parts) < 3:
                files_with_errors.append((md_file, "Invalid YAML frontmatter structure"))
                continue
                
            yaml_content = parts[1].strip()
            
            # Parse YAML
            try:
                yaml_data = yaml.safe_load(yaml_content)
            except yaml.YAMLError as e:
                files_with_errors.append((md_file, f"YAML parsing error: {e}"))
                continue
            
            # Check for compliance
            if yaml_data is None:
                files_with_errors.append((md_file, "Empty YAML frontmatter"))
                continue
                
            # Check for deprecated 'tools' field
            if 'tools' in yaml_data:
                non_compliant_files.append((md_file, "Uses deprecated 'tools:' field"))
                continue
            
            # File is compliant (either has allowed-tools or no tools field at all)
            compliant_files.append(md_file)
            
        except Exception as e:
            files_with_errors.append((md_file, f"Error reading file: {e}"))
    
    # Calculate compliance rate
    total_command_files = len(md_files) - len(report_files)
    compliant_count = len(compliant_files)
    compliance_rate = (compliant_count / total_command_files * 100) if total_command_files > 0 else 0
    
    # Report results
    print(f"✅ Compliant command files: {compliant_count}")
    print(f"❌ Non-compliant files: {len(non_compliant_files)}")
    print(f"⚠️  Files with errors: {len(files_with_errors)}")
    print(f"📊 Report/documentation files: {len(report_files)}")
    print(f"📈 Compliance rate: {compliance_rate:.1f}%")
    
    # Show issues if any
    if non_compliant_files:
        print("\n❌ NON-COMPLIANT FILES:")
        for file_path, issue in non_compliant_files:
            print(f"   - {file_path.relative_to(commands_dir)}: {issue}")
    
    if files_with_errors:
        print("\n⚠️  FILES WITH ERRORS:")
        for file_path, error in files_with_errors:
            print(f"   - {file_path.relative_to(commands_dir)}: {error}")
    
    if report_files:
        print("\n📊 REPORT/DOCUMENTATION FILES (skipped):")
        for file_path in report_files:
            print(f"   - {file_path.relative_to(commands_dir)}")
    
    # Final status
    is_fully_compliant = len(non_compliant_files) == 0 and len(files_with_errors) == 0
    
    print(f"\n🏆 COMPLIANCE STATUS:")
    if is_fully_compliant:
        print("✅ 100% CLAUDE CODE COMPLIANT!")
        print("   All command files meet Claude Code YAML standards")
    else:
        print("❌ Compliance issues detected")
        print(f"   {len(non_compliant_files + files_with_errors)} files need attention")
    
    return is_fully_compliant

def main():
    """Main function for command line usage"""
    commands_dir = None
    
    # Check for command line argument
    if len(sys.argv) > 1:
        commands_dir = sys.argv[1]
        if not os.path.exists(commands_dir):
            print(f"❌ Directory not found: {commands_dir}")
            sys.exit(1)
    
    # Run validation
    is_compliant = validate_yaml_compliance(commands_dir)
    
    # Exit with appropriate code
    sys.exit(0 if is_compliant else 1)

if __name__ == "__main__":
    main()