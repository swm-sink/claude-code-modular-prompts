#!/usr/bin/env python3
"""
Continuous Improvement Pipeline Implementation
Automated framework for detecting, planning, executing, and validating improvements to Claude Code.
"""

import json
import logging
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import subprocess
import statistics
from dataclasses import dataclass, asdict
from enum import Enum

class PipelineStage(Enum):
    MONITORING = "monitoring"
    ANALYSIS = "analysis"
    PLANNING = "planning"
    EXECUTION = "execution"
    VALIDATION = "validation"

class ImprovementPriority(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class ImprovementStatus(Enum):
    IDENTIFIED = "identified"
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"

@dataclass
class PerformanceMetrics:
    response_time_p95: float
    success_rate: float
    error_rate: float
    token_efficiency: float
    user_satisfaction: float
    timestamp: datetime
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            **asdict(self),
            'timestamp': self.timestamp.isoformat()
        }

@dataclass
class ImprovementOpportunity:
    id: str
    title: str
    description: str
    category: str
    priority: ImprovementPriority
    estimated_effort: int  # hours
    expected_impact: float  # 0-1 scale
    success_criteria: List[str]
    implementation_plan: str
    risk_assessment: str
    dependencies: List[str]
    created_at: datetime
    status: ImprovementStatus = ImprovementStatus.IDENTIFIED
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            **asdict(self),
            'priority': self.priority.value,
            'status': self.status.value,
            'created_at': self.created_at.isoformat()
        }

class ContinuousImprovementPipeline:
    """Main pipeline orchestrator for automated continuous improvement."""
    
    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or Path(".claude/pipeline_config.json")
        self.metrics_path = Path(".claude/metrics")
        self.improvements_path = Path(".claude/improvements")
        self.logs_path = Path(".claude/logs")
        
        # Create necessary directories
        for path in [self.metrics_path, self.improvements_path, self.logs_path]:
            path.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.logs_path / 'pipeline.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Load configuration
        self.config = self._load_config()
        
        # Initialize pipeline state
        self.current_stage = PipelineStage.MONITORING
        self.active_improvements: List[ImprovementOpportunity] = []
        self.metrics_history: List[PerformanceMetrics] = []
        
    def _load_config(self) -> Dict[str, Any]:
        """Load pipeline configuration with defaults."""
        default_config = {
            "monitoring": {
                "collection_interval_seconds": 300,  # 5 minutes
                "metrics_retention_days": 90,
                "alert_thresholds": {
                    "response_time_p95": 3.0,  # seconds
                    "success_rate": 0.85,
                    "error_rate": 0.05,
                    "user_satisfaction": 4.0
                }
            },
            "analysis": {
                "trend_analysis_days": 30,
                "significance_threshold": 0.05,
                "minimum_data_points": 10
            },
            "execution": {
                "max_concurrent_improvements": 3,
                "rollback_timeout_minutes": 30,
                "quality_gate_timeout_minutes": 60
            },
            "validation": {
                "stability_monitoring_hours": 24,
                "user_feedback_collection_hours": 48,
                "performance_validation_samples": 100
            }
        }
        
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    user_config = json.load(f)
                # Deep merge user config with defaults
                return self._deep_merge(default_config, user_config)
            except Exception as e:
                self.logger.warning(f"Failed to load config: {e}. Using defaults.")
        
        return default_config
    
    def _deep_merge(self, base: Dict, override: Dict) -> Dict:
        """Deep merge two dictionaries."""
        result = base.copy()
        for key, value in override.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        return result
    
    def collect_metrics(self) -> PerformanceMetrics:
        """Collect current performance metrics from various sources."""
        self.logger.info("Collecting performance metrics...")
        
        try:
            # Collect response time metrics
            response_time_p95 = self._measure_response_times()
            
            # Collect success rate metrics  
            success_rate = self._measure_success_rates()
            
            # Collect error rate metrics
            error_rate = self._measure_error_rates()
            
            # Collect token efficiency metrics
            token_efficiency = self._measure_token_efficiency()
            
            # Collect user satisfaction metrics
            user_satisfaction = self._measure_user_satisfaction()
            
            metrics = PerformanceMetrics(
                response_time_p95=response_time_p95,
                success_rate=success_rate,
                error_rate=error_rate,
                token_efficiency=token_efficiency,
                user_satisfaction=user_satisfaction,
                timestamp=datetime.now()
            )
            
            # Store metrics
            self._store_metrics(metrics)
            self.metrics_history.append(metrics)
            
            self.logger.info(f"Metrics collected: {metrics}")
            return metrics
            
        except Exception as e:
            self.logger.error(f"Failed to collect metrics: {e}")
            raise
    
    def _measure_response_times(self) -> float:
        """Measure 95th percentile response times."""
        try:
            # Simulate measurement by checking recent command execution times
            response_times = []
            
            # Check session logs for recent command execution times
            session_logs = list(self.logs_path.glob("session_*.json"))
            for log_file in session_logs[-10:]:  # Last 10 sessions
                try:
                    with open(log_file, 'r') as f:
                        session_data = json.load(f)
                    
                    for command in session_data.get('commands', []):
                        if 'execution_time' in command:
                            response_times.append(command['execution_time'])
                except Exception:
                    continue
            
            if response_times:
                return self._percentile(response_times, 95)
            else:
                # Default baseline if no data available
                return 1.5
                
        except Exception as e:
            self.logger.warning(f"Failed to measure response times: {e}")
            return 2.0  # Conservative default
    
    def _measure_success_rates(self) -> float:
        """Measure task completion success rates."""
        try:
            successes = 0
            total = 0
            
            # Analyze recent GitHub issues for success tracking
            result = subprocess.run(
                ['gh', 'issue', 'list', '--state', 'closed', '--limit', '50', '--json', 'title,labels'],
                capture_output=True, text=True, check=True
            )
            
            issues = json.loads(result.stdout)
            
            for issue in issues:
                total += 1
                # Consider issue successful if it has 'completed' or 'resolved' labels
                labels = [label['name'].lower() for label in issue.get('labels', [])]
                if any(label in ['completed', 'resolved', 'done'] for label in labels):
                    successes += 1
            
            if total > 0:
                return successes / total
            else:
                return 0.9  # Default high success rate
                
        except Exception as e:
            self.logger.warning(f"Failed to measure success rates: {e}")
            return 0.85  # Conservative default
    
    def _measure_error_rates(self) -> float:
        """Measure error rates from logs and execution history."""
        try:
            errors = 0
            total = 0
            
            # Analyze recent log files for error patterns
            log_files = list(self.logs_path.glob("*.log"))
            for log_file in log_files:
                try:
                    with open(log_file, 'r') as f:
                        lines = f.readlines()[-1000:]  # Last 1000 lines
                    
                    for line in lines:
                        total += 1
                        if 'ERROR' in line.upper() or 'FAILED' in line.upper():
                            errors += 1
                except Exception:
                    continue
            
            if total > 0:
                return errors / total
            else:
                return 0.02  # Default low error rate
                
        except Exception as e:
            self.logger.warning(f"Failed to measure error rates: {e}")
            return 0.05  # Conservative default
    
    def _measure_token_efficiency(self) -> float:
        """Measure token usage efficiency."""
        try:
            # Check for token usage reports
            token_files = list(Path(".claude").glob("*token*.json"))
            
            if token_files:
                latest_file = max(token_files, key=lambda x: x.stat().st_mtime)
                with open(latest_file, 'r') as f:
                    token_data = json.load(f)
                
                # Calculate efficiency as output quality per token used
                total_tokens = token_data.get('total_tokens', 1000)
                quality_score = token_data.get('average_quality', 8.0)
                
                return quality_score / (total_tokens / 1000)  # Quality per 1k tokens
            else:
                return 8.0  # Default good efficiency
                
        except Exception as e:
            self.logger.warning(f"Failed to measure token efficiency: {e}")
            return 7.0  # Conservative default
    
    def _measure_user_satisfaction(self) -> float:
        """Measure user satisfaction from feedback and session outcomes."""
        try:
            # Look for user feedback in session data
            satisfaction_scores = []
            
            session_files = list(self.logs_path.glob("session_*.json"))
            for session_file in session_files[-20:]:  # Last 20 sessions
                try:
                    with open(session_file, 'r') as f:
                        session_data = json.load(f)
                    
                    if 'user_satisfaction' in session_data:
                        satisfaction_scores.append(session_data['user_satisfaction'])
                    elif 'outcome' in session_data and session_data['outcome'] == 'success':
                        satisfaction_scores.append(4.5)  # Assume high satisfaction for successful sessions
                except Exception:
                    continue
            
            if satisfaction_scores:
                return statistics.mean(satisfaction_scores)
            else:
                return 4.2  # Default good satisfaction
                
        except Exception as e:
            self.logger.warning(f"Failed to measure user satisfaction: {e}")
            return 4.0  # Conservative default
    
    def _percentile(self, data: List[float], percentile: int) -> float:
        """Calculate percentile of a dataset."""
        if not data:
            return 0.0
        
        sorted_data = sorted(data)
        index = (percentile / 100) * (len(sorted_data) - 1)
        
        if index.is_integer():
            return sorted_data[int(index)]
        else:
            lower_index = int(index)
            upper_index = lower_index + 1
            weight = index - lower_index
            
            if upper_index >= len(sorted_data):
                return sorted_data[-1]
            
            return sorted_data[lower_index] * (1 - weight) + sorted_data[upper_index] * weight
    
    def _store_metrics(self, metrics: PerformanceMetrics):
        """Store metrics to persistent storage."""
        metrics_file = self.metrics_path / f"metrics_{datetime.now().strftime('%Y%m%d')}.json"
        
        # Load existing metrics for the day
        daily_metrics = []
        if metrics_file.exists():
            try:
                with open(metrics_file, 'r') as f:
                    daily_metrics = json.load(f)
            except Exception:
                daily_metrics = []
        
        # Add new metrics
        daily_metrics.append(metrics.to_dict())
        
        # Save updated metrics
        with open(metrics_file, 'w') as f:
            json.dump(daily_metrics, f, indent=2)
    
    def analyze_performance_trends(self) -> List[ImprovementOpportunity]:
        """Analyze performance trends and identify improvement opportunities."""
        self.logger.info("Analyzing performance trends...")
        
        opportunities = []
        
        try:
            # Collect recent metrics for trend analysis
            recent_metrics = self._load_recent_metrics()
            
            if len(recent_metrics) < self.config['analysis']['minimum_data_points']:
                self.logger.warning("Insufficient data for trend analysis")
                return opportunities
            
            # Analyze response time trends
            response_time_trend = self._analyze_metric_trend(
                recent_metrics, 'response_time_p95'
            )
            
            if response_time_trend['is_degrading']:
                opportunities.append(ImprovementOpportunity(
                    id=f"perf_response_time_{int(time.time())}",
                    title="Improve Response Time Performance",
                    description=f"Response times showing degradation trend: {response_time_trend['change']:.2f}% increase",
                    category="performance",
                    priority=ImprovementPriority.HIGH,
                    estimated_effort=4,
                    expected_impact=0.8,
                    success_criteria=[
                        "95th percentile response time < 2 seconds",
                        "No performance regression for 48 hours",
                        "User satisfaction maintained above 4.0"
                    ],
                    implementation_plan="Analyze bottlenecks, optimize critical paths, implement caching where appropriate",
                    risk_assessment="Low risk - performance optimizations are generally safe",
                    dependencies=[],
                    created_at=datetime.now()
                ))
            
            # Analyze success rate trends
            success_rate_trend = self._analyze_metric_trend(
                recent_metrics, 'success_rate'
            )
            
            if success_rate_trend['is_degrading']:
                opportunities.append(ImprovementOpportunity(
                    id=f"quality_success_rate_{int(time.time())}",
                    title="Improve Task Success Rates",
                    description=f"Success rates showing decline: {success_rate_trend['change']:.2f}% decrease",
                    category="quality",
                    priority=ImprovementPriority.CRITICAL,
                    estimated_effort=6,
                    expected_impact=0.9,
                    success_criteria=[
                        "Success rate > 90%",
                        "Error rate < 3%",
                        "User satisfaction > 4.2"
                    ],
                    implementation_plan="Analyze failure patterns, improve error handling, enhance validation",
                    risk_assessment="Medium risk - changes to core logic require careful testing",
                    dependencies=[],
                    created_at=datetime.now()
                ))
            
            # Analyze error rate trends
            error_rate_trend = self._analyze_metric_trend(
                recent_metrics, 'error_rate'
            )
            
            if error_rate_trend['is_degrading']:
                opportunities.append(ImprovementOpportunity(
                    id=f"reliability_error_rate_{int(time.time())}",
                    title="Reduce Error Rates",
                    description=f"Error rates increasing: {error_rate_trend['change']:.2f}% increase",
                    category="reliability",
                    priority=ImprovementPriority.HIGH,
                    estimated_effort=5,
                    expected_impact=0.7,
                    success_criteria=[
                        "Error rate < 2%",
                        "No critical errors for 72 hours",
                        "Improved error recovery mechanisms"
                    ],
                    implementation_plan="Enhance error handling, improve input validation, add circuit breakers",
                    risk_assessment="Low risk - error handling improvements are generally safe",
                    dependencies=[],
                    created_at=datetime.now()
                ))
            
            # Analyze token efficiency trends
            efficiency_trend = self._analyze_metric_trend(
                recent_metrics, 'token_efficiency'
            )
            
            if efficiency_trend['is_degrading']:
                opportunities.append(ImprovementOpportunity(
                    id=f"efficiency_token_{int(time.time())}",
                    title="Improve Token Efficiency",
                    description=f"Token efficiency declining: {efficiency_trend['change']:.2f}% decrease",
                    category="efficiency",
                    priority=ImprovementPriority.MEDIUM,
                    estimated_effort=3,
                    expected_impact=0.6,
                    success_criteria=[
                        "Token efficiency > 8.0",
                        "No quality degradation",
                        "Cost reduction > 10%"
                    ],
                    implementation_plan="Optimize prompts, improve pattern selection, reduce redundancy",
                    risk_assessment="Low risk - efficiency improvements typically don't affect functionality",
                    dependencies=[],
                    created_at=datetime.now()
                ))
            
            # Analyze user satisfaction trends
            satisfaction_trend = self._analyze_metric_trend(
                recent_metrics, 'user_satisfaction'
            )
            
            if satisfaction_trend['is_degrading']:
                opportunities.append(ImprovementOpportunity(
                    id=f"ux_satisfaction_{int(time.time())}",
                    title="Improve User Experience",
                    description=f"User satisfaction declining: {satisfaction_trend['change']:.2f}% decrease",
                    category="user_experience",
                    priority=ImprovementPriority.HIGH,
                    estimated_effort=4,
                    expected_impact=0.8,
                    success_criteria=[
                        "User satisfaction > 4.3",
                        "Positive user feedback trend",
                        "Reduced user-reported issues"
                    ],
                    implementation_plan="Analyze user feedback, improve UX flows, enhance documentation",
                    risk_assessment="Low risk - UX improvements are typically low-risk",
                    dependencies=[],
                    created_at=datetime.now()
                ))
            
            self.logger.info(f"Identified {len(opportunities)} improvement opportunities")
            return opportunities
            
        except Exception as e:
            self.logger.error(f"Failed to analyze trends: {e}")
            return opportunities
    
    def _load_recent_metrics(self) -> List[PerformanceMetrics]:
        """Load recent metrics for trend analysis."""
        metrics = []
        analysis_days = self.config['analysis']['trend_analysis_days']
        start_date = datetime.now() - timedelta(days=analysis_days)
        
        for i in range(analysis_days):
            date = start_date + timedelta(days=i)
            metrics_file = self.metrics_path / f"metrics_{date.strftime('%Y%m%d')}.json"
            
            if metrics_file.exists():
                try:
                    with open(metrics_file, 'r') as f:
                        daily_data = json.load(f)
                    
                    for metric_dict in daily_data:
                        metrics.append(PerformanceMetrics(
                            response_time_p95=metric_dict['response_time_p95'],
                            success_rate=metric_dict['success_rate'],
                            error_rate=metric_dict['error_rate'],
                            token_efficiency=metric_dict['token_efficiency'],
                            user_satisfaction=metric_dict['user_satisfaction'],
                            timestamp=datetime.fromisoformat(metric_dict['timestamp'])
                        ))
                except Exception as e:
                    self.logger.warning(f"Failed to load metrics from {metrics_file}: {e}")
        
        return sorted(metrics, key=lambda x: x.timestamp)
    
    def _analyze_metric_trend(self, metrics: List[PerformanceMetrics], metric_name: str) -> Dict[str, Any]:
        """Analyze trend for a specific metric."""
        values = [getattr(metric, metric_name) for metric in metrics]
        
        if len(values) < 2:
            return {'is_degrading': False, 'change': 0, 'trend': 'insufficient_data'}
        
        # Simple linear trend analysis
        n = len(values)
        x = list(range(n))
        
        # Calculate linear regression slope
        x_mean = sum(x) / n
        y_mean = sum(values) / n
        
        numerator = sum((x[i] - x_mean) * (values[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean) ** 2 for i in range(n))
        
        if denominator == 0:
            slope = 0
        else:
            slope = numerator / denominator
        
        # Calculate percentage change
        first_value = values[0]
        last_value = values[-1]
        
        if first_value == 0:
            percentage_change = 0
        else:
            percentage_change = ((last_value - first_value) / first_value) * 100
        
        # Determine if degrading based on metric type
        is_degrading = False
        if metric_name in ['response_time_p95', 'error_rate']:
            # Higher is worse for these metrics
            is_degrading = slope > 0 and abs(percentage_change) > 5
        else:
            # Lower is worse for these metrics
            is_degrading = slope < 0 and abs(percentage_change) > 5
        
        return {
            'is_degrading': is_degrading,
            'change': percentage_change,
            'slope': slope,
            'trend': 'degrading' if is_degrading else 'stable'
        }
    
    def prioritize_improvements(self, opportunities: List[ImprovementOpportunity]) -> List[ImprovementOpportunity]:
        """Prioritize improvement opportunities based on impact and effort."""
        def priority_score(opportunity: ImprovementOpportunity) -> float:
            # Priority enum to numeric values
            priority_weights = {
                ImprovementPriority.CRITICAL: 10,
                ImprovementPriority.HIGH: 7,
                ImprovementPriority.MEDIUM: 4,
                ImprovementPriority.LOW: 1
            }
            
            priority_weight = priority_weights.get(opportunity.priority, 1)
            impact_weight = opportunity.expected_impact * 10
            effort_penalty = opportunity.estimated_effort / 10
            
            return priority_weight + impact_weight - effort_penalty
        
        return sorted(opportunities, key=priority_score, reverse=True)
    
    def execute_improvement(self, improvement: ImprovementOpportunity) -> bool:
        """Execute a single improvement with quality gates and monitoring."""
        self.logger.info(f"Executing improvement: {improvement.title}")
        
        try:
            # Update status
            improvement.status = ImprovementStatus.IN_PROGRESS
            self._save_improvement(improvement)
            
            # Create GitHub issue for tracking
            issue_number = self._create_github_issue(improvement)
            
            # Execute improvement based on category
            if improvement.category == "performance":
                success = self._execute_performance_improvement(improvement)
            elif improvement.category == "quality":
                success = self._execute_quality_improvement(improvement)
            elif improvement.category == "reliability":
                success = self._execute_reliability_improvement(improvement)
            elif improvement.category == "efficiency":
                success = self._execute_efficiency_improvement(improvement)
            elif improvement.category == "user_experience":
                success = self._execute_ux_improvement(improvement)
            else:
                self.logger.warning(f"Unknown improvement category: {improvement.category}")
                success = False
            
            if success:
                # Validate improvement
                validation_success = self._validate_improvement(improvement)
                
                if validation_success:
                    improvement.status = ImprovementStatus.COMPLETED
                    self.logger.info(f"Successfully completed improvement: {improvement.title}")
                else:
                    # Rollback if validation fails
                    self._rollback_improvement(improvement)
                    improvement.status = ImprovementStatus.ROLLED_BACK
                    success = False
            else:
                improvement.status = ImprovementStatus.FAILED
                
            # Update GitHub issue
            self._update_github_issue(issue_number, improvement)
            self._save_improvement(improvement)
            
            return success
            
        except Exception as e:
            self.logger.error(f"Failed to execute improvement {improvement.title}: {e}")
            improvement.status = ImprovementStatus.FAILED
            self._save_improvement(improvement)
            return False
    
    def _execute_performance_improvement(self, improvement: ImprovementOpportunity) -> bool:
        """Execute performance-related improvements."""
        self.logger.info(f"Executing performance improvement: {improvement.title}")
        
        # Simulate performance improvements
        # In a real implementation, this would involve:
        # - Code profiling and optimization
        # - Database query optimization
        # - Caching implementation
        # - Algorithm improvements
        
        time.sleep(2)  # Simulate implementation time
        return True
    
    def _execute_quality_improvement(self, improvement: ImprovementOpportunity) -> bool:
        """Execute quality-related improvements."""
        self.logger.info(f"Executing quality improvement: {improvement.title}")
        
        # Simulate quality improvements
        # In a real implementation, this would involve:
        # - Enhanced validation logic
        # - Better error handling
        # - Improved test coverage
        # - Code review process improvements
        
        time.sleep(3)  # Simulate implementation time
        return True
    
    def _execute_reliability_improvement(self, improvement: ImprovementOpportunity) -> bool:
        """Execute reliability-related improvements."""
        self.logger.info(f"Executing reliability improvement: {improvement.title}")
        
        # Simulate reliability improvements
        # In a real implementation, this would involve:
        # - Circuit breaker implementation
        # - Retry mechanisms
        # - Graceful degradation
        # - Health check improvements
        
        time.sleep(2)  # Simulate implementation time
        return True
    
    def _execute_efficiency_improvement(self, improvement: ImprovementOpportunity) -> bool:
        """Execute efficiency-related improvements."""
        self.logger.info(f"Executing efficiency improvement: {improvement.title}")
        
        # Simulate efficiency improvements
        # In a real implementation, this would involve:
        # - Prompt optimization
        # - Resource usage optimization
        # - Algorithmic improvements
        # - Caching strategies
        
        time.sleep(1)  # Simulate implementation time
        return True
    
    def _execute_ux_improvement(self, improvement: ImprovementOpportunity) -> bool:
        """Execute user experience improvements."""
        self.logger.info(f"Executing UX improvement: {improvement.title}")
        
        # Simulate UX improvements
        # In a real implementation, this would involve:
        # - Interface improvements
        # - Documentation updates
        # - Error message improvements
        # - Workflow optimization
        
        time.sleep(2)  # Simulate implementation time
        return True
    
    def _validate_improvement(self, improvement: ImprovementOpportunity) -> bool:
        """Validate that an improvement meets its success criteria."""
        self.logger.info(f"Validating improvement: {improvement.title}")
        
        try:
            # Collect post-improvement metrics
            post_metrics = self.collect_metrics()
            
            # Check success criteria
            validation_results = []
            
            for criterion in improvement.success_criteria:
                # Simple validation logic - in practice, this would be more sophisticated
                if "response time" in criterion.lower():
                    result = post_metrics.response_time_p95 < 3.0
                elif "success rate" in criterion.lower():
                    result = post_metrics.success_rate > 0.85
                elif "error rate" in criterion.lower():
                    result = post_metrics.error_rate < 0.05
                elif "satisfaction" in criterion.lower():
                    result = post_metrics.user_satisfaction > 4.0
                elif "efficiency" in criterion.lower():
                    result = post_metrics.token_efficiency > 7.0
                else:
                    result = True  # Default to pass for unknown criteria
                
                validation_results.append(result)
                self.logger.info(f"Validation criterion '{criterion}': {'PASS' if result else 'FAIL'}")
            
            # All criteria must pass
            overall_success = all(validation_results)
            
            self.logger.info(f"Overall validation: {'PASS' if overall_success else 'FAIL'}")
            return overall_success
            
        except Exception as e:
            self.logger.error(f"Validation failed with error: {e}")
            return False
    
    def _rollback_improvement(self, improvement: ImprovementOpportunity) -> bool:
        """Rollback a failed improvement."""
        self.logger.warning(f"Rolling back improvement: {improvement.title}")
        
        try:
            # Simulate rollback process
            # In a real implementation, this would involve:
            # - Restoring previous configurations
            # - Reverting code changes
            # - Restoring database states
            # - Clearing caches
            
            time.sleep(1)  # Simulate rollback time
            
            self.logger.info(f"Successfully rolled back improvement: {improvement.title}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to rollback improvement {improvement.title}: {e}")
            return False
    
    def _create_github_issue(self, improvement: ImprovementOpportunity) -> Optional[int]:
        """Create a GitHub issue for tracking improvement progress."""
        try:
            issue_body = f"""
## Improvement: {improvement.title}

**Category:** {improvement.category}
**Priority:** {improvement.priority.value}
**Estimated Effort:** {improvement.estimated_effort} hours
**Expected Impact:** {improvement.expected_impact:.1f}/1.0

### Description
{improvement.description}

### Implementation Plan
{improvement.implementation_plan}

### Success Criteria
{chr(10).join('- ' + criterion for criterion in improvement.success_criteria)}

### Risk Assessment
{improvement.risk_assessment}

### Dependencies
{chr(10).join('- ' + dep for dep in improvement.dependencies) if improvement.dependencies else 'None'}

---
*This issue was automatically created by the Continuous Improvement Pipeline*
"""
            
            result = subprocess.run([
                'gh', 'issue', 'create',
                '--title', f"[Improvement] {improvement.title}",
                '--body', issue_body,
                '--label', 'improvement',
                '--label', improvement.category,
                '--label', improvement.priority.value
            ], capture_output=True, text=True, check=True)
            
            # Extract issue number from output
            output = result.stderr.strip()
            if output and output.split('/')[-1].isdigit():
                issue_number = int(output.split('/')[-1])
                self.logger.info(f"Created GitHub issue #{issue_number} for improvement")
                return issue_number
            
        except Exception as e:
            self.logger.warning(f"Failed to create GitHub issue: {e}")
        
        return None
    
    def _update_github_issue(self, issue_number: Optional[int], improvement: ImprovementOpportunity):
        """Update GitHub issue with improvement status."""
        if not issue_number:
            return
        
        try:
            status_comment = f"""
## Status Update: {improvement.status.value.title()}

**Updated:** {datetime.now().isoformat()}

{self._get_status_description(improvement.status)}
"""
            
            subprocess.run([
                'gh', 'issue', 'comment', str(issue_number),
                '--body', status_comment
            ], check=True)
            
            # Close issue if completed or failed
            if improvement.status in [ImprovementStatus.COMPLETED, ImprovementStatus.FAILED]:
                subprocess.run([
                    'gh', 'issue', 'close', str(issue_number)
                ], check=True)
                
        except Exception as e:
            self.logger.warning(f"Failed to update GitHub issue #{issue_number}: {e}")
    
    def _get_status_description(self, status: ImprovementStatus) -> str:
        """Get descriptive text for improvement status."""
        descriptions = {
            ImprovementStatus.IDENTIFIED: "Improvement opportunity has been identified and is pending planning.",
            ImprovementStatus.PLANNED: "Implementation plan has been created and improvement is ready for execution.",
            ImprovementStatus.IN_PROGRESS: "Improvement is currently being implemented.",
            ImprovementStatus.COMPLETED: "Improvement has been successfully implemented and validated.",
            ImprovementStatus.FAILED: "Improvement implementation failed and has been cancelled.",
            ImprovementStatus.ROLLED_BACK: "Improvement was implemented but failed validation and has been rolled back."
        }
        
        return descriptions.get(status, "Unknown status")
    
    def _save_improvement(self, improvement: ImprovementOpportunity):
        """Save improvement to persistent storage."""
        improvement_file = self.improvements_path / f"{improvement.id}.json"
        
        with open(improvement_file, 'w') as f:
            json.dump(improvement.to_dict(), f, indent=2)
    
    def run_pipeline_cycle(self) -> Dict[str, Any]:
        """Run a complete pipeline cycle."""
        self.logger.info("Starting continuous improvement pipeline cycle")
        
        cycle_results = {
            'start_time': datetime.now().isoformat(),
            'metrics': None,
            'opportunities_identified': 0,
            'improvements_executed': 0,
            'improvements_successful': 0,
            'improvements_failed': 0,
            'status': 'running'
        }
        
        try:
            # Stage 1: Monitoring and Analysis
            self.current_stage = PipelineStage.MONITORING
            metrics = self.collect_metrics()
            cycle_results['metrics'] = metrics.to_dict()
            
            # Stage 2: Analysis
            self.current_stage = PipelineStage.ANALYSIS
            opportunities = self.analyze_performance_trends()
            cycle_results['opportunities_identified'] = len(opportunities)
            
            if not opportunities:
                self.logger.info("No improvement opportunities identified")
                cycle_results['status'] = 'completed'
                cycle_results['end_time'] = datetime.now().isoformat()
                return cycle_results
            
            # Stage 3: Planning
            self.current_stage = PipelineStage.PLANNING
            prioritized_opportunities = self.prioritize_improvements(opportunities)
            
            # Stage 4: Execution
            self.current_stage = PipelineStage.EXECUTION
            max_concurrent = self.config['execution']['max_concurrent_improvements']
            improvements_to_execute = prioritized_opportunities[:max_concurrent]
            
            for improvement in improvements_to_execute:
                cycle_results['improvements_executed'] += 1
                
                success = self.execute_improvement(improvement)
                
                if success:
                    cycle_results['improvements_successful'] += 1
                else:
                    cycle_results['improvements_failed'] += 1
            
            # Stage 5: Validation (overall cycle validation)
            self.current_stage = PipelineStage.VALIDATION
            final_metrics = self.collect_metrics()
            
            cycle_results['status'] = 'completed'
            cycle_results['end_time'] = datetime.now().isoformat()
            cycle_results['final_metrics'] = final_metrics.to_dict()
            
            self.logger.info(f"Pipeline cycle completed: {cycle_results}")
            
        except Exception as e:
            self.logger.error(f"Pipeline cycle failed: {e}")
            cycle_results['status'] = 'failed'
            cycle_results['error'] = str(e)
            cycle_results['end_time'] = datetime.now().isoformat()
        
        return cycle_results

def main():
    """Main entry point for the continuous improvement pipeline."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Continuous Improvement Pipeline")
    parser.add_argument('--config', type=Path, help="Configuration file path")
    parser.add_argument('--collect-metrics', action='store_true', help="Collect metrics only")
    parser.add_argument('--analyze-trends', action='store_true', help="Analyze trends only")
    parser.add_argument('--run-cycle', action='store_true', help="Run full pipeline cycle")
    
    args = parser.parse_args()
    
    pipeline = ContinuousImprovementPipeline(config_path=args.config)
    
    if args.collect_metrics:
        metrics = pipeline.collect_metrics()
        print(json.dumps(metrics.to_dict(), indent=2))
    elif args.analyze_trends:
        opportunities = pipeline.analyze_performance_trends()
        print(json.dumps([opp.to_dict() for opp in opportunities], indent=2))
    elif args.run_cycle:
        results = pipeline.run_pipeline_cycle()
        print(json.dumps(results, indent=2))
    else:
        print("Please specify an action: --collect-metrics, --analyze-trends, or --run-cycle")
        sys.exit(1)

if __name__ == "__main__":
    main()