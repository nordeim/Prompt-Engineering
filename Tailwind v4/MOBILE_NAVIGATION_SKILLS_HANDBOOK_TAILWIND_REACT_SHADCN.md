# Mobile Navigation “Disappears” — Skills Handbook (Tailwind + React + shadcn/ui)

## 0) Purpose
This handbook is a stack-specific guide for **Tailwind CSS + React + shadcn/ui (Radix primitives)** to prevent, diagnose, and fix the failure mode:

- Mobile viewport is active
- Navigation is intended to exist
- But navigation is **not visible / not reachable / not usable**

It is written for:
- **React developers** building responsive navs with Tailwind utilities
- **Coding agents** generating React + Tailwind + shadcn markup

This document keeps the same structure as the plain-HTML handbook, but replaces implementation details with **shadcn-first** patterns and Tailwind/React-specific troubleshooting.

---

## 1) Definition of “Nav Disappears”
A mobile navigation is considered “disappeared” when **any** of these are true:
- The user has **no visible navigation affordance** (no links, no trigger)
- The nav exists but is **not visible** (Tailwind utilities hide it at the current breakpoint)
- The nav is visible but **not interactive** (covered by overlay, wrong z-index)
- The nav is interactive but **not reachable by keyboard**

### Success criteria
A correct mobile nav must satisfy:
- **Discoverability:** a clear menu affordance at mobile breakpoints
- **Reachability:** touch + keyboard can open and navigate
- **Resilience:** route changes, resize/orientation, hydration do not break state
- **No clipping:** all items are reachable on small-height devices

---

## 2) Non‑Negotiable Guardrails (Prevention Rules)
These rules prevent the majority of mobile nav disappearance bugs in Tailwind/React/shadcn.

### 2.1 Never hide desktop nav without showing a mobile substitute
The most common Tailwind mistake is:

- Desktop nav: `hidden md:flex`
- Mobile trigger: missing, or also `hidden`

**Rule:**
- If you use `hidden md:flex` on the desktop nav, you must include a mobile trigger like `md:hidden`.

### 2.2 Use shadcn/ui primitives for stability and accessibility
If shadcn/ui is available, use:
- **`Sheet`** for mobile navigation (overlay/drawer)
- **`NavigationMenu`** for desktop navigation (optional)

Do not rebuild dialogs/drawers manually.

### 2.3 Avoid Tailwind class strings that get purged
Tailwind builds styles by scanning for class strings.

**Forbidden:** dynamic class concatenation that Tailwind cannot statically analyze:

- `className={"md:" + size}`
- `className={isOpen ? "translate-x-0" : `-translate-x-${n}`}`

**Rule:** always keep Tailwind class names as static strings or use a known-safe variant system.

### 2.4 Don’t rely on CSS-only “display:none” for stateful menus
For mobile menus, prefer state-driven components:
- shadcn `Sheet` open state
- route-change close behavior

### 2.5 Respect z-index layering and portals
shadcn (Radix) uses portals for overlays. Don’t break them by:
- disabling portals (when available)
- forcing parent stacking contexts that trap overlays

### 2.6 Ensure keyboard support is real
With shadcn `Sheet`, you get:
- focus management
- Escape-to-close

**Rule:** mobile menu triggers must be real buttons (`Button` / `SheetTrigger`) and must be reachable by Tab.

---

## 3) Root-Cause Taxonomy (Tailwind/React/shadcn)
Use this taxonomy to quickly classify the cause.

### Class A — Destructive hiding without substitution (Tailwind breakpoints)
**Signature:**
- Desktop nav has `hidden md:flex`
- Mobile trigger is missing or also hidden

**Fix:**
- Add `md:hidden` trigger (usually a `SheetTrigger`) and render nav items in the Sheet.

### Class B — Hidden by conditional rendering / state never true
**Signature:**
- React condition prevents rendering nav on mobile: `isMobile && <Nav />`
- `isMobile` relies on `window` and fails on SSR/hydration

**Fix:**
- Avoid `window`-based conditional rendering for core nav.
- Prefer CSS breakpoints + always-rendered components.
- If you must branch, do it in client-only components with stable fallbacks.

### Class C — Clipped by overflow / centered layout in Sheet content
**Signature:**
- Sheet opens but top items are missing on short viewports
- Menu appears “sparse” or clipped

**Fix:**
- In `SheetContent`, use a scroll container: `overflow-y-auto` and top padding.
- Avoid `justify-center` for nav lists; use `justify-start`.

### Class D — Behind another layer (z-index/stacking)
**Signature:**
- Sheet opens but clicks don’t work
- Overlay is behind sticky header or other layer

**Fix:**
- Ensure Sheet uses sufficient z-index (shadcn defaults are usually fine).
- If your header has extreme z-index (`z-[9999]`), reduce it or raise Sheet.
- Avoid accidental stacking contexts on the portal root (rare, but possible if you heavily customize).

### Class E — Tailwind build/purge missing styles
**Signature:**
- In dev it works, in prod menu disappears
- Computed styles show missing Tailwind classes

**Fix:**
- Ensure content globs include all relevant files (`./app/**/*.{ts,tsx}`, etc.)
- Avoid dynamic class strings; use static classes or safelist

### Class F — Route-change state bug
**Signature:**
- Menu opens but never closes, or closes instantly
- On navigation, Sheet stays open and overlays the new page

**Fix:**
- Close the Sheet on route change / link click.
- In Next.js, close on `onClick` of `Link` or use pathname effect.

### Class G — Keyboard-only failure (focus/trigger missing)
**Signature:**
- Trigger is an icon but not a button
- Focus ring missing due to aggressive Tailwind resets

**Fix:**
- Use `Button` / `SheetTrigger`.
- Ensure focus styles exist: `focus-visible:outline-none focus-visible:ring-2 ...`

### Class H — Click-outside handler race condition
**Signature:**
- Menu briefly opens then immediately closes (or never visibly opens)
- Click on trigger sets state true, but document listener sets it false
- `aria-expanded` may flicker or stay false
- Console logs show state toggling true→false in rapid succession

**Root Cause:**
Document-level click handlers fire after component handlers due to event bubbling. If the click-outside logic doesn't exclude the trigger element, it immediately undoes the toggle.

```tsx
// Problematic pattern
document.addEventListener('click', (e) => {
  if (!menuElement.contains(e.target)) {
    setIsOpen(false); // Fires when toggle button is clicked!
  }
});
```

**Fix:**
- Exclude trigger element from click-outside detection
- Use a ref or query selector to identify the trigger

```tsx
const handleClickOutside = (e: MouseEvent) => {
  const target = e.target as HTMLElement;
  const menu = document.getElementById('mobile-menu');
  const trigger = document.querySelector('.menu-toggle');
  
  // Check BOTH menu AND trigger
  if (menu && !menu.contains(target) && !trigger?.contains(target)) {
    setIsOpen(false);
  }
};
```

---

## 4) 5‑Minute Diagnostic Decision Tree (DevTools + React)
Use this flow before editing code.

### Step 1 — Is the nav trigger rendered on mobile?
- In Elements, search for your trigger (e.g. `SheetTrigger`, `button[aria-label="Open menu"]`)

If missing:
- Likely Class A (breakpoint utilities) or Class B (conditional rendering).

### Step 2 — Is it hidden by Tailwind utilities?
In computed styles, check:
- `display: none`

Then inspect classes:
- `hidden`, `md:hidden`, `sm:hidden`, `max-md:hidden`, etc.

If hidden due to breakpoint classes:
- Class A.

### Step 3 — Does the Sheet/Draft open state change?
- Click trigger
- Confirm `data-state="open"` appears on Radix elements

If state never changes:
- Class F (JS wiring), or trigger not connected.

### Step 3b — Does the menu open then immediately close?
- Add `console.log('open')` and `console.log('close')` to handlers
- Watch for rapid "open" → "close" sequence
- Check if document-level click listener is firing

If opens then closes:
- Class H (click-outside race condition)
- Verify trigger is excluded from click-outside detection

### Step 4 — Is the menu content present but clipped?
- Find `SheetContent`
- Confirm it has `overflow-y-auto` and adequate padding

If top items missing:
- Class C.

### Step 5 — Is the overlay behind something?
- Inspect `z-index` of header, overlay, content
- Look for extreme values like `z-[9999]`

If behind:
- Class D.

### Step 6 — Production-only disappearance?
- Suspect Tailwind purge: Class E.
- Check build config: `content` globs and class string patterns.

### Step 7 — Keyboard verification
- Tab to trigger
- Enter/Space opens
- Escape closes

If fails:
- Class G.

---

## 5) Canonical Reference Implementation (shadcn-first)
This is the recommended pattern agents should use.

### 5.1 Data model (single source of truth)
Keep nav items in one array so desktop and mobile share the same links.

```ts
export const NAV_ITEMS = [
  { href: "#collections", label: "Collections" },
  { href: "#showcase", label: "Artisanal Range" },
  { href: "#about", label: "Our Story" },
  { href: "/journal", label: "Journal" },
] as const;
```

### 5.2 Desktop + Mobile header skeleton (Tailwind breakpoints)
- Desktop links: `hidden md:flex`
- Mobile trigger: `md:hidden`

### 5.3 Mobile nav with `Sheet`
This provides accessible overlay behavior out of the box.

```tsx
"use client";

import * as React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

import { Button } from "@/components/ui/button";
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";

import { NAV_ITEMS } from "./nav-items";

export function MobileNavSheet() {
  const [open, setOpen] = React.useState(false);
  const pathname = usePathname();

  React.useEffect(() => {
    // Close on route change to prevent stranded overlays
    setOpen(false);
  }, [pathname]);

  return (
    <Sheet open={open} onOpenChange={setOpen}>
      <SheetTrigger asChild>
        <Button
          variant="outline"
          size="icon"
          className="md:hidden"
          aria-label={open ? "Close navigation" : "Open navigation"}
        >
          <span className="sr-only">Menu</span>
          {/* Replace with an icon component if desired */}
          <span className="h-5 w-5">≡</span>
        </Button>
      </SheetTrigger>

      <SheetContent side="right" className="p-0">
        <div className="flex h-full flex-col">
          <SheetHeader className="border-b px-6 py-4">
            <SheetTitle>Navigation</SheetTitle>
          </SheetHeader>

          <nav className="flex-1 overflow-y-auto px-6 py-6">
            <ul className="flex flex-col gap-3">
              {NAV_ITEMS.map((item) => (
                <li key={item.href}>
                  <SheetClose asChild>
                    <Link
                      href={item.href}
                      className="block rounded-md px-3 py-2 text-lg font-medium leading-tight hover:bg-muted focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
                    >
                      {item.label}
                    </Link>
                  </SheetClose>
                </li>
              ))}
            </ul>
          </nav>
        </div>
      </SheetContent>
    </Sheet>
  );
}
```

### 5.4 Desktop nav (simple)
```tsx
import Link from "next/link";
import { NAV_ITEMS } from "./nav-items";

export function DesktopNav() {
  return (
    <nav className="hidden md:flex items-center gap-8">
      {NAV_ITEMS.map((item) => (
        <Link
          key={item.href}
          href={item.href}
          className="text-sm font-medium hover:underline underline-offset-8"
        >
          {item.label}
        </Link>
      ))}
    </nav>
  );
}
```

### Notes
- `SheetClose` ensures the menu closes when a link is clicked.
- `overflow-y-auto` ensures no clipping on small height.
- Keep breakpoints symmetrical: `md:hidden` for trigger, `hidden md:flex` for desktop links.

---

## 6) Anti‑Patterns (Tailwind/React/shadcn)
### Anti‑Pattern 1 — Missing mobile trigger
```tsx
<nav className="hidden md:flex">...</nav>
// no md:hidden trigger
```
Result: mobile nav disappears.

### Anti‑Pattern 2 — Both trigger and desktop nav hidden at mobile
```tsx
<button className="hidden md:inline-flex">Menu</button>
<nav className="hidden md:flex">...</nav>
```
Result: nothing is visible on mobile.

### Anti‑Pattern 3 — SSR/hydration conditional nav
```tsx
const isMobile = window.innerWidth < 768; // breaks on SSR
return isMobile ? <MobileNav/> : <DesktopNav/>;
```
Result: flicker, mismatch, or missing nav.

### Anti‑Pattern 4 — Purge-prone dynamic classes
```tsx
<div className={"md:" + variant}>...</div>
```
Result: works in dev, disappears in prod.

### Anti‑Pattern 5 — Extreme z-index escalation
```tsx
<header className="sticky top-0 z-[999999]">...</header>
```
Result: overlays (Sheet) may appear behind or feel broken.

### Anti‑Pattern 6 — Click-outside closes toggle button clicks
```tsx
// Document click handler that doesn't exclude trigger
useEffect(() => {
  const handleClick = (e: MouseEvent) => {
    if (!menuRef.current?.contains(e.target as Node)) {
      setIsOpen(false); // Closes even when toggle was clicked!
    }
  };
  document.addEventListener('click', handleClick);
  return () => document.removeEventListener('click', handleClick);
}, []);
```
Result: menu never opens because toggle is outside menu element.

**Fix:**
```tsx
if (!menuRef.current?.contains(target) && !triggerRef.current?.contains(target)) {
  setIsOpen(false);
}
```

---

## 7) Verification Protocol (Tailwind/React/shadcn)
### 7.1 Responsive test matrix
Test these sizes:
- 360×640
- 390×844
- 430×932
- 768×1024
- 1024×768+

Also test:
- reduced motion (OS setting)
- iOS Safari (or emulation) scrolling inside the Sheet

### 7.2 Keyboard-only checklist
- Tab reaches `SheetTrigger`
- Enter/Space opens
- Focus lands inside Sheet
- Escape closes
- Focus returns to trigger

### 7.3 Behavior checklist
- Link click closes Sheet
- Route change closes Sheet (Next.js)
- Resize to desktop does not leave Sheet stuck open

### 7.4 Styling/utility checklist
- Trigger visible on mobile (`md:hidden`)
- Desktop links hidden on mobile (`hidden md:flex`)
- No purge issues (classes present in production)

### 7.5 Optional automation
- Playwright/Cypress: verify trigger exists at mobile viewport and sheet opens
- axe-core: basic a11y checks for button name + focus order

---

## 8) Troubleshooting Worksheet (Copy/Paste)
**Viewport (w×h):**

**Framework context:** Next.js? CRA? Vite?

**Observed behavior:**

**Step 1: Trigger rendered?** (Yes/No)
- Trigger selector:
- Trigger breakpoint classes:

**Step 2: Hidden by Tailwind?**
- Computed `display`:
- Classes on trigger/nav:

**Step 3: Sheet state toggles?**
- `data-state` changes to `open`? (Yes/No)

**Step 4: Content clipped?**
- SheetContent scroll container present? (overflow-y-auto)

**Step 5: z-index conflict?**
- Header z-index:
- Sheet overlay z-index:

**Step 6: Prod-only?**
- Tailwind content globs correct?
- Dynamic class strings present?

**Step 3b: Opens then immediately closes?**
- Console shows rapid open→close? (Yes/No)
- Trigger excluded from click-outside? (Yes/No)

**Classification (A–H):**

**Fix applied:**

**Verification completed:**
- responsive matrix:
- keyboard checklist:

---

## 9) Agent Instruction Block (Prompt)
Use this as a “skills” rule set for any Tailwind/React/shadcn mockup.

- Use shadcn/ui primitives: `Sheet` for mobile nav, do not roll your own drawer.
- Breakpoints must be symmetrical:
  - Desktop nav: `hidden md:flex`
  - Mobile trigger: `md:hidden`
- Do not hide `.nav` on mobile without providing a trigger and an accessible menu.
- Avoid dynamic Tailwind class string construction that Tailwind can’t statically detect.
- Mobile menu must not clip items: use `overflow-y-auto`, avoid `justify-center` for lists.
- Ensure keyboard UX: trigger must be a button; Escape closes; focus returns.
- Close the Sheet on link click and on route change.
- If using document-level click-outside detection, always exclude the trigger element.
- Before final output, run the verification protocol and report it.

---

## 10) Case Study: Click-Outside Race Condition (Class H)

**Project:** Morning Brew Collective  
**Date:** January 2026  
**Stack:** Next.js 15, React, Custom CSS (not shadcn Sheet)

### Symptom
Mobile hamburger menu visible but clicking it appeared to do nothing. Menu never opened.

### Initial Hypothesis
Assumed static HTML issue — JavaScript not hydrating properly.

### Investigation
1. Examined rendered HTML: menu element existed with `transform: translateX(100%)`
2. Reviewed `header.tsx`: toggle button correctly called `setIsMobileMenuOpen(true)`
3. Reviewed `mobile-menu.tsx`: component used `isOpen` prop for transform
4. **Key finding:** `handleClickOutside` was attached to `document` on mount

### Root Cause
```tsx
const handleClickOutside = (e: MouseEvent) => {
  const mobileMenu = document.getElementById('mobile-menu');
  if (mobileMenu && !mobileMenu.contains(e.target)) {
    setIsMobileMenuOpen(false); // ← Problem!
  }
};

useEffect(() => {
  document.addEventListener('click', handleClickOutside);
  // ...
}, []);
```

**Event sequence on button click:**
1. User clicks `.menu-toggle` button
2. React `onClick` fires → `setIsMobileMenuOpen(true)`
3. Click event bubbles to `document`
4. `handleClickOutside` fires
5. Button is NOT inside `#mobile-menu`
6. `setIsMobileMenuOpen(false)` → menu closes immediately

### Fix Applied
```tsx
const handleClickOutside = (e: MouseEvent) => {
  const target = e.target as HTMLElement;
  const mobileMenu = document.getElementById('mobile-menu');
  const menuToggle = document.querySelector('.menu-toggle');
  
  // Exclude BOTH menu AND toggle button
  if (mobileMenu && !mobileMenu.contains(target) && !menuToggle?.contains(target)) {
    setIsMobileMenuOpen(false);
  }
};
```

### Lessons Learned
1. **Always log both open and close handlers** when debugging state issues
2. **Document-level listeners fire after component handlers** due to bubbling
3. **Click-outside logic must exclude trigger elements**, not just the menu itself
4. This bug is invisible in static HTML inspection — the DOM is correct, the race condition is temporal

### Classification
**Class H** — Click-outside handler race condition
