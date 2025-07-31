# `PROJECT_CONFIG.xml` Schema Reference

This document provides a comprehensive reference for all possible settings in the `PROJECT_CONFIG.xml` file. This file is the central nervous system of the Prompt Factory, allowing you to tailor the behavior of every command to your specific project.

## Root Element: `<project_config>`

This is the mandatory root element of the configuration file.

---

## `<metadata>`

Contains basic information about the project.

**Example:**
```xml
<metadata>
  <name>your-project-name</name>
  <version>1.0.0</version>
  <description>A brief description of the project.</description>
</metadata>
```

---

## `<tech_stack>`

Describes the core technologies used in the project.

*   **`<languages>`**: A list of `<language>` elements.
    *   `<language name="..." version="..." primary="true|false" />`
*   **`<frameworks>`**: A list of `<framework>` elements.
    *   `<framework name="..." version="..." primary="true|false" />`
*   **`<database>`**:
    *   `<database type="..." version="..." />`
*   **`<package_managers>`**: A list of `<manager>` elements.
    *   `<manager language="..." name="..." manifest="..." />`
*   **`<tools>`**: A list of `<tool>` elements.
    *   `<tool type="linter|formatter|testing|builder" name="..." command="..." config_file="..." />`

**Example:**
```xml
<tech_stack>
  <languages>
    <language name="python" version="3.11" primary="true"/>
  </languages>
  <frameworks>
    <framework name="django" version="4.2" primary="true"/>
  </frameworks>
  <package_managers>
    <manager language="python" name="pip" manifest="requirements.txt"/>
  </package_managers>
  <tools>
    <tool type="linter" name="flake8" command="flake8" config_file=".flake8"/>
  </tools>
</tech_stack>
```

---

## `<paths>`

Maps key project directories.

**Example:**
```xml
<paths>
  <source>src/</source>
  <tests>tests/</tests>
  <docs>docs/</docs>
</paths>
```

---

## `<scripts>`

Defines aliases for common project commands. The `id` attribute is standardized and used by factory commands.

**Standard IDs**: `test`, `test:unit`, `lint`, `format`, `build`, `run:dev`, `deps:install`, etc.

**Example:**
```xml
<scripts>
  <script id="test">pytest --cov=src</script>
  <script id="lint">flake8 src</script>
</scripts>
```

---

## `<command_settings>`

Allows for fine-grained control over the behavior of specific commands.

**Example:**
```xml
<command_settings>
  <command name="/protocol">
    <setting key="[EXAMPLE_KEY_SANITIZED]""true" />
    <setting key="[EXAMPLE_KEY_SANITIZED]""false" />
  </command>
  <command name="/query">
    <setting key="[EXAMPLE_KEY_SANITIZED]""100" />
  </command>
</command_settings>
```

## Referencing Config Values in Prompts

To use a value from this file in a command prompt, use the following syntax: `${scope.path.to.value}`.

*   **Scope**: `metadata`, `tech_stack`, `paths`, `scripts`, `command_settings`.
*   **Accessing by attribute**: Use a `.` (e.g., `${tech_stack.languages.language.name}`).
*   **Accessing by ID**: Use a `#` (e.g., `${scripts.script#test}`).
*   **Accessing command settings**: Use `command#command_name.setting_key` (e.g., `${command_settings.command#protocol.epiccc.check.run_security_scan}`). 