| version | last_updated | status |
|---------|--------------|--------|
| 1.0.0   | 2025-07-08   | stable |

# Duplication Prevention Module

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

**PURPOSE**: Enforce DRY (Don't Repeat Yourself) principles through mandatory duplication scanning

────────────────────────────────────────────────────────────────────────────────

```xml
<module purpose="Prevent duplication through mandatory scanning and verification">
  
  <duplication_scan_requirements enforcement="MANDATORY">
    <pre_creation_scan>
      <step>1. PAUSE: Before creating ANY file, scan entire codebase</step>
      <step>2. SEARCH: Look for similar functionality by multiple methods</step>
      <step>3. ANALYZE: Compare existing code with intended implementation</step>
      <step>4. DECIDE: Enhance existing vs create new (prefer enhance)</step>
      <step>5. DOCUMENT: Record duplication analysis in decision registry</step>
    </pre_creation_scan>
    
    <scan_methods>
      <method name="filename_similarity">
        <action>Search for files with similar names or patterns</action>
        <tools>Glob with wildcards, case-insensitive matching</tools>
      </method>
      
      <method name="functionality_search">
        <action>Search for code implementing similar features</action>
        <tools>Grep for function names, class names, API endpoints</tools>
      </method>
      
      <method name="pattern_detection">
        <action>Identify similar code structures and patterns</action>
        <tools>AST analysis, pattern matching, similarity scoring</tools>
      </method>
      
      <method name="conceptual_overlap">
        <action>Find conceptually similar implementations</action>
        <tools>Documentation search, comment analysis, naming patterns</tools>
      </method>
    </scan_methods>
  </duplication_scan_requirements>
  
  <enforcement_checkpoints>
    <checkpoint name="DUPLICATION_SCAN">
      <template>
        ┌─────────────────────────────────────────────────────────────┐
        │ CHECKPOINT: DUPLICATION PREVENTION                          │
        │ Status: SCANNING                                            │
        │ Time: {timestamp}                                           │
        └─────────────────────────────────────────────────────────────┘
        
        🔍 Scanning for existing implementations...
        
        ✓ Scan Results:
          • Files with similar names: {count} found
            - {file_path_1}
            - {file_path_2}
          
          • Similar functionality detected:
            - {existing_function} in {file_path}
            - {similar_pattern} in {file_path}
          
          • Conceptual overlaps:
            - {concept_1}: {location}
            - {concept_2}: {location}
        
        📊 Duplication Analysis:
          • Similarity Score: {percentage}%
          • Recommendation: {ENHANCE_EXISTING|CREATE_NEW}
          • Justification: {detailed_reasoning}
        
        ✅ Decision: {decision_made}
      </template>
    </checkpoint>
  </enforcement_checkpoints>
  
  <duplication_decision_framework>
    <criteria_for_new_file>
      <criterion>Functionality is fundamentally different (>80% unique)</criterion>
      <criterion>Separation of concerns requires isolation</criterion>
      <criterion>Performance requirements demand specialized implementation</criterion>
      <criterion>Security boundaries prevent code sharing</criterion>
    </criteria_for_new_file>
    
    <criteria_for_enhancement>
      <criterion>Existing code can be extended with <20% modification</criterion>
      <criterion>Similar patterns or structures already exist</criterion>
      <criterion>Shared functionality can be extracted and reused</criterion>
      <criterion>Configuration can achieve desired behavior</criterion>
    </criteria_for_enhancement>
    
    <decision_documentation enforcement="REQUIRED">
      <format>
        Decision ID: DUP-{timestamp}
        Type: {NEW_FILE|ENHANCEMENT|REFACTOR}
        Existing Code: {paths_to_similar_code}
        Similarity Analysis: {detailed_comparison}
        Decision Rationale: {why_this_approach}
        Alternatives Considered: {other_options}
      </format>
    </decision_documentation>
  </duplication_decision_framework>
  
  <enhancement_patterns>
    <pattern name="extend_existing">
      <approach>Add new methods/functions to existing modules</approach>
      <when>Core functionality exists, needs additional features</when>
      <example>Adding new validation rules to existing validator</example>
    </pattern>
    
    <pattern name="extract_shared">
      <approach>Extract common functionality to shared utilities</approach>
      <when>Multiple components need same functionality</when>
      <example>Creating shared authentication utilities</example>
    </pattern>
    
    <pattern name="parameterize_behavior">
      <approach>Make existing code configurable via parameters</approach>
      <when>Same logic, different configuration needed</when>
      <example>Adding options to existing data processors</example>
    </pattern>
    
    <pattern name="composition_over_creation">
      <approach>Compose existing components rather than recreate</approach>
      <when>Required functionality can be built from existing parts</when>
      <example>Building new features by combining existing modules</example>
    </pattern>
  </enhancement_patterns>
  
  <integration_requirements>
    <command_integration>
      <rule>ALL commands MUST include duplication scanning step</rule>
      <rule>File creation blocked until scan completes</rule>
      <rule>Enhancement preferred over creation by default</rule>
    </command_integration>
    
    <module_integration>
      <rule>Modules must check for existing implementations</rule>
      <rule>Cross-module duplication must be prevented</rule>
      <rule>Shared functionality extracted to common modules</rule>
    </module_integration>
    
    <critical_thinking_integration>
      <rule>30-second analysis includes duplication assessment</rule>
      <rule>Existing code review is mandatory first step</rule>
      <rule>Justification required for any new file creation</rule>
    </critical_thinking_integration>
  </integration_requirements>
  
  <enforcement_rules>
    <rule priority="CRITICAL">NO file creation without duplication scan</rule>
    <rule priority="CRITICAL">Scan results MUST be displayed to user</rule>
    <rule priority="CRITICAL">Enhancement is default unless justified</rule>
    <rule priority="HIGH">All decisions documented in registry</rule>
    <rule priority="HIGH">Similarity >40% requires explicit justification</rule>
    <rule priority="MEDIUM">Regular codebase scans for duplication creep</rule>
  </enforcement_rules>
  
  <metrics_tracking>
    <metric name="duplication_prevented">Files not created due to existing code</metric>
    <metric name="enhancements_made">Existing files enhanced vs new created</metric>
    <metric name="similarity_scores">Average similarity of new vs existing code</metric>
    <metric name="scan_compliance">Percentage of creations with proper scanning</metric>
  </metrics_tracking>
  
</module>
```

────────────────────────────────────────────────────────────────────────────────

## Duplication Prevention Workflow

### 1. Pre-Creation Phase
- Mandatory pause for duplication analysis
- Comprehensive codebase scanning
- Similarity scoring and assessment
- Enhancement vs creation decision

### 2. Decision Phase
- Document analysis results
- Justify approach selection
- Record in decision registry
- Get user confirmation if needed

### 3. Implementation Phase
- Follow enhancement patterns when possible
- Create new only when truly necessary
- Maintain references to similar code
- Update documentation

### 4. Verification Phase
- Confirm no unintended duplication
- Verify enhancement effectiveness
- Update metrics tracking
- Document lessons learned

────────────────────────────────────────────────────────────────────────────────

## Integration with Framework

This module integrates with:
- **Critical Thinking**: 30-second analysis includes duplication scan
- **Decision Registry**: All duplication decisions recorded
- **Quality Gates**: Duplication metrics part of quality score
- **All Commands**: Mandatory scanning before file operations

────────────────────────────────────────────────────────────────────────────────

*Preventing the disasters of duplication through mandatory verification.*