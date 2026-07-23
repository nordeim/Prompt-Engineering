# Background
Let's start with a preliminary question: How did we get here?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, we must first see the complete arc that AI engineering has traversed over the past four years. This arc is not linear—it is a sequence of capability leaps → old frameworks collapsing → new abstractions emerging.

Recommended reading for additional background:

- AI Operating Systems: From Instructions to Intent
- From Prompt Engineering to Context Engineering
- The Token Naming Dilemma: When Information Theory Invades Linguistics
- OpenClaw: The Hidden Risks Behind the Hype
- Deep Dive: Google Workspace CLI
- Meta-Skills: Making AI Think Like You
- Agent Trends: Nativization & CLI-fication
- AI Programming Ecosystem: What Anthropic Acquiring Bun Means
- Deep Thoughts: On AI Development Trends
- A Brief Look at AI Browsers
- Deep Dive: Anthropic MCP Protocol

---

## Act One: Generation (Nov 2022 — 2023)

On November 30, 2022, ChatGPT launched. It reached approximately 100 million monthly active users in about two months. But what truly changed wasn't NLP technology—GPT-3 had already existed for two years—it was the interaction paradigm. Before this, LLMs were APIs that only engineers could use; after this, they became conversational interfaces that everyone could use.

The core tension in this act was: **models could generate, but they couldn't act**. They could write an email, but couldn't send it; could write code, but couldn't run it. The relationship between user and model was "you ask, I answer"—a stateless, single-turn, passive information exchange.

The engineering output was **Prompt Engineering**: how to ask to get better answers from the model. Few-shot, chain-of-thought, role-playing—all essentially aimed at maximizing information density within the limited space of a single API call.

---

## Act Two: Connection (2023 — 2024)

In March 2023, OpenAI released GPT-4, bringing multimodality and longer context windows. That same month, they launched ChatGPT Plugins, giving models "hands" for the first time—they could call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool invocation as structured JSON in model outputs.

This was a critical turning point: models evolved from "being able to speak" to "being able to connect." But the Plugins ecosystem quickly revealed its fragility—each plugin required its own OAuth flow, its own schema definition, its own error handling. Connecting 10 plugins was already painful; 100 was impossible.

In the second half of 2023, LangChain emerged, attempting to solve the "connection" problem with a layer of intermediate abstraction. It did lower the barrier to entry, but also introduced the cost of over-abstraction—too many layers of wrapping, difficult debugging, unpredictable performance. Around the same time, projects like AutoGPT and BabyAGI attempted to have models autonomously execute tasks in loops, but all quickly faded after demos due to a lack of reliable stopping conditions and validation mechanisms.

🤯 **Lesson One**
Making models "able to connect to tools" is necessary, but far from sufficient. Connection ≠ orchestration, and orchestration ≠ governance.

---

## Act Three: Reasoning (2024)

2024 was the year "reasoning models" arrived. OpenAI's o1 series launched in September, featuring "spending more time thinking before answering" as its core characteristic, achieving a qualitative leap in math and programming tasks. In December, the ARC Prize announced that OpenAI's o3 achieved 87.5% on the ARC-AGI-1 Semi-Private Eval with high-compute configuration, shocking the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet excelled at code generation and long-document understanding, and DeepSeek-R1 as an open-weight model proved that high-performance reasoning was no longer a closed-source monopoly.

More importantly, two things happened at the end of 2024:

**First: Anthropic released the Model Context Protocol (MCP).** This was not another plugin system, but an open standard protocol defining how AI applications communicate with external tools and data sources via JSON-RPC 2.0. Its core insight was: the connection problem is essentially an N×M problem—N AI applications × M data sources, each combination requiring a custom connector. MCP reduced it to N+M: each application implements an MCP client once, each tool implements an MCP server once. Later, OpenAI and Google DeepMind successively announced support for MCP, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

**Second: Anthropic released "Building Effective Agents"** [1] (December 2024). This article was the first to systematically discuss agent engineering patterns—from the simplest prompt chaining to evaluator-optimizer loops—and clearly established a principle: start with the simplest pattern, and only introduce more structure when complexity demonstrably delivers better results. This principle later became one of the core guiding philosophies of harness engineering.

By 2025, Anthropic had elevated context engineering to a standalone engineering practice in "Effective context engineering for AI agents"[2], emphasizing that the real difficulty was no longer "how to write prompts," but "at each step, what information, in what form, and at what timing to give to the model." This was the critical transition layer from Prompt Engineering to Harness Engineering—the problem had moved from "single invocation" up to "context per step," but had not yet moved up to "the entire task outer loop."

🤯 **Lesson Two**
The model's reasoning capability addresses the "single-step quality" problem, but the reliability of long-horizon tasks won't automatically improve just because each step is smarter. A model that can solve IMO gold-medal problems will still, in the middle of a four-hour full-stack development task, "forget what it was doing."

---

## Act Four: Action (2025)

If 2023 was the year of Chatbots and 2024 was the year of Multimodality, then 2025 was the year of Agents.

Early in the year, DeepSeek-R1's open-source release forced the market to reassess the competitive landscape of models. This was followed by a wave of agent products: Claude Code (terminal-based programming agent), GitHub Copilot Agent Mode, Cursor's autonomous coding loops, Manus (browser-operation agent), OpenAI Operator. The MCP ecosystem exploded, with thousands of MCP servers built by the community and SDKs covering all major languages. Google released the Agent2Agent (A2A) protocol to address cross-vendor agent communication.

But the most important discovery of 2025 wasn't what agents could do—it was how they broke when doing it:

- Agents tried to complete entire tasks in one go, running out of context window halfway through.
- Agents declared "all done" after completing 70% and stopped.
- Cascading errors occurred when multiple agents ran in parallel; a single small error was amplified to an undebuggable level.
- Codebases developed severe "AI slop" after continuous agent work—redundant code, inconsistent naming, outdated documentation.

These were not intellectual problems of the models, but structural problems of the systems.

🤯 **Lesson Three**
Agent capabilities have reached the level of "can work autonomously for hours," but the engineering infrastructure around them is still stuck in the era of "single-turn conversations." This fracture is the root cause of Harness Engineering's emergence.

---

## Act Five: Governance (2026 — Present)

At the start of 2026, the industry's focus began shifting from "how to make agents more capable" to "how to keep agents from going off the rails." "Harness Engineering" as a public term wasn't invented on a single day, but rather began rapidly coalescing and spreading in February 2026:

- **February 5, 2026:** Mitchell Hashimoto explicitly wrote "Engineer the Harness" in "My AI Adoption Journey"[3]—considered one of the starting points for the term entering mainstream discussion.
- **February 11, 2026:** OpenAI published an engineering article directly titled "Harness Engineering: Leveraging Codex in an Agent-First World"[4]. They detailed how a small team, in five months, built an internal beta product from an empty repository—publicly stated as "zero lines of human-handwritten code," reaching roughly a million lines of code across the repository and generating about 1,500 PRs. More precisely, the initial scaffold was still generated by Codex with a small number of templates as guidance; after that, application logic, tests, CI, documentation, observability, and internal tools were produced by agents as much as possible. Core discovery: engineers' work shifted toward designing environments, specifying intent, and building feedback loops.
- **March 2026:** Anthropic released "Harness Design for Long-Running Application Development," upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, demonstrating that evaluators still provide significant gains near the boundaries of model capabilities.
- **April 2026:** The Thoughtworks / Fowler ecosystem ("Harness Engineering - first thoughts"[5]) systematized the concept into a more complete methodological framework—guides (feedforward control) and sensors (feedback control), each further divided into computational (deterministic) and inferential (probabilistic) categories, forming a 2×2 control matrix. Thus, April is better understood as "the methodological abstraction became complete," rather than "the first naming."

---

## What Exactly Is a Harness?

Let's derive it from first principles, rather than starting from a definition.

### The Five Fundamental Challenges of Agents

An agent is essentially "a system that autonomously pursues goals in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone:

**1. State Persistence**
- **Essence:** Agents need to remember what they've done across time and across sessions.
- **Why models can't solve it:** Models are inherently stateless; context windows have limits; they cannot naturally bear the burden of long-term continuous state.

**2. Goal Alignment**
- **Essence:** In long-horizon tasks, agents easily drift, get distracted, or declare completion prematurely.
- **Why models can't solve it:** Models lack external anchors; they cannot consistently calibrate "what truly counts as done."

**3. Action Verifiability**
- **Essence:** Every step is probabilistic; we need to distinguish between "did" and "did correctly."
- **Why models can't solve it:** Models have an inherent tendency toward self-praise and misjudgment when evaluating their own results.

**4. Entropy Suppression**
- **Essence:** Continuous output continually accumulates redundancy, drift, and inconsistency.
- **Why models can't solve it:** Models copy existing patterns, even when those patterns are themselves bad or low-quality.

**5. Human-AI Boundary**
- **Essence:** When to be autonomous and when to hand off to humans needs to be clearly and engineerably defined.
- **Why models can't solve it:** Models do not have reliable "uncertainty awareness" and cannot consistently judge when to stop and hand back to humans.

Harness is the engineering practice that systematically addresses these five challenges.

### A Precise Definition

Anthropic, in "Demystifying evals for AI agents"[6], gives a definition worth adopting directly: **an agent harness (or scaffold) is the system that enables a model to act as an agent; it handles input processing, orchestrates tool calls, and returns results.** More critically, Anthropic further points out: when we evaluate "an agent," we are actually evaluating the **model + harness** combination, not the model's standalone capability. This definition is crucial because it shifts the unit of explanation for agent performance from model parameters to the outer-loop structure in which the model operates.

A distinction that must be made clear: **agent harness** and **evaluation harness** are not the same thing. The former is responsible for running the agent (processing input, orchestrating tools, managing state); the latter is responsible for batch-running tasks, recording trajectories, executing graders, and aggregating scores. Many discussions lump "harness" into one big bucket, sometimes talking about runtime orchestration and sometimes about evaluation pipelines. This article discusses Harness Engineering as the former—the engineering of the runtime outer-loop system.

Based on this, a more precise formulation:

📌
**Harness = the outer-loop system that enables a model to act as an Agent.**

It includes plan decomposition, persistent state, tool orchestration, validation gates, feedback loops, fallback mechanisms, human-AI handoff points, and audit logs. Evaluating an agent's performance means evaluating the **model + harness** combination, not the model alone.

Several points worth expanding on:

- **"Outer loop" is the key phrase.** The model's reasoning is the "inner loop"—given a context, generate the next step. The harness is the "outer loop"—deciding when to start a new inner loop, what context to give it, how to validate its outputs, when to fall back, when to stop. The quality of the inner loop depends on model capability; the quality of the outer loop depends on harness design.

- **Harness is not an upgraded prompt.** A single prompt cannot solve cross-session state, validation gates, tool discovery, failure recovery, and continuous entropy control. Treating Harness as "a longer system prompt" is the most common failure mode today.

- **Harness is also not a framework name.** LangChain is a framework, CrewAI is a framework; Harness Engineering is not. It is a practice, just as DevOps is not a tool but an engineering culture.

---

## Three Layers of Engineering Abstraction

### Prompt → Context → Harness

To understand Harness's position, we must first see its relationship to the two preceding layers. These three are not replacements but nested abstractions:

📌 **Key Insight**
**Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline operates."** The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; but harness also includes multi-step structure, tool mediation, validation gates, and durable state—things that go beyond single-step context.

---

## The Six Engineering Components of Harness

This section is the most substantive part of the article. Each component will explain what problem it solves, Anthropic/OpenAI's specific approaches, and the design principles behind them.

### 1. Durable State Surfaces: Preventing Agents from "Amnesia on Duty"

**The Problem:** The core pain point for long-running agents is like an engineer on a project team who completely loses memory at every shift change. Context windows are limited; complex projects cannot be completed in a single window. Agents need a way to bridge the gap between sessions.

**Anthropic's Solution:** Instead of trying to build an "infinite context window," they externalize state into resumable artifacts:

- The first initializer agent sets up the environment: creates `init.sh` (startup script), `claude-progress.txt` (progress log), and an initial git commit (baseline snapshot).
- Generates a feature list: expands high-level requirements into 200+ specific features, all initially marked as failing.
- Each subsequent coding agent only makes incremental progress, leaving behind structured updates and a "clean state" at session end.
- Key rule: agents can only change the pass/fail status of features; they cannot arbitrarily modify the test definitions themselves.

This feature list design may seem "crude," but it is extremely effective—it shifts the definition of "done" from the agent's subjective feeling to an external, persistent, structured, and inheritable completion surface. The agent doesn't need to "remember" what it did before; it just needs to read the feature list and git diff to resume within 30 seconds.

Anthropic later discovered a deeper issue: **context anxiety**. Even with compaction (summarizing early conversation content), agents would still degrade in behavior because they felt the context was "too full." The solution wasn't better compaction, but **context reset**—giving the next agent a completely fresh context, passing all necessary information through externalized state artifacts (rather than conversation history). This is more aggressive than compaction, but more effective.

📌 **Design Principle**
State ≠ "saving chat history." True durable state is a structured artifact that an agent can read, understand, and resume from after a cold start, without any context history. If your agent can't know within 30 seconds of a cold start "where we left off and what to do next," your state management is failing.

---

### 2. Decomposition & Plans: Breaking Long Tasks into Agent-Sized Chunks

**The Problem:** Tell an agent to "build a clone of claude.ai" and it will try to do everything in one go—writing all the code in a single session. The result is either context explosion or declaring "done" halfway through.

**Evolution:**

- **November 2025:** Anthropic initially addressed this with an initializer + coding two-role structure. The initializer handled decomposition and initialization; coding handled gradual implementation.
- **March 2026:** This structure was upgraded to a **planner / generator / evaluator** three-role system:
  - **Planner** doesn't write code directly; it expands a high-level description into a complete product spec and step-by-step feature list.
  - **Generator** implements features one by one, committing after each.
  - **Evaluator** independently assesses the generator's output, marking pass/fail and providing specific improvement suggestions.

OpenAI's counterpart is `PLANS.md`, `Implement.md`, `Documentation.md`—complex tasks are planned first, executed by milestone with validation at each stage, and documentation is continuously updated as shared memory.

📌 **Design Principle**
Plans must be promoted to first-class artifacts, not one-off chat content. They need to be written to the file system, version-controlled, readable by subsequent agents, and referenceable by validation gates. A plan that exists only in a conversation is not a plan—it's just a thought.

---

### 3. Feedback Loops: Guides and Sensors

**The Problem:** The agent writes code—how does it know if it's correct? By having the agent evaluate itself? Anthropic explicitly discovered an embarrassing fact: when asked to evaluate its own work, agents tend to enthusiastically praise themselves—even when humans can clearly see the quality is mediocre.

This requires a feedback system that doesn't rely on agent self-evaluation. By April 2026, the community had already framed harness as a clear 2×2 matrix:

**Guides** constrain the agent before it acts, increasing the probability of "getting it right the first time." **Sensors** provide signals after the agent acts, enabling self-correction.

Key insight:
- Only guides, no sensors → agent encodes rules but never knows if they worked.
- Only sensors, no guides → agent repeats the same mistakes and then gets corrected.
- **Computational** control is cheap, fast, deterministic, and can run on every change.
- **Inferential** control is expensive, slow, non-deterministic, but can handle subjective judgments (e.g., "is this UI design too ugly?").

Anthropic's evaluator-optimizer pattern aligns perfectly with this. They also acknowledged a subtle fact: **evaluators are not always necessary**—when the underlying model crosses a certain capability threshold, the evaluator degrades from "necessary component" to "overhead." This shows that a good harness is not a fixed template but an adaptive system that co-evolves with model capability boundaries.

---

### 4. Legibility: Building a Perceptual Surface for Agents

**The Problem:** Agents can write code, but can they "see" what their code looks like when running? Can they read error logs? Can they understand performance metrics?

OpenAI's harness engineering practice offers an extremely sharp judgment: **Any knowledge not within the agent's runtime-visible scope simply does not exist.**

This is not rhetoric. They did the following concrete work to improve legibility:

- Spawned an independent browser instance for each git worktree via CDP (Chrome DevTools Protocol[7]), allowing the agent to "see" the UI.
- Exposed logs, metrics, and traces for agent querying.
- Made repository knowledge the system of record: design principles, product intent, execution plans, known technical debt, Architecture Decision Records (ADRs)—all placed in the repo and kept consistent via lint and CI.
- Placed `AGENTS.md`, structured `docs/`, execution plans, and knowledge documents as much as possible into the repo, making them a versioned system of record. However, OpenAI also publicly cautioned: **overly long `AGENTS.md` files rot quickly, consume context, and cause all constraints to lose focus**—better to treat it as a directory index, with the real knowledge distributed across structured documents.

📌 **Design Principle**
Legibility is not about making code more elegant—it's about making knowledge, constraints, acceptance criteria, and decision history enter the agent's perceptual surface. This directly transforms "knowledge management" from a team collaboration problem into an agent-executable problem. For agents, experience shared in Slack, tacit architectural boundaries, and constraints scattered across external documents—if they are not in a runtime-accessible artifact surface, they do not exist.

---

### 5. Tool Mediation: More Tools = More Need for Harness

**The Problem:** After the MCP ecosystem explosion, an agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions into context causes severe problems—token costs spike, latency increases, and agents get lost in the sea of tools.

Anthropic's core approach in MCP + Code Execution engineering practice: **Don't let the model call tools directly; let the model write code to call tools.**

What's the difference?

**Direct tool-calling mode:** All tool definitions loaded into context → model selects a tool → calls it → results passed back to context → model continues. Each step consumes context space; intermediate results remain in the model's inner loop.

**Code execution mode:** Model writes code → code runs in a sandbox, discovering and calling MCP tools on demand → only the final result is passed back. Tool discovery, data filtering, and intermediate processing all happen within the execution environment, not in the context.

The essence of this approach is: move tool usage from the model's inner loop to a more efficient external execution loop. This is precisely harness engineering—it's not a "tool registry," but a system-level design that determines how tools are discovered, when they're exposed, at what granularity, whether results need to enter the context, where state is stored, and how failures are handled.

---

### 6. Entropy Control: Continuous Garbage Collection for Agents

**The Problem:** Fully autonomous agent codebases continuously replicate existing patterns—even when those patterns are inconsistent, suboptimal, or outright bad. Over time, drift and entropy are inevitable.

OpenAI spoke most directly about this: they initially spent about 20% of a human's time per week cleaning up "AI slop" (redundant code, outdated documentation, inconsistent naming, copy-pasted dead code). Later, they systematized this cleanup logic:

- **Documentation consistency agents** periodically verify that documentation matches the code.
- **Refactor agents** systematically clean up technical debt according to plan.
- **Architectural enforcement** uses CI to mechanistically maintain module boundaries.

📌 **Design Principle**
Harness is not only responsible for "getting the agent running," but also for continuously suppressing the system noise amplified by agents. This is the most essential difference between harness and simple "agent frameworks"—frameworks care about startup and orchestration; harness cares about long-term maintainability.

---

## Harnessability: Not Every System Is Equally Easy to Harness

If we only understand Harness Engineering as "adding more rules and loops to agents," we're still not deep enough. The more fundamental question is: **not every system is equally easy to harness.**

OpenAI's practice consistently hints at the same thing: they were able to push Codex to high throughput not just because the model was strong enough, but because they persistently pushed knowledge back into the repo, artifactized plans, versioned decisions, and made the environment more readable for agents. How naturally suited a system is to being harnessed by agents is itself an important variable.

Following this logic yields a highly explanatory judgment: systems that are strongly typed, well-tested, clearly bounded, document-versioned, and runtime-observable are naturally higher in harnessability; systems where knowledge is scattered across human minds, chat tools, and oral tradition will first hit the wall of "invisible → incomprehensible → ungovernable," no matter how strong the model is.

This means that, in the agent era, a team's engineering infrastructure quality (CI completeness, documentation structure, architectural boundary clarity) is no longer just an "engineering hygiene" issue—it directly determines how far agents can go on your system. **Harnessability will become a key dimension for evaluating a system's "agent-readiness."**

---

## Intent Systems: A Deeper Paradigm Shift — From Instruction-Driven to Intent-Driven

The above covers Harness's engineering components. But if we only look at components, we fall into "assembling technical details." Let's step back and discuss something more fundamental—why Harness Engineering is not just an engineering practice, but a product of a paradigm shift.

### Four Fractures in Human-Computer Interaction

Throughout the entire history of computing, human-machine interaction has undergone four fundamental fractures:

1. **CLI (Command Line):** Humans must precisely master the machine's language. `ls -la | grep .py` is an instruction; a single character typo breaks it. Core assumption: "humans adapt to machines."
2. **GUI (Graphical User Interface):** Machines lower the barrier through visual metaphors—folders, desktops, drag-and-drop. Core assumption: "machines present themselves using metaphors humans understand."
3. **Apps (Mobile Applications):** Logic is solidified into fixed interfaces—one function per button, one screen per button. Core assumption: "humans choose among preset paths."
4. **Agents (Intent-Driven):** Humans only express goals; systems autonomously plan and execute paths. Core assumption: **"machines understand human intent and decide on their own how to achieve it."**

Each fracture is not just a technology upgrade, but a **reallocation of control**. In the CLI era, humans held 100% control. In the Agent era, humans delegate most execution control, retaining only goal-setting and key decision points.

What are the engineering consequences of this delegation?

In an instruction-driven world, a bug is "the system didn't correctly execute my instruction"—it can be covered by traditional testing. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent but chose a terrible execution path"—this requires an entirely new set of validation, constraint, and feedback mechanisms, and that is precisely the problem Harness is designed to solve.

---

## Applications Are Being "CLI-fied"—But Not for Humans

A highly counterintuitive trend: in the Agent era, all applications and websites are being re-"CLI-fied"—not to bring users back to terminals, but to turn everything into programmable interfaces from the agent's perspective.

**MCP is the protocol-layer implementation of this.** When an agent needs to operate Google Drive, it doesn't need to "open a webpage and click buttons"—it needs a set of structured API calls. MCP servers abstract Google Drive into a set of callable functions: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This means three things:

1. **The object of readability has changed.** Readability used to be for humans—clear UI, reasonable information architecture. Now it must first be for agents—structured APIs, machine-parseable documentation, programmable permission models.

2. **Application boundaries are dissolving.** When agents call any tool via MCP and collaborate with other agents via A2A, apps degrade from "destinations" to "infrastructure." Users no longer "open an app to do something," but rather "express an intent, and the agent orchestrates multiple services to complete it."

3. **Harness becomes the new "operating system layer."** The GUI era OS managed windows, files, and processes. The agent era needs to manage: agent lifecycles, tool discovery and authorization, context scheduling and reclamation, multi-agent collaboration and isolation, and human approval intervention points.

---

## From Chatbot to AgentOS

Connecting all the threads above reveals a clear evolutionary path. These three stages are not functional overlays, but fundamental changes in engineering abstraction layers:

**Level 1: Chatbot (2022-2023)**
- Single-turn conversations, stateless, human fully in the loop.
- Core value: information retrieval and content generation.
- Engineering abstraction: Prompt Engineering.
- Representative products: ChatGPT, Claude (early).
- Ceiling: Can speak but cannot act. Every conversation is isolated.

**Level 2: AI Browser / Agent IDE (2024-2025)**
- Multi-step tasks, tool calls, limited autonomy.
- Core value: task execution and workflow automation.
- Engineering abstraction: Context Engineering + lightweight Harness.
- Representative products: Claude Code, Cursor, Manus, Codex.
- Ceiling: Single-agent capabilities are strong but long-horizon tasks are unstable; multi-agent collaboration lacks standards; state management is manual.

**Level 3: AgentOS (2026 — emergent, forward-looking)**
- This must be written with restraint. AgentOS is not yet a converged industrial paradigm. But it has indeed entered the agendas of research and systems communities. The 2024 AIOS[8] paper proposed extracting scheduling, context management, memory management, and access control from the agent application layer into a kernel-like layer; ASPLOS 2026 features a dedicated AgenticOS Workshop[9] exploring OS primitives for agent workloads.

Therefore, a safer statement is not "AgentOS has arrived," but: **Harness Engineering is pushing problems from the application layer toward the system layer.** When agents are no longer just coding assistants, but always-on, multi-agent, cross-tool, cross-identity long-running entities, user-space harness will eventually encounter deeper systemic problems:

- **Agent lifecycle management:** initialization, running, suspension, resumption, termination—not stateless function calls, but complete process management.
- **Context scheduling:** context windows are scarce resources; decisions must be made about what information to load, compress, and discard—this is the agent version of "memory management."
- **Multi-agent isolation and collaboration:** one agent's actions shouldn't pollute another's environment, yet they need to share certain states—requiring mechanism similar to process isolation + IPC.
- **Governance and auditing:** every step of every agent's decisions must be traceable—in finance, healthcare, and other sectors, this is not optional, but a compliance requirement.

📌 **Key Positioning**
**Harness is the user-space layer of AgentOS.** AgentOS is the kernel—managing scheduling, isolation, resources. Harness is the user-space shell and daemon—managing task decomposition, state persistence, validation feedback, and human-agent handoff. They are not competitors but natural upper and lower layers.

---

## Five Typical Symptoms

Enough theory—back to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are still in the temporary ad-hoc stage. Here are five typical symptoms:

**Symptom 1: Framework Jungle.** LangChain, CrewAI, AutoGen, Agno, n8n... each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to validation to rollback to auditing. Users cobble together different frameworks and end up with a fragile pipeline, not a governable system.

**Symptom 2: Chatbot Skin with Agent Core.** Many products are essentially a chatbot interface wrapped around an agent loop—but lacking real state management, task decomposition, and validation gates. They impress in demos but repeatedly fail in production.

**Symptom 3: Tool Registration ≠ Tool Governance.** MCP makes connections easy, but "able to connect" doesn't mean "able to use well." Agents faced with 50 tools get confused, make redundant calls, and take wrong paths. One engineering team found that giving agents access to all available tools initially performed worse—it only improved after trimming to the minimal necessary set.

**Symptom 4: One-Time Rules vs. Evolvable Constraints.** Most teams' agent configurations are a giant `AGENTS.md` or system prompt. But practice shows this approach inevitably fails—when everything is important, nothing is. Agents pattern-match locally instead of navigating consciously. Rules decay faster than humans can maintain them.

**Symptom 5: Lack of On-the-Loop Thinking.** "In the loop" means manually editing artifacts when unsatisfied with agent output; "on the loop" means changing the harness so the system automatically produces better results next time. Most teams remain in the loop—fixing individual errors one by one, rather than systematically improving the control loops that produce the errors.

---

## What Harness Is Not

Clarifying boundaries is as important as clarifying definitions:

- **It is not "a longer system prompt."** A single prompt cannot solve cross-session state, validation gates, tool discovery, failure recovery, and continuous entropy control.
- **It is not a proprietary term of any single vendor.** Anthropic and OpenAI both use it publicly; academic preprints are already abstracting it into a cross-product general concept.
- **It is not "unnecessary once models get stronger."** Quite the opposite—Anthropic explicitly notes that harness will redistribute value as model boundaries shift outward: some checks become redundant, but planning, validation, handoff, and state governance for harder tasks become more important. The stronger the model, the more need to place longer, more expensive, and more dangerous tasks into controlled outer loops.

In fact, the space of **interesting harness combinations** does not shrink as models get stronger—it shifts. An evaluator that works today may become overhead with the next generation of models, but new capability boundaries will create new harness needs.

---

## Overlooked Critical Issues

### Harness Testability
When we say "harness makes agents verifiable," a meta-question is: **how is the harness itself verified?** If the evaluator uses another LLM, and that LLM also has hallucination tendencies, we've built a "verifying unreliable systems with unreliable systems" loop.

Anthropic's approach is to use computational sensors (test suites, linters, type checking) for foundational verification whenever possible, only using inferential sensors for subjective judgments (UI aesthetics, code style). This is a pragmatic layered strategy, but not a perfect solution.

### Emergent Behavior of Multi-Agent Systems
When 10 agents run in parallel, each making independent decisions, system behavior emerges in patterns that cannot be predicted from single-agent analysis. This is similar to concurrent bugs in distributed systems—but worse, because each "process" is non-deterministic. Current harness designs primarily target single-agent scenarios; harness principles for multi-agent collaboration have not yet crystallized.

### Engineering Trade-offs of Cost and Latency
Every layer of the harness—planner, evaluator, sensor, garbage collection—consumes additional tokens and latency. When the harness overhead exceeds the quality improvement it delivers, it's over-engineering. How to measure harness ROI and how to dynamically adjust harness depth based on task complexity are unsolved engineering problems.

### A New Security Dimension: The Attack Target Shifts from Data to Agency
This is the layer many articles gloss over lightly but is actually the most dangerous. As agents acquire persistent state, external tools, and long-term autonomy, the attack surface is no longer just "what did the model answer incorrectly," but "can the system be manipulated via leverage."

In April 2025, Invariant Labs disclosed **Tool Poisoning Attacks**[10]: malicious instructions can be hidden in MCP tool descriptions, invisible to users but visible to models, thereby inducing agents to perform unauthorized operations; a week later, they demonstrated data exfiltration scenarios via untrusted MCP servers chained with trusted WhatsApp MCP. This means Harness Engineering cannot only discuss throughput and stability—it must also directly address tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation.

MCP's open standardization is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connectivity becomes, the more it demands tighter governance from the upper harness layer. The harness permission model must evolve from static "can/cannot" to dynamic "under what conditions, up to what limits, and only after human confirmation." That is, the harness is not just an outer loop for improving output—it is itself a new security boundary.

---

## Judgments & Outlook

**Judgment 1: Harness Engineering will become one of the foundational disciplines of the AI engineering era.**
Model capability improvements will continue to absorb some micro-level prompt techniques, but they will not absorb harness engineering. Because it addresses a higher-level problem: how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents need to work across time, tools, environments, and human-AI boundaries, harness will not disappear—instead, it will increasingly resemble the intersection of software architecture, testing engineering, SRE, and security engineering.

**Judgment 2: The focus of competitive advantage is shifting from model quality to Harness and system design.**
As GPT, Claude, and Gemini converge in core capabilities, what determines product success is no longer model differences, but harness quality. The strongest evidence comes from LangChain: keeping the underlying model unchanged, they improved deepagents-cli from 52.8% to 66.5% on Terminal Bench 2.0—a 13.7-point gain, moving from the periphery of the Top 30 to Top 5—solely through harness modifications. This result cannot be exaggerated as "models are no longer important," but it sufficiently demonstrates: on the same model, harness can create a massive system-level gap. The focus of competitive advantage is shifting upward to harness and system design.

**Judgment 3: The migration from Chatbot to AgentOS will not happen in one step.**
There will be an intermediate "AI Browser + lightweight Harness" phase lasting 2-3 years. Most enterprises will first gain value in this phase, then gradually evolve toward a heavier AgentOS architecture. Teams trying to jump to AgentOS in one step will most likely fail due to governance complexity exceeding their capacity to bear.

**Judgment 4: The engineer's role is shifting from "code producer" to "designer of autonomous systems."**
This is not a job-loss warning, but an upgrade requirement. The value of defining intent, shaping environments, setting boundaries, designing feedback, absorbing exceptions, and solidifying rules will rise sharply. When unsatisfied with agent output, the low-level approach is to manually edit the artifact; the high-level approach is to change the harness so the system automatically does better next time. From in the loop to on the loop—this is the core upgrade path for engineers in the agent era.

---

## Appendix: Three Self-Assessment Questions for Practitioners

Before starting to build your own harness, answer these three questions:

1. **Does your agent have durable state surfaces?** Can it resume within 30 seconds after a cold start—or does it start from scratch every time?

2. **Does your system have machine-readable acceptance criteria?** Is the definition of "done" the agent's subjective feeling, or an externally structured validation surface—a feature list, a test suite, a checkable pass/fail status?

3. **Are your repository, tools, logs, metrics, and policies legible and enforceable to agents?** Or are they only readable by humans—with agents left to guess?

If none of these three are in place, what you're building is most likely still just a "chatbot that can run commands"...

---

## References

[1] Anthropic. "Building Effective Agents." (December 2024)

[2] Anthropic. "Effective context engineering for AI agents." (2025)

[3] Mitchell Hashimoto. "My AI Adoption Journey." (February 5, 2026)

[4] OpenAI. "Harness Engineering: Leveraging Codex in an Agent-First World." (February 11, 2026)

[5] Thoughtworks / Fowler. "Harness Engineering - first thoughts." (April 2026)

[6] Anthropic. "Demystifying evals for AI agents." (2026)

[7] Chrome DevTools Protocol (CDP). https://chromedevtools.github.io/devtools-protocol/

[8] AIOS: LLM Agent Operating System. (2024)

[9] ASPLOS 2026 AgenticOS Workshop. https://agenticos.github.io/

[10] Invariant Labs. "Tool Poisoning Attacks." (April 2025)
