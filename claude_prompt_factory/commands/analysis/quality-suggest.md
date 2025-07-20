# /quality suggest - Quality Suggestion Command

**Purpose**: Generate a prioritized, actionable list of quality improvement suggestions with impact assessment and implementation guidance.

## Usage
```bash
/quality suggest [path]
```

## Workflow

The `/quality suggest` command follows a systematic process to generate high-quality improvement suggestions.

```xml
<suggestion_workflow>
  <step name="Analyze Code Quality">
    <description>Perform a comprehensive analysis of the codebase to identify areas for improvement in performance, maintainability, security, test coverage, and documentation.</description>
    <tool_usage>
      <tool>Parallel Grep/Glob/Read</tool>
      <description>Scan the codebase for anti-patterns, complexity, and other quality issues.</description>
    </tool_usage>
  </step>
  
  <step name="Prioritize Opportunities">
    <description>Prioritize the identified improvement opportunities based on their potential impact and the estimated effort required to implement them.</description>
  </step>
  
  <step name="Generate Suggestions">
    <description>Generate a clear, actionable list of suggestions, complete with code examples and implementation guidance.</description>
    <output>A prioritized list of improvement suggestions, organized by impact and effort.</output>
  </step>
</suggestion_workflow>
```

## Suggestion Output Format
```markdown
## Priority 1: High Impact, Low Effort (Quick Wins)
*   **Performance**: Cache the result of the `calculate_heavy_stuff()` function. (Estimated Effort: 2 hours)
*   **Maintainability**: Extract the validation logic from the `user_controller.py` into a separate helper function. (Estimated Effort: 1 hour)

## Priority 2: High Impact, High Effort (Strategic Improvements)
*   **Architecture**: Implement a dependency injection framework to decouple your services. (Estimated Effort: 2 days)
*   **Security**: Add a centralized input validation framework to protect against injection attacks. (Estimated Effort: 3 days)

## Code Examples
[Specific before/after code examples for each suggestion will be provided here.]
```
