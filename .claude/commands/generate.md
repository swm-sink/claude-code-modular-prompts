---
name: generate
description: Generate code following project patterns
usage: "/generate [type] [name]"
tools: [Read, Write, Edit, Glob, Grep]
---

# Generate Command

## What I'll Do

I'll generate code that matches your project's patterns and conventions by:
1. Analyzing existing code patterns
2. Following your framework conventions
3. Maintaining consistent style
4. Creating appropriate tests

## What I Can Generate

- **component**: UI components
- **api**: API endpoints  
- **model**: Data models
- **service**: Service layers
- **test**: Test files
- **command**: Claude Code commands
- **config**: Configuration files

## My Approach

1. **Learn** - Study existing similar files
2. **Match** - Follow detected patterns
3. **Generate** - Create consistent code
4. **Test** - Add appropriate tests
5. **Integrate** - Update imports/exports

## Example Usage

```
/generate component UserProfile
/generate api /users/profile
/generate test UserService
/generate command analyze-deps
```

Tell me what to generate and I'll match your project's style.