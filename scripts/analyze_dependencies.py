#!/usr/bin/env python3
"""Unified dependency analysis tool - replaces multiple import/dependency scripts.

This tool consolidates functionality from:
- analyze_imports.py
- analyze_imports_detailed.py
- analyze_dependency_conflicts.py
- check_dependencies.py
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

# Add the parent directory to the path so we can import from lib
sys.path.insert(0, str(Path(__file__).parent))

from lib.import_analysis import analyze_project_dependencies, ImportAnalyzer


def print_summary(analysis_result):
    """Print a formatted summary of the analysis."""
    summary = analysis_result['summary']
    
    print(f"\n📊 Dependency Analysis Summary")
    print(f"{'='*60}")
    print(f"Total Python files analyzed: {summary['total_files']}")
    print(f"External dependencies found: {summary['external_dependencies']}")
    print(f"Total unique imports: {summary['total_imports']}")
    print(f"Files with external deps: {summary['files_with_external_deps']}")
    print(f"Errors encountered: {summary['errors']}")
    print(f"Potential conflicts: {summary['conflicts']}")


def print_external_deps(analysis_result):
    """Print external dependencies with files that use them."""
    external_deps = analysis_result['external_deps']
    
    if external_deps:
        print(f"\n📦 External Dependencies (require pip install):")
        print(f"{'-'*60}")
        for dep, files in sorted(external_deps.items()):
            print(f"\n{dep}:")
            for file in sorted(files):
                print(f"  - {file}")


def print_conflicts(analysis_result):
    """Print potential dependency conflicts."""
    conflicts = analysis_result['conflicts']
    
    if conflicts:
        print(f"\n⚠️  Potential Conflicts Detected:")
        print(f"{'-'*60}")
        for module, files in conflicts:
            print(f"\n{module} imported in multiple contexts:")
            for file in files:
                context = "test" if "test" in file else "production"
                print(f"  - {file} ({context})")


def write_requirements(analysis_result, output_file='requirements.txt'):
    """Write requirements.txt file."""
    requirements = analysis_result['requirements']
    
    if requirements:
        with open(output_file, 'w') as f:
            f.write("# Auto-generated requirements from dependency analysis\n")
            f.write(f"# Generated on: {datetime.now().strftime('%Y-%m-%d')}\n\n")
            for req in requirements.values():
                f.write(f"{req}\n")
        
        print(f"\n📄 Requirements file written to {output_file}")
        print(f"   {len(requirements)} dependencies listed")


def analyze_single_file(filepath):
    """Analyze a single Python file for imports."""
    analyzer = ImportAnalyzer(detailed_mode=True)
    analyzer.analyze_file(filepath)
    
    print(f"\n📄 Import Analysis for {filepath}")
    print(f"{'-'*60}")
    
    imports = analyzer.imports_by_file[filepath]
    
    if imports['stdlib']:
        print(f"\n📚 Standard Library Imports ({len(imports['stdlib'])}):")
        for imp in sorted(imports['stdlib']):
            print(f"  - {imp}")
    
    if imports['external']:
        print(f"\n📦 External Dependencies ({len(imports['external'])}):")
        for imp in sorted(imports['external']):
            print(f"  - {imp}")
    
    if imports['local']:
        print(f"\n🏠 Local Imports ({len(imports['local'])}):")
        for imp in sorted(imports['local']):
            print(f"  - {imp}")
    
    if imports['relative']:
        print(f"\n🔗 Relative Imports ({len(imports['relative'])}):")
        for imp in sorted(imports['relative']):
            print(f"  - {imp}")
    
    if analyzer.errors:
        print(f"\n❌ Errors:")
        for error in analyzer.errors:
            print(f"  - {error}")


def main():
    """Main entry point for the unified dependency analyzer."""
    parser = argparse.ArgumentParser(
        description="Unified dependency analysis tool for Python projects"
    )
    parser.add_argument(
        '--mode', 
        choices=['summary', 'detailed', 'conflicts', 'single-file'],
        default='summary',
        help='Analysis mode'
    )
    parser.add_argument(
        '--file',
        help='Single file to analyze (for single-file mode)'
    )
    parser.add_argument(
        '--output',
        help='Output file for results (JSON format)'
    )
    parser.add_argument(
        '--requirements',
        action='store_true',
        help='Generate requirements.txt file'
    )
    parser.add_argument(
        '--dirs',
        nargs='+',
        default=['./scripts', './.claude/scripts'],
        help='Directories to analyze'
    )
    
    args = parser.parse_args()
    
    # Handle single-file mode
    if args.mode == 'single-file':
        if not args.file:
            print("Error: --file required for single-file mode")
            sys.exit(1)
        analyze_single_file(args.file)
        return
    
    # Analyze project dependencies
    detailed = args.mode == 'detailed'
    analysis_result = analyze_project_dependencies(args.dirs, detailed=detailed)
    
    # Display results based on mode
    if args.mode == 'summary':
        print_summary(analysis_result)
        print_external_deps(analysis_result)
    elif args.mode == 'detailed':
        print_summary(analysis_result)
        print_external_deps(analysis_result)
        print_conflicts(analysis_result)
        if analysis_result['errors']:
            print(f"\n❌ Errors encountered:")
            for error in analysis_result['errors']:
                print(f"  - {error}")
    elif args.mode == 'conflicts':
        print_conflicts(analysis_result)
    
    # Generate requirements.txt if requested
    if args.requirements:
        write_requirements(analysis_result)
    
    # Save detailed output if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(analysis_result, f, indent=2, default=str)
        print(f"\n📊 Detailed results saved to {args.output}")
    
    # Return appropriate exit code
    if analysis_result['errors'] or analysis_result['conflicts']:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()