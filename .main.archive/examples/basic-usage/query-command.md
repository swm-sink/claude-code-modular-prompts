# Using the `/query` Command

## Scenario

You're a new developer on a project, and you've been tasked with fixing a bug in the authentication system. Before you start making changes, you want to understand how authentication is currently handled.

## The Problem

You need to:
1. Understand the authentication flow
2. Locate relevant code files
3. Identify potential security considerations
4. Get oriented without making any changes

## The Solution: `/query`

The `/query` command is perfect for exploring and understanding code without making modifications.

### Example Usage

```bash
/query "how does user authentication work in this application?"
```

### What the Command Does

1. **Parallel Search**: Uses multiple search strategies to find authentication-related code
2. **Context Gathering**: Reads relevant files and builds understanding
3. **Analysis**: Identifies patterns, security considerations, and architecture
4. **Reporting**: Provides a structured summary of findings

### Expected Output

The command will provide:

- **Authentication Flow**: Step-by-step breakdown of the login process
- **Key Files**: List of files involved in authentication
- **Security Patterns**: Identification of security measures in place
- **Dependencies**: External libraries or services used
- **Potential Issues**: Areas that might need attention

### Follow-up Actions

Based on the query results, you might:

```bash
# Focus on a specific area
/query "what validation happens during login?"

# Start targeted development
/task "fix email validation in login form"

# Use safe protocol for critical changes
/protocol "update password hashing algorithm"
```

## Why This Works

The `/query` command is designed to:
- Be **non-destructive** - never modifies code
- Provide **comprehensive analysis** - searches broadly then focuses
- Generate **actionable insights** - gives you next steps
- **Save time** - avoids manual code exploration

---
*This example demonstrates the framework's philosophy: start with understanding, then take focused action.* 