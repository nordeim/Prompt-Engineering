### 1. Executive Summary

This architecture blueprint outlines the plan to construct a custom AI agent framework based on **Pi** (`earendil-works/pi`), the terminal-first coding harness. Following the **Anti-Generic Philosophy**, our custom agent will eschew heavy, black-box agent frameworks in favor of Pi’s signature minimalist design: **a small, programmable core with extensible, modular edges**.

The blueprint details a dual-layered architecture:
1. **The Core Agentic Loop (`pi-core`)**: Managing context compilation, state transformation, token-efficient summary compaction, and execution of a minimal 4-tool primitive set (`read`, `write`, `edit`, `bash`).
2. **The Interactive UI Layer (`pi-interactive`)**: Orchestrated around custom-built Text User Interface (TUI) components and an extensible TypeScript plugin ecosystem that allows runtime registration of custom keyboard hotkeys, custom skills, and prompt templates.

Our design language will leverage a **Brutalist Utilitarian aesthetic**—relying strictly on intentional monochrome spaces, bespoke ASCII block layouts, raw terminal box-drawing characters, and highly legible typographical hierarchies (optimized for monospaced typefaces like *JetBrains Mono* or *SF Mono*).

---

### 2. Phase 1: ANALYZE — Deep, Multi-Dimensional Requirement Mining

#### System Deconstruction & Implicit Needs
To successfully replicate and customize the Pi-agent harness, we must structurally dissect its key mechanics highlighted in the architectural walkthrough:

```
                  ┌─────────────────────────────────────────┐
                  │            User / CLI / TUI             │
                  └────────────────────┬────────────────────┘
                                       │
                        [Interactive TUI / RPC Input]
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │            pi-interactive               │
                  │  (client.ts / main.ts Core Launcher)    │
                  └────────────────────┬────────────────────┘
                                       │
                       [Resolves Extensions & Skills]
                                       │
                                       ▼
                  ┌─────────────────────────────────────────┐
                  │                pi-core                  │
                  │        (Agent Session Loop)             │
                  └────────┬───────────┬───────────┬────────┘
                           │           │           │
      ┌────────────────────┘           │           └────────────────────┐
      ▼                                ▼                                ▼
┌──────────────┐             ┌───────────────────┐             ┌────────────────┐
│ Init Context │             │ State Transform   │             │ LLM Call Loop  │
│ - System MD  │             │ & Compaction      │             │ - Tool Call    │
│ - Workspace  │             │ - Checks token    │             │   Execution    │
│   agents.md  │             │   counts          │             │ - Custom Tool  │
│ - Message    │             │ - Rebuilds state  │             │   Registration │
│   History    │             │   via LLM summary │             └────────────────┘
└──────────────┘             └───────────────────┘
```

1. **Context Initialization & Resolution Hierarchy**: 
   When a turn begins, the harness must dynamically compose the context window:
   * **System Prompt**: Base configuration merged with `.pi/system.md` or runtime overrides.
   * **Active Workspaces**: Project-level instructions from `agents.md`.
   * **Registered Skills & Tools**: Serialized descriptions of typescript tools/skills parsed into markup.
   * **Session Tree**: Reconstructed from the branch history.
2. **Branching Session Tree (Memory Engine)**: 
   Unlike standard linear chat logs, Pi records sessions as trees within flat `.jsonl` files where each line represents a node featuring its own `id` and `parent` pointer. To switch states or "fork" a conversation, the engine resolves the path from the selected node up to the root, preventing history corruption.
3. **Context Compaction Algorithm**: 
   When context bounds near limits, Pi doesn't drop messages blindly. Instead, a designated system prompt (`summarize-prompt`) triggers a meta-LLM pass that condenses the active tree history into a structured Markdown document tracking *Goals, Constraints, Progress (Done/Todo), Key Decisions, and Critical Context*.
4. **Surgical Tool Primitive Design**: 
   By default, the core remains highly sandboxed, utilizing only four key tools: `read`, `write`, `edit`, and `bash`. Advanced utility is delegated to modular TS extensions rather than a bloated core.

#### Risk Assessment & Mitigation Strategies

| Identified Risk | Impact | Mitigating Strategy |
| :--- | :--- | :--- |
| **Token Exhaustion on Large Repositories** | High | Strict token-counting intercepts pre-turn. We will implement active context window compaction using local tokenizer libraries (`gptspt` or `tiktoken`). |
| **Silent Bash Command Failures** | Medium | The `bash` execution tool must hook direct stream pipes (`stdout`, `stderr`) back into the TUI frame-buffers in real-time, supporting interruption signals (`Ctrl+C`). |
| **Tree Traversal Performance on Long Sessions** | Low | Implement a memory-mapped indexing scheme for JSONL traversal, cache evaluated histories, and dynamically render only visible leaves in the session tree browser. |

#### Conceptual Aesthetic Direction: Brutalist Utilitarian
* **Typographical Hierarchy**: Heavy use of bold monospaced headings (`#`, `##`) coupled with thin line decorations. Strict rejection of generic gradients.
* **Palette**: High-contrast monochromatic terminal UI. Colors are reserved purely for semantic indicators (e.g., green indicators for successful builds, red for error buffers, dim grey for background operations/reasoning steps).
* **Interface**: Custom-rendered terminal grid boxes utilizing standard Unicode Box-Drawing characters (`┌`, `─`, `┐`, `│`). Double borders delineate key structural areas.

---

### 3. Phase 2: PLAN — Structured Execution Roadmap

We will divide development of our custom coding harness into 4 core sequential milestones:

```
┌────────────────────────────────────────────────────────────────────────┐
│                              ROADMAP                                   │
├───────────────┬────────────────────────────────────────────────────────┤
│ Milestone 1   │ Core Agent Loop & Tool primitives (read/write/bash)     │
├───────────────┼────────────────────────────────────────────────────────┤
│ Milestone 2   │ Hierarchical Session Tree & JSONL Storage Engine       │
├───────────────┼────────────────────────────────────────────────────────┤
│ Milestone 3   │ Dual-Mode Client & Custom TUI (No-reflow layout)       │
├───────────────┼────────────────────────────────────────────────────────┤
│ Milestone 4   │ TypeScript Extension SDK & Dynamic Skills System       │
└───────────────┴────────────────────────────────────────────────────────┘
```

#### Detailed Milestone Checklist

##### Milestone 1: Core Agentic Engine (`pi-core`)
* [ ] Initialize TypeScript workspace with strict mode enabled.
* [ ] Implement token calculation algorithms to monitor state boundaries.
* [ ] Build the core agentic runtime loop (Context Compilation → Compaction Check → Model Call → Tool Execution).
* [ ] Implement the minimal tool set:
  * `read`: Safe, file-path checked read handler.
  * `write`: Single-pass file writer with file-creation safeguards.
  * `edit`: Pattern-based search-and-replace editor (minimizing large file rewrites).
  * `bash`: Child process runner with real-time stream piping and interruption support.
* [ ] Define LLM Provider wrappers with strict schemas for tool-calling interfaces (Anthropic, OpenAI, DeepSeek, Ollama).

##### Milestone 2: Hierarchical Session Tree & JSONL Engine
* [ ] Design database-less persistence mapping local paths to session directories under `~/.pi/agent/sessions/`.
* [ ] Implement JSONL writer that appends messages with UUIDs and `parent` fields to maintain a tree graph.
* [ ] Build tree traversal algorithms to reconstruct linear message histories along specific node branches.
* [ ] Implement the `check-compaction` trigger and its corresponding LLM context summary prompt.

##### Milestone 3: Interactive TUI Client & Entry Points
* [ ] Write standard entry points (`main.ts` and `client.ts`).
* [ ] Build low-overhead ANSI-escape TUI component runner.
* [ ] Design keybind registration middleware (handling text inputs, commands like `/tree`, `/reload`, and exit inputs).
* [ ] Create layout sections (Message Viewport, Context Details Footer, Command Input line).

##### Milestone 4: TypeScript Extensions & Dynamic Skills
* [ ] Design the Extension interface, exposing lifecycle hooks: `onStart`, `beforeLLMCall`, `onToolResult`, and `onMessage`.
* [ ] Implement a system to parse Workspace-level skills (`.md` instruction files).
* [ ] Build the dynamic package resolver supporting loading third-party extensions via local directories or NPM packages.

#### Success Criteria & Validation Checkpoints
* **Compaction Test**: Running a simulated 50-turn conversation must trigger compaction without dropping core constraints or workspace file paths.
* **Tree Splitting (Forking)**: Modifying a file in a branched history segment must result in a clean tree divergence in the persistent JSONL, retaining the ancestor messages on both branches.
* **Performance Benchmark**: UI rendering during tool execution must avoid screen-flickering or unnecessary repaints, utilizing strict terminal frame buffering.

#### Estimated Effort & Timeline
* **Total Estimated Time**: 4-5 Weeks
* **Developer Allocation**: 1 Senior Backend/Agent Engineer, 1 Senior Frontend/TUI Architect.

---

### 4. Phase 3: VALIDATE — Explicit Confirmation Checkpoint

To ensure complete alignment before any code is generated or structured folder layouts are committed:

> **Validation Gate**: 
> 1. Does the structural roadmap and the chosen **Brutalist Utilitarian** aesthetic meet your criteria?
> 2. Are there any particular LLM providers or models you would like the core adapter layer to support out-of-the-box (e.g., Anthropic Claude, DeepSeek V4, OpenAI)?
> 3. Do you want to include specific custom tools beyond the classic four (Read, Write, Edit, Bash) inside the base codebase?

Please provide your feedback or confirm the plan to initiate the **IMPLEMENT** phase.

# https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221k8mirVyEtqO-yEA6svVkal6LFD5lTFl5%22%5D,%22action%22:%22open%22,%22userId%22:%22103961307342447084491%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing
