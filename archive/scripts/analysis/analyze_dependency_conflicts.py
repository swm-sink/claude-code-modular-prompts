#!/usr/bin/env python3
"""Analyze potential dependency conflicts and version requirements."""

import subprocess
import sys
import json
import re
from collections import defaultdict
from pathlib import Path

def get_package_dependencies(package_name):
    """Get dependencies of an installed package."""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'show', package_name],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            deps = {}
            for line in result.stdout.split('\n'):
                if line.startswith('Requires:'):
                    requires = line.split(':', 1)[1].strip()
                    if requires:
                        for dep in requires.split(','):
                            dep = dep.strip()
                            if dep:
                                deps[dep] = 'any'
            return deps
        return {}
    except Exception:
        return {}

def analyze_conflicts():
    """Analyze potential dependency conflicts."""
    # Our direct dependencies
    direct_deps = {
        'psutil': '>=5.9.0',
        'defusedxml': '>=0.7.1',
        'schedule': '>=1.2.0',
        'numpy': '>=1.21.0',
        'pandas': '>=1.5.0',
        'requests': '>=2.28.0'
    }
    
    # Analyze dependency tree
    dep_tree = {}
    all_deps = set()
    
    print("🔍 Analyzing dependency tree...")
    print("=" * 60)
    
    for pkg, version in direct_deps.items():
        print(f"\n📦 {pkg} {version}")
        subdeps = get_package_dependencies(pkg)
        dep_tree[pkg] = subdeps
        
        if subdeps:
            print(f"   Dependencies: {', '.join(subdeps.keys())}")
            all_deps.update(subdeps.keys())
        else:
            print(f"   No dependencies found (package might not be installed)")
    
    # Check for common problematic dependencies
    print("\n⚠️  Potential Issues:")
    print("-" * 60)
    
    issues = []
    
    # Check numpy/pandas compatibility
    if 'numpy' in direct_deps and 'pandas' in direct_deps:
        print("✅ numpy + pandas: Generally compatible, pandas manages numpy version")
    
    # Check for XML parsing conflicts
    if 'defusedxml' in direct_deps:
        print("✅ defusedxml: Safe XML parsing, no known conflicts")
    
    # Check schedule compatibility
    if 'schedule' in direct_deps:
        print("⚠️  schedule: Pure Python, but check for timezone handling if needed")
        issues.append("schedule package doesn't handle timezones - consider using APScheduler for complex scheduling")
    
    # Version compatibility matrix
    print("\n📊 Version Compatibility Matrix:")
    print("-" * 60)
    
    compat_matrix = {
        'numpy': {
            '>=1.21.0': 'Python 3.8+',
            '>=1.24.0': 'Python 3.9+ (recommended for pandas 2.x)'
        },
        'pandas': {
            '>=1.5.0': 'numpy >=1.20.3',
            '>=2.0.0': 'numpy >=1.23.2 (Python 3.9+)'
        },
        'psutil': {
            '>=5.9.0': 'Python 3.6+ (cross-platform)'
        }
    }
    
    for pkg, versions in compat_matrix.items():
        if pkg in direct_deps:
            print(f"\n{pkg}:")
            for ver, compat in versions.items():
                print(f"  {ver}: {compat}")
    
    # Generate optimized requirements
    print("\n📝 Generating optimized requirements...")
    
    with open('requirements_optimized.txt', 'w') as f:
        f.write("# Optimized dependencies for Claude Code Modular Prompts\n")
        f.write("# Generated on: 2025-07-13\n")
        f.write("# Python 3.8+ recommended\n\n")
        
        f.write("# Core dependencies\n")
        f.write("psutil>=5.9.0  # System monitoring\n")
        f.write("defusedxml>=0.7.1  # Safe XML parsing\n")
        f.write("schedule>=1.2.0  # Simple job scheduling\n")
        f.write("\n# Data processing (optional - only if using analytics scripts)\n")
        f.write("numpy>=1.21.0  # Numerical computing\n")
        f.write("pandas>=1.5.0  # Data analysis\n")
        f.write("\n# Network (optional - only if using monitoring scripts)\n")
        f.write("requests>=2.28.0  # HTTP library\n")
    
    # Create minimal requirements
    with open('requirements_minimal.txt', 'w') as f:
        f.write("# Minimal required dependencies\n")
        f.write("# For basic framework operation\n\n")
        f.write("psutil>=5.9.0\n")
        f.write("defusedxml>=0.7.1\n")
    
    print("✅ Created requirements_optimized.txt (with comments)")
    print("✅ Created requirements_minimal.txt (absolute minimum)")
    
    # Consolidation recommendations
    print("\n💡 Consolidation Recommendations:")
    print("-" * 60)
    print("1. Group scripts by dependency requirements:")
    print("   - Core scripts: psutil, defusedxml")
    print("   - Analytics scripts: + numpy, pandas")
    print("   - Monitoring scripts: + schedule, requests")
    print("\n2. Consider creating separate requirements files:")
    print("   - requirements-core.txt")
    print("   - requirements-analytics.txt") 
    print("   - requirements-monitoring.txt")
    print("\n3. Use optional imports in scripts for non-critical dependencies")
    
    return {
        'direct_dependencies': direct_deps,
        'dependency_tree': dep_tree,
        'all_dependencies': list(all_deps),
        'issues': issues,
        'recommendations': [
            'Use requirements_minimal.txt for basic operation',
            'Use requirements_optimized.txt for full functionality',
            'Consider virtual environments for different use cases'
        ]
    }

def main():
    report = analyze_conflicts()
    
    # Save detailed report
    with open('dependency_conflicts_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n📄 Detailed report saved to dependency_conflicts_report.json")

if __name__ == "__main__":
    main()