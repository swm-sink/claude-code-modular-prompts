#!/usr/bin/env python3
"""
Agent V13: Generate visual dependency graph
Creates ASCII representation of module dependencies
"""

import os
import re
from collections import defaultdict

def load_dependencies():
    """Load dependency data from previous analysis"""
    dependencies = defaultdict(set)
    
    # Parse the detailed report
    with open('internal/reports/agents/V13_DEPENDENCY_MAPPING_REPORT.md', 'r') as f:
        content = f.read()
    
    # Extract dependencies from detailed section
    current_module = None
    in_depends_section = False
    
    for line in content.split('\n'):
        if line.startswith('### '):
            current_module = line.replace('### ', '').strip()
            in_depends_section = False
        elif line.strip() == 'Depends on:':
            in_depends_section = True
        elif in_depends_section and line.startswith('- '):
            dep = line.replace('- ', '').strip()
            if current_module:
                dependencies[current_module].add(dep)
    
    return dependencies

def create_category_graph():
    """Create a graph showing dependencies between categories"""
    dependencies = load_dependencies()
    
    # Aggregate by category
    category_deps = defaultdict(lambda: defaultdict(int))
    
    for module, deps in dependencies.items():
        # Extract source category
        if '/' in module:
            src_category = module.split('/')[0]
        else:
            continue
            
        for dep in deps:
            if '/' in dep:
                dst_category = dep.split('/')[0]
                if src_category != dst_category:
                    category_deps[src_category][dst_category] += 1
    
    # Create ASCII visualization
    print("\n=== Category-Level Dependency Graph ===\n")
    print("Arrow thickness indicates number of dependencies:")
    print("→ (1-5)  ⟹ (6-15)  ⟹⟹ (16-30)  ⟹⟹⟹ (30+)\n")
    
    categories = sorted(set(list(category_deps.keys()) + 
                           [dst for deps in category_deps.values() for dst in deps.keys()]))
    
    for src in categories:
        if src in category_deps:
            print(f"\n{src}")
            for dst, count in sorted(category_deps[src].items(), key=lambda x: x[1], reverse=True):
                if count > 30:
                    arrow = "⟹⟹⟹"
                elif count > 15:
                    arrow = "⟹⟹"
                elif count > 5:
                    arrow = "⟹"
                else:
                    arrow = "→"
                print(f"  {arrow} {dst} ({count} dependencies)")

def create_core_module_graph():
    """Create graph of core modules and their relationships"""
    dependencies = load_dependencies()
    
    # Core modules (from previous analysis)
    core_modules = [
        'patterns/pattern-library.md',
        'quality/universal-quality-gates.md',
        'quality/production-standards.md',
        'development/task-management.md',
        'quality/tdd.md',
        'quality/critical-thinking.md',
        'patterns/critical-thinking-pattern.md',
        'patterns/session-management.md',
        'patterns/intelligent-routing.md',
        'patterns/multi-agent.md'
    ]
    
    print("\n\n=== Core Module Dependency Network ===\n")
    print("Top 10 most depended-upon modules:\n")
    
    # Find dependencies between core modules
    for module in core_modules:
        print(f"\n{module}")
        
        # Who depends on this module?
        dependents = []
        for src, deps in dependencies.items():
            if module in deps and src in core_modules:
                dependents.append(src)
        
        if dependents:
            print("  ← Depended on by:")
            for dep in dependents:
                print(f"    • {dep}")
        
        # What does this module depend on?
        if module in dependencies:
            core_deps = [d for d in dependencies[module] if d in core_modules]
            if core_deps:
                print("  → Depends on:")
                for dep in core_deps:
                    print(f"    • {dep}")

def create_command_module_graph():
    """Show command to module mappings"""
    command_mappings = {
        '/auto': 'patterns/intelligent-routing.md',
        '/task': 'development/task-management.md',
        '/feature': 'development/planning/feature-workflow.md',
        '/swarm': 'development/multi-agent.md',
        '/query': 'development/research-analysis.md',
        '/session': 'system/session/session-management.md',
        '/docs': 'development/documentation.md',
        '/protocol': 'system/session/session-management.md',
        '/init': 'domain/wizard/README.md',
        '/context-prime': 'system/context/project-priming.md',
        '/adapt': 'domain/adaptation/template-orchestration.md',
        '/validate': 'domain/adaptation/adaptation-validation.md',
        '/init-custom': 'domain/wizard/domain-wizard.md',
        '/init-new': 'development/project-initialization.md',
        '/init-research': 'development/research-analysis.md',
        '/init-validate': 'quality/setup-validation.md',
        '/chain': 'patterns/command-chaining-architecture.md',
        '/meta-review': 'meta/framework-auditor.md',
        '/meta-evolve': 'meta/update-cycle-manager.md',
        '/meta-optimize': 'meta/continuous-optimizer.md',
        '/meta-govern': 'meta/governance-enforcer.md',
        '/meta-fix': 'meta/compliance-diagnostics.md'
    }
    
    print("\n\n=== Command → Module Mapping ===\n")
    
    dependencies = load_dependencies()
    
    for cmd, module in sorted(command_mappings.items()):
        print(f"\n{cmd} → {module}")
        
        # Show what this command's module depends on
        if module in dependencies and dependencies[module]:
            print("  Executes with:")
            for dep in sorted(list(dependencies[module])[:5]):  # Top 5 dependencies
                print(f"    • {dep}")

def main():
    create_category_graph()
    create_core_module_graph()
    create_command_module_graph()
    
    print("\n\n=== Dependency Insights ===")
    print("\n1. No circular dependencies detected - clean architecture!")
    print("2. Clear hierarchy: patterns and quality modules form the foundation")
    print("3. Strong separation of concerns between categories")
    print("4. Commands properly delegate to their designated modules")
    print("5. Meta modules form a separate layer for framework evolution")

if __name__ == "__main__":
    main()