# Example: Automated Code Cleanup Workflow

The Prompt Factory really shines when you start combining its commands into automated workflows. The `/workflow run` command allows you to define a series of steps that can be executed in sequence or in parallel.

## Scenario

You want to perform a comprehensive cleanup of your codebase. This involves removing unused code, fixing any linting errors, and formatting the code according to project standards.

## Workflow Definition

You can define this workflow in a simple YAML file:

**`cleanup-workflow.yml`**:
```yaml
name: Code Cleanup Workflow
steps:
  - name: clean_code
    command: /code clean .
  - name: lint_code
    command: /code lint . --fix
    depends_on: [clean_code]
  - name: format_code
    command: /code format .
    depends_on: [lint_code]
```

## Usage

Once you've defined your workflow, you can execute it with a single command:

```bash
/workflow run cleanup-workflow.yml
```

## Expected Behavior

The `/workflow run` command will orchestrate the entire cleanup process:

1.  It will run the `/code clean` command to remove any unused code.
2.  Once that is complete, it will run the `/code lint --fix` command to automatically fix any linting errors.
3.  Finally, it will run the `/code format` command to ensure the code is formatted according to project standards.

This example demonstrates how you can use the "Prompt Factory" to automate complex, multi-step tasks and create your own powerful, reusable workflows. 