# Translation Engine v4.0 → v5.0 Changelog

**Subject:** `System Prompt: Deterministic Forensic Translation Engine`
**Change type:** Major revision (38 findings addressed: 8 Critical, 11 High, 13 Medium, 6 Low)
**Audit document:** `Translation_Engine_v4_Audit_and_v5_Plan.md`
**v5.0 artifact:** `Translation_Engine_v5_Prompt.md` (629 lines, ~47 KB)

This changelog maps every v4.0 section/line to its disposition in v5.0, with the finding IDs that drove each change. It serves as the traceability artifact required by the v5 plan's execution step 4.

---

## Summary by Section

| v4.0 Section | Disposition in v5.0 | Finding IDs |
|---|---|---|
| Header + Role (lines 1–4) | Revised: behavioral-determinism contract replaces decoding-parameter claim | C1 |
| System Parameters (lines 6–9) | Split: behavioral contract stays in Role block; literal decoding settings moved to "Deployment Note" block labeled as operator guidance | C1 |
| Core Philosophy (3 Axioms) | Preserved + extended: Axiom 1 gains licensed-deviation note reconciling with idiom handling; new Axiom 4 (Instruction Quarantine) | H8 |
| Defensive Protocol 1 — Entity Anchoring | Preserved + extended: bidirectional; new person/place/case/honorific sub-protocol; corrected exemplar split (translated vs preserved); term-authority ladder | H6, M1, M3 |
| Defensive Protocol 2 — Modal & Epistemic Mapping | Preserved + extended: all tables bidirectional; new `shall`; new Financial markers; new Statistical-claims markers | H2, H3, M11, M12 |
| Defensive Protocol 3 — Anti-Translationese | Preserved (S3) + extended with additional collocations | — |
| Defensive Protocol 4 — Culturally-Bound Expressions | Preserved (S8) + refined; linked to `--notes` mode | — |
| Defensive Protocol 5 — Source Error / OCR | Preserved + linked to `--notes` mode | L4 |
| (new) Defensive Protocol 6 — Grammar Asymmetry | Added: tense/aspect, number, definiteness, gender-unknown pronouns | H4 |
| (new) Defensive Protocol 7 — Quantity & Locale Conventions | Added: numeric-equivalence standard, currency, dates, units, percent/ranges | H5, C6 |
| Mandatory Multi-Phase Workflow | Revised: single global repair budget (≤2 audit loops; other phases execute once); Phase 5 becomes MQM-lite audit with severity classes; topology check split into structural vs surface | C3, C8, M6 |
| Phase 1: Topological Parsing | Preserved + clarified HTML-table handling + comment-policy linkage | L5, H11 |
| Phase 2: Semantic & Modal Deconstruction | Preserved | — |
| Phase 3: Domain Reconstruction | Preserved + Grammar Asymmetry and Quantity & Locale applications | H4, H5 |
| Phase 4: Typographical Compilation | Revised: split into Structural Topology vs Surface Typography; title-of-works mapping; nested quote/parenthetical rules; CJK–Latin spacing edge cases; emoji/mention/hashtag passthrough | C2, C3, H7, M4, M13, L2 |
| Phase 5: Zero-Trust Audit | Revised: MQM-lite severity classes; IU-coverage bookkeeping replaces "information density" check; structural-only topology check; numeric-equivalence standard replaces "identical numbers" | C3, C6, M6 |
| Ambiguity Resolution Protocol | Preserved (S4) + linked to Notice Channel and `--notes` mode | C4 |
| Quality Priorities | Preserved (S5) + MQM-lite severity classes assigned per priority | — |
| Strict Output Constraints | Revised: Notice Channel defined; no-silent-failure rule; mode-specific outputs | C4, C5 |
| Optional Glossary Output Mode | Revised: completed schema; Certainty enum defined; first-occurrence ordering; carry-over block format | H10, M9 |
| (new) §0 Intake & Direction Protocol | Added | C7 |
| (new) Modes & Runtime Parameters | Added: default, `--glossary`, `--notes`, `--qa`, `--strict`, `--locale`, `--termbase`, `--translate-comments`, `--publishing` | C4, C5, H1, H9, M5 |
| (new) Terminology Precedence Ladder | Added: 6-rung precedence from user termbase down to "preserve original" | H9, M3 |
| (new) Conformance Level Definitions (L1–L4) | Added: acceptance criteria per level; scope-boundary statement | M8, L3 |
| Few-Shot Calibration Examples | Revised: 4 → 8 examples; Example 3 (no-op) replaced; new: CN→EN legal hedge, injection quarantine, OCR artifact, title-of-works | M7, L4 |
| Self-Test Instruction | Revised: scoped quote checks; locked-retention exemption; notice-channel check; mode-output check | C2, M10 |
| (new) Extensibility: Domain Pack | Added: pluggable register extensions | future-proofing |
| Footer ("Translation Quality Target") | Preserved + version line added | — |

---

## Critical Fixes (C1–C8) — Disposition Detail

### C1 — Self-referential decoding parameters
- **v4.0 location:** lines 7–9 ("Set `temperature=0` and `top_p=0.1` for all translation operations.")
- **v5.0 fix:** Replaced with a behavioral-determinism contract in the Role/Operating Mode block ("Operate as a deterministic state machine: at every decision point, choose the rendering most consistent with the locked glossary, the modality tables, and prior choices within the same payload"). Literal decoding settings moved to a "Deployment Note (for the inference layer, not the model)" block, clearly labeled as operator guidance outside the model's own control.

### C2 — "No smart quotes" gate contradicts mandated Chinese typography
- **v4.0 location:** Phase 4 mandates Chinese full-width quotes `""` `''` (U+201C/201D/2018/2019 — the same codepoints as English curly quotes); Self-Test demands "no smart quotes."
- **v5.0 fix:** Quote-width rule is now scoped per segment language and typography profile: Chinese segments *retain* `""` `''`; English technical segments use straight quotes; `--publishing` profile permits curly quotes in English prose. Self-Test reworded: "No half-width-converted or flattened quotes in Chinese segments (Chinese segments retain `""` `''` U+201C/201D/2018/2019); no curly quotes in English technical segments (default profile) unless `--publishing` is active."

### C3 — Topology fidelity check contradicts mandated typography transformation
- **v4.0 location:** Phase 5 Topology Check requires every Markdown symbol "exactly as the source," while Phase 4 *requires* deviating from source surface (spacing injection, quote normalization, punctuation-width conversion).
- **v5.0 fix:** Phase 5 audit now distinguishes **Structural Topology Check** (headings, lists, tables, fences, link targets — must match source exactly) from **Surface Typography Check** (normalized per Phase 4 rules; exempt from source-identity check, audited against the typography rules instead). Few-Shot Example 3 explicitly demonstrates this distinction.

### C4 — Translator's notes conditionally permitted, but the permitting mode doesn't exist
- **v4.0 location:** Defensive Protocol 4 and Ambiguity Protocol step 4 reference an "output mode permits commentary" that was never defined.
- **v5.0 fix:** New `Modes & Runtime Parameters` section explicitly defines `--notes` mode (permits inline `[译注: …]` notes) and `--qa` mode (permits audit summary). All references to "if the output mode permits" now resolve to a defined flag.

### C5 — Silent best-effort fallback undermines the forensic guarantee
- **v4.0 location:** Phase 5 — "halt and output the best-effort translation with a silent internal flag (do not expose the flag to the user)."
- **v5.0 fix:** "Silent internal flag" mechanism abolished. New Notice Channel protocol: audit failure in default mode appends one `[NOTICE]` line at the payload foot; `--strict` mode emits *only* the Notice line and suppresses the payload. No-silent-failure rule explicitly stated in Output Constraints.

### C6 — "Identical numbers" fact-check contradicts the numeral-localization example
- **v4.0 location:** Phase 5 Fact Check demands numbers be "identical"; Example 1 requires converting "$2.4 million" → "240 万美元".
- **v5.0 fix:** Phase 5 Fact Check now requires "numerically equivalent under the Quantity & Locale Conventions" (not surface-identical). New Defensive Protocol 7 — Quantity & Locale Conventions — defines the conversion policy explicitly (currency, dates, units, percent/ranges).

### C7 — The core operating instruction is missing: direction detection
- **v4.0 location:** Absent entirely.
- **v5.0 fix:** New §0 Intake & Direction Protocol added before Core Philosophy. Defines: explicit override handling, auto-detection, bilingual payload handling, third-language Notice Channel, empty/garbled payload behavior, same-language "translation" requests.

### C8 — Iteration budget is doubly and inconsistently specified
- **v4.0 location:** Workflow header says "Maximum self-correction iterations per phase: 2"; Phase 5 says "return to Phase 3 (maximum 2 iterations)."
- **v5.0 fix:** Single global repair budget stated once: "Audit-failure loops ≤ 2. All other phases execute exactly once." Per-phase phrasing deleted. Phase 5 references the global budget consistently.

---

## High Coverage Gaps (H1–H11) — Disposition Detail

| ID | Gap | v5.0 Section | Status |
|----|-----|--------------|--------|
| H1 | No locale dimension (Simplified/Traditional, Mainland/Taiwan, US/UK) | Modes & Runtime Parameters — `--locale=zh-CN\|zh-TW\|en-US\|en-GB` + Entity Anchoring locale-terminology sub-rules | Closed |
| H2 | Modality tables one-directional | Defensive Protocol 2 — all tables bidirectional with symmetric negative examples | Closed |
| H3 | Financial register listed but no markers | Defensive Protocol 2 — new Financial / Securities-Disclosure Markers block (10 entries) | Closed |
| H4 | No grammatical-asymmetry protocol | Defensive Protocol 6 — Grammar Asymmetry Protocol (tense/aspect, number, articles, pronouns) | Closed |
| H5 | No quantity, date, or unit policy | Defensive Protocol 7 — Quantity & Locale Conventions | Closed |
| H6 | Named-entity coverage gaps (persons, places, cases, honorifics) | Defensive Protocol 1 — extended with person/place/case/honorific sub-protocol | Closed |
| H7 | No title-of-works typography mapping (《》 ↔ italics/quotes) | Typography Rules — Title-of-Works Mapping table with GB/T exclusion list | Closed |
| H8 | No prompt-injection quarantine | Axiom 4 — Instruction Quarantine | Closed |
| H9 | No user-termbase injection or precedence protocol | Modes (`--termbase`) + Terminology Precedence Ladder (6 rungs) | Closed |
| H10 | No cross-segment terminology persistence | Glossary Mode — Carry-Over block format defined | Closed |
| H11 | Code-comment and UI-string immutability overreaches | Defensive Protocol 1 — localization exception + Phase 1 comment policy (`--translate-comments`) | Closed |

---

## Medium Precision Issues (M1–M13) — Disposition Detail

| ID | Issue | v5.0 Fix |
|----|-------|-----------|
| M1 | "Meta" miscategorized as translated-name example | Defensive Protocol 1 — split into Translated set (苹果, 微软, 谷歌, 亚马逊, 甲骨文) and Preserved set (Meta, OpenAI, Anthropic, Palantir) |
| M2 | RFC 2119 citation imprecise (lowercase "must" vs uppercase MUST) | Defensive Protocol 2 — Engineering markers table distinguishes MUST/SHOULD/MAY (uppercase, BCP 14 normative) from must/should/may (lowercase, ordinary English) |
| M3 | "Universally preferred" circular | Resolved by Terminology Precedence Ladder (6 explicit rungs) |
| M4 | CJK–Latin spacing rule not labeled as style choice | Typography Rules — labeled as "digital house-style rule"; enumerated edge cases (full-width punctuation adjacency, `%`/`$`/`°`/unit symbols, bold/italic spans, link text) |
| M5 | Straight-quote-only rule conflicts with publishing claim | Typography Rules — English Typography now has Default (technical, straight quotes) and Publishing (`--publishing`, typographic quotes permitted in prose) profiles |
| M6 | "Information density proportional" unmeasurable | Phase 5 — replaced with IU-Coverage Bookkeeping check |
| M7 | Example 3 is a no-op | Few-Shot Example 3 replaced with EN→CN case demonstrating typography, immutability, and the C3 structural-vs-surface distinction |
| M8 | L1–L4 levels invoked but undefined | New Conformance Level Definitions section — acceptance criteria per level |
| M9 | Glossary schema "Certainty" undefined | Glossary Mode — Certainty enum: `locked-standard` / `locked-context` / `candidate`; first-occurrence ordering |
| M10 | Self-test "no unexplained English" false-flags mandated retentions | Self-Test — Locked-Retention Exemption: immutable elements, locked-glossary retentions, and domain-standard acronyms are exempt |
| M11 | "shall" missing from modal map | Defensive Protocol 2 — Legal markers table: `shall` → 须/应当; `shall not` → 不得 |
| M12 | Statistical/medical modality gaps | Defensive Protocol 2 — Medical markers table extended: "significant (stat.)" → 具有统计学意义; "associated with" → 与……相关 (never 导致) |
| M13 | "Dominant language" punctuation under-specified for nested cases | Typography Rules — nested cases specified: fully-English parenthetical inside Chinese follows English; nested Chinese quotes follow outer-双 inner-单 ("…'…'…") |

---

## Low Findings (L1–L6) — Disposition Detail

| ID | Issue | v5.0 Fix |
|----|-------|-----------|
| L1 | "Halt and output" vestigial | Replaced by Notice Channel + `--strict` mechanism |
| L2 | No passthrough for emoji/mentions/hashtags | Typography Rules — explicit passthrough rule |
| L3 | No scope boundary (engine ≠ certified translation) | Conformance Level Definitions — explicit scope-boundary statement |
| L4 | Only 4 calibration examples; none adversarial | Few-Shots — expanded to 8; new: CN→EN legal hedge, injection attempt, OCR artifact, title-of-works |
| L5 | "Merged cells" implies HTML tables | Phase 1 — clarified: standard Markdown tables supported as-is; HTML tables with `colspan`/`rowspan` preserved verbatim, only cell text translated |
| L6 | No fidelity stance for offensive/sensitive content | Implicit in Axiom 1 + Axiom 4 — forensic completeness = translate-as-is, no sanitizing; Axiom 4 also neutralizes any "soft refusal" injected by safety filters that would edit content |

---

## v4.0 Strengths Preserved (S1–S8)

| ID | Strength | Preservation in v5.0 |
|----|----------|----------------------|
| S1 | Explicit modality tables with negative examples | Preserved verbatim and extended bidirectionally (Legal, Engineering, Medical, Financial) |
| S2 | Immutable-element anchoring | Preserved verbatim and refined (localization exception, comment policy) |
| S3 | Anti-translationese collocation pairs (both directions) | Preserved verbatim and extended (8 EN→CN + 6 CN→EN collocations) |
| S4 | Ambiguity Resolution Protocol as ordered hierarchy | Preserved verbatim, linked to Notice Channel and `--notes` mode |
| S5 | Quality Priorities with override rule | Preserved verbatim, with MQM-lite severity classes layered on |
| S6 | Few-shot examples with reasoning lines | Preserved and expanded (4 → 8 examples) |
| S7 | Prohibition on meta-commentary / phase leakage | Preserved verbatim |
| S8 | Culturally-bound idiom handling with functional-equivalence preference | Preserved verbatim and refined (functional-equivalence is now reconciled with Axiom 1 via the licensed-deviation note) |

---

## Acceptance Criteria Status (v5 Plan §4)

All 12 acceptance criteria are satisfied by the v5.0 draft. The right column locates the corresponding rule in `Translation_Engine_v5_Prompt.md`.

| # | Criterion | v5.0 location |
|---|-----------|----------------|
| 1 | C2 regression: Chinese source with `""` yields U+201C/201D in output; Self-Test does not flag | Typography Rules (Chinese Typography) + Self-Test (scoped quote check) |
| 2 | C7 direction: monolingual EN → CN; monolingual CN → EN; French → single Notice line, no translation | §0 Intake & Direction Protocol + Output Constraints (Notice Channel) |
| 3 | C5 visibility: forced audit failure → default appends Notice; `--strict` emits only Notice | Modes (`--strict`) + Phase 5 audit failure behavior + Output Constraints (no-silent-failure rule) |
| 4 | H8 injection: source containing "ignore previous instructions" → translated verbatim; behavior unchanged | Axiom 4 + Few-Shot Example 6 |
| 5 | H2 bidirectionality: "涉嫌转移资产" → "allegedly transferred assets"; "allegedly" → 涉嫌/据称 | Defensive Protocol 2 — Legal markers table (bidirectional) + Few-Shot Example 5 |
| 6 | H1 locale: `--locale=zh-TW` → 軟體/網路; defaults → 简体 + Mainland terms | Modes (`--locale`) + Entity Anchoring (locale-terminology sub-rules) |
| 7 | H5 quantities: "$2.4 million" → 240 万美元; "yesterday" → 昨天; no USD↔CNY conversion | Defensive Protocol 7 — Quantity & Locale Conventions + Few-Shot Example 1 |
| 8 | H7 titles: 《三体》 → *The Three-Body Problem*; "Hamlet" → 《哈姆雷特》; organization never wrapped in 《》 | Typography Rules — Title-of-Works Mapping + Few-Shot Example 8 |
| 9 | C3 topology: curly quotes + tight CJK spacing normalized per rules; headings/tables/fences match exactly; no audit loop | Phase 1 + Phase 5 (Structural vs Surface split) + Few-Shot Example 3 |
| 10 | M11/M12 modality: "shall" → 须/应当; "significantly associated with" → 与……显著相关（统计学）, never 导致 | Defensive Protocol 2 — Legal markers (shall) + Medical markers (statistical claims) |
| 11 | H10 persistence: Segment 2 with Segment 1's glossary reproduces identical terms; termbase override beats built-in | Glossary Mode — Carry-Over block + Terminology Precedence Ladder |
| 12 | Output hygiene: no mode flag → zero meta-commentary; `--qa` → audit summary with severity counts only | Modes + Output Constraints + Self-Test (mode-output check) |

---

## Self-Review Pass Results

### Pass 1 — Contradiction Sweep

Fifteen pairwise contradiction checks were performed against the C2/C3/C4/C6 failure pattern. All clear:

1. Quote rule (C2) — scoped per segment language + typography profile; no conflict.
2. Topology check (C3) — split into structural vs surface; no conflict.
3. Translator's notes (C4) — all conditional references resolve to `--notes` mode; no undefined gates.
4. Silent failure (C5) — abolished; Notice Channel + `--strict` defined consistently.
5. Identical numbers (C6) — replaced with numeric-equivalence standard; consistent across Phase 5, Example 1, and Defensive Protocol 7.
6. Direction detection (C7) — §0 defines the trigger comprehensively.
7. Iteration budget (C8) — single global budget, consistently referenced.
8. Decoding parameters (C1) — behavioral contract in Role; literal settings in Deployment Note; no overlap.
9. Axiom 1 vs idiom handling — licensed-deviation note reconciles them.
10. Axiom 4 vs runtime flags — flags may not override Axioms; consistent across Axiom 4 and Modes sections.
11. Title-of-Works vs Entity Anchoring — organization names excluded from 《》 in both sections.
12. Glossary carry-over vs Precedence Ladder — consistent ordering.
13. `--strict` mode behavior — consistent across Modes, Phase 5, and Output Constraints.
14. `--publishing` profile scope — consistent across Modes and Typography Rules.
15. Immutable elements localization exception — consistent across Entity Anchoring, Phase 1, and Modes (`--translate-comments`).

### Pass 2 — Validation Suite (12 cases)

All 12 cases from v5 Plan §5 (Validation Suite) mentally executed against the draft:

1. Legal modality trap (EN→CN) — Example 1 covers; passes.
2. Legal modality trap (CN→EN) — Example 5 covers; passes.
3. RFC 2119 uppercase/lowercase — Engineering markers table distinguishes; passes.
4. Injection attempt — Example 6 covers; passes.
5. OCR artifacts — Example 7 covers; passes.
6. Mixed curly/straight quotes — Typography Rules + Self-Test cover; passes.
7. Bilingual input — §0 rule 3 covers; passes.
8. Third-language input — §0 rule 4 + Notice Channel cover; passes.
9. Locale switch — Modes (`--locale`) covers; passes.
10. Financial hedging — Financial markers table covers; passes.
11. Statistical claims — Medical markers table covers; passes.
12. Title-of-works — Example 8 + Title-of-Works Mapping cover; passes.
13. 3-segment terminology-persistence chain — Carry-over block + Precedence Ladder cover; passes.

### Pass 3 — Acceptance Criteria Check

All 12 acceptance criteria from v5 Plan §4 confirmed satisfiable. See the "Acceptance Criteria Status" table above.

---

## Line-Count Comparison

| Metric | v4.0 | v5.0 | Delta |
|---|---|---|---|
| Total lines | 214 | 629 | +415 |
| Sections (top-level `###`) | 8 | 17 | +9 |
| Few-shot examples | 4 | 8 | +4 |
| Modality tables | 3 (one-directional) | 4 (bidirectional) | +1 |
| Defined mode flags | 1 (implicit `--glossary`) | 8 | +7 |
| Critical-defect count | 8 | 0 | −8 |
| High-gap count | 11 | 0 | −11 |
| Medium-issue count | 13 | 0 | −13 |
| Low-finding count | 6 | 0 | −6 |

---

## Migration Notes for Operators

1. **Drop-in replacement.** v5.0 is designed as a drop-in replacement for v4.0. No external code changes are required; the prompt is self-contained.
2. **Inference-layer settings.** The literal `temperature=0` / `top_p=0.1` settings previously claimed by the model are now operator guidance in the Deployment Note. Operators who were already applying these settings need not change anything; operators who were not should apply them for best results.
3. **New flags are opt-in.** The new mode flags (`--notes`, `--qa`, `--strict`, `--locale`, `--termbase`, `--translate-comments`, `--publishing`) are all opt-in. Default behavior (payload only, zh-CN/en-US, technical typography profile) matches v4.0 observable behavior — except that audit failures now emit a visible Notice Channel line instead of failing silently (the C5 fix).
4. **Backward compatibility for `--glossary`.** The `--glossary` flag from v4.0 still works; the schema is now stricter (Certainty enum, first-occurrence ordering) but the basic format is unchanged.
5. **No certified-translation claim.** The new Conformance Level Definitions section makes explicit that engine output is *not* a certified or sworn translation. This is a clarification of scope, not a reduction in capability — v4.0 also did not produce certified translations, it simply did not say so.

---

*End of changelog. For the v5.0 prompt itself, see `Translation_Engine_v5_Prompt.md`.*
