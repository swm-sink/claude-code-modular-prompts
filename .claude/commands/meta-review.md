| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-11   | stable |

# /meta-review - Comprehensive Framework Audit & Validation

────────────────────────────────────────────────────────────────────────────────


────────────────────────────────────────────────────────────────────────────────

> **⚡ Clear Purpose**: Conducts comprehensive audit of entire framework for compliance, consistency, and effectiveness. Generates detailed compliance reports with specific remediation steps.

────────────────────────────────────────────────────────────────────────────────

```xml
<command purpose="Comprehensive framework audit and validation with compliance reporting and remediation guidance">
  
  <delegation target="modules/meta/framework-auditor.md">
    Framework structure analysis → Compliance validation → Quality gate verification → Pattern consistency check → Version validation → Temporal standards audit → Remediation planning → Audit reporting
  </delegation>
  
  <pattern_integration>
    <uses_pattern from="patterns/critical-thinking-pattern.md">Deep framework analysis approach</uses_pattern>
    <uses_pattern from="patterns/quality-validation-pattern.md">Systematic compliance verification</uses_pattern>
    <uses_pattern from="patterns/validation-pattern.md">Comprehensive validation methodology</uses_pattern>
    <uses_pattern from="patterns/performance-optimization-pattern.md">Parallel audit operations</uses_pattern>
    <uses_pattern from="patterns/error-recovery-pattern.md">Audit failure handling</uses_pattern>
    <uses_pattern from="patterns/documentation-pattern.md">Audit report generation</uses_pattern>
  </pattern_integration>
  
  <thinking_pattern enforcement="MANDATORY">
    <checkpoint id="1" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Analyze framework structure and scope for comprehensive audit planning</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What framework components need comprehensive audit coverage?
          - What compliance standards and quality gates must be verified?
          - How does audit scope connect to remediation planning and reporting?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Scope Question: What framework components (commands, modules, patterns) need audit coverage?]
          - [Standards Question: What compliance standards and quality gates apply to each component?]
          - [Consistency Question: What patterns and conventions must be verified across the framework?]
          - [Version Question: What version alignment and temporal standards need validation?]
          - [Quality Question: What quality metrics and performance standards must be measured?]
          - [Safety Question: What safety boundaries and immutable zones must be protected?]
          - [Integration Question: How do command-module integrations need validation?]
          - [Effectiveness Question: What usage patterns and success metrics indicate framework effectiveness?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this audit scope optimal for comprehensive framework validation?
          - What evidence supports this approach to compliance verification?
          - How will this analysis guide effective remediation planning?
        </decision_reasoning>
      </interleaved_thinking>
    </checkpoint>
    
    <checkpoint id="2" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Execute comprehensive framework audit with systematic compliance verification</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What systematic audit methodology ensures complete coverage?
          - What parallel operations optimize audit efficiency?
          - How does audit execution connect to evidence collection and validation?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Coverage Question: Are all framework components being audited systematically?]
          - [Standards Question: Are compliance checks being applied consistently across components?]
          - [Evidence Question: What evidence is being collected to support audit findings?]
          - [Efficiency Question: How can parallel operations optimize audit execution time?]
          - [Validation Question: Are audit results being validated for accuracy and completeness?]
          - [Safety Question: Are safety boundaries being respected during audit operations?]
          - [Integration Question: Are command-module integrations being validated properly?]
          - [Metrics Question: Are quality metrics being measured accurately?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this audit execution approach optimal for comprehensive validation?
          - What evidence supports the accuracy of audit findings?
          - How will this methodology ensure complete framework coverage?
        </decision_reasoning>
      </interleaved_thinking>
    </checkpoint>
    
    <checkpoint id="3" verify="true" enforcement="BLOCKING" thinking_mode="interleaved">
      <action>Generate compliance report with prioritized remediation recommendations</action>
      <interleaved_thinking enforcement="MANDATORY">
        <pre_analysis>
          - What audit findings require immediate attention vs. future optimization?
          - What remediation strategies align with framework safety boundaries?
          - How does reporting connect to actionable improvement workflows?
        </pre_analysis>
        <critical_thinking minimum_time="30_seconds">
          - [Priority Question: What audit findings represent critical vs. optimization opportunities?]
          - [Safety Question: What remediations respect framework safety boundaries and immutable zones?]
          - [Feasibility Question: What remediation steps are practically achievable within constraints?]
          - [Impact Question: What changes will provide maximum framework improvement?]
          - [Sequence Question: What order of remediation optimizes success probability?]
          - [Validation Question: How can remediation effectiveness be measured?]
          - [Integration Question: How do remediations integrate with existing framework evolution?]
          - [Documentation Question: What reporting format enables effective action planning?]
        </critical_thinking>
        <decision_reasoning>
          - Why is this remediation prioritization optimal for framework improvement?
          - What evidence supports these recommendations for safety and effectiveness?
          - How will this reporting approach enable systematic framework evolution?
        </decision_reasoning>
      </interleaved_thinking>
    </checkpoint>
  </thinking_pattern>
  
  <quality_gates enforcement="MANDATORY">
    <gate name="audit_coverage" requirement="100% framework component coverage">
      <validation>All commands, modules, and patterns must be audited</validation>
      <remediation>Expand audit scope to include missing components</remediation>
    </gate>
    <gate name="compliance_verification" requirement="All standards validated">
      <validation>Quality gates, safety boundaries, and conventions verified</validation>
      <remediation>Address compliance gaps through systematic remediation</remediation>
    </gate>
    <gate name="safety_preservation" requirement="No safety boundary violations">
      <validation>Immutable zones and safety constraints respected</validation>
      <remediation>Reject any recommendations that violate safety boundaries</remediation>
    </gate>
    <gate name="actionable_reporting" requirement="Clear remediation guidance">
      <validation>Report provides specific, actionable improvement steps</validation>
      <remediation>Enhance reporting with detailed implementation guidance</remediation>
    </gate>
  </quality_gates>
  
  <success_criteria>
    <criterion>Complete framework audit coverage with no missing components</criterion>
    <criterion>Accurate compliance verification with evidence-based findings</criterion>
    <criterion>Prioritized remediation recommendations within safety boundaries</criterion>
    <criterion>Actionable reporting that enables systematic framework improvement</criterion>
  </success_criteria>
  
  <restrictions>
    <restriction>READ-ONLY: No modifications to framework during audit</restriction>
    <restriction>SAFETY: Must respect all immutable zones and safety boundaries</restriction>
    <restriction>EVIDENCE: All findings must be supported by concrete evidence</restriction>
    <restriction>ACTIONABLE: Recommendations must be practically implementable</restriction>
  </restrictions>
</command>
```