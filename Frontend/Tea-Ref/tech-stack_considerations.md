This stack represents a "bleeding edge" configuration (assuming a mid-2026 timeframe based on the versions listed). While these components are designed to work together, you will encounter specific friction points regarding React Server Components (RSC) serialization, CSS-in-JS deprecation, and strict type inference.
## Compatibility Matrix & Critical Conflicts

| Component [1, 2, 3, 4, 5, 6] | Version | Compatibility Status | Primary Conflict / Issue |
|---|---|---|---|
| Next.js | 16.x | Stable (LTS) | middleware.ts is replaced by proxy.ts; check for use cache directive usage. |
| React | 19.x | Stable | Breaking: forwardRef is largely deprecated; ref is now a standard prop. |
| TypeScript | 5.9 | Stable | strictInference flag can break existing loosely typed Shadcn components. |
| Tailwind CSS | v4 | Stable | No longer uses tailwind.config.js by default; requires @import "tailwindcss". |
| Radix UI | Latest | Patch Required | Silent failures in asChild prop merging due to React 16+ serialization changes. |
| Shadcn UI | Latest | Compatible | Requires manual update to remove forwardRef to match React 19 standards. |

## Deep Dive: Known Issues & Solutions## 1. Radix UI "Silent Failure" in Next.js 16
A regression in Next.js 16+ (specifically 16.0.10+) affects how React Server Components serialize the Slot primitive used by Radix. [6] 

* The Conflict: The asChild prop, which is fundamental to how Radix (and thus Shadcn) merges properties with child elements, may silently fail to merge classes in local development.
* The Fix: Move className directly to the child element instead of the Radix primitive, or avoid asChild for problematic components during dev. [6] 

## 2. Tailwind v4 Architecture Shift
Tailwind v4 is a significant departure from v3, moving away from a JavaScript-heavy configuration.

* The Conflict: Old tailwind.config.js files are ignored by default. If your project relies on legacy plugins not yet ported to v4, they will break.
* The Fix: Use the new CSS-first configuration via @theme blocks in your global CSS. Ensure you are using the @tailwindcss/postcss plugin rather than the legacy PostCSS configuration. [3, 5, 7] 

## 3. React 19 Prop Changes (forwardRef) [8] 
React 19 simplifies how ref is handled, treating it as a normal prop rather than requiring the forwardRef wrapper. [9, 10, 11] 

* The Conflict: Many Shadcn UI components were originally scaffolded with forwardRef. While backwards compatible, keeping them causes "double-ref" warnings or hydration mismatches in Next.js 16.
* The Fix: Shadcn's latest CLI and documentation recommend removing forwardRef entirely and passing ref as a standard prop. [3, 12] 

## 4. TypeScript 5.9 Strictness [13] 
TypeScript 5.9 introduces strictInference and changes to module detection. [4, 13] 

* The Conflict: Components that rely on implicit any in complex generics (common in UI primitives) may now throw errors.
* The Fix: Ensure your tsconfig.json targets esnext and explicitly define types for data-slot attributes introduced in newer Shadcn versions. [3, 13] 

## Recommendation for Implementation
To avoid these conflicts, initialize your project using the dedicated Shadcn v4/React 19 guide. This path ensures the CLI provides components pre-formatted for React 19 (no forwardRef) and Tailwind v4 (OKLCH color space instead of HSL). [3] 
Are you looking for a migration script to update your existing Shadcn components to the React 19/Tailwind v4 standard?

[1] [https://www.luckymedia.dev](https://www.luckymedia.dev/blog/nextjs-16-an-early-look-and-release-date)
[2] [https://github.com](https://github.com/vercel/next.js/releases)
[3] [https://ui.shadcn.com](https://ui.shadcn.com/docs/tailwind-v4)
[4] [https://www.digitalapplied.com](https://www.digitalapplied.com/blog/typescript-5-9-new-features-developer-guide-2026)
[5] [https://medium.com](https://medium.com/@hardikkumarpro0005/fixing-next-js-15-and-tailwind-css-v4-build-issues-complete-solutions-guide-438b0665eabe)
[6] [https://github.com](https://github.com/radix-ui/primitives/issues/3780)
[7] [https://medium.com](https://medium.com/uxdworld/5-advanced-shadcn-tailwind-4-combinations-that-transform-ui-development-1fd65cd715a2#:~:text=Tailwind%20CSS%20v4.%200%20shifts%20from%20JavaScript,shadcn%20components%20integrate%20with%20your%20design%20system.)
[8] [https://www.youtube.com](https://www.youtube.com/watch?v=rwC7HY8_U_g&t=256)
[9] [https://dirox.com](https://dirox.com/post/new-react-19-features-you-should-know-explained-with-code-examples#:~:text=React%2019%20allows%20refs%20to%20be%20passed,props%20without%20needing%20forwardRef%2C%20simplifying%20component%20composition.)
[10] [https://blog.stackademic.com](https://blog.stackademic.com/exploring-the-new-features-in-react-19-transforming-the-developer-experience-fac3c18d4aba#:~:text=Overview:%20React%2019%20allows%20ref%20to%20be,composition%20and%20improves%20how%20refs%20are%20handled.)
[11] [https://levelup.gitconnected.com](https://levelup.gitconnected.com/react-19-released-new-game-changing-features-for-developers-you-must-know-50535f8e05f8#:~:text=React%2019%20simplifies%20this%20by%20allowing%20you,longer%20need%20forwardRef%20in%20many%20common%20scenarios.)
[12] [https://infinum.com](https://infinum.com/handbook/frontend/react/tailwind/shadcn#:~:text=Instead%20it%20%28%20ShadCN%20UI%20%29%20gives,or%20refactor%20without%20fighting%20an%20API%20surface.)
[13] [https://thenewstack.io](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/#:~:text=TypeScript%205.9%20was%20released%20on%20August%201%2C,**%2D%2Dtarget%20can%20typically%20be%20set%20to%20esnext**)

---

In the 2026 Next.js 16 ecosystem, JWT (JSON Web Tokens) remains the foundational technology for token-based auth, but the "optimal framework" has shifted toward libraries that abstract the complexities of JWT management, session rotation, and security. [1, 2] 
## The Best Recommendation (Frameworks)
For a modern React 19 / Next.js 16 stack, the choice depends on your trade-off between speed and control:

* [Clerk](https://clerk.com/articles/what-authentication-solutions-work-well-with-react-and-nextjs): Currently the most commonly adopted for rapid development. It is a managed service providing pre-built UI components (like <SignIn />) that are native to React 19 and fully compatible with Next.js 16’s proxy.ts.
* [Auth.js](https://authjs.dev/guides/refresh-token-rotation) (formerly NextAuth.js): The standard open-source toolkit if you want full control over your database. It supports both "stateless" JWT strategies and "database" session strategies.
* Better Auth: A newer, rising favorite specifically for TypeScript purists. It is praised for being more lightweight and type-safe than Auth.js while avoiding the vendor lock-in of Clerk. [3, 4, 5, 6, 7, 8, 9, 10] 

## Is it JWT or "Something Else"?
It is usually both. Modern authentication is rarely just "raw" JWT anymore; it typically uses a Hybrid Approach: [6, 11, 12, 13, 14] 

| Feature [6, 15, 16, 17, 18] | JWT (Stateless) | Sessions (Database) | Modern Hybrid (Clerk/Auth.js) |
|---|---|---|---|
| Storage | Client (Cookies/Local) | Server (DB/Redis) | Short-lived JWTs in cookies + Refresh Tokens. |
| Verification | Fast (no DB lookup) | Slower (requires DB check) | Fast local verification with optional 1-min TTLs to mitigate risk. |
| Revocation | Difficult (valid until expiry) | Instant (delete from DB) | Session-based revocation via a managed backend or refresh token invalidation. |

## Why use JWT with Next.js 16?

* Edge Compatibility: JWTs are ideal for Next.js Serverless and Edge environments because the server can verify the token signature without needing to query a central database on every request.
* Stateless Scaling: Without server-side sessions, your application scales horizontally with ease, making it a "go-to" for distributed microservices.
* Security Shift: Best practice in 2026 dictates storing JWTs in HttpOnly, Secure cookies to prevent XSS attacks, rather than localStorage. [2, 15, 19, 20] 

Summary Verdict: Use Clerk if you want to be "up and running" in minutes with a polished UI. Use Better Auth or Auth.js if you need to keep your user data in your own database (Prisma/Drizzle). [10, 21, 22] 
Would you like a starter template configuration for one of these frameworks to test in your stack?

[1] [https://strapi.io](https://strapi.io/blog/jwt-vs-oauth)
[2] [https://codegive.com](https://codegive.com/blog/jwt_authentication_next_js.php)
[3] [https://workos.com](https://workos.com/blog/top-authentication-solutions-nextjs-2026)
[4] [https://www.youtube.com](https://www.youtube.com/watch?v=vP0wS-dgFic&t=36)
[5] [https://clerk.com](https://clerk.com/articles/what-authentication-solutions-work-well-with-react-and-nextjs)
[6] [https://clerk.com](https://clerk.com/articles/nextjs-session-management-solving-nextauth-persistence-issues)
[7] [https://supastarter.dev](https://supastarter.dev/blog/better-auth-vs-nextauth-vs-clerk)
[8] [https://authjs.dev](https://authjs.dev/guides/refresh-token-rotation)
[9] [https://www.youtube.com](https://www.youtube.com/watch?v=LMUsWY5alY0&t=124)
[10] [https://www.youtube.com](https://www.youtube.com/watch?v=TDzfWm0Tn8U&t=403)
[11] [https://medium.com](https://medium.com/@jbyj/why-not-go-ahead-and-use-jwts-for-authentication-31810a4ce605#:~:text=Cookies%20are%20a%20%28mostly%29%20standarized%20mechanism%20and,%28and%20routinely%20are%29%20used%20in%20your%20application.)
[12] [https://zuplo.com](https://zuplo.com/blog/authentication-with-both-jwt-and-api-keys#:~:text=There%20are%20countless%20debates%20on%20which%20authentication,or%20both%29%20your%20API%20should%20support%20both.)
[13] [https://www.reddit.com](https://www.reddit.com/r/django/comments/1bb7y1m/session_and_jwt_authentication_a_good_idea/#:~:text=However%20in%20the%20very%20near%20future%2C%20I,tokens%2C%20which%20are%20then%20stored%20in%20AsyncStorage.)
[14] [https://medium.com](https://medium.com/@bhargavkoya56/why-jwt-authentication-is-reshaping-enterprise-api-security-in-2025-4ce7b36656ea#:~:text=The%20Future%20of%20API%20Authentication%20As%20we,remains%20the%20backbone%20of%20modern%20API%20security.)
[15] [https://medium.com](https://medium.com/@outreach_8378/jwt-vs-oauth-a-developers-guide-to-choosing-the-right-authentication-638b9b3ab9e7)
[16] [https://www.youtube.com](https://www.youtube.com/watch?v=fyTxwIa-1U0&t=12)
[17] [https://zuplo.com](https://zuplo.com/learning-center/top-7-api-authentication-methods-compared)
[18] [https://www.linkedin.com](https://www.linkedin.com/posts/alexxubyte_systemdesign-coding-interviewtips-activity-7196173730081898496-S3Qo#:~:text=JWT%20for%20authentication%20is%20great%20for%20stateless,although%20the%20token%20might%20be%20still%20valid.)
[19] [https://www.reddit.com](https://www.reddit.com/r/nextjs/comments/1aj327r/nextjs_app_router_authentication_sessions_cookies/)
[20] [https://www.wallarm.com](https://www.wallarm.com/what/oauth-vs-jwt-detailed-comparison)
[21] [https://chhimpashubham.medium.com](https://chhimpashubham.medium.com/nextauth-js-vs-clerk-vs-auth-js-which-is-best-for-your-next-js-app-in-2025-fc715c2ccbfd)
[22] [https://www.reddit.com](https://www.reddit.com/r/reactjs/comments/1icpyu5/how_to_handle_auth_best_practices/#:~:text=js%2C%20or%20my%20current%20favourite%20by%20far%2C,beats%20Better%20Auth%20atm%20for%20its%20documentation.)

---

Adding these specific versions to your stack is technically compatible but introduces significant architectural redundancy and potential hydration issues in the Next.js 16/React 19 environment.
## Conflict Analysis & Compatibility Matrix

| Specification [1, 2, 3, 4, 5, 6, 7, 8] | Version | Conflict Status | Critical Consideration |
|---|---|---|---|
| Zustand | 5.x | Low Risk | High risk of Server/Client state desync if used for data that should be in TanStack Query. |
| Zod | 4.x | No Conflict | Schema-first validation is the industry standard for Shadcn forms and Server Actions. |
| TanStack Query | 5.x | Low Risk | Overlaps with Next.js 16's native use cache and request memoization. |
| Axios | 1.14 | High Risk | JWT interceptors often fail in Server Components and the new Next.js 16 proxy.ts. |

------------------------------
## Key Areas of Friction## 1. The "Dual-Source" Problem (Zustand vs. TanStack Query)
Using both for global state often leads to "state fragmentation."

* The Conflict: Developers frequently store fetched API data in a Zustand store. In Next.js 16, this is an anti-pattern. TanStack Query should handle all server-originated data, while Zustand should be reserved strictly for client-only UI state (e.g., "is the sidebar open?").
* The Fix: Use the TanStack Query Devtools to ensure server state is not being duplicated in your Zustand store.

## 2. Axios Interceptors vs. Next.js 16 proxy.ts
Next.js 16 has officially renamed middleware.ts to proxy.ts. [9, 10] 

* The Conflict: Axios interceptors run in the browser (client-side). However, Next.js 16 Server Components and proxy.ts do not execute Axios client code. If you rely on an Axios interceptor to attach a JWT, your Server Actions and Server Side Rendering (SSR) requests will fail because they won't have the token.
* The Fix: Use the native fetch API. It is more deeply integrated with Next.js 16's caching layer (use cache). For JWTs, handle them in proxy.ts to ensure tokens are attached to requests regardless of whether they originate from the client or server. [2, 6, 8] 

## 3. Zod 4 + React 19 Forms

* Compatibility: Zod 4 is fully compatible with the new Shadcn UI v4 standards, which have removed forwardRef to align with React 19.
* Advantage: This allows for "type-safe" server actions where the same Zod schema validates data on both the client (via React Hook Form) and the server. [3, 4, 11] 

## 4. Hydration Errors (Zustand 5)

* The Conflict: In Next.js 16, if a Zustand store is initialized with data on the server that differs from the client, you will get a Hydration Mismatch error.
* The Fix: Always use a "persisted" or "hydrated" check in your components before rendering state from Zustand, or utilize the useStore hook with a selector to ensure safety. [12] 

## Summary Recommendation

* Keep: Zod 4 (essential) and TanStack Query 5 (for complex caching).
* Caution: Use Zustand 5 sparingly—only for UI state that doesn't touch the database.
* Replace: Consider replacing Axios with native fetch wrappers. Next.js 16's architecture is optimized for fetch for its automatic request memoization and caching features. [6, 13] 

Would you like to see the correct implementation pattern for a JWT-protected fetch call that works in both Client and Server Components?

[1] [https://github.com](https://github.com/pmndrs/zustand/discussions/2200#:~:text=There%20is%20a%20bit%20of%20an%20invisible,ErrorBoundary%20which%20does%20fire%20on%20the%20server.)
[2] [https://www.reddit.com](https://www.reddit.com/r/nextjs/comments/1bs7513/confused_about_zustand_usage_within_next/#:~:text=TLDR:%20Use%20Zustand%20with%20context%20if%20you,okay%20if%20you%20know%20what%20you%27re%20doing.)
[3] [https://github.com](https://github.com/orgs/react-hook-form/discussions/11209)
[4] [https://www.youtube.com](https://www.youtube.com/watch?v=rdgbXXmDDgk)
[5] [https://dev.to](https://dev.to/krish_kakadiya_5f0eaf6342/react-server-components-tanstack-query-the-2026-data-fetching-power-duo-you-cant-ignore-21fj)
[6] [https://medium.com](https://medium.com/@bendesai5703/next-js-16-react-query-the-ultimate-guide-to-modern-data-fetching-caching-performance-ac13a62d727d)
[7] [https://dev.to](https://dev.to/aakash_shrivas_0806333bbe/nextjs-middleware-is-changing-what-you-need-to-know-about-the-move-toward-proxies-3ndk)
[8] [https://github.com](https://github.com/vercel/next.js/discussions/77392)
[9] [https://nextjs.org](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
[10] [https://github.com](https://github.com/workos/authkit-nextjs/issues/364)
[11] [https://ui.shadcn.com](https://ui.shadcn.com/docs/tailwind-v4)
[12] [https://www.npmjs.com](https://www.npmjs.com/package/zustand)
[13] [https://posthog.com](https://posthog.com/docs/advanced/proxy/nextjs-middleware)

---

In the Next.js 16 and React 19 environment, the "Isomorphic Fetch" pattern is the recommended way to handle JWT-protected calls. This pattern allows the same utility to run in both Server Components and Client Components by abstracting how it retrieves the token.
## Core Implementation Strategy: The "Auth Fetcher"
The primary goal is to store your JWT in HttpOnly cookies. This ensures security against XSS and allows the server to read the token automatically.
## 1. Define the Shared Fetch Utility
Create a utility that detects the environment. In Server Components, it uses next/headers to read cookies; in Client Components, it makes a request to a local API route that acts as a secure proxy to your external backend. [1, 2] 

// lib/auth-fetch.tsimport { cookies } from 'next/headers';
export async function authFetch(url: string, options: RequestInit = {}) {
  let token: string | undefined;

  if (typeof window === 'undefined') {
    // SERVER-SIDE: Access cookies directly from the request headers
    const cookieStore = await cookies();
    token = cookieStore.get('auth_token')?.value;
  } else {
    // CLIENT-SIDE: Tokens in HttpOnly cookies are not accessible to JS.
    // We send the request to our own Next.js API route (/api/proxy)
    // which then forwards it with the cookie to the external backend.
    url = `/api/proxy?path=${encodeURIComponent(url)}`;
  }

  const headers = new Headers(options.headers);
  if (token) {
    headers.set('Authorization', `Bearer ${token}`);
  }

  return fetch(url, { ...options, headers });
}

## 2. The proxy.ts (Next.js 16 Middleware Replacement)
In Next.js 16, middleware.ts is renamed to proxy.ts. Its role is to intercept requests and handle global concerns like token refresh before the request reaches your components. [3, 4, 5] 

// proxy.tsimport { NextResponse } from 'next/server';import type { NextRequest } from 'next/server';
export async function proxy(request: NextRequest) {
  const token = request.cookies.get('auth_token');

  // OPTIONAL: Implement automatic token rotation here.
  // If the token is expired, call your backend's /refresh endpoint 
  // and update the response cookie before passing the request through.
  
  if (!token && !request.nextUrl.pathname.startsWith('/login')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }

  return NextResponse.next();
}

## Usage Patterns

* In Server Components (RSC):
You can call authFetch directly within your async component. Since it's on the server, it will securely pull the token from the cookie store and call your backend.
* In Client Components:
When authFetch is called from a component with 'use client', it automatically reroutes the request through your internal /api/proxy route. This hides your external API URL from the browser and keeps token handling server-side. [6, 7] 

## Why this pattern is optimal for your stack:

   1. React 19 Compatibility: It avoids legacy forwardRef patterns and works perfectly with the new use hook for data fetching.
   2. No Axios Needed: By using native fetch, you benefit from Next.js 16's automatic request memoization, which prevents duplicate calls even if multiple components request the same data in one render pass.
   3. Security: Storing tokens in HttpOnly cookies instead of localStorage (where libraries like Axios often look) protects you from modern token-stealing scripts. [6, 8, 9] 

Would you like a specific API Route Handler example to complete the "Client-to-External-Backend" proxy logic?

[1] [https://github.com](https://github.com/vercel/next.js/discussions/69451#:~:text=Here%27s%20some%20information%20about%20making%20authenticated%20calls,like%20TRPC%20and%20use%20NextJS%20as%20BFF.)
[2] [https://medium.com](https://medium.com/@mohdjamikhann/seamless-authentication-solution-with-cookies-and-jwt-in-next-js-and-express-backend-f8c0bc9d079c)
[3] [https://nextjs.org](https://nextjs.org/blog/next-16)
[4] [https://nextjs.org](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
[5] [https://auth0.com](https://auth0.com/blog/whats-new-nextjs-16/)
[6] [https://www.youtube.com](https://www.youtube.com/watch?v=WKfPctdIDek)
[7] [https://stackoverflow.com](https://stackoverflow.com/questions/77826240/next-js-store-jwt-from-external-api-to-use-it-for-calls-to-that-api)
[8] [https://nextjs.org](https://nextjs.org/docs/app/getting-started/fetching-data)
[9] [https://www.youtube.com](https://www.youtube.com/watch?v=AcYF18oGn6Y&t=250)

---

To implement the "Client-to-External-Backend" proxy in Next.js 16/React 19, we treat the Next.js API Route as a Backend-for-Frontend (BFF). This approach keeps your external API secret and ensures your HttpOnly JWTs are handled securely on the server.
## The Implementation Pattern
The pattern involves two main parts: a dynamic Route Handler that forwards requests and a specialized utility to call it.
## 1. The BFF Proxy Route Handler
This handler acts as a bridge. It intercepts client requests, attaches the secure JWT from the browser's cookies, and forwards the request to your actual backend.

// app/api/proxy/route.tsimport { cookies } from 'next/headers';import { NextRequest, NextResponse } from 'next/server';
export async function ALL(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const targetPath = searchParams.get('path'); // e.g., "users/me"

  if (!targetPath) {
    return NextResponse.json({ error: 'Missing target path' }, { status: 400 });
  }

  // 1. Retrieve the JWT from the secure HttpOnly cookie
  const cookieStore = await cookies();
  const token = cookieStore.get('auth_token')?.value;

  // 2. Build the external API URL
  const backendUrl = `${process.env.EXTERNAL_API_URL}/${targetPath}`;

  // 3. Forward the request to the external backend
  try {
    const response = await fetch(backendUrl, {
      method: request.method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`, // Attach the JWT
      },
      // Forward body for POST/PUT/PATCH requests
      body: request.method !== 'GET' ? await request.text() : undefined,
    });

    const data = await response.json();
    return NextResponse.json(data, { status: response.status });
  } catch (error) {
    return NextResponse.json({ error: 'Proxy request failed' }, { status: 500 });
  }
}
// Next.js 16 allows catch-all methods via 'ALL' or specific exports for GET, POST, etc.export { ALL as GET, ALL as POST, ALL as PUT, ALL as DELETE };

## 2. Usage in a Client Component (TanStack Query)
Since you are using TanStack Query 5, your queryFn will now hit your internal proxy instead of the external API directly.

'use client';import { useQuery } from '@tanstack/react-query';
export function UserProfile() {
  const { data, isLoading } = useQuery({
    queryKey: ['user-me'],
    queryFn: async () => {
      // We call our internal Next.js proxy
      const res = await fetch('/api/proxy?path=users/me');
      if (!res.ok) throw new Error('Network response was not ok');
      return res.json();
    },
  });

  if (isLoading) return <div>Loading...</div>;
  return <div>Welcome, {data.name}!</div>;
}

## Why this is the "Correct" Pattern for your Stack:

* Next.js 16 proxy.ts Integration: Your proxy.ts (formerly middleware) can sit in front of this route to handle [token rotation](https://authjs.dev/guides/refresh-token-rotation) or redirect users if the auth_token cookie is missing before the request even hits the handler. [3]
* Security (BFF Layer): Your external backend URL (e.g., ://production-server.com) is never exposed in the browser's Network tab—only the /api/proxy endpoint is visible.
* React 19 Compatibility: This pattern avoids complex client-side interceptors (like legacy Axios configurations) and uses standard fetch which is optimized for React 19's [Server Component serialization](https://nextjs.org/docs/app/api-reference/file-conventions/proxy).
* TanStack Query 5 friendly: TanStack Query is purely a state manager; it doesn't care where the fetch goes. By pointing it to your BFF, you keep the client logic simple while the server handles the "heavy lifting" of auth headers. [1, 2, 3, 4, 5] 

Would you like to explore how to implement Refresh Token Rotation inside the new proxy.ts file to keep these sessions alive?

[1] [https://www.reddit.com](https://www.reddit.com/r/nextjs/comments/1f5o1nl/server_action_vs_route_handler/)
[2] [https://medium.com](https://medium.com/@urboifox/authentication-in-next-ajs-with-an-external-backend-262fc2748158)
[3] [https://u11d.com](https://u11d.com/blog/nextjs-16-proxy-vs-middleware-bff-guide/)
[4] [https://beyondit.blog](https://beyondit.blog/blogs/nextjs-16-1-migration-middleware-to-proxy)
[5] [https://www.youtube.com](https://www.youtube.com/watch?v=m4Yyu_oePbA)
