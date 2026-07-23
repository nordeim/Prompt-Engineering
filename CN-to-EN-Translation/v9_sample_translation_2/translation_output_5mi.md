Background 
 
Let us first answer a prerequisite question: how did we get here? 
 
To understand why Harness Engineering suddenly became a serious engineering practice under discussion in 2026, we need to first see the full arc that AI engineering has traveled over the past four years. This arc is not linear; it is  
a recurring cycle of capability leap → old framework collapse → new abstraction emergence. 
 
Recommended reading to supplement some additional background: 
 
- AI Operating System: From Instructions to Intent 
- From Prompt Engineering to Context Engineering 
- The Token Naming Predicament: When Information Theory Invades Linguistics 
- OpenClaw: The Hidden Dangers Behind the Madness 
- In-Depth Analysis: Google Workspace CLI 
- Meta-Skills: Making AI Think Like You 
- Reflections on Agent Trends: Native and CLI Convergence 
- The AI Coding Ecosystem: What Does Anthropic's Acquisition of Bun Mean? 
- Deep Reflection: Discussing AI Development Trends 
- A Brief Take on AI Browsers 
- In-Depth Analysis: The Anthropic MCP Protocol 
 
Act One: Generation (Nov 2022 — 2023) 
 
On November 30, 2022, ChatGPT launched. It reached approximately 100 million monthly active users about two months after launch. But what truly changed wasn't NLP technology — GPT-3 had already existed for two years — it was the 
interaction paradigm. Before this, an LLM was an API that only engineers could use; after this, it became a conversational interface usable by everyone. 
 
The core tension in this act was: models could generate, but they could not act. They could draft an email, but they could not send it; they could write a piece of code, but they could not run it. The relationship between user and 
model was "you ask, I answer" — a stateless, single-turn, passive exchange of information. 
 
The engineering artifact was Prompt Engineering: how to ask so that the model would answer better. Few-shot, chain-of-thought, role-play — all were essentially attempts to maximize information density within the limited space of a 
single API call. 
 
Act Two: Connection (2023 — 2024) 
 
In March 2023, OpenAI released GPT-4, bringing multimodality and a longer context window. The same month, ChatGPT Plugins were introduced, the first time a model "grew hands" — it could call external APIs, access real-time data. In    
June, OpenAI formally released the Function Calling API, standardizing tool invocation as structured JSON in the model's output. 
 
This was a critical turning point: models evolved from "able to speak" to "able to connect." But the Plugins ecosystem quickly revealed its fragility — each plugin required its own OAuth flow, its own schema definition, its own error  
handling. Even linking 10 plugins was painful; 100 was simply impossible. 
 
In the second half of 2023, LangChain rose to prominence, attempting to solve the "connection" problem with a layer of intermediary abstraction. It did lower the barrier to entry, but it also introduced the cost of over-abstraction —  
too many layers of wrapping, hard to debug, unpredictable performance. Around the same time, projects such as AutoGPT and BabyAGI tried to make models autonomously loop through tasks, but they all faded quickly after the demo stage    
due to a lack of reliable stopping conditions and verification mechanisms. 
 
│ 🤯 Lesson One 
│ Letting a model "connect to tools" is necessary, but far from sufficient. Connection is not orchestration, and orchestration is not governance. 
 
Act Three: Reasoning (2024) 
 
2024 was the year "reasoning models" took the stage. OpenAI's o1 series launched in September, defined by the core feature "spending more time thinking before answering," and achieved a qualitative leap on math and programming tasks.  
In December, the ARC Prize announced that OpenAI o3 reached 87.5% on the ARC-AGI-1 Semi-Private Eval at high-compute configuration, stunning the entire community. At the same time, Anthropic's Claude 3.5 Sonnet performed strongly on   
code generation and long-document understanding, and DeepSeek-R1, as an open-weights model, proved that high-performance reasoning was no longer the exclusive patent of closed-source systems. 
 
What mattered more were two events at the end of 2024: 
 
The first: Anthropic released the Model Context Protocol (MCP). This was not yet another plugin system, but an open standard protocol that used JSON-RPC 2.0 to define how AI applications communicate with external tools and data 
sources. Its core insight was: the connection problem is fundamentally an N×M problem — N AI applications × M data sources, each combination requiring a custom connector. MCP simplified it to N+M: each application implements an MCP    
client once, each tool implements an MCP server once. Later, OpenAI and Google DeepMind successively announced support for MCP; in December 2025, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation. 
 
The second: Anthropic published the Building Effective Agents[1] guide (December 2024). This was the first systematic discussion of engineering patterns for agents — from the simplest prompt chaining to the evaluator-optimizer loop —  
and explicitly put forward a principle: start with the simplest pattern, and only introduce more structure when complexity demonstrably yields better results. This principle later became one of the core guiding ideas of harness 
engineering. 
 
By 2025, Anthropic had separately elevated context engineering to an independent engineering practice, Effective context engineering for AI agents[2], emphasizing that the true difficulty is no longer just "how to write a prompt," but 
"at each step, what information, in what form, and at what moment to hand to the model." This is the critical bridging layer between Prompt Engineering and Harness Engineering — the question has shifted from "single call" upward to    
"per-step context," but has not yet shifted to "the entire task's outer loop." 
 
│ 🤯 Lesson Two 
│ A model's reasoning capability solves the "single-step quality" problem, but reliability on long tasks is not automatically obtained just because a single step becomes smarter. A model that can solve an IMO gold-medal problem will   
│ still, halfway through a four-hour full-stack development task, "forget what it was doing." 
 
Act Four: Action (2025) 
 
If 2023 was the year of the chatbot, and 2024 was the year of multimodality, then 2025 was the year of the agent. 
 
Early in the year, DeepSeek-R1's open-source release forced the market to reassess the landscape of model competition. What followed was a string of agent products: Claude Code (a coding agent in the terminal), GitHub Copilot Agent    
Mode, Cursor's autonomous coding loop, Manus (a browser-operation agent), and OpenAI Operator. The MCP ecosystem exploded, with the community building thousands of MCP servers, and SDKs covering all major languages. Google released    
the Agent2Agent (A2A) protocol, addressing cross-vendor communication between agents. 
 
But the most important discovery of 2025 was not what agents could do, but how agents break while doing it: 
 
- Agents attempted to complete an entire task in one go, only to exhaust their context window halfway through. 
- After completing 70%, they announced "all done" and then stopped. 
- When multiple agents ran in parallel, cascading errors emerged, with each small mistake amplified beyond debuggability. 
- After agents worked continuously, codebases suffered severe "AI slop" — redundant code, inconsistent naming, outdated documentation. 
 
These are not problems of model intelligence, but of system structure. 
 
│ 🤯 Lesson Three 
│ Agent capability has reached the level of "working autonomously for hours," but the engineering infrastructure around them still remains stuck in the era of "single conversation." This rupture is the root cause of the birth of 
│ Harness Engineering. 
 
Act Five: Governance (2026 — Present) 
 
At the start of 2026, the industry's attention began to shift from "how to make agents more capable" to "how to keep agents from failing." "Harness Engineering" as a public term was not invented on some particular day, but began to    
crystallize and spread rapidly in February 2026: 
 
- February 5, 2026: Mitchell Hashimoto explicitly wrote "Engineer the Harness" in My AI Adoption Journey[3], which is regarded as one of the starting points of the term entering mainstream discussion. 
- February 11, 2026: OpenAI directly published an engineering article titled Harness Engineering: Leveraging Codex in an Agent-First World[4]. They used a small team to build an internal beta product from an empty repository in five   
  months; the public framing was "zero lines of human-written code," with the repository reaching on the order of a million lines of code and producing about 1,500 PRs. More precisely, the initial scaffold was still generated by Codex 
  under the guidance of a small amount of template work, after which application logic, tests, CI, documentation, observability, and internal tools were produced mostly by agents. The core finding was that engineers' work shifted 
  toward designing environments, specifying intent, and building feedback loops. 
- March 2026: Anthropic published Harness Design for Long-Running Application Development, upgrading the previous initializer/coding two-role architecture to a planner/generator/evaluator three-role system, demonstrating that the 
  evaluator still brings clear gains near the boundary of model capability. 
- April 2026: The Thoughtworks / Fowler system (Harness Engineering - first thoughts[5]) systematized the concept into a more complete methodology framework — a combination of guides (feed-forward control) and sensors (feedback 
  control), each further divided into computational (deterministic) and inferential (inferential) categories, forming a 2×2 control matrix. Therefore, April is better understood as "the methodological abstraction became complete," not 
  "the first naming." 
 
What Exactly Is a Harness? 
 
Let us derive from first principles, rather than starting from a definition. 
 
The Five Fundamental Challenges of an Agent 
 
The essence of an agent is "a system that autonomously advances goals in an open environment." This definition implies five engineering challenges, none of which can be solved by a smarter model alone: 
 
### State Persistence 
 
- Essence: An agent needs to remember what it has done across time and across sessions. 
- Why a model cannot solve it: A model is itself stateless; its context window also has a limit, and cannot naturally bear long-term continuous state. 
 
### Goal Consistency 
 
- Essence: On long tasks, an agent easily drifts, goes off-script, or even prematurely announces completion. 
- Why a model cannot solve it: A model lacks external anchors, and cannot stably calibrate "what counts as truly done." 
 
### Action Verifiability 
 
- Essence: Every step is probabilistic; we need to distinguish between "did it" and "did it right." 
- Why a model cannot solve it: When a model evaluates its own output, it inherently harbors self-praise and misjudgment biases. 
 
### Entropy Suppression 
 
- Essence: Continuous output continually accumulates redundancy, drift, and inconsistency. 
- Why a model cannot solve it: A model will replicate existing patterns, even when those patterns themselves are bad or low-quality. 
 
### Human–Machine Boundary 
 
- Essence: When to act autonomously and when to hand off to a human must be defined clearly and engineered explicitly. 
- Why a model cannot solve it: A model does not possess a reliable "uncertainty self-awareness," and cannot stably judge when it should stop and hand control back to a human. 
 
A harness is the engineering practice that systematically answers these five challenges. 
 
A Precise Definition 
 
Anthropic, in Demystifying evals for AI agents[6], offers a definition worth adopting directly: the agent harness (or scaffold) is the system that enables a model to act as an agent; it handles input, orchestrates tool calls, and 
returns results. More critically, Anthropic goes further to point out: when we evaluate "an agent," what we actually evaluate is the combined model + harness, not the model's standalone capability. This definition is very important,   
because it shifts the explanatory unit of agent efficacy — from model parameters to the outer-loop structure in which the model sits. 
 
Image 
 
Here one frequently confused concept must be separated out: the agent harness and the evaluation harness are not the same thing. The former is responsible for running the agent (handling input, orchestrating tools, managing state);    
the latter is responsible for batch-running tasks, recording trajectories, executing graders, and aggregating scores. Many discussions lump "harness" into one big bucket, and as a result sometimes talk about runtime orchestration and  
sometimes about the evaluation pipeline. The Harness Engineering discussed in this article refers to the former — the engineering of the runtime outer-loop system. 
 
Building on this, a more precise formulation: 
 
│ 📌 
│ Harness = the outer-loop system that enables a model to act as an agent. 
│ 
│ It includes plan decomposition, persistent state, tool orchestration, verification gates, feedback loops, rollback mechanisms, human–machine handoff points, and audit logs. When evaluating an agent's efficacy, we are not evaluating  
│ the model itself, but the combined model + harness. 
 
A few points here are worth expanding on: 
 
- Outer loop is the key phrase. The model's reasoning is the "inner loop" — given a context, generate the next step. The harness is the "outer loop" — it decides when to start a new inner loop, what context to give it, how to verify   
  its output, when to roll back, and when to stop. The quality of the inner loop depends on the model; the quality of the outer loop depends on harness design. 
- A harness is not an upgraded prompt. No single prompt can solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control. Treating a harness as "a longer system prompt" is the most    
  common failure pattern today. 
- A harness is also not a framework name. LangChain is a framework, CrewAI is a framework; Harness Engineering is not. It is a practice, just as DevOps is not a tool but an engineering culture. 
 
The Three-Layer Engineering Abstraction 
 
### Prompt → Context → Harness 
 
To understand where the harness sits, we first need to see clearly its relationship with the preceding two layers. These three layers are not substitutive; they are progressively higher levels of abstraction: 
 
Image 
 
│ 📌 
│ Key insight. Context Engineering is "what to feed at each step"; Harness Engineering is "how the entire pipeline runs." The former is a subset of the latter. On the user-facing side, harness engineering is essentially a specific 
│ form of context engineering; but the harness also encompasses multi-step structure, tool mediation, verification gates, and durable state — these go beyond the scope of single-step context. 
 
The Six Core Engineering Components of the Harness 
 
This section is the hardest-hitting part of the article. Each component will explain clearly what problem it solves, the specific approach taken by Anthropic / OpenAI, and the underlying design rationale. 
 
Durable State Surfaces: Letting an Agent No Longer "Clock In Amnesia" 
 
Problem: The core pain point of a long-running agent is like an engineer on a project team completely losing memory every shift change. The context window is finite, a complex project cannot be completed within a single window, and    
the agent needs a way to bridge the gulf between sessions. 
 
Anthropic's solution: Instead of trying to build "infinitely long context," they externalized state into continuously usable artifacts: 
 
- The first initializer agent sets up the environment: creates init.sh (startup script), claude-progress.txt (progress log), and the initial git commit (baseline snapshot). 
- Generate a feature list: expand the high-level requirements into 200+ specific features, all initially marked as failing. 
- Each subsequent coding agent only advances incrementally, leaving behind structured updates and a "clean state" at the end of the session. 
- Key rule: the agent can only change the passes status of a feature; it cannot freely modify the test definitions themselves. 
 
This feature-list design looks "crude," but is extremely effective — it transforms the definition of "done" from the agent's subjective feeling into an external, persistent, structured, inheritable completion surface. The agent 
doesn't need to "remember" what it did before; it only needs to read the feature list and git diff to resume within 30 seconds. 
 
Anthropic later also discovered a deeper issue: context anxiety. Even with compaction (summarizing and compressing early conversations), the agent still degrades in behavior because it "feels the context is too full." The solution is  
not better compaction, but context reset — give the next agent a brand-new context directly, transmitting all necessary information through external state artifacts (rather than conversation history). This is more radical than 
compaction, but works better. 
 
│ 📌 
│ Design rationale. State ≠ "save the chat record." True durable state is a structured artifact that the agent can read, understand, and resume from after a cold start, with no context history at all. If your agent cannot, within 30   
│ seconds of a cold start, know "where we left off, and what to do next," then your state management has failed. 
 
Decomposition & Plans: Cutting Long Tasks into Pieces an Agent Can Digest 
 
Problem: Tell an agent "build a clone of claude.ai," and it will try to do it all in one go — writing all the code within a single session. The result is either a blown context window, or declaring "done" halfway through. 
 
Evolution of the approach: 
 
- In November 2025, Anthropic initially solved this problem with an initializer + coding two-role structure. The initializer is responsible for decomposition and initialization; coding is responsible for incremental implementation.    
- In March 2026, this structure was upgraded to a planner / generator / evaluator three-role system: 
    - The planner does not write code directly, but expands a one- or two-sentence high-level description into a full product spec and a step-by-step feature list. 
    - The generator is responsible for landing each feature incrementally, committing as each one is completed. 
    - The evaluator is responsible for independently assessing the generator's output, marking pass/fail, and providing concrete improvement suggestions. 
 
The corresponding artifact in OpenAI's ecosystem is PLANS.md, Implement.md, and Documentation.md — complex tasks are planned first, executed milestone-by-milestone, with verification at each phase, while continually updating 
documentation as shared memory. 
 
│ 📌 
│ Design rationale. A plan must be elevated to a first-class artifact, not one-shot chat content. It needs to be written into the file system, version-controlled, readable by subsequent agents, and referenced by verification gates. A  
│ plan that exists only within a conversation is, in essence, not a plan — it is just an idea. 
 
Feedback Loops: Guides and Sensors 
 
Problem: An agent wrote code — how does it know whether what it wrote is correct? Rely on the agent's self-evaluation? Anthropic explicitly surfaced an embarrassing fact: when asked to evaluate its own work, the agent tends to 
enthusiastically self-praise — even when, by human standards, the quality is clearly mediocre. 
 
This calls for a feedback system that does not depend on the agent's self-evaluation. By April 2026, the community had a framework that decomposed the harness into a very clear 2×2 matrix: 
 
Image 
 
Guides constrain the agent before it acts, raising the probability of "getting it right the first time." Sensors give signals after the agent has acted, supporting self-correction. 
 
Image 
 
Key insights: 
 
- Only guides but no sensors → the agent encodes rules but never knows whether the rules are taking effect. 
- Only sensors but no guides → the agent repeats the same mistakes and then gets corrected. 
- Computational control is cheap, fast, deterministic, and can run on every change. 
- Inferential control is expensive, slow, and non-deterministic, but can handle subjective judgments (such as "is this UI design too ugly?"). 
 
Anthropic's evaluator-optimizer pattern is fully consistent with this. They also acknowledge a subtle fact: the evaluator is not always necessary — once the underlying model capability crosses a certain threshold, the evaluator 
degrades from "an essential component" to "an extra overhead." This shows that a good harness is not a fixed template, but a trim-on-demand system that co-evolves with the boundary of model capability. 
 
Image 
 
Legibility: Building a Perception Surface for the Agent 
 
Problem: An agent can write code, but can it "see" what its written code looks like when it runs? Can it read error logs? Can it understand performance metrics? 
 
OpenAI, in its harness-engineering practice, offers an extremely sharp observation: any knowledge that is not within the agent's runtime-visible scope is, for all practical purposes, nonexistent. 
 
This is not a rhetorical flourish. They did the following concrete work to improve legibility: 
 
- Spin up a separate browser instance for each git worktree, exposing the UI to the agent via CDP (Chrome DevTools Protocol[7]), so the agent can "see" it. 
- Expose logs, metrics, and traces to the agent for querying. 
- Repository knowledge as the system of record: design principles, product intent, execution plans, known technical debt, architectural decision records (ADRs) — all are placed in the repo, with lint/CI maintaining consistency. 
- Where possible, put AGENTS.md, structured docs/, execution plans, and knowledge documents in the repo, making them a versioned system of record. But OpenAI also publicly cautions that an overly long AGENTS.md rots quickly, crowds    
  context, and causes all constraints to lose focus simultaneously — a better practice is to turn it into a table-of-contents index, with the actual knowledge scattered into structured documents. 
 
│ 📌 
│ Design rationale. Legibility is not "making the code more elegant," but bringing knowledge, constraints, acceptance criteria, and decision history into the agent's perception surface. This directly converts "knowledge management"    
│ from a team-collaboration problem into an agent-execution problem. For an agent, the experience buried in Slack, the architectural boundaries passed down orally, and the constraints scattered in external documents — if they don't    
│ enter the runtime-accessible artifact surface, they are equivalent to nonexistent. 
 
Tool Mediation: The More Tools, the More You Need a Harness 
 
Problem: With the MCP ecosystem exploding, an agent may connect to dozens of MCP servers and access hundreds of tools. But stuffing all tool definitions directly into context creates serious problems — token cost balloons, latency 
climbs, and the agent loses its way in a sea of tools. 
 
Anthropic, in its MCP + Code Execution engineering practice, puts forward a core idea: don't let the model call tools directly; let the model write code that calls tools. 
 
Where is the difference? 
 
- Direct tool-call mode: All tool definitions are loaded into context → the model selects the tool → makes the call → the result goes back into context → the model continues. Each step consumes context space, and intermediate results  
  live within the model's inner loop. 
- Code-execution mode: The model writes a piece of code → the code runs in a sandbox, discovers and calls MCP tools on demand → only the final result is passed back to the model. Tool discovery, data filtering, and intermediate 
  processing all happen inside the execution environment, and never enter context. 
 
The essence of this idea is: moving tool usage from the model's inner loop to a more efficient external execution loop. This is precisely harness engineering — it is not a "tool registry," but a system-level design that decides how    
tools are discovered, when they are exposed, at what granularity they are exposed, whether results need to enter context, where state is held, and how failures fall back. 
 
Entropy Control: The Agent's Continuous Garbage Collection 
 
Problem: A fully automated agent's codebase will continually replicate existing patterns — even when those patterns are uneven, suboptimal, or simply bad. Over time, drift and entropy increase are inevitable. 
 
OpenAI puts this most bluntly: at first they relied on people spending about 20% of their time each week cleaning up "AI slop" (redundant code, outdated docs, inconsistent naming, copy-pasted dead code). They later systematized this   
cleanup logic: 
 
- Documentation consistency agents periodically verify that docs align with code. 
- Refactor agents clean up technical debt on a planned schedule. 
- Architectural enforcement mechanistically maintains module boundaries through CI. 
 
│ 📌 
│ Design rationale. The harness is not only responsible for "making the agent run," but also for continuously suppressing the system noise that the agent amplifies. This is the most essential difference between it and a simple "agent  
│ framework" — the framework cares about startup and orchestration; the harness cares about long-term governability. 
 
Harnessability: Not Every System Is Equally Easy to Harness 
 
If we only understand Harness Engineering as "adding a few more rules and loops to the agent," that isn't deep enough. The more fundamental question is: not every system is equally easy to harness. 
 
OpenAI's practice keeps hinting at the same thing: the reason they could push Codex to high throughput isn't just that the model is strong enough, but that they continually pressed knowledge back into the repo, made plans into 
artifacts, version-controlled decisions, and made the environment more legible to the agent. How naturally suited a system is to being tamed by an agent is itself an important variable. 
 
Following this logic, one arrives at a powerful explanatory judgment: a strongly typed, well-tested, clearly bounded, version-controlled, runtime-observable system inherently has higher harnessability; whereas a system whose knowledge 
is scattered in people's heads, chat tools, and oral transmission — no matter how strong the model — will crash first into the wall of "invisible → cannot understand → cannot govern." 
 
This means that in the agent era, the quality of a team's engineering infrastructure (CI maturity, degree of doc structure, clarity of architectural boundaries) is no longer just an "engineering hygiene" issue — it directly determines 
how far an agent can go on your system. Harnessability will become a key dimension for evaluating a system's agent-readiness. 
 
The Intent System 
 
A Deeper Paradigm Shift: From Instruction-Driven to Intent-Driven 
 
The above discusses the engineering components of the harness. But if we only look at components, we'll fall into "a stitching together of technical details." Let's step back and talk about something more fundamental — why Harness 
Engineering is not just an engineering practice, but the product of a paradigm shift. 
 
The Four Ruptures in Human–Computer Interaction 
 
Reviewing the entire history of computing, the interaction between humans and machines has gone through four fundamental ruptures: 
 
- CLI (command line): Humans must precisely master the language of machines. ls -la | grep .py is one instruction; a single character wrong and it fails. The core assumption of interaction is "the human adapts to the machine." 
- GUI (graphical interface): Machines use visual metaphors to lower the barrier. Folders, desktops, drag-and-drop. The core assumption is "the machine presents itself using metaphors humans can understand." 
- App (mobile application): Logic is frozen into fixed interfaces. One button per feature, one screen per button. The core assumption is "the human chooses among preset paths." 
- Agent (intent-driven): Humans only express goals; the system autonomously plans the execution path. The core assumption is "the machine understands the human's intent and decides how to do it on its own." 
 
Each rupture is not just a technological upgrade, but a redistribution of control. In the CLI era, humans held 100% of control; in the agent era, humans yield most execution control, retaining only goal-setting and key decision 
points. 
 
What are the engineering consequences of this yielding? 
 
In an instruction-driven world, a bug is "the system did not correctly execute my instruction" — coverable by traditional tests. In an intent-driven world, a bug becomes "the system misunderstood my intent" or "the system correctly    
understood the intent, but chose a poor execution path" — this calls for an entirely new set of verification, constraint, and feedback mechanisms, which is precisely what the harness exists to solve. 
 
Applications Are Being "CLI-ified" — but Not for Humans 
 
A highly counter-intuitive trend: in the agent era, all applications and websites are being re-"CLI-ified" — not by pushing users back to the terminal, but by turning everything into programmable interfaces from the agent's 
perspective. 
 
The essence of MCP is the protocol-layer realization of this. When an agent needs to operate Google Drive, it doesn't need to "open a web page and click buttons" — it needs a set of structured API calls. The MCP server abstracts 
Google Drive into a set of callable functions: gdrive.getDocument, gdrive.createFile, gdrive.search. 
 
This means three things: 
 
First, the object of legibility has changed. In the past, legibility was for humans to read — clean UI, reasonable information architecture. Now the priority is for the agent to read — structured APIs, machine-parseable documentation, 
programmable permission models. 
 
Second, the boundaries of the application are dissolving. When an agent calls any tool via MCP, or collaborates with other agents via A2A, the App degrades from "destination" to "infrastructure." Users no longer "open one app to do    
one thing," but rather "express an intent, and the agent orchestrates multiple services to complete it." 
 
Third, the harness becomes the new "operating-system layer." The GUI-era operating system managed windows, files, and processes. The agent era needs to manage: the lifecycle of agents, the discovery and authorization of tools, the 
scheduling and reclamation of context, the collaboration and isolation of multi-agent systems, and the human-approval intervention points. 
 
From Chatbot to AgentOS 
 
Stringing all of the above threads together, a clear evolutionary path emerges. These three stages are not feature-stacking, but fundamental changes in the layer of engineering abstraction: 
 
### Level 1: Chatbot (2022–2023) 
 
Single conversation, stateless, fully human-in-the-loop. Core value is information retrieval and content generation. The engineering abstraction layer is Prompt Engineering. Representative products: ChatGPT, Claude (early). 
 
Ceiling: Can speak, cannot act. Each conversation is isolated. 
 
### Level 2: AI Browser / Agent IDE (2024–2025) 
 
Multi-step tasks, tool calls, limited autonomy. Core value is task execution and workflow automation. The engineering abstraction layer is Context Engineering + lightweight Harness. Representative products: Claude Code, Cursor, Manus, 
Codex. 
 
Ceiling: A single agent is highly capable, but unstable on long tasks; multi-agent collaboration lacks standards; state management is manual labor. 
 
### Level 3: AgentOS (2026 — budding stage, forward-looking direction) 
 
Here we must write with restraint. AgentOS is not yet a converged industry paradigm. But it has indeed entered the research and systems-community agenda. The 2024 AIOS[8] paper proposed lifting problems of scheduling, context 
management, memory management, access control, and the like from the agent application layer to a kernel-like layer; ASPLOS 2026 has a dedicated AgenticOS Workshop[9] exploring OS primitives for agent workloads. 
 
Image 
 
Therefore a more cautious statement is not "AgentOS has arrived," but: Harness Engineering is pushing the problem from the application layer to the system layer. When an agent is no longer just a coding assistant, but an always-on,    
multi-agent, cross-tool, cross-identity long-term executor, the userland harness will inevitably, in the end, bump against more fundamental system problems: 
 
- Agent lifecycle management: initialization, running, suspension, resumption, termination — not stateless function calls, but full process management. 
- Context scheduling: The context window is a scarce resource; we need to decide what information is loaded when, when to compress, when to discard — this is the agent version of "memory management." 
- Multi-agent isolation and collaboration: One agent's operations should not pollute another's environment, but they need to share certain state — a mechanism like process isolation + IPC is needed. 
- Governance and audit: Each step of each agent's decisions must be traceable — in finance, healthcare, and other fields, this is not a nice-to-have but a regulatory requirement. 
 
Image 
 
│ 📌 
│ Key positioning. The harness is the userland layer of AgentOS. AgentOS is the kernel — managing scheduling, isolation, resources. The harness is the userland shell and daemon — managing task decomposition, state continuity, 
│ verification feedback, human–machine handoff. The two are not competitive, but are a natural upper-and-lower-layer pair. 
 
Five Typical Symptoms 
 
Theory is done; back to reality. If you observe the current ecosystem, you'll find that most so-called "agent systems" are still in the ad-hoc-alliance phase. Here are five typical symptoms: 
 
Symptom One: The framework jungle. LangChain, CrewAI, AutoGen, Agno, n8n… each solves a small slice of the problem, but none offers a complete lifecycle from planning to verification to rollback to audit. Users piece frameworks 
together, ending up with a fragile pipeline rather than a governable system. 
 
Symptom Two: Chatbot skin + agent core. A great many products are essentially a chatbot interface wrapped around an agent loop — but they lack real state management, task decomposition, and verification gates. They dazzle in demos;    
they fail repeatedly in production. 
 
Symptom Three: Tool registration ≠ tool governance. MCP makes connection easy, but "able to connect" does not equal "able to use." Faced with 50 tools, the agent becomes confused, makes redundant calls, goes down blind alleys. 
Engineering teams have found that initially giving the agent the full toolset actually performs worse — trimming down to the minimum necessary set is what improves things. 
 
Symptom Four: One-shot rules vs. evolvable constraints. Most teams' agent configuration is a giant AGENTS.md or system prompt. But practice shows this approach is bound to fail — when everything is important, nothing is important. The 
agent pattern-matches locally, instead of navigating deliberately. Rules rot faster than people can maintain them. 
 
Symptom Five: Lack of on-the-loop thinking. "In the loop" means manually modifying the output when you're dissatisfied with the agent's output; "on the loop" means modifying the harness, so that the system automatically produces a 
better result next time. Most teams are still in the loop — fixing errors one by one, rather than systematically improving the control loop that generates the errors. 
 
What the Harness Is Not 
 
Clarifying the boundary is just as important as clarifying the definition. 
 
- It is not "swap in a longer system prompt." No single prompt can solve cross-session state, verification gates, tool discovery, failure recovery, and continuous entropy control. 
- It is not a vendor-proprietary term. Both Anthropic and OpenAI use it publicly; academic preprints are already abstracting it as a cross-product general concept. 
- It is also not "no longer needed as models get stronger." Quite the contrary — Anthropic explicitly points out that the harness redistributes value as the model frontier moves outward: some checks become redundant, but planning, 
  verification, handoff, and state governance for harder tasks become more important. The stronger the model, the more we need to put longer, more expensive, and more dangerous tasks into a controlled outer loop. 
 
In fact, the space of "interesting harness combinations" will not shrink as models get stronger — it will shift. Today's effective evaluator may degrade to redundant overhead against the next-generation model, but new capability 
frontiers will spawn new harness needs. 
 
Overlooked Critical Issues 
 
The Testability of the Harness 
 
When we say "the harness makes the agent verifiable," a meta-question arises: how do we verify the harness itself? If the evaluator is another LLM, and that LLM also has hallucination tendencies, we've built a loop of "using an 
unreliable system to verify an unreliable system." 
 
Anthropic's approach is to use computational sensors (test suites, linters, type checks) as much as possible for baseline verification, and only enable inferential sensors at the layer of subjective judgment (UI aesthetics, code 
style). This is a pragmatic stratified strategy, but it is not a perfect solution. 
 
Emergent Behavior in Multi-Agent Systems 
 
When 10 agents run in parallel and make decisions independently, the system's behavior can exhibit emergent patterns that single-agent analysis cannot predict. This resembles concurrency bugs in distributed systems — but it's worse,   
because every "process" is non-deterministic. Current harness design is mainly aimed at single-agent scenarios; the harness principles for multi-agent collaboration have not yet solidified. 
 
Engineering Trade-offs of Cost and Latency 
 
Every layer of the harness — planner, evaluator, sensor, garbage collection — consumes additional tokens and latency. When the harness's own overhead exceeds the quality improvement it brings, that's over-engineering. How to measure   
the harness's ROI and how to dynamically adjust the harness's depth according to task complexity is an unresolved engineering problem. 
 
A New Dimension of Security: Attack Targets Have Shifted From Data to Agency 
 
This is the layer that many articles gloss over most casually — but in fact it's the most dangerous. As agents gain persistent state, external tools, and long-duration autonomy, the attack surface is no longer just "what did the model 
answer incorrectly," but "can the system be leveraged and manipulated." 
 
Invariant Labs disclosed Tool Poisoning Attacks[10] in April 2025: malicious instructions can be hidden inside MCP tool descriptions, invisible to the user but visible to the model, thereby inducing the agent to perform unauthorized   
operations; a week later, they demonstrated a data-exfiltration scenario that chains an untrusted MCP server with a trusted WhatsApp MCP. This means that Harness Engineering cannot only talk about throughput and stability — it must    
squarely address tool trust, cross-tool data flow, least privilege, approval boundaries, and execution isolation. 
 
Image 
 
MCP's open standardization matters (Anthropic donated MCP to the AAIF under the Linux Foundation in December 2025), but the more successful open connection is, the more the upper-layer harness must do strict governance. The harness's  
permission model must be upgraded from a static "may / may not" to a dynamic "under what conditions may, up to what ceiling, only after human confirmation." In other words, the harness is not only the outer loop that improves output — 
it is itself a new security boundary. 
 
Judgments & Outlook 
 
Judgment One: Harness Engineering Will Become One of the Foundational Disciplines of the AI Engineering Era 
 
Model capability improvements will continue to swallow up some micro-level prompt tricks, but they will not swallow harness engineering. Because it deals with a higher-level problem: how to embed unstable, expensive, probabilistic 
intelligence into a long-term governable engineering system. As long as agents have to work across time, across tools, across environments, and across the human–machine boundary, the harness will not disappear — it will increasingly   
resemble the intersection of software architecture, test engineering, SRE, and security engineering. 
 
Judgment Two: The Center of Gravity of the Moat Is Shifting From Model Quality Upward to Harness and System Design 
 
When GPT, Claude, and Gemini converge on core capabilities, what determines product success is no longer model differences, but harness quality. The hardest evidence comes from LangChain: holding the underlying model constant, by 
modifying only the harness, they lifted deepagents-cli on Terminal Bench 2.0 from 52.8% to 66.5%, an increase of 13.7 points, pulling the ranking from outside the top 30 up to the top 5. This result cannot be exaggerated into "models  
don't matter anymore," but it is sufficient to show that: on top of the same model, the harness alone can open up an enormous systemic gap. The center of gravity of the moat is shifting upward to the harness and system design. 
 
Judgment Three: The Migration From Chatbot to AgentOS Will Not Happen Overnight 
 
In between, there will be a 2–3 year "AI Browser + lightweight Harness" phase. Most enterprises will first capture value at this stage, and then gradually evolve toward heavier AgentOS architectures. Teams that try to jump straight to 
AgentOS will most likely fail because the governance complexity exceeds their capacity to bear it. 
 
Judgment Four: The Engineer's Role Is Shifting From "Code Producer" to "Designer of Autonomous Systems" 
 
This is not a redundancy warning, but an ability-upgrade requirement. Defining intent, shaping the environment, setting boundaries, designing feedback, absorbing anomalies, codifying rules — the value of these capabilities will rise   
sharply. When dissatisfied with the agent's output, the low-level approach is to manually modify the product; the high-level approach is to modify the harness, so that the system automatically does better next time. From in the loop   
to on the loop — this is the core upgrade path for engineers in the agent era. 
 
Appendix 
 
Three self-check questions for practitioners. Before you begin building your own harness, first answer these three: 
 
1. Does your agent have durable state surfaces? Can it resume within 30 seconds after a cold start — or does it start from scratch every time? 
2. Does your system have machine-readable acceptance criteria? Is the definition of "done" the agent's subjective feeling, or an external, structured verification surface — a feature list, a set of test cases, a checkable pass/fail    
   state? 
3. Are your repo, tools, logs, metrics, and policies legible and enforceable to the agent? Or can only humans read them — and the agent can only guess? 
 
If none of these three things is in place, what you're building is most likely still just "a chatbot that knows how to run commands..."
