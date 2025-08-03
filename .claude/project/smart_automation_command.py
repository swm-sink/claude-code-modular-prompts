#!/usr/bin/env python3
"""
Smart Automation Command Implementation
Practical automation system for command template adaptation
Phase 3 - Production Ready Smart Automation
"""

import os
import sys
import shutil
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional

# Import the automation engine
import importlib.util
spec = importlib.util.spec_from_file_location("smart_automation_engine", 
                                             os.path.join(os.path.dirname(__file__), "smart-automation-engine.py"))
smart_automation_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(smart_automation_module)
SmartPlaceholderReplacer = smart_automation_module.SmartPlaceholderReplacer

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S')

class SmartAutomationCommand:
    """Production-ready smart automation command"""
    
    def __init__(self, target_directory: str = ".", base_commands_dir: str = ".claude/commands"):
        self.target_dir = Path(target_directory).resolve()
        self.base_commands_dir = Path(base_commands_dir)
        self.replacer = SmartPlaceholderReplacer(str(self.target_dir))
        
    def create_adapted_commands_directory(self) -> Path:
        """Create directory for adapted commands"""
        adapted_dir = self.target_dir / ".claude" / "commands"
        adapted_dir.mkdir(parents=True, exist_ok=True)
        return adapted_dir
    
    def select_high_value_commands(self) -> List[Path]:
        """Select commands that provide highest value with automation"""
        if not self.base_commands_dir.exists():
            return []
        
        # Priority command categories for 70%+ automation success
        high_value_patterns = [
            "core/*.md",           # Core development commands
            "development/*.md",    # Development workflow commands  
            "devops/*.md",         # DevOps and deployment commands
            "quality/*.md",        # Quality assurance commands
            "meta/adapt-*.md",     # Adaptation commands
            "meta/project-*.md"    # Project management commands
        ]
        
        selected_commands = []
        for pattern in high_value_patterns:
            selected_commands.extend(self.base_commands_dir.glob(pattern))
        
        # Also include examples that work well with automation
        examples_dir = self.base_commands_dir / "examples"
        if examples_dir.exists():
            selected_commands.extend(examples_dir.glob("component-demo-*.md"))
        
        return selected_commands
    
    def apply_smart_automation(self, command_files: List[Path], mode: str = "quick") -> Dict[str, Any]:
        """Apply smart automation to selected command files"""
        logging.info(f"🚀 Applying smart automation in {mode} mode")
        
        # Generate replacement map
        replacement_map = self.replacer.generate_replacement_map()
        
        results = {
            'total_files': len(command_files),
            'processed_files': 0,
            'total_placeholders': 0,
            'total_replacements': 0,
            'high_automation_files': 0,
            'file_results': []
        }
        
        adapted_dir = self.create_adapted_commands_directory()
        
        for file_path in command_files:
            try:
                # Process the file
                result = self.replacer.process_command_file(file_path, replacement_map)
                if result:
                    results['file_results'].append(result)
                    results['total_placeholders'] += result['total_placeholders']
                    results['total_replacements'] += result['replacements_made']
                    
                    if result['automation_percentage'] >= 70:
                        results['high_automation_files'] += 1
                    
                    # Create adapted file
                    relative_path = file_path.relative_to(self.base_commands_dir)
                    adapted_file_path = adapted_dir / relative_path
                    adapted_file_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Write adapted content
                    adapted_file_path.write_text(result['modified_content'])
                    
                    results['processed_files'] += 1
                    
                    logging.info(f"✅ {file_path.name}: {result['automation_percentage']:.1f}% automated")
                
            except Exception as e:
                logging.error(f"Error processing {file_path}: {e}")
        
        # Calculate overall automation
        overall_automation = (results['total_replacements'] / results['total_placeholders'] * 100) if results['total_placeholders'] > 0 else 0
        results['overall_automation'] = overall_automation
        results['target_achieved'] = overall_automation >= 70
        
        return results
    
    def generate_automation_report(self, results: Dict[str, Any]) -> str:
        """Generate comprehensive automation report"""
        report = []
        report.append("🎯 SMART AUTOMATION RESULTS")
        report.append("=" * 50)
        report.append(f"Target Directory: {self.target_dir}")
        report.append(f"Files Processed: {results['processed_files']}/{results['total_files']}")
        report.append(f"Total Placeholders: {results['total_placeholders']}")
        report.append(f"Automated Replacements: {results['total_replacements']}")
        report.append(f"Overall Automation: {results['overall_automation']:.1f}%")
        report.append(f"Phase 3 Target (70%): {'✅ ACHIEVED' if results['target_achieved'] else '❌ NOT MET'}")
        report.append("")
        
        report.append("📊 HIGH-VALUE AUTOMATION BREAKDOWN")
        report.append("=" * 50)
        report.append(f"Commands with 70%+ Automation: {results['high_automation_files']}")
        
        # Show best performing files
        sorted_results = sorted(results['file_results'], key=lambda x: x['automation_percentage'], reverse=True)
        
        report.append("\n🏆 TOP AUTOMATED COMMANDS")
        report.append("-" * 30)
        for result in sorted_results[:10]:
            file_name = Path(result['file_path']).name
            report.append(f"{file_name}: {result['automation_percentage']:.1f}% ({result['replacements_made']}/{result['total_placeholders']})")
        
        if results['target_achieved']:
            report.append("\n✅ SUCCESS: 70%+ automation achieved!")
            report.append("🎯 Your project is ready for productive Claude Code usage")
            report.append("📁 Adapted commands available in .claude/commands/")
        else:
            report.append("\n⚠️  Target not fully met, but significant automation achieved")
            report.append("🔧 Manual customization needed for remaining placeholders")
            report.append("💡 Consider using /replace-placeholders for remaining items")
        
        return "\n".join(report)
    
    def create_project_summary(self, replacement_map: Dict[str, str]) -> str:
        """Create summary of detected project context"""
        summary = []
        summary.append("🔍 DETECTED PROJECT CONTEXT")
        summary.append("=" * 50)
        
        key_detections = {
            '[INSERT_PROJECT_NAME]': 'Project Name',
            '[INSERT_COMPANY_NAME]': 'Organization',
            '[INSERT_TECH_STACK]': 'Technology Stack', 
            '[INSERT_FRAMEWORK]': 'Primary Framework',
            '[INSERT_TESTING_FRAMEWORK]': 'Testing Framework',
            '[INSERT_CI_CD_PLATFORM]': 'CI/CD Platform',
            '[INSERT_DATABASE_TYPE]': 'Database Type',
            '[INSERT_DEPLOYMENT_TARGET]': 'Deployment Target'
        }
        
        for placeholder, label in key_detections.items():
            if placeholder in replacement_map:
                summary.append(f"{label}: {replacement_map[placeholder]}")
        
        summary.append(f"\nTotal Automatic Replacements: {len(replacement_map)}")
        return "\n".join(summary)

def main(target_directory: str = ".", mode: str = "quick"):
    """Main automation command execution"""
    logging.info("🚀 SMART AUTOMATION COMMAND")
    logging.info("=" * 60)
    
    # Initialize automation system
    automation = SmartAutomationCommand(target_directory)
    
    # Generate replacement map and show context
    replacement_map = automation.replacer.generate_replacement_map()
    print(automation.create_project_summary(replacement_map))
    
    # Select high-value commands for automation
    command_files = automation.select_high_value_commands()
    
    if not command_files:
        print("\n❌ No command templates found. Please run from the correct directory.")
        return False
    
    logging.info(f"Selected {len(command_files)} high-value commands for automation")
    
    # Apply smart automation
    results = automation.apply_smart_automation(command_files, mode)
    
    # Display results
    print(f"\n{automation.generate_automation_report(results)}")
    
    return results['target_achieved']

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Smart Automation Command for Claude Code Templates")
    parser.add_argument("target_directory", nargs="?", default=".", help="Target project directory")
    parser.add_argument("--mode", choices=["quick", "thorough"], default="quick", help="Automation mode")
    
    args = parser.parse_args()
    
    success = main(args.target_directory, args.mode)
    sys.exit(0 if success else 1)