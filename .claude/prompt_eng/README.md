# Prompt Engineering Components

This directory contains ALL prompt engineering components for the Claude Code Modular Prompts Framework.

## Directory Structure

### `/commands/`
All command definitions and prompt templates:
- **`/core/`** - Main commands (auto, task, feature, swarm, query, session, docs, protocol)
- **`/meta/`** - Meta-framework commands (meta-review, meta-evolve, meta-optimize, meta-govern, meta-fix)
- **`/setup/`** - Setup and initialization commands (init, context-prime, adapt, validate)

### `/frameworks/`
All prompt engineering frameworks:
- RISE, TRACE, CARE, CLEAR, SOAR, CRISP, SPARK, FOCUS, LEAP
- Framework selector and advanced framework patterns

### `/personas/`
All persona definitions:
- **`/core/`** - Core engineering personas
- **`/rd-engineering/`** - 25 specialized R&D engineering personas

### `/patterns/`
Thinking and composition patterns:
- **`/thinking/`** - Thinking patterns, critical thinking templates
- **`/composition/`** - Module composition, prompt construction patterns
- **`/visualization/`** - Runtime dashboards, execution visualization

### `/modules/`
Prompt engineering specific modules:
- **`/routing/`** - Intelligent routing, persona management, deterministic routing
- **`/orchestration/`** - Multi-agent coordination, swarm patterns

## Key Principles

1. **Separation of Concerns**: All prompt engineering components are isolated here
2. **No System Code**: System functionality belongs in `/system/`
3. **Clear Organization**: Related components are grouped together
4. **Version Control**: All components follow framework version 3.0.0

## Usage

Components in this directory are referenced by commands and composed by the Module Runtime Engine.
Cross-references should use paths relative to `.claude/`.