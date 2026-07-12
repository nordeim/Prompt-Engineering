# Meticulous Translation SKILL

## 1. Purpose

Produce publication-quality translations that preserve the source document's meaning, technical accuracy, nuance, hierarchy, rhetorical intent, formatting, and stylistic register while reading naturally to native speakers of the target language. This skill treats translation as a rigorous, evidence‑preserving process—not as paraphrasing or creative rewriting.

---

## 2. Core Philosophy

**Translate intent, not words.**  
At the same time, **never rewrite facts**.

The hierarchy of priorities during translation is:

1. **Preserve meaning** – all claims, data, and logical connections.
2. **Preserve technical correctness** – terminology, metrics, version numbers.
3. **Preserve logical structure** – paragraph breaks, lists, flow of reasoning.
4. **Preserve rhetorical force** – emphasis, certainty, doubt, hedging.
5. **Preserve formatting** – Markdown, tables, code blocks, links.
6. **Read naturally** – conform to target‑language conventions without distorting any of the above.

Readability serves faithfulness; it is never an excuse to simplify, omit, or “improve” the original.

---

## 3. Translation Principles

These rules apply to every sentence and every element.

| Rule | Description |
|------|-------------|
| 1 | Never add information. |
| 2 | Never omit information. |
| 3 | Never weaken the author's certainty. |
| 4 | Never strengthen the author's certainty. |
| 5 | Maintain **one** translation for each technical term throughout the document. |
| 6 | Preserve ambiguity if the source is ambiguous. |
| 7 | Do not “improve” arguments, flow, or style; only transfer them. |
| 8 | Translate evaluation labels consistently (e.g., “成立” → “Confirmed”). |
| 9 | Keep product names, file paths, commands, and code exactly as in the source. |
|10 | Treat numbers, units, and version strings as immutable facts. |

---

## 4. Workflow

Translation is not a single‑pass activity. Follow this ordered pipeline:

```
Read & understand the whole document
          ↓
   Phase 1 – Document analysis
          ↓
   Phase 2 – Terminology extraction
          ↓
   Phase 3 – Style calibration
          ↓
   Phase 4 – Structural preservation review
          ↓
   Phase 5 – Initial translation
          ↓
   Phase 6 – Consistency pass
          ↓
   Phase 7 – QA pass
```

Each phase is described in detail below.

---

## 5. Phase 1 – Document Analysis

Before translating a single word, answer:

- What **type** of document is this? (README, RFC, architecture guide, whitepaper, report, blog post, design doc, security advisory, benchmark report, etc.)
- Who is the **audience**? (Developers, executives, researchers, general public)
- What is the **register**? (Formal academic, technical‑evangelical, neutral report, legal)
- What is the **intent**? (Inform, persuade, teach, standardise)
- How is **evidence** presented? (Citations, footnotes, inline data, cross‑references)
- What is the **hierarchy**? (Heading levels, nesting of lists, blockquotes)
- Where are **repeated structures**? (Repeated verification labels, identical table formats)

Document your findings; they drive all subsequent decisions.

---

## 6. Phase 2 – Terminology Extraction

Extract every domain‑specific term, acronym, and named entity. For each, define:

- **Preferred translation** (if translatable)
- **Alternative translations** (acceptable but inferior)
- **Forbidden translations** (wrong or misleading)

Record them in a glossary that you will consult during translation.

**Example glossary fragment (Chinese → English)**

| Source term | Preferred English | Notes |
|-------------|-------------------|-------|
| 执行环境 | execution environment | Not “runtime” unless document explicitly uses “runtime” |
| 硬件隔离 | hardware isolation | |
| 冷启动 | cold start | Never “cool start” |
| 快照 | snapshot | |
| 回滚 | rollback | |
| 沙箱 | sandbox | |
| 成立 | Confirmed | In verification context; not “valid”, “true”, “established” |

Product names, file systems, protocols, and commands that **must not be translated** should be listed explicitly: CubeSandbox, RustVMM, KVM, XFS, FICLONE, etc.

---

## 7. Phase 3 – Style Calibration

Determine the style profile of the source and map it onto equivalent natural conventions in the target language.

| Style aspect | How to recognise | How to transfer |
|--------------|------------------|-----------------|
| Academic / formal | Long sentences, nominalizations, cautious hedging | Use formal register, impersonal constructions, “may”, “can”, “is believed to” |
| Technical report | Clear claims, data, tables, “Verification Result” labels | Preserve declarative tone, keep data‑driven phrasing, no marketing fluff |
| README / guide | Direct, instructive, bullet‑heavy | Keep directness, use “should”, “must”, action‑oriented language |
| Security advisory | Authoritative, precise, severity levels | Maintain gravity, translate severity terms consistently |
| Marketing / blog | Engaging, shorter sentences, occasional enthusiasm | Allow slightly more natural expression but still never over‑promise |

Calibration also includes punctuation conventions (Chinese vs. English quotation marks, dashes, spacing) – the translation must follow target‑language orthographic rules without breaking Markdown.

---

## 8. Phase 4 – Structural Preservation

Before translating, map every structural element so that none are lost or altered:

- [ ] Headings (level, numbering)
- [ ] Paragraphs (boundaries, line breaks)
- [ ] Bullet lists and nested indentation
- [ ] Numbered lists
- [ ] Blockquotes
- [ ] Tables (columns, alignment)
- [ ] Horizontal rules (`---`)
- [ ] Code blocks and inline code
- [ ] Links and footnotes
- [ ] Emphasis (bold, italic)
- [ ] Images / alt text

During translation, replicate these elements **exactly** as they appear in the source. If a heading is `### 3. Performance Metrics`, the translation must also be a level‑3 heading with the same numbering.

---

## 9. Phase 5 – Translation

Apply these guidelines while producing the initial draft:

- **Prefer faithful translation** over literal or overly idiomatic translation.  
  *Faithful*: accurately conveys meaning, respects author's structure and emphasis.  
  *Idiomatic*: might rearrange sentences for “better flow” – do this **only** when the source structure would genuinely confuse a native reader, and never at the cost of emphasis or logical order.
- **Never summarise**. If a paragraph is long, the translation is long.
- **Keep the author's voice** – if the source is dry and technical, do not add personality.
- **For evaluation phrases**, use the pre‑defined glossary equivalents.
- **For product names, versions, URLs**, copy them verbatim.
- **For numbers and units**, never change units, precision, or formatting.

---

## 10. Phase 6 – Consistency Pass

Review the full translation looking **only** for consistency:

- Does the same Chinese term map to the **same** English term every time?
- Did “execution environment” accidentally turn into “runtime” on page 5?
- Did “claim” become “assertion”, “verification” become “validation”?
- Are evaluation labels identical everywhere (e.g., “Verification Result: ✅ Confirmed”)?
- Are all capitalisations of product names consistent?

If you find inconsistency, harmonise to the glossary; never alternate.

---

## 11. Phase 7 – QA Pass

Execute a final quality‑assurance checklist **item by item**:

- [ ] No missing paragraphs
- [ ] No omitted bullet points or list items
- [ ] No altered heading levels or numbering
- [ ] No changed code blocks or inline code
- [ ] All numbers preserved exactly (magnitude, decimal places, units)
- [ ] All version strings unchanged
- [ ] All product names unchanged
- [ ] All file system names unchanged
- [ ] All dates preserved (format can be localised, but value must be identical)
- [ ] All Markdown syntax intact (links, tables, blockquotes, emphasis)
- [ ] All hyperlinks functional (if translated URL is present, copy original)
- [ ] No factual additions or deletions
- [ ] Tone and certainty consistent with source
- [ ] Translation reads naturally in target language (no “translationese”)
- [ ] Document could be published without requiring substantive editorial revision

---

## 12. Handling Technical Terminology

- Use established English technical terms, not literal calques.
- If a term has multiple possible translations, choose the one most common in formal technical documentation for that domain.
- For emerging or project‑specific terms, preserve the original if untranslatable, and add a brief parenthetical explanation on first use only if absolutely necessary (and if the source does so). Avoid inventing new terms.
- Do **not** translate terms that are part of a command, API, or file system name (e.g., `reflink`, `FICLONE`).

**Mapping examples (Chinese → English)**:

| Chinese | English (technical) | Wrong |
|---------|---------------------|-------|
| 页表 | page table | – |
| 嵌套虚拟化 | nested virtualization | – |
| 写时复制 | copy-on-write (CoW) | “copy while writing” |
| 宿主机 | host machine | “landlord machine” |
| Guest OS | guest OS (keep English) | – |

---

## 13. Handling Product Names

**Never translate:**

- CubeSandbox
- RustVMM
- KVM
- E2B
- Docker
- gVisor
- GitHub
- Ubuntu
- XFS, Ext4
- vmlinux

Retain original capitalisation, spelling, and punctuation. If a product name appears in quotes or with trademark symbols, keep them.

---

## 14. Handling Numbers

Numbers are facts. Do not:

- Convert units
- Round figures
- Change “<60ms” to “approximately 60ms”
- Alter “P95 at 90ms” to “95th percentile at 90ms” unless the source does

Keep all mathematical ranges, inequalities, and statistical notations exactly as written.

---

## 15. Handling Tables

- Preserve column alignment and header row.
- Translate content cell by cell; never merge or split cells.
- If the table contains checkmarks (✅), keep them unchanged.
- If a cell contains only a symbol or number, do not alter it.

---

## 16. Handling Markdown

Treat Markdown syntax as untranslatable code:

- Headers: `#`, `##`, `###`, etc.
- Bold/Italic: `**`, `*`
- Inline code: backticks
- Code blocks: triple backticks with language specifiers
- Links: `[text](url)` – translate link text, never alter URL
- Images: `![alt text](url)` – translate alt text
- Horizontal rules: `---`

The translated document must be a valid Markdown document with identical structure.

---

## 17. Handling Tone

Tone is often carried by small words. Translate degree of certainty precisely:

| Chinese | Appropriate English | Avoid |
|---------|---------------------|-------|
| 准确描述 | accurately describes | perfectly describes |
| 多个来源证实 | confirmed by multiple sources | proven beyond doubt |
| 高度可信 | highly credible | indisputably true |
| 广泛讨论 | widely discussed | universally agreed |
| 一致确认 | consistently confirmed | unanimously verified |
| 可能 | may / possibly | must / will |
| 尚未 | has not yet | never |

Never make the author sound more or less confident than they intended.

---

## 18. Chinese → English Guidelines

- Chinese often uses topic‑comment structures; convert them to subject‑predicate when necessary for natural English, but preserve the information order if possible.
- Avoid heavy nominalisation inherited from Chinese (e.g., “进行验证” → “verify”, not “conduct verification”).
- Break long, comma‑joined sentences into shorter ones only when it improves readability **and** does not alter logical relationships.
- Use “we” or passive voice only if the original does.
- Titles and headings: use title case or sentence case according to the English document type convention, as long as it does not affect meaning.
- Translate “【用户提示】” as “【User Note】” or similar, preserving the brackets and intent.

---

## 19. English → Chinese Guidelines

- Use natural Chinese technical writing: concise, clear, with appropriate four‑character expressions but not forced.
- Avoid “translationese”: do not copy English word order mechanically; restructure to natural Chinese SVO or topic‑comment patterns while keeping the same emphasis.
- Product names: keep in English unless there is a widely accepted official Chinese name.
- Punctuation: use Chinese full‑width punctuation (。、 “”) while preserving Markdown structure (e.g., `**bold**` stays as ASCII asterisks).
- English acronyms: keep them in Latin script; do not invent Chinese translations unless the source provides one.
- Maintain formal/informal register parity: a casual English blog post should become a casually styled Chinese post, not a formal report.

---

## 20. Common Mistakes

| Mistake | Why it matters |
|---------|----------------|
| Summarising long paragraphs | Loss of nuance and evidence |
| Improving the author's argument | Changes meaning; can introduce error |
| Dropping hedging words (“may”, “often”) | Distorts certainty |
| Translating product names literally | Creates confusion and unrecognisable entities |
| Breaking Markdown syntax | Document may not render |
| Inconsistent terminology | Confuses readers and undermines credibility |
| Changing units or numbers | Falsifies data |
| Reordering bullet points or sections | Alters emphasis and logical flow |
| Adding explanatory notes without marking them as translator's notes | Injects unverified content |
| Using machine‑translation defaults without review | Often results in literal, unidiomatic output |

---

## 21. Translation Decision Framework

Whenever uncertain, step through this decision tree:

1. **Does my translation preserve the factual claim?** If not, revise.
2. **Does it preserve the evidence (numbers, sources)?** If not, revise.
3. **Are all technical terms mapped to the glossary?** If not, revise.
4. **Is the structure (headings, lists, quotes) identical?** If not, revise.
5. **Does the tone match the source?** If not, revise.
6. **Does it read naturally?** If not, adjust wording while keeping 1–5 intact.

Only after all six are satisfied is the translation ready.

---

## 22. Quality Checklist

The final deliverable must pass all of these checks:

- [ ] Every paragraph from the source is present.
- [ ] Every bullet, list item, and table row is accounted for.
- [ ] Headings match in level and hierarchy.
- [ ] All code blocks and inline code are unchanged.
- [ ] Numbers, dates, versions, and units are identical.
- [ ] Product names and technical acronyms are preserved exactly.
- [ ] Glossary‑driven terminology is used consistently.
- [ ] Evaluation labels and checkmarks are uniform.
- [ ] Markdown syntax is valid and correctly nested.
- [ ] Links are unchanged and functional.
- [ ] No factual additions, deletions, or distortions.
- [ ] Tone and certainty match the original.
- [ ] Target‑language prose is idiomatic and professional.
- [ ] The document can be published directly without editorial revision.

---

## 23. Example Workflow

**Document:** *CubeSandbox Architecture & Deployment Guide* verification report (Chinese → English).

1. **Analysis:** Formal technical verification report with blockquotes, tables, and repeated “Verification Result: ✅ 成立” labels. Audience: engineers evaluating claims.
2. **Glossary:** Mapped “执行环境”→“execution environment”, “硬件隔离”→“hardware isolation”, “成立”→“Confirmed”, etc. Listed untranslatables: CubeSandbox, RustVMM, XFS, etc.
3. **Style calibration:** Neutral, evidence‑based tone; evaluation labels kept identical throughout.
4. **Structural map:** 1 executive summary, 9 numbered claim sections, 1 summary table, final conclusion.
5. **Translation:** Faithfully translated each claim, kept blockquotes, used “Verification Result: ✅ Confirmed” consistently.
6. **Consistency pass:** Verified “claim” not mutated to “assertion”, “Confirmed” not turned into “Valid”.
7. **QA pass:** Checked all numbers, version strings, Markdown table alignment, link preservation.

Result: a translation that reads as an original English technical report while being demonstrably equivalent to the Chinese source.

---

## 24. Success Criteria

A successful translation produced with this skill meets all of the following:

- A domain expert would consider the technical content completely equivalent to the source.
- A native speaker would not detect that it is a translation; it reads as an original document.
- Formatting, hierarchy, and document structure are identical to the source.
- Terminology is internally consistent throughout the entire document.
- No factual information has been added, omitted, strengthened, or weakened.
- The translation can be published directly without requiring substantive editorial revision.

---

https://chat.deepseek.com/share/rrjs06f9vxwhbdx3vw
