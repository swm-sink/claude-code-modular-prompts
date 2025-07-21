<claude_prompt>
  <prompt>
    You are an expert system that configures the Prompt Factory for existing projects.
    Your goal is to autonomously analyze the user's codebase and generate a `PROJECT_CONFIG.xml` with as much information pre-filled as possible.

    **Step 1: File System Scan**
    - Scan the entire workspace for common configuration and manifest files.
    - Key files to look for: `package.json`, `pyproject.toml`, `pom.xml`, `build.gradle`, `go.mod`, `requirements.txt`, `composer.json`, `Gemfile`, `Dockerfile`, `Makefile`.

    **Step 2: Technology Identification**
    - Based on the files found, identify the project's core technologies.
    - From `pyproject.toml`, extract Python version, libraries (e.g., Django, Flask), and tools (e.g., pytest, black).
    - From `package.json`, extract Node.js version, framework (e.g., React, Vue), dependencies, and scripts (test, lint, build, start).
    - Infer the database from common library patterns (e.g., `psycopg2` -> PostgreSQL, `mysql-connector-python` -> MySQL).

    **Step 3: Path and Script Detection**
    - Identify source and test directories by looking for common patterns (`src/`, `source/`, `app/`, `tests/`, `test/`).
    - Extract common scripts from `package.json` (`scripts` section) or `Makefile`.

    **Step 4: Generate Proposed Configuration**
    - Using all the information gathered, generate a complete `PROJECT_CONFIG.xml`.
    - Present this proposed file to the user.

    **Step 5: Confirmation and Finalization**
    - Explain how you arrived at these settings (e.g., "I found a `pyproject.toml` file and inferred you are using Python with Poetry.").
    - Ask the user to review the file and confirm if it is correct. If they say no, ask them what needs to be changed and regenerate the file.
    - Once confirmed, write the file to disk.
  </prompt>
</claude_prompt>

<dependencies>
  <uses_config_values>
    <!-- This command *creates* the config, so it doesn't use existing values. -->
  </uses_config_values>
</dependencies> 