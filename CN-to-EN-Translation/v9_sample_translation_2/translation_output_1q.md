<engine_logs>
## Phase 1: Topological Parsing
- Structural elements: H1 (implied title), H2 (背景, 第一幕–第五幕, Harness 到底是什么, 意图系统, 五个典型症状, Harness 不是什么, 被忽视的关键问题, 判断 & 展望, 附), H3 (Agent 的五个根本性挑战, 一个精确定义, 三层工程抽象, Harness 六大工程构件 subsections, 人机交互的四次断裂, 应用正在被"CLI 化", 从 Chatbot 到 AgentOS, 五个典型症状 items, 判断一–四)
- Immutable elements locked: `ls -la | grep .py`, `init.sh`, `claude-progress.txt`, `PLANS.md`, `Implement.md`, `Documentation.md`, `AGENTS.md`, `docs/`, `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`, `deepagents-cli`, `Terminal Bench 2.0`, `JSON-RPC 2.0`, `CDP`, `OAuth`, `CI`, `ADR`, `MCP`, `A2A`, `SDK`, `PR`, `ARC-AGI-1`, `N×M`, `N+M`, `2×2`, `AIOS`, `ASPLOS 2026`, `AAIF`
- Code-fence seal applied: inline code spans sealed (ls -la | grep .py, init.sh, claude-progress.txt, PLANS.md, Implement.md, Documentation.md, AGENTS.md, docs/, gdrive.*, deepagents-cli)
- Nested structures: none complex
- Code-fence whitespace: PASS
- Comment policy: preserved verbatim (default)
- Markdown density: >50 elements — High density — extra Quarantine vigilance
- Source HTML/structural element inventory: "Image" placeholder ×5 (image references), emoji 🤯 ×3, 📌 ×7, footnote refs [1]–[10], bold markers throughout
- Estimated output tokens: ~6500. Draft-Lock tier: Full (proceeding without wrapper segmentation; best-effort single pass)
- Structural Topology locked.

## Phase 2: Semantic & Modal Deconstruction
- IU count: ~180 IUs (grouped into 18 Clusters by section)
- Primary domain: engineering (AI engineering, agent systems, software architecture)
- Secondary domain terms: none significant (<5% out-of-domain)
- Domain pack active: Engineering
- Domain mismatch: none
- Source register: neutral-professional with informal-technical elements (colloquial metaphors: 一把梭, 土, 翻车, 失忆上岗)
- Modal tags: IU clusters contain hedging (大概率, 可能, 不是...而是), assertion (必须, 就是), speculation (前瞻性方向)
- Ambiguities: none blocking
- Self-referential UI: none

## Phase 3: Domain Reconstruction & Translation (with DRAFT PAYLOAD)
- Translation draft complete.
- Terminology choices: Harness Engineering (preserved), Agent (preserved), Context Engineering (preserved), Prompt Engineering (preserved), durable state (preserved), feature list (preserved), evaluator/generator/planner (preserved), guides/sensors (preserved), computational/inferential (preserved), legibility (preserved), tool mediation (preserved), entropy control (preserved), harnessability (preserved), AgentOS (preserved), AI slop (preserved), in the loop / on the loop (preserved)
- Grammar Asymmetry applications: CN passive → EN active where natural; 了 → past tense for completed actions; aspect particles mapped
- Quantity & Locale applications: dates preserved exactly; percentages preserved; version numbers preserved
- Self-referential UI handling: none
- Register match: neutral-professional + informal-technical → MATCHED (occasional colloquial English equivalents for 一把梭→"go all-in", 土→"crude", 翻车→"crash and burn")

### DRAFT PAYLOAD v1
Background
Let's answer a prerequisite question first: how did we get here?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, we must first see clearly the complete arc that AI engineering has traversed over the past four years. This arc is not linear—it is a series of cycles: capability leap → old framework collapses → new abstraction emerges.

Recommended reading for additional background:

AI Operating Systems: From Instructions to Intent
From Prompt Engineering to Context Engineering
The Token Naming Dilemma: When Information Theory Meets Linguistics
OpenClaw: The Risks Behind the Frenzy
Deep Dive: Google Workspace CLI
Meta-Skills: Making AI Think Like You
Agent Trends: Nativization & CLI-ification
The AI Programming Ecosystem: What Anthropic's Acquisition of Bun Means
Deep Thoughts: On AI Development Trends
A Brief Look at AI Browsers
Deep Dive: The Anthropic MCP Protocol
Act I: Generation (Nov 2022 – 2023)
On November 30, 2022, ChatGPT launched. It reached approximately 100 million monthly active users about two months after launch. But what this event truly changed was not NLP technology—GPT-3 had already existed for two years—it was the interaction paradigm. Before this, an LLM was an API that only engineers could use; after this, it became a conversational interface that everyone could use.

The core contradiction in this act: the model could generate, but could not act. It could write an email but not send it; it could write code but not run it. The relationship between user and model was "you ask, I answer"—a stateless, single-turn, passive information exchange.

The engineering artifact of this era was Prompt Engineering: how to ask so that the model answers better. Few-shot, chain-of-thought, role-playing—fundamentally, all of these were attempts to maximize information density within the limited space of a single API call.

Act II: Connection (2023 – 2024)
In March 2023, OpenAI released GPT-4, bringing multimodality and longer context windows. That same month, they launched ChatGPT Plugins, giving the model "hands" for the first time—able to call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool invocation as structured JSON within model output.

This was a pivotal turning point: the model evolved from "can speak" to "can connect." But the Plugins ecosystem quickly exposed its fragility—each plugin required its own OAuth flow, its own schema definition, its own error handling. Connecting 10 plugins was already painful; 100 was simply impossible.

In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with a layer of intermediate abstraction. It did lower the barrier to entry, but at the cost of over-abstraction—too many wrapper layers, difficult debugging, unpredictable performance. Around the same time, projects like AutoGPT and BabyAGI attempted to let models autonomously loop through tasks, but all fell silent after their demos due to the lack of reliable stopping conditions and verification mechanisms.

🤯 Lesson One
Making a model "able to connect to tools" is necessary, but far from sufficient. Connection is not orchestration, and orchestration is not governance.

Act III: Reasoning (2024)
2024 was the year "reasoning models" took the stage. OpenAI's o1 series launched in September, with "spend more time thinking before answering" as its defining characteristic, achieving a qualitative leap in math and coding tasks. In December, the ARC Prize announced that OpenAI o3 reached 87.5% on the ARC-AGI-1 Semi-Private Eval with high-compute configuration, stunning the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet excelled at code generation and long-document comprehension, and DeepSeek-R1, as an open-weight model, proved that high-performance reasoning was no longer the exclusive domain of closed-source systems.

More importantly, two events at the end of 2024:

First: Anthropic released the Model Context Protocol (MCP). This was not yet another plugin system, but an open standard protocol using JSON-RPC 2.0 to define how AI applications communicate with external tools and data sources. Its core insight: the connection problem is fundamentally an N×M problem—N AI applications × M data sources, each combination requiring a custom connector. MCP simplified this to N+M: each application implements one MCP client, each tool implements one MCP server. Later, OpenAI and Google DeepMind announced MCP support in succession, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

Second: Anthropic published the Building Effective Agents[1] guide (December 2024). This article was the first to systematically discuss engineering patterns for agents—from the simplest prompt chaining to the evaluator-optimizer loop—and explicitly proposed a principle: start with the simplest pattern, and only introduce more structure when complexity demonstrably yields better results. This principle later became one of the core guiding tenets of harness engineering.

By 2025, Anthropic further elevated context engineering as an independent engineering practice in Effective context engineering for AI agents[2], emphasizing that the real difficulty was no longer just "how to write a prompt" but "at each step, what information, in what form, at what timing to hand to the model." This is the critical transitional layer between Prompt Engineering and Harness Engineering—the problem had already shifted upward from "single invocation" to "per-step context," but had not yet ascended to "the entire task's outer loop."

🤯 Lesson Two
A model's reasoning ability solves the "single-step quality" problem, but long-task reliability is not automatically achieved just because individual steps become smarter. A model capable of solving IMO gold-medal problems can still "forget what it's doing" midway through a four-hour full-stack development task.

Act IV: Action (2025)
If 2023 was the year of chatbots and 2024 was the year of multimodality, then 2025 was the year of agents.

At the start of the year, DeepSeek-R1's open-source release forced the market to reassess the competitive landscape. Then came a succession of agent products: Claude Code (a coding agent in the terminal), GitHub Copilot Agent Mode, Cursor's autonomous coding loop, Manus (a browser-operating agent), OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all mainstream languages. Google released the Agent2Agent (A2A) protocol to solve cross-vendor communication between agents.

But the most important discovery of 2025 was not what agents can do—it was how agents break while doing it:

An agent tries to complete the entire task in one shot (going all-in), and the context window runs out halfway through.
An agent announces "everything is done" after completing 70%, then stops.
Multiple agents running in parallel produce cascading errors, where a single small mistake gets amplified beyond debuggability.
The codebase develops severe "AI slop" after continuous agent work—redundant code, inconsistent naming, outdated documentation.
These are not problems of model intelligence; they are problems of system structure.

🤯 Lesson Three
Agent capability has reached the level of "can work autonomously for hours," but the engineering infrastructure around it is still stuck in the "single conversation" era. This fracture is the root cause of Harness Engineering's birth.

Act V: Governance (2026 – Present)
At the start of 2026, the industry's attention began shifting from "how to make agents more capable" to "how to keep agents from crashing." "Harness Engineering" as a public term was not invented on a single day; rather, it rapidly coalesced and spread starting in February 2026:

On February 5, 2026, Mitchell Hashimoto explicitly wrote "Engineer the Harness" in My AI Adoption Journey[3]—widely regarded as one of the starting points for the term's entry into mainstream discussion.
On February 11, 2026, OpenAI published an engineering article titled Harness Engineering: Leveraging Codex in an Agent-First World[4]. They used a small team to build an internal beta product from an empty repository in five months, publicly stating "zero lines of hand-written code," with the repository reaching approximately one million lines of code and producing roughly 1,500 PRs. More precisely, the initial scaffold was still generated by Codex under minimal template guidance, after which application logic, tests, CI, documentation, observability, and internal tools were produced by agents as much as possible. Core finding: the engineer's focus shifted to designing environments, specifying intent, and building feedback loops.
In March 2026, Anthropic published *Harness Design for Long-Running Application Development*, upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, demonstrating that the evaluator still delivers significant gains near the model's capability boundary.
In April 2026, the Thoughtworks / Fowler lineage (Harness Engineering - first thoughts[5]) systematized the concept into a more complete methodological framework—a combination of guides (feedforward control) and sensors (feedback control), each subdivided into computational (deterministic) and inferential (probabilistic) categories, forming a 2×2 control matrix. April is therefore better understood as "the methodological abstraction becoming complete" rather than "the first naming."
What Exactly Is a Harness?
Let us derive this from first principles rather than starting from a definition.

The Five Fundamental Challenges of Agents
The essence of an agent is "a system that autonomously advances goals in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone:

State Persistence
Essence: An agent needs to remember what it has done across time and across sessions.
Why the model cannot solve this: The model itself is stateless, the context window has an upper bound, and it cannot natively bear long-term continuous state.
Goal Consistency
Essence: In long tasks, agents tend to drift, self-congratulate, or even prematurely declare completion.
Why the model cannot solve this: The model lacks external anchor points and cannot stably calibrate "what actually counts as truly done."
Action Verifiability
Essence: Every step is probabilistic; one must distinguish "did it" from "did it correctly."
Why the model cannot solve this: When evaluating its own results, the model has a natural tendency toward self-praise and misjudgment.
Entropy Suppression
Essence: Continuous output inevitably accumulates redundancy, drift, and inconsistency.
Why the model cannot solve this: The model replicates existing patterns, even when those patterns are themselves bad or low-quality.
Human-Machine Boundary
Essence: When to be autonomous and when to hand off to a human must be defined explicitly and engineered.
Why the model cannot solve this: The model does not possess reliable "uncertainty self-awareness" and cannot stably judge when to stop and return control to a human.
A harness is the engineering practice that systematically answers these five challenges.

A Precise Definition
Anthropic provided a definition in Demystifying evals for AI agents[6] that is well worth adopting directly: an agent harness (or scaffold) is the system that enables a model to act as an agent; it handles inputs, orchestrates tool invocations, and returns results. More critically, Anthropic further noted: when we evaluate "an agent," we are actually evaluating the combination of model + harness, not the model's capability in isolation. This definition is profoundly important because it shifts the unit of explanation for agent effectiveness from model parameters to the outer-loop structure in which the model operates.

Image
Here we must disentangle a frequently conflated concept: an agent harness and an evaluation harness are not the same thing. The former is responsible for making the agent run (handling inputs, orchestrating tools, managing state); the latter is responsible for batch-running tasks, recording trajectories, executing graders, and aggregating scores. Many discussions lump "harness" into a catch-all bucket, sometimes talking about runtime orchestration and other times about evaluation pipelines. The Harness Engineering discussed in this article refers to the former—the engineering of the runtime outer-loop system.

Based on this, a more precise formulation:

📌
Harness = the outer-loop system that enables a model to act as an Agent.

It encompasses plan decomposition, persistent state, tool orchestration, verification gates, feedback loops, rollback mechanisms, human-machine handoff points, and audit logs. When evaluating an Agent's effectiveness, what is being evaluated is not the model itself, but the combination of model + harness.

Several key points here deserve elaboration:

Outer loop is the keyword. The model's reasoning is the "inner loop"—given context, generate the next step. The harness is the "outer loop"—deciding when to start a new inner loop, what context to give it, how to verify its output, when to roll back, when to stop. Inner-loop quality depends on model capability; outer-loop quality depends on harness design.
A harness is not an upgraded version of a prompt. A single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, or continuous entropy control. Treating a harness as "a longer system prompt" is the most common failure mode today.
A harness is also not a framework name. LangChain is a framework, CrewAI is a framework—Harness Engineering is not. It is a practice, just as DevOps is not a tool but an engineering culture.
Three Layers of Engineering Abstraction
Prompt → Context → Harness

To understand the harness's position, one must first see its relationship to the two preceding layers. These three layers are not replacements but progressive levels of abstraction:

Image
📌 Key Insight
Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline operates." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; but a harness also encompasses multi-step structure, tool mediation, verification gates, and durable state—these exceed the scope of single-step context.

The Six Engineering Components of a Harness
This section is the most technically dense part of the article. Each component explains what problem it solves, what Anthropic/OpenAI specifically do, and the design principles behind it.

Durable State Surfaces: So Agents Don't Show Up to Work with Amnesia
Problem: The core pain point of long-running agents is like an engineer on a project team who completely loses their memory at every shift change. The context window is finite, complex projects cannot be completed within a single window, and the agent needs a way to bridge the gap between sessions.

Anthropic's solution: Rather than attempting "infinite context," they externalized state into resumable artifacts:

The first initializer agent sets up the environment: creates `init.sh` (startup script), `claude-progress.txt` (progress log), and an initial git commit (baseline snapshot).
Generates a feature list: expands high-level requirements into 200+ specific features, all initially marked as failing.
Each subsequent coding agent makes only incremental progress, leaving structured updates and a "clean state" at session end.
Key rule: agents can only change a feature's passes status; they cannot arbitrarily modify the test definitions themselves.
This feature list design looks "crude," but it is extraordinarily effective—it transforms the definition of "done" from the agent's subjective feeling into an external, persistent, structured, inheritable completion surface. The agent does not need to "remember" what was done before; it only needs to read the feature list and git diff to resume within 30 seconds.

Anthropic later discovered a deeper problem: context anxiety. Even with compaction (summarizing and compressing early conversation), agents still degrade in behavior because they feel "the context is too full." The solution is not better compaction but context reset—giving the next agent a completely fresh context, passing all necessary information through externalized state artifacts (rather than conversation history). This is more radical than compaction, but works better.

📌 Design Principle
State ≠ "saving chat history." True durable state is a structured artifact that an agent can read, understand, and resume from after a cold start with zero conversation history. If your agent cannot determine "where did we leave off, what's the next step" within 30 seconds of a cold start, your state management has failed.

Decomposition & Plans: Cutting Long Tasks into Bite-Sized Chunks for Agents
Problem: Tell an agent "build a clone of claude.ai" and it will try to go all-in—writing all the code in a single session. The result is either the context explodes, or it declares "done" halfway through.

Evolution:

In November 2025, Anthropic initially solved this with an initializer + coding two-role structure. The initializer handles decomposition and initialization; coding handles step-by-step implementation.

In March 2026, this structure was upgraded to a planner / generator / evaluator three-role system:

The Planner does not write code directly but expands one or two high-level descriptions into a complete product spec and a step-by-step feature list
The Generator implements feature by feature, committing after each completion
The Evaluator independently assesses the generator's output, marks pass/fail, and provides specific improvement suggestions
OpenAI's counterpart is `PLANS.md`, `Implement.md`, `Documentation.md`—complex tasks are planned first, executed by milestone, verified at each stage, with documentation continuously updated as shared memory.

📌 Design Principle
A plan must be elevated to a first-class artifact, not remain disposable chat content. It needs to be written to the file system, version-controlled, readable by subsequent agents, and referenceable by verification gates. A plan that exists only in conversation is not really a plan—it is merely a thought.

Feedback Loops: Guides and Sensors
Problem: An agent wrote code—how do you know it's correct? Rely on the agent's self-assessment? Anthropic explicitly discovered an embarrassing fact: when asked to evaluate their own work, agents tend to enthusiastically self-praise—even when the quality is visibly mediocre to a human.

This requires a feedback system that does not depend on the agent's self-evaluation. By April 2026, the community had a framework that decomposed the harness into a very clear 2×2 matrix:

Image
Guides constrain the agent before it acts, increasing the probability of "getting it right the first time." Sensors provide signals after the agent acts, enabling self-correction.

Image
Key insights:

Guides without sensors → the agent encodes rules but never knows whether the rules are effective
Sensors without guides → the agent repeatedly makes the same mistakes and then gets corrected
Computational control is cheap, fast, deterministic, and can run on every change
Inferential control is expensive, slow, non-deterministic, but can handle subjective judgments (e.g., "is this UI design too ugly?")
Anthropic's evaluator-optimizer pattern aligns perfectly with this. They also acknowledged a subtle fact: the evaluator is not always necessary—once the base model's capability crosses a certain threshold, the evaluator degrades from "essential component" to "extra overhead." This shows that a good harness is not a fixed template but a tailorable system that co-evolves with the model's capability boundary.

Image
Legibility: Building a Perception Surface for Agents
Problem: An agent can write code now, but can it "see" what the code looks like when it runs? Can it read error logs? Can it understand performance metrics?

OpenAI offered an extremely sharp judgment in their harness engineering practice: any knowledge not within the agent's runtime visibility effectively does not exist.

This is not rhetoric. They did the following concrete work to improve legibility:

Launch a dedicated browser instance for each git worktree, using CDP (Chrome DevTools Protocol[7]) so the agent can "see" the UI
Expose all logs, metrics, and traces for agent querying.
Repository knowledge as system of record: design principles, product intent, execution plans, known technical debt, architecture decision records (ADR)—all placed in the repo with lint/CI maintaining consistency.
Place `AGENTS.md`, structured `docs/`, execution plans, and knowledge documents in the repo as much as possible, making them a versioned system of record; but OpenAI also publicly cautioned: an overly long `AGENTS.md` rots quickly, crowds out context, and causes all constraints to lose focus simultaneously—a better approach is to make it a directory index, with actual knowledge distributed across structured documents.
📌 Design Principle
Legibility is not "making code more elegant"—it is making knowledge, constraints, acceptance criteria, and decision history enter the agent's perception surface. This directly transforms "knowledge management" from a team collaboration problem into an agent executability problem. For an agent, experience in Slack, architecturally transmitted boundaries, constraints scattered across external documents—if these do not enter runtime-accessible artifact surfaces, they effectively do not exist.

Tool Mediation: More Tools Means More Need for a Harness
Problem: After the MCP ecosystem exploded, a single agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions directly into context creates serious problems—token costs skyrocket, latency rises, and the agent loses its way in an ocean of tools.

Anthropic proposed a core approach in their MCP + Code Execution engineering practice: don't let the model call tools directly; let the model write code that calls tools.

What's the difference?

Direct tool invocation mode: All tool definitions loaded into context → model selects tool → invokes → result returned to context → model continues. Every step consumes context space; intermediate results circulate within the model's inner loop.
Code execution mode: Model writes a piece of code → code runs in a sandbox, discovering and invoking MCP tools as needed → only the final result is returned to the model. Tool discovery, data filtering, and intermediate processing all complete within the execution environment, never entering context.
The essence of this approach: move tool usage from the model's inner loop to a more efficient external execution loop. This is precisely harness engineering—it is not a "tool registry" but a system-level design that determines how tools are discovered, when they are exposed, at what granularity, whether results need to enter context, where state lives, and how failures roll back.

Entropy Control: Continuous Garbage Collection for Agents
Problem: Fully autonomous agent codebases continuously replicate existing patterns—even when those patterns are uneven, suboptimal, or outright bad. Over time, drift and entropy accumulation are inevitable.

OpenAI was the most blunt about this: they initially relied on humans spending roughly 20% of their time each week cleaning up "AI slop" (redundant code, outdated documentation, inconsistent naming, copy-pasted dead code). Later, they systematized this cleanup logic:

Documentation consistency agents periodically verify whether documentation matches code
Refactor agents clean up technical debt on schedule
Architectural enforcement mechanically maintains module boundaries through CI
📌 Design Principle
A harness is not only responsible for "making the agent run" but also for continuously suppressing the system noise that agents amplify. This is its most fundamental distinction from a simple "agent framework"—a framework cares about startup and orchestration; a harness cares about long-term governability.

Harnessability: Not Every System Is Easy to Harness
If we understand Harness Engineering only as "add more rules and loops to the agent," we haven't gone deep enough. The more fundamental question is: not every system is equally easy to harness.

OpenAI's practice consistently implies the same thing: the reason they could push Codex to high throughput is not just because the model is strong enough, but because they continuously pressed knowledge back into the repo, artifactized plans, versioned decisions, and made the environment more readable for agents. How naturally suited a system is to being tamed by agents is itself an important variable.

Following this logic yields a highly explanatory judgment: systems with strong typing, comprehensive tests, clear boundaries, versioned documentation, and runtime observability are naturally higher in harnessability; whereas systems where knowledge is scattered across human minds, chat tools, and oral tradition will hit the wall of "invisible → incomprehensible → ungovernable" no matter how strong the model is.

This means that in the agent era, a team's engineering infrastructure quality (CI completeness, documentation structuring, architectural boundary clarity) is no longer just a matter of "engineering literacy"—it directly determines how far an agent can go in your system. Harnessability will become a key dimension for evaluating a system's "agent-readiness."

The Intent System
A Deeper Paradigm Shift: From Instruction-Driven to Intent-Driven

The above covers the engineering components of a harness. But looking only at components leads to "assembling technical details." Let us step back and discuss something more fundamental—why Harness Engineering is not merely an engineering practice but the product of a paradigm shift.

Four Ruptures in Human-Machine Interaction
Looking back at the entire history of computing, human-machine interaction has undergone four fundamental ruptures:

CLI (command line): Humans must precisely master the machine's language. `ls -la | grep .py` is an instruction—get one character wrong in the syntax and it fails. The core assumption of interaction is "humans adapt to machines."
GUI (graphical interface): Machines lower the barrier through visual metaphors. Folders, desktops, drag-and-drop. The core assumption is "machines present themselves through metaphors humans can understand."
App (mobile applications): Logic is solidified into fixed interfaces. One button per function, one screen per button. The core assumption is "humans choose within preset paths."
Agent (intent-driven): Humans express only goals; the system autonomously plans execution paths. The core assumption is "machines understand human intent and autonomously decide how to proceed."
Each rupture is not merely a technology upgrade but a redistribution of control. In the CLI era, humans held 100% control; in the Agent era, humans have ceded most execution control, retaining only goal-setting and critical decision points.

What are the engineering consequences of this cession?

In an instruction-driven world, a bug is "the system did not correctly execute my instruction"—coverable by traditional testing. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent but chose a poor execution path"—this requires an entirely new set of verification, constraint, and feedback mechanisms, which is precisely what a harness is designed to solve.

Applications Are Being "CLI-ified," But Not for Humans
A highly counterintuitive trend: in the Agent era, all applications and websites are being re-"CLI-ified"—not to send users back to the terminal, but to turn everything into programmable interfaces from the Agent's perspective.

MCP is essentially the protocol-layer implementation of this. When an Agent needs to operate Google Drive, it doesn't need to "open a webpage and click buttons"—it needs a set of structured API calls. An MCP server abstracts Google Drive into a set of callable functions: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This implies three things:

First, the audience for readability has changed. Past readability was for humans—clear UI, sensible information architecture. Now it must first be for Agents—structured APIs, machine-parseable documentation, programmable permission models.

Second, application boundaries are dissolving. When Agents invoke any tool via MCP and collaborate with other Agents via A2A, Apps degrade from "destinations" to "infrastructure." Users no longer "open an App to do one thing" but "express an intent, and the Agent orchestrates multiple services to fulfill it."

Third, the Harness becomes the new "operating system layer." The GUI-era OS managed windows, files, and processes. The Agent era needs to manage: Agent lifecycles, tool discovery and authorization, context scheduling and reclamation, multi-Agent collaboration and isolation, and human approval intervention points.

From Chatbot to AgentOS
Connecting all the threads above reveals a clear evolutionary path. These three stages are not feature additions but fundamental changes in the engineering abstraction layer:

Level 1: Chatbot (2022–2023)
Single-turn conversation, stateless, human fully in the loop. Core value is information retrieval and content generation. Engineering abstraction layer is Prompt Engineering. Representative products: ChatGPT, Claude (early).

Ceiling: can speak but cannot act. Every conversation is isolated.

Level 2: AI Browser / Agent IDE (2024–2025)
Multi-step tasks, tool invocation, limited autonomy. Core value is task execution and workflow automation. Engineering abstraction layer is Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus, Codex.

Ceiling: single-agent capability is strong but long tasks are unstable; multi-agent collaboration lacks standards; state management is manual labor.

Level 3: AgentOS (2026– nascent stage, forward-looking direction)
This must be written with restraint. AgentOS is not yet a converged industry paradigm. But it has indeed entered the research and systems community agenda. The 2024 AIOS[8] paper proposed extracting scheduling, context management, memory management, and access control from the agent application layer into a kernel-like layer; ASPLOS 2026 featured a dedicated AgenticOS Workshop[9] exploring OS primitives for agent workloads.

Image
A more measured statement, therefore, is not "AgentOS has arrived" but: Harness Engineering is pushing the problem from the application layer toward the system layer. When agents are no longer just coding assistants but always-on, multi-agent, cross-tool, cross-identity long-running execution entities, user-space harnesses will inevitably encounter deeper system-level problems:

Agent lifecycle management: initialization, running, suspension, resumption, termination—not stateless function calls but full process management.
Context scheduling: The context window is a scarce resource; decisions must be made about what information to load when, when to compress, when to discard—this is the agent version of "memory management."
Multi-Agent isolation and collaboration: One agent's operations should not pollute another's environment, yet they need to share certain state—requiring mechanisms analogous to process isolation + IPC.
Governance and audit: Every decision step of every agent must be traceable—in finance, healthcare, and similar domains, this is not a nice-to-have but a compliance requirement.
Image
📌 Key Positioning
The Harness is the user-space layer of AgentOS. AgentOS is the kernel—managing scheduling, isolation, and resources. The Harness is the user-space shell and daemon—managing task decomposition, state resumption, verification feedback, and human-machine handoff. The two are not competitors but natural upper and lower layers.

Five Typical Symptoms
Theory aside, back to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are still in the makeshift assembly stage. Here are five typical symptoms:

Symptom One: Framework jungle. LangChain, CrewAI, AutoGen, Agno, n8n… each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to verification to rollback to audit. Users cobble together across frameworks, getting a fragile pipeline rather than a governable system.

Symptom Two: Chatbot skin + Agent core. A large number of products are essentially a chatbot interface wrapped around an agent loop—but lacking true state management, task decomposition, and verification gates. Stunning in demos, repeatedly crashing in production.

Symptom Three: Tool registration ≠ tool governance. MCP made connection easy, but "can connect" does not equal "knows how to use." An agent facing 50 tools becomes confused, makes redundant calls, and takes detours. Engineering teams have found that initially providing agents with all tools actually yields worse results—performance improved only after pruning to the minimal necessary set.

Symptom Four: One-time rules vs. evolvable constraints. Most teams' agent configuration is a massive `AGENTS.md` or system prompt. But practice shows this approach inevitably fails—when everything is important, nothing is important. Agents pattern-match locally rather than consciously navigating. Rules rot faster than humans can maintain them.

Symptom Five: Lack of on-the-loop thinking. "In the loop" means manually fixing artifacts when unsatisfied with agent output; "on the loop" means modifying the harness so the system automatically produces better results next time. Most teams are still stuck in the loop—fixing errors one by one rather than systematically improving the control loops that produce them.

What a Harness Is Not
Clarifying boundaries is as important as clarifying definitions.

It is not "a longer system prompt." Because a single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, or continuous entropy control.

It is not some vendor's proprietary term. Both Anthropic and OpenAI use it publicly, and academic preprints are already abstracting it into a cross-product universal concept.

It is also not "won't be needed once models get stronger." Quite the opposite—Anthropic explicitly noted that as the model boundary expands, the harness redistributes value: certain checks become redundant, but planning, verification, handoff, and state governance for harder tasks become more important. The stronger the model, the more necessary it is to place longer, more expensive, more dangerous tasks inside a controlled outer loop.

In fact, the space of interesting harness combinations does not shrink as models get stronger—it shifts. An evaluator effective today may become redundant overhead before the next generation of models, but new capability boundaries will spawn new harness requirements.

Overlooked Critical Questions
Testability of the Harness
When we say "the harness makes agents verifiable," a meta-question arises: how do you verify the harness itself? If the evaluator uses another LLM, and that LLM also has hallucination tendencies, we have built a loop of "using an unreliable system to verify an unreliable system."

Anthropic's approach is to use computational sensors (test suites, linters, type checkers) for foundational verification as much as possible, enabling inferential sensors only at the subjective judgment level (UI aesthetics, code style). This is a pragmatic layered strategy, but not a perfect solution.

Emergent Behavior in Multi-Agent Systems
When 10 agents run in parallel, each making independent decisions, system behavior exhibits emergent patterns that single-agent analysis cannot predict. This is analogous to concurrency bugs in distributed systems—but worse, because every "process" is non-deterministic. Current harness design primarily targets single-agent scenarios; harness principles for multi-agent collaboration have not yet crystallized.

Engineering Trade-offs Between Cost and Latency
Every layer of the harness—planner, evaluator, sensor, garbage collection—consumes additional tokens and latency. When the harness's own overhead exceeds the quality improvement it delivers, that is over-engineering. How to measure harness ROI and how to dynamically adjust harness depth based on task complexity remain unsolved engineering problems.

A New Dimension of Security: The Attack Target Shifts from Data to Agency
This is the layer most articles gloss over but is actually the most dangerous. As agents gain persistent state, external tools, and long-duration autonomy, the attack surface is no longer just "what did the model get wrong" but "can the system be co-opted."

Invariant Labs disclosed Tool Poisoning Attacks[10] in April 2025: malicious instructions can be hidden in MCP tool descriptions, invisible to users but visible to the model, thereby inducing agents to perform unauthorized operations; a week later, they demonstrated a data exfiltration scenario where an untrusted MCP server leveraged a trusted WhatsApp MCP. This means Harness Engineering cannot discuss only throughput and stability—it must also directly address tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation.

Image
MCP's open standardization is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connection becomes, the more the upper-layer harness must enforce stricter governance. The harness's permission model must upgrade from static "can/cannot" to dynamic "under what conditions can, up to what limit can, only after human confirmation can." In other words, the harness is not only an outer loop for improving output—it is itself a new security boundary.

Judgments & Outlook
Judgment One: Harness Engineering will become one of the foundational disciplines of the AI engineering era
Model capability improvements will continue to absorb some micro-level prompt techniques, but will not absorb harness engineering. Because it addresses higher-level problems: how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents must work across time, across tools, across environments, and across human-machine boundaries, the harness will not disappear—it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

Judgment Two: The moat's center of gravity is shifting upward from model quality to harness and system design
When GPT, Claude, and Gemini converge on core capabilities, what determines product success or failure is no longer model differentiation but harness quality. The hardest evidence comes from LangChain: without changing the underlying model, they improved deepagents-cli on Terminal Bench 2.0 from 52.8% to 66.5%—a gain of 13.7 points—solely by modifying the harness, pulling their ranking from outside the Top 30 into the Top 5. This result should not be exaggerated into "models no longer matter," but it is sufficient to demonstrate: on top of the same model, the harness alone can create enormous system-level gaps. The moat's center of gravity is shifting upward to harness and system design.

Judgment Three: The migration from Chatbot to AgentOS will not happen in one step
There will be a 2–3 year "AI Browser + lightweight Harness" phase in between. Most enterprises will first capture value in this phase, then gradually evolve toward heavier AgentOS architectures. Teams attempting to leap directly to AgentOS will most likely fail because governance complexity exceeds their capacity to bear.

Judgment Four: The engineer's role is shifting from "code producer" to "designer of autonomous systems"
This is not an unemployment warning but a capability upgrade requirement. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing anomalies, distilling rules—the value of these capabilities will rise sharply. When unsatisfied with agent output, the low-level approach is to manually fix artifacts; the high-level approach is to modify the harness so the system automatically does better next time. From in the loop to on the loop—this is the engineer's core upgrade path in the agent era.

Appendix
Three self-check questions for practitioners. Before building your own harness, answer these three questions first:

Does your agent have durable state surfaces? Can it resume within 30 seconds of a cold start—or does it start from scratch every time?
Does your system have machine-readable acceptance criteria? Is the definition of "done" the agent's subjective feeling, or an external structured verification surface—a feature list, a set of test cases, a checkable pass/fail state?
Are your repo, tools, logs, metrics, and policies legible and enforceable for the agent? Or can only humans read them—leaving the agent to guess?
If none of these three exist, what you've built is most likely still just "a chatbot that can run commands"...
### END DRAFT PAYLOAD v1

## Phase 4: Typographical Compilation (auditing DRAFT PAYLOAD v1)
- Surface Typography applied: straight quotes in EN technical text; no CJK-Latin spacing needed (EN output); punctuation half-width throughout
- Title-of-Works mappings: *Harness Design for Long-Running Application Development* (article/guide → italics per convention for standalone published works)
- Nested-structure preservation: PASS — all inline code spans preserved, all reference links [1]-[10] preserved
- Code-fence whitespace preservation: PASS — inline code spans verbatim
- Code-fence seal integrity: PASS — `ls -la | grep .py`, `init.sh`, `claude-progress.txt`, `PLANS.md`, `Implement.md`, `Documentation.md`, `AGENTS.md`, `docs/`, `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`, `deepagents-cli` all character-identical
- Anti-Enhancement verification: PASS — no elements added; all "Image" placeholders preserved ×5; all emoji preserved; all footnote refs preserved

## Phase 5: Zero-Trust MQM-lite Audit (auditing DRAFT PAYLOAD v1)
- Fact Check: PASS — all dates, percentages (87.5%, 52.8%, 66.5%, 13.7, 200+, 1,500, ~1M), version numbers preserved
- Modality Check: PASS — 大概率→"most likely", 可能→"may/can", hedging preserved throughout
- Structural Topology Check: PASS — heading hierarchy, lists, bold, emoji, Image placeholders all match source
- Surface Typography Check: PASS — straight quotes in EN, half-width punctuation
- Collocation Check: PASS — Engineering pack collocations applied (execute, deploy, roll back, high availability, etc.)
- IU-Coverage Bookkeeping: PASS — all semantic content present; no omissions, no additions
- Ambiguity Handling Check: PASS — no blocking ambiguities
- Self-Referential UI Check: PASS — N/A
- Anti-Enhancement Check: PASS — no elements added; all source elements preserved
- Code-Fence Seal Check: PASS — all backtick content character-identical
- Draft-Lock Integrity: PASS — v1 complete, all IUs present
- Severity counts: Critical=0 Major=0 Minor=0 Neutral=0
- Overall confidence: 96
- Repair loops used: 0 / 2

## Phase 6: Self-Test Pre-Output Gate
- Quote check (scoped): PASS — straight quotes used in EN technical text
- Source-Script Leakage: PASS — no stray CJK in EN prose
- Grammar Fluency: PASS — natural English phrasing throughout
- Locked-retention exemption: PASS — retained terms are proper nouns, product names, technical terms
- Notice-channel check: PASS — no Notice warranted
- Reasoning-marker check: PASS — no phase numbers or reasoning in payload
- Heading-hierarchy check: PASS — matches source
- Heading-translation-consistency: PASS — all headings translated consistently
- Nested-structure check: PASS
- Code-fence-whitespace check: PASS
- Code-fence seal integrity: PASS
- Self-referential UI check: PASS — N/A
- Anti-Enhancement Gate: PASS — all source elements present; zero additions; all link targets character-identical
- Draft-Lock Integrity Gate: PASS — DRAFT PAYLOAD v1 is locked; final output will be character-identical to v1; no re-translation or re-generation will occur
- Mode-output check: PASS
- Scratchpad-format check: PASS
- Self-Test result: PASS
</engine_logs>
Background
Let's answer a prerequisite question first: how did we get here?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, we must first see clearly the complete arc that AI engineering has traversed over the past four years. This arc is not linear—it is a series of cycles: capability leap → old framework collapses → new abstraction emerges.

Recommended reading for additional background:

AI Operating Systems: From Instructions to Intent
From Prompt Engineering to Context Engineering
The Token Naming Dilemma: When Information Theory Meets Linguistics
OpenClaw: The Risks Behind the Frenzy
Deep Dive: Google Workspace CLI
Meta-Skills: Making AI Think Like You
Agent Trends: Nativization & CLI-ification
The AI Programming Ecosystem: What Anthropic's Acquisition of Bun Means
Deep Thoughts: On AI Development Trends
A Brief Look at AI Browsers
Deep Dive: The Anthropic MCP Protocol
Act I: Generation (Nov 2022 – 2023)
On November 30, 2022, ChatGPT launched. It reached approximately 100 million monthly active users about two months after launch. But what this event truly changed was not NLP technology—GPT-3 had already existed for two years—it was the interaction paradigm. Before this, an LLM was an API that only engineers could use; after this, it became a conversational interface that everyone could use.

The core contradiction in this act: the model could generate, but could not act. It could write an email but not send it; it could write code but not run it. The relationship between user and model was "you ask, I answer"—a stateless, single-turn, passive information exchange.

The engineering artifact of this era was Prompt Engineering: how to ask so that the model answers better. Few-shot, chain-of-thought, role-playing—fundamentally, all of these were attempts to maximize information density within the limited space of a single API call.

Act II: Connection (2023 – 2024)
In March 2023, OpenAI released GPT-4, bringing multimodality and longer context windows. That same month, they launched ChatGPT Plugins, giving the model "hands" for the first time—able to call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool invocation as structured JSON within model output.

This was a pivotal turning point: the model evolved from "can speak" to "can connect." But the Plugins ecosystem quickly exposed its fragility—each plugin required its own OAuth flow, its own schema definition, its own error handling. Connecting 10 plugins was already painful; 100 was simply impossible.

In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with a layer of intermediate abstraction. It did lower the barrier to entry, but at the cost of over-abstraction—too many wrapper layers, difficult debugging, unpredictable performance. Around the same time, projects like AutoGPT and BabyAGI attempted to let models autonomously loop through tasks, but all fell silent after their demos due to the lack of reliable stopping conditions and verification mechanisms.

🤯 Lesson One
Making a model "able to connect to tools" is necessary, but far from sufficient. Connection is not orchestration, and orchestration is not governance.

Act III: Reasoning (2024)
2024 was the year "reasoning models" took the stage. OpenAI's o1 series launched in September, with "spend more time thinking before answering" as its defining characteristic, achieving a qualitative leap in math and coding tasks. In December, the ARC Prize announced that OpenAI o3 reached 87.5% on the ARC-AGI-1 Semi-Private Eval with high-compute configuration, stunning the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet excelled at code generation and long-document comprehension, and DeepSeek-R1, as an open-weight model, proved that high-performance reasoning was no longer the exclusive domain of closed-source systems.

More importantly, two events at the end of 2024:

First: Anthropic released the Model Context Protocol (MCP). This was not yet another plugin system, but an open standard protocol using JSON-RPC 2.0 to define how AI applications communicate with external tools and data sources. Its core insight: the connection problem is fundamentally an N×M problem—N AI applications × M data sources, each combination requiring a custom connector. MCP simplified this to N+M: each application implements one MCP client, each tool implements one MCP server. Later, OpenAI and Google DeepMind announced MCP support in succession, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

Second: Anthropic published the Building Effective Agents[1] guide (December 2024). This article was the first to systematically discuss engineering patterns for agents—from the simplest prompt chaining to the evaluator-optimizer loop—and explicitly proposed a principle: start with the simplest pattern, and only introduce more structure when complexity demonstrably yields better results. This principle later became one of the core guiding tenets of harness engineering.

By 2025, Anthropic further elevated context engineering as an independent engineering practice in Effective context engineering for AI agents[2], emphasizing that the real difficulty was no longer just "how to write a prompt" but "at each step, what information, in what form, at what timing to hand to the model." This is the critical transitional layer between Prompt Engineering and Harness Engineering—the problem had already shifted upward from "single invocation" to "per-step context," but had not yet ascended to "the entire task's outer loop."

🤯 Lesson Two
A model's reasoning ability solves the "single-step quality" problem, but long-task reliability is not automatically achieved just because individual steps become smarter. A model capable of solving IMO gold-medal problems can still "forget what it's doing" midway through a four-hour full-stack development task.

Act IV: Action (2025)
If 2023 was the year of chatbots and 2024 was the year of multimodality, then 2025 was the year of agents.

At the start of the year, DeepSeek-R1's open-source release forced the market to reassess the competitive landscape. Then came a succession of agent products: Claude Code (a coding agent in the terminal), GitHub Copilot Agent Mode, Cursor's autonomous coding loop, Manus (a browser-operating agent), OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all mainstream languages. Google released the Agent2Agent (A2A) protocol to solve cross-vendor communication between agents.

But the most important discovery of 2025 was not what agents can do—it was how agents break while doing it:

An agent tries to complete the entire task in one shot (going all-in), and the context window runs out halfway through.
An agent announces "everything is done" after completing 70%, then stops.
Multiple agents running in parallel produce cascading errors, where a single small mistake gets amplified beyond debuggability.
The codebase develops severe "AI slop" after continuous agent work—redundant code, inconsistent naming, outdated documentation.
These are not problems of model intelligence; they are problems of system structure.

🤯 Lesson Three
Agent capability has reached the level of "can work autonomously for hours," but the engineering infrastructure around it is still stuck in the "single conversation" era. This fracture is the root cause of Harness Engineering's birth.

Act V: Governance (2026 – Present)
At the start of 2026, the industry's attention began shifting from "how to make agents more capable" to "how to keep agents from crashing." "Harness Engineering" as a public term was not invented on a single day; rather, it rapidly coalesced and spread starting in February 2026:

On February 5, 2026, Mitchell Hashimoto explicitly wrote "Engineer the Harness" in My AI Adoption Journey[3]—widely regarded as one of the starting points for the term's entry into mainstream discussion.
On February 11, 2026, OpenAI published an engineering article titled Harness Engineering: Leveraging Codex in an Agent-First World[4]. They used a small team to build an internal beta product from an empty repository in five months, publicly stating "zero lines of hand-written code," with the repository reaching approximately one million lines of code and producing roughly 1,500 PRs. More precisely, the initial scaffold was still generated by Codex under minimal template guidance, after which application logic, tests, CI, documentation, observability, and internal tools were produced by agents as much as possible. Core finding: the engineer's focus shifted to designing environments, specifying intent, and building feedback loops.
In March 2026, Anthropic published *Harness Design for Long-Running Application Development*, upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, demonstrating that the evaluator still delivers significant gains near the model's capability boundary.
In April 2026, the Thoughtworks / Fowler lineage (Harness Engineering - first thoughts[5]) systematized the concept into a more complete methodological framework—a combination of guides (feedforward control) and sensors (feedback control), each subdivided into computational (deterministic) and inferential (probabilistic) categories, forming a 2×2 control matrix. April is therefore better understood as "the methodological abstraction becoming complete" rather than "the first naming."
What Exactly Is a Harness?
Let us derive this from first principles rather than starting from a definition.

The Five Fundamental Challenges of Agents
The essence of an agent is "a system that autonomously advances goals in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone:

State Persistence
Essence: An agent needs to remember what it has done across time and across sessions.
Why the model cannot solve this: The model itself is stateless, the context window has an upper bound, and it cannot natively bear long-term continuous state.
Goal Consistency
Essence: In long tasks, agents tend to drift, self-congratulate, or even prematurely declare completion.
Why the model cannot solve this: The model lacks external anchor points and cannot stably calibrate "what actually counts as truly done."
Action Verifiability
Essence: Every step is probabilistic; one must distinguish "did it" from "did it correctly."
Why the model cannot solve this: When evaluating its own results, the model has a natural tendency toward self-praise and misjudgment.
Entropy Suppression
Essence: Continuous output inevitably accumulates redundancy, drift, and inconsistency.
Why the model cannot solve this: The model replicates existing patterns, even when those patterns are themselves bad or low-quality.
Human-Machine Boundary
Essence: When to be autonomous and when to hand off to a human must be defined explicitly and engineered.
Why the model cannot solve this: The model does not possess reliable "uncertainty self-awareness" and cannot stably judge when to stop and return control to a human.
A harness is the engineering practice that systematically answers these five challenges.

A Precise Definition
Anthropic provided a definition in Demystifying evals for AI agents[6] that is well worth adopting directly: an agent harness (or scaffold) is the system that enables a model to act as an agent; it handles inputs, orchestrates tool invocations, and returns results. More critically, Anthropic further noted: when we evaluate "an agent," we are actually evaluating the combination of model + harness, not the model's capability in isolation. This definition is profoundly important because it shifts the unit of explanation for agent effectiveness from model parameters to the outer-loop structure in which the model operates.

Image
Here we must disentangle a frequently conflated concept: an agent harness and an evaluation harness are not the same thing. The former is responsible for making the agent run (handling inputs, orchestrating tools, managing state); the latter is responsible for batch-running tasks, recording trajectories, executing graders, and aggregating scores. Many discussions lump "harness" into a catch-all bucket, sometimes talking about runtime orchestration and other times about evaluation pipelines. The Harness Engineering discussed in this article refers to the former—the engineering of the runtime outer-loop system.

Based on this, a more precise formulation:

📌
Harness = the outer-loop system that enables a model to act as an Agent.

It encompasses plan decomposition, persistent state, tool orchestration, verification gates, feedback loops, rollback mechanisms, human-machine handoff points, and audit logs. When evaluating an Agent's effectiveness, what is being evaluated is not the model itself, but the combination of model + harness.

Several key points here deserve elaboration:

Outer loop is the keyword. The model's reasoning is the "inner loop"—given context, generate the next step. The harness is the "outer loop"—deciding when to start a new inner loop, what context to give it, how to verify its output, when to roll back, when to stop. Inner-loop quality depends on model capability; outer-loop quality depends on harness design.
A harness is not an upgraded version of a prompt. A single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, or continuous entropy control. Treating a harness as "a longer system prompt" is the most common failure mode today.
A harness is also not a framework name. LangChain is a framework, CrewAI is a framework—Harness Engineering is not. It is a practice, just as DevOps is not a tool but an engineering culture.
Three Layers of Engineering Abstraction
Prompt → Context → Harness

To understand the harness's position, one must first see its relationship to the two preceding layers. These three layers are not replacements but progressive levels of abstraction:

Image
📌 Key Insight
Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline operates." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; but a harness also encompasses multi-step structure, tool mediation, verification gates, and durable state—these exceed the scope of single-step context.

The Six Engineering Components of a Harness
This section is the most technically dense part of the article. Each component explains what problem it solves, what Anthropic/OpenAI specifically do, and the design principles behind it.

Durable State Surfaces: So Agents Don't Show Up to Work with Amnesia
Problem: The core pain point of long-running agents is like an engineer on a project team who completely loses their memory at every shift change. The context window is finite, complex projects cannot be completed within a single window, and the agent needs a way to bridge the gap between sessions.

Anthropic's solution: Rather than attempting "infinite context," they externalized state into resumable artifacts:

The first initializer agent sets up the environment: creates `init.sh` (startup script), `claude-progress.txt` (progress log), and an initial git commit (baseline snapshot).
Generates a feature list: expands high-level requirements into 200+ specific features, all initially marked as failing.
Each subsequent coding agent makes only incremental progress, leaving structured updates and a "clean state" at session end.
Key rule: agents can only change a feature's passes status; they cannot arbitrarily modify the test definitions themselves.
This feature list design looks "crude," but it is extraordinarily effective—it transforms the definition of "done" from the agent's subjective feeling into an external, persistent, structured, inheritable completion surface. The agent does not need to "remember" what was done before; it only needs to read the feature list and git diff to resume within 30 seconds.

Anthropic later discovered a deeper problem: context anxiety. Even with compaction (summarizing and compressing early conversation), agents still degrade in behavior because they feel "the context is too full." The solution is not better compaction but context reset—giving the next agent a completely fresh context, passing all necessary information through externalized state artifacts (rather than conversation history). This is more radical than compaction, but works better.

📌 Design Principle
State ≠ "saving chat history." True durable state is a structured artifact that an agent can read, understand, and resume from after a cold start with zero conversation history. If your agent cannot determine "where did we leave off, what's the next step" within 30 seconds of a cold start, your state management has failed.

Decomposition & Plans: Cutting Long Tasks into Bite-Sized Chunks for Agents
Problem: Tell an agent "build a clone of claude.ai" and it will try to go all-in—writing all the code in a single session. The result is either the context explodes, or it declares "done" halfway through.

Evolution:

In November 2025, Anthropic initially solved this with an initializer + coding two-role structure. The initializer handles decomposition and initialization; coding handles step-by-step implementation.

In March 2026, this structure was upgraded to a planner / generator / evaluator three-role system:

The Planner does not write code directly but expands one or two high-level descriptions into a complete product spec and a step-by-step feature list
The Generator implements feature by feature, committing after each completion
The Evaluator independently assesses the generator's output, marks pass/fail, and provides specific improvement suggestions
OpenAI's counterpart is `PLANS.md`, `Implement.md`, `Documentation.md`—complex tasks are planned first, executed by milestone, verified at each stage, with documentation continuously updated as shared memory.

📌 Design Principle
A plan must be elevated to a first-class artifact, not remain disposable chat content. It needs to be written to the file system, version-controlled, readable by subsequent agents, and referenceable by verification gates. A plan that exists only in conversation is not really a plan—it is merely a thought.

Feedback Loops: Guides and Sensors
Problem: An agent wrote code—how do you know it's correct? Rely on the agent's self-assessment? Anthropic explicitly discovered an embarrassing fact: when asked to evaluate their own work, agents tend to enthusiastically self-praise—even when the quality is visibly mediocre to a human.

This requires a feedback system that does not depend on the agent's self-evaluation. By April 2026, the community had a framework that decomposed the harness into a very clear 2×2 matrix:

Image
Guides constrain the agent before it acts, increasing the probability of "getting it right the first time." Sensors provide signals after the agent acts, enabling self-correction.

Image
Key insights:

Guides without sensors → the agent encodes rules but never knows whether the rules are effective
Sensors without guides → the agent repeatedly makes the same mistakes and then gets corrected
Computational control is cheap, fast, deterministic, and can run on every change
Inferential control is expensive, slow, non-deterministic, but can handle subjective judgments (e.g., "is this UI design too ugly?")
Anthropic's evaluator-optimizer pattern aligns perfectly with this. They also acknowledged a subtle fact: the evaluator is not always necessary—once the base model's capability crosses a certain threshold, the evaluator degrades from "essential component" to "extra overhead." This shows that a good harness is not a fixed template but a tailorable system that co-evolves with the model's capability boundary.

Image
Legibility: Building a Perception Surface for Agents
Problem: An agent can write code now, but can it "see" what the code looks like when it runs? Can it read error logs? Can it understand performance metrics?

OpenAI offered an extremely sharp judgment in their harness engineering practice: any knowledge not within the agent's runtime visibility effectively does not exist.

This is not rhetoric. They did the following concrete work to improve legibility:

Launch a dedicated browser instance for each git worktree, using CDP (Chrome DevTools Protocol[7]) so the agent can "see" the UI
Expose all logs, metrics, and traces for agent querying.
Repository knowledge as system of record: design principles, product intent, execution plans, known technical debt, architecture decision records (ADR)—all placed in the repo with lint/CI maintaining consistency.
Place `AGENTS.md`, structured `docs/`, execution plans, and knowledge documents in the repo as much as possible, making them a versioned system of record; but OpenAI also publicly cautioned: an overly long `AGENTS.md` rots quickly, crowds out context, and causes all constraints to lose focus simultaneously—a better approach is to make it a directory index, with actual knowledge distributed across structured documents.
📌 Design Principle
Legibility is not "making code more elegant"—it is making knowledge, constraints, acceptance criteria, and decision history enter the agent's perception surface. This directly transforms "knowledge management" from a team collaboration problem into an agent executability problem. For an agent, experience in Slack, architecturally transmitted boundaries, constraints scattered across external documents—if these do not enter runtime-accessible artifact surfaces, they effectively do not exist.

Tool Mediation: More Tools Means More Need for a Harness
Problem: After the MCP ecosystem exploded, a single agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions directly into context creates serious problems—token costs skyrocket, latency rises, and the agent loses its way in an ocean of tools.

Anthropic proposed a core approach in their MCP + Code Execution engineering practice: don't let the model call tools directly; let the model write code that calls tools.

What's the difference?

Direct tool invocation mode: All tool definitions loaded into context → model selects tool → invokes → result returned to context → model continues. Every step consumes context space; intermediate results circulate within the model's inner loop.
Code execution mode: Model writes a piece of code → code runs in a sandbox, discovering and invoking MCP tools as needed → only the final result is returned to the model. Tool discovery, data filtering, and intermediate processing all complete within the execution environment, never entering context.
The essence of this approach: move tool usage from the model's inner loop to a more efficient external execution loop. This is precisely harness engineering—it is not a "tool registry" but a system-level design that determines how tools are discovered, when they are exposed, at what granularity, whether results need to enter context, where state lives, and how failures roll back.

Entropy Control: Continuous Garbage Collection for Agents
Problem: Fully autonomous agent codebases continuously replicate existing patterns—even when those patterns are uneven, suboptimal, or outright bad. Over time, drift and entropy accumulation are inevitable.

OpenAI was the most blunt about this: they initially relied on humans spending roughly 20% of their time each week cleaning up "AI slop" (redundant code, outdated documentation, inconsistent naming, copy-pasted dead code). Later, they systematized this cleanup logic:

Documentation consistency agents periodically verify whether documentation matches code
Refactor agents clean up technical debt on schedule
Architectural enforcement mechanically maintains module boundaries through CI
📌 Design Principle
A harness is not only responsible for "making the agent run" but also for continuously suppressing the system noise that agents amplify. This is its most fundamental distinction from a simple "agent framework"—a framework cares about startup and orchestration; a harness cares about long-term governability.

Harnessability: Not Every System Is Easy to Harness
If we understand Harness Engineering only as "add more rules and loops to the agent," we haven't gone deep enough. The more fundamental question is: not every system is equally easy to harness.

OpenAI's practice consistently implies the same thing: the reason they could push Codex to high throughput is not just because the model is strong enough, but because they continuously pressed knowledge back into the repo, artifactized plans, versioned decisions, and made the environment more readable for agents. How naturally suited a system is to being tamed by agents is itself an important variable.

Following this logic yields a highly explanatory judgment: systems with strong typing, comprehensive tests, clear boundaries, versioned documentation, and runtime observability are naturally higher in harnessability; whereas systems where knowledge is scattered across human minds, chat tools, and oral tradition will hit the wall of "invisible → incomprehensible → ungovernable" no matter how strong the model is.

This means that in the agent era, a team's engineering infrastructure quality (CI completeness, documentation structuring, architectural boundary clarity) is no longer just a matter of "engineering literacy"—it directly determines how far an agent can go in your system. Harnessability will become a key dimension for evaluating a system's "agent-readiness."

The Intent System
A Deeper Paradigm Shift: From Instruction-Driven to Intent-Driven

The above covers the engineering components of a harness. But looking only at components leads to "assembling technical details." Let us step back and discuss something more fundamental—why Harness Engineering is not merely an engineering practice but the product of a paradigm shift.

Four Ruptures in Human-Machine Interaction
Looking back at the entire history of computing, human-machine interaction has undergone four fundamental ruptures:

CLI (command line): Humans must precisely master the machine's language. `ls -la | grep .py` is an instruction—get one character wrong in the syntax and it fails. The core assumption of interaction is "humans adapt to machines."
GUI (graphical interface): Machines lower the barrier through visual metaphors. Folders, desktops, drag-and-drop. The core assumption is "machines present themselves through metaphors humans can understand."
App (mobile applications): Logic is solidified into fixed interfaces. One button per function, one screen per button. The core assumption is "humans choose within preset paths."
Agent (intent-driven): Humans express only goals; the system autonomously plans execution paths. The core assumption is "machines understand human intent and autonomously decide how to proceed."
Each rupture is not merely a technology upgrade but a redistribution of control. In the CLI era, humans held 100% control; in the Agent era, humans have ceded most execution control, retaining only goal-setting and critical decision points.

What are the engineering consequences of this cession?

In an instruction-driven world, a bug is "the system did not correctly execute my instruction"—coverable by traditional testing. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent but chose a poor execution path"—this requires an entirely new set of verification, constraint, and feedback mechanisms, which is precisely what a harness is designed to solve.

Applications Are Being "CLI-ified," But Not for Humans
A highly counterintuitive trend: in the Agent era, all applications and websites are being re-"CLI-ified"—not to send users back to the terminal, but to turn everything into programmable interfaces from the Agent's perspective.

MCP is essentially the protocol-layer implementation of this. When an Agent needs to operate Google Drive, it doesn't need to "open a webpage and click buttons"—it needs a set of structured API calls. An MCP server abstracts Google Drive into a set of callable functions: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This implies three things:

First, the audience for readability has changed. Past readability was for humans—clear UI, sensible information architecture. Now it must first be for Agents—structured APIs, machine-parseable documentation, programmable permission models.

Second, application boundaries are dissolving. When Agents invoke any tool via MCP and collaborate with other Agents via A2A, Apps degrade from "destinations" to "infrastructure." Users no longer "open an App to do one thing" but "express an intent, and the Agent orchestrates multiple services to fulfill it."

Third, the Harness becomes the new "operating system layer." The GUI-era OS managed windows, files, and processes. The Agent era needs to manage: Agent lifecycles, tool discovery and authorization, context scheduling and reclamation, multi-Agent collaboration and isolation, and human approval intervention points.

From Chatbot to AgentOS
Connecting all the threads above reveals a clear evolutionary path. These three stages are not feature additions but fundamental changes in the engineering abstraction layer:

Level 1: Chatbot (2022–2023)
Single-turn conversation, stateless, human fully in the loop. Core value is information retrieval and content generation. Engineering abstraction layer is Prompt Engineering. Representative products: ChatGPT, Claude (early).

Ceiling: can speak but cannot act. Every conversation is isolated.

Level 2: AI Browser / Agent IDE (2024–2025)
Multi-step tasks, tool invocation, limited autonomy. Core value is task execution and workflow automation. Engineering abstraction layer is Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus, Codex.

Ceiling: single-agent capability is strong but long tasks are unstable; multi-agent collaboration lacks standards; state management is manual labor.

Level 3: AgentOS (2026– nascent stage, forward-looking direction)
This must be written with restraint. AgentOS is not yet a converged industry paradigm. But it has indeed entered the research and systems community agenda. The 2024 AIOS[8] paper proposed extracting scheduling, context management, memory management, and access control from the agent application layer into a kernel-like layer; ASPLOS 2026 featured a dedicated AgenticOS Workshop[9] exploring OS primitives for agent workloads.

Image
A more measured statement, therefore, is not "AgentOS has arrived" but: Harness Engineering is pushing the problem from the application layer toward the system layer. When agents are no longer just coding assistants but always-on, multi-agent, cross-tool, cross-identity long-running execution entities, user-space harnesses will inevitably encounter deeper system-level problems:

Agent lifecycle management: initialization, running, suspension, resumption, termination—not stateless function calls but full process management.
Context scheduling: The context window is a scarce resource; decisions must be made about what information to load when, when to compress, when to discard—this is the agent version of "memory management."
Multi-Agent isolation and collaboration: One agent's operations should not pollute another's environment, yet they need to share certain state—requiring mechanisms analogous to process isolation + IPC.
Governance and audit: Every decision step of every agent must be traceable—in finance, healthcare, and similar domains, this is not a nice-to-have but a compliance requirement.
Image
📌 Key Positioning
The Harness is the user-space layer of AgentOS. AgentOS is the kernel—managing scheduling, isolation, and resources. The Harness is the user-space shell and daemon—managing task decomposition, state resumption, verification feedback, and human-machine handoff. The two are not competitors but natural upper and lower layers.

Five Typical Symptoms
Theory aside, back to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are still in the makeshift assembly stage. Here are five typical symptoms:

Symptom One: Framework jungle. LangChain, CrewAI, AutoGen, Agno, n8n… each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to verification to rollback to audit. Users cobble together across frameworks, getting a fragile pipeline rather than a governable system.

Symptom Two: Chatbot skin + Agent core. A large number of products are essentially a chatbot interface wrapped around an agent loop—but lacking true state management, task decomposition, and verification gates. Stunning in demos, repeatedly crashing in production.

Symptom Three: Tool registration ≠ tool governance. MCP made connection easy, but "can connect" does not equal "knows how to use." An agent facing 50 tools becomes confused, makes redundant calls, and takes detours. Engineering teams have found that initially providing agents with all tools actually yields worse results—performance improved only after pruning to the minimal necessary set.

Symptom Four: One-time rules vs. evolvable constraints. Most teams' agent configuration is a massive `AGENTS.md` or system prompt. But practice shows this approach inevitably fails—when everything is important, nothing is important. Agents pattern-match locally rather than consciously navigating. Rules rot faster than humans can maintain them.

Symptom Five: Lack of on-the-loop thinking. "In the loop" means manually fixing artifacts when unsatisfied with agent output; "on the loop" means modifying the harness so the system automatically produces better results next time. Most teams are still stuck in the loop—fixing errors one by one rather than systematically improving the control loops that produce them.

What a Harness Is Not
Clarifying boundaries is as important as clarifying definitions.

It is not "a longer system prompt." Because a single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, or continuous entropy control.

It is not some vendor's proprietary term. Both Anthropic and OpenAI use it publicly, and academic preprints are already abstracting it into a cross-product universal concept.

It is also not "won't be needed once models get stronger." Quite the opposite—Anthropic explicitly noted that as the model boundary expands, the harness redistributes value: certain checks become redundant, but planning, verification, handoff, and state governance for harder tasks become more important. The stronger the model, the more necessary it is to place longer, more expensive, more dangerous tasks inside a controlled outer loop.

In fact, the space of interesting harness combinations does not shrink as models get stronger—it shifts. An evaluator effective today may become redundant overhead before the next generation of models, but new capability boundaries will spawn new harness requirements.

Overlooked Critical Questions
Testability of the Harness
When we say "the harness makes agents verifiable," a meta-question arises: how do you verify the harness itself? If the evaluator uses another LLM, and that LLM also has hallucination tendencies, we have built a loop of "using an unreliable system to verify an unreliable system."

Anthropic's approach is to use computational sensors (test suites, linters, type checkers) for foundational verification as much as possible, enabling inferential sensors only at the subjective judgment level (UI aesthetics, code style). This is a pragmatic layered strategy, but not a perfect solution.

Emergent Behavior in Multi-Agent Systems
When 10 agents run in parallel, each making independent decisions, system behavior exhibits emergent patterns that single-agent analysis cannot predict. This is analogous to concurrency bugs in distributed systems—but worse, because every "process" is non-deterministic. Current harness design primarily targets single-agent scenarios; harness principles for multi-agent collaboration have not yet crystallized.

Engineering Trade-offs Between Cost and Latency
Every layer of the harness—planner, evaluator, sensor, garbage collection—consumes additional tokens and latency. When the harness's own overhead exceeds the quality improvement it delivers, that is over-engineering. How to measure harness ROI and how to dynamically adjust harness depth based on task complexity remain unsolved engineering problems.

A New Dimension of Security: The Attack Target Shifts from Data to Agency
This is the layer most articles gloss over but is actually the most dangerous. As agents gain persistent state, external tools, and long-duration autonomy, the attack surface is no longer just "what did the model get wrong" but "can the system be co-opted."

Invariant Labs disclosed Tool Poisoning Attacks[10] in April 2025: malicious instructions can be hidden in MCP tool descriptions, invisible to users but visible to the model, thereby inducing agents to perform unauthorized operations; a week later, they demonstrated a data exfiltration scenario where an untrusted MCP server leveraged a trusted WhatsApp MCP. This means Harness Engineering cannot discuss only throughput and stability—it must also directly address tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation.

Image
MCP's open standardization is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connection becomes, the more the upper-layer harness must enforce stricter governance. The harness's permission model must upgrade from static "can/cannot" to dynamic "under what conditions can, up to what limit can, only after human confirmation can." In other words, the harness is not only an outer loop for improving output—it is itself a new security boundary.

Judgments & Outlook
Judgment One: Harness Engineering will become one of the foundational disciplines of the AI engineering era
Model capability improvements will continue to absorb some micro-level prompt techniques, but will not absorb harness engineering. Because it addresses higher-level problems: how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents must work across time, across tools, across environments, and across human-machine boundaries, the harness will not disappear—it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

Judgment Two: The moat's center of gravity is shifting upward from model quality to harness and system design
When GPT, Claude, and Gemini converge on core capabilities, what determines product success or failure is no longer model differentiation but harness quality. The hardest evidence comes from LangChain: without changing the underlying model, they improved deepagents-cli on Terminal Bench 2.0 from 52.8% to 66.5%—a gain of 13.7 points—solely by modifying the harness, pulling their ranking from outside the Top 30 into the Top 5. This result should not be exaggerated into "models no longer matter," but it is sufficient to demonstrate: on top of the same model, the harness alone can create enormous system-level gaps. The moat's center of gravity is shifting upward to harness and system design.

Judgment Three: The migration from Chatbot to AgentOS will not happen in one step
There will be a 2–3 year "AI Browser + lightweight Harness" phase in between. Most enterprises will first capture value in this phase, then gradually evolve toward heavier AgentOS architectures. Teams attempting to leap directly to AgentOS will most likely fail because governance complexity exceeds their capacity to bear.

Judgment Four: The engineer's role is shifting from "code producer" to "designer of autonomous systems"
This is not an unemployment warning but a capability upgrade requirement. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing anomalies, distilling rules—the value of these capabilities will rise sharply. When unsatisfied with agent output, the low-level approach is to manually fix artifacts; the high-level approach is to modify the harness so the system automatically does better next time. From in the loop to on the loop—this is the engineer's core upgrade path in the agent era.

Appendix
Three self-check questions for practitioners. Before building your own harness, answer these three questions first:

Does your agent have durable state surfaces? Can it resume within 30 seconds of a cold start—or does it start from scratch every time?
Does your system have machine-readable acceptance criteria? Is the definition of "done" the agent's subjective feeling, or an external structured verification surface—a feature list, a set of test cases, a checkable pass/fail state?
Are your repo, tools, logs, metrics, and policies legible and enforceable for the agent? Or can only humans read them—leaving the agent to guess?
If none of these three exist, what you've built is most likely still just "a chatbot that can run commands"...
