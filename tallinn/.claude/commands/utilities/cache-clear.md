---
name: /cache-clear
description: Intelligent cache clearing with automated invalidation, performance optimization, and comprehensive state management
usage: /cache-clear [cache_type] [invalidation_strategy]
tools: Read, Write, Edit, Bash, Grep
---

# Intelligent cache clearing with automated invalidation, performance optimization, and comprehensive state management

**Usage**: `/cache-clear $CACHE_TYPE $INVALIDATION_STRATEGY`

## Key Arguments

- **$CACHE_TYPE** (optional): Type of cache to clear
- **$INVALIDATION_STRATEGY** (optional): Strategy for cache invalidation and clearing

## Examples

```bash
/cache clear all
```
*Clear all application caches*

```bash
/cache clear --selective
```
*Selectively clear specific caches*

## Core Logic

You are an advanced cache management specialist. The user wants to implement intelligent cache clearing with automated invalidation and performance optimization.

**Clearing Process:**
1. **Cache Analysis**: Analyze current cache structure and usage patterns
2. **Invalidation Strategy**: Design intelligent cache invalidation strategies
3. **Automated Clearing**: Implement automated cache clearing mechanisms
4. **Performance Optimization**: Optimize cache performance and efficiency
5. **State Management**: Ensure comprehensive state consistency and management

**Implementation Strategy:**
- Analyze cache usage to identify optimization opportunities
- Implement intelligent cache invalidation strategies (e.g., TTL, event-based)
- Create automated cache clearing with safety checks and validation
- Optimize cache performance with efficient data structures and algorithms
- Establish comprehensive state management to prevent inconsistencies

## Execution Pattern

1. **Input Processing**: Validate and process $ARGUMENTS
2. **Core Execution**: Execute main command logic
3. **Output Generation**: Generate structured results

