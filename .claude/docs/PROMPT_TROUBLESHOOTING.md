# Troubleshooting Guide and FAQ for /prompt Command

<guide_metadata>
  <purpose>Comprehensive troubleshooting guide and frequently asked questions for prompt engineering</purpose>
  <audience>All users of the /prompt command</audience>
  <version>1.0.0</version>
  <last_updated>2025-07-06</last_updated>
</guide_metadata>

## Overview

This guide addresses common issues, provides solutions, and answers frequently asked questions about the `/prompt` command and prompt engineering within the Claude Code framework.

<troubleshooting_sections>
  <section name="common_errors">Solutions for typical error messages and failures</section>
  <section name="performance_issues">Addressing slow or inefficient prompt behavior</section>
  <section name="quality_problems">Fixing low-quality or inconsistent outputs</section>
  <section name="integration_issues">Resolving problems with other commands and workflows</section>
  <section name="advanced_debugging">Debugging complex prompt systems and patterns</section>
  <section name="faq">Frequently asked questions and best practices</section>
</troubleshooting_sections>

## Common Errors and Solutions

### Error 1: "Invalid subcommand" 

**Error Message**: 
```
Error: Invalid subcommand 'creat'. Use: create, evaluate, test, or improve
```

**Cause**: Typo in subcommand name or using unsupported subcommand.

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Check spelling of subcommand</action>
    <example>
      ```bash
      # Wrong
      /prompt creat "my_prompt"
      
      # Correct
      /prompt create "my_prompt"
      ```
    </example>
  </solution>
  
  <solution priority="secondary">
    <action>Verify available subcommands</action>
    <command>/prompt --help</command>
    <available_subcommands>create, evaluate, test, improve</available_subcommands>
  </solution>
</solution_set>

### Error 2: "Prompt file not found"

**Error Message**:
```
Error: Prompt file not found: my_prompt.md
FileNotFoundError: [Errno 2] No such file or directory: 'my_prompt.md'
```

**Cause**: Incorrect file path or file doesn't exist.

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Verify file path and location</action>
    <example>
      ```bash
      # Check if file exists
      ls .claude/prompts/
      
      # Use full path
      /prompt evaluate ".claude/prompts/my_prompt_v1.0.md"
      ```
    </example>
  </solution>
  
  <solution priority="secondary">
    <action>Check file naming convention</action>
    <convention>Prompts are saved as {name}_{version}.md in .claude/prompts/</convention>
    <example>
      ```bash
      # After creating a prompt
      /prompt create "my_assistant"
      # Creates: .claude/prompts/my_assistant_v1.0.md
      
      # Correct evaluation
      /prompt evaluate "my_assistant_v1.0.md"
      ```
    </example>
  </solution>
</solution_set>

### Error 3: "Invalid parameter value"

**Error Message**:
```
Error: Invalid value 'wrong_type' for parameter --type. 
Valid values are: system, user, assistant, hybrid
```

**Cause**: Using unsupported parameter values.

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Use correct parameter values</action>
    <valid_parameters>
      <parameter name="--type">system, user, assistant, hybrid</parameter>
      <parameter name="--framework">claude, gpt, general</parameter>
      <parameter name="--style">directive, conversational, structured, narrative</parameter>
      <parameter name="--metrics">clarity, specificity, robustness, effectiveness, all</parameter>
      <parameter name="--scenarios">basic, edge-cases, adversarial, all</parameter>
    </valid_parameters>
  </solution>
  
  <solution priority="secondary">
    <action>Check parameter help</action>
    <command>/prompt create --help</command>
    <note>Shows all available parameters and values for each subcommand</note>
  </solution>
</solution_set>

### Error 4: "Evaluation failed with low scores"

**Error Message**:
```
Warning: Evaluation completed with concerning scores:
- Clarity: 4.2/10 (Below minimum threshold of 6.0)
- Specificity: 3.8/10 (Below minimum threshold of 6.0)
```

**Cause**: Prompt quality issues affecting evaluation metrics.

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Review prompt structure and clarity</action>
    <improvement_areas>
      <area name="clarity">
        <issue>Ambiguous instructions</issue>
        <fix>Use specific, unambiguous language</fix>
        <example>
          ```markdown
          <!-- Unclear -->
          Please help with coding stuff.
          
          <!-- Clear -->
          Analyze the provided Python code for bugs, performance issues, 
          and suggest specific improvements with code examples.
          ```
        </example>
      </area>
      
      <area name="specificity">
        <issue>Vague requirements</issue>
        <fix>Add detailed instructions and examples</fix>
        <example>
          ```markdown
          <!-- Vague -->
          Review this code.
          
          <!-- Specific -->
          ## Code Review Process
          1. Check for syntax errors and logic bugs
          2. Evaluate performance and optimization opportunities  
          3. Assess security vulnerabilities
          4. Suggest improvements with rationale
          
          ## Output Format
          - Summary: Brief overview of findings
          - Critical Issues: High-priority problems requiring immediate attention
          - Improvements: Suggestions for enhancement
          ```
        </example>
      </area>
    </improvement_areas>
  </solution>
  
  <solution priority="secondary">
    <action>Use prompt patterns for better structure</action>
    <recommended_patterns>
      <pattern>XML-Structured for complex prompts</pattern>
      <pattern>Few-Shot for format-specific tasks</pattern>
      <pattern>Chain-of-Thought for reasoning tasks</pattern>
    </recommended_patterns>
  </solution>
</solution_set>

### Error 5: "Test scenarios failed"

**Error Message**:
```
Test Results: 3/8 scenarios passed (37.5% success rate)
Failed scenarios: edge_case_1, edge_case_2, adversarial_1, adversarial_2, basic_3
```

**Cause**: Prompt doesn't handle various input scenarios properly.

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Add error handling and edge case coverage</action>
    <improvements>
      <improvement name="edge_case_handling">
        ```markdown
        ## Error Handling
        
        <error_scenarios>
          <scenario name="empty_input">
            <response>Request the required input before proceeding</response>
          </scenario>
          
          <scenario name="invalid_format">
            <response>Explain the expected format and ask for correction</response>
          </scenario>
          
          <scenario name="unclear_request">
            <response>Ask clarifying questions to understand the requirement</response>
          </scenario>
        </error_scenarios>
        ```
      </improvement>
      
      <improvement name="input_validation">
        ```markdown
        ## Input Validation
        
        Before processing any request:
        1. Verify all required information is provided
        2. Check that input format matches expectations
        3. Validate that the request is within scope
        4. If any validation fails, provide helpful guidance
        ```
      </improvement>
    </improvements>
  </solution>
  
  <solution priority="secondary">
    <action>Review failed test scenarios</action>
    <debugging_approach>
      ```bash
      # Get detailed test results
      /prompt test "my_prompt.md" --scenarios all --output detailed_report.md
      
      # Review specific failure details
      cat detailed_report.md
      
      # Fix issues and retest
      /prompt improve "my_prompt.md" --based-on detailed_report.md
      ```
    </debugging_approach>
  </solution>
</solution_set>

## Performance Issues

### Issue 1: Slow Response Times

**Symptoms**: Prompts take unusually long to execute or evaluate.

**Diagnosis**:
<diagnostic_steps>
  <step>Check prompt complexity and token count</step>
  <step>Verify network connectivity and API limits</step>
  <step>Review pattern complexity (Tree-of-Thought, Self-Consistency are slower)</step>
  <step>Check for infinite loops in reasoning patterns</step>
</diagnostic_steps>

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Optimize prompt structure for efficiency</action>
    <optimization_techniques>
      <technique name="token_reduction">
        ```bash
        # Check current token count
        /prompt evaluate "my_prompt.md" --metrics efficiency
        
        # Create token-optimized version
        /prompt create "my_prompt_optimized" --style efficient --tokens-max 1000
        ```
      </technique>
      
      <technique name="pattern_simplification">
        ```markdown
        <!-- Complex (slow) -->
        Use Tree-of-Thought with Self-Consistency validation
        
        <!-- Simplified (faster) -->
        Use Chain-of-Thought with single reasoning path
        ```
      </technique>
    </optimization_techniques>
  </solution>
  
  <solution priority="secondary">
    <action>Use progressive complexity</action>
    <approach>Start with simple patterns and escalate only when needed</approach>
    <example>
      ```bash
      # Create adaptive prompt that starts simple
      /prompt create "adaptive_assistant" --complexity adaptive
      ```
    </example>
  </solution>
</solution_set>

### Issue 2: High Token Usage Costs

**Symptoms**: Unexpectedly high API costs due to token consumption.

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Implement token budgeting</action>
    <budgeting_strategies>
      <strategy name="prompt_optimization">
        ```bash
        # Set token limits during creation
        /prompt create "cost_optimized" --tokens-max 500 --style efficient
        
        # Monitor token usage
        /prompt evaluate "cost_optimized.md" --metrics efficiency
        ```
      </strategy>
      
      <strategy name="pattern_selection">
        ```markdown
        Token Efficiency by Pattern:
        - Zero-Shot: 50-200 tokens (Very High efficiency)
        - Few-Shot: 200-800 tokens (High efficiency)  
        - Chain-of-Thought: 400-1200 tokens (Medium efficiency)
        - Tree-of-Thought: 800-2000 tokens (Low efficiency)
        - Self-Consistency: 1200-3000 tokens (Very Low efficiency)
        ```
      </strategy>
    </budgeting_strategies>
  </solution>
  
  <solution priority="secondary">
    <action>Use caching for repeated components</action>
    <caching_approach>
      ```bash
      # Cache common prompt sections
      /prompt cache create "security_guidelines" --content "security_section.md"
      
      # Reuse cached content
      /prompt create "secure_reviewer" --include-cache "security_guidelines"
      ```
    </caching_approach>
  </solution>
</solution_set>

## Quality Problems

### Issue 1: Inconsistent Output Quality

**Symptoms**: Same prompt produces varying quality results across different runs.

**Diagnosis**:
<diagnostic_checklist>
  <check>Prompt contains ambiguous instructions</check>
  <check>Missing examples or constraints</check>
  <check>Overly complex reasoning chains</check>
  <check>Insufficient error handling</check>
</diagnostic_checklist>

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Add consistency mechanisms</action>
    <consistency_techniques>
      <technique name="explicit_constraints">
        ```markdown
        ## Output Requirements
        
        <constraints>
          <format>Always use the specified JSON structure</format>
          <length>Responses must be 100-300 words</length>
          <tone>Maintain professional, helpful tone</tone>
          <accuracy>Verify all facts before including</accuracy>
        </constraints>
        ```
      </technique>
      
      <technique name="validation_steps">
        ```markdown
        ## Quality Validation
        
        Before providing your response:
        1. Verify it addresses the specific question asked
        2. Check that all required information is included
        3. Confirm the format matches requirements
        4. Review for clarity and accuracy
        ```
      </technique>
    </consistency_techniques>
  </solution>
  
  <solution priority="secondary">
    <action>Use Self-Consistency pattern for critical tasks</action>
    <implementation>
      ```bash
      # Create self-validating prompt
      /prompt create "consistent_analyzer" --pattern self-consistency
      ```
    </implementation>
  </solution>
</solution_set>

### Issue 2: Low Accuracy or Relevance

**Symptoms**: Prompt outputs don't meet accuracy requirements or miss the point.

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Improve prompt specificity and examples</action>
    <improvement_framework>
      <step name="add_context">
        ```markdown
        ## Context
        You are analyzing financial data for investment decisions.
        The user needs actionable insights for portfolio management.
        Accuracy is critical as recommendations affect real investments.
        ```
      </step>
      
      <step name="provide_examples">
        ```markdown
        ## Examples
        
        Input: "AAPL stock analysis"
        Good Output: "Apple Inc. (AAPL) analysis: P/E ratio 28.5 vs sector avg 24.2, 
                    revenue growth 8.1% YoY, recommend HOLD with $175 target based on..."
        
        Poor Output: "Apple is a good company with strong products."
        ```
      </step>
      
      <step name="define_success_criteria">
        ```markdown
        ## Success Criteria
        - Include specific numerical data
        - Provide clear recommendations with rationale
        - Reference current market conditions
        - Mention relevant risks and opportunities
        ```
      </step>
    </improvement_framework>
  </solution>
  
  <solution priority="secondary">
    <action>Use Chain-of-Thought for complex analysis</action>
    <reasoning_structure>
      ```markdown
      ## Analysis Process
      
      Step 1: Gather and verify relevant data
      Step 2: Apply appropriate analytical frameworks
      Step 3: Consider multiple perspectives and scenarios
      Step 4: Synthesize findings into clear recommendations
      Step 5: Validate conclusions against success criteria
      ```
    </reasoning_structure>
  </solution>
</solution_set>

## Integration Issues

### Issue 1: /prompt Command Conflicts with Other Commands

**Symptoms**: Unexpected behavior when using /prompt with /auto, /task, or /swarm.

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Understand command hierarchy and delegation</action>
    <hierarchy_explanation>
      ```
      /auto → Intelligent routing (may use /prompt internally)
      /task → Development execution (integrates with /prompt)
      /swarm → Multi-agent coordination (uses specialized prompts)
      /prompt → Direct prompt engineering (standalone or integrated)
      ```
    </hierarchy_explanation>
  </solution>
  
  <solution priority="secondary">
    <action>Use appropriate command for your use case</action>
    <use_case_mapping>
      <mapping>
        <scenario>Creating standalone prompts</scenario>
        <command>/prompt create</command>
      </mapping>
      <mapping>
        <scenario>Prompts for development workflows</scenario>
        <command>/task with prompt integration</command>
      </mapping>
      <mapping>
        <scenario>Multi-agent prompt coordination</scenario>
        <command>/swarm with prompt specifications</command>
      </mapping>
      <mapping>
        <scenario>Uncertain about best approach</scenario>
        <command>/auto (will route appropriately)</command>
      </mapping>
    </use_case_mapping>
  </solution>
</solution_set>

### Issue 2: Session Management Conflicts

**Symptoms**: Prompt work not properly tracked in sessions or sessions interfering with prompt evaluation.

**Solutions**:
<solution_set>
  <solution priority="primary">
    <action>Properly integrate prompt work with session management</action>
    <integration_approach>
      ```bash
      # Start session for complex prompt development
      /session create "prompt_optimization_project"
      
      # Perform prompt work within session context
      /prompt create "complex_assistant" --session-aware
      /prompt evaluate "complex_assistant_v1.0.md" --session-update
      /prompt improve "complex_assistant_v1.0.md" --session-track
      
      # Session automatically tracks progress
      /session status
      ```
    </integration_approach>
  </solution>
</solution_set>

## Advanced Debugging

### Debugging Complex Pattern Combinations

**Symptoms**: Multi-pattern prompts behaving unexpectedly or producing poor results.

**Debugging Approach**:
<debugging_methodology>
  <step name="isolate_patterns">
    <description>Test each pattern individually</description>
    <example>
      ```bash
      # Test base prompt without patterns
      /prompt create "base_version" --patterns none
      /prompt test "base_version.md"
      
      # Add patterns one by one
      /prompt create "with_xml" --patterns xml-structured
      /prompt create "with_xml_cot" --patterns xml-structured,chain-of-thought
      
      # Compare results
      /prompt evaluate "base_version.md,with_xml.md,with_xml_cot.md" --compare
      ```
    </example>
  </step>
  
  <step name="analyze_interactions">
    <description>Identify pattern conflicts or synergies</description>
    <common_conflicts>
      <conflict>
        <patterns>Tree-of-Thought + Token-Efficient</patterns>
        <issue>Contradictory goals (exploration vs. brevity)</issue>
        <solution>Use adaptive complexity or choose primary goal</solution>
      </conflict>
      <conflict>
        <patterns>Role-Based + Zero-Shot</patterns>
        <issue>Role context may override zero-shot simplicity</issue>
        <solution>Simplify role definition or use Few-Shot instead</solution>
      </conflict>
    </common_conflicts>
  </step>
  
  <step name="optimize_combination">
    <description>Refine pattern interaction for best results</description>
    <optimization_strategies>
      <strategy>Sequence patterns logically (structure → reasoning → validation)</strategy>
      <strategy>Balance complexity with effectiveness requirements</strategy>
      <strategy>Use hierarchical patterns (main + supporting)</strategy>
    </optimization_strategies>
  </step>
</debugging_methodology>

### Performance Profiling for Prompts

**Tools and Techniques**:
<profiling_tools>
  <tool name="token_analysis">
    <purpose>Analyze token usage patterns and efficiency</purpose>
    <command>
      ```bash
      /prompt profile "my_prompt.md" --analysis tokens --detailed
      
      # Output shows:
      # - Token distribution by section
      # - Efficiency metrics
      # - Optimization suggestions
      ```
    </command>
  </tool>
  
  <tool name="execution_timing">
    <purpose>Measure response times and identify bottlenecks</purpose>
    <command>
      ```bash
      /prompt profile "my_prompt.md" --analysis timing --iterations 10
      
      # Output shows:
      # - Average response time
      # - Variance and outliers
      # - Performance breakdown by pattern
      ```
    </command>
  </tool>
  
  <tool name="quality_correlation">
    <purpose>Correlate complexity with quality improvements</purpose>
    <command>
      ```bash
      /prompt profile "my_prompt.md" --analysis quality-complexity
      
      # Output shows:
      # - Quality score vs. token usage
      # - Diminishing returns analysis
      # - Optimal complexity recommendations
      ```
    </command>
  </tool>
</profiling_tools>

## Frequently Asked Questions

### General Questions

<faq_section category="general">
  <question id="q1">
    <q>What's the difference between /prompt and just writing prompts manually?</q>
    <a>The /prompt command provides systematic engineering approaches including evaluation metrics, automated testing, pattern libraries, version control, and improvement workflows. Manual prompting lacks these quality assurance and optimization capabilities.</a>
  </question>
  
  <question id="q2">
    <q>Can I use /prompt with non-Claude AI models?</q>
    <a>Yes, use --framework gpt for OpenAI models or --framework general for model-agnostic prompts. However, some features like XML structuring are optimized for Claude.</a>
  </question>
  
  <question id="q3">
    <q>How do I know which prompt pattern to use?</q>
    <a>Consider task complexity: Zero-Shot for simple tasks, Few-Shot for format-specific work, Chain-of-Thought for reasoning, Tree-of-Thought for creative problems, and Self-Consistency for critical accuracy needs.</a>
  </question>
  
  <question id="q4">
    <q>What's the minimum evaluation score for production use?</q>
    <a>Generally 8.0/10 overall with no individual metric below 7.0. Critical applications may require 8.5+ overall with enhanced security and robustness testing.</a>
  </question>
</faq_section>

### Technical Questions

<faq_section category="technical">
  <question id="t1">
    <q>How are evaluation metrics calculated?</q>
    <a>Metrics use weighted scoring: Clarity (30%), Specificity (30%), Robustness (20%), Effectiveness (20%). Each metric analyzes multiple factors using both automated checks and heuristic assessments.</a>
  </question>
  
  <question id="t2">
    <q>Can I create custom evaluation metrics?</q>
    <a>Yes, use --custom-metrics parameter with your evaluation framework. See PROMPT_ADVANCED_FEATURES.md for details on implementing domain-specific metrics.</a>
  </question>
  
  <question id="t3">
    <q>How do I handle sensitive information in prompts?</q>
    <a>Use placeholder variables, implement input sanitization, add security validation steps, and test with adversarial scenarios. Never include actual sensitive data in prompt templates.</a>
  </question>
  
  <question id="t4">
    <q>What's the token limit for prompts?</q>
    <a>No hard limit, but recommendations: System prompts 1000-4000 tokens, User prompts 200-1000 tokens, Complex analysis prompts up to 8000 tokens. Monitor costs and performance.</a>
  </question>
</faq_section>

### Best Practices Questions

<faq_section category="best_practices">
  <question id="bp1">
    <q>How often should I update and improve prompts?</q>
    <a>Monitor continuously, evaluate monthly, and improve when: success rate drops >5%, new use cases emerge, user feedback indicates issues, or technology updates require adaptation.</a>
  </question>
  
  <question id="bp2">
    <q>Should I use multiple patterns in one prompt?</q>
    <a>Use multiple patterns when task complexity justifies it, but start simple. Common effective combinations: XML + Chain-of-Thought, Few-Shot + Role-Based, Tree-of-Thought + Self-Consistency.</a>
  </question>
  
  <question id="bp3">
    <q>How do I handle prompt versioning in teams?</q>
    <a>Use semantic versioning (major.minor.patch), maintain changelog, require peer review for production changes, and use branch-based development with proper testing before merges.</a>
  </question>
  
  <question id="bp4">
    <q>What's the best way to test prompts?</q>
    <a>Test progressively: basic scenarios first, then edge cases, finally adversarial inputs. Use automated testing for regressions and manual testing for quality assessment.</a>
  </question>
</faq_section>

### Troubleshooting Questions

<faq_section category="troubleshooting">
  <question id="ts1">
    <q>My prompt works sometimes but fails other times. Why?</q>
    <a>Common causes: ambiguous instructions, missing edge case handling, insufficient examples, or overly complex reasoning chains. Add explicit constraints and error handling.</a>
  </question>
  
  <question id="ts2">
    <q>How do I debug prompts that produce wrong answers?</q>
    <a>Use Chain-of-Thought to see reasoning steps, add validation instructions, provide more specific examples, and test with edge cases to identify failure patterns.</a>
  </question>
  
  <question id="ts3">
    <q>My evaluation scores are low but the prompt seems to work. Why?</q>
    <a>Evaluation metrics may not align with your specific use case. Consider custom metrics, manual quality assessment, or adjusting the prompt structure to better match evaluation criteria.</a>
  </question>
  
  <question id="ts4">
    <q>How do I fix prompts that are too slow?</q>
    <a>Reduce token count, simplify patterns (use Zero-Shot instead of Tree-of-Thought), remove unnecessary examples, and use efficient XML structure instead of verbose prose.</a>
  </question>
</faq_section>

## Getting Additional Help

### Support Resources

<support_resources>
  <resource name="documentation">
    <description>Comprehensive guides and references</description>
    <files>
      <file>PROMPT_USAGE_GUIDE.md - Complete command reference</file>
      <file>PROMPT_PATTERNS_GUIDE.md - Pattern library and examples</file>
      <file>PROMPT_BEST_PRACTICES.md - Optimization guidelines</file>
      <file>PROMPT_ADVANCED_FEATURES.md - Advanced techniques</file>
    </files>
  </resource>
  
  <resource name="community_support">
    <description>Community forums and discussion channels</description>
    <channels>
      <channel>GitHub Issues - Bug reports and feature requests</channel>
      <channel>GitHub Discussions - Questions and community help</channel>
      <channel>Discord/Slack - Real-time community support</channel>
    </channels>
  </resource>
  
  <resource name="professional_support">
    <description>Enterprise and professional support options</description>
    <options>
      <option>Consulting services for complex implementations</option>
      <option>Training programs for teams and organizations</option>
      <option>Custom pattern development and optimization</option>
    </options>
  </resource>
</support_resources>

### Escalation Process

<escalation_process>
  <level name="self_service" priority="1">
    <resources>Documentation, FAQ, community forums</resources>
    <timeline>Immediate</timeline>
  </level>
  
  <level name="community_support" priority="2">
    <resources>GitHub issues, community discussions, Discord/Slack</resources>
    <timeline>1-3 days</timeline>
  </level>
  
  <level name="maintainer_support" priority="3">
    <resources>Direct contact with framework maintainers</resources>
    <timeline>3-7 days</timeline>
    <criteria>Critical bugs, security issues, framework-level problems</criteria>
  </level>
  
  <level name="professional_support" priority="4">
    <resources>Paid consulting and professional services</resources>
    <timeline>By agreement</timeline>
    <criteria>Complex implementations, training needs, custom development</criteria>
  </level>
</escalation_process>

## Contributing to Troubleshooting

Help improve this guide by:

<contribution_opportunities>
  <opportunity name="report_issues">
    <description>Report new issues and solutions you discover</description>
    <process>Create GitHub issue with detailed problem description and solution</process>
  </opportunity>
  
  <opportunity name="add_faqs">
    <description>Contribute frequently asked questions from your experience</description>
    <process>Submit pull request with new FAQ entries and solutions</process>
  </opportunity>
  
  <opportunity name="improve_solutions">
    <description>Enhance existing solutions with better approaches</description>
    <process>Submit pull request with improved troubleshooting steps</process>
  </opportunity>
  
  <opportunity name="add_examples">
    <description>Provide real-world examples and case studies</description>
    <process>Share anonymized examples of problems and solutions</process>
  </opportunity>
</contribution_opportunities>

---

*This troubleshooting guide is continuously updated based on user feedback and emerging issues. If you encounter problems not covered here, please contribute your findings to help the community.*