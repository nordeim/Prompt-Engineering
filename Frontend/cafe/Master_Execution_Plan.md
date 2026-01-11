# Master Execution Plan (MEP)
## Merlion Brews — Phase-by-Phase Build Plan for an AI Coding Agent

**Purpose**: This document is a *deterministic*, *phase-gated* execution plan that an AI coding agent can follow to build the complete Merlion Brews codebase with minimal supervision. Each phase is independently executable and ends with objective validation gates. Each file includes:

- **Purpose** (why it exists)
- **Interfaces** (imports/exports, endpoints, env vars, DB tables)
- **Checklist** (must pass before moving forward)

**Scope lock (must not drift)**
- **Frontend**: Next.js 15 (App Router) + Tailwind CSS v4 + Shadcn primitives + Merlion wrapper components
- **Backend**: Laravel 12 (PHP 8.3+) from day 1
- **Database**: PostgreSQL 16 from day 1 (Redis 7 for cache/queues)
- **Payments**: Stripe PaymentIntents with **PayNow required**
- **Compliance**: GST 9% inclusive pricing + invoicing; **InvoiceNow in MVP via provider API**
- **Design authority**: `cafe.html` is the source of truth for tokens, CSS layers, and interaction behaviors
- **Browser floor**: Safari 16.4+, Chrome 111+, Firefox 128+ (Tailwind v4 constraint)

---

## 0. Agent Operating Rules

### 0.1 Global rules
- **Do not change scope**: If a missing requirement is discovered, append as a “Phase X+” enhancement, don’t rewrite prior phases.
- **One phase at a time**: Complete all file checklists for the current phase before starting the next phase.
- **No silent assumptions**: If an interface choice is ambiguous (e.g. Stripe Checkout vs PaymentIntents UI), pick the simplest compliant option and document it in an ADR file in-repo.
- **No “magic”**: Every external dependency must be represented as:
  - env vars
  - config files
  - documented setup steps
- **Validation is mandatory**: each phase defines validations (lint/build/tests) that must pass.

### 0.2 Directory conventions
The repository is a monorepo:
- `frontend/` — Next.js 15 storefront BFF
- `backend/` — Laravel 12 API
- `infra/` — local/dev infra (Docker Compose, scripts)
- `docs/` — ADRs and runbooks

---

## 1. Phase 1 — Monorepo Foundation + Local Dev Infrastructure

### 1.1 Outcome
A developer can run the full stack locally (Next.js + Laravel + Postgres + Redis) with consistent configuration and a single “happy path” command sequence.

### 1.2 Files to create

#### 0) `.gitignore`
 - **Purpose**: Prevent committing generated, secret, and OS-specific files across the monorepo.
 - **Interfaces**:
   - Covers `frontend/` (Next/Node), `backend/` (Laravel/PHP), `infra/` volumes, `.env` files.
 - **Checklist**:
   - Ignores `.env` files (but not `.env.example`)
   - Ignores `node_modules/`, `.next/`, `vendor/`, `storage/logs/`, `bootstrap/cache/`
   - Ignores IDE files (at minimum `.idea/`, `.vscode/`) and OS artifacts

#### 1) `README.md`
- **Purpose**: Single source for project setup/run instructions.
- **Interfaces**:
  - Commands for local dev
  - Links to `Project_Architecture_Document.md` and `docs/`
- **Checklist**:
  - Includes prerequisites (Node LTS, PHP 8.3, Composer, Docker)
  - Includes step-by-step: start infra, migrate DB, run backend, run frontend
  - Includes env var setup pointers for both apps

#### 2) `infra/docker-compose.yml`
- **Purpose**: Spin up Postgres 16 + Redis 7 for local development.
- **Interfaces**:
  - Exposes Postgres port, Redis port
  - Declares named volumes for persistence
- **Checklist**:
  - Postgres image pinned to major 16
  - Redis image pinned to major 7
  - Health checks enabled for Postgres and Redis
  - No hardcoded secrets (uses env or `.env`)

#### 3) `infra/.env.example`
- **Purpose**: Template env vars for local infra.
- **Interfaces**:
  - POSTGRES_DB / POSTGRES_USER / POSTGRES_PASSWORD
  - REDIS_PORT
- **Checklist**:
  - Contains safe placeholder values
  - Matches `docker-compose.yml`

#### 4) `docs/adr/ADR-0001-scope-lock.md`
- **Purpose**: Prevent scope drift; records the locked decisions.
- **Interfaces**: None (documentation)
- **Checklist**:
  - Lists the locked decisions in the “Scope lock” section above
  - Includes “Do not downgrade Tailwind v4” and “PayNow required”

#### 5) `docs/runbooks/local-development.md`
- **Purpose**: Operational runbook for local environment troubleshooting.
- **Interfaces**:
  - Common errors (ports, migrations, queue)
- **Checklist**:
  - Covers Postgres connectivity checks
  - Covers Redis connectivity checks
  - Covers “reset DB” instructions

### 1.3 Phase validations
- `docker compose up -d` brings up Postgres and Redis healthy
- README steps are executable end-to-end

---

## 2. Phase 2 — Backend Skeleton (Laravel 12) + Core Domain Model

### 2.1 Outcome
Laravel API runs locally, connects to Postgres, supports migrations, and exposes a versioned health endpoint.

### 2.2 Files to create (backend)

#### 0) `backend/` (Laravel scaffold via official tooling)
 - **Purpose**: Create a correct Laravel 12 baseline (framework files, artisan tooling, config defaults).
 - **Interfaces**:
   - Produces `artisan`, `bootstrap/`, `config/`, `public/`, `routes/`, `app/`, etc.
 - **Checklist**:
   - Generated using the official Laravel installer or `composer create-project`
   - `php artisan --version` reports Laravel 12.x
   - `php -v` is PHP 8.3+
   - `config/database.php` is configured (via `.env`) to use PostgreSQL

#### 1) `backend/composer.json`
- **Purpose**: Backend dependency manifest.
- **Interfaces**:
  - PHP >= 8.3
  - Laravel 12
- **Checklist**:
  - Uses Laravel 12
  - Includes required extensions (pdo_pgsql)

#### 2) `backend/.env.example`
- **Purpose**: Backend env template.
- **Interfaces**:
  - DB connection (pgsql)
  - Redis queue/cache
  - Stripe secret/webhook secret
  - InvoiceNow provider credentials
- **Checklist**:
  - No real secrets
  - Includes all required env keys referenced by code

#### 3) `backend/routes/api.php`
- **Purpose**: API routes.
- **Interfaces**:
  - `GET /api/v1/health`
- **Checklist**:
  - Health route returns JSON with version + timestamp
  - Versioned prefix used

#### 4) `backend/app/Http/Controllers/HealthController.php`
- **Purpose**: Health endpoint controller.
- **Interfaces**:
  - Returns JSON
- **Checklist**:
  - Does not query external services
  - Includes app version / git sha if available

#### 5) `backend/database/migrations/xxxx_xx_xx_create_core_tables.php`
- **Purpose**: Create foundational tables (users optional), products, inventory, orders, invoices.
- **Interfaces**:
  - Tables: `products`, `inventory`, `inventory_reservations`, `inventory_ledger`, `orders`, `order_items`, `payments`, `webhook_events`, `invoices`, `invoice_transmissions`
- **Checklist**:
  - All tables created with indexes on lookup keys
  - FK constraints where appropriate
  - Monetary amounts stored as integer cents
  - Ledger tables are append-only by design

#### 6) `backend/app/Models/*` (multiple)
Create at least:
- `Product`, `InventoryItem`, `InventoryReservation`, `InventoryLedgerEntry`, `Order`, `OrderItem`, `Payment`, `WebhookEvent`, `Invoice`, `InvoiceTransmission`
- **Purpose**: Eloquent models for core entities.
- **Interfaces**:
  - Relationships (Order → Items)
  - Attribute casting for JSON fields
- **Checklist**:
  - Model fillable/guarded set correctly
  - Relationships defined and named consistently
  - UUID primary keys (or clearly documented alternative)

### 2.3 Phase validations
- `php artisan migrate` succeeds against Postgres
- `GET /api/v1/health` returns 200

---

## 3. Phase 3 — Design Token Bridge + CSS Layers (Frontend Foundation)

### 3.1 Outcome
Next.js 15 app exists with Tailwind v4 configured in a way that preserves the `cafe.html` layer model and design tokens.

### 3.2 Files to create (frontend)

#### 0) `frontend/` (Next.js scaffold via official tooling)
 - **Purpose**: Create a correct Next.js 15 baseline with App Router.
 - **Interfaces**:
   - Produces `app/`, `next.config.*`, `package.json`, TypeScript config, etc.
 - **Checklist**:
   - Generated using an official Next.js scaffold (`create-next-app`)
   - Next.js is v15.x
   - App Router is enabled (`frontend/app/` exists)
   - `npm run build` succeeds before adding custom features

#### 1) `frontend/package.json`
- **Purpose**: Frontend dependencies.
- **Interfaces**:
  - Next.js 15
  - Tailwind CSS v4
  - Shadcn/Radix deps
- **Checklist**:
  - Includes Next 15
  - Includes Tailwind v4
  - Includes scripts: dev, build, start, lint

#### 2) `frontend/next.config.*`
- **Purpose**: Next config.
- **Interfaces**:
  - Enables App Router
- **Checklist**:
  - Minimal config; no experimental flags unless required

#### 3) `frontend/app/layout.tsx`
- **Purpose**: Root layout; sets fonts and global wrappers.
- **Interfaces**:
  - Imports global CSS
  - Defines metadata
- **Checklist**:
  - Includes `lang="en-SG"`
  - Includes skip link container

#### 4) `frontend/app/globals.css`
- **Purpose**: The authoritative place to implement the CSS layer strategy.
- **Interfaces**:
  - Uses Tailwind v4 `@import "tailwindcss";`
  - Defines `@layer tokens, base, components, utilities, overrides;` (project layers)
  - Defines `@theme { ... }` with token variables
- **Checklist**:
  - Includes tokens from `cafe.html`:
    - colors + rgb variants + ui variants
    - fonts
    - fluid type scale
    - spacing scale
    - durations + easing
    - shadows + z-index
  - Includes reduced motion and contrast media overrides
  - Includes `folio-frame` component styles as in `cafe.html`

#### 5) `frontend/design-tokens/index.ts`
- **Purpose**: Type-safe token mirror used by TS code (e.g. invoices PDF styling, Motion configs).
- **Interfaces**:
  - Exports `designTokens` object
- **Checklist**:
  - Token values match `globals.css` variables
  - Exports typed token keys for IDE safety

#### 6) `frontend/lib/cn.ts`
- **Purpose**: Utility to merge class names.
- **Interfaces**:
  - exports `cn(...classes)`
- **Checklist**:
  - Works with conditional classes

#### 7) `frontend/.env.example`
- **Purpose**: Frontend env template.
- **Interfaces**:
  - `NEXT_PUBLIC_API_BASE_URL` (Laravel base URL)
  - `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`
  - `STRIPE_SECRET_KEY` (server-only for BFF routes)
- **Checklist**:
  - No real secrets
  - Contains every env var referenced by `frontend/app/api/*`

### 3.3 Phase validations
- `npm run build` succeeds
- Visual check: basic page renders using token colors and fonts

---

## 4. Phase 4 — Merlion Component System (Shadcn Primitives + Wrappers)

### 4.1 Outcome
Reusable components replicate the “soul” of `cafe.html` without coupling the entire UI to raw HTML.

### 4.2 Files to create

#### 1) `frontend/components/ui/*` (shadcn primitives)
- **Purpose**: Base primitives.
- **Interfaces**:
  - Exported components used by wrappers
- **Checklist**:
  - Installed consistently via shadcn
  - No bespoke styling in primitives

#### 2) `frontend/components/merlion/button-merlion.tsx`
- **Purpose**: Implements `.btn`, `.btn-primary`, `.btn-secondary` behaviors.
- **Interfaces**:
  - Exports `ButtonMerlion`
  - Props: variant, asChild, etc.
- **Checklist**:
  - Hover underlay animation matches `cafe.html`
  - Focus-visible state is accessible

#### 3) `frontend/components/merlion/card-merlion.tsx`
- **Purpose**: Card wrapper with `folio-frame` support.
- **Interfaces**:
  - Exports `CardMerlion` with props `withFolioFrame?: boolean`
- **Checklist**:
  - `folio-frame` hover lift/shadow matches

#### 4) `frontend/components/merlion/ornament.tsx`
- **Purpose**: Peranakan corner ornaments as reusable component.
- **Interfaces**:
  - Props: position tl/tr/bl/br
- **Checklist**:
  - SVG path/circle details preserved
  - `aria-hidden` used properly

#### 5) `frontend/components/merlion/texture-overlay.tsx`
- **Purpose**: Global paper-fiber overlay.
- **Interfaces**:
  - Used in root layout
- **Checklist**:
  - `pointer-events: none` and correct z-index

#### 6) `frontend/components/merlion/zigzag.tsx`
- **Purpose**: Implements zig-zag editorial layout with RTL flip.
- **Interfaces**:
  - `ZigzagSection` + item props
- **Checklist**:
  - Even children flip using RTL technique

#### 7) `frontend/components/merlion/mobile-nav.tsx`
- **Purpose**: Mobile nav behavior from `cafe.html`.
- **Interfaces**:
  - Manages open state, `aria-expanded`, escape key, focus management
- **Checklist**:
  - Escape closes
  - Focus moves to first link on open
  - Restores focus to trigger on close

### 4.3 Phase validations
- Build passes
- Quick smoke: hero + nav + card + zigzag render without layout shift

---

## 5. Phase 5 — Storefront Pages (Content + Catalog)

### 5.1 Outcome
Pages mirror the structure and voice of `cafe.html` while pulling product data from Laravel.

### 5.2 Files to create

#### 1) `frontend/app/page.tsx`
- **Purpose**: Landing page.
- **Interfaces**:
  - Server Component; calls Laravel catalog endpoints
- **Checklist**:
  - Contains hero content and scroll indicator pattern
  - Uses Merlion wrappers (no raw `.btn` strings unless encapsulated)

#### 2) `frontend/app/api/catalog/route.ts`
- **Purpose**: BFF route handler that fetches catalog from Laravel.
- **Interfaces**:
  - `GET /api/catalog`
- **Checklist**:
  - Implements caching headers suitable for catalog
  - Handles Laravel failures gracefully

#### 3) `backend/routes/api.php` additions
- **Purpose**: Catalog endpoints.
- **Interfaces**:
  - `GET /api/v1/products`
  - `GET /api/v1/products/{slug}`
- **Checklist**:
  - Route names and controller bindings are versioned (`/api/v1/...`)
  - Responses are JSON-only (no HTML)
  - Response includes a stable field set required by UI: `slug`, `name`, `description`, `price_*` (GST-inclusive)

#### 4) `backend/app/Http/Controllers/ProductController.php`
- **Purpose**: Catalog endpoints implementation.
- **Interfaces**:
  - JSON responses
- **Checklist**:
  - Stable response schema
  - Includes fields required by UI (name, slug, description, price)

### 5.3 Phase validations
- Frontend renders products via Laravel
- No direct DB access from Next.js (always via Laravel)

---

## 6. Phase 6 — Cart + Inventory Reservation

### 6.1 Outcome
Add-to-cart creates/updates server-side reservations with TTL; oversell is prevented.

### 6.2 Files to create

#### 1) `backend/routes/api.php` additions
- **Purpose**: Expose inventory reservation endpoints for cart synchronization.
- **Interfaces**:
  - `POST /api/v1/reservations` (create)
  - `PATCH /api/v1/reservations/{id}` (update)
  - `DELETE /api/v1/reservations/{id}` (release)
- **Checklist**:
  - Routes are versioned (`/api/v1/...`)
  - `POST` returns `reservation_id` and `expires_at`
  - `DELETE` is idempotent (safe to call multiple times)

#### 2) `backend/app/Http/Controllers/ReservationController.php`
- **Purpose**: Reservation endpoints.
- **Interfaces**:
  - JSON responses
- **Checklist**:
  - Uses DB transactions
  - Prevents oversell with `stock_count - reserved_count >= qty`
  - Returns `expires_at`

#### 3) `backend/app/Services/InventoryService.php`
- **Purpose**: Encapsulates reservation and confirmation logic.
- **Interfaces**:
  - `reserve(items, ttl)`
  - `confirm(reservationId)`
  - `releaseExpired()`
- **Checklist**:
  - Ledger entries created for each reservation/confirm/release

#### 4) `frontend/lib/cart-store.ts`
- **Purpose**: Client state store (local) that syncs to reservations.
- **Interfaces**:
  - `addItem(sku, qty)`
  - `removeItem(sku)`
  - `syncReservation()`
- **Checklist**:
  - Stores `reservation_id` and `expires_at`
  - Handles expiry gracefully

#### 5) `frontend/app/api/reservations/route.ts`
- **Purpose**: BFF endpoints to call Laravel reservation endpoints.
- **Interfaces**:
  - `POST /api/reservations` (creates/updates reservation via Laravel)
- **Checklist**:
  - Validates payload
  - Returns normalized response for client
  - Does not expose Laravel internal errors verbatim (maps to safe error codes)

### 6.3 Phase validations
- Concurrency test: two users attempting last-item reserve: only one succeeds
- Expired reservations get released via scheduled job

---

## 7. Phase 7 — Checkout + Stripe PaymentIntents (PayNow required)

### 7.1 Outcome
Checkout creates an order draft, initiates Stripe payment with PayNow enabled, and completes via webhook.

### 7.2 Files to create

#### 1) `frontend/app/checkout/page.tsx`
- **Purpose**: Checkout UI.
- **Interfaces**:
  - Calls BFF to create order draft
  - Initiates Stripe payment
- **Checklist**:
  - Displays GST breakdown
  - Offers PayNow

#### 2) `frontend/app/api/checkout/route.ts`
- **Purpose**: BFF checkout orchestration.
- **Interfaces**:
  - `POST /api/checkout` (creates order draft via Laravel, creates Stripe PaymentIntent)
- **Checklist**:
  - Uses deterministic idempotency key per reservation/order
  - Stores Stripe IDs in Laravel via API

#### 3) `backend/routes/api.php` additions
- **Purpose**: Expose order draft creation and Stripe intent orchestration endpoints.
- **Interfaces**:
  - `POST /api/v1/orders/draft`
  - `POST /api/v1/payments/stripe/intent`
- **Checklist**:
  - Routes are versioned (`/api/v1/...`)
  - Draft creation is idempotent per `reservation_id`
  - Stripe intent endpoint requires server-side authentication/authorization strategy (even if “public MVP”, document the placeholder)

#### 4) `backend/app/Http/Controllers/OrderController.php`
- **Purpose**: Order draft creation.
- **Interfaces**:
  - JSON responses
- **Checklist**:
  - Stores cents amounts
  - Stores GST rate and breakdown

#### 5) `backend/app/Services/GstService.php`
- **Purpose**: GST calculation.
- **Interfaces**:
  - `calculate(subtotalCents): { subtotal_cents, gst_cents, total_cents, gst_rate }`
- **Checklist**:
  - Uses 9% rate
  - Rounds to nearest cent

#### 6) `backend/app/Http/Controllers/StripeWebhookController.php`
- **Purpose**: Stripe webhook receiver.
- **Interfaces**:
  - `POST /api/v1/webhooks/stripe`
- **Checklist**:
  - Verifies signature using raw request body
  - Idempotency using Stripe event id
  - On success: marks order paid, confirms reservation, creates invoice

#### 7) `backend/app/Services/StripeService.php`
- **Purpose**: Stripe API wrapper.
- **Interfaces**:
  - `createPaymentIntent(order, paymentMethodTypes)`
- **Checklist**:
  - Includes PayNow in payment methods
  - Sets metadata: `order_id`, `reservation_id`

### 7.3 Phase validations
- Test payment flow success via webhook
- Test webhook replay does not double-charge or double-decrement inventory

---

## 8. Phase 8 — Invoicing + InvoiceNow Provider Integration (MVP)

### 8.1 Outcome
Invoices are generated per paid order and transmitted to InvoiceNow via provider API with audit logging and retries.

### 8.2 Files to create

#### 1) `backend/app/Services/InvoiceNumberService.php`
- **Purpose**: Generate unique invoice numbers.
- **Interfaces**:
  - `generate(): string`
- **Checklist**:
  - Unique constraint in DB enforced

#### 2) `backend/app/Services/InvoiceService.php`
- **Purpose**: Build invoice payload.
- **Interfaces**:
  - `createInvoiceForOrder(orderId)`
  - Returns invoice entity
- **Checklist**:
  - Includes Business Registration `2015123456K`
  - Includes GST Registration `M9-1234567-8`
  - Includes GST breakdown

#### 3) `backend/app/Services/InvoiceNowProviderClient.php`
- **Purpose**: HTTP client wrapper for provider API.
- **Interfaces**:
  - `sendInvoice(invoicePayload): ProviderResponse`
- **Checklist**:
  - All credentials from env
  - Handles errors and returns structured error info

#### 4) `backend/app/Jobs/TransmitInvoiceNowJob.php`
- **Purpose**: Async transmission with retries.
- **Interfaces**:
  - Inputs: invoice_id
- **Checklist**:
  - Retries with backoff
  - Writes `invoice_transmissions` rows

#### 5) `backend/app/Console/Kernel.php` additions
- **Purpose**: Schedule reconciliation jobs.
- **Interfaces**:
  - Scheduled commands/jobs for invoice transmission retries and reservation cleanup
- **Checklist**:
  - Schedules “retry stuck transmissions”

### 8.3 Phase validations
- Paid order triggers invoice creation
- Transmission attempt logged
- Retry mechanism works on simulated failures

---

## 9. Phase 9 — Observability, Security Hardening, and Quality Gates

### 9.1 Outcome
The system is production-ready enough to deploy with monitoring hooks and clear runbooks.

### 9.2 Files to create

#### 1) `docs/runbooks/production-operations.md`
- **Purpose**: Incident and operational guidance.
- **Interfaces**:
  - Procedures covering:
    - Stripe webhook intake and idempotency failures
    - Inventory reservation expiry and reconciliation
    - InvoiceNow transmission retries and stuck states
- **Checklist**:
  - Covers webhook failures, invoice failures, reservation release

#### 2) `backend/app/Http/Middleware/RateLimitMiddleware.php` (or framework rate limiting config)
- **Purpose**: Rate limit checkout/webhooks.
- **Interfaces**:
  - Applied to endpoints:
    - `POST /api/v1/webhooks/stripe`
    - `POST /api/v1/orders/draft`
    - `POST /api/v1/reservations`
- **Checklist**:
  - Sensible defaults, documented

#### 3) `frontend/tests/visual/*` (Playwright)
- **Purpose**: Visual regression for design fidelity.
- **Interfaces**:
  - CI runnable via `npm run test:visual` (script must exist when implemented)
- **Checklist**:
  - Snapshot hero, folio-frame hover, ornaments, zigzag

#### 4) `backend/tests/Feature/*`
- **Purpose**: Feature tests for critical flows.
- **Interfaces**:
  - PHPUnit tests validating API endpoints and service behaviors
- **Checklist**:
  - Inventory oversell prevention
  - Webhook idempotency
  - GST correctness

### 9.3 Phase validations
- CI-style command set passes (lint + tests)

---

## 10. Phase 10 — Newsletter, Consent, and Transactional Messaging

### 10.1 Outcome
Newsletter signup is implemented end-to-end with explicit consent capture (PDPA-aligned), and the system can send transactional emails (order confirmation, invoice delivery) via a pluggable mail provider.

### 10.2 Files to create

#### 1) `backend/routes/api.php` additions
- **Purpose**: Expose newsletter subscription and consent endpoints.
- **Interfaces**:
  - `POST /api/v1/newsletter/subscribe`
- **Checklist**:
  - Payload includes `email` and `consent_marketing: true`
  - Stores consent timestamp and source

#### 2) `backend/app/Http/Controllers/NewsletterController.php`
- **Purpose**: Newsletter subscribe endpoint.
- **Interfaces**:
  - Request validation: `email`, `consent_marketing`
  - Response: `{ status }` and a stable message
- **Checklist**:
  - Rejects requests without explicit consent
  - Idempotent by email (multiple submits safe)

#### 3) `backend/database/migrations/xxxx_xx_xx_create_newsletter_tables.php`
- **Purpose**: Store subscribers and consent.
- **Interfaces**:
  - Tables: `newsletter_subscribers`
- **Checklist**:
  - Unique index on `email`
  - Stores `consent_granted_at`, `consent_source`, `unsubscribed_at`

#### 4) `backend/app/Services/MailService.php`
- **Purpose**: Central wrapper for sending email.
- **Interfaces**:
  - `send(to, template, data)`
- **Checklist**:
  - Uses Laravel mail configuration (no direct provider SDK calls in controllers)
  - Logs failures for reconciliation

#### 5) `frontend/components/merlion/newsletter-form.tsx`
- **Purpose**: Newsletter form matching `cafe.html` tone and hierarchy.
- **Interfaces**:
  - Calls `POST /api/newsletter/subscribe` (BFF)
- **Checklist**:
  - Includes explicit consent checkbox (unchecked by default)
  - Accessible labels and error states

#### 6) `frontend/app/api/newsletter/route.ts`
- **Purpose**: BFF route to call Laravel newsletter endpoint.
- **Interfaces**:
  - `POST /api/newsletter/subscribe`
- **Checklist**:
  - Validates payload server-side
  - Maps Laravel validation errors to safe client errors

### 10.3 Phase validations
- Newsletter signup succeeds with consent and fails without consent
- Transactional email sending works in dev (log driver / sandbox)

---

## 11. Phase 11 — Experiences & Events Booking (Tasting Room + Cultural Gatherings)

### 11.1 Outcome
Users can book experiences and reserve event spots (as implied by `cafe.html`), with capacity management and optional payment requirements.

### 11.2 Files to create

#### 1) `backend/database/migrations/xxxx_xx_xx_create_events_and_bookings.php`
- **Purpose**: Store events/experiences and reservations.
- **Interfaces**:
  - Tables: `experiences`, `events`, `event_sessions`, `bookings`
- **Checklist**:
  - Capacity fields and indexes
  - Booking state machine field (`status`: pending/confirmed/cancelled)

#### 2) `backend/app/Services/CapacityService.php`
- **Purpose**: Prevent overbooking.
- **Interfaces**:
  - `reserveSpot(sessionId, qty)`
  - `confirmBooking(bookingId)`
  - `cancelBooking(bookingId)`
- **Checklist**:
  - Uses transactions
  - Prevents oversell under concurrency

#### 3) `backend/routes/api.php` additions
- **Purpose**: Booking APIs.
- **Interfaces**:
  - `GET /api/v1/events`
  - `POST /api/v1/bookings`
  - `POST /api/v1/bookings/{id}/cancel`
- **Checklist**:
  - All endpoints versioned
  - Cancel is idempotent

#### 4) `frontend/app/events/page.tsx`
- **Purpose**: Events listing page.
- **Interfaces**:
  - Fetches events via BFF or direct server fetch to Laravel
- **Checklist**:
  - Uses Merlion components
  - Preserves `cafe.html` narrative hierarchy

#### 5) `frontend/app/api/bookings/route.ts`
- **Purpose**: BFF booking creation.
- **Interfaces**:
  - `POST /api/bookings`
- **Checklist**:
  - Validates payload
  - Provides user-friendly errors for sold-out sessions

### 11.3 Phase validations
- Two users racing for last seat: only one booking succeeds
- Book/cancel flows work end-to-end

---

## 12. Phase 12 — Admin Dashboard (Day‑1 Operations)

### 12.1 Outcome
Admin users can manage products, inventory adjustments, orders, invoices, bookings, and operational states (webhook/invoice transmission statuses).

### 12.2 Files to create

#### 1) `backend/database/migrations/xxxx_xx_xx_create_admin_roles.php`
- **Purpose**: Admin RBAC.
- **Interfaces**:
  - Tables for roles/permissions (implementation choice must be documented)
- **Checklist**:
  - Includes an initial `admin` role
  - Seed mechanism documented (seeders or artisan command)

#### 2) `backend/routes/api.php` additions
- **Purpose**: Admin endpoints.
- **Interfaces**:
  - `GET /api/v1/admin/orders`
  - `PATCH /api/v1/admin/inventory/{sku}`
  - `GET /api/v1/admin/invoices/{id}`
- **Checklist**:
  - Protected by auth middleware
  - Inventory adjustments always write to ledger

#### 3) `frontend/app/admin/layout.tsx`
- **Purpose**: Admin layout shell.
- **Interfaces**:
  - Uses shared tokens and Merlion wrapper styles
- **Checklist**:
  - Clear navigation
  - Accessible, responsive layout

#### 4) `frontend/app/admin/orders/page.tsx`
- **Purpose**: Admin order list.
- **Interfaces**:
  - Fetches `GET /api/v1/admin/orders`
- **Checklist**:
  - Shows paid/unpaid states and invoice transmission status

### 12.3 Phase validations
- Admin can adjust inventory and ledger is written
- Admin can view invoice transmission attempts

---

## 13. Phase 13 — CI, Deployment, and Environment Promotion

### 13.1 Outcome
The repository can be built and tested automatically, and deployed to production-like environments with clear promotion steps.

### 13.2 Files to create

#### 1) `docs/runbooks/deployment.md`
- **Purpose**: Deployment instructions.
- **Interfaces**:
  - Describes deployment targets for frontend and backend
- **Checklist**:
  - Includes environment variables list
  - Includes rollback strategy

#### 2) `infra/production/*` (provider-specific)
- **Purpose**: Deployment manifests.
- **Interfaces**:
  - Backend container build/run notes
  - Frontend deploy notes
- **Checklist**:
  - No secrets committed
  - Uses env-based configuration

### 13.3 Phase validations
- CI pipeline runs build + tests
- Deploy runbook is complete and reproducible

---

## 14. Global Interfaces Contract (must remain stable)

### 14.1 Backend API (minimum contract)
- `GET /api/v1/health`
- `GET /api/v1/products`
- `GET /api/v1/products/{slug}`
- `POST /api/v1/reservations`
- `PATCH /api/v1/reservations/{id}`
- `DELETE /api/v1/reservations/{id}`
- `POST /api/v1/orders/draft`
- `POST /api/v1/webhooks/stripe`

- `POST /api/v1/newsletter/subscribe`

- `GET /api/v1/events`
- `POST /api/v1/bookings`
- `POST /api/v1/bookings/{id}/cancel`

- `GET /api/v1/admin/orders`
- `PATCH /api/v1/admin/inventory/{sku}`
- `GET /api/v1/admin/invoices/{id}`

### 14.2 Frontend BFF routes (minimum contract)
- `GET /api/catalog`
- `POST /api/reservations`
- `POST /api/checkout`

- `POST /api/newsletter/subscribe`
- `POST /api/bookings`

---

## 15. Final Review Checklist for This MEP (self-validation)
The AI coding agent (or reviewer) must confirm:
- Every phase has:
  - Outcome
  - File list
  - Per-file purpose/interfaces/checklist
  - Phase validations
- Requirements are explicitly encoded:
  - Tailwind v4
  - Laravel/Postgres day 1
  - PayNow required
  - InvoiceNow via provider
  - `cafe.html` design authority
- No phase depends on undocumented prior work

---

## 16. Notes for Minimal-Supervision Execution
- If a phase introduces new env vars, **update `.env.example` files** in that same phase.
- If a response schema changes, create an ADR in `docs/adr/`.
- Keep the UI “soul” safe by ensuring `globals.css` and wrapper components match `cafe.html` before adding more product features.
