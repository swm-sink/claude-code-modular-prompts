# Integration-First Testing Module

| version | last_updated | module_type | status |
|---------|--------------|-------------|--------|
| 1.0.0   | 2025-07-20   | testing     | stable |

## Purpose
Implement integration-first testing methodology with 80/20 rule (80% integration, 20% unit) to ensure real-world reliability and business outcome validation.

## Core Principles

### 80/20 Testing Rule
```xml
<testing_distribution enforcement="MANDATORY">
  <integration_tests>80% - Test real system interactions</integration_tests>
  <unit_tests>20% - Test critical business logic in isolation</unit_tests>
  <rationale>Integration tests catch 80% of real-world failures</rationale>
  <validation>Automated coverage tracking enforces distribution</validation>
</testing_distribution>
```

### Integration-First Hierarchy
```xml
<test_hierarchy priority="CRITICAL">
  <tier_1 priority="highest">End-to-end business workflows</tier_1>
  <tier_2 priority="high">API contract testing with real services</tier_2>
  <tier_3 priority="medium">Database transaction testing</tier_3>
  <tier_4 priority="medium">File system operation testing</tier_4>
  <tier_5 priority="low">Unit tests for complex business logic only</tier_5>
</test_hierarchy>
```

## Real Database Testing Patterns

### Database Test Setup
```python
# Database Integration Test Template
import pytest
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer
from your_app.models import User, Product, Order
from your_app.database import get_session

@pytest.fixture(scope="session")
def real_database():
    """Use real PostgreSQL container for integration tests"""
    with PostgresContainer("postgres:15") as postgres:
        engine = sa.create_engine(postgres.get_connection_url())
        # Run migrations
        Base.metadata.create_all(engine)
        yield engine

@pytest.fixture
def db_session(real_database):
    """Fresh database session for each test"""
    Session = sessionmaker(bind=real_database)
    session = Session()
    try:
        yield session
    finally:
        session.rollback()
        session.close()

# Integration Test Example
def test_complete_order_workflow(db_session):
    """Test complete order workflow with real database"""
    # Create user
    user = User(email="test@example.com", name="Test User")
    db_session.add(user)
    db_session.commit()
    
    # Create product
    product = Product(name="Test Product", price=99.99, stock=10)
    db_session.add(product)
    db_session.commit()
    
    # Create order
    order = Order(user_id=user.id, product_id=product.id, quantity=2)
    db_session.add(order)
    db_session.commit()
    
    # Verify business outcome
    updated_product = db_session.get(Product, product.id)
    assert updated_product.stock == 8
    assert order.total_amount == 199.98
    
    # Verify data integrity
    assert db_session.query(Order).filter_by(user_id=user.id).count() == 1
```

### Database Transaction Testing
```python
def test_transaction_rollback_on_failure(db_session):
    """Test transaction rollback preserves data integrity"""
    initial_count = db_session.query(User).count()
    
    try:
        with db_session.begin():
            # Create valid user
            user1 = User(email="valid@example.com", name="Valid User")
            db_session.add(user1)
            
            # Attempt invalid operation that should fail
            user2 = User(email="valid@example.com", name="Duplicate")  # Same email
            db_session.add(user2)
            db_session.commit()
    except IntegrityError:
        db_session.rollback()
    
    # Verify no partial commits occurred
    final_count = db_session.query(User).count()
    assert final_count == initial_count
```

## Real Filesystem Testing Patterns

### File System Integration Tests
```python
import tempfile
import shutil
from pathlib import Path
from your_app.file_processor import FileProcessor, ProcessingError

@pytest.fixture
def temp_workspace():
    """Create real temporary directory for file operations"""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)

def test_file_processing_workflow(temp_workspace):
    """Test complete file processing with real filesystem"""
    processor = FileProcessor(workspace=temp_workspace)
    
    # Create test input file
    input_file = temp_workspace / "input.csv"
    input_file.write_text("name,age\nJohn,30\nJane,25")
    
    # Process file
    output_file = processor.process_csv(input_file)
    
    # Verify output exists and has correct content
    assert output_file.exists()
    content = output_file.read_text()
    assert "John,30" in content
    assert "Jane,25" in content
    
    # Verify file permissions
    assert output_file.stat().st_mode & 0o777 == 0o644

def test_file_system_error_recovery(temp_workspace):
    """Test graceful handling of filesystem errors"""
    processor = FileProcessor(workspace=temp_workspace)
    
    # Create read-only directory
    readonly_dir = temp_workspace / "readonly"
    readonly_dir.mkdir()
    readonly_dir.chmod(0o444)
    
    # Attempt to write to read-only directory
    with pytest.raises(ProcessingError, match="Permission denied"):
        processor.create_output_file(readonly_dir / "output.txt")
    
    # Verify no partial files created
    assert not (readonly_dir / "output.txt").exists()
```

## Business Outcome Validation

### Business Logic Integration Tests
```python
def test_user_subscription_business_flow(db_session, stripe_mock):
    """Test complete subscription business workflow"""
    user_service = UserService(db_session)
    payment_service = PaymentService(stripe_mock)
    subscription_service = SubscriptionService(db_session, payment_service)
    
    # Business workflow: User subscribes to premium plan
    user = user_service.create_user("premium@example.com")
    plan = subscription_service.get_plan("premium")
    
    # Execute business operation
    subscription = subscription_service.subscribe_user(
        user_id=user.id,
        plan_id=plan.id,
        payment_method="card_123"
    )
    
    # Validate business outcomes
    assert subscription.status == "active"
    assert user.has_premium_access()
    assert subscription.next_billing_date is not None
    
    # Validate side effects
    payment_records = db_session.query(Payment).filter_by(
        user_id=user.id
    ).all()
    assert len(payment_records) == 1
    assert payment_records[0].amount == plan.price

def test_order_fulfillment_business_logic(db_session, inventory_service):
    """Test order fulfillment business constraints"""
    order_service = OrderService(db_session, inventory_service)
    
    # Setup: Product with limited stock
    product = create_test_product(name="Limited Item", stock=5)
    user = create_test_user()
    
    # Business scenario: Large order exceeding stock
    with pytest.raises(InsufficientStockError):
        order_service.create_order(
            user_id=user.id,
            items=[{"product_id": product.id, "quantity": 10}]
        )
    
    # Verify business invariant: No partial orders created
    orders = db_session.query(Order).filter_by(user_id=user.id).all()
    assert len(orders) == 0
    
    # Verify inventory unchanged
    updated_product = db_session.get(Product, product.id)
    assert updated_product.stock == 5
```

## API Contract Testing

### REST API Integration Tests
```python
import requests
from your_app.app import create_app

@pytest.fixture
def api_client():
    """Real API client with test database"""
    app = create_app(config="testing")
    with app.test_client() as client:
        yield client

def test_api_user_creation_workflow(api_client, db_session):
    """Test complete user creation via API"""
    # POST new user
    response = api_client.post("/api/users", json={
        "email": "newuser@example.com",
        "name": "New User",
        "password": "secure123"
    })
    
    assert response.status_code == 201
    user_data = response.get_json()
    
    # Verify response contract
    assert "id" in user_data
    assert "email" in user_data
    assert "created_at" in user_data
    assert "password" not in user_data  # Security check
    
    # Verify database state
    user = db_session.get(User, user_data["id"])
    assert user.email == "newuser@example.com"
    assert user.password_hash != "secure123"  # Password hashed
    
    # GET user to verify retrieval
    get_response = api_client.get(f"/api/users/{user.id}")
    assert get_response.status_code == 200
    assert get_response.get_json()["email"] == user.email

def test_api_error_handling_and_contracts(api_client):
    """Test API error handling maintains contracts"""
    # Invalid input
    response = api_client.post("/api/users", json={
        "email": "invalid-email",
        "name": ""
    })
    
    assert response.status_code == 400
    error_data = response.get_json()
    
    # Verify error contract
    assert "errors" in error_data
    assert "email" in error_data["errors"]
    assert "name" in error_data["errors"]
    assert isinstance(error_data["errors"], dict)
```

## Test Templates and Examples

### Integration Test Template
```python
"""
Integration Test Template
Use this template for all integration tests
"""
import pytest
from testcontainers.postgres import PostgresContainer
from your_app import create_app, db
from your_app.models import Base

class IntegrationTestBase:
    """Base class for integration tests"""
    
    @pytest.fixture(scope="class", autouse=True)
    def setup_integration_environment(self):
        """Setup real integration environment"""
        # Real database
        with PostgresContainer("postgres:15") as postgres:
            self.db_url = postgres.get_connection_url()
            
            # Real application
            self.app = create_app({
                "DATABASE_URL": self.db_url,
                "TESTING": True
            })
            
            with self.app.app_context():
                # Create schema
                Base.metadata.create_all(db.engine)
                yield
                
                # Cleanup
                Base.metadata.drop_all(db.engine)
    
    @pytest.fixture(autouse=True)
    def fresh_transaction(self):
        """Fresh transaction for each test"""
        with self.app.app_context():
            connection = db.engine.connect()
            transaction = connection.begin()
            
            # Configure session to use transaction
            db.session.configure(bind=connection)
            
            yield
            
            # Rollback transaction
            transaction.rollback()
            connection.close()

# Example usage
class TestUserWorkflows(IntegrationTestBase):
    def test_user_registration_flow(self):
        """Test complete user registration"""
        # Test implementation here
        pass
```

### Performance Integration Test Template
```python
def test_api_performance_under_load(api_client, db_session):
    """Test API performance with realistic data volume"""
    import time
    import concurrent.futures
    
    # Setup: Create realistic data volume
    users = [create_test_user(f"user{i}@example.com") for i in range(100)]
    products = [create_test_product(f"Product {i}") for i in range(50)]
    db_session.add_all(users + products)
    db_session.commit()
    
    def create_order(user_id):
        return api_client.post("/api/orders", json={
            "user_id": user_id,
            "items": [{"product_id": products[0].id, "quantity": 1}]
        })
    
    # Execute concurrent requests
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(create_order, user.id) 
            for user in users[:20]
        ]
        responses = [f.result() for f in futures]
    
    execution_time = time.time() - start_time
    
    # Validate performance and correctness
    assert execution_time < 5.0  # Under 5 seconds
    assert all(r.status_code in [200, 201] for r in responses)
    
    # Verify data integrity
    order_count = db_session.query(Order).count()
    assert order_count == 20
```

## Thinking Pattern for Integration-First Testing

```xml
<thinking_pattern name="integration_first_testing">
  <step_1>Identify Business Workflow</step_1>
  <step_2>Map Real System Dependencies</step_2>
  <step_3>Design Integration Test Scenarios</step_3>
  <step_4>Setup Real Infrastructure (DB, Files, APIs)</step_4>
  <step_5>Execute Business Workflow</step_5>
  <step_6>Validate Business Outcomes</step_6>
  <step_7>Verify Data Integrity</step_7>
  <step_8>Test Error Scenarios</step_8>
  <step_9>Add Unit Tests for Complex Logic Only</step_9>
  <step_10>Measure and Enforce 80/20 Distribution</step_10>
</thinking_pattern>
```

## Enforcement Rules

```xml
<enforcement_rules priority="CRITICAL">
  <rule>80% integration tests MANDATORY - automated coverage tracking</rule>
  <rule>Real infrastructure required - no mocks for integration tests</rule>
  <rule>Business outcome validation required for all workflows</rule>
  <rule>Unit tests only for complex business logic (20% maximum)</rule>
  <rule>Performance testing required for API endpoints</rule>
  <rule>Error scenario testing mandatory</rule>
  <rule>Data integrity validation required</rule>
</enforcement_rules>
```

## Integration Points

- **TDD Enforcement Engine**: Validates integration-first approach during TDD cycles
- **Test Quality Gates**: Enforces 80/20 distribution and business outcome validation
- **Testing Patterns Library**: Provides templates and utilities for integration tests
- **Test Framework Integration**: Connects to /task and /feature workflows

## Validation Metrics

- Test distribution ratio (target: 80% integration, 20% unit)
- Business workflow coverage (target: 100%)
- Real infrastructure usage (target: 100% for integration tests)
- Error scenario coverage (target: 90%)
- Performance benchmark coverage (target: 100% for APIs)