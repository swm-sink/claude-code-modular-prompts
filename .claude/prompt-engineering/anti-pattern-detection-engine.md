# Anti-Pattern Detection Engine

| version | last_updated | status | agent |
|---------|--------------|--------|--------|
| 1.0.0   | 2025-07-20   | production | I26 |

## Purpose

Comprehensive anti-pattern detection system that identifies code smells, architectural violations, and testing anti-patterns in real-time during development workflows.

## Core Detection Algorithms

### God Object Detection

```python
class GodObjectDetector:
    """Detects god objects through multiple metrics"""
    
    def __init__(self):
        self.max_methods = 20
        self.max_lines = 500
        self.max_responsibilities = 5
        self.max_dependencies = 15
    
    def analyze_class(self, class_node):
        """Comprehensive god object analysis"""
        metrics = {
            'method_count': len(class_node.methods),
            'line_count': class_node.end_line - class_node.start_line,
            'responsibility_count': self._count_responsibilities(class_node),
            'dependency_count': len(class_node.dependencies),
            'cohesion_score': self._calculate_cohesion(class_node),
            'coupling_score': self._calculate_coupling(class_node)
        }
        
        violations = []
        if metrics['method_count'] > self.max_methods:
            violations.append({
                'type': 'TOO_MANY_METHODS',
                'severity': 'HIGH',
                'actual': metrics['method_count'],
                'threshold': self.max_methods,
                'suggestion': 'Extract related methods into separate classes'
            })
        
        if metrics['responsibility_count'] > self.max_responsibilities:
            violations.append({
                'type': 'TOO_MANY_RESPONSIBILITIES',
                'severity': 'CRITICAL',
                'actual': metrics['responsibility_count'],
                'threshold': self.max_responsibilities,
                'suggestion': 'Apply Single Responsibility Principle - split class'
            })
        
        return {
            'is_god_object': len(violations) > 0,
            'metrics': metrics,
            'violations': violations,
            'refactoring_suggestions': self._generate_refactoring_plan(class_node, violations)
        }
    
    def _count_responsibilities(self, class_node):
        """Count distinct responsibilities using method analysis"""
        # Analyze method names, dependencies, and data access patterns
        responsibilities = set()
        
        for method in class_node.methods:
            # Extract responsibility indicators from method names
            words = self._extract_action_words(method.name)
            for word in words:
                responsibilities.add(self._categorize_responsibility(word))
        
        return len(responsibilities)
    
    def _generate_refactoring_plan(self, class_node, violations):
        """Generate step-by-step refactoring suggestions"""
        plans = []
        
        for violation in violations:
            if violation['type'] == 'TOO_MANY_METHODS':
                plans.append({
                    'step': 1,
                    'action': 'GROUP_RELATED_METHODS',
                    'description': 'Identify and group methods by responsibility',
                    'methods': self._group_methods_by_responsibility(class_node)
                })
                plans.append({
                    'step': 2,
                    'action': 'EXTRACT_CLASSES',
                    'description': 'Create new classes for each responsibility group',
                    'new_classes': self._suggest_new_class_names(class_node)
                })
        
        return plans
```

### Testing Theatre Detection

```python
class TestingTheatreDetector:
    """Detects fake testing patterns that provide false security"""
    
    def __init__(self):
        self.min_assertion_ratio = 0.3
        self.max_mock_ratio = 0.7
        self.min_branch_coverage = 0.8
        self.suspicious_patterns = [
            r'assert.*True',  # Always passing assertions
            r'assert.*1.*==.*1',  # Trivial assertions
            r'mock.*return_value.*=.*None',  # Overmocking
            r'@patch.*autospec=False'  # Dangerous mocking
        ]
    
    def analyze_test_file(self, test_file_path):
        """Comprehensive test quality analysis"""
        with open(test_file_path, 'r') as f:
            content = f.read()
        
        test_methods = self._extract_test_methods(content)
        violations = []
        
        for method in test_methods:
            method_violations = self._analyze_test_method(method)
            violations.extend(method_violations)
        
        # File-level analysis
        file_violations = self._analyze_test_file_structure(content)
        violations.extend(file_violations)
        
        return {
            'is_testing_theatre': len(violations) > 0,
            'violations': violations,
            'quality_score': self._calculate_test_quality_score(test_methods),
            'improvement_suggestions': self._generate_test_improvements(violations)
        }
    
    def _analyze_test_method(self, method):
        """Analyze individual test method for anti-patterns"""
        violations = []
        
        # Check for assertion quality
        assertions = self._extract_assertions(method.body)
        if len(assertions) == 0:
            violations.append({
                'type': 'NO_ASSERTIONS',
                'severity': 'CRITICAL',
                'method': method.name,
                'suggestion': 'Add meaningful assertions to verify behavior'
            })
        
        # Check for trivial assertions
        for assertion in assertions:
            if self._is_trivial_assertion(assertion):
                violations.append({
                    'type': 'TRIVIAL_ASSERTION',
                    'severity': 'HIGH',
                    'method': method.name,
                    'assertion': assertion,
                    'suggestion': 'Replace with meaningful business logic assertion'
                })
        
        # Check for overmocking
        mocks = self._extract_mocks(method.body)
        if len(mocks) / max(len(assertions), 1) > self.max_mock_ratio:
            violations.append({
                'type': 'OVERMOCKING',
                'severity': 'MEDIUM',
                'method': method.name,
                'mock_count': len(mocks),
                'assertion_count': len(assertions),
                'suggestion': 'Reduce mocks, test real behavior where possible'
            })
        
        return violations
    
    def _generate_test_improvements(self, violations):
        """Generate actionable test improvement suggestions"""
        improvements = []
        
        violation_types = [v['type'] for v in violations]
        
        if 'NO_ASSERTIONS' in violation_types:
            improvements.append({
                'priority': 'CRITICAL',
                'action': 'ADD_MEANINGFUL_ASSERTIONS',
                'description': 'Add assertions that verify actual business behavior',
                'examples': [
                    'assert result.is_valid == True',
                    'assert len(processed_items) == expected_count',
                    'assert error_message == "Invalid input format"'
                ]
            })
        
        if 'TRIVIAL_ASSERTION' in violation_types:
            improvements.append({
                'priority': 'HIGH',
                'action': 'IMPROVE_ASSERTION_QUALITY',
                'description': 'Replace trivial assertions with business logic verification',
                'pattern': 'Instead of assert True, verify actual outcomes'
            })
        
        return improvements
```

### Hallucinated Architecture Detection

```python
class HallucinatedArchitectureDetector:
    """Detects architecture patterns that don't actually exist in code"""
    
    def __init__(self):
        self.architecture_patterns = {
            'mvc': ['models', 'views', 'controllers'],
            'layered': ['presentation', 'business', 'data', 'persistence'],
            'microservices': ['services', 'gateway', 'discovery'],
            'clean_architecture': ['entities', 'use_cases', 'adapters', 'frameworks']
        }
    
    def analyze_project_architecture(self, project_path):
        """Analyze if claimed architecture patterns actually exist"""
        claimed_patterns = self._extract_claimed_patterns(project_path)
        actual_structure = self._analyze_actual_structure(project_path)
        
        violations = []
        
        for pattern in claimed_patterns:
            if pattern in self.architecture_patterns:
                verification = self._verify_pattern_implementation(
                    pattern, 
                    actual_structure, 
                    self.architecture_patterns[pattern]
                )
                
                if not verification['exists']:
                    violations.append({
                        'type': 'HALLUCINATED_PATTERN',
                        'severity': 'CRITICAL',
                        'pattern': pattern,
                        'claimed_location': verification['claimed_location'],
                        'missing_components': verification['missing_components'],
                        'suggestion': f'Implement {pattern} pattern or remove claims'
                    })
        
        return {
            'has_hallucinated_architecture': len(violations) > 0,
            'violations': violations,
            'actual_patterns': self._identify_actual_patterns(actual_structure),
            'recommendations': self._generate_architecture_recommendations(violations)
        }
    
    def _verify_pattern_implementation(self, pattern, structure, required_components):
        """Verify if architecture pattern is actually implemented"""
        missing_components = []
        exists = True
        
        for component in required_components:
            if not self._component_exists_in_structure(component, structure):
                missing_components.append(component)
                exists = False
        
        return {
            'exists': exists,
            'missing_components': missing_components,
            'implementation_percentage': (len(required_components) - len(missing_components)) / len(required_components),
            'claimed_location': self._find_pattern_claims(pattern)
        }
```

### Pattern Smell Detection

```python
class PatternSmellDetector:
    """Detects misuse of design patterns and anti-patterns"""
    
    def __init__(self):
        self.pattern_smells = {
            'singleton_abuse': {
                'indicators': ['global_state', 'multiple_responsibilities', 'testing_difficulty'],
                'severity': 'HIGH'
            },
            'factory_overkill': {
                'indicators': ['single_implementation', 'unnecessary_abstraction'],
                'severity': 'MEDIUM'
            },
            'observer_chaos': {
                'indicators': ['circular_dependencies', 'memory_leaks', 'event_storms'],
                'severity': 'HIGH'
            },
            'strategy_confusion': {
                'indicators': ['single_strategy', 'no_runtime_switching'],
                'severity': 'MEDIUM'
            }
        }
    
    def analyze_pattern_usage(self, codebase_path):
        """Analyze design pattern usage for smells"""
        patterns_found = self._identify_patterns_in_code(codebase_path)
        violations = []
        
        for pattern_instance in patterns_found:
            pattern_type = pattern_instance['type']
            if pattern_type in self.pattern_smells:
                smell_analysis = self._analyze_pattern_smell(
                    pattern_instance, 
                    self.pattern_smells[pattern_type]
                )
                
                if smell_analysis['has_smell']:
                    violations.append({
                        'type': f'{pattern_type.upper()}_SMELL',
                        'severity': self.pattern_smells[pattern_type]['severity'],
                        'location': pattern_instance['location'],
                        'smell_indicators': smell_analysis['indicators'],
                        'suggestion': smell_analysis['recommendation']
                    })
        
        return {
            'has_pattern_smells': len(violations) > 0,
            'violations': violations,
            'pattern_usage_quality': self._calculate_pattern_quality_score(patterns_found, violations),
            'refactoring_priorities': self._prioritize_pattern_refactoring(violations)
        }
```

## Real-Time Detection Integration

```python
class RealTimeDetectionEngine:
    """Integrates all detection algorithms for real-time analysis"""
    
    def __init__(self):
        self.detectors = {
            'god_object': GodObjectDetector(),
            'testing_theatre': TestingTheatreDetector(),
            'hallucinated_architecture': HallucinatedArchitectureDetector(),
            'pattern_smell': PatternSmellDetector()
        }
        
        self.detection_config = {
            'run_on_save': True,
            'run_on_commit': True,
            'run_on_pr': True,
            'blocking_violations': ['CRITICAL'],
            'warning_violations': ['HIGH', 'MEDIUM']
        }
    
    def analyze_file_change(self, file_path, change_type):
        """Analyze specific file change for anti-patterns"""
        results = {}
        
        # Determine which detectors to run based on file type
        if file_path.endswith('.py'):
            if 'test' in file_path:
                results['testing_theatre'] = self.detectors['testing_theatre'].analyze_test_file(file_path)
            else:
                results['god_object'] = self.detectors['god_object'].analyze_file(file_path)
                results['pattern_smell'] = self.detectors['pattern_smell'].analyze_file(file_path)
        
        # Architecture analysis for structural changes
        if change_type in ['directory_add', 'file_move', 'refactor']:
            results['hallucinated_architecture'] = self.detectors['hallucinated_architecture'].analyze_project_architecture('.')
        
        return self._consolidate_results(results)
    
    def _consolidate_results(self, results):
        """Consolidate detection results into actionable report"""
        all_violations = []
        blocking_issues = []
        
        for detector_name, result in results.items():
            if result and 'violations' in result:
                for violation in result['violations']:
                    violation['detector'] = detector_name
                    all_violations.append(violation)
                    
                    if violation['severity'] in self.detection_config['blocking_violations']:
                        blocking_issues.append(violation)
        
        return {
            'total_violations': len(all_violations),
            'blocking_issues': len(blocking_issues),
            'violations': all_violations,
            'should_block': len(blocking_issues) > 0,
            'summary': self._generate_violation_summary(all_violations),
            'action_items': self._generate_action_items(all_violations)
        }
```

## Framework Integration

```python
class AntiPatternDetectionFramework:
    """Main framework integration for anti-pattern detection"""
    
    def __init__(self):
        self.engine = RealTimeDetectionEngine()
        self.prevention_mode = True
        self.education_mode = True
    
    def integrate_with_tdd_cycle(self, tdd_phase):
        """Integrate detection with TDD cycle phases"""
        if tdd_phase == 'RED':
            # Focus on test quality during red phase
            return self.engine.detectors['testing_theatre']
        
        elif tdd_phase == 'GREEN':
            # Focus on implementation quality during green phase
            return [
                self.engine.detectors['god_object'],
                self.engine.detectors['pattern_smell']
            ]
        
        elif tdd_phase == 'REFACTOR':
            # Full analysis during refactor phase
            return list(self.engine.detectors.values())
    
    def generate_prevention_guidance(self, violation):
        """Generate educational content for preventing anti-patterns"""
        guidance = {
            'explanation': self._explain_anti_pattern(violation['type']),
            'prevention_tips': self._get_prevention_tips(violation['type']),
            'best_practices': self._get_best_practices(violation['type']),
            'examples': self._get_good_examples(violation['type'])
        }
        
        return guidance
```

## Usage Integration

The anti-pattern detection engine integrates with:

1. **TDD Cycle**: Runs appropriate detectors at each TDD phase
2. **Git Hooks**: Pre-commit and pre-push validation
3. **IDE Integration**: Real-time feedback during development
4. **Quality Gates**: Blocks commits with critical violations
5. **Education System**: Provides learning content for developers

## Configuration

```yaml
# .claude/config/anti-pattern-detection.yaml
detection:
  enabled: true
  real_time: true
  blocking_mode: true
  
detectors:
  god_object:
    enabled: true
    max_methods: 20
    max_lines: 500
    max_responsibilities: 5
    
  testing_theatre:
    enabled: true
    min_assertion_ratio: 0.3
    require_meaningful_assertions: true
    
  hallucinated_architecture:
    enabled: true
    verify_claimed_patterns: true
    
  pattern_smell:
    enabled: true
    severity_threshold: "MEDIUM"

reporting:
  format: "detailed"
  include_suggestions: true
  include_examples: true
  generate_refactoring_plan: true
```

This anti-pattern detection engine provides comprehensive, real-time analysis to prevent common development anti-patterns and maintain code quality throughout the development lifecycle.