| version | last_updated | status | readiness |
|---------|--------------|--------|----------|
| 3.0.0   | 2025-07-12   | stable | 80%      |

# Docs Command - Documentation Generation and Management

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

```xml
<command name="docs" category="documentation" enforcement="CRITICAL">
  
  <purpose>
    Execute comprehensive documentation generation with audience-focused content creation, systematic organization, quality validation, and maintainability optimization with Claude 4 enhanced content generation capabilities.
  </purpose>
  
  <scope>
    <includes>API documentation, user guides, technical specifications, setup guides, architecture documentation, contributing guidelines</includes>
    <excludes>Code implementation, system modifications, configuration changes, non-documentation tasks</excludes>
    <boundaries>Documentation-only operations with systematic content creation and organization without system modifications</boundaries>
  </scope>
  
  <input_specification>
    <required_arguments>Documentation requirements with target audience, content type, scope, and quality standards</required_arguments>
    <context_requirements>System documentation, codebase access, existing documentation patterns, audience requirements</context_requirements>
    <preconditions>Documentation framework available, target audience defined, content scope established, quality standards set</preconditions>
  </input_specification>
  
  <output_specification>
    <deliverables>Comprehensive documentation, organized content structure, validation reports, maintenance procedures</deliverables>
    <success_criteria>Documentation complete, audience needs met, quality validated, maintenance procedures established</success_criteria>
    <artifacts>Documentation files, content organization, style guides, validation reports, maintenance documentation</artifacts>
  </output_specification>
</command>
```

Documentation generation and management.

## Thinking Pattern - Claude 4 Enhanced

```xml
<thinking_pattern enforcement="MANDATORY">
  
  <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="extended">
    <action>Documentation Scope and Audience Analysis: Comprehensive analysis of documentation requirements and target audience needs</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What documentation is needed and for which specific audiences?
        - How do audience requirements inform content structure and presentation?
        - What scope ensures comprehensive coverage without overwhelming detail?
      </pre_analysis>
      <critical_thinking minimum_time="45_seconds">
        - [Audience Question: Who are the target audiences and what are their specific documentation needs?]
        - [Scope Question: What content boundaries ensure comprehensive yet focused documentation?]
        - [Requirements Question: What functional and quality requirements must documentation meet?]
        - [Context Question: How does existing documentation inform structure and approach?]
        - [Value Question: What documentation provides maximum practical value to users?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this documentation approach serve audience needs optimally?
        - What evidence supports scope decisions and content prioritization?
        - How does analysis ensure comprehensive yet accessible documentation?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch audience analysis, scope definition, and requirements gathering</tool_optimization>
      <context_efficiency>Load existing documentation, system context, and audience needs concurrently</context_efficiency>
      <dependency_analysis>Identify analysis steps that can be parallelized vs sequential requirements development</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>DOCS_ANALYSIS: [audiences] requiring [content_types] with [scope] meeting [quality_standards]</output_format>
    <validation>Audiences clearly defined, content scope appropriate, requirements validated, quality standards established</validation>
    <enforcement>BLOCK documentation creation until comprehensive analysis validates approach</enforcement>
    <context_transfer>Audience definitions, content scope, quality requirements, documentation standards</context_transfer>
  </checkpoint>
  
  <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Content Research and Information Gathering: Systematic collection and analysis of documentation source material</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - What source materials provide comprehensive information for documentation?
        - How can research ensure accuracy and completeness of content?
        - What systematic approach optimizes information gathering efficiency?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Sources Question: Are all relevant information sources identified and analyzed comprehensively?]
        - [Accuracy Question: How can content accuracy be validated against source systems?]
        - [Completeness Question: Does research cover all aspects required for comprehensive documentation?]
        - [Currency Question: Is information current and reflective of system state?]
        - [Quality Question: Does source material meet standards for professional documentation?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this research approach ensure comprehensive and accurate content?
        - What evidence validates information completeness and accuracy?
        - How does systematic gathering optimize documentation quality?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Execute parallel information gathering across multiple sources and systems</tool_optimization>
      <context_efficiency>Optimize concurrent research across codebase, existing docs, and system components</context_efficiency>
      <dependency_analysis>Identify research that can be parallelized vs sequential validation requirements</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>CONTENT_RESEARCH: [sources_analyzed] with [information_gathered] ensuring [accuracy] and [completeness]</output_format>
    <validation>All sources analyzed, information comprehensive, accuracy validated, content complete</validation>
    <enforcement>BLOCK content creation until systematic research validates comprehensive information gathering</enforcement>
    <context_transfer>Research findings, validated information, source documentation, accuracy confirmation</context_transfer>
  </checkpoint>
  
  <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Structure Design and Organization Planning: Create logical documentation architecture with optimal user navigation</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should documentation be structured for optimal user experience?
        - What organizational approach serves different audience needs effectively?
        - How can structure balance comprehensiveness with accessibility?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Structure Question: Does documentation structure serve user navigation and comprehension optimally?]
        - [Organization Question: Are content sections logically organized and easily discoverable?]
        - [Flow Question: Does information flow support user learning and task completion?]
        - [Accessibility Question: Is documentation accessible to users with varying expertise levels?]
        - [Maintenance Question: Does structure support ongoing documentation maintenance and updates?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this structural approach optimize user experience and comprehension?
        - What evidence supports organizational decisions for audience effectiveness?
        - How does structure balance comprehensive coverage with practical usability?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Batch structure design, organization planning, and navigation optimization</tool_optimization>
      <context_efficiency>Design structure and user experience concurrently</context_efficiency>
      <dependency_analysis>Identify structural planning that can be optimized while maintaining logical coherence</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>STRUCTURE_DESIGN: [organization] with [navigation] supporting [user_experience] and [maintenance]</output_format>
    <validation>Structure logical, organization optimal, navigation clear, user experience validated, maintenance supported</validation>
    <enforcement>BLOCK content creation until structure design validates user experience and maintainability</enforcement>
    <context_transfer>Documentation structure, organization plan, navigation design, user experience optimization</context_transfer>
  </checkpoint>
  
  <checkpoint id="4" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
    <action>Content Creation and Quality Validation: Generate comprehensive content with systematic quality assurance</action>
    <interleaved_thinking enforcement="MANDATORY">
      <pre_analysis>
        - How should content be created to meet audience needs and quality standards?
        - What quality validation ensures professional and accurate documentation?
        - How can content creation balance comprehensiveness with clarity?
      </pre_analysis>
      <critical_thinking minimum_time="30_seconds">
        - [Content Question: Does generated content meet audience needs and professional standards?]
        - [Clarity Question: Is content clear, well-written, and easily understandable?]
        - [Accuracy Question: Is all content technically accurate and properly validated?]
        - [Completeness Question: Does content coverage address all user requirements comprehensively?]
        - [Consistency Question: Is content style and format consistent throughout documentation?]
      </critical_thinking>
      <decision_reasoning>
        - Why does this content approach ensure professional quality and user value?
        - What evidence demonstrates content accuracy and comprehensive coverage?
        - How does quality validation support ongoing documentation excellence?
      </decision_reasoning>
    </interleaved_thinking>
    <parallel_execution_considerations>
      <tool_optimization>Optimize content creation with concurrent quality validation and review</tool_optimization>
      <context_efficiency>Generate content and validate quality concurrently where appropriate</context_efficiency>
      <dependency_analysis>Identify content creation that can be optimized while maintaining quality standards</dependency_analysis>
    </parallel_execution_considerations>
    <output_format>CONTENT_CREATED: [documentation] with [quality_validated] meeting [standards] and [user_needs]</output_format>
    <validation>Content comprehensive, quality validated, standards met, user needs addressed, consistency maintained</validation>
    <enforcement>BLOCK completion until content creation validates professional quality and comprehensive coverage</enforcement>
    <context_transfer>Complete documentation, quality validation, professional standards confirmation, user value assessment</context_transfer>
  </checkpoint>
  
</thinking_pattern>
```

## Instructions

Execute comprehensive documentation generation workflow for: $ARGUMENTS

1. **Documentation Analysis**: Understand audience needs and documentation requirements.
   - **Analysis Checkpoint**: Define audiences, scope, and quality standards

2. **Content Research**: Systematic information gathering from all relevant sources.
   - **Research Checkpoint**: Comprehensive source analysis with accuracy validation

3. **Structure Design**: Create logical organization optimized for user experience.
   - **Structure Checkpoint**: Design navigation and organization for optimal usability

4. **Content Creation**: Generate comprehensive content with quality validation.
   - **Content Checkpoint**: Professional documentation meeting all requirements

## Critical Rules

- ALWAYS analyze target audience needs before creating content
- NEVER create documentation without systematic research and validation
- Ensure content accuracy through comprehensive source validation
- Use clear, professional writing appropriate for target audience
- **DOCUMENTATION GATEWAY**: ALL documentation must go through /docs command
- **QUALITY STANDARDS**: Maintain professional standards and consistency throughout

## Module Integration

```xml
<module_orchestration>
  <core_modules>
    <module>patterns/thinking/critical-thinking-pattern.md</module>
    <module>development/documentation.md</module>
    <module>patterns/documentation-pattern.md</module>
    <module>patterns/user-interaction-pattern.md</module>
  </core_modules>
  
  <contextual_modules>
    <module condition="api_documentation">patterns/api-documentation.md</module>
    <module condition="user_guides">patterns/user-guide-creation.md</module>
    <module condition="technical_specs">patterns/technical-specification.md</module>
    <module condition="architecture_docs">patterns/architecture-documentation.md</module>
  </contextual_modules>
  
  <support_modules>
    <module>patterns/validation-pattern.md</module>
    <module>patterns/content-organization.md</module>
    <module>quality/documentation-quality.md</module>
  </support_modules>
</module_orchestration>
```

## Documentation Types

- **API Documentation**: Comprehensive API reference with examples
- **User Guides**: Step-by-step guides for end users
- **Technical Specifications**: Detailed technical documentation
- **Architecture Documentation**: System architecture and design documentation
- **Setup Guides**: Installation and configuration instructions
- **Contributing Guidelines**: Development and contribution procedures

## Examples

- `/docs "Create API documentation for user service"` - Generates comprehensive API documentation
- `/docs "Write setup guide for new developers"` - Creates developer onboarding documentation
- `/docs "Document the authentication flow"` - Creates technical flow documentation
- `/docs "Create user guide for admin panel"` - Generates end-user documentation
- `/docs "Document system architecture"` - Creates architectural documentation