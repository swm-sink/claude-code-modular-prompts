# Deprecation Notice

As part of our move to the new "Prompt Factory" architecture, we have deprecated several components of the old framework in favor of simpler, more powerful, prompt-based commands. This document outlines these deprecations and explains the new, recommended approach.

## 1. Streamlit Dashboard

*   **Status**: Deprecated
*   **Reason**: The Streamlit dashboard was a complex, code-heavy component that was difficult to maintain and extend. It also created a separation between the user's workflow in Claude Code and the analysis of that workflow.
*   **Replacement**: The functionality of the Streamlit dashboard has been replaced by a series of powerful, prompt-based commands that can be run directly within Claude Code.
    *   **Command Exploration**: Use `ls -R claude_prompt_factory/commands` to explore the command library.
    *   **Performance Analysis**: Use the `/analyze performance` command.
    *   **Quality Reporting**: Use the `/quality report` command.

## 2. Python Scripts (`scripts/`)

*   **Status**: Deprecated
*   **Reason**: The Python scripts in the `scripts/` directory were another source of complexity and maintenance overhead. They also made the framework less portable and more difficult to set up.
*   **Replacements**: The core functionality of these scripts has been converted into new, prompt-based commands.
    *   **`project_initializer.py`**: Replaced by the new `/init` command, which provides a prompt-driven wizard for setting up new projects.
    *   **`test_workflow_integration.py`**: Replaced by the new `/workflow` command, which provides a powerful, DAG-based workflow orchestration engine.
    *   **`deployment_pipeline.py`**: Replaced by the new `/deploy` command, which provides a structured, multi-stage deployment pipeline.

By replacing these complex, coded components with simple, powerful, prompt-based commands, we have created a framework that is more robust, easier to maintain, and more aligned with the "Claude Code Native" philosophy. 