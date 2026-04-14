# 1. Restating the Goal Clearly

We are building a **dynamic e-commerce website** for a premium tea brand ("Cha Yuan") that blends Eastern tea heritage with a modern lifestyle aesthetic. The frontend will be built with **Next.js 16 (App Router), React 19, TypeScript 5.9, Tailwind CSS v4, Framer Motion 12, Radix UI / Shadcn UI components, Zod 4, and a BFF pattern for API communication**. The backend will be **Django 6 + PostgreSQL 17**, with Redis for caching. The site must deliver an **elegant, traditional, culturally rich, and lifestyle-oriented experience**, featuring:

- **Hero section** with brand philosophy and tea garden imagery
- **Product lines** organized by origin, fermentation level, and season
- **Tea culture** content (brewing methods, tasting guides, history)
- **Subscription service** (monthly curated tea box)
- **Purchase entry** (online store link / e-commerce integration)

The provided static HTML template serves as a **visual and interaction reference**—it demonstrates the desired design language, animations, and component structure. Our task is to transform this static mockup into a **production-ready, maintainable, and scalable Next.js application** with a proper backend integration strategy.

---

# 2. Possible Approaches

Given the tech stack and requirements, I see **four architectural approaches** varying in complexity and flexibility:

## Approach A: Static Site + Client-Side E-Commerce Embed
- **Frontend**: Next.js static generation (`next build && next export`) with client-side data fetching from an external e-commerce platform (e.g., Shopify Storefront API).
- **Backend**: None (or minimal) – use Shopify/Liquid for product management, checkout, subscriptions.
- **Pros**: Fastest to market, minimal backend maintenance, leverages existing e-commerce infrastructure.
- **Cons**: Limited customization of checkout flow, subscription logic tied to third-party, less control over data models, potential vendor lock-in.

## Approach B: Headless CMS + Next.js (Content-Driven)
- **Frontend**: Next.js with Incremental Static Regeneration (ISR) fetching content from a headless CMS (e.g., Sanity, Contentful, Strapi).
- **Backend**: Headless CMS for products, blog, culture content; external e-commerce for cart/checkout (or custom Django).
- **Pros**: Excellent content editing experience for non-technical users, fast performance, separates content from commerce.
- **Cons**: Adds another service to manage and pay for, integration overhead between CMS and e-commerce.

## Approach C: Custom Django Backend + Next.js BFF (Full-Stack Custom)
- **Frontend**: Next.js with BFF proxy pattern (as detailed in `tech-stack_considerations.md`), Server Components for initial data, TanStack Query for client-side caching.
- **Backend**: Django 6 + Django Ninja (REST or GraphQL) with PostgreSQL 17, Redis caching, custom product management, subscription logic, and authentication.
- **Pros**: Maximum control over data models, business logic, and user experience; single source of truth; ideal for unique subscription workflows; fits perfectly with provided tech-stack considerations.
- **Cons**: Higher development effort, requires building admin interface (or using Django Admin), more moving parts to maintain.

## Approach D: Hybrid – Django Backend + Next.js with Embedded E-Commerce
- **Frontend**: Next.js BFF for content and user profiles, but **product catalog and checkout** delegated to a service like **Shopify** or **Stripe Checkout**.
- **Backend**: Django manages **tea culture content, user accounts, subscription preferences, and order history**; product sync via webhooks or periodic import.
- **Pros**: Best of both worlds: custom content/culture experience with proven e-commerce checkout, reduced PCI compliance scope.
- **Cons**: Complex synchronization between systems, potential data inconsistency.

---

# 3. Trade-Off Comparison

| Criteria | Approach A (Static+External) | Approach B (Headless CMS) | Approach C (Custom Django) | Approach D (Hybrid) |
|----------|------------------------------|---------------------------|----------------------------|---------------------|
| **Development Speed** | ⚡ Fastest (weeks) | 🏃 Moderate (1-2 months) | 🐢 Slowest (2-3 months) | 🏃 Moderate |
| **Customization Flexibility** | 🔴 Low (limited by platform) | 🟡 Medium (content flexible, commerce fixed) | 🟢 High (full control) | 🟡 Medium-High |
| **Long-Term Maintainability** | 🟡 Medium (vendor lock-in) | 🟢 Good (decoupled) | 🟢 Excellent (tailored) | 🟡 Medium (integration points) |
| **Subscription Complexity** | 🔴 Limited (recurring app) | 🟡 Depends on commerce provider | 🟢 Full custom workflows | 🟢 Can use Stripe Billing |
| **Content Team Empowerment** | 🔴 Poor (dev needed) | 🟢 Excellent (CMS UI) | 🟡 Django Admin (good) | 🟡 Django Admin |
| **Performance (Core Web Vitals)** | 🟢 Excellent (static) | 🟢 Excellent (ISR) | 🟢 Excellent (SSR/RSC) | 🟢 Excellent |
| **Alignment with Tech-Stack Doc** | 🔴 Contradicts BFF/JWT guidance | 🟡 Partial | 🟢 **Full alignment** | 🟡 Partial |

---

# 4. Recommended Best Default Path: **Approach C – Custom Django + Next.js BFF**

**Why this is the strongest choice given the context:**

1. **Tech-Stack Harmony**: The provided `tech-stack_considerations.md` is explicitly written for a **Next.js 16 + Django 6** stack. It details friction points (React 19 `forwardRef`, Tailwind v4, JWT handling via BFF) that are **directly addressed by a custom integration**. Using a third-party e-commerce platform would render much of that guidance irrelevant.

2. **Unique Brand Experience**: A premium tea brand with a focus on **culture, storytelling, and curated subscriptions** benefits from a bespoke backend. The subscription model ("Discovery Box", "Connoisseur Box") can be fully tailored with custom logic (e.g., seasonal selection algorithms, member-only content) that would be constrained by off-the-shelf subscription apps.

3. **Data Ownership & Future Flexibility**: Tea inventory, origin stories, brewing parameters, and customer preferences are **core intellectual property**. Owning the data model allows for future features like personalized recommendations based on tasting history, tea journaling, or community features.

4. **BFF Pattern Justification**: The BFF proxy pattern outlined in the document is designed specifically for **secure JWT handling with an external backend**—exactly our Django API. This ensures tokens are stored in `HttpOnly` cookies and requests are proxied securely.

5. **Django 6 Advantages**: The latest Django LTS brings async views, native task queue, and excellent ORM performance with PostgreSQL 17. Django Admin provides a **free, customizable admin panel** for managing products, orders, and content, reducing the need for a separate CMS initially.

**Potential Concern Mitigated**: Development speed may be slower, but we can **prioritize an MVP** that includes the essential pages (product listing, product detail, subscription sign-up) and use **Django Admin** for content management. We can **defer complex e-commerce features** (cart, checkout) to a later phase if needed, initially linking to an external store link as per the "Purchase Entry" requirement.

---

# 5. Short Execution Plan (Phased)

### Phase 1: Project Setup & Core Infrastructure (Week 1)
- Initialize Next.js 16 project with TypeScript, Tailwind v4, Shadcn UI (React 19 compatible).
- Set up Django 6 project with Django Ninja, PostgreSQL 17, Redis.
- Configure **BFF proxy route** (`/api/proxy/[...path]`) in Next.js for secure API communication.
- Implement **JWT authentication** with `HttpOnly` cookies (using `django-simple-jwt` or custom).
- Create basic Django models: `TeaProduct`, `TeaCategory`, `Origin`, `SubscriptionPlan`.

### Phase 2: Frontend Foundation & Design System (Week 2)
- Implement the **design tokens** (colors, typography, spacing) from the HTML template into Tailwind v4 `@theme`.
- Build reusable components: `Header`, `Footer`, `Button`, `Container`, `SectionHeader`, `ProductCard`.
- Convert static HTML sections into **React Server Components** where possible, with client components for interactive elements (tabs, mobile menu).
- Set up **Framer Motion** for scroll-triggered animations (replacing CSS `reveal` logic).

### Phase 3: Product Catalog & Dynamic Pages (Week 3)
- Create API endpoints: `/api/tea/products/`, `/api/tea/categories/`.
- Implement **product listing page** with filtering by origin/fermentation/season (using URL search params).
- Implement **product detail page** with rich content (images, description, brewing params).
- Integrate **TanStack Query** for client-side data fetching and caching.

### Phase 4: Subscription & Tea Culture Content (Week 4)
- Build **subscription landing section** (dynamic from Django).
- Create **Tea Culture** blog-like pages: brewing guides, tasting notes, history (using Django flat pages or a simple `Article` model).
- Implement **newsletter signup** (save to Django, integrate with email service later).

### Phase 5: E-Commerce Integration (MVP vs. Full)
- **MVP Option**: "Purchase Entry" links to an external shop (e.g., Shopify store) as per original requirement.
- **Full Option**: Implement cart and checkout using **Stripe Checkout** (or similar) with Django handling order creation and webhooks.

### Phase 6: Testing, Optimization, Deployment (Week 5)
- Write unit/integration tests for critical paths (JWT flow, product API).
- Optimize images with Next.js `Image` component.
- Deploy frontend to Vercel, backend to Railway/AWS.
- Set up CI/CD pipelines.

---

Excellent. You've chosen **Approach C** with full e-commerce capabilities, custom Django admin for content management, and user accounts for subscriptions, orders, reviews, and a preference quiz. This sets a clear and ambitious scope. Let's now dive deeper into the **ANALYZE** phase to refine our understanding before presenting a detailed plan.

---

## 1. Restated Goal (Refined with Your Decisions)

We are building **Cha Yuan**, a premium tea e-commerce platform with:

- **Full in-site shopping cart and checkout** (not just an external link)
- **Custom Django Admin** as the primary content management system for products, blog/culture posts, and subscription plans
- **User accounts** supporting:
  - Subscription management (view/modify/cancel)
  - Order history
  - Product reviews
  - A **personalized tea preference quiz**

The frontend will be a **Next.js 16 (App Router) + React 19 + TypeScript** application following the **BFF proxy pattern** to communicate with a **Django 6 + PostgreSQL 17** backend. The visual identity and interaction patterns from the provided HTML template will serve as the foundation for the UI.

---

## 2. Sub-Approaches Within "Approach C" (Custom Django + Next.js BFF)

Even within the custom full-stack path, there are architectural nuances that affect development velocity, security, and scalability.

| Sub-Approach | Description | Key Characteristics |
|--------------|-------------|---------------------|
| **C1: Monolithic Django with Next.js as "Dumb" Frontend** | Django serves all business logic, including session/cart management via server-side sessions. Next.js acts primarily as a view layer, calling Django APIs for everything. Cart state lives on Django server. | Simpler backend logic; relies on Django sessions; less client-side state complexity; higher latency for cart updates. |
| **C2: BFF with Client-Side Cart State (Hybrid)** | Next.js BFF handles authentication and proxies API calls. Cart state is managed **client-side** (Zustand) with synchronization to Django only at checkout. Django manages inventory, orders, user profiles. | Faster cart interactions; reduced server load; more complex inventory validation at checkout; potential for stale client state. |
| **C3: BFF with Server-Managed Cart (Redis)** | Next.js BFF proxies to Django, but the **cart itself is stored server-side in Redis** (via Django). The client receives a cart ID stored in a cookie. All cart operations are API calls. | Single source of truth for cart; allows cart persistence across devices; simpler inventory checks; slightly higher latency per cart action. |
| **C4: Headless Commerce Backend (Saleor/Medusa) + Django for Content** | Replace custom Django e-commerce with a specialized open-source headless commerce platform (e.g., Saleor, Medusa). Django handles only content (blog, culture, quiz) and user profile extensions. | Faster e-commerce feature implementation; robust cart/checkout out-of-the-box; increased operational complexity (two backends); potential for data fragmentation. |

---

## 3. Trade-Off Comparison of Sub-Approaches

| Criteria | C1: Django Monolith | C2: Client-Side Cart | C3: Server-Managed Cart (Redis) | C4: Headless Commerce + Django |
|----------|---------------------|----------------------|--------------------------------|--------------------------------|
| **Cart Reliability** | 🟢 High (server truth) | 🟡 Medium (stale data risk) | 🟢 High (server truth) | 🟢 High (platform-specific) |
| **Perceived Performance** | 🟡 Slower cart updates | 🟢 Instant UI feedback | 🟡 API call per action | 🟢 Optimized |
| **Implementation Complexity** | 🟢 Low | 🟡 Medium (sync logic) | 🟡 Medium (Redis integration) | 🔴 High (dual systems) |
| **Checkout Security** | 🟢 Built-in Django | 🟡 Requires careful validation | 🟢 Centralized checks | 🟢 Handled by platform |
| **Future Scalability** | 🟡 Vertical scaling | 🟢 Horizontally scalable | 🟢 Horizontally scalable | 🟢 Good |
| **Alignment with Tech-Stack Doc** | 🟢 Yes | 🟢 Yes | 🟢 Yes | 🔴 Partially (adds complexity) |
| **Time to MVP** | 🟢 Fastest (Django all-in) | 🟢 Fast | 🟡 Moderate | 🟡 Moderate |

---

## 4. Recommended Best Default Path: **C3 – BFF with Server-Managed Cart (Redis)**

**Rationale:**

- **Single Source of Truth**: The cart lives on the server (Django/Redis). This eliminates inconsistencies between client and server, simplifies inventory validation during checkout, and enables future features like "save cart for later" or cross-device cart persistence.
- **Security**: The BFF pattern already mandates `HttpOnly` cookies for authentication. Extending this to a `cart_id` cookie keeps the cart secure and tamper-proof.
- **Alignment with Provided Guidance**: The tech-stack considerations emphasize **TanStack Query for server state** and **Zustand only for UI state**. A server-managed cart fits perfectly: TanStack Query handles cart data fetching/mutations; Zustand can manage local UI (e.g., "is cart drawer open?").
- **Performance**: With Redis as the cart store, read/write operations are sub-millisecond. Django can asynchronously sync the cart to the database upon checkout.
- **Development Velocity**: While slightly more complex than C1 initially, it prevents future refactoring when we inevitably need features like abandoned cart recovery or persistent guest carts.

**Mitigation**: We can start with **Django database-backed sessions for cart** (simpler) and migrate to Redis later if needed. However, given Redis is already in the stack for caching, using it for cart storage is a natural fit.

---

## 5. Short Execution Plan (High-Level Phases)

### Phase 1: Foundation (Week 1-2)
- **Backend**: Set up Django 6 project with PostgreSQL 17, Redis 7.4, Django Ninja, JWT auth (`django-simple-jwt` with cookie storage).
- **Frontend**: Initialize Next.js 16 project with TypeScript, Tailwind v4, Shadcn UI (React 19 compatible), Framer Motion, TanStack Query, Zustand, Zod.
- **BFF**: Implement proxy route handler (`/api/proxy/[...path]`) and authentication utilities.
- **Data Models**: Define Django models for `User` (extended), `Product`, `Category`, `Origin`, `Review`, `Order`, `Cart`, `SubscriptionPlan`, `QuizQuestion`, `UserPreference`.

### Phase 2: Core E-Commerce (Week 3-4)
- **Product Catalog**: API endpoints for listing/filtering products, product detail. Frontend product listing and detail pages.
- **Cart**: Django API for cart CRUD (stored in Redis). Frontend cart drawer and page using TanStack Query.
- **Checkout**: Integrate **Stripe** for payment processing. Django endpoints for creating payment intent, confirming order, and handling webhooks.

### Phase 3: User Accounts & Content (Week 5-6)
- **Authentication**: Sign up, login, password reset flows in Next.js using server actions and BFF.
- **User Dashboard**: Order history, subscription management, profile settings.
- **Reviews**: API and UI for submitting product reviews.
- **Tea Culture Content**: Django models for `Article`/`Guide`. Frontend blog-like pages with rich text rendering.
- **Admin Customization**: Tailor Django Admin for easy management of products, articles, subscriptions, and quiz data.

### Phase 4: Subscription & Quiz (Week 7)
- **Subscription**: Recurring billing logic (Stripe Billing). User subscription dashboard.
- **Preference Quiz**: Interactive multi-step quiz in Next.js, saving results to user profile.

### Phase 5: Polish & Deployment (Week 8)
- **Animations**: Implement Framer Motion scroll reveals and page transitions.
- **Testing**: Unit tests for critical paths (JWT, cart, checkout).
- **Deployment**: Frontend to Vercel, Backend to Railway/AWS, Redis to Upstash/Elasticache.

---

## 6. Sharp Clarification Questions (Before Detailed Planning)

1. **Payment Provider Preference**: The plan assumes **Stripe** as the payment processor due to its robust subscription and checkout APIs. Do you have an existing Stripe account, or would you prefer an alternative (e.g., Braintree, PayPal, Razorpay)? This affects integration complexity.

2. **Subscription Fulfillment Logic**: The subscription boxes ("Discovery," "Connoisseur," "Master's Reserve") are curated monthly. How should product selection work? Will an admin manually assign products each month, or should the system automatically select based on rules (e.g., "seasonal teas not previously sent to user")? This impacts the subscription model design.

3. **Quiz Personalization Depth**: The preference quiz will influence recommendations. Should it be a **one-time onboarding quiz** or a **dynamic profile** that updates as users rate teas? Also, do you want the quiz results to directly affect which teas appear in the subscription box?

---

# Master Execution Plan: Cha Yuan Premium Tea E-Commerce Platform

This document outlines the comprehensive implementation plan for building the Cha Yuan platform using **Approach C3 – BFF with Server-Managed Cart (Redis)**. The plan is structured into distinct phases with clear deliverables, file structures, API endpoints, and success criteria. All phases align with the six-step workflow: **Analyze → Plan → Validate → Implement → Verify → Deliver**.

---

## Phase 0: Environment & Project Initialization (Days 1–3)

### Objectives
- Establish version-controlled monorepo structure.
- Configure backend and frontend environments with all dependencies.
- Set up local development services (PostgreSQL, Redis).

### Deliverables

| Deliverable | Description | Success Criteria |
|-------------|-------------|------------------|
| Monorepo Structure | `cha-yuan/` with `backend/` and `frontend/` directories | Git initialized, `.gitignore` configured |
| Django Backend Skeleton | Django 6 project named `chayuan` with app `core` and `api` | `python manage.py runserver` loads welcome page |
| PostgreSQL & Redis | Docker Compose file for local services | `docker-compose up` starts Postgres 17 and Redis 7.4 |
| Next.js Frontend Skeleton | Next.js 16 App Router with TypeScript, Tailwind v4, Shadcn UI | `npm run dev` serves on `localhost:3000` |
| Environment Variables | `.env.local` (frontend) and `.env` (backend) templates | Secrets not committed; documented in README |

### File Tree (Key Additions)

```
cha-yuan/
├── backend/
│   ├── chayuan/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── asgi.py
│   ├── core/
│   │   ├── models.py
│   │   ├── admin.py
│   │   └── migrations/
│   ├── api/
│   │   ├── urls.py
│   │   ├── authentication.py
│   │   └── v1/
│   ├── manage.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── globals.css
│   │   └── api/proxy/[...path]/route.ts
│   ├── components/
│   ├── lib/
│   ├── hooks/
│   ├── types/
│   ├── next.config.js
│   ├── tailwind.config.ts
│   ├── package.json
│   └── tsconfig.json
├── docker-compose.yml
└── README.md
```

### Implementation Steps

1. **Backend**:
   - Create virtual environment, install `Django==6.0`, `django-ninja==1.0`, `psycopg2-binary`, `djangorestframework-simplejwt`, `redis`, `stripe`.
   - Run `django-admin startproject chayuan .` and `python manage.py startapp core`.
   - Configure `settings.py` for PostgreSQL and Redis cache.
   - Set up custom user model (email as username).

2. **Frontend**:
   - Run `npx create-next-app@16 frontend --typescript --tailwind --app`.
   - Install `@shadcn/ui`, `framer-motion`, `@tanstack/react-query`, `zustand`, `zod`, `react-hook-form`.
   - Initialize Shadcn with Tailwind v4 configuration.

3. **Docker Compose**:
   - Define services for `postgres` (v17) and `redis` (v7.4).

---

## Phase 1: Authentication & BFF Foundation (Week 1)

### Objectives
- Implement JWT authentication with `HttpOnly` cookies.
- Create Next.js BFF proxy route for secure API communication.
- Build reusable authenticated fetch utility.

### Backend Tasks

| Task | Files | API Endpoints | Success Criteria |
|------|-------|---------------|------------------|
| Custom User Model | `core/models.py` | N/A | User model uses email; migrations applied |
| JWT Cookie Endpoints | `api/v1/auth.py` | `POST /api/v1/auth/login/`, `POST /api/v1/auth/logout/`, `POST /api/v1/auth/refresh/`, `GET /api/v1/auth/me/` | Tokens set as `HttpOnly` cookies; refresh rotation works |
| Authentication Backend | `api/authentication.py` | N/A | Custom `JWTAuth` class for Django Ninja |
| CORS Configuration | `chayuan/settings.py` | N/A | Frontend origin allowed; credentials enabled |

**Sample `api/v1/auth.py`**:
```python
from ninja import Router
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware.csrf import get_token

router = Router()

@router.post("/login")
def login(request, email: str, password: str):
    user = authenticate(email=email, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        response = {"detail": "success"}
        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=True,
            samesite="Lax",
            path="/api/auth/refresh"
        )
        response.set_cookie(
            key="access_token",
            value=str(refresh.access_token),
            httponly=True,
            secure=True,
            samesite="Lax"
        )
        return response
    return {"detail": "Invalid credentials"}, 401
```

### Frontend Tasks

| Task | Files | Success Criteria |
|------|-------|------------------|
| Proxy Route Handler | `app/api/proxy/[...path]/route.ts` | Forwards requests to Django backend with cookie attached |
| Auth Fetch Utility | `lib/auth-fetch.ts` | Detects server/client, reads token on server, uses proxy on client |
| Login/Signup Pages | `app/(auth)/login/page.tsx`, `app/(auth)/signup/page.tsx` | Form validation with Zod, successful login sets cookie |
| Auth Context/Provider | `components/providers/auth-provider.tsx` | Provides user state via React Context + TanStack Query |
| Protected Route Middleware | `proxy.ts` (Next.js 16) | Redirects unauthenticated users from protected routes |

**Key Code: `app/api/proxy/[...path]/route.ts`** (BFF Proxy):
```typescript
import { cookies } from 'next/headers';
import { NextRequest, NextResponse } from 'next/server';

export async function ALL(request: NextRequest) {
  const path = request.nextUrl.pathname.replace('/api/proxy', '');
  const backendUrl = `${process.env.BACKEND_URL}${path}`;

  const cookieStore = await cookies();
  const accessToken = cookieStore.get('access_token')?.value;

  const headers = new Headers(request.headers);
  headers.set('Content-Type', 'application/json');
  if (accessToken) {
    headers.set('Authorization', `Bearer ${accessToken}`);
  }

  const response = await fetch(backendUrl, {
    method: request.method,
    headers,
    body: request.method !== 'GET' ? await request.text() : undefined,
  });

  const data = await response.json();
  return NextResponse.json(data, { status: response.status });
}
```

### Success Criteria (Phase 1)
- Users can sign up, log in, and log out.
- JWT tokens are stored in secure `HttpOnly` cookies.
- Server Components can fetch protected data via `authFetch`.
- Client Components can fetch data via TanStack Query hitting `/api/proxy`.

---

## Phase 2: Core Data Models & Admin Customization (Week 1–2)

### Objectives
- Define Django models for products, categories, origins, reviews, quiz, subscriptions, orders, cart.
- Customize Django Admin for content managers.

### Backend Tasks

| Model | Fields Summary | Admin Features |
|-------|----------------|----------------|
| `Origin` | name, description, image, slug | Search, list display |
| `TeaCategory` | name (Green, Oolong, etc.), fermentation_level, description | Filter sidebar |
| `Product` | name, slug, description, price, stock, origin (FK), category (FK), images (multiple), brewing_temp, brewing_time, tasting_notes, harvest_season, is_subscription_eligible | Inline images, rich text for description, auto-slug |
| `ProductImage` | product (FK), image, alt, is_primary | Inline in Product admin |
| `Review` | user (FK), product (FK), rating (1-5), comment, created_at | List filter by product, moderation actions |
| `QuizQuestion` | question_text, order | Inline for `QuizChoice` |
| `QuizChoice` | question (FK), choice_text, value (JSON for preference mapping) | Inline |
| `UserPreference` | user (FK), preferences (JSON), quiz_completed (bool) | Readonly in User admin |
| `SubscriptionPlan` | name, slug, price, description, interval (monthly), stripe_price_id | List display |
| `UserSubscription` | user (FK), plan (FK), status, current_period_start/end, stripe_subscription_id | Actions: cancel, reactivate |
| `Order` | user (FK), status, total, shipping_address, stripe_payment_intent_id, created_at | Readonly, list display |
| `OrderItem` | order (FK), product (FK), quantity, price_at_time | Inline in Order admin |
| `Cart` (Redis-backed) | Not a Django model; managed via Redis | N/A |
| `Article` | title, slug, content (Markdown), author, published_at, category (Brewing/Tasting/History) | Rich text editor (e.g., django-markdownx) |

### API Endpoints (Django Ninja)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/products/` | GET | List products with filtering (origin, category, season, fermentation) |
| `/api/v1/products/{slug}/` | GET | Product detail |
| `/api/v1/categories/` | GET | List tea categories |
| `/api/v1/origins/` | GET | List origins |
| `/api/v1/reviews/` | GET, POST | List reviews for product; authenticated POST |
| `/api/v1/quiz/questions/` | GET | Fetch all quiz questions with choices |
| `/api/v1/quiz/submit/` | POST | Save user preferences |
| `/api/v1/subscriptions/plans/` | GET | List available plans |
| `/api/v1/articles/` | GET | List culture articles |
| `/api/v1/articles/{slug}/` | GET | Article detail |

### Admin Customization
- Override `ProductAdmin` to include inline images and a preview of slug.
- Add custom actions for bulk updating stock.
- Use `django-import-export` for product CSV import.
- Customize dashboard with recent orders, low stock alerts.

### Success Criteria (Phase 2)
- All models created and migrated.
- Admin interface allows full CRUD on products, categories, articles, quiz questions.
- API endpoints return properly serialized data (tested via Swagger UI at `/api/docs`).

---

## Phase 3: Product Catalog & Tea Culture Frontend (Week 2–3)

### Objectives
- Implement public-facing product listing and detail pages.
- Build Tea Culture (blog) section.
- Apply visual design from HTML template using Tailwind and Framer Motion.

### Frontend Tasks

| Page/Component | File Path | Features |
|----------------|-----------|----------|
| Homepage | `app/page.tsx` | Hero, Philosophy, Featured Products (reusable components) |
| Product Listing | `app/products/page.tsx` | Filter by origin, category, fermentation, season; sort options |
| Product Detail | `app/products/[slug]/page.tsx` | Image gallery, description, brewing guide, reviews, add to cart |
| Tea Culture Index | `app/culture/page.tsx` | Grid of articles |
| Article Detail | `app/culture/[slug]/page.tsx` | Rendered Markdown content |
| Search | `app/search/page.tsx` | Client-side search via API |
| Components | `components/product-card.tsx`, `components/product-tabs.tsx`, `components/review-list.tsx`, `components/add-review-form.tsx` | Shadcn UI + Framer Motion animations |

### Data Fetching Strategy
- **Server Components**: Fetch initial product list/detail using `authFetch` (server-side) for SEO.
- **Client Components**: Use TanStack Query for filters, pagination, and user-specific actions (reviews, cart).

### API Integration
- Create typed API client in `lib/api-client.ts` using `authFetch`.
- Define Zod schemas for product, category, review in `types/schemas.ts`.

### Animations
- Replace CSS reveal classes with Framer Motion `whileInView` and `variants`.
- Implement page transitions with `AnimatePresence` in `layout.tsx`.

### Success Criteria (Phase 3)
- Product listing with working filters and pagination.
- Product detail page displays all information, including brewing parameters.
- Tea culture section renders articles from Django.
- UI matches the design language of the HTML template (colors, typography, spacing).

---

## Phase 4: Shopping Cart (Redis-Backed) & Checkout (Week 3–4)

### Objectives
- Implement server-managed cart using Redis.
- Integrate Stripe Checkout for payments.
- Create order confirmation flow.

### Backend Tasks

| Task | Endpoints | Implementation Notes |
|------|-----------|----------------------|
| Cart Service (Redis) | `api/v1/cart.py` | `GET /cart/`, `POST /cart/add/`, `PATCH /cart/item/{id}/`, `DELETE /cart/item/{id}/` |
| Cart Data Structure | Redis hash: `cart:{session_id}` with fields `product_id:quantity` | Use `uuid.uuid4()` for anonymous carts, store `cart_id` in cookie |
| Merge Cart on Login | Middleware to migrate anonymous cart to user cart after authentication | |
| Stripe Checkout Session | `POST /api/v1/checkout/create-session/` | Creates Stripe Checkout session with line items from cart |
| Stripe Webhook | `POST /api/v1/webhooks/stripe/` | Handles `checkout.session.completed` to create Order, clear cart |
| Order API | `GET /api/v1/orders/`, `GET /api/v1/orders/{id}/` | For user dashboard |

**Cart API Example**:
```python
@router.get("/cart")
def get_cart(request):
    cart_id = request.COOKIES.get("cart_id")
    if not cart_id:
        return {"items": [], "total": 0}
    cart_data = redis_client.hgetall(f"cart:{cart_id}")
    # Convert to list of items with product details
    ...

@router.post("/cart/add")
def add_to_cart(request, product_id: int, quantity: int = 1):
    cart_id = request.COOKIES.get("cart_id") or str(uuid.uuid4())
    redis_client.hincrby(f"cart:{cart_id}", product_id, quantity)
    response = {"success": True}
    if not request.COOKIES.get("cart_id"):
        response.set_cookie("cart_id", cart_id, httponly=True, max_age=60*60*24*30)
    return response
```

### Frontend Tasks

| Component | File | Functionality |
|-----------|------|---------------|
| Cart Provider | `components/providers/cart-provider.tsx` | Zustand store for UI state (drawer open) + TanStack Query for cart data |
| Cart Drawer | `components/cart/cart-drawer.tsx` | Slide-out panel showing items, quantity adjust, remove |
| Cart Page | `app/cart/page.tsx` | Full-page cart with summary and checkout button |
| Checkout Flow | `app/checkout/page.tsx` | Redirects to Stripe Checkout; handles success/cancel |
| Order Confirmation | `app/checkout/success/page.tsx` | Displays order summary from Stripe session |

### Stripe Integration Flow
1. User clicks "Checkout" → frontend calls `POST /api/proxy/checkout/create-session/`.
2. Backend creates Stripe Checkout session with line items, success/cancel URLs.
3. Frontend redirects to `session.url`.
4. Stripe redirects to success URL → frontend shows order confirmation.
5. Webhook updates order status and clears cart.

### Success Criteria (Phase 4)
- Users can add/remove items to cart; cart persists across page refreshes.
- Anonymous carts are merged upon login.
- Checkout completes successfully with Stripe test mode.
- Orders appear in user dashboard and Django Admin.

---

## Phase 5: User Accounts, Reviews & Preference Quiz (Week 5–6)

### Objectives
- Build user dashboard for order history, subscriptions, profile.
- Implement product reviews.
- Create one-time onboarding preference quiz.

### Backend Tasks

| Task | Endpoints | Description |
|------|-----------|-------------|
| User Profile | `GET /api/v1/users/me/`, `PATCH /api/v1/users/me/` | Update name, email, password |
| Order History | `GET /api/v1/users/me/orders/` | Paginated list of user orders |
| Subscription Management | `GET /api/v1/users/me/subscription/`, `POST /api/v1/users/me/subscription/cancel/` | View active sub, cancel |
| Review Submission | `POST /api/v1/products/{slug}/reviews/` | Authenticated users only; one review per product |
| Quiz Questions | `GET /api/v1/quiz/questions/` | Returns list of questions with choices |
| Quiz Submission | `POST /api/v1/quiz/submit/` | Saves preferences to `UserPreference` |

### Frontend Tasks

| Page/Component | File Path | Features |
|----------------|-----------|----------|
| Dashboard Layout | `app/dashboard/layout.tsx` | Sidebar navigation (Orders, Subscription, Reviews, Profile) |
| Orders List | `app/dashboard/orders/page.tsx` | Table of past orders with links to detail |
| Order Detail | `app/dashboard/orders/[id]/page.tsx` | Shows items, total, status |
| Subscription Panel | `app/dashboard/subscription/page.tsx` | Displays current plan, next billing date, cancel button |
| Reviews List | `app/dashboard/reviews/page.tsx` | User's submitted reviews with edit option |
| Preference Quiz | `app/quiz/page.tsx` | Multi-step form using React Hook Form + Zod; saves results |

### Quiz Flow
- Protected route; redirect to quiz if not completed.
- On completion, store preferences in backend; used later for product recommendations.

### Success Criteria (Phase 5)
- Authenticated users can view order history, manage subscription, write reviews.
- Quiz can be taken once; results saved.
- User dashboard is polished and responsive.

---

## Phase 6: Subscription Service with Auto-Selection Rules (Week 6–7)

### Objectives
- Implement recurring subscriptions via Stripe Billing.
- Build automated monthly box curation based on user preferences and history.

### Backend Tasks

| Task | Implementation | Success Criteria |
|------|----------------|------------------|
| Stripe Product/Price Sync | Management command to sync Django `SubscriptionPlan` with Stripe | Plans created in Stripe dashboard |
| Subscription Creation | `POST /api/v1/subscriptions/create/` | Creates Stripe subscription; webhook confirms activation |
| Monthly Curation Job | Celery beat task (or Django Tasks) | Runs monthly; selects 3-5 teas per subscriber based on rules |
| Curation Rules Engine | `core/curation.py` | Implements "seasonal teas not previously sent to user" logic; considers quiz preferences |
| Shipping Label Generation | Integration with shipping carrier (e.g., Shippo) | Generated after curation |
| Subscription Shipment Model | `SubscriptionShipment` (user_sub, products, status, tracking) | Admin can view/manage shipments |

**Curation Logic Snippet**:
```python
def curate_box(user):
    # Get user preferences from quiz
    prefs = UserPreference.objects.get(user=user).preferences
    # Get all subscription-eligible teas
    eligible = Product.objects.filter(is_subscription_eligible=True, stock__gt=0)
    # Exclude teas user has received in past shipments
    past_ids = SubscriptionShipment.objects.filter(
        subscription__user=user
    ).values_list('products__id', flat=True)
    candidates = eligible.exclude(id__in=past_ids)
    # Filter by season (current season)
    current_season = get_current_season()
    candidates = candidates.filter(harvest_season=current_season)
    # Score candidates based on preference match (e.g., category preference)
    # Select top 4
    selected = score_and_select(candidates, prefs, limit=4)
    return selected
```

### Frontend Tasks

| Page | Features |
|------|----------|
| Subscription Signup | `app/subscribe/page.tsx` | Displays plans, links to checkout (Stripe) |
| Subscription Dashboard | Enhanced with shipment history, upcoming box preview | |

### Success Criteria (Phase 6)
- Users can subscribe to a plan; recurring billing works.
- Admin can trigger monthly curation (or it runs automatically).
- Subscribers see their shipment history and next box contents.

---

## Phase 7: Polish, Testing & Deployment (Week 7–8)

### Objectives
- Optimize performance, accessibility, and SEO.
- Write comprehensive tests.
- Deploy to production.

### Tasks

| Area | Actions | Success Criteria |
|------|---------|------------------|
| Frontend Optimization | Add Next.js `Image` for all images; lazy load; implement `next/font` | Lighthouse score > 95 |
| SEO | Metadata API for all pages; generate sitemap; structured data (Product schema) | Google Rich Results Test passes |
| Accessibility | Audit with axe DevTools; ensure keyboard navigation | WCAG 2.1 AA compliant |
| Backend Tests | Unit tests for models, API endpoints (pytest) | Coverage > 80% |
| Frontend Tests | Component tests with React Testing Library; E2E with Playwright for critical flows | Key user journeys pass |
| Deployment | Frontend to Vercel; Backend to Railway/AWS; Redis to Upstash; Postgres to managed service | Production URL accessible |
| CI/CD | GitHub Actions for lint, test, build on PR; auto-deploy on main | Green pipeline |

### Deployment Checklist
- Set environment variables (Stripe keys, secret keys).
- Configure custom domain and SSL.
- Set up monitoring (Sentry, Logtail).
- Enable Stripe live mode.

---

## Success Metrics Summary

| Phase | Key Deliverable | Success Indicator |
|-------|-----------------|-------------------|
| 0 | Environment setup | Local dev runs without errors |
| 1 | Auth + BFF | Users can sign in; protected API calls work |
| 2 | Data models + Admin | Admin can manage all content types |
| 3 | Catalog + Culture | Product pages render with filters; articles display |
| 4 | Cart + Checkout | Successful test purchase via Stripe |
| 5 | User dashboard | Order history, reviews, quiz functional |
| 6 | Subscriptions | Recurring billing; curated boxes generated |
| 7 | Production deployment | Site live with SSL, monitoring |

---

## Next Steps

1. **Validate**: Review this master plan and confirm scope, timeline, and any adjustments.
2. **Implement**: Once validated, I will begin Phase 0 execution, providing regular progress updates.
3. **Verify**: Each phase includes success criteria; I will run tests and request your verification before proceeding.

# https://chat.deepseek.com/share/vazgkj0x3jijc7ye8h
