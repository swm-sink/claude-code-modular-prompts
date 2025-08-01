#!/usr/bin/env python3
"""
AI Consumption Validation Test Suite
Tests the effectiveness of XML tagging and modular architecture for AI understanding
"""

import os
import re
import yaml
import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

class AIConsumptionValidator:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.results = {
            'xml_navigation': {},
            'component_discovery': {},
            'workflow_assembly': {},
            'context_understanding': {},
            'errors': []
        }
        
    def validate_xml_navigation(self) -> Dict[str, bool]:
        """Test AI's ability to navigate using XML tags"""
        print("\n🔍 Testing XML Navigation Capabilities...")
        
        navigation_tests = {
            'metadata_presence': self._check_xml_metadata_presence(),
            'relationship_mapping': self._check_component_relationships(),
            'priority_guidance': self._check_priority_levels(),
            'memory_optimization': self._check_memory_priorities(),
            'layer_identification': self._check_progressive_layers()
        }
        
        self.results['xml_navigation'] = navigation_tests
        return navigation_tests
    
    def _check_xml_metadata_presence(self) -> bool:
        """Check if critical files have XML metadata"""
        critical_files = [
            'CLAUDE.md',
            'README.md',
            '.claude/commands/core/quick-command.md',
            '.claude/commands/core/build-command.md',
            '.claude/commands/core/assemble-command.md'
        ]
        
        found_count = 0
        for file_path in critical_files:
            full_path = self.base_path / file_path
            if full_path.exists():
                content = full_path.read_text()
                if '<!-- AI_METADATA_START -->' in content:
                    found_count += 1
                    
        success = found_count >= 3  # At least 3 critical files should have metadata
        print(f"  {'✅' if success else '❌'} XML Metadata Presence: {found_count}/{len(critical_files)} critical files tagged")
        return success
    
    def _check_component_relationships(self) -> bool:
        """Verify component compatibility matrix is accessible"""
        components_dir = self.base_path / '.claude/components'
        if not components_dir.exists():
            return False
            
        relationship_patterns = [
            r'<compatibility_matrix>',
            r'<required_components>',
            r'<incompatible_with>',
            r'compatibility.*=.*"(strong|weak|incompatible)"'
        ]
        
        found_relationships = 0
        for comp_file in components_dir.glob('*.md'):
            if comp_file.name in ['README.md', 'COMPONENT-LIBRARY-INDEX.md']:
                continue
            content = comp_file.read_text()
            for pattern in relationship_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    found_relationships += 1
                    break
                    
        success = found_relationships >= 10  # At least 10 components should have relationships
        print(f"  {'✅' if success else '❌'} Component Relationships: {found_relationships} components with defined relationships")
        return success
    
    def _check_priority_levels(self) -> bool:
        """Check if priority levels guide AI attention"""
        priority_patterns = [
            r'ai_consumption_priority.*=.*"(critical|high|medium|low)"',
            r'<priority>(critical|high|medium|low)</priority>'
        ]
        
        priority_files = 0
        for md_file in self.base_path.rglob('*.md'):
            content = md_file.read_text()
            for pattern in priority_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    priority_files += 1
                    break
                    
        success = priority_files >= 20
        print(f"  {'✅' if success else '❌'} Priority Guidance: {priority_files} files with AI priority levels")
        return success
    
    def _check_memory_priorities(self) -> bool:
        """Verify memory priority system for context management"""
        memory_pattern = r'memory_priority.*=.*"(\d+)"'
        
        memory_files = []
        for md_file in self.base_path.rglob('*.md'):
            content = md_file.read_text()
            match = re.search(memory_pattern, content)
            if match:
                priority = int(match.group(1))
                memory_files.append((md_file.name, priority))
                
        # Check if we have a good distribution
        high_priority = sum(1 for _, p in memory_files if p >= 8)
        medium_priority = sum(1 for _, p in memory_files if 5 <= p < 8)
        
        success = len(memory_files) >= 10 and high_priority >= 3
        print(f"  {'✅' if success else '❌'} Memory Optimization: {len(memory_files)} files with memory priorities")
        return success
    
    def _check_progressive_layers(self) -> bool:
        """Check Progressive Disclosure layer identification"""
        layer_pattern = r'progressive_disclosure_layer.*=.*"([123])"'
        
        layers_found = defaultdict(list)
        commands_dir = self.base_path / '.claude/commands'
        
        for cmd_file in commands_dir.rglob('*.md'):
            content = cmd_file.read_text()
            match = re.search(layer_pattern, content)
            if match:
                layer = match.group(1)
                layers_found[layer].append(cmd_file.name)
                
        success = len(layers_found) >= 2  # At least 2 layers should be defined
        print(f"  {'✅' if success else '❌'} Layer Identification: {len(layers_found)} progressive disclosure layers found")
        return success
    
    def validate_component_discovery(self) -> Dict[str, bool]:
        """Test AI's ability to discover and select components"""
        print("\n🧩 Testing Component Discovery Workflow...")
        
        discovery_tests = {
            'category_organization': self._check_component_categories(),
            'search_optimization': self._check_component_tags(),
            'usage_patterns': self._check_usage_examples(),
            'complexity_guidance': self._check_complexity_levels()
        }
        
        self.results['component_discovery'] = discovery_tests
        return discovery_tests
    
    def _check_component_categories(self) -> bool:
        """Verify components are properly categorized"""
        components_dir = self.base_path / '.claude/components'
        
        categories = defaultdict(int)
        for comp_file in components_dir.glob('*.md'):
            if comp_file.name in ['README.md', 'COMPONENT-LIBRARY-INDEX.md']:
                continue
            content = comp_file.read_text()
            # Look for category tags
            cat_match = re.search(r'category.*=.*"([^"]+)"', content)
            if cat_match:
                categories[cat_match.group(1)] += 1
                
        success = len(categories) >= 6  # At least 6 categories as documented
        print(f"  {'✅' if success else '❌'} Category Organization: {len(categories)} component categories found")
        return success
    
    def _check_component_tags(self) -> bool:
        """Check if components have searchable tags"""
        tag_patterns = [
            r'<tags>([^<]+)</tags>',
            r'tags.*=.*\[([^\]]+)\]',
            r'keywords.*:.*([^\n]+)'
        ]
        
        tagged_components = 0
        components_dir = self.base_path / '.claude/components'
        
        for comp_file in components_dir.glob('*.md'):
            if comp_file.name in ['README.md', 'COMPONENT-LIBRARY-INDEX.md']:
                continue
            content = comp_file.read_text()
            for pattern in tag_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    tagged_components += 1
                    break
                    
        success = tagged_components >= 30  # At least 30% should be tagged
        print(f"  {'✅' if success else '❌'} Search Optimization: {tagged_components} components with searchable tags")
        return success
    
    def _check_usage_examples(self) -> bool:
        """Verify components have usage examples"""
        example_patterns = [
            r'## Usage Example',
            r'### Example',
            r'```[^`]+example[^`]+```',
            r'<example>'
        ]
        
        components_with_examples = 0
        components_dir = self.base_path / '.claude/components'
        
        for comp_file in components_dir.glob('*.md'):
            if comp_file.name in ['README.md', 'COMPONENT-LIBRARY-INDEX.md']:
                continue
            content = comp_file.read_text()
            for pattern in example_patterns:
                if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
                    components_with_examples += 1
                    break
                    
        success = components_with_examples >= 40
        print(f"  {'✅' if success else '❌'} Usage Patterns: {components_with_examples} components with examples")
        return success
    
    def _check_complexity_levels(self) -> bool:
        """Check if components indicate complexity"""
        complexity_patterns = [
            r'complexity.*=.*"(simple|moderate|complex)"',
            r'<complexity_level>(beginner|intermediate|advanced|expert)</complexity_level>'
        ]
        
        complexity_marked = 0
        components_dir = self.base_path / '.claude/components'
        
        for comp_file in components_dir.glob('*.md'):
            if comp_file.name in ['README.md', 'COMPONENT-LIBRARY-INDEX.md']:
                continue
            content = comp_file.read_text()
            for pattern in complexity_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    complexity_marked += 1
                    break
                    
        success = complexity_marked >= 20
        print(f"  {'✅' if success else '❌'} Complexity Guidance: {complexity_marked} components with complexity levels")
        return success
    
    def validate_workflow_assembly(self) -> Dict[str, bool]:
        """Test AI's ability to assemble components into commands"""
        print("\n🔄 Testing Workflow Assembly Capabilities...")
        
        assembly_tests = {
            'assembly_templates': self._check_assembly_templates(),
            'compatibility_validation': self._check_compatibility_matrix(),
            'orchestration_support': self._check_orchestration_patterns(),
            'error_recovery': self._check_error_handling()
        }
        
        self.results['workflow_assembly'] = assembly_tests
        return assembly_tests
    
    def _check_assembly_templates(self) -> bool:
        """Verify assembly templates exist"""
        template_locations = [
            '.claude/components/assembly-templates',
            '.claude/templates/assembly',
            '.claude/commands/core/assemble-command.md'
        ]
        
        templates_found = 0
        for location in template_locations:
            path = self.base_path / location
            if path.exists():
                if path.is_file():
                    templates_found += 1
                else:
                    templates_found += len(list(path.glob('*.md')))
                    
        success = templates_found >= 3
        print(f"  {'✅' if success else '❌'} Assembly Templates: {templates_found} templates available")
        return success
    
    def _check_compatibility_matrix(self) -> bool:
        """Check for component compatibility validation"""
        matrix_patterns = [
            r'compatibility.*matrix',
            r'<compatibility_validation>',
            r'component.*compatibility'
        ]
        
        matrix_references = 0
        for md_file in self.base_path.rglob('*.md'):
            content = md_file.read_text()
            for pattern in matrix_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    matrix_references += 1
                    break
                    
        success = matrix_references >= 5
        print(f"  {'✅' if success else '❌'} Compatibility Validation: {matrix_references} compatibility matrix references")
        return success
    
    def _check_orchestration_patterns(self) -> bool:
        """Verify orchestration patterns are documented"""
        orchestration_patterns = [
            r'/[a-z-]+\s+-->',
            r'can_invoke_commands',
            r'orchestration.*capability',
            r'command.*chain'
        ]
        
        orchestration_docs = 0
        for md_file in self.base_path.rglob('*.md'):
            content = md_file.read_text()
            for pattern in orchestration_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    orchestration_docs += 1
                    break
                    
        success = orchestration_docs >= 20
        print(f"  {'✅' if success else '❌'} Orchestration Support: {orchestration_docs} files with orchestration patterns")
        return success
    
    def _check_error_handling(self) -> bool:
        """Check for error recovery mechanisms"""
        error_patterns = [
            r'error.*handling',
            r'fallback.*mechanism',
            r'recovery.*strategy',
            r'<error_recovery>'
        ]
        
        error_docs = 0
        for md_file in self.base_path.rglob('*.md'):
            content = md_file.read_text()
            for pattern in error_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    error_docs += 1
                    break
                    
        success = error_docs >= 10
        print(f"  {'✅' if success else '❌'} Error Recovery: {error_docs} files with error handling guidance")
        return success
    
    def validate_context_understanding(self) -> Dict[str, bool]:
        """Test AI's understanding of project context"""
        print("\n🧠 Testing Context Engineering Effectiveness...")
        
        context_tests = {
            'anti_patterns': self._check_antipattern_documentation(),
            'project_principles': self._check_principle_understanding(),
            'evolution_tracking': self._check_project_evolution(),
            'best_practices': self._check_best_practices()
        }
        
        self.results['context_understanding'] = context_tests
        return context_tests
    
    def _check_antipattern_documentation(self) -> bool:
        """Verify anti-patterns are well documented"""
        antipattern_file = self.base_path / '.claude/context/llm-antipatterns.md'
        
        if antipattern_file.exists():
            content = antipattern_file.read_text()
            # Count documented patterns
            pattern_count = len(re.findall(r'##\s+\d+\.', content))
            success = pattern_count >= 40  # Should have 48 as documented
        else:
            success = False
            pattern_count = 0
            
        print(f"  {'✅' if success else '❌'} Anti-pattern Documentation: {pattern_count} patterns documented")
        return success
    
    def _check_principle_understanding(self) -> bool:
        """Check if core principles are embedded"""
        principle_patterns = [
            r'modular.*construction',
            r'many.*components.*few.*commands',
            r'progressive.*disclosure',
            r'ai.*consumption'
        ]
        
        principle_docs = 0
        for md_file in self.base_path.rglob('*.md'):
            content = md_file.read_text()
            for pattern in principle_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    principle_docs += 1
                    break
                    
        success = principle_docs >= 20
        print(f"  {'✅' if success else '❌'} Project Principles: {principle_docs} files reference core principles")
        return success
    
    def _check_project_evolution(self) -> bool:
        """Verify project evolution is tracked"""
        evolution_patterns = [
            r'v1\.0.*v2\.0',
            r'evolution.*tracking',
            r'<project_evolution>',
            r'phase.*\d+.*complete'
        ]
        
        evolution_refs = 0
        for md_file in self.base_path.rglob('*.md'):
            content = md_file.read_text()
            for pattern in evolution_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    evolution_refs += 1
                    break
                    
        success = evolution_refs >= 10
        print(f"  {'✅' if success else '❌'} Evolution Tracking: {evolution_refs} files track project evolution")
        return success
    
    def _check_best_practices(self) -> bool:
        """Check for best practices documentation"""
        practices_file = self.base_path / '.claude/context/prompt-engineering-best-practices.md'
        
        if practices_file.exists():
            content = practices_file.read_text()
            # Look for structured best practices
            practices = len(re.findall(r'###.*Best Practice', content, re.IGNORECASE))
            success = practices >= 5
        else:
            success = False
            practices = 0
            
        print(f"  {'✅' if success else '❌'} Best Practices: {practices} documented best practices")
        return success
    
    def generate_report(self) -> str:
        """Generate comprehensive validation report"""
        report = [
            "\n" + "="*60,
            "🤖 AI CONSUMPTION OPTIMIZATION VALIDATION REPORT",
            "="*60,
            "\n📊 VALIDATION SUMMARY:"
        ]
        
        total_tests = 0
        passed_tests = 0
        
        for category, tests in self.results.items():
            if category == 'errors':
                continue
                
            category_passed = sum(1 for result in tests.values() if result)
            category_total = len(tests)
            total_tests += category_total
            passed_tests += category_passed
            
            category_name = category.replace('_', ' ').title()
            report.append(f"\n{category_name}: {category_passed}/{category_total} tests passed")
            
            for test_name, result in tests.items():
                test_display = test_name.replace('_', ' ').title()
                status = "✅" if result else "❌"
                report.append(f"  {status} {test_display}")
        
        # Overall score
        score = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        grade = self._calculate_grade(score)
        
        report.extend([
            f"\n📈 Overall AI Consumption Score: {score:.1f}%",
            f"🎓 Grade: {grade}",
            "\n" + "="*60
        ])
        
        # Add recommendations
        report.extend(self._generate_recommendations())
        
        return '\n'.join(report)
    
    def _calculate_grade(self, score: float) -> str:
        """Calculate letter grade from score"""
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "F"
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on results"""
        recommendations = ["\n💡 RECOMMENDATIONS:"]
        
        # Check each category for issues
        nav_score = sum(self.results['xml_navigation'].values()) / len(self.results['xml_navigation'])
        if nav_score < 0.8:
            recommendations.append("  1. Enhance XML metadata coverage in critical files")
            recommendations.append("  2. Define more component relationships for better AI navigation")
            
        discovery_score = sum(self.results['component_discovery'].values()) / len(self.results['component_discovery'])
        if discovery_score < 0.8:
            recommendations.append("  3. Add more usage examples to components")
            recommendations.append("  4. Improve component tagging for better discoverability")
            
        assembly_score = sum(self.results['workflow_assembly'].values()) / len(self.results['workflow_assembly'])
        if assembly_score < 0.8:
            recommendations.append("  5. Create more assembly templates for common workflows")
            recommendations.append("  6. Document orchestration patterns more clearly")
            
        context_score = sum(self.results['context_understanding'].values()) / len(self.results['context_understanding'])
        if context_score < 0.8:
            recommendations.append("  7. Enhance anti-pattern documentation")
            recommendations.append("  8. Better embed project principles throughout documentation")
            
        return recommendations


def main():
    """Run AI consumption validation tests"""
    print("🤖 AI Consumption Optimization Validation Suite")
    print("Testing the effectiveness of XML tagging and modular architecture")
    print("="*60)
    
    validator = AIConsumptionValidator()
    
    # Run all validations
    validator.validate_xml_navigation()
    validator.validate_component_discovery()
    validator.validate_workflow_assembly()
    validator.validate_context_understanding()
    
    # Generate and print report
    report = validator.generate_report()
    print(report)
    
    # Save report
    report_path = Path('reports/testing/ai-consumption-validation-report.md')
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    print(f"\n📄 Report saved to: {report_path}")


if __name__ == "__main__":
    main()