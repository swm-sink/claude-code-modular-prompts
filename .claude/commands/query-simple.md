# /query - Understand Before You Build

You research and analyze systems without making changes.

## RESEARCH WORKFLOW:

### 1. DEFINE QUESTIONS (30 seconds)
- What exactly do you need to understand?
- What files/components are involved?

### 2. GATHER INFORMATION (3 minutes)
- Use parallel reads: `Read("file1"), Read("file2"), Read("file3")`
- Search patterns: `Grep("pattern", pattern="*.py", output_mode="content")`
- Map dependencies: `Glob("**/*.js")` then analyze imports

### 3. ANALYZE PATTERNS (2 minutes)
- Identify architectural patterns
- Map data flow and dependencies
- Note security and performance implications

### 4. DOCUMENT FINDINGS (1 minute)
- Clear summary of how system works
- Key files and their roles
- Recommendations for next steps

## READ-ONLY RULES:
- Never modify any files
- Use parallel tool calls for efficiency
- Provide actionable insights
- Always suggest next command

## OUTPUT FORMAT:
```
## SYSTEM ANALYSIS: [topic]

**How it works:** [2-3 sentence summary]

**Key Components:**
- file1.py: Handles login logic
- file2.js: Frontend validation
- config.json: Auth settings

**Architecture Pattern:** [pattern name and description]

**Security Notes:** [key security considerations]

**Next Steps:** 
- Use `/task` to fix specific issues
- Use `/docs` to document the flow
```

## EXAMPLE:
`/query "How does user authentication work in this system?"`

---

**NOW RESEARCH: $ARGUMENTS**