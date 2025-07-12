# First Task - Real Code Change in 3 Minutes

> **Objective**: Execute your first real development task via the framework, including actual code modification and TDD workflow.

Now that you've experienced framework responsiveness in hello-world, let's make your first actual code change. This example guides you through a complete task workflow: analysis → test creation → implementation → validation.

## 🎯 3-Minute Real Development

### Prerequisites
- ✅ Completed [hello-world/](../hello-world/) successfully
- ✅ Framework responding to commands
- ✅ Basic PROJECT_CONFIG.xml customization

### Step 1: Setup Task Environment (30 seconds)

```bash
# Copy task-optimized configuration
cp /path/to/claude-code-modular-prompts/examples/quick-start/first-task/PROJECT_CONFIG.xml .

# Verify you have a source directory (create if needed)
mkdir -p src
ls src/
```

### Step 2: Define Your First Task (30 seconds)

```bash
# Use framework to analyze what would be a good first task
/query "analyze this project structure and suggest a simple, safe first task to implement"
```

**Framework will suggest**: A simple utility function, helper method, or basic improvement specific to your project.

### Step 3: Execute Task with TDD (2 minutes)

```bash
# Execute the suggested task using TDD workflow
/task "implement a simple string utility function that capitalizes the first letter of each word"
```

**What happens**:
1. **RED**: Framework creates failing test first
2. **GREEN**: Framework implements minimal code to pass test
3. **REFACTOR**: Framework improves code quality while keeping tests green

### Step 4: Validate Success (30 seconds)

```bash
# Verify the implementation
/query "show me what files were created and explain the implementation"

# Test the code (if applicable)
npm test  # or appropriate test command for your project
```

## ✅ Success Indicators

After completing this task, you should have:

- [ ] **New test file**: Test created before implementation (TDD RED phase)
- [ ] **Working implementation**: Code that passes the test (TDD GREEN phase)
- [ ] **Quality improvements**: Refactored code with good structure (TDD REFACTOR phase)
- [ ] **No broken functionality**: Existing code still works
- [ ] **Understanding of task workflow**: Clear grasp of framework development process

## 🔍 What Just Happened?

### TDD Workflow in Action
1. **Analysis**: Framework understood your request and project context
2. **Test-First**: Created failing test to define expected behavior
3. **Minimal Implementation**: Wrote just enough code to pass the test
4. **Quality Refactoring**: Improved code structure while maintaining test success
5. **Validation**: Confirmed implementation meets requirements

### Framework Intelligence
- **Context-Aware**: Suggestion matched your project type and structure
- **Safe Execution**: Made minimal, focused changes without affecting existing code
- **Quality-Focused**: Applied TDD principles automatically
- **Documentation**: Clear explanation of what was implemented and why

## 🚀 Try More Tasks

### Immediate Next Tasks (Choose One)

#### Easy: More Utilities
```bash
/task "add a function to format dates in a readable way"
/task "create a simple validation helper for email addresses"
/task "implement a basic logging utility"
```

#### Medium: Project Improvements
```bash
/task "add better error handling to the main function"
/task "create a configuration helper for environment variables"
/task "add input validation to existing functions"
```

#### Advanced: Feature Components
```bash
/task "create a reusable component for user input validation"
/task "implement a simple caching mechanism"
/task "add retry logic to network requests"
```

## 🔧 Customization Options

### Adjust Task Complexity

**For simpler tasks** (learning focus):
```xml
<test_first_enforcement>moderate</test_first_enforcement>
<threshold>70</threshold>
```

**For production tasks** (quality focus):
```xml
<test_first_enforcement>strict</test_first_enforcement>
<threshold>95</threshold>
```

### Different Programming Languages

**Python Tasks**:
```bash
/task "create a simple data validation decorator"
/task "implement a retry mechanism with exponential backoff"
```

**Go Tasks**:
```bash
/task "create a simple HTTP client wrapper"
/task "implement basic structured logging"
```

**TypeScript Tasks**:
```bash
/task "create a type-safe configuration interface"
/task "implement a simple state management utility"
```

## 🚨 Troubleshooting

### Task seems too complex?
```bash
# Ask for simpler alternatives
/query "suggest 3 very simple tasks appropriate for learning the framework"
```

### Tests failing?
```bash
# Let framework diagnose and fix
/task "fix the failing tests and ensure implementation is correct"
```

### Implementation doesn't match expectations?
```bash
# Ask for explanation and alternatives
/query "explain the current implementation and suggest improvements"
```

### Want to start over?
```bash
# Clean slate - remove generated files and try again
git status  # see what was created
# Remove unwanted files and retry with different task
```

## 💡 Learning Points

### Framework Capabilities You Just Used
- **Intelligent Task Analysis**: Framework understood vague requirements and made them specific
- **Automatic TDD**: Applied test-driven development without you needing to know TDD
- **Context Preservation**: Maintained understanding of your project throughout the workflow
- **Quality Gates**: Applied appropriate code quality standards automatically
- **Safe Execution**: Made changes without breaking existing functionality

### Development Workflow You Just Learned
- **Requirements Clarification**: Framework helps refine vague requests into specific tasks
- **Test-Driven Approach**: Tests created before implementation ensures better design
- **Incremental Development**: Small, focused changes reduce risk and improve quality
- **Validation and Feedback**: Immediate confirmation that changes work as expected

## 🎯 Next Steps

### Immediate (Next 5 Minutes)
- **Try another task**: Practice the workflow with a different implementation
- **Explore task variations**: Use different `/task` commands to see adaptation
- **Review what was created**: Understand the code and tests generated

### Next Level (Next 30 Minutes)
- **Move to [basic-feature/](../basic-feature/)**: Experience complete feature development
- **Explore [workflows/](../../workflows/)**: Learn real-world development patterns
- **Try `/feature` command**: Move from single tasks to complete features

### Advanced Learning
- **Study generated code**: Learn from framework's implementation choices
- **Modify and extend**: Build on what framework created
- **Experiment with quality settings**: Try different enforcement levels

## 📚 Related Concepts

- **TDD Fundamentals**: [docs/quality/tdd.md](../../../.claude/modules/quality/tdd.md)
- **Task Management**: [docs/development/task-management.md](../../../.claude/modules/development/task-management.md)
- **Quality Gates**: [docs/quality/universal-quality-gates.md](../../../.claude/modules/quality/universal-quality-gates.md)
- **Command Selection**: [docs/user-guide/commands/command-selection.md](../../../docs/user-guide/commands/command-selection.md)

---

**Checkpoint**: You just completed your first real development task via the framework! 🎉

**Ready for complete features?** Continue to [basic-feature/](../basic-feature/) for end-to-end feature development.

**Want to master workflows?** Explore [workflows/](../../workflows/) to see how professionals structure complex development work.