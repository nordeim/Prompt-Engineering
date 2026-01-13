Awesome understanding! Now, please think deeper and think harder to deeply and thoroughly explore systematically and meticulously how best to re-imagine the complete codebase for a Singapore based small-to-medium cafe shop business, using the following static HTML mock-up as the e-commerce website's landing page design, meaning keep as much UI/UX aesthetic design and style as possible while turning the website into a "full function" enterprise-grade production ready e-commerce platform serving both online and offline customers. Next, meticulously plan and then create a comprehensive `MASTER_EXECUTION_PLAN.md` for an coding Agent to use as single source of truth guide to successfully build the complete codebase with minimal error and minimal supervision, break the master plan into logical phases that can be executed independently, and for each phase, specify the list of files to create, and describe a list of features and interfaces for each file together with a checklist for the file.

# Codebase Requirements:
Singapore-first, design-led headless commerce platform. It fuses the aesthetic of the static HTML mock-up with enterprise-grade transactional integrity and strict local compliance (GST, InvoiceNow, PayNow).

The system is architected as a **Backend-for-Frontend (BFF)** hybrid:
- **Frontend**: Next.js 15 (App Router) handles the "soul" (UX, animations, design tokens) and orchestrates user flows.
- **Backend**: Laravel 12 acts as the domain authority, handling inventory, orders, compliance, and invoicing.

## Architecture & Technology Stack

**Frontend (`/frontend`)**
- **Framework**: Next.js 15 (App Router)
- **Styling**: Tailwind CSS v4 (CSS-first config via `@theme`)
- **Components**: Shadcn UI primitives wrapped in custom components to enforce the design system.
- **Design Source**: Attached static HTML mock-up is the authoritative source for tokens, CSS layers, and interaction behaviors.

**Backend (`/backend`)**
- **Framework**: Laravel 12 (PHP 8.3+)
- **Database**: PostgreSQL 16
- **Cache/Queue**: Redis 7
- **Key Services**: Inventory (Two-Phase Reservation), Orders (GST Logic), Invoicing (InvoiceNow via Provider API), Newsletter (PDPA Consent).

**Infrastructure (`/infra`)**
- Docker Compose for local development (Postgres + Redis).
- Production Dockerfiles for CI/CD.

## Development Constraints

These decisions are **architecturally locked** and must not be drifted from:
1.  **Design Authority**: Attached static HTML mock-up is the source of truth.
2.  **Compliance**: 9% GST inclusive pricing, PayNow support via Stripe, and InvoiceNow readiness are mandatory MVP features.
3.  **Stack**: Laravel/Postgres from Day 1 (no serverless backend functions for domain logic).
4.  **Browser Support**: Modern browsers only (Safari 16.4+, Chrome 111+) to support Tailwind v4 native cascade layers.

## Environment Prerequisites
- Node.js v22 LTS
- PHP 8.3+ & Composer
- Docker Desktop / Compose
