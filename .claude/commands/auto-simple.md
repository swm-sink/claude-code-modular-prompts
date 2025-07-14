# /auto - Smart Command Router

You analyze requests and route to the right command instantly.

## ROUTING LOGIC:
1. **Single file/component + clear requirements** → `/task`
2. **Multiple files/components** → `/swarm` 
3. **Need to understand codebase first** → `/query`
4. **Generate documentation** → `/docs`
5. **Long-running complex work** → `/session`

## DECISION TREE:
```
Is this ONE focused task?
├─ YES → /task "your request"
└─ NO → Is this research/understanding?
    ├─ YES → /query "your request"  
    └─ NO → Is this documentation?
        ├─ YES → /docs "your request"
        └─ NO → Is this multi-component?
            ├─ YES → /swarm "your request"
            └─ NO → /session "your request"
```

## EXAMPLE ROUTING:
- `/auto "Fix login bug"` → `/task "Fix login bug"`
- `/auto "Build user dashboard"` → `/swarm "Build user dashboard"`
- `/auto "How does auth work?"` → `/query "How does auth work?"`

## USAGE:
`/auto "your request here"`

---

**NOW ANALYZE AND ROUTE: $ARGUMENTS**

**Step 1: Analyze the request**
- Is this a single focused task? 
- Does it require understanding first?
- Is it documentation?
- Multiple components?

**Step 2: Route to optimal command**
Based on analysis, execute the chosen command with the original request.