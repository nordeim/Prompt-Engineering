## Background

Let us first address a prerequisite question: How did we get to where we are today?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, one must first see the complete arc that AI engineering has traversed over the past four years. This arc is not linear; it is a series of cycles: **capability leap → old framework collapses → new abstraction emerges**.

Recommended reading for additional background knowledge:

- AI Operating Systems: From Instructions to Intent
- From Prompt Engineering to Context Engineering
- The Token Naming Dilemma: When Information Theory Encounters Linguistics
- OpenClaw: The Hidden Risks Behind the Madness
- Deep Dive: Google Workspace CLI
- Meta-Skills: Making AI Think Like You
- Agent Trends: Native & CLI
- AI Programming Ecosystem: What Does Anthropic's Acquisition of Bun Mean?
- Deep Thoughts on AI Development Trends
- A Brief Discussion on AI Browsers
- Deep Dive: Anthropic's MCP Protocol

---

## Act One: Generation (2022.11 – 2023)

On November 30, 2022, ChatGPT went live. It reached approximately 100 million monthly active users within about two months. But what this event truly changed was not NLP technology — GPT-3 had already existed for two years — but the interaction paradigm. Before this, an LLM was an API that only engineers could use; after this, it became a conversational interface that anyone could use.

The core contradiction in this act was: the model could generate, but it could not act. It could write an email but could not send it; it could write a piece of code but could not run it. The relationship between the user and the model was "you ask, I answer" — a stateless, single-turn, passive exchange of information.

The engineering artifact was Prompt Engineering: how to ask, in order to get the model to answer better. Few-shot, chain-of-thought, role-playing — these were all essentially ways to maximize information density within the limited space of a single API call.

---

## Act Two: Connection (2023 – 2024)

In March 2023, OpenAI released GPT-4, bringing multimodal capabilities and a longer context window. That same month, ChatGPT Plugins were launched, allowing the model to "grow hands" for the first time — it could call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool calls as structured JSON in model output.

This was a critical turning point: the model evolved from "able to speak" to "able to connect." But the Plugins ecosystem quickly exposed its fragility — each plugin required an independent OAuth flow, independent schema definition, and independent error handling. Connecting 10 plugins was already painful; 100 was simply impossible.

In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with a layer of intermediate abstraction. It did lower the barrier to entry, but it also introduced the cost of over-abstraction — too many wrapper layers, difficult debugging, and unpredictable performance. During the same period, projects like AutoGPT and BabyAGI attempted to let models autonomously execute tasks in loops, but both quickly faded after their demos due to the lack of reliable stopping conditions and validation mechanisms.

🤯 **Lesson One**
Letting the model "connect to tools" was necessary, but far from sufficient. Connection does not equal orchestration, and orchestration does not equal governance.

---

## Act Three: Reasoning (2024)

2024 was the year "reasoning models" took the stage. OpenAI's o1 series, released in September, centered on "thinking longer before answering" and achieved a qualitative leap in mathematics and coding tasks. In December, ARC Prize announced that OpenAI o3 achieved 87.5% on the ARC-AGI-1 Semi-Private Eval under the high-compute configuration, stunning the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet performed exceptionally well in code generation and long-document comprehension, and DeepSeek-R1, as an open-weight model, demonstrated that high-performance reasoning was no longer the exclusive domain of closed-source models.

More important were two events at the end of 2024:

**The first:** Anthropic released the Model Context Protocol (MCP). This was not yet another plugin system, but an open standard protocol using JSON-RPC 2.0 to define how AI applications communicate with external tools and data sources. Its core insight was that the connection problem is fundamentally an N×M problem — N AI applications × M data sources, each combination requiring a custom connector. MCP simplified it to N+M: each application implements an MCP client once, and each tool implements an MCP server once. Later, OpenAI and Google DeepMind successively announced support for MCP, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

**The second:** Anthropic published *Building Effective Agents*[1] (December 2024). This article systematically discussed agent engineering patterns for the first time — from the simplest prompt chaining to the evaluator-optimizer loop — and explicitly proposed a principle: start with the simplest pattern, and only introduce more structure when complexity demonstrably yields better results. This principle later became one of the core guiding ideas of Harness Engineering.

By 2025, Anthropic had elevated context engineering as a standalone engineering practice with *Effective Context Engineering for AI Agents*[2], emphasizing that the real challenge was no longer just "how to write a prompt," but "at each step, what information, in what form, at what timing, to give to the model." This was the critical transitional layer between Prompt Engineering and Harness Engineering — the problem had moved up from "single call" to "per-step context," but had not yet moved up to "the entire task's outer loop."

🤯 **Lesson Two**
A model's reasoning ability solves the "single-step quality" problem, but the reliability of long tasks does not automatically improve just because each step is smarter. A model capable of winning an IMO gold medal will still "forget what it was doing" midway through a four-hour full-stack development task.

---

## Act Four: Action (2025)

If 2023 was the Chatbot year and 2024 was the multimodal year, then 2025 was the Agent year.

At the start of the year, the open-source release of DeepSeek-R1 caused the market to re-evaluate the model competition landscape. Then came a cascade of agent products: Claude Code (a terminal-based coding agent), GitHub Copilot Agent Mode, Cursor's autonomous coding loops, Manus (a browser-operating agent), and OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all major languages. Google released the Agent-to-Agent (A2A) protocol to solve cross-vendor communication between agents.

But the most important discovery of 2025 was not what agents could do, but how they broke down while doing it:

- Agents attempted to complete entire tasks in one shot ("going all in") and ran out of the context window halfway through.
- After completing 70%, agents would declare "everything is done" and then stop.
- When multiple agents ran in parallel, they produced cascading errors, and small individual mistakes were amplified to the point of being undebuggable.
- Codebases developed severe "AI slop" after agents worked on them continuously — redundant code, inconsistent naming, and outdated documentation.

These were not problems with the model's intelligence, but with the system's structure.

🤯 **Lesson Three**
Agents' capabilities have reached the level of "being able to work autonomously for hours," but the engineering infrastructure around them is still stuck in the era of "single conversation." This fracture is the root cause from which Harness Engineering was born.

---

## Act Five: Governance (2026 – Present)

At the start of 2026, the industry's attention began shifting from "how to make agents more capable" to "how to keep agents from crashing." "Harness Engineering" as a public term was not suddenly invented one day, but began rapidly coalescing and spreading starting in February 2026:

- **February 5, 2026:** Mitchell Hashimoto explicitly wrote "Engineer the Harness" in *My AI Adoption Journey*[3] — this is considered one of the starting points for the term entering mainstream discussion.
- **February 11, 2026:** OpenAI published an engineering article titled *Harness Engineering: Leveraging Codex in an Agent-First World*[4]. They used a small team to build an internal beta product from an empty repository in five months, with the public statement being "zero lines of hand-written code"; the repository reached approximately a million lines of code in scale, producing about 1,500 PRs. More precisely, the initial scaffold was still generated by Codex under guidance from a small number of templates, after which application logic, tests, CI, documentation, observability, and internal tools were produced as much as possible by agents. The core finding: the engineer's work shifted toward **designing environments**, **specifying intent**, and **building feedback loops**.
- **March 2026:** Anthropic published *Harness Design for Long-Running Application Development*, upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, demonstrating that the evaluator still delivers significant gains near the boundary of model capability.
- **April 2026:** The Thoughtworks/Fowler framework (*Harness Engineering — First Thoughts*[5]) systematized this concept into a more complete methodological framework — a combination of **guides** (feedforward control) and **sensors** (feedback control), each further divided into **computational** (deterministic) and **inferential** (probabilistic) categories, forming a 2×2 control matrix. Thus, April is better understood as the point where "methodological abstraction became complete," rather than the point of "first naming."

---

## What Exactly Is a Harness?

Let us derive this from first principles rather than starting from a definition.

### Five Fundamental Challenges of Agents

An agent is, by its nature, "a system that autonomously advances goals in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone:

**State Persistence**
Essence: An agent needs to remember what it has done across time and across sessions.
Why models cannot solve it: The model itself is stateless, and the context window has an upper limit; it cannot naturally bear long-term continuous state.

**Goal Consistency**
Essence: In long tasks, agents tend to drift, self-indulge, or even declare completion prematurely.
Why models cannot solve it: Models lack external anchors and cannot stably calibrate "what counts as truly completed."

**Action Verifiability**
Essence: Every step is probabilistic; one must distinguish between "did it" and "did it right."
Why models cannot solve it: Models have an inherent tendency toward self-praise and misjudgment when evaluating their own results.

**Entropy Suppression**
Essence: Continuous production constantly accumulates redundancy, drift, and inconsistency.
Why models cannot solve it: Models replicate existing patterns, even when those patterns are themselves bad or low-quality.

**Human-Machine Boundary**
Essence: When to act autonomously and when to hand off to humans must be explicitly and engineering-ly defined.
Why models cannot solve it: Models do not have reliable "uncertainty self-awareness" and cannot stably judge when to stop and return control to humans.

A Harness is the engineering practice that systematically addresses these five challenges.

### A Precise Definition

Anthropic, in *Demystifying Evals for AI Agents*[6], offered a definition well worth adopting directly: an **agent harness** (or scaffold) is the system that enables a model to act as an agent; it handles input processing, orchestrates tool calls, and returns results. More importantly, Anthropic further pointed out: when we evaluate "an agent," what we are actually evaluating is the combination of **model + harness**, not the model's capabilities alone. This definition is critically important because it shifts the unit of explanation for agent effectiveness from model parameters to the outer-loop structure in which the model operates.

Here, a frequently confused concept must be unpacked: an **agent harness** and an **evaluation harness** are not the same thing. The former is responsible for running the agent (processing input, orchestrating tools, managing state); the latter is responsible for batch-running tasks, recording trajectories, executing graders, and aggregating scores. Many discussions conflate "harness" into one big basket, sometimes talking about runtime orchestration, sometimes about evaluation pipelines. The Harness Engineering discussed in this article refers to the former — the engineering of **runtime outer-loop systems**.

Based on this, a more precise formulation:

📌
**Harness = the outer-loop system that enables a model to act as an Agent.**

It includes plan decomposition, persistent state, tool orchestration, verification gating, feedback loops, fallback mechanisms, human-machine handoff points, and audit logs. When evaluating an agent's effectiveness, what is being evaluated is not the model itself, but the **model + harness** combination.

Several points deserve elaboration:

- **Outer loop is the key term.** The model's reasoning is the "inner loop" — given context, generate the next step. The Harness is the "outer loop" — it decides when to start a new inner loop, what context to give it, how to verify its output, when to fall back, and when to stop. The quality of the inner loop depends on model capability; the quality of the outer loop depends on harness design.
- **The Harness is not an upgraded prompt.** A single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control. Treating the Harness as "a longer system prompt" is the most common failure mode today.
- **The Harness is not a framework name.** LangChain is a framework, CrewAI is a framework; Harness Engineering is neither. It is a practice, just as DevOps is not a tool but an engineering culture.

---

## Three Layers of Engineering Abstraction

**Prompt → Context → Harness**

To understand where the Harness sits, one must first see its relationship with the preceding two layers. These three layers are not replacements for each other, but progressively higher levels of abstraction:

📌 **Key Insight**
Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline runs." The former is a subset of the latter. From the user's perspective, harness engineering is essentially a specific form of context engineering; but the harness also encompasses multi-step structure, tool mediation, verification gates, and durable state — these go beyond the scope of single-step context.

---

## Six Engineering Components of the Harness

This section is the most hard-core part of the entire article. Each component explains what problem it solves, the specific approaches taken by Anthropic/OpenAI, and the design principles behind it.

### Durable State Surfaces: Preventing Agents from "Starting a Shift with Amnesia"

**Problem:** The core pain point of long-running agents is like an engineer on a project team completely losing their memory every time they change shifts. The context window is limited; complex projects cannot be completed within a single window; the agent needs a way to bridge the gap between sessions.

**Anthropic's approach:** They did not attempt to create an "infinitely long context." Instead, they externalized state into durable artifacts:

- A first **initializer agent** sets up the environment: creating `init.sh` (a startup script), `claude-progress.txt` (a progress log), and an initial git commit (a baseline snapshot).
- It generates a **feature list**: expanding high-level requirements into 200+ specific features, initially all marked as failing.
- Each subsequent **coding agent** only does incremental work, leaving behind structured updates and a "clean state" when the session ends.
- **Key rule:** The agent can only change a feature's passes status; it cannot arbitrarily modify the test definitions themselves.

This feature list design may look "crude," but it is extremely effective — it transforms the definition of "done" from the agent's subjective feeling into an external, persistent, structured, inheritable completion surface. The agent does not need to "remember" what was done before; it only needs to read the feature list and git diff to resume within 30 seconds.

Anthropic later discovered a deeper problem: **context anxiety**. Even with compaction (summarized compression of earlier conversation), the agent's behavior would still degrade because it "felt" the context was too full. The solution was not better compaction, but **context reset** — giving the next agent a completely fresh context, transmitting all necessary information through externalized state artifacts (rather than conversation history). This is more aggressive than compaction, but the results are better.

📌 **Design Principle**
State ≠ "saving chat history." True durable state is a structured artifact that an agent can cold-start, read, understand, and resume from — without any context history. If your agent cannot know "where it left off and what to do next" within 30 seconds of a cold start, your state management has failed.

### Decomposition & Plans: Cutting Long Tasks into Chunks Agents Can Swallow

**Problem:** Tell an agent to "build a clone of claude.ai," and it will attempt to go all in — writing all the code in a single session. The result is either a context explosion or a premature "I'm done" halfway through.

**Evolution:**

- In November 2025, Anthropic initially solved this with an initializer + coding two-role structure. The initializer handled decomposition and initialization; coding handled step-by-step implementation.
- In March 2026, this structure was upgraded to a **planner / generator / evaluator** three-role system:
  - **Planner** does not write code directly; instead, it expands one or two high-level descriptions into a complete product spec and a step-by-step feature list.
  - **Generator** handles implementing each feature, committing after each one is completed.
  - **Evaluator** independently evaluates the generator's output, marking pass/fail and providing specific improvement suggestions.

OpenAI's counterpart is `PLANS.md`, `Implement.md`, `Documentation.md` — complex tasks are planned first, execution proceeds by milestones, verification is performed at each stage, and documentation is continuously updated as shared memory.

📌 **Design Principle**
Plans must be elevated to first-class artifacts, not one-time chat content. They need to be written into the file system, version-controlled, readable by subsequent agents, and referenced by verification gates. A plan that exists only in a conversation is, by nature, not a plan — it is merely a passing thought.

### Feedback Loops: Guides and Sensors

**Problem:** An agent writes code — how does it know if it wrote it correctly? By having the agent evaluate itself? Anthropic explicitly discovered an embarrassing fact: when asked to evaluate its own work, the agent tends to enthusiastically praise itself — even when, in human judgment, the quality is clearly mediocre.

This requires a feedback system that does not rely on the agent's self-evaluation. By April 2026, community frameworks had decomposed the harness into a very clear 2×2 matrix:

**Guides** constrain the agent before it acts, increasing the probability of "getting it right the first time." **Sensors** provide signals after the agent acts, supporting self-correction.

Key insights:

- Guides without sensors → the agent encodes rules but never knows whether the rules are being followed.
- Sensors without guides → the agent repeatedly makes the same mistakes and then gets corrected.
- **Computational** controls are cheap, fast, deterministic, and can be run on every change.
- **Inferential** controls are expensive, slow, and non-deterministic, but can handle subjective judgments (e.g., "Is this UI design too ugly?").

Anthropic's evaluator-optimizer pattern is fully consistent with this. They also acknowledged a subtle reality: the evaluator is not always necessary — once the base model's capability crosses a certain threshold, the evaluator degrades from a "necessary component" to "overhead." This means a good harness is not a fixed template but a **trimmable system that co-evolves with model capability boundaries**.

### Legibility: Building Perception Surfaces for Agents

**Problem:** An agent can write code, but can it "see" what its code looks like when running? Can it read error logs? Can it understand performance metrics?

OpenAI, in their Harness Engineering practice, delivered an extremely sharp judgment: **any knowledge not within the agent's runtime visible range is equivalent to nonexistent.**

This is not rhetoric. They did the following concrete work to enhance legibility:

- For each git worktree, they launched an independent browser instance, using CDP (Chrome DevTools Protocol[7]) so the agent could "see" the UI.
- Logs, metrics, and traces were all exposed for the agent to query.
- **Repository knowledge as a system of record**: design principles, product intent, execution plans, known technical debt, and architecture decision records (ADRs) were all placed in the repo and maintained for consistency via lint/CI.
- `AGENTS.md`, structured `docs/`, execution plans, and knowledge documents were placed in the repo as much as possible to make them a versioned system of record. However, OpenAI also publicly warned: overly long `AGENTS.md` files rot quickly, crowd out context, and cause all constraints to lose focus simultaneously — a better approach is to turn it into a directory index, with the actual knowledge scattered into structured documents.

📌 **Design Principle**
Legibility does not mean "making code more elegant." It means making knowledge, constraints, acceptance criteria, and decision history enter the agent's perception surface. This directly transforms "knowledge management" from a team collaboration problem into an agent executability problem. For an agent, the experience in Slack, the orally transmitted architectural boundaries, and the constraints scattered across external documents — if these do not enter the runtime-accessible artifact surface — are equivalent to nonexistent.

### Tool Mediation: The More Tools, the More You Need a Harness

**Problem:** After the MCP ecosystem exploded, a single agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions directly into the context produces severe problems — token costs skyrocket, latency increases, and the agent gets lost in a sea of tools.

Anthropic, in their MCP + Code Execution engineering practice, proposed a core idea: **don't let the model call tools directly — let the model write code to call tools.**

What is the difference?

- **Direct tool calling mode:** All tool definitions are loaded into context → model selects a tool → calls it → results are sent back to context → model continues. Every step consumes context space; intermediate results circulate within the model.
- **Code execution mode:** The model writes a piece of code → the code runs in a sandbox, discovering and calling MCP tools as needed → only the final results are sent back to the model. Tool discovery, data filtering, and intermediate processing all happen within the execution environment, not in context.

The essence of this approach is: **moving tool usage from the model's inner loop to a more efficient external execution loop.** This is precisely Harness Engineering — it is not a "tool registry," but a system-level design that determines how tools are discovered, when they are exposed, at what granularity they are exposed, whether results need to enter context, where state is placed, and how failures are rolled back.

### Entropy Control: Continuous Garbage Collection for Agents

**Problem:** Fully autonomous agent codebases continuously replicate existing patterns — even when those patterns are uneven, suboptimal, or outright bad. Over time, drift and entropy increase is inevitable.

OpenAI was most blunt about this: initially, they relied on humans spending approximately 20% of their time each week cleaning up "AI slop" (redundant code, outdated documentation, inconsistent naming, copy-pasted dead code). Later, they systematized this cleanup logic:

- **Documentation consistency agents** periodically verify that documentation matches code.
- **Refactor agents** clean up technical debt on a schedule.
- **Architectural enforcement** mechanically maintains module boundaries through CI.

📌 **Design Principle**
The Harness is not only responsible for "keeping the agent running"; it is also responsible for continuously suppressing the system noise amplified by agents. This is its most fundamental distinction from a simple "agent framework" — frameworks care about startup and orchestration; a harness cares about long-term governability.

### Harnessability: Not Every System Is Easy to Harness

If one understands Harness Engineering only as "adding more rules and loops to agents," the understanding is not deep enough. The more fundamental question is: not every system is equally easy to harness.

OpenAI's practice consistently hints at the same thing: the reason they were able to push Codex to high throughput was not just because the model was strong enough, but because they continuously pushed knowledge back into the repo, turned plans into artifacts, versioned decisions, and made the environment more legible to agents. How naturally suited a system is驯化 by agents is itself an important variable.

Following this logic, one can arrive at a judgment with strong explanatory power: **systems that are strongly typed, thoroughly tested, have clear boundaries, versioned documentation, and runtime-observability naturally have higher harnessability**; whereas systems where knowledge is scattered across people's heads, chat tools, and oral traditions will, regardless of how strong the model is, first hit the wall of "invisible → incomprehensible → ungovernable."

This means that in the agent era, a team's engineering infrastructure quality (CI maturity, documentation structuring, clarity of architectural boundaries) is no longer just an "engineering literacy" issue — it directly determines how far an agent can go on your system. **Harnessability will become the key dimension for evaluating a system's "agent-readiness."**

---

## Intent Systems

A deeper paradigm shift: from instruction-driven to intent-driven.

The above discusses the engineering components of the Harness. But if one only looks at components, one falls into "the patchwork of technical details." Let us step back and discuss something more fundamental — why Harness Engineering is not just an engineering practice, but a product of a paradigm shift.

### Four Fractures in Human-Computer Interaction

Looking at the entire history of computing, the interaction between humans and machines has undergone four fundamental fractures:

- **CLI (command line):** Humans must precisely master the machine's language. `ls -la | grep .py` is an instruction; one wrong character and it fails. The core assumption of interaction is "humans adapt to machines."
- **GUI (graphical interface):** The machine lowers the barrier through visual metaphors. Folders, desktops, drag-and-drop. The core assumption of interaction is "the machine presents itself using metaphors that humans can understand."
- **App (mobile application):** Logic is solidified into fixed interfaces. One button per function, one screen per button. The core assumption of interaction is "humans choose from pre-set paths."
- **Agent (intent-driven):** Humans express only goals; the system autonomously plans the execution path. The core assumption of interaction is **"the machine understands human intent and autonomously decides how to do it."**

Each fracture is not merely a technical upgrade but a redistribution of control. In the CLI era, humans had 100% control; in the Agent era, humans have ceded most execution control, retaining only goal-setting and key decision points.

What is the engineering consequence of this cession?

In the instruction-driven world, a bug is "the system did not correctly execute my instruction" — it can be covered by traditional testing. In the intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent but chose a terrible execution path" — this requires an entirely new set of verification, constraint, and feedback mechanisms, and this is precisely what the Harness is designed to solve.

### Applications Are Being "CLI-ified," but Not for Humans

A very counterintuitive trend: in the Agent era, all applications and websites are being "CLI-ified" again — not to send users back to the terminal, but to turn everything into programmable interfaces from the Agent's perspective.

The essence of MCP is the protocol-layer implementation of this. When an Agent needs to operate Google Drive, it does not need to "open a web page, click buttons" — it needs a set of structured API calls. The MCP server abstracts Google Drive into a set of callable functions: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This means three things:

**First, the object of legibility has changed.** In the past, legibility was for humans — clear UI, rational information architecture. Now, it must first be for Agents — structured APIs, machine-parseable documentation, programmable permission models.

**Second, application boundaries are dissolving.** When an Agent calls any tool via MCP and collaborates with other Agents via A2A, Apps degrade from "destinations" to "infrastructure." Users no longer "open an App to do one thing"; instead, they "express an intent, and the Agent orchestrates multiple services to complete it."

**Third, the Harness becomes the new "operating system layer."** In the GUI era, the operating system managed windows, files, and processes. The Agent era requires managing: Agent lifecycles, tool discovery and authorization, context scheduling and reclamation, multi-agent collaboration and isolation, and human-approval intervention points.

### From Chatbot to AgentOS

Stringing all these threads together reveals a clear evolutionary path. These three stages are not feature accumulations but fundamental changes in engineering abstraction layers:

**Level 1: Chatbot (2022–2023)**
Single conversation, stateless, humans fully in the loop. Core value is information retrieval and content generation. The engineering abstraction layer is Prompt Engineering. Representative products: ChatGPT, Claude (early).

*Ceiling:* Able to speak, unable to act. Every conversation is isolated.

**Level 2: AI Browser / Agent IDE (2024–2025)**
Multi-step tasks, tool calling, limited autonomy. Core value is task execution and workflow automation. The engineering abstraction layer is Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus, Codex.

*Ceiling:* A single agent is capable but unstable on long tasks; multi-agent collaboration lacks standards; state management is manual work.

**Level 3: AgentOS (2026– Nascent stage, forward-looking direction)**

This must be written with restraint. AgentOS is not yet a converged industrial paradigm. But it has indeed entered the research and systems community's agenda. The 2024 AIOS[8] paper proposed extracting scheduling, context management, memory management, and access control from the agent application layer into a kernel-like layer. At ASPLOS 2026, there is a dedicated AgenticOS Workshop[9] exploring OS primitives for agent workloads.

Therefore, the more measured statement is not "AgentOS has arrived," but: **Harness Engineering is pushing the problem from the application layer to the systems layer.** When agents are no longer just a coding assistant but are always-on, multi-agent, cross-tool, cross-identity long-running execution entities, user-space harnesses will inevitably encounter deeper system problems:

- **Agent lifecycle management:** Initialization, running, suspension, resumption, termination — not stateless function calls, but full process management.
- **Context scheduling:** The context window is a scarce resource; decisions must be made about what information to load, when to compress, and when to discard — this is the agent version of "memory management."
- **Multi-agent isolation and collaboration:** One agent's operations should not pollute another's environment, but they also need to share certain state — requiring mechanisms similar to process isolation + IPC.
- **Governance and auditing:** Every decision of every agent at every step must be traceable — in finance, healthcare, and similar domains, this is not a nice-to-have but a compliance requirement.

📌 **Key Positioning**
The Harness is the user-space layer of AgentOS. AgentOS is the kernel — it manages scheduling, isolation, and resources. The Harness is the shell and daemon of user space — it manages task decomposition, state resumption, verification feedback, and human-machine handoff. The two are not competitors but natural upper and lower layers.

---

## Five Telltale Symptoms

Theory is done; back to reality. If you observe the current ecosystem, most so-called "agent systems" are still in a stage of makeshift assembly. Here are five telltale symptoms:

**Symptom One: Framework Jungle.** LangChain, CrewAI, AutoGen, Agno, n8n... each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to verification to fallback to auditing. Users stitch together different frameworks and end up with a fragile pipeline rather than a governable system.

**Symptom Two: Chatbot Skin + Agent Core.** Many products are essentially a chatbot interface wrapped around an agent loop — but lack real state management, task decomposition, and verification gates. They dazzle in demos but frequently crash in production.

**Symptom Three: Tool Registration ≠ Tool Governance.** MCP makes connection easy, but "being able to connect" does not mean "knowing how to use." An agent faced with 50 tools will get confused, make redundant calls, and take detours. Some engineering teams have found that giving the agent all tools initially yielded poor results — only after trimming to the minimal necessary set did performance improve.

**Symptom Four: One-time Rules vs. Evolvable Constraints.** Most teams' agent configuration is a giant `AGENTS.md` or system prompt. But practice shows this approach is doomed to fail — when everything is important, nothing is important. The agent will pattern-match locally rather than navigate intentionally. Rules rot faster than humans can maintain them.

**Symptom Five: Lack of "On-the-Loop" Thinking.** "In the loop" means manually fixing outputs when you are dissatisfied with the agent's results; "on the loop" means modifying the harness so the system automatically produces better results next time. Most teams are still "in the loop" — fixing errors one by one rather than systematically improving the control loops that generate those errors.

---

## What the Harness Is NOT

Clarifying boundaries is as important as clarifying definitions.

**It is not "switching to a longer system prompt."** Because a single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control.

**It is not a proprietary term of any single vendor.** Both Anthropic and OpenAI are using it publicly, and academic preprints are already abstracting it into a cross-product general concept.

**Nor is it "something that will no longer be needed once models get stronger."** Quite the opposite — Anthropic explicitly states that the harness will redistribute value as model boundaries shift outward: certain checks become redundant, but planning, verification, handoff, and state governance for harder tasks become more important. The stronger the model, the more necessary it becomes to place longer, costlier, and riskier tasks within a controlled outer loop.

In practice, the space of interesting harness combinations will not shrink as models get stronger — it will shift. An evaluator effective today may become redundant overhead for the next generation of models, but new capability boundaries will spawn new harness needs.

---

## Overlooked Key Issues

### Testability of the Harness

When we say "the harness makes agents verifiable," a meta-question is: how do we verify the harness itself? If the evaluator uses another LLM, and that LLM also has hallucination tendencies, we have built a loop of "verifying an unreliable system with another unreliable system."

Anthropic's approach is to use **computational sensors** (test suites, linters, type checking) for foundational verification as much as possible, only enabling **inferential sensors** for subjective judgment (UI aesthetics, code style). This is a pragmatic layered strategy, but not a perfect solution.

### Emergent Behavior in Multi-Agent Systems

When 10 agents run in parallel, each making independent decisions, system behavior will exhibit patterns that single-agent analysis cannot predict. This is analogous to concurrency bugs in distributed systems — but worse, because every "process" is non-deterministic. Current harness design primarily targets single-agent scenarios; harness principles for multi-agent collaboration have not yet solidified.

### Engineering Trade-offs of Cost and Latency

Every layer of the harness — planner, evaluator, sensor, garbage collection — consumes additional tokens and introduces latency. When the overhead of the harness itself exceeds the quality improvement it brings, it is over-engineering. How to measure the ROI of the harness and how to dynamically adjust the depth of the harness based on task complexity remain unsolved engineering problems.

### A New Dimension of Security: The Attack Target Has Shifted from Data to Agency

This is the layer that most articles are most likely to gloss over, but it is actually the most dangerous. As agents acquire persistent state, external tools, and long-duration autonomy, the attack surface is no longer just "what the model gets wrong," but "whether the system can be hijacked and manipulated."

Invariant Labs disclosed **Tool Poisoning Attacks**[10] in April 2025: malicious instructions can be hidden in MCP tool descriptions — invisible to the user but visible to the model — thereby inducing the agent to perform unauthorized operations. One week later, they demonstrated a data exfiltration scenario via an untrusted MCP server interacting with a trusted WhatsApp MCP server. This means Harness Engineering cannot only talk about throughput and stability; it must also directly address **tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation**.

The open standardization of MCP is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connections become, the more they demand stricter governance from the upper-layer harness. The harness's permission model must evolve from a static "allowed/not allowed" to a dynamic "allowed under what conditions, up to what limits, and requiring human confirmation before proceeding." In other words, the harness is not just an outer loop that boosts output — it is itself the new security boundary.

---

## Judgments & Outlook

**Judgment One: Harness Engineering will become one of the foundational disciplines of the AI engineering era.**
Model capability improvements will continue to absorb some micro-level prompt techniques, but they will not absorb Harness Engineering. Because it addresses higher-level problems: how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents need to work across time, across tools, across environments, and across human-machine boundaries, the harness will not disappear — it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

**Judgment Two: The center of the moat is shifting from model quality up to Harness and system design.**
When GPT, Claude, and Gemini converge on core capabilities, what determines product success or failure is no longer model differences but harness quality. The hardest evidence comes from LangChain: keeping the underlying model unchanged, they improved deepagents-cli's score on Terminal Bench 2.0 from 52.8% to 66.5% — a gain of 13.7 points — and moved from outside the Top 30 into the Top 5 solely by modifying the harness. This result cannot be exaggerated into "the model no longer matters," but it is sufficient to demonstrate: above the same model, the harness alone can open up an enormous system-level gap. The center of the moat is shifting upward to harness and system design.

**Judgment Three: The migration from Chatbot to AgentOS will not happen in one step.**
There will be an intermediate 2–3 year stage of "AI Browser + lightweight Harness." Most enterprises will first capture value in this stage, then gradually evolve toward the heavier AgentOS architecture. Teams that attempt to jump directly to AgentOS will most likely fail because governance complexity exceeds their capacity to absorb.

**Judgment Four: The engineer's role is shifting from "code producer" to "designer of autonomous systems."**
This is not a layoff warning, but a capability upgrade requirement. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing exceptions, distilling rules — the value of these capabilities will rise sharply. When dissatisfied with agent output, the low-level approach is to manually fix the artifacts; the high-level approach is to modify the harness so the system automatically does better next time. **From "in the loop" to "on the loop" — this is the core upgrade path for engineers in the agent era.**

---

## Appendix

**Three self-check questions for practitioners.** Before you start building your own harness, answer these three questions first:

1. **Does your agent have durable state surfaces?** Can it resume within 30 seconds of a cold start — or does it start from scratch every time?
2. **Does your system have machine-readable acceptance criteria?** Is the definition of "done" the agent's subjective feeling, or an external structured verification surface — a feature list, a set of test cases, a checkable pass/fail status?
3. **Are your repo, tools, logs, metrics, and policies legible and enforceable to agents?** Or can only humans read them — while the agent can only guess?

If the answer to all three is no, what you have built is most likely still just "a chatbot that can run commands"...
