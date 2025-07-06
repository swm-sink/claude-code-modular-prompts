<command name="swarm" purpose="Multi-agent orchestration for complex systems with automatic session management">
  
  <delegation target="modules/patterns/multi-agent.md">
    This command delegates ALL implementation to the multi-agent patterns module which provides comprehensive orchestration using native Task() and Batch() patterns with mandatory session creation and intelligent coordination.
  </delegation>
  
  <module_integration>
    <primary_module>modules/patterns/multi-agent.md</primary_module>
    <supporting_modules>
      <module>modules/patterns/session-management.md</module>
      <module>modules/quality/production-standards.md</module>
      <module>modules/security/audit.md</module>
      <module>modules/development/protocol-enforcement.md</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="basic">/swarm "Build microservices e-commerce platform"</example>
    <example type="performance">/swarm "Optimize entire application for 10x scale"</example>
    <example type="migration">/swarm "Migrate legacy monolith to cloud-native microservices"</example>
    <example type="integration">/swarm "Build real-time notification system with WebSockets and Redis"</example>
  </usage_examples>
  
  <trigger_conditions>
    <condition type="complexity">Multi-component systems with ≥3 specialized areas</condition>
    <condition type="architecture">System architecture and large-scale refactoring</condition>
    <condition type="enterprise">Enterprise integrations with multiple touchpoints</condition>
    <condition type="optimization">Performance optimization across multiple layers</condition>
  </trigger_conditions>
  
  <strict_enforcement target="session_requirement">
    <primary_rule>MUST create GitHub session for ALL /swarm executions</primary_rule>
    <verification>Session creation is mandatory before any multi-agent work begins</verification>
    <consequence>No /swarm execution permitted without session tracking and coordination</consequence>
  </strict_enforcement>
  
  <reference>
    See modules/patterns/multi-agent.md for complete implementation details including Task() and Batch() patterns, session coordination, and quality gate enforcement across all agents.
  </reference>
  
</command>
