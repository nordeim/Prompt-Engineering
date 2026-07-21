Background
First, let us answer a prerequisite question: How did we get to where we are today?

To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, one must first clearly see the complete arc that AI engineering has traversed over the past four years. This arc is not linear, but rather a cycle of capability jumps → collapse of old frameworks → emergence of new abstractions.

Recommended reading to supplement additional background knowledge:

AI Operating System: From Instruction to Intent
From Prompt Engineering to Context Engineering
The Token Naming Dilemma: When Information Theory Crashes into Linguistics
OpenClaw: The Hidden Dangers Behind the Madness
In-Depth Analysis: Google Workspace CLI
Meta-Skills: Making AI Think Like You
Brief Thoughts on Agent Trends: Native & CLI-Oriented
AI Programming Ecology: What Anthropic's Acquisition of Bun Means
Deep Thinking: Chatting About AI Development Trends
A Brief Discussion on AI Browsers
In-Depth Analysis: Anthropic MCP Protocol

Act I: Generation (2022.11 — 2023)
On November 30, 2022, ChatGPT was launched. It reached approximately 100 million monthly active users about two months after its launch. But what this event truly changed was not NLP technology—GPT-3 had already existed for two years—but the interaction paradigm. Before this, the LLM was an API that only engineers could use; after this, it became a conversational interface that everyone could use.

The core contradiction in this act was: the model could generate, but could not act. It could write an email, but could not send it; it could write a piece of code, but could not run it. The relationship between the user and the model was "you ask, I answer"—a stateless, single-turn, passive exchange of information.

The engineering artifact was Prompt Engineering: how to ask in order to make the model answer better. Few-shot, chain-of-thought, and role-playing were essentially ways to maximize information density within the limited space of a single API call.

Act II: Connection (2023 — 2024)
In March 2023, OpenAI released GPT-4, bringing multimodality and longer context windows. In the same month, ChatGPT Plugins were launched, allowing the model to "grow hands" for the first time—it could call external APIs and access real-time data. In June, OpenAI officially released the Function Calling API, standardizing tool invocation into structured JSON within the model's output.

This was a critical turning point: the model evolved from "able to speak" to "able to connect." However, the Plugins ecosystem quickly exposed its fragility—each plugin required an independent OAuth flow, an independent schema definition, and independent error handling. Connecting 10 plugins was already very painful; 100 was simply impossible.

In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with a layer of intermediate abstraction. It did indeed lower the barrier to entry, but it also introduced the cost of over-abstraction—too many layers of wrapping, difficult debugging, and unpredictable performance. During the same period, projects like AutoGPT and BabyAGI attempted to let models autonomously execute tasks in a loop, but all quickly faded after demos due to a lack of reliable stopping conditions and verification mechanisms.

🤯 Lesson One
Allowing a model to "connect to tools" is necessary, but far from sufficient. Connection does not equal orchestration, and orchestration does not equal governance.

Act III: Reasoning (2024)
The year 2024 was the year "reasoning models" made their debut. OpenAI's o1 series, released in September, featured "spending more time thinking before answering" as its core characteristic, achieving a qualitative leap in mathematical and programming tasks. In December, ARC Prize announced that OpenAI o3 reached 87.5% on the ARC-AGI-1 Semi-Private Eval under a high-compute configuration, shocking the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet performed outstandingly in code generation and long-document understanding, and DeepSeek-R1, as an open-weight model, proved that high-performance reasoning was no longer a closed-source patent.

More importantly, two events occurred at the end of 2024:

First: Anthropic released the Model Context Protocol (MCP). This was not just another plugin system, but an open standard protocol that used JSON-RPC 2.0 to define how AI applications communicate with external tools and data sources. Its core insight was: the connection problem is essentially an N×M problem—N AI applications × M data sources, with each combination requiring a custom connector. MCP simplified this into N+M: each application implements the MCP client once, and each tool implements the MCP server once. Later, OpenAI and Google DeepMind successively announced support for MCP, and in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation.

Second: Anthropic released the "Building Effective Agents"[1] guide (December 2024). This article systematically discussed engineering patterns for agents for the first time—from the simplest prompt chaining to the evaluator-optimizer loop—and explicitly proposed a principle: use the simplest pattern first, and introduce more structure only when complexity demonstrably yields better results. This principle later became one of the core guiding ideologies of harness engineering.

By 2025, Anthropic elevated context engineering to an independent engineering practice, "Effective context engineering for AI agents"[2], emphasizing that the real difficulty was no longer just "how to write prompts," but "what information, in what format, and at what timing to hand over to the model at each step." This was the critical transition layer between Prompt Engineering and Harness Engineering—the problem had shifted upward from "single invocation" to "per-step context," but had not yet shifted upward to the "entire task outer loop."

🤯 Lesson Two
The reasoning capability of models solves the "single-step quality" problem, but the reliability of long tasks is not automatically obtained just because single steps are smarter. A model capable of solving IMO gold-medal problems will still "forget what it is doing" halfway through a four-hour full-stack development task.

Act IV: Action (2025)
If 2023 was the year of the Chatbot and 2024 was the year of multimodality, then 2025 was the year of the Agent.

Early in the year, the open-source release of DeepSeek-R1 forced the market to re-evaluate the competitive landscape of models. This was followed by a series of agent products: Claude Code (a programming agent in the terminal), GitHub Copilot Agent Mode, Cursor's autonomous coding loop, Manus (a browser operation agent), and OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all mainstream languages. Google released the Agent2Agent (A2A) protocol to solve cross-vendor communication between agents.

However, the most important discovery of 2025 was not what agents could do, but how agents broke down while doing it:

- The agent attempts to complete the entire task in one go (all at once) and exhausts the context window halfway through.
- The agent announces "all done" after completing 70% and then stops.
- Multiple agents running in parallel produce cascading errors, where a single small error is amplified into an undebuggable state.
- The codebase develops severe "AI slop" after agents work continuously—redundant code, inconsistent naming, and outdated documentation.

These are not intelligence problems of the model, but structural problems of the system.

🤯 Lesson Three
The capability of agents has reached a level where they "can work autonomously for hours," but the engineering infrastructure surrounding them remains stuck in the "single-turn conversation" era. This fracture is the root cause of the birth of Harness Engineering.

Act V: Governance (2026 — Present)
At the start of 2026, the industry's attention began to shift from "how to make agents more capable" to "how to keep agents from derailing." "Harness Engineering," as a public term, was not suddenly invented on a specific day, but rather rapidly formed and proliferated beginning in February 2026:

- On February 5, 2026, Mitchell Hashimoto explicitly wrote "Engineer the Harness" in "My AI Adoption Journey"[3]—this is considered one of the starting points for the term entering mainstream discussion.
- On February 11, 2026, OpenAI published an engineering article directly titled "Harness Engineering: Leveraging Codex in an Agent-First World"[4]. They used a small team to build an internal beta product from an empty repository in five months; the public statement was "zero lines of manually written code," with the repository reaching the magnitude of approximately one million lines of code and generating about 1,500 PRs. More accurately, the initial scaffold was still generated by Codex under the guidance of a small number of templates, after which application logic, testing, CI, documentation, observability, and internal tools were produced by agents as much as possible. Core finding: engineers' focus shifted to designing environments, specifying intent, and building feedback loops.
- In March 2026, Anthropic published "Harness Design for Long-Running Application Development", upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, proving that evaluators still yield significant gains near the boundaries of model capabilities.
- In April 2026, the Thoughtworks / Fowler system ("Harness Engineering - first thoughts"[5]) systematized this concept into a more complete methodological framework—a combination of guides (feed-forward control) and sensors (feedback control), each further divided into computational (deterministic) and inferential categories, forming a 2×2 control matrix. Therefore, April is better understood as the point when "methodological abstraction became complete," rather than "the first naming."

What exactly is a Harness?
Let us deduce from first principles, rather than starting from definitions.

The Five Fundamental Challenges of Agents
The essence of an agent is "a system that autonomously advances goals in an open environment." This definition implies five engineering challenges, none of which can be solved solely by a smarter model:

- State Durability
Essence: Agents need to remember what they have done across time and across sessions.
Why models cannot solve it: Models themselves are stateless, and the context window has a hard limit, making them naturally unable to bear long-term continuous states.

- Goal Alignment
Essence: In long tasks, agents are prone to drifting, hallucinating goals, or even prematurely announcing completion.
Why models cannot solve it: Models lack external anchors and cannot stably calibrate "what truly counts as done."

- Action Verifiability
Essence: Every step is probabilistic; there needs to be a distinction between "did it" and "did it right."
Why models cannot solve it: Models naturally possess a tendency toward self-praise and misjudgment when evaluating their own results.

- Entropy Control
Essence: Continuous output will constantly accumulate redundancy, drift, and inconsistency.
Why models cannot solve it: Models will replicate existing patterns, even if those patterns themselves are bad or of low quality.

- Human-Machine Boundary
Essence: When to be autonomous and when to hand over to humans needs to be explicitly and programmatically defined.
Why models cannot solve it: Models lack reliable "uncertainty self-awareness" and cannot stably judge when to stop and hand back to humans.

Harness is the engineering practice that systematically answers these five challenges.

A Precise Definition
Anthropic provided a definition highly worthy of direct adoption in "Demystifying evals for AI agents"[6]: an agent harness (or scaffold) is the system that enables the model to act as an agent; it is responsible for processing inputs, orchestrating tool calls, and returning results. More crucially, Anthropic further pointed out: when we evaluate "an agent," we are actually evaluating the combination of the model + harness, not the isolated capability of the model. This definition is extremely important because it shifts the unit of explanation for agent effectiveness from model parameters to the outer loop structure in which the model resides.

Image

A frequently confused concept must be unpacked here: an agent harness and an evaluation harness are not the same thing. The former is responsible for running the agent (processing inputs, orchestrating tools, managing state), while the latter is responsible for running tasks in batches, recording trajectories, executing graders, and aggregating scores. Many discussions toss "harness" into one big basket, resulting in talking about runtime orchestration one moment and evaluation pipelines the next. The Harness Engineering discussed in this article refers to the former—the engineering of the runtime outer loop system.

Based on this, a more precise formulation is:

📌
Harness = The outer loop system that enables a model to act as an Agent.

It encompasses plan decomposition, persistent state, tool orchestration, verification gating, feedback loops, fallback mechanisms, human-machine handover points, and audit logs. When evaluating an agent's effectiveness, one evaluates the combination of model + harness, not the model itself.

A few key points here are worth expanding upon:

- Outer loop is the keyword. The model's reasoning is the "inner loop"—given context, generate the next step. The harness is the "outer loop"—deciding when to start a new inner loop, what context to give it, how to verify its output, when to fall back, and when to stop. The quality of the inner loop depends on model capability; the quality of the outer loop depends on harness design.
- A harness is not an upgraded version of a prompt. A single prompt cannot solve cross-session states, verification gates, tool discovery, failure recovery, and continuous entropy control. Treating a harness as "a longer system prompt" is currently the most common failure mode.
- A harness is also not a framework name. LangChain is a framework, CrewAI is a framework, Harness Engineering is not. It is a practice, just as DevOps is not a tool but an engineering culture.

Three Layers of Engineering Abstraction
Prompt → Context → Harness

To understand the position of a harness, one must first see clearly its relationship with the previous two layers. These three layers are not substitutes for one another, but rather progressive levels of abstraction:

Image

📌 Key Insight
Context Engineering is about "what to feed at each step," while Harness Engineering is about "how the entire pipeline runs." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context engineering; however, a harness also encompasses multi-step structures, tool mediation, verification gates, and durable state—these exceed the scope of single-step context.

The Six Major Engineering Components of a Harness
This section is the most hardcore part of the entire article. For each component, it will clearly explain what problem it solves, the specific practices of Anthropic/OpenAI, and the underlying design principles.

Durable State Surfaces: Curing Agents of "Amnesia on the Job"
Problem: The core pain point of a long-running agent is like an engineer in a project team suffering from complete amnesia every time they change shifts. The context window is limited, complex projects cannot be completed within a single window, and the agent needs a way to bridge the chasm between sessions.

Anthropic's Solution: They did not attempt to build an "infinitely long context," but rather externalized the state into continuable artifacts:

- The first initializer agent sets up the environment: creating `init.sh` (startup script), `claude-progress.txt` (progress log), and an initial `git commit` (baseline snapshot).
- Generates a feature list: expands high-level requirements into 200+ specific features, initially all marked as failing.
- Subsequent coding agents only make incremental progress, leaving structured updates and a "clean state" when the session ends.
- Key rule: The agent can only change the `passes` status of a feature; it cannot arbitrarily modify the test definition itself.

This feature list design looks "crude," but it is extremely effective—it shifts the definition of "done" from the agent's subjective feeling to an external, persistent, structured, and inheritable completion surface. The agent does not need to "remember" what it did previously; it only needs to read the feature list and git diff to resume work within 30 seconds.

Anthropic later discovered a deeper problem: context anxiety. Even with compaction (summarizing early conversations), agents would still exhibit behavioral degradation because they felt the "context was too full." The solution was not better compaction, but a context reset—directly giving the next agent a completely new context, passing all necessary information through externalized state artifacts (rather than conversation history). This is more radical than compaction, but yields better results.

📌 Design Principle
State ≠ "saving chat history." True durable state consists of structured artifacts that an agent can read, understand, and resume from after a cold start, without any context history. If your agent cannot know "where it left off last time and what to do next" within 30 seconds of a cold start, your state management has failed.

Decomposition & Plans: Slicing Long Tasks into Chunks the Agent Can Digest
Problem: Tell an agent to "build a clone of claude.ai," and it will attempt an all-at-once approach—trying to write all the code in a single session. The result is either a blown context window or an announcement of "done" halfway through.

Evolutionary Process:

- In November 2025, Anthropic initially solved this problem using an initializer + coding two-role structure. The initializer handles decomposition and setup, while the coding agent handles step-by-step implementation.
- In March 2026, this structure was upgraded to a planner / generator / evaluator three-role system:

  - The Planner does not write code directly, but expands one or two sentences of high-level description into a complete product spec and a step-by-step feature list.
  - The Generator is responsible for implementing features one by one, committing each time one is completed.
  - The Evaluator is responsible for independently assessing the generator's output, marking pass/fail, and providing specific suggestions for improvement.

OpenAI's counterpart to this is `PLANS.md`, `Implement.md`, and `Documentation.md`—complex tasks are planned first, execution runs by milestones, verification is performed at each stage, and documentation is continuously updated as shared memory.

📌 Design Principle
Plans must be elevated to first-class artifacts, not one-off chat content. They need to be written to the file system, version-controlled, readable by subsequent agents, and referenced by verification gates. A plan that exists only in a conversation is essentially not a plan—it is merely a passing thought.

Feedback Loops: Guides and Sensors
Problem: After an agent writes code, how does it know if it wrote it correctly? Relying on the agent to evaluate itself? Anthropic explicitly discovered an embarrassing fact: when asked to evaluate its own work, an agent tends to enthusiastically praise itself—even when the quality is clearly mediocre to a human.

This necessitates a feedback system that does not rely on the agent's self-evaluation. By April 2026, frameworks in the community had already broken down the harness into a very clear 2×2 matrix:

Image

Guides constrain the agent before it acts, increasing the probability of "getting it right the first time." Sensors provide signals after the agent acts, supporting self-correction.

Image

Key Insights:

- Guides without sensors → The agent has the rules encoded but never knows if they took effect.
- Sensors without guides → The agent repeatedly makes the same mistakes and is subsequently corrected.
- Computational controls are cheap, fast, and deterministic; they can run on every change.
- Inferential controls are expensive, slow, and non-deterministic, but can handle subjective judgments (e.g., "Is this UI design too ugly?").

Anthropic's evaluator-optimizer pattern is entirely consistent with this. They also acknowledged a subtle fact: evaluators are not perpetually necessary—when the base model's capabilities cross a certain threshold, the evaluator degrades from a "necessary component" to "additional overhead." This indicates that a good harness is not a fixed template, but a tailorable system that co-evolves with the model's capability boundaries.

Image

Legibility: Building a Perception Surface for the Agent
Problem: The agent can write code, but can it "see" what its code looks like when it runs? Can it read error logs? Can it understand performance metrics?

OpenAI offered an extremely sharp judgment in their harness engineering practice: any knowledge that is not within the agent's visible scope at runtime might as well not exist.

This is not rhetoric. They did the following specific work to improve legibility:

- Launched an independent browser instance for each git worktree, allowing the agent to "see" the UI via CDP (Chrome DevTools Protocol)[7].
- Exposed logs, metrics, and traces completely for the agent to query.
- Repository knowledge as the system of record: design principles, product intent, execution plans, known technical debt, and Architecture Decision Records (ADR) were all put into the repo, with consistency maintained via lint/CI.
- Placed `AGENTS.md`, structured `docs/`, execution plans, and knowledge documents into the repo as much as possible, making them a versioned system of record; however, OpenAI also publicly warned: an overly long `AGENTS.md` will quickly rot, crowd the context, and cause all constraints to lose focus simultaneously—a better approach is to turn it into a directory index, scattering the actual knowledge into structured documents.

📌 Design Principle
Legibility is not about "making code more elegant," but about bringing knowledge, constraints, acceptance criteria, and decision history into the agent's perception surface. This directly transforms "knowledge management" from a team collaboration problem into an agent executability problem. For an agent, experience in Slack, orally transmitted architectural boundaries, and constraints scattered in external documents simply do not exist if they do not enter the artifact surface accessible at runtime.

Tool Mediation: The More Tools, the More a Harness is Needed
Problem: Following the explosion of the MCP ecosystem, an agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions directly into the context creates severe problems—token costs skyrocket, latency increases, and the agent loses its way in a sea of tools.

In their engineering practice with MCP + Code Execution, Anthropic proposed a core approach: do not let the model call tools directly; let the model write code to call tools.

What is the difference?

- Direct tool invocation mode: All tool definitions are loaded into the context → the model selects a tool → invokes it → the result is passed back into the context → the model continues. Every step consumes context space, and intermediate results cycle within the model's inner loop.
- Code execution mode: The model writes a piece of code → the code runs in a sandbox, discovering and calling MCP tools on demand → only the final result is passed back to the model. Tool discovery, data filtering, and intermediate processing are all completed within the execution environment and do not enter the context.

The essence of this approach is: moving tool usage out of the model's inner loop and into a more efficient external execution loop. This is exactly what harness engineering is—it is not a "tool registry," but a system-level design that dictates how tools are discovered, when they are exposed, at what granularity they are exposed, whether results need to enter the context, where state is stored, and how failures fall back.

Entropy Control: Continuous Garbage Collection for Agents
Problem: Fully automated agent codebases will continually copy existing patterns—even if those patterns are uneven, suboptimal, or terrible. Over time, drift and entropy growth are inevitable.

OpenAI spoke most plainly about this: initially, they relied on humans spending about 20% of their time every week cleaning up "AI slop" (redundant code, outdated documents, inconsistent naming, copy-pasted dead code). Later, they systematized this cleanup logic:

- Documentation consistency agents periodically verify whether documentation and code align.
- Refactor agents clean up technical debt according to schedules.
- Architectural enforcement mechanically maintains module boundaries via CI.

📌 Design Principle
A harness is not only responsible for "making the agent run," but also for continuously suppressing the systemic noise amplified by the agent. This is its most fundamental difference from a simple "agent framework"—frameworks care about startup and orchestration, while harnesses care about long-term governability.

Harnessability: Not Every System is Easily Harnessed
If Harness Engineering is understood solely as "adding more rules and loops to the agent," it is not deep enough. The more fundamental issue is: not every system is equally easy to harness.

OpenAI's practice constantly hints at the same thing: they were able to push Codex to high throughput not just because the model was strong enough, but because they continuously compressed knowledge back into the repo, turned plans into artifacts, versioned decisions, and made environments more readable to agents. How naturally suited a system is to being tamed by an agent is, in itself, a crucial variable.

Following this logic, one arrives at a highly explanatory judgment: systems that are strongly typed, comprehensively tested, clearly bounded, versioned in documentation, and observable at runtime naturally possess higher harnessability; whereas systems where knowledge is scattered in human brains, chat tools, and word of mouth will, no matter how strong the model, first hit the wall of "invisible → incomprehensible → ungovernable."

This means that in the agent era, the quality of a team's engineering infrastructure (CI completeness, documentation structure, architectural boundary clarity) is no longer just a matter of "engineering literacy"—it directly determines how far agents can go on your system. Harnessability will become the critical dimension for evaluating a system's "agent-readiness."

Intent Systems
A Deeper Paradigm Shift: From Instruction-Driven to Intent-Driven

What was discussed above are the engineering components of a harness. But looking only at the components leads to being bogged down in "the splicing of technical details." Let us take a step back and discuss a more fundamental matter—why Harness Engineering is not just an engineering practice, but the product of a paradigm shift.

The Four Fractures of Human-Machine Interaction
Reviewing the entire history of computing, the interaction between humans and machines has experienced four fundamental fractures:

- CLI (Command Line Interface): Humans must precisely master the machine's language. `ls -la | grep .py` is an instruction; getting a single character of syntax wrong causes failure. The core assumption of the interaction is "the human adapts to the machine."
- GUI (Graphical User Interface): The machine lowers the barrier via visual metaphors. Folders, desktops, drag-and-drop. The core assumption of the interaction is "the machine presents itself using metaphors humans can understand."
- App (Mobile Application): Logic is solidified into fixed interfaces. One function per button, one screen per button. The core assumption of the interaction is "the human chooses from pre-set paths."
- Agent (Intent-Driven): Humans only express goals, and the system autonomously plans execution paths. The core assumption of the interaction is "the machine understands human intent and autonomously decides how to act."

Every fracture is not merely a technological upgrade, but a reallocation of control. In the CLI era, humans possessed 100% control; in the Agent era, humans concede most execution control, retaining only goal setting and key decision points.

What is the engineering consequence of this concession?

In an instruction-driven world, a bug is "the system did not execute my instruction correctly"—this can be covered by traditional testing. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly understood the intent but chose a terrible execution path"—this requires an entirely new set of verification, constraint, and feedback mechanisms, and this is exactly the problem a harness is meant to solve.

Applications are being "CLI-ified," but not for humans
A highly counter-intuitive trend: in the Agent era, all applications and websites are being re-"CLI-ified"—not to send users back to the terminal, but to turn everything into programmable interfaces from the Agent's perspective.

The essence of MCP is the protocol-layer implementation of this very thing. When an agent needs to operate Google Drive, it does not need to "open a web page and click buttons"—it needs a set of structured API calls. The MCP server abstracts Google Drive into a set of callable functions: `gdrive.getDocument`, `gdrive.createFile`, `gdrive.search`.

This means three things:

First, the target of legibility has changed. In the past, legibility was for humans to see—clear UIs, reasonable information architecture. Now, it must first be for agents to see—structured APIs, machine-parseable documentation, programmable permission models.

Second, the boundaries of applications are dissolving. When an agent calls any tool via MCP or collaborates with other agents via A2A, the App degrades from a "destination" to "infrastructure." The user no longer "opens an App to do a thing," but rather "expresses an intent, and the Agent orchestrates multiple services to complete it."

Third, the harness becomes the new "operating system layer." The operating system of the GUI era managed windows, files, and processes. What needs to be managed in the Agent era is: the lifecycle of the agent, the discovery and authorization of tools, the scheduling and recycling of context, the collaboration and isolation of multiple agents, and the intervention points for human approval.

From Chatbot to AgentOS
Stringing all the above clues together reveals a clear evolutionary path. These three stages are not feature additions, but fundamental changes in engineering abstraction layers:

Level 1: Chatbot (2022-2023)
Single-turn conversations, stateless, humans fully in the loop. The core value is information retrieval and content generation. The engineering abstraction layer is Prompt Engineering. Representative products: ChatGPT, Claude (early).

Ceiling: Can speak but cannot do. Every conversation is isolated.

Level 2: AI Browser / Agent IDE (2024-2025)
Multi-step tasks, tool invocation, limited autonomy. The core value is task execution and workflow automation. The engineering abstraction layer is Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus, Codex.

Ceiling: Strong single-agent capability but unstable on long tasks; multi-agent collaboration lacks standards; state management is manual work.

Level 3: AgentOS (2026- Germination period, forward-looking direction)
Restraint must be exercised here. AgentOS is not yet a converged industrial paradigm. However, it has indeed entered the agenda of research and systems communities. The 2024 AIOS[8] paper proposed extracting scheduling, context management, memory management, and access control from the agent application layer into a kernel-like layer; ASPLOS 2026 featured a dedicated AgenticOS Workshop[9] to explore OS primitives for agent workloads.

Image

Therefore, a safer statement is not "AgentOS has arrived," but: Harness Engineering is pushing problems from the application layer down to the system layer. When an agent is no longer just a coding assistant, but an always-on, multi-agent, cross-tool, cross-identity long-term executor, the user-space harness will ultimately inevitably hit deeper system problems:

- Agent lifecycle management: Initialization, execution, suspension, resumption, termination—this is not stateless function invocation, but full process management.
- Context scheduling: The context window is a scarce resource; decisions must be made regarding what information to load when, when to compress, and when to discard—this is the agent version of "memory management."
- Multi-agent isolation and collaboration: One agent's operations should not pollute another's environment, yet they need to share certain states—a mechanism akin to process isolation + IPC is needed.
- Governance and auditing: Every decision at every step of every agent needs to be traceable—in fields like finance and healthcare, this is not icing on the cake, but a compliance requirement.

Image

📌 Key Positioning
The harness is the user-space layer of an AgentOS. AgentOS is the kernel—managing scheduling, isolation, and resources. The harness is the user-space shell and daemon—managing task decomposition, state continuation, verification feedback, and human-machine handovers. The two are not in competition; they are naturally upper and lower layers.

Five Typical Symptoms
With the theory out of the way, let us return to reality. If you observe the current ecosystem, you will find that most so-called "agent systems" are actually still in the makeshift stage. Here are five typical symptoms:

Symptom 1: The framework jungle. LangChain, CrewAI, AutoGen, Agno, n8n... each framework solves a small piece of the problem, but none provides a complete lifecycle from planning to verification to fallback to auditing. Users cobble things together across different frameworks, resulting in a fragile pipeline rather than a governable system.

Symptom 2: Chatbot skin + Agent core. A massive number of products are essentially a chatbot interface wrapped around an agent loop—yet lack true state management, task decomposition, and verification gates. They dazzle in demos but frequently derail in production.

Symptom 3: Tool registration ≠ Tool governance. MCP makes connection easy, but "able to connect" does not equal "knowing how to use." Faced with 50 tools, an agent will get confused, make redundant calls, and take detours. Some engineering teams found that initially providing an agent with all tools actually yielded very poor results—improvements only came after paring them down to the minimum necessary set.

Symptom 4: One-off rules vs. Evolvable constraints. The agent configuration for most teams is a massive `AGENTS.md` or system prompt. But practice has shown this approach inevitably fails—when everything is important, nothing is important. The agent will pattern-match locally rather than navigate consciously. Rules rot faster than humans can maintain them.

Symptom 5: Lack of on-the-loop thinking. "In the loop" is manually modifying the artifact when dissatisfied with the agent's output; "on the loop" is modifying the harness so the system automatically produces better results next time. Most teams are still stuck "in the loop"—fixing individual errors rather than systematically improving the control loops that produced them.

What a Harness is Not
Clarifying boundaries is just as important as clarifying definitions.

It is not "swapping in a longer system prompt." Because a single prompt cannot solve cross-session states, verification gates, tool discovery, failure recovery, and continuous entropy control.

It is not a proprietary term of any specific vendor. Both Anthropic and OpenAI are using it publicly, and academic preprints are already abstracting it into a cross-product general concept.

Neither is it something that "will no longer be needed once models get stronger." Quite the opposite—Anthropic explicitly points out that a harness will reallocate value as model boundaries shift outward: some checks will become redundant, but planning, verification, handoff, and state governance will become even more important for harder tasks. The stronger the model, the greater the need to place longer, more expensive, and more dangerous tasks into a controlled outer loop.

In reality, the space for interesting harness combinations will not shrink as models get stronger—it will move. Evaluators that are effective today might become redundant overhead in the face of next-generation models, but new capability boundaries will spawn new harness demands.

Overlooked Key Issues
The testability of the harness
When we say "a harness makes an agent verifiable," the meta-question is: how is the harness itself verified? If the evaluator uses another LLM, and that LLM also has hallucination tendencies, we have built a loop of "using an unreliable system to verify an unreliable system."

Anthropic's approach is to rely as much as possible on computational sensors (test suites, linters, type checking) for basic verification, only enabling inferential sensors for subjective judgments (UI aesthetics, code style). This is a pragmatic layered strategy, but not a perfect solution.

The emergent behavior of multi-agents
When 10 agents run in parallel, making independent decisions, the system behavior will exhibit emergent patterns that single-agent analysis cannot predict. This is akin to concurrency bugs in distributed systems—but worse, because every "process" is non-deterministic. Current harness designs primarily target single-agent scenarios; harness principles for multi-agent collaboration have not yet been established.

Engineering trade-offs of cost and latency
Every layer of a harness—planner, evaluator, sensor, garbage collection—consumes additional tokens and latency. When the overhead of the harness itself exceeds the quality improvements it brings, it is over-engineering. How to measure the ROI of a harness and how to dynamically adjust the depth of the harness based on task complexity remain unsolved engineering problems.

The new dimension of safety: The attack target has shifted from data to agency
This is the layer that many articles gloss over most easily, yet it is actually the most dangerous. As agents gain persistent state, external tools, and long-term autonomy, the attack surface is no longer just "what did the model answer incorrectly," but rather "can the system be leveraged and manipulated."

Invariant Labs disclosed Tool Poisoning Attacks[10] in April 2025: malicious instructions can be hidden within MCP tool descriptions, invisible to users but visible to the model, thereby inducing the agent to execute unauthorized operations; a week later, they demonstrated a data exfiltration scenario via an untrusted MCP server linking to a trusted WhatsApp MCP. This means Harness Engineering cannot just discuss throughput and stability; it must also directly address tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation.

Image

MCP's open standardization is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connection becomes, the more strictly the upper-layer harness must govern. The harness's permission model must upgrade from a static "can/cannot" to a dynamic "under what conditions it can, up to what limit it can, and only after human confirmation it can." In other words, a harness is not just an outer loop that improves output; it is itself a new safety boundary.

Judgments & Outlook
Judgment 1: Harness Engineering will become one of the foundational disciplines of the AI engineering era
Improvements in model capabilities will continuously swallow up some micro-level prompt techniques, but they will not swallow up harness engineering. This is because it deals with higher-level problems: how to embed an unstable, expensive, and probabilistic intelligence into a long-term governable engineering system. As long as agents need to work across time, tools, environments, and human-machine boundaries, the harness will not disappear—instead, it will increasingly resemble the intersection of software architecture, test engineering, SRE, and security engineering.

Judgment 2: The center of gravity for moats is shifting upward from model quality to Harness and system design
When GPT, Claude, and Gemini converge in core capabilities, what determines product success or failure will no longer be model differences, but harness quality. The hardest evidence comes from LangChain: while keeping the underlying model unchanged, they improved `deepagents-cli` on Terminal Bench 2.0 from 52.8% to 66.5% simply by modifying the harness—an increase of 13.7 points, pulling its rank from outside the Top 30 into the Top 5. This result should not be exaggerated into "models no longer matter," but it is enough to show: on top of the same model, a harness is sufficient to widen massive systemic gaps. The center of gravity for moats is shifting upward to harness and system design.

Judgment 3: The migration from Chatbot to AgentOS will not happen in one step
There will be a 2-3 year intermediate phase of "AI Browser + Lightweight Harness." Most enterprises will first capture value in this phase and then gradually evolve toward heavier AgentOS architectures. Teams that attempt to jump straight to an AgentOS will highly likely fail because the governance complexity will exceed their capacity to bear it.

Judgment 4: The engineer's role is shifting from "code producer" to "designer of autonomous systems"
This is not a warning of unemployment, but a demand for capability upgrades. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing anomalies, and solidifying rules—the value of these capabilities will rise sharply. When dissatisfied with an agent's output, the low-level approach is to manually modify the artifact; the high-level approach is to modify the harness so the system automatically does better next time. From *in the loop* to *on the loop*—this is the core upgrade path for engineers in the agent era.

Appendix
Three self-check questions for practitioners. Before starting to build your own harness, answer these three questions first:

1. Does your agent have durable state surfaces? After a cold start, can it resume work within 30 seconds—or does it start from scratch every time?
2. Does your system have machine-readable acceptance criteria? Is the definition of "done" based on the agent's own feeling, or is it an external structured verification surface—a feature list, a suite of test cases, an inspectable pass/fail state?
3. Are your repo, tools, logs, metrics, and policies legible and enforceable to the agent? Or can only humans read them—leaving the agent to guess?

If you have none of these three things, what you are building is highly likely still just a "chatbot that can run commands"...

---

https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221o5BkK6hTvxH_VzWgD3h3mIKaY1as0J8H%22%5D,%22action%22:%22open%22,%22userId%22:%22103961307342447084491%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing 
