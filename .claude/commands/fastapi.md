# /fastapi - Enterprise API Development

**Purpose**: Build production-ready FastAPI applications with best practices, performance optimization, and enterprise patterns.

## When to Use

Use `/fastapi` for:
- REST API development
- Microservice creation
- API gateway implementation
- WebSocket services
- GraphQL endpoints
- Background task APIs

## Session Management

- **Recommends sessions** for new API services
- **Links to active session** if building APIs
- **Tracks API endpoints** created in session
- **Documents architecture decisions**
- Use `/session start` for microservice development

## Core Patterns

### Project Structure
```
app/
├── api/
│   ├── v1/
│   │   ├── endpoints/
│   │   ├── dependencies.py
│   │   └── router.py
├── core/
│   ├── config.py
│   ├── security.py
│   └── database.py
├── models/
├── schemas/
├── services/
├── repositories/
└── main.py
```

### Layered Architecture
```python
# Clean separation of concerns
Controller (API endpoints)
    ↓
Service Layer (Business logic)
    ↓
Repository Layer (Data access)
    ↓
Database
```

## Common Implementations

### RESTful CRUD API
```python
# Automatic implementation of all layers
@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service),
    current_user: User = Depends(get_current_user)
):
    return await user_service.get_by_id(user_id)
```

### Service Layer
```python
# Business logic separated from API
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
    
    async def create_user(self, data: UserCreate) -> User:
        # Business validation
        # External service calls
        # Transaction handling
        return await self.repo.create(data)
```

### Repository Pattern
```python
# Data access abstraction
class UserRepository:
    async def create(self, data: dict) -> User:
        # Database specific code
        # Query optimization
        # Connection handling
```

## Performance Features

### Async/Await
```python
# Non-blocking I/O for high concurrency
@router.get("/data")
async def get_data(
    cache: Redis = Depends(get_redis),
    db: Database = Depends(get_db)
):
    # Parallel execution
    cached, fresh = await asyncio.gather(
        cache.get("data"),
        db.fetch_data()
    )
    return cached or fresh
```

### Caching Strategy
```python
# Multi-level caching
@cached(expire=300)  # 5-minute cache
async def expensive_operation():
    # In-memory cache (first level)
    # Redis cache (second level)  
    # Database (third level)
```

### Database Optimization
```python
# Connection pooling
database = Database(
    DATABASE_URL,
    min_size=10,
    max_size=20,
    command_timeout=60
)

# Query optimization
@router.get("/users")
async def list_users(
    limit: int = Query(100, le=1000),
    offset: int = 0
):
    # Pagination
    # Index usage
    # Projection
```

## Advanced Features

### WebSocket Support
```python
@router.websocket("/ws/{client_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    client_id: str
):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(client_id)
```

### Background Tasks
```python
# Async task processing
@router.post("/reports/generate")
async def generate_report(
    background_tasks: BackgroundTasks,
    report_request: ReportRequest
):
    task_id = str(uuid4())
    background_tasks.add_task(
        process_report, 
        task_id, 
        report_request
    )
    return {"task_id": task_id}
```

### API Versioning
```python
# Version management
app = FastAPI()

# Mount versioned routers
app.mount("/api/v1", create_app_v1())
app.mount("/api/v2", create_app_v2())

# Header-based versioning
@router.get("/resource")
async def get_resource(
    version: str = Header("X-API-Version", "v1")
):
    if version == "v2":
        return ResourceV2()
    return ResourceV1()
```

## Security Integration

### Authentication
```python
# JWT with refresh tokens
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token",
    auto_error=True
)

async def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> User:
    # Validate JWT
    # Check expiration
    # Load user
```

### Rate Limiting
```python
# Per-user rate limiting
@router.get("/api/data")
@rate_limit("5/minute")
async def get_data(
    current_user: User = Depends(get_current_user)
):
    # Rate limit by user ID
    # Redis-backed counters
```

## Error Handling

### Global Exception Handler
```python
@app.exception_handler(ValueError)
async def value_error_handler(
    request: Request,
    exc: ValueError
):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Invalid input",
            "detail": str(exc),
            "request_id": request.state.request_id
        }
    )
```

### Structured Errors
```python
class APIError(BaseModel):
    error: str
    detail: Optional[str]
    request_id: str
    timestamp: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "error": "ValidationError",
                "detail": "Email format invalid",
                "request_id": "123e4567-e89b",
                "timestamp": "2024-01-01T00:00:00Z"
            }
        }
```

## Testing Support

### Automatic Test Generation
```python
# Generated test for each endpoint
async def test_create_user(client: AsyncClient):
    response = await client.post(
        "/api/v1/users",
        json={"email": "test@example.com"}
    )
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"
```

## Documentation

### OpenAPI Integration
```python
# Automatic API documentation
app = FastAPI(
    title="Enterprise API",
    description="Production-ready API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)
```

## Examples

### Complete CRUD Service
```bash
/fastapi "Create user management API with auth"
# Generates:
- User model with validation
- CRUD endpoints
- JWT authentication
- Role-based authorization
- Comprehensive tests
- API documentation
```

### Microservice
```bash
/fastapi "Build payment processing microservice"
# Prompts: "Create session for this microservice? (y/n)"
# If yes: Creates session #128 "Payment Microservice"

# Creates:
- Service architecture → Updates session: "Layered architecture defined"
- External API integration → Updates session: "Stripe/PayPal integrated"
- Event publishing → Updates session: "Kafka events configured"
- Error handling → Updates session: "Global handlers added"
- Monitoring endpoints → Updates session: "Health/metrics endpoints"
# Session includes API documentation link
```

## Token Optimization
- Focus on patterns over boilerplate
- Reusable components
- Clear architecture
- Max 10k tokens per service