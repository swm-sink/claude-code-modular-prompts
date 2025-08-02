# Circuit Breaker Pattern

**Purpose**: Advanced circuit breaker for LLM error handling with intelligent failure detection, automatic service isolation, and gradual recovery mechanisms.

**Usage**: 
- Implement three-state pattern (closed, open, half-open) for system reliability
- Monitor error rates and response times to detect system degradation
- Fail fast during outages to prevent cascading failures
- Provide fallback strategies with cached results or safe defaults
- Enable gradual recovery with automatic state transitions

**Compatibility**: 
- **Works with**: error-handler, chaos-engineering, performance monitoring, fallback systems
- **Requires**: Service endpoints requiring reliability protection
- **Conflicts**: None (universal reliability pattern)

**Implementation**:
```python
# Circuit breaker implementation
class CircuitBreaker:
    def __init__(self, failure_threshold=5, recovery_timeout=60, success_threshold=3):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.success_threshold = success_threshold
        
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
        
    def call(self, operation, *args, **kwargs):
        if self.state == "OPEN":
            if self.should_attempt_reset():
                self.state = "HALF_OPEN"
            else:
                return self.fallback_response()
        
        try:
            # Execute the operation
            result = operation(*args, **kwargs)
            self.on_success()
            return result
            
        except Exception as e:
            self.on_failure()
            if self.state == "OPEN":
                return self.fallback_response()
            else:
                raise e
    
    def on_success(self):
        self.failure_count = 0
        
        if self.state == "HALF_OPEN":
            self.success_count += 1
            if self.success_count >= self.success_threshold:
                self.state = "CLOSED"
                self.success_count = 0
    
    def on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"
            
        if self.state == "HALF_OPEN":
            self.state = "OPEN"
            self.success_count = 0
    
    def should_attempt_reset(self):
        return (time.time() - self.last_failure_time) >= self.recovery_timeout
    
    def fallback_response(self):
        # Return cached result or safe default
        return {
            "success": False,
            "message": "Service temporarily unavailable",
            "fallback": True,
            "retry_after": self.recovery_timeout
        }

# Usage wrapper for LLM operations
def protected_llm_operation(operation_name, circuit_breaker):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return circuit_breaker.call(func, *args, **kwargs)
            except Exception as e:
                # Log failure and return graceful degradation
                log_circuit_breaker_failure(operation_name, str(e))
                return circuit_breaker.fallback_response()
        return wrapper
    return decorator

# Example usage
@protected_llm_operation("code_analysis", circuit_breaker)
def analyze_code_with_llm(code_content):
    # LLM operation that might fail
    response = llm_client.analyze(code_content)
    if response.error_rate > 0.5:
        raise Exception("High error rate detected")
    return response

# Circuit breaker monitoring
def get_circuit_breaker_metrics(breaker):
    return {
        "state": breaker.state,
        "failure_count": breaker.failure_count,
        "success_count": breaker.success_count,
        "uptime_percentage": calculate_uptime(breaker),
        "last_failure": breaker.last_failure_time
    }
```

**Category**: reliability | **Complexity**: moderate | **Time**: 3 hours