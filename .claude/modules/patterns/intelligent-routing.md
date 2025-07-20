| version | last_updated | status |
|---------|--------------|--------|
| 3.1.0   | 2025-07-20   | hardened |

# Intelligent Routing Module

────────────────────────────────────────────────────────────────────────────────

Purpose: Intelligent command routing with complexity analysis and decision optimization for the /auto command
Dependencies: [@security/validation, @edge-cases/input-handling, @recovery/command-recovery]

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="intelligent_routing" category="patterns">
  
  <purpose>
    Intelligent command routing with complexity analysis, decision optimization, and comprehensive input validation for the /auto command.
  </purpose>
  
  <interface_contract>
    <inputs>
      <required>user_request (validated string), context_information (dict), available_commands (list)</required>
      <optional>user_preferences (dict), performance_history (dict), complexity_hints (dict)</optional>
      <validation>All inputs undergo security validation before processing</validation>
    </inputs>
    <outputs>
      <success>optimal_command_selection, confidence_score, routing_rationale, alternative_options</success>
      <failure>routing_failure (with recovery hints), analysis_errors (with context), fallback_suggestions</failure>
    </outputs>
  </interface_contract>
  
  <security_validation>
    <input_sanitization>
      User request sanitized for command injection patterns
      Path validation for any file references
      Size limits enforced (max 10KB input)
    </input_sanitization>
    <edge_case_handling>
      Empty/whitespace input detection
      Unicode normalization for international users
      Extremely large input rejection with helpful message
    </edge_case_handling>
  </security_validation>
  
  <execution_pattern>
    <claude_4_behavior>
      WHEN invoked:
      1. Parse user request and extract intent and complexity indicators
      2. Analyze task scope and determine optimal command routing
      3. Generate routing decision with confidence score and rationale
      4. Provide alternative routing options with trade-off analysis
      5. Route to selected command with full context preservation
    </claude_4_behavior>
  </execution_pattern>
  
  <trigger_conditions>
    <condition type="automatic">/auto command invoked with user request</condition>
    <condition type="explicit">Uncertain command selection requiring analysis</condition>
    <condition type="explicit">Complex routing requiring decision optimization</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="input_validation" order="1">
      <requirements>
        All inputs must be validated before processing
        Security patterns from SECURITY_VALIDATION.md must be applied
        Edge cases from EDGE_CASES.md must be handled
        MANDATORY: Fail fast with clear error messages
      </requirements>
      <actions>
        # Input validation following hardening patterns
        if not user_request or not user_request.strip():
            raise ValueError("Request cannot be empty. Please provide a clear description of what you need.")
        
        # Size validation
        if len(user_request) > 10000:
            raise ValueError(f"Request too large ({len(user_request)} chars). Please break into smaller, focused requests.")
        
        # Basic sanitization for dangerous patterns
        dangerous_patterns = ['rm -rf', 'sudo', 'eval(', 'exec(', '__import__']
        for pattern in dangerous_patterns:
            if pattern in user_request.lower():
                raise ValueError(f"Request contains potentially dangerous pattern: {pattern}")
        
        # Unicode normalization
        import unicodedata
        user_request = unicodedata.normalize('NFKC', user_request.strip())
      </actions>
      <validation>
        Input is non-empty and within size limits
        No dangerous patterns detected
        Unicode properly normalized
        Ready for safe processing
      </validation>
    </phase>
    
    <phase name="request_analysis" order="2">
      <requirements>
        Validated user request must be parsed and understood
        Context information must be extracted
        Intent recognition must be performed
        Complexity indicators must be identified
        MANDATORY: Use 30s critical thinking for complex routing decisions
      </requirements>
      <actions>
        Parse user request for keywords and action verbs
        Extract domain context and technical requirements
        Identify scope indicators (single file, multi-file, system-wide)
        Analyze complexity signals (research needed, multiple steps, dependencies)
        Classify request type (implementation, research, feature, debugging)
        MANDATORY: Apply critical thinking patterns for ambiguous requests
        ENFORCEMENT: Use quality gates for analysis depth
      </actions>
      <validation>
        Request intent clearly identified with confidence score
        Context and requirements properly extracted
        Complexity level assessed with supporting evidence
        Routing criteria established based on analysis
        VERIFICATION: Analysis documented with reasoning chain
      </validation>
      <blocking_conditions>
        <condition>Request intent unclear or ambiguous</condition>
        <condition>Insufficient context for routing decision</condition>
        <condition>Complexity analysis incomplete</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="complexity_scoring" order="2">
      <requirements>
        Request analysis from phase 1 must be completed
        Complexity scoring framework must be applied
        Command suitability must be evaluated
        BLOCKING GATE: Routing decisions require complexity justification
      </requirements>
      <actions>
        Score task complexity across multiple dimensions
        Evaluate file count and system scope requirements
        Assess research and analysis needs before implementation
        Calculate coordination and dependency complexity
        Map complexity to optimal command selection
        MANDATORY: Document complexity scoring rationale
        ENFORCEMENT: Use established complexity thresholds
      </actions>
      <validation>
        Complexity score calculated with clear methodology
        All complexity dimensions evaluated systematically
        Command mapping based on complexity thresholds
        Scoring rationale documented for transparency
        VERIFICATION: Complexity analysis supports routing decision
      </validation>
      <blocking_conditions>
        <condition>Complexity scoring incomplete or inconsistent</condition>
        <condition>Command mapping doesn't align with complexity</condition>
        <condition>Insufficient justification for routing decision</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="command_selection" order="3">
      <requirements>
        Complexity scoring from phase 2 must be available
        Command capabilities must be mapped to requirements
        Routing decision must be optimized for success
        BLOCKING GATE: Selection must pass capability validation
      </requirements>
      <actions>
        Map complexity score to optimal command selection
        Evaluate command capabilities against requirements
        Consider user preferences and working patterns
        Generate primary recommendation with confidence score
        Identify alternative options with trade-off analysis
        MANDATORY: Validate command capability alignment
        ENFORCEMENT: Use command-specific capability matrices
      </actions>
      <validation>
        Primary command selection optimized for requirements
        Command capabilities align with identified needs
        Confidence score reflects selection certainty
        Alternative options provide meaningful choices
        VERIFICATION: Selection logic documented and defensible
      </validation>
      <blocking_conditions>
        <condition>Command capabilities insufficient for requirements</condition>
        <condition>Selection logic inconsistent with analysis</condition>
        <condition>Confidence score doesn't reflect selection quality</condition>
      </blocking_conditions>
    </phase>
    
    <phase name="routing_execution" order="4">
      <requirements>
        Command selection from phase 3 must be finalized
        Routing context must be preserved for delegation
        Execution handoff must be seamless
        BLOCKING GATE: Context preservation is mandatory
      </requirements>
      <actions>
        Prepare routing context for selected command
        Preserve all analysis and decision rationale
        Execute routing to selected command with full context
        Monitor routing success and collect feedback
        Update routing patterns based on outcomes
        MANDATORY: Ensure complete context handoff
        ENFORCEMENT: Validate context preservation
      </actions>
      <validation>
        Routing executed to optimal command selection
        Context fully preserved in command delegation
        Routing feedback collected for learning
        Execution successful with no information loss
        VERIFICATION: Selected command receives complete context
      </validation>
      <blocking_conditions>
        <condition>Context preservation fails during routing</condition>
        <condition>Command execution fails due to routing issues</condition>
        <condition>Information loss during handoff</condition>
      </blocking_conditions>
    </phase>
    
  </implementation>
  
  <complexity_scoring_framework>
    <dimension name="scope_complexity">
      <single_file>Score: 1-2 → /task</single_file>
      <multi_file>Score: 3-5 → /feature</multi_file>
      <system_wide>Score: 6-8 → /swarm</system_wide>
      <enterprise>Score: 9-10 → /swarm with specialized agents</enterprise>
    </dimension>
    <dimension name="research_complexity">
      <clear_requirements>Score: 1-2 → Direct implementation</clear_requirements>
      <some_research>Score: 3-5 → /query then implementation</some_research>
      <deep_analysis>Score: 6-8 → /query with comprehensive analysis</deep_analysis>
      <domain_expertise>Score: 9-10 → /query with domain specialization</domain_expertise>
    </dimension>
    <dimension name="coordination_complexity">
      <single_developer>Score: 1-2 → /task</single_developer>
      <team_coordination>Score: 3-5 → /feature</team_coordination>
      <multi_team>Score: 6-8 → /swarm</multi_team>
      <cross_functional>Score: 9-10 → /swarm with specialized coordination</cross_functional>
    </dimension>
    <dimension name="implementation_complexity">
      <straightforward>Score: 1-3 → /task</straightforward>
      <moderate_complexity>Score: 4-6 → /feature</moderate_complexity>
      <high_complexity>Score: 7-9 → /swarm</high_complexity>
      <architectural>Score: 10 → /swarm with architectural agents</architectural>
    </dimension>
  </complexity_scoring_framework>
  
  <routing_decision_matrix>
    <command name="/task">
      <optimal_for>
        Single file modifications or small features
        Clear requirements with minimal research needed
        Straightforward implementation without complex dependencies
        Direct problem-solving with known solutions
      </optimal_for>
      <complexity_thresholds>
        Scope: 1-2 | Research: 1-3 | Coordination: 1-2 | Implementation: 1-3
      </complexity_thresholds>
      <success_indicators>
        Clear, actionable requirements
        Minimal external dependencies
        Single responsibility focus
        Predictable implementation path
      </success_indicators>
    </command>
    <command name="/query">
      <optimal_for>
        Research and understanding requirements
        Codebase analysis and pattern identification
        Problem investigation and root cause analysis
        Knowledge gathering before implementation
      </optimal_for>
      <complexity_thresholds>
        Scope: Any | Research: 4-10 | Coordination: Any | Implementation: Any
      </complexity_thresholds>
      <success_indicators>
        Unclear requirements needing clarification
        Unfamiliar codebase or domain
        Investigation needed before action
        Learning required for effective implementation
      </success_indicators>
    </command>
    <command name="/feature">
      <optimal_for>
        Multi-file features with clear specifications
        PRD-driven development with defined acceptance criteria
        Moderate complexity requiring structured approach
        Features requiring testing and validation
      </optimal_for>
      <complexity_thresholds>
        Scope: 3-5 | Research: 1-5 | Coordination: 3-5 | Implementation: 4-6
      </complexity_thresholds>
      <success_indicators>
        Clear feature specifications
        Multi-component implementation
        Testing and validation requirements
        Structured development approach needed
      </success_indicators>
    </command>
    <command name="/swarm">
      <optimal_for>
        Complex multi-system features
        High coordination requirements
        Architectural changes and refactoring
        Multi-agent specialized development
      </optimal_for>
      <complexity_thresholds>
        Scope: 6-10 | Research: Any | Coordination: 6-10 | Implementation: 7-10
      </complexity_thresholds>
      <success_indicators>
        System-wide impact and changes
        Multiple specialized skill requirements
        High coordination and integration needs
        Architectural or platform-level changes
      </success_indicators>
    </command>
  </routing_decision_matrix>
  
  <routing_confidence_calculation>
    <confidence_factors>
      <clear_requirements weight="0.3">How clear are the requirements?</clear_requirements>
      <complexity_alignment weight="0.25">How well does complexity align with command?</complexity_alignment>
      <historical_success weight="0.2">Historical success rate for similar routing</historical_success>
      <context_completeness weight="0.15">How complete is the context information?</context_completeness>
      <alternative_gap weight="0.1">How much better is primary vs alternatives?</alternative_gap>
    </confidence_factors>
    <confidence_thresholds>
      <high_confidence>85-100% - Strong routing recommendation</high_confidence>
      <medium_confidence>70-84% - Good routing with alternatives</medium_confidence>
      <low_confidence>50-69% - Uncertain routing, present options</low_confidence>
      <very_low_confidence>Below 50% - Request clarification</very_low_confidence>
    </confidence_thresholds>
  </routing_confidence_calculation>
  
  <alternative_analysis>
    <alternative_generation>
      Generate 2-3 alternative routing options
      Explain trade-offs and use cases for each
      Consider user preferences and working style
      Provide clear rationale for each alternative
    </alternative_generation>
    <trade_off_analysis>
      Compare speed vs. thoroughness
      Analyze simple vs. comprehensive approaches
      Consider immediate vs. planned execution
      Evaluate learning vs. doing trade-offs
    </trade_off_analysis>
  </alternative_analysis>
  
  <integration_points>
    <depends_on>
      ../../system/../../system/quality/critical-thinking.md for complex routing analysis
      patterns/tool-usage.md for parallel execution optimization
      development/research-analysis.md for research routing decisions
    </depends_on>
    <provides_to>
      /auto command for intelligent routing decisions
      All commands for optimal routing context
      patterns/session-management-pattern.md for routing history
    </provides_to>
  </integration_points>
  
  <quality_gates enforcement="strict">
    <gate name="analysis_completeness" requirement="Request analysis covers all complexity dimensions"/>
    <gate name="routing_justification" requirement="Routing decision supported by complexity analysis"/>
    <gate name="confidence_validation" requirement="Confidence score reflects analysis quality"/>
    <gate name="context_preservation" requirement="Complete context handoff to selected command"/>
  </quality_gates>
  
</module>
```

## Intelligent Routing Decision Examples

### Example 1: Simple Implementation
**Request**: "Add a validation function to check email format"
**Analysis**: Single file, clear requirements, straightforward implementation
**Complexity Score**: Scope: 1, Research: 1, Coordination: 1, Implementation: 2
**Routing**: /task (Confidence: 95%)
**Rationale**: Clear, single-file implementation with known solution patterns

### Example 2: Research-Heavy Task
**Request**: "Optimize the slow database queries in our reporting system"
**Analysis**: Requires investigation, performance analysis, multiple solutions
**Complexity Score**: Scope: 4, Research: 8, Coordination: 3, Implementation: 5
**Routing**: /query (Confidence: 88%)
**Rationale**: High research complexity requires understanding before implementation

### Example 3: Multi-System Feature
**Request**: "Implement user authentication with SSO, API keys, and role-based access"
**Analysis**: Multiple components, security requirements, integration needs
**Complexity Score**: Scope: 7, Research: 4, Coordination: 8, Implementation: 8
**Routing**: /swarm (Confidence: 91%)
**Rationale**: High coordination and implementation complexity requires specialized agents

### Example 4: Moderate Feature
**Request**: "Add a new dashboard page with charts and filters"
**Analysis**: Multi-file feature, clear requirements, moderate complexity
**Complexity Score**: Scope: 4, Research: 2, Coordination: 4, Implementation: 5
**Routing**: /feature (Confidence: 85%)
**Rationale**: Clear feature scope with structured development approach needed

## Error Recovery and Edge Cases

### Input Validation Failures
When input validation fails:
1. **Empty/Whitespace Input**: "Request cannot be empty. Please provide a clear description."
2. **Oversized Input**: "Request too large. Please break into smaller, focused requests."
3. **Dangerous Patterns**: "Potentially dangerous pattern detected. Please rephrase safely."

### Routing Ambiguity Recovery
When routing confidence is low (<0.6):
```
I'm not certain about the best approach. Here are the top options:
1. /task - If this is a simple, single-file change
2. /feature - If this involves multiple components  
3. /query - If you need to understand the codebase first

Could you clarify: [specific clarifying question based on ambiguity]
```

### Performance Optimization
- **Caching**: Recent routing decisions cached for 15 minutes
- **Early Exit**: High confidence (>0.9) routes skip additional analysis
- **Token Budget**: Maximum 4K tokens for routing analysis

## Anti-patterns to Avoid
- Routing without sufficient complexity analysis
- Ignoring research needs for unfamiliar domains
- Under-estimating coordination requirements
- Over-complicating simple implementations
- Insufficient context preservation in routing
- **NEW**: Skipping input validation for "simple" requests
- **NEW**: Not providing recovery options on failures

## Routing Validation Checklist
- [ ] Input validated and sanitized
- [ ] Request intent clearly identified and understood
- [ ] Complexity scored across all dimensions
- [ ] Command capabilities aligned with requirements
- [ ] Routing decision supported by analysis
- [ ] Confidence score reflects selection quality
- [ ] Alternative options provided with trade-offs
- [ ] Context fully preserved for command delegation
- [ ] Error recovery paths defined