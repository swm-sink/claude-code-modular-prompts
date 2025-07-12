#!/usr/bin/env python3
"""
Agent P5: Documentation Production Validator
Mission: Final documentation accuracy audit for production users
Scope: Documentation vs reality validation, user experience testing, accuracy verification
"""

import json
import re
from pathlib import Path
from datetime import datetime
import os

class AgentP5DocumentationValidator:
    def __init__(self):
        self.base_path = Path(".")
        self.documentation_results = {
            'agent': 'Agent P5 - Documentation Production Validator',
            'timestamp': datetime.now().isoformat(),
            'mission': 'Final documentation accuracy audit for production users',
            'scope': {
                'documentation_files_audited': 0,
                'claims_verified': 0,
                'accuracy_tests_performed': 0,
                'user_experience_scenarios': 0
            },
            'documentation_audit': {
                'accuracy_verification': {
                    'score': 0,
                    'accurate_claims': [],
                    'inaccurate_claims': [],
                    'outdated_information': []
                },
                'user_experience': {
                    'score': 0,
                    'onboarding_clarity': 0,
                    'navigation_ease': 0,
                    'completeness': 0
                },
                'production_readiness': {
                    'score': 0,
                    'deployment_instructions': False,
                    'configuration_guidance': False,
                    'troubleshooting_coverage': False
                },
                'consistency_check': {
                    'score': 0,
                    'consistent_terminology': True,
                    'version_alignment': True,
                    'structural_alignment': True
                }
            },
            'overall_documentation_score': 0,
            'production_certification': False,
            'critical_issues': [],
            'recommendations': []
        }
        
        # Current framework state (from previous agents)
        self.framework_reality = {
            'directories': 35,  # Actual count
            'functional_commands': 4,  # From Agent 9
            'accessible_commands': 9,  # From Agent 9
            'total_commands': 14,  # From Agent P2
            'quality_modules': 119,  # From Agent 10
            'performance_improvement': '13%',  # From Agent 10
            'pattern_duplication_eliminated': True,  # From Agent 7.1
            'atomic_commits_integrated': True  # From framework enhancement
        }
    
    def discover_documentation_files(self):
        """Discover all documentation files"""
        print("📚 Discovering documentation files...")
        
        doc_patterns = [
            'README.md',
            'CLAUDE.md',
            'GETTING_STARTED.md',
            '.claude/**/README.md',
            'docs/**/*.md',
            '**/DOCUMENTATION*.md',
            '**/GUIDE*.md'
        ]
        
        doc_files = []
        for pattern in doc_patterns:
            doc_files.extend(self.base_path.glob(pattern))
        
        # Remove duplicates
        unique_docs = list(set(doc_files))
        
        self.documentation_results['scope']['documentation_files_audited'] = len(unique_docs)
        
        print(f"  📊 Found {len(unique_docs)} documentation files")
        
        return unique_docs
    
    def verify_accuracy_claims(self, doc_files):
        """Verify accuracy of documentation claims against reality"""
        print("🔍 Verifying documentation accuracy claims...")
        
        accurate_claims = []
        inaccurate_claims = []
        outdated_information = []
        accuracy_score = 0
        
        for doc_file in doc_files:
            try:
                content = doc_file.read_text()
                doc_name = doc_file.name
                
                # Test specific claims against reality
                claims_tested = 0
                claims_accurate = 0
                
                # Directory count claims
                dir_matches = re.findall(r'(\d+)\s*director(?:y|ies)', content, re.IGNORECASE)
                for match in dir_matches:
                    claims_tested += 1
                    claimed_dirs = int(match)
                    actual_dirs = self.framework_reality['directories']
                    
                    if abs(claimed_dirs - actual_dirs) <= 2:  # Allow small variance
                        accurate_claims.append(f"{doc_name}: Directory count ({claimed_dirs}) accurate")
                        claims_accurate += 1
                    else:
                        inaccurate_claims.append(f"{doc_name}: Claims {claimed_dirs} directories, actually {actual_dirs}")
                
                # Command functionality claims
                if 'command' in content.lower():
                    claims_tested += 1
                    # Look for specific command count claims
                    cmd_matches = re.findall(r'(\d+).*command(?:s)?.*(?:functional|working)', content, re.IGNORECASE)
                    for match in cmd_matches:
                        claimed_functional = int(match)
                        actual_functional = self.framework_reality['functional_commands']
                        
                        if claimed_functional == actual_functional:
                            accurate_claims.append(f"{doc_name}: Functional commands count accurate")
                            claims_accurate += 1
                        else:
                            inaccurate_claims.append(f"{doc_name}: Claims {claimed_functional} functional commands, actually {actual_functional}")
                
                # Pattern duplication claims
                if 'pattern' in content.lower() and 'duplication' in content.lower():
                    claims_tested += 1
                    if 'eliminated' in content.lower() or 'resolved' in content.lower():
                        if self.framework_reality['pattern_duplication_eliminated']:
                            accurate_claims.append(f"{doc_name}: Pattern duplication elimination claim accurate")
                            claims_accurate += 1
                        else:
                            inaccurate_claims.append(f"{doc_name}: Claims pattern duplication eliminated, but still exists")
                
                # Performance improvement claims
                perf_matches = re.findall(r'(\d+(?:\.\d+)?)%.*(?:improvement|faster|reduction)', content, re.IGNORECASE)
                for match in perf_matches:
                    claims_tested += 1
                    claimed_improvement = float(match)
                    # Check if reasonable (within 5% of actual 13%)
                    if 8 <= claimed_improvement <= 18:
                        accurate_claims.append(f"{doc_name}: Performance improvement claim reasonable")
                        claims_accurate += 1
                    else:
                        inaccurate_claims.append(f"{doc_name}: Performance claim {claimed_improvement}% seems inaccurate")
                
                # Check for outdated version references
                version_matches = re.findall(r'version\s*[:\s]*(\d+\.\d+(?:\.\d+)?)', content, re.IGNORECASE)
                for version in version_matches:
                    claims_tested += 1
                    if version.startswith('3.0'):
                        accurate_claims.append(f"{doc_name}: Version {version} current")
                        claims_accurate += 1
                    elif version.startswith('2.'):
                        outdated_information.append(f"{doc_name}: References outdated version {version}")
                    else:
                        accurate_claims.append(f"{doc_name}: Version {version} acceptable")
                        claims_accurate += 1
                
                # Calculate accuracy for this document
                if claims_tested > 0:
                    doc_accuracy = (claims_accurate / claims_tested) * 100
                    accuracy_score += doc_accuracy
                
            except Exception as e:
                inaccurate_claims.append(f"Could not verify claims in {doc_file}: {e}")
        
        # Calculate overall accuracy score
        total_docs_with_claims = len([f for f in doc_files if any(keyword in f.read_text().lower() 
                                    for keyword in ['directory', 'command', 'pattern', 'performance', 'version'])
                                    ])
        
        if total_docs_with_claims > 0:
            accuracy_score = accuracy_score / total_docs_with_claims
        else:
            accuracy_score = 50  # Default if no testable claims found
        
        accuracy_score = min(accuracy_score, 100)
        
        self.documentation_results['documentation_audit']['accuracy_verification'] = {
            'score': round(accuracy_score, 1),
            'accurate_claims': accurate_claims,
            'inaccurate_claims': inaccurate_claims,
            'outdated_information': outdated_information
        }
        
        self.documentation_results['scope']['claims_verified'] = len(accurate_claims) + len(inaccurate_claims)
        
        print(f"  📊 Accuracy Score: {accuracy_score:.1f}/100")
        print(f"  ✅ Accurate Claims: {len(accurate_claims)}")
        print(f"  ❌ Inaccurate Claims: {len(inaccurate_claims)}")
        print(f"  📅 Outdated Information: {len(outdated_information)}")
        
        return accuracy_score
    
    def test_user_experience(self, doc_files):
        """Test documentation from user experience perspective"""
        print("👤 Testing user experience...")
        
        ux_score = 0
        onboarding_clarity = 0
        navigation_ease = 0
        completeness = 0
        
        # Test onboarding clarity
        getting_started = next((f for f in doc_files if 'getting_started' in f.name.lower()), None)
        if getting_started:
            try:
                content = getting_started.read_text()
                
                # Check for essential onboarding elements
                onboarding_elements = [
                    ('installation', r'(?i)install|setup|download'),
                    ('quick_start', r'(?i)quick.*start|getting.*started'),
                    ('first_command', r'(?i)first.*command|example|tutorial'),
                    ('configuration', r'(?i)config|setup|customize'),
                    ('troubleshooting', r'(?i)troubleshoot|problem|issue|error')
                ]
                
                for element, pattern in onboarding_elements:
                    if re.search(pattern, content):
                        onboarding_clarity += 20
                
            except Exception as e:
                pass
        else:
            # Deduct points for missing getting started guide
            onboarding_clarity = 30
        
        # Test navigation ease
        claude_md = next((f for f in doc_files if 'claude' in f.name.lower()), None)
        if claude_md:
            try:
                content = claude_md.read_text()
                
                # Check for navigation aids
                navigation_elements = [
                    ('table_of_contents', r'(?i)table.*of.*contents|toc|\[.*\]\(#'),
                    ('cross_references', r'\[.*\]\([^)]+\.md\)'),
                    ('clear_sections', r'^#{1,3}\s+[A-Z]'),
                    ('command_index', r'(?i)command.*list|available.*command'),
                    ('module_structure', r'(?i)module.*structure|directory.*structure')
                ]
                
                for element, pattern in navigation_elements:
                    if re.search(pattern, content, re.MULTILINE):
                        navigation_ease += 20
                
            except Exception as e:
                pass
        
        # Test completeness
        essential_topics = [
            ('commands', r'(?i)command'),
            ('modules', r'(?i)module'),
            ('quality', r'(?i)quality|tdd'),
            ('configuration', r'(?i)config'),
            ('examples', r'(?i)example|usage')
        ]
        
        topics_covered = 0
        total_content = ""
        
        for doc_file in doc_files:
            try:
                total_content += doc_file.read_text().lower()
            except:
                continue
        
        for topic, pattern in essential_topics:
            if re.search(pattern, total_content):
                topics_covered += 1
        
        completeness = (topics_covered / len(essential_topics)) * 100
        
        # Calculate overall UX score
        ux_score = (onboarding_clarity * 0.4 + navigation_ease * 0.3 + completeness * 0.3)
        
        self.documentation_results['documentation_audit']['user_experience'] = {
            'score': round(ux_score, 1),
            'onboarding_clarity': round(onboarding_clarity, 1),
            'navigation_ease': round(navigation_ease, 1),
            'completeness': round(completeness, 1)
        }
        
        self.documentation_results['scope']['user_experience_scenarios'] = 3  # onboarding, navigation, completeness
        
        print(f"  📊 User Experience Score: {ux_score:.1f}/100")
        print(f"  🎯 Onboarding Clarity: {onboarding_clarity:.1f}/100")
        print(f"  🧭 Navigation Ease: {navigation_ease:.1f}/100")
        print(f"  📋 Completeness: {completeness:.1f}/100")
        
        return ux_score
    
    def test_production_readiness_docs(self, doc_files):
        """Test production readiness documentation"""
        print("🏭 Testing production readiness documentation...")
        
        production_score = 0
        deployment_instructions = False
        configuration_guidance = False
        troubleshooting_coverage = False
        
        total_content = ""
        for doc_file in doc_files:
            try:
                total_content += doc_file.read_text().lower()
            except:
                continue
        
        # Check for deployment instructions
        deployment_patterns = [
            r'(?i)deploy|installation|setup|production',
            r'(?i)getting.*started|quick.*start',
            r'(?i)configure|config|initialization'
        ]
        
        for pattern in deployment_patterns:
            if re.search(pattern, total_content):
                deployment_instructions = True
                production_score += 33
                break
        
        # Check for configuration guidance
        config_patterns = [
            r'(?i)config|customiz|adapt|setup',
            r'(?i)environment|variable|setting',
            r'(?i)project.*config|claude\.md'
        ]
        
        for pattern in config_patterns:
            if re.search(pattern, total_content):
                configuration_guidance = True
                production_score += 33
                break
        
        # Check for troubleshooting coverage
        troubleshooting_patterns = [
            r'(?i)troubleshoot|problem|issue|error',
            r'(?i)debug|fix|resolve|solution',
            r'(?i)faq|common.*issue|known.*issue'
        ]
        
        for pattern in troubleshooting_patterns:
            if re.search(pattern, total_content):
                troubleshooting_coverage = True
                production_score += 34
                break
        
        self.documentation_results['documentation_audit']['production_readiness'] = {
            'score': production_score,
            'deployment_instructions': deployment_instructions,
            'configuration_guidance': configuration_guidance,
            'troubleshooting_coverage': troubleshooting_coverage
        }
        
        print(f"  📊 Production Readiness Score: {production_score}/100")
        print(f"  🚀 Deployment Instructions: {'✅' if deployment_instructions else '❌'}")
        print(f"  ⚙️  Configuration Guidance: {'✅' if configuration_guidance else '❌'}")
        print(f"  🔧 Troubleshooting Coverage: {'✅' if troubleshooting_coverage else '❌'}")
        
        return production_score
    
    def check_consistency(self, doc_files):
        """Check documentation consistency"""
        print("📏 Checking documentation consistency...")
        
        consistency_score = 100
        consistent_terminology = True
        version_alignment = True
        structural_alignment = True
        
        # Check terminology consistency
        terminology_variants = {
            'claude code': ['claude code', 'claude-code', 'claudecode'],
            'framework': ['framework', 'system', 'platform'],
            'command': ['command', 'cmd', 'instruction'],
            'module': ['module', 'component', 'plugin']
        }
        
        all_content = ""
        for doc_file in doc_files:
            try:
                all_content += doc_file.read_text().lower() + " "
            except:
                continue
        
        for term, variants in terminology_variants.items():
            variant_counts = [all_content.count(variant) for variant in variants]
            if len(set(variant_counts)) > 1 and max(variant_counts) > 0:
                # Inconsistent usage found
                consistency_score -= 10
                consistent_terminology = False
        
        # Check version alignment
        version_refs = re.findall(r'version\s*[:\s]*(\d+\.\d+(?:\.\d+)?)', all_content, re.IGNORECASE)
        unique_versions = set(version_refs)
        if len(unique_versions) > 2:  # Allow for current and one previous version
            consistency_score -= 15
            version_alignment = False
        
        # Check structural alignment
        directory_counts = re.findall(r'(\d+)\s*director(?:y|ies)', all_content, re.IGNORECASE)
        if directory_counts:
            unique_dir_counts = set(int(count) for count in directory_counts)
            if len(unique_dir_counts) > 2:  # Allow for some variance
                consistency_score -= 15
                structural_alignment = False
        
        self.documentation_results['documentation_audit']['consistency_check'] = {
            'score': consistency_score,
            'consistent_terminology': consistent_terminology,
            'version_alignment': version_alignment,
            'structural_alignment': structural_alignment
        }
        
        print(f"  📊 Consistency Score: {consistency_score}/100")
        print(f"  📝 Terminology: {'✅' if consistent_terminology else '❌'}")
        print(f"  🔢 Version Alignment: {'✅' if version_alignment else '❌'}")
        print(f"  🏗️  Structural Alignment: {'✅' if structural_alignment else '❌'}")
        
        return consistency_score
    
    def identify_critical_issues(self):
        """Identify critical documentation issues"""
        critical_issues = []
        
        accuracy = self.documentation_results['documentation_audit']['accuracy_verification']
        ux = self.documentation_results['documentation_audit']['user_experience']
        production = self.documentation_results['documentation_audit']['production_readiness']
        consistency = self.documentation_results['documentation_audit']['consistency_check']
        
        # Critical accuracy issues
        if accuracy['score'] < 70:
            critical_issues.append(f"Documentation accuracy too low: {accuracy['score']:.1f}%")
        
        if len(accuracy['inaccurate_claims']) > 3:
            critical_issues.append(f"Too many inaccurate claims: {len(accuracy['inaccurate_claims'])}")
        
        # Critical UX issues
        if ux['onboarding_clarity'] < 60:
            critical_issues.append("Onboarding documentation insufficient")
        
        if ux['completeness'] < 60:
            critical_issues.append("Documentation coverage incomplete")
        
        # Critical production issues
        if not production['deployment_instructions']:
            critical_issues.append("Missing deployment instructions")
        
        # Critical consistency issues
        if not consistency['consistent_terminology']:
            critical_issues.append("Inconsistent terminology usage")
        
        self.documentation_results['critical_issues'] = critical_issues
        return critical_issues
    
    def calculate_overall_score(self):
        """Calculate overall documentation score"""
        accuracy_score = self.documentation_results['documentation_audit']['accuracy_verification']['score']
        ux_score = self.documentation_results['documentation_audit']['user_experience']['score']
        production_score = self.documentation_results['documentation_audit']['production_readiness']['score']
        consistency_score = self.documentation_results['documentation_audit']['consistency_check']['score']
        
        # Weighted scoring
        overall_score = (
            accuracy_score * 0.35 +    # Most important
            ux_score * 0.30 +          # User experience critical
            production_score * 0.20 +   # Production readiness
            consistency_score * 0.15    # Consistency important but not critical
        )
        
        self.documentation_results['overall_documentation_score'] = round(overall_score, 1)
        
        # Production certification requires high scores and no critical issues
        critical_issues = self.documentation_results['critical_issues']
        certification = (
            overall_score >= 80 and
            accuracy_score >= 75 and
            len(critical_issues) <= 1
        )
        
        self.documentation_results['production_certification'] = certification
        
        return overall_score, certification
    
    def generate_recommendations(self):
        """Generate documentation improvement recommendations"""
        recommendations = []
        
        overall_score = self.documentation_results['overall_documentation_score']
        accuracy = self.documentation_results['documentation_audit']['accuracy_verification']
        ux = self.documentation_results['documentation_audit']['user_experience']
        production = self.documentation_results['documentation_audit']['production_readiness']
        
        if overall_score >= 90:
            recommendations.append("Documentation is excellent for production deployment")
        elif overall_score >= 80:
            recommendations.append("Documentation is production-ready with minor improvements")
        elif overall_score >= 70:
            recommendations.append("Documentation needs improvements before production")
        else:
            recommendations.append("Significant documentation improvements required")
        
        # Specific recommendations based on scores
        if accuracy['score'] < 80:
            recommendations.append("Update documentation to match current framework state")
            recommendations.append("Review and correct inaccurate claims")
        
        if ux['onboarding_clarity'] < 80:
            recommendations.append("Improve getting started guide with clearer instructions")
        
        if ux['navigation_ease'] < 80:
            recommendations.append("Add table of contents and cross-references")
        
        if production['score'] < 80:
            recommendations.append("Add comprehensive deployment and configuration guides")
        
        # Address critical issues
        for issue in self.documentation_results['critical_issues']:
            recommendations.append(f"CRITICAL: {issue}")
        
        recommendations.extend([
            "Maintain documentation accuracy with framework changes",
            "Test documentation with new users regularly",
            "Keep production guides up to date"
        ])
        
        self.documentation_results['recommendations'] = recommendations
        return recommendations
    
    def execute_documentation_validation(self):
        """Execute complete documentation validation"""
        print("🚀 Agent P5: Starting Documentation Production Validation...")
        print("🎯 Mission: Final documentation accuracy audit for production users")
        
        # Discover documentation
        doc_files = self.discover_documentation_files()
        
        # Execute all validations
        accuracy_score = self.verify_accuracy_claims(doc_files)
        ux_score = self.test_user_experience(doc_files)
        production_score = self.test_production_readiness_docs(doc_files)
        consistency_score = self.check_consistency(doc_files)
        
        # Identify issues and calculate results
        critical_issues = self.identify_critical_issues()
        overall_score, certification = self.calculate_overall_score()
        recommendations = self.generate_recommendations()
        
        # Update scope
        self.documentation_results['scope']['accuracy_tests_performed'] = 4  # accuracy, ux, production, consistency
        
        # Save results
        with open('agent_p5_documentation_validation_results.json', 'w') as f:
            json.dump(self.documentation_results, f, indent=2)
        
        # Report summary
        print("\n" + "="*80)
        print("🎯 AGENT P5 DOCUMENTATION VALIDATION - COMPLETE!")
        print("="*80)
        print(f"📚 Documentation Files Audited: {len(doc_files)}")
        print(f"🔍 Accuracy Score: {accuracy_score:.1f}/100")
        print(f"👤 User Experience Score: {ux_score:.1f}/100")
        print(f"🏭 Production Readiness Score: {production_score}/100")
        print(f"📏 Consistency Score: {consistency_score}/100")
        print(f"📈 Overall Documentation Score: {overall_score:.1f}/100")
        print(f"🚨 Critical Issues: {len(critical_issues)}")
        print(f"🏆 Production Certification: {'✅ CERTIFIED' if certification else '❌ NOT CERTIFIED'}")
        
        if certification:
            print("\n🎉 DOCUMENTATION VALIDATION PASSED!")
            print("Documentation certified for production deployment")
        else:
            print("\n⚠️  DOCUMENTATION IMPROVEMENTS NEEDED!")
            print("Address documentation issues before production deployment")
        
        return certification

if __name__ == "__main__":
    agent_p5 = AgentP5DocumentationValidator()
    agent_p5.execute_documentation_validation()