Please analyze this repository and create an `AGENTS.md` file at the repository root with the following content and guidelines.

This file will be used by agentic coding agents operating in this repository.

Requirements
1. **Build / lint / test commands**
   - Include commands to build the project.
   - Include linting commands.
   - Include test commands.
   - **Especially** include the exact command to run a single test (one test file or one test case).

2. **Code style guidelines**
   - Imports (ordering, grouping, absolute vs relative).
   - Formatting (line length, indentation, trailing whitespace).
   - Types (use of type hints, typing conventions).
   - Naming conventions (variables, functions, classes, constants).
   - Error handling (exceptions, logging, retry policies).
   - Tests (structure, naming, fixtures, mocks).
   - Documentation (docstrings, README updates).
   - Commit messages and PR etiquette.
   - Any other repository-specific conventions.

Additional details
- Make this document a comprehensive, informative, and useful single source of truth (SSOT) guide to be able to fully initialize a new coding agent to achieve the same level of understanding of the project, its codebase, design and architecture as you have.
- If there are Cursor rules (in `.cursor/rules/` or `.cursorrules`) or Copilot rules (in `.github/copilot-instructions.md`), include them in the `AGENTS.md`.
- If an `AGENTS.md` already exists in the repository root (`/`), improve and expand it according to the above requirements.
