#!/usr/bin/env python3
"""
Functional Path Traversal Protection Test

Simple test that validates path traversal protection is working without
complex imports. This demonstrates actual functional protection.
"""

import os
import sys
import pathlib
import tempfile

# Add the implementation directory to path
current_dir = pathlib.Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from path_validation_impl import (
        validate_path_security,
        validate_notebook_path,
        validate_component_name,
        validate_endpoint_name,
        SecurityError
    )
    print("✅ Successfully imported path validation functions")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)

def test_notebook_run_protection():
    """Test /notebook-run path traversal protection"""
    print("\n🔒 Testing /notebook-run protection...")
    
    # Test legitimate paths
    legitimate_tests = [
        "notebooks/analysis.ipynb",
        "data/dataset.csv",
        "experiments/model.ipynb"
    ]
    
    for test_path in legitimate_tests:
        result = validate_path_security(test_path, "notebook-run")
        if result['valid']:
            print(f"✅ ALLOWED: {test_path}")
        else:
            print(f"❌ BLOCKED: {test_path} - {result['reason']}")
    
    # Test malicious paths
    malicious_tests = [
        "../../../etc/passwd",
        "../../system/secrets",
        "notebooks/../../../sensitive"
    ]
    
    blocked_count = 0
    for test_path in malicious_tests:
        result = validate_path_security(test_path, "notebook-run")
        if not result['valid']:
            print(f"✅ BLOCKED: {test_path} - {result['reason']}")
            blocked_count += 1
        else:
            print(f"❌ FAILED TO BLOCK: {test_path}")
    
    return blocked_count == len(malicious_tests)

def test_component_gen_protection():
    """Test /component-gen path traversal protection"""
    print("\n🔒 Testing /component-gen protection...")
    
    # Test legitimate component names
    legitimate_tests = [
        "Button",
        "UserCard",
        "DataGrid"
    ]
    
    for test_name in legitimate_tests:
        result = validate_component_name(test_name)
        if result['valid']:
            print(f"✅ ALLOWED: {test_name}")
        else:
            print(f"❌ BLOCKED: {test_name} - {result['reason']}")
    
    # Test malicious component names
    malicious_tests = [
        "../../../etc/malicious",
        "../../config/override",
        "component<script>alert('xss')</script>"
    ]
    
    blocked_count = 0
    for test_name in malicious_tests:
        result = validate_component_name(test_name)
        if not result['valid']:
            print(f"✅ BLOCKED: {test_name} - {result['reason']}")
            blocked_count += 1
        else:
            print(f"❌ FAILED TO BLOCK: {test_name}")
    
    return blocked_count == len(malicious_tests)

def test_api_design_protection():
    """Test /api-design path traversal protection"""
    print("\n🔒 Testing /api-design protection...")
    
    # Test legitimate endpoint names
    legitimate_tests = [
        "users",
        "dashboard/analytics",
        "auth/login"
    ]
    
    for test_endpoint in legitimate_tests:
        result = validate_endpoint_name(test_endpoint)
        if result['valid']:
            print(f"✅ ALLOWED: {test_endpoint}")
        else:
            print(f"❌ BLOCKED: {test_endpoint} - {result['reason']}")
    
    # Test malicious endpoint names
    malicious_tests = [
        "../../../etc/passwd",
        "../../config/secrets",
        "../../../system/hack"
    ]
    
    blocked_count = 0
    for test_endpoint in malicious_tests:
        result = validate_endpoint_name(test_endpoint)
        if not result['valid']:
            print(f"✅ BLOCKED: {test_endpoint} - {result['reason']}")
            blocked_count += 1
        else:
            print(f"❌ FAILED TO BLOCK: {test_endpoint}")
    
    return blocked_count == len(malicious_tests)

def test_performance():
    """Test that validation performance is under 5ms"""
    print("\n⚡ Testing performance...")
    
    import time
    test_path = "notebooks/analysis.ipynb"
    iterations = 100
    
    start_time = time.time()
    for _ in range(iterations):
        validate_path_security(test_path, "notebook-run")
    
    total_time = time.time() - start_time
    avg_time_ms = (total_time * 1000) / iterations
    
    print(f"Average validation time: {avg_time_ms:.2f}ms")
    
    if avg_time_ms < 5.0:
        print("✅ Performance test PASSED - Under 5ms limit")
        return True
    else:
        print("❌ Performance test FAILED - Exceeds 5ms limit")
        return False

def main():
    """Run all functional protection tests"""
    print("🧪 FUNCTIONAL PATH TRAVERSAL PROTECTION TESTS")
    print("=" * 50)
    
    results = {
        'notebook_run': test_notebook_run_protection(),
        'component_gen': test_component_gen_protection(),
        'api_design': test_api_design_protection(),
        'performance': test_performance()
    }
    
    print("\n📊 TEST RESULTS:")
    print("=" * 30)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name.replace('_', '-').title()}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🛡️  All functional path traversal protection tests PASSED")
        print("🔒 Security protection is working correctly")
        return True
    else:
        print("⚠️  Some tests FAILED - Review implementation")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)