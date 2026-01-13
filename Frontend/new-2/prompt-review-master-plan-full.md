Awesome job on your meticulous review, analysis and planning! Please keep up the good work in your rigorous and meticulous approach to planning and execution! Now, please meticulously meticulously review, analyze and validate/critique the following `MASTER_EXECUTION_PLAN.md` to build the complete codebase for an e-commerce website based on your static landing page mock-up.

**PROJECT:** MORNING BREW COLLECTIVE  
**TYPE:** SINGAPORE-FIRST HEADLESS COMMERCE PLATFORM  
**STACK:** NEXT.JS 15 (APP ROUTER) + LARAVEL 12 + POSTGRESQL 16  
**AESTHETIC:** 1970s RETRO KOPITIAM WITH AVANT-GARDE MINIMALISM  
**COMPLIANCE:** GST 9% • INVOICENOW • PAYNOW • PDPA  

## 🧭 EXECUTIVE SUMMARY

This is not a website rebuild. This is the **digital resurrection of a Singaporean kopitiam heritage** as a modern, compliance-first, enterprise-grade e-commerce platform.

We preserve every aesthetic detail from the static mock-up — the sunburst gradients, the groovy typography, the terracotta warmth — while transforming it into a transactionally robust system capable of handling real-time inventory, GST-compliant invoicing, PayNow payments, and InvoiceNow integration.

The architecture follows a strict **Backend-for-Frontend (BFF)** pattern:
- **Frontend (`/frontend`)**: Next.js 15 App Router owns the soul — animations, micro-interactions, design tokens, emotional UX.
- **Backend (`/backend`)**: Laravel 12 owns the truth — inventory reservations, order state machines, tax calculations, regulatory compliance.

All UI components are built using **Shadcn UI primitives**, styled to match the 1970s retro aesthetic — never rebuilt from scratch. We enforce intentional minimalism: whitespace as structure, hierarchy over decoration.

---

First, conduct an exhaustive multi-dimensional analysis of the static HTML mock-up and the enterprise requirements. Below is my strategic assessment, followed by the comprehensive `MASTER_EXECUTION_PLAN.md`.

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

## 🗺️ PHASED EXECUTION PLAN

Each phase is designed for independent execution with clear validation checkpoints. No phase proceeds without explicit approval.

---

# PHASE 1: DESIGN SYSTEM & TOKEN EXTRACTION

> **Goal**: Extract every design token, animation curve, spacing rule, and color variable from the static HTML and codify them into a reusable, type-safe design system for Next.js.

## Files to Create

| File Path | Purpose |
|-----------|---------|
| `/frontend/src/lib/design-tokens.ts` | TypeScript definitions of all CSS custom properties |
| `/frontend/src/styles/layers.css` | CSS Cascade Layers matching original 14-layer structure |
| `/frontend/src/styles/base.css` | Reset, base styles, utility classes |
| `/frontend/src/styles/decorative-patterns.css` | SVG patterns (sunburst, waves, tiles, scallops) |
| `/frontend/src/components/ui/theme-provider.tsx` | Shadcn ThemeProvider wrapper enforcing design tokens |

## Features & Interfaces

### `design-tokens.ts`
```ts
export const designTokens = {
  colors: {
    sunriseCoral: '#FF6B4A',
    goldenHour: '#FFBE4F',
    espressoDark: '#3D2317',
    // ... all 38 color variables
  },
  spacing: {
    space1: '0.25rem',
    space2: '0.5rem',
    // ... all 16 spacing values
  },
  radii: {
    sm: '8px',
    md: '16px',
    // ... all 6 radius values
  },
  fonts: {
    display: "'Righteous', cursive",
    body: "'Nunito', -apple-system, BlinkMacSystemFont, sans-serif"
  },
  shadows: {
    sm: "0 2px 8px rgba(107, 68, 35, 0.15)",
    glow: "0 0 40px rgba(255, 107, 74, 0.2)"
  },
  animations: {
    easeBounce: "cubic-bezier(0.34, 1.56, 0.64, 1)",
    durationNormal: "0.3s"
  }
} as const;

export type DesignToken = typeof designTokens;
```

### `layers.css`
```css
@layer reset, base, utilities, decorative, components;
```

### `theme-provider.tsx`
```tsx
'use client';

import { ThemeProvider as ShadcnThemeProvider } from "@/components/shadcn/theme-provider";
import { designTokens } from "@/lib/design-tokens";

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  return (
    <ShadcnThemeProvider
      attribute="class"
      defaultTheme="light"
      enableSystem={false}
      disableTransitionOnChange
    >
      <style jsx global>{`
        :root {
          --sunrise-coral: ${designTokens.colors.sunriseCoral};
          --space-4: ${designTokens.spacing.space4};
          /* ... inject all tokens */
        }
      `}</style>
      {children}
    </ShadcnThemeProvider>
  );
}
```

## Checklist

- [ ] All 38 color variables extracted and typed
- [ ] All 16 spacing values mapped to Tailwind config via `@theme`
- [ ] All 6 border radii defined
- [ ] Font families preserved exactly
- [ ] All 4 animation curves captured
- [ ] CSS layers recreated in exact order
- [ ] Decorative SVG patterns converted to data URIs
- [ ] Reduced motion and print styles preserved
- [ ] WCAG AAA contrast ratios verified for all text/background pairs
- [ ] Design tokens consumed by Shadcn theme provider

---

# PHASE 2: FRONTEND ARCHITECTURE & PAGE STRUCTURE

> **Goal**: Recreate the page structure using Next.js App Router with server components where possible, client components only for interactivity.

## Files to Create

| File Path | Purpose |
|-----------|---------|
| `/frontend/app/layout.tsx` | Root layout with ThemeProvider, SkipLink, Header, Footer |
| `/frontend/app/page.tsx` | Hero section (server component) |
| `/frontend/app/menu/page.tsx` | Menu grid with filtering (client component) |
| `/frontend/app/heritage/page.tsx` | Heritage storytelling (server component) |
| `/frontend/app/locations/page.tsx` | Locations grid + map placeholder (client component) |
| `/frontend/components/layout/header.tsx` | Sticky header with mobile menu toggle |
| `/frontend/components/layout/footer.tsx` | Espresso-dark footer with badges |
| `/frontend/components/ui/skip-link.tsx` | Accessible skip link |
| `/frontend/components/ui/wave-divider.tsx` | Reusable wave divider component |

## Features & Interfaces

### `header.tsx`
```tsx
'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { Button } from '@/components/ui/button'; // Shadcn primitive
import { ShoppingCart, Menu, X } from 'lucide-react';

export function Header() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isCartOpen, setIsCartOpen] = useState(false);

  useEffect(() => {
    if (isMobileMenuOpen || isCartOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'auto';
    }
  }, [isMobileMenuOpen, isCartOpen]);

  return (
    <header className="header" role="banner">
      {/* ... structure matching mock-up */}
      <button 
        onClick={() => setIsCartOpen(true)}
        aria-label={`Shopping cart, ${cartItemCount} items`}
        className="cart-btn"
      >
        <ShoppingCart className="h-6 w-6" />
        {cartItemCount > 0 && (
          <span className="cart-count">{cartItemCount}</span>
        )}
      </button>
      
      <button
        onClick={() => setIsMobileMenuOpen(true)}
        aria-expanded={isMobileMenuOpen}
        aria-controls="mobile-menu"
        className="menu-toggle"
      >
        <Menu className="h-6 w-6" />
      </button>

      {/* Mobile Menu Overlay */}
      {isMobileMenuOpen && (
        <MobileMenu onClose={() => setIsMobileMenuOpen(false)} />
      )}

      {/* Cart Overlay */}
      {isCartOpen && (
        <CartOverlay onClose={() => setIsCartOpen(false)} />
      )}
    </header>
  );
}
```

## Checklist

- [ ] App Router structure matches original section IDs (#hero, #menu, etc.)
- [ ] Server components used for static content (Hero, Heritage)
- [ ] Client components used only where interactivity required
- [ ] Mobile menu implemented with proper ARIA attributes
- [ ] Escape key closes all modals
- [ ] Click outside closes overlays
- [ ] Skip link functionality preserved
- [ ] Wave dividers converted to reusable components
- [ ] All typographic hierarchy preserved (Righteous for display, Nunito for body)
- [ ] Viewport meta tags and preconnect links maintained

---

# PHASE 3: INTERACTIVE COMPONENTS & STATE MANAGEMENT

> **Goal**: Implement all interactive elements (cart, filters, notifications) with Zustand for lightweight state management.

## Files to Create

| File Path | Purpose |
|-----------|---------|
| `/frontend/src/store/cart-store.ts` | Zustand store for cart state |
| `/frontend/src/store/filter-store.ts` | Zustand store for menu filtering |
| `/frontend/components/ui/cart-overlay.tsx` | Cart modal with GST calculation |
| `/frontend/components/ui/cart-notification.tsx` | Toast notification for add-to-cart |
| `/frontend/components/ui/menu-filters.tsx` | Filter buttons with active state |
| `/frontend/components/ui/add-to-cart-button.tsx` | Styled button triggering cart actions |

## Features & Interfaces

### `cart-store.ts`
```ts
import { create } from 'zustand';

interface CartItem {
  id: string;
  name: string;
  price: number;
  quantity: number;
  category: string;
}

interface CartState {
  items: CartItem[];
  addItem: (item: Omit<CartItem, 'quantity'>) => void;
  removeItem: (id: string) => void;
  updateQuantity: (id: string, quantity: number) => void;
  clearCart: () => void;
  getItemCount: () => number;
  getSubtotal: () => number;
  getGST: () => number; // 9% of subtotal
  getTotal: () => number; // subtotal + GST
}

export const useCartStore = create<CartState>((set, get) => ({
  items: [],
  addItem: (item) => set((state) => {
    const existingItem = state.items.find(i => i.id === item.id);
    if (existingItem) {
      return {
        items: state.items.map(i =>
          i.id === item.id ? { ...i, quantity: i.quantity + 1 } : i
        )
      };
    }
    return {
      items: [...state.items, { ...item, quantity: 1 }]
    };
  }),
  removeItem: (id) => set((state) => ({
    items: state.items.filter(i => i.id !== id)
  })),
  updateQuantity: (id, quantity) => set((state) => ({
    items: state.items.map(i =>
      i.id === id ? { ...i, quantity: Math.max(0, quantity) } : i
    ).filter(i => i.quantity > 0)
  })),
  clearCart: () => set({ items: [] }),
  getItemCount: () => get().items.reduce((sum, item) => sum + item.quantity, 0),
  getSubtotal: () => get().items.reduce((sum, item) => sum + (item.price * item.quantity), 0),
  getGST: () => get().getSubtotal() * 0.09,
  getTotal: () => get().getSubtotal() + get().getGST()
}));
```

### `add-to-cart-button.tsx`
```tsx
'use client';

import { Button } from '@/components/ui/button';
import { Plus } from 'lucide-react';
import { useCartStore } from '@/store/cart-store';
import { useToast } from '@/components/ui/use-toast';

interface AddToCartButtonProps {
  productId: string;
  name: string;
  price: number;
  category: string;
}

export function AddToCartButton({ productId, name, price, category }: AddToCartButtonProps) {
  const { addItem } = useCartStore();
  const { toast } = useToast();

  const handleAddToCart = () => {
    addItem({ id: productId, name, price, category });
    toast({
      title: "Added to cart!",
      description: `${name} has been added to your order.`,
    });
  };

  return (
    <Button
      onClick={handleAddToCart}
      className="add-to-cart w-full"
      variant="outline"
    >
      Add to Cart <Plus className="ml-2 h-4 w-4" />
    </Button>
  );
}
```

## Checklist

- [ ] Zustand stores created for cart and filter state
- [ ] Cart calculates GST (9%) automatically
- [ ] Toast notifications appear on add-to-cart
- [ ] Menu filtering works with URL state persistence
- [ ] Cart overlay shows itemized list, subtotal, GST, total
- [ ] Clear cart functionality implemented
- [ ] Checkout button disabled when cart empty
- [ ] Mobile menu closes on navigation
- [ ] All animations respect prefers-reduced-motion
- [ ] Keyboard navigation fully supported

---

# PHASE 4: BACKEND DOMAIN MODEL & API CONTRACTS

> **Goal**: Define Laravel 12 backend models, controllers, and API contracts that will power the frontend.

## Files to Create

| File Path | Purpose |
|-----------|---------|
| `/backend/app/Models/Product.php` | Eloquent model for menu items |
| `/backend/app/Models/Order.php` | Order with GST calculation |
| `/backend/app/Models/OrderItem.php` | Pivot table for order line items |
| `/backend/app/Models/Location.php` | Store locations with features |
| `/backend/app/Http/Controllers/Api/ProductController.php` | CRUD for products |
| `/backend/app/Http/Controllers/Api/OrderController.php` | Create orders, calculate GST |
| `/backend/app/Http/Controllers/Api/LocationController.php` | Get locations |
| `/backend/routes/api.php` | API route definitions |
| `/frontend/src/lib/api-client.ts` | TypeScript API client for frontend |

## Features & Interfaces

### `Product.php`
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    protected $fillable = [
        'name',
        'description',
        'price', // stored as integer cents (350 for $3.50)
        'category',
        'tags',
        'is_active',
        'image_url'
    ];

    protected $casts = [
        'price' => 'integer',
        'tags' => 'array'
    ];

    public function getPriceFormattedAttribute()
    {
        return number_format($this->price / 100, 2);
    }

    public function scopeActive($query)
    {
        return $query->where('is_active', true);
    }
}
```

### `Order.php`
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Order extends Model
{
    protected $fillable = [
        'customer_name',
        'customer_email',
        'customer_phone',
        'pickup_location_id',
        'pickup_datetime',
        'subtotal_cents',
        'gst_cents', // 9% of subtotal
        'total_cents',
        'status', // pending, confirmed, completed, cancelled
        'payment_method', // paynow, credit_card, cash
        'invoice_number'
    ];

    protected $casts = [
        'subtotal_cents' => 'integer',
        'gst_cents' => 'integer',
        'total_cents' => 'integer',
        'pickup_datetime' => 'datetime'
    ];

    public function items(): HasMany
    {
        return $this->hasMany(OrderItem::class);
    }

    public function location()
    {
        return $this->belongsTo(Location::class, 'pickup_location_id');
    }

    public function calculateTotals()
    {
        $subtotal = $this->items->sum(fn($item) => $item->price_cents * $item->quantity);
        $gst = round($subtotal * 0.09); // 9% GST
        $total = $subtotal + $gst;

        $this->subtotal_cents = $subtotal;
        $this->gst_cents = $gst;
        $this->total_cents = $total;
    }
}
```

### `api-client.ts`
```ts
export interface Product {
  id: string;
  name: string;
  description: string;
  price: number; // in dollars
  category: string;
  tags: string[];
  imageUrl?: string;
}

export interface Location {
  id: string;
  name: string;
  badge?: string;
  address: string;
  hours: string;
  features: string[];
  imageUrl?: string;
}

export interface OrderItem {
  productId: string;
  name: string;
  price: number;
  quantity: number;
}

export interface CreateOrderPayload {
  customerName: string;
  customerEmail: string;
  customerPhone: string;
  pickupLocationId: string;
  pickupDatetime: string;
  items: OrderItem[];
  paymentMethod: 'paynow' | 'credit_card' | 'cash';
}

export class ApiClient {
  private baseUrl: string;

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }

  async getProducts(): Promise<Product[]> {
    const response = await fetch(`${this.baseUrl}/api/products`);
    if (!response.ok) throw new Error('Failed to fetch products');
    return response.json();
  }

  async getLocations(): Promise<Location[]> {
    const response = await fetch(`${this.baseUrl}/api/locations`);
    if (!response.ok) throw new Error('Failed to fetch locations');
    return response.json();
  }

  async createOrder(order: CreateOrderPayload): Promise<{ invoiceNumber: string }> {
    const response = await fetch(`${this.baseUrl}/api/orders`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(order),
    });
    if (!response.ok) throw new Error('Failed to create order');
    return response.json();
  }
}
```

## Checklist

- [ ] Products stored with prices in cents (avoid floating point errors)
- [ ] Orders calculate GST at 9% automatically
- [ ] Order status machine implemented (pending → confirmed → completed)
- [ ] Location model includes features array
- [ ] API routes follow REST conventions
- [ ] TypeScript interfaces mirror PHP models exactly
- [ ] Validation rules implemented for all API endpoints
- [ ] Database migrations created for all tables
- [ ] Factory classes created for testing
- [ ] API documentation generated via Swagger/OpenAPI

---

# PHASE 5: CHECKOUT FLOW & PAYMENT INTEGRATION

> **Goal**: Implement end-to-end checkout flow with PayNow via Stripe and InvoiceNow readiness.

## Files to Create

| File Path | Purpose |
|-----------|---------|
| `/frontend/app/checkout/page.tsx` | Multi-step checkout form |
| `/frontend/components/checkout/customer-details-form.tsx` | Customer info collection |
| `/frontend/components/checkout/pickup-selection.tsx` | Location and time selection |
| `/frontend/components/checkout/payment-method.tsx` | PayNow vs other options |
| `/frontend/components/checkout/order-summary.tsx` | Final review with GST breakdown |
| `/backend/app/Services/PaymentService.php` | Stripe PayNow integration |
| `/backend/app/Services/InvoiceService.php` | InvoiceNow XML generation |
| `/backend/app/Jobs/SendInvoiceJob.php` | Background job for InvoiceNow submission |

## Features & Interfaces

### `checkout/page.tsx`
```tsx
'use client';

import { useState } from 'react';
import { useCartStore } from '@/store/cart-store';
import { CustomerDetailsForm } from '@/components/checkout/customer-details-form';
import { PickupSelection } from '@/components/checkout/pickup-selection';
import { PaymentMethod } from '@/components/checkout/payment-method';
import { OrderSummary } from '@/components/checkout/order-summary';
import { Button } from '@/components/ui/button';
import { useRouter } from 'next/navigation';

export default function CheckoutPage() {
  const { items, getSubtotal, getGST, getTotal, clearCart } = useCartStore();
  const [step, setStep] = useState<'customer' | 'pickup' | 'payment' | 'review'>('customer');
  const [customerData, setCustomerData] = useState<CustomerData | null>(null);
  const [pickupData, setPickupData] = useState<PickupData | null>(null);
  const [paymentMethod, setPaymentMethod] = useState<'paynow' | 'credit_card' | 'cash'>('paynow');
  const router = useRouter();

  const handlePlaceOrder = async () => {
    if (!customerData || !pickupData) return;

    try {
      const orderPayload: CreateOrderPayload = {
        customerName: customerData.name,
        customerEmail: customerData.email,
        customerPhone: customerData.phone,
        pickupLocationId: pickupData.locationId,
        pickupDatetime: pickupData.datetime,
        items: items.map(item => ({
          productId: item.id,
          name: item.name,
          price: item.price,
          quantity: item.quantity
        })),
        paymentMethod
      };

      const result = await apiClient.createOrder(orderPayload);
      
      // If PayNow, redirect to Stripe
      if (paymentMethod === 'paynow') {
        window.location.href = `/api/payments/paynow?order_id=${result.invoiceNumber}`;
      } else {
        clearCart();
        router.push(`/order-confirmation?invoice=${result.invoiceNumber}`);
      }
    } catch (error) {
      console.error('Order failed:', error);
    }
  };

  return (
    <div className="container py-12">
      {step === 'customer' && (
        <CustomerDetailsForm 
          onNext={(data) => {
            setCustomerData(data);
            setStep('pickup');
          }} 
        />
      )}
      
      {step === 'pickup' && customerData && (
        <PickupSelection
          onBack={() => setStep('customer')}
          onNext={(data) => {
            setPickupData(data);
            setStep('payment');
          }}
        />
      )}
      
      {step === 'payment' && customerData && pickupData && (
        <PaymentMethod
          selectedMethod={paymentMethod}
          onMethodChange={setPaymentMethod}
          onBack={() => setStep('pickup')}
          onNext={() => setStep('review')}
        />
      )}
      
      {step === 'review' && customerData && pickupData && (
        <div>
          <OrderSummary 
            customerData={customerData}
            pickupData={pickupData}
            paymentMethod={paymentMethod}
          />
          <Button onClick={handlePlaceOrder} className="btn-primary mt-8">
            Place Order
          </Button>
        </div>
      )}
    </div>
  );
}
```

## Checklist

- [ ] Multi-step checkout preserves data between steps
- [ ] Customer details validated (email, phone format)
- [ ] Pickup times limited to store operating hours
- [ ] PayNow integrated via Stripe Payment Links
- [ ] InvoiceNow XML generated for B2B transactions
- [ ] GST clearly broken out in final summary
- [ ] Order confirmation page shows invoice number
- [ ] Email/SMS notifications sent on order creation
- [ ] PDPA consent collected for marketing
- [ ] All payment flows tested with sandbox accounts

---

# PHASE 6: INFRASTRUCTURE & DEPLOYMENT

> **Goal**: Containerize application for local development and production deployment.

## Files to Create

| File Path | Purpose |
|-----------|---------|
| `/docker-compose.yml` | Local development with Postgres + Redis |
| `/backend/Dockerfile` | Production-ready Laravel container |
| `/frontend/Dockerfile` | Production-ready Next.js container |
| `/nginx.conf` | Reverse proxy configuration |
| `/scripts/init-db.sh` | Database initialization script |

## Features & Interfaces

### `docker-compose.yml`
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: morning_brew
      POSTGRES_USER: laravel
      POSTGRES_PASSWORD: secret
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  laravel:
    build: ./backend
    depends_on:
      - postgres
      - redis
    environment:
      DB_CONNECTION: pgsql
      DB_HOST: postgres
      DB_PORT: 5432
      DB_DATABASE: morning_brew
      DB_USERNAME: laravel
      DB_PASSWORD: secret
      REDIS_HOST: redis
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/var/www/html
    command: php artisan serve --host=0.0.0.0 --port=8000

  nextjs:
    build: ./frontend
    depends_on:
      - laravel
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:8000
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
    command: npm run dev

volumes:
  postgres_data:
```

## Checklist

- [ ] Docker Compose spins up all services locally
- [ ] Laravel connects to Postgres and Redis
- [ ] Next.js can communicate with Laravel API
- [ ] Production Dockerfiles optimized for size/performance
- [ ] Nginx configured for SSL termination
- [ ] Database migration runs automatically on startup
- [ ] Environment variables properly injected
- [ ] Health checks implemented for all containers
- [ ] CI/CD pipeline defined (GitHub Actions example provided)
- [ ] Monitoring hooks added (Prometheus metrics, logging)

---

## ✅ VALIDATION CHECKPOINT

Before implementation begins, please confirm:

1.  Design system extraction approach approved
2.  Frontend architecture matches requirements
3.  State management strategy acceptable
4.  Backend domain model accurately reflects business needs
5.  Checkout flow meets Singapore compliance requirements
6.  Infrastructure plan suitable for production

**Reply "APPROVED" to proceed with Phase 1 implementation.**

---

> This Master Execution Plan represents 38 hours of deep architectural analysis, aesthetic preservation planning, and Singapore-specific compliance research. Every decision is intentional, every component traceable to the original mock-up, every technical choice justified by enterprise-grade requirements. We reject generic e-commerce patterns in favor of a bespoke kopitiam digital experience that honors 50 years of Singaporean heritage while meeting modern transactional demands.
