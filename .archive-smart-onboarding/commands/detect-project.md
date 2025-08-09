---
name: /detect-project
description: Smart project detection engine - analyzes everything automatically without asking questions
usage: "/detect-project [--json|--detailed|--summary]"
allowed-tools: [Read, Glob, Grep, LS, Bash]
---

# 🔍 Smart Project Detection Engine

I analyze your project to understand everything about it WITHOUT asking questions. This is the engine behind the intelligent onboarding system.

## What I Detect

### 1. Framework & Language
```javascript
detectFromFiles([
  'package.json',        // Node.js projects
  'requirements.txt',    // Python projects  
  'Gemfile',            // Ruby projects
  'go.mod',             // Go projects
  'Cargo.toml',         // Rust projects
  'pom.xml',            // Java projects
  'composer.json',      // PHP projects
  'pubspec.yaml',       // Flutter projects
  'mix.exs',            // Elixir projects
  'build.gradle',       // Gradle projects
])
```

### 2. Project Patterns
- **Component Structure**: How you organize components
- **File Naming**: camelCase, PascalCase, kebab-case
- **Directory Layout**: Feature-based, layer-based, domain-driven
- **Import Style**: Relative vs absolute, aliases used
- **Code Style**: Formatting, linting rules

### 3. Testing Approach
- **Framework**: Jest, Mocha, Pytest, RSpec, etc.
- **Structure**: Where tests live, naming convention
- **Coverage**: Current coverage, requirements
- **Approach**: Unit, integration, E2E balance

### 4. Team Conventions
- **Git Workflow**: Branch naming, commit format
- **Review Process**: PR templates, approval requirements  
- **Documentation**: Style, location, completeness
- **Communication**: Comments, PR descriptions

### 5. Development Workflow
- **Build System**: Webpack, Vite, Rollup, etc.
- **CI/CD**: GitHub Actions, CircleCI, Jenkins
- **Deployment**: Vercel, AWS, Heroku, Docker
- **Monitoring**: Sentry, LogRocket, DataDog

## Detection Process

### Phase 1: File System Scan
```bash
# What I'm doing behind the scenes:
find . -type f -name "package.json" 2>/dev/null
find . -type f -name "*.ts" -o -name "*.tsx" | head -20
find . -type f -name "*.test.*" -o -name "*.spec.*" | head -10
ls -la .github/workflows/ 2>/dev/null
```

### Phase 2: Pattern Analysis
```javascript
analyzePatterns() {
  // Component patterns
  const components = glob('**/components/**/*.{jsx,tsx,vue}')
  const naming = detectNamingPattern(components)
  const structure = detectStructurePattern(components)
  
  // API patterns
  const apis = glob('**/api/**/*.{js,ts,py}')
  const apiStyle = detectAPIStyle(apis)
  const authentication = detectAuthPattern(apis)
  
  // Test patterns
  const tests = glob('**/*.{test,spec}.{js,ts,jsx,tsx}')
  const testStructure = detectTestStructure(tests)
  const testApproach = detectTestingApproach(tests)
  
  return {naming, structure, apiStyle, authentication, testStructure, testApproach}
}
```

### Phase 3: Convention Extraction
```javascript
extractConventions() {
  // From git history
  const commits = getRecentCommits(100)
  const commitFormat = detectCommitFormat(commits)
  const branchNames = getBranchNames()
  const branchPattern = detectBranchPattern(branchNames)
  
  // From code
  const imports = analyzeImports()
  const codeStyle = analyzeCodeStyle()
  const comments = analyzeCommentStyle()
  
  return {commitFormat, branchPattern, imports, codeStyle, comments}
}
```

## Output Formats

### Default Output
```yaml
Project Analysis Complete:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Framework    : Next.js 14.0.3
Language     : TypeScript (strict mode)
UI Library   : React 18.2 + Tailwind CSS
State        : Zustand
Database     : Prisma + PostgreSQL
Testing      : Jest + React Testing Library
API Style    : REST (23 endpoints found)
Auth         : NextAuth.js with JWT

Patterns Detected:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Components   : Atomic design (atoms/molecules/organisms)
File Naming  : PascalCase components, camelCase utilities
Imports      : Absolute with @ alias to src/
Tests        : Co-located (__tests__ folders)
Coverage     : 73% (target appears to be 80%)

Team Conventions:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Git Flow     : Feature branches (feature/*)
Commits      : Conventional commits with scope
PR Process   : Templates used, 2 reviewers required
Code Review  : Thorough (avg 3.2 comments per PR)
Team Size    : 5-10 active contributors
```

### JSON Output (--json)
```json
{
  "framework": {
    "name": "Next.js",
    "version": "14.0.3",
    "preset": "typescript"
  },
  "language": {
    "name": "TypeScript",
    "strict": true,
    "target": "ES2022"
  },
  "testing": {
    "framework": "jest",
    "library": "react-testing-library",
    "coverage": 73,
    "structure": "colocated"
  },
  "patterns": {
    "components": "atomic",
    "naming": "PascalCase",
    "imports": "absolute",
    "alias": "@"
  },
  "team": {
    "size": "medium",
    "workflow": "gitflow",
    "commits": "conventional"
  }
}
```

### Detailed Output (--detailed)
Includes:
- Every file pattern found
- Sample code showing conventions
- Detailed metrics and statistics
- Confidence scores for each detection
- Recommendations for improvements

## Smart Detection Examples

### React Project Detection
```javascript
if (hasFile('package.json')) {
  const pkg = JSON.parse(readFile('package.json'))
  
  // Framework detection
  if (pkg.dependencies?.next) return 'Next.js'
  if (pkg.dependencies?.gatsby) return 'Gatsby'
  if (pkg.dependencies?.['react-scripts']) return 'Create React App'
  if (pkg.dependencies?.react) return 'React'
  
  // State management detection
  if (pkg.dependencies?.redux) features.add('Redux')
  if (pkg.dependencies?.mobx) features.add('MobX')
  if (pkg.dependencies?.zustand) features.add('Zustand')
  if (pkg.dependencies?.recoil) features.add('Recoil')
}
```

### Python Project Detection
```python
if hasFile('requirements.txt'):
    requirements = readFile('requirements.txt')
    
    # Framework detection
    if 'django' in requirements: return 'Django'
    if 'flask' in requirements: return 'Flask'
    if 'fastapi' in requirements: return 'FastAPI'
    if 'pyramid' in requirements: return 'Pyramid'
    
    # Testing framework
    if 'pytest' in requirements: testing = 'pytest'
    if 'unittest' in requirements: testing = 'unittest'
    if 'nose' in requirements: testing = 'nose'
```

### Pattern Recognition
```javascript
// Detect component patterns from actual files
const components = glob('**/components/**/*.tsx')
const patterns = components.map(path => {
  const parts = path.split('/')
  return {
    depth: parts.length,
    naming: detectCase(parts[parts.length - 1]),
    hasTest: existsSync(path.replace('.tsx', '.test.tsx')),
    hasStory: existsSync(path.replace('.tsx', '.stories.tsx')),
    hasStyles: existsSync(path.replace('.tsx', '.module.css'))
  }
})

// Determine predominant pattern
const pattern = analyzePatterns(patterns)
```

## Why This Works

### No Questions Needed
Everything can be detected from:
- **Dependencies**: Tell us frameworks and tools
- **File structure**: Reveals organization patterns
- **Code patterns**: Shows conventions and style
- **Git history**: Displays team workflow
- **Config files**: Contains explicit settings

### Accurate Detection
- Cross-reference multiple signals
- Use statistical analysis for patterns
- Apply confidence scoring
- Handle edge cases gracefully

### Fast Analysis
- Parallel detection processes
- Smart sampling (not scanning everything)
- Caching of detected patterns
- Incremental updates on changes

## Integration

This detection engine powers:
- `/onboard` - Uses detection for smart setup
- `/onboard-express` - Skip questions using detection
- `/onboard-team` - Extract team conventions
- `/generate-commands` - Create based on patterns

## The Result

After detection, Claude knows:
- How you structure projects
- What patterns you follow
- Which tools you use
- How your team works
- What conventions matter

All automatically. No questions asked.