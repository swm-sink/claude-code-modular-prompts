#!/usr/bin/env python3
"""
Continuous Improvement System
Agent 14: Data-driven improvement tracking, trend analysis, and optimization recommendations
"""

import os
import json
import numpy as np
import pandas as pd
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
import statistics
from enum import Enum

class ImprovementType(Enum):
    PERFORMANCE = "performance"
    QUALITY = "quality"
    SECURITY = "security"
    RELIABILITY = "reliability"
    USER_EXPERIENCE = "user_experience"
    OPERATIONAL = "operational"

class ImprovementPriority(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

@dataclass
class ImprovementOpportunity:
    """Improvement opportunity data structure"""
    id: str
    type: str
    priority: str
    title: str
    description: str
    current_state: Dict[str, Any]
    target_state: Dict[str, Any]
    impact_estimate: float
    effort_estimate: float
    roi_score: float
    confidence_level: float
    data_sources: List[str]
    recommended_actions: List[str]
    success_metrics: List[str]
    timeline_estimate: str
    dependencies: List[str]
    risks: List[str]
    created_at: str
    updated_at: str

@dataclass
class TrendAnalysis:
    """Trend analysis results"""
    metric_name: str
    trend_direction: str  # improving, degrading, stable
    trend_strength: float  # 0-1
    change_rate: float
    confidence: float
    data_points: int
    time_period: str
    statistical_significance: bool
    trend_summary: str

@dataclass
class ImprovementKPI:
    """Key Performance Indicator for improvements"""
    name: str
    current_value: float
    target_value: float
    trend: str
    improvement_rate: float
    achievement_percentage: float
    last_updated: str

class ContinuousImprovementSystem:
    """Comprehensive continuous improvement and optimization system"""
    
    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path)
        self.improvement_dir = self.root_path / "reports" / "continuous-improvement"
        self.improvement_dir.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        self.setup_logging()
        
        # Historical data storage
        self.metrics_history = deque(maxlen=1000)  # Keep last 1000 data points
        self.improvement_opportunities = {}
        self.improvement_kpis = {}
        
        # Analysis configuration
        self.trend_analysis_window = 30  # days
        self.significance_threshold = 0.05
        self.minimum_data_points = 5
        
        # Load historical data
        self.load_historical_data()
        
    def setup_logging(self):
        """Setup logging for continuous improvement system"""
        log_dir = self.improvement_dir / "logs"
        log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_dir / f"improvement-{datetime.utcnow().strftime('%Y-%m-%d')}.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def load_historical_data(self):
        """Load historical metrics data for analysis"""
        try:
            # Load production monitoring data
            prod_monitoring_dir = self.root_path / "reports" / "production-monitoring" / "daily"
            if prod_monitoring_dir.exists():
                for day_dir in sorted(prod_monitoring_dir.iterdir()):
                    if day_dir.is_dir():
                        for file_path in sorted(day_dir.glob("*.json")):
                            try:
                                with open(file_path, 'r') as f:
                                    data = json.load(f)
                                    self.metrics_history.append(data)
                            except Exception as e:
                                self.logger.warning(f"Error loading {file_path}: {e}")
                                
            # Load operational monitoring data
            ops_monitoring_dir = self.root_path / "reports" / "operational-monitoring" / "daily"
            if ops_monitoring_dir.exists():
                for day_dir in sorted(ops_monitoring_dir.iterdir()):
                    if day_dir.is_dir():
                        for file_path in sorted(day_dir.glob("*.json")):
                            try:
                                with open(file_path, 'r') as f:
                                    data = json.load(f)
                                    # Merge with existing data or add new
                                    for existing_data in self.metrics_history:
                                        if existing_data.get('timestamp') == data.get('timestamp'):
                                            existing_data.update(data)
                                            break
                                    else:
                                        self.metrics_history.append(data)
                            except Exception as e:
                                self.logger.warning(f"Error loading {file_path}: {e}")
                                
            self.logger.info(f"Loaded {len(self.metrics_history)} historical data points")
            
        except Exception as e:
            self.logger.error(f"Error loading historical data: {e}")
            
    def analyze_trends(self, metric_path: str, days: int = None) -> TrendAnalysis:
        """Analyze trends for a specific metric"""
        if days is None:
            days = self.trend_analysis_window
            
        try:
            # Extract metric values from historical data
            cutoff_date = datetime.utcnow() - timedelta(days=days)
            
            values = []
            timestamps = []
            
            for data_point in self.metrics_history:
                try:
                    timestamp_str = data_point.get('timestamp')
                    if not timestamp_str:
                        continue
                        
                    timestamp = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
                    if timestamp < cutoff_date:
                        continue
                        
                    # Navigate to metric value using dot notation
                    value = self.get_nested_value(data_point, metric_path)
                    if value is not None:
                        values.append(float(value))
                        timestamps.append(timestamp)
                        
                except Exception as e:
                    continue
                    
            if len(values) < self.minimum_data_points:
                return TrendAnalysis(
                    metric_name=metric_path,
                    trend_direction="insufficient_data",
                    trend_strength=0.0,
                    change_rate=0.0,
                    confidence=0.0,
                    data_points=len(values),
                    time_period=f"{days} days",
                    statistical_significance=False,
                    trend_summary=f"Insufficient data points ({len(values)} < {self.minimum_data_points})"
                )
                
            # Calculate trend statistics
            trend_stats = self.calculate_trend_statistics(values, timestamps)
            
            return TrendAnalysis(
                metric_name=metric_path,
                trend_direction=trend_stats['direction'],
                trend_strength=trend_stats['strength'],
                change_rate=trend_stats['change_rate'],
                confidence=trend_stats['confidence'],
                data_points=len(values),
                time_period=f"{days} days",
                statistical_significance=trend_stats['significant'],
                trend_summary=trend_stats['summary']
            )
            
        except Exception as e:
            self.logger.error(f"Error analyzing trends for {metric_path}: {e}")
            return TrendAnalysis(
                metric_name=metric_path,
                trend_direction="error",
                trend_strength=0.0,
                change_rate=0.0,
                confidence=0.0,
                data_points=0,
                time_period=f"{days} days",
                statistical_significance=False,
                trend_summary=f"Analysis error: {str(e)}"
            )
            
    def get_nested_value(self, data: Dict, path: str) -> Any:
        """Get nested value from dictionary using dot notation"""
        keys = path.split('.')
        current = data
        
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
                
        return current
        
    def calculate_trend_statistics(self, values: List[float], timestamps: List[datetime]) -> Dict[str, Any]:
        """Calculate statistical trend analysis"""
        try:
            # Convert timestamps to numeric values (days since first timestamp)
            time_deltas = [(ts - timestamps[0]).total_seconds() / 86400 for ts in timestamps]
            
            # Calculate linear regression
            if len(values) >= 2:
                correlation = np.corrcoef(time_deltas, values)[0, 1] if len(set(values)) > 1 else 0
                slope = np.polyfit(time_deltas, values, 1)[0] if len(set(time_deltas)) > 1 else 0
            else:
                correlation = 0
                slope = 0
                
            # Determine trend direction and strength
            if abs(correlation) < 0.1:
                direction = "stable"
                strength = 0.0
            elif correlation > 0:
                direction = "improving"
                strength = abs(correlation)
            else:
                direction = "degrading"
                strength = abs(correlation)
                
            # Calculate change rate (per day)
            if len(values) >= 2:
                total_days = (timestamps[-1] - timestamps[0]).total_seconds() / 86400
                total_change = values[-1] - values[0]
                change_rate = total_change / max(total_days, 1) if total_days > 0 else 0
            else:
                change_rate = 0
                
            # Statistical significance (simplified)
            significant = len(values) >= 10 and abs(correlation) > 0.3
            
            # Confidence calculation
            confidence = min(1.0, len(values) / 30 * abs(correlation))
            
            # Summary
            if direction == "stable":
                summary = f"Metric is stable with {len(values)} data points"
            elif direction == "improving":
                summary = f"Metric is improving (correlation: {correlation:.3f}, change rate: {change_rate:.3f}/day)"
            else:
                summary = f"Metric is degrading (correlation: {correlation:.3f}, change rate: {change_rate:.3f}/day)"
                
            return {
                'direction': direction,
                'strength': strength,
                'change_rate': change_rate,
                'confidence': confidence,
                'significant': significant,
                'correlation': correlation,
                'slope': slope,
                'summary': summary
            }
            
        except Exception as e:
            self.logger.error(f"Error calculating trend statistics: {e}")
            return {
                'direction': 'error',
                'strength': 0.0,
                'change_rate': 0.0,
                'confidence': 0.0,
                'significant': False,
                'correlation': 0.0,
                'slope': 0.0,
                'summary': f"Calculation error: {str(e)}"
            }
            
    def identify_improvement_opportunities(self) -> List[ImprovementOpportunity]:
        """Identify improvement opportunities based on trend analysis and current state"""
        opportunities = []
        
        # Define key metrics to analyze
        metrics_to_analyze = [
            {
                'path': 'performance.response_time_p95',
                'type': ImprovementType.PERFORMANCE,
                'target_trend': 'decreasing',
                'target_value': 500.0,
                'unit': 'ms'
            },
            {
                'path': 'quality.security_score',
                'type': ImprovementType.SECURITY,
                'target_trend': 'increasing',
                'target_value': 90.0,
                'unit': 'score'
            },
            {
                'path': 'quality.quality_gate_pass_rate',
                'type': ImprovementType.QUALITY,
                'target_trend': 'increasing',
                'target_value': 98.0,
                'unit': '%'
            },
            {
                'path': 'operational.availability_percent',
                'type': ImprovementType.RELIABILITY,
                'target_trend': 'increasing',
                'target_value': 99.99,
                'unit': '%'
            },
            {
                'path': 'quality.documentation_accuracy_score',
                'type': ImprovementType.USER_EXPERIENCE,
                'target_trend': 'increasing',
                'target_value': 90.0,
                'unit': '%'
            }
        ]
        
        for metric_config in metrics_to_analyze:
            try:
                trend_analysis = self.analyze_trends(metric_config['path'])
                
                if trend_analysis.data_points < self.minimum_data_points:
                    continue
                    
                # Get current value
                current_value = self.get_current_metric_value(metric_config['path'])
                if current_value is None:
                    continue
                    
                opportunity = self.evaluate_metric_opportunity(
                    metric_config, trend_analysis, current_value
                )
                
                if opportunity:
                    opportunities.append(opportunity)
                    
            except Exception as e:
                self.logger.error(f"Error evaluating metric {metric_config['path']}: {e}")
                
        # Sort by ROI score
        opportunities.sort(key=lambda x: x.roi_score, reverse=True)
        
        return opportunities
        
    def get_current_metric_value(self, metric_path: str) -> Optional[float]:
        """Get current value for a metric"""
        try:
            # Check latest production monitoring data
            latest_file = self.root_path / "reports" / "production-monitoring" / "current" / "production-monitoring-latest.json"
            if latest_file.exists():
                with open(latest_file, 'r') as f:
                    data = json.load(f)
                    value = self.get_nested_value(data, metric_path)
                    if value is not None:
                        return float(value)
                        
            # Check latest operational monitoring data
            ops_latest_file = self.root_path / "reports" / "operational-monitoring" / "current" / "operational-monitoring-latest.json"
            if ops_latest_file.exists():
                with open(ops_latest_file, 'r') as f:
                    data = json.load(f)
                    value = self.get_nested_value(data, metric_path)
                    if value is not None:
                        return float(value)
                        
            return None
        except Exception as e:
            self.logger.error(f"Error getting current value for {metric_path}: {e}")
            return None
            
    def evaluate_metric_opportunity(self, metric_config: Dict, trend_analysis: TrendAnalysis, 
                                  current_value: float) -> Optional[ImprovementOpportunity]:
        """Evaluate improvement opportunity for a specific metric"""
        target_value = metric_config['target_value']
        metric_type = metric_config['type']
        target_trend = metric_config['target_trend']
        
        # Calculate gap and impact
        if target_trend == 'increasing':
            gap = max(0, target_value - current_value)
            impact = gap / target_value if target_value > 0 else 0
            needs_improvement = current_value < target_value
        else:  # decreasing
            gap = max(0, current_value - target_value)
            impact = gap / current_value if current_value > 0 else 0
            needs_improvement = current_value > target_value
            
        # Skip if no improvement needed
        if not needs_improvement or impact < 0.05:  # Less than 5% gap
            return None
            
        # Calculate priority based on impact and trend
        if impact > 0.5 or trend_analysis.trend_direction == "degrading":
            priority = ImprovementPriority.HIGH
        elif impact > 0.2:
            priority = ImprovementPriority.MEDIUM
        else:
            priority = ImprovementPriority.LOW
            
        # Generate recommendations based on metric type
        recommendations = self.generate_metric_recommendations(metric_config, trend_analysis, current_value)
        
        # Estimate effort and ROI
        effort_estimate = self.estimate_improvement_effort(metric_type, impact)
        roi_score = impact / max(effort_estimate, 0.1)  # Prevent division by zero
        
        opportunity_id = f"{metric_type.value}_{int(datetime.utcnow().timestamp())}"
        
        return ImprovementOpportunity(
            id=opportunity_id,
            type=metric_type.value,
            priority=priority.value,
            title=f"Improve {metric_config['path'].replace('.', ' ').title()}",
            description=f"Current {metric_config['path']}: {current_value:.2f}{metric_config['unit']}, Target: {target_value:.2f}{metric_config['unit']} (Gap: {gap:.2f})",
            current_state={
                'value': current_value,
                'trend': trend_analysis.trend_direction,
                'trend_strength': trend_analysis.trend_strength
            },
            target_state={
                'value': target_value,
                'improvement_percentage': impact * 100
            },
            impact_estimate=impact,
            effort_estimate=effort_estimate,
            roi_score=roi_score,
            confidence_level=trend_analysis.confidence,
            data_sources=[metric_config['path']],
            recommended_actions=recommendations,
            success_metrics=[
                f"{metric_config['path']} reaches {target_value:.2f}{metric_config['unit']}",
                f"Improvement trend sustained for 30+ days"
            ],
            timeline_estimate=self.estimate_improvement_timeline(effort_estimate),
            dependencies=self.identify_improvement_dependencies(metric_type),
            risks=self.identify_improvement_risks(metric_type),
            created_at=datetime.utcnow().isoformat(),
            updated_at=datetime.utcnow().isoformat()
        )
        
    def generate_metric_recommendations(self, metric_config: Dict, trend_analysis: TrendAnalysis, 
                                      current_value: float) -> List[str]:
        """Generate specific recommendations based on metric type"""
        metric_type = metric_config['type']
        
        recommendations = {
            ImprovementType.PERFORMANCE: [
                "Optimize framework loading and initialization",
                "Implement caching for frequently accessed data",
                "Profile and optimize critical code paths",
                "Consider asynchronous processing for heavy operations"
            ],
            ImprovementType.SECURITY: [
                "Address critical security vulnerabilities immediately",
                "Implement automated security scanning in CI/CD",
                "Enhance access controls and authentication",
                "Regular security audits and penetration testing"
            ],
            ImprovementType.QUALITY: [
                "Increase test coverage to 95%+",
                "Implement stricter quality gates",
                "Enhance code review processes",
                "Automate quality checks in development workflow"
            ],
            ImprovementType.RELIABILITY: [
                "Implement redundancy and failover mechanisms",
                "Enhance monitoring and alerting",
                "Improve error handling and recovery",
                "Establish SRE practices and runbooks"
            ],
            ImprovementType.USER_EXPERIENCE: [
                "Improve documentation accuracy and completeness",
                "Enhance user onboarding and guides",
                "Implement user feedback collection",
                "Streamline user workflows and interfaces"
            ],
            ImprovementType.OPERATIONAL: [
                "Automate deployment and rollback processes",
                "Implement infrastructure as code",
                "Enhance monitoring and observability",
                "Establish incident response procedures"
            ]
        }
        
        return recommendations.get(metric_type, ["Review and optimize current processes"])
        
    def estimate_improvement_effort(self, metric_type: ImprovementType, impact: float) -> float:
        """Estimate effort required for improvement (0-1 scale)"""
        base_efforts = {
            ImprovementType.PERFORMANCE: 0.3,
            ImprovementType.SECURITY: 0.5,
            ImprovementType.QUALITY: 0.4,
            ImprovementType.RELIABILITY: 0.6,
            ImprovementType.USER_EXPERIENCE: 0.2,
            ImprovementType.OPERATIONAL: 0.4
        }
        
        base_effort = base_efforts.get(metric_type, 0.4)
        
        # Adjust based on impact (larger impact = more effort)
        adjusted_effort = base_effort + (impact * 0.3)
        
        return min(1.0, adjusted_effort)
        
    def estimate_improvement_timeline(self, effort: float) -> str:
        """Estimate timeline for improvement implementation"""
        if effort < 0.2:
            return "1-2 weeks"
        elif effort < 0.4:
            return "2-4 weeks"
        elif effort < 0.6:
            return "1-2 months"
        elif effort < 0.8:
            return "2-3 months"
        else:
            return "3+ months"
            
    def identify_improvement_dependencies(self, metric_type: ImprovementType) -> List[str]:
        """Identify dependencies for improvement implementation"""
        dependencies = {
            ImprovementType.PERFORMANCE: [
                "Performance profiling tools",
                "Load testing infrastructure",
                "Monitoring and metrics collection"
            ],
            ImprovementType.SECURITY: [
                "Security scanning tools",
                "Vulnerability databases",
                "Security team review"
            ],
            ImprovementType.QUALITY: [
                "Test automation infrastructure",
                "Quality gate configuration",
                "Development team training"
            ],
            ImprovementType.RELIABILITY: [
                "Monitoring infrastructure",
                "Incident response procedures",
                "SRE team resources"
            ],
            ImprovementType.USER_EXPERIENCE: [
                "User feedback mechanisms",
                "Documentation review process",
                "UX design resources"
            ],
            ImprovementType.OPERATIONAL: [
                "Automation tools",
                "Infrastructure resources",
                "DevOps team capacity"
            ]
        }
        
        return dependencies.get(metric_type, ["Team resources and time"])
        
    def identify_improvement_risks(self, metric_type: ImprovementType) -> List[str]:
        """Identify risks associated with improvement implementation"""
        risks = {
            ImprovementType.PERFORMANCE: [
                "Performance optimizations may introduce bugs",
                "Changes could affect system stability",
                "Resource constraints may limit improvements"
            ],
            ImprovementType.SECURITY: [
                "Security changes may break existing functionality",
                "New security measures may impact user experience",
                "False positives in security scanning"
            ],
            ImprovementType.QUALITY: [
                "Stricter quality gates may slow development",
                "Quality improvements require team adoption",
                "Balancing quality vs. delivery speed"
            ],
            ImprovementType.RELIABILITY: [
                "Reliability improvements may require system downtime",
                "Complex failover mechanisms may introduce failure points",
                "Cost of redundancy and monitoring"
            ],
            ImprovementType.USER_EXPERIENCE: [
                "User experience changes may confuse existing users",
                "Documentation updates require ongoing maintenance",
                "User feedback may be subjective or conflicting"
            ],
            ImprovementType.OPERATIONAL: [
                "Operational changes may disrupt existing workflows",
                "Automation may fail and require manual intervention",
                "Team training and adoption challenges"
            ]
        }
        
        return risks.get(metric_type, ["Implementation complexity and resource requirements"])
        
    def update_improvement_kpis(self) -> Dict[str, ImprovementKPI]:
        """Update improvement KPIs based on current metrics"""
        kpis = {}
        
        # Define key improvement KPIs
        kpi_definitions = [
            {
                'name': 'Framework Response Time',
                'metric_path': 'performance.response_time_p95',
                'target': 500.0,
                'direction': 'decrease'
            },
            {
                'name': 'Security Score',
                'metric_path': 'quality.security_score',
                'target': 90.0,
                'direction': 'increase'
            },
            {
                'name': 'Quality Gate Pass Rate',
                'metric_path': 'quality.quality_gate_pass_rate',
                'target': 98.0,
                'direction': 'increase'
            },
            {
                'name': 'System Availability',
                'metric_path': 'operational.availability_percent',
                'target': 99.99,
                'direction': 'increase'
            },
            {
                'name': 'Documentation Accuracy',
                'metric_path': 'quality.documentation_accuracy_score',
                'target': 90.0,
                'direction': 'increase'
            }
        ]
        
        for kpi_def in kpi_definitions:
            try:
                current_value = self.get_current_metric_value(kpi_def['metric_path'])
                if current_value is None:
                    continue
                    
                trend_analysis = self.analyze_trends(kpi_def['metric_path'], days=7)
                
                # Calculate achievement percentage
                if kpi_def['direction'] == 'increase':
                    achievement_pct = (current_value / kpi_def['target']) * 100
                    improvement_rate = trend_analysis.change_rate
                else:
                    achievement_pct = (kpi_def['target'] / max(current_value, 0.1)) * 100
                    improvement_rate = -trend_analysis.change_rate
                    
                achievement_pct = min(100, max(0, achievement_pct))
                
                # Determine trend status
                if trend_analysis.trend_direction == "improving":
                    trend_status = "↗️ Improving"
                elif trend_analysis.trend_direction == "degrading":
                    trend_status = "↘️ Degrading"
                else:
                    trend_status = "→ Stable"
                    
                kpi = ImprovementKPI(
                    name=kpi_def['name'],
                    current_value=current_value,
                    target_value=kpi_def['target'],
                    trend=trend_status,
                    improvement_rate=improvement_rate,
                    achievement_percentage=achievement_pct,
                    last_updated=datetime.utcnow().isoformat()
                )
                
                kpis[kpi_def['name']] = kpi
                
            except Exception as e:
                self.logger.error(f"Error updating KPI {kpi_def['name']}: {e}")
                
        self.improvement_kpis = kpis
        return kpis
        
    def generate_improvement_report(self) -> str:
        """Generate comprehensive improvement analysis report"""
        # Update KPIs and identify opportunities
        kpis = self.update_improvement_kpis()
        opportunities = self.identify_improvement_opportunities()
        
        report = f"""# Continuous Improvement Report - Agent 14

**Generated**: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}
**Analysis Period**: {self.trend_analysis_window} days
**Data Points Analyzed**: {len(self.metrics_history)}

## 📊 Improvement KPIs

"""
        
        for kpi_name, kpi in kpis.items():
            status_emoji = "✅" if kpi.achievement_percentage >= 95 else "⚠️" if kpi.achievement_percentage >= 80 else "❌"
            report += f"""### {status_emoji} {kpi.name}
- **Current**: {kpi.current_value:.2f}
- **Target**: {kpi.target_value:.2f}
- **Achievement**: {kpi.achievement_percentage:.1f}%
- **Trend**: {kpi.trend}
- **Improvement Rate**: {kpi.improvement_rate:.3f}/day

"""
        
        report += "## 🎯 Top Improvement Opportunities\n\n"
        
        if opportunities:
            for i, opp in enumerate(opportunities[:5], 1):  # Top 5 opportunities
                priority_emoji = {
                    'critical': '🔴',
                    'high': '🟠',
                    'medium': '🟡',
                    'low': '🔵'
                }.get(opp.priority, '⚪')
                
                report += f"""### {i}. {priority_emoji} {opp.title}
- **Priority**: {opp.priority.upper()}
- **Type**: {opp.type.title()}
- **Impact**: {opp.impact_estimate:.1%}
- **Effort**: {opp.effort_estimate:.1f}/1.0
- **ROI Score**: {opp.roi_score:.2f}
- **Timeline**: {opp.timeline_estimate}
- **Confidence**: {opp.confidence_level:.1%}

**Description**: {opp.description}

**Current State**:
- Value: {opp.current_state['value']:.2f}
- Trend: {opp.current_state['trend']}

**Target State**:
- Value: {opp.target_state['value']:.2f}
- Improvement: {opp.target_state['improvement_percentage']:.1f}%

**Recommended Actions**:
"""
                for action in opp.recommended_actions[:3]:  # Top 3 actions
                    report += f"- {action}\n"
                    
                report += f"""
**Success Metrics**:
"""
                for metric in opp.success_metrics:
                    report += f"- {metric}\n"
                    
                report += "\n"
        else:
            report += "No significant improvement opportunities identified at this time.\n\n"
            
        report += """## 📈 Trend Analysis Summary

"""
        
        # Analyze key metrics trends
        key_metrics = [
            'performance.response_time_p95',
            'quality.security_score', 
            'quality.quality_gate_pass_rate',
            'operational.availability_percent'
        ]
        
        for metric in key_metrics:
            trend = self.analyze_trends(metric)
            if trend.data_points >= self.minimum_data_points:
                trend_emoji = "📈" if trend.trend_direction == "improving" else "📉" if trend.trend_direction == "degrading" else "📊"
                report += f"- **{metric}**: {trend_emoji} {trend.trend_direction} ({trend.data_points} data points, {trend.confidence:.1%} confidence)\n"
                
        report += f"""

## 🔄 Continuous Improvement Process

### Feedback Loops
1. **Automated Monitoring**: Continuous metrics collection and analysis
2. **Trend Detection**: Daily trend analysis with statistical significance testing
3. **Opportunity Identification**: Weekly opportunity assessment and prioritization
4. **Implementation Tracking**: Monthly progress review and adjustment

### Success Patterns
- Focus on high-ROI improvements (ROI > 2.0)
- Address degrading trends immediately
- Maintain gains through continuous monitoring
- Balance quick wins with strategic improvements

### Improvement Methodology
1. **Identify**: Data-driven opportunity identification
2. **Prioritize**: ROI-based prioritization with impact/effort analysis
3. **Plan**: Detailed implementation planning with dependencies and risks
4. **Execute**: Systematic implementation with progress tracking
5. **Measure**: Continuous measurement and validation of improvements
6. **Sustain**: Long-term monitoring to ensure gains are maintained

## 📋 Next Actions

### Immediate (This Week)
"""
        
        # Add immediate actions based on opportunities
        high_priority_opps = [opp for opp in opportunities if opp.priority in ['critical', 'high']]
        if high_priority_opps:
            for opp in high_priority_opps[:3]:
                report += f"- Address {opp.title} ({opp.priority} priority)\n"
        else:
            report += "- Continue monitoring current performance levels\n"
            
        report += """
### Short-term (This Month)
- Implement top 3 improvement opportunities
- Review and update improvement KPI targets
- Establish baseline measurements for new initiatives

### Long-term (This Quarter)
- Establish predictive improvement analytics
- Implement automated improvement recommendations
- Create improvement culture and training programs

## 💡 Strategic Recommendations

"""
        
        # Generate strategic recommendations
        strategic_recommendations = []
        
        if any(kpi.achievement_percentage < 80 for kpi in kpis.values()):
            strategic_recommendations.append("🎯 Focus on achieving 80%+ on all KPIs before adding new metrics")
            
        if any(opp.priority == 'critical' for opp in opportunities):
            strategic_recommendations.append("🚨 Address critical improvement opportunities immediately")
            
        if len(opportunities) > 10:
            strategic_recommendations.append("📊 Implement prioritization framework to focus on highest-impact improvements")
            
        if len(self.metrics_history) < 100:
            strategic_recommendations.append("📈 Collect more historical data to improve trend analysis accuracy")
            
        if not strategic_recommendations:
            strategic_recommendations.append("✅ System is performing well - maintain current improvement processes")
            
        for rec in strategic_recommendations:
            report += f"- {rec}\n"
            
        report += f"""

---
**Continuous Improvement System**: Agent 14
**Report ID**: improvement-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}
**Next Analysis**: {(datetime.utcnow() + timedelta(days=7)).strftime('%Y-%m-%d')}
**Historical Data Points**: {len(self.metrics_history)}
"""
        
        return report
        
    def save_improvement_analysis(self, opportunities: List[ImprovementOpportunity], 
                                kpis: Dict[str, ImprovementKPI], report: str):
        """Save improvement analysis results"""
        timestamp = datetime.utcnow()
        
        # Save opportunities
        opportunities_data = {
            'timestamp': timestamp.isoformat(),
            'opportunities': [asdict(opp) for opp in opportunities],
            'total_opportunities': len(opportunities),
            'high_priority_count': len([opp for opp in opportunities if opp.priority in ['critical', 'high']])
        }
        
        opportunities_file = self.improvement_dir / f"opportunities-{timestamp.strftime('%Y-%m-%d-%H%M%S')}.json"
        with open(opportunities_file, 'w') as f:
            json.dump(opportunities_data, f, indent=2)
            
        # Save KPIs
        kpis_data = {
            'timestamp': timestamp.isoformat(),
            'kpis': {name: asdict(kpi) for name, kpi in kpis.items()},
            'overall_achievement': statistics.mean([kpi.achievement_percentage for kpi in kpis.values()]) if kpis else 0
        }
        
        kpis_file = self.improvement_dir / f"kpis-{timestamp.strftime('%Y-%m-%d-%H%M%S')}.json"
        with open(kpis_file, 'w') as f:
            json.dump(kpis_data, f, indent=2)
            
        # Save report
        report_file = self.improvement_dir / f"improvement-report-{timestamp.strftime('%Y-%m-%d-%H%M%S')}.md"
        with open(report_file, 'w') as f:
            f.write(report)
            
        # Update latest files
        latest_dir = self.improvement_dir / "latest"
        latest_dir.mkdir(exist_ok=True)
        
        with open(latest_dir / "opportunities-latest.json", 'w') as f:
            json.dump(opportunities_data, f, indent=2)
            
        with open(latest_dir / "kpis-latest.json", 'w') as f:
            json.dump(kpis_data, f, indent=2)
            
        with open(latest_dir / "improvement-report-latest.md", 'w') as f:
            f.write(report)
            
        self.logger.info(f"Improvement analysis saved: {report_file}")
        
    def run_improvement_analysis(self) -> Dict[str, Any]:
        """Run complete improvement analysis cycle"""
        self.logger.info("🔍 Running continuous improvement analysis...")
        
        try:
            # Update KPIs
            kpis = self.update_improvement_kpis()
            
            # Identify opportunities
            opportunities = self.identify_improvement_opportunities()
            
            # Generate report
            report = self.generate_improvement_report()
            
            # Save results
            self.save_improvement_analysis(opportunities, kpis, report)
            
            # Return summary
            return {
                'timestamp': datetime.utcnow().isoformat(),
                'opportunities_identified': len(opportunities),
                'high_priority_opportunities': len([opp for opp in opportunities if opp.priority in ['critical', 'high']]),
                'kpis_tracked': len(kpis),
                'average_kpi_achievement': statistics.mean([kpi.achievement_percentage for kpi in kpis.values()]) if kpis else 0,
                'data_points_analyzed': len(self.metrics_history),
                'analysis_status': 'completed'
            }
            
        except Exception as e:
            self.logger.error(f"Error in improvement analysis: {e}")
            return {
                'timestamp': datetime.utcnow().isoformat(),
                'analysis_status': 'error',
                'error_message': str(e)
            }

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Continuous Improvement System')
    parser.add_argument('--mode', choices=['analyze', 'report', 'kpis'], default='analyze',
                       help='Analysis mode')
    
    args = parser.parse_args()
    
    improvement_system = ContinuousImprovementSystem()
    
    if args.mode == 'analyze':
        print("🔍 Running continuous improvement analysis...")
        result = improvement_system.run_improvement_analysis()
        
        print(f"✅ Analysis complete:")
        print(f"📊 Opportunities identified: {result.get('opportunities_identified', 0)}")
        print(f"🎯 High priority: {result.get('high_priority_opportunities', 0)}")
        print(f"📈 KPIs tracked: {result.get('kpis_tracked', 0)}")
        print(f"⭐ Average KPI achievement: {result.get('average_kpi_achievement', 0):.1f}%")
        
    elif args.mode == 'report':
        print("📊 Generating improvement report...")
        report = improvement_system.generate_improvement_report()
        print(report)
        
    elif args.mode == 'kpis':
        print("📈 Updating improvement KPIs...")
        kpis = improvement_system.update_improvement_kpis()
        
        print(f"\n📊 Current KPIs:")
        for name, kpi in kpis.items():
            status = "✅" if kpi.achievement_percentage >= 95 else "⚠️" if kpi.achievement_percentage >= 80 else "❌"
            print(f"{status} {name}: {kpi.current_value:.2f} (target: {kpi.target_value:.2f}) - {kpi.achievement_percentage:.1f}%")

if __name__ == "__main__":
    main()