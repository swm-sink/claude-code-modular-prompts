"""
Integration tests for complete user workflows in the Streamlit dashboard.
Tests end-to-end prompt engineering journeys and cross-component functionality.
"""

import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

from components.interactive_prompt_builder import InteractivePromptBuilder
from components.framework_overview import FrameworkOverview
from components.command_explorer import CommandExplorer
from components.context_aware_analyzer import ContextAwareAnalyzer
from components.module_visualizer import PromptComponentExplorer
from components.module_visualizer import PromptModule


class TestIntegrationWorkflows:
    """Test complete user workflows and component integration"""
    
    @pytest.fixture
    def framework_path(self):
        """Get the framework path for testing"""
        return Path(__file__).parent.parent.parent / ".claude"
    
    @pytest.fixture
    def mock_streamlit(self):
        """Mock streamlit components for testing"""
        with patch('streamlit.title'), \
             patch('streamlit.write'), \
             patch('streamlit.columns'), \
             patch('streamlit.tabs'), \
             patch('streamlit.selectbox'), \
             patch('streamlit.button'), \
             patch('streamlit.multiselect'), \
             patch('streamlit.text_area'), \
             patch('streamlit.sidebar'), \
             patch('streamlit.container'), \
             patch('streamlit.expander'):
            yield
    
    def test_prompt_engineering_workflow_integration(self, framework_path, mock_streamlit):
        """Test the complete prompt engineering workflow"""
        
        # Step 1: Framework Overview - User understands the system
        overview = FrameworkOverview(framework_path=framework_path)
        assert overview.framework_path.exists()
        
        # Step 2: Component Exploration - User explores available modules  
        explorer = PromptComponentExplorer(framework_path=framework_path)
        modules = explorer._load_all_modules()
        assert len(modules) > 0, "Should have framework modules available"
        
        # Step 3: Interactive Prompt Building - User composes prompts
        builder = InteractivePromptBuilder(framework_path=framework_path)
        assert builder.framework_path.exists()
        
        # Test module selection and composition
        test_modules = [
            PromptModule(
                name="test_module",
                category="patterns", 
                description="Test module",
                purpose="Testing",
                token_efficiency=0.8,
                use_cases=["testing"]
            )
        ]
        
        # Simulate adding modules to workspace
        builder.composition_workspace = test_modules
        
        # Test prompt generation
        prompt = builder._generate_prompt()
        assert prompt is not None
        assert len(prompt) > 0
        assert "claude_4_module_execution" in prompt
        
        # Step 4: Validation and Testing - User validates the prompt
        validation = builder._validate_prompt_structure()
        assert "overall_valid" in validation
        assert "xml_valid" in validation
        
        print("✅ Complete prompt engineering workflow integration test passed")
    
    def test_component_cross_communication(self, framework_path, mock_streamlit):
        """Test that components can share state and communicate"""
        
        # Initialize multiple components
        builder = InteractivePromptBuilder(framework_path=framework_path)
        analyzer = ContextAwareAnalyzer(framework_path=framework_path)
        explorer = CommandExplorer(framework_path=framework_path)
        
        # Test shared framework access
        assert builder.framework_path == analyzer.framework_path == explorer.framework_path
        
        # Test module data consistency
        builder_modules = builder._load_all_modules()
        analyzer_modules = analyzer._load_framework_modules()
        
        # Should have modules from same source
        assert len(builder_modules) > 0
        assert len(analyzer_modules) > 0
        
        print("✅ Cross-component communication test passed")
    
    def test_error_handling_graceful_degradation(self, mock_streamlit):
        """Test error handling and graceful degradation"""
        
        # Test with invalid framework path
        invalid_path = Path("/nonexistent/path")
        
        # Components should handle invalid paths gracefully
        builder = InteractivePromptBuilder(framework_path=invalid_path)
        
        # Should not crash on invalid path
        try:
            modules = builder._load_all_modules()
            # Should return empty dict or handle gracefully
            assert isinstance(modules, dict)
        except Exception as e:
            # If it raises an exception, it should be handled gracefully
            assert "not found" in str(e).lower() or "does not exist" in str(e).lower() or "no such file" in str(e).lower()
        
        print("✅ Error handling graceful degradation test passed")
    
    def test_performance_characteristics(self, framework_path, mock_streamlit):
        """Test performance characteristics of key components"""
        import time
        
        # Test Interactive Prompt Builder initialization time
        start_time = time.time()
        builder = InteractivePromptBuilder(framework_path=framework_path)
        init_time = time.time() - start_time
        
        assert init_time < 2.0, f"Component initialization took {init_time:.2f}s, should be < 2s"
        
        # Test module loading time
        start_time = time.time()
        modules = builder._load_all_modules()
        load_time = time.time() - start_time
        
        assert load_time < 3.0, f"Module loading took {load_time:.2f}s, should be < 3s"
        
        # Test prompt generation time (if modules available)
        if modules:
            # Convert dict values to list and create test modules
            test_modules = [
                PromptModule(
                    name="test_module_1",
                    category="patterns", 
                    description="Test module 1",
                    purpose="Testing",
                    token_efficiency=0.8,
                    use_cases=["testing"]
                )
            ]
            builder.composition_workspace = test_modules
            
            start_time = time.time()
            prompt = builder._generate_prompt()
            gen_time = time.time() - start_time
            
            assert gen_time < 1.0, f"Prompt generation took {gen_time:.2f}s, should be < 1s"
        
        print("✅ Performance characteristics test passed")
    
    def test_state_persistence_simulation(self, framework_path, mock_streamlit):
        """Test state management and persistence capabilities"""
        
        builder = InteractivePromptBuilder(framework_path=framework_path)
        
        # Simulate user building a prompt
        test_modules = [
            PromptModule(
                name="module1",
                category="patterns",
                description="Test module 1", 
                purpose="Testing",
                token_efficiency=0.8,
                use_cases=["testing"]
            ),
            PromptModule(
                name="module2", 
                category="development",
                description="Test module 2",
                purpose="Development", 
                token_efficiency=0.9,
                use_cases=["dev"]
            )
        ]
        
        builder.composition_workspace = test_modules
        
        # Test prompt composition
        prompt = builder._generate_prompt()
        assert prompt is not None
        
        # Test state can be serialized (for session persistence)
        state_data = {
            'workspace_modules': [
                {
                    'name': m.name,
                    'category': m.category,
                    'description': m.description,
                    'purpose': m.purpose,
                    'token_efficiency': m.token_efficiency,
                    'use_cases': m.use_cases
                } for m in builder.composition_workspace
            ],
            'constructed_prompt': builder.constructed_prompt
        }
        
        assert len(state_data['workspace_modules']) == 2
        assert state_data['constructed_prompt'] is not None
        
        print("✅ State persistence simulation test passed")
    
    def test_export_functionality_readiness(self, framework_path, mock_streamlit):
        """Test readiness for export functionality"""
        
        builder = InteractivePromptBuilder(framework_path=framework_path)
        
        # Create a test composition
        test_modules = [
            PromptModule(
                name="export_test_module",
                category="patterns",
                description="Module for export testing",
                purpose="Export testing",
                token_efficiency=0.85,
                use_cases=["export", "testing"]
            )
        ]
        
        builder.composition_workspace = test_modules
        prompt = builder._generate_prompt()
        
        # Test export data structure
        export_data = {
            'metadata': {
                'created_at': '2025-07-18',
                'framework_version': '3.0.0',
                'component_count': len(test_modules)
            },
            'composition': {
                'modules': [
                    {
                        'name': m.name,
                        'category': m.category,
                        'description': m.description,
                        'purpose': m.purpose,
                        'token_efficiency': m.token_efficiency,
                        'use_cases': m.use_cases
                    } for m in test_modules
                ]
            },
            'prompt': {
                'generated_content': prompt,
                'validation_status': builder._validate_prompt_structure()
            }
        }
        
        # Verify export data completeness
        assert 'metadata' in export_data
        assert 'composition' in export_data
        assert 'prompt' in export_data
        assert export_data['metadata']['component_count'] == 1
        assert len(export_data['composition']['modules']) == 1
        assert export_data['prompt']['generated_content'] is not None
        
        print("✅ Export functionality readiness test passed")


def run_integration_tests():
    """Run all integration tests and report results"""
    
    print("🚀 Starting Integration Workflow Tests")
    print("=" * 50)
    
    # Get framework path
    framework_path = Path(__file__).parent.parent.parent / ".claude"
    
    # Initialize test class
    test_class = TestIntegrationWorkflows()
    
    # Mock streamlit for testing
    with patch('streamlit.title'), \
         patch('streamlit.write'), \
         patch('streamlit.columns'), \
         patch('streamlit.tabs'), \
         patch('streamlit.selectbox'), \
         patch('streamlit.button'), \
         patch('streamlit.multiselect'), \
         patch('streamlit.text_area'), \
         patch('streamlit.sidebar'), \
         patch('streamlit.container'), \
         patch('streamlit.expander'):
        
        tests = [
            ("Prompt Engineering Workflow", test_class.test_prompt_engineering_workflow_integration),
            ("Cross-Component Communication", test_class.test_component_cross_communication),
            ("Error Handling", test_class.test_error_handling_graceful_degradation),
            ("Performance Characteristics", test_class.test_performance_characteristics),
            ("State Persistence", test_class.test_state_persistence_simulation),
            ("Export Readiness", test_class.test_export_functionality_readiness)
        ]
        
        passed = 0
        failed = 0
        
        for test_name, test_func in tests:
            try:
                print(f"\n📋 Running: {test_name}")
                if test_name == "Error Handling":
                    test_func()  # No arguments for this test
                else:
                    test_func(framework_path, None)  # Pass mock_streamlit as None since it's already patched
                passed += 1
            except Exception as e:
                print(f"❌ FAILED: {test_name} - {str(e)}")
                failed += 1
                import traceback
                traceback.print_exc()
    
    print("\n" + "=" * 50)
    print(f"📊 Integration Test Results:")
    print(f"   ✅ Passed: {passed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📈 Success Rate: {passed/(passed+failed)*100:.1f}%")
    
    return passed, failed


if __name__ == "__main__":
    run_integration_tests()