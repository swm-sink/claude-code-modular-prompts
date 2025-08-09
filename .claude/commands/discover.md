---
name: discover
description: Deep project discovery and DNA extraction
usage: "/discover"
allowed-tools: [Read, Write, Glob, Grep, WebSearch]
model: opus
---

# Discover Command - Extract Your Project's DNA

<command_execution>
This command performs 30-60 minute deep discovery of your project.
Everything executes through Claude's tools. No external dependencies.
</command_execution>

## Deep Discovery Process

### Phase 1: Technical Architecture (10-15 minutes)
I'll analyze your entire codebase:

- **Framework Detection**: Using Glob and Read to identify all frameworks
- **Dependency Analysis**: Reading lock files and configs
- **Pattern Recognition**: Using Grep to find recurring patterns
- **Testing Strategy**: Identifying test frameworks and coverage
- **Build System**: Understanding compilation and deployment

### Phase 2: Domain Intelligence (10-15 minutes)
I'll extract business understanding:

- **Business Logic**: Analyzing core domain files
- **Data Models**: Understanding entities and relationships
- **API Patterns**: REST, GraphQL, gRPC detection
- **User Flows**: Identifying key user journeys
- **Integration Points**: External services and APIs

### Phase 3: Team Conventions (10-15 minutes)
I'll learn your team's style:

- **Coding Standards**: Naming conventions, file organization
- **Git Patterns**: Commit messages, branching strategy
- **Documentation Style**: Comments, README patterns
- **Error Handling**: Exception patterns and logging
- **Performance Patterns**: Caching, optimization strategies

<pattern_library>
  <anti_patterns>
    <!-- Extracted from ANTIPATTERNS-MASTER.md -->
    <category name="llm_hallucination">
      <pattern>invented_metrics</pattern>
      <pattern>false_success_claims</pattern>
      <pattern>theatrical_language</pattern>
      <prevention>demand_evidence</prevention>
    </category>
    <category name="over_engineering">
      <pattern>unnecessary_abstraction</pattern>
      <pattern>premature_optimization</pattern>
      <pattern>framework_obsession</pattern>
      <prevention>start_simple</prevention>
    </category>
    <category name="context_pollution">
      <pattern>irrelevant_history</pattern>
      <pattern>token_waste</pattern>
      <pattern>context_bloat</pattern>
      <prevention>targeted_context</prevention>
    </category>
  </anti_patterns>
  
  <consultation_flow>
    <!-- Extracted from consultation-flow-simple.md -->
    <stage name="discovery" duration="5-7 minutes">
      <tools>Glob, Read, LS, Grep</tools>
      <focus>project_structure, tech_stack, conventions</focus>
    </stage>
    <stage name="deep_dive" duration="10-15 minutes">
      <tools>Read, Grep, WebSearch</tools>
      <focus>architecture, patterns, dependencies</focus>
    </stage>
    <stage name="synthesis" duration="5-10 minutes">
      <tools>Write</tools>
      <focus>create_project_dna, recommendations</focus>
    </stage>
  </consultation_flow>
  
  <generation_patterns>
    <!-- Extracted from generation-engine-simple.md -->
    <approach>template_based</approach>
    <customization>project_specific</customization>
    <validation>test_generated_commands</validation>
  </generation_patterns>
</pattern_library>

## Output: PROJECT-DNA.md

I'll create a comprehensive PROJECT-DNA.md containing:

```markdown
# Project DNA - [Your Project Name]

## Technical Architecture
- Primary Language: [Detected]
- Frameworks: [List]
- Testing: [Strategy]
- Build: [System]

## Domain Model
- Core Entities: [Identified]
- Business Rules: [Extracted]
- User Journeys: [Mapped]

## Team Conventions
- Code Style: [Analyzed]
- Git Workflow: [Detected]
- Documentation: [Pattern]

## Recommended Commands
Based on your project DNA, I recommend generating:
- `/test-[your-framework]` - Run your specific test suite
- `/deploy-[your-platform]` - Deploy to your platform
- `/analyze-[your-domain]` - Domain-specific analysis
```

## Interactive Process

Throughout discovery, I'll:
1. **Ask clarifying questions** when patterns are ambiguous
2. **Provide confidence scores** for each finding
3. **Show evidence** for all conclusions
4. **Validate with you** before finalizing

<web_validation>
  <!-- References from web-validated-sources.md -->
  <validation confidence="high">
    All patterns validated against 2024-2025 best practices.
    Zero hallucination through evidence-based discovery.
  </validation>
</web_validation>

## Next Step

After discovery completes, run `/generate` to create project-specific commands based on your PROJECT-DNA.md

<execution_guarantee>
This command performs real analysis using Claude's tools.
Not a template. Not instructions. Actual execution.
</execution_guarantee>