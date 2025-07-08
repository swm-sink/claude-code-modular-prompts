| version | last_updated | status |
|---------|--------------|--------|
| 2.6.0   | 2025-07-08   | stable |

# /auto - Intelligent routing with framework selection intelligence

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Intelligent routing with framework selection intelligence and research-first approach">
  
  <delegation target="modules/patterns/intelligent-routing.md">
    Analyze request → Select optimal framework → Calculate complexity → Research deeply → Route to optimal command with framework integration
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Parse request and identify task characteristics for framework selection</action>
      <critical_thinking>
        - What exactly is being requested and what type of work is this?
        - What domain does this fall into (technical/business/UX/research)?
        - What's the complexity level (simple/moderate/complex)?
        - What interaction style would be most effective (directive/collaborative/exploratory)?
        - Does this require code changes that need TDD enforcement?
      </critical_thinking>
      <output_format>REQUEST_ANALYSIS: [type] in [domain] with [complexity] requiring [interaction_style] and [tdd_requirement]</output_format>
      <validation>Request analyzed across all framework selection dimensions</validation>
      <enforcement>BLOCK if insufficient analysis for framework selection</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Select optimal framework using framework selector intelligence</action>
      <critical_thinking>
        - Based on complexity assessment, which frameworks are most suitable?
        - Does the domain (technical/business/UX/research) suggest specific frameworks?
        - What interaction style will yield the best results?
        - Should I use a single framework or combination strategy?
        - How does framework choice affect routing decision?
      </critical_thinking>
      <output_format>FRAMEWORK_SELECTION: Primary=[framework] Secondary=[alternatives] Strategy=[single/combination] Reasoning=[justification]</output_format>
      <validation>Framework selection justified and appropriate for task characteristics</validation>
      <enforcement>BLOCK if framework selection lacks clear justification</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Calculate complexity score with framework and TDD overhead</action>
      <critical_thinking>
        - Components×5 + integrations×4 + security×3 = base score
        - Add framework complexity overhead based on selected framework
        - Add +2 for each component requiring new tests
        - Add +3 for each integration requiring test coordination
        - Does complexity justify current framework choice and routing?
      </critical_thinking>
      <output_format>COMPLEXITY_SCORE: [number] ([base] + [framework_overhead] + [tdd_overhead]) = [total]</output_format>
      <validation>Score calculated with framework and TDD complexity factors</validation>
      <enforcement>VERIFY complexity includes framework optimization considerations</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Research codebase if needed for framework-aware routing</action>
      <critical_thinking>
        - What existing code/patterns would be affected?
        - Are there existing patterns that align with selected framework?
        - Do I need to understand current architecture before framework-optimized routing?
        - Would research-first help optimize framework selection and routing?
      </critical_thinking>
      <output_format>RESEARCH_STATUS: [NEEDED/COMPLETE] - [findings relevant to framework and routing]</output_format>
      <validation>Research completed with framework optimization insights</validation>
      <enforcement>BLOCK routing until framework-aware research confirms approach</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Route with framework integration and TDD enforcement</action>
      <critical_thinking>
        - ≤2: /query with LEAP/CLEAR frameworks (research-focused)
        - 3-9: /task with RISE/CARE frameworks (structured development)
        - 10-14: /feature with SOAR/CLEAR frameworks (comprehensive development)
        - ≥15: /swarm with TRACE/BRIDGE frameworks (multi-agent coordination)
        - Does routed command support selected framework effectively?
      </critical_thinking>
      <output_format>ROUTING_DECISION: Score [number] → /[command] with [framework] (TDD: [level], Framework: [optimization])</output_format>
      <validation>Route integrates framework selection with TDD enforcement</validation>
      <enforcement>VERIFY target command has framework integration capabilities</enforcement>
    </checkpoint>
    <checkpoint id="6" verify="true" enforcement="BLOCKING">
      <action>Execute framework-optimized routing with comprehensive delegation</action>
      <critical_thinking>
        - Does the target command support the selected framework?
        - Will framework integration optimize execution quality?
        - Are quality gates configured for framework validation?
        - Is execution path optimized for framework and TDD success?
      </critical_thinking>
      <output_format>EXECUTION_DELEGATION: Routing to /[command] with framework=[selected] TDD=[confirmed] optimization=[enabled]</output_format>
      <validation>Target command confirmed for framework and TDD capabilities</validation>
      <enforcement>BLOCK if target lacks framework integration or TDD enforcement</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <tdd_integration enforcement="MANDATORY">
    <routing_tdd_awareness>Route to TDD-enforcing commands for code changes, research commands for analysis</routing_tdd_awareness>
    <complexity_adjustment>Include TDD overhead in complexity scoring for accurate routing</complexity_adjustment>
    <command_verification>Verify target commands have proper TDD enforcement before routing</command_verification>
    <validation>Reference quality/tdd.md#routing_considerations for TDD-aware routing</validation>
    <blocking_conditions>
      <condition>Routing code changes to non-TDD-enforcing commands</condition>
      <condition>Complexity calculation ignores TDD testing requirements</condition>
      <condition>Target command lacks adequate TDD enforcement capabilities</condition>
      <condition>Research bypassed when TDD approach unclear</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before routing decision</module>
      <module>frameworks/framework-selector.md - Intelligent framework selection based on task characteristics</module>
      <module>patterns/intelligent-routing.md - Framework-aware request analysis and complexity scoring</module>
      <module>quality/tdd.md - TDD-aware routing considerations with framework integration</module>
      <module>patterns/pattern-library.md - Proven execution patterns</module>
    </core_stack>
    <contextual_modules>
      <conditional module="frameworks/rise.md" condition="structured_approach_needed"/>
      <conditional module="frameworks/trace.md" condition="precision_specification_needed"/>
      <conditional module="frameworks/care.md" condition="outcome_validation_needed"/>
      <conditional module="frameworks/advanced-frameworks.md" condition="specialized_framework_needed"/>
      <conditional module="development/research-analysis.md" condition="research_needed"/>
      <conditional module="quality/error-recovery.md" condition="routing_failures"/>
      <conditional module="patterns/session-management.md" condition="complex_routing"/>
    </contextual_modules>
  </module_execution>
  
  <depends_on>
    frameworks/framework-selector.md for intelligent framework selection
    patterns/intelligent-routing.md for framework-aware analysis and routing
    frameworks/rise.md, frameworks/trace.md, frameworks/care.md for foundational frameworks
    frameworks/advanced-frameworks.md for specialized framework ecosystem
    quality/tdd.md for TDD-aware routing with framework integration
    patterns/pattern-library.md for proven execution patterns
    quality/error-recovery.md for resilient execution
    All commands and modules for dynamic routing decisions
  </depends_on>
  
  <examples>
    /auto "Add user authentication"     → CRISP framework → Score ~12 → Routes to /task with technical precision
    /auto "Build e-commerce platform"   → BRIDGE framework → Score 40+ → Routes to /swarm with integration focus
    /auto "How does caching work?"      → LEAP framework → Score 1 → Routes to /query with learning approach
    /auto "Create API endpoints"        → RISE framework → Score ~10 → Routes to /feature with structured development
    /auto "Debug payment failures"     → SPARK framework → Score ~8 → Routes to /task with problem-solving focus
    /auto "Plan user experience redesign" → FOCUS framework → Score ~15 → Routes to /swarm with user-centered approach
  </examples>
  
  <rules>
    <rule>ALWAYS select optimal framework before routing</rule>
    <rule>ALWAYS calculate complexity score with framework considerations</rule>
    <rule>ALWAYS research first for informed framework-aware decisions</rule>
    <rule>NEVER skip framework selection or complexity scoring algorithm</rule>
    <rule>ALWAYS validate framework compatibility with target command</rule>
  </rules>
  
  <pattern_usage>
    • Uses intelligent_selection pattern for framework choice
    • Implements three_x_rule pattern for routing decisions
    • Applies consequence_mapping for impact analysis
    • Leverages parallel_execution for research operations
    • Uses explicit_validation pattern with framework verification
    • Integrates smart_memoization for cached framework and routing decisions
    • Applies error_recovery for resilient framework-aware routing
    • Uses framework_optimization patterns for enhanced execution
    
    See modules/frameworks/framework-selector.md for framework selection details
    See modules/patterns/pattern-library.md for pattern details
    See modules/patterns/intelligent-routing.md for full implementation
  </pattern_usage>
  

  <prompt_construction>
    <assembly_preview>
      FRAMEWORK-AWARE WORKFLOW ASSEMBLY:
      ┌─────────────────┐
      │ 1. Request     │ → Parse & categorize request with domain/complexity analysis
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 2. Framework   │ → Intelligent framework selection using task characteristics
      │   Selection    │
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 3. Complexity  │ → Calculate routing score with framework overhead
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 4. Research    │ → Framework-aware pattern investigation
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 5. Route       │ → Framework-optimized command selection
      └────────┬────────┘
               ↓
      ┌─────────────────┐
      │ 6. Execute     │ → Framework-integrated execution with TDD enforcement
      └─────────────────┘
    </assembly_preview>

    <context_budget>
      Estimated tokens: ~10,000
      - Request analysis: 1,500
      - Framework selection: 2,000
      - Complexity scoring: 1,000
      - Research phase: 4,000
      - Routing decision: 1,500
    </context_budget>
  </prompt_construction>

  <runtime_visualization>
    <execution_trace>
      [00:00] ▶️ START: /auto "Build payment system"
      [00:15] 🔍 ANALYSIS: Multi-component financial system detected (domain: technical, complexity: high)
      [00:25] 🎯 FRAMEWORK: Selected BRIDGE framework for complex integration approach
      [00:40] 📊 COMPLEXITY: Score 95/100 → High complexity (base: 85, framework: +5, TDD: +5)
      [00:55] 📚 RESEARCH: Framework-aware analysis of payment patterns and compliance
      [01:40] 🚀 ROUTING: Escalating to /swarm with BRIDGE framework integration
      [01:45] ✅ COMPLETE: Routed with framework optimization and TDD enforcement
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
```