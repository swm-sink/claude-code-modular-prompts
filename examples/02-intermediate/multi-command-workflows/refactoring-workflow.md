# Refactoring Workflow Example

## Overview
This example demonstrates the **query → feature → protocol** workflow for systematic, large-scale refactoring with architectural improvements.

## The Problem Scenario
Your e-commerce application has grown organically over 2 years. The checkout process is becoming difficult to maintain:
- 800+ line checkout view function
- Business logic mixed with presentation logic
- No clear separation of concerns
- Adding new payment methods requires touching multiple files
- Testing is difficult due to tight coupling

Time for strategic refactoring to improve maintainability and enable future growth.

## The Multi-Command Workflow

### Step 1: Analysis and Understanding - `/query`
```bash
/query "analyze checkout system architecture and identify refactoring opportunities for better maintainability"
```

**What the Framework Does:**
- Maps current checkout system architecture
- Identifies code smells and coupling issues
- Analyzes dependencies and data flow
- Evaluates testing gaps and pain points
- Recommends architectural improvements

**Expected Framework Output:**
```
🏗️ CHECKOUT SYSTEM ARCHITECTURE ANALYSIS:

Current Structure:
├── views/
│   └── checkout.py (847 lines) - MONOLITHIC ⚠️
├── models/
│   ├── order.py - Order, OrderItem models
│   ├── payment.py - Payment, Transaction models
│   └── customer.py - Customer, Address models
├── forms/
│   └── checkout_forms.py - 12 different forms
└── templates/
    └── checkout/ - 8 template files

Code Smell Analysis:
🚨 CRITICAL ISSUES:
- checkout_view() function: 847 lines (recommended: <50)
- 15 different responsibilities in single function
- Direct database queries mixed with business logic
- Payment processing logic embedded in view
- No error recovery or transaction rollback
- Hard to test due to monolithic structure

🔍 COUPLING ANALYSIS:
checkout.py dependencies:
├── models (5 different models directly imported)
├── payment_processors (3 different gateways)
├── inventory_service (stock checking)
├── email_service (order confirmations)
├── tax_calculator (complex tax logic)
└── shipping_calculator (shipping cost logic)

📊 COMPLEXITY METRICS:
- Cyclomatic complexity: 47 (recommended: <10)
- Lines of code: 847 (recommended: <100 per function)
- Number of parameters: 23 (recommended: <5)
- Nested levels: 8 (recommended: <4)

🧪 TESTING CHALLENGES:
- Current test coverage: 23% (recommended: >90%)
- Integration tests only (no unit tests possible)
- Mock setup requires 15+ external dependencies
- Test execution time: 45 seconds per test

💡 REFACTORING OPPORTUNITIES:

1. EXTRACT SERVICES:
   - PaymentProcessor service
   - InventoryService  
   - TaxCalculationService
   - ShippingService
   - OrderCreationService

2. IMPLEMENT PATTERNS:
   - Command pattern for checkout steps
   - Strategy pattern for payment methods
   - Factory pattern for service creation
   - Observer pattern for order events

3. IMPROVE ARCHITECTURE:
   - Separate business logic from presentation
   - Implement proper error handling and rollback
   - Add comprehensive validation
   - Create testable, modular components

🎯 RECOMMENDED APPROACH:
Strangler Fig pattern - gradually replace monolithic checkout with 
modular services while maintaining existing functionality.
```

### Step 2: Systematic Refactoring Implementation - `/feature`
```bash
/feature "refactor checkout system into modular services with proper separation of concerns and comprehensive testing"
```

**What the Framework Does:**
- Creates Product Requirements Document for refactoring
- Designs new modular architecture
- Implements services using TDD approach
- Maintains backward compatibility during transition
- Creates comprehensive test suite for all components

**Generated PRD for Refactoring:**
```
📋 CHECKOUT SYSTEM REFACTORING PRD

## Executive Summary
Transform monolithic checkout system into modular, testable, maintainable 
architecture while preserving all existing functionality and improving performance.

## Technical Requirements

### Service Architecture:
1. **CheckoutOrchestrator** - Coordinates checkout process
2. **PaymentProcessorService** - Handles all payment operations
3. **InventoryService** - Manages stock checking and reservation
4. **TaxCalculationService** - Centralizes tax logic
5. **ShippingService** - Handles shipping calculations
6. **OrderService** - Manages order creation and lifecycle
7. **NotificationService** - Handles email/SMS notifications

### Quality Requirements:
- Test coverage: >95% for all services
- Performance: <200ms response time for checkout
- Backward compatibility: 100% API compatibility
- Error handling: Comprehensive with rollback capability
- Documentation: Full API documentation for all services

### Implementation Strategy:
- Phase 1: Extract and test core services
- Phase 2: Implement new checkout orchestrator
- Phase 3: Migrate existing checkout to use services
- Phase 4: Remove legacy code after validation
```

**Generated Service Architecture (TDD Implementation):**

```python
# services/checkout/orchestrator.py
from typing import Dict, Any, Optional
from dataclasses import dataclass
from .payment_processor import PaymentProcessorService
from .inventory import InventoryService
from .tax_calculator import TaxCalculationService
from .shipping import ShippingService
from .order_service import OrderService
from .notifications import NotificationService

@dataclass
class CheckoutRequest:
    customer_id: int
    items: List[Dict[str, Any]]
    shipping_address: Dict[str, str]
    payment_method: Dict[str, Any]
    promotional_codes: Optional[List[str]] = None

@dataclass
class CheckoutResult:
    success: bool
    order_id: Optional[int] = None
    payment_id: Optional[str] = None
    errors: List[str] = None
    total_amount: Optional[Decimal] = None

class CheckoutOrchestrator:
    """
    Orchestrates the checkout process using modular services.
    Implements the Command pattern for each checkout step.
    """
    
    def __init__(self):
        self.payment_service = PaymentProcessorService()
        self.inventory_service = InventoryService()
        self.tax_service = TaxCalculationService()
        self.shipping_service = ShippingService()
        self.order_service = OrderService()
        self.notification_service = NotificationService()
    
    def process_checkout(self, request: CheckoutRequest) -> CheckoutResult:
        """
        Main checkout processing with comprehensive error handling and rollback.
        """
        rollback_actions = []
        
        try:
            # Step 1: Validate and reserve inventory
            inventory_result = self.inventory_service.reserve_items(
                request.items, request.customer_id
            )
            if not inventory_result.success:
                return CheckoutResult(
                    success=False, 
                    errors=inventory_result.errors
                )
            rollback_actions.append(
                lambda: self.inventory_service.release_reservation(
                    inventory_result.reservation_id
                )
            )
            
            # Step 2: Calculate taxes and shipping
            tax_result = self.tax_service.calculate_tax(
                request.items, request.shipping_address
            )
            shipping_result = self.shipping_service.calculate_shipping(
                request.items, request.shipping_address
            )
            
            total_amount = (
                inventory_result.subtotal + 
                tax_result.tax_amount + 
                shipping_result.shipping_cost
            )
            
            # Step 3: Process payment
            payment_result = self.payment_service.process_payment(
                amount=total_amount,
                payment_method=request.payment_method,
                customer_id=request.customer_id
            )
            if not payment_result.success:
                self._execute_rollback(rollback_actions)
                return CheckoutResult(
                    success=False,
                    errors=payment_result.errors
                )
            rollback_actions.append(
                lambda: self.payment_service.refund_payment(
                    payment_result.payment_id
                )
            )
            
            # Step 4: Create order
            order_result = self.order_service.create_order(
                customer_id=request.customer_id,
                items=request.items,
                payment_id=payment_result.payment_id,
                shipping_address=request.shipping_address,
                total_amount=total_amount
            )
            if not order_result.success:
                self._execute_rollback(rollback_actions)
                return CheckoutResult(
                    success=False,
                    errors=order_result.errors
                )
            
            # Step 5: Confirm inventory reservation
            self.inventory_service.confirm_reservation(
                inventory_result.reservation_id,
                order_result.order_id
            )
            
            # Step 6: Send notifications (async, non-blocking)
            self.notification_service.send_order_confirmation.delay(
                order_result.order_id
            )
            
            return CheckoutResult(
                success=True,
                order_id=order_result.order_id,
                payment_id=payment_result.payment_id,
                total_amount=total_amount
            )
            
        except Exception as e:
            self._execute_rollback(rollback_actions)
            return CheckoutResult(
                success=False,
                errors=[f"Unexpected error during checkout: {str(e)}"]
            )
    
    def _execute_rollback(self, rollback_actions: List[callable]):
        """Execute rollback actions in reverse order"""
        for action in reversed(rollback_actions):
            try:
                action()
            except Exception as e:
                # Log rollback failures but don't raise
                logger.error(f"Rollback action failed: {e}")

# services/checkout/payment_processor.py
from abc import ABC, abstractmethod
from typing import Dict, Any
from enum import Enum

class PaymentMethod(Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    STRIPE = "stripe"
    BANK_TRANSFER = "bank_transfer"

class PaymentProcessor(ABC):
    """Strategy pattern for different payment processors"""
    
    @abstractmethod
    def process_payment(self, amount: Decimal, payment_data: Dict) -> PaymentResult:
        pass
    
    @abstractmethod
    def refund_payment(self, payment_id: str) -> RefundResult:
        pass

class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: Decimal, payment_data: Dict) -> PaymentResult:
        # Stripe-specific implementation
        pass

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: Decimal, payment_data: Dict) -> PaymentResult:
        # PayPal-specific implementation
        pass

class PaymentProcessorFactory:
    """Factory pattern for payment processor creation"""
    
    @staticmethod
    def create_processor(payment_method: PaymentMethod) -> PaymentProcessor:
        processors = {
            PaymentMethod.STRIPE: StripePaymentProcessor,
            PaymentMethod.PAYPAL: PayPalPaymentProcessor,
            # Add more processors as needed
        }
        
        processor_class = processors.get(payment_method)
        if not processor_class:
            raise ValueError(f"Unsupported payment method: {payment_method}")
        
        return processor_class()

class PaymentProcessorService:
    """Main service for payment processing with strategy pattern"""
    
    def process_payment(self, amount: Decimal, payment_method: Dict, customer_id: int) -> PaymentResult:
        method_type = PaymentMethod(payment_method['type'])
        processor = PaymentProcessorFactory.create_processor(method_type)
        
        return processor.process_payment(amount, payment_method)
```

**Comprehensive Test Suite:**
```python
# tests/services/test_checkout_orchestrator.py
import pytest
from unittest.mock import Mock, patch
from services.checkout.orchestrator import CheckoutOrchestrator, CheckoutRequest
from services.checkout.payment_processor import PaymentMethod

class TestCheckoutOrchestrator:
    
    @pytest.fixture
    def orchestrator(self):
        return CheckoutOrchestrator()
    
    @pytest.fixture
    def sample_request(self):
        return CheckoutRequest(
            customer_id=123,
            items=[
                {'product_id': 1, 'quantity': 2, 'price': 29.99},
                {'product_id': 2, 'quantity': 1, 'price': 49.99}
            ],
            shipping_address={
                'street': '123 Main St',
                'city': 'San Francisco', 
                'state': 'CA',
                'zip': '94102'
            },
            payment_method={
                'type': 'stripe',
                'card_token': 'tok_visa'
            }
        )
    
    def test_successful_checkout_flow(self, orchestrator, sample_request):
        """Test complete successful checkout process"""
        
        # Mock all service responses as successful
        with patch.multiple(
            orchestrator,
            inventory_service=Mock(),
            tax_service=Mock(),
            shipping_service=Mock(),
            payment_service=Mock(),
            order_service=Mock(),
            notification_service=Mock()
        ):
            # Configure mock returns
            orchestrator.inventory_service.reserve_items.return_value = Mock(
                success=True, reservation_id='res_123', subtotal=Decimal('109.97')
            )
            orchestrator.tax_service.calculate_tax.return_value = Mock(
                tax_amount=Decimal('9.90')
            )
            orchestrator.shipping_service.calculate_shipping.return_value = Mock(
                shipping_cost=Decimal('5.99')
            )
            orchestrator.payment_service.process_payment.return_value = Mock(
                success=True, payment_id='pay_123'
            )
            orchestrator.order_service.create_order.return_value = Mock(
                success=True, order_id=456
            )
            
            result = orchestrator.process_checkout(sample_request)
            
            assert result.success is True
            assert result.order_id == 456
            assert result.payment_id == 'pay_123'
            assert result.total_amount == Decimal('125.86')
    
    def test_checkout_rollback_on_payment_failure(self, orchestrator, sample_request):
        """Test that rollback occurs when payment fails"""
        
        with patch.multiple(
            orchestrator,
            inventory_service=Mock(),
            tax_service=Mock(),
            shipping_service=Mock(),
            payment_service=Mock(),
        ):
            # Inventory succeeds, payment fails
            orchestrator.inventory_service.reserve_items.return_value = Mock(
                success=True, reservation_id='res_123', subtotal=Decimal('109.97')
            )
            orchestrator.payment_service.process_payment.return_value = Mock(
                success=False, errors=['Card declined']
            )
            
            result = orchestrator.process_checkout(sample_request)
            
            assert result.success is False
            assert 'Card declined' in result.errors
            
            # Verify rollback was called
            orchestrator.inventory_service.release_reservation.assert_called_once_with('res_123')
    
    def test_checkout_handles_unexpected_errors(self, orchestrator, sample_request):
        """Test graceful handling of unexpected errors"""
        
        with patch.object(orchestrator.inventory_service, 'reserve_items') as mock_reserve:
            mock_reserve.side_effect = Exception("Database connection error")
            
            result = orchestrator.process_checkout(sample_request)
            
            assert result.success is False
            assert len(result.errors) == 1
            assert "Unexpected error during checkout" in result.errors[0]

# Performance tests
class TestCheckoutPerformance:
    
    def test_checkout_performance_under_load(self):
        """Test checkout performance with concurrent requests"""
        import time
        import threading
        
        orchestrator = CheckoutOrchestrator()
        results = []
        
        def checkout_worker(request):
            start_time = time.time()
            result = orchestrator.process_checkout(request)
            end_time = time.time()
            results.append((result, end_time - start_time))
        
        # Simulate 100 concurrent checkout requests
        threads = []
        for i in range(100):
            request = create_sample_request(customer_id=i)
            thread = threading.Thread(target=checkout_worker, args=(request,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        # Verify performance requirements
        avg_response_time = sum(r[1] for r in results) / len(results)
        assert avg_response_time < 0.2  # Under 200ms average
        
        success_rate = sum(1 for r in results if r[0].success) / len(results)
        assert success_rate > 0.95  # >95% success rate
```

### Step 3: Production Deployment and Validation - `/protocol`
```bash
/protocol "deploy refactored checkout system with comprehensive monitoring and rollback capability"
```

**What the Framework Does:**
- Validates all tests pass with >95% coverage
- Performs A/B testing between old and new checkout
- Sets up comprehensive monitoring for performance metrics
- Creates automated rollback triggers
- Validates production deployment safety

**Framework Validation Output:**
```
🚀 REFACTORING DEPLOYMENT VALIDATION:

Code Quality Metrics:
✅ Test Coverage: 97.3% (target: >95%)
✅ Cyclomatic Complexity: Average 3.2 (target: <10)
✅ Lines per Function: Average 23 (target: <50)
✅ Service Coupling: Loose coupling achieved
✅ Dependency Injection: 100% implemented

Performance Benchmarks:
✅ Checkout Response Time: 156ms (target: <200ms)
✅ Database Queries: Reduced from 47 to 12 per checkout
✅ Memory Usage: Reduced by 34%
✅ Concurrent Handling: 500 concurrent checkouts (0% failures)

A/B Testing Results (7 days):
📊 Legacy Checkout (50% traffic):
   - Average response time: 847ms
   - Error rate: 2.3%
   - Conversion rate: 87.2%

📊 Refactored Checkout (50% traffic):  
   - Average response time: 156ms (82% improvement)
   - Error rate: 0.1% (95% improvement)
   - Conversion rate: 94.1% (8% improvement)

🧪 Comprehensive Testing:
✅ Unit Tests: 247 tests, 100% pass
✅ Integration Tests: 89 tests, 100% pass  
✅ Load Tests: 10,000 concurrent users, 0% failures
✅ Security Tests: All vulnerabilities resolved
✅ Rollback Tests: Complete rollback in 30 seconds

📊 MONITORING SETUP:
- Response time percentiles (p50, p95, p99)
- Error rate by checkout step
- Payment processor success rates
- Database connection pool metrics
- Service dependency health checks
- Business metrics (conversion rates, cart abandonment)

🎯 ROLLBACK TRIGGERS:
- Error rate > 1% for 2 consecutive minutes
- Average response time > 300ms for 5 minutes
- Any service dependency failure
- Manual trigger via operations dashboard

✅ PRODUCTION DEPLOYMENT APPROVED:
- Phased rollout: 5% → 25% → 50% → 100% over 4 days
- Feature flags enabled for instant rollback
- 24/7 monitoring for first week
- Success criteria validated at each phase
```

## Key Learning Points

### ✅ Refactoring Workflow Benefits
1. **Strategic Analysis**: `query` identifies architectural problems and opportunities
2. **Systematic Implementation**: `feature` creates comprehensive solution with PRD
3. **Safe Deployment**: `protocol` ensures production readiness with monitoring

### 📚 Architectural Improvements Achieved
- **Separation of Concerns**: Business logic separated from presentation
- **Testability**: 97% test coverage vs previous 23%
- **Performance**: 82% improvement in response time
- **Maintainability**: Modular services vs monolithic function
- **Extensibility**: Easy to add new payment methods and features

### 🔍 When to Use This Workflow
- ✅ Large-scale architectural improvements
- ✅ Legacy code modernization
- ✅ Performance optimization projects
- ✅ Maintainability improvements
- ✅ Adding testability to existing systems

### 🚀 Pattern Applications
- **Monolith Decomposition**: Breaking large functions/classes
- **Service Extraction**: Creating modular services
- **Design Pattern Implementation**: Strategy, Factory, Command patterns
- **Performance Optimization**: Database query optimization, caching

## Variations for Different Refactoring Types

### Database Schema Refactoring:
```bash
/query "analyze database schema for normalization and performance opportunities"
/feature "refactor database schema with migration strategy and data integrity"
/protocol "deploy schema changes with zero-downtime migration"
```

### API Refactoring:
```bash
/query "analyze API design for RESTful principles and performance issues"  
/feature "refactor API with backward compatibility and improved design"
/protocol "deploy API changes with versioning and client migration plan"
```

### Frontend Architecture Refactoring:
```bash
/query "analyze frontend architecture for component reusability and performance"
/feature "refactor frontend with modern patterns and component architecture" 
/protocol "deploy frontend changes with progressive enhancement strategy"
```

## Success Metrics

This refactoring workflow achieved:
- **82% Performance Improvement**: Response time reduced from 847ms to 156ms
- **95% Error Reduction**: Error rate from 2.3% to 0.1%
- **8% Conversion Increase**: Better user experience improved business metrics
- **97% Test Coverage**: From untestable to highly testable architecture
- **Maintainability**: Adding new features now takes hours instead of days

## Long-term Benefits

### For Development Team:
- **Faster Feature Development**: Modular architecture enables rapid iteration
- **Reduced Bug Rate**: Comprehensive testing catches issues early
- **Easier Debugging**: Clear separation of concerns simplifies troubleshooting
- **Knowledge Sharing**: Well-documented, testable code improves team velocity

### For Business:
- **Improved User Experience**: Faster, more reliable checkout process
- **Higher Conversion Rates**: Better performance leads to more completed purchases
- **Reduced Operational Costs**: Fewer errors and easier maintenance
- **Future-Proofing**: Architecture supports business growth and new requirements

This workflow transforms legacy code into modern, maintainable architecture while ensuring business continuity and improved performance.