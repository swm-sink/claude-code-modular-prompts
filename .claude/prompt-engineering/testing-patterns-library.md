# Testing Patterns Library

| version | last_updated | module_type | status |
|---------|--------------|-------------|--------|
| 1.0.0   | 2025-07-20   | testing     | stable |

## Purpose
Comprehensive library of reusable testing patterns including integration test templates, API testing patterns, database testing utilities, and performance test templates.

## Integration Test Templates

### Database Integration Test Template
```python
"""
Database Integration Test Template
Complete pattern for testing database operations with real infrastructure
"""
import pytest
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer
from contextlib import contextmanager
from typing import Generator, Any

@pytest.fixture(scope="session")
def database_container():
    """Real PostgreSQL container for integration tests"""
    with PostgresContainer("postgres:15") as postgres:
        # Set environment variables for application
        import os
        os.environ["DATABASE_URL"] = postgres.get_connection_url()
        
        # Create engine and run migrations
        engine = sa.create_engine(postgres.get_connection_url())
        
        # Import your models and create tables
        from your_app.models import Base
        Base.metadata.create_all(engine)
        
        yield engine
        
        # Cleanup
        Base.metadata.drop_all(engine)

@pytest.fixture
def db_session(database_container):
    """Fresh database session for each test with automatic rollback"""
    SessionLocal = sessionmaker(bind=database_container)
    session = SessionLocal()
    
    # Start transaction
    connection = session.connection()
    transaction = connection.begin()
    
    try:
        yield session
    finally:
        # Rollback transaction to ensure test isolation
        transaction.rollback()
        session.close()

@pytest.fixture
def sample_data(db_session):
    """Create sample data for tests"""
    from your_app.models import User, Product, Category
    
    # Create category
    category = Category(name="Electronics", description="Electronic products")
    db_session.add(category)
    
    # Create products
    products = [
        Product(name="Laptop", price=999.99, category=category, stock=10),
        Product(name="Mouse", price=29.99, category=category, stock=50)
    ]
    db_session.add_all(products)
    
    # Create users
    users = [
        User(email="buyer@example.com", name="Buyer User"),
        User(email="seller@example.com", name="Seller User")
    ]
    db_session.add_all(users)
    
    db_session.commit()
    
    return {
        "category": category,
        "products": products,
        "users": users
    }

# Example integration test using template
class TestOrderWorkflow:
    """Integration tests for order workflow"""
    
    def test_complete_order_creation_workflow(self, db_session, sample_data):
        """Test complete order creation with database integration"""
        from your_app.services import OrderService
        
        order_service = OrderService(db_session)
        buyer = sample_data["users"][0]
        laptop = sample_data["products"][0]
        
        # Create order
        order = order_service.create_order(
            user_id=buyer.id,
            items=[{"product_id": laptop.id, "quantity": 2}]
        )
        
        # Verify order created
        assert order.id is not None
        assert order.user_id == buyer.id
        assert order.total_amount == 1999.98
        assert order.status == "pending"
        
        # Verify database state
        db_order = db_session.query(Order).filter_by(id=order.id).first()
        assert db_order is not None
        assert len(db_order.items) == 1
        assert db_order.items[0].quantity == 2
        
        # Verify inventory updated
        updated_laptop = db_session.query(Product).filter_by(id=laptop.id).first()
        assert updated_laptop.stock == 8
    
    def test_order_validation_constraints(self, db_session, sample_data):
        """Test order validation with database constraints"""
        from your_app.services import OrderService
        from your_app.exceptions import InsufficientStockError
        
        order_service = OrderService(db_session)
        buyer = sample_data["users"][0]
        laptop = sample_data["products"][0]
        
        # Attempt order exceeding stock
        with pytest.raises(InsufficientStockError):
            order_service.create_order(
                user_id=buyer.id,
                items=[{"product_id": laptop.id, "quantity": 15}]  # Only 10 in stock
            )
        
        # Verify no partial order created
        orders = db_session.query(Order).filter_by(user_id=buyer.id).all()
        assert len(orders) == 0
        
        # Verify stock unchanged
        laptop_check = db_session.query(Product).filter_by(id=laptop.id).first()
        assert laptop_check.stock == 10

# Database Testing Utilities
class DatabaseTestHelpers:
    """Utility functions for database testing"""
    
    @staticmethod
    def assert_database_state(session, model, **conditions):
        """Assert specific database state exists"""
        query = session.query(model)
        for field, value in conditions.items():
            query = query.filter(getattr(model, field) == value)
        
        result = query.first()
        assert result is not None, f"Expected {model.__name__} with {conditions} not found"
        return result
    
    @staticmethod
    def count_records(session, model, **conditions):
        """Count records matching conditions"""
        query = session.query(model)
        for field, value in conditions.items():
            query = query.filter(getattr(model, field) == value)
        return query.count()
    
    @staticmethod
    @contextmanager
    def assert_no_database_changes(session, model):
        """Context manager to assert no database changes occurred"""
        initial_count = session.query(model).count()
        yield
        final_count = session.query(model).count()
        assert initial_count == final_count, f"Unexpected {model.__name__} changes detected"
    
    @staticmethod
    def create_test_record(session, model, **kwargs):
        """Create and return test record"""
        record = model(**kwargs)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
```

### File System Integration Test Template
```python
"""
File System Integration Test Template
Pattern for testing file operations with real filesystem
"""
import pytest
import tempfile
import shutil
from pathlib import Path
from typing import Generator
import os

@pytest.fixture
def temp_workspace() -> Generator[Path, None, None]:
    """Create temporary workspace for file operations"""
    temp_dir = Path(tempfile.mkdtemp())
    
    # Create common directory structure
    (temp_dir / "input").mkdir()
    (temp_dir / "output").mkdir()
    (temp_dir / "temp").mkdir()
    
    yield temp_dir
    
    # Cleanup
    shutil.rmtree(temp_dir)

@pytest.fixture
def sample_files(temp_workspace: Path):
    """Create sample files for testing"""
    files = {}
    
    # CSV file
    csv_content = "name,age,email\nJohn,30,john@example.com\nJane,25,jane@example.com"
    csv_file = temp_workspace / "input" / "users.csv"
    csv_file.write_text(csv_content)
    files["csv"] = csv_file
    
    # JSON file
    json_content = '{"users": [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]}'
    json_file = temp_workspace / "input" / "users.json"
    json_file.write_text(json_content)
    files["json"] = json_file
    
    # Binary file
    binary_file = temp_workspace / "input" / "data.bin"
    binary_file.write_bytes(b'\x00\x01\x02\x03\x04')
    files["binary"] = binary_file
    
    return files

class TestFileProcessing:
    """Integration tests for file processing operations"""
    
    def test_csv_processing_workflow(self, temp_workspace: Path, sample_files):
        """Test CSV processing with real files"""
        from your_app.processors import CSVProcessor
        
        processor = CSVProcessor(temp_workspace)
        input_file = sample_files["csv"]
        
        # Process CSV file
        result = processor.process_csv(
            input_file=input_file,
            output_dir=temp_workspace / "output",
            transformations=["uppercase_names", "add_id_column"]
        )
        
        # Verify output file created
        assert result.output_file.exists()
        assert result.output_file.suffix == ".csv"
        
        # Verify file content
        output_content = result.output_file.read_text()
        assert "JOHN" in output_content
        assert "JANE" in output_content
        assert "id," in output_content  # ID column added
        
        # Verify file permissions
        assert oct(result.output_file.stat().st_mode)[-3:] == "644"
        
        # Verify processing metadata
        assert result.records_processed == 2
        assert result.processing_time < 1.0  # Should be fast
    
    def test_file_error_handling(self, temp_workspace: Path):
        """Test file processing error scenarios"""
        from your_app.processors import CSVProcessor
        from your_app.exceptions import FileProcessingError
        
        processor = CSVProcessor(temp_workspace)
        
        # Test non-existent file
        with pytest.raises(FileProcessingError, match="File not found"):
            processor.process_csv(
                input_file=temp_workspace / "nonexistent.csv",
                output_dir=temp_workspace / "output"
            )
        
        # Test read-only output directory
        readonly_dir = temp_workspace / "readonly"
        readonly_dir.mkdir()
        readonly_dir.chmod(0o444)
        
        with pytest.raises(FileProcessingError, match="Permission denied"):
            processor.process_csv(
                input_file=sample_files["csv"],
                output_dir=readonly_dir
            )
        
        # Verify no partial files created
        assert len(list(readonly_dir.glob("*"))) == 0
    
    def test_large_file_processing(self, temp_workspace: Path):
        """Test processing with large files"""
        from your_app.processors import CSVProcessor
        
        # Create large CSV file (1MB)
        large_csv = temp_workspace / "input" / "large.csv"
        with open(large_csv, 'w') as f:
            f.write("name,value\n")
            for i in range(50000):
                f.write(f"user{i},value{i}\n")
        
        processor = CSVProcessor(temp_workspace)
        
        # Process large file
        result = processor.process_csv(
            input_file=large_csv,
            output_dir=temp_workspace / "output",
            chunk_size=1000
        )
        
        # Verify processing completed
        assert result.output_file.exists()
        assert result.records_processed == 50000
        
        # Verify memory usage was reasonable (using chunks)
        assert result.peak_memory_mb < 100  # Should not load entire file

# File System Testing Utilities
class FileSystemTestHelpers:
    """Utility functions for file system testing"""
    
    @staticmethod
    def assert_file_content(file_path: Path, expected_content: str):
        """Assert file contains expected content"""
        assert file_path.exists(), f"File {file_path} does not exist"
        actual_content = file_path.read_text()
        assert actual_content == expected_content
    
    @staticmethod
    def assert_file_permissions(file_path: Path, expected_mode: str):
        """Assert file has expected permissions"""
        actual_mode = oct(file_path.stat().st_mode)[-3:]
        assert actual_mode == expected_mode
    
    @staticmethod
    def create_test_file(workspace: Path, filename: str, content: str) -> Path:
        """Create test file with content"""
        file_path = workspace / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)
        return file_path
    
    @staticmethod
    @contextmanager
    def temporary_file_permissions(file_path: Path, mode: int):
        """Temporarily change file permissions"""
        original_mode = file_path.stat().st_mode
        file_path.chmod(mode)
        try:
            yield
        finally:
            file_path.chmod(original_mode)
```

## API Testing Patterns

### REST API Integration Test Template
```python
"""
REST API Integration Test Template
Complete pattern for testing REST APIs with real HTTP server
"""
import pytest
import requests
from typing import Generator, Dict, Any
import json
from dataclasses import dataclass

@pytest.fixture(scope="session")
def api_server():
    """Start real API server for integration tests"""
    from your_app.app import create_app
    import threading
    import time
    
    app = create_app(config="testing")
    
    # Start server in thread
    server_thread = threading.Thread(
        target=app.run,
        kwargs={"host": "127.0.0.1", "port": 5555, "debug": False}
    )
    server_thread.daemon = True
    server_thread.start()
    
    # Wait for server to start
    time.sleep(1)
    
    base_url = "http://127.0.0.1:5555"
    
    # Verify server is running
    try:
        response = requests.get(f"{base_url}/health")
        assert response.status_code == 200
    except requests.exceptions.ConnectionError:
        pytest.fail("Could not connect to test API server")
    
    yield base_url

@pytest.fixture
def api_client(api_server):
    """API client with authentication and common headers"""
    
    @dataclass
    class APIClient:
        base_url: str
        session: requests.Session
        
        def get(self, endpoint: str, **kwargs) -> requests.Response:
            return self.session.get(f"{self.base_url}{endpoint}", **kwargs)
        
        def post(self, endpoint: str, **kwargs) -> requests.Response:
            return self.session.post(f"{self.base_url}{endpoint}", **kwargs)
        
        def put(self, endpoint: str, **kwargs) -> requests.Response:
            return self.session.put(f"{self.base_url}{endpoint}", **kwargs)
        
        def delete(self, endpoint: str, **kwargs) -> requests.Response:
            return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)
        
        def authenticate(self, username: str, password: str):
            """Authenticate and set auth headers"""
            response = self.post("/auth/login", json={
                "username": username,
                "password": password
            })
            assert response.status_code == 200
            token = response.json()["access_token"]
            self.session.headers.update({"Authorization": f"Bearer {token}"})
    
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    return APIClient(base_url=api_server, session=session)

@pytest.fixture
def authenticated_client(api_client, test_user):
    """Pre-authenticated API client"""
    api_client.authenticate(test_user["username"], test_user["password"])
    return api_client

class TestUserAPI:
    """Integration tests for User API endpoints"""
    
    def test_user_registration_workflow(self, api_client):
        """Test complete user registration workflow"""
        user_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "SecurePass123",
            "name": "New User"
        }
        
        # Register user
        response = api_client.post("/api/users", json=user_data)
        
        # Verify response
        assert response.status_code == 201
        response_data = response.json()
        
        # Verify response structure
        assert "id" in response_data
        assert "username" in response_data
        assert "email" in response_data
        assert "created_at" in response_data
        assert "password" not in response_data  # Security check
        
        # Verify user can login
        login_response = api_client.post("/auth/login", json={
            "username": user_data["username"],
            "password": user_data["password"]
        })
        assert login_response.status_code == 200
        assert "access_token" in login_response.json()
    
    def test_user_crud_operations(self, authenticated_client):
        """Test complete CRUD operations for users"""
        # Create user
        user_data = {
            "username": "cruduser",
            "email": "crud@example.com",
            "name": "CRUD User"
        }
        
        create_response = authenticated_client.post("/api/users", json=user_data)
        assert create_response.status_code == 201
        user_id = create_response.json()["id"]
        
        # Read user
        get_response = authenticated_client.get(f"/api/users/{user_id}")
        assert get_response.status_code == 200
        user = get_response.json()
        assert user["username"] == user_data["username"]
        
        # Update user
        update_data = {"name": "Updated CRUD User"}
        put_response = authenticated_client.put(f"/api/users/{user_id}", json=update_data)
        assert put_response.status_code == 200
        
        # Verify update
        updated_user = authenticated_client.get(f"/api/users/{user_id}").json()
        assert updated_user["name"] == "Updated CRUD User"
        
        # Delete user
        delete_response = authenticated_client.delete(f"/api/users/{user_id}")
        assert delete_response.status_code == 204
        
        # Verify deletion
        get_deleted = authenticated_client.get(f"/api/users/{user_id}")
        assert get_deleted.status_code == 404
    
    def test_api_error_handling(self, api_client):
        """Test API error responses and edge cases"""
        # Test validation errors
        invalid_user = {
            "username": "",  # Invalid
            "email": "invalid-email",  # Invalid format
            "password": "123"  # Too short
        }
        
        response = api_client.post("/api/users", json=invalid_user)
        assert response.status_code == 400
        
        error_data = response.json()
        assert "errors" in error_data
        assert "username" in error_data["errors"]
        assert "email" in error_data["errors"]
        assert "password" in error_data["errors"]
        
        # Test duplicate username
        valid_user = {
            "username": "existinguser",
            "email": "existing@example.com",
            "password": "SecurePass123"
        }
        
        # Create first user
        first_response = api_client.post("/api/users", json=valid_user)
        assert first_response.status_code == 201
        
        # Try to create duplicate
        duplicate_response = api_client.post("/api/users", json=valid_user)
        assert duplicate_response.status_code == 409
        assert "already exists" in duplicate_response.json()["error"]
    
    def test_api_performance(self, authenticated_client):
        """Test API performance requirements"""
        import time
        
        # Test response time
        start_time = time.time()
        response = authenticated_client.get("/api/users")
        end_time = time.time()
        
        response_time = (end_time - start_time) * 1000  # Convert to ms
        assert response_time < 200  # Should respond within 200ms
        
        # Test with pagination
        response = authenticated_client.get("/api/users?page=1&limit=50")
        assert response.status_code == 200
        assert len(response.json()["users"]) <= 50

# API Testing Utilities
class APITestHelpers:
    """Utility functions for API testing"""
    
    @staticmethod
    def assert_response_structure(response: requests.Response, expected_fields: list):
        """Assert response has expected JSON structure"""
        assert response.headers.get("content-type") == "application/json"
        data = response.json()
        
        for field in expected_fields:
            assert field in data, f"Expected field '{field}' not found in response"
    
    @staticmethod
    def assert_error_response(response: requests.Response, expected_status: int, error_message: str = None):
        """Assert error response format"""
        assert response.status_code == expected_status
        error_data = response.json()
        assert "error" in error_data or "errors" in error_data
        
        if error_message:
            error_text = str(error_data)
            assert error_message in error_text
    
    @staticmethod
    def create_test_user(api_client, username: str = None) -> Dict[str, Any]:
        """Create test user and return user data"""
        username = username or f"testuser_{int(time.time())}"
        user_data = {
            "username": username,
            "email": f"{username}@example.com",
            "password": "TestPass123",
            "name": f"Test {username}"
        }
        
        response = api_client.post("/api/users", json=user_data)
        assert response.status_code == 201
        
        return response.json()
```

## Database Testing Utilities

### Database Test Fixtures and Helpers
```python
"""
Database Testing Utilities
Comprehensive utilities for database testing
"""
import pytest
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from typing import Type, Any, Dict, List
import factory
from factory.alchemy import SQLAlchemyModelFactory

class BaseModelFactory(SQLAlchemyModelFactory):
    """Base factory for database models"""
    
    class Meta:
        abstract = True
        sqlalchemy_session_persistence = "commit"

# Example model factories
class UserFactory(BaseModelFactory):
    """Factory for User model"""
    
    class Meta:
        model = User
    
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    name = factory.Faker("name")
    password_hash = factory.Faker("sha256")
    created_at = factory.Faker("date_time_this_year")
    is_active = True

class ProductFactory(BaseModelFactory):
    """Factory for Product model"""
    
    class Meta:
        model = Product
    
    name = factory.Faker("word")
    description = factory.Faker("text", max_nb_chars=200)
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    stock = factory.Faker("random_int", min=0, max=100)
    category = factory.SubFactory("CategoryFactory")

class OrderFactory(BaseModelFactory):
    """Factory for Order model"""
    
    class Meta:
        model = Order
    
    user = factory.SubFactory(UserFactory)
    status = factory.Faker("random_element", elements=["pending", "processing", "shipped", "delivered"])
    total_amount = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
    created_at = factory.Faker("date_time_this_year")

class DatabaseTestUtilities:
    """Comprehensive database testing utilities"""
    
    def __init__(self, session):
        self.session = session
    
    def create_user(self, **kwargs) -> User:
        """Create test user with custom attributes"""
        return UserFactory.create(
            _session=self.session,
            **kwargs
        )
    
    def create_product(self, **kwargs) -> Product:
        """Create test product with custom attributes"""
        return ProductFactory.create(
            _session=self.session,
            **kwargs
        )
    
    def create_order_with_items(self, user: User = None, products: List[Product] = None) -> Order:
        """Create order with order items"""
        if user is None:
            user = self.create_user()
        
        if products is None:
            products = [self.create_product() for _ in range(2)]
        
        order = OrderFactory.create(
            _session=self.session,
            user=user
        )
        
        # Create order items
        total_amount = 0
        for product in products:
            quantity = factory.Faker("random_int", min=1, max=5).generate()
            item_total = product.price * quantity
            total_amount += item_total
            
            order_item = OrderItem(
                order=order,
                product=product,
                quantity=quantity,
                unit_price=product.price,
                total_price=item_total
            )
            self.session.add(order_item)
        
        order.total_amount = total_amount
        self.session.commit()
        
        return order
    
    @contextmanager
    def transaction_rollback(self):
        """Context manager for testing transaction rollback"""
        savepoint = self.session.begin_nested()
        try:
            yield
        finally:
            savepoint.rollback()
    
    def assert_record_count(self, model: Type, expected_count: int, **filters):
        """Assert record count in database"""
        query = self.session.query(model)
        
        for field, value in filters.items():
            query = query.filter(getattr(model, field) == value)
        
        actual_count = query.count()
        assert actual_count == expected_count, \
            f"Expected {expected_count} {model.__name__} records, found {actual_count}"
    
    def assert_record_exists(self, model: Type, **conditions) -> Any:
        """Assert record exists with given conditions"""
        query = self.session.query(model)
        
        for field, value in conditions.items():
            query = query.filter(getattr(model, field) == value)
        
        record = query.first()
        assert record is not None, \
            f"Expected {model.__name__} with {conditions} not found"
        
        return record
    
    def assert_record_not_exists(self, model: Type, **conditions):
        """Assert record does not exist"""
        query = self.session.query(model)
        
        for field, value in conditions.items():
            query = query.filter(getattr(model, field) == value)
        
        record = query.first()
        assert record is None, \
            f"Unexpected {model.__name__} with {conditions} found"
    
    def bulk_create(self, factory_class, count: int, **kwargs) -> List[Any]:
        """Create multiple records using factory"""
        return factory_class.create_batch(
            count,
            _session=self.session,
            **kwargs
        )
    
    def cleanup_all_data(self):
        """Clean up all test data from database"""
        # Delete in reverse dependency order
        for table in reversed(Base.metadata.sorted_tables):
            self.session.execute(table.delete())
        self.session.commit()

@pytest.fixture
def db_utils(db_session):
    """Database utilities fixture"""
    return DatabaseTestUtilities(db_session)

# Example usage of database utilities
class TestDatabaseUtilities:
    """Tests demonstrating database utility usage"""
    
    def test_user_creation_with_utilities(self, db_utils):
        """Test using database utilities for user creation"""
        # Create user with defaults
        user = db_utils.create_user()
        assert user.id is not None
        assert user.username is not None
        
        # Create user with custom attributes
        custom_user = db_utils.create_user(
            username="customuser",
            email="custom@example.com"
        )
        assert custom_user.username == "customuser"
        
        # Assert record count
        db_utils.assert_record_count(User, 2)
    
    def test_complex_order_creation(self, db_utils):
        """Test creating complex order with items"""
        # Create order with default products
        order = db_utils.create_order_with_items()
        
        assert order.id is not None
        assert order.user_id is not None
        assert len(order.items) == 2
        assert order.total_amount > 0
        
        # Verify database relationships
        db_utils.assert_record_exists(Order, id=order.id)
        db_utils.assert_record_count(OrderItem, 2, order_id=order.id)
    
    def test_transaction_rollback_utility(self, db_utils):
        """Test transaction rollback utility"""
        initial_count = db_utils.session.query(User).count()
        
        with db_utils.transaction_rollback():
            # Create user within transaction
            user = db_utils.create_user()
            assert user.id is not None
            
            # Verify user exists within transaction
            db_utils.assert_record_count(User, initial_count + 1)
        
        # Verify rollback occurred
        db_utils.assert_record_count(User, initial_count)
```

## Performance Test Templates

### Load Testing Pattern
```python
"""
Performance Test Templates
Patterns for load testing and performance validation
"""
import pytest
import time
import concurrent.futures
import statistics
from typing import List, Dict, Callable
import psutil
import threading
from dataclasses import dataclass

@dataclass
class PerformanceResult:
    """Performance test result"""
    operation_name: str
    total_operations: int
    success_count: int
    failure_count: int
    average_response_time: float
    median_response_time: float
    p95_response_time: float
    p99_response_time: float
    operations_per_second: float
    peak_memory_mb: float
    peak_cpu_percent: float

class PerformanceTestFramework:
    """Framework for performance testing"""
    
    def __init__(self):
        self.response_times = []
        self.success_count = 0
        self.failure_count = 0
        self.memory_usage = []
        self.cpu_usage = []
        self.monitoring_active = False
    
    def run_load_test(self, 
                     operation: Callable,
                     operation_name: str,
                     concurrent_users: int = 10,
                     operations_per_user: int = 100,
                     ramp_up_time: float = 5.0) -> PerformanceResult:
        """Run load test with specified parameters"""
        
        print(f"🚀 Starting load test: {operation_name}")
        print(f"   Users: {concurrent_users}")
        print(f"   Operations per user: {operations_per_user}")
        print(f"   Ramp-up time: {ramp_up_time}s")
        
        # Start monitoring
        self._start_monitoring()
        
        # Calculate delay between user starts
        delay_between_users = ramp_up_time / concurrent_users if concurrent_users > 1 else 0
        
        # Run load test
        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_users) as executor:
            futures = []
            
            for user_id in range(concurrent_users):
                # Stagger user start times
                time.sleep(delay_between_users)
                
                future = executor.submit(
                    self._run_user_operations,
                    operation,
                    operations_per_user,
                    user_id
                )
                futures.append(future)
            
            # Wait for all users to complete
            concurrent.futures.wait(futures)
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # Stop monitoring
        self._stop_monitoring()
        
        # Calculate results
        result = self._calculate_results(
            operation_name, 
            total_time,
            concurrent_users * operations_per_user
        )
        
        self._print_results(result)
        return result
    
    def _run_user_operations(self, operation: Callable, operations_count: int, user_id: int):
        """Run operations for a single user"""
        for operation_id in range(operations_count):
            start_time = time.time()
            
            try:
                # Execute operation
                operation(user_id=user_id, operation_id=operation_id)
                
                # Record success
                end_time = time.time()
                response_time = (end_time - start_time) * 1000  # Convert to ms
                
                self.response_times.append(response_time)
                self.success_count += 1
                
            except Exception as e:
                # Record failure
                self.failure_count += 1
                print(f"Operation failed for user {user_id}, operation {operation_id}: {e}")
    
    def _start_monitoring(self):
        """Start system monitoring"""
        self.monitoring_active = True
        self.memory_usage = []
        self.cpu_usage = []
        
        def monitor():
            process = psutil.Process()
            while self.monitoring_active:
                self.memory_usage.append(process.memory_info().rss / 1024 / 1024)  # MB
                self.cpu_usage.append(process.cpu_percent())
                time.sleep(0.1)
        
        self.monitor_thread = threading.Thread(target=monitor)
        self.monitor_thread.start()
    
    def _stop_monitoring(self):
        """Stop system monitoring"""
        self.monitoring_active = False
        if hasattr(self, 'monitor_thread'):
            self.monitor_thread.join()
    
    def _calculate_results(self, operation_name: str, total_time: float, total_operations: int) -> PerformanceResult:
        """Calculate performance test results"""
        response_times_sorted = sorted(self.response_times)
        
        return PerformanceResult(
            operation_name=operation_name,
            total_operations=total_operations,
            success_count=self.success_count,
            failure_count=self.failure_count,
            average_response_time=statistics.mean(response_times_sorted) if response_times_sorted else 0,
            median_response_time=statistics.median(response_times_sorted) if response_times_sorted else 0,
            p95_response_time=self._percentile(response_times_sorted, 95),
            p99_response_time=self._percentile(response_times_sorted, 99),
            operations_per_second=self.success_count / total_time if total_time > 0 else 0,
            peak_memory_mb=max(self.memory_usage) if self.memory_usage else 0,
            peak_cpu_percent=max(self.cpu_usage) if self.cpu_usage else 0
        )
    
    def _percentile(self, data: List[float], percentile: int) -> float:
        """Calculate percentile"""
        if not data:
            return 0
        
        index = int((percentile / 100) * len(data))
        if index >= len(data):
            index = len(data) - 1
        
        return data[index]
    
    def _print_results(self, result: PerformanceResult):
        """Print performance test results"""
        print(f"\n📊 Performance Test Results: {result.operation_name}")
        print(f"   Total Operations: {result.total_operations}")
        print(f"   Successful: {result.success_count}")
        print(f"   Failed: {result.failure_count}")
        print(f"   Success Rate: {(result.success_count/result.total_operations)*100:.1f}%")
        print(f"   Operations/Second: {result.operations_per_second:.1f}")
        print(f"   Average Response Time: {result.average_response_time:.1f}ms")
        print(f"   Median Response Time: {result.median_response_time:.1f}ms")
        print(f"   95th Percentile: {result.p95_response_time:.1f}ms")
        print(f"   99th Percentile: {result.p99_response_time:.1f}ms")
        print(f"   Peak Memory Usage: {result.peak_memory_mb:.1f}MB")
        print(f"   Peak CPU Usage: {result.peak_cpu_percent:.1f}%")

# Example performance tests
class TestAPIPerformance:
    """Performance tests for API endpoints"""
    
    def test_user_creation_performance(self, api_client):
        """Test user creation API performance"""
        framework = PerformanceTestFramework()
        
        def create_user_operation(user_id: int, operation_id: int):
            """Single user creation operation"""
            user_data = {
                "username": f"perfuser_{user_id}_{operation_id}",
                "email": f"perfuser_{user_id}_{operation_id}@example.com",
                "password": "TestPass123",
                "name": f"Performance User {user_id}-{operation_id}"
            }
            
            response = api_client.post("/api/users", json=user_data)
            
            # Assert successful creation
            assert response.status_code == 201
            assert "id" in response.json()
        
        # Run load test
        result = framework.run_load_test(
            operation=create_user_operation,
            operation_name="User Creation API",
            concurrent_users=20,
            operations_per_user=50,
            ramp_up_time=10.0
        )
        
        # Assert performance requirements
        assert result.success_count >= result.total_operations * 0.95  # 95% success rate
        assert result.p95_response_time <= 200  # 95% under 200ms
        assert result.operations_per_second >= 50  # At least 50 ops/sec
        assert result.peak_memory_mb <= 500  # Under 500MB memory
    
    def test_database_query_performance(self, db_session, db_utils):
        """Test database query performance"""
        # Setup: Create test data
        db_utils.bulk_create(UserFactory, 1000)
        db_utils.bulk_create(ProductFactory, 500)
        
        framework = PerformanceTestFramework()
        
        def query_operation(user_id: int, operation_id: int):
            """Single database query operation"""
            # Complex query with joins
            result = db_session.query(User)\
                .join(Order)\
                .join(OrderItem)\
                .join(Product)\
                .filter(Product.price > 50)\
                .limit(10)\
                .all()
            
            # Ensure query returns results
            assert len(result) >= 0
        
        result = framework.run_load_test(
            operation=query_operation,
            operation_name="Database Query Performance",
            concurrent_users=10,
            operations_per_user=200,
            ramp_up_time=5.0
        )
        
        # Assert database performance requirements
        assert result.p95_response_time <= 50  # 95% under 50ms
        assert result.operations_per_second >= 100  # At least 100 queries/sec

@pytest.fixture
def performance_framework():
    """Performance testing framework fixture"""
    return PerformanceTestFramework()
```

## Thinking Pattern for Testing Patterns

```xml
<thinking_pattern name="testing_patterns_library">
  <step_1>Identify Test Type Requirements</step_1>
  <step_2>Select Appropriate Template Pattern</step_2>
  <step_3>Setup Test Infrastructure (DB, Files, APIs)</step_3>
  <step_4>Create Test Data and Fixtures</step_4>
  <step_5>Execute Test Operations</step_5>
  <step_6>Validate Business Outcomes</step_6>
  <step_7>Check Performance Requirements</step_7>
  <step_8>Verify Error Handling</step_8>
  <step_9>Clean Up Test Resources</step_9>
  <step_10>Document Test Results and Patterns</step_10>
</thinking_pattern>
```

## Integration Points

- **Integration-First Testing**: Provides templates for integration test implementation
- **TDD Enforcement Engine**: Uses patterns during TDD cycles
- **Test Quality Gates**: Validates pattern usage and effectiveness
- **Test Framework Integration**: Integrates patterns into command workflows

## Validation Metrics

- Template usage rate (target: 90%+)
- Test pattern consistency (target: 95%+)
- Integration test coverage using patterns (target: 80%+)
- Performance test coverage (target: 100% for critical paths)
- Pattern effectiveness score (target: 85%+)