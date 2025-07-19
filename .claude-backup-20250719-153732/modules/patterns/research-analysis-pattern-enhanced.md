| version | last_updated | status |
|---------|--------------|--------|
| 1.1.0   | 2025-07-19   | enhanced |

# Research & Analysis Pattern Module (Enhanced with Helpful Errors)

────────────────────────────────────────────────────────────────────────────────

**Enhancement**: This version implements helpful error messages for common research scenarios

────────────────────────────────────────────────────────────────────────────────

```xml
<module name="research_analysis_pattern_enhanced" category="patterns">
  
  <purpose>
    Systematic information gathering and understanding before implementation, now with helpful guidance that assists users through common research challenges and provides actionable solutions.
  </purpose>
  
  <trigger_conditions>
    <condition type="automatic">Starting work on unfamiliar codebase</condition>
    <condition type="explicit">Understanding requirements for new features</condition>
    <condition type="explicit">Investigating bugs or performance issues</condition>
    <condition type="explicit">Learning about existing patterns and conventions</condition>
    <condition type="explicit">Making architectural decisions</condition>
  </trigger_conditions>
  
  <pre_research_guidance>
    <check name="scope_validation">
      <validation>
        <!-- Check if research scope is too broad -->
        if query_too_broad():
          return Guidance(
            "💡 Your research query might be too broad",
            current_query=user_query,
            suggestions=[
              "Try focusing on a specific component or feature",
              f"For example: /query \"How does {specific_component} handle {specific_task}?\"",
              "Or break into multiple queries for different aspects"
            ],
            examples=[
              "❌ Broad: \"How does the system work?\"",
              "✅ Focused: \"How does user authentication flow work?\"",
              "✅ Focused: \"What database queries does the API make?\""
            ]
          )
        
        <!-- Guide on missing project context -->
        if no_project_context():
          return HelpfulError(
            "❌ No project context found",
            problem="Cannot analyze code without project information",
            solutions=[
              "Make sure you're in the project root directory",
              f"Current directory: {current_dir}",
              "Run: cd /path/to/your/project",
              "Or initialize context: /context-prime"
            ],
            why="Need to know project structure to search effectively"
          )
      </validation>
    </check>
  </pre_research_guidance>
  
  <implementation>
    
    <phase name="define_research_goals" order="1">
      <helpful_validations>
        <!-- Help users define better research goals -->
        if goals_unclear():
          return Guidance(
            "📋 Let's clarify your research goals",
            current_request=user_input,
            better_approaches=[
              {
                "instead_of": "Understand the codebase",
                "try": "Map the API endpoints and their data flow"
              },
              {
                "instead_of": "Find performance issues",
                "try": "Identify database queries taking >100ms"
              },
              {
                "instead_of": "Learn the architecture",
                "try": "Document component dependencies and interfaces"
              }
            ],
            template="I need to understand [specific_component] to [specific_goal]"
          )
      </helpful_validations>
      
      <actions>
        Clarify what you need to understand
        Identify specific information required
        Define what decisions this research will inform
        Determine required level of detail
        Document constraints and timeline
      </actions>
    </phase>
    
    <phase name="gather_information" order="2">
      <helpful_validations>
        <!-- Help with file discovery issues -->
        if cant_find_files():
          return HelpfulError(
            "❌ Cannot find relevant files",
            searched_for=search_terms,
            search_locations=searched_paths,
            solutions=[
              "Try different search terms:",
              f"  Instead of '{failed_term}' try '{suggested_term}'",
              "Use glob patterns:",
              f"  Glob: '**/*{pattern}*' to search all subdirectories",
              "Check common locations:",
              f"  {common_locations_for_file_type}"
            ],
            commands=[
              f"Find files: Glob('**/*{keyword}*')",
              f"Search content: Grep('{keyword}')",
              f"List directory: LS('{suggested_dir}')"
            ]
          )
        
        <!-- Guide on search strategy -->
        if inefficient_search():
          return Optimization(
            "🚀 Search more efficiently",
            current_approach="Sequential file reads",
            better_approach="Parallel search operations",
            example=[
              "// Instead of:",
              "Read(file1) then Read(file2) then Read(file3)",
              "",
              "// Do this (parallel):",
              "Read(file1), Read(file2), Read(file3)",
              "",
              "// Or batch search:",
              "Grep('pattern', path='src/', glob='*.js')"
            ],
            performance="3-10x faster with parallel operations"
          )
      </helpful_validations>
      
      <actions>
        Collect relevant data from multiple sources
        Read existing documentation and code
        Search for similar implementations
        Analyze patterns and conventions
        Review related issues and discussions
        Use parallel searches for efficiency
      </actions>
      
      <search_assistance>
        <!-- Help with common search scenarios -->
        <scenario name="finding_api_endpoints">
          if searching_for_api():
            return SearchGuidance(
              "🔍 Finding API endpoints",
              strategies=[
                "Search for route definitions: @app.route, router.get, etc.",
                "Look in common locations: routes/, api/, controllers/",
                "Check framework patterns: Express, FastAPI, Django URLs"
              ],
              commands=[
                "Grep('@app.route')",
                "Grep('router\\.(get|post|put|delete)')",
                "LS('./routes') or LS('./api')"
              ]
            )
        </scenario>
        
        <scenario name="understanding_data_flow">
          if analyzing_data_flow():
            return SearchGuidance(
              "🔍 Tracing data flow",
              strategies=[
                "Start from entry point (API/UI)",
                "Follow function calls systematically",
                "Map data transformations"
              ],
              visual_aid="""
                API endpoint → Controller → Service → Database
                     ↓              ↓           ↓         ↓
                  validation    business    data      query
                               logic     transform
              """
            )
        </scenario>
      </search_assistance>
    </phase>
    
    <phase name="analyze_findings" order="3">
      <helpful_validations>
        <!-- Help organize complex findings -->
        if too_much_information():
          return Guidance(
            "📊 Organizing your findings",
            problem="Found too much information to process",
            organization_tips=[
              "Group by functionality or component",
              "Create a hierarchy: System → Module → Function",
              "Focus on most relevant findings first",
              "Use diagrams for complex relationships"
            ],
            template="""
              ## Key Findings
              
              ### Component A
              - Purpose: ...
              - Key files: ...
              - Dependencies: ...
              
              ### Component B
              - Purpose: ...
              - Interactions with A: ...
            """
          )
        
        <!-- Help identify patterns -->
        if missing_patterns():
          return Guidance(
            "🔍 Pattern Recognition Help",
            look_for=[
              "Repeated code structures across files",
              "Common naming conventions",
              "Consistent error handling approaches",
              "Shared utility functions"
            ],
            examples=[
              "All API handlers follow: validate → process → respond",
              "Error format: {code: 'ERROR_TYPE', message: '...'}",
              "Database queries use repository pattern"
            ]
          )
      </helpful_validations>
      
      <actions>
        Process and synthesize the information
        Identify patterns and themes
        Compare different approaches
        Evaluate pros and cons
        Note gaps and inconsistencies
        Document key insights
      </actions>
    </phase>
    
    <phase name="validate_understanding" order="4">
      <helpful_validations>
        <!-- Help verify understanding -->
        if understanding_uncertain():
          return Guidance(
            "✓ Validating your understanding",
            verification_methods=[
              "Trace through a specific example",
              "Check if your mental model matches the code",
              "Look for contradicting evidence",
              "Test assumptions with small experiments"
            ],
            example_trace="""
              Let's trace a user login:
              1. POST /api/login receives credentials
              2. AuthController.login validates format
              3. AuthService.authenticate checks database
              4. Returns JWT token or error
              
              Does this match what you found?
            """
          )
      </helpful_validations>
    </phase>
    
    <phase name="document_results" order="5">
      <helpful_validations>
        <!-- Guide documentation creation -->
        if documentation_incomplete():
          return Guidance(
            "📝 Documentation Checklist",
            missing_sections=identify_missing_sections(),
            template="""
              # Research: {topic}
              
              ## Summary
              {one_paragraph_overview}
              
              ## Key Findings
              - Finding 1: ...
              - Finding 2: ...
              
              ## Architecture/Flow
              {diagram_or_description}
              
              ## Recommendations
              - For implementation: ...
              - Potential issues: ...
              
              ## References
              - Key files: ...
              - Documentation: ...
            """,
            reminder="Good documentation helps future you!"
          )
      </helpful_validations>
    </phase>
    
  </implementation>
  
  <error_handling>
    <error code="RAP001" severity="warning">
      <old_message>Insufficient research depth - expand information gathering</old_message>
      <helpful_message>
        ⚠️  Research Depth Warning
        
        Your analysis might be too shallow for the task at hand.
        
        Current coverage:
        - Files examined: {file_count}
        - Patterns identified: {pattern_count}
        - Cross-references: {xref_count}
        
        For '{research_topic}', also consider:
        {suggested_additional_areas}
        
        Quick additions:
        1. {specific_suggestion_1}
        2. {specific_suggestion_2}
        3. {specific_suggestion_3}
        
        Commands to dig deeper:
        {relevant_search_commands}
      </helpful_message>
    </error>
    
    <error code="RAP002" severity="warning">
      <old_message>Single source reliance - require multiple sources</old_message>
      <helpful_message>
        ⚠️  Single Source Warning
        
        Relying on only one source of information is risky.
        
        Current source: {single_source}
        
        Also check:
        - Documentation: Look for README, docs/, or wiki
        - Code comments: Often contain rationale
        - Tests: Show intended behavior
        - Git history: Understand evolution
        - Issues/PRs: Discussion and context
        
        Specific suggestions for '{topic}':
        {contextual_source_suggestions}
        
        This prevents misunderstanding from incomplete info.
      </helpful_message>
    </error>
    
    <error code="RAP003" severity="critical">
      <old_message>Contradictory evidence unresolved - require resolution</old_message>
      <helpful_message>
        ❌ Contradictory Information Found
        
        Found conflicting information that needs resolution:
        
        Source 1: {source_1}
        Claims: {claim_1}
        
        Source 2: {source_2}  
        Claims: {claim_2}
        
        To resolve:
        1. Check which is more recent
           Command: git log -p {file_1} {file_2}
        
        2. Look for deprecation notices
           Command: Grep('deprecated|obsolete|legacy')
        
        3. Check active usage
           Command: Grep('{pattern}' to see what's actually used)
        
        4. Ask yourself:
           - Which pattern appears more frequently?
           - Which has more recent commits?
           - Which has better test coverage?
        
        Can't resolve? Document both approaches with context.
      </helpful_message>
    </error>
    
    <error code="RAP004" severity="warning">
      <old_message>Missing documentation - require findings documentation</old_message>
      <helpful_message>
        ⚠️  Documentation Required
        
        You've done the research but haven't documented findings.
        
        Research topic: {topic}
        Time invested: {duration}
        
        Quick documentation template:
        ```markdown
        # Research: {topic}
        Date: {date}
        
        ## What I Was Looking For
        {research_goal}
        
        ## What I Found
        - Key insight 1: ...
        - Key insight 2: ...
        
        ## Important Files
        - {file_1}: {what_it_does}
        - {file_2}: {what_it_does}
        
        ## Next Steps
        - {actionable_next_step_1}
        - {actionable_next_step_2}
        ```
        
        Save to: docs/research/{topic}-{date}.md
        
        Future you will thank present you!
      </helpful_message>
    </error>
  </error_handling>
  
  <common_blockers>
    <blocker name="empty_search_results">
      <symptom>Search returns no results</symptom>
      <helpful_response>
        🔍 No results? Let's troubleshoot:
        
        Searched for: "{search_term}"
        
        Try these approaches:
        1. Broaden your search
           - Remove specific terms: "{broader_term}"
           - Use wildcards: "{term}*"
           
        2. Check different locations
           - Current search path: {path}
           - Try: {alternative_paths}
           
        3. Different search strategy
           - By file type: Glob('**/*.{extension}')
           - By content: Grep('{partial_term}')
           - By structure: LS() to explore
           
        4. Verify basics
           - Are you in the right directory?
           - Is the codebase checked out?
           - Do the files exist?
           
        Still stuck? The feature might not exist yet!
      </helpful_response>
    </blocker>
    
    <blocker name="too_many_results">
      <symptom>Search returns too many results to analyze</symptom>
      <helpful_response>
        📚 Too many results? Let's filter:
        
        Found: {result_count} matches
        
        Filtering strategies:
        1. Add more specific terms
           Current: "{search}"
           Better: "{search} AND {specific_context}"
           
        2. Limit by file type
           Add: --type=js or glob='*.py'
           
        3. Exclude irrelevant paths
           Skip: node_modules, vendor, build
           
        4. Focus on key directories
           Instead of: "/"
           Try: "/src" or "/app"
           
        5. Use smarter patterns
           Instead of: "user"
           Try: "class User" or "function.*user"
           
        Pro tip: Start narrow, broaden if needed.
      </helpful_response>
    </blocker>
  </common_blockers>
  
  <success_indicators>
    <indicator>Clear understanding of researched topic</indicator>
    <indicator>Multiple sources validate findings</indicator>
    <indicator>Patterns and conventions identified</indicator>
    <indicator>Findings documented for future reference</indicator>
    <indicator>Research directly informs next steps</indicator>
  </success_indicators>
  
</module>
```

## Benefits of Enhanced Research Errors

### For Users
1. **Better Search Results**: Know how to search effectively
2. **Organized Analysis**: Structure complex findings clearly
3. **Validation Confidence**: Know when understanding is correct
4. **Time Savings**: Avoid common research pitfalls

### For Framework
1. **Higher Quality Research**: Users do thorough analysis
2. **Better Documentation**: Findings captured systematically
3. **Improved Decisions**: Research leads to better implementation
4. **Knowledge Retention**: Research documented for reuse

## Real-World Example

### Before Enhancement
```
User: /query "how does authentication work"
Error: RAP001 - Insufficient research depth
```

### After Enhancement
```
User: /query "how does authentication work"

⚠️ Research Depth Warning

Your analysis might be too shallow for authentication understanding.

Current coverage:
- Files examined: 3
- Patterns identified: 1  
- Cross-references: 0

For 'authentication', also consider:
- Token generation and validation
- Session management approach
- Password hashing strategy
- Permission checking logic

Quick additions:
1. Search for JWT/session handling: Grep('jwt|session|token')
2. Find auth middleware: Grep('authenticate|authorize')
3. Check security config: Read('./config/security.*')

Commands to dig deeper:
- Grep('login|signin', path='src/')
- Grep('bcrypt|hash|salt')
- Read('./src/middleware/auth.js')
```

---

**Note**: This enhanced version provides helpful guidance throughout the research process while maintaining all existing functionality.