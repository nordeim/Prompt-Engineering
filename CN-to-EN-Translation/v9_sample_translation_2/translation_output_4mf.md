Background 
 
To answer a prerequisite question first: how did we get here? 
 
To understand why Harness Engineering suddenly became a seriously discussed engineering practice in 2026, you first need to see the full arc that AI engineering has traveled over the past four years. This arc is not linear — it is a   
repeating cycle of capability leap → old framework collapse → new abstraction emerges. 
 
Recommended reading for additional background: 
 
- AI Operating Systems: From Instructions to Intent 
- From Prompt Engineering to Context Engineering 
- The Token Naming Dilemma: When Information Theory Invades Linguistics 
- OpenClaw: The Hidden Risks Behind the Madness 
- Deep Dive: Google Workspace CLI 
- Meta-Skills: Making AI Think Like You 
  -浅思 on Agent Trends: Native-ification & CLI-ification 
- The AI Programming Ecosystem: What Does Anthropic's Acquisition of Bun Mean? 
- Deep Reflections: On AI Development Trends 
- A Brief Look at AI Browsers 
- Deep Dive: Anthropic's MCP Protocol 
 
Act One: Generation (November 2022 — 2023) 
 
On November 30, 2022, ChatGPT went live. It reached roughly 100 million monthly active users within about two months. But what truly changed was not NLP technology — GPT-3 had already existed for two years — it was the interaction 
paradigm. Before this, the LLM was an API; only engineers could use it. After this, it became a conversational interface that everyone could use. 
 
The core contradiction in this act was: the model could generate, but it could not act. It could write an email but not send it; it could write a code snippet but not run it. The relationship between user and model was "you ask, I 
answer" — a stateless, single-turn, passive exchange of information. 
 
The engineering output was Prompt Engineering: how to ask questions so the model answers better. Few-shot, chain-of-thought, role-playing — all of these were fundamentally about maximizing information density within the limited space  
of a single API call. 
 
Act Two: Connection (2023 — 2024) 
 
In March 2023, OpenAI released GPT-4, bringing multimodality and longer context windows. That same month, ChatGPT Plugins launched, giving the model "hands" for the first time — the ability to call external APIs and access real-time   
data. In June, OpenAI released the Function Calling API, standardizing tool invocation as structured JSON in the model's output. 
 
This was a pivotal turning point: the model evolved from "can speak" to "can connect." But the Plugins ecosystem quickly revealed its fragility — each plugin required its own OAuth flow, its own schema definition, its own error 
handling. Connecting 10 plugins was already painful; 100 was simply impossible. 
 
In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with a layer of intermediate abstraction. It did lower the barrier to entry, but it also introduced the cost of over-abstraction —  
too many wrapper layers, difficult debugging, unpredictable performance. Around the same time, projects like AutoGPT and BabyAGI tried to let models autonomously loop through tasks, but all of them quickly faded after their demos 
because they lacked reliable stopping conditions and verification mechanisms. 
 
│ 🤯 Lesson One 
│ Making models "able to connect to tools" is necessary, but far from sufficient. Connection is not orchestration, and orchestration is not governance. 
 
Act Three: Reasoning (2024) 
 
2024 was the year "reasoning models" arrived. OpenAI's o1 series launched in September, featuring the core characteristic of "spending more time thinking before answering," achieving a qualitative leap in mathematics and programming   
tasks. In December, the ARC Prize revealed that OpenAI o3 achieved 87.5% on the ARC-AGI-1 Semi-Private Eval under a high-compute configuration, stunning the entire community. Meanwhile, Anthropic's Claude 3.5 Sonnet excelled at code   
generation and long-document understanding, and DeepSeek-R1, as an open-weights model, proved that high-performance reasoning was no longer the exclusive domain of closed-source models. 
 
More importantly, two things happened at the end of 2024: 
 
First: Anthropic released the Model Context Protocol (MCP). This was not yet another plugin system but an open standard protocol that used JSON-RPC 2.0 to define how AI applications communicate with external tools and data sources.    
Its core insight was: the connection problem is fundamentally an N×M problem — N AI applications × M data sources, each combination requiring a custom connector. MCP reduced this to N+M: each application implements one MCP client, 
each tool implements one MCP server. Later, OpenAI and Google DeepMind both announced support for MCP. In December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation. 
 
Second: Anthropic released the "Building Effective Agents"[1] guide (December 2024). This article was the first to systematically discuss engineering patterns for agents — from the simplest prompt chaining to the evaluator-optimizer   
loop — and explicitly articulated a principle: start with the simplest pattern, and only introduce more structure when complexity genuinely produces better results. This principle later became one of the core guiding ideas of Harness  
Engineering. 
 
By 2025, Anthropic further elevated Context Engineering into a standalone engineering practice with "Effective Context Engineering for AI Agents"[2], emphasizing that the real difficulty was no longer just "how to write prompts" but   
"at each step, what information, in what form, at what moment to give to the model." This was the critical transitional layer between Prompt Engineering and Harness Engineering — the problem had moved up from "single call" to 
"per-step context," but had not yet moved up to "the entire task's outer loop." 
 
│ 🤯 Lesson Two 
│ A model's reasoning ability solves "single-step quality," but the reliability of long tasks is not automatically gained simply because each step is smarter. A model that can solve IMO gold-medal problems will still "forget what it   
│ was doing" midway through a four-hour full-stack development task. 
 
Act Four: Action (2025) 
 
If 2023 was the year of chatbots and 2024 was the year of multimodality, then 2025 was the year of agents. 
 
At the start of the year, the open-source release of DeepSeek-R1 caused the market to reassess the landscape of model competition. This was followed by a wave of agent products: Claude Code (a terminal-based coding agent), GitHub 
Copilot Agent Mode, Cursor's autonomous coding loops, Manus (a browser-operation agent), and OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers and SDKs covering all major languages. 
Google released the Agent-to-Agent (A2A) protocol to solve cross-vendor communication between agents. 
 
But the most important discovery of 2025 was not what agents could do, but how they failed while doing it: 
 
- Agents attempted to complete entire tasks in one shot ("all in one shot"), exhausting their context window midway. 
- Agents announced "all done" after completing 70%, then stopped. 
- When multiple agents ran in parallel, they produced cascading errors, with a single small error amplified into something un-debuggable. 
- Codebases developed severe "AI slop" after sustained agent work — redundant code, inconsistent naming, stale documentation. 
 
These were not problems of model intelligence; they were problems of system structure. 
 
│ 🤯 Lesson Three 
│ Agent capability has reached the level of "can work autonomously for hours," but the engineering infrastructure around it is still stuck in the "single conversation" era. This gap is the root cause of why Harness Engineering was 
│ born. 
 
Act Five: Governance (2026 — Present) 
 
At the start of 2026, the industry's attention shifted from "how to make agents more capable" to "how to prevent agents from crashing." "Harness Engineering" as a public term was not invented overnight on a single day, but rather 
rapidly coalesced and spread starting in February 2026: 
 
- February 5, 2026: Mitchell Hashimoto explicitly wrote "Engineer the Harness" in My AI Adoption Journey[3] — this is considered one of the starting points of the term entering mainstream discussion. 
- February 11, 2026: OpenAI published an engineering article directly titled "Harness Engineering: Leveraging Codex in an Agent-First World"[4]. They described how a small team built an internal beta product from an empty repository   
  over five months, publicly stating "zero lines of human-written code," with the repository reaching roughly one million lines of code and generating approximately 1,500 PRs. More precisely, the initial scaffold was still generated   
  by Codex under light template guidance, after which application logic, tests, CI, documentation, observability, and internal tooling were then尽可能 produced by agents. The core finding: engineers' work shifted toward designing 
  environments, specifying intent, and building feedback loops. 
- March 2026: Anthropic published Harness Design for Long-Running Application Development, upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, demonstrating that the 
  evaluator still delivers significant gains even near the model's capability boundary. 
- April 2026: The Thoughtworks/Fowler lineage (Harness Engineering — first thoughts[5]) systematized this concept into a more complete methodological framework — a combination of guides (feedforward control) and sensors (feedback 
  control), each further divided into computational (deterministic) and inferential (inferential) types, forming a 2×2 control matrix. Therefore, April is better understood as "the point where methodological abstraction became 
  complete," rather than "the first naming." 
 
What Exactly Is a Harness? 
 
Let's derive this from first principles, rather than starting from a definition. 
 
### Five Fundamental Challenges of Agents 
 
An agent is, at its essence, "a system that autonomously advances goals in an open environment." This definition implies five engineering challenges, each of which cannot be solved by a smarter model alone: 
 
State Persistence 
Essence: Agents need to remember what they have done across time and across sessions. 
Why models can't solve it: Models are inherently stateless, and context windows have hard upper limits; they cannot naturally carry long-term continuous state. 
 
Goal Consistency 
Essence: In long tasks, agents tend to drift, engage in self-referential loops, or even declare completion prematurely. 
Why models can't solve it: Models lack external anchors; they cannot stably calibrate "what counts as truly done." 
 
Action Verifiability 
Essence: Every step is probabilistic; you need to distinguish "done" from "done correctly." 
Why models can't solve it: When models evaluate their own results, they have an inherent tendency toward self-congratulation and misjudgment. 
 
Entropy Suppression 
Essence: Continuous output constantly accumulates redundancy, drift, and inconsistency. 
Why models can't solve it: Models replicate existing patterns, even when those patterns are themselves poor or low-quality. 
 
Human-Machine Boundary 
Essence: Knowing when to act autonomously and when to hand off to a human requires clear, engineering-grade definitions. 
Why models can't solve it: Models lack reliable "uncertainty self-awareness"; they cannot stably judge when to stop and hand back to a human. 
 
Harness is the engineering practice that systematically addresses these five challenges. 
 
### A Precise Definition 
 
Anthropic, in Demystifying Evals for AI Agents[6], provides a definition worth adopting directly: an agent harness (or scaffold) is the system that enables a model to act as an agent; it handles input, orchestrates tool invocations,   
and returns results. More crucially, Anthropic further points out: when we evaluate "an agent," we are actually evaluating the model + harness combination, not the model's capability alone. This definition is important because it 
shifts the unit of explanation for agent effectiveness from model parameters to the outer-loop structure in which the model operates. 
 
│ (Image placeholder) 
 
Here we must untangle a frequently conflated concept: an agent harness and an evaluation harness are not the same thing. The former is responsible for making the agent run (handling input, orchestrating tools, managing state); the 
latter is responsible for batch-running tasks, recording traces, executing graders, and aggregating scores. Many discussions lump "harness" into one catch-all bucket, oscillating between runtime orchestration and evaluation pipelines. 
The Harness Engineering discussed in this article refers to the former — the engineering of the runtime outer-loop system. 
 
Based on this, a more precise formulation: 
 
│ 📌 Harness = the outer-loop system that enables a model to act as an Agent. 
│ 
│ It encompasses plan decomposition, persistent state, tool orchestration, verification gating, feedback loops, rollback mechanisms, human-machine handoff points, and audit logs. When evaluating an Agent's effectiveness, you are not   
│ evaluating the model itself, but the model + harness combination. 
 
Several points here are worth expanding: 
 
- Outer loop is the key term. The model's reasoning is the "inner loop" — given context, generate the next step. The harness is the "outer loop" — deciding when to start a new inner loop, what context to give it, how to verify its 
  output, when to roll back, and when to stop. The quality of the inner loop depends on model capability; the quality of the outer loop depends on harness design. 
- Harness is not an upgraded prompt. A single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control. Treating a harness as "just a longer system prompt" is the    
  most common failure mode today. 
- Harness is also not a framework name. LangChain is a framework, CrewAI is a framework, but Harness Engineering is not. It is a practice, just as DevOps is not a tool but an engineering culture. 
 
### Three Layers of Engineering Abstraction 
 
Prompt → Context → Harness 
 
To understand where a harness sits, you must first see its relationship to the two preceding layers. These three layers are not replacements for each other but progressive levels of abstraction: 
 
│ (Image placeholder) 
 
│ 📌 Key Insight 
│ Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline operates." The former is a subset of the latter. On the user side, harness engineering is essentially a specific form of context 
│ engineering; but a harness also includes multi-step structure, tool mediation, verification gates, and durable state — these extend beyond the scope of single-step context. 
 
### Six Core Engineering Components of a Harness 
 
This section is the most technically dense part of the article. Each component explains what problem it solves, Anthropic/OpenAI's specific approaches, and the design principles behind them. 
 
#### 1. Durable State Surfaces: So Agents No Longer "Start Amnesiac" 
 
Problem: The core pain point of long-running agents is analogous to a project team where every engineer who goes on shift has complete amnesia. Context windows are finite, complex projects cannot be completed within a single window,   
and agents need a way to bridge the gap between sessions. 
 
Anthropic's approach: Rather than attempting to build an "infinitely long context," they externalized state into durable artifacts: 
 
- An initializer agent sets up the environment: creates init.sh (startup script), claude-progress.txt (progress log), and an initial git commit (baseline snapshot). 
- It generates a feature list: expanding high-level requirements into 200+ specific features, all initially marked as failing. 
- Each subsequent coding agent performs only incremental progress, leaving structured updates and a "clean state" at the end of each session. 
- Key rule: Agents may only change a feature's pass/fail status; they cannot arbitrarily modify the test definitions themselves. 
 
This feature list design may look "crude," but it is remarkably effective — it transforms the definition of "done" from the agent's subjective sense into an external, persistent, structured, inheritable completion surface. The agent   
does not need to "remember" what it did before; it only needs to read the feature list and git diff to resume within 30 seconds. 
 
Anthropic later discovered an even deeper problem: context anxiety. Even with compaction (summarizing and compressing earlier conversation turns), agents still degrade in behavior because they feel the "context is too full." The 
solution was not better compaction but context reset — giving the next agent a completely fresh context and passing all necessary information through externalized state artifacts (rather than conversation history). This is more 
aggressive than compaction but works better. 
 
│ 📌 Design Principle 
│ State ≠ "saving chat history." True durable state is a structured artifact that an agent can read, understand, and resume from after a cold start with zero conversation history. If your agent cannot know within 30 seconds after a    
│ cold start where it left off and what to do next, your state management has failed. 
 
#### 2. Decomposition & Plans: Cutting Long Tasks into Agent-Size Chunks 
 
Problem: Tell an agent to "build a clone of claude.ai," and it will attempt to do everything in one shot — writing all the code in a single session. The result is either a context window overflow or a premature "done" declaration 
halfway through. 
 
Evolution: 
 
- In November 2025, Anthropic initially addressed this with an initializer + coding two-role structure. The initializer handled decomposition and initialization; the coding agent handled step-by-step implementation. 
- In March 2026, this structure was upgraded to a planner / generator / evaluator three-role system: 
    - Planner: Does not write code directly; instead, expands a one- or two-sentence high-level description into a complete product spec and step-by-step feature list. 
    - Generator: Implements features one by one, committing after each completion. 
    - Evaluator: Independently evaluates the generator's output, marking pass/fail and providing specific improvement suggestions. 
- OpenAI's counterpart is PLANS.md, Implement.md, Documentation.md — complex tasks are planned first, execution proceeds by milestones, each stage undergoes verification, and documentation is continuously updated as shared memory. 
 
│ 📌 Design Principle 
│ Plans must be elevated to first-class artifacts, not ephemeral chat content. They must be written to the filesystem, version-controlled, readable by subsequent agents, and referenced by verification gates. A plan that exists only in 
│ conversation is not a plan at all — it is merely a fleeting thought. 
 
#### 3. Feedback Loops: Guides and Sensors 
 
Problem: An agent writes code — how do you know if it's correct? Rely on the agent's self-evaluation? Anthropic explicitly discovered an embarrassing fact: when asked to evaluate their own work, agents tend to enthusiastically 
congratulate themselves — even when the quality is clearly mediocre by human standards. 
 
This necessitates a feedback system that does not depend on agent self-evaluation. By April 2026, community frameworks had decomposed the harness into a very clear 2×2 matrix: 
 
│ (Image placeholder) 
 
Guides constrain the agent before it acts, increasing the probability of "getting it right the first time." Sensors provide signals after the agent acts, enabling self-correction. 
 
│ (Image placeholder) 
 
Key insights: 
 
- Guides without sensors → the agent encodes rules but never knows whether the rules are actually taking effect. 
- Sensors without guides → the agent repeatedly makes the same error and then gets corrected. 
- Computational control is cheap, fast, and deterministic — it can run on every change. 
- Inferential control is expensive, slow, and non-deterministic, but it handles subjective judgment (e.g., "is this UI design too ugly?"). 
 
Anthropic's evaluator-optimizer pattern is entirely consistent with this. They also acknowledged a subtle fact: the evaluator is not always necessary — once the base model's capability crosses a certain threshold, the evaluator 
degrades from a "necessary component" to "unnecessary overhead." This shows that a good harness is not a fixed template but a trimmable system that co-evolves with the model's capability boundary. 
 
│ (Image placeholder) 
 
#### 4. Legibility: Building a Perception Surface for Agents 
 
Problem: Agents can write code now — but can they "see" what the code looks like when it runs? Can they read error logs? Can they understand performance metrics? 
 
OpenAI, in their harness engineering practice, made an extremely pointed observation: any knowledge not within the agent's runtime visible range might as well not exist. 
 
This is not rhetoric. They did the following concrete work to improve legibility: 
 
- Spawned an independent browser instance for each git worktree, using the Chrome DevTools Protocol (CDP)[7] to let the agent "see" the UI. 
- Exposed logs, metrics, and traces for agent querying. 
- Made the repository the system of record: design principles, product intent, execution plans, known technical debt, and Architecture Decision Records (ADRs) were all placed in the repo and kept consistent via lint/CI. 
- Placed AGENTS.md, structured docs/, execution plans, and knowledge documents into the repo as a versioned system of record; but OpenAI also publicly cautioned: excessively long AGENTS.md files rot quickly, consume context, and cause 
  all constraints to lose focus simultaneously — a better approach is to make it a directory index, with actual knowledge distributed across structured documents. 
 
│ 📌 Design Principle 
│ Legibility is not "making code more elegant"; it is making knowledge, constraints, acceptance criteria, and decision history enter the agent's perception surface. This directly transforms "knowledge management" from a team 
│ collaboration problem into an agent executability problem. For an agent, experience trapped in Slack, architectural boundaries passed down orally, and constraints scattered across external documents — if they do not enter the 
│ runtime-accessible artifact surface, they might as well not exist. 
 
#### 5. Tool Mediation: The More Tools You Have, the More You Need a Harness 
 
Problem: After the MCP ecosystem exploded, a single agent might connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions directly into context creates serious problems — token costs skyrocket,   
latency increases, and the agent gets lost in an ocean of tools. 
 
Anthropic, in their MCP + Code Execution engineering practice, proposed a core idea: don't let the model call tools directly; let the model write code that calls tools. 
 
What's the difference? 
 
- Direct tool-call mode: All tool definitions loaded into context → model selects tool → calls it → result returned to context → model continues. Every step consumes context space, with intermediate results cycling inside the model.   
- Code execution mode: Model writes a snippet of code → code runs in a sandbox, discovering and calling MCP tools on demand → only the final result is returned to the model. Tool discovery, data filtering, and intermediate processing  
  all happen within the execution environment and never enter context. 
 
The essence of this idea is: move tool usage from the model's inner loop into a more efficient external execution loop. This is precisely what harness engineering is — it is not a "tool registry" but the system-level design that 
determines how tools are discovered, when they are exposed, at what granularity, whether results need to enter context, where state is stored, and how failures are rolled back. 
 
#### 6. Entropy Control: Continuous Garbage Collection for Agents 
 
Problem: Fully autonomous agent codebases constantly replicate existing patterns — even when those patterns are inconsistent, suboptimal, or outright poor. Over time, drift and entropy accumulation are inevitable. 
 
OpenAI was the most candid about this: they initially relied on humans spending roughly 20% of their time each week cleaning up "AI slop" (redundant code, stale documentation, inconsistent naming, copy-pasted dead code). They later    
systematized this cleanup logic: 
 
- Documentation consistency agents periodically verify that documentation matches code. 
- Refactor agents clean up technical debt on a planned schedule. 
- Architectural enforcement mechanically maintains module boundaries through CI. 
 
│ 📌 Design Principle 
│ A harness is not only responsible for "making the agent run" but also for continuously suppressing the system noise amplified by the agent. This is the most essential distinction from a simple "agent framework" — a framework cares   
│ about startup and orchestration; a harness cares about long-term governability. 
 
#### 7. Harnessability: Not Every System Is Easy to Harness 
 
If you understand Harness Engineering only as "adding more rules and loops to an agent," you haven't gone deep enough. The more fundamental question is: not every system is equally easy to harness. 
 
OpenAI's practice repeatedly implies the same thing: the reason they could push Codex to high throughput was not just because the model was strong enough, but because they continuously pushed knowledge back into the repo, made plans   
into artifacts, versioned decisions, and made the environment more legible to agents. How naturally a system lends itself to being tamed by an agent is itself an important variable. 
 
Following this logic leads to a highly explanatory judgment: strongly typed, thoroughly tested, clear-boundaried, versioned-documentation, runtime-observable systems have naturally higher harnessability; whereas systems where 
knowledge is scattered across human minds, chat tools, and oral tradition — no matter how strong the model — will first hit the wall of "can't see → can't understand → can't govern." 
 
This means that in the agent era, a team's engineering infrastructure quality (CI maturity, documentation structure, architectural boundary clarity) is no longer just a matter of "engineering hygiene" — it directly determines how far  
an agent can go within your system. Harnessability will become a key dimension for evaluating a system's "agent-readiness." 
 
### The Intent System 
 
A deeper paradigm shift: from instruction-driven to intent-driven. 
 
What has been discussed above are the engineering components of a harness. But if you look only at the components, you'll fall into "assembling technical details." Let's step back and address something more fundamental — why Harness   
Engineering is not merely an engineering practice but the product of a paradigm shift. 
 
### Four Ruptures in Human-Machine Interaction 
 
Reviewing the entire history of computing, human-machine interaction has undergone four fundamental ruptures: 
 
- CLI (Command Line): Humans must precisely master the machine's language. ls -la | grep .py is an instruction — a single wrong character breaks it. The core interaction assumption is "humans adapt to machines." 
- GUI (Graphical User Interface): Machines lower the barrier through visual metaphors. Folders, desktops, drag-and-drop. The core assumption is "machines present themselves using metaphors humans can understand." 
- App (Mobile Application): Logic is frozen into fixed interfaces. One function per button, one screen per button. The core assumption is "humans choose within predefined paths." 
- Agent (Intent-Driven): Humans express only goals; the system autonomously plans execution paths. The core assumption is "the machine understands human intent and decides how to execute autonomously." 
 
Each rupture is not merely a technological upgrade but a redistribution of control. In the CLI era, humans held 100% of control; in the Agent era, humans cede most execution control, retaining only goal-setting and critical decision   
points. 
 
What are the engineering consequences of this cession? 
 
In an instruction-driven world, a bug is "the system did not correctly execute my instruction" — it can be covered by traditional testing. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system    
correctly understood the intent but chose a terrible execution path" — this requires an entirely new set of verification, constraint, and feedback mechanisms, which is precisely what a harness addresses. 
 
### Applications Are Being "CLI-ified" — But Not for Humans 
 
A highly counterintuitive trend: in the Agent era, all applications and websites are being re-"CLI-ified" — not to send users back to the terminal, but to turn everything into programmable interfaces from the Agent's perspective. 
 
MCP is the protocol-layer implementation of this. When an Agent needs to operate Google Drive, it does not need to "open a web page and click buttons" — it needs a set of structured API calls. The MCP server abstracts Google Drive 
into a set of callable functions: gdrive.getDocument, gdrive.createFile, gdrive.search. 
 
This means three things: 
 
First, the object of legibility has changed. Legibility used to be for humans — clear UIs, sensible information architecture. Now it must first be for Agents — structured APIs, machine-parseable documentation, programmable permission  
models. 
 
Second, application boundaries are dissolving. When an Agent calls any tool through MCP and collaborates with other Agents through A2A, the App degrades from "destination" to "infrastructure." Users no longer "open an App to do one    
thing" but "express an intent, and the Agent orchestrates multiple services to accomplish it." 
 
Third, Harness becomes the new "operating system layer." In the GUI era, the operating system managed windows, files, and processes. In the Agent era, what needs to be managed is: Agent lifecycle, tool discovery and authorization, 
context scheduling and reclamation, multi-Agent coordination and isolation, and human approval intervention points. 
 
### From Chatbot to AgentOS 
 
Connecting all the threads above reveals a clear evolutionary path. These three stages are not feature additions but fundamental changes in engineering abstraction layers: 
 
Level 1: Chatbot (2022–2023) 
Single conversation, stateless, human fully in the loop. Core value: information retrieval and content generation. Engineering abstraction layer: Prompt Engineering. Representative products: ChatGPT, Claude (early). 
 
Ceiling: Can speak but cannot act. Every conversation is isolated. 
 
Level 2: AI Browser / Agent IDE (2024–2025) 
Multi-step tasks, tool invocations, limited autonomy. Core value: task execution and workflow automation. Engineering abstraction layer: Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus,   
Codex. 
 
Ceiling: Single-agent capability strong but long-task instability; multi-agent collaboration lacks standards; state management is manual labor. 
 
Level 3: AgentOS (2026 — Incubation, Forward-Looking Direction) 
This must be written with restraint. AgentOS is not yet a converged industry paradigm. But it has genuinely entered the research and systems community agenda. The 2024 AIOS[8] paper proposed extracting scheduling, context management,  
memory management, and access control from the agent application layer into a kernel-like layer; ASPLOS 2026 featured a dedicated AgenticOS Workshop[9] exploring OS primitives for agent workloads. 
 
│ (Image placeholder) 
 
Therefore, the more prudent statement is not "AgentOS has arrived" but: Harness Engineering is pushing problems from the application layer toward the systems layer. When an agent is no longer just a coding assistant but an always-on,  
multi-agent, cross-tool, cross-identity long-running execution body, the user-space harness will inevitably encounter deeper system-level problems: 
 
- Agent lifecycle management: initialization, running, suspension, resumption, termination — these are not stateless function calls; they are full process management. 
- Context scheduling: The context window is a scarce resource; deciding what information to load when, when to compress, and when to discard — this is the agent version of "memory management." 
- Multi-Agent isolation and coordination: One agent's operations should not pollute another's environment, yet they need to share certain state — requiring mechanisms analogous to process isolation + IPC. 
- Governance and audit: Every decision at every step by every agent must be traceable — in finance, healthcare, and similar domains, this is not a nice-to-have but a compliance requirement. 
 
│ (Image placeholder) 
 
│ 📌 Key Positioning 
│ The harness is the user-space layer of AgentOS. AgentOS is the kernel — managing scheduling, isolation, and resources. The harness is the user-space shell and daemon — managing task decomposition, state resumption, verification 
│ feedback, and human-machine handoff. The two are not competitors but naturally layered. 
 
### Five Typical Symptoms 
 
Theory is done; back to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are still in the ad-hoc assembly stage. Here are five typical symptoms: 
 
Symptom 1: The Framework Jungle. LangChain, CrewAI, AutoGen, Agno, n8n... each framework solves a small slice of the problem, but none provides a complete lifecycle from planning to verification to rollback to auditing. Users cobble   
together pieces across different frameworks, producing a fragile pipeline rather than a governable system. 
 
Symptom 2: Chatbot Skin + Agent Core. Many products are essentially a chatbot interface wrapped around an agent loop — but lacking genuine state management, task decomposition, or verification gates. Stunning in demos; crashing 
frequently in production. 
 
Symptom 3: Tool Registration ≠ Tool Governance. MCP makes connection easy, but "can connect" does not mean "knows how to use." Agents面对 50 tools become confused, make redundant calls, and take circuitous paths. Some engineering 
teams discovered that providing all tools to the agent upfront actually performed worse — performance improved only after trimming to the minimal necessary set. 
 
Symptom 4: One-Shot Rules vs. Evolvable Constraints. Most teams' agent configuration is a massive AGENTS.md or system prompt. Practice shows this approach inevitably fails — when everything is important, nothing is. Agents perform 
local pattern matching rather than conscious navigation. Rules rot faster than humans can maintain them. 
 
Symptom 5: Lack of On-the-Loop Thinking. "In the loop" means manually editing artifacts when unsatisfied with agent output; "on the loop" means modifying the harness so the system automatically produces better results next time. Most  
teams are still stuck in the loop — fixing errors one by one rather than systematically improving the control loops that produce them. 
 
### What Harness Is Not 
 
Clarifying boundaries is as important as clarifying definitions. 
 
- It is not "replacing it with a longer system prompt." Because a single prompt cannot solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control. 
- It is not a proprietary term of any single vendor. Both Anthropic and OpenAI use it publicly, and academic preprints are already abstracting it into a cross-product general concept. 
- It is also not "something that won't be needed once models get stronger." Quite the opposite — Anthropic explicitly states that harnesses will reallocate value as model boundaries shift outward: certain checks become redundant, but  
  planning, verification, handoff, and state governance for harder tasks become more important. The stronger the model, the more you need to place longer, costlier, and more dangerous tasks into controlled outer loops. 
 
In practice, the space of interesting harness combinations will not shrink as models grow stronger — it will shift. An evaluator that is effective today may become redundant overhead before the next-generation model, but new 
capability boundaries will give rise to new harness requirements. 
 
### Overlooked Critical Issues 
 
Testability of the Harness Itself 
When we say "a harness makes agents verifiable," a meta-question arises: how do you verify the harness itself? If the evaluator uses another LLM, and that LLM also has hallucination tendencies, we have built a loop of "using an 
unreliable system to verify an unreliable system." 
 
Anthropic's approach is to use computational sensors (test suites, linters, type checks) for baseline verification as much as possible, only activating inferential sensors for subjective judgment (UI aesthetics, code style). This is a 
pragmatic layered strategy, but not a perfect solution. 
 
Emergent Behavior in Multi-Agent Systems 
When 10 agents run in parallel, each making independent decisions, the system behavior exhibits patterns that single-agent analysis cannot predict. This is analogous to concurrency bugs in distributed systems — but worse, because 
every "process" is non-deterministic. Current harness designs primarily target single-agent scenarios; harness principles for multi-agent coordination have not yet crystallized. 
 
Cost and Latency Engineering Trade-offs 
Every layer of the harness — planner, evaluator, sensor, garbage collection — consumes additional tokens and latency. When the overhead of the harness exceeds the quality improvement it delivers, that is over-engineering. How to 
measure a harness's ROI and how to dynamically adjust harness depth based on task complexity remains an unsolved engineering problem. 
 
A New Dimension of Security: Attack Targets Shift from Data to Agency 
 
This is the layer that most articles gloss over most easily but is actually the most dangerous. As agents gain persistent state, external tools, and long-term autonomy, the attack surface is no longer just "what the model gets wrong"  
but "whether the system can be hijacked and manipulated." 
 
Invariant Labs disclosed Tool Poisoning Attacks[10] in April 2025: malicious instructions can be hidden in MCP tool descriptions — invisible to users but visible to the model — inducing the agent to execute unauthorized operations. A  
week later, they demonstrated a data exfiltration scenario where an untrusted MCP server leveraged a trusted WhatsApp MCP. This means Harness Engineering cannot only discuss throughput and stability; it must directly address tool 
trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation. 
 
│ (Image placeholder) 
 
MCP's open standardization is important (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connections become, the more the upper-layer harness must enforce stricter 
governance. The harness's permission model must evolve from static "can/cannot" to dynamic "under what conditions can, up to what threshold can, and only after human confirmation can." In other words, the harness is not merely an 
outer loop that boosts output — it is itself a new security boundary. 
 
### Judgments & Outlook 
 
Judgment 1: Harness Engineering will become one of the foundational disciplines of the AI engineering era. 
Model capability improvements will continue to absorb some micro-level prompt techniques, but they will not absorb harness engineering. Because it addresses higher-level questions: how to embed unstable, expensive, probabilistic 
intelligence into a long-term governable engineering system. As long as agents need to work across time, tools, environments, and human-machine boundaries, harnesses will not disappear — they will increasingly resemble the 
intersection of software architecture, testing engineering, SRE, and security engineering. 
 
Judgment 2: The moat is shifting upward from model quality to Harness and system design. 
When GPT, Claude, and Gemini converge on core capabilities, what determines product success is no longer model differentiation but harness quality. The strongest evidence comes from LangChain: while keeping the underlying model 
unchanged, they improved deepagents-cli on Terminal Bench 2.0 from 52.8% to 66.5% — a 13.7-point increase, moving from the outer edge of Top 30 to Top 5 — simply by modifying the harness. This result cannot be overstated as "models no 
longer matter," but it is sufficient to demonstrate: above the same model, a harness can create enormous system-level differentiation. The moat's center of gravity is shifting upward to harness and system design. 
 
Judgment 3: The migration from Chatbot to AgentOS will not happen in one step. 
There will be a 2–3 year intermediate stage of "AI Browser + Lightweight Harness." Most enterprises will first capture value in this stage, then gradually evolve toward heavier AgentOS architectures. Teams that attempt to jump 
straight to AgentOS will most likely fail because governance complexity exceeds their capacity to absorb it. 
 
Judgment 4: The engineer's role is shifting from "code producer" to "designer of autonomous systems." 
This is not a layoff warning but an upskilling requirement. Defining intent, shaping environments, setting boundaries, designing feedback, absorbing exceptions, consolidating rules — the value of these capabilities will rise sharply.  
When dissatisfied with agent output, the low-level approach is to manually edit artifacts; the high-level approach is to modify the harness so the system automatically produces better results next time. From in the loop to on the loop 
— this is the engineer's core upgrade path in the agent era. 
 
---
 
Appendix 
 
### Three Self-Check Questions for Practitioners 
 
Before you start building your own harness, answer these three questions first: 
 
1. Does your agent have durable state surfaces? After a cold start, can it resume within 30 seconds — or does it start from scratch every time? 
2. Does your system have machine-readable acceptance criteria? Is the definition of "done" the agent's subjective sense, or an external structured verification surface — a feature list, a set of test cases, an inspectable pass/fail    
   state? 
3. Are your repo, tools, logs, metrics, and policies legible and enforceable to the agent? Or are they only readable by humans — with the agent left to guess? 
 
If none of these three things exist, what you've built is most likely just "a chatbot that can run commands"...
