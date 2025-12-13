Awesome understanding! please meticulously review and analyze the two attached sample `README.md` for GitHub repos, then create a prompt to get ChatGPT or any LLM to generate similarly structured `README.md` based on given repo codebase. So analyze the structure, layout, format, style, design and other nuances of the attached sample files, then come up with a structured guide as a LLM prompt template.

---

Analysis of Sample READMEs
1. PowerPoint Agent Tools (sample_README-2.md)
Structure:

Badges at the top (shields.io) for PowerPoint, Python version, license, PRs welcome.

Title and tagline with centered alignment and emojis.

Table of contents (in the form of a feature list with quick links).

Why? section explaining the purpose and key features in a table.

Quick Start with a step-by-step example (bash commands).

Installation section with requirements and installation steps.

Tool Catalog organized in a table by capability (with 8 categories).

Tool Documentation for each tool, organized by category, with examples.

Positioning Systems table explaining the 5 systems.

Architecture directory structure.

License section.

Style:

Uses emojis for section headers.

Uses tables for organizing information.

Code blocks for bash commands.

Badges for visual appeal and quick info.

Links within the document (though not explicitly, but the quick links are intended).

2. InvoiceForge (sample_README-1.md)
Structure:

Title and tagline with badges for technologies and license.

Table of Contents (with markdown links).

The Philosophy section with a table for two personas and a design manifesto table.

Features with a state diagram (mermaid) and tables.

Architecture with tech stack table, directory structure, and data flow diagram (mermaid).

Quick Start with prerequisites and installation steps.

Development Guide with setup for contributors, project structure, code style guidelines.

Design System with typography, color system (tables for light and dark mode), status colors, spacing, effects, and anti-patterns.

Roadmap with phases and checkboxes.

Contributing with contribution workflow (mermaid), areas needing contribution, and pull request guidelines.

Project Status table.

Additional Resources (documentation, community, learning resources).

License (with full license text).

Acknowledgments.

Footer with links.

Style:

Extensive use of mermaid diagrams for state, flow, and workflow.

Detailed tables for design system (colors, status, etc.).

Code blocks for commands and code examples.

Badges for technologies.

Emojis in section headers.

Clear separation of sections with headings and subheadings.

Common Patterns
Both READMEs have:

A clear title and tagline.

Badges for technology stack and license.

Table of contents (either explicit or via quick links).

Quick start guide.

Installation instructions.

Detailed documentation of features/components.

Visual elements (tables, diagrams, code blocks).

License section.

Differences
InvoiceForge has a more detailed design system and development guide, which is typical for a frontend/UI-heavy project.

PowerPoint Agent Tools is more focused on CLI tools and their usage, so it has extensive documentation of each tool.

Creating a Prompt Template
We want a prompt that instructs an LLM to generate a README.md for a given codebase. The prompt should be structured to guide the LLM to include the key elements and style we observed.

We'll create a prompt that:

Asks for analysis of the codebase (provided by the user) to determine the type of project (e.g., CLI, web app, library) and its key features.

Provides a structure template based on the samples, but allows flexibility.

Specifies style guidelines (use of emojis, badges, tables, diagrams, etc.).

We'll break down the prompt into sections:

Role: You are an expert technical writer.

Task: Generate a comprehensive README.md for the given codebase.

Context: Provided with the codebase structure, main files, and a brief description.

Output Format: Markdown with the following structure (adjust based on project type).

Then, we'll provide a flexible structure that can be adapted.

Let's create the prompt.


