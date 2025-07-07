| version | last_updated | status |
|---------|--------------|--------|
| 3.0.0   | 2025-07-07   | stable |

# CRITICAL THINKING ENFORCEMENT - EXTREME PRIORITY

────────────────────────────────────────────────────────────────────────────────

**STATUS**: MANDATORY | **SEVERITY**: CATASTROPHIC PREVENTION  
**CANONICAL IMPLEMENTATION**: `.claude/modules/quality/critical-thinking.md`

> **Note**: This document provides context and lessons learned. For the authoritative implementation, see the [Critical Thinking Module](../../.claude/modules/quality/critical-thinking.md).

## The Problem We're Solving

The recent framework refactor created:
- **262+ duplicate files** in shadow directories
- **Contradictory claims** of simplification while adding complexity
- **Broken references** throughout the system
- **Lost critical capabilities** without understanding impact

This represents a CATASTROPHIC FAILURE of thinking before acting.

## Historical Context: Framework Disaster Lessons

The critical thinking rules were established after a catastrophic framework refactor that created 262+ duplicate files while claiming simplification. The key lessons learned are implemented in the Critical Thinking Module.

### Key Enforcement Points (See Module for Implementation)

1. **THINK DEEPLY** - Minimum 30-second analysis before any action
2. **DRY PRINCIPLE** - Zero tolerance for duplication
3. **FORENSIC VERIFICATION** - Every claim must be verified with evidence

### What Failed During the Disaster

- Surface-level thinking led to massive duplication
- Unverified claims ("35 files") while creating 300+
- Ignored git status warnings showing the true impact
- Lost critical capabilities without understanding dependencies

## Real Examples From the Disaster

### ❌ What Went Wrong
- **Claim**: "Simplifying from 157 to 35 files"  
  **Reality**: Created 262 duplicate files in shadow directories

- **Claim**: "Making the framework cleaner"  
  **Reality**: Left battle test code scattered throughout src/

- **Claim**: "No theoretical features"  
  **Reality**: Kept framework_intelligence.py and battle tests

### ✅ What We Do Now
All critical thinking enforcement is implemented through the module system. The module provides:
- Mandatory pre-action analysis checklists
- DRY principle enforcement with duplication scanning
- Forensic verification protocols
- Integration with AWARE framework
- Session documentation requirements

## Why This Document Exists

This historical record exists to:
1. Document the lessons learned from the framework disaster
2. Provide context for why the critical thinking module is so strict
3. Serve as a warning about the consequences of hasty action
4. Point to the canonical implementation in the module system

## Remember

Every framework change affects EVERYTHING. A moment of careless action creates hours of cleanup work. The critical thinking module exists to prevent another disaster.

**For implementation details, see: `.claude/modules/quality/critical-thinking.md`**