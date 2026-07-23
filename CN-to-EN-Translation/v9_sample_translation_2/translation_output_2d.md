Background
Let's start with a preliminary question: how did we get here?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, you must first see the full arc AI engineering has traveled over the past four years. That arc isn't linear; it's a series of cycles: capability leaps → old frameworks collapse → new abstractions emerge.

Recommended reading for additional context:

AI Operating Systems: From Commands to Intent
From Prompt Engineering to Context Engineering
The Token Naming Dilemma: When Information Theory Stumbles into Linguistics
OpenClaw: The Hidden Dangers Behind the Madness
Deep Dive: Google Workspace CLI
Meta-Skills: Teaching AI to Think Like You
Thoughts on Agent Trends: Native and CLI
AI Coding Ecosystem: What Anthropic's Acquisition of Bun Means
Deep Thinking: A Discussion on AI Development Trends
A Brief Talk on AI Browsers
Deep Dive: Anthropic MCP Protocol
Act 1: Generation (2022.11 – 2023)
On November 30, 2022, ChatGPT launched. It reached roughly 100 million monthly active users about two months later. But what truly changed was not NLP technology—GPT-3 had already existed for two years—but the interaction paradigm. Before this, an LLM was an API, usable only by engineers; afterward, it became a conversational interface, accessible to everyone.

The core contradiction in this act: the model could generate, but could not act. It could write an email, but couldn't send it; could write code, but couldn't run it. The relationship between user and model was "you ask, I answer"—a stateless, single-turn, passive exchange of information.

The engineering product of this era was Prompt Engineering: how to ask so that the model answers better. Few-shot, chain-of-thought, role-playing—all, at their core, were attempts to maximize information density within the limited space of a single API call.

Act 2: Connection (2023 – 2024)
In March 2023, OpenAI released GPT-4, bringing multimodality and a longer context window. That same month, ChatGPT Plugins were introduced, giving the model "hands" for the first time—it could call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool use as structured JSON within the model's output.

This was a critical turning point: the model evolved from "able to speak" to "able to connect." But the Plugins ecosystem quickly exposed its fragility—each plugin required an independent OAuth flow, an independent schema definition, independent error handling. Connecting ten plugins was already painful; a hundred was impossible.

In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with a layer of intermediate abstraction. It indeed lowered the barrier to entry, but it also introduced the cost of over-abstraction—too many layers of wrapping, difficult debugging, unpredictable performance. Around the same time, projects like AutoGPT and BabyAGI tried to let the model autonomously loop through tasks, but all quickly faded after demos because they lacked reliable stopping conditions and verification mechanisms.

🤯 Lesson 1
Giving the model "the ability to connect to tools" is necessary but far from sufficient. Connection does not equal orchestration, and orchestration does not equal governance.

Act 3: Reasoning (2024)
2024 was the year "reasoning models" took the stage. OpenAI's o1 series, released in September, featured "spending more time thinking before answering" as its core trait, achieving a qualitative leap in math and programming tasks. In December, the ARC Prize announced that OpenAI o3, in a high-compute configuration, achieved 87.5% on the ARC-AGI-1 Semi-Private Eval, shocking the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet excelled at code generation and long-document understanding, and DeepSeek-R1, as an open-weight model, proved that high-performance reasoning was no longer a closed-source monopoly.

More importantly, two events at the end of 2024:

First: Anthropic released the Model Context Protocol (MCP). This was not just another plugin system; it was an open standard protocol, using JSON-RPC 2.0, that defined how AI applications communicate with external tools and data sources. Its core insight: the connection problem is fundamentally an N×M problem—N AI applications × M data sources, with each combination requiring a custom connector. MCP simplified it to N+M: each application implements the MCP client once, each tool implements the MCP server once. Later, OpenAI and Google DeepMind announced support for MCP. In December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

Second: Anthropic released the Building Effective Agents[1] guide (December 2024). This article was the first to systematically discuss agent engineering patterns—from the simplest prompt chaining to evaluator-optimizer loops—and explicitly put forward a principle: start with the simplest pattern; introduce more structure only when the added complexity demonstrably yields better results. This principle later became one of the core guiding ideas of harness engineering.

By 2025, Anthropic separately elevated context engineering as a distinct engineering practice in Effective context engineering for AI agents[2], emphasizing that the real challenge was no longer just "how to write a prompt" but "what information, in what form, and at what moment, to feed to the model at each step." This was the key transitional layer between Prompt Engineering and Harness Engineering—the problem had already moved from "single-turn quality" up to "per-step context," but not yet up to "the entire task outer loop."

🤯 Lesson 2
A model's reasoning ability solves the "single-step quality" problem, but the reliability of long tasks does not automatically arise just because each step becomes smarter. A model capable of solving an IMO gold-medal problem can still "forget what it was doing" midway through a four-hour full-stack development task.

Act 4: Action (2025)
If 2023 was the year of Chatbots and 2024 the year of Multimodality, then 2025 was the year of Agents.

At the start of the year, the open-source release of DeepSeek-R1 caused the market to reassess the competitive landscape of models. Then came a cascade of agent products: Claude Code (a coding agent in the terminal), GitHub Copilot Agent Mode, Cursor's autonomous coding loops, Manus (a browser-operation agent), OpenAI Operator. The MCP ecosystem exploded; the community built thousands of MCP servers, with SDKs covering all major languages. Google released the Agent2Agent (A2A) protocol, solving cross-vendor communication between agents.

But the most important discovery of 2025 wasn't what agents could do—it was how they failed while doing it:

Agents attempted to complete an entire task in one shot (all-in), exhausting the context window halfway through.
Agents, after completing 70%, declared "all done" and stopped.
Multiple agents running in parallel produced cascading errors, amplifying a small, single mistake into something undebuggable.
Codebases, after sustained agent work, suffered severe "AI slop"—redundant code, inconsistent naming, outdated documentation.
These are not problems of model intelligence; they are problems of system structure.

🤯 Lesson 3
Agent capability has reached the level of "autonomously working for hours," but the engineering infrastructure surrounding them remains stuck in the era of "single-turn conversation." That fracture is the root cause of Harness Engineering's emergence.

Act 5: Governance (2026 – Present)
As 2026 began, the industry's attention started shifting from "how to make agents more capable" to "how to prevent agents from crashing." "Harness Engineering" as a public term did not appear overnight; it rapidly coalesced and spread starting in February 2026:

February 5, 2026: Mitchell Hashimoto explicitly wrote "Engineer the Harness" in My AI Adoption Journey[3]—regarded as one of the starting points for the term entering mainstream discussion.
February 11, 2026: OpenAI directly published an engineering article titled Harness Engineering: Leveraging Codex in an Agent-First World[4]. They described how a small team built an internal beta product from an empty repository in five months, publicly stating it was "zero lines of human-written code," with the repository reaching approximately a million lines of code and generating about 1,500 PRs. More precisely, the initial scaffold was still generated by Codex under minimal template guidance, after which application logic, tests, CI, documentation, observability, and internal tools were produced as much as possible by agents. The core finding: the engineers' focus shifted toward designing environments, specifying intent, and building feedback loops.
March 2026: Anthropic published "Harness Design for Long-Running Application Development," upgrading the earlier initializer/coding two-role architecture into a planner/generator/evaluator three-role system, demonstrating that an evaluator can still yield significant gains near the boundaries of model capability.
April 2026: The Thoughtworks / Fowler system (Harness Engineering - first thoughts[5]) systematized the concept into a more complete methodological framework—a combination of guides (feedforward control) and sensors (feedback control), each further divided into computational (deterministic) and inferential (probabilistic), forming a 2×2 control matrix. Thus, April is better understood as the moment "the methodological abstraction became complete," rather than the "first naming."

What is a Harness, Exactly?
Let's derive it from first principles, not from a definition.

Five Fundamental Challenges of Agents
The essence of an agent is "a system that autonomously advances toward a goal in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone:

State Persistence
Nature: An agent needs to remember what it has done across time and across sessions.
Why the model can't solve it: The model itself is stateless, and the context window has an upper bound; it cannot natively shoulder long-term continuous state.
Goal Consistency
Nature: During long tasks, agents tend to drift, indulge in self-satisfaction, or even prematurely declare completion.
Why the model can't solve it: The model lacks external anchors and cannot stably calibrate "what counts as truly done."
Action Verifiability
Nature: Every step is probabilistic; you need to distinguish "did it" from "did it correctly."
Why the model can't solve it: When evaluating its own results, the model has an inherent tendency toward self-praise and misjudgment.
Entropy Suppression
Nature: Continuous output will accumulate redundancy, drift, and inconsistency.
Why the model can't solve it: The model replicates existing patterns, even if those patterns are themselves bad or low-quality.
Human–Machine Boundary
Nature: When to act autonomously and when to hand back to a human needs clear, engineered definitions.
Why the model can't solve it: The model does not have reliable "uncertainty awareness" and cannot stably judge when it should stop and return control to a human.
Harness is the engineering practice that systematically answers these five challenges.

A Precise Definition
In Demystifying evals for AI agents[6], Anthropic offers a definition worth adopting directly: an agent harness (or scaffold) is the system that enables a model to act as an agent; it handles inputs, orchestrates tool calls, and returns results. More critically, Anthropic further points out: when we evaluate "an agent," what we are actually evaluating is the combination of model + harness, not the model's ability in isolation. This definition is crucial because it shifts the unit of explanation for agent performance from model parameters to the outer-loop structure that the model sits within.

Image
Here we must disentangle a frequently conflated concept: an agent harness and an evaluation harness are not the same thing. The former is responsible for making the agent run (handling inputs, orchestrating tools, managing state); the latter is responsible for batch-running tasks, recording trajectories, executing graders, and aggregating scores. Many discussions throw "harness" into a single bucket, so that one moment they're talking about runtime orchestration and the next about evaluation pipelines. The Harness Engineering discussed in this article refers to the former—the engineering of the runtime outer-loop system.

Based on this, a more precise formulation:

📌
Harness = the outer-loop system that enables a model to act as an Agent.

It includes plan decomposition, durable state, tool orchestration, verification gating, feedback loops, fallback mechanisms, human handoff points, and audit logging. When evaluating an agent's effectiveness, you are evaluating not the model itself, but the combination of model + harness.

A few points worth expanding:

Outer loop is the key term. The model's reasoning is the "inner loop"—given context, generate the next step. Harness is the "outer loop"—deciding when to start a new inner loop, what context to give it, how to verify its output, when to fall back, when to stop. The quality of the inner loop depends on model capability; the quality of the outer loop depends on harness design.
Harness is not an upgraded prompt. A single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control. Treating Harness as "a longer system prompt" is the most common failure mode today.
Harness is also not a framework name. LangChain is a framework, CrewAI is a framework; Harness Engineering is not. It is a practice, just as DevOps is not a tool but an engineering culture.
Three Layers of Engineering Abstraction
Prompt → Context → Harness

To understand Harness's position, you need to see its relationship with the two layers below. These three layers are not replacements for one another but progressive levels of abstraction:

Image
📌 Key Insight
Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline operates." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; but harness also includes multi-step structure, tool intermediation, verification gates, and durable state—things that extend beyond single-step context.

The Six Major Engineering Components of a Harness
This section is the most technically dense part of the article. For each component, I will clarify what problem it solves, the specific approaches of Anthropic/OpenAI, and the underlying design principles.

Durable State Surfaces: So the Agent No Longer "Arrives with Amnesia"
Problem: The core pain point of long-running agents is like an engineer on a project team who suffers total amnesia at every shift change. The context window is finite; complex projects cannot be completed within a single window. The agent needs a way to bridge the gap between sessions.

Anthropic's Solution: They did not attempt to build an "infinitely long context." Instead, they externalized state into resumable artifacts:

The first initializer agent sets up the environment: creates init.sh (startup script), claude-progress.txt (progress log), and an initial git commit (baseline snapshot).
It generates a feature list: expanding high-level requirements into 200+ concrete features, all initially marked as failing.
Each subsequent coding agent performs only incremental progress, leaving structured updates and a "clean state" at session end.
Key rule: the agent can only change the passes status of a feature; it cannot arbitrarily modify the test definitions themselves.
This feature list design looks "rudimentary" but is extremely effective—it transforms the definition of "done" from the agent's subjective feeling into an external, persistent, structured, inheritable surface of completion. The agent doesn't need to "remember" what it did before; it only needs to read the feature list and git diff to resume in 30 seconds.

Anthropic later discovered an even deeper problem: context anxiety. Even with compaction (summarizing earlier conversations), the agent would still degrade behaviorally because it felt the "context was too full." The solution wasn't better compaction; it was context reset—giving the next agent a completely fresh context, passing all necessary information through externalized state artifacts (not conversation history). This is more radical than compaction, but more effective.

📌 Design Principle
State ≠ "saving chat history." True durable state is a structured artifact that an agent can read, understand, and resume from after a cold start, with no prior context history. If your agent cannot figure out, within 30 seconds of a cold start, "where it left off and what to do next," your state management has failed.

Decomposition & Plans: Cutting Long Tasks into Bites an Agent Can Swallow
Problem: Telling an agent "build a clone of claude.ai" will cause it to try to do everything in one shot—writing all the code in a single session. The result is either the context explodes or it stops halfway through and declares "done."

Evolution:

In November 2025, Anthropic initially solved this with a two-role structure: initializer + coding. The initializer decomposed and initialized; the coding agent implemented step by step.
In March 2026, this was upgraded to a three-role system: planner / generator / evaluator.
The planner does not write code directly; it expands a one- or two-sentence high-level description into a full product spec and a step-by-step feature list.
The generator implements feature by feature, committing after each one.
The evaluator independently assesses the generator's output, marks pass/fail, and gives specific improvement suggestions.
OpenAI's counterpart consists of PLANS.md, Implement.md, Documentation.md—complex tasks are planned first, executed along milestones with verification at each stage, while continuously updating documentation as shared memory.

📌 Design Principle
The plan must be elevated to a first-class artifact, not disposable chat content. It needs to be written to the file system, version-controlled, readable by subsequent agents, and referenced by verification gates. A plan that exists only within a conversation is, fundamentally, not a plan—it's merely a thought.

Feedback Loops: Guides and Sensors
Problem: The agent wrote code—how do you know it's correct? By asking the agent itself? Anthropic explicitly found an embarrassing truth: when asked to evaluate its own work, an agent tends to enthusiastically praise itself—even when the quality is plainly mediocre by human standards.

This demands a feedback system that does not rely on the agent's self-evaluation. By April 2026, the community had decomposed harness into a very clear 2×2 matrix:

Image
Guides constrain the agent before it acts, increasing the probability of "getting it right the first time." Sensors give signals after the agent acts, supporting self-correction.

Image
Key insights:

Guides without sensors → the agent encodes rules but never knows if the rules took effect.
Sensors without guides → the agent repeats the same mistakes endlessly and then gets corrected.
Computational controls are cheap, fast, and deterministic, and can run on every change.
Inferential controls are expensive, slow, and non-deterministic, but can handle subjective judgments (e.g., "is this UI design too ugly?").
Anthropic's evaluator-optimizer pattern is fully consistent with this. They also acknowledged a subtle fact: an evaluator is not always necessary—when the base model capability crosses a certain threshold, the evaluator degrades from a "necessary component" to "overhead." This shows that a good harness is not a fixed template but a tailorable system that co-evolves with the model's capability boundary.

Image
Legibility: Building the Agent's Perceptual Surface
Problem: The agent can write code, but can it "see" what the code it wrote looks like when running? Can it read error logs? Can it understand performance metrics?

OpenAI, in their harness engineering practice, made an extremely sharp judgment: knowledge that is not within the agent's runtime-visible surface is, in effect, non-existent.

This isn't rhetoric. They did the following concrete work to improve legibility:

For each git worktree, they launched an independent browser instance, using CDP (Chrome DevTools Protocol[7]) to let the agent "see" the UI.
They exposed logs, metrics, and traces for the agent to query.
Repository knowledge as the system of record: design principles, product intent, execution plans, known technical debt, and Architecture Decision Records (ADRs) all go into the repo and are kept consistent via lint/CI.
They placed AGENTS.md, structured docs/, execution plans, and knowledge documents into the repo as much as possible, making them a versioned system of record. But OpenAI also publicly cautioned: an overly long AGENTS.md will rapidly decay, hog context, and cause all constraints to lose focus simultaneously—a better approach is to turn it into a directory index, with real knowledge split into structured documents.
📌 Design Principle
Legibility is not "making code more elegant"; it's about bringing knowledge, constraints, acceptance criteria, and decision history into the agent's perceptual surface. This directly transforms "knowledge management" from a team collaboration problem into an agent executability problem. For an agent, domain experience shared in Slack, architectural boundaries passed down orally, and constraints scattered across external documents are, unless they enter the runtime-accessible artifact surface, tantamount to non-existence.

Tool Mediation: The More Tools, the More Harness You Need
Problem: After the MCP ecosystem explodes, an agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions into the context creates serious problems—token costs spike, latency rises, and the agent gets lost in a sea of tools.

Anthropic, in their engineering practice around MCP + Code Execution, put forward a core idea: don't let the model directly call tools; let the model write code to call tools.

What's the difference?

Direct tool-calling mode: All tool definitions loaded into context → model selects tool → calls it → results flow back into context → model continues. Every step consumes context space; intermediate results cycle inside the model.
Code execution mode: Model writes a piece of code → the code runs in a sandbox, discovering and calling MCP tools as needed → only the final result is returned to the model. Tool discovery, data filtering, and intermediate processing all happen within the execution environment, never entering the context.
The essence of this approach is moving tool usage out of the model's inner loop and into a more efficient external execution loop. This is precisely harness engineering—it's not a "tool registry"; it's a system-level design that determines how tools are discovered, when they're exposed, at what granularity, whether results need to enter context, where state resides, and how failures are rolled back.

Entropy Control: Continuous Garbage Collection for Agents
Problem: A fully automated agent codebase will continually replicate existing patterns—even if those patterns are uneven, suboptimal, or outright bad. Over time, drift and entropy become inevitable.

OpenAI is bluntest about this: initially, their team spent about 20% of their time each week manually cleaning up "AI slop" (redundant code, outdated docs, inconsistent naming, copy-pasted dead code). They later systematized this cleanup:

Documentation consistency agents periodically verify that documentation matches code.
Refactor agents clean up technical debt according to a plan.
Architectural enforcement is mechanized through CI to maintain module boundaries.
📌 Design Principle
A harness is not just responsible for "making the agent run"; it is also responsible for continuously suppressing the system noise that the agent amplifies. This is the most fundamental difference from a simple "agent framework"—frameworks care about launch and orchestration; harness cares about long-term governability.

Harnessability: Not Every System Is Equally Easy to Harness
If we only understand Harness Engineering as "adding more rules and loops to the agent," we haven't gone deep enough. The deeper question is: not every system is equally easy to harness.

OpenAI's practice constantly hints at the same thing: the reason they could push Codex to high throughput was not only because the model was strong, but also because they continuously pushed knowledge back into the repo, artifact-ized plans, versioned decisions, and made the environment more legible to the agent. How naturally suitable a system is for being tamed by an agent is itself an important variable.

Following this logic leads to a very explanatory judgment: systems that are strongly typed, well-tested, with clear boundaries, versioned documentation, and runtime observability are naturally higher in harnessability. Conversely, systems where knowledge is scattered across human brains, chat tools, and word-of-mouth—no matter how strong the model—will first crash into the wall of "can't see → can't understand → can't govern."

This means that, in the agent era, a team's engineering infrastructure quality (CI completeness, documentation structure, architectural boundary clarity) is no longer just a matter of "engineering culture"—it directly determines how far an agent can go on your system. Harnessability will become a critical dimension for evaluating a system's "agent-readiness."

The Intent System
A Deeper Paradigm Shift: From Command-Driven to Intent-Driven

The above covered the engineering components of a harness. But if we only look at the components, we'll get bogged down in a patchwork of technical details. Let's step back and discuss something more fundamental—why Harness Engineering is not just an engineering practice but the product of a paradigm shift.

Four Ruptures in Human–Computer Interaction
Looking back over the entire history of computing, human–machine interaction has undergone four fundamental ruptures:

CLI (Command Line): The human must precisely master the machine's language. ls -la | grep .py is a command; a single syntax error breaks it. The core assumption of the interaction is "the human adapts to the machine."
GUI (Graphical User Interface): The machine lowers the barrier through visual metaphors. Folders, desktop, drag-and-drop. The core assumption is "the machine presents itself in metaphors the human can understand."
App (Mobile Applications): Logic is solidified into fixed interfaces. One function per button, one button per screen. The core assumption is "the human chooses within preset paths."
Agent (Intent-Driven): The human merely expresses a goal; the system autonomously plans the execution path. The core assumption is "the machine understands the human's intent and autonomously decides how to do it."
Each rupture is not just a technology upgrade but a redistribution of control. In the CLI era, the human held 100% of control; in the Agent era, the human cedes most execution control, retaining only goal-setting and key decision points.

What are the engineering consequences of this ceding?

In a command-driven world, a bug is "the system did not correctly execute my command"—which can be covered by traditional testing. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent but chose a terrible execution path"—this demands an entirely new set of verification, constraint, and feedback mechanisms, which is precisely what Harness must solve.

Applications Are Being "CLI-fied," but Not for Humans
A deeply counterintuitive trend: in the Agent era, all applications and websites are being re-"CLI-fied"—not by making users return to the terminal, but by turning everything into a programmable interface from the agent's perspective.

MCP is essentially the protocol-layer realization of this. When an agent needs to operate Google Drive, it doesn't need to "open a web page and click buttons"—it needs a set of structured API calls. An MCP server abstracts Google Drive into a set of callable functions: gdrive.getDocument, gdrive.createFile, gdrive.search.

This means three things:

First, the object of readability has changed. In the past, readability was for humans—clear UI, reasonable information architecture. Now it must first be for agents—structured APIs, machine-parseable documentation, programmable permission models.

Second, application boundaries are dissolving. When agents call any tool via MCP and collaborate with other agents via A2A, the App degrades from a "destination" to "infrastructure." Users no longer "open an App to do something"; they "express an intent, and the agent orchestrates multiple services to complete it."

Third, Harness becomes a new "operating system layer." The GUI-era OS managed windows, files, and processes. The Agent era needs to manage: agent lifecycles, tool discovery and authorization, context scheduling and reclamation, multi-agent collaboration and isolation, and human-approval intervention points.

From Chatbot to AgentOS
Stringing all the threads above together reveals a clear evolutionary path. These three stages are not a functional overlay but a fundamental change in the engineering abstraction layer:

Level 1: Chatbot (2022–2023)
Single-turn conversation, stateless, human fully in the loop. Core value: information retrieval and content generation. Engineering abstraction layer: Prompt Engineering. Representative products: ChatGPT, Claude (early).

Ceiling: Can speak, cannot do. Each conversation is isolated.

Level 2: AI Browser / Agent IDE (2024–2025)
Multi-step tasks, tool use, limited autonomy. Core value: task execution and workflow automation. Engineering abstraction layer: Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus, Codex.

Ceiling: Single-agent capability is strong but long tasks are unstable; multi-agent collaboration lacks standards; state management is manual work.

Level 3: AgentOS (2026– nascent, forward-looking direction)
Here we must write with restraint. AgentOS is not yet a converged industry paradigm. But it has indeed entered the agendas of the research and systems communities. The 2024 AIOS[8] paper proposed pulling problems such as scheduling, context management, memory management, and access control out of the agent application layer into a kernel-like layer; ASPLOS 2026 featured a dedicated AgenticOS Workshop[9] exploring OS primitives for agent workloads.

Image
Therefore, a more cautious statement is not "AgentOS has arrived," but: Harness Engineering is pushing the problem from the application layer to the system layer. When agents are no longer just coding assistants but always-on, multi-agent, cross-tool, cross-identity, long-running executors, user-space harness will inevitably hit deeper system problems:

Agent lifecycle management: initialization, running, suspension, resumption, termination—not stateless function calls, but full process management.
Context scheduling: The context window is a scarce resource; you must decide what information to load when, when to compress, and when to discard—this is the agent version of "memory management."
Multi-agent isolation and collaboration: One agent's operations must not pollute another's environment, yet they need to share some state—requiring mechanisms akin to process isolation + IPC.
Governance and audit: Every decision of every agent at every step must be traceable—in domains like finance and healthcare, this is not a nice-to-have but a compliance requirement.
Image
📌 Key Positioning
Harness is the user-space layer of AgentOS. AgentOS is the kernel—managing scheduling, isolation, resources. Harness is the user-space shell and daemon—managing task decomposition, state continuity, verification feedback, and human handoff. The two are not in competition; they are natural upper and lower layers.

Five Classic Symptoms
Theory said, back to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are still in a cobbled-together phase. Here are five classic symptoms:

Symptom 1: The Framework Jungle. LangChain, CrewAI, AutoGen, Agno, n8n… Each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to verification to fallback to auditing. Users patch together different frameworks and end up with a fragile pipeline, not a governable system.

Symptom 2: Chatbot Skin + Agent Core. A huge number of products are essentially a chatbot interface wrapped around an agent loop—but they lack genuine state management, task decomposition, and verification gates. They wow in demos, but crash repeatedly in production.

Symptom 3: Tool Registration ≠ Tool Governance. MCP made connection easy, but "able to connect" does not equal "able to use well." An agent facing 50 tools gets confused, makes redundant calls, and takes detours. Engineering teams have found that giving the agent all tools initially produced worse results—improvement only came after paring down to the minimal necessary set.

Symptom 4: One-Off Rules vs. Evolvable Constraints. Most teams' agent configuration is a huge AGENTS.md or system prompt. But practice shows this approach is doomed to fail—when everything is important, nothing is important. The agent will do local pattern matching rather than navigate consciously. Rules decay faster than people can maintain them.

Symptom 5: Lack of "On-the-Loop" Thinking. "In the loop" is manually fixing artifacts when you're unsatisfied with the agent's output; "on the loop" is modifying the harness so the system autonomously produces better results next time. Most teams remain stuck in-the-loop—fixing errors one by one, rather than systematically improving the control loops that produced the errors.

What Harness Is Not
Clarifying boundaries is as important as clarifying definitions.

It is not "a longer system prompt." Because a single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control.

It is not a proprietary term from any one vendor. Both Anthropic and OpenAI use it publicly; academic preprints are already abstracting it into a cross-product general concept.

It is also not something that "won't be needed once models get stronger." Quite the opposite—Anthropic explicitly states that harness will redistribute value as the model boundary shifts outward: some checks become redundant, but planning, verification, handoff, and state governance for harder tasks become more important. The stronger models get, the more you need to place longer, more expensive, and riskier tasks into governed outer loops.

In fact, the space of interesting harness combinations won't shrink as models get stronger—it will shift. An evaluator effective today might become redundant overhead with the next model generation, but new capability boundaries will spawn new harness needs.

Overlooked Critical Issues
Testability of the Harness
When we say "harness makes the agent verifiable," a meta-question arises: how do you verify the harness itself? If the evaluator is another LLM, and that LLM also has hallucination tendencies, we've built a cycle of "verifying an unreliable system with another unreliable system."

Anthropic's approach is to use computational sensors (test suites, linters, type checkers) as much as possible for basic verification, and only bring in inferential sensors at the subjective judgment layer (UI aesthetics, code style). This is a pragmatic layered strategy, but not a perfect solution.

Emergent Behavior of Multi-Agent Systems
When ten agents run in parallel, each making independent decisions, system behavior can exhibit patterns unpredictable from analyzing any single agent. This resembles distributed-system concurrency bugs—but worse, because each "process" is non-deterministic. Current harness designs mainly target single-agent scenarios; multi-agent collaboration harness principles have not yet settled.

Cost and Latency Engineering Trade-offs
Every layer of the harness—planner, evaluator, sensor, garbage collection—consumes additional tokens and latency. When the harness's own overhead exceeds the quality improvement it brings, that's over-engineering. How to measure harness ROI and how to dynamically adjust harness depth based on task complexity remains an unsolved engineering problem.

A New Security Dimension: The Attack Target Shifts from Data to Agency
This is the layer most articles gloss over but is actually the most dangerous. As agents gain durable state, external tools, and long-duration autonomy, the attack surface is no longer just "what the model answered wrong" but "whether the system can be leveraged and manipulated."

In April 2025, Invariant Labs disclosed Tool Poisoning Attacks[10]: malicious instructions can be hidden in MCP tool descriptions, invisible to the user but visible to the model, thereby inducing the agent to perform unauthorized operations. A week later, they demonstrated a data exfiltration scenario through an untrusted MCP server linked to a trusted WhatsApp MCP. This means Harness Engineering cannot just talk about throughput and stability; it must squarely confront tool trust, cross-tool data flows, least privilege, approval boundaries, and execution isolation.

Image
The open standardization of MCP is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connections become, the more the upper-layer harness must enforce stricter governance. The harness's permission model must upgrade from static "allowed/not allowed" to dynamic "allowed under what conditions, up to what limit, and requiring human confirmation after a certain point." That is, the harness is not only the outer loop that improves output; it is itself the new security boundary.

Judgments & Outlook
Judgment 1: Harness Engineering will become one of the foundational disciplines of the AI engineering era.
Improvements in model capability will continue to swallow some micro-level prompt techniques, but they will not swallow harness engineering. Because it deals with a higher-level problem: how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents need to work across time, tools, environments, and human–machine boundaries, harness will not disappear—on the contrary, it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

Judgment 2: The focus of the moat is shifting from model quality up to harness and system design.
When GPT, Claude, and Gemini converge on core capabilities, what determines product success is no longer model differences but harness quality. The strongest evidence comes from LangChain: keeping the underlying model unchanged, purely by modifying the harness, they lifted deepagents-cli on Terminal Bench 2.0 from 52.8% to 66.5%, a gain of 13.7 points, pulling it from the outer fringes of the Top 30 into the Top 5. This result should not be exaggerated to "the model no longer matters," but it is enough to show: atop the same model, harness can open up a massive system-level gap. The moat is shifting upward to harness and system design.

Judgment 3: The migration from Chatbot to AgentOS will not happen in one leap.
There will be a 2–3 year intermediate "AI Browser + lightweight Harness" phase. Most enterprises will first derive value in this phase and then gradually evolve toward heavier AgentOS architectures. Teams that try to jump directly to AgentOS will most likely fail because the governance complexity exceeds their capacity.

Judgment 4: The engineer's role is transforming from "code producer" to "designer of autonomous systems."
This is not a job-loss warning; it's a capability upgrade demand. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing exceptions, and codifying rules—the value of these skills will rise sharply. When dissatisfied with an agent's output, the low-level approach is to manually fix the artifact; the high-level approach is to modify the harness so the system does better autonomously next time. Moving from in the loop to on the loop—that is the core upgrade path for engineers in the agent era.

Appendix
Three self-check questions for practitioners. Before you start building your own harness, answer these three:

Does your agent have durable state surfaces? After a cold start, can it resume within 30 seconds—or does it always start from scratch?
Does your system have machine-readable acceptance criteria? Is "done" defined by the agent's self-perception, or by an external structured verification surface—a feature list, a set of test cases, a checkable pass/fail status?
Are your repo, tools, logs, metrics, and policies legible and enforceable to the agent? Or can only humans read them—while the agent merely guesses?
If the answer to all three is no, what you've built is probably still just "a chatbot that can run commands."
