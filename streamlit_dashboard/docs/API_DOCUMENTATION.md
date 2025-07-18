# Claude Code Modular Prompts Dashboard - API Documentation

## Overview

This document provides comprehensive API documentation for the Claude Code Modular Prompts Dashboard. The API provides programmatic access to all dashboard functionality including template management, component access, performance monitoring, and sharing capabilities.

## Table of Contents

1. [Authentication](#authentication)
2. [Base URLs and Endpoints](#base-urls-and-endpoints)
3. [Template Manager API](#template-manager-api)
4. [Framework Explorer API](#framework-explorer-api)
5. [URL Sharing API](#url-sharing-api)
6. [Performance Monitoring API](#performance-monitoring-api)
7. [Error Handling](#error-handling)
8. [Rate Limiting](#rate-limiting)
9. [SDKs and Examples](#sdks-and-examples)

## Authentication

The API uses session-based authentication through Streamlit's session state management. For programmatic access, authentication tokens can be generated through the dashboard interface.

### Session Management

```python
import streamlit as st

# Initialize session
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_id = None
    st.session_state.session_id = generate_session_id()
```

### API Key Authentication

For external API access, generate an API key:

```python
from components.auth import generate_api_key

api_key = generate_api_key(user_id="your_user_id")
headers = {"Authorization": f"Bearer {api_key}"}
```

## Base URLs and Endpoints

### Development Environment
```
Base URL: http://localhost:8501/api/v1
```

### Production Environment
```
Base URL: https://your-domain.com/api/v1
```

### API Versioning

The API uses semantic versioning with the version specified in the URL path:
- `/api/v1/` - Current stable version
- `/api/v2/` - Next major version (when available)

## Template Manager API

### Template Operations

#### List Templates

```http
GET /api/v1/templates
```

**Query Parameters:**
- `category` (optional): Filter by category
- `author` (optional): Filter by author
- `tag` (optional): Filter by tag
- `limit` (optional): Number of results (default: 50)
- `offset` (optional): Pagination offset (default: 0)

**Response:**
```json
{
  "status": "success",
  "data": {
    "templates": [
      {
        "id": "template_001",
        "name": "Development Workflow",
        "description": "Standard development workflow template",
        "category": "development",
        "author": "Claude Assistant",
        "version": "1.0.0",
        "created_at": "2025-07-18T10:00:00Z",
        "updated_at": "2025-07-18T10:00:00Z",
        "components": [
          {
            "type": "command",
            "name": "task",
            "file": "commands/task.md"
          }
        ],
        "metadata": {
          "framework_version": "3.0.0",
          "tags": ["development", "workflow"],
          "difficulty": "intermediate"
        }
      }
    ],
    "total": 1,
    "has_more": false
  }
}
```

#### Get Template Details

```http
GET /api/v1/templates/{template_id}
```

**Path Parameters:**
- `template_id` (required): Unique template identifier

**Response:**
```json
{
  "status": "success",
  "data": {
    "template": {
      "id": "template_001",
      "name": "Development Workflow",
      "description": "Standard development workflow template",
      "category": "development",
      "author": "Claude Assistant",
      "version": "1.0.0",
      "created_at": "2025-07-18T10:00:00Z",
      "updated_at": "2025-07-18T10:00:00Z",
      "components": [
        {
          "type": "command",
          "name": "task",
          "file": "commands/task.md",
          "dependencies": []
        }
      ],
      "metadata": {
        "framework_version": "3.0.0",
        "tags": ["development", "workflow"],
        "difficulty": "intermediate",
        "estimated_time": "30 minutes",
        "prerequisites": []
      }
    }
  }
}
```

#### Create Template

```http
POST /api/v1/templates
```

**Request Body:**
```json
{
  "name": "New Template",
  "description": "Description of the new template",
  "category": "development",
  "author": "Your Name",
  "version": "1.0.0",
  "components": [
    {
      "type": "command",
      "name": "task",
      "file": "commands/task.md"
    }
  ],
  "metadata": {
    "framework_version": "3.0.0",
    "tags": ["development", "custom"],
    "difficulty": "beginner"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "template": {
      "id": "template_002",
      "name": "New Template",
      "created_at": "2025-07-18T10:15:00Z",
      "validation_status": "valid",
      "validation_errors": []
    }
  }
}
```

#### Update Template

```http
PUT /api/v1/templates/{template_id}
```

**Request Body:** Same as create template

**Response:**
```json
{
  "status": "success",
  "data": {
    "template": {
      "id": "template_002",
      "updated_at": "2025-07-18T10:30:00Z",
      "validation_status": "valid",
      "validation_errors": []
    }
  }
}
```

#### Delete Template

```http
DELETE /api/v1/templates/{template_id}
```

**Response:**
```json
{
  "status": "success",
  "message": "Template deleted successfully"
}
```

#### Validate Template

```http
POST /api/v1/templates/{template_id}/validate
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "validation_status": "valid",
    "validation_errors": [],
    "warnings": [],
    "component_validation": {
      "commands/task.md": {
        "status": "valid",
        "exists": true,
        "dependencies_met": true
      }
    }
  }
}
```

## Framework Explorer API

### Component Operations

#### List Components

```http
GET /api/v1/components
```

**Query Parameters:**
- `type` (optional): Filter by component type (command, module, system, etc.)
- `category` (optional): Filter by category
- `search` (optional): Search in component names and descriptions

**Response:**
```json
{
  "status": "success",
  "data": {
    "components": [
      {
        "id": "task_command",
        "name": "task",
        "type": "command",
        "path": ".claude/commands/task.md",
        "description": "Single component focused development with TDD",
        "version": "3.0.0",
        "dependencies": ["tdd-cycle-pattern", "quality-gates"],
        "metadata": {
          "author": "Claude Framework",
          "usage": "Single file changes, bug fixes, <50 lines of code"
        }
      }
    ]
  }
}
```

#### Get Component Details

```http
GET /api/v1/components/{component_id}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "component": {
      "id": "task_command",
      "name": "task",
      "type": "command",
      "path": ".claude/commands/task.md",
      "content": "# /task Command\n\n## Purpose\n...",
      "description": "Single component focused development with TDD",
      "version": "3.0.0",
      "dependencies": ["tdd-cycle-pattern", "quality-gates"],
      "dependents": ["feature-command", "auto-command"],
      "metadata": {
        "author": "Claude Framework",
        "created_at": "2025-07-18T10:00:00Z",
        "updated_at": "2025-07-18T10:00:00Z",
        "usage": "Single file changes, bug fixes, <50 lines of code",
        "examples": [
          "/task \"fix the login validation bug\"",
          "/task \"add unit tests for the user service\""
        ]
      }
    }
  }
}
```

#### Get Component Dependencies

```http
GET /api/v1/components/{component_id}/dependencies
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "dependencies": {
      "direct": [
        {
          "id": "tdd-cycle-pattern",
          "name": "TDD Cycle Pattern",
          "type": "module",
          "required": true
        }
      ],
      "indirect": [
        {
          "id": "quality-gates",
          "name": "Quality Gates",
          "type": "system",
          "required": true
        }
      ]
    },
    "dependency_graph": {
      "nodes": [
        {"id": "task_command", "type": "command"},
        {"id": "tdd-cycle-pattern", "type": "module"}
      ],
      "edges": [
        {"from": "task_command", "to": "tdd-cycle-pattern"}
      ]
    }
  }
}
```

## URL Sharing API

### Sharing Operations

#### Generate Sharing URL

```http
POST /api/v1/sharing/generate
```

**Request Body:**
```json
{
  "template_id": "template_001",
  "expires_in_days": 30,
  "max_access_count": 100,
  "base_url": "https://your-domain.com/share"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "token": "abc123def456ghi789",
    "share_url": "https://your-domain.com/share/abc123def456ghi789",
    "expires_at": "2025-08-17T10:00:00Z",
    "max_access_count": 100,
    "created_at": "2025-07-18T10:00:00Z"
  }
}
```

#### Access Shared Template

```http
GET /api/v1/sharing/access/{token}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "template": {
      "id": "template_001",
      "name": "Development Workflow",
      "description": "Standard development workflow template",
      "category": "development",
      "author": "Claude Assistant",
      "version": "1.0.0",
      "components": [...],
      "metadata": {...},
      "sharing_info": {
        "shared_by": "Claude Assistant",
        "shared_at": "2025-07-18T10:00:00Z",
        "access_count": 1
      }
    }
  }
}
```

#### Validate Sharing Token

```http
GET /api/v1/sharing/validate/{token}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "valid": true,
    "token_info": {
      "token": "abc123def456ghi789",
      "template_id": "template_001",
      "expires_at": "2025-08-17T10:00:00Z",
      "access_count": 1,
      "max_access_count": 100,
      "is_expired": false,
      "is_access_limit_reached": false
    }
  }
}
```

#### Revoke Sharing Token

```http
DELETE /api/v1/sharing/revoke/{token}
```

**Response:**
```json
{
  "status": "success",
  "message": "Token revoked successfully"
}
```

#### Get Sharing Statistics

```http
GET /api/v1/sharing/statistics
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "total_shared_templates": 5,
    "total_access_count": 150,
    "active_tokens": 3,
    "expired_tokens": 2,
    "access_limited_tokens": 0,
    "most_accessed_templates": [
      {
        "template_id": "template_001",
        "name": "Development Workflow",
        "access_count": 50
      }
    ]
  }
}
```

## Performance Monitoring API

### Metrics Operations

#### Get Current Metrics

```http
GET /api/v1/metrics/current
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "metrics": {
      "memory_usage": {
        "value": 128.5,
        "unit": "MB",
        "timestamp": "2025-07-18T10:00:00Z"
      },
      "cpu_usage": {
        "value": 15.2,
        "unit": "percent",
        "timestamp": "2025-07-18T10:00:00Z"
      },
      "active_sessions": {
        "value": 3,
        "unit": "sessions",
        "timestamp": "2025-07-18T10:00:00Z"
      }
    }
  }
}
```

#### Get Metrics History

```http
GET /api/v1/metrics/history
```

**Query Parameters:**
- `metric_name` (optional): Filter by specific metric
- `start_time` (optional): Start time for range query
- `end_time` (optional): End time for range query
- `interval` (optional): Aggregation interval (minute, hour, day)

**Response:**
```json
{
  "status": "success",
  "data": {
    "metrics": [
      {
        "name": "memory_usage",
        "values": [
          {
            "timestamp": "2025-07-18T10:00:00Z",
            "value": 128.5,
            "unit": "MB"
          }
        ]
      }
    ]
  }
}
```

#### Record Custom Metric

```http
POST /api/v1/metrics/record
```

**Request Body:**
```json
{
  "name": "custom_metric",
  "value": 42.0,
  "unit": "units",
  "category": "custom",
  "metadata": {
    "source": "api",
    "user_id": "user123"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Metric recorded successfully"
}
```

#### Get Performance Summary

```http
GET /api/v1/metrics/summary
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "summary": {
      "total_metrics": 1500,
      "categories": {
        "system": {
          "count": 800,
          "latest_timestamp": "2025-07-18T10:00:00Z"
        },
        "performance": {
          "count": 700,
          "latest_timestamp": "2025-07-18T10:00:00Z"
        }
      },
      "session_info": {
        "session_id": "session_12345",
        "uptime": 7200,
        "request_count": 150,
        "error_count": 2
      }
    }
  }
}
```

## Error Handling

### Error Response Format

All API errors follow a consistent format:

```json
{
  "status": "error",
  "error": {
    "code": "TEMPLATE_NOT_FOUND",
    "message": "Template with ID 'template_001' was not found",
    "details": {
      "template_id": "template_001",
      "suggestion": "Check that the template ID is correct and the template exists"
    }
  }
}
```

### HTTP Status Codes

- `200 OK` - Successful request
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid request parameters
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Access denied
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Validation error
- `429 Too Many Requests` - Rate limit exceeded
- `500 Internal Server Error` - Server error

### Common Error Codes

- `TEMPLATE_NOT_FOUND` - Template does not exist
- `TEMPLATE_VALIDATION_ERROR` - Template validation failed
- `COMPONENT_NOT_FOUND` - Component does not exist
- `SHARING_TOKEN_INVALID` - Invalid or expired sharing token
- `SHARING_TOKEN_EXPIRED` - Sharing token has expired
- `SHARING_ACCESS_LIMIT_REACHED` - Token access limit reached
- `AUTHENTICATION_REQUIRED` - Authentication required for this endpoint
- `PERMISSION_DENIED` - Insufficient permissions
- `RATE_LIMIT_EXCEEDED` - API rate limit exceeded
- `VALIDATION_ERROR` - Input validation failed

## Rate Limiting

The API implements rate limiting to ensure fair usage:

### Rate Limits

- **Standard endpoints**: 100 requests per minute per IP
- **Template operations**: 50 requests per minute per user
- **Sharing operations**: 20 requests per minute per user
- **Metrics recording**: 200 requests per minute per user

### Rate Limit Headers

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1642781400
```

### Rate Limit Exceeded Response

```json
{
  "status": "error",
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Please try again later.",
    "details": {
      "limit": 100,
      "remaining": 0,
      "reset_time": "2025-07-18T10:01:00Z"
    }
  }
}
```

## SDKs and Examples

### Python SDK

```python
import requests
from typing import Dict, Any, Optional

class ClaudeCodeDashboardAPI:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def list_templates(self, category: Optional[str] = None) -> Dict[str, Any]:
        """List all templates"""
        params = {}
        if category:
            params['category'] = category
        
        response = requests.get(
            f"{self.base_url}/api/v1/templates",
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json()
    
    def get_template(self, template_id: str) -> Dict[str, Any]:
        """Get template details"""
        response = requests.get(
            f"{self.base_url}/api/v1/templates/{template_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def create_template(self, template_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new template"""
        response = requests.post(
            f"{self.base_url}/api/v1/templates",
            headers=self.headers,
            json=template_data
        )
        response.raise_for_status()
        return response.json()
    
    def generate_sharing_url(self, template_id: str, expires_in_days: int = 30) -> Dict[str, Any]:
        """Generate sharing URL for a template"""
        response = requests.post(
            f"{self.base_url}/api/v1/sharing/generate",
            headers=self.headers,
            json={
                "template_id": template_id,
                "expires_in_days": expires_in_days
            }
        )
        response.raise_for_status()
        return response.json()

# Usage example
api = ClaudeCodeDashboardAPI(
    base_url="http://localhost:8501",
    api_key="your_api_key"
)

# List templates
templates = api.list_templates(category="development")
print(f"Found {len(templates['data']['templates'])} templates")

# Create a new template
new_template = {
    "name": "API Test Template",
    "description": "Template created via API",
    "category": "development",
    "author": "API User",
    "version": "1.0.0",
    "components": [
        {
            "type": "command",
            "name": "task",
            "file": "commands/task.md"
        }
    ],
    "metadata": {
        "framework_version": "3.0.0",
        "tags": ["api", "test"]
    }
}

created_template = api.create_template(new_template)
print(f"Created template: {created_template['data']['template']['id']}")
```

### JavaScript SDK

```javascript
class ClaudeCodeDashboardAPI {
    constructor(baseUrl, apiKey) {
        this.baseUrl = baseUrl;
        this.headers = {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json'
        };
    }
    
    async listTemplates(category = null) {
        const params = new URLSearchParams();
        if (category) params.append('category', category);
        
        const response = await fetch(
            `${this.baseUrl}/api/v1/templates?${params}`,
            { headers: this.headers }
        );
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }
    
    async getTemplate(templateId) {
        const response = await fetch(
            `${this.baseUrl}/api/v1/templates/${templateId}`,
            { headers: this.headers }
        );
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }
    
    async createTemplate(templateData) {
        const response = await fetch(
            `${this.baseUrl}/api/v1/templates`,
            {
                method: 'POST',
                headers: this.headers,
                body: JSON.stringify(templateData)
            }
        );
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }
}

// Usage example
const api = new ClaudeCodeDashboardAPI('http://localhost:8501', 'your_api_key');

// List templates
api.listTemplates('development')
    .then(templates => {
        console.log(`Found ${templates.data.templates.length} templates`);
    })
    .catch(error => {
        console.error('Error:', error);
    });
```

### cURL Examples

#### List Templates
```bash
curl -X GET \
  "http://localhost:8501/api/v1/templates" \
  -H "Authorization: Bearer your_api_key" \
  -H "Content-Type: application/json"
```

#### Create Template
```bash
curl -X POST \
  "http://localhost:8501/api/v1/templates" \
  -H "Authorization: Bearer your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "cURL Test Template",
    "description": "Template created via cURL",
    "category": "development",
    "author": "API User",
    "version": "1.0.0",
    "components": [
      {
        "type": "command",
        "name": "task",
        "file": "commands/task.md"
      }
    ],
    "metadata": {
      "framework_version": "3.0.0",
      "tags": ["api", "curl"]
    }
  }'
```

#### Generate Sharing URL
```bash
curl -X POST \
  "http://localhost:8501/api/v1/sharing/generate" \
  -H "Authorization: Bearer your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "template_id": "template_001",
    "expires_in_days": 30,
    "max_access_count": 100
  }'
```

## Versioning and Compatibility

### API Versioning

The API uses semantic versioning with the following compatibility guarantee:

- **Major version** (v1, v2): Breaking changes
- **Minor version** (v1.1, v1.2): New features, backward compatible
- **Patch version** (v1.1.1, v1.1.2): Bug fixes, backward compatible

### Deprecation Policy

- Features are deprecated with 6 months notice
- Deprecated features are marked in API responses
- Migration guides are provided for breaking changes

### Change Log

#### Version 1.0.0 (2025-07-18)
- Initial API release
- Template management endpoints
- Framework explorer endpoints
- URL sharing functionality
- Performance monitoring endpoints

---

*Last Updated: 2025-07-18*
*API Version: 1.0.0*