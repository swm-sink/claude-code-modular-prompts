# Claude Code Source Verification Checklist

## Purpose
This checklist ensures we only include sources that genuinely demonstrate Claude Code usage and native agentic abilities.

## Required Criteria (Must Have at Least 3)

### 1. Claude Code Structure Indicators
- [ ] Contains `.claude/` directory
- [ ] Has `CLAUDE.md` file
- [ ] Includes `.claude/settings.json`
- [ ] Has `.claude/commands/` with slash commands
- [ ] Uses `.claude/components/` or similar organization

### 2. Tool Usage Evidence
- [ ] Uses Read tool for file operations
- [ ] Uses Write/Edit tools for modifications
- [ ] Uses Bash tool for system commands
- [ ] Uses TodoWrite for task management
- [ ] Uses WebSearch or WebFetch
- [ ] Shows multi-tool workflows

### 3. Agentic Behavior Patterns
- [ ] Demonstrates autonomous planning
- [ ] Shows multi-step execution
- [ ] Includes self-correction/adaptation
- [ ] Has context-aware decision making
- [ ] Shows goal-directed behavior

### 4. Command/Prompt Engineering
- [ ] Custom slash commands defined
- [ ] System prompts configured
- [ ] Context engineering demonstrated
- [ ] Prompt templates provided
- [ ] Mode-based command design

## Exclusion Criteria (Automatic Disqualification)

### Not Claude Code If:
- [ ] Only uses Claude API directly
- [ ] Just chat interface usage
- [ ] No tool usage shown
- [ ] Generic LLM prompting
- [ ] Theoretical discussion only

## Quality Indicators (Nice to Have)

### High-Value Sources Show:
- [ ] Performance optimization techniques
- [ ] Error handling patterns
- [ ] Security considerations
- [ ] Integration with other tools
- [ ] Innovative use cases
- [ ] Measurable improvements
- [ ] Well-documented examples

## Verification Process

1. **Quick Scan** (30 seconds)
   - Check for `.claude/` or CLAUDE.md
   - Look for tool usage keywords
   - Identify Claude Code specific features

2. **Deep Check** (2-3 minutes)
   - Verify actual implementation
   - Confirm tool usage is real
   - Check code examples work
   - Note unique patterns

3. **Document** (2 minutes)
   - Fill out source template
   - Rate 1-5 based on value
   - Extract key patterns
   - Note verification status

## Red Flags to Watch For

1. **Theatrical Claims**
   - "Revolutionary approach"
   - "10x productivity boost"
   - Unverifiable metrics

2. **Shallow Usage**
   - Only mentions Claude Code
   - No actual implementation
   - Copy-pasted examples

3. **Outdated Content**
   - Pre-Claude Code era
   - Deprecated patterns
   - Old API versions

## Documentation Requirements

For each verified source:
- Clear verification status
- Specific tools/features used
- Actual code examples
- Practical insights
- Honest limitations

## Borderline Cases

If unsure about inclusion:
1. Does it teach something valuable about Claude Code?
2. Can the patterns be adapted for Claude Code use?
3. Is it high-quality LLM agent content applicable to Claude?

If yes to any → Include with clear notes about limitations