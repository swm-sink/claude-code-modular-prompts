# Dynamic Context Management

| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-20   | production |

## Purpose

Real-time context adaptation engine with .llm/ directory management, context versioning, dynamic context switching mechanisms, and comprehensive performance monitoring for optimal development workflow efficiency.

## Architecture Overview

```xml
<dynamic_context_management version="1.0.0" enforcement="CRITICAL">
  <purpose>Real-time context adaptation with intelligent management and optimization</purpose>
  
  <core_components>
    <component name="llm_directory_manager">
      <description>Manages .llm/ directory structure and file organization</description>
      <responsibilities>File lifecycle, versioning, cleanup, access control</responsibilities>
      <optimization>Intelligent caching, lazy loading, batch operations</optimization>
    </component>
    
    <component name="context_versioning_system">
      <description>Tracks context evolution and enables rollback capabilities</description>
      <responsibilities>Version tracking, diff management, rollback procedures</responsibilities>
      <optimization>Incremental versioning, compression, smart diff algorithms</optimization>
    </component>
    
    <component name="dynamic_switching_engine">
      <description>Real-time context switching based on task requirements</description>
      <responsibilities>Context transition, state preservation, optimization triggers</responsibilities>
      <optimization>Predictive switching, seamless transitions, minimal overhead</optimization>
    </component>
    
    <component name="performance_monitor">
      <description>Comprehensive monitoring and optimization of context operations</description>
      <responsibilities>Metrics collection, performance analysis, optimization suggestions</responsibilities>
      <optimization>Real-time monitoring, automated tuning, bottleneck detection</optimization>
    </component>
  </core_components>
  
  <integration_points>
    <hierarchical_context>Seamless integration with hierarchical context system</hierarchical_context>
    <memory_management>Coordinated with 6-layer memory architecture</memory_management>
    <template_library>Dynamic loading of context templates as needed</template_library>
    <native_features>Optimized for Claude Code's native capabilities</native_features>
  </integration_points>
  
  <performance_requirements>
    <context_switching>< 2 seconds for major context changes</context_switching>
    <file_operations>< 500ms for .llm/ directory operations</file_operations>
    <versioning>< 100ms for version creation and retrieval</versioning>
    <monitoring_overhead>< 5% of total system resources</monitoring_overhead>
  </performance_requirements>
</dynamic_context_management>
```

## .llm/ Directory Management

```python
class LLMDirectoryManager:
    """Comprehensive management of .llm/ directory structure"""
    
    def __init__(self, base_path=".llm/"):
        self.base_path = base_path
        self.directory_structure = {
            'contexts/': 'Active context files and configurations',
            'versions/': 'Context version history and snapshots',
            'templates/': 'Local template cache and customizations',
            'sessions/': 'Session-specific context and state',
            'analytics/': 'Usage analytics and performance metrics',
            'cache/': 'Temporary files and optimized context',
            'config/': 'Directory configuration and preferences'
        }
        self.file_lifecycle = {}
        self.access_patterns = {}
        
    def initialize_directory_structure(self):
        """Initialize .llm/ directory with proper structure"""
        try:
            # Create base directory
            os.makedirs(self.base_path, exist_ok=True)
            
            # Create subdirectories
            for subdir, description in self.directory_structure.items():
                full_path = os.path.join(self.base_path, subdir)
                os.makedirs(full_path, exist_ok=True)
                
                # Create README for documentation
                readme_path = os.path.join(full_path, 'README.md')
                if not os.path.exists(readme_path):
                    self._create_directory_readme(readme_path, description)
                    
            # Initialize configuration
            self._initialize_config()
            
            return {'status': 'success', 'structure': self.directory_structure}
            
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
            
    def manage_file_lifecycle(self, file_path: str, operation: str) -> dict:
        """Manage file lifecycle with intelligent cleanup"""
        operations = {
            'create': self._handle_file_creation,
            'update': self._handle_file_update,
            'access': self._handle_file_access,
            'cleanup': self._handle_file_cleanup,
            'archive': self._handle_file_archive
        }
        
        if operation not in operations:
            return {'status': 'error', 'error': f'Unknown operation: {operation}'}
            
        try:
            result = operations[operation](file_path)
            self._update_access_patterns(file_path, operation)
            return result
            
        except Exception as e:
            return {'status': 'error', 'error': str(e), 'operation': operation}
            
    def _handle_file_creation(self, file_path: str) -> dict:
        """Handle new file creation with metadata"""
        full_path = self._get_full_path(file_path)
        
        # Create file metadata
        metadata = {
            'created_at': time.time(),
            'version': 1,
            'size': 0,
            'access_count': 0,
            'last_modified': time.time(),
            'lifecycle_stage': 'active'
        }
        
        self.file_lifecycle[file_path] = metadata
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        return {'status': 'created', 'path': full_path, 'metadata': metadata}
        
    def _handle_file_cleanup(self, file_path: str = None) -> dict:
        """Intelligent file cleanup based on usage patterns"""
        cleanup_rules = {
            'age_threshold': 7 * 24 * 3600,  # 7 days
            'access_threshold': 5,  # Minimum access count
            'size_threshold': 10 * 1024 * 1024,  # 10MB
            'cache_retention': 24 * 3600  # 24 hours for cache
        }
        
        cleaned_files = []
        current_time = time.time()
        
        for tracked_file, metadata in self.file_lifecycle.items():
            should_cleanup = False
            cleanup_reason = []
            
            # Check age
            age = current_time - metadata['created_at']
            if age > cleanup_rules['age_threshold'] and metadata['access_count'] < cleanup_rules['access_threshold']:
                should_cleanup = True
                cleanup_reason.append('old_unused')
                
            # Check if in cache directory
            if 'cache/' in tracked_file:
                cache_age = current_time - metadata['last_modified']
                if cache_age > cleanup_rules['cache_retention']:
                    should_cleanup = True
                    cleanup_reason.append('cache_expired')
                    
            if should_cleanup:
                cleanup_result = self._cleanup_file(tracked_file, cleanup_reason)
                cleaned_files.append(cleanup_result)
                
        return {'status': 'completed', 'cleaned_files': cleaned_files}
        
    def optimize_directory_structure(self) -> dict:
        """Optimize directory structure based on usage patterns"""
        optimization_results = {
            'structure_changes': [],
            'performance_improvements': [],
            'space_savings': 0,
            'access_optimizations': []
        }
        
        # Analyze access patterns
        access_analysis = self._analyze_access_patterns()
        
        # Optimize frequently accessed files
        for file_path, access_data in access_analysis['frequent_files'].items():
            if access_data['access_frequency'] > 10:  # Frequently accessed
                optimization = self._optimize_file_access(file_path, access_data)
                optimization_results['access_optimizations'].append(optimization)
                
        # Consolidate related files
        consolidation_opportunities = self._identify_consolidation_opportunities()
        for opportunity in consolidation_opportunities:
            consolidation_result = self._consolidate_files(opportunity)
            optimization_results['structure_changes'].append(consolidation_result)
            
        # Compress infrequently accessed files
        compression_candidates = self._identify_compression_candidates()
        for candidate in compression_candidates:
            compression_result = self._compress_file(candidate)
            optimization_results['space_savings'] += compression_result.get('space_saved', 0)
            
        return optimization_results
        
    def get_directory_health(self) -> dict:
        """Comprehensive directory health assessment"""
        health_metrics = {
            'total_files': len(self.file_lifecycle),
            'total_size': self._calculate_total_size(),
            'active_files': self._count_active_files(),
            'cache_efficiency': self._calculate_cache_efficiency(),
            'access_distribution': self._analyze_access_distribution(),
            'cleanup_candidates': self._identify_cleanup_candidates(),
            'optimization_score': 0.0
        }
        
        # Calculate optimization score
        factors = [
            ('cache_efficiency', health_metrics['cache_efficiency'], 0.3),
            ('access_distribution', self._score_access_distribution(health_metrics['access_distribution']), 0.3),
            ('cleanup_health', 1.0 - (len(health_metrics['cleanup_candidates']) / max(health_metrics['total_files'], 1)), 0.2),
            ('size_efficiency', self._score_size_efficiency(health_metrics['total_size']), 0.2)
        ]
        
        optimization_score = sum(weight * score for _, score, weight in factors)
        health_metrics['optimization_score'] = optimization_score
        
        return health_metrics

# Usage patterns
def setup_llm_directory():
    """Example: Set up .llm/ directory for project"""
    manager = LLMDirectoryManager()
    
    # Initialize directory structure
    init_result = manager.initialize_directory_structure()
    
    # Create initial context files
    context_files = [
        'contexts/project_context.json',
        'contexts/user_preferences.json',
        'sessions/current_session.json'
    ]
    
    for file_path in context_files:
        manager.manage_file_lifecycle(file_path, 'create')
        
    return init_result
```

## Context Versioning System

```python
class ContextVersioningSystem:
    """Advanced context versioning with rollback capabilities"""
    
    def __init__(self, llm_manager: LLMDirectoryManager):
        self.llm_manager = llm_manager
        self.version_storage = os.path.join(llm_manager.base_path, 'versions')
        self.version_index = {}
        self.diff_engine = ContextDiffEngine()
        self.compression_engine = ContextCompressionEngine()
        
    def create_version(self, context_id: str, context_data: dict, metadata: dict = None) -> dict:
        """Create new version of context with intelligent diffing"""
        try:
            # Generate version ID
            version_id = self._generate_version_id(context_id)
            
            # Get previous version for diffing
            previous_version = self._get_latest_version(context_id)
            
            if previous_version:
                # Create incremental diff
                diff = self.diff_engine.create_diff(previous_version['data'], context_data)
                storage_data = {
                    'type': 'incremental',
                    'base_version': previous_version['version_id'],
                    'diff': diff,
                    'metadata': metadata or {}
                }
            else:
                # First version - store complete data
                storage_data = {
                    'type': 'complete',
                    'data': context_data,
                    'metadata': metadata or {}
                }
                
            # Compress if beneficial
            if self._should_compress(storage_data):
                storage_data = self.compression_engine.compress(storage_data)
                storage_data['compressed'] = True
                
            # Store version
            version_path = self._get_version_path(context_id, version_id)
            self._store_version(version_path, storage_data)
            
            # Update index
            self._update_version_index(context_id, version_id, storage_data)
            
            return {
                'status': 'success',
                'version_id': version_id,
                'context_id': context_id,
                'storage_type': storage_data['type'],
                'compressed': storage_data.get('compressed', False)
            }
            
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
            
    def retrieve_version(self, context_id: str, version_id: str = None) -> dict:
        """Retrieve specific version or latest version"""
        try:
            if version_id is None:
                version_id = self._get_latest_version_id(context_id)
                
            if not version_id:
                return {'status': 'error', 'error': 'No versions found'}
                
            # Get version data
            version_data = self._load_version(context_id, version_id)
            
            if version_data['type'] == 'incremental':
                # Reconstruct from diffs
                reconstructed_data = self._reconstruct_from_diffs(context_id, version_id)
                return {
                    'status': 'success',
                    'version_id': version_id,
                    'data': reconstructed_data,
                    'metadata': version_data.get('metadata', {})
                }
            else:
                # Complete version
                return {
                    'status': 'success',
                    'version_id': version_id,
                    'data': version_data['data'],
                    'metadata': version_data.get('metadata', {})
                }
                
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
            
    def rollback_to_version(self, context_id: str, target_version_id: str) -> dict:
        """Rollback context to specific version"""
        try:
            # Retrieve target version
            target_version = self.retrieve_version(context_id, target_version_id)
            
            if target_version['status'] != 'success':
                return {'status': 'error', 'error': 'Target version not found'}
                
            # Create rollback version
            rollback_metadata = {
                'rollback': True,
                'rollback_from': self._get_latest_version_id(context_id),
                'rollback_to': target_version_id,
                'rollback_timestamp': time.time()
            }
            
            rollback_result = self.create_version(
                context_id, 
                target_version['data'], 
                rollback_metadata
            )
            
            return {
                'status': 'success',
                'rollback_version': rollback_result['version_id'],
                'target_version': target_version_id,
                'data': target_version['data']
            }
            
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
            
    def get_version_history(self, context_id: str) -> dict:
        """Get complete version history for context"""
        if context_id not in self.version_index:
            return {'status': 'error', 'error': 'Context not found'}
            
        versions = self.version_index[context_id]
        
        history = []
        for version_info in versions:
            history.append({
                'version_id': version_info['version_id'],
                'created_at': version_info['created_at'],
                'type': version_info['type'],
                'size': version_info.get('size', 0),
                'metadata': version_info.get('metadata', {})
            })
            
        return {
            'status': 'success',
            'context_id': context_id,
            'total_versions': len(history),
            'history': history
        }
        
    def _reconstruct_from_diffs(self, context_id: str, target_version_id: str) -> dict:
        """Reconstruct context by applying diffs from base version"""
        # Find reconstruction path
        reconstruction_path = self._find_reconstruction_path(context_id, target_version_id)
        
        if not reconstruction_path:
            raise ValueError(f"Cannot reconstruct version {target_version_id}")
            
        # Start with base version
        base_version = reconstruction_path[0]
        base_data = self._load_version(context_id, base_version)['data']
        
        # Apply diffs in sequence
        current_data = base_data
        for version_id in reconstruction_path[1:]:
            version_data = self._load_version(context_id, version_id)
            diff = version_data['diff']
            current_data = self.diff_engine.apply_diff(current_data, diff)
            
        return current_data
        
    def optimize_version_storage(self, context_id: str) -> dict:
        """Optimize version storage through consolidation and compression"""
        optimization_results = {
            'versions_processed': 0,
            'space_saved': 0,
            'consolidations': 0,
            'compressions': 0
        }
        
        if context_id not in self.version_index:
            return optimization_results
            
        versions = self.version_index[context_id]
        
        # Identify optimization opportunities
        optimization_plan = self._create_optimization_plan(versions)
        
        # Execute consolidations
        for consolidation in optimization_plan['consolidations']:
            result = self._consolidate_versions(context_id, consolidation)
            optimization_results['consolidations'] += 1
            optimization_results['space_saved'] += result.get('space_saved', 0)
            
        # Execute compressions
        for compression in optimization_plan['compressions']:
            result = self._compress_version(context_id, compression)
            optimization_results['compressions'] += 1
            optimization_results['space_saved'] += result.get('space_saved', 0)
            
        optimization_results['versions_processed'] = len(versions)
        return optimization_results
```

## Dynamic Context Switching Engine

```python
class DynamicContextSwitchingEngine:
    """Real-time context switching with intelligent optimization"""
    
    def __init__(self, context_manager, versioning_system, template_library):
        self.context_manager = context_manager
        self.versioning_system = versioning_system
        self.template_library = template_library
        self.switching_history = []
        self.active_contexts = {}
        self.switching_rules = {}
        self.performance_optimizer = SwitchingPerformanceOptimizer()
        
    def switch_context(self, target_context: dict, transition_strategy: str = 'optimal') -> dict:
        """Perform intelligent context switching"""
        try:
            # Analyze current context
            current_context = self._get_current_context()
            
            # Plan context transition
            transition_plan = self._plan_context_transition(
                current_context, target_context, transition_strategy
            )
            
            # Execute transition with optimization
            transition_result = self._execute_context_transition(transition_plan)
            
            # Track switching performance
            self._record_switching_metrics(transition_plan, transition_result)
            
            return {
                'status': 'success',
                'transition_plan': transition_plan,
                'execution_time': transition_result['execution_time'],
                'context_id': transition_result['context_id'],
                'optimization_applied': transition_result.get('optimizations', [])
            }
            
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
            
    def _plan_context_transition(self, current: dict, target: dict, strategy: str) -> dict:
        """Plan optimal context transition strategy"""
        strategies = {
            'minimal': self._plan_minimal_transition,
            'optimal': self._plan_optimal_transition,
            'aggressive': self._plan_aggressive_transition,
            'preserving': self._plan_preserving_transition
        }
        
        planner = strategies.get(strategy, self._plan_optimal_transition)
        return planner(current, target)
        
    def _plan_optimal_transition(self, current: dict, target: dict) -> dict:
        """Plan optimal transition balancing speed and preservation"""
        # Analyze context differences
        diff_analysis = self._analyze_context_differences(current, target)
        
        # Identify reusable components
        reusable_components = self._identify_reusable_components(current, target)
        
        # Plan loading strategy
        loading_strategy = self._optimize_loading_strategy(target, reusable_components)
        
        # Plan preservation strategy
        preservation_strategy = self._plan_preservation_strategy(current, diff_analysis)
        
        return {
            'strategy': 'optimal',
            'diff_analysis': diff_analysis,
            'reusable_components': reusable_components,
            'loading_strategy': loading_strategy,
            'preservation_strategy': preservation_strategy,
            'estimated_time': self._estimate_transition_time(loading_strategy),
            'optimizations': self._identify_optimization_opportunities(current, target)
        }
        
    def _execute_context_transition(self, transition_plan: dict) -> dict:
        """Execute context transition with monitoring"""
        start_time = time.time()
        
        # Phase 1: Preserve current context if needed
        if transition_plan['preservation_strategy']['preserve']:
            preservation_result = self._preserve_current_context(
                transition_plan['preservation_strategy']
            )
        else:
            preservation_result = {'status': 'skipped'}
            
        # Phase 2: Prepare new context components
        preparation_result = self._prepare_context_components(
            transition_plan['loading_strategy']
        )
        
        # Phase 3: Apply optimizations
        optimization_result = self._apply_transition_optimizations(
            transition_plan['optimizations']
        )
        
        # Phase 4: Activate new context
        activation_result = self._activate_new_context(preparation_result['context'])
        
        end_time = time.time()
        
        return {
            'execution_time': end_time - start_time,
            'context_id': activation_result['context_id'],
            'preservation': preservation_result,
            'preparation': preparation_result,
            'optimization': optimization_result,
            'activation': activation_result
        }
        
    def configure_switching_rules(self, rules: dict):
        """Configure intelligent switching rules"""
        default_rules = {
            'auto_switch_triggers': {
                'command_change': True,
                'project_change': True,
                'domain_change': True,
                'workflow_change': False
            },
            
            'preservation_rules': {
                'preserve_on_temporary_switch': True,
                'preserve_user_customizations': True,
                'preserve_session_state': True,
                'max_preserved_contexts': 5
            },
            
            'optimization_rules': {
                'enable_predictive_loading': True,
                'enable_background_preparation': True,
                'enable_caching': True,
                'max_cache_size': 50 * 1024 * 1024  # 50MB
            },
            
            'performance_rules': {
                'max_switch_time': 5.0,  # seconds
                'parallel_loading': True,
                'lazy_component_loading': True,
                'compression_threshold': 1024 * 1024  # 1MB
            }
        }
        
        # Merge with provided rules
        self.switching_rules = self._merge_rules(default_rules, rules)
        
    def get_switching_analytics(self) -> dict:
        """Get comprehensive switching analytics"""
        if not self.switching_history:
            return {'status': 'no_data'}
            
        analytics = {
            'total_switches': len(self.switching_history),
            'average_switch_time': self._calculate_average_switch_time(),
            'most_common_transitions': self._analyze_common_transitions(),
            'performance_trends': self._analyze_performance_trends(),
            'optimization_effectiveness': self._analyze_optimization_effectiveness(),
            'bottlenecks': self._identify_switching_bottlenecks(),
            'recommendations': self._generate_switching_recommendations()
        }
        
        return analytics
        
    def optimize_switching_performance(self) -> dict:
        """Optimize switching performance based on usage patterns"""
        analytics = self.get_switching_analytics()
        
        if analytics.get('status') == 'no_data':
            return {'status': 'insufficient_data'}
            
        optimizations = []
        
        # Optimize common transitions
        for transition in analytics['most_common_transitions']:
            optimization = self._optimize_common_transition(transition)
            optimizations.append(optimization)
            
        # Address bottlenecks
        for bottleneck in analytics['bottlenecks']:
            bottleneck_fix = self._create_bottleneck_fix(bottleneck)
            optimizations.append(bottleneck_fix)
            
        # Apply optimizations
        applied_optimizations = []
        for optimization in optimizations:
            result = self._apply_switching_optimization(optimization)
            if result['status'] == 'success':
                applied_optimizations.append(result)
                
        return {
            'status': 'success',
            'optimizations_applied': len(applied_optimizations),
            'expected_improvement': self._calculate_expected_improvement(applied_optimizations),
            'details': applied_optimizations
        }

# Usage patterns
def intelligent_context_switching():
    """Example: Intelligent context switching"""
    switching_engine = DynamicContextSwitchingEngine(
        context_manager, versioning_system, template_library
    )
    
    # Configure intelligent switching
    switching_engine.configure_switching_rules({
        'auto_switch_triggers': {
            'command_change': True,
            'domain_change': True
        },
        'optimization_rules': {
            'enable_predictive_loading': True,
            'enable_background_preparation': True
        }
    })
    
    # Switch context for new task
    target_context = {
        'domain': 'web_development',
        'project_type': 'react_spa',
        'workflow': 'tdd_strict'
    }
    
    switch_result = switching_engine.switch_context(target_context, 'optimal')
    return switch_result
```

## Performance Monitoring System

```python
class DynamicContextPerformanceMonitor:
    """Comprehensive performance monitoring for dynamic context management"""
    
    def __init__(self):
        self.metrics_collector = MetricsCollector()
        self.performance_analyzer = PerformanceAnalyzer()
        self.optimization_engine = OptimizationEngine()
        self.alert_system = AlertSystem()
        
    def monitor_context_operations(self, operation_type: str, operation_data: dict):
        """Monitor context operations with detailed metrics"""
        start_time = time.time()
        
        # Collect baseline metrics
        baseline_metrics = self._collect_baseline_metrics()
        
        # Monitor operation execution
        operation_metrics = self._monitor_operation_execution(operation_type, operation_data)
        
        # Calculate performance impact
        performance_impact = self._calculate_performance_impact(
            baseline_metrics, operation_metrics
        )
        
        # Store metrics
        self.metrics_collector.store_metrics({
            'operation_type': operation_type,
            'start_time': start_time,
            'end_time': time.time(),
            'baseline': baseline_metrics,
            'operation': operation_metrics,
            'impact': performance_impact
        })
        
        # Check for alerts
        self._check_performance_alerts(performance_impact)
        
    def _collect_baseline_metrics(self) -> dict:
        """Collect baseline performance metrics"""
        return {
            'memory_usage': self._get_memory_usage(),
            'context_cache_size': self._get_context_cache_size(),
            'active_contexts': self._count_active_contexts(),
            'file_handles': self._count_file_handles(),
            'cpu_usage': self._get_cpu_usage()
        }
        
    def _monitor_operation_execution(self, operation_type: str, operation_data: dict) -> dict:
        """Monitor specific operation execution"""
        monitoring_strategies = {
            'context_switch': self._monitor_context_switch,
            'version_create': self._monitor_version_create,
            'template_load': self._monitor_template_load,
            'file_operation': self._monitor_file_operation,
            'cache_operation': self._monitor_cache_operation
        }
        
        monitor_func = monitoring_strategies.get(operation_type, self._monitor_generic_operation)
        return monitor_func(operation_data)
        
    def generate_performance_report(self, time_period: int = 3600) -> dict:
        """Generate comprehensive performance report"""
        end_time = time.time()
        start_time = end_time - time_period
        
        # Get metrics for time period
        period_metrics = self.metrics_collector.get_metrics_for_period(start_time, end_time)
        
        # Analyze performance
        analysis = self.performance_analyzer.analyze_metrics(period_metrics)
        
        report = {
            'period': {
                'start': start_time,
                'end': end_time,
                'duration': time_period
            },
            'summary': {
                'total_operations': len(period_metrics),
                'average_operation_time': analysis['average_operation_time'],
                'slowest_operations': analysis['slowest_operations'],
                'most_frequent_operations': analysis['most_frequent_operations']
            },
            'performance_trends': analysis['trends'],
            'bottlenecks': analysis['bottlenecks'],
            'optimization_opportunities': analysis['optimizations'],
            'alerts_triggered': self.alert_system.get_alerts_for_period(start_time, end_time),
            'recommendations': self._generate_performance_recommendations(analysis)
        }
        
        return report
        
    def optimize_performance(self) -> dict:
        """Automatically optimize performance based on metrics"""
        # Analyze current performance
        current_metrics = self._get_current_performance_metrics()
        
        # Identify optimization opportunities
        opportunities = self.optimization_engine.identify_opportunities(current_metrics)
        
        # Apply optimizations
        applied_optimizations = []
        for opportunity in opportunities:
            if opportunity['confidence'] > 0.8:  # High confidence optimizations only
                result = self._apply_optimization(opportunity)
                if result['status'] == 'success':
                    applied_optimizations.append(result)
                    
        # Measure improvement
        post_optimization_metrics = self._get_current_performance_metrics()
        improvement = self._calculate_improvement(current_metrics, post_optimization_metrics)
        
        return {
            'status': 'success',
            'optimizations_applied': len(applied_optimizations),
            'performance_improvement': improvement,
            'details': applied_optimizations
        }
        
    def setup_real_time_monitoring(self, config: dict = None) -> dict:
        """Setup real-time performance monitoring"""
        default_config = {
            'monitoring_interval': 30,  # seconds
            'alert_thresholds': {
                'operation_time': 5.0,  # seconds
                'memory_usage': 0.8,  # 80% of limit
                'cache_hit_ratio': 0.7,  # 70% minimum
                'error_rate': 0.05  # 5% maximum
            },
            'auto_optimization': True,
            'detailed_logging': False
        }
        
        monitoring_config = {**default_config, **(config or {})}
        
        # Start monitoring thread
        monitoring_thread = self._start_monitoring_thread(monitoring_config)
        
        return {
            'status': 'started',
            'monitoring_thread_id': monitoring_thread.ident,
            'config': monitoring_config
        }

# Usage patterns
def comprehensive_performance_monitoring():
    """Example: Comprehensive performance monitoring setup"""
    monitor = DynamicContextPerformanceMonitor()
    
    # Setup real-time monitoring
    monitoring_config = {
        'monitoring_interval': 15,
        'alert_thresholds': {
            'operation_time': 3.0,
            'memory_usage': 0.75,
            'cache_hit_ratio': 0.8
        },
        'auto_optimization': True
    }
    
    monitor.setup_real_time_monitoring(monitoring_config)
    
    # Monitor context switch operation
    context_switch_data = {
        'from_context': 'web_development',
        'to_context': 'data_science',
        'strategy': 'optimal'
    }
    
    monitor.monitor_context_operations('context_switch', context_switch_data)
    
    # Generate performance report
    report = monitor.generate_performance_report(3600)  # Last hour
    
    return report
```

## Integration Architecture

```xml
<integration_architecture>
  <component_coordination>
    <llm_directory_manager>
      <integration>Provides file system foundation for all other components</integration>
      <coordination>Manages file lifecycle for versioning and switching systems</coordination>
    </llm_directory_manager>
    
    <context_versioning_system>
      <integration>Uses LLM directory for version storage and management</integration>
      <coordination>Provides rollback capabilities for context switching</coordination>
    </context_versioning_system>
    
    <dynamic_switching_engine>
      <integration>Leverages versioning for context preservation and rollback</integration>
      <coordination>Uses template library for context composition</coordination>
    </dynamic_switching_engine>
    
    <performance_monitor>
      <integration>Monitors all other components for optimization opportunities</integration>
      <coordination>Provides feedback loop for continuous improvement</coordination>
    </performance_monitor>
  </component_coordination>
  
  <framework_integration>
    <hierarchical_context>Provides context hierarchy management for dynamic switching</hierarchical_context>
    <memory_management>Coordinates memory allocation with context switching</memory_management>
    <template_library>Sources context templates for dynamic adaptation</template_library>
    <native_features>Optimizes for Claude Code's parallel execution capabilities</native_features>
  </framework_integration>
  
  <performance_optimization>
    <parallel_operations>Leverage Claude Code's parallel tool execution</parallel_operations>
    <intelligent_caching>Cache frequently used contexts and templates</intelligent_caching>
    <predictive_loading>Pre-load likely needed contexts based on patterns</predictive_loading>
    <background_optimization>Optimize contexts during idle periods</background_optimization>
  </performance_optimization>
</integration_architecture>
```

## Performance Targets & Success Metrics

- **Context Switching**: <2 seconds for major context changes
- **File Operations**: <500ms for .llm/ directory operations  
- **Version Management**: <100ms for version creation/retrieval
- **Memory Efficiency**: >90% effective utilization of allocated memory
- **Cache Hit Ratio**: >85% for frequently accessed contexts
- **Optimization Effectiveness**: >30% performance improvement from auto-optimization
- **Error Rate**: <1% for all context operations
- **Recovery Time**: <5 seconds for error recovery and rollback

<function_calls>
<invoke name="TodoWrite">
<parameter name="todos">[{"id": "I21", "content": "I21 - Hierarchical Context System: Build multi-level context hierarchy with dynamic loading and @ imports", "status": "completed", "priority": "high"}, {"id": "I22", "content": "I22 - Memory Management Architecture: Optimize memory usage with 6-layer hierarchical system", "status": "completed", "priority": "high"}, {"id": "I23", "content": "I23 - Native Claude Code Integration: Maximize native features with parallel tool execution", "status": "completed", "priority": "high"}, {"id": "I24", "content": "I24 - Context Templates Library: Create reusable domain-specific context templates", "status": "completed", "priority": "high"}, {"id": "I25", "content": "I25 - Dynamic Context Management: Enable real-time adaptation with .llm/ directory management", "status": "completed", "priority": "high"}]