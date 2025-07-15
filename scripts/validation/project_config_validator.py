#!/usr/bin/env python3
"""
Unified PROJECT_CONFIG.xml Validation System

Comprehensive validation combining:
- Tier-aware validation (minimal/standard/advanced)
- Placeholder resolution testing
- Domain-specific validation
- Minimal config generation
- Intelligent suggestions and auto-fixes

Consolidates functionality from:
- validate-project-config.py (placeholder resolution)
- scripts/config/configuration_validator.py (tier-aware validation)
- scripts/config/framework/config_validator.py (minimal config generation)

Author: Claude Code Framework - Phase 2.1 Consolidation
Version: 2.0.0
Date: 2025-07-15
"""

try:
    import defusedxml.ElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    import warnings
    warnings.warn("defusedxml not available, using standard XML parser. Install defusedxml for better security.")

from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import logging
import re
import sys
import os
import json
import argparse


class ValidationLevel(Enum):
    """Validation severity levels"""
    ERROR = "error"
    WARNING = "warning" 
    INFO = "info"
    SUGGESTION = "suggestion"


class ConfigTier(Enum):
    """Configuration tier levels"""
    MINIMAL = "minimal"
    STANDARD = "standard"
    ADVANCED = "advanced"


@dataclass
class ValidationIssue:
    """Represents a validation issue"""
    level: ValidationLevel
    message: str
    path: str
    suggestion: Optional[str] = None
    auto_fix: Optional[str] = None


@dataclass 
class ValidationResult:
    """Results of configuration validation"""
    is_valid: bool
    issues: List[ValidationIssue]
    suggestions: List[str]
    tier: ConfigTier
    confidence_score: float
    config_values: Dict[str, str]
    placeholder_results: Dict[str, str]


class UnifiedProjectConfigValidator:
    """
    Unified validation system combining all validation approaches.
    
    Features:
    - Tier-aware validation (minimal/standard/advanced)
    - Placeholder resolution testing and validation
    - Domain-specific validation rules
    - Minimal configuration generation
    - Intelligent suggestions and auto-fixes
    - Project context analysis
    """
    
    def __init__(self, project_root: Optional[str] = None):
        """
        Initialize unified configuration validator.
        
        Args:
            project_root: Path to project root directory (default: current directory)
        """
        self.project_root = Path(project_root) if project_root else Path.cwd()
        self.config_file = self.project_root / "PROJECT_CONFIG.xml"
        self.logger = logging.getLogger(__name__)
        
        # Core validation configuration
        self.required_sections = {
            'project_info': {
                'required_fields': ['name', 'primary_language'],
                'optional_fields': ['description', 'domain', 'framework_stack']
            },
            'project_structure': {
                'required_fields': ['source_directory', 'test_directory'],
                'optional_fields': ['docs_directory', 'scripts_directory', 'config_directory', 'build_directory']
            },
            'quality_standards': {
                'required_fields': ['test_coverage'],
                'optional_fields': ['code_quality', 'performance', 'security_requirements']
            },
            'development_workflow': {
                'required_fields': ['commands'],
                'optional_fields': ['git_workflow']
            }
        }
        
        self.optional_sections = {
            'domain_specific_rules': 'Project-specific rules and requirements',
            'custom_personas': 'Custom personas for the project',
            'security_requirements': 'Security and compliance requirements',
            'deployment': 'Deployment configuration',
            'framework_behavior': 'Framework behavior customization',
            'integrations': 'External API and service integrations'
        }
        
        # Valid values for specific fields
        self.valid_values = {
            'domain': [
                'web-development', 'mobile-engineering', 'data-analytics', 
                'data-engineering', 'devops-platform', 'enterprise-tools',
                'financial-technology', 'machine-learning', 'platform-engineering',
                'game-development', 'fintech', 'healthcare', 'e-commerce', 'general-development'
            ],
            'primary_language': [
                'javascript', 'typescript', 'python', 'java', 'go', 'rust',
                'cpp', 'csharp', 'swift', 'kotlin', 'php', 'ruby', 'c', 'dart'
            ],
            'test_coverage.enforcement': ['BLOCKING', 'CONDITIONAL', 'ADVISORY'],
            'file_creation_policy': ['conservative', 'moderate', 'permissive'],
            'test_first_enforcement': ['strict', 'flexible', 'advisory'],
            'documentation_generation': ['automatic', 'on-request', 'manual']
        }
        
        # Domain-specific validators
        self.domain_validators = {
            "web-development": self._validate_web_development,
            "data-analytics": self._validate_data_analytics,
            "mobile-engineering": self._validate_mobile_engineering,
            "platform-engineering": self._validate_platform_engineering
        }
        
        # Placeholder test cases from CLAUDE.md
        self.claude_md_placeholders = [
            ("source_directory", "project_structure.source_directory", "src"),
            ("test_directory", "project_structure.test_directory", "tests"),
            ("docs_directory", "project_structure.docs_directory", "docs"),
            ("scripts_directory", "project_structure.scripts_directory", "scripts"),
            ("test_coverage.threshold", "quality_standards.test_coverage.threshold", "90"),
            ("performance.response_time_p95", "quality_standards.performance.response_time_p95", "200ms"),
            ("commands.test", "development_workflow.commands.test", "language-specific"),
            ("commands.lint", "development_workflow.commands.lint", "language-specific"),
            ("commands.build", "development_workflow.commands.build", "language-specific"),
            ("ai_temperature.factual", "framework_behavior.ai_temperature.factual", "0.2"),
            ("ai_temperature.analysis", "framework_behavior.ai_temperature.analysis", "0.3"),
            ("ai_temperature.creative", "framework_behavior.ai_temperature.creative", "0.7"),
        ]
    
    def validate(self, config_path: Optional[Path] = None, enable_placeholder_testing: bool = True) -> ValidationResult:
        """
        Comprehensive validation combining all validation approaches.
        
        Args:
            config_path: Path to config file (default: PROJECT_CONFIG.xml in project root)
            enable_placeholder_testing: Whether to test placeholder resolution
            
        Returns:
            ValidationResult with comprehensive validation details
        """
        config_path = config_path or self.config_file
        
        # Initialize result
        result = ValidationResult(
            is_valid=True,
            issues=[],
            suggestions=[],
            tier=ConfigTier.MINIMAL,
            confidence_score=0.0,
            config_values={},
            placeholder_results={}
        )
        
        # Check if config file exists
        if not config_path.exists():
            result.is_valid = False
            result.issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                message=f"PROJECT_CONFIG.xml not found at {config_path}",
                path="root",
                suggestion="Create PROJECT_CONFIG.xml using generate_minimal_config() or copy from template"
            ))
            return result
        
        try:
            # Parse XML
            tree = ET.parse(config_path)
            root = tree.getroot()
            
            # Validate root element
            if root.tag != 'project_configuration':
                result.issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    message=f"Root element should be 'project_configuration', found '{root.tag}'",
                    path="root"
                ))
                result.is_valid = False
            
            # Load configuration values
            result.config_values = self._load_config_values(root)
            
            # Determine configuration tier
            result.tier = self._determine_tier(root)
            
            # Core validations
            result.issues.extend(self._validate_core_structure(root))
            result.issues.extend(self._validate_project_info(root))
            
            # Tier-appropriate validations
            if result.tier in [ConfigTier.STANDARD, ConfigTier.ADVANCED]:
                result.issues.extend(self._validate_quality_standards(root))
                result.issues.extend(self._validate_development_workflow(root))
            
            if result.tier == ConfigTier.ADVANCED:
                result.issues.extend(self._validate_advanced_features(root))
                result.issues.extend(self._validate_security_requirements(root))
                result.issues.extend(self._validate_integrations(root))
            
            # Domain-specific validation
            domain = self._get_domain(root)
            if domain in self.domain_validators:
                result.issues.extend(self.domain_validators[domain](root, result.tier))
            
            # Placeholder resolution testing
            if enable_placeholder_testing:
                result.placeholder_results = self._test_placeholder_resolution(result.config_values)
                result.issues.extend(self._validate_claude_md_placeholders(config_path.parent))
            
            # Generate intelligent suggestions
            result.suggestions = self._generate_suggestions(root, result.issues, self.project_root)
            
            # Calculate confidence score
            result.confidence_score = self._calculate_confidence(result.issues, result.tier)
            
            # Final validation status
            result.is_valid = not any(issue.level == ValidationLevel.ERROR for issue in result.issues)
            
        except ET.ParseError as e:
            result.is_valid = False
            result.issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                message=f"XML parsing error: {e}",
                path="root"
            ))
        except Exception as e:
            result.is_valid = False
            result.issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                message=f"Validation error: {e}",
                path="root"
            ))
        
        return result
    
    def _load_config_values(self, root: ET.Element) -> Dict[str, str]:
        """Load all configuration values into a flat dictionary with dot notation."""
        config_values = {}
        
        def extract_values(element, path=""):
            for child in element:
                child_path = f"{path}.{child.tag}" if path else child.tag
                if child.text and child.text.strip():
                    config_values[child_path] = child.text.strip()
                extract_values(child, child_path)
        
        extract_values(root)
        return config_values
    
    def _determine_tier(self, root: ET.Element) -> ConfigTier:
        """Determine the configuration tier based on complexity and explicit setting."""
        # Check for explicit tier attribute
        tier_attr = root.get("tier")
        if tier_attr:
            try:
                return ConfigTier(tier_attr)
            except ValueError:
                pass
        
        # Infer tier from complexity
        sections = len(list(root))
        custom_personas = root.find("custom_personas") is not None
        custom_rules = root.find("domain_specific_rules") is not None
        integrations = root.find("integrations") is not None
        security = root.find("security_requirements") is not None
        
        if sections <= 6 and not custom_personas and not integrations and not security:
            return ConfigTier.MINIMAL
        elif sections <= 10 and not custom_personas:
            return ConfigTier.STANDARD
        else:
            return ConfigTier.ADVANCED
    
    def _validate_core_structure(self, root: ET.Element) -> List[ValidationIssue]:
        """Validate core XML structure and required sections."""
        issues = []
        
        # Check version
        version = root.get("version")
        if not version:
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                message="Missing version attribute",
                path="root",
                suggestion="Add version='1.0.0' to project_configuration element",
                auto_fix='version="1.0.0"'
            ))
        elif version != "1.0.0":
            issues.append(ValidationIssue(
                level=ValidationLevel.INFO,
                message=f"Version {version} may not be compatible with current framework",
                path="root"
            ))
        
        # Check required sections for minimal configuration
        required_sections = ["project_info"]
        for section in required_sections:
            if root.find(section) is None:
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    message=f"Missing required section: {section}",
                    path="root",
                    auto_fix=f"<{section}></{section}>"
                ))
        
        return issues
    
    def _validate_project_info(self, root: ET.Element) -> List[ValidationIssue]:
        """Validate project_info section with comprehensive checks."""
        issues = []
        project_info = root.find("project_info")
        
        if project_info is None:
            return issues
        
        # Required fields
        required_fields = ["name", "primary_language"]
        for field in required_fields:
            element = project_info.find(field)
            if element is None or not element.text:
                issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    message=f"Missing required field: project_info.{field}",
                    path=f"project_info.{field}",
                    auto_fix=f"<{field}>Your Project Name</{field}>"
                ))
        
        # Validate language
        language_elem = project_info.find("primary_language")
        if language_elem is not None and language_elem.text:
            if language_elem.text.lower() not in self.valid_values['primary_language']:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    message=f"Unusual primary language: {language_elem.text}",
                    path="project_info.primary_language",
                    suggestion=f"Consider one of: {', '.join(self.valid_values['primary_language'][:5])}, ..."
                ))
        
        # Validate domain
        domain_elem = project_info.find("domain")
        if domain_elem is not None and domain_elem.text:
            if domain_elem.text not in self.valid_values['domain']:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    message=f"Unknown domain: {domain_elem.text}",
                    path="project_info.domain",
                    suggestion=f"Consider one of: {', '.join(self.valid_values['domain'][:3])}, ..."
                ))
        
        return issues
    
    def _validate_quality_standards(self, root: ET.Element) -> List[ValidationIssue]:
        """Validate quality_standards section with coverage enforcement."""
        issues = []
        quality_standards = root.find("quality_standards")
        
        if quality_standards is None:
            issues.append(ValidationIssue(
                level=ValidationLevel.INFO,
                message="No quality standards defined, using framework defaults",
                path="quality_standards",
                suggestion="Consider adding quality_standards section for production projects"
            ))
            return issues
        
        # Validate test coverage
        test_coverage = quality_standards.find("test_coverage")
        if test_coverage is not None:
            # Check threshold
            threshold_elem = test_coverage.find("threshold")
            if threshold_elem is not None:
                try:
                    threshold = int(threshold_elem.text)
                    if not 0 <= threshold <= 100:
                        issues.append(ValidationIssue(
                            level=ValidationLevel.ERROR,
                            message=f"Invalid coverage threshold: {threshold}% (must be 0-100)",
                            path="quality_standards.test_coverage.threshold"
                        ))
                    elif threshold < 70:
                        issues.append(ValidationIssue(
                            level=ValidationLevel.WARNING,
                            message=f"Low coverage threshold: {threshold}% (recommended: 80%+)",
                            path="quality_standards.test_coverage.threshold",
                            suggestion="Consider increasing to at least 80% for production code"
                        ))
                except ValueError:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        message=f"Invalid coverage threshold: {threshold_elem.text} (must be number)",
                        path="quality_standards.test_coverage.threshold"
                    ))
            
            # Check enforcement
            enforcement_elem = test_coverage.find("enforcement")
            if enforcement_elem is not None:
                if enforcement_elem.text not in self.valid_values['test_coverage.enforcement']:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        message=f"Invalid enforcement: {enforcement_elem.text}",
                        path="quality_standards.test_coverage.enforcement",
                        suggestion=f"Must be one of: {', '.join(self.valid_values['test_coverage.enforcement'])}"
                    ))
        
        # Validate performance targets
        performance = quality_standards.find("performance")
        if performance is not None:
            response_time = performance.find("response_time_p95")
            if response_time is not None:
                time_pattern = re.compile(r'^\d+ms$')
                if not time_pattern.match(response_time.text):
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        message=f"Invalid response time format: {response_time.text} (use format: 200ms)",
                        path="quality_standards.performance.response_time_p95"
                    ))
        
        return issues
    
    def _validate_development_workflow(self, root: ET.Element) -> List[ValidationIssue]:
        """Validate development_workflow section."""
        issues = []
        workflow = root.find("development_workflow")
        
        if workflow is None:
            return issues
        
        # Validate commands
        commands = workflow.find("commands")
        if commands is not None:
            recommended_commands = ["install", "test", "build", "lint"]
            for cmd in recommended_commands:
                cmd_elem = commands.find(cmd)
                if cmd_elem is None or not cmd_elem.text:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.WARNING,
                        message=f"Missing recommended command: {cmd}",
                        path=f"development_workflow.commands.{cmd}",
                        suggestion=f"Add <{cmd}>auto-detect</{cmd}> for automatic detection"
                    ))
        
        return issues
    
    def _validate_advanced_features(self, root: ET.Element) -> List[ValidationIssue]:
        """Validate advanced configuration features."""
        issues = []
        
        # Validate custom personas
        personas = root.find("custom_personas")
        if personas is not None:
            for persona in personas.findall("persona"):
                name_elem = persona.find("name")
                if name_elem is None or not name_elem.text:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        message="Custom persona missing name",
                        path="custom_personas.persona.name"
                    ))
                
                expertise_elem = persona.find("expertise")
                if expertise_elem is None or not expertise_elem.text:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.WARNING,
                        message="Custom persona missing expertise description",
                        path="custom_personas.persona.expertise"
                    ))
        
        return issues
    
    def _validate_security_requirements(self, root: ET.Element) -> List[ValidationIssue]:
        """Validate security requirements."""
        issues = []
        security = root.find("security_requirements")
        
        if security is None:
            return issues
        
        # Check for basic security measures
        auth_elem = security.find("authentication")
        if auth_elem is not None and auth_elem.text == "none":
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                message="No authentication configured",
                path="security_requirements.authentication",
                suggestion="Consider adding authentication for production applications"
            ))
        
        encryption_elem = security.find("data_encryption")
        if encryption_elem is not None and encryption_elem.text == "none":
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                message="No data encryption configured",
                path="security_requirements.data_encryption",
                suggestion="Consider encryption for sensitive data"
            ))
        
        return issues
    
    def _validate_integrations(self, root: ET.Element) -> List[ValidationIssue]:
        """Validate integration configurations."""
        issues = []
        integrations = root.find("integrations")
        
        if integrations is None:
            return issues
        
        # Validate external APIs
        external_apis = integrations.find("external_apis")
        if external_apis is not None:
            for api in external_apis.findall("api"):
                name_elem = api.find("name")
                type_elem = api.find("type")
                
                if name_elem is None or not name_elem.text:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        message="External API missing name",
                        path="integrations.external_apis.api.name"
                    ))
                
                if type_elem is not None:
                    valid_types = ["REST", "GraphQL", "gRPC", "WebSocket", "SOAP"]
                    if type_elem.text not in valid_types:
                        issues.append(ValidationIssue(
                            level=ValidationLevel.WARNING,
                            message=f"Unknown API type: {type_elem.text}",
                            path="integrations.external_apis.api.type",
                            suggestion=f"Common types: {', '.join(valid_types)}"
                        ))
        
        return issues
    
    def _validate_web_development(self, root: ET.Element, tier: ConfigTier) -> List[ValidationIssue]:
        """Domain-specific validation for web development projects."""
        issues = []
        
        # Check for web-specific performance targets
        quality_standards = root.find("quality_standards")
        if quality_standards is not None:
            performance = quality_standards.find("performance")
            if performance is not None:
                response_time = performance.find("response_time_p95")
                if response_time is not None:
                    try:
                        time_ms = int(response_time.text.replace("ms", ""))
                        if time_ms > 500:
                            issues.append(ValidationIssue(
                                level=ValidationLevel.WARNING,
                                message=f"High response time target: {time_ms}ms (web apps typically < 300ms)",
                                path="quality_standards.performance.response_time_p95",
                                suggestion="Consider reducing to 200-300ms for better user experience"
                            ))
                    except (ValueError, AttributeError):
                        pass
        
        return issues
    
    def _validate_data_analytics(self, root: ET.Element, tier: ConfigTier) -> List[ValidationIssue]:
        """Domain-specific validation for data analytics projects."""
        issues = []
        
        # Check for data-specific structure
        project_structure = root.find("project_structure")
        if project_structure is not None:
            data_dir = project_structure.find("data_directory")
            if data_dir is None:
                issues.append(ValidationIssue(
                    level=ValidationLevel.SUGGESTION,
                    message="Consider adding data_directory for data analytics projects",
                    path="project_structure",
                    suggestion="Add <data_directory>data</data_directory>"
                ))
        
        return issues
    
    def _validate_mobile_engineering(self, root: ET.Element, tier: ConfigTier) -> List[ValidationIssue]:
        """Domain-specific validation for mobile engineering projects."""
        issues = []
        
        # Check for mobile-appropriate performance targets
        quality_standards = root.find("quality_standards")
        if quality_standards is not None:
            performance = quality_standards.find("performance")
            if performance is not None:
                memory_limit = performance.find("memory_limit")
                if memory_limit is not None and "GB" in memory_limit.text:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.WARNING,
                        message="High memory limit for mobile application",
                        path="quality_standards.performance.memory_limit",
                        suggestion="Mobile apps typically use 256-512MB memory limits"
                    ))
        
        return issues
    
    def _validate_platform_engineering(self, root: ET.Element, tier: ConfigTier) -> List[ValidationIssue]:
        """Domain-specific validation for platform engineering projects."""
        issues = []
        
        # Check for infrastructure-related configurations
        deployment = root.find("deployment")
        if deployment is None and tier == ConfigTier.ADVANCED:
            issues.append(ValidationIssue(
                level=ValidationLevel.SUGGESTION,
                message="Consider adding deployment configuration for platform engineering",
                path="deployment",
                suggestion="Platform projects typically need detailed deployment configurations"
            ))
        
        return issues
    
    def _test_placeholder_resolution(self, config_values: Dict[str, str]) -> Dict[str, str]:
        """Test dynamic placeholder resolution against CLAUDE.md patterns."""
        placeholder_results = {}
        
        for placeholder, config_path, default in self.claude_md_placeholders:
            resolved = self._resolve_placeholder(placeholder, default, config_values)
            placeholder_results[placeholder] = resolved
        
        return placeholder_results
    
    def _resolve_placeholder(self, path: str, default: str, config_values: Dict[str, str]) -> str:
        """Simulate runtime placeholder resolution with comprehensive path searching."""
        # Direct lookup first
        if path in config_values:
            return config_values[path]
        
        # Convert placeholder path formats and search comprehensively
        search_paths = [
            path,
            path.replace("_", "."),
            f"project_structure.{path}",
            f"quality_standards.{path}",
            f"development_workflow.{path}",
            f"framework_behavior.{path}",
            f"quality_standards.test_coverage.{path}",
            f"quality_standards.performance.{path}",
            f"development_workflow.commands.{path}",
            f"framework_behavior.ai_temperature.{path}"
        ]
        
        for search_path in search_paths:
            if search_path in config_values:
                return config_values[search_path]
        
        # Try suffix matching
        for key, value in config_values.items():
            if key.endswith(f".{path}") or key.endswith(f".{path.replace('_', '.')}"):
                return value
        
        return default
    
    def _validate_claude_md_placeholders(self, project_root: Path) -> List[ValidationIssue]:
        """Validate that all CLAUDE.md placeholders can be resolved."""
        issues = []
        
        # Try to find CLAUDE.md
        potential_paths = [
            project_root / "CLAUDE.md",
            project_root.parent / "CLAUDE.md",
            project_root.parent.parent / "CLAUDE.md",
            Path.cwd() / "CLAUDE.md"
        ]
        
        claude_md_path = None
        for path in potential_paths:
            if path.exists():
                claude_md_path = path
                break
        
        if not claude_md_path:
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                message="CLAUDE.md not found for placeholder validation",
                path="claude_md",
                suggestion="Ensure CLAUDE.md exists in project root for complete validation"
            ))
            return issues
        
        try:
            with open(claude_md_path, 'r') as f:
                content = f.read()
            
            # Find all [PROJECT_CONFIG: path | DEFAULT: value] patterns
            pattern = r'\[PROJECT_CONFIG:\s*([^|]+)\s*\|\s*DEFAULT:\s*([^\]]+)\]'
            placeholders = re.findall(pattern, content)
            
            unique_placeholders = set(placeholders)
            if unique_placeholders:
                issues.append(ValidationIssue(
                    level=ValidationLevel.INFO,
                    message=f"Found {len(unique_placeholders)} CLAUDE.md placeholders for validation",
                    path="claude_md_placeholders"
                ))
        
        except Exception as e:
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                message=f"Error reading CLAUDE.md: {e}",
                path="claude_md"
            ))
        
        return issues
    
    def _get_domain(self, root: ET.Element) -> str:
        """Extract domain from configuration."""
        project_info = root.find("project_info")
        if project_info is not None:
            domain_elem = project_info.find("domain")
            if domain_elem is not None and domain_elem.text:
                return domain_elem.text
        return "general-development"
    
    def _generate_suggestions(self, root: ET.Element, issues: List[ValidationIssue], 
                            project_root: Path) -> List[str]:
        """Generate intelligent configuration suggestions."""
        suggestions = []
        
        # Extract existing suggestions from issues
        for issue in issues:
            if issue.suggestion:
                suggestions.append(issue.suggestion)
        
        # Add contextual suggestions based on project detection
        suggestions.extend(self._analyze_project_context(project_root, root))
        
        return list(set(suggestions))  # Remove duplicates
    
    def _analyze_project_context(self, project_root: Path, root: ET.Element) -> List[str]:
        """Analyze project context and provide intelligent suggestions."""
        suggestions = []
        
        # Check for common files and suggest configurations
        if (project_root / "package.json").exists():
            suggestions.append("Detected Node.js project - consider JavaScript/TypeScript configuration")
        
        if (project_root / "requirements.txt").exists() or (project_root / "pyproject.toml").exists():
            suggestions.append("Detected Python project - consider adding pytest and black configurations")
        
        if (project_root / "Cargo.toml").exists():
            suggestions.append("Detected Rust project - consider cargo test and clippy configurations")
        
        if (project_root / "go.mod").exists():
            suggestions.append("Detected Go project - consider go test and golint configurations")
        
        if (project_root / "pom.xml").exists() or (project_root / "build.gradle").exists():
            suggestions.append("Detected Java project - consider Maven/Gradle test configurations")
        
        # Check for missing directories
        project_structure = root.find("project_structure")
        if project_structure is not None:
            src_dir = project_structure.find("source_directory")
            if src_dir is not None and src_dir.text:
                src_path = project_root / src_dir.text
                if not src_path.exists():
                    suggestions.append(f"Source directory '{src_dir.text}' does not exist - consider creating it")
        
        return suggestions
    
    def _calculate_confidence(self, issues: List[ValidationIssue], tier: ConfigTier) -> float:
        """Calculate configuration confidence score."""
        base_score = 1.0
        
        # Penalize errors more than warnings
        for issue in issues:
            if issue.level == ValidationLevel.ERROR:
                base_score -= 0.2
            elif issue.level == ValidationLevel.WARNING:
                base_score -= 0.1
            elif issue.level == ValidationLevel.INFO:
                base_score -= 0.05
        
        # Bonus for higher tier completeness
        if tier == ConfigTier.ADVANCED:
            base_score += 0.1
        elif tier == ConfigTier.STANDARD:
            base_score += 0.05
        
        return max(0.0, min(1.0, base_score))
    
    def generate_minimal_config(self, project_name: str, domain: str, language: str) -> str:
        """
        Generate a minimal valid PROJECT_CONFIG.xml.
        
        Args:
            project_name: Name of the project
            domain: Project domain from valid_values['domain']
            language: Primary programming language from valid_values['primary_language']
            
        Returns:
            XML content as string
        """
        template = f"""<?xml version="1.0" encoding="UTF-8"?>
<project_configuration version="1.0.0" tier="minimal">
  <project_info>
    <name>{project_name}</name>
    <domain>{domain}</domain>
    <description>Generated minimal configuration</description>
    <primary_language>{language}</primary_language>
  </project_info>

  <project_structure>
    <root_directory>.</root_directory>
    <source_directory>src</source_directory>
    <test_directory>tests</test_directory>
    <docs_directory>docs</docs_directory>
    <scripts_directory>scripts</scripts_directory>
  </project_structure>

  <quality_standards>
    <test_coverage>
      <threshold>90</threshold>
      <enforcement>BLOCKING</enforcement>
      <tool>auto-detect</tool>
    </test_coverage>
    <performance>
      <response_time_p95>200ms</response_time_p95>
    </performance>
    <code_quality>
      <linter>auto-detect</linter>
      <formatter>auto-detect</formatter>
    </code_quality>
  </quality_standards>

  <development_workflow>
    <commands>
      <install>auto-detect</install>
      <test>auto-detect</test>
      <lint>auto-detect</lint>
      <build>auto-detect</build>
    </commands>
    <git_workflow>
      <branch_pattern>feature/*</branch_pattern>
      <commit_style>conventional</commit_style>
    </git_workflow>
  </development_workflow>

  <framework_behavior>
    <file_creation_policy>conservative</file_creation_policy>
    <test_first_enforcement>strict</test_first_enforcement>
    <ai_temperature>
      <factual>0.2</factual>
      <analysis>0.3</analysis>
      <creative>0.7</creative>
    </ai_temperature>
  </framework_behavior>
</project_configuration>"""
        return template
    
    def print_validation_report(self, result: ValidationResult, verbose: bool = False):
        """Print a comprehensive validation report."""
        print(f"\n=== PROJECT_CONFIG.xml Validation Report ===")
        print(f"Configuration Status: {'✅ VALID' if result.is_valid else '❌ INVALID'}")
        print(f"Configuration Tier: {result.tier.value}")
        print(f"Confidence Score: {result.confidence_score:.2f}")
        print(f"Total Issues: {len(result.issues)}")
        
        if result.issues:
            print(f"\n--- Issues Found ---")
            for issue in result.issues:
                icon = {"error": "❌", "warning": "⚠️", "info": "ℹ️", "suggestion": "💡"}[issue.level.value]
                print(f"{icon} [{issue.level.value.upper()}] {issue.path}: {issue.message}")
                if issue.suggestion:
                    print(f"    💭 Suggestion: {issue.suggestion}")
                if verbose and issue.auto_fix:
                    print(f"    🔧 Auto-fix: {issue.auto_fix}")
        
        if result.suggestions:
            print(f"\n--- Intelligent Suggestions ---")
            for suggestion in result.suggestions:
                print(f"💡 {suggestion}")
        
        if verbose and result.placeholder_results:
            print(f"\n--- Placeholder Resolution Results ---")
            for placeholder, resolved in result.placeholder_results.items():
                config_key = f"{'✓' if placeholder in result.config_values else 'D'}"
                print(f"  {config_key} {placeholder}: '{resolved}'")
        
        if verbose and result.config_values:
            print(f"\n--- Configuration Summary ---")
            key_fields = [
                "project_info.name", "project_info.domain", "project_info.primary_language",
                "quality_standards.test_coverage.threshold", "project_structure.source_directory"
            ]
            for field in key_fields:
                value = result.config_values.get(field, "N/A")
                print(f"  {field}: {value}")


def main():
    """CLI interface for the unified configuration validator."""
    parser = argparse.ArgumentParser(
        description="Unified PROJECT_CONFIG.xml Validator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python project_config_validator.py                     # Validate PROJECT_CONFIG.xml in current directory
  python project_config_validator.py --project-root ../  # Validate in parent directory
  python project_config_validator.py --generate MyApp --domain web-development --language python
  python project_config_validator.py --verbose           # Detailed validation report
        """
    )
    
    parser.add_argument('--project-root', help="Project root directory (default: current directory)")
    parser.add_argument('--config-file', help="Specific PROJECT_CONFIG.xml file to validate")
    parser.add_argument('--generate', help="Generate minimal config with project name")
    parser.add_argument('--domain', help="Project domain for generation")
    parser.add_argument('--language', help="Primary language for generation")
    parser.add_argument('--output', help="Output file for generation")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    parser.add_argument('--no-placeholders', action='store_true', help="Disable placeholder testing")
    
    args = parser.parse_args()
    
    # Setup logging
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    
    try:
        validator = UnifiedProjectConfigValidator(project_root=args.project_root)
        
        if args.generate:
            # Generate minimal configuration
            if not args.domain or not args.language:
                print("ERROR: --domain and --language required for generation")
                print(f"Valid domains: {', '.join(validator.valid_values['domain'])}")
                print(f"Valid languages: {', '.join(validator.valid_values['primary_language'])}")
                return 1
            
            config_content = validator.generate_minimal_config(
                args.generate, args.domain, args.language
            )
            
            if args.output:
                with open(args.output, 'w') as f:
                    f.write(config_content)
                print(f"✅ Generated configuration saved to {args.output}")
            else:
                print(config_content)
        
        else:
            # Validate configuration
            config_path = Path(args.config_file) if args.config_file else None
            result = validator.validate(
                config_path=config_path, 
                enable_placeholder_testing=not args.no_placeholders
            )
            
            validator.print_validation_report(result, verbose=args.verbose)
            
            return 0 if result.is_valid else 1
    
    except Exception as e:
        logging.error(f"Validation failed: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())