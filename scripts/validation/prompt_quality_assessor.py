#!/usr/bin/env python3
"""
Prompt Quality Assessor

Integrates with the Claude framework's ultra-critical quality scoring system
to provide accurate quality assessment for prompt engineering changes.
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
import math

class PromptQualityAssessor:
    """Advanced quality assessor using framework's ultra-critical quality scoring."""
    
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)
        self.claude_dir = self.repo_root / ".claude"
        self.baseline_score = 85  # Framework baseline from production-standards.md
        
        # Quality dimensions from production-standards.md
        self.quality_dimensions = {
            "code_quality": {"weight": 0.25, "score": 0},
            "framework_effectiveness": {"weight": 0.20, "score": 0},
            "critical_thinking": {"weight": 0.20, "score": 0},
            "process_quality": {"weight": 0.15, "score": 0},
            "predictive_analytics": {"weight": 0.10, "score": 0},
            "architectural_fitness": {"weight": 0.10, "score": 0}
        }
        
    def assess_quality(self, changed_files: List[str], analysis_results: Dict = None) -> Dict:
        """Main quality assessment entry point."""
        print("📊 Starting ultra-critical quality assessment...")
        
        # Initialize scores
        self._initialize_dimension_scores()
        
        # Assess each dimension
        self._assess_code_quality(changed_files)
        self._assess_framework_effectiveness(changed_files)
        self._assess_critical_thinking(changed_files)
        self._assess_process_quality(changed_files, analysis_results)
        self._assess_predictive_analytics(changed_files)
        self._assess_architectural_fitness(changed_files)
        
        # Calculate overall score
        overall_score = self._calculate_overall_score()
        
        # Generate quality assessment
        assessment = {
            "overall_score": overall_score,
            "grade": self._get_grade(overall_score),
            "dimensions": dict(self.quality_dimensions),
            "recommendations": self._generate_quality_recommendations(),
            "compliance": self._check_compliance(overall_score),
            "risk_factors": self._identify_risk_factors(),
            "improvement_actions": self._suggest_improvements()
        }
        
        print(f"📊 Quality Assessment Complete: {overall_score}/100 ({assessment['grade']})")
        return assessment
    
    def _initialize_dimension_scores(self):
        """Initialize dimension scores to baseline."""
        for dimension in self.quality_dimensions:
            self.quality_dimensions[dimension]["score"] = self.baseline_score
    
    def _assess_code_quality(self, changed_files: List[str]):
        """Assess code quality dimension (25% weight)."""
        print("📝 Assessing code quality dimension...")
        
        score = self.baseline_score
        
        # Analyze file structure and organization
        structure_score = self._assess_file_structure(changed_files)
        
        # Analyze content quality
        content_score = self._assess_content_quality(changed_files)
        
        # Analyze consistency
        consistency_score = self._assess_consistency(changed_files)
        
        # Weighted average
        score = (structure_score * 0.4 + content_score * 0.4 + consistency_score * 0.2)
        
        self.quality_dimensions["code_quality"]["score"] = max(0, min(100, score))
    
    def _assess_framework_effectiveness(self, changed_files: List[str]):
        """Assess framework effectiveness dimension (20% weight)."""
        print("🚀 Assessing framework effectiveness dimension...")
        
        score = self.baseline_score
        
        # Check command delegation success
        delegation_score = self._assess_command_delegation(changed_files)
        
        # Check module coupling
        coupling_score = self._assess_module_coupling(changed_files)
        
        # Check pattern reusability
        reusability_score = self._assess_pattern_reusability(changed_files)
        
        # Weighted average
        score = (delegation_score * 0.4 + coupling_score * 0.3 + reusability_score * 0.3)
        
        self.quality_dimensions["framework_effectiveness"]["score"] = max(0, min(100, score))
    
    def _assess_critical_thinking(self, changed_files: List[str]):
        """Assess critical thinking dimension (20% weight)."""
        print("🧠 Assessing critical thinking dimension...")
        
        score = self.baseline_score
        
        # Look for thinking patterns
        thinking_patterns = self._analyze_thinking_patterns(changed_files)
        
        # Look for assumption challenges
        assumption_challenges = self._analyze_assumption_challenges(changed_files)
        
        # Look for evidence validation
        evidence_validation = self._analyze_evidence_validation(changed_files)
        
        # Calculate score based on critical thinking indicators
        if thinking_patterns > 0:
            score += 5
        if assumption_challenges > 0:
            score += 3
        if evidence_validation > 0:
            score += 2
        
        self.quality_dimensions["critical_thinking"]["score"] = max(0, min(100, score))
    
    def _assess_process_quality(self, changed_files: List[str], analysis_results: Dict = None):
        """Assess process quality dimension (15% weight)."""
        print("⚙️ Assessing process quality dimension...")
        
        score = self.baseline_score
        
        # Check TDD compliance indicators
        tdd_indicators = self._check_tdd_indicators(changed_files)
        
        # Check quality gate integration
        quality_gate_integration = self._check_quality_gate_integration(changed_files)
        
        # Factor in analysis results if available
        if analysis_results:
            if analysis_results.get("semantic_issues"):
                score -= len(analysis_results["semantic_issues"]) * 2
            if analysis_results.get("dependency_impacts"):
                score -= len(analysis_results["dependency_impacts"]) * 3
        
        self.quality_dimensions["process_quality"]["score"] = max(0, min(100, score))
    
    def _assess_predictive_analytics(self, changed_files: List[str]):
        """Assess predictive analytics dimension (10% weight)."""
        print("🔮 Assessing predictive analytics dimension...")
        
        score = self.baseline_score
        
        # Check for analytics integration
        analytics_integration = self._check_analytics_integration(changed_files)
        
        # Check for meta-framework usage
        meta_framework_usage = self._check_meta_framework_usage(changed_files)
        
        if analytics_integration:
            score += 5
        if meta_framework_usage:
            score += 5
        
        self.quality_dimensions["predictive_analytics"]["score"] = max(0, min(100, score))
    
    def _assess_architectural_fitness(self, changed_files: List[str]):
        """Assess architectural fitness dimension (10% weight)."""
        print("🏗️ Assessing architectural fitness dimension...")
        
        score = self.baseline_score
        
        # Check API design consistency
        api_consistency = self._check_api_consistency(changed_files)
        
        # Check error handling completeness
        error_handling = self._check_error_handling(changed_files)
        
        # Check integration point quality
        integration_quality = self._check_integration_quality(changed_files)
        
        # Weighted score
        score = (api_consistency * 0.4 + error_handling * 0.3 + integration_quality * 0.3)
        
        self.quality_dimensions["architectural_fitness"]["score"] = max(0, min(100, score))
    
    def _assess_file_structure(self, changed_files: List[str]) -> float:
        """Assess file structure quality."""
        score = self.baseline_score
        
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if not full_path.exists():
                score -= 5  # Missing files are problematic
                continue
            
            # Check file naming conventions
            if not self._follows_naming_conventions(file_path):
                score -= 2
            
            # Check proper directory placement
            if not self._proper_directory_placement(file_path):
                score -= 3
        
        return max(0, min(100, score))
    
    def _assess_content_quality(self, changed_files: List[str]) -> float:
        """Assess content quality."""
        score = self.baseline_score
        
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if not full_path.exists():
                continue
            
            content = self._read_file_safely(full_path)
            if not content:
                score -= 5
                continue
            
            # Check for proper XML structure in framework files
            if file_path.endswith('.md') and '<module' in content:
                if not self._valid_xml_structure(content):
                    score -= 5
            
            # Check for proper documentation structure
            if not self._has_proper_documentation(content):
                score -= 3
            
            # Check for version tables
            if not self._has_version_table(content):
                score -= 2
        
        return max(0, min(100, score))
    
    def _assess_consistency(self, changed_files: List[str]) -> float:
        """Assess consistency across files."""
        score = self.baseline_score
        
        # Check naming consistency
        naming_patterns = self._analyze_naming_patterns(changed_files)
        if len(set(naming_patterns)) > 1:
            score -= 5
        
        # Check structure consistency
        structure_patterns = self._analyze_structure_patterns(changed_files)
        if len(set(structure_patterns)) > 2:
            score -= 3
        
        return max(0, min(100, score))
    
    def _assess_command_delegation(self, changed_files: List[str]) -> float:
        """Assess command delegation patterns."""
        score = self.baseline_score
        
        command_files = [f for f in changed_files if ".claude/commands/" in f]
        
        for file_path in command_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content:
                    # Check for proper module delegation
                    if "module =" in content or "delegate" in content.lower():
                        score += 2
                    else:
                        score -= 5
        
        return max(0, min(100, score))
    
    def _assess_module_coupling(self, changed_files: List[str]) -> float:
        """Assess module coupling quality."""
        score = self.baseline_score
        
        module_files = [f for f in changed_files if ".claude/modules/" in f]
        
        for file_path in module_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content:
                    # Check for proper integration points
                    if "integration_points" in content:
                        score += 3
                    if "depends_on" in content and "provides_to" in content:
                        score += 2
        
        return max(0, min(100, score))
    
    def _assess_pattern_reusability(self, changed_files: List[str]) -> float:
        """Assess pattern reusability."""
        score = self.baseline_score
        
        # Check for pattern files
        pattern_files = [f for f in changed_files if ".claude/patterns/" in f or "pattern" in f.lower()]
        
        if pattern_files:
            score += 5  # Bonus for pattern development
        
        return max(0, min(100, score))
    
    def _analyze_thinking_patterns(self, changed_files: List[str]) -> int:
        """Count thinking pattern implementations."""
        count = 0
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content and "thinking_pattern" in content:
                    count += 1
        return count
    
    def _analyze_assumption_challenges(self, changed_files: List[str]) -> int:
        """Count assumption challenge indicators."""
        count = 0
        challenge_keywords = ["challenge", "assumptions", "validate", "verify", "evidence"]
        
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content:
                    for keyword in challenge_keywords:
                        if keyword in content.lower():
                            count += 1
                            break
        return count
    
    def _analyze_evidence_validation(self, changed_files: List[str]) -> int:
        """Count evidence validation indicators."""
        count = 0
        validation_keywords = ["validation", "evidence", "verify", "test", "proof"]
        
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content:
                    for keyword in validation_keywords:
                        if keyword in content.lower():
                            count += 1
                            break
        return count
    
    def _check_tdd_indicators(self, changed_files: List[str]) -> bool:
        """Check for TDD indicators."""
        tdd_keywords = ["red", "green", "refactor", "test", "tdd"]
        
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content:
                    for keyword in tdd_keywords:
                        if keyword in content.lower():
                            return True
        return False
    
    def _check_quality_gate_integration(self, changed_files: List[str]) -> bool:
        """Check for quality gate integration."""
        quality_keywords = ["quality_gates", "quality gate", "validation", "compliance"]
        
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content:
                    for keyword in quality_keywords:
                        if keyword in content.lower():
                            return True
        return False
    
    def _check_analytics_integration(self, changed_files: List[str]) -> bool:
        """Check for analytics integration."""
        analytics_keywords = ["analytics", "metrics", "monitoring", "performance"]
        
        for file_path in changed_files:
            if "analytics" in file_path or "metrics" in file_path:
                return True
            
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content:
                    for keyword in analytics_keywords:
                        if keyword in content.lower():
                            return True
        return False
    
    def _check_meta_framework_usage(self, changed_files: List[str]) -> bool:
        """Check for meta-framework usage."""
        return any(".claude/meta/" in f for f in changed_files)
    
    def _check_api_consistency(self, changed_files: List[str]) -> float:
        """Check API design consistency."""
        score = self.baseline_score
        
        # Check for consistent interface patterns
        interface_patterns = []
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content and "interface_contract" in content:
                    interface_patterns.append(self._extract_interface_pattern(content))
        
        # Consistency bonus/penalty
        if len(set(interface_patterns)) <= 1 and interface_patterns:
            score += 5
        elif len(set(interface_patterns)) > 2:
            score -= 5
        
        return max(0, min(100, score))
    
    def _check_error_handling(self, changed_files: List[str]) -> float:
        """Check error handling completeness."""
        score = self.baseline_score
        
        error_handling_keywords = ["error", "exception", "failure", "rollback", "recovery"]
        
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content:
                    error_handling_found = any(keyword in content.lower() for keyword in error_handling_keywords)
                    if error_handling_found:
                        score += 2
        
        return max(0, min(100, score))
    
    def _check_integration_quality(self, changed_files: List[str]) -> float:
        """Check integration point quality."""
        score = self.baseline_score
        
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content and "integration_points" in content:
                    if "depends_on" in content and "provides_to" in content:
                        score += 5
                    else:
                        score -= 3
        
        return max(0, min(100, score))
    
    def _calculate_overall_score(self) -> float:
        """Calculate weighted overall quality score."""
        total_score = 0
        total_weight = 0
        
        for dimension, data in self.quality_dimensions.items():
            weight = data["weight"]
            score = data["score"]
            total_score += score * weight
            total_weight += weight
        
        return round(total_score / total_weight if total_weight > 0 else 0, 1)
    
    def _get_grade(self, score: float) -> str:
        """Get letter grade based on score."""
        if score >= 95:
            return "A+"
        elif score >= 90:
            return "A"
        elif score >= 85:
            return "B+"
        elif score >= 80:
            return "B"
        elif score >= 75:
            return "C+"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    def _check_compliance(self, score: float) -> Dict:
        """Check compliance with framework standards."""
        return {
            "production_ready": score >= 85,
            "enterprise_ready": score >= 90,
            "critical_systems_ready": score >= 90,
            "requires_improvement": score < 85,
            "requires_major_work": score < 70,
            "deployment_blocked": score < 60
        }
    
    def _identify_risk_factors(self) -> List[str]:
        """Identify quality risk factors."""
        risk_factors = []
        
        for dimension, data in self.quality_dimensions.items():
            if data["score"] < 70:
                risk_factors.append(f"Low {dimension.replace('_', ' ')} score: {data['score']}/100")
        
        return risk_factors
    
    def _suggest_improvements(self) -> List[str]:
        """Suggest specific improvements."""
        improvements = []
        
        for dimension, data in self.quality_dimensions.items():
            if data["score"] < 85:
                if dimension == "code_quality":
                    improvements.append("Improve file structure and documentation quality")
                elif dimension == "framework_effectiveness":
                    improvements.append("Enhance command delegation and module coupling")
                elif dimension == "critical_thinking":
                    improvements.append("Add more thinking patterns and validation steps")
                elif dimension == "process_quality":
                    improvements.append("Integrate with TDD processes and quality gates")
                elif dimension == "predictive_analytics":
                    improvements.append("Add analytics integration and meta-framework usage")
                elif dimension == "architectural_fitness":
                    improvements.append("Improve API consistency and error handling")
        
        return improvements
    
    def _generate_quality_recommendations(self) -> List[str]:
        """Generate quality recommendations."""
        recommendations = []
        overall_score = self._calculate_overall_score()
        
        if overall_score >= 90:
            recommendations.append("✅ Excellent quality! Consider sharing best practices.")
        elif overall_score >= 85:
            recommendations.append("✅ Good quality, ready for production deployment.")
        elif overall_score >= 75:
            recommendations.append("⚠️ Acceptable quality, address weak areas before deployment.")
        elif overall_score >= 70:
            recommendations.append("❌ Below standard, improvement plan required.")
        else:
            recommendations.append("🚫 Poor quality, complete rework needed.")
        
        return recommendations
    
    # Helper methods
    def _read_file_safely(self, file_path: Path) -> Optional[str]:
        """Safely read file content."""
        try:
            return file_path.read_text(encoding='utf-8')
        except Exception:
            return None
    
    def _follows_naming_conventions(self, file_path: str) -> bool:
        """Check if file follows naming conventions."""
        filename = Path(file_path).name
        # Basic check for kebab-case .md files
        return filename.endswith('.md') and re.match(r'^[a-z0-9-]+\.md$', filename)
    
    def _proper_directory_placement(self, file_path: str) -> bool:
        """Check if file is in proper directory."""
        if ".claude/commands/" in file_path:
            return file_path.endswith('.md')
        elif ".claude/modules/" in file_path:
            return file_path.endswith('.md')
        elif ".claude/system/" in file_path:
            return file_path.endswith('.md')
        return True
    
    def _valid_xml_structure(self, content: str) -> bool:
        """Check for valid XML structure."""
        return '<module' in content and '</module>' in content
    
    def _has_proper_documentation(self, content: str) -> bool:
        """Check for proper documentation structure."""
        return bool(content.strip()) and len(content) > 100
    
    def _has_version_table(self, content: str) -> bool:
        """Check for version table."""
        return '| version |' in content or 'last_updated' in content
    
    def _analyze_naming_patterns(self, changed_files: List[str]) -> List[str]:
        """Analyze naming patterns."""
        patterns = []
        for file_path in changed_files:
            filename = Path(file_path).name
            if '-' in filename:
                patterns.append('kebab-case')
            elif '_' in filename:
                patterns.append('snake_case')
            else:
                patterns.append('single-word')
        return patterns
    
    def _analyze_structure_patterns(self, changed_files: List[str]) -> List[str]:
        """Analyze structure patterns."""
        patterns = []
        for file_path in changed_files:
            if ".claude/commands/" in file_path:
                patterns.append('command')
            elif ".claude/modules/" in file_path:
                patterns.append('module')
            else:
                patterns.append('other')
        return patterns
    
    def _extract_interface_pattern(self, content: str) -> str:
        """Extract interface pattern from content."""
        if "interface_contract" in content:
            return "standard"
        else:
            return "none"

def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(description="Assess prompt engineering quality")
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    parser.add_argument("--changed-files", nargs="+", required=True, help="List of changed files")
    parser.add_argument("--analysis-results", help="JSON file with analysis results")
    parser.add_argument("--output", help="Output file for assessment")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    
    args = parser.parse_args()
    
    # Load analysis results if provided
    analysis_results = None
    if args.analysis_results:
        with open(args.analysis_results, 'r') as f:
            analysis_results = json.load(f)
    
    # Perform assessment
    assessor = PromptQualityAssessor(args.repo_root)
    results = assessor.assess_quality(args.changed_files, analysis_results)
    
    if args.json:
        output = json.dumps(results, indent=2)
    else:
        # Generate readable report
        report = []
        report.append("# 📊 Prompt Quality Assessment Report")
        report.append(f"**Overall Score**: {results['overall_score']}/100 ({results['grade']})")
        report.append("")
        
        report.append("## 📈 Dimension Scores")
        for dimension, data in results["dimensions"].items():
            report.append(f"- **{dimension.replace('_', ' ').title()}**: {data['score']}/100 (Weight: {data['weight']*100}%)")
        report.append("")
        
        if results["recommendations"]:
            report.append("## 💡 Recommendations")
            for rec in results["recommendations"]:
                report.append(f"- {rec}")
            report.append("")
        
        if results["improvement_actions"]:
            report.append("## 🔧 Improvement Actions")
            for action in results["improvement_actions"]:
                report.append(f"- {action}")
        
        output = "\n".join(report)
    
    if args.output:
        Path(args.output).write_text(output)
        print(f"📊 Quality assessment written to {args.output}")
    else:
        print(output)
    
    # Exit with appropriate code based on quality score
    if results["overall_score"] >= 85:
        sys.exit(0)  # Success
    elif results["overall_score"] >= 70:
        sys.exit(1)  # Warning
    else:
        sys.exit(2)  # Failure

if __name__ == "__main__":
    main()