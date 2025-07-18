"""
Routing Simulator Component for Claude Code Modular Prompts Framework
Provides interactive command routing simulation, decision tree visualization, and routing analytics
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from typing import Dict, List, Any, Optional
import re
import json
from datetime import datetime, timedelta
import random


class RoutingSimulator:
    """Component for simulating and analyzing command routing decisions"""
    
    def __init__(self, framework_path: Path):
        """Initialize Routing Simulator with framework path"""
        self.framework_path = framework_path
        self.commands = self.load_commands()
        self.routing_patterns = self.load_routing_patterns()
        self.decision_tree = self.get_decision_tree_data()
        self.simulation_history = []
    
    def load_commands(self) -> Dict[str, Any]:
        """Load all commands from the framework"""
        commands = {}
        commands_dir = self.framework_path / "commands"
        
        if commands_dir.exists():
            for command_file in commands_dir.glob("*.md"):
                command_info = self.parse_command_info(command_file)
                if command_info:
                    commands[command_info['name']] = command_info
        
        return commands
    
    def parse_command_info(self, command_path: Path) -> Dict[str, Any]:
        """Parse command information from file"""
        if not command_path.exists():
            return {}
        
        content = command_path.read_text()
        name = command_path.stem
        
        # Extract purpose
        purpose = ""
        purpose_match = re.search(r'##?\s*Purpose\s*\n+(.*?)(?:\n\n|##)', content, re.IGNORECASE | re.DOTALL)
        if purpose_match:
            purpose = purpose_match.group(1).strip()
        
        # Extract criteria
        criteria = []
        criteria_match = re.search(r'##?\s*Criteria\s*\n+(.*?)(?:\n\n|##)', content, re.IGNORECASE | re.DOTALL)
        if criteria_match:
            criteria_text = criteria_match.group(1)
            criteria = [line.strip("- ").strip() for line in criteria_text.split('\n') if line.strip().startswith('-')]
        
        # Extract examples
        examples = []
        examples_match = re.search(r'##?\s*Examples?\s*\n+(.*?)(?:\n\n|##|$)', content, re.IGNORECASE | re.DOTALL)
        if examples_match:
            examples_text = examples_match.group(1)
            examples = [line.strip("- ").strip() for line in examples_text.split('\n') if line.strip().startswith('-')]
        
        return {
            'name': name,
            'purpose': purpose,
            'criteria': criteria,
            'examples': examples,
            'content': content
        }
    
    def load_routing_patterns(self) -> List[Dict[str, Any]]:
        """Load routing patterns from modules"""
        patterns = []
        patterns_dir = self.framework_path / "modules" / "patterns"
        
        if patterns_dir.exists():
            for pattern_file in patterns_dir.glob("*routing*.md"):
                pattern_content = pattern_file.read_text()
                patterns.append({
                    'name': pattern_file.stem,
                    'content': pattern_content
                })
        
        return patterns
    
    def analyze_request_complexity(self, request: str) -> Dict[str, Any]:
        """Analyze the complexity of a user request"""
        # Simple complexity scoring based on keywords and length
        complexity_indicators = {
            'high': ['system', 'architecture', 'authentication', 'database', 'API', 'integration', 'multiple', 'complete'],
            'medium': ['feature', 'component', 'functionality', 'interface', 'module'],
            'low': ['fix', 'bug', 'typo', 'update', 'small', 'simple']
        }
        
        request_lower = request.lower()
        score = 0
        factors = []
        
        # Check for complexity indicators
        for level, keywords in complexity_indicators.items():
            for keyword in keywords:
                if keyword in request_lower:
                    if level == 'high':
                        score += 3
                        factors.append(f"High complexity: '{keyword}'")
                    elif level == 'medium':
                        score += 2
                        factors.append(f"Medium complexity: '{keyword}'")
                    else:
                        score += 1
                        factors.append(f"Low complexity: '{keyword}'")
        
        # Length factor
        if len(request.split()) > 10:
            score += 2
            factors.append("Long description suggests complexity")
        
        # Estimate components
        component_indicators = ['and', ',', 'with', 'including', 'plus']
        estimated_components = 1
        for indicator in component_indicators:
            estimated_components += request_lower.count(indicator)
        
        return {
            'complexity_score': score,
            'factors': factors,
            'estimated_components': estimated_components,
            'word_count': len(request.split())
        }
    
    def predict_optimal_command(self, request: str) -> Dict[str, Any]:
        """Predict the optimal command for a request"""
        analysis = self.analyze_request_complexity(request)
        request_lower = request.lower()
        
        # Simple rule-based routing
        if any(word in request_lower for word in ['how', 'what', 'why', 'explain', 'understand']):
            command = 'query'
            confidence = 85
            reasoning = "Question words detected - research/analysis needed"
        elif analysis['complexity_score'] <= 3:
            command = 'task'
            confidence = 80
            reasoning = "Low complexity - suitable for focused task"
        elif analysis['estimated_components'] >= 3:
            command = 'swarm'
            confidence = 75
            reasoning = "Multiple components detected - coordination needed"
        elif analysis['complexity_score'] >= 8:
            command = 'feature'
            confidence = 85
            reasoning = "High complexity - full feature development required"
        else:
            command = 'auto'
            confidence = 60
            reasoning = "Unclear requirements - intelligent routing recommended"
        
        return {
            'recommended_command': command,
            'confidence': confidence,
            'reasoning': reasoning,
            'analysis': analysis
        }
    
    def simulate_routing_decision(self, request: str) -> Dict[str, Any]:
        """Simulate a complete routing decision"""
        analysis = self.analyze_request_complexity(request)
        recommendation = self.predict_optimal_command(request)
        alternatives = self.get_alternative_commands(request)
        
        # Create decision path
        decision_path = [
            "1. Analyze request complexity",
            f"2. Complexity score: {analysis['complexity_score']}",
            f"3. Component estimate: {analysis['estimated_components']}",
            f"4. Route to: /{recommendation['recommended_command']}",
            f"5. Confidence: {recommendation['confidence']}%"
        ]
        
        simulation = {
            'request': request,
            'analysis': analysis,
            'recommendation': recommendation,
            'alternatives': alternatives,
            'decision_path': decision_path,
            'timestamp': datetime.now().isoformat()
        }
        
        # Store in history
        self.simulation_history.append(simulation)
        
        return simulation
    
    def get_decision_tree_data(self) -> Dict[str, Any]:
        """Get decision tree visualization data"""
        nodes = [
            {'id': 'start', 'label': 'User Request', 'level': 0, 'type': 'start'},
            {'id': 'analyze', 'label': 'Analyze Complexity', 'level': 1, 'type': 'process'},
            {'id': 'question', 'label': 'Question?', 'level': 2, 'type': 'decision'},
            {'id': 'simple', 'label': 'Simple Task?', 'level': 2, 'type': 'decision'},
            {'id': 'complex', 'label': 'Complex Feature?', 'level': 2, 'type': 'decision'},
            {'id': 'multipart', 'label': 'Multiple Components?', 'level': 2, 'type': 'decision'},
            {'id': 'query', 'label': '/query', 'level': 3, 'type': 'command'},
            {'id': 'task', 'label': '/task', 'level': 3, 'type': 'command'},
            {'id': 'feature', 'label': '/feature', 'level': 3, 'type': 'command'},
            {'id': 'swarm', 'label': '/swarm', 'level': 3, 'type': 'command'},
            {'id': 'auto', 'label': '/auto', 'level': 3, 'type': 'command'}
        ]
        
        edges = [
            {'from': 'start', 'to': 'analyze'},
            {'from': 'analyze', 'to': 'question'},
            {'from': 'analyze', 'to': 'simple'},
            {'from': 'analyze', 'to': 'complex'},
            {'from': 'analyze', 'to': 'multipart'},
            {'from': 'question', 'to': 'query', 'label': 'Yes'},
            {'from': 'simple', 'to': 'task', 'label': 'Yes'},
            {'from': 'complex', 'to': 'feature', 'label': 'Yes'},
            {'from': 'multipart', 'to': 'swarm', 'label': 'Yes'},
            {'from': 'simple', 'to': 'auto', 'label': 'Unclear'}
        ]
        
        return {'nodes': nodes, 'edges': edges}
    
    def get_routing_statistics(self) -> Dict[str, Any]:
        """Get routing statistics from simulation history"""
        if not self.simulation_history:
            return {
                'total_simulations': 0,
                'command_distribution': {},
                'average_confidence': 0
            }
        
        total = len(self.simulation_history)
        commands = [sim['recommendation']['recommended_command'] for sim in self.simulation_history]
        confidences = [sim['recommendation']['confidence'] for sim in self.simulation_history]
        
        # Count command distribution
        command_counts = {}
        for cmd in commands:
            command_counts[cmd] = command_counts.get(cmd, 0) + 1
        
        return {
            'total_simulations': total,
            'command_distribution': command_counts,
            'average_confidence': sum(confidences) / len(confidences) if confidences else 0
        }
    
    def render_simulation_input(self):
        """Render simulation input interface"""
        st.subheader("🎯 Request Simulator")
        
        # Sample requests for quick testing
        sample_requests = [
            "Fix bug in login function",
            "Build complete user authentication system",
            "How does the routing algorithm work?",
            "Create dashboard with multiple charts",
            "Add OAuth integration to existing API"
        ]
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            request = st.text_input(
                "Enter your request:",
                placeholder="Describe what you want to accomplish...",
                key="routing_request"
            )
        
        with col2:
            if st.button("🎲 Random", help="Try a random sample request"):
                sample_request = random.choice(sample_requests)
                st.session_state.routing_request = sample_request
                st.rerun()
        
        # Quick samples
        st.write("**Quick samples:**")
        cols = st.columns(len(sample_requests))
        for i, sample in enumerate(sample_requests):
            with cols[i]:
                if st.button(f"📝 {sample[:20]}...", key=f"sample_{i}"):
                    st.session_state.routing_request = sample
                    st.rerun()
        
        if st.button("🔍 Analyze Request", type="primary") and request:
            simulation = self.simulate_routing_decision(request)
            
            # Display results
            st.success(f"**Recommended Command:** `/{simulation['recommendation']['recommended_command']}`")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Confidence", f"{simulation['recommendation']['confidence']}%")
                
            with col2:
                st.metric("Complexity Score", simulation['analysis']['complexity_score'])
            
            # Show reasoning
            st.info(f"**Reasoning:** {simulation['recommendation']['reasoning']}")
            
            # Show decision path
            with st.expander("Decision Path"):
                for step in simulation['decision_path']:
                    st.write(f"• {step}")
            
            # Show alternatives
            if simulation['alternatives']:
                with st.expander("Alternative Commands"):
                    for alt in simulation['alternatives']:
                        st.write(f"• **/{alt['command']}**: {alt['reason']}")
    
    def render_decision_tree_visualization(self):
        """Render decision tree visualization"""
        st.subheader("🌳 Decision Tree")
        
        tree_data = self.decision_tree
        
        # Create a simplified tree visualization using plotly
        fig = go.Figure()
        
        # Add nodes
        for node in tree_data['nodes']:
            color = {
                'start': '#4CAF50',
                'process': '#2196F3', 
                'decision': '#FF9800',
                'command': '#9C27B0'
            }.get(node['type'], '#666666')
            
            fig.add_trace(go.Scatter(
                x=[node['level']],
                y=[hash(node['id']) % 100],  # Simple positioning
                mode='markers+text',
                marker=dict(size=20, color=color),
                text=node['label'],
                textposition="middle center",
                name=node['type'].title(),
                showlegend=False
            ))
        
        fig.update_layout(
            title="Command Routing Decision Tree",
            xaxis_title="Decision Level",
            yaxis_title="",
            yaxis=dict(showticklabels=False),
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def render_routing_metrics(self):
        """Render routing metrics"""
        stats = self.get_routing_statistics()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Simulations", stats['total_simulations'])
        
        with col2:
            st.metric("Average Confidence", f"{stats['average_confidence']:.1f}%")
        
        with col3:
            most_used = max(stats['command_distribution'].items(), key=lambda x: x[1]) if stats['command_distribution'] else ('none', 0)
            st.metric("Most Used Command", f"/{most_used[0]}" if most_used[0] != 'none' else 'N/A')
        
        # Command distribution chart
        if stats['command_distribution']:
            fig = px.pie(
                values=list(stats['command_distribution'].values()),
                names=[f"/{cmd}" for cmd in stats['command_distribution'].keys()],
                title="Command Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    def validate_routing_logic(self) -> Dict[str, Any]:
        """Validate routing logic"""
        issues = []
        recommendations = []
        
        # Check if all commands are covered
        if len(self.commands) < 4:
            issues.append("Insufficient command coverage")
            recommendations.append("Add more command definitions")
        
        # Check routing patterns
        if not self.routing_patterns:
            issues.append("No routing patterns defined")
            recommendations.append("Define routing patterns in modules/patterns/")
        
        return {
            'is_valid': len(issues) == 0,
            'issues': issues,
            'recommendations': recommendations
        }
    
    def export_routing_rules(self, file_path: Path) -> bool:
        """Export routing rules to file"""
        try:
            rules = {
                'commands': self.commands,
                'patterns': self.routing_patterns,
                'decision_tree': self.decision_tree,
                'timestamp': datetime.now().isoformat()
            }
            
            with open(file_path, 'w') as f:
                json.dump(rules, f, indent=2)
            
            return True
        except Exception:
            return False
    
    def get_alternative_commands(self, request: str) -> List[Dict[str, str]]:
        """Get alternative command suggestions"""
        alternatives = []
        request_lower = request.lower()
        
        # Simple rule-based alternatives
        if 'bug' in request_lower or 'fix' in request_lower:
            alternatives.append({'command': 'task', 'reason': 'Simple bug fixes'})
            alternatives.append({'command': 'query', 'reason': 'Research the issue first'})
        
        if 'system' in request_lower or 'architecture' in request_lower:
            alternatives.append({'command': 'feature', 'reason': 'Complex system changes'})
            alternatives.append({'command': 'swarm', 'reason': 'Multi-component coordination'})
        
        if not alternatives:
            alternatives.append({'command': 'auto', 'reason': 'Let intelligent routing decide'})
        
        return alternatives
    
    def calculate_routing_accuracy(self, test_cases: List[Dict[str, str]]) -> float:
        """Calculate routing accuracy from test cases"""
        if not test_cases:
            return 0.0
        
        correct = sum(1 for case in test_cases if case['predicted'] == case['actual'])
        return (correct / len(test_cases)) * 100
    
    def get_command_usage_trends(self, days: int = 7) -> pd.DataFrame:
        """Get command usage trends"""
        # Generate sample trend data
        dates = [datetime.now() - timedelta(days=i) for i in range(days)]
        commands = ['task', 'feature', 'query', 'swarm', 'auto']
        
        trend_data = []
        for date in dates:
            for command in commands:
                usage_count = random.randint(0, 10)
                trend_data.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'command': command,
                    'usage_count': usage_count
                })
        
        return pd.DataFrame(trend_data)
    
    def render(self):
        """Main render method for the component"""
        st.title("🎯 Routing Simulator")
        st.markdown("Test and analyze command routing decisions")
        
        tabs = st.tabs(["🎯 Simulator", "🌳 Decision Tree", "📊 Analytics", "⚙️ Configuration"])
        
        with tabs[0]:
            self.render_simulation_input()
        
        with tabs[1]:
            self.render_decision_tree_visualization()
            
            # Show routing logic validation
            st.divider()
            validation = self.validate_routing_logic()
            
            if validation['is_valid']:
                st.success("✅ Routing logic is valid")
            else:
                st.warning("⚠️ Routing logic has issues:")
                for issue in validation['issues']:
                    st.write(f"• {issue}")
                
                st.info("Recommendations:")
                for rec in validation['recommendations']:
                    st.write(f"• {rec}")
        
        with tabs[2]:
            st.subheader("Routing Analytics")
            self.render_routing_metrics()
            
            # Usage trends
            trends = self.get_command_usage_trends()
            if not trends.empty:
                st.subheader("Command Usage Trends (7 days)")
                fig = px.line(
                    trends,
                    x='date',
                    y='usage_count',
                    color='command',
                    title="Command Usage Over Time"
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with tabs[3]:
            st.subheader("Configuration")
            
            # Export functionality
            if st.button("📋 Export Routing Rules", type="secondary"):
                export_path = Path("routing_rules.json")
                if self.export_routing_rules(export_path):
                    st.success(f"Routing rules exported to {export_path}")
                else:
                    st.error("Failed to export routing rules")
            
            # Show current commands
            st.subheader("Available Commands")
            for cmd_name, cmd_info in self.commands.items():
                with st.expander(f"/{cmd_name}"):
                    st.write(f"**Purpose:** {cmd_info['purpose']}")
                    if cmd_info['criteria']:
                        st.write("**Criteria:**")
                        for criterion in cmd_info['criteria']:
                            st.write(f"• {criterion}")
                    if cmd_info['examples']:
                        st.write("**Examples:**")
                        for example in cmd_info['examples']:
                            st.write(f"• {example}")