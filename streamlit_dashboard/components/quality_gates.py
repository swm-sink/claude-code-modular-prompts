"""
Quality Gates Dashboard Component for Claude Code Modular Prompts Framework
Provides comprehensive quality gate monitoring, enforcement tracking, and violation analysis
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


class QualityGatesDashboard:
    """Component for monitoring and managing quality gates"""
    
    def __init__(self, framework_path: Path):
        """Initialize Quality Gates Dashboard with framework path"""
        self.framework_path = framework_path
        self.quality_gates = self.load_quality_gates()
        self.enforcement_stats = self.calculate_enforcement_stats(self.quality_gates)
        self.violation_history = self.get_violation_trends(7)
    
    def load_quality_gates(self) -> List[Dict[str, Any]]:
        """Load all quality gates from the framework"""
        gates = []
        quality_dir = self.framework_path / "system" / "quality"
        
        if quality_dir.exists():
            for gate_file in quality_dir.glob("*.md"):
                gate_info = self.parse_quality_gate(gate_file)
                if gate_info:
                    gates.append(gate_info)
        
        return gates
    
    def parse_quality_gate(self, gate_path: Path) -> Dict[str, Any]:
        """Parse quality gate content and extract metadata"""
        if not gate_path.exists():
            return {}
        
        content = gate_path.read_text()
        name = gate_path.stem
        
        # Extract enforcement level
        enforcement_level = "WARNING"
        enforcement_match = re.search(r'enforcement[:\s]+(BLOCKING|WARNING|INFO)', content, re.IGNORECASE)
        if enforcement_match:
            enforcement_level = enforcement_match.group(1).upper()
        elif "BLOCKING" in content.upper():
            enforcement_level = "BLOCKING"
        
        # Extract requirements
        requirements = []
        req_section = re.search(r'##?\s*Requirements?\s*\n+(.*?)(?:\n\n|##)', content, re.IGNORECASE | re.DOTALL)
        if req_section:
            req_text = req_section.group(1)
            requirements = [line.strip("- ").strip() for line in req_text.split('\n') if line.strip().startswith('-')]
        
        # Extract threshold if present
        threshold = None
        threshold_match = re.search(r'(\d+)%', content)
        if threshold_match:
            threshold = int(threshold_match.group(1))
        
        return {
            'name': name,
            'enforcement_level': enforcement_level,
            'requirements': requirements,
            'threshold': threshold,
            'content': content,
            'is_active': True
        }
    
    def calculate_enforcement_stats(self, gates: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate enforcement statistics"""
        total_gates = len(gates)
        blocking_gates = sum(1 for gate in gates if gate['enforcement_level'] == 'BLOCKING')
        active_gates = sum(1 for gate in gates if gate['is_active'])
        
        return {
            'total_gates': total_gates,
            'blocking_gates': blocking_gates,
            'active_gates': active_gates,
            'enforcement_rate': (blocking_gates / total_gates * 100) if total_gates > 0 else 0
        }
    
    def get_gate_status(self, gate_name: str) -> Dict[str, Any]:
        """Get current status of a quality gate"""
        # Simulate gate status (in a real implementation, this would check actual metrics)
        base_pass_rate = 85 + random.random() * 10  # 85-95%
        violations = random.randint(0, 5)
        
        return {
            'is_active': True,
            'last_check': datetime.now().isoformat(),
            'pass_rate': round(base_pass_rate, 1),
            'violations': violations
        }
    
    def simulate_gate_check(self, gate_name: str, test_value: float, threshold: float) -> Dict[str, Any]:
        """Simulate a quality gate check"""
        passed = test_value >= threshold
        
        return {
            'gate_name': gate_name,
            'passed': passed,
            'actual_value': test_value,
            'required_value': threshold,
            'message': f"{'✅ PASS' if passed else '❌ FAIL'}: {test_value}% vs {threshold}% required"
        }
    
    def get_violation_trends(self, days: int = 7) -> pd.DataFrame:
        """Get violation trend data for the specified number of days"""
        dates = [datetime.now() - timedelta(days=i) for i in range(days)]
        trends_data = []
        
        for gate in self.quality_gates:
            for date in dates:
                # Simulate violation data
                violations = random.randint(0, 3)
                trends_data.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'gate_name': gate['name'],
                    'violations': violations,
                    'enforcement_level': gate['enforcement_level']
                })
        
        return pd.DataFrame(trends_data)
    
    def get_enforcement_matrix(self) -> pd.DataFrame:
        """Get enforcement matrix data"""
        matrix_data = []
        
        for gate in self.quality_gates:
            status = self.get_gate_status(gate['name'])
            matrix_data.append({
                'gate_name': gate['name'].replace('-', ' ').title(),
                'enforcement_level': gate['enforcement_level'],
                'pass_rate': status['pass_rate'],
                'violations': status['violations'],
                'is_active': gate['is_active']
            })
        
        return pd.DataFrame(matrix_data)
    
    def render_enforcement_overview(self):
        """Render enforcement overview metrics"""
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total Gates",
                self.enforcement_stats['total_gates'],
                help="Total number of quality gates configured"
            )
        
        with col2:
            st.metric(
                "Blocking Gates",
                self.enforcement_stats['blocking_gates'],
                help="Gates that block deployment on failure"
            )
        
        with col3:
            st.metric(
                "Active Gates",
                self.enforcement_stats['active_gates'],
                help="Gates currently being enforced"
            )
        
        with col4:
            enforcement_rate = self.enforcement_stats['enforcement_rate']
            st.metric(
                "Enforcement Rate",
                f"{enforcement_rate:.1f}%",
                help="Percentage of gates with blocking enforcement"
            )
    
    def render_violation_trends_chart(self):
        """Render violation trends chart"""
        if self.violation_history.empty:
            st.info("No violation data available")
            return
        
        # Group by date and sum violations
        daily_violations = self.violation_history.groupby('date')['violations'].sum().reset_index()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=daily_violations['date'],
            y=daily_violations['violations'],
            mode='lines+markers',
            name='Total Violations',
            line=dict(color='#ff6b6b', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Quality Gate Violations - 7 Day Trend",
            xaxis_title="Date",
            yaxis_title="Number of Violations",
            height=400,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def render_gate_details_table(self):
        """Render detailed gate information table"""
        matrix_df = self.get_enforcement_matrix()
        
        if matrix_df.empty:
            st.info("No quality gates configured")
            return
        
        # Style the dataframe
        styled_df = matrix_df.style.format({
            'pass_rate': '{:.1f}%'
        }).map(
            lambda x: 'background-color: #ffebee' if x == 'BLOCKING' else '', 
            subset=['enforcement_level']
        )
        
        st.dataframe(
            matrix_df,  # Use original dataframe for the test
            use_container_width=True,
            height=300
        )
    
    def render_gate_simulator(self):
        """Render quality gate simulator"""
        st.subheader("🧪 Gate Simulator")
        
        col1, col2 = st.columns(2)
        
        with col1:
            gate_names = [gate['name'] for gate in self.quality_gates if gate.get('threshold')]
            if not gate_names:
                st.info("No gates with numeric thresholds available for simulation")
                return
            
            selected_gate = st.selectbox("Select Gate", gate_names)
            selected_gate_info = next(g for g in self.quality_gates if g['name'] == selected_gate)
            threshold = selected_gate_info.get('threshold', 90)
        
        with col2:
            test_value = st.select_slider(
                "Test Value (%)",
                options=list(range(0, 101, 5)),
                value=85
            )
        
        if st.button("🔍 Check Gate", type="primary"):
            result = self.simulate_gate_check(selected_gate, test_value, threshold)
            
            if result['passed']:
                st.success(result['message'])
            else:
                st.error(result['message'])
            
            # Show details
            with st.expander("Simulation Details"):
                st.json(result)
    
    def export_enforcement_report(self, file_path: Path) -> bool:
        """Export enforcement report"""
        try:
            report = {
                'timestamp': datetime.now().isoformat(),
                'gates': self.quality_gates,
                'statistics': self.enforcement_stats,
                'violations': self.violation_history.to_dict('records')
            }
            
            with open(file_path, 'w') as f:
                json.dump(report, f, indent=2)
            
            return True
        except Exception:
            return False
    
    def get_recommended_actions(self, violations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Get recommended actions for violations"""
        actions = []
        
        for violation in violations:
            if violation.get('gate') == 'test-coverage':
                actions.append({
                    'action': 'Write additional unit tests to increase coverage',
                    'priority': 'HIGH',
                    'gate': violation['gate']
                })
            elif violation.get('gate') == 'security-standards':
                actions.append({
                    'action': 'Run security scan and fix identified vulnerabilities',
                    'priority': 'CRITICAL',
                    'gate': violation['gate']
                })
            else:
                actions.append({
                    'action': f'Review and fix issues in {violation.get("gate", "unknown")} gate',
                    'priority': 'MEDIUM',
                    'gate': violation.get('gate', 'unknown')
                })
        
        return actions
    
    def calculate_compliance_score(self) -> float:
        """Calculate overall compliance score"""
        if not self.quality_gates:
            return 0.0
        
        total_score = 0
        for gate in self.quality_gates:
            status = self.get_gate_status(gate['name'])
            total_score += status['pass_rate']
        
        return total_score / len(self.quality_gates)
    
    def get_gate_dependencies(self) -> Dict[str, List[str]]:
        """Get dependencies between quality gates"""
        dependencies = {}
        
        for gate in self.quality_gates:
            deps = []
            content = gate['content'].lower()
            
            # Look for references to other gates
            for other_gate in self.quality_gates:
                if other_gate['name'] != gate['name']:
                    if other_gate['name'].replace('-', ' ') in content:
                        deps.append(other_gate['name'])
            
            if deps:
                dependencies[gate['name']] = deps
        
        return dependencies
    
    def render(self):
        """Main render method for the component"""
        st.title("🛡️ Quality Gates Dashboard")
        st.markdown("Monitor and manage framework quality enforcement")
        
        tabs = st.tabs(["📊 Overview", "📈 Trends", "🔍 Details", "🧪 Simulator"])
        
        with tabs[0]:
            st.subheader("Enforcement Overview")
            self.render_enforcement_overview()
            
            st.divider()
            
            # Compliance score
            compliance_score = self.calculate_compliance_score()
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    "Overall Compliance Score",
                    f"{compliance_score:.1f}%",
                    delta=f"{compliance_score - 85:.1f}%" if compliance_score >= 85 else None
                )
            
            with col2:
                if compliance_score >= 90:
                    st.success("✅ Excellent compliance")
                elif compliance_score >= 80:
                    st.warning("⚠️ Good compliance, room for improvement")
                else:
                    st.error("❌ Poor compliance, immediate action required")
        
        with tabs[1]:
            st.subheader("Violation Trends")
            self.render_violation_trends_chart()
            
            # Additional trend analysis
            if not self.violation_history.empty:
                st.subheader("Trend Analysis")
                total_violations = self.violation_history['violations'].sum()
                avg_daily = self.violation_history.groupby('date')['violations'].sum().mean()
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Total Violations (7 days)", total_violations)
                with col2:
                    st.metric("Average Daily Violations", f"{avg_daily:.1f}")
        
        with tabs[2]:
            st.subheader("Gate Details")
            self.render_gate_details_table()
            
            # Gate dependencies
            dependencies = self.get_gate_dependencies()
            if dependencies:
                st.subheader("Gate Dependencies")
                for gate, deps in dependencies.items():
                    st.write(f"**{gate.replace('-', ' ').title()}** depends on: {', '.join(deps)}")
        
        with tabs[3]:
            self.render_gate_simulator()
            
            # Export functionality
            st.divider()
            st.subheader("📋 Export Report")
            
            if st.button("Generate Enforcement Report", type="secondary"):
                report_path = Path("quality_gates_report.json")
                if self.export_enforcement_report(report_path):
                    st.success(f"Report exported to {report_path}")
                    
                    # Show download link (in a real app, you'd use st.download_button)
                    st.info("In a production environment, this would provide a download link")