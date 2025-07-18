"""
Prompt Testing Sandbox Component
Provides safe execution environment for testing prompts with comprehensive safety validation
"""

import streamlit as st
import json
import time
import psutil
import hashlib
import tempfile
import subprocess
import sys
import io
import contextlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Union, Callable
from dataclasses import dataclass, asdict
import threading
import resource
from contextlib import contextmanager
import logging


@dataclass
class SandboxEnvironment:
    """Configuration for a sandbox execution environment"""
    environment_id: str
    name: str
    description: str = ""
    max_execution_time: float = 30.0
    max_memory_mb: int = 512
    max_output_length: int = 10000
    allowed_modules: List[str] = None
    blocked_modules: List[str] = None
    safety_level: str = "moderate"  # strict, moderate, permissive
    isolation_level: str = "medium"  # low, medium, high
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.allowed_modules is None:
            self.allowed_modules = ["json", "math", "datetime", "random", "string", "re"]
        if self.blocked_modules is None:
            self.blocked_modules = ["subprocess", "os", "sys"]
        if self.metadata is None:
            self.metadata = {}
        
        # Validate configuration
        if self.max_execution_time <= 0:
            raise ValueError("max_execution_time must be positive")
        if self.max_memory_mb <= 0:
            raise ValueError("max_memory_mb must be positive")
        if self.safety_level not in ["strict", "moderate", "permissive"]:
            raise ValueError("safety_level must be strict, moderate, or permissive")
        if self.isolation_level not in ["low", "medium", "high"]:
            raise ValueError("isolation_level must be low, medium, or high")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SandboxEnvironment':
        """Create from dictionary"""
        return cls(**data)
    
    def validate(self) -> tuple[bool, str]:
        """Validate environment configuration"""
        if not self.environment_id:
            return False, "Environment ID is required"
        if not self.name:
            return False, "Environment name is required"
        if self.max_execution_time <= 0:
            return False, "Max execution time must be positive"
        if self.max_memory_mb <= 0:
            return False, "Max memory must be positive"
        if self.safety_level not in ["strict", "moderate", "permissive"]:
            return False, "Safety level must be strict, moderate, or permissive"
        return True, "Valid"
    
    @classmethod
    def create_development_preset(cls) -> 'SandboxEnvironment':
        """Create a development preset environment"""
        return cls(
            environment_id="development",
            name="Development",
            description="Development environment with moderate safety",
            max_execution_time=30.0,
            max_memory_mb=512,
            safety_level="moderate",
            isolation_level="medium"
        )
    
    @classmethod
    def create_production_preset(cls) -> 'SandboxEnvironment':
        """Create a production preset environment"""
        return cls(
            environment_id="production",
            name="Production",
            description="Production environment with strict safety",
            max_execution_time=10.0,
            max_memory_mb=256,
            safety_level="strict",
            isolation_level="high"
        )
    
    @classmethod
    def create_research_preset(cls) -> 'SandboxEnvironment':
        """Create a research preset environment"""
        return cls(
            environment_id="research",
            name="Research",
            description="Research environment with extended resources",
            max_execution_time=60.0,
            max_memory_mb=1024,
            safety_level="permissive",
            isolation_level="low"
        )


@dataclass
class PromptTest:
    """Definition of a prompt test scenario"""
    test_id: str
    name: str
    description: str = ""
    prompt_content: str = ""
    test_inputs: List[Dict[str, Any]] = None
    expected_outputs: List[str] = None
    success_criteria: Dict[str, Any] = None
    environment_id: str = "default"
    timeout: float = 30.0
    max_retries: int = 3
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.test_inputs is None:
            self.test_inputs = []
        if self.expected_outputs is None:
            self.expected_outputs = []
        if self.success_criteria is None:
            self.success_criteria = {}
        if self.metadata is None:
            self.metadata = {}
        
        # Validate
        if not self.test_id:
            raise ValueError("test_id is required")
        if not self.name:
            raise ValueError("name is required")
        if not self.prompt_content:
            raise ValueError("prompt_content is required")
        if self.timeout <= 0:
            raise ValueError("timeout must be positive")
        if self.max_retries < 0:
            raise ValueError("max_retries must be non-negative")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PromptTest':
        """Create from dictionary"""
        return cls(**data)
    
    def validate(self) -> tuple[bool, str]:
        """Validate the prompt test"""
        if not self.test_id:
            return False, "Test ID is required"
        if not self.name:
            return False, "Test name is required"
        if not self.prompt_content:
            return False, "Prompt content is required"
        if self.timeout <= 0:
            return False, "Timeout must be positive"
        return True, "Valid"
    
    def render_prompt(self, inputs: Dict[str, Any]) -> str:
        """Render the prompt with given inputs"""
        try:
            return self.prompt_content.format(**inputs)
        except KeyError as e:
            raise ValueError(f"Missing input variable: {e}")
    
    def evaluate_success_criteria(self, output: str) -> Dict[str, Any]:
        """Evaluate success criteria against output"""
        result = {
            'success': True,
            'score': 1.0,
            'violations': []
        }
        
        violations = []
        score = 1.0
        
        # Check minimum length
        if 'min_length' in self.success_criteria:
            min_len = self.success_criteria['min_length']
            if len(output) < min_len:
                violations.append(f"Output too short: {len(output)} < {min_len}")
                score -= 0.3
        
        # Check maximum length
        if 'max_length' in self.success_criteria:
            max_len = self.success_criteria['max_length']
            if len(output) > max_len:
                violations.append(f"Output too long: {len(output)} > {max_len}")
                score -= 0.2
        
        # Check keywords
        if 'keywords' in self.success_criteria:
            keywords = self.success_criteria['keywords']
            missing_keywords = []
            for keyword in keywords:
                if keyword.lower() not in output.lower():
                    missing_keywords.append(keyword)
            if missing_keywords:
                violations.append(f"Missing keywords: {missing_keywords}")
                score -= 0.3
        
        # Check forbidden words
        if 'forbidden_words' in self.success_criteria:
            forbidden = self.success_criteria['forbidden_words']
            found_forbidden = []
            for word in forbidden:
                if word.lower() in output.lower():
                    found_forbidden.append(word)
            if found_forbidden:
                violations.append(f"Forbidden words found: {found_forbidden}")
                score -= 0.4
        
        result['success'] = len(violations) == 0 and score > 0.5
        result['score'] = max(0.0, score)
        result['violations'] = violations
        
        return result


@dataclass
class ExecutionResult:
    """Result of a prompt execution"""
    result_id: str
    test_id: str
    environment_id: str
    timestamp: Union[datetime, str] = None
    execution_time: float = 0.0
    memory_used_mb: float = 0.0
    success: bool = False
    output: str = ""
    error_message: Optional[str] = None
    safety_violations: List[str] = None
    resource_violations: List[str] = None
    exit_code: int = 0
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
        elif isinstance(self.timestamp, str):
            self.timestamp = datetime.fromisoformat(self.timestamp)
        if self.safety_violations is None:
            self.safety_violations = []
        if self.resource_violations is None:
            self.resource_violations = []
        if self.metadata is None:
            self.metadata = {}
        
        # Validate
        if self.execution_time < 0:
            raise ValueError("execution_time must be non-negative")
        if self.memory_used_mb < 0:
            raise ValueError("memory_used_mb must be non-negative")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        result = asdict(self)
        result['timestamp'] = self.timestamp.isoformat()
        return result
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ExecutionResult':
        """Create from dictionary"""
        if 'timestamp' in data and isinstance(data['timestamp'], str):
            data['timestamp'] = datetime.fromisoformat(data['timestamp'])
        return cls(**data)
    
    def validate(self) -> tuple[bool, str]:
        """Validate the execution result"""
        if not self.result_id:
            return False, "Result ID is required"
        if not self.test_id:
            return False, "Test ID is required"
        if not self.environment_id:
            return False, "Environment ID is required"
        if self.execution_time < 0:
            return False, "Execution time must be non-negative"
        if self.memory_used_mb < 0:
            return False, "Memory usage must be non-negative"
        return True, "Valid"
    
    def get_performance_score(self) -> float:
        """Get performance score (0.0 to 1.0)"""
        # Score based on execution time and memory usage
        # Lower is better for both metrics
        time_score = max(0.0, 1.0 - (self.execution_time / 60.0))  # Normalize to 1 minute
        memory_score = max(0.0, 1.0 - (self.memory_used_mb / 1024.0))  # Normalize to 1 GB
        return (time_score + memory_score) / 2.0
    
    def get_safety_score(self) -> float:
        """Get safety score (0.0 to 1.0)"""
        # Score based on safety violations
        if not self.safety_violations:
            return 1.0
        # Each violation reduces score by 0.2
        return max(0.0, 1.0 - (len(self.safety_violations) * 0.2))
    
    def get_overall_score(self) -> float:
        """Get overall score (0.0 to 1.0)"""
        performance_score = self.get_performance_score()
        safety_score = self.get_safety_score()
        success_score = 1.0 if self.success else 0.0
        
        # Weight: 40% performance, 40% safety, 20% success
        return (performance_score * 0.4 + safety_score * 0.4 + success_score * 0.2)
    
    def has_violations(self) -> bool:
        """Check if result has any violations"""
        return len(self.safety_violations) > 0 or len(self.resource_violations) > 0
    
    def get_violation_summary(self) -> Dict[str, Any]:
        """Get summary of violations"""
        return {
            'safety_violations': self.safety_violations,
            'resource_violations': self.resource_violations,
            'total_violations': len(self.safety_violations) + len(self.resource_violations)
        }


class SafetyValidator:
    """Validates prompt safety and security"""
    
    def __init__(self, safety_level: str = "moderate", blocked_modules: List[str] = None, 
                 blocked_functions: List[str] = None, blocked_keywords: List[str] = None,
                 max_code_length: int = 10000):
        self.safety_level = safety_level
        self.blocked_modules = blocked_modules or ['os', 'subprocess', 'sys']
        self.blocked_functions = blocked_functions or ['exec', 'eval', 'open']
        self.blocked_keywords = blocked_keywords or ['import os', 'import subprocess']
        self.max_code_length = max_code_length
        
        # Predefined patterns for different safety levels
        self.strict_patterns = [
            r'import\s+os',
            r'import\s+sys',
            r'import\s+subprocess',
            r'__import__',
            r'exec\s*\(',
            r'eval\s*\(',
            r'open\s*\(',
            r'file\s*\(',
            r'input\s*\(',
            r'raw_input\s*\(',
        ]
        self.moderate_patterns = [
            r'import\s+os',
            r'import\s+subprocess',
            r'__import__',
            r'exec\s*\(',
            r'eval\s*\(',
        ]
        self.permissive_patterns = [
            r'exec\s*\(',
            r'eval\s*\(',
        ]
    
    def validate_prompt(self, prompt: str) -> Dict[str, Any]:
        """Validate prompt for safety issues"""
        import re
        
        violations = []
        is_safe = True
        
        # Check code length
        if len(prompt) > self.max_code_length:
            violations.append({
                'type': 'code_length',
                'message': f"Code too long: {len(prompt)} > {self.max_code_length}",
                'severity': 'medium'
            })
            is_safe = False
        
        # Check blocked modules
        for module in self.blocked_modules:
            pattern = rf'import\s+{re.escape(module)}'
            if re.search(pattern, prompt, re.IGNORECASE):
                violations.append({
                    'type': 'blocked_module',
                    'message': f"Blocked module detected: {module}",
                    'severity': 'high'
                })
                is_safe = False
        
        # Check blocked functions
        for func in self.blocked_functions:
            pattern = rf'{re.escape(func)}\s*\('
            if re.search(pattern, prompt, re.IGNORECASE):
                violations.append({
                    'type': 'blocked_function',
                    'message': f"Blocked function detected: {func}",
                    'severity': 'high'
                })
                is_safe = False
        
        # Check blocked keywords
        for keyword in self.blocked_keywords:
            if keyword.lower() in prompt.lower():
                violations.append({
                    'type': 'blocked_keyword',
                    'message': f"Blocked keyword detected: {keyword}",
                    'severity': 'medium'
                })
                is_safe = False
        
        # Check dangerous patterns
        patterns = self._get_patterns()
        for pattern in patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                violations.append({
                    'type': 'dangerous_pattern',
                    'message': f"Potentially unsafe pattern detected: {pattern}",
                    'severity': 'high'
                })
                is_safe = False
        
        return {
            'is_safe': is_safe,
            'violations': violations,
            'safety_level': self.safety_level
        }
    
    def validate_code(self, code: str) -> Dict[str, Any]:
        """Validate code for safety issues"""
        return self.validate_prompt(code)
    
    def analyze_code(self, code: str) -> Dict[str, Any]:
        """Analyze code for detailed safety assessment"""
        result = self.validate_code(code)
        
        # Add additional analysis
        result['analysis'] = {
            'code_length': len(code),
            'line_count': len(code.split('\n')),
            'safety_score': self._calculate_safety_score(result['violations']),
            'recommendations': self._generate_recommendations(result['violations'])
        }
        
        return result
    
    def _calculate_safety_score(self, violations: List[Dict]) -> float:
        """Calculate safety score based on violations"""
        if not violations:
            return 1.0
        
        score = 1.0
        for violation in violations:
            if violation['severity'] == 'high':
                score -= 0.3
            elif violation['severity'] == 'medium':
                score -= 0.2
            else:
                score -= 0.1
        
        return max(0.0, score)
    
    def _generate_recommendations(self, violations: List[Dict]) -> List[str]:
        """Generate recommendations based on violations"""
        recommendations = []
        
        violation_types = [v['type'] for v in violations]
        
        if 'blocked_module' in violation_types:
            recommendations.append("Consider using safer alternatives to blocked modules")
        
        if 'blocked_function' in violation_types:
            recommendations.append("Replace blocked functions with safer alternatives")
        
        if 'code_length' in violation_types:
            recommendations.append("Consider breaking down long code into smaller functions")
        
        if 'dangerous_pattern' in violation_types:
            recommendations.append("Review and sanitize potentially dangerous code patterns")
        
        return recommendations
    
    def _get_patterns(self) -> List[str]:
        """Get patterns based on safety level"""
        if self.safety_level == "strict":
            return self.strict_patterns
        elif self.safety_level == "moderate":
            return self.moderate_patterns
        else:
            return self.permissive_patterns
    
    @classmethod
    def create_strict_preset(cls) -> 'SafetyValidator':
        """Create strict safety validator preset"""
        return cls(
            safety_level='strict',
            blocked_modules=['os', 'subprocess', 'sys', 'shutil', 'glob'],
            blocked_functions=['exec', 'eval', 'open', 'input', 'raw_input'],
            blocked_keywords=['import os', 'import subprocess', 'import sys'],
            max_code_length=5000
        )
    
    @classmethod
    def create_moderate_preset(cls) -> 'SafetyValidator':
        """Create moderate safety validator preset"""
        return cls(
            safety_level='moderate',
            blocked_modules=['os', 'subprocess', 'sys'],
            blocked_functions=['exec', 'eval'],
            blocked_keywords=['import os', 'import subprocess'],
            max_code_length=10000
        )
    
    @classmethod
    def create_permissive_preset(cls) -> 'SafetyValidator':
        """Create permissive safety validator preset"""
        return cls(
            safety_level='permissive',
            blocked_modules=[],
            blocked_functions=['exec', 'eval'],
            blocked_keywords=[],
            max_code_length=50000
        )


class ResourceMonitor:
    """Monitors resource usage during execution"""
    
    def __init__(self, max_execution_time: float = 30.0, max_memory_mb: int = 512, 
                 max_cpu_percent: float = 80.0, max_output_length: int = 10000,
                 monitor_interval: float = 1.0):
        self.max_execution_time = max_execution_time
        self.max_memory_mb = max_memory_mb
        self.max_cpu_percent = max_cpu_percent
        self.max_output_length = max_output_length
        self.monitor_interval = monitor_interval
        
        # Runtime state
        self.start_time = None
        self.start_memory = None
        self.process = None
        self.monitoring = False
        self.resource_history = []
    
    def start_monitoring(self):
        """Start monitoring resources"""
        self.start_time = time.time()
        self.process = psutil.Process()
        self.start_memory = self.process.memory_info().rss / 1024 / 1024  # MB
        self.monitoring = True
        self.resource_history = []
    
    def get_current_usage(self) -> Dict[str, float]:
        """Get current resource usage"""
        if self.start_time is None:
            return {"execution_time": 0.0, "memory_usage_mb": 0.0, "cpu_percent": 0.0}
        
        current_time = time.time()
        execution_time = current_time - self.start_time
        
        try:
            current_memory = self.process.memory_info().rss / 1024 / 1024  # MB
            memory_usage = current_memory - self.start_memory
            cpu_percent = self.process.cpu_percent()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            memory_usage = 0.0
            cpu_percent = 0.0
        
        usage = {
            "execution_time": execution_time,
            "memory_usage_mb": max(0, memory_usage),
            "cpu_percent": cpu_percent
        }
        
        # Add to history
        if self.monitoring:
            self.resource_history.append({
                **usage,
                "timestamp": current_time
            })
        
        return usage
    
    def stop_monitoring(self) -> Dict[str, float]:
        """Stop monitoring and return final usage"""
        usage = self.get_current_usage()
        self.monitoring = False
        self.start_time = None
        self.start_memory = None
        self.process = None
        return usage
    
    def check_violations(self) -> List[Dict[str, Any]]:
        """Check for resource violations"""
        violations = []
        current_usage = self.get_current_usage()
        
        if current_usage["execution_time"] > self.max_execution_time:
            violations.append({
                'type': 'execution_time',
                'message': f"Execution time exceeded: {current_usage['execution_time']:.2f}s > {self.max_execution_time}s",
                'severity': 'high'
            })
        
        if current_usage["memory_usage_mb"] > self.max_memory_mb:
            violations.append({
                'type': 'memory_usage',
                'message': f"Memory usage exceeded: {current_usage['memory_usage_mb']:.1f}MB > {self.max_memory_mb}MB",
                'severity': 'high'
            })
        
        if current_usage["cpu_percent"] > self.max_cpu_percent:
            violations.append({
                'type': 'cpu_usage',
                'message': f"CPU usage exceeded: {current_usage['cpu_percent']:.1f}% > {self.max_cpu_percent}%",
                'severity': 'medium'
            })
        
        return violations
    
    def get_monitoring_report(self) -> Dict[str, Any]:
        """Get comprehensive monitoring report"""
        current_usage = self.get_current_usage()
        violations = self.check_violations()
        
        # Calculate statistics from history
        if self.resource_history:
            execution_times = [r['execution_time'] for r in self.resource_history]
            memory_usage = [r['memory_usage_mb'] for r in self.resource_history]
            cpu_usage = [r['cpu_percent'] for r in self.resource_history]
            
            stats = {
                'peak_memory_mb': max(memory_usage) if memory_usage else 0,
                'avg_memory_mb': sum(memory_usage) / len(memory_usage) if memory_usage else 0,
                'peak_cpu_percent': max(cpu_usage) if cpu_usage else 0,
                'avg_cpu_percent': sum(cpu_usage) / len(cpu_usage) if cpu_usage else 0,
                'total_execution_time': max(execution_times) if execution_times else 0
            }
        else:
            stats = {
                'peak_memory_mb': current_usage["memory_usage_mb"],
                'avg_memory_mb': current_usage["memory_usage_mb"],
                'peak_cpu_percent': current_usage["cpu_percent"],
                'avg_cpu_percent': current_usage["cpu_percent"],
                'total_execution_time': current_usage["execution_time"]
            }
        
        return {
            'current_usage': current_usage,
            'violations': violations,
            'statistics': stats,
            'limits': {
                'max_execution_time': self.max_execution_time,
                'max_memory_mb': self.max_memory_mb,
                'max_cpu_percent': self.max_cpu_percent,
                'max_output_length': self.max_output_length
            },
            'monitoring_active': self.monitoring,
            'history_length': len(self.resource_history)
        }
    
    def get_resource_history(self) -> List[Dict[str, Any]]:
        """Get resource usage history"""
        return self.resource_history.copy()
    
    def reset_monitoring(self):
        """Reset monitoring state"""
        self.start_time = None
        self.start_memory = None
        self.process = None
        self.monitoring = False
        self.resource_history = []
    
    def generate_usage_report(self, usage_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate usage report from usage data"""
        violations = []
        
        # Check for violations
        if usage_data.get('execution_time', 0) > self.max_execution_time:
            violations.append({
                'type': 'execution_time',
                'message': f"Execution time exceeded: {usage_data['execution_time']:.2f}s > {self.max_execution_time}s"
            })
        
        if usage_data.get('memory_mb', 0) > self.max_memory_mb:
            violations.append({
                'type': 'memory_usage',
                'message': f"Memory usage exceeded: {usage_data['memory_mb']:.1f}MB > {self.max_memory_mb}MB"
            })
        
        if usage_data.get('cpu_percent', 0) > self.max_cpu_percent:
            violations.append({
                'type': 'cpu_usage',
                'message': f"CPU usage exceeded: {usage_data['cpu_percent']:.1f}% > {self.max_cpu_percent}%"
            })
        
        if usage_data.get('output_length', 0) > self.max_output_length:
            violations.append({
                'type': 'output_length',
                'message': f"Output length exceeded: {usage_data['output_length']} > {self.max_output_length}"
            })
        
        # Calculate efficiency score
        efficiency = self.calculate_efficiency_score(usage_data)
        
        return {
            'summary': {
                'execution_time': usage_data.get('execution_time', 0),
                'memory_mb': usage_data.get('memory_mb', 0),
                'cpu_percent': usage_data.get('cpu_percent', 0),
                'output_length': usage_data.get('output_length', 0),
                'violation_count': len(violations)
            },
            'details': usage_data,
            'violations': violations,
            'efficiency_score': efficiency,
            'limits': {
                'max_execution_time': self.max_execution_time,
                'max_memory_mb': self.max_memory_mb,
                'max_cpu_percent': self.max_cpu_percent,
                'max_output_length': self.max_output_length
            }
        }
    
    def calculate_efficiency_score(self, usage_data: Dict[str, Any]) -> float:
        """Calculate efficiency score based on resource usage"""
        # Score components (lower usage = higher score)
        time_score = max(0.0, 1.0 - (usage_data.get('execution_time', 0) / self.max_execution_time))
        memory_score = max(0.0, 1.0 - (usage_data.get('memory_mb', 0) / self.max_memory_mb))
        cpu_score = max(0.0, 1.0 - (usage_data.get('cpu_percent', 0) / self.max_cpu_percent))
        output_score = max(0.0, 1.0 - (usage_data.get('output_length', 0) / self.max_output_length))
        
        # Weighted average
        return (time_score * 0.3 + memory_score * 0.3 + cpu_score * 0.2 + output_score * 0.2)
    
    def monitor_execution(self, execution_func: Callable, *args, **kwargs) -> Dict[str, Any]:
        """Monitor execution of a function"""
        self.start_monitoring()
        
        try:
            result = execution_func(*args, **kwargs)
            usage = self.stop_monitoring()
            violations = self.check_violations()
            
            return {
                'result': result,
                'usage': usage,
                'violations': violations,
                'success': True
            }
        except Exception as e:
            usage = self.stop_monitoring()
            violations = self.check_violations()
            
            return {
                'result': None,
                'usage': usage,
                'violations': violations,
                'success': False,
                'error': str(e)
            }


class PromptSandbox:
    """Main prompt testing sandbox component"""
    
    def __init__(self, storage_path: Path = None):
        self.storage_path = storage_path or Path("data/prompt_sandbox")
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        # Initialize default environments
        self.environments = self._load_environments()
        if not self.environments:
            self._create_default_environments()
        
        # Initialize components
        self.safety_validator = SafetyValidator()
        self.resource_monitor = ResourceMonitor()
        
        # Test storage
        self.tests = self._load_tests()
        self.results = self._load_results()
        
        # Additional attributes expected by tests
        self.active_tests = {}
        self.execution_history = []
    
    def _load_environments(self) -> Dict[str, SandboxEnvironment]:
        """Load environments from storage"""
        env_file = self.storage_path / "environments.json"
        if env_file.exists():
            try:
                with open(env_file, 'r') as f:
                    data = json.load(f)
                return {k: SandboxEnvironment.from_dict(v) for k, v in data.items()}
            except Exception as e:
                st.error(f"Error loading environments: {e}")
        return {}
    
    def _save_environments(self):
        """Save environments to storage"""
        env_file = self.storage_path / "environments.json"
        try:
            with open(env_file, 'w') as f:
                data = {k: v.to_dict() for k, v in self.environments.items()}
                json.dump(data, f, indent=2)
        except Exception as e:
            st.error(f"Error saving environments: {e}")
    
    def _create_default_environments(self):
        """Create default sandbox environments"""
        defaults = [
            SandboxEnvironment(
                environment_id="development",
                name="Development",
                max_execution_time=30.0,
                max_memory_mb=256,
                safety_level="moderate",
                description="General development environment with moderate safety"
            ),
            SandboxEnvironment(
                environment_id="production",
                name="Production",
                max_execution_time=10.0,
                max_memory_mb=128,
                safety_level="strict",
                description="Production environment with strict safety controls"
            ),
            SandboxEnvironment(
                environment_id="research",
                name="Research",
                max_execution_time=60.0,
                max_memory_mb=1024,
                safety_level="permissive",
                description="Research environment with extended resources"
            )
        ]
        
        for env in defaults:
            self.environments[env.environment_id] = env
        
        self._save_environments()
    
    def _load_tests(self) -> Dict[str, PromptTest]:
        """Load tests from storage"""
        tests_file = self.storage_path / "tests.json"
        if tests_file.exists():
            try:
                with open(tests_file, 'r') as f:
                    data = json.load(f)
                return {k: PromptTest.from_dict(v) for k, v in data.items()}
            except Exception as e:
                st.error(f"Error loading tests: {e}")
        return {}
    
    def _save_tests(self):
        """Save tests to storage"""
        tests_file = self.storage_path / "tests.json"
        try:
            with open(tests_file, 'w') as f:
                data = {k: v.to_dict() for k, v in self.tests.items()}
                json.dump(data, f, indent=2)
        except Exception as e:
            st.error(f"Error saving tests: {e}")
    
    def _load_results(self) -> List[ExecutionResult]:
        """Load results from storage"""
        results_file = self.storage_path / "results.json"
        if results_file.exists():
            try:
                with open(results_file, 'r') as f:
                    data = json.load(f)
                return [ExecutionResult.from_dict(item) for item in data]
            except Exception as e:
                st.error(f"Error loading results: {e}")
        return []
    
    def _save_results(self):
        """Save results to storage"""
        results_file = self.storage_path / "results.json"
        try:
            with open(results_file, 'w') as f:
                data = [result.to_dict() for result in self.results]
                json.dump(data, f, indent=2)
        except Exception as e:
            st.error(f"Error saving results: {e}")
    
    def execute_prompt(self, test: PromptTest, environment: SandboxEnvironment) -> ExecutionResult:
        """Execute a prompt test in the specified environment"""
        import uuid
        
        # Generate result ID
        result_id = str(uuid.uuid4())
        
        # Validate safety first
        self.safety_validator.safety_level = environment.safety_level
        safety_result = self.safety_validator.validate_prompt(test.prompt_content)
        
        if not safety_result['is_safe']:
            return ExecutionResult(
                result_id=result_id,
                test_id=test.test_id,
                environment_id=environment.environment_id,
                output="",
                error_message=f"Safety validation failed: {'; '.join([v['message'] for v in safety_result['violations']])}",
                safety_violations=[v['message'] for v in safety_result['violations']],
                success=False
            )
        
        # Start monitoring
        self.resource_monitor.start_monitoring()
        
        try:
            # Simulate prompt execution (in a real implementation, this would execute the prompt)
            output = self._simulate_prompt_execution(test.prompt_content, environment)
            
            # Get resource usage
            usage = self.resource_monitor.stop_monitoring()
            
            # Check for resource violations
            resource_violations = self.resource_monitor.check_violations()
            
            # Check success criteria
            success = self._check_success_criteria(output, test.success_criteria)
            
            return ExecutionResult(
                result_id=result_id,
                test_id=test.test_id,
                environment_id=environment.environment_id,
                output=output,
                execution_time=usage["execution_time"],
                memory_used_mb=usage["memory_usage_mb"],
                resource_violations=[v['message'] for v in resource_violations],
                success=success
            )
            
        except Exception as e:
            usage = self.resource_monitor.stop_monitoring()
            return ExecutionResult(
                result_id=result_id,
                test_id=test.test_id,
                environment_id=environment.environment_id,
                output="",
                error_message=str(e),
                execution_time=usage["execution_time"],
                memory_used_mb=usage["memory_usage_mb"],
                success=False
            )
    
    def _simulate_prompt_execution(self, prompt: str, environment: SandboxEnvironment) -> str:
        """Simulate prompt execution (placeholder for real implementation)"""
        # This is a simulation - in a real implementation, this would execute the prompt
        # in a sandboxed environment
        import time
        time.sleep(0.1)  # Simulate execution time
        
        # Simulate memory usage by creating temporary data
        temp_data = ['x' * 1000 for _ in range(100)]  # Simulate memory usage
        
        if "error" in prompt.lower():
            raise Exception("Simulated execution error")
        
        # Clean up temp data
        del temp_data
        
        return f"Executed prompt in {environment.name} environment: {prompt[:100]}..."
    
    def _check_success_criteria(self, output: str, criteria: List[str]) -> bool:
        """Check if output meets success criteria"""
        if not criteria:
            return True
        
        for criterion in criteria:
            if criterion.lower() not in output.lower():
                return False
        
        return True
    
    def create_environment(self, env_config: Dict[str, Any]) -> str:
        """Create a new sandbox environment"""
        import uuid
        env_id = str(uuid.uuid4())
        
        # Create environment with generated ID
        env_config['environment_id'] = env_id
        
        # Create SandboxEnvironment object
        environment = SandboxEnvironment(**env_config)
        
        # Add to environments
        self.environments[env_id] = environment
        
        # Save to storage
        self._save_environments()
        
        return env_id
    
    def create_test(self, test_config: Dict[str, Any]) -> str:
        """Create a new prompt test"""
        import uuid
        test_id = str(uuid.uuid4())
        
        # Create test with generated ID
        test_config['test_id'] = test_id
        
        # Create PromptTest object
        test = PromptTest(**test_config)
        
        # Add to tests
        self.tests[test_id] = test
        self.active_tests[test_id] = test
        
        # Save to storage
        self._save_tests()
        
        return test_id
    
    def execute_single_prompt(self, prompt: str, environment_id: str = "development") -> ExecutionResult:
        """Execute a single prompt in the specified environment"""
        import uuid
        
        # Create temporary test
        test = PromptTest(
            test_id=f"single_{uuid.uuid4()}",
            name="Single Prompt Execution",
            prompt_content=prompt,
            environment_id=environment_id
        )
        
        # Get environment
        if environment_id not in self.environments:
            raise ValueError(f"Environment '{environment_id}' not found")
        
        environment = self.environments[environment_id]
        
        # Execute the test
        return self.execute_prompt(test, environment)
    
    def render_sandbox_interface(self) -> None:
        """Render the sandbox interface (alias for render method)"""
        self.render()
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get sandbox statistics"""
        total_tests = len(self.tests)
        total_results = len(self.results)
        successful_results = sum(1 for r in self.results if r.success)
        failed_results = total_results - successful_results
        
        # Calculate averages
        if total_results > 0:
            avg_execution_time = sum(r.execution_time for r in self.results) / total_results
            avg_memory_usage = sum(r.memory_used_mb for r in self.results) / total_results
        else:
            avg_execution_time = 0.0
            avg_memory_usage = 0.0
        
        # Count violations
        safety_violations = sum(len(r.safety_violations) for r in self.results)
        resource_violations = sum(len(r.resource_violations) for r in self.results)
        
        return {
            'total_environments': len(self.environments),
            'total_tests': total_tests,
            'total_executions': total_results,
            'successful_executions': successful_results,
            'failed_executions': failed_results,
            'success_rate': successful_results / total_results if total_results > 0 else 0.0,
            'average_execution_time': avg_execution_time,
            'average_memory_usage': avg_memory_usage,
            'safety_violations_count': safety_violations,
            'resource_violations_count': resource_violations,
            'active_tests': len(self.active_tests),
            'execution_history_length': len(self.execution_history)
        }
    
    def execute_test(self, test_id: str, environment_id: str = None) -> ExecutionResult:
        """Execute a test by ID"""
        if test_id not in self.tests:
            raise ValueError(f"Test '{test_id}' not found")
        
        test = self.tests[test_id]
        env_id = environment_id or test.environment_id
        
        if env_id not in self.environments:
            raise ValueError(f"Environment '{env_id}' not found")
        
        environment = self.environments[env_id]
        result = self.execute_prompt(test, environment)
        
        # Add to execution history
        self.execution_history.append(result)
        
        return result
    
    def get_execution_history(self) -> List[ExecutionResult]:
        """Get execution history"""
        return self.execution_history.copy()
    
    def render(self):
        """Render the prompt testing sandbox interface"""
        st.header("🧪 Prompt Testing Sandbox")
        
        # Main tabs
        tab1, tab2, tab3, tab4 = st.tabs(["🏃 Run Tests", "⚙️ Environments", "📝 Test Management", "📊 Results"])
        
        with tab1:
            self._render_test_execution()
        
        with tab2:
            self._render_environment_management()
        
        with tab3:
            self._render_test_management()
        
        with tab4:
            self._render_results_view()
    
    def _render_test_execution(self):
        """Render test execution interface"""
        st.subheader("Execute Prompt Tests")
        
        # Quick test section
        st.markdown("### Quick Test")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            prompt = st.text_area("Enter prompt to test:", height=150)
            success_criteria = st.text_input("Success criteria (comma-separated):")
        
        with col2:
            env_options = list(self.environments.keys())
            selected_env = st.selectbox("Environment:", env_options)
            
            if st.button("🚀 Execute Test", type="primary"):
                if prompt and selected_env:
                    # Create temporary test
                    test = PromptTest(
                        test_id=f"quick_test_{int(time.time())}",
                        name="Quick Test",
                        prompt=prompt,
                        success_criteria=[c.strip() for c in success_criteria.split(",") if c.strip()]
                    )
                    
                    # Execute test
                    with st.spinner("Executing test..."):
                        result = self.execute_prompt(test, self.environments[selected_env])
                        self.results.append(result)
                        self._save_results()
                    
                    # Display result
                    self._display_execution_result(result)
        
        # Batch test section
        st.markdown("### Batch Test Execution")
        if self.tests:
            selected_tests = st.multiselect(
                "Select tests to run:",
                options=list(self.tests.keys()),
                format_func=lambda x: self.tests[x].name
            )
            
            if selected_tests:
                batch_env = st.selectbox("Environment for batch:", env_options, key="batch_env")
                
                if st.button("🔄 Run Batch Tests"):
                    progress_bar = st.progress(0)
                    results_container = st.empty()
                    
                    batch_results = []
                    for i, test_id in enumerate(selected_tests):
                        test = self.tests[test_id]
                        result = self.execute_prompt(test, self.environments[batch_env])
                        batch_results.append(result)
                        self.results.append(result)
                        
                        progress_bar.progress((i + 1) / len(selected_tests))
                    
                    self._save_results()
                    
                    # Display batch results
                    with results_container.container():
                        st.success(f"Executed {len(batch_results)} tests")
                        for result in batch_results:
                            self._display_execution_result(result)
        else:
            st.info("No tests available. Create tests in the Test Management tab.")
    
    def _render_environment_management(self):
        """Render environment management interface"""
        st.subheader("Sandbox Environments")
        
        # Environment list
        for env_id, env in self.environments.items():
            with st.expander(f"🏗️ {env.name} ({env_id})"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Description:** {env.description}")
                    st.write(f"**Safety Level:** {env.safety_level}")
                    st.write(f"**Max Execution Time:** {env.max_execution_time}s")
                    st.write(f"**Max Memory:** {env.max_memory_mb}MB")
                
                with col2:
                    st.write("**Allowed Modules:**")
                    for module in env.allowed_modules:
                        st.write(f"  • {module}")
                    
                    if st.button(f"🗑️ Delete {env.name}", key=f"delete_{env_id}"):
                        del self.environments[env_id]
                        self._save_environments()
                        st.experimental_rerun()
        
        # Add new environment
        st.markdown("### Add New Environment")
        with st.form("new_environment"):
            col1, col2 = st.columns(2)
            
            with col1:
                new_env_id = st.text_input("Environment ID:")
                new_env_name = st.text_input("Environment Name:")
                new_env_desc = st.text_area("Description:")
            
            with col2:
                new_safety_level = st.selectbox("Safety Level:", ["strict", "moderate", "permissive"])
                new_max_time = st.number_input("Max Execution Time (s):", min_value=1.0, value=30.0)
                new_max_memory = st.number_input("Max Memory (MB):", min_value=64, value=256)
            
            if st.form_submit_button("➕ Add Environment"):
                if new_env_id and new_env_name:
                    new_env = SandboxEnvironment(
                        environment_id=new_env_id,
                        name=new_env_name,
                        description=new_env_desc,
                        safety_level=new_safety_level,
                        max_execution_time=new_max_time,
                        max_memory_mb=new_max_memory
                    )
                    
                    is_valid, message = new_env.validate()
                    if is_valid:
                        self.environments[new_env_id] = new_env
                        self._save_environments()
                        st.success(f"Environment '{new_env_name}' added successfully!")
                        st.experimental_rerun()
                    else:
                        st.error(f"Invalid environment: {message}")
    
    def _render_test_management(self):
        """Render test management interface"""
        st.subheader("Test Management")
        
        # Existing tests
        if self.tests:
            st.markdown("### Existing Tests")
            for test_id, test in self.tests.items():
                with st.expander(f"📝 {test.name}"):
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.write(f"**Prompt:** {test.prompt[:200]}...")
                        st.write(f"**Success Criteria:** {', '.join(test.success_criteria)}")
                        st.write(f"**Timeout:** {test.timeout}s")
                    
                    with col2:
                        if st.button(f"🗑️ Delete", key=f"delete_test_{test_id}"):
                            del self.tests[test_id]
                            self._save_tests()
                            st.experimental_rerun()
        
        # Add new test
        st.markdown("### Add New Test")
        with st.form("new_test"):
            test_name = st.text_input("Test Name:")
            test_prompt = st.text_area("Prompt:", height=150)
            test_criteria = st.text_input("Success Criteria (comma-separated):")
            test_timeout = st.number_input("Timeout (s):", min_value=1.0, value=30.0)
            
            if st.form_submit_button("➕ Add Test"):
                if test_name and test_prompt:
                    test_id = f"test_{int(time.time())}"
                    new_test = PromptTest(
                        test_id=test_id,
                        name=test_name,
                        prompt=test_prompt,
                        success_criteria=[c.strip() for c in test_criteria.split(",") if c.strip()],
                        timeout=test_timeout
                    )
                    
                    self.tests[test_id] = new_test
                    self._save_tests()
                    st.success(f"Test '{test_name}' added successfully!")
                    st.experimental_rerun()
    
    def _render_results_view(self):
        """Render results view interface"""
        st.subheader("Execution Results")
        
        if not self.results:
            st.info("No execution results available. Run some tests first!")
            return
        
        # Filter options
        col1, col2, col3 = st.columns(3)
        
        with col1:
            env_filter = st.selectbox("Filter by Environment:", 
                                    ["All"] + list(self.environments.keys()))
        
        with col2:
            success_filter = st.selectbox("Filter by Success:", 
                                        ["All", "Success", "Failed"])
        
        with col3:
            limit = st.number_input("Show last N results:", min_value=10, value=50)
        
        # Filter results
        filtered_results = self.results[-limit:]
        
        if env_filter != "All":
            filtered_results = [r for r in filtered_results if r.environment_id == env_filter]
        
        if success_filter != "All":
            success_value = success_filter == "Success"
            filtered_results = [r for r in filtered_results if r.success == success_value]
        
        # Display results
        st.markdown(f"### Results ({len(filtered_results)} shown)")
        
        for result in reversed(filtered_results):
            self._display_execution_result(result)
    
    def _display_execution_result(self, result: ExecutionResult):
        """Display an execution result"""
        status_color = "🟢" if result.success else "🔴"
        
        with st.expander(f"{status_color} {result.test_id} - {result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Environment:** {result.environment_id}")
                st.write(f"**Success:** {'✅ Yes' if result.success else '❌ No'}")
                st.write(f"**Execution Time:** {result.execution_time:.2f}s")
                st.write(f"**Memory Usage:** {result.memory_usage_mb:.1f}MB")
            
            with col2:
                if result.error:
                    st.error(f"**Error:** {result.error}")
                else:
                    st.success("**Status:** Completed successfully")
            
            if result.output:
                st.text_area("Output:", result.output, height=100, key=f"output_{result.test_id}_{result.timestamp}")


# Global convenience functions
def execute_prompt_safely(prompt: str, environment_id: str = "development") -> ExecutionResult:
    """Execute a prompt safely in the specified environment"""
    sandbox = PromptSandbox()
    
    if environment_id not in sandbox.environments:
        raise ValueError(f"Environment '{environment_id}' not found")
    
    test = PromptTest(
        test_id=f"safe_exec_{int(time.time())}",
        name="Safe Execution",
        prompt=prompt
    )
    
    return sandbox.execute_prompt(test, sandbox.environments[environment_id])


def validate_prompt_safety(prompt: str, safety_level: str = "moderate") -> Dict[str, Any]:
    """Validate prompt safety"""
    validator = SafetyValidator(safety_level=safety_level)
    result = validator.validate_prompt(prompt)
    
    # Add risk level based on violations
    if not result['is_safe']:
        if any(v['severity'] == 'high' for v in result['violations']):
            risk_level = 'high'
        elif any(v['severity'] == 'medium' for v in result['violations']):
            risk_level = 'medium'
        else:
            risk_level = 'low'
    else:
        risk_level = 'none'
    
    result['risk_level'] = risk_level
    return result


def get_execution_limits(environment_id: str = "development") -> Dict[str, Any]:
    """Get execution limits for an environment"""
    sandbox = PromptSandbox()
    
    if environment_id not in sandbox.environments:
        raise ValueError(f"Environment '{environment_id}' not found")
    
    env = sandbox.environments[environment_id]
    return {
        "max_execution_time": env.max_execution_time,
        "max_memory_mb": env.max_memory_mb,
        "max_cpu_percent": 80.0,  # Default from ResourceMonitor
        "max_output_length": env.max_output_length,
        "safety_level": env.safety_level
    }