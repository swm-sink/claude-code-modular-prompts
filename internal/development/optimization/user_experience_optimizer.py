#!/usr/bin/env python3
"""
User Experience Optimizer for Claude Code Modular Framework

This module provides comprehensive user experience enhancements including:
- Immediate feedback for user actions
- Progressive loading indicators
- Real-time performance visibility
- Intuitive error handling and recovery
- Predictive user assistance

Agent 5: Performance & Optimization Engineer
Target: 95% user satisfaction, sub-second response times, intuitive interactions
"""

import time
import asyncio
import threading
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass
from datetime import datetime
import json
import logging
from pathlib import Path
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FeedbackType(Enum):
    """Types of user feedback."""
    IMMEDIATE = "immediate"
    PROGRESS = "progress"
    COMPLETION = "completion"
    ERROR = "error"
    SUCCESS = "success"
    WARNING = "warning"


class UserActionType(Enum):
    """Types of user actions."""
    COMMAND_EXECUTION = "command_execution"
    FILE_OPERATION = "file_operation"
    ANALYSIS_REQUEST = "analysis_request"
    OPTIMIZATION_REQUEST = "optimization_request"
    VALIDATION_REQUEST = "validation_request"


@dataclass
class UserFeedback:
    """User feedback message."""
    type: FeedbackType
    message: str
    timestamp: datetime
    action_id: str
    progress_percent: Optional[float] = None
    estimated_time_remaining: Optional[float] = None
    details: Optional[Dict[str, Any]] = None


@dataclass
class UserAction:
    """User action tracking."""
    action_id: str
    action_type: UserActionType
    description: str
    start_time: datetime
    estimated_duration: float
    status: str = "started"
    progress_percent: float = 0.0
    result: Optional[Any] = None


class ImmediateFeedbackProvider:
    """Provides immediate feedback for user actions."""
    
    def __init__(self):
        self.feedback_callbacks = []
        self.action_history = []
        
    def register_feedback_callback(self, callback: Callable[[UserFeedback], None]):
        """Register a callback for feedback delivery."""
        self.feedback_callbacks.append(callback)
    
    def provide_immediate_feedback(self, action_type: UserActionType, message: str, 
                                 action_id: str, details: Optional[Dict] = None):
        """Provide immediate feedback for user action."""
        feedback = UserFeedback(
            type=FeedbackType.IMMEDIATE,
            message=message,
            timestamp=datetime.now(),
            action_id=action_id,
            details=details
        )
        
        self._deliver_feedback(feedback)
        
        # Console output for immediate visibility
        timestamp_str = feedback.timestamp.strftime("%H:%M:%S")
        print(f"[{timestamp_str}] 🚀 {message}")
        
        if details:
            for key, value in details.items():
                print(f"         {key}: {value}")
    
    def provide_progress_feedback(self, action_id: str, progress_percent: float, 
                                message: str, estimated_time_remaining: Optional[float] = None):
        """Provide progress feedback for ongoing operations."""
        feedback = UserFeedback(
            type=FeedbackType.PROGRESS,
            message=message,
            timestamp=datetime.now(),
            action_id=action_id,
            progress_percent=progress_percent,
            estimated_time_remaining=estimated_time_remaining
        )
        
        self._deliver_feedback(feedback)
        
        # Console progress bar
        bar_length = 30
        filled_length = int(bar_length * progress_percent // 100)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        
        time_remaining = f" | ETA: {estimated_time_remaining:.1f}s" if estimated_time_remaining else ""
        print(f"\r⏳ [{bar}] {progress_percent:.1f}% {message}{time_remaining}", end='', flush=True)
        
        if progress_percent >= 100:
            print()  # New line after completion
    
    def provide_completion_feedback(self, action_id: str, success: bool, 
                                  message: str, result: Optional[Any] = None):
        """Provide completion feedback."""
        feedback_type = FeedbackType.SUCCESS if success else FeedbackType.ERROR
        
        feedback = UserFeedback(
            type=feedback_type,
            message=message,
            timestamp=datetime.now(),
            action_id=action_id,
            details={'result': result, 'success': success}
        )
        
        self._deliver_feedback(feedback)
        
        # Console completion message
        timestamp_str = feedback.timestamp.strftime("%H:%M:%S")
        icon = "✅" if success else "❌"
        print(f"[{timestamp_str}] {icon} {message}")
        
        if result and isinstance(result, dict):
            for key, value in result.items():
                print(f"         {key}: {value}")
    
    def _deliver_feedback(self, feedback: UserFeedback):
        """Deliver feedback to registered callbacks."""
        for callback in self.feedback_callbacks:
            try:
                callback(feedback)
            except Exception as e:
                logger.error(f"Feedback callback error: {e}")


class ProgressiveLoadingManager:
    """Manages progressive loading for complex operations."""
    
    def __init__(self, feedback_provider: ImmediateFeedbackProvider):
        self.feedback_provider = feedback_provider
        self.active_operations = {}
        
    def start_progressive_operation(self, action_id: str, description: str, 
                                  estimated_duration: float, steps: List[str]) -> UserAction:
        """Start a progressive loading operation."""
        action = UserAction(
            action_id=action_id,
            action_type=UserActionType.COMMAND_EXECUTION,
            description=description,
            start_time=datetime.now(),
            estimated_duration=estimated_duration
        )
        
        self.active_operations[action_id] = {
            'action': action,
            'steps': steps,
            'current_step': 0,
            'step_start_time': time.time()
        }
        
        # Provide immediate feedback
        self.feedback_provider.provide_immediate_feedback(
            action_type=action.action_type,
            message=f"Starting: {description}",
            action_id=action_id,
            details={
                'estimated_duration': f"{estimated_duration:.1f}s",
                'total_steps': len(steps)
            }
        )
        
        return action
    
    def update_progress(self, action_id: str, step_completed: bool = False, 
                       custom_message: Optional[str] = None):
        """Update progress for an ongoing operation."""
        if action_id not in self.active_operations:
            return
        
        operation = self.active_operations[action_id]
        action = operation['action']
        steps = operation['steps']
        
        if step_completed:
            operation['current_step'] = min(operation['current_step'] + 1, len(steps))
            operation['step_start_time'] = time.time()
        
        # Calculate progress
        current_step = operation['current_step']
        progress_percent = (current_step / len(steps)) * 100
        
        # Estimate remaining time
        elapsed_time = time.time() - action.start_time.timestamp()
        if progress_percent > 0:
            estimated_total = elapsed_time * 100 / progress_percent
            estimated_remaining = max(0, estimated_total - elapsed_time)
        else:
            estimated_remaining = action.estimated_duration
        
        # Current step message
        if current_step < len(steps):
            step_message = steps[current_step]
        else:
            step_message = "Finalizing..."
        
        message = custom_message or f"Step {current_step + 1}/{len(steps)}: {step_message}"
        
        # Provide progress feedback
        self.feedback_provider.provide_progress_feedback(
            action_id=action_id,
            progress_percent=progress_percent,
            message=message,
            estimated_time_remaining=estimated_remaining
        )
        
        # Update action
        action.progress_percent = progress_percent
        action.status = "completed" if progress_percent >= 100 else "in_progress"
    
    def complete_operation(self, action_id: str, success: bool, 
                         result: Optional[Any] = None, message: Optional[str] = None):
        """Complete a progressive operation."""
        if action_id not in self.active_operations:
            return
        
        operation = self.active_operations[action_id]
        action = operation['action']
        
        # Final progress update
        self.feedback_provider.provide_progress_feedback(
            action_id=action_id,
            progress_percent=100.0,
            message="Completing...",
            estimated_time_remaining=0.0
        )
        
        # Completion feedback
        elapsed_time = time.time() - action.start_time.timestamp()
        completion_message = message or (
            f"Completed: {action.description} in {elapsed_time:.1f}s"
            if success else f"Failed: {action.description}"
        )
        
        self.feedback_provider.provide_completion_feedback(
            action_id=action_id,
            success=success,
            message=completion_message,
            result=result
        )
        
        # Update action
        action.status = "completed" if success else "failed"
        action.result = result
        
        # Clean up
        del self.active_operations[action_id]


class RealTimeVisibilityDashboard:
    """Provides real-time visibility into system performance."""
    
    def __init__(self):
        self.metrics = {}
        self.active_operations = {}
        self.performance_history = []
        self.update_interval = 1.0  # Update every second
        self.monitoring_active = False
        
    def start_monitoring(self):
        """Start real-time monitoring."""
        self.monitoring_active = True
        
        def monitor_loop():
            while self.monitoring_active:
                self._update_metrics()
                self._display_dashboard()
                time.sleep(self.update_interval)
        
        monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
        monitor_thread.start()
    
    def stop_monitoring(self):
        """Stop real-time monitoring."""
        self.monitoring_active = False
    
    def register_operation(self, action_id: str, operation_type: str, description: str):
        """Register an operation for monitoring."""
        self.active_operations[action_id] = {
            'type': operation_type,
            'description': description,
            'start_time': time.time(),
            'status': 'active'
        }
    
    def update_operation_status(self, action_id: str, status: str, result: Optional[Any] = None):
        """Update operation status."""
        if action_id in self.active_operations:
            self.active_operations[action_id]['status'] = status
            self.active_operations[action_id]['result'] = result
            
            if status in ['completed', 'failed']:
                # Move to history
                operation = self.active_operations[action_id]
                operation['end_time'] = time.time()
                operation['duration'] = operation['end_time'] - operation['start_time']
                
                self.performance_history.append(operation)
                del self.active_operations[action_id]
                
                # Keep only last 50 operations
                if len(self.performance_history) > 50:
                    self.performance_history = self.performance_history[-50:]
    
    def _update_metrics(self):
        """Update system metrics."""
        try:
            import psutil
            
            self.metrics = {
                'cpu_percent': psutil.cpu_percent(),
                'memory_percent': psutil.virtual_memory().percent,
                'active_operations': len(self.active_operations),
                'completed_operations': len(self.performance_history),
                'timestamp': datetime.now().isoformat()
            }
        except ImportError:
            # Fallback metrics if psutil not available
            self.metrics = {
                'active_operations': len(self.active_operations),
                'completed_operations': len(self.performance_history),
                'timestamp': datetime.now().isoformat()
            }
    
    def _display_dashboard(self):
        """Display real-time dashboard (simplified console version)."""
        # Clear previous dashboard (simplified)
        print("\n" + "="*60)
        print("🚀 Real-Time Performance Dashboard")
        print("="*60)
        
        # System metrics
        if 'cpu_percent' in self.metrics:
            print(f"💻 System: CPU {self.metrics['cpu_percent']:.1f}% | Memory {self.metrics['memory_percent']:.1f}%")
        
        # Active operations
        print(f"⚡ Active Operations: {self.metrics['active_operations']}")
        for action_id, operation in self.active_operations.items():
            elapsed = time.time() - operation['start_time']
            print(f"   📋 {operation['description']} ({elapsed:.1f}s)")
        
        # Recent completions
        if self.performance_history:
            recent_ops = self.performance_history[-3:]  # Last 3 operations
            print(f"✅ Recent Completions:")
            for op in recent_ops:
                status_icon = "✅" if op['status'] == 'completed' else "❌"
                print(f"   {status_icon} {op['description']} ({op['duration']:.1f}s)")
        
        print("="*60)
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary for reporting."""
        if not self.performance_history:
            return {}
        
        durations = [op['duration'] for op in self.performance_history if 'duration' in op]
        
        if not durations:
            return {}
        
        import statistics
        
        return {
            'total_operations': len(self.performance_history),
            'average_duration': statistics.mean(durations),
            'median_duration': statistics.median(durations),
            'min_duration': min(durations),
            'max_duration': max(durations),
            'success_rate': len([op for op in self.performance_history if op['status'] == 'completed']) / len(self.performance_history) * 100
        }


class ErrorRecoveryAssistant:
    """Provides intelligent error handling and recovery assistance."""
    
    def __init__(self, feedback_provider: ImmediateFeedbackProvider):
        self.feedback_provider = feedback_provider
        self.error_patterns = {}
        self.recovery_strategies = {}
        self._initialize_recovery_strategies()
    
    def _initialize_recovery_strategies(self):
        """Initialize common recovery strategies."""
        self.recovery_strategies = {
            'file_not_found': {
                'message': "File not found. Let me help you locate it or create it.",
                'actions': ['search_similar_files', 'create_file_template', 'check_common_locations']
            },
            'permission_denied': {
                'message': "Permission denied. Let me suggest alternative approaches.",
                'actions': ['check_file_permissions', 'suggest_alternative_location', 'create_workaround']
            },
            'timeout_error': {
                'message': "Operation timed out. Let me optimize the approach.",
                'actions': ['break_into_smaller_operations', 'increase_timeout', 'parallel_processing']
            },
            'validation_error': {
                'message': "Validation failed. Let me provide specific guidance.",
                'actions': ['show_validation_details', 'suggest_corrections', 'provide_examples']
            }
        }
    
    def handle_error(self, error: Exception, action_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle error with intelligent recovery assistance."""
        error_type = type(error).__name__
        error_message = str(error)
        
        # Analyze error pattern
        error_pattern = self._analyze_error_pattern(error_type, error_message)
        
        # Get recovery strategy
        recovery_strategy = self._get_recovery_strategy(error_pattern)
        
        # Provide user feedback
        self.feedback_provider.provide_completion_feedback(
            action_id=action_id,
            success=False,
            message=f"Error: {error_message}",
            result={'error_type': error_type, 'recovery_available': recovery_strategy is not None}
        )
        
        # Provide recovery assistance
        if recovery_strategy:
            recovery_message = recovery_strategy['message']
            recovery_actions = recovery_strategy['actions']
            
            self.feedback_provider.provide_immediate_feedback(
                action_type=UserActionType.COMMAND_EXECUTION,
                message=recovery_message,
                action_id=f"{action_id}_recovery",
                details={
                    'recovery_actions': recovery_actions,
                    'error_pattern': error_pattern
                }
            )
            
            return {
                'error_handled': True,
                'recovery_strategy': recovery_strategy,
                'error_pattern': error_pattern
            }
        
        return {
            'error_handled': False,
            'error_type': error_type,
            'error_message': error_message
        }
    
    def _analyze_error_pattern(self, error_type: str, error_message: str) -> str:
        """Analyze error to determine pattern."""
        error_message_lower = error_message.lower()
        
        if 'no such file' in error_message_lower or 'file not found' in error_message_lower:
            return 'file_not_found'
        elif 'permission denied' in error_message_lower:
            return 'permission_denied'
        elif 'timeout' in error_message_lower:
            return 'timeout_error'
        elif 'validation' in error_message_lower or 'invalid' in error_message_lower:
            return 'validation_error'
        else:
            return 'unknown_error'
    
    def _get_recovery_strategy(self, error_pattern: str) -> Optional[Dict[str, Any]]:
        """Get recovery strategy for error pattern."""
        return self.recovery_strategies.get(error_pattern)


class UserExperienceOptimizer:
    """Main user experience optimization coordinator."""
    
    def __init__(self):
        self.feedback_provider = ImmediateFeedbackProvider()
        self.progress_manager = ProgressiveLoadingManager(self.feedback_provider)
        self.dashboard = RealTimeVisibilityDashboard()
        self.error_assistant = ErrorRecoveryAssistant(self.feedback_provider)
        
        # Start monitoring
        self.dashboard.start_monitoring()
        
        # Register console feedback callback
        self.feedback_provider.register_feedback_callback(self._console_feedback_callback)
    
    def _console_feedback_callback(self, feedback: UserFeedback):
        """Default console feedback callback."""
        # This is already handled in the feedback provider
        pass
    
    def optimize_user_operation(self, operation_name: str, operation_func: Callable, 
                               steps: Optional[List[str]] = None, 
                               estimated_duration: float = 5.0) -> Any:
        """
        Optimize user operation with comprehensive UX enhancements.
        
        Args:
            operation_name: Name of the operation
            operation_func: Function to execute
            steps: Optional list of operation steps
            estimated_duration: Estimated duration in seconds
            
        Returns:
            Result of the operation
        """
        import uuid
        action_id = str(uuid.uuid4())
        
        # Default steps if not provided
        if steps is None:
            steps = ["Initialize", "Process", "Validate", "Complete"]
        
        # Start progressive operation
        action = self.progress_manager.start_progressive_operation(
            action_id=action_id,
            description=operation_name,
            estimated_duration=estimated_duration,
            steps=steps
        )
        
        # Register with dashboard
        self.dashboard.register_operation(action_id, "user_operation", operation_name)
        
        try:
            # Execute operation with progress updates
            result = self._execute_with_progress(action_id, operation_func, steps)
            
            # Complete successfully
            self.progress_manager.complete_operation(
                action_id=action_id,
                success=True,
                result=result,
                message=f"Successfully completed: {operation_name}"
            )
            
            self.dashboard.update_operation_status(action_id, "completed", result)
            
            return result
            
        except Exception as e:
            # Handle error with recovery assistance
            error_info = self.error_assistant.handle_error(e, action_id, {
                'operation_name': operation_name,
                'steps': steps
            })
            
            self.progress_manager.complete_operation(
                action_id=action_id,
                success=False,
                result=error_info,
                message=f"Error in {operation_name}: {str(e)}"
            )
            
            self.dashboard.update_operation_status(action_id, "failed", error_info)
            
            raise
    
    def _execute_with_progress(self, action_id: str, operation_func: Callable, 
                             steps: List[str]) -> Any:
        """Execute operation with progress updates."""
        # Simulate step progression
        for i, step in enumerate(steps):
            self.progress_manager.update_progress(
                action_id=action_id,
                step_completed=i > 0,
                custom_message=f"Step {i+1}/{len(steps)}: {step}"
            )
            
            # Small delay to show progress
            time.sleep(0.1)
        
        # Execute actual operation
        result = operation_func()
        
        # Final progress update
        self.progress_manager.update_progress(
            action_id=action_id,
            step_completed=True,
            custom_message="Operation completed"
        )
        
        return result
    
    def get_user_experience_report(self) -> Dict[str, Any]:
        """Get comprehensive user experience report."""
        return {
            'performance_summary': self.dashboard.get_performance_summary(),
            'active_operations': len(self.dashboard.active_operations),
            'feedback_metrics': {
                'feedback_callbacks': len(self.feedback_provider.feedback_callbacks),
                'action_history': len(self.feedback_provider.action_history)
            },
            'error_handling': {
                'recovery_strategies': len(self.error_assistant.recovery_strategies),
                'error_patterns': len(self.error_assistant.error_patterns)
            },
            'user_satisfaction_targets': {
                'response_time_target': '<1s',
                'success_rate_target': '>95%',
                'user_satisfaction_target': '>95%'
            }
        }


def demonstrate_user_experience_optimization():
    """Demonstrate user experience optimization capabilities."""
    print("🌟 User Experience Optimization Demonstration")
    print("=" * 60)
    
    # Initialize UX optimizer
    ux_optimizer = UserExperienceOptimizer()
    
    # Demonstrate operations with different characteristics
    operations = [
        ("Quick Analysis", lambda: time.sleep(1.0) or "Analysis complete", 
         ["Initialize", "Scan", "Analyze", "Complete"], 1.5),
        ("Complex Processing", lambda: time.sleep(2.0) or "Processing complete", 
         ["Setup", "Process Phase 1", "Process Phase 2", "Validate", "Finalize"], 3.0),
        ("Error Demo", lambda: exec('raise ValueError("Demo error for recovery")'), 
         ["Prepare", "Execute", "Validate"], 1.0)
    ]
    
    results = []
    
    for name, func, steps, duration in operations:
        print(f"\n🚀 Starting: {name}")
        
        try:
            result = ux_optimizer.optimize_user_operation(
                operation_name=name,
                operation_func=func,
                steps=steps,
                estimated_duration=duration
            )
            results.append(result)
            print(f"✅ {name} completed successfully")
            
        except Exception as e:
            print(f"❌ {name} failed: {e}")
            results.append(None)
    
    # Wait for dashboard updates
    time.sleep(2)
    
    # Generate UX report
    print("\n📊 User Experience Report:")
    ux_report = ux_optimizer.get_user_experience_report()
    
    perf_summary = ux_report.get('performance_summary', {})
    if perf_summary:
        print(f"  Average operation duration: {perf_summary.get('average_duration', 0):.1f}s")
        print(f"  Success rate: {perf_summary.get('success_rate', 0):.1f}%")
        print(f"  Total operations: {perf_summary.get('total_operations', 0)}")
    
    print(f"  Active operations: {ux_report['active_operations']}")
    print(f"  Feedback callbacks: {ux_report['feedback_metrics']['feedback_callbacks']}")
    print(f"  Recovery strategies: {ux_report['error_handling']['recovery_strategies']}")
    
    # Stop monitoring
    ux_optimizer.dashboard.stop_monitoring()
    
    return 0


if __name__ == "__main__":
    exit_code = demonstrate_user_experience_optimization()
    exit(exit_code)