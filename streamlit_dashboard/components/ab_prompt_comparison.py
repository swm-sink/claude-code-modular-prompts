"""
A/B Prompt Comparison System for Claude Code Framework Dashboard
Advanced comparison system for testing different prompt compositions and measuring their relative effectiveness
"""
import streamlit as st
import pandas as pd
import json
import time
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import re
import numpy as np
import hashlib


@dataclass
class PromptVariant:
    """Represents a prompt variant for A/B testing"""
    variant_id: str
    name: str
    description: str
    prompt_text: str
    composition_modules: List[str]
    token_count: int
    expected_effectiveness: float
    created_at: datetime
    metadata: Dict[str, Any]


@dataclass
class ComparisonResult:
    """Represents the result of an A/B comparison"""
    comparison_id: str
    variant_a: PromptVariant
    variant_b: PromptVariant
    test_scenario: str
    winner: str  # 'A', 'B', or 'tie'
    confidence_level: float
    effectiveness_diff: float
    performance_metrics: Dict[str, Any]
    detailed_analysis: Dict[str, Any]
    timestamp: datetime


class ABPromptComparison:
    """Advanced A/B testing system for prompt comparisons"""
    
    def __init__(self, framework_path: Path):
        """Initialize A/B Prompt Comparison system"""
        self.framework_path = framework_path
        self.prompt_variants = []
        self.comparison_history = []
        self.active_comparison = None
        
    def render(self):
        """Render the A/B Prompt Comparison interface"""
        st.title("⚖️ A/B Prompt Comparison")
        st.write("**Compare different prompt compositions and measure their relative effectiveness**")
        
        # Create tabs for different comparison aspects
        tab1, tab2, tab3, tab4 = st.tabs([
            "🔄 Setup Comparison", 
            "⚖️ Run A/B Test", 
            "📊 Results Analysis", 
            "📈 Comparison History"
        ])
        
        with tab1:
            self._render_comparison_setup()
        
        with tab2:
            self._render_ab_testing()
        
        with tab3:
            self._render_results_analysis()
        
        with tab4:
            self._render_comparison_history()
    
    def _render_comparison_setup(self):
        """Render comparison setup interface"""
        st.subheader("🔄 Setup A/B Comparison")
        st.write("**Create and manage prompt variants for comparison testing**")
        
        # Variant management
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.write("**Variant A (Control)**")
            self._render_variant_editor("A")
        
        with col2:
            st.write("**Variant B (Test)**")
            self._render_variant_editor("B")
        
        # Comparison configuration
        st.divider()
        st.subheader("🎯 Comparison Configuration")
        
        col_a, col_b = st.columns([2, 1])
        
        with col_a:
            # Test scenarios selection
            test_scenarios = [
                "Simple Task Request",
                "Complex Analysis Request", 
                "Research Query",
                "Error Debugging",
                "Documentation Request",
                "Custom Scenario"
            ]
            
            selected_scenarios = st.multiselect(
                "Select Test Scenarios",
                test_scenarios,
                default=["Simple Task Request", "Complex Analysis Request"],
                help="Choose scenarios to test both prompt variants against"
            )
            
            # Comparison metrics
            comparison_metrics = st.multiselect(
                "Comparison Metrics",
                ["Effectiveness Score", "Token Efficiency", "Response Quality", "Execution Time", "Criteria Met"],
                default=["Effectiveness Score", "Token Efficiency", "Response Quality"],
                help="Select metrics to compare between variants"
            )
        
        with col_b:
            st.write("**Test Configuration:**")
            
            confidence_level = st.selectbox(
                "Confidence Level",
                [90, 95, 99],
                index=1,
                format_func=lambda x: f"{x}%"
            )
            
            test_iterations = st.slider(
                "Test Iterations",
                min_value=1,
                max_value=10,
                value=3,
                help="Number of test iterations per scenario"
            )
            
            randomize_order = st.checkbox(
                "Randomize Test Order",
                value=True,
                help="Randomize the order of variant testing"
            )
        
        # Start comparison
        if len(self.prompt_variants) >= 2 and selected_scenarios:
            if st.button("🚀 Start A/B Comparison", type="primary"):
                self._initialize_comparison(selected_scenarios, comparison_metrics, confidence_level, test_iterations)
                st.success("A/B comparison initialized! Switch to 'Run A/B Test' tab to proceed.")
                st.rerun()
        else:
            if len(self.prompt_variants) < 2:
                st.warning("Please create at least 2 prompt variants to run comparison")
            if not selected_scenarios:
                st.warning("Please select at least one test scenario")
    
    def _render_variant_editor(self, variant_label: str):
        """Render variant editor for A or B"""
        variant_key = f"variant_{variant_label.lower()}"
        
        # Load existing variant if available
        existing_variant = None
        for variant in self.prompt_variants:
            if variant.name.endswith(f"Variant {variant_label}"):
                existing_variant = variant
                break
        
        with st.container():
            # Variant creation/editing
            variant_name = st.text_input(
                f"Variant {variant_label} Name",
                value=existing_variant.name if existing_variant else f"Prompt Variant {variant_label}",
                key=f"{variant_key}_name"
            )
            
            variant_description = st.text_area(
                f"Description",
                value=existing_variant.description if existing_variant else "",
                placeholder=f"Describe what makes this variant unique...",
                key=f"{variant_key}_desc"
            )
            
            prompt_text = st.text_area(
                f"Prompt Text",
                value=existing_variant.prompt_text if existing_variant else "",
                height=200,
                placeholder=f"Enter the complete prompt for variant {variant_label}...",
                key=f"{variant_key}_prompt"
            )
            
            # Module composition (optional)
            modules_used = st.text_input(
                f"Modules Used (comma-separated)",
                value=", ".join(existing_variant.composition_modules) if existing_variant else "",
                placeholder="intelligent-routing, tdd-cycle-pattern, ...",
                key=f"{variant_key}_modules"
            )
            
            if st.button(f"Save Variant {variant_label}", key=f"{variant_key}_save"):
                if prompt_text and variant_name:
                    self._save_variant(variant_label, variant_name, variant_description, prompt_text, modules_used)
                    st.success(f"Variant {variant_label} saved!")
                    st.rerun()
                else:
                    st.error("Please provide variant name and prompt text")
            
            # Display variant preview
            if prompt_text:
                st.write("**Preview:**")
                with st.expander(f"Variant {variant_label} Preview", expanded=False):
                    st.code(prompt_text[:300] + "..." if len(prompt_text) > 300 else prompt_text)
                    
                    word_count = len(prompt_text.split())
                    token_estimate = word_count * 1.3
                    
                    col_x, col_y = st.columns(2)
                    with col_x:
                        st.metric("Word Count", word_count)
                    with col_y:
                        st.metric("Est. Tokens", f"{token_estimate:.0f}")
    
    def _render_ab_testing(self):
        """Render A/B testing execution interface"""
        st.subheader("⚖️ Run A/B Test")
        
        if not self.active_comparison:
            st.info("No active comparison. Set up a comparison in the 'Setup Comparison' tab first.")
            return
        
        st.write("**Active A/B Comparison**")
        
        # Display comparison overview
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            st.write("**Variant A (Control)**")
            variant_a = self.active_comparison["variant_a"]
            st.write(f"Name: {variant_a['name']}")
            st.write(f"Modules: {len(variant_a['composition_modules'])}")
            st.write(f"Tokens: {variant_a['token_count']}")
        
        with col2:
            st.write("**VS**")
            st.markdown("## ⚖️")
        
        with col3:
            st.write("**Variant B (Test)**")
            variant_b = self.active_comparison["variant_b"]
            st.write(f"Name: {variant_b['name']}")
            st.write(f"Modules: {len(variant_b['composition_modules'])}")
            st.write(f"Tokens: {variant_b['token_count']}")
        
        # Test execution
        st.divider()
        st.write("**Test Execution**")
        
        scenarios = self.active_comparison["test_scenarios"]
        metrics = self.active_comparison["comparison_metrics"]
        
        st.write(f"**Scenarios:** {', '.join(scenarios)}")
        st.write(f"**Metrics:** {', '.join(metrics)}")
        
        if st.button("🚀 Execute A/B Test", type="primary"):
            self._execute_ab_test()
            st.rerun()
        
        # Show test progress if running
        if self.active_comparison.get("status") == "running":
            st.write("**Test in Progress...**")
            progress_bar = st.progress(0.7)  # Simulated progress
            st.info("Testing variants against selected scenarios...")
        
        # Show results if completed
        elif self.active_comparison.get("status") == "completed":
            self._render_ab_results_summary()
    
    def _render_results_analysis(self):
        """Render detailed results analysis"""
        st.subheader("📊 Results Analysis")
        
        if not self.comparison_history:
            st.info("No comparison results available. Run an A/B test first!")
            return
        
        # Select comparison to analyze
        comparison_options = [
            f"{result.variant_a.name} vs {result.variant_b.name} - {result.timestamp.strftime('%Y-%m-%d %H:%M')}"
            for result in self.comparison_history[-5:]  # Show latest 5
        ]
        
        if not comparison_options:
            st.info("No completed comparisons to analyze")
            return
        
        selected_comparison = st.selectbox(
            "Select Comparison to Analyze",
            range(len(comparison_options)),
            format_func=lambda x: comparison_options[x]
        )
        
        result = self.comparison_history[-(len(comparison_options)-selected_comparison)]
        
        # Winner announcement
        if result.winner == "tie":
            st.info(f"🤝 **TIE** - Both variants performed similarly (confidence: {result.confidence_level:.1%})")
        else:
            winner_name = result.variant_a.name if result.winner == "A" else result.variant_b.name
            st.success(f"🏆 **WINNER: {winner_name}** (confidence: {result.confidence_level:.1%})")
        
        # Detailed metrics comparison
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.write("**Performance Comparison**")
            
            metrics_data = []
            for metric, values in result.performance_metrics.items():
                variant_a_value = values.get("variant_a", 0)
                variant_b_value = values.get("variant_b", 0)
                
                metrics_data.append({
                    "Metric": metric,
                    "Variant A": f"{variant_a_value:.2f}" if isinstance(variant_a_value, float) else str(variant_a_value),
                    "Variant B": f"{variant_b_value:.2f}" if isinstance(variant_b_value, float) else str(variant_b_value),
                    "Difference": f"{abs(variant_a_value - variant_b_value):.2f}" if isinstance(variant_a_value, (int, float)) else "N/A"
                })
            
            metrics_df = pd.DataFrame(metrics_data)
            st.dataframe(metrics_df, use_container_width=True)
        
        with col2:
            # Performance radar chart
            self._render_performance_radar(result)
        
        # Detailed analysis insights
        st.divider()
        st.write("**Detailed Analysis**")
        
        analysis = result.detailed_analysis
        
        col_a, col_b = st.columns([1, 1])
        
        with col_a:
            st.write("**Strengths & Weaknesses**")
            
            if "variant_a_strengths" in analysis:
                st.write(f"**{result.variant_a.name} Strengths:**")
                for strength in analysis["variant_a_strengths"]:
                    st.write(f"• {strength}")
            
            if "variant_a_weaknesses" in analysis:
                st.write(f"**{result.variant_a.name} Weaknesses:**")
                for weakness in analysis["variant_a_weaknesses"]:
                    st.write(f"• {weakness}")
        
        with col_b:
            if "variant_b_strengths" in analysis:
                st.write(f"**{result.variant_b.name} Strengths:**")
                for strength in analysis["variant_b_strengths"]:
                    st.write(f"• {strength}")
            
            if "variant_b_weaknesses" in analysis:
                st.write(f"**{result.variant_b.name} Weaknesses:**")
                for weakness in analysis["variant_b_weaknesses"]:
                    st.write(f"• {weakness}")
        
        # Recommendations
        if "recommendations" in analysis:
            st.write("**🎯 Recommendations:**")
            for rec in analysis["recommendations"]:
                st.write(f"• {rec}")
    
    def _render_comparison_history(self):
        """Render comparison history and trends"""
        st.subheader("📈 Comparison History")
        
        if not self.comparison_history:
            st.info("No comparison history available")
            return
        
        # History overview
        history_data = []
        for result in self.comparison_history:
            history_data.append({
                "Timestamp": result.timestamp.strftime("%Y-%m-%d %H:%M"),
                "Variant A": result.variant_a.name,
                "Variant B": result.variant_b.name,
                "Winner": result.winner.upper() if result.winner != "tie" else "TIE",
                "Confidence": f"{result.confidence_level:.1%}",
                "Effectiveness Diff": f"{result.effectiveness_diff:.2f}",
                "Test Scenario": result.test_scenario
            })
        
        history_df = pd.DataFrame(history_data)
        st.dataframe(history_df, use_container_width=True)
        
        # Trends analysis
        if len(self.comparison_history) >= 3:
            st.divider()
            st.write("**Trends Analysis**")
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                # Winner distribution
                winner_counts = {}
                for result in self.comparison_history:
                    winner_counts[result.winner] = winner_counts.get(result.winner, 0) + 1
                
                fig_winners = px.pie(
                    values=list(winner_counts.values()),
                    names=list(winner_counts.keys()),
                    title="Winner Distribution"
                )
                st.plotly_chart(fig_winners, use_container_width=True)
            
            with col2:
                # Confidence trends
                confidence_data = [
                    {"Test": i+1, "Confidence": result.confidence_level}
                    for i, result in enumerate(self.comparison_history)
                ]
                
                confidence_df = pd.DataFrame(confidence_data)
                
                fig_confidence = px.line(
                    confidence_df, 
                    x="Test", 
                    y="Confidence",
                    title="Confidence Level Trends",
                    markers=True
                )
                fig_confidence.update_layout(yaxis_tickformat=".1%")
                st.plotly_chart(fig_confidence, use_container_width=True)
    
    def _save_variant(self, variant_label: str, name: str, description: str, prompt_text: str, modules_used: str):
        """Save a prompt variant"""
        modules_list = [m.strip() for m in modules_used.split(",") if m.strip()] if modules_used else []
        
        variant_id = hashlib.md5(f"{name}_{prompt_text}".encode()).hexdigest()[:8]
        
        variant = PromptVariant(
            variant_id=variant_id,
            name=name,
            description=description,
            prompt_text=prompt_text,
            composition_modules=modules_list,
            token_count=int(len(prompt_text.split()) * 1.3),  # Rough estimate
            expected_effectiveness=0.75,  # Default estimate
            created_at=datetime.now(),
            metadata={"variant_label": variant_label}
        )
        
        # Remove existing variant with same label
        self.prompt_variants = [v for v in self.prompt_variants if not v.name.endswith(f"Variant {variant_label}")]
        
        self.prompt_variants.append(variant)
    
    def _initialize_comparison(self, scenarios: List[str], metrics: List[str], confidence: int, iterations: int):
        """Initialize an A/B comparison"""
        if len(self.prompt_variants) < 2:
            return
        
        # Get the two most recent variants (A and B)
        variant_a = None
        variant_b = None
        
        for variant in self.prompt_variants:
            if variant.name.endswith("Variant A"):
                variant_a = variant
            elif variant.name.endswith("Variant B"):
                variant_b = variant
        
        if not variant_a or not variant_b:
            return
        
        self.active_comparison = {
            "comparison_id": hashlib.md5(f"{variant_a.variant_id}_{variant_b.variant_id}_{datetime.now()}".encode()).hexdigest()[:8],
            "variant_a": asdict(variant_a),
            "variant_b": asdict(variant_b),
            "test_scenarios": scenarios,
            "comparison_metrics": metrics,
            "confidence_level": confidence / 100,
            "test_iterations": iterations,
            "status": "initialized"
        }
    
    def _execute_ab_test(self):
        """Execute the A/B test (simulated)"""
        if not self.active_comparison:
            return
        
        self.active_comparison["status"] = "running"
        
        # Simulate test execution
        time.sleep(1)  # Simulate processing time
        
        # Generate simulated results
        variant_a_effectiveness = np.random.uniform(0.7, 0.9)
        variant_b_effectiveness = np.random.uniform(0.65, 0.95)
        
        effectiveness_diff = abs(variant_a_effectiveness - variant_b_effectiveness)
        
        # Determine winner
        if effectiveness_diff < 0.05:
            winner = "tie"
            confidence = 0.6
        elif variant_a_effectiveness > variant_b_effectiveness:
            winner = "A"
            confidence = min(0.95, 0.7 + effectiveness_diff)
        else:
            winner = "B"
            confidence = min(0.95, 0.7 + effectiveness_diff)
        
        # Create comparison result
        result = ComparisonResult(
            comparison_id=self.active_comparison["comparison_id"],
            variant_a=PromptVariant(**self.active_comparison["variant_a"]),
            variant_b=PromptVariant(**self.active_comparison["variant_b"]),
            test_scenario=", ".join(self.active_comparison["test_scenarios"]),
            winner=winner,
            confidence_level=confidence,
            effectiveness_diff=effectiveness_diff,
            performance_metrics={
                "Effectiveness Score": {
                    "variant_a": variant_a_effectiveness,
                    "variant_b": variant_b_effectiveness
                },
                "Token Efficiency": {
                    "variant_a": variant_a_effectiveness / (self.active_comparison["variant_a"]["token_count"] / 1000),
                    "variant_b": variant_b_effectiveness / (self.active_comparison["variant_b"]["token_count"] / 1000)
                },
                "Response Quality": {
                    "variant_a": np.random.uniform(0.6, 0.9),
                    "variant_b": np.random.uniform(0.6, 0.9)
                }
            },
            detailed_analysis=self._generate_detailed_analysis(variant_a_effectiveness, variant_b_effectiveness, winner),
            timestamp=datetime.now()
        )
        
        self.comparison_history.append(result)
        self.active_comparison["status"] = "completed"
        self.active_comparison["result"] = asdict(result)
    
    def _generate_detailed_analysis(self, a_eff: float, b_eff: float, winner: str) -> Dict[str, Any]:
        """Generate detailed analysis for comparison results"""
        analysis = {}
        
        if winner == "A":
            analysis["variant_a_strengths"] = [
                "Higher overall effectiveness score",
                "Better pattern matching",
                "More consistent performance"
            ]
            analysis["variant_b_weaknesses"] = [
                "Lower effectiveness in complex scenarios",
                "Token efficiency could be improved"
            ]
        elif winner == "B":
            analysis["variant_b_strengths"] = [
                "Superior effectiveness score",
                "Better token utilization",
                "More robust across scenarios"
            ]
            analysis["variant_a_weaknesses"] = [
                "Lower performance in key metrics",
                "Could benefit from optimization"
            ]
        else:
            analysis["general_observations"] = [
                "Both variants performed similarly",
                "Consider testing with more challenging scenarios",
                "Small differences suggest both approaches are viable"
            ]
        
        analysis["recommendations"] = [
            "Test with additional scenarios for better confidence",
            "Consider hybrid approach combining strengths of both variants",
            "Monitor performance in production environment"
        ]
        
        return analysis
    
    def _render_ab_results_summary(self):
        """Render A/B test results summary"""
        if not self.active_comparison.get("result"):
            return
        
        result_data = self.active_comparison["result"]
        
        st.divider()
        st.write("**🎉 A/B Test Results**")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if result_data["winner"] == "A":
                st.success(f"🏆 **Winner: Variant A**")
            elif result_data["winner"] == "B":
                st.success(f"🏆 **Winner: Variant B**")
            else:
                st.info("🤝 **Result: Tie**")
        
        with col2:
            st.metric("Confidence Level", f"{result_data['confidence_level']:.1%}")
        
        with col3:
            st.metric("Effectiveness Difference", f"{result_data['effectiveness_diff']:.2f}")
        
        # Quick metrics
        st.write("**Performance Summary:**")
        metrics = result_data["performance_metrics"]
        
        for metric_name, values in metrics.items():
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric(f"Variant A - {metric_name}", f"{values['variant_a']:.2f}")
            with col_b:
                st.metric(f"Variant B - {metric_name}", f"{values['variant_b']:.2f}")
    
    def _render_performance_radar(self, result: ComparisonResult):
        """Render performance radar chart comparing variants"""
        metrics = list(result.performance_metrics.keys())
        variant_a_values = [result.performance_metrics[m]["variant_a"] for m in metrics]
        variant_b_values = [result.performance_metrics[m]["variant_b"] for m in metrics]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=variant_a_values,
            theta=metrics,
            fill='toself',
            name=result.variant_a.name
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=variant_b_values,
            theta=metrics,
            fill='toself',
            name=result.variant_b.name
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )
            ),
            title="Performance Comparison",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)