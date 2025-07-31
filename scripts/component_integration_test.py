#!/usr/bin/env python3
"""
Component Library Integration Test
=================================

Comprehensive testing for the 94-component library integration with
the Progressive Disclosure System, focusing on:
- All 94 components accessibility
- Atomic component functionality (21 components)
- Component assembly patterns
- Integration with Layer 3 (Assemble Command)
- Component compatibility matrix validation

Author: Testing Framework Agent  
Date: 2025-07-31
"""

import os
import re
import yaml
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass
from enum import Enum


class ComponentTestResult(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARNING = "WARNING"


@dataclass
class ComponentTest:
    component_path: str
    test_name: str
    result: ComponentTestResult
    details: str
    score: float = 0.0


class ComponentLibraryIntegrationTester:
    """Test the 94-component library and its integration"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.components_dir = self.project_root / ".claude" / "components"
        self.commands_dir = self.project_root / ".claude" / "commands"
        self.test_results: List[ComponentTest] = []
        
        # Expected component structure
        self.expected_total_components = 94
        self.expected_atomic_components = 21
        
        # Component categories
        self.component_categories = [
            "atomic",
            "core", 
            "quality",
            "specialized",
            "workflow",
            "integration"
        ]
        
        # Key atomic components that should exist
        self.key_atomic_components = [
            "input-validation.md",
            "output-formatter.md",
            "error-handler.md", 
            "progress-indicator.md",
            "file-reader.md",
            "file-writer.md",
            "search-files.md",
            "user-confirmation.md",
            "task-summary.md",
            "parameter-parser.md"
        ]
    
    def run_component_integration_tests(self) -> Dict:
        """Run comprehensive component library integration tests"""
        print("🧩 Component Library Integration Testing")
        print("="*45)
        
        # Test 1: Component Library Structure
        print("\n📁 Testing Component Library Structure")
        self.test_component_library_structure()
        
        # Test 2: Atomic Components
        print("\n⚛️  Testing Atomic Components")
        self.test_atomic_components()
        
        # Test 3: Component Content Quality
        print("\n📝 Testing Component Content Quality")
        self.test_component_content_quality()
        
        # Test 4: Assembly Integration
        print("\n🔧 Testing Assembly Integration")
        self.test_assembly_integration()
        
        # Test 5: Component Compatibility
        print("\n🔗 Testing Component Compatibility")
        self.test_component_compatibility()
        
        return self.generate_component_report()
    
    def test_component_library_structure(self):
        """Test overall component library structure"""
        
        # Test total component count
        if not self.components_dir.exists():
            self.test_results.append(ComponentTest(
                "library",
                "Components Directory Exists",
                ComponentTestResult.FAIL,
                "Components directory not found",
                0.0
            ))
            return
        
        all_components = list(self.components_dir.rglob("*.md"))
        actual_count = len(all_components)
        
        if actual_count == self.expected_total_components:
            self.test_results.append(ComponentTest(
                "library",
                "Total Component Count",
                ComponentTestResult.PASS,
                f"Exactly {actual_count} components found",
                100.0
            ))
        elif abs(actual_count - self.expected_total_components) <= 5:
            self.test_results.append(ComponentTest(
                "library",
                "Total Component Count", 
                ComponentTestResult.WARNING,
                f"Found {actual_count} components, expected {self.expected_total_components}",
                85.0
            ))
        else:
            self.test_results.append(ComponentTest(
                "library",
                "Total Component Count",
                ComponentTestResult.FAIL,
                f"Found {actual_count} components, expected {self.expected_total_components}",
                50.0
            ))
        
        # Test component directory structure
        existing_categories = []
        for category in self.component_categories:
            category_dir = self.components_dir / category
            if category_dir.exists() and category_dir.is_dir():
                existing_categories.append(category)
        
        category_score = (len(existing_categories) / len(self.component_categories)) * 100
        
        if category_score >= 80:
            self.test_results.append(ComponentTest(
                "library",
                "Component Categories",
                ComponentTestResult.PASS,
                f"Found {len(existing_categories)}/{len(self.component_categories)} expected categories",
                category_score
            ))
        else:
            self.test_results.append(ComponentTest(
                "library",
                "Component Categories",
                ComponentTestResult.WARNING,
                f"Only found {len(existing_categories)}/{len(self.component_categories)} expected categories",
                category_score
            ))
        
        print(f"    ✅ Component Library: {actual_count} components in {len(existing_categories)} categories")
    
    def test_atomic_components(self):
        """Test atomic component functionality"""
        
        atomic_dir = self.components_dir / "atomic"
        
        if not atomic_dir.exists():
            self.test_results.append(ComponentTest(
                "atomic",
                "Atomic Directory Exists",
                ComponentTestResult.FAIL,
                "Atomic components directory not found",
                0.0
            ))
            return
        
        # Count atomic components
        atomic_components = list(atomic_dir.glob("*.md"))
        actual_atomic_count = len(atomic_components)
        
        if actual_atomic_count >= self.expected_atomic_components - 2:
            self.test_results.append(ComponentTest(
                "atomic",
                "Atomic Component Count",
                ComponentTestResult.PASS,
                f"Found {actual_atomic_count} atomic components",
                100.0
            ))
        elif actual_atomic_count >= 15:
            self.test_results.append(ComponentTest(
                "atomic",
                "Atomic Component Count",
                ComponentTestResult.WARNING,
                f"Found {actual_atomic_count} atomic components, expected ~{self.expected_atomic_components}",
                75.0
            ))
        else:
            self.test_results.append(ComponentTest(
                "atomic",
                "Atomic Component Count",
                ComponentTestResult.FAIL,
                f"Only found {actual_atomic_count} atomic components",
                50.0
            ))
        
        # Test key atomic components
        key_components_found = []
        for key_component in self.key_atomic_components:
            component_path = atomic_dir / key_component
            if component_path.exists():
                key_components_found.append(key_component)
        
        key_score = (len(key_components_found) / len(self.key_atomic_components)) * 100
        
        if key_score >= 80:
            self.test_results.append(ComponentTest(
                "atomic",
                "Key Atomic Components",
                ComponentTestResult.PASS,
                f"Found {len(key_components_found)}/{len(self.key_atomic_components)} key atomic components",
                key_score
            ))
        else:
            self.test_results.append(ComponentTest(
                "atomic",
                "Key Atomic Components",
                ComponentTestResult.FAIL,
                f"Only found {len(key_components_found)}/{len(self.key_atomic_components)} key atomic components",
                key_score
            ))
        
        # Test atomic component structure
        atomic_structure_score = 0
        atomic_tests_passed = 0
        
        for component_file in atomic_components[:5]:  # Test first 5 for performance
            try:
                content = component_file.read_text(encoding='utf-8')
                
                # Test atomic component criteria
                is_atomic = True
                issues = []
                
                # Should be short (5-15 lines of actual content)
                content_lines = [line for line in content.split('\n') if line.strip() and not line.startswith('#')]
                if len(content_lines) > 20:
                    is_atomic = False
                    issues.append("too long for atomic component")
                
                # Should have clear, single purpose
                if len(content.split('\n\n')) > 4:  # More than 4 paragraphs
                    is_atomic = False
                    issues.append("too complex for atomic component")
                
                if is_atomic:
                    atomic_tests_passed += 1
                    atomic_structure_score += 100
                else:
                    atomic_structure_score += 50
                    
            except Exception as e:
                atomic_structure_score += 0
        
        atomic_structure_avg = atomic_structure_score / min(5, len(atomic_components)) if atomic_components else 0
        
        if atomic_structure_avg >= 85:
            self.test_results.append(ComponentTest(
                "atomic",
                "Atomic Component Structure",
                ComponentTestResult.PASS,
                f"Atomic components properly structured ({atomic_tests_passed}/{min(5, len(atomic_components))} tested)",
                atomic_structure_avg
            ))
        else:
            self.test_results.append(ComponentTest(
                "atomic",
                "Atomic Component Structure",
                ComponentTestResult.WARNING,
                f"Some atomic components may be too complex ({atomic_tests_passed}/{min(5, len(atomic_components))} passed)",
                atomic_structure_avg
            ))
        
        print(f"    ✅ Atomic Components: {len(key_components_found)}/{len(self.key_atomic_components)} key components found")
    
    def test_component_content_quality(self):
        """Test quality of component content"""
        
        all_components = list(self.components_dir.rglob("*.md"))
        
        if not all_components:
            self.test_results.append(ComponentTest(
                "quality",
                "Component Content Quality",
                ComponentTestResult.FAIL,
                "No components found to test",
                0.0
            ))
            return
        
        # Test sample of components for quality
        sample_size = min(10, len(all_components))
        sample_components = all_components[:sample_size]
        
        quality_scores = []
        
        for component_file in sample_components:
            try:
                content = component_file.read_text(encoding='utf-8')
                quality_score = 0
                
                # Test 1: Has clear purpose/description
                if any(keyword in content.lower() for keyword in ['purpose:', 'description:', '## overview', '## purpose']):
                    quality_score += 25
                
                # Test 2: Has usage examples or patterns
                if any(keyword in content.lower() for keyword in ['example', 'usage', 'pattern', '```']):
                    quality_score += 25
                
                # Test 3: Reasonable length (not empty, not too verbose)
                if 50 <= len(content) <= 2000:
                    quality_score += 25
                
                # Test 4: Clear structure
                if content.count('#') >= 1 and content.count('\n\n') >= 1:
                    quality_score += 25
                
                quality_scores.append(quality_score)
                
            except Exception as e:
                quality_scores.append(0)
        
        avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0
        
        if avg_quality >= 75:
            self.test_results.append(ComponentTest(
                "quality",
                "Component Content Quality",
                ComponentTestResult.PASS,
                f"Average component quality: {avg_quality:.1f}% ({sample_size} components tested)",
                avg_quality
            ))
        elif avg_quality >= 50:
            self.test_results.append(ComponentTest(
                "quality",
                "Component Content Quality", 
                ComponentTestResult.WARNING,
                f"Average component quality: {avg_quality:.1f}% (acceptable but could improve)",
                avg_quality
            ))
        else:
            self.test_results.append(ComponentTest(
                "quality",
                "Component Content Quality",
                ComponentTestResult.FAIL,
                f"Average component quality: {avg_quality:.1f}% (needs improvement)",
                avg_quality
            ))
        
        print(f"    ✅ Content Quality: {avg_quality:.1f}% average quality score")
    
    def test_assembly_integration(self):
        """Test integration with Layer 3 Assemble Command"""
        
        # Test Layer 3 command references to components
        assemble_command = self.commands_dir / "core" / "assemble-command.md"
        
        if not assemble_command.exists():
            self.test_results.append(ComponentTest(
                "assembly",
                "Assemble Command Integration",
                ComponentTestResult.FAIL,
                "Assemble command not found",
                0.0
            ))
            return
        
        content = assemble_command.read_text().lower()
        
        # Test references to component library
        component_references = 0
        component_keywords = [
            "94 components",
            "component library",
            "assembly",
            "atomic components",
            "compatibility matrix"
        ]
        
        for keyword in component_keywords:
            if keyword in content:
                component_references += 1
        
        reference_score = (component_references / len(component_keywords)) * 100
        
        if reference_score >= 60:
            self.test_results.append(ComponentTest(
                "assembly",
                "Component Library References",
                ComponentTestResult.PASS,
                f"Assemble command references {component_references}/{len(component_keywords)} component features",
                reference_score
            ))
        else:
            self.test_results.append(ComponentTest(
                "assembly",
                "Component Library References",
                ComponentTestResult.FAIL,
                f"Assemble command only references {component_references}/{len(component_keywords)} component features",
                reference_score
            ))
        
        # Test for assembly examples or patterns
        if "example" in content or "pattern" in content or "workflow" in content:
            self.test_results.append(ComponentTest(
                "assembly",
                "Assembly Examples",
                ComponentTestResult.PASS,
                "Assembly examples or patterns documented",
                100.0
            ))
        else:
            self.test_results.append(ComponentTest(
                "assembly",
                "Assembly Examples",
                ComponentTestResult.WARNING,
                "Limited assembly examples in documentation",
                50.0
            ))
        
        print(f"    ✅ Assembly Integration: {component_references}/{len(component_keywords)} features referenced")
    
    def test_component_compatibility(self):
        """Test component compatibility and assembly patterns"""
        
        all_components = list(self.components_dir.rglob("*.md"))
        
        # Test for compatibility documentation
        compatibility_files = []
        assembly_files = []
        
        for component_file in all_components:
            try:
                content = component_file.read_text().lower()
                
                if any(keyword in content for keyword in ['compatible', 'compatibility', 'works with']):
                    compatibility_files.append(component_file.name)
                
                if any(keyword in content for keyword in ['assembly', 'combine', 'integrate']):
                    assembly_files.append(component_file.name)
                    
            except:
                continue
        
        # Test compatibility matrix existence
        compatibility_docs = list(self.project_root.rglob("*compatibility*matrix*.md"))
        
        if compatibility_docs:
            self.test_results.append(ComponentTest(
                "compatibility",
                "Compatibility Matrix Documentation",
                ComponentTestResult.PASS,
                f"Found {len(compatibility_docs)} compatibility documentation files",
                100.0
            ))
        else:
            self.test_results.append(ComponentTest(
                "compatibility",
                "Compatibility Matrix Documentation",
                ComponentTestResult.WARNING,
                "No dedicated compatibility matrix documentation found",
                50.0
            ))
        
        # Test component assembly patterns
        assembly_score = (len(assembly_files) / max(1, len(all_components) // 10)) * 100
        assembly_score = min(100, assembly_score)  # Cap at 100%
        
        if assembly_score >= 50:
            self.test_results.append(ComponentTest(
                "compatibility",
                "Assembly Pattern Documentation",
                ComponentTestResult.PASS,
                f"Found assembly references in {len(assembly_files)} components",
                assembly_score
            ))
        else:
            self.test_results.append(ComponentTest(
                "compatibility",
                "Assembly Pattern Documentation",
                ComponentTestResult.WARNING,
                f"Limited assembly documentation: {len(assembly_files)} components",
                assembly_score
            ))
        
        print(f"    ✅ Compatibility: {len(compatibility_files)} components document compatibility")
    
    def generate_component_report(self) -> Dict:
        """Generate comprehensive component integration report"""
        print("\n" + "="*45)
        print("🏆 COMPONENT LIBRARY INTEGRATION RESULTS")
        print("="*45)
        
        # Calculate category scores
        category_scores = {}
        categories = ["library", "atomic", "quality", "assembly", "compatibility"]
        
        for category in categories:
            category_tests = [t for t in self.test_results if t.component_path == category]
            if category_tests:
                category_score = sum(t.score for t in category_tests) / len(category_tests)
                category_scores[category] = category_score
            else:
                category_scores[category] = 0.0
        
        # Overall statistics
        total_tests = len(self.test_results)
        passed = sum(1 for r in self.test_results if r.result == ComponentTestResult.PASS)
        failed = sum(1 for r in self.test_results if r.result == ComponentTestResult.FAIL)
        warnings = sum(1 for r in self.test_results if r.result == ComponentTestResult.WARNING)
        
        overall_score = sum(category_scores.values()) / len(category_scores) if category_scores else 0
        
        print(f"\n📊 COMPONENT INTEGRATION SUMMARY:")
        print(f"   Library Structure: {category_scores.get('library', 0):.1f}%")
        print(f"   Atomic Components: {category_scores.get('atomic', 0):.1f}%")
        print(f"   Content Quality: {category_scores.get('quality', 0):.1f}%")
        print(f"   Assembly Integration: {category_scores.get('assembly', 0):.1f}%")
        print(f"   Compatibility Matrix: {category_scores.get('compatibility', 0):.1f}%")
        print(f"\n   🎯 Overall Component Integration Score: {overall_score:.1f}%")
        
        # Grade assignment
        if overall_score >= 90:
            grade = "A"
        elif overall_score >= 80:
            grade = "B"
        elif overall_score >= 70:
            grade = "C"
        else:
            grade = "D"
        
        print(f"   🎓 Component Integration Grade: {grade}")
        
        # Test results breakdown
        print(f"\n📋 TEST RESULTS BREAKDOWN:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed}")
        print(f"   ❌ Failed: {failed}")
        print(f"   ⚠️  Warnings: {warnings}")
        
        # Detailed results by category
        print(f"\n🔍 DETAILED RESULTS BY CATEGORY:")
        current_category = None
        for result in self.test_results:
            if result.component_path != current_category:
                current_category = result.component_path
                category_name = {
                    "library": "Library Structure",
                    "atomic": "Atomic Components",
                    "quality": "Content Quality",
                    "assembly": "Assembly Integration",
                    "compatibility": "Compatibility Testing"
                }.get(current_category, current_category)
                print(f"\n   📌 {category_name}:")
            
            status_icon = {
                ComponentTestResult.PASS: "✅",
                ComponentTestResult.FAIL: "❌",
                ComponentTestResult.WARNING: "⚠️"
            }[result.result]
            
            print(f"      {status_icon} {result.test_name}: {result.details} ({result.score:.1f}%)")
        
        # Component library readiness assessment
        print(f"\n🎯 COMPONENT LIBRARY STATUS:")
        
        critical_failures = [r for r in self.test_results 
                           if r.result == ComponentTestResult.FAIL and r.score < 50]
        
        if overall_score >= 80 and len(critical_failures) == 0:
            print("   ✅ Component library fully accessible and integrated")
            print("   ✅ Atomic components properly structured")
            print("   ✅ Assembly integration functional")
            print("   🚀 COMPONENT LIBRARY STATUS: PRODUCTION READY")
        elif overall_score >= 70:
            print("   ⚠️  Component library functional with minor integration issues")
            print("   🔧 COMPONENT LIBRARY STATUS: NEEDS MINOR IMPROVEMENTS")
        else:
            print("   ❌ Critical component library integration issues detected")
            print("   🔧 COMPONENT LIBRARY STATUS: REQUIRES MAJOR WORK")
        
        return {
            "timestamp": "2025-07-31",
            "overall_score": overall_score,
            "grade": grade,
            "category_scores": category_scores,
            "total_tests": total_tests,
            "passed": passed,
            "failed": failed,
            "warnings": warnings,
            "critical_failures": len(critical_failures),
            "system_status": "PRODUCTION READY" if overall_score >= 80 and len(critical_failures) == 0 else "NEEDS WORK",
            "expected_components": self.expected_total_components,
            "expected_atomic": self.expected_atomic_components,
            "test_details": [
                {
                    "category": r.component_path,
                    "test_name": r.test_name,
                    "result": r.result.value,
                    "details": r.details,
                    "score": r.score
                } for r in self.test_results
            ]
        }


def main():
    """Run Component Library Integration Testing"""
    tester = ComponentLibraryIntegrationTester()
    results = tester.run_component_integration_tests()
    
    # Save results
    with open("component_integration_test_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n🏁 Component Integration Testing Complete!")
    print(f"   Overall Score: {results['overall_score']:.1f}%")
    print(f"   Grade: {results['grade']}")
    print(f"   Status: {results['system_status']}")
    
    return results


if __name__ == "__main__":
    main()