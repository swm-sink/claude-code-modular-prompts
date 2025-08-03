# Submodule Integration Helpers

## Purpose

This directory contains helper scripts and templates for integrating the Claude Code Context Engineering framework as a git submodule in parent projects.

## Contents

### Scripts

#### detect_mode.sh
Core script that determines execution context:
- Detects if running in transformation mode (Stage 1)
- Detects if running as framework in parent project (Stage 2)
- Sets environment variables for commands to use
- Provides multiple fallback detection methods

#### setup.sh
Initial setup script for parent projects:
- Adds this repository as a git submodule
- Creates initial context structure
- Generates starter CLAUDE.md
- Configures mode detection

#### test_integration.sh
Tests the integration is working correctly (to be implemented)

### Templates

#### .gitmodules.template
Template for parent project's `.gitmodules` configuration

#### .gitignore.template
Template for excluding transformation-specific files

### Documentation

#### integrate.md
Detailed integration guide for parent projects (to be created)

## Usage

### For Parent Projects

1. Run the setup script:
   ```bash
   ./.claude-context/.submodule/setup.sh
   ```

2. Source mode detection in your commands:
   ```bash
   source .claude-context/.submodule/detect_mode.sh
   ```

### For Transformation

Mode detection automatically identifies transformation context when `.transformation/active` exists.

## Environment Variables

See `.claude/framework/docs/ENVIRONMENT_VARIABLES.md` for complete reference.