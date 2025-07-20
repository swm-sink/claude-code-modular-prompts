# Package Usage Patterns (I20)

| version | last_updated | status | agent |
|---------|--------------|---------|-------|
| 1.0.0   | 2025-07-20   | active | I20 |

## Purpose
Comprehensive package usage pattern system that provides language-specific templates, common usage examples, best practice patterns, and anti-pattern detection to ensure optimal and secure package integration in generated code.

## Core Usage Pattern Framework

### Language-Specific Package Patterns

```python
class LanguagePackagePatterns:
    def __init__(self):
        self.patterns = {
            "python": PythonPatterns(),
            "javascript": JavaScriptPatterns(),
            "typescript": TypeScriptPatterns(),
            "go": GoPatterns(),
            "rust": RustPatterns(),
            "java": JavaPatterns(),
            "php": PHPPatterns(),
            "ruby": RubyPatterns(),
            "c_sharp": CSharpPatterns()
        }
        
        self.pattern_categories = {
            "initialization": "Package setup and configuration",
            "basic_usage": "Common operations and methods",
            "error_handling": "Proper error handling patterns",
            "async_patterns": "Asynchronous operation patterns",
            "testing": "Testing and mocking patterns",
            "configuration": "Configuration and environment setup",
            "security": "Security best practices",
            "performance": "Performance optimization patterns"
        }
    
    def get_usage_pattern(self, package_name: str, language: str, 
                         pattern_type: str) -> UsagePattern:
        """Get specific usage pattern for package and language"""
        if language not in self.patterns:
            raise UnsupportedLanguageError(f"Language {language} not supported")
        
        language_patterns = self.patterns[language]
        return language_patterns.get_pattern(package_name, pattern_type)

class PythonPatterns:
    def __init__(self):
        self.package_patterns = {
            "requests": {
                "initialization": self._requests_init_patterns(),
                "basic_usage": self._requests_basic_patterns(),
                "error_handling": self._requests_error_patterns(),
                "async_patterns": self._requests_async_patterns(),
                "testing": self._requests_testing_patterns(),
                "security": self._requests_security_patterns()
            },
            "pandas": {
                "initialization": self._pandas_init_patterns(),
                "basic_usage": self._pandas_basic_patterns(),
                "error_handling": self._pandas_error_patterns(),
                "performance": self._pandas_performance_patterns(),
                "testing": self._pandas_testing_patterns()
            },
            "flask": {
                "initialization": self._flask_init_patterns(),
                "basic_usage": self._flask_basic_patterns(),
                "error_handling": self._flask_error_patterns(),
                "security": self._flask_security_patterns(),
                "testing": self._flask_testing_patterns(),
                "configuration": self._flask_config_patterns()
            },
            "django": {
                "initialization": self._django_init_patterns(),
                "basic_usage": self._django_basic_patterns(),
                "error_handling": self._django_error_patterns(),
                "security": self._django_security_patterns(),
                "testing": self._django_testing_patterns(),
                "configuration": self._django_config_patterns()
            }
        }
    
    def _requests_init_patterns(self) -> List[PatternTemplate]:
        return [
            PatternTemplate(
                name="basic_session_setup",
                description="Initialize requests session with proper configuration",
                code="""
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Create session with retry strategy
session = requests.Session()
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

# Set default headers
session.headers.update({
    'User-Agent': 'MyApp/1.0',
    'Accept': 'application/json'
})
""",
                best_practices=[
                    "Always use sessions for multiple requests",
                    "Configure appropriate retry strategies",
                    "Set meaningful User-Agent headers",
                    "Use connection pooling for performance"
                ],
                security_notes=[
                    "Never hardcode API keys in headers",
                    "Use environment variables for secrets",
                    "Validate SSL certificates in production"
                ]
            ),
            PatternTemplate(
                name="secure_session_setup",
                description="Initialize requests session with security best practices",
                code="""
import requests
import os
from requests.auth import HTTPBasicAuth

# Secure session configuration
session = requests.Session()

# SSL/TLS configuration
session.verify = True  # Always verify SSL certificates
session.cert = None    # Client certificate if needed

# Authentication setup
if os.getenv('API_USERNAME') and os.getenv('API_PASSWORD'):
    session.auth = HTTPBasicAuth(
        os.getenv('API_USERNAME'),
        os.getenv('API_PASSWORD')
    )

# Security headers
session.headers.update({
    'User-Agent': os.getenv('USER_AGENT', 'SecureApp/1.0'),
    'Accept': 'application/json',
    'Content-Type': 'application/json'
})

# Timeout configuration
session.timeout = (5, 30)  # (connect_timeout, read_timeout)
""",
                security_notes=[
                    "Always verify SSL certificates",
                    "Use environment variables for credentials",
                    "Set appropriate timeouts",
                    "Implement proper error handling"
                ]
            )
        ]
    
    def _requests_basic_patterns(self) -> List[PatternTemplate]:
        return [
            PatternTemplate(
                name="get_request_with_error_handling",
                description="Perform GET request with comprehensive error handling",
                code="""
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

def make_safe_get_request(url: str, **kwargs) -> dict:
    \"\"\"Make GET request with proper error handling\"\"\"
    try:
        response = session.get(url, timeout=30, **kwargs)
        response.raise_for_status()  # Raises HTTPError for bad responses
        
        # Validate content type
        content_type = response.headers.get('content-type', '')
        if 'application/json' not in content_type:
            raise ValueError(f"Expected JSON response, got {content_type}")
        
        return response.json()
        
    except Timeout:
        logger.error(f"Request to {url} timed out")
        raise
    except ConnectionError:
        logger.error(f"Failed to connect to {url}")
        raise
    except requests.HTTPError as e:
        logger.error(f"HTTP error {e.response.status_code}: {e.response.text}")
        raise
    except ValueError as e:
        logger.error(f"Invalid response format: {e}")
        raise
    except RequestException as e:
        logger.error(f"Request failed: {e}")
        raise
""",
                best_practices=[
                    "Always use timeouts",
                    "Check response status codes",
                    "Validate response content type",
                    "Implement comprehensive error handling",
                    "Log errors for debugging"
                ]
            )
        ]
    
    def _requests_security_patterns(self) -> List[PatternTemplate]:
        return [
            PatternTemplate(
                name="secure_api_request",
                description="Secure API request with authentication and validation",
                code="""
import requests
import os
import hashlib
import hmac
from typing import Dict, Any

class SecureAPIClient:
    def __init__(self):
        self.base_url = os.getenv('API_BASE_URL')
        self.api_key = os.getenv('API_KEY')
        self.api_secret = os.getenv('API_SECRET')
        
        if not all([self.base_url, self.api_key, self.api_secret]):
            raise ValueError("Missing required environment variables")
        
        self.session = requests.Session()
        self.session.timeout = (5, 30)
        self.session.verify = True
    
    def _generate_signature(self, method: str, path: str, body: str = "") -> str:
        \"\"\"Generate HMAC signature for request authentication\"\"\"
        message = f"{method.upper()}{path}{body}"
        return hmac.new(
            self.api_secret.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
    
    def make_authenticated_request(self, method: str, endpoint: str, 
                                 data: Dict[Any, Any] = None) -> dict:
        \"\"\"Make authenticated request with signature\"\"\"
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        path = f"/{endpoint.lstrip('/')}"
        
        # Prepare request body
        body = ""
        if data:
            body = json.dumps(data, sort_keys=True)
        
        # Generate signature
        signature = self._generate_signature(method, path, body)
        
        # Set headers
        headers = {
            'X-API-Key': self.api_key,
            'X-Signature': signature,
            'Content-Type': 'application/json',
            'User-Agent': 'SecureClient/1.0'
        }
        
        # Make request
        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            data=body if body else None
        )
        
        response.raise_for_status()
        return response.json()
""",
                security_notes=[
                    "Never log or expose API secrets",
                    "Use HMAC signatures for request authentication",
                    "Validate all environment variables on startup",
                    "Implement rate limiting on client side"
                ]
            )
        ]

class JavaScriptPatterns:
    def __init__(self):
        self.package_patterns = {
            "axios": {
                "initialization": self._axios_init_patterns(),
                "basic_usage": self._axios_basic_patterns(),
                "error_handling": self._axios_error_patterns(),
                "async_patterns": self._axios_async_patterns(),
                "testing": self._axios_testing_patterns()
            },
            "react": {
                "initialization": self._react_init_patterns(),
                "basic_usage": self._react_basic_patterns(),
                "error_handling": self._react_error_patterns(),
                "testing": self._react_testing_patterns(),
                "performance": self._react_performance_patterns()
            },
            "express": {
                "initialization": self._express_init_patterns(),
                "basic_usage": self._express_basic_patterns(),
                "error_handling": self._express_error_patterns(),
                "security": self._express_security_patterns(),
                "testing": self._express_testing_patterns()
            }
        }
    
    def _axios_init_patterns(self) -> List[PatternTemplate]:
        return [
            PatternTemplate(
                name="axios_instance_setup",
                description="Create configured axios instance with interceptors",
                code="""
import axios from 'axios';

// Create axios instance with base configuration
const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:3000/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
});

// Request interceptor for authentication
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized access
      localStorage.removeItem('authToken');
      window.location.href = '/login';
    }
    
    // Log error for debugging
    console.error('API Error:', {
      url: error.config?.url,
      method: error.config?.method,
      status: error.response?.status,
      data: error.response?.data
    });
    
    return Promise.reject(error);
  }
);

export default apiClient;
""",
                best_practices=[
                    "Use axios instances for consistent configuration",
                    "Implement request/response interceptors",
                    "Set appropriate timeouts",
                    "Handle authentication tokens securely",
                    "Implement comprehensive error handling"
                ]
            )
        ]
    
    def _react_init_patterns(self) -> List[PatternTemplate]:
        return [
            PatternTemplate(
                name="react_component_with_hooks",
                description="Modern React component with hooks and error handling",
                code="""
import React, { useState, useEffect, useCallback, useMemo } from 'react';
import PropTypes from 'prop-types';

const UserProfile = ({ userId, onUserUpdate }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Memoized API call
  const fetchUser = useCallback(async (id) => {
    try {
      setLoading(true);
      setError(null);
      
      const response = await apiClient.get(`/users/${id}`);
      setUser(response.data);
    } catch (err) {
      setError(err.message || 'Failed to fetch user');
      console.error('User fetch error:', err);
    } finally {
      setLoading(false);
    }
  }, []);

  // Effect for initial data loading
  useEffect(() => {
    if (userId) {
      fetchUser(userId);
    }
  }, [userId, fetchUser]);

  // Memoized computed values
  const userDisplayName = useMemo(() => {
    if (!user) return '';
    return `${user.firstName} ${user.lastName}`.trim();
  }, [user]);

  // Event handlers
  const handleRefresh = useCallback(() => {
    fetchUser(userId);
  }, [userId, fetchUser]);

  // Error boundary fallback
  if (error) {
    return (
      <div className="error-container">
        <p>Error: {error}</p>
        <button onClick={handleRefresh}>Retry</button>
      </div>
    );
  }

  // Loading state
  if (loading) {
    return <div className="loading">Loading user profile...</div>;
  }

  // Main render
  return (
    <div className="user-profile">
      <h2>{userDisplayName}</h2>
      <p>Email: {user?.email}</p>
      <button onClick={handleRefresh}>Refresh</button>
    </div>
  );
};

UserProfile.propTypes = {
  userId: PropTypes.string.isRequired,
  onUserUpdate: PropTypes.func
};

UserProfile.defaultProps = {
  onUserUpdate: () => {}
};

export default UserProfile;
""",
                best_practices=[
                    "Use functional components with hooks",
                    "Implement proper prop validation",
                    "Handle loading and error states",
                    "Use useCallback and useMemo for optimization",
                    "Implement proper cleanup in useEffect"
                ]
            )
        ]
```

### Common Usage Examples

```python
class UsageExampleGenerator:
    def __init__(self):
        self.example_categories = {
            "quickstart": "Getting started examples",
            "common_tasks": "Frequently used operations",
            "advanced_usage": "Complex scenarios and patterns",
            "integration": "Integration with other packages",
            "troubleshooting": "Common issues and solutions"
        }
    
    def generate_usage_examples(self, package_name: str, language: str) -> List[UsageExample]:
        """Generate comprehensive usage examples for package"""
        examples = []
        
        # Get base patterns
        patterns = self.pattern_engine.get_package_patterns(package_name, language)
        
        for category in self.example_categories:
            category_examples = self._generate_category_examples(
                package_name, language, category, patterns
            )
            examples.extend(category_examples)
        
        return examples
    
    def _generate_category_examples(self, package_name: str, language: str, 
                                  category: str, patterns: List[PatternTemplate]) -> List[UsageExample]:
        """Generate examples for specific category"""
        if language == "python" and package_name == "requests":
            return self._generate_requests_examples(category)
        elif language == "javascript" and package_name == "axios":
            return self._generate_axios_examples(category)
        elif language == "python" and package_name == "pandas":
            return self._generate_pandas_examples(category)
        
        return []
    
    def _generate_requests_examples(self, category: str) -> List[UsageExample]:
        examples = {
            "quickstart": [
                UsageExample(
                    title="Simple GET Request",
                    description="Basic GET request with error handling",
                    code="""
import requests

try:
    response = requests.get('https://api.github.com/users/octocat')
    response.raise_for_status()
    user_data = response.json()
    print(f"User: {user_data['name']}")
except requests.RequestException as e:
    print(f"Request failed: {e}")
""",
                    explanation="Always check response status and handle exceptions properly"
                ),
                UsageExample(
                    title="POST Request with JSON Data",
                    description="Sending JSON data in POST request",
                    code="""
import requests
import json

data = {
    'name': 'John Doe',
    'email': 'john@example.com'
}

try:
    response = requests.post(
        'https://api.example.com/users',
        json=data,  # Automatically sets Content-Type
        timeout=10
    )
    response.raise_for_status()
    created_user = response.json()
    print(f"Created user ID: {created_user['id']}")
except requests.RequestException as e:
    print(f"Failed to create user: {e}")
""",
                    explanation="Use json parameter for automatic JSON encoding and Content-Type header"
                )
            ],
            "common_tasks": [
                UsageExample(
                    title="API Client with Session",
                    description="Reusable API client using sessions",
                    code="""
import requests
from typing import Dict, Any

class APIClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
            'User-Agent': 'MyApp/1.0'
        })
        self.session.timeout = 30
    
    def get(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()

# Usage
client = APIClient('https://api.example.com', 'your-api-key')
users = client.get('users', params={'page': 1, 'limit': 10})
""",
                    explanation="Sessions provide connection pooling and consistent configuration"
                )
            ]
        }
        
        return examples.get(category, [])
```

### Best Practice Templates

```python
class BestPracticeTemplates:
    def __init__(self):
        self.practice_categories = {
            "error_handling": "Comprehensive error handling patterns",
            "security": "Security best practices",
            "performance": "Performance optimization techniques",
            "testing": "Testing and mocking strategies",
            "configuration": "Configuration management",
            "logging": "Proper logging practices"
        }
    
    def get_best_practices(self, package_name: str, language: str) -> Dict[str, List[BestPractice]]:
        """Get best practices for specific package and language"""
        practices = {}
        
        for category in self.practice_categories:
            practices[category] = self._get_category_practices(package_name, language, category)
        
        return practices
    
    def _get_category_practices(self, package_name: str, language: str, category: str) -> List[BestPractice]:
        """Get best practices for specific category"""
        if category == "error_handling":
            return self._get_error_handling_practices(package_name, language)
        elif category == "security":
            return self._get_security_practices(package_name, language)
        elif category == "performance":
            return self._get_performance_practices(package_name, language)
        elif category == "testing":
            return self._get_testing_practices(package_name, language)
        
        return []
    
    def _get_error_handling_practices(self, package_name: str, language: str) -> List[BestPractice]:
        """Get error handling best practices"""
        if language == "python" and package_name == "requests":
            return [
                BestPractice(
                    title="Comprehensive Exception Handling",
                    description="Handle all possible request exceptions appropriately",
                    code="""
import requests
from requests.exceptions import (
    RequestException, Timeout, ConnectionError, 
    HTTPError, TooManyRedirects, InvalidURL
)

def safe_api_call(url: str, **kwargs) -> dict:
    try:
        response = requests.get(url, timeout=30, **kwargs)
        response.raise_for_status()
        return response.json()
        
    except Timeout:
        # Handle timeout specifically
        logging.error(f"Request to {url} timed out")
        raise APITimeoutError("Request timed out")
        
    except ConnectionError:
        # Handle connection issues
        logging.error(f"Failed to connect to {url}")
        raise APIConnectionError("Connection failed")
        
    except HTTPError as e:
        # Handle HTTP errors with status codes
        status_code = e.response.status_code
        if status_code == 404:
            raise APINotFoundError("Resource not found")
        elif status_code == 401:
            raise APIAuthenticationError("Authentication failed")
        elif status_code >= 500:
            raise APIServerError(f"Server error: {status_code}")
        else:
            raise APIClientError(f"Client error: {status_code}")
            
    except InvalidURL:
        logging.error(f"Invalid URL: {url}")
        raise APIInvalidURLError("Invalid URL format")
        
    except RequestException as e:
        # Catch-all for other request exceptions
        logging.error(f"Unexpected request error: {e}")
        raise APIUnknownError("Unknown request error")
""",
                    rationale="Specific exception handling allows for appropriate error recovery strategies",
                    impact="Improved reliability and user experience"
                )
            ]
        
        return []
```

### Anti-Pattern Detection

```python
class AntiPatternDetector:
    def __init__(self):
        self.anti_patterns = {
            "python": {
                "requests": self._requests_anti_patterns(),
                "pandas": self._pandas_anti_patterns(),
                "flask": self._flask_anti_patterns()
            },
            "javascript": {
                "axios": self._axios_anti_patterns(),
                "react": self._react_anti_patterns(),
                "express": self._express_anti_patterns()
            }
        }
    
    def detect_anti_patterns(self, code: str, package_name: str, language: str) -> List[AntiPatternDetection]:
        """Detect anti-patterns in code for specific package"""
        if language not in self.anti_patterns:
            return []
        
        if package_name not in self.anti_patterns[language]:
            return []
        
        patterns = self.anti_patterns[language][package_name]
        detections = []
        
        for pattern in patterns:
            if pattern.detect(code):
                detections.append(AntiPatternDetection(
                    pattern=pattern,
                    location=pattern.find_location(code),
                    severity=pattern.severity,
                    fix_suggestion=pattern.get_fix_suggestion()
                ))
        
        return detections
    
    def _requests_anti_patterns(self) -> List[AntiPattern]:
        return [
            AntiPattern(
                name="no_timeout",
                description="Making requests without timeout",
                pattern=r"requests\.(get|post|put|delete|patch)\([^)]*\)(?!.*timeout)",
                severity="high",
                explanation="Requests without timeout can hang indefinitely",
                correct_usage="requests.get(url, timeout=30)",
                code_smell="""
# BAD: No timeout specified
response = requests.get('https://api.example.com/data')

# GOOD: Timeout specified
response = requests.get('https://api.example.com/data', timeout=30)
"""
            ),
            AntiPattern(
                name="ignoring_status_codes",
                description="Not checking HTTP status codes",
                pattern=r"requests\.(get|post|put|delete|patch)\([^)]*\)(?!.*raise_for_status)",
                severity="medium",
                explanation="Ignoring status codes can lead to processing error responses as valid data",
                correct_usage="response.raise_for_status()",
                code_smell="""
# BAD: Not checking status
response = requests.get(url)
data = response.json()

# GOOD: Check status first
response = requests.get(url)
response.raise_for_status()
data = response.json()
"""
            ),
            AntiPattern(
                name="hardcoded_credentials",
                description="Hardcoded API keys or credentials",
                pattern=r"(api_key|token|password)\s*=\s*['\"][^'\"]+['\"]",
                severity="critical",
                explanation="Hardcoded credentials pose security risks",
                correct_usage="Use environment variables: os.getenv('API_KEY')",
                code_smell="""
# BAD: Hardcoded API key
api_key = "sk-1234567890abcdef"

# GOOD: Environment variable
api_key = os.getenv('API_KEY')
"""
            )
        ]
    
    def _react_anti_patterns(self) -> List[AntiPattern]:
        return [
            AntiPattern(
                name="missing_dependency_array",
                description="useEffect without dependency array",
                pattern=r"useEffect\([^)]+\)\s*(?!,\s*\[)",
                severity="high",
                explanation="Missing dependency array causes effect to run on every render",
                correct_usage="useEffect(effect, [dependencies])",
                code_smell="""
// BAD: Missing dependency array
useEffect(() => {
  fetchData();
});

// GOOD: With dependency array
useEffect(() => {
  fetchData();
}, [userId]);
"""
            ),
            AntiPattern(
                name="direct_state_mutation",
                description="Directly mutating state objects",
                pattern=r"(state\.|\.state\.)[^=]*\[\w+\]\s*=|push\(|pop\(|splice\(",
                severity="high",
                explanation="Direct state mutation breaks React's update mechanism",
                correct_usage="Use setState with new objects/arrays",
                code_smell="""
// BAD: Direct mutation
state.items.push(newItem);
setState(state);

// GOOD: Create new array
setState({
  ...state,
  items: [...state.items, newItem]
});
"""
            )
        ]
```

## Pattern Integration with Code Generation

```yaml
code_generation_integration:
  pattern_selection:
    - analyze_user_intent
    - match_to_appropriate_patterns
    - apply_language_specific_templates
    - inject_best_practices
    
  quality_enhancement:
    - automatic_error_handling_injection
    - security_pattern_application
    - performance_optimization_suggestions
    - testing_pattern_inclusion
    
  anti_pattern_prevention:
    - real_time_code_validation
    - pattern_compliance_checking
    - automatic_correction_suggestions
    - best_practice_enforcement

usage_pattern_learning:
  user_behavior_analysis:
    - track_commonly_used_patterns
    - identify_custom_patterns
    - adapt_to_team_preferences
    - learn_from_code_reviews
    
  pattern_evolution:
    - update_patterns_based_on_feedback
    - incorporate_new_best_practices
    - deprecate_outdated_patterns
    - maintain_pattern_versioning

real_time_assistance:
  ide_integration:
    - pattern_autocomplete
    - real_time_anti_pattern_detection
    - best_practice_suggestions
    - security_warning_highlights
    
  documentation_generation:
    - automatic_usage_examples
    - pattern_explanation_injection
    - best_practice_documentation
    - troubleshooting_guides
```

## Usage Examples

```python
# Example: Generate usage patterns for a package
pattern_engine = PackageUsagePatterns()

# Get comprehensive patterns for requests library
patterns = pattern_engine.get_usage_pattern("requests", "python", "basic_usage")
print(f"Pattern: {patterns.name}")
print(f"Code:\n{patterns.code}")

# Detect anti-patterns in user code
code_sample = """
import requests
response = requests.get('https://api.example.com/data')
data = response.json()
"""

anti_patterns = pattern_engine.detect_anti_patterns(code_sample, "requests", "python")
for detection in anti_patterns:
    print(f"Anti-pattern: {detection.pattern.name}")
    print(f"Fix: {detection.fix_suggestion}")

# Generate best practice examples
best_practices = pattern_engine.get_best_practices("react", "javascript")
for category, practices in best_practices.items():
    print(f"Category: {category}")
    for practice in practices:
        print(f"  - {practice.title}: {practice.description}")
```

This package usage pattern system provides comprehensive templates, examples, and guidance to ensure generated code follows language-specific best practices and avoids common anti-patterns while maintaining security and performance standards.