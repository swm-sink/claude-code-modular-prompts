---
name: /demo-api-integration
description: "Demonstrate API integration pattern with validation and transformation"
usage: "[api_endpoint] [output_format]"
allowed-tools: Read, Write, Edit, Grep, WebFetch
category: examples
---

# API Integration Demo - External Data Processing

*This command demonstrates API integration with data processing (123.1% score)*

## Step 1: Call External API
```
Make API call to external service:
- Construct proper API request with headers and parameters
- Handle authentication if required (API keys, tokens)
- Execute HTTP request with appropriate method (GET, POST, etc.)
- Manage timeout and retry logic for reliability
- Capture response data and status codes
```

## Step 2: Validate API Response
```
Validate the API response:
- Check HTTP status codes for success/failure
- Validate response format matches expected schema
- Verify required fields are present and correctly typed
- Check for error messages or warning indicators
- Ensure data integrity and completeness
```

## Step 3: Transform Response Data
```
Transform data to specified format:
- Parse input data structure
- Convert to target format (preserving data integrity)
- Apply formatting rules for target type
- Validate transformation result
- Prepare formatted output for writing
```

## Step 4: Format Final Output
```
Format the final output:
- Apply consistent formatting rules
- Add headers, metadata, or structure as needed
- Ensure output meets target format specifications
- Include summary information
- Prepare formatted content for display or saving
```

**Pattern Score: 123.1% (Strong Performance)**  
**Components Used: 4 (api-caller, response-validator, data-transformer, output-formatter)**  
**Validation Status: ✅ Strong Performance - Reliable External Integration**