# Package Whitelist System (I16)

| version | last_updated | status | agent |
|---------|--------------|---------|-------|
| 1.0.0   | 2025-07-20   | active | I16 |

## Purpose
Comprehensive package whitelist management system for preventing LLM hallucinations and ensuring only verified, real packages are used in code generation across all programming languages.

## Core Capabilities

### Language-Specific Package Repositories

```xml
<package_repositories>
  <python>
    <pypi>
      <verification_api>https://pypi.org/pypi/{package}/json</verification_api>
      <search_api>https://pypi.org/search/?q={query}</search_api>
      <status_codes>200=exists, 404=not_found</status_codes>
    </pypi>
    <conda>
      <verification_api>https://api.anaconda.org/package/conda-forge/{package}</verification_api>
      <channels>conda-forge, bioconda, pytorch</channels>
    </conda>
  </python>
  
  <javascript>
    <npm>
      <verification_api>https://registry.npmjs.org/{package}</verification_api>
      <unpkg>https://unpkg.com/{package}/package.json</unpkg>
      <status_codes>200=exists, 404=not_found</status_codes>
    </npm>
    <yarn>
      <registry>https://registry.yarnpkg.com/{package}</registry>
    </yarn>
  </javascript>
  
  <go>
    <modules>
      <verification_api>https://proxy.golang.org/{module}/@v/list</verification_api>
      <pkg_go_dev>https://pkg.go.dev/{module}</pkg_go_dev>
    </modules>
  </go>
  
  <rust>
    <crates_io>
      <verification_api>https://crates.io/api/v1/crates/{crate}</verification_api>
      <status_codes>200=exists, 404=not_found</status_codes>
    </crates_io>
  </rust>
  
  <java>
    <maven_central>
      <verification_api>https://search.maven.org/solrsearch/select?q=g:{group}+AND+a:{artifact}</verification_api>
      <format>response.numFound > 0 = exists</format>
    </maven_central>
  </java>
  
  <php>
    <packagist>
      <verification_api>https://packagist.org/packages/{vendor}/{package}.json</verification_api>
      <status_codes>200=exists, 404=not_found</status_codes>
    </packagist>
  </php>
  
  <ruby>
    <rubygems>
      <verification_api>https://rubygems.org/api/v1/gems/{gem}.json</verification_api>
      <status_codes>200=exists, 404=not_found</status_codes>
    </rubygems>
  </ruby>
  
  <c_sharp>
    <nuget>
      <verification_api>https://api.nuget.org/v3-flatcontainer/{package}/index.json</verification_api>
      <status_codes>200=exists, 404=not_found</status_codes>
    </nuget>
  </c_sharp>
</package_repositories>
```

### Comprehensive Package Whitelist

```python
# Real-time Package Verification System
VERIFIED_PACKAGES = {
    "python": {
        "core": [
            "requests", "numpy", "pandas", "flask", "django", "fastapi",
            "pytest", "click", "sqlalchemy", "psycopg2", "redis", "celery",
            "boto3", "pydantic", "uvicorn", "gunicorn", "pillow", "matplotlib"
        ],
        "ai_ml": [
            "tensorflow", "pytorch", "scikit-learn", "transformers", "openai",
            "langchain", "chromadb", "faiss-cpu", "sentence-transformers"
        ],
        "web": [
            "aiohttp", "starlette", "jinja2", "wtforms", "marshmallow",
            "httpx", "websockets", "socketio"
        ],
        "testing": [
            "pytest", "unittest", "mock", "coverage", "tox", "black", "flake8",
            "mypy", "bandit", "safety"
        ]
    },
    
    "javascript": {
        "core": [
            "react", "vue", "angular", "express", "next", "nuxt", "gatsby",
            "lodash", "axios", "fetch", "socket.io", "moment", "dayjs"
        ],
        "build_tools": [
            "webpack", "vite", "rollup", "parcel", "babel", "typescript",
            "eslint", "prettier", "jest", "cypress", "playwright"
        ],
        "ui": [
            "tailwindcss", "bootstrap", "material-ui", "antd", "chakra-ui",
            "styled-components", "emotion"
        ]
    },
    
    "go": {
        "core": [
            "github.com/gin-gonic/gin", "github.com/gorilla/mux",
            "github.com/labstack/echo", "github.com/go-chi/chi",
            "gorm.io/gorm", "github.com/lib/pq", "go.mongodb.org/mongo-driver"
        ],
        "testing": [
            "github.com/stretchr/testify", "github.com/onsi/ginkgo",
            "github.com/golang/mock"
        ]
    },
    
    "rust": {
        "core": [
            "serde", "tokio", "actix-web", "warp", "reqwest", "clap",
            "diesel", "sqlx", "uuid", "chrono", "regex"
        ],
        "async": [
            "async-std", "futures", "async-trait"
        ]
    }
}
```

### Version Verification Mechanisms

```python
# Version Validation System
class PackageVersionValidator:
    def __init__(self):
        self.version_patterns = {
            "semantic": r"^\d+\.\d+\.\d+(-[\w\d\.-]+)?(\+[\w\d\.-]+)?$",
            "python_dev": r"^\d+\.\d+\.\d+(\.dev\d+)?$",
            "npm_prerelease": r"^\d+\.\d+\.\d+(-[a-zA-Z]+\.\d+)?$"
        }
    
    def validate_version_format(self, version: str, language: str) -> bool:
        """Validate version string format"""
        if language in ["python", "rust"]:
            return bool(re.match(self.version_patterns["semantic"], version))
        elif language == "javascript":
            return bool(re.match(self.version_patterns["npm_prerelease"], version))
        return True
    
    def check_version_exists(self, package: str, version: str, language: str) -> bool:
        """Verify version exists in package repository"""
        api_endpoints = {
            "python": f"https://pypi.org/pypi/{package}/{version}/json",
            "javascript": f"https://registry.npmjs.org/{package}/{version}",
            "go": f"https://proxy.golang.org/{package}/@v/{version}.info",
            "rust": f"https://crates.io/api/v1/crates/{package}/{version}"
        }
        
        if language not in api_endpoints:
            return False
            
        try:
            response = requests.get(api_endpoints[language], timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False
    
    def get_latest_version(self, package: str, language: str) -> Optional[str]:
        """Get latest stable version of package"""
        try:
            if language == "python":
                response = requests.get(f"https://pypi.org/pypi/{package}/json")
                if response.status_code == 200:
                    return response.json()["info"]["version"]
            elif language == "javascript":
                response = requests.get(f"https://registry.npmjs.org/{package}/latest")
                if response.status_code == 200:
                    return response.json()["version"]
        except requests.RequestException:
            pass
        return None
```

### Package Validation Patterns

```python
# Validation Pattern Engine
class PackageValidationEngine:
    def __init__(self):
        self.validation_cache = {}
        self.cache_ttl = 3600  # 1 hour
    
    def validate_package_existence(self, package_spec: dict) -> ValidationResult:
        """
        Validate package exists in official repository
        
        Args:
            package_spec: {
                "name": "package_name",
                "version": "1.0.0",
                "language": "python",
                "source": "pypi"
            }
        """
        cache_key = f"{package_spec['language']}:{package_spec['name']}:{package_spec.get('version', 'latest')}"
        
        # Check cache first
        if self.is_cache_valid(cache_key):
            return self.validation_cache[cache_key]
        
        result = self._perform_validation(package_spec)
        self.validation_cache[cache_key] = {
            "result": result,
            "timestamp": time.time()
        }
        
        return result
    
    def _perform_validation(self, package_spec: dict) -> ValidationResult:
        """Perform actual package validation"""
        language = package_spec["language"]
        package_name = package_spec["name"]
        version = package_spec.get("version")
        
        # Step 1: Check if package is in whitelist
        if not self.is_whitelisted(package_name, language):
            return ValidationResult(
                valid=False,
                reason="Package not in whitelist",
                suggestion=self.suggest_alternatives(package_name, language)
            )
        
        # Step 2: Verify package exists in repository
        if not self.verify_repository_existence(package_name, language):
            return ValidationResult(
                valid=False,
                reason="Package does not exist in official repository",
                suggestion="Check package name spelling or use alternative"
            )
        
        # Step 3: Validate version if specified
        if version and not self.validate_version_exists(package_name, version, language):
            latest_version = self.get_latest_version(package_name, language)
            return ValidationResult(
                valid=False,
                reason=f"Version {version} does not exist",
                suggestion=f"Use latest version: {latest_version}"
            )
        
        return ValidationResult(valid=True, reason="Package validated successfully")
```

### Fallback Mechanisms

```python
# Fallback System for Missing Packages
class PackageFallbackSystem:
    def __init__(self):
        self.fallback_mappings = {
            "python": {
                # Common misspellings and alternatives
                "beautifulsoup": "beautifulsoup4",
                "pil": "pillow",
                "yaml": "pyyaml",
                "cv2": "opencv-python",
                "sklearn": "scikit-learn",
                "torch": "pytorch"
            },
            "javascript": {
                "react-dom": "@types/react-dom",
                "jquery": "jquery",
                "bootstrap": "bootstrap",
                "moment": "dayjs"  # Modern alternative
            },
            "go": {
                "uuid": "github.com/google/uuid",
                "mux": "github.com/gorilla/mux"
            }
        }
        
        self.category_alternatives = {
            "http_client": {
                "python": ["requests", "httpx", "aiohttp"],
                "javascript": ["axios", "fetch", "node-fetch"],
                "go": ["net/http", "github.com/go-resty/resty"],
                "rust": ["reqwest", "hyper"]
            },
            "json_parsing": {
                "python": ["json", "orjson", "ujson"],
                "javascript": ["JSON", "fast-json-stringify"],
                "go": ["encoding/json", "github.com/json-iterator/go"],
                "rust": ["serde_json", "simd-json"]
            },
            "testing": {
                "python": ["pytest", "unittest", "nose2"],
                "javascript": ["jest", "mocha", "vitest"],
                "go": ["testing", "github.com/stretchr/testify"],
                "rust": ["built-in test", "criterion"]
            }
        }
    
    def suggest_fallback(self, package_name: str, language: str) -> List[str]:
        """Suggest fallback packages for missing/invalid packages"""
        suggestions = []
        
        # Direct mapping fallback
        if language in self.fallback_mappings:
            if package_name in self.fallback_mappings[language]:
                suggestions.append(self.fallback_mappings[language][package_name])
        
        # Category-based suggestions
        package_category = self.detect_package_category(package_name)
        if package_category and package_category in self.category_alternatives:
            if language in self.category_alternatives[package_category]:
                suggestions.extend(self.category_alternatives[package_category][language])
        
        # Fuzzy matching for typos
        fuzzy_matches = self.fuzzy_match_packages(package_name, language)
        suggestions.extend(fuzzy_matches[:3])  # Top 3 matches
        
        return list(dict.fromkeys(suggestions))  # Remove duplicates while preserving order
    
    def detect_package_category(self, package_name: str) -> Optional[str]:
        """Detect package category based on name patterns"""
        category_patterns = {
            "http_client": ["http", "request", "client", "fetch", "curl"],
            "json_parsing": ["json", "parse", "serialize"],
            "testing": ["test", "spec", "mock", "assert", "expect"],
            "database": ["db", "sql", "mongo", "redis", "postgres"],
            "ui_framework": ["ui", "component", "react", "vue", "angular"]
        }
        
        package_lower = package_name.lower()
        for category, keywords in category_patterns.items():
            if any(keyword in package_lower for keyword in keywords):
                return category
        return None
```

## Integration with LLM Code Generation

```python
# LLM Integration Hooks
class LLMPackageValidator:
    def __init__(self, whitelist_system: PackageWhitelistSystem):
        self.whitelist = whitelist_system
        self.validation_prompts = {
            "pre_generation": """
            Before generating any code with package imports, validate all packages using the package whitelist system.
            CRITICAL: Never use packages that don't exist in official repositories.
            """,
            
            "package_validation": """
            For each package in the code:
            1. Check if package exists in whitelist
            2. Verify package exists in official repository
            3. Validate version compatibility
            4. Suggest alternatives if package invalid
            """,
            
            "post_validation": """
            After code generation, run final package validation:
            - All imports must be from verified packages
            - All versions must exist in repositories
            - Provide installation commands for all packages
            """
        }
    
    def validate_generated_code(self, code: str, language: str) -> ValidationReport:
        """Validate all packages in generated code"""
        extracted_packages = self.extract_packages_from_code(code, language)
        validation_results = []
        
        for package in extracted_packages:
            result = self.whitelist.validate_package_existence({
                "name": package["name"],
                "version": package.get("version"),
                "language": language
            })
            validation_results.append({
                "package": package,
                "result": result
            })
        
        return ValidationReport(
            code=code,
            language=language,
            validations=validation_results,
            overall_valid=all(r["result"].valid for r in validation_results)
        )
```

## Real-Time Validation Capabilities

```yaml
real_time_validation:
  triggers:
    - code_generation_start
    - import_statement_creation
    - dependency_file_modification
    - package_installation_request
  
  validation_speed:
    - api_calls: < 500ms
    - cache_hits: < 10ms
    - batch_validation: < 2s for 50 packages
  
  error_prevention:
    - block_invalid_packages: true
    - suggest_alternatives: true
    - provide_installation_commands: true
    - validate_version_compatibility: true

monitoring:
  metrics:
    - validation_success_rate
    - api_response_times
    - cache_hit_ratio
    - false_positive_rate
  
  alerts:
    - new_package_requests
    - validation_failures
    - api_endpoint_failures
    - cache_invalidation_events
```

## Usage Examples

```python
# Example: Validating Python packages
validator = PackageWhitelistSystem()

# Validate single package
result = validator.validate_package("requests", "python", "2.28.1")
print(f"Valid: {result.valid}, Reason: {result.reason}")

# Validate code with multiple packages
code = """
import requests
import pandas as pd
import nonexistent_package
"""

report = validator.validate_code(code, "python")
for validation in report.validations:
    if not validation["result"].valid:
        print(f"Invalid package: {validation['package']['name']}")
        print(f"Suggestion: {validation['result'].suggestion}")
```

## Integration Points

- **LLM Code Generation**: Pre-validation before any package usage
- **IDE Integration**: Real-time validation in development environments  
- **CI/CD Pipeline**: Automated package validation in build processes
- **Documentation**: Auto-generated package documentation with verified examples
- **Security Scanning**: Integration with vulnerability databases

This module provides the foundation for preventing LLM package hallucinations while ensuring developers have access to comprehensive, verified package ecosystems across all major programming languages.