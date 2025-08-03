#!/usr/bin/env python3
"""
Placeholder Analysis System
Analyzes all placeholders across command templates to understand automation requirements
Phase 3, Step 1 - Smart Automation Planning
"""

import os
import re
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict, Counter

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%H:%M:%S')

class PlaceholderAnalyzer:
    def __init__(self, base_dir: str = ".claude"):
        self.base_dir = Path(base_dir)
        self.commands_dir = self.base_dir / "commands"
        
    def extract_placeholders(self, content: str) -> Set[str]:
        """Extract all [INSERT_XXX] placeholders from content"""
        # Match [INSERT_XXX] pattern
        pattern = r'\[INSERT_([A-Z_]+)\]'
        matches = re.findall(pattern, content)
        return set(f"[INSERT_{match}]" for match in matches)
    
    def analyze_command_file(self, file_path: Path) -> Dict[str, any]:
        """Analyze a single command file for placeholders"""
        try:
            content = file_path.read_text()
            placeholders = self.extract_placeholders(content)
            
            # Count occurrences
            placeholder_counts = {}
            for placeholder in placeholders:
                placeholder_counts[placeholder] = content.count(placeholder)
            
            return {
                'file_path': str(file_path),
                'relative_path': str(file_path.relative_to(self.base_dir)),
                'placeholders': placeholders,
                'placeholder_counts': placeholder_counts,
                'total_placeholders': sum(placeholder_counts.values()),
                'unique_placeholders': len(placeholders)
            }
        except Exception as e:
            logging.error(f"Error analyzing {file_path}: {e}")
            return None
    
    def get_all_command_files(self) -> List[Path]:
        """Get all markdown files in commands directory"""
        if not self.commands_dir.exists():
            return []
        
        return list(self.commands_dir.rglob("*.md"))
    
    def analyze_all_commands(self) -> Dict[str, any]:
        """Analyze all command files for placeholder usage"""
        command_files = self.get_all_command_files()
        
        results = {
            'total_files': len(command_files),
            'files_with_placeholders': 0,
            'files_without_placeholders': 0,
            'file_analyses': [],
            'global_placeholder_stats': defaultdict(int),
            'placeholder_frequency': Counter(),
            'automation_opportunities': {}
        }
        
        for file_path in command_files:
            analysis = self.analyze_command_file(file_path)
            if analysis:
                results['file_analyses'].append(analysis)
                
                if analysis['total_placeholders'] > 0:
                    results['files_with_placeholders'] += 1
                    
                    # Update global stats
                    for placeholder, count in analysis['placeholder_counts'].items():
                        results['global_placeholder_stats'][placeholder] += count
                        results['placeholder_frequency'][placeholder] += 1
                else:
                    results['files_without_placeholders'] += 1
        
        return results
    
    def categorize_placeholders(self, placeholder_stats: Dict[str, int]) -> Dict[str, List[str]]:
        """Categorize placeholders by automation difficulty"""
        categories = {
            'project_metadata': [],      # Easy - can be detected from project
            'technology_stack': [],      # Medium - can be detected from files
            'user_preferences': [],      # Hard - requires user input
            'domain_specific': [],       # Medium - can be inferred from context
            'configuration': []          # Medium - can be detected from config files
        }
        
        # Classification patterns
        project_patterns = ['PROJECT_NAME', 'COMPANY_NAME', 'ORGANIZATION']
        tech_patterns = ['TECH_STACK', 'FRAMEWORK', 'LANGUAGE', 'PLATFORM']
        user_patterns = ['USER_NAME', 'EMAIL', 'TEAM_SIZE', 'PREFERENCES']
        domain_patterns = ['DOMAIN', 'INDUSTRY', 'USE_CASE', 'WORKFLOW_TYPE']
        config_patterns = ['CONFIG', 'SETTINGS', 'ENVIRONMENT', 'PORT', 'URL']
        
        for placeholder in placeholder_stats:
            placeholder_upper = placeholder.upper()
            
            if any(pattern in placeholder_upper for pattern in project_patterns):
                categories['project_metadata'].append(placeholder)
            elif any(pattern in placeholder_upper for pattern in tech_patterns):
                categories['technology_stack'].append(placeholder)
            elif any(pattern in placeholder_upper for pattern in user_patterns):
                categories['user_preferences'].append(placeholder)
            elif any(pattern in placeholder_upper for pattern in domain_patterns):
                categories['domain_specific'].append(placeholder)
            elif any(pattern in placeholder_upper for pattern in config_patterns):
                categories['configuration'].append(placeholder)
            else:
                # Default to domain_specific for uncategorized
                categories['domain_specific'].append(placeholder)
        
        return categories
    
    def calculate_automation_potential(self, categories: Dict[str, List[str]], 
                                     placeholder_stats: Dict[str, int]) -> Dict[str, any]:
        """Calculate automation potential and target percentages"""
        
        # Automation difficulty weights
        automation_weights = {
            'project_metadata': 0.9,    # 90% automatable
            'technology_stack': 0.8,    # 80% automatable  
            'configuration': 0.7,       # 70% automatable
            'domain_specific': 0.5,     # 50% automatable
            'user_preferences': 0.2     # 20% automatable
        }
        
        total_occurrences = sum(placeholder_stats.values())
        automatable_occurrences = 0
        
        category_analysis = {}
        
        for category, placeholders in categories.items():
            if not placeholders:
                continue
                
            category_occurrences = sum(placeholder_stats.get(p, 0) for p in placeholders)
            automation_weight = automation_weights.get(category, 0.3)
            automatable_in_category = category_occurrences * automation_weight
            
            category_analysis[category] = {
                'placeholder_count': len(placeholders),
                'total_occurrences': category_occurrences,
                'automation_weight': automation_weight,
                'automatable_occurrences': automatable_in_category,
                'automation_percentage': automation_weight * 100,
                'placeholders': placeholders
            }
            
            automatable_occurrences += automatable_in_category
        
        overall_automation_potential = (automatable_occurrences / total_occurrences) * 100 if total_occurrences > 0 else 0
        
        return {
            'total_placeholder_occurrences': total_occurrences,
            'automatable_occurrences': automatable_occurrences,
            'overall_automation_potential': overall_automation_potential,
            'target_achievement': overall_automation_potential >= 70,
            'category_analysis': category_analysis
        }
    
    def generate_automation_roadmap(self, categories: Dict[str, List[str]], 
                                  automation_analysis: Dict[str, any]) -> List[Dict[str, str]]:
        """Generate roadmap for implementing automation"""
        roadmap = []
        
        # Priority order based on automation potential and impact
        priority_order = [
            ('project_metadata', 'High Impact - Easy Implementation'),
            ('technology_stack', 'High Impact - Medium Implementation'),
            ('configuration', 'Medium Impact - Medium Implementation'),
            ('domain_specific', 'Medium Impact - Hard Implementation'),
            ('user_preferences', 'Low Impact - Manual Required')
        ]
        
        for category, description in priority_order:
            if category in categories and categories[category]:
                analysis = automation_analysis['category_analysis'].get(category, {})
                roadmap.append({
                    'category': category,
                    'description': description,
                    'placeholder_count': analysis.get('placeholder_count', 0),
                    'automation_potential': f"{analysis.get('automation_percentage', 0):.1f}%",
                    'implementation_strategy': self.get_implementation_strategy(category),
                    'placeholders': categories[category]
                })
        
        return roadmap
    
    def get_implementation_strategy(self, category: str) -> str:
        """Get implementation strategy for each category"""
        strategies = {
            'project_metadata': 'Scan package.json, setup.py, Cargo.toml, git config for project name, organization',
            'technology_stack': 'Analyze file extensions, dependencies, frameworks from package files',
            'configuration': 'Parse config files (.env, config.json, settings files) for common values',
            'domain_specific': 'Use directory structure, file patterns, and content analysis for context',
            'user_preferences': 'Interactive prompts with smart defaults and caching'
        }
        return strategies.get(category, 'Custom analysis required')
    
    def run_analysis(self) -> Dict[str, any]:
        """Run complete placeholder analysis"""
        logging.info("🔍 PLACEHOLDER ANALYSIS SYSTEM")
        logging.info("=" * 60)
        
        # Analyze all commands
        results = self.analyze_all_commands()
        
        # Categorize placeholders
        categories = self.categorize_placeholders(results['global_placeholder_stats'])
        
        # Calculate automation potential
        automation_analysis = self.calculate_automation_potential(categories, results['global_placeholder_stats'])
        
        # Generate automation roadmap
        roadmap = self.generate_automation_roadmap(categories, automation_analysis)
        
        # Compile final results
        final_results = {
            'file_analysis': results,
            'placeholder_categories': categories,
            'automation_analysis': automation_analysis,
            'automation_roadmap': roadmap,
            'phase_3_feasibility': automation_analysis['target_achievement']
        }
        
        return final_results

def print_analysis_results(results: Dict[str, any]):
    """Print comprehensive analysis results"""
    file_analysis = results['file_analysis']
    automation_analysis = results['automation_analysis']
    roadmap = results['automation_roadmap']
    
    print(f"\n📊 PLACEHOLDER ANALYSIS RESULTS")
    print(f"=" * 50)
    print(f"Total Command Files: {file_analysis['total_files']}")
    print(f"Files with Placeholders: {file_analysis['files_with_placeholders']}")
    print(f"Files without Placeholders: {file_analysis['files_without_placeholders']}")
    print(f"Unique Placeholders Found: {len(file_analysis['global_placeholder_stats'])}")
    print(f"Total Placeholder Occurrences: {automation_analysis['total_placeholder_occurrences']}")
    
    print(f"\n🎯 AUTOMATION POTENTIAL ANALYSIS")
    print(f"=" * 50)
    print(f"Overall Automation Potential: {automation_analysis['overall_automation_potential']:.1f}%")
    print(f"Phase 3 Target (70%): {'✅ ACHIEVABLE' if automation_analysis['target_achievement'] else '❌ CHALLENGING'}")
    print(f"Automatable Occurrences: {automation_analysis['automatable_occurrences']:.1f}/{automation_analysis['total_placeholder_occurrences']}")
    
    print(f"\n📋 CATEGORY BREAKDOWN")
    print(f"=" * 50)
    for category, analysis in automation_analysis['category_analysis'].items():
        print(f"{category.replace('_', ' ').title()}:")
        print(f"  - Placeholders: {analysis['placeholder_count']}")
        print(f"  - Occurrences: {analysis['total_occurrences']}")
        print(f"  - Automation Potential: {analysis['automation_percentage']:.1f}%")
        print(f"  - Examples: {', '.join(analysis['placeholders'][:3])}{'...' if len(analysis['placeholders']) > 3 else ''}")
        print()
    
    print(f"📈 AUTOMATION ROADMAP")
    print(f"=" * 50)
    for i, item in enumerate(roadmap, 1):
        print(f"{i}. {item['category'].replace('_', ' ').title()}")
        print(f"   {item['description']}")
        print(f"   Automation Potential: {item['automation_potential']}")
        print(f"   Strategy: {item['implementation_strategy']}")
        print(f"   Placeholders: {len(item['placeholders'])} unique")
        print()
    
    print(f"🚀 PHASE 3 RECOMMENDATION")
    print(f"=" * 50)
    if automation_analysis['target_achievement']:
        print("✅ Phase 3 target (70% automation) is ACHIEVABLE")
        print("🎯 Recommended approach: Implement categories 1-3 first")
        print("⚡ Expected result: 70%+ automation with medium effort")
    else:
        print("⚠️  Phase 3 target (70% automation) is CHALLENGING")
        print("🎯 Recommended approach: Focus on high-impact categories")
        print("⚡ Expected result: May need to adjust target or implementation")

if __name__ == "__main__":
    analyzer = PlaceholderAnalyzer()
    results = analyzer.run_analysis()
    print_analysis_results(results)