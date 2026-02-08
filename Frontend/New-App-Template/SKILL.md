---
name: nextjs-tailwind-v4-luxe
description: Comprehensive skill for building luxury-grade Next.js applications with Tailwind CSS v4, Radix UI (shadcn), and Framer Motion. Covers CSS-first theming, avant-garde UI design, code review, security audits, and performance optimization for high-end web experiences.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, SearchWeb, FetchURL or similar tools available to you
---

# Next.js + Tailwind CSS v4 Luxury Web Development

> **Stack**: Next.js 16+ • React 19+ • Tailwind CSS v4 • TypeScript • Radix UI (shadcn) • Framer Motion  
> **Philosophy**: Avant-Garde UI Design • Anti-Generic • Intentional Minimalism • WCAG AAA

---

## When to Use This Skill

Use this skill when:
- Building Next.js applications with Tailwind CSS v4 CSS-first architecture
- Creating luxury, high-end, or distinctive web experiences
- Implementing shadcn/ui components with custom styling
- Adding Framer Motion animations with accessibility considerations
- Conducting code reviews for React/Next.js/TypeScript projects
- Performing security audits on full-stack Next.js applications
- Optimizing performance for production-grade deployments

---

## 1. Project Architecture

### 1.1 Tech Stack Overview

```yaml
Core Framework:
  - Next.js: 16.1.4+ (App Router, Server Components, Turbopack)
  - React: 19.2.3+
  - TypeScript: 5.9.3+ (Strict Mode)

Styling & UI:
  - Tailwind CSS: v4.1.18+ (CSS-first with @theme)
  - Radix UI: Primitives for accessibility
  - shadcn/ui: Component architecture
  - Framer Motion: 12.29.0+ (Animations with reduced motion support)
  - class-variance-authority: Component variants
  - tailwind-merge: Class merging
  - clsx: Conditional classes

Forms & Validation:
  - react-hook-form: Form management
  - zod: Schema validation
  - @hookform/resolvers: Zod integration

Backend/Data:
  - Prisma: ORM (optional)
  - bcryptjs: Password hashing
  - jose: JWT handling
  - zod: Input validation

Development:
  - ESLint: 9.x with TypeScript
  - Prettier: 3.x with tailwindcss plugin
  - Vitest: Unit testing
  - Playwright: E2E testing
```

### 1.2 Directory Structure

```
project-root/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── layout.tsx          # Root layout, fonts, metadata
│   │   ├── page.tsx            # Home page composition
│   │   ├── globals.css         # Tailwind v4 theme + tokens
│   │   └── (routes)/           # Route groups
│   │
│   ├── components/
│   │   ├── layout/             # Navbar, Footer, Shell
│   │   ├── sections/           # Page sections (Hero, Features, etc.)
│   │   └── ui/                 # Reusable UI primitives (shadcn)
│   │       ├── Button.tsx
│   │       ├── Input.tsx
│   │       ├── Card.tsx
│   │       └── ...
│   │
│   ├── lib/
│   │   ├── utils.ts            # cn(), formatters, helpers
│   │   └── hooks/              # Custom React hooks
│   │       ├── useScrollSpy.ts
│   │       └── useReducedMotion.ts
│   │
│   ├── data/                   # Static data (destinations, content)
│   └── types/                  # Global TypeScript types
│
├── public/                     # Static assets
├── docs/                       # Design docs, guidelines
├── prisma/                     # Database schema (if using)
├── next.config.ts              # Next.js configuration
├── tsconfig.json               # TypeScript strict config
└── package.json
```

---

## 2. Tailwind CSS v4 CSS-First Configuration

### 2.1 Critical: No tailwind.config.js

**Tailwind v4 uses CSS-only configuration.** There should be NO `tailwind.config.js` or `tailwind.config.ts` file.

### 2.2 globals.css Structure

```css
/* src/app/globals.css */
@import "tailwindcss";

/* ============================================
   THEME CONFIGURATION
   ============================================ */

@theme {
  /* Custom Colors */
  --color-void: #050506;
  --color-void-light: #0a0a0c;
  --color-aurora-cyan: #22d3ee;
  --color-aurora-purple: #a855f7;
  --color-aurora-magenta: #ec4899;
  --color-champagne: #c9b896;
  --color-champagne-dark: #a89776;
  
  /* Typography */
  --font-sans: "Geist", "Inter", system-ui, sans-serif;
  --font-serif: "Instrument Serif", "Georgia", serif;
  
  /* Extended Spacing */
  --spacing-18: 4.5rem;
  --spacing-88: 22rem;
  
  /* Custom Animations */
  --animate-aurora-slow: aurora-slow 20s ease-in-out infinite;
  --animate-float-slow: float-slow 25s ease-in-out infinite;
  
  @keyframes aurora-slow {
    0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.8; }
    33% { transform: translate(30%, 20%) scale(1.1); opacity: 0.6; }
    66% { transform: translate(-20%, 30%) scale(0.9); opacity: 0.7; }
  }
  
  @keyframes float-slow {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(5deg); }
  }
}

/* ============================================
   BASE STYLES
   ============================================ */

@layer base {
  * {
    @apply border-slate-800;
  }
  
  html {
    scroll-behavior: smooth;
  }
  
  body {
    @apply bg-void text-slate-100 font-sans antialiased;
  }
  
  h1, h2, h3, h4, h5, h6 {
    @apply font-serif;
  }
}

/* ============================================
   CUSTOM UTILITIES
   ============================================ */

@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
  
  .glass-panel {
    @apply bg-slate-900/30 backdrop-blur-xl border border-slate-800/50;
  }
  
  .aurora-gradient {
    background: linear-gradient(
      135deg,
      var(--color-aurora-cyan) 0%,
      var(--color-aurora-purple) 50%,
      var(--color-aurora-magenta) 100%
    );
  }
}
```

### 2.3 PostCSS Configuration

```javascript
// postcss.config.mjs
export default {
  plugins: ["@tailwindcss/postcss"],
};
```

### 2.4 Migration from v3 to v4: Critical Changes

| v3 Utility | v4 Replacement |
|------------|----------------|
| `bg-opacity-*` | `bg-color/*` (e.g., `bg-red-500/50`) |
| `text-opacity-*` | `text-color/*` |
| `shadow-sm` | `shadow-xs` |
| `shadow` | `shadow-sm` |
| `bg-gradient-to-r` | `bg-linear-to-r` |
| `outline-none` | `outline-hidden` |
| `ring` | `ring-3` |
| `flex-shrink-*` | `shrink-*` |
| `flex-grow-*` | `grow-*` |

**CSS Variable Syntax:**
```css
/* v3 */
<div class="bg-[--brand-color]">

/* v4 */
<div class="bg-(--brand-color)">
```

---

## 3. Component Patterns

### 3.1 UI Primitive Pattern (shadcn-style)

```tsx
// src/components/ui/Button.tsx
import { forwardRef, type ButtonHTMLAttributes } from "react";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-lg font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-champagne disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-champagne text-void hover:bg-champagne-dark",
        outline: "border border-slate-700 bg-transparent hover:bg-slate-800",
        ghost: "hover:bg-slate-800",
        link: "underline-offset-4 hover:underline text-champagne",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-8 px-3 text-sm",
        lg: "h-12 px-6 text-lg",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);

export interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  loading?: boolean;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, loading, children, ...props }, ref) => {
    return (
      <button
        ref={ref}
        className={cn(buttonVariants({ variant, size }), className)}
        disabled={props.disabled || loading}
        {...props}
      >
        {loading ? (
          <>
            <span className="mr-2 h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent" />
            {children}
          </>
        ) : (
          children
        )}
      </button>
    );
  }
);

Button.displayName = "Button";
```

### 3.2 Section Component Pattern

```tsx
// src/components/sections/Hero.tsx
"use client";

import { motion } from "framer-motion";
import { useReducedMotion } from "@/lib/hooks/useReducedMotion";
import { Button } from "@/components/ui/Button";

export function Hero() {
  const prefersReducedMotion = useReducedMotion();

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Background Animation */}
      <motion.div
        initial={prefersReducedMotion ? {} : { opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 1, ease: "easeOut" }}
        className="absolute inset-0 aurora-gradient opacity-20"
      />
      
      {/* Content */}
      <div className="relative z-10 container mx-auto px-4 text-center">
        <motion.h1
          initial={prefersReducedMotion ? {} : { opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.2 }}
          className="text-5xl md:text-7xl lg:text-8xl font-serif text-white mb-6"
        >
          Beyond First Class
        </motion.h1>
        
        <motion.p
          initial={prefersReducedMotion ? {} : { opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
          className="text-xl text-slate-400 max-w-2xl mx-auto mb-8"
        >
          Curated journeys for the world's most discerning travelers
        </motion.p>
        
        <motion.div
          initial={prefersReducedMotion ? {} : { opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.6 }}
        >
          <Button size="lg">Begin Your Journey</Button>
        </motion.div>
      </div>
    </section>
  );
}
```

### 3.3 Form Component Pattern

```tsx
// src/components/ui/Input.tsx
import { forwardRef, type InputHTMLAttributes } from "react";
import { cn } from "@/lib/utils";

export interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, label, error, ...props }, ref) => {
    return (
      <div className="space-y-2">
        {label && (
          <label className="text-sm font-medium text-slate-300">
            {label}
            {props.required && <span className="text-aurora-magenta ml-1">*</span>}
          </label>
        )}
        <input
          ref={ref}
          className={cn(
            "flex h-10 w-full rounded-lg border border-slate-700 bg-slate-900/50 px-3 py-2 text-sm text-white placeholder:text-slate-500 focus:outline-none focus:ring-2 focus:ring-champagne focus:border-transparent disabled:cursor-not-allowed disabled:opacity-50 transition-colors",
            error && "border-aurora-magenta focus:ring-aurora-magenta",
            className
          )}
          {...props}
        />
        {error && (
          <p className="text-sm text-aurora-magenta">{error}</p>
        )}
      </div>
    );
  }
);

Input.displayName = "Input";
```

### 3.4 useReducedMotion Hook (Required)

```tsx
// src/lib/hooks/useReducedMotion.ts
import { useState, useEffect } from "react";

export function useReducedMotion(): boolean {
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(false);

  useEffect(() => {
    const mediaQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
    setPrefersReducedMotion(mediaQuery.matches);

    const handler = (event: MediaQueryListEvent) => {
      setPrefersReducedMotion(event.matches);
    };

    mediaQuery.addEventListener("change", handler);
    return () => mediaQuery.removeEventListener("change", handler);
  }, []);

  return prefersReducedMotion;
}
```

---

## 4. Avant-Garde Design Principles

### 4.1 Anti-Generic Philosophy

Every interface must have a **distinctive conceptual direction**. Reject:
- Bootstrap-style predictable grids
- Safe "Inter/Roboto" pairings without typographical hierarchy
- Purple-gradient-on-white clichés
- Predictable card grids and hero sections
- The homogenized "AI slop" aesthetic

### 4.2 Design Thinking Framework

Before coding, commit to a **BOLD aesthetic direction**:

| Direction | Characteristics |
|-----------|-----------------|
| **Brutally Minimal** | Extreme whitespace, single focal point |
| **Maximalist Chaos** | Layered textures, bold typography |
| **Retro-Futuristic** | Neon, chrome, geometric patterns |
| **Organic/Natural** | Soft curves, earthy tones, fluid shapes |
| **Luxury/Refined** | Serif fonts, gold accents, subtle gradients |
| **Editorial/Magazine** | Asymmetric layouts, bold headlines |
| **Brutalist/Raw** | Exposed structure, monospace, high contrast |
| **Art Deco/Geometric** | Symmetry, gold/black, stepped forms |

### 4.3 Intentional Minimalism

- **Whitespace is structural**, not just empty space
- **Every element earns its place** through calculated purpose
- If you cannot justify an element's existence, delete it
- **Typography hierarchy** speaks louder than decoration

### 4.4 Multi-Dimensional Analysis

Analyze every design decision through:
1. **Psychological**: User sentiment and cognitive load
2. **Technical**: Rendering performance, repaint/reflow costs
3. **Accessibility**: WCAG AAA strictness
4. **Scalability**: Long-term maintenance and modularity

### 4.5 Animation Guidelines

```typescript
// Timing
const ANIMATION_DURATION = {
  instant: 0,      // State changes
  fast: 150,       // Micro-interactions
  normal: 300,     // Standard transitions
  slow: 500,       // Page transitions
  dramatic: 800,   // Hero animations
};

// Easing
const EASING = {
  entrance: [0.0, 0.0, 0.2, 1],  // Decelerate
  exit: [0.4, 0.0, 1.0, 1.0],    // Accelerate
  standard: [0.4, 0.0, 0.2, 1],  // Symmetric
};

// Stagger
const STAGGER_DELAY = 50; // ms between items
```

---

## 5. Code Review Protocol

### 5.1 Pre-Review Checklist

Before any code review or completion claim:

```bash
# TypeScript Check
npx tsc --noEmit

# Lint
npm run lint

# Tests
npm test

# Build
npm run build
```

### 5.2 Review Categories

#### Critical (Must Fix)
- [ ] No `any` types - use `unknown` instead
- [ ] Proper error handling with user feedback
- [ ] Accessibility: focus states, ARIA labels, keyboard navigation
- [ ] `useReducedMotion` check for all animations
- [ ] No memory leaks in useEffect (proper cleanup)
- [ ] Form validation with Zod schemas
- [ ] XSS prevention (no `dangerouslySetInnerHTML` without sanitization)

#### High Priority
- [ ] TypeScript strict mode compliance
- [ ] Prefer `interface` over `type` (except unions/intersections)
- [ ] Early returns, avoid nested conditionals
- [ ] Loading states for async operations
- [ ] Error boundaries for component trees
- [ ] Proper React key usage in lists

#### Medium Priority
- [ ] Component composition over inheritance
- [ ] Memoization for expensive computations
- [ ] Image optimization with next/image
- [ ] Proper semantic HTML

### 5.3 Code Review Response Pattern

```
READ → UNDERSTAND → VERIFY → EVALUATE → RESPOND → IMPLEMENT
```

**Rules:**
- No performative agreement ("You're absolutely right!")
- Verify technically before implementing
- If unclear: STOP and ask for clarification
- YAGNI check: grep for usage before adding "proper" features

---

## 6. Security Audit Protocol

### 6.1 OWASP Top 10 2025 Checklist

| Category | Checks |
|----------|--------|
| **A01 Broken Access Control** | IDOR prevention, proper auth checks, SSRF protection |
| **A02 Security Misconfiguration** | Secure headers, no default credentials, error handling |
| **A03 Supply Chain** | Audit dependencies (`npm audit`), lock file integrity |
| **A04 Cryptographic Failures** | bcrypt for passwords, jose for JWT, no hardcoded secrets |
| **A05 Injection** | No SQL injection (use Prisma/ORM), no XSS |
| **A06 Insecure Design** | Input validation, business logic flaws |
| **A07 Authentication Failures** | Session management, MFA, secure cookies |
| **A08 Integrity Failures** | Code signing, dependency verification |
| **A09 Logging & Monitoring** | Security event logging, failed auth attempts |
| **A10 Exceptional Conditions** | Fail-closed, proper error handling |

### 6.2 High-Risk Patterns to Flag

```typescript
// ❌ String concatenation in queries
const query = "SELECT * FROM users WHERE id = " + userId;

// ❌ Dynamic code execution
eval(userInput);
new Function(userInput);

// ❌ Unsafe deserialization
JSON.parse(untrustedData); // Without validation

// ❌ Path traversal
fs.readFile(`./uploads/${userInput}`);

// ❌ Disabled security
fetch(url, { verify: false }); // SSL verification disabled
```

### 6.3 Secret Detection Patterns

| Type | Indicators |
|------|------------|
| API Keys | `api_key`, `apikey`, high entropy strings |
| Tokens | `token`, `bearer`, `jwt` |
| Credentials | `password`, `secret`, `key` |
| Cloud | `AWS_`, `AZURE_`, `GCP_` prefixes |

### 6.4 Next.js Specific Security

```typescript
// next.config.ts
const nextConfig = {
  // Security headers
  async headers() {
    return [
      {
        source: "/(.*)",
        headers: [
          {
            key: "X-Frame-Options",
            value: "DENY",
          },
          {
            key: "X-Content-Type-Options",
            value: "nosniff",
          },
          {
            key: "Referrer-Policy",
            value: "strict-origin-when-cross-origin",
          },
        ],
      },
    ];
  },
  
  // Image optimization
  images: {
    formats: ["image/avif", "image/webp"],
    remotePatterns: [
      { protocol: "https", hostname: "images.unsplash.com" },
    ],
  },
};
```

---

## 7. Performance Optimization

### 7.1 Critical Rules (Do First)

1. **Eliminate Waterfalls**
   ```typescript
   // ❌ Sequential (slow)
   const user = await getUser();
   const posts = await getPosts(user.id);
   
   // ✅ Parallel (fast)
   const [user, posts] = await Promise.all([
     getUser(),
     getPosts(),
   ]);
   ```

2. **Bundle Size Optimization**
   ```typescript
   // ✅ Dynamic imports for large components
   const HeavyChart = dynamic(() => import("./HeavyChart"), {
     loading: () => <Skeleton />,
   });
   
   // ✅ Direct imports (avoid barrel files)
   import { Button } from "@/components/ui/Button";
   // NOT: import { Button } from "@/components/ui"; (index.ts)
   ```

3. **Server Components by Default**
   ```typescript
   // Server component (default) - no "use client"
   export async function ServerComponent() {
     const data = await fetchData(); // Fetches on server
     return <div>{data}</div>;
   }
   
   // Client component only when needed
   "use client";
   export function ClientComponent() {
     const [state, setState] = useState();
     return <div>{state}</div>;
   }
   ```

### 7.2 Image Optimization

```tsx
import Image from "next/image";

// ✅ Optimized images
<Image
  src="/hero.jpg"
  alt="Hero image"
  width={1200}
  height={600}
  priority // Above-fold images
  className="object-cover"
/>;

// ✅ Responsive images
<Image
  src="/photo.jpg"
  alt="Photo"
  fill
  sizes="(max-width: 768px) 100vw, 50vw"
  className="object-cover"
/>
```

### 7.3 Font Optimization

```tsx
// app/layout.tsx
import { Geist, Instrument_Serif } from "next/font/google";

const geist = Geist({
  subsets: ["latin"],
  variable: "--font-sans",
});

const instrumentSerif = Instrument_Serif({
  subsets: ["latin"],
  weight: "400",
  variable: "--font-serif",
});

export default function RootLayout({ children }) {
  return (
    <html className={`${geist.variable} ${instrumentSerif.variable}`}>
      <body>{children}</body>
    </html>
  );
}
```

---

## 8. Accessibility Requirements (WCAG AAA)

### 8.1 Mandatory Practices

```tsx
// ✅ Semantic HTML
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
  </ul>
</nav>

<main>
  <section aria-labelledby="features-heading">
    <h2 id="features-heading">Features</h2>
  </section>
</main>

// ✅ Focus management
<button className="focus-visible:ring-2 focus-visible:ring-champagne focus-visible:outline-none">
  Click me
</button>

// ✅ ARIA labels for icon buttons
<button aria-label="Close dialog">
  <XIcon />
</button>

// ✅ Form labels
<label htmlFor="email">Email</label>
<input id="email" type="email" aria-required="true" />

// ✅ Error announcements
<div role="alert" className="text-aurora-magenta">
  {errorMessage}
</div>
```

### 8.2 Color Contrast Requirements

| Element | Minimum Ratio |
|---------|---------------|
| Normal text | 4.5:1 |
| Large text (18pt+) | 3:1 |
| UI components | 3:1 |

Test with: [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

### 8.3 Reduced Motion Support

```tsx
"use client";

import { motion } from "framer-motion";
import { useReducedMotion } from "@/lib/hooks/useReducedMotion";

export function AnimatedCard() {
  const prefersReducedMotion = useReducedMotion();

  return (
    <motion.div
      initial={prefersReducedMotion ? {} : { opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      Content
    </motion.div>
  );
}
```

---

## 9. Mobile Navigation Patterns

### 9.1 Breakpoint Strategy

```tsx
// Desktop nav: visible at md and above
<nav className="hidden md:flex items-center gap-8">...</nav>

// Mobile trigger: hidden at md and above
<button className="md:hidden" aria-label="Open menu">Menu</button>
```

### 9.2 Mobile Navigation with Sheet

```tsx
"use client";

import * as React from "react";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/Sheet";

export function MobileNav() {
  const [open, setOpen] = React.useState(false);

  return (
    <Sheet open={open} onOpenChange={setOpen}>
      <SheetTrigger asChild>
        <Button variant="ghost" size="icon" className="md:hidden">
          <MenuIcon />
        </Button>
      </SheetTrigger>
      
      <SheetContent side="right" className="w-[300px]">
        <nav className="flex flex-col gap-4">
          <Link href="/" onClick={() => setOpen(false)}>Home</Link>
          <Link href="/about" onClick={() => setOpen(false)}>About</Link>
        </nav>
      </SheetContent>
    </Sheet>
  );
}
```

### 9.3 Common Mobile Nav Failures

| Class | Symptom | Fix |
|-------|---------|-----|
| **A** | No visible nav on mobile | Add mobile trigger + overlay |
| **B** | Hidden by opacity/visibility | Verify state toggling |
| **C** | Clipped by overflow | Use `position: fixed` |
| **D** | Behind another layer | Check z-index scale |
| **E** | Breakpoint mismatch | Verify viewport meta |
| **F** | JavaScript failure | Guard selectors, check console |
| **G** | Keyboard inaccessible | Use real `<button>` elements |
| **H** | Click-outside race | Exclude trigger from handler |

---

## 10. Verification Gates

### 10.1 Pre-Commit Checklist

```bash
# 1. Type Check
npx tsc --noEmit

# 2. Lint
npm run lint

# 3. Tests
npm test

# 4. Build
npm run build

# 5. Security Audit
npm audit
```

### 10.2 Pre-Deploy Checklist

- [ ] All tests passing
- [ ] Build successful (exit 0)
- [ ] No console errors
- [ ] Accessibility: keyboard navigation works
- [ ] Accessibility: screen reader compatible
- [ ] Performance: Lighthouse score > 90
- [ ] Security: No high/critical vulnerabilities
- [ ] Responsive: Tested on mobile, tablet, desktop
- [ ] Analytics: Error tracking configured

### 10.3 Design Quality Gate

Before marking any UI work complete:
- [ ] Distinctive aesthetic direction (not generic)
- [ ] Intentional whitespace usage
- [ ] Typography hierarchy is clear
- [ ] Animations respect `prefers-reduced-motion`
- [ ] Color contrast meets WCAG AAA
- [ ] Micro-interactions are satisfying (150-300ms)

---

## 11. Project-Specific Conventions

### 11.1 Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Components | PascalCase | `Hero.tsx`, `Button.tsx` |
| Hooks | camelCase with `use` | `useScrollSpy.ts` |
| Utils | camelCase | `cn.ts`, `formatCurrency.ts` |
| Constants | SCREAMING_SNAKE | `API_ENDPOINTS` |
| Types | PascalCase | `UserProfile`, `Destination` |
| Files | kebab-case | `concierge-form.tsx` |

### 11.2 Import Order

```tsx
// 1. React/Next
import { useState } from "react";
import Image from "next/image";

// 2. Third-party
import { motion } from "framer-motion";
import { z } from "zod";

// 3. Absolute imports (@/)
import { Button } from "@/components/ui/Button";
import { useReducedMotion } from "@/lib/hooks/useReducedMotion";

// 4. Relative imports
import { HeroAnimation } from "./HeroAnimation";
```

### 11.3 File Headers

```tsx
"use client"; // If using hooks/browser APIs

// Or for server components (default), no directive needed
```

---

## Related Skills

| Skill | When to Use |
|-------|-------------|
| [aesthetic](../.agents/skills/aesthetic/SKILL.md) | Deep design analysis, inspiration workflows |
| [code-review](../.agents/skills/code-review/SKILL.md) | Detailed review protocols, feedback handling |
| [vulnerability-scanner](../.agents/skills/vulnerability-scanner/SKILL.md) | Deep security analysis, threat modeling |
| [nextjs-react-expert](../.agents/skills/nextjs-react-expert/SKILL.md) | Advanced performance optimization |
| [web-design-guidelines](../.agents/skills/web-design-guidelines/SKILL.md) | Vercel Web Interface Guidelines compliance |
| [tailwind-patterns](../.agents/skills/tailwind-patterns/SKILL.md) | Tailwind CSS patterns and best practices |
| [ui-styling](../.agents/skills/ui-styling/SKILL.md) | shadcn/ui implementation guidance |

---

> **Remember**: Technical excellence requires both rigorous implementation and distinctive design. Every line of code and every pixel should demonstrate intentionality and craftsmanship worthy of a luxury experience.
