# SKILL.md: Meticulous Technical Translation

## 1. Purpose

This document serves as the definitive operational manual for executing **meticulous technical translations**. The mission is not merely to "translate documents" from one language to another. The objective is to produce publication-quality translations that preserve the source document's meaning, technical accuracy, nuance, hierarchy, rhetorical intent, formatting, and stylistic register, while reading naturally to native speakers of the target language.

This skill is designed to be universally applicable across a wide spectrum of high-stakes technical documentation, including but not limited to:

*   GitHub READMEs and Repository Wikis
*   Request for Comments (RFCs) and Design Documents
*   System Architecture Whitepapers
*   Security Advisories and Audit Reports
*   Benchmark and Performance Reports
*   API and SDK Documentation
*   Technical Blogs and Research Summaries

The principles outlined herein apply primarily to **Chinese ↔ English** translation pairs but establish a rigorous framework adaptable to any language pair requiring high technical fidelity.

---

## 2. Core Philosophy

The foundation of meticulous translation rests on a singular, uncompromising philosophy: **Translate intent rather than words, but never rewrite facts.**

A technical document is not just a collection of sentences; it is a structured transmission of precise logic, empirical evidence, and architectural reality. To achieve professional-grade output, the translator (human or AI) must adhere to a strict **Hierarchy of Preservation**. When conflicts arise between these elements, the higher priority always overrides the lower.

### The Hierarchy of Preservation

1.  **Preserve Meaning & Factual Accuracy:** The empirical truth of the source text is inviolable. Never add, omit, strengthen, or weaken a technical claim.
2.  **Preserve Technical Correctness:** Use industry-standard terminology. A "thread" is not a "process"; a "snapshot" is not a "backup".
3.  **Preserve Logical Structure:** The sequence of arguments, conditions, and caveats must remain intact.
4.  **Preserve Rhetorical Force & Tone:** If the source is authoritative, the translation must be authoritative. If it is cautionary, the translation must be cautionary.
5.  **Preserve Formatting & Hierarchy:** Markdown structures, code blocks, tables, and emphasis are part of the document's semantic payload.
6.  **Preserve Natural Readability:** The text should flow naturally in the target language. *Notice that readability is last.* It must never be achieved at the cost of accuracy, structure, or technical precision.

---

## 3. Translation Principles

To operationalize the core philosophy, the following eight principles must be strictly enforced during every translation task.

### Rule 1: Never Add Information
Do not insert explanatory notes, context, or "helpful" clarifications that do not exist in the source text. If the source assumes the reader knows what KVM is, do not add a definition of KVM.

### Rule 2: Never Omit Information
Do not summarize, condense, or drop qualifiers. If the source says "in most testing environments under 32GB," do not translate it as "in testing environments." The qualifiers are legally and technically binding.

### Rule 3: Never Weaken Certainty
If the source states a fact definitively, the translation must not introduce doubt.
*   *Source:* "This eliminates the risk."
*   *Incorrect:* "This helps reduce the risk."
*   *Correct:* "This eliminates the risk."

### Rule 4: Never Strengthen Certainty
Conversely, do not elevate a hypothesis or a probability to an absolute fact.
*   *Source:* "This approach appears to mitigate latency."
*   *Incorrect:* "This approach eliminates latency."
*   *Correct:* "This approach appears to mitigate latency."

### Rule 5: Never Normalize Terminology Mid-Document
If the author uses three different terms for the same concept, you must translate them using three corresponding terms, or establish a glossary and apply it consistently. Do not silently "fix" the author's vocabulary inconsistencies unless explicitly instructed to edit.

### Rule 6: Translate Consistently
A specific technical concept must be rendered with the exact same target-language phrase every time it appears. "Execution environment" must not become "runtime" halfway through the document.

### Rule 7: Preserve Ambiguity
If the source text is ambiguous, the translation must remain equally ambiguous. Do not resolve technical ambiguities by guessing the author's intent.

### Rule 8: Do Not "Improve" Arguments
You are a translator, not a peer reviewer. If the author's logic is flawed, their phrasing is awkward, or their argument is weak, translate the flaw, the awkwardness, and the weakness faithfully.

---

## 4. Workflow

Meticulous translation is not a single-step generation process. It is a disciplined, multi-phase pipeline. Skipping phases guarantees degradation in quality.

```text
[Phase 1] Document Analysis
    ↓
[Phase 2] Terminology Extraction
    ↓
[Phase 3] Style Calibration
    ↓
[Phase 4] Structural Preservation Mapping
    ↓
[Phase 5] Execution (Translation)
    ↓
[Phase 6] Consistency Pass
    ↓
[Phase 7] Quality Assurance (QA) Pass
```

---

## 5. Phase 1: Document Analysis

Before translating a single word, you must analyze the source document to understand its context, constraints, and intent.

**Analysis Checklist:**
*   **Document Type:** Is it an RFC, a README, a marketing whitepaper, or a post-mortem incident report?
*   **Target Audience:** Are the readers kernel developers, DevOps engineers, enterprise CTOs, or end-users?
*   **Register & Tone:** Is it academic, legal, instructional, conversational, or authoritative?
*   **Rhetorical Intent:** Is the document trying to persuade, instruct, warn, or report?
*   **Evidence Style:** Does the author rely on benchmarks, logical proofs, citations, or anecdotal evidence?
*   **Document Hierarchy:** How are headings, lists, and code blocks used to structure the argument?
*   **Repetition:** Are there recurring motifs, catchphrases, or structural patterns?
*   **Formatting Constraints:** Are there strict Markdown requirements, table alignments, or specific inline code styles?

---

## 6. Phase 2: Terminology Extraction

Never begin translating without first building a localized glossary. This prevents "terminology drift" and ensures domain accuracy.

Create a mental or explicit table mapping source terms to target terms, explicitly noting forbidden translations.

**Example Glossary Format:**

| Source Term | Preferred Translation | Context / Nuance | Forbidden Translation |
| :--- | :--- | :--- | :--- |
| 执行环境 | execution environment | Refers to the infrastructure layer | runtime, execution context |
| 硬件隔离 | hardware isolation | Refers to VT-x/AMD-V boundaries | physical separation |
| 内核逃逸 | kernel escape | Security vulnerability context | core breakout |
| 常驻内存 | resident memory | Memory actively held by the process | static memory |
| 快照 | snapshot | Point-in-time state capture | backup, image |
| 宿主机 | host machine | The physical or primary VM layer | master server, parent |
| 裸金属 | bare-metal | Direct hardware access without hypervisor | raw metal |

*Rule:* If a term has a universally accepted industry standard in the target language, use it. If it is a novel concept introduced by the author, translate it descriptively and consistently.

---

## 7. Phase 3: Style Calibration

Different technical documents require distinct stylistic registers. You must calibrate your output to match the expected conventions of the target document type.

*   **Architecture Guides / RFCs:** Formal, objective, precise. Use passive voice where appropriate to emphasize the system over the actor. Avoid colloquialisms.
*   **GitHub READMEs:** Instructive, welcoming but professional. Use imperative mood for installation steps (e.g., "Run the script," not "You should run the script").
*   **Security Advisories:** Urgent, unambiguous, highly structured. Use stark, definitive language regarding vulnerabilities and mitigations.
*   **Benchmark Reports:** Empirical, statistical, neutral. Focus heavily on exact phrasing for metrics (e.g., "P99 latency," "throughput," "overhead").
*   **Technical Blogs:** Engaging, slightly conversational, narrative-driven. Allow for more idiomatic expressions while maintaining technical accuracy.

---

## 8. Phase 4: Structural Preservation

In technical documentation, **structure is semantics**. A change in formatting can alter the meaning of a technical instruction.

**Preservation Mandates:**
*   **Markdown Headings:** Never change an `H2` to an `H3`. The hierarchy defines the document outline.
*   **Tables:** Preserve column counts, alignment markers (`:---`, `:---:`, `---:`), and header structures.
*   **Lists:** Maintain exact nesting levels. A sub-bullet in the source must be a sub-bullet in the target. Do not convert bulleted lists to numbered lists unless the source implies strict sequential order.
*   **Blockquotes:** Retain `>` for quoted claims, citations, or terminal output.
*   **Horizontal Rules:** Retain `---` or `***` exactly where they appear to denote section breaks.
*   **Code Blocks:** Never translate code, CLI commands, variable names, or JSON/YAML keys. Only translate code *comments* if they exist and are in the source language.
*   **Inline Code:** Preserve backticks `` ` ``. Do not translate the contents inside backticks (e.g., `` `install.sh` `` remains `` `install.sh` ``, not `` `installation script` ``).
*   **Links:** Preserve Markdown link syntax `[Text](URL)`. Translate the `Text` but never the `URL`.
*   **Emphasis:** If the source uses **bold** for emphasis, use **bold**. Do not swap it for *italics* or `code`.

---

## 9. Phase 5: Execution (Translation)

During the actual translation, you must constantly navigate between four modes of translation. Technical documentation overwhelmingly favors **Faithful Translation**.

1.  **Literal Translation:** Word-for-word. *Use only for strict legal contracts or highly constrained UI strings.* Often results in poor readability in technical docs.
2.  **Faithful Translation:** Meaning-for-meaning, preserving syntax and structure where possible, but adapting grammar to target language rules. *This is the default mode for technical documentation.*
3.  **Idiomatic Translation:** Prioritizes target-language naturalness over structural fidelity. *Use for marketing materials or high-level executive summaries.*
4.  **Adaptive Translation:** Rewriting the concept entirely for a different cultural context. *Never use this in technical documentation.*

**Execution Strategy:**
Read the source sentence. Extract the logical payload (Who did what, under what conditions, with what result?). Formulate the target sentence using the glossary terms. Verify the logical payload matches. Adjust syntax for target-language flow.

---

## 10. Phase 6: Consistency Pass

Human translators and LLMs both suffer from "synonym drift"—the unconscious tendency to use different words for the same concept to avoid sounding repetitive. In technical writing, repetition is a feature, not a bug.

**Consistency Checks:**
*   Did "execution environment" become "runtime" in paragraph 4?
*   Did "claim" become "assertion" or "statement" later in the text?
*   Did "verification" become "validation"? (Note: Verification = "Did we build the thing right?" Validation = "Did we build the right thing?". They are not interchangeable).
*   Did "sandbox" become "container" or "isolation zone"?

*Action:* Perform a mental string-replace check across the entire document to ensure glossary terms are applied with 100% consistency.

---

## 11. Phase 7: Quality Assurance (QA) Pass

The final pass is a ruthless, checklist-driven audit of the translated output against the source.

**The Localization QA Checklist:**
*   [ ] **Missing Numbers:** Are all integers, floats, and percentages present?
*   [ ] **Units:** Are units (ms, MB, GB, cores) identical and correctly formatted?
*   [ ] **Versions:** Are version numbers (e.g., v0.5.0, 24.04.4) unchanged?
*   [ ] **Filenames/Paths:** Are paths (`/data/cubelet`) and filenames (`install.sh`) untranslated and intact?
*   [ ] **Markdown Integrity:** Are all bolding, italics, code blocks, and links correctly closed and formatted?
*   [ ] **Table Alignment:** Do tables render correctly without broken pipes `|`?
*   [ ] **Capitalization:** Are product names and acronyms capitalized correctly according to target language conventions?
*   [ ] **Notes/Callouts:** Are "Note:", "Warning:", or "【User Note】" markers preserved?
*   [ ] **List Nesting:** Are multi-level lists indented correctly?
*   [ ] **Orphaned Punctuation:** Are there stray commas or periods outside of code blocks?

---

## 12. Handling Technical Terminology

Technical terminology requires a binary decision matrix: **Translate the Concept** vs. **Retain the Original**.

### When to Retain the Original (Do Not Translate)
*   **Industry Standards:** Linux, Docker, Kubernetes, KVM, RustVMM, BIOS, UEFI, x86_64, ARM64, aarch64, REST, gRPC.
*   **File Formats & Protocols:** JSON, YAML, XML, HTTP, SSH, TLS, XFS, Ext4, ioctl.
*   **Specific Commands & APIs:** `FICLONE`, `vmlinux`, `reflink`, `O(1)`.
*   **File Extensions:** `.md`, `.sh`, `.py`.

### When to Translate the Concept
*   **General Infrastructure:** 宿主机 (host machine), 虚拟机 (virtual machine), 容器 (container), 沙箱 (sandbox).
*   **Architectural Patterns:** 嵌套虚拟化 (nested virtualization), 写时复制 (copy-on-write), 硬件隔离 (hardware isolation).
*   **Metrics:** 冷启动 (cold start), 常驻内存 (resident memory), 吞吐量 (throughput), 延迟 (latency).

*Rule of Thumb:* If a developer would type the English word into a search engine or terminal, retain the English word. If it is a descriptive architectural concept, translate it.

---

## 13. Handling Product Names

Product names, project names, and branded features are proper nouns. **Never translate them** unless the parent company has explicitly released an official, localized brand name for the target market.

*   **Correct:** CubeSandbox, CubeCoW, AutoPause, AutoResume, E2B SDK, Tencent Cloud.
*   **Incorrect:** 立方体沙箱, 立方体写时复制, 自动暂停, E2B软件开发包.

*Exception:* If the product name is a generic descriptive phrase in the source language (e.g., "腾讯云" -> "Tencent Cloud"), apply standard proper noun capitalization rules in the target language.

---

## 14. Handling Numbers and Metrics

Numbers in technical documents are empirical data points. They are not subject to localization or stylistic preference.

**Strict Preservation Rules:**
*   **Units:** Never convert units (e.g., do not change MB to GB, or ms to seconds) unless explicitly requested. Keep `<60ms` as `<60ms`.
*   **Precision:** Do not round numbers. `67ms` is not `about 70ms`.
*   **Ranges & Inequalities:** Preserve `<`, `>`, `≤`, `≥`, and `~`. `<5MB` must remain `<5MB`.
*   **Scientific Notation:** Keep `10^6` or `1e6` exactly as formatted.
*   **Percentiles:** `P95` and `P99` are standard statistical terms. Do not translate them to "95th percentile" unless the source explicitly used the long-form phrase.
*   **Dates:** Preserve the format or adapt to target locale standard *only if* it doesn't cause ambiguity (e.g., 2026年7月3日 -> July 3, 2026).
*   **Hardware Specs:** `96-core` remains `96-core`. `32GB` remains `32GB`.

---

## 15. Handling Tables

Tables are highly structured data matrices. Breaking the structure destroys the data.

1.  **Headers:** Translate the header text, but preserve the alignment markers (`| :--- | :---: | ---: |`).
2.  **Markdown Pipes:** Ensure every row has the exact same number of `|` characters as the header.
3.  **Checkmarks & Emojis:** Preserve `✅`, `❌`, `⚠️` exactly. They serve as visual data points.
4.  **Code inside Tables:** If a table cell contains inline code (e.g., `install.sh`), retain the backticks.
5.  **Line Breaks:** Avoid introducing raw line breaks inside a table cell, as this breaks Markdown rendering. Use `<br>` if absolutely necessary, but prefer keeping cells on a single line.

---

## 16. Handling Markdown

Markdown is the presentation layer of the document. Treat Markdown syntax as immutable code.

*   **Headings:** Preserve the exact number of `#` symbols.
*   **Bold/Italics:** `**text**` must remain `**text**`. Do not change it to `*text*`.
*   **Links:** `[Display Text](url "Title")` -> Translate `Display Text` and `Title`, never `url`.
*   **Images:** `![Alt Text](image.png)` -> Translate `Alt Text`.
*   **Blockquotes:** Ensure the `>` symbol is present on every line of a multi-line blockquote.
*   **Horizontal Rules:** Preserve `---` or `***` on its own line with empty lines above and below.

---

## 17. Handling Tone and Evaluation Language

Technical reports often contain evaluation language (words that judge the quality, certainty, or success of a claim). Translating these requires precise mapping to maintain the author's exact level of confidence.

### The Tone Lexicon (Chinese → English)

| Source Phrase | Correct Translation | Incorrect / Altered Translation | Reason |
| :--- | :--- | :--- | :--- |
| 准确描述了 | accurately describes | perfectly describes | "Perfectly" overstates the claim. |
| 得到证实 | confirmed | proven | "Proven" implies mathematical absolute; "confirmed" fits empirical testing. |
| 具有高度可信度 | highly credible | indisputably true | Maintains professional objectivity. |
| 广泛讨论 | widely discussed | universally accepted | "Universally" is a factual overreach. |
| 一致确认 | consistently confirmed | unanimously proven | "Consistently" refers to data alignment, not human voting. |
| 交叉验证 | cross-validated | double-checked | "Cross-validated" is the correct statistical/scientific term. |
| 成立 | Confirmed | Valid / True / Correct | "Confirmed" is the standard verdict for hypothesis/testing claims. |
| 核心矛盾 | core challenge / trilemma | core contradiction | "Contradiction" implies a logical error; "challenge" implies an engineering hurdle. |

---

## 18. Chinese → English Guidelines

Translating from Chinese to English requires bridging the gap between **Parataxis (意合)** and **Hypotaxis (形合)**.

1.  **Parataxis vs. Hypotaxis:** Chinese relies on logical flow and context, often omitting conjunctions and subjects. English relies on explicit grammatical structures, conjunctions, and pronouns. You must supply the missing subjects ("it", "the system", "developers") and conjunctions ("because", "although", "which") to make the English grammatically sound.
2.  **Verb Preference:** Chinese frequently uses nouns or adjectives as verbs (e.g., "进行验证" - conduct verification). English prefers strong, direct verbs. Translate "进行验证" simply as "verify" or "validate".
3.  **Nominalization:** Avoid excessive nominalization inherited from Chinese bureaucratic or academic writing.
    *   *Source:* 实现了启动速度的优化 (Achieved the optimization of startup speed).
    *   *Target:* Optimized startup speed. (Not: Achieved the optimization of...)
4.  **Information Order:** Chinese often presents the condition, context, and evidence *before* the main conclusion. English often prefers the conclusion first, followed by the context. However, in strict technical verification reports, preserve the source's logical flow (Evidence -> Conclusion) to maintain the rhetorical build-up.
5.  **Subjectless Sentences:** Chinese technical docs often drop the subject.
    *   *Source:* 必须将 `/data` 挂载为 XFS。
    *   *Target:* The `/data` directory must be mounted on an XFS filesystem. (Passive voice is appropriate here).

---

## 19. English → Chinese Guidelines

Translating from English to Chinese requires avoiding "Translationese" (翻译腔) and adhering to native technical writing conventions.

1.  **Avoid Long Attributive Clauses:** English uses long "which/that" clauses. Chinese cannot stack 30 words of adjectives before a noun. Break long sentences into shorter, logical clauses.
2.  **Use Four-Character Idioms (四字格) Appropriately:** Chinese technical writing benefits from the rhythm and conciseness of four-character phrases, but only where they fit naturally.
    *   *Example:* "High availability and fault tolerance" -> "高可用与容错" (Good). "无缝迁移" (Seamless migration). "硬件隔离" (Hardware isolation).
3.  **Punctuation Conventions:**
    *   Use full-width punctuation (，。；：！？) for prose.
    *   Use half-width punctuation (, . ; : ! ?) *inside* code blocks, inline code, and when directly adjacent to English words/numbers to prevent ugly spacing.
    *   *Example:* 版本 `v0.5.0` 引入了 AutoPause。 (Space between Chinese and English/code is standard practice in modern Chinese technical typography).
4.  **Passive Voice:** English uses passive voice heavily ("The memory is allocated by..."). Chinese prefers active voice or subjectless structures ("由...分配内存" or simply "分配内存"). Avoid the "被" (bèi) structure unless describing a negative event (e.g., "被攻击" - attacked).
5.  **Product Names:** Keep English product names in English. Do not write "库伯内提斯" for Kubernetes. Write "Kubernetes".

---

## 20. Common Mistakes and Failure Modes

Awareness of common failure modes is critical for QA. Avoid these at all costs:

1.  **Over-Literal Translation:** Translating idioms or structural quirks word-for-word, resulting in unreadable target text.
2.  **Over-Localization:** Translating product names, standard protocols, or CLI commands that should have been left in English.
3.  **Over-Editing / "Improving":** Rewriting the author's architecture or fixing their logical errors. You are a mirror, not an editor.
4.  **Summarization:** Condensing a dense technical paragraph into a brief overview. Every technical caveat must survive.
5.  **Hallucinated Clarification:** Adding "For example, like Docker..." when the source didn't mention Docker.
6.  **Dropped Qualifiers:** Missing words like "typically", "in most cases", "up to", or "less than".
7.  **Inconsistent Terminology:** Using "VM" in paragraph 1, "Virtual Machine" in paragraph 2, and "Instance" in paragraph 3 for the exact same concept.
8.  **Reordered Arguments:** Changing the sequence of a troubleshooting list, which might break chronological dependencies.
9.  **Changing Certainty:** Turning "may cause" into "causes", or "is designed to" into "does".
10. **Breaking Markdown:** Forgetting to close a bold tag `**`, or breaking a table by missing a pipe `|`.
11. **Translating Filenames/Paths:** Changing `/etc/cube/config.yaml` to `/etc/cube/配置.yaml`.
12. **Translating Code:** Translating variable names inside a Python or Bash snippet.

---

## 21. Translation Decision Framework

When faced with a complex sentence or ambiguous term, do not rely on intuition. Run the text through this deterministic decision tree:

**Step 1: Meaning & Fact Check**
*   *Question:* Does my translation alter the empirical truth or technical scope of the source?
*   *Action:* If YES -> Reject and rewrite. If NO -> Proceed.

**Step 2: Evidence & Qualifier Check**
*   *Question:* Have I preserved all conditions, thresholds, and statistical qualifiers?
*   *Action:* If NO -> Add them back. If YES -> Proceed.

**Step 3: Terminology Check**
*   *Question:* Is this term in my glossary? Am I using the exact preferred translation?
*   *Action:* If NO -> Correct to glossary standard. If YES -> Proceed.

**Step 4: Structure & Formatting Check**
*   *Question:* Does the Markdown structure, list nesting, and emphasis match the source exactly?
*   *Action:* If NO -> Fix formatting. If YES -> Proceed.

**Step 5: Tone & Register Check**
*   *Question:* Does the evaluation language match the author's level of certainty? Is the register appropriate for the document type?
*   *Action:* If NO -> Adjust tone lexicon. If YES -> Proceed.

**Step 6: Readability & Flow Check**
*   *Question:* Does this read like it was originally written by a native-speaking domain expert?
*   *Action:* If NO -> Refine syntax and grammar (without violating Steps 1-5). If YES -> **Approve.**

---

## 22. Quality Checklist (The Acceptance Test)

Before finalizing any translation output, verify it against this exhaustive checklist. A single failure requires revision.

*   [ ] **Factual Integrity:** No facts added, omitted, strengthened, or weakened.
*   [ ] **Terminology:** Glossary applied with 100% consistency. No synonym drift.
*   [ ] **Product Names:** All proprietary names, protocols, and tools retained in original language.
*   [ ] **Numbers & Units:** All metrics, versions, dates, and hardware specs exactly match source.
*   [ ] **Code & Paths:** Filenames, directories, CLI commands, and code blocks completely untranslated.
*   [ ] **Markdown Syntax:** Headings, bold/italics, links, and tables structurally perfect.
*   [ ] **List Nesting:** Bullet points and numbered lists maintain exact hierarchy.
*   [ ] **Tone:** Evaluation language accurately reflects source certainty and rhetorical intent.
*   [ ] **Grammar:** Target language syntax is correct, professional, and free of "translationese".
*   [ ] **Completeness:** Every paragraph, sentence, and footnote from the source is present.

---

## 23. Example Workflow

To illustrate the meticulous translation process, observe how a single complex sentence is processed through the phases.

**Source Text:**
> 基于对GitHub仓库README.md的深入分析及广泛的网络搜索验证，以下是对“CubeSandbox Architecture & Deployment Guide”中各项核心声明的详细验证报告。

**Phase 1: Analysis**
*   *Type:* Introduction to a Verification Report.
*   *Tone:* Formal, objective, authoritative.
*   *Key Elements:* GitHub, README.md, CubeSandbox Architecture & Deployment Guide.

**Phase 2: Terminology**
*   深入分析 -> in-depth analysis
*   广泛的网络搜索验证 -> extensive cross-verification through publicly available sources (Avoid literal "web search", use professional phrasing).
*   核心声明 -> core claims
*   验证报告 -> verification report

**Phase 3: Style Calibration**
*   Must sound like a professional technical auditor writing an executive summary.

**Phase 4: Structural Preservation**
*   Single paragraph. Contains a specific document title in quotes. Markdown blockquote context (implied by surrounding text).

**Phase 5: Execution (Drafting)**
*   *Draft 1 (Literal):* Based on in-depth analysis of GitHub repository README.md and extensive web search verification, the following is a detailed verification report of each core claim in "CubeSandbox Architecture & Deployment Guide".
*   *Critique 1:* "web search verification" sounds amateur. "each core claim" is slightly clunky.
*   *Draft 2 (Refined):* Based on an in-depth analysis of the GitHub repository's README.md and extensive cross-verification through publicly available sources, the following is a detailed verification report of the core claims presented in the **CubeSandbox Architecture & Deployment Guide**.

**Phase 6: Consistency**
*   Checked "verification" vs "validation". "Verification" is correct here.
*   Checked "core claims". Consistent with glossary.

**Phase 7: QA**
*   `README.md` preserved.
*   Document title preserved.
*   Grammar is natural and professional.

**Final Output:**
> Based on an in-depth analysis of the GitHub repository's **README.md** and extensive cross-verification through publicly available sources, the following is a detailed verification report of the core claims presented in the **CubeSandbox Architecture & Deployment Guide**.

---

## 24. Success Criteria

A translation produced using this `SKILL.md` is considered successful if and only if it satisfies all of the following criteria:

1.  **Domain Expert Equivalence:** A senior engineer or domain expert reading the translation would gain the exact same technical understanding, architectural insight, and empirical data as a reader of the source text.
2.  **Native Naturalness:** A native speaker of the target language would not recognize the text as a translation. It reads with the cadence, vocabulary, and syntactic flow of an originally authored document.
3.  **Structural Fidelity:** The document hierarchy, Markdown formatting, tables, and code blocks are pixel-perfect representations of the source structure.
4.  **Terminological Rigor:** Technical terms are applied with absolute consistency and align with industry standards.
5.  **Empirical Invariance:** No factual information, metric, qualifier, or degree of certainty has been added, omitted, strengthened, or weakened.
6.  **Publication Readiness:** The translated document could be merged into a production repository, published as an RFC, or distributed to enterprise clients immediately, without requiring substantive editorial or technical revision.

***

*End of Meticulous Translation Skill Manual.*
