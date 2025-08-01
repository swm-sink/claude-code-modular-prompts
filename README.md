# Claude Code Modular Prompts - v2.0 Template Library

<!-- AI_METADATA_START -->
<ai_document_metadata>
  <document_type>documentation</document_type>
  <ai_consumption_priority>critical</ai_consumption_priority>
  <content_structure>markdown_body</content_structure>
  <file_path>/Users/smenssink/conductor/repo/claude-code-modular-prompts/lusaka/README.md</file_path>
  <last_modified>2025-07-31T12:00:00Z</last_modified>
  <ai_index_version>1.0</ai_index_version>
</ai_document_metadata>

<project_overview_metadata>
  <project_type>template_library</project_type>
  <version>2.0</version>
  <command_count>88</command_count>
  <component_count>91</component_count>
  <progressive_disclosure_support>true</progressive_disclosure_support>
  <orchestration_enabled>true</orchestration_enabled>
  <target_audience>claude_code_developers</target_audience>
</project_overview_metadata>

<ai_navigation>
  <discovery_metadata>
    <primary_discovery_path>user_documentation</primary_discovery_path>
    <quick_access_sections>
      <section ref="quick_start">30-second installation</section>
      <section ref="what_you_get">Template inventory</section>
      <section ref="progressive_disclosure">3-layer system</section>
      <section ref="installation">Setup instructions</section>
    </quick_access_sections>
  </discovery_metadata>
  
  <relationship_map>
    <related_documentation>
      <file type="guide" ref="SETUP.md" relation="installation_details"/>
      <file type="guide" ref="ADAPTATION-GUIDE.md" relation="customization_help"/>
      <file type="assessment" ref="ULTRATHINK-FRAMEWORK-ASSESSMENT.md" relation="value_proposition"/>
    </related_documentation>
    <key_commands>
      <command ref="quick-command" layer="1"/>
      <command ref="build-command" layer="2"/>
      <command ref="assemble-command" layer="3"/>
    </key_commands>
  </relationship_map>
</ai_navigation>

<context_engineering>
  <ai_understanding_scope>
    <scope_level>project</scope_level>
    <context_retention>session</context_retention>
    <memory_priority>9</memory_priority>
  </ai_understanding_scope>
  
  <user_journey_metadata>
    <entry_points>
      <point type="installation">setup.sh script</point>
      <point type="discovery">/help command</point>
      <point type="immediate_use">quick-command templates</point>
    </entry_points>
    <learning_progression>
      <stage level="1">Use auto-generation templates</stage>
      <stage level="2">Customize with guided options</stage>
      <stage level="3">Assemble custom components</stage>
    </learning_progression>
  </user_journey_metadata>
</context_engineering>
<!-- AI_METADATA_END -->

**Comprehensive collection of 88 Claude Code v2.0 command templates with orchestration support and 91 reusable components for rapid project customization.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-green.svg)](https://github.com/swm-sink/claude-code-modular-prompts/releases)

## 🚀 Quick Start (30 seconds)

```bash
# Install template library
./setup.sh /path/to/your/project

# Start using immediately (in Claude Code)
/help                              # See all commands
/task "add user authentication"    # Execute any development task
/analyze "why is my app slow?"     # Analyze code or problems
```

**Templates require customization - use guide commands for step-by-step help.**

## What You Get

**88 v2.0 Command Templates:**
- **Core Commands** (12): Essential development workflows with orchestration
- **Quality Commands** (12): Testing, validation, analysis tools with v2.0 features
- **Specialized Commands** (11): Advanced workflows and patterns with command chaining
- **Meta Commands** + others (53): Template adaptation, management, and specialized tools

**91 Reusable Components:**
- **Atomic Components** (21): Simple building blocks
- **Regular Components** (70): Complex reusable patterns

**v2.0 Template Library Features:**
- **Orchestration Support**: Commands can invoke other commands for complex workflows
- **Task-Based Prompting**: Clear task descriptions and implementation strategies
- **Enhanced Context**: Improved Claude understanding and response quality
- Manual customization guides with placeholder replacement
- Anti-pattern documentation (48+ documented pitfalls)
- Multiple integration methods (git submodule, direct copy, selective)
- Comprehensive testing and validation frameworks

## How It Works

1. **Import Templates**: Choose integration method (git submodule recommended)
2. **Customize**: Use guide commands like `/adapt-to-project` for customization checklists
3. **Replace Placeholders**: Manual find/replace of [INSERT_XXX] placeholders in your editor
4. **Validate**: Use `/validate-adaptation` to verify your customizations
5. **Maintain**: Use `/sync-from-reference` for updates from the template library

## Installation Methods

### Method 1: Git Submodule (Recommended)
```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-framework
cd .claude-framework && ./setup.sh
```

### Method 2: Direct Integration
```bash
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts && ./setup.sh ../your-project
```

### Method 3: Selective Copy
Choose specific commands/components to copy manually.

## Usage Examples

**Template Customization:**
```
/adapt-to-project           # Get customization checklist
/replace-placeholders       # See all placeholders to replace
/validate-adaptation        # Verify your customizations
```

**Command Template Usage:**
```
/task "implement authentication"    # Use customized task template
/test "run integration tests"       # Use customized test template  
/analyze "performance bottlenecks"  # Use customized analysis template
```

**Component Assembly:**
```
# Build custom commands from atomic components
# Copy from .claude/components/atomic/ into your slash commands
```

## Installation

**Recommended:**
```bash
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts
./setup-minimal.sh /path/to/your/project
```

**Or as git submodule:**
```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-templates
cd .claude-templates && ./setup-minimal.sh ../
```

## File Structure After Installation

```
your-project/
├── .claude/
│   ├── commands/
│   │   ├── help.md      # /help - Command guide
│   │   ├── task.md      # /task - Execute any development task
│   │   ├── analyze.md   # /analyze - Analyze code and problems
│   │   ├── review.md    # /review - Code review with suggestions  
│   │   ├── debug.md     # /debug - Debug issues and errors
│   │   ├── test.md      # /test - Generate and run tests
│   │   └── docs.md      # /docs - Create documentation
│   └── settings.json    # Claude Code configuration
└── CLAUDE.md            # Project memory (optional)
```

**Total: 8 files, ~50KB**

## Universal Compatibility

**Works with any programming language or framework:**
- JavaScript, TypeScript, Python, Java, Go, Rust, C#, PHP, Ruby
- React, Vue, Angular, Django, Spring, Laravel, Rails, Express
- Any project type: web apps, APIs, mobile apps, desktop apps, scripts

## Requirements

- Claude Code desktop application
- Git (for cloning)

## Why This Saves Time

**Without these commands**: Write Claude Code prompts from scratch, learn through trial and error, repeat common patterns.

**With these commands**: Use proven patterns immediately, commands adapt automatically to your project.

## FAQ

**Do these commands work with my tech stack?**
Yes - they automatically adapt to any programming language or framework.

**Can I add more commands later?**
Yes - you can copy additional commands from the full template library if needed.

**What if I need project-specific customization?**
The commands work universally, but you can modify them in your `.claude/commands/` directory.

## Getting Help

- Start with `/help` command in Claude Code
- Use `/task "what you want to accomplish"` for most development needs
- Commands provide detailed examples and explanations

## Advanced Usage

**Need more commands?** This repo also contains:

1. **Template Library**: 81+ additional command templates that require manual customization. See `./setup.sh` for details.

2. **Atomic Components**: 21 simple building blocks (5-10 lines each) for creating custom commands:
   - Input validation, output formatting, error handling
   - File operations, search functionality, progress indicators  
   - See `.claude/COMPONENT-ASSEMBLY-GUIDE.md` for usage

**Note**: The template library and components require manual work. Only the 7 core commands work immediately without customization.

## License

MIT - Use freely in your projects.

---

*7 essential commands that work immediately with any programming language or framework.*