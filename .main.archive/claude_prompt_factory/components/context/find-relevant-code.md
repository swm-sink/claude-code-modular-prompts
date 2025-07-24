<prompt_component>
  <step name="Identify Relevant Code">
    <description>
      Based on the user's request, perform a comprehensive analysis of the codebase to identify the most relevant files, classes, functions, and code snippets.
      You should use a combination of file searching, code analysis, and dependency tracing to make your determination.
      Prioritize files located in the `${paths.source}` and `${paths.tests}` directories.
    </description>
    <output>
      List the identified files and a brief justification for why each is relevant to the user's request.
      Do not proceed until you have a high degree of confidence in the identified code.
    </output>
  </step>
</prompt_component> 