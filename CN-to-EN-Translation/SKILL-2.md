# Meticulous Translation

## Purpose

Produce publication-quality translations that preserve the source document's meaning, technical accuracy, nuance, hierarchy, rhetorical intent, formatting, and stylistic register while reading naturally to native speakers of the target language.

This skill is designed for technical documents including but not limited to:

- GitHub READMEs and repository documentation
- Architecture documents and design specifications
- RFCs and technical proposals
- Whitepapers and research summaries
- Technical blogs and benchmark reports
- Security advisories and audit reports
- Product documentation and deployment guides
- API reference documentation

Supported language pairs: Chinese ↔ English (bidirectional).

---

## Core Philosophy

### 1. Translate Intent, Not Words

The highest priority is to convey what the author intended to communicate, not to render each word literally. A sentence that reads naturally in the target language while preserving the author's exact meaning is preferable to a sentence that is grammatically correct but semantically distorted by over-literal translation.

### 2. Never Rewrite Facts

While style and phrasing may be adapted for the target language, factual claims, technical specifications, numerical data, version numbers, and evidence must never be altered, summarized, or "improved." The translator is a conduit, not an editor.

### 3. Preserve Before Polish

The hierarchy of preservation is:

1. **Meaning** — the semantic content and factual claims
2. **Technical correctness** — terminology, specifications, and technical relationships
3. **Logical structure** — argument flow, evidence hierarchy, and document organization
4. **Rhetorical force** — emphasis, certainty, and evaluative tone
5. **Formatting** — Markdown structure, tables, lists, code blocks, and hierarchy
6. **Natural readability** — idiomatic target-language prose

Readability comes **last**, not first. A translation that sounds beautiful but changes the meaning has failed. A translation that is slightly less elegant but perfectly faithful has succeeded.

### 4. Consistency Over Creativity

Once a term, phrase, or stylistic choice is established, it must be maintained throughout the entire document. Mid-document terminology drift is one of the most common and damaging translation errors.

---

## Translation Principles

### Rule 1: Never Add Information
Do not introduce explanations, clarifications, or background context that does not exist in the source. If the source assumes the reader knows something, the translation must make the same assumption.

### Rule 2: Never Omit Information
Every claim, qualifier, caveat, and piece of evidence in the source must appear in the translation. Do not summarize paragraphs into sentences or drop "minor" details.

### Rule 3: Never Weaken Certainty
If the source says "confirmed," do not translate it as "suggested" or "indicated." If the source says "all," do not translate it as "most."

### Rule 4: Never Strengthen Certainty
If the source says "highly credible," do not translate it as "proven" or "indisputably true." The translator's job is to preserve the author's epistemic stance, not to endorse it.

### Rule 5: Never Normalize Terminology Mid-Document
If "execution environment" was chosen in paragraph 3, it must remain "execution environment" in paragraph 47. Do not switch to "runtime," "operating context," or "deployment environment" later.

### Rule 6: Translate Consistently
Establish a glossary before translating and adhere to it. Use the same translation for the same concept every time.

### Rule 7: Preserve Ambiguity If the Source Is Ambiguous
If the source is intentionally vague or leaves something unstated, do not resolve the ambiguity in translation. The reader of the translation should encounter the same ambiguity as the reader of the original.

### Rule 8: Do Not "Improve" Arguments
If the source contains a weak argument, a logical gap, or awkward phrasing, translate it faithfully. Do not silently fix the author's reasoning.

---

## Workflow

Meticulous translation follows a deterministic seven-phase pipeline. Do not skip phases. Each phase exists to catch a specific category of error.

```
Read
  ↓
Analyze
  ↓
Extract Terminology
  ↓
Determine Style
  ↓
Translate
  ↓
Consistency Pass
  ↓
QA Pass
```

---

## Phase 1: Document Analysis

Before translating a single sentence, analyze the source document thoroughly. Answer the following questions:

### Document Type
What kind of document is this? The type determines the appropriate register and conventions:

| Document Type | Expected Register |
|---------------|-------------------|
| GitHub README | Informative, approachable, technically precise |
| Architecture document | Formal, systematic, evidence-oriented |
| RFC / Technical proposal | Formal, deliberative, specification-oriented |
| Whitepaper | Authoritative, persuasive, comprehensive |
| Technical blog | Conversational but technically precise |
| Security advisory | Urgent, precise, unambiguous |
| Benchmark report | Analytical, data-driven, neutral |
| Product documentation | Instructional, clear, task-oriented |
| Deployment guide | Procedural, imperative, detailed |

### Audience
Who is the intended reader? Experts? General developers? Decision-makers? The audience determines how much background knowledge can be assumed and how technical the language should be.

### Register
What is the stylistic register? Formal? Conversational? Academic? Legal? The translation must match the source register, not the translator's personal style.

### Intent
What is the author trying to achieve? Inform? Persuade? Instruct? Warn? Verify? The translation must serve the same communicative purpose.

### Evidence Style
How does the author support claims? With data? With citations? With logical argument? With authority? The evidence style must be preserved.

### Document Hierarchy
Map the document structure. Identify:

- Title and subtitle levels
- Section headings and their relationships
- Blockquotes (especially for quoted claims)
- Bullet lists and their nesting depth
- Numbered lists and their sequence
- Tables and their column structure
- Horizontal rules (`---`) and their semantic function
- Code blocks and inline code
- Links and references

### Repetition
Identify phrases, claims, or structural patterns that repeat. Repetition in the source should be preserved in the translation. Do not vary wording merely to avoid repetition unless the source itself varies.

### Formatting
Note all Markdown formatting, including:

- Heading levels (`#`, `##`, `###`, etc.)
- Bold and italic emphasis
- Blockquotes (`>`)
- Bullet lists (`*`, `-`, `+`)
- Numbered lists (`1.`, `2.`, etc.)
- Tables (pipe-delimited)
- Horizontal rules (`---`)
- Code blocks (fenced and indented)
- Inline code (backticks)
- Links (`[text](url)`)
- Images

---

## Phase 2: Terminology Extraction

Before translating, build a glossary. Extract every technical term, product name, and domain-specific concept. For each term, determine:

```
Term: [exact source term]
Preferred Translation: [chosen target-language equivalent]
Alternative Translation: [acceptable but less preferred equivalent]
Forbidden Translation: [common but incorrect equivalent]
Rationale: [why this choice was made]
```

### Example Glossary Entries

```
Term: 执行环境
Preferred Translation: execution environment
Alternative Translation: runtime environment
Forbidden Translation: runtime
Rationale: The document consistently discusses infrastructure-level
           sandboxing, not language runtimes. "Runtime" would be misleading.
```

```
Term: 内核逃逸
Preferred Translation: kernel escape
Alternative Translation: kernel-level escape
Forbidden Translation: kernel panic, system crash
Rationale: "Kernel escape" is the established security term for sandbox
           breakout via kernel vulnerabilities.
```

```
Term: 成立
Preferred Translation: Confirmed
Alternative Translation: Validated
Forbidden Translation: True, Correct, Proven, Verified
Rationale: In verification contexts, "Confirmed" is the standard English
           equivalent of Chinese "成立" in technical reports.
```

### Product Names: Never Translate

The following categories must remain in their original form:

- Product names (CubeSandbox, CubeCoW, RustVMM, Firecracker, Envoy)
- Technology names (KVM, PVM, Docker, Kubernetes)
- File names (README.md, vmlinux, install.sh)
- Protocol names (HTTP, SSH, API, SDK)
- Data formats (JSON, YAML, XML, CSV)
- Operating systems (Ubuntu, Linux, Windows)
- Filesystem names (XFS, Ext4, Btrfs, ZFS)
- Feature names (AutoPause, AutoResume, reflink, FICLONE)
- Version numbers (v0.5.0, v1.2.3)
- Organization names (Tencent Cloud, GitHub, AWS)

Exception: If a product has an officially established localized name in the target market (e.g., "微信" for "WeChat" in Chinese), use the official localized name.

### Technical Terminology: Translate Once, Use Everywhere

For domain-specific concepts that are not product names, establish a single translation and use it consistently. Examples:

| Chinese | English |
|---------|---------|
| 执行环境 | execution environment |
| 硬件隔离 | hardware isolation |
| 内核逃逸 | kernel escape |
| 冷启动 | cold start |
| 常驻内存 | resident memory |
| 快照 | snapshot |
| 回滚 | rollback |
| 克隆 | clone |
| 写时复制 | copy-on-write (CoW) |
| 生命周期 | lifecycle |
| 挂起 | suspend |
| 恢复 | resume |
| 沙箱 | sandbox |
| 裸金属服务器 | bare-metal server |
| 宿主机 | host machine |
| Guest OS | guest OS (or guest operating system) |
| Hypervisor | hypervisor |
| 页表 | page table |
| 嵌套虚拟化 | nested virtualization |
| 文件系统 | filesystem |
| 自动化安装 | automated installation |
| 一键安装 | one-click installation |
| 性能报告 | performance report |
| 官方文档 | official documentation |
| 官方仓库 | official repository |
| 发布说明 | release notes |
| 更新日志 | changelog |
| 部署指南 | deployment guide |
| 快速开始指南 | quick start guide |
| 安全分析 | security analysis |

---

## Phase 3: Style Calibration

Determine the stylistic conventions appropriate for the document type and apply them consistently.

### Formal Technical English

For architecture documents, whitepapers, verification reports, and RFCs:

- Use complete sentences.
- Prefer active voice for clarity, but use passive voice when the agent is unknown or unimportant.
- Avoid contractions.
- Use precise technical vocabulary.
- Maintain an objective, evidence-oriented tone.
- Avoid colloquialisms, idioms, and cultural references.

### README / Documentation Style

For GitHub READMEs and product documentation:

- Use clear, direct prose.
- Balance technical precision with accessibility.
- Use imperative mood for instructions ("Run the script," not "You should run the script").
- Maintain a helpful but not overly casual tone.

### Security Advisory Style

For security reports and advisories:

- Be unambiguous and precise.
- Use "must" for requirements, "should" for recommendations.
- Avoid speculative language.
- State impact clearly and concisely.

### Chinese Technical Writing Style

For English → Chinese translation:

- Prefer concise, information-dense prose.
- Four-character expressions are acceptable where they convey technical concepts naturally (e.g., "硬件隔离" for "hardware isolation").
- Avoid "translationese" — awkward calques that sound like literal translations.
- Use Chinese punctuation conventions (full-width commas, periods, and quotation marks) for prose, but preserve ASCII punctuation for Markdown syntax and code.
- Maintain appropriate formality for the document type.

---

## Phase 4: Structural Preservation

The document's physical structure is part of its meaning. Preserve it exactly.

### Headings

- Preserve heading levels exactly (`#` → `#`, `##` → `##`, etc.).
- Translate heading text into natural technical English (or Chinese), not literal word-for-word equivalents.
- Example: "执行摘要" → "Executive Summary" (not "Execution Summary").
- Example: "声明验证详情" → "Claim Verification Details" (not "Detailed Verification of Declared Statements").

### Blockquotes

- Every blockquote (`>`) in the source must remain a blockquote in the translation.
- Preserve the exact formatting within blockquotes (e.g., `> **Original Claim:** ...`).
- Do not convert blockquotes to regular paragraphs or vice versa.

### Bullet Lists

- Preserve bullet nesting depth exactly.
- If the source uses `*`, use `*` in the translation. If `-`, use `-`.
- Do not merge or split list items.
- Do not change the order of list items.

### Numbered Lists

- Preserve numbering exactly (`1.`, `2.`, etc.).
- Do not renumber unless the source itself is renumbered.
- Do not merge or split numbered items.

### Tables

- Preserve Markdown table formatting (pipe-delimited).
- Translate only the cell contents.
- Maintain column alignment (left, center, right) if explicitly marked.
- Preserve checkmarks (✅, ❌, ✓, ✗) and other symbols.
- Do not add or remove columns.
- Do not add or remove rows.

### Horizontal Rules

- Preserve `---` exactly where they appear.
- Do not add horizontal rules where none exist.
- Do not remove existing horizontal rules.

### Code Blocks

- Preserve fenced code blocks (```) and their language identifiers.
- Do not translate code.
- Do not translate comments inside code blocks unless explicitly instructed.
- Preserve indentation exactly.

### Inline Code

- Preserve inline code (backticks) exactly.
- Do not translate text inside backticks unless it is a natural-language string that should be localized.
- Example: `` `install.sh` `` remains `` `install.sh` ``.
- Example: `` `FICLONE` `` remains `` `FICLONE` ``.

### Links

- Preserve link syntax (`[text](url)`) exactly.
- Translate link text if it is natural language.
- Do not change URLs.
- Do not add or remove links.

### Emphasis

- Preserve bold (`**text**`) and italic (`*text*`) exactly.
- Do not add emphasis where none exists.
- Do not remove existing emphasis.

---

## Phase 5: Translation

With the glossary established and the style calibrated, perform the actual translation. Follow these sub-principles:

### Translation Modes

Understand the four modes of translation and select the appropriate one for each segment:

| Mode | Description | Appropriate For |
|------|-------------|-----------------|
| **Literal** | Word-for-word rendering | Legal texts, contracts, precise definitions |
| **Faithful** | Meaning-for-meaning, preserving structure | Technical documentation, architecture guides |
| **Idiomatic** | Natural target-language expression | Marketing copy, conversational blogs |
| **Adaptive** | Restructuring for cultural appropriateness | UI text, user-facing instructions |

For technical documentation, **faithful translation** is the default mode. Use idiomatic translation only where literal or faithful translation would produce genuinely confusing or unnatural results, and only after confirming that no meaning is lost.

### Sentence-Level Guidelines

#### Chinese → English

- **Avoid excessive nominalization.** Chinese technical writing often uses noun-heavy structures. English technical writing prefers verbs where natural.
  - Poor: "The realization of the optimization of the performance is necessary."
  - Better: "We must optimize performance."
  - Best (if source is neutral): "Performance optimization is necessary."

- **Restructure only when required for idiomatic English.** Do not restructure sentences merely to make them "flow better" if the original structure carries rhetorical or logical weight.

- **Preserve information order where possible.** If the source presents A before B, the translation should present A before B unless English grammar absolutely requires reversal.

- **Use established English technical terminology.** Do not invent calques. If a concept has a standard English term, use it.

- **Translate evaluation language consistently.** In verification contexts:
  - "成立" → "Confirmed"
  - "准确描述了" → "accurately describes"
  - "得到证实" → "confirmed"
  - "具有高度可信度" → "highly credible"
  - "广泛讨论" → "widely discussed"
  - "一致确认" → "consistently confirmed"
  - "交叉验证" → "cross-validated"

#### English → Chinese

- **Avoid translationese.** Do not produce sentences that sound like they were translated by a machine.
  - Poor: "该指南声称其能提供硬件隔离。"
  - Better: "指南声称其可提供硬件隔离。"

- **Prefer natural Chinese technical writing conventions.** Chinese technical prose is often more concise than English. Condense where appropriate without losing information.

- **Use four-character expressions where appropriate.** They are a natural feature of Chinese technical writing.
  - "hardware-isolated" → "硬件隔离的"
  - "sub-100ms startup" → "亚百毫秒启动"

- **Retain product names in English** unless there is a widely accepted official Chinese name.

- **Maintain appropriate punctuation conventions.** Use full-width punctuation for Chinese prose, but preserve ASCII punctuation for Markdown syntax and code.

### Numbers and Units

- **Never change numerical values.**
- **Never change units.**
- **Never change precision.**
- **Never change ranges.**
- **Never change scientific notation.**
- **Never change percentages.**
- **Never change version numbers.**
- **Never change latency figures.**
- **Never change memory sizes.**
- **Never change dates.**
- **Never change file sizes.**

Examples of what to preserve exactly:

- `<60ms` → `<60ms`
- `<5MB` → `<5MB`
- `32GB` → `32GB`
- `96-core` → `96-core`
- `2000+` → `2000+`
- `P95 = 90ms` → `P95 = 90ms`
- `P99 = 137ms` → `P99 = 137ms`
- `v0.5.0` → `v0.5.0`
- `July 3, 2026` → `July 3, 2026`
- `x86_64` → `x86_64`
- `aarch64` → `aarch64`

### Tone Preservation

Map evaluative and descriptive language consistently:

| Chinese | English | Rationale |
|---------|---------|-----------|
| 准确描述了 | accurately describes | Neutral, precise |
| 得到证实 | confirmed | Standard verification term |
| 具有高度可信度 | highly credible | Preserves epistemic modesty |
| 广泛讨论 | widely discussed | Neutral, factual |
| 一致确认 | consistently confirmed | Emphasizes cross-source agreement |
| 交叉验证 | cross-validated | Technical term |
| 核心声明 | core claim | Standard analytical term |
| 核心能力 | core capability | Standard analytical term |
| 核心特性 | core feature | Standard analytical term |
| 技术方案 | technical architecture | Broader than "technical solution" |
| 技术路径 | technical approach | Neutral, descriptive |

Avoid strengthening or weakening the author's certainty:

- Do not translate "highly credible" as "indisputably true."
- Do not translate "confirmed" as "proven."
- Do not translate "widely discussed" as "universally accepted."
- Do not translate "suggested" as "confirmed."

---

## Phase 6: Consistency Pass

After the initial translation, perform a dedicated consistency pass. Read the entire translated document and verify:

### Terminology Consistency

- Did "execution environment" ever become "runtime" halfway through?
- Did "claim" become "assertion" later?
- Did "verification" become "validation" randomly?
- Did "sandbox" become "container" in some paragraphs?
- Did "host machine" become "server" in some sections?

### Phrase Consistency

- Are recurring phrases rendered identically every time?
- Is "Verification Result: ✅ Confirmed" rendered exactly the same way in every instance?
- Are section headers formatted consistently?

### Formatting Consistency

- Are all blockquotes formatted the same way?
- Are all bullet lists using the same marker?
- Are all tables using the same alignment?
- Are inline code and code blocks preserved consistently?

### Style Consistency

- Is the register consistent throughout?
- Does the tone shift unexpectedly between sections?
- Are contractions used consistently (or not at all)?

---

## Phase 7: QA Pass

Perform a final quality assurance pass using the following checklist. Treat this as a professional localization QA acceptance test.

### Content Completeness

- [ ] No missing paragraphs
- [ ] No missing sentences
- [ ] No missing bullets
- [ ] No missing table rows
- [ ] No missing table columns
- [ ] No omitted blockquotes
- [ ] No omitted code blocks
- [ ] No omitted inline code
- [ ] No omitted links
- [ ] No omitted images
- [ ] No omitted horizontal rules
- [ ] No omitted footnotes

### Structural Integrity

- [ ] Heading levels preserved exactly
- [ ] Heading hierarchy preserved
- [ ] Bullet list nesting preserved
- [ ] Numbered list sequence preserved
- [ ] Table structure preserved
- [ ] Blockquote formatting preserved
- [ ] Horizontal rules preserved
- [ ] Code block language identifiers preserved
- [ ] Inline code preserved
- [ ] Link URLs unchanged
- [ ] Link text translated appropriately
- [ ] Emphasis (bold, italic) preserved

### Numerical Accuracy

- [ ] All numbers unchanged
- [ ] All units unchanged
- [ ] All precision unchanged
- [ ] All ranges unchanged
- [ ] All version numbers unchanged
- [ ] All latency figures unchanged
- [ ] All memory sizes unchanged
- [ ] All dates unchanged
- [ ] All percentages unchanged
- [ ] All scientific notation unchanged

### Terminology Accuracy

- [ ] Product names unchanged
- [ ] Technology names unchanged
- [ ] File names unchanged
- [ ] Protocol names unchanged
- [ ] Data format names unchanged
- [ ] Filesystem names unchanged
- [ ] Feature names unchanged
- [ ] Organization names unchanged
- [ ] Domain terminology consistent throughout
- [ ] No invented terms
- [ ] No dropped technical terms

### Fidelity

- [ ] No factual additions
- [ ] No factual deletions
- [ ] No factual reinterpretations
- [ ] No summarized paragraphs
- [ ] No expanded explanations
- [ ] No "improved" arguments
- [ ] No weakened certainty
- [ ] No strengthened certainty
- [ ] Ambiguity preserved where source is ambiguous

### Tone and Style

- [ ] Register appropriate for document type
- [ ] Tone consistent throughout
- [ ] Evaluation language mapped consistently
- [ ] No colloquialisms in formal documents
- [ ] No overly enthusiastic wording in neutral reports
- [ ] No speculative language in factual documents
- [ ] Natural target-language prose
- [ ] Reads as an original document, not a translation

### Markdown Integrity

- [ ] No broken table alignment
- [ ] No broken lists
- [ ] No broken code blocks
- [ ] No broken links
- [ ] No broken emphasis
- [ ] No broken blockquotes
- [ ] No broken horizontal rules
- [ ] No changed capitalization in code
- [ ] No changed indentation in code

---

## Handling Specific Elements

### Blockquotes for Quoted Claims

When the source uses blockquotes to present original claims for verification, preserve this structure exactly:

```markdown
> **Original Claim:** [claim text]
```

Do not convert to regular text. Do not drop the "Original Claim" label. Do not reformat.

### Verification Results

When the source uses a standard verification result format, preserve it exactly:

```markdown
**Verification Result:** ✅ Confirmed
```

Use the same label, the same checkmark, and the same capitalization every time. Do not alternate between "Confirmed," "Valid," "True," "Correct," or "Verified."

### Summary Tables

When the source contains a summary table at the end of a section, preserve:

- The table structure
- The column headers
- The row order
- The checkmarks or status indicators
- The evidence source references

Translate only the natural-language cell contents.

### Horizontal Rules as Section Dividers

When `---` is used to separate major sections (e.g., between the Executive Summary and the detailed verification), preserve it. The horizontal rule carries semantic weight as a visual separator.

---

## Translation Decision Framework

Whenever uncertain about a translation choice, apply the following decision tree in order:

```
1. Does this preserve meaning?
   ↓ No → Revise.
   ↓ Yes → Continue.

2. Does this preserve technical correctness?
   ↓ No → Revise.
   ↓ Yes → Continue.

3. Does this preserve logical structure?
   ↓ No → Revise.
   ↓ Yes → Continue.

4. Does this preserve rhetorical force?
   ↓ No → Revise.
   ↓ Yes → Continue.

5. Does this preserve formatting?
   ↓ No → Revise.
   ↓ Yes → Continue.

6. Does this read naturally in the target language?
   ↓ No → Revise for readability without compromising 1-5.
   ↓ Yes → Accept.
```

If a choice satisfies 1-5 but not 6, revise for readability while maintaining 1-5. If a choice satisfies 6 but fails 1-5, it is unacceptable regardless of how elegant it sounds.

---

## Common Failure Modes

Be vigilant against the following common translation errors:

### Over-Literal Translation

Rendering each word individually without regard for natural target-language syntax or meaning.

- Example: "硬件隔离的" → "hardware-isolated of" (instead of "hardware-isolated").

### Over-Localization

Adapting the text so aggressively that technical meaning is lost or altered.

- Example: Translating "kernel escape" as "system crash" because it "sounds more natural."

### Over-Editing

"Improving" the author's writing by adding explanations, smoothing arguments, or filling gaps.

- Example: Adding a sentence of background explanation that the author did not include.

### Summarization

Condensing the source into shorter form, dropping details deemed "minor."

- Example: Reducing a three-bullet analysis to a single sentence.

### Hallucinated Clarification

Adding explanatory text that the translator believes the reader needs, even though the source does not include it.

- Example: Adding a parenthetical explanation of a technical term that the source left unexplained.

### Dropped Qualifiers

Omitting words that soften, limit, or qualify a claim.

- Example: "under 60ms in single-concurrency conditions" → "under 60ms" (dropping the condition).

### Inconsistent Terminology

Using different translations for the same concept at different points in the document.

- Example: "execution environment" in paragraph 1, "runtime environment" in paragraph 5, "operating context" in paragraph 12.

### Reordered Arguments

Changing the order of points in a list or the sequence of sentences in a paragraph.

- Example: Reversing the order of two bullet points because "it flows better."

### Changed Certainty

Strengthening or weakening the author's level of confidence.

- Example: "highly credible" → "indisputably true" (strengthened).
- Example: "confirmed" → "suggested" (weakened).

### Broken Markdown

Altering the document's formatting structure.

- Example: Converting a blockquote to a regular paragraph.
- Example: Breaking table alignment by adding or removing spaces.
- Example: Changing list nesting by altering indentation.

### Translated Filenames

Translating file names or paths that should remain in their original form.

- Example: `README.md` → `自述文件.md`.

### Translated Code

Translating variable names, function names, or comments inside code blocks.

- Example: `install.sh` → `安装.sh`.

### Changed Inline Code

Modifying text inside backticks.

- Example: `` `FICLONE` `` → `` `文件克隆` ``.

### Broken Lists

Merging or splitting list items, changing markers, or altering nesting.

### Lost Hyperlinks

Dropping links or changing their targets.

---

## Bidirectional Guidelines

### Chinese → English

1. **Avoid excessive nominalization inherited from Chinese.** Chinese technical writing tends toward noun-heavy structures. English prefers verbs where natural.

2. **Restructure only when required for idiomatic English.** Preserve information order and emphasis where possible.

3. **Translate evaluation language consistently.** Establish a mapping for evaluative terms (e.g., "成立" → "Confirmed") and adhere to it.

4. **Use established English technical terminology.** Do not invent calques. Consult established glossaries and documentation.

5. **Preserve the analytical, evidence-based tone.** Chinese verification reports often sound formal and authoritative. The English should match this register, not sound casual or conversational.

6. **Handle Chinese four-character expressions carefully.** Many have no direct English equivalent. Translate the meaning, not the characters.

7. **Preserve Chinese paragraph breaks.** Chinese prose often uses shorter paragraphs than English. Do not merge paragraphs unless the source itself is a single long paragraph.

### English → Chinese

1. **Avoid translationese.** The translation should read like it was originally written by a Chinese technical professional, not like a word-for-word conversion.

2. **Prefer natural Chinese technical writing conventions.** Chinese technical prose is often more concise and direct than English. Condense where appropriate.

3. **Use four-character expressions where they fit naturally.** They are a legitimate and effective feature of Chinese technical writing.

4. **Retain product names in English** unless an official Chinese name is widely established.

5. **Maintain appropriate punctuation conventions.** Use full-width punctuation for Chinese prose, but preserve ASCII punctuation for Markdown syntax, code, and product names.

6. **Handle English hedging carefully.** English phrases like "it is suggested that" or "it appears that" should be mapped to appropriate Chinese expressions that preserve the same level of epistemic caution.

7. **Preserve English paragraph structure.** Do not split English paragraphs into multiple Chinese paragraphs unless the source itself uses short paragraphs.

---

## Success Criteria

A translation produced using this skill is considered successful if and only if it satisfies **all** of the following criteria:

1. **Technical equivalence:** A domain expert reading the translation would consider the technical content equivalent to the source. No facts, specifications, or relationships have been altered.

2. **Native readability:** A native speaker of the target language would not recognize the document as a translation. It reads as though it were originally authored in the target language.

3. **Structural fidelity:** Formatting, hierarchy, and document structure are preserved exactly. Headings, lists, tables, code blocks, blockquotes, and horizontal rules match the source.

4. **Terminological consistency:** Technical terminology remains internally consistent throughout the document. The same concept is never rendered with different terms.

5. **Factual integrity:** No factual information has been added, omitted, strengthened, or weakened. The translation is a faithful conduit of the author's claims.

6. **Publishable quality:** The translated document could be published directly — as a GitHub README, a whitepaper, a technical blog, or a product document — without requiring substantive editorial revision. Minor copy-editing (typo fixes, minor rephrasing) is acceptable; structural or factual changes are not.

---

## Example Workflow

The following example illustrates the complete workflow applied to a short excerpt from a technical verification report.

### Source (Chinese)

```markdown
#### 3. 性能指标：启动速度与内存开销

> **声明原文**：It provisions MicroVMs in <60ms with <5MB memory overhead.

**验证结果：✅ 成立，且有多场景数据支撑**

*   **<60ms冷启动**：在单并发场景下，端到端冷启动时间确认为 **<60ms**。在高并发下表现依然出色：50并发时平均启动时间为67ms，P95为90ms，P99为137ms。
*   **<5MB内存开销**：在沙箱规格不超过32GB的测试环境下，单实例常驻内存开销确认为 **<5MB**。
*   **高密度部署**：得益于其轻量级设计，一台96核服务器可同时运行超过**2000个**沙箱实例。
```

### Phase 1: Document Analysis

- **Document type:** Technical verification report
- **Audience:** Technical professionals evaluating CubeSandbox
- **Register:** Formal, analytical, evidence-based
- **Intent:** Verify and confirm performance claims
- **Evidence style:** Data-driven with specific benchmarks
- **Hierarchy:** H4 heading → blockquote → verification result → bulleted analysis
- **Repetition:** "确认为" (has been confirmed) repeats; "<60ms" and "<5MB" repeat
- **Formatting:** H4, blockquote, bold labels, nested bullets with bold subheadings

### Phase 2: Terminology Extraction

| Term | Preferred Translation | Rationale |
|------|----------------------|-----------|
| 性能指标 | performance metrics | Standard technical term |
| 启动速度 | startup latency | More precise than "startup speed" |
| 内存开销 | memory overhead | Standard term |
| 声明原文 | Original Claim | Standard label for quoted claims |
| 验证结果 | Verification Result | Standard label for verification |
| 成立 | Confirmed | Standard verification outcome |
| 冷启动 | cold start | Standard term |
| 端到端 | end-to-end | Standard term |
| 常驻内存 | resident memory | Standard term |
| 沙箱规格 | sandbox specifications | Context-appropriate |
| 高密度部署 | high-density deployment | Standard term |
| 轻量级设计 | lightweight architecture | "Design" → "architecture" in this context |

### Phase 3: Style Calibration

- Formal technical English
- Objective, evidence-oriented tone
- Data presented clearly with units preserved
- Bullet points used for parallel analysis

### Phase 4: Structural Preservation

- H4 → H4
- Blockquote → Blockquote
- Bold label "验证结果：✅ 成立..." → Bold label "Verification Result: ✅ Confirmed..."
- Three bullets with bold subheadings → Three bullets with bold subheadings
- All numbers and units preserved exactly

### Phase 5: Translation

```markdown
#### 3. Performance Metrics: Startup Latency and Memory Overhead

> **Original Claim:** It provisions MicroVMs in <60ms with <5MB memory overhead.

**Verification Result:** ✅ Confirmed, supported by benchmark data across multiple scenarios

* **<60ms Cold Start:** Under single-concurrency conditions, end-to-end cold startup latency has been confirmed to be **under 60ms**. Performance remains excellent under higher concurrency: at **50 concurrent launches**, the average startup time is **67ms**, with **P95 at 90ms** and **P99 at 137ms**.
* **<5MB Memory Overhead:** In testing environments where sandbox specifications do not exceed **32GB**, the resident memory overhead per sandbox instance has been confirmed to be **under 5MB**.
* **High-Density Deployment:** Owing to its lightweight architecture, a **96-core server** can simultaneously host **more than 2,000** sandbox instances.
```

### Phase 6: Consistency Pass

- "Verification Result: ✅ Confirmed" matches established pattern
- "cold startup latency" used consistently (not "cold boot time")
- "resident memory" used consistently (not "persistent memory")
- "sandbox" used consistently (not "container")
- All numbers preserved exactly

### Phase 7: QA Pass

- [x] No missing paragraphs
- [x] No missing bullets
- [x] Heading levels preserved
- [x] Blockquote preserved
- [x] All numbers unchanged
- [x] All units unchanged
- [x] Product names unchanged
- [x] Terminology consistent
- [x] Tone appropriate
- [x] Markdown preserved
- [x] No factual additions or deletions

---

## Final Notes

This skill is not a collection of translation tips. It is an operational manual designed to guide another capable language model toward producing translations with the consistency, rigor, and fidelity of a professional technical translator.

The discipline of the workflow — analyze first, extract terminology, calibrate style, preserve structure, translate faithfully, enforce consistency, and validate rigorously — is what separates meticulous translation from conventional machine translation.

Apply this skill with patience and precision. The quality of the output is directly proportional to the care invested in each phase.
