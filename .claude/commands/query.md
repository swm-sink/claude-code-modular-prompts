<command purpose="Research and analysis with zero modifications - understanding before action">
  
  <delegation target="modules/development/research-analysis.md">
    This command delegates ALL implementation to the research analysis module which provides comprehensive read-only codebase investigation, architecture mapping, and pattern discovery with guaranteed zero modifications.
  </delegation>
  
  <module_integration>
    <primary_module>modules/development/research-analysis.md</primary_module>
    <supporting_modules>
      <module>modules/patterns/tool-usage.md</module>
      <module>modules/quality/critical-thinking.md</module>
      <module>modules/security/audit.md</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="basic">/query "How does the authentication system work?"</example>
    <example type="architecture">/query "What is the current microservice architecture?"</example>
    <example type="patterns">/query "Find all uses of the Repository pattern"</example>
    <example type="security">/query "Identify potential security vulnerabilities"</example>
    <example type="performance">/query "Find performance bottlenecks in API"</example>
    <example type="technical_debt">/query "Assess technical debt in codebase"</example>
  </usage_examples>
  
  <read_only_guarantee>
    <rule enforcement="absolute">NEVER modifies any files or creates commits</rule>
    <rule enforcement="absolute">Safe for production analysis and code reviews</rule>
    <rule enforcement="absolute">Perfect for understanding before modification</rule>
  </read_only_guarantee>
  
  <strict_enforcement target="zero_modifications">
    <primary_rule>MUST maintain absolute read-only guarantee - zero file modifications</primary_rule>
    <verification>No file writes, commits, or changes permitted during execution</verification>
    <consequence>Any modification attempt violates query command contract</consequence>
  </strict_enforcement>
  
  <reference>
    See modules/development/research-analysis.md for complete implementation details including search strategies, analysis patterns, and output formatting for comprehensive codebase understanding.
  </reference>
  
</command>