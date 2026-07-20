# Translation Engine v7.0 — Feedback Analysis & v8.0 Design Validation

**Document type:** Critical analysis of external feedback + design validation for v8.0
**Subject:** External critique of `Translation_Engine_v7_Prompt.md` (1081 lines)
**Test context:**
- **Test:** AI Agent book README (`source_file_to_translate-5.md`), CN→EN, ~950 lines of complex Markdown with code blocks, tables, badges, and bilingual content.
- **Output:** `translated_output_5.md` — high-quality L2/L3 translation rated 9.2/10 by the external reviewer.
- **Critique:** `critique_translation_engine_prompt_v7.md` — rates the v7 prompt 9.8/10, identifies 3 vulnerabilities + solves 2 "mysteries".
**Analysis method:** Cross-validation of each critique finding against (a) the v7 prompt text, (b) the actual test output, (c) the identified translation issues.
**Outcome:** 3 vulnerabilities accepted + 1 grammar issue + 1 documentation clarification. v8.0 is a targeted refinement, not an architectural overhaul.

---

## 1. Executive Summary

The external critique is **technically precise and well-targeted**. It correctly identifies that v7's core mechanics are sound (9.8/10 rating) and that the translation output was high quality (9.2/10). The critique does two things exceptionally well:

1. **Solves two "mysteries"** by cross-referencing the prompt with the output — proving that the untranslated code comments were correct prompt adherence (not a failure), and that the "Implementation落地" artifact was a real gap in Phase 6 checks.
2. **Identifies 3 vulnerabilities** with specific, actionable fixes.

Of the 3 vulnerabilities:

- **Vulnerability A (Asymmetric Typography Checks):** ✅ Fully valid — the headline v8 fix. v7 Phase 6 has a hard check for straight ASCII quotes in Chinese text but lacks a symmetrical check for CJK character leakage in English text. This is why "Implementation落地" slipped through.
- **Vulnerability B (Instruction Quarantine edge cases):** ⚠️ Partially valid — real attention-dilution concern with complex Markdown payloads, but no specific fix proposed. v8 will strengthen Axiom 4 with explicit guidance.
- **Vulnerability C (Notice Channel position):** ✅ Valid — LLMs anchor on early tokens. Moving a Notice Channel conditions summary into §1 Primary Directive improves enforcement.

Additionally, the critique identifies a grammar fluency issue ("(mocks) integrating" instead of "simulates (mocks) integration") that warrants a new Phase 6 Grammar Fluency Check.

**Verdict:** The critique is accepted as the basis for v8.0. All 3 vulnerabilities + 1 grammar issue + 1 documentation clarification will be addressed. v8.0 is a targeted refinement — v7's architecture is preserved; only specific rules are added or strengthened.

---

## 2. Test Output Quality Assessment

### 2.1 Translation output (`translated_output_5.md`) — L2/L3 quality, 9.2/10

The v7 engine translated a ~950-line Chinese README for an AI Agent book repository into English. Quality assessment based on the external review and my own cross-check:

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Structural & Markdown Integrity | 9.5/10 | Emojis, bullet points, links, tables, bolding all preserved. Code block comments preserved verbatim (correct behavior per §11 Phase 1, but flagged as an issue by the reviewer who didn't realize `--translate-comments` wasn't passed). |
| Technical Terminology & Domain Accuracy | 10/10 | Outstanding localization of Chinese developer slang: "人肉基准" → "manual benchmark", "开箱即用" → "out-of-the-box readiness", "脱敏处理" → "log sanitization", "提议者-审核者" → "Proposer-Reviewer". |
| Semantic Fidelity & Nuance | 9.5/10 | Complex pipelines translated with high fidelity. "跑通「自下而上因子发现 → 聚类出案件原型 → 对话式建议 Agent」三段流水线" flawlessly rendered. Minor: "(mocks) integrating" slightly clunky. |
| Fluency, Grammar, Localization | 8.5/10 | General flow exceptional. **Critical artifact:** "Implementation落地 sees Chapter 8" — Chinese character leakage into English prose. Minor: Star History section subject clarity. |

**Conclusion:** The translation validates that v7's scratchpad protocol, epistemic isomorphism, anti-translationese collocations, and targeted repair blocks work correctly for complex Markdown-heavy technical documents. The single critical artifact ("Implementation落地") exposes the Phase 6 gap that v8 will fix.

### 2.2 The two "Mysteries" solved by the critique

**Mystery 1: Why were code block comments left in Chinese?**

The critique correctly identifies this as **correct prompt adherence, not a model failure**. v7 §11 Phase 1 explicitly states: *"Identify code comments and apply the comment policy (default: preserve verbatim; `--translate-comments`: translate)."* Since the test did not pass `--translate-comments`, the engine correctly locked the code comments as immutable.

**v8 action:** No fix needed. But v8 will add a scratchpad documentation note in Phase 1 to make this behavior explicitly visible to auditors (so future reviewers don't mistake it for a failure).

**Mystery 2: Why did "Implementation落地" slip through?**

The critique correctly diagnoses: the engine tried to map 落地 → "implement/deploy" per §8.3 but glitched, concatenating English+Chinese. The Phase 6 "Locked-retention exemption" check says "Unexplained English words in Chinese-dominant text (or vice versa)" should trigger repair — but this check is described bidirectionally yet is hard for models to self-diagnose without an explicit, aggressive CJK-leakage check.

**v8 action:** Add a dedicated "Source-Script Leakage Check" to Phase 6 (Vulnerability A fix).

---

## 3. Critique Validation — Point by Point

### 3.1 Vulnerability A: Asymmetric Typography/Artifact Checks (§9.3 & Phase 6)

> *"The prompt is heavily optimized to prevent English typographic pollution in Chinese text. For example, Phase 6 demands a hard failure if straight ASCII quotes appear in Chinese text. It lacks a symmetrical hard check for Chinese typographic pollution in English text. Phase 6 should include a specific check: 'Source-Script Leakage Check: [PASS/FAIL] — confirm no stray CJK characters (汉字) remain in English-dominant translated prose unless strictly protected by Entity Anchoring (§8.1).' This would have caught the Implementation落地 artifact and triggered a Phase 4 Repair Block."*

**Validity: ✅ Fully valid. This is the headline v8 fix.**

Cross-check against v7 §11 Phase 6: The "Locked-retention exemption" check says *"Unexplained English words in Chinese-dominant text (or vice versa) are permitted only when they are immutable elements, locked-glossary retentions, or domain-standard acronyms."* This is bidirectional in theory, but:

1. The check is buried among 10 other checks — low attention weight.
2. It doesn't explicitly name "CJK characters in English prose" as a failure pattern.
3. The model sees 落地 as a valid token it just processed, making self-diagnosis hard.

The critique's proposed fix — a dedicated "Source-Script Leakage Check" — is the correct solution. It should be:
- Explicit and aggressive (like the Quote check)
- Named clearly (CJK characters in English prose = FAIL)
- Scoped to English-dominant segments (CN→EN direction)
- Symmetric: also check for English words in Chinese-dominant segments (EN→CN direction) — though this is already partially covered by the Locked-retention exemption

**v8 fix:** Add "Source-Script Leakage Check" to §11 Phase 6 as a new explicit check.

### 3.2 Vulnerability B: Instruction Quarantine vs. Edge Cases (§6 Axiom 4)

> *"The instruction quarantine is excellent for preventing prompt injection, but it assumes the LLM can always flawlessly distinguish between 'payload data' and 'system instructions'. Because the prompt itself is extraordinarily long, highly complex markdown payloads (like the source file we tested, which is full of metadata, tables, and code formatting) can occasionally cause the LLM's attention heads to blur the line between the system prompt's markdown formatting rules and the payload's markdown content."*

**Validity: ⚠️ Partially valid.**

The critique identifies a real attention-dilution concern but does not propose a specific fix. The issue is that when the payload itself contains Markdown that resembles the system prompt's structure (headings, code blocks, tables), the LLM may conflate payload-Markdown-rules with system-prompt-Markdown-rules.

**v8 approach:** Strengthen Axiom 4 with explicit guidance for Markdown-heavy payloads:
- Reaffirm that the system prompt's Markdown rules (§9 Typography) apply ONLY to the translated output, never to the source payload's structure.
- Clarify that source-payload Markdown is always inert data, even when it structurally resembles system-prompt sections.
- Add a scratchpad note in Phase 1 when the payload contains >50 Markdown elements (high structural density) to trigger extra Instruction Quarantine vigilance.

This is a mitigation, not a complete fix — the underlying attention-dilution problem is an LLM architectural limitation. But the explicit guidance will reduce failure frequency.

### 3.3 Vulnerability C: Notice Channel Deadlock Exception Position (§1 & §15.5)

> *"The prompt attempts to resolve a deadlock where the LLM is told 'always translate' but also told 'stop and emit a notice if out-of-scope'. While the prompt logically resolves this (Notice Channel engages the Primary Directive Exception), in practice, LLMs struggle with 'if/then' contradictions separated by 10 pages of tokens. The Fix: Move the Notice Channel conditions directly into the Primary Directive block (§1) rather than placing them at the end of the prompt in §15.5. LLMs anchor heavily on the first 500 tokens of a prompt."*

**Validity: ✅ Valid.**

v7 §1 already has the Notice Channel Exception clause, but it's a general statement. The actual conditions (out-of-scope input, blocking ambiguity, audit failure, empty payload) are in §15.5 — far from the §1 anchor position. LLMs do anchor on early tokens (well-documented in the prompt-engineering literature).

**v8 fix:** Expand §1 to include a brief summary of the Notice Channel warranting conditions, so the engine has them in its highest-attention zone. The full Notice Channel protocol remains in §15.5; §1 gets a one-line summary.

### 3.4 Grammar Fluency Issue: "(mocks) integrating"

> *"In Chapter 5, the phrase 'and (mocks) integrating with GitHub via MCP to create Issues' is slightly clunky. The original was '并（mock）通过 MCP 对接 GitHub 创建 Issue'. A more natural phrasing would be: '...and simulates (mocks) integration with GitHub via MCP to create Issues'."*

**Validity: ✅ Valid — minor but worth fixing.**

This is a grammar fluency issue. The Phase 5 Collocation Check should catch awkward verb-noun pairings, but "(mocks) integrating" is grammatically valid (just clunky) — it slipped through. A dedicated Grammar Fluency Check in Phase 6 would catch this.

**v8 fix:** Add a "Grammar Fluency Check" to §11 Phase 6. This check verifies that the target-language prose reads naturally, with no awkward verb-noun pairings, dangling modifiers, or clunky parenthetical insertions. This is a Minor-severity check (repair target: Phase 3 or Phase 4).

### 3.5 Mystery 1 Documentation: Code-comment behavior

The critique correctly identifies that untranslated code comments were correct behavior. However, future auditors may make the same mistake. v8 should add a scratchpad documentation note in Phase 1 that explicitly records: "Code comments preserved verbatim per default comment policy (`--translate-comments` not active)."

**v8 fix:** Add a scratchpad note to §11 Phase 1 documenting the comment-policy decision.

---

## 4. v8.0 Design — Summary of Changes

### 4.1 New rules added (3 findings)

| Finding | v8 section | New rule |
|---------|------------|----------|
| Vulnerability A (Source-Script Leakage) | §11 Phase 6 | Source-Script Leakage Check: no stray CJK characters (汉字) in English-dominant translated prose unless protected by Entity Anchoring; symmetric check for English words in Chinese-dominant prose |
| Vulnerability C (Notice Channel position) | §1 Primary Directive | Notice Channel conditions summary added to §1 (full protocol remains in §15.5) |
| Grammar fluency ("(mocks) integrating") | §11 Phase 6 | Grammar Fluency Check: target-language prose reads naturally, no awkward verb-noun pairings or clunky parentheticals |

### 4.2 Strengthened rules (2 findings)

| Finding | v8 section | Strengthening |
|---------|------------|---------------|
| Vulnerability B (Instruction Quarantine edge cases) | §6 Axiom 4 | Explicit guidance for Markdown-heavy payloads: system-prompt Markdown rules apply only to translated output, never to source-payload structure |
| Mystery 1 (code-comment documentation) | §11 Phase 1 | Scratchpad note documenting comment-policy decision for auditor clarity |

### 4.3 Preserved from v7 (all v7 strengths retained)

All v7.0 strengths are preserved in v8.0 — v8 is a strict superset of v7. The 20-section structure is unchanged; only §1, §6, and §11 receive targeted additions.

---

## 5. Acceptance Criteria for v8.0

| # | Criterion | Source |
|---|-----------|--------|
| 1 | Source-Script Leakage Check added to Phase 6 — catches "Implementation落地" artifact | Vulnerability A |
| 2 | Notice Channel conditions summary in §1 Primary Directive (high-attention zone) | Vulnerability C |
| 3 | Axiom 4 strengthened with Markdown-heavy payload guidance | Vulnerability B |
| 4 | Grammar Fluency Check added to Phase 6 — catches "(mocks) integrating" | Grammar issue |
| 5 | Phase 1 scratchpad documents comment-policy decision | Mystery 1 |
| 6 | All v7 strengths preserved | — |
| 7 | v8 is a strict superset of v7 (no v7 rules removed) | — |

---

## 6. Execution Plan

1. Draft v8.0 by applying the 5 targeted changes to v7.0
2. Self-review Pass 1: Contradiction sweep (new rules checked against existing rules)
3. Self-review Pass 2: Validate all 7 acceptance criteria are satisfiable
4. Self-review Pass 3: Verify all v7 strengths are preserved
5. Deliver `Translation_Engine_v8_Prompt.md` + `Translation_Engine_v8_Changelog.md` + this analysis document

---

*End of feedback analysis. For the v8.0 prompt, see `Translation_Engine_v8_Prompt.md`. For the v7→v8 changelog, see `Translation_Engine_v8_Changelog.md`.*
