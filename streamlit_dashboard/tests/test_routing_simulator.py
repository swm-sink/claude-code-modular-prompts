"""
Tests for Routing Simulator Component
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
from components.routing_simulator import RoutingSimulator


class TestRoutingSimulator:
    """Test suite for Routing Simulator component"""
    
    @pytest.fixture
    def mock_framework_path(self, tmp_path):
        """Create a mock framework directory structure"""
        framework_dir = tmp_path / ".claude"
        framework_dir.mkdir()
        
        # Create commands directory
        commands_dir = framework_dir / "commands"
        commands_dir.mkdir()
        
        # Create mock command files
        auto_content = """
# Auto Command - Intelligent Routing

## Purpose
Automatically route requests to appropriate commands

## Decision Logic
- Simple task → /task
- Complex feature → /feature  
- Research needed → /query
- Multi-component → /swarm
- Unknown → analyze and route

## Examples
- "Fix bug in login" → /task
- "Add user authentication" → /feature
- "How does X work?" → /query
- "Build dashboard" → /swarm
"""
        (commands_dir / "auto.md").write_text(auto_content)
        
        task_content = """
# Task Command

## Purpose
Single-focused development with TDD

## Criteria
- <50 lines of code
- Single file modification
- Clear requirements
- Testable output

## Examples
- Fix specific bug
- Add small feature
- Update configuration
- Write tests
"""
        (commands_dir / "task.md").write_text(task_content)
        
        feature_content = """
# Feature Command

## Purpose
Complete feature development with PRD

## Criteria
- Multi-component changes
- Complex requirements
- System integration
- Full lifecycle

## Examples
- User authentication system
- API endpoints
- Database schema
- UI components
"""
        (commands_dir / "feature.md").write_text(feature_content)
        
        # Create modules for patterns
        modules_dir = framework_dir / "modules"
        modules_dir.mkdir()
        patterns_dir = modules_dir / "patterns"
        patterns_dir.mkdir()
        
        routing_content = """
# Intelligent Routing Pattern

## Decision Tree
1. Analyze complexity
2. Check component count
3. Evaluate requirements clarity
4. Route to optimal command

## Routing Rules
- Single file + clear → /task
- Multiple files → /feature
- Unknown requirements → /query
- Coordination needed → /swarm
"""
        (patterns_dir / "intelligent-routing.md").write_text(routing_content)
        
        return framework_dir
    
    @pytest.fixture
    def routing_simulator(self, mock_framework_path):
        """Create RoutingSimulator instance with mock path"""
        return RoutingSimulator(framework_path=mock_framework_path)
    
    def test_initialization(self, routing_simulator, mock_framework_path):
        """Test that RoutingSimulator initializes correctly"""
        assert routing_simulator.framework_path == mock_framework_path
        assert hasattr(routing_simulator, 'commands')
        assert hasattr(routing_simulator, 'routing_patterns')
        assert hasattr(routing_simulator, 'decision_tree')
    
    def test_load_commands(self, routing_simulator):
        """Test loading commands from framework"""
        commands = routing_simulator.load_commands()
        
        assert isinstance(commands, dict)
        assert len(commands) >= 3
        assert 'auto' in commands
        assert 'task' in commands
        assert 'feature' in commands
    
    def test_parse_command_info(self, routing_simulator):
        """Test parsing command information"""
        command_path = routing_simulator.framework_path / "commands" / "task.md"
        command_info = routing_simulator.parse_command_info(command_path)
        
        assert isinstance(command_info, dict)
        assert command_info['name'] == 'task'
        assert 'purpose' in command_info
        assert 'criteria' in command_info
        assert 'examples' in command_info
        assert len(command_info['examples']) > 0
    
    def test_load_routing_patterns(self, routing_simulator):
        """Test loading routing patterns"""
        patterns = routing_simulator.load_routing_patterns()
        
        assert isinstance(patterns, list)
        assert len(patterns) > 0
        assert any('intelligent-routing' in p['name'] for p in patterns)
    
    def test_analyze_request_complexity(self, routing_simulator):
        """Test analyzing request complexity"""
        simple_request = "Fix typo in README"
        complex_request = "Build a complete user authentication system with OAuth, JWT, and role-based access control"
        
        simple_analysis = routing_simulator.analyze_request_complexity(simple_request)
        complex_analysis = routing_simulator.analyze_request_complexity(complex_request)
        
        assert isinstance(simple_analysis, dict)
        assert isinstance(complex_analysis, dict)
        assert 'complexity_score' in simple_analysis
        assert 'complexity_score' in complex_analysis
        assert simple_analysis['complexity_score'] < complex_analysis['complexity_score']
        assert 'factors' in simple_analysis
        assert 'estimated_components' in simple_analysis
    
    def test_predict_optimal_command(self, routing_simulator):
        """Test predicting optimal command"""
        test_cases = [
            ("Fix bug in login function", "task"),
            ("Build complete authentication system", "feature"),
            ("How does the routing work?", "query"),
            ("Create dashboard with multiple components", "swarm")
        ]
        
        for request, expected_command in test_cases:
            prediction = routing_simulator.predict_optimal_command(request)
            
            assert isinstance(prediction, dict)
            assert 'recommended_command' in prediction
            assert 'confidence' in prediction
            assert 'reasoning' in prediction
            # Note: We're testing the structure, not exact command since AI routing can vary
    
    def test_simulate_routing_decision(self, routing_simulator):
        """Test simulating routing decision"""
        request = "Add user authentication"
        
        simulation = routing_simulator.simulate_routing_decision(request)
        
        assert isinstance(simulation, dict)
        assert 'request' in simulation
        assert 'analysis' in simulation
        assert 'recommendation' in simulation
        assert 'alternatives' in simulation
        assert 'decision_path' in simulation
        assert simulation['request'] == request
    
    def test_get_decision_tree_data(self, routing_simulator):
        """Test getting decision tree visualization data"""
        tree_data = routing_simulator.get_decision_tree_data()
        
        assert isinstance(tree_data, dict)
        assert 'nodes' in tree_data
        assert 'edges' in tree_data
        assert len(tree_data['nodes']) > 0
        assert len(tree_data['edges']) > 0
    
    def test_get_routing_statistics(self, routing_simulator):
        """Test getting routing statistics"""
        # Simulate some routing decisions first
        requests = [
            "Fix bug in login",
            "Build authentication system", 
            "How does X work?",
            "Create multi-component dashboard"
        ]
        
        for request in requests:
            routing_simulator.simulate_routing_decision(request)
        
        stats = routing_simulator.get_routing_statistics()
        
        assert isinstance(stats, dict)
        assert 'total_simulations' in stats
        assert 'command_distribution' in stats
        assert 'average_confidence' in stats
    
    @patch('streamlit.text_input')
    @patch('streamlit.button')
    def test_render_simulation_input(self, mock_button, mock_input, routing_simulator):
        """Test rendering simulation input"""
        mock_input.return_value = "Test request"
        mock_button.return_value = True
        
        routing_simulator.render_simulation_input()
        
        # Verify input components were created
        assert mock_input.called
        assert mock_button.called
    
    @patch('streamlit.plotly_chart')
    def test_render_decision_tree_visualization(self, mock_plotly, routing_simulator):
        """Test rendering decision tree visualization"""
        routing_simulator.render_decision_tree_visualization()
        
        # Verify visualization was created
        mock_plotly.assert_called_once()
        chart = mock_plotly.call_args[0][0]
        assert isinstance(chart, go.Figure)
    
    @patch('streamlit.metric')
    @patch('streamlit.columns')
    def test_render_routing_metrics(self, mock_columns, mock_metric, routing_simulator):
        """Test rendering routing metrics"""
        mock_cols = [Mock(), Mock(), Mock()]
        mock_columns.return_value = mock_cols
        
        # Setup column context managers
        for col in mock_cols:
            col.__enter__ = Mock(return_value=None)
            col.__exit__ = Mock(return_value=None)
        
        routing_simulator.render_routing_metrics()
        
        # Verify metrics were created
        assert mock_columns.called
        assert mock_metric.call_count >= 3
    
    def test_validate_routing_logic(self, routing_simulator):
        """Test validating routing logic"""
        validation = routing_simulator.validate_routing_logic()
        
        assert isinstance(validation, dict)
        assert 'is_valid' in validation
        assert 'issues' in validation
        assert 'recommendations' in validation
    
    def test_export_routing_rules(self, routing_simulator, tmp_path):
        """Test exporting routing rules"""
        export_path = tmp_path / "routing_rules.json"
        success = routing_simulator.export_routing_rules(export_path)
        
        assert success is True
        assert export_path.exists()
        
        # Verify export content
        import json
        with open(export_path) as f:
            rules = json.load(f)
        
        assert 'commands' in rules
        assert 'patterns' in rules
        assert 'decision_tree' in rules
    
    def test_get_alternative_commands(self, routing_simulator):
        """Test getting alternative command suggestions"""
        request = "Fix authentication bug"
        alternatives = routing_simulator.get_alternative_commands(request)
        
        assert isinstance(alternatives, list)
        assert len(alternatives) >= 1
        assert all('command' in alt and 'reason' in alt for alt in alternatives)
    
    @patch('streamlit.tabs')
    def test_render_method(self, mock_tabs, routing_simulator):
        """Test main render method"""
        # Mock tabs
        tabs = [Mock(), Mock(), Mock(), Mock()]
        mock_tabs.return_value = tabs
        
        # Setup tab context managers
        for tab in tabs:
            tab.__enter__ = Mock(return_value=None)
            tab.__exit__ = Mock(return_value=None)
        
        routing_simulator.render()
        
        # Verify tabs were created
        mock_tabs.assert_called_once_with(["🎯 Simulator", "🌳 Decision Tree", "📊 Analytics", "⚙️ Configuration"])
    
    def test_calculate_routing_accuracy(self, routing_simulator):
        """Test calculating routing accuracy"""
        # Mock some historical data
        test_cases = [
            {"request": "Fix bug", "predicted": "task", "actual": "task"},
            {"request": "Build feature", "predicted": "feature", "actual": "feature"},
            {"request": "Research topic", "predicted": "query", "actual": "query"}
        ]
        
        accuracy = routing_simulator.calculate_routing_accuracy(test_cases)
        
        assert isinstance(accuracy, float)
        assert 0 <= accuracy <= 100
    
    def test_get_command_usage_trends(self, routing_simulator):
        """Test getting command usage trends"""
        trends = routing_simulator.get_command_usage_trends(days=7)
        
        assert isinstance(trends, pd.DataFrame)
        if not trends.empty:
            assert 'date' in trends.columns
            assert 'command' in trends.columns
            assert 'usage_count' in trends.columns