#!/usr/bin/env python3
"""
Security Audit and API Key Rotation Implementation

Refactored version using modular security components for improved maintainability.
This script now serves as a coordinator for the various security modules.
"""

import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from security import (
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
        ApiKeyRotationManager,
        KeyRotationValidator,
        SecurityReportGenerator,
    )
except ImportError as e:
    print(f"Error importing security modules: {e}")
    print("Make sure the security package is properly installed.")
    sys.exit(1)


class SecurityAuditor:
    """Main security auditor class using modular checkers."""
    
    def __init__(self):
        self.framework_root = Path("claude_prompt_factory")
        self.rotation_manager = ApiKeyRotationManager()
        self.validator = KeyRotationValidator()
        self.report_generator = SecurityReportGenerator()
        
    def run_comprehensive_audit(self):
        """Run comprehensive security audit using modular checkers."""
        print("🔒 Running Comprehensive Security Audit...")
        print("=" * 60)
        
        # Initialize all checkers
        checkers = {
            "Sensitive Data Exposure": SensitiveDataChecker(self.framework_root),
            "Input Validation": InputValidationChecker(self.framework_root),
            "Authentication & Authorization": AuthenticationChecker(self.framework_root),
            "API Key Management": ApiKeyManagementChecker(self.framework_root),
            "Dependency Vulnerabilities": DependencyChecker(self.framework_root),
            "Configuration Security": ConfigurationSecurityChecker(self.framework_root),
            "OWASP Compliance": OWASPComplianceChecker(self.framework_root),
            "Code Injection Prevention": InjectionPreventionChecker(self.framework_root),
            "Error Handling": ErrorHandlingChecker(self.framework_root),
            "Logging & Monitoring": LoggingSecurityChecker(self.framework_root)
        }
        
        audit_results = {}
        passed_checks = 0
        
        # Run all security checks
        for check_name, checker in checkers.items():
            print(f"\n🔍 Checking: {check_name}")
            print("-" * 40)
            
            try:
                result = checker.check()
                audit_results[check_name] = result
                
                if result["passed"]:
                    print(f"✅ PASSED - Risk Level: {result['risk_level']}")
                    passed_checks += 1
                else:
                    print(f"❌ FAILED - Risk Level: {result['risk_level']}")
                    if result.get('issues'):
                        print(f"   Issues: {len(result['issues'])} found")
            except Exception as e:
                print(f"❌ ERROR running check: {e}")
                audit_results[check_name] = {
                    "passed": False,
                    "risk_level": "HIGH",
                    "issues": [f"Check failed with error: {e}"]
                }
        
        # Implement API key rotation
        print("\n🔑 Implementing API Key Rotation...")
        try:
            self.rotation_manager.implement_api_key_rotation()
        except Exception as e:
            print(f"❌ Error implementing API key rotation: {e}")
        
        # Generate security report
        try:
            self.report_generator.generate_security_report(audit_results, passed_checks, len(checkers))
        except Exception as e:
            print(f"❌ Error generating security report: {e}")
        
        # Validate security fixes
        try:
            self.validator.validate_security_fixes()
        except Exception as e:
            print(f"❌ Error validating security fixes: {e}")
        
        print("\n" + "=" * 60)
        print(f"Security Audit Complete: {passed_checks}/{len(checkers)} checks passed")
        
        return {
            "passed_checks": passed_checks,
            "total_checks": len(checkers),
            "success_rate": (passed_checks / len(checkers) * 100) if checkers else 0,
            "audit_results": audit_results
        }

    def run_quick_audit(self, check_names: list = None):
        """Run a quick audit with only specified checks."""
        if check_names is None:
            check_names = ["Sensitive Data Exposure", "API Key Management", "Code Injection Prevention"]
        
        print("🚀 Running Quick Security Audit...")
        print("=" * 60)
        
        all_checkers = {
            "Sensitive Data Exposure": SensitiveDataChecker(self.framework_root),
            "Input Validation": InputValidationChecker(self.framework_root),
            "Authentication & Authorization": AuthenticationChecker(self.framework_root),
            "API Key Management": ApiKeyManagementChecker(self.framework_root),
            "Dependency Vulnerabilities": DependencyChecker(self.framework_root),
            "Configuration Security": ConfigurationSecurityChecker(self.framework_root),
            "OWASP Compliance": OWASPComplianceChecker(self.framework_root),
            "Code Injection Prevention": InjectionPreventionChecker(self.framework_root),
            "Error Handling": ErrorHandlingChecker(self.framework_root),
            "Logging & Monitoring": LoggingSecurityChecker(self.framework_root)
        }
        
        checkers = {name: all_checkers[name] for name in check_names if name in all_checkers}
        
        audit_results = {}
        passed_checks = 0
        
        for check_name, checker in checkers.items():
            print(f"\n🔍 Checking: {check_name}")
            print("-" * 40)
            
            try:
                result = checker.check()
                audit_results[check_name] = result
                
                if result["passed"]:
                    print(f"✅ PASSED - Risk Level: {result['risk_level']}")
                    passed_checks += 1
                else:
                    print(f"❌ FAILED - Risk Level: {result['risk_level']}")
                    if result.get('issues'):
                        print(f"   Issues: {len(result['issues'])} found")
            except Exception as e:
                print(f"❌ ERROR running check: {e}")
        
        print(f"\n🎯 Quick Audit Complete: {passed_checks}/{len(checkers)} checks passed")
        return audit_results


def main():
    """Main entry point for security audit."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Run comprehensive security audit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run full comprehensive audit
  python scripts/security_audit.py
  
  # Run quick audit with key checks
  python scripts/security_audit.py --quick
  
  # Run specific checks only
  python scripts/security_audit.py --checks "Sensitive Data Exposure,API Key Management"
"""
    )
    
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Run quick audit with essential checks only"
    )
    
    parser.add_argument(
        "--checks",
        help="Comma-separated list of specific checks to run"
    )
    
    args = parser.parse_args()
    
    auditor = SecurityAuditor()
    
    try:
        if args.quick:
            auditor.run_quick_audit()
        elif args.checks:
            check_list = [check.strip() for check in args.checks.split(',')]
            auditor.run_quick_audit(check_list)
        else:
            auditor.run_comprehensive_audit()
    except KeyboardInterrupt:
        print("\n\n⚠️  Audit interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Audit failed with error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())