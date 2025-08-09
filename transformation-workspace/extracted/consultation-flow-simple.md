# Consultation Flow - Claude Native Implementation
# Extracted from 382-line YAML → 50-line prompt template
# Web Validated: 2025-01-09

## 30-60 Minute Deep Consultation Structure

### Core Philosophy
"Have a conversation with an expert consultant who learns your project deeply"
- Adaptive questioning based on responses
- User can skip/pause/deep-dive at any point
- Show growing understanding in real-time

### Implementation with Claude Native Tools

```markdown
## Stage 1: Project Discovery (5-7 minutes)

Use these tools to understand the project:
1. Glob("**/*.{json,yaml,toml,xml}") - Find config files
2. Read("package.json" or "requirements.txt" or "pom.xml") - Identify tech stack
3. LS("/") - Understand project structure
4. Grep("test|spec" with file pattern) - Find testing approach

Ask based on discoveries:
- "I see you're using [framework]. How do you structure [pattern]?"
- "Your package.json shows [deps]. What's your approach to [related concept]?"
- "I notice [pattern] in your codebase. Is this your standard approach?"

## Stage 2: Technical Deep Dive (5-7 minutes)

Use tools to explore architecture:
1. Grep("class|interface|function export") - Find main components
2. Read key architecture files found
3. Search for patterns: MVC, services, controllers, models

Adaptive questions based on findings:
- For React: "How do you handle state management with [found library]?"
- For Node: "I see Express/Fastify. What's your API structure?"
- For Python: "Using [Django/Flask/FastAPI]. How do you organize [pattern]?"

## Stage 3: Domain Extraction (7-10 minutes)

Extract business logic:
1. Grep("entity|model|schema") - Find domain objects
2. Read API routes or controllers for workflows
3. Search for validation, business rules

Map the domain:
- "Your models show [entities]. How do these relate?"
- "I found these API endpoints. What are the main user flows?"
- "These validation rules suggest [business logic]. Is this correct?"

## Stage 4: Preference Learning (3-5 minutes)

Understand team patterns:
1. Grep("TODO|FIXME|HACK") - Find pain points
2. Read recent commits for patterns
3. Check documentation style

Learn preferences:
- "I notice you prefer [pattern]. Should Claude follow this?"
- "Your TODOs mention [issue]. How should we handle this?"
- "Your commit style is [pattern]. Should I match this?"
```

### Session Management (Simple JSON)

```json
{
  "session_id": "consultation-2025-01-09",
  "stage": 1,
  "discoveries": {
    "tech_stack": ["framework", "libraries"],
    "patterns": ["architecture", "testing"],
    "domain": ["entities", "workflows"],
    "preferences": ["style", "conventions"]
  },
  "next_questions": ["adaptive based on discoveries"],
  "time_spent": 0,
  "can_resume": true
}
```

### Key Simplifications from Original YAML

1. **From**: 382 lines of YAML configuration
   **To**: 50 lines of executable prompts using Claude tools

2. **From**: Complex state machines and transitions
   **To**: Simple JSON session file

3. **From**: Hardcoded question trees
   **To**: Adaptive questions based on actual code analysis

4. **From**: Abstract workflow definitions
   **To**: Direct tool usage (Read, Grep, Glob)

5. **From**: Theoretical frameworks
   **To**: Practical discovery through code examination

This approach uses Claude's intelligence to adapt rather than scripted logic.