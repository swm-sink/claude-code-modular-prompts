# Intelligent Command Routing Engine

## Overview

The routing engine is the brain behind `/auto`, analyzing user intent, project context, and historical patterns to route requests to the optimal command. This eliminates the cognitive burden of remembering 18+ commands.

## 🧠 Core Routing Algorithm

### Multi-Signal Analysis Pipeline

```python
class IntelligentRouter:
    def route(self, request: str, context: Context) -> RouteDecision:
        # 1. Intent Classification
        intent = self.classify_intent(request)
        
        # 2. Complexity Analysis  
        complexity = self.analyze_complexity(request, context)
        
        # 3. Context Integration
        signals = self.gather_context_signals(context)
        
        # 4. Pattern Matching
        historical_match = self.match_historical_patterns(request, context.user)
        
        # 5. Safety Assessment
        risk_level = self.assess_risk_level(request, context.environment)
        
        # 6. Decision Making
        decision = self.make_routing_decision(
            intent, complexity, signals, historical_match, risk_level
        )
        
        return decision
```

## 📊 Intent Classification System

### Primary Intent Categories

```yaml
Development Intents:
  - fix: Bug fixes, error corrections → /task
  - implement: New functionality → /task or /feature
  - add: New features or components → /feature
  - refactor: Code improvements → /task or /team
  - optimize: Performance improvements → /task or /analyze

Research Intents:
  - understand: Code comprehension → /analyze
  - investigate: Problem analysis → /analyze  
  - explore: Codebase discovery → /analyze
  - profile: Performance analysis → /analyze
  - audit: Security/quality review → /analyze

Deployment Intents:
  - deploy: Production changes → /deploy
  - release: Version deployment → /deploy
  - rollback: Revert changes → /deploy
  - hotfix: Emergency fixes → /deploy

Collaboration Intents:
  - coordinate: Multi-person work → /team
  - parallelize: Concurrent tasks → /team
  - distribute: Work distribution → /team

Management Intents:
  - setup: Framework configuration → /setup
  - configure: Settings management → /setup
  - optimize: Framework tuning → /setup
  - document: Documentation tasks → /setup docs
```

### Intent Recognition Patterns

```javascript
const intentPatterns = {
  task: {
    keywords: ['fix', 'bug', 'error', 'issue', 'small', 'quick', 'simple'],
    patterns: [
      /fix\s+(?:the\s+)?(\w+)\s+(?:bug|issue|error)/i,
      /update\s+(?:the\s+)?(\w+)\s+(?:component|function|method)/i,
      /change\s+(?:the\s+)?(\w+)\s+to\s+(\w+)/i
    ],
    scopeIndicators: ['file', 'function', 'method', 'component', 'line']
  },
  
  feature: {
    keywords: ['add', 'implement', 'create', 'build', 'feature', 'new'],
    patterns: [
      /(?:add|implement|create)\s+(?:a\s+)?(?:new\s+)?(\w+)\s+(?:feature|system|module)/i,
      /build\s+(?:a\s+)?(\w+)\s+(?:that|which)\s+(.*)/i,
      /integrate\s+(\w+)\s+(?:with|into)\s+(\w+)/i
    ],
    scopeIndicators: ['system', 'module', 'integration', 'api', 'service']
  },
  
  analyze: {
    keywords: ['why', 'how', 'understand', 'investigate', 'analyze', 'explore'],
    patterns: [
      /(?:why|how)\s+(?:is|does|did)\s+(?:the\s+)?(\w+)\s+(.*)/i,
      /(?:understand|investigate|analyze)\s+(?:the\s+)?(\w+)/i,
      /(?:what|where)\s+(?:is|are)\s+(?:the\s+)?(\w+)/i
    ],
    scopeIndicators: ['performance', 'architecture', 'structure', 'dependencies']
  }
};
```

## 🔍 Complexity Analysis

### Complexity Scoring Algorithm

```typescript
interface ComplexityFactors {
  scopeIndicators: number;      // Keywords indicating scope
  fileCount: number;            // Estimated files affected
  componentCount: number;       // Estimated components
  crossCutting: boolean;        // Affects multiple systems
  timeIndicators: number;       // Time-related keywords
  uncertaintyLevel: number;     // Ambiguous requirements
}

function calculateComplexity(request: string, context: Context): ComplexityScore {
  const factors: ComplexityFactors = {
    scopeIndicators: countScopeKeywords(request),
    fileCount: estimateFileImpact(request, context),
    componentCount: estimateComponentImpact(request),
    crossCutting: detectCrossCuttingConcerns(request),
    timeIndicators: countTimeKeywords(request),
    uncertaintyLevel: measureAmbiguity(request)
  };
  
  // Weighted scoring
  const score = 
    factors.scopeIndicators * 0.2 +
    factors.fileCount * 0.25 +
    factors.componentCount * 0.25 +
    (factors.crossCutting ? 0.2 : 0) +
    factors.timeIndicators * 0.05 +
    factors.uncertaintyLevel * 0.05;
    
  return {
    score,
    category: score < 0.3 ? 'simple' : score < 0.7 ? 'moderate' : 'complex',
    factors
  };
}
```

### Complexity-Based Routing

```yaml
Simple (score < 0.3):
  - Single file changes → /task
  - Clear bug fixes → /task
  - Minor updates → /task

Moderate (0.3 ≤ score < 0.7):
  - Multi-file features → /feature
  - System exploration → /analyze
  - Coordinated changes → /team

Complex (score ≥ 0.7):
  - Architecture changes → /team + /session
  - Major refactoring → /team
  - System overhauls → /analyze → /feature → /deploy
```

## 🎯 Context Signal Integration

### Context Signals Hierarchy

```typescript
interface ContextSignals {
  // Project State (High Priority)
  gitStatus: {
    branch: string;
    hasChanges: boolean;
    isFeatureBranch: boolean;
    hasConflicts: boolean;
  };
  
  // Active Session (High Priority)
  activeSession: {
    exists: boolean;
    type: string;
    duration: number;
    lastCommand: string;
  };
  
  // Recent Activity (Medium Priority)
  recentCommands: {
    last5Commands: string[];
    dominantPattern: string;
    avgComplexity: number;
  };
  
  // Project Type (Medium Priority)
  projectCharacteristics: {
    language: string;
    framework: string;
    size: 'small' | 'medium' | 'large';
    testCoverage: number;
  };
  
  // User Patterns (Low Priority)
  userPreferences: {
    preferredCommands: Map<string, number>;
    avgSessionLength: number;
    expertiseLevel: number;
  };
}
```

### Signal-Based Adaptations

```javascript
function adaptRouting(baseRoute: string, signals: ContextSignals): RouteDecision {
  let route = baseRoute;
  let modifiers = [];
  
  // Active session adaptation
  if (signals.activeSession.exists) {
    if (signals.activeSession.type === 'feature' && baseRoute === '/task') {
      // Upgrade to feature context
      route = '/feature';
      modifiers.push('--continue-session');
    }
  }
  
  // Git state adaptation
  if (signals.gitStatus.hasConflicts && baseRoute === '/deploy') {
    // Force conflict resolution
    route = '/task';
    modifiers.push('--resolve-conflicts');
  }
  
  // Recent activity adaptation
  if (signals.recentCommands.dominantPattern === 'analysis' && baseRoute === '/task') {
    // Suggest analysis first
    return {
      primary: '/analyze',
      secondary: baseRoute,
      reason: 'Recent analysis pattern suggests understanding needed first'
    };
  }
  
  // Project size adaptation
  if (signals.projectCharacteristics.size === 'large' && baseRoute === '/task') {
    // Suggest team for large projects
    if (estimatedImpact(request) > LARGE_IMPACT_THRESHOLD) {
      route = '/team';
      modifiers.push('--distributed');
    }
  }
  
  return { route, modifiers };
}
```

## 🚀 Decision Making Engine

### Multi-Factor Decision Matrix

```typescript
interface RouteDecision {
  primaryCommand: string;
  confidence: number;
  alternatives: Alternative[];
  reasoning: string;
  suggestedModifiers: string[];
}

class DecisionEngine {
  private weights = {
    intentMatch: 0.35,
    complexityMatch: 0.25,
    contextRelevance: 0.20,
    historicalSuccess: 0.15,
    safetyRequirement: 0.05
  };
  
  makeDecision(factors: RoutingFactors): RouteDecision {
    const candidates = this.generateCandidates(factors);
    
    // Score each candidate
    const scored = candidates.map(candidate => ({
      command: candidate,
      score: this.scoreCandidate(candidate, factors),
      reasoning: this.explainScore(candidate, factors)
    }));
    
    // Sort by score
    scored.sort((a, b) => b.score - a.score);
    
    // Build decision
    return {
      primaryCommand: scored[0].command,
      confidence: scored[0].score,
      alternatives: scored.slice(1, 4).map(s => ({
        command: s.command,
        confidence: s.score,
        reasoning: s.reasoning
      })),
      reasoning: scored[0].reasoning,
      suggestedModifiers: this.suggestModifiers(scored[0].command, factors)
    };
  }
}
```

### Confidence Thresholds

```yaml
High Confidence (≥ 0.8):
  - Direct command execution
  - No alternatives shown
  - Example: "fix login bug" → /task (0.92)

Medium Confidence (0.6 - 0.8):
  - Show primary with explanation
  - Offer top alternative
  - Example: "improve API" → /task (0.75) or /analyze (0.65)

Low Confidence (< 0.6):
  - Present multiple options
  - Explain differences
  - Let user choose
  - Example: "make it faster" → Multiple options with explanations
```

## 📈 Learning and Adaptation

### Pattern Learning System

```python
class PatternLearner:
    def __init__(self):
        self.pattern_db = PatternDatabase()
        self.success_tracker = SuccessTracker()
    
    def learn_from_execution(self, request: str, decision: RouteDecision, outcome: Outcome):
        # Track success/failure
        self.success_tracker.record(request, decision, outcome)
        
        # Update pattern weights
        if outcome.successful:
            self.pattern_db.reinforce(request, decision.primaryCommand)
        else:
            self.pattern_db.diminish(request, decision.primaryCommand)
        
        # Discover new patterns
        if outcome.user_corrected:
            self.pattern_db.add_pattern(
                request, 
                outcome.actual_command,
                confidence=0.7
            )
    
    def predict_best_route(self, request: str, base_prediction: str) -> str:
        historical_matches = self.pattern_db.find_similar(request)
        
        if historical_matches:
            best_match = max(historical_matches, key=lambda m: m.success_rate)
            if best_match.success_rate > 0.8:
                return best_match.command
        
        return base_prediction
```

### Continuous Improvement Metrics

```yaml
Tracking Metrics:
  - Route accuracy: % of correct first-time routes
  - User corrections: How often users override
  - Command success: Task completion rates
  - Time to decision: Routing speed
  - Context relevance: How well context improved decisions

Improvement Triggers:
  - Pattern success > 90%: Increase weight
  - Pattern failure > 30%: Decrease weight  
  - New pattern discovered: Add to database
  - Context signal helpful: Increase importance
```

## 🔥 Performance Optimization

### Caching Strategy

```typescript
class RouteCache {
  private cache = new LRUCache<string, RouteDecision>(1000);
  private contextHash = new ContextHasher();
  
  getCached(request: string, context: Context): RouteDecision | null {
    const key = this.generateKey(request, context);
    return this.cache.get(key);
  }
  
  private generateKey(request: string, context: Context): string {
    // Include only material context changes
    const materialContext = {
      gitBranch: context.gitStatus.branch,
      hasSession: context.activeSession.exists,
      projectType: context.projectCharacteristics.language
    };
    
    return `${hash(request)}:${this.contextHash.hash(materialContext)}`;
  }
}
```

### Fast Path Optimizations

```yaml
Instant Routes (< 100ms):
  - Exact pattern matches from cache
  - High-confidence keyword matches
  - Recent repeat requests

Fast Routes (< 500ms):
  - Simple intent classification
  - Basic complexity analysis
  - Cached context signals

Standard Routes (< 2s):
  - Full analysis pipeline
  - Context integration
  - Learning consultation
```

## 🎮 User Experience Features

### Interactive Clarification

When confidence is low, the router asks clarifying questions:

```typescript
interface ClarificationDialog {
  question: string;
  options: {
    label: string;
    command: string;
    explanation: string;
  }[];
}

// Example:
{
  question: "I see you want to make improvements. What's your focus?",
  options: [
    {
      label: "Fix a specific bug",
      command: "/task",
      explanation: "Best for focused fixes in single files"
    },
    {
      label: "Add new functionality", 
      command: "/feature",
      explanation: "Full feature development with tests"
    },
    {
      label: "Understand the current code",
      command: "/analyze",
      explanation: "Explore and analyze before making changes"
    }
  ]
}
```

### Routing Explanations

Every routing decision includes human-readable explanation:

```javascript
function explainRouting(decision: RouteDecision): string {
  const templates = {
    high_confidence: `I'm routing this to ${decision.primaryCommand} because ${decision.reasoning}.`,
    
    medium_confidence: `This looks like a ${decision.primaryCommand} task (${Math.round(decision.confidence * 100)}% confident). 
                        ${decision.reasoning}. 
                        Alternative: ${decision.alternatives[0]?.command} might also work.`,
    
    low_confidence: `I see a few ways to approach this:
                     1. ${decision.primaryCommand} - ${decision.reasoning}
                     2. ${decision.alternatives[0]?.command} - ${decision.alternatives[0]?.reasoning}
                     Which would you prefer?`
  };
  
  return decision.confidence >= 0.8 ? templates.high_confidence :
         decision.confidence >= 0.6 ? templates.medium_confidence :
         templates.low_confidence;
}
```

## 📊 Routing Examples

### Example 1: Simple Bug Fix
```
Input: "fix the login button not working"
Analysis:
  - Intent: fix (high confidence)
  - Complexity: simple (single component)
  - Context: no active session
  - Risk: low
  
Decision: /task (confidence: 0.92)
Explanation: "This is a focused bug fix in a single component."
```

### Example 2: Feature Request
```
Input: "add user notifications to the dashboard"
Analysis:
  - Intent: add feature (high confidence)
  - Complexity: moderate (multiple components)
  - Context: feature branch active
  - Risk: medium
  
Decision: /feature (confidence: 0.85)
Explanation: "This requires adding new functionality across multiple components."
```

### Example 3: Ambiguous Request
```
Input: "make the app faster"
Analysis:
  - Intent: optimize (medium confidence)
  - Complexity: unknown
  - Context: no specific target
  - Risk: varies
  
Decision: Multiple options (confidence: 0.45)
Options presented:
  1. /analyze - "First, let's analyze where the performance issues are"
  2. /task - "If you know the specific bottleneck to fix"
  3. /feature - "If this requires architectural changes"
```

### Example 4: Context-Aware Routing
```
Input: "continue working on this"
Analysis:
  - Intent: continue (context-dependent)
  - Active session: feature development
  - Last command: /feature
  - Recent files: authentication module
  
Decision: /feature --resume (confidence: 0.88)
Explanation: "Resuming your feature development session on authentication."
```

## 🚀 Implementation Plan

### Phase 1: Core Router (Days 1-3)
- Intent classification engine
- Basic complexity analysis  
- Simple routing rules
- Cache implementation

### Phase 2: Context Integration (Days 4-5)
- Git state integration
- Session awareness
- Project characteristic detection
- Context-based adaptations

### Phase 3: Learning System (Days 6-7)
- Pattern database setup
- Success tracking
- Learning algorithms
- Continuous improvement

### Phase 4: UX Polish (Days 8-10)
- Interactive clarifications
- Routing explanations
- Performance optimization
- Edge case handling

---
*Routing Engine Specification v1.0.0 | Generated: 2025-07-19*