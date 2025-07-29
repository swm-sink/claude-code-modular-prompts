# Advanced: Multi-Phase Feature Implementation

## Overview
This example demonstrates implementing a complex feature (real-time notifications) using Claude Code's advanced workflow patterns.

## Feature: Real-Time Notification System

### Phase 1: Planning and Architecture

#### Using ClaudeFlow Pattern
```markdown
/plan Implement real-time notification system with:
- WebSocket connections for live updates  
- Notification preferences per user
- Email/SMS fallbacks
- Read/unread tracking
- Notification center UI
- Admin broadcast capabilities
```

#### Generated Plan Structure
```yaml
phases:
  1-infrastructure:
    - Set up WebSocket server
    - Create notification service architecture
    - Design database schema
    
  2-backend:
    - User preference API
    - Notification dispatch system
    - Queue management
    - Fallback handlers
    
  3-frontend:
    - Notification center component
    - Real-time connection management
    - UI indicators
    
  4-integration:
    - Connect all components
    - End-to-end testing
    - Performance optimization
```

### Phase 2: Infrastructure Setup

#### Task Management
```python
TodoWrite(todos=[
    {
        "id": "notif-infra-1",
        "content": "Design notification database schema",
        "status": "in_progress",
        "priority": "high"
    },
    {
        "id": "notif-infra-2",
        "content": "Set up Redis for pub/sub",
        "status": "pending",
        "priority": "high"
    },
    {
        "id": "notif-infra-3",
        "content": "Configure WebSocket server",
        "status": "pending",
        "priority": "high"
    },
    {
        "id": "notif-infra-4",
        "content": "Create message queue structure",
        "status": "pending",
        "priority": "medium"
    }
])
```

#### Database Schema Creation
```python
# Research existing patterns
existing_schemas = Grep("CREATE TABLE", path="migrations/", type="sql")

# Create comprehensive schema
Write(
    file_path="migrations/001_create_notifications.sql",
    content="""
-- Notifications table
CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id),
    type VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    message TEXT,
    data JSONB,
    read_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    expires_at TIMESTAMP,
    INDEX idx_user_unread (user_id, read_at),
    INDEX idx_created (created_at DESC)
);

-- User preferences
CREATE TABLE notification_preferences (
    user_id UUID PRIMARY KEY REFERENCES users(id),
    email_enabled BOOLEAN DEFAULT true,
    sms_enabled BOOLEAN DEFAULT false,
    push_enabled BOOLEAN DEFAULT true,
    quiet_hours_start TIME,
    quiet_hours_end TIME,
    frequency_limit INTEGER DEFAULT 10,
    preferences JSONB DEFAULT '{}'::jsonb
);

-- Delivery tracking
CREATE TABLE notification_deliveries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    notification_id UUID REFERENCES notifications(id),
    channel VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,
    attempted_at TIMESTAMP DEFAULT NOW(),
    delivered_at TIMESTAMP,
    error_message TEXT
);
"""
)

# Run migration
Bash("npm run db:migrate", description="Apply notification schema")
```

### Phase 3: Backend Implementation

#### Service Architecture
```python
# Create modular service structure
service_files = {
    "src/services/notification/index.js": "Main notification service",
    "src/services/notification/dispatcher.js": "Message dispatching",
    "src/services/notification/channels/email.js": "Email channel",
    "src/services/notification/channels/sms.js": "SMS channel",
    "src/services/notification/channels/websocket.js": "WebSocket channel",
    "src/services/notification/queue.js": "Queue management",
    "src/services/notification/preferences.js": "User preferences"
}

for filepath, description in service_files.items():
    Write(filepath, generate_service_code(filepath, description))
```

#### WebSocket Server Setup
```python
# Check for existing WebSocket usage
existing_ws = Grep("WebSocket|ws:|socket\\.io", path="src/")

# Create WebSocket server with authentication
MultiEdit(
    file_path="src/server.js",
    edits=[
        {
            "old_string": "const app = express();",
            "new_string": """const app = express();
const server = createServer(app);
const wss = new WebSocketServer({ 
    server,
    verifyClient: async (info, cb) => {
        const token = parseToken(info.req);
        const user = await verifyToken(token);
        cb(!!user, user);
    }
});"""
        },
        {
            "old_string": "app.listen(PORT",
            "new_string": "server.listen(PORT"
        }
    ]
)

# Add connection handling
Write(
    file_path="src/websocket/connection-manager.js",
    content=websocket_connection_code
)
```

### Phase 4: Frontend Components

#### Notification Center Component
```python
# Research UI patterns
ui_patterns = parallel_search([
    Grep("dropdown|popover", type="jsx"),
    Grep("badge|indicator", type="jsx"),
    Grep("infinite.?scroll", type="jsx")
])

# Create component hierarchy
components = [
    "NotificationCenter/index.jsx",
    "NotificationCenter/NotificationList.jsx",
    "NotificationCenter/NotificationItem.jsx",
    "NotificationCenter/NotificationBadge.jsx",
    "NotificationCenter/hooks/useNotifications.js",
    "NotificationCenter/hooks/useWebSocket.js"
]

for component in components:
    Write(f"src/components/{component}", component_code)

# Add tests
Write(
    "src/components/NotificationCenter/__tests__/NotificationCenter.test.jsx",
    comprehensive_test_suite
)
```

### Phase 5: Integration and Testing

#### Quality Gates
```python
# Run comprehensive checks
quality_results = parallel_execute([
    Bash("npm run test:unit -- notification", description="Unit tests"),
    Bash("npm run test:integration -- notification", description="Integration tests"),
    Bash("npm run lint src/services/notification", description="Lint checks"),
    Bash("npm run typecheck", description="Type checking")
])

# Performance testing
Bash("""
    npm run test:load -- \
    --concurrent=1000 \
    --duration=60 \
    --endpoint=/api/notifications
""", description="Load test WebSocket connections")

# Security audit
security_checks = [
    Grep("eval|Function\\(", path="src/services/notification/"),
    Bash("npm audit --production", description="Check dependencies"),
    Bash("npm run security:scan", description="Security scan")
]
```

#### End-to-End Testing
```python
Write(
    file_path="e2e/notification-flow.test.js",
    content="""
describe('Notification System E2E', () => {
    test('User receives real-time notification', async () => {
        // Set up test user
        const user = await createTestUser();
        const ws = await connectWebSocket(user.token);
        
        // Trigger notification
        await api.post('/api/admin/broadcast', {
            title: 'System Update',
            message: 'New features available'
        });
        
        // Verify real-time delivery
        const notification = await waitForWebSocketMessage(ws);
        expect(notification.title).toBe('System Update');
        
        // Verify UI update
        const badge = await page.$('.notification-badge');
        const count = await badge.innerText();
        expect(count).toBe('1');
    });
    
    test('Fallback to email when offline', async () => {
        // Test email delivery
    });
    
    test('Respects user preferences', async () => {
        // Test preference handling
    });
});
"""
)

Bash("npm run test:e2e -- notification-flow", description="Run E2E tests")
```

### Phase 6: Performance Optimization

#### Optimization Analysis
```python
# Analyze current performance
perf_data = parallel_analyze([
    Bash("npm run lighthouse -- /notifications", description="Lighthouse audit"),
    Grep("SELECT.*FROM notifications", path="src/", description="Find N+1 queries"),
    Bash("npm run bundle:analyze", description="Check bundle impact")
])

# Implement optimizations
optimizations = [
    {
        "issue": "Large bundle size",
        "solution": "Lazy load notification center",
        "implementation": lazy_load_component
    },
    {
        "issue": "Frequent re-renders",
        "solution": "Implement virtual scrolling",
        "implementation": virtual_scroll_implementation
    },
    {
        "issue": "N+1 queries",
        "solution": "Batch notification fetching",
        "implementation": batch_query_implementation
    }
]

for opt in optimizations:
    implement_optimization(opt)
```

### Phase 7: Documentation and Deployment

#### Comprehensive Documentation
```python
# Generate API documentation
Bash("npm run docs:generate -- src/services/notification", 
     description="Generate API docs")

# Create user guide
Write(
    file_path="docs/features/notifications.md",
    content=user_documentation
)

# Update CLAUDE.md
Edit(
    file_path="CLAUDE.md",
    old_string="## Features",
    new_string="""## Features

### Real-Time Notifications
- WebSocket server: Port 3001
- Redis required for pub/sub
- Test broadcast: `npm run test:broadcast`
- Debug mode: `DEBUG=notifications npm run dev`
"""
)
```

#### Deployment Preparation
```python
# Create deployment checklist
checklist = [
    "Database migrations ready",
    "Environment variables documented", 
    "WebSocket proxy configured",
    "Redis connection verified",
    "Monitoring alerts set up",
    "Rollback plan prepared"
]

# Verify production readiness
for item in checklist:
    verify_deployment_item(item)

# Save state for next session
/memory
```

## Key Patterns Demonstrated

### 1. **Phased Approach**
- Clear separation between planning and execution
- Each phase has specific goals
- Quality gates between phases

### 2. **Comprehensive Testing**
- Unit tests for each component
- Integration tests for workflows
- E2E tests for user journeys
- Performance and security testing

### 3. **Error Handling**
- Fallback mechanisms (email when WebSocket fails)
- Graceful degradation
- Comprehensive error logging

### 4. **State Management**
- TodoWrite for progress tracking
- Memory commands for session persistence
- Git commits at phase boundaries

### 5. **Performance Consciousness**
- Load testing early
- Bundle size monitoring
- Query optimization
- Caching strategies

### 6. **Documentation Throughout**
- API docs generated from code
- User guides created
- CLAUDE.md updated
- Deployment docs prepared

## Lessons Learned

1. **Break Complex Features**: Divide into manageable phases
2. **Test Continuously**: Don't wait until the end
3. **Monitor Performance**: Track metrics throughout
4. **Document Decisions**: Future you will thank you
5. **Use Tools Wisely**: Right tool for each task
6. **Maintain Visibility**: Regular todo updates

This advanced example shows how Claude Code can handle complex, multi-phase feature development with proper planning, execution, and quality assurance.