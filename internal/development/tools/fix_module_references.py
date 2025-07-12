#!/usr/bin/env python3
"""
Fix broken module references in the framework.
Updates all module references to point to the correct locations.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

# Mapping of broken references to their correct locations
REFERENCE_FIXES = {
    # Quality modules - now in system/quality/
    "quality/universal-quality-gates.md": "system/quality/universal-quality-gates.md",
    "quality/tdd.md": "system/quality/tdd.md",
    "quality/critical-thinking.md": "system/quality/critical-thinking.md",
    "quality/tdd-enforcement.md": "system/quality/tdd-enforcement.md",
    "quality/security-gate-verification.md": "system/quality/security-gate-verification.md",
    "quality/performance-gates.md": "system/quality/performance-gates.md",
    "quality/gate-verification.md": "system/quality/gate-verification.md",
    "quality/production-standards.md": "system/quality/production-standards.md",
    "quality/pre-commit.md": "system/quality/pre-commit.md",
    "quality/test-coverage.md": "system/quality/test-coverage.md",
    "quality/performance-validation.md": "system/quality/performance-validation.md",
    "quality/domain-validation.md": "system/quality/domain-validation.md",
    "quality/error-recovery.md": "patterns/error-recovery.md",
    
    # Pattern modules - in prompt_eng/patterns/
    "patterns/critical-thinking-pattern.md": "prompt_eng/patterns/thinking/critical-thinking-pattern.md",
    "patterns/git-operations.md": "system/git/git-operations.md",
    "patterns/session-management.md": "system/session/session-management.md",
    "patterns/module-composition-framework.md": "prompt_eng/patterns/composition/module-composition-framework.md",
    "patterns/implementation.md": "patterns/implementation-pattern.md",
    "patterns/coordination-patterns.md": "prompt_eng/patterns/orchestration/coordination-patterns.md",
    "patterns/execution-orchestration.md": "prompt_eng/patterns/orchestration/execution-orchestration.md",
    "patterns/prompt-construction-visualization.md": "prompt_eng/patterns/visualization/prompt-construction-visualization.md",
    "patterns/runtime-execution-dashboard.md": "prompt_eng/patterns/visualization/runtime-execution-dashboard.md",
    
    # Getting started modules - moved to domain/
    "getting-started/template-orchestration.md": "domain/adaptation/template-orchestration.md",
    "getting-started/domain-templates.md": "domain/templates/README.md",
    "getting-started/adaptation-validation.md": "domain/adaptation/adaptation-validation.md",
    "getting-started/domain-adaptation.md": "domain/adaptation/domain-adaptation.md",
    
    # Development modules
    "development/knowledge-management.md": "development/documentation/knowledge-management.md",
    
    # Security modules
    "security/audit.md": "system/security/audit.md",
    
    # System modules
    "system/git/worktree-isolation.md": "system/git/worktree-isolation.md",
    
    # Meta modules
    "meta/framework-evolver.md": "meta/evolution/framework-evolver.md",
    "meta/adaptation-validation.md": "meta/validation/adaptation-validation.md",
    
    # Additional quality modules that may be missing
    "quality/comprehensive-testing.md": "system/quality/comprehensive-testing.md",
    "quality/quality-validation.md": "system/quality/quality-validation.md",
    "quality/domain-documentation.md": "system/quality/domain-documentation.md",
    "quality/security-validation.md": "system/quality/security-validation.md",
    "quality/setup-validation.md": "system/quality/setup-validation.md",
    "quality/feature-validation.md": "system/quality/feature-validation.md",
    "quality/compliance-validation.md": "system/quality/compliance-validation.md",
    "quality/general-validation.md": "system/quality/general-validation.md",
    
    # Pattern modules - more specific paths
    "patterns/thinking/critical-thinking-pattern.md": "prompt_eng/patterns/thinking/critical-thinking-pattern.md",
    "patterns/composition/module-composition-framework.md": "prompt_eng/patterns/composition/module-composition-framework.md",
    "patterns/orchestration/coordination-patterns.md": "prompt_eng/patterns/orchestration/coordination-patterns.md",
    "patterns/orchestration/execution-orchestration.md": "prompt_eng/patterns/orchestration/execution-orchestration.md",
    "patterns/visualization/prompt-construction-visualization.md": "prompt_eng/patterns/visualization/prompt-construction-visualization.md",
    "patterns/visualization/runtime-execution-dashboard.md": "prompt_eng/patterns/visualization/runtime-execution-dashboard.md",
    "patterns/thinking-pattern-template.md": "prompt_eng/patterns/thinking/thinking-pattern-template.md",
    "patterns/optimization.md": "patterns/performance-optimization.md",
    
    # Getting started modules - more specific paths
    "getting-started/template-systems.md": "domain/templates/template-systems.md",
    "getting-started/domain-specific-validation.md": "domain/validation/domain-specific-validation.md",
    
    # Development modules - more specific paths
    "development/complex-feature-development.md": "development/feature-development.md",
    "development/configuration-analysis.md": "development/analysis/configuration-analysis.md",
    "development/conventional-commits.md": "development/git/conventional-commits.md",
    "development/reproduce-issue.md": "development/debugging/reproduce-issue.md",
    
    # Planning modules
    "planning/prd-generation.md": "planning/prd/prd-generation.md",
    "planning/mvp-strategy.md": "planning/strategy/mvp-strategy.md",
    "planning/intelligent-prd.md": "planning/prd/intelligent-prd.md",
    "planning/prd-core.md": "planning/prd/prd-core.md",
    
    # Testing modules
    "testing/comprehensive-testing.md": "system/testing/comprehensive-testing.md",
    "modules/testing/iterative-testing.md": "system/testing/iterative-testing.md",
    "modules/planning/mvp-strategy.md": "planning/strategy/mvp-strategy.md",
    
    # System modules - git
    "system/git/git-operations.md": "system/git/git-operations.md",
}

def fix_references_in_file(file_path, dry_run=False):
    """Fix broken references in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    fixes_made = []
    
    # Fix each broken reference
    for broken_ref, correct_ref in REFERENCE_FIXES.items():
        # Find all variations of the reference
        patterns = [
            # Direct reference patterns
            f"\\[([^\\]]+)\\]\\({re.escape(broken_ref)}\\)",
            f"\\[([^\\]]+)\\]\\(\\.\\.\\/+{re.escape(broken_ref)}\\)",
            f"\\[([^\\]]+)\\]\\(\\.\\.\\/\\.\\.\\/+{re.escape(broken_ref)}\\)",
            # Simple text references
            f"\\b{re.escape(broken_ref)}\\b",
            f"\\.\\.\\/+{re.escape(broken_ref)}\\b",
            f"\\.\\.\\/\\.\\.\\/+{re.escape(broken_ref)}\\b",
        ]
        
        for pattern in patterns:
            matches = list(re.finditer(pattern, content))
            if matches:
                for match in reversed(matches):  # Process in reverse to maintain positions
                    if match.groups():
                        # It's a markdown link
                        link_text = match.group(1)
                        # Calculate relative path from current file to target
                        current_dir = os.path.dirname(file_path)
                        target_path = os.path.join('.claude', correct_ref)
                        rel_path = os.path.relpath(target_path, current_dir)
                        replacement = f"[{link_text}]({rel_path})"
                    else:
                        # It's a simple text reference
                        # Calculate relative path
                        current_dir = os.path.dirname(file_path)
                        target_path = os.path.join('.claude', correct_ref)
                        rel_path = os.path.relpath(target_path, current_dir)
                        replacement = rel_path
                    
                    content = content[:match.start()] + replacement + content[match.end():]
                    fixes_made.append(f"{broken_ref} → {correct_ref}")
    
    if content != original_content:
        if not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        return fixes_made
    return []

def fix_all_references(dry_run=False):
    """Fix references in all markdown files."""
    fixed_files = {}
    
    # Find all markdown files in .claude/modules/
    modules_dir = Path('.claude/modules')
    for md_file in modules_dir.rglob('*.md'):
        fixes = fix_references_in_file(md_file, dry_run)
        if fixes:
            fixed_files[str(md_file)] = fixes
    
    return fixed_files

def main():
    """Run the reference fixer."""
    import argparse
    parser = argparse.ArgumentParser(description='Fix broken module references')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be fixed without making changes')
    args = parser.parse_args()
    
    print("🔍 Scanning for broken references...")
    fixed_files = fix_all_references(args.dry_run)
    
    if fixed_files:
        print(f"\n{'DRY RUN - ' if args.dry_run else ''}Fixed references in {len(fixed_files)} files:\n")
        for file_path, fixes in sorted(fixed_files.items()):
            print(f"📄 {file_path}")
            for fix in fixes:
                print(f"   ✅ {fix}")
            print()
        
        total_fixes = sum(len(fixes) for fixes in fixed_files.values())
        print(f"{'Would fix' if args.dry_run else 'Fixed'} {total_fixes} broken references total.")
        
        if args.dry_run:
            print("\nRun without --dry-run to apply these fixes.")
    else:
        print("✅ No broken references found to fix!")
    
    # Save fix report
    report = {
        'dry_run': args.dry_run,
        'files_fixed': len(fixed_files),
        'total_fixes': sum(len(fixes) for fixes in fixed_files.values()),
        'fixes_by_file': fixed_files,
        'reference_mapping': REFERENCE_FIXES
    }
    
    with open('reference_fix_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📊 Fix report saved to reference_fix_report.json")

if __name__ == "__main__":
    main()