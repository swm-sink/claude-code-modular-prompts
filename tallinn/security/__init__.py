#!/usr/bin/env python3
"""
Security Module for Claude Code Framework

Provides comprehensive security auditing, API key management,
and rotation capabilities in a modular, reusable way.
"""

from .audit_checkers import (
    SensitiveDataChecker,
    InputValidationChecker,
    AuthenticationChecker,
    ApiKeyManagementChecker,
    DependencyChecker,
    ConfigurationSecurityChecker,
    OWASPComplianceChecker,
    InjectionPreventionChecker,
    ErrorHandlingChecker,
    LoggingSecurityChecker,
)

from .key_rotation import (
    ApiKeyRotationManager,
    KeyRotationValidator,
)

from .report_generator import (
    SecurityReportGenerator,
)

__all__ = [
    # Checkers
    'SensitiveDataChecker',
    'InputValidationChecker',
    'AuthenticationChecker',
    'ApiKeyManagementChecker',
    'DependencyChecker',
    'ConfigurationSecurityChecker',
    'OWASPComplianceChecker',
    'InjectionPreventionChecker',
    'ErrorHandlingChecker',
    'LoggingSecurityChecker',
    
    # Key Management
    'ApiKeyRotationManager',
    'KeyRotationValidator',
    
    # Reporting
    'SecurityReportGenerator',
]