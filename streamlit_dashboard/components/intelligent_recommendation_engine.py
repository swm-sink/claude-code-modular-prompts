"""
Intelligent Recommendation Engine for Claude Code Framework Dashboard
Advanced AI-powered system that provides optimal module combinations and prompt engineering recommendations
"""
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import json
from collections import defaultdict, Counter
import math


@dataclass
class ModuleRecommendation:
    """Represents a module recommendation"""
    module_name: str
    reason: str
    confidence: float
    expected_improvement: float
    compatibility_score: float
    usage_context: str
    evidence: List[str]


@dataclass 
class CompositionRecommendation:
    """Represents a complete prompt composition recommendation"""
    composition_id: str
    name: str
    modules: List[str]
    expected_effectiveness: float
    confidence: float
    use_cases: List[str]
    pros: List[str]
    cons: List[str]
    optimization_tips: List[str]


@dataclass
class UserProfile:
    """Represents a user's prompt engineering profile"""
    user_id: str
    preferred_contexts: List[str]
    skill_level: str
    frequently_used_modules: List[str]
    effectiveness_history: List[float]
    learning_goals: List[str]


class IntelligentRecommendationEngine:
    """Advanced recommendation engine for optimal prompt engineering"""
    
    def __init__(self, framework_path: Path):
        """Initialize Intelligent Recommendation Engine"""
        self.framework_path = framework_path
        self.user_profiles = {}
        self.current_user = "default_user"
        self.recommendation_history = []
        self.module_database = self._load_module_database()
        self.effectiveness_matrix = self._build_effectiveness_matrix()
        self._initialize_demo_profile()
        
    def _load_module_database(self) -> Dict[str, Dict[str, Any]]:
        """Load comprehensive module database with metadata"""
        return {
            "critical-thinking-pattern": {
                "category": "thinking",
                "complexity": "medium", 
                "effectiveness_base": 0.85,
                "token_efficiency": 0.78,
                "contexts": ["analysis", "development", "research"],
                "synergies": ["tdd-cycle-pattern", "quality-validation-pattern"],
                "anti_patterns": [],
                "learning_curve": "moderate"
            },
            "tdd-cycle-pattern": {
                "category": "development",
                "complexity": "medium",
                "effectiveness_base": 0.92,
                "token_efficiency": 0.82,
                "contexts": ["development", "testing"],
                "synergies": ["quality-validation-pattern", "critical-thinking-pattern"],
                "anti_patterns": ["rapid-prototyping"],
                "learning_curve": "steep"
            },
            "intelligent-routing": {
                "category": "orchestration",
                "complexity": "high",
                "effectiveness_base": 0.88,
                "token_efficiency": 0.75,
                "contexts": ["coordination", "complex-tasks"],
                "synergies": ["multi-agent", "session-management-pattern"],
                "anti_patterns": ["simple-tasks"],
                "learning_curve": "moderate"
            },
            "research-analysis-pattern": {
                "category": "analysis", 
                "complexity": "medium",
                "effectiveness_base": 0.83,
                "token_efficiency": 0.71,
                "contexts": ["research", "analysis", "investigation"],
                "synergies": ["documentation-pattern", "critical-thinking-pattern"],
                "anti_patterns": ["rapid-execution"],
                "learning_curve": "easy"
            },
            "documentation-pattern": {
                "category": "documentation",
                "complexity": "low",
                "effectiveness_base": 0.79,
                "token_efficiency": 0.85,
                "contexts": ["documentation", "communication"],
                "synergies": ["research-analysis-pattern", "workflow-orchestration-engine"],
                "anti_patterns": [],
                "learning_curve": "easy"
            },
            "multi-agent": {
                "category": "coordination",
                "complexity": "high",
                "effectiveness_base": 0.87,
                "token_efficiency": 0.68,
                "contexts": ["coordination", "complex-tasks", "parallel-work"],
                "synergies": ["intelligent-routing", "session-management-pattern"],
                "anti_patterns": ["simple-tasks", "single-focus"],
                "learning_curve": "steep"
            },
            "quality-validation-pattern": {
                "category": "quality",
                "complexity": "medium",
                "effectiveness_base": 0.90,
                "token_efficiency": 0.80,
                "contexts": ["development", "validation", "testing"],
                "synergies": ["tdd-cycle-pattern", "comprehensive-testing"],
                "anti_patterns": ["rapid-prototyping"],
                "learning_curve": "moderate"
            },
            "workflow-orchestration-engine": {
                "category": "orchestration",
                "complexity": "high",
                "effectiveness_base": 0.86,
                "token_efficiency": 0.73,
                "contexts": ["complex-workflows", "automation"],
                "synergies": ["session-management-pattern", "context-management-pattern"],
                "anti_patterns": ["simple-tasks"],
                "learning_curve": "steep"
            },
            "session-management-pattern": {
                "category": "management",
                "complexity": "medium",
                "effectiveness_base": 0.81,
                "token_efficiency": 0.77,
                "contexts": ["long-sessions", "state-management"],
                "synergies": ["multi-agent", "workflow-orchestration-engine"],
                "anti_patterns": ["single-shot-tasks"],
                "learning_curve": "moderate"
            },
            "comprehensive-testing": {
                "category": "testing",
                "complexity": "medium",
                "effectiveness_base": 0.84,
                "token_efficiency": 0.76,
                "contexts": ["testing", "validation", "development"],
                "synergies": ["quality-validation-pattern", "tdd-cycle-pattern"],
                "anti_patterns": ["rapid-prototyping"],
                "learning_curve": "moderate"
            }
        }
    
    def _build_effectiveness_matrix(self) -> np.ndarray:
        """Build effectiveness matrix for module combinations"""
        modules = list(self.module_database.keys())
        n = len(modules)
        matrix = np.eye(n)  # Start with identity matrix
        
        # Add synergy bonuses
        for i, module_a in enumerate(modules):
            synergies = self.module_database[module_a]["synergies"]
            for j, module_b in enumerate(modules):
                if module_b in synergies:
                    matrix[i][j] = 1.15  # 15% synergy bonus
                elif module_a != module_b:
                    matrix[i][j] = 1.05  # 5% general combination bonus
        
        return matrix
    
    def _initialize_demo_profile(self):
        """Initialize demo user profile"""
        self.user_profiles[self.current_user] = UserProfile(
            user_id=self.current_user,
            preferred_contexts=["development", "research"],
            skill_level="intermediate",
            frequently_used_modules=["tdd-cycle-pattern", "critical-thinking-pattern", "documentation-pattern"],
            effectiveness_history=[0.85, 0.82, 0.89, 0.87, 0.91],
            learning_goals=["improve code quality", "faster development", "better documentation"]
        )
    
    def render(self):
        """Render the Intelligent Recommendation Engine interface"""
        st.title("🎯 Intelligent Recommendation Engine")
        st.write("**AI-powered recommendations for optimal module combinations and prompt engineering strategies**")
        
        # Create tabs for different recommendation types
        tab1, tab2, tab3, tab4 = st.tabs([
            "🎯 Smart Recommendations",
            "🔧 Module Optimizer", 
            "👤 Personalized Assistant",
            "📊 Learning Analytics"
        ])
        
        with tab1:
            self._render_smart_recommendations()
        
        with tab2:
            self._render_module_optimizer()
        
        with tab3:
            self._render_personalized_assistant()
        
        with tab4:
            self._render_learning_analytics()
    
    def _render_smart_recommendations(self):
        """Render intelligent recommendation interface"""
        st.subheader("🎯 Smart Recommendations")
        st.write("**Get AI-powered recommendations for your prompt engineering needs**")
        
        # Input section
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # User requirements input
            user_goal = st.text_input(
                "What are you trying to accomplish?",
                placeholder="e.g., Build a robust testing framework for Python code",
                help="Describe your specific goal or task"
            )
            
            context = st.selectbox(
                "Context",
                ["development", "research", "documentation", "analysis", "coordination", "testing"],
                help="Select the primary context for your work"
            )
            
            complexity = st.selectbox(
                "Task Complexity",
                ["simple", "medium", "complex"],
                index=1,
                help="How complex is your task?"
            )
            
            current_modules = st.multiselect(
                "Currently Using (optional)",
                list(self.module_database.keys()),
                help="Select modules you're already planning to use"
            )
        
        with col2:
            st.write("**Recommendation Settings:**")
            
            num_recommendations = st.slider(
                "Number of Recommendations",
                min_value=1,
                max_value=5,
                value=3
            )
            
            focus_area = st.selectbox(
                "Focus On",
                ["effectiveness", "efficiency", "learning", "innovation"],
                help="What should we optimize for?"
            )
            
            experience_level = st.selectbox(
                "Your Experience Level",
                ["beginner", "intermediate", "advanced"],
                index=1
            )
        
        # Generate recommendations
        if user_goal:
            if st.button("🚀 Get Recommendations", type="primary"):
                recommendations = self._generate_smart_recommendations(
                    user_goal, context, complexity, current_modules, 
                    num_recommendations, focus_area, experience_level
                )
                
                st.divider()
                st.write("**🎯 Recommended Compositions:**")
                
                for i, rec in enumerate(recommendations):
                    with st.expander(f"💡 {rec.name} (Effectiveness: {rec.expected_effectiveness:.1%})", 
                                   expanded=i==0):
                        
                        col_a, col_b = st.columns([2, 1])
                        
                        with col_a:
                            st.write(f"**Modules:** {', '.join(rec.modules)}")
                            st.write(f"**Use Cases:** {', '.join(rec.use_cases)}")
                            
                            st.write("**✅ Pros:**")
                            for pro in rec.pros:
                                st.write(f"• {pro}")
                            
                            if rec.cons:
                                st.write("**⚠️ Considerations:**")
                                for con in rec.cons:
                                    st.write(f"• {con}")
                        
                        with col_b:
                            st.metric("Confidence", f"{rec.confidence:.1%}")
                            st.metric("Expected Effectiveness", f"{rec.expected_effectiveness:.1%}")
                            
                            if st.button(f"Apply Composition", key=f"apply_{i}"):
                                st.success("Composition applied! Use this in your prompt builder.")
                        
                        if rec.optimization_tips:
                            st.write("**🔧 Optimization Tips:**")
                            for tip in rec.optimization_tips:
                                st.write(f"• {tip}")
        else:
            st.info("👆 Describe your goal to get personalized recommendations")
    
    def _render_module_optimizer(self):
        """Render module optimization interface"""
        st.subheader("🔧 Module Optimizer")
        st.write("**Optimize your current module selection for better performance**")
        
        # Current composition analysis
        st.write("**Current Composition Analysis:**")
        
        selected_modules = st.multiselect(
            "Select Your Current Modules",
            list(self.module_database.keys()),
            help="Choose the modules in your current composition"
        )
        
        if selected_modules:
            # Analyze current composition
            analysis = self._analyze_current_composition(selected_modules)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Current Effectiveness", f"{analysis['effectiveness']:.1%}")
            with col2:
                st.metric("Token Efficiency", f"{analysis['token_efficiency']:.1%}")
            with col3:
                st.metric("Synergy Score", f"{analysis['synergy_score']:.1%}")
            
            # Optimization recommendations
            st.divider()
            st.write("**🎯 Optimization Recommendations:**")
            
            optimizations = self._generate_optimization_recommendations(selected_modules)
            
            for opt_type, recommendations in optimizations.items():
                if recommendations:
                    st.write(f"**{opt_type.replace('_', ' ').title()}:**")
                    for rec in recommendations:
                        st.write(f"• {rec.module_name}: {rec.reason} (Confidence: {rec.confidence:.1%})")
            
            # Alternative compositions
            st.divider()
            st.write("**🔄 Alternative Compositions:**")
            
            alternatives = self._generate_alternative_compositions(selected_modules)
            
            for i, alt in enumerate(alternatives):
                col_a, col_b = st.columns([3, 1])
                
                with col_a:
                    st.write(f"**Alternative {i+1}:** {', '.join(alt['modules'])}")
                    st.caption(f"Expected improvement: +{alt['improvement']:.1%}")
                
                with col_b:
                    if st.button(f"Try This", key=f"alt_{i}"):
                        st.success("Alternative composition loaded!")
        else:
            st.info("Select modules to see optimization recommendations")
    
    def _render_personalized_assistant(self):
        """Render personalized assistant interface"""
        st.subheader("👤 Personalized Assistant")
        st.write("**Get recommendations tailored to your experience and preferences**")
        
        # User profile management
        profile = self.user_profiles.get(self.current_user)
        
        if profile:
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.write("**Your Profile:**")
                st.write(f"**Skill Level:** {profile.skill_level}")
                st.write(f"**Preferred Contexts:** {', '.join(profile.preferred_contexts)}")
                st.write(f"**Avg Effectiveness:** {np.mean(profile.effectiveness_history):.1%}")
                
                # Recent performance trend
                if len(profile.effectiveness_history) >= 3:
                    recent_trend = profile.effectiveness_history[-3:]
                    trend_direction = "📈" if recent_trend[-1] > recent_trend[0] else "📉"
                    st.write(f"**Recent Trend:** {trend_direction}")
            
            with col2:
                st.write("**Frequently Used Modules:**")
                for module in profile.frequently_used_modules:
                    effectiveness = self.module_database[module]["effectiveness_base"]
                    st.write(f"• {module} ({effectiveness:.1%})")
                
                st.write("**Learning Goals:**")
                for goal in profile.learning_goals:
                    st.write(f"• {goal}")
            
            # Personalized recommendations
            st.divider()
            st.write("**🎯 Personalized Recommendations:**")
            
            personal_recs = self._generate_personalized_recommendations(profile)
            
            for category, recs in personal_recs.items():
                if recs:
                    with st.expander(f"📋 {category.replace('_', ' ').title()}", expanded=False):
                        for rec in recs:
                            st.write(f"• **{rec['title']}:** {rec['description']}")
                            if rec.get('action'):
                                if st.button(rec['action'], key=f"action_{category}_{rec['title']}"):
                                    st.success(f"Applied: {rec['title']}")
            
            # Learning path recommendations
            st.divider()
            st.write("**📚 Recommended Learning Path:**")
            
            learning_path = self._generate_learning_path(profile)
            
            for step, item in enumerate(learning_path, 1):
                st.write(f"**Step {step}: {item['title']}**")
                st.write(f"Focus: {item['focus']}")
                st.write(f"Expected benefit: {item['benefit']}")
                st.divider()
        
        # Profile editing
        with st.expander("✏️ Edit Profile", expanded=False):
            new_contexts = st.multiselect(
                "Preferred Contexts",
                ["development", "research", "documentation", "analysis", "coordination", "testing"],
                default=profile.preferred_contexts if profile else []
            )
            
            new_skill = st.selectbox(
                "Skill Level",
                ["beginner", "intermediate", "advanced"],
                index=["beginner", "intermediate", "advanced"].index(profile.skill_level) if profile else 1
            )
            
            new_goals = st.text_area(
                "Learning Goals (one per line)",
                value="\n".join(profile.learning_goals) if profile else ""
            )
            
            if st.button("Update Profile"):
                goals_list = [g.strip() for g in new_goals.split('\n') if g.strip()]
                self._update_user_profile(new_contexts, new_skill, goals_list)
                st.success("Profile updated!")
                st.rerun()
    
    def _render_learning_analytics(self):
        """Render learning analytics dashboard"""
        st.subheader("📊 Learning Analytics")
        st.write("**Track your prompt engineering progress and insights**")
        
        profile = self.user_profiles.get(self.current_user)
        
        if not profile or len(profile.effectiveness_history) < 3:
            st.info("Not enough data for analytics. Use the system more to see insights!")
            return
        
        # Performance analytics
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Effectiveness trend
            history_data = [
                {"Session": i+1, "Effectiveness": score}
                for i, score in enumerate(profile.effectiveness_history)
            ]
            
            history_df = pd.DataFrame(history_data)
            
            fig_trend = px.line(
                history_df,
                x="Session",
                y="Effectiveness",
                title="Your Effectiveness Trend",
                markers=True
            )
            fig_trend.update_layout(yaxis_tickformat=".1%")
            st.plotly_chart(fig_trend, use_container_width=True)
        
        with col2:
            # Module mastery radar
            module_mastery = self._calculate_module_mastery(profile)
            
            fig_radar = go.Figure()
            
            fig_radar.add_trace(go.Scatterpolar(
                r=list(module_mastery.values()),
                theta=list(module_mastery.keys()),
                fill='toself',
                name='Mastery Level'
            ))
            
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 1]
                    )
                ),
                title="Module Mastery Profile",
                height=400
            )
            
            st.plotly_chart(fig_radar, use_container_width=True)
        
        # Progress metrics
        st.divider()
        col3, col4, col5, col6 = st.columns(4)
        
        with col3:
            avg_effectiveness = np.mean(profile.effectiveness_history)
            st.metric("Average Effectiveness", f"{avg_effectiveness:.1%}")
        
        with col4:
            improvement = profile.effectiveness_history[-1] - profile.effectiveness_history[0]
            st.metric("Total Improvement", f"{improvement:+.1%}")
        
        with col5:
            consistency = 1 - np.std(profile.effectiveness_history)
            st.metric("Consistency", f"{consistency:.1%}")
        
        with col6:
            mastery_score = np.mean(list(self._calculate_module_mastery(profile).values()))
            st.metric("Mastery Score", f"{mastery_score:.1%}")
        
        # Insights and achievements
        st.divider()
        insights = self._generate_learning_insights(profile)
        
        col_a, col_b = st.columns([1, 1])
        
        with col_a:
            st.write("**🎯 Key Insights:**")
            for insight in insights["insights"]:
                st.write(f"• {insight}")
        
        with col_b:
            st.write("**🏆 Achievements:**")
            for achievement in insights["achievements"]:
                st.write(f"🏅 {achievement}")
    
    def _generate_smart_recommendations(self, goal: str, context: str, complexity: str, 
                                      current_modules: List[str], num_recs: int, 
                                      focus: str, experience: str) -> List[CompositionRecommendation]:
        """Generate smart recommendations based on user inputs"""
        recommendations = []
        
        # Base recommendations by context and complexity
        base_compositions = {
            ("development", "simple"): [["tdd-cycle-pattern", "quality-validation-pattern"]],
            ("development", "medium"): [["critical-thinking-pattern", "tdd-cycle-pattern", "quality-validation-pattern"]],
            ("development", "complex"): [["critical-thinking-pattern", "tdd-cycle-pattern", "quality-validation-pattern", "comprehensive-testing"]],
            ("research", "simple"): [["research-analysis-pattern", "documentation-pattern"]],
            ("research", "medium"): [["critical-thinking-pattern", "research-analysis-pattern", "documentation-pattern"]],
            ("research", "complex"): [["critical-thinking-pattern", "research-analysis-pattern", "documentation-pattern", "workflow-orchestration-engine"]],
            ("coordination", "medium"): [["intelligent-routing", "multi-agent", "session-management-pattern"]],
            ("coordination", "complex"): [["intelligent-routing", "multi-agent", "session-management-pattern", "workflow-orchestration-engine"]]
        }
        
        # Get base compositions
        key = (context, complexity)
        compositions = base_compositions.get(key, [["critical-thinking-pattern", "documentation-pattern"]])
        
        # Generate recommendations
        for i, modules in enumerate(compositions[:num_recs]):
            effectiveness = self._calculate_composition_effectiveness(modules)
            
            rec = CompositionRecommendation(
                composition_id=f"rec_{i}",
                name=f"Optimized {context.title()} Composition",
                modules=modules,
                expected_effectiveness=effectiveness,
                confidence=0.85 if experience == "advanced" else 0.75,
                use_cases=[f"{context} tasks", f"{complexity} complexity projects"],
                pros=[
                    "Proven module combination",
                    "High effectiveness score", 
                    "Good token efficiency"
                ],
                cons=["May be overkill for simple tasks"] if complexity == "simple" else [],
                optimization_tips=[
                    "Start with core modules and add as needed",
                    "Monitor token usage for efficiency",
                    "Customize for your specific domain"
                ]
            )
            
            recommendations.append(rec)
        
        return recommendations
    
    def _analyze_current_composition(self, modules: List[str]) -> Dict[str, float]:
        """Analyze effectiveness of current module composition"""
        if not modules:
            return {"effectiveness": 0.0, "token_efficiency": 0.0, "synergy_score": 0.0}
        
        # Calculate base effectiveness
        base_effectiveness = np.mean([
            self.module_database[module]["effectiveness_base"] 
            for module in modules
        ])
        
        # Calculate token efficiency
        token_efficiency = np.mean([
            self.module_database[module]["token_efficiency"]
            for module in modules
        ])
        
        # Calculate synergy score
        synergy_score = self._calculate_synergy_score(modules)
        
        return {
            "effectiveness": base_effectiveness * synergy_score,
            "token_efficiency": token_efficiency,
            "synergy_score": synergy_score
        }
    
    def _calculate_synergy_score(self, modules: List[str]) -> float:
        """Calculate synergy score for module combination"""
        if len(modules) <= 1:
            return 1.0
        
        synergy_count = 0
        total_pairs = 0
        
        for i, module_a in enumerate(modules):
            for j, module_b in enumerate(modules[i+1:], i+1):
                total_pairs += 1
                synergies_a = self.module_database[module_a]["synergies"]
                if module_b in synergies_a:
                    synergy_count += 1
        
        return 1.0 + (synergy_count / max(total_pairs, 1)) * 0.2  # Up to 20% bonus
    
    def _generate_optimization_recommendations(self, modules: List[str]) -> Dict[str, List[ModuleRecommendation]]:
        """Generate optimization recommendations for current modules"""
        recommendations = {
            "add_modules": [],
            "replace_modules": [],
            "remove_modules": []
        }
        
        current_categories = {self.module_database[m]["category"] for m in modules}
        
        # Suggest additions
        for module, data in self.module_database.items():
            if module not in modules:
                # Check if this module has synergy with current modules
                synergy_count = sum(1 for m in modules if m in data["synergies"])
                if synergy_count > 0:
                    rec = ModuleRecommendation(
                        module_name=module,
                        reason=f"High synergy with {synergy_count} current modules",
                        confidence=0.8,
                        expected_improvement=synergy_count * 0.05,
                        compatibility_score=0.9,
                        usage_context=", ".join(data["contexts"]),
                        evidence=[f"Synergy with existing modules"]
                    )
                    recommendations["add_modules"].append(rec)
        
        # Suggest replacements for low-performing modules
        for module in modules:
            effectiveness = self.module_database[module]["effectiveness_base"]
            if effectiveness < 0.8:  # Low performing
                # Find better alternatives in same category
                category = self.module_database[module]["category"]
                alternatives = [
                    (m, data) for m, data in self.module_database.items()
                    if data["category"] == category and m != module and data["effectiveness_base"] > effectiveness
                ]
                
                if alternatives:
                    best_alt = max(alternatives, key=lambda x: x[1]["effectiveness_base"])
                    rec = ModuleRecommendation(
                        module_name=best_alt[0],
                        reason=f"Higher effectiveness than {module}",
                        confidence=0.7,
                        expected_improvement=best_alt[1]["effectiveness_base"] - effectiveness,
                        compatibility_score=0.8,
                        usage_context=", ".join(best_alt[1]["contexts"]),
                        evidence=[f"Replace {module} for better performance"]
                    )
                    recommendations["replace_modules"].append(rec)
        
        return recommendations
    
    def _generate_alternative_compositions(self, current_modules: List[str]) -> List[Dict[str, Any]]:
        """Generate alternative compositions"""
        alternatives = []
        
        # Alternative 1: More focused approach
        if len(current_modules) > 3:
            core_modules = current_modules[:3]  # Take most important
            effectiveness = self._calculate_composition_effectiveness(core_modules)
            alternatives.append({
                "modules": core_modules,
                "improvement": effectiveness - self._calculate_composition_effectiveness(current_modules),
                "reason": "Simplified, more focused approach"
            })
        
        # Alternative 2: Enhanced with synergies
        enhanced_modules = current_modules.copy()
        for module in current_modules:
            synergies = self.module_database[module]["synergies"]
            for synergy in synergies:
                if synergy not in enhanced_modules:
                    enhanced_modules.append(synergy)
                    break  # Add just one synergy
        
        if enhanced_modules != current_modules:
            effectiveness = self._calculate_composition_effectiveness(enhanced_modules)
            alternatives.append({
                "modules": enhanced_modules,
                "improvement": effectiveness - self._calculate_composition_effectiveness(current_modules),
                "reason": "Enhanced with synergistic modules"
            })
        
        return alternatives[:3]  # Return top 3
    
    def _calculate_composition_effectiveness(self, modules: List[str]) -> float:
        """Calculate overall effectiveness of a module composition"""
        if not modules:
            return 0.0
        
        base_effectiveness = np.mean([
            self.module_database[module]["effectiveness_base"]
            for module in modules
        ])
        
        synergy_multiplier = self._calculate_synergy_score(modules)
        
        return min(0.99, base_effectiveness * synergy_multiplier)
    
    def _generate_personalized_recommendations(self, profile: UserProfile) -> Dict[str, List[Dict[str, str]]]:
        """Generate personalized recommendations based on user profile"""
        recommendations = {
            "skill_development": [],
            "efficiency_improvements": [],
            "new_explorations": []
        }
        
        # Skill development recommendations
        if profile.skill_level == "beginner":
            recommendations["skill_development"] = [
                {
                    "title": "Master Core Patterns",
                    "description": "Focus on TDD and documentation patterns first",
                    "action": "Start Learning Path"
                },
                {
                    "title": "Practice with Simple Tasks",
                    "description": "Build confidence with straightforward compositions",
                    "action": "View Examples"
                }
            ]
        elif profile.skill_level == "intermediate":
            recommendations["skill_development"] = [
                {
                    "title": "Explore Advanced Orchestration", 
                    "description": "Learn workflow orchestration and multi-agent patterns",
                    "action": "Try Advanced Modules"
                },
                {
                    "title": "Optimize Token Efficiency",
                    "description": "Focus on creating more efficient prompt compositions",
                    "action": "Run Efficiency Analysis"
                }
            ]
        
        # Based on recent performance
        recent_avg = np.mean(profile.effectiveness_history[-3:])
        if recent_avg < 0.8:
            recommendations["efficiency_improvements"] = [
                {
                    "title": "Review Module Synergies",
                    "description": "Your recent compositions may lack synergistic modules",
                    "action": "Check Synergies"
                }
            ]
        
        return recommendations
    
    def _generate_learning_path(self, profile: UserProfile) -> List[Dict[str, str]]:
        """Generate a personalized learning path"""
        if profile.skill_level == "beginner":
            return [
                {
                    "title": "Foundation Patterns",
                    "focus": "critical-thinking-pattern, documentation-pattern",
                    "benefit": "Build strong analytical and communication skills"
                },
                {
                    "title": "Development Essentials", 
                    "focus": "tdd-cycle-pattern, quality-validation-pattern",
                    "benefit": "Create reliable, high-quality code"
                },
                {
                    "title": "Advanced Composition",
                    "focus": "Module synergies and optimization",
                    "benefit": "Maximize effectiveness of prompt combinations"
                }
            ]
        else:
            return [
                {
                    "title": "Orchestration Mastery",
                    "focus": "workflow-orchestration-engine, multi-agent",
                    "benefit": "Handle complex, multi-step workflows"
                },
                {
                    "title": "Optimization Techniques",
                    "focus": "Token efficiency and performance tuning", 
                    "benefit": "Create more efficient and effective prompts"
                },
                {
                    "title": "Innovation & Experimentation",
                    "focus": "Novel module combinations and patterns",
                    "benefit": "Discover new effective approaches"
                }
            ]
    
    def _calculate_module_mastery(self, profile: UserProfile) -> Dict[str, float]:
        """Calculate mastery level for different modules"""
        mastery = {}
        
        for module in profile.frequently_used_modules[:6]:  # Top 6 modules
            # Simulate mastery based on usage and effectiveness
            usage_factor = 0.8  # High usage
            effectiveness_factor = np.mean(profile.effectiveness_history)
            mastery[module.replace('-', ' ').title()] = min(1.0, usage_factor * effectiveness_factor)
        
        return mastery
    
    def _generate_learning_insights(self, profile: UserProfile) -> Dict[str, List[str]]:
        """Generate learning insights and achievements"""
        insights = []
        achievements = []
        
        # Performance insights
        recent_trend = profile.effectiveness_history[-3:]
        if recent_trend[-1] > recent_trend[0]:
            insights.append("Your recent performance shows consistent improvement")
        
        avg_effectiveness = np.mean(profile.effectiveness_history)
        if avg_effectiveness > 0.85:
            achievements.append("High Performer - Maintaining >85% effectiveness")
        
        if len(profile.effectiveness_history) >= 10:
            achievements.append("Experienced User - 10+ prompt compositions")
        
        # Module usage insights
        if len(profile.frequently_used_modules) >= 5:
            insights.append("You're effectively using diverse module combinations")
        
        return {"insights": insights, "achievements": achievements}
    
    def _update_user_profile(self, contexts: List[str], skill: str, goals: List[str]):
        """Update user profile with new information"""
        if self.current_user in self.user_profiles:
            profile = self.user_profiles[self.current_user]
            profile.preferred_contexts = contexts
            profile.skill_level = skill
            profile.learning_goals = goals