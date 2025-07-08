#!/usr/bin/env python3
"""
Script to enhance all commands with prompt construction sections.
Adds assembly_preview, context_budget, runtime_visualization, and claude_4_interpretation.
"""

import os
import re
from pathlib import Path

# Define the base path
BASE_PATH = Path(__file__).parent.parent / ".claude" / "commands"

# Command-specific enhancements
COMMAND_ENHANCEMENTS = {
    "auto.md": {
        "version": "2.4.1",
        "workflow_steps": [
            "│ 1. Request     │ → Parse & categorize request",
            "│    Analysis    │",
            "│ 2. Complexity  │ → Calculate routing score", 
            "│    Scoring     │",
            "│ 3. Research    │ → Deep pattern investigation",
            "│    Phase       │", 
            "│ 4. Route       │ → Intelligent command selection",
            "│    Decision    │"
        ],
        "context_budget": "~8,000",
        "budget_breakdown": [
            "- Request analysis: 1,500",
            "- Complexity scoring: 1,000", 
            "- Research phase: 4,000",
            "- Routing decision: 1,500"
        ],
        "example_trace": [
            "[00:00] ▶️ START: /auto \"Build payment system\"",
            "[00:15] 🔍 ANALYSIS: Multi-component financial system detected",
            "[00:30] 📊 COMPLEXITY: Score 95/100 → High complexity",
            "[00:45] 📚 RESEARCH: Analyzing payment patterns and compliance",
            "[01:30] 🎯 ROUTING: Escalating to /swarm for multi-agent approach",
            "[01:35] ✅ COMPLETE: Routed with comprehensive analysis"
        ]
    },
    "swarm.md": {
        "version": "2.4.1", 
        "workflow_steps": [
            "│ 1. Session     │ → GitHub coordination hub",
            "│    Creation    │",
            "│ 2. Component   │ → Multi-agent decomposition",
            "│    Analysis    │",
            "│ 3. Worktree    │ → Isolation setup",
            "│    Setup       │",
            "│ 4. Parallel    │ → Task() execution",
            "│    Execution   │",
            "│ 5. Integration │ → Merge & validation",
            "│    Merge       │"
        ],
        "context_budget": "~25,000",
        "budget_breakdown": [
            "- Session coordination: 3,000",
            "- Component analysis: 5,000",
            "- Worktree operations: 2,000", 
            "- Parallel task execution: 12,000",
            "- Integration & merge: 3,000"
        ],
        "example_trace": [
            "[00:00] ▶️ START: /swarm \"E-commerce platform\"",
            "[00:30] 🎯 SESSION: Created GitHub #156 for coordination",
            "[00:45] 🔍 ANALYSIS: 4 components identified (auth, cart, payment, ui)",
            "[01:00] 🌳 WORKTREES: Setting up isolated development branches",
            "[01:15] 🚀 PARALLEL: Spawning 4 specialized Task() agents",
            "[02:00] ⚡ PROGRESS: All agents reporting green status",
            "[02:15] 🔗 MERGE: Integrating components with validation",
            "[02:30] ✅ COMPLETE: Platform deployed with full testing"
        ]
    },
    "query.md": {
        "version": "2.4.1",
        "workflow_steps": [
            "│ 1. Query       │ → Parse research intent",
            "│    Analysis    │",
            "│ 2. Parallel    │ → Multi-source search",
            "│    Search      │", 
            "│ 3. Deep        │ → Pattern analysis",
            "│    Analysis    │",
            "│ 4. Report      │ → Comprehensive findings",
            "│    Generation  │"
        ],
        "context_budget": "~10,000",
        "budget_breakdown": [
            "- Query parsing: 1,000",
            "- Parallel search: 4,000",
            "- Deep analysis: 3,500", 
            "- Report generation: 1,500"
        ],
        "example_trace": [
            "[00:00] ▶️ START: /query \"How does auth work?\"",
            "[00:15] 🔍 ANALYSIS: Authentication system research",
            "[00:30] 🔄 SEARCH: Parallel scanning auth modules...",
            "[01:00] 📊 ANALYSIS: Found 3 auth patterns, analyzing...",
            "[01:30] 📝 REPORT: Comprehensive auth analysis complete",
            "[01:35] ✅ COMPLETE: Research findings delivered"
        ]
    },
    "session.md": {
        "version": "2.4.1",
        "workflow_steps": [
            "│ 1. Session     │ → GitHub issue management",
            "│    Type        │",
            "│ 2. Context     │ → State preservation",  
            "│    Management  │",
            "│ 3. Artifact    │ → Link tracking",
            "│    Linking     │",
            "│ 4. Progress    │ → Status updates",
            "│    Tracking    │"
        ],
        "context_budget": "~6,000",
        "budget_breakdown": [
            "- Session operations: 2,000",
            "- Context preservation: 1,500",
            "- Artifact linking: 1,500",
            "- Progress updates: 1,000"
        ],
        "example_trace": [
            "[00:00] ▶️ START: /session create \"API refactor\"",
            "[00:15] 🎯 SESSION: GitHub issue #157 created",
            "[00:30] 💾 CONTEXT: Preserving session state",
            "[00:45] 🔗 ARTIFACTS: Linking related files and tasks",
            "[01:00] ✅ COMPLETE: Session ready for development"
        ]
    },
    "feature.md": {
        "version": "2.4.1",
        "workflow_steps": [
            "│ 1. PRD         │ → Requirements generation",
            "│    Generation  │",
            "│ 2. Session     │ → GitHub coordination",
            "│    Creation    │",
            "│ 3. MVP         │ → Minimum viable scope",
            "│    Analysis    │", 
            "│ 4. TDD         │ → Test-driven execution",
            "│    Execution   │",
            "│ 5. Quality     │ → Production standards",
            "│    Gates       │"
        ],
        "context_budget": "~18,000",
        "budget_breakdown": [
            "- PRD generation: 4,000",
            "- Session setup: 2,000",
            "- MVP analysis: 3,000",
            "- TDD execution: 7,000", 
            "- Quality validation: 2,000"
        ],
        "example_trace": [
            "[00:00] ▶️ START: /feature \"User notifications\"",
            "[00:30] 📋 PRD: Generated comprehensive requirements",
            "[00:45] 🎯 SESSION: GitHub issue #158 tracking feature",
            "[01:00] 🎯 MVP: Identified core notification pipeline",
            "[01:15] 🔴 TDD: Writing failing notification tests...",
            "[01:45] ✅ TDD: All tests passing with implementation",
            "[02:00] 🎯 QUALITY: All production gates passed",
            "[02:15] ✅ COMPLETE: Feature ready for deployment"
        ]
    },
    "docs.md": {
        "version": "2.4.1", 
        "workflow_steps": [
            "│ 1. Gateway     │ → Block external docs",
            "│    Enforcement │",
            "│ 2. Type        │ → Documentation category",
            "│    Analysis    │",
            "│ 3. Content     │ → Generate or search",
            "│    Generation  │",
            "│ 4. Standards   │ → Apply formatting rules",
            "│    Application │",
            "│ 5. Index       │ → Update documentation index",
            "│    Update      │"
        ],
        "context_budget": "~12,000",
        "budget_breakdown": [
            "- Gateway enforcement: 1,000",
            "- Type analysis: 1,500", 
            "- Content generation: 6,000",
            "- Standards application: 2,000",
            "- Index updates: 1,500"
        ],
        "example_trace": [
            "[00:00] ▶️ START: /docs \"API documentation\"",
            "[00:15] 🚫 GATEWAY: External doc creation blocked",
            "[00:30] 🔍 ANALYSIS: API documentation type identified",
            "[00:45] 📝 GENERATION: Creating comprehensive API docs",
            "[01:30] 📏 STANDARDS: Applying framework formatting",
            "[01:45] 📚 INDEX: Updating documentation index",
            "[02:00] ✅ COMPLETE: API documentation published"
        ]
    },
    "protocol.md": {
        "version": "2.4.1",
        "workflow_steps": [
            "│ 1. Session     │ → Compliance tracking",
            "│    Creation    │", 
            "│ 2. Requirements│ → TDD validation",
            "│    Validation  │",
            "│ 3. TDD         │ → Strictest enforcement",
            "│    Enforcement │",
            "│ 4. Security    │ → Threat modeling",
            "│    Analysis    │",
            "│ 5. Performance │ → Benchmark validation",
            "│    Validation  │",
            "│ 6. Quality     │ → Production gates",
            "│    Gates       │",
            "│ 7. Compliance  │ → Audit documentation",
            "│    Docs        │"
        ],
        "context_budget": "~20,000",
        "budget_breakdown": [
            "- Session & compliance: 2,000",
            "- Requirements validation: 2,500",
            "- TDD enforcement: 6,000",
            "- Security analysis: 3,000",
            "- Performance validation: 2,500",
            "- Quality gates: 2,000", 
            "- Compliance docs: 2,000"
        ],
        "example_trace": [
            "[00:00] ▶️ START: /protocol \"Payment processing\"",
            "[00:30] 🎯 SESSION: Compliance tracking #159 created",
            "[00:45] ✅ REQUIREMENTS: All validated as testable",
            "[01:00] 🔴 TDD: Writing comprehensive failing tests...",
            "[01:30] ✅ TDD: Implementation with 98% coverage",
            "[01:45] 🔒 SECURITY: Threat model completed, all clear",
            "[02:00] ⚡ PERFORMANCE: <150ms p95 achieved",
            "[02:15] 🎯 QUALITY: All production gates passed", 
            "[02:30] 📋 COMPLIANCE: Audit trail documented",
            "[02:45] ✅ COMPLETE: Production-ready with compliance"
        ]
    }
}

def update_command_version(content: str, version: str) -> str:
    """Update the version in the version table."""
    pattern = r'\| version \| last_updated \| status \|\n\|---------|--------------|--------\|\n\| [^|]+ \| [^|]+ \| [^|]+ \|'
    replacement = f'| version | last_updated | status |\n|---------|--------------|--------|\n| {version}   | 2025-07-08   | stable |'
    return re.sub(pattern, replacement, content)

def add_prompt_construction_sections(content: str, command_name: str) -> str:
    """Add prompt construction sections to a command."""
    config = COMMAND_ENHANCEMENTS[command_name]
    
    # Build the workflow assembly visual
    workflow_visual = "      WORKFLOW ASSEMBLY:\n      ┌─────────────────┐\n"
    for i, step in enumerate(config["workflow_steps"]):
        workflow_visual += f"      {step}\n"
        if i < len(config["workflow_steps"]) - 1:
            workflow_visual += "      └────────┬────────┘\n               ↓\n      ┌─────────────────┐\n"
        else:
            workflow_visual += "      └─────────────────┘"
    
    # Build context budget breakdown
    budget_breakdown = "\n".join([f"      {item}" for item in config["budget_breakdown"]])
    
    # Build execution trace  
    trace_lines = "\n".join([f"      {line}" for line in config["example_trace"]])
    
    # Create the prompt construction sections
    prompt_construction = f'''
  <prompt_construction>
    <assembly_preview>
{workflow_visual}
    </assembly_preview>

    <context_budget>
      Estimated tokens: {config["context_budget"]}
{budget_breakdown}
    </context_budget>
  </prompt_construction>

  <runtime_visualization>
    <execution_trace>
{trace_lines}
    </execution_trace>
  </runtime_visualization>

  <claude_4_interpretation>
    <parsing_behavior>
      1. Reads checkpoint structure sequentially
      2. Executes critical_thinking questions internally
      3. Formats output according to output_format specifications
      4. Validates against enforcement rules before proceeding
      5. Applies parallel execution optimization where possible
    </parsing_behavior>

    <decision_points>
      - Checkpoint failures trigger enforcement actions
      - Module selection based on contextual conditions
      - Parallel execution for independent operations
      - Quality gate validation at completion boundaries
      - Error recovery through graceful degradation paths
    </decision_points>
  </claude_4_interpretation>

</command>
```'''
    
    # Find the end of the command and insert the new sections
    end_pattern = r'</command>\s*```\s*$'
    if re.search(end_pattern, content, re.MULTILINE):
        return re.sub(end_pattern, prompt_construction, content, flags=re.MULTILINE)
    else:
        # If pattern not found, append before the last ```
        return content.replace('```\n', prompt_construction + '\n')

def enhance_command_file(file_path: Path) -> bool:
    """Enhance a single command file."""
    try:
        command_name = file_path.name
        if command_name not in COMMAND_ENHANCEMENTS:
            print(f"No enhancement config for {command_name}")
            return False
            
        content = file_path.read_text()
        
        # Update version
        content = update_command_version(content, COMMAND_ENHANCEMENTS[command_name]["version"])
        
        # Add prompt construction sections
        content = add_prompt_construction_sections(content, command_name)
        
        # Write back the updated content
        file_path.write_text(content)
        print(f"✅ Enhanced {command_name}")
        return True
        
    except Exception as e:
        print(f"❌ Error enhancing {file_path.name}: {e}")
        return False

def main():
    """Main enhancement process."""
    print("🚀 Starting command enhancement process...")
    
    if not BASE_PATH.exists():
        print(f"❌ Commands directory not found: {BASE_PATH}")
        return
    
    enhanced_count = 0
    total_commands = 0
    
    for command_file in BASE_PATH.glob("*.md"):
        total_commands += 1
        if command_file.name == "task.md":
            print(f"⏭️ Skipping {command_file.name} (already enhanced)")
            enhanced_count += 1
            continue
            
        if enhance_command_file(command_file):
            enhanced_count += 1
    
    print(f"\n📊 Enhancement complete: {enhanced_count}/{total_commands} commands enhanced")
    
    if enhanced_count == total_commands:
        print("✅ All commands successfully enhanced with prompt construction sections!")
    else:
        print("⚠️ Some commands may need manual review")

if __name__ == "__main__":
    main()