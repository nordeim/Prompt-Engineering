╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   PROJECT: MORNING BREW COLLECTIVE                                            ║
║   TYPE: SINGAPORE-FIRST HEADLESS COMMERCE PLATFORM                            ║
║   STACK: NEXT.JS 15 (APP ROUTER) + LARAVEL 12 + POSTGRESQL 16                 ║
║   AESTHETIC: 1970s RETRO KOPITIAM WITH AVANT-GARDE MINIMALISM                 ║
║   COMPLIANCE: GST 9% • INVOICENOW • PAYNOW • PDPA                             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

🧭 EXECUTIVE SUMMARY
This is not a website rebuild. This is the digital resurrection of a Singaporean kopitiam heritage as a modern, compliance-first, enterprise-grade e-commerce platform.

We preserve every aesthetic detail from the static mock-up — the sunburst gradients, the groovy typography, the terracotta warmth — while transforming it into a transactionally robust system capable of handling real-time inventory, GST-compliant invoicing, PayNow payments, and InvoiceNow integration.

The architecture follows a strict Backend-for-Frontend (BFF) pattern:

Frontend (/frontend): Next.js 15 App Router owns the soul — animations, micro-interactions, design tokens, emotional UX.
Backend (/backend): Laravel 12 owns the truth — inventory reservations, order state machines, tax calculations, regulatory compliance.
All UI components are built using Shadcn UI primitives, styled to match the 1970s retro aesthetic — never rebuilt from scratch. We enforce intentional minimalism: whitespace as structure, hierarchy over decoration.

🗺️ PHASED EXECUTION PLAN
Each phase is designed for independent execution with clear validation checkpoints. No phase proceeds without explicit approval.

PHASE 1: DESIGN SYSTEM & TOKEN EXTRACTION
Goal: Extract every design token, animation curve, spacing rule, and color variable from the static HTML and codify them into a reusable, type-safe design system for Next.js.

Files to Create
File Path	Purpose
/frontend/src/lib/design-tokens.ts	TypeScript definitions of all CSS custom properties
/frontend/src/styles/layers.css	CSS Cascade Layers matching original 14-layer structure
/frontend/src/styles/base.css	Reset, base styles, utility classes
/frontend/src/styles/decorative-patterns.css	SVG patterns (sunburst, waves, tiles, scallops)
/frontend/src/components/ui/theme-provider.tsx	Shadcn ThemeProvider wrapper enforcing design tokens
Features & Interfaces
design-tokens.ts
TypeScript

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
layers.css
CSS

@layer reset, base, utilities, decorative, components;
theme-provider.tsx
React

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
Checklist
 All 38 color variables extracted and typed
 All 16 spacing values mapped to Tailwind config via @theme
 All 6 border radii defined
 Font families preserved exactly
 All 4 animation curves captured
 CSS layers recreated in exact order
 Decorative SVG patterns converted to data URIs
 Reduced motion and print styles preserved
 WCAG AAA contrast ratios verified for all text/background pairs
 Design tokens consumed by Shadcn theme provider
PHASE 2: FRONTEND ARCHITECTURE & PAGE STRUCTURE
Goal: Recreate the page structure using Next.js App Router with server components where possible, client components only for interactivity.

Files to Create
File Path	Purpose
/frontend/app/layout.tsx	Root layout with ThemeProvider, SkipLink, Header, Footer
/frontend/app/page.tsx	Hero section (server component)
/frontend/app/menu/page.tsx	Menu grid with filtering (client component)
/frontend/app/heritage/page.tsx	Heritage storytelling (server component)
/frontend/app/locations/page.tsx	Locations grid + map placeholder (client component)
/frontend/components/layout/header.tsx	Sticky header with mobile menu toggle
/frontend/components/layout/footer.tsx	Espresso-dark footer with badges
/frontend/components/ui/skip-link.tsx	Accessible skip link
/frontend/components/ui/wave-divider.tsx	Reusable wave divider component
Features & Interfaces
header.tsx
React

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
Checklist
 App Router structure matches original section IDs (#hero, #menu, etc.)
 Server components used for static content (Hero, Heritage)
 Client components used only where interactivity required
 Mobile menu implemented with proper ARIA attributes
 Escape key closes all modals
 Click outside closes overlays
 Skip link functionality preserved
 Wave dividers converted to reusable components
 All typographic hierarchy preserved (Righteous for display, Nunito for body)
 Viewport meta tags and preconnect links maintained
PHASE 3: INTERACTIVE COMPONENTS & STATE MANAGEMENT
Goal: Implement all interactive elements (cart, filters, notifications) with Zustand for lightweight state management.

Files to Create
File Path	Purpose
/frontend/src/store/cart-store.ts	Zustand store for cart state
/frontend/src/store/filter-store.ts	Zustand store for menu filtering
/frontend/components/ui/cart-overlay.tsx	Cart modal with GST calculation
/frontend/components/ui/cart-notification.tsx	Toast notification for add-to-cart
/frontend/components/ui/menu-filters.tsx	Filter buttons with active state
/frontend/components/ui/add-to-cart-button.tsx	Styled button triggering cart actions
Features & Interfaces
cart-store.ts
TypeScript

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
add-to-cart-button.tsx
React

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
Checklist
 Zustand stores created for cart and filter state
 Cart calculates GST (9%) automatically
 Toast notifications appear on add-to-cart
 Menu filtering works with URL state persistence
 Cart overlay shows itemized list, subtotal, GST, total
 Clear cart functionality implemented
 Checkout button disabled when cart empty
 Mobile menu closes on navigation
 All animations respect prefers-reduced-motion
 Keyboard navigation fully supported
PHASE 4: BACKEND DOMAIN MODEL & API CONTRACTS
Goal: Define Laravel 12 backend models, controllers, and API contracts that will power the frontend.

Files to Create
File Path	Purpose
/backend/app/Models/Product.php	Eloquent model for menu items
/backend/app/Models/Order.php	Order with GST calculation
/backend/app/Models/OrderItem.php	Pivot table for order line items
/backend/app/Models/Location.php	Store locations with features
/backend/app/Http/Controllers/Api/ProductController.php	CRUD for products
/backend/app/Http/Controllers/Api/OrderController.php	Create orders, calculate GST
/backend/app/Http/Controllers/Api/LocationController.php	Get locations
/backend/routes/api.php	API route definitions
/frontend/src/lib/api-client.ts	TypeScript API client for frontend
Features & Interfaces
Product.php
PHP

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
Order.php
PHP

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Order extends Model
{
    protected $fillable = [
        
