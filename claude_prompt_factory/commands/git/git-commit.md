<command_file>
  <metadata>
    <name>/git commit</name>
    <purpose>Generates intelligent, meaningful commit messages following the Conventional Commits format.</purpose>
    <usage>
      <![CDATA[
      /git commit <auto_stage=true>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="auto_stage" type="boolean" required="false" default="true">
      <description>If true, automatically stages all tracked, changed files before committing.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Analyze staged changes and generate a conventional commit message.</description>
      <usage>/git commit</usage>
    </example>
    <example>
      <description>Stage all current changes and then generate the commit message.</description>
      <usage>/git commit auto_stage=true</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a git expert. The user wants to create a high-quality commit.

      1.  **Analyze Changes**:
          *   If `auto_stage` is true, stage all changed files (`git add .`).
          *   Analyze the staged changes using `git diff --staged`.
          *   Based on the changes, determine the appropriate commit type (feat, fix, refactor, etc.) and scope.

      2.  **Generate Commit Message**:
          *   Generate a commit message that follows the Conventional Commits specification.
          *   The message should have a clear, concise subject line.
          *   The body should explain the "what" and "why" of the change.

      3.  **Propose Commit Command**:
          *   Present the final `git commit -m "..."` command to the user for them to execute.
    </prompt>
  </claude_prompt>

  <dependencies>
    <!-- This command interacts directly with git -->
  </dependencies>
</command_file>