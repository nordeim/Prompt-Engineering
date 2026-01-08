# Mobile Navigation “Disappears” — Skills Handbook

## 0) Purpose
This handbook captures a repeatable, production-grade approach to **preventing**, **diagnosing**, and **fixing** the common failure mode:

- Mobile viewport is active
- The navigation exists in the design intent
- But the nav is **not visible / not reachable / not usable**

It is designed for:
- **Human developers** building HTML mockups
- **Coding agents** generating HTML/CSS/JS that must not ship a dead-end nav

## 1) Definition of “Nav Disappears”
A mobile navigation is considered “disappeared” when **any** of these are true:
- The user has **no visible navigation affordance** (no links, no menu button, no drawer)
- The nav exists but is **not visible** (hidden by CSS)
- The nav is visible but **not interactive** (covered by another layer)
- The nav is interactive but **not reachable by keyboard**

### Success criteria
A correct mobile nav implementation must satisfy:
- **Discoverability:** there is a clear affordance (links or a menu button)
- **Reachability:** the nav can be opened and navigated with touch and keyboard
- **Resilience:** resize/orientation changes do not strand the nav in a broken state
- **No clipping:** all items remain reachable even on small-height screens

---

## 2) Non‑Negotiable Guardrails (Prevention Rules)
These rules prevent >80% of “nav disappeared” bugs.

### 2.1 Viewport meta is mandatory
Include exactly one:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Without it, breakpoints may not behave as expected on real devices.

### 2.2 Never “destroy” navigation without “substitution”
**Forbidden pattern:**

- A mobile media query sets `.nav` / `.nav-links` to `display: none`
- There is **no mobile replacement** (menu button + overlay/drawer)

If you hide desktop nav on mobile, you must introduce a mobile pattern:
- **Menu button** + overlay/drawer
- Or keep inline nav visible (small, stacked)

### 2.3 Use semantic controls for interactive toggles
- Use a real `<button type="button">` for opening/closing the menu.
- Avoid checkbox/label hacks when accessibility matters.

### 2.4 Mobile overlays must not be clipped
If an overlay menu is used:
- It must be `position: fixed` (or otherwise outside clipping ancestors)
- It must not be inside a container with `overflow: hidden` unless intentional
- It should support `overflow-y: auto` for small-height devices

### 2.5 Establish a z-index scale
Random `z-index` values cause “exists but behind something” failures.

Define a scale (example):
- `--z-base: 0`
- `--z-sticky: 200` (header)
- `--z-modal: 300` (overlay nav)

Then **use the scale consistently**.

---

## 3) Root-Cause Taxonomy (What Actually Causes the Bug)
Use this taxonomy to classify the failure quickly.

### Class A — Destructive hiding without substitution
**Signature:**
- `@media (...) { .nav-links { display: none } }`
- No menu trigger exists in DOM

**Fix:**
- Add a mobile trigger + mobile nav presentation (overlay/drawer)

### Class B — Hidden by visibility/opacity/transform state
**Signature:**
- `opacity: 0`, `visibility: hidden`, or transform moves it off-screen
- Open state never activates (CSS state missing or JS not toggling)

**Fix:**
- Verify state toggling logic and selectors
- Ensure open state actually changes computed styles

### Class C — Clipped by overflow or layout constraints
**Signature:**
- Nav exists and is “open” but top items are missing
- Parent has `overflow: hidden`, or overlay is centered and items clip off-screen

**Fix:**
- Use `position: fixed` overlay
- Use `justify-content: flex-start` + `overflow-y: auto`

### Class D — Behind another layer (z-index/stacking context)
**Signature:**
- Nav is present and visible in DOM, but cannot be clicked
- Another element overlays it

**Fix:**
- Raise nav layer using the z-index scale
- Remove accidental stacking contexts (e.g. `transform` on parents)

### Class E — Breakpoint/viewport mismatch
**Signature:**
- Works in desktop devtools but fails on real device
- Breakpoints not triggering

**Fix:**
- Ensure viewport meta
- Verify media query units and breakpoint values

### Class F — JavaScript state bug
**Signature:**
- Menu button exists but does nothing
- Console errors, selector mismatches, timing issues

**Fix:**
- Guard selectors, attach listeners after DOM ready
- Implement a single `setMenuState(isOpen)` function

### Class G — Keyboard-only failure (appears “gone” for keyboard users)
**Signature:**
- Mouse/touch can open
- Keyboard can’t reach the trigger or links

**Fix:**
- Ensure trigger is a `<button>`
- Provide visible focus states
- Support Escape-to-close and focus return

---

## 4) 5‑Minute Diagnostic Decision Tree (DevTools‑First)
Use this flow before editing code.

### Step 1 — Is the nav present in the DOM?
- Inspect Elements
- Search for `<nav` or `.nav-links`

If **not present**:
- You have Class A (missing mobile substitution) or template omission.

If **present**:
- Continue.

### Step 2 — Is it hidden by computed CSS?
In Computed styles, check:
- `display`
- `visibility`
- `opacity`

If `display: none`:
- Find the rule (likely a mobile media query)
- This is Class A (if no replacement) or Class B (if replacement exists but is hidden)

### Step 3 — Is it off-screen or clipped?
Check layout box:
- `position`
- `top/left/right/bottom`
- `transform`
- any ancestor `overflow: hidden`

If clipped:
- This is Class C.

### Step 4 — Is it behind another layer?
If it looks “open” but clicks fail:
- Temporarily toggle `pointer-events: none` on suspected overlays
- Inspect stacking contexts:
  - Any parent with `transform`, `filter`, `opacity < 1`, `position` + `z-index`

This is Class D.

### Step 5 — Is JS failing to toggle state?
- Check Console for errors
- Verify click handler is attached
- Verify state change occurs (body class or attribute)

This is Class F.

### Step 6 — Keyboard verification
- Tab to menu button
- Open with Enter/Space
- Escape closes
- Focus returns to trigger

Failures here are Class G.

---

## 5) Canonical Reference Implementation (Recommended Pattern)
This is the “safe default” pattern agents should use unless the project already mandates a component library.

### 5.1 HTML (semantic toggle)
```html
<header class="header">
  <a class="logo" href="#">Brand</a>

  <button
    type="button"
    class="menu-trigger"
    aria-controls="main-navigation"
    aria-expanded="false"
    aria-label="Open navigation"
  >
    <span class="sr-only">Menu</span>
    <span class="line line-1"></span>
    <span class="line line-2"></span>
  </button>

  <nav id="main-navigation" class="nav-links" aria-label="Main navigation">
    <a href="#section-1">Section 1</a>
    <a href="#section-2">Section 2</a>
    <a href="#section-3">Section 3</a>
  </nav>
</header>
```

### 5.2 CSS (mobile overlay that can’t clip items)
Key properties that prevent “disappears”:
- Do not use `display: none` for the nav
- Use fixed positioning
- Allow scrolling
- Avoid vertical centering that can hide top items

```css
.menu-trigger { display: none; }

@media (max-width: 768px) {
  .menu-trigger { display: inline-flex; }

  body.menu-open { overflow: hidden; }

  .nav-links {
    position: fixed;
    inset: 0;
    top: var(--nav-height, 64px);

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;

    padding: 64px 24px;
    gap: 16px;

    overflow-y: auto;

    opacity: 0;
    visibility: hidden;
    transform: translateY(10px);
    transition: opacity 200ms ease, transform 200ms ease, visibility 200ms ease;

    z-index: var(--z-modal, 300);
    background: #fff;
  }

  body.menu-open .nav-links {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
}
```

### 5.3 JS (minimal state machine)
Requirements:
- Toggle `aria-expanded`
- Escape-to-close
- Close on link click
- Close on resize back to desktop
- Restore focus

```js
(() => {
  const body = document.body;
  const button = document.querySelector('.menu-trigger');
  const nav = document.getElementById('main-navigation');

  if (!button || !nav) return;

  const setMenuState = (open, { focus = true } = {}) => {
    if (open) {
      body.classList.add('menu-open');
      button.setAttribute('aria-expanded', 'true');
      button.setAttribute('aria-label', 'Close navigation');
      if (focus) {
        const first = nav.querySelector('a');
        if (first) first.focus();
      }
      return;
    }

    body.classList.remove('menu-open');
    button.setAttribute('aria-expanded', 'false');
    button.setAttribute('aria-label', 'Open navigation');
    if (focus) button.focus();
  };

  button.addEventListener('click', () => {
    setMenuState(!body.classList.contains('menu-open'));
  });

  nav.querySelectorAll('a').forEach((a) => {
    a.addEventListener('click', () => setMenuState(false, { focus: false }));
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && body.classList.contains('menu-open')) {
      setMenuState(false);
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 768 && body.classList.contains('menu-open')) {
      setMenuState(false, { focus: false });
    }
  });
})();
```

---

## 6) Anti‑Patterns (What Agents Must Not Produce)
### Anti‑Pattern 1 — “Hide nav on mobile” without a menu trigger
```css
@media (max-width: 768px) {
  .nav-links { display: none; }
}
```
This creates a navigation dead-end.

### Anti‑Pattern 2 — Random z-index escalation
```css
.nav { z-index: 999999; }
```
This hides architectural problems and creates new ones.

### Anti‑Pattern 3 — Overlay inside `overflow: hidden` container
Overlays should be `position: fixed` or otherwise guaranteed not to be clipped.

### Anti‑Pattern 4 — Non-semantic clickable divs
`<div onClick>` without keyboard support creates an “invisible” nav for keyboard users.

---

## 7) Verification Protocol (What Must Be Checked Before “Done”)
### 7.1 Responsive test matrix
Minimum widths:
- 360
- 390
- 430
- 768
- 1024+

Also test:
- small height scenarios (e.g. 360×640)
- orientation change (portrait/landscape)

### 7.2 Keyboard-only checklist
- Tab reaches the menu button
- Enter/Space opens
- Focus moves into menu
- Escape closes
- Focus returns to button

### 7.3 Behavior checklist
- Menu opens and closes reliably
- Clicking a link closes the menu
- Resizing to desktop closes the menu
- No background scroll bleed when open (scroll lock)

### 7.4 Visual checklist
- Menu isn’t clipped: top items visible
- Menu isn’t behind header/hero layers
- Focus ring visible on links and trigger

---

## 8) Troubleshooting Worksheet (Copy/Paste)
Use this when a nav disappears.

**Page/Route:**

**Viewport (w×h):**

**Observed behavior:**

**Step 1: DOM present?** (Yes/No)
- Selector(s):

**Step 2: Computed styles**
- display:
- visibility:
- opacity:

**Step 3: Layout box**
- position:
- top/transform:
- overflow clipping ancestor:

**Step 4: Stacking context**
- overlay element suspected:
- z-index values:

**Step 5: JS state**
- button exists:
- click handler works:
- state changes (class/aria):

**Classification (A–G):**

**Fix applied:**

**Verification completed:**
- responsive matrix:
- keyboard checklist:

---

## 9) Agent Instruction Block (Use This As a Prompt)
Paste this into your coding agent instructions for any HTML mockup task:

- You must not hide navigation on mobile without a substitute pattern.
- If you introduce `@media (max-width: ...) { .nav-links { display:none } }`, you must also add a mobile menu button and an accessible overlay/drawer.
- Always add viewport meta.
- Implement a semantic `<button>` trigger with `aria-controls` and `aria-expanded`.
- Implement: Escape-to-close, close-on-link-click, resize reset.
- Mobile overlay must use `position: fixed`, `overflow-y: auto`, and `justify-content: flex-start`.
- Before final output, you must complete the verification protocol (responsive + keyboard) and report it.
