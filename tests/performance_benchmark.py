#!/usr/bin/env python3
"""Performance benchmark for framework operations."""

import time
import os
import sys
from pathlib import Path
from statistics import mean, stdev

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def benchmark_module_loading():
    """Benchmark module loading performance."""
    module_dir = project_root / ".claude" / "modules"
    times = []
    
    for _ in range(10):
        start = time.perf_counter()
        
        # Simulate module loading
        module_files = list(module_dir.rglob("*.md"))
        for module_file in module_files[:5]:  # Load first 5 modules
            content = module_file.read_text()
            # Simulate parsing
            _ = len(content.split('\n'))
        
        end = time.perf_counter()
        times.append((end - start) * 1000)  # Convert to ms
    
    return times


def benchmark_command_loading():
    """Benchmark command loading performance."""
    command_dir = project_root / ".claude" / "commands"
    times = []
    
    for _ in range(10):
        start = time.perf_counter()
        
        # Simulate command loading
        command_files = list(command_dir.glob("*.md"))
        for command_file in command_files[:6]:  # Load core commands
            content = command_file.read_text()
            # Simulate delegation parsing
            if "delegation target=" in content:
                _ = content.index("delegation target=")
        
        end = time.perf_counter()
        times.append((end - start) * 1000)  # Convert to ms
    
    return times


def benchmark_dependency_resolution():
    """Benchmark dependency resolution performance."""
    times = []
    
    for _ in range(10):
        start = time.perf_counter()
        
        # Simulate dependency resolution
        claude_md = project_root / "CLAUDE.md"
        content = claude_md.read_text()
        
        # Find module references
        module_refs = [line for line in content.split('\n') if 'modules/' in line]
        command_refs = [line for line in content.split('\n') if 'commands/' in line]
        
        # Verify references exist
        for ref in module_refs[:5]:
            if 'module=' in ref:
                module_name = ref.split('module="')[1].split('"')[0]
                module_path = project_root / ".claude" / module_name
                _ = module_path.exists()
        
        end = time.perf_counter()
        times.append((end - start) * 1000)  # Convert to ms
    
    return times


def benchmark_full_framework_load():
    """Benchmark full framework initialization."""
    times = []
    
    for _ in range(10):
        start = time.perf_counter()
        
        # Load CLAUDE.md
        claude_md = project_root / "CLAUDE.md"
        claude_content = claude_md.read_text()
        
        # Load core commands
        command_dir = project_root / ".claude" / "commands"
        core_commands = ["auto.md", "task.md", "feature.md", "swarm.md", "query.md", "session.md"]
        for cmd in core_commands:
            cmd_path = command_dir / cmd
            if cmd_path.exists():
                _ = cmd_path.read_text()
        
        # Load settings
        settings_path = project_root / ".claude" / "settings" / "settings.json"
        if settings_path.exists():
            _ = settings_path.read_text()
        
        end = time.perf_counter()
        times.append((end - start) * 1000)  # Convert to ms
    
    return times


def print_results(name, times):
    """Print benchmark results."""
    avg = mean(times)
    std = stdev(times) if len(times) > 1 else 0
    min_time = min(times)
    max_time = max(times)
    p95 = sorted(times)[int(len(times) * 0.95) - 1]
    
    print(f"\n{name}:")
    print(f"  Average: {avg:.2f}ms")
    print(f"  Std Dev: {std:.2f}ms")
    print(f"  Min: {min_time:.2f}ms")
    print(f"  Max: {max_time:.2f}ms")
    print(f"  P95: {p95:.2f}ms")
    
    if p95 > 200:
        print(f"  ⚠️  WARNING: P95 exceeds 200ms target!")
    else:
        print(f"  ✅ PASS: P95 within 200ms target")
    
    return p95


def main():
    """Run all benchmarks."""
    print("🚀 Framework Performance Benchmarks")
    print("=" * 50)
    
    all_p95s = []
    
    # Run benchmarks
    module_times = benchmark_module_loading()
    all_p95s.append(print_results("Module Loading", module_times))
    
    command_times = benchmark_command_loading()
    all_p95s.append(print_results("Command Loading", command_times))
    
    dep_times = benchmark_dependency_resolution()
    all_p95s.append(print_results("Dependency Resolution", dep_times))
    
    full_times = benchmark_full_framework_load()
    all_p95s.append(print_results("Full Framework Load", full_times))
    
    # Overall summary
    print("\n" + "=" * 50)
    print("📊 Overall Summary:")
    print(f"  Max P95 across all operations: {max(all_p95s):.2f}ms")
    
    if max(all_p95s) <= 200:
        print("  ✅ All operations within 200ms p95 target!")
        return 0
    else:
        print("  ❌ Some operations exceed 200ms p95 target")
        return 1


if __name__ == "__main__":
    sys.exit(main())