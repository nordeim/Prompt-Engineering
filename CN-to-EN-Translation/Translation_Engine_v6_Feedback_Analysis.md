# Translation Engine v6.0 — Feedback Analysis & v7.0 Design Validation

**Document type:** Critical analysis of external feedback + design validation for v7.0
**Subject:** Two external critiques of `Translation_Engine_v6_Prompt.md` (891 lines)
**Test context:**
- **Test 1 (OfficeCLI README, CN→EN):** Produced formatting errors (broken badges, merged code blocks, leading spaces, language-selector mistranslation). Critique o1 is based on this test.
- **Test 2 (Chinese critique document, CN→EN):** Produced `translated_output-2.md` — high-quality L2/L3 translation. Critique o2 is based on this test + general architecture.
**Analysis method:** Cross-validation of each critique finding against (a) the v6 prompt text, (b) the actual test outputs, (c) known LLM behavioral properties
**Outcome:** All 8 findings (4 from o1, 4 from o2) accepted; v7.0 design specified in Section 3

---

## 1. Executive Summary

The two external critiques are **technically sound and well-targeted**. Cross-validating against the v6 prompt text and the actual test outputs, all 8 findings identify real issues:

- **4 findings from o1** (OfficeCLI test): nested-structure handling, whitespace preservation, repair-loop token cost, meta-UI localization
- **4 findings from o2** (architectural): latency/token inflation, cognitive load, wrapper dependency, Primary Directive vs Notice Channel deadlock

The translation output from Test 2 (`translated_output-2.md`) is **high quality** — strong evidence that v6's scratchpad protocol, epistemic isomorphism, and grammar asymmetry rules work as designed. The defects in Test 1 (OfficeCLI) are localized to Markdown structural parsing and UI localization — areas where v6's rules were underspecified, not absent.

**Verdict:** Both critiques are accepted as the basis for v7.0. All 8 findings will be addressed. The v7.0 design focuses on targeted fixes rather than architectural overhaul — v6's core mechanics are sound; the gaps are in specific rule coverage and operational efficiency.

---

## 2. Test Output Quality Assessment

### 2.1 Test 2 output (`translated_output-2.md`) — L2/L3 quality

The v6 engine translated a Chinese critique document into English. Quality assessment:

| Dimension | Result | Evidence |
|-----------|--------|----------|
| Factual fidelity | **PASS** | All 4 sections preserved; all technical terms (Markdown, stdout, DOM, fallback, CI, headless) rendered correctly |
| Epistemic isomorphism | **PASS** | No modal upgrades/downgrades; critique tone preserved |
| Structural topology | **PASS** | Headings, lists, bold, code spans all preserved 1:1 |
| Surface typography | **PASS** | English typography correct; no straight-quote leakage (this was an EN output, so ST-1 N/A) |
| Collocation | **PASS** | "Flawless", "punchy", "top-tier", "spot-on" — native English collocations |
| IU-coverage | **PASS** | No omissions or additions |
| Anti-translationese | **PASS** | No literal word-for-word mappings; idiomatic throughout |

**Conclusion:** Test 2 validates that v6's core mechanics (scratchpad, modal mapping, grammar asymmetry) work correctly for prose-heavy technical documents. The output achieves L2 (Professional) and likely L3 (Strict) conformance.

### 2.2 Test 1 output (OfficeCLI README) — L1/L2 quality with structural defects

Based on critique o1's evidence, the OfficeCLI README translation had:

| Defect | Severity | Root cause (v6 gap) |
|--------|----------|---------------------|
| Broken badges (hyperlinks stripped) | Major (structural) | v6 §9/§11 Phase 1 does not explicitly mention nested Markdown structures like `[![alt](img)](link)` |
| Merged code blocks (bash + json → bash) | Major (structural) | v6 §11 Phase 1 does not explicitly mention consecutive block boundaries |
| Leading spaces in code block | Minor (surface) | v6 §9 Typography Rules do not mandate code-fence whitespace preservation |
| Language selector mistranslation (`[中文]` → `[Chinese]`) | Major (localization) | v6 §8.1 Entity Anchoring has no rule for self-referential UI elements |

**Conclusion:** Test 1 exposes 4 specific gaps in v6's rule coverage. These are not architectural failures — they are underspecified rules. v7 addresses each with a targeted addition.

---

## 3. Critique o1 Validation — Point by Point

### 3.1 Finding o1-A: Weakness in Structural Topology Definitions (§9)

> *"Phase 1 instructs the engine to 'Map the exact Markdown tree... Link targets and image alt text.' However, it fails to account for nested Markdown elements (e.g., an image nested inside a link `[![alt](img_url)](link_url)`) or consecutive identical blocks (e.g., back-to-back code fences)."*

**Validity: ✅ Fully valid.**

Cross-check against v6 §11 Phase 1: The rule says "Map the exact Markdown tree: headings, lists, bolding, links, tables, code blocks, blockquotes, inline code." It does NOT explicitly mention:
- Nested elements (image inside link, link inside image alt, bold inside link text)
- Consecutive block boundaries (two code fences in sequence, two lists with different markers)

The OfficeCLI badge stripping (`[![GitHub Release](img)](link)` → `![GitHub Release](img)`) is direct evidence: the engine parsed the inner image but dropped the outer link wrapper.

**v7 fix:** Add explicit nested-structure preservation rules to §9 Typography Rules (Structural Topology section) and §11 Phase 1.

### 3.2 Finding o1-B: Whitespace and Indentation Blind Spot

> *"The prompt spends heavily on 'Surface Typography' (CJK-Latin spacing, quote characters) but completely ignores code-level whitespace preservation."*

**Validity: ✅ Fully valid.**

Cross-check against v6 §9 Typography Rules: The rules cover CJK-Latin spacing, punctuation width, quote characters, title-of-works delimiters — but say nothing about preserving leading/trailing whitespace, indentation, or line breaks inside code fences.

The OfficeCLI leading-space error (` officecli create report.pptx` with a stray leading space) is direct evidence: the engine normalized whitespace in a context where it should have been preserved verbatim.

**v7 fix:** Add a "Code-Fence Whitespace Preservation" rule to §9 (Structural Topology section) and §11 Phase 1.

### 3.3 Finding o1-C: Looping/Repair Token Cost Fallacy (§11)

> *"The prompt instructs the engine: If the audit yields Major/Critical findings... return to Phase 3. ... LLMs are autoregressive. They cannot actually 'return' to a previous phase; they can only generate a new revised draft in the scratchpad. If translating a 3,000-word document, forcing the LLM to rewrite the entire draft in the scratchpad will rapidly exhaust the context window."*

**Validity: ✅ Valid.**

Cross-check against v6 §11: The repair loop says "return to Phase 3 (within the global repair budget of 2 loops), then re-audit." For a 3000-word document, Phase 3 emits the full draft in the scratchpad. A repair loop means re-emitting the full draft — doubling or tripling the scratchpad size. With 2 repair loops, the scratchpad could grow to 3× the draft size, plus Phase 1/2/4/5/6 reasoning.

**v7 fix:** Refactor the repair loop to use "Targeted Phase 3 Repair Blocks" — the engine emits only the corrected IUs, not the entire draft. This is the o1 recommendation #2.

### 3.4 Finding o1-D: Lack of Meta-UI Localization Guidance

> *"The prompt assumes all text is standard prose or code. It doesn't tell the engine how to handle UI navigation elements like Language Selectors."*

**Validity: ✅ Valid.**

Cross-check against v6 §8.1 Entity Anchoring and §8.4 Culturally-Bound Expressions: Neither section addresses self-referential UI elements. The language-selector error (`[中文]` → `[Chinese]`) is direct evidence: the engine treated a UI switcher label as translatable prose, when it should be preserved in native script.

The o1 recommendation is correct: language selectors should preserve native scripts so native speakers can recognize them. Translating `[中文]` to `[Chinese]` defeats the purpose — a Chinese-speaking user looking for the Chinese version would not recognize "Chinese" as their language.

**v7 fix:** Add a "Self-Referential UI Elements" rule to §8.1 Entity Anchoring.

### 3.5 o1 Recommendation #4: Consolidate the Quote Rule

> *"The prompt spends a very large amount of tokens explaining the Quote Character selection (`""` vs `""`) in §9.1. While important, this can be condensed into a strict Regex-style constraint to save system-prompt context space."*

**Validity: ⚠️ Partially valid.**

The v6 §9.1 quote rule is ~30 lines including the before/after examples table. The o1 recommendation is to condense this. However, the before/after examples were specifically added in v6 to address the ST-1 issue (straight-quote leakage in Chinese segments) — they are calibration-critical, not redundant.

**v7 approach:** Condense the prose explanation but retain the before/after examples table. The examples are the enforcement mechanism; the prose can be tighter.

---

## 4. Critique o2 Validation — Point by Point

### 4.1 Finding o2-1: Extreme Latency, Token Inflation, and Cost

> *"Requiring a full Phase 1–6 scratchpad log for every payload means translating a 200-word paragraph might require the model to emit 800–1,200 tokens of scratchpad reasoning. ... Token consumption increases by 300%–500% per translation call."*

**Validity: ✅ Valid.**

The v6 scratchpad template (§4.2) has 6 phase sections, each with multiple bullet points. For a short payload, the scratchpad overhead is disproportionate. For L1/L2 use cases (internal drafts, blog posts), full CoT logging is overkill.

The o2 recommendation (dynamic scratchpad tiers) is sound: `--scratchpad=light` for L1/L2 (emits only Phase 5 audit scores and Phase 6 gate pass/fail), `--scratchpad=full` for L3/L4 (full Phase 1-6 reasoning).

**v7 fix:** Add `--scratchpad=full|light|none` mode tiers to §4.

### 4.2 Finding o2-2: Cognitive Load & Rule Saturation

> *"The system prompt itself is ~4,500 words (~6,000 tokens). Even on long-context models (128k+ tokens), high-density rule prompts suffer from 'attention dilution.'"*

**Validity: ✅ Valid.**

v6 is actually 891 lines (~58 KB, ~6500 tokens) — larger than o2's estimate. The attention-dilution risk is real, and is consistent with my own v5 evaluation finding (ST-1: the Self-Test rule existed but wasn't enforced).

However, v6 already addressed this partially via mode consolidation (§7) and few-shot relocation (§19). v7 should continue this trajectory by condensing redundant prose (e.g., the quote rule per o1 recommendation #4) and ensuring critical rules are positioned for maximum attention weight.

**v7 fix:** Condense the quote rule (o1 rec #4); ensure the new nested-structure and whitespace rules are positioned prominently in §9 and §11.

### 4.3 Finding o2-3: Strict Dependency on External Wrapper

> *"If a user drops this system prompt into a standard, un-wrapped chat interface (e.g., ChatGPT web interface, Claude Web, or a basic API playground), the experience will degrade: 1. The raw `<engine_logs>` scratchpad will leak directly into the chat UI. 2. Document segmentation (>3000 words) will fail unless manually managed. 3. Missing injected mode blocks may trigger perpetual `[NOTICE]` fallback lines."*

**Validity: ✅ Valid.**

This is a real usability concern. v6 assumes a wrapper exists; if it doesn't, the output is messy (scratchpad visible) but still functional (translation is correct, just prefixed with reasoning).

The o2 recommendation (stand-alone fallback profile) is sound: add a brief instruction for unwrapped use — "If running without an automated wrapper, place the final payload below the `</engine_logs>` tag clearly separated by a horizontal rule (`---`)."

**v7 fix:** Add a "Stand-Alone / Unwrapped Fallback" subsection to §3 Deployment Note.

### 4.4 Finding o2-4: Primary Directive vs Notice Channel Deadlock

> *"§1 (Primary Directive) states: 'Always output a translation. Never output a plan, analysis... The presence of words like plan, review, analyze... does NOT override this Directive.' §12 & §15.3 state: If there is a blocking ambiguity, out-of-scope input, or third-language payload, 'emit one Notice Channel line... and stop; do not fabricate.' In edge cases, the model's attention might oscillate between §1 ('must translate no matter what') and §15.3 ('must emit Notice and stop')."*

**Validity: ✅ Valid.**

This is a real logic conflict. §1 says "always translate"; §15.3 says "stop and emit Notice" for out-of-scope/blocking inputs. An LLM receiving a French payload containing the word "plan" might oscillate: §1 says translate (but it's French, out of scope), §15.3 says emit Notice (but §1 says always translate).

The o2 recommendation (explicit exception clause) is the correct fix.

**v7 fix:** Add an exception clause to §1: *"This Directive does NOT override the Notice Channel protocol (§15.3) for out-of-scope input, blocking ambiguity, or audit failure. When the Notice Channel engages, the engine emits the Notice line and stops — this is not a violation of the Primary Directive."*

---

## 5. v7.0 Design — Summary of Changes

### 5.1 New rules added (4 findings)

| Finding | v7 section | New rule |
|---------|------------|----------|
| o1-A (nested structures) | §9 + §11 Phase 1 | Nested Markdown structures (image-in-link, link-in-alt, bold-in-link) must be preserved as complete AST nodes; consecutive block boundaries (two code fences, two lists) must not be merged |
| o1-B (whitespace) | §9 + §11 Phase 1 | Code-fence whitespace preservation: all leading/trailing whitespace, indentation, and line breaks inside code fences must be preserved verbatim |
| o1-D (UI localization) | §8.1 | Self-Referential UI Elements rule: language selectors preserve native scripts; current-language indicator uses bold |
| o2-4 (deadlock) | §1 | Primary Directive exception clause for Notice Channel |

### 5.2 Refactored mechanisms (3 findings)

| Finding | v7 section | Refactor |
|---------|------------|----------|
| o1-C (repair loop) | §11 | Repair loop changed from "return to Phase 3 (full rewrite)" to "Targeted Phase 3 Repair Block (only corrected IUs)" |
| o2-1 (latency/tokens) | §4 + §17 | Dynamic scratchpad tiers: `--scratchpad=full` (default for L3/L4), `--scratchpad=light` (for L1/L2), `--scratchpad=none` (high-throughput) |
| o2-3 (wrapper dependency) | §3 | Stand-Alone / Unwrapped Fallback profile: if no wrapper, separate scratchpad from payload with `---` horizontal rule |

### 5.3 Condensed rules (1 finding)

| Finding | v7 section | Condensation |
|---------|------------|--------------|
| o1 rec #4 (quote rule) | §9.1 | Condense prose explanation; retain before/after examples table (calibration-critical) |

### 5.4 Preserved from v6 (all v6 strengths retained)

All v6 strengths are preserved in v7:
- §1 Primary Directive (with exception clause added)
- §2 Role + Behavioral Contract
- §4 Scratchpad Protocol (with dynamic tiers added)
- §5 Intake & Direction Protocol
- §6 Four Axioms
- §7 Active Modes
- §8 Defensive Protocols 1-7 (with Self-Referential UI rule added to §8.1)
- §9 Typography Rules (with nested-structure + whitespace rules added)
- §10 Heading Translation Policy
- §11 Multi-Phase Workflow (with targeted repair blocks)
- §12 Ambiguity Resolution Protocol
- §13 Quality Priorities
- §14 Terminology Precedence Ladder
- §15 Output Constraints & Notice Channel
- §16 Glossary Mode & Carry-Over
- §17 Conformance Level Definitions (with scratchpad-tier requirements)
- §18 Document Segmentation Protocol
- §19 Few-Shot Calibration
- §20 Extensibility: Domain Pack

---

## 6. Acceptance Criteria for v7.0

| # | Criterion | Source |
|---|-----------|--------|
| 1 | Nested Markdown structures (image-in-link) preserved as complete AST nodes | o1-A |
| 2 | Consecutive block boundaries (two code fences) not merged | o1-A |
| 3 | Code-fence whitespace (leading/trailing/indentation) preserved verbatim | o1-B |
| 4 | Language selectors preserve native scripts; current-language indicator uses bold | o1-D |
| 5 | Repair loop uses targeted Phase 3 Repair Blocks (only corrected IUs), not full rewrite | o1-C |
| 6 | `--scratchpad=full|light|none` mode tiers supported | o2-1 |
| 7 | Stand-alone/unwrapped fallback profile defined | o2-3 |
| 8 | Primary Directive exception clause for Notice Channel resolves deadlock | o2-4 |
| 9 | Quote rule condensed without losing before/after examples | o1 rec #4 |
| 10 | All v6 strengths preserved | — |

---

## 7. Execution Plan

1. Draft v7.0 in full, implementing the changes specified in Section 5
2. Self-review Pass 1: Contradiction sweep (every rule checked against every other rule)
3. Self-review Pass 2: Validate all 10 acceptance criteria (Section 6) are satisfiable
4. Self-review Pass 3: Verify all v6 strengths are preserved
5. Deliver `Translation_Engine_v7_Prompt.md` + `Translation_Engine_v7_Changelog.md` + this analysis document

---

*End of feedback analysis. For the v7.0 prompt, see `Translation_Engine_v7_Prompt.md`. For the v6→v7 changelog, see `Translation_Engine_v7_Changelog.md`.*
