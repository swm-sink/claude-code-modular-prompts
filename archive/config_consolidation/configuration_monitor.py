#!/usr/bin/env python3
"""
Configuration Change Monitoring System for PROJECT_CONFIG
Tracks configuration changes, impact analysis, and health monitoring

TASK 6: Build configuration change monitoring system  
Author: Agent 4 - Configuration System Simplification
"""

import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import xml.etree.ElementTree as ET
import hashlib


class ChangeType(Enum):
    """Types of configuration changes"""
    ADDED = "added"
    MODIFIED = "modified" 
    REMOVED = "removed"
    RESTRUCTURED = "restructured"


class ImpactLevel(Enum):
    """Impact levels for configuration changes"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"


@dataclass
class ConfigurationChange:
    """Represents a single configuration change"""
    timestamp: str
    change_type: ChangeType
    path: str
    old_value: Optional[str]
    new_value: Optional[str]
    impact_level: ImpactLevel
    description: str
    affected_components: List[str]


@dataclass
class ChangeImpactAnalysis:
    """Analysis of change impact on the system"""
    breaking_changes: List[str]
    performance_impact: str
    quality_impact: str
    security_impact: str
    recommended_actions: List[str]
    rollback_complexity: str


@dataclass
class ConfigurationHealth:
    """Health metrics for configuration"""
    setup_time_seconds: float
    developer_satisfaction_score: float
    framework_utilization_percent: float
    quality_achievement_percent: float
    performance_achievement_percent: float
    error_rate_percent: float
    last_updated: str


@dataclass
class HealthTrend:
    """Trend analysis for configuration health"""
    metric_name: str
    current_value: float
    previous_value: float
    trend_direction: str  # "improving", "declining", "stable"
    significance: str  # "significant", "minor", "negligible"


class ConfigurationMonitor:
    """Main configuration monitoring and analysis engine"""
    
    def __init__(self, project_root: Path, history_file: Optional[Path] = None):
        self.project_root = project_root
        self.history_file = history_file or project_root / ".claude" / "config_history.json"
        self.health_file = project_root / ".claude" / "config_health.json"
        self.metrics_file = project_root / ".claude" / "config_metrics.json"
        
        # Ensure monitoring directory exists
        self.history_file.parent.mkdir(parents=True, exist_ok=True)
    
    def track_configuration_change(self, config_path: Path, description: str = "") -> ChangeImpactAnalysis:
        """Track a configuration change and analyze its impact"""
        current_config = self._parse_config(config_path)
        previous_config = self._get_previous_config()
        
        changes = self._detect_changes(previous_config, current_config)
        impact_analysis = self._analyze_change_impact(changes)
        
        # Record changes in history
        change_record = {
            "timestamp": datetime.now().isoformat(),
            "config_hash": self._calculate_config_hash(current_config),
            "changes": [asdict(change) for change in changes],
            "impact_analysis": asdict(impact_analysis),
            "description": description
        }
        
        self._save_change_record(change_record)
        self._update_current_config(current_config)
        
        return impact_analysis
    
    def validate_change_safety(self, old_config: Dict[str, Any], new_config: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate that configuration changes are safe"""
        safety_issues = []
        
        # Check for quality threshold degradation
        old_coverage = self._extract_coverage_threshold(old_config)
        new_coverage = self._extract_coverage_threshold(new_config)
        
        if old_coverage and new_coverage and new_coverage < old_coverage:
            if old_coverage - new_coverage > 10:  # More than 10% reduction
                safety_issues.append(f"Significant coverage reduction: {old_coverage}% → {new_coverage}%")
        
        # Check for security requirement removal
        old_security = old_config.get("security_requirements", {})
        new_security = new_config.get("security_requirements", {})
        
        for key, value in old_security.items():
            if key not in new_security or new_security[key] == "none":
                if value != "none":
                    safety_issues.append(f"Security requirement removed or disabled: {key}")
        
        # Check for performance target relaxation
        old_perf = self._extract_performance_targets(old_config)
        new_perf = self._extract_performance_targets(new_config)
        
        if old_perf.get("response_time_p95") and new_perf.get("response_time_p95"):
            old_time = int(old_perf["response_time_p95"].replace("ms", ""))
            new_time = int(new_perf["response_time_p95"].replace("ms", ""))
            
            if new_time > old_time * 1.5:  # More than 50% increase
                safety_issues.append(f"Performance target significantly relaxed: {old_time}ms → {new_time}ms")
        
        # Check for essential command removal
        old_commands = old_config.get("development_workflow", {}).get("commands", {})
        new_commands = new_config.get("development_workflow", {}).get("commands", {})
        
        essential_commands = ["test", "build", "install"]
        for cmd in essential_commands:
            if cmd in old_commands and cmd not in new_commands:
                safety_issues.append(f"Essential command removed: {cmd}")
        
        is_safe = len(safety_issues) == 0
        return is_safe, safety_issues
    
    def monitor_config_effectiveness(self, usage_metrics: Dict[str, Any]) -> ConfigurationHealth:
        """Monitor how well the configuration serves the project"""
        
        # Calculate health metrics
        setup_time = usage_metrics.get("setup_time_seconds", 0.0)
        dev_satisfaction = usage_metrics.get("developer_satisfaction_score", 0.0)
        framework_utilization = usage_metrics.get("framework_utilization_percent", 0.0)
        quality_achievement = usage_metrics.get("quality_achievement_percent", 0.0)
        performance_achievement = usage_metrics.get("performance_achievement_percent", 0.0)
        error_rate = usage_metrics.get("error_rate_percent", 0.0)
        
        health = ConfigurationHealth(
            setup_time_seconds=setup_time,
            developer_satisfaction_score=dev_satisfaction,
            framework_utilization_percent=framework_utilization,
            quality_achievement_percent=quality_achievement,
            performance_achievement_percent=performance_achievement,
            error_rate_percent=error_rate,
            last_updated=datetime.now().isoformat()
        )
        
        # Save health metrics
        self._save_health_metrics(health)
        
        return health
    
    def analyze_health_trends(self, days_back: int = 30) -> List[HealthTrend]:
        """Analyze configuration health trends over time"""
        health_history = self._load_health_history(days_back)
        
        if len(health_history) < 2:
            return []
        
        trends = []
        current = health_history[-1]
        previous = health_history[0]
        
        metrics = [
            ("setup_time_seconds", "lower_is_better"),
            ("developer_satisfaction_score", "higher_is_better"),
            ("framework_utilization_percent", "higher_is_better"),
            ("quality_achievement_percent", "higher_is_better"),
            ("performance_achievement_percent", "higher_is_better"),
            ("error_rate_percent", "lower_is_better")
        ]
        
        for metric_name, direction in metrics:
            current_val = getattr(current, metric_name)
            previous_val = getattr(previous, metric_name)
            
            if current_val == 0 and previous_val == 0:
                continue
            
            # Calculate trend
            if previous_val == 0:
                trend_direction = "improving" if current_val > 0 else "stable"
                significance = "significant" if current_val > 0 else "negligible"
            else:
                percent_change = abs(current_val - previous_val) / previous_val
                
                if direction == "higher_is_better":
                    trend_direction = "improving" if current_val > previous_val else "declining"
                else:
                    trend_direction = "improving" if current_val < previous_val else "declining"
                
                if current_val == previous_val:
                    trend_direction = "stable"
                
                significance = "significant" if percent_change > 0.1 else "minor" if percent_change > 0.05 else "negligible"
            
            trends.append(HealthTrend(
                metric_name=metric_name,
                current_value=current_val,
                previous_value=previous_val,
                trend_direction=trend_direction,
                significance=significance
            ))
        
        return trends
    
    def generate_optimization_recommendations(self, health: ConfigurationHealth, trends: List[HealthTrend]) -> List[str]:
        """Generate recommendations for configuration optimization"""
        recommendations = []
        
        # Setup time optimization
        if health.setup_time_seconds > 300:  # More than 5 minutes
            recommendations.append("Setup time is high - consider moving to Tier 1 (Minimal) configuration")
        elif health.setup_time_seconds > 120:  # More than 2 minutes
            recommendations.append("Setup time above target - consider using smart defaults for common settings")
        
        # Developer satisfaction
        if health.developer_satisfaction_score < 7.0:
            recommendations.append("Low developer satisfaction - survey team for configuration pain points")
        
        # Framework utilization
        if health.framework_utilization_percent < 60:
            recommendations.append("Low framework utilization - consider training or documentation updates")
        
        # Quality achievement
        if health.quality_achievement_percent < 80:
            recommendations.append("Quality targets not being met - review quality standards configuration")
        
        # Performance achievement
        if health.performance_achievement_percent < 85:
            recommendations.append("Performance targets not being met - consider adjusting targets or optimization")
        
        # Error rate
        if health.error_rate_percent > 5:
            recommendations.append("High configuration error rate - consider adding validation and guidance")
        
        # Trend-based recommendations
        for trend in trends:
            if trend.significance == "significant" and trend.trend_direction == "declining":
                if trend.metric_name == "developer_satisfaction_score":
                    recommendations.append("Developer satisfaction declining - investigate recent configuration changes")
                elif trend.metric_name == "quality_achievement_percent":
                    recommendations.append("Quality achievement declining - review and update quality standards")
                elif trend.metric_name == "performance_achievement_percent":
                    recommendations.append("Performance achievement declining - investigate performance bottlenecks")
        
        return recommendations
    
    def _detect_changes(self, old_config: Optional[Dict[str, Any]], new_config: Dict[str, Any]) -> List[ConfigurationChange]:
        """Detect changes between two configurations"""
        changes = []
        
        if old_config is None:
            # New configuration
            changes.append(ConfigurationChange(
                timestamp=datetime.now().isoformat(),
                change_type=ChangeType.ADDED,
                path="root",
                old_value=None,
                new_value="initial_configuration",
                impact_level=ImpactLevel.HIGH,
                description="Initial configuration created",
                affected_components=["all"]
            ))
            return changes
        
        # Compare configurations recursively
        changes.extend(self._compare_dict(old_config, new_config, ""))
        
        return changes
    
    def _compare_dict(self, old_dict: Dict[str, Any], new_dict: Dict[str, Any], path: str) -> List[ConfigurationChange]:
        """Recursively compare dictionaries for changes"""
        changes = []
        
        # Check for removed keys
        for key in old_dict:
            if key not in new_dict:
                changes.append(ConfigurationChange(
                    timestamp=datetime.now().isoformat(),
                    change_type=ChangeType.REMOVED,
                    path=f"{path}.{key}" if path else key,
                    old_value=str(old_dict[key]),
                    new_value=None,
                    impact_level=self._assess_impact_level(key, old_dict[key], None),
                    description=f"Removed configuration: {key}",
                    affected_components=self._identify_affected_components(key)
                ))
        
        # Check for added or modified keys
        for key in new_dict:
            current_path = f"{path}.{key}" if path else key
            
            if key not in old_dict:
                # Added
                changes.append(ConfigurationChange(
                    timestamp=datetime.now().isoformat(),
                    change_type=ChangeType.ADDED,
                    path=current_path,
                    old_value=None,
                    new_value=str(new_dict[key]),
                    impact_level=self._assess_impact_level(key, None, new_dict[key]),
                    description=f"Added configuration: {key}",
                    affected_components=self._identify_affected_components(key)
                ))
            elif old_dict[key] != new_dict[key]:
                # Modified
                if isinstance(old_dict[key], dict) and isinstance(new_dict[key], dict):
                    # Recursively compare nested dictionaries
                    changes.extend(self._compare_dict(old_dict[key], new_dict[key], current_path))
                else:
                    changes.append(ConfigurationChange(
                        timestamp=datetime.now().isoformat(),
                        change_type=ChangeType.MODIFIED,
                        path=current_path,
                        old_value=str(old_dict[key]),
                        new_value=str(new_dict[key]),
                        impact_level=self._assess_impact_level(key, old_dict[key], new_dict[key]),
                        description=f"Modified configuration: {key}",
                        affected_components=self._identify_affected_components(key)
                    ))
        
        return changes
    
    def _assess_impact_level(self, key: str, old_value: Any, new_value: Any) -> ImpactLevel:
        """Assess the impact level of a configuration change"""
        # Critical impact
        critical_keys = ["test_coverage.threshold", "security_requirements", "authentication"]
        if any(critical_key in key for critical_key in critical_keys):
            return ImpactLevel.CRITICAL
        
        # High impact
        high_impact_keys = ["quality_standards", "performance", "commands"]
        if any(high_key in key for high_key in high_impact_keys):
            return ImpactLevel.HIGH
        
        # Medium impact
        medium_impact_keys = ["project_structure", "domain_specific_rules"]
        if any(medium_key in key for medium_key in medium_impact_keys):
            return ImpactLevel.MEDIUM
        
        # Low impact for everything else
        return ImpactLevel.LOW
    
    def _identify_affected_components(self, key: str) -> List[str]:
        """Identify which framework components are affected by a change"""
        components = []
        
        if "test" in key:
            components.extend(["testing", "quality_gates", "tdd"])
        if "coverage" in key:
            components.extend(["testing", "quality_gates"])
        if "performance" in key:
            components.extend(["quality_gates", "monitoring"])
        if "security" in key:
            components.extend(["security", "quality_gates"])
        if "commands" in key:
            components.extend(["development_workflow", "automation"])
        if "structure" in key:
            components.extend(["file_organization", "navigation"])
        
        return components if components else ["general"]
    
    def _analyze_change_impact(self, changes: List[ConfigurationChange]) -> ChangeImpactAnalysis:
        """Analyze the overall impact of configuration changes"""
        breaking_changes = []
        performance_impact = "none"
        quality_impact = "none"
        security_impact = "none"
        recommended_actions = []
        rollback_complexity = "simple"
        
        # Analyze each change
        for change in changes:
            if change.impact_level == ImpactLevel.CRITICAL:
                breaking_changes.append(change.description)
                rollback_complexity = "complex"
            
            if "performance" in change.path:
                performance_impact = "high" if change.impact_level in [ImpactLevel.CRITICAL, ImpactLevel.HIGH] else "medium"
            
            if "quality" in change.path or "coverage" in change.path:
                quality_impact = "high" if change.impact_level in [ImpactLevel.CRITICAL, ImpactLevel.HIGH] else "medium"
            
            if "security" in change.path:
                security_impact = "high" if change.impact_level in [ImpactLevel.CRITICAL, ImpactLevel.HIGH] else "medium"
        
        # Generate recommendations
        if breaking_changes:
            recommended_actions.append("Test all affected components before deployment")
            recommended_actions.append("Create rollback plan for critical changes")
        
        if performance_impact in ["high", "medium"]:
            recommended_actions.append("Run performance benchmarks to validate changes")
        
        if quality_impact in ["high", "medium"]:
            recommended_actions.append("Verify quality gates still pass with new configuration")
        
        if security_impact in ["high", "medium"]:
            recommended_actions.append("Run security scans to validate security configuration")
        
        return ChangeImpactAnalysis(
            breaking_changes=breaking_changes,
            performance_impact=performance_impact,
            quality_impact=quality_impact,
            security_impact=security_impact,
            recommended_actions=recommended_actions,
            rollback_complexity=rollback_complexity
        )
    
    def _parse_config(self, config_path: Path) -> Dict[str, Any]:
        """Parse XML configuration to dictionary"""
        try:
            tree = ET.parse(config_path)
            root = tree.getroot()
            return self._xml_to_dict(root)
        except (ET.ParseError, FileNotFoundError):
            return {}
    
    def _xml_to_dict(self, element: ET.Element) -> Dict[str, Any]:
        """Convert XML element to dictionary"""
        result = {}
        
        # Add attributes
        if element.attrib:
            result.update(element.attrib)
        
        # Add child elements
        for child in element:
            child_dict = self._xml_to_dict(child)
            if child.tag in result:
                # Handle multiple elements with same tag
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_dict)
            else:
                result[child.tag] = child_dict
        
        # Add text content if no children
        if not list(element) and element.text:
            if result:
                result["_text"] = element.text.strip()
            else:
                return element.text.strip()
        
        return result
    
    def _calculate_config_hash(self, config: Dict[str, Any]) -> str:
        """Calculate hash of configuration for change detection"""
        config_str = json.dumps(config, sort_keys=True)
        return hashlib.sha256(config_str.encode()).hexdigest()
    
    def _get_previous_config(self) -> Optional[Dict[str, Any]]:
        """Get the most recent configuration from history"""
        if not self.history_file.exists():
            return None
        
        try:
            with open(self.history_file, 'r') as f:
                history = json.load(f)
                if history and "current_config" in history:
                    return history["current_config"]
        except (json.JSONDecodeError, FileNotFoundError):
            pass
        
        return None
    
    def _save_change_record(self, change_record: Dict[str, Any]):
        """Save change record to history file"""
        history = {"changes": [], "current_config": {}}
        
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r') as f:
                    history = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        history["changes"].append(change_record)
        
        # Keep only last 100 changes
        if len(history["changes"]) > 100:
            history["changes"] = history["changes"][-100:]
        
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=2)
    
    def _update_current_config(self, config: Dict[str, Any]):
        """Update current configuration in history"""
        history = {"changes": [], "current_config": {}}
        
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r') as f:
                    history = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        history["current_config"] = config
        
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=2)
    
    def _save_health_metrics(self, health: ConfigurationHealth):
        """Save health metrics to file"""
        health_history = []
        
        if self.health_file.exists():
            try:
                with open(self.health_file, 'r') as f:
                    health_history = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        health_history.append(asdict(health))
        
        # Keep only last 90 days of data
        cutoff_date = datetime.now() - timedelta(days=90)
        health_history = [
            h for h in health_history 
            if datetime.fromisoformat(h["last_updated"]) > cutoff_date
        ]
        
        with open(self.health_file, 'w') as f:
            json.dump(health_history, f, indent=2)
    
    def _load_health_history(self, days_back: int) -> List[ConfigurationHealth]:
        """Load health history for trend analysis"""
        if not self.health_file.exists():
            return []
        
        try:
            with open(self.health_file, 'r') as f:
                health_data = json.load(f)
            
            cutoff_date = datetime.now() - timedelta(days=days_back)
            recent_health = [
                ConfigurationHealth(**h) for h in health_data
                if datetime.fromisoformat(h["last_updated"]) > cutoff_date
            ]
            
            return sorted(recent_health, key=lambda h: h.last_updated)
            
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _extract_coverage_threshold(self, config: Dict[str, Any]) -> Optional[int]:
        """Extract test coverage threshold from configuration"""
        try:
            quality = config.get("quality_standards", {})
            coverage = quality.get("test_coverage", {})
            threshold = coverage.get("threshold")
            
            if threshold:
                return int(threshold)
        except (ValueError, KeyError):
            pass
        
        return None
    
    def _extract_performance_targets(self, config: Dict[str, Any]) -> Dict[str, str]:
        """Extract performance targets from configuration"""
        try:
            quality = config.get("quality_standards", {})
            performance = quality.get("performance", {})
            return {
                "response_time_p95": performance.get("response_time_p95", ""),
                "memory_limit": performance.get("memory_limit", "")
            }
        except KeyError:
            return {}


def main():
    """Example usage of the Configuration Monitor"""
    project_root = Path.cwd()
    monitor = ConfigurationMonitor(project_root)
    
    # Example: Track a configuration change
    config_path = project_root / "PROJECT_CONFIG.xml"
    if config_path.exists():
        impact = monitor.track_configuration_change(config_path, "Updated quality standards")
        
        print("Change Impact Analysis:")
        print(f"Breaking Changes: {len(impact.breaking_changes)}")
        print(f"Performance Impact: {impact.performance_impact}")
        print(f"Quality Impact: {impact.quality_impact}")
        print(f"Security Impact: {impact.security_impact}")
        
        if impact.recommended_actions:
            print("\nRecommended Actions:")
            for action in impact.recommended_actions:
                print(f"  - {action}")
    
    # Example: Monitor configuration health
    usage_metrics = {
        "setup_time_seconds": 120.0,
        "developer_satisfaction_score": 8.5,
        "framework_utilization_percent": 75.0,
        "quality_achievement_percent": 92.0,
        "performance_achievement_percent": 88.0,
        "error_rate_percent": 2.0
    }
    
    health = monitor.monitor_config_effectiveness(usage_metrics)
    print(f"\nConfiguration Health Score: {health.developer_satisfaction_score}/10")
    
    # Example: Analyze trends
    trends = monitor.analyze_health_trends(30)
    if trends:
        print("\nHealth Trends (30 days):")
        for trend in trends:
            print(f"  {trend.metric_name}: {trend.trend_direction} ({trend.significance})")


if __name__ == "__main__":
    main()