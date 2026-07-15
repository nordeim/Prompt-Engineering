# v4.0 Change Log: Improvements Over v1.0 → v2.0 → v3.0

## Document Statistics

| Metric | v1.0 | v2.0 | v3.0 | v4.0 (New) |
|--------|------|------|------|------------|
| Words | ~368 | ~660 | ~758 | ~2,050 |
| Characters | ~2,645 | ~5,035 | ~5,637 | ~14,260 |
| Lines | 134 | 86 | 78 | 214 |
| Sections | 5 | 4 | 6 | 9 |

---

## Section-by-Section Improvements

### 1. Role & Operating Mode

**v3.0 had:** "Deterministic Neural Translation State Machine"
**v4.0 changes to:** "Deterministic Translation State Machine"
**Why:** "Neural" and "Deterministic" are contradictory concepts. Neural networks are inherently probabilistic. Removing "Neural" eliminates cognitive dissonance.

**NEW in v4.0:**
- `temperature=0` and `top_p=0.1` explicitly specified as non-negotiable system parameters
- Explicit prohibition against deviating from locked glossary, modality tags, or Markdown topology

---

### 2. Core Philosophy

**v3.0 had:** "Information Entropy Conservation"
**v4.0 changes to:** "Information Fidelity Conservation"
**Why:** In information theory, "entropy" measures uncertainty, not information quantity. The intended meaning was conservation of factual content, which is fidelity, not entropy.

**Retained from v3.0:**
- Epistemic Isomorphism (unchanged)
- Domain-Native Reconstruction (unchanged)

---

### 3. Defensive Protocols (Major Expansion)

**v3.0 had 3 defensive protocols:**
1. Entity and Proper Noun Anchoring
2. Strict Modal and Epistemic Mapping
3. Anti-Translationese and Collocation Enforcement

**v4.0 expands to 5 defensive protocols:**

| Protocol | v3.0 | v4.0 | Notes |
|----------|------|------|-------|
| Entity Anchoring | ✅ Basic | ✅ Enhanced | Added Product Names & Trademarks, expanded Immutable Elements list |
| Modal Mapping | ✅ Legal + Engineering | ✅ + Medical | Added clinical markers (suggests, indicates, contraindicated) |
| Anti-Translationese | ✅ EN→CN + CN→EN | ✅ + Gerund rule | Added "……性" suffix prohibition |
| Culturally-Bound Expressions | ❌ ABSENT | ✅ NEW | Added idiom/metaphor handling with examples |
| Source Error / OCR Handling | ❌ ABSENT | ✅ NEW | Added artifact preservation and ambiguity protocol trigger |

**NEW Medical/Clinical markers:**
- "suggests" = 提示 (not 证明)
- "indicates" = 表明 / 提示
- "contraindicated" = 禁忌

**NEW Culturally-bound examples:**
- "low-hanging fruit" → 容易实现的目标
- "boil the ocean" → 试图同时处理过多问题
- 杀鸡取卵 → "sacrifice long-term gains for short-term profit"

---

### 4. Workflow (Structural Improvements)

**v3.0 had:** 5 Phases without iteration limits
**v4.0 changes to:** 5 Phases with **maximum 2 self-correction iterations per phase**
**Why:** Prevents infinite loops and runaway token consumption.

**NEW in Phase 1:**
- Complex table handling: "merged cells or nested structures, preserve exact cell alignment and spanning"

**NEW in Phase 2:**
- Domain register tagging (legal, medical, engineering, financial, general)
- Ambiguity trigger: links to new Ambiguity Resolution Protocol

**NEW in Phase 4 (Typography):**
- **Mixed-Language Sentences** subsection (was missing in all previous versions)
  - Dominant-language punctuation rule
  - Terminal punctuation for code-ending Chinese sentences (e.g., 请运行 `npm install`。)

**ENHANCED in Phase 5 (Audit):**
- v3.0 had 3 checks (Fact, Modality, Topology)
- v4.0 has **6 checks** (+ Collocation, + Typography, + Omission/Addition)
- Added explicit failure handling: "If audit fails after 2 repair iterations, halt and output best-effort"

---

### 5. Ambiguity Resolution Protocol (COMPLETELY NEW)

**Not present in v1, v2, or v3.**

Hierarchy:
1. Prefer Context
2. Prefer Domain Convention
3. Prefer Literal with Least Risk
4. Flag if Permitted

**Why this matters:** All previous versions assumed the source text was always clear. In practice, ambiguous source (polysemous terms, unclear pronouns, missing subjects) is common. Without guidance, the model guesses — which violates Information Fidelity Conservation.

---

### 6. Quality Priorities (Unchanged Structure, Enhanced Descriptions)

**v3.0 had:** 5 priorities with parenthetical labels
**v4.0 retains:** Same 5 priorities but adds domain coverage to #2:
- "Legal / Technical / Medical safety" (was just "Legal/Technical" in v3)

---

### 7. Output Constraints (Softened Language)

**v3.0 used:** "Zero" prefix branding (Zero Metatext, Zero Commentary, etc.)
**v4.0 uses:** Direct imperative statements without "Zero" prefix
**Why:** Research shows aggressive "Never"/"Zero" language can trigger aversion responses in some models (particularly Claude). Direct imperatives are equally enforceable but less adversarial.

**NEW in v4.0:**
- Glossary mode trigger instruction: "If the user has requested glossary mode..."
- Explicit prohibition against exposing phase numbers in output

---

### 8. Optional Glossary Output Mode (COMPLETELY NEW)

**Not present in v1, v2, or v3.**

Format: Term | Source Language | Target Language | Domain | Certainty

**Why this matters:** Users need to verify what terms were locked. A glossary output mode enables human-in-the-loop verification without requiring the model to explain its choices inline.

---

### 9. Few-Shot Calibration Examples (COMPLETELY NEW)

**Not present in v1, v2, or v3.** This is the single most impactful addition.

**4 examples covering:**
1. Legal Modal Precision (EN → CN) — "allegedly" handling with wrong answer shown
2. Engineering Collocation (CN → EN) — multi-error wrong answer shown
3. Chinese Typography & Immutable Code (Mixed) — spacing rules in practice
4. Epistemic Downgrade Protection (EN → CN) — "may" vs "will"

Each example includes:
- Source sentence
- Correct translation
- Wrong translation (with error annotation)
- Reasoning breakdown

**Why this matters:** Research consistently shows that 2-5 high-quality examples outperform pages of abstract instructions for format-sensitive tasks. The examples serve as "calibration anchors" that constrain the model's output distribution.

---

### 10. Self-Test Instruction / Pre-Output Gate (COMPLETELY NEW)

**Not present in v1, v2, or v3.**

Checks before emission:
- No smart quotes
- No unexplained foreign words outside immutable elements
- No internal reasoning markers ("Step 1:", "I think", etc.)
- Exact heading hierarchy preserved

**Why this matters:** Acts as a final circuit breaker before output. Catches the most common leakage patterns (meta-commentary, reasoning exposure, formatting drift).

---

## Critical Gap Resolution Summary

| Gap | v1 | v2 | v3 | v4.0 Status |
|-----|----|----|----|-------------|
| Few-shot examples | ❌ | ❌ | ❌ | ✅ 4 examples |
| Temperature=0 instruction | ❌ | ❌ | ⚠️ Mentioned | ✅ Explicit |
| "Ask for clarification" protocol | ❌ | ❌ | ❌ | ✅ Ambiguity Resolution Protocol |
| Culturally-bound idioms | ❌ | ❌ | ❌ | ✅ Dedicated section |
| OCR/error handling | ❌ | ❌ | ❌ | ✅ Source Error protocol |
| Glossary output mechanism | ❌ | ❌ | ❌ | ✅ Optional mode |
| Mixed-language punctuation | ❌ | ❌ | ❌ | ✅ Mixed-Language subsection |
| Iteration limits | ❌ | ❌ | ❌ | ✅ Max 2 per phase |
| Self-test pre-output gate | ❌ | ❌ | ❌ | ✅ Pre-Output Gate |
| Medical modality markers | ❌ | ❌ | ❌ | ✅ Added to Modal Mapping |
| Product/trademark rules | ❌ | ❌ | ❌ | ✅ Added to Entity Anchoring |
| Aggressive language softened | N/A | ⚠️ | ⚠️ | ✅ "Do not" instead of "Never" |

---

## Known Limitations of v4.0 (Honest Assessment)

Despite the improvements, v4.0 still has areas for future refinement:

1. **No automatic domain detection**: The model still relies on user-provided context or self-inference for domain register. A future version could include a pre-flight domain classifier.

2. **No multi-document consistency**: The glossary is locked per-document. Cross-document terminology consistency would require an external knowledge base.

3. **No handling of right-to-left (RTL) languages**: The prompt assumes LTR (Chinese/English) only. Arabic/Hebrew mixed with CJK would require additional rules.

4. **No explicit bias mitigation for gendered language**: Chinese and English handle gender differently. A future version should include guidance for gender-neutral translation where appropriate.

5. **Token cost**: At ~2,050 words, v4.0 is ~2.7x longer than v3.0. For API-cost-sensitive deployments, a "v4.0-lite" compressed version may be warranted.

6. **No empirical validation**: The prompt has not been A/B tested against a held-out test set of difficult translations. Effectiveness claims are theoretical, based on prompt engineering best practices.

---

## Recommended Deployment Configuration

```
Model: Claude 4 Sonnet / GPT-5 / Gemini 2.5 Pro
Temperature: 0
Top-p: 0.1
Max tokens: 4096 (adjust for document length)
System prompt: [v4.0 full text]
User prompt: [source text to translate]
Optional: Append "--glossary" to user prompt for glossary output
```

---

*Change Log compiled: 2026-07-15*
*Analyst: Deterministic Forensic Translation Engine v4.0*
