# Background

Let's start with a prerequisite question: how did we get here?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, we first need to see the complete arc that AI engineering has traced over the past four years. This arc is not linear—it is a series of cycles: capability jump → old framework collapse → new abstraction emerges.

Recommended reading for additional background:

- AI Operating Systems: From Instructions to Intent
- From Prompt Engineering to Context Engineering
- The Token Naming Dilemma: When Information Theory Meets Linguistics
- OpenClaw: The Risks Behind the Hype
- Deep Dive: Google Workspace CLI
- Meta-Skills: Making AI Think Like You
- Reflections on Agent Trends: Native & CLI-First
- The AI Programming Ecosystem: What Anthropic's Acquisition of Bun Means
- Deep Thoughts: On AI Development Trends
- A Brief Look at AI Browsers
- Deep Dive: The Anthropic MCP Protocol
- Act One: Generation (Nov 2022 – 2023)

On November 30, 2022, ChatGPT launched. It reached approximately 100 million monthly active users within about two months. But what this event truly changed was not NLP technology—GPT-3 had already existed for two years—it was the interaction paradigm. Before this, an LLM was an API that only engineers could use; after this, it became a conversational interface that everyone could use.

The core contradiction in this act: the model could generate, but could not act. It could write an email but not send it; it could write code but not run it. The relationship between user and model was "you ask, I answer"—a stateless, single-turn, passive exchange of information.

The engineering artifact of this act was Prompt Engineering: how to ask so the model answers better. Few-shot, chain-of-thought, role-playing—all of these were essentially attempts to maximize information density within the limited space of a single API call.

## Act Two: Connection (2023 – 2024)

In March 2023, OpenAI released GPT-4, bringing multimodality and longer context windows. That same month, they launched ChatGPT Plugins, giving the model "hands" for the first time—it could call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool invocation as structured JSON within model output.

This was a pivotal turning point: the model evolved from "can speak" to "can connect." But the Plugins ecosystem quickly exposed its fragility—each plugin required its own OAuth flow, its own schema definition, its own error handling. Connecting 10 plugins was already painful; 100 was simply impossible.

In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with a layer of intermediate abstraction. It did lower the barrier to entry, but at the cost of over-abstraction—too many layers of wrapping, difficult debugging, unpredictable performance. Around the same time, projects like AutoGPT and BabyAGI attempted to let models autonomously loop through tasks, but all quickly faded after their demos due to the lack of reliable stopping conditions and verification mechanisms.

> 🤯 Lesson One
>
> Making a model "able to connect to tools" is necessary but far from sufficient. Connection is not orchestration, and orchestration is not governance.

## Act Three: Reasoning (2024)

2024 was the year "reasoning models" took the stage. OpenAI's o1 series launched in September, with "spend more time thinking before answering" as its defining characteristic, achieving a qualitative leap on math and programming tasks. In December, the ARC Prize announced that OpenAI o3 reached 87.5% on the ARC-AGI-1 Semi-Private Eval with a high-compute configuration, stunning the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet excelled at code generation and long-document comprehension, and DeepSeek-R1, as an open-weight model, proved that high-performance reasoning was no longer a closed-source monopoly.

More importantly, two things happened at the end of 2024:

**First: Anthropic released the Model Context Protocol (MCP).** This was not yet another plugin system, but an open standard protocol using JSON-RPC 2.0 to define how AI applications communicate with external tools and data sources. Its core insight: the connection problem is fundamentally an N×M problem—N AI applications × M data sources, with each combination requiring a custom connector. MCP simplified this to N+M: each application implements an MCP client once, each tool implements an MCP server once. OpenAI and Google DeepMind subsequently announced MCP support, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

**Second: Anthropic released the *Building Effective Agents*[1] guide (December 2024).** This article was the first to systematically discuss agent engineering patterns—from the simplest prompt chaining to the evaluator-optimizer loop—and explicitly articulated a principle: start with the simplest pattern, and only introduce more structure when complexity demonstrably yields better results. This principle later became one of the core guiding tenets of harness engineering.

By 2025, Anthropic further elevated context engineering into an independent engineering practice in *Effective context engineering for AI agents*[2], emphasizing that the real difficulty was no longer just "how to write a prompt" but "at each step, what information to give the model, in what form, and at what time." This is the critical transitional layer between Prompt Engineering and Harness Engineering—the problem has already shifted from "a single call" up to "per-step context," but has not yet shifted up to "the entire task outer loop."

> 🤯 Lesson Two
>
> A model's reasoning ability solves the "single-step quality" problem, but long-task reliability is not automatically achieved just because individual steps get smarter. A model that can solve IMO gold-medal problems will still "forget what it's doing" midway through a four-hour full-stack development task.

## Act Four: Action (2025)

If 2023 was the year of the Chatbot and 2024 was the year of Multimodal, then 2025 was the year of the Agent.

At the start of the year, the open-source release of DeepSeek-R1 forced the market to reassess the competitive landscape. Then came a wave of agent products: Claude Code (a coding agent in the terminal), GitHub Copilot Agent Mode, Cursor's autonomous coding loop, Manus (a browser-operation agent), OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all major languages. Google released the Agent2Agent (A2A) protocol to solve cross-vendor communication between agents.

But the most important discovery of 2025 was not what agents *can* do—it was how agents *fail* while doing it:

- An agent tries to complete the entire task in one pass ("all-in"), and runs out of context window halfway through.
- An agent announces "everything is done" after completing 70%, then stops.
- Multiple agents running in parallel produce cascading errors, where a single small mistake gets amplified into something undebuggable.
- After an agent works continuously on a codebase, severe "AI slop" appears—redundant code, inconsistent naming, outdated documentation.

These are not problems of model intelligence; they are problems of system structure.

> 🤯 Lesson Three
>
> Agent capability has reached the level of "can work autonomously for hours," but the engineering infrastructure around it is still stuck in the "single conversation" era. This rupture is the root cause of Harness Engineering's emergence.

## Act Five: Governance (2026 – Present)

At the start of 2026, the industry's attention began shifting from "how to make agents more capable" to "how to keep agents from crashing." "Harness Engineering" as a public term was not invented on any single day; rather, it rapidly coalesced and spread starting in February 2026:

- On February 5, 2026, Mitchell Hashimoto explicitly wrote "Engineer the Harness" in *My AI Adoption Journey*[3]—widely regarded as one of the starting points for the term's entry into mainstream discussion.
- On February 11, 2026, OpenAI published an engineering article titled *Harness Engineering: Leveraging Codex in an Agent-First World*[4]. A small team built an internal beta product from an empty repository in five months, publicly stating "zero lines of hand-written code." The repository reached approximately one million lines of code and produced roughly 1,500 PRs. More precisely, the initial scaffold was still generated by Codex under minimal template guidance; afterward, application logic, tests, CI, documentation, observability, and internal tools were produced by agents as much as possible. The core finding: engineers' focus shifted to **designing environments**, **specifying intent**, and **building feedback loops**.
- In March 2026, Anthropic released *Harness Design for Long-Running Application Development*, upgrading the earlier initializer/coding two-role architecture to a planner/generator/evaluator three-role system, demonstrating that the evaluator still delivers significant gains near the boundary of model capability.
- In April 2026, the Thoughtworks / Fowler lineage (*Harness Engineering - first thoughts*[5]) systematized the concept into a more complete methodological framework—a combination of guides (feedforward control) and sensors (feedback control), each subdivided into computational (deterministic) and inferential categories, forming a 2×2 control matrix. April is therefore better understood as "the methodological abstraction became complete" rather than "the first naming."

## What Exactly Is a Harness?

Let's derive this from first principles rather than starting from a definition.

### Five Fundamental Challenges of Agents

The essence of an agent is "a system that autonomously advances toward goals in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone:

**State Persistence**
- Essence: An agent needs to remember what it has done across time and across sessions.
- Why the model can't solve it: The model itself is stateless, the context window has an upper bound, and it cannot natively sustain long-term continuous state.

**Goal Consistency**
- Essence: In long tasks, agents tend to drift, go off on tangents, or even prematurely declare completion.
- Why the model can't solve it: The model lacks external anchor points and cannot stably calibrate "what actually counts as truly done."

**Action Verifiability**
- Essence: Every step is probabilistic; we need to distinguish "did it" from "did it correctly."
- Why the model can't solve it: When evaluating its own results, the model has a natural tendency toward self-congratulation and misjudgment.

**Entropy Suppression**
- Essence: Continuous output constantly accumulates redundancy, drift, and inconsistency.
- Why the model can't solve it: The model replicates existing patterns, even when those patterns are themselves bad or low-quality.

**Human-Machine Boundary**
- Essence: When to be autonomous and when to hand off to a human needs to be explicitly and engineeringly defined.
- Why the model can't solve it: The model does not have reliable "uncertainty self-awareness" and cannot stably judge when to stop and return control to a human.

A harness is the engineering practice that systematically addresses these five challenges.

### A Precise Definition

Anthropic provided a definition in *Demystifying evals for AI agents*[6] that is well worth adopting directly: an agent harness (or scaffold) is the system that enables a model to act as an agent; it handles inputs, orchestrates tool calls, and returns results. More critically, Anthropic further noted: when we evaluate "an agent," we are actually evaluating the combination of model + harness, not the model's capability in isolation. This definition is extremely important because it shifts the unit of explanation for agent effectiveness from model parameters to the outer-loop structure in which the model operates.

Image

We must disentangle a concept that is frequently conflated: an agent harness and an evaluation harness are not the same thing. The former is responsible for making the agent run (handling inputs, orchestrating tools, managing state); the latter is responsible for batch-running tasks, recording trajectories, executing graders, and aggregating scores. Many discussions lump "harness" into a catch-all bucket, sometimes talking about runtime orchestration and sometimes about evaluation pipelines. The Harness Engineering discussed in this article refers to the former—the engineering of the runtime outer-loop system.

Based on this, a more precise formulation:

> 📌
> Harness = the outer-loop system that enables a model to act as an Agent.
>
> It encompasses plan decomposition, durable state, tool orchestration, verification gates, feedback loops, rollback mechanisms, human handoff points, and audit logs. When evaluating an Agent's effectiveness, what is being evaluated is not the model itself, but the combination of model + harness.

Several points here deserve elaboration:

**The outer loop is the key word.** The model's reasoning is the "inner loop"—given context, generate the next step. The harness is the "outer loop"—deciding when to start a new inner loop, what context to give it, how to verify its output, when to roll back, when to stop. The quality of the inner loop depends on model capability; the quality of the outer loop depends on harness design.

**A harness is not an upgraded prompt.** A single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, or continuous entropy control. Treating a harness as "a longer system prompt" is the most common failure mode today.

**A harness is also not a framework name.** LangChain is a framework. CrewAI is a framework. Harness Engineering is not. It is a practice—just as DevOps is not a tool but an engineering culture.

### Three Layers of Engineering Abstraction

Prompt → Context → Harness

To understand where the harness sits, we first need to see its relationship to the two preceding layers. These three layers are not replacements for one another but progressive levels of abstraction:

Image

> 📌 Key Insight
>
> Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline runs." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; but the harness also encompasses multi-step structure, tool mediation, verification gates, and durable state—things that go beyond the scope of single-step context.

## The Six Engineering Components of a Harness

This section is the most substantive part of the article. For each component, we will explain what problem it solves, what Anthropic/OpenAI specifically do, and the design principles behind it.

### Durable State Surfaces: Keeping Agents from "Showing Up Amnesiac"

**Problem:** The core pain point of long-running agents is like an engineer on a project team who completely loses their memory at every shift change. The context window is finite, complex projects cannot be completed within a single window, and the agent needs a way to bridge the gap between sessions.

**Anthropic's solution:** Rather than attempting "infinitely long context," they externalized state into resumable artifacts:

- The first initializer agent sets up the environment: creates `init.sh` (startup script), `claude-progress.txt` (progress log), and an initial git commit (baseline snapshot).
- Generates a feature list: expands high-level requirements into 200+ specific features, all initially marked as failing.
- Each subsequent coding agent only makes incremental progress, leaving structured updates and a "clean state" at session end.
- Critical rule: agents can only change a feature's `passes` status; they cannot arbitrarily modify the test definitions themselves.

This feature list design looks "crude," but it is extremely effective—it transforms the definition of "done" from the agent's subjective feeling into an external, durable, structured, inheritable completion surface. The agent doesn't need to "remember" what was done before; it only needs to read the feature list and the git diff to resume within 30 seconds.

Anthropic later discovered a deeper problem: **context anxiety**. Even with compaction (summarizing and compressing earlier conversation), agents still degrade in behavior because they feel "the context is too full." The solution is not better compaction but **context reset**—giving the next agent an entirely fresh context and transmitting all necessary information through externalized state artifacts (rather than conversation history). This is more aggressive than compaction, but works better.

> 📌 Design Principle
>
> State ≠ "saving chat history." True durable state is a structured artifact that an agent can read, understand, and resume from after a cold start with zero context history. If your agent cannot determine "where did we leave off and what's next" within 30 seconds of a cold start, your state management has failed.

### Decomposition & Plans: Cutting Long Tasks into Agent-Sized Pieces

**Problem:** Tell an agent "build a clone of claude.ai" and it will try to do everything in a single pass—writing all the code in one session. The result is either the context explodes or it declares "done" halfway through.

**Evolution:**

- In November 2025, Anthropic initially solved this with an initializer + coding two-role structure. The initializer handles decomposition and initialization; the coding agent handles step-by-step implementation.
- In March 2026, this was upgraded to a planner / generator / evaluator three-role system:
  - The **Planner** does not write code directly; instead, it expands one or two high-level descriptions into a complete product spec and a step-by-step feature list.
  - The **Generator** implements features one by one, committing after each completion.
  - The **Evaluator** independently assesses the generator's output, marks pass/fail, and provides specific improvement suggestions.

OpenAI's counterpart is PLANS.md, Implement.md, Documentation.md—complex tasks are planned first, executed by milestone, verified at each stage, with documentation continuously updated as shared memory.

> 📌 Design Principle
>
> A plan must be elevated to a first-class artifact, not remain as one-off chat content. It needs to be written to the file system, version-controlled, readable by subsequent agents, and referenceable by verification gates. A plan that exists only in a conversation is not really a plan—it is just a thought.

### Feedback Loops: Guides and Sensors

**Problem:** An agent wrote code—how do we know it's correct? Rely on the agent's self-evaluation? Anthropic explicitly discovered an embarrassing fact: when asked to evaluate their own work, agents tend to enthusiastically praise themselves—even when the quality is obviously mediocre to human eyes.

This requires a feedback system that does not depend on the agent's self-evaluation. In April 2026, the community produced a framework that decomposed the harness into a very clear 2×2 matrix:

Image

**Guides** constrain the agent before it acts, increasing the probability of "getting it right the first time." **Sensors** provide signals after the agent acts, enabling self-correction.

Image

Key insights:

- Guides without sensors → the agent encodes rules but never knows whether they took effect.
- Sensors without guides → the agent repeatedly makes the same mistakes and then gets corrected.
- Computational control is cheap, fast, and deterministic—it can run on every change.
- Inferential control is expensive, slow, and non-deterministic, but can handle subjective judgments (e.g., "is this UI design too ugly?").

Anthropic's evaluator-optimizer pattern aligns perfectly with this. They also acknowledged a subtle fact: the evaluator is not always necessary—once the base model's capability crosses a certain threshold, the evaluator degrades from "essential component" to "extra overhead." This shows that a good harness is not a fixed template but a trimmable system that co-evolves with the boundary of model capability.

Image

### Legibility: Building a Perception Surface for Agents

**Problem:** An agent can write code now, but can it "see" what its code looks like when running? Can it read error logs? Can it understand performance metrics?

OpenAI offered an extremely sharp judgment in their harness engineering practice: **any knowledge not within the agent's runtime visible scope effectively does not exist.**

This is not rhetoric. They did the following concrete work to improve legibility:

- Launched an independent browser instance for each git worktree, using CDP (Chrome DevTools Protocol[7]) so the agent can "see" the UI.
- Exposed all logs, metrics, and traces for agent querying.
- Repository knowledge as a system of record: design principles, product intent, execution plans, known technical debt, architecture decision records (ADRs)—all placed in the repo and kept consistent via lint/CI.
- Placed AGENTS.md, structured docs/, execution plans, and knowledge documents in the repo as much as possible, making them a versioned system of record; but OpenAI also publicly warned: an overly long AGENTS.md rots quickly, crowds out context, and causes all constraints to lose focus simultaneously—a better approach is to turn it into a directory index, with actual knowledge distributed across structured documents.

> 📌 Design Principle
>
> Legibility is not "making code more elegant"—it is making knowledge, constraints, acceptance criteria, and decision history enter the agent's perception surface. This directly transforms "knowledge management" from a team collaboration problem into an agent executability problem. For an agent, experience in Slack, orally transmitted architectural boundaries, and constraints scattered across external documentation—if they don't enter the runtime-accessible artifact surface, they effectively do not exist.

### Tool Mediation: More Tools Means More Need for a Harness

**Problem:** After the MCP ecosystem exploded, a single agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions directly into context creates serious problems—token costs skyrocket, latency increases, and the agent loses its way in a sea of tools.

Anthropic proposed a core approach in their MCP + Code Execution engineering practice: **don't let the model call tools directly; let the model write code that calls tools.**

What's the difference?

- **Direct tool invocation mode:** All tool definitions loaded into context → model selects a tool → invokes it → result returns to context → model continues. Every step consumes context space; intermediate results stay in the model's inner loop.
- **Code execution mode:** Model writes a piece of code → code runs in a sandbox, discovering and invoking MCP tools as needed → only the final result returns to the model. Tool discovery, data filtering, and intermediate processing all happen inside the execution environment, never entering context.

The essence of this approach: move tool usage from the model's inner loop to a more efficient external execution loop. This is precisely harness engineering—it is not a "tool registry" but a system-level design that determines how tools are discovered, when they are exposed, at what granularity, whether results need to enter context, where state lives, and how failures roll back.

### Entropy Control: Continuous Garbage Collection for Agents

**Problem:** Fully autonomous agent codebases constantly replicate existing patterns—even when those patterns are uneven, suboptimal, or outright bad. Over time, drift and entropy accumulation are inevitable.

OpenAI was the most blunt about this: they initially relied on humans spending roughly 20% of their time each week cleaning up "AI slop" (redundant code, outdated documentation, inconsistent naming, copy-pasted dead code). They later systematized this cleanup logic:

- **Documentation consistency agents** periodically verify whether documentation matches code.
- **Refactor agents** clean up technical debt on schedule.
- **Architectural enforcement** mechanically maintains module boundaries through CI.

> 📌 Design Principle
>
> A harness is not only responsible for "getting the agent running" but also for continuously suppressing the system noise that agents amplify. This is the most fundamental distinction between a harness and a simple "agent framework"—a framework cares about startup and orchestration; a harness cares about long-term governability.

## Harnessability: Not Every System Is Equally Easy to Harness

If we understand Harness Engineering only as "add more rules and loops to the agent," we haven't gone deep enough. The more fundamental question is: not every system is equally easy to harness.

OpenAI's practice continually implies the same thing: the reason they could push Codex to high throughput is not just because the model is strong enough, but because they continuously compressed knowledge back into the repo, turned plans into artifacts, versioned decisions, and made the environment more legible to agents. How naturally suited a system is to being tamed by agents is itself an important variable.

Following this logic yields a highly explanatory judgment: systems with strong typing, comprehensive tests, clear boundaries, versioned documentation, and runtime observability naturally have higher harnessability; systems where knowledge is scattered across human brains, chat tools, and word of mouth will hit the wall of "invisible → incomprehensible → ungovernable" first, no matter how strong the model is.

This means that in the agent era, the quality of a team's engineering infrastructure (CI maturity, documentation structure, architectural boundary clarity) is no longer just a matter of "engineering discipline"—it directly determines how far an agent can go on your system. Harnessability will become a key dimension for evaluating a system's "agent-readiness."

## The Intent System

### A Deeper Paradigm Shift: From Instruction-Driven to Intent-Driven

What we've discussed above are the engineering components of a harness. But if we only look at components, we fall into "assembling technical details." Let's step back and discuss something more fundamental—why Harness Engineering is not just an engineering practice but the product of a paradigm shift.

### Four Ruptures in Human-Machine Interaction

Looking back at the entire history of computing, human-machine interaction has undergone four fundamental ruptures:

- **CLI (Command Line):** Humans must precisely master the machine's language. `ls -la | grep .py` is an instruction—get one character wrong and it fails. The core assumption of interaction is "humans adapt to machines."
- **GUI (Graphical Interface):** Machines lower the barrier through visual metaphors. Folders, desktops, drag-and-drop. The core assumption is "machines present themselves through metaphors humans can understand."
- **App (Mobile Applications):** Logic is solidified into fixed interfaces. One button per function, one screen per button. The core assumption is "humans choose within preset paths."
- **Agent (Intent-Driven):** Humans express only goals; the system autonomously plans execution paths. The core assumption is **"machines understand human intent and autonomously decide how to proceed."**

Each rupture is not merely a technology upgrade but a redistribution of control. In the CLI era, humans held 100% control; in the Agent era, humans have ceded most execution control, retaining only goal-setting and critical decision points.

What are the engineering consequences of this cession?

In an instruction-driven world, a bug is "the system didn't correctly execute my instruction"—coverable by traditional testing. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent but chose a poor execution path"—this requires an entirely new set of verification, constraint, and feedback mechanisms, which is precisely what the harness is designed to solve.

### Applications Are Being "CLI-ified," But Not for Humans

A highly counterintuitive trend: in the Agent era, all applications and websites are being re-"CLI-ified"—not to send users back to the terminal, but to turn everything into programmable interfaces from the Agent's perspective.

MCP is essentially the protocol-layer implementation of this. When an Agent needs to operate Google Drive, it doesn't need to "open a webpage and click buttons"—it needs a set of structured API calls. An MCP server abstracts Google Drive into a set of callable functions: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This implies three things:

**First, the audience for readability has changed.** Readability used to be for humans—clear UI, sensible information architecture. Now it must first be for Agents—structured APIs, machine-parseable documentation, programmable permission models.

**Second, application boundaries are dissolving.** When Agents call any tool via MCP and collaborate with other Agents via A2A, Apps degrade from "destinations" to "infrastructure." Users no longer "open an App to do one thing" but "express an intent, and the Agent orchestrates multiple services to fulfill it."

**Third, the harness becomes the new "operating system layer."** The OS in the GUI era managed windows, files, and processes. The Agent era needs to manage: agent lifecycles, tool discovery and authorization, context scheduling and reclamation, multi-agent collaboration and isolation, and human approval intervention points.

### From Chatbot to AgentOS

Connecting all the threads above reveals a clear evolutionary path. These three stages are not feature stacking but fundamental changes in the engineering abstraction layer:

**Level 1: Chatbot (2022–2023)**
Single conversation, stateless, human fully in the loop. Core value: information retrieval and content generation. Engineering abstraction layer: Prompt Engineering. Representative products: ChatGPT, Claude (early).

Ceiling: can speak but cannot act. Every conversation is isolated.

**Level 2: AI Browser / Agent IDE (2024–2025)**
Multi-step tasks, tool invocation, limited autonomy. Core value: task execution and workflow automation. Engineering abstraction layer: Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus, Codex.

Ceiling: single-agent capability is strong but long tasks are unstable; multi-agent collaboration lacks standards; state management is manual labor.

**Level 3: AgentOS (2026– nascent stage, forward-looking direction)**
We must write this with restraint. AgentOS is not yet a converged industry paradigm. But it has indeed entered the research and systems community agenda. The 2024 AIOS[8] paper proposed extracting scheduling, context management, memory management, and access control from the agent application layer into a kernel-like layer; ASPLOS 2026 featured a dedicated AgenticOS Workshop[9] exploring OS primitives for agent workloads.

Image

A more measured statement, therefore, is not "AgentOS has arrived" but: **Harness Engineering is pushing the problem from the application layer toward the systems layer.** When agents are no longer just coding assistants but always-on, multi-agent, cross-tool, cross-identity long-running execution entities, user-space harnesses will inevitably encounter deeper systems-level problems:

- **Agent lifecycle management:** initialization, running, suspension, resumption, termination—not stateless function calls but full process management.
- **Context scheduling:** The context window is a scarce resource; we need to decide what information to load when, when to compress, when to discard—this is the agent version of "memory management."
- **Multi-agent isolation and collaboration:** One agent's operations should not pollute another's environment, yet they need to share certain state—requiring mechanisms analogous to process isolation + IPC.
- **Governance and audit:** Every decision at every step of every agent must be traceable—in finance, healthcare, and similar domains, this is not a nice-to-have but a compliance requirement.

Image

> 📌 Key Positioning
>
> The harness is the user-space layer of AgentOS. AgentOS is the kernel—managing scheduling, isolation, and resources. The harness is the user-space shell and daemon—managing task decomposition, state resumption, verification feedback, and human handoff. The two are not competitors but natural upper and lower layers.

## Five Typical Symptoms

Theory aside, back to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are still in the improvised assembly stage. Here are five typical symptoms:

**Symptom One: Framework Jungle.** LangChain, CrewAI, AutoGen, Agno, n8n… each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to verification to rollback to audit. Users patch together across frameworks and get a fragile pipeline, not a governable system.

**Symptom Two: Chatbot Skin + Agent Core.** A large number of products are essentially a chatbot interface wrapped around an agent loop—but lacking true state management, task decomposition, and verification gates. Stunning in demos, constantly crashing in production.

**Symptom Three: Tool Registration ≠ Tool Governance.** MCP made connection easy, but "can connect" does not equal "knows how to use." An agent facing 50 tools gets confused, makes redundant calls, and takes detours. Engineering teams have found that initially providing agents with all tools actually produces worse results—performance improved only after trimming to the minimal necessary set.

**Symptom Four: One-off Rules vs. Evolvable Constraints.** Most teams' agent configuration is a giant AGENTS.md or system prompt. But practice shows this approach inevitably fails—when everything is important, nothing is important. Agents pattern-match locally rather than consciously navigating. Rules rot faster than humans can maintain them.

**Symptom Five: Lack of On-the-Loop Thinking.** "In the loop" means manually fixing output when dissatisfied with agent results; "on the loop" means modifying the harness so the system automatically produces better results next time. Most teams are still stuck in the loop—fixing errors one by one rather than systematically improving the control loops that produce them.

## What a Harness Is Not

Clarifying boundaries is as important as clarifying definitions.

**It is not "a longer system prompt."** Because a single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, or continuous entropy control.

**It is not a proprietary term from any single vendor.** Both Anthropic and OpenAI use it publicly, and academic preprints are already abstracting it into a cross-product universal concept.

**It is also not "won't be needed once models get stronger."** Quite the opposite—Anthropic explicitly noted that the harness redistributes value as the model boundary expands: certain checks become redundant, but planning, verification, handoff, and state governance for harder tasks become more important. The stronger the model, the more we need to place longer, more expensive, more dangerous tasks inside a controlled outer loop.

In fact, the space of interesting harness combinations does not shrink as models get stronger—it *moves*. An evaluator that is effective today may become redundant overhead in the face of the next generation of models, but new capability boundaries will spawn new harness requirements.

## Overlooked Critical Issues

### Testability of the Harness

When we say "the harness makes agents verifiable," a meta-question arises: how do we verify the harness itself? If the evaluator uses another LLM, and that LLM also has hallucination tendencies, we have built a loop of "verifying an unreliable system with an unreliable system."

Anthropic's approach is to use computational sensors (test suites, linters, type checkers) for foundational verification as much as possible, only enabling inferential sensors at the level of subjective judgment (UI aesthetics, code style). This is a pragmatic layered strategy, but not a perfect solution.

### Emergent Behavior in Multi-Agent Systems

When 10 agents run in parallel, each making independent decisions, system behavior exhibits emergent patterns that single-agent analysis cannot predict. This is analogous to concurrency bugs in distributed systems—but worse, because every "process" is non-deterministic. Current harness design primarily targets single-agent scenarios; harness principles for multi-agent collaboration have not yet been consolidated.

### Engineering Trade-offs: Cost and Latency

Every layer of the harness—planner, evaluator, sensor, garbage collection—consumes additional tokens and latency. When the harness's own overhead exceeds the quality improvement it delivers, that is over-engineering. How to measure harness ROI and how to dynamically adjust harness depth based on task complexity remain unsolved engineering problems.

### A New Dimension of Security: The Attack Target Shifts from Data to Agency

This is the layer most articles gloss over but is actually the most dangerous. As agents gain durable state, external tools, and long-running autonomy, the attack surface is no longer just "what did the model answer wrong" but "can the system be co-opted and manipulated."

Invariant Labs disclosed Tool Poisoning Attacks[10] in April 2025: malicious instructions can be hidden in MCP tool descriptions—invisible to users but visible to the model—thereby inducing agents to perform unauthorized operations. A week later, they demonstrated a data exfiltration scenario where an untrusted MCP server leveraged a trusted WhatsApp MCP. This means Harness Engineering cannot discuss only throughput and stability; it must also directly address tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation.

Image

MCP's open standardization is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connection becomes, the more the upper-layer harness must enforce stricter governance. The harness's permission model must evolve from static "can/cannot" to dynamic "under what conditions can, up to what limit can, only after human confirmation can." In other words, the harness is not only an outer loop for improving output—it is itself a new security boundary.

## Judgments & Outlook

**Judgment One: Harness Engineering will become one of the foundational disciplines of the AI engineering era.**

Improvements in model capability will continue to absorb some micro-level prompt techniques, but will not absorb harness engineering. Because it addresses higher-level problems: how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents need to work across time, across tools, across environments, and across human-machine boundaries, the harness will not disappear—it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

**Judgment Two: The center of gravity for competitive moats is shifting upward from model quality to harness and system design.**

When GPT, Claude, and Gemini converge on core capabilities, what determines product success is no longer model differentiation but harness quality. The hardest evidence comes from LangChain: without changing the underlying model, they improved deepagents-cli from 52.8% to 66.5% on Terminal Bench 2.0—a gain of 13.7 points—simply by modifying the harness, pulling their ranking from outside the Top 30 into the Top 5. This result should not be exaggerated into "models no longer matter," but it is sufficient to demonstrate: on top of the same model, the harness alone can create enormous system-level gaps. The center of gravity for competitive moats is shifting upward to harness and system design.

**Judgment Three: The migration from Chatbot to AgentOS will not happen in one step.**

There will be a 2–3 year "AI Browser + lightweight Harness" phase in between. Most enterprises will first capture value in this phase, then gradually evolve toward heavier AgentOS architectures. Teams that attempt to jump directly to AgentOS will in all likelihood fail because governance complexity exceeds their capacity to bear.

**Judgment Four: The engineer's role is shifting from "code producer" to "designer of autonomous systems."**

This is not an unemployment warning but a capability upgrade requirement. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing anomalies, consolidating rules—the value of these capabilities will rise sharply. When dissatisfied with agent output, the low-level approach is to manually fix the artifact; the high-level approach is to modify the harness so the system automatically does better next time. From in the loop to on the loop—this is the engineer's core upgrade path in the agent era.

## Appendix

Three self-check questions for practitioners. Before building your own harness, answer these three questions first:

1. Does your agent have **durable state surfaces**? Can it resume within 30 seconds of a cold start—or does it start from scratch every time?
2. Does your system have **machine-readable acceptance criteria**? Is the definition of "done" the agent's subjective feeling, or an external structured verification surface—a feature list, a set of test cases, a checkable pass/fail state?
3. Are your repo, tools, logs, metrics, and policies **legible and enforceable to the agent**? Or can only humans read them—leaving the agent to guess?

If none of these three things exist, what you've built is most likely still just "a chatbot that can run commands"…
