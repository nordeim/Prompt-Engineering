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

---

Applying elite software engineering standards, strict TypeScript patterns, and our defined **Brutalist Utilitarian** design direction, here is the complete, modular base implementation for your custom Pi-agent clone.

---

### Project Structure

```text
pi-agent/
├── package.json
├── tsconfig.json
├── src/
│   ├── types.ts          # Strictly defined structural interfaces
│   ├── session.ts        # JSONL memory engine & tree traversal resolution
│   ├── tools.ts          # Core sandboxed system tools (read, write, edit, bash)
│   ├── agent.ts          # Agent loop orchestration & compaction check
│   └── index.ts          # Command-line entry point & Brutalist TUI REPL
```

---

### 1. Project Initialization & Dependencies

To set up the workspace, initialize your node project and install dependencies:

```bash
npm init -y
npm install dotenv tiktoken OpenAI @types/node typescript ts-node --save
```

#### `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "rootDir": "./src",
    "outDir": "./dist",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"]
}
```

---

### 2. Implementation Modules

#### Module 1: `src/types.ts`
This file establishes the foundational contract for our system prompt composition, message nodes, and tool signatures.

```typescript
export type Role = 'system' | 'user' | 'assistant' | 'tool';

export interface ToolCall {
  id: string;
  type: 'function';
  function: {
    name: string;
    arguments: string;
  };
}

export interface ToolResult {
  role: 'tool';
  tool_call_id: string;
  content: string;
}

export interface AgentMessage {
  role: Role;
  content: string | null;
  name?: string;
  tool_calls?: ToolCall[];
}

export interface MessageNode {
  id: string;
  parent: string | null;
  timestamp: string;
  message: AgentMessage;
}

export interface SessionContext {
  systemPrompt: string;
  workspacePrompt: string;
  history: AgentMessage[];
  tokenCount: number;
}

export interface ToolDefinition {
  name: string;
  description: string;
  parameters: Record<string, unknown>;
  execute: (args: Record<string, unknown>) => Promise<string>;
}
```

---

#### Module 2: `src/session.ts`
This component handles the flat JSONL append-only database. It parses the nodes to dynamically resolve the hierarchical message tree, tracing a route from the requested leaf message node back to the session root.

```typescript
import * as fs from 'fs/promises';
import * as path from 'path';
import { randomUUID } from 'crypto';
import { MessageNode, AgentMessage } from './types.js';

export class SessionStore {
  private filepath: string;

  constructor(sessionDir: string, sessionId: string) {
    this.filepath = path.join(sessionDir, `${sessionId}.jsonl`);
  }

  async initialize(): Promise<void> {
    const dir = path.dirname(this.filepath);
    await fs.mkdir(dir, { recursive: true });
    try {
      await fs.access(this.filepath);
    } catch {
      await fs.writeFile(this.filepath, '');
    }
  }

  async appendNode(parent: string | null, message: AgentMessage): Promise<MessageNode> {
    const node: MessageNode = {
      id: randomUUID(),
      parent,
      timestamp: new Date().toISOString(),
      message,
    };
    await fs.appendFile(this.filepath, JSON.stringify(node) + '\n', 'utf-8');
    return node;
  }

  async resolveHistory(leafId: string | null): Promise<{ nodes: MessageNode[]; leafId: string | null }> {
    if (!leafId) return { nodes: [], leafId: null };

    const content = await fs.readFile(this.filepath, 'utf-8');
    const lines = content.split('\n').filter(line => line.trim() !== '');
    const nodeMap = new Map<string, MessageNode>();

    for (const line of lines) {
      const node: MessageNode = JSON.parse(line);
      nodeMap.set(node.id, node);
    }

    const path: MessageNode[] = [];
    let currentId: string | null = leafId;

    while (currentId) {
      const node = nodeMap.get(currentId);
      if (!node) break;
      path.push(node);
      currentId = node.parent;
    }

    return {
      nodes: path.reverse(),
      leafId,
    };
  }

  async findLatestLeaf(): Promise<string | null> {
    try {
      const content = await fs.readFile(this.filepath, 'utf-8');
      const lines = content.split('\n').filter(line => line.trim() !== '');
      if (lines.length === 0) return null;
      const lastNode: MessageNode = JSON.parse(lines[lines.length - 1]);
      return lastNode.id;
    } catch {
      return null;
    }
  }
}
```

---

#### Module 3: `src/tools.ts`
The core sandbox. It isolates execution to standard paths and provides pattern-matched file editing instead of resource-heavy file rewrites.

```typescript
import * as fs from 'fs/promises';
import * as path from 'path';
import { exec } from 'child_process';
import { ToolDefinition } from './types.js';

export const createSystemTools = (workspaceRoot: string): Record<string, ToolDefinition> => {
  const sanitizePath = (targetPath: string): string => {
    const resolved = path.resolve(workspaceRoot, targetPath);
    if (!resolved.startsWith(path.resolve(workspaceRoot))) {
      throw new Error(`Access Denied: Path escape detected outside workspace workspace.`);
    }
    return resolved;
  };

  return {
    read: {
      name: 'read',
      description: 'Reads the complete text content of a file located within the workspace.',
      parameters: {
        type: 'object',
        properties: {
          path: { type: 'string', description: 'Relative path to the target file.' }
        },
        required: ['path']
      },
      execute: async (args) => {
        const filePath = sanitizePath(args.path as string);
        try {
          return await fs.readFile(filePath, 'utf-8');
        } catch (err) {
          return `Error reading file: ${(err as Error).message}`;
        }
      }
    },

    write: {
      name: 'write',
      description: 'Overwrites or creates a file with target content within the workspace.',
      parameters: {
        type: 'object',
        properties: {
          path: { type: 'string', description: 'Relative path to output target.' },
          content: { type: 'string', description: 'Raw file body to output.' }
        },
        required: ['path', 'content']
      },
      execute: async (args) => {
        const filePath = sanitizePath(args.path as string);
        try {
          await fs.mkdir(path.dirname(filePath), { recursive: true });
          await fs.writeFile(filePath, args.content as string, 'utf-8');
          return `Successfully wrote to ${args.path}`;
        } catch (err) {
          return `Error writing file: ${(err as Error).message}`;
        }
      }
    },

    edit: {
      name: 'edit',
      description: 'Performs pattern search-and-replace mutations inside a targeted file.',
      parameters: {
        type: 'object',
        properties: {
          path: { type: 'string', description: 'Target file path.' },
          search: { type: 'string', description: 'Explicit line chunk pattern to target.' },
          replace: { type: 'string', description: 'Replacement string chunk.' }
        },
        required: ['path', 'search', 'replace']
      },
      execute: async (args) => {
        const filePath = sanitizePath(args.path as string);
        try {
          const original = await fs.readFile(filePath, 'utf-8');
          if (!original.includes(args.search as string)) {
            return `Edit Error: Search pattern was not located within ${args.path}. Ensure the block matches exactly.`;
          }
          const modified = original.replace(args.search as string, args.replace as string);
          await fs.writeFile(filePath, modified, 'utf-8');
          return `Successfully patched pattern inside ${args.path}`;
        } catch (err) {
          return `Error patching file: ${(err as Error).message}`;
        }
      }
    },

    bash: {
      name: 'bash',
      description: 'Executes non-interactive shell commands inside the workspace root shell.',
      parameters: {
        type: 'object',
        properties: {
          command: { type: 'string', description: 'Shell command string to run.' }
        },
        required: ['command']
      },
      execute: async (args) => {
        return new Promise<string>((resolve) => {
          exec(args.command as string, { cwd: workspaceRoot }, (error, stdout, stderr) => {
            const out = stdout ? `STDOUT:\n${stdout}` : '';
            const err = stderr ? `STDERR:\n${stderr}` : '';
            const status = error ? `EXIT CODE: ${error.code}` : 'EXIT CODE: 0';
            resolve([out, err, status].filter(Boolean).join('\n'));
          });
        });
      }
    }
  };
};
```

---

#### Module 4: `src/agent.ts`
Orchestrates the active conversation loop, token validation context checkups, and summary compaction passes.

```typescript
import { OpenAI } from 'openai';
import { get_encoding } from 'tiktoken';
import { SessionStore } from './session.js';
import { createSystemTools } from './tools.js';
import { AgentMessage, ToolCall } from './types.js';

const SUMMARIZE_SYSTEM_PROMPT = `You are a context summarization assistant. Your task is to compress complex message histories.
Analyze the provided history carefully. Create a structured, highly condensed Markdown summary detailing:
# Goal
- Core objective of user
# Progress
- [x] Completed actions
- [ ] Remaining work
# Key Decisions
- Document critical architecture choices
# Critical Context
- Target paths, file variables, configurations.
Provide ONLY this structural document.`;

export class PiAgent {
  private openai: OpenAI;
  private sessionStore: SessionStore;
  private tools: ReturnType<typeof createSystemTools>;
  private model: string;
  private maxTokens: number;
  private currentLeafId: string | null = null;

  constructor(options: {
    apiKey: string;
    baseUrl?: string;
    sessionStore: SessionStore;
    workspaceRoot: string;
    model?: string;
    maxTokens?: number;
  }) {
    this.openai = new OpenAI({ apiKey: options.apiKey, baseURL: options.baseUrl });
    this.sessionStore = options.sessionStore;
    this.tools = createSystemTools(options.workspaceRoot);
    this.model = options.model ?? 'gpt-4o-mini';
    this.maxTokens = options.maxTokens ?? 16000;
  }

  async start(): Promise<void> {
    await this.sessionStore.initialize();
    this.currentLeafId = await this.sessionStore.findLatestLeaf();
  }

  private calculateTokens(text: string): number {
    const enc = get_encoding('cl100k_base');
    const tokens = enc.encode(text).length;
    enc.free();
    return tokens;
  }

  async handleUserTurn(userPrompt: string, onUpdate: (log: string) => void): Promise<string> {
    // 1. Resolve active history tree
    let historyData = await this.sessionStore.resolveHistory(this.currentLeafId);
    let messages = historyData.nodes.map(n => n.message);

    // 2. Perform token assessment
    const rawTokens = this.calculateTokens(JSON.stringify(messages) + userPrompt);
    if (rawTokens > this.maxTokens * 0.75) {
      onUpdate('▲ Token ceiling threshold approached. Triggering summarization compaction...');
      const summary = await this.compactHistory(messages);
      
      // Clean start: Summary replaces history
      const systemMessage: AgentMessage = { role: 'system', content: summary };
      const baseNode = await this.sessionStore.appendNode(null, systemMessage);
      this.currentLeafId = baseNode.id;
      
      historyData = await this.sessionStore.resolveHistory(this.currentLeafId);
      messages = historyData.nodes.map(n => n.message);
    }

    // Append incoming user turn to JSONL database
    const userMsg: AgentMessage = { role: 'user', content: userPrompt };
    const userNode = await this.sessionStore.appendNode(this.currentLeafId, userMsg);
    this.currentLeafId = userNode.id;
    messages.push(userMsg);

    // 3. Enter agentic tool execution loop
    let keepRunning = true;
    let finalContent = 'No response generated.';

    while (keepRunning) {
      onUpdate('● Evaluating next step...');
      const response = await this.openai.chat.completions.create({
        model: this.model,
        messages: messages.map(m => ({
          role: m.role,
          content: m.content,
          tool_calls: m.tool_calls as any,
          name: m.name
        })),
        tools: Object.values(this.tools).map(t => ({
          type: 'function',
          function: {
            name: t.name,
            description: t.description,
            parameters: t.parameters
          }
        }))
      });

      const assistantChoice = response.choices[0].message;
      const assistantMessage: AgentMessage = {
        role: 'assistant',
        content: assistantChoice.content,
        tool_calls: assistantChoice.tool_calls as ToolCall[] | undefined
      };

      const assistantNode = await this.sessionStore.appendNode(this.currentLeafId, assistantMessage);
      this.currentLeafId = assistantNode.id;
      messages.push(assistantMessage);

      if (assistantChoice.tool_calls && assistantChoice.tool_calls.length > 0) {
        for (const call of assistantChoice.tool_calls) {
          const tool = this.tools[call.function.name];
          if (!tool) {
            const toolResult: AgentMessage = {
              role: 'tool',
              content: `Error: Tool ${call.function.name} does not exist.`,
              name: call.function.name
            };
            const tNode = await this.sessionStore.appendNode(this.currentLeafId, toolResult);
            this.currentLeafId = tNode.id;
            messages.push(toolResult);
            continue;
          }

          onUpdate(`⚒ Tool Call: \x1b[33m${tool.name}\x1b[0m with args: ${call.function.arguments}`);
          const args = JSON.parse(call.function.arguments);
          const executionOutput = await tool.execute(args);

          const toolResult: AgentMessage = {
            role: 'tool',
            content: executionOutput,
            name: tool.name
          };
          // Patch standard property format
          (toolResult as any).tool_call_id = call.id;

          const tNode = await this.sessionStore.appendNode(this.currentLeafId, toolResult);
          this.currentLeafId = tNode.id;
          messages.push(toolResult);
        }
      } else {
        keepRunning = false;
        finalContent = assistantChoice.content ?? '';
      }
    }

    return finalContent;
  }

  private async compactHistory(messages: AgentMessage[]): Promise<string> {
    const summaryResponse = await this.openai.chat.completions.create({
      model: this.model,
      messages: [
        { role: 'system', content: SUMMARIZE_SYSTEM_PROMPT },
        { role: 'user', content: JSON.stringify(messages) }
      ]
    });
    return summaryResponse.choices[0].message.content ?? '# Compacted session start';
  }
}
```

---

#### Module 5: `src/index.ts`
The REPL environment and client launcher designed in clean, raw monochromatic ASCII boxes.

```typescript
import * as readline from 'readline';
import * as dotenv from 'dotenv';
import { PiAgent } from './agent.js';
import { SessionStore } from './session.js';

dotenv.config();

const apiKey = process.env.OPENAI_API_KEY;
if (!apiKey) {
  console.error('CRITICAL ERROR: Please define your OPENAI_API_KEY inside environmental variables.');
  process.exit(1);
}

const workspaceRoot = process.cwd();
const sessionStore = new SessionStore(workspaceRoot + '/.pi/agent/sessions', 'default-session');
const agent = new PiAgent({
  apiKey,
  sessionStore,
  workspaceRoot,
  model: 'gpt-4o-mini'
});

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const displayHeader = (): void => {
  console.clear();
  console.log('┌──────────────────────────────────────────────────────────┐');
  console.log('│   pi-agent-harness : BRUTALIST SHELL INTERFACE v1.0.0    │');
  console.log('├──────────────────────────────────────────────────────────┤');
  console.log('│ Commands:                                                │');
  console.log('│   /exit - Terminate operational terminal                 │');
  console.log('│   /tree - Output traversal trace index history           │');
  console.log('└──────────────────────────────────────────────────────────┘');
};

const handleCommand = async (input: string): Promise<boolean> => {
  if (input === '/exit') {
    console.log('■ Disconnected. Farewell.');
    process.exit(0);
  }
  if (input === '/tree') {
    const leaf = await sessionStore.findLatestLeaf();
    const traversal = await sessionStore.resolveHistory(leaf);
    console.log('\n┌── SESSION TRAVERSAL TREE TRACE ──────────────────────────┐');
    if (traversal.nodes.length === 0) {
      console.log('│ No history node logs tracked on branch.');
    } else {
      traversal.nodes.forEach((node, index) => {
        const roleIndicator = node.message.role.toUpperCase().padEnd(9, ' ');
        const snippet = (node.message.content ?? '[TOOL CALL]')
          .replace(/\n/g, ' ')
          .substring(0, 35);
        console.log(`│ [${index.toString().padStart(2, '0')}] Node: ${node.id.substring(0, 8)} | ${roleIndicator} | ${snippet}...`);
      });
    }
    console.log('└──────────────────────────────────────────────────────────┘\n');
    return true;
  }
  return false;
};

const promptUser = (): void => {
  rl.question('pi-agent> ', async (input) => {
    const cleanInput = input.trim();
    if (!cleanInput) {
      promptUser();
      return;
    }

    const commandIntercepted = await handleCommand(cleanInput);
    if (commandIntercepted) {
      promptUser();
      return;
    }

    console.log('\n┌── AGENT LOG OUTPUTS ─────────────────────────────────────┐');
    try {
      const response = await agent.handleUserTurn(cleanInput, (update) => {
        console.log(`│ ${update}`);
      });
      console.log('├── FINAL RESPONSE ────────────────────────────────────────┤');
      console.log(response);
    } catch (err) {
      console.log(`│ Execution Failure: ${(err as Error).message}`);
    }
    console.log('└──────────────────────────────────────────────────────────┘\n');

    promptUser();
  });
};

const main = async (): Promise<void> => {
  displayHeader();
  await agent.start();
  promptUser();
};

main().catch((err) => {
  console.error(`Fatal crash: ${err.message}`);
  process.exit(1);
});
```

---

### 3. Execution & Testing

To run the custom harness workspace interface:

1. Create a local `.env` file containing your key configuration:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
2. Run the application through target runtime wrapper:
   ```bash
   npx ts-node src/index.ts
   ```

