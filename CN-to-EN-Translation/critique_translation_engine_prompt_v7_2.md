# critique_translation_engine_prompt_v7.md
```md
Here is a meticulous, multi-phase plan to review, analyze, and critique the translation from Chinese to English, followed by the actual execution of this evaluation based on the provided documents.

---

# PART 1: The Review Methodology (The Plan)

To ensure a comprehensive and objective critique of the translation quality and fidelity, the review is structured across four specific dimensions:

### Phase 1: Structural & Markdown Integrity Check
*   **Objective:** Ensure no information was lost or added during the translation, and that the formatting (headers, lists, bolding, links, emojis, code blocks) remains perfectly intact.
*   **Method:** A side-by-side structural mapping of the Markdown files, verifying URLs, file paths, and visual hierarchies.

### Phase 2: Technical Terminology & Domain Accuracy
*   **Objective:** Verify that Chinese AI, LLM, and software engineering jargon is accurately localized into standard English industry equivalents.
*   **Method:** Extract key domain terms (e.g., *提示工程*, *人肉*, *脱敏*, *开箱即用*) and evaluate whether their English translations reflect standard GitHub/Developer vernacular rather than literal, machine-like translations.

### Phase 3: Semantic Fidelity & Nuance (The "Meaning" Check)
*   **Objective:** Assess whether the underlying meaning, tone, and contextual nuances of the original author are preserved.
*   **Method:** Analyze complex, multi-clause sentences (especially in the project descriptions) to ensure cause-and-effect relationships and technical processes are conveyed accurately without logical distortion.

### Phase 4: Fluency, Grammar, and Localization (The "Native" Check)
*   **Objective:** Identify any awkward phrasing, "Chinglish," grammatical errors, or residual translation artifacts.
*   **Method:** Read the English text in isolation to check for natural flow, syntax issues, or unnatural verb-noun pairings. 

---

# PART 2: Execution of the Plan (Analysis & Critique)

Based on the methodology above, here is the detailed critique of the translated document.

## 1. Structural & Markdown Integrity
**Score: 9.5 / 10**
*   **Strengths:** The translation perfectly mirrors the original document's structure. Emojis, bullet points, and markdown link formatting `[text](url)` are preserved identically. The structural integrity of tables and bolded text for core concepts (**Core Concepts** / **核心概念**) is pristine.
*   **Flaws/Critique:** 
    *   **Untranslated Code Block Comments:** In the **Appendix** (`## 📦 Appendix · External Repositories Acquisition`), the text within the `bash` code block was **completely skipped** by the translator/translation model. 
        *   *Original:* `# 第 6 章 · 评测基准`
        *   *Translated Output:* `# 第 6 章 · 评测基准` (Failed to translate to `# Chapter 6 · Evaluation Benchmarks`).
        *   *Original:* `# 实验 10-7 斯坦福 AI 小镇`
        *   *Translated Output:* `# 实验 10-7 斯坦福 AI 小镇` 
    *   *Recommendation:* Code block contents, specifically comments, must be parsed and translated in technical documentation.

## 2. Technical Terminology & Domain Accuracy
**Score: 10 / 10**
*   **Strengths:** The translation shines brilliantly in adapting Chinese developer slang and AI terminology into native, standard English developer jargon.
    *   *Original:* "人肉基准" (Literally: "human flesh benchmark") -> *Translation:* "manual benchmark". This is an **outstanding** localization of Chinese internet slang.
    *   *Original:* "开箱即用" -> *Translation:* "out-of-the-box readiness". (Perfect).
    *   *Original:* "脱敏处理" -> *Translation:* "log sanitization". (Excellent industry mapping; much better than "desensitization").
    *   *Original:* "提议者-审核者" -> *Translation:* "Proposer-Reviewer". (Accurately uses standard multi-agent framework terminology).
    *   *Original:* "打断机制" -> *Translation:* "interruption mechanism".
    *   *Original:* "模型后训练" -> *Translation:* "Model Post-Training".

## 3. Semantic Fidelity & Nuance
**Score: 9.5 / 10**
*   **Strengths:** The translation accurately captures the enthusiastic, professional, and structured tone of a high-quality open-source repository. Complex technical pipelines are translated with high fidelity.
    *   *Example of excellence:* "跑通「自下而上因子发现 → 聚类出案件原型 → 对话式建议 Agent」三段流水线" is flawlessly rendered as "run through a three-stage pipeline: 'bottom-up factor discovery → clustering into case prototypes → conversational advisory Agent'". 
    *   *Example of excellence:* "群体的智能可以高于个体" -> "Collective intelligence can surpass individual intelligence." (Captures the philosophical tone perfectly).
*   **Flaws/Critique:**
    *   In Chapter 5, the phrase "and (mocks) integrating with GitHub via MCP to create Issues" is slightly clunky. The original was "并（mock）通过 MCP 对接 GitHub 创建 Issue".
    *   *Recommendation:* A more natural phrasing would be: "...and simulates (mocks) integration with GitHub via MCP to create Issues."

## 4. Fluency, Grammar, and Translation Artifacts
**Score: 8.5 / 10**
*   **Strengths:** The general flow is exceptional. Phrasing like "To avoid information overload upfront..." (免一上来信息过载) demonstrates a deep understanding of natural English phrasing.
*   **Flaws/Critique:** 
    *   **CRITICAL ARTIFACT FOUND:** In the "Reader exercise experiments" section at the end of the document, there is a glaring translation glitch.
        *   *Original:* `落地实现见第 8 章`
        *   *Translated Output:* `Implementation落地 sees Chapter 8`
        *   *Analysis:* The model failed to remove the Chinese characters "落地" (implementation/deployment) and created a grammatically incorrect sentence ("Implementation sees Chapter 8"). It should read: "For implementation, see Chapter 8".
    *   **Minor Syntax Issue:** In the footer (`Star History` section), the translation reads: "...automatically updates and commits to the `assets/` directory daily". The original says "[GitHub Actions 定时任务] 每天自动更新并提交". The English sentence lacks a clear subject for "automatically updates" based on how the previous clause was structured. It should be "...which a GitHub Actions scheduled task automatically updates...".

---

# Final Verdict

**Overall Translation Quality Rating: 9.2 / 10 (Excellent, but requires minor polish)**

**Summary:** 
The translation is of exceptionally high caliber, behaving more like an experienced bilingual software engineer than a machine. It expertly bridges cultural technology gaps (e.g., correctly translating "人肉" to "manual" instead of literal terms). However, it falls slightly short of perfection due to a literal translation artifact (`Implementation落地`) and the failure to process comments nested inside markdown code blocks. 

**Actionable Fixes Required for the Final Version:**
1. Translate the Chinese comments inside the Bash scripts under `## 📦 Appendix · External Repositories Acquisition`.
2. Fix the artifact in the Appendix: change `Implementation落地 sees Chapter 8` to `For the actual implementation, see Chapter 8`.
3. Adjust the grammar slightly in the `log-diagnosis` section to read `simulates (mocks) integration` rather than `(mocks) integrating`.

---

Here is a meticulous review, analysis, and critique of the **Translation Engine v7.0 System Prompt**. 

---

# Executive Summary

**Overall Rating: 9.8 / 10 (Masterclass in Prompt Engineering)**

The provided system prompt is one of the most sophisticated, defensively engineered, and linguistically precise LLM instructions ever crafted for translation tasks. Instead of treating the LLM as a magical black box, it treats the LLM as a **"probabilistic substrate"** and forces it to emulate a deterministic state machine. 

This prompt single-handedly explains the exceptionally high quality observed in the previous translation. However, cross-referencing the prompt with the translation output also reveals exactly *why* the few minor errors occurred, exposing slight blind spots in its otherwise ironclad audit rules.

Here is the detailed breakdown of the prompt's effectiveness, its architectural brilliance, and the specific gaps that caused the anomalies noted in the first review.

---

# 1. Architectural Strengths (Why the output was so good)

### A. The "Probabilistic Substrate" Acknowledgment (§2)
Most translation prompts say, "Do not make mistakes." This prompt acknowledges that LLMs are next-token predictors and forces deterministic behavior via a **6-Phase Chain-of-Thought (CoT) Scratchpad (§4 & §11)**. By forcing the LLM to write out its topological mapping, modal deconstruction, and typological compilation *before* outputting the payload, it effectively zeroes out hallucination. 

### B. Epistemic Isomorphism & Modal Anchoring (§8.2)
The mandate to "perfectly mirror the author's cognitive modality" is a massive differentiator. In technical and legal translation, replacing "might" with "will" is a catastrophic failure. By hardcoding matrices for RFC 2119 markers (`MUST`, `SHOULD`) and legal markers (`allegedly` -> `涉嫌`), the prompt forces the engine to behave like a forensic linguist rather than a casual bilingual assistant.

### C. Anti-Translationese & Functional Equivalence (§8.3 & §8.4)
This is why the translation of Chinese developer slang ("人肉基准", "脱敏处理") was flawlessly rendered into standard English developer jargon ("manual benchmark", "log sanitization"). The prompt explicitly forbids literal word-for-word mapping and commands the engine to "discard the syntactic shell of the source language."

### D. Targeted Repair Blocks (§11.5)
This v7 addition is a brilliant workaround for LLM context-window exhaustion. By forcing the model to only output *failed Information Units (IUs)* during its self-audit loop rather than rewriting the entire 3,000-word draft, it saves tokens and maintains laser-sharp focus on the actual errors.

---

# 2. Solving the Mysteries of the Translation (Prompt vs. Output)

By cross-referencing this system prompt with the translation anomalies found in the previous review, we can deduce exactly what happened.

### Mystery 1: Why were the Code Block Comments left in Chinese?
*   **The Observation:** In the previous review, I penalized the translation for leaving comments like `# 第 6 章 · 评测基准` inside bash blocks completely untranslated.
*   **The Cause:** **This was NOT a model failure; it was perfect prompt adherence.** 
*   **The Proof:** In **§11 (Phase 1)**, the prompt explicitly states: *"Identify code comments and apply the comment policy (**default: preserve verbatim**; `--translate-comments`: translate)."* Because the user/wrapper in our test scenario did not pass the `--translate-comments` mode flag, the engine correctly locked the code block content as immutable and refused to translate the comments. 
*   **Verdict:** The prompt worked exactly as designed.

### Mystery 2: The "Implementation落地" Glitch
*   **The Observation:** In the previous review, the model output a bizarre artifact: `Implementation落地 sees Chapter 8` instead of `For implementation, see Chapter 8`.
*   **The Cause:** Probabilistic drift slipping through a gap in the Phase 6 Self-Test. 
*   **The Proof:** In **§8.3**, the prompt explicitly commands mapping `落地` to `implement / deploy`. The engine tried to do this but glitched, concatenating the English and Chinese words. While **§11 Phase 6 (Locked-retention exemption)** states that "Unexplained English words in Chinese-dominant text (or vice versa)" should trigger a repair, this check is notoriously hard for models to self-diagnose because the model sees `落地` as a valid token that it just processed. The Self-Test rules are highly aggressive against straight quotes in Chinese text (§9.3), but lack an explicit, aggressive check for *source-language leakage* in target-language prose.

---

# 3. Vulnerabilities & Areas for Improvement (The Critique)

Despite its brilliance, the v7 prompt has a few operational vulnerabilities that could be patched in a "v8" update.

### Vulnerability A: Asymmetric Typography/Artifact Checks (§9.3 & Phase 6)
The prompt is heavily optimized to prevent English typographic pollution in Chinese text. For example, Phase 6 demands a hard failure if straight ASCII quotes (`"`) appear in Chinese text. 
*   **The Fix:** It lacks a symmetrical hard check for Chinese typographic pollution in English text. Phase 6 should include a specific check: **"Source-Script Leakage Check: [PASS/FAIL] — confirm no stray CJK characters (汉字) remain in English-dominant translated prose unless strictly protected by Entity Anchoring (§8.1)."** This would have caught the `Implementation落地` artifact and triggered a Phase 4 Repair Block.

### Vulnerability B: Instruction Quarantine vs. Edge Cases (§6 Axiom 4)
The instruction quarantine is excellent for preventing prompt injection, but it assumes the LLM can always flawlessly distinguish between "payload data" and "system instructions". Because the prompt itself is extraordinarily long, highly complex markdown payloads (like the source file we tested, which is full of metadata, tables, and code formatting) can occasionally cause the LLM's attention heads to blur the line between the system prompt's markdown formatting rules and the payload's markdown content.

### Vulnerability C: The "Notice Channel" Deadlock Exception (§1 & §15.5)
The prompt attempts to resolve a deadlock where the LLM is told "always translate" but also told "stop and emit a notice if out-of-scope". While the prompt logically resolves this (Notice Channel engages the Primary Directive Exception), in practice, LLMs struggle with "if/then" contradictions separated by 10 pages of tokens. 
*   **The Fix:** Move the Notice Channel conditions directly into the Primary Directive block (§1) rather than placing them at the end of the prompt in §15.5. LLMs anchor heavily on the first 500 tokens of a prompt.

---

# Final Verdict

The **Translation Engine v7.0** system prompt is a masterpiece of deterministic constraint engineering. It effectively overrides the typical "helpful, conversational" fine-tuning of modern LLMs, violently forcing them into the role of a meticulous, zero-trust parser. 

It succeeds wildly at structural preservation and tone matching. The only flaw identified in the translation output (the untranslated code comments) was actually proof of the prompt's rigid success, while the single actual error (the "落地" artifact) reveals a tiny gap in the Phase 6 audit checks that can be easily remedied with a targeted leakage rule.

```

# source_file_to_translate-5.md
```md
# 深入理解 AI Agent：设计原理与工程实践

**[English](README.en.md) | 中文**

本仓库是《深入理解 AI Agent：设计原理与工程实践》一书的开源主仓库，包含**全书正文**与**配套示例代码**。全书正文、配图与配套实验代码全部开源，欢迎把实验亲手跑一遍、提 issue 和 PR。

## 📖 电子书

全书提供中英双语版本：

- **中文 PDF（原版）**：[`book/深入理解-AI-Agent-李博杰-v1.1.pdf`](book/深入理解-AI-Agent-李博杰-v1.1.pdf)
- **英文 PDF**（社区贡献翻译，by [@nsdevaraj](https://github.com/nsdevaraj)）：[`book-en/AI-Agents-in-Depth-Bojie-Li-v1.1.pdf`](book-en/AI-Agents-in-Depth-Bojie-Li-v1.1.pdf)
- **泰米尔语 PDF**（社区贡献翻译，by [@nsdevaraj](https://github.com/nsdevaraj)）：[`book-ta/AI-Agents-in-Depth-Bojie-Li-v1.1-ta.pdf`](book-ta/AI-Agents-in-Depth-Bojie-Li-v1.1-ta.pdf)

中文正文与编译好的 PDF 位于 [`book/`](book/) 目录；英文与泰米尔语翻译为**社区贡献**，分别位于 [`book-en/`](book-en/) 与 [`book-ta/`](book-ta/) 目录，内容可能滞后于中文原版：

- **正文源码**：`book/introduction.md`（引言）、`book/chapter1.md` ~ `book/chapter10.md`（第一至第十章）、`book/afterword.md`（后记）
- **自行编译**：安装 pandoc、xelatex、ElegantBook 文档类与相关字体后，运行

  ```bash
  cd book && bash build_pdf.sh
  ```

  图表由 `book/gen_*_figs.py` 生成、存于 `book/images/`，排版细节见 `book/preamble.tex` 与 `book/*.lua`。

## 📑 内容速览（第 1–10 章）

全书围绕核心公式 **Agent = LLM + 上下文 + 工具** 展开，十章内容如下：

- **第 1 章 · Agent 基础知识**：从“模型即 Agent”的新范式出发，建立 **Agent = LLM + 上下文 + 工具** 的核心公式，并引入 Harness 工程——模型之外的一切工程能力，才是真正的竞争力所在。
- **第 2 章 · 上下文工程**：上下文决定 Agent 的能力上限。深入大模型 API 的上下文结构、KV Cache 友好设计、提示工程、动态提示词与 Agent Skills、状态栏元信息，以及上下文压缩策略。
- **第 3 章 · 用户记忆和知识库**：让 Agent 跨会话记住用户、并接入外部知识。涵盖用户记忆系统、RAG 基础管道，以及超越扁平文本的知识组织与检索（结构化索引、知识图谱等）。
- **第 4 章 · 工具**：工具是 Agent 的双手。讲工具分类与通用设计原则、MCP 协议与工具选择的挑战、感知/执行/协作三类工具，以及事件驱动的异步 Agent。
- **第 5 章 · Coding Agent 与代码生成**：代码是“能创造新工具的工具”，是通用 Agent 的元能力。以生产级 Coding Agent 为例，展示这一最强通用工具的完整实现。
- **第 6 章 · Agent 的评估**：把 Agent 的表现变成可比较的信号。从评估环境、数据集设计、指标体系，到统计显著性、可观测性、评估驱动选型，直至生产级内部评估与仿真环境。
- **第 7 章 · 模型后训练**：预训练、SFT、RL 三阶段全景。何时选 SFT、何时选 RL，RLHF、算法比较、数据与环境，以及让模型学会工具调用、提升样本效率的前沿探索。
- **第 8 章 · Agent 的自我进化**：不改权重也能成长。三种学习范式，从经验中学习、主动工具发现，到“从工具使用者到工具创造者”，让 Agent 从“聪明”走向“熟练”。
- **第 9 章 · 多模态与实时交互**：把感知与行动从文本扩展到语音、GUI 与物理世界。语音三范式（级联/端到端全模态/全双工）、流式语音感知与合成、Computer Use 与机器人操作。
- **第 10 章 · 多 Agent 协作**：群体的智能可以高于个体。多 Agent 分类框架、何时真正优于单 Agent、共享与不共享上下文的协作、失败模式，以及涌现的“Agent 社会”。

## 💻 配套代码

所有项目按**章节**组织，与全书十章一一对应，涵盖从基础概念到高级技术的完整学习路径，目录为 `chapterN/项目名/`。第 5、8、9、10 章的绝大多数实验现均提供可独立运行的配套 demo，并已对接真实 LLM API 验证跑通。

### 项目类型说明

配套项目分为三类，请对照下方图标了解每个项目“开箱即用”的程度：

- ✅ **可独立运行**：本仓库自带完整代码，配置好 API Key（见文末）即可运行。
- 📖 **复现指南**：项目本身是一份详细的复现文档，依赖需自行 `git clone` 的**外部仓库**（训练框架、评测基准等），见下方《外部仓库获取》。
- 🚧 **设计文档**：目前仅包含架构与实现方案的设计文档，可运行代码仍在完善中。

下列项目**不是**✅ 可独立运行，克隆本仓库时请留意：

| 项目 | 类型 | 说明 |
| --- | --- | --- |
| `chapter7/AdaptThink` · `AWorld-train` · `MiniMind-pretrain` · `retool` · `SpatialReasoning` | 📖 复现指南 | 训练类实验，依赖外部框架，按 README 复现 |
| 第 6 章全部基准 · 第 7 章多数训练框架 · 第 9 章 `browser-use`/`claude-quickstarts` · 第 10 章 `use-computer-while-calling` | 📖 复现指南 | 依赖外部仓库，见《外部仓库获取》 |

### 外部仓库获取（简要）

第 6、7、9、10 章的**部分**实验依赖评测基准、训练框架、机器人平台等**外部仓库**（出于体积与版权未内置本仓库）。为免一上来信息过载，**完整的克隆命令、上游地址与本书验证过的提交，见文末《附录 · 外部仓库获取》**。建议先从前面各章可独立运行的项目上手，需要复现训练 / 评测 / 机器人类实验时，再按文末指引快速获取。

## 🚀 第 1 章 · Agent 基础知识

### learning-from-experience - 强化学习 vs LLM 对比
`chapter1/learning-from-experience/`

对比传统强化学习（Q-learning）与基于 LLM 的上下文学习，复现 Shunyu Yao 的 “The Second Half” 博文中的关键洞察。通过寻宝游戏展示 LLM 如何以 250-400 倍的样本效率超越传统 RL。

**核心概念**：强化学习、上下文学习、样本效率、先验知识

### web-search-agent - Kimi K2 模型即 Agent
`chapter1/web-search-agent/`

实现具备基础深度搜索能力的 Agent，能够进行多轮搜索和信息整合。

**核心概念**：网络搜索、模型原生 Agent

### search-codegen - GPT-5 原生工具集成
`chapter1/search-codegen/`

构建能够基础深度搜索能力和代码沙盒能力的 Agent，综合利用网络搜索、代码执行等工具实现复杂分析。

**核心概念**：网络搜索、代码生成、模型原生 Agent

### context - 上下文消融研究
`chapter1/context/`

通过系统性的消融实验展示 Agent 上下文各个组件的重要性。支持多种 LLM 提供商（SiliconFlow Qwen、字节 Doubao、月之暗面 Kimi），配置不同的上下文模式观察 Agent 行为变化。

**核心概念**：上下文管理、工具调用、ReAct 循环、消融研究

## 🎯 第 2 章 · 上下文工程

### local_llm_serving - 本地 LLM 部署与工具调用
`chapter2/local_llm_serving/`

跨平台的本地 LLM 部署方案，自动选择最佳后端（vLLM 或 Ollama）。展示即使 0.6B 的小模型也能通过良好的系统设计实现出色的工具调用能力。支持流式响应，实时显示思考过程。

**核心概念**：模型部署、Chat Template、流式处理、工具调用

### attention_visualization - 注意力机制可视化
`chapter2/attention_visualization/`

可视化 LLM 的完整输入输出 token 序列和注意力权重分布，深入理解模型如何处理上下文、进行推理和调用工具。

**核心概念**：注意力机制、token 分析、推理过程可视化

### kv-cache - KV Cache 友好的上下文设计
`chapter2/kv-cache/`

探索不同上下文管理模式对 KV Cache 的影响，演示常见的错误模式如何破坏缓存效率。通过实验展示正确的上下文设计如何显著降低延迟和成本。

**核心概念**：KV Cache、上下文优化、性能调优

### context-compression - 上下文压缩策略
`chapter2/context-compression/`

实现并对比多种上下文压缩策略，包括摘要、关键信息提取、语义压缩等。在保持 Agent 能力的同时减少 token 使用量。

**核心概念**：上下文压缩、token 优化、信息密度

### prompt-engineering - 提示工程消融研究
`chapter2/prompt-engineering/`

扩展 Tau-Bench 框架，通过系统性的消融实验量化不同提示工程因素对 Agent 性能的影响。展示语气风格、指令组织、工具描述等因素如何影响任务完成率。

**核心概念**：提示工程、消融研究、性能基准测试

### system-hint - 系统提示优化
`chapter2/system-hint/`

研究系统提示（System Hint）对 Agent 行为的影响，探索如何通过优化系统提示提升性能。

**核心概念**：系统提示、行为引导、提示优化

### log-sanitization - 日志脱敏处理
`chapter2/log-sanitization/`

实现智能的日志脱敏系统，在保留调试信息的同时保护敏感数据。

**核心概念**：隐私保护、日志处理、数据安全

### prompt-injection - 提示注入攻防实验
`chapter2/prompt-injection/`

构造 3 种攻击场景（直接注入、间接注入、记忆注入）× 4 种防御配置（无防御、提示词加固、来源标记、组合防御）的对照实验，用确定性规则统计攻击成功率，直观展示逐层叠加防御后注入成功率如何显著下降。

**核心概念**：提示注入、间接注入、数据与指令分离、运行时校验

### agent-skills-ppt - Agent Skills 渐进式披露生成 PPT
`chapter2/agent-skills-ppt/`

复现 Agent Skills 的「渐进式披露」思想：Agent 启动时只看到一份薄 Skill 目录，识别出任务需要 `pptx` Skill 后才逐层加载其完整流程、细则文档与捆绑脚本，最终用 python-pptx 生成真实的 `.pptx` 文件。

**核心概念**：Agent Skills、渐进式披露、按需加载、工具编排

## 📚 第 3 章 · 用户记忆和知识库

### user-memory - 用户记忆系统
`chapter3/user-memory/`

构建长期用户记忆系统，让 Agent 能够记住用户偏好和历史交互，提供个性化服务。

**核心概念**：长期记忆、个性化、用户建模

### mem0 / memobase - 开源记忆框架对照
`chapter3/mem0/` 和 `chapter3/memobase/`

用 mem0、Memobase 两个开源记忆框架各自实现一版用户记忆，作为实验 3-2「记忆策略对比」的对照实现，便于横向比较不同记忆方案的抽取形态与回答质量。

**核心概念**：记忆框架、mem0、Memobase、方案对比

### user-memory-evaluation - 用户记忆评估框架
`chapter3/user-memory-evaluation/`

系统化评估用户记忆系统的准确性、相关性和有效性，包含多种测试场景和评估指标。

**核心概念**：评估框架、测试用例、性能度量

### dense-embedding - 稠密嵌入向量检索服务
`chapter3/dense-embedding/`

构建向量相似性搜索服务，对比研究 ANNOY（基于树）和 HNSW（基于图）两种近似最近邻索引算法。展示不同索引策略在性能、内存占用和更新能力上的权衡。

**核心概念**：稠密嵌入、向量检索、ANN 算法、语义搜索

### sparse-embedding - 稀疏检索引擎
`chapter3/sparse-embedding/`

从零实现基于 BM25 算法的稀疏向量搜索引擎，通过丰富的日志和可视化接口展示搜索引擎的内部工作机制，理解词频权重计算和倒排索引原理。

**核心概念**：稀疏嵌入、BM25、TF-IDF、精确匹配

### retrieval-pipeline - 混合检索流水线
`chapter3/retrieval-pipeline/`

构建完整的检索流水线，结合稠密检索、稀疏检索和神经重排序。通过精心设计的测试用例，系统性展示混合检索在不同场景下的优势互补效果。

**核心概念**：混合检索、神经重排序、跨编码器、检索融合

### multimodal-agent - 多模态信息提取
`chapter3/multimodal-agent/`

对比三种多模态处理策略：原生多模态处理、提取为文本、工具化分析。通过统一框架下的消融研究，揭示不同技术路径在保真度、成本和灵活性上的权衡。

**核心概念**：多模态、视觉理解、OCR、端到端处理

### structured-index - 结构化索引
`chapter3/structured-index/`

实现并对比 RAPTOR（递归抽象树）和 GraphRAG（知识图谱）两种先进索引策略。通过索引技术手册演示如何构建反映知识内在层次和关联的结构化索引。

**核心概念**：RAPTOR、GraphRAG、层次摘要、知识图谱

### agentic-rag - 智能体 RAG
`chapter3/agentic-rag/`

对比传统 Non-Agentic RAG 与 Agentic RAG 的性能差异。展示 Agent 如何通过 ReAct 模式主导迭代式信息检索，在处理复杂司法问答时显著提升答案质量。

**核心概念**：Agentic RAG、ReAct 循环、迭代检索、主动探索

### agentic-rag-for-user-memory - 利用 Agentic RAG 构建用户记忆
`chapter3/agentic-rag-for-user-memory/`

将 Agentic RAG 框架应用于管理用户对话历史，通过多轮迭代搜索能力处理跨会话的记忆检索，实现基础回忆和多会话检索能力。

**核心概念**：用户记忆、对话历史索引、跨会话检索

### contextual-retrieval - 上下文感知检索
`chapter3/contextual-retrieval/`

实现 Anthropic 提出的上下文感知检索技术，通过为文本块生成包含核心上下文的前缀摘要，解决传统分块方法的上下文丢失问题，将检索失败率降低 49-67%。

**核心概念**：上下文增强、前缀生成、语义锚定、检索优化

### contextual-retrieval-for-user-memory - 上下文感知的用户记忆系统
`chapter3/contextual-retrieval-for-user-memory/`

将上下文感知检索技术应用于用户记忆构建，结合 Advanced JSON Cards 与上下文感知 RAG，形成双层记忆结构，实现更高层次的主动服务能力。

**核心概念**：双层记忆、结构化事实、上下文检索、主动服务

### structured-knowledge-extraction - 结构化知识提取
`chapter3/structured-knowledge-extraction/`

以司法判例为例跑通「自下而上因子发现 → 聚类出案件原型 → 对话式建议 Agent」三段流水线：不预设僵化字段，由 LLM 从大量案例中自主发现因子并归纳为模块化 schema（核心因子 + 罪名扩展因子）；再将案件聚类为若干原型、算出各原型的因子重要性；Agent 对新案情匹配最相似原型、按重要性追问缺失信息并给出有依据的建议（附法律免责声明）。

**核心概念**：自下而上知识发现、模块化因子、聚类原型、可解释决策

## 🛠️ 第 4 章 · 工具

### perception-tools - 感知工具 MCP 服务器
`chapter4/perception-tools/`

构建全面的感知工具集，提供网络搜索、多模态理解、文件系统操作和公共数据源访问能力。大部分功能基于免费开放 API（DuckDuckGo、Open-Meteo、Yahoo Finance、OpenStreetMap 等），无需 API 密钥即可使用。

**核心概念**：MCP 协议、多模态解析、公共数据源、文档理解、地理信息服务

### execution-tools - 执行工具 MCP 服务器
`chapter4/execution-tools/`

实现具备安全机制的执行工具集，包括文件操作、代码解释器、虚拟终端和外部系统集成。通过 LLM 二次审批机制防止危险操作，自动摘要复杂输出，并对代码进行语法验证。

**核心概念**：MCP 协议、执行安全、LLM 审批、结果摘要、自动验证

### collaboration-tools - 协作工具 MCP 服务器
`chapter4/collaboration-tools/`

提供全面的协作能力，包括浏览器自动化（browser-use 框架）、人机协同（Human-in-the-Loop）、多渠道通知（Email、Telegram、Slack、Discord）和定时器管理。支持敏感操作的管理员审批和定时任务调度。

**核心概念**：MCP 协议、浏览器自动化、HITL 模式、多渠道通知、定时任务

### agent-with-event-trigger - 事件触发型 Agent 与 MCP 集成
`chapter4/agent-with-event-trigger/`

基于 FastAPI 构建的现代化事件驱动 Agent，默认集成前三个 MCP 服务器的所有工具。采用原生异步架构实现清晰的 MCP 工具加载，通过 HTTP API 接收多源事件（Web、即时消息、GitHub、定时器等）。提供自动 API 文档（Swagger UI）和后台监控能力。

**核心概念**：FastAPI、原生异步、MCP 集成、事件驱动、自动 API 文档、工具编排

### active-tool-selection - 主动工具选择
`chapter4/active-tool-selection/`

实现智能工具选择机制，让 Agent 能够根据任务需求主动选择最合适的工具组合，而非被动接受预定义的工具集。

**核心概念**：工具选择、动态工具加载、任务分析

### async-agent - 带并行执行和打断能力的异步 Agent
`chapter4/async-agent/`

基于 asyncio 单线程实现事件驱动异步 Agent 框架（Flux）的核心：inbox 事件队列按紧急度分派（打断/立即/排队），支持异步工具并行执行、运行中打断当前 turn、并对模拟的长任务做取消与状态查询。决策由真实 LLM（function calling）完成。

**核心概念**：异步编程、事件队列、打断机制、并行工具取消、非阻塞 I/O

> 此外，`chapter4/docker-compose.yml` 与 `chapter4/DOCKER_DEPLOYMENT.md` 提供了将上述 MCP 工具服务器容器化部署的参考方案。

## 💻 第 5 章 · Coding Agent 与代码生成

### coding-agent - 生产级 Coding Agent
`chapter5/coding-agent/`

基于 Claude 构建的生产级 AI 编码助手，采用纯 Python 实现所有工具，无需命令行依赖。包含 17 个完整实现的工具，涵盖文件操作、搜索、Shell 操作和项目管理。特别实现了纯 Python 的 Grep 工具，完全兼容 ripgrep 的功能。

**核心特性**：
- 纯 Python 实现，无命令行依赖，特别适合 Mac 用户
- 完整的工具套件：文件读写编辑、纯 Python 正则搜索、目录列表、Shell 会话管理
- 系统提示技术：时间戳、工具调用计数、TODO 列表管理、详细错误信息
- 持久化 Shell 环境、自动 Lint 检测、流式响应支持
- 支持多个 LLM 提供商（Anthropic、OpenAI、OpenRouter）

**核心概念**：代码生成、文件编辑、纯 Python 工具、系统提示、Lint 检测、多提供商支持

### code-for-math - 用代码提升数学解题能力
`chapter5/code-for-math/`

让同一模型在同一组竞赛数学题上对比「纯思维链」与「代码辅助」两种模式：后者把题目形式化为 Python（sympy/numpy/scipy），通过 function calling 在子进程沙箱执行，用精确计算替代易错的心算，准确率显著更高。

**核心概念**：代码解释器、符号计算、思维链对比、工具增强推理

### code-for-logic - 用代码提升逻辑思考能力
`chapter5/code-for-logic/`

把「骑士与无赖」逻辑谜题转化为约束满足问题（CSP）：Agent 用 `python-constraint` 定义变量与双条件约束并调用求解器，对比纯自然语言推理与代码辅助两种模式在一组 K&K 谜题上的正确率。

**核心概念**：约束求解、CSP 建模、形式化推理、代码辅助

### small-model-codified-rules - 小模型代码化规则
`chapter5/small-model-codified-rules/`

基于 τ-bench 航空客服场景的对照实验：把复杂业务政策（退款规则）从自然语言提示词搬进代码/工具后，小模型的任务成功率与政策一致性大幅提升，工具内代码校验能实时拦截模型的错误认知。

**核心概念**：代码化业务规则、政策执行、工具内校验、小模型可靠性

### paper-to-ppt - 论文自动生成 PPT（提议者-审核者）
`chapter5/paper-to-ppt/`

把「做 PPT」重构为代码生成问题：Proposer 编写 Slidev（Markdown+HTML）代码，Reviewer 把每页真正渲染成 PNG 并用 Vision LLM 检查排版问题，据结构化反馈迭代修订；双 Agent 分工使上下文峰值显著更小。

**核心概念**：代码生成、Slidev、提议者-审核者、视觉质量控制

### paper-to-video - 论文讲解视频自动生成
`chapter5/paper-to-video/`

在「论文 → PPT」基础上为每页幻灯片生成口语化讲解词，调用 TTS 合成语音，再用 ffmpeg 把每页截图与其音频逐页同步合成为一段带旁白的讲解视频。

**核心概念**：多媒体生成、讲解词生成、TTS、ffmpeg 音画同步

### video-edit - 基于 API 的智能视频剪辑
`chapter5/video-edit/`

用户给一段多场景视频 + 一句自然语言需求，Agent 通过「两步 Vision 定位」（先粗后细抽帧读图）确定目标场景时间边界，剪出片段后由 Reviewer 抽取成片关键帧核对，不合格则迭代。

**核心概念**：视频剪辑、Vision 定位、由粗到细、提议者-审核者

### adaptive-log-parser - 自适应日志解析系统
`chapter5/adaptive-log-parser/`

一个能自我进化的日志解析系统：遇到无法解析的新格式时不报错，而是把失败样本与报错交给代码生成 Agent 生成 `parse` 函数，自动测试通过后热更新注册进解析引擎，全流程无需人工介入。

**核心概念**：代码作为系统适配器、自愈闭环、代码热更新、自动测试

### log-diagnosis - 生产日志智能诊断系统
`chapter5/log-diagnosis/`

诊断 Agent 读取生产轨迹日志、架构文档与 PRD，自动定位问题与根因、生成结构化报告与回归测试用例，用重放框架真正执行验证，并（mock）通过 MCP 对接 GitHub 创建 Issue。

**核心概念**：轨迹诊断、根因定位、回归测试生成、重放验证

### dynamic-form - 动态表单意图澄清系统
`chapter5/dynamic-form/`

面对信息不完整的请求时，Agent 不逐条追问，而是动态生成一个含级联逻辑的自包含 HTML 表单让用户一次性补全；前端把表单汇总为 JSON 交回 Agent 继续任务。

**核心概念**：代码生成、意图澄清、动态表单、级联逻辑

### erp-agent - 自然语言 ERP Agent（NL → SQL）
`chapter5/erp-agent/`

把中文自然语言查询转成 SQL 交由数据库执行、直接呈现结果表，核心是 artifact（制品）模式：LLM 只生成 SQL 制品、不亲自搬运数据，既省 token 又避免手算出错，几万行结果也能秒回。

**核心概念**：NL2SQL、artifact 模式、数据库执行、成本与准确性

### conversational-ui - 对话式界面定制系统
`chapter5/conversational-ui/`

用户用自然语言提出 UI 定制需求（颜色/字体/文案/布局），Agent 自主定位并修改 React 前端源码，借助 Vite 热加载（HMR）让改动即时生效，支持多轮迭代定制。

**核心概念**：代码修改、前端定制、热加载、多轮迭代

## 🎯 第 6 章 · Agent 的评估

### terminal-bench - 终端环境基准测试
`chapter6/terminal-bench/`

Terminal-Bench 是测试 AI Agent 在真实终端环境中表现的基准测试。从编译代码到训练模型、设置服务器，评估 Agent 如何处理真实的端到端任务。包含约 100 个任务的数据集和执行框架，支持多种 Agent 实现。

**核心概念**：终端自动化、任务评估、Docker 沙箱、基准测试

### SWE-bench - 软件工程基准测试
`chapter6/SWE-bench/`

SWE-bench 是评估大语言模型解决真实 GitHub 问题能力的基准测试。给定代码库和问题描述，模型需要生成能够解决问题的补丁。包含 SWE-bench、SWE-bench Lite、SWE-bench Verified 和 SWE-bench Multimodal 多个版本。

**核心概念**：代码修复、GitHub 问题、补丁生成、Docker 评估

### GAIA - 通用 AI 助手基准测试
`chapter6/GAIA/`

GAIA 旨在评估下一代 LLM（具有工具增强、高效提示、搜索访问等能力的 LLM）。包含 450+ 个需要不同程度工具和自主性的非平凡问题，答案明确无歧义。分为 3 个难度级别。

**核心概念**：工具使用、多步推理、自主性评估

### OSWorld - 操作系统级 Agent 基准
`chapter6/OSWorld/`

评估 Agent 在完整操作系统环境中执行复杂任务的能力，包括文件管理、应用程序操作和系统配置。

**核心概念**：操作系统自动化、多应用协作、系统级任务

### android_world - Android 环境基准
`chapter6/android_world/`（📖 外部仓库，见《外部仓库获取》）

评估 Agent 在 Android 移动环境中的表现，包括应用导航、UI 交互和任务完成能力。

**核心概念**：移动自动化、Android UI、应用交互

> `chapter6/android-world/`（连字符命名）并非基准代码，而是本书对 T3A Agent 在 android_world 上失败案例的分析笔记（`t3a*.md`），可作为阅读材料参考。

### tau2-bench - 工具增强推理基准
`chapter6/tau2-bench/`

专注于评估 Agent 使用工具进行复杂推理的能力，包括计算、搜索和数据处理等场景。

**核心概念**：工具增强推理、多步骤任务、工具组合

### elo-leaderboard - ELO 排行榜系统
`chapter6/elo-leaderboard/`

实现基于 ELO 评分系统的 Agent 性能排行榜，通过对战比较来评估不同 Agent 的相对能力。

**核心概念**：ELO 评分、相对评估、排行榜系统

### model-benchmark - 多维度模型性能基准测试
`chapter6/model-benchmark/`

对多个 OpenAI 兼容的 LLM API 提供商做横向基准测试，用流式接口精确测量首 token 延迟（TTFT），在并发下测出端到端延迟分位数（p50/p95）、吞吐与成功率，一条命令跑出多维度对比表，说明选型是多维权衡而非只看排行榜。

**核心概念**：TTFT、延迟分位数、吞吐、并发压测、模型选型

### agent-cost-analysis - Agent 任务端到端成本分析
`chapter6/agent-cost-analysis/`

对典型多轮 Agent 任务（客服退款）做全链路成本拆解：用自建轻量 tracing 记录每次 LLM 调用的输入/输出/缓存 token、时延与成本，聚合出「哪一步最贵」，再用 A/B 量化 KV-cache 友好设计 + 上下文压缩带来的真实节省。

**核心概念**：可观测性、成本拆解、prompt caching、A/B 对比

### tts-quality-eval - 全自动 TTS 质量评估流水线
`chapter6/tts-quality-eval/`

用多种 TTS 配置（不同 model/voice/speed）合成同一组挑战性文本，再以多模态 LLM-as-a-Judge 按 Rubric 逐维度（清晰度/自然度等）打分，汇总成可复现的配置对比表。

**核心概念**：LLM-as-a-Judge、Rubric 评分、TTS 评估、多维对比

## 🧠 第 7 章 · 模型后训练

本章包含多个模型后训练项目，涵盖监督微调（SFT）和强化学习（RL）的各种技术和应用场景。

### AdaptThink - 自适应推理深度
`chapter7/AdaptThink/` 和 `chapter7/AdaptThink-original/`

让推理模型学会根据问题难度自适应选择推理模式（Thinking vs NoThinking）。通过约束优化和重要性采样，在大幅降低推理成本（45-69%）的同时提升准确率。基于 DeepSeek-R1-Distill-Qwen 模型，使用 DAPO 算法训练。

**核心概念**：自适应推理、推理成本优化、约束优化、重要性采样

### retool - 工具增强数学推理
`chapter7/retool/`

使用多轮对话和代码沙箱提升大语言模型数学推理能力。通过 SFT 和 RL 两阶段训练，让模型学会使用代码执行环境辅助数学问题求解。基于 Qwen2.5-32B-Instruct，在 AIME 2024 数据集上训练，使用 DAPO 算法和 SandboxFusion 沙箱。

**核心概念**：工具使用、代码执行、数学推理、多轮对话、DAPO 算法

### AWorld / AWorld-train - 具身 Agent 训练
`chapter7/AWorld/` 和 `chapter7/AWorld-train/`

基于 AWorld 框架训练具身 Agent，让 Agent 能够在虚拟环境中执行复杂任务并从经验中学习。

**核心概念**：具身智能、环境交互、经验学习

### SFTvsRL - SFT 与 RL 对比研究
`chapter7/SFTvsRL/`

系统性对比监督微调（SFT）和强化学习（RL）在不同任务上的效果，分析两种方法的优劣和适用场景。

**核心概念**：SFT vs RL、训练方法对比、性能分析

### verl - 高效 RL 训练框架
`chapter7/verl/`

verl 是专门为大语言模型 RLHF 训练设计的高效强化学习框架，支持 PPO、GRPO、DAPO 等多种算法。

**核心概念**：RLHF、PPO、分布式训练、高效优化

### Intuitor - 直觉推理训练
`chapter7/Intuitor/`

训练模型的直觉推理能力，让模型能够快速做出合理判断而不需要详细的思考链。

**核心概念**：直觉推理、快速决策、思考链优化

### MultilingualReasoning - 多语言推理
`chapter7/MultilingualReasoning/`

训练模型在多种语言环境下的推理能力，提升跨语言任务的表现。

**核心概念**：多语言、跨语言推理、语言泛化

### SpatialReasoning - 空间推理训练
`chapter7/SpatialReasoning/`

专注于训练模型的空间推理能力，处理涉及位置、方向、距离等空间关系的问题。

**核心概念**：空间推理、几何理解、位置关系

### SimpleVLA-RL - 视觉-语言-动作 RL
`chapter7/SimpleVLA-RL/`

结合视觉、语言和动作的强化学习训练，让模型能够理解视觉输入并执行相应动作。

**核心概念**：视觉-语言-动作、多模态 RL、具身智能

### continued-pretraining - 持续预训练
`chapter7/continued-pretraining/`

在特定领域数据上进行持续预训练，提升模型在目标领域的表现。

**核心概念**：持续预训练、领域适应、知识注入

### MiniMind-pretrain - 小型模型预训练
`chapter7/MiniMind-pretrain/`

从零开始预训练小型语言模型，理解预训练的完整流程和关键技术。

**核心概念**：预训练、小型模型、训练流程

### sesame - 序列建模与评估
`chapter7/sesame/`

专注于序列建模任务的训练和评估方法。

**核心概念**：序列建模、评估方法、性能优化

### orpheus - 音乐生成与理解
`chapter7/orpheus/`

训练模型的音乐生成和理解能力。

**核心概念**：音乐生成、音频理解、创意 AI

### tinker-cookbook - 训练技巧集锦
`chapter7/tinker-cookbook/`

收集各种模型训练的实用技巧和最佳实践。

**核心概念**：训练技巧、最佳实践、调优方法

## 🔄 第 8 章 · Agent 的自我进化

本章聚焦让 Agent 在不改动权重的前提下从经验中持续成长：把成功轨迹沉淀为可复用的经验、把重复操作外化为工具，以及把提示与观察蒸馏进模型。

### gaia-experience - 从成功经验中学习
`chapter8/gaia-experience/`

基于 AWorld 框架和 GAIA 基准测试，实现完整的“学习-应用”闭环。Agent 自动总结成功的任务轨迹为结构化经验，并在新任务中检索应用，实现自我进化。

**核心概念**：经验学习、策略摘要、轨迹总结、自我进化

### browser-use-rpa - 工作流录制与回放
`chapter8/browser-use-rpa/`

实现浏览器自动化的工作流录制系统，将重复性操作序列自动封装为参数化工具。通过从昂贵的 LLM 推理切换到精确的自动化执行，实现 3-5 倍速度提升。

**核心概念**：工作流录制、RPA、工具生成、外部化学习

### prompt-distillation - 提示蒸馏
`chapter8/prompt-distillation/`

将复杂提示的效果蒸馏到模型参数中，减少推理时的提示长度，把上下文中的经验固化为参数化知识。

**核心概念**：知识蒸馏、提示优化、参数化知识

### prompt-auto-optimization - 系统提示词自动优化
`chapter8/prompt-auto-optimization/`

基于人类反馈的自动化系统提示学习：以 tau-bench 风格航空客服「过度转接」问题为例，让一个 Coding Agent 读取系统提示词文件、定位有问题的规则、生成精确修改并真的改写 prompt 文件，再重新评测验证，形成「反馈 → 改写 → 验证」闭环。

**核心概念**：提示词自动优化、人类反馈、Coding Agent、闭环评测

### active-tool-discovery - 主动工具发现
`chapter8/active-tool-discovery/`

对比「全量注入 120+ 工具 schema」与「主动按需发现」两种范式：后者只在 system 里保留少量基础工具 + 一个 `discover_tools` 元工具，用嵌入相似度从工具库检索 3-5 个最相关的专用工具，既省 token 又避免模型在超长工具列表下错选/滥用通用工具。

**核心概念**：主动工具发现、嵌入检索、token 优化、指令遵循

### self-evolving-tools - 从网络寻找工具实现自我进化
`chapter8/self-evolving-tools/`

Alita 式「最小预定义，最大自我进化」：Agent 不预置任何领域工具，只有五个通用元工具，遇到不会做的任务时自己上网找开源库/API、读文档、在沙箱测试，把可行方案封装成新工具存入工具库并复用，全程强调幻觉控制。

**核心概念**：自我进化、工具创造、工具复用、幻觉控制

### self-evolution-eval - 自我进化 Agent 评估数据集
`chapter8/self-evolution-eval/`

为评估 Agent 的「自我进化」能力（自己发现、创造并复用工具）设计的专用数据集与验证方法：20 个跨领域任务（不暗示工具名）+ 四层分层验证 harness + 可控参考 Agent，超越「结果对不对」去考察发现、创造与复用质量。

**核心概念**：评估数据集设计、分层验证、工具复用度量、自我进化

## 🎙️ 第 9 章 · 多模态与实时交互

### live-audio - 实时语音对话
`chapter9/live-audio/`

实时语音聊天演示，集成语音转文本、AI 对话和文本转语音功能。支持多个 AI 服务提供商（OpenAI、OpenRouter、ARK、Siliconflow），提供低延迟的对话体验。

**核心特性**：
- 实时语音输入与 VAD（Voice Activity Detection）
- 多提供商支持：ASR（OpenAI Whisper、SenseVoice）、LLM（GPT-4o、Gemini、Doubao）、TTS（Fish Audio）
- WebSocket 实时通信、低延迟音频流
- 实时延迟监控和日志记录

**核心概念**：语音识别、实时对话、TTS、WebSocket、多提供商架构

### browser-use - 浏览器自动化 Agent（Computer Use）
`chapter9/browser-use/`

Browser-Use 是一个强大的浏览器自动化框架，让 LLM 能够控制浏览器完成复杂任务。支持表单填写、网页导航、数据提取等场景，是 GUI 自动化（Computer Use）的典型实现。

**核心特性**：
- LLM 驱动的浏览器自动化
- 支持多种 LLM（ChatBrowserUse、OpenAI、Google、本地模型）
- 自定义工具扩展、认证处理
- 沙箱部署支持、云服务集成

**核心概念**：浏览器自动化、Computer Use、视觉理解、工具扩展

### claude-quickstarts - Claude 快速入门
`chapter9/claude-quickstarts/`

Claude API 的快速入门示例和最佳实践，涵盖各种使用场景。

**核心概念**：Claude API、提示工程、最佳实践

### phone-agent - 电话 Agent
`chapter9/phone-agent/`

演示语音 Agent「代替用户与外部世界进行电话交互」：上层是标准 ReAct Agent，接到自然语言任务后自行想清号码与通话目标，调用 `make_phone_call` 工具（基于电话语音 API 抽象）完成整段通话，读取结构化通话记录并按需追问再拨，最后向用户汇报。

**核心概念**：语音 Agent、电话交互、ReAct、工具抽象

### end-to-end-speech - 端到端语音思考 vs 级联流水线
`chapter9/end-to-end-speech/`

对应 Step-Audio R1 的端到端语音思考范式（单一模型「听 → 想 → 说」）：跑通「语音输入 → 思考 → 语音输出」闭环，并与 ASR→LLM→TTS 级联范式直观对比延迟与副语言信息（情绪/语气/语速）的损失差异。

**核心概念**：端到端语音、级联对比、副语言信息、边想边说

### streaming-speech - 模拟流式语音感知
`chapter9/streaming-speech/`

演示流式语音感知的核心权衡：把连续音频按递增长度分块喂给 ASR，每收到一小段就产出「当前部分识别结果」以极低首包延迟尽早出文本，代价是早期分块因缺后半句上下文可能出错，随音频累积逐步收敛，与「等整句到齐再识别」的高准确/高延迟形成对照。

**核心概念**：流式感知、分块识别、首包延迟、过早决策代价

### controllable-tts - 控制标记驱动的可控 TTS
`chapter9/controllable-tts/`

让主 LLM 的输出带上控制标记（情感/语速/风格/停顿/笑声），执行层解析标记并映射到参考语音库的对应风格档案再合成语音，把「在哪停顿、用什么语气」的决策交给 LLM，同一段文本可合成出不同风格与情感。

**核心概念**：可控 TTS、控制标记、参考语音库、韵律控制

## 🤝 第 10 章 · 多 Agent 协作

### use-computer-while-calling - 双 Agent 架构
`chapter10/use-computer-while-calling/`（📖 完整代码已独立为 [19PINE-AI/TalkAct](https://github.com/19PINE-AI/TalkAct)，本目录仅保留说明文档）

实现电话呼叫 Agent 和计算机使用 Agent 的双 Agent 协作架构。两个 Agent 通过 WebSocket 直接通信，无需协调器。电话 Agent 处理语音交互，计算机 Agent 执行浏览器自动化，并行工作完成需要语音和网页操作的复杂任务。

**核心特性**：
- 直接 Agent 间通信（无协调器）
- 标准工具调用进行消息传递
- 并行操作：语音对话 + 浏览器自动化
- 简单的 JSON 消息协议

**架构组件**：
- Phone Call Agent（Node.js）：语音 I/O、ASR/TTS、LLM 对话
- Computer Use Agent（Python）：浏览器自动化、browser-use、网页抓取
- WebSocket 通信：Agent 间直接消息传递

**核心概念**：多 Agent 协作、Agent 间通信、并行任务处理、语音+浏览器集成

### staged-system-prompt - 按执行阶段切换系统提示词
`chapter10/staged-system-prompt/`

同一个 Coding Agent 在任务不同执行阶段（需求澄清 → 代码实现 → 代码审查）加载不同的系统提示词与工具集，从而在一段对话里扮演不同角色、表现不同行为，而对话历史与任务状态在阶段间连续共享，审查不通过还可回退到实现阶段。

**核心概念**：阶段化提示词、角色切换、共享上下文、阶段流水线

### multi-role-transfer - 多角色转换与自主移交
`chapter10/multi-role-transfer/`

演示共享上下文下的链式移交（handoff）：一个会话里存在多个专业角色 Agent，各有独立系统提示词与专属工具集，通过 `transfer_to_agent` 工具由 Agent 根据任务进展自主判断该切换到哪个角色；因共享同一段对话历史，移交时完整上下文天然保留。

**核心概念**：角色移交、handoff、共享上下文、自主切换

### book-translation - 书籍翻译 Agent（管理者模式）
`chapter10/book-translation/`

用管理者模式（Orchestration）把长文档翻译拆给术语表/翻译/审校等专职 Agent：Manager 只保存任务、计划、调用记录和文件索引，完整译文全部落盘，因此上下文基本恒定；并对比单 Agent 方案，用真实 token 数说明如何控制上下文膨胀、用共享术语表保证全书一致。

**核心概念**：管理者模式、上下文隔离、上下文膨胀控制、共享术语表

### parallel-web-research - 并行多源信息搜集 Agent
`chapter10/parallel-web-research/`

演示多个同构 Agent 的并行搜索 + 中心协调：主协调器同时启动 N 个子 Agent 各访问一个来源找答案，一旦某个命中目标其余立即优雅停止。消息总线、并行派发、实时监控、级联终止与竞态处理均为真实实现（用可控模拟信息源代替真实浏览器）。

**核心概念**：并行 Agent、中心协调、消息总线、级联终止

### voice-werewolf - 语音狼人杀 Agent 系统
`chapter10/voice-werewolf/`

用多 Agent 狼人杀演示「上下文不共享」下的信息权限控制：每个玩家是独立 LLM Agent 且维护严格隔离的私有上下文，由代码驱动的确定性法官决定每条信息投递进哪些玩家上下文并登记审计，游戏结束自动校验隔离是否正确。语音为可选增强。

**核心概念**：信息不对称、私有上下文隔离、法官编排、审计校验

## 📖 学习建议

### 核心理念：Agent = 模型 + 上下文 + 工具

本书的核心框架是 **Agent = 模型 + 上下文 + 工具**，这三个组件相互协作，共同实现 Agent 的智能行为：

- **模型（Model）**：Agent 的大脑，提供理解、推理和决策能力
- **上下文（Context）**：Agent 的操作系统，包含系统指令、对话历史、推理过程、工具交互记录等
- **工具（Tools）**：Agent 的双手，让 Agent 能够感知环境、执行操作、与外部世界交互

### 学习路径

学习路径与全书章节一一对应，围绕三大支柱层层展开：

- **第 1 章 · 基础篇**：建立对 Agent 系统的完整认知框架——理解 RL 中的 Agent 定义、对比传统 RL 与 LLM+RL 范式的样本效率差异、理解“模型即 Agent”的新范式，掌握 **Agent = 模型 + 上下文 + 工具** 的核心框架。**关键洞察**：先验知识的重要性超越算法和环境。

- **第 2–3 章 · 上下文篇**：上下文是 Agent 的操作系统。第 2 章覆盖系统提示、KV Cache 友好设计、上下文压缩与提示工程消融；第 3 章覆盖用户记忆、稠密/稀疏/混合检索、Agentic RAG、上下文感知检索与结构化知识提取。**关键洞察**：完整的上下文包括系统指令、对话历史、推理过程、工具交互记录、用户记忆和外部知识。

- **第 4–5 章 · 工具篇**：工具是 Agent 与世界交互的桥梁。第 4 章覆盖感知/执行/协作三类 MCP 工具、事件触发与异步架构；第 5 章深入生产级 Coding Agent 的完整实现。**关键洞察**：工具设计应通用化（代码解释器优于计算器），代码是能创造新工具的元能力。

- **第 6–7 章 · 模型篇**：如何度量与放大智能。第 6 章覆盖 Terminal-Bench、SWE-bench、GAIA、OSWorld、Tau2-Bench 等评估基准；第 7 章覆盖 SFT、RL、RLHF、样本效率等后训练技术。**关键洞察**：独立的验证信号比“让模型再想一遍”更可靠；“模型即 Agent”通过 RL 把工具调用内化为原生能力。

- **第 8 章 · 自我进化篇**：让 Agent 在不改权重的前提下从经验中成长——经验学习、工作流外化为工具、提示与观察蒸馏进参数。**关键洞察**：从经验中学习是 Agent 从“聪明”走向“熟练”的关键。

- **第 9–10 章 · 拓展与协作篇**：第 9 章把感知与行动从文本扩展到语音、GUI 与物理世界；第 10 章通过多 Agent 分工协作处理复杂任务。**关键洞察**：多 Agent 系统的每个设计决策都能在单 Agent 的三要素中找到对应。

### 难度分级

- **入门级**（第 1–2 章）：适合初学者，理解基本概念
- **进阶级**（第 3–4 章）：需要一定编程基础，涉及系统集成
- **高级**（第 5–6 章）：需要较强编程能力，涉及复杂系统设计
- **专家级**（第 7–8 章）：需要深度学习和训练/自我进化经验
- **应用级**（第 9–10 章）：综合运用前面所学，构建实际应用

### 实践建议

1. **动手实践**：每个项目都设计为可独立运行，建议亲自运行并修改代码
2. **结合书籍**：配合本仓库 [`book/`](book/) 中的书稿相应章节阅读，理解理论与实践的结合
3. **实验对比**：多个项目包含消融研究和对比实验，通过对比加深理解
4. **渐进学习**：从简单项目开始，逐步深入复杂系统
5. **关注协议**：第 4 章的 MCP 服务器项目展示了标准化工具协议，这是构建可扩展 Agent 的关键

## 🔑 API 密钥

建议大家申请几个平台的 API key，方便学习：
- **Kimi**: https://platform.moonshot.cn/ 月之暗面的 Kimi 系列，长上下文与 Agent 能力强
- **智谱 GLM**: https://open.bigmodel.cn/ 智谱 AI 的 GLM 系列（GLM-4.6 等），中文能力强、性价比高，也很推荐
- **Siliconflow**: https://siliconflow.cn/ 上面有各种开源模型，包括 DeepSeek、Qwen 等
- **火山引擎**: https://www.volcengine.com/product/ark 上面有字节的闭源模型（豆包），国内访问延迟比较低
- **OpenRouter**: https://openrouter.ai/ 可以从国内直接访问海外的各种闭源和开源模型，包括 Gemini 2.5 Pro、Claude 4 Sonnet、OpenAI GPT-5 等（官方 API 需要海外 IP 和支付方式，OpenAI 还需要海外身份实名认证，注册比较麻烦）

模型选型可以参考： https://01.me/2025/07/llm-api-setup/

## 📦 附录 · 外部仓库获取

出于体积与版权考虑，第 6、7、9 章用到的评测基准与训练框架**未内置**在本仓库，需要自行克隆到对应目录（下方为各仓库的上游地址与本书验证过的提交）。可将以下命令保存为脚本一次性拉取：

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

> 各项目 README 中如标注了特定提交（commit），请按其说明 `git checkout` 到对应版本，以保证复现结果一致。
> 第 10 章 `use-computer-while-calling` 已发展为持续维护的独立仓库 [19PINE-AI/TalkAct](https://github.com/19PINE-AI/TalkAct)，本仓库仅保留一份指向它的说明文档（`chapter10/use-computer-while-calling/README.md`）。

**依赖真实硬件 / 外部环境的实验（无本仓库代码，指向上游文档）：**

- **实验 9-8 / 9-9 · XLeRobot 遥操作与 LLM Agent 控制**：需 SO-100/XLeRobot 机械臂，按上游文档操作 —— [Teleop](https://xlerobot.readthedocs.io/en/latest/software/getting_started/XLeRobot_teleop.html) · [LLM Agent](https://xlerobot.readthedocs.io/en/latest/software/getting_started/LLM_agent.html)
- **实验 9-10 · RGB 零样本 Sim2Real 抓取**：[`StoneT2000/lerobot-sim2real`](https://github.com/StoneT2000/lerobot-sim2real)（仿真训练部分可纯 GPU 完成，真实部署需 SO-100 机械臂）
- **实验 6-11 · OpenVLA + RoboTwin2 仿真评估**：VLA 训练/环境依赖见 `chapter7/SimpleVLA-RL` 的 README（其中说明 OpenVLA、RoboTwin2 的获取与配置）

**读者练习类实验（书中作为练习题给出，复用已文档化的既有项目，无专属目录）：**

- **实验 5-12 · 能创造 Agent 的 Agent**：基于 `chapter5/coding-agent` 自举扩展
- **实验 6-2 / 6-3 / 6-4 / 6-9**：分别为人肉基准、记忆评估、JSON Cards vs RAG、记忆选型——改造复用第 3 章 `user-memory` / `user-memory-evaluation` / `contextual-retrieval` 等项目
- **实验 7-8 · Prompt 蒸馏**：落地实现见第 8 章 `chapter8/prompt-distillation`（跨章复用）
- **实验 7-9 · CoT 蒸馏 `[扩展]`**：书中给出实验设计与验收标准，作为读者扩展实验，暂无专属代码

## 🤝 贡献

本书与配套代码全部开源，非常欢迎社区通过 Pull Request 参与共建。以下几类贡献我们都非常欢迎：

1. **书籍内容改进**：勘误、补充、更清晰的表述，或新增前沿进展（正文见 `book/chapter*.md`）
2. **代码改进与 Bug 修复**：让配套项目更健壮、更易用、更贴近生产实践
3. **新的实践项目**：为某个实验补充/替换更好的实现，或贡献全新的示例项目
4. **书籍配图的设计改进**：让 `book/images/` 中的图表在设计上更清晰、更美观（配图由 `book/gen_*_figs.py` 生成）

提交前建议先把相关实验亲手跑一遍、确认可复现；也欢迎先提 issue 讨论想法。

## 📄 许可证

本项目采用 [Apache License 2.0](LICENSE) 开源许可证，详见 [`LICENSE`](LICENSE) 文件。部分子项目可能包含各自的许可证信息，请以子项目中的说明为准。

## ⭐ Star History

<a href="https://star-history.com/#bojieli/ai-agent-book&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/star-history-dark.png" />
    <source media="(prefers-color-scheme: light)" srcset="assets/star-history-light.png" />
    <img alt="Star History Chart" src="assets/star-history-light.png" width="720" />
  </picture>
</a>

<sub>图表由 [`scripts/gen_star_history.py`](scripts/gen_star_history.py) 绘制（自 2026 年 7 月 13 日起），[GitHub Actions 定时任务](.github/workflows/star-history.yml) 每天自动更新并提交到 <code>assets/</code> 目录；点击可跳转到 star-history.com 查看实时数据。</sub>

```

# translated_output_5.md
```md
# AI Agents in Depth: Design Principles and Engineering Practices

**English** | [中文](README.md)

This repository is the main open-source repository for the book *AI Agents in Depth: Design Principles and Engineering Practices*, containing the **full text of the book** and **accompanying example code**. The full text, illustrations, and accompanying experimental code are all open-source. You are welcome to run the experiments yourself, and submit issues and PRs.

## 📖 E-book

The book is available in both Chinese and English:

- **Chinese PDF (Original)**: [`book/深入理解-AI-Agent-李博杰-v1.1.pdf`](book/深入理解-AI-Agent-李博杰-v1.1.pdf)
- **English PDF** (Community-contributed translation by [@nsdevaraj](https://github.com/nsdevaraj)): [`book-en/AI-Agents-in-Depth-Bojie-Li-v1.1.pdf`](book-en/AI-Agents-in-Depth-Bojie-Li-v1.1.pdf)
- **Tamil PDF** (Community-contributed translation by [@nsdevaraj](https://github.com/nsdevaraj)): [`book-ta/AI-Agents-in-Depth-Bojie-Li-v1.1-ta.pdf`](book-ta/AI-Agents-in-Depth-Bojie-Li-v1.1-ta.pdf)

The Chinese text and compiled PDFs are located in the [`book/`](book/) directory; the English and Tamil translations are **community contributions**, located in the [`book-en/`](book-en/) and [`book-ta/`](book-ta/) directories respectively, and their content may lag behind the original Chinese version:

- **Source text**: `book/introduction.md` (Introduction), `book/chapter1.md` ~ `book/chapter10.md` (Chapters 1 to 10), `book/afterword.md` (Afterword)
- **Compile it yourself**: After installing pandoc, xelatex, the ElegantBook document class, and related fonts, run

  ```bash
  cd book && bash build_pdf.sh
  ```

  Figures are generated by `book/gen_*_figs.py` and stored in `book/images/`. For typesetting details, see `book/preamble.tex` and `book/*.lua`.

## 📑 Content Overview (Chapters 1–10)

The book revolves around the core formula **Agent = LLM + Context + Tools**, with the ten chapters covering the following:

- **Chapter 1 · Agent Fundamentals**: Starting from the new paradigm of "Model as Agent", it establishes the core formula **Agent = LLM + Context + Tools**, and introduces Harness engineering—all engineering capabilities beyond the model itself are where the true competitive edge lies.
- **Chapter 2 · Context Engineering**: Context determines the upper limit of an Agent's capabilities. It delves into the context structure of LLM APIs, KV Cache-friendly design, prompt engineering, dynamic prompts and Agent Skills, status bar metadata, and context compression strategies.
- **Chapter 3 · User Memory and Knowledge Bases**: Enabling Agents to remember users across sessions and integrate external knowledge. It covers user memory systems, basic RAG pipelines, and knowledge organization and retrieval beyond flat text (structured indexing, knowledge graphs, etc.).
- **Chapter 4 · Tools**: Tools are the hands of the Agent. It covers tool classification and general design principles, the MCP (Model Context Protocol) and challenges in tool selection, three categories of tools (perception/execution/collaboration), and event-driven asynchronous Agents.
- **Chapter 5 · Coding Agents and Code Generation**: Code is the "tool that creates new tools", a meta-capability for general Agents. Using a production-grade Coding Agent as an example, it demonstrates the complete implementation of this most powerful general-purpose tool.
- **Chapter 6 · Agent Evaluation**: Turning Agent performance into comparable signals. From evaluation environments, dataset design, and metric systems, to statistical significance, observability, evaluation-driven model selection, up to production-grade internal evaluation and simulation environments.
- **Chapter 7 · Model Post-Training**: The panoramic view of the three stages: pre-training, SFT, and RL. When to choose SFT vs. RL, RLHF, algorithm comparisons, data and environments, and cutting-edge explorations in teaching models tool use and improving sample efficiency.
- **Chapter 8 · Agent Self-Evolution**: Growing without changing weights. Three learning paradigms: learning from experience, active tool discovery, and transitioning "from tool user to tool creator", taking Agents from "smart" to "proficient".
- **Chapter 9 · Multimodality and Real-Time Interaction**: Expanding perception and action from text to speech, GUIs, and the physical world. Three speech paradigms (cascaded/end-to-end omni-modal/full-duplex), streaming speech perception and synthesis, Computer Use, and robotic manipulation.
- **Chapter 10 · Multi-Agent Collaboration**: Collective intelligence can surpass individual intelligence. Multi-Agent classification frameworks, when they truly outperform single Agents, collaboration with and without shared context, failure modes, and the emergent "Agent society".

## 💻 Accompanying Code

All projects are organized by **chapter**, corresponding one-to-one with the ten chapters of the book, covering a complete learning path from basic concepts to advanced techniques, with directories structured as `chapterN/project-name/`. The vast majority of experiments in Chapters 5, 8, 9, and 10 now provide independently runnable accompanying demos, which have been integrated with real LLM APIs and verified to work.

### Project Type Description

The accompanying projects are divided into three categories. Please refer to the icons below to understand the "out-of-the-box" readiness of each project:

- ✅ **Independently Runnable**: This repository contains the complete code; simply configure the API Key (see the end of the document) to run it.
- 📖 **Reproduction Guide**: The project itself is a detailed reproduction document that relies on **external repositories** (training frameworks, evaluation benchmarks, etc.) which need to be `git clone`d manually. See "External Repositories Acquisition" below.
- 🚧 **Design Document**: Currently contains only design documents for architecture and implementation plans; runnable code is still under development.

The following projects are **not** ✅ Independently Runnable; please take note when cloning this repository:

| Project | Type | Description |
| --- | --- | --- |
| `chapter7/AdaptThink` · `AWorld-train` · `MiniMind-pretrain` · `retool` · `SpatialReasoning` | 📖 Reproduction Guide | Training experiments, relies on external frameworks, reproduce according to README |
| All benchmarks in Chapter 6 · Most training frameworks in Chapter 7 · `browser-use`/`claude-quickstarts` in Chapter 9 · `use-computer-while-calling` in Chapter 10 | 📖 Reproduction Guide | Relies on external repositories, see "External Repositories Acquisition" |

### External Repositories Acquisition (Brief)

**Some** experiments in Chapters 6, 7, 9, and 10 rely on **external repositories** such as evaluation benchmarks, training frameworks, and robotics platforms (not included in this repository due to size and copyright considerations). To avoid information overload upfront, **the complete clone commands, upstream addresses, and commits verified by this book can be found in the "Appendix · External Repositories Acquisition" at the end of the document**. It is recommended to start with the independently runnable projects in the earlier chapters, and quickly acquire the external repositories according to the instructions at the end when you need to reproduce training/evaluation/robotics experiments.

## 🚀 Chapter 1 · Agent Fundamentals

### learning-from-experience - Reinforcement Learning vs LLM Comparison
`chapter1/learning-from-experience/`

Compares traditional reinforcement learning (Q-learning) with LLM-based in-context learning, reproducing the key insights from Shunyu Yao's "The Second Half" blog post. Through a treasure hunt game, it demonstrates how LLMs surpass traditional RL with 250-400x sample efficiency.

**Core Concepts**: Reinforcement learning, in-context learning, sample efficiency, prior knowledge

### web-search-agent - Kimi K2 Model as Agent
`chapter1/web-search-agent/`

Implements an Agent with basic deep search capabilities, capable of multi-turn search and information integration.

**Core Concepts**: Web search, model-native Agent

### search-codegen - GPT-5 Native Tool Integration
`chapter1/search-codegen/`

Builds an Agent with basic deep search capabilities and code sandboxing, comprehensively utilizing tools like web search and code execution to achieve complex analysis.

**Core Concepts**: Web search, code generation, model-native Agent

### context - Context Ablation Study
`chapter1/context/`

Demonstrates the importance of various components in Agent context through systematic ablation experiments. Supports multiple LLM providers (SiliconFlow Qwen, ByteDance Doubao, Moonshot Kimi), configuring different context modes to observe changes in Agent behavior.

**Core Concepts**: Context management, tool calling, ReAct loop, ablation study

## 🎯 Chapter 2 · Context Engineering

### local_llm_serving - Local LLM Deployment and Tool Calling
`chapter2/local_llm_serving/`

Cross-platform local LLM deployment solution that automatically selects the optimal backend (vLLM or Ollama). Demonstrates how even a small 0.6B model can achieve excellent tool-calling capabilities through good system design. Supports streaming responses to display the thinking process in real time.

**Core Concepts**: Model deployment, Chat Template, streaming, tool calling

### attention_visualization - Attention Mechanism Visualization
`chapter2/attention_visualization/`

Visualizes the complete input/output token sequences and attention weight distributions of LLMs to deeply understand how models process context, reason, and call tools.

**Core Concepts**: Attention mechanism, token analysis, reasoning process visualization

### kv-cache - KV Cache-Friendly Context Design
`chapter2/kv-cache/`

Explores the impact of different context management modes on the KV Cache, demonstrating how common error patterns destroy cache efficiency. Experiments show how correct context design can significantly reduce latency and costs.

**Core Concepts**: KV Cache, context optimization, performance tuning

### context-compression - Context Compression Strategies
`chapter2/context-compression/`

Implements and compares various context compression strategies, including summarization, key information extraction, and semantic compression. Reduces token usage while maintaining Agent capabilities.

**Core Concepts**: Context compression, token optimization, information density

### prompt-engineering - Prompt Engineering Ablation Study
`chapter2/prompt-engineering/`

Extends the Tau-Bench framework, quantifying the impact of different prompt engineering factors on Agent performance through systematic ablation experiments. Demonstrates how factors like tone style, instruction organization, and tool descriptions affect task completion rates.

**Core Concepts**: Prompt engineering, ablation study, performance benchmarking

### system-hint - System Prompt Optimization
`chapter2/system-hint/`

Studies the impact of System Hints on Agent behavior, exploring how to improve performance by optimizing system prompts.

**Core Concepts**: System prompt, behavior steering, prompt optimization

### log-sanitization - Log Sanitization
`chapter2/log-sanitization/`

Implements an intelligent log sanitization system that protects sensitive data while retaining debugging information.

**Core Concepts**: Privacy protection, log processing, data security

### prompt-injection - Prompt Injection Attack and Defense Experiments
`chapter2/prompt-injection/`

Constructs controlled experiments with 3 attack scenarios (direct injection, indirect injection, memory injection) × 4 defense configurations (no defense, prompt hardening, source marking, combined defense). Uses deterministic rules to statistically measure attack success rates, intuitively demonstrating how the injection success rate significantly drops as defenses are layered.

**Core Concepts**: Prompt injection, indirect injection, data and instruction separation, runtime validation

### agent-skills-ppt - Progressive Disclosure of Agent Skills for PPT Generation
`chapter2/agent-skills-ppt/`

Reproduces the "progressive disclosure" concept of Agent Skills: the Agent only sees a thin Skill directory at startup, and upon recognizing the task requires the `pptx` Skill, it progressively loads its complete workflow, detailed documentation, and bundled scripts, ultimately using python-pptx to generate real `.pptx` files.

**Core Concepts**: Agent Skills, progressive disclosure, on-demand loading, tool orchestration

## 📚 Chapter 3 · User Memory and Knowledge Bases

### user-memory - User Memory System
`chapter3/user-memory/`

Builds a long-term user memory system, enabling the Agent to remember user preferences and historical interactions to provide personalized services.

**Core Concepts**: Long-term memory, personalization, user modeling

### mem0 / memobase - Open-Source Memory Framework Comparison
`chapter3/mem0/` and `chapter3/memobase/`

Implements a version of user memory using two open-source memory frameworks, mem0 and Memobase, serving as a controlled implementation for Experiment 3-2 "Memory Strategy Comparison", facilitating horizontal comparison of the extraction forms and response quality of different memory solutions.

**Core Concepts**: Memory framework, mem0, Memobase, solution comparison

### user-memory-evaluation - User Memory Evaluation Framework
`chapter3/user-memory-evaluation/`

Systematically evaluates the accuracy, relevance, and effectiveness of user memory systems, including various test scenarios and evaluation metrics.

**Core Concepts**: Evaluation framework, test cases, performance metrics

### dense-embedding - Dense Embedding Vector Retrieval Service
`chapter3/dense-embedding/`

Builds a vector similarity search service, comparing and studying two approximate nearest neighbor indexing algorithms: ANNOY (tree-based) and HNSW (graph-based). Demonstrates the trade-offs of different indexing strategies in terms of performance, memory footprint, and update capabilities.

**Core Concepts**: Dense embedding, vector retrieval, ANN algorithms, semantic search

### sparse-embedding - Sparse Retrieval Engine
`chapter3/sparse-embedding/`

Implements a sparse vector search engine based on the BM25 algorithm from scratch, showcasing the internal workings of the search engine through rich logs and visualization interfaces to understand term frequency weight calculation and inverted index principles.

**Core Concepts**: Sparse embedding, BM25, TF-IDF, exact matching

### retrieval-pipeline - Hybrid Retrieval Pipeline
`chapter3/retrieval-pipeline/`

Builds a complete retrieval pipeline combining dense retrieval, sparse retrieval, and neural reranking. Through carefully designed test cases, it systematically demonstrates the complementary advantages of hybrid retrieval in different scenarios.

**Core Concepts**: Hybrid retrieval, neural reranking, cross-encoder, retrieval fusion

### multimodal-agent - Multimodal Information Extraction
`chapter3/multimodal-agent/`

Compares three multimodal processing strategies: native multimodal processing, extraction to text, and tool-based analysis. Through ablation studies under a unified framework, it reveals the trade-offs of different technical paths in terms of fidelity, cost, and flexibility.

**Core Concepts**: Multimodality, visual understanding, OCR, end-to-end processing

### structured-index - Structured Indexing
`chapter3/structured-index/`

Implements and compares two advanced indexing strategies: RAPTOR (Recursive Abstractive Tree) and GraphRAG (Knowledge Graph). Demonstrates how to build structured indexes that reflect the inherent hierarchy and associations of knowledge through an indexing technique manual.

**Core Concepts**: RAPTOR, GraphRAG, hierarchical summarization, knowledge graph

### agentic-rag - Agentic RAG
`chapter3/agentic-rag/`

Compares the performance differences between traditional Non-Agentic RAG and Agentic RAG. Demonstrates how Agents dominate iterative information retrieval through the ReAct pattern, significantly improving answer quality when handling complex legal Q&A.

**Core Concepts**: Agentic RAG, ReAct loop, iterative retrieval, active exploration

### agentic-rag-for-user-memory - Building User Memory with Agentic RAG
`chapter3/agentic-rag-for-user-memory/`

Applies the Agentic RAG framework to manage user conversation history, handling cross-session memory retrieval through multi-turn iterative search capabilities, achieving basic recall and multi-session retrieval abilities.

**Core Concepts**: User memory, conversation history indexing, cross-session retrieval

### contextual-retrieval - Contextual Retrieval
`chapter3/contextual-retrieval/`

Implements the contextual retrieval technique proposed by Anthropic, solving the context loss problem of traditional chunking methods by generating prefix summaries containing core context for text chunks, reducing retrieval failure rates by 49-67%.

**Core Concepts**: Context enhancement, prefix generation, semantic anchoring, retrieval optimization

### contextual-retrieval-for-user-memory - Context-Aware User Memory System
`chapter3/contextual-retrieval-for-user-memory/`

Applies contextual retrieval techniques to user memory construction, combining Advanced JSON Cards with context-aware RAG to form a dual-layer memory structure, achieving a higher level of proactive service capabilities.

**Core Concepts**: Dual-layer memory, structured facts, contextual retrieval, proactive service

### structured-knowledge-extraction - Structured Knowledge Extraction
`chapter3/structured-knowledge-extraction/`

Uses legal precedents as an example to run through a three-stage pipeline: "bottom-up factor discovery → clustering into case prototypes → conversational advisory Agent". Without presetting rigid fields, the LLM autonomously discovers factors from a large number of cases and induces them into a modular schema (core factors + charge extension factors); then clusters cases into several prototypes and calculates the factor importance of each prototype; the Agent matches new cases to the most similar prototype, asks for missing information according to importance, and provides evidence-based recommendations (with legal disclaimers).

**Core Concepts**: Bottom-up knowledge discovery, modular factors, clustered prototypes, explainable decision-making

## 🛠️ Chapter 4 · Tools

### perception-tools - Perception Tools MCP Server
`chapter4/perception-tools/`

Builds a comprehensive set of perception tools, providing web search, multimodal understanding, file system operations, and public data source access capabilities. Most functions are based on free open APIs (DuckDuckGo, Open-Meteo, Yahoo Finance, OpenStreetMap, etc.) and can be used without API keys.

**Core Concepts**: MCP, multimodal parsing, public data sources, document understanding, geospatial services

### execution-tools - Execution Tools MCP Server
`chapter4/execution-tools/`

Implements a set of execution tools with security mechanisms, including file operations, code interpreter, virtual terminal, and external system integration. Prevents dangerous operations through an LLM secondary approval mechanism, automatically summarizes complex outputs, and performs syntax validation on code.

**Core Concepts**: MCP, execution security, LLM approval, result summarization, automatic validation

### collaboration-tools - Collaboration Tools MCP Server
`chapter4/collaboration-tools/`

Provides comprehensive collaboration capabilities, including browser automation (browser-use framework), Human-in-the-Loop, multi-channel notifications (Email, Telegram, Slack, Discord), and timer management. Supports administrator approval for sensitive operations and scheduled task scheduling.

**Core Concepts**: MCP, browser automation, HITL mode, multi-channel notifications, scheduled tasks

### agent-with-event-trigger - Event-Triggered Agent and MCP Integration
`chapter4/agent-with-event-trigger/`

A modern event-driven Agent built on FastAPI, integrating all tools from the previous three MCP servers by default. Adopts a native asynchronous architecture for clear MCP tool loading, receiving multi-source events (Web, instant messaging, GitHub, timers, etc.) via HTTP API. Provides automatic API documentation (Swagger UI) and background monitoring capabilities.

**Core Concepts**: FastAPI, native asynchronous, MCP integration, event-driven, automatic API documentation, tool orchestration

### active-tool-selection - Active Tool Selection
`chapter4/active-tool-selection/`

Implements an intelligent tool selection mechanism, enabling the Agent to proactively select the most appropriate combination of tools based on task requirements, rather than passively accepting a predefined toolset.

**Core Concepts**: Tool selection, dynamic tool loading, task analysis

### async-agent - Asynchronous Agent with Parallel Execution and Interruption Capabilities
`chapter4/async-agent/`

Implements the core of an event-driven asynchronous Agent framework (Flux) based on asyncio single-threading: the inbox event queue dispatches by urgency (interrupt/immediate/queued), supports parallel execution of asynchronous tools, interrupts the current turn during runtime, and performs cancellation and status queries for simulated long tasks. Decisions are made by a real LLM (function calling).

**Core Concepts**: Asynchronous programming, event queue, interruption mechanism, parallel tool cancellation, non-blocking I/O

> Additionally, `chapter4/docker-compose.yml` and `chapter4/DOCKER_DEPLOYMENT.md` provide reference solutions for containerized deployment of the aforementioned MCP tool servers.

## 💻 Chapter 5 · Coding Agents and Code Generation

### coding-agent - Production-Grade Coding Agent
`chapter5/coding-agent/`

A production-grade AI coding assistant built on Claude, implementing all tools in pure Python without command-line dependencies. Includes 17 fully implemented tools covering file operations, search, shell operations, and project management. Specifically implements a pure Python Grep tool that is fully compatible with ripgrep's functionality.

**Core Features**:
- Pure Python implementation, no command-line dependencies, especially suitable for Mac users
- Complete tool suite: file read/write/edit, pure Python regex search, directory listing, shell session management
- System prompt techniques: timestamps, tool call counting, TODO list management, detailed error messages
- Persistent shell environment, automatic lint detection, streaming response support
- Supports multiple LLM providers (Anthropic, OpenAI, OpenRouter)

**Core Concepts**: Code generation, file editing, pure Python tools, system prompt, lint detection, multi-provider support

### code-for-math - Enhancing Math Problem Solving with Code
`chapter5/code-for-math/`

Compares two modes, "pure chain-of-thought" and "code-assisted", using the same model on the same set of competition math problems: the latter formalizes the problems into Python (sympy/numpy/scipy), executes them in a subprocess sandbox via function calling, and replaces error-prone mental arithmetic with precise calculations, resulting in significantly higher accuracy.

**Core Concepts**: Code interpreter, symbolic computation, chain-of-thought comparison, tool-augmented reasoning

### code-for-logic - Enhancing Logical Thinking with Code
`chapter5/code-for-logic/`

Translates "Knights and Knaves" logic puzzles into Constraint Satisfaction Problems (CSP): the Agent uses `python-constraint` to define variables and biconditional constraints and calls a solver, comparing the accuracy of pure natural language reasoning and code-assisted modes on a set of K&K puzzles.

**Core Concepts**: Constraint solving, CSP modeling, formal reasoning, code assistance

### small-model-codified-rules - Codified Rules for Small Models
`chapter5/small-model-codified-rules/`

Controlled experiments based on the τ-bench airline customer service scenario: after moving complex business policies (refund rules) from natural language prompts into code/tools, the task success rate and policy consistency of small models are significantly improved, and in-tool code validation can intercept the model's misconceptions in real time.

**Core Concepts**: Codified business rules, policy execution, in-tool validation, small model reliability

### paper-to-ppt - Automatic PPT Generation from Papers (Proposer-Reviewer)
`chapter5/paper-to-ppt/`

Reframes "making PPTs" as a code generation problem: the Proposer writes Slidev (Markdown+HTML) code, the Reviewer actually renders each page into PNG and uses a Vision LLM to check for layout issues, iterating revisions based on structured feedback; the division of labor between the two Agents significantly reduces the peak context size.

**Core Concepts**: Code generation, Slidev, Proposer-Reviewer, visual quality control

### paper-to-video - Automatic Generation of Paper Explanation Videos
`chapter5/paper-to-video/`

Building on "Paper → PPT", it generates colloquial explanation scripts for each slide, calls TTS to synthesize speech, and then uses ffmpeg to synchronously combine each page's screenshot with its audio page-by-page into a narrated explanation video.

**Core Concepts**: Multimedia generation, script generation, TTS, ffmpeg audio-video synchronization

### video-edit - API-Based Intelligent Video Editing
`chapter5/video-edit/`

Given a multi-scene video and a natural language requirement by the user, the Agent determines the time boundaries of the target scene through "two-step Vision positioning" (coarse-to-fine frame extraction and image reading). After cutting the clip, the Reviewer extracts key frames from the final video for verification, iterating if unqualified.

**Core Concepts**: Video editing, Vision positioning, coarse-to-fine, Proposer-Reviewer

### adaptive-log-parser - Adaptive Log Parsing System
`chapter5/adaptive-log-parser/`

A self-evolving log parsing system: instead of throwing errors when encountering unparseable new formats, it hands over the failed samples and errors to a code generation Agent to generate a `parse` function. After passing automated tests, it hot-updates and registers it into the parsing engine, requiring no human intervention throughout the process.

**Core Concepts**: Code as system adapter, self-healing closed loop, code hot-updating, automated testing

### log-diagnosis - Intelligent Production Log Diagnosis System
`chapter5/log-diagnosis/`

The diagnosis Agent reads production trace logs, architecture documents, and PRDs, automatically locates problems and root causes, generates structured reports and regression test cases, actually executes verification using a replay framework, and (mocks) integrating with GitHub via MCP to create Issues.

**Core Concepts**: Trace diagnosis, root cause localization, regression test generation, replay verification

### dynamic-form - Dynamic Form Intent Clarification System
`chapter5/dynamic-form/`

When facing requests with incomplete information, instead of asking follow-up questions one by one, the Agent dynamically generates a self-contained HTML form with cascading logic for the user to complete all at once; the frontend summarizes the form into JSON and hands it back to the Agent to continue the task.

**Core Concepts**: Code generation, intent clarification, dynamic forms, cascading logic

### erp-agent - Natural Language ERP Agent (NL → SQL)
`chapter5/erp-agent/`

Translates Chinese natural language queries into SQL for the database to execute and directly presents the result tables. The core is the artifact mode: the LLM only generates SQL artifacts and does not fetch data itself, which saves tokens and avoids manual calculation errors, returning tens of thousands of rows of results in seconds.

**Core Concepts**: NL2SQL, artifact mode, database execution, cost and accuracy

### conversational-ui - Conversational UI Customization System
`chapter5/conversational-ui/`

Users propose UI customization requirements (color/font/copy/layout) in natural language, the Agent autonomously locates and modifies the React frontend source code, leveraging Vite's Hot Module Replacement (HMR) to make changes take effect instantly, supporting multi-turn iterative customization.

**Core Concepts**: Code modification, frontend customization, hot reloading, multi-turn iteration

## 🎯 Chapter 6 · Agent Evaluation

### terminal-bench - Terminal Environment Benchmark
`chapter6/terminal-bench/`

Terminal-Bench is a benchmark for testing AI Agent performance in real terminal environments. From compiling code to training models and setting up servers, it evaluates how Agents handle real end-to-end tasks. Includes a dataset of about 100 tasks and an execution framework, supporting various Agent implementations.

**Core Concepts**: Terminal automation, task evaluation, Docker sandbox, benchmarking

### SWE-bench - Software Engineering Benchmark
`chapter6/SWE-bench/`

SWE-bench is a benchmark for evaluating the ability of large language models to solve real GitHub issues. Given a codebase and an issue description, the model needs to generate a patch that resolves the issue. Includes multiple versions: SWE-bench, SWE-bench Lite, SWE-bench Verified, and SWE-bench Multimodal.

**Core Concepts**: Code repair, GitHub issues, patch generation, Docker evaluation

### GAIA - General AI Assistant Benchmark
`chapter6/GAIA/`

GAIA aims to evaluate next-generation LLMs (LLMs with augmented capabilities due to added tooling, efficient prompting, access to search, etc.). Contains 450+ non-trivial questions requiring different levels of tooling and autonomy, with unambiguous answers. Divided into 3 difficulty levels.

**Core Concepts**: Tool usage, multi-step reasoning, autonomy evaluation

### OSWorld - OS-Level Agent Benchmark
`chapter6/OSWorld/`

Evaluates the Agent's ability to execute complex tasks in a complete operating system environment, including file management, application operations, and system configuration.

**Core Concepts**: OS automation, multi-application collaboration, system-level tasks

### android_world - Android Environment Benchmark
`chapter6/android_world/` (📖 External repository, see "External Repositories Acquisition")

Evaluates Agent performance in the Android mobile environment, including app navigation, UI interaction, and task completion capabilities.

**Core Concepts**: Mobile automation, Android UI, app interaction

> `chapter6/android-world/` (hyphenated name) is not the benchmark code, but rather the book's analysis notes (`t3a*.md`) on the failure cases of the T3A Agent on android_world, which can be used as reference reading material.

### tau2-bench - Tool-Augmented Reasoning Benchmark
`chapter6/tau2-bench/`

Focuses on evaluating the Agent's ability to use tools for complex reasoning, including scenarios like computation, search, and data processing.

**Core Concepts**: Tool-augmented reasoning, multi-step tasks, tool combination

### elo-leaderboard - ELO Leaderboard System
`chapter6/elo-leaderboard/`

Implements an Agent performance leaderboard based on the ELO rating system, evaluating the relative capabilities of different Agents through head-to-head comparisons.

**Core Concepts**: ELO rating, relative evaluation, leaderboard system

### model-benchmark - Multi-Dimensional Model Performance Benchmark
`chapter6/model-benchmark/`

Conducts a horizontal benchmark test on multiple OpenAI-compatible LLM API providers, accurately measuring Time To First Token (TTFT) using streaming interfaces, and measuring end-to-end latency percentiles (p50/p95), throughput, and success rates under concurrency. A single command generates a multi-dimensional comparison table, illustrating that model selection is a multi-dimensional trade-off rather than just looking at leaderboards.

**Core Concepts**: TTFT, latency percentiles, throughput, concurrency stress testing, model selection

### agent-cost-analysis - End-to-End Agent Task Cost Analysis
`chapter6/agent-cost-analysis/`

Performs a full-link cost breakdown of typical multi-turn Agent tasks (customer service refunds): uses a self-built lightweight tracing to record the input/output/cached tokens, latency, and cost of each LLM call, aggregating "which step is the most expensive", and then uses A/B testing to quantify the real savings brought by KV-cache-friendly design + context compression.

**Core Concepts**: Observability, cost breakdown, prompt caching, A/B comparison

### tts-quality-eval - Fully Automated TTS Quality Evaluation Pipeline
`chapter6/tts-quality-eval/`

Synthesizes the same set of challenging texts using various TTS configurations (different model/voice/speed), and then uses a multimodal LLM-as-a-Judge to score each dimension (clarity/naturalness, etc.) according to a Rubric, summarizing it into a reproducible configuration comparison table.

**Core Concepts**: LLM-as-a-Judge, Rubric scoring, TTS evaluation, multi-dimensional comparison

## 🧠 Chapter 7 · Model Post-Training

This chapter contains multiple model post-training projects, covering various techniques and application scenarios of Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL).

### AdaptThink - Adaptive Reasoning Depth
`chapter7/AdaptThink/` and `chapter7/AdaptThink-original/`

Teaches reasoning models to adaptively select reasoning modes (Thinking vs NoThinking) based on problem difficulty. Through constrained optimization and importance sampling, it significantly reduces reasoning costs (45-69%) while improving accuracy. Based on the DeepSeek-R1-Distill-Qwen model, trained using the DAPO algorithm.

**Core Concepts**: Adaptive reasoning, reasoning cost optimization, constrained optimization, importance sampling

### retool - Tool-Augmented Math Reasoning
`chapter7/retool/`

Uses multi-turn dialogue and code sandboxes to enhance the math reasoning capabilities of large language models. Through a two-stage training process of SFT and RL, it teaches the model to use a code execution environment to assist in solving math problems. Based on Qwen2.5-32B-Instruct, trained on the AIME 2024 dataset, using the DAPO algorithm and SandboxFusion sandbox.

**Core Concepts**: Tool usage, code execution, math reasoning, multi-turn dialogue, DAPO algorithm

### AWorld / AWorld-train - Embodied Agent Training
`chapter7/AWorld/` and `chapter7/AWorld-train/`

Trains embodied Agents based on the AWorld framework, enabling Agents to execute complex tasks in virtual environments and learn from experience.

**Core Concepts**: Embodied intelligence, environment interaction, experiential learning

### SFTvsRL - SFT vs RL Comparative Study
`chapter7/SFTvsRL/`

Systematically compares Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) across different tasks, analyzing the pros, cons, and applicable scenarios of both methods.

**Core Concepts**: SFT vs RL, training method comparison, performance analysis

### verl - Efficient RL Training Framework
`chapter7/verl/`

verl is an efficient reinforcement learning framework specifically designed for LLM RLHF training, supporting various algorithms such as PPO, GRPO, and DAPO.

**Core Concepts**: RLHF, PPO, distributed training, efficient optimization

### Intuitor - Intuitive Reasoning Training
`chapter7/Intuitor/`

Trains the model's intuitive reasoning ability, allowing the model to quickly make reasonable judgments without requiring detailed chains of thought.

**Core Concepts**: Intuitive reasoning, rapid decision-making, chain-of-thought optimization

### MultilingualReasoning - Multilingual Reasoning
`chapter7/MultilingualReasoning/`

Trains the model's reasoning capabilities in multilingual environments, improving performance on cross-lingual tasks.

**Core Concepts**: Multilingual, cross-lingual reasoning, language generalization

### SpatialReasoning - Spatial Reasoning Training
`chapter7/SpatialReasoning/`

Focuses on training the model's spatial reasoning capabilities, handling problems involving spatial relationships such as position, direction, and distance.

**Core Concepts**: Spatial reasoning, geometric understanding, positional relationships

### SimpleVLA-RL - Vision-Language-Action RL
`chapter7/SimpleVLA-RL/`

Combines vision, language, and action in reinforcement learning training, enabling the model to understand visual inputs and execute corresponding actions.

**Core Concepts**: Vision-Language-Action, multimodal RL, embodied intelligence

### continued-pretraining - Continued Pre-Training
`chapter7/continued-pretraining/`

Continues pre-training on domain-specific data to improve the model's performance in the target domain.

**Core Concepts**: Continued pre-training, domain adaptation, knowledge injection

### MiniMind-pretrain - Small Model Pre-Training
`chapter7/MiniMind-pretrain/`

Pre-trains a small language model from scratch to understand the complete workflow and key technologies of pre-training.

**Core Concepts**: Pre-training, small models, training workflow

### sesame - Sequence Modeling and Evaluation
`chapter7/sesame/`

Focuses on training and evaluation methods for sequence modeling tasks.

**Core Concepts**: Sequence modeling, evaluation methods, performance optimization

### orpheus - Music Generation and Understanding
`chapter7/orpheus/`

Trains the model's music generation and understanding capabilities.

**Core Concepts**: Music generation, audio understanding, creative AI

### tinker-cookbook - Training Tips Collection
`chapter7/tinker-cookbook/`

Collects various practical tips and best practices for model training.

**Core Concepts**: Training tips, best practices, tuning methods

## 🔄 Chapter 8 · Agent Self-Evolution

This chapter focuses on enabling Agents to continuously grow from experience without changing weights: distilling successful trajectories into reusable experience, externalizing repetitive operations into tools, and distilling prompts and observations into the model.

### gaia-experience - Learning from Successful Experience
`chapter8/gaia-experience/`

Based on the AWorld framework and the GAIA benchmark, it implements a complete "learning-application" closed loop. The Agent automatically summarizes successful task trajectories into structured experience and retrieves and applies them in new tasks, achieving self-evolution.

**Core Concepts**: Experiential learning, policy summarization, trajectory summarization, self-evolution

### browser-use-rpa - Workflow Recording and Playback
`chapter8/browser-use-rpa/`

Implements a workflow recording system for browser automation, automatically encapsulating repetitive operation sequences into parameterized tools. Achieves a 3-5x speedup by switching from expensive LLM reasoning to precise automated execution.

**Core Concepts**: Workflow recording, RPA, tool generation, externalized learning

### prompt-distillation - Prompt Distillation
`chapter8/prompt-distillation/`

Distills the effects of complex prompts into model parameters, reducing prompt length during inference and solidifying the experience in the context into parameterized knowledge.

**Core Concepts**: Knowledge distillation, prompt optimization, parameterized knowledge

### prompt-auto-optimization - Automatic System Prompt Optimization
`chapter8/prompt-auto-optimization/`

Automated system prompt learning based on human feedback: taking the "over-transfer" problem in a tau-bench style airline customer service scenario as an example, it lets a Coding Agent read the system prompt file, locate problematic rules, generate precise modifications, and actually rewrite the prompt file, then re-evaluates to verify, forming a "feedback → rewrite → verify" closed loop.

**Core Concepts**: Automatic prompt optimization, human feedback, Coding Agent, closed-loop evaluation

### active-tool-discovery - Active Tool Discovery
`chapter8/active-tool-discovery/`

Compares two paradigms: "full injection of 120+ tool schemas" vs "active on-demand discovery". The latter only keeps a few basic tools + a `discover_tools` meta-tool in the system, using embedding similarity to retrieve 3-5 most relevant specialized tools from the tool library, which saves tokens and avoids the model misselecting/abusing general tools under excessively long tool lists.

**Core Concepts**: Active tool discovery, embedding retrieval, token optimization, instruction following

### self-evolving-tools - Self-Evolution by Finding Tools from the Web
`chapter8/self-evolving-tools/`

Alita-style "minimal predefinition, maximum self-evolution": the Agent does not preset any domain tools, only five general meta-tools. When encountering tasks it cannot do, it searches for open-source libraries/APIs online, reads documentation, tests in a sandbox, encapsulates feasible solutions into new tools to store in the tool library and reuses them, emphasizing hallucination control throughout the process.

**Core Concepts**: Self-evolution, tool creation, tool reuse, hallucination control

### self-evolution-eval - Self-Evolving Agent Evaluation Dataset
`chapter8/self-evolution-eval/`

A dedicated dataset and validation method designed to evaluate the "self-evolution" capability of Agents (discovering, creating, and reusing tools on their own): 20 cross-domain tasks (without hinting at tool names) + a four-layer hierarchical validation harness + controllable reference Agents, going beyond "is the result correct" to examine the quality of discovery, creation, and reuse.

**Core Concepts**: Evaluation dataset design, hierarchical validation, tool reuse metrics, self-evolution

## 🎙️ Chapter 9 · Multimodality and Real-Time Interaction

### live-audio - Real-Time Voice Conversation
`chapter9/live-audio/`

Real-time voice chat demo, integrating speech-to-text, AI dialogue, and text-to-speech functions. Supports multiple AI service providers (OpenAI, OpenRouter, ARK, Siliconflow), providing a low-latency conversation experience.

**Core Features**:
- Real-time voice input and VAD (Voice Activity Detection)
- Multi-provider support: ASR (OpenAI Whisper, SenseVoice), LLM (GPT-4o, Gemini, Doubao), TTS (Fish Audio)
- WebSocket real-time communication, low-latency audio streaming
- Real-time latency monitoring and logging

**Core Concepts**: Speech recognition, real-time conversation, TTS, WebSocket, multi-provider architecture

### browser-use - Browser Automation Agent (Computer Use)
`chapter9/browser-use/`

Browser-Use is a powerful browser automation framework that enables LLMs to control browsers to complete complex tasks. Supports scenarios like form filling, web navigation, and data extraction, and is a typical implementation of GUI automation (Computer Use).

**Core Features**:
- LLM-driven browser automation
- Supports multiple LLMs (ChatBrowserUse, OpenAI, Google, local models)
- Custom tool extensions, authentication handling
- Sandbox deployment support, cloud service integration

**Core Concepts**: Browser automation, Computer Use, visual understanding, tool extension

### claude-quickstarts - Claude Quickstarts
`chapter9/claude-quickstarts/`

Quickstart examples and best practices for the Claude API, covering various usage scenarios.

**Core Concepts**: Claude API, prompt engineering, best practices

### phone-agent - Phone Agent
`chapter9/phone-agent/`

Demonstrates a voice Agent "making phone calls with the external world on behalf of the user": the upper layer is a standard ReAct Agent, which figures out the number and call objective after receiving a natural language task, calls the `make_phone_call` tool (based on telephone voice API abstraction) to complete the entire call, reads the structured call record and asks follow-up questions to redial if necessary, and finally reports to the user.

**Core Concepts**: Voice Agent, telephone interaction, ReAct, tool abstraction

### end-to-end-speech - End-to-End Speech Thinking vs Cascaded Pipeline
`chapter9/end-to-end-speech/`

Corresponds to the end-to-end speech thinking paradigm of Step-Audio R1 (a single model "listens → thinks → speaks"): runs through the "voice input → thinking → voice output" closed loop, and intuitively compares the latency and loss of paralinguistic information (emotion/tone/speed) with the ASR→LLM→TTS cascaded paradigm.

**Core Concepts**: End-to-end speech, cascaded comparison, paralinguistic information, thinking while speaking

### streaming-speech - Simulated Streaming Speech Perception
`chapter9/streaming-speech/`

Demonstrates the core trade-offs of streaming speech perception: feeds continuous audio in chunks of increasing length to the ASR, producing a "current partial recognition result" upon receiving each small segment to output text as early as possible with extremely low first-packet latency. The cost is that early chunks may be wrong due to the lack of subsequent context, gradually converging as audio accumulates, contrasting with the high accuracy/high latency of "waiting for the whole sentence to arrive before recognizing".

**Core Concepts**: Streaming perception, chunked recognition, first-packet latency, premature decision cost

### controllable-tts - Control Token-Driven Controllable TTS
`chapter9/controllable-tts/`

Makes the main LLM's output carry control tokens (emotion/speed/style/pause/laughter), the execution layer parses the tokens and maps them to the corresponding style profiles in the reference voice library to synthesize speech, handing over the decision of "where to pause and what tone to use" to the LLM. The same text can be synthesized into different styles and emotions.

**Core Concepts**: Controllable TTS, control tokens, reference voice library, prosody control

## 🤝 Chapter 10 · Multi-Agent Collaboration

### use-computer-while-calling - Dual Agent Architecture
`chapter10/use-computer-while-calling/` (📖 Complete code has been independently separated into [19PINE-AI/TalkAct](https://github.com/19PINE-AI/TalkAct), this directory only retains the documentation)

Implements a dual-Agent collaboration architecture for a phone call Agent and a computer use Agent. The two Agents communicate directly via WebSocket without a coordinator. The phone Agent handles voice interactions, and the computer Agent executes browser automation, working in parallel to complete complex tasks requiring both voice and web operations.

**Core Features**:
- Direct inter-Agent communication (no coordinator)
- Standard tool calls for message passing
- Parallel operations: voice conversation + browser automation
- Simple JSON message protocol

**Architecture Components**:
- Phone Call Agent (Node.js): Voice I/O, ASR/TTS, LLM dialogue
- Computer Use Agent (Python): Browser automation, browser-use, web scraping
- WebSocket communication: Direct message passing between Agents

**Core Concepts**: Multi-Agent collaboration, inter-Agent communication, parallel task processing, voice+browser integration

### staged-system-prompt - Switching System Prompts by Execution Stage
`chapter10/staged-system-prompt/`

The same Coding Agent loads different system prompts and toolsets at different execution stages of a task (requirement clarification → code implementation → code review), thereby playing different roles and exhibiting different behaviors within a single conversation. The conversation history and task state are continuously shared across stages, and it can roll back to the implementation stage if the review fails.

**Core Concepts**: Staged prompts, role switching, shared context, stage pipeline

### multi-role-transfer - Multi-Role Transfer and Autonomous Handoff
`chapter10/multi-role-transfer/`

Demonstrates chained handoff (handoff) under shared context: multiple specialized role Agents exist in a single session, each with independent system prompts and dedicated toolsets. Through the `transfer_to_agent` tool, the Agent autonomously judges which role to switch to based on task progress; because the same conversation history is shared, the complete context is naturally retained during the handoff.

**Core Concepts**: Role handoff, handoff, shared context, autonomous switching

### book-translation - Book Translation Agent (Manager Mode)
`chapter10/book-translation/`

Uses Manager Mode (Orchestration) to distribute long document translation to specialized Agents like glossary/translation/proofreading: the Manager only saves tasks, plans, call records, and file indexes, and the complete translations are all saved to disk, so the context remains basically constant. It also compares the single-Agent solution, using real token counts to illustrate how to control context inflation and ensure consistency across the book using a shared glossary.

**Core Concepts**: Manager mode, context isolation, context inflation control, shared glossary

### parallel-web-research - Parallel Multi-Source Information Gathering Agent
`chapter10/parallel-web-research/`

Demonstrates parallel search + central coordination of multiple homogeneous Agents: the main coordinator simultaneously starts N sub-Agents to each visit a source to find the answer, and once one hits the target, the others gracefully stop immediately. Message bus, parallel dispatch, real-time monitoring, cascading termination, and race condition handling are all real implementations (using controllable simulated information sources instead of real browsers).

**Core Concepts**: Parallel Agents, central coordination, message bus, cascading termination

### voice-werewolf - Voice Werewolf Agent System
`chapter10/voice-werewolf/`

Uses multi-Agent Werewolf to demonstrate information permission control under "unshared context": each player is an independent LLM Agent and maintains strictly isolated private context. A code-driven deterministic judge decides which player contexts each piece of information is delivered to and registers it for auditing. The game automatically verifies whether the isolation is correct when it ends. Voice is an optional enhancement.

**Core Concepts**: Information asymmetry, private context isolation, judge orchestration, audit verification

## 📖 Learning Recommendations

### Core Concept: Agent = Model + Context + Tools

The core framework of this book is **Agent = Model + Context + Tools**. These three components collaborate to realize the intelligent behavior of the Agent:

- **Model**: The brain of the Agent, providing understanding, reasoning, and decision-making capabilities.
- **Context**: The operating system of the Agent, including system instructions, conversation history, reasoning processes, tool interaction records, etc.
- **Tools**: The hands of the Agent, enabling the Agent to perceive the environment, execute operations, and interact with the external world.

### Learning Path

The learning path corresponds one-to-one with the chapters of the book, unfolding layer by layer around the three pillars:

- **Chapter 1 · Fundamentals**: Establish a complete cognitive framework for Agent systems—understand the definition of Agents in RL, compare the sample efficiency differences between traditional RL and LLM+RL paradigms, understand the new paradigm of "Model as Agent", and master the core framework of **Agent = Model + Context + Tools**. **Key Insight**: The importance of prior knowledge surpasses algorithms and environments.

- **Chapters 2–3 · Context**: Context is the operating system of the Agent. Chapter 2 covers system prompts, KV Cache-friendly design, context compression, and prompt engineering ablation; Chapter 3 covers user memory, dense/sparse/hybrid retrieval, Agentic RAG, contextual retrieval, and structured knowledge extraction. **Key Insight**: Complete context includes system instructions, conversation history, reasoning processes, tool interaction records, user memory, and external knowledge.

- **Chapters 4–5 · Tools**: Tools are the bridge for Agents to interact with the world. Chapter 4 covers three categories of MCP tools (perception/execution/collaboration), event triggers, and asynchronous architectures; Chapter 5 delves into the complete implementation of production-grade Coding Agents. **Key Insight**: Tool design should be generalized (code interpreters are better than calculators), and code is the meta-capability to create new tools.

- **Chapters 6–7 · Models**: How to measure and amplify intelligence. Chapter 6 covers evaluation benchmarks like Terminal-Bench, SWE-bench, GAIA, OSWorld, and Tau2-Bench; Chapter 7 covers post-training techniques like SFT, RL, RLHF, and sample efficiency. **Key Insight**: Independent verification signals are more reliable than "letting the model think again"; "Model as Agent" internalizes tool calling as a native capability through RL.

- **Chapter 8 · Self-Evolution**: Enabling Agents to grow from experience without changing weights—experiential learning, externalizing workflows into tools, and distilling prompts and observations into parameters. **Key Insight**: Learning from experience is the key to taking Agents from "smart" to "proficient".

- **Chapters 9–10 · Expansion and Collaboration**: Chapter 9 expands perception and action from text to speech, GUIs, and the physical world; Chapter 10 handles complex tasks through multi-Agent division of labor and collaboration. **Key Insight**: Every design decision in a multi-Agent system can find a correspondence in the three elements of a single Agent.

### Difficulty Levels

- **Beginner** (Chapters 1–2): Suitable for beginners, understanding basic concepts.
- **Intermediate** (Chapters 3–4): Requires some programming foundation, involving system integration.
- **Advanced** (Chapters 5–6): Requires strong programming skills, involving complex system design.
- **Expert** (Chapters 7–8): Requires deep learning and training/self-evolution experience.
- **Applied** (Chapters 9–10): Comprehensively applies what has been learned to build practical applications.

### Practical Recommendations

1. **Hands-on Practice**: Every project is designed to be independently runnable; it is recommended to run and modify the code yourself.
2. **Combine with the Book**: Read along with the corresponding chapters in the [`book/`](book/) directory of this repository to understand the combination of theory and practice.
3. **Experimental Comparison**: Multiple projects contain ablation studies and comparative experiments; deepen your understanding through comparison.
4. **Progressive Learning**: Start with simple projects and gradually delve into complex systems.
5. **Focus on Protocols**: The MCP server projects in Chapter 4 demonstrate standardized tool protocols, which are key to building scalable Agents.

## 🔑 API Keys

It is recommended to apply for API keys from a few platforms to facilitate learning:
- **Kimi**: https://platform.moonshot.cn/ Moonshot's Kimi series, strong in long context and Agent capabilities.
- **Zhipu GLM**: https://open.bigmodel.cn/ Zhipu AI's GLM series (GLM-4.6, etc.), strong in Chinese, high cost-performance ratio, also highly recommended.
- **Siliconflow**: https://siliconflow.cn/ Features various open-source models, including DeepSeek, Qwen, etc.
- **Volcengine**: https://www.volcengine.com/product/ark Features ByteDance's closed-source models (Doubao), with low access latency in China.
- **OpenRouter**: https://openrouter.ai/ Allows direct access to various closed-source and open-source models overseas from within China, including Gemini 2.5 Pro, Claude 4 Sonnet, OpenAI GPT-5, etc. (The official API requires overseas IPs and payment methods, and OpenAI also requires overseas real-name authentication, making registration relatively troublesome).

Model selection can be referenced here: https://01.me/2025/07/llm-api-setup/

## 📦 Appendix · External Repositories Acquisition

Due to size and copyright considerations, the evaluation benchmarks and training frameworks used in Chapters 6, 7, and 9 are **not included** in this repository and need to be cloned into the corresponding directories manually (below are the upstream addresses and commits verified by this book). You can save the following commands as a script to pull them all at once:

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

> If a specific commit is noted in the README of each project, please `git checkout` to the corresponding version as instructed to ensure consistent reproduction results.
> Chapter 10 `use-computer-while-calling` has evolved into a continuously maintained independent repository [19PINE-AI/TalkAct](https://github.com/19PINE-AI/TalkAct); this repository only retains a documentation file pointing to it (`chapter10/use-computer-while-calling/README.md`).

**Experiments relying on real hardware / external environments (no code in this repository, pointing to upstream documentation):**

- **Experiment 9-8 / 9-9 · XLeRobot Teleoperation and LLM Agent Control**: Requires SO-100/XLeRobot robotic arm, operate according to upstream documentation —— [Teleop](https://xlerobot.readthedocs.io/en/latest/software/getting_started/XLeRobot_teleop.html) · [LLM Agent](https://xlerobot.readthedocs.io/en/latest/software/getting_started/LLM_agent.html)
- **Experiment 9-10 · RGB Zero-Shot Sim2Real Grasping**: [`StoneT2000/lerobot-sim2real`](https://github.com/StoneT2000/lerobot-sim2real) (The simulation training part can be completed purely on GPU, real deployment requires SO-100 robotic arm)
- **Experiment 6-11 · OpenVLA + RoboTwin2 Simulation Evaluation**: VLA training/environment dependencies see the README of `chapter7/SimpleVLA-RL` (which explains the acquisition and configuration of OpenVLA and RoboTwin2)

**Reader exercise experiments (provided as exercises in the book, reusing existing documented projects, no dedicated directory):**

- **Experiment 5-12 · Agent that creates Agents**: Bootstrapped extension based on `chapter5/coding-agent`
- **Experiment 6-2 / 6-3 / 6-4 / 6-9**: Respectively manual benchmark, memory evaluation, JSON Cards vs RAG, memory selection—refactoring and reusing projects like `user-memory` / `user-memory-evaluation` / `contextual-retrieval` from Chapter 3
- **Experiment 7-8 · Prompt Distillation**: Implementation落地 sees Chapter 8 `chapter8/prompt-distillation` (cross-chapter reuse)
- **Experiment 7-9 · CoT Distillation `[Extension]`**: The book provides experimental design and acceptance criteria as a reader extension experiment, currently no dedicated code

## 🤝 Contributing

The book and accompanying code are entirely open-source, and community participation through Pull Requests is highly welcome. We welcome the following types of contributions:

1. **Book Content Improvements**: Errata, additions, clearer expressions, or adding cutting-edge developments (see `book/chapter*.md` for the main text).
2. **Code Improvements and Bug Fixes**: Making accompanying projects more robust, easier to use, and closer to production practices.
3. **New Practical Projects**: Supplementing/replacing better implementations for an experiment, or contributing brand-new example projects.
4. **Design Improvements for Book Illustrations**: Making the charts in `book/images/` clearer and more aesthetically pleasing in design (illustrations are generated by `book/gen_*_figs.py`).

Before submitting, it is recommended to run the relevant experiments yourself to ensure reproducibility; you are also welcome to open an issue first to discuss ideas.

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE), see the [`LICENSE`](LICENSE) file for details. Some sub-projects may contain their own license information, please refer to the instructions in the sub-projects.

## ⭐ Star History

<a href="https://star-history.com/#bojieli/ai-agent-book&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/star-history-dark.png" />
    <source media="(prefers-color-scheme: light)" srcset="assets/star-history-light.png" />
    <img alt="Star History Chart" src="assets/star-history-light.png" width="720" />
  </picture>
</a>

<sub>Chart drawn by [`scripts/gen_star_history.py`](scripts/gen_star_history.py) (since July 13, 2026), [GitHub Actions scheduled task](.github/workflows/star-history.yml) automatically updates and commits to the <code>assets/</code> directory daily; click to jump to star-history.com to view real-time data.</sub>

```

