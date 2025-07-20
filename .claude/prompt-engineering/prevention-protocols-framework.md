# Prevention Protocols Framework

| version | last_updated | status | agent |
|---------|--------------|--------|--------|
| 1.0.0   | 2025-07-20   | production | I27 |

## Purpose

Comprehensive prevention system that proactively stops anti-patterns before they occur through real-time triggers, automatic refactoring suggestions, educational guidance, and enforcement mechanisms.

## Real-Time Prevention Triggers

### Git Hook Integration

```python
class GitHookPreventionTriggers:
    """Prevention triggers integrated with Git workflow"""
    
    def __init__(self):
        self.hooks = {
            'pre-commit': self._pre_commit_prevention,
            'pre-push': self._pre_push_prevention,
            'post-commit': self._post_commit_learning,
            'pre-merge': self._pre_merge_validation
        }
        
        self.prevention_rules = {
            'god_object': {
                'trigger_threshold': 15,  # methods
                'action': 'suggest_extraction',
                'blocking': True
            },
            'testing_theatre': {
                'trigger_threshold': 0.2,  # assertion ratio
                'action': 'require_real_tests',
                'blocking': True
            },
            'hallucinated_architecture': {
                'trigger_threshold': 1,  # any occurrence
                'action': 'demand_implementation',
                'blocking': True
            }
        }
    
    def _pre_commit_prevention(self, staged_files):
        """Prevent anti-patterns at commit time"""
        violations = []
        
        for file_path in staged_files:
            if self._is_code_file(file_path):
                # Run lightweight prevention checks
                quick_analysis = self._quick_pattern_check(file_path)
                
                for violation in quick_analysis:
                    if self._should_block_commit(violation):
                        violations.append({
                            'file': file_path,
                            'violation': violation,
                            'prevention_action': self._get_prevention_action(violation),
                            'auto_fix_available': self._has_auto_fix(violation)
                        })
        
        if violations:
            return self._handle_commit_violations(violations)
        
        return {'allowed': True, 'message': 'All prevention checks passed'}
    
    def _handle_commit_violations(self, violations):
        """Handle violations found during commit"""
        blocking_violations = [v for v in violations if self._is_blocking(v['violation'])]
        
        if blocking_violations:
            # Offer auto-fixes where possible
            auto_fixable = [v for v in blocking_violations if v['auto_fix_available']]
            
            response = {
                'allowed': False,
                'message': f'Found {len(blocking_violations)} blocking violations',
                'violations': blocking_violations,
                'auto_fixes_available': len(auto_fixable),
                'commands': []
            }
            
            if auto_fixable:
                response['commands'].append({
                    'action': 'auto_fix',
                    'command': 'claude-fix --apply-safe-fixes',
                    'description': f'Auto-fix {len(auto_fixable)} violations'
                })
            
            response['commands'].append({
                'action': 'manual_review',
                'command': 'claude-review --show-violations',
                'description': 'Review violations and apply manual fixes'
            })
            
            return response
        
        return {'allowed': True, 'warnings': violations}
```

### IDE Integration Triggers

```python
class IDEPreventionTriggers:
    """Real-time prevention in IDE/editor"""
    
    def __init__(self):
        self.real_time_enabled = True
        self.suggestion_delay = 2.0  # seconds
        self.prevention_cache = {}
    
    def on_file_change(self, file_path, change_event):
        """Trigger prevention on file changes"""
        if not self.real_time_enabled:
            return
        
        # Debounce rapid changes
        if self._should_debounce(file_path, change_event):
            return
        
        # Quick pattern analysis
        analysis = self._analyze_current_state(file_path)
        
        if analysis['potential_violations']:
            return self._generate_real_time_suggestions(analysis)
    
    def _analyze_current_state(self, file_path):
        """Analyze current file state for emerging anti-patterns"""
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Quick heuristic checks
        potential_violations = []
        
        # God object early warning
        if self._count_methods_heuristic(content) > 12:
            potential_violations.append({
                'type': 'emerging_god_object',
                'severity': 'WARNING',
                'current_methods': self._count_methods_heuristic(content),
                'threshold': 15,
                'suggestion': 'Consider extracting related methods into separate classes'
            })
        
        # Testing theatre early warning
        if 'def test_' in content and self._count_assertions_heuristic(content) == 0:
            potential_violations.append({
                'type': 'test_without_assertions',
                'severity': 'ERROR',
                'suggestion': 'Add meaningful assertions to verify behavior'
            })
        
        return {
            'file_path': file_path,
            'potential_violations': potential_violations,
            'timestamp': time.time()
        }
    
    def _generate_real_time_suggestions(self, analysis):
        """Generate immediate suggestions for developer"""
        suggestions = []
        
        for violation in analysis['potential_violations']:
            if violation['type'] == 'emerging_god_object':
                suggestions.append({
                    'type': 'refactor_suggestion',
                    'priority': 'MEDIUM',
                    'message': f"Class approaching god object threshold ({violation['current_methods']}/{violation['threshold']} methods)",
                    'actions': [
                        {
                            'label': 'Extract Methods',
                            'command': 'claude-refactor --extract-methods',
                            'description': 'Automatically suggest method extraction'
                        },
                        {
                            'label': 'Analyze Responsibilities',
                            'command': 'claude-analyze --responsibilities',
                            'description': 'Show responsibility breakdown'
                        }
                    ]
                })
            
            elif violation['type'] == 'test_without_assertions':
                suggestions.append({
                    'type': 'test_improvement',
                    'priority': 'HIGH',
                    'message': 'Test method detected without assertions',
                    'actions': [
                        {
                            'label': 'Add Assertions',
                            'command': 'claude-test --suggest-assertions',
                            'description': 'Suggest meaningful assertions'
                        },
                        {
                            'label': 'Test Template',
                            'command': 'claude-test --template',
                            'description': 'Insert test template with assertions'
                        }
                    ]
                })
        
        return {
            'suggestions': suggestions,
            'should_show_popup': any(s['priority'] == 'HIGH' for s in suggestions),
            'should_highlight': True
        }
```

## Automatic Refactoring Suggestions

### Smart Refactoring Engine

```python
class SmartRefactoringEngine:
    """Intelligent refactoring suggestions and auto-fixes"""
    
    def __init__(self):
        self.refactoring_patterns = {
            'extract_method': ExtractMethodRefactoring(),
            'extract_class': ExtractClassRefactoring(),
            'move_method': MoveMethodRefactoring(),
            'inline_method': InlineMethodRefactoring(),
            'rename_for_clarity': RenameRefactoring(),
            'split_responsibilities': SplitClassRefactoring()
        }
        
        self.safety_checks = SafetyCheckEngine()
    
    def suggest_refactoring(self, violation):
        """Generate smart refactoring suggestions"""
        if violation['type'] == 'god_object':
            return self._suggest_god_object_refactoring(violation)
        elif violation['type'] == 'testing_theatre':
            return self._suggest_test_improvements(violation)
        elif violation['type'] == 'pattern_smell':
            return self._suggest_pattern_corrections(violation)
        
        return []
    
    def _suggest_god_object_refactoring(self, violation):
        """Suggest specific refactoring for god objects"""
        class_info = violation['class_info']
        suggestions = []
        
        # Analyze class structure
        method_groups = self._group_methods_by_responsibility(class_info)
        
        if len(method_groups) > 1:
            for group_name, methods in method_groups.items():
                if len(methods) >= 3:  # Minimum group size for extraction
                    suggestions.append({
                        'type': 'extract_class',
                        'priority': 'HIGH',
                        'description': f'Extract {group_name} responsibility into separate class',
                        'methods_to_extract': methods,
                        'suggested_class_name': self._suggest_class_name(group_name),
                        'estimated_effort': 'MEDIUM',
                        'safety_score': self._calculate_extraction_safety(methods),
                        'auto_applicable': self._can_auto_extract(methods),
                        'preview': self._generate_extraction_preview(group_name, methods)
                    })
        
        # Method-level suggestions
        large_methods = self._identify_large_methods(class_info)
        for method in large_methods:
            if method['lines'] > 20:
                suggestions.append({
                    'type': 'extract_method',
                    'priority': 'MEDIUM',
                    'description': f'Split large method {method["name"]} ({method["lines"]} lines)',
                    'method_name': method['name'],
                    'suggested_extractions': self._suggest_method_extractions(method),
                    'auto_applicable': True,
                    'preview': self._generate_method_extraction_preview(method)
                })
        
        return suggestions
    
    def _suggest_test_improvements(self, violation):
        """Suggest test quality improvements"""
        test_info = violation['test_info']
        suggestions = []
        
        if violation['subtype'] == 'no_assertions':
            suggestions.append({
                'type': 'add_assertions',
                'priority': 'CRITICAL',
                'description': 'Add meaningful assertions to verify behavior',
                'suggested_assertions': self._generate_assertion_suggestions(test_info),
                'auto_applicable': True,
                'template': self._get_assertion_template(test_info)
            })
        
        elif violation['subtype'] == 'trivial_assertions':
            suggestions.append({
                'type': 'improve_assertions',
                'priority': 'HIGH',
                'description': 'Replace trivial assertions with meaningful business logic checks',
                'current_assertions': violation['trivial_assertions'],
                'improved_assertions': self._suggest_assertion_improvements(violation['trivial_assertions']),
                'auto_applicable': False,  # Requires understanding of business logic
                'guidance': 'Focus on verifying the actual behavior and outcomes of your code'
            })
        
        return suggestions
    
    def apply_auto_refactoring(self, suggestion):
        """Apply automatic refactoring where safe"""
        if not suggestion['auto_applicable']:
            return {'success': False, 'reason': 'Manual intervention required'}
        
        # Safety checks first
        safety_result = self.safety_checks.verify_refactoring_safety(suggestion)
        if not safety_result['safe']:
            return {'success': False, 'reason': safety_result['risks']}
        
        # Apply refactoring
        refactoring_type = suggestion['type']
        refactoring_engine = self.refactoring_patterns[refactoring_type]
        
        try:
            result = refactoring_engine.apply(suggestion)
            
            # Verify result doesn't break tests
            test_result = self._run_affected_tests(result['affected_files'])
            
            if test_result['all_passed']:
                return {
                    'success': True,
                    'changes': result['changes'],
                    'message': f"Successfully applied {refactoring_type} refactoring"
                }
            else:
                # Rollback changes
                self._rollback_changes(result['changes'])
                return {
                    'success': False,
                    'reason': f'Refactoring broke {test_result["failed_count"]} tests',
                    'failed_tests': test_result['failed_tests']
                }
        
        except Exception as e:
            return {'success': False, 'reason': f'Refactoring failed: {str(e)}'}
```

## Education and Guidance System

### Interactive Learning Engine

```python
class EducationGuidanceSystem:
    """Interactive education system for preventing anti-patterns"""
    
    def __init__(self):
        self.learning_modules = {
            'god_object': GodObjectLearningModule(),
            'testing_theatre': TestingTheatreLearningModule(),
            'design_patterns': DesignPatternLearningModule(),
            'clean_code': CleanCodeLearningModule()
        }
        
        self.user_progress = UserProgressTracker()
        self.adaptive_engine = AdaptiveLearningEngine()
    
    def provide_contextual_guidance(self, violation, user_experience_level):
        """Provide education tailored to user level and context"""
        module = self.learning_modules.get(violation['category'])
        if not module:
            return self._generic_guidance(violation)
        
        guidance = module.get_guidance(
            violation_type=violation['type'],
            user_level=user_experience_level,
            context=violation.get('context', {})
        )
        
        return {
            'explanation': guidance['explanation'],
            'why_problematic': guidance['why_problematic'],
            'how_to_fix': guidance['how_to_fix'],
            'prevention_tips': guidance['prevention_tips'],
            'interactive_examples': guidance['interactive_examples'],
            'further_reading': guidance['further_reading'],
            'practice_exercises': guidance['practice_exercises']
        }
    
    class GodObjectLearningModule:
        """Specialized learning for god object prevention"""
        
        def get_guidance(self, violation_type, user_level, context):
            if user_level == 'BEGINNER':
                return {
                    'explanation': """
                    A "God Object" is a class that knows too much or does too much. 
                    Think of it like a Swiss Army knife - while versatile, it's not 
                    the best tool for any specific job.
                    """,
                    'why_problematic': [
                        "Hard to understand - too many responsibilities",
                        "Difficult to test - too many dependencies",
                        "Hard to modify - changes affect many things",
                        "Teams struggle to work on it simultaneously"
                    ],
                    'how_to_fix': self._beginner_god_object_fixes(context),
                    'prevention_tips': [
                        "Follow Single Responsibility Principle",
                        "Ask: 'What is this class's ONE job?'",
                        "If you use 'and' to describe it, split it",
                        "Keep classes under 200 lines when possible"
                    ],
                    'interactive_examples': self._generate_beginner_examples(),
                    'practice_exercises': self._beginner_exercises()
                }
            
            elif user_level == 'INTERMEDIATE':
                return {
                    'explanation': """
                    God Objects violate the Single Responsibility Principle and create 
                    high coupling, low cohesion systems. They become change bottlenecks 
                    and testing nightmares.
                    """,
                    'why_problematic': [
                        "Violates SOLID principles (especially SRP and OCP)",
                        "Creates maintenance bottlenecks",
                        "Reduces code reusability",
                        "Makes parallel development difficult"
                    ],
                    'how_to_fix': self._intermediate_god_object_fixes(context),
                    'prevention_tips': [
                        "Use composition over inheritance",
                        "Apply Extract Class refactoring early",
                        "Monitor class complexity metrics",
                        "Regular architectural reviews"
                    ],
                    'interactive_examples': self._generate_intermediate_examples(),
                    'practice_exercises': self._intermediate_exercises()
                }
        
        def _beginner_god_object_fixes(self, context):
            """Simple, step-by-step fixes for beginners"""
            return [
                {
                    'step': 1,
                    'action': 'Identify Responsibilities',
                    'description': 'List everything your class does',
                    'example': 'UserManager: validates users, saves to database, sends emails, generates reports'
                },
                {
                    'step': 2,
                    'action': 'Group Related Methods',
                    'description': 'Find methods that work together',
                    'example': 'Email methods: send_welcome_email(), send_reset_email(), format_email()'
                },
                {
                    'step': 3,
                    'action': 'Extract New Classes',
                    'description': 'Create new classes for each group',
                    'example': 'Create EmailService class for all email-related methods'
                },
                {
                    'step': 4,
                    'action': 'Update Original Class',
                    'description': 'Use new classes in original class',
                    'example': 'UserManager now uses EmailService instance'
                }
            ]
```

### Adaptive Learning Engine

```python
class AdaptiveLearningEngine:
    """Adapts education based on user patterns and progress"""
    
    def __init__(self):
        self.user_patterns = UserPatternAnalyzer()
        self.knowledge_graph = KnowledgeGraphEngine()
        self.reinforcement_scheduler = ReinforcementScheduler()
    
    def analyze_user_learning_needs(self, user_id, recent_violations):
        """Analyze what the user needs to learn"""
        violation_patterns = self._analyze_violation_patterns(recent_violations)
        knowledge_gaps = self._identify_knowledge_gaps(user_id, violation_patterns)
        
        return {
            'primary_focus_areas': knowledge_gaps['critical'],
            'secondary_areas': knowledge_gaps['important'],
            'learning_style': self._determine_learning_style(user_id),
            'recommended_sequence': self._plan_learning_sequence(knowledge_gaps),
            'reinforcement_schedule': self._plan_reinforcement(knowledge_gaps)
        }
    
    def _analyze_violation_patterns(self, violations):
        """Find patterns in user's coding violations"""
        patterns = {}
        
        for violation in violations:
            pattern_key = f"{violation['type']}_{violation.get('context', 'general')}"
            if pattern_key not in patterns:
                patterns[pattern_key] = {
                    'count': 0,
                    'severity_distribution': {},
                    'trend': 'unknown',
                    'contexts': []
                }
            
            patterns[pattern_key]['count'] += 1
            severity = violation['severity']
            patterns[pattern_key]['severity_distribution'][severity] = patterns[pattern_key]['severity_distribution'].get(severity, 0) + 1
            patterns[pattern_key]['contexts'].append(violation.get('context', {}))
        
        return patterns
    
    def create_personalized_learning_path(self, user_id, focus_areas):
        """Create customized learning path for user"""
        user_profile = self.user_patterns.get_profile(user_id)
        
        learning_path = []
        
        for area in focus_areas:
            modules = self._get_learning_modules_for_area(area)
            
            for module in modules:
                adapted_module = self._adapt_module_to_user(module, user_profile)
                learning_path.append(adapted_module)
        
        return {
            'learning_path': learning_path,
            'estimated_duration': self._estimate_completion_time(learning_path, user_profile),
            'milestones': self._define_milestones(learning_path),
            'progress_tracking': self._setup_progress_tracking(learning_path)
        }
```

## Enforcement Mechanisms

### Quality Gate Integration

```python
class EnforcementMechanisms:
    """Enforcement system that blocks problematic code"""
    
    def __init__(self):
        self.enforcement_levels = {
            'ADVISORY': {'block': False, 'warn': True, 'log': True},
            'WARNING': {'block': False, 'warn': True, 'log': True, 'require_acknowledgment': True},
            'BLOCKING': {'block': True, 'warn': True, 'log': True, 'require_override': True},
            'CRITICAL': {'block': True, 'warn': True, 'log': True, 'no_override': True}
        }
        
        self.override_system = OverrideSystemManager()
        self.audit_logger = AuditLogger()
    
    def enforce_quality_gate(self, violations, context):
        """Enforce quality gate based on violations"""
        highest_severity = self._get_highest_severity(violations)
        enforcement_level = self._determine_enforcement_level(highest_severity, context)
        
        action = self.enforcement_levels[enforcement_level]
        
        if action['block']:
            return self._handle_blocking_enforcement(violations, enforcement_level, context)
        elif action['warn']:
            return self._handle_warning_enforcement(violations, context)
        else:
            return self._handle_advisory_enforcement(violations, context)
    
    def _handle_blocking_enforcement(self, violations, level, context):
        """Handle blocking enforcement with possible override"""
        # Log the enforcement action
        self.audit_logger.log_enforcement_action({
            'level': level,
            'violations': violations,
            'context': context,
            'timestamp': time.time(),
            'blocked': True
        })
        
        # Check if override is possible
        if level == 'CRITICAL' or not self._can_override(context):
            return {
                'action': 'BLOCK',
                'allowed': False,
                'message': f'Code blocked due to {len(violations)} critical violations',
                'violations': violations,
                'override_possible': False,
                'required_actions': self._get_required_actions(violations)
            }
        
        # Blocking with override option
        return {
            'action': 'BLOCK_WITH_OVERRIDE',
            'allowed': False,
            'message': f'Code blocked - override available with justification',
            'violations': violations,
            'override_possible': True,
            'override_requirements': self._get_override_requirements(violations, context),
            'required_actions': self._get_required_actions(violations)
        }
    
    def process_override_request(self, override_request):
        """Process request to override enforcement"""
        # Validate override request
        validation = self.override_system.validate_override(override_request)
        
        if not validation['valid']:
            return {
                'approved': False,
                'reason': validation['reason'],
                'requirements': validation['missing_requirements']
            }
        
        # Log override request
        self.audit_logger.log_override_request(override_request)
        
        # Apply override logic
        approval = self._evaluate_override_request(override_request)
        
        if approval['approved']:
            # Create temporary bypass
            bypass_token = self.override_system.create_bypass_token(
                override_request, 
                duration=approval['duration']
            )
            
            return {
                'approved': True,
                'bypass_token': bypass_token,
                'conditions': approval['conditions'],
                'expires_at': approval['expires_at']
            }
        
        return approval
    
    def _get_required_actions(self, violations):
        """Get required actions to resolve violations"""
        actions = []
        
        for violation in violations:
            if violation['type'] == 'god_object':
                actions.append({
                    'action': 'refactor_class',
                    'description': f'Refactor {violation["class_name"]} to reduce responsibilities',
                    'estimated_effort': 'HIGH',
                    'tools_available': ['claude-refactor', 'manual-extraction'],
                    'priority': 'CRITICAL'
                })
            
            elif violation['type'] == 'testing_theatre':
                actions.append({
                    'action': 'improve_tests',
                    'description': f'Add meaningful assertions to {violation["test_method"]}',
                    'estimated_effort': 'MEDIUM',
                    'tools_available': ['claude-test-improve', 'manual-assertions'],
                    'priority': 'HIGH'
                })
        
        return actions
```

## Framework Integration Protocol

```python
class PreventionFrameworkIntegration:
    """Integrates prevention protocols with existing framework"""
    
    def __init__(self):
        self.tdd_integration = TDDPreventionIntegration()
        self.command_integration = CommandPreventionIntegration()
        self.quality_gate_integration = QualityGatePreventionIntegration()
    
    def integrate_with_tdd_cycle(self):
        """Integrate prevention with TDD cycle"""
        return {
            'red_phase': {
                'triggers': ['test_quality_check', 'assertion_guidance'],
                'prevention': ['testing_theatre_prevention'],
                'education': ['effective_testing_practices']
            },
            'green_phase': {
                'triggers': ['implementation_quality_check', 'pattern_guidance'],
                'prevention': ['god_object_prevention', 'pattern_smell_prevention'],
                'education': ['clean_code_practices', 'design_patterns']
            },
            'refactor_phase': {
                'triggers': ['architecture_analysis', 'refactoring_suggestions'],
                'prevention': ['all_anti_patterns'],
                'education': ['refactoring_techniques', 'architecture_principles']
            }
        }
    
    def integrate_with_commands(self):
        """Integrate prevention with framework commands"""
        return {
            '/task': {
                'prevention_focus': ['god_object', 'testing_theatre'],
                'real_time_triggers': True,
                'enforcement_level': 'WARNING'
            },
            '/feature': {
                'prevention_focus': ['architecture_patterns', 'design_patterns'],
                'real_time_triggers': True,
                'enforcement_level': 'BLOCKING'
            },
            '/query': {
                'prevention_focus': ['none'],  # Read-only operation
                'educational_opportunities': True
            }
        }
```

## Configuration and Customization

```yaml
# .claude/config/prevention-protocols.yaml
prevention:
  enabled: true
  real_time_triggers: true
  enforcement_enabled: true
  education_enabled: true

triggers:
  git_hooks:
    pre_commit: true
    pre_push: true
    post_commit: true
    
  ide_integration:
    real_time: true
    debounce_delay: 2.0
    popup_threshold: "HIGH"
    
  quality_gates:
    blocking_violations: ["CRITICAL"]
    warning_violations: ["HIGH", "MEDIUM"]

education:
  adaptive_learning: true
  user_level_detection: true
  progress_tracking: true
  reinforcement_schedule: "spaced_repetition"

enforcement:
  default_level: "WARNING"
  override_system: true
  audit_logging: true
  
  level_mapping:
    god_object: "BLOCKING"
    testing_theatre: "BLOCKING"
    hallucinated_architecture: "CRITICAL"
    pattern_smell: "WARNING"
```

This prevention protocols framework provides comprehensive, proactive protection against anti-patterns through real-time detection, intelligent suggestions, adaptive education, and configurable enforcement mechanisms.