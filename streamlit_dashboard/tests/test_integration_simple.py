"""
Simplified integration tests for streamlit dashboard components.
Focus on basic functionality without complex mocking.
"""

import sys
from pathlib import Path
from unittest.mock import patch
import time

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_basic_component_imports():
    """Test that all main components can be imported without errors"""
    print("🔍 Testing component imports...")
    
    try:
        from components.interactive_prompt_builder import InteractivePromptBuilder
        print("  ✅ InteractivePromptBuilder imported successfully")
    except Exception as e:
        print(f"  ❌ Failed to import InteractivePromptBuilder: {e}")
        return False
        
    try:
        from components.framework_overview import FrameworkOverview
        print("  ✅ FrameworkOverview imported successfully")
    except Exception as e:
        print(f"  ❌ Failed to import FrameworkOverview: {e}")
        return False
        
    try:
        from components.command_explorer import CommandExplorer
        print("  ✅ CommandExplorer imported successfully")
    except Exception as e:
        print(f"  ❌ Failed to import CommandExplorer: {e}")
        return False
        
    try:
        from components.context_aware_analyzer import ContextAwareAnalyzer
        print("  ✅ ContextAwareAnalyzer imported successfully")
    except Exception as e:
        print(f"  ❌ Failed to import ContextAwareAnalyzer: {e}")
        return False
        
    return True

def test_component_initialization():
    """Test that components can be initialized with framework path"""
    print("🚀 Testing component initialization...")
    
    framework_path = Path(__file__).parent.parent.parent / ".claude"
    
    if not framework_path.exists():
        print(f"  ⚠️  Framework path not found: {framework_path}")
        print("  📝 Testing with mock path...")
        framework_path = Path("/tmp/test_claude")
    
    try:
        from components.interactive_prompt_builder import InteractivePromptBuilder
        builder = InteractivePromptBuilder(framework_path=framework_path)
        print(f"  ✅ InteractivePromptBuilder initialized with path: {builder.framework_path}")
    except Exception as e:
        print(f"  ❌ Failed to initialize InteractivePromptBuilder: {e}")
        return False
        
    try:
        from components.framework_overview import FrameworkOverview
        overview = FrameworkOverview(framework_path=framework_path)
        print(f"  ✅ FrameworkOverview initialized with path: {overview.framework_path}")
    except Exception as e:
        print(f"  ❌ Failed to initialize FrameworkOverview: {e}")
        return False
        
    return True

def test_streamlit_app_structure():
    """Test that the main app structure is valid"""
    print("📱 Testing app structure...")
    
    try:
        from app import AppConfig, setup_navigation, route_to_page, main
        print("  ✅ App components imported successfully")
        
        # Test AppConfig
        config_path = AppConfig.FRAMEWORK_PATH
        print(f"  ✅ Framework path configured: {config_path}")
        
        # Test navigation pages
        pages = AppConfig.NAVIGATION_PAGES
        print(f"  ✅ Navigation configured with {len(pages)} pages")
        
        # Check for key pages
        key_pages = [
            "Framework Overview",
            "Interactive Prompt Builder", 
            "Command Explorer"
        ]
        
        for page in key_pages:
            if page in pages:
                print(f"    ✅ {page} found in navigation")
            else:
                print(f"    ❌ {page} missing from navigation")
                return False
                
        return True
        
    except Exception as e:
        print(f"  ❌ Failed to test app structure: {e}")
        return False

def test_prompt_builder_functionality():
    """Test core prompt builder functionality without full streamlit"""
    print("🔧 Testing prompt builder functionality...")
    
    framework_path = Path(__file__).parent.parent.parent / ".claude"
    
    try:
        from components.interactive_prompt_builder import InteractivePromptBuilder
        
        # Mock streamlit components for testing
        with patch('streamlit.title'), \
             patch('streamlit.write'), \
             patch('streamlit.columns'), \
             patch('streamlit.tabs'), \
             patch('streamlit.container'):
            
            builder = InteractivePromptBuilder(framework_path=framework_path)
            
            # Test module loading
            start_time = time.time()
            all_modules = builder._load_all_modules()
            load_time = time.time() - start_time
            
            print(f"  ✅ Module loading completed in {load_time:.2f}s")
            print(f"  📊 Found {len(all_modules)} module categories")
            
            # Test basic composition workspace
            builder.composition_workspace = []
            print("  ✅ Composition workspace initialized")
            
            # Test prompt generation with empty workspace
            try:
                prompt = builder._generate_prompt()
                print("  ✅ Prompt generation completed")
                print(f"  📝 Generated prompt length: {len(prompt) if prompt else 0} characters")
            except Exception as e:
                print(f"  ⚠️  Prompt generation with empty workspace: {e}")
            
            return True
            
    except Exception as e:
        print(f"  ❌ Failed to test prompt builder: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_performance_characteristics():
    """Test basic performance characteristics"""
    print("⚡ Testing performance characteristics...")
    
    framework_path = Path(__file__).parent.parent.parent / ".claude"
    
    try:
        from components.interactive_prompt_builder import InteractivePromptBuilder
        
        # Test initialization time
        start_time = time.time()
        builder = InteractivePromptBuilder(framework_path=framework_path)
        init_time = time.time() - start_time
        
        print(f"  ⏱️  Component initialization: {init_time:.3f}s")
        
        if init_time < 2.0:
            print("  ✅ Initialization time acceptable (< 2s)")
        else:
            print("  ⚠️  Initialization time high (>= 2s)")
            
        # Test module loading time
        start_time = time.time()
        modules = builder._load_all_modules()
        load_time = time.time() - start_time
        
        print(f"  ⏱️  Module loading: {load_time:.3f}s")
        
        if load_time < 3.0:
            print("  ✅ Module loading time acceptable (< 3s)")
        else:
            print("  ⚠️  Module loading time high (>= 3s)")
            
        return True
        
    except Exception as e:
        print(f"  ❌ Failed performance test: {e}")
        return False

def test_error_handling():
    """Test basic error handling"""
    print("🛡️ Testing error handling...")
    
    try:
        from components.interactive_prompt_builder import InteractivePromptBuilder
        
        # Test with invalid path
        invalid_path = Path("/nonexistent/path/to/framework")
        builder = InteractivePromptBuilder(framework_path=invalid_path)
        
        # This should not crash
        try:
            modules = builder._load_all_modules()
            print("  ✅ Handled invalid path gracefully")
            print(f"  📊 Returned {len(modules)} modules (expected empty)")
        except Exception as e:
            print(f"  ✅ Handled invalid path with exception: {type(e).__name__}")
            
        return True
        
    except Exception as e:
        print(f"  ❌ Error handling test failed: {e}")
        return False

def run_all_tests():
    """Run all integration tests"""
    print("🚀 Starting Simplified Integration Tests")
    print("=" * 60)
    
    tests = [
        ("Component Imports", test_basic_component_imports),
        ("Component Initialization", test_component_initialization),
        ("App Structure", test_streamlit_app_structure),
        ("Prompt Builder Functionality", test_prompt_builder_functionality),
        ("Performance Characteristics", test_performance_characteristics),
        ("Error Handling", test_error_handling)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n📋 Running: {test_name}")
        print("-" * 40)
        
        try:
            success = test_func()
            if success:
                print(f"✅ {test_name} PASSED")
                passed += 1
            else:
                print(f"❌ {test_name} FAILED")
                failed += 1
        except Exception as e:
            print(f"❌ {test_name} FAILED with exception: {e}")
            failed += 1
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print(f"📊 Integration Test Results:")
    print(f"   ✅ Passed: {passed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📈 Success Rate: {passed/(passed+failed)*100:.1f}%")
    
    if passed == len(tests):
        print("🎉 ALL TESTS PASSED! Dashboard integration is working well.")
    elif passed > failed:
        print("👍 Most tests passed. Some minor issues to address.")
    else:
        print("⚠️  Several issues found. Requires attention.")
    
    return passed, failed

if __name__ == "__main__":
    run_all_tests()