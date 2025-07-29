# GitHub Workflow Documentation

## Project-Specific Git Configuration

This repository uses **repository-scoped** Git configuration to avoid conflicts with other projects.

### Current Configuration
```bash
# Repository-specific user settings (LOCAL ONLY)
user.name=swm-sink
user.email=stefan.menssink@gmail.com

# Repository-specific credential settings (LOCAL ONLY)
credential.https://github.com/swm-sink/claude-code-modular-prompts.git.username=swm-sink
credential.https://github.com/swm-sink/claude-code-modular-prompts.git.helper=store

# Remote repository
remote.origin.url=https://github.com/swm-sink/claude-code-modular-prompts.git
```

## Authentication Method

**⚠️ IMPORTANT: This project uses Personal Access Token (PAT) authentication only**

### Why PAT Only?
- **No GitHub CLI conflicts** with other projects
- **Repository-scoped credentials** prevent interference
- **Consistent authentication** across all git operations
- **Secure token management** with repository-specific storage

### Current PAT Configuration
- **Username**: `swm-sink`
- **Token**: [CONFIGURED LOCALLY - NOT STORED IN REPO]
- **Scope**: Repository-specific to avoid global credential conflicts

## GitHub Operations for This Project

### 1. Pushing Changes
```bash
# Standard push (uses stored PAT automatically)
git push origin main

# Force push (when needed)
git push --force-with-lease origin main
```

### 2. Pulling/Fetching
```bash
# Fetch latest changes
git fetch origin

# Pull and merge
git pull origin main
```

### 3. Credential Management
```bash
# View current credentials (repository-specific)
git config --list --local | grep credential

# Remove stored credentials if needed
git credential reject <<EOF
protocol=https
host=github.com
path=/swm-sink/claude-code-modular-prompts.git
EOF
```

## Setting Up on New Machine

If you need to set up this repository on a new machine:

```bash
# 1. Clone the repository
git clone https://github.com/swm-sink/claude-code-modular-prompts.git
cd claude-code-modular-prompts

# 2. Configure repository-specific user settings
git config user.name "swm-sink"
git config user.email "stefan.menssink@gmail.com"

# 3. Configure repository-specific credentials
git config credential.https://github.com/swm-sink/claude-code-modular-prompts.git.username swm-sink
git config credential.https://github.com/swm-sink/claude-code-modular-prompts.git.helper store

# 4. On first push/pull, enter your PAT when prompted for password
# Note: Never commit PAT tokens to the repository
```

## Security Notes

### PAT Storage
- Credentials are stored in local credential helper
- **Repository-scoped only** - won't affect other GitHub repositories
- Token is encrypted by the operating system's credential manager

### Best Practices
1. **Never commit PAT tokens** to the repository
2. **Use repository-scoped credentials** only
3. **Rotate PAT tokens** periodically
4. **Keep PAT tokens** in secure password manager
5. **Use minimal scopes** on PAT (repo access only)

## Troubleshooting

### Authentication Failed
If you get authentication errors:

```bash
# 1. Check current configuration
git config --list --local | grep credential

# 2. Clear stored credentials
git credential reject <<EOF
protocol=https
host=github.com
path=/swm-sink/claude-code-modular-prompts.git
EOF

# 3. Try push again (will prompt for new credentials)
git push origin main
```

### Multiple GitHub Accounts
This configuration ensures **zero conflicts** with other GitHub projects:

- **Global git config** remains unchanged
- **Other repositories** use their own credentials
- **Repository isolation** prevents cross-contamination

## Repository URLs

- **GitHub Repository**: https://github.com/swm-sink/claude-code-modular-prompts.git
- **Clone URL**: `git clone https://github.com/swm-sink/claude-code-modular-prompts.git`

---

*This documentation ensures clean separation from other GitHub projects and consistent authentication for this repository only.*