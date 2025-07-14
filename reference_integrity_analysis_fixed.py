#!/usr/bin/env python3
"""
Agent V6: Reference Integrity Validator - Fixed Version
Comprehensive analysis of all cross-references in the Claude Code Modular Prompts framework.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict, Counter
import sys

class ReferenceIntegrityValidator:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.results = {
            'commands_analyzed': 0,
            'modules_analyzed': 0,
            'total_references': 0,
            'broken_references': [],
            'orphaned_modules': [],
            'circular_dependencies': [],
            'reference_patterns': defaultdict(int),
            'module_usage_count': defaultdict(int),
            'commands_to_modules': defaultdict(list),
            'modules_to_modules': defaultdict(list),
            'error_details': []
        }
        
    def analyze_framework(self):
        """Main analysis method"""
        print("🔍 Starting Reference Integrity Analysis...")
        
        # 1. Find all command files
        commands_dir = self.base_path / '.claude' / 'commands'
        if not commands_dir.exists():
            self.results['error_details'].append("Commands directory not found")
            return
            
        # 2. Find all module files
        modules_dir = self.base_path / '.claude' / 'modules'
        if not modules_dir.exists():
            self.results['error_details'].append("Modules directory not found")
            return
            
        # 3. Get all existing modules with multiple path resolution strategies
        existing_modules = self.get_existing_modules()
        
        # 4. Analyze command references
        self.analyze_command_references(commands_dir, existing_modules)
        
        # 5. Analyze module-to-module references
        self.analyze_module_references(modules_dir, existing_modules)
        
        # 6. Find orphaned modules
        self.find_orphaned_modules(existing_modules)
        
        # 7. Detect circular dependencies
        self.detect_circular_dependencies()
        
        # 8. Check CLAUDE.md architecture declarations
        self.check_claude_md_references()
        
        print("✅ Analysis complete!")
        return self.results
    
    def get_existing_modules(self):
        """Get all existing module files with flexible path matching"""
        modules_dir = self.base_path / '.claude' / 'modules'
        system_dir = self.base_path / '.claude' / 'system'
        prompt_eng_dir = self.base_path / '.claude' / 'prompt_eng'
        domain_dir = self.base_path / '.claude' / 'domain'
        
        existing_modules = {}  # Use dict to track multiple path formats
        
        for base_dir in [modules_dir, system_dir, prompt_eng_dir, domain_dir]:
            if base_dir.exists():
                for file_path in base_dir.rglob('*.md'):
                    # Convert to relative path from .claude/
                    rel_path = file_path.relative_to(self.base_path / '.claude')
                    
                    # Store both full path and basename
                    existing_modules[str(rel_path)] = file_path
                    
                    # Also store with different potential prefixes
                    if rel_path.parts[0] == 'modules':
                        # Store without modules/ prefix
                        short_path = '/'.join(rel_path.parts[1:])
                        existing_modules[short_path] = file_path
                    elif rel_path.parts[0] == 'system':
                        # Store without system/ prefix
                        short_path = '/'.join(rel_path.parts[1:])
                        existing_modules[short_path] = file_path
                    
                    # Store just the filename
                    existing_modules[file_path.name] = file_path
                    
        return existing_modules
    
    def analyze_command_references(self, commands_dir, existing_modules):
        """Analyze references in command files"""
        for cmd_file in commands_dir.glob('*.md'):
            self.results['commands_analyzed'] += 1
            
            try:
                content = cmd_file.read_text()
                
                # Find module references
                module_refs = self.extract_module_references(content)
                
                for ref in module_refs:
                    self.results['total_references'] += 1
                    
                    # Try to resolve the reference
                    resolved_path = self.resolve_reference(ref, existing_modules)
                    
                    if resolved_path:
                        self.results['module_usage_count'][resolved_path] += 1
                        self.results['commands_to_modules'][cmd_file.name].append(resolved_path)
                    else:
                        self.results['broken_references'].append({
                            'source': str(cmd_file),
                            'reference': ref,
                            'type': 'command_to_module'
                        })
                    
                    # Track reference patterns
                    pattern = self.get_reference_pattern(ref)
                    self.results['reference_patterns'][pattern] += 1
                    
            except Exception as e:
                self.results['error_details'].append(f"Error reading {cmd_file}: {e}")
    
    def analyze_module_references(self, modules_dir, existing_modules):
        """Analyze module-to-module references"""
        for module_file in modules_dir.rglob('*.md'):
            self.results['modules_analyzed'] += 1
            
            try:
                content = module_file.read_text()
                rel_path = module_file.relative_to(self.base_path / '.claude')
                
                # Find references to other modules
                module_refs = self.extract_module_references(content)
                
                for ref in module_refs:
                    self.results['total_references'] += 1
                    
                    # Try to resolve the reference
                    resolved_path = self.resolve_reference(ref, existing_modules)
                    
                    if resolved_path:
                        self.results['module_usage_count'][resolved_path] += 1
                        self.results['modules_to_modules'][str(rel_path)].append(resolved_path)
                    else:
                        self.results['broken_references'].append({
                            'source': str(module_file),
                            'reference': ref,
                            'type': 'module_to_module'
                        })
                        
            except Exception as e:
                self.results['error_details'].append(f"Error reading {module_file}: {e}")
    
    def resolve_reference(self, ref, existing_modules):
        """Try to resolve a reference to an actual file"""
        # Clean the reference
        ref = ref.strip().lstrip('/')
        
        # Try direct match first
        if ref in existing_modules:
            return str(existing_modules[ref].relative_to(self.base_path / '.claude'))
        
        # Try with modules/ prefix
        modules_ref = f"modules/{ref}"
        if modules_ref in existing_modules:
            return str(existing_modules[modules_ref].relative_to(self.base_path / '.claude'))
        
        # Try with system/ prefix
        system_ref = f"system/{ref}"
        if system_ref in existing_modules:
            return str(existing_modules[system_ref].relative_to(self.base_path / '.claude'))
        
        # Try with patterns/ prefix under modules
        if not ref.startswith('modules/') and not ref.startswith('system/'):
            patterns_ref = f"modules/patterns/{ref}"
            if patterns_ref in existing_modules:
                return str(existing_modules[patterns_ref].relative_to(self.base_path / '.claude'))
        
        # Try just the filename
        filename = ref.split('/')[-1]
        if filename in existing_modules:
            return str(existing_modules[filename].relative_to(self.base_path / '.claude'))
        
        return None
    
    def extract_module_references(self, content):
        """Extract module references from content"""
        references = []
        
        # Pattern 1: <module>path/to/module.md</module>
        pattern1 = r'<module[^>]*>([^<]+\.md)</module>'
        references.extend(re.findall(pattern1, content))
        
        # Pattern 2: module = "path/to/module.md"
        pattern2 = r'module\s*=\s*"([^"]+\.md)"'
        references.extend(re.findall(pattern2, content))
        
        # Pattern 3: <delegation target="modules/path/to/module.md">
        pattern3 = r'<delegation[^>]*target="([^"]+\.md)"'
        references.extend(re.findall(pattern3, content))
        
        # Pattern 4: Direct references to .md files
        pattern4 = r'(?:modules/|patterns/|development/|quality/|security/|system/)([^"\s\)]+\.md)'
        references.extend(re.findall(pattern4, content))
        
        # Pattern 5: .claude/modules/path/to/module.md
        pattern5 = r'\.claude/([^"\s]+\.md)'
        references.extend(re.findall(pattern5, content))
        
        return list(set(references))  # Remove duplicates
    
    def get_reference_pattern(self, ref):
        """Categorize reference patterns"""
        if 'patterns/' in ref:
            return 'pattern_module'
        elif 'development/' in ref:
            return 'development_module'
        elif 'meta/' in ref:
            return 'meta_module'
        elif 'quality/' in ref:
            return 'quality_module'
        elif 'security/' in ref:
            return 'security_module'
        elif 'system/' in ref:
            return 'system_module'
        else:
            return 'other'
    
    def find_orphaned_modules(self, existing_modules):
        """Find modules that are never referenced"""
        # Get all actual file paths
        actual_files = set()
        for key, file_path in existing_modules.items():
            if '/' in key:  # Only consider full paths
                actual_files.add(str(file_path.relative_to(self.base_path / '.claude')))
        
        used_modules = set(self.results['module_usage_count'].keys())
        
        for module in actual_files:
            if module not in used_modules:
                # Skip README files and certain special files
                if not any(skip in module.lower() for skip in ['readme', 'master_module_guide', 'usage']):
                    self.results['orphaned_modules'].append(module)
    
    def detect_circular_dependencies(self):
        """Detect circular dependencies in module references"""
        # Build dependency graph
        graph = self.results['modules_to_modules']
        
        def dfs(node, visited, rec_stack, path):
            visited.add(node)
            rec_stack.add(node)
            current_path = path + [node]
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    cycle = dfs(neighbor, visited, rec_stack, current_path)
                    if cycle:
                        return cycle
                elif neighbor in rec_stack:
                    # Found a cycle
                    cycle_start = current_path.index(neighbor)
                    return current_path[cycle_start:] + [neighbor]
            
            rec_stack.remove(node)
            return None
        
        visited = set()
        for node in graph:
            if node not in visited:
                cycle = dfs(node, visited, set(), [])
                if cycle:
                    self.results['circular_dependencies'].append(cycle)
    
    def check_claude_md_references(self):
        """Check references declared in CLAUDE.md architecture section"""
        claude_md = self.base_path / 'CLAUDE.md'
        if not claude_md.exists():
            self.results['error_details'].append("CLAUDE.md not found")
            return
            
        try:
            content = claude_md.read_text()
            
            # Find architecture section
            arch_match = re.search(r'<architecture>.*?</architecture>', content, re.DOTALL)
            if arch_match:
                arch_content = arch_match.group(0)
                
                # Extract declared command->module mappings
                cmd_pattern = r'<cmd name = "([^"]+)" module = "([^"]+)"'
                declared_mappings = re.findall(cmd_pattern, arch_content)
                
                existing_modules = self.get_existing_modules()
                
                for cmd_name, module_ref in declared_mappings:
                    # Check if the declared module exists
                    resolved_path = self.resolve_reference(module_ref, existing_modules)
                    if not resolved_path:
                        self.results['broken_references'].append({
                            'source': 'CLAUDE.md',
                            'reference': module_ref,
                            'type': 'architecture_declaration',
                            'command': cmd_name
                        })
                        
        except Exception as e:
            self.results['error_details'].append(f"Error analyzing CLAUDE.md: {e}")
    
    def generate_report(self):
        """Generate comprehensive report"""
        report = []
        
        report.append("# Agent V6: Reference Integrity Validation Report")
        report.append(f"**Date**: {self.get_current_date()}")
        report.append(f"**Agent**: V6 - Reference Integrity Validator")
        report.append("")
        
        # Summary
        report.append("## Executive Summary")
        report.append(f"- **Commands Analyzed**: {self.results['commands_analyzed']}")
        report.append(f"- **Modules Analyzed**: {self.results['modules_analyzed']}")
        report.append(f"- **Total References Checked**: {self.results['total_references']}")
        report.append(f"- **Broken References**: {len(self.results['broken_references'])}")
        report.append(f"- **Orphaned Modules**: {len(self.results['orphaned_modules'])}")
        report.append(f"- **Circular Dependencies**: {len(self.results['circular_dependencies'])}")
        report.append("")
        
        # Reference Patterns Analysis
        report.append("## Reference Patterns Analysis")
        total_patterns = sum(self.results['reference_patterns'].values())
        if total_patterns > 0:
            for pattern, count in sorted(self.results['reference_patterns'].items(), key=lambda x: x[1], reverse=True):
                percentage = (count / total_patterns * 100)
                report.append(f"- **{pattern}**: {count} references ({percentage:.1f}%)")
        else:
            report.append("- No reference patterns detected")
        report.append("")
        
        # Broken References (show top 20)
        if self.results['broken_references']:
            report.append("## ❌ Broken References")
            report.append(f"**Total**: {len(self.results['broken_references'])}")
            report.append("")
            
            by_type = defaultdict(list)
            for ref in self.results['broken_references']:
                by_type[ref['type']].append(ref)
            
            for ref_type, refs in by_type.items():
                report.append(f"### {ref_type.replace('_', ' ').title()}")
                # Show first 10 examples
                for ref in refs[:10]:
                    report.append(f"- **Source**: `{ref['source']}`")
                    report.append(f"  - **Missing**: `{ref['reference']}`")
                    if 'command' in ref:
                        report.append(f"  - **Command**: `{ref['command']}`")
                    report.append("")
                
                if len(refs) > 10:
                    report.append(f"... and {len(refs) - 10} more")
                    report.append("")
        else:
            report.append("## ✅ No Broken References Found")
            report.append("")
        
        # Orphaned Modules (show first 20)
        if self.results['orphaned_modules']:
            report.append("## 🔍 Orphaned Modules")
            report.append(f"**Total**: {len(self.results['orphaned_modules'])}")
            report.append("")
            report.append("These modules exist but are never referenced:")
            for module in sorted(self.results['orphaned_modules'])[:20]:
                report.append(f"- `{module}`")
            if len(self.results['orphaned_modules']) > 20:
                report.append(f"... and {len(self.results['orphaned_modules']) - 20} more")
            report.append("")
        else:
            report.append("## ✅ No Orphaned Modules Found")
            report.append("")
        
        # Circular Dependencies
        if self.results['circular_dependencies']:
            report.append("## ⚠️ Circular Dependencies")
            report.append(f"**Total**: {len(self.results['circular_dependencies'])}")
            report.append("")
            for i, cycle in enumerate(self.results['circular_dependencies'], 1):
                report.append(f"### Cycle {i}")
                report.append(f"**Path**: {' → '.join(cycle)}")
                report.append("")
        else:
            report.append("## ✅ No Circular Dependencies Found")
            report.append("")
        
        # Module Usage Statistics
        report.append("## Module Usage Statistics")
        report.append("")
        report.append("### Most Referenced Modules")
        most_used = sorted(self.results['module_usage_count'].items(), key=lambda x: x[1], reverse=True)[:10]
        for module, count in most_used:
            report.append(f"- `{module}`: {count} references")
        report.append("")
        
        # Error Details
        if self.results['error_details']:
            report.append("## ⚠️ Analysis Errors")
            for error in self.results['error_details']:
                report.append(f"- {error}")
            report.append("")
        
        # Recommendations
        report.append("## 🎯 Recommendations")
        
        if self.results['broken_references']:
            report.append("### High Priority")
            report.append("- **Fix broken references** - These directly impact framework functionality")
            report.append("- **Validate CLAUDE.md architecture declarations** - Ensure alignment with actual implementation")
            report.append("")
        
        if self.results['orphaned_modules']:
            report.append("### Medium Priority")
            report.append("- **Review orphaned modules** - Archive unused modules or establish references")
            report.append("- **Update module documentation** - Ensure all modules have clear purposes")
            report.append("")
        
        if self.results['circular_dependencies']:
            report.append("### Low Priority")
            report.append("- **Resolve circular dependencies** - Refactor to eliminate cycles")
            report.append("- **Implement dependency graphs** - Visual representation of module relationships")
            report.append("")
        
        report.append("### General Improvements")
        report.append("- **Standardize reference patterns** - Consistent module reference format")
        report.append("- **Implement reference validation** - Automated checking in CI/CD")
        report.append("- **Create module registry** - Central index of all available modules")
        report.append("")
        
        # Framework Health Score
        total_issues = len(self.results['broken_references']) + len(self.results['circular_dependencies'])
        if total_issues == 0:
            health_score = 100
        elif total_issues <= 5:
            health_score = 95
        elif total_issues <= 10:
            health_score = 90
        elif total_issues <= 20:
            health_score = 85
        else:
            health_score = max(50, 100 - (total_issues * 2))
        
        report.append(f"## Framework Health Score: {health_score}%")
        report.append("")
        
        if health_score >= 95:
            report.append("🟢 **Excellent** - Framework reference integrity is strong")
        elif health_score >= 85:
            report.append("🟡 **Good** - Minor issues that should be addressed")
        elif health_score >= 75:
            report.append("🟠 **Fair** - Several issues requiring attention")
        else:
            report.append("🔴 **Poor** - Critical issues need immediate resolution")
        
        return '\n'.join(report)
    
    def get_current_date(self):
        """Get current date in standard format"""
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d')

def main():
    base_path = "/Users/smenssink/Documents/Github/claude-code-modular-prompts"
    
    validator = ReferenceIntegrityValidator(base_path)
    results = validator.analyze_framework()
    
    # Generate report
    report = validator.generate_report()
    
    # Write report
    output_path = f"{base_path}/agent-communications/v6-reference-integrity.md"
    with open(output_path, 'w') as f:
        f.write(report)
    
    print(f"📋 Report written to: {output_path}")
    
    # Also save raw results as JSON
    json_path = f"{base_path}/agent-communications/v6-reference-integrity-data.json"
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print(f"📊 Raw data saved to: {json_path}")

if __name__ == "__main__":
    main()