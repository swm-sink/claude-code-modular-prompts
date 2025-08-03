# Framework Detection Patterns

*Automated project type detection for Claude Code template adaptation*

## Core Detection Strategy

### File-Based Detection Matrix
```
JavaScript/TypeScript:
- package.json → Extract name, dependencies, scripts
- tsconfig.json → TypeScript configuration
- .babelrc, babel.config.js → Babel transpilation
- webpack.config.js → Module bundling
- next.config.js → Next.js framework
- nuxt.config.js → Nuxt.js framework

Python:
- requirements.txt → Pip dependencies
- setup.py → Package setup
- pyproject.toml → Modern Python packaging
- Pipfile → Pipenv dependencies
- manage.py → Django framework
- app.py, main.py → Flask/FastAPI patterns

Java:
- pom.xml → Maven build system
- build.gradle → Gradle build system
- application.properties → Spring Boot
- web.xml → Traditional servlet

Go:
- go.mod → Go modules
- main.go → Entry point
- Dockerfile → Containerization

Rust:
- Cargo.toml → Cargo package manager
- src/main.rs → Binary crate
- src/lib.rs → Library crate

Other:
- composer.json → PHP
- Gemfile → Ruby
- .csproj → C#/.NET
- CMakeLists.txt → C/C++
```

## Framework-Specific Patterns

### React Detection
```javascript
// package.json indicators
"dependencies": {
  "react": "^18.0.0",
  "react-dom": "^18.0.0"
}

// File structure indicators
src/App.js, src/index.js, public/index.html

// Additional frameworks
"next": "^13.0.0" → Next.js
"@remix-run/react" → Remix
"gatsby": "^5.0.0" → Gatsby
```

### Backend Framework Detection
```python
# Django indicators
manage.py, settings.py, urls.py, wsgi.py

# Flask indicators  
app.py with from flask import Flask

# FastAPI indicators
main.py with from fastapi import FastAPI

# Express.js indicators
package.json with "express": "^4.0.0"
app.js with express() initialization
```

### Database Detection
```yaml
# SQL Databases
- PostgreSQL: psycopg2, pg, DATABASE_URL=postgres://
- MySQL: mysql2, pymysql, DATABASE_URL=mysql://
- SQLite: sqlite3, better-sqlite3, *.db files

# NoSQL Databases  
- MongoDB: mongoose, pymongo, MONGODB_URI
- Redis: redis, ioredis, REDIS_URL
- Elasticsearch: @elastic/elasticsearch
```

## Automated Placeholder Replacement

### Project Metadata Extraction
```javascript
// From package.json
{
  "name": "my-awesome-app", // → [INSERT_PROJECT_NAME]
  "description": "...",      // → [INSERT_DESCRIPTION]
  "author": "John Doe",      // → [INSERT_AUTHOR]
  "license": "MIT"           // → [INSERT_LICENSE]
}

// From git config
git config user.name  // → [INSERT_AUTHOR]
git config user.email // → [INSERT_EMAIL]

// From directory structure
src/components/ → React/Vue component architecture
controllers/ → MVC pattern
models/ → Data modeling
tests/ → Testing setup
```

### Tech Stack Classification
```yaml
Frontend Frameworks:
- React: "react", "react-dom", "next", "gatsby"
- Vue: "vue", "nuxt", "@vue/cli"
- Angular: "@angular/core", "@angular/cli"
- Svelte: "svelte", "sveltekit"

Backend Patterns:
- API Server: express, fastapi, spring-boot
- Full Stack: next.js, nuxt.js, django
- Microservices: docker-compose.yml, kubernetes/
- Serverless: serverless.yml, netlify.toml

Development Tools:
- Bundlers: webpack, vite, rollup, parcel
- Testing: jest, pytest, mocha, cypress
- Linting: eslint, pylint, prettier
- CI/CD: .github/workflows/, .gitlab-ci.yml
```

## Domain Classification

### Project Type Detection
```javascript
// Web Application
Frontend + Backend + Database = Full Stack Web App

// API Service  
Express/FastAPI + Database + No Frontend = REST API

// Static Site
HTML/CSS/JS + No Backend = Static Website

// Mobile App
react-native, flutter, ionic = Mobile Application

// CLI Tool
bin/ directory, commander.js, click (Python) = Command Line Tool

// Library/Package
No main entry point, focused on exports = Library/Package
```

### Use Case Patterns
```yaml
E-commerce:
- Dependencies: stripe, paypal, shopify
- Files: cart.js, checkout.js, products/
- Database: orders, products, users tables

SaaS Application:
- Authentication: auth0, firebase-auth, passport
- Subscription: stripe subscriptions
- Multi-tenancy: tenant isolation patterns

Content Management:
- CMS: contentful, strapi, sanity
- Static generators: gatsby, next.js, hugo
- Content files: markdown, MDX

Data Processing:
- Python: pandas, numpy, jupyter notebooks
- Databases: data warehouses, ETL pipelines
- Files: *.csv, *.json data files
```

## Automation Triggers

### When to Auto-Replace Placeholders
1. **High Confidence Detection** (>90% certainty)
   - Clear package.json with standard patterns
   - Conventional file structure
   - Standard naming conventions

2. **Medium Confidence** (70-90% certainty)
   - Partial indicators present
   - Non-standard but recognizable patterns
   - Require user confirmation

3. **Low Confidence** (<70% certainty)
   - Ambiguous project structure
   - Multiple possible interpretations
   - Fall back to manual customization guide

### Validation Patterns
```bash
# Verify detection accuracy
package.json exists && has valid JSON structure
main entry point exists (index.js, main.py, etc.)
dependencies are resolvable
build/test scripts are functional

# Cross-reference multiple indicators
File structure + dependencies + scripts alignment
Git history shows consistent patterns
README.md mentions detected frameworks
```

This framework detection system enables true automation of template customization based on project analysis rather than manual placeholder replacement.