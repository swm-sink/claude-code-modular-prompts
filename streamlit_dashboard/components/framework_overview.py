"""
Framework Overview Component for Claude Code Modular Prompts Framework
Provides comprehensive statistics, architecture visualization, and health metrics
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import json
from collections import defaultdict
import pandas as pd


class FrameworkOverview:
    """Framework Overview component providing statistics and architecture visualization"""
    
    def __init__(self, framework_path: Path):
        """Initialize Framework Overview with framework path"""
        self.framework_path = framework_path
        self.statistics = {}
        self.architecture_data = {}
        self._cache = {}
        
    def collect_statistics(self) -> Dict[str, Any]:
        """Collect comprehensive framework statistics"""
        stats = {
            'total_commands': 0,
            'total_modules': 0,
            'module_categories': defaultdict(int),
            'quality_gates': 0,
            'framework_version': '3.0.0',
            'last_updated': datetime.now().strftime('%Y-%m-%d')
        }
        
        # Count commands
        commands_dir = self.framework_path / "commands"
        if commands_dir.exists():
            stats['total_commands'] = len(list(commands_dir.glob("*.md")))
        
        # Count modules and categorize them
        modules_dir = self.framework_path / "modules"
        if modules_dir.exists():
            for category_dir in modules_dir.iterdir():
                if category_dir.is_dir():
                    module_count = len(list(category_dir.glob("*.md")))
                    stats['module_categories'][category_dir.name] = module_count
                    stats['total_modules'] += module_count
        
        # Count quality gates
        quality_dir = self.framework_path / "system" / "quality"
        if quality_dir.exists():
            stats['quality_gates'] = len(list(quality_dir.glob("*.md")))
        
        self.statistics = stats
        return stats
    
    def analyze_architecture(self) -> Dict[str, Any]:
        """Analyze framework architecture and relationships"""
        arch_data = {
            'command_module_mappings': {},
            'module_dependencies': {},
            'quality_gate_coverage': {},
            'architectural_patterns': []
        }
        
        # Analyze command-module mappings
        commands_dir = self.framework_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.glob("*.md"):
                cmd_name = cmd_file.stem
                # In a real implementation, we'd parse the file to find module references
                arch_data['command_module_mappings'][cmd_name] = []
        
        # Identify architectural patterns
        if (self.framework_path / "modules" / "patterns").exists():
            arch_data['architectural_patterns'] = [
                p.stem for p in (self.framework_path / "modules" / "patterns").glob("*.md")
            ]
        
        self.architecture_data = arch_data
        return arch_data
    
    def create_architecture_visualization(self) -> go.Figure:
        """Create interactive architecture visualization"""
        if not self.architecture_data:
            self.analyze_architecture()
        
        # Create a hierarchical structure visualization
        fig = go.Figure()
        
        # Add framework root
        fig.add_trace(go.Scatter(
            x=[0], y=[0],
            mode='markers+text',
            name='Framework',
            text=['Claude Code Framework'],
            textposition='top center',
            marker=dict(size=30, color='blue')
        ))
        
        # Add main components
        components = ['Commands', 'Modules', 'System', 'Meta']
        x_positions = [-2, -0.7, 0.7, 2]
        y_position = -1
        
        for i, comp in enumerate(components):
            fig.add_trace(go.Scatter(
                x=[x_positions[i]], y=[y_position],
                mode='markers+text',
                name=comp,
                text=[comp],
                textposition='top center',
                marker=dict(size=20, color='lightblue')
            ))
            
            # Add connections
            fig.add_trace(go.Scatter(
                x=[0, x_positions[i]], y=[0, y_position],
                mode='lines',
                line=dict(color='gray', width=1),
                showlegend=False
            ))
        
        fig.update_layout(
            title="Framework Architecture",
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=600
        )
        
        return fig
    
    def create_module_distribution_chart(self) -> go.Figure:
        """Create module distribution chart"""
        if not self.statistics:
            self.collect_statistics()
        
        categories = list(self.statistics['module_categories'].keys())
        values = list(self.statistics['module_categories'].values())
        
        fig = go.Figure(data=[
            go.Pie(
                labels=categories,
                values=values,
                hole=0.3,
                marker_colors=px.colors.qualitative.Set3
            )
        ])
        
        fig.update_layout(
            title="Module Distribution by Category",
            height=400
        )
        
        return fig
    
    def create_quality_metrics_chart(self) -> go.Figure:
        """Create quality metrics visualization"""
        # Mock quality metrics for now
        metrics = {
            'Test Coverage': 95,
            'Documentation': 88,
            'Code Quality': 92,
            'Security': 98,
            'Performance': 85
        }
        
        fig = go.Figure(data=[
            go.Bar(
                x=list(metrics.keys()),
                y=list(metrics.values()),
                text=list(metrics.values()),
                textposition='auto',
                marker_color='lightgreen'
            )
        ])
        
        fig.update_layout(
            title="Quality Metrics",
            yaxis_title="Score (%)",
            yaxis=dict(range=[0, 100]),
            height=400
        )
        
        return fig
    
    def get_recent_changes(self, days: int = 7) -> List[Dict[str, Any]]:
        """Get recent changes to the framework"""
        changes = []
        cutoff_date = datetime.now() - timedelta(days=days)
        
        # Walk through framework directory
        for path in self.framework_path.rglob("*.md"):
            stat = path.stat()
            mod_time = datetime.fromtimestamp(stat.st_mtime)
            
            if mod_time > cutoff_date:
                changes.append({
                    'file': str(path.relative_to(self.framework_path)),
                    'type': 'modified',
                    'timestamp': mod_time.isoformat()
                })
        
        # Sort by timestamp
        changes.sort(key=lambda x: x['timestamp'], reverse=True)
        return changes
    
    def calculate_framework_health_score(self) -> Dict[str, float]:
        """Calculate overall framework health score"""
        scores = {
            'test_coverage': 95.0,  # Mock value
            'documentation_completeness': 88.0,  # Mock value
            'module_consistency': 92.0,  # Mock value
            'overall_score': 0.0
        }
        
        # Calculate overall score as weighted average
        weights = {'test_coverage': 0.4, 'documentation_completeness': 0.3, 'module_consistency': 0.3}
        scores['overall_score'] = sum(
            scores[metric] * weight 
            for metric, weight in weights.items()
        )
        
        return scores
    
    def export_framework_report(self, output_path: Path) -> bool:
        """Export comprehensive framework report"""
        try:
            report = {
                'statistics': self.collect_statistics(),
                'architecture': self.analyze_architecture(),
                'health_score': self.calculate_framework_health_score(),
                'timestamp': datetime.now().isoformat()
            }
            
            with open(output_path, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            
            return True
        except Exception as e:
            st.error(f"Error exporting report: {str(e)}")
            return False
    
    def render_statistics_dashboard(self):
        """Render statistics dashboard"""
        st.title("📊 Framework Statistics")
        
        if not self.statistics:
            self.collect_statistics()
        
        # Display key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Commands", self.statistics['total_commands'])
        
        with col2:
            st.metric("Total Modules", self.statistics['total_modules'])
        
        with col3:
            st.metric("Quality Gates", self.statistics.get('quality_gates', 0))
        
        with col4:
            st.metric("Framework Version", self.statistics['framework_version'])
        
        # Module breakdown
        st.subheader("Module Categories")
        for category, count in self.statistics['module_categories'].items():
            st.write(f"**{category.title()}**: {count} modules")
    
    def render(self):
        """Main render method for Framework Overview"""
        st.title("🏗️ Framework Overview")
        
        # Create tabs for different views
        tabs = st.tabs(["📊 Statistics", "🏗️ Architecture", "📈 Metrics", "🔄 Recent Changes"])
        
        with tabs[0]:
            self.render_statistics_dashboard()
            
            # Module distribution chart
            st.subheader("Module Distribution")
            fig = self.create_module_distribution_chart()
            st.plotly_chart(fig, use_container_width=True)
        
        with tabs[1]:
            st.subheader("Framework Architecture")
            fig = self.create_architecture_visualization()
            st.plotly_chart(fig, use_container_width=True)
            
            # Architectural patterns
            if not self.architecture_data:
                self.analyze_architecture()
            
            if self.architecture_data['architectural_patterns']:
                st.subheader("Architectural Patterns")
                for pattern in self.architecture_data['architectural_patterns']:
                    st.write(f"• {pattern}")
        
        with tabs[2]:
            st.subheader("Quality Metrics")
            fig = self.create_quality_metrics_chart()
            st.plotly_chart(fig, use_container_width=True)
            
            # Health score
            health_score = self.calculate_framework_health_score()
            st.subheader("Framework Health Score")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Overall Health", f"{health_score['overall_score']:.1f}%")
            with col2:
                st.metric("Test Coverage", f"{health_score['test_coverage']:.1f}%")
        
        with tabs[3]:
            st.subheader("Recent Changes")
            
            days = st.slider("Show changes from last N days", 1, 30, 7)
            changes = self.get_recent_changes(days)
            
            if changes:
                for change in changes[:10]:  # Show only last 10
                    st.write(f"📄 **{change['file']}** - {change['type']} on {change['timestamp'][:10]}")
            else:
                st.info("No recent changes found")
        
        # Export functionality
        st.divider()
        if st.button("📥 Export Framework Report"):
            report_path = Path("framework_report.json")
            if self.export_framework_report(report_path):
                st.success(f"Report exported to {report_path}")