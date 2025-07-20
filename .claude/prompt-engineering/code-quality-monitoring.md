# Code Quality Monitoring

| version | last_updated | status | agent |
|---------|--------------|--------|--------|
| 1.0.0   | 2025-07-20   | production | I28 |

## Purpose

Continuous quality tracking system that monitors mutation scores, test effectiveness, architecture compliance, and trends to provide real-time insights into code health and quality evolution.

## Mutation Score Tracking

### Advanced Mutation Testing Engine

```python
class MutationScoreTracker:
    """Advanced mutation testing with intelligent operator selection"""
    
    def __init__(self):
        self.mutation_operators = {
            'arithmetic': ['+', '-', '*', '/', '%', '**'],
            'relational': ['==', '!=', '<', '>', '<=', '>='],
            'logical': ['and', 'or', 'not'],
            'conditional': ['if', 'elif', 'else'],
            'assignment': ['=', '+=', '-=', '*=', '/='],
            'boundary': ['range_boundaries', 'list_boundaries'],
            'method_calls': ['method_deletion', 'return_modification']
        }
        
        self.intelligent_selection = True
        self.coverage_guided = True
        self.performance_optimized = True
    
    def run_mutation_testing(self, target_files, test_files):
        """Run comprehensive mutation testing"""
        # Phase 1: Coverage analysis to guide mutation placement
        coverage_data = self._analyze_test_coverage(target_files, test_files)
        
        # Phase 2: Intelligent mutation operator selection
        mutation_candidates = self._select_mutation_candidates(target_files, coverage_data)
        
        # Phase 3: Execute mutations with parallel processing
        mutation_results = self._execute_mutations_parallel(mutation_candidates, test_files)
        
        # Phase 4: Analyze results and calculate scores
        analysis = self._analyze_mutation_results(mutation_results)
        
        return {
            'overall_score': analysis['mutation_score'],
            'detailed_scores': analysis['per_file_scores'],
            'weak_areas': analysis['low_quality_areas'],
            'strong_areas': analysis['high_quality_areas'],
            'improvement_suggestions': analysis['suggestions'],
            'trend_data': self._compare_with_historical(analysis),
            'quality_gates': self._evaluate_quality_gates(analysis)
        }
    
    def _select_mutation_candidates(self, target_files, coverage_data):
        """Intelligently select mutation points based on coverage and code analysis"""
        candidates = []
        
        for file_path in target_files:
            ast_analysis = self._analyze_ast_structure(file_path)
            
            # Focus on covered code that's actually tested
            covered_lines = coverage_data['files'][file_path]['covered_lines']
            
            for node in ast_analysis['nodes']:
                if node['line_number'] in covered_lines:
                    # Determine best mutation operators for this node
                    applicable_operators = self._get_applicable_operators(node)
                    
                    for operator in applicable_operators:
                        candidates.append({
                            'file': file_path,
                            'line': node['line_number'],
                            'column': node['column'],
                            'original_code': node['code'],
                            'mutation_operator': operator,
                            'mutated_code': self._apply_mutation(node['code'], operator),
                            'expected_impact': self._estimate_impact(node, operator),
                            'priority': self._calculate_priority(node, operator, coverage_data)
                        })
        
        # Sort by priority and select top candidates
        candidates.sort(key=lambda x: x['priority'], reverse=True)
        return candidates[:self._calculate_optimal_mutation_count(len(candidates))]
    
    def _execute_mutations_parallel(self, candidates, test_files):
        """Execute mutations in parallel for performance"""
        from concurrent.futures import ThreadPoolExecutor, as_completed
        import tempfile
        import shutil
        
        results = []
        
        with ThreadPoolExecutor(max_workers=4) as executor:
            future_to_mutation = {}
            
            for candidate in candidates:
                future = executor.submit(self._execute_single_mutation, candidate, test_files)
                future_to_mutation[future] = candidate
            
            for future in as_completed(future_to_mutation):
                candidate = future_to_mutation[future]
                try:
                    result = future.result()
                    result['candidate'] = candidate
                    results.append(result)
                except Exception as exc:
                    results.append({
                        'candidate': candidate,
                        'status': 'error',
                        'error': str(exc),
                        'killed': False
                    })
        
        return results
    
    def _execute_single_mutation(self, candidate, test_files):
        """Execute a single mutation and run tests"""
        import tempfile
        import subprocess
        import shutil
        import os
        
        # Create temporary copy of file with mutation
        original_file = candidate['file']
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
            # Apply mutation to file content
            with open(original_file, 'r') as f:
                original_content = f.read()
            
            mutated_content = self._apply_mutation_to_content(
                original_content, 
                candidate['line'], 
                candidate['mutation_operator'],
                candidate['mutated_code']
            )
            
            temp_file.write(mutated_content)
            temp_file_path = temp_file.name
        
        try:
            # Temporarily replace original file
            backup_path = f"{original_file}.backup"
            shutil.copy2(original_file, backup_path)
            shutil.copy2(temp_file_path, original_file)
            
            # Run tests
            test_result = self._run_tests_for_mutation(test_files)
            
            # Restore original file
            shutil.copy2(backup_path, original_file)
            os.remove(backup_path)
            
            return {
                'status': 'completed',
                'killed': not test_result['all_passed'],
                'test_results': test_result,
                'execution_time': test_result['execution_time']
            }
            
        except Exception as e:
            # Ensure original file is restored
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, original_file)
                os.remove(backup_path)
            
            raise e
        
        finally:
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
    
    def _analyze_mutation_results(self, results):
        """Analyze mutation testing results for insights"""
        total_mutations = len(results)
        killed_mutations = len([r for r in results if r.get('killed', False)])
        
        mutation_score = killed_mutations / total_mutations if total_mutations > 0 else 0
        
        # Per-file analysis
        file_scores = {}
        for result in results:
            file_path = result['candidate']['file']
            if file_path not in file_scores:
                file_scores[file_path] = {'total': 0, 'killed': 0}
            
            file_scores[file_path]['total'] += 1
            if result.get('killed', False):
                file_scores[file_path]['killed'] += 1
        
        # Calculate per-file scores
        for file_path in file_scores:
            file_data = file_scores[file_path]
            file_data['score'] = file_data['killed'] / file_data['total'] if file_data['total'] > 0 else 0
        
        # Identify weak areas (low mutation scores)
        weak_areas = [
            {
                'file': file_path,
                'score': data['score'],
                'mutations_survived': data['total'] - data['killed']
            }
            for file_path, data in file_scores.items()
            if data['score'] < 0.7  # Threshold for weak areas
        ]
        
        # Generate improvement suggestions
        suggestions = self._generate_mutation_improvement_suggestions(results, weak_areas)
        
        return {
            'mutation_score': mutation_score,
            'per_file_scores': file_scores,
            'low_quality_areas': weak_areas,
            'high_quality_areas': [
                {'file': f, 'score': d['score']} 
                for f, d in file_scores.items() 
                if d['score'] >= 0.9
            ],
            'suggestions': suggestions,
            'total_mutations': total_mutations,
            'killed_mutations': killed_mutations
        }
```

### Test Effectiveness Monitoring

```python
class TestEffectivenessMonitor:
    """Monitor and analyze test suite effectiveness"""
    
    def __init__(self):
        self.metrics = {
            'coverage_metrics': CoverageAnalyzer(),
            'assertion_quality': AssertionQualityAnalyzer(),
            'test_isolation': TestIsolationAnalyzer(),
            'performance_metrics': TestPerformanceAnalyzer(),
            'maintainability': TestMaintainabilityAnalyzer()
        }
    
    def analyze_test_effectiveness(self, test_directory):
        """Comprehensive test effectiveness analysis"""
        test_files = self._discover_test_files(test_directory)
        
        effectiveness_report = {
            'overall_score': 0,
            'dimension_scores': {},
            'detailed_analysis': {},
            'trends': {},
            'action_items': []
        }
        
        # Analyze each dimension
        for dimension, analyzer in self.metrics.items():
            dimension_result = analyzer.analyze(test_files)
            effectiveness_report['dimension_scores'][dimension] = dimension_result['score']
            effectiveness_report['detailed_analysis'][dimension] = dimension_result
        
        # Calculate overall effectiveness score
        effectiveness_report['overall_score'] = self._calculate_overall_score(
            effectiveness_report['dimension_scores']
        )
        
        # Generate action items
        effectiveness_report['action_items'] = self._generate_action_items(
            effectiveness_report['detailed_analysis']
        )
        
        # Trend analysis
        effectiveness_report['trends'] = self._analyze_trends(effectiveness_report)
        
        return effectiveness_report
    
    class CoverageAnalyzer:
        """Analyze test coverage effectiveness"""
        
        def analyze(self, test_files):
            """Analyze coverage quality and effectiveness"""
            coverage_data = self._run_coverage_analysis(test_files)
            
            # Multiple coverage metrics
            metrics = {
                'line_coverage': coverage_data['line_coverage'],
                'branch_coverage': coverage_data['branch_coverage'],
                'function_coverage': coverage_data['function_coverage'],
                'condition_coverage': coverage_data.get('condition_coverage', 0),
                'path_coverage': self._analyze_path_coverage(coverage_data)
            }
            
            # Coverage quality analysis
            quality_indicators = {
                'meaningful_coverage': self._analyze_meaningful_coverage(coverage_data),
                'edge_case_coverage': self._analyze_edge_case_coverage(coverage_data),
                'error_path_coverage': self._analyze_error_path_coverage(coverage_data)
            }
            
            # Calculate composite score
            score = self._calculate_coverage_score(metrics, quality_indicators)
            
            return {
                'score': score,
                'metrics': metrics,
                'quality_indicators': quality_indicators,
                'uncovered_critical_paths': self._identify_critical_uncovered_paths(coverage_data),
                'recommendations': self._generate_coverage_recommendations(metrics, quality_indicators)
            }
        
        def _analyze_meaningful_coverage(self, coverage_data):
            """Analyze if coverage represents meaningful testing"""
            # Look for patterns that indicate meaningful vs. accidental coverage
            meaningful_indicators = []
            
            for file_path, file_data in coverage_data['files'].items():
                # Check if covered lines include assertions
                covered_lines_with_assertions = self._count_covered_assertions(file_data)
                total_covered_lines = len(file_data['covered_lines'])
                
                if total_covered_lines > 0:
                    assertion_ratio = covered_lines_with_assertions / total_covered_lines
                    meaningful_indicators.append(assertion_ratio)
            
            return sum(meaningful_indicators) / len(meaningful_indicators) if meaningful_indicators else 0
    
    class AssertionQualityAnalyzer:
        """Analyze quality and effectiveness of test assertions"""
        
        def analyze(self, test_files):
            """Analyze assertion quality across test files"""
            all_assertions = []
            
            for test_file in test_files:
                file_assertions = self._extract_assertions(test_file)
                all_assertions.extend(file_assertions)
            
            # Quality metrics
            quality_metrics = {
                'assertion_density': self._calculate_assertion_density(all_assertions, test_files),
                'assertion_specificity': self._analyze_assertion_specificity(all_assertions),
                'business_logic_coverage': self._analyze_business_logic_assertions(all_assertions),
                'error_case_assertions': self._analyze_error_case_assertions(all_assertions),
                'assertion_independence': self._analyze_assertion_independence(all_assertions)
            }
            
            # Anti-pattern detection
            anti_patterns = {
                'trivial_assertions': self._detect_trivial_assertions(all_assertions),
                'assertion_roulette': self._detect_assertion_roulette(all_assertions),
                'mystery_guest': self._detect_mystery_guest_patterns(all_assertions),
                'eager_test': self._detect_eager_test_patterns(all_assertions)
            }
            
            score = self._calculate_assertion_quality_score(quality_metrics, anti_patterns)
            
            return {
                'score': score,
                'quality_metrics': quality_metrics,
                'anti_patterns': anti_patterns,
                'improvement_suggestions': self._generate_assertion_improvements(quality_metrics, anti_patterns)
            }
        
        def _analyze_assertion_specificity(self, assertions):
            """Analyze how specific and meaningful assertions are"""
            specificity_scores = []
            
            for assertion in assertions:
                # Analyze assertion patterns
                if 'assertTrue' in assertion['code'] or 'assertFalse' in assertion['code']:
                    specificity_scores.append(0.3)  # Generic boolean assertions
                elif 'assertEqual' in assertion['code'] or 'assertEquals' in assertion['code']:
                    specificity_scores.append(0.7)  # Value-specific assertions
                elif 'assertRaises' in assertion['code'] or 'assertThrows' in assertion['code']:
                    specificity_scores.append(0.9)  # Exception-specific assertions
                elif self._is_custom_assertion(assertion['code']):
                    specificity_scores.append(0.95)  # Domain-specific assertions
                else:
                    specificity_scores.append(0.5)  # Default
            
            return sum(specificity_scores) / len(specificity_scores) if specificity_scores else 0
```

### Architecture Compliance Monitoring

```python
class ArchitectureComplianceMonitor:
    """Monitor adherence to architectural patterns and constraints"""
    
    def __init__(self):
        self.architecture_rules = ArchitectureRuleEngine()
        self.pattern_detector = ArchitecturePatternDetector()
        self.dependency_analyzer = DependencyAnalyzer()
        self.layering_validator = LayeringValidator()
    
    def monitor_architecture_compliance(self, project_path):
        """Comprehensive architecture compliance monitoring"""
        # Detect current architecture patterns
        detected_patterns = self.pattern_detector.detect_patterns(project_path)
        
        # Load architecture rules (from config or inferred)
        architecture_rules = self.architecture_rules.load_rules(project_path, detected_patterns)
        
        # Run compliance checks
        compliance_results = {
            'dependency_violations': self._check_dependency_compliance(project_path, architecture_rules),
            'layering_violations': self._check_layering_compliance(project_path, architecture_rules),
            'pattern_violations': self._check_pattern_compliance(project_path, architecture_rules),
            'coupling_violations': self._check_coupling_compliance(project_path, architecture_rules),
            'cohesion_violations': self._check_cohesion_compliance(project_path, architecture_rules)
        }
        
        # Calculate compliance scores
        compliance_scores = self._calculate_compliance_scores(compliance_results)
        
        # Generate improvement roadmap
        improvement_roadmap = self._generate_improvement_roadmap(compliance_results, compliance_scores)
        
        return {
            'overall_compliance': compliance_scores['overall'],
            'dimension_scores': compliance_scores['dimensions'],
            'violations': compliance_results,
            'detected_patterns': detected_patterns,
            'architecture_health': self._assess_architecture_health(compliance_results),
            'improvement_roadmap': improvement_roadmap,
            'trend_analysis': self._analyze_compliance_trends(compliance_scores)
        }
    
    def _check_dependency_compliance(self, project_path, rules):
        """Check for dependency rule violations"""
        dependency_graph = self.dependency_analyzer.build_graph(project_path)
        violations = []
        
        for rule in rules.get('dependency_rules', []):
            rule_violations = self._validate_dependency_rule(dependency_graph, rule)
            violations.extend(rule_violations)
        
        # Common dependency anti-patterns
        circular_dependencies = self.dependency_analyzer.detect_circular_dependencies(dependency_graph)
        violations.extend([
            {
                'type': 'circular_dependency',
                'severity': 'HIGH',
                'cycle': cycle,
                'impact': 'Makes code hard to test and modify'
            }
            for cycle in circular_dependencies
        ])
        
        return violations
    
    def _check_layering_compliance(self, project_path, rules):
        """Check for layering violations"""
        layer_structure = self.layering_validator.analyze_layers(project_path)
        violations = []
        
        # Check layer ordering rules
        for rule in rules.get('layering_rules', []):
            if rule['type'] == 'layer_ordering':
                layer_violations = self._validate_layer_ordering(layer_structure, rule)
                violations.extend(layer_violations)
            
            elif rule['type'] == 'layer_isolation':
                isolation_violations = self._validate_layer_isolation(layer_structure, rule)
                violations.extend(isolation_violations)
        
        return violations
```

### Trend Analysis System

```python
class QualityTrendAnalyzer:
    """Analyze quality trends over time"""
    
    def __init__(self):
        self.historical_data = HistoricalDataManager()
        self.trend_detector = TrendDetectionEngine()
        self.prediction_engine = QualityPredictionEngine()
    
    def analyze_quality_trends(self, current_metrics):
        """Analyze quality trends and predict future state"""
        # Get historical data
        historical_metrics = self.historical_data.get_historical_metrics()
        
        # Trend analysis for each metric
        trend_analysis = {}
        
        for metric_name, current_value in current_metrics.items():
            historical_values = [h[metric_name] for h in historical_metrics if metric_name in h]
            
            if len(historical_values) >= 3:  # Minimum data points for trend analysis
                trend_analysis[metric_name] = self._analyze_metric_trend(
                    metric_name, 
                    historical_values, 
                    current_value
                )
        
        # Overall quality trend
        overall_trend = self._analyze_overall_quality_trend(trend_analysis)
        
        # Predictions
        predictions = self.prediction_engine.predict_quality_evolution(
            historical_metrics, 
            current_metrics,
            trend_analysis
        )
        
        # Risk assessment
        risk_assessment = self._assess_quality_risks(trend_analysis, predictions)
        
        return {
            'metric_trends': trend_analysis,
            'overall_trend': overall_trend,
            'predictions': predictions,
            'risk_assessment': risk_assessment,
            'recommendations': self._generate_trend_recommendations(trend_analysis, risk_assessment)
        }
    
    def _analyze_metric_trend(self, metric_name, historical_values, current_value):
        """Analyze trend for a specific metric"""
        # Calculate trend indicators
        trend_direction = self._calculate_trend_direction(historical_values + [current_value])
        trend_strength = self._calculate_trend_strength(historical_values + [current_value])
        volatility = self._calculate_volatility(historical_values + [current_value])
        
        # Determine trend significance
        is_significant = self._is_trend_significant(historical_values, current_value)
        
        # Calculate momentum
        momentum = self._calculate_momentum(historical_values + [current_value])
        
        return {
            'direction': trend_direction,  # 'improving', 'declining', 'stable'
            'strength': trend_strength,    # 0.0 to 1.0
            'volatility': volatility,      # 0.0 to 1.0
            'significant': is_significant,
            'momentum': momentum,          # Rate of change
            'current_value': current_value,
            'historical_average': sum(historical_values) / len(historical_values),
            'improvement_rate': self._calculate_improvement_rate(historical_values, current_value)
        }
```

## Real-Time Dashboard Integration

```python
class QualityMonitoringDashboard:
    """Real-time quality monitoring dashboard"""
    
    def __init__(self):
        self.mutation_tracker = MutationScoreTracker()
        self.test_monitor = TestEffectivenessMonitor()
        self.architecture_monitor = ArchitectureComplianceMonitor()
        self.trend_analyzer = QualityTrendAnalyzer()
        
        self.real_time_enabled = True
        self.refresh_interval = 30  # seconds
    
    def get_dashboard_data(self):
        """Get complete dashboard data"""
        dashboard_data = {
            'timestamp': time.time(),
            'quality_overview': self._get_quality_overview(),
            'mutation_testing': self._get_mutation_data(),
            'test_effectiveness': self._get_test_effectiveness_data(),
            'architecture_compliance': self._get_architecture_data(),
            'trend_analysis': self._get_trend_data(),
            'alerts': self._get_active_alerts(),
            'recommendations': self._get_priority_recommendations()
        }
        
        return dashboard_data
    
    def _get_quality_overview(self):
        """Get high-level quality overview"""
        return {
            'overall_health': self._calculate_overall_health(),
            'quality_score': self._calculate_composite_quality_score(),
            'trend_indicator': self._get_trend_indicator(),
            'critical_issues': self._count_critical_issues(),
            'quality_gates_status': self._get_quality_gates_status()
        }
```

## Configuration and Integration

```yaml
# .claude/config/quality-monitoring.yaml
monitoring:
  enabled: true
  real_time: true
  historical_tracking: true
  
mutation_testing:
  enabled: true
  parallel_execution: true
  intelligent_selection: true
  performance_optimized: true
  minimum_score_threshold: 0.8
  
test_effectiveness:
  coverage_threshold: 0.9
  assertion_quality_threshold: 0.8
  maintainability_threshold: 0.7
  
architecture_compliance:
  pattern_detection: true
  dependency_validation: true
  layering_validation: true
  coupling_monitoring: true
  
trend_analysis:
  historical_data_retention: "6_months"
  trend_detection_sensitivity: "medium"
  prediction_horizon: "30_days"
  
dashboard:
  refresh_interval: 30
  real_time_alerts: true
  notification_channels: ["slack", "email"]
  
integration:
  tdd_cycle: true
  quality_gates: true
  ci_cd_pipeline: true
  ide_plugins: true
```

This code quality monitoring system provides comprehensive, real-time tracking of all quality dimensions with intelligent analysis, trend detection, and actionable insights for continuous improvement.