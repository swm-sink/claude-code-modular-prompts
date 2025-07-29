# Claude Code Prompt Templates

**Ready-to-use Claude Code command templates** - Copy templates, adapt to your project automatically, and start using powerful Claude Code commands immediately.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-green.svg)](https://github.com/swm-sink/claude-code-modular-prompts/releases)

## Quick Start (2 Commands)

```bash
# 1. Copy templates to your project
./setup.sh /path/to/your/project

# 2. Auto-adapt to your project (in Claude Code)
/adapt-to-project
```

That's it! Your templates are now customized and ready to use.

## What You Get

**Proven Claude Code commands for:**
- Core development workflows (`/task`, `/help`, `/query`)
- API design and testing (`/api-design`, `/test-integration`)
- Database operations (`/db-migrate`, `/db-backup`)
- Security and quality checks (`/secure-audit`, `/quality-check`)
- DevOps and deployment (`/deploy`, `/ci-setup`)

**Plus supporting files:**
- Anti-pattern documentation to avoid common mistakes
- Best practices guides for Claude Code usage
- Reusable prompt components
- Configuration templates

## How It Works

1. **Setup copies templates** to your `.claude/` directory
2. **Adapt-to-project analyzes** your codebase and auto-customizes templates
3. **Start using commands** immediately in Claude Code conversations

## Example: Before & After

**Before (generic template):**
```markdown
# Deploy [INSERT_PROJECT_NAME] to [INSERT_DEPLOYMENT_TARGET]
Using [INSERT_CI_CD_PLATFORM] for [INSERT_TECH_STACK]...
```

**After auto-adaptation:**
```markdown
# Deploy MyApp to AWS ECS
Using GitHub Actions for React+Node.js...
```

## Installation Options

### Option 1: Direct Setup
```bash
git clone https://github.com/swm-sink/claude-code-modular-prompts
cd claude-code-modular-prompts
./setup.sh /path/to/your/project
```

### Option 2: As Submodule (for updates)
```bash
git submodule add https://github.com/swm-sink/claude-code-modular-prompts .claude-templates
cd .claude-templates
./setup.sh ../
```

## Available Commands

### Core Commands
- `/help` - Get help for any topic
- `/task` - Break down and execute complex tasks
- `/query` - Search and analyze your codebase
- `/auto` - Automated code generation

### Development Commands
- `/dev` - Development workflow assistance
- `/api-design` - Design and document APIs
- `/refactor` - Code refactoring guidance
- `/debug` - Debug assistance and troubleshooting

### Quality & Security
- `/test-unit` - Unit testing guidance
- `/test-integration` - Integration testing setup
- `/secure-audit` - Security audit workflows
- `/quality-check` - Code quality assessment

### DevOps & Deployment
- `/deploy` - Deployment assistance
- `/ci-setup` - CI/CD pipeline setup
- `/monitor` - Monitoring and alerting setup
- `/backup` - Backup and recovery procedures

## Supported Tech Stacks

Auto-adapts for:
- **Frontend**: React, Vue, Angular, Next.js, Svelte
- **Backend**: Node.js, Python, Java, Go, Ruby
- **Mobile**: React Native, Flutter
- **Data**: Jupyter, pandas, SQL databases
- **Cloud**: AWS, Azure, GCP, Docker, Kubernetes

## Adaptation Process

The `/adapt-to-project` command:
1. Analyzes your project structure and dependencies
2. Identifies your tech stack and frameworks
3. Customizes all templates with your project details
4. Removes unused templates for your stack
5. Validates the adaptation completed successfully

## Requirements

- Claude Code desktop application
- Git (for cloning and submodule support)
- Basic project structure (package.json, requirements.txt, etc.)

## Commands for Managing Templates

- `/adapt-to-project` - Auto-adapt all templates to your project
- `/validate-adaptation` - Check that adaptation completed successfully
- `/sync-templates` - Update templates from reference library
- `/reset-templates` - Reset to original state if needed

## Project Structure After Setup

```
your-project/
├── .claude/
│   ├── commands/          # Customized commands ready to use
│   ├── components/        # Reusable prompt components
│   ├── context/           # Best practices and anti-patterns
│   └── config/            # Project configuration
└── ...your project files
```

## Why This Saves Time

**Without templates**: Write Claude Code commands from scratch, learn through trial and error, repeat common patterns.

**With templates**: Start with proven patterns, auto-adapt to your project, use immediately.

## FAQ

**How long does setup take?**
5 minutes to copy templates, 2 minutes for auto-adaptation.

**Do I need all the templates?**
No - unused templates are automatically removed during adaptation.

**What if my project changes?**
Run `/adapt-to-project` again to re-customize templates.

**Can I modify the templates?**
Yes - they're copied to your project and fully customizable.

## Getting Help

- Start with `/help` command in Claude Code
- Check the `/docs` folder for detailed guides
- Review anti-patterns in `/context` folder to avoid common mistakes

## License

MIT - Use freely in your projects.

---

*Get started in 2 commands. No complexity, no manual work - just copy and adapt.*