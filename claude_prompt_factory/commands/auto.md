# /auto - Intelligent Command Router

**Purpose**: Automatically analyze a user's request and route it to the most appropriate command.

## Usage
```bash
/auto "[your request in natural language]"
```

## Workflow

The `/auto` command uses a multi-stage process to determine the best course of action.

```xml
<auto_workflow>
  <step name="Analyze Request">
    <description>Parse the user's natural language request to determine the primary intent (e.g., 'fix a bug', 'add a feature', 'analyze code').</description>
  </step>
  
  <step name="Analyze Codebase Context">
    <description>Analyze the current state of the codebase to provide context for the request. This includes identifying the primary language, framework, and other relevant technologies.</description>
    <tool_usage>
      <tool>Codebase Analysis</tool>
      <description>Analyze the codebase to understand the technical context.</description>
    </tool_usage>
  </step>
  
  <step name="Select & Execute Command">
    <description>Based on the user's intent and the codebase context, select the most appropriate command from the library and execute it with the user's original request as the input. The routing logic will be transparently explained to the user.</description>
    <tool_usage>
      <tool>Command Execution</tool>
      <description>Execute the selected command.</description>
    </tool_usage>
  </step>
</auto_workflow>
```

## Routing Transparency

When routing, I'll explain my decision:
```
🤖 Analyzing your request...
✓ Detected: Bug fix for authentication
✓ Complexity: Low (single component)
✓ Routing to: /task command
✓ Reason: Focused fix with clear scope

Executing: /task "fix login validation error"
```

## Examples

### Example 1: Bug Fix
```bash
/auto "users can't log in after the last deployment"
```
**Expected Route**: `/task "fix the login issue"`

### Example 2: Feature Request
```bash
/auto "add dark mode to the application"
```
**Expected Route**: `/feature "add dark mode"`

### Example 3: Analysis
```bash
/auto "why is the API slow?"
```
**Expected Route**: `/query "analyze API performance"`

### Example 4: Refactoring
```bash
/auto "clean up the user service code"
```
**Expected Route**: `/dev refactor "cleanup the user service"`

## Configuration

The behavior of the `/auto` command can be configured in the `PROJECT_CONFIG.xml` file.

```xml
<command name="/auto">
  <setting name="explain_routing" value="true" description="Whether to explain the routing decision before executing the command." />
</command>
```