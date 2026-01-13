# Deep Analysis: Morning Brew Collective E-Commerce Platform
## Executive Summary
First conduct an exhaustive multi-dimensional analysis of the static HTML mock-up and the enterprise requirements. Below is my strategic assessment, followed by the comprehensive `MASTER_EXECUTION_PLAN.md`.

## Pre-Planning Analysis
1. Design Token Extraction from HTML Mock-up
```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  DESIGN SYSTEM AUDIT — "SUNRISE AT THE KOPITIAM"                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PALETTE HIERARCHY                                                          │
│  ─────────────────                                                          │
│  Primary Action    → Sunrise Coral #FF6B4A (CTAs, badges, highlights)       │
│  Secondary Warmth  → Golden Hour #FFBE4F (accents, underlines, borders)     │
│  Grounding Dark    → Espresso Dark #3D2317 (text, footer, modals)           │
│  Surface Light     → Latte Cream #FFF5E6 (backgrounds)                      │
│  Fresh Accent      → Mint Fresh #B8E6D4 (location section)                  │
│                                                                             │
│  TYPOGRAPHY PAIRING                                                         │
│  ─────────────────                                                          │
│  Display           → 'Righteous' (Google Fonts) - 1970s groovy aesthetic    │
│  Body              → 'Nunito' - Warm, readable, friendly                    │
│                                                                             │
│  SPATIAL SYSTEM                                                             │
│  ─────────────────                                                          │
│  Grid              → 8pt base unit (0.25rem increments)                     │
│  Container         → 1200px max-width                                       │
│  Radius            → Generous (16-48px) - "soft 70s" feel                   │
│                                                                             │
│  MOTION SIGNATURE                                                           │
│  ─────────────────                                                          │
│  Primary Easing    → cubic-bezier(0.34, 1.56, 0.64, 1) — "bounce"           │
│  Secondary Easing  → cubic-bezier(0.23, 1, 0.32, 1) — "smooth"              │
│  Duration Scale    → 150ms / 300ms / 500ms                                  │
│                                                                             │
│  DECORATIVE PATTERNS                                                        │
│  ─────────────────                                                          │
│  • Sunburst conic gradients (rotating background)                           │
│  • Wave section dividers (SVG paths)                                        │
│  • Scalloped edges                                                          │
│  • Tile patterns (kopitiam floor aesthetic)                                 │
│  • Coffee ring stain decorations                                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

2. Singapore Compliance Requirements Analysis
Requirement	Implementation Strategy	Complexity
9% GST Inclusive	All displayed prices include GST; breakdown shown at checkout. Store prices as cents (integer) to avoid float precision issues.	Medium
PayNow QR	Stripe Singapore supports PayNow. Generate QR codes via Stripe API with paynow payment method.	Medium
InvoiceNow (PEPPOL)	Integrate with IMDA-approved Access Point (e.g., InvoiceNow API). Generate UBL 2.1 compliant XML.	High
PDPA Consent	Explicit opt-in checkboxes, consent timestamps, withdrawal mechanism, data export capability.	Medium

3. Architecture Decision Records
```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  ADR-001: BFF ARCHITECTURE                                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  DECISION: Next.js handles UI orchestration; Laravel owns domain logic      │
│                                                                             │
│  RATIONALE:                                                                 │
│  • Next.js Server Components reduce client bundle, improve SEO              │
│  • Laravel's Eloquent ORM provides robust relational data handling          │
│  • Redis enables inventory reservation locks (atomic operations)            │
│  • Clear separation: Frontend = Experience, Backend = Truth                 │
│                                                                             │
│  DATA FLOW:                                                                 │
│                                                                             │
│   Browser ─────► Next.js (App Router) ─────► Laravel API ─────► PostgreSQL  │
│      │               │                            │                         │
│      │               │ Server Components          │ Domain Logic            │
│      │               │ Route Handlers             │ Validation              │
│      │               │ Edge Middleware            │ Business Rules          │
│      │               ▼                            ▼                         │
│      └────────── React RSC ◄───────────── JSON API Responses               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  ADR-002: TWO-PHASE INVENTORY RESERVATION                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PROBLEM: Prevent overselling while allowing cart abandonment               │
│                                                                             │
│  SOLUTION:                                                                  │
│                                                                             │
│  PHASE 1: SOFT RESERVE (Add to Cart)                                        │
│  ┌─────────────────────────────────────────────────────────────────┐        │
│  │  • Decrement `available_quantity` in Redis (atomic DECRBY)      │        │
│  │  • Set TTL on reservation (15 minutes default)                  │        │
│  │  • Store reservation_id in cart session                         │        │
│  │  • On TTL expiry: Redis keyspace notification → restore stock   │        │
│  └─────────────────────────────────────────────────────────────────┘        │
│                                                                             │
│  PHASE 2: HARD COMMIT (Checkout Success)                                    │
│  ┌─────────────────────────────────────────────────────────────────┐        │
│  │  • Decrement `stock_quantity` in PostgreSQL (transaction)       │        │
│  │  • Delete Redis reservation key                                 │        │
│  │  • Create order record with line items                          │        │
│  │  • Trigger InvoiceNow generation (async job)                    │        │
│  └─────────────────────────────────────────────────────────────────┘        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

4. Risk Assessment
Risk	Impact	Probability	Mitigation
Design drift from mock-up	High	Medium	Design tokens as single source; automated visual regression tests
GST calculation errors	Critical	Low	Decimal128 for currency; unit tests for edge cases; audit logging
Inventory race conditions	High	Medium	Redis atomic operations; database row-level locking
InvoiceNow API unavailability	Medium	Low	Queue-based retry with exponential backoff; manual fallback
PDPA non-compliance	Critical	Low	Consent audit trail; data retention policies; encryption at rest

---

# File: MASTER_EXECUTION_PLAN.md
# Morning Brew Collective — Enterprise E-Commerce Platform
# Version: 1.0.0 | Last Updated: 2024

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## TABLE OF CONTENTS

1. [Project Overview](#1-project-overview)
2. [Architecture Blueprint](#2-architecture-blueprint)
3. [Phase 0: Environment Foundation](#phase-0-environment-foundation)
4. [Phase 1: Frontend Scaffold](#phase-1-frontend-scaffold)
5. [Phase 2: Design System Implementation](#phase-2-design-system-implementation)
6. [Phase 3: Backend Foundation](#phase-3-backend-foundation)
7. [Phase 4: Product Catalog Domain](#phase-4-product-catalog-domain)
8. [Phase 5: Cart & Inventory Reservation](#phase-5-cart--inventory-reservation)
9. [Phase 6: Authentication & User Management](#phase-6-authentication--user-management)
10. [Phase 7: Checkout & Payment Processing](#phase-7-checkout--payment-processing)
11. [Phase 8: Order Fulfillment & Notifications](#phase-8-order-fulfillment--notifications)
12. [Phase 9: Singapore Compliance Layer](#phase-9-singapore-compliance-layer)
13. [Phase 10: Admin Dashboard](#phase-10-admin-dashboard)
14. [Phase 11: Testing & Quality Assurance](#phase-11-testing--quality-assurance)
15. [Phase 12: Deployment & DevOps](#phase-12-deployment--devops)
16. [Appendix A: Database Schema](#appendix-a-database-schema)
17. [Appendix B: API Contracts](#appendix-b-api-contracts)
18. [Appendix C: Design Tokens Reference](#appendix-c-design-tokens-reference)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 1. PROJECT OVERVIEW

### 1.1 Mission Statement

Transform the Morning Brew Collective static HTML mock-up into a Singapore-first, 
design-led headless commerce platform that preserves the authentic 1970s kopitiam 
aesthetic while delivering enterprise-grade transactional integrity and strict 
local compliance (GST, InvoiceNow, PayNow, PDPA).

### 1.2 Success Criteria
```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ FUNCTIONAL REQUIREMENTS │
├─────────────────────────────────────────────────────────────────────────────┤
│ □ Product browsing with category filtering │
│ □ Shopping cart with real-time inventory reservation │
│ □ User authentication (email/password + social) │
│ □ Checkout flow with Stripe + PayNow QR support │
│ □ Order tracking and history │
│ □ Newsletter subscription with PDPA consent │
│ □ Store locator with operating hours │
│ □ Admin dashboard for inventory/order management │
│ □ InvoiceNow compliant e-invoice generation │
│ □ 9% GST inclusive pricing with breakdown at checkout │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ NON-FUNCTIONAL REQUIREMENTS │
├─────────────────────────────────────────────────────────────────────────────┤
│ □ Lighthouse Performance Score: ≥90 │
│ □ WCAG 2.1 AA Accessibility Compliance │
│ □ First Contentful Paint: <1.5s │
│ □ Time to Interactive: <3.5s │
│ □ 99.9% uptime SLA readiness │
│ □ Mobile-first responsive design │
│ □ SEO optimization with structured data │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Technology Stack (Locked)
```text
| Layer | Technology | Version | Notes |
|-------|------------|---------|-------|
| Frontend Runtime | Next.js | 15.x | App Router, React Server Components |
| Frontend Styling | Tailwind CSS | 4.x | CSS-first config via `@theme` |
| UI Components | Shadcn/UI | Latest | Radix primitives, custom styled |
| Backend Framework | Laravel | 12.x | PHP 8.3+ |
| Database | PostgreSQL | 16.x | Primary data store |
| Cache/Queue | Redis | 7.x | Sessions, inventory locks, queues |
| Payment Gateway | Stripe | Latest | PayNow support enabled |
| Email | Laravel Mail | - | With queue workers |
| File Storage | S3-compatible | - | Product images |
```

### 1.4 Repository Structure
```text
morning-brew-collective/
├── frontend/ # Next.js 15 Application
│ ├── src/
│ │ ├── app/ # App Router pages
│ │ ├── components/ # React components
│ │ │ ├── ui/ # Shadcn UI primitives
│ │ │ ├── layout/ # Layout components
│ │ │ ├── features/ # Feature-specific components
│ │ │ └── patterns/ # Decorative patterns (from mock-up)
│ │ ├── lib/ # Utilities, API clients
│ │ ├── hooks/ # Custom React hooks
│ │ ├── stores/ # Zustand state stores
│ │ ├── styles/ # Global CSS, Tailwind config
│ │ └── types/ # TypeScript definitions
│ ├── public/ # Static assets
│ ├── tailwind.config.ts
│ ├── next.config.ts
│ └── package.json
│
├── backend/ # Laravel 12 Application
│ ├── app/
│ │ ├── Http/
│ │ │ ├── Controllers/ # API controllers
│ │ │ ├── Middleware/ # Custom middleware
│ │ │ ├── Requests/ # Form requests (validation)
│ │ │ └── Resources/ # API resources (transformers)
│ │ ├── Models/ # Eloquent models
│ │ ├── Services/ # Business logic services
│ │ ├── Jobs/ # Queue jobs
│ │ ├── Events/ # Domain events
│ │ ├── Listeners/ # Event listeners
│ │ ├── Policies/ # Authorization policies
│ │ └── Enums/ # PHP enums
│ ├── database/
│ │ ├── migrations/ # Schema migrations
│ │ ├── seeders/ # Data seeders
│ │ └── factories/ # Model factories
│ ├── routes/
│ │ ├── api.php # API routes
│ │ └── channels.php # Broadcast channels
│ ├── config/
│ ├── tests/
│ └── composer.json
│
├── infra/ # Infrastructure
│ ├── docker/
│ │ ├── frontend.Dockerfile
│ │ ├── backend.Dockerfile
│ │ └── nginx.conf
│ ├── docker-compose.yml # Local development
│ ├── docker-compose.prod.yml # Production
│ └── scripts/
│ ├── setup.sh
│ └── seed.sh
│
├── docs/ # Documentation
│ ├── API.md
│ ├── DESIGN_SYSTEM.md
│ └── DEPLOYMENT.md
│
├── .github/
│ └── workflows/ # CI/CD pipelines
│
└── README.md
```


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 2. ARCHITECTURE BLUEPRINT

### 2.1 System Context Diagram
```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ │
│ EXTERNAL SYSTEMS │
│ │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│ │ Stripe │ │ PayNow │ │InvoiceNow│ │ Google │ │
│ │ Payments │ │ QR │ │ (PEPPOL)│ │ OAuth │ │
│ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ │
│ │ │ │ │ │
│ └───────────────┴───────┬───────┴───────────────┘ │
│ │ │
│ ▼ │
│ ┌─────────────────────────────────────────────────────────────────────┐ │
│ │ MORNING BREW PLATFORM │ │
│ │ │ │
│ │ ┌─────────────────┐ ┌─────────────────┐ │ │
│ │ │ FRONTEND │ REST │ BACKEND │ │ │
│ │ │ Next.js 15 │◄────────►│ Laravel 12 │ │
```
