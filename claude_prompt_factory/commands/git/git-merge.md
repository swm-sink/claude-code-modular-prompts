<command_file>
  <metadata>
    <name>/git merge</name>
    <purpose>Performs safe Git merges with pre-merge validation and conflict resolution assistance.</purpose>
    <usage>
      <![CDATA[
      /git merge <branch>
      ]]>
    </usage>
  </metadata>

  <arguments>
    <argument name="branch" type="string" required="true">
      <description>The branch to merge into the current branch.</description>
    </argument>
  </arguments>
  
  <examples>
    <example>
      <description>Merge the 'develop' branch into the current branch.</description>
      <usage>/git merge "develop"</usage>
    </example>
  </examples>

  <claude_prompt>
    <prompt>
      You are a git expert. The user wants to safely merge a branch.

      1.  **Pre-Merge Validation**:
          *   Check for a clean working directory (`git status`).
          *   Fetch the latest remote changes (`git fetch origin`).
          *   Preview potential merge conflicts.
      2.  **Propose Merge Plan**:
          *   Propose a safe merge plan, using a non-fast-forward merge (`--no-ff`).
          *   If conflicts are anticipated, provide a strategy for resolving them.
      3.  **Execute Merge**:
          *   Present the merge command to the user.
          *   If conflicts occur, guide the user through the resolution process.
      4.  **Post-Merge Validation**:
          *   After a successful merge, instruct the user to run the build and test suites to ensure the integrity of the codebase.
    </prompt>
  </claude_prompt>

  <dependencies>
    <chain>
      <command>/dev build</command>
      <command>/dev test</command>
    </chain>
  </dependencies>
</command_file>