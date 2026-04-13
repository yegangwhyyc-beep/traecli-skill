---
name: trae-cli
description: TRAE CLI integration for code generation, framework initialization, and automated testing. Use when the user needs to: (1) Generate code through natural language, (2) Initialize development frameworks, (3) Build and run automated tests, or (4) Any development tasks that can be accomplished through TRAE CLI.
---

# TRAE CLI Skill

TRAE CLI is ByteDance's development tool that supports code generation, framework initialization, and automated testing through natural language interaction.

## Overview

TRAE CLI (`traecli`) provides a natural language interface for development tasks:
- **Code generation**: Generate code based on requirements
- **Framework initialization**: Create project structures for various frameworks
- **Automated testing**: Build and run test scripts
- **Natural language interaction**: All operations use conversational prompts

## Workflow

### 1. Understand the Development Request

Analyze the user's request to identify the core development need:
- What needs to be built?
- What type of project/framework?
- What functionality should be implemented?
- What are the testing requirements?

### 2. Execute with TRAE CLI

Use the wrapper script to execute TRAE CLI commands:

```bash
python3 ~/.agents/skills/trae-cli/scripts/trae_wrapper.py "<natural-language-prompt>" [workdir]
```

**Available wrapper methods:**
- `execute(prompt, workdir)` - General natural language command
- `generate_code(requirement, workdir)` - Generate code
- `init_framework(project_type, project_name, workdir)` - Initialize project
- `build_tests(test_requirements, workdir)` - Build test scripts
- `run_tests(workdir)` - Run tests

### 3. Review and Iterate

- Check the output from TRAE CLI
- Verify generated code meets requirements
- Run tests if applicable
- Iterate based on results

## Example Workflows

### Example 1: Initialize a React Project

```
User: "帮我创建一个 React 待办事项应用"

Agent steps:
1. Execute: python3 trae_wrapper.py "Initialize a React project named todo-app" ./workspace
2. Review generated project structure
3. Report results to user
```

### Example 2: Generate Specific Feature

```
User: "给这个项目添加用户认证功能"

Agent steps:
1. Execute: python3 trae_wrapper.py "Generate code: Add user authentication with JWT" ./workspace/my-app
2. Review generated code
3. Confirm implementation with user
```

### Example 3: Build and Run Tests

```
User: "为这个功能写测试并运行"

Agent steps:
1. Execute: python3 trae_wrapper.py "Build automated test scripts for user authentication module" ./workspace/my-app
2. Execute: python3 trae_wrapper.py "Run all tests" ./workspace/my-app
3. Report test results
4. If tests fail, work with TRAE CLI to fix issues
```

## Important Notes

### Working Directory

Always specify an appropriate working directory:
- For new projects: parent directory where project should be created
- For existing projects: the project root directory

### Error Handling

If TRAE CLI fails:
1. Check if `traecli` is installed and in PATH
2. Review error messages from TRAE CLI
3. Adjust the natural language prompt if needed
4. Retry with more specific instructions

### Test Verification

After building tests:
1. Run tests to verify they pass
2. Report test coverage if available
3. If tests fail, help diagnose and fix issues using TRAE CLI

### Iterative Development

TRAEAR CLI supports iterative refinement. If initial results don't meet requirements:
- Provide feedback to TRAE CLI with specific adjustments
- Re-run commands with modified prompts
- Continue iterating until satisfactory

## Integration with Existing Skills

This skill can work alongside:
- `coding-agent` - Use TRAE CLI as the backend for coding tasks
- `gh-issues` - Build and test fixes for GitHub issues using TRAE CLI

## Limitations

- TRAE CLI must be installed and accessible in the system PATH
- Natural language prompts should be clear and specific
- Some complex operations may require multiple iterations
