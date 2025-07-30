---
name: /docs
description: "Create and maintain documentation for code and projects"
usage: /docs [--generate | --update | --api] [target]
category: core
tools: Read, Write, Edit, Bash, Grep, Glob
---

# Universal Documentation Generator

**Create comprehensive documentation for any codebase, API, or project.**

## Documentation Types

### Code Documentation
```
/docs --generate src/utils/parser.js
/docs --generate "authentication system documentation"
/docs --api src/routes/users.js
```

### Project Documentation
```
/docs --generate README
/docs --update "installation instructions"
/docs --generate "contributing guidelines"
```

### API Documentation
```
/docs --api src/controllers/
/docs --api "REST API endpoints"
/docs --generate "API usage examples"
```

## Documentation Generation

### Automatic Analysis
**I'll examine your code to generate:**
- **Function/method documentation** with parameters and return values
- **Class documentation** with properties and methods
- **API endpoint documentation** with request/response formats
- **Usage examples** with real code samples
- **Installation and setup guides**

### Smart Content Creation
**Documentation includes:**
- **Clear descriptions** in plain language
- **Code examples** that actually work
- **Parameter specifications** with types and constraints
- **Error handling** documentation
- **Integration examples** and best practices

## Example Documentation Generation

### Function Documentation
```
👤 /docs --generate src/auth/validateToken.js

🤖 Analyzing validateToken function...
🤖 Generating comprehensive documentation...

✅ Generated documentation:

## validateToken

Validates JWT tokens and extracts user information.

### Syntax
```javascript
const result = await validateToken(token, options);
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `token` | string | Yes | JWT token to validate |
| `options` | object | No | Configuration options |
| `options.issuer` | string | No | Expected token issuer |
| `options.audience` | string | No | Expected token audience |

### Returns

**Success Response:**
```javascript
{
  valid: true,
  user: {
    id: "12345",
    email: "user@example.com",
    roles: ["user"]
  },
  exp: 1640995200
}
```

**Error Response:**
```javascript
{
  valid: false,
  error: "Token expired",
  code: "TOKEN_EXPIRED"
}
```

### Usage Examples

**Basic Validation:**
```javascript
const { validateToken } = require('./auth/validateToken');

const result = await validateToken(userToken);
if (result.valid) {
  console.log('User:', result.user);
} else {
  console.log('Invalid token:', result.error);
}
```

**With Options:**
```javascript
const result = await validateToken(token, {
  issuer: 'myapp.com',
  audience: 'api.myapp.com'
});
```

### Error Handling

| Error Code | Description | Solution |
|------------|-------------|----------|
| `TOKEN_EXPIRED` | Token has expired | Request new token |
| `TOKEN_INVALID` | Token format invalid | Check token format |
| `TOKEN_SIGNATURE_INVALID` | Signature verification failed | Check signing key |

### Dependencies

- `jsonwebtoken`: Token parsing and validation
- `crypto`: Signature verification

### See Also

- [`generateToken()`](./generateToken.md) - Create new JWT tokens
- [`refreshToken()`](./refreshToken.md) - Refresh expired tokens
```

### API Documentation
```
👤 /docs --api src/routes/users.js

🤖 Analyzing user API endpoints...
🤖 Generating REST API documentation...

✅ Generated API Documentation:

# Users API

## Endpoints

### GET /api/users
Get list of users with optional filtering.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | integer | No | Page number (default: 1) |
| `limit` | integer | No | Items per page (default: 10, max: 100) |
| `role` | string | No | Filter by user role |
| `active` | boolean | No | Filter by active status |

**Example Request:**
```bash
GET /api/users?page=2&limit=20&role=admin&active=true
```

**Success Response (200):**
```json
{
  "users": [
    {
      "id": "12345",
      "email": "admin@example.com",
      "name": "Admin User",
      "role": "admin",
      "active": true,
      "createdAt": "2023-01-15T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

### POST /api/users
Create a new user account.

**Request Body:**
```json
{
  "email": "newuser@example.com",
  "name": "New User",
  "password": "securePassword123",
  "role": "user"
}
```

**Validation Rules:**
- `email`: Valid email format, unique
- `name`: 2-50 characters
- `password`: Minimum 8 characters, must include numbers
- `role`: One of: "user", "admin", "moderator"

**Success Response (201):**
```json
{
  "user": {
    "id": "67890",
    "email": "newuser@example.com",
    "name": "New User",
    "role": "user",
    "active": true,
    "createdAt": "2023-12-01T15:45:00Z"
  }
}
```

**Error Responses:**

**400 Bad Request** - Validation errors:
```json
{
  "error": "Validation failed",
  "details": [
    {
      "field": "email",
      "message": "Email already exists"
    }
  ]
}
```

**401 Unauthorized** - Missing or invalid authentication:
```json
{
  "error": "Authentication required"
}
```

### Authentication
All endpoints require JWT token in Authorization header:
```bash
Authorization: Bearer your-jwt-token-here
```

### Rate Limiting
- **Public endpoints**: 100 requests per hour per IP
- **Authenticated endpoints**: 1000 requests per hour per user
```

## Project Documentation

### README Generation
```
👤 /docs --generate README

🤖 Analyzing project structure...
🤖 Generating comprehensive README...

✅ Generated README.md:

# MyAwesome Project

A modern web application built with React and Node.js for managing user accounts and projects.

## Features

- 🔐 **User Authentication** - Secure JWT-based authentication
- 👥 **User Management** - Create, update, and manage user accounts  
- 📊 **Dashboard** - Real-time analytics and project overview
- 🔒 **Role-based Access** - Admin, moderator, and user roles
- 📱 **Responsive Design** - Mobile-first responsive interface

## Quick Start

### Prerequisites
- Node.js 18+ 
- npm or yarn
- PostgreSQL 13+

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/myawesome-project.git
cd myawesome-project
```

2. **Install dependencies**
```bash
npm install
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your database and API configurations
```

4. **Set up database**
```bash
npm run db:migrate
npm run db:seed
```

5. **Start development server**
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## Project Structure

```
src/
├── components/          # React components
│   ├── auth/           # Authentication components
│   ├── dashboard/      # Dashboard components
│   └── shared/         # Reusable components
├── pages/              # Page components
├── services/           # API services
├── utils/              # Utility functions
└── styles/             # CSS and styling

server/
├── controllers/        # API controllers
├── middleware/         # Express middleware
├── models/            # Database models
├── routes/            # API routes
└── utils/             # Server utilities
```

## API Documentation

See [API.md](./API.md) for complete API documentation.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

## Documentation Maintenance

### Keeping Docs Updated
```
👤 /docs --update "installation instructions changed"

🤖 Analyzing current installation documentation...
🤖 Identifying outdated sections...

📝 DOCUMENTATION UPDATES NEEDED:

**Outdated Sections Found:**
1. **Prerequisites** - Node.js version changed from 16+ to 18+
2. **Environment Setup** - New required variables added
3. **Database Setup** - Migration commands updated

**Updated Installation Section:**
```markdown
### Prerequisites
- Node.js 18+ (updated from 16+)
- npm or yarn  
- PostgreSQL 13+
- Redis 6+ (newly required for session management)

### Environment Variables
Copy `.env.example` to `.env` and configure:

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/myapp

# Authentication (updated)
JWT_SECRET=your-secret-key
JWT_EXPIRY=24h

# Redis (new requirement)
REDIS_URL=redis://localhost:6379

# Email Service (new)
SMTP_HOST=smtp.example.com
SMTP_USER=your-email@example.com
SMTP_PASS=your-password
```

### Database Setup (updated commands)
```bash
npm run db:setup     # Creates database and runs migrations
npm run db:seed      # Seeds initial data
```
```

✅ Updated documentation sections identified and fixed
🎯 Recommendation: Review monthly to keep documentation current
```

## Multi-Language Support

**Automatic documentation generation for:**
- **JavaScript/TypeScript**: JSDoc, TSDoc, function signatures
- **Python**: Docstrings, type hints, Sphinx compatibility
- **Java**: Javadoc, Spring annotations, API documentation
- **Go**: Go doc format, package documentation
- **Rust**: Rustdoc, crate documentation
- **C#**: XML documentation, API reference

## Documentation Best Practices

**I'll ensure documentation includes:**
- **Clear examples** that users can copy-paste
- **Complete parameter lists** with types and constraints
- **Error handling** documentation with common solutions
- **Integration guides** showing real-world usage
- **Version compatibility** information

**Documentation Standards:**
- **Consistent formatting** across all files
- **Up-to-date examples** that match current code
- **Searchable structure** with proper headings
- **Cross-references** between related functions
- **Visual elements** like diagrams when helpful

## Ready to Document?

Choose your documentation task:

```
/docs --generate [file-or-feature]    # Create new documentation
/docs --api [endpoint-or-controller]  # Generate API docs
/docs --update [section-to-update]    # Update existing docs
/docs README                          # Generate project README
```

I'll create comprehensive, accurate documentation for your project!