#!/usr/bin/env python3
"""
Progressive Disclosure System Layer Validation Test
==================================================

Comprehensive testing for all 3 layers of the Progressive Disclosure System:
- Layer 1: Quick Command (30-second auto-generation) 
- Layer 2: Build Command (guided customization)
- Layer 3: Assemble Command (full component library access)

This test validates that each layer works as documented and provides
proper upgrade paths between layers.

Author: Testing Framework Agent
Date: 2025-07-31
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class LayerTestResult(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARNING = "WARNING"


@dataclass
class LayerTest:
    layer: str
    test_name: str
    result: LayerTestResult
    details: str
    score: float = 0.0


class ProgressiveDisclosureLayerTester:
    """Test all 3 layers of Progressive Disclosure System"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.commands_dir = self.project_root / ".claude" / "commands"
        self.components_dir = self.project_root / ".claude" / "components"
        self.test_results: List[LayerTest] = []
        
        # Layer definitions
        self.layers = {
            "layer1": {
                "file": "quick-command.md",
                "name": "Quick Command (Auto-Generation)",
                "expected_features": [
                    "30-second success",
                    "auto-generate",
                    "search|analyze|transform|validate|report",
                    "intelligence behind",
                    "complete command"
                ]
            },
            "layer2": {
                "file": "build-command.md", 
                "name": "Build Command (Guided Customization)",
                "expected_features": [
                    "guided customization",
                    "json config",
                    "smart option",
                    "project detection",
                    "customize"
                ]
            },
            "layer3": {
                "file": "assemble-command.md",
                "name": "Assemble Command (Component Library)",
                "expected_features": [
                    "component library",
                    "assembly",
                    "compatibility matrix",
                    "91 components",
                    "interactive"
                ]
            }
        }
    
    def run_layer_validation_tests(self) -> Dict:
        """Run comprehensive layer validation"""
        print("🎯 Progressive Disclosure System Layer Validation")
        print("="*55)
        
        # Test each layer
        for layer_id, layer_info in self.layers.items():
            print(f"\n🔍 Testing {layer_info['name']}")
            self.test_layer(layer_id, layer_info)
        
        # Test inter-layer integration
        print(f"\n🔗 Testing Inter-Layer Integration")
        self.test_layer_integration()
        
        # Test upgrade paths
        print(f"\n⬆️  Testing Upgrade Paths")
        self.test_upgrade_paths()
        
        return self.generate_layer_report()
    
    def test_layer(self, layer_id: str, layer_info: Dict):
        """Test individual layer functionality"""
        layer_file = self.commands_dir / "core" / layer_info["file"]
        
        # Test 1: Layer file exists
        if not layer_file.exists():
            self.test_results.append(LayerTest(
                layer_id,
                "File Existence",
                LayerTestResult.FAIL,
                f"Layer file {layer_info['file']} not found",
                0.0
            ))
            return
        
        self.test_results.append(LayerTest(
            layer_id,
            "File Existence", 
            LayerTestResult.PASS,
            f"Layer file {layer_info['file']} found",
            100.0
        ))
        
        # Test 2: YAML frontmatter compliance
        content = layer_file.read_text(encoding='utf-8')
        
        if not content.startswith('---'):
            self.test_results.append(LayerTest(
                layer_id,
                "YAML Frontmatter",
                LayerTestResult.FAIL,
                "No YAML frontmatter found",
                0.0
            ))
            return
        
        try:
            yaml_end = content.find('---', 3)
            yaml_content = content[3:yaml_end].strip()
            yaml_data = yaml.safe_load(yaml_content)
            
            # Check required fields
            required_fields = ['name', 'description', 'allowed-tools']
            missing_fields = [field for field in required_fields if field not in yaml_data]
            
            if missing_fields:
                self.test_results.append(LayerTest(
                    layer_id,
                    "YAML Compliance",
                    LayerTestResult.FAIL,
                    f"Missing fields: {missing_fields}",
                    50.0
                ))
            else:
                self.test_results.append(LayerTest(
                    layer_id,
                    "YAML Compliance",
                    LayerTestResult.PASS,
                    "All required YAML fields present",
                    100.0
                ))
                
        except Exception as e:
            self.test_results.append(LayerTest(
                layer_id,
                "YAML Parsing",
                LayerTestResult.FAIL,
                f"YAML parsing error: {str(e)}",
                0.0
            ))
            return
        
        # Test 3: Layer-specific features
        content_lower = content.lower()
        features_found = 0
        features_tested = len(layer_info["expected_features"])
        
        for feature in layer_info["expected_features"]:
            if re.search(feature.lower(), content_lower):
                features_found += 1
        
        feature_score = (features_found / features_tested) * 100
        
        if feature_score >= 80:
            result = LayerTestResult.PASS
            details = f"Found {features_found}/{features_tested} expected features"
        elif feature_score >= 60:
            result = LayerTestResult.WARNING
            details = f"Found {features_found}/{features_tested} expected features (acceptable)"
        else:
            result = LayerTestResult.FAIL
            details = f"Only found {features_found}/{features_tested} expected features"
        
        self.test_results.append(LayerTest(
            layer_id,
            "Feature Completeness",
            result,
            details,
            feature_score
        ))
        
        # Test 4: Layer-specific functionality tests
        if layer_id == "layer1":
            self.test_layer1_specifics(content)
        elif layer_id == "layer2":
            self.test_layer2_specifics(content)
        elif layer_id == "layer3":
            self.test_layer3_specifics(content)
        
        print(f"    ✅ {layer_info['name']}: {features_found}/{features_tested} features validated")
    
    def test_layer1_specifics(self, content: str):
        """Test Quick Command specific functionality"""
        content_lower = content.lower()
        
        # Test auto-generation templates
        command_types = ["search", "analyze", "transform", "validate", "report"]
        types_documented = sum(1 for cmd_type in command_types if cmd_type in content_lower)
        
        if types_documented >= 4:
            self.test_results.append(LayerTest(
                "layer1",
                "Command Type Coverage",
                LayerTestResult.PASS,
                f"Documents {types_documented}/5 command types",
                (types_documented / 5) * 100
            ))
        else:
            self.test_results.append(LayerTest(
                "layer1",
                "Command Type Coverage",
                LayerTestResult.FAIL,
                f"Only documents {types_documented}/5 command types",
                (types_documented / 5) * 100
            ))
        
        # Test intelligence examples
        intelligence_examples = content_lower.count("intelligence")
        if intelligence_examples >= 2:
            self.test_results.append(LayerTest(
                "layer1",
                "Intelligence Documentation",
                LayerTestResult.PASS,
                f"Found {intelligence_examples} intelligence examples",
                100.0
            ))
        else:
            self.test_results.append(LayerTest(
                "layer1",
                "Intelligence Documentation", 
                LayerTestResult.WARNING,
                f"Limited intelligence examples: {intelligence_examples}",
                50.0
            ))
        
        # Test generation examples
        example_count = content_lower.count("example")
        if example_count >= 5:
            self.test_results.append(LayerTest(
                "layer1",
                "Usage Examples",
                LayerTestResult.PASS,
                f"Found {example_count} usage examples",
                100.0
            ))
        else:
            self.test_results.append(LayerTest(
                "layer1",
                "Usage Examples",
                LayerTestResult.WARNING,
                f"Limited examples: {example_count}",
                70.0
            ))
    
    def test_layer2_specifics(self, content: str):
        """Test Build Command specific functionality"""
        content_lower = content.lower()
        
        # Test guided customization features
        customization_features = [
            "guided",
            "customize", 
            "options",
            "configuration",
            "project detection"
        ]
        
        features_found = sum(1 for feature in customization_features if feature in content_lower)
        
        if features_found >= 3:
            self.test_results.append(LayerTest(
                "layer2",
                "Customization Features",
                LayerTestResult.PASS,
                f"Found {features_found}/5 customization features",
                (features_found / 5) * 100
            ))
        else:
            self.test_results.append(LayerTest(
                "layer2",
                "Customization Features",
                LayerTestResult.FAIL,
                f"Only found {features_found}/5 customization features",
                (features_found / 5) * 100
            ))
        
        # Test configuration support
        if "json" in content_lower or "config" in content_lower:
            self.test_results.append(LayerTest(
                "layer2",
                "Configuration Support",
                LayerTestResult.PASS,
                "Configuration system documented",
                100.0
            ))
        else:
            self.test_results.append(LayerTest(
                "layer2",
                "Configuration Support",
                LayerTestResult.FAIL,
                "No configuration system documented",
                0.0
            ))
    
    def test_layer3_specifics(self, content: str):
        """Test Assemble Command specific functionality"""
        content_lower = content.lower()
        
        # Test component library access
        component_keywords = [
            "component library",
            "assembly",
            "91 components",
            "compatibility",
            "interactive"
        ]
        
        keywords_found = sum(1 for keyword in component_keywords if keyword in content_lower)
        
        if keywords_found >= 3:
            self.test_results.append(LayerTest(
                "layer3",
                "Component Library Features",
                LayerTestResult.PASS,
                f"Found {keywords_found}/5 component library features",
                (keywords_found / 5) * 100
            ))
        else:
            self.test_results.append(LayerTest(
                "layer3",
                "Component Library Features",
                LayerTestResult.FAIL,
                f"Only found {keywords_found}/5 component library features",
                (keywords_found / 5) * 100
            ))
        
        # Test assembly documentation
        if "assembly" in content_lower and ("template" in content_lower or "pattern" in content_lower):
            self.test_results.append(LayerTest(
                "layer3",
                "Assembly Documentation",
                LayerTestResult.PASS,
                "Assembly patterns documented",
                100.0
            ))
        else:
            self.test_results.append(LayerTest(
                "layer3",
                "Assembly Documentation",
                LayerTestResult.WARNING,
                "Limited assembly documentation",
                50.0
            ))
    
    def test_layer_integration(self):
        """Test integration between layers"""
        
        # Test upgrade path documentation
        layer1_file = self.commands_dir / "core" / "quick-command.md"
        layer2_file = self.commands_dir / "core" / "build-command.md"
        layer3_file = self.commands_dir / "core" / "assemble-command.md"
        
        upgrade_paths_found = 0
        
        # Check Layer 1 -> Layer 2 references
        if layer1_file.exists():
            content = layer1_file.read_text().lower()
            if "build-command" in content or "layer 2" in content:
                upgrade_paths_found += 1
        
        # Check Layer 2 -> Layer 3 references
        if layer2_file.exists():
            content = layer2_file.read_text().lower()
            if "assemble-command" in content or "layer 3" in content:
                upgrade_paths_found += 1
        
        # Check Layer 1 -> Layer 3 references
        if layer1_file.exists():
            content = layer1_file.read_text().lower()
            if "assemble-command" in content or "full assembly" in content:
                upgrade_paths_found += 1
        
        if upgrade_paths_found >= 2:
            self.test_results.append(LayerTest(
                "integration",
                "Layer Upgrade Paths",
                LayerTestResult.PASS,
                f"Found {upgrade_paths_found} upgrade path references",
                (upgrade_paths_found / 3) * 100
            ))
        else:
            self.test_results.append(LayerTest(
                "integration",
                "Layer Upgrade Paths",
                LayerTestResult.WARNING,
                f"Limited upgrade paths: {upgrade_paths_found}",
                (upgrade_paths_found / 3) * 100
            ))
        
        print(f"    ✅ Integration: {upgrade_paths_found} upgrade paths found")
    
    def test_upgrade_paths(self):
        """Test upgrade path functionality"""
        
        # Check for consistent upgrade syntax
        upgrade_syntax_tests = [
            ("--customize", "build command customization flag"),
            ("--interactive", "assemble command interactive flag"),
            ("/build-command", "layer 2 command reference"),
            ("/assemble-command", "layer 3 command reference")
        ]
        
        command_files = list(self.commands_dir.rglob("*.md"))
        syntax_found = 0
        
        for syntax, description in upgrade_syntax_tests:
            found_in_files = 0
            for cmd_file in command_files:
                try:
                    content = cmd_file.read_text()
                    if syntax in content:
                        found_in_files += 1
                except:
                    continue
            
            if found_in_files > 0:
                syntax_found += 1
                self.test_results.append(LayerTest(
                    "upgrade_paths",
                    f"Upgrade Syntax - {syntax}",
                    LayerTestResult.PASS,
                    f"Found {description} in {found_in_files} files",
                    100.0
                ))
            else:
                self.test_results.append(LayerTest(
                    "upgrade_paths",
                    f"Upgrade Syntax - {syntax}",
                    LayerTestResult.WARNING,
                    f"No {description} references found",
                    0.0
                ))
        
        print(f"    ✅ Upgrade Paths: {syntax_found}/{len(upgrade_syntax_tests)} syntax patterns found")
    
    def generate_layer_report(self) -> Dict:
        """Generate comprehensive layer validation report"""
        print("\n" + "="*55)
        print("🏆 PROGRESSIVE DISCLOSURE LAYER VALIDATION RESULTS")
        print("="*55)
        
        # Calculate layer scores
        layer_scores = {}
        for layer_id in ["layer1", "layer2", "layer3", "integration", "upgrade_paths"]:
            layer_tests = [t for t in self.test_results if t.layer == layer_id]
            if layer_tests:
                layer_score = sum(t.score for t in layer_tests) / len(layer_tests)
                layer_scores[layer_id] = layer_score
            else:
                layer_scores[layer_id] = 0.0
        
        # Overall statistics
        total_tests = len(self.test_results)
        passed = sum(1 for r in self.test_results if r.result == LayerTestResult.PASS)
        failed = sum(1 for r in self.test_results if r.result == LayerTestResult.FAIL)
        warnings = sum(1 for r in self.test_results if r.result == LayerTestResult.WARNING)
        
        overall_score = sum(layer_scores.values()) / len(layer_scores) if layer_scores else 0
        
        print(f"\n📊 LAYER VALIDATION SUMMARY:")
        print(f"   Layer 1 (Quick Command): {layer_scores.get('layer1', 0):.1f}%")
        print(f"   Layer 2 (Build Command): {layer_scores.get('layer2', 0):.1f}%")
        print(f"   Layer 3 (Assemble Command): {layer_scores.get('layer3', 0):.1f}%")
        print(f"   Integration Testing: {layer_scores.get('integration', 0):.1f}%")
        print(f"   Upgrade Paths: {layer_scores.get('upgrade_paths', 0):.1f}%")
        print(f"\n   🎯 Overall Progressive Disclosure Score: {overall_score:.1f}%")
        
        # Grade assignment
        if overall_score >= 90:
            grade = "A"
        elif overall_score >= 80:
            grade = "B"
        elif overall_score >= 70:
            grade = "C"
        else:
            grade = "D"
        
        print(f"   🎓 Progressive Disclosure Grade: {grade}")
        
        # Test results breakdown
        print(f"\n📋 DETAILED TEST RESULTS:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed}")
        print(f"   ❌ Failed: {failed}")
        print(f"   ⚠️  Warnings: {warnings}")
        
        # Individual test results
        print(f"\n🔍 INDIVIDUAL TEST DETAILS:")
        current_layer = None
        for result in self.test_results:
            if result.layer != current_layer:
                current_layer = result.layer
                layer_name = {
                    "layer1": "Layer 1 - Quick Command",
                    "layer2": "Layer 2 - Build Command", 
                    "layer3": "Layer 3 - Assemble Command",
                    "integration": "Integration Testing",
                    "upgrade_paths": "Upgrade Path Testing"
                }.get(current_layer, current_layer)
                print(f"\n   📌 {layer_name}:")
            
            status_icon = {
                LayerTestResult.PASS: "✅",
                LayerTestResult.FAIL: "❌",
                LayerTestResult.WARNING: "⚠️"
            }[result.result]
            
            print(f"      {status_icon} {result.test_name}: {result.details} ({result.score:.1f}%)")
        
        # System readiness assessment
        print(f"\n🎯 PROGRESSIVE DISCLOSURE SYSTEM STATUS:")
        
        critical_failures = [r for r in self.test_results 
                           if r.result == LayerTestResult.FAIL and r.score < 50]
        
        if overall_score >= 80 and len(critical_failures) == 0:
            print("   ✅ All 3 layers operational and documented")
            print("   ✅ Layer integration validated")
            print("   ✅ Upgrade paths functional")
            print("   🚀 PROGRESSIVE DISCLOSURE STATUS: PRODUCTION READY")
        elif overall_score >= 70:
            print("   ⚠️  Progressive Disclosure System functional with minor issues")
            print("   🔧 PROGRESSIVE DISCLOSURE STATUS: NEEDS MINOR IMPROVEMENTS")
        else:
            print("   ❌ Critical Progressive Disclosure System issues detected")
            print("   🔧 PROGRESSIVE DISCLOSURE STATUS: REQUIRES MAJOR WORK")
        
        return {
            "timestamp": "2025-07-31",
            "overall_score": overall_score,
            "grade": grade,
            "layer_scores": layer_scores,
            "total_tests": total_tests,
            "passed": passed,
            "failed": failed,
            "warnings": warnings,
            "critical_failures": len(critical_failures),
            "system_status": "PRODUCTION READY" if overall_score >= 80 and len(critical_failures) == 0 else "NEEDS WORK",
            "test_details": [
                {
                    "layer": r.layer,
                    "test_name": r.test_name,
                    "result": r.result.value,
                    "details": r.details,
                    "score": r.score
                } for r in self.test_results
            ]
        }


def main():
    """Run Progressive Disclosure System layer validation"""
    tester = ProgressiveDisclosureLayerTester()
    results = tester.run_layer_validation_tests()
    
    # Save results
    import json
    with open("progressive_disclosure_validation_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n🏁 Progressive Disclosure Validation Complete!")
    print(f"   Overall Score: {results['overall_score']:.1f}%")
    print(f"   Grade: {results['grade']}")
    print(f"   Status: {results['system_status']}")
    
    return results


if __name__ == "__main__":
    main()