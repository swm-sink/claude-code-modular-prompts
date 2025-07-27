#!/usr/bin/env python3
"""
Claude Code Functional Testing
Test commands within Claude Code context rather than shell execution
"""

import json
import os
import time
from datetime import datetime
import re

class ClaudeCodeFunctionalTester:
    def __init__(self, commands_dir=".claude/commands"):
        self.commands_dir = commands_dir
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "total_tests": 0,
            "passed_tests": 0,
            "failed_tests": 0,
            "test_results": {},
            "functional_score": 0.0
        }

    def analyze_command_structure(self, file_path):
        """Analyze command structure for functional testing"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract YAML front matter
            yaml_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            yaml_data = {}
            if yaml_match:
                yaml_content = yaml_match.group(1)
                for line in yaml_content.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        yaml_data[key.strip()] = value.strip()
            
            # Analyze command content structure
            analysis = {
                "has_yaml_frontmatter": bool(yaml_match),
                "command_name": yaml_data.get('name', ''),
                "description": yaml_data.get('description', ''),
                "usage": yaml_data.get('usage', ''),
                "tools": yaml_data.get('tools', ''),
                "content_length": len(content),
                "has_examples": 'example' in content.lower() or '```' in content,
                "has_instructions": any(word in content.lower() for word in ['step', 'instruction', 'process', 'execute']),
                "has_security_considerations": 'security' in content.lower() or 'safe' in content.lower(),
                "component_includes": len(re.findall(r'<include>.*?</include>', content)),
                "xml_structure": bool(re.search(r'<\w+>', content))
            }
            
            return analysis
            
        except Exception as e:
            return {"error": str(e)}

    def test_command_completeness(self, analysis):
        """Test if command has all necessary elements for functionality"""
        score = 0
        max_score = 10
        issues = []
        
        # Required elements (2 points each)
        if analysis.get("has_yaml_frontmatter"):
            score += 2
        else:
            issues.append("Missing YAML front matter")
            
        if analysis.get("command_name"):
            score += 2
        else:
            issues.append("Missing command name")
            
        # Important elements (1 point each)
        if analysis.get("description"):
            score += 1
        else:
            issues.append("Missing description")
            
        if analysis.get("content_length", 0) > 100:
            score += 1
        else:
            issues.append("Insufficient content length")
            
        if analysis.get("has_instructions"):
            score += 1
        else:
            issues.append("Missing clear instructions")
            
        if analysis.get("has_examples"):
            score += 1
        else:
            issues.append("Missing examples")
            
        # Bonus elements (1 point each)
        if analysis.get("usage"):
            score += 1
            
        if analysis.get("has_security_considerations"):
            score += 1
            
        return {
            "score": score,
            "max_score": max_score,
            "percentage": (score / max_score) * 100,
            "issues": issues,
            "passed": score >= 7  # 70% threshold
        }

    def test_command_claude_code_compliance(self, analysis):
        """Test Claude Code specific compliance"""
        score = 0
        max_score = 8
        issues = []
        
        # Claude Code specific requirements
        if analysis.get("command_name", "").startswith('/'):
            score += 2
        else:
            issues.append("Command name should start with /")
            
        if analysis.get("tools"):
            score += 2
        else:
            issues.append("No tools specified")
            
        if analysis.get("xml_structure"):
            score += 2
        else:
            issues.append("No XML structure found")
            
        if analysis.get("component_includes") > 0:
            score += 2
        else:
            issues.append("No component includes found")
            
        return {
            "score": score,
            "max_score": max_score,
            "percentage": (score / max_score) * 100,
            "issues": issues,
            "passed": score >= 5  # 62.5% threshold
        }

    def run_functional_tests(self):
        """Run functional tests on all commands"""
        print("🚀 Claude Code Functional Testing")
        print("=" * 80)
        
        # Get all command files
        command_files = []
        for root, dirs, files in os.walk(self.commands_dir):
            for file in files:
                if file.endswith('.md'):
                    command_files.append(os.path.join(root, file))
        
        print(f"📊 Testing {len(command_files)} command files...")
        
        passed_tests = 0
        total_tests = len(command_files)
        
        for file_path in command_files:
            self.results["total_tests"] += 1
            
            # Get relative path for cleaner output
            rel_path = os.path.relpath(file_path, self.commands_dir)
            
            try:
                # Analyze command structure
                analysis = self.analyze_command_structure(file_path)
                
                if "error" in analysis:
                    print(f"❌ ERROR: {rel_path} - {analysis['error']}")
                    self.results["test_results"][rel_path] = {"status": "error", "error": analysis["error"]}
                    continue
                
                # Run completeness test
                completeness = self.test_command_completeness(analysis)
                
                # Run Claude Code compliance test
                compliance = self.test_command_claude_code_compliance(analysis)
                
                # Overall test result
                overall_passed = completeness["passed"] and compliance["passed"]
                
                if overall_passed:
                    print(f"✅ PASS: {rel_path}")
                    passed_tests += 1
                    self.results["passed_tests"] += 1
                else:
                    print(f"❌ FAIL: {rel_path}")
                    print(f"   Completeness: {completeness['percentage']:.1f}% | Compliance: {compliance['percentage']:.1f}%")
                    self.results["failed_tests"] += 1
                
                # Store detailed results
                self.results["test_results"][rel_path] = {
                    "status": "pass" if overall_passed else "fail",
                    "completeness": completeness,
                    "compliance": compliance,
                    "analysis": analysis
                }
                
            except Exception as e:
                print(f"❌ ERROR: {rel_path} - {str(e)}")
                self.results["test_results"][rel_path] = {"status": "error", "error": str(e)}
        
        # Calculate final score
        if total_tests > 0:
            self.results["functional_score"] = (passed_tests / total_tests) * 100
        
        print("\n" + "=" * 80)
        print(f"✅ Functional testing completed")
        print(f"📊 Results: {passed_tests}/{total_tests} commands passed ({self.results['functional_score']:.1f}%)")
        print("=" * 80)
        
        return self.results

    def generate_report(self, output_file="tests/results/functional_validation_report.json"):
        """Generate detailed report"""
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        # Generate markdown report
        md_file = output_file.replace('.json', '.md')
        with open(md_file, 'w') as f:
            f.write(f"# Claude Code Functional Validation Report\n\n")
            f.write(f"**Generated:** {self.results['timestamp']}\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"- **Total Commands Tested:** {self.results['total_tests']}\n")
            f.write(f"- **Passed:** {self.results['passed_tests']}\n")
            f.write(f"- **Failed:** {self.results['failed_tests']}\n")
            f.write(f"- **Success Rate:** {self.results['functional_score']:.1f}%\n\n")
            
            f.write(f"## Test Results\n\n")
            for command, result in self.results['test_results'].items():
                status_icon = "✅" if result['status'] == 'pass' else "❌" if result['status'] == 'fail' else "⚠️"
                f.write(f"### {status_icon} {command}\n\n")
                
                if result['status'] in ['pass', 'fail']:
                    f.write(f"- **Completeness:** {result['completeness']['percentage']:.1f}%\n")
                    f.write(f"- **Compliance:** {result['compliance']['percentage']:.1f}%\n")
                    if result['completeness']['issues']:
                        f.write(f"- **Issues:** {', '.join(result['completeness']['issues'] + result['compliance']['issues'])}\n")
                elif result['status'] == 'error':
                    f.write(f"- **Error:** {result['error']}\n")
                f.write("\n")
        
        print(f"📋 Detailed reports generated:")
        print(f"   JSON: {output_file}")
        print(f"   Markdown: {md_file}")

if __name__ == "__main__":
    tester = ClaudeCodeFunctionalTester()
    results = tester.run_functional_tests()
    tester.generate_report()