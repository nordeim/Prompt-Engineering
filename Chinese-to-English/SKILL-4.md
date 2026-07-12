# SKILL.md: Meticulous Technical Translation

## 1. Purpose

The primary goal of this skill is not simply to "translate documents." It is to **produce publication-quality translations that preserve the source document's meaning, technical accuracy, nuance, hierarchy, rhetorical intent, formatting, and stylistic register while reading naturally to native speakers of the target language.**

This skill enables a capable LLM to reliably produce translations approaching the quality of professional human technical translators. It is explicitly designed to be reusable across a wide range of technical domains—including GitHub READMEs, RFCs, architecture documents, whitepapers, technical blogs, research summaries, benchmark reports, design documents, security reports, and product documentation—without becoming overly specific to any single project or codebase.

---

## 2. Core Philosophy

The foundation of this skill rests on two overarching principles:
1. **Translate intent rather than words.** Do not perform mechanical word-for-word substitution. Understand the semantic and rhetorical intent of the source text and convey it in the target language.
2. **Never rewrite facts.** You are a translator, not an author or an editor. Do not add external knowledge, omit inconvenient details, or "improve" the author's technical arguments.

When conflicts arise, adhere to the following strict hierarchy of preservation:
1. **Preserve meaning:** The factual information must remain exactly intact.
2. **Preserve technical correctness:** Industry-standard terminology must be used accurately.
3. **Preserve logical structure:** The argument's flow and hierarchy must mirror the source.
4. **Preserve rhetorical force:** The author's tone (e.g., authoritative, cautionary, analytical) must be maintained.
5. **Preserve formatting:** All Markdown, tables, and code blocks must be retained.
6. **Preserve natural readability:** The text must read fluently in the target language.

*Note that natural readability comes **last**. Never sacrifice factual precision or formatting for the sake of making a sentence sound slightly smoother.*

---

## 3. Translation Principles

To execute the core philosophy, adhere strictly to the following explicit rules:

* **Rule 1:** Never add information. (No hallucinated clarifications).
* **Rule 2:** Never omit information. (No summarizing or dropping difficult phrases).
* **Rule 3:** Never weaken certainty. (If the source says "confirmed," do not write "likely").
* **Rule 4:** Never strengthen certainty. (If the source says "highly credible," do not write "unquestionably true").
* **Rule 5:** Never normalize terminology mid-document. (If a specific term is chosen, use it consistently).
* **Rule 6:** Translate consistently. (Avoid using synonyms for the same technical concept).
* **Rule 7:** Preserve ambiguity if the source is ambiguous. (Do not resolve uncertainties on the author's behalf).
* **Rule 8:** Do not "improve" arguments. (Translate what is there, not what you think the author meant to say).

---

## 4. Workflow

Translation must be executed as a deterministic pipeline, mirroring the workflow of a professional technical translator. Do not attempt to translate sentence-by-sentence from the top down. Follow this sequence:

```text
Read (Comprehend)
   ↓
Analyze (Document Type & Structure)
   ↓
Extract Terminology (Glossary Building)
   ↓
Determine Style (Register Calibration)
   ↓
Translate (Drafting)
   ↓
Consistency Pass (Term Drift Check)
   ↓
QA Pass (Structural & Factual Validation)
```

---

## 5. Phase 1: Document Analysis

Before translating, analyze the document's macro-structure and intent:
* **Document type:** Is this a README, an RFC, a security advisory, or a research paper?
* **Audience:** Who is reading this? (Developers, executives, end-users?)
* **Register:** Is the tone formal, academic, conversational, or imperative?
* **Intent:** Is it to instruct, persuade, report, or warn?
* **Evidence style:** Does the document rely on citations, benchmarks, or logical deduction?
* **Document hierarchy:** Map out headings, subheadings, and lists.
* **Repetition:** Note repeated phrases that signal structural intent.
* **Formatting:** Identify all Markdown elements, tables, and code blocks.

---

## 6. Phase 2: Terminology Extraction

Build a mental or scratchpad glossary *before* translating. For critical or recurring terms, define the Preferred Translation, Alternatives, and Forbidden Translations.

**Example Glossary Format:**
| Source Term | Preferred Translation | Forbidden Translation | Reason |
| :--- | :--- | :--- | :--- |
| 执行环境 | Execution environment | Runtime | Document specifically discusses infrastructure, not process execution. |
| 成立 | Confirmed | True / Valid / Correct | Maintain consistent evidential tone. |
| 裸金属服务器 | Bare-metal server | Physical machine | Industry-standard cloud terminology. |

Extracting terminology first prevents term drift and ensures industry-standard phrasing is used from the first sentence.

---

## 7. Phase 3: Style Calibration

Determine the stylistic conventions appropriate for the document type. 
* *Academic/RFC:* Passive voice acceptable, highly precise, objective.
* *Architecture Guide:* Objective, structural, explanatory.
* *README:* Imperative for instructions, descriptive for features.
* *Security Advisory:* Urgent, precise, cautious.

Calibrate your output to match these conventions. Avoid overly enthusiastic wording in analytical documents; avoid dry academic prose in tutorial READMEs.

---

## 8. Phase 4: Structural Preservation

Formatting is part of the document's meaning. Teach yourself to preserve structure meticulously.

Preserve exactly:
* Markdown headings (`#`, `##`, `###`)
* Tables (`|---|---|`)
* Bulleted and numbered lists (maintain exact nesting levels)
* Blockquotes (`>`)
* Horizontal rules (`---`)
* Code blocks (```` ``` ````) and inline code (` ` `)
* Links and footnotes
* Emphasis (`**bold**`, `*italic*`)

Never merge paragraphs to improve flow. Never split a long paragraph into two. Maintain the exact structural boundaries of the source.

---

## 9. Phase 5: Translation (Drafting)

During the drafting phase, distinguish between translation modes:
* **Literal translation:** Word-for-word. (Rarely appropriate, use only for simple noun phrases).
* **Faithful translation:** Preserves meaning and structure while adapting grammar for natural flow. (Preferred for technical documentation).
* **Idiomatic translation:** Prioritizes target-language idioms over source structure. (Rarely appropriate for technical docs).
* **Adaptive translation:** Changes format or context entirely. (Forbidden).

**Technical documentation should overwhelmingly favor *Faithful translation*.** Restructure a sentence only when the target language's grammar strictly demands it, while preserving emphasis and information order wherever possible.

---

## 10. Phase 6: Consistency Pass

After the initial draft is complete, perform a dedicated consistency pass. LLMs and humans often unconsciously introduce variation. 

Check for:
* Did "execution environment" become "runtime" halfway through?
* Did "claim" become "assertion" in section 4?
* Did "verification" become "validation" randomly?
* Did capitalization of product names change?

If a term was translated a specific way in the introduction, it must be translated that way in the conclusion.

---

## 11. Phase 7: QA Pass

Perform a final Quality Assurance pass focused strictly on structural and factual integrity. Consult the Quality Checklist (Section 22). 

Specifically scan for:
* Missing numbers, units, or version numbers.
* Changed filenames or code snippets.
* Lost Markdown formatting or broken table alignment.
* Dropped qualifiers (e.g., omitting "sub-100ms" or "under certain conditions").
* Hallucinated clarifications inserted into the text.

---

## 12. Handling Technical Terminology

Technical terms are the backbone of the document. 

* **Never translate** well-established acronyms or project names unless there is an official, widely accepted localization. (e.g., Linux, Docker, RustVMM, KVM, README, GitHub, API, SDK, JSON, YAML).
* **Translate concepts** using industry-standard English terminology rather than literal calques. (e.g., "写时复制" -> "copy-on-write (CoW)", not "write-time-copy").
* **Maintain capitalization:** If the source writes "MicroVM", do not write "micro-vm" or "microVM" unless the source is inconsistent.
* When introducing a translated term, it is often acceptable to include the original source term in parentheses on first use if ambiguity is likely.

---

## 13. Handling Product Names

Product names, filesystems, and specific technologies must remain untranslated and retain their exact original casing.

**Examples to keep verbatim:**
* CubeSandbox, CubeCoW
* Ubuntu, XFS, Ext4
* AutoPause, AutoResume
* E2B
* vmlinux, FICLONE, reflink

Do not attempt to translate these into descriptive phrases (e.g., never translate "AutoPause" to "Automatic Suspension").

---

## 14. Handling Numbers

Numbers, metrics, and performance figures are critical factual data points. 

**Never change:**
* Units (ms, MB, GB, cores)
* Precision (do not round 137ms to 140ms)
* Ranges (e.g., `<60ms`, `>2000`)
* Scientific notation
* Percentages
* Version numbers (v0.5.0)
* Dates (July 3, 2026)

If the source says `<5MB memory overhead`, do not write "less than 5 megabytes of memory overhead." Retain the exact numerical expression: `<5MB memory overhead`.

---

## 15. Handling Tables

Markdown tables must be preserved with their exact alignment.

* Translate only the textual contents of the cells.
* Keep the header row structure intact.
* Retain any special characters (e.g., ✅, ❌, ⚠️).
* Do not reorder the columns or rows.

**Example Target Table Structure:**
```markdown
| Claim Category | Core Claim | Verification Result | Key Evidence Sources |
| :--- | :--- | :--- | :--- |
| **Performance** | <60ms startup, <5MB memory | ✅ Confirmed | Official documentation |
```

---

## 16. Handling Markdown

Markdown formatting is a structural semantic element.

* Blockquotes (`>`) must remain blockquotes. They often denote original claims or cited material.
* Horizontal rules (`---`) act as section separators and must be retained exactly.
* Inline code (`` `code` ``) must be preserved precisely as inline code.
* Do not convert a bulleted list into a prose paragraph to "save space."

---

## 17. Handling Tone (Tone Lexicon)

Preserve the exact strength of the author's evaluation language. Use a consistent tone lexicon.

**Chinese to English Tone Mapping:**
| Source Tone | Preferred Translation | Forbidden Translation |
| :--- | :--- | :--- |
| 准确描述了 | accurately describes | perfectly describes |
| 得到证实 | confirmed | proven |
| 具有高度可信度 | highly credible | indisputably true |
| 成立 | Confirmed | Valid / True / Correct |
| 广泛讨论 | widely discussed | universally debated |
| 交叉验证 | cross-validated | cross-proven |

Do not exaggerate the author's claims, and do not soften the author's certainty.

---

## 18. Chinese → English Guidelines

When translating from Chinese to English technical documentation:

1. **Avoid excessive nominalization:** Chinese technical writing often stacks nouns. English prefers verbs. (e.g., "实现快速部署" -> "deploy quickly", not "achieve rapid deployment implementation").
2. **Restructure only when required:** Chinese allows long modifier chains before a noun (e.g., "基于RustVMM与KVM构建硬件隔离的MicroVM"). English requires breaking these up or using prepositional phrases ("MicroVMs built on RustVMM and KVM that provide hardware isolation").
3. **Consistent evaluation language:** If a document uses "成立" in a verification context, always use "Confirmed," not alternating between "Valid," "True," or "Correct."
4. **Use established terminology:** Do not create literal calques. (e.g., "宿主机" -> "host machine", not "host-machine").

---

## 19. English → Chinese Guidelines

When translating from English to Chinese technical documentation:

1. **Avoid translationese:** Do not write Chinese that strictly follows English syntax. Use natural Chinese technical writing conventions.
2. **Concise expressions:** Use four-character idioms where appropriate and natural in technical contexts (e.g., "毫发无损" for "remains unaffected", "无缝迁移" for "seamless migration").
3. **Retain English product names:** Unless there is a universally accepted official Chinese name (e.g., "Ubuntu" stays "Ubuntu").
4. **Punctuation conventions:** Use full-width punctuation (，。：) for Chinese prose, but retain half-width punctuation (`, . :`) inside code blocks, inline code, and URLs.
5. **Preserve Markdown structure:** Ensure that Markdown syntax does not break when adapting Chinese full-width characters.

---

## 20. Common Failure Modes

Be vigilant against these common LLM translation errors:

* **Over-literal translation:** Producing awkward, unidiomatic phrasing.
* **Over-localization:** Changing units, currency, or product names unnecessarily.
* **Over-editing:** Rewriting the author's sentences to "make them better."
* **Summarization:** Condensing two paragraphs into one.
* **Hallucinated clarification:** Adding definitions or context not present in the source.
* **Dropped qualifiers:** Omitting words like "sub-", "approximately", or "under certain conditions."
* **Inconsistent terminology:** Using "snapshot" in section 1 and "screen capture" in section 2.
* **Reordered arguments:** Moving bullet points or sentences because it "flows better."
* **Changing certainty:** Modifying "might" to "will" or "confirmed" to "likely."
* **Breaking Markdown:** Dropping `>` symbols or failing to align table cells.
* **Changing list nesting:** Moving a sub-bullet to a top-level bullet.

---

## 21. Translation Decision Framework

Whenever you are uncertain about how to translate a phrase, do not guess. Run the phrase through this deterministic decision tree:

```text
Does the proposed translation preserve the exact Meaning?
  ├─ No → Revise.
  └─ Yes ↓

Does it preserve the Evidence/Facts?
  ├─ No → Revise.
  └─ Yes ↓

Does it use the established Terminology?
  ├─ No → Revise.
  └─ Yes ↓

Does it preserve the Document Structure (Markdown/formatting)?
  ├─ No → Revise.
  └─ Yes ↓

Does it match the author's Tone/Certainty?
  ├─ No → Revise.
  └─ Yes ↓

Is it Readable in the target language?
  ├─ No → Restructure grammar (only), then re-evaluate.
  └─ Yes → PROCEED.
```

---

## 22. Quality Checklist

Before outputting the final translation, verify every item on this list:

* [ ] No missing paragraphs or sentences.
* [ ] No omitted bullets or list items.
* [ ] No changed or reworded headings.
* [ ] No altered code blocks or inline code.
* [ ] All numbers, units, and version numbers are unchanged.
* [ ] All product names, filenames, and filesystems remain untranslated.
* [ ] Terminology is internally consistent throughout the entire document.
* [ ] Tone and strength of certainty are preserved (no strengthening/weakening).
* [ ] Document structure and hierarchy are preserved.
* [ ] All Markdown formatting (tables, blockquotes, rules) is preserved.
* [ ] Table alignments and special characters (✅) are preserved.
* [ ] Links and footnotes are preserved.
* [ ] No factual information has been added or deleted.
* [ ] The target prose reads naturally to a native speaker.
* [ ] The document reads as though it were originally written in the target language.

---

## 23. Example Workflow

**Scenario:** Translating a Chinese verification report on a cloud sandbox project.

1. **Read & Analyze:** Identify it as a formal, evidence-based technical report. The audience is technical engineers. The tone is analytical and authoritative.
2. **Extract Terminology:**
   * 核心声明 -> Core claim (NOT: core statement)
   * 验证结果：✅ 成立 -> Verification Result: ✅ Confirmed (NOT: Result: True)
   * 沙箱 -> sandbox
   * 裸金属服务器 -> bare-metal server
3. **Determine Style:** Formal English technical documentation. Use precise verbs. Avoid marketing language.
4. **Translate:** Execute the draft, preserving all `>` blockquotes, `---` rules, and `| Table |` structures.
5. **Consistency Pass:** Ensure "MicroVM" is never written as "micro VM". Ensure "confirmed" is used every time "成立" appears.
6. **QA Pass:** Check that `<60ms` was not accidentally changed to `60ms`. Check that `v0.5.0` is exact. Verify all `✅` symbols are present in the table.

---

## 24. Success Criteria

A translation executed under this skill is considered successful only if it satisfies all the following conditions:

1. A domain expert would consider the technical content strictly equivalent to the source.
2. A native speaker would not recognize it as a literal or machine translation.
3. Formatting, hierarchy, and document structure are perfectly preserved.
4. Terminology remains internally consistent throughout the entirety of the text.
5. No factual information has been added, omitted, strengthened, or weakened.
6. The translated document could be published directly in a professional context without requiring substantive editorial revision.

---

https://chat.z.ai/s/6c7a90a7-e193-450b-8237-2ddbb8684f6d 
