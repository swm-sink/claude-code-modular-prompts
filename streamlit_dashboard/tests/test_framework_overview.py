"""
Tests for Framework Overview Component
Following TDD approach - writing tests first
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import sys
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Add the streamlit_dashboard directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the component we're going to build
from components.framework_overview import FrameworkOverview


class TestFrameworkOverview:
    """Test suite for Framework Overview component"""
    
    @pytest.fixture
    def mock_framework_path(self, tmp_path):
        """Create a mock framework directory structure"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create mock directory structure
        (framework_dir / "commands").mkdir()
        (framework_dir / "modules").mkdir()
        (framework_dir / "modules" / "patterns").mkdir()
        (framework_dir / "modules" / "development").mkdir()
        (framework_dir / "modules" / "meta").mkdir()
        (framework_dir / "system").mkdir()
        (framework_dir / "system" / "quality").mkdir()
        
        # Create some mock files
        (framework_dir / "commands" / "auto.md").write_text("# Auto command")
        (framework_dir / "commands" / "task.md").write_text("# Task command")
        (framework_dir / "modules" / "patterns" / "tdd-cycle.md").write_text("# TDD pattern")
        (framework_dir / "system" / "quality" / "gates.md").write_text("# Quality gates")
        
        return framework_dir
    
    @pytest.fixture
    def framework_overview(self, mock_framework_path):
        """Create FrameworkOverview instance with mock path"""
        return FrameworkOverview(framework_path=mock_framework_path)
    
    def test_initialization(self, framework_overview, mock_framework_path):
        """Test that FrameworkOverview initializes correctly"""
        assert framework_overview.framework_path == mock_framework_path
        assert hasattr(framework_overview, 'statistics')
        assert hasattr(framework_overview, 'architecture_data')
    
    def test_collect_statistics(self, framework_overview):
        """Test framework statistics collection"""
        stats = framework_overview.collect_statistics()
        
        assert isinstance(stats, dict)
        assert 'total_commands' in stats
        assert 'total_modules' in stats
        assert 'module_categories' in stats
        assert 'quality_gates' in stats
        assert 'framework_version' in stats
        assert 'last_updated' in stats
        
        # Check values
        assert stats['total_commands'] == 2  # auto.md and task.md
        assert stats['total_modules'] >= 1  # At least tdd-cycle.md
        assert isinstance(stats['module_categories'], dict)
        assert 'patterns' in stats['module_categories']
    
    def test_analyze_architecture(self, framework_overview):
        """Test framework architecture analysis"""
        arch_data = framework_overview.analyze_architecture()
        
        assert isinstance(arch_data, dict)
        assert 'command_module_mappings' in arch_data
        assert 'module_dependencies' in arch_data
        assert 'quality_gate_coverage' in arch_data
        assert 'architectural_patterns' in arch_data
    
    @patch('streamlit.title')
    @patch('streamlit.metric')
    @patch('streamlit.columns')
    def test_render_statistics_dashboard(self, mock_columns, mock_metric, mock_title, framework_overview):
        """Test statistics dashboard rendering"""
        # Mock columns behavior
        mock_col1, mock_col2, mock_col3, mock_col4 = Mock(), Mock(), Mock(), Mock()
        mock_columns.return_value = [mock_col1, mock_col2, mock_col3, mock_col4]
        
        # Setup column context managers
        for col in [mock_col1, mock_col2, mock_col3, mock_col4]:
            col.__enter__ = Mock(return_value=None)
            col.__exit__ = Mock(return_value=None)
        
        framework_overview.render_statistics_dashboard()
        
        # Verify title was called
        mock_title.assert_called_once()
        
        # Verify metrics were displayed
        assert mock_metric.call_count >= 4  # At least 4 metrics
    
    def test_create_architecture_visualization(self, framework_overview):
        """Test architecture visualization creation"""
        fig = framework_overview.create_architecture_visualization()
        
        assert isinstance(fig, go.Figure)
        assert len(fig.data) > 0  # Should have at least one trace
        assert fig.layout.title.text is not None
    
    def test_create_module_distribution_chart(self, framework_overview):
        """Test module distribution chart creation"""
        fig = framework_overview.create_module_distribution_chart()
        
        assert isinstance(fig, go.Figure)
        assert len(fig.data) > 0
        # Should be a pie or bar chart showing module categories
    
    def test_create_quality_metrics_chart(self, framework_overview):
        """Test quality metrics chart creation"""
        fig = framework_overview.create_quality_metrics_chart()
        
        assert isinstance(fig, go.Figure)
        assert len(fig.data) > 0
        # Should show quality gate compliance metrics
    
    @patch('streamlit.tabs')
    @patch('streamlit.plotly_chart')
    def test_render_method(self, mock_plotly_chart, mock_tabs, framework_overview):
        """Test main render method"""
        # Mock tabs
        mock_tab1, mock_tab2, mock_tab3, mock_tab4 = Mock(), Mock(), Mock(), Mock()
        mock_tabs.return_value = [mock_tab1, mock_tab2, mock_tab3, mock_tab4]
        
        # Setup tab context managers
        for tab in [mock_tab1, mock_tab2, mock_tab3, mock_tab4]:
            tab.__enter__ = Mock(return_value=None)
            tab.__exit__ = Mock(return_value=None)
        
        framework_overview.render()
        
        # Verify tabs were created
        mock_tabs.assert_called_once_with(["📊 Statistics", "🏗️ Architecture", "📈 Metrics", "🔄 Recent Changes"])
        
        # Verify charts were rendered
        assert mock_plotly_chart.call_count >= 3  # At least 3 charts
    
    def test_get_recent_changes(self, framework_overview):
        """Test recent changes detection"""
        changes = framework_overview.get_recent_changes(days=7)
        
        assert isinstance(changes, list)
        # Each change should have file, type, and timestamp
        for change in changes:
            assert 'file' in change
            assert 'type' in change
            assert 'timestamp' in change
    
    def test_calculate_framework_health_score(self, framework_overview):
        """Test framework health score calculation"""
        score = framework_overview.calculate_framework_health_score()
        
        assert isinstance(score, dict)
        assert 'overall_score' in score
        assert 'test_coverage' in score
        assert 'documentation_completeness' in score
        assert 'module_consistency' in score
        
        # Score should be between 0 and 100
        assert 0 <= score['overall_score'] <= 100
    
    def test_export_framework_report(self, framework_overview, tmp_path):
        """Test framework report export functionality"""
        report_path = tmp_path / "framework_report.json"
        
        success = framework_overview.export_framework_report(report_path)
        
        assert success is True
        assert report_path.exists()
        
        # Verify report content
        import json
        with open(report_path) as f:
            report = json.load(f)
        
        assert 'statistics' in report
        assert 'architecture' in report
        assert 'health_score' in report
        assert 'timestamp' in report