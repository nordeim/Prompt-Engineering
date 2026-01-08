# Executive Summary
You want a **skills handbook** that prevents and systematically diagnoses the “mobile navigation disappeared” failure mode in HTML mockups—both to **teach your coding agent how to avoid creating the bug** and to **troubleshoot/fix it quickly** when it appears. I’ll propose a guide that is:

- **Diagnostic-first:** a decision tree that pinpoints root cause in minutes.
- **Pattern-first:** a small set of “approved” responsive-nav implementations (with a11y requirements).
- **Anti-pattern-first:** explicit “do not do this unless…” rules (the exact failure your agent keeps producing).
- **Verification-first:** a repeatable QA protocol + promptable checklist your agent must run before it declares done.

# Deep Root-Cause Taxonomy (Why nav “disappears” on mobile)
In practice, “nav missing” collapses into a handful of classes. Your handbook should treat these as **first-class categories**, each with signatures + fixes:

## 1) “Destructive hiding” without substitution (most common)
- **Symptom:** `@media` sets `.nav-links { display: none; }` and there is **no mobile trigger/menu**.
- **Fix:** either **don’t hide**; or hide the desktop layout but **introduce** a mobile disclosure pattern (button + overlay/drawer).

## 2) Hidden by visibility/opacity but still intercepting or clipped
- **Causes:** `visibility:hidden`, `opacity:0`, transforms; but **parent has `overflow:hidden`** or menu is positioned off-screen.
- **Fix:** ensure open state toggles `visibility/opacity/transform` *and* overlay has `overflow-y:auto` and isn’t clipped by ancestors.

## 3) Stacking / layering (z-index wars)
- **Causes:** menu exists but is behind header/hero/backdrop due to `position` + `z-index` + new stacking contexts (`transform`, `filter`, `opacity`).
- **Fix:** define a z-index scale, avoid accidental stacking contexts, verify with DevTools “Layers”.

## 4) Layout collapse (flex/grid + wrap + min-width)
- **Causes:** `flex-wrap`, `white-space`, long labels, `min-width`, or container constraints push items out.
- **Fix:** adjust container behavior; ensure mobile layout is a column list with controlled spacing.

## 5) Viewport / breakpoint mismatch
- **Causes:** missing `<meta name="viewport">`, incorrect breakpoints, device width ≠ CSS width.
- **Fix:** enforce viewport meta; use sane breakpoints; test with real device emulation.

## 6) JS state bugs / event timing
- **Causes:** toggle code not running, DOM selectors wrong, listeners attached before DOM ready, resize not handled.
- **Fix:** resilient state machine; guard selectors; close on resize; maintain `aria-expanded`.

## 7) Accessibility-driven “invisible”
- **Causes:** focus styles off; trigger not keyboard-focusable; “works” with mouse only.
- **Fix:** semantic `<button>`, visible focus, Escape-to-close, focus return, scroll lock.

# Handbook Design: What it must contain (to train an agent)
## Approved Patterns (prescriptive)
- **Pattern A:** “Button + overlay” (no framework) with:
  - `button[aria-controls][aria-expanded]`
  - `nav#id`
  - body/class-based open state
  - Escape close, outside click close, close on link click, resize reset
- **Pattern B:** “Button + drawer” (same mechanics, different motion)
- **Pattern C:** “Framework/library-specific” (only if project has it)

## Forbidden / high-risk anti-patterns
- **Anti-pattern 1:** “Hide nav on mobile” without adding a trigger.
- **Anti-pattern 2:** Using `<label>`/checkbox hack when a11y is required.
- **Anti-pattern 3:** Random `z-index` values without a scale.
- **Anti-pattern 4:** `overflow:hidden` on ancestors of dropdown overlays.

## Diagnostics Decision Tree (the “5-minute fix” flow)
A page-1 flow like:
1) Is nav element present in DOM on mobile?
2) If present, is it being hidden (computed styles)?
3) If visible, is it off-screen/clipped (layout box)?
4) If visible but not clickable, is it behind something (stacking)?
5) If toggle exists, does it update state + `aria-expanded`?

Include the exact DevTools actions:
- **Elements panel:** search `<nav`, check computed `display/visibility/opacity`.
- **Layout box model:** confirm its size/position.
- **Toggle `:hov` / force state:** open menus.
- **Disable CSS rules live:** isolate offending rule.
- **Z-index/layers inspection:** stacking contexts.

# Implementation Plan (with validation checkpoint)
## Phase 1 — Scope & Standards (Decision Gate)
- **Checklist**
  - Define target: plain HTML/CSS/JS only, or include frameworks?
  - Choose accessibility bar: WCAG AA vs AAA.
  - Decide deliverable: `NAV_HANDOOK.md` in repo vs external doc.
- **Success criteria**
  - Agent can follow the doc to prevent the bug in new mockups.

## Phase 2 — Root-Cause Taxonomy + Decision Tree
- **Checklist**
  - Write taxonomy (7 classes above) with “symptoms → confirm steps → fix”.
  - Produce a single-page decision tree.
- **Success criteria**
  - Any “nav missing” report maps to a class within 3 checks.

## Phase 3 — Reference Implementations + Anti-patterns
- **Checklist**
  - Provide 1–2 canonical nav templates (overlay + drawer).
  - Include minimal JS state machine + a11y notes.
  - Add anti-pattern examples + why they fail.
- **Success criteria**
  - Agent can paste template and adapt safely.

## Phase 4 — Verification Protocol + Agent Prompts
- **Checklist**
  - Responsive test matrix (width/height, reduced motion).
  - Keyboard-only checklist.
  - “Agent self-check prompt” the agent must run before final output.
- **Success criteria**
  - Agent output includes a “Verified” section with checks passed.

## Phase 5 — Deliver Markdown Handbook
- **Checklist**
  - Make it skimmable: Quick Fix page, then deep sections.
  - Add “Troubleshooting worksheets” (copy/paste).
- **Success criteria**
  - A new developer can fix the bug without asking you.

# Validation Checkpoint (before I write the handbook)
Answer these so the guide is calibrated:

1) **Target stack(s):** plain HTML/CSS/JS only, or also Tailwind/React/etc.?  
2) **Accessibility target:** AA or AAA? (AAA implies stronger focus management, semantics, and documentation.)  
3) **Output format/location:** a `docs/` Markdown file in the repo, or a standalone `NAVIGATION_TROUBLESHOOTING.md` at root?  
4) **Your agent:** is it primarily failing by generating `display:none` on mobile, or other patterns too?

## Status
- **Planning complete and ready for your confirmation** on the 4 decisions above. Once you confirm, I’ll proceed to execute Phase 2–5 and produce the handbook content.
