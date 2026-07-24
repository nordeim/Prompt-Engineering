## v10.1 Changes (vs v10.0)

### F-1: Successive Draft Protocol (replaces "in-place modification")
- **What:** §4.6 rewritten. DRAFT PAYLOAD is now versioned (v1 → v2 → v3). Final output is character-identical to the LATEST version. "In-place modification" language removed entirely.
- **Why:** v10.0's "in-place modification" was physically impossible for auto-regressive models. If repairs modified the draft, the "character-identical" rule created a logical contradiction.
- **Impact:** Repair blocks now produce a new DRAFT PAYLOAD version (complete text, not a diff). Token cost when repairs needed: ~3× payload (v1 + v2 in scratchpad + v2 in output). When no repairs: ~2× payload (unchanged from v10.0).
- **Migration:** Scratchpad format changes: DRAFT PAYLOAD sections are now versioned. Wrapper parsers should handle `### DRAFT PAYLOAD v[N]` headers.

### F-2: Size-Aware Draft-Lock Tiers
- **What:** New §4.7. Full Draft-Lock for <800 words; Segmented for 800–3,000; Mandatory Segmentation for >3,000; Anchored Regeneration for `--scratchpad=light`.
- **Why:** v10.0's Full Draft-Lock doubled output tokens unconditionally, risking truncation on older models and excessive cost on all models.
- **Impact:** Token cost is now proportional to payload size. Large documents are segmented before Draft-Lock is applied.
- **Migration:** Wrapper should implement size-based segmentation trigger. Phase 1 now emits token budget estimation.

### F-3: Source Preservation Clause (Anti-Enhancement refinement)
- **What:** §9.1.1 modified. Anti-Enhancement prohibits ADDING, not PRESERVING. Phase 1 inventories source HTML/structural elements. Phase 6 verifies both "no additions" and "no omissions."
- **Why:** v10.0's zero-tolerance phrasing could cause the model to strip legitimate source HTML elements.
- **Impact:** Source-present `<br>`, `<hr>`, `<div>`, badges are now explicitly protected. Phase 1 scratchpad adds "Source HTML/structural element inventory" field.
- **Migration:** No wrapper changes needed.

### F-4: Primary/Secondary Domain Classification
- **What:** §14.4 modified. Domain mismatch flagged only when >20% of IUs are out-of-domain. Single out-of-domain terms handled by universal rules.
- **Why:** v10.0's Phase 2 could over-react to a single out-of-domain term.
- **Impact:** Phase 2 scratchpad adds "Primary domain" and "Secondary domain terms" fields. Mismatch flag is less trigger-happy.
- **Migration:** No wrapper changes needed. Wrapper keyword heuristic unchanged.
