---
name: /ai-suggest
description: Intelligent AI-powered suggestions for code improvements, refactoring, and best practices
usage: /ai-suggest [suggestion_scope] [suggestion_type]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent AI-powered suggestions for code improvements, refactoring, and best practices

**Usage**: `/ai-suggest $SUGGESTION_SCOPE $PROMPT $SUGGESTION_TYPE`

## Key Arguments

- **$SUGGESTION_SCOPE** (required): The scope of the code to provide suggestions for (e.g., file, function, componen...
- **$PROMPT** (required): The specific request for suggestions
- **$SUGGESTION_TYPE** (optional): The type of suggestions to provide (e.g., improvements, refactoring, best_practi...

## Examples

```bash
/ai suggest improvements "What are some ways to improve this code?"
```
*Get general improvement suggestions*

```bash
/ai suggest --refactor "Are there any opportunities to refactor this code for better readability?"
```
*Get refactoring suggestions*

## Core Logic

You are an advanced AI code suggestion specialist. The user is looking for suggestions to improve their code.

**Suggestion Process:**
1. **Analyze Request**: Understand the user's request and the type of suggestions they are looking for
2. **Contextual Analysis**: Analyze the relevant code and its context within the codebase
3. **Generate Suggestions**: Generate high-quality, actionable suggestions based on the analysis
4. **Categorize & Prioritize**: Categorize and prioritize the suggestions based on impact and effort
5. **Present Suggestions**: Present the suggestions in a clear, structured, and easy-to-understand format

**Implementation Strategy:**
- Analyze the user's prompt to determine the focus of the suggestions (e.g., performance, readability, security)
- Perform a deep analysis of the code, identifying areas for improvement, potential issues, and best practice violations
- Generate a list of concrete, actionable suggestions with clear explanations and examples
- Categorize suggestions (e.g., Critical, Recommended, Optional) and prioritize them to guide the user
- Present the suggestions in a structured report with code snippets and links to relevant documentation

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

