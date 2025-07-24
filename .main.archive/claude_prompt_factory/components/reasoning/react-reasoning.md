<prompt_component>
  <step name="ReAct Reasoning Framework">
    <description>
Advanced ReAct (Reasoning + Acting) framework that combines systematic reasoning with action planning. Provides iterative reasoning cycles with observation analysis and adaptive improvement for complex problem-solving tasks using Claude's natural reasoning capabilities.
    </description>
  </step>

  <react_reasoning>
    <reasoning_acting_cycle>
      <!-- ReAct iterative reasoning and action framework -->
      <core_react_cycle>
```

## ReAct Pattern Implementation

### Core ReAct Cycle
```xml
<react_cycle>
  <thought>Analyze the current situation and plan next steps</thought>
  <action>Take a specific, measurable action</action>
  <observation>Observe and analyze the results</observation>
  <evaluation>Assess progress and determine next iteration</evaluation>
</react_cycle>
```

### Native Prompting Pattern
When Claude enters ReAct mode, it follows this structured thinking:

**Thought Phase:**
- What do I know about the current situation?
- What are the possible approaches?
- What should I try first and why?

**Action Phase:**
- Execute a specific, concrete action
- Make the action observable and measurable
- Focus on one clear step at a time

**Observation Phase:**
- What happened as a result of my action?
- What new information did I gain?
- What worked and what didn't?

**Next Iteration:**
- Based on observations, what should I do next?
- How do I adjust my approach?
- Am I making progress toward the goal?

## Implementation Examples

### Code Analysis with ReAct
```xml
<react_example>
  <goal>Analyze React component for performance issues</goal>
  
  <iteration_1>
    <thought>I need to examine the component structure and identify potential performance bottlenecks. Let me start by looking at the render method and state usage.</thought>
    <action>Read the component file and identify render patterns, state variables, and prop usage.</action>
    <observation>The component has 15 state variables, uses inline object creation in render, and doesn't implement any memoization. This suggests unnecessary re-renders.</observation>
  </iteration_1>
  
  <iteration_2>
    <thought>Based on the observation, the main issues are excessive state and inline object creation. I should prioritize the most impactful optimization first.</thought>
    <action>Analyze which state variables actually trigger meaningful UI changes vs. internal tracking.</action>
    <observation>Only 3 of the 15 state variables affect the UI. The rest are used for internal calculations and could be refs or computed values.</observation>
  </iteration_2>
  
  <iteration_3>
    <thought>Now I have a clear optimization path: reduce state variables and implement memoization for expensive computations.</thought>
    <action>Generate specific refactoring recommendations with code examples.</action>
    <observation>Created actionable recommendations that could reduce re-renders by ~80% based on the analysis.</observation>
  </iteration_3>
</react_example>
```

### Problem Solving with ReAct
```xml
<react_problem_solving>
  <problem>Debug authentication flow that's failing intermittently</problem>
  
  <thought>Intermittent failures suggest a race condition, timing issue, or external dependency problem. I need to systematically narrow down the possible causes.</thought>
  <action>Examine the authentication flow code to identify async operations, external API calls, and potential race conditions.</action>
  <observation>The flow makes 3 sequential API calls with token refresh logic. There's no proper error handling for token refresh failures.</observation>
  
  <thought>Token refresh failures could cause intermittent auth issues. I should investigate the refresh mechanism and its error handling.</thought>
  <action>Analyze the token refresh logic and identify failure scenarios.</action>
  <observation>Token refresh has a 5-second timeout, but the API sometimes takes 6-8 seconds. Failed refreshes aren't retried, causing auth failures.</observation>
  
  <thought>This explains the intermittent failures. The solution is to increase timeout and add retry logic for token refresh.</thought>
  <action>Design a robust token refresh strategy with appropriate timeouts and retry mechanisms.</action>
  <observation>Proposed solution includes 15-second timeout, exponential backoff retry, and graceful fallback to re-authentication if refresh fails.</observation>
</react_problem_solving>
```

## Advanced ReAct Patterns

### Multi-Path Reasoning
```xml
<multi_path_react>
  <thought>I have multiple approaches to solve this problem. Let me explore them in parallel.</thought>
  
  <path_1>
    <action>Try approach A: Direct optimization</action>
    <observation>Works but has limitations</observation>
    <evaluation>Partially successful, continue developing</evaluation>
  </path_1>
  
  <path_2>
    <action>Try approach B: Architectural change</action>
    <observation>More complex but addresses root cause</observation>
    <evaluation>Promising, requires more investigation</evaluation>
  </path_2>
  
  <synthesis>
    <thought>Approach B addresses the root cause better, but I can incorporate the quick wins from approach A.</thought>
    <action>Combine the best elements of both approaches</action>
    <observation>Hybrid solution provides both immediate improvements and long-term architectural benefits</observation>
  </synthesis>
</multi_path_react>
```

### Self-Correcting ReAct
```xml
<self_correcting_react>
  <thought>My previous action didn't produce the expected result. I need to analyze what went wrong.</thought>
  <action>Review my previous reasoning and identify the flawed assumption.</action>
  <observation>I assumed the issue was in the frontend, but the error pattern suggests a backend problem.</observation>
  
  <correction>
    <thought>I need to shift focus to the backend and re-examine the problem from that perspective.</thought>
    <action>Analyze backend logs and API response patterns.</action>
    <observation>Backend is returning inconsistent response formats, causing frontend parsing errors.</observation>
  </correction>
  
  <validation>
    <thought>This backend inconsistency explains the original problem much better.</thought>
    <action>Verify this hypothesis by examining more backend responses.</action>
    <observation>Confirmed: 15% of API responses have malformed JSON structure.</observation>
  </validation>
</self_correcting_react>
```

## Integration Patterns

### With Other Components
ReAct reasoning enhances other components:

```xml
<integration_examples>
  <with_optimization>
    <thought>How can I optimize this prompt for better performance?</thought>
    <action>Apply OPRO optimization techniques</action>
    <observation>Performance improved by 30%</observation>
  </with_optimization>
  
  <with_constitutional>
    <thought>Does this solution align with our safety principles?</thought>
    <action>Apply constitutional AI evaluation</action>
    <observation>Solution is safe and ethical</observation>
  </with_constitutional>
  
  <with_meta_learning>
    <thought>How can I learn from this experience for future similar problems?</thought>
    <action>Extract generalizable patterns and add to knowledge base</action>
    <observation>Identified 3 reusable problem-solving patterns</observation>
  </with_meta_learning>
</integration_examples>
```

## Usage Instructions

### Activation
To activate ReAct reasoning in any command:
```xml
<activate_react>
  <mode>react_reasoning</mode>
  <structure>thought_action_observation</structure>
  <iterations>auto_determine</iterations>
</activate_react>
```

### Customization
```xml
<react_customization>
  <depth>shallow|medium|deep</depth>
  <focus>speed|thoroughness|creativity</focus>
  <output>steps_only|full_reasoning|summary</output>
</react_customization>
```

## Performance Characteristics

### Token Efficiency
- **Structured thinking** reduces redundant reasoning
- **Clear action steps** minimize unnecessary exploration
- **Observation focus** prevents analysis paralysis

### Quality Improvement
- **Iterative refinement** improves solution quality
- **Self-correction** catches and fixes errors
- **Multi-path exploration** finds better solutions

### Adaptability
- **Dynamic adjustment** based on problem complexity
- **Context-aware** reasoning appropriate to domain
- **Goal-oriented** maintains focus on objectives

      </adaptability>
    </reasoning_acting_cycle>
  </react_reasoning>

  <o>
ReAct reasoning framework completed with systematic problem-solving:

**Reasoning Cycles:** [count] iterative reasoning and action cycles completed
**Problem Resolution:** [percentage]% complex problem resolution success rate
**Action Planning:** [count] strategic actions planned and executed
**Observation Analysis:** [percentage]% observation accuracy and insight generation
**Adaptive Improvement:** [0-100] reasoning framework effectiveness rating
**Systematic Approach:** Advanced ReAct reasoning with native Claude capabilities
  </o>
</prompt_component> 