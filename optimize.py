#!/usr/bin/env python3
"""Framework performance optimization analyzer."""

import os
import re
import time
from pathlib import Path
from collections import defaultdict

def analyze_token_usage():
    """Analyze token usage across modules."""
    stats = defaultdict(int)
    
    for module_file in Path('.claude/modules').rglob('*.md'):
        with open(module_file, 'r') as f:
            content = f.read()
        
        stats['total_chars'] += len(content)
        stats['total_lines'] += content.count('\n')
        stats['xml_blocks'] += content.count('<')
        
        # Check for redundant patterns
        if content.count('IMPORTANT:') > 3:
            stats['verbose_modules'] += 1
    
    return stats

def analyze_module_complexity():
    """Score module complexity."""
    complexity_scores = {}
    
    for module_file in Path('.claude/modules').rglob('*.md'):
        with open(module_file, 'r') as f:
            content = f.read()
        
        score = 0
        score += content.count('<') * 2  # XML complexity
        score += content.count('```') * 3  # Code blocks
        score += len(re.findall(r'^#{1,3} ', content, re.MULTILINE))  # Headers
        
        complexity_scores[str(module_file)] = score
    
    return dict(sorted(complexity_scores.items(), key=lambda x: x[1], reverse=True)[:5])

def measure_import_time():
    """Measure module import performance."""
    start = time.time()
    
    # Simulate loading all modules
    module_count = 0
    for module_file in Path('.claude/modules').rglob('*.md'):
        with open(module_file, 'r') as f:
            _ = f.read()
        module_count += 1
    
    elapsed = time.time() - start
    return elapsed, module_count

def suggest_optimizations(stats, complexity, load_time):
    """Generate optimization suggestions."""
    suggestions = []
    
    avg_chars = stats['total_chars'] / max(stats.get('module_count', 1), 1)
    if avg_chars > 5000:
        suggestions.append("Consider splitting large modules (avg size: {:.0f} chars)".format(avg_chars))
    
    if stats['verbose_modules'] > 5:
        suggestions.append(f"Reduce verbosity in {stats['verbose_modules']} modules with excessive IMPORTANT tags")
    
    if load_time[0] > 0.5:
        suggestions.append(f"Implement lazy loading (current load time: {load_time[0]:.2f}s)")
    
    return suggestions

def main():
    """Run performance analysis."""
    print("⚡ Framework Performance Analyzer v1.0.0\n")
    
    # Analyze token usage
    stats = analyze_token_usage()
    stats['module_count'] = len(list(Path('.claude/modules').rglob('*.md')))
    
    # Analyze complexity
    complexity = analyze_module_complexity()
    
    # Measure performance
    load_time = measure_import_time()
    
    # Generate report
    print("📊 Token Usage Analysis:")
    print(f"  • Total modules: {stats['module_count']}")
    print(f"  • Total characters: {stats['total_chars']:,}")
    print(f"  • Average size: {stats['total_chars'] // max(stats['module_count'], 1):,} chars/module")
    print(f"  • XML blocks: {stats['xml_blocks']}")
    
    print("\n🔥 Most Complex Modules:")
    for module, score in complexity.items():
        print(f"  • {Path(module).name}: complexity score {score}")
    
    print(f"\n⏱️  Performance Metrics:")
    print(f"  • Module load time: {load_time[0]:.3f}s")
    print(f"  • Modules/second: {load_time[1] / max(load_time[0], 0.001):.0f}")
    
    suggestions = suggest_optimizations(stats, complexity, load_time)
    if suggestions:
        print("\n💡 Optimization Suggestions:")
        for suggestion in suggestions:
            print(f"  • {suggestion}")

if __name__ == "__main__":
    main()