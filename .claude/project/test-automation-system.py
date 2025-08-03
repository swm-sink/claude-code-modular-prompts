#!/usr/bin/env python3
"""
Automation System Test & Validation
Tests the smart automation system against actual command templates
Phase 3 - Smart Automation Validation
"""

import os
import sys
import logging
from pathlib import Path
from typing import Dict, List, Any

# Import the SmartPlaceholderReplacer directly by executing the file
import importlib.util
spec = importlib.util.spec_from_file_location("smart_automation_engine", 
                                             os.path.join(os.path.dirname(__file__), "smart-automation-engine.py"))
smart_automation_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(smart_automation_module)
SmartPlaceholderReplacer = smart_automation_module.SmartPlaceholderReplacer

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S')

class AutomationSystemTester:
    """Tests automation system against real command templates"""
    
    def __init__(self, base_dir: str = ".claude"):
        self.base_dir = Path(base_dir)
        self.commands_dir = self.base_dir / "commands"
        self.replacer = SmartPlaceholderReplacer()
        
    def get_test_command_files(self) -> List[Path]:
        """Get command files for testing (excluding examples to test on fresh templates)"""
        if not self.commands_dir.exists():
            return []
        
        # Get all command files except examples (they're already customized)
        all_files = list(self.commands_dir.rglob("*.md"))
        test_files = [f for f in all_files if 'examples' not in str(f)]
        return test_files
    
    def run_automation_test(self) -> Dict[str, Any]:
        """Run comprehensive automation test on command templates"""
        logging.info("🧪 AUTOMATION SYSTEM TEST")
        logging.info("=" * 60)
        
        # Get replacement map
        replacement_map = self.replacer.generate_replacement_map()
        
        # Get test files
        test_files = self.get_test_command_files()
        logging.info(f"Testing automation on {len(test_files)} command templates")
        
        # Process each file
        results = []
        for file_path in test_files:
            result = self.replacer.process_command_file(file_path, replacement_map)
            if result:
                results.append(result)
        
        # Calculate overall automation
        automation_stats = self.replacer.calculate_overall_automation(results)
        
        # Compile test results
        test_results = {
            'replacement_map': replacement_map,
            'test_files_count': len(test_files),
            'processed_files': len(results),
            'file_results': results,
            'automation_stats': automation_stats,
            'test_passed': automation_stats['target_achieved']
        }
        
        return test_results
    
    def analyze_automation_gaps(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze which placeholders are not being automated"""
        import re
        
        missed_placeholders = {}
        low_automation_files = []
        
        for result in results:
            if result['automation_percentage'] < 70:
                low_automation_files.append({
                    'file': result['file_path'],
                    'automation': result['automation_percentage'],
                    'placeholders': result['total_placeholders'],
                    'automated': result['replacements_made']
                })
                
                # Extract missed placeholders
                remaining_placeholders = re.findall(r'\[INSERT_[A-Z_]+\]', result['modified_content'])
                for placeholder in remaining_placeholders:
                    missed_placeholders[placeholder] = missed_placeholders.get(placeholder, 0) + 1
        
        return {
            'missed_placeholders': missed_placeholders,
            'low_automation_files': low_automation_files,
            'improvement_suggestions': self.generate_improvement_suggestions(missed_placeholders)
        }
    
    def generate_improvement_suggestions(self, missed_placeholders: Dict[str, int]) -> List[str]:
        """Generate suggestions for improving automation"""
        suggestions = []
        
        common_missed = sorted(missed_placeholders.items(), key=lambda x: x[1], reverse=True)[:5]
        
        for placeholder, count in common_missed:
            if 'USER' in placeholder or 'EMAIL' in placeholder:
                suggestions.append(f"Add user profile detection for {placeholder} (appears {count} times)")
            elif 'CONFIG' in placeholder or 'SETTINGS' in placeholder:
                suggestions.append(f"Add configuration file parsing for {placeholder} (appears {count} times)")
            elif 'URL' in placeholder or 'ENDPOINT' in placeholder:
                suggestions.append(f"Add service discovery for {placeholder} (appears {count} times)")
            elif 'VERSION' in placeholder:
                suggestions.append(f"Add version detection from package files for {placeholder} (appears {count} times)")
            else:
                suggestions.append(f"Create smart default or detection rule for {placeholder} (appears {count} times)")
        
        return suggestions

def print_test_results(results: Dict[str, Any]):
    """Print comprehensive test results"""
    automation_stats = results['automation_stats']
    
    print(f"\n🎯 AUTOMATION TEST RESULTS")
    print(f"=" * 50)
    print(f"Files Tested: {results['test_files_count']}")
    print(f"Files Processed: {results['processed_files']}")
    print(f"Total Placeholders: {automation_stats['total_placeholders']}")
    print(f"Automated Replacements: {automation_stats['total_replacements']}")
    print(f"Automation Percentage: {automation_stats['automation_percentage']:.1f}%")
    print(f"Target (70%): {'✅ ACHIEVED' if automation_stats['target_achieved'] else '❌ NOT MET'}")
    
    print(f"\n📊 FILE BREAKDOWN")
    print(f"=" * 50)
    print(f"Fully Automated Files: {automation_stats['fully_automated_files']}")
    print(f"Partially Automated Files: {automation_stats['partially_automated_files']}")
    print(f"Non-Automated Files: {automation_stats['non_automated_files']}")
    
    # Show automation percentage distribution
    file_results = results['file_results']
    high_automation = sum(1 for r in file_results if r['automation_percentage'] >= 70)
    medium_automation = sum(1 for r in file_results if 30 <= r['automation_percentage'] < 70)
    low_automation = sum(1 for r in file_results if r['automation_percentage'] < 30)
    
    print(f"\n📈 AUTOMATION DISTRIBUTION")
    print(f"=" * 50)
    print(f"High Automation (70%+): {high_automation} files")
    print(f"Medium Automation (30-70%): {medium_automation} files")
    print(f"Low Automation (<30%): {low_automation} files")
    
    # Show top automated replacements
    replacement_map = results['replacement_map']
    print(f"\n⚡ AUTOMATED REPLACEMENTS ({len(replacement_map)})")
    print(f"=" * 50)
    for placeholder, replacement in list(replacement_map.items())[:10]:
        print(f"  {placeholder} → {replacement}")
    if len(replacement_map) > 10:
        print(f"  ... and {len(replacement_map) - 10} more")

def main():
    """Main test execution"""
    tester = AutomationSystemTester()
    
    # Run automation test
    test_results = tester.run_automation_test()
    
    # Print results
    print_test_results(test_results)
    
    # Analyze gaps if target not met
    if not test_results['test_passed']:
        print(f"\n🔍 AUTOMATION GAP ANALYSIS")
        print(f"=" * 50)
        
        gap_analysis = tester.analyze_automation_gaps(test_results['file_results'])
        
        print(f"Most Common Missed Placeholders:")
        for placeholder, count in list(gap_analysis['missed_placeholders'].items())[:5]:
            print(f"  {placeholder}: {count} occurrences")
        
        print(f"\nImprovement Suggestions:")
        for suggestion in gap_analysis['improvement_suggestions'][:3]:
            print(f"  • {suggestion}")
    
    print(f"\n🚀 AUTOMATION SYSTEM STATUS")
    print(f"=" * 50)
    if test_results['test_passed']:
        print("✅ Phase 3 target ACHIEVED - 70%+ automation ready")
        print("🎯 System ready for production use")
    else:
        current_pct = test_results['automation_stats']['automation_percentage']
        print(f"⚠️  Phase 3 target NOT MET - {current_pct:.1f}% vs 70% target")
        print("🔧 Additional optimization needed")
    
    return test_results

if __name__ == "__main__":
    main()