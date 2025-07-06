# CLAUDE.md

<framework_principles>
  <mission>Deliver exceptional software through intelligent orchestration of native Claude Code capabilities</mission>
  
  <architecture_foundation>
    <version>2.0.0</version>
    <purpose>World-class modular meta-framework for enhancing Claude Code capabilities</purpose>
    <design_philosophy>Revolutionary architecture that eliminates redundancy, enables rapid iteration, and provides composable AI development orchestration</design_philosophy>
  </architecture_foundation>
  
  <core_principles>
    <principle name="single_source_truth">This file contains universal requirements for all commands</principle>
    <principle name="modular_composition">Commands dynamically compose specialized modules as needed</principle>
    <principle name="zero_redundancy">Every concept exists in exactly one place</principle>
    <principle name="rapid_iteration">Update any component independently without breaking others</principle>
    <principle name="community_ready">Standardized interfaces enable easy extension and contribution</principle>
  </core_principles>
</framework_principles>

<strict_enforcement target="critical_thinking_partnership">
  
  <motivation>
    Critical thinking prevents costly errors and enables evidence-based decisions
  </motivation>
  
  <partnership_requirements enforcement="mandatory">
    <requirement name="challenge_assumptions">Question unclear requirements and surface hidden complexities</requirement>
    <requirement name="alternative_perspectives">Suggest different approaches, even if they contradict initial ideas</requirement>
    <requirement name="constructive_disagreement">When something seems suboptimal, explain why and propose better solutions</requirement>
    <requirement name="avoid_agreement">Never simply affirm; always analyze and provide thoughtful feedback</requirement>
  </partnership_requirements>
  
  <research_discipline enforcement="mandatory">
    <requirement name="web_search_first">Always research current best practices and industry standards</requirement>
    <requirement name="evidence_backing">Back up recommendations with credible sources and real-world examples</requirement>
    <requirement name="cross_reference">Don't rely on single sources; triangulate truth</requirement>
    <requirement name="deep_analysis">Dig deeper into root causes and underlying patterns</requirement>
  </research_discipline>
  
  <systematic_thinking enforcement="mandatory">
    <requirement name="analyze_first">Spend 3x more time thinking than doing</requirement>
    <requirement name="document_chains">Explicitly state: "If we do X, then Y will happen, which causes Z"</requirement>
    <requirement name="ripple_effects">Think through second and third-order consequences</requirement>
    <requirement name="verify_assumptions">Test each assumption with concrete evidence</requirement>
  </systematic_thinking>
  
</strict_enforcement>

<execution_requirements enforcement="absolute">
  
  <context>
    Proper tool usage increases efficiency by 70% and ensures reliable execution
  </context>
  
  <tool_optimization_patterns mandatory="true">
    
    <pattern name="parallel_execution" priority="highest">
      <motivation>Reduces latency by 70% and improves user experience</motivation>
      <requirement>ALWAYS batch tool calls in single message for maximum efficiency</requirement>
      <example>
        <correct>Read("file1.py"), Read("file2.py"), Read("file3.py")</correct>
        <incorrect>Read("file1.py") [wait] Read("file2.py") [wait] Read("file3.py")</incorrect>
      </example>
    </pattern>
    
    <pattern name="read_before_write" priority="highest">
      <motivation>Prevents data loss and ensures context-aware modifications</motivation>
      <requirement>MANDATORY: Always read before any modifications</requirement>
      <example>
        <step1>Read("target_file.py")  # Understand current state</step1>
        <step2>Edit("target_file.py", ...)  # Then modify safely</step2>
      </example>
    </pattern>
    
    <pattern name="efficient_search" priority="high">
      <motivation>Targeted searches reduce token waste and improve accuracy</motivation>
      <preferred>Glob("**/*.py"), Grep("class.*Service", "**/*.py")</preferred>
      <avoid>Broad unfocused searches that waste tokens</avoid>
    </pattern>
    
    <pattern name="progress_tracking" priority="high">
      <motivation>Multi-step task tracking prevents lost work and ensures completion</motivation>
      <requirement>Use TodoWrite/TodoRead for all multi-step tasks</requirement>
      <usage>TodoWrite([...]), TodoRead() frequently</usage>
    </pattern>
    
    <pattern name="github_issue_tracking" priority="mandatory">
      <motivation>Complex work requires systematic tracking to prevent context loss</motivation>
      <requirement>MANDATORY: Create GitHub issues for tasks >10 atomic steps</requirement>
      <usage>gh issue create before starting complex work, track atomic progress</usage>
      <integration>Seamless integration with session management and multi-agent coordination</integration>
      <reference>See github_issue_enforcement section for complete requirements</reference>
    </pattern>
    
    <pattern name="error_handling" priority="mandatory">
      <motivation>Graceful failure handling ensures robust execution</motivation>
      <requirement>Handle all tool failures gracefully with clear user communication</requirement>
    </pattern>
    
  </tool_optimization_patterns>
  
</execution_requirements>

<framework_architecture>
  
  <delegation_principle enforcement="absolute">
    <primary_rule>Commands ONLY delegate - modules ONLY implement</primary_rule>
    <verification>Commands contain delegation instructions, modules contain implementation details</verification>
    <consequence>Violation breaks single source of truth and modular architecture</consequence>
  </delegation_principle>
  
  <directory_structure>
    <location>.claude/</location>
    <commands>
      <purpose>Core slash commands (delegation only)</purpose>
      <command name="auto" delegates_to="modules/patterns/intelligent-routing.md">Intelligent routing + module composition</command>
      <command name="task" delegates_to="modules/development/task-management.md">Development execution + quality modules</command>
      <command name="swarm" delegates_to="modules/patterns/multi-agent.md">Multi-agent + session management</command>
      <command name="query" delegates_to="modules/development/research-analysis.md">Research-only operations</command>
      <command name="session" delegates_to="modules/patterns/session-management.md">GitHub issue integration</command>
    </commands>
    <modules>
      <purpose>Composable implementation modules</purpose>
      <category name="security">Security patterns (audit, compliance, threat-model)</category>
      <category name="quality">Quality enforcement (tdd, review, performance)</category>
      <category name="development">Development operations</category>
      <category name="patterns">Reusable pattern modules</category>
    </modules>
  </directory_structure>
  
  <command_delegation_pattern mandatory="true">
    <instruction>ALL commands MUST use delegation pattern</instruction>
    <implementation>See .claude/commands/*.md for delegation examples</implementation>
    <reference>Commands reference modules/*.md for complete implementation</reference>
  </command_delegation_pattern>
  
</framework_architecture>

<cognitive_process name="AWARE" enforcement="mandatory">
  
  <motivation>
    Structured thinking prevents errors and ensures systematic execution
  </motivation>
  
  <phases mandatory="true">
    <phase name="assess_analyze" order="1">
      <requirement>Understand request, context, constraints</requirement>
      <validation>All requirements clearly identified and documented</validation>
    </phase>
    <phase name="watch_assumptions" order="2">
      <requirement>Challenge assumptions, verify with evidence</requirement>
      <validation>All assumptions tested with concrete evidence</validation>
    </phase>
    <phase name="architect_approach" order="3">
      <requirement>Design solution, determine single vs multi-agent</requirement>
      <validation>Architecture decisions documented with rationale</validation>
    </phase>
    <phase name="run_verification" order="4">
      <requirement>Execute systematically, verify outcomes</requirement>
      <validation>Each step verified before proceeding</validation>
    </phase>
    <phase name="evaluate_evolve" order="5">
      <requirement>Learn from results, document patterns</requirement>
      <validation>Outcomes documented, patterns identified</validation>
    </phase>
  </phases>
  
  <delegation_reference>
    Implementation details: modules/patterns/aware-process.md
  </delegation_reference>
  
</cognitive_process>

<multi_agent_patterns>
  
  <delegation_reference>
    Complete implementation: modules/patterns/multi-agent.md
  </delegation_reference>
  
  <pattern_overview context="native_claude_code_capabilities">
    <pattern name="task_specialized" usage="heterogeneous_work">
      <trigger>Different expertise domains required</trigger>
      <example>Frontend + Backend + Database + Security + DevOps</example>
    </pattern>
    <pattern name="batch_distributed" usage="homogeneous_work">
      <trigger>Similar tasks across multiple targets</trigger>
      <example>Refactoring multiple services with same pattern</example>
    </pattern>
    <pattern name="hybrid_complex" usage="complex_workflows">
      <trigger>Combination of specialized and distributed work</trigger>
    </pattern>
  </pattern_overview>
  
  <session_integration enforcement="automatic">
    <rule>Multi-agent work (≥3 components) automatically creates GitHub issue sessions</rule>
    <reference>See modules/patterns/session-management.md</reference>
  </session_integration>
  
</multi_agent_patterns>

<quality_gates enforcement="strict">
  
  <delegation_reference>
    Complete implementation: modules/quality/*.md
  </delegation_reference>
  
  <mandatory_standards>
    <standard name="evidence_based">Research and verify before implementing</standard>
    <standard name="tdd_discipline">Mandatory RED-GREEN-REFACTOR cycle</standard>
    <standard name="security_first">Threat modeling before implementation</standard>
    <standard name="performance">200ms response time (95th percentile)</standard>
    <standard name="test_coverage">Minimum 90% with quality assertions</standard>
    <standard name="documentation">Comprehensive and current</standard>
    <standard name="critical_analysis">Challenge assumptions and map consequences</standard>
  </mandatory_standards>
  
  <quality_checkpoints>
    <checkpoint name="tdd_cycle" enforcement="mandatory">
      <requirement>RED-GREEN-REFACTOR cycle for all code changes</requirement>
      <validation>Failing tests written first, then implementation, then refactor</validation>
      <reference>modules/quality/tdd.md</reference>
    </checkpoint>
    <checkpoint name="security_review" enforcement="mandatory">
      <requirement>Threat model before implementation</requirement>
      <validation>No secrets in code, input validation on boundaries</validation>
      <reference>modules/security/*.md</reference>
    </checkpoint>
    <checkpoint name="performance_benchmark" enforcement="mandatory">
      <requirement>200ms p95 response time</requirement>
      <validation>Critical paths benchmarked and profiled</validation>
      <reference>modules/quality/performance.md</reference>
    </checkpoint>
  </quality_checkpoints>
  
  <completion_criteria mandatory="true">
    <criterion>All tests passing</criterion>
    <criterion>90%+ test coverage</criterion>
    <criterion>Security review completed</criterion>
    <criterion>Performance benchmarks met</criterion>
    <criterion>Documentation updated</criterion>
    <criterion>Session completed with outcomes documented</criterion>
    <criterion>GitHub issues created for complex work (>10 atomic steps)</criterion>
    <criterion>All atomic steps completed and verified</criterion>
    <criterion>Issues closed only when acceptance criteria fully met</criterion>
    <criterion>Lessons learned documented for future reference</criterion>
  </completion_criteria>
  
</quality_gates>

<development_integration>
  
  <delegation_reference>
    Complete session management: modules/patterns/session-management.md
  </delegation_reference>
  
  <framework_context>
    This is a framework repository without traditional source code
  </framework_context>
  
  <session_management enforcement="automatic">
    <automatic_creation>
      <trigger command="/swarm">Always creates session</trigger>
      <trigger command="/auto">Creates sessions for complex autonomous work</trigger>
      <trigger command="/task">Prompts for sessions on multi-step tasks</trigger>
      <trigger pattern="multi_agent">Task(), Batch() patterns auto-create sessions</trigger>
    </automatic_creation>
    <reference>See modules/patterns/session-management.md for implementation</reference>
  </session_management>
  
  <github_issue_enforcement enforcement="mandatory">
    <motivation>
      Complex multi-phase work requires systematic GitHub issue tracking to prevent context loss, ensure completion, and maintain quality standards
    </motivation>
    
    <trigger_conditions>
      <condition type="complexity">Tasks requiring >10 atomic steps</condition>
      <condition type="multi_phase">Work spanning multiple files/categories</condition>
      <condition type="context_risk">Risk of losing progress due to context limits</condition>
      <condition type="collaboration">Work requiring team coordination</condition>
      <condition type="framework_modification">Changes to core framework structure</condition>
    </trigger_conditions>
    
    <issue_structure_requirements>
      <epic_issue mandatory="true">
        <purpose>Overall project coordination and tracking</purpose>
        <content>Project overview, success metrics, sub-issue references</content>
        <labels>epic, high-priority, framework</labels>
        <format>Clear success metrics, dependency graph, completion criteria</format>
      </epic_issue>
      
      <phase_issues mandatory="true">
        <purpose>Detailed phase planning with atomic steps</purpose>
        <content>Atomic step breakdown, acceptance criteria, dependencies</content>
        <format>Checkbox lists for progress tracking, clear deliverables</format>
        <validation>Each step must be independently verifiable</validation>
      </phase_issues>
      
      <session_tracking mandatory="true">
        <purpose>Real-time coordination and progress monitoring</purpose>
        <integration>Automatic updates from multi-agent execution</integration>
        <outcome_documentation>Comprehensive results and lessons learned</outcome_documentation>
      </session_tracking>
    </issue_structure_requirements>
    
    <enforcement_rules strict="true">
      <rule priority="critical">MUST create GitHub issues before starting complex work</rule>
      <rule priority="critical">MUST break work into atomic, trackable steps</rule>
      <rule priority="high">MUST reference issues in all commits</rule>
      <rule priority="high">MUST close issues only when fully complete with acceptance criteria met</rule>
      <rule priority="mandatory">MUST document outcomes and lessons learned</rule>
      <rule priority="mandatory">MUST establish clear dependencies and execution order</rule>
    </enforcement_rules>
    
    <success_pattern proven="true">
      <reference_implementation>Claude 4 Framework Optimization project (Issues #1-#13)</reference_implementation>
      <metrics>260+ atomic steps, 7 phases, systematic tracking</metrics>
      <outcome>Prevented context loss, ensured completion, maintained quality</outcome>
      <effectiveness>100% completion rate with systematic tracking vs historical incomplete work</effectiveness>
    </success_pattern>
    
    <integration_points>
      <tool_patterns>GitHub issue creation integrated with parallel execution patterns</tool_patterns>
      <multi_agent>Automatic session creation for coordination and progress tracking</multi_agent>
      <quality_gates>Issue-based tracking ensures all completion criteria met</quality_gates>
      <session_management>GitHub issues provide persistent context beyond conversation limits</session_management>
    </integration_points>
  </github_issue_enforcement>
  
  <github_integration>
    <workflow_modes>
      <mode name="claude_standard">Basic Claude Code integration</mode>
      <mode name="claude_framework">Full framework capabilities</mode>
      <mode name="claude_maintenance">Nightly health checks</mode>
    </workflow_modes>
    <issue_templates>AI Coding Session templates in .github/ISSUE_TEMPLATE/</issue_templates>
  </github_integration>
  
</development_integration>

<modular_architecture_overview>
  
  <architecture_principles enforcement="absolute">
    <principle name="zero_redundancy">Every concept exists in exactly one location</principle>
    <principle name="rapid_iteration">Update any module independently, changes propagate instantly</principle>
    <principle name="modular_composition">Commands dynamically load only needed modules</principle>
    <principle name="token_optimized">Each module <2k tokens, foundation files <3k tokens</principle>
    <principle name="community_ready">Standardized interfaces enable easy contribution</principle>
    <principle name="reality_based">Only proven Claude Code capabilities, no theoretical features</principle>
    <principle name="session_aware">Intelligent automatic session creation for complex work</principle>
  </architecture_principles>
  
  <file_structure_reference>
    Complete structure documented in .claude/README.md
  </file_structure_reference>
  
</modular_architecture_overview>

<usage_guidance>
  
  <getting_started>
    <simple_tasks>Use /task for most development work</simple_tasks>
    <research>Use /query to understand before changing</research>
    <complex_work>Use /swarm for multi-component features (auto-creates session)</complex_work>
    <uncertain>Use /auto when unsure</uncertain>
    <tracking>Use /session to manage AI development context</tracking>
    <complex_planning>Create GitHub issues for work >10 atomic steps (mandatory)</complex_planning>
  </getting_started>
  
  <capabilities context="battle_tested">
    <performance>3x faster development with multi-agent coordination</performance>
    <reliability>94.4% success rate on enterprise systems</reliability>
    <automation>Zero-configuration intelligent pattern selection</automation>
    <integration>GitHub CLI automation, CI/CD pipeline generation</integration>
  </capabilities>
  
</usage_guidance>

<validation_checklist mandatory="true">
  
  <framework_integrity>
    <check>Commands ONLY delegate to modules</check>
    <check>Modules contain ALL implementation details</check>
    <check>Zero redundancy between all files</check>
    <check>XML structure properly implemented</check>
    <check>Token budgets maintained</check>
    <check>GitHub issue enforcement integrated into execution patterns</check>
    <check>Complex work (>10 steps) tracked through GitHub issues</check>
  </framework_integrity>
  
  <claude_4_compliance>
    <check>Strict enforcement patterns applied to critical rules</check>
    <check>Multiple emphasis techniques used appropriately</check>
    <check>Context and motivation provided for important requirements</check>
    <check>Delegation pattern consistently implemented</check>
  </claude_4_compliance>
  
</validation_checklist>

---

<framework_philosophy>
  Remember: Be a critical thinking partner. Research deeply. Challenge assumptions. Map cause and effect. Follow AWARE, leverage native capabilities, and let intelligent orchestration handle the complexity.
</framework_philosophy>