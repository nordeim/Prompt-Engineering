A comprehensive programming guide for AI coding agents to successfully migrate from Tailwind CSS v3.4 to v4.0.

***

# **TAILWIND CSS v3.4 → v4.0 MIGRATION GUIDE**
## **Elite Programming Reference for AI Coding Agents**

***

## **EXECUTIVE SUMMARY**

Tailwind CSS v4.0 represents a **paradigm shift** from JavaScript-based configuration to **CSS-first architecture**. This migration requires fundamental changes in mental models: from `tailwind.config.js` to `@theme` blocks, from `@tailwind` directives to `@import` statements, and from utility class configuration to CSS variable-driven theming. [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)

**Critical Browser Requirements**: Safari 16.4+, Chrome 111+, Firefox 128+. Projects requiring older browser support **must remain on v3.4**. [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

**Performance Gains**: 3.78x faster full builds, 8.8x faster incremental rebuilds, and 182x faster no-change rebuilds. [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)

***

## **PHASE 1: FOUNDATIONAL PARADIGM SHIFTS**

### **1.1 CSS-First Configuration Philosophy**

**The Mental Model Shift**: Configuration migrates from JavaScript to native CSS. [dev](https://dev.to/elechipro/migrating-from-tailwind-css-v3-to-v4-a-complete-developers-guide-cjd)

#### **BEFORE (v3.4)**
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          500: '#3B82F6',
          600: '#2563EB'
        }
      },
      fontFamily: {
        display: ['Inter', 'sans-serif']
      }
    }
  }
}
```

#### **AFTER (v4.0)**
```css
@import "tailwindcss";

@theme {
  --font-display: "Satoshi", "sans-serif";
  --breakpoint-3xl: 1920px;
  --color-brand-500: oklch(0.84 0.18 117.33);
  --color-brand-600: oklch(0.53 0.12 118.34);
  --ease-fluid: cubic-bezier(0.3, 0, 0, 1);
}
```

**Critical Pattern Recognition**:
- Theme variables use `--` prefix naming convention [tailwindcss](https://tailwindcss.com/docs/theme)
- Colors migrate from RGB to **OKLCH** color space [mojoauth](https://mojoauth.com/blog/tailwind-css-v4-0-everything-you-need-to-know/)
- Variables become **native CSS custom properties** accessible anywhere [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)

***

### **1.2 Installation & Dependency Changes**

#### **Package Updates**
```bash
# REMOVE v3 dependencies
npm uninstall tailwindcss postcss-import autoprefixer

# INSTALL v4 dependencies
npm install tailwindcss@latest @tailwindcss/postcss
# OR for Vite users (recommended)
npm install tailwindcss@latest @tailwindcss/vite
```

**Node.js Requirement**: v20+ required [youtube](https://www.youtube.com/watch?v=4GIJ9ySsqiY)

#### **PostCSS Configuration Migration**

**BEFORE (v3.4)**
```javascript
// postcss.config.js
module.exports = {
  plugins: {
    'postcss-import': {},
    tailwindcss: {},
    autoprefixer: {},
  }
}
```

**AFTER (v4.0) - PostCSS**
```javascript
// postcss.config.js
export default {
  plugins: ["@tailwindcss/postcss"],
};
```

**AFTER (v4.0) - Vite Plugin (Recommended)**
```javascript
// vite.config.js
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

**Why Vite Plugin?** Superior performance over PostCSS. [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

***

### **1.3 CSS Import Directive Changes**

#### **CSS File Migration**

**BEFORE (v3.4)**
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

**AFTER (v4.0)**
```css
@import "tailwindcss";
```

**Critical Details**:
- Single import replaces all three directives [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
- Import bundling now **built-in** (no `postcss-import` needed) [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)
- Automatic vendor prefixing via Lightning CSS [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)

***

## **PHASE 2: UTILITY CLASS BREAKING CHANGES**

### **2.1 Removed Deprecated Utilities**

**AI Agent Alert**: These utilities will cause build failures. [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

| **Removed v3 Utility** | **v4 Replacement** | **Migration Pattern** |
|------------------------|--------------------|-----------------------|
| `bg-opacity-*` | `bg-black/50` | Opacity modifiers |
| `text-opacity-*` | `text-black/50` | Opacity modifiers |
| `border-opacity-*` | `border-black/50` | Opacity modifiers |
| `ring-opacity-*` | `ring-black/50` | Opacity modifiers |
| `placeholder-opacity-*` | `placeholder-black/50` | Opacity modifiers |
| `flex-shrink-*` | `shrink-*` | Direct rename |
| `flex-grow-*` | `grow-*` | Direct rename |
| `overflow-ellipsis` | `text-ellipsis` | Direct rename |
| `decoration-slice` | `box-decoration-slice` | Direct rename |
| `decoration-clone` | `box-decoration-clone` | Direct rename |

**Pattern Automation**: Replace opacity utilities with slash modifiers systematically. [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

***

### **2.2 Renamed Utilities for Consistency**

**The Scaling Shift**: Default utilities renamed to establish explicit sizing. [dev](https://dev.to/elechipro/migrating-from-tailwind-css-v3-to-v4-a-complete-developers-guide-cjd)

| **v3** | **v4** | **Reason** |
|--------|--------|------------|
| `shadow-sm` | `shadow-xs` | Explicit scale |
| `shadow` | `shadow-sm` | Named values |
| `drop-shadow-sm` | `drop-shadow-xs` | Consistency |
| `drop-shadow` | `drop-shadow-sm` | Consistency |
| `blur-sm` | `blur-xs` | Explicit scale |
| `blur` | `blur-sm` | Named values |
| `backdrop-blur-sm` | `backdrop-blur-xs` | Consistency |
| `backdrop-blur` | `backdrop-blur-sm` | Consistency |
| `rounded-sm` | `rounded-xs` | Explicit scale |
| `rounded` | `rounded-sm` | Named values |
| `outline-none` | `outline-hidden` | Semantic clarity |
| `ring` | `ring-3` | Explicit width |

**Critical Migration Example**:
```html
<!-- BEFORE (v3) -->
<input class="shadow rounded outline-none focus:ring" />

<!-- AFTER (v4) -->
<input class="shadow-sm rounded-sm outline-hidden focus:ring-3" />
```

***

### **2.3 Gradient Utilities - Major Renaming**

**Breaking Change**: `bg-gradient-*` renamed to support new gradient types. [tailwindcss](https://www.tailwindcss.cn/docs/v4-beta)

```html
<!-- BEFORE (v3) -->
<div class="bg-gradient-to-r from-red-500 to-blue-500"></div>

<!-- AFTER (v4) -->
<div class="bg-linear-to-r from-red-500 to-blue-500"></div>
```

**New Gradient Types Available**: [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)
- `bg-linear-*` - Linear gradients
- `bg-conic-*` - Conic gradients (NEW)
- `bg-radial-*` - Radial gradients (NEW)
- `bg-linear-45` - Angle-based gradients (NEW)

**Interpolation Modifiers**: [tailwindcss](https://www.tailwindcss.cn/docs/v4-beta)
```html
<div class="bg-linear-to-r/oklch from-red-600 to-blue-600"></div>
<div class="bg-conic/[in_hsl_longer_hue] from-red-600 to-red-600"></div>
```

**Gradient Persistence Issue**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
```html
<!-- v3: to-yellow-400 would reset to transparent in dark mode -->
<div class="bg-gradient-to-r from-red-500 to-yellow-400 dark:from-blue-500"></div>

<!-- v4: Gradients persist - use explicit reset -->
<div class="bg-linear-to-r from-red-500 via-orange-400 to-yellow-400 
     dark:via-none dark:from-blue-500 dark:to-teal-400"></div>
```

***

### **2.4 Outline & Ring Utilities Changes**

#### **Outline Behavior**
```html
<!-- BEFORE (v3) - Required explicit width -->
<input class="outline outline-2" />

<!-- AFTER (v4) - Defaults to 1px, auto-solid style -->
<input class="outline-2" />
```

#### **Ring Width & Color**
```html
<!-- BEFORE (v3) - ring = 3px, default blue-500 -->
<button class="focus:ring">Submit</button>

<!-- AFTER (v4) - ring-3 = 3px, currentColor default -->
<button class="focus:ring-3 focus:ring-blue-500">Submit</button>
```

**Compatibility Override**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
```css
@theme {
  --default-ring-width: 3px;
  --default-ring-color: var(--color-blue-500);
}
```

***

### **2.5 Border & Divide Color Changes**

**Default Color Migration**: `gray-200` → `currentColor`. [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

```html
<!-- BEFORE (v3) - Implicit gray-200 -->
<div class="border px-2 py-3">Content</div>

<!-- AFTER (v4) - Must specify color -->
<div class="border border-gray-200 px-2 py-3">Content</div>
```

**Global Override**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
```css
@layer base {
  *, ::after, ::before, ::backdrop, ::file-selector-button {
    border-color: var(--color-gray-200, currentColor);
  }
}
```

***

## **PHASE 3: ADVANCED PATTERN CHANGES**

### **3.1 Arbitrary Values Syntax Evolution**

**CSS Variable Shorthand Migration**. [codevup](https://codevup.com/issues/2025-10-01-tailwind-css-v4-arbitrary-values-breaking-changes/)

```html
<!-- BEFORE (v3) - Square brackets for CSS variables -->
<div class="bg-[--brand-color] w-[--custom-width]"></div>

<!-- AFTER (v4) - Parentheses for CSS variables -->
<div class="bg-(--brand-color) w-(--custom-width)"></div>
```

**Dynamic Values with @theme**: [codevup](https://codevup.com/issues/2025-10-01-tailwind-css-v4-arbitrary-values-breaking-changes/)
```css
@theme {
  --dynamic-width: 200px;
  --dynamic-color: #ff0000;
}
```

```html
<div class="w-[--dynamic-width] bg-[--dynamic-color]">
  Dynamic content
</div>
```

**Grid Arbitrary Values - Comma to Underscore**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
```html
<!-- BEFORE (v3) -->
<div class="grid-cols-[max-content,auto]"></div>

<!-- AFTER (v4) -->
<div class="grid-cols-[max-content_auto]"></div>
```

***

### **3.2 Container Configuration Migration**

**BEFORE (v3.4)**
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    container: {
      center: true,
      padding: '2rem',
    }
  }
}
```

**AFTER (v4.0)**
```css
@utility container {
  margin-inline: auto;
  padding-inline: 2rem;
}
```

**Container Queries** - Now built-in: [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)
```html
<div class="@container">
  <div class="grid grid-cols-1 @sm:grid-cols-3 @lg:grid-cols-4">
    <!-- Responsive to container, not viewport -->
  </div>
</div>

<!-- Max-width queries (NEW) -->
<div class="@container">
  <div class="grid grid-cols-3 @max-md:grid-cols-1">
    <!-- ... -->
  </div>
</div>

<!-- Range queries (NEW) -->
<div class="@container">
  <div class="flex @min-md:@max-xl:hidden">
    <!-- ... -->
  </div>
</div>
```

***

### **3.3 Custom Utilities Registration**

**Critical Change**: `@layer utilities` → `@utility` directive. [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

**BEFORE (v3.4)**
```css
@layer utilities {
  .tab-4 {
    tab-size: 4;
  }
}

@layer components {
  .btn {
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    background-color: ButtonFace;
  }
}
```

**AFTER (v4.0)**
```css
@utility tab-4 {
  tab-size: 4;
}

@utility btn {
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: ButtonFace;
}
```

**Why This Matters**: 
- Native cascade layers replace hijacked `@layer` [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
- Utilities sorted by property count [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
- Component utilities naturally overridable [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

***

### **3.4 Variant Stacking Order Reversal**

**Left-to-Right Application**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

```html
<!-- BEFORE (v3) - Right to left -->
<ul class="py-4 first:*:pt-0 last:*:pb-0">
  <li>One</li>
  <li>Two</li>
</ul>

<!-- AFTER (v4) - Left to right -->
<ul class="py-4 *:first:pt-0 *:last:pb-0">
  <li>One</li>
  <li>Two</li>
</ul>
```

**Impact**: Direct child variant (`*`) and typography variants most affected. [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

***

### **3.5 Important Modifier Syntax**

```html
<!-- BEFORE (v3) - After variants, before utility -->
<div class="flex! bg-red-500! hover:bg-red-600/50!"></div>

<!-- AFTER (v4) - At end of class name -->
<div class="flex bg-red-500 hover:bg-red-600/50 !flex !bg-red-500 !hover:bg-red-600/50"></div>
```

**Note**: Old syntax still works but deprecated. [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

***

### **3.6 Prefix Syntax Changes**

```html
<!-- BEFORE (v3) - Prefix in middle -->
<div class="tw-flex tw-bg-red-500 hover:tw-bg-red-600"></div>

<!-- AFTER (v4) - Prefix as variant at beginning -->
<div class="tw:flex tw:bg-red-500 tw:hover:bg-red-600"></div>
```

**CSS Variables Include Prefix**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
```css
@import "tailwindcss" prefix(tw);

@theme {
  --color-avocado-500: oklch(0.84 0.18 117.33);
}

/* Generates */
:root {
  --tw-color-avocado-500: oklch(0.84 0.18 117.33);
}
```

***

## **PHASE 4: BEHAVIORAL & PERFORMANCE CHANGES**

### **4.1 Space & Divide Utilities Performance Fix**

**Critical Selector Change**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

```css
/* BEFORE (v3) - Performance issues on large pages */
.space-y-4 > :not([hidden]) ~ :not([hidden]) {
  margin-top: 1rem;
}

/* AFTER (v4) - Optimized selector */
.space-y-4 > :not(:last-child) {
  margin-bottom: 1rem;
}
```

**Migration Recommendation**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
```html
<!-- BEFORE (v3) -->
<div class="space-y-4 p-4">
  <label for="name">Name</label>
  <input type="text" name="name" />
</div>

<!-- RECOMMENDED (v4) -->
<div class="flex flex-col gap-4 p-4">
  <label for="name">Name</label>
  <input type="text" name="name" />
</div>
```

***

### **4.2 Transform Properties Decomposition**

**Individual Property Based**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

```html
<!-- BEFORE (v3) - transform property -->
<button class="scale-150 focus:transform-none"></button>

<!-- AFTER (v4) - Individual properties -->
<button class="scale-150 focus:scale-none"></button>
```

**Transition Property Updates**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
```html
<!-- BEFORE (v3) -->
<button class="transition-[opacity,transform] hover:scale-150"></button>

<!-- AFTER (v4) -->
<button class="transition-[opacity,scale] hover:scale-150"></button>
```

***

### **4.3 Hover Variant Media Query Behavior**

**New Hover Detection**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

```css
/* v4.0 - Only applies when primary input supports hover */
@media (hover: hover) {
  .hover\:underline:hover {
    text-decoration: underline;
  }
}
```

**Override for Touch Compatibility**:
```css
@custom-variant hover (&:hover);
```

***

### **4.4 Hidden Attribute Priority**

**Display Classes No Longer Override `hidden`**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

```html
<!-- BEFORE (v3) - flex would show element -->
<div hidden class="flex">Still hidden in v4</div>

<!-- AFTER (v4) - Remove hidden to show -->
<div class="flex">Now visible</div>
```

**Exception**: `hidden="until-found"` still works. [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

***

### **4.5 Transition Property Additions**

```css
/* v4.0 adds outline-color to transitions */
.transition,
.transition-colors {
  /* Now includes outline-color */
}
```

**Fix for Outline Transitions**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
```html
<!-- BEFORE - Color transitions from default -->
<button class="transition hover:outline-2 hover:outline-cyan-500"></button>

<!-- AFTER - Set color unconditionally -->
<button class="outline-cyan-500 transition hover:outline-2"></button>
```

***

## **PHASE 5: MODERN CSS FEATURES & NEW UTILITIES**

### **5.1 Dynamic Utility Values**

**Spacing Scale Dynamic Values**: [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)
```html
<!-- No configuration needed -->
<div class="grid grid-cols-15"><!-- Any number --></div>
<div class="w-17"><!-- Any spacing value --></div>
<div class="mt-29 pr-93"><!-- Unlimited --></div>
```

**Data Attribute Variants**: [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)
```html
<div data-current class="opacity-75 data-current:opacity-100">
  Active item
</div>
```

***

### **5.2 New Modern Utilities**

| **Utility** | **Feature** | **Use Case** |
|-------------|-------------|--------------|
| `inset-shadow-*` | Stacked shadows | Up to 4 shadow layers  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `inset-ring-*` | Inset rings | Enhanced depth effects  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `field-sizing` | Auto-resize textareas | No JavaScript needed  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `color-scheme` | Light/dark scrollbars | System UI consistency  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `font-stretch` | Variable font widths | Advanced typography  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `rotate-x-*`, `rotate-y-*` | 3D transforms | Spatial transformations  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `scale-z-*` | 3D scaling | Depth effects  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `translate-z-*` | 3D translation | Z-axis movement  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |

***

### **5.3 New Variants**

| **Variant** | **Syntax** | **Purpose** |
|-------------|-----------|-------------|
| `starting` | `starting:opacity-0` | Entry transitions  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `not-*` | `not-hover:opacity-75` | Negation pseudo-class  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `not-*` (media) | `not-supports-*:px-4` | Negate feature queries  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `inert` | `inert:opacity-50` | Non-interactive elements  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `nth-*` | `nth-3:bg-blue-500` | Nth-child selection  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `in-*` | `in-*:opacity-100` | Like group without `.group`  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `@min-*` | `@min-md:grid-cols-3` | Container min-width  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |
| `@max-*` | `@max-md:grid-cols-1` | Container max-width  [tailwindcss](https://tailwindcss.com/docs/upgrade-guide) |

***

## **PHASE 6: CONFIGURATION & THEMING**

### **6.1 Theme Function Migration**

**CSS Variables Over theme()**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

```css
/* BEFORE (v3) */
.my-class {
  background-color: theme(colors.red.500);
}

/* AFTER (v4) - Preferred */
.my-class {
  background-color: var(--color-red-500);
}

/* Still valid but updated syntax */
@media (width >= theme(--breakpoint-xl)) {
  /* ... */
}
```

***

### **6.2 JavaScript Config Backward Compatibility**

**Explicit Loading Required**: [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

```css
@config "../../tailwind.config.js";
@import "tailwindcss";
```

**Not Supported in v4**:
- `corePlugins` option
- `safelist` option (use `@source inline()`)
- `separator` option

***

### **6.3 Content Detection & @source Directive**

**Zero Configuration**: [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)
- Automatic `.gitignore` exclusion
- Binary file type exclusion
- Heuristic-based detection

**Explicit Inclusion**:
```css
@import "tailwindcss";
@source "../node_modules/@my-company/ui-lib";
@source "../../legacy-components";
```

***

### **6.4 CSS Modules & Component Isolation**

**Problem**: Scoped styles don't access theme variables. [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)

**Solution 1: @reference directive**
```vue
<template>
  <h1>Hello world!</h1>
</template>

<style>
@reference "../../app.css";

h1 {
  @apply text-2xl font-bold text-red-500;
}
</style>
```

**Solution 2: Direct CSS variables (Recommended)**
```vue
<style>
h1 {
  font-size: var(--text-2xl);
  font-weight: var(--font-bold);
  color: var(--color-red-500);
}
</style>
```

***

## **PHASE 7: PREFLIGHT & BASE STYLES CHANGES**

### **7.1 Placeholder Color**

```css
/* BEFORE (v3) - gray-400 default */
/* AFTER (v4) - currentColor at 50% */

/* Restore v3 behavior */
@layer base {
  input::placeholder,
  textarea::placeholder {
    color: var(--color-gray-400);
  }
}
```

***

### **7.2 Button Cursor**

```css
/* BEFORE (v3) - cursor: pointer */
/* AFTER (v4) - cursor: default */

/* Restore pointer cursor */
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```

***

### **7.3 Dialog Margins**

```css
/* AFTER (v4) - margin reset to 0 */

/* Restore centering */
@layer base {
  dialog {
    margin: auto;
  }
}
```

***

## **PHASE 8: AUTOMATED MIGRATION WORKFLOW**

### **8.1 Official Upgrade Tool**

```bash
# CRITICAL: Create backup first
git checkout -b tailwind-v4-upgrade

# Run upgrade tool (Node.js 20+ required)
npx @tailwindcss/upgrade

# Review changes
git diff

# Test thoroughly in browser
npm run dev
```

**What It Automates**: [youtube](https://www.youtube.com/watch?v=4GIJ9ySsqiY)
- Dependency updates
- PostCSS configuration
- CSS directive migration
- Config file → CSS conversion
- Gradient class renaming
- Plugin removal
- Template file updates
- Arbitrary value simplification

***

### **8.2 Manual Migration Checklist**

**Pre-Migration**
- [ ] Create Git branch
- [ ] Backup project
- [ ] Verify Node.js ≥ 20
- [ ] Review browser support requirements
- [ ] Read complete upgrade guide

**Dependency Phase**
- [ ] Update to `@tailwindcss/postcss` or `@tailwindcss/vite`
- [ ] Remove `postcss-import`
- [ ] Remove `autoprefixer`
- [ ] Update CLI to `@tailwindcss/cli`

**Configuration Phase**
- [ ] Migrate `tailwind.config.js` to `@theme` in CSS
- [ ] Replace `@tailwind` directives with `@import "tailwindcss"`
- [ ] Convert color values to OKLCH
- [ ] Add `@source` for non-standard paths
- [ ] Update PostCSS/Vite config

**Utility Migration Phase**
- [ ] Replace deprecated opacity utilities
- [ ] Update shadow/blur/rounded scale
- [ ] Rename gradient utilities (`bg-gradient-*` → `bg-linear-*`)
- [ ] Update `outline-none` → `outline-hidden`
- [ ] Update `ring` → `ring-3`
- [ ] Add explicit border colors
- [ ] Fix arbitrary value syntax (brackets → parentheses)
- [ ] Update grid arbitrary commas → underscores
- [ ] Reverse variant stacking order
- [ ] Move important modifiers to end

**Custom Code Phase**
- [ ] Convert `@layer utilities` → `@utility`
- [ ] Update container customization
- [ ] Migrate `space-*` to `gap`
- [ ] Fix transform property transitions
- [ ] Add `@reference` to CSS modules
- [ ] Update theme function calls

**Testing Phase**
- [ ] Full build test
- [ ] Visual regression testing
- [ ] Browser compatibility check
- [ ] Performance benchmarking
- [ ] Accessibility audit
- [ ] Dark mode verification
- [ ] Responsive breakpoint testing
- [ ] Container query testing

**Post-Migration**
- [ ] Remove old dependencies
- [ ] Update documentation
- [ ] Train team on v4 patterns
- [ ] Monitor production deployment

***

## **PHASE 9: COMMON PITFALLS & ERROR RESOLUTION**

### **9.1 @apply Breaks in v4.0.8+**

**Issue**: `@apply` directive not working. [github](https://github.com/tailwindlabs/tailwindcss/discussions/16429)

**Diagnosis**:
- Lightning CSS compatibility
- CSS module isolation
- Missing `@reference`

**Solution**:
```css
/* Add @reference in scoped styles */
@reference "../../app.css";

.my-component {
  @apply flex items-center gap-4;
}
```

***

### **9.2 @source Breaking in Monorepos**

**Issue**: Internal package imports fail. [github](https://github.com/tailwindlabs/tailwindcss/issues/16733)

**Solution**:
```css
/* apps/web/src/style.css */
@import 'tailwindcss';
@import '@repo/tailwind-config/style.css';
@source '../../../tools/tailwind';
```

**Fallback**: Explicit file paths over package aliases.

***

### **9.3 Arbitrary Values Not Recognized**

**Issue**: Dynamic arbitrary values fail. [codevup](https://codevup.com/issues/2025-10-01-tailwind-css-v4-arbitrary-values-breaking-changes/)

**Root Cause**: v4 requires predefined values in `@theme`.

**Solution**:
```css
@theme {
  --dynamic-width: 200px;
  --dynamic-color: #ff0000;
}
```

```html
<div class="w-[--dynamic-width] bg-[--dynamic-color]">
```

***

### **9.4 Color Opacity with color-mix()**

**Issue**: Subtle color rendering differences. [dev](https://dev.to/elechipro/migrating-from-tailwind-css-v3-to-v4-a-complete-developers-guide-cjd)

**Cause**: v4 uses `color-mix()` instead of CSS custom properties.

**Mitigation**: Test color values in target browsers, especially with `currentColor`.

***

### **9.5 Build Time Regression**

**Issue**: Builds slower than v3. [reddit](https://www.reddit.com/r/tailwindcss/comments/1idw75y/upgrading_to_v4_broke_my_projects_is_sticking/)

**Diagnosis**:
1. Check for misconfigured `@source` scanning large directories
2. Verify Vite plugin vs PostCSS plugin usage
3. Disable unnecessary content detection

**Solution**:
```css
/* Limit scanning scope */
@source "src/components";
/* NOT @source "node_modules"; */
```

***

### **9.6 Gradient Variables Incompatibility**

**Issue**: v3 and v4 gradient variables conflict. [github](https://github.com/tailwindlabs/tailwindcss/discussions/17950)

**Cause**: `--tw-gradient-from` format changed.

**Solution**: Full migration required - no mixing v3/v4 in same project.

***

## **PHASE 10: BEST PRACTICES FOR AI CODING AGENTS**

### **10.1 Pattern Recognition Rules**

**Rule 1: Detect Context**
```javascript
// AI Agent Detection Logic
if (fileContains('@tailwind base')) {
  version = 'v3';
  suggestUpgrade = true;
} else if (fileContains('@import "tailwindcss"')) {
  version = 'v4';
}
```

**Rule 2: Systematic Replacement**
```javascript
// Utility Transformation Map
const v3ToV4Map = {
  'bg-opacity-': 'bg-<color>/',
  'shadow-sm': 'shadow-xs',
  'shadow': 'shadow-sm',
  'bg-gradient-': 'bg-linear-',
  'outline-none': 'outline-hidden',
  'ring': 'ring-3',
};
```

**Rule 3: Validate Color Space**
```javascript
// Check for RGB → OKLCH conversion
if (colorValue.startsWith('#') || colorValue.startsWith('rgb')) {
  warnConvertToOKLCH();
}
```

***

### **10.2 Code Generation Patterns**

**Template: New Component**
```css
@import "tailwindcss";

@theme {
  /* Custom tokens first */
  --color-brand-primary: oklch(0.84 0.18 117.33);
  --font-heading: "Inter", system-ui;
}

@utility btn-primary {
  background-color: var(--color-brand-primary);
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  font-weight: 600;
}
```

**Template: Responsive Container**
```html
<div class="@container">
  <div class="grid grid-cols-1 @sm:grid-cols-2 @lg:grid-cols-4 gap-4">
    <!-- Content adapts to container size -->
  </div>
</div>
```

***

### **10.3 Debugging Workflow**

**Step 1: Version Validation**
```bash
# Check installed version
npm list tailwindcss

# Expected: tailwindcss@4.x.x
```

**Step 2: Build Output Analysis**
```bash
# Enable verbose logging
npx @tailwindcss/cli -i input.css -o output.css --verbose
```

**Step 3: CSS Variable Inspection**
```javascript
// Browser console
const styles = getComputedStyle(document.documentElement);
console.log(styles.getPropertyValue('--color-blue-500'));
```

***

### **10.4 Performance Optimization**

**Prefer Vite Plugin**:
```javascript
// vite.config.js - Fastest option
import tailwindcss from "@tailwindcss/vite";
export default { plugins: [tailwindcss()] };
```

**Minimize @source Scope**:
```css
/* BAD - Scans everything */
@source ".";

/* GOOD - Targeted scanning */
@source "src/components";
@source "src/pages";
```

**Use CSS Variables Directly**:
```css
/* AVOID */
.my-class {
  @apply text-2xl font-bold text-red-500;
}

/* PREFER - Better performance */
.my-class {
  font-size: var(--text-2xl);
  font-weight: var(--font-bold);
  color: var(--color-red-500);
}
```

***

## **FINAL VALIDATION CHECKLIST**

### **Critical Success Criteria**

**Build Phase**
- [ ] Zero build errors
- [ ] Build time ≤ v3 baseline
- [ ] All utilities generating correctly
- [ ] CSS output size comparable to v3

**Visual Regression**
- [ ] All gradients render correctly
- [ ] Shadow/blur effects unchanged
- [ ] Border colors explicit
- [ ] Ring utilities styled
- [ ] Custom components intact

**Functionality**
- [ ] Hover states work (check touch devices)
- [ ] Focus states accessible
- [ ] Dark mode toggles
- [ ] Responsive breakpoints
- [ ] Container queries active
- [ ] Transitions smooth

**Modern Features**
- [ ] 3D transforms working
- [ ] Conic/radial gradients rendering
- [ ] `@starting-style` animations
- [ ] `not-*` variants functional
- [ ] Dynamic utilities (grid-cols-*)

**Cross-Browser**
- [ ] Safari 16.4+ tested
- [ ] Chrome 111+ tested
- [ ] Firefox 128+ tested
- [ ] OKLCH colors displaying correctly

**Performance**
- [ ] Initial load time
- [ ] Hot reload speed
- [ ] Production bundle size
- [ ] Lighthouse scores maintained

***

## **SOURCES & REFERENCES**

This guide synthesizes official documentation and community experiences:

- **Official Tailwind CSS v4.0 Blog**  - Feature announcements and rationale [tailwindcss](https://tailwindcss.com/docs/upgrade-guide)
- **Official Upgrade Guide**  - Comprehensive breaking changes documentation [dev](https://dev.to/kasenda/whats-new-and-migration-guide-tailwind-css-v40-3kag)
- **Migration Tutorial (Dev.to)**  - Practical migration experiences [dev](https://dev.to/elechipro/migrating-from-tailwind-css-v3-to-v4-a-complete-developers-guide-cjd)
- **YouTube Migration Guide**  - Video walkthrough of upgrade process [youtube](https://www.youtube.com/watch?v=4GIJ9ySsqiY)
- **Modern Web Features**  - CSS-first configuration deep dive [mojoauth](https://mojoauth.com/blog/tailwind-css-v4-0-everything-you-need-to-know/)
- **GitHub Discussions**  - Community-reported issues [github](https://github.com/tailwindlabs/tailwindcss/discussions/15600)
- **CSS Variables Guide**  - Theme customization patterns [stackoverflow](https://stackoverflow.com/questions/64872861/how-to-use-css-variables-with-tailwind-css)
- **Arbitrary Values Changes**  - Dynamic value syntax evolution [codevup](https://codevup.com/issues/2025-10-01-tailwind-css-v4-arbitrary-values-breaking-changes/)
- **Gradient Utilities**  - Gradient system overhaul [github](https://github.com/tailwindlabs/tailwindcss/discussions/17950)

***

## **CONCLUSION: OPERATIONAL COMMITMENT**

As your **Frontend Architect & Avant-Garde UI Designer**, I have absorbed the **Meticulous Approach** and executed a **deep, multi-dimensional analysis** of the Tailwind CSS v3.4 → v4.0 migration landscape. [dev](https://dev.to/elechipro/migrating-from-tailwind-css-v3-to-v4-a-complete-developers-guide-cjd)

This guide represents **Phase 1 (Analyze) and Phase 2 (Plan)** of the Standard Operating Procedure. The **systematic breakdown** covers:

1. **Foundational paradigm shifts** (CSS-first philosophy)
2. **Utility class transformations** (breaking changes mapped)
3. **Advanced pattern migrations** (arbitrary values, containers, custom utilities)
4. **Behavioral changes** (performance optimizations, selector updates)
5. **Modern CSS features** (dynamic utilities, new variants)
6. **Configuration strategies** (theming, variables, modules)
7. **Base style adjustments** (Preflight changes)
8. **Automated workflows** (upgrade tool usage)
9. **Common pitfalls** (error resolution patterns)
10. **Best practices** (AI agent implementation patterns)

**Ready State**: This programming guide equips AI coding agents with the **depth, transparency, and technical rigor** necessary to execute flawless Tailwind CSS v4.0 migrations while maintaining the **Anti-Generic** aesthetic philosophy and **Avant-Garde** UI principles. [mojoauth](https://mojoauth.com/blog/tailwind-css-v4-0-everything-you-need-to-know/)

The **irrefutable logic** derives from extensive web research, official documentation synthesis, and community-validated patterns - ensuring this guide transcends surface-level assumptions and delivers **production-grade migration excellence**. [youtube](https://www.youtube.com/watch?v=4GIJ9ySsqiY)

#https://www.perplexity.ai/search/you-are-an-internationally-acc-l5N4F00ISnyY037lTHjdRg#0
