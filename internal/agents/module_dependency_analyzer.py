#!/usr/bin/env python3
"""
Module Dependency Analysis Script
Analyzes cross-references in .claude/modules/ directory
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple

class ModuleDependencyAnalyzer:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.modules_path = self.base_path / ".claude" / "modules"
        self.references = defaultdict(set)
        self.broken_references = defaultdict(set)
        self.circular_dependencies = []
        
    def analyze(self):
        """Main analysis function"""
        print("Starting module dependency analysis...")
        
        # Find all markdown files
        all_modules = list(self.modules_path.rglob("*.md"))
        print(f"Found {len(all_modules)} module files")
        
        # Extract references from each module
        for module_file in all_modules:
            self._extract_references(module_file)
            
        # Check for broken references
        self._check_broken_references()
        
        # Check for circular dependencies
        self._check_circular_dependencies()
        
        # Generate report
        return self._generate_report()
    
    def _extract_references(self, module_file: Path):
        """Extract all module references from a file"""
        try:
            with open(module_file, 'r') as f:
                content = f.read()
                
            # Pattern to match module references
            pattern = r'(?:modules/|quality/|security/|patterns/|development/|planning/|testing/|meta/|getting-started/|system/)[a-zA-Z0-9/_-]+\.md'
            
            matches = re.findall(pattern, content)
            
            # Store relative path from modules directory
            relative_path = str(module_file.relative_to(self.modules_path))
            
            for match in matches:
                self.references[relative_path].add(match)
                
        except Exception as e:
            print(f"Error reading {module_file}: {e}")
    
    def _check_broken_references(self):
        """Check which references point to non-existent files"""
        for module, refs in self.references.items():
            for ref in refs:
                # Check if referenced file exists
                ref_path = self.modules_path / ref
                if not ref_path.exists():
                    self.broken_references[module].add(ref)
    
    def _check_circular_dependencies(self):
        """Detect circular dependencies between modules"""
        for module_a, refs_a in self.references.items():
            for ref in refs_a:
                # Skip if reference is broken
                if ref in self.broken_references[module_a]:
                    continue
                    
                # Check if referenced module also references back
                ref_relative = ref
                if ref_relative in self.references:
                    refs_b = self.references[ref_relative]
                    if module_a in refs_b or f"modules/{module_a}" in refs_b:
                        if (ref_relative, module_a) not in self.circular_dependencies:
                            self.circular_dependencies.append((module_a, ref_relative))
    
    def _generate_report(self) -> Dict:
        """Generate comprehensive analysis report"""
        # Count statistics
        total_modules = len(self.references)
        total_references = sum(len(refs) for refs in self.references.values())
        total_broken = sum(len(refs) for refs in self.broken_references.values())
        
        # Find modules with most dependencies
        dependency_counts = {
            module: len(refs) for module, refs in self.references.items()
        }
        most_dependent = sorted(dependency_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # Find most referenced modules
        referenced_counts = defaultdict(int)
        for refs in self.references.values():
            for ref in refs:
                referenced_counts[ref] += 1
        most_referenced = sorted(referenced_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # Find isolated modules (no dependencies and not referenced)
        all_referenced = set()
        for refs in self.references.values():
            all_referenced.update(refs)
        
        isolated_modules = []
        for module in self.references.keys():
            if len(self.references[module]) == 0 and module not in all_referenced:
                isolated_modules.append(module)
        
        report = {
            "summary": {
                "total_modules": total_modules,
                "total_references": total_references,
                "total_broken_references": total_broken,
                "broken_percentage": round((total_broken / total_references * 100) if total_references > 0 else 0, 2),
                "circular_dependencies_count": len(self.circular_dependencies)
            },
            "broken_references": {
                module: list(refs) for module, refs in self.broken_references.items() 
                if refs
            },
            "circular_dependencies": self.circular_dependencies,
            "most_dependent_modules": most_dependent,
            "most_referenced_modules": most_referenced,
            "isolated_modules": isolated_modules,
            "problematic_patterns": self._identify_problematic_patterns()
        }
        
        return report
    
    def _identify_problematic_patterns(self) -> List[Dict]:
        """Identify problematic dependency patterns"""
        patterns = []
        
        # Pattern 1: Modules with >50% broken references
        for module, refs in self.references.items():
            if refs:
                broken_count = len(self.broken_references.get(module, set()))
                if broken_count / len(refs) > 0.5:
                    patterns.append({
                        "type": "high_broken_reference_ratio",
                        "module": module,
                        "total_refs": len(refs),
                        "broken_refs": broken_count,
                        "ratio": round(broken_count / len(refs) * 100, 2)
                    })
        
        # Pattern 2: Deep dependency chains (modules that reference modules that reference modules)
        # This is simplified - just checking 2-level dependencies
        for module, refs in self.references.items():
            deep_deps = set()
            for ref in refs:
                if ref in self.references:
                    deep_deps.update(self.references[ref])
            if len(deep_deps) > 10:
                patterns.append({
                    "type": "deep_dependency_chain",
                    "module": module,
                    "direct_deps": len(refs),
                    "indirect_deps": len(deep_deps)
                })
        
        return patterns


def main():
    # Get the project root
    project_root = "/Users/smenssink/Documents/Github/claude-code-modular-prompts"
    
    analyzer = ModuleDependencyAnalyzer(project_root)
    report = analyzer.analyze()
    
    # Save report to JSON
    output_file = Path(project_root) / "module_dependency_analysis.json"
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    print("\n=== MODULE DEPENDENCY ANALYSIS SUMMARY ===")
    print(f"Total modules analyzed: {report['summary']['total_modules']}")
    print(f"Total cross-references: {report['summary']['total_references']}")
    print(f"Broken references: {report['summary']['total_broken_references']} ({report['summary']['broken_percentage']}%)")
    print(f"Circular dependencies: {report['summary']['circular_dependencies_count']}")
    
    print("\n=== TOP 5 MODULES WITH BROKEN REFERENCES ===")
    broken_sorted = sorted(
        [(m, len(refs)) for m, refs in report['broken_references'].items()],
        key=lambda x: x[1],
        reverse=True
    )[:5]
    for module, count in broken_sorted:
        print(f"  {module}: {count} broken references")
    
    print("\n=== CIRCULAR DEPENDENCIES ===")
    for dep in report['circular_dependencies'][:5]:
        print(f"  {dep[0]} <-> {dep[1]}")
    
    print(f"\nFull report saved to: {output_file}")


if __name__ == "__main__":
    main()