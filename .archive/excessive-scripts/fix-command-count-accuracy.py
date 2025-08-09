#!/usr/bin/env python3
"""
Fix Command Count Accuracy
Update all documentation to reflect the correct command count of 85.
"""

import re
from pathlib import Path

def fix_command_counts():
    project_root = Path(".")
    files_to_fix = [
        'README.md',
        'CLAUDE.md', 
        'USAGE.md',
        'FAQ.md'
    ]
    
    fixes_applied = []
    
    for file_name in files_to_fix:
        file_path = project_root / file_name
        if not file_path.exists():
            continue
            
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            original_content = content
            
            # Replace various patterns for command counts
            patterns_to_fix = [
                (r'\b82\s+command', '85 command'),
                (r'\b82\s+Claude\s+Code\s+command', '85 Claude Code command'),
                (r'\b82\s+command\s+templates', '85 command templates'),
                (r'collection\s+of\s+82\s+Claude', 'collection of 85 Claude'),
                (r'Total\s+Commands:\s+82', 'Total Commands: 85'),
                (r'Total\s+Command\s+Templates:\s+82', 'Total Command Templates: 85'),
            ]
            
            local_fixes = 0
            for pattern, replacement in patterns_to_fix:
                new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                if new_content != content:
                    content = new_content
                    local_fixes += 1
            
            if content != original_content:
                with open(file_path, 'w') as f:
                    f.write(content)
                fixes_applied.append(f"{file_name}: {local_fixes} count fixes applied")
            
        except Exception as e:
            print(f"Error fixing {file_name}: {e}")
    
    return fixes_applied

def main():
    print("🔢 Fixing command count accuracy (82 → 85)...")
    fixes = fix_command_counts()
    
    print(f"\n✅ Fixes Applied:")
    for fix in fixes:
        print(f"   • {fix}")
    
    print(f"\n📊 Summary:")
    print(f"   Previous Count: 82 commands")
    print(f"   Actual Count: 85 commands") 
    print(f"   Difference: +3 commands (4 UX commands added in Step 89)")
    print(f"   Files Updated: {len(fixes)}")
    
    return len(fixes)

if __name__ == "__main__":
    main()