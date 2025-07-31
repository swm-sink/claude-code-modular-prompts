#!/usr/bin/env python3
"""
Final YAML Compliance Validation for Claude Code Commands
"""

import os
import yaml
from pathlib import Path

def validate_final_compliance():
    commands_dir = Path("/Users/smenssink/conductor/repo/claude-code-modular-prompts/.claude/commands")
    
    print("🔍 FINAL YAML COMPLIANCE VALIDATION")
    print("=" * 50)
    
    # Find all .md files
    all_md_files = list(commands_dir.rglob("*.md"))
    print(f"📁 Total .md files found: {len(all_md_files)}")
    
    # Count deprecated fields
    files_with_tools = []
    files_with_allowed_tools = []
    files_with_yaml_errors = []
    files_without_frontmatter = []
    
    for md_file in all_md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.startswith('---'):
                files_without_frontmatter.append(md_file)
                continue
            
            # Extract YAML frontmatter
            parts = content.split('---', 2)
            if len(parts) < 3:
                files_without_frontmatter.append(md_file)
                continue
            
            yaml_content = parts[1].strip()
            
            # Try to parse YAML
            try:
                yaml_data = yaml.safe_load(yaml_content)
            except yaml.YAMLError:
                files_with_yaml_errors.append(md_file)
                continue
            
            # Check for deprecated 'tools' field
            if 'tools' in yaml_data:
                files_with_tools.append(md_file)
            
            # Check for correct 'allowed-tools' field
            if 'allowed-tools' in yaml_data:
                files_with_allowed_tools.append(md_file)
                
        except Exception as e:
            print(f"❌ Error processing {md_file}: {e}")
    
    # Calculate compliance
    compliance_rate = (len(files_with_allowed_tools) / len(all_md_files)) * 100 if all_md_files else 0
    
    print(f"✅ Files with correct 'allowed-tools:' field: {len(files_with_allowed_tools)}")
    print(f"❌ Files with deprecated 'tools:' field: {len(files_with_tools)}")
    print(f"⚠️  Files with YAML errors: {len(files_with_yaml_errors)}")
    print(f"⚠️  Files without YAML frontmatter: {len(files_without_frontmatter)}")
    print(f"📊 Compliance rate: {compliance_rate:.1f}%")
    
    # Show any remaining issues
    if files_with_tools:
        print("\n❌ FILES STILL USING DEPRECATED 'tools:' FIELD:")
        for f in files_with_tools:
            print(f"   - {f.relative_to(commands_dir)}")
    
    if files_with_yaml_errors:
        print("\n⚠️  FILES WITH YAML ERRORS:")
        for f in files_with_yaml_errors:
            print(f"   - {f.relative_to(commands_dir)}")
    
    if files_without_frontmatter:
        print("\n⚠️  FILES WITHOUT YAML FRONTMATTER:")
        for f in files_without_frontmatter:
            print(f"   - {f.relative_to(commands_dir)}")
    
    # Final result
    is_fully_compliant = (
        len(files_with_tools) == 0 and 
        len(files_with_yaml_errors) == 0 and
        len(files_with_allowed_tools) > 0 and
        len(files_without_frontmatter) == 0
    )
    
    print(f"\n🏆 FINAL RESULT:")
    if is_fully_compliant:
        print("✅ 100% CLAUDE CODE YAML COMPLIANCE ACHIEVED!")
        print("✅ All commands use correct 'allowed-tools:' field")
        print("✅ No deprecated 'tools:' fields found")
        print("✅ All YAML frontmatter is valid")
    else:
        print("❌ Compliance issues still exist")
    
    return {
        'total_files': len(all_md_files),
        'compliant_files': len(files_with_allowed_tools),
        'deprecated_files': len(files_with_tools),
        'yaml_errors': len(files_with_yaml_errors),
        'no_frontmatter': len(files_without_frontmatter),
        'compliance_rate': compliance_rate,
        'fully_compliant': is_fully_compliant
    }

if __name__ == "__main__":
    results = validate_final_compliance()