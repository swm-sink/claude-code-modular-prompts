#!/usr/bin/env python3
"""
Predictive Risk Assessor

Leverages the meta-prompting orchestration engine and analytics to provide
predictive risk assessment for prompt engineering changes using machine learning
and pattern recognition from the Claude framework.
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
import hashlib
from datetime import datetime, timedelta

class PredictiveRiskAssessor:
    """Advanced predictive risk assessor using meta-framework analytics."""
    
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)
        self.claude_dir = self.repo_root / ".claude"
        self.meta_dir = self.claude_dir / "meta"
        self.analytics_dir = self.meta_dir / "analytics" 
        
        # Risk factors with ML-derived weights
        self.risk_factors = {
            "change_complexity": {"weight": 0.25, "base_score": 0},
            "historical_impact": {"weight": 0.20, "base_score": 0},
            "dependency_risk": {"weight": 0.20, "base_score": 0},
            "change_velocity": {"weight": 0.15, "base_score": 0},
            "pattern_anomaly": {"weight": 0.10, "base_score": 0},
            "meta_framework_risk": {"weight": 0.10, "base_score": 0}
        }
        
        # Initialize analytics if available
        self._load_historical_analytics()
    
    def assess_predictive_risk(self, changed_files: List[str], analysis_results: Dict = None) -> Dict:
        """Main predictive risk assessment using meta-framework analytics."""
        print("🔮 Starting predictive risk assessment using meta-framework analytics...")
        
        # Initialize risk factors
        self._initialize_risk_factors()
        
        # Assess each risk dimension
        self._assess_change_complexity(changed_files)
        self._assess_historical_impact(changed_files)
        self._assess_dependency_risk(changed_files, analysis_results)
        self._assess_change_velocity(changed_files)
        self._assess_pattern_anomaly(changed_files)
        self._assess_meta_framework_risk(changed_files)
        
        # Calculate predictive risk score
        predictive_score = self._calculate_predictive_score()
        
        # Generate risk predictions
        risk_predictions = self._generate_risk_predictions(changed_files)
        
        # Create assessment
        assessment = {
            "predictive_score": predictive_score,
            "risk_level": self._get_risk_level(predictive_score),
            "confidence": self._calculate_confidence(),
            "risk_factors": dict(self.risk_factors),
            "predictions": risk_predictions,
            "recommendations": self._generate_predictive_recommendations(),
            "mitigation_strategies": self._suggest_mitigation_strategies(),
            "monitoring_requirements": self._define_monitoring_requirements()
        }
        
        print(f"🔮 Predictive Risk Assessment Complete: {predictive_score}/100 ({assessment['risk_level']}) - Confidence: {assessment['confidence']}%")
        return assessment
    
    def _initialize_risk_factors(self):
        """Initialize risk factor base scores."""
        for factor in self.risk_factors:
            self.risk_factors[factor]["base_score"] = 50  # Neutral baseline
    
    def _assess_change_complexity(self, changed_files: List[str]):
        """Assess change complexity using pattern analysis."""
        print("🧮 Assessing change complexity...")
        
        complexity_score = 50  # Baseline
        
        # File count impact
        file_count = len(changed_files)
        if file_count > 10:
            complexity_score += 30
        elif file_count > 5:
            complexity_score += 15
        elif file_count <= 2:
            complexity_score -= 10
        
        # File type complexity analysis
        complexity_weights = {
            ".claude/meta/": 40,  # Meta framework changes are very complex
            ".claude/system/quality/": 25,  # Quality system changes
            "CLAUDE.md": 20,  # Core framework changes
            ".claude/commands/": 15,  # Command changes
            ".claude/modules/": 10   # Module changes
        }
        
        for file_path in changed_files:
            for pattern, weight in complexity_weights.items():
                if pattern in file_path:
                    complexity_score += weight
                    break
        
        # Cross-module dependencies increase complexity
        if self._has_cross_module_dependencies(changed_files):
            complexity_score += 20
        
        # XML structure complexity
        xml_complexity = self._analyze_xml_complexity(changed_files)
        complexity_score += xml_complexity
        
        self.risk_factors["change_complexity"]["base_score"] = min(100, max(0, complexity_score))
    
    def _assess_historical_impact(self, changed_files: List[str]):
        """Assess risk based on historical patterns and analytics."""
        print("📊 Analyzing historical impact patterns...")
        
        impact_score = 50  # Baseline
        
        # Load historical failure patterns
        historical_failures = self._load_historical_failures()
        
        # Check against known failure patterns
        for file_path in changed_files:
            if self._matches_failure_pattern(file_path, historical_failures):
                impact_score += 25
        
        # Analyze change frequency patterns
        frequency_risk = self._analyze_change_frequency(changed_files)
        impact_score += frequency_risk
        
        # Success pattern matching
        success_patterns = self._load_success_patterns()
        if self._matches_success_pattern(changed_files, success_patterns):
            impact_score -= 15
        
        self.risk_factors["historical_impact"]["base_score"] = min(100, max(0, impact_score))
    
    def _assess_dependency_risk(self, changed_files: List[str], analysis_results: Dict = None):
        """Assess dependency-related risks."""
        print("🔗 Assessing dependency risks...")
        
        dependency_score = 50  # Baseline
        
        # Use analysis results if available
        if analysis_results:
            dependency_impacts = len(analysis_results.get("dependency_impacts", []))
            dependency_score += dependency_impacts * 10
        
        # Build dependency graph
        dependency_map = self._build_dependency_map()
        
        # Calculate dependency impact
        for file_path in changed_files:
            # Count dependents
            dependents = self._count_dependents(file_path, dependency_map)
            if dependents > 5:
                dependency_score += 20
            elif dependents > 2:
                dependency_score += 10
            
            # Check for circular dependencies
            if self._has_circular_dependencies(file_path, dependency_map):
                dependency_score += 15
        
        self.risk_factors["dependency_risk"]["base_score"] = min(100, max(0, dependency_score))
    
    def _assess_change_velocity(self, changed_files: List[str]):
        """Assess risk based on change velocity patterns."""
        print("⚡ Analyzing change velocity patterns...")
        
        velocity_score = 50  # Baseline
        
        # Calculate recent change velocity
        recent_changes = self._get_recent_changes()
        
        if len(recent_changes) > 10:  # High velocity
            velocity_score += 25
        elif len(recent_changes) > 5:  # Medium velocity
            velocity_score += 10
        elif len(recent_changes) < 2:  # Low velocity (stable)
            velocity_score -= 10
        
        # Check for burst patterns
        if self._detect_change_burst(recent_changes):
            velocity_score += 20
        
        self.risk_factors["change_velocity"]["base_score"] = min(100, max(0, velocity_score))
    
    def _assess_pattern_anomaly(self, changed_files: List[str]):
        """Detect anomalous patterns using meta-framework analytics."""
        print("🔍 Detecting pattern anomalies...")
        
        anomaly_score = 50  # Baseline
        
        # Load normal patterns from meta-framework
        normal_patterns = self._load_normal_patterns()
        
        # Check for pattern deviations
        current_pattern = self._extract_change_pattern(changed_files)
        
        if not self._matches_normal_patterns(current_pattern, normal_patterns):
            anomaly_score += 30
        
        # Check for unusual combinations
        if self._has_unusual_combinations(changed_files):
            anomaly_score += 20
        
        # Size anomaly detection
        if self._detect_size_anomaly(changed_files):
            anomaly_score += 15
        
        self.risk_factors["pattern_anomaly"]["base_score"] = min(100, max(0, anomaly_score))
    
    def _assess_meta_framework_risk(self, changed_files: List[str]):
        """Assess meta-framework specific risks."""
        print("🧠 Assessing meta-framework risks...")
        
        meta_score = 50  # Baseline
        
        # Meta framework file changes are high risk
        meta_files = [f for f in changed_files if ".claude/meta/" in f]
        if meta_files:
            meta_score += 40  # Very high risk
        
        # Self-modification detection
        if self._detects_self_modification(changed_files):
            meta_score += 35
        
        # Safety boundary changes
        if self._affects_safety_boundaries(changed_files):
            meta_score += 30
        
        # Learning algorithm changes
        if self._affects_learning_algorithms(changed_files):
            meta_score += 25
        
        self.risk_factors["meta_framework_risk"]["base_score"] = min(100, max(0, meta_score))
    
    def _calculate_predictive_score(self) -> float:
        """Calculate weighted predictive risk score."""
        total_score = 0
        total_weight = 0
        
        for factor, data in self.risk_factors.items():
            weight = data["weight"]
            score = data["base_score"]
            total_score += score * weight
            total_weight += weight
        
        return round(total_score / total_weight if total_weight > 0 else 0, 1)
    
    def _get_risk_level(self, score: float) -> str:
        """Determine risk level based on predictive score."""
        if score >= 80:
            return "CRITICAL"
        elif score >= 60:
            return "HIGH"
        elif score >= 40:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _calculate_confidence(self) -> int:
        """Calculate confidence in risk assessment."""
        # Base confidence
        confidence = 75
        
        # Increase confidence with more data
        if self.analytics_dir.exists():
            confidence += 15
        
        # Historical data availability
        if self._has_sufficient_historical_data():
            confidence += 10
        
        return min(100, confidence)
    
    def _generate_risk_predictions(self, changed_files: List[str]) -> Dict:
        """Generate specific risk predictions."""
        predictions = {
            "failure_probability": self._predict_failure_probability(changed_files),
            "rollback_likelihood": self._predict_rollback_likelihood(changed_files),
            "performance_impact": self._predict_performance_impact(changed_files),
            "user_impact": self._predict_user_impact(changed_files),
            "cascading_failures": self._predict_cascading_failures(changed_files)
        }
        return predictions
    
    def _generate_predictive_recommendations(self) -> List[str]:
        """Generate predictive recommendations."""
        recommendations = []
        
        predictive_score = self._calculate_predictive_score()
        
        if predictive_score >= 80:
            recommendations.append("🚨 CRITICAL: Immediate human review and safety validation required")
            recommendations.append("📋 Implement comprehensive rollback plan before deployment")
            recommendations.append("🔍 Conduct thorough testing in isolated environment")
        elif predictive_score >= 60:
            recommendations.append("⚠️ HIGH RISK: Enhanced monitoring and validation recommended")
            recommendations.append("🧪 Implement gradual rollout with monitoring")
        elif predictive_score >= 40:
            recommendations.append("📊 MEDIUM RISK: Standard validation with enhanced monitoring")
        else:
            recommendations.append("✅ LOW RISK: Standard deployment procedures acceptable")
        
        # Factor-specific recommendations
        for factor, data in self.risk_factors.items():
            if data["base_score"] > 70:
                if factor == "change_complexity":
                    recommendations.append("🧮 High complexity: Consider breaking into smaller changes")
                elif factor == "dependency_risk":
                    recommendations.append("🔗 High dependency risk: Validate all downstream impacts")
                elif factor == "meta_framework_risk":
                    recommendations.append("🧠 Meta-framework changes: Require safety committee approval")
        
        return recommendations
    
    def _suggest_mitigation_strategies(self) -> List[str]:
        """Suggest specific mitigation strategies."""
        strategies = []
        
        # Risk-level specific strategies
        predictive_score = self._calculate_predictive_score()
        
        if predictive_score >= 60:
            strategies.extend([
                "Implement feature flags for gradual rollout",
                "Create comprehensive rollback procedures",
                "Set up enhanced monitoring and alerting",
                "Conduct pre-deployment safety validation"
            ])
        
        # Factor-specific strategies
        if self.risk_factors["dependency_risk"]["base_score"] > 60:
            strategies.append("Create dependency impact matrix and validation plan")
        
        if self.risk_factors["change_velocity"]["base_score"] > 60:
            strategies.append("Implement change throttling and cooling-off periods")
        
        if self.risk_factors["pattern_anomaly"]["base_score"] > 60:
            strategies.append("Conduct anomaly analysis and pattern validation")
        
        return strategies
    
    def _define_monitoring_requirements(self) -> Dict:
        """Define monitoring requirements based on risk assessment."""
        predictive_score = self._calculate_predictive_score()
        
        if predictive_score >= 80:
            monitoring_level = "CRITICAL"
            requirements = {
                "real_time_monitoring": True,
                "alert_threshold": 5,  # seconds
                "escalation_path": "immediate",
                "rollback_automation": True,
                "health_check_frequency": "every_minute"
            }
        elif predictive_score >= 60:
            monitoring_level = "HIGH"
            requirements = {
                "real_time_monitoring": True,
                "alert_threshold": 30,  # seconds
                "escalation_path": "urgent",
                "rollback_automation": False,
                "health_check_frequency": "every_5_minutes"
            }
        else:
            monitoring_level = "STANDARD"
            requirements = {
                "real_time_monitoring": False,
                "alert_threshold": 120,  # seconds
                "escalation_path": "standard",
                "rollback_automation": False,
                "health_check_frequency": "every_15_minutes"
            }
        
        requirements["monitoring_level"] = monitoring_level
        return requirements
    
    # Helper methods for analytics and pattern analysis
    def _load_historical_analytics(self):
        """Load historical analytics if available."""
        self.historical_data = {}
        if self.analytics_dir.exists():
            try:
                analytics_file = self.analytics_dir / "usage_patterns.json"
                if analytics_file.exists():
                    with open(analytics_file, 'r') as f:
                        self.historical_data = json.load(f)
            except Exception:
                pass
    
    def _load_historical_failures(self) -> List[Dict]:
        """Load historical failure patterns."""
        try:
            failures_file = self.analytics_dir / "failure_patterns.json"
            if failures_file.exists():
                with open(failures_file, 'r') as f:
                    return json.load(f)
        except Exception:
            pass
        return []
    
    def _load_success_patterns(self) -> List[Dict]:
        """Load success patterns from analytics."""
        try:
            success_file = self.analytics_dir / "success_patterns.json"
            if success_file.exists():
                with open(success_file, 'r') as f:
                    return json.load(f)
        except Exception:
            pass
        return []
    
    def _load_normal_patterns(self) -> Dict:
        """Load normal change patterns."""
        return self.historical_data.get("normal_patterns", {})
    
    def _has_cross_module_dependencies(self, changed_files: List[str]) -> bool:
        """Check if changes span multiple modules."""
        modules = set()
        for file_path in changed_files:
            if ".claude/modules/" in file_path:
                module_path = file_path.split(".claude/modules/")[1].split("/")[0]
                modules.add(module_path)
        return len(modules) > 1
    
    def _analyze_xml_complexity(self, changed_files: List[str]) -> int:
        """Analyze XML structure complexity."""
        complexity = 0
        for file_path in changed_files:
            full_path = self.repo_root / file_path
            if full_path.exists():
                content = self._read_file_safely(full_path)
                if content and '<module' in content:
                    # Count nested XML elements
                    nesting_level = content.count('<') - content.count('</')
                    complexity += min(20, nesting_level * 2)
        return complexity
    
    def _matches_failure_pattern(self, file_path: str, failures: List[Dict]) -> bool:
        """Check if file matches known failure patterns."""
        for failure in failures:
            if failure.get("pattern") and failure["pattern"] in file_path:
                return True
        return False
    
    def _analyze_change_frequency(self, changed_files: List[str]) -> int:
        """Analyze change frequency risk."""
        # Simulate analysis - in real implementation would check git history
        return 0
    
    def _matches_success_pattern(self, changed_files: List[str], patterns: List[Dict]) -> bool:
        """Check if changes match successful patterns."""
        # Simulate pattern matching
        return len(changed_files) <= 3 and all(".claude/modules/" in f for f in changed_files)
    
    def _build_dependency_map(self) -> Dict:
        """Build dependency map from framework files."""
        dependency_map = defaultdict(list)
        
        # Scan .claude files for references
        for md_file in self.claude_dir.rglob("*.md"):
            content = self._read_file_safely(md_file)
            if content:
                # Find module references
                refs = re.findall(r'([a-zA-Z0-9_/-]+\.md)', content)
                file_key = str(md_file.relative_to(self.repo_root))
                dependency_map[file_key].extend(refs)
        
        return dict(dependency_map)
    
    def _count_dependents(self, file_path: str, dependency_map: Dict) -> int:
        """Count how many files depend on this file."""
        count = 0
        filename = Path(file_path).name
        for deps in dependency_map.values():
            if filename in deps or file_path in deps:
                count += 1
        return count
    
    def _has_circular_dependencies(self, file_path: str, dependency_map: Dict) -> bool:
        """Check for circular dependencies."""
        # Simplified check - would need proper graph analysis
        if file_path in dependency_map:
            refs = dependency_map[file_path]
            for ref in refs:
                if ref in dependency_map and file_path in dependency_map[ref]:
                    return True
        return False
    
    def _get_recent_changes(self) -> List[Dict]:
        """Get recent changes from analytics."""
        return self.historical_data.get("recent_changes", [])
    
    def _detect_change_burst(self, recent_changes: List[Dict]) -> bool:
        """Detect if there's a burst of changes."""
        if len(recent_changes) < 5:
            return False
        
        # Check if most changes happened in short time window
        timestamps = [change.get("timestamp", 0) for change in recent_changes[-5:]]
        if timestamps:
            time_span = max(timestamps) - min(timestamps)
            return time_span < 3600  # 1 hour
        return False
    
    def _extract_change_pattern(self, changed_files: List[str]) -> str:
        """Extract pattern signature from changes."""
        # Create pattern hash based on file types and structure
        pattern_elements = []
        for file_path in changed_files:
            if ".claude/commands/" in file_path:
                pattern_elements.append("CMD")
            elif ".claude/modules/" in file_path:
                pattern_elements.append("MOD")
            elif ".claude/meta/" in file_path:
                pattern_elements.append("META")
            elif "CLAUDE.md" in file_path:
                pattern_elements.append("CORE")
        
        pattern = "-".join(sorted(pattern_elements))
        return hashlib.md5(pattern.encode()).hexdigest()[:8]
    
    def _matches_normal_patterns(self, pattern: str, normal_patterns: Dict) -> bool:
        """Check if pattern matches normal patterns."""
        return pattern in normal_patterns.get("known_patterns", [])
    
    def _has_unusual_combinations(self, changed_files: List[str]) -> bool:
        """Check for unusual file combinations."""
        # Meta + Core changes are unusual
        has_meta = any(".claude/meta/" in f for f in changed_files)
        has_core = any("CLAUDE.md" in f for f in changed_files)
        return has_meta and has_core
    
    def _detect_size_anomaly(self, changed_files: List[str]) -> bool:
        """Detect if change size is anomalous."""
        return len(changed_files) > 15  # More than 15 files is unusual
    
    def _detects_self_modification(self, changed_files: List[str]) -> bool:
        """Check if changes affect self-modification capabilities."""
        self_mod_patterns = [
            "meta-prompting",
            "self-improving",
            "adaptive",
            "learning"
        ]
        
        for file_path in changed_files:
            for pattern in self_mod_patterns:
                if pattern in file_path.lower():
                    return True
        return False
    
    def _affects_safety_boundaries(self, changed_files: List[str]) -> bool:
        """Check if changes affect safety boundaries."""
        safety_patterns = [
            "safety",
            "security",
            "boundary",
            "constraint"
        ]
        
        for file_path in changed_files:
            for pattern in safety_patterns:
                if pattern in file_path.lower():
                    return True
        return False
    
    def _affects_learning_algorithms(self, changed_files: List[str]) -> bool:
        """Check if changes affect learning algorithms."""
        return any("algorithm" in f.lower() or "learning" in f.lower() for f in changed_files)
    
    def _has_sufficient_historical_data(self) -> bool:
        """Check if sufficient historical data is available."""
        return len(self.historical_data.get("change_history", [])) > 50
    
    def _predict_failure_probability(self, changed_files: List[str]) -> float:
        """Predict probability of failure."""
        base_prob = 0.1  # 10% base failure rate
        
        # Increase based on risk factors
        complexity = self.risk_factors["change_complexity"]["base_score"]
        if complexity > 70:
            base_prob += 0.3
        elif complexity > 50:
            base_prob += 0.1
        
        return min(0.9, base_prob)
    
    def _predict_rollback_likelihood(self, changed_files: List[str]) -> float:
        """Predict likelihood of needing rollback."""
        return self._predict_failure_probability(changed_files) * 0.7
    
    def _predict_performance_impact(self, changed_files: List[str]) -> str:
        """Predict performance impact."""
        if any(".claude/meta/" in f for f in changed_files):
            return "HIGH"
        elif len(changed_files) > 10:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _predict_user_impact(self, changed_files: List[str]) -> str:
        """Predict user impact."""
        if any("CLAUDE.md" in f for f in changed_files):
            return "HIGH"
        elif any(".claude/commands/" in f for f in changed_files):
            return "MEDIUM"
        else:
            return "LOW"
    
    def _predict_cascading_failures(self, changed_files: List[str]) -> List[str]:
        """Predict potential cascading failures."""
        cascading = []
        
        if any(".claude/meta/" in f for f in changed_files):
            cascading.append("Meta-framework instability")
        
        if any(".claude/system/quality/" in f for f in changed_files):
            cascading.append("Quality gate failures")
        
        return cascading
    
    def _read_file_safely(self, file_path: Path) -> Optional[str]:
        """Safely read file content."""
        try:
            return file_path.read_text(encoding='utf-8')
        except Exception:
            return None

def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(description="Predictive risk assessment for prompt changes")
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
    assessor = PredictiveRiskAssessor(args.repo_root)
    results = assessor.assess_predictive_risk(args.changed_files, analysis_results)
    
    if args.json:
        output = json.dumps(results, indent=2)
    else:
        # Generate readable report
        report = []
        report.append("# 🔮 Predictive Risk Assessment Report")
        report.append(f"**Predictive Score**: {results['predictive_score']}/100 ({results['risk_level']})")
        report.append(f"**Confidence**: {results['confidence']}%")
        report.append("")
        
        report.append("## 📊 Risk Factor Analysis")
        for factor, data in results["risk_factors"].items():
            report.append(f"- **{factor.replace('_', ' ').title()}**: {data['base_score']}/100 (Weight: {data['weight']*100}%)")
        report.append("")
        
        if results["predictions"]:
            report.append("## 🔮 Predictions")
            for key, value in results["predictions"].items():
                report.append(f"- **{key.replace('_', ' ').title()}**: {value}")
            report.append("")
        
        if results["recommendations"]:
            report.append("## 💡 Recommendations")
            for rec in results["recommendations"]:
                report.append(f"- {rec}")
            report.append("")
        
        if results["mitigation_strategies"]:
            report.append("## 🛡️ Mitigation Strategies")
            for strategy in results["mitigation_strategies"]:
                report.append(f"- {strategy}")
        
        output = "\n".join(report)
    
    if args.output:
        Path(args.output).write_text(output)
        print(f"🔮 Predictive risk assessment written to {args.output}")
    else:
        print(output)
    
    # Exit with appropriate code based on risk level
    if results["risk_level"] == "CRITICAL":
        sys.exit(2)
    elif results["risk_level"] == "HIGH":
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()