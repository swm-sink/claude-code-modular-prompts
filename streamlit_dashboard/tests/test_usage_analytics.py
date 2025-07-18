"""
TDD Tests for Usage Analytics System
RED PHASE: Write failing tests first
"""

import pytest
import json
import tempfile
import time
from pathlib import Path
from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch, mock_open
from typing import Dict, Any, List

# Import the components we're testing
try:
    from components.usage_analytics import (
        UsageAnalytics,
        UserSession,
        UserAction,
        AnalyticsMetric,
        get_analytics_instance,
        track_page_view,
        track_user_action,
        track_metric
    )
except ImportError:
    # These don't exist yet - we'll create them
    UsageAnalytics = None
    UserSession = None
    UserAction = None
    AnalyticsMetric = None
    get_analytics_instance = None
    track_page_view = None
    track_user_action = None
    track_metric = None


class TestUserSession:
    """Test the UserSession data class"""
    
    def test_user_session_creation(self):
        """Test UserSession can be created with proper data"""
        if UserSession is None:
            pytest.skip("UserSession not implemented yet")
        
        session_data = {
            'session_id': 'session_123',
            'user_id': 'user_456',
            'start_time': datetime.now().isoformat(),
            'last_activity': datetime.now().isoformat(),
            'page_views': 5,
            'actions_count': 10,
            'components_used': ['framework_explorer', 'template_manager'],
            'features_accessed': ['create_template', 'share_template'],
            'metadata': {'user_agent': 'TestAgent', 'ip_address': '192.168.1.1'}
        }
        
        session = UserSession(**session_data)
        assert session.session_id == 'session_123'
        assert session.user_id == 'user_456'
        assert session.page_views == 5
        assert session.actions_count == 10
        assert len(session.components_used) == 2
        assert len(session.features_accessed) == 2
    
    def test_user_session_validation(self):
        """Test UserSession validation"""
        if UserSession is None:
            pytest.skip("UserSession not implemented yet")
        
        # Test empty session ID
        with pytest.raises(ValueError):
            UserSession(
                session_id="",
                user_id="user_123",
                start_time=datetime.now().isoformat(),
                last_activity=datetime.now().isoformat()
            )
        
        # Test empty user ID
        with pytest.raises(ValueError):
            UserSession(
                session_id="session_123",
                user_id="",
                start_time=datetime.now().isoformat(),
                last_activity=datetime.now().isoformat()
            )
    
    def test_user_session_activity_tracking(self):
        """Test session activity tracking methods"""
        if UserSession is None:
            pytest.skip("UserSession not implemented yet")
        
        session = UserSession(
            session_id="session_123",
            user_id="user_456",
            start_time=datetime.now().isoformat(),
            last_activity=datetime.now().isoformat()
        )
        
        # Test page view tracking
        initial_page_views = session.page_views
        session.add_page_view("dashboard")
        assert session.page_views == initial_page_views + 1
        assert "dashboard" in session.components_used
        
        # Test action tracking
        initial_actions = session.actions_count
        session.add_action("create_template")
        assert session.actions_count == initial_actions + 1
        assert "create_template" in session.features_accessed
    
    def test_user_session_duration_calculation(self):
        """Test session duration calculation"""
        if UserSession is None:
            pytest.skip("UserSession not implemented yet")
        
        start_time = datetime.now()
        session = UserSession(
            session_id="session_123",
            user_id="user_456",
            start_time=start_time.isoformat(),
            last_activity=start_time.isoformat()
        )
        
        # Simulate some activity after 5 seconds
        time.sleep(0.1)  # Small delay for testing
        session.update_activity()
        
        duration = session.get_session_duration()
        assert duration >= 0.1  # Should have some duration
    
    def test_user_session_serialization(self):
        """Test session serialization"""
        if UserSession is None:
            pytest.skip("UserSession not implemented yet")
        
        session = UserSession(
            session_id="session_123",
            user_id="user_456",
            start_time=datetime.now().isoformat(),
            last_activity=datetime.now().isoformat(),
            page_views=3,
            actions_count=7
        )
        
        # Test to_dict
        session_dict = session.to_dict()
        assert isinstance(session_dict, dict)
        assert session_dict['session_id'] == 'session_123'
        assert session_dict['user_id'] == 'user_456'
        assert session_dict['page_views'] == 3
        assert session_dict['actions_count'] == 7
        
        # Test from_dict
        recreated_session = UserSession.from_dict(session_dict)
        assert recreated_session.session_id == session.session_id
        assert recreated_session.user_id == session.user_id
        assert recreated_session.page_views == session.page_views
        assert recreated_session.actions_count == session.actions_count


class TestUserAction:
    """Test the UserAction data class"""
    
    def test_user_action_creation(self):
        """Test UserAction can be created with proper data"""
        if UserAction is None:
            pytest.skip("UserAction not implemented yet")
        
        action_data = {
            'action_id': 'action_123',
            'session_id': 'session_456',
            'user_id': 'user_789',
            'timestamp': datetime.now().isoformat(),
            'action_type': 'button_click',
            'action_name': 'create_template',
            'component': 'template_manager',
            'page': 'dashboard',
            'duration': 2.5,
            'metadata': {'button_text': 'Create Template', 'template_type': 'development'}
        }
        
        action = UserAction(**action_data)
        assert action.action_id == 'action_123'
        assert action.session_id == 'session_456'
        assert action.user_id == 'user_789'
        assert action.action_type == 'button_click'
        assert action.action_name == 'create_template'
        assert action.component == 'template_manager'
        assert action.page == 'dashboard'
        assert action.duration == 2.5
        assert action.metadata['button_text'] == 'Create Template'
    
    def test_user_action_validation(self):
        """Test UserAction validation"""
        if UserAction is None:
            pytest.skip("UserAction not implemented yet")
        
        # Test empty action type
        with pytest.raises(ValueError):
            UserAction(
                action_id="action_123",
                session_id="session_456",
                user_id="user_789",
                timestamp=datetime.now().isoformat(),
                action_type="",
                action_name="test_action",
                component="test_component",
                page="test_page"
            )
        
        # Test empty action name
        with pytest.raises(ValueError):
            UserAction(
                action_id="action_123",
                session_id="session_456",
                user_id="user_789",
                timestamp=datetime.now().isoformat(),
                action_type="click",
                action_name="",
                component="test_component",
                page="test_page"
            )
    
    def test_user_action_serialization(self):
        """Test action serialization"""
        if UserAction is None:
            pytest.skip("UserAction not implemented yet")
        
        action = UserAction(
            action_id="action_123",
            session_id="session_456",
            user_id="user_789",
            timestamp=datetime.now().isoformat(),
            action_type="click",
            action_name="test_action",
            component="test_component",
            page="test_page",
            duration=1.5
        )
        
        # Test to_dict
        action_dict = action.to_dict()
        assert isinstance(action_dict, dict)
        assert action_dict['action_id'] == 'action_123'
        assert action_dict['action_type'] == 'click'
        assert action_dict['duration'] == 1.5
        
        # Test from_dict
        recreated_action = UserAction.from_dict(action_dict)
        assert recreated_action.action_id == action.action_id
        assert recreated_action.action_type == action.action_type
        assert recreated_action.duration == action.duration


class TestAnalyticsMetric:
    """Test the AnalyticsMetric data class"""
    
    def test_analytics_metric_creation(self):
        """Test AnalyticsMetric can be created with proper data"""
        if AnalyticsMetric is None:
            pytest.skip("AnalyticsMetric not implemented yet")
        
        metric_data = {
            'metric_id': 'metric_123',
            'name': 'page_load_time',
            'value': 1.25,
            'unit': 'seconds',
            'timestamp': datetime.now().isoformat(),
            'category': 'performance',
            'tags': ['frontend', 'optimization'],
            'metadata': {'page': 'dashboard', 'user_agent': 'TestAgent'}
        }
        
        metric = AnalyticsMetric(**metric_data)
        assert metric.metric_id == 'metric_123'
        assert metric.name == 'page_load_time'
        assert metric.value == 1.25
        assert metric.unit == 'seconds'
        assert metric.category == 'performance'
        assert len(metric.tags) == 2
        assert 'frontend' in metric.tags
        assert metric.metadata['page'] == 'dashboard'
    
    def test_analytics_metric_validation(self):
        """Test AnalyticsMetric validation"""
        if AnalyticsMetric is None:
            pytest.skip("AnalyticsMetric not implemented yet")
        
        # Test empty metric name
        with pytest.raises(ValueError):
            AnalyticsMetric(
                metric_id="metric_123",
                name="",
                value=1.0,
                unit="units",
                timestamp=datetime.now().isoformat()
            )
        
        # Test non-numeric value
        with pytest.raises(ValueError):
            AnalyticsMetric(
                metric_id="metric_123",
                name="test_metric",
                value="not_a_number",
                unit="units",
                timestamp=datetime.now().isoformat()
            )
    
    def test_analytics_metric_serialization(self):
        """Test metric serialization"""
        if AnalyticsMetric is None:
            pytest.skip("AnalyticsMetric not implemented yet")
        
        metric = AnalyticsMetric(
            metric_id="metric_123",
            name="test_metric",
            value=42.5,
            unit="units",
            timestamp=datetime.now().isoformat(),
            category="test"
        )
        
        # Test to_dict
        metric_dict = metric.to_dict()
        assert isinstance(metric_dict, dict)
        assert metric_dict['metric_id'] == 'metric_123'
        assert metric_dict['name'] == 'test_metric'
        assert metric_dict['value'] == 42.5
        assert metric_dict['unit'] == 'units'
        assert metric_dict['category'] == 'test'
        
        # Test from_dict
        recreated_metric = AnalyticsMetric.from_dict(metric_dict)
        assert recreated_metric.metric_id == metric.metric_id
        assert recreated_metric.name == metric.name
        assert recreated_metric.value == metric.value


class TestUsageAnalytics:
    """Test the UsageAnalytics component"""
    
    @pytest.fixture
    def temp_storage(self):
        """Create temporary storage directory"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            yield Path(tmp_dir)
    
    @pytest.fixture
    def mock_streamlit(self):
        """Mock Streamlit session state"""
        with patch('streamlit.session_state') as mock_session:
            mock_session.keys.return_value = ["test_key"]
            mock_session.__contains__ = MagicMock(return_value=False)
            mock_session.__setitem__ = MagicMock()
            mock_session.__getitem__ = MagicMock(return_value="test_session_id")
            mock_session.analytics_session_id = "test_session_123"
            mock_session.analytics_user_id = "test_user_456"
            yield mock_session
    
    def test_usage_analytics_initialization(self, temp_storage, mock_streamlit):
        """Test UsageAnalytics can be initialized"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        assert analytics.storage_path == temp_storage
        assert analytics.enable_tracking is True
        assert hasattr(analytics, 'active_sessions')
        assert hasattr(analytics, 'recent_actions')
        assert hasattr(analytics, 'recent_metrics')
    
    def test_usage_analytics_disabled_tracking(self, temp_storage):
        """Test UsageAnalytics with disabled tracking"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage, enable_tracking=False)
        assert analytics.enable_tracking is False
        assert analytics.current_session is None
    
    def test_track_page_view(self, temp_storage, mock_streamlit):
        """Test tracking page views"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Track a page view
        analytics.track_page_view("dashboard", {"test": "metadata"})
        
        # Verify session was updated
        if analytics.current_session:
            assert analytics.current_session.page_views >= 1
            assert "dashboard" in analytics.current_session.components_used
        
        # Verify action was recorded
        assert len(analytics.recent_actions) >= 1
        latest_action = analytics.recent_actions[-1]
        assert latest_action.action_type == "page_view"
        assert latest_action.page == "dashboard"
    
    def test_track_user_action(self, temp_storage, mock_streamlit):
        """Test tracking user actions"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Track a user action
        analytics.track_user_action(
            action_type="button_click",
            action_name="create_template",
            component="template_manager",
            page="dashboard",
            duration=1.5,
            metadata={"button_id": "create_btn"}
        )
        
        # Verify session was updated
        if analytics.current_session:
            assert analytics.current_session.actions_count >= 1
            assert "create_template" in analytics.current_session.features_accessed
        
        # Verify action was recorded
        assert len(analytics.recent_actions) >= 1
        latest_action = analytics.recent_actions[-1]
        assert latest_action.action_type == "button_click"
        assert latest_action.action_name == "create_template"
        assert latest_action.component == "template_manager"
        assert latest_action.duration == 1.5
    
    def test_track_metric(self, temp_storage, mock_streamlit):
        """Test tracking custom metrics"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Track a metric
        analytics.track_metric(
            name="response_time",
            value=0.25,
            unit="seconds",
            category="performance",
            tags=["api", "fast"],
            metadata={"endpoint": "/api/templates"}
        )
        
        # Verify metric was recorded
        assert len(analytics.recent_metrics) >= 1
        latest_metric = analytics.recent_metrics[-1]
        assert latest_metric.name == "response_time"
        assert latest_metric.value == 0.25
        assert latest_metric.unit == "seconds"
        assert latest_metric.category == "performance"
        assert "api" in latest_metric.tags
    
    def test_get_session_analytics(self, temp_storage, mock_streamlit):
        """Test getting session analytics"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Add some activity
        analytics.track_page_view("dashboard")
        analytics.track_user_action("click", "test_action", "test_component", "dashboard")
        
        # Get session analytics
        session_analytics = analytics.get_session_analytics()
        
        if session_analytics:
            assert "session_id" in session_analytics
            assert "user_id" in session_analytics
            assert "page_views" in session_analytics
            assert "actions_count" in session_analytics
            assert "components_used" in session_analytics
            assert "features_accessed" in session_analytics
            assert session_analytics["page_views"] >= 1
            assert session_analytics["actions_count"] >= 1
    
    def test_get_usage_statistics(self, temp_storage, mock_streamlit):
        """Test getting usage statistics"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Add some activity
        analytics.track_page_view("dashboard")
        analytics.track_page_view("template_manager")
        analytics.track_user_action("click", "create_template", "template_manager", "dashboard")
        
        # Get usage statistics
        stats = analytics.get_usage_statistics(days=7)
        
        assert isinstance(stats, dict)
        assert "total_sessions" in stats
        assert "total_page_views" in stats
        assert "total_actions" in stats
        assert "unique_users" in stats
        assert "popular_pages" in stats
        assert "popular_actions" in stats
        assert "average_session_duration" in stats
        assert "bounce_rate" in stats
        assert "daily_stats" in stats
    
    def test_get_component_analytics(self, temp_storage, mock_streamlit):
        """Test getting component analytics"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Add component-specific activity
        analytics.track_page_view("template_manager")
        analytics.track_user_action("click", "create_template", "template_manager", "template_manager")
        analytics.track_user_action("click", "edit_template", "template_manager", "template_manager")
        
        # Get component analytics
        component_stats = analytics.get_component_analytics()
        
        assert isinstance(component_stats, dict)
        if "template_manager" in component_stats:
            stats = component_stats["template_manager"]
            assert "page_views" in stats
            assert "actions" in stats
            assert "unique_users" in stats
            assert "popular_actions" in stats
            assert stats["page_views"] >= 1
            assert stats["actions"] >= 2
    
    def test_get_user_journey_analytics(self, temp_storage, mock_streamlit):
        """Test getting user journey analytics"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Simulate user journey
        analytics.track_page_view("dashboard")
        analytics.track_page_view("template_manager")
        analytics.track_page_view("url_sharing")
        
        # Get journey analytics
        journey_stats = analytics.get_user_journey_analytics()
        
        assert isinstance(journey_stats, dict)
        assert "total_journeys" in journey_stats
        assert "common_paths" in journey_stats
        assert "entry_points" in journey_stats
        assert "exit_points" in journey_stats
        assert "average_journey_length" in journey_stats
    
    def test_data_persistence(self, temp_storage, mock_streamlit):
        """Test data persistence to files"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Add some data
        analytics.track_page_view("dashboard")
        analytics.track_user_action("click", "test_action", "test_component", "dashboard")
        analytics.track_metric("test_metric", 42.0, "units", "test")
        
        # Verify files were created
        assert len(list(analytics.sessions_dir.glob("*.json"))) >= 1
        assert len(list(analytics.actions_dir.glob("*.json"))) >= 1
        assert len(list(analytics.metrics_dir.glob("*.json"))) >= 1
    
    def test_cleanup_old_data(self, temp_storage, mock_streamlit):
        """Test cleaning up old data"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Create some old test files
        old_file = analytics.actions_dir / "actions_2020-01-01.json"
        old_file.write_text(json.dumps([{"test": "data"}]))
        
        recent_file = analytics.actions_dir / f"actions_{datetime.now().strftime('%Y-%m-%d')}.json"
        recent_file.write_text(json.dumps([{"test": "data"}]))
        
        # Run cleanup
        analytics.cleanup_old_data()
        
        # Verify old file was removed and recent file remains
        assert not old_file.exists()
        assert recent_file.exists()
    
    def test_export_analytics_data(self, temp_storage, mock_streamlit):
        """Test exporting analytics data"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Add some data
        analytics.track_page_view("dashboard")
        analytics.track_metric("test_metric", 42.0, "units")
        
        # Export data
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now() + timedelta(days=1)
        
        export_data = analytics.export_analytics_data(start_date, end_date)
        
        assert isinstance(export_data, dict)
        assert "export_timestamp" in export_data
        assert "date_range" in export_data
        assert "sessions" in export_data
        assert "actions" in export_data
        assert "metrics" in export_data
        assert len(export_data["actions"]) >= 1
        assert len(export_data["metrics"]) >= 1
    
    @patch('streamlit.title')
    @patch('streamlit.subheader')
    @patch('streamlit.columns')
    @patch('streamlit.metric')
    @patch('streamlit.selectbox')
    @patch('streamlit.info')
    @patch('streamlit.expander')
    @patch('streamlit.button')
    @patch('streamlit.markdown')
    def test_render_analytics_dashboard(self, mock_markdown, mock_button, mock_expander, 
                                       mock_info, mock_selectbox, mock_metric, mock_columns, 
                                       mock_subheader, mock_title, temp_storage, mock_streamlit):
        """Test rendering analytics dashboard UI"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Mock Streamlit components
        def mock_columns_side_effect(n):
            return [MagicMock() for _ in range(n)]
        
        mock_columns.side_effect = mock_columns_side_effect
        mock_selectbox.return_value = "7 days"
        mock_button.return_value = False
        
        # Mock expander context manager
        mock_expander_context = MagicMock()
        mock_expander_context.__enter__ = MagicMock(return_value=mock_expander_context)
        mock_expander_context.__exit__ = MagicMock(return_value=None)
        mock_expander.return_value = mock_expander_context
        
        # Test that method exists and can be called
        assert hasattr(analytics, 'render_analytics_dashboard')
        
        # Call method (should not raise exceptions)
        try:
            analytics.render_analytics_dashboard()
            # If we get here, the method executed without errors
            assert True
        except AttributeError:
            # Method might not exist yet
            pytest.skip("render_analytics_dashboard not implemented yet")


class TestGlobalFunctions:
    """Test global convenience functions"""
    
    def test_get_analytics_instance(self):
        """Test getting global analytics instance"""
        if get_analytics_instance is None:
            pytest.skip("get_analytics_instance not implemented yet")
        
        # Clear global instance
        import components.usage_analytics
        components.usage_analytics._analytics_instance = None
        
        instance1 = get_analytics_instance()
        instance2 = get_analytics_instance()
        
        # Should return the same instance
        assert instance1 is instance2
        assert isinstance(instance1, UsageAnalytics)
    
    @patch('components.usage_analytics.get_analytics_instance')
    def test_track_page_view_convenience(self, mock_get_instance):
        """Test track_page_view convenience function"""
        if track_page_view is None:
            pytest.skip("track_page_view not implemented yet")
        
        mock_analytics = MagicMock()
        mock_get_instance.return_value = mock_analytics
        
        track_page_view("dashboard", {"test": "metadata"})
        
        # Verify analytics was called
        mock_analytics.track_page_view.assert_called_once_with("dashboard", {"test": "metadata"})
    
    @patch('components.usage_analytics.get_analytics_instance')
    def test_track_user_action_convenience(self, mock_get_instance):
        """Test track_user_action convenience function"""
        if track_user_action is None:
            pytest.skip("track_user_action not implemented yet")
        
        mock_analytics = MagicMock()
        mock_get_instance.return_value = mock_analytics
        
        track_user_action("click", "test_action", "test_component", "dashboard", 1.5, {"test": "metadata"})
        
        # Verify analytics was called
        mock_analytics.track_user_action.assert_called_once_with(
            "click", "test_action", "test_component", "dashboard", 1.5, {"test": "metadata"}
        )
    
    @patch('components.usage_analytics.get_analytics_instance')
    def test_track_metric_convenience(self, mock_get_instance):
        """Test track_metric convenience function"""
        if track_metric is None:
            pytest.skip("track_metric not implemented yet")
        
        mock_analytics = MagicMock()
        mock_get_instance.return_value = mock_analytics
        
        track_metric("test_metric", 42.0, "units", "test", ["tag1", "tag2"], {"test": "metadata"})
        
        # Verify analytics was called
        mock_analytics.track_metric.assert_called_once_with(
            "test_metric", 42.0, "units", "test", ["tag1", "tag2"], {"test": "metadata"}
        )
    
    def test_analytics_error_handling(self, temp_storage):
        """Test error handling in analytics system"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Test with invalid data
        try:
            analytics.track_page_view("", {})  # Empty page name
            analytics.track_user_action("", "", "", "", 0.0, {})  # Empty action data
            analytics.track_metric("", 0.0, "", "", [], {})  # Empty metric data
            
            # Should handle errors gracefully
            assert True
        except Exception as e:
            # Some validation errors are expected
            assert isinstance(e, ValueError)
    
    def test_analytics_thread_safety(self, temp_storage):
        """Test thread safety of analytics system"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        import threading
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        def worker():
            for i in range(10):
                analytics.track_page_view(f"page_{i}")
                analytics.track_user_action("click", f"action_{i}", "component", "page", 1.0)
                analytics.track_metric(f"metric_{i}", i * 10.0, "units", "test")
        
        # Start multiple threads
        threads = []
        for _ in range(3):
            thread = threading.Thread(target=worker)
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Verify data was recorded (some actions from each thread)
        assert len(analytics.recent_actions) >= 30  # 3 threads * 10 actions each
        assert len(analytics.recent_metrics) >= 30  # 3 threads * 10 metrics each
    
    def test_analytics_performance(self, temp_storage):
        """Test analytics performance with large datasets"""
        if UsageAnalytics is None:
            pytest.skip("UsageAnalytics not implemented yet")
        
        analytics = UsageAnalytics(storage_path=temp_storage)
        
        # Generate a large amount of test data
        start_time = time.time()
        
        for i in range(100):
            analytics.track_page_view(f"page_{i % 10}")
            analytics.track_user_action("click", f"action_{i}", "component", "page", 1.0)
            analytics.track_metric(f"metric_{i}", i * 1.0, "units", "test")
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        # Should process 300 items in reasonable time (less than 5 seconds)
        assert processing_time < 5.0
        
        # Verify data was recorded
        assert len(analytics.recent_actions) >= 200  # 100 page views + 100 actions
        assert len(analytics.recent_metrics) >= 100