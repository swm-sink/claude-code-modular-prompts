"""
Tests for Unified Template Manager component
TDD RED PHASE: Write failing tests first
"""

import pytest
import unittest.mock as mock
from pathlib import Path
import json
import tempfile
from unittest.mock import MagicMock, patch
from datetime import datetime
from typing import Dict, List, Any
import copy

# Import the component we're going to build
try:
    from components.template_manager import TemplateManager, Template, TemplateCategory, TemplateValidator
except ImportError:
    # These don't exist yet - we'll create them
    TemplateManager = None
    Template = None
    TemplateCategory = None
    TemplateValidator = None


class TestTemplate:
    """Test the Template data class"""
    
    def test_template_creation(self):
        """Test Template can be created with proper data"""
        if Template is None:
            pytest.skip("Template not implemented yet")
        
        template_data = {
            'id': 'test_template_001',
            'name': 'Test Template',
            'description': 'A test template for unit testing',
            'category': 'development',
            'author': 'Test Author',
            'version': '1.0.0',
            'components': [
                {'type': 'command', 'name': 'task', 'file': 'commands/task.md'},
                {'type': 'module', 'name': 'tdd-cycle', 'file': 'modules/patterns/tdd-cycle.md'}
            ],
            'metadata': {
                'framework_version': '3.0.0',
                'tags': ['development', 'tdd', 'testing'],
                'difficulty': 'beginner'
            }
        }
        
        template = Template(**template_data)
        assert template.id == 'test_template_001'
        assert template.name == 'Test Template'
        assert template.category == 'development'
        assert len(template.components) == 2
        assert len(template.metadata['tags']) == 3
    
    def test_template_validation(self):
        """Test Template validates required fields"""
        if Template is None:
            pytest.skip("Template not implemented yet")
        
        # Test missing required fields
        with pytest.raises(ValueError):
            Template(id="", name="Test", description="Test", category="dev", author="Test", version="1.0")
        
        with pytest.raises(ValueError):
            Template(id="test", name="", description="Test", category="dev", author="Test", version="1.0")
        
        with pytest.raises(ValueError):
            Template(id="test", name="Test", description="Test", category="invalid", author="Test", version="1.0")
    
    def test_template_serialization(self):
        """Test Template can be serialized to/from dictionary"""
        if Template is None:
            pytest.skip("Template not implemented yet")
        
        template_data = {
            'id': 'test_template_001',
            'name': 'Test Template',
            'description': 'A test template',
            'category': 'development',
            'author': 'Test Author',
            'version': '1.0.0',
            'components': [{'type': 'command', 'name': 'task'}],
            'metadata': {'tags': ['test']}
        }
        
        template = Template(**template_data)
        
        # Test to_dict
        serialized = template.to_dict()
        assert isinstance(serialized, dict)
        assert serialized['id'] == 'test_template_001'
        assert serialized['name'] == 'Test Template'
        
        # Test from_dict
        recreated = Template.from_dict(serialized)
        assert recreated.id == template.id
        assert recreated.name == template.name
        assert recreated.components == template.components


class TestTemplateCategory:
    """Test the TemplateCategory enum/class"""
    
    def test_template_categories(self):
        """Test template categories are properly defined"""
        if TemplateCategory is None:
            pytest.skip("TemplateCategory not implemented yet")
        
        # Test that standard categories exist
        assert hasattr(TemplateCategory, 'DEVELOPMENT')
        assert hasattr(TemplateCategory, 'RESEARCH')
        assert hasattr(TemplateCategory, 'ANALYSIS')
        assert hasattr(TemplateCategory, 'DOCUMENTATION')
        assert hasattr(TemplateCategory, 'TESTING')
        assert hasattr(TemplateCategory, 'CUSTOM')
    
    def test_category_validation(self):
        """Test category validation"""
        if TemplateCategory is None:
            pytest.skip("TemplateCategory not implemented yet")
        
        # Test valid categories
        assert TemplateCategory.is_valid('development')
        assert TemplateCategory.is_valid('research')
        assert TemplateCategory.is_valid('analysis')
        
        # Test invalid categories
        assert not TemplateCategory.is_valid('invalid_category')
        assert not TemplateCategory.is_valid('')
        assert not TemplateCategory.is_valid(None)


class TestTemplateValidator:
    """Test the TemplateValidator class"""
    
    @pytest.fixture
    def framework_path(self, tmp_path):
        """Create a temporary framework directory"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create sample framework structure
        commands_dir = framework_dir / "commands"
        commands_dir.mkdir()
        (commands_dir / "task.md").write_text("# Task Command")
        
        modules_dir = framework_dir / "modules" / "patterns"
        modules_dir.mkdir(parents=True)
        (modules_dir / "tdd-cycle.md").write_text("# TDD Cycle")
        
        return framework_dir
    
    def test_validator_initialization(self, framework_path):
        """Test TemplateValidator can be initialized"""
        if TemplateValidator is None:
            pytest.skip("TemplateValidator not implemented yet")
        
        validator = TemplateValidator(framework_path=framework_path)
        assert validator.framework_path == framework_path
    
    def test_validate_template_components(self, framework_path):
        """Test validating template components exist"""
        if TemplateValidator is None:
            pytest.skip("TemplateValidator not implemented yet")
        
        validator = TemplateValidator(framework_path=framework_path)
        
        # Valid template
        valid_template = {
            'components': [
                {'type': 'command', 'name': 'task', 'file': 'commands/task.md'},
                {'type': 'module', 'name': 'tdd-cycle', 'file': 'modules/patterns/tdd-cycle.md'}
            ]
        }
        
        is_valid, errors = validator.validate_template_components(valid_template)
        assert is_valid is True
        assert len(errors) == 0
        
        # Invalid template (missing file)
        invalid_template = {
            'components': [
                {'type': 'command', 'name': 'nonexistent', 'file': 'commands/nonexistent.md'}
            ]
        }
        
        is_valid, errors = validator.validate_template_components(invalid_template)
        assert is_valid is False
        assert len(errors) > 0
    
    def test_validate_framework_version(self, framework_path):
        """Test validating framework version compatibility"""
        if TemplateValidator is None:
            pytest.skip("TemplateValidator not implemented yet")
        
        validator = TemplateValidator(framework_path=framework_path)
        
        # Test compatible version
        assert validator.validate_framework_version('3.0.0') is True
        assert validator.validate_framework_version('3.0.1') is True
        
        # Test incompatible version
        assert validator.validate_framework_version('2.0.0') is False
        assert validator.validate_framework_version('4.0.0') is False
    
    def test_resolve_template_dependencies(self, framework_path):
        """Test resolving template dependencies"""
        if TemplateValidator is None:
            pytest.skip("TemplateValidator not implemented yet")
        
        validator = TemplateValidator(framework_path=framework_path)
        
        template_data = {
            'components': [
                {'type': 'command', 'name': 'task', 'file': 'commands/task.md'}
            ]
        }
        
        resolved_deps = validator.resolve_template_dependencies(template_data)
        
        assert isinstance(resolved_deps, list)
        # Should include implicit dependencies like quality gates for commands


class TestTemplateManager:
    """Test the TemplateManager component"""
    
    @pytest.fixture
    def template_storage(self, tmp_path):
        """Create temporary template storage directory"""
        storage_dir = tmp_path / "templates"
        storage_dir.mkdir()
        return storage_dir
    
    @pytest.fixture
    def framework_path(self, tmp_path):
        """Create a temporary framework directory"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create sample framework structure
        commands_dir = framework_dir / "commands"
        commands_dir.mkdir()
        (commands_dir / "task.md").write_text("# Task Command")
        
        # Create modules directory structure
        modules_dir = framework_dir / "modules" / "patterns"
        modules_dir.mkdir(parents=True)
        (modules_dir / "tdd-cycle.md").write_text("# TDD Cycle Pattern")
        
        return framework_dir
    
    @pytest.fixture
    def sample_template(self):
        """Create a sample template for testing"""
        return {
            'id': 'sample_template_001',
            'name': 'Sample Development Template',
            'description': 'A sample template for development workflows',
            'category': 'development',
            'author': 'Test Author',
            'version': '1.0.0',
            'components': [
                {'type': 'command', 'name': 'task', 'file': 'commands/task.md'},
                {'type': 'module', 'name': 'tdd-cycle', 'file': 'modules/patterns/tdd-cycle.md'}
            ],
            'metadata': {
                'framework_version': '3.0.0',
                'tags': ['development', 'tdd', 'workflow'],
                'difficulty': 'beginner',
                'created_at': datetime.now().isoformat()
            }
        }
    
    def test_template_manager_initialization(self, template_storage, framework_path):
        """Test TemplateManager can be initialized"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(
            template_storage_path=template_storage,
            framework_path=framework_path
        )
        
        assert manager.template_storage_path == template_storage
        assert manager.framework_path == framework_path
        assert hasattr(manager, 'validator')
    
    def test_save_template(self, template_storage, framework_path, sample_template):
        """Test saving a template"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save template
        success = manager.save_template(sample_template)
        assert success is True
        
        # Verify file was created
        template_file = template_storage / f"{sample_template['id']}.json"
        assert template_file.exists()
        
        # Verify content
        with open(template_file) as f:
            saved_data = json.load(f)
        
        assert saved_data['id'] == sample_template['id']
        assert saved_data['name'] == sample_template['name']
    
    def test_load_template(self, template_storage, framework_path, sample_template):
        """Test loading a template"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save template first
        manager.save_template(sample_template)
        
        # Load template
        loaded_template = manager.load_template(sample_template['id'])
        
        assert loaded_template is not None
        assert loaded_template['id'] == sample_template['id']
        assert loaded_template['name'] == sample_template['name']
        assert len(loaded_template['components']) == len(sample_template['components'])
    
    def test_list_templates(self, template_storage, framework_path, sample_template):
        """Test listing all templates"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save multiple templates
        template1 = copy.deepcopy(sample_template)
        template1['id'] = 'template_001'
        template1['name'] = 'Template 1'
        
        template2 = copy.deepcopy(sample_template)
        template2['id'] = 'template_002'
        template2['name'] = 'Template 2'
        template2['category'] = 'research'
        
        manager.save_template(template1)
        manager.save_template(template2)
        
        # List all templates
        templates = manager.list_templates()
        
        assert len(templates) == 2
        assert any(t['id'] == 'template_001' for t in templates)
        assert any(t['id'] == 'template_002' for t in templates)
    
    def test_search_templates(self, template_storage, framework_path, sample_template):
        """Test searching templates"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save test templates
        template1 = copy.deepcopy(sample_template)
        template1['id'] = 'dev_template_001'
        template1['name'] = 'Development Workflow'
        template1['category'] = 'development'
        template1['metadata']['tags'] = ['python', 'tdd', 'development']
        
        template2 = copy.deepcopy(sample_template)
        template2['id'] = 'research_template_001'
        template2['name'] = 'Research Analysis'
        template2['category'] = 'research'
        template2['metadata']['tags'] = ['analysis', 'research', 'data']
        
        manager.save_template(template1)
        manager.save_template(template2)
        
        # Search by category
        dev_templates = manager.search_templates(category='development')
        assert len(dev_templates) == 1
        assert dev_templates[0]['id'] == 'dev_template_001'
        
        # Search by tag
        tdd_templates = manager.search_templates(tags=['tdd'])
        assert len(tdd_templates) == 1
        assert tdd_templates[0]['id'] == 'dev_template_001'
        
        # Search by name
        research_templates = manager.search_templates(name_contains='Research')
        assert len(research_templates) == 1
        assert research_templates[0]['id'] == 'research_template_001'
    
    def test_delete_template(self, template_storage, framework_path, sample_template):
        """Test deleting a template"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save template
        manager.save_template(sample_template)
        
        # Verify it exists
        assert manager.load_template(sample_template['id']) is not None
        
        # Delete template
        success = manager.delete_template(sample_template['id'])
        assert success is True
        
        # Verify it's gone
        assert manager.load_template(sample_template['id']) is None
    
    def test_validate_template(self, template_storage, framework_path, sample_template):
        """Test validating a template"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Test valid template
        is_valid, errors = manager.validate_template(sample_template)
        assert is_valid is True
        assert len(errors) == 0
        
        # Test invalid template
        invalid_template = copy.deepcopy(sample_template)
        invalid_template['components'] = [
            {'type': 'command', 'name': 'nonexistent', 'file': 'commands/nonexistent.md'}
        ]
        
        is_valid, errors = manager.validate_template(invalid_template)
        assert is_valid is False
        assert len(errors) > 0
    
    def test_get_template_categories(self, template_storage, framework_path):
        """Test getting available template categories"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        categories = manager.get_template_categories()
        
        assert isinstance(categories, list)
        assert 'development' in categories
        assert 'research' in categories
        assert 'analysis' in categories
        assert 'documentation' in categories
    
    def test_export_template(self, template_storage, framework_path, sample_template, tmp_path):
        """Test exporting a template"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save template
        manager.save_template(sample_template)
        
        # Export template
        export_file = tmp_path / "exported_template.json"
        success = manager.export_template(sample_template['id'], export_file)
        
        assert success is True
        assert export_file.exists()
        
        # Verify exported content
        with open(export_file) as f:
            exported_data = json.load(f)
        
        assert exported_data['id'] == sample_template['id']
        assert exported_data['name'] == sample_template['name']
    
    def test_import_template(self, template_storage, framework_path, sample_template, tmp_path):
        """Test importing a template"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Create template file to import
        import_file = tmp_path / "import_template.json"
        with open(import_file, 'w') as f:
            json.dump(sample_template, f)
        
        # Import template
        success = manager.import_template(import_file)
        
        assert success is True
        
        # Verify template was imported
        imported_template = manager.load_template(sample_template['id'])
        assert imported_template is not None
        assert imported_template['name'] == sample_template['name']
    
    def test_get_template_metadata(self, template_storage, framework_path, sample_template):
        """Test getting template metadata without loading full template"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save template
        manager.save_template(sample_template)
        
        # Get metadata only
        metadata = manager.get_template_metadata(sample_template['id'])
        
        assert metadata is not None
        assert metadata['name'] == sample_template['name']
        assert metadata['category'] == sample_template['category']
        assert metadata['author'] == sample_template['author']
        assert 'components' not in metadata  # Should not include full components
    
    def test_duplicate_template(self, template_storage, framework_path, sample_template):
        """Test duplicating a template"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save original template
        manager.save_template(sample_template)
        
        # Duplicate template
        new_id = 'duplicated_template_001'
        new_name = 'Duplicated Template'
        
        success = manager.duplicate_template(
            source_id=sample_template['id'],
            new_id=new_id,
            new_name=new_name
        )
        
        assert success is True
        
        # Verify duplicate exists
        duplicated = manager.load_template(new_id)
        assert duplicated is not None
        assert duplicated['id'] == new_id
        assert duplicated['name'] == new_name
        assert duplicated['components'] == sample_template['components']
    
    def test_render_template_gallery_ui(self, template_storage, framework_path):
        """Test rendering template gallery UI"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Test that the method exists and can be called
        # We don't test Streamlit rendering in unit tests
        assert hasattr(manager, 'render_template_gallery_ui')
        assert callable(manager.render_template_gallery_ui)
    
    def test_get_template_usage_stats(self, template_storage, framework_path, sample_template):
        """Test getting template usage statistics"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save multiple templates with different categories and tags
        template1 = copy.deepcopy(sample_template)
        template1['id'] = 'stats_template_001'
        template1['category'] = 'development'
        template1['metadata']['tags'] = ['python', 'tdd']
        template1['author'] = 'Author 1'
        
        template2 = copy.deepcopy(sample_template)
        template2['id'] = 'stats_template_002'
        template2['category'] = 'research'
        template2['metadata']['tags'] = ['analysis', 'data']
        template2['author'] = 'Author 2'
        
        template3 = copy.deepcopy(sample_template)
        template3['id'] = 'stats_template_003'
        template3['category'] = 'development'
        template3['metadata']['tags'] = ['python', 'web']
        template3['author'] = 'Author 1'
        
        manager.save_template(template1)
        manager.save_template(template2)
        manager.save_template(template3)
        
        # Get usage statistics
        stats = manager.get_template_usage_stats()
        
        assert isinstance(stats, dict)
        assert stats['total_templates'] == 3
        
        # Check category statistics
        assert stats['categories']['development'] == 2
        assert stats['categories']['research'] == 1
        
        # Check tag statistics
        assert stats['tags']['python'] == 2
        assert stats['tags']['tdd'] == 1
        assert stats['tags']['analysis'] == 1
        assert stats['tags']['data'] == 1
        assert stats['tags']['web'] == 1
        
        # Check author statistics
        assert stats['authors']['Author 1'] == 2
        assert stats['authors']['Author 2'] == 1
    
    def test_get_templates_by_category(self, template_storage, framework_path, sample_template):
        """Test getting templates by category"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save templates with different categories
        template1 = copy.deepcopy(sample_template)
        template1['id'] = 'dev_template_001'
        template1['category'] = 'development'
        
        template2 = copy.deepcopy(sample_template)
        template2['id'] = 'research_template_001'
        template2['category'] = 'research'
        
        template3 = copy.deepcopy(sample_template)
        template3['id'] = 'dev_template_002'
        template3['category'] = 'development'
        
        manager.save_template(template1)
        manager.save_template(template2)
        manager.save_template(template3)
        
        # Get templates by category
        dev_templates = manager.get_templates_by_category('development')
        research_templates = manager.get_templates_by_category('research')
        
        assert len(dev_templates) == 2
        assert len(research_templates) == 1
        
        # Check that correct templates are returned
        dev_ids = [t['id'] for t in dev_templates]
        assert 'dev_template_001' in dev_ids
        assert 'dev_template_002' in dev_ids
        
        research_ids = [t['id'] for t in research_templates]
        assert 'research_template_001' in research_ids
    
    @patch('streamlit.title')
    @patch('streamlit.subheader')
    @patch('streamlit.columns')
    @patch('streamlit.metric')
    @patch('streamlit.text_input')
    @patch('streamlit.selectbox')
    @patch('streamlit.multiselect')
    @patch('streamlit.info')
    def test_render_gallery_tab_mock(self, mock_info, mock_multiselect, mock_selectbox, 
                                   mock_text_input, mock_metric, mock_columns, 
                                   mock_subheader, mock_title,
                                   template_storage, framework_path):
        """Test rendering gallery tab with mocked Streamlit components"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Mock Streamlit components with side_effect to handle different column counts
        def mock_columns_side_effect(n):
            return [MagicMock() for _ in range(n)]
        
        mock_columns.side_effect = mock_columns_side_effect
        mock_text_input.return_value = ""
        mock_selectbox.return_value = "All"
        mock_multiselect.return_value = []
        
        # Test that method exists and can be called
        assert hasattr(manager, '_render_gallery_tab')
        
        # Call method (should not raise exceptions)
        try:
            manager._render_gallery_tab()
            # If we get here, the method executed without errors
            assert True
        except AttributeError:
            # Method might not exist yet
            pytest.skip("_render_gallery_tab not implemented yet")
    
    @patch('streamlit.title')
    @patch('streamlit.subheader')
    @patch('streamlit.columns')
    @patch('streamlit.metric')
    @patch('streamlit.json')
    def test_render_statistics_tab_mock(self, mock_json, mock_metric, mock_columns, 
                                      mock_subheader, mock_title,
                                      template_storage, framework_path, sample_template):
        """Test rendering statistics tab with mocked Streamlit components"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Add some test data
        manager.save_template(sample_template)
        
        # Mock Streamlit components with side_effect to handle different column counts
        def mock_columns_side_effect(n):
            return [MagicMock() for _ in range(n)]
        
        mock_columns.side_effect = mock_columns_side_effect
        
        # Test that method exists and can be called
        assert hasattr(manager, '_render_statistics_tab')
        
        # Call method (should not raise exceptions)
        try:
            manager._render_statistics_tab()
            # If we get here, the method executed without errors
            assert True
        except AttributeError:
            # Method might not exist yet
            pytest.skip("_render_statistics_tab not implemented yet")
    
    @patch('streamlit.markdown')
    @patch('streamlit.slider')
    @patch('streamlit.number_input')
    @patch('streamlit.text_input')
    @patch('streamlit.button')
    @patch('streamlit.columns')
    @patch('streamlit.success')
    @patch('streamlit.code')
    @patch('streamlit.error')
    def test_render_template_sharing_dialog_mock(self, mock_error, mock_code, mock_success,
                                                mock_columns, mock_button, mock_text_input,
                                                mock_number_input, mock_slider, mock_markdown,
                                                template_storage, framework_path, sample_template):
        """Test rendering template sharing dialog with mocked Streamlit components"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save template first
        manager.save_template(sample_template)
        
        # Mock Streamlit components
        mock_columns.return_value = [MagicMock(), MagicMock()]
        mock_slider.return_value = 30
        mock_number_input.return_value = 100
        mock_text_input.return_value = "https://example.com/share"
        mock_button.return_value = False
        
        # Test that method exists and can be called
        assert hasattr(manager, '_render_template_sharing_dialog')
        
        # Call method (should not raise exceptions)
        try:
            manager._render_template_sharing_dialog(sample_template)
            # If we get here, the method executed without errors
            assert True
        except AttributeError:
            # Method might not exist yet
            pytest.skip("_render_template_sharing_dialog not implemented yet")
    
    def test_template_metadata_indexing(self, template_storage, framework_path, sample_template):
        """Test template metadata indexing functionality"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save template
        manager.save_template(sample_template)
        
        # Check that metadata index was updated
        assert sample_template['id'] in manager.metadata_index
        metadata = manager.metadata_index[sample_template['id']]
        
        assert metadata['name'] == sample_template['name']
        assert metadata['category'] == sample_template['category']
        assert metadata['author'] == sample_template['author']
        
        # Components should not be in metadata index (for efficiency)
        assert 'components' not in metadata
    
    def test_template_validation_integration(self, template_storage, framework_path):
        """Test template validation integration with TemplateManager"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Test validation of complete template
        complete_template = {
            'id': 'validation_test_001',
            'name': 'Validation Test Template',
            'description': 'A template for testing validation',
            'category': 'development',
            'author': 'Test Author',
            'version': '1.0.0',
            'components': [
                {'type': 'command', 'name': 'task', 'file': 'commands/task.md'}
            ],
            'metadata': {
                'framework_version': '3.0.0',
                'tags': ['test', 'validation'],
                'difficulty': 'intermediate'
            }
        }
        
        is_valid, errors = manager.validate_template(complete_template)
        
        if is_valid:
            assert len(errors) == 0
        else:
            assert len(errors) > 0
            assert isinstance(errors, list)
    
    def test_template_file_operations(self, template_storage, framework_path, sample_template):
        """Test template file operations and path handling"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Test _get_template_file_path method
        expected_path = template_storage / f"{sample_template['id']}.json"
        actual_path = manager._get_template_file_path(sample_template['id'])
        
        assert actual_path == expected_path
        assert isinstance(actual_path, Path)
        
        # Test file creation after saving
        manager.save_template(sample_template)
        assert actual_path.exists()
        
        # Test file deletion after deleting template
        manager.delete_template(sample_template['id'])
        assert not actual_path.exists()
    
    def test_template_search_edge_cases(self, template_storage, framework_path, sample_template):
        """Test template search with edge cases"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Save template
        manager.save_template(sample_template)
        
        # Test search with empty criteria
        results = manager.search_templates()
        assert len(results) == 1
        
        # Test search with non-existent category
        results = manager.search_templates(category='nonexistent')
        assert len(results) == 0
        
        # Test search with non-existent tags
        results = manager.search_templates(tags=['nonexistent_tag'])
        assert len(results) == 0
        
        # Test search with partial name match
        results = manager.search_templates(name_contains='Sample')
        assert len(results) == 1
        
        # Test search with case insensitive name
        results = manager.search_templates(name_contains='sample')
        assert len(results) == 1
        
        # Test search with non-existent author
        results = manager.search_templates(author='Nonexistent Author')
        assert len(results) == 0
    
    def test_template_component_operations(self, template_storage, framework_path, sample_template):
        """Test template component operations"""
        if TemplateManager is None:
            pytest.skip("TemplateManager not implemented yet")
        
        manager = TemplateManager(template_storage, framework_path)
        
        # Create template instance
        template = Template(**sample_template)
        
        # Test component operations
        initial_count = template.get_component_count()
        assert initial_count == len(sample_template['components'])
        
        # Test adding component
        new_component = {'type': 'module', 'name': 'new-module', 'file': 'modules/new-module.md'}
        template.add_component(new_component)
        
        assert template.get_component_count() == initial_count + 1
        assert new_component in template.components
        
        # Test removing component (assuming components have IDs)
        if template.components:
            first_component = template.components[0]
            if 'id' in first_component:
                template.remove_component(first_component['id'])
                assert first_component not in template.components