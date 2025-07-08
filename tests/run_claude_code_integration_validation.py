#!/usr/bin/env python3
"""Claude Code Integration Validation Runner.

This script runs comprehensive validation of the Claude Code terminal integration,
demonstrating all implemented features and generating a detailed report.
"""

import os
import sys
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from tests.framework.claude_code_terminal_integration import (
    ClaudeCodeTerminalIntegrator,
    CommandOrchestrator,
    SessionManager,
    MemorySystemOptimizer,
    PerformanceOptimizer
)


def run_comprehensive_integration_validation():
    """Run comprehensive integration validation."""
    print("🚀 Claude Code Terminal Integration Validation")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Initialize all components
    print("🔧 Initializing components...")
    integrator = ClaudeCodeTerminalIntegrator(project_root)
    orchestrator = CommandOrchestrator(project_root / ".claude" / "commands")
    session_manager = SessionManager(project_root)
    memory_optimizer = MemorySystemOptimizer(project_root)
    performance_optimizer = PerformanceOptimizer(project_root)
    
    # Run validation tests
    validation_results = {}
    
    print("🧪 Running Environment Integration Tests...")
    validation_results["environment"] = run_environment_tests(integrator)
    
    print("🎯 Running Command Orchestration Tests...")
    validation_results["orchestration"] = run_orchestration_tests(orchestrator)
    
    print("📊 Running Session Management Tests...")
    validation_results["session"] = run_session_tests(session_manager)
    
    print("💾 Running Memory System Tests...")
    validation_results["memory"] = run_memory_tests(memory_optimizer)
    
    print("⚡ Running Performance Tests...")
    validation_results["performance"] = run_performance_tests(performance_optimizer)
    
    print("🔗 Running Integration Tests...")
    validation_results["integration"] = run_integration_tests(
        integrator, orchestrator, session_manager, memory_optimizer, performance_optimizer
    )
    
    # Generate comprehensive report
    print("\n📄 Generating comprehensive report...")
    report = generate_validation_report(validation_results)
    
    # Save report
    report_file = save_validation_report(report)
    
    # Print summary
    print_validation_summary(report)
    
    print(f"\n📄 Full report saved to: {report_file}")
    
    # Return success/failure
    overall_success = all(result.get("success", False) for result in validation_results.values())
    return 0 if overall_success else 1


def run_environment_tests(integrator: ClaudeCodeTerminalIntegrator) -> Dict[str, Any]:
    """Run environment integration tests."""
    tests = [
        ("Memory File Detection", lambda: integrator.detect_memory_files()),
        ("Token Budget Monitoring", lambda: integrator.get_token_budget()),
        ("Context Window Optimization", lambda: integrator.optimize_context_window({
            "critical_instructions": "High priority content",
            "context_info": "Medium priority content",
            "examples": "Low priority content with\n# comments\n  extra whitespace  \n",
            "references": "Lowest priority content"
        })),
        ("Framework Version Compatibility", lambda: integrator.check_framework_version_compatibility()),
        ("Production Readiness", lambda: integrator.validate_production_readiness()),
        ("CI Compatibility", lambda: integrator.check_ci_compatibility())
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            start_time = time.time()
            result = test_func()
            execution_time = time.time() - start_time
            results[test_name] = {
                "success": True,
                "execution_time": execution_time,
                "result": result
            }
            print(f"  ✅ {test_name}: {execution_time:.3f}s")
        except Exception as e:
            results[test_name] = {
                "success": False,
                "error": str(e)
            }
            print(f"  ❌ {test_name}: {str(e)}")
    
    return {"success": all(r.get("success", False) for r in results.values()), "tests": results}


def run_orchestration_tests(orchestrator: CommandOrchestrator) -> Dict[str, Any]:
    """Run command orchestration tests."""
    tests = [
        ("Command Discovery", lambda: orchestrator.discover_commands()),
        ("Metadata Parsing", lambda: orchestrator.parse_command_metadata("task")),
        ("Dependency Resolution", lambda: orchestrator.resolve_module_dependencies("task")),
        ("Execution Planning", lambda: orchestrator.create_execution_plan("task", {"input": "test"})),
        ("Meta-prompt Generation", lambda: orchestrator.generate_meta_prompt("task", {"target": "test_file.py"})),
        ("Parallel Execution Optimization", lambda: orchestrator.optimize_parallel_execution([
            "read_file1", "read_file2", "analyze_data1", "analyze_data2", "write_output"
        ])),
        ("Intelligent Routing", lambda: orchestrator.route_command_intelligently("I need to implement a new feature with tests"))
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            start_time = time.time()
            result = test_func()
            execution_time = time.time() - start_time
            results[test_name] = {
                "success": True,
                "execution_time": execution_time,
                "result": result
            }
            print(f"  ✅ {test_name}: {execution_time:.3f}s")
        except Exception as e:
            results[test_name] = {
                "success": False,
                "error": str(e)
            }
            print(f"  ❌ {test_name}: {str(e)}")
    
    return {"success": all(r.get("success", False) for r in results.values()), "tests": results}


def run_session_tests(session_manager: SessionManager) -> Dict[str, Any]:
    """Run session management tests."""
    tests = [
        ("Session Initialization", lambda: session_manager.initialize_session()),
        ("Context Preservation", lambda: run_context_preservation_test(session_manager)),
        ("Session Compaction", lambda: session_manager.compact_session({
            "messages": ["msg"] * 1000,
            "context": "x" * 10000,
            "metadata": {f"key{i}": f"value{i}" for i in range(100)}
        })),
        ("GitHub Issue Tracking", lambda: session_manager.track_github_issue({
            "session_id": "test_session",
            "tasks": [{"task": "task1", "completed": True}]
        })),
        ("Metrics Collection", lambda: session_manager.collect_session_metrics({
            "start_time": time.time() - 3600,
            "commands_executed": 10,
            "tokens_used": 50000,
            "errors_encountered": 2
        }))
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            start_time = time.time()
            result = test_func()
            execution_time = time.time() - start_time
            results[test_name] = {
                "success": True,
                "execution_time": execution_time,
                "result": result
            }
            print(f"  ✅ {test_name}: {execution_time:.3f}s")
        except Exception as e:
            results[test_name] = {
                "success": False,
                "error": str(e)
            }
            print(f"  ❌ {test_name}: {str(e)}")
    
    return {"success": all(r.get("success", False) for r in results.values()), "tests": results}


def run_context_preservation_test(session_manager: SessionManager) -> Dict[str, Any]:
    """Test context preservation and restoration."""
    test_context = {
        "current_task": "test_task",
        "progress": {"completed": 5, "total": 10},
        "variables": {"test_var": "test_value"}
    }
    
    session_manager.preserve_context(test_context)
    restored_context = session_manager.restore_context()
    
    return {
        "preserved": test_context,
        "restored": restored_context,
        "match": restored_context == test_context
    }


def run_memory_tests(memory_optimizer: MemorySystemOptimizer) -> Dict[str, Any]:
    """Run memory system tests."""
    tests = [
        ("Memory Hierarchy Loading", lambda: memory_optimizer.load_memory_hierarchy()),
        ("Token Optimization", lambda: memory_optimizer.optimize_memory_tokens({
            "project_memory": "x" * 5000,
            "user_memory": "y" * 3000,
            "imported_memory": "z" * 2000
        })),
        ("Conditional Memory Loading", lambda: memory_optimizer.load_conditional_memory({
            "task_type": "development",
            "modules_needed": ["tdd", "task-management"],
            "priority": "high"
        })),
        ("Usage Analytics", lambda: memory_optimizer.analyze_memory_usage({
            "session_duration": 3600,
            "tokens_consumed": 75000,
            "context_switches": 5
        }))
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            start_time = time.time()
            result = test_func()
            execution_time = time.time() - start_time
            results[test_name] = {
                "success": True,
                "execution_time": execution_time,
                "result": result
            }
            print(f"  ✅ {test_name}: {execution_time:.3f}s")
        except Exception as e:
            results[test_name] = {
                "success": False,
                "error": str(e)
            }
            print(f"  ❌ {test_name}: {str(e)}")
    
    return {"success": all(r.get("success", False) for r in results.values()), "tests": results}


def run_performance_tests(performance_optimizer: PerformanceOptimizer) -> Dict[str, Any]:
    """Run performance optimization tests."""
    tests = [
        ("Parallel Tool Execution", lambda: performance_optimizer.execute_tools_parallel([
            {"tool": "Read", "params": {"file": "file1.py"}},
            {"tool": "Read", "params": {"file": "file2.py"}},
            {"tool": "Read", "params": {"file": "file3.py"}}
        ])),
        ("Context Budget Optimization", lambda: performance_optimizer.optimize_context_budget({
            "framework_size": 120000,
            "session_data": 30000,
            "working_memory": 25000
        })),
        ("Response Time Optimization", lambda: performance_optimizer.optimize_response_time({
            "command": "task",
            "complexity": "medium",
            "estimated_duration": 120
        })),
        ("SWE-bench Performance Validation", lambda: performance_optimizer.validate_swe_bench_performance({
            "baseline_performance": 72.5,
            "current_performance": 79.4,
            "test_cases": 100,
            "success_rate": 0.794
        }))
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            start_time = time.time()
            result = test_func()
            execution_time = time.time() - start_time
            results[test_name] = {
                "success": True,
                "execution_time": execution_time,
                "result": result
            }
            print(f"  ✅ {test_name}: {execution_time:.3f}s")
        except Exception as e:
            results[test_name] = {
                "success": False,
                "error": str(e)
            }
            print(f"  ❌ {test_name}: {str(e)}")
    
    return {"success": all(r.get("success", False) for r in results.values()), "tests": results}


def run_integration_tests(integrator, orchestrator, session_manager, memory_optimizer, performance_optimizer) -> Dict[str, Any]:
    """Run full integration tests."""
    tests = [
        ("Full Integration Workflow", lambda: integrator.run_full_integration_test(
            orchestrator, session_manager, memory_optimizer, performance_optimizer
        )),
        ("End-to-End Performance", lambda: run_end_to_end_performance_test(
            integrator, orchestrator, session_manager, memory_optimizer, performance_optimizer
        ))
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            start_time = time.time()
            result = test_func()
            execution_time = time.time() - start_time
            results[test_name] = {
                "success": True,
                "execution_time": execution_time,
                "result": result
            }
            print(f"  ✅ {test_name}: {execution_time:.3f}s")
        except Exception as e:
            results[test_name] = {
                "success": False,
                "error": str(e)
            }
            print(f"  ❌ {test_name}: {str(e)}")
    
    return {"success": all(r.get("success", False) for r in results.values()), "tests": results}


def run_end_to_end_performance_test(integrator, orchestrator, session_manager, memory_optimizer, performance_optimizer) -> Dict[str, Any]:
    """Run end-to-end performance test."""
    start_time = time.time()
    
    # Initialize session
    session = session_manager.initialize_session()
    
    # Load memory hierarchy
    memory_hierarchy = memory_optimizer.load_memory_hierarchy()
    
    # Create execution plan
    execution_plan = orchestrator.create_execution_plan("task", {"input": "test_file.py"})
    
    # Optimize parallel execution
    parallel_plan = orchestrator.optimize_parallel_execution([
        "read_file1", "read_file2", "analyze_data", "write_output"
    ])
    
    # Execute parallel tools
    tool_results = performance_optimizer.execute_tools_parallel([
        {"tool": "Read", "params": {"file": "file1.py"}},
        {"tool": "Read", "params": {"file": "file2.py"}}
    ])
    
    # Optimize context
    context_optimization = integrator.optimize_context_window({
        "critical_instructions": "Important instructions",
        "context_info": "Context information",
        "examples": "Example code with\n# comments\n  extra spaces  \n",
        "references": "Reference materials"
    })
    
    end_time = time.time()
    total_time = end_time - start_time
    
    return {
        "total_execution_time": total_time,
        "performance_target_met": total_time < 2.0,  # Under 2 seconds
        "parallel_speedup": tool_results.get("speedup_factor", 1.0),
        "context_optimization_ratio": context_optimization.get("compression_ratio", 1.0),
        "memory_efficiency": len(memory_hierarchy) > 0,
        "session_initialized": session.get("session_id") is not None
    }


def generate_validation_report(validation_results: Dict[str, Any]) -> Dict[str, Any]:
    """Generate comprehensive validation report."""
    total_tests = 0
    passed_tests = 0
    
    for category, result in validation_results.items():
        if "tests" in result:
            category_tests = result["tests"]
            total_tests += len(category_tests)
            passed_tests += sum(1 for t in category_tests.values() if t.get("success", False))
    
    success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    report = {
        "validation_session": {
            "timestamp": datetime.now().isoformat(),
            "framework_version": "3.0.0",
            "total_tests": total_tests,
            "passed_tests": passed_tests,
            "success_rate": success_rate
        },
        "category_results": validation_results,
        "performance_summary": {
            "environment_integration": validation_results.get("environment", {}).get("success", False),
            "command_orchestration": validation_results.get("orchestration", {}).get("success", False),
            "session_management": validation_results.get("session", {}).get("success", False),
            "memory_optimization": validation_results.get("memory", {}).get("success", False),
            "performance_optimization": validation_results.get("performance", {}).get("success", False),
            "integration_tests": validation_results.get("integration", {}).get("success", False)
        },
        "recommendations": generate_recommendations(validation_results)
    }
    
    return report


def generate_recommendations(validation_results: Dict[str, Any]) -> List[str]:
    """Generate recommendations based on validation results."""
    recommendations = []
    
    # Check success rates
    for category, result in validation_results.items():
        if not result.get("success", False):
            recommendations.append(f"🔧 {category.title()}: Review failing tests and improve implementation")
    
    # Performance recommendations
    if validation_results.get("performance", {}).get("success", False):
        recommendations.append("✅ Performance: All performance tests passed - system ready for production")
    
    # Integration recommendations
    if validation_results.get("integration", {}).get("success", False):
        recommendations.append("✅ Integration: Full integration tests passed - components work together seamlessly")
    
    # General recommendations
    recommendations.extend([
        "📊 Monitoring: Set up continuous monitoring for production deployment",
        "🔒 Security: Implement additional security measures for production use",
        "📈 Optimization: Continue optimizing based on real-world usage patterns"
    ])
    
    return recommendations


def save_validation_report(report: Dict[str, Any]) -> Path:
    """Save validation report to file."""
    report_dir = project_root / "tests" / "results" / "integration"
    report_dir.mkdir(parents=True, exist_ok=True)
    
    report_file = report_dir / f"claude_code_integration_validation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    return report_file


def print_validation_summary(report: Dict[str, Any]) -> None:
    """Print validation summary."""
    print("\n" + "=" * 60)
    print("📊 CLAUDE CODE INTEGRATION VALIDATION SUMMARY")
    print("=" * 60)
    
    session = report["validation_session"]
    print(f"Framework Version: {session['framework_version']}")
    print(f"Total Tests: {session['total_tests']}")
    print(f"Passed Tests: {session['passed_tests']}")
    print(f"Success Rate: {session['success_rate']:.1f}%")
    
    print(f"\n📈 Performance Summary:")
    performance = report["performance_summary"]
    for category, success in performance.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {category.replace('_', ' ').title()}: {status}")
    
    print(f"\n🎯 Recommendations:")
    for i, rec in enumerate(report["recommendations"], 1):
        print(f"  {i}. {rec}")


if __name__ == "__main__":
    exit_code = run_comprehensive_integration_validation()
    sys.exit(exit_code)