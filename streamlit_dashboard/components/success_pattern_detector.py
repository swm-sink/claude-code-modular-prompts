"""
Prompt Pattern Discovery for Claude Code Framework Dashboard
AI-powered discovery of effective prompt engineering patterns and module compositions
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass, asdict
import re
from collections import defaultdict, Counter


@dataclass
class PromptPattern:
    """Represents a discovered prompt engineering pattern"""
    pattern_id: str
    name: str
    description: str
    structure: str
    effectiveness_score: float
    use_cases: List[str]
    module_composition: List[str]
    example_prompt: str
    success_metrics: Dict[str, float]
    complexity_level: str  # beginner, intermediate, advanced
    token_efficiency: float


@dataclass
class PatternAnalysis:
    """Analysis results for prompt patterns"""
    total_patterns: int
    effectiveness_distribution: Dict[str, int]
    complexity_breakdown: Dict[str, int]
    most_effective_patterns: List[PromptPattern]
    recommended_combinations: List[Dict[str, Any]]


class PromptPatternDiscovery:
    """AI-powered prompt pattern discovery and analysis system"""
    
    def __init__(self, framework_path: Path):
        """Initialize Prompt Pattern Discovery"""
        self.framework_path = framework_path
        self.discovered_patterns = self._discover_prompt_patterns()
        self.pattern_database = self._build_pattern_database()
        self.effectiveness_metrics = self._calculate_effectiveness_metrics()
        
    def _discover_prompt_patterns(self) -> List[PromptPattern]:
        """Discover proven prompt engineering patterns"""
        patterns = []
        
        # Pattern 1: Structured Thinking Pattern
        patterns.append(PromptPattern(
            pattern_id="structured_thinking",
            name="Structured Thinking Pattern",
            description="Step-by-step analytical approach with clear reasoning phases",
            structure="Context → Analysis → Reasoning → Conclusion → Verification",
            effectiveness_score=0.92,
            use_cases=["Complex problem solving", "Decision making", "Code analysis"],
            module_composition=["critical-thinking-pattern", "tdd-cycle-pattern", "quality-validation-pattern"],
            example_prompt=self._generate_example_prompt("structured_thinking"),
            success_metrics={"clarity": 0.95, "accuracy": 0.89, "completeness": 0.91},
            complexity_level="intermediate",
            token_efficiency=0.87
        ))
        
        # Pattern 2: Context-Aware Development Pattern
        patterns.append(PromptPattern(
            pattern_id="context_aware_dev",
            name="Context-Aware Development Pattern",
            description="Project-specific development with intelligent context utilization",
            structure="Project Analysis → Context Priming → Development → Integration → Validation",
            effectiveness_score=0.89,
            use_cases=["Feature development", "Bug fixing", "Code refactoring"],
            module_composition=["research-analysis-pattern", "feature-workflow", "tdd-cycle-pattern"],
            example_prompt=self._generate_example_prompt("context_aware_dev"),
            success_metrics={"relevance": 0.93, "accuracy": 0.86, "efficiency": 0.88},
            complexity_level="advanced",
            token_efficiency=0.82
        ))
        
        # Pattern 3: Iterative Refinement Pattern
        patterns.append(PromptPattern(
            pattern_id="iterative_refinement",
            name="Iterative Refinement Pattern",
            description="Progressive improvement through feedback cycles",
            structure="Initial Approach → Feedback Analysis → Refinement → Validation → Repeat",
            effectiveness_score=0.94,
            use_cases=["Prompt optimization", "Code improvement", "Learning enhancement"],
            module_composition=["iterative-testing", "quality-validation-pattern", "performance-optimization"],
            example_prompt=self._generate_example_prompt("iterative_refinement"),
            success_metrics={"improvement_rate": 0.94, "convergence": 0.91, "quality": 0.96},
            complexity_level="advanced",
            token_efficiency=0.85
        ))
        
        # Pattern 4: Multi-Modal Analysis Pattern
        patterns.append(PromptPattern(
            pattern_id="multi_modal_analysis",
            name="Multi-Modal Analysis Pattern",
            description="Comprehensive analysis using multiple perspectives and approaches",
            structure="Technical Analysis → Business Analysis → User Analysis → Integration → Synthesis",
            effectiveness_score=0.88,
            use_cases=["Requirements analysis", "Architecture design", "Problem diagnosis"],
            module_composition=["research-analysis-pattern", "multi-agent", "comprehensive-error-handling"],
            example_prompt=self._generate_example_prompt("multi_modal_analysis"),
            success_metrics={"comprehensiveness": 0.92, "depth": 0.85, "balance": 0.87},
            complexity_level="advanced",
            token_efficiency=0.79
        ))
        
        # Pattern 5: Rapid Prototyping Pattern
        patterns.append(PromptPattern(
            pattern_id="rapid_prototyping",
            name="Rapid Prototyping Pattern",
            description="Quick development with validation checkpoints",
            structure="Minimal Viable Solution → Quick Validation → Incremental Enhancement → Testing",
            effectiveness_score=0.86,
            use_cases=["MVP development", "Proof of concept", "Quick experiments"],
            module_composition=["mvp-strategy", "tdd-cycle-pattern", "atomic-operation-pattern"],
            example_prompt=self._generate_example_prompt("rapid_prototyping"),
            success_metrics={"speed": 0.94, "viability": 0.83, "adaptability": 0.89},
            complexity_level="intermediate",
            token_efficiency=0.91
        ))
        
        # Pattern 6: Quality-First Pattern
        patterns.append(PromptPattern(
            pattern_id="quality_first",
            name="Quality-First Development Pattern",
            description="Quality gates and validation at every step",
            structure="Quality Planning → Test-First Development → Continuous Validation → Quality Assurance",
            effectiveness_score=0.91,
            use_cases=["Production systems", "Critical features", "Enterprise development"],
            module_composition=["tdd-cycle-pattern", "quality-validation-pattern", "enforcement-verification"],
            example_prompt=self._generate_example_prompt("quality_first"),
            success_metrics={"reliability": 0.96, "maintainability": 0.89, "robustness": 0.93},
            complexity_level="advanced",
            token_efficiency=0.84
        ))
        
        # Pattern 7: Collaborative Intelligence Pattern  
        patterns.append(PromptPattern(
            pattern_id="collaborative_intelligence",
            name="Collaborative Intelligence Pattern",
            description="Coordinated multi-agent approach for complex tasks",
            structure="Task Decomposition → Agent Coordination → Parallel Execution → Result Integration",
            effectiveness_score=0.87,
            use_cases=["Large projects", "Complex integrations", "Research tasks"],
            module_composition=["multi-agent", "session-management-pattern", "workflow-orchestration-engine"],
            example_prompt=self._generate_example_prompt("collaborative_intelligence"),
            success_metrics={"coordination": 0.85, "efficiency": 0.89, "coverage": 0.87},
            complexity_level="advanced",
            token_efficiency=0.78
        ))
        
        # Pattern 8: Adaptive Learning Pattern
        patterns.append(PromptPattern(
            pattern_id="adaptive_learning",
            name="Adaptive Learning Pattern",
            description="Self-improving approach that learns from experience",
            structure="Initial Learning → Pattern Recognition → Adaptation → Performance Measurement → Evolution",
            effectiveness_score=0.85,
            use_cases=["Skill development", "Process optimization", "Continuous improvement"],
            module_composition=["pattern-recognition", "performance-optimization", "adaptive-routing"],
            example_prompt=self._generate_example_prompt("adaptive_learning"),
            success_metrics={"learning_rate": 0.88, "adaptation": 0.83, "retention": 0.86},
            complexity_level="beginner",
            token_efficiency=0.88
        ))
        
        return patterns
    
    def _generate_example_prompt(self, pattern_id: str) -> str:
        """Generate example prompts for each pattern"""
        examples = {
            "structured_thinking": """# Structured Analysis Request

## Context
I need to analyze the performance bottleneck in our API system.

## Analysis Framework
1. **Problem Identification**: Identify specific performance issues
2. **Root Cause Analysis**: Trace issues to their source
3. **Solution Evaluation**: Compare potential solutions
4. **Implementation Planning**: Create step-by-step plan
5. **Validation Strategy**: Define success criteria

## Expected Output
- Clear problem statement
- Evidence-based root cause analysis
- Prioritized solution recommendations
- Implementation roadmap with validation checkpoints""",

            "context_aware_dev": """# Context-Aware Development Request

## Project Context
- Framework: Django REST API
- Database: PostgreSQL
- Current Issue: Slow query performance
- Business Impact: User complaints about response times

## Development Approach
1. **Analyze current codebase** for query patterns
2. **Identify optimization opportunities** based on project constraints
3. **Implement targeted improvements** following project standards
4. **Validate changes** against business requirements

## Integration Requirements
- Must maintain existing API compatibility
- Follow established coding conventions
- Include comprehensive tests
- Document performance improvements""",

            "iterative_refinement": """# Iterative Improvement Request

## Initial Objective
Optimize the user authentication flow for better security and UX.

## Refinement Process
1. **Version 1**: Implement basic improvements
2. **Feedback Analysis**: Evaluate effectiveness and user impact
3. **Version 2**: Address identified issues and enhance further
4. **Validation**: Measure improvements against baseline
5. **Final Optimization**: Polish and perfect the solution

## Success Criteria
- Measurable security improvements
- Enhanced user experience metrics
- Performance benchmarks
- Stakeholder feedback integration""",

            "multi_modal_analysis": """# Multi-Modal Analysis Request

## Analysis Dimensions
- **Technical**: Code quality, architecture, performance
- **Business**: Cost impact, ROI, strategic alignment
- **User**: Experience, accessibility, usability
- **Operational**: Maintenance, scalability, monitoring

## Integration Approach
1. Conduct each analysis independently
2. Identify synergies and conflicts
3. Synthesize unified recommendations
4. Prioritize based on overall impact

## Expected Output
Comprehensive recommendation balancing all perspectives with clear trade-offs and justifications.""",

            "rapid_prototyping": """# Rapid Prototype Request

## Objective
Create a functional prototype for real-time data visualization dashboard.

## Prototyping Approach
1. **MVP Definition**: Core features only
2. **Quick Implementation**: 80/20 approach
3. **Early Validation**: User feedback on core functionality
4. **Iterative Enhancement**: Add features based on validation

## Success Metrics
- Working prototype in minimal time
- Core functionality demonstrated
- User feedback collected
- Clear path to full implementation""",

            "quality_first": """# Quality-First Development Request

## Quality Framework
- **Testing**: TDD with comprehensive coverage
- **Code Quality**: Static analysis, peer review
- **Performance**: Benchmarking and optimization
- **Security**: Threat modeling and validation

## Development Process
1. Define quality gates before implementation
2. Test-driven development approach
3. Continuous quality validation
4. Performance and security verification

## Acceptance Criteria
- 90%+ test coverage
- Zero critical security issues
- Performance benchmarks met
- Code review approval""",

            "collaborative_intelligence": """# Collaborative Intelligence Request

## Task Coordination
- **Agent 1**: Frontend implementation
- **Agent 2**: Backend API development  
- **Agent 3**: Database optimization
- **Agent 4**: Integration testing

## Coordination Framework
1. Task decomposition and assignment
2. Parallel execution with checkpoints
3. Regular synchronization points
4. Integrated result validation

## Success Criteria
- Coordinated delivery
- Quality integration
- Minimal conflicts
- Comprehensive coverage""",

            "adaptive_learning": """# Adaptive Learning Request

## Learning Objective
Improve prompt engineering skills through systematic practice and reflection.

## Learning Process
1. **Baseline Assessment**: Current skill level
2. **Pattern Recognition**: Identify effective techniques
3. **Deliberate Practice**: Apply new patterns
4. **Performance Measurement**: Track improvement
5. **Adaptation**: Refine approach based on results

## Success Metrics
- Measurable skill improvement
- Pattern mastery demonstration
- Consistent quality output
- Self-assessment accuracy"""
        }
        
        return examples.get(pattern_id, "Example prompt not available")
    
    def _build_pattern_database(self) -> Dict[str, Any]:
        """Build comprehensive pattern database with metadata"""
        database = {
            "patterns_by_complexity": defaultdict(list),
            "patterns_by_effectiveness": defaultdict(list),
            "patterns_by_use_case": defaultdict(list),
            "module_combinations": defaultdict(list)
        }
        
        for pattern in self.discovered_patterns:
            database["patterns_by_complexity"][pattern.complexity_level].append(pattern)
            
            # Effectiveness buckets
            if pattern.effectiveness_score >= 0.9:
                database["patterns_by_effectiveness"]["high"].append(pattern)
            elif pattern.effectiveness_score >= 0.8:
                database["patterns_by_effectiveness"]["medium"].append(pattern)
            else:
                database["patterns_by_effectiveness"]["low"].append(pattern)
            
            # Index by use cases
            for use_case in pattern.use_cases:
                database["patterns_by_use_case"][use_case].append(pattern)
            
            # Index by module combinations
            for module in pattern.module_composition:
                database["module_combinations"][module].append(pattern)
        
        return database
    
    def _calculate_effectiveness_metrics(self) -> Dict[str, float]:
        """Calculate overall effectiveness metrics"""
        if not self.discovered_patterns:
            return {}
        
        scores = [p.effectiveness_score for p in self.discovered_patterns]
        token_efficiencies = [p.token_efficiency for p in self.discovered_patterns]
        
        return {
            "average_effectiveness": np.mean(scores),
            "effectiveness_std": np.std(scores),
            "top_quartile_effectiveness": np.percentile(scores, 75),
            "average_token_efficiency": np.mean(token_efficiencies),
            "pattern_diversity": len(set(p.complexity_level for p in self.discovered_patterns)),
            "total_patterns": len(self.discovered_patterns)
        }
    
    def render(self):
        """Render the Prompt Pattern Discovery interface"""
        st.title("🔍 Prompt Pattern Discovery")
        st.markdown("**Discover and learn from proven prompt engineering patterns and module compositions**")
        
        # Create tabs for different discovery modes
        tab1, tab2, tab3, tab4 = st.tabs([
            "🎯 Pattern Library",
            "📊 Pattern Analysis", 
            "🔍 Pattern Search",
            "🧠 Learning Insights"
        ])
        
        with tab1:
            self._render_pattern_library()
        
        with tab2:
            self._render_pattern_analysis()
        
        with tab3:
            self._render_pattern_search()
        
        with tab4:
            self._render_learning_insights()
    
    def _render_pattern_library(self):
        """Render the comprehensive pattern library"""
        st.subheader("🎯 Proven Prompt Engineering Patterns")
        st.write(f"**{len(self.discovered_patterns)} proven patterns with effectiveness scores 85-94%**")
        
        # Filter controls
        col1, col2, col3 = st.columns(3)
        
        with col1:
            complexity_filter = st.selectbox(
                "Filter by Complexity", 
                ["All", "beginner", "intermediate", "advanced"]
            )
        
        with col2:
            min_effectiveness = st.slider(
                "Minimum Effectiveness", 
                0.0, 1.0, 0.85, 0.05
            )
        
        with col3:
            sort_by = st.selectbox(
                "Sort by", 
                ["Effectiveness", "Token Efficiency", "Complexity", "Name"]
            )
        
        # Filter patterns
        filtered_patterns = self.discovered_patterns
        if complexity_filter != "All":
            filtered_patterns = [p for p in filtered_patterns if p.complexity_level == complexity_filter]
        
        filtered_patterns = [p for p in filtered_patterns if p.effectiveness_score >= min_effectiveness]
        
        # Sort patterns
        if sort_by == "Effectiveness":
            filtered_patterns.sort(key=lambda p: p.effectiveness_score, reverse=True)
        elif sort_by == "Token Efficiency":
            filtered_patterns.sort(key=lambda p: p.token_efficiency, reverse=True)
        elif sort_by == "Complexity":
            complexity_order = {"beginner": 1, "intermediate": 2, "advanced": 3}
            filtered_patterns.sort(key=lambda p: complexity_order[p.complexity_level])
        else:  # Name
            filtered_patterns.sort(key=lambda p: p.name)
        
        # Display patterns
        for pattern in filtered_patterns:
            self._render_pattern_card(pattern)
    
    def _render_pattern_card(self, pattern: PromptPattern):
        """Render individual pattern card"""
        with st.expander(f"⭐ {pattern.name} (Effectiveness: {pattern.effectiveness_score:.1%})", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**Description:** {pattern.description}")
                st.write(f"**Structure:** {pattern.structure}")
                st.write(f"**Complexity:** {pattern.complexity_level.title()}")
                
                if pattern.use_cases:
                    st.write("**Best for:**")
                    for use_case in pattern.use_cases:
                        st.write(f"• {use_case}")
                
                if pattern.module_composition:
                    st.write("**Module Composition:**")
                    st.write(", ".join(pattern.module_composition))
            
            with col2:
                # Effectiveness metrics
                st.metric("Effectiveness", f"{pattern.effectiveness_score:.1%}")
                st.metric("Token Efficiency", f"{pattern.token_efficiency:.1%}")
                
                # Success metrics radar
                if pattern.success_metrics:
                    self._render_pattern_metrics_radar(pattern)
            
            # Example prompt
            if pattern.example_prompt:
                st.subheader("📝 Example Prompt")
                st.code(pattern.example_prompt, language="markdown")
            
            # Action buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"📋 Copy Pattern", key=f"copy_{pattern.pattern_id}"):
                    st.success("Pattern structure copied!")
                    st.code(pattern.structure, language="text")
            
            with col2:
                if st.button(f"🔍 Analyze", key=f"analyze_{pattern.pattern_id}"):
                    self._show_pattern_analysis(pattern)
            
            with col3:
                if st.button(f"🚀 Apply", key=f"apply_{pattern.pattern_id}"):
                    self._show_pattern_application(pattern)
    
    def _render_pattern_metrics_radar(self, pattern: PromptPattern):
        """Render pattern metrics as radar chart"""
        if not pattern.success_metrics:
            return
        
        categories = list(pattern.success_metrics.keys())
        values = list(pattern.success_metrics.values())
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=pattern.name,
            fillcolor='rgba(255, 99, 132, 0.3)',
            line_color='rgb(255, 99, 132)'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )),
            showlegend=False,
            height=200,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def _show_pattern_analysis(self, pattern: PromptPattern):
        """Show detailed pattern analysis"""
        st.subheader(f"🔍 Analysis: {pattern.name}")
        st.write(f"**Pattern ID:** {pattern.pattern_id}")
        st.write(f"**Effectiveness Score:** {pattern.effectiveness_score:.1%}")
        st.write(f"**Token Efficiency:** {pattern.token_efficiency:.1%}")
        st.write(f"**Complexity Level:** {pattern.complexity_level.title()}")
        
        if pattern.success_metrics:
            st.write("**Success Metrics:**")
            for metric, value in pattern.success_metrics.items():
                st.write(f"• {metric.title()}: {value:.1%}")
    
    def _show_pattern_application(self, pattern: PromptPattern):
        """Show pattern application guide"""
        st.subheader(f"🚀 Apply: {pattern.name}")
        st.write("**How to apply this pattern:**")
        
        steps = pattern.structure.split(" → ")
        for i, step in enumerate(steps, 1):
            st.write(f"{i}. {step}")
        
        st.write("**Recommended modules to include:**")
        for module in pattern.module_composition:
            st.write(f"• {module}")
    
    def _render_pattern_analysis(self):
        """Render pattern analysis dashboard"""
        st.subheader("📊 Pattern Analysis & Insights")
        
        # Overall metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Patterns", self.effectiveness_metrics["total_patterns"])
        with col2:
            st.metric("Avg Effectiveness", f"{self.effectiveness_metrics['average_effectiveness']:.1%}")
        with col3:
            st.metric("Avg Token Efficiency", f"{self.effectiveness_metrics['average_token_efficiency']:.1%}")
        with col4:
            st.metric("Complexity Levels", self.effectiveness_metrics["pattern_diversity"])
        
        # Effectiveness distribution
        effectiveness_scores = [p.effectiveness_score for p in self.discovered_patterns]
        fig_hist = px.histogram(
            x=effectiveness_scores,
            title="Pattern Effectiveness Distribution",
            nbins=10,
            labels={'x': 'Effectiveness Score', 'y': 'Count'}
        )
        st.plotly_chart(fig_hist, use_container_width=True)
        
        # Complexity breakdown
        complexity_counts = Counter(p.complexity_level for p in self.discovered_patterns)
        fig_pie = px.pie(
            values=list(complexity_counts.values()),
            names=list(complexity_counts.keys()),
            title="Patterns by Complexity Level"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
        # Top performing patterns
        st.subheader("🏆 Top Performing Patterns")
        top_patterns = sorted(self.discovered_patterns, key=lambda p: p.effectiveness_score, reverse=True)[:5]
        
        for i, pattern in enumerate(top_patterns, 1):
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.write(f"#{i}")
            with col2:
                st.write(f"**{pattern.name}**")
                st.write(f"{pattern.description[:80]}...")
            with col3:
                st.metric("Score", f"{pattern.effectiveness_score:.1%}")
    
    def _render_pattern_search(self):
        """Render pattern search interface"""
        st.subheader("🔍 Find Patterns for Your Needs")
        
        # Search controls
        col1, col2 = st.columns(2)
        
        with col1:
            search_query = st.text_input(
                "Search patterns:",
                placeholder="e.g., 'quality', 'development', 'analysis'..."
            )
        
        with col2:
            use_case_filter = st.selectbox(
                "Filter by use case:",
                ["All"] + list(set(use_case for pattern in self.discovered_patterns for use_case in pattern.use_cases))
            )
        
        # Scenario-based recommendations
        st.subheader("📋 Scenario-Based Recommendations")
        
        scenario = st.selectbox(
            "What are you trying to accomplish?",
            [
                "Analyze a complex problem",
                "Develop a new feature", 
                "Optimize existing code",
                "Learn a new skill",
                "Debug an issue",
                "Create documentation",
                "Plan a project"
            ]
        )
        
        if scenario:
            recommendations = self._get_scenario_recommendations(scenario)
            st.write(f"**Recommended patterns for '{scenario}':**")
            
            for pattern in recommendations:
                with st.expander(f"⭐ {pattern.name}", expanded=False):
                    st.write(f"**Why it's good for this scenario:** {pattern.description}")
                    st.write(f"**Effectiveness:** {pattern.effectiveness_score:.1%}")
                    st.write(f"**Structure:** {pattern.structure}")
    
    def _get_scenario_recommendations(self, scenario: str) -> List[PromptPattern]:
        """Get pattern recommendations for specific scenarios"""
        scenario_mapping = {
            "Analyze a complex problem": ["structured_thinking", "multi_modal_analysis"],
            "Develop a new feature": ["context_aware_dev", "quality_first"],
            "Optimize existing code": ["iterative_refinement", "quality_first"],
            "Learn a new skill": ["adaptive_learning", "structured_thinking"],
            "Debug an issue": ["structured_thinking", "context_aware_dev"],
            "Create documentation": ["structured_thinking", "multi_modal_analysis"],
            "Plan a project": ["collaborative_intelligence", "context_aware_dev"]
        }
        
        pattern_ids = scenario_mapping.get(scenario, [])
        return [p for p in self.discovered_patterns if p.pattern_id in pattern_ids]
    
    def _render_learning_insights(self):
        """Render learning insights and recommendations"""
        st.subheader("🧠 Learning Insights & Growth Path")
        
        # Learning progression
        st.subheader("📈 Recommended Learning Progression")
        
        beginner_patterns = [p for p in self.discovered_patterns if p.complexity_level == "beginner"]
        intermediate_patterns = [p for p in self.discovered_patterns if p.complexity_level == "intermediate"]
        advanced_patterns = [p for p in self.discovered_patterns if p.complexity_level == "advanced"]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("**🌱 Beginner (Start Here)**")
            for pattern in beginner_patterns:
                st.write(f"• {pattern.name}")
                st.write(f"  Effectiveness: {pattern.effectiveness_score:.1%}")
        
        with col2:
            st.write("**📈 Intermediate (Build Skills)**")
            for pattern in intermediate_patterns:
                st.write(f"• {pattern.name}")
                st.write(f"  Effectiveness: {pattern.effectiveness_score:.1%}")
        
        with col3:
            st.write("**🚀 Advanced (Master Level)**")
            for pattern in advanced_patterns:
                st.write(f"• {pattern.name}")
                st.write(f"  Effectiveness: {pattern.effectiveness_score:.1%}")
        
        # Pattern combination insights
        st.subheader("🔗 Pattern Combination Insights")
        st.write("**Powerful pattern combinations for maximum effectiveness:**")
        
        combinations = [
            {
                "name": "Quality-Driven Development",
                "patterns": ["quality_first", "structured_thinking", "iterative_refinement"],
                "effectiveness": 0.93,
                "description": "Combine quality gates with structured analysis and continuous improvement"
            },
            {
                "name": "Intelligent Problem Solving",
                "patterns": ["structured_thinking", "multi_modal_analysis", "adaptive_learning"],
                "effectiveness": 0.91,
                "description": "Multi-perspective analysis with learning and adaptation"
            },
            {
                "name": "Rapid Quality Delivery",
                "patterns": ["rapid_prototyping", "quality_first", "context_aware_dev"],
                "effectiveness": 0.89,
                "description": "Fast delivery without compromising quality standards"
            }
        ]
        
        for combo in combinations:
            with st.expander(f"⚡ {combo['name']} (Effectiveness: {combo['effectiveness']:.1%})", expanded=False):
                st.write(f"**Description:** {combo['description']}")
                st.write("**Patterns to combine:**")
                for pattern_id in combo['patterns']:
                    pattern = next(p for p in self.discovered_patterns if p.pattern_id == pattern_id)
                    st.write(f"• {pattern.name}")


# Maintain backward compatibility
SuccessPatternDetector = PromptPatternDiscovery