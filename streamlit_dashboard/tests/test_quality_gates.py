"""
Tests for Quality Gates Dashboard Component
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
from components.quality_gates import QualityGatesDashboard


class TestQualityGatesDashboard:
    """Test suite for Quality Gates Dashboard component"""
    
    @pytest.fixture
    def mock_framework_path(self, tmp_path):
        """Create a mock framework directory structure"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create quality gates directory
        system_dir = framework_dir / "system"
        system_dir.mkdir()
        quality_dir = system_dir / "quality"
        quality_dir.mkdir()
        
        # Create mock quality gate files
        tdd_content = """
# TDD Enforcement Gate

## Requirements
- All code must follow RED→GREEN→REFACTOR cycle
- Tests must be written before implementation
- Coverage must be >= 90%

## Enforcement Level
BLOCKING

## Validation
- Check for test files
- Verify tests fail before implementation
- Measure coverage
"""
        (quality_dir / "tdd-enforcement.md").write_text(tdd_content)
        
        coverage_content = """
# Test Coverage Gate

## Threshold
90%

## Tools
- Python: pytest-cov
- JavaScript: jest coverage
- TypeScript: nyc

## Enforcement
BLOCKING - No merge if coverage < 90%
"""
        (quality_dir / "test-coverage.md").write_text(coverage_content)
        
        security_content = """
# Security Standards Gate

## Requirements
- No hardcoded secrets
- Threat modeling required
- Security scan must pass

## Severity Levels
- CRITICAL: Block immediately
- HIGH: Block before production
- MEDIUM: Fix within sprint
- LOW: Track in backlog
"""
        (quality_dir / "security-standards.md").write_text(security_content)
        
        return framework_dir
    
    @pytest.fixture
    def quality_dashboard(self, mock_framework_path):
        """Create QualityGatesDashboard instance with mock path"""
        return QualityGatesDashboard(framework_path=mock_framework_path)
    
    def test_initialization(self, quality_dashboard, mock_framework_path):
        """Test that QualityGatesDashboard initializes correctly"""
        assert quality_dashboard.framework_path == mock_framework_path
        assert hasattr(quality_dashboard, 'quality_gates')
        assert hasattr(quality_dashboard, 'enforcement_stats')
        assert hasattr(quality_dashboard, 'violation_history')
    
    def test_load_quality_gates(self, quality_dashboard):
        """Test loading quality gates from framework"""
        gates = quality_dashboard.load_quality_gates()
        
        assert isinstance(gates, list)
        assert len(gates) >= 3
        assert any(gate['name'] == 'tdd-enforcement' for gate in gates)
        assert any(gate['name'] == 'test-coverage' for gate in gates)
        assert any(gate['name'] == 'security-standards' for gate in gates)
    
    def test_parse_quality_gate(self, quality_dashboard):
        """Test parsing individual quality gate"""
        gate_path = quality_dashboard.framework_path / "system" / "quality" / "tdd-enforcement.md"
        gate_info = quality_dashboard.parse_quality_gate(gate_path)
        
        assert isinstance(gate_info, dict)
        assert gate_info['name'] == 'tdd-enforcement'
        assert 'requirements' in gate_info
        assert 'enforcement_level' in gate_info
        assert gate_info['enforcement_level'] == 'BLOCKING'
    
    def test_calculate_enforcement_stats(self, quality_dashboard):
        """Test calculating enforcement statistics"""
        gates = quality_dashboard.load_quality_gates()
        stats = quality_dashboard.calculate_enforcement_stats(gates)
        
        assert isinstance(stats, dict)
        assert 'total_gates' in stats
        assert 'blocking_gates' in stats
        assert 'active_gates' in stats
        assert 'enforcement_rate' in stats
        assert stats['total_gates'] >= 3
    
    def test_get_gate_status(self, quality_dashboard):
        """Test getting current status of a quality gate"""
        status = quality_dashboard.get_gate_status('tdd-enforcement')
        
        assert isinstance(status, dict)
        assert 'is_active' in status
        assert 'last_check' in status
        assert 'pass_rate' in status
        assert 'violations' in status
    
    def test_simulate_gate_check(self, quality_dashboard):
        """Test simulating a quality gate check"""
        result = quality_dashboard.simulate_gate_check(
            gate_name='test-coverage',
            test_value=85,
            threshold=90
        )
        
        assert isinstance(result, dict)
        assert result['passed'] is False
        assert result['gate_name'] == 'test-coverage'
        assert result['actual_value'] == 85
        assert result['required_value'] == 90
        assert 'message' in result
    
    def test_get_violation_trends(self, quality_dashboard):
        """Test getting violation trend data"""
        trends = quality_dashboard.get_violation_trends(days=7)
        
        assert isinstance(trends, pd.DataFrame)
        assert 'date' in trends.columns
        assert 'violations' in trends.columns
        assert 'gate_name' in trends.columns
    
    def test_get_enforcement_matrix(self, quality_dashboard):
        """Test getting enforcement matrix data"""
        matrix = quality_dashboard.get_enforcement_matrix()
        
        assert isinstance(matrix, pd.DataFrame)
        assert len(matrix) > 0
        assert 'gate_name' in matrix.columns
        assert 'enforcement_level' in matrix.columns
        assert 'pass_rate' in matrix.columns
    
    @patch('streamlit.columns')
    @patch('streamlit.metric')
    def test_render_enforcement_overview(self, mock_metric, mock_columns, quality_dashboard):
        """Test rendering enforcement overview"""
        mock_cols = [Mock(), Mock(), Mock(), Mock()]
        mock_columns.return_value = mock_cols
        
        # Setup column context managers
        for col in mock_cols:
            col.__enter__ = Mock(return_value=None)
            col.__exit__ = Mock(return_value=None)
        
        quality_dashboard.render_enforcement_overview()
        
        # Verify metrics were created
        assert mock_columns.called
        assert mock_metric.call_count >= 4
    
    @patch('streamlit.plotly_chart')
    def test_render_violation_trends_chart(self, mock_plotly, quality_dashboard):
        """Test rendering violation trends chart"""
        quality_dashboard.render_violation_trends_chart()
        
        # Verify chart was created
        mock_plotly.assert_called_once()
        chart_config = mock_plotly.call_args[0][0]
        assert isinstance(chart_config, go.Figure)
    
    @patch('streamlit.dataframe')
    def test_render_gate_details_table(self, mock_dataframe, quality_dashboard):
        """Test rendering gate details table"""
        quality_dashboard.render_gate_details_table()
        
        # Verify dataframe was rendered
        mock_dataframe.assert_called_once()
        df = mock_dataframe.call_args[0][0]
        assert isinstance(df, pd.DataFrame)
    
    @patch('streamlit.select_slider')
    @patch('streamlit.button')
    def test_render_gate_simulator(self, mock_button, mock_slider, quality_dashboard):
        """Test rendering gate simulator"""
        mock_slider.return_value = 85
        mock_button.return_value = True
        
        quality_dashboard.render_gate_simulator()
        
        # Verify simulator UI was created
        assert mock_slider.called
        assert mock_button.called
    
    def test_export_enforcement_report(self, quality_dashboard, tmp_path):
        """Test exporting enforcement report"""
        report_path = tmp_path / "enforcement_report.json"
        success = quality_dashboard.export_enforcement_report(report_path)
        
        assert success is True
        assert report_path.exists()
        
        # Verify report content
        import json
        with open(report_path) as f:
            report = json.load(f)
        
        assert 'timestamp' in report
        assert 'gates' in report
        assert 'statistics' in report
        assert 'violations' in report
    
    def test_get_recommended_actions(self, quality_dashboard):
        """Test getting recommended actions for violations"""
        violations = [
            {'gate': 'test-coverage', 'value': 85, 'threshold': 90},
            {'gate': 'security-standards', 'severity': 'HIGH'}
        ]
        
        actions = quality_dashboard.get_recommended_actions(violations)
        
        assert isinstance(actions, list)
        assert len(actions) >= 2
        assert all('action' in a and 'priority' in a for a in actions)
    
    @patch('streamlit.tabs')
    def test_render_method(self, mock_tabs, quality_dashboard):
        """Test main render method"""
        # Mock tabs
        tabs = [Mock(), Mock(), Mock(), Mock()]
        mock_tabs.return_value = tabs
        
        # Setup tab context managers
        for tab in tabs:
            tab.__enter__ = Mock(return_value=None)
            tab.__exit__ = Mock(return_value=None)
        
        quality_dashboard.render()
        
        # Verify tabs were created
        mock_tabs.assert_called_once_with(["📊 Overview", "📈 Trends", "🔍 Details", "🧪 Simulator"])
    
    def test_calculate_compliance_score(self, quality_dashboard):
        """Test calculating overall compliance score"""
        score = quality_dashboard.calculate_compliance_score()
        
        assert isinstance(score, float)
        assert 0 <= score <= 100
    
    def test_get_gate_dependencies(self, quality_dashboard):
        """Test getting dependencies between quality gates"""
        deps = quality_dashboard.get_gate_dependencies()
        
        assert isinstance(deps, dict)
        # TDD gate might depend on test coverage gate
        if 'tdd-enforcement' in deps:
            assert isinstance(deps['tdd-enforcement'], list)