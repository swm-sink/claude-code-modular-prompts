<module name="prompt-engineering" version="1.0.0">
  
  <metadata>
    <description>Comprehensive prompt engineering implementation for systematic creation, evaluation, testing, and improvement of AI prompts</description>
    <category>development</category>
    <tokens>1800</tokens>
    <dependencies>
      <module>patterns/research-analysis.md</module>
      <module>quality/critical-thinking.md</module>
      <module>patterns/session-management.md</module>
    </dependencies>
  </metadata>
  
  <implementation>
    
    <workflow name="prompt_engineering_lifecycle">
      
      <phase name="initialization" order="1">
        <steps>
          <step>Parse command parameters and validate inputs</step>
          <step>Load appropriate templates based on prompt type</step>
          <step>Initialize session tracking for complex workflows</step>
          <step>Prepare output formatting and storage</step>
        </steps>
        <validation>
          <check>Valid subcommand provided</check>
          <check>Required parameters present</check>
          <check>Output paths accessible</check>
        </validation>
      </phase>
      
      <phase name="create" order="2" condition="subcommand==create">
        <steps>
          <step>Research best practices for prompt type and framework</step>
          <step>Analyze requirements and extract key objectives</step>
          <step>Select appropriate prompt patterns and structures</step>
          <step>Generate initial prompt with clear sections</step>
          <step>Add examples and edge case handling</step>
          <step>Include validation criteria and success metrics</step>
          <step>Document prompt purpose and usage guidelines</step>
        </steps>
        <patterns>
          <pattern name="system_prompt_structure">
            <sections>
              <section>Role and Identity</section>
              <section>Core Capabilities</section>
              <section>Behavioral Guidelines</section>
              <section>Output Formatting</section>
              <section>Examples and Anti-patterns</section>
              <section>Error Handling</section>
            </sections>
          </pattern>
          <pattern name="structured_format">
            <elements>
              <element>Clear task definition</element>
              <element>Input/output specifications</element>
              <element>Constraints and requirements</element>
              <element>Step-by-step instructions</element>
              <element>Quality criteria</element>
            </elements>
          </pattern>
        </patterns>
        <output>
          <file>prompts/{name}_{version}.md</file>
          <metadata>creation_timestamp, parameters, initial_metrics</metadata>
        </output>
      </phase>
      
      <phase name="evaluate" order="3" condition="subcommand==evaluate">
        <steps>
          <step>Load prompt file and parse structure</step>
          <step>Apply evaluation metrics framework</step>
          <step>Analyze clarity and specificity scores</step>
          <step>Check for ambiguities and contradictions</step>
          <step>Assess robustness against edge cases</step>
          <step>Compare against framework best practices</step>
          <step>Generate comprehensive evaluation report</step>
        </steps>
        <metrics>
          <metric name="clarity" weight="0.3">
            <factors>
              <factor>Unambiguous language usage</factor>
              <factor>Clear task boundaries</factor>
              <factor>Explicit success criteria</factor>
            </factors>
          </metric>
          <metric name="specificity" weight="0.3">
            <factors>
              <factor>Detailed instructions</factor>
              <factor>Concrete examples provided</factor>
              <factor>Edge cases addressed</factor>
            </factors>
          </metric>
          <metric name="robustness" weight="0.2">
            <factors>
              <factor>Error handling coverage</factor>
              <factor>Graceful degradation</factor>
              <factor>Input validation</factor>
            </factors>
          </metric>
          <metric name="effectiveness" weight="0.2">
            <factors>
              <factor>Goal achievement likelihood</factor>
              <factor>Output quality consistency</factor>
              <factor>Performance optimization</factor>
            </factors>
          </metric>
        </metrics>
        <output>
          <report>evaluation_{prompt_name}_{timestamp}.md</report>
          <scores>metrics.json</scores>
        </output>
      </phase>
      
      <phase name="test" order="4" condition="subcommand==test">
        <steps>
          <step>Load prompt and test configuration</step>
          <step>Generate test scenarios based on parameters</step>
          <step>Execute prompt with each test case</step>
          <step>Capture and analyze outputs</step>
          <step>Identify failure patterns and edge cases</step>
          <step>Calculate success rates and metrics</step>
          <step>Generate detailed test report</step>
        </steps>
        <scenarios>
          <category name="basic">
            <test>Standard use case execution</test>
            <test>Simple parameter variations</test>
            <test>Expected input formats</test>
          </category>
          <category name="edge_cases">
            <test>Boundary value inputs</test>
            <test>Malformed or incomplete data</test>
            <test>Extreme parameter combinations</test>
          </category>
          <category name="adversarial">
            <test>Prompt injection attempts</test>
            <test>Conflicting instructions</test>
            <test>Resource exhaustion scenarios</test>
          </category>
        </scenarios>
        <output>
          <results>test_results_{prompt_name}_{timestamp}.json</results>
          <report>test_report_{prompt_name}_{timestamp}.md</report>
        </output>
      </phase>
      
      <phase name="improve" order="5" condition="subcommand==improve">
        <steps>
          <step>Load evaluation and test results</step>
          <step>Identify improvement priorities</step>
          <step>Research solutions for identified issues</step>
          <step>Apply targeted improvements</step>
          <step>Preserve effective elements</step>
          <step>Re-evaluate improved version</step>
          <step>Document changes and rationale</step>
        </steps>
        <improvement_strategies>
          <strategy name="clarity_enhancement">
            <action>Simplify complex sentences</action>
            <action>Add explicit definitions</action>
            <action>Remove ambiguous terms</action>
          </strategy>
          <strategy name="specificity_increase">
            <action>Add concrete examples</action>
            <action>Define edge case behavior</action>
            <action>Specify exact output formats</action>
          </strategy>
          <strategy name="robustness_hardening">
            <action>Add error handling instructions</action>
            <action>Include validation steps</action>
            <action>Define fallback behaviors</action>
          </strategy>
        </improvement_strategies>
        <versioning>
          <format>semantic (major.minor.patch)</format>
          <changelog>Auto-generated from improvements</changelog>
        </versioning>
        <output>
          <improved_prompt>prompts/{name}_{new_version}.md</improved_prompt>
          <changelog>CHANGELOG_{prompt_name}.md</changelog>
        </output>
      </phase>
      
    </workflow>
    
    <error_handling>
      <error type="invalid_subcommand">
        <message>Invalid subcommand. Use: create, evaluate, test, or improve</message>
        <recovery>Display help documentation</recovery>
      </error>
      <error type="missing_parameters">
        <message>Required parameters missing: {parameters}</message>
        <recovery>Prompt for missing values</recovery>
      </error>
      <error type="file_not_found">
        <message>Prompt file not found: {filepath}</message>
        <recovery>Suggest file search or creation</recovery>
      </error>
      <error type="test_failure">
        <message>Test execution failed: {error}</message>
        <recovery>Log error, continue with remaining tests</recovery>
      </error>
    </error_handling>
    
    <integration_points>
      <integration name="template_library">
        <path>.claude/prompts/templates/</path>
        <purpose>Reusable prompt patterns and structures</purpose>
      </integration>
      <integration name="metrics_storage">
        <path>.claude/prompts/metrics/</path>
        <purpose>Historical metrics and improvement tracking</purpose>
      </integration>
      <integration name="session_tracking">
        <module>patterns/session-management.md</module>
        <purpose>Complex workflow coordination</purpose>
      </integration>
      <integration name="multi_agent_evaluation">
        <module>patterns/multi-agent.md</module>
        <purpose>Parallel evaluation from multiple expert perspectives</purpose>
      </integration>
      <integration name="quality_standards">
        <module>quality/production-standards.md</module>
        <purpose>Production-grade prompt quality enforcement</purpose>
      </integration>
      <integration name="tdd_methodology">
        <module>quality/tdd.md</module>
        <purpose>Test-driven prompt development methodology</purpose>
      </integration>
    </integration_points>
    
    <best_practices>
      <practice name="iterative_refinement">Always test before deploying</practice>
      <practice name="version_control">Track all prompt iterations</practice>
      <practice name="metric_driven">Use data to guide improvements</practice>
      <practice name="documentation">Maintain comprehensive usage guides</practice>
      <practice name="framework_specific">Optimize for target AI system</practice>
    </best_practices>
    
  </implementation>
  
  <usage_guidance>
    <quick_start>
      <step>Start with /prompt create for new prompts</step>
      <step>Use /prompt evaluate to assess existing prompts</step>
      <step>Run /prompt test to validate behavior</step>
      <step>Apply /prompt improve based on results</step>
    </quick_start>
    <advanced_workflows>
      <workflow>Continuous improvement cycles with automated testing</workflow>
      <workflow>A/B testing different prompt versions</workflow>
      <workflow>Framework migration and optimization</workflow>
    </advanced_workflows>
  </usage_guidance>
  
</module>