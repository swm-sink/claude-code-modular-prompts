---
name: commit
description: Create a well-structured git commit
usage: "/commit [message]"
allowed-tools: [Bash]
---

# Create Git Commit

I'll analyze your changes and create a clear commit.

## Checking Changes
```bash
git status
git diff --staged
```

## Analyzing
- Files changed: [count]
- Type detected: [feat|fix|refactor|docs|test]
- Scope: [identified from files]

## Commit Message
```
[type]([scope]): [concise description]

[Optional body for complex changes]
```

## Creating Commit
```bash
git add [files]
git commit -m "[message]"
```

✅ Committed: [hash] [message]

**Next**: `git push` when ready