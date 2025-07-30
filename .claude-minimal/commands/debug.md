---
name: /debug
description: "Debug issues, errors, and problems in your code"
usage: /debug "description of the problem" [error-message] [file-path]
category: core
tools: Read, Bash, Grep, Glob, LS
---

# Universal Debugging Assistant

**Diagnose and fix bugs, errors, and unexpected behavior in any codebase.**

## Debugging Approaches

### Error Diagnosis
```
/debug "getting 500 error on user login"
/debug "TypeError: Cannot read property 'name' of undefined"
/debug "database connection keeps timing out"
```

### Behavior Issues
```
/debug "my React component won't re-render"
/debug "API returns empty data sometimes"
/debug "tests pass individually but fail together"
```

### Performance Problems
```
/debug "app becomes unresponsive after 10 minutes"
/debug "memory usage keeps growing"
/debug "slow database queries"
```

### Integration Issues
```
/debug "third-party API integration failing"
/debug "deployment works locally but not in production"
/debug "CORS errors in development"
```

## Debugging Process

### 1. Problem Analysis
- **🔍 Symptom identification**
- **📍 Error location pinpointing**  
- **🕐 Timing and frequency analysis**
- **🌍 Environment considerations**
- **📊 Impact assessment**

### 2. Investigation
- **📂 Code examination**
- **📜 Log analysis**
- **🔗 Dependency checking**
- **⚙️ Configuration review**
- **🗃️ Data state inspection**

### 3. Solution Implementation
- **🎯 Root cause fixes**
- **🛡️ Prevention measures**
- **🧪 Testing verification**
- **📚 Documentation updates**

## Example Debugging Sessions

### Frontend Error Debug
```
👤 /debug "React app crashes with 'Cannot read property 'map' of undefined'"

🤖 Analyzing React error...
🤖 Examining component code and data flow...

🔍 ERROR ANALYSIS:
❌ Error: TypeError: Cannot read property 'map' of undefined
📍 Location: UserList.jsx line 45
🕐 Timing: During initial component mount

🧠 ROOT CAUSE INVESTIGATION:
1. Component renders before data is loaded
2. API call is asynchronous but component assumes data exists
3. No loading state or null checking

💡 SOLUTION:
```jsx
// Current problematic code:
const UserList = ({ users }) => {
  return (
    <div>
      {users.map(user => <UserCard key={user.id} user={user} />)}
    </div>
  );
};

// Fixed code:
const UserList = ({ users }) => {
  // Add null checking and loading state
  if (!users) {
    return <div>Loading users...</div>;
  }
  
  if (users.length === 0) {
    return <div>No users found</div>;
  }
  
  return (
    <div>
      {users.map(user => <UserCard key={user.id} user={user} />)}
    </div>
  );
};
```

🎯 PREVENTION:
• Always handle loading states
• Use TypeScript for better type safety
• Add default props: `users = []`
• Consider using React Suspense

✅ VERIFICATION:
1. Test with empty data
2. Test with slow network
3. Add error boundary for fallback
```

### Backend API Debug
```
👤 /debug "API returns 500 error intermittently"

🤖 Debugging intermittent 500 error...
🤖 Analyzing server logs and request patterns...

🔍 ERROR PATTERN ANALYSIS:
❌ Error: 500 Internal Server Error
📊 Frequency: ~15% of requests
🕐 Timing: Occurs under load (>100 concurrent requests)
📍 Endpoint: POST /api/users

🧠 ROOT CAUSE INVESTIGATION:
1. Database connection pool exhaustion
2. No connection cleanup in error cases
3. Race condition in user creation logic

💡 SOLUTION:
```javascript
// Current problematic code:
app.post('/api/users', async (req, res) => {
  const connection = await db.getConnection();
  try {
    const user = await connection.query('INSERT INTO users...', data);
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: 'Server error' });
    // BUG: Connection not released on error!
  }
  connection.release();
});

// Fixed code:
app.post('/api/users', async (req, res) => {
  const connection = await db.getConnection();
  try {
    const user = await connection.query('INSERT INTO users...', data);
    res.json(user);
  } catch (error) {
    console.error('User creation error:', error);
    res.status(500).json({ error: 'Failed to create user' });
  } finally {
    // Always release connection
    connection.release();
  }
});
```

🎯 ADDITIONAL FIXES:
1. Increase connection pool size
2. Add request timeout handling
3. Implement retry logic
4. Add monitoring/alerting

🧪 TESTING:
• Load test with 200+ concurrent requests
• Verify connection pool metrics
• Monitor error rates in production
```

### Performance Debug
```
👤 /debug "my Python script becomes slower over time"

🤖 Analyzing performance degradation...
🤖 Profiling memory usage and execution patterns...

📊 PERFORMANCE ANALYSIS:
⚠️  Issue: Processing time increases from 2s to 45s
📈 Pattern: Linear degradation with data size
🧠 Likely: Memory leak or inefficient algorithm

🔍 PROFILING RESULTS:
• Memory usage: Grows from 100MB to 2GB
• CPU usage: Stable (not a computation issue)
• Garbage collection: Frequent, expensive

💡 ROOT CAUSE FOUND:
```python
# Problematic code - memory leak:
processed_items = []  # This grows infinitely!

def process_data_stream():
    for item in data_stream:
        result = expensive_operation(item)
        processed_items.append(result)  # Memory leak!
        yield result

# Fixed code:
def process_data_stream(batch_size=1000):
    batch = []
    for item in data_stream:
        result = expensive_operation(item)
        batch.append(result)
        
        if len(batch) >= batch_size:
            yield from batch
            batch.clear()  # Free memory regularly
    
    # Handle remaining items
    if batch:
        yield from batch
```

🎯 OPTIMIZATION STRATEGY:
1. Process data in batches
2. Use generators instead of lists  
3. Implement explicit garbage collection
4. Add memory monitoring

✅ RESULTS:
• Memory usage: Stable at ~150MB
• Processing time: Constant 2-3s per batch
• 95% performance improvement
```

## Multi-Technology Support

**Universal debugging across:**
- **Web**: Frontend (React, Vue, Angular), Backend (Node.js, Python, Java)
- **Mobile**: React Native, Flutter, native iOS/Android
- **Desktop**: Electron, WPF, Qt applications  
- **Systems**: Server applications, microservices, APIs
- **Databases**: SQL, NoSQL, performance issues
- **DevOps**: Deployment, CI/CD, infrastructure problems

## Debugging Tools Integration

**I'll help you use:**
- **Browser DevTools**: Console, Network, Performance tabs
- **IDE Debugging**: Breakpoints, watch variables, call stacks
- **Command Line**: curl, logs, system monitoring
- **Profiling Tools**: Memory profilers, performance analyzers
- **Testing**: Unit tests, integration tests for reproduction

## Prevention Strategies

**Common patterns I'll suggest:**
- **Error boundaries** for graceful failure handling
- **Input validation** to prevent bad data
- **Logging strategies** for better visibility
- **Monitoring** for early problem detection
- **Testing** to catch regressions

## Ready to Debug?

Describe the problem you're experiencing:

```
/debug "error message here"
/debug "unexpected behavior description"  
/debug "performance issue details"
/debug "integration problem"
```

I'll help you find and fix the root cause!