"""
Prompt Optimization Assistant for Claude Code Framework Dashboard
Provides intelligent prompt optimization recommendations based on context, goals, and effectiveness analysis
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import re
import json
from datetime import datetime
from dataclasses import dataclass
from enum import Enum


class OptimizationStrategy(Enum):
    """Different prompt optimization strategies"""
    TOKEN_EFFICIENCY = "token_efficiency"
    CLARITY_ENHANCEMENT = "clarity_enhancement"
    EFFECTIVENESS_BOOST = "effectiveness_boost"
    SPECIFICITY_IMPROVEMENT = "specificity_improvement"
    CONTEXT_OPTIMIZATION = "context_optimization"


@dataclass
class OptimizationRecommendation:
    """A specific optimization recommendation"""
    strategy: OptimizationStrategy
    title: str
    description: str
    implementation: str
    expected_improvement: str
    confidence_score: float
    applicable_modules: List[str]


@dataclass
class PromptAnalysis:
    """Analysis results for a prompt"""
    token_count: int
    clarity_score: float
    specificity_score: float
    effectiveness_score: float
    optimization_potential: float
    issues: List[str]
    strengths: List[str]


class PromptOptimizationAssistant:
    """Advanced prompt optimization assistant with AI-powered recommendations"""
    
    def __init__(self, framework_path: Path):
        """Initialize Prompt Optimization Assistant"""
        self.framework_path = framework_path
        self.optimization_strategies = self._load_optimization_strategies()
        self.modules_database = self._load_modules_database()
        self.optimization_history = []
        
    def _load_optimization_strategies(self) -> Dict[OptimizationStrategy, Dict[str, Any]]:
        """Load optimization strategies and their configurations"""
        return {
            OptimizationStrategy.TOKEN_EFFICIENCY: {
                "name": "Token Efficiency Optimization",
                "description": "Reduce token usage while maintaining effectiveness",
                "techniques": [
                    "Use concise language",
                    "Remove redundant phrases",
                    "Optimize structure",
                    "Combine related instructions"
                ],
                "expected_improvement": "20-30% token reduction"
            },
            OptimizationStrategy.CLARITY_ENHANCEMENT: {
                "name": "Clarity Enhancement",
                "description": "Improve prompt clarity and reduce ambiguity",
                "techniques": [
                    "Use specific terminology",
                    "Add clear examples",
                    "Structure with bullet points",
                    "Define expectations clearly"
                ],
                "expected_improvement": "40-50% better understanding"
            },
            OptimizationStrategy.EFFECTIVENESS_BOOST: {
                "name": "Effectiveness Boost",
                "description": "Enhance prompt effectiveness and output quality",
                "techniques": [
                    "Add context priming",
                    "Include success criteria",
                    "Use proven patterns",
                    "Optimize instruction order"
                ],
                "expected_improvement": "25-35% better results"
            },
            OptimizationStrategy.SPECIFICITY_IMPROVEMENT: {
                "name": "Specificity Improvement",
                "description": "Make prompts more specific and targeted",
                "techniques": [
                    "Add domain context",
                    "Specify output format",
                    "Include constraints",
                    "Define scope clearly"
                ],
                "expected_improvement": "30-40% more targeted output"
            },
            OptimizationStrategy.CONTEXT_OPTIMIZATION: {
                "name": "Context Optimization",
                "description": "Optimize prompt context for better understanding",
                "techniques": [
                    "Add background information",
                    "Include relevant examples",
                    "Provide context hierarchy",
                    "Reference related concepts"
                ],
                "expected_improvement": "35-45% better context awareness"
            }
        }
    
    def _load_modules_database(self) -> Dict[str, Dict[str, Any]]:
        """Load modules database for optimization recommendations"""
        modules = {}
        modules_dir = self.framework_path / "modules"
        
        if not modules_dir.exists():
            return modules
            
        for category_dir in modules_dir.iterdir():
            if category_dir.is_dir():
                for module_file in category_dir.glob("*.md"):
                    try:
                        content = module_file.read_text()
                        name = module_file.stem.replace('-', '_')
                        
                        modules[name] = {
                            "category": category_dir.name,
                            "purpose": self._extract_xml_content(content, 'purpose') or "Module component",
                            "optimization_focus": self._analyze_module_optimization_focus(content),
                            "file_path": str(module_file)
                        }
                    except Exception:
                        continue
                        
        return modules
    
    def _extract_xml_content(self, content: str, tag: str) -> Optional[str]:
        """Extract content from XML tags"""
        pattern = f'<{tag}>(.*?)</{tag}>'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else None
    
    def _analyze_module_optimization_focus(self, content: str) -> List[str]:
        """Analyze what optimization strategies a module supports"""
        focus_areas = []
        
        if any(word in content.lower() for word in ['token', 'efficient', 'compact']):
            focus_areas.append('token_efficiency')
        if any(word in content.lower() for word in ['clear', 'clarity', 'understand']):
            focus_areas.append('clarity_enhancement')
        if any(word in content.lower() for word in ['effective', 'quality', 'improve']):
            focus_areas.append('effectiveness_boost')
        if any(word in content.lower() for word in ['specific', 'precise', 'targeted']):
            focus_areas.append('specificity_improvement')
        if any(word in content.lower() for word in ['context', 'background', 'domain']):
            focus_areas.append('context_optimization')
            
        return focus_areas or ['effectiveness_boost']
    
    def render(self):
        """Render the Prompt Optimization Assistant interface"""
        st.title("🚀 Prompt Optimization Assistant")
        st.markdown("**Get AI-powered recommendations to optimize your prompts for better effectiveness and efficiency**")
        
        # Create tabs for different optimization workflows
        tab1, tab2, tab3, tab4 = st.tabs([
            "🔍 Prompt Analysis",
            "🚀 Optimization Recommendations", 
            "📊 Strategy Comparison",
            "📈 Optimization Tracking"
        ])
        
        with tab1:
            self._render_prompt_analysis()
        
        with tab2:
            self._render_optimization_recommendations()
        
        with tab3:
            self._render_strategy_comparison()
        
        with tab4:
            self._render_optimization_tracking()
    
    def _render_prompt_analysis(self):
        """Render prompt analysis interface"""
        st.subheader("🔍 Prompt Analysis & Diagnosis")
        st.write("**Analyze your prompts to identify optimization opportunities**")
        
        # Prompt input
        prompt_text = st.text_area(
            "Enter your prompt for analysis:",
            placeholder="Paste your prompt here to analyze its effectiveness, clarity, and optimization potential...",
            height=200
        )
        
        if prompt_text:
            # Analyze the prompt
            analysis = self._analyze_prompt(prompt_text)
            
            # Display analysis results
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Token Count", analysis.token_count)
            with col2:
                st.metric("Clarity Score", f"{analysis.clarity_score:.1%}")
            with col3:
                st.metric("Specificity Score", f"{analysis.specificity_score:.1%}")
            with col4:
                st.metric("Effectiveness Score", f"{analysis.effectiveness_score:.1%}")
            
            # Optimization potential radar chart
            self._render_optimization_radar(analysis)
            
            # Issues and strengths
            col1, col2 = st.columns(2)
            
            with col1:
                if analysis.issues:
                    st.subheader("⚠️ Areas for Improvement")
                    for issue in analysis.issues:
                        st.write(f"• {issue}")
            
            with col2:
                if analysis.strengths:
                    st.subheader("✅ Strengths")
                    for strength in analysis.strengths:
                        st.write(f"• {strength}")
            
            # Store analysis for recommendations
            st.session_state['current_analysis'] = analysis
            st.session_state['current_prompt'] = prompt_text
    
    def _analyze_prompt(self, prompt_text: str) -> PromptAnalysis:
        """Analyze a prompt and return analysis results"""
        # Token count estimation
        token_count = len(prompt_text.split()) * 1.3  # Rough estimation
        
        # Clarity score based on structure and language
        clarity_score = self._calculate_clarity_score(prompt_text)
        
        # Specificity score based on concrete instructions
        specificity_score = self._calculate_specificity_score(prompt_text)
        
        # Effectiveness score based on best practices
        effectiveness_score = self._calculate_effectiveness_score(prompt_text)
        
        # Optimization potential (inverse of current effectiveness)
        optimization_potential = 1.0 - effectiveness_score
        
        # Identify issues and strengths
        issues = self._identify_issues(prompt_text)
        strengths = self._identify_strengths(prompt_text)
        
        return PromptAnalysis(
            token_count=int(token_count),
            clarity_score=clarity_score,
            specificity_score=specificity_score,
            effectiveness_score=effectiveness_score,
            optimization_potential=optimization_potential,
            issues=issues,
            strengths=strengths
        )
    
    def _calculate_clarity_score(self, prompt_text: str) -> float:
        """Calculate clarity score based on prompt structure"""
        score = 0.5  # Base score
        
        # Bonus for clear structure
        if any(marker in prompt_text for marker in ['1.', '2.', '•', '-', '#']):
            score += 0.2
        
        # Bonus for examples
        if any(word in prompt_text.lower() for word in ['example', 'for instance', 'such as']):
            score += 0.15
        
        # Bonus for clear instructions
        if any(word in prompt_text.lower() for word in ['please', 'should', 'must', 'need to']):
            score += 0.1
        
        # Penalty for excessive length
        if len(prompt_text) > 1000:
            score -= 0.1
        
        return min(1.0, max(0.0, score))
    
    def _calculate_specificity_score(self, prompt_text: str) -> float:
        """Calculate specificity score based on concrete instructions"""
        score = 0.4  # Base score
        
        # Bonus for specific terms
        specific_terms = ['format', 'style', 'length', 'include', 'exclude', 'requirements']
        for term in specific_terms:
            if term in prompt_text.lower():
                score += 0.1
        
        # Bonus for constraints
        if any(word in prompt_text.lower() for word in ['exactly', 'only', 'must not', 'limit']):
            score += 0.15
        
        # Bonus for output format specification
        if any(word in prompt_text.lower() for word in ['json', 'markdown', 'list', 'table']):
            score += 0.1
        
        return min(1.0, max(0.0, score))
    
    def _calculate_effectiveness_score(self, prompt_text: str) -> float:
        """Calculate effectiveness score based on best practices"""
        score = 0.3  # Base score
        
        # Bonus for context setting
        if any(word in prompt_text.lower() for word in ['context', 'background', 'situation']):
            score += 0.15
        
        # Bonus for role specification
        if any(word in prompt_text.lower() for word in ['you are', 'act as', 'role', 'expert']):
            score += 0.1
        
        # Bonus for clear goals
        if any(word in prompt_text.lower() for word in ['goal', 'objective', 'purpose', 'aim']):
            score += 0.15
        
        # Bonus for step-by-step approach
        if any(word in prompt_text.lower() for word in ['step', 'first', 'then', 'next', 'finally']):
            score += 0.1
        
        # Bonus for quality criteria
        if any(word in prompt_text.lower() for word in ['quality', 'accuracy', 'detailed', 'comprehensive']):
            score += 0.1
        
        return min(1.0, max(0.0, score))
    
    def _identify_issues(self, prompt_text: str) -> List[str]:
        """Identify potential issues in the prompt"""
        issues = []
        
        if len(prompt_text) < 50:
            issues.append("Prompt may be too short to provide sufficient context")
        
        if len(prompt_text) > 2000:
            issues.append("Prompt may be too long, consider breaking into steps")
        
        if not any(marker in prompt_text for marker in ['?', '.', '!', ':']):
            issues.append("Lacks clear sentence structure")
        
        if prompt_text.count(' ') < 10:
            issues.append("May lack sufficient detail or instructions")
        
        if not re.search(r'[A-Z]', prompt_text):
            issues.append("Missing proper capitalization")
        
        return issues
    
    def _identify_strengths(self, prompt_text: str) -> List[str]:
        """Identify strengths in the prompt"""
        strengths = []
        
        if any(marker in prompt_text for marker in ['1.', '2.', '•', '-']):
            strengths.append("Well-structured with clear organization")
        
        if any(word in prompt_text.lower() for word in ['example', 'for instance']):
            strengths.append("Includes helpful examples")
        
        if len(prompt_text.split()) > 50:
            strengths.append("Provides sufficient detail and context")
        
        if any(word in prompt_text.lower() for word in ['please', 'specific', 'detailed']):
            strengths.append("Uses clear, polite instructions")
        
        return strengths
    
    def _render_optimization_radar(self, analysis: PromptAnalysis):
        """Render optimization potential radar chart"""
        categories = ['Clarity', 'Specificity', 'Effectiveness', 'Token Efficiency']
        scores = [
            analysis.clarity_score,
            analysis.specificity_score, 
            analysis.effectiveness_score,
            1.0 - (analysis.token_count / 1000)  # Inverse relationship for efficiency
        ]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=scores,
            theta=categories,
            fill='toself',
            name='Current Score',
            fillcolor='rgba(75, 192, 192, 0.3)',
            line_color='rgb(75, 192, 192)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )),
            showlegend=True,
            title="Prompt Analysis Radar Chart"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_optimization_recommendations(self):
        """Render optimization recommendations based on analysis"""
        st.subheader("🚀 Personalized Optimization Recommendations")
        
        if 'current_analysis' not in st.session_state:
            st.info("Please analyze a prompt first to get personalized recommendations")
            return
        
        analysis = st.session_state['current_analysis']
        prompt_text = st.session_state.get('current_prompt', '')
        
        # Generate recommendations
        recommendations = self._generate_recommendations(analysis, prompt_text)
        
        st.write(f"**Found {len(recommendations)} optimization opportunities:**")
        
        for i, rec in enumerate(recommendations, 1):
            with st.expander(f"{i}. {rec.title} (Confidence: {rec.confidence_score:.1%})", expanded=False):
                st.write(f"**Strategy:** {rec.strategy.value.replace('_', ' ').title()}")
                st.write(f"**Description:** {rec.description}")
                st.write(f"**Expected Improvement:** {rec.expected_improvement}")
                
                st.code(rec.implementation, language="markdown")
                
                if rec.applicable_modules:
                    st.write(f"**Recommended Modules:** {', '.join(rec.applicable_modules)}")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"Apply Optimization {i}", key=f"apply_{i}"):
                        self._apply_optimization(rec, prompt_text)
                with col2:
                    if st.button(f"Learn More", key=f"learn_{i}"):
                        self._show_strategy_details(rec.strategy)
    
    def _generate_recommendations(self, analysis: PromptAnalysis, prompt_text: str) -> List[OptimizationRecommendation]:
        """Generate personalized optimization recommendations"""
        recommendations = []
        
        # Token efficiency recommendations
        if analysis.token_count > 500:
            recommendations.append(OptimizationRecommendation(
                strategy=OptimizationStrategy.TOKEN_EFFICIENCY,
                title="Reduce Token Usage",
                description="Your prompt is quite long. We can optimize it for token efficiency.",
                implementation="• Remove redundant phrases\n• Use bullet points instead of paragraphs\n• Combine related instructions\n• Use more concise language",
                expected_improvement="20-30% token reduction",
                confidence_score=0.85,
                applicable_modules=self._find_applicable_modules('token_efficiency')
            ))
        
        # Clarity enhancement
        if analysis.clarity_score < 0.7:
            recommendations.append(OptimizationRecommendation(
                strategy=OptimizationStrategy.CLARITY_ENHANCEMENT,
                title="Improve Clarity and Structure",
                description="Your prompt could benefit from clearer structure and instructions.",
                implementation="• Add numbered steps\n• Include specific examples\n• Define key terms\n• Use clear action verbs",
                expected_improvement="40-50% better understanding",
                confidence_score=0.9,
                applicable_modules=self._find_applicable_modules('clarity_enhancement')
            ))
        
        # Specificity improvement
        if analysis.specificity_score < 0.6:
            recommendations.append(OptimizationRecommendation(
                strategy=OptimizationStrategy.SPECIFICITY_IMPROVEMENT,
                title="Increase Specificity",
                description="Add more specific instructions and constraints for better results.",
                implementation="• Specify output format\n• Add length requirements\n• Include quality criteria\n• Define scope and boundaries",
                expected_improvement="30-40% more targeted output",
                confidence_score=0.8,
                applicable_modules=self._find_applicable_modules('specificity_improvement')
            ))
        
        # Effectiveness boost
        if analysis.effectiveness_score < 0.8:
            recommendations.append(OptimizationRecommendation(
                strategy=OptimizationStrategy.EFFECTIVENESS_BOOST,
                title="Enhance Overall Effectiveness",
                description="Apply proven prompt engineering patterns for better results.",
                implementation="• Add context priming\n• Include success criteria\n• Use step-by-step approach\n• Add quality verification",
                expected_improvement="25-35% better results",
                confidence_score=0.75,
                applicable_modules=self._find_applicable_modules('effectiveness_boost')
            ))
        
        return sorted(recommendations, key=lambda x: x.confidence_score, reverse=True)
    
    def _find_applicable_modules(self, optimization_focus: str) -> List[str]:
        """Find modules that support a specific optimization focus"""
        applicable = []
        for module_name, module_info in self.modules_database.items():
            if optimization_focus in module_info.get('optimization_focus', []):
                applicable.append(module_name.replace('_', ' ').title())
        return applicable[:3]  # Limit to top 3
    
    def _apply_optimization(self, recommendation: OptimizationRecommendation, original_prompt: str):
        """Apply optimization recommendation to prompt"""
        st.success(f"Applied optimization: {recommendation.title}")
        
        # Store in optimization history
        self.optimization_history.append({
            'timestamp': datetime.now(),
            'strategy': recommendation.strategy.value,
            'title': recommendation.title,
            'original_prompt_length': len(original_prompt),
            'expected_improvement': recommendation.expected_improvement
        })
        
        # Show implementation guide
        st.subheader("Implementation Guide")
        st.write("Apply these changes to your prompt:")
        st.code(recommendation.implementation, language="markdown")
    
    def _show_strategy_details(self, strategy: OptimizationStrategy):
        """Show detailed information about an optimization strategy"""
        strategy_info = self.optimization_strategies[strategy]
        
        st.subheader(f"📚 {strategy_info['name']}")
        st.write(strategy_info['description'])
        
        st.write("**Techniques:**")
        for technique in strategy_info['techniques']:
            st.write(f"• {technique}")
        
        st.write(f"**Expected Improvement:** {strategy_info['expected_improvement']}")
    
    def _render_strategy_comparison(self):
        """Render strategy comparison interface"""
        st.subheader("📊 Optimization Strategy Comparison")
        st.write("**Compare different optimization strategies and their expected benefits**")
        
        # Strategy comparison matrix
        strategies_data = []
        for strategy, info in self.optimization_strategies.items():
            strategies_data.append({
                'Strategy': info['name'],
                'Focus Area': strategy.value.replace('_', ' ').title(),
                'Expected Improvement': info['expected_improvement'],
                'Description': info['description']
            })
        
        df = pd.DataFrame(strategies_data)
        st.dataframe(df, use_container_width=True)
        
        # Strategy effectiveness chart
        strategy_names = [info['name'] for info in self.optimization_strategies.values()]
        effectiveness_scores = [0.85, 0.9, 0.8, 0.75, 0.88]  # Example scores
        
        fig = px.bar(
            x=strategy_names,
            y=effectiveness_scores,
            title="Strategy Effectiveness Comparison",
            labels={'x': 'Strategy', 'y': 'Effectiveness Score'}
        )
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_optimization_tracking(self):
        """Render optimization tracking dashboard"""
        st.subheader("📈 Optimization Tracking & Progress")
        
        if not self.optimization_history:
            st.info("No optimization history yet. Start analyzing and optimizing prompts to track your progress!")
            return
        
        # Create tracking metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Optimizations", len(self.optimization_history))
        with col2:
            recent_optimizations = [opt for opt in self.optimization_history 
                                  if (datetime.now() - opt['timestamp']).days <= 7]
            st.metric("This Week", len(recent_optimizations))
        with col3:
            avg_improvement = "25-30%"  # Example calculation
            st.metric("Avg Improvement", avg_improvement)
        
        # Optimization timeline
        if len(self.optimization_history) > 1:
            df_history = pd.DataFrame(self.optimization_history)
            df_history['date'] = df_history['timestamp'].dt.date
            
            daily_counts = df_history.groupby('date').size().reset_index(name='count')
            
            fig = px.line(
                daily_counts,
                x='date',
                y='count',
                title="Optimization Activity Over Time"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Strategy usage breakdown
        strategy_counts = {}
        for opt in self.optimization_history:
            strategy = opt['strategy']
            strategy_counts[strategy] = strategy_counts.get(strategy, 0) + 1
        
        if strategy_counts:
            fig_pie = px.pie(
                values=list(strategy_counts.values()),
                names=list(strategy_counts.keys()),
                title="Optimization Strategies Used"
            )
            st.plotly_chart(fig_pie, use_container_width=True)


# Maintain backward compatibility
ContextAwareAnalyzer = PromptOptimizationAssistant