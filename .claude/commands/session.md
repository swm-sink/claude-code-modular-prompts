| version | last_updated | status |
|---------|--------------|--------|
| 2.3.1   | 2025-07-08   | stable |

# /session - AI session management via GitHub Issues

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="AI session management via GitHub Issues with context preservation">
  
  <delegation target="modules/patterns/session-management.md">
    Create issue → Track progress → Update status → Link artifacts → Complete with summary
  </delegation>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING">
      <action>Determine session type and TDD tracking requirements</action>
      <critical_thinking>
        - What type of session operation is requested?
        - Does this session involve code changes requiring TDD tracking?
        - Should I document TDD compliance status in the session?
        - Will this session coordinate multiple TDD-enforced tasks?
      </critical_thinking>
      <output_format>SESSION_TYPE: [start/update/complete/view] (TDD tracking: [required/optional/none])</output_format>
      <validation>Session type identified with appropriate TDD tracking level</validation>
      <enforcement>BLOCK if session type unclear or TDD tracking needs unidentified</enforcement>
    </checkpoint>
    <checkpoint id="2" verify="true" enforcement="BLOCKING">
      <action>Create or manage GitHub issue with TDD progress tracking</action>
      <critical_thinking>
        - Should the issue template include TDD compliance checkboxes?
        - How do I track TDD progress across multiple work sessions?
        - Should I link to test files and coverage reports?
        - Does the session need TDD coordination between team members?
      </critical_thinking>
      <output_format>GITHUB_ISSUE: #[number] with TDD tracking [enabled/documented]</output_format>
      <validation>Issue created/updated with appropriate TDD progress tracking</validation>
      <enforcement>VERIFY TDD tracking elements included in session documentation</enforcement>
    </checkpoint>
    <checkpoint id="3" verify="true" enforcement="BLOCKING">
      <action>Update session progress with TDD compliance status</action>
      <critical_thinking>
        - What TDD milestones have been completed since last update?
        - Are test coverage metrics improving appropriately?
        - Should I document any TDD challenges or blockers?
        - How does TDD progress align with overall session goals?
      </critical_thinking>
      <output_format>PROGRESS_UPDATE: [milestones] with TDD status [compliant/in-progress/blocked]</output_format>
      <validation>Progress update includes comprehensive TDD compliance documentation</validation>
      <enforcement>ENSURE TDD progress documented with specific metrics and evidence</enforcement>
    </checkpoint>
    <checkpoint id="4" verify="true" enforcement="BLOCKING">
      <action>Link artifacts with TDD evidence and documentation</action>
      <critical_thinking>
        - Which commits demonstrate TDD compliance (tests-first)?
        - Should I link to test files and coverage reports?
        - Are PRs properly documenting TDD evidence?
        - How can I preserve TDD methodology for future sessions?
      </critical_thinking>
      <output_format>ARTIFACT_LINKING: Commits, PRs, tests linked with TDD evidence</output_format>
      <validation>All relevant TDD artifacts properly linked and documented</validation>
      <enforcement>VERIFY TDD evidence accessible through session artifacts</enforcement>
    </checkpoint>
    <checkpoint id="5" verify="true" enforcement="BLOCKING">
      <action>Complete session with TDD lessons learned and compliance summary</action>
      <critical_thinking>
        - What TDD practices worked well in this session?
        - What TDD challenges were encountered and how resolved?
        - Is final test coverage meeting quality standards?
        - What TDD improvements should be applied to future sessions?
      </critical_thinking>
      <output_format>SESSION_COMPLETION: Summary with TDD compliance [verified/documented]</output_format>
      <validation>Session completion includes comprehensive TDD analysis and lessons</validation>
      <enforcement>BLOCK completion if TDD compliance not verified and documented</enforcement>
    </checkpoint>
  </thinking_pattern>
  
  <module_integration>
    <primary_module>modules/patterns/session-management.md</primary_module>
    <supporting_modules>
      <module>modules/patterns/git-operations.md for commit linking</module>
      <module>modules/quality/production-standards.md for compliance tracking</module>
      <module>modules/patterns/multi-agent.md for swarm coordination</module>
    </supporting_modules>
  </module_integration>
  
  <usage_examples>
    <example type="start">/session start "Implement OAuth2 authentication" # Creates #124</example>
    <example type="update">/session update "Completed user model, TDD tests passing"</example>
    <example type="link">/session link PR-456 # Links PR to current session</example>
    <example type="complete">/session complete "OAuth2 fully implemented with 95% coverage"</example>
    <example type="view">/session view 123 # Shows full session history</example>
  </usage_examples>
  
  <github_integration>
    <feature>Creates GitHub issues with AI session template</feature>
    <feature>Manages labels programmatically (ai-session, active, completed)</feature>
    <feature>Links commits and PRs automatically</feature>
    <feature>Provides searchable session history</feature>
    <feature>Zero external dependencies - pure GitHub CLI</feature>
  </github_integration>
  
  <strict_enforcement target="session_tracking">
    <primary_rule>Multi-agent work MUST use session tracking for coordination</primary_rule>
    <verification>Complex tasks automatically prompt for session creation</verification>
    <consequence>Session-less multi-agent work creates coordination failures</consequence>
  </strict_enforcement>
  
  <reference>
    See modules/patterns/session-management.md for complete implementation details including GitHub CLI operations, session templates, workflow integration, and team coordination patterns.
  </reference>
  
  <tdd_integration enforcement="MANDATORY">
    <session_tdd_tracking>Document TDD progress and compliance in all development sessions</session_tdd_tracking>
    <test_artifact_linking>Link test files, coverage reports, and TDD evidence to sessions</test_artifact_linking>
    <methodology_preservation>Preserve TDD methodology decisions and lessons learned</methodology_preservation>
    <validation>Reference quality/tdd.md#session_tracking for TDD session management</validation>
    <blocking_conditions>
      <condition>Development session lacks TDD progress tracking</condition>
      <condition>Session completion without TDD compliance verification</condition>
      <condition>Artifacts missing TDD evidence or test links</condition>
      <condition>Multi-agent coordination without TDD synchronization</condition>
    </blocking_conditions>
  </tdd_integration>
  
  <module_execution enforcement="MANDATORY">
    <core_stack order="sequential">
      <module>quality/critical-thinking.md - 30-second analysis before session operations</module>
      <module>patterns/session-management.md - GitHub issue management and tracking</module>
      <module>quality/tdd.md - TDD progress tracking and compliance documentation</module>
      <module>patterns/git-operations.md - Artifact linking and version control integration</module>
    </core_stack>
    <contextual_modules>
      <conditional module="quality/production-standards.md" condition="development_session"/>
      <conditional module="patterns/multi-agent.md" condition="swarm_coordination"/>
      <conditional module="context/restore-session.md" condition="session_resumption"/>
    </contextual_modules>
  </module_execution>
  
  <pattern_usage>
    • Implements issue_tracking pattern from pattern-library.md
    • Uses explicit_validation for session operations
    • Applies single_responsibility pattern
    • Leverages graceful_degradation for error handling
    
    See modules/patterns/pattern-library.md for pattern details
    See modules/patterns/session-management.md for full implementation
  </pattern_usage>
  
</command>
```