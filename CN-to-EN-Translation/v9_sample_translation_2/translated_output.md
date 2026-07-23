Background
Let's first answer a preliminary question: How did we get here?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, you must first see the complete arc that AI engineering has traced over the past four years. That arc is not linear—it is a cycle of **capability jumps → old frameworks collapsing → new abstractions emerging** repeating over and over.

Related reading for additional background:

- [AI Operating System: From Instructions to Intent](https://yage.ai/ai-os.html)
- [From Prompt Engineering to Context Engineering](https://yage.ai/context-engineering.html)
- [The Token Naming Dilemma: When Information Theory Collides with Linguistics](https://yage.ai/token-naming.html)
- [OpenClaw: The Hidden Dangers Behind the Madness](https://yage.ai/openclaw.html)
- [Deep Dive: Google Workspace CLI](https://yage.ai/google-workspace-cli.html)
- [Meta-Skill: Making AI Think Like You](https://yage.ai/meta-skill.html)
- [Brief Thoughts on Agent Trends: Nativization & CLI-fication](https://yage.ai/agent-trends.html)
- [AI Coding Ecosystem: What Does Anthropic's Acquisition of Bun Mean?](https://yage.ai/anthropic-bun.html)
- [Deep Thinking: On AI Development Trends](https://yage.ai/ai-deep-thinking.html)
- [A Brief Talk on AI Browsers](https://yage.ai/ai-browser.html)
- [Deep Dive: The Anthropic MCP Protocol](https://yage.ai/mcp.html)

---

## Act One: Generation (Nov 2022 — 2023)

On November 30, 2022, ChatGPT launched. It reached approximately 100 million monthly active users in about two months. But what this truly changed was not NLP technology—GPT-3 had already existed for two years—it was the **interaction paradigm**. Before this, an LLM was an API that only engineers could use; after this, it became a conversational interface that everyone could use.

The core contradiction in this act was: **the model could generate, but it could not act.** It could write an email, but not send it; it could write code, but not run it. The relationship between user and model was "you ask, I answer"—a stateless, single-turn, passive information exchange.

The engineering artifact of this era was **Prompt Engineering**: how to ask so that the model answers better. Few-shot, chain-of-thought, role-playing—at their core, these were all ways to maximize information density within the limited space of a single API call.

---

## Act Two: Connection (2023 — 2024)

In March 2023, OpenAI released GPT-4, bringing multimodality and longer context windows. That same month, ChatGPT Plugins launched, giving the model "hands" for the first time—it could call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool invocation as structured JSON in model outputs.

This was a critical turning point: the model had evolved from "being able to talk" to "being able to connect." But the Plugins ecosystem quickly revealed its fragility—each plugin required its own OAuth flow, its own schema definition, its own error handling. Connecting 10 plugins was already painful; 100 was impossible.

In the second half of 2023, LangChain rose, attempting to solve the "connection" problem with a layer of intermediate abstraction. It indeed lowered the barrier to entry, but also introduced the cost of over-abstraction—too many layers of wrapping, difficult debugging, unpredictable performance. Around the same time, projects like AutoGPT and BabyAGI tried to make models autonomously loop through tasks, but lacking reliable stopping conditions and verification mechanisms, they quickly faded after their demos.

🤯 **Lesson One**

Enabling models to "connect to tools" is necessary, but far from sufficient. Connection is not orchestration, and orchestration is not governance.

---

## Act Three: Reasoning (2024)

2024 was the year "reasoning models" took the stage. OpenAI's o1 series, released in September, featured "spending more time thinking before answering" and achieved a qualitative leap in math and programming tasks. In December, the ARC Prize announced that OpenAI o3, in its high-compute configuration, achieved 87.5% on the ARC-AGI-1 Semi-Private Eval, stunning the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet excelled at code generation and long-document understanding, and DeepSeek-R1, as an open-weight model, proved that high-performance reasoning was no longer a closed-source monopoly.

But more important were two events at the end of 2024:

**First: Anthropic released the Model Context Protocol (MCP).** This was not yet another plugin system—it was an open standard protocol that used JSON-RPC 2.0 to define how AI applications communicate with external tools and data sources. Its core insight was: the connection problem is fundamentally an N×M problem—N AI applications × M data sources, each combination requiring a custom connector. MCP simplifies this to N+M: each application implements an MCP client once, each tool implements an MCP server once. Later, OpenAI and Google DeepMind announced support for MCP, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

**Second: Anthropic published the *Building Effective Agents*[^1] guide (December 2024).** This article systematically discussed agent engineering patterns for the first time—from the simplest prompt chaining to evaluator-optimizer loops—and clearly proposed a principle: **start with the simplest pattern, and only introduce more structure when complexity genuinely delivers better results.** This principle later became one of the core guiding ideas of harness engineering.

By 2025, Anthropic had further elevated context engineering into an independent engineering practice with *Effective context engineering for AI agents*[^2], emphasizing that the real challenge was no longer just "how to write a prompt," but "at each step, what information, in what form, and at what timing to give to the model." This was the critical transitional layer between Prompt Engineering and Harness Engineering—the problem had shifted upward from "a single invocation" to "per-step context," but had not yet risen to "the entire outer task loop."

🤯 **Lesson Two**

A model's reasoning ability solves the "single-step quality" problem, but the reliability of long-duration tasks is not automatically obtained just because individual steps become smarter. A model that can solve IMO gold medal problems will still "forget what it was doing" midway through a four-hour full-stack development task.

---

## Act Four: Action (2025)

If 2023 was the year of the Chatbot and 2024 was the year of Multimodality, then 2025 was the **year of the Agent**.

At the start of the year, DeepSeek-R1's open-source release forced the market to reassess the competitive landscape of models. This was followed by a cascade of agent products: Claude Code (terminal-based programming agent), GitHub Copilot Agent Mode, Cursor's autonomous coding loop, Manus (browser-operating agent), OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all major languages. Google released the Agent2Agent (A2A) protocol to solve cross-vendor communication between agents.

But the most important discovery of 2025 was not what agents could do—it was **how agents broke while doing it**:

- An agent would attempt to complete an entire task in one go, exhausting its context window midway through.
- An agent would announce "all done" after completing 70%, then stop.
- Multiple agents operating in parallel would produce cascading errors, with a single small mistake amplified to an undebuggable scale.
- Codebases would develop severe "AI slop" after continuous agent work—redundant code, inconsistent naming, outdated documentation.

These were not problems of the model's intelligence. They were **structural problems of the system.**

🤯 **Lesson Three**

Agent capabilities have reached the level of "being able to work autonomously for hours," but the engineering infrastructure surrounding them remains stuck in the era of "single conversations." This rupture is the root cause of Harness Engineering's emergence.

---

## Act Five: Governance (2026 — Present)

At the start of 2026, the industry's attention began shifting from "how to make agents more capable" to "how to keep agents from crashing." "Harness Engineering" as a public term was not invented on a single day, but rather experienced rapid coinage and diffusion starting in February 2026:

- **February 5, 2026:** Mitchell Hashimoto, in *My AI Adoption Journey*[^3], explicitly wrote "Engineer the Harness"—considered one of the starting points for the term entering mainstream discussion.
- **February 11, 2026:** OpenAI directly published an engineering article titled *Harness Engineering: Leveraging Codex in an Agent-First World*[^4]. With a small team, building from an empty repository over five months to produce an internal beta product, they publicly stated "zero lines of hand-written code," with the repository reaching approximately one million lines of code and generating roughly 1,500 PRs. More precisely, the initial scaffold was still generated by Codex under minimal template guidance, after which application logic, tests, CI, documentation, observability, and internal tools were produced by agents wherever possible. Key finding: **the engineer's focus shifted to designing environments, specifying intent, and building feedback loops.**
- **March 2026:** Anthropic published *Harness Design for Long-Running Application Development*, upgrading the previous two-role architecture (initializer/coding) to a three-role system (planner/generator/evaluator), demonstrating that the evaluator still brings significant gains near the model capability boundary.
- **April 2026:** The Thoughtworks/Fowler camp (*Harness Engineering - first thoughts*[^5]) systematized the concept into a more complete methodological framework—a combination of **guides** (feedforward control) and **sensors** (feedback control), each further divided into **computational** (deterministic) and **inferential** types, forming a 2×2 control matrix. Thus, April is better understood as "when the methodological abstraction became complete" rather than "when it was first named."

---

## What Exactly Is a Harness?

Let's derive it from first principles, not from a definition.

### The Five Fundamental Challenges of Agents

The essence of an agent is "a system that autonomously advances toward goals in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone:

**1. State Persistence**
- Essence: The agent needs to remember what it has done across time and sessions.
- Why models can't solve it: Models are inherently stateless, context windows have upper limits, and they cannot naturally assume long-term continuous state.

**2. Goal Coherence**
- Essence: In long-duration tasks, agents tend to drift, get carried away, or even declare completion early.
- Why models can't solve it: Models lack external anchoring and cannot reliably calibrate what "truly counts as done."

**3. Action Verifiability**
- Essence: Every step is probabilistic—we need to distinguish between "it was done" and "it was done correctly."
- Why models can't solve it: When evaluating their own results, models naturally exhibit a tendency toward self-praise and misjudgment.

**4. Entropy Suppression**
- Essence: Continuous output accumulates redundancy, drift, and inconsistency.
- Why models can't solve it: Models replicate existing patterns, even when those patterns are themselves bad or low-quality.

**5. Human-Machine Boundary**
- Essence: When to act autonomously and when to hand off to a human needs clear and engineering-defined boundaries.
- Why models can't solve it: Models lack reliable "uncertainty awareness" and cannot stably determine when to stop and hand off to humans.

**A Harness is the engineering practice that systematically addresses these five challenges.**

### A Precise Definition

Anthropic, in *Demystifying evals for AI agents*[^6], offers a definition worth adopting directly: **An agent harness (or scaffold) is the system that enables a model to act as an agent; it handles input, orchestrates tool calls, and returns results.** More critically, Anthropic further points out: when we evaluate "an agent," what we're actually evaluating is the **model + harness combination**, not the model's capability alone. This definition is important because it shifts the unit of explanation for agent effectiveness—from model parameters to the outer-loop structure in which the model operates.

![Diagram illustrating model + harness = evaluation combination](https://yage.ai/agent-harness-eval.jpg)

Here we must disentangle a frequently conflated concept: **an agent harness and an evaluation harness are not the same thing.** The former is responsible for making the agent run (processing input, orchestrating tools, managing state); the latter is responsible for batch-running tasks, recording trajectories, executing graders, and aggregating scores. Many discussions lump "harness" into one big basket, resulting in one moment talking about runtime orchestration and the next about evaluation pipelines. The Harness Engineering discussed in this article refers to the former—the engineering of the **runtime outer-loop system.**

Based on this, a more precise formulation:

> **A Harness = The outer-loop system that enables a model to act as an Agent.**
>
> It includes plan decomposition, persistent state, tool orchestration, verification gates, feedback loops, rollback mechanisms, human-machine handoff points, and audit logs. When evaluating an Agent's effectiveness, what is evaluated is not the model itself, but the **model + harness combination.**

Several points are worth elaborating:

**Outer-loop** is the keyword. The model's reasoning is the "inner loop"—given context, generate the next step. The Harness is the "outer loop"—deciding when to start a new inner loop, what context to give it, how to verify its output, when to roll back, when to stop. The quality of the inner loop depends on model capability; the quality of the outer loop depends on harness design.

**A Harness is not an upgraded prompt.** A single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control. Treating a Harness as "a longer system prompt" is the most common failure mode today.

**A Harness is also not the name of a framework.** LangChain is a framework, CrewAI is a framework. Harness Engineering is not. It is a **practice**, just as DevOps is not a tool but an engineering culture.

---

## Three Layers of Engineering Abstraction

### Prompt → Context → Harness

To understand the position of Harness, you must first see its relationship with the two layers below it. These three layers are not replacements for each other—they are **progressive levels of abstraction**:

| Layer | Core Question | Time Horizon | Unit of Analysis |
|---|---|---|---|
| **Prompt Engineering** | What text to include in a single API call? | Single turn | Text composition |
| **Context Engineering** | What information to give the model at each step? | Single step | Information architecture |
| **Harness Engineering** | How does the entire pipeline operate? | Entire task | System architecture |

> **Key Insight**
>
> Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline runs." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; but a harness also includes multi-step structure, tool mediation, verification gates, and durable state—these go beyond the scope of single-step context.

---

## The Six Engineering Components of a Harness

This section is the most hardcore part of the entire article. Each component explains what problem it solves, how Anthropic/OpenAI specifically approach it, and the design principles behind it.

### 1. Durable State Surfaces: Making Agents Stop "Starting from Amnesia"

**Problem:** The core pain point of long-duration agents is like having an engineer on a project team who suffers complete amnesia every shift change. Context windows are limited; complex projects cannot be completed within a single window. Agents need a way to bridge the gap between sessions.

**Anthropic's Solution:** Rather than attempting "infinite context," they externalize state into **durable artifacts**:

1. An initializer agent sets up the environment: creates `init.sh` (startup script), `claude-progress.txt` (progress log), and an initial git commit (baseline snapshot).
2. Generates a **feature list**: expands high-level requirements into 200+ concrete features, all initially marked as failing.
3. Each subsequent coding agent only makes incremental progress, leaving structured updates and a "clean state" at the end of each session.
4. **Key rule:** Agents can only change a feature's passes/fails status; they cannot arbitrarily modify the test definitions themselves.

This feature list design may look "crude," but it is extremely effective—it transforms the definition of "done" from the agent's subjective feeling into an **external, persistent, structured, and inheritable completion surface.** The agent doesn't need to "remember" what it did before; it only needs to read the feature list and git diff to resume within 30 seconds.

Anthropic later discovered an even deeper problem: **context anxiety.** Even with compaction (summarizing and compressing early conversation history), agents would still exhibit behavioral degradation because they "felt" the context was too full. The solution was not better compaction, but **context reset**—directly giving the next agent a brand-new context, passing all necessary information through externalized state artifacts (not conversation history). This is more aggressive than compaction, but works better.

> **Design Principle**
>
> State ≠ "saving chat history." True durable state is a structured artifact that an agent can read, understand, and resume from after a cold start, with no context history whatsoever. If your agent cannot know within 30 seconds of a cold start "how far we got and what to do next," your state management is failing.

---

### 2. Decomposition & Plans: Cutting Long Tasks into Agent-Sized Chunks

**Problem:** Tell an agent "build a clone of claude.ai," and it will try to go all in—writing all the code in a single session. Result: either context explodes, or it announces "done" halfway through.

**Evolution:**

- **November 2025:** Anthropic initially solved this with a two-role structure: initializer + coding. The initializer handled decomposition and initialization; the coding agent handled incremental implementation.
- **March 2026:** This structure was upgraded to a **planner / generator / evaluator** three-role system:
  - **Planner** doesn't write code directly, but expands a one- or two-sentence high-level description into a complete product spec and step-by-step feature list.
  - **Generator** implements each feature incrementally, committing after each completion.
  - **Evaluator** independently evaluates the generator's output, marks pass/fail, and provides specific improvement suggestions.

- **OpenAI's counterpart:** `PLANS.md`, `Implement.md`, `Documentation.md`—complex tasks are planned first, executed milestone by milestone, with verification at each stage, and documentation is continuously updated as shared memory.

> **Design Principle**
>
> Plans must be elevated to **first-class artifacts**, not one-time chat content. They need to be written to the filesystem, version-controlled, readable by subsequent agents, and referenced by verification gates. A plan that exists only inside a conversation is not a plan—it's just a thought.

---

### 3. Feedback Loops: Guides & Sensors

**Problem:** An agent writes code—how do you know whether it's correct? Rely on the agent to evaluate itself? Anthropic explicitly uncovered an uncomfortable fact: **when asked to evaluate their own work, agents tend to enthusiastically praise themselves—even when the quality is clearly mediocre by human standards.**

This necessitates a feedback system that does not rely on agent self-evaluation. By April 2026, the community had frameworks that decomposed harness into a clear 2×2 matrix:

| | **Computational** (Deterministic) | **Inferential** (Probabilistic) |
|---|---|---|
| **Guides** (Feedforward) | Type checking, linting, static analysis, schemas | System prompts, architecture constraints, style guides |
| **Sensors** (Feedback) | Test suites, CI checks, assertion validations | Code review, evaluator LLM, visual assessment |

**Guides** constrain the agent before it acts, increasing the probability of "getting it right the first time." **Sensors** signal the agent after it acts, supporting self-correction.

**Key Insights:**
- **Guides without sensors** → the agent encodes rules but never knows whether they took effect.
- **Sensors without guides** → the agent repeats the same errors only to be corrected each time.
- **Computational control** is cheap, fast, and deterministic—it can run on every change.
- **Inferential control** is expensive, slow, and non-deterministic—but it can handle subjective judgments (e.g., "is this UI design too ugly?").

Anthropic's evaluator-optimizer pattern is fully consistent with this. They also acknowledge a subtle fact: **evaluators are not always necessary.** When the base model's capability crosses a certain threshold, the evaluator degrades from "essential component" to "extra overhead." This shows that a good harness is not a fixed template, but a **tailorable system that co-evolves with the model's capability boundary.**

![Diagram showing computational guides, computational sensors, inferential guides, inferential sensors in a 2x2 matrix](https://yage.ai/harness-guides-sensors.png)

---

### 4. Legibility: Building a Perception Surface for Agents

**Problem:** Agents can write code—but can they "see" what their code looks like when it runs? Can they read error logs? Can they understand performance metrics?

OpenAI, in their harness engineering practice, offered an extremely sharp judgment: **Anything outside an agent's runtime-visible range effectively does not exist.**

This is not rhetoric. They did the following concrete work to improve legibility:

- Launched an independent browser instance for each git worktree, using CDP (Chrome DevTools Protocol[^7]) to let agents "see" the UI.
- Exposed logs, metrics, and traces for agent querying.
- Used **repository knowledge as the system of record**: design principles, product intent, execution plans, known technical debt, architecture decision records (ADRs)—all stored in the repo and kept consistent via lint/CI.
- Stored `AGENTS.md`, structured `docs/`, execution plans, and knowledge documents in the repo as much as possible, making them a versioned system of record. However, OpenAI also publicly warned: **overly long `AGENTS.md` files rot quickly, crowd out context, and cause all constraints to lose focus simultaneously**—a better approach is to turn it into a directory index, with real knowledge scattered across structured documents.

> **Design Principle**
>
> Legibility is not about "making code more elegant"—it's about bringing knowledge, constraints, acceptance criteria, and decision history into the agent's perception surface. This directly transforms "knowledge management" from a team collaboration problem into an agent executability problem. For an agent, experience shared in Slack, architectural boundaries passed down verbally, and constraints scattered across external documents—if they don't enter the runtime-accessible artifact surface, they do not exist.

---

### 5. Tool Mediation: More Tools Demand More Harness

**Problem:** After the MCP ecosystem explosion, an agent might connect to dozens of MCP servers, accessing hundreds of tools. But stuffing all tool definitions into context creates serious problems—soaring token costs, increased latency, and agents getting lost in a sea of tools.

Anthropic, in their MCP + Code Execution engineering practice, proposed a core idea: **Don't let the model call tools directly—let the model write code to call tools.**

What's the difference?

- **Direct tool-calling mode:** All tool definitions are loaded into context → model selects a tool → calls it → result is passed back to context → model continues. Every step consumes context space; intermediate results stay within the model's inner loop.
- **Code execution mode:** The model writes code → the code runs in a sandbox, discovering and calling MCP tools on demand → only the final result is passed back to the model. Tool discovery, data filtering, and intermediate processing all happen inside the execution environment—they never enter context.

The essence of this idea is: **move tool usage from the model's inner loop to a more efficient external execution circuit.** This is precisely harness engineering—it is not a "tool registry," but a system-level design that determines **how tools are discovered, when they are exposed, at what granularity, whether results need to enter context, where state lives, and how failures roll back.**

---

### 6. Entropy Control: Continuous Garbage Collection for Agents

**Problem:** Fully autonomous agent codebases continuously replicate existing patterns—even when those patterns are uneven, suboptimal, or outright bad. Over time, drift and entropy are inevitable.

OpenAI put this most plainly: **initially, they relied on humans spending about 20% of their time each week cleaning up "AI slop"** —redundant code, outdated documentation, inconsistent naming, copy-pasted dead code. Later, they systematized this cleanup:

- **Documentation consistency agents** periodically verify that documentation aligns with code.
- **Refactor agents** systematically clean up technical debt according to plan.
- **Architectural enforcement** mechanizes module boundary maintenance through CI.

> **Design Principle**
>
> A Harness is not only responsible for "making the agent run"—it is also responsible for **continuously suppressing the system noise that agents amplify.** This is the most fundamental distinction between a harness and a simple "agent framework"—frameworks care about startup and orchestration; harnesses care about **long-term governability.**

---

## Harnessability: Not Every System Is Equally Easy to Harness

If you only understand Harness Engineering as "adding more rules and loops for the agent," you haven't gone deep enough. The more fundamental question is: **Not every system is equally easy to harness.**

OpenAI's practice consistently hints at the same thing: the reason they could push Codex to high throughput was not just that the model was strong enough, but also because they **continuously pushed knowledge back into the repo, artifactized plans, versioned decisions, and made the environment more legible to agents.** How naturally suited a system is to being tamed by agents is itself an important variable.

Following this logic yields a highly explanatory judgment: **Strongly typed, well-tested, clearly bounded, versioned-documented, runtime-observable systems naturally have higher harnessability; systems whose knowledge is scattered across human brains, chat tools, and word-of-mouth—no matter how strong the model—will first hit the wall of "invisible → incomprehensible → ungovernable."**

This means that in the agent era, a team's engineering infrastructure quality (CI completeness, documentation structure, architecture boundary clarity) is no longer just a matter of "engineering maturity"—it **directly determines how far an agent can go on your system.** Harnessability will become a key dimension for evaluating a system's "agent-readiness."

---

## The Intent System

### A Deeper Paradigm Shift: From Instruction-Driven to Intent-Driven

The above covers the engineering components of a Harness. But if you look only at the components, you'll get lost in a "patchwork of technical details." Let's step back and talk about something more fundamental—why Harness Engineering is not just an engineering practice, but a product of a **paradigm shift.**

### The Four Ruptures in Human-Computer Interaction

Looking back at the entire history of computing, human-computer interaction has undergone four fundamental ruptures:

1. **CLI (Command Line):** Humans must precisely master the machine's language. `ls -la | grep .py` is a command; a single wrong character in the syntax and it fails. Core assumption: **the human adapts to the machine.**

2. **GUI (Graphical Interface):** The machine lowers the barrier through visual metaphors. Folders, desktops, drag-and-drop. Core assumption: **the machine presents itself through metaphors humans can understand.**

3. **App (Mobile Applications):** Logic is solidified into fixed interfaces. One function per button, one button per screen. Core assumption: **the human chooses among preset paths.**

4. **Agent (Intent-Driven):** Humans only express goals; the system autonomously plans the execution path. Core assumption: **the machine understands human intent and autonomously decides how to proceed.**

Each rupture is not just a technological upgrade—it is a **redistribution of control.** In the CLI era, humans held 100% control. In the Agent era, humans cede most execution control, retaining only goal-setting and key decision points.

What are the engineering consequences of this ceding?

In an instruction-driven world, a bug is "the system did not correctly execute my instruction"—which can be covered by traditional testing. In an intent-driven world, a bug becomes "the system misconstrued my intent" or "the system correctly understood my intent but chose a terrible execution path"—requiring an entirely new set of verification, constraint, and feedback mechanisms. **This is precisely what a Harness must solve.**

### Applications Are Being "CLI-fied"—But Not for Humans

A deeply counterintuitive trend: in the Agent era, all applications and websites are being re-"CLI-fied"—not to send users back to the terminal, but to turn everything into **programmable interfaces from the Agent's perspective.**

MCP is the protocol-level implementation of this. When an Agent needs to operate Google Drive, it no longer needs to "open a webpage and click buttons"—it needs a set of structured API calls. MCP servers abstract Google Drive into a set of callable functions: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This means three things:

**First, the target of readability has changed.** In the past, readability was for humans—clear UI, reasonable information architecture. Now, it must first be readable for agents—structured APIs, machine-parseable documentation, programmable permission models.

**Second, application boundaries are dissolving.** When an Agent calls any tool via MCP and collaborates with other Agents via A2A, the App degrades from "destination" to "infrastructure." Users no longer "open an App to do something"—they "express an intent, and the Agent orchestrates multiple services to fulfill it."

**Third, the Harness becomes the new "operating system layer."** The GUI-era OS managed windows, files, and processes. The Agent era needs to manage: agent lifecycles, tool discovery and authorization, context scheduling and reclamation, multi-agent collaboration and isolation, and human approval intervention points.

---

## From Chatbot to AgentOS

Tying all the threads above together reveals a clear evolutionary path. These three stages are not functional stacking—they are **fundamental changes in engineering abstraction layers:**

| Level | Era | Core Characteristics | Engineering Abstraction Layer | Representative Products | Ceiling |
|---|---|---|---|---|---|
| **Level 1: Chatbot** | 2022-2023 | Single conversation, stateless, human fully in the loop | Prompt Engineering | ChatGPT, Claude (early) | Can talk but cannot act. Every conversation is isolated. |
| **Level 2: AI Browser / Agent IDE** | 2024-2025 | Multi-step tasks, tool calling, limited autonomy | Context Engineering + Lightweight Harness | Claude Code, Cursor, Manus, Codex | Strong single-agent capability but unstable long tasks; multi-agent collaboration lacks standards; state management is manual labor. |
| **Level 3: AgentOS** | 2026 (budding phase, forward-looking direction) | Always-on, multi-agent, cross-tool, cross-identity | Harness Engineering → AgentOS | TBD | |

I must write this section with restraint. AgentOS is not yet a converged industry paradigm. But it has already entered the research and systems community agenda. The 2024 AIOS[^8] paper proposed extracting scheduling, context management, memory management, and access control from the agent application layer into a kernel-like layer; ASPLOS 2026 features a dedicated AgenticOS Workshop[^9] exploring OS primitives for agent workloads.

Thus, the safer statement is not "AgentOS has arrived," but rather: **Harness Engineering is pushing problems from the application layer toward the system layer.** When agents are no longer just coding assistants, but always-on, multi-agent, cross-tool, cross-identity long-running entities, user-space harnesses will inevitably eventually encounter deeper system-level problems:

- **Agent lifecycle management:** initialization, running, suspension, resumption, termination—not stateless function calls, but complete process management.
- **Context scheduling:** Context windows are scarce resources—deciding what information to load, compress, or discard at what time—this is the "memory management" equivalent for agents.
- **Multi-agent isolation & collaboration:** One agent's operations should not pollute another's environment, yet they need to share certain state—requiring mechanisms analogous to process isolation + IPC.
- **Governance & audit:** Every decision made by every agent must be traceable—in finance, healthcare, and other regulated domains, this is not a nice-to-have but a compliance requirement.

> **Key Positioning**
>
> A **Harness is the user-space layer of AgentOS.** AgentOS is the kernel—handling scheduling, isolation, and resources. The Harness is the user-space shell and daemon—handling task decomposition, state persistence, verification feedback, and human-machine handoff. The two are not competitors, but naturally a lower and upper layer.

---

## Five Typical Symptoms

Theory done. Back to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are still operating at the level of temporary patchwork. Here are five typical symptoms:

**Symptom One: Framework Jungle.** LangChain, CrewAI, AutoGen, Agno, n8n... Each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to verification to rollback to audit. Users piece things together across different frameworks and end up with a fragile pipeline, not a governable system.

**Symptom Two: Chatbot Skin + Agent Core.** A large number of products are essentially a chatbot interface wrapped around an agent loop—but lacking genuine state management, task decomposition, and verification gates. Impressive in demos, but frequently crashing in production.

**Symptom Three: Tool Registration ≠ Tool Governance.** MCP makes connection easy, but "being able to connect" is not the same as "knowing how to use." An agent faced with 50 tools becomes confused, makes redundant calls, and takes detours. Some engineering teams found that initially giving agents all available tools actually produced **worse** results—improvement only came after trimming down to the minimum necessary set.

**Symptom Four: One-Time Rules vs. Evolvable Constraints.** Most teams' agent configuration is a massive `AGENTS.md` or system prompt. But practice shows this approach inevitably fails—when everything is important, nothing is important. The agent pattern-matches locally instead of navigating deliberately. Rules rot faster than humans can maintain them.

**Symptom Five: Lack of On-the-Loop Thinking.** "In the loop" means manually tweaking artifacts when unsatisfied with agent output; "on the loop" means changing the harness so the system automatically produces better results next time. Most teams remain stuck in the loop—fixing errors one by one, rather than systematically improving the control circuits that produce those errors.

---

## What a Harness Is Not

Clarifying boundaries is as important as clarifying definitions.

- **It is not "a longer system prompt."** A single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control.
- **It is not a proprietary term from any single vendor.** Anthropic and OpenAI both use it publicly; academic preprints are already abstracting it into a cross-product general concept.
- **It is not something that "becomes unnecessary as models get stronger."** Quite the opposite—Anthropic explicitly states that as the model capability boundary expands, harness value will be redistributed: some checks become redundant, but planning, verification, handoff, and state governance for increasingly harder tasks become even more important. The stronger the model, the more you need to place longer, costlier, and riskier tasks into a controlled outer loop.

In fact, the space of **interesting harness combinations** will not shrink as models get stronger—it will **shift.** Today's effective evaluator may become redundant overhead before the next-generation model, but new capability boundaries will give rise to new harness requirements.

---

## Overlooked Critical Problems

### Testability of the Harness Itself

When we say "the harness makes the agent verifiable," a meta-question arises: **how does the harness itself get verified?** If the evaluator uses another LLM, and that LLM also has a tendency toward hallucination, then we have constructed a "verifying an unreliable system with an unreliable system" loop.

Anthropic's approach is to primarily use **computational sensors** (test suites, linters, type checking) for basic verification, and only enable **inferential sensors** for subjective judgments (UI aesthetics, code style). This is a pragmatic layered strategy, but not a perfect solution.

### Emergent Behavior in Multi-Agent Systems

When 10 agents run in parallel, each making independent decisions, system-level behavior emerges that cannot be predicted by analyzing any single agent. This resembles concurrency bugs in distributed systems—but worse, because every "process" is non-deterministic. Current harness design primarily targets single-agent scenarios; harness principles for multi-agent collaboration have yet to crystallize.

### Engineering Trade-offs in Cost and Latency

Every layer of the harness—planner, evaluator, sensor, garbage collection—consumes additional tokens and latency. When the overhead of the harness itself exceeds the quality improvements it brings, that is **over-engineering.** How to measure the ROI of a harness, and how to dynamically adjust harness depth based on task complexity, are still unsolved engineering problems.

### A New Dimension of Security: The Attack Target Shifts from Data to Agency

This is the layer that many articles tend to gloss over, yet it is perhaps the most dangerous. As agents gain persistent state, external tools, and long-duration autonomy, the attack surface is no longer just "the model answered something wrong," but "could the system be manipulated via proxy?"

In April 2025, Invariant Labs disclosed **Tool Poisoning Attacks**[^10]: malicious instructions can be hidden inside MCP tool descriptions—invisible to users, but visible to models—thereby inducing agents to execute unauthorized operations. A week later, they demonstrated a data exfiltration scenario leveraging untrusted MCP servers in conjunction with a trusted WhatsApp MCP server. This means Harness Engineering cannot only deal with throughput and stability—it must also directly address **tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation.**

MCP's open standardization is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connectivity becomes, the more the **upper-layer harness must perform stricter governance.** The harness's permission model must evolve from static "allowed/not allowed" to dynamic: "allowed under what conditions, up to what limit, only after human confirmation." In other words, **the harness is not just an output-enhancing outer loop—it is itself a new security boundary.**

---

## Judgments & Outlook

### Judgment One: Harness Engineering Will Become a Foundational Discipline of the AI Engineering Era

Model capability improvements will continue to swallow some micro-level prompt techniques, but they will **not** swallow harness engineering. Because it deals with a higher-level problem: **how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system.** As long as agents must work across time, across tools, across environments, and across human-machine boundaries, the harness will not disappear—on the contrary, it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

### Judgment Two: The Center of Gravity of the Moat Is Shifting from Model Quality to Harness & System Design

When GPT, Claude, and Gemini converge on core capabilities, what determines product success is no longer model differentiation, but **harness quality.** The hardest evidence comes from LangChain: keeping the underlying model unchanged and only modifying the harness, they improved `deepagents-cli` on Terminal Bench 2.0 from 52.8% to 66.5%—a gain of 13.7 points, pushing the ranking from outside the Top 30 into the Top 5. This result cannot be exaggerated into "models no longer matter," but it is sufficient to demonstrate: **on top of the same model, the harness alone can create a huge system-level gap.** The center of gravity of the moat is shifting upward—to harness and system design.

### Judgment Three: The Migration from Chatbot to AgentOS Will Not Happen in One Step

There will be an intermediate 2–3 year phase of **"AI Browser + Lightweight Harness."** Most enterprises will derive value in this phase first, then gradually evolve toward heavier AgentOS architectures. Teams attempting to jump directly to AgentOS will likely fail because governance complexity exceeds their capacity.

### Judgment Four: The Engineer's Role Is Shifting from "Code Producer" to "Autonomous System Designer"

This is not a layoff warning—it is a **capability upgrade requirement.** Defining intent, shaping environments, setting boundaries, designing feedback, absorbing anomalies, and codifying rules—the value of these capabilities will rise sharply. When unsatisfied with agent output, the low-level approach is to manually tweak the artifact; the high-level approach is to **change the harness so the system automatically does better next time.** From **in the loop** to **on the loop** —this is the engineer's core upgrade path in the agent era.

---

## Appendix

### Three Self-Check Questions for Practitioners

Before you start building your own harness, answer these three questions:

1. **Does your agent have durable state surfaces?** Can it resume within 30 seconds after a cold start—or does it start from scratch every time?
2. **Does your system have machine-readable acceptance criteria?** Is the definition of "done" based on the agent's subjective feeling, or on an external, structured verification surface—a feature list, a set of test cases, a checkable pass/fail status?
3. **Are your repo, tools, logs, metrics, and policies legible and enforceable to agents?** Or are they only readable by humans—leaving the agent to guess?

If you have none of these three things, what you've built is likely still just **"a chatbot that can run commands"...**

---

[^1]: Anthropic, *Building Effective Agents*, December 2024
[^2]: Anthropic, *Effective context engineering for AI agents*, 2025
[^3]: Mitchell Hashimoto, *My AI Adoption Journey*, February 5, 2026
[^4]: OpenAI, *Harness Engineering: Leveraging Codex in an Agent-First World*, February 11, 2026
[^5]: Thoughtworks/Fowler, *Harness Engineering - first thoughts*, April 2026
[^6]: Anthropic, *Demystifying evals for AI agents*, 2025
[^7]: Chrome DevTools Protocol (CDP)
[^8]: AIOS: LLM Agent Operating System, 2024
[^9]: ASPLOS 2026 AgenticOS Workshop
[^10]: Invariant Labs, *Tool Poisoning Attacks*, April 2025
