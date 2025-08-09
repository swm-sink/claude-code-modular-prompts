---
name: deep-discovery-real
description: Actually analyze your project and generate working commands in 30-60 minutes
usage: "deep-discovery-real"
allowed-tools: [Read, Write, Edit, MultiEdit, Bash, Glob, Grep, LS, TodoWrite]
category: discovery
---

# Deep Discovery (Real Implementation)

## What This ACTUALLY Does

This command performs a real 30-60 minute consultation that:
1. **Analyzes** your actual project files
2. **Discovers** your specific patterns
3. **Generates** working commands tailored to your project
4. **Validates** that everything works

No templates. No placeholders. Real, working commands.

## The ACTUAL Implementation

### Phase 1: Technical Analysis (10-15 minutes)

```python
# This is what actually happens:

1. Framework Detection:
   framework = Read('package.json') or Read('requirements.txt') or Read('go.mod')
   
2. Structure Analysis:
   structure = LS('.') then Glob('**/*.{js,ts,py,go}')
   
3. Pattern Detection:
   patterns = Grep('import|require|from', '**/*.{js,ts,py}')
   naming = analyze_file_names(Glob('**/*'))
   
4. Test Analysis:
   tests = Glob('**/*.{test,spec}.*')
   test_framework = detect_from_imports(tests)
```

### Phase 2: Interactive Consultation (15-20 minutes)

```markdown
# Real questions based on discoveries:

"I detected React 18.2 with TypeScript. Is this correct?"
"I see you use kebab-case for files. Should generated commands follow this?"
"You have 47% test coverage. Should new components include tests?"
"I found both .tsx and .jsx files. Which should I use?"
```

### Phase 3: Command Generation (10-15 minutes)

```python
# ACTUAL generation that happens:

for pattern in discovered_patterns:
    if pattern.type == 'component':
        command = create_component_command(
            naming=pattern.naming,
            structure=pattern.structure,
            imports=pattern.imports,
            testing=pattern.testing
        )
        Write(f'.claude/commands/{command.name}.md', command.content)
```

### Phase 4: Validation (5-10 minutes)

```bash
# Test each generated command:
for command in generated_commands:
    test_result = execute_command_dry_run(command)
    if test_result.failed:
        fix_and_retry(command)
```

## Example: What ACTUALLY Gets Generated

### For a Real Next.js + TypeScript Project

After analyzing YOUR project, this command would generate:

```markdown
# .claude/commands/create-page.md
---
name: create-page
description: Create a Next.js page with your exact setup
usage: "create-page <name>"
allowed-tools: [Write, Read, MultiEdit]
---

# Create Next.js Page

This command creates pages matching YOUR project:
- Uses `/app` directory (detected App Router)
- TypeScript with your tsconfig settings
- Your Tailwind classes
- Your layout.tsx wrapper
- Your metadata pattern

## Implementation

When you run `/create-page about`, it will:

1. Create `app/about/page.tsx`:
   ```typescript
   // Your actual import pattern
   import { Metadata } from 'next'
   import { Container } from '@/components/ui/Container'
   
   export const metadata: Metadata = {
     title: 'About - YourApp',
     description: 'About page'
   }
   
   export default function AboutPage() {
     return (
       <Container>
         <h1 className="text-4xl font-bold">About</h1>
       </Container>
     )
   }
   ```

2. Create test file (because you test your pages):
   ```typescript
   // app/about/page.test.tsx
   import { render, screen } from '@testing-library/react'
   import AboutPage from './page'
   
   describe('AboutPage', () => {
     it('renders the about page', () => {
       render(<AboutPage />)
       expect(screen.getByText('About')).toBeInTheDocument()
     })
   })
   ```
```

## The Key Difference

### Old Approach (Templates)
```markdown
Create component at [COMPONENT_PATH]/[COMPONENT_NAME].[EXTENSION]
Using [FRAMEWORK] patterns with [TEST_FRAMEWORK]
```

### New Approach (Actual Generation)
```markdown
Create component at src/components/Button.tsx
Using React 18.2 with TypeScript and your exact imports
Including your jest+RTL test setup
Following your team's exact patterns
```

## How to Use This

```bash
# Run the real deep discovery
/deep-discovery-real

# You'll see:
"🔍 Analyzing your project structure..."
"📊 Found: Next.js 14.0.3, TypeScript, Tailwind, Jest"
"💬 Let me ask a few questions to understand your preferences..."

# Answer ~10 smart questions based on what was found

# Then:
"🚀 Generating 12 commands tailored to your project..."
"✅ Created: create-page, create-component, create-api-route..."
"🎉 Complete! Your commands are ready to use."

# Now you can immediately:
/create-page pricing
/create-component Button
/create-api-route users
# And they'll work EXACTLY like your team writes code
```

## Why This Works

1. **Uses Claude's Real Capabilities**: Read, Write, Grep - not imaginary engines
2. **Analyzes Actual Files**: Not theoretical patterns
3. **Generates Real Commands**: Not templates with placeholders
4. **Validates Everything**: Ensures it actually works
5. **Takes 30-60 Minutes**: But delivers immediate value

## Success Metrics

✅ Commands work on first try
✅ Match your exact patterns
✅ No manual customization needed
✅ Save hours of setup time
✅ Team consistency improved

This is what we should be building. Not YAML configurations. Not template libraries. Real, working command generation based on actual project analysis.