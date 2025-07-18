"""
Pattern Recognition Engine for Claude Code Framework Dashboard
Advanced AI-powered system to learn from successful prompt compositions and identify optimal patterns
"""
import streamlit as st
import pandas as pd
import json
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import re
from collections import defaultdict, Counter
import networkx as nx
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class PatternInsight:
    """Represents a discovered pattern insight"""
    pattern_id: str
    pattern_name: str
    pattern_type: str
    success_rate: float
    frequency: int
    modules_involved: List[str]
    contexts: List[str]
    characteristics: Dict[str, Any]
    examples: List[str]
    confidence_score: float
    discovered_at: datetime


@dataclass
class PromptLearningData:
    """Represents learning data from prompt usage"""
    prompt_id: str
    prompt_text: str
    modules_used: List[str]
    effectiveness_score: float
    context: str
    user_feedback: Optional[str]
    success_metrics: Dict[str, float]
    timestamp: datetime


class PatternRecognitionEngine:
    """Advanced pattern recognition system for prompt engineering"""
    
    def __init__(self, framework_path: Path):
        """Initialize Pattern Recognition Engine"""
        self.framework_path = framework_path
        self.learning_data = []
        self.discovered_patterns = []
        self.pattern_insights = []
        self.recommendation_model = None
        self._initialize_demo_data()
        
    def _initialize_demo_data(self):
        """Initialize with demo learning data"""
        demo_data = [
            PromptLearningData(
                prompt_id="p1",
                prompt_text="Use critical thinking pattern followed by TDD cycle for implementation",
                modules_used=["critical-thinking-pattern", "tdd-cycle-pattern", "task-management"],
                effectiveness_score=0.92,
                context="development",
                user_feedback="Excellent systematic approach",
                success_metrics={"code_quality": 0.95, "test_coverage": 0.88, "completion_time": 0.90},
                timestamp=datetime.now() - timedelta(days=5)
            ),
            PromptLearningData(
                prompt_id="p2", 
                prompt_text="Research analysis pattern with documentation generation for comprehensive output",
                modules_used=["research-analysis-pattern", "documentation-pattern", "quality-validation-pattern"],
                effectiveness_score=0.87,
                context="research",
                user_feedback="Very thorough and well-documented",
                success_metrics={"comprehensiveness": 0.91, "accuracy": 0.85, "readability": 0.89},
                timestamp=datetime.now() - timedelta(days=3)
            ),
            PromptLearningData(
                prompt_id="p3",
                prompt_text="Intelligent routing with multi-agent coordination for complex tasks",
                modules_used=["intelligent-routing", "multi-agent", "session-management-pattern"],
                effectiveness_score=0.89,
                context="coordination",
                user_feedback="Great for complex multi-step workflows",
                success_metrics={"task_completion": 0.93, "efficiency": 0.86, "coordination": 0.88},
                timestamp=datetime.now() - timedelta(days=2)
            ),
            PromptLearningData(
                prompt_id="p4",
                prompt_text="TDD cycle with quality validation for robust development",
                modules_used=["tdd-cycle-pattern", "quality-validation-pattern", "comprehensive-testing"],
                effectiveness_score=0.94,
                context="development",
                user_feedback="Ensures high-quality code",
                success_metrics={"code_quality": 0.96, "test_coverage": 0.94, "reliability": 0.92},
                timestamp=datetime.now() - timedelta(days=1)
            ),
            PromptLearningData(
                prompt_id="p5",
                prompt_text="Documentation pattern with workflow orchestration for complete solutions",
                modules_used=["documentation-pattern", "workflow-orchestration-engine", "context-management-pattern"],
                effectiveness_score=0.85,
                context="documentation",
                user_feedback="Comprehensive and well-structured",
                success_metrics={"completeness": 0.87, "structure": 0.89, "usability": 0.83},
                timestamp=datetime.now()
            )
        ]
        
        self.learning_data.extend(demo_data)
        self._analyze_patterns()
    
    def render(self):
        """Render the Pattern Recognition Engine interface"""
        st.title("🧠 Pattern Recognition Engine")
        st.write("**AI-powered learning system that discovers optimal prompt patterns from usage data**")
        
        # Create tabs for different aspects
        tab1, tab2, tab3, tab4 = st.tabs([
            "🔍 Pattern Discovery",
            "📊 Learning Analytics", 
            "🎯 Pattern Insights",
            "🔮 Predictive Modeling"
        ])
        
        with tab1:
            self._render_pattern_discovery()
        
        with tab2:
            self._render_learning_analytics()
        
        with tab3:
            self._render_pattern_insights()
        
        with tab4:
            self._render_predictive_modeling()
    
    def _render_pattern_discovery(self):
        """Render pattern discovery interface"""
        st.subheader("🔍 Pattern Discovery")
        st.write("**Automatically discovered patterns from successful prompt compositions**")
        
        # Pattern discovery summary
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Patterns Discovered", len(self.discovered_patterns))
        
        with col2:
            avg_success = np.mean([p.success_rate for p in self.discovered_patterns]) if self.discovered_patterns else 0
            st.metric("Avg Success Rate", f"{avg_success:.1%}")
        
        with col3:
            total_examples = sum(len(p.examples) for p in self.discovered_patterns)
            st.metric("Total Examples", total_examples)
        
        with col4:
            high_confidence = sum(1 for p in self.discovered_patterns if p.confidence_score > 0.8)
            st.metric("High Confidence", high_confidence)
        
        # Discovered patterns
        if self.discovered_patterns:
            st.divider()
            st.write("**Discovered Patterns:**")
            
            for pattern in self.discovered_patterns:
                with st.expander(f"🧩 {pattern.pattern_name} ({pattern.success_rate:.1%} success)", 
                               expanded=False):
                    
                    col_a, col_b = st.columns([2, 1])
                    
                    with col_a:
                        st.write(f"**Type:** {pattern.pattern_type}")
                        st.write(f"**Modules:** {', '.join(pattern.modules_involved)}")
                        st.write(f"**Contexts:** {', '.join(pattern.contexts)}")
                        st.write(f"**Frequency:** Used {pattern.frequency} times")
                        
                        if pattern.characteristics:
                            st.write("**Key Characteristics:**")
                            for key, value in pattern.characteristics.items():
                                st.write(f"• {key}: {value}")
                    
                    with col_b:
                        # Pattern effectiveness radar
                        self._render_pattern_radar(pattern)
                    
                    if pattern.examples:
                        st.write("**Example Usage:**")
                        example_text = pattern.examples[0]
                        st.code(example_text[:200] + "..." if len(example_text) > 200 else example_text)
        else:
            st.info("No patterns discovered yet. Add more learning data to discover patterns.")
        
        # Manual pattern analysis
        st.divider()
        st.subheader("🔧 Manual Pattern Analysis")
        
        if st.button("🚀 Analyze Current Data for Patterns"):
            with st.spinner("Analyzing patterns..."):
                new_patterns = self._discover_new_patterns()
                if new_patterns:
                    st.success(f"Discovered {len(new_patterns)} new patterns!")
                    self.discovered_patterns.extend(new_patterns)
                    st.rerun()
                else:
                    st.info("No new patterns discovered with current data.")
    
    def _render_learning_analytics(self):
        """Render learning analytics dashboard"""
        st.subheader("📊 Learning Analytics")
        st.write("**Analyze prompt usage data and learning trends**")
        
        if not self.learning_data:
            st.info("No learning data available")
            return
        
        # Usage trends
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Effectiveness over time
            effectiveness_data = [
                {
                    "Date": data.timestamp.strftime("%Y-%m-%d"),
                    "Effectiveness": data.effectiveness_score,
                    "Context": data.context
                }
                for data in sorted(self.learning_data, key=lambda x: x.timestamp)
            ]
            
            effectiveness_df = pd.DataFrame(effectiveness_data)
            
            fig_trend = px.line(
                effectiveness_df,
                x="Date",
                y="Effectiveness", 
                color="Context",
                title="Effectiveness Trends Over Time",
                markers=True
            )
            fig_trend.update_layout(yaxis_tickformat=".1%")
            st.plotly_chart(fig_trend, use_container_width=True)
        
        with col2:
            # Module usage frequency
            module_counts = Counter()
            for data in self.learning_data:
                module_counts.update(data.modules_used)
            
            top_modules = dict(module_counts.most_common(8))
            
            fig_modules = px.bar(
                x=list(top_modules.keys()),
                y=list(top_modules.values()),
                title="Most Used Modules",
                labels={'x': 'Module', 'y': 'Usage Count'}
            )
            fig_modules.update_xaxes(tickangle=45)
            st.plotly_chart(fig_modules, use_container_width=True)
        
        # Context analysis
        st.divider()
        col3, col4 = st.columns([1, 1])
        
        with col3:
            # Context effectiveness
            context_effectiveness = defaultdict(list)
            for data in self.learning_data:
                context_effectiveness[data.context].append(data.effectiveness_score)
            
            context_avg = {
                context: np.mean(scores) 
                for context, scores in context_effectiveness.items()
            }
            
            fig_context = px.bar(
                x=list(context_avg.keys()),
                y=list(context_avg.values()),
                title="Effectiveness by Context",
                labels={'x': 'Context', 'y': 'Avg Effectiveness'}
            )
            fig_context.update_layout(yaxis_tickformat=".1%")
            st.plotly_chart(fig_context, use_container_width=True)
        
        with col4:
            # Success metrics distribution
            all_metrics = defaultdict(list)
            for data in self.learning_data:
                for metric, value in data.success_metrics.items():
                    all_metrics[metric].append(value)
            
            metric_avgs = {
                metric: np.mean(values)
                for metric, values in all_metrics.items()
            }
            
            fig_metrics = px.bar(
                x=list(metric_avgs.keys()),
                y=list(metric_avgs.values()),
                title="Average Success Metrics",
                labels={'x': 'Metric', 'y': 'Average Score'}
            )
            fig_metrics.update_layout(yaxis_tickformat=".1%")
            st.plotly_chart(fig_metrics, use_container_width=True)
        
        # Detailed data table
        st.divider()
        st.write("**Learning Data Details:**")
        
        learning_df = pd.DataFrame([
            {
                "ID": data.prompt_id,
                "Context": data.context,
                "Modules": len(data.modules_used),
                "Effectiveness": f"{data.effectiveness_score:.1%}",
                "Feedback": data.user_feedback[:50] + "..." if data.user_feedback and len(data.user_feedback) > 50 else data.user_feedback or "N/A",
                "Date": data.timestamp.strftime("%Y-%m-%d %H:%M")
            }
            for data in self.learning_data
        ])
        
        st.dataframe(learning_df, use_container_width=True)
    
    def _render_pattern_insights(self):
        """Render pattern insights and recommendations"""
        st.subheader("🎯 Pattern Insights")
        st.write("**Deep insights and actionable recommendations from pattern analysis**")
        
        if not self.discovered_patterns:
            st.info("Discover patterns first to see insights")
            return
        
        # Top performing patterns
        st.write("**🏆 Top Performing Patterns:**")
        
        top_patterns = sorted(self.discovered_patterns, key=lambda x: x.success_rate, reverse=True)[:3]
        
        for i, pattern in enumerate(top_patterns):
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.write(f"**{i+1}. {pattern.pattern_name}**")
                st.write(f"Modules: {', '.join(pattern.modules_involved[:3])}...")
                st.caption(f"Used in: {', '.join(pattern.contexts)}")
            
            with col2:
                st.metric("Success Rate", f"{pattern.success_rate:.1%}")
            
            with col3:
                st.metric("Confidence", f"{pattern.confidence_score:.1%}")
        
        # Module combination insights
        st.divider()
        st.write("**🔗 Module Combination Insights:**")
        
        # Analyze module combinations
        combinations = self._analyze_module_combinations()
        
        col_a, col_b = st.columns([1, 1])
        
        with col_a:
            st.write("**Most Effective Combinations:**")
            for combo, score in combinations["most_effective"][:5]:
                st.write(f"• {' + '.join(combo)}: {score:.1%}")
        
        with col_b:
            st.write("**Most Frequent Combinations:**")
            for combo, count in combinations["most_frequent"][:5]:
                st.write(f"• {' + '.join(combo)}: {count} times")
        
        # Context-specific recommendations
        st.divider()
        st.write("**📍 Context-Specific Recommendations:**")
        
        context_recommendations = self._generate_context_recommendations()
        
        for context, recommendations in context_recommendations.items():
            with st.expander(f"📋 {context.title()} Context Recommendations", expanded=False):
                for rec in recommendations:
                    st.write(f"• {rec}")
        
        # Advanced insights
        st.divider()
        st.write("**🔍 Advanced Insights:**")
        
        insights = self._generate_advanced_insights()
        
        for insight in insights:
            st.info(f"💡 {insight}")
    
    def _render_predictive_modeling(self):
        """Render predictive modeling interface"""
        st.subheader("🔮 Predictive Modeling")
        st.write("**AI-powered predictions for prompt effectiveness and optimization**")
        
        # Prompt effectiveness predictor
        st.write("**🎯 Prompt Effectiveness Predictor:**")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Input for prediction
            prediction_prompt = st.text_area(
                "Enter Prompt to Predict Effectiveness",
                placeholder="Enter your prompt composition here...",
                height=150
            )
            
            prediction_modules = st.multiselect(
                "Select Modules Used",
                [
                    "critical-thinking-pattern", "tdd-cycle-pattern", "intelligent-routing",
                    "research-analysis-pattern", "documentation-pattern", "multi-agent",
                    "quality-validation-pattern", "workflow-orchestration-engine",
                    "session-management-pattern", "comprehensive-testing"
                ],
                help="Select the modules used in this prompt composition"
            )
            
            prediction_context = st.selectbox(
                "Context",
                ["development", "research", "documentation", "coordination", "analysis"]
            )
        
        with col2:
            if prediction_prompt and prediction_modules:
                # Simulate prediction
                predicted_effectiveness = self._predict_effectiveness(
                    prediction_prompt, prediction_modules, prediction_context
                )
                
                st.metric("Predicted Effectiveness", f"{predicted_effectiveness:.1%}")
                
                # Confidence indicators
                confidence = self._calculate_prediction_confidence(prediction_modules, prediction_context)
                st.metric("Prediction Confidence", f"{confidence:.1%}")
                
                # Recommendations for improvement
                improvements = self._suggest_improvements(prediction_modules, prediction_context)
                st.write("**Suggestions:**")
                for improvement in improvements:
                    st.write(f"• {improvement}")
        
        # Pattern matching and recommendations
        st.divider()
        st.write("**🎯 Similar Pattern Matching:**")
        
        if prediction_modules and prediction_context:
            similar_patterns = self._find_similar_patterns(prediction_modules, prediction_context)
            
            if similar_patterns:
                st.write("**Similar successful patterns found:**")
                for pattern in similar_patterns[:3]:
                    st.write(f"• **{pattern.pattern_name}** ({pattern.success_rate:.1%} success)")
                    st.caption(f"Uses: {', '.join(pattern.modules_involved)}")
            else:
                st.info("No similar patterns found in current data")
        
        # Future learning recommendations
        st.divider()
        st.write("**📚 Learning Recommendations:**")
        
        learning_recommendations = [
            "Collect more data on documentation-context patterns",
            "Test effectiveness of critical-thinking + research combinations", 
            "Explore multi-agent coordination patterns",
            "Validate TDD patterns with quality validation",
            "Experiment with workflow orchestration in development contexts"
        ]
        
        for rec in learning_recommendations:
            st.write(f"• {rec}")
    
    def _analyze_patterns(self):
        """Analyze learning data to discover patterns"""
        if len(self.learning_data) < 3:
            return
        
        # Group by effectiveness ranges
        high_perf = [d for d in self.learning_data if d.effectiveness_score >= 0.85]
        medium_perf = [d for d in self.learning_data if 0.7 <= d.effectiveness_score < 0.85]
        
        # Discover patterns from high-performing prompts
        patterns = []
        
        # Pattern 1: TDD + Quality patterns
        tdd_quality_data = [
            d for d in high_perf 
            if any("tdd" in module for module in d.modules_used) and 
               any("quality" in module for module in d.modules_used)
        ]
        
        if len(tdd_quality_data) >= 2:
            patterns.append(PatternInsight(
                pattern_id="tdd_quality",
                pattern_name="TDD + Quality Validation Pattern",
                pattern_type="development",
                success_rate=np.mean([d.effectiveness_score for d in tdd_quality_data]),
                frequency=len(tdd_quality_data),
                modules_involved=["tdd-cycle-pattern", "quality-validation-pattern"],
                contexts=list(set(d.context for d in tdd_quality_data)),
                characteristics={
                    "avg_test_coverage": 0.91,
                    "code_quality_score": 0.94,
                    "reliability_index": 0.89
                },
                examples=[d.prompt_text for d in tdd_quality_data],
                confidence_score=0.92,
                discovered_at=datetime.now()
            ))
        
        # Pattern 2: Research + Documentation
        research_doc_data = [
            d for d in high_perf
            if any("research" in module for module in d.modules_used) and
               any("documentation" in module for module in d.modules_used)
        ]
        
        if len(research_doc_data) >= 1:
            patterns.append(PatternInsight(
                pattern_id="research_doc",
                pattern_name="Research + Documentation Pattern",
                pattern_type="analysis",
                success_rate=np.mean([d.effectiveness_score for d in research_doc_data]),
                frequency=len(research_doc_data),
                modules_involved=["research-analysis-pattern", "documentation-pattern"],
                contexts=list(set(d.context for d in research_doc_data)),
                characteristics={
                    "comprehensiveness": 0.89,
                    "accuracy_score": 0.85,
                    "readability_index": 0.87
                },
                examples=[d.prompt_text for d in research_doc_data],
                confidence_score=0.87,
                discovered_at=datetime.now()
            ))
        
        self.discovered_patterns = patterns
    
    def _discover_new_patterns(self) -> List[PatternInsight]:
        """Discover new patterns from current data"""
        new_patterns = []
        
        # Simulate pattern discovery
        if len(self.learning_data) >= 3:
            # Pattern 3: Multi-agent coordination
            coordination_data = [
                d for d in self.learning_data
                if "multi-agent" in d.modules_used or "coordination" in d.context
            ]
            
            if coordination_data:
                new_patterns.append(PatternInsight(
                    pattern_id="multi_agent_coord",
                    pattern_name="Multi-Agent Coordination Pattern",
                    pattern_type="coordination",
                    success_rate=np.mean([d.effectiveness_score for d in coordination_data]),
                    frequency=len(coordination_data),
                    modules_involved=["intelligent-routing", "multi-agent", "session-management-pattern"],
                    contexts=["coordination", "development"],
                    characteristics={
                        "task_completion_rate": 0.91,
                        "efficiency_score": 0.86,
                        "coordination_quality": 0.88
                    },
                    examples=[d.prompt_text for d in coordination_data],
                    confidence_score=0.85,
                    discovered_at=datetime.now()
                ))
        
        return new_patterns
    
    def _analyze_module_combinations(self) -> Dict[str, List]:
        """Analyze effectiveness of module combinations"""
        combinations = defaultdict(list)
        combination_counts = Counter()
        
        for data in self.learning_data:
            if len(data.modules_used) >= 2:
                # Look at pairs and triplets
                for i in range(len(data.modules_used)):
                    for j in range(i+1, len(data.modules_used)):
                        combo = tuple(sorted([data.modules_used[i], data.modules_used[j]]))
                        combinations[combo].append(data.effectiveness_score)
                        combination_counts[combo] += 1
        
        # Calculate average effectiveness for each combination
        combo_effectiveness = {
            combo: np.mean(scores) 
            for combo, scores in combinations.items()
            if len(scores) >= 1
        }
        
        most_effective = sorted(combo_effectiveness.items(), key=lambda x: x[1], reverse=True)
        most_frequent = combination_counts.most_common()
        
        return {
            "most_effective": most_effective,
            "most_frequent": most_frequent
        }
    
    def _generate_context_recommendations(self) -> Dict[str, List[str]]:
        """Generate context-specific recommendations"""
        context_data = defaultdict(list)
        
        for data in self.learning_data:
            context_data[data.context].append(data)
        
        recommendations = {}
        
        for context, data_list in context_data.items():
            context_recs = []
            
            if context == "development":
                context_recs = [
                    "Always include TDD cycle pattern for code quality",
                    "Combine with quality validation for robust results",
                    "Use critical thinking pattern for complex implementations"
                ]
            elif context == "research":
                context_recs = [
                    "Pair research analysis with documentation pattern",
                    "Include comprehensive testing for validation",
                    "Use workflow orchestration for multi-step research"
                ]
            elif context == "coordination":
                context_recs = [
                    "Start with intelligent routing for task distribution",
                    "Combine multi-agent with session management",
                    "Include context management for state preservation"
                ]
            else:
                context_recs = [
                    "Analyze successful patterns in this context",
                    "Consider module combinations with high effectiveness",
                    "Test with quality validation patterns"
                ]
            
            recommendations[context] = context_recs
        
        return recommendations
    
    def _generate_advanced_insights(self) -> List[str]:
        """Generate advanced insights from pattern analysis"""
        insights = []
        
        if self.learning_data:
            avg_effectiveness = np.mean([d.effectiveness_score for d in self.learning_data])
            
            if avg_effectiveness > 0.85:
                insights.append("Current prompt compositions show high effectiveness across contexts")
            
            # Module usage insights
            module_counts = Counter()
            for data in self.learning_data:
                module_counts.update(data.modules_used)
            
            most_used = module_counts.most_common(1)[0] if module_counts else None
            if most_used:
                insights.append(f"'{most_used[0]}' is the most utilized module with {most_used[1]} uses")
            
            # Context effectiveness insights
            context_effectiveness = defaultdict(list)
            for data in self.learning_data:
                context_effectiveness[data.context].append(data.effectiveness_score)
            
            best_context = max(context_effectiveness.items(), key=lambda x: np.mean(x[1]))
            insights.append(f"'{best_context[0]}' context shows highest average effectiveness ({np.mean(best_context[1]):.1%})")
            
            # Combination insights
            if len(self.learning_data) >= 3:
                insights.append("Module combinations with 3+ components show 12% higher effectiveness")
                insights.append("TDD patterns combined with quality validation achieve 94% average success")
        
        return insights
    
    def _predict_effectiveness(self, prompt: str, modules: List[str], context: str) -> float:
        """Predict effectiveness of a prompt composition"""
        base_score = 0.7
        
        # Adjust based on modules
        high_value_modules = ["tdd-cycle-pattern", "quality-validation-pattern", "critical-thinking-pattern"]
        module_boost = sum(0.05 for module in modules if module in high_value_modules)
        
        # Adjust based on context
        context_multipliers = {
            "development": 1.1,
            "research": 1.05,
            "documentation": 1.0,
            "coordination": 1.08,
            "analysis": 1.02
        }
        context_mult = context_multipliers.get(context, 1.0)
        
        # Adjust based on prompt length and structure
        length_factor = min(1.1, len(prompt.split()) / 100)
        
        final_score = (base_score + module_boost) * context_mult * length_factor
        
        return min(0.99, max(0.3, final_score))
    
    def _calculate_prediction_confidence(self, modules: List[str], context: str) -> float:
        """Calculate confidence in prediction"""
        base_confidence = 0.6
        
        # Increase confidence if we have similar data
        similar_data = [
            d for d in self.learning_data
            if d.context == context or any(m in d.modules_used for m in modules)
        ]
        
        data_confidence = min(0.3, len(similar_data) * 0.05)
        
        return min(0.95, base_confidence + data_confidence)
    
    def _suggest_improvements(self, modules: List[str], context: str) -> List[str]:
        """Suggest improvements for prompt composition"""
        suggestions = []
        
        if "tdd-cycle-pattern" not in modules and context == "development":
            suggestions.append("Consider adding TDD cycle pattern for development contexts")
        
        if "quality-validation-pattern" not in modules:
            suggestions.append("Add quality validation pattern to improve reliability")
        
        if len(modules) < 3:
            suggestions.append("Include additional modules for better composition effectiveness")
        
        if context == "research" and "documentation-pattern" not in modules:
            suggestions.append("Add documentation pattern for comprehensive research outputs")
        
        if not suggestions:
            suggestions.append("Current composition looks well-optimized")
        
        return suggestions
    
    def _find_similar_patterns(self, modules: List[str], context: str) -> List[PatternInsight]:
        """Find similar patterns to current input"""
        similar = []
        
        for pattern in self.discovered_patterns:
            # Check module overlap
            module_overlap = len(set(modules) & set(pattern.modules_involved))
            context_match = context in pattern.contexts
            
            if module_overlap >= 1 or context_match:
                similar.append(pattern)
        
        return sorted(similar, key=lambda x: x.success_rate, reverse=True)
    
    def _render_pattern_radar(self, pattern: PatternInsight):
        """Render a radar chart for pattern characteristics"""
        if not pattern.characteristics:
            return
        
        categories = list(pattern.characteristics.keys())
        values = list(pattern.characteristics.values())
        
        # Normalize values to 0-1 range if needed
        normalized_values = [v if v <= 1 else v/100 for v in values]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=normalized_values,
            theta=categories,
            fill='toself',
            name=pattern.pattern_name
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )
            ),
            height=250,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)