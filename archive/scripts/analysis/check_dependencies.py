#!/usr/bin/env python3
"""Check which dependencies are installed and which are missing."""

import subprocess
import sys
import json
from pathlib import Path

def check_package(package_name):
    """Check if a package is installed and get its version."""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'show', package_name],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            # Parse version from output
            for line in result.stdout.split('\n'):
                if line.startswith('Version:'):
                    version = line.split(':', 1)[1].strip()
                    return True, version
        return False, None
    except Exception as e:
        return False, str(e)

def main():
    # Required packages based on our analysis
    required_packages = {
        'psutil': '>=5.9.0',
        'defusedxml': '>=0.7.1', 
        'schedule': '>=1.2.0',
        'numpy': '>=1.21.0',
        'pandas': '>=1.5.0',
        'requests': '>=2.28.0'
    }
    
    installed = {}
    missing = {}
    
    print("🔍 Checking Python package dependencies...")
    print("=" * 60)
    
    for package, required_version in required_packages.items():
        is_installed, version = check_package(package)
        if is_installed:
            installed[package] = version
            print(f"✅ {package:15} {version:10} (required: {required_version})")
        else:
            missing[package] = required_version
            print(f"❌ {package:15} NOT INSTALLED (required: {required_version})")
    
    print("\n📊 Summary:")
    print(f"  Installed: {len(installed)}/{len(required_packages)}")
    print(f"  Missing: {len(missing)}/{len(required_packages)}")
    
    if missing:
        print("\n⚠️  Missing packages:")
        for pkg, version in missing.items():
            print(f"  - {pkg} {version}")
        
        print("\n💡 To install missing packages, run:")
        print("  pip install -r requirements_clean.txt")
        
        # Create minimal requirements for missing packages only
        with open('requirements_missing.txt', 'w') as f:
            f.write("# Missing dependencies only\n")
            f.write("# Generated on: 2025-07-13\n\n")
            for pkg, version in sorted(missing.items()):
                f.write(f"{pkg}{version}\n")
        
        print("\n  Or install only missing packages:")
        print("  pip install -r requirements_missing.txt")
    else:
        print("\n✅ All required packages are installed!")
    
    # Save status report
    status = {
        'timestamp': '2025-07-13',
        'total_required': len(required_packages),
        'installed': installed,
        'missing': missing,
        'all_installed': len(missing) == 0
    }
    
    with open('dependency_status.json', 'w') as f:
        json.dump(status, f, indent=2)
    
    print("\n📄 Dependency status saved to dependency_status.json")
    
    return len(missing) == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)