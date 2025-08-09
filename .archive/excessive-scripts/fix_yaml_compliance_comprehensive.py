#!/usr/bin/env python3
"""
YAML Compliance Fixer for Claude Code Modular Prompts
Converts deprecated 'tools:' field to correct 'allowed-tools:' field
"""

import os
import re
import yaml
from typing import List, Dict, Tuple
import shutil
from pathlib import Path

class YAMLComplianceFixer:
    def __init__(self, commands_dir: str):
        self.commands_dir = Path(commands_dir)
        self.backup_dir = Path(commands_dir).parent / "backup_before_yaml_fix"
        self.changes_made = []
        self.errors = []
        
    def create_backup(self):
        """Create backup of all commands before making changes"""
        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)
        shutil.copytree(self.commands_dir, self.backup_dir)
        print(f"✅ Backup created at: {self.backup_dir}")
    
    def find_files_with_tools_field(self) -> List[Path]:
        """Find all .md files containing the deprecated 'tools:' field"""
        files_with_tools = []
        
        for md_file in self.commands_dir.rglob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Check if file has yaml frontmatter with tools: field
                if content.startswith('---') and '\ntools:' in content:
                    files_with_tools.append(md_file)
                    
            except Exception as e:
                self.errors.append(f"Error reading {md_file}: {e}")
                
        return files_with_tools
    
    def extract_yaml_frontmatter(self, content: str) -> Tuple[str, str, str]:
        """Extract YAML frontmatter, content, and separators"""
        if not content.startswith('---'):
            raise ValueError("File does not start with YAML frontmatter")
            
        # Find the end of frontmatter
        parts = content.split('---', 2)
        if len(parts) < 3:
            raise ValueError("Invalid YAML frontmatter structure")
            
        yaml_content = parts[1].strip()
        markdown_content = parts[2]
        
        return yaml_content, markdown_content, "---"
    
    def fix_yaml_content(self, yaml_content: str) -> str:
        """Fix the YAML content by replacing 'tools:' with 'allowed-tools:'"""
        lines = yaml_content.split('\n')
        fixed_lines = []
        
        for line in lines:
            # Check if this line starts with 'tools:'
            if re.match(r'^tools:\s*', line):
                # Replace 'tools:' with 'allowed-tools:'
                fixed_line = re.sub(r'^tools:', 'allowed-tools:', line)
                fixed_lines.append(fixed_line)
            else:
                fixed_lines.append(line)
                
        return '\n'.join(fixed_lines)
    
    def validate_yaml_syntax(self, yaml_content: str) -> bool:
        """Validate that the YAML syntax is correct"""
        try:
            yaml.safe_load(yaml_content)
            return True
        except yaml.YAMLError as e:
            return False
    
    def fix_single_file(self, file_path: Path) -> Dict:
        """Fix a single file and return change details"""
        change_info = {
            'file': str(file_path.relative_to(self.commands_dir)),
            'success': False,
            'error': None,
            'before': None,
            'after': None
        }
        
        try:
            # Read original content
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Extract YAML frontmatter
            yaml_content, markdown_content, separator = self.extract_yaml_frontmatter(original_content)
            
            # Store original for comparison
            change_info['before'] = yaml_content
            
            # Fix the YAML
            fixed_yaml = self.fix_yaml_content(yaml_content)
            change_info['after'] = fixed_yaml
            
            # Validate fixed YAML
            if not self.validate_yaml_syntax(fixed_yaml):
                raise ValueError("Fixed YAML has invalid syntax")
            
            # Reconstruct file content
            new_content = f"{separator}\n{fixed_yaml}\n{separator}{markdown_content}"
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            change_info['success'] = True
            
        except Exception as e:
            change_info['error'] = str(e)
            self.errors.append(f"Error fixing {file_path}: {e}")
            
        return change_info
    
    def fix_all_files(self) -> Dict:
        """Fix all files with deprecated tools: field"""
        print("🔍 Finding files with deprecated 'tools:' field...")
        files_to_fix = self.find_files_with_tools_field()
        
        print(f"📊 Found {len(files_to_fix)} files to fix")
        
        if not files_to_fix:
            return {
                'total_files': 0,
                'fixed_files': 0,
                'failed_files': 0,
                'changes': [],
                'errors': []
            }
        
        # Create backup
        self.create_backup()
        
        # Fix each file
        print("🔧 Fixing files...")
        fixed_count = 0
        failed_count = 0
        
        for file_path in files_to_fix:
            print(f"  Processing: {file_path.relative_to(self.commands_dir)}")
            change_info = self.fix_single_file(file_path)
            self.changes_made.append(change_info)
            
            if change_info['success']:
                fixed_count += 1
                print(f"    ✅ Fixed")
            else:
                failed_count += 1
                print(f"    ❌ Failed: {change_info['error']}")
        
        return {
            'total_files': len(files_to_fix),
            'fixed_files': fixed_count,
            'failed_files': failed_count,
            'changes': self.changes_made,
            'errors': self.errors
        }
    
    def validate_compliance_after_fix(self) -> Dict:
        """Validate that all files are now compliant"""
        print("🔍 Validating compliance after fixes...")
        
        total_files = len(list(self.commands_dir.rglob("*.md")))
        files_with_tools = self.find_files_with_tools_field()
        files_with_allowed_tools = []
        
        # Check for files with allowed-tools
        for md_file in self.commands_dir.rglob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.startswith('---') and '\nallowed-tools:' in content:
                        files_with_allowed_tools.append(md_file)
            except Exception as e:
                self.errors.append(f"Error validating {md_file}: {e}")
        
        compliance_rate = (len(files_with_allowed_tools) / total_files) * 100 if total_files > 0 else 0
        
        return {
            'total_md_files': total_files,
            'files_with_deprecated_tools': len(files_with_tools),
            'files_with_allowed_tools': len(files_with_allowed_tools),
            'compliance_rate': compliance_rate,
            'is_fully_compliant': len(files_with_tools) == 0 and len(files_with_allowed_tools) > 0
        }

def main():
    # Set the commands directory path
    commands_dir = "/Users/smenssink/conductor/repo/claude-code-modular-prompts/.claude/commands"
    
    if not os.path.exists(commands_dir):
        print(f"❌ Commands directory not found: {commands_dir}")
        return
    
    print("🚀 Starting YAML Compliance Fix for Claude Code Commands")
    print("=" * 60)
    
    # Initialize fixer
    fixer = YAMLComplianceFixer(commands_dir)
    
    # Fix all files
    results = fixer.fix_all_files()
    
    # Validate compliance
    validation = fixer.validate_compliance_after_fix()
    
    # Print detailed report
    print("\n" + "=" * 60)
    print("📊 YAML COMPLIANCE FIX REPORT")
    print("=" * 60)
    
    print(f"📁 Total .md files in commands directory: {validation['total_md_files']}")
    print(f"🔧 Files processed: {results['total_files']}")
    print(f"✅ Files successfully fixed: {results['fixed_files']}")
    print(f"❌ Files with errors: {results['failed_files']}")
    print(f"📊 Current compliance rate: {validation['compliance_rate']:.1f}%")
    print(f"🎯 Fully compliant: {'YES' if validation['is_fully_compliant'] else 'NO'}")
    
    # Show specific changes made
    if results['changes']:
        print(f"\n📝 DETAILED CHANGES MADE:")
        print("-" * 40)
        for i, change in enumerate(results['changes'], 1):
            status = "✅" if change['success'] else "❌"
            print(f"{i:2d}. {status} {change['file']}")
            if change['success'] and change['before'] != change['after']:
                # Show the specific line that changed
                before_lines = change['before'].split('\n')
                after_lines = change['after'].split('\n')
                for j, (before_line, after_line) in enumerate(zip(before_lines, after_lines)):
                    if before_line != after_line:
                        print(f"     Before: {before_line.strip()}")
                        print(f"     After:  {after_line.strip()}")
                        break
            elif not change['success']:
                print(f"     Error: {change['error']}")
    
    # Show any errors
    if results['errors']:
        print(f"\n❌ ERRORS ENCOUNTERED:")
        print("-" * 40)
        for i, error in enumerate(results['errors'], 1):
            print(f"{i:2d}. {error}")
    
    # Final status
    print(f"\n🏆 FINAL STATUS:")
    if validation['is_fully_compliant']:
        print("✅ ALL COMMANDS ARE NOW 100% CLAUDE CODE COMPLIANT!")
        print("✅ All 'tools:' fields successfully converted to 'allowed-tools:'")
    else:
        print("❌ Some files still need attention")
        if validation['files_with_deprecated_tools'] > 0:
            print(f"   - {validation['files_with_deprecated_tools']} files still have 'tools:' field")
        if validation['files_with_allowed_tools'] == 0:
            print(f"   - No files found with 'allowed-tools:' field")
    
    print(f"\n💾 Backup saved at: {fixer.backup_dir}")
    print("   Use this backup to restore original files if needed")

if __name__ == "__main__":
    main()