---
name: /think-deep
description: "Advanced deep thinking and problem-solving with structured analysis, multi-perspective exploration, and comprehensive synthesis"
usage: "[problem_statement] [thinking_depth]"
tools: Read, Write, Edit, Bash, Grep
---
# /think deep - Advanced Deep Thinking
A powerful command for deep thinking and complex problem-solving, utilizing structured analysis, multi-perspective exploration, and comprehensive synthesis.
## Usage
```bash
/think deep "How can we optimize our database performance?" # Start a deep thinking session
/think deep --depth "high" "What are the security implications of our new feature?" # High-depth thinking
/think deep --framework "first_principles" "Analyze our user engagement strategy" # Use a specific thinking framework
```
<command_file>
  <metadata>
    <n>/think deep</n>
    <purpose>Advanced deep thinking and problem-solving with structured analysis, multi-perspective exploration, and comprehensive synthesis</purpose>
    <usage>
      <![CDATA[
      /think deep "[problem_statement]" --depth [thinking_depth] --framework [thinking_framework]
      ]]>
    </usage>
  </metadata>
  <arguments>
    <argument name="problem_statement" type="string" required="true">
      <description>The problem or question to think deeply about</description>
    </argument>
    <argument name="thinking_depth" type="string" required="false" default="medium">
      <description>The depth of the thinking process (e.g., low, medium, high)</description>
    </argument>
    <argument name="thinking_framework" type="string" required="false" default="structured_analysis">
      <description>The thinking framework to use (e.g., structured_analysis, first_principles, six_thinking_hats)</description>
    </argument>
  </arguments>
  <examples>
    <example>
      <description>Start a deep thinking session on database performance</description>
      <usage>/think deep "How can we optimize our database performance by 50%?"</usage>
    </example>
    <example>
      <description>High-depth thinking on security implications</description>
      <usage>/think deep --depth "high" "What are the long-term security implications of using a third-party authentication service?"</usage>
    </example>
  </examples>
  <claude_prompt>
    <prompt>
You are an advanced deep thinking and problem-solving specialist. The user wants to engage in a deep thinking process to analyze a complex problem.
**Thinking Process:**
1. **Deconstruct the Problem**: Break down the problem into its fundamental components
2. **Multi-perspective Analysis**: Analyze the problem from various perspectives (e.g., technical, business, user)
3. **Generate Insights**: Generate deep insights and potential solutions through structured thinking frameworks
4. **Synthesize Findings**: Synthesize the analysis and insights into a comprehensive conclusion
5. **Formulate Action Plan**: Formulate a clear, actionable plan based on the synthesized findings
**Implementation Strategy:**
- Use the specified thinking framework to guide the analysis (e.g., First Principles, Six Thinking Hats, SWOT Analysis)
- Explore the problem from multiple angles, considering short-term and long-term implications
- Generate a wide range of ideas and solutions, then critically evaluate them
- Synthesize the findings into a structured report with clear arguments and evidence
- Provide a prioritized, actionable plan with concrete next steps
<include component="components/reasoning/tree-of-thoughts.md" />
<include component="components/reporting/generate-structured-report.md" />
    </prompt>
  </claude_prompt>
  <dependencies>
    <includes_components>
      <component>components/reasoning/tree-of-thoughts.md</component>
      <component>components/reporting/generate-structured-report.md</component>
    </includes_components>
    <uses_config_values>
      <value>thinking.default_framework</value>
      <value>reporting.output.format</value>
    </uses_config_values>
  </dependencies>
</command_file>