Background
Preliminary question: How did we get here today?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, we must first look at the complete arc of AI engineering over the past four years. This arc is not linear, but a cycle of capability leaps → old framework collapse → new abstraction emergence.

Recommended reading to provide additional background knowledge:
"AI Operating Systems: From Instructions to Intent"
"From Prompt Engineering to Context Engineering"
"The Token Naming Dilemma: When Information Theory Meets Linguistics"
"OpenClaw: The Hidden Dangers Behind the Madness"
"Deep Dive: Google Workspace CLI"
"Meta-Skills: Making AI Think Like You"
"Brief Thoughts on Agent Trends: Native & CLI-ification"
"AI Programming Ecosystem: What Does Anthropic's Acquisition of Bun Mean?"
"Deep Thinking: Discussing AI Development Trends"
"A Brief Talk on AI Browsers"
"Deep Dive: Anthropic MCP Protocol"

Act I: Generation (2022.11 — 2023)
On November 30, 2022, ChatGPT went live. It reached about 100 million monthly active users roughly two months after launch. But what this truly changed was not NLP technology—GPT-3 had existed for two years—but the interaction paradigm. Before this, an LLM was an API accessible only to engineers; after this, it became a conversational interface accessible to everyone.

The core contradiction in this act was: the model could generate, but it could not act. It could write an email, but couldn't send it; it could write code, but couldn't run it. The relationship between the user and the model was "you ask, I answer"—a stateless, single-turn, passive information exchange.

The engineering artifact was Prompt Engineering: how to ask so the model answers better. Few-shot, chain-of-thought, and role-playing were essentially ways to maximize information density within the limited space of a single API call.

Act II: Connection (2023 — 2024)
In March 2023, OpenAI released GPT-4, bringing multimodality and a longer context window. In the same month, ChatGPT Plugins were introduced, giving the model "hands" for the first time—capable of calling external APIs and accessing real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool calls into structured JSON within the model's output.

This was a critical turning point: the model evolved from "being able to speak" to "being able to connect." But the Plugins ecosystem quickly revealed its fragility—each plugin required an independent OAuth flow, independent schema definition, and independent error handling. Connecting 10 plugins was already painful; 100 was fundamentally impossible.

In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with a layer of intermediate abstraction. It did lower the barrier to entry, but also introduced the cost of over-abstraction—too many layers of wrapping, difficult debugging, and unpredictable performance. During the same period, projects like AutoGPT and BabyAGI tried to let models autonomously loop through tasks, but quickly faded after their demos due to the lack of reliable stopping conditions and verification mechanisms.

🤯 Lesson 1
Making the model "capable of connecting tools" is necessary, but far from sufficient. Connection is not orchestration, and orchestration is not governance.

Act III: Reasoning (2024)
2024 was the year "reasoning models" entered the stage. OpenAI's o1 series was released in September, featuring "spending more time thinking before answering" as its core characteristic, achieving a qualitative leap in math and coding tasks. In December, ARC Prize announced that OpenAI o3 achieved 87.5% on the ARC-AGI-1 Semi-Private Eval under the high-compute configuration, shocking the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet showed outstanding performance in code generation and long-document understanding, and DeepSeek-R1, as an open-weights model, proved that high-performance reasoning was no longer the exclusive domain of closed-source models.

Even more important were two events at the end of 2024:

First: Anthropic released the Model Context Protocol (MCP). This was not just another plugin system, but an open standard protocol defining how AI applications communicate with external tools and data sources using JSON-RPC 2.0. Its core insight was: the connection problem is essentially an N×M problem—N AI applications × M data sources, each combination requiring a custom connector. MCP simplified this to N+M: each application implements an MCP client once, and each tool implements an MCP server once. Later, OpenAI and Google DeepMind successively announced support for MCP, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

Second: Anthropic released the "Building Effective Agents"[1] guide (December 2024). This article systematically discussed engineering patterns for agents for the first time—from the simplest prompt chaining to the evaluator-optimizer loop—and explicitly proposed a principle: start with the simplest pattern, and only introduce more structure when complexity actually yields better results. This principle later became one of the core guiding ideologies of harness engineering.

In 2025, Anthropic further elevated context engineering into an independent engineering practice, "Effective context engineering for AI agents"[2], emphasizing that the real challenge was no longer just "how to write a prompt," but "at each step, what information to give the model, in what form, and at what timing." This was a key transitional layer from Prompt Engineering to Harness Engineering—the problem had shifted up from "single call" to "per-step context," but had not yet shifted up to "the entire task's outer loop."

🤯 Lesson 2
The model's reasoning ability solves the "single-step quality" problem, but long-task reliability does not automatically come from smarter single steps. A model capable of solving an IMO gold medal problem will still "forget what it's doing" midway through a four-hour full-stack development task.

Act IV: Action (2025)
If 2023 was the year of the Chatbot and 2024 the year of Multimodality, then 2025 was the year of the Agent.

At the beginning of the year, the open-source release of DeepSeek-R1 prompted the market to reassess the landscape of model competition. This was followed by a slew of agent products: Claude Code (a coding agent in the terminal), GitHub Copilot Agent Mode, Cursor's autonomous coding loop, Manus (a browser operation agent), and OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all mainstream languages. Google released the Agent2Agent (A2A) protocol to solve cross-vendor communication between agents.

But the most important discovery in 2025 was not what agents could do, but how they crashed when doing it:
The agent attempted to complete the entire task in one go, exhausting its context window halfway through.
The agent announced "all done" after completing 70%, and then stopped.
Multiple agents running in parallel produced cascading errors, where a single small error was amplified to the point of being undebuggable.
The codebase exhibited severe "AI slop" after continuous agent work—redundant code, inconsistent naming, outdated documentation.
These were not model intelligence issues, but system structural issues.

🤯 Lesson 3
Agent capabilities have reached the level of "being able to work autonomously for hours," but the engineering infrastructure surrounding them remains stuck in the era of "single-turn conversations." This rupture is the root cause of the birth of Harness Engineering.

Act V: Governance (2026 — Present)
At the beginning of 2026, the industry's attention shifted from "how to make agents more capable" to "how to prevent agents from derailing." As a public term, "Harness Engineering" was not invented overnight; rather, it rapidly coalesced and spread starting in February 2026:

On February 5, 2026, Mitchell Hashimoto explicitly wrote "Engineer the Harness" in "My AI Adoption Journey"[3]—this is considered one of the starting points for the term entering mainstream discussion.
On February 11, 2026, OpenAI published an engineering article directly titled "Harness Engineering: Leveraging Codex in an Agent-First World"[4]. Using a small team, they built an internal beta product from an empty repository in five months, publicly stating "zero lines of manually written code," with the repository reaching the scale of about a million lines of code and generating about 1,500 PRs. More accurately, the initial scaffold was still generated by Codex with minimal template guidance, and subsequent application logic, tests, CI, documentation, observability, and internal tools were produced by agents as much as possible. Core finding: engineers' focus shifted to designing environments, specifying intent, and building feedback loops.
In March 2026, Anthropic released "*Harness Design for Long-Running Application Development*", upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, proving that the evaluator could still bring significant gains near the boundary of model capabilities.
In April 2026, the Thoughtworks / Fowler system ("*Harness Engineering - first thoughts*"[5]) systematized this concept into a more complete methodological framework—the combination of guides (feedforward control) and sensors (feedback control), each further divided into computational (deterministic) and inferential (inferential) categories, forming a 2×2 control matrix. Therefore, April is better understood as "methodological abstraction becoming complete," rather than "first naming."
What exactly is a Harness?
Let's deduce from first principles rather than starting from a definition.

The Five Fundamental Challenges of Agents
The essence of an agent is "a system that autonomously advances goals in an open environment." This definition implies five engineering challenges, none of which can be solved solely by a smarter model:

State Persistence
Essence: Agents need to remember what they have done across time and sessions.
Why models can't solve it: Models themselves are stateless, and context windows have limits, making them inherently unfit for bearing long-term continuous state.
Goal Alignment
Essence: In long tasks, agents easily drift, self-indulge, or even declare completion prematurely.
Why models can't solve it: Models lack external anchors and cannot stably calibrate "what truly counts as done."
Action Verifiability
Essence: Every step is probabilistic, requiring a distinction between "did it" and "did it right."
Why models can't solve it: Models naturally have a tendency for self-praise and misjudgment when evaluating their own results.
Entropy Suppression
Essence: Continuous output inevitably accumulates redundancy, drift, and inconsistency.
Why models can't solve it: Models replicate existing patterns, even if those patterns are inherently bad or low-quality.
Human-Machine Boundary
Essence: When to be autonomous and when to hand off to humans needs to be explicitly and engineeringly defined.
Why models can't solve it: Models do not have reliable "uncertainty awareness" and cannot stably judge when to stop and hand back to humans.
Harness is the engineering practice that systematically answers these five challenges.

A Precise Definition
Anthropic gave a definition in "Demystifying evals for AI agents"[6] that is highly worth adopting directly: the agent harness (or scaffold) is the system that enables the model to act as an agent; it is responsible for handling input, orchestrating tool calls, and returning results. More importantly, Anthropic further pointed out: when we evaluate "an agent," we are actually evaluating the combination of model + harness, not the model's standalone capability. This definition is crucial because it shifts the unit of explanation for agent effectiveness from model parameters to the outer loop structure in which the model operates.

Image
Here we must disentangle a frequently confused concept: an agent harness and an evaluation harness are not the same thing. The former is responsible for making the agent run (handling input, orchestrating tools, managing state), while the latter is responsible for batch-running tasks, recording trajectories, executing graders, and aggregating scores. Many discussions turn "harness" into a catch-all basket, resulting in talking about runtime orchestration one moment and evaluation pipelines the next. The Harness Engineering discussed in this article refers to the former—the engineering of the runtime outer loop system.

Based on this, a more precise formulation:

📌
Harness = The outer loop system that enables the model to act as an Agent.

It includes plan decomposition, persistent state, tool orchestration, verification gates, feedback loops, rollback mechanisms, human handoff points, and audit logs. When evaluating an Agent's effectiveness, it is not the model itself being evaluated, but the combination of model + harness.

There are a few key points worth elaborating on here:

Outer loop is the keyword. The model's reasoning is the "inner loop"—given a context, generate the next step. The Harness is the "outer loop"—deciding when to start a new inner loop, what context to give it, how to verify its output, when to roll back, and when to stop. The quality of the inner loop depends on model capability, while the quality of the outer loop depends on harness design.
Harness is not an upgraded version of a prompt. A single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control. Treating Harness as "a longer system prompt" is the most common failure mode today.
Harness is also not a framework name. LangChain is a framework, CrewAI is a framework, Harness Engineering is not. It is a practice, just as DevOps is not a tool but an engineering culture.
Three-Layer Engineering Abstraction
Prompt → Context → Harness

To understand the position of Harness, we must first see its relationship with the previous two layers. These three layers are not mutually exclusive but progressive abstraction levels:

Image
📌 Key Insight
Context Engineering is "what to feed at each step," while Harness Engineering is "how the entire pipeline operates." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; but harness also includes multi-step structures, tool mediation, verification gates, and durable state—things that exceed the scope of single-step context.

The Six Engineering Components of Harness
This section is the most hardcore part of the article. For each component, we will clarify what problem it solves, the specific practices of Anthropic/OpenAI, and the underlying design principles.

Durable State Surfaces: Preventing Agents from "Amnesiac Onboarding"
Problem: The core pain point of long-running agents is like an engineer in a project team completely losing their memory at every shift change. Context windows are limited, and complex projects cannot be completed within a single window. Agents need a way to bridge the gap between sessions.

Anthropic's Solution: Instead of trying to build an "infinitely long context," they externalized state into resumable artifacts:

The first initializer agent sets up the environment: creating `init.sh` (startup script), `claude-progress.txt` (progress log), and an initial git commit (baseline snapshot).
Generates a feature list: expanding high-level requirements into 200+ specific features, initially all marked as failing.
Subsequent coding agents only make incremental progress, leaving structured updates and a "clean state" at the end of the session.
Key rule: agents can only change the passes status of a feature, not arbitrarily modify the test definition itself.
This feature list design looks "dumb," but it is extremely effective—it shifts the definition of "done" from the agent's subjective feeling to an external, persistent, structured, and inheritable completion surface. The agent doesn't need to "remember" what it did before; it just needs to read the feature list and git diff to resume in 30 seconds.

Anthropic later discovered a deeper problem: context anxiety. Even with compaction (summarizing and compressing early conversations), agents still exhibit behavioral degradation because they feel the "context is too full." The solution was not better compaction, but context reset—directly giving the next agent a completely new context, passing all necessary information through externalized state artifacts (rather than conversation history). This is more aggressive than compaction, but works better.

📌 Design Principle
State ≠ "saving chat history." True durable state is a structured artifact that the agent can read, understand, and resume from after a cold start, without any context history. If your agent cannot know "where it left off and what to do next" within 30 seconds of a cold start, your state management has failed.

Decomposition & Plans: Slicing Long Tasks into Agent-Digestible Chunks
Problem: Tell an agent to "build a clone of claude.ai," and it will try to do it all in one go—writing all the code in a single session. The result is either a context blowup or declaring "done" halfway through.

Evolution:

In November 2025, Anthropic initially solved this with an initializer + coding two-role structure. The initializer was responsible for decomposition and initialization, while coding handled step-by-step implementation.

In March 2026, this structure was upgraded to a planner / generator / evaluator three-role system:

The Planner doesn't write code directly, but expands a sentence or two of high-level description into a complete product spec and a step-by-step feature list
The Generator is responsible for implementing feature by feature, committing after each completion
The Evaluator is responsible for independently assessing the Generator's output, marking pass/fail, and providing specific improvement suggestions
OpenAI's corresponding artifacts are `PLANS.md`, `Implement.md`, `Documentation.md`—complex tasks are planned first, executed by milestones, verified at each stage, and documentation is continuously updated as shared memory.

📌 Design Principle
Plans must be elevated to first-class artifacts, not one-off chat content. They need to be written to the file system, version-controlled, readable by subsequent agents, and referenced by verification gates. A plan that exists only in a conversation is essentially not a plan—it's just a passing thought.

Feedback Loops: Guides and Sensors
Problem: An agent writes code, but how does it know if it's correct? Rely on the agent to evaluate itself? Anthropic explicitly discovered an embarrassing fact: when asked to evaluate their own work, agents tend to enthusiastically self-praise—even when the quality is obviously mediocre to humans.

This requires a feedback system that does not rely on agent self-evaluation. In April 2026, a community framework split harness into a very clear 2×2 matrix:

Image
Guides constrain the agent before it acts, increasing the probability of "getting it right the first time." Sensors give signals after the agent acts, supporting self-correction.

Image
Key Insights:

Only guides without sensors → the agent encodes rules but never knows if the rules took effect
Only sensors without guides → the agent constantly repeats the same mistakes and then gets corrected
Computational control is cheap, fast, and deterministic, runnable on every change
Inferential control is expensive, slow, and non-deterministic, but can handle subjective judgments (e.g., "is this UI design too ugly")
Anthropic's evaluator-optimizer pattern aligns perfectly with this. They also acknowledged a subtle fact: evaluators are not always necessary—when the base model's capability crosses a certain threshold, the evaluator degrades from a "necessary component" to "extra overhead." This shows that a good harness is not a fixed template, but a tailorable system that co-evolves with the model's capability boundary.

Image
Legibility: Building a Perception Surface for Agents
Problem: The agent can write code, but can it "see" what the code looks like when running? Can it read error logs? Can it understand performance metrics?

OpenAI made an extremely sharp judgment in their harness engineering practice: any knowledge not visible within the agent's runtime environment equals non-existence.

This is not rhetoric. They did the following specific work to improve legibility:

Started an independent browser instance for each git worktree, allowing the agent to "see" the UI via CDP (Chrome DevTools Protocol[7])
Exposed all logs, metrics, and traces for the agent to query.
Repository knowledge as system of record: design principles, product intent, execution plans, known tech debt, and Architectural Decision Records (ADR), all put into the repo with consistency maintained via lint/CI.
Placed `AGENTS.md`, structured `docs/`, execution plans, and knowledge docs into the repo as much as possible, making them a versioned system of record; but OpenAI also publicly warned: an overly long `AGENTS.md` will quickly rot, crowd the context, and make all constraints lose focus simultaneously—a better practice is to turn it into a directory index and scatter the actual knowledge into structured documents.
📌 Design Principle
Legibility is not "making code more elegant," but bringing knowledge, constraints, acceptance criteria, and decision history into the agent's perception surface. This directly turns "knowledge management" from a team collaboration issue into an agent-executability issue. For an agent, experience in Slack, orally inherited architectural boundaries, and constraints scattered in external documents equal non-existence if they do not enter the runtime-accessible artifact surface.

Tool Mediation: The More Tools, the More Harness is Needed
Problem: After the explosion of the MCP ecosystem, an agent might connect to dozens of MCP servers and access hundreds of tools. But directly stuffing all tool definitions into the context causes severe problems—soaring token costs, increased latency, and the agent losing its way in a sea of tools.

Anthropic proposed a core idea in their MCP + Code Execution engineering practice: don't let the model call tools directly; let the model write code to call tools.

Where is the difference?

Direct tool calling mode: All tool definitions are loaded into the context → model selects a tool → calls it → result returns to the context → model continues. Every step consumes context space, and intermediate results stay within the model's inner loop.
Code execution mode: The model writes a piece of code → the code runs in a sandbox, discovering and calling MCP tools as needed → only the final result is returned to the model. Tool discovery, data filtering, and intermediate processing are all done within the execution environment, not entering the context.
The essence of this idea is: moving tool usage from the model's inner loop to a more efficient external execution loop. This is precisely harness engineering—it is not a "tool registry," but the system-level design that determines how tools are discovered, when they are exposed, at what granularity they are exposed, whether results need to enter the context, where state is kept, and how failures roll back.

Entropy Control: Continuous Garbage Collection for Agents
Problem: Fully automated agent codebases continuously replicate existing patterns—even if those patterns are uneven, suboptimal, or terrible. Over time, drift and entropy increase are inevitable.

OpenAI put it most bluntly: initially, they relied on humans spending about 20% of their time each week cleaning up "AI slop" (redundant code, outdated docs, inconsistent naming, copy-pasted dead code). Later, this cleanup logic was systematized:

Documentation consistency agents periodically verify if docs match the code
Refactor agents clean up tech debt on schedule
Architectural enforcement mechanically maintains module boundaries via CI
📌 Design Principle
Harness is not only responsible for "making the agent run," but also for continuously suppressing the system noise amplified by the agent. This is its most essential difference from a simple "agent framework"—frameworks care about starting and orchestrating, while harnesses care about long-term governability.

Harnessability: Not Every System is Easily Harnessed
If we only understand Harness Engineering as "adding more rules and loops to agents," it's not deep enough. The more fundamental issue is: not every system is equally easy to harness.

OpenAI's practices constantly hint at the same thing: they could push Codex to high throughput not just because the model was strong enough, but because they continuously compressed knowledge back into the repo, artifactized plans, versioned decisions, and made the environment more readable for agents. How inherently suitable a system is for being tamed by agents is itself an important variable.

Following this logic leads to a highly explanatory judgment: strongly typed, comprehensively tested, clearly bounded, version-documented, and runtime-observable systems are inherently higher harnessability; systems where knowledge is scattered across human brains, chat tools, and word-of-mouth will hit the wall of "cannot see → cannot understand → cannot govern" no matter how strong the model is.

This means that in the agent era, a team's engineering infrastructure quality (CI completeness, degree of document structuring, clarity of architectural boundaries) is no longer just an "engineering literacy" issue—it directly determines how far an agent can go on your system. Harnessability will become a key dimension for evaluating a system's "agent-readiness."

Intent Systems
A Deeper Paradigm Shift: From Instruction-Driven to Intent-Driven

The above covers the engineering components of Harness. But looking only at components leads to falling into a "patchwork of technical details." Let's step back and discuss something more fundamental—why Harness Engineering is not just an engineering practice, but the product of a paradigm shift.

The Four Ruptures in Human-Computer Interaction
Looking back at the entire history of computing, human-computer interaction has undergone four fundamental ruptures:

CLI (Command Line): Humans had to master the machine's language precisely. `ls -la | grep .py` is an instruction; a single syntax error breaks it. The core assumption of interaction was "humans adapt to machines."
GUI (Graphical User Interface): Machines lowered the barrier through visual metaphors. Folders, desktops, drag-and-drop. The core assumption of interaction was "machines present themselves using metaphors humans can understand."
App (Mobile Application): Logic was solidified into fixed interfaces. One button per feature, one screen per button. The core assumption of interaction was "humans choose among preset paths."
Agent (Intent-Driven): Humans only express goals, and the system autonomously plans the execution path. The core assumption of interaction is "machines understand human intent and autonomously decide how to do it."
Every rupture is not just a technical upgrade, but a redistribution of control. In the CLI era, humans had 100% control; in the Agent era, humans relinquish most execution control, retaining only goal setting and key decision points.

What are the engineering consequences of this relinquishment?

In an instruction-driven world, a bug is "the system didn't execute my instructions correctly"—which can be covered by traditional testing. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent, but chose a terrible execution path"—this requires a whole new set of verification, constraint, and feedback mechanisms, which is exactly what Harness is meant to solve.

Applications are being "CLI-ified," but not for humans
A very counterintuitive trend: in the Agent era, all applications and websites are being re-"CLI-ified"—not to make users return to the terminal, but to turn everything into a programmable interface from the Agent's perspective.

The essence of MCP is the protocol layer implementation of this very thing. When an Agent needs to operate Google Drive, it doesn't need to "open a webpage, click a button"—it needs a set of structured API calls. The MCP server abstracts Google Drive into a set of callable functions: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This means three things:

First, the object of legibility has changed. Past legibility was for humans—clear UI, reasonable information architecture. Now it must first be for Agents—structured APIs, machine-parseable documentation, programmable permission models.

Second, application boundaries are dissolving. When an Agent calls any tool via MCP and collaborates with other Agents via A2A, Apps degrade from "destinations" to "infrastructure." Users no longer "open an app to do a thing," but "express an intent, and the Agent orchestrates multiple services to complete it."

Third, Harness becomes the new "Operating System layer." The OS in the GUI era managed windows, files, and processes. The Agent era needs to manage: the Agent lifecycle, tool discovery and authorization, context scheduling and recycling, multi-Agent collaboration and isolation, and human approval intervention points.

From Chatbot to AgentOS
Stringing together all these clues, we can see a clear evolutionary path. These three stages are not feature stacking, but fundamental changes in engineering abstraction layers:

Level 1: Chatbot (2022-2023)
Single-turn conversation, stateless, human completely in the loop. Core value is information retrieval and content generation. The engineering abstraction layer is Prompt Engineering. Representative products: ChatGPT, Claude (early).

Ceiling: Can speak but cannot act. Every conversation is isolated.

Level 2: AI Browser / Agent IDE (2024-2025)
Multi-step tasks, tool calls, limited autonomy. Core value is task execution and workflow automation. The engineering abstraction layer is Context Engineering + Lightweight Harness. Representative products: Claude Code, Cursor, Manus, Codex.

Ceiling: Single agent is strong but unstable in long tasks; multi-agent collaboration lacks standards; state management is manual work.

Level 3: AgentOS (2026- Incubation period, forward-looking direction)
Here we must be restrained. AgentOS is not yet a converged industry paradigm. But it has indeed entered the agenda of the research and systems community. The 2024 AIOS[8] paper proposed abstracting scheduling, context management, memory management, and access control from the agent application layer into a kernel-like layer; ASPLOS 2026 featured a dedicated AgenticOS Workshop[9] exploring OS primitives for agent workloads.

Image
Therefore, a more accurate statement is not "AgentOS has arrived," but: Harness Engineering is pushing the problem from the application layer to the system layer. When an agent is no longer just a coding assistant, but an always-on, multi-agent, cross-tool, cross-identity long-term executor, the user-mode harness will eventually hit deeper system problems:

Agent lifecycle management: initialization, running, suspension, resumption, termination—not stateless function calls, but complete process management.
Context scheduling: The context window is a scarce resource, requiring decisions on what information to load when, compress when, and discard when—this is the agent version of "memory management."
Multi-Agent isolation and collaboration: One agent's operations should not pollute another's environment, yet they need to share certain states—requiring mechanisms like process isolation + IPC.
Governance and auditing: Every decision step of every agent needs to be traceable—in fields like finance and healthcare, this is not a nice-to-have but a compliance requirement.
Image
📌 Key Positioning
Harness is the user-mode layer of AgentOS. AgentOS is the kernel—managing scheduling, isolation, and resources. Harness is the user-mode shell and daemon—managing task decomposition, state resumption, verification feedback, and human handoff. The two are not competitors, but natural upper and lower layers.

Five Typical Symptoms
Theory aside, back to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are actually still in a makeshift patchwork stage. Here are five typical symptoms:

Symptom 1: Framework Jungle. LangChain, CrewAI, AutoGen, Agno, n8n... each framework solves a small piece of the puzzle, but none provides a complete lifecycle from planning to verification to rollback to auditing. Users patch things together across frameworks, resulting in a fragile pipeline rather than a governable system.

Symptom 2: Chatbot Skin + Agent Core. Many products are essentially a chatbot interface wrapped around an agent loop—but lacking true state management, task decomposition, and verification gates. Amazing in demos, constantly derailing in production.

Symptom 3: Tool Registration ≠ Tool Governance. MCP makes connection easy, but "can connect" does not mean "can use." Agents get confused when facing 50 tools, making redundant calls and taking detours. Engineering teams have found that initially giving agents all tools yields poor results—improvement only comes after paring down to the minimal necessary set.

Symptom 4: One-off Rules vs. Evolvable Constraints. Most teams' agent configs are a giant `AGENTS.md` or system prompt. But practice shows this approach is doomed to fail—when everything is important, nothing is. Agents will pattern-match locally rather than navigate consciously. Rules rot faster than humans can maintain them.

Symptom 5: Lack of on-the-loop Thinking. "In the loop" is manually modifying the output when unsatisfied with the agent's result; "on the loop" is modifying the harness so the system automatically produces better results next time. Most teams are still stuck in the loop—fixing errors one by one rather than systematically improving the control loop that generates the errors.

What Harness is Not
Clarifying boundaries is just as important as clarifying definitions.

It is not "just swapping in a longer system prompt." Because a single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control.

It is not a proprietary term from a specific vendor. Both Anthropic and OpenAI use it publicly, and academic preprints are already abstracting it into a cross-product universal concept.

It is also not "something no longer needed once the model gets stronger." Quite the opposite—Anthropic explicitly points out that the harness will redistribute value as the model's boundary moves outward: certain checks become redundant, but planning, verification, handoff, and state governance for harder tasks become more important. The stronger the model, the more necessary it is to place longer, more expensive, and more dangerous tasks into a controlled outer loop.

In fact, the space for interesting harness combinations will not shrink as models get stronger—it will shift. Evaluators that are effective today may become redundant overhead for the next generation of models, but new capability boundaries will spawn new harness needs.

Overlooked Key Issues
Testability of Harness
When we say "harness makes agents verifiable," a meta-question is: how is the harness itself verified? If the evaluator uses another LLM, and that LLM is also prone to hallucinations, we have built a loop of "using an unreliable system to verify an unreliable system."

Anthropic's approach is to use computational sensors (test suites, linters, type checkers) for baseline verification whenever possible, activating inferential sensors only for subjective judgments (UI aesthetics, code style). This is a pragmatic layered strategy, but not a perfect solution.

Emergent Behavior of Multi-Agents
When 10 agents run in parallel, each making independent decisions, the system behavior will emergently produce patterns unpredictable by single-agent analysis. This is similar to concurrency bugs in distributed systems—but worse, because every "process" is non-deterministic. Current harness designs mainly target single-agent scenarios, and harness principles for multi-agent collaboration have not yet solidified.

Engineering Trade-offs of Cost and Latency
Every layer of the harness—planner, evaluator, sensor, garbage collection—consumes extra tokens and latency. When the overhead of the harness itself exceeds the quality improvement it brings, it is over-engineering. How to measure the ROI of a harness and how to dynamically adjust the depth of the harness based on task complexity is an unsolved engineering problem.

The New Dimension of Security: Attack Targets Shift from Data to Agency
This is the layer that many articles easily gloss over, but is actually the most dangerous. As agents gain persistent state, external tools, and long-term autonomy, the attack surface is no longer just "what the model answered wrong," but "can the system be manipulated by leveraging it."

Invariant Labs disclosed Tool Poisoning Attacks[10] in April 2025: malicious instructions could be hidden in MCP tool descriptions, invisible to users but visible to the model, thereby inducing the agent to execute unauthorized operations; a week later, they demonstrated a data exfiltration scenario via an untrusted MCP server chaining with a trusted WhatsApp MCP. This means Harness Engineering cannot just talk about throughput and stability, but must squarely address tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation.

Image
The open standardization of MCP is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connections are, the more the upper-layer harness must enforce stricter governance. The harness's permission model must be upgraded from a static "can/cannot" to a dynamic "under what conditions it can, up to what limit, and requiring human confirmation." That is, the harness is not just an outer loop to improve output; it is itself the new security boundary.

Judgments & Outlook
Judgment 1: Harness Engineering will become one of the foundational disciplines of the AI engineering era
Improvements in model capability will continue to swallow up some micro prompt techniques, but will not swallow harness engineering. Because it deals with higher-level problems: how to embed unstable, expensive, probabilistic intelligence into a long-term governable engineering system. As long as agents work across time, tools, environments, and human-machine boundaries, the harness will not disappear—instead, it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

Judgment 2: The moat's focus is shifting from model quality up to Harness and system design
When GPT, Claude, and Gemini converge in core capabilities, what determines a product's success is no longer model differences, but harness quality. The hardest proof comes from LangChain: keeping the underlying model unchanged, they improved `deepagents-cli` on Terminal Bench 2.0 from 52.8% to 66.5% just by modifying the harness, a 13.7-point increase, pulling its rank from the outskirts of the Top 30 to the Top 5. This result cannot be exaggerated to "models don't matter anymore," but it is sufficient to show that on top of the same model, the harness is enough to open up a massive systemic gap. The moat's focus is shifting up to harness and system design.

Judgment 3: The migration from Chatbot to AgentOS will not happen overnight
In between, there will be a 2-3 year "AI Browser + Lightweight Harness" phase. Most enterprises will first gain value in this phase, and then gradually evolve toward a heavier AgentOS architecture. Teams trying to jump straight to AgentOS will likely fail due to governance complexity exceeding their capacity.

Judgment 4: The engineer's role is shifting from "code producer" to "designer of autonomous systems"
This is not an unemployment warning, but a capability upgrade requirement. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing anomalies, and consolidating rules—the value of these capabilities will rise sharply. When unsatisfied with an agent's output, the low-level approach is to manually edit the artifact; the high-level approach is to modify the harness so the system automatically does better next time. From in the loop to on the loop, this is the core upgrade path for engineers in the agent era.

Appendix
Three self-check questions for practitioners. Before starting to build your own harness, answer these three questions first:

Does your agent have durable state surfaces? Can it resume within 30 seconds of a cold start—or does it start from scratch every time?
Does your system have machine-readable acceptance criteria? Is the definition of "done" the agent's own feeling, or an external structured verification surface—a feature list, a set of test cases, a checkable pass/fail status?
Are your repo, tools, logs, metrics, and policies legible and enforceable for the agent? Or are they only readable by humans—leaving the agent to guess?
If you have none of these three, you're likely just building "a chatbot that can run commands"...
