---
name: /find-commands
description: Smart command discovery tool with filtering and search capabilities (v2.0)
version: 2.0
usage: '/find-commands [category] [keyword] [--list-categories]'
category: meta
allowed-tools:  
- Read
- LS
- Grep
dependencies:
- /help
- /welcome
validation:
  pre-execution: Validate search parameters and category filters
  during-execution: Search through command library efficiently
  post-execution: Present results in organized format
progressive-disclosure:
  layer-integration: Command discovery for all system layers
  escalation-path: Browse categories → keyword search → advanced filtering
  de-escalation: Simple category listing
safety-measures:
  - Validate search patterns
  - Limit result sets for performance
  - Handle missing commands gracefully
  - Cache search results
error-recovery:
  no-results: Suggest alternative search terms
  invalid-category: Show available categories
  search-error: Fallback to basic listing
---

# /find-commands - Smart Command Discovery

I'll help you discover available commands with category [CATEGORY], keyword [KEYWORD], or list all categories with --list-categories.

## Implementation

I'll search through the available commands and provide:
- Commands matching your criteria
- Brief descriptions of each command
- Usage examples and categories
- Suggestions for related commands
