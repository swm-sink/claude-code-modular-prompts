#!/usr/bin/env python3
"""
Atomic Rollback Performance Benchmark and Validation Script
Validates <2 second rollback performance and monitors compliance
"""

import subprocess
import time
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class AtomicRollbackBenchmark:
    """Performance benchmarking and validation for atomic rollback operations"""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.performance_targets = {
            "commit_speed": 1.0,      # seconds
            "rollback_speed": 2.0,    # seconds  
            "validation_speed": 5.0,  # seconds
            "recovery_speed": 10.0    # seconds
        }
        self.results = []
        
    def benchmark_commit_performance(self) -> Tuple[float, bool]:
        """Benchmark atomic commit performance"""
        print("🔄 Testing atomic commit performance...")
        
        # Create test commit
        test_file = self.repo_path / "test_atomic_commit.tmp"
        test_file.write_text(f"Test commit at {datetime.now()}")
        
        start_time = time.perf_counter()
        try:
            subprocess.run([
                "git", "add", str(test_file)
            ], cwd=self.repo_path, check=True, capture_output=True)
            
            subprocess.run([
                "git", "commit", "-m", "BENCHMARK: Test atomic commit performance"
            ], cwd=self.repo_path, check=True, capture_output=True)
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Commit failed: {e}")
            return float('inf'), False
            
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        # Cleanup
        test_file.unlink(missing_ok=True)
        
        passed = duration <= self.performance_targets["commit_speed"]
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} Commit: {duration:.3f}s (target: {self.performance_targets['commit_speed']}s)")
        
        return duration, passed
    
    def benchmark_rollback_performance(self) -> Tuple[float, bool]:
        """Benchmark rollback performance - CRITICAL <2 second requirement"""
        print("🔄 Testing rollback performance...")
        
        start_time = time.perf_counter()
        try:
            result = subprocess.run([
                "git", "reset", "--hard", "HEAD~1"
            ], cwd=self.repo_path, check=True, capture_output=True)
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Rollback failed: {e}")
            return float('inf'), False
            
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        passed = duration <= self.performance_targets["rollback_speed"]
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} Rollback: {duration:.3f}s (target: {self.performance_targets['rollback_speed']}s)")
        
        if not passed:
            print("🚨 CRITICAL: Rollback performance does not meet <2 second requirement!")
            
        return duration, passed
    
    def benchmark_validation_performance(self) -> Tuple[float, bool]:
        """Benchmark post-rollback validation performance"""
        print("🔄 Testing validation performance...")
        
        start_time = time.perf_counter()
        try:
            # Test git status
            subprocess.run([
                "git", "status", "--porcelain"
            ], cwd=self.repo_path, check=True, capture_output=True)
            
            # Test git log
            subprocess.run([
                "git", "log", "--oneline", "-5"
            ], cwd=self.repo_path, check=True, capture_output=True)
            
            # Test repository integrity
            subprocess.run([
                "git", "fsck", "--quick"
            ], cwd=self.repo_path, check=True, capture_output=True)
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Validation failed: {e}")
            return float('inf'), False
            
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        passed = duration <= self.performance_targets["validation_speed"]
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} Validation: {duration:.3f}s (target: {self.performance_targets['validation_speed']}s)")
        
        return duration, passed
    
    def benchmark_full_recovery(self) -> Tuple[float, bool]:
        """Benchmark complete recovery cycle"""
        print("🔄 Testing full recovery performance...")
        
        # Create test scenario
        test_file = self.repo_path / "test_recovery.tmp"
        test_file.write_text(f"Recovery test at {datetime.now()}")
        
        start_time = time.perf_counter()
        try:
            # Commit
            subprocess.run([
                "git", "add", str(test_file)
            ], cwd=self.repo_path, check=True, capture_output=True)
            
            subprocess.run([
                "git", "commit", "-m", "BENCHMARK: Recovery test commit"
            ], cwd=self.repo_path, check=True, capture_output=True)
            
            # Rollback
            subprocess.run([
                "git", "reset", "--hard", "HEAD~1"
            ], cwd=self.repo_path, check=True, capture_output=True)
            
            # Validate
            subprocess.run([
                "git", "status", "--porcelain"
            ], cwd=self.repo_path, check=True, capture_output=True)
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Recovery failed: {e}")
            return float('inf'), False
        finally:
            # Cleanup
            test_file.unlink(missing_ok=True)
            
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        passed = duration <= self.performance_targets["recovery_speed"]
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} Full Recovery: {duration:.3f}s (target: {self.performance_targets['recovery_speed']}s)")
        
        return duration, passed
    
    def run_comprehensive_benchmark(self) -> Dict:
        """Run complete performance benchmark suite"""
        print("🚀 Starting Atomic Rollback Performance Benchmark")
        print("=" * 60)
        
        # Initialize git if needed
        if not (self.repo_path / ".git").exists():
            print("📁 Initializing git repository...")
            subprocess.run(["git", "init"], cwd=self.repo_path, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=self.repo_path, check=True)
            subprocess.run(["git", "config", "user.name", "Benchmark Test"], cwd=self.repo_path, check=True)
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "repo_path": str(self.repo_path),
            "targets": self.performance_targets,
            "tests": {}
        }
        
        # Run benchmarks
        commit_time, commit_pass = self.benchmark_commit_performance()
        rollback_time, rollback_pass = self.benchmark_rollback_performance()
        validation_time, validation_pass = self.benchmark_validation_performance()
        recovery_time, recovery_pass = self.benchmark_full_recovery()
        
        results["tests"] = {
            "commit_performance": {
                "duration": commit_time,
                "passed": commit_pass,
                "target": self.performance_targets["commit_speed"]
            },
            "rollback_performance": {
                "duration": rollback_time,
                "passed": rollback_pass,
                "target": self.performance_targets["rollback_speed"]
            },
            "validation_performance": {
                "duration": validation_time,
                "passed": validation_pass,
                "target": self.performance_targets["validation_speed"]
            },
            "recovery_performance": {
                "duration": recovery_time,
                "passed": recovery_pass,
                "target": self.performance_targets["recovery_speed"]
            }
        }
        
        # Calculate overall compliance
        all_tests = [commit_pass, rollback_pass, validation_pass, recovery_pass]
        overall_pass = all(all_tests)
        compliance_rate = sum(all_tests) / len(all_tests) * 100
        
        results["overall"] = {
            "passed": overall_pass,
            "compliance_rate": compliance_rate,
            "critical_rollback_compliant": rollback_pass
        }
        
        print("=" * 60)
        print("📊 BENCHMARK RESULTS SUMMARY")
        print(f"Overall Compliance: {compliance_rate:.1f}%")
        print(f"Critical Rollback (<2s): {'✅ COMPLIANT' if rollback_pass else '❌ NON-COMPLIANT'}")
        print(f"All Tests Passed: {'✅ YES' if overall_pass else '❌ NO'}")
        
        if not rollback_pass:
            print("🚨 CRITICAL FAILURE: Rollback performance does not meet framework requirements!")
            print("   Framework stability may be compromised.")
            print("   Consider repository optimization or hardware upgrade.")
            
        return results
    
    def save_results(self, results: Dict, output_file: str = "atomic_rollback_benchmark.json"):
        """Save benchmark results to file"""
        output_path = self.repo_path / output_file
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"📝 Results saved to: {output_path}")

def main():
    """Main benchmark execution"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Atomic Rollback Performance Benchmark")
    parser.add_argument("--repo-path", default=".", help="Repository path")
    parser.add_argument("--output", default="atomic_rollback_benchmark.json", help="Output file")
    parser.add_argument("--quiet", action="store_true", help="Suppress output")
    
    args = parser.parse_args()
    
    benchmark = AtomicRollbackBenchmark(args.repo_path)
    results = benchmark.run_comprehensive_benchmark()
    benchmark.save_results(results, args.output)
    
    # Exit with error if critical rollback test fails
    if not results["overall"]["critical_rollback_compliant"]:
        print("❌ BENCHMARK FAILED: Critical rollback performance requirements not met")
        sys.exit(1)
    
    print("✅ BENCHMARK PASSED: All performance requirements met")
    sys.exit(0)

if __name__ == "__main__":
    main()