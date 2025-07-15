# Feature Development Example

## Overview
This example demonstrates how to use the `/feature` command for complete feature development with PRD creation, planning, implementation, and validation.

## Example Scenario
You need to add a shopping cart system to your e-commerce application.

## Step-by-Step Walkthrough

### 1. Issue the Command
```bash
/feature "shopping cart system for e-commerce site"
```

### 2. Expected Framework Response
The framework will:
1. **Create PRD**: Generate Product Requirements Document
2. **Analyze dependencies**: Identify related systems and components
3. **Plan architecture**: Design the feature structure
4. **Create implementation plan**: Break down into manageable tasks
5. **Implement with TDD**: Build each component test-first
6. **Validate feature**: Ensure all requirements are met

### 3. Sample Framework Output - PRD Generation
```
📋 GENERATING PRODUCT REQUIREMENTS DOCUMENT...

# Shopping Cart System PRD

## Executive Summary
Implement a complete shopping cart system enabling users to add, remove, and purchase items with persistent storage and checkout integration.

## User Stories
1. As a user, I want to add items to my cart so I can purchase multiple items
2. As a user, I want to view my cart contents and total price
3. As a user, I want to update quantities or remove items
4. As a user, I want my cart to persist between sessions
5. As a user, I want to proceed to checkout from my cart

## Technical Requirements
- Cart persistence (database storage)
- Integration with existing product catalog
- Real-time price calculations
- Session management
- Checkout process integration

## Success Criteria
- Users can add/remove items with immediate UI feedback
- Cart persists across browser sessions
- Accurate price calculations including taxes/shipping
- Performance: <200ms response time for cart operations
- Test coverage: >90% for all cart functionality
```

### 4. Architecture Planning
```
🏗️ FEATURE ARCHITECTURE PLAN:

Components:
1. Cart Model (data persistence)
2. CartItem Model (individual items)
3. Cart Service (business logic)
4. Cart API (REST endpoints)
5. Cart UI Components (frontend)
6. Cart Middleware (session management)

Database Schema:
- carts table (id, user_id, created_at, updated_at)
- cart_items table (id, cart_id, product_id, quantity, price)

API Endpoints:
- GET /api/cart/ - Get current cart
- POST /api/cart/items/ - Add item to cart
- PUT /api/cart/items/{id}/ - Update item quantity
- DELETE /api/cart/items/{id}/ - Remove item
- POST /api/cart/checkout/ - Proceed to checkout
```

### 5. Implementation Plan
```
📋 IMPLEMENTATION PHASES:

Phase 1: Data Models (TDD)
- Create Cart model with tests
- Create CartItem model with tests
- Database migrations

Phase 2: Business Logic (TDD)
- Cart service with add/remove/update operations
- Price calculation logic
- Inventory validation

Phase 3: API Layer (TDD)
- REST API endpoints
- Request/response validation
- Error handling

Phase 4: Frontend Integration (TDD)
- Cart UI components
- Real-time updates
- User experience polish

Phase 5: Integration Testing
- End-to-end testing
- Performance validation
- Security testing
```

### 6. Generated Implementation - Phase 1

**Cart Model (`src/cart/models.py`):**
```python
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Cart for {self.user.username}"
    
    @property
    def total_items(self):
        return self.items.aggregate(
            total=models.Sum('quantity')
        )['total'] or 0
    
    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['cart', 'product']
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name} in cart"
    
    @property
    def subtotal(self):
        return self.quantity * self.product.price
```

**Test Files (`tests/cart/test_models.py`):**
```python
import pytest
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from products.models import Product

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def product():
    return Product.objects.create(name='Test Product', price=29.99)

@pytest.fixture
def cart(user):
    return Cart.objects.create(user=user)

def test_cart_creation(user):
    cart = Cart.objects.create(user=user)
    assert cart.user == user
    assert cart.total_items == 0
    assert cart.total_price == 0

def test_cart_item_creation(cart, product):
    item = CartItem.objects.create(cart=cart, product=product, quantity=2)
    assert item.cart == cart
    assert item.product == product
    assert item.quantity == 2
    assert item.subtotal == 59.98

def test_cart_total_calculation(cart, product):
    CartItem.objects.create(cart=cart, product=product, quantity=3)
    assert cart.total_items == 3
    assert cart.total_price == 89.97
```

### 7. Generated Implementation - Phase 2

**Cart Service (`src/cart/services.py`):**
```python
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from products.models import Product

class CartService:
    def __init__(self, user):
        self.user = user
        self.cart, created = Cart.objects.get_or_create(user=user)
    
    def add_item(self, product_id, quantity=1):
        product = get_object_or_404(Product, id=product_id)
        
        # Check inventory
        if product.stock < quantity:
            raise ValueError(f"Only {product.stock} items available")
        
        item, created = CartItem.objects.get_or_create(
            cart=self.cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            item.quantity += quantity
            item.save()
        
        return item
    
    def remove_item(self, product_id):
        CartItem.objects.filter(
            cart=self.cart,
            product_id=product_id
        ).delete()
    
    def update_quantity(self, product_id, quantity):
        if quantity <= 0:
            self.remove_item(product_id)
            return
        
        item = CartItem.objects.get(
            cart=self.cart,
            product_id=product_id
        )
        item.quantity = quantity
        item.save()
        return item
    
    def clear_cart(self):
        self.cart.items.all().delete()
```

### 8. Generated Implementation - Phase 3

**API Views (`src/cart/views.py`):**
```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from .services import CartService
from .serializers import CartSerializer, CartItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart
    
    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        cart_service = CartService(request.user)
        try:
            item = cart_service.add_item(
                product_id=request.data['product_id'],
                quantity=request.data.get('quantity', 1)
            )
            return Response(CartItemSerializer(item).data)
        except ValueError as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    @action(detail=True, methods=['delete'])
    def remove_item(self, request, pk=None):
        cart_service = CartService(request.user)
        cart_service.remove_item(request.data['product_id'])
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### 9. Generated Implementation - Phase 4

**Frontend Components (React example):**
```jsx
// CartComponent.js
import React, { useState, useEffect } from 'react';
import api from '../services/api';

const CartComponent = () => {
  const [cart, setCart] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchCart();
  }, []);

  const fetchCart = async () => {
    try {
      const response = await api.get('/api/cart/');
      setCart(response.data);
    } catch (error) {
      console.error('Error fetching cart:', error);
    } finally {
      setLoading(false);
    }
  };

  const addItem = async (productId, quantity = 1) => {
    try {
      await api.post('/api/cart/add_item/', {
        product_id: productId,
        quantity: quantity
      });
      fetchCart(); // Refresh cart
    } catch (error) {
      console.error('Error adding item:', error);
    }
  };

  const removeItem = async (productId) => {
    try {
      await api.delete('/api/cart/remove_item/', {
        data: { product_id: productId }
      });
      fetchCart(); // Refresh cart
    } catch (error) {
      console.error('Error removing item:', error);
    }
  };

  if (loading) return <div>Loading cart...</div>;

  return (
    <div className="cart-container">
      <h2>Shopping Cart</h2>
      {cart && cart.items.length > 0 ? (
        <div>
          {cart.items.map(item => (
            <div key={item.id} className="cart-item">
              <span>{item.product.name}</span>
              <span>Quantity: {item.quantity}</span>
              <span>Price: ${item.subtotal}</span>
              <button onClick={() => removeItem(item.product.id)}>
                Remove
              </button>
            </div>
          ))}
          <div className="cart-total">
            <strong>Total: ${cart.total_price}</strong>
          </div>
          <button className="checkout-btn">Proceed to Checkout</button>
        </div>
      ) : (
        <p>Your cart is empty</p>
      )}
    </div>
  );
};

export default CartComponent;
```

### 10. Validation and Testing
```bash
# Run all tests
pytest tests/cart/ -v

# Test API endpoints
python manage.py test cart.tests.test_views

# Frontend tests
npm test -- --testPathPattern=cart

# Integration tests
python manage.py test cart.tests.test_integration
```

## Key Learning Points

### ✅ What the Framework Does Well
- **Complete Feature Lifecycle**: From PRD to implementation
- **Architectural Planning**: Thoughtful system design
- **TDD Throughout**: Tests for every component
- **Integration Ready**: All components work together
- **Documentation**: Comprehensive documentation and examples

### 📚 Best Practices Demonstrated
1. **Requirements First**: Clear PRD before implementation
2. **Modular Design**: Separate concerns (models, services, views)
3. **Test-Driven**: Tests written before implementation
4. **API-First**: RESTful API design
5. **Frontend Integration**: Complete user experience

### 🔍 Command Variations to Try
```bash
# More specific features
/feature "shopping cart with discount codes and promotions"

# Different complexity levels
/feature "simple wishlist functionality"

# Integration focused
/feature "shopping cart with payment gateway integration"
```

## Next Steps

1. **Deploy**: Set up staging environment for testing
2. **User Testing**: Gather feedback on cart functionality
3. **Optimize**: Performance tuning and caching
4. **Extend**: Add related features like wishlists or recommendations

## Common Patterns

### When to Use `/feature`
- ✅ Complete new functionality
- ✅ Multi-component systems
- ✅ User-facing features
- ✅ Features requiring PRD

### When to Use Other Commands
- `/task` for individual components within the feature
- `/query` for understanding existing cart implementations
- `/auto` when unsure about feature scope

This example demonstrates the `/feature` command's power for complete feature development with proper planning, architecture, and implementation.