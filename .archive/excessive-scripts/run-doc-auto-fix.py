#!/usr/bin/env python3
"""
Run Documentation Auto-Fix (Live Mode)
Apply automatic fixes to sync documentation with implementation
"""

import sys
import os
sys.path.append('.')

# Import the validator class directly
# SECURITY: Replaced exec() with safer import pattern
import sys
sys.path.append('.')
try:
    import documentation_sync_validator
    # Use module functions instead of exec
except ImportError:
    print("Warning: documentation-sync-validator module not available")

def main():
    print("🔧 DOCUMENTATION AUTO-FIX TOOL")
    print("=" * 40)
    print("This will automatically update documentation to match implementation.")
    print("Files that will be updated: README.md, CLAUDE.md")
    print()
    
    validator = DocumentationSyncValidator()
    
    # Run the live auto-fix
    result = validator.run_live_auto_fix()
    
    # Run validation again to check results
    print(f"\n🔍 POST-FIX VALIDATION")
    print("=" * 30)
    
    sync_report = validator.generate_sync_report()
    
    print(f"\n🎯 FINAL RESULTS:")
    print(f"    Documentation accuracy: {sync_report['overall_accuracy']:.1f}%")
    print(f"    Remaining issues: {sync_report['total_issues']}")
    
    if sync_report['overall_accuracy'] >= 90.0:
        print(f"\n🏆 SUCCESS: Documentation sync achieved!")
    else:
        print(f"\n⚠️  Additional work needed for complete sync")
    
    return sync_report

if __name__ == "__main__":
    main()