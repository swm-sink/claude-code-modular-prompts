#!/usr/bin/env python3
"""
Agent V13: Module Dependency Analyzer
Analyzes cross-references and dependencies between modules
"""

import os
import re
from collections import defaultdict
from pathlib import Path

def extract_module_references(file_path):
    """Extract references to other modules from a markdown file"""
    references = set()
    
    with open(file_path, 'r') as f:
        content = f.read()
        
    # Pattern 1: Direct module references like modules/development/task-management.md
    pattern1 = r'modules/([^/\s]+)/([^/\s]+)\.md'
    matches1 = re.findall(pattern1, content)
    for category, module in matches1:
        references.add(f"modules/{category}/{module}.md")
    
    # Pattern 2: References in canonical_source tags
    pattern2 = r'<canonical_source>([^<]+)</canonical_source>'
    matches2 = re.findall(pattern2, content)
    for ref in matches2:
        if 'modules/' in ref or 'system/' in ref or 'prompt_eng/' in ref:
            references.add(ref.strip())
    
    # Pattern 3: Module references in cmd tags
    pattern3 = r'module\s*=\s*"([^"]+)"'
    matches3 = re.findall(pattern3, content)
    for ref in matches3:
        if not ref.startswith('.'):
            references.add(ref)
    
    # Pattern 4: References to patterns, quality, etc.
    pattern4 = r'(patterns|quality|development|security|system|meta)/([^/\s]+)\.md'
    matches4 = re.findall(pattern4, content)
    for category, module in matches4:
        references.add(f"{category}/{module}.md")
    
    # Pattern 5: Cross-references in documentation
    pattern5 = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    matches5 = re.findall(pattern5, content)
    for _, ref in matches5:
        if any(prefix in ref for prefix in ['modules/', 'system/', 'prompt_eng/', 'patterns/', 'quality/']):
            references.add(ref.strip())
    
    return references

def build_dependency_graph():
    """Build complete dependency graph for all modules"""
    dependencies = defaultdict(set)
    module_files = []
    
    # Find all module files
    for root, dirs, files in os.walk('.claude'):
        # Skip archive directories
        if 'archive' in root:
            continue
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                # Include modules, system, prompt_eng directories
                if any(dir in path for dir in ['/modules/', '/system/', '/prompt_eng/', '/domain/', '/development/', '/meta/']):
                    module_files.append(path)
    
    # Analyze each module
    for module_path in module_files:
        # Normalize path for consistency
        module_key = module_path.replace('.claude/', '').replace('\\', '/')
        refs = extract_module_references(module_path)
        
        for ref in refs:
            # Skip self-references
            if ref != module_key and not ref.startswith('.'):
                dependencies[module_key].add(ref)
    
    return dependencies, module_files

def find_core_modules(dependencies):
    """Find modules that many others depend on"""
    dependency_count = defaultdict(int)
    
    for module, deps in dependencies.items():
        for dep in deps:
            dependency_count[dep] += 1
    
    # Sort by dependency count
    core_modules = sorted(dependency_count.items(), key=lambda x: x[1], reverse=True)
    return core_modules

def find_circular_dependencies(dependencies):
    """Find circular dependencies in the graph"""
    circular = []
    
    def has_cycle(node, visited, rec_stack, path):
        visited[node] = True
        rec_stack[node] = True
        path.append(node)
        
        if node in dependencies:
            for neighbor in dependencies[node]:
                if neighbor not in visited:
                    if has_cycle(neighbor, visited, rec_stack, path):
                        return True
                elif rec_stack.get(neighbor, False):
                    # Found cycle
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    circular.append(cycle)
                    return True
        
        path.pop()
        rec_stack[node] = False
        return False
    
    visited = {}
    for module in dependencies:
        if module not in visited:
            has_cycle(module, visited, {}, [])
    
    return circular

def generate_dependency_matrix(dependencies, module_files):
    """Generate a dependency matrix"""
    # Get unique module names
    all_modules = set()
    for module in module_files:
        module_key = module.replace('.claude/', '').replace('\\', '/')
        all_modules.add(module_key)
    
    for module, deps in dependencies.items():
        all_modules.add(module)
        all_modules.update(deps)
    
    # Filter to only actual modules (99 modules)
    module_list = sorted([m for m in all_modules if any(prefix in m for prefix in ['modules/', 'system/', 'prompt_eng/', 'domain/', 'development/', 'meta/'])])
    
    return module_list, dependencies

def main():
    print("=== Agent V13: Module Dependency Analysis ===\n")
    
    # Build dependency graph
    print("Building dependency graph...")
    dependencies, module_files = build_dependency_graph()
    
    print(f"Total modules analyzed: {len(module_files)}")
    print(f"Modules with dependencies: {len(dependencies)}")
    
    # Find core modules
    print("\n=== Core Modules (Most Depended Upon) ===")
    core_modules = find_core_modules(dependencies)
    for module, count in core_modules[:20]:  # Top 20
        print(f"{count:3d} dependencies: {module}")
    
    # Find circular dependencies
    print("\n=== Circular Dependencies ===")
    circular = find_circular_dependencies(dependencies)
    if circular:
        for cycle in circular:
            print(f"Circular: {' -> '.join(cycle)}")
    else:
        print("No circular dependencies found!")
    
    # Generate statistics
    print("\n=== Dependency Statistics ===")
    dep_counts = [len(deps) for deps in dependencies.values()]
    if dep_counts:
        print(f"Average dependencies per module: {sum(dep_counts) / len(dep_counts):.2f}")
        print(f"Max dependencies: {max(dep_counts)}")
        print(f"Min dependencies: {min(dep_counts)}")
    
    # Modules with no dependencies
    print("\n=== Standalone Modules (No Dependencies) ===")
    standalone = []
    for module in module_files:
        module_key = module.replace('.claude/', '').replace('\\', '/')
        if module_key not in dependencies or len(dependencies[module_key]) == 0:
            standalone.append(module_key)
    
    print(f"Found {len(standalone)} standalone modules")
    for module in sorted(standalone)[:10]:  # Show first 10
        print(f"  - {module}")
    
    # Save detailed report
    print("\n=== Generating Detailed Report ===")
    module_list, deps = generate_dependency_matrix(dependencies, module_files)
    
    with open('internal/reports/agents/V13_DEPENDENCY_MAPPING_REPORT.md', 'w') as f:
        f.write("# Agent V13: Module Dependency Mapping Report\n\n")
        f.write(f"## Summary\n")
        f.write(f"- Total modules analyzed: {len(module_files)}\n")
        f.write(f"- Modules with dependencies: {len(dependencies)}\n")
        f.write(f"- Circular dependencies found: {len(circular)}\n\n")
        
        f.write("## Core Modules (Top 20 Most Depended Upon)\n\n")
        for module, count in core_modules[:20]:
            f.write(f"1. **{module}** - {count} dependencies\n")
        
        f.write("\n## Detailed Dependency Map\n\n")
        for module in sorted(dependencies.keys()):
            if dependencies[module]:
                f.write(f"### {module}\n")
                f.write("Depends on:\n")
                for dep in sorted(dependencies[module]):
                    f.write(f"- {dep}\n")
                f.write("\n")
    
    print("Report saved to internal/reports/agents/V13_DEPENDENCY_MAPPING_REPORT.md")

if __name__ == "__main__":
    main()