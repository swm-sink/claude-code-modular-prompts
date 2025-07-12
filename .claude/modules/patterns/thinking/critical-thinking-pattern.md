| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-09   | stable |

# Critical Thinking Pattern Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<module name="critical_thinking_pattern" category="patterns">
  
  <purpose>
    Structured analysis and decision-making framework for complex problems, providing systematic approach to challenge assumptions, evaluate evidence, and make well-reasoned decisions.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Complex problems requiring deep analysis</condition>
    <condition type="explicit">Multiple solution options need evaluation</condition>
    <condition type="explicit">Risk assessment is needed</condition>
    <condition type="explicit">Assumptions should be challenged</condition>
    <condition type="explicit">"think harder" or "ultrathink" is requested</condition>
  </trigger_conditions>
  
  <implementation>
    
    <phase name="assess_situation" order="1">
      <requirements>
        Problem scope must be clearly defined
        Context and constraints must be gathered
        Initial assumptions must be identified
      </requirements>
      <actions>
        Gather context and understand the problem scope
        Identify what exactly is the problem we're solving
        Document constraints and requirements that exist
        Surface initial assumptions being made
        Identify what information is missing
      </actions>
      <validation>
        Problem clearly defined with specific scope
        All constraints and requirements documented
        Initial assumptions explicitly stated
        Information gaps identified
      </validation>
    </phase>
    
    <phase name="challenge_assumptions" order="2">
      <requirements>
        Initial assumptions from phase 1 must be documented
        Open mindset to question existing beliefs
        Readiness to surface hidden complexities
      </requirements>
      <actions>
        Question existing beliefs and surface hidden complexities
        Challenge what if initial understanding is wrong
        Examine what assumptions could be invalid
        Explore alternative perspectives that exist
        Identify what could be missing from current view
      </actions>
      <validation>
        All initial assumptions explicitly challenged
        Alternative perspectives explored
        Hidden complexities surfaced
        Potential blind spots identified
      </validation>
    </phase>
    
    <phase name="generate_options" order="3">
      <requirements>
        Problem assessment completed
        Assumptions challenged
        Multiple solution approaches needed
      </requirements>
      <actions>
        Create multiple solution approaches
        Identify all possible approaches
        Evaluate pros and cons of each option
        Assess risks and benefits
        Consider what experts in this domain would do
      </actions>
      <validation>
        Multiple viable options generated
        Pros and cons documented for each
        Risks and benefits assessed
        Expert perspectives considered
      </validation>
    </phase>
    
    <phase name="evaluate_evidence" order="4">
      <requirements>
        Multiple options from phase 3 must be available
        Evidence quality assessment capability
        Reliability evaluation framework
      </requirements>
      <actions>
        Assess the quality and reliability of information
        Identify evidence that supports each option
        Evaluate how reliable this information is
        Find evidence that contradicts current thinking
        Determine what would change the mind
      </actions>
      <validation>
        Evidence quality assessed for each option
        Information reliability evaluated
        Contradictory evidence identified
        Decision criteria clearly defined
      </validation>
    </phase>
    
    <phase name="map_consequences" order="5">
      <requirements>
        Options evaluated with evidence
        Consequence mapping framework
        Chain of effects analysis capability
      </requirements>
      <actions>
        Think through the chain of effects
        Map what happens next for each option
        Identify second and third order effects
        Analyze what could go wrong with each approach
        Define what success would look like
      </actions>
      <validation>
        Consequences mapped for each option
        Second and third order effects identified
        Failure scenarios analyzed
        Success criteria defined
      </validation>
    </phase>
    
    <phase name="make_decision" order="6">
      <requirements>
        Complete analysis from phases 1-5
        Clear decision criteria
        Backup plan capability
      </requirements>
      <actions>
        Choose the best approach based on analysis
        Identify which option best meets requirements
        Document key trade-offs
        Define how success will be measured
        Establish backup plan
      </actions>
      <validation>
        Decision based on systematic analysis
        Trade-offs clearly documented
        Success metrics defined
        Backup plan established
      </validation>
    </phase>
    
  </implementation>
  
  <integration_points>
    <provides_to>
      quality/tdd.md for test design decisions
      development/research-analysis.md for information gathering
      quality/quality-validation.md for comprehensive testing
      patterns/error-recovery.md for failure planning
    </provides_to>
    <depends_on>
      quality/critical-thinking.md for enforcement framework
    </depends_on>
  </integration_points>
  
  <pattern_usage>
    <uses_pattern from="patterns/pattern-library.md">systematic_analysis</uses_pattern>
    <uses_pattern from="patterns/pattern-library.md">three_x_rule</uses_pattern>
    <implementation_notes>
      Provides structured thinking framework for complex decisions
      Integrates with TDD cycle for test-driven development
      Supports research-first methodology
      Enables quality validation through systematic analysis
    </implementation_notes>
  </pattern_usage>
  
  <configuration>
    <setting name="minimum_thinking_time" default="30_seconds" required="true">
      Minimum time required for critical thinking analysis
    </setting>
    <setting name="evidence_quality_threshold" default="high" required="false">
      Required quality level for evidence evaluation
    </setting>
    <setting name="consequence_depth" default="3_levels" required="false">
      Number of consequence levels to analyze
    </setting>
  </configuration>
  
  <error_handling>
    <error code="CTP001" severity="critical">
      Insufficient analysis time - enforce minimum thinking period
    </error>
    <error code="CTP002" severity="warning">
      Assumptions not challenged - require explicit assumption review
    </error>
    <error code="CTP003" severity="warning">
      Evidence quality low - require additional validation
    </error>
  </error_handling>
  
  <examples>
    <example name="architecture_decision">
      <description>Architecture decisions requiring trade-off analysis</description>
      <code>
        Apply critical thinking pattern to evaluate microservices vs monolith
        Phase 1: Assess current system constraints and requirements
        Phase 2: Challenge assumptions about scalability needs
        Phase 3: Generate multiple architectural options
        Phase 4: Evaluate evidence for each approach
        Phase 5: Map consequences of each choice
        Phase 6: Make decision based on systematic analysis
      </code>
      <expected_output>
        Well-reasoned architectural decision with documented trade-offs
        Clear rationale for choice with evidence support
        Risk mitigation strategies and success metrics
      </expected_output>
    </example>
    
    <example name="bug_investigation">
      <description>Complex bug investigation needing systematic approach</description>
      <code>
        Apply critical thinking pattern to complex production issue
        Phase 1: Assess symptoms and system context
        Phase 2: Challenge assumptions about root cause
        Phase 3: Generate multiple hypothesis options
        Phase 4: Evaluate evidence for each hypothesis
        Phase 5: Map consequences of each potential fix
        Phase 6: Choose optimal debugging approach
      </code>
      <expected_output>
        Systematic bug investigation with clear hypothesis
        Evidence-based root cause analysis
        Risk-assessed solution with backup plans
      </expected_output>
    </example>
  </examples>
  
</module>
```

## Anti-patterns to Avoid
- Rushing to first solution without analysis
- Ignoring evidence that contradicts preference  
- Failing to consider alternative approaches
- Not mapping consequences of decisions

## Validation Checklist
- [ ] All key questions have been addressed
- [ ] Multiple perspectives have been considered
- [ ] Assumptions have been explicitly challenged
- [ ] Evidence has been evaluated for quality
- [ ] Consequences have been mapped through multiple levels
- [ ] Decision is well-reasoned and justified