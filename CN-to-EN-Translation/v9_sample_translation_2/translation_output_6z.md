Background
Let's first answer a preliminary question: how did we get here today?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, we must first clearly see the complete arc that AI engineering has traveled over the past four years. This arc is not linear, but a series of cycles: capability leap → collapse of old frameworks → emergence of new abstractions.

Recommended reading to supplement some additional background knowledge:

AI Operating System: From Instructions to Intent
From Prompt Engineering to Context Engineering
The Token Naming Dilemma: When Information Theory Meets Linguistics
OpenClaw: The Hidden Dangers Behind the Madness
Deep Dive: Google Workspace CLI
Meta-Skills: Making AI Think Like You
Shallow Thoughts on Agent Trends: Native & CLI-ification
AI Coding Ecosystem: What Does Anthropic's Acquisition of Bun Mean?
Deep Thinking: Discussing AI Development Trends
A Brief Discussion on AI Browsers
Deep Dive: Anthropic MCP Protocol
Act I: Generation (Nov 2022 — 2023)
On November 30, 2022, ChatGPT went live. It reached about 100 million monthly active users in roughly two months. But what this event truly changed was not NLP technology—GPT-3 had already existed for two years—but rather the interaction paradigm. Before this, an LLM was an API that only engineers could use; after this, it became a conversational interface that everyone could use.

The core contradiction in this act was: the model could generate, but it could not act. It could write an email, but couldn't send it; it could write a piece of code, but couldn't run it. The relationship between the user and the model was "you ask, I answer"—a stateless, single-turn, passive exchange of information.

The engineering artifact was Prompt Engineering: how to ask so that the model could answer better. Few-shot, chain-of-thought, and role-playing were essentially about maximizing information density within the limited space of a single API call.

Act II: Connection (2023 — 2024)
In March 2023, OpenAI released GPT-4, bringing multimodal capabilities and a longer context window. In the same month, they launched ChatGPT Plugins, giving the model "hands" for the first time—it could call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool calls as structured JSON in the model's output.

This was a critical turning point: the model evolved from "being able to talk" to "being able to connect." But the Plugins ecosystem quickly exposed its fragility—each plugin required an independent OAuth flow, independent schema definition, and independent error handling. Connecting 10 plugins was already painful; 100 was completely impossible.

In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with a layer of intermediate abstraction. It did lower the barrier to entry, but it also introduced the cost of over-abstraction—too many layers of wrapping, difficult debugging, and unpredictable performance. During the same period, projects like AutoGPT and BabyAGI attempted to have models autonomously loop through tasks, but they quickly faded into obscurity after the demo phase due to a lack of reliable stopping conditions and verification mechanisms.

🤯 Lesson 1
Enabling the model to "connect to tools" is necessary, but far from sufficient. Connection is not orchestration, and orchestration is not governance.

Act III: Reasoning (2024)
2024 was the year "reasoning models" took the stage. OpenAI's o1 series was released in September, featuring "spending more time thinking before answering" as its core characteristic, achieving a qualitative leap in math and coding tasks. In December, the ARC Prize announced that OpenAI o3 reached 87.5% on the ARC-AGI-1 Semi-Private Eval under the high-compute configuration, shocking the entire community. At the same time, Anthropic's Claude 3.5 Sonnet showed excellent performance in code generation and long-document understanding, and DeepSeek-R1, as an open-weights model, proved that high-performance reasoning was no longer the exclusive domain of closed-source models.

More important were two events at the end of 2024:

First: Anthropic released the Model Context Protocol (MCP). This was not just another plugin system, but an open standard protocol that used JSON-RPC 2.0 to define how AI applications communicate with external tools and data sources. Its core insight was that the connection problem is inherently an N×M problem—N AI applications × M data sources, where each combination required a custom connector. MCP simplified this to N+M: each application implements an MCP client once, and each tool implements an MCP server once. Later, OpenAI and Google DeepMind successively announced support for MCP, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

Second: Anthropic released the Building Effective Agents[1] guide (December 2024). This article systematically discussed engineering patterns for agents for the first time—from the simplest prompt chaining to the evaluator-optimizer loop—and explicitly proposed a principle: start with the simplest pattern, and only introduce more structure when complexity actually yields better results. This principle later became one of the core guiding philosophies of harness engineering.

In 2025, Anthropic further elevated context engineering into an independent engineering practice, Effective context engineering for AI agents[2], emphasizing that the real challenge was no longer just "how to write a prompt," but "what information, in what form, and at what timing to provide to the model at each step." This was the key transitional layer between Prompt Engineering and Harness Engineering—the problem had shifted upward from "single call" to "per-step context," but had not yet moved up to the "entire task outer loop."

🤯 Lesson 2
The model's reasoning capability solves the "single-step quality" problem, but long-task reliability is not automatically achieved just because single steps are smarter. A model capable of solving an IMO gold medal problem will still "forget what it's doing" midway through a four-hour full-stack development task.

Act IV: Action (2025)
If 2023 was the year of the Chatbot and 2024 was the year of Multimodal, then 2025 was the year of the Agent.

At the beginning of the year, the open-source release of DeepSeek-R1 prompted the market to reassess the landscape of model competition. This was followed by a slew of agent products: Claude Code (a coding agent in the terminal), GitHub Copilot Agent Mode, Cursor's autonomous coding loop, Manus (a browser operation agent), and OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all mainstream languages. Google released the Agent2Agent (A2A) protocol to solve cross-vendor communication between agents.

But the most important discovery in 2025 was not what agents could do, but how they crashed while doing it:

Agents attempted to complete the entire task at once (going all in), exhausting the context window halfway through.
Agents announced "all done" after completing 70%, and then stopped.
When multiple agents ran in parallel, cascading errors occurred, amplifying a single small error to an un-debuggable state.
Codebases exhibited severe "AI slop" after continuous agent work—redundant code, inconsistent naming, and outdated documentation.
These were not model intelligence issues, but system structural issues.

🤯 Lesson 3
Agent capabilities have reached the level of "being able to work autonomously for hours," but the engineering infrastructure surrounding them remains stuck in the era of "single-turn conversations." This rupture is the root cause of the birth of Harness Engineering.

Act V: Governance (2026 — Present)
At the beginning of 2026, the industry's attention shifted from "how to make agents more capable" to "how to keep agents from derailing." As a public term, "Harness Engineering" was not invented overnight on a specific day, but rapidly crystallized and spread starting in February 2026:

On February 5, 2026, Mitchell Hashimoto explicitly wrote "Engineer the Harness" in My AI Adoption Journey[3]—this is considered one of the starting points for the term entering mainstream discussion.
On February 11, 2026, OpenAI published an engineering article directly titled Harness Engineering: Leveraging Codex in an Agent-First World[4]. They used a small team to build an internal beta product from an empty repository in five months, publicly stating "zero lines of manually handwritten code," with the repository reaching the scale of about a million lines of code and generating about 1,500 PRs. More accurately, the initial scaffold was still generated by Codex guided by a few templates, and afterwards the application logic, testing, CI, documentation, observability, and internal tools were produced by agents as much as possible. Core finding: the focus of engineers' work shifted to designing environments, specifying intent, and building feedback loops.
In March 2026, Anthropic released "Harness Design for Long-Running Application Development," upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, proving that the evaluator could still bring significant gains near the boundary of model capabilities.
In April 2026, the Thoughtworks / Fowler system systematized this concept into a more complete methodological framework—the combination of guides (feedforward control) and sensors (feedback control), each further divided into computational (deterministic) and inferential (inferred) categories, forming a 2×2 control matrix. Therefore, April is more appropriately understood as "methodological abstraction becoming complete," rather than "first naming."
What exactly is a Harness?
Let's deduce this from first principles, rather than starting from a definition.

The Five Fundamental Challenges of Agents
The essence of an Agent is "a system that autonomously advances goals in an open environment." This definition implies five engineering challenges, none of which can be solved solely by a smarter model:

State Persistence
Essence: Agents need to remember what they have done across time and sessions.
Why models can't solve it: Models are inherently stateless, and context windows have upper limits, making them unable to naturally bear long-term continuous state.
Goal Alignment
Essence: In long tasks, agents are prone to drift, go off on tangents, or even prematurely declare completion.
Why models can't solve it: Models lack external anchors and cannot stably calibrate "what truly counts as done."
Action Verifiability
Essence: Every step is probabilistic, requiring a distinction between "did it" and "did it right."
Why models can't solve it: Models naturally have a tendency towards self-praise and misjudgment when evaluating their own results.
Entropy Increase Suppression
Essence: Continuous output will continuously accumulate redundancy, drift, and inconsistency.
Why models can't solve it: Models replicate existing patterns, even if those patterns are inherently bad or low-quality.
Human-Machine Boundary
Essence: When to be autonomous and when to hand over to humans needs to be explicitly and engineeringly defined.
Why models can't solve it: Models do not have reliable "uncertainty self-awareness" and cannot stably judge when to stop and hand back to humans.
A Harness is the engineering practice of systematically answering these five challenges.

A Precise Definition
In Demystifying evals for AI agents[6], Anthropic provided a definition very much worth adopting directly: an agent harness (or scaffold) is the system that enables the model to act as an agent; it is responsible for processing inputs, orchestrating tool calls, and returning results. More critically, Anthropic further pointed out: when we evaluate "an agent," we are actually evaluating the combination of model + harness, not the model's standalone capability. This definition is very important because it shifts the unit of explanation for agent effectiveness from model parameters to the outer loop structure in which the model resides.

Image
Here we must untangle a frequently confused concept: an agent harness and an evaluation harness are not the same thing. The former is responsible for making the agent run (processing inputs, orchestrating tools, managing state), while the latter is responsible for running tasks in batch, recording traces, executing graders, and aggregating scores. Many discussions mix "harness" into one big basket, resulting in talking about runtime orchestration one moment and evaluation pipelines the next. The Harness Engineering discussed in this article refers to the former—the engineering of the runtime outer loop system.

Based on this, a more precise formulation:

📌
Harness = The outer loop system that enables the model to act as an Agent.

It includes plan decomposition, persistent state, tool orchestration, verification gating, feedback loops, rollback mechanisms, human-machine handoff points, and audit logs. When evaluating the effectiveness of an Agent, it is not the model itself that is evaluated, but the combination of model + harness.

There are several key points worth expanding upon here:

The outer loop is the keyword. The model's reasoning is the "inner loop"—given a context, generate the next step. The Harness is the "outer loop"—deciding when to start a new inner loop, what context to give it, how to verify its output, when to roll back, and when to stop. The quality of the inner loop depends on model capability, while the quality of the outer loop depends on harness design.
A Harness is not an upgraded version of a prompt. A single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control. Treating a Harness as "a longer system prompt" is the most common failure mode today.
A Harness is also not a framework name. LangChain is a framework, CrewAI is a framework, Harness Engineering is not. It is a practice, just as DevOps is not a tool but an engineering culture.
Three Layers of Engineering Abstraction
Prompt → Context → Harness

To understand the position of the Harness, we must first see its relationship with the previous two layers. These three layers are not alternative relationships, but progressive levels of abstraction:

Image
📌 Key Insight
Context Engineering is "what to feed at each step," while Harness Engineering is "how the entire pipeline operates." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; but harness also includes multi-step structures, tool mediation, verification gates, and durable state—these exceed the scope of single-step context.

Six Major Engineering Components of Harness
This section is the most hardcore part of the article. Each component will clearly explain what problem it solves, the specific practices of Anthropic/OpenAI, and the design principles behind it.

Durable State Surfaces: Keeping Agents from "Amnesic Onboarding"
Problem: The core pain point of long-running Agents is like an engineer in a project team completely losing their memory at every shift change. Context windows are limited, and complex projects cannot be completed within a single window; Agents need a way to bridge the gap between sessions.

Anthropic's Solution: Instead of trying to make an "infinitely long context," they externalized state into resumable artifacts:

The first initializer agent sets up the environment: creates init.sh (startup script), claude-progress.txt (progress log), and an initial git commit (baseline snapshot).
Generates a feature list: expands high-level requirements into 200+ specific features, initially all marked as failing.
Each subsequent coding agent only makes incremental progress, leaving structured updates and a "clean state" at the end of the session.
Key rule: agents can only change the passes status of a feature, and cannot arbitrarily modify the test definitions themselves.
This feature list design looks "unrefined," but it is extremely effective—it shifts the definition of "done" from the agent's subjective feeling to an external, persistent, structured, and inheritable completion surface. The Agent doesn't need to "remember" what it did before; it only needs to read the feature list and git diff to resume in 30 seconds.

Anthropic later discovered a deeper problem: context anxiety. Even with compaction (summarizing and compressing early conversations), the agent's behavior would still degrade due to feeling the "context is too full." The solution was not better compaction, but a context reset—directly giving the next agent a completely new context, passing all necessary information through externalized state artifacts (rather than conversation history). This is more aggressive than compaction, but works better.

📌 Design Principle
State ≠ "saving chat history." True durable state is a structured artifact that the agent can read, understand, and resume from after a cold start, without any context history. If your agent cannot know "where it left off last time and what to do next" within 30 seconds after a cold start, your state management has failed.

Decomposition & Plans: Slicing Long Tasks into Agent-Digestible Chunks
Problem: Tell an agent to "build a clone of claude.ai," and it will attempt to do it all in one go—writing all the code in a single session. The result is either a context explosion or a premature declaration of "done" halfway through.

Evolutionary Process:

In November 2025, Anthropic initially solved this problem using an initializer + coding two-role structure. The initializer was responsible for decomposition and initialization, while coding handled step-by-step implementation.

In March 2026, this structure was upgraded to a planner / generator / evaluator three-role system:

The Planner does not write code directly, but expands a sentence or two of high-level description into a complete product spec and a step-by-step feature list
The Generator is responsible for implementing feature by feature, committing after each completion
The Evaluator is responsible for independently evaluating the Generator's output, marking pass/fail, and providing specific improvement suggestions
OpenAI's counterpart on this side is PLANS.md, Implement.md, Documentation.md—planning first for complex tasks, running by milestones during execution, verifying at each stage, and continuously updating documentation as shared memory.

📌 Design Principle
Plans must be elevated to first-class artifacts, rather than one-off chat content. They need to be written to the file system, version-controlled, readable by subsequent agents, and referenced by verification gates. A plan that exists only in a conversation is essentially not a plan—it is just a passing thought.

Feedback Loops: Guides and Sensors
Problem: An agent writes code, but how does it know if it's written correctly? Rely on the agent to evaluate itself? Anthropic explicitly discovered an embarrassing fact: when asked to evaluate their own work, agents tend to enthusiastically self-praise—even when the quality is obviously mediocre to humans.

This requires a feedback system that does not rely on the agent's self-evaluation. In April 2026, a framework from the community broke down the harness into a very clear 2×2 matrix:

Image
Guides constrain the agent before it acts, increasing the probability of "getting it right the first time." Sensors provide signals after the agent acts, supporting self-correction.

Image
Key Insights:

Only guides and no sensors → the agent encodes the rules but never knows if the rules are actually effective
Only sensors and no guides → the agent constantly repeats the same mistakes and then gets corrected
Computational controls are cheap, fast, and deterministic, and can run on every change
Inferential controls are expensive, slow, and non-deterministic, but can handle subjective judgments (like "is this UI design too ugly")
Anthropic's evaluator-optimizer pattern is completely consistent with this. They also acknowledged a subtle fact: evaluators are not always necessary—when the base model's capabilities cross a certain threshold, the evaluator degrades from a "necessary component" to an "overhead cost." This shows that a good harness is not a fixed template, but a tailorable system that co-evolves with the model's capability boundaries.

Image
Legibility: Building a Perception Surface for Agents
Problem: The Agent can write code now, but can it "see" what the code it wrote looks like when running? Can it read error logs? Can it understand performance metrics?

In their harness engineering practice, OpenAI made an extremely sharp judgment: any knowledge not within the agent's runtime visible scope simply does not exist.

This is not rhetoric. They did the following specific work to improve legibility:

Launch an independent browser instance for each git worktree, allowing the agent to "see" the UI via CDP (Chrome DevTools Protocol[7])
Expose all logs, metrics, and traces for the agent to query.
Repository knowledge as a system of record: design principles, product intent, execution plans, known tech debt, and Architecture Decision Records (ADR) are all placed into the repo and maintained for consistency using lint/CI.
Put AGENTS.md, structured docs/, execution plans, and knowledge documents into the repo as much as possible, making them a versioned system of record; but OpenAI also publicly warned: an overly long AGENTS.md will quickly rot, squeeze the context, and cause all constraints to lose focus simultaneously—a better approach is to turn it into a directory index, scattering the actual knowledge into structured documents.
📌 Design Principle
Legibility is not about "making the code more elegant," but about bringing knowledge, constraints, acceptance criteria, and decision history into the agent's perception surface. This directly turns "knowledge management" from a team collaboration issue into an agent-executability issue. For an agent, experiences in Slack, orally inherited architectural boundaries, and constraints scattered in external documents simply do not exist if they do not enter the runtime-accessible artifact surface.

Tool Mediation: The More Tools, the More Harness is Needed
Problem: After the explosion of the MCP ecosystem, an agent might connect to dozens of MCP servers and access hundreds of tools. But directly stuffing all tool definitions into the context will cause severe problems—soaring token costs, increased latency, and the agent losing its way in a sea of tools.

In their engineering practice of MCP + Code Execution, Anthropic proposed a core approach: do not let the model call tools directly; let the model write code to call tools.

What is the difference?

Direct tool calling mode: All tool definitions are loaded into the context → the model selects a tool → calls it → the result is passed back to the context → the model continues. Every step consumes context space, and intermediate results stay in the model's inner loop.
Code execution mode: The model writes a piece of code → the code runs in a sandbox, discovering and calling MCP tools as needed → only the final result is passed back to the model. Tool discovery, data filtering, and intermediate processing are all completed within the execution environment, never entering the context.
The essence of this idea is: moving tool usage from the model's inner loop to a more efficient external execution loop. This is exactly harness engineering—it is not a "tool registry center," but a system-level design that determines how tools are discovered, when they are exposed, at what granularity they are exposed, whether results need to enter the context, where state is stored, and how failures roll back.

Entropy Control: Continuous Garbage Collection for Agents
Problem: Fully automated agent codebases will continuously replicate existing patterns—even if those patterns are uneven, suboptimal, or even terrible. Over time, drift and entropy increase are inevitable.

OpenAI put it most bluntly: initially, they relied on humans spending about 20% of their time each week cleaning up "AI slop" (redundant code, outdated docs, inconsistent naming, copy-pasted dead code). Later, they systematized this cleanup logic:

Documentation consistency agents regularly verify whether the documentation is consistent with the code
Refactor agents clean up tech debt on a schedule
Architectural enforcement mechanically maintains module boundaries through CI
📌 Design Principle
The Harness is not only responsible for "getting the agent running," but also for continuously suppressing the system noise amplified by the agent. This is its most essential difference from a simple "agent framework"—frameworks care about startup and orchestration, while harnesses care about long-term governability.

Harnessability: Not Every System is Easy to Harness
If we merely understand Harness Engineering as "adding more rules and loops to the agent," it is not deep enough. The more fundamental question is: not every system is equally easy to harness.

OpenAI's practice constantly hints at the same thing: the reason they could push Codex to high throughput is not just because the model is strong enough, but because they continuously compressed knowledge back into the repo, artifact-ized plans, versioned decisions, and made the environment more readable for agents. How inherently suitable a system is for domestication by an agent is itself an important variable.

Following this logic, we can arrive at a very explanatory judgment: systems with strong typing, complete testing, clear boundaries, versioned documentation, and runtime observability inherently have higher harnessability; whereas systems where knowledge is scattered in human brains, chat tools, and word-of-mouth will first hit the wall of "cannot see → cannot understand → cannot govern," no matter how strong the model is.

This means that in the agent era, the quality of a team's engineering infrastructure (CI completeness, degree of documentation structuring, clarity of architectural boundaries) is no longer just an issue of "engineering literacy"—it directly determines how far an agent can go on your system. Harnessability will become a key dimension for evaluating a system's "agent-readiness."

Intent Systems
A Deeper Paradigm Shift: From Instruction-Driven to Intent-Driven

The above discussed the engineering components of the Harness. But if we only look at the components, we will fall into the trap of "stitching together technical details." Let's take a step back and talk about something more fundamental—why Harness Engineering is not just an engineering practice, but the product of a paradigm shift.

Four Ruptures in Human-Computer Interaction
Looking back at the entire history of computing, human-computer interaction has undergone four fundamental ruptures:

CLI (Command Line): Humans had to master the machine's language precisely. `ls -la | grep .py` is an instruction; a single character syntax error means failure. The core assumption of interaction was "humans adapt to the machine."
GUI (Graphical User Interface): The machine lowered the barrier through visual metaphors. Folders, desktops, drag-and-drop. The core assumption of interaction was "the machine presents itself using metaphors humans can understand."
App (Mobile Application): Logic was solidified into fixed interfaces. One button per function, one screen per button. The core assumption of interaction was "humans choose among preset paths."
Agent (Intent-Driven): Humans only express goals, and the system autonomously plans the execution path. The core assumption of interaction is "the machine understands human intent and autonomously decides how to do it."
Each rupture was not just a technological upgrade, but a redistribution of control. In the CLI era, humans had 100% control; in the Agent era, humans have ceded most execution control, retaining only goal setting and key decision points.

What are the engineering consequences of this concession?

In an instruction-driven world, a bug is "the system did not correctly execute my instruction"—which can be covered by traditional testing. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent, but chose a terrible execution path"—which requires a completely new set of verification, constraint, and feedback mechanisms. And this is exactly the problem Harness aims to solve.

Applications are Being "CLI-ified", but Not for Humans
A highly counter-intuitive trend: in the Agent era, all applications and websites are being re-"CLI-ified"—not asking users to return to the terminal, but turning everything into programmable interfaces from the Agent's perspective.

The essence of MCP is the protocol-layer implementation of this very thing. When an Agent needs to operate Google Drive, it doesn't need to "open a webpage and click buttons"—it needs a set of structured API calls. The MCP server abstracts Google Drive into a set of callable functions: gdrive.getDocument, gdrive.createFile, gdrive.search.

This implies three things:

First, the object of legibility has changed. Past legibility was for humans—clear UI, reasonable information architecture. Now it must first be for Agents—structured APIs, machine-parseable documentation, programmable permission models.
Second, the boundaries of applications are dissolving. When an Agent calls any tool via MCP and collaborates with other Agents via A2A, the App degrades from a "destination" to "infrastructure." Users no longer "open an app to do one thing," but rather "express an intent, and the Agent orchestrates multiple services to complete it."
Third, the Harness becomes the new "operating system layer." The operating system in the GUI era managed windows, files, and processes. The Agent era needs to manage: the Agent's lifecycle, tool discovery and authorization, context scheduling and recycling, multi-Agent collaboration and isolation, and human approval intervention points.
From Chatbot to AgentOS
Stringing all the above clues together, we can see a clear evolutionary path. These three stages are not feature additions, but fundamental changes in engineering abstraction layers:

Level 1: Chatbot (2022-2023)
Single-turn conversation, stateless, human completely in the loop. Core value is information retrieval and content generation. Engineering abstraction layer is Prompt Engineering. Representative products: ChatGPT, Claude (early stage).

Ceiling: Can talk but cannot do. Every conversation is isolated.

Level 2: AI Browser / Agent IDE (2024-2025)
Multi-step tasks, tool calling, limited autonomy. Core value is task execution and workflow automation. Engineering abstraction layer is Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus, Codex.

Ceiling: Single agent capability is strong but unstable in long tasks; multi-agent collaboration lacks standards; state management is manual labor.

Level 3: AgentOS (2026- Sprouting Stage, Forward-looking Direction)
We must write with restraint here. AgentOS is not yet a converged industry paradigm. But it has indeed entered the agenda of the research and systems community. The 2024 AIOS[8] paper proposed abstracting issues like scheduling, context management, memory management, and access control from the agent application layer to a kernel-like layer; ASPLOS 2026 featured a dedicated AgenticOS Workshop[9] to explore OS primitives for agent workloads.

Image
Therefore, a more prudent statement is not "AgentOS has arrived," but rather: Harness Engineering is pushing the problem from the application layer to the system layer. When an agent is no longer just a coding assistant, but an always-on, multi-agent, cross-tool, cross-identity long-term executor, the user-mode harness will eventually encounter deeper system-level issues:

Agent lifecycle management: initialization, running, suspension, resumption, termination—not stateless function calls, but complete process management.
Context scheduling: The context window is a scarce resource; we need to decide what information to load, when to compress, and when to discard—this is the agent version of "memory management."
Multi-Agent isolation and collaboration: One agent's operations should not pollute another's environment, yet they need to share certain states—requiring mechanisms similar to process isolation + IPC.
Governance and auditing: Every decision step of every agent needs to be traceable—in areas like finance and healthcare, this is not just icing on the cake but a compliance requirement.
Image
📌 Key Positioning
The Harness is the user-mode layer of the AgentOS. The AgentOS is the kernel—managing scheduling, managing isolation, managing resources. The Harness is the user-mode shell and daemon—managing task decomposition, managing state resumption, managing verification feedback, managing human-machine handoff. The two are not in competition, but are naturally upper and lower layers.

Five Typical Symptoms
Theory aside, let's return to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are actually still stuck in a makeshift stage. Here are five typical symptoms:

Symptom 1: Framework Jungle. LangChain, CrewAI, AutoGen, Agno, n8n... Each framework solves a small piece of the puzzle, but none provides a complete lifecycle from planning to verification to rollback to auditing. Users piece together different frameworks, resulting in a fragile pipeline rather than a governable system.
Symptom 2: Chatbot Skin + Agent Core. A large number of products are essentially a chatbot interface wrapped around an agent loop—but lacking true state management, task decomposition, and verification gates. They look stunning in demos but frequently derail in production.
Symptom 3: Tool Registration ≠ Tool Governance. MCP makes connection easy, but "being able to connect" does not equal "knowing how to use." An agent facing 50 tools will get confused, make redundant calls, and take detours. Some engineering teams found that initially providing the agent with all tools yielded poor results—improvement only came after streamlining to the minimal necessary set.
Symptom 4: One-off Rules vs. Evolvable Constraints. Most teams' agent configuration is a giant AGENTS.md or system prompt. But practice shows this approach is doomed to fail—when everything is important, nothing is. The agent will pattern-match locally rather than navigate consciously. Rules rot faster than humans can maintain them.
Symptom 5: Lack of on-the-loop Thinking. "In the loop" is manually modifying the output when unsatisfied with the agent's result; "on the loop" is modifying the harness so the system automatically yields better results next time. Most teams are still stuck in the loop—fixing errors one by one, rather than systematically improving the control loops that generate the errors.
What a Harness is Not
Clarifying boundaries is just as important as clarifying definitions.

It is not "switching to a longer system prompt." Because a single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control.
It is not a proprietary term owned by any specific vendor. Both Anthropic and OpenAI are using it publicly, and academic preprints are already abstracting it into a cross-product universal concept.
It is also not "something no longer needed once the model gets stronger." On the contrary—Anthropic explicitly pointed out that the harness will redistribute value as model boundaries shift outward: certain checks become redundant, but planning, verification, handoff, and state governance for more difficult tasks become even more important. The stronger the model, the more it needs to place longer, more expensive, and more dangerous tasks into a controlled outer loop.
In fact, the space for interesting harness combinations will not shrink as models get stronger—it will shift. Evaluators that are effective today may become redundant overhead in the face of the next generation of models, but new capability boundaries will spawn new harness demands.

Neglected Key Issues
Testability of the Harness
When we say "the harness makes the agent verifiable," a meta-question arises: how is the harness itself verified? If the evaluator uses another LLM, and that LLM also has a tendency to hallucinate, we have built a loop of "verifying an unreliable system with an unreliable system."

Anthropic's approach is to use computational sensors (test suites, linters, type checkers) for foundational verification as much as possible, and only enable inferential sensors for subjective judgment levels (UI aesthetics, code style). This is a pragmatic layered strategy, but not a perfect solution.

Emergent Behavior of Multi-Agents
When 10 agents run in parallel, each making independent decisions, the system behavior will emergently exhibit patterns unpredictable by single-agent analysis. This is similar to concurrency bugs in distributed systems—but worse, because every "process" is non-deterministic. Current harness designs primarily target single-agent scenarios, and the harness principles for multi-agent collaboration have not yet solidified.

Engineering Trade-off of Cost and Latency
Every layer of the Harness—planner, evaluator, sensor, garbage collection—consumes additional tokens and latency. When the overhead of the harness itself exceeds the quality improvement it brings, it is over-engineering. How to measure the ROI of a harness, and how to dynamically adjust the depth of the harness based on task complexity, remains an unsolved engineering problem.

A New Dimension of Security: The Attack Target Shifts from Data to Agency
This is the layer that many articles most easily gloss over, yet is actually the most dangerous. As agents possess persistent state, external tools, and long-term autonomy, the attack surface is no longer just "what the model answered incorrectly," but "whether the system can be manipulated by leveraging it."

In April 2025, Invariant Labs disclosed Tool Poisoning Attacks[10]: malicious instructions could be hidden in MCP tool descriptions, invisible to users but visible to the model, thereby inducing the agent to perform unauthorized operations; a week later, they demonstrated a data exfiltration scenario linking an untrusted MCP server with a trusted WhatsApp MCP. This means Harness Engineering cannot just talk about throughput and stability; it must also directly address tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation.

Image
The open standardization of MCP is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connection is, the more it demands stricter governance from the upper-layer harness. The harness's permission model must upgrade from a static "can/cannot" to a dynamic "under what conditions it can, up to what limit it can, and only after human confirmation." In other words, the harness is not just an outer loop to improve output; it is itself the new security boundary.

Judgments & Prospects
Judgment 1: Harness Engineering will become one of the foundational disciplines of the AI engineering era
Improvements in model capabilities will continue to swallow some microscopic prompt techniques, but they will not swallow harness engineering. Because it deals with higher-level problems: how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents need to work across time, tools, environments, and human-machine boundaries, the harness will not disappear—instead, it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

Judgment 2: The focus of the moat is shifting upward from model quality to Harness and system design
When GPT, Claude, and Gemini converge in core capabilities, what determines a product's success is no longer model differences, but harness quality. The hardest evidence comes from LangChain: keeping the underlying model unchanged, they improved deepagents-cli on Terminal Bench 2.0 from 52.8% to 66.5% just by modifying the harness, an increase of 13.7 points, pulling the rank from the outskirts of the Top 30 to the Top 5. This result cannot be exaggerated into "models are no longer important," but it is enough to show that: on top of the same model, the harness is sufficient to open up a huge systemic gap. The focus of the moat is shifting upward to harness and system design.

Judgment 3: The migration from Chatbot to AgentOS will not happen overnight
In between, there will be a 2-3 year "AI Browser + lightweight Harness" stage. Most enterprises will first gain value in this stage, and then gradually evolve toward a heavier AgentOS architecture. Teams trying to jump straight to AgentOS will most likely fail because the governance complexity exceeds their capacity to bear.

Judgment 4: The engineer's role is shifting from "code producer" to "designer of autonomous systems"
This is not a warning of unemployment, but a demand for capability upgrades. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing anomalies, consolidating rules—the value of these capabilities will rise sharply. When unsatisfied with the agent's output, the low-level approach is to manually modify the product; the high-level approach is to modify the harness so the system automatically does better next time. From in the loop to on the loop, this is the core upgrade path for engineers in the agent era.

Appendix
Three self-check questions for practitioners. Before starting to build your own harness, answer these three questions first:

Does your agent have durable state surfaces? Can it resume within 30 seconds after a cold start—or does it start from scratch every time?
Does your system have machine-readable acceptance criteria? Is the definition of "done" the agent's own feeling, or an external structured verification surface—a feature list, a set of test cases, a checkable pass/fail status?
Are your repo, tools, logs, metrics, and policies legible and enforceable for the agent? Or can only humans read them—leaving the agent to guess?
If you don't have any of these three things, what you've built is most likely just "a chatbot that can run commands"...
