#!/usr/bin/env python3
"""
Documentation Accuracy Verification Test
========================================

Comprehensive verification that all documentation claims match actual
implementation. Tests all documented features, counts, and capabilities
to ensure no false claims or outdated information.

Critical Areas:
- Command count claims vs actual files
- Component count claims vs actual files  
- Feature documentation vs implementation
- Interactive Consultation System claims vs functionality
- Example workflows vs actual command availability

Author: Testing Framework Agent
Date: 2025-07-31
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass
from enum import Enum


class DocTestResult(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARNING = "WARNING"


@dataclass
class DocumentationTest:
    document: str
    test_name: str
    result: DocTestResult
    details: str
    score: float = 0.0


class DocumentationAccuracyTester:
    """Test documentation accuracy against actual implementation"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.commands_dir = self.project_root / ".claude" / "commands"
        self.components_dir = self.project_root / ".claude" / "components"
        self.test_results: List[DocumentationTest] = []
        
        # Key documentation files to test
        self.key_docs = [
            "CLAUDE.md",
            "README.md",
            "USAGE.md",
            "FAQ.md"
        ]
        
        # Interactive Consultation System commands
        self.progressive_disclosure_commands = [
            "quick-command.md",
            "build-command.md",
            "assemble-command.md"
        ]
    
    def run_documentation_accuracy_tests(self) -> Dict:
        """Run comprehensive documentation accuracy verification"""
        print("📚 Documentation Accuracy Verification")
        print("="*40)
        
        # Test 1: Count Claims Verification
        print("\n🔢 Verifying Count Claims")
        self.verify_count_claims()
        
        # Test 2: Feature Claims Verification
        print("\n🎯 Verifying Feature Claims")
        self.verify_feature_claims()
        
        # Test 3: Command Examples Verification
        print("\n💡 Verifying Command Examples")
        self.verify_command_examples()
        
        # Test 4: Interactive Consultation System Claims
        print("\n🎚️  Verifying Interactive Consultation System Claims")
        self.verify_progressive_disclosure_claims()
        
        # Test 5: Workflow Documentation
        print("\n🔄 Verifying Workflow Documentation")
        self.verify_workflow_documentation()
        
        return self.generate_documentation_report()
    
    def verify_count_claims(self):
        """Verify all numerical claims in documentation"""
        
        # Get actual counts
        actual_commands = len(list(self.commands_dir.rglob("*.md"))) if self.commands_dir.exists() else 0
        actual_components = len(list(self.components_dir.rglob("*.md"))) if self.components_dir.exists() else 0
        
        # Test each key documentation file
        for doc_name in self.key_docs:
            doc_path = self.project_root / doc_name
            if not doc_path.exists():
                self.test_results.append(DocumentationTest(
                    doc_name,
                    "Document Exists",
                    DocTestResult.WARNING,
                    f"{doc_name} not found",
                    0.0
                ))
                continue
            
            content = doc_path.read_text(encoding='utf-8')
            
            # Test command count claims
            command_patterns = [
                r'(\d+)\s+command[s]?\s+template[s]?',
                r'(\d+)\s+active\s+command[s]?',
                r'(\d+)\s+Claude\s+Code\s+command[s]?'
            ]
            
            command_claims = []
            for pattern in command_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                command_claims.extend([int(m) for m in matches])
            
            if command_claims:
                # Check if any claim matches actual count (within tolerance)
                accurate_claims = [claim for claim in command_claims 
                                 if abs(claim - actual_commands) <= 2]
                
                if accurate_claims:
                    self.test_results.append(DocumentationTest(
                        doc_name,
                        "Command Count Claims",
                        DocTestResult.PASS,
                        f"Command count claims are accurate: {accurate_claims} (actual: {actual_commands})",
                        100.0
                    ))
                else:
                    self.test_results.append(DocumentationTest(
                        doc_name,
                        "Command Count Claims",
                        DocTestResult.FAIL,
                        f"Command count claims are inaccurate: {command_claims} (actual: {actual_commands})",
                        0.0
                    ))
            
            # Test component count claims
            component_patterns = [
                r'(\d+)\s+component[s]?\s+template[s]?',
                r'(\d+)\s+reusable\s+component[s]?',
                r'(\d+)\s+prompt\s+fragment[s]?'
            ]
            
            component_claims = []
            for pattern in component_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                component_claims.extend([int(m) for m in matches])
            
            if component_claims:
                # Check accuracy
                accurate_claims = [claim for claim in component_claims 
                                 if abs(claim - actual_components) <= 5]
                
                if accurate_claims:
                    self.test_results.append(DocumentationTest(
                        doc_name,
                        "Component Count Claims",
                        DocTestResult.PASS,
                        f"Component count claims are accurate: {accurate_claims} (actual: {actual_components})",
                        100.0
                    ))
                else:
                    self.test_results.append(DocumentationTest(
                        doc_name,
                        "Component Count Claims",
                        DocTestResult.FAIL,
                        f"Component count claims are inaccurate: {component_claims} (actual: {actual_components})",
                        0.0
                    ))
        
        print(f"    ✅ Count Verification: Commands={actual_commands}, Components={actual_components}")
    
    def verify_feature_claims(self):
        """Verify feature claims against actual implementation"""
        
        # Features to verify
        features_to_verify = {
            "Interactive Consultation System": ["3-layer", "layer 1", "layer 2", "layer 3"],
            "Quick Command Auto-Generation": ["30-second", "auto-generate", "intelligence"],
            "Component Library": ["91 component", "atomic component", "assembly"],
            "YAML Compliance": ["100%", "claude code", "allowed-tools"],
            "Template Adaptation": ["placeholder", "customization", "manual"]
        }
        
        for doc_name in self.key_docs:
            doc_path = self.project_root / doc_name
            if not doc_path.exists():
                continue
            
            content = doc_path.read_text(encoding='utf-8').lower()
            
            for feature_name, keywords in features_to_verify.items():
                keywords_found = sum(1 for keyword in keywords if keyword.lower() in content)
                keyword_score = (keywords_found / len(keywords)) * 100
                
                if keywords_found >= len(keywords) // 2:  # At least half the keywords
                    # Verify implementation exists
                    implementation_verified = self.verify_feature_implementation(feature_name)
                    
                    if implementation_verified:
                        self.test_results.append(DocumentationTest(
                            doc_name,
                            f"Feature Claim - {feature_name}",
                            DocTestResult.PASS,
                            f"Feature documented and implemented ({keywords_found}/{len(keywords)} keywords)",
                            keyword_score
                        ))
                    else:
                        self.test_results.append(DocumentationTest(
                            doc_name,
                            f"Feature Claim - {feature_name}",
                            DocTestResult.FAIL,
                            f"Feature documented but not implemented ({keywords_found}/{len(keywords)} keywords)",
                            keyword_score / 2
                        ))
        
        print(f"    ✅ Feature Claims: Verified {len(features_to_verify)} feature categories")
    
    def verify_feature_implementation(self, feature_name: str) -> bool:
        """Verify that claimed features actually exist"""
        
        if feature_name == "Interactive Consultation System":
            # Check for the 3 progressive disclosure commands
            return all((self.commands_dir / "core" / cmd).exists() 
                      for cmd in self.progressive_disclosure_commands)
        
        elif feature_name == "Quick Command Auto-Generation":
            # Check quick-command exists and has auto-generation content
            quick_cmd = self.commands_dir / "core" / "quick-command.md"
            if quick_cmd.exists():
                content = quick_cmd.read_text().lower()
                return "auto-generate" in content and "intelligence" in content
            return False
            
        elif feature_name == "Component Library":
            # Check components directory and count
            return (self.components_dir.exists() and 
                   len(list(self.components_dir.rglob("*.md"))) >= 80)
        
        elif feature_name == "YAML Compliance":
            # Check for Claude Code YAML fields in sample commands
            sample_commands = list(self.commands_dir.rglob("*.md"))[:5]
            compliant_count = 0
            
            for cmd_file in sample_commands:
                try:
                    content = cmd_file.read_text()
                    if "allowed-tools:" in content and not "tools:" in content:
                        compliant_count += 1
                except:
                    continue
            
            return compliant_count >= len(sample_commands) // 2
        
        elif feature_name == "Template Adaptation":
            # Check for placeholder and adaptation-related files
            adaptation_files = list(self.project_root.rglob("*adapt*"))
            placeholder_files = [f for f in self.commands_dir.rglob("*.md") 
                               if "[INSERT_" in f.read_text()]
            return len(adaptation_files) > 0 or len(placeholder_files) > 10
        
        return True  # Default to true for unknown features
    
    def verify_command_examples(self):
        """Verify that documented command examples actually exist"""
        
        for doc_name in self.key_docs:
            doc_path = self.project_root / doc_name
            if not doc_path.exists():
                continue
            
            content = doc_path.read_text(encoding='utf-8')
            
            # Find command references (lines starting with /)
            command_examples = re.findall(r'/([a-z-]+)', content)
            unique_examples = list(set(command_examples))
            
            if not unique_examples:
                continue
            
            # Verify examples exist
            existing_examples = []
            for example in unique_examples:
                example_files = list(self.commands_dir.rglob(f"{example}.md"))
                if example_files:
                    existing_examples.append(example)
            
            if len(existing_examples) == len(unique_examples):
                self.test_results.append(DocumentationTest(
                    doc_name,
                    "Command Examples",
                    DocTestResult.PASS,
                    f"All {len(unique_examples)} command examples exist",
                    100.0
                ))
            elif len(existing_examples) >= len(unique_examples) * 0.8:
                self.test_results.append(DocumentationTest(
                    doc_name,
                    "Command Examples",
                    DocTestResult.WARNING,
                    f"{len(existing_examples)}/{len(unique_examples)} command examples exist",
                    (len(existing_examples) / len(unique_examples)) * 100
                ))
            else:
                self.test_results.append(DocumentationTest(
                    doc_name,
                    "Command Examples",
                    DocTestResult.FAIL,
                    f"Only {len(existing_examples)}/{len(unique_examples)} command examples exist",
                    (len(existing_examples) / len(unique_examples)) * 100
                ))
        
        print(f"    ✅ Command Examples: Verified availability of documented examples")
    
    def verify_progressive_disclosure_claims(self):
        """Verify Interactive Consultation System documentation claims"""
        
        # Check main Interactive Consultation System documentation
        progressive_docs = []
        
        # Find Interactive Consultation System related documentation
        for doc_file in self.project_root.rglob("*progressive*disclosure*.md"):
            progressive_docs.append(doc_file)
        
        # Check main documentation files for Interactive Consultation System content
        for doc_name in self.key_docs:
            doc_path = self.project_root / doc_name
            if doc_path.exists():
                content = doc_path.read_text().lower()
                if "progressive disclosure" in content:
                    progressive_docs.append(doc_path)
        
        if not progressive_docs:
            self.test_results.append(DocumentationTest(
                "system",
                "Interactive Consultation System Documentation",
                DocTestResult.FAIL,
                "No Interactive Consultation System documentation found",
                0.0
            ))
            return
        
        # Test claims in Interactive Consultation System documentation
        for doc_path in progressive_docs:
            content = doc_path.read_text().lower()
            
            # Test layer claims
            layer_claims = {
                "layer 1": "quick-command" in content,
                "layer 2": "build-command" in content,
                "layer 3": "assemble-command" in content
            }
            
            verified_layers = sum(1 for layer, exists in layer_claims.items() 
                                if exists and self.verify_layer_exists(layer))
            
            layer_score = (verified_layers / 3) * 100
            
            if layer_score >= 100:
                self.test_results.append(DocumentationTest(
                    doc_path.name,
                    "Interactive Consultation System Layers",
                    DocTestResult.PASS,
                    f"All 3 layers documented and implemented",
                    layer_score
                ))
            elif layer_score >= 66:
                self.test_results.append(DocumentationTest(
                    doc_path.name,
                    "Interactive Consultation System Layers",
                    DocTestResult.WARNING,
                    f"{verified_layers}/3 layers documented and implemented",
                    layer_score
                ))
            else:
                self.test_results.append(DocumentationTest(
                    doc_path.name,
                    "Interactive Consultation System Layers",
                    DocTestResult.FAIL,
                    f"Only {verified_layers}/3 layers documented and implemented",
                    layer_score
                ))
        
        print(f"    ✅ Interactive Consultation System: {len(progressive_docs)} documentation files verified")
    
    def verify_layer_exists(self, layer_name: str) -> bool:
        """Verify that a Interactive Consultation System layer exists"""
        layer_commands = {
            "layer 1": "quick-command.md",
            "layer 2": "build-command.md", 
            "layer 3": "assemble-command.md"
        }
        
        command_file = layer_commands.get(layer_name)
        if command_file:
            return (self.commands_dir / "core" / command_file).exists()
        return False
    
    def verify_workflow_documentation(self):
        """Verify workflow documentation accuracy"""
        
        # Look for workflow documentation
        workflow_docs = []
        
        for doc_name in self.key_docs:
            doc_path = self.project_root / doc_name
            if doc_path.exists():
                content = doc_path.read_text().lower()
                if any(keyword in content for keyword in ['workflow', 'step by step', 'how to use']):
                    workflow_docs.append(doc_path)
        
        # Test workflow accuracy
        for doc_path in workflow_docs:
            content = doc_path.read_text()
            
            # Check for realistic timelines
            time_claims = re.findall(r'(\d+)\s*(minute|hour|second)', content.lower())
            unrealistic_claims = [claim for claim in time_claims 
                                if (claim[1] == 'second' and int(claim[0]) < 10) or
                                   (claim[1] == 'minute' and int(claim[0]) < 1)]
            
            if not unrealistic_claims:
                self.test_results.append(DocumentationTest(
                    doc_path.name,
                    "Workflow Timelines",
                    DocTestResult.PASS,
                    "Realistic timelines documented",
                    100.0
                ))
            else:
                self.test_results.append(DocumentationTest(
                    doc_path.name,
                    "Workflow Timelines",
                    DocTestResult.WARNING,
                    f"Some timelines may be unrealistic: {unrealistic_claims}",
                    70.0
                ))
            
            # Check for step completeness
            step_references = len(re.findall(r'step \d+', content.lower()))
            if step_references > 0:
                self.test_results.append(DocumentationTest(
                    doc_path.name,
                    "Workflow Steps",
                    DocTestResult.PASS,
                    f"Found {step_references} documented workflow steps",
                    100.0
                ))
        
        print(f"    ✅ Workflow Documentation: {len(workflow_docs)} workflow documents verified")
    
    def generate_documentation_report(self) -> Dict:
        """Generate comprehensive documentation accuracy report"""
        print("\n" + "="*40)
        print("🏆 DOCUMENTATION ACCURACY RESULTS")
        print("="*40)
        
        # Calculate statistics
        total_tests = len(self.test_results)
        passed = sum(1 for r in self.test_results if r.result == DocTestResult.PASS)
        failed = sum(1 for r in self.test_results if r.result == DocTestResult.FAIL)
        warnings = sum(1 for r in self.test_results if r.result == DocTestResult.WARNING)
        
        # Calculate scores by document
        document_scores = {}
        for result in self.test_results:
            doc = result.document
            if doc not in document_scores:
                document_scores[doc] = []
            document_scores[doc].append(result.score)
        
        document_averages = {
            doc: sum(scores) / len(scores) if scores else 0
            for doc, scores in document_scores.items()
        }
        
        overall_score = sum(document_averages.values()) / len(document_averages) if document_averages else 0
        
        print(f"\n📊 DOCUMENTATION ACCURACY SUMMARY:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed}")
        print(f"   ❌ Failed: {failed}")
        print(f"   ⚠️  Warnings: {warnings}")
        print(f"   📈 Overall Accuracy Score: {overall_score:.1f}%")
        
        # Grade assignment
        if overall_score >= 90:
            grade = "A"
        elif overall_score >= 80:
            grade = "B"
        elif overall_score >= 70:
            grade = "C"
        else:
            grade = "D"
        
        print(f"   🎓 Documentation Accuracy Grade: {grade}")
        
        # Document breakdown
        print(f"\n📋 ACCURACY BY DOCUMENT:")
        for doc, avg_score in sorted(document_averages.items()):
            print(f"   {doc}: {avg_score:.1f}%")
        
        # Critical inaccuracies
        critical_failures = [r for r in self.test_results 
                           if r.result == DocTestResult.FAIL and 
                           ('count' in r.test_name.lower() or 
                            'feature' in r.test_name.lower())]
        
        if critical_failures:
            print(f"\n❌ CRITICAL INACCURACIES FOUND:")
            for failure in critical_failures[:3]:  # Show first 3
                print(f"   • {failure.document}: {failure.details}")
            if len(critical_failures) > 3:
                print(f"   • ... and {len(critical_failures) - 3} more critical issues")
        
        # Documentation reliability assessment
        print(f"\n🎯 DOCUMENTATION RELIABILITY ASSESSMENT:")
        
        if overall_score >= 90 and len(critical_failures) == 0:
            print("   ✅ All major claims verified against implementation")
            print("   ✅ Count claims accurate")
            print("   ✅ Feature claims match reality")
            print("   🚀 DOCUMENTATION STATUS: HIGHLY RELIABLE")
        elif overall_score >= 80:
            print("   ⚠️  Most claims verified with minor inaccuracies")
            print("   🔧 DOCUMENTATION STATUS: GENERALLY RELIABLE")
        else:
            print("   ❌ Significant inaccuracies detected")
            print("   🔧 DOCUMENTATION STATUS: NEEDS MAJOR UPDATES")
        
        return {
            "timestamp": "2025-07-31",
            "total_tests": total_tests,
            "passed": passed,
            "failed": failed,
            "warnings": warnings,
            "overall_score": overall_score,
            "grade": grade,
            "document_scores": document_averages,
            "critical_failures": len(critical_failures),
            "system_status": "HIGHLY RELIABLE" if overall_score >= 90 and len(critical_failures) == 0 else "NEEDS WORK",
            "test_details": [
                {
                    "document": r.document,
                    "test_name": r.test_name,
                    "result": r.result.value,
                    "details": r.details,
                    "score": r.score
                } for r in self.test_results
            ]
        }


def main():
    """Run Documentation Accuracy Verification"""
    tester = DocumentationAccuracyTester()
    results = tester.run_documentation_accuracy_tests()
    
    # Save results
    import json
    with open("documentation_accuracy_test_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n🏁 Documentation Accuracy Testing Complete!")
    print(f"   Overall Score: {results['overall_score']:.1f}%")
    print(f"   Grade: {results['grade']}")
    print(f"   Status: {results['system_status']}")
    
    return results


if __name__ == "__main__":
    main()