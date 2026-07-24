Background

First, answer a prerequisite question: How did we get here?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, one must first see the complete arc that AI engineering has traversed over the past four years. This arc is not linear; it is a cycle of capability leaps → collapse of old frameworks → emergence of new abstractions.

Recommended reading for additional background:

"AI OS: From Instructions to Intent"
"From Prompt Engineering to Context Engineering"
"The Token Naming Dilemma: When Information Theory Invades Linguistics"
"OpenClaw: The Risks Behind the Hype"
"Deep Dive: Google Workspace CLI"
"Meta-Skills: Making AI Think Like You"
"Agent Trends: Nativization & CLI-ization"
"The AI Programming Ecosystem: What Does Anthropic's Acquisition of Bun Mean?"
"Deep Thinking: On AI Development Trends"
"On AI Browsers"
"Deep Dive: The Anthropic MCP Protocol"

Act One: Generation (2022.11 — 2023)

On November 30, 2022, ChatGPT went live. It reached approximately 100 million monthly active users about two months after launch. But what truly changed was not NLP technology — GPT-3 had already existed for two years — but the interaction paradigm. Before this, the LLM was an API usable only by engineers; after this, it became a conversational interface usable by everyone.

The core contradiction in this act is: the model can generate, but it cannot act. It can write an email, but cannot send it; it can write a block of code, but cannot run it. The relationship between user and model is "you ask, I answer" — a stateless, single-turn, passive exchange of information.

The engineering product of this era is Prompt Engineering: how to ask so that the model answers better. Few-shot, chain-of-thought, role-playing — all are essentially attempts to maximize information density within the limited space of a single API call.

Act Two: Connection (2023 — 2024)

In March 2023, OpenAI released GPT-4, bringing multimodality and longer context windows. In the same month, it launched ChatGPT Plugins, giving the model "hands" for the first time — the ability to call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool invocation as structured JSON in model output.

This is a critical inflection point: the model evolved from "can speak" to "can connect." But the Plugins ecosystem quickly exposed its fragility — each plugin required independent OAuth flows, independent schema definitions, and independent error handling. Connecting 10 plugins was already painful; 100 was impossible.

In the second half of 2023, LangChain rose, attempting to solve the "connection" problem with a layer of intermediate abstraction. It did lower the barrier to entry, but at the cost of over-abstraction — too many layers of wrapping, difficult debugging, unpredictable performance. During the same period, projects like AutoGPT and BabyAGI attempted to let models autonomously loop through task execution, but all fell silent soon after their demos due to the lack of reliable stopping conditions and verification mechanisms.

🤯 Lesson One
Making the model "able to connect to tools" is necessary, but far from sufficient. Connection does not equal orchestration, and orchestration does not equal governance.

Act Three: Reasoning (2024)

2024 is the year "reasoning models" took the stage. OpenAI's o1 series launched in September, with "spending more time thinking before answering" as its core characteristic, achieving a qualitative leap in mathematics and programming tasks. In December, the ARC Prize announced that OpenAI o3 reached 87.5% on the ARC-AGI-1 Semi-Private Eval in its high-compute configuration, shocking the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet excelled in code generation and long-document understanding, and DeepSeek-R1, as an open-weight model, proved that high-performance reasoning was no longer the exclusive domain of closed-source models.

More importantly, two events occurred at the end of 2024:

First: Anthropic released the Model Context Protocol (MCP). This is not yet another plugin system, but an open standard protocol that uses JSON-RPC 2.0 to define how AI applications communicate with external tools and data sources. Its core insight is: the connection problem is fundamentally an N×M problem — N AI applications × M data sources, each combination requiring a custom connector. MCP reduced it to N+M: each application implements an MCP client once, and each tool implements an MCP server once. Later, OpenAI and Google DeepMind successively announced support for MCP; in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

Second: Anthropic published the "Building Effective Agents" guide (December 2024). This article was the first to systematically discuss agent engineering patterns — from the simplest prompt chaining to the evaluator-optimizer loop — and explicitly proposed a principle: start with the simplest pattern, and only introduce more structure when complexity genuinely yields better results. This principle later became one of the core guiding philosophies of Harness Engineering.

By 2025, Anthropic further elevated context engineering as an independent engineering practice in "Effective Context Engineering for AI Agents," emphasizing that the real difficulty is no longer merely "how to write a prompt," but "at each step, what information, in what form, and at what timing, to hand to the model." This is the key transition layer from Prompt Engineering to Harness Engineering — the problem has shifted upward from "single call" to "per-step context," but has not yet shifted to "the entire task outer loop."

🤯 Lesson Two
The model's reasoning capability solves the "single-step quality" problem, but the reliability of long tasks does not automatically follow from smarter individual steps. A model capable of solving IMO gold-medal problems can still "forget what it was doing" midway through a four-hour full-stack development task.

Act Four: Action (2025)

If 2023 was the Chatbot year and 2024 the multimodal year, then 2025 was the Agent year.

At the beginning of the year, the open-source release of DeepSeek-R1 caused the market to reassess the landscape of model competition. This was followed by a string of agent products: Claude Code (a programming agent in the terminal), GitHub Copilot Agent Mode, Cursor's autonomous coding loop, Manus (a browser-operating agent), and OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all mainstream languages. Google released the Agent2Agent (A2A) protocol to solve cross-vendor communication between agents.

But the most important discovery of 2025 was not what agents can do, but how they break while doing it:

An agent attempts to complete an entire task in one go, exhausting its context window halfway through.
An agent declares "all done" after completing 70%, then stops.
Multiple agents running in parallel produce cascading errors, with a single small mistake amplified to an undebuggable degree.
After continuous agent work, the codebase develops severe "AI slop" — redundant code, inconsistent naming, outdated documentation.
These are not intelligence problems of the model, but structural problems of the system.

🤯 Lesson Three
Agent capabilities have reached the level of "can autonomously work for hours," but the engineering infrastructure surrounding them remains stuck in the "single conversation" era. This fracture is the root cause of Harness Engineering's birth.

Act Five: Governance (2026 — Present)

At the beginning of 2026, industry attention began shifting from "how to make agents more capable" to "how to keep agents from going off the rails." "Harness Engineering" as a public term was not invented on a single day, but began rapidly coalescing and spreading starting in February 2026:

On February 5, 2026, Mitchell Hashimoto explicitly wrote "Engineer the Harness" in "My AI Adoption Journey" — considered one of the starting points for the term entering mainstream discussion.
On February 11, 2026, OpenAI directly published an engineering article titled "Harness Engineering: Leveraging Codex in an Agent-First World." They used a small team to build an internal beta product from an empty repository over five months, publicly stating "zero lines of human-handwritten code," with the repository reaching approximately one million lines of code and generating about 1,500 PRs. More precisely, the initial scaffold was still generated by Codex under limited template guidance; thereafter, application logic, tests, CI, documentation, observability, and internal tools were produced by the agent as much as possible. The core discovery: engineers' work shifted toward designing environments, specifying intent, and building feedback loops.
In March 2026, Anthropic published "Harness Design for Long-Running Application Development," upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, proving that the evaluator can still deliver clear gains near the model capability boundary.
In April 2026, the Thoughtworks / Fowler system ("Harness Engineering — First Thoughts") systematized this concept into a more complete methodological framework — a combination of guides (feedforward control) and sensors (feedback control), each further divided into computational (deterministic) and inferential (probabilistic) types, forming a 2×2 control matrix. Thus, April is better understood as "the methodological abstraction became complete," rather than "the first naming."
What Is Harness, Exactly?

Let us derive from first principles, rather than starting from a definition.

The Five Fundamental Challenges of Agents

The essence of an agent is "a system that autonomously advances goals in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone:

State Persistence
Essence: The agent needs to remember what it has done across time and across sessions.
Why the model cannot solve it: The model itself is stateless, and the context window has an upper limit; it cannot naturally assume long-term continuous state.
Goal Consistency
Essence: In long tasks, the agent tends to drift, get carried away, or even declare completion prematurely.
Why the model cannot solve it: The model lacks external anchor points and cannot stably calibrate "what actually counts as done."
Action Verifiability
Essence: Every step is probabilistic; one must distinguish between "did it" and "did it right."
Why the model cannot solve it: The model has a natural tendency toward self-praise and misjudgment when evaluating its own results.
Entropy Suppression
Essence: Continuous output constantly accumulates redundancy, drift, and inconsistency.
Why the model cannot solve it: The model will replicate existing patterns, even when those patterns themselves are bad or low-quality.
Human-Agent Boundary
Essence: When to act autonomously and when to hand off to humans needs to be defined clearly and engineered.
Why the model cannot solve it: The model does not possess reliable "uncertainty self-awareness" and cannot stably judge when it should stop and return control to humans.
Harness is the engineering practice that systematically answers these five challenges.

A Precise Definition

Anthropic gave a definition in "Demystifying Evals for AI Agents" that is well worth adopting directly: an agent harness (or scaffold) is the system that enables a model to act as an agent; it handles input, orchestrates tool calls, and returns results. More critically, Anthropic further points out: when we evaluate "an agent," we are actually evaluating the combination of model + harness, not the model's capabilities alone. This definition is vitally important because it shifts the explanatory unit of agent effectiveness from model parameters to the outer-loop structure in which the model operates.

Image

Here, a concept that is often conflated must be unpacked: agent harness and evaluation harness are not the same thing. The former is responsible for making the agent run (handling input, orchestrating tools, managing state); the latter is responsible for batch-running tasks, recording traces, executing graders, and aggregating scores. Much discussion throws "harness" into one big bucket, resulting in oscillation between runtime orchestration and evaluation pipelines. The Harness Engineering discussed in this article refers to the former — the engineering of runtime outer-loop systems.

Based on this, a more precise formulation:

📌
Harness = the outer-loop system that enables a model to act as an Agent.

It encompasses planning and decomposition, durable state, tool orchestration, validation gating, feedback loops, fallback mechanisms, human handoff points, and audit logs. When evaluating an Agent's effectiveness, one evaluates not the model itself, but the model + harness combination.

Several points here are worth elaborating:

Outer loop is the keyword. Model reasoning is the "inner loop" — given context, generate the next step. Harness is the "outer loop" — deciding when to start a new inner loop, what context to give it, how to verify its output, when to fall back, when to stop. Inner-loop quality depends on model capability; outer-loop quality depends on harness design.
Harness is not an upgraded prompt. A single prompt cannot solve cross-session state, validation gates, tool discovery, failure recovery, and continuous entropy control. Treating Harness as "a longer system prompt" is the most common failure mode today.
Harness is not a framework name. LangChain is a framework; CrewAI is a framework; Harness Engineering is not. It is a practice, just as DevOps is not a tool but an engineering culture.
Three Layers of Engineering Abstraction

Prompt → Context → Harness

To understand Harness's position, one must first see its relationship with the preceding two layers. These three layers are not replacements but progressive levels of abstraction:

Image

📌 Key Insight
Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline operates." The former is a subset of the latter. On the user side, Harness Engineering is essentially a specific form of Context Engineering; but Harness also encompasses multi-step structure, tool mediation, validation gates, and durable state — areas beyond the scope of single-step context.

The Six Engineering Components of Harness

This section is the most硬核 (hardcore) part of the article. Each component will explain what problem it solves, Anthropic/OpenAI's specific approach, and the design principles behind it.

Durable State Surfaces: Preventing Agents from "Showing Up Amnesiac"

Problem: The core pain point of long-running agents is like an engineer on a project team who suffers complete amnesia every shift change. The context window is limited, and complex projects cannot be completed within a single window; the agent needs a way to bridge the gap between sessions.

Anthropic's solution: Rather than attempting "infinite context," they externalized state into durable artifacts:

The first initializer agent sets up the environment: creating init.sh (startup script), claude-progress.txt (progress log), initial git commit (baseline snapshot).
It generates a feature list: expanding high-level requirements into 200+ specific features, initially all marked as failing.
Each subsequent coding agent makes only incremental progress, leaving structured updates and a "clean state" at the end of each session.
Key rule: the agent may only change a feature's passes status; it may not arbitrarily modify the test definitions themselves.
This feature list design looks " crude," but is extremely effective — it transforms the definition of "done" from the agent's subjective feeling into an external, durable, structured, and inheritable completion surface. The agent does not need to "remember" what was done before; it only needs to read the feature list and git diff to resume within 30 seconds.

Anthropic later discovered a deeper problem: context anxiety. Even with compaction (summarizing compression of early conversations), agents still degraded in behavior because they felt "the context is too full." The solution was not better compaction, but context reset — directly giving the next agent a completely fresh context, passing all necessary information through externalized state artifacts (rather than conversation history). This is more radical than compaction, but more effective.

📌 Design Principle
State ≠ "saving chat history." True durable state is a structured artifact that an agent can read, understand, and resume from after a cold start, with zero context history. If your agent cannot know "where we left off and what to do next" within 30 seconds of cold start, your state management has failed.

Decomposition & Plans: Breaking Long Tasks into Agent-Digestible Chunks

Problem: Tell an agent "build a clone of claude.ai," and it will try to go all-in — writing all the code in a single session. The result is either a blown context window or a declaration of "done" halfway through.

Evolution:

In November 2025, Anthropic used an initializer + coding two-role structure to preliminarily solve this problem. The initializer handled decomposition and initialization; the coding role handled gradual implementation.

In March 2026, this structure was upgraded to a planner / generator / evaluator three-role system:

The planner does not write code directly, but expands one or two sentences of high-level description into a complete product spec and step-by-step feature list.
The generator is responsible for landing each feature one by one, committing after each completion.
The evaluator independently assesses the generator's output, marking pass/fail and giving specific improvement suggestions.
OpenAI's counterpart is PLANS.md, Implement.md, Documentation.md — complex tasks are planned first, executed milestone by milestone, with verification at each stage, while continuously updating documentation as shared memory.

📌 Design Principle
Plans must be elevated to first-class artifacts, not one-time chat content. They need to be written to the filesystem, version-managed, readable by subsequent agents, and referenceable by validation gates. A plan that exists only in conversation is essentially not a plan — it is merely a passing thought.

Feedback Loops: Guides and Sensors

Problem: The agent wrote code — how does it know if the code is correct? Rely on the agent's own evaluation? Anthropic explicitly discovered an embarrassing fact: when asked to evaluate its own work, the agent tends to enthusiastically self-praise — even when the quality is clearly mediocre to human eyes.

This calls for a feedback system that does not rely on agent self-evaluation. In April 2026, the community already had frameworks breaking harness into a very clear 2×2 matrix:

Image

Guides constrain the agent before it acts, increasing the probability of "getting it right the first time." Sensors give signals after the agent acts, supporting self-correction.

Image

Key insights:

Only guides, no sensors → the agent encodes rules but never knows if they are effective.
Only sensors, no guides → the agent repeatedly makes the same mistakes and then gets corrected.
Computational control is cheap, fast, and deterministic; it can run on every change.
Inferential control is expensive, slow, and non-deterministic, but can handle subjective judgments (e.g., "is this UI design too ugly?").
Anthropic's evaluator-optimizer mode is fully consistent with this. They simultaneously acknowledged a subtle fact: the evaluator is not always necessary — when the base model capability crosses a certain threshold, the evaluator degrades from "necessary component" to "additional overhead." This shows that a good harness is not a fixed template, but a trimmable system that co-evolves with model capability boundaries.

Image

Legibility: Building Perceptual Surfaces for Agents

Problem: The agent can write code, but can it "see" what its code looks like when running? Can it read error logs? Can it understand performance metrics?

OpenAI gave an extremely sharp judgment in their Harness Engineering practice: any knowledge not visible to the agent at runtime is equivalent to nonexistent.

This is not rhetoric. They did the following concrete work to improve legibility:

Launch an independent browser instance for each git worktree, allowing the agent to "see" the UI through CDP (Chrome DevTools Protocol).
Expose all logs, metrics, and traces to the agent for querying.
Repository knowledge as system of record: design principles, product intent, execution plans, known technical debt, architectural decision records (ADR) — all placed in the repo and maintained consistent through lint/CI.
Place AGENTS.md, structured docs/, execution plans, and knowledge documents in the repo as much as possible, making them a versioned system of record; but OpenAI also publicly cautioned: an overly long AGENTS.md rots quickly, consumes context, and causes all constraints to lose focus simultaneously — the better approach is to turn it into a directory index, with true knowledge broken into structured documents.
📌 Design Principle
Legibility is not "making code more elegant," but making knowledge, constraints, acceptance criteria, and decision history enter the agent's perceptual surface. This directly transforms "knowledge management" from a team collaboration problem into an agent-executable problem. For the agent, experience in Slack, architectural boundaries passed down orally, and constraints scattered in external documents are equivalent to nonexistent if they do not enter runtime-accessible artifact surfaces.

Tool Mediation: More Tools Demand More Harness

Problem: After the MCP ecosystem exploded, an agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions directly into context creates serious problems — token cost explodes, latency rises, and the agent gets lost in a sea of tools.

Anthropic proposed a core idea in their MCP + Code Execution engineering practice: don't let the model call tools directly; let the model write code to call tools.

What is the difference?

Direct tool invocation mode: All tool definitions are loaded into context → model selects tool → calls it → result is fed back into context → model continues. Every step consumes context space; intermediate results stay in the model's inner loop.
Code execution mode: The model writes a block of code → code runs in a sandbox, discovering and calling MCP tools on demand → only the final result is fed back to the model. Tool discovery, data filtering, and intermediate processing all happen in the execution environment, never entering context.
The essence of this idea is: moving tool usage from the model's inner loop to a more efficient external execution loop. This is precisely Harness Engineering — it is not a "tool registry," but a system-level design that determines how tools are discovered, when they are exposed, at what granularity they are exposed, whether results need to enter context, where state resides, and how failures fall back.

Entropy Control: Continuous Garbage Collection for Agents

Problem: Fully autonomous agent codebases will continuously replicate existing patterns — even when those patterns are uneven, suboptimal, or outright bad. Over time, drift and entropy are inevitable.

OpenAI stated this most bluntly: they initially relied on humans spending about 20% of their time each week cleaning up "AI slop" (redundant code, outdated documentation, inconsistent naming, copy-pasted dead code). Later, they systematized this cleanup logic:

Documentation consistency agents periodically verify whether documentation and code are consistent.
Refactor agents clean up technical debt on schedule.
Architectural enforcement mechanically maintains module boundaries through CI.
📌 Design Principle
Harness is responsible not only for "making the agent run," but also for continuously suppressing the system noise that the agent amplifies. This is its most essential difference from simple "agent frameworks" — frameworks care about startup and orchestration; Harness cares about long-term governability.

Harnessability: Not Every System Is Equally Harnessable

If Harness Engineering is understood only as "adding more rules and loops to the agent," it does not go deep enough. The more fundamental question is: not every system is equally easy to harness.

OpenAI's practice constantly hints at the same thing: the reason they could push Codex to high throughput is not just because the model is strong enough, but because they continuously pushed knowledge back into the repo, made plans into artifacts, versioned decisions, and made the environment more readable to the agent. How naturally suitable a system is for being tamed by an agent is itself an important variable.

Following this logic, a highly explanatory judgment emerges: systems that are strongly typed, thoroughly tested, have clear boundaries, versioned documentation, and runtime observability are naturally more harnessable; while systems where knowledge is scattered in human brains, chat tools, and oral tradition will hit the wall of "invisible → incomprehensible → ungovernable" even with a stronger model.

This means that in the agent era, a team's engineering infrastructure quality (CI completeness, documentation structuring, architectural boundary clarity) is no longer just an "engineering literacy" issue — it directly determines how far an agent can go on your system. Harnessability will become the key dimension for evaluating a system's "agent-readiness."

Intent System

A deeper paradigm shift: from instruction-driven to intent-driven

The above discussed the engineering components of Harness. But if one only looks at components, one falls into "splicing technical details." Let us step back and address a more fundamental matter — why Harness Engineering is not just an engineering practice, but the product of a paradigm shift.

Four Discontinuities in Human-Computer Interaction

Looking back at the entire history of computing, human-machine interaction has experienced four fundamental discontinuities:

CLI (Command Line): Humans must precisely master the machine's language. `ls -la | grep .py` is an instruction; one wrong character and it fails. The core assumption of interaction is "humans adapt to machines."
GUI (Graphical Interface): The machine lowers the barrier through visual metaphors. Folders, desktops, drag-and-drop. The core assumption of interaction is "the machine presents itself through metaphors humans can understand."
App (Mobile Application): Logic is frozen into fixed interfaces. One function per button, one button per screen. The core assumption of interaction is "humans choose among preset paths."
Agent (Intent-Driven): Humans only express goals; the system autonomously plans and executes paths. The core assumption of interaction is "the machine understands human intent and autonomously decides how to act."
Each discontinuity is not merely a technological upgrade, but a redistribution of control. In the CLI era, humans held 100% control; in the Agent era, humans cede most execution control, retaining only goal-setting and key decision points.

What are the engineering consequences of this cession?

In the instruction-driven world, a bug is "the system did not correctly execute my instruction" — coverable by traditional testing. In the intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent but chose a terrible execution path" — requiring a completely new set of verification, constraint, and feedback mechanisms, which is precisely what Harness is designed to solve.

Applications Are Being "CLI-ified" — But Not for Humans

A very counterintuitive trend: in the Agent era, all applications and websites are being re-"CLI-ified" — not to bring users back to the terminal, but to turn everything into a programmable interface from the Agent's perspective.

The essence of MCP is the protocol-layer realization of this. When an Agent needs to operate Google Drive, it does not need to "open a webpage and click buttons" — it needs a set of structured API calls. The MCP server abstracts Google Drive into a set of callable methods: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This means three things:

First, the object of readability has changed. Past readability was for humans — clear UI, reasonable information architecture. Now it must first be for Agents — structured APIs, machine-parseable documentation, programmable permission models.
Second, application boundaries are dissolving. When an Agent calls any tool through MCP and collaborates with other Agents through A2A, the App degrades from "destination" to "infrastructure." Users no longer "open an App to do one thing," but "express an intent, and the Agent orchestrates multiple services to complete it."
Third, Harness becomes the new "operating system layer." The GUI-era OS managed windows, files, and processes. The Agent era needs to manage: Agent lifecycles, tool discovery and authorization, context scheduling and reclamation, multi-Agent collaboration and isolation, and human approval intervention points.
From Chatbot to AgentOS

Stringing all the above clues together, one can see a clear evolution path. These three stages are not feature stacking, but fundamental changes in engineering abstraction layers:

Level 1: Chatbot (2022–2023)
Single-turn conversation, stateless, humans fully in the loop. Core value is information retrieval and content generation. Engineering abstraction layer is Prompt Engineering. Representative products: ChatGPT, Claude (early).

Ceiling: can speak but cannot act. Every conversation is isolated.

Level 2: AI Browser / Agent IDE (2024–2025)
Multi-step tasks, tool calls, limited autonomy. Core value is task execution and workflow automation. Engineering abstraction layer is Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus, Codex.

Ceiling: single-agent capability is strong but long-task stability is weak; multi-agent collaboration lacks standards; state management is manual.

Level 3: AgentOS (2026–, embryonic stage)
This must be written with restraint. AgentOS is not yet a converged industry paradigm. But it has indeed entered the research and systems community agenda. The 2024 AIOS paper proposed extracting scheduling, context management, memory management, and access control from the agent application layer into a kernel-like layer; ASPLOS 2026 hosted a dedicated AgenticOS Workshop exploring OS primitives for agent workloads.

Image

Therefore, the more prudent statement is not "AgentOS has arrived," but: Harness Engineering is pushing the problem from the application layer toward the systems layer. When the agent is no longer just a coding assistant, but an always-on, multi-agent, cross-tool, cross-identity long-running execution entity, user-space harness will inevitably hit more fundamental system problems:

Agent lifecycle management: initialization, running, suspension, resumption, termination — not stateless function calls, but full process management.
Context scheduling: The context window is a scarce resource; decisions must be made about what information to load when, when to compress, when to discard — the agent version of "memory management."
Multi-Agent isolation and collaboration: one agent's operations should not pollute another's environment, yet they need to share certain states — requiring mechanisms akin to process isolation + IPC.
Governance and audit: every step of every agent's decision-making must be traceable — in finance, healthcare, and other domains, this is not a nice-to-have but a compliance requirement.
Image

📌 Key Positioning
Harness is the user-space layer of AgentOS. AgentOS is the kernel — managing scheduling, isolation, and resources. Harness is the user-space shell and daemon — managing task decomposition, state persistence, validation feedback, and human handoff. The two are not competitive but natural upper and lower layers.

Five Typical Symptoms

Theory is done; back to reality. If you observe the current ecosystem, you will find that most so-called "agent systems" are still stuck in the temporary-patch stage. Here are five typical symptoms:

Symptom One: Framework Jungle. LangChain, CrewAI, AutoGen, Agno, n8n... each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to validation to fallback to audit. Users patch together different frameworks, getting a fragile pipeline rather than a governable system.

Symptom Two: Chatbot Skin + Agent Core. Many products are essentially a chatbot interface wrapped around an agent loop — but lack real state management, task decomposition, or validation gates. Impressive in demos, frequently failing in production.

Symptom Three: Tool Registration ≠ Tool Governance. MCP makes connection easy, but "can connect" does not equal "can use well." An agent facing 50 tools gets confused, makes redundant calls, and takes detours. Some engineering teams found that initially giving the agent all tools actually performed worse — performance only improved after trimming to the minimum necessary set.

Symptom Four: One-Shot Rules vs. Evolvable Constraints. Most teams' agent configuration is a massive AGENTS.md or system prompt. But practice shows this approach is guaranteed to fail — when everything is important, nothing is. The agent pattern-matches locally rather than navigating consciously. Rules rot faster than humans can maintain them.

Symptom Five: Lack of On-the-Loop Thinking. "In the loop" means manually fixing agent output when dissatisfied; "on the loop" means modifying the harness so the system automatically produces better results next time. Most teams remain in the loop — fixing errors one by one, rather than systematically improving the control loop that produces the errors.

What Harness Is Not

Clarifying boundaries is as important as clarifying the definition.

It is not "a longer system prompt." Because a single prompt cannot solve cross-session state, validation gates, tool discovery, failure recovery, and continuous entropy control.

It is not a vendor-specific term. Both Anthropic and OpenAI use it publicly, and academic preprints are already abstracting it into a cross-product universal concept.

It is not "something we won't need once models get stronger." On the contrary — Anthropic explicitly states that harness will redistribute value as model boundaries expand: some checks become redundant, but planning, validation, handoff, and state governance for harder tasks become more important. The stronger the model, the more necessary it is to put longer, more expensive, and more dangerous tasks into a controlled outer loop.

In fact, the space of interesting harness combinations will not shrink as models get stronger — it will shift. Today's effective evaluator may become redundant overhead in front of the next-generation model, but new capability boundaries will spawn new harness needs.

Overlooked Critical Issues

Testability of Harness

When we say "harness makes agents verifiable," a meta-question is: how is the harness itself verified? If the evaluator uses another LLM, and that LLM also has a hallucination tendency, we have built a cycle of "using an unreliable system to verify an unreliable system."

Anthropic's approach is to use computational sensors (test suites, linters, type checks) for foundational verification as much as possible, and only enable inferential sensors (UI aesthetics, code style) for subjective judgments. This is a pragmatic layered strategy, but not a perfect solution.

Emergent Behavior of Multi-Agent Systems

When 10 agents run in parallel and make independent decisions, system behavior will exhibit patterns that no single-agent analysis can predict. This is similar to distributed-system concurrency bugs — but worse, because each "process" is non-deterministic. Current harness designs mainly target single-agent scenarios; harness principles for multi-agent collaboration have not yet precipitated.

Cost-and-Latency Engineering Tradeoffs

Every layer of Harness — planner, evaluator, sensor, garbage collection — consumes additional tokens and latency. When harness overhead exceeds the quality improvement it brings, it is over-engineering. How to measure harness ROI, and how to dynamically adjust harness depth based on task complexity, is an unsolved engineering problem.

A New Dimension of Security: Attack Targets Shift from Data to Agency

This is the layer that many articles most easily gloss over, yet it is the most dangerous. As agents gain persistent state, external tools, and long-term autonomy, the attack surface is no longer merely "what the model answered wrong," but "can the system be leveraged and manipulated."

In April 2025, Invariant Labs disclosed Tool Poisoning Attacks: malicious instructions can hide in MCP tool descriptions, invisible to users but visible to models, thereby inducing agents to execute unauthorized operations; a week later, they demonstrated a data exfiltration scenario linking an untrusted MCP server to a trusted WhatsApp MCP. This means Harness Engineering cannot discuss only throughput and stability; it must directly address tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation.

Image

MCP's open standardization is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connections become, the more the upper-layer harness must enforce stricter governance. Harness permission models must upgrade from static "can/cannot" to dynamic "can under what conditions, up to what limit, and only after human confirmation." In other words, harness is not just an outer loop that improves output; it is itself a new security boundary.

Assessment & Outlook

Assessment One: Harness Engineering will become one of the foundational disciplines of the AI engineering era
Model capability improvements will continuously consume some micro-level prompt techniques, but not Harness Engineering. Because it addresses higher-level problems: how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents need to work across time, across tools, across environments, and across human-agent boundaries, harness will not disappear — it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

Assessment Two: The center of competitive moats is shifting upward from model quality to Harness and system design
As GPT, Claude, and Gemini converge in core capabilities, what determines product success is no longer model differences, but harness quality. The hardest evidence comes from LangChain: by modifying only the harness while keeping the underlying model unchanged, they improved deepagents-cli on Terminal Bench 2.0 from 52.8% to 66.5%, a 13.7-point gain, moving the ranking from outside the Top 30 to the Top 5. This result cannot be exaggerated into "models no longer matter," but it is sufficient to show: on the same model, harness can create a massive system gap. The center of competitive moats is shifting upward to harness and system design.

Assessment Three: The migration from Chatbot to AgentOS will not happen overnight
There will be a 2-3 year "AI Browser + lightweight Harness" intermediate stage. Most enterprises will first capture value in this stage, then gradually evolve toward heavier AgentOS architectures. Teams attempting to jump directly to AgentOS will likely fail because governance complexity exceeds their capacity.

Assessment Four: The engineer's role is shifting from "code producer" to "designer of autonomous systems"
This is not a job-loss warning, but a capability upgrade requirement. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing anomalies, and precipitating rules — the value of these capabilities will rise sharply. When dissatisfied with agent output, the low-level approach is to manually fix the artifact; the high-level approach is to modify the harness so the system automatically does better next time. From in the loop to on the loop — this is the core upgrade path for engineers in the agent era.

Appendix

Three Self-Check Questions for Practitioners. Before building your own harness, answer these three questions first:

Does your agent have durable state surfaces? Can it resume within 30 seconds of cold start — or does it start from scratch every time?
Does your system have machine-readable acceptance criteria? Is the definition of "done" the agent's own feeling, or an external structured validation surface — a feature list, a set of test cases, a checkable pass/fail state?
Are your repo, tools, logs, metrics, and policies legible and enforceable to the agent? Or are they only human-readable — leaving the agent to guess?
If none of these three things are in place, what you are building is probably just a "chatbot that can run commands"...
