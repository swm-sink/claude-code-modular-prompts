#!/usr/bin/env python3
"""Check for concept duplications across framework modules."""

import os
import re
from collections import defaultdict
from pathlib import Path

# Key concepts to check for duplication
CONCEPTS_TO_CHECK = {
    'tdd_concepts': [
        r'red.green.refactor',
        r'test.driven.development',
        r'tdd.cycle',
        r'red_phase.*green_phase.*refactor_phase'
    ],
    'prd_concepts': [
        r'prd_template',
        r'executive_summary.*user_stories.*technical_requirements',
        r'requirement_quality_standards',
        r'user_story_standards'
    ],
    'coverage_requirements': [
        r'coverage.*90%',
        r'coverage.*85%',
        r'coverage.*95%',
        r'line_coverage.*branch_coverage'
    ],
    'session_management': [
        r'session_integration',
        r'github.*issue.*tracking',
        r'session_lifecycle',
        r'session_documentation'
    ],
    'critical_thinking': [
        r'deep_thinking.*30.seconds',
        r'critical_thinking.*enforcement',
        r'pre_action_analysis',
        r'forensic_verification'
    ]
}

def find_modules(base_path):
    """Find all .md module files."""
    modules = []
    for root, dirs, files in os.walk(base_path):
        # Skip archive directories
        if 'archive' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                modules.append(os.path.join(root, file))
    return modules

def check_concepts_in_file(filepath, concepts):
    """Check which concepts appear in a file."""
    found_concepts = defaultdict(list)
    
    try:
        with open(filepath, 'r') as f:
            content = f.read().lower()
            
        for concept_type, patterns in concepts.items():
            for pattern in patterns:
                if re.search(pattern.lower(), content):
                    found_concepts[concept_type].append(pattern)
    
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    
    return found_concepts

def main():
    """Main function to check for duplications."""
    base_path = Path(__file__).parent.parent
    modules_path = base_path / '.claude' / 'modules'
    
    modules = find_modules(modules_path)
    
    # Track where each concept appears
    concept_locations = defaultdict(list)
    
    for module in modules:
        rel_path = os.path.relpath(module, base_path)
        found = check_concepts_in_file(module, CONCEPTS_TO_CHECK)
        
        for concept_type, patterns in found.items():
            if patterns:
                concept_locations[concept_type].append(rel_path)
    
    # Report findings
    print("# Concept Duplication Check Report\n")
    print(f"Checked {len(modules)} module files\n")
    
    duplications_found = False
    
    for concept_type, locations in concept_locations.items():
        if len(locations) > 1:
            duplications_found = True
            print(f"## {concept_type}")
            print(f"Found in {len(locations)} locations:")
            for loc in sorted(locations):
                print(f"  - {loc}")
            print()
    
    if not duplications_found:
        print("✅ No concept duplications found!")
    else:
        print("\n⚠️  Concept duplications detected. Review the above locations.")
    
    # Check for proper references
    print("\n## Reference Check")
    print("Checking if modules properly reference canonical sources...\n")
    
    # Check specific reference patterns
    reference_checks = {
        'quality/tdd.md': r'quality/tdd\.md',
        'planning/prd-core.md': r'planning/prd-core\.md',
        'patterns/session-management.md': r'patterns/session-management\.md'
    }
    
    for module in modules:
        if 'prd-core.md' in module:
            continue  # Skip the canonical source itself
            
        rel_path = os.path.relpath(module, base_path)
        
        # Check if PRD-related modules reference prd-core
        if 'planning/' in rel_path and ('prd' in rel_path or 'intelligent' in rel_path):
            with open(module, 'r') as f:
                content = f.read()
            if 'prd-core.md' not in content and 'prd-core' not in os.path.basename(module):
                print(f"⚠️  {rel_path} may need to reference planning/prd-core.md")

if __name__ == '__main__':
    main()