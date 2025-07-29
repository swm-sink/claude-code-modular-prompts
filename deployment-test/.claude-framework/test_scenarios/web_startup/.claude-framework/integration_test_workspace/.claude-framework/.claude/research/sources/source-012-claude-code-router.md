# Source #12: Claude Code Router

### Metadata
- **URL**: https://github.com/musistudio/claude-code-router
- **Author/Organization**: musistudio (Community)
- **Date**: 2025 (Active)
- **Type**: Community/Tool

### Verification Status
- ⚠️ Routing layer for Claude Code
- ✅ Multi-model orchestration
- ✅ Cost optimization patterns
- ✅ Dynamic model switching
- ✅ Request transformation

### Rating: 4/5

### Key Patterns Observed

1. **Multi-Model Architecture**:
   ```javascript
   roles = {
     default: "general-tasks",
     background: "lightweight-tasks",
     think: "reasoning-planning",
     longContext: "extended-context"
   }
   ```

2. **Request Transformation**:
   - OpenAI → Anthropic format
   - Environment variable injection
   - Dynamic prompt rewriting

3. **Cost Optimization**:
   - Primary model: DeepSeek-V3
   - <10% cost of Claude 3.5 Sonnet
   - Context-aware model selection

### Code Examples

```javascript
// Model selection based on context
if (tokenCount > 100000) {
  model = roles.longContext;
} else if (isReasoningTask) {
  model = roles.think;
} else {
  model = roles.default;
}

// Request transformation
const anthropicRequest = transformOpenAIToAnthropic(request);
```

### Insights & Innovations

- Regional access problem solving
- Cost-performance optimization
- Flexible model orchestration
- No source code modification needed
- Real-time token calculation

### Practical Applications

- Budget-conscious deployments
- Regional restriction bypass
- Custom model strategies
- Performance optimization
- Request monitoring

### Limitations/Caveats

- Additional infrastructure layer
- Potential latency overhead
- Model compatibility considerations