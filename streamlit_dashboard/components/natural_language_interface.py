"""
Natural Language Workflow Builder for Claude Code Framework Dashboard
Conversational interface with step-by-step guidance and decision support
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import json
import re
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime
import random


@dataclass
class WorkflowStep:
    """Represents a single step in a workflow"""
    step_id: str
    title: str
    description: str
    command: str
    module: Optional[str]
    prerequisites: List[str]
    expected_output: str
    success_criteria: List[str]
    common_issues: List[str]
    estimated_time: int  # in minutes


@dataclass
class Workflow:
    """Represents a complete workflow"""
    workflow_id: str
    name: str
    description: str
    steps: List[WorkflowStep]
    total_time: int
    difficulty: str
    success_rate: float
    tags: List[str]


class NaturalLanguageInterface:
    """Natural language workflow builder with conversational interface"""
    
    def __init__(self, framework_path: Path):
        self.framework_path = framework_path
        self.conversation_history = []
        self.current_workflow = None
        self.user_context = {}
        self.intent_patterns = self._load_intent_patterns()
        self.workflow_templates = self._load_workflow_templates()
        self.step_guidance = self._load_step_guidance()
        
    def _load_intent_patterns(self) -> Dict[str, List[str]]:
        """Load intent recognition patterns"""
        return {
            "want_to_build": [
                r"i want to (?:build|create|make|develop) (.+)",
                r"how do i (?:build|create|make|develop) (.+)",
                r"need help (?:building|creating|making|developing) (.+)",
                r"(?:build|create|make|develop) (.+) for me"
            ],
            "want_to_fix": [
                r"i (?:need to|want to) fix (.+)",
                r"how do i fix (.+)",
                r"there's (?:a bug|an issue|a problem) with (.+)",
                r"(?:fix|solve|resolve) (.+) issue"
            ],
            "want_to_learn": [
                r"how do i (?:learn|understand) (.+)",
                r"what is (.+)",
                r"can you explain (.+)",
                r"i don't understand (.+)"
            ],
            "want_to_optimize": [
                r"how can i (?:optimize|improve) (.+)",
                r"make (.+) (?:faster|better|more efficient)",
                r"(?:optimize|improve|enhance) (.+)"
            ],
            "want_to_deploy": [
                r"how do i (?:deploy|release) (.+)",
                r"deploy (.+) to (?:production|staging)",
                r"ready to (?:deploy|release) (.+)"
            ],
            "want_to_test": [
                r"how do i test (.+)",
                r"need to (?:test|validate) (.+)",
                r"write tests for (.+)"
            ]
        }
    
    def _load_workflow_templates(self) -> Dict[str, Workflow]:
        """Load predefined workflow templates"""
        return {
            "build_new_feature": Workflow(
                workflow_id="build_new_feature",
                name="Build New Feature",
                description="Complete workflow for building a new feature from scratch",
                steps=[
                    WorkflowStep(
                        step_id="research",
                        title="Research and Understanding",
                        description="Understand the requirements and existing codebase",
                        command="/query",
                        module="research-analysis-pattern",
                        prerequisites=[],
                        expected_output="Comprehensive understanding of requirements and codebase",
                        success_criteria=["Clear problem definition", "Existing code analysis complete"],
                        common_issues=["Insufficient research", "Missing requirements"],
                        estimated_time=15
                    ),
                    WorkflowStep(
                        step_id="plan",
                        title="Feature Planning",
                        description="Create detailed feature plan with PRD",
                        command="/feature",
                        module="workflow-orchestration-engine",
                        prerequisites=["research"],
                        expected_output="Feature plan with PRD and implementation strategy",
                        success_criteria=["PRD created", "Implementation plan defined"],
                        common_issues=["Vague requirements", "Missing edge cases"],
                        estimated_time=20
                    ),
                    WorkflowStep(
                        step_id="implement",
                        title="Implementation",
                        description="Implement the feature with TDD approach",
                        command="/task",
                        module="tdd-cycle-pattern",
                        prerequisites=["plan"],
                        expected_output="Working feature implementation with tests",
                        success_criteria=["Tests passing", "Feature working", "Code quality maintained"],
                        common_issues=["Skipping tests", "Poor error handling"],
                        estimated_time=45
                    ),
                    WorkflowStep(
                        step_id="validate",
                        title="Validation and Deployment",
                        description="Validate feature and prepare for deployment",
                        command="/protocol",
                        module="production-validation",
                        prerequisites=["implement"],
                        expected_output="Production-ready feature",
                        success_criteria=["All tests passing", "Production checks complete"],
                        common_issues=["Missing edge case tests", "Performance issues"],
                        estimated_time=25
                    )
                ],
                total_time=105,
                difficulty="medium",
                success_rate=0.87,
                tags=["feature", "development", "tdd"]
            ),
            "fix_bug": Workflow(
                workflow_id="fix_bug",
                name="Fix Bug",
                description="Systematic approach to fixing bugs",
                steps=[
                    WorkflowStep(
                        step_id="investigate",
                        title="Bug Investigation",
                        description="Understand and reproduce the bug",
                        command="/query",
                        module="research-analysis-pattern",
                        prerequisites=[],
                        expected_output="Clear understanding of bug and root cause",
                        success_criteria=["Bug reproduced", "Root cause identified"],
                        common_issues=["Insufficient investigation", "Wrong assumptions"],
                        estimated_time=20
                    ),
                    WorkflowStep(
                        step_id="fix",
                        title="Implement Fix",
                        description="Fix the bug with proper testing",
                        command="/task",
                        module="tdd-cycle-pattern",
                        prerequisites=["investigate"],
                        expected_output="Bug fix with regression tests",
                        success_criteria=["Bug fixed", "Tests prevent regression"],
                        common_issues=["Incomplete fix", "Missing regression tests"],
                        estimated_time=30
                    )
                ],
                total_time=50,
                difficulty="low",
                success_rate=0.92,
                tags=["bug", "fix", "testing"]
            ),
            "optimize_performance": Workflow(
                workflow_id="optimize_performance",
                name="Optimize Performance",
                description="Systematic performance optimization workflow",
                steps=[
                    WorkflowStep(
                        step_id="analyze",
                        title="Performance Analysis",
                        description="Analyze current performance and identify bottlenecks",
                        command="/query",
                        module="research-analysis-pattern",
                        prerequisites=[],
                        expected_output="Performance baseline and bottleneck identification",
                        success_criteria=["Performance metrics collected", "Bottlenecks identified"],
                        common_issues=["Inadequate profiling", "Wrong optimization targets"],
                        estimated_time=25
                    ),
                    WorkflowStep(
                        step_id="optimize",
                        title="Implement Optimizations",
                        description="Apply performance optimizations",
                        command="/task",
                        module="performance-optimization",
                        prerequisites=["analyze"],
                        expected_output="Performance improvements implemented",
                        success_criteria=["Measurable performance gains", "No regression"],
                        common_issues=["Premature optimization", "Breaking changes"],
                        estimated_time=40
                    ),
                    WorkflowStep(
                        step_id="validate",
                        title="Validate Improvements",
                        description="Measure and validate performance improvements",
                        command="/protocol",
                        module="performance-validation",
                        prerequisites=["optimize"],
                        expected_output="Validated performance improvements",
                        success_criteria=["Performance targets met", "No side effects"],
                        common_issues=["Insufficient testing", "Regression introduced"],
                        estimated_time=20
                    )
                ],
                total_time=85,
                difficulty="high",
                success_rate=0.78,
                tags=["performance", "optimization", "analysis"]
            ),
            "create_documentation": Workflow(
                workflow_id="create_documentation",
                name="Create Documentation",
                description="Comprehensive documentation creation workflow",
                steps=[
                    WorkflowStep(
                        step_id="analyze",
                        title="Documentation Analysis",
                        description="Analyze what documentation is needed",
                        command="/query",
                        module="research-analysis-pattern",
                        prerequisites=[],
                        expected_output="Documentation requirements and gaps identified",
                        success_criteria=["Documentation audit complete", "Gaps identified"],
                        common_issues=["Missing user perspective", "Incomplete analysis"],
                        estimated_time=15
                    ),
                    WorkflowStep(
                        step_id="create",
                        title="Create Documentation",
                        description="Generate comprehensive documentation",
                        command="/docs",
                        module="documentation-pattern",
                        prerequisites=["analyze"],
                        expected_output="Complete documentation set",
                        success_criteria=["All sections covered", "Clear and comprehensive"],
                        common_issues=["Too technical", "Missing examples"],
                        estimated_time=35
                    )
                ],
                total_time=50,
                difficulty="low",
                success_rate=0.89,
                tags=["documentation", "writing", "analysis"]
            )
        }
    
    def _load_step_guidance(self) -> Dict[str, Dict[str, Any]]:
        """Load step-by-step guidance information"""
        return {
            "research": {
                "checklist": [
                    "Define the problem clearly",
                    "Understand user requirements",
                    "Analyze existing codebase",
                    "Identify potential challenges",
                    "Research best practices"
                ],
                "tips": [
                    "Take time to understand the full context",
                    "Don't rush into implementation",
                    "Ask clarifying questions",
                    "Document your findings"
                ],
                "common_mistakes": [
                    "Insufficient research",
                    "Making assumptions",
                    "Skipping edge cases",
                    "Not considering dependencies"
                ]
            },
            "planning": {
                "checklist": [
                    "Create detailed requirements",
                    "Design system architecture",
                    "Plan implementation phases",
                    "Identify testing strategy",
                    "Consider deployment requirements"
                ],
                "tips": [
                    "Break down complex features",
                    "Plan for error handling",
                    "Consider performance implications",
                    "Design for maintainability"
                ],
                "common_mistakes": [
                    "Vague specifications",
                    "Overengineering",
                    "Missing error scenarios",
                    "Inadequate testing plans"
                ]
            },
            "implementation": {
                "checklist": [
                    "Write tests first (TDD)",
                    "Implement minimal viable solution",
                    "Handle edge cases",
                    "Add proper error handling",
                    "Maintain code quality"
                ],
                "tips": [
                    "Follow TDD cycle strictly",
                    "Commit frequently",
                    "Keep functions small",
                    "Write clear comments"
                ],
                "common_mistakes": [
                    "Skipping tests",
                    "Poor error handling",
                    "Overly complex solutions",
                    "Ignoring code quality"
                ]
            }
        }
    
    def recognize_intent(self, user_input: str) -> Tuple[str, str]:
        """Recognize user intent from natural language input"""
        user_input = user_input.lower().strip()
        
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, user_input)
                if match:
                    extracted_object = match.group(1) if match.groups() else ""
                    return intent, extracted_object
        
        return "unknown", user_input
    
    def generate_workflow(self, intent: str, object_description: str) -> Optional[Workflow]:
        """Generate a workflow based on recognized intent"""
        workflow_mapping = {
            "want_to_build": "build_new_feature",
            "want_to_fix": "fix_bug",
            "want_to_optimize": "optimize_performance",
            "want_to_learn": "create_documentation",
            "want_to_deploy": "build_new_feature",  # Deploy usually follows build
            "want_to_test": "fix_bug"  # Testing workflow similar to bug fixing
        }
        
        template_id = workflow_mapping.get(intent)
        if template_id and template_id in self.workflow_templates:
            workflow = self.workflow_templates[template_id]
            # Customize workflow based on object description
            customized_workflow = self._customize_workflow(workflow, object_description)
            return customized_workflow
        
        return None
    
    def _customize_workflow(self, workflow: Workflow, object_description: str) -> Workflow:
        """Customize workflow based on specific object description"""
        # Create a copy of the workflow
        customized_steps = []
        for step in workflow.steps:
            customized_step = WorkflowStep(
                step_id=step.step_id,
                title=step.title,
                description=step.description.replace("feature", object_description) if object_description else step.description,
                command=step.command,
                module=step.module,
                prerequisites=step.prerequisites,
                expected_output=step.expected_output,
                success_criteria=step.success_criteria,
                common_issues=step.common_issues,
                estimated_time=step.estimated_time
            )
            customized_steps.append(customized_step)
        
        return Workflow(
            workflow_id=f"{workflow.workflow_id}_custom",
            name=workflow.name + f" ({object_description})" if object_description else workflow.name,
            description=workflow.description,
            steps=customized_steps,
            total_time=workflow.total_time,
            difficulty=workflow.difficulty,
            success_rate=workflow.success_rate,
            tags=workflow.tags
        )
    
    def generate_dynamic_questions(self, workflow: Workflow) -> List[Dict[str, Any]]:
        """Generate dynamic questions to better understand user needs"""
        questions = []
        
        # Base questions for all workflows
        questions.extend([
            {
                "question": "What's your experience level with this type of task?",
                "type": "select",
                "options": ["Beginner", "Intermediate", "Advanced"],
                "key": "experience_level"
            },
            {
                "question": "What's your primary programming language?",
                "type": "select",
                "options": ["Python", "JavaScript", "TypeScript", "Java", "Go", "Rust", "Other"],
                "key": "primary_language"
            },
            {
                "question": "How complex is your project?",
                "type": "select",
                "options": ["Simple (< 10 files)", "Medium (10-50 files)", "Large (> 50 files)"],
                "key": "project_complexity"
            }
        ])
        
        # Workflow-specific questions
        if workflow.workflow_id == "build_new_feature":
            questions.extend([
                {
                    "question": "Is this a frontend, backend, or full-stack feature?",
                    "type": "select",
                    "options": ["Frontend", "Backend", "Full-stack", "Not sure"],
                    "key": "feature_type"
                },
                {
                    "question": "Do you have existing tests in your project?",
                    "type": "select",
                    "options": ["Yes, comprehensive", "Some tests", "No tests"],
                    "key": "existing_tests"
                }
            ])
        elif workflow.workflow_id == "fix_bug":
            questions.extend([
                {
                    "question": "Can you reproduce the bug consistently?",
                    "type": "select",
                    "options": ["Yes, always", "Sometimes", "No, it's intermittent"],
                    "key": "bug_reproducibility"
                },
                {
                    "question": "Do you have error logs or stack traces?",
                    "type": "select",
                    "options": ["Yes, detailed logs", "Some information", "No logs available"],
                    "key": "error_information"
                }
            ])
        elif workflow.workflow_id == "optimize_performance":
            questions.extend([
                {
                    "question": "What type of performance issue are you experiencing?",
                    "type": "select",
                    "options": ["Slow response times", "High memory usage", "CPU bottlenecks", "Database queries"],
                    "key": "performance_issue"
                },
                {
                    "question": "Do you have performance monitoring tools?",
                    "type": "select",
                    "options": ["Yes, comprehensive", "Basic monitoring", "No monitoring"],
                    "key": "monitoring_tools"
                }
            ])
        
        return questions
    
    def adjust_workflow_based_on_answers(self, workflow: Workflow, answers: Dict[str, Any]) -> Workflow:
        """Adjust workflow based on user answers"""
        adjusted_steps = []
        
        for step in workflow.steps:
            # Adjust time estimates based on experience
            time_multiplier = 1.0
            if answers.get("experience_level") == "Beginner":
                time_multiplier = 1.5
            elif answers.get("experience_level") == "Advanced":
                time_multiplier = 0.8
            
            # Adjust based on project complexity
            if answers.get("project_complexity") == "Large (> 50 files)":
                time_multiplier *= 1.3
            elif answers.get("project_complexity") == "Simple (< 10 files)":
                time_multiplier *= 0.8
            
            adjusted_time = int(step.estimated_time * time_multiplier)
            
            # Customize step descriptions based on answers
            description = step.description
            if answers.get("primary_language"):
                description += f" (Focus on {answers['primary_language']} best practices)"
            
            adjusted_step = WorkflowStep(
                step_id=step.step_id,
                title=step.title,
                description=description,
                command=step.command,
                module=step.module,
                prerequisites=step.prerequisites,
                expected_output=step.expected_output,
                success_criteria=step.success_criteria,
                common_issues=step.common_issues,
                estimated_time=adjusted_time
            )
            adjusted_steps.append(adjusted_step)
        
        return Workflow(
            workflow_id=workflow.workflow_id + "_adjusted",
            name=workflow.name + " (Personalized)",
            description=workflow.description,
            steps=adjusted_steps,
            total_time=sum(step.estimated_time for step in adjusted_steps),
            difficulty=workflow.difficulty,
            success_rate=workflow.success_rate,
            tags=workflow.tags + ["personalized"]
        )
    
    def render(self):
        """Render the natural language interface"""
        st.title("🗣️ Natural Language Workflow Builder")
        st.markdown("Tell me what you want to accomplish, and I'll guide you through the process!")
        
        # Initialize session state
        if "conversation_history" not in st.session_state:
            st.session_state.conversation_history = []
        if "current_workflow" not in st.session_state:
            st.session_state.current_workflow = None
        if "user_context" not in st.session_state:
            st.session_state.user_context = {}
        
        # Create tabs
        tab1, tab2, tab3 = st.tabs([
            "💬 Conversation",
            "📋 Workflow Guide",
            "✅ Progress Tracker"
        ])
        
        with tab1:
            self._render_conversation_interface()
        
        with tab2:
            self._render_workflow_guide()
        
        with tab3:
            self._render_progress_tracker()
    
    def _render_conversation_interface(self):
        """Render the conversational interface"""
        st.subheader("💬 Tell me what you want to accomplish")
        
        # Display conversation history
        if st.session_state.conversation_history:
            st.markdown("### Conversation History")
            for i, exchange in enumerate(st.session_state.conversation_history):
                with st.expander(f"Exchange {i+1}: {exchange['user_input'][:50]}..."):
                    st.markdown(f"**You:** {exchange['user_input']}")
                    st.markdown(f"**Assistant:** {exchange['assistant_response']}")
                    if exchange.get('workflow'):
                        st.markdown(f"**Suggested Workflow:** {exchange['workflow'].name}")
        
        # Input field
        user_input = st.text_area(
            "What would you like to do?",
            placeholder="e.g., 'I want to build a user authentication system' or 'I need to fix a bug in my API'",
            height=100
        )
        
        col1, col2 = st.columns([1, 4])
        
        with col1:
            if st.button("🚀 Get Help", type="primary"):
                if user_input.strip():
                    # Recognize intent
                    intent, object_description = self.recognize_intent(user_input)
                    
                    # Generate workflow
                    workflow = self.generate_workflow(intent, object_description)
                    
                    if workflow:
                        # Generate response
                        response = self._generate_response(intent, object_description, workflow)
                        
                        # Store in conversation history
                        exchange = {
                            "user_input": user_input,
                            "assistant_response": response,
                            "intent": intent,
                            "object_description": object_description,
                            "workflow": workflow,
                            "timestamp": datetime.now().isoformat()
                        }
                        st.session_state.conversation_history.append(exchange)
                        st.session_state.current_workflow = workflow
                        
                        # Show response
                        st.success("Great! I understand what you want to do.")
                        st.markdown(response)
                        
                        # Show workflow preview
                        with st.expander("📋 Suggested Workflow Preview"):
                            self._show_workflow_preview(workflow)
                    else:
                        st.warning("I'm not sure how to help with that. Can you be more specific?")
                        
                        # Show available templates
                        st.markdown("Here are some things I can help you with:")
                        for template_id, template in self.workflow_templates.items():
                            st.markdown(f"- {template.name}: {template.description}")
                else:
                    st.warning("Please tell me what you'd like to accomplish!")
        
        with col2:
            if st.button("🔄 Start Over"):
                st.session_state.conversation_history = []
                st.session_state.current_workflow = None
                st.session_state.user_context = {}
                st.experimental_rerun()
    
    def _generate_response(self, intent: str, object_description: str, workflow: Workflow) -> str:
        """Generate a conversational response"""
        responses = {
            "want_to_build": f"I see you want to build {object_description}. That's exciting! I've prepared a comprehensive workflow that will guide you through the entire process, from research to deployment.",
            "want_to_fix": f"I understand you need to fix {object_description}. Don't worry, I'll help you systematically identify and resolve the issue.",
            "want_to_optimize": f"Great! Optimizing {object_description} requires a methodical approach. I'll help you identify bottlenecks and implement improvements safely.",
            "want_to_learn": f"Learning about {object_description} is a great goal! I'll guide you through understanding the concepts and creating practical documentation.",
            "want_to_deploy": f"Deploying {object_description} requires careful planning. I'll help you ensure everything is production-ready.",
            "want_to_test": f"Testing {object_description} is crucial for quality. I'll guide you through creating comprehensive tests."
        }
        
        base_response = responses.get(intent, f"I'll help you with {object_description}.")
        
        workflow_info = f"\n\nI've created a {workflow.difficulty} difficulty workflow with {len(workflow.steps)} steps that should take about {workflow.total_time} minutes. This approach has a {workflow.success_rate:.0%} success rate based on similar projects."
        
        return base_response + workflow_info
    
    def _show_workflow_preview(self, workflow: Workflow):
        """Show a preview of the workflow"""
        st.markdown(f"**{workflow.name}**")
        st.markdown(f"*{workflow.description}*")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Steps", len(workflow.steps))
        with col2:
            st.metric("Est. Time", f"{workflow.total_time}min")
        with col3:
            st.metric("Success Rate", f"{workflow.success_rate:.0%}")
        
        st.markdown("**Steps:**")
        for i, step in enumerate(workflow.steps, 1):
            st.markdown(f"{i}. **{step.title}** ({step.estimated_time}min) - {step.description}")
        
        if st.button("✨ Customize This Workflow"):
            st.session_state.show_customization = True
    
    def _render_workflow_guide(self):
        """Render the workflow guide interface"""
        st.subheader("📋 Step-by-Step Workflow Guide")
        
        if st.session_state.current_workflow:
            workflow = st.session_state.current_workflow
            
            # Show workflow customization if requested
            if st.session_state.get("show_customization", False):
                st.markdown("### 🎯 Customize Your Workflow")
                
                questions = self.generate_dynamic_questions(workflow)
                answers = {}
                
                for question in questions:
                    if question["type"] == "select":
                        answers[question["key"]] = st.selectbox(
                            question["question"],
                            options=question["options"],
                            key=f"q_{question['key']}"
                        )
                
                if st.button("🔧 Apply Customizations"):
                    customized_workflow = self.adjust_workflow_based_on_answers(workflow, answers)
                    st.session_state.current_workflow = customized_workflow
                    st.session_state.user_context = answers
                    st.session_state.show_customization = False
                    st.success("Workflow customized successfully!")
                    st.experimental_rerun()
            
            # Show the workflow steps
            st.markdown(f"### {workflow.name}")
            st.markdown(f"*{workflow.description}*")
            
            # Progress indicator
            if "current_step" not in st.session_state:
                st.session_state.current_step = 0
            
            progress = st.session_state.current_step / len(workflow.steps)
            st.progress(progress)
            st.markdown(f"**Progress:** Step {st.session_state.current_step + 1} of {len(workflow.steps)}")
            
            # Show current step details
            if st.session_state.current_step < len(workflow.steps):
                current_step = workflow.steps[st.session_state.current_step]
                
                st.markdown(f"## Step {st.session_state.current_step + 1}: {current_step.title}")
                st.markdown(f"**Estimated Time:** {current_step.estimated_time} minutes")
                st.markdown(f"**Description:** {current_step.description}")
                
                # Show step guidance
                step_type = current_step.step_id
                if step_type in self.step_guidance:
                    guidance = self.step_guidance[step_type]
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**✅ Checklist:**")
                        for item in guidance["checklist"]:
                            st.markdown(f"- [ ] {item}")
                        
                        st.markdown("**💡 Tips:**")
                        for tip in guidance["tips"]:
                            st.markdown(f"- {tip}")
                    
                    with col2:
                        st.markdown("**⚠️ Common Mistakes:**")
                        for mistake in guidance["common_mistakes"]:
                            st.markdown(f"- {mistake}")
                        
                        st.markdown("**🎯 Success Criteria:**")
                        for criterion in current_step.success_criteria:
                            st.markdown(f"- {criterion}")
                
                # Action buttons
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if st.button("⏭️ Next Step", disabled=st.session_state.current_step >= len(workflow.steps) - 1):
                        st.session_state.current_step += 1
                        st.experimental_rerun()
                
                with col2:
                    if st.button("⏮️ Previous Step", disabled=st.session_state.current_step <= 0):
                        st.session_state.current_step -= 1
                        st.experimental_rerun()
                
                with col3:
                    if st.button("🔄 Reset Progress"):
                        st.session_state.current_step = 0
                        st.experimental_rerun()
                
                # Show command to run
                st.markdown("---")
                st.markdown(f"**🚀 Command to Run:** `{current_step.command}`")
                if current_step.module:
                    st.markdown(f"**🧩 Module:** `{current_step.module}`")
                
                st.markdown(f"**📋 Expected Output:** {current_step.expected_output}")
                
                if current_step.common_issues:
                    with st.expander("⚠️ Common Issues & Solutions"):
                        for issue in current_step.common_issues:
                            st.markdown(f"- {issue}")
            
            else:
                st.success("🎉 Workflow Complete!")
                st.markdown("Congratulations! You've completed all the steps in your workflow.")
                st.balloons()
                
                if st.button("🔄 Start New Workflow"):
                    st.session_state.current_workflow = None
                    st.session_state.current_step = 0
                    st.experimental_rerun()
        
        else:
            st.info("Start a conversation to get a personalized workflow guide!")
            
            # Show available templates
            st.markdown("### 📚 Available Workflow Templates")
            
            for template_id, template in self.workflow_templates.items():
                with st.expander(f"{template.name} ({template.difficulty} difficulty)"):
                    st.markdown(f"**Description:** {template.description}")
                    st.markdown(f"**Steps:** {len(template.steps)}")
                    st.markdown(f"**Estimated Time:** {template.total_time} minutes")
                    st.markdown(f"**Success Rate:** {template.success_rate:.0%}")
                    
                    if st.button(f"Use {template.name}", key=f"use_{template_id}"):
                        st.session_state.current_workflow = template
                        st.session_state.current_step = 0
                        st.experimental_rerun()
    
    def _render_progress_tracker(self):
        """Render the progress tracking interface"""
        st.subheader("✅ Progress Tracker")
        
        if st.session_state.current_workflow:
            workflow = st.session_state.current_workflow
            
            # Overall progress
            current_step = st.session_state.get("current_step", 0)
            progress = current_step / len(workflow.steps)
            
            st.markdown("### 📊 Overall Progress")
            st.progress(progress)
            st.markdown(f"**Completed:** {current_step}/{len(workflow.steps)} steps ({progress:.0%})")
            
            # Time tracking
            completed_time = sum(step.estimated_time for step in workflow.steps[:current_step])
            remaining_time = workflow.total_time - completed_time
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Time Spent", f"{completed_time}min")
            
            with col2:
                st.metric("Time Remaining", f"{remaining_time}min")
            
            with col3:
                st.metric("Total Time", f"{workflow.total_time}min")
            
            # Step-by-step progress
            st.markdown("### 📝 Step Progress")
            
            for i, step in enumerate(workflow.steps):
                if i < current_step:
                    st.markdown(f"✅ **Step {i+1}: {step.title}** - Completed ({step.estimated_time}min)")
                elif i == current_step:
                    st.markdown(f"🔄 **Step {i+1}: {step.title}** - In Progress ({step.estimated_time}min)")
                else:
                    st.markdown(f"⏳ **Step {i+1}: {step.title}** - Pending ({step.estimated_time}min)")
            
            # Success prediction
            st.markdown("### 🎯 Success Prediction")
            
            # Calculate success probability based on progress
            base_success_rate = workflow.success_rate
            progress_bonus = progress * 0.1  # 10% bonus for progress
            user_experience = st.session_state.user_context.get("experience_level", "Intermediate")
            
            experience_multiplier = {
                "Beginner": 0.9,
                "Intermediate": 1.0,
                "Advanced": 1.1
            }
            
            predicted_success = min(base_success_rate + progress_bonus, 1.0) * experience_multiplier.get(user_experience, 1.0)
            
            st.metric("Predicted Success Rate", f"{predicted_success:.0%}")
            
            # Show factors affecting success
            st.markdown("**Factors Affecting Success:**")
            st.markdown(f"- Base workflow success rate: {base_success_rate:.0%}")
            st.markdown(f"- Progress bonus: +{progress_bonus:.0%}")
            st.markdown(f"- Experience level ({user_experience}): {experience_multiplier.get(user_experience, 1.0):.0%}")
            
            # Export progress
            if st.button("📊 Export Progress Report"):
                progress_data = {
                    "workflow_name": workflow.name,
                    "total_steps": len(workflow.steps),
                    "completed_steps": current_step,
                    "progress_percentage": progress * 100,
                    "time_spent": completed_time,
                    "time_remaining": remaining_time,
                    "predicted_success_rate": predicted_success * 100,
                    "user_context": st.session_state.user_context
                }
                
                st.download_button(
                    label="Download Progress Report",
                    data=json.dumps(progress_data, indent=2),
                    file_name=f"workflow_progress_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
        
        else:
            st.info("No active workflow to track. Start a conversation to begin!")