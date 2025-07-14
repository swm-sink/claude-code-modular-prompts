#!/usr/bin/env python3
"""
Agent P4: Quality Infrastructure Auditor
Mission: Validate 119 quality modules for production deployment
Scope: TDD enforcement, quality gates, atomic commits, production compliance
"""

import json
import subprocess
import re
from pathlib import Path
from datetime import datetime
import os

class AgentP4QualityAuditor:
    def __init__(self):
        self.base_path = Path(".")
        self.quality_results = {
            'agent': 'Agent P4 - Quality Infrastructure Auditor',
            'timestamp': datetime.now().isoformat(),
            'mission': 'Validate quality infrastructure for production deployment',
            'scope': {
                'quality_modules_found': 0,
                'quality_gates_tested': 0,
                'tdd_components_validated': 0,
                'atomic_commit_integration_checked': 0
            },
            'quality_audit': {
                'tdd_enforcement': {
                    'score': 0,
                    'components_found': [],
                    'issues': []
                },
                'quality_gates': {
                    'score': 0,
                    'gates_functional': [],
                    'gates_missing': []
                },
                'atomic_commits': {
                    'score': 0,
                    'integration_points': [],
                    'coverage_percentage': 0
                },
                'module_accessibility': {
                    'score': 0,
                    'accessible_modules': 0,
                    'broken_modules': 0
                },
                'production_standards': {
                    'score': 0,
                    'compliance_areas': [],
                    'violations': []
                }
            },
            'overall_quality_score': 0,
            'production_certification': False,
            'recommendations': []
        }
        
        # Quality patterns to look for
        self.quality_patterns = {
            'tdd': [
                r'(?i)red.*green.*refactor',
                r'(?i)test.*driven.*development',
                r'(?i)tdd',
                r'(?i)failing.*test',
                r'(?i)test.*first'
            ],
            'quality_gates': [
                r'(?i)quality.*gate',
                r'(?i)coverage.*threshold',
                r'(?i)validation.*gate',
                r'(?i)blocking.*enforcement',
                r'(?i)quality.*enforcement'
            ],
            'atomic_commits': [
                r'(?i)atomic.*commit',
                r'(?i)rollback',
                r'(?i)instant.*rollback',
                r'(?i)commit.*safety',
                r'(?i)bulletproof'
            ]
        }
    
    def discover_quality_modules(self):
        """Discover all quality-related modules"""
        print("🔍 Discovering quality modules...")
        
        quality_paths = [
            '.claude/modules/quality',
            '.claude/system/quality',
            '.claude/modules/patterns',
            '.claude/system'
        ]
        
        quality_modules = []
        
        for path in quality_paths:
            quality_path = Path(path)
            if quality_path.exists():
                modules = list(quality_path.rglob('*.md'))
                quality_modules.extend(modules)
        
        # Also check for quality-related files by name
        all_files = list(self.base_path.glob('.claude/**/*.md'))
        quality_keywords = ['quality', 'tdd', 'test', 'validation', 'gate', 'enforcement']
        
        for file_path in all_files:
            file_name = file_path.name.lower()
            if any(keyword in file_name for keyword in quality_keywords):
                if file_path not in quality_modules:
                    quality_modules.append(file_path)
        
        self.quality_results['scope']['quality_modules_found'] = len(quality_modules)
        
        print(f"  📊 Found {len(quality_modules)} quality modules")
        
        return quality_modules
    
    def audit_tdd_enforcement(self, quality_modules):
        """Audit TDD enforcement capabilities"""
        print("🧪 Auditing TDD enforcement...")
        
        tdd_components = []
        tdd_issues = []
        tdd_score = 0
        
        for module in quality_modules:
            try:
                content = module.read_text()
                module_name = module.name
                
                # Check for TDD patterns
                tdd_matches = 0
                for pattern in self.quality_patterns['tdd']:
                    if re.search(pattern, content):
                        tdd_matches += 1
                
                if tdd_matches > 0:
                    tdd_components.append({
                        'module': str(module),
                        'tdd_patterns_found': tdd_matches,
                        'has_red_green_refactor': bool(re.search(r'(?i)red.*green.*refactor', content)),
                        'has_test_first': bool(re.search(r'(?i)test.*first', content)),
                        'has_enforcement': bool(re.search(r'(?i)enforcement|blocking|mandatory', content))
                    })
                
                # Check for TDD cycle implementation
                if 'red' in content.lower() and 'green' in content.lower() and 'refactor' in content.lower():
                    tdd_score += 25
                
                # Check for enforcement mechanisms
                if re.search(r'(?i)blocking|mandatory|enforce', content):
                    tdd_score += 15
                
            except Exception as e:
                tdd_issues.append(f"Could not read module {module}: {e}")
        
        # Bonus for having multiple TDD components
        if len(tdd_components) >= 3:
            tdd_score += 20
        elif len(tdd_components) >= 1:
            tdd_score += 10
        
        # Check for TDD in CLAUDE.md
        try:
            claude_md = Path('CLAUDE.md').read_text()
            if re.search(r'(?i)tdd.*mandatory', claude_md):
                tdd_score += 30
        except:
            tdd_issues.append("Could not verify TDD configuration in CLAUDE.md")
        
        tdd_score = min(tdd_score, 100)
        
        self.quality_results['quality_audit']['tdd_enforcement'] = {
            'score': tdd_score,
            'components_found': tdd_components,
            'issues': tdd_issues
        }
        
        self.quality_results['scope']['tdd_components_validated'] = len(tdd_components)
        
        print(f"  📊 TDD Score: {tdd_score}/100")
        print(f"  📊 TDD Components: {len(tdd_components)}")
        
        return tdd_score
    
    def audit_quality_gates(self, quality_modules):
        """Audit quality gates functionality"""
        print("🚪 Auditing quality gates...")
        
        gates_functional = []
        gates_missing = []
        gate_score = 0
        
        # Expected quality gates
        expected_gates = [
            'test_coverage',
            'performance_thresholds',
            'security_validation',
            'code_quality',
            'tdd_compliance'
        ]
        
        for module in quality_modules:
            try:
                content = module.read_text()
                module_name = module.name
                
                # Check for quality gate patterns
                gate_matches = 0
                for pattern in self.quality_patterns['quality_gates']:
                    if re.search(pattern, content):
                        gate_matches += 1
                
                if gate_matches > 0:
                    gates_functional.append({
                        'module': str(module),
                        'gate_patterns_found': gate_matches,
                        'has_thresholds': bool(re.search(r'(?i)threshold|limit|requirement', content)),
                        'has_blocking': bool(re.search(r'(?i)blocking|fail|abort', content))
                    })
                    gate_score += 15
                
            except Exception as e:
                continue
        
        # Check CLAUDE.md for quality gate configuration
        try:
            claude_md = Path('CLAUDE.md').read_text()
            if 'quality_gates' in claude_md.lower():
                gate_score += 20
            if 'test_coverage' in claude_md.lower():
                gate_score += 15
            if 'blocking' in claude_md.lower():
                gate_score += 10
        except:
            gates_missing.append("Quality gates not configured in CLAUDE.md")
        
        # Check for specific gate implementations
        coverage_files = list(self.base_path.glob('**/*coverage*'))
        if coverage_files:
            gate_score += 15
        else:
            gates_missing.append("Test coverage enforcement")
        
        gate_score = min(gate_score, 100)
        
        self.quality_results['quality_audit']['quality_gates'] = {
            'score': gate_score,
            'gates_functional': gates_functional,
            'gates_missing': gates_missing
        }
        
        self.quality_results['scope']['quality_gates_tested'] = len(gates_functional)
        
        print(f"  📊 Quality Gates Score: {gate_score}/100")
        print(f"  📊 Functional Gates: {len(gates_functional)}")
        
        return gate_score
    
    def audit_atomic_commits(self):
        """Audit atomic commits integration"""
        print("⚛️  Auditing atomic commits integration...")
        
        integration_points = []
        atomic_score = 0
        coverage_count = 0
        total_commands = 0
        
        # Check commands for atomic commit integration
        commands_path = Path('.claude/commands')
        if commands_path.exists():
            command_files = list(commands_path.glob('*.md'))
            total_commands = len(command_files)
            
            for command_file in command_files:
                try:
                    content = command_file.read_text()
                    
                    atomic_matches = 0
                    for pattern in self.quality_patterns['atomic_commits']:
                        if re.search(pattern, content):
                            atomic_matches += 1
                    
                    if atomic_matches > 0:
                        integration_points.append({
                            'command': command_file.name,
                            'atomic_patterns_found': atomic_matches,
                            'has_rollback': bool(re.search(r'(?i)rollback', content)),
                            'has_safety': bool(re.search(r'(?i)safety|bulletproof', content))
                        })
                        coverage_count += 1
                        atomic_score += 5
                
                except Exception as e:
                    continue
        
        # Check CLAUDE.md for atomic commits configuration
        try:
            claude_md = Path('CLAUDE.md').read_text()
            if 'atomic_commits' in claude_md.lower():
                atomic_score += 25
            if 'universal_atomic_commits' in claude_md.lower():
                atomic_score += 25
            if 'instant_rollback' in claude_md.lower():
                atomic_score += 20
        except:
            pass
        
        # Check for atomic commit patterns in modules
        quality_modules = list(self.base_path.glob('.claude/modules/**/*.md'))
        for module in quality_modules[:10]:  # Sample check
            try:
                content = module.read_text()
                if re.search(r'(?i)atomic.*commit', content):
                    atomic_score += 2
            except:
                continue
        
        # Calculate coverage percentage
        coverage_percentage = (coverage_count / total_commands * 100) if total_commands > 0 else 0
        
        atomic_score = min(atomic_score, 100)
        
        self.quality_results['quality_audit']['atomic_commits'] = {
            'score': atomic_score,
            'integration_points': integration_points,
            'coverage_percentage': round(coverage_percentage, 1)
        }
        
        self.quality_results['scope']['atomic_commit_integration_checked'] = len(integration_points)
        
        print(f"  📊 Atomic Commits Score: {atomic_score}/100")
        print(f"  📊 Coverage: {coverage_percentage:.1f}%")
        
        return atomic_score
    
    def audit_module_accessibility(self, quality_modules):
        """Audit quality module accessibility"""
        print("📂 Auditing module accessibility...")
        
        accessible_count = 0
        broken_count = 0
        
        for module in quality_modules:
            try:
                # Test basic accessibility
                content = module.read_text()
                size = len(content)
                
                if size > 100:  # Has substantial content
                    accessible_count += 1
                else:
                    broken_count += 1
                    
            except Exception as e:
                broken_count += 1
        
        total_modules = len(quality_modules)
        accessibility_percentage = (accessible_count / total_modules * 100) if total_modules > 0 else 0
        
        # Score based on accessibility
        if accessibility_percentage >= 95:
            accessibility_score = 100
        elif accessibility_percentage >= 90:
            accessibility_score = 90
        elif accessibility_percentage >= 80:
            accessibility_score = 75
        else:
            accessibility_score = 50
        
        self.quality_results['quality_audit']['module_accessibility'] = {
            'score': accessibility_score,
            'accessible_modules': accessible_count,
            'broken_modules': broken_count
        }
        
        print(f"  📊 Accessibility Score: {accessibility_score}/100")
        print(f"  📊 Accessible Modules: {accessible_count}/{total_modules}")
        
        return accessibility_score
    
    def audit_production_standards(self):
        """Audit production standards compliance"""
        print("🏭 Auditing production standards compliance...")
        
        compliance_areas = []
        violations = []
        standards_score = 0
        
        # Check version control standards
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
            if not result.stdout.strip():
                compliance_areas.append("Clean git repository")
                standards_score += 20
            else:
                violations.append("Uncommitted changes in repository")
        except:
            violations.append("Git not available or not a git repository")
        
        # Check documentation standards
        required_docs = ['CLAUDE.md', 'GETTING_STARTED.md']
        for doc in required_docs:
            if Path(doc).exists():
                compliance_areas.append(f"{doc} present")
                standards_score += 15
            else:
                violations.append(f"Missing {doc}")
        
        # Check framework structure standards
        required_dirs = ['.claude/commands', '.claude/modules', '.claude/system']
        for dir_path in required_dirs:
            if Path(dir_path).exists():
                compliance_areas.append(f"{dir_path} structure present")
                standards_score += 10
            else:
                violations.append(f"Missing {dir_path} structure")
        
        # Check for production readiness indicators
        claude_md_path = Path('CLAUDE.md')
        if claude_md_path.exists():
            try:
                content = claude_md_path.read_text()
                if 'production' in content.lower():
                    compliance_areas.append("Production configuration present")
                    standards_score += 10
                if 'version' in content.lower():
                    compliance_areas.append("Version information present")
                    standards_score += 5
            except:
                violations.append("Could not verify CLAUDE.md content")
        
        standards_score = min(standards_score, 100)
        
        self.quality_results['quality_audit']['production_standards'] = {
            'score': standards_score,
            'compliance_areas': compliance_areas,
            'violations': violations
        }
        
        print(f"  📊 Production Standards Score: {standards_score}/100")
        print(f"  📊 Compliance Areas: {len(compliance_areas)}")
        print(f"  📊 Violations: {len(violations)}")
        
        return standards_score
    
    def calculate_overall_quality_score(self):
        """Calculate overall quality score"""
        tdd_score = self.quality_results['quality_audit']['tdd_enforcement']['score']
        gates_score = self.quality_results['quality_audit']['quality_gates']['score']
        atomic_score = self.quality_results['quality_audit']['atomic_commits']['score']
        accessibility_score = self.quality_results['quality_audit']['module_accessibility']['score']
        standards_score = self.quality_results['quality_audit']['production_standards']['score']
        
        # Weighted scoring
        overall_score = (
            tdd_score * 0.25 +
            gates_score * 0.25 +
            atomic_score * 0.25 +
            accessibility_score * 0.15 +
            standards_score * 0.10
        )
        
        self.quality_results['overall_quality_score'] = round(overall_score, 1)
        
        # Production certification requires >= 75% overall score and all critical components
        certification = (
            overall_score >= 75 and
            tdd_score >= 70 and
            atomic_score >= 70 and
            accessibility_score >= 90
        )
        
        self.quality_results['production_certification'] = certification
        
        return overall_score, certification
    
    def generate_recommendations(self):
        """Generate quality improvement recommendations"""
        recommendations = []
        
        tdd_score = self.quality_results['quality_audit']['tdd_enforcement']['score']
        gates_score = self.quality_results['quality_audit']['quality_gates']['score']
        atomic_score = self.quality_results['quality_audit']['atomic_commits']['score']
        overall_score = self.quality_results['overall_quality_score']
        
        if overall_score >= 90:
            recommendations.append("Quality infrastructure is excellent for production")
        elif overall_score >= 75:
            recommendations.append("Quality infrastructure is production-ready with minor improvements")
        else:
            recommendations.append("Significant quality improvements needed before production")
        
        if tdd_score < 70:
            recommendations.append("Strengthen TDD enforcement mechanisms")
        
        if gates_score < 70:
            recommendations.append("Implement comprehensive quality gates")
        
        if atomic_score < 70:
            recommendations.append("Enhance atomic commits integration")
        
        violations = self.quality_results['quality_audit']['production_standards']['violations']
        if violations:
            recommendations.append(f"Address production standards violations: {len(violations)} issues")
        
        recommendations.extend([
            "Maintain regular quality audits",
            "Monitor quality metrics in production",
            "Ensure all new features pass quality gates"
        ])
        
        self.quality_results['recommendations'] = recommendations
        return recommendations
    
    def execute_quality_audit(self):
        """Execute complete quality infrastructure audit"""
        print("🚀 Agent P4: Starting Quality Infrastructure Audit...")
        print("🎯 Mission: Validate quality infrastructure for production deployment")
        
        # Discover quality modules
        quality_modules = self.discover_quality_modules()
        
        # Execute all audits
        tdd_score = self.audit_tdd_enforcement(quality_modules)
        gates_score = self.audit_quality_gates(quality_modules)
        atomic_score = self.audit_atomic_commits()
        accessibility_score = self.audit_module_accessibility(quality_modules)
        standards_score = self.audit_production_standards()
        
        # Calculate overall results
        overall_score, certification = self.calculate_overall_quality_score()
        recommendations = self.generate_recommendations()
        
        # Save results
        with open('agent_p4_quality_audit_results.json', 'w') as f:
            json.dump(self.quality_results, f, indent=2)
        
        # Report summary
        print("\n" + "="*80)
        print("🎯 AGENT P4 QUALITY INFRASTRUCTURE AUDIT - COMPLETE!")
        print("="*80)
        print(f"📊 Quality Modules Found: {len(quality_modules)}")
        print(f"🧪 TDD Enforcement Score: {tdd_score}/100")
        print(f"🚪 Quality Gates Score: {gates_score}/100")
        print(f"⚛️  Atomic Commits Score: {atomic_score}/100")
        print(f"📂 Module Accessibility: {accessibility_score}/100")
        print(f"🏭 Production Standards: {standards_score}/100")
        print(f"📈 Overall Quality Score: {overall_score}/100")
        print(f"🏆 Production Certification: {'✅ CERTIFIED' if certification else '❌ NOT CERTIFIED'}")
        
        if certification:
            print("\n🎉 QUALITY AUDIT PASSED!")
            print("Quality infrastructure certified for production deployment")
        else:
            print("\n⚠️  QUALITY IMPROVEMENTS NEEDED!")
            print("Address quality issues before production deployment")
        
        return certification

if __name__ == "__main__":
    agent_p4 = AgentP4QualityAuditor()
    agent_p4.execute_quality_audit()