#!/usr/bin/env python3
"""
Project Template Validation Script

Validates all PROJECT_CONFIG.xml templates to ensure they are:
- Well-formed XML
- Complete with all required sections  
- Consistent with framework expectations
- Ready for immediate use

Usage: python validate_templates.py
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Any


class TemplateValidator:
    """Validates PROJECT_CONFIG.xml templates"""
    
    def __init__(self):
        self.templates_dir = Path(__file__).parent
        self.required_sections = {
            'project_metadata': ['name', 'version', 'description'],
            'tech_stack': ['primary_language', 'framework'],
            'project_structure': ['source_directory', 'test_directory'],
            'commands': ['test', 'build', 'install'],
            'quality_standards': ['test_coverage', 'performance'],
            'framework_behavior': ['file_creation_policy', 'test_first_enforcement'],
            'development_workflow': ['git_workflow', 'commit_format']
        }
        
    def find_all_templates(self) -> List[Path]:
        """Find all XML template files"""
        templates = []
        for root, dirs, files in os.walk(self.templates_dir):
            for file in files:
                if file.endswith('.xml') and 'config' in file:
                    templates.append(Path(root) / file)
        return templates
    
    def validate_xml_structure(self, template_path: Path) -> Dict[str, Any]:
        """Validate XML structure and completeness"""
        result = {
            'path': template_path,
            'valid_xml': False,
            'complete_sections': {},
            'missing_sections': [],
            'warnings': [],
            'tech_stack': 'unknown'
        }
        
        try:
            # Parse XML
            tree = ET.parse(template_path)
            root = tree.getroot()
            result['valid_xml'] = True
            
            # Extract basic info
            name_elem = root.find('.//name')
            if name_elem is not None:
                result['project_name'] = name_elem.text
            
            lang_elem = root.find('.//primary_language')
            if lang_elem is not None:
                result['tech_stack'] = lang_elem.text
            
            # Check required sections
            for section, required_fields in self.required_sections.items():
                section_elem = root.find(f'.//{section}')
                if section_elem is not None:
                    found_fields = []
                    missing_fields = []
                    
                    for field in required_fields:
                        field_elem = section_elem.find(f'.//{field}')
                        if field_elem is not None and field_elem.text:
                            found_fields.append(field)
                        else:
                            missing_fields.append(field)
                    
                    result['complete_sections'][section] = {
                        'found': found_fields,
                        'missing': missing_fields,
                        'complete': len(missing_fields) == 0
                    }
                else:
                    result['missing_sections'].append(section)
            
            # Check for specific quality issues
            self._check_quality_issues(root, result)
            
        except ET.ParseError as e:
            result['xml_error'] = str(e)
        except Exception as e:
            result['error'] = str(e)
        
        return result
    
    def _check_quality_issues(self, root: ET.Element, result: Dict[str, Any]):
        """Check for common quality issues"""
        warnings = []
        
        # Check for placeholder values
        placeholder_patterns = ['my-project', 'your-org', 'example.com', 'changeme']
        for elem in root.iter():
            if elem.text:
                for pattern in placeholder_patterns:
                    if pattern in elem.text.lower():
                        warnings.append(f"Placeholder value detected: '{elem.text}' in {elem.tag}")
        
        # Check test coverage thresholds
        coverage_elem = root.find('.//test_coverage/threshold')
        if coverage_elem is not None:
            try:
                threshold = int(coverage_elem.text)
                if threshold < 70:
                    warnings.append(f"Low test coverage threshold: {threshold}%")
                elif threshold > 95:
                    warnings.append(f"Very high test coverage threshold: {threshold}%")
            except ValueError:
                warnings.append(f"Invalid test coverage threshold: {coverage_elem.text}")
        
        # Check for missing descriptions
        desc_elem = root.find('.//description')
        if desc_elem is None or not desc_elem.text or len(desc_elem.text) < 10:
            warnings.append("Missing or too short project description")
        
        result['warnings'] = warnings
    
    def validate_all_templates(self) -> Dict[str, Any]:
        """Validate all templates and return summary"""
        templates = self.find_all_templates()
        results = []
        
        print(f"Found {len(templates)} templates to validate...")
        
        for template in templates:
            print(f"\nValidating: {template.relative_to(self.templates_dir)}")
            result = self.validate_xml_structure(template)
            results.append(result)
            
            # Print immediate feedback
            if result['valid_xml']:
                print(f"  ✅ Valid XML structure")
                print(f"  📋 Tech Stack: {result['tech_stack']}")
                
                complete_count = sum(1 for s in result['complete_sections'].values() if s['complete'])
                total_sections = len(self.required_sections)
                print(f"  📊 Complete Sections: {complete_count}/{total_sections}")
                
                if result['warnings']:
                    print(f"  ⚠️  Warnings: {len(result['warnings'])}")
                    for warning in result['warnings'][:3]:  # Show first 3
                        print(f"    - {warning}")
                    if len(result['warnings']) > 3:
                        print(f"    ... and {len(result['warnings']) - 3} more")
            else:
                print(f"  ❌ XML parsing failed: {result.get('xml_error', 'Unknown error')}")
        
        # Generate summary
        summary = self._generate_summary(results)
        return summary
    
    def _generate_summary(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate validation summary"""
        total = len(results)
        valid_xml = sum(1 for r in results if r['valid_xml'])
        fully_complete = sum(1 for r in results if r['valid_xml'] and 
                           all(s['complete'] for s in r['complete_sections'].values()))
        
        tech_stacks = {}
        total_warnings = 0
        
        for result in results:
            if result['valid_xml']:
                stack = result['tech_stack']
                tech_stacks[stack] = tech_stacks.get(stack, 0) + 1
                total_warnings += len(result['warnings'])
        
        return {
            'total_templates': total,
            'valid_xml_count': valid_xml,
            'fully_complete_count': fully_complete,
            'tech_stacks': tech_stacks,
            'total_warnings': total_warnings,
            'results': results,
            'success_rate': (fully_complete / total * 100) if total > 0 else 0
        }
    
    def print_detailed_report(self, summary: Dict[str, Any]):
        """Print detailed validation report"""
        print("\n" + "="*60)
        print("📋 PROJECT TEMPLATE VALIDATION REPORT")
        print("="*60)
        
        print(f"\n📊 Overall Statistics:")
        print(f"  Total Templates: {summary['total_templates']}")
        print(f"  Valid XML: {summary['valid_xml_count']}")
        print(f"  Fully Complete: {summary['fully_complete_count']}")
        print(f"  Success Rate: {summary['success_rate']:.1f}%")
        print(f"  Total Warnings: {summary['total_warnings']}")
        
        print(f"\n🛠️  Technology Stacks:")
        for stack, count in summary['tech_stacks'].items():
            print(f"  {stack}: {count} template(s)")
        
        print(f"\n📝 Detailed Results:")
        for result in summary['results']:
            template_name = result['path'].name
            status = "✅" if (result['valid_xml'] and 
                           all(s['complete'] for s in result['complete_sections'].values())) else "⚠️"
            
            print(f"\n{status} {template_name}")
            print(f"   Tech Stack: {result['tech_stack']}")
            
            if result['valid_xml']:
                for section, info in result['complete_sections'].items():
                    status_icon = "✅" if info['complete'] else "❌"
                    print(f"   {status_icon} {section}: {len(info['found'])}/{len(info['found']) + len(info['missing'])} fields")
                    if info['missing']:
                        print(f"      Missing: {', '.join(info['missing'])}")
                
                if result['warnings']:
                    print(f"   ⚠️  Warnings ({len(result['warnings'])}):")
                    for warning in result['warnings']:
                        print(f"      - {warning}")
            else:
                print(f"   ❌ XML Error: {result.get('xml_error', 'Unknown')}")
        
        print(f"\n✅ Validation Complete!")
        
        if summary['success_rate'] == 100:
            print("🎉 All templates are complete and ready to use!")
        elif summary['success_rate'] >= 80:
            print("👍 Most templates are in good shape, minor issues to address.")
        else:
            print("⚠️  Several templates need attention before they're ready for users.")


def main():
    """Main validation script"""
    print("🔍 PROJECT TEMPLATE VALIDATOR")
    print("Validating all PROJECT_CONFIG.xml templates...\n")
    
    validator = TemplateValidator()
    summary = validator.validate_all_templates()
    validator.print_detailed_report(summary)
    
    # Exit code based on success rate
    if summary['success_rate'] >= 100:
        return 0
    elif summary['success_rate'] >= 80:
        return 1
    else:
        return 2


if __name__ == "__main__":
    sys.exit(main())