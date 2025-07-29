---
description: Advanced documentation publishing with multi-platform distribution, automated deployment, and comprehensive formatting
argument-hint: "[publish_target] [distribution_strategy]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /docs publish - Advanced Documentation Publishing

Sophisticated documentation publishing system with multi-platform distribution, automated deployment, and comprehensive formatting optimization.

## Usage
```bash
/docs publish web                            # Web-based documentation publishing
/docs publish --multi-platform               # Multi-platform distribution
/docs publish --automated                    # Fully automated publishing
/docs publish --comprehensive                # Comprehensive publishing framework
```

<command_file>
  <metadata>
    <n>/docs publish</n>
    <purpose>Advanced documentation publishing with multi-platform distribution, automated deployment, and comprehensive formatting</purpose>
    <usage>
      <![CDATA[
      /docs publish [publish_target]
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="publish_target" type="string" required="false" default="web">
      <description>Target platform for documentation publishing</description>
    </argument>
    <argument name="distribution_strategy" type="string" required="false" default="automated">
      <description>Strategy for documentation distribution</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Web-based documentation publishing</description>
      <usage>/docs publish web</usage>
    </example>
    <example>
      <description>Multi-platform distribution</description>
      <usage>/docs publish --multi-platform</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      <!-- Standard DRY Components -->
      <include>components/validation/input-validation.md</include>
      <include>components/workflow/command-execution.md</include>
      <include>components/workflow/error-handling.md</include>
      <include>components/interaction/progress-reporting.md</include>
      
      <!-- Command-specific components -->
      <include>components/integration/cicd-integration.md</include>
      <include>components/quality/framework-validation.md</include>
      <include>components/performance/auto-scaling.md</include>
      <include>components/documentation/format-optimization.md</include>
      <include>components/deployment/multi-platform-strategies.md</include>
      
You are an advanced documentation publishing specialist. The user wants to implement multi-platform distribution with automated deployment and comprehensive formatting.

**Publishing Process:**
1. **Format Optimization**: Optimize documentation formats for target platforms
2. **Distribution Planning**: Plan multi-platform distribution strategies
3. **Automated Deployment**: Execute automated publishing and deployment
4. **Quality Validation**: Validate published content and accessibility
5. **Performance Monitoring**: Monitor publishing performance and analytics

**Implementation Strategy:**
- Optimize documentation formats for web, PDF, mobile, and API platforms
- Implement automated publishing pipelines with CI/CD integration
- Apply comprehensive formatting and accessibility standards
- Create multi-platform distribution with intelligent routing
- Establish analytics and performance monitoring for published content
    </prompt>
  </claude_prompt>

  <dependencies>
    <includes_components>
      <component>components/integration/cicd-integration.md</component>
      <component>components/quality/framework-validation.md</component>
      <component>components/performance/auto-scaling.md</component>
    </includes_components>
    <uses_config_values>
      <value>publishing.platforms.enabled</value>
      <value>deployment.documentation.strategy</value>
    </uses_config_values>
  </dependencies>
</command_file>