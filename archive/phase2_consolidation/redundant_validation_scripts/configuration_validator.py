#!/usr/bin/env python3
"""
Configuration Validation System for PROJECT_CONFIG
Provides comprehensive validation with intelligent guidance and tier-aware checks

TASK 5: Design configuration validation system
Author: Agent 4 - Configuration System Simplification
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import re
import json


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


class ConfigurationValidator:
    """Main configuration validation engine with tier-aware validation"""
    
    def __init__(self):
        self.domain_validators = {
            "web-development": WebDevelopmentValidator(),
            "data-analytics": DataAnalyticsValidator(),
            "mobile-engineering": MobileEngineeringValidator(),
            "platform-engineering": PlatformEngineeringValidator()
        }
    
    def validate(self, config_path: Path, project_root: Optional[Path] = None) -> ValidationResult:
        """Validate a PROJECT_CONFIG file with comprehensive checks"""
        try:
            tree = ET.parse(config_path)
            root = tree.getroot()
        except ET.ParseError as e:
            return ValidationResult(
                is_valid=False,
                issues=[ValidationIssue(
                    level=ValidationLevel.ERROR,
                    message=f"XML parsing error: {e}",
                    path="root"
                )],
                suggestions=[],
                tier=ConfigTier.MINIMAL,
                confidence_score=0.0
            )
        
        # Determine configuration tier
        tier = self._determine_tier(root)
        
        # Run tier-appropriate validations
        issues = []
        suggestions = []
        
        # Core validation (all tiers)
        issues.extend(self._validate_core_structure(root))
        issues.extend(self._validate_project_info(root))
        
        if tier in [ConfigTier.STANDARD, ConfigTier.ADVANCED]:
            issues.extend(self._validate_quality_standards(root))
            issues.extend(self._validate_development_workflow(root))
        
        if tier == ConfigTier.ADVANCED:
            issues.extend(self._validate_advanced_features(root))
            issues.extend(self._validate_security_requirements(root))
            issues.extend(self._validate_integrations(root))
        
        # Domain-specific validation
        domain = self._get_domain(root)
        if domain in self.domain_validators:
            domain_issues = self.domain_validators[domain].validate(root, tier)
            issues.extend(domain_issues)
        
        # Generate suggestions
        suggestions = self._generate_suggestions(root, issues, project_root)
        
        # Calculate confidence score
        confidence_score = self._calculate_confidence(issues, tier)
        
        is_valid = not any(issue.level == ValidationLevel.ERROR for issue in issues)
        
        return ValidationResult(
            is_valid=is_valid,
            issues=issues,
            suggestions=suggestions,
            tier=tier,
            confidence_score=confidence_score
        )
    
    def _determine_tier(self, root: ET.Element) -> ConfigTier:
        """Determine the configuration tier based on complexity"""
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
        
        if sections <= 6 and not custom_personas and not integrations:
            return ConfigTier.MINIMAL
        elif sections <= 10 and not custom_personas:
            return ConfigTier.STANDARD
        else:
            return ConfigTier.ADVANCED
    
    def _validate_core_structure(self, root: ET.Element) -> List[ValidationIssue]:
        """Validate core XML structure"""
        issues = []
        
        # Check version
        version = root.get("version")
        if not version:
            issues.append(ValidationIssue(
                level=ValidationLevel.WARNING,
                message="Missing version attribute",
                path="root",
                suggestion="Add version='1.0.0' to project_configuration element"
            ))
        elif version != "1.0.0":
            issues.append(ValidationIssue(
                level=ValidationLevel.INFO,
                message=f"Version {version} may not be compatible with current framework",
                path="root"
            ))
        
        # Check required sections
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
        """Validate project_info section"""
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
            valid_languages = [
                "python", "javascript", "typescript", "java", "go", "rust", 
                "c#", "php", "ruby", "swift", "kotlin", "dart", "c++", "c"
            ]
            if language_elem.text.lower() not in valid_languages:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    message=f"Unusual primary language: {language_elem.text}",
                    path="project_info.primary_language",
                    suggestion=f"Consider one of: {', '.join(valid_languages[:5])}, ..."
                ))
        
        # Validate domain
        domain_elem = project_info.find("domain")
        if domain_elem is not None and domain_elem.text:
            valid_domains = [
                "web-development", "mobile-engineering", "data-analytics", 
                "platform-engineering", "game-development", "fintech", 
                "healthcare", "e-commerce", "general-development"
            ]
            if domain_elem.text not in valid_domains:
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    message=f"Unknown domain: {domain_elem.text}",
                    path="project_info.domain",
                    suggestion=f"Consider one of: {', '.join(valid_domains[:3])}, ..."
                ))
        
        return issues
    
    def _validate_quality_standards(self, root: ET.Element) -> List[ValidationIssue]:
        """Validate quality_standards section"""
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
            
            enforcement_elem = test_coverage.find("enforcement")
            if enforcement_elem is not None:
                valid_enforcement = ["BLOCKING", "CONDITIONAL", "ADVISORY"]
                if enforcement_elem.text not in valid_enforcement:
                    issues.append(ValidationIssue(
                        level=ValidationLevel.ERROR,
                        message=f"Invalid enforcement: {enforcement_elem.text}",
                        path="quality_standards.test_coverage.enforcement",
                        suggestion=f"Must be one of: {', '.join(valid_enforcement)}"
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
        """Validate development_workflow section"""
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
        """Validate advanced configuration features"""
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
        """Validate security requirements"""
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
        """Validate integration configurations"""
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
    
    def _get_domain(self, root: ET.Element) -> str:
        """Extract domain from configuration"""
        project_info = root.find("project_info")
        if project_info is not None:
            domain_elem = project_info.find("domain")
            if domain_elem is not None and domain_elem.text:
                return domain_elem.text
        return "general-development"
    
    def _generate_suggestions(self, root: ET.Element, issues: List[ValidationIssue], 
                            project_root: Optional[Path]) -> List[str]:
        """Generate intelligent configuration suggestions"""
        suggestions = []
        
        # Extract existing suggestions from issues
        for issue in issues:
            if issue.suggestion:
                suggestions.append(issue.suggestion)
        
        # Add contextual suggestions based on project detection
        if project_root:
            suggestions.extend(self._analyze_project_context(project_root, root))
        
        return list(set(suggestions))  # Remove duplicates
    
    def _analyze_project_context(self, project_root: Path, root: ET.Element) -> List[str]:
        """Analyze project context and provide suggestions"""
        suggestions = []
        
        # Check for common files and suggest configurations
        if (project_root / "package.json").exists():
            suggestions.append("Detected Node.js project - consider JavaScript/TypeScript configuration")
        
        if (project_root / "requirements.txt").exists():
            suggestions.append("Detected Python project - consider adding pytest and black configurations")
        
        if (project_root / "Cargo.toml").exists():
            suggestions.append("Detected Rust project - consider cargo test and clippy configurations")
        
        if (project_root / "go.mod").exists():
            suggestions.append("Detected Go project - consider go test and golint configurations")
        
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
        """Calculate configuration confidence score"""
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


class DomainValidator:
    """Base class for domain-specific validators"""
    
    def validate(self, root: ET.Element, tier: ConfigTier) -> List[ValidationIssue]:
        """Validate domain-specific requirements"""
        return []


class WebDevelopmentValidator(DomainValidator):
    """Validator for web development projects"""
    
    def validate(self, root: ET.Element, tier: ConfigTier) -> List[ValidationIssue]:
        issues = []
        
        # Check for web-specific quality standards
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
        
        # Check for domain-specific rules
        domain_rules = root.find("domain_specific_rules")
        if domain_rules is not None:
            rule_texts = [rule.text for rule in domain_rules.findall("rule") if rule.text]
            
            recommended_rules = [
                "responsive design", "accessibility", "performance", "security"
            ]
            
            for recommended in recommended_rules:
                if not any(recommended.lower() in rule.lower() for rule in rule_texts):
                    issues.append(ValidationIssue(
                        level=ValidationLevel.SUGGESTION,
                        message=f"Consider adding {recommended} rule for web development",
                        path="domain_specific_rules",
                        suggestion=f"Add rule about {recommended} best practices"
                    ))
        
        return issues


class DataAnalyticsValidator(DomainValidator):
    """Validator for data analytics projects"""
    
    def validate(self, root: ET.Element, tier: ConfigTier) -> List[ValidationIssue]:
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
        
        # Check for appropriate coverage thresholds
        quality_standards = root.find("quality_standards")
        if quality_standards is not None:
            test_coverage = quality_standards.find("test_coverage")
            if test_coverage is not None:
                threshold = test_coverage.find("threshold")
                if threshold is not None:
                    try:
                        threshold_val = int(threshold.text)
                        if threshold_val > 85:
                            issues.append(ValidationIssue(
                                level=ValidationLevel.INFO,
                                message=f"High coverage threshold ({threshold_val}%) for data analytics",
                                path="quality_standards.test_coverage.threshold",
                                suggestion="Data science projects often use 70-80% coverage due to experimental nature"
                            ))
                    except ValueError:
                        pass
        
        return issues


class MobileEngineeringValidator(DomainValidator):
    """Validator for mobile engineering projects"""
    
    def validate(self, root: ET.Element, tier: ConfigTier) -> List[ValidationIssue]:
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


class PlatformEngineeringValidator(DomainValidator):
    """Validator for platform engineering projects"""
    
    def validate(self, root: ET.Element, tier: ConfigTier) -> List[ValidationIssue]:
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


def main():
    """Example usage of the Configuration Validator"""
    validator = ConfigurationValidator()
    
    # Example validation
    config_path = Path("PROJECT_CONFIG.xml")
    if config_path.exists():
        result = validator.validate(config_path, Path.cwd())
        
        print(f"Validation Result: {'PASSED' if result.is_valid else 'FAILED'}")
        print(f"Configuration Tier: {result.tier.value}")
        print(f"Confidence Score: {result.confidence_score:.2f}")
        
        if result.issues:
            print("\nIssues Found:")
            for issue in result.issues:
                print(f"  {issue.level.value.upper()}: {issue.message}")
                if issue.suggestion:
                    print(f"    Suggestion: {issue.suggestion}")
        
        if result.suggestions:
            print("\nSuggestions:")
            for suggestion in result.suggestions:
                print(f"  - {suggestion}")
    else:
        print("No PROJECT_CONFIG.xml found in current directory")


if __name__ == "__main__":
    main()