"""
Tests for Meta Framework Control Panel Component
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
from components.meta_framework import MetaFrameworkControlPanel


class TestMetaFrameworkControlPanel:
    """Test suite for Meta Framework Control Panel component"""
    
    @pytest.fixture
    def mock_framework_path(self, tmp_path):
        """Create a mock framework directory structure"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create meta directory
        meta_dir = framework_dir / "meta"
        meta_dir.mkdir()
        
        # Create learning data
        learning_dir = meta_dir / "learning"
        learning_dir.mkdir()
        
        # Create performance data
        perf_data = {
            "token_efficiency": [0.8, 0.85, 0.9],
            "response_time": [1.2, 1.0, 0.8],
            "user_satisfaction": [8.5, 8.8, 9.1]
        }
        
        import json
        (learning_dir / "performance_metrics.json").write_text(json.dumps(perf_data))
        
        # Create optimization history
        optimization_history = [
            {"date": "2025-07-15", "type": "token_optimization", "improvement": 15},
            {"date": "2025-07-16", "type": "context_optimization", "improvement": 10},
            {"date": "2025-07-17", "type": "parallel_execution", "improvement": 25}
        ]
        
        (meta_dir / "optimization_history.json").write_text(json.dumps(optimization_history))
        
        return framework_dir
    
    @pytest.fixture
    def meta_panel(self, mock_framework_path):
        """Create MetaFrameworkControlPanel instance with mock path"""
        return MetaFrameworkControlPanel(framework_path=mock_framework_path)
    
    def test_initialization(self, meta_panel, mock_framework_path):
        """Test that MetaFrameworkControlPanel initializes correctly"""
        assert meta_panel.framework_path == mock_framework_path
        assert hasattr(meta_panel, 'performance_metrics')
        assert hasattr(meta_panel, 'optimization_history')
        assert hasattr(meta_panel, 'learning_data')
    
    def test_load_performance_metrics(self, meta_panel):
        """Test loading performance metrics"""
        metrics = meta_panel.load_performance_metrics()
        
        assert isinstance(metrics, dict)
        assert 'token_efficiency' in metrics
        assert 'response_time' in metrics
        assert 'user_satisfaction' in metrics
        assert len(metrics['token_efficiency']) == 3
    
    def test_get_framework_health_score(self, meta_panel):
        """Test calculating framework health score"""
        health_score = meta_panel.get_framework_health_score()
        
        assert isinstance(health_score, float)
        assert 0 <= health_score <= 100
    
    def test_analyze_usage_patterns(self, meta_panel):
        """Test analyzing usage patterns"""
        patterns = meta_panel.analyze_usage_patterns()
        
        assert isinstance(patterns, dict)
        assert 'most_used_commands' in patterns
        assert 'peak_usage_times' in patterns
        assert 'efficiency_trends' in patterns
    
    def test_get_optimization_recommendations(self, meta_panel):
        """Test getting optimization recommendations"""
        recommendations = meta_panel.get_optimization_recommendations()
        
        assert isinstance(recommendations, list)
        assert len(recommendations) > 0
        assert all('priority' in rec and 'description' in rec for rec in recommendations)
    
    def test_simulate_framework_evolution(self, meta_panel):
        """Test simulating framework evolution"""
        evolution = meta_panel.simulate_framework_evolution(days_ahead=30)
        
        assert isinstance(evolution, dict)
        assert 'predicted_improvements' in evolution
        assert 'risk_factors' in evolution
        assert 'confidence_score' in evolution
        assert 0 <= evolution['confidence_score'] <= 100
    
    def test_get_module_usage_analytics(self, meta_panel):
        """Test getting module usage analytics"""
        analytics = meta_panel.get_module_usage_analytics()
        
        assert isinstance(analytics, pd.DataFrame)
        if not analytics.empty:
            assert 'module_name' in analytics.columns
            assert 'usage_count' in analytics.columns
            assert 'efficiency_score' in analytics.columns
    
    def test_calculate_roi_metrics(self, meta_panel):
        """Test calculating ROI metrics"""
        roi = meta_panel.calculate_roi_metrics()
        
        assert isinstance(roi, dict)
        assert 'time_saved' in roi
        assert 'efficiency_gain' in roi
        assert 'cost_reduction' in roi
    
    @patch('streamlit.metric')
    @patch('streamlit.columns')
    def test_render_performance_dashboard(self, mock_columns, mock_metric, meta_panel):
        """Test rendering performance dashboard"""
        mock_cols = [Mock(), Mock(), Mock(), Mock()]
        mock_columns.return_value = mock_cols
        
        # Setup column context managers
        for col in mock_cols:
            col.__enter__ = Mock(return_value=None)
            col.__exit__ = Mock(return_value=None)
        
        meta_panel.render_performance_dashboard()
        
        # Verify metrics were created
        assert mock_columns.called
        assert mock_metric.call_count >= 4
    
    @patch('streamlit.plotly_chart')
    def test_render_evolution_timeline(self, mock_plotly, meta_panel):
        """Test rendering evolution timeline"""
        meta_panel.render_evolution_timeline()
        
        # Verify chart was created
        mock_plotly.assert_called_once()
        chart = mock_plotly.call_args[0][0]
        assert isinstance(chart, go.Figure)
    
    def test_export_meta_analysis(self, meta_panel, tmp_path):
        """Test exporting meta analysis"""
        export_path = tmp_path / "meta_analysis.json"
        success = meta_panel.export_meta_analysis(export_path)
        
        assert success is True
        assert export_path.exists()
        
        # Verify export content
        import json
        with open(export_path) as f:
            analysis = json.load(f)
        
        assert 'performance_metrics' in analysis
        assert 'optimization_history' in analysis
        assert 'recommendations' in analysis
    
    def test_predict_performance_trends(self, meta_panel):
        """Test predicting performance trends"""
        trends = meta_panel.predict_performance_trends(weeks_ahead=4)
        
        assert isinstance(trends, dict)
        assert 'token_efficiency' in trends
        assert 'response_time' in trends
        assert 'projected_improvements' in trends
    
    def test_get_framework_version_comparison(self, meta_panel):
        """Test getting framework version comparison"""
        comparison = meta_panel.get_framework_version_comparison()
        
        assert isinstance(comparison, dict)
        assert 'current_version' in comparison
        assert 'performance_delta' in comparison
        assert 'feature_additions' in comparison
    
    @patch('streamlit.selectbox')
    @patch('streamlit.button')
    def test_render_optimization_controls(self, mock_button, mock_selectbox, meta_panel):
        """Test rendering optimization controls"""
        mock_selectbox.return_value = "token_optimization"
        mock_button.return_value = True
        
        meta_panel.render_optimization_controls()
        
        # Verify controls were created
        assert mock_selectbox.called
        assert mock_button.called
    
    def test_validate_framework_integrity(self, meta_panel):
        """Test validating framework integrity"""
        validation = meta_panel.validate_framework_integrity()
        
        assert isinstance(validation, dict)
        assert 'is_valid' in validation
        assert 'issues' in validation
        assert 'recommendations' in validation
    
    def test_get_learning_insights(self, meta_panel):
        """Test getting learning insights"""
        insights = meta_panel.get_learning_insights()
        
        assert isinstance(insights, list)
        assert all('insight' in item and 'confidence' in item for item in insights)
    
    @patch('streamlit.tabs')
    def test_render_method(self, mock_tabs, meta_panel):
        """Test main render method"""
        # Mock tabs
        tabs = [Mock(), Mock(), Mock(), Mock()]
        mock_tabs.return_value = tabs
        
        # Setup tab context managers
        for tab in tabs:
            tab.__enter__ = Mock(return_value=None)
            tab.__exit__ = Mock(return_value=None)
        
        meta_panel.render()
        
        # Verify tabs were created
        mock_tabs.assert_called_once_with(["🌟 Overview", "📈 Performance", "🔮 Evolution", "⚙️ Control"])
    
    def test_calculate_optimization_impact(self, meta_panel):
        """Test calculating optimization impact"""
        impact = meta_panel.calculate_optimization_impact("token_optimization")
        
        assert isinstance(impact, dict)
        assert 'improvement_percentage' in impact
        assert 'affected_components' in impact
        assert 'time_to_implement' in impact
    
    def test_get_competitive_benchmarks(self, meta_panel):
        """Test getting competitive benchmarks"""
        benchmarks = meta_panel.get_competitive_benchmarks()
        
        assert isinstance(benchmarks, dict)
        assert 'industry_average' in benchmarks
        assert 'framework_score' in benchmarks
        assert 'ranking' in benchmarks