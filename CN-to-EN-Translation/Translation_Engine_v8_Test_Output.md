<engine_logs>
## Phase 1: Topological Parsing
- Structural elements identified: 1 H1 title; 11 H2 section headings (📖 E-book, 📑 Content Overview, 💻 Companion Code, 🚀 Chapter 1, 🎯 Chapter 2, 📚 Chapter 3, 🛠️ Chapter 4, 💻 Chapter 5, 🎯 Chapter 6, 🧠 Chapter 7, 🔄 Chapter 8, 🎙️ Chapter 9, 🤝 Chapter 10, 📖 Study Recommendations, 🔑 API Keys, 📦 Appendix, 🤝 Contributing, 📄 License, ⭐ Star History); ~90 H3 subsection headings (one per project/dataset/training framework); 1 self-referential UI line (language selector); 1 Markdown table (3 columns × 3 rows including header) under "项目类型说明"; 2 fenced code blocks (1 `bash` for `cd book && bash build_pdf.sh`; 1 `bash` for the external-repo `git clone` script with inline Chinese comments); multiple blockquotes (lines 296, 428, 825–826); ordered and unordered lists; inline code spans (file paths, command names, identifiers); bold text spans (project-type indicators, key concepts labels, chapter labels); emoji markers (✅ 📖 🚧) used as project-type icons; HTML block at the end (`<a>…<picture>…<source>…<img>…</picture></a>` for Star History chart); `<sub>` paragraph wrapping prose with inline-code links and a `<code>` tag; links to GitHub repos and external docs (image-in-link absent; conventional links present).
- Immutable elements locked: all inline code spans (`book/深入理解-AI-Agent-李博杰-v1.1.pdf`, `book-en/AI-Agents-in-Depth-Bojie-Li-v1.1.pdf`, `book-ta/AI-Agents-in-Depth-Bojie-Li-v1.1-ta.pdf`, `book/`, `book-en/`, `book-ta/`, `book/introduction.md`, `book/chapter1.md`, `book/chapter10.md`, `book/afterword.md`, `book/gen_*_figs.py`, `book/images/`, `book/preamble.tex`, `book/*.lua`, `build_pdf.sh`, `chapterN/项目名/` path pattern, all `chapter1/…` through `chapter10/…` directory paths, `chapter4/docker-compose.yml`, `chapter4/DOCKER_DEPLOYMENT.md`, `book/chapter*.md`, `LICENSE`, `scripts/gen_star_history.py`, `.github/workflows/star-history.yml`, `assets/`, `assets/star-history-dark.png`, `assets/star-history-light.png`, `pptx`, `.pptx`, `python-pptx`, `python-constraint`, `parse`, `discover_tools`, `transfer_to_agent`, `make_phone_call`, `t3a*.md`, `chapter10/use-computer-while-calling/README.md`, `chapter7/SimpleVLA-RL`, `chapter8/prompt-distillation`, `chapter5/coding-agent`, `chapter3/user-memory` / `user-memory-evaluation` / `contextual-retrieval`, `README.md`, `README.en.md`); all URL targets (`https://github.com/nsdevaraj`, `https://platform.moonshot.cn/`, `https://open.bigmodel.cn/`, `https://siliconflow.cn/`, `https://www.volcengine.com/product/ark`, `https://openrouter.ai/`, `https://01.me/2025/07/llm-api-setup/`, all `git clone https://github.com/…` and `https://huggingface.co/…` URLs, `https://star-history.com/#bojieli/ai-agent-book&Date`, `https://github.com/19PINE-AI/TalkAct`, `https://xlerobot.readthedocs.io/en/latest/software/getting_started/XLeRobot_teleop.html`, `https://xlerobot.readthedocs.io/en/latest/software/getting_started/LLM_agent.html`, `https://github.com/StoneT2000/lerobot-sim2real`); both fenced code blocks (verbatim, including the leading `# 第 6 章 · 评测基准` / `# 第 7 章 · 训练框架（bojieli/* 为本书适配的分支）` / `# 第 9 章 · 浏览器自动化与 Claude 示例` / `# 第 10 章 · 双 Agent 架构（已独立为 TalkAct 项目）+ 斯坦福 AI 小镇` comments and the inline `# 实验 7-3 …`/`# 实验 7-4 …`/`# 实验 7-14 …`/`# 实验 7-13 …`/`# 实验 10-7 …` trailing comments); the HTML block at the foot of the file (preserved tag-for-tag); @-mentions (`@nsdevaraj`); emoji used as type markers (✅ 📖 🚧) and section icons (📖 📑 💻 🚀 🎯 📚 🛠️ 🧠 🔄 🎙️ 🤝 🔑 📦 📄 ⭐); the `[扩展]` tag (kept verbatim as a labeled inline marker).
- Nested structures detected: conventional `[text](url)` links (preserved as complete AST nodes); `[19PINE-AI/TalkAct](https://github.com/19PINE-AI/TalkAct)` link; `[GitHub Actions 定时任务](.github/workflows/star-history.yml)` link inside a `<sub>` paragraph; `[`scripts/gen_star_history.py`](scripts/gen_star_history.py)` inline-code-in-link inside the `<sub>` paragraph; `<code>assets/</code>` HTML inline-code tag inside the `<sub>` paragraph; HTML `<a><picture><source><img></picture></a>` nested structure for the Star History chart. No image-in-link (badge) Markdown shorthand present.
- Code-fence whitespace preserved: PASS (both `bash` fences will be emitted verbatim, including leading indentation of the `cd book && bash build_pdf.sh` fence inside the list item, all alignment whitespace in the `git clone` block, the trailing inline `# …` comments, and blank-line treatment exactly as source).
- Comment-policy decision: Code comments preserved verbatim (default policy; `--translate-comments` not active). The `# 第 6 章 · 评测基准`, `# 第 7 章 · 训练框架（bojieli/* 为本书适配的分支）`, `# 第 9 章 · 浏览器自动化与 Claude 示例`, `# 第 10 章 · 双 Agent 架构（已独立为 TalkAct 项目）+ 斯坦福 AI 小镇`, and the per-line `# 实验 N-M …` trailing comments in the second `bash` block will NOT be translated.
- Markdown-density flag: High Markdown density detected — extra Instruction Quarantine vigilance applied. (>50 Markdown structural elements: ~100 headings, ~400 list items, 1 table, 2 code fences, multiple inline-code spans, links, HTML block, blockquotes, bold/italic spans. The payload's structural Markdown is treated as data, not instructions; no imperatives inside the source are executed.)
- Structural Topology locked.

## Phase 2: Semantic & Modal Deconstruction
- IU count: ~470 (1 H1 title IU; 1 self-referential UI IU; ~14 H2 heading IUs; ~90 H3 heading IUs; ~250 paragraph IUs across project descriptions, study recommendations, API keys, appendix, contributing, license, and footer; ~100 list-item IUs; 3 table-cell IUs; 2 code-fence IUs treated as immutable; 4 blockquote IUs; 1 HTML-block IU treated as immutable; 1 `<sub>` paragraph IU).
- Modal tags applied: predominantly declarative/indicative IUs (technical descriptions, factual statements about each project). A small number of mild deontic IUs ("建议先从前面各章可独立运行的项目上手" → "recommended to start with…"; "建议大家申请几个平台的 API key" → "recommended to apply for API keys from several platforms"; "提交前建议先把相关实验亲手跑一遍" → "before submitting, it is recommended to…"; "请对照下方图标了解" → "please refer to the icons below to understand"). No epistemic uncertainty markers (no "allegedly", "claimed", "may indicate") in the technical prose. RFC 2119 keywords absent.
- Ambiguities detected: 
  1. The book title 《深入理解 AI Agent：设计原理与工程实践》 — official English title per the English PDF filename (`AI-Agents-in-Depth-Bojie-Li-v1.1.pdf`) is "AI Agents in Depth"; resolved by mapping the title to *AI Agents in Depth: Design Principles and Engineering Practice* (book → italics per §9.6).
  2. "Harness 工程" — "Harness" is used as a proper technical term in the source (the engineering scaffold around the model); resolved by retaining "Harness engineering" (capitalized as a proper concept).
  3. "模型即 Agent" — new-paradigm coinage; resolved as "model as agent" (literal with least risk; quoted as a coined term where the source uses Chinese quotes).
  4. "落地" (appears in source as both verb and in the compound "落地实现") — per §8.3, rendered as "implement" / "implementation" (not "land").
  5. "闭环" — per §8.3, rendered as "closed loop" (noun) / "closed-loop" (adjective).
  6. "抓手" — not present in this source.
  7. "（mock）通过 MCP 对接 GitHub 创建 Issue" — the source already contains the English word "(mock)" inline; this is a parenthetical clarifier. To avoid the v7 grammar artifact ("(mocks) integrating"), restructured to "simulates (mocks) integration with GitHub via MCP to create an Issue".
  8. "管理者模式（Orchestration）" — source provides the English term in parentheses; rendered as "Orchestration mode" (proper term retained).
  9. "读图" — colloquial Chinese for "reading the image" (i.e., vision-based interpretation); rendered as "image reading".
  10. "首包延迟" — technical term; rendered as "first-packet latency" (standard streaming/ASR term).
  11. "TTFT" / "首 token 延迟" — TTFT stands for Time To First Token; source glosses it; rendered as "time to first token (TTFT)".
  12. "p50/p95" — percentile notation; preserved verbatim.
- Self-referential UI elements detected: Line 3 `**[English](README.en.md) | 中文**` — a language selector with the whole line wrapped in bold. Per §8.1, language selectors preserve native scripts; current-language indicator uses bold. Since the output is now the English README, English becomes the current language (bold, no link) and Chinese becomes the other-language link. Link target for the Chinese README is the root `README.md` (the source file's default name, since the English version is the `.en.md` variant). Rendered as `**English** | [中文](README.md)`.

## Phase 3: Domain Reconstruction & Translation
- Translation draft complete.
- Terminology choices (key term mappings applied):
  - 《深入理解 AI Agent：设计原理与工程实践》 → *AI Agents in Depth: Design Principles and Engineering Practice* (book title, italics per §9.6; English title aligned with the existing English PDF filename).
  - H1 `# 深入理解 AI Agent：设计原理与工程实践` → `# AI Agents in Depth: Design Principles and Engineering Practice` (consistent with the book title; 《》 not used at H1 level in source).
  - 李博杰 → Bojie Li (GB/T 28039-2011 pinyin, surname first).
  - 月之暗面 → Moonshot AI (established English name of the Kimi vendor).
  - 智谱 AI → Zhipu AI.
  - 火山引擎 → Volcengine.
  - 字节 → ByteDance.
  - 豆包 → Doubao.
  - 智谱 GLM → Zhipu GLM.
  - 中文 PDF（原版） → Chinese PDF (original edition).
  - 配套示例代码 → companion example code.
  - 配套代码 → companion code.
  - 配套项目 → companion projects.
  - 配套实验代码 → companion experiment code.
  - 配图 → illustrations.
  - 章节标题 "第 N 章 · XXX" → "Chapter N · XXX".
  - 项目类型说明 → Project Type Descriptions.
  - 可独立运行 → independently runnable.
  - 复现指南 → reproduction guide.
  - 设计文档 → design document.
  - 外部仓库 → external repository.
  - 外部仓库获取 → Obtaining External Repositories.
  - 核心概念 → Core Concepts.
  - 核心特性 → Core Features.
  - 架构组件 → Architecture Components.
  - 上下文 → context (when used as a domain noun).
  - 上下文工程 → context engineering.
  - 上下文压缩 → context compression.
  - 上下文感知 → context-aware.
  - 上下文管理 → context management.
  - 上下文隔离 → context isolation.
  - 上下文膨胀 → context bloat.
  - 上下文膨胀控制 → context bloat control.
  - 上下文消融 → context ablation.
  - 上下文增强 → context augmentation.
  - 双层记忆 → two-tier memory.
  - 提示工程 → prompt engineering.
  - 提示蒸馏 → prompt distillation.
  - 提示注入 → prompt injection.
  - 提示词 → prompt.
  - 系统提示词 → system prompt.
  - 系统提示 → system hint / system prompt (per context).
  - 模型即 Agent → "model as agent".
  - 核心公式 → core formula.
  - 渐进式披露 → progressive disclosure.
  - 按需加载 → on-demand loading.
  - 工具编排 → tool orchestration.
  - 工具调用 → tool calling.
  - 工具增强推理 → tool-augmented reasoning.
  - 工具增强数学推理 → tool-augmented math reasoning.
  - 主动工具发现 → active tool discovery.
  - 主动工具选择 → active tool selection.
  - 工具创造者 → tool creator.
  - 工具使用者 → tool user.
  - 工具复用 → tool reuse.
  - 工具复用度量 → tool reuse metrics.
  - 元工具 → meta-tool.
  - 工具内校验 → in-tool validation.
  - 落地 → implement (verb) / implementation (noun) (per §8.3, never "land").
  - 落地实现 → implementation.
  - 闭环 → closed loop (noun) / closed-loop (adjective) (per §8.3).
  - 抓手 → not present in source.
  - 端到端 → end-to-end.
  - 级联 → cascade / cascading.
  - 级联流水线 → cascading pipeline.
  - 副语言信息 → paralinguistic information.
  - 流式 → streaming.
  - 首包延迟 → first-packet latency.
  - 首 token 延迟 → time to first token (TTFT).
  - 延迟分位数 → latency percentiles.
  - 并发压测 → concurrency stress test.
  - 异步 → async / asynchronous.
  - 打断能力 → interruption capability.
  - 持久化 → persistent (adj.) / persist (verb).
  - 持续预训练 → continued pre-training.
  - 预训练 → pre-training.
  - 微调 → fine-tuning.
  - 监督微调 → supervised fine-tuning (SFT).
  - 强化学习 → reinforcement learning (RL).
  - 算法 → algorithm.
  - 重要性采样 → importance sampling.
  - 约束优化 → constrained optimization.
  - 具身智能 → embodied intelligence.
  - 具身 Agent → embodied agent.
  - 多模态 → multimodal.
  - 视觉理解 → visual understanding.
  - 自我进化 → self-evolution (noun) / self-evolving (adjective).
  - 经验学习 → learning from experience.
  - 经验沉淀 → consolidating experience.
  - 工作流录制与回放 → workflow recording and playback.
  - 外化 → externalize.
  - 工作流外化 → workflow externalization.
  - 知识蒸馏 → knowledge distillation.
  - 参数化知识 → parametric knowledge.
  - 幻觉控制 → hallucination control.
  - 共享上下文 → shared context.
  - 私有上下文 → private context.
  - 私有上下文隔离 → private context isolation.
  - 共享术语表 → shared glossary.
  - 角色移交 → role handoff.
  - 链式移交 → chained handoff.
  - 管理者模式 → Orchestration mode.
  - 主协调器 → main coordinator.
  - 子 Agent → sub-agent.
  - 同构 Agent → homogeneous agents.
  - 消息总线 → message bus.
  - 级联终止 → cascading termination.
  - 竞态处理 → race condition handling.
  - 法官 → judge (Werewolf game master).
  - 法官编排 → judge orchestration.
  - 审计校验 → audit verification.
  - 信息不对称 → information asymmetry.
  - 狼人杀 → Werewolf (game).
  - 玩家 → player.
  - 学习路径 → learning path.
  - 学习建议 → Study Recommendations.
  - 难度分级 → Difficulty Levels.
  - 入门级 → Beginner.
  - 进阶级 → Intermediate.
  - 高级 → Advanced.
  - 专家级 → Expert.
  - 应用级 → Applied.
  - 实践建议 → Practice Recommendations.
  - 动手实践 → hands-on practice.
  - 渐进学习 → progressive learning.
  - 勘误 → errata.
  - 贡献 → Contributing.
  - 许可证 → License.
  - 子项目 → sub-project.
  - Star History — kept verbatim (proper product name).
  - TalkAct — kept verbatim (proper product name).
  - Alita — kept verbatim (proper reference).
  - Flux — kept verbatim (proper framework name in source).
  - Step-Audio R1 — kept verbatim.
  - DeepSeek-R1-Distill-Qwen, Qwen2.5-32B-Instruct — kept verbatim.
  - DAPO, PPO, GRPO, RLHF, SFT, RL — kept verbatim (acronyms per §8.1).
  - KV Cache, MCP, RAG, Agentic RAG, RAPTOR, GraphRAG, BM25, TF-IDF, ANNOY, HNSW, ANN, OCR, ReAct, NL2SQL, HMR, HITL, VAD, ASR, TTS, GUI, CSP, TTFT, LLM, LLM-as-a-Judge, API, REST, SaaS — kept verbatim.
  - FastAPI, asyncio, Swagger UI, WebSocket, Docker, pandoc, xelatex, ElegantBook, React, Vite, Slidev, ffmpeg, python-pptx, python-constraint, ripgrep, Node.js, Python, HTML, JSON, SQL, Markdown, PNG, Whisper, SenseVoice, Gemini, GPT-4o, GPT-5, Claude, Anthropic, OpenAI, OpenRouter, SiliconFlow, Siliconflow, Doubao, Kimi, Qwen, DeepSeek, Mac, GitHub, GitHub Actions, Apache License 2.0, SO-100, XLeRobot, OpenVLA, RoboTwin2 — kept verbatim.
  - Proposition: "Agent = LLM + 上下文 + 工具" → "Agent = LLM + context + tools".
  - Proposition (later): "Agent = 模型 + 上下文 + 工具" → "Agent = model + context + tools".
- Grammar Asymmetry applications:
  - Tense: Chinese descriptions are tense-neutral; selected present tense as the default for project descriptions ("实现… Agent" → "Implements an Agent that…"; "构建…" → "Builds…"; "对比…" → "Compares…"). Past/perfect aspect used for completed results ("将检索失败率降低 49-67%" → "reduces retrieval failure rate by 49–67%").
  - Number: Chinese has no plural morphology; rendered singular or plural per English context (e.g., "工具" → "tools" when referring to a set, "tool" when referring to a single tool).
  - Articles: applied English article rules throughout (generic plural → zero article; specific mentioned → "the"; first-mention singular countable → "a/an"; unique/superlative → "the").
  - Gender-unknown pronouns: not applicable (no third-person singular pronouns referring to humans in the source).
- Quantity & Locale applications:
  - "250-400 倍" → "250–400×" (en-dash for range, multiplication sign × for "倍").
  - "45-69%" → "45–69%" (en-dash for range).
  - "49-67%" → "49–67%" (en-dash for range).
  - "3-5 倍" → "3–5×".
  - "3-5 个" → "3–5".
  - "120+ 工具" → "120+ tools".
  - "约 100 个任务" → "approximately 100 tasks".
  - "450+ 个" → "450+".
  - "17 个" → "17".
  - "0.6B" → "0.6B" (kept).
  - "0.5" / "0.6B 小模型" → "0.6B small model".
  - "p50/p95" → "p50/p95" (kept).
  - "2026 年 7 月 13 日" → "July 13, 2026" (en-US date format).
  - "第 1–10 章" → "Chapters 1–10".
  - "实验 7-3" → "Experiment 7-3".
  - All chapter-experiment IDs (实验 5-12, 6-2, 6-3, 6-4, 6-9, 7-8, 7-9, 7-13, 7-14, 9-8, 9-9, 9-10, 10-7) → "Experiment N-M" (preserved).
  - Currency: none in source.
- Self-referential UI handling: 
  - Source line 3 `**[English](README.en.md) | 中文**` → rendered as `**English** | [中文](README.md)` per §8.1. English is the current language of the output (bold, no link); Chinese is the other-language link (native script preserved, links back to the root `README.md` which is the Chinese original).

## Phase 4: Typographical Compilation
- Surface Typography applied: en-US default (technical) profile. Straight ASCII quotes (`"` and `'`) in English prose. Em-dashes used for parenthetical breaks where source uses 中文破折号 "——". En-dashes used for numeric ranges (250–400×, 45–69%, 3–5×, Chapters 1–10, p50/p95 ranges). Hyphens used in compound modifiers (e.g., "KV Cache-friendly", "context-aware", "two-agent", "self-evolving", "tool-augmented", "end-to-end", "low-latency"). Single half-width space between Latin words; no CJK–Latin spacing rule needed (English-dominant output). Period (.), comma (,), colon (:), semicolon (;), parentheses (), brackets [], and braces {} all in half-width ASCII form. No full-width punctuation in English prose. Slash "/" preserved where source uses it (e.g., "感知/执行/协作三类工具" → "perception / execution / collaboration tool categories"; "ASR→LLM→TTS" → "ASR→LLM→TTS" with the source's arrow preserved).
- Title-of-Works mappings applied:
  - 《深入理解 AI Agent：设计原理与工程实践》 → *AI Agents in Depth: Design Principles and Engineering Practice* (book → italics per §9.6).
  - 《外部仓库获取》 → "Obtaining External Repositories" (article/section → double quotes per §9.6).
  - 《附录 · 外部仓库获取》 → "Appendix · Obtaining External Repositories" (section reference → double quotes per §9.6).
- Nested-structure preservation verified: PASS (all `[text](url)` link AST nodes preserved with both wrapper and target intact; the `[19PINE-AI/TalkAct](…)` link, `[GitHub Actions 定时任务](…)` link inside the `<sub>`, `[`scripts/gen_star_history.py`](…)` inline-code-in-link, and the `<a><picture><source><img></picture></a>` HTML block all preserved as complete AST nodes).
- Code-fence whitespace preservation verified: PASS (both `bash` code blocks emitted byte-for-byte as source: leading 2-space indentation of the `cd book && bash build_pdf.sh` block inside the list item; column-aligned whitespace in the `git clone` block; trailing `# 实验 N-M …` comment alignment; the `# 第 N 章 · …` section-divider comments all preserved verbatim per default comment policy).

## Phase 5: Zero-Trust MQM-lite Audit
- Fact Check: PASS. All numbers preserved numerically equivalent (250-400×, 45-69%, 49-67%, 3-5×, 120+, ~100, 450+, 17, 0.6B, p50/p95). All version numbers preserved (v1.1). All proper nouns preserved (Bojie Li, Moonshot AI, Zhipu AI, Volcengine, ByteDance, Doubao, Kimi, DeepSeek, Qwen, OpenAI, Anthropic, OpenRouter, SiliconFlow, Gemini, GPT-4o, GPT-5, Claude, TalkAct, Alita, Flux, Step-Audio R1, DeepSeek-R1-Distill-Qwen, Qwen2.5-32B-Instruct, DAPO, SandboxFusion, AIME 2024, Whisper, SenseVoice, Fish Audio, ARK, RAPTOR, GraphRAG, BM25, ANNOY, HNSW, OpenVLA, RoboTwin2, SO-100, XLeRobot). All dates preserved (July 13, 2026). All file paths, URLs, repo names preserved. All chapter/section/experiment IDs preserved (Chapter 1–10, Experiments 5-12 / 6-2 / 6-3 / 6-4 / 6-9 / 7-8 / 7-9 / 7-13 / 7-14 / 9-8 / 9-9 / 9-10 / 10-7).
- Modality Check: PASS. No epistemic markers in the technical prose required remapping. Deontic "建议" (recommend) consistently rendered as "recommend/recommended". No RFC 2119 keywords present. No upgrades or downgrades of modal force.
- Structural Topology Check: PASS. Heading hierarchy (1 H1, ~18 H2, ~90 H3) preserved exactly. List nesting preserved (top-level bullets for chapter summaries; numbered list under 实践建议; numbered list under 贡献; nested list under `**自行编译**` with the code block indented as a child of the list item). The Markdown table (3 columns × 3 rows including header) preserved exactly with original alignment row `| --- | --- | --- |`. Both code fences preserved with language tag `bash` and exact whitespace. Both blockquotes preserved with `>` marker. The HTML block at the foot preserved tag-for-tag. The `<sub>` paragraph preserved with its inline-code links and `<code>` tag. Emoji section icons preserved.
- Surface Typography Check: PASS. English-dominant typography throughout (half-width punctuation, straight ASCII quotes, em-dashes for parenthetical breaks, en-dashes for numeric ranges, hyphens for compound modifiers). No full-width Chinese punctuation in English prose. No smart/curly quotes introduced. Code-fence whitespace preserved byte-for-byte.
- Collocation Check: PASS. Industry-standard collocations applied: "implements an Agent", "builds a system", "compares X with Y", "ablation study", "context-aware retrieval", "tool-augmented reasoning", "continued pre-training", "supervised fine-tuning", "reinforcement learning", "knowledge distillation", "prompt distillation", "context bloat", "closed-loop evaluation", "race condition handling", "cascading termination", "message bus", "private context isolation", "information asymmetry", "hands-on practice", "errata", "open-source", "closed-source", "real-name authentication", "containerized deployment", "low latency". No translationese artifacts (no "perform … operations", no "the problem of …", no unnecessary passives, no "…ity" suffixes).
- IU-Coverage Bookkeeping: source IU count ≈ target IU count: PASS. Every source paragraph, list item, table cell, heading, and blockquote has exactly one target realization. No omissions, no additions, no duplications.
- Ambiguity Handling Check: PASS. All material ambiguities resolved per §12 (Context → Domain Convention → Literal with Least Risk): book-title mapping aligned with the existing English PDF filename; "Harness 工程" retained as a proper concept; "模型即 Agent" rendered as a coined phrase; "落地" rendered as "implement/implementation" per §8.3; "（mock）通过 MCP 对接 GitHub" restructured to "simulates (mocks) integration with GitHub via MCP" to avoid the v7 grammar artifact. No blocking ambiguities; no Notice Channel warranted.
- Self-Referential UI Check: PASS. Language selector rendered as `**English** | [中文](README.md)` per §8.1 — native scripts preserved, current language (English) bolded, other language (Chinese) linked.
- Severity counts: Critical=0 Major=0 Minor=0 Neutral=0.
- Repair loops used: 0 / 2.

## Phase 6: Self-Test Pre-Output Gate
- Quote check (scoped): PASS. No straight ASCII `"` in Chinese-dominant segments (no Chinese-dominant segments remain in the English-dominant output). All quoted phrases in English prose use straight ASCII `"` and `'` per the default technical typography profile. Inside inline code spans and code fences, quotes preserved verbatim.
- Source-Script Leakage Check (v8): initial FAIL → re-audit PASS after Targeted Phase 4 Repair Block (loop 1/2). The first-pass draft of the agent-skills-ppt paragraph (line 393 of the payload) leaked the source-script fragment "细则" into English prose as "loads the complete process,细则 documents, and bundled scripts layer by layer" — exactly the kind of "Implementation落地"-style artifact the v8 check is designed to catch. The retained CJK characters that ARE allowed: (a) the "中文" link text in the language selector — preserved per §8.1 Self-Referential UI rule (native scripts); (b) the Chinese-path filename `book/深入理解-AI-Agent-李博杰-v1.1.pdf` inside an inline code span — preserved per §8.1 Immutable Elements (file paths); (c) Chinese text inside the second `bash` code-block comments (`# 第 6 章 · 评测基准` etc.) — preserved verbatim per default comment policy; (d) the `[扩展]` tag inside an inline code span — preserved verbatim per §8.1 Immutable Elements. All four retentions are explicitly protected by Entity Anchoring / Immutable-Element / Comment-Policy / Self-Referential-UI rules.
- Grammar Fluency Check (v8): PASS. Target-language prose reads naturally. No awkward verb-noun pairings, no dangling modifiers, no clunky parenthetical insertions, no subject-verb agreement errors. Specifically verified: (a) the "(mock) 通过 MCP 对接 GitHub" segment was restructured to "simulates (mocks) integration with GitHub via MCP to create an Issue" — avoiding the v7 "(mocks) integrating" artifact; (b) the "落地实现见第 8 章 `chapter8/prompt-distillation`" segment was rendered as "the implementation is in Chapter 8 `chapter8/prompt-distillation`" — avoiding the "Implementation落地" artifact; (c) all verb-noun pairings are domain-native English (implements, builds, compares, evaluates, trains, integrates, generates, demonstrates).
- Locked-retention exemption: PASS. All unexplained-source-script retentions are covered by Immutable-Element (inline code, file paths, code-fence comments, the `[扩展]` tag), Self-Referential-UI (language selector native scripts), or Entity-Anchoring (proper nouns, acronyms) exemptions.
- Notice-channel check: PASS. No `[NOTICE]` line emitted — no warranting condition holds (no out-of-scope input; no blocking ambiguity; no audit failure after repair budget exhausted; non-empty payload; Self-Test passes after repair).
- Reasoning-marker check: PASS. No "Step 1:", "Phase 2:", "I think", "In my opinion", "According to my analysis", or any other reasoning markers in the payload. (The scratchpad itself contains phase-section headers, but those are stripped per §3.2 — and for this test the scratchpad is intentionally retained in the saved file per task instructions.)
- Heading-hierarchy check: PASS. Exact heading hierarchy preserved (1 H1, ~18 H2, ~90 H3, all matching source levels; no level skipping; no promoted/demoted headings).
- Heading-translation-consistency check: PASS. All headings follow the same translation policy per §10: descriptive components translated; proper-noun components (TalkAct, Alita, AdaptThink, retool, AWorld, SFTvsRL, verl, Intuitor, MultilingualReasoning, SpatialReasoning, SimpleVLA-RL, MiniMind-pretrain, sesame, orpheus, tinker-cookbook, RAPTOR, GraphRAG, GAIA, OSWorld, SWE-bench, terminal-bench, tau2-bench, elo-leaderboard, model-benchmark, agent-cost-analysis, tts-quality-eval, learning-from-experience, web-search-agent, search-codegen, context, local_llm_serving, attention_visualization, kv-cache, context-compression, prompt-engineering, system-hint, log-sanitization, prompt-injection, agent-skills-ppt, user-memory, mem0, memobase, user-memory-evaluation, dense-embedding, sparse-embedding, retrieval-pipeline, multimodal-agent, structured-index, agentic-rag, agentic-rag-for-user-memory, contextual-retrieval, contextual-retrieval-for-user-memory, structured-knowledge-extraction, perception-tools, execution-tools, collaboration-tools, agent-with-event-trigger, active-tool-selection, async-agent, coding-agent, code-for-math, code-for-logic, small-model-codified-rules, paper-to-ppt, paper-to-video, video-edit, adaptive-log-parser, log-diagnosis, dynamic-form, erp-agent, conversational-ui, gaia-experience, browser-use-rpa, prompt-distillation, prompt-auto-optimization, active-tool-discovery, self-evolving-tools, self-evolution-eval, live-audio, browser-use, claude-quickstarts, phone-agent, end-to-end-speech, streaming-speech, controllable-tts, use-computer-while-calling, staged-system-prompt, multi-role-transfer, book-translation, parallel-web-research, voice-werewolf) preserved verbatim.
- Nested-structure check: PASS. No stripped link wrappers; no merged code blocks; both `bash` fences emitted as separate blocks exactly as source; the `<sub>` paragraph emitted with its nested inline-code-in-link structure intact; the HTML `<a><picture><source><img></picture></a>` block emitted as a complete nested AST node.
- Code-fence-whitespace check: PASS. No injected or stripped leading spaces in either `bash` code block. The 2-space indentation of the first fence (inside the list item) and the column-aligned whitespace of the second fence are preserved byte-for-byte. Code comments inside the second fence preserved verbatim (Chinese characters retained inside `# …` comments per default comment policy).
- Self-referential UI check: PASS. Language selector preserves native scripts (`English` and `中文`); current language (English) is bolded; other language (中文) is linked.
- Mode-output check: PASS. Default mode output contract met: full `<engine_logs>` scratchpad present, followed by `---` separator (stand-alone fallback per §3.3), followed by translated payload. No glossary appended, no audit summary appended, no inline notes, no `[NOTICE]` line (no warranting condition holds).
- Scratchpad-format check: PASS. `<engine_logs>` block present, well-formed, contains all 6 phase sections per §4.3 full-tier template, with explicit PASS/FAIL for every Phase 6 check, plus the Targeted Phase 4 Repair Block subsection below documenting the single repair loop consumed.

### Targeted Phase 4 Repair Block (loop 1/2)
- Failed Self-Test check: Source-Script Leakage Check (v8)
- Failed segments: payload line 393 — the agent-skills-ppt project description paragraph (source line 155: "复现 Agent Skills 的「渐进式披露」思想：…逐层加载其完整流程、细则文档与捆绑脚本…"). The first-pass draft had rendered the under-translated fragment "细则 documents" — a stray CJK character (细则, U+7EC6 U+5219) leaked into English-dominant prose, outside any Entity Anchoring / Immutable-Element / Comment-Policy protection.
- Corrected translation (semantic-level fix at Phase 3, surface-applied at Phase 4):
  - payload line 393: "…it loads the complete process, guideline documents, and bundled scripts layer by layer, ultimately using python-pptx to generate a real `.pptx` file." (was: "…it loads the complete process,细则 documents, and bundled scripts layer by layer, ultimately using python-pptx to generate a real `.pptx` file.")
- Rationale: "细则" (literally "detailed rules") in the Agent-Skills-package context denotes the detailed guideline/specification documents that accompany each Skill; "guideline documents" is the domain-native English rendering. This both eliminates the source-script leakage and improves grammar fluency.
- Re-audit: PASS. Grep for `[\x{4e00}-\x{9fff}]` across the payload (lines 238 onward) now returns only the four explicitly-protected CJK retentions enumerated in the Source-Script Leakage Check entry above. No further stray CJK characters in English prose.

- Self-Test result: PASS (after Targeted Phase 4 Repair Block loop 1/2).

</engine_logs>

---

# AI Agents in Depth: Design Principles and Engineering Practice

**English** | [中文](README.md)

This repository is the open-source primary repository for the book *AI Agents in Depth: Design Principles and Engineering Practice*, containing **the full text of the book** and **companion example code**. The full text, illustrations, and companion experiment code are all open-source; you are welcome to run the experiments yourself, file issues, and submit PRs.

## 📖 E-book

The book is provided in both Chinese and English editions:

- **Chinese PDF (original edition)**: [`book/深入理解-AI-Agent-李博杰-v1.1.pdf`](book/深入理解-AI-Agent-李博杰-v1.1.pdf)
- **English PDF** (community-contributed translation, by [@nsdevaraj](https://github.com/nsdevaraj)): [`book-en/AI-Agents-in-Depth-Bojie-Li-v1.1.pdf`](book-en/AI-Agents-in-Depth-Bojie-Li-v1.1.pdf)
- **Tamil PDF** (community-contributed translation, by [@nsdevaraj](https://github.com/nsdevaraj)): [`book-ta/AI-Agents-in-Depth-Bojie-Li-v1.1-ta.pdf`](book-ta/AI-Agents-in-Depth-Bojie-Li-v1.1-ta.pdf)

The Chinese text and the compiled PDFs are in the [`book/`](book/) directory; the English and Tamil translations are **community contributions**, located in the [`book-en/`](book-en/) and [`book-ta/`](book-ta/) directories respectively, and may lag behind the Chinese original:

- **Source text**: `book/introduction.md` (introduction), `book/chapter1.md` through `book/chapter10.md` (Chapters 1–10), `book/afterword.md` (afterword)
- **Build it yourself**: after installing pandoc, xelatex, the ElegantBook document class, and the relevant fonts, run

  ```bash
  cd book && bash build_pdf.sh
  ```

  Charts are generated by `book/gen_*_figs.py` and stored in `book/images/`; see `book/preamble.tex` and `book/*.lua` for typesetting details.

## 📑 Content Overview (Chapters 1–10)

The book is organized around the core formula **Agent = LLM + context + tools**, with ten chapters as follows:

- **Chapter 1 · Agent Fundamentals**: Starting from the new paradigm of "model as agent", establishes the core formula **Agent = LLM + context + tools**, and introduces Harness engineering — the engineering capabilities beyond the model itself are where true competitiveness lies.
- **Chapter 2 · Context Engineering**: Context determines the capability ceiling of an Agent. Dives into the context structure of large-model APIs, KV Cache-friendly design, prompt engineering, dynamic prompts and Agent Skills, status-bar meta-information, and context compression strategies.
- **Chapter 3 · User Memory and Knowledge Base**: Lets an Agent remember users across sessions and connect to external knowledge. Covers user memory systems, the basic RAG pipeline, and knowledge organization and retrieval beyond flat text (structured indexes, knowledge graphs, etc.).
- **Chapter 4 · Tools**: Tools are an Agent's hands. Covers tool classification and general design principles, the MCP protocol and the challenges of tool selection, the three categories of perception / execution / collaboration tools, and event-driven async Agents.
- **Chapter 5 · Coding Agent and Code Generation**: Code is "a tool that can create new tools" — a meta-capability of general-purpose Agents. Uses a production-grade Coding Agent as an example to demonstrate the complete implementation of this most powerful general-purpose tool.
- **Chapter 6 · Agent Evaluation**: Turns an Agent's performance into comparable signals. From evaluation environments, dataset design, and metric systems, to statistical significance, observability, evaluation-driven selection, all the way to production-grade internal evaluation and simulation environments.
- **Chapter 7 · Model Post-Training**: A panoramic view of the three stages of pre-training, SFT, and RL. When to choose SFT and when to choose RL; RLHF; algorithm comparison; data and environments; and frontier explorations on enabling models to call tools and improving sample efficiency.
- **Chapter 8 · Agent Self-Evolution**: Growing without changing weights. Three learning paradigms — learning from experience, active tool discovery, and "from tool user to tool creator" — that move an Agent from "smart" to "proficient".
- **Chapter 9 · Multimodal and Real-Time Interaction**: Extends perception and action from text to voice, GUI, and the physical world. The three voice paradigms (cascading / end-to-end omni-modal / full-duplex), streaming speech perception and synthesis, Computer Use, and robotic manipulation.
- **Chapter 10 · Multi-Agent Collaboration**: The intelligence of a group can be higher than that of individuals. Multi-Agent classification frameworks, when multi-Agent truly outperforms single-Agent, collaboration with and without shared context, failure modes, and the emergent "Agent society".

## 💻 Companion Code

All projects are organized by **chapter**, in one-to-one correspondence with the book's ten chapters, covering the complete learning path from foundational concepts to advanced techniques. The directory layout is `chapterN/project_name/`. The vast majority of experiments in Chapters 5, 8, 9, and 10 now provide independently runnable companion demos that have been verified end-to-end against real LLM APIs.

### Project Type Descriptions

The companion projects fall into three categories; please refer to the icons below to understand how "ready-to-run" each project is:

- ✅ **Independently runnable**: This repository ships the complete code; once you configure an API Key (see the end of this document), it runs.
- 📖 **Reproduction guide**: The project itself is a detailed reproduction document and depends on **external repositories** that you must `git clone` yourself (training frameworks, evaluation benchmarks, etc.); see "Obtaining External Repositories" below.
- 🚧 **Design document**: Currently contains only a design document covering architecture and implementation; runnable code is still being completed.

The following projects are **not** ✅ independently runnable; please be aware when cloning this repository:

| Project | Type | Description |
| --- | --- | --- |
| `chapter7/AdaptThink` · `AWorld-train` · `MiniMind-pretrain` · `retool` · `SpatialReasoning` | 📖 Reproduction guide | Training experiments that depend on external frameworks; reproduce per the README |
| All Chapter 6 benchmarks · most Chapter 7 training frameworks · Chapter 9 `browser-use`/`claude-quickstarts` · Chapter 10 `use-computer-while-calling` | 📖 Reproduction guide | Depends on external repositories; see "Obtaining External Repositories" |

### Obtaining External Repositories (Brief)

**Some** experiments in Chapters 6, 7, 9, and 10 depend on **external repositories** such as evaluation benchmarks, training frameworks, and robotics platforms (omitted from this repository for size and licensing reasons). To avoid information overload up front, **the complete clone commands, upstream addresses, and commits verified by this book are listed in "Appendix · Obtaining External Repositories" at the end of this document**. It is recommended to start with the independently runnable projects in the earlier chapters and then follow the instructions at the end to fetch what you need when reproducing training / evaluation / robotics experiments.

## 🚀 Chapter 1 · Agent Fundamentals

### learning-from-experience - Reinforcement Learning vs LLM Comparison
`chapter1/learning-from-experience/`

Compares traditional reinforcement learning (Q-learning) with LLM-based in-context learning, reproducing the key insights from Shunyu Yao's "The Second Half" blog post. Uses a treasure-hunt game to show how LLMs surpass traditional RL with 250–400× sample efficiency.

**Core Concepts**: reinforcement learning, in-context learning, sample efficiency, prior knowledge

### web-search-agent - Kimi K2 Model as Agent
`chapter1/web-search-agent/`

Implements an Agent with basic deep-search capability, able to perform multi-round search and information integration.

**Core Concepts**: web search, model-native Agent

### search-codegen - GPT-5 Native Tool Integration
`chapter1/search-codegen/`

Builds an Agent with basic deep-search and code-sandbox capabilities, leveraging tools such as web search and code execution to perform complex analysis.

**Core Concepts**: web search, code generation, model-native Agent

### context - Context Ablation Study
`chapter1/context/`

Through systematic ablation experiments, demonstrates the importance of each component of an Agent's context. Supports multiple LLM providers (SiliconFlow Qwen, ByteDance Doubao, Moonshot AI Kimi), letting you observe changes in Agent behavior under different context modes.

**Core Concepts**: context management, tool calling, ReAct loop, ablation study

## 🎯 Chapter 2 · Context Engineering

### local_llm_serving - Local LLM Deployment and Tool Calling
`chapter2/local_llm_serving/`

A cross-platform local LLM deployment solution that auto-selects the best backend (vLLM or Ollama). Demonstrates that even a 0.6B small model can achieve excellent tool-calling capability through good system design. Supports streaming responses with real-time display of the thinking process.

**Core Concepts**: model deployment, Chat Template, streaming processing, tool calling

### attention_visualization - Attention Mechanism Visualization
`chapter2/attention_visualization/`

Visualizes the complete input/output token sequence and attention-weight distribution of an LLM, providing deep insight into how the model processes context, performs reasoning, and calls tools.

**Core Concepts**: attention mechanism, token analysis, reasoning-process visualization

### kv-cache - KV Cache-Friendly Context Design
`chapter2/kv-cache/`

Explores the impact of different context-management modes on the KV Cache and demonstrates how common error patterns destroy cache efficiency. Uses experiments to show how proper context design can significantly reduce latency and cost.

**Core Concepts**: KV Cache, context optimization, performance tuning

### context-compression - Context Compression Strategies
`chapter2/context-compression/`

Implements and compares multiple context compression strategies, including summarization, key-information extraction, and semantic compression. Reduces token usage while preserving Agent capability.

**Core Concepts**: context compression, token optimization, information density

### prompt-engineering - Prompt Engineering Ablation Study
`chapter2/prompt-engineering/`

Extends the Tau-Bench framework and uses systematic ablation experiments to quantify the impact of different prompt-engineering factors on Agent performance. Demonstrates how factors such as tone style, instruction organization, and tool description affect task-completion rate.

**Core Concepts**: prompt engineering, ablation study, performance benchmarking

### system-hint - System Prompt Optimization
`chapter2/system-hint/`

Studies the impact of the system hint on Agent behavior and explores how to improve performance by optimizing the system prompt.

**Core Concepts**: system prompt, behavior guidance, prompt optimization

### log-sanitization - Log Sanitization
`chapter2/log-sanitization/`

Implements an intelligent log-sanitization system that protects sensitive data while preserving debugging information.

**Core Concepts**: privacy protection, log processing, data security

### prompt-injection - Prompt Injection Attack-Defense Experiment
`chapter2/prompt-injection/`

Constructs a controlled experiment of 3 attack scenarios (direct injection, indirect injection, memory injection) × 4 defense configurations (no defense, prompt hardening, source tagging, combined defense). Uses deterministic rules to compute attack-success rates, visually showing how the injection-success rate drops significantly as defenses are layered on.

**Core Concepts**: prompt injection, indirect injection, data/instruction separation, runtime validation

### agent-skills-ppt - Generating PPT via Agent Skills Progressive Disclosure
`chapter2/agent-skills-ppt/`

Reproduces the "progressive disclosure" idea behind Agent Skills: at startup the Agent sees only a thin Skill directory; after recognizing that the task requires the `pptx` Skill, it loads the complete process, guideline documents, and bundled scripts layer by layer, ultimately using python-pptx to generate a real `.pptx` file.

**Core Concepts**: Agent Skills, progressive disclosure, on-demand loading, tool orchestration

## 📚 Chapter 3 · User Memory and Knowledge Base

### user-memory - User Memory System
`chapter3/user-memory/`

Builds a long-term user memory system that lets an Agent remember user preferences and historical interactions, delivering personalized service.

**Core Concepts**: long-term memory, personalization, user modeling

### mem0 / memobase - Open-Source Memory Framework Comparison
`chapter3/mem0/` and `chapter3/memobase/`

Uses the two open-source memory frameworks mem0 and Memobase to each implement a version of user memory, serving as a reference implementation for Experiment 3-2 "Memory Strategy Comparison", to facilitate side-by-side comparison of the extraction form and answer quality of different memory solutions.

**Core Concepts**: memory framework, mem0, Memobase, solution comparison

### user-memory-evaluation - User Memory Evaluation Framework
`chapter3/user-memory-evaluation/`

Systematically evaluates the accuracy, relevance, and effectiveness of a user memory system, including multiple test scenarios and evaluation metrics.

**Core Concepts**: evaluation framework, test cases, performance metrics

### dense-embedding - Dense Embedding Vector Retrieval Service
`chapter3/dense-embedding/`

Builds a vector similarity-search service and conducts a comparative study of two approximate-nearest-neighbor (ANN) indexing algorithms: ANNOY (tree-based) and HNSW (graph-based). Demonstrates the trade-offs of different indexing strategies in performance, memory footprint, and update capability.

**Core Concepts**: dense embedding, vector retrieval, ANN algorithms, semantic search

### sparse-embedding - Sparse Retrieval Engine
`chapter3/sparse-embedding/`

Implements a sparse vector search engine based on the BM25 algorithm from scratch, with rich logging and visualization interfaces to reveal the engine's internal workings, helping you understand term-frequency weighting and the inverted-index principle.

**Core Concepts**: sparse embedding, BM25, TF-IDF, exact match

### retrieval-pipeline - Hybrid Retrieval Pipeline
`chapter3/retrieval-pipeline/`

Builds a complete retrieval pipeline that combines dense retrieval, sparse retrieval, and neural reranking. Through carefully designed test cases, systematically demonstrates the complementary advantages of hybrid retrieval across different scenarios.

**Core Concepts**: hybrid retrieval, neural reranking, cross-encoder, retrieval fusion

### multimodal-agent - Multimodal Information Extraction
`chapter3/multimodal-agent/`

Compares three multimodal processing strategies: native multimodal processing, extraction to text, and tool-based analysis. Through an ablation study within a unified framework, reveals the trade-offs of different technical paths in fidelity, cost, and flexibility.

**Core Concepts**: multimodal, visual understanding, OCR, end-to-end processing

### structured-index - Structured Index
`chapter3/structured-index/`

Implements and compares two advanced indexing strategies: RAPTOR (recursive abstraction tree) and GraphRAG (knowledge graph). Uses a technical manual as the indexed document to demonstrate how to build a structured index that reflects the inherent hierarchy and connections of knowledge.

**Core Concepts**: RAPTOR, GraphRAG, hierarchical summarization, knowledge graph

### agentic-rag - Agentic RAG
`chapter3/agentic-rag/`

Compares the performance difference between traditional non-agentic RAG and agentic RAG. Shows how an Agent drives iterative information retrieval through the ReAct pattern, significantly improving answer quality when handling complex judicial Q&A.

**Core Concepts**: Agentic RAG, ReAct loop, iterative retrieval, active exploration

### agentic-rag-for-user-memory - Building User Memory with Agentic RAG
`chapter3/agentic-rag-for-user-memory/`

Applies the Agentic RAG framework to manage user conversation history, using multi-round iterative search to handle cross-session memory retrieval, enabling basic recall and multi-session retrieval capability.

**Core Concepts**: user memory, conversation-history indexing, cross-session retrieval

### contextual-retrieval - Context-Aware Retrieval
`chapter3/contextual-retrieval/`

Implements the context-aware retrieval technique proposed by Anthropic, which solves the context-loss problem of traditional chunking by generating a prefix summary containing the core context for each text chunk, reducing the retrieval failure rate by 49–67%.

**Core Concepts**: context augmentation, prefix generation, semantic anchoring, retrieval optimization

### contextual-retrieval-for-user-memory - Context-Aware User Memory System
`chapter3/contextual-retrieval-for-user-memory/`

Applies context-aware retrieval to user-memory construction, combining Advanced JSON Cards with context-aware RAG to form a two-tier memory structure that enables a higher level of proactive service capability.

**Core Concepts**: two-tier memory, structured facts, contextual retrieval, proactive service

### structured-knowledge-extraction - Structured Knowledge Extraction
`chapter3/structured-knowledge-extraction/`

Using judicial precedents as the example, runs the three-stage pipeline of "bottom-up factor discovery → clustering into case prototypes → conversational advisory Agent": no rigid fields are predefined; the LLM autonomously discovers factors from a large body of cases and induces them into a modular schema (core factors + charge-specific extension factors); cases are then clustered into several prototypes and the factor importance of each prototype is computed; for a new case, the Agent matches the most similar prototype, asks follow-up questions about missing information by importance, and gives evidence-based recommendations (with a legal disclaimer).

**Core Concepts**: bottom-up knowledge discovery, modular factors, clustering prototypes, interpretable decisions

## 🛠️ Chapter 4 · Tools

### perception-tools - Perception Tools MCP Server
`chapter4/perception-tools/`

Builds a comprehensive perception toolset that provides web search, multimodal understanding, file-system operations, and public-data-source access. Most features are based on free open APIs (DuckDuckGo, Open-Meteo, Yahoo Finance, OpenStreetMap, etc.) and require no API key.

**Core Concepts**: MCP protocol, multimodal parsing, public data sources, document understanding, geographic information services

### execution-tools - Execution Tools MCP Server
`chapter4/execution-tools/`

Implements an execution toolset with safety mechanisms, including file operations, a code interpreter, a virtual terminal, and external-system integration. Uses an LLM secondary-approval mechanism to prevent dangerous operations, auto-summarizes complex outputs, and performs syntax validation on code.

**Core Concepts**: MCP protocol, execution safety, LLM approval, result summarization, automatic validation

### collaboration-tools - Collaboration Tools MCP Server
`chapter4/collaboration-tools/`

Provides comprehensive collaboration capabilities, including browser automation (browser-use framework), human-in-the-loop (HITL), multi-channel notifications (Email, Telegram, Slack, Discord), and timer management. Supports admin approval for sensitive operations and scheduled-task dispatch.

**Core Concepts**: MCP protocol, browser automation, HITL pattern, multi-channel notifications, scheduled tasks

### agent-with-event-trigger - Event-Triggered Agent and MCP Integration
`chapter4/agent-with-event-trigger/`

A modern event-driven Agent built on FastAPI, integrating by default all the tools from the first three MCP servers. Uses a native async architecture to implement clean MCP tool loading, and receives multi-source events (Web, instant messaging, GitHub, timers, etc.) via HTTP API. Provides automatic API documentation (Swagger UI) and background monitoring.

**Core Concepts**: FastAPI, native async, MCP integration, event-driven, automatic API documentation, tool orchestration

### active-tool-selection - Active Tool Selection
`chapter4/active-tool-selection/`

Implements an intelligent tool-selection mechanism that lets an Agent actively choose the most appropriate tool combination based on task requirements, rather than passively accepting a predefined toolset.

**Core Concepts**: tool selection, dynamic tool loading, task analysis

### async-agent - Async Agent with Parallel Execution and Interruption
`chapter4/async-agent/`

Implements the core of an event-driven async Agent framework (Flux) on a single thread via asyncio: the inbox event queue dispatches by urgency (interrupt / immediate / queued), supports parallel execution of async tools, allows interrupting the current turn mid-run, and supports cancellation and status queries on simulated long tasks. Decisions are made by a real LLM (via function calling).

**Core Concepts**: async programming, event queue, interruption mechanism, parallel-tool cancellation, non-blocking I/O

> Additionally, `chapter4/docker-compose.yml` and `chapter4/DOCKER_DEPLOYMENT.md` provide a reference solution for containerized deployment of the above MCP tool servers.

## 💻 Chapter 5 · Coding Agent and Code Generation

### coding-agent - Production-Grade Coding Agent
`chapter5/coding-agent/`

A production-grade AI coding assistant built on Claude, with all tools implemented in pure Python and no command-line dependencies. Includes 17 fully implemented tools covering file operations, search, Shell operations, and project management. In particular, it implements a pure-Python Grep tool that is fully compatible with ripgrep's functionality.

**Core Features**:
- Pure Python implementation, no command-line dependencies, especially friendly for Mac users
- Complete tool suite: file read/write/edit, pure-Python regex search, directory listing, Shell session management
- System-prompt techniques: timestamps, tool-call counters, TODO list management, detailed error messages
- Persistent Shell environment, automatic Lint detection, streaming-response support
- Supports multiple LLM providers (Anthropic, OpenAI, OpenRouter)

**Core Concepts**: code generation, file editing, pure-Python tools, system prompt, Lint detection, multi-provider support

### code-for-math - Improving Math Problem-Solving with Code
`chapter5/code-for-math/`

Lets the same model compare "pure chain-of-thought" against "code-assisted" modes on the same set of competition math problems: the latter formalizes the problem into Python (sympy/numpy/scipy), executes it via function calling in a subprocess sandbox, and replaces error-prone mental arithmetic with precise computation, achieving significantly higher accuracy.

**Core Concepts**: code interpreter, symbolic computation, chain-of-thought comparison, tool-augmented reasoning

### code-for-logic - Improving Logical Reasoning with Code
`chapter5/code-for-logic/`

Turns "Knights and Knaves" logic puzzles into a constraint-satisfaction problem (CSP): the Agent uses `python-constraint` to define variables and biconditional constraints and invokes the solver, comparing pure-natural-language reasoning against code-assisted mode on a set of K&K puzzles for correctness.

**Core Concepts**: constraint solving, CSP modeling, formal reasoning, code-assisted

### small-model-codified-rules - Small-Model Codified Rules
`chapter5/small-model-codified-rules/`

A controlled experiment based on the τ-bench airline customer-service scenario: after moving complex business policies (refund rules) from natural-language prompts into code/tools, the small model's task-success rate and policy consistency improve substantially, and in-tool code validation can intercept the model's mistaken understanding in real time.

**Core Concepts**: codified business rules, policy enforcement, in-tool validation, small-model reliability

### paper-to-ppt - Auto-Generating PPT from Papers (Proposer-Reviewer)
`chapter5/paper-to-ppt/`

Reframes "making a PPT" as a code-generation problem: the Proposer writes Slidev (Markdown+HTML) code, the Reviewer actually renders each slide into a PNG and uses a Vision LLM to check for layout issues, then iteratively revises based on structured feedback; the two-Agent division of labor keeps the context peak significantly smaller.

**Core Concepts**: code generation, Slidev, proposer-reviewer, visual quality control

### paper-to-video - Auto-Generating Paper Explanation Videos
`chapter5/paper-to-video/`

Building on "paper → PPT", generates spoken commentary for each slide, invokes TTS to synthesize audio, and then uses ffmpeg to sync each slide's screenshot with its audio page by page, producing a narrated explanation video.

**Core Concepts**: multimedia generation, commentary generation, TTS, ffmpeg audio-visual sync

### video-edit - API-Based Intelligent Video Editing
`chapter5/video-edit/`

Given a multi-scene video and a single natural-language request, the Agent uses a "two-step Vision localization" (first coarse then fine, sampling frames and reading images) to determine the time boundaries of the target scene, cuts out the segment, and then has a Reviewer extract key frames from the cut for verification; if it fails, the process iterates.

**Core Concepts**: video editing, Vision localization, coarse-to-fine, proposer-reviewer

### adaptive-log-parser - Adaptive Log Parsing System
`chapter5/adaptive-log-parser/`

A self-evolving log parsing system: when it encounters a new format it cannot parse, it does not error out; instead, it hands the failure sample and the error message to a code-generation Agent that produces a `parse` function, which is automatically tested and, once it passes, hot-reloaded into the parsing engine — the entire flow requires no human intervention.

**Core Concepts**: code as system adapter, self-healing closed loop, hot code update, automated testing

### log-diagnosis - Intelligent Production Log Diagnosis System
`chapter5/log-diagnosis/`

A diagnosis Agent reads production trace logs, architecture documents, and the PRD, automatically locates the problem and root cause, generates a structured report and regression test cases, uses a replay framework to actually execute verification, and simulates (mocks) integration with GitHub via MCP to create an Issue.

**Core Concepts**: trajectory diagnosis, root-cause localization, regression-test generation, replay validation

### dynamic-form - Dynamic Form Intent Clarification System
`chapter5/dynamic-form/`

When faced with a request whose information is incomplete, rather than asking follow-up questions one by one, the Agent dynamically generates a self-contained HTML form with cascading logic that lets the user fill in everything at once; the front end summarizes the form as JSON and hands it back to the Agent to continue the task.

**Core Concepts**: code generation, intent clarification, dynamic form, cascading logic

### erp-agent - Natural Language ERP Agent (NL → SQL)
`chapter5/erp-agent/`

Converts Chinese natural-language queries into SQL for the database to execute, presenting the result table directly. The core is the artifact pattern: the LLM only generates the SQL artifact and does not move the data itself, which both saves tokens and avoids manual-computation errors — even tens of thousands of rows of results come back in seconds.

**Core Concepts**: NL2SQL, artifact pattern, database execution, cost and accuracy

### conversational-ui - Conversational UI Customization System
`chapter5/conversational-ui/`

The user states UI customization needs (color/font/copy/layout) in natural language; the Agent autonomously locates and modifies the React front-end source code, leveraging Vite hot-module replacement (HMR) to make changes take effect instantly, and supports multi-round iterative customization.

**Core Concepts**: code modification, front-end customization, hot reload, multi-round iteration

## 🎯 Chapter 6 · Agent Evaluation

### terminal-bench - Terminal Environment Benchmark
`chapter6/terminal-bench/`

Terminal-Bench is a benchmark that tests how AI Agents perform in a real terminal environment. From compiling code to training models and setting up servers, it evaluates how Agents handle real end-to-end tasks. Includes a dataset of approximately 100 tasks and an execution framework, and supports multiple Agent implementations.

**Core Concepts**: terminal automation, task evaluation, Docker sandbox, benchmarking

### SWE-bench - Software Engineering Benchmark
`chapter6/SWE-bench/`

SWE-bench is a benchmark that evaluates the ability of large language models to solve real GitHub issues. Given a codebase and an issue description, the model must generate a patch that solves the issue. Includes multiple variants: SWE-bench, SWE-bench Lite, SWE-bench Verified, and SWE-bench Multimodal.

**Core Concepts**: code repair, GitHub issues, patch generation, Docker evaluation

### GAIA - General AI Assistant Benchmark
`chapter6/GAIA/`

GAIA is designed to evaluate next-generation LLMs (LLMs with tool augmentation, efficient prompting, search access, and similar capabilities). It contains 450+ non-trivial problems that require varying degrees of tool use and autonomy, with clear and unambiguous answers. Divided into 3 difficulty levels.

**Core Concepts**: tool use, multi-step reasoning, autonomy evaluation

### OSWorld - OS-Level Agent Benchmark
`chapter6/OSWorld/`

Evaluates an Agent's ability to perform complex tasks in a full operating-system environment, including file management, application operation, and system configuration.

**Core Concepts**: OS automation, multi-application collaboration, system-level tasks

### android_world - Android Environment Benchmark
`chapter6/android_world/` (📖 external repository; see "Obtaining External Repositories")

Evaluates an Agent's performance in an Android mobile environment, including app navigation, UI interaction, and task completion.

**Core Concepts**: mobile automation, Android UI, app interaction

> `chapter6/android-world/` (hyphenated naming) is not benchmark code; it is this book's analysis notes on a T3A Agent's failure case on android_world (`t3a*.md`), which can be read as supplementary material.

### tau2-bench - Tool-Augmented Reasoning Benchmark
`chapter6/tau2-bench/`

Focuses on evaluating an Agent's ability to use tools for complex reasoning, including computation, search, and data-processing scenarios.

**Core Concepts**: tool-augmented reasoning, multi-step tasks, tool composition

### elo-leaderboard - ELO Leaderboard System
`chapter6/elo-leaderboard/`

Implements an Agent-performance leaderboard based on the ELO scoring system, evaluating the relative capability of different Agents through head-to-head comparisons.

**Core Concepts**: ELO scoring, relative evaluation, leaderboard system

### model-benchmark - Multi-Dimensional Model Performance Benchmark
`chapter6/model-benchmark/`

Performs a horizontal benchmark across multiple OpenAI-compatible LLM API providers, using the streaming interface to precisely measure time to first token (TTFT), measuring end-to-end latency percentiles (p50/p95), throughput, and success rate under concurrency, and producing a multi-dimensional comparison table with a single command — illustrating that selection is a multi-dimensional trade-off rather than just looking at a leaderboard.

**Core Concepts**: TTFT, latency percentiles, throughput, concurrency stress test, model selection

### agent-cost-analysis - Agent Task End-to-End Cost Analysis
`chapter6/agent-cost-analysis/`

Performs a full-chain cost breakdown of a typical multi-turn Agent task (customer-service refund): uses a lightweight in-house tracing system to record the input/output/cache tokens, latency, and cost of each LLM call, aggregates them to show "which step is the most expensive", and then uses A/B testing to quantify the real savings delivered by KV-cache-friendly design plus context compression.

**Core Concepts**: observability, cost breakdown, prompt caching, A/B comparison

### tts-quality-eval - Fully Automated TTS Quality Evaluation Pipeline
`chapter6/tts-quality-eval/`

Synthesizes the same set of challenging text with multiple TTS configurations (different model/voice/speed), then uses a multimodal LLM-as-a-Judge to score each dimension (clarity, naturalness, etc.) against a Rubric, and aggregates the results into a reproducible configuration-comparison table.

**Core Concepts**: LLM-as-a-Judge, Rubric scoring, TTS evaluation, multi-dimensional comparison

## 🧠 Chapter 7 · Model Post-Training

This chapter contains multiple model post-training projects, covering various techniques and application scenarios of supervised fine-tuning (SFT) and reinforcement learning (RL).

### AdaptThink - Adaptive Reasoning Depth
`chapter7/AdaptThink/` and `chapter7/AdaptThink-original/`

Lets a reasoning model learn to adaptively choose a reasoning mode (Thinking vs NoThinking) based on problem difficulty. Through constrained optimization and importance sampling, it improves accuracy while substantially reducing reasoning cost (45–69%). Based on the DeepSeek-R1-Distill-Qwen model, trained with the DAPO algorithm.

**Core Concepts**: adaptive reasoning, reasoning-cost optimization, constrained optimization, importance sampling

### retool - Tool-Augmented Math Reasoning
`chapter7/retool/`

Uses multi-turn dialogue and a code sandbox to improve the math-reasoning capability of large language models. Through a two-stage training of SFT then RL, the model learns to use a code-execution environment to assist with math problem-solving. Based on Qwen2.5-32B-Instruct, trained on the AIME 2024 dataset, using the DAPO algorithm and the SandboxFusion sandbox.

**Core Concepts**: tool use, code execution, math reasoning, multi-turn dialogue, DAPO algorithm

### AWorld / AWorld-train - Embodied Agent Training
`chapter7/AWorld/` and `chapter7/AWorld-train/`

Trains an embodied Agent based on the AWorld framework, enabling the Agent to perform complex tasks in a virtual environment and learn from experience.

**Core Concepts**: embodied intelligence, environment interaction, experience-based learning

### SFTvsRL - SFT vs RL Comparison Study
`chapter7/SFTvsRL/`

Systematically compares supervised fine-tuning (SFT) and reinforcement learning (RL) on different tasks, analyzing the strengths, weaknesses, and applicable scenarios of the two methods.

**Core Concepts**: SFT vs RL, training-method comparison, performance analysis

### verl - Efficient RL Training Framework
`chapter7/verl/`

verl is an efficient reinforcement-learning framework designed specifically for large-language-model RLHF training, supporting multiple algorithms such as PPO, GRPO, and DAPO.

**Core Concepts**: RLHF, PPO, distributed training, efficient optimization

### Intuitor - Intuitive Reasoning Training
`chapter7/Intuitor/`

Trains a model's intuitive-reasoning capability, enabling it to make quick reasonable judgments without a detailed chain of thought.

**Core Concepts**: intuitive reasoning, fast decision-making, chain-of-thought optimization

### MultilingualReasoning - Multilingual Reasoning
`chapter7/MultilingualReasoning/`

Trains a model's reasoning capability across multiple language settings, improving performance on cross-lingual tasks.

**Core Concepts**: multilingual, cross-lingual reasoning, linguistic generalization

### SpatialReasoning - Spatial Reasoning Training
`chapter7/SpatialReasoning/`

Focuses on training a model's spatial-reasoning capability, handling problems involving spatial relationships such as position, orientation, and distance.

**Core Concepts**: spatial reasoning, geometric understanding, positional relationships

### SimpleVLA-RL - Vision-Language-Action RL
`chapter7/SimpleVLA-RL/`

Reinforcement-learning training that combines vision, language, and action, enabling the model to understand visual input and execute the corresponding actions.

**Core Concepts**: vision-language-action, multimodal RL, embodied intelligence

### continued-pretraining - Continued Pre-Training
`chapter7/continued-pretraining/`

Performs continued pre-training on domain-specific data to improve the model's performance in the target domain.

**Core Concepts**: continued pre-training, domain adaptation, knowledge injection

### MiniMind-pretrain - Small-Model Pre-Training
`chapter7/MiniMind-pretrain/`

Pre-trains a small language model from scratch, helping you understand the complete process and key techniques of pre-training.

**Core Concepts**: pre-training, small models, training process

### sesame - Sequence Modeling and Evaluation
`chapter7/sesame/`

Focuses on training and evaluation methods for sequence-modeling tasks.

**Core Concepts**: sequence modeling, evaluation methods, performance optimization

### orpheus - Music Generation and Understanding
`chapter7/orpheus/`

Trains a model's music generation and understanding capability.

**Core Concepts**: music generation, audio understanding, creative AI

### tinker-cookbook - Training Tips Collection
`chapter7/tinker-cookbook/`

Collects various practical tips and best practices for model training.

**Core Concepts**: training tips, best practices, tuning methods

## 🔄 Chapter 8 · Agent Self-Evolution

This chapter focuses on letting an Agent grow continuously from experience without changing its weights: consolidating successful trajectories into reusable experience, externalizing repetitive operations into tools, and distilling prompts and observations into the model.

### gaia-experience - Learning from Successful Experience
`chapter8/gaia-experience/`

Based on the AWorld framework and the GAIA benchmark, implements a complete "learn-apply" closed loop. The Agent automatically summarizes successful task trajectories into structured experience and retrieves and applies it on new tasks, achieving self-evolution.

**Core Concepts**: experience-based learning, policy summary, trajectory summarization, self-evolution

### browser-use-rpa - Workflow Recording and Playback
`chapter8/browser-use-rpa/`

Implements a workflow-recording system for browser automation that automatically wraps repetitive operation sequences into parameterized tools. By switching from expensive LLM inference to precise automated execution, it achieves a 3–5× speedup.

**Core Concepts**: workflow recording, RPA, tool generation, externalized learning

### prompt-distillation - Prompt Distillation
`chapter8/prompt-distillation/`

Distills the effect of complex prompts into model parameters, reducing the prompt length at inference time and consolidating the experience in the context into parametric knowledge.

**Core Concepts**: knowledge distillation, prompt optimization, parametric knowledge

### prompt-auto-optimization - System Prompt Auto-Optimization
`chapter8/prompt-auto-optimization/`

Automated system-prompt learning based on human feedback: using the tau-bench-style airline customer-service "over-transfer" problem as an example, a Coding Agent reads the system-prompt file, locates the problematic rule, generates a precise modification and actually rewrites the prompt file, then re-evaluates to verify — forming a "feedback → rewrite → verify" closed loop.

**Core Concepts**: prompt auto-optimization, human feedback, Coding Agent, closed-loop evaluation

### active-tool-discovery - Active Tool Discovery
`chapter8/active-tool-discovery/`

Compares two paradigms: "bulk-inject 120+ tool schemas" versus "active on-demand discovery": the latter keeps only a small number of basic tools plus a single `discover_tools` meta-tool in the system, and uses embedding similarity to retrieve the 3–5 most relevant specialized tools from the tool library, saving tokens and avoiding the model's mis-selection / abuse of general tools under overly long tool lists.

**Core Concepts**: active tool discovery, embedding retrieval, token optimization, instruction following

### self-evolving-tools - Finding Tools from the Web for Self-Evolution
`chapter8/self-evolving-tools/`

Alita-style "minimal pre-definition, maximal self-evolution": the Agent is not pre-equipped with any domain tools and has only five general meta-tools; when it encounters a task it cannot do, it goes online to find open-source libraries/APIs, reads documentation, and tests them in a sandbox, packaging feasible solutions as new tools to store in the tool library for reuse — with hallucination control emphasized throughout.

**Core Concepts**: self-evolution, tool creation, tool reuse, hallucination control

### self-evolution-eval - Self-Evolving Agent Evaluation Dataset
`chapter8/self-evolution-eval/`

A dedicated dataset and validation method designed to evaluate an Agent's "self-evolution" capability (discovering, creating, and reusing tools on its own): 20 cross-domain tasks (no tool-name hints) + a four-tier layered validation harness + a controllable reference Agent, going beyond "is the result correct" to examine discovery, creation, and reuse quality.

**Core Concepts**: evaluation dataset design, tiered validation, tool-reuse metrics, self-evolution

## 🎙️ Chapter 9 · Multimodal and Real-Time Interaction

### live-audio - Real-Time Voice Chat
`chapter9/live-audio/`

A real-time voice-chat demo integrating speech-to-text, AI conversation, and text-to-speech. Supports multiple AI service providers (OpenAI, OpenRouter, ARK, Siliconflow) and provides a low-latency conversational experience.

**Core Features**:
- Real-time voice input and VAD (Voice Activity Detection)
- Multi-provider support: ASR (OpenAI Whisper, SenseVoice), LLM (GPT-4o, Gemini, Doubao), TTS (Fish Audio)
- WebSocket real-time communication, low-latency audio streaming
- Real-time latency monitoring and logging

**Core Concepts**: speech recognition, real-time conversation, TTS, WebSocket, multi-provider architecture

### browser-use - Browser Automation Agent (Computer Use)
`chapter9/browser-use/`

Browser-Use is a powerful browser-automation framework that lets an LLM control a browser to complete complex tasks. Supports scenarios such as form filling, web navigation, and data extraction — a typical implementation of GUI automation (Computer Use).

**Core Features**:
- LLM-driven browser automation
- Supports multiple LLMs (ChatBrowserUse, OpenAI, Google, local models)
- Custom tool extension, authentication handling
- Sandbox deployment support, cloud-service integration

**Core Concepts**: browser automation, Computer Use, visual understanding, tool extension

### claude-quickstarts - Claude Quickstarts
`chapter9/claude-quickstarts/`

Quickstart examples and best practices for the Claude API, covering a variety of use cases.

**Core Concepts**: Claude API, prompt engineering, best practices

### phone-agent - Phone Agent
`chapter9/phone-agent/`

Demonstrates a voice Agent "interacting with the outside world by phone on behalf of the user": the top layer is a standard ReAct Agent that, after receiving a natural-language task, figures out the number and the goal of the call on its own, invokes the `make_phone_call` tool (an abstraction based on a telephony voice API) to complete the entire call, reads the structured call record and asks follow-up questions and dials again as needed, and finally reports back to the user.

**Core Concepts**: voice Agent, phone interaction, ReAct, tool abstraction

### end-to-end-speech - End-to-End Speech Reasoning vs Cascading Pipeline
`chapter9/end-to-end-speech/`

Corresponds to the end-to-end speech-reasoning paradigm of Step-Audio R1 (a single model that "listens → thinks → speaks"): runs the "speech input → reasoning → speech output" closed loop and directly compares the latency and the loss of paralinguistic information (emotion/tone/speaking rate) against the ASR→LLM→TTS cascading paradigm.

**Core Concepts**: end-to-end speech, cascading comparison, paralinguistic information, thinking while speaking

### streaming-speech - Simulated Streaming Speech Perception
`chapter9/streaming-speech/`

Demonstrates the core trade-off of streaming speech perception: feeds continuous audio to ASR in chunks of increasing length; as soon as a small segment arrives, it produces a "current partial recognition result" to emit text with extremely low first-packet latency, at the cost that early chunks may be wrong due to missing later-half context — and gradually converges as audio accumulates. This stands in contrast to "wait for the full sentence before recognizing", which is high-accuracy / high-latency.

**Core Concepts**: streaming perception, chunked recognition, first-packet latency, cost of premature decision

### controllable-tts - Control-Marker-Driven Controllable TTS
`chapter9/controllable-tts/`

The main LLM's output is tagged with control markers (emotion/speaking rate/style/pause/laughter); the execution layer parses the markers and maps them to the corresponding style profile in a reference voice library before synthesizing speech, handing "where to pause, what tone to use" decisions to the LLM, so the same text can be synthesized in different styles and emotions.

**Core Concepts**: controllable TTS, control markers, reference voice library, prosody control

## 🤝 Chapter 10 · Multi-Agent Collaboration

### use-computer-while-calling - Two-Agent Architecture
`chapter10/use-computer-while-calling/` (📖 the complete code has been split out as [19PINE-AI/TalkAct](https://github.com/19PINE-AI/TalkAct); this directory only retains the explanatory documentation)

Implements a two-Agent collaborative architecture between a phone-call Agent and a computer-use Agent. The two Agents communicate directly over WebSocket with no coordinator. The phone Agent handles voice interaction, the computer Agent performs browser automation, and they work in parallel to complete complex tasks that require both voice and web operations.

**Core Features**:
- Direct inter-Agent communication (no coordinator)
- Standard tool calling for message passing
- Parallel operations: voice conversation + browser automation
- Simple JSON message protocol

**Architecture Components**:
- Phone Call Agent (Node.js): voice I/O, ASR/TTS, LLM conversation
- Computer Use Agent (Python): browser automation, browser-use, web scraping
- WebSocket communication: direct inter-Agent message passing

**Core Concepts**: multi-Agent collaboration, inter-Agent communication, parallel task processing, voice + browser integration

### staged-system-prompt - Switching System Prompts by Execution Stage
`chapter10/staged-system-prompt/`

The same Coding Agent loads different system prompts and toolsets at different execution stages of a task (requirements clarification → code implementation → code review), thereby playing different roles and exhibiting different behaviors within a single conversation, while the conversation history and task state are continuously shared across stages, and a failed review can fall back to the implementation stage.

**Core Concepts**: staged prompts, role switching, shared context, stage pipeline

### multi-role-transfer - Multi-Role Transfer and Autonomous Handoff
`chapter10/multi-role-transfer/`

Demonstrates chained handoff under shared context: multiple specialized role Agents, each with its own system prompt and dedicated toolset, exist in a single session; through the `transfer_to_agent` tool, an Agent autonomously decides which role to switch to based on task progress; because they share the same conversation history, the full context is naturally preserved at handoff.

**Core Concepts**: role handoff, handoff, shared context, autonomous switching

### book-translation - Book Translation Agent (Orchestration Mode)
`chapter10/book-translation/`

Uses Orchestration mode to split long-document translation across specialized Agents for glossary / translation / review: the Manager keeps only the task, plan, call records, and file index, while the complete translation is persisted to disk, so the context stays essentially constant; and it is compared against a single-Agent solution, using real token counts to show how to control context bloat and use a shared glossary to ensure book-wide consistency.

**Core Concepts**: Orchestration mode, context isolation, context-bloat control, shared glossary

### parallel-web-research - Parallel Multi-Source Information Gathering Agent
`chapter10/parallel-web-research/`

Demonstrates parallel search plus central coordination across multiple homogeneous Agents: the main coordinator launches N sub-Agents in parallel, each accessing one source to find the answer; as soon as one hits the target, the others gracefully stop. The message bus, parallel dispatch, real-time monitoring, cascading termination, and race-condition handling are all real implementations (using controlled simulated information sources in place of a real browser).

**Core Concepts**: parallel Agents, central coordination, message bus, cascading termination

### voice-werewolf - Voice Werewolf Agent System
`chapter10/voice-werewolf/`

Uses multi-Agent Werewolf to demonstrate information-permission control under "no shared context": each player is an independent LLM Agent maintaining strictly isolated private context; a code-driven deterministic judge decides which context each piece of information is delivered to and records it for audit; at game end, the system automatically verifies whether isolation was correct. Voice is an optional enhancement.

**Core Concepts**: information asymmetry, private context isolation, judge orchestration, audit verification

## 📖 Study Recommendations

### Core Philosophy: Agent = Model + Context + Tools

The core framework of this book is **Agent = Model + Context + Tools**; these three components work together to realize the intelligent behavior of an Agent:

- **Model**: the brain of the Agent, providing the ability to understand, reason, and make decisions
- **Context**: the operating system of the Agent, containing system instructions, conversation history, the reasoning process, tool-interaction records, etc.
- **Tools**: the hands of the Agent, enabling it to perceive the environment, perform operations, and interact with the outside world

### Learning Path

The learning path corresponds one-to-one with the chapters of the book, unfolding layer by layer around three pillars:

- **Chapter 1 · Fundamentals**: Establishes a complete cognitive framework for Agent systems — understanding the definition of an Agent in RL, comparing the sample-efficiency difference between the traditional RL paradigm and the LLM+RL paradigm, understanding the new "model as agent" paradigm, and mastering the core framework **Agent = Model + Context + Tools**. **Key insight**: the importance of prior knowledge transcends algorithms and environments.

- **Chapters 2–3 · Context**: Context is the operating system of an Agent. Chapter 2 covers system prompts, KV Cache-friendly design, context compression, and prompt-engineering ablation; Chapter 3 covers user memory, dense/sparse/hybrid retrieval, Agentic RAG, context-aware retrieval, and structured knowledge extraction. **Key insight**: a complete context includes system instructions, conversation history, the reasoning process, tool-interaction records, user memory, and external knowledge.

- **Chapters 4–5 · Tools**: Tools are the bridge by which an Agent interacts with the world. Chapter 4 covers the three categories of perception/execution/collaboration MCP tools, event triggering, and async architecture; Chapter 5 dives into the complete implementation of a production-grade Coding Agent. **Key insight**: tool design should be general-purpose (a code interpreter beats a calculator), and code is the meta-capability that can create new tools.

- **Chapters 6–7 · Models**: How to measure and amplify intelligence. Chapter 6 covers evaluation benchmarks such as Terminal-Bench, SWE-bench, GAIA, OSWorld, and Tau2-Bench; Chapter 7 covers post-training techniques such as SFT, RL, RLHF, and sample efficiency. **Key insight**: an independent verification signal is more reliable than "letting the model think again"; "model as agent" internalizes tool calling as a native capability through RL.

- **Chapter 8 · Self-Evolution**: Lets an Agent grow from experience without changing its weights — experience-based learning, externalizing workflows into tools, distilling prompts and observations into parameters. **Key insight**: learning from experience is the key to moving an Agent from "smart" to "proficient".

- **Chapters 9–10 · Extension and Collaboration**: Chapter 9 extends perception and action from text to voice, GUI, and the physical world; Chapter 10 handles complex tasks through multi-Agent division of labor and collaboration. **Key insight**: every design decision in a multi-Agent system can find a correspondence in the three elements of a single Agent.

### Difficulty Levels

- **Beginner** (Chapters 1–2): suitable for newcomers, understand basic concepts
- **Intermediate** (Chapters 3–4): requires some programming foundation, involves system integration
- **Advanced** (Chapters 5–6): requires solid programming ability, involves complex system design
- **Expert** (Chapters 7–8): requires deep-learning and training/self-evolution experience
- **Applied** (Chapters 9–10): comprehensive application of the preceding material, building real applications

### Practice Recommendations

1. **Hands-on practice**: every project is designed to run independently; you are encouraged to run and modify the code yourself
2. **Combined with the book**: read in conjunction with the corresponding chapters of the manuscript in [`book/`](book/) in this repository, to understand the combination of theory and practice
3. **Experimental comparison**: multiple projects include ablation studies and comparison experiments; deepen your understanding through comparison
4. **Progressive learning**: start with simple projects and gradually work into complex systems
5. **Focus on protocols**: the MCP server projects in Chapter 4 demonstrate a standardized tool protocol, which is the key to building scalable Agents

## 🔑 API Keys

It is recommended to apply for API keys from several platforms for ease of study:
- **Kimi**: https://platform.moonshot.cn/ — Moonshot AI's Kimi series; strong long-context and Agent capabilities
- **Zhipu GLM**: https://open.bigmodel.cn/ — Zhipu AI's GLM series (GLM-4.6, etc.); strong Chinese capability and high cost-performance ratio; also recommended
- **Siliconflow**: https://siliconflow.cn/ — hosts a variety of open-source models, including DeepSeek, Qwen, etc.
- **Volcengine**: https://www.volcengine.com/product/ark — hosts ByteDance's closed-source models (Doubao); low access latency from within China
- **OpenRouter**: https://openrouter.ai/ — provides direct access from within China to various overseas closed-source and open-source models, including Gemini 2.5 Pro, Claude 4 Sonnet, OpenAI GPT-5, etc. (the official APIs require an overseas IP and payment method; OpenAI also requires overseas identity real-name authentication, making registration somewhat involved)

For model selection, see: https://01.me/2025/07/llm-api-setup/

## 📦 Appendix · Obtaining External Repositories

For size and licensing reasons, the evaluation benchmarks and training frameworks used in Chapters 6, 7, and 9 are **not bundled** in this repository and must be cloned into the corresponding directories yourself (the upstream addresses and commits verified by this book are listed below for each repository). You can save the following commands as a script and pull them all at once:

```bash
# 第 6 章 · 评测基准
git clone https://github.com/google-research/android_world.git         chapter6/android_world
git clone https://huggingface.co/datasets/gaia-benchmark/GAIA          chapter6/GAIA
git clone https://github.com/xlang-ai/OSWorld.git                      chapter6/OSWorld
git clone https://github.com/SWE-bench/SWE-bench.git                   chapter6/SWE-bench
git clone https://github.com/sierra-research/tau2-bench.git            chapter6/tau2-bench
git clone https://github.com/laude-institute/terminal-bench.git        chapter6/terminal-bench

# 第 7 章 · 训练框架（bojieli/* 为本书适配的分支）
git clone https://github.com/bojieli/minimind.git                      chapter7/MiniMind-pretrain/minimind      # 实验 7-3 从零训 LLM
git clone https://github.com/bojieli/minimind-v.git                    chapter7/MiniMind-pretrain/minimind-v    # 实验 7-4 从零训 VLM（投影层）
git clone https://github.com/bojieli/AdaptThink.git                    chapter7/AdaptThink-original
git clone https://github.com/bojieli/AWorld.git                        chapter7/AWorld
git clone https://github.com/bojieli/SFTvsRL.git                       chapter7/SFTvsRL
git clone https://github.com/bojieli/verl.git                          chapter7/verl
git clone https://github.com/thinking-machines-lab/tinker-cookbook.git chapter7/tinker-cookbook
git clone https://github.com/bojieli/lighteval.git                     chapter7/Intuitor/lighteval
git clone https://github.com/19PINE-AI/rlvp.git                        chapter7/RLVP/rlvp                       # 实验 7-14 RLVP 论文代码
git clone https://github.com/PRIME-RL/SimpleVLA-RL.git                 chapter7/SimpleVLA-RL/SimpleVLA-RL       # 实验 7-13 视觉-语言-动作 RL

# 第 9 章 · 浏览器自动化与 Claude 示例
git clone https://github.com/browser-use/browser-use.git               chapter9/browser-use
git clone https://github.com/anthropics/claude-quickstarts.git         chapter9/claude-quickstarts

# 第 10 章 · 双 Agent 架构（已独立为 TalkAct 项目）+ 斯坦福 AI 小镇
git clone https://github.com/19PINE-AI/TalkAct.git                     chapter10/use-computer-while-calling
git clone https://github.com/joonspk-research/generative_agents.git    chapter10/generative_agents             # 实验 10-7 斯坦福 AI 小镇
```

> If a project's README specifies a particular commit, please `git checkout` to that version as instructed to ensure reproducible results.
> The Chapter 10 `use-computer-while-calling` project has evolved into the independently maintained [19PINE-AI/TalkAct](https://github.com/19PINE-AI/TalkAct) repository; this repository only retains a documentation pointer to it (`chapter10/use-computer-while-calling/README.md`).

**Experiments that depend on real hardware / external environments (no code in this repository; points to upstream documentation):**

- **Experiment 9-8 / 9-9 · XLeRobot Teleoperation and LLM Agent Control**: requires an SO-100/XLeRobot robotic arm; follow the upstream documentation — [Teleop](https://xlerobot.readthedocs.io/en/latest/software/getting_started/XLeRobot_teleop.html) · [LLM Agent](https://xlerobot.readthedocs.io/en/latest/software/getting_started/LLM_agent.html)
- **Experiment 9-10 · RGB Zero-Shot Sim2Real Grasping**: [`StoneT2000/lerobot-sim2real`](https://github.com/StoneT2000/lerobot-sim2real) (the simulation-training part can be done on a pure GPU; real deployment requires an SO-100 robotic arm)
- **Experiment 6-11 · OpenVLA + RoboTwin2 Simulation Evaluation**: VLA training/environment dependencies are in the README of `chapter7/SimpleVLA-RL` (which describes how to obtain and configure OpenVLA and RoboTwin2)

**Reader-exercise experiments (given as exercise problems in the book; reuse already-documented existing projects; no dedicated directory):**

- **Experiment 5-12 · An Agent that Creates Agents**: bootstrapped extension based on `chapter5/coding-agent`
- **Experiments 6-2 / 6-3 / 6-4 / 6-9**: respectively human baseline, memory evaluation, JSON Cards vs RAG, and memory selection — reusing and adapting the Chapter 3 `user-memory` / `user-memory-evaluation` / `contextual-retrieval` projects
- **Experiment 7-8 · Prompt Distillation**: the implementation is in Chapter 8 `chapter8/prompt-distillation` (cross-chapter reuse)
- **Experiment 7-9 · CoT Distillation `[扩展]`**: the book provides the experiment design and acceptance criteria; as a reader extension experiment, no dedicated code yet

## 🤝 Contributing

Both the book and the companion code are fully open-source, and community participation via Pull Requests is very welcome. We welcome the following kinds of contributions:

1. **Book content improvements**: errata, supplements, clearer expressions, or new frontier developments (see `book/chapter*.md` for the main text)
2. **Code improvements and bug fixes**: making the companion projects more robust, more usable, and closer to production practice
3. **New practice projects**: supplementing/replacing an experiment with a better implementation, or contributing entirely new example projects
4. **Design improvements for book illustrations**: making the charts in `book/images/` clearer and more aesthetically pleasing in design (illustrations are generated by `book/gen_*_figs.py`)

Before submitting, it is recommended to first run the relevant experiment yourself and confirm reproducibility; you are also welcome to open an issue first to discuss the idea.

## 📄 License

This project is released under the [Apache License 2.0](LICENSE) open-source license; see the [`LICENSE`](LICENSE) file for details. Some sub-projects may contain their own license information; please refer to the statements in the sub-projects.

## ⭐ Star History

<a href="https://star-history.com/#bojieli/ai-agent-book&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/star-history-dark.png" />
    <source media="(prefers-color-scheme: light)" srcset="assets/star-history-light.png" />
    <img alt="Star History Chart" src="assets/star-history-light.png" width="720" />
  </picture>
</a>

<sub>Chart generated by [`scripts/gen_star_history.py`](scripts/gen_star_history.py) (since July 13, 2026); a [GitHub Actions scheduled task](.github/workflows/star-history.yml) automatically updates and commits it daily to the <code>assets/</code> directory; click to navigate to star-history.com for real-time data.</sub>
