"""
AI-Powered Routing Recommendation Engine for Claude Code Modular Prompts Framework
Intelligently recommends the best command based on user input and project context
"""

import streamlit as st
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field, asdict
from datetime import datetime
import math
from collections import defaultdict, Counter
import pickle


@dataclass
class RoutingRecommendation:
    """Represents a routing recommendation with confidence and reasoning"""
    
    command: str
    confidence: float
    reasoning: str
    context_factors: List[str] = field(default_factory=list)
    alternative_commands: List[str] = field(default_factory=list)
    parameters: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate recommendation data"""
        if not self.command.startswith("/"):
            raise ValueError("Command must start with '/'")
        
        if not 0 <= self.confidence <= 1:
            raise ValueError("Confidence must be between 0 and 1")
        
        if not self.reasoning or self.reasoning.strip() == "":
            raise ValueError("Reasoning cannot be empty")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RoutingRecommendation':
        """Create from dictionary"""
        return cls(**data)


@dataclass
class UserContext:
    """Represents user context for routing decisions"""
    
    user_input: str
    project_type: str = "unknown"
    file_count: int = 0
    test_coverage: int = 0
    recent_commands: List[str] = field(default_factory=list)
    project_complexity: str = "unknown"
    framework_usage: Dict[str, bool] = field(default_factory=dict)
    time_context: str = "normal"
    
    def is_small_project(self) -> bool:
        """Check if this is a small project"""
        return self.file_count <= 10 or self.project_complexity == "small"
    
    def has_high_test_coverage(self) -> bool:
        """Check if project has high test coverage"""
        return self.test_coverage >= 80
    
    def get_dominant_recent_command(self) -> Optional[str]:
        """Get the most frequently used recent command"""
        if not self.recent_commands:
            return None
        
        counter = Counter(self.recent_commands)
        return counter.most_common(1)[0][0]
    
    def indicates_new_feature(self) -> bool:
        """Check if user input indicates a new feature"""
        feature_keywords = [
            "create", "add", "new", "implement", "build", "develop",
            "feature", "functionality", "system", "module", "component"
        ]
        
        input_lower = self.user_input.lower()
        return any(keyword in input_lower for keyword in feature_keywords)
    
    def indicates_bug_fix(self) -> bool:
        """Check if user input indicates a bug fix"""
        bug_keywords = [
            "fix", "bug", "error", "issue", "problem", "broken",
            "repair", "correct", "resolve", "debug"
        ]
        
        input_lower = self.user_input.lower()
        return any(keyword in input_lower for keyword in bug_keywords)
    
    def indicates_research(self) -> bool:
        """Check if user input indicates research/analysis"""
        research_keywords = [
            "understand", "analyze", "investigate", "explore", "research",
            "find", "look", "examine", "study", "how", "why", "what"
        ]
        
        input_lower = self.user_input.lower()
        return any(keyword in input_lower for keyword in research_keywords)
    
    @classmethod
    def from_project_analysis(cls, 
                            user_input: str, 
                            project_data: Dict[str, Any], 
                            recent_commands: List[str] = None) -> 'UserContext':
        """Create context from project analysis"""
        return cls(
            user_input=user_input,
            project_type=project_data.get("project_type", "unknown"),
            file_count=project_data.get("file_count", 0),
            test_coverage=project_data.get("test_coverage", 0),
            recent_commands=recent_commands or [],
            project_complexity=project_data.get("complexity", "unknown"),
            framework_usage=project_data.get("frameworks", {}),
            time_context=project_data.get("time_context", "normal")
        )


class ProjectAnalyzer:
    """Analyzes project structure and characteristics"""
    
    def __init__(self, project_path: Path):
        """Initialize project analyzer"""
        self.project_path = project_path
        self._file_patterns = {
            "python": [".py"],
            "javascript": [".js", ".jsx"],
            "typescript": [".ts", ".tsx"],
            "java": [".java"],
            "go": [".go"],
            "rust": [".rs"],
            "c": [".c", ".h"],
            "cpp": [".cpp", ".hpp", ".cc"]
        }
        
        self._framework_indicators = {
            "react": ["package.json", "src/App.jsx", "src/App.tsx"],
            "vue": ["vue.config.js", "src/App.vue"],
            "angular": ["angular.json", "src/app/app.component.ts"],
            "django": ["manage.py", "settings.py", "urls.py"],
            "flask": ["app.py", "main.py", "wsgi.py"],
            "fastapi": ["main.py", "app.py"],
            "spring": ["pom.xml", "build.gradle", "Application.java"],
            "express": ["package.json", "server.js", "app.js"]
        }
    
    def analyze_project_structure(self) -> Dict[str, Any]:
        """Analyze complete project structure"""
        return {
            "file_count": self.count_source_files(),
            "test_coverage_estimate": self.estimate_test_coverage(),
            "project_type": self.detect_project_type(),
            "complexity": self.analyze_complexity(),
            "frameworks": self.identify_frameworks(),
            "languages": self.identify_languages(),
            "has_tests": self.has_test_files(),
            "has_docs": self.has_documentation()
        }
    
    def count_source_files(self) -> int:
        """Count source code files"""
        if not self.project_path.exists():
            return 0
        
        count = 0
        for pattern_list in self._file_patterns.values():
            for pattern in pattern_list:
                count += len(list(self.project_path.rglob(f"*{pattern}")))
        
        return count
    
    def detect_project_type(self) -> str:
        """Detect the type of project"""
        if not self.project_path.exists():
            return "unknown"
        
        # Check for specific file patterns
        if (self.project_path / "package.json").exists():
            package_json = self.project_path / "package.json"
            try:
                with open(package_json) as f:
                    package_data = json.load(f)
                    if "react" in package_data.get("dependencies", {}):
                        return "web_application"
                    elif "express" in package_data.get("dependencies", {}):
                        return "api"
            except:
                pass
        
        if (self.project_path / "manage.py").exists():
            return "web_application"
        
        if (self.project_path / "main.py").exists():
            return "script"
        
        if (self.project_path / "setup.py").exists():
            return "library"
        
        # Check for API patterns
        api_files = list(self.project_path.rglob("*api*"))
        if api_files:
            return "api"
        
        # Check for web patterns
        web_files = list(self.project_path.rglob("*web*")) + list(self.project_path.rglob("*html*"))
        if web_files:
            return "web_application"
        
        return "unknown"
    
    def analyze_complexity(self) -> str:
        """Analyze project complexity"""
        file_count = self.count_source_files()
        
        if file_count <= 10:
            return "small"
        elif file_count <= 50:
            return "medium"
        elif file_count <= 200:
            return "large"
        else:
            return "enterprise"
    
    def estimate_test_coverage(self) -> int:
        """Estimate test coverage based on test files"""
        if not self.project_path.exists():
            return 0
        
        source_count = self.count_source_files()
        if source_count == 0:
            return 0
        
        # Count test files
        test_patterns = ["test_*.py", "*_test.py", "*.test.js", "*.spec.js", "*.test.ts", "*.spec.ts"]
        test_count = 0
        
        for pattern in test_patterns:
            test_count += len(list(self.project_path.rglob(pattern)))
        
        # Rough estimate based on test file ratio
        if test_count == 0:
            return 0
        
        ratio = test_count / source_count
        
        if ratio >= 0.8:
            return 90
        elif ratio >= 0.5:
            return 75
        elif ratio >= 0.3:
            return 60
        elif ratio >= 0.1:
            return 40
        else:
            return 20
    
    def identify_frameworks(self) -> Dict[str, bool]:
        """Identify frameworks used in the project"""
        frameworks = {}
        
        for framework, indicators in self._framework_indicators.items():
            found = False
            for indicator in indicators:
                if (self.project_path / indicator).exists():
                    found = True
                    break
            frameworks[framework] = found
        
        return frameworks
    
    def identify_languages(self) -> Dict[str, int]:
        """Identify programming languages and their file counts"""
        languages = {}
        
        for language, extensions in self._file_patterns.items():
            count = 0
            for ext in extensions:
                count += len(list(self.project_path.rglob(f"*{ext}")))
            if count > 0:
                languages[language] = count
        
        return languages
    
    def has_test_files(self) -> bool:
        """Check if project has test files"""
        test_patterns = ["test_*.py", "*_test.py", "*.test.js", "*.spec.js", "tests/"]
        
        for pattern in test_patterns:
            if list(self.project_path.rglob(pattern)):
                return True
        
        return False
    
    def has_documentation(self) -> bool:
        """Check if project has documentation"""
        doc_patterns = ["README*", "docs/", "*.md", "*.rst"]
        
        for pattern in doc_patterns:
            if list(self.project_path.rglob(pattern)):
                return True
        
        return False


@dataclass
class RoutingRule:
    """Represents a routing rule for decision making"""
    
    name: str
    conditions: Dict[str, Any]
    recommendation: str
    confidence_base: float
    reasoning_template: str
    priority: int = 5
    
    def evaluate(self, context: UserContext) -> Tuple[bool, float]:
        """Evaluate rule against context"""
        matches = True
        confidence_factors = []
        
        # Check file count conditions
        if "file_count" in self.conditions:
            file_conditions = self.conditions["file_count"]
            if "max" in file_conditions and context.file_count > file_conditions["max"]:
                matches = False
            if "min" in file_conditions and context.file_count < file_conditions["min"]:
                matches = False
            
            if matches:
                confidence_factors.append(0.8)
        
        # Check keyword conditions
        if "user_input_keywords" in self.conditions:
            keywords = self.conditions["user_input_keywords"]
            input_lower = context.user_input.lower()
            keyword_matches = sum(1 for keyword in keywords if keyword in input_lower)
            
            if keyword_matches == 0:
                matches = False
            else:
                confidence_factors.append(min(1.0, keyword_matches / len(keywords)))
        
        # Check project complexity
        if "project_complexity" in self.conditions:
            allowed_complexity = self.conditions["project_complexity"]
            if context.project_complexity not in allowed_complexity:
                matches = False
            else:
                confidence_factors.append(0.7)
        
        # Check test coverage
        if "test_coverage" in self.conditions:
            coverage_conditions = self.conditions["test_coverage"]
            if "min" in coverage_conditions and context.test_coverage < coverage_conditions["min"]:
                matches = False
            else:
                confidence_factors.append(0.6)
        
        # Calculate confidence
        if matches and confidence_factors:
            avg_confidence = sum(confidence_factors) / len(confidence_factors)
            final_confidence = self.confidence_base * avg_confidence
        elif matches:
            final_confidence = self.confidence_base
        else:
            final_confidence = 0.0
        
        return matches, final_confidence


class RoutingDecisionTree:
    """Decision tree for routing recommendations"""
    
    def __init__(self):
        """Initialize decision tree with default rules"""
        self.rules: List[RoutingRule] = []
        self._initialize_default_rules()
    
    def _initialize_default_rules(self):
        """Initialize with default routing rules"""
        # Task rule - small focused work
        self.add_rule(RoutingRule(
            name="small_task_rule",
            conditions={
                "file_count": {"max": 10},
                "user_input_keywords": ["fix", "bug", "update", "change", "modify"],
                "project_complexity": ["small", "medium"]
            },
            recommendation="/task",
            confidence_base=0.85,
            reasoning_template="Small focused task detected - single file changes in manageable project",
            priority=8
        ))
        
        # Feature rule - new functionality
        self.add_rule(RoutingRule(
            name="new_feature_rule",
            conditions={
                "user_input_keywords": ["create", "add", "new", "implement", "build", "feature"],
                "project_complexity": ["medium", "large", "enterprise"]
            },
            recommendation="/feature",
            confidence_base=0.80,
            reasoning_template="New feature development detected - requires comprehensive planning",
            priority=7
        ))
        
        # Query rule - research and analysis
        self.add_rule(RoutingRule(
            name="research_rule",
            conditions={
                "user_input_keywords": ["understand", "analyze", "investigate", "explore", "how", "why", "what"],
            },
            recommendation="/query",
            confidence_base=0.75,
            reasoning_template="Research and analysis task detected - understanding required before changes",
            priority=6
        ))
        
        # Swarm rule - complex multi-component work
        self.add_rule(RoutingRule(
            name="complex_swarm_rule",
            conditions={
                "file_count": {"min": 50},
                "project_complexity": ["large", "enterprise"],
                "user_input_keywords": ["system", "architecture", "refactor", "migrate"]
            },
            recommendation="/swarm",
            confidence_base=0.70,
            reasoning_template="Complex multi-component work detected - requires coordinated development",
            priority=5
        ))
        
        # Auto rule - uncertain or complex routing
        self.add_rule(RoutingRule(
            name="auto_fallback_rule",
            conditions={},  # Always matches
            recommendation="/auto",
            confidence_base=0.40,
            reasoning_template="Uncertain routing context - let auto command determine best approach",
            priority=1
        ))
    
    def add_rule(self, rule: RoutingRule):
        """Add a routing rule"""
        self.rules.append(rule)
        # Sort by priority (higher priority first)
        self.rules.sort(key=lambda r: r.priority, reverse=True)
    
    def evaluate(self, context: UserContext) -> List[RoutingRecommendation]:
        """Evaluate all rules and return recommendations"""
        recommendations = []
        
        for rule in self.rules:
            matches, confidence = rule.evaluate(context)
            
            if matches and confidence > 0.3:  # Minimum confidence threshold
                # Generate context factors
                context_factors = []
                if context.is_small_project():
                    context_factors.append("small_project")
                if context.has_high_test_coverage():
                    context_factors.append("high_test_coverage")
                if context.indicates_new_feature():
                    context_factors.append("new_feature_detected")
                if context.indicates_bug_fix():
                    context_factors.append("bug_fix_detected")
                if context.indicates_research():
                    context_factors.append("research_detected")
                
                # Generate alternative commands
                alternatives = []
                for other_rule in self.rules:
                    if other_rule != rule:
                        alt_matches, alt_confidence = other_rule.evaluate(context)
                        if alt_matches and alt_confidence > 0.2:
                            alternatives.append(other_rule.recommendation)
                
                recommendation = RoutingRecommendation(
                    command=rule.recommendation,
                    confidence=confidence,
                    reasoning=rule.reasoning_template,
                    context_factors=context_factors,
                    alternative_commands=alternatives[:3],  # Top 3 alternatives
                    parameters={
                        "file_count": context.file_count,
                        "project_complexity": context.project_complexity,
                        "project_type": context.project_type
                    }
                )
                
                recommendations.append(recommendation)
        
        # Sort by confidence and return top recommendations
        recommendations.sort(key=lambda r: r.confidence, reverse=True)
        return recommendations[:5]  # Top 5 recommendations


class RoutingEngine:
    """Main AI-powered routing recommendation engine"""
    
    def __init__(self, framework_path: Path, project_path: Path):
        """Initialize routing engine"""
        self.framework_path = framework_path
        self.project_path = project_path
        self.decision_tree = RoutingDecisionTree()
        self.project_analyzer = ProjectAnalyzer(project_path)
        
        # Learning data
        self.feedback_history = []
        self.user_patterns = defaultdict(list)
        
        # Load available commands
        self.available_commands = self._load_available_commands()
    
    def _load_available_commands(self) -> List[str]:
        """Load available commands from framework"""
        commands = []
        
        commands_dir = self.framework_path / "commands"
        if commands_dir.exists():
            for cmd_file in commands_dir.glob("*.md"):
                commands.append(f"/{cmd_file.stem}")
        
        return commands
    
    def get_routing_recommendation(self, 
                                 user_input: str, 
                                 recent_commands: List[str] = None) -> RoutingRecommendation:
        """Get the best routing recommendation"""
        # Analyze project context
        project_analysis = self.project_analyzer.analyze_project_structure()
        
        # Create user context
        context = UserContext.from_project_analysis(
            user_input=user_input,
            project_data=project_analysis,
            recent_commands=recent_commands or []
        )
        
        # Get recommendations from decision tree
        recommendations = self.decision_tree.evaluate(context)
        
        if recommendations:
            # Apply learning adjustments
            best_recommendation = self._apply_learning_adjustments(recommendations[0], context)
            return best_recommendation
        else:
            # Fallback recommendation
            return RoutingRecommendation(
                command="/auto",
                confidence=0.5,
                reasoning="No specific pattern detected - using auto command for intelligent routing",
                context_factors=["fallback"],
                alternative_commands=self.available_commands[:3]
            )
    
    def get_multiple_recommendations(self, 
                                   user_input: str, 
                                   recent_commands: List[str] = None,
                                   max_recommendations: int = 3) -> List[RoutingRecommendation]:
        """Get multiple routing recommendations"""
        # Analyze project context
        project_analysis = self.project_analyzer.analyze_project_structure()
        
        # Create user context
        context = UserContext.from_project_analysis(
            user_input=user_input,
            project_data=project_analysis,
            recent_commands=recent_commands or []
        )
        
        # Get recommendations from decision tree
        recommendations = self.decision_tree.evaluate(context)
        
        # Apply learning adjustments to all recommendations
        adjusted_recommendations = []
        for rec in recommendations[:max_recommendations]:
            adjusted = self._apply_learning_adjustments(rec, context)
            adjusted_recommendations.append(adjusted)
        
        return adjusted_recommendations
    
    def _apply_learning_adjustments(self, 
                                  recommendation: RoutingRecommendation, 
                                  context: UserContext) -> RoutingRecommendation:
        """Apply learning adjustments based on feedback history"""
        # Simple learning: adjust confidence based on past feedback
        for feedback in self.feedback_history:
            if (feedback.get("recommended_command") == recommendation.command and 
                self._contexts_similar(feedback.get("context", {}), context)):
                
                rating = feedback.get("user_rating", 3)
                if rating >= 4:
                    recommendation.confidence = min(1.0, recommendation.confidence * 1.1)
                elif rating <= 2:
                    recommendation.confidence = max(0.1, recommendation.confidence * 0.9)
        
        return recommendation
    
    def _contexts_similar(self, context1: Dict[str, Any], context2: UserContext) -> bool:
        """Check if contexts are similar for learning purposes"""
        # Simple similarity check
        if context1.get("project_complexity") == context2.project_complexity:
            return True
        
        if abs(context1.get("file_count", 0) - context2.file_count) < 10:
            return True
        
        return False
    
    def learn_from_feedback(self, feedback: Dict[str, Any]) -> bool:
        """Learn from user feedback"""
        try:
            # Store feedback
            feedback["timestamp"] = datetime.now().isoformat()
            self.feedback_history.append(feedback)
            
            # Update user patterns
            user_input = feedback.get("user_input", "")
            actual_command = feedback.get("actual_command", "")
            
            if user_input and actual_command:
                self.user_patterns[user_input].append(actual_command)
            
            # Limit history size
            if len(self.feedback_history) > 100:
                self.feedback_history = self.feedback_history[-100:]
            
            return True
        except Exception:
            return False
    
    def explain_recommendation(self, recommendation: RoutingRecommendation) -> Dict[str, Any]:
        """Explain recommendation logic"""
        return {
            "decision_path": f"Analyzed input '{recommendation.parameters.get('user_input', 'N/A')}' with project context",
            "context_factors": {
                "file_count": recommendation.parameters.get("file_count", 0),
                "project_type": recommendation.parameters.get("project_type", "unknown"),
                "project_complexity": recommendation.parameters.get("project_complexity", "unknown"),
                "detected_patterns": recommendation.context_factors
            },
            "alternative_paths": [
                {"command": cmd, "reason": f"Alternative for different interpretation"}
                for cmd in recommendation.alternative_commands
            ],
            "confidence_breakdown": {
                "base_confidence": 0.7,
                "context_adjustments": recommendation.confidence - 0.7,
                "learning_adjustments": "Applied based on historical feedback"
            }
        }
    
    def get_available_commands(self) -> List[str]:
        """Get available commands"""
        return self.available_commands
    
    def save_model(self, model_path: Path) -> bool:
        """Save routing model"""
        try:
            model_data = {
                "feedback_history": self.feedback_history,
                "user_patterns": dict(self.user_patterns),
                "timestamp": datetime.now().isoformat()
            }
            
            with open(model_path, 'w') as f:
                json.dump(model_data, f, indent=2)
            
            return True
        except Exception:
            return False
    
    def load_model(self, model_path: Path) -> bool:
        """Load routing model"""
        try:
            if not model_path.exists():
                return False
            
            with open(model_path, 'r') as f:
                model_data = json.load(f)
            
            self.feedback_history = model_data.get("feedback_history", [])
            self.user_patterns = defaultdict(list, model_data.get("user_patterns", {}))
            
            return True
        except Exception:
            return False
    
    def render_routing_ui(self):
        """Render routing recommendation UI"""
        st.title("🎯 AI-Powered Routing Recommendations")
        
        # Input section
        st.subheader("📝 Get Routing Recommendation")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            user_input = st.text_area(
                "Describe what you want to do:",
                placeholder="e.g., Fix the login bug in the authentication service",
                height=100
            )
        
        with col2:
            st.markdown("**Project Context**")
            if self.project_path.exists():
                project_analysis = self.project_analyzer.analyze_project_structure()
                st.metric("Files", project_analysis["file_count"])
                st.metric("Complexity", project_analysis["complexity"])
                st.metric("Test Coverage", f"{project_analysis['test_coverage_estimate']}%")
            else:
                st.info("No project detected")
        
        # Get recommendation
        if st.button("🔍 Get Recommendation") and user_input:
            with st.spinner("Analyzing and generating recommendation..."):
                # Get recent commands from session state
                recent_commands = st.session_state.get("recent_commands", [])
                
                # Get multiple recommendations
                recommendations = self.get_multiple_recommendations(
                    user_input=user_input,
                    recent_commands=recent_commands,
                    max_recommendations=3
                )
                
                if recommendations:
                    st.success(f"Found {len(recommendations)} recommendation(s)")
                    
                    # Display primary recommendation
                    primary_rec = recommendations[0]
                    
                    st.subheader("🎯 Primary Recommendation")
                    
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.markdown(f"### {primary_rec.command}")
                        st.markdown(f"**Confidence:** {primary_rec.confidence:.1%}")
                        st.markdown(f"**Reasoning:** {primary_rec.reasoning}")
                        
                        # Context factors
                        if primary_rec.context_factors:
                            st.markdown("**Context Factors:**")
                            for factor in primary_rec.context_factors:
                                st.markdown(f"• {factor.replace('_', ' ').title()}")
                    
                    with col2:
                        st.markdown("**Alternative Commands:**")
                        for alt_cmd in primary_rec.alternative_commands:
                            st.markdown(f"• {alt_cmd}")
                        
                        # Quick action buttons
                        if st.button("✅ Use This Recommendation"):
                            st.session_state["selected_command"] = primary_rec.command
                            st.success(f"Selected: {primary_rec.command}")
                        
                        if st.button("📊 Explain Decision"):
                            explanation = self.explain_recommendation(primary_rec)
                            st.json(explanation)
                    
                    # Show alternative recommendations
                    if len(recommendations) > 1:
                        st.subheader("🔄 Alternative Recommendations")
                        
                        for i, rec in enumerate(recommendations[1:], 1):
                            with st.expander(f"Alternative {i}: {rec.command} (Confidence: {rec.confidence:.1%})"):
                                st.markdown(f"**Reasoning:** {rec.reasoning}")
                                
                                col1, col2 = st.columns(2)
                                with col1:
                                    if rec.context_factors:
                                        st.markdown("**Context Factors:**")
                                        for factor in rec.context_factors:
                                            st.markdown(f"• {factor.replace('_', ' ').title()}")
                                
                                with col2:
                                    if st.button(f"Use {rec.command}", key=f"use_alt_{i}"):
                                        st.session_state["selected_command"] = rec.command
                                        st.success(f"Selected: {rec.command}")
                    
                    # Feedback section
                    st.subheader("💬 Provide Feedback")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        actual_command = st.selectbox(
                            "What command did you actually use?",
                            options=[""] + self.available_commands,
                            key="actual_command"
                        )
                    
                    with col2:
                        rating = st.slider(
                            "How helpful was this recommendation?",
                            min_value=1,
                            max_value=5,
                            value=3,
                            key="rating"
                        )
                    
                    with col3:
                        if st.button("Submit Feedback") and actual_command:
                            feedback = {
                                "user_input": user_input,
                                "recommended_command": primary_rec.command,
                                "actual_command": actual_command,
                                "user_rating": rating,
                                "context": {
                                    "file_count": primary_rec.parameters.get("file_count", 0),
                                    "project_complexity": primary_rec.parameters.get("project_complexity", "unknown")
                                }
                            }
                            
                            if self.learn_from_feedback(feedback):
                                st.success("Thank you for your feedback!")
                            else:
                                st.error("Failed to save feedback")
                
                else:
                    st.warning("No recommendations generated")
        
        # Statistics and learning section
        st.divider()
        st.subheader("📊 Routing Statistics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Available Commands**")
            for cmd in self.available_commands:
                st.markdown(f"• {cmd}")
        
        with col2:
            st.markdown("**Learning Statistics**")
            st.metric("Feedback Entries", len(self.feedback_history))
            st.metric("User Patterns", len(self.user_patterns))
            
            if self.feedback_history:
                avg_rating = sum(f.get("user_rating", 3) for f in self.feedback_history) / len(self.feedback_history)
                st.metric("Average Rating", f"{avg_rating:.1f}/5")
        
        # Model management
        st.divider()
        st.subheader("🧠 Model Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💾 Save Model"):
                model_path = Path("routing_model.json")
                if self.save_model(model_path):
                    st.success(f"Model saved to {model_path}")
                else:
                    st.error("Failed to save model")
        
        with col2:
            uploaded_file = st.file_uploader("📤 Load Model", type=['json'])
            if uploaded_file:
                import tempfile
                with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
                    tmp.write(uploaded_file.read().decode())
                    tmp_path = Path(tmp.name)
                
                if self.load_model(tmp_path):
                    st.success("Model loaded successfully!")
                    st.rerun()
                else:
                    st.error("Failed to load model")
    
    def render(self):
        """Main render method"""
        self.render_routing_ui()