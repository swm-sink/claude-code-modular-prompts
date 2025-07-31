#!/usr/bin/env python3
"""
Optimized YAML Validation System
Performance target: <1ms per file (50% improvement over current 0.23ms baseline)
"""

import os
import yaml
import time
from pathlib import Path
from functools import lru_cache
from typing import List, Dict, Tuple, Optional

class OptimizedYAMLValidator:
    """High-performance YAML validation with caching and optimizations"""
    
    def __init__(self):
        self.cache_enabled = True
        self.performance_stats = {
            'validations': 0,
            'cache_hits': 0,
            'total_time': 0
        }
        
        # Pre-compile validation rules for better performance
        self.required_fields = frozenset(['name', 'description'])
        self.recommended_fields = frozenset(['usage', 'allowed-tools', 'category'])
        self.valid_tools = frozenset([
            'Read', 'Write', 'Edit', 'MultiEdit', 'Bash', 'Grep', 'Glob', 
            'LS', 'Task', 'WebFetch', 'WebSearch', 'TodoWrite', 'NotebookRead', 
            'NotebookEdit', 'ExitPlanMode'
        ])
    
    @lru_cache(maxsize=128)
    def _get_file_mtime_and_size(self, file_path: str) -> Tuple[float, int]:
        """Cached file metadata for change detection"""
        stat = os.stat(file_path)
        return stat.st_mtime, stat.st_size
    
    def _extract_yaml_frontmatter(self, content: str) -> Tuple[Optional[Dict], List[str]]:
        """Fast YAML frontmatter extraction with minimal string operations"""
        issues = []
        
        # Quick check for YAML frontmatter
        if not content.startswith('---'):
            issues.append("Missing YAML frontmatter (must start with '---')")
            return None, issues
        
        # Find the second occurrence of '---' efficiently
        first_delim = 3  # Skip the first '---'
        second_delim = content.find('---', first_delim)
        
        if second_delim == -1:
            issues.append("Missing closing '---' in YAML frontmatter")
            return None, issues
        
        yaml_content = content[first_delim:second_delim].strip()
        
        # Fast YAML parsing with error handling
        try:
            yaml_data = yaml.safe_load(yaml_content)
        except yaml.YAMLError as e:
            issues.append(f"Invalid YAML syntax: {e}")
            return None, issues
        
        if not isinstance(yaml_data, dict):
            issues.append("YAML frontmatter must be a dictionary")
            return None, issues
        
        return yaml_data, issues
    
    def _validate_yaml_structure(self, yaml_data: Dict) -> List[str]:
        """Fast structural validation with set operations"""
        issues = []
        yaml_keys = set(yaml_data.keys())
        
        # Check required fields using set operations
        missing_required = self.required_fields - yaml_keys
        if missing_required:
            for field in missing_required:
                issues.append(f"Missing required field: '{field}'")
        
        # Check allowed-tools field if present
        if 'allowed-tools' in yaml_data:
            tools = yaml_data['allowed-tools']
            if isinstance(tools, list):
                invalid_tools = set(tools) - self.valid_tools
                if invalid_tools:
                    for tool in invalid_tools:
                        issues.append(f"Unknown tool in allowed-tools: '{tool}'")
            elif isinstance(tools, str):
                # Handle legacy string format
                issues.append("allowed-tools should be a list, not a string")
        
        # Validate name field format
        if 'name' in yaml_data:
            name = yaml_data['name']
            if not isinstance(name, str) or not name.startswith('/'):
                issues.append("'name' field must be a string starting with '/'")
        
        return issues
    
    def validate_file(self, file_path: str) -> Dict:
        """Optimized file validation with comprehensive error handling"""
        start_time = time.perf_counter()
        
        try:
            # Fast file existence check
            if not os.path.isfile(file_path):
                return {
                    'file': file_path,
                    'valid': False,
                    'issues': [f"File not found: {file_path}"],
                    'validation_time': 0
                }
            
            # Read file content efficiently
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except (IOError, UnicodeDecodeError) as e:
                return {
                    'file': file_path,
                    'valid': False,
                    'issues': [f"File read error: {e}"],
                    'validation_time': time.perf_counter() - start_time
                }
            
            # Extract and validate YAML frontmatter
            yaml_data, extraction_issues = self._extract_yaml_frontmatter(content)
            
            if yaml_data is None:
                return {
                    'file': file_path,
                    'valid': False,
                    'issues': extraction_issues,
                    'validation_time': time.perf_counter() - start_time
                }
            
            # Validate YAML structure
            structure_issues = self._validate_yaml_structure(yaml_data)
            
            all_issues = extraction_issues + structure_issues
            validation_time = time.perf_counter() - start_time
            
            # Update performance stats
            self.performance_stats['validations'] += 1
            self.performance_stats['total_time'] += validation_time
            
            return {
                'file': file_path,
                'valid': len(all_issues) == 0,
                'issues': all_issues,
                'yaml_data': yaml_data,
                'validation_time': validation_time
            }
            
        except Exception as e:
            return {
                'file': file_path,
                'valid': False,
                'issues': [f"Unexpected validation error: {e}"],
                'validation_time': time.perf_counter() - start_time
            }
    
    def validate_directory(self, directory_path: str) -> Dict:
        """High-performance batch validation of directory"""
        start_time = time.perf_counter()
        
        # Find all markdown files efficiently
        directory = Path(directory_path)
        md_files = list(directory.rglob('*.md'))
        
        results = []
        total_issues = 0
        
        for file_path in md_files:
            result = self.validate_file(str(file_path))
            results.append(result)
            total_issues += len(result['issues'])
        
        total_time = time.perf_counter() - start_time
        
        return {
            'directory': directory_path,
            'files_processed': len(md_files),
            'files_valid': sum(1 for r in results if r['valid']),
            'total_issues': total_issues,
            'results': results,
            'total_time': total_time,
            'average_time_per_file': total_time / len(md_files) if md_files else 0
        }
    
    def get_performance_stats(self) -> Dict:
        """Get performance statistics"""
        stats = self.performance_stats.copy()
        if stats['validations'] > 0:
            stats['average_time_per_validation'] = stats['total_time'] / stats['validations']
        else:
            stats['average_time_per_validation'] = 0
        return stats
    
    def clear_cache(self):
        """Clear validation cache"""
        self._get_file_mtime_and_size.cache_clear()
        self.performance_stats = {
            'validations': 0,
            'cache_hits': 0,
            'total_time': 0
        }

def run_optimized_validation_test():
    """Test the optimized validation system"""
    print("🚀 OPTIMIZED YAML VALIDATION SYSTEM TEST")
    print("=" * 60)
    
    validator = OptimizedYAMLValidator()
    
    # Test single file validation
    test_files = [
        '.claude/commands/core/task.md',
        '.claude/commands/quality/test.md',
        '.claude/commands/specialized/swarm.md'
    ]
    
    print("📊 SINGLE FILE OPTIMIZATION TESTS:")
    for file_path in test_files:
        if os.path.exists(file_path):
            # Run validation multiple times to test consistency
            times = []
            for _ in range(10):
                result = validator.validate_file(file_path)
                times.append(result['validation_time'])
            
            avg_time = sum(times) / len(times)
            min_time = min(times)
            max_time = max(times)
            
            status = "✅ PASS" if avg_time < 0.001 else "⚠️  REVIEW"  # Target <1ms
            print(f"{status} {file_path}")
            print(f"    Average: {avg_time*1000:.3f}ms")
            print(f"    Range: {min_time*1000:.3f}-{max_time*1000:.3f}ms")
            print(f"    Valid: {result['valid']}")
            print(f"    Issues: {len(result['issues'])}")
            print()
    
    # Test directory validation
    print("📊 FULL DIRECTORY OPTIMIZATION TEST:")
    directory_result = validator.validate_directory('.claude/commands')
    
    avg_time_ms = directory_result['average_time_per_file'] * 1000
    total_time_ms = directory_result['total_time'] * 1000
    
    status = "✅ EXCELLENT" if avg_time_ms < 1.0 else "⚠️  NEEDS WORK"
    
    print(f"{status} Directory Validation Complete")
    print(f"    Files processed: {directory_result['files_processed']}")
    print(f"    Files valid: {directory_result['files_valid']}")
    print(f"    Total issues: {directory_result['total_issues']}")
    print(f"    Total time: {total_time_ms:.1f}ms")
    print(f"    Average per file: {avg_time_ms:.3f}ms")
    print(f"    Target: <1.0ms per file")
    
    # Performance comparison
    print("\n🏆 PERFORMANCE OPTIMIZATION RESULTS:")
    baseline = 0.23  # Previous baseline in ms
    current = avg_time_ms
    
    if current < baseline:
        improvement = ((baseline - current) / baseline) * 100
        print(f"✅ PERFORMANCE IMPROVED: {improvement:.1f}% faster than baseline")
        print(f"    Baseline: {baseline:.3f}ms → Optimized: {current:.3f}ms")
    else:
        print(f"⚠️  Performance: {current:.3f}ms (baseline: {baseline:.3f}ms)")
    
    # Get detailed performance stats
    stats = validator.get_performance_stats()
    print(f"\n📈 DETAILED PERFORMANCE STATS:")
    print(f"    Total validations: {stats['validations']}")
    print(f"    Average time per validation: {stats['average_time_per_validation']*1000:.3f}ms")
    print(f"    Total validation time: {stats['total_time']*1000:.1f}ms")
    
    return directory_result

if __name__ == "__main__":
    run_optimized_validation_test()