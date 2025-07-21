#!/usr/bin/env python3
"""
AGENT-9 Quality Assurance - Final Validation & Production Readiness
Comprehensive quality audit with constitutional compliance and safety validation
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

class QualityAssuranceAuditor:
    def __init__(self):
        self.base_path = Path("claude_prompt_factory")
        self.commands_path = self.base_path / "commands"
        self.components_path = self.base_path / "components"
        
        # Quality metrics
        self.quality_metrics = {
            'template_compliance': 0,
            'component_integrity': 0,
            'constitutional_compliance': 0,
            'safety_validation': 0,
            'performance_score': 0,
            'documentation_coverage': 0
        }
        
        self.issues = []
        self.production_readiness_factors = []
        
    def audit_template_compliance(self):
        """Audit template compliance across all commands and components"""
        print("📋 Auditing Template Compliance...")
        
        total_files = 0
        compliant_files = 0
        
        # Check command files for YAML frontmatter and structure
        for cmd_file in self.commands_path.rglob("*.md"):
            if cmd_file.name == "README.md":
                continue
                
            total_files += 1
            try:
                with open(cmd_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                has_yaml = content.startswith('---')
                has_xml_structure = ('<command_file>' in content or 
                                   '<claude_prompt>' in content)
                has_component_includes = 'include component=' in content
                
                if has_yaml and (has_xml_structure or has_component_includes):
                    compliant_files += 1
                else:
                    self.issues.append(f"Template non-compliance: {cmd_file}")
                    
            except Exception as e:
                self.issues.append(f"Error reading {cmd_file}: {e}")
        
        # Check component files for XML structure
        for comp_file in self.components_path.rglob("*.md"):
            if comp_file.name == "README.md":
                continue
                
            total_files += 1
            try:
                with open(comp_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                has_prompt_component = content.startswith('<prompt_component>')
                has_step_structure = '<step name=' in content
                
                if has_prompt_component or has_step_structure:
                    compliant_files += 1
                else:
                    self.issues.append(f"Component structure issue: {comp_file}")
                    
            except Exception as e:
                self.issues.append(f"Error reading {comp_file}: {e}")
        
        compliance_rate = (compliant_files / total_files * 100) if total_files > 0 else 0
        self.quality_metrics['template_compliance'] = compliance_rate
        
        print(f"   └── Files audited: {total_files}")
        print(f"   └── Compliant files: {compliant_files}")
        print(f"   └── Compliance rate: {compliance_rate:.1f}%")
        
        return compliance_rate >= 80  # 80% threshold for production
    
    def audit_component_integrity(self):
        """Audit component reference integrity and resolution"""
        print("\n🔗 Auditing Component Integrity...")
        
        include_pattern = re.compile(r'<include\s+component="([^"]+)"\s*/>')
        total_includes = 0
        valid_includes = 0
        
        for cmd_file in self.commands_path.rglob("*.md"):
            try:
                with open(cmd_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                matches = include_pattern.findall(content)
                for component_path in matches:
                    total_includes += 1
                    full_path = self.base_path / component_path
                    
                    if full_path.exists():
                        valid_includes += 1
                    else:
                        self.issues.append(f"Missing component: {component_path} (in {cmd_file})")
                        
            except Exception as e:
                self.issues.append(f"Error auditing {cmd_file}: {e}")
        
        integrity_rate = (valid_includes / total_includes * 100) if total_includes > 0 else 100
        self.quality_metrics['component_integrity'] = integrity_rate
        
        print(f"   └── Component includes: {total_includes}")
        print(f"   └── Valid includes: {valid_includes}")
        print(f"   └── Integrity rate: {integrity_rate:.1f}%")
        
        return integrity_rate >= 95  # 95% threshold for production
    
    def audit_constitutional_compliance(self):
        """Audit constitutional AI compliance and safety frameworks"""
        print("\n⚖️  Auditing Constitutional AI Compliance...")
        
        constitutional_components = [
            'components/constitutional/constitutional-framework.md',
            'components/constitutional/safety-framework.md',
            'components/constitutional/wisdom-alignment.md'
        ]
        
        constitutional_score = 0
        for comp_path in constitutional_components:
            full_path = self.base_path / comp_path
            if full_path.exists():
                constitutional_score += 1
                print(f"   ✅ {comp_path}")
            else:
                self.issues.append(f"Missing constitutional component: {comp_path}")
                print(f"   ❌ {comp_path}")
        
        # Check for constitutional integration in commands
        commands_with_constitutional = 0
        total_critical_commands = 0
        
        critical_patterns = ['protocol', 'security', 'deploy', 'production']
        
        for cmd_file in self.commands_path.rglob("*.md"):
            if any(pattern in str(cmd_file).lower() for pattern in critical_patterns):
                total_critical_commands += 1
                try:
                    with open(cmd_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    if 'constitutional' in content.lower() or 'safety' in content.lower():
                        commands_with_constitutional += 1
                        
                except Exception:
                    pass
        
        compliance_rate = (constitutional_score / len(constitutional_components) * 100)
        self.quality_metrics['constitutional_compliance'] = compliance_rate
        
        print(f"   └── Constitutional components: {constitutional_score}/{len(constitutional_components)}")
        print(f"   └── Critical commands with safety: {commands_with_constitutional}/{total_critical_commands}")
        print(f"   └── Constitutional compliance: {compliance_rate:.1f}%")
        
        return compliance_rate >= 90  # 90% threshold for production
    
    def audit_safety_validation(self):
        """Audit safety patterns and validation mechanisms"""
        print("\n🛡️  Auditing Safety Validation...")
        
        safety_patterns = [
            'request-user-confirmation',
            'error-handling',
            'circuit-breaker',
            'anti-pattern-detection'
        ]
        
        safety_coverage = 0
        commands_with_safety = 0
        total_commands = 0
        
        for cmd_file in self.commands_path.rglob("*.md"):
            if cmd_file.name == "README.md":
                continue
                
            total_commands += 1
            try:
                with open(cmd_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                safety_found = any(pattern in content for pattern in safety_patterns)
                if safety_found:
                    commands_with_safety += 1
                    
            except Exception:
                pass
        
        safety_coverage = (commands_with_safety / total_commands * 100) if total_commands > 0 else 0
        self.quality_metrics['safety_validation'] = safety_coverage
        
        print(f"   └── Commands with safety patterns: {commands_with_safety}/{total_commands}")
        print(f"   └── Safety coverage: {safety_coverage:.1f}%")
        
        return safety_coverage >= 60  # 60% threshold for production
    
    def audit_performance_benchmarks(self):
        """Audit performance benchmarks and optimization compliance"""
        print("\n⚡ Auditing Performance Benchmarks...")
        
        # Load performance report if exists
        perf_report_file = Path("performance_optimization_report.json")
        if perf_report_file.exists():
            try:
                with open(perf_report_file) as f:
                    perf_data = json.load(f)
                    
                # Evaluate performance metrics
                component_usage_efficiency = perf_data['framework_analysis']['unique_components_used'] / perf_data['framework_analysis']['total_components'] * 100
                
                memory_efficiency = 100 - (perf_data['memory_optimization']['potential_memory_savings'] / 100)
                
                performance_score = (component_usage_efficiency + memory_efficiency) / 2
                self.quality_metrics['performance_score'] = performance_score
                
                print(f"   └── Component usage efficiency: {component_usage_efficiency:.1f}%")
                print(f"   └── Memory efficiency: {memory_efficiency:.1f}%")
                print(f"   └── Overall performance score: {performance_score:.1f}%")
                
                return performance_score >= 70  # 70% threshold for production
                
            except Exception as e:
                self.issues.append(f"Error reading performance report: {e}")
        
        self.issues.append("Performance optimization report not found")
        self.quality_metrics['performance_score'] = 50  # Default poor score
        print("   ❌ Performance optimization report not found")
        return False
    
    def audit_documentation_coverage(self):
        """Audit documentation coverage and quality"""
        print("\n📚 Auditing Documentation Coverage...")
        
        total_directories = 0
        documented_directories = 0
        
        # Check for README files in command directories
        for dir_path in self.commands_path.iterdir():
            if dir_path.is_dir() and dir_path.name != '__pycache__':
                total_directories += 1
                readme_path = dir_path / "README.md"
                if readme_path.exists():
                    documented_directories += 1
                else:
                    self.issues.append(f"Missing README: {dir_path}")
        
        # Check main documentation files
        main_docs = [
            'claude_prompt_factory/CLAUDE.md',
            'README.md',
            'docs/GETTING_STARTED.md'
        ]
        
        main_docs_count = 0
        for doc_path in main_docs:
            if Path(doc_path).exists():
                main_docs_count += 1
            else:
                self.issues.append(f"Missing main documentation: {doc_path}")
        
        coverage_rate = (documented_directories / total_directories * 100) if total_directories > 0 else 0
        main_docs_rate = (main_docs_count / len(main_docs) * 100)
        
        overall_coverage = (coverage_rate + main_docs_rate) / 2
        self.quality_metrics['documentation_coverage'] = overall_coverage
        
        print(f"   └── Documented directories: {documented_directories}/{total_directories}")
        print(f"   └── Main documentation: {main_docs_count}/{len(main_docs)}")
        print(f"   └── Documentation coverage: {overall_coverage:.1f}%")
        
        return overall_coverage >= 80  # 80% threshold for production
    
    def evaluate_production_readiness(self):
        """Evaluate overall production readiness based on all audits"""
        print("\n🎯 Evaluating Production Readiness...")
        
        readiness_factors = {
            'Template Compliance': self.quality_metrics['template_compliance'] >= 80,
            'Component Integrity': self.quality_metrics['component_integrity'] >= 95,
            'Constitutional Compliance': self.quality_metrics['constitutional_compliance'] >= 90,
            'Safety Validation': self.quality_metrics['safety_validation'] >= 60,
            'Performance Benchmarks': self.quality_metrics['performance_score'] >= 70,
            'Documentation Coverage': self.quality_metrics['documentation_coverage'] >= 80
        }
        
        passed_factors = sum(readiness_factors.values())
        total_factors = len(readiness_factors)
        
        for factor, passed in readiness_factors.items():
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"   {status} {factor}")
            if passed:
                self.production_readiness_factors.append(factor)
        
        readiness_score = (passed_factors / total_factors * 100)
        
        if readiness_score >= 85:
            readiness_status = "🟢 PRODUCTION READY"
        elif readiness_score >= 70:
            readiness_status = "🟡 NEEDS IMPROVEMENT"
        else:
            readiness_status = "🔴 NOT READY"
        
        print(f"\n   {readiness_status}")
        print(f"   Overall readiness: {readiness_score:.1f}% ({passed_factors}/{total_factors} factors)")
        
        return readiness_score, readiness_status
    
    def generate_quality_assurance_report(self):
        """Generate comprehensive quality assurance report"""
        print("\n📋 Generating Quality Assurance Report...")
        
        readiness_score, readiness_status = self.evaluate_production_readiness()
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'quality_metrics': self.quality_metrics,
            'production_readiness': {
                'score': readiness_score,
                'status': readiness_status,
                'passed_factors': self.production_readiness_factors
            },
            'issues_found': len(self.issues),
            'critical_issues': [issue for issue in self.issues if 'Missing' in issue or 'Error' in issue],
            'recommendations': [
                "Address all critical issues before production deployment",
                "Implement continuous monitoring for quality metrics",
                "Regular constitutional compliance audits",
                "Performance monitoring and optimization cycles",
                "Documentation maintenance and updates"
            ],
            'next_steps': [
                "Fix remaining template compliance issues",
                "Resolve component integrity gaps", 
                "Enhance safety pattern coverage",
                "Complete documentation gaps",
                "Establish production monitoring"
            ]
        }
        
        # Save comprehensive report
        with open('quality_assurance_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        # Save issues list
        with open('quality_issues.txt', 'w') as f:
            f.write("Quality Assurance Issues\n")
            f.write("======================\n\n")
            for i, issue in enumerate(self.issues, 1):
                f.write(f"{i}. {issue}\n")
        
        print(f"   └── Quality report saved to quality_assurance_report.json")
        print(f"   └── Issues list saved to quality_issues.txt")
        print(f"   └── Production readiness: {readiness_score:.1f}%")
        
        return report
    
    def run_comprehensive_audit(self):
        """Run comprehensive quality assurance audit"""
        print("🔍 AGENT-9 Quality Assurance - Final Validation")
        print("==============================================")
        
        # Run all audit phases
        template_ok = self.audit_template_compliance()
        integrity_ok = self.audit_component_integrity()
        constitutional_ok = self.audit_constitutional_compliance()
        safety_ok = self.audit_safety_validation()
        performance_ok = self.audit_performance_benchmarks()
        docs_ok = self.audit_documentation_coverage()
        
        # Generate final report
        report = self.generate_quality_assurance_report()
        
        print(f"\n✅ Quality Assurance Audit Complete!")
        print(f"📊 Summary:")
        print(f"   • Issues identified: {len(self.issues)}")
        print(f"   • Production readiness: {report['production_readiness']['score']:.1f}%")
        print(f"   • Status: {report['production_readiness']['status']}")
        
        return report

if __name__ == "__main__":
    auditor = QualityAssuranceAuditor()
    auditor.run_comprehensive_audit() 