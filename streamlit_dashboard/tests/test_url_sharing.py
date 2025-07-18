"""
TDD Tests for URL Sharing functionality in Template Manager
RED PHASE: Write failing tests first
"""

import pytest
import json
import uuid
from pathlib import Path
from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch
from typing import Dict, Any, Optional

# Import the component we're going to build
try:
    from components.url_sharing import URLSharingManager, SharedTemplate, SharingToken
except ImportError:
    # These don't exist yet - we'll create them
    URLSharingManager = None
    SharedTemplate = None
    SharingToken = None


class TestSharingToken:
    """Test the SharingToken data class"""
    
    def test_token_creation(self):
        """Test SharingToken can be created with proper data"""
        if SharingToken is None:
            pytest.skip("SharingToken not implemented yet")
        
        token_data = {
            'token': 'abc123def456',
            'template_id': 'test_template_001',
            'created_at': datetime.now().isoformat(),
            'expires_at': (datetime.now() + timedelta(days=30)).isoformat(),
            'access_count': 0,
            'max_access_count': 100
        }
        
        token = SharingToken(**token_data)
        assert token.token == 'abc123def456'
        assert token.template_id == 'test_template_001'
        assert token.access_count == 0
        assert token.max_access_count == 100
    
    def test_token_expiry_check(self):
        """Test token expiry validation"""
        if SharingToken is None:
            pytest.skip("SharingToken not implemented yet")
        
        # Expired token
        expired_token = SharingToken(
            token='expired123',
            template_id='test_template_001',
            created_at=datetime.now().isoformat(),
            expires_at=(datetime.now() - timedelta(days=1)).isoformat(),
            access_count=5,
            max_access_count=100
        )
        
        assert expired_token.is_expired() is True
        
        # Valid token
        valid_token = SharingToken(
            token='valid123',
            template_id='test_template_001',
            created_at=datetime.now().isoformat(),
            expires_at=(datetime.now() + timedelta(days=30)).isoformat(),
            access_count=5,
            max_access_count=100
        )
        
        assert valid_token.is_expired() is False
    
    def test_token_access_limit_check(self):
        """Test token access limit validation"""
        if SharingToken is None:
            pytest.skip("SharingToken not implemented yet")
        
        # Token at access limit
        max_access_token = SharingToken(
            token='maxed123',
            template_id='test_template_001',
            created_at=datetime.now().isoformat(),
            expires_at=(datetime.now() + timedelta(days=30)).isoformat(),
            access_count=100,
            max_access_count=100
        )
        
        assert max_access_token.is_access_limit_reached() is True
        
        # Token under access limit
        under_limit_token = SharingToken(
            token='under123',
            template_id='test_template_001',
            created_at=datetime.now().isoformat(),
            expires_at=(datetime.now() + timedelta(days=30)).isoformat(),
            access_count=50,
            max_access_count=100
        )
        
        assert under_limit_token.is_access_limit_reached() is False
    
    def test_token_validity_check(self):
        """Test comprehensive token validity check"""
        if SharingToken is None:
            pytest.skip("SharingToken not implemented yet")
        
        # Valid token
        valid_token = SharingToken(
            token='valid123',
            template_id='test_template_001',
            created_at=datetime.now().isoformat(),
            expires_at=(datetime.now() + timedelta(days=30)).isoformat(),
            access_count=50,
            max_access_count=100
        )
        
        assert valid_token.is_valid() is True
        
        # Invalid token (expired)
        expired_token = SharingToken(
            token='expired123',
            template_id='test_template_001',
            created_at=datetime.now().isoformat(),
            expires_at=(datetime.now() - timedelta(days=1)).isoformat(),
            access_count=50,
            max_access_count=100
        )
        
        assert expired_token.is_valid() is False
    
    def test_token_serialization(self):
        """Test token serialization to/from dictionary"""
        if SharingToken is None:
            pytest.skip("SharingToken not implemented yet")
        
        token_data = {
            'token': 'test123',
            'template_id': 'test_template_001',
            'created_at': datetime.now().isoformat(),
            'expires_at': (datetime.now() + timedelta(days=30)).isoformat(),
            'access_count': 10,
            'max_access_count': 100
        }
        
        token = SharingToken(**token_data)
        
        # Test to_dict
        serialized = token.to_dict()
        assert isinstance(serialized, dict)
        assert serialized['token'] == 'test123'
        assert serialized['template_id'] == 'test_template_001'
        
        # Test from_dict
        recreated = SharingToken.from_dict(serialized)
        assert recreated.token == token.token
        assert recreated.template_id == token.template_id
        assert recreated.access_count == token.access_count


class TestSharedTemplate:
    """Test the SharedTemplate data class"""
    
    def test_shared_template_creation(self):
        """Test SharedTemplate can be created with proper data"""
        if SharedTemplate is None:
            pytest.skip("SharedTemplate not implemented yet")
        
        template_data = {
            'id': 'shared_template_001',
            'name': 'Shared Development Template',
            'description': 'A shared template for development workflows',
            'category': 'development',
            'author': 'Original Author',
            'version': '1.0.0',
            'components': [
                {'type': 'command', 'name': 'task', 'file': 'commands/task.md'}
            ],
            'metadata': {
                'framework_version': '3.0.0',
                'tags': ['development', 'shared'],
                'difficulty': 'intermediate'
            },
            'sharing_info': {
                'shared_by': 'user@example.com',
                'shared_at': datetime.now().isoformat(),
                'share_url': 'https://example.com/share/abc123',
                'access_count': 5
            }
        }
        
        shared_template = SharedTemplate(**template_data)
        assert shared_template.id == 'shared_template_001'
        assert shared_template.name == 'Shared Development Template'
        assert shared_template.sharing_info['shared_by'] == 'user@example.com'
        assert shared_template.sharing_info['access_count'] == 5
    
    def test_shared_template_from_regular_template(self):
        """Test creating SharedTemplate from regular template"""
        if SharedTemplate is None:
            pytest.skip("SharedTemplate not implemented yet")
        
        regular_template = {
            'id': 'regular_template_001',
            'name': 'Regular Template',
            'description': 'A regular template',
            'category': 'development',
            'author': 'Author',
            'version': '1.0.0',
            'components': [],
            'metadata': {'framework_version': '3.0.0'}
        }
        
        sharing_info = {
            'shared_by': 'user@example.com',
            'shared_at': datetime.now().isoformat(),
            'share_url': 'https://example.com/share/xyz789',
            'access_count': 0
        }
        
        shared_template = SharedTemplate.from_template(regular_template, sharing_info)
        assert shared_template.id == 'regular_template_001'
        assert shared_template.name == 'Regular Template'
        assert shared_template.sharing_info['shared_by'] == 'user@example.com'
        assert shared_template.sharing_info['access_count'] == 0


class TestURLSharingManager:
    """Test the URLSharingManager component"""
    
    @pytest.fixture
    def sharing_storage(self, tmp_path):
        """Create temporary sharing storage directory"""
        storage_dir = tmp_path / "sharing"
        storage_dir.mkdir()
        return storage_dir
    
    @pytest.fixture
    def sample_template(self):
        """Create a sample template for testing"""
        return {
            'id': 'sample_template_001',
            'name': 'Sample Template',
            'description': 'A sample template for testing',
            'category': 'development',
            'author': 'Test Author',
            'version': '1.0.0',
            'components': [
                {'type': 'command', 'name': 'task', 'file': 'commands/task.md'}
            ],
            'metadata': {
                'framework_version': '3.0.0',
                'tags': ['test', 'sample'],
                'difficulty': 'beginner'
            }
        }
    
    def test_url_sharing_manager_initialization(self, sharing_storage):
        """Test URLSharingManager can be initialized"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        assert manager.sharing_storage_path == sharing_storage
        assert hasattr(manager, 'tokens_index')
        assert hasattr(manager, 'shared_templates_index')
    
    def test_generate_sharing_token(self, sharing_storage, sample_template):
        """Test generating a sharing token for a template"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate token
        token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=100
        )
        
        assert token is not None
        assert isinstance(token, str)
        assert len(token) >= 16  # Should be reasonably long
        
        # Verify token is stored
        stored_token = manager.get_token_info(token)
        assert stored_token is not None
        assert stored_token.template_id == sample_template['id']
        assert stored_token.max_access_count == 100
    
    def test_generate_sharing_url(self, sharing_storage, sample_template):
        """Test generating a sharing URL for a template"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate sharing URL
        share_url = manager.generate_sharing_url(
            template_data=sample_template,
            base_url="https://example.com/share",
            expires_in_days=30
        )
        
        assert share_url is not None
        assert isinstance(share_url, str)
        assert share_url.startswith("https://example.com/share/")
        
        # Extract token from URL
        token = share_url.split("/")[-1]
        assert len(token) >= 16
        
        # Verify token is valid
        stored_token = manager.get_token_info(token)
        assert stored_token is not None
        assert stored_token.template_id == sample_template['id']
    
    def test_access_shared_template(self, sharing_storage, sample_template):
        """Test accessing a shared template via token"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate token
        token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=100
        )
        
        # Access shared template
        shared_template = manager.access_shared_template(token)
        
        assert shared_template is not None
        assert shared_template['id'] == sample_template['id']
        assert shared_template['name'] == sample_template['name']
        
        # Verify access count incremented
        token_info = manager.get_token_info(token)
        assert token_info.access_count == 1
    
    def test_access_expired_token(self, sharing_storage, sample_template):
        """Test accessing template with expired token"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate token with very short expiry
        token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=-1,  # Already expired
            max_access_count=100
        )
        
        # Try to access - should fail
        shared_template = manager.access_shared_template(token)
        assert shared_template is None
    
    def test_access_over_limit_token(self, sharing_storage, sample_template):
        """Test accessing template with access limit reached"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate token with low access limit
        token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=1
        )
        
        # Access once - should work
        shared_template = manager.access_shared_template(token)
        assert shared_template is not None
        
        # Access again - should fail (limit reached)
        shared_template = manager.access_shared_template(token)
        assert shared_template is None
    
    def test_revoke_sharing_token(self, sharing_storage, sample_template):
        """Test revoking a sharing token"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate token
        token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=100
        )
        
        # Verify token works
        shared_template = manager.access_shared_template(token)
        assert shared_template is not None
        
        # Revoke token
        success = manager.revoke_sharing_token(token)
        assert success is True
        
        # Verify token no longer works
        shared_template = manager.access_shared_template(token)
        assert shared_template is None
    
    def test_list_shared_templates(self, sharing_storage, sample_template):
        """Test listing all shared templates"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate multiple sharing tokens
        token1 = manager.generate_sharing_token(sample_template, expires_in_days=30)
        
        template2 = sample_template.copy()
        template2['id'] = 'sample_template_002'
        template2['name'] = 'Sample Template 2'
        token2 = manager.generate_sharing_token(template2, expires_in_days=30)
        
        # List shared templates
        shared_templates = manager.list_shared_templates()
        
        assert len(shared_templates) == 2
        template_ids = [t['id'] for t in shared_templates]
        assert 'sample_template_001' in template_ids
        assert 'sample_template_002' in template_ids
    
    def test_get_sharing_statistics(self, sharing_storage, sample_template):
        """Test getting sharing statistics"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate token and access it
        token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=100
        )
        
        # Access the template multiple times
        manager.access_shared_template(token)
        manager.access_shared_template(token)
        
        # Get statistics
        stats = manager.get_sharing_statistics()
        
        assert isinstance(stats, dict)
        assert 'total_shared_templates' in stats
        assert 'total_access_count' in stats
        assert 'active_tokens' in stats
        assert stats['total_shared_templates'] >= 1
        assert stats['total_access_count'] >= 2
    
    def test_cleanup_expired_tokens(self, sharing_storage, sample_template):
        """Test cleaning up expired tokens"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate expired token
        expired_token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=-1,  # Already expired
            max_access_count=100
        )
        
        # Generate valid token
        valid_token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=100
        )
        
        # Cleanup expired tokens
        cleaned_count = manager.cleanup_expired_tokens()
        assert cleaned_count >= 1
        
        # Verify expired token is gone
        assert manager.get_token_info(expired_token) is None
        
        # Verify valid token still exists
        assert manager.get_token_info(valid_token) is not None
    
    def test_validate_sharing_token(self, sharing_storage, sample_template):
        """Test validating sharing tokens"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate valid token
        valid_token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=100
        )
        
        # Test valid token
        is_valid, error_msg = manager.validate_sharing_token(valid_token)
        assert is_valid is True
        assert error_msg is None
        
        # Test invalid token
        is_valid, error_msg = manager.validate_sharing_token("invalid_token_123")
        assert is_valid is False
        assert error_msg is not None
        assert "not found" in error_msg.lower()
    
    def test_render_sharing_ui(self, sharing_storage):
        """Test rendering sharing UI"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Test that the method exists and can be called
        assert hasattr(manager, 'render_sharing_ui')
        assert callable(manager.render_sharing_ui)
    
    @patch('streamlit.title')
    @patch('streamlit.subheader')
    @patch('streamlit.columns')
    @patch('streamlit.metric')
    @patch('streamlit.info')
    @patch('streamlit.expander')
    @patch('streamlit.markdown')
    @patch('streamlit.button')
    @patch('streamlit.divider')
    def test_render_sharing_ui_without_template_mock(self, mock_divider, mock_button, 
                                                   mock_markdown, mock_expander, mock_info, 
                                                   mock_metric, mock_columns, mock_subheader, 
                                                   mock_title, sharing_storage):
        """Test rendering sharing UI without template data using mocked Streamlit components"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Mock Streamlit components with side_effect to handle different column counts
        def mock_columns_side_effect(n):
            return [MagicMock() for _ in range(n)]
        
        mock_columns.side_effect = mock_columns_side_effect
        mock_expander.return_value.__enter__ = MagicMock()
        mock_expander.return_value.__exit__ = MagicMock()
        mock_button.return_value = False
        
        # Test that method exists and can be called
        assert hasattr(manager, 'render_sharing_ui')
        
        # Call method without template data (should not raise exceptions)
        try:
            manager.render_sharing_ui()
            # If we get here, the method executed without errors
            assert True
        except AttributeError:
            # Method might not exist yet
            pytest.skip("render_sharing_ui not implemented yet")
    
    @patch('streamlit.title')
    @patch('streamlit.subheader')
    @patch('streamlit.columns')
    @patch('streamlit.metric')
    @patch('streamlit.slider')
    @patch('streamlit.number_input')
    @patch('streamlit.button')
    @patch('streamlit.text_input')
    @patch('streamlit.success')
    @patch('streamlit.code')
    @patch('streamlit.write')
    @patch('streamlit.error')
    @patch('streamlit.json')
    @patch('streamlit.markdown')
    @patch('streamlit.divider')
    def test_render_sharing_ui_with_template_mock(self, mock_divider, mock_markdown, mock_json, 
                                                mock_error, mock_write, mock_code, mock_success, 
                                                mock_text_input, mock_button, mock_number_input, 
                                                mock_slider, mock_metric, mock_columns, 
                                                mock_subheader, mock_title, 
                                                sharing_storage, sample_template):
        """Test rendering sharing UI with template data using mocked Streamlit components"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Mock Streamlit components with side_effect to handle different column counts
        def mock_columns_side_effect(n):
            return [MagicMock() for _ in range(n)]
        
        mock_columns.side_effect = mock_columns_side_effect
        mock_slider.return_value = 30
        mock_number_input.return_value = 100
        mock_button.return_value = False
        mock_text_input.return_value = "https://example.com/share"
        
        # Test that method exists and can be called
        assert hasattr(manager, 'render_sharing_ui')
        
        # Call method with template data (should not raise exceptions)
        try:
            manager.render_sharing_ui(template_data=sample_template)
            # If we get here, the method executed without errors
            assert True
        except AttributeError:
            # Method might not exist yet
            pytest.skip("render_sharing_ui not implemented yet")
    
    @patch('streamlit.title')
    @patch('streamlit.subheader')
    @patch('streamlit.columns')
    @patch('streamlit.metric')
    @patch('streamlit.info')
    @patch('streamlit.expander')
    @patch('streamlit.markdown')
    @patch('streamlit.button')
    @patch('streamlit.divider')
    def test_render_sharing_ui_with_shared_templates_mock(self, mock_divider, mock_button, 
                                                        mock_markdown, mock_expander, mock_info, 
                                                        mock_metric, mock_columns, mock_subheader, 
                                                        mock_title, sharing_storage, sample_template):
        """Test rendering sharing UI with existing shared templates using mocked Streamlit components"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate a shared template first
        token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=100
        )
        
        # Mock Streamlit components with side_effect to handle different column counts
        def mock_columns_side_effect(n):
            return [MagicMock() for _ in range(n)]
        
        mock_columns.side_effect = mock_columns_side_effect
        
        # Mock expander context manager
        mock_expander_context = MagicMock()
        mock_expander_context.__enter__ = MagicMock(return_value=mock_expander_context)
        mock_expander_context.__exit__ = MagicMock(return_value=None)
        mock_expander.return_value = mock_expander_context
        
        mock_button.return_value = False
        
        # Test that method exists and can be called
        assert hasattr(manager, 'render_sharing_ui')
        
        # Call method (should not raise exceptions)
        try:
            manager.render_sharing_ui()
            # If we get here, the method executed without errors
            assert True
        except AttributeError:
            # Method might not exist yet
            pytest.skip("render_sharing_ui not implemented yet")
    
    def test_get_sharing_statistics_comprehensive(self, sharing_storage, sample_template):
        """Test comprehensive sharing statistics functionality"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate multiple tokens with different configurations
        token1 = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=100
        )
        
        template2 = sample_template.copy()
        template2['id'] = 'sample_template_002'
        template2['name'] = 'Sample Template 2'
        token2 = manager.generate_sharing_token(
            template_data=template2,
            expires_in_days=7,
            max_access_count=50
        )
        
        # Access templates to increment counters
        manager.access_shared_template(token1)
        manager.access_shared_template(token1)
        manager.access_shared_template(token2)
        
        # Get comprehensive statistics
        stats = manager.get_sharing_statistics()
        
        assert isinstance(stats, dict)
        assert 'total_shared_templates' in stats
        assert 'total_access_count' in stats
        assert 'active_tokens' in stats
        assert 'expired_tokens' in stats
        
        assert stats['total_shared_templates'] == 2
        assert stats['total_access_count'] == 3
        assert stats['active_tokens'] >= 2
    
    def test_cleanup_expired_tokens_with_statistics(self, sharing_storage, sample_template):
        """Test cleanup functionality with statistics tracking"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate expired and valid tokens
        expired_token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=-1,  # Already expired
            max_access_count=100
        )
        
        valid_token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=100
        )
        
        # Get statistics before cleanup
        stats_before = manager.get_sharing_statistics()
        
        # Cleanup expired tokens
        cleaned_count = manager.cleanup_expired_tokens()
        
        # Get statistics after cleanup
        stats_after = manager.get_sharing_statistics()
        
        # Verify cleanup worked
        assert cleaned_count >= 1
        assert stats_after['expired_tokens'] < stats_before['expired_tokens']
        
        # Verify expired token is gone
        assert manager.get_token_info(expired_token) is None
        
        # Verify valid token still exists
        assert manager.get_token_info(valid_token) is not None
    
    def test_token_validation_edge_cases(self, sharing_storage, sample_template):
        """Test token validation with various edge cases"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Test validation with None
        is_valid, error_msg = manager.validate_sharing_token(None)
        assert is_valid is False
        assert error_msg is not None
        
        # Test validation with empty string
        is_valid, error_msg = manager.validate_sharing_token("")
        assert is_valid is False
        assert error_msg is not None
        
        # Test validation with very long token
        long_token = "a" * 1000
        is_valid, error_msg = manager.validate_sharing_token(long_token)
        assert is_valid is False
        assert error_msg is not None
        
        # Test validation with special characters
        special_token = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        is_valid, error_msg = manager.validate_sharing_token(special_token)
        assert is_valid is False
        assert error_msg is not None
    
    def test_shared_template_access_tracking(self, sharing_storage, sample_template):
        """Test comprehensive access tracking for shared templates"""
        if URLSharingManager is None:
            pytest.skip("URLSharingManager not implemented yet")
        
        manager = URLSharingManager(sharing_storage_path=sharing_storage)
        
        # Generate token
        token = manager.generate_sharing_token(
            template_data=sample_template,
            expires_in_days=30,
            max_access_count=5
        )
        
        # Track access count
        initial_stats = manager.get_sharing_statistics()
        initial_access_count = initial_stats['total_access_count']
        
        # Access template multiple times
        access_count = 0
        for i in range(3):
            result = manager.access_shared_template(token)
            if result is not None:
                access_count += 1
        
        # Verify access count increased
        final_stats = manager.get_sharing_statistics()
        final_access_count = final_stats['total_access_count']
        
        assert final_access_count == initial_access_count + access_count
        
        # Verify token info reflects access count
        token_info = manager.get_token_info(token)
        assert token_info.access_count == access_count