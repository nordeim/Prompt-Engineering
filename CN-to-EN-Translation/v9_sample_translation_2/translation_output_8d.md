**Background**

First, a preliminary question: how did we get to today?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, we must first see the complete arc that AI engineering has traversed over the past four years. This arc is not linear; it's a cycle of capability jumps, old framework collapses, and new abstractions emerging.

For further reading, here is some additional background material:

*   AI Operating System: From Instructions to Intent
*   From Prompt Engineering to Context Engineering
*   The Token Naming Dilemma: When Information Theory Collides with Linguistics
*   OpenClaw: The Hidden Risks of the Craze
*   Deep Dive: Google Workspace CLI
*   Meta-Skills: Making AI Think Like You
*   Agent Trends: Nativization & CLI-fication
*   AI Programming Ecosystem: What Does Anthropic's Acquisition of Bun Mean?
*   Deep Thoughts: Discussing AI Development Trends
*   A Brief Look at AI Browsers
*   Deep Dive: Anthropic's MCP Protocol

**Act One: Generation (Nov 2022 — 2023)**

On November 30, 2022, ChatGPT was launched. It reached approximately 100 million monthly active users in about two months. But what truly changed wasn't NLP technology—GPT-3 had existed for two years—but the interaction paradigm. Before this, the LLM was an API, only usable by engineers; after this, it became a conversational interface, usable by everyone.

The core contradiction in this act was: the model could generate, but it couldn't act. It could write an email but couldn't send it; it could write code but couldn't run it. The relationship between the user and the model was "you ask, I answer"—a stateless, single-turn, passive exchange of information.

The engineering product of this era was Prompt Engineering: how to ask the model to get a better answer. Few-shot, chain-of-thought, role-playing—all were essentially attempts to maximize information density within the limited space of a single API call.

**Act Two: Connection (2023 — 2024)**

In March 2023, OpenAI released GPT-4, bringing multimodality and a longer context window. That same month, they launched ChatGPT Plugins, allowing the model to "grow hands" for the first time—to call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool invocation as structured JSON in the model's output.

This was a critical turning point: the model evolved from "being able to speak" to "being able to connect." But the Plugin ecosystem quickly revealed its fragility—each plugin required a separate OAuth flow, a separate schema definition, and separate error handling. Connecting 10 plugins was painful; 100 was impossible.

In the second half of 2023, LangChain rose, attempting to solve the "connection" problem with an intermediate abstraction layer. It did lower the barrier to entry but also introduced the cost of over-abstraction—too many layers of wrapping, difficult debugging, and unpredictable performance. Around the same time, projects like AutoGPT and BabyAGI attempted to let models autonomously loop through tasks, but they quickly fizzled out after demos due to a lack of reliable stopping conditions and validation mechanisms.

🤯 **Lesson One**
Giving the model the "ability to connect to tools" was necessary, but far from sufficient. Connection is not orchestration, and orchestration is not governance.

**Act Three: Reasoning (2024)**

2024 was the year "Reasoning Models" debuted. OpenAI's o1 series, released in September, featured "taking more time to think before answering," achieving a qualitative leap in mathematics and programming tasks. In December, the ARC Prize announced that OpenAI's o3 achieved 87.5% on the ARC-AGI-1 Semi-Private Eval with high-compute configuration, shocking the community. Meanwhile, Anthropic's Claude 3.5 Sonnet excelled at code generation and long-document understanding, and DeepSeek-R1 proved as an open-weight model that high-performance reasoning was no longer a closed-source monopoly.

More importantly, two events occurred at the end of 2024:

**First:** Anthropic released the Model Context Protocol (MCP). This is not another plugin system but an open standard protocol that defines how AI applications communicate with external tools and data sources using JSON-RPC 2.0. Its core insight was: the connection problem is essentially an N×M problem—N AI applications × M data sources, each combination requiring a custom connector. MCP simplifies this to N+M: each application implements an MCP client once, and each tool implements an MCP server once. Later, OpenAI and Google DeepMind announced support for MCP, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

**Second:** Anthropic published the *Building Effective Agents* [1] guide (December 2024). This article systematically discussed engineering patterns for agents for the first time—from the simplest prompt chaining to evaluator-optimizer loops—and clearly proposed a principle: start with the simplest pattern, and only introduce more structure when complexity demonstrably yields better results. This principle later became one of the core guiding philosophies of harness engineering.

By 2025, Anthropic had also elevated context engineering to an independent engineering practice, *Effective context engineering for AI agents* [2], emphasizing that the real difficulty was no longer just "how to write a prompt" but "what information to give the model, in what form, and at what moment, at each step." This was a critical transitional layer from Prompt Engineering to Harness Engineering—the problem had moved from "single invocation" to "context at each step," but had not yet moved up to "the entire outer loop of the task."

🤯 **Lesson Two**
The model's reasoning ability solves the "single-step quality" problem, but the reliability of long-term tasks is not automatically gained because a single step is smarter. A model that can solve an IMO gold medal problem can still "forget what it's doing" halfway through a four-hour full-stack development task.

**Act Four: Action (2025)**

If 2023 was the year of Chatbots, 2024 was the year of Multimodality, then 2025 was the year of Agents.

Early in the year, the open-source release of DeepSeek-R1 prompted the market to reassess the competitive landscape. This was followed by a wave of agent products: Claude Code (a terminal-based programming agent), GitHub Copilot Agent Mode, Cursor's autonomous coding loop, Manus (a browser operation agent), and OpenAI Operator. The MCP ecosystem exploded, with thousands of MCP servers built by the community, and SDKs covering all major languages. Google released the Agent2Agent (A2A) protocol, addressing cross-vendor communication between agents.

But the most important discovery of 2025 was not what agents *could do*, but how they *broke down* while doing it:

*   Agents attempted to complete the entire task in one go (one-shot) and exhausted their context window halfway through.
*   Agents declared "task complete" after 70% completion and stopped.
*   Multiple agents running in parallel caused cascading errors, where a single small mistake was amplified to an undebuggable scale.
*   Codebases, after continuous work by agents, showed serious "AI slop"—redundant code, inconsistent naming, outdated documentation.

These were not intellectual problems of the model, but structural problems of the system.

🤯 **Lesson Three**
Agent capabilities have reached the level where they "can work autonomously for hours," but the engineering infrastructure surrounding them is still stuck in the era of "single conversations." This fracture is the root cause of Harness Engineering's birth.

**Act Five: Governance (2026 — Present)**

At the beginning of 2026, the industry's attention began shifting from "how to make agents more capable" to "how to keep agents from failing." "Harness Engineering," as a public term, wasn't invented overnight but began to rapidly coalesce and spread starting in February 2026:

*   **February 5, 2026:** Mitchell Hashimoto, in *My AI Adoption Journey* [3], explicitly wrote "Engineer the Harness"—considered one of the starting points for the term's entry into mainstream discussion.
*   **February 11, 2026:** OpenAI published an engineering article directly titled *Harness Engineering: Leveraging Codex in an Agent-First World* [4]. They detailed how a small team built an internal beta product from an empty repository in five months, with a public statement of "zero lines of human-written code." The repository reached approximately one million lines of code and generated about 1,500 PRs. More precisely, the initial scaffold was generated by Codex under the guidance of a small number of templates, after which application logic, tests, CI, documentation, observability, and internal tools were produced by agents as much as possible. The core finding: engineers' focus shifted to designing environments, specifying intent, and building feedback loops.
*   **March 2026:** Anthropic released *Harness Design for Long-Running Application Development*, upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, demonstrating that evaluators still brought significant gains near the model's capability boundaries.
*   **April 2026:** The Thoughtworks / Fowler ecosystem (*Harness Engineering - first thoughts* [5]) systematized the concept into a more complete methodological framework—guides (feedforward control) and sensors (feedback control), each divided into computational (deterministic) and inferential (inferential) types, forming a 2×2 control matrix. Thus, April is better understood as the moment "methodological abstraction became complete," rather than "the first naming."

**What Exactly is a Harness?**

Let's derive it from first principles, rather than from a definition.

**The Five Fundamental Challenges of Agents**

The essence of an agent is "a system that autonomously pursues goals in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone:

1.  **Durable State**
    *   *Nature:* Agents need to remember what they've done across time and sessions.
    *   *Why the model can't solve it:* The model itself is stateless; the context window has an upper limit, and it cannot naturally assume long-term continuous state.
2.  **Goal Consistency**
    *   *Nature:* In long tasks, agents are prone to drift, get distracted, or even prematurely declare completion.
    *   *Why the model can't solve it:* The model lacks external anchors to stably calibrate "what truly counts as complete."
3.  **Action Verifiability**
    *   *Nature:* Each step is probabilistic; we need to distinguish between "done" and "done correctly."
    *   *Why the model can't solve it:* The model has a natural tendency towards self-praise and misjudgment when evaluating its own results.
4.  **Entropy Suppression**
    *   *Nature:* Continuous output continuously accumulates redundancy, drift, and inconsistency.
    *   *Why the model can't solve it:* Models copy existing patterns, even if those patterns are bad or of low quality.
5.  **Human-AI Boundary**
    *   *Nature:* When to act autonomously and when to hand over to a human needs to be clearly and engineeringly defined.
    *   *Why the model can't solve it:* The model has no reliable sense of "uncertainty" and cannot stably judge when to stop and return control to a human.

A Harness is the engineering practice of systematically addressing these five challenges.

**A Precise Definition**

Anthropic, in *Demystifying evals for AI agents* [6], gives a definition well worth adopting directly: an agent harness (or scaffold) is the system that enables a model to act as an agent; it is responsible for handling input, orchestrating tool calls, and returning results. More crucially, Anthropic further points out that when we evaluate "an agent," we are actually evaluating the combination of **model + harness**, not the model's capabilities alone. This definition is very important because it shifts the unit of explanation for agent performance from the model's parameters to the outer-loop structure the model is embedded in.

Image

It is critical to disentangle a frequently confused concept here: **agent harness** and **evaluation harness** are not the same thing. The former is responsible for making the agent run (handling input, orchestrating tools, managing state). The latter is responsible for running tasks in batch, recording trajectories, executing graders, and aggregating scores. Much discussion lumps "harness" into one big basket, leading to confusion—one moment talking about runtime orchestration, the next about evaluation pipelines. The Harness Engineering discussed in this article refers to the former—the engineering of the runtime outer-loop system.

Based on this, a more precise formulation is:

📌
**Harness = The outer-loop system that enables a model to act as an Agent.**

It includes plan decomposition, persistent state, tool orchestration, validation gateways, feedback loops, fallback mechanisms, human-AI handoff points, and audit logs. Evaluating an Agent's performance means evaluating the combination of model + harness, not the model itself.

Several points here are worth expanding on:

*   **Outer loop** is the key word. The model's reasoning is the "inner loop"—given a context, generate the next step. The Harness is the "outer loop"—deciding when to start a new inner loop, what context to provide it, how to verify its output, when to fall back, and when to stop. The quality of the inner loop depends on the model's capabilities; the quality of the outer loop depends on the harness design.
*   A **Harness is not an upgraded prompt**. A single prompt cannot solve cross-session state, validation gateways, tool discovery, failure recovery, and continuous entropy control. Treating a Harness as "a longer system prompt" is the most common failure mode today.
*   A **Harness is also not a framework name**. LangChain is a framework, CrewAI is a framework; Harness Engineering is not. It's a practice, just as DevOps is not a tool but an engineering culture.

**Three Layers of Engineering Abstraction**

Prompt → Context → Harness

To understand the position of Harness, we must first see its relationship with the previous two layers. These three layers are not substitutions, but progressive levels of abstraction:

Image

📌 **Key Insight**
Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline operates." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; but the harness also includes multi-step structure, tool mediation, validation gateways, and durable state—these go beyond the scope of single-step context.

**The Six Engineering Components of a Harness**

This section is the most hardcore part of the article. Each component will clarify what problem it solves, Anthropic/OpenAI's specific approaches, and the underlying design principles.

**Durable State Surfaces: Stop Agents from "Coming to Work with Amnesia"**

*   **Problem:** The core pain point for long-running agents is like an engineer on a project team who completely loses memory every time they start a new shift. The context window is limited; complex projects cannot be completed in a single window. The agent needs a way to bridge the gap between sessions.

*   **Anthropic's Solution:** Instead of attempting to create an "infinitely long context," they externalized state into resume-able artifacts:

    1.  An initializer agent sets up the environment: creates `init.sh` (startup script), `claude-progress.txt` (progress log), and an initial git commit (baseline snapshot).
    2.  Generates a feature list: expands high-level requirements into 200+ specific features, all initially marked as failing.
    3.  Each subsequent coding agent only makes incremental progress, leaving structured updates and a "clean state" at the end of the session.
    4.  **Critical rule:** Agents can only change the `passes` status of a feature; they cannot arbitrarily modify the test definitions themselves.

    This feature list design seems "old school," but is extremely effective—it turns the definition of "done" from the agent's subjective feeling into an external, durable, structured, inheritable completion surface. The agent doesn't need to "remember" what it did before; it only needs to read the feature list and `git diff` to resume its work within 30 seconds.

    Anthropic later discovered a deeper issue: **context anxiety**. Even with compaction (summarizing early conversation history), agents still degraded behaviorally because they *felt* the context was "too full." The solution wasn't better compaction, but **context reset**—giving the next agent a completely fresh context, passing all necessary information through externalized state artifacts (not conversation history). This is more aggressive than compaction, but more effective.

📌 **Design Principle**
State ≠ "Saving the chat history." True durable state is a structured artifact that an agent can read, understand, and resume from after a cold start, without any historical context. If your agent cannot know "where it left off and what to do next" within 30 seconds of a cold start, your state management is failing.

**Decomposition & Plans: Breaking Long Tasks into Agent-Sized Chunks**

*   **Problem:** Tell an agent to "build a clone of claude.ai," and it will try to do it all at once—write all the code in a single session. The result is either the context explodes or it declares completion halfway through.

*   **Evolutionary Process:**

    *   In November 2025, Anthropic initially solved this with an initializer + coding two-role structure. The initializer handled decomposition and setup, while the coder handled step-by-step implementation.
    *   In March 2026, this was upgraded to a **planner / generator / evaluator** three-role system:
        *   The Planner doesn't write code directly but expands a high-level description into a complete product spec and a step-by-step feature list.
        *   The Generator is responsible for implementing features one by one, committing after each.
        *   The Evaluator independently assesses the Generator's output, marking pass/fail and providing specific improvement suggestions.

    OpenAI's counterpart is `PLANS.md`, `Implement.md`, `Documentation.md`—complex tasks are first planned, then executed milestone by milestone, with validation at each stage, and documentation is continuously updated as shared memory.

📌 **Design Principle**
Plans must be elevated to first-class artifacts, not one-off chat content. They need to be written to the filesystem, version-controlled, readable by subsequent agents, and referenced by validation gateways. A plan that exists only in a conversation is not a plan—it's just an idea.

**Feedback Loops: Guides and Sensors**

*   **Problem:** The agent writes code. How does it know if it's correct? Rely on the agent to evaluate itself? Anthropic explicitly discovered an awkward fact: when asked to evaluate its own work, the agent tends to enthusiastically praise itself—even when a human would judge the quality as mediocre.

    This requires a feedback system that doesn't depend on the agent's self-evaluation. By April 2026, there were frameworks that decomposed the harness into a very clear 2×2 matrix:

Image

**Guides** constrain the agent *before* it acts, increasing the probability of "getting it right the first time." **Sensors** provide signals *after* the agent acts, supporting self-correction.

Image

**Key Insights:**

*   Guides without sensors → agent encodes rules but never knows if they are effective.
*   Sensors without guides → agent repeats the same mistakes and is corrected repeatedly.
*   Computational control is cheap, fast, deterministic, and can run on every change.
*   Inferential control is expensive, slow, non-deterministic, but can handle subjective judgments (e.g., "Is this UI design too ugly?").

Anthropic's evaluator-optimizer pattern is entirely consistent with this. They also acknowledge a subtle fact: the evaluator is not *always* necessary—once the underlying model's capabilities cross a certain threshold, the evaluator degrades from a "necessary component" to "overhead." This shows that a good harness is not a fixed template but a system that co-evolves with the model's capability boundaries and can be trimmed accordingly.

Image

**Legibility: Building Perception Surfaces for Agents**

*   **Problem:** The agent can write code, but can it "see" the code it wrote running? Can it read error logs? Understand performance metrics?

*   **OpenAI's Practice:** In their harness engineering practice, OpenAI made a remarkably sharp judgment: **knowledge that is not visible within the agent's runtime environment, doesn't exist.**

    This isn't rhetoric. They did the following specific work to improve legibility:

    1.  Spawn an independent browser instance for each git worktree via CDP (Chrome DevTools Protocol [7]), allowing the agent to "see" the UI.
    2.  Expose logs, metrics, and traces to the agent for querying.
    3.  Treat **Repository Knowledge as the System of Record**: design principles, product intent, execution plans, known technical debt, and architecture decision records (ADRs) are all placed in the repo and maintained with lint/CI.
    4.  Place `AGENTS.md`, structured `docs/`, execution plans, and knowledge documents into the repo as much as possible, making them versioned systems of record. However, OpenAI also publicly warns: overly long `AGENTS.md` files rot quickly, crowd out context, and defocus all constraints simultaneously—a better approach is to make it a directory index, with the real knowledge distributed in structured documents.

📌 **Design Principle**
Legibility is not "making code more elegant." It's about bringing knowledge, constraints, acceptance criteria, and decision history into the agent's perception surface. This directly transforms "knowledge management" from a team collaboration problem into an agent-executable problem. For an agent, experience shared in Slack, tacit architectural boundaries, and constraints scattered in external documents—if they don't enter the runtime-accessible artifact surface—simply do not exist.

**Tool Mediation: More Tools Mean More Harness Is Needed**

*   **Problem:** After the MCP ecosystem exploded, an agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions into the context creates serious problems—soaring token costs, increased latency, and the agent losing its way in a sea of tools.

*   **Anthropic's Approach:** In their engineering practice with MCP + Code Execution, they proposed a core idea: don't let the model call tools directly; let the model write code to call tools.

    What's the difference?

    *   **Direct Tool Call Mode:** All tool definitions are loaded into context → the model selects a tool → makes the call → results are passed back into context → the model continues. Each step consumes context space, and intermediate results cycle within the model's inner loop.
    *   **Code Execution Mode:** The model writes code → the code runs in a sandbox, discovering and calling MCP tools on demand → only the final result is passed back to the model. Tool discovery, data filtering, and intermediate processing all happen within the execution environment, not in the context.

    The essence of this idea is: move tool usage from the model's inner loop to a more efficient external execution loop. This is precisely harness engineering—it's not a "tool registry" but a system-level design that determines how tools are discovered, when they are exposed, at what granularity, whether results need to enter context, where state is stored, and how failures are handled.

**Entropy Control: Continuous Garbage Collection for Agents**

*   **Problem:** A fully automated agent codebase continuously copies existing patterns—even if those patterns are uneven, suboptimal, or even bad. Over time, drift and entropy increase inevitably.

*   **OpenAI's Approach:** They stated it most bluntly: initially, humans spent about 20% of their week cleaning up "AI slop" (redundant code, outdated documentation, inconsistent naming, copy-pasted dead code). They later systematized this cleanup logic:

    *   **Documentation consistency agents** regularly verify that documentation matches the code.
    *   **Refactor agents** clean up technical debt according to a plan.
    *   **Architectural enforcement** mechanistically maintains module boundaries through CI.

📌 **Design Principle**
The harness is not only responsible for "getting the agent running" but also for continuously suppressing the system noise amplified by the agent. This is the most essential difference between it and a simple "agent framework"—the framework cares about startup and orchestration; the harness cares about long-term maintainability.

**Harnessability: Not Every System is Equally Easy to Harness**

If we only understand Harness Engineering as "adding more rules and loops to the agent," we're not going deep enough. A more fundamental question is: not every system is equally easy to harness.

OpenAI's practice subtly implies the same thing: their ability to push Codex to high throughput was not only because the model was powerful enough, but also because they continuously pushed knowledge back into the repo, artifacted plans, versioned decisions, and made the environment more legible to the agent. How naturally suitable a system is for being tamed by an agent is itself an important variable.

Following this logic leads to a highly explanatory judgment: systems that are strongly typed, well-tested, have clear boundaries, have versioned documentation, and are observable at runtime are inherently more *harnessable*; while systems where knowledge resides in human brains, chat tools, and word-of-mouth, even with a powerful model, will hit a wall of "invisible → incomprehensible → ungovernable."

This means that in the age of agents, a team's engineering infrastructure quality (CI completeness, documentation structure, clarity of architectural boundaries) is no longer just an "engineering hygiene" issue—it directly determines how far an agent can go on your system. Harnessability will become a key dimension for evaluating a system's "agent-readiness."

**The Intent System**

A Deeper Paradigm Shift: From Instruction-Driven to Intent-Driven

The above covers the engineering components of the Harness. But if we only look at the components, we fall into the trap of "stitching together technical details." Let's step back and talk about something more fundamental—why Harness Engineering is not just an engineering practice but a product of a paradigm shift.

**The Four Great Fractures in Human-Computer Interaction**

Looking back at the entire history of computing, human-machine interaction has undergone four fundamental fractures:

1.  **CLI (Command Line):** Humans must precisely master the machine's language. `ls -la | grep .py` is an instruction; a single wrong character and it doesn't work. The core assumption is "humans adapt to the machine."
2.  **GUI (Graphical User Interface):** The machine lowers the barrier through visual metaphors: folders, desktops, drag-and-drop. The core assumption is "the machine presents itself using metaphors humans understand."
3.  **Apps (Mobile Applications):** Logic is solidified into fixed interfaces. One function per button, one screen per button. The core assumption is "humans choose from preset paths."
4.  **Agents (Intent-Driven):** Humans only express goals; the system autonomously plans the execution path. The core assumption is "the machine understands human intent and decides autonomously how to proceed."

Each fracture is not just a technological upgrade but a redistribution of control. In the CLI era, humans had 100% control; in the Agent era, humans cede most execution control, retaining only goal setting and key decision points.

What are the engineering consequences of this ceding?

In an instruction-driven world, a bug is "the system didn't correctly execute my instruction"—which can be covered by traditional testing. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent but chose a poor execution path"—which requires a completely new set of validation, constraint, and feedback mechanisms. This is precisely the problem the Harness is designed to solve.

**Applications are Being "CLI-fied," But Not for Humans**

A very counter-intuitive trend: in the Agent era, all applications and websites are being re-"CLI-fied"—not to bring users back to the terminal, but to turn everything into a programmable interface from the Agent's perspective.

MCP is the protocol-layer implementation of this. When an Agent needs to operate Google Drive, it doesn't need to "open a webpage and click a button"—it needs a set of structured API calls. The MCP server abstracts Google Drive into a set of callable functions: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This means three things:

1.  **The target audience for readability has changed.** In the past, readability was for humans—clear UI, reasonable information architecture. Now, it's primarily for Agents—structured APIs, machine-parsable documentation, programmable permission models.
2.  **The boundaries of applications are dissolving.** When Agents call any tool via MCP and collaborate with other Agents via A2A, Apps degrade from "destinations" to "infrastructure." Users no longer "open an App to do one thing" but rather "express an intent, and an Agent orchestrates multiple services to fulfill it."
3.  **Harness becomes the new "Operating System layer."** The OS of the GUI era managed windows, files, and processes. The Agent era needs to manage: Agent lifecycles, tool discovery and authorization, context scheduling and reclamation, multi-agent collaboration and isolation, and human approval checkpoints.

**From Chatbot to AgentOS**

Connecting all the threads above reveals a clear evolutionary path. These three stages are not feature additions but fundamental changes in engineering abstraction layers:

*   **Level 1: Chatbot (2022-2023)**
    *   Single-turn conversation, stateless, human fully in the loop.
    *   Core value: information retrieval and content generation.
    *   Engineering abstraction layer: Prompt Engineering.
    *   Representative products: ChatGPT, Claude (early).
    *   Ceiling: Can speak but can't act. Each conversation is isolated.

*   **Level 2: AI Browser / Agent IDE (2024-2025)**
    *   Multi-step tasks, tool calls, limited autonomy.
    *   Core value: task execution and workflow automation.
    *   Engineering abstraction layer: Context Engineering + Lightweight Harness.
    *   Representative products: Claude Code, Cursor, Manus, Codex.
    *   Ceiling: Single agent is capable, but long-term tasks are unstable; multi-agent collaboration lacks standards; state management is manual work.

*   **Level 3: AgentOS (2026 — Emergent, Forward-looking)**
    *   This must be written cautiously. AgentOS is not yet a converged industrial paradigm. However, it has indeed entered the research and systems community agenda. The 2024 AIOS [8] paper proposed abstracting scheduling, context management, memory management, access control, and other issues from the agent application layer to a kernel-like layer. ASPLOS 2026 has a dedicated AgenticOS Workshop [9] exploring OS primitives for agent workloads.

Image

Therefore, a safer statement is not "AgentOS has arrived," but: **Harness Engineering is pushing issues from the application layer towards the system layer.** When an agent is no longer just a coding assistant, but an always-on, multi-agent, cross-tool, cross-identity, long-running execution entity, the userspace harness will inevitably encounter more fundamental system issues:

*   **Agent Lifecycle Management:** Initialization, running, suspension, resumption, termination—not stateless function calls, but full process management.
*   **Context Scheduling:** The context window is a scarce resource; decisions need to be made about what information is loaded when, compressed when, and discarded when—this is the agent version of "memory management."
*   **Multi-Agent Isolation and Collaboration:** One agent's operations shouldn't pollute another's environment, but they also need to share certain states—requiring mechanisms similar to process isolation + IPC.
*   **Governance and Audit:** Every step of every agent's decisions must be traceable—in finance and healthcare, this is not just a nice-to-have, but a compliance requirement.

Image

📌 **Key Positioning**
Harness is the userspace layer of AgentOS. AgentOS is the kernel—managing scheduling, isolation, and resources. Harness is the userspace shell and daemon—managing task decomposition, state resumption, validation feedback, and human-AI handoffs. They are not in competition but are natural upper and lower layers.

**Five Typical Symptoms**

Theory discussed. Let's return to reality. Observing the current ecosystem, most so-called "agent systems" are still in a temporary, ad-hoc stage. Here are five typical symptoms:

1.  **Symptom One: Framework Jungle.** LangChain, CrewAI, AutoGen, Agno, n8n... each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to validation to rollback to audit. Users cobble together different frameworks, resulting in a fragile pipeline, not a governable system.

2.  **Symptom Two: Chatbot Skin, Agent Core.** Many products are essentially a chatbot interface wrapped around an agent loop—but lack real state management, task decomposition, and validation gateways. They are impressive in demos but frequently fail in production.

3.  **Symptom Three: Tool Registration ≠ Tool Governance.** MCP makes connection easy, but "can connect" doesn't mean "will use effectively." An agent confronted with 50 tools becomes confused, makes redundant calls, and takes inefficient paths. Engineering teams have found that initially giving the agent all tools actually hurts performance—improvement only came after trimming down to a minimal necessary set.

4.  **Symptom Four: One-Time Rules vs. Evolvable Constraints.** Most teams' agent configuration is a giant `AGENTS.md` or system prompt. But practice shows this approach inevitably fails—when everything is important, nothing is. The agent operates on local pattern matching, not conscious navigation. Rules rot faster than humans can maintain them.

5.  **Symptom Five: Lack of On-the-Loop Thinking.** "In the loop" means manually modifying the product when unsatisfied with the agent's output. "On the loop" means changing the harness so the system automatically produces better results next time. Most teams are still stuck in the loop—fixing errors one by one instead of systematically improving the control loop that generates the errors.

**What a Harness is Not**

Clarifying the boundaries is as important as clarifying the definition.

*   It is **not** "a longer system prompt." A single prompt cannot solve cross-session state, validation gateways, tool discovery, failure recovery, and continuous entropy control.
*   It is **not** a proprietary term of any single vendor. Anthropic and OpenAI both use it publicly, and academic preprints are already abstracting it into a cross-product, general-purpose concept.
*   It is **not** something "that becomes unnecessary when the model gets stronger." Quite the opposite—Anthropic explicitly notes that the harness will reallocate value as model boundaries shift: some checks become redundant, but planning, validation, handoffs, and state governance for more difficult tasks become even more critical. The stronger the model, the more it needs longer, more expensive, and more dangerous tasks placed in a controlled outer loop.

In fact, the space of interesting harness combinations will not shrink as the model gets stronger—it will move. An evaluator that is effective today might become redundant overhead for the next generation of models, but the new capability boundaries will spawn new harness requirements.

**Crucial Overlooked Issues**

*   **Testability of the Harness**
    When we say "the harness makes the agent verifiable," a meta-question is: how do we verify the harness itself? If the evaluator uses another LLM, and that LLM also has a tendency to hallucinate, we've built a loop of "using an unreliable system to verify an unreliable system." Anthropic's approach is to use computational sensors (test suites, linters, type checking) for basic verification whenever possible, and only employ inferential sensors for subjective judgments (UI aesthetics, code style). This is a pragmatic, layered strategy, but not a perfect solution.

*   **Emergent Behavior in Multi-Agent Systems**
    When 10 agents run in parallel, each making independent decisions, the system behavior will exhibit patterns that analysis of individual agents cannot predict. This is similar to concurrency bugs in distributed systems—but worse, because each "process" is non-deterministic. Current harness design primarily targets single-agent scenarios; harness principles for multi-agent collaboration have not yet been codified.

*   **Engineering Trade-offs between Cost and Latency**
    Every layer of the harness—planner, evaluator, sensors, garbage collection—consumes extra tokens and latency. When the harness's own overhead exceeds the quality improvement it brings, that's over-engineering. How to measure the ROI of the harness and how to dynamically adjust its depth based on task complexity is an as-yet unsolved engineering problem.

*   **A New Security Dimension: The Target Shifts from Data to Agency**
    This is the most dangerous layer that many articles tend to gloss over. As agents gain durable state, external tools, and long-term autonomy, the attack surface is no longer just "what the model answered incorrectly," but "can the system be manipulated."

    In April 2025, Invariant Labs disclosed Tool Poisoning Attacks [10]: malicious instructions can be hidden in MCP tool descriptions, invisible to users but visible to the model, inducing the agent to perform unauthorized actions. A week later, they demonstrated a data exfiltration scenario where an untrusted MCP server could be chained with a trusted WhatsApp MCP server. This means Harness Engineering cannot only talk about throughput and stability; it must also directly address tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation.

Image
    MCP's open standardization is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connections are, the more they demand stricter governance from the upper-layer harness. The harness's permission model must be upgraded from a static "can/cannot" to a dynamic "under what conditions, to what extent, and only after human confirmation." In other words, the harness is not just an outer loop for improving output; it is itself a new security boundary.

**Judgment & Outlook**

*   **Judgment One: Harness Engineering will become one of the foundational disciplines of the AI Engineering era.**
    Model capability improvements will continue to subsume some micro-prompting techniques, but they will not subsume harness engineering. Because it deals with a higher-level problem: how to embed an unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents need to work across time, tools, environments, and human-machine boundaries, the harness will not disappear—it will increasingly resemble an intersection of software architecture, testing engineering, SRE, and security engineering.

*   **Judgment Two: The center of gravity for moats is shifting from model quality to Harness and System Design.**
    As GPT, Claude, and Gemini converge in core capabilities, the differentiator for product success is no longer the model, but the quality of the harness. The most compelling evidence comes from LangChain: while keeping the underlying model unchanged, they improved deepagents-cli on Terminal Bench 2.0 from 52.8% to 66.5%—a 13.7-point gain—simply by modifying the harness, vaulting from the periphery of the Top 30 to the Top 5. This result cannot be exaggerated as "the model no longer matters," but it sufficiently demonstrates that, on top of the same model, the harness is enough to create a huge system gap. The center of gravity for the moat is shifting upward, to harness and system design.

*   **Judgment Three: The migration from Chatbot to AgentOS will not happen in one leap.**
    There will be a 2-3 year intermediate phase of "AI Browser + Lightweight Harness." Most enterprises will gain value in this phase first, then gradually evolve towards heavier AgentOS architectures. Teams that attempt to jump straight to AgentOS will likely fail because governance complexity exceeds their capacity.

*   **Judgment Four: The engineer's role is evolving from "code producer" to "designer of autonomous systems."**
    This is not a warning of unemployment, but a demand for capability upgrades. Defining intent, shaping the environment, setting boundaries, designing feedback, absorbing exceptions, and codifying rules—the value of these skills will rise dramatically. When unsatisfied with the agent's output, the lower-level approach is to manually modify the product; the higher-level approach is to change the harness so the system automatically does better next time. From *in the loop* to *on the loop*—this is the core upgrade path for engineers in the agent era.

**Appendix**

Three self-assessment questions for practitioners. Before you start building your own harness, answer these three questions:

1.  Does your agent have **durable state surfaces**? Can it resume within 30 seconds of a cold start—or does it start from scratch every time?
2.  Does your system have **machine-readable acceptance criteria**? Is the definition of "done" based on the agent's subjective feeling, or an external, structured verification surface—a feature list, a set of test cases, a checkable pass/fail state?
3.  Are your repo, tools, logs, metrics, and policies **legible and enforceable** to the agent? Or are they only readable by humans—forcing the agent to guess?

If you don't have these three things, what you're building is most likely still just a "chatbot that can run commands"...
