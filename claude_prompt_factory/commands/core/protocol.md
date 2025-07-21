---
description: Safe, rigorous protocol for critical changes with validation, rollback, and comprehensive testing
argument-hint: "[protocol_type] [risk_level]"
allowed-tools: Read, Write, Edit, Bash, Grep
---

# /protocol - Critical Change Protocol

Ultra-safe protocol for critical changes with comprehensive validation, rollback capabilities, and multi-stage testing.

## Usage
```bash
/protocol database                           # Database migration protocol
/protocol security                           # Security update protocol
/protocol production                         # Production deployment protocol
/protocol emergency                          # Emergency hotfix protocol
```

<claude_prompt>
  <prompt>
    You are executing a development task using the rigorous EPICCC protocol. Your behavior is configured by the `/protocol` settings in `PROJECT_CONFIG.xml`.

    You will proceed through the following enabled phases. For each phase, you will perform the described actions and think step-by-step.

    **EVALUATE Phase** (Enabled: ${command_settings.command#protocol.epiccc.evaluate.enabled})
    - Assess the task's impact, review dependencies, and define a clear scope.

    **PLAN Phase** (Enabled: ${command_settings.command#protocol.epiccc.plan.enabled})
    - Develop detailed implementation, testing, and rollback plans. Present these for approval.

    **IMPLEMENT Phase** (Enabled: ${command_settings.command#protocol.epiccc.implement.enabled})
    - Execute the coding tasks as per the plan, logging all progress.

    **CHECK Phase** (Enabled: ${command_settings.command#protocol.epiccc.check.enabled})
    - Perform a thorough validation of the implementation.
    - Run static analysis (Enabled: ${command_settings.command#protocol.epiccc.check.run_static_analysis}) using the `${scripts.script#lint}` command.
    - Run unit tests (Enabled: ${command_settings.command#protocol.epiccc.check.run_unit_tests}) using the `${scripts.script#test:unit}` command.
    - Run integration tests (Enabled: ${command_settings.command#protocol.epiccc.check.run_integration_tests}) using the `${scripts.script#test:integration}` command.
    - Run security scan (Enabled: ${command_settings.command#protocol.epiccc.check.run_security_scan}) using the `${scripts.script#security:scan}` command.
    - Request peer review (Enabled: ${command_settings.command#protocol.epiccc.check.request_peer_review}) by pausing and asking for human approval.

    **COMMIT Phase** (Enabled: ${command_settings.command#protocol.epiccc.commit.enabled})
    - After all checks pass, generate a conventional commit message and commit the changes.

    **CONTINUE Phase** (Enabled: ${command_settings.command#protocol.epiccc.continue.enabled})
    - Assess if the goal is fully met. If not, spawn a new EPICCC cycle to address the remaining work.

    Begin with the EVALUATE phase.
  </prompt>
</claude_prompt>

<dependencies>
  <uses_config_values>
    <value>command_settings.command#protocol.epiccc.evaluate.enabled</value>
    <value>command_settings.command#protocol.epiccc.plan.enabled</value>
    <value>command_settings.command#protocol.epiccc.implement.enabled</value>
    <value>command_settings.command#protocol.epiccc.check.enabled</value>
    <value>command_settings.command#protocol.epiccc.check.run_static_analysis</value>
    <value>command_settings.command#protocol.epiccc.check.run_unit_tests</value>
    <value>command_settings.command#protocol.epiccc.check.run_integration_tests</value>
    <value>command_settings.command#protocol.epiccc.check.run_security_scan</value>
    <value>command_settings.command#protocol.epiccc.check.request_peer_review</value>
    <value>command_settings.command#protocol.epiccc.commit.enabled</value>
    <value>command_settings.command#protocol.epiccc.continue.enabled</value>
    <value>scripts.script#lint</value>
    <value>scripts.script#test:unit</value>
    <value>scripts.script#test:integration</value>
    <value>scripts.script#security:scan</value>
  </uses_config_values>
</dependencies> 