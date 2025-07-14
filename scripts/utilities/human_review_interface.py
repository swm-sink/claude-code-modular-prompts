#!/usr/bin/env python3
"""
Human Review Interface

Creates an interactive interface for human reviewers to make informed decisions
about prompt engineering changes. Provides visual impact assessment, risk
analysis, and guided decision-making tools.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import subprocess
from datetime import datetime

class HumanReviewInterface:
    """Interactive interface for human prompt engineering review."""
    
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)
        self.claude_dir = self.repo_root / ".claude"
        
        # Review decision templates
        self.decision_templates = {
            "approve": {
                "action": "APPROVE",
                "color": "🟢",
                "follow_up": ["standard_monitoring", "documentation_update"]
            },
            "approve_with_conditions": {
                "action": "APPROVE_WITH_CONDITIONS", 
                "color": "🟡",
                "follow_up": ["enhanced_monitoring", "staged_rollout", "documentation_update"]
            },
            "request_changes": {
                "action": "REQUEST_CHANGES",
                "color": "🔴", 
                "follow_up": ["detailed_feedback", "improvement_plan", "re_review"]
            },
            "defer_to_committee": {
                "action": "DEFER_TO_COMMITTEE",
                "color": "🔵",
                "follow_up": ["committee_review", "expert_consultation", "safety_analysis"]
            }
        }
    
    def create_review_interface(self, 
                               risk_assessment: Dict,
                               quality_assessment: Dict,
                               change_analysis: Dict,
                               escalation_info: Dict,
                               changed_files: List[str]) -> Dict:
        """Create comprehensive human review interface."""
        print("👥 Creating human review interface with visual impact assessment...")
        
        # Generate visual impact assessment
        visual_assessment = self._create_visual_assessment(
            risk_assessment, quality_assessment, change_analysis
        )
        
        # Create decision guidance
        decision_guidance = self._create_decision_guidance(
            risk_assessment, quality_assessment, escalation_info
        )
        
        # Generate risk visualization
        risk_visualization = self._create_risk_visualization(risk_assessment)
        
        # Create quality dashboard
        quality_dashboard = self._create_quality_dashboard(quality_assessment)
        
        # Generate change impact analysis
        change_impact = self._create_change_impact_analysis(change_analysis, changed_files)
        
        # Create review checklist
        review_checklist = self._create_review_checklist(escalation_info)
        
        # Generate recommendations
        ai_recommendations = self._generate_ai_recommendations(
            risk_assessment, quality_assessment, change_analysis
        )
        
        # Create interface
        interface = {
            "review_metadata": {
                "timestamp": datetime.utcnow().isoformat(),
                "escalation_level": escalation_info.get("escalation_level", "unknown"),
                "requires_immediate_attention": escalation_info.get("escalation_level") == "critical_risk",
                "estimated_review_time": self._estimate_review_time(escalation_info),
                "expertise_required": self._get_required_expertise(change_analysis)
            },
            "visual_assessment": visual_assessment,
            "decision_guidance": decision_guidance,
            "risk_visualization": risk_visualization,
            "quality_dashboard": quality_dashboard,
            "change_impact": change_impact,
            "review_checklist": review_checklist,
            "ai_recommendations": ai_recommendations,
            "decision_templates": self.decision_templates,
            "supporting_data": {
                "raw_risk_assessment": risk_assessment,
                "raw_quality_assessment": quality_assessment,
                "raw_change_analysis": change_analysis,
                "escalation_details": escalation_info
            }
        }
        
        print("👥 Human review interface created successfully")
        return interface
    
    def _create_visual_assessment(self, risk_assessment: Dict, quality_assessment: Dict, change_analysis: Dict) -> Dict:
        """Create visual impact assessment with charts and indicators."""
        
        # Risk score visualization
        risk_score = risk_assessment.get("predictive_score", 0)
        risk_visual = {
            "score": risk_score,
            "level": risk_assessment.get("risk_level", "UNKNOWN"),
            "bar_chart": self._create_score_bar(risk_score, "Risk"),
            "color_code": self._get_risk_color(risk_score),
            "trend_indicator": self._get_trend_indicator(risk_assessment)
        }
        
        # Quality score visualization  
        quality_score = quality_assessment.get("overall_score", 0)
        quality_visual = {
            "score": quality_score,
            "grade": quality_assessment.get("grade", "Unknown"),
            "bar_chart": self._create_score_bar(quality_score, "Quality"),
            "color_code": self._get_quality_color(quality_score),
            "dimension_breakdown": self._create_dimension_chart(quality_assessment)
        }
        
        # Change complexity visualization
        change_complexity = self._calculate_change_complexity(change_analysis)
        complexity_visual = {
            "score": change_complexity,
            "level": self._get_complexity_level(change_complexity),
            "bar_chart": self._create_score_bar(change_complexity, "Complexity"),
            "color_code": self._get_complexity_color(change_complexity)
        }
        
        # Overall health indicator
        overall_health = self._calculate_overall_health(risk_score, quality_score, change_complexity)
        health_visual = {
            "status": overall_health["status"],
            "color": overall_health["color"],
            "icon": overall_health["icon"],
            "summary": overall_health["summary"]
        }
        
        return {
            "risk_visualization": risk_visual,
            "quality_visualization": quality_visual,
            "complexity_visualization": complexity_visual,
            "overall_health": health_visual,
            "dashboard_summary": self._create_dashboard_summary(risk_score, quality_score, change_complexity)
        }
    
    def _create_decision_guidance(self, risk_assessment: Dict, quality_assessment: Dict, escalation_info: Dict) -> Dict:
        """Create decision guidance for human reviewers."""
        
        risk_score = risk_assessment.get("predictive_score", 0)
        quality_score = quality_assessment.get("overall_score", 0)
        production_ready = quality_assessment.get("compliance", {}).get("production_ready", False)
        escalation_level = escalation_info.get("escalation_level", "unknown")
        
        # Determine recommended action
        if escalation_level == "critical_risk":
            recommended_action = "defer_to_committee"
            rationale = "Critical risk level requires committee review for safety"
        elif not production_ready:
            recommended_action = "request_changes"
            rationale = "Below 85% quality threshold - not production ready"
        elif risk_score >= 60:
            recommended_action = "approve_with_conditions"
            rationale = "High risk requires enhanced monitoring and staged rollout"
        elif quality_score >= 90 and risk_score < 30:
            recommended_action = "approve"
            rationale = "High quality and low risk - standard deployment acceptable"
        else:
            recommended_action = "approve_with_conditions"
            rationale = "Moderate risk/quality - enhanced monitoring recommended"
        
        # Create decision matrix
        decision_matrix = self._create_decision_matrix(risk_score, quality_score, production_ready)
        
        # Generate considerations
        key_considerations = self._generate_key_considerations(risk_assessment, quality_assessment, escalation_info)
        
        # Create risk-benefit analysis
        risk_benefit = self._create_risk_benefit_analysis(risk_assessment, quality_assessment)
        
        return {
            "recommended_action": recommended_action,
            "recommendation_rationale": rationale,
            "confidence_level": self._calculate_recommendation_confidence(risk_assessment, quality_assessment),
            "decision_matrix": decision_matrix,
            "key_considerations": key_considerations,
            "risk_benefit_analysis": risk_benefit,
            "alternative_actions": self._get_alternative_actions(recommended_action),
            "precedent_cases": self._find_precedent_cases(risk_score, quality_score)
        }
    
    def _create_risk_visualization(self, risk_assessment: Dict) -> Dict:
        """Create detailed risk visualization."""
        
        risk_factors = risk_assessment.get("risk_factors", {})
        
        # Factor breakdown chart
        factor_chart = []
        for factor, data in risk_factors.items():
            factor_chart.append({
                "name": factor.replace("_", " ").title(),
                "score": data.get("base_score", 0),
                "weight": data.get("weight", 0) * 100,
                "impact": data.get("base_score", 0) * data.get("weight", 0),
                "bar": self._create_mini_bar(data.get("base_score", 0))
            })
        
        # Risk timeline
        risk_timeline = {
            "immediate": risk_assessment.get("predictions", {}).get("failure_probability", 0) * 100,
            "short_term": min(100, risk_assessment.get("predictive_score", 0) * 1.2),
            "long_term": max(0, risk_assessment.get("predictive_score", 0) * 0.8)
        }
        
        # Mitigation impact
        mitigation_strategies = risk_assessment.get("mitigation_strategies", [])
        mitigation_impact = {
            "available_strategies": len(mitigation_strategies),
            "estimated_risk_reduction": min(50, len(mitigation_strategies) * 10),
            "implementation_complexity": self._assess_mitigation_complexity(mitigation_strategies)
        }
        
        return {
            "factor_breakdown": factor_chart,
            "risk_timeline": risk_timeline,
            "mitigation_impact": mitigation_impact,
            "predictions": risk_assessment.get("predictions", {}),
            "confidence": risk_assessment.get("confidence", 0)
        }
    
    def _create_quality_dashboard(self, quality_assessment: Dict) -> Dict:
        """Create comprehensive quality dashboard."""
        
        dimensions = quality_assessment.get("dimensions", {})
        
        # Dimension scores with visualizations
        dimension_scores = []
        for dimension, data in dimensions.items():
            dimension_scores.append({
                "name": dimension.replace("_", " ").title(),
                "score": data.get("score", 0),
                "weight": data.get("weight", 0) * 100,
                "status": self._get_dimension_status(data.get("score", 0)),
                "bar": self._create_mini_bar(data.get("score", 0)),
                "improvement_potential": max(0, 100 - data.get("score", 0))
            })
        
        # Compliance matrix
        compliance = quality_assessment.get("compliance", {})
        compliance_matrix = []
        for key, value in compliance.items():
            compliance_matrix.append({
                "requirement": key.replace("_", " ").title(),
                "status": "✅ Met" if value else "❌ Not Met",
                "critical": key in ["production_ready", "enterprise_ready"]
            })
        
        # Quality trends (simulated)
        quality_trends = {
            "current_score": quality_assessment.get("overall_score", 0),
            "trend_direction": "stable",  # Would be calculated from historical data
            "improvement_areas": quality_assessment.get("improvement_actions", [])
        }
        
        return {
            "dimension_scores": dimension_scores,
            "compliance_matrix": compliance_matrix,
            "quality_trends": quality_trends,
            "overall_grade": quality_assessment.get("grade", "Unknown"),
            "recommendations": quality_assessment.get("recommendations", [])
        }
    
    def _create_change_impact_analysis(self, change_analysis: Dict, changed_files: List[str]) -> Dict:
        """Create detailed change impact analysis."""
        
        # File impact categorization
        file_impacts = []
        for file_path in changed_files:
            impact = {
                "file": file_path,
                "category": self._categorize_file(file_path),
                "risk_level": self._assess_file_risk(file_path),
                "dependencies": self._count_file_dependencies(file_path),
                "criticality": self._assess_file_criticality(file_path)
            }
            file_impacts.append(impact)
        
        # Dependency analysis
        dependency_analysis = {
            "total_dependencies": len(change_analysis.get("dependency_impacts", [])),
            "critical_dependencies": len([d for d in change_analysis.get("dependency_impacts", []) if d.get("severity") == "HIGH"]),
            "dependency_graph": self._create_dependency_graph_summary(change_analysis)
        }
        
        # Security impact
        security_analysis = {
            "security_implications": len(change_analysis.get("security_implications", [])),
            "threat_level": self._assess_threat_level(change_analysis),
            "affected_security_controls": self._get_affected_security_controls(change_analysis)
        }
        
        # Performance impact prediction
        performance_impact = {
            "predicted_impact": "LOW",  # Would use ML model
            "affected_components": self._get_affected_components(changed_files),
            "resource_usage_change": "minimal"
        }
        
        return {
            "file_impacts": file_impacts,
            "dependency_analysis": dependency_analysis,
            "security_analysis": security_analysis,
            "performance_impact": performance_impact,
            "rollback_complexity": self._assess_rollback_complexity(changed_files),
            "testing_requirements": self._generate_testing_requirements(change_analysis)
        }
    
    def _create_review_checklist(self, escalation_info: Dict) -> Dict:
        """Create dynamic review checklist based on escalation level."""
        
        escalation_level = escalation_info.get("escalation_level", "low_risk")
        
        # Base checklist items
        base_checklist = [
            {"item": "Review change documentation and rationale", "required": True, "checked": False},
            {"item": "Assess quality scores and compliance status", "required": True, "checked": False},
            {"item": "Review risk assessment and mitigation strategies", "required": True, "checked": False},
            {"item": "Validate testing coverage and approach", "required": True, "checked": False}
        ]
        
        # Add escalation-specific items
        if escalation_level in ["high_risk", "critical_risk"]:
            base_checklist.extend([
                {"item": "Review security implications and threat model", "required": True, "checked": False},
                {"item": "Validate rollback procedures and safety measures", "required": True, "checked": False},
                {"item": "Assess impact on dependent systems", "required": True, "checked": False}
            ])
        
        if escalation_level == "critical_risk":
            base_checklist.extend([
                {"item": "Consult with security team", "required": True, "checked": False},
                {"item": "Review with architecture committee", "required": True, "checked": False},
                {"item": "Validate emergency procedures", "required": True, "checked": False},
                {"item": "Approve enhanced monitoring plan", "required": True, "checked": False}
            ])
        
        # Expertise-specific items
        expertise_items = self._get_expertise_checklist_items(escalation_info)
        base_checklist.extend(expertise_items)
        
        return {
            "checklist_items": base_checklist,
            "completion_requirements": {
                "required_items": len([item for item in base_checklist if item["required"]]),
                "optional_items": len([item for item in base_checklist if not item["required"]]),
                "estimated_time": self._estimate_checklist_time(base_checklist)
            },
            "escalation_specific": escalation_level != "low_risk"
        }
    
    def _generate_ai_recommendations(self, risk_assessment: Dict, quality_assessment: Dict, change_analysis: Dict) -> Dict:
        """Generate AI-powered recommendations for review decision."""
        
        # Analyze patterns and generate recommendations
        recommendations = {
            "primary_recommendation": self._get_primary_ai_recommendation(risk_assessment, quality_assessment),
            "confidence": self._calculate_ai_confidence(risk_assessment, quality_assessment),
            "reasoning": self._generate_ai_reasoning(risk_assessment, quality_assessment, change_analysis),
            "alternative_options": self._get_ai_alternatives(risk_assessment, quality_assessment),
            "risk_mitigation_suggestions": risk_assessment.get("mitigation_strategies", []),
            "quality_improvement_suggestions": quality_assessment.get("improvement_actions", []),
            "monitoring_recommendations": self._generate_monitoring_recommendations(risk_assessment)
        }
        
        # Add contextual insights
        recommendations["contextual_insights"] = [
            f"Quality score of {quality_assessment.get('overall_score', 0)}/100 is {'above' if quality_assessment.get('overall_score', 0) >= 85 else 'below'} production threshold",
            f"Risk level is {risk_assessment.get('risk_level', 'unknown')} with {risk_assessment.get('confidence', 0)}% confidence",
            f"Change affects {len(change_analysis.get('change_categories', {}))} different framework areas"
        ]
        
        return recommendations
    
    # Helper methods for visualizations and analysis
    def _create_score_bar(self, score: float, label: str) -> str:
        """Create ASCII bar chart for score."""
        filled = int(score / 5)  # 20 chars max
        empty = 20 - filled
        bar = "█" * filled + "░" * empty
        return f"{label}: [{bar}] {score}/100"
    
    def _create_mini_bar(self, score: float) -> str:
        """Create mini ASCII bar for small displays."""
        filled = int(score / 10)  # 10 chars max
        empty = 10 - filled
        return "█" * filled + "░" * empty
    
    def _get_risk_color(self, score: float) -> str:
        """Get color code for risk score."""
        if score >= 80:
            return "🔴 Critical"
        elif score >= 60:
            return "🟠 High"
        elif score >= 40:
            return "🟡 Medium"
        else:
            return "🟢 Low"
    
    def _get_quality_color(self, score: float) -> str:
        """Get color code for quality score."""
        if score >= 90:
            return "🟢 Excellent"
        elif score >= 85:
            return "🟡 Good"
        elif score >= 70:
            return "🟠 Acceptable"
        else:
            return "🔴 Poor"
    
    def _get_complexity_color(self, score: float) -> str:
        """Get color code for complexity score."""
        if score >= 80:
            return "🔴 Very High"
        elif score >= 60:
            return "🟠 High"
        elif score >= 40:
            return "🟡 Medium"
        else:
            return "🟢 Low"
    
    def _calculate_change_complexity(self, change_analysis: Dict) -> float:
        """Calculate overall change complexity score."""
        base_complexity = 30
        
        # Add complexity based on various factors
        security_implications = len(change_analysis.get("security_implications", []))
        dependency_impacts = len(change_analysis.get("dependency_impacts", []))
        semantic_issues = len(change_analysis.get("semantic_issues", []))
        
        complexity = base_complexity + (security_implications * 15) + (dependency_impacts * 10) + (semantic_issues * 5)
        
        return min(100, complexity)
    
    def _get_complexity_level(self, complexity: float) -> str:
        """Get complexity level description."""
        if complexity >= 80:
            return "VERY_HIGH"
        elif complexity >= 60:
            return "HIGH"
        elif complexity >= 40:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _calculate_overall_health(self, risk_score: float, quality_score: float, complexity_score: float) -> Dict:
        """Calculate overall health indicator."""
        
        # Weighted health calculation
        health_score = (quality_score * 0.4) + ((100 - risk_score) * 0.4) + ((100 - complexity_score) * 0.2)
        
        if health_score >= 80:
            return {"status": "HEALTHY", "color": "🟢", "icon": "✅", "summary": "Low risk, high quality change"}
        elif health_score >= 60:
            return {"status": "CAUTION", "color": "🟡", "icon": "⚠️", "summary": "Moderate risk, acceptable quality"}
        elif health_score >= 40:
            return {"status": "WARNING", "color": "🟠", "icon": "⚠️", "summary": "Higher risk, quality concerns"}
        else:
            return {"status": "CRITICAL", "color": "🔴", "icon": "🚨", "summary": "High risk, quality issues"}
    
    def _create_dashboard_summary(self, risk_score: float, quality_score: float, complexity_score: float) -> str:
        """Create dashboard summary text."""
        return f"""
📊 REVIEW DASHBOARD SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 Quality: {quality_score}/100 {self._get_quality_color(quality_score)}
⚡ Risk: {risk_score}/100 {self._get_risk_color(risk_score)}
🧮 Complexity: {complexity_score}/100 {self._get_complexity_color(complexity_score)}
━━━━━━━━━━━━━━━━━━━━━━━━━━━
{self._calculate_overall_health(risk_score, quality_score, complexity_score)['summary']}
"""
    
    def _create_decision_matrix(self, risk_score: float, quality_score: float, production_ready: bool) -> List[Dict]:
        """Create decision matrix for guidance."""
        matrix = []
        
        # Quality vs Risk matrix
        if quality_score >= 90 and risk_score < 30:
            matrix.append({"condition": "High Quality + Low Risk", "recommendation": "APPROVE", "confidence": "HIGH"})
        elif quality_score >= 85 and risk_score < 60:
            matrix.append({"condition": "Good Quality + Medium Risk", "recommendation": "APPROVE_WITH_CONDITIONS", "confidence": "MEDIUM"})
        elif not production_ready:
            matrix.append({"condition": "Below Production Threshold", "recommendation": "REQUEST_CHANGES", "confidence": "HIGH"})
        elif risk_score >= 80:
            matrix.append({"condition": "Critical Risk Level", "recommendation": "DEFER_TO_COMMITTEE", "confidence": "HIGH"})
        else:
            matrix.append({"condition": "Standard Case", "recommendation": "APPROVE_WITH_CONDITIONS", "confidence": "MEDIUM"})
        
        return matrix
    
    def _generate_key_considerations(self, risk_assessment: Dict, quality_assessment: Dict, escalation_info: Dict) -> List[str]:
        """Generate key considerations for reviewer."""
        considerations = []
        
        # Risk-based considerations
        if risk_assessment.get("predictive_score", 0) >= 60:
            considerations.append("⚡ High risk score requires enhanced validation and monitoring")
        
        # Quality-based considerations
        if not quality_assessment.get("compliance", {}).get("production_ready", False):
            considerations.append("📊 Below 85% quality threshold - not ready for production")
        
        # Security considerations
        if risk_assessment.get("predictions", {}).get("cascading_failures"):
            considerations.append("🔒 Potential for cascading failures identified")
        
        # Meta-framework considerations
        if escalation_info.get("escalation_level") == "critical_risk":
            considerations.append("🧠 Critical changes require safety committee approval")
        
        return considerations
    
    def _create_risk_benefit_analysis(self, risk_assessment: Dict, quality_assessment: Dict) -> Dict:
        """Create risk-benefit analysis."""
        
        benefits = []
        risks = []
        
        # Assess benefits
        if quality_assessment.get("overall_score", 0) >= 85:
            benefits.append("High quality implementation meets production standards")
        
        # Assess risks
        if risk_assessment.get("predictive_score", 0) >= 60:
            risks.append("High probability of deployment issues")
        
        # Calculate net benefit
        benefit_score = len(benefits) * 25
        risk_impact = risk_assessment.get("predictive_score", 0)
        net_benefit = benefit_score - risk_impact
        
        return {
            "benefits": benefits,
            "risks": risks,
            "net_benefit_score": net_benefit,
            "recommendation": "PROCEED" if net_benefit > 0 else "RECONSIDER"
        }
    
    def _calculate_recommendation_confidence(self, risk_assessment: Dict, quality_assessment: Dict) -> str:
        """Calculate confidence in AI recommendation."""
        
        risk_confidence = risk_assessment.get("confidence", 0)
        quality_confidence = 85  # Assume high confidence in quality assessment
        
        avg_confidence = (risk_confidence + quality_confidence) / 2
        
        if avg_confidence >= 85:
            return "HIGH"
        elif avg_confidence >= 70:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _get_alternative_actions(self, recommended_action: str) -> List[str]:
        """Get alternative actions to recommended action."""
        all_actions = list(self.decision_templates.keys())
        return [action for action in all_actions if action != recommended_action]
    
    def _find_precedent_cases(self, risk_score: float, quality_score: float) -> List[Dict]:
        """Find similar precedent cases (simulated)."""
        # In real implementation, would query historical data
        return [
            {"case": "Similar risk/quality profile", "outcome": "Approved with monitoring", "date": "2025-07-01"},
            {"case": "High risk framework change", "outcome": "Required committee review", "date": "2025-06-15"}
        ]
    
    def _get_trend_indicator(self, risk_assessment: Dict) -> str:
        """Get risk trend indicator."""
        # Would calculate from historical data
        return "stable"
    
    def _create_dimension_chart(self, quality_assessment: Dict) -> List[Dict]:
        """Create quality dimension breakdown chart."""
        dimensions = quality_assessment.get("dimensions", {})
        chart = []
        
        for dimension, data in dimensions.items():
            chart.append({
                "name": dimension.replace("_", " ").title(),
                "score": data.get("score", 0),
                "weight": data.get("weight", 0) * 100
            })
        
        return chart
    
    def _categorize_file(self, file_path: str) -> str:
        """Categorize file by its path."""
        if ".claude/meta/" in file_path:
            return "META_FRAMEWORK"
        elif ".claude/system/quality/" in file_path:
            return "QUALITY_SYSTEM"
        elif ".claude/commands/" in file_path:
            return "COMMAND"
        elif ".claude/modules/" in file_path:
            return "MODULE"
        elif "CLAUDE.md" in file_path:
            return "CORE_CONFIG"
        else:
            return "OTHER"
    
    def _assess_file_risk(self, file_path: str) -> str:
        """Assess individual file risk level."""
        if ".claude/meta/" in file_path:
            return "CRITICAL"
        elif ".claude/system/quality/" in file_path or "CLAUDE.md" in file_path:
            return "HIGH"
        elif ".claude/commands/" in file_path:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _count_file_dependencies(self, file_path: str) -> int:
        """Count file dependencies (simulated)."""
        # Would scan for actual dependencies
        return 3
    
    def _assess_file_criticality(self, file_path: str) -> str:
        """Assess file criticality."""
        critical_patterns = ["meta", "quality", "CLAUDE.md"]
        if any(pattern in file_path for pattern in critical_patterns):
            return "CRITICAL"
        return "NORMAL"
    
    def _estimate_review_time(self, escalation_info: Dict) -> str:
        """Estimate review time based on escalation level."""
        level = escalation_info.get("escalation_level", "low_risk")
        time_estimates = {
            "critical_risk": "2-4 hours",
            "high_risk": "1-2 hours", 
            "medium_risk": "30-60 minutes",
            "low_risk": "15-30 minutes"
        }
        return time_estimates.get(level, "30-60 minutes")
    
    def _get_required_expertise(self, change_analysis: Dict) -> List[str]:
        """Get required expertise areas."""
        expertise = ["framework_knowledge"]
        
        if change_analysis.get("security_implications"):
            expertise.append("security")
        
        if any("meta" in str(change_analysis).lower().split() for change_analysis in [change_analysis]):
            expertise.append("meta_framework")
            
        return expertise
    
    # Additional helper methods would continue...
    def _assess_mitigation_complexity(self, strategies: List[str]) -> str:
        """Assess complexity of mitigation strategies."""
        if len(strategies) > 5:
            return "HIGH"
        elif len(strategies) > 2:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _get_dimension_status(self, score: float) -> str:
        """Get status for quality dimension."""
        if score >= 85:
            return "EXCELLENT"
        elif score >= 70:
            return "GOOD"
        else:
            return "NEEDS_IMPROVEMENT"

def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(description="Human review interface for prompt changes")
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    parser.add_argument("--risk-assessment", required=True, help="Risk assessment JSON file")
    parser.add_argument("--quality-assessment", required=True, help="Quality assessment JSON file")
    parser.add_argument("--change-analysis", required=True, help="Change analysis JSON file")
    parser.add_argument("--escalation-info", required=True, help="Escalation info JSON file")
    parser.add_argument("--changed-files", nargs="+", required=True, help="List of changed files")
    parser.add_argument("--output", help="Output file for review interface")
    parser.add_argument("--format", choices=["json", "html", "markdown"], default="json", help="Output format")
    
    args = parser.parse_args()
    
    # Load assessment files
    with open(args.risk_assessment, 'r') as f:
        risk_assessment = json.load(f)
    
    with open(args.quality_assessment, 'r') as f:
        quality_assessment = json.load(f)
    
    with open(args.change_analysis, 'r') as f:
        change_analysis = json.load(f)
    
    with open(args.escalation_info, 'r') as f:
        escalation_info = json.load(f)
    
    # Create review interface
    interface = HumanReviewInterface(args.repo_root)
    review_interface = interface.create_review_interface(
        risk_assessment, quality_assessment, change_analysis, escalation_info, args.changed_files
    )
    
    # Generate output
    if args.format == "json":
        output = json.dumps(review_interface, indent=2)
    elif args.format == "markdown":
        output = interface._generate_markdown_interface(review_interface)
    elif args.format == "html":
        output = interface._generate_html_interface(review_interface)
    else:
        output = json.dumps(review_interface, indent=2)
    
    if args.output:
        Path(args.output).write_text(output)
        print(f"👥 Review interface written to {args.output}")
    else:
        print(output)

if __name__ == "__main__":
    main()