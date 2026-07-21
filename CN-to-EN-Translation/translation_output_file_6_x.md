# Harness Engineering: The Outer Loop of the Agent Era

## Background

Let's start with a prerequisite question: how did we get here?

To understand why Harness Engineering became a seriously discussed engineering practice in 2026, you need to see the full arc that AI engineering has traced over the past four years. That arc is not linear — it's a cycle of capability jumps, old frameworks collapsing, and new abstractions emerging.

**Recommended reading for additional background:**

- AI Operating System: From Instruction to Intent
- From Prompt Engineering to Context Engineering
- The Token Naming Dilemma: When Information Theory Meets Linguistics
- OpenClaw: The Risks Behind the Frenzy
- Deep Dive: Google Workspace CLI
- Meta-Skills: Making AI Think Like You
- Agent Trends: Native and CLI-Oriented
- AI Programming Ecosystem: What Does Anthropic's Acquisition of Bun Mean?
- Deep Thoughts on AI Development Trends
- AI Browsers
- Deep Dive: The Anthropic MCP Protocol

### Act One: Generation (November 2022 – 2023)

On November 30, 2022, ChatGPT went live. It reached roughly 100 million monthly active users in about two months. But what truly changed was not NLP technology — GPT-3 had existed for two years already — but the interaction paradigm. Before this, LLMs were an API that only engineers could use; after this, they became a conversational interface that everyone could use.

The central contradiction of this era: models could generate, but they could not act. They could draft an email but not send it; write code but not run it. The relationship between user and model was "you ask, I answer" — a stateless, single-turn, passive exchange of information.

The engineering product was Prompt Engineering: how to ask questions so the model gives better answers. Few-shot, chain-of-thought, role-playing — all essentially attempts to maximize information density within the limited space of a single API call.

### Act Two: Connection (2023 – 2024)

In March 2023, OpenAI released GPT-4, bringing multimodality and a longer context window. That same month, ChatGPT Plugins launched, giving models "hands" for the first time — the ability to call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool use as structured JSON in model output.

This was a critical turning point: models evolved from "able to speak" to "able to connect." But the Plugins ecosystem quickly exposed its fragility — each plugin required its own OAuth flow, its own schema definition, its own error handling. Connecting ten plugins was already painful; a hundred was impossible.

In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with an intermediary abstraction layer. It did lower the barrier to entry, but at the cost of excessive abstraction — too many wrapper layers, difficult debugging, unpredictable performance. In the same period, projects like AutoGPT and BabyAGI tried to have models autonomously loop through task execution, but both went quiet after their demos due to a lack of reliable stopping conditions and verification mechanisms.

> 🤯 **Lesson One**
>
> Making models "able to connect to tools" is necessary but far from sufficient. Connection does not equal orchestration; orchestration does not equal governance.

### Act Three: Reasoning (2024)

2024 was the year "reasoning models" took the stage. OpenAI's o1 series launched in September with the core feature of "spending more time thinking before answering," achieving a qualitative leap in math and programming tasks. In December, the ARC Prize announced that OpenAI o3 scored 87.5% on the ARC-AGI-1 Semi-Private Eval under its high-compute configuration, stunning the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet excelled in code generation and long-document understanding, and DeepSeek-R1, as an open-weight model, proved that high-performance reasoning was no longer exclusive to closed-source systems.

More important were two developments at the end of 2024:

**First: Anthropic released the Model Context Protocol (MCP).** This was not yet another plugin system, but an open standard protocol using JSON-RPC 2.0 to define how AI applications communicate with external tools and data sources. Its core insight was that the connection problem is fundamentally an N×M problem — N AI applications × M data sources, where each combination requires a custom connector. MCP reduced it to N+M: each application implements an MCP client once, and each tool implements an MCP server once. OpenAI and Google DeepMind subsequently announced MCP support, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

**Second: Anthropic published *Building Effective Agents* [1] (December 2024).** This article was the first to systematically discuss agent engineering patterns — from the simplest prompt chaining to evaluator-optimizer loops — and explicitly articulated a principle: start with the simplest pattern, and only introduce more structure when complexity demonstrably produces better results. This principle later became one of the core guiding philosophies of harness engineering.

By 2025, Anthropic elevated context engineering as a standalone engineering practice in *Effective Context Engineering for AI Agents* [2], emphasizing that the real challenge is no longer just "how to write a prompt," but "what information, in what form, at what moment, to hand to the model at each step." This was the critical transition layer between Prompt Engineering and Harness Engineering — the problem had moved up from "single call" to "per-step context," but had not yet moved up to "the entire task's outer loop."

> 🤯 **Lesson Two**
>
> A model's reasoning ability solves the "single-step quality" problem, but long-task reliability does not automatically follow from smarter individual steps. A model that can win an IMO gold medal will still "forget what it was doing" partway through a four-hour full-stack development task.

### Act Four: Action (2025)

If 2023 was the Chatbot year and 2024 the multimodal year, then 2025 was the Agent year.

At the start of the year, DeepSeek-R1's open-source release forced the market to reassess the model competition landscape. This was followed by a cascade of agent products: Claude Code (a coding agent in the terminal), GitHub Copilot Agent Mode, Cursor's autonomous coding loop, Manus (a browser-operating agent), and OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all major languages. Google released the Agent-to-Agent (A2A) protocol to solve cross-vendor communication between agents.

But the most important discovery of 2025 was not what agents could do, but how they broke down while doing it:

- Agents tried to complete an entire task in a single pass and ran out of context window halfway through.
- Agents declared "all done" after completing 70%, then stopped.
- Multiple agents running in parallel produced cascading errors — a small mistake in one was amplified into something un-debuggable.
- Codebases developed serious "AI slop" after sustained agent work — redundant code, inconsistent naming, stale documentation.

These are not problems of model intelligence. They are problems of system structure.

> 🤯 **Lesson Three**
>
> Agent capabilities have reached the level of "can work autonomously for hours," but the engineering infrastructure around them remains stuck in the "single conversation" era. This fracture is the root cause from which Harness Engineering was born.

### Act Five: Governance (2026 – Present)

At the start of 2026, the industry's attention began shifting from "how to make agents more capable" to "how to keep agents from crashing." The term "Harness Engineering" did not emerge overnight as an invention — rather, it rapidly coalesced and spread starting in February 2026:

- **February 5, 2026:** Mitchell Hashimoto, in *My AI Adoption Journey* [3], explicitly wrote "Engineer the Harness" — this is considered one of the starting points for the term entering mainstream discussion.
- **February 11, 2026:** OpenAI published an engineering article directly titled *Harness Engineering: Leveraging Codex in an Agent-First World* [4]. A small team built an internal beta product from an empty repository in five months, publicly stating "zero lines of hand-written code," with the repository reaching roughly a million lines of code and generating approximately 1,500 PRs. More precisely, the initial scaffold was still generated by Codex with some template guidance; after that, application logic, tests, CI, documentation, observability, and internal tools were produced by agents to the greatest extent possible. The core finding: the engineer's work shifted to **designing environments**, **specifying intent**, and **building feedback loops**.
- **March 2026:** Anthropic published *Harness Design for Long-Running Application Development*, upgrading the earlier initializer/coder two-role architecture to a planner/generator/evaluator three-role system, demonstrating that the evaluator still delivers meaningful gains near the boundary of model capability.
- **April 2026:** The Thoughtworks/Fowler system (*Harness Engineering — First Thoughts* [5]) systematized the concept into a more complete methodological framework — a combination of **guides** (feedforward control) and **sensors** (feedback control), each further divided into **computational** (deterministic) and **inferential** (non-deterministic) types, forming a 2×2 control matrix. Therefore, April is better understood as the point when "the methodological abstraction became complete," rather than the point of "first naming."

---

## What Exactly Is a Harness?

Let's derive this from first principles rather than starting from definitions.

### The Five Fundamental Challenges of Agents

An agent is, by nature, "a system that autonomously advances toward a goal in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone:

1. **State Persistence**
   *Essence:* Agents need to remember what they've done across time and across sessions.
   *Why models can't solve it:* Models are inherently stateless; context windows have upper limits and cannot naturally serve as long-term, continuous state.

2. **Goal Consistency**
   *Essence:* In long tasks, agents tend to drift, self-congratulate, or declare completion prematurely.
   *Why models can't solve it:* Models lack external anchors and cannot stably calibrate what "truly complete" means.

3. **Action Verifiability**
   *Essence:* Every step is probabilistic; "did it" must be distinguished from "did it right."
   *Why models can't solve it:* Models have a natural tendency toward self-congratulation and misjudgment when evaluating their own results.

4. **Entropy Suppression**
   *Essence:* Continuous production inevitably accumulates redundancy, drift, and inconsistency.
   *Why models can't solve it:* Models will copy existing patterns, even when those patterns are themselves bad or low-quality.

5. **Human-Machine Boundary**
   *Essence:* When to be autonomous and when to hand off to humans must be explicitly and engineerically defined.
   *Why models can't solve it:* Models lack reliable "uncertainty self-awareness" and cannot stably judge when they should stop and defer to humans.

The harness is the engineering practice that systematically addresses all five challenges.

### A Precise Definition

Anthropic, in *Demystifying Evals for AI Agents* [6], provided a definition well worth adopting directly: an **agent harness** (or scaffold) is the system that enables a model to act as an agent; it is responsible for handling inputs, orchestrating tool calls, and returning results. More critically, Anthropic further stated: when we evaluate "an agent," what we are actually evaluating is the **model + harness** combination, not the model's standalone capability. This definition is highly significant because it shifts the explanatory unit of agent effectiveness from model parameters to the outer-loop structure in which the model operates.

Here, a concept that is frequently confused must be unpacked: an **agent harness** and an **evaluation harness** are not the same thing. The former is responsible for running the agent (processing input, orchestrating tools, managing state); the latter is responsible for batch-running tasks, recording trajectories, executing graders, and aggregating scores. Many discussions collapse "harness" into one big basket, alternating between runtime orchestration and evaluation pipelines. The Harness Engineering discussed in this article refers to the former — the engineering of **runtime outer-loop systems**.

Based on this, a more precise formulation:

> 📌 The **harness** is the **outer-loop system** that enables a model to act as an Agent.

It encompasses plan decomposition, persistent state, tool orchestration, validation gates, feedback loops, rollback mechanisms, human handoff points, and audit logging. When evaluating an agent's effectiveness, what is being evaluated is not the model itself, but the **model + harness** combination.

Several key points deserve elaboration:

- **"Outer loop" is the key term.** The model's reasoning is the "inner loop" — given context, generate the next step. The harness is the "outer loop" — it decides when to start a new inner loop, what context to give it, how to validate its output, when to roll back, and when to stop. Inner-loop quality depends on model capability; outer-loop quality depends on harness design.
- **The harness is not an upgraded prompt.** A single prompt cannot handle cross-session state, validation gates, tool discovery, failure recovery, and sustained entropy control. Treating the harness as "a longer system prompt" is currently the most common failure mode.
- **The harness is not a framework name.** LangChain is a framework; CrewAI is a framework. Harness Engineering is neither. It is a practice — just as DevOps is not a tool but an engineering culture.

### Three Layers of Engineering Abstraction

**Prompt → Context → Harness**

To understand where the harness sits, you must first see its relationship to the preceding two layers. These three layers are not replacements but progressively deeper levels of abstraction:

> 📌 **Key Insight**
>
> Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline operates." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; but the harness also encompasses multi-step structure, tool mediation, validation gates, and durable state — all of which exceed the scope of single-step context.

---

## The Six Core Engineering Components of the Harness

This section is the most technically dense part of the article. Each component clarifies the problem it solves, the specific approaches of Anthropic/OpenAI, and the underlying design rationale.

### Durable State Surfaces: Ending the Agent's "Amnesia"

**Problem:** The core pain point of long-running agents is like an engineer on a project team reporting for duty with no memory every shift change. Context windows are finite; complex projects cannot be completed within a single window. Agents need a way to bridge the gap between sessions.

**Anthropic's approach:** Rather than trying to build an "infinitely long context," they externalized state into **durable artifacts**:

- The first **initializer agent** sets up the environment: creates `init.sh` (startup script), `claude-progress.txt` (progress log), and the initial git commit (baseline snapshot).
- It generates a **feature list**: expanding high-level requirements into 200+ specific features, all initially marked as failing.
- Each subsequent **coding agent** performs only incremental work, leaving structured updates and a "clean state" when its session ends.
- Key rule: agents can only change a feature's `passes` status — they cannot arbitrarily modify test definitions themselves.

This feature list design may look "crude," but it is remarkably effective — it transforms the definition of "complete" from the agent's subjective feeling into an external, durable, structured, inheritable completion surface. The agent does not need to "remember" what was done before; it just needs to read the feature list and `git diff` to resume within 30 seconds.

Anthropic later discovered an even deeper problem: **context anxiety**. Even with compaction (summarizing and compressing early conversation), agents still degraded in behavior because they *felt* "the context is too full." The solution was not better compaction but **context reset** — giving the next agent a brand-new context and passing all necessary information through externalized state artifacts (rather than conversation history). This is more aggressive than compaction, but it works better.

> 📌 **Design Principle**
>
> State ≠ "saving chat history." True durable state is a structured artifact that an agent can read, understand, and resume from after a cold start, with zero prior context history. If your agent cannot figure out "where it left off and what to do next" within 30 seconds of a cold start, your state management has failed.

### Decomposition & Plans: Cutting Long Tasks Into Pieces the Agent Can Swallow

**Problem:** Tell an agent to "build a clone of claude.ai" and it will try to do everything in a single pass — writing all the code in one session. The result is either a context overflow or a premature declaration of "done" halfway through.

**Evolution:**

- In November 2025, Anthropic initially solved this with an initializer + coder two-role structure. The initializer handled decomposition and initialization; the coder handled incremental implementation.
- In March 2026, this structure was upgraded to a **planner / generator / evaluator** three-role system:
  - **Planner** does not write code directly; instead, it expands one- or two-sentence high-level descriptions into a complete product spec and a step-by-step feature list.
  - **Generator** implements features one by one, committing after each completion.
  - **Evaluator** independently assesses the generator's output, marks pass/fail, and provides specific improvement suggestions.

On OpenAI's side, the equivalents are `PLANS.md`, `Implement.md`, and `Documentation.md` — complex tasks are planned first, execution proceeds by milestones, verification happens at each stage, and documentation is continuously updated as shared memory.

> 📌 **Design Principle**
>
> Plans must be elevated to **first-class artifacts**, not one-off chat content. They need to be written to the file system, version-controlled, readable by downstream agents, and referenced by validation gates. A plan that exists only in a conversation is not a plan — it's a passing thought.

### Feedback Loops: Guides and Sensors

**Problem:** An agent writes code — how do you know if it wrote it correctly? Rely on the agent to evaluate itself? Anthropic explicitly uncovered an embarrassing fact: when asked to evaluate their own work, agents tend to **enthusiastically self-congratulate** — even when quality is clearly mediocre by human standards.

This requires a feedback system that does not depend on the agent's self-evaluation. By April 2026, the community had frameworks that split the harness into a clear **2×2 matrix**:

- **Guides** constrain the agent *before* action, increasing the probability of "getting it right the first time."
- **Sensors** provide signals *after* action, supporting self-correction.

**Key Insight:**

- Guides without sensors → agents encode rules but never know whether the rules actually take effect.
- Sensors without guides → agents repeat the same mistakes and get corrected over and over.
- **Computational** controls are cheap, fast, and deterministic — they can run on every change.
- **Inferential** controls are expensive, slow, and non-deterministic — but they can handle subjective judgments (e.g., "is this UI design too ugly?").

Anthropic's evaluator-optimizer pattern aligns perfectly with this. They also acknowledged a subtle reality: the evaluator is not always necessary — once the base model's capability crosses a certain threshold, the evaluator degrades from "essential component" to "additional overhead." This demonstrates that a good harness is not a fixed template but an **adaptable system that evolves alongside model capability boundaries**.

### Legibility: Building a Perception Surface for Agents

**Problem:** Agents can write code, but can they *see* what happens when that code runs? Can they read error logs? Can they understand performance metrics?

OpenAI, in their harness engineering practice, delivered an extremely sharp judgment: **any knowledge that is not within the agent's runtime visible range might as well not exist.**

This is not rhetoric. They took the following concrete steps to improve legibility:

- Each git worktree gets an independent browser instance, via CDP (Chrome DevTools Protocol [7]), so the agent can "see" the UI.
- Logs, metrics, and traces are all exposed for agent querying.
- **Repository knowledge as the system of record:** design principles, product intent, execution plans, known technical debt, Architecture Decision Records (ADRs) — all placed in the repo and maintained for consistency via lint/CI.
- `AGENTS.md`, structured `docs/`, execution plans, and knowledge documents are placed in the repo as versioned systems of record; but OpenAI also publicly cautioned: overly long `AGENTS.md` files decay quickly, crowd out context, and cause all constraints to lose focus simultaneously — the better approach is to turn it into a directory index, with the actual knowledge scattered across structured documents.

> 📌 **Design Principle**
>
> Legibility is not "making code more elegant." It is about making knowledge, constraints, acceptance criteria, and decision history enter the agent's perception surface. This directly transforms "knowledge management" from a team collaboration problem into an **agent-executability** problem. For agents, institutional knowledge in Slack, oral transmission of architectural boundaries, and constraints scattered across external documentation — if they do not enter the runtime-accessible artifact surface, they might as well not exist.

### Tool Mediation: The More Tools, the More Harness Is Needed

**Problem:** After the MCP ecosystem exploded, a single agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions directly into the context creates severe problems — token costs surge, latency rises, and the agent loses direction in a sea of tools.

Anthropic, in their MCP + Code Execution engineering practice, proposed a core idea: **don't let the model call tools directly; let the model write code to call tools.**

What's the difference?

- **Direct tool-calling mode:** All tool definitions loaded into context → model selects a tool → call executed → result returned to context → model continues. Every step consumes context space; intermediate results circulate within the model.
- **Code execution mode:** Model writes a piece of code → code runs in a sandbox, discovering and calling MCP tools on demand → only the final result is returned to the model. Tool discovery, data filtering, and intermediate processing all happen within the execution environment and never enter the context.

The essence of this idea is: **move tool usage from the model's inner loop to a more efficient external execution loop.** This is precisely harness engineering — it is not a "tool registry," but a system-level design that determines how tools are discovered, when they are exposed, at what granularity, whether results need to enter context, where state lives, and how failures roll back.

### Entropy Control: Garbage Collection for Agents

**Problem:** A fully automated agent codebase will continuously copy existing patterns — even when those patterns are inconsistent, suboptimal, or outright bad. Over time, drift and entropy become inevitable.

OpenAI was the most direct about this: they initially relied on humans spending roughly 20% of each week cleaning up "AI slop" (redundant code, stale documentation, inconsistent naming, copy-pasted dead code). Later, they systematized this cleanup logic:

- **Documentation consistency agents** periodically verify that documentation matches code.
- **Refactor agents** clean up technical debt on a scheduled basis.
- **Architectural enforcement** mechanically maintains module boundaries through CI.

> 📌 **Design Principle**
>
> The harness is responsible not just for "getting the agent running" but also for **continuously suppressing the system noise that agents amplify.** This is its most fundamental distinction from a simple "agent framework" — frameworks care about startup and orchestration; the harness cares about **long-term governability**.

### Harnessability: Not Every System Is Easy to Harness

If you only understand Harness Engineering as "add more rules and loops to the agent," you're not going deep enough. The more fundamental question is: not every system is equally easy to harness.

OpenAI's practice keeps pointing to the same thing: the reason they could push Codex to high throughput was not just that the model was strong enough, but that they **continuously pushed knowledge back into the repo, made plans into artifacts, versioned decisions, and made the environment agent-legible.** How naturally suited a system is to being harnessed by agents is itself a critical variable.

Following this logic, you arrive at a highly explanatory judgment: **systems that are strongly typed, thoroughly tested, clearly bounded, version-documented, and runtime-observable inherently have higher harnessability**; while systems where knowledge lives in people's heads, chat tools, and oral tradition — no matter how strong the model — will first hit the wall of "invisible → incomprehensible → ungovernable."

This means that in the agent era, a team's engineering infrastructure quality (CI maturity, documentation structure, clarity of architectural boundaries) is no longer just a matter of "engineering discipline" — it directly determines how far an agent can go on your system. **Harnessability will become the key dimension for evaluating a system's "agent-readiness."**

---

## The Intent System

A deeper paradigm shift: from instruction-driven to intent-driven

What we discussed above covers the engineering components of the harness. But focusing only on components leads to "patching together technical details." Let's step back and discuss something more fundamental — why Harness Engineering is not just an engineering practice but the product of a paradigm shift.

### Four Ruptures in Human-Machine Interaction

Looking at the entire history of computing, human-machine interaction has undergone four fundamental ruptures:

1. **CLI (Command Line):** Humans must precisely master the machine's language. `ls -la | grep .py` is an instruction — one wrong character in the syntax and it fails. The core assumption of interaction is "humans adapt to machines."
2. **GUI (Graphical Interface):** Machines use visual metaphors to lower the barrier. Folders, desktops, drag-and-drop. The core assumption is "machines present themselves using metaphors humans can understand."
3. **App (Mobile Application):** Logic is crystallized into fixed interfaces. One button per function, one screen per button. The core assumption is "humans select from predefined paths."
4. **Agent (Intent-Driven):** Humans express only goals; the system autonomously plans execution paths. The core assumption is **"the machine understands human intent and autonomously decides how to do it."**

Each rupture is not merely a technology upgrade but a redistribution of control. In the CLI era, humans held 100% control; in the Agent era, humans cede most execution control, retaining only goal-setting and critical decision points.

What is the engineering consequence of this cession?

In an instruction-driven world, a bug means "the system did not correctly execute my instruction" — coverable with traditional testing. In an intent-driven world, bugs become "the system misunderstood my intent" or "the system understood the intent correctly but chose a terrible execution path" — requiring an entirely new set of validation, constraint, and feedback mechanisms, which is precisely what the harness must solve.

### Applications Are Being "CLI-fied" — But Not for Humans

A highly counterintuitive trend: in the Agent era, all applications and websites are being re-"CLI-fied" — not returning users to the terminal, but transforming everything into programmable interfaces from the Agent's perspective.

This is the protocol-level implementation that MCP fundamentally represents. When an Agent needs to operate Google Drive, it does not "open a web page and click buttons" — it needs a set of structured API calls. The MCP server abstracts Google Drive into a set of callable functions: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This means three things:

**First, the object of readability has changed.** Readability used to be for humans — clear UI, sensible information architecture. Now it must first be for agents — structured APIs, machine-parseable documentation, programmable permission models.

**Second, application boundaries are dissolving.** When Agents invoke any tool via MCP and collaborate with other Agents via A2A, Apps degrade from "destinations" to "infrastructure." Users no longer "open an App to do one thing" — they "express an intent, and the Agent orchestrates multiple services to complete it."

**Third, the harness becomes the new "operating system layer."** In the GUI era, operating systems managed windows, files, and processes. The Agent era requires management of: agent lifecycles, tool discovery and authorization, context scheduling and recycling, multi-agent collaboration and isolation, and human approval intervention points.

### From Chatbot to AgentOS

Stringing all these threads together reveals a clear evolutionary path. These three stages are not feature additions — they are fundamental changes in the engineering abstraction layer:

**Level 1: Chatbot (2022–2023)**
Single-turn conversation, stateless, humans fully in the loop. Core value is information retrieval and content generation. Engineering abstraction layer: Prompt Engineering. Representative products: ChatGPT, Claude (early).
*Ceiling:* Able to speak but not to act. Every conversation is isolated.

**Level 2: AI Browser / Agent IDE (2024–2025)**
Multi-step tasks, tool calling, limited autonomy. Core value is task execution and workflow automation. Engineering abstraction layer: Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus, Codex.
*Ceiling:* Individual agents are capable but unstable on long tasks; multi-agent collaboration lacks standards; state management is hand-crafted.

**Level 3: AgentOS (2026–, nascent, forward-looking direction)**
Restraint is warranted here. AgentOS is not yet a converged industry paradigm. But it has genuinely entered the research and systems community agenda. The 2024 AIOS paper [8] proposed extracting scheduling, context management, memory management, and access control from the agent application layer into a kernel-like layer; at ASPLOS 2026, a dedicated AgenticOS Workshop [9] explored OS primitives for agent workloads.

Therefore, the more measured formulation is not "AgentOS has arrived," but: **Harness Engineering is pushing problems from the application layer toward the system layer.** When agents are no longer just a coding assistant but always-on, multi-agent, cross-tool, cross-identity long-running executors, userspace harness will inevitably bump into deeper system-level problems:

- **Agent lifecycle management:** initialization, running, suspension, recovery, termination — not stateless function calls, but full process management.
- **Context scheduling:** The context window is a scarce resource requiring decisions about what information to load, compress, or discard when — this is the agent-version of "memory management."
- **Multi-agent isolation and collaboration:** One agent's operations must not pollute another's environment, yet they need to share certain state — requiring mechanisms analogous to process isolation + IPC.
- **Governance and auditing:** Every agent's every decision must be traceable — in finance, healthcare, and other domains, this is not a nice-to-have but a compliance requirement.

> 📌 **Key Positioning**
>
> The harness is the **userspace layer** of AgentOS. AgentOS is the kernel — it manages scheduling, isolation, and resources. The harness is the userspace shell and daemon — it manages task decomposition, state persistence, validation and feedback, and human-machine handoff. The two are not competitors; they are a natural upper and lower layer.

---

## Five Telltale Symptoms

Theory aside, back to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are still in the ad-hoc phase. Here are five telltale symptoms:

**Symptom 1: Framework Jungle.** LangChain, CrewAI, AutoGen, Agno, n8n… each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to validation to rollback to auditing. Users patch together different frameworks and end up with a fragile pipeline, not a governable system.

**Symptom 2: Chatbot Skin + Agent Engine.** A large number of products are essentially a chatbot interface wrapped around an agent loop — but lack genuine state management, task decomposition, and validation gates. Impressive in demos, frequently crashing in production.

**Symptom 3: Tool Registration ≠ Tool Governance.** MCP makes connection easy, but "able to connect" does not mean "knows how to use." An agent facing 50 tools will get confused, make redundant calls, and take detours. Engineering teams have found that initially giving the agent all available tools produced worse results — trimming to the minimum necessary set is what yielded improvements.

**Symptom 4: One-Off Rules vs. Evolvable Constraints.** Most teams' agent configuration is a giant `AGENTS.md` or system prompt. But practice shows this approach is doomed to fail — when everything is important, nothing is important. The agent matches local patterns rather than navigating intentionally. Rules decay faster than humans can maintain them.

**Symptom 5: Lack of "On-the-Loop" Thinking.** "In the loop" means manually editing artifacts when you're dissatisfied with agent output; "on the loop" means modifying the harness so the system automatically produces better results next time. Most teams are still stuck "in the loop" — fixing errors one by one rather than systematically improving the control loop that produces those errors.

---

## What the Harness Is Not

Clarifying boundaries is as important as clarifying definitions.

**It is not "just a longer system prompt."** Because a single prompt cannot handle cross-session state, validation gates, tool discovery, failure recovery, and sustained entropy control.

**It is not a proprietary term of any single vendor.** Both Anthropic and OpenAI use it publicly, and academic preprints are already abstracting it into a cross-product general concept.

**It is not something that "becomes unnecessary once models get stronger."** Quite the opposite — Anthropic explicitly states that the harness will **redistribute value as the model's boundary shifts outward**: certain checks become redundant, but planning, validation, handoff, and state governance for harder tasks become more important. The stronger the model, the more it needs to place longer, costlier, and more dangerous tasks inside a controlled outer loop.

In practice, the space of interesting harness combinations will not shrink as models get stronger — **it will shift**. Today's effective evaluator may become redundant overhead in the face of the next generation of models, but new capability boundaries will give rise to new harness needs.

---

## Overlooked Critical Issues

### Testability of the Harness

When we say "the harness makes the agent verifiable," the meta-question is: how do you verify the harness itself? If the evaluator uses another LLM — and that LLM also has hallucination tendencies — we have built a "verifying unreliable systems with unreliable systems" loop.

Anthropic's approach is to use **computational sensors** (test suites, linters, type checking) for baseline validation wherever possible, and only enable **inferential sensors** at the level of subjective judgment (UI aesthetics, code style). This is a pragmatic layering strategy, but not a perfect solution.

### Emergent Behavior in Multi-Agent Systems

When ten agents run in parallel, each making independent decisions, the system exhibits emergent behavior that single-agent analysis cannot predict. This is analogous to concurrency bugs in distributed systems — but worse, because every "process" is non-deterministic. Current harness design is primarily aimed at single-agent scenarios; harness principles for multi-agent collaboration have not yet solidified.

### Cost-Latency Engineering Tradeoffs

Every layer of the harness — planner, evaluator, sensor, garbage collection — consumes additional tokens and latency. When the harness's own overhead exceeds the quality improvement it brings, that is over-engineering. How to measure the ROI of the harness, and how to dynamically adjust harness depth based on task complexity, remain unsolved engineering problems.

### A New Dimension of Security: Attack Targets Have Shifted from Data to Agency

This is the layer most articles tend to gloss over but which is in fact the most dangerous. As agents gain persistent state, external tools, and long-term autonomy, the attack surface is no longer just "what the model gets wrong" but "whether the system can be manipulated to act against its intended purpose."

Invariant Labs disclosed Tool Poisoning Attacks [10] in April 2025: malicious instructions can be hidden in MCP tool descriptions — invisible to users but visible to models — thereby inducing agents to execute unauthorized operations. One week later, they demonstrated a data exfiltration scenario leveraging an untrusted MCP server's interaction with a trusted WhatsApp MCP. This means Harness Engineering cannot talk only about throughput and stability; it must also squarely address **tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation**.

MCP's open standardization is important (Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation in December 2025), but the more successful open connectivity becomes, the more it demands stricter governance from the upper harness layer. The harness's permission model must evolve from a static "allowed / not allowed" to a dynamic "under what conditions, up to what limits, and only after human confirmation." In other words, the harness is not just an outer loop that boosts output — it is itself the new security boundary.

---

## Judgments & Outlook

**Judgment 1: Harness Engineering will become one of the foundational disciplines of the AI engineering era.**

Advances in model capability will continue to absorb some micro-level prompt techniques, but will not absorb harness engineering. Because it operates at a higher-level problem: how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents must work across time, tools, environments, and human-machine boundaries, the harness will not disappear — it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

**Judgment 2: The competitive moat is shifting from model quality to harness and system design.**

When GPT, Claude, and Gemini converge in core capabilities, product success will be determined not by model differentiation but by harness quality. The strongest evidence comes from LangChain: holding the underlying model constant and modifying only the harness, they improved deepagents-cli on Terminal Bench 2.0 from 52.8% to 66.5% — a gain of 13.7 points, pulling the ranking from the fringes of the Top 30 into the Top 5. This result cannot be exaggerated into "models no longer matter," but it is sufficient to demonstrate: atop the same model, the harness alone can produce a vast system-level gap. The competitive moat is moving upward to harness and system design.

**Judgment 3: The migration from Chatbot to AgentOS will not happen in a single step.**

There will be a 2–3 year intermediate "AI Browser + lightweight Harness" stage. Most enterprises will first capture value in this stage, then gradually evolve toward a heavier AgentOS architecture. Teams that attempt to jump directly to AgentOS will most likely fail because governance complexity will exceed their capacity to absorb.

**Judgment 4: The engineer's role is shifting from "code producer" to "designer of autonomous systems."**

This is not a layoff warning but a capability upgrade requirement. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing exceptions, distilling rules — the value of these abilities will surge. When dissatisfied with agent output, the low-level approach is to manually edit artifacts; the high-level approach is to modify the harness so the system automatically does better next time. **From in the loop to on the loop — this is the engineer's core upgrade path in the agent era.**

---

## Appendix

**Three self-check questions for practitioners.** Before you start building your own harness, answer these three questions first:

1. **Does your agent have durable state surfaces?** Can it resume within 30 seconds of a cold start — or does it start from scratch every time?
2. **Does your system have machine-readable acceptance criteria?** Is the definition of "complete" the agent's subjective feeling, or an external, structured verification surface — a feature list, a set of test cases, a checkable pass/fail status?
3. **Is your repo, tooling, logs, metrics, and policy legible and enforceable to agents?** Or can only humans read them — with agents left to guess?

If none of these three things are in place, what you're building is most likely still just "a chatbot that happens to run commands"…

---

https://aistudio.xiaomimimo.com/#/share/05fbcd9d5d651be339688aa4e4dc0e47 
