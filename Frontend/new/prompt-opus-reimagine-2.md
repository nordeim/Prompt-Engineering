This is a comprehensive request to reimagine a landing page for a Singapore-based café shop that:

Invokes nostalgia of the 1970s
Uses a refreshing and cheerful color scheme - like aromatic fresh coffee in the morning
Let me analyze the existing codebase first:

Current Design Analysis:

The existing design uses a "Dawn to Noon" gradient color system
Colors: Dawn cream, terracotta sunrise, honey gold, avocado leaf, coffee brown
Typography: Playfair Display (display) + Raleway (body)
The design has heritage storytelling elements
Good accessibility features built in
Cart system is functional
What needs to change for 1970s nostalgia + cheerful/refreshing feel:

Color Palette Rethinking:

1970s colors: harvest gold, avocado green, burnt orange, mustard yellow, chocolate brown, olive, rust
But we need "refreshing and cheerful" like morning coffee
Blend: warm oranges, sunny yellows, warm creams, terracotta, with pops of teal/aqua for freshness
Think: sunshine through café windows, warm wood tones, vintage ceramic colors
Typography for 1970s feel:

Consider fonts that evoke that era: rounded, groovy, or classic serif fonts
Could use: Playfair Display is actually good for heritage feel
Maybe add a display font like "Recoleta", "Fraunces", or something with 70s character
Or a rounded sans-serif for that vintage café vibe
Design Elements for 1970s:

Rounded corners (very 70s)
Geometric patterns (circles, arches, sunbursts)
Hand-drawn or organic shapes
Vintage-style badges and stamps
Textured backgrounds (paper, linen)
Retro illustration style with curved and wavy dividers between sections, starburst motifs
Visual Hierarchy & Layout:

Magazine-style editorial layouts with asymmetric compositions
Large, personality-driven typography
Layered elements through overlapping cards
Vintage photo treatments using sepia and duotone effects
Psychological Impact:

Warmth creates comfort and nostalgia, while cheerfulness energizes and welcomes visitors
Freshness appeals to the morning routine, and authenticity builds trust through heritage storytelling
I'm designing a landing page that captures 1970s Singapore kopitiam aesthetics with cheerful, warm, refreshing colors while maintaining full functionality and improving accessibility. The goal is to deliver an emotional, nostalgic experience with genuine personality rather than generic design.

For the color direction, I'm drawing from "Retro-Tropical Warmth"—sunrise orange (#FF8C42) for energy, warm mustard yellow (#E5B25D) as a 70s staple, cream and ivory (#FFF8E7) for vintage warmth, teak brown (#6B4423) echoing kopitiam wood, vintage teal (#4A7C7E) as a refreshing 70s accent, and terracotta (#C65D3B) to round out the palette.

The visual language includes curved and scalloped edges, sunburst patterns, retro badge styling, hand-drawn line art, rounded rectangles, stacked card layouts, and decorative borders inspired by 70s kopitiam tiles. For typography, I'm considering Fraunces for its variable 70s personality in display contexts, while keeping Raleway or exploring rounder alternatives for body text.

The redesigned version shifts toward a more playful, rounded aesthetic with bolder color blocking and 70s decorative elements like sunbursts, distinguishing it from the original's more restrained approach.

Morning Brew Collective — 1970s Retro-Tropical Reimagination
Executive Summary
I will deliver a complete reimagination of your café landing page that fuses 1970s Singaporean kopitiam nostalgia with a cheerful, sun-drenched morning coffee aesthetic. This isn't a refresh—it's a conceptual transformation that honors the era's warmth while feeling utterly fresh.

Phase 1: Deep Analysis & Conceptual Direction
Design Philosophy: "Sunrise at the Kopitiam"
The Psychological Narrative:
Imagine Singapore, 1973. The morning sun cuts through louvered shutters, casting warm stripes across formica tables. Uncles read Chinese newspapers over kopi, steam rising in golden light. There's the clatter of ceramic on marble, the hiss of the coffee sock being pulled. This is the sensory memory we're encoding.

Aesthetic Pillars:

Dimension	Direction	Justification
Color	Harvest Gold, Burnt Sienna, Vintage Teal, Warm Cream	70s color theory + coffee warmth + refreshing contrast
Typography	Rounded serifs + Humanist sans	Period authenticity meets readability
Shape Language	Arches, scallops, sunbursts, rounded rectangles	70s decorative vocabulary—anti-angular
Texture	Linen grain, wood patterns, tile motifs	Tactile nostalgia without noise
Motion	Gentle, organic (like steam rising)	Calm energy, not frenetic
Anti-Generic Commitments
❌ Rejected: Purple gradients, glassmorphism, generic card grids, Inter/Roboto
✅ Embraced: Bold color blocking, asymmetric layouts, hand-crafted feel, distinctive typography

Phase 2: Implementation
Complete Reimagined Landing Page

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Morning Brew Collective - Singapore's authentic kopitiam experience since 1973. Traditional coffee, breakfast, and pastries where the morning ritual lives.">
  <meta name="theme-color" content="#8B4513">
  <title>Morning Brew Collective — Est. 1973 | Singapore's Kopitiam Heritage</title>

  <!-- Preconnect for Performance -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  
  <!-- Typography: Fraunces (70s variable serif) + DM Sans (friendly humanist) -->
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,400;9..144,500;9..144,700;9..144,900&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    /* ═══════════════════════════════════════════════════════════════
       LAYER 0: CSS CUSTOM PROPERTIES — 1970s TROPICAL SUNRISE SYSTEM
       ═══════════════════════════════════════════════════════════════ */
    :root {
      /* ─── PRIMARY PALETTE: Kopitiam Sunrise ─── */
      --clr-sunrise-gold: #E5A84B;
      --clr-burnt-sienna: #C65D3B;
      --clr-harvest-orange: #E07830;
      --clr-vintage-teal: #3D8B8B;
      --clr-deep-teal: #2A6363;
      --clr-kopitiam-brown: #5C3D2E;
      --clr-dark-roast: #3A2318;
      --clr-warm-cream: #FFF8E7;
      --clr-ivory: #FFFDF5;
      --clr-latte: #F5E6D3;
      --clr-terracotta: #D4654A;
      --clr-soft-coral: #F4A261;
      
      /* ─── SEMANTIC COLORS ─── */
      --clr-text-primary: #3A2318;
      --clr-text-secondary: #5C3D2E;
      --clr-text-muted: #8B7355;
      --clr-text-inverse: #FFF8E7;
      --clr-accent: var(--clr-vintage-teal);
      --clr-accent-hover: var(--clr-deep-teal);
      --clr-highlight: var(--clr-sunrise-gold);
      --clr-cta: var(--clr-burnt-sienna);
      --clr-cta-hover: #A84D2F;
      
      /* ─── SURFACE COLORS ─── */
      --surface-light: var(--clr-ivory);
      --surface-warm: var(--clr-latte);
      --surface-cream: var(--clr-warm-cream);
      --surface-dark: var(--clr-kopitiam-brown);
      --surface-darker: var(--clr-dark-roast);
      
      /* ─── DECORATIVE: 70s Tile Pattern (SVG encoded) ─── */
      --pattern-tile: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M30 0 L60 30 L30 60 L0 30 Z' fill='none' stroke='%23E5A84B' stroke-width='0.5' opacity='0.15'/%3E%3Ccircle cx='30' cy='30' r='8' fill='none' stroke='%233D8B8B' stroke-width='0.5' opacity='0.1'/%3E%3C/svg%3E");
      
      --pattern-scallop: url("data:image/svg+xml,%3Csvg width='40' height='20' viewBox='0 0 40 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 20 Q10 0 20 20 Q30 0 40 20' fill='none' stroke='%23E5A84B' stroke-width='1' opacity='0.2'/%3E%3C/svg%3E");
      
      --pattern-sunburst: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='50' cy='50' r='20' fill='%23E5A84B' opacity='0.05'/%3E%3Ccircle cx='50' cy='50' r='35' fill='none' stroke='%23E5A84B' stroke-width='0.5' opacity='0.08'/%3E%3Ccircle cx='50' cy='50' r='48' fill='none' stroke='%23E5A84B' stroke-width='0.3' opacity='0.05'/%3E%3C/svg%3E");
      
      /* ─── TYPOGRAPHY ─── */
      --font-display: 'Fraunces', Georgia, serif;
      --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      
      --text-xs: clamp(0.7rem, 0.65rem + 0.25vw, 0.75rem);
      --text-sm: clamp(0.8rem, 0.75rem + 0.25vw, 0.875rem);
      --text-base: clamp(0.95rem, 0.9rem + 0.25vw, 1.05rem);
      --text-lg: clamp(1.1rem, 1rem + 0.5vw, 1.25rem);
      --text-xl: clamp(1.25rem, 1.1rem + 0.75vw, 1.5rem);
      --text-2xl: clamp(1.5rem, 1.25rem + 1.25vw, 2rem);
      --text-3xl: clamp(1.875rem, 1.5rem + 1.875vw, 2.5rem);
      --text-4xl: clamp(2.25rem, 1.75rem + 2.5vw, 3.25rem);
      --text-5xl: clamp(2.75rem, 2rem + 3.75vw, 4.5rem);
      --text-hero: clamp(3rem, 2.25rem + 3.75vw, 5.5rem);
      
      /* ─── SPACING (8pt base) ─── */
      --space-1: 0.25rem;
      --space-2: 0.5rem;
      --space-3: 0.75rem;
      --space-4: 1rem;
      --space-5: 1.25rem;
      --space-6: 1.5rem;
      --space-8: 2rem;
      --space-10: 2.5rem;
      --space-12: 3rem;
      --space-16: 4rem;
      --space-20: 5rem;
      --space-24: 6rem;
      --space-32: 8rem;
      
      /* ─── RADII: Soft 70s curves ─── */
      --radius-sm: 0.5rem;
      --radius-md: 1rem;
      --radius-lg: 1.5rem;
      --radius-xl: 2rem;
      --radius-2xl: 3rem;
      --radius-full: 9999px;
      --radius-arch: 50% 50% 0 0;
      
      /* ─── SHADOWS: Warm, soft ─── */
      --shadow-sm: 0 2px 8px rgba(92, 61, 46, 0.08);
      --shadow-md: 0 4px 16px rgba(92, 61, 46, 0.12);
      --shadow-lg: 0 8px 32px rgba(92, 61, 46, 0.16);
      --shadow-xl: 0 16px 48px rgba(92, 61, 46, 0.2);
      --shadow-glow: 0 0 40px rgba(229, 168, 75, 0.3);
      
      /* ─── ANIMATION ─── */
      --ease-smooth: cubic-bezier(0.4, 0, 0.2, 1);
      --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
      --ease-out: cubic-bezier(0, 0, 0.2, 1);
      --duration-fast: 150ms;
      --duration-base: 300ms;
      --duration-slow: 500ms;
      --duration-slower: 700ms;
      
      /* ─── LAYOUT ─── */
      --container-max: 1280px;
      --container-narrow: 720px;
      --nav-height: 72px;
      
      /* ─── Z-INDEX ─── */
      --z-base: 1;
      --z-dropdown: 100;
      --z-sticky: 500;
      --z-overlay: 1000;
      --z-modal: 2000;
      --z-toast: 3000;
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 1: CSS RESET & BASE
       ═══════════════════════════════════════════════════════════════ */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    
    html {
      scroll-behavior: smooth;
      -webkit-text-size-adjust: 100%;
    }
    
    body {
      font-family: var(--font-body);
      font-size: var(--text-base);
      line-height: 1.6;
      color: var(--clr-text-primary);
      background: var(--surface-cream);
      min-height: 100vh;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    
    img, svg, video {
      display: block;
      max-width: 100%;
      height: auto;
    }
    
    button {
      font: inherit;
      cursor: pointer;
      border: none;
      background: none;
    }
    
    a {
      color: inherit;
      text-decoration: none;
    }
    
    ul, ol { list-style: none; }
    
    /* Focus styles for keyboard navigation */
    :focus-visible {
      outline: 3px solid var(--clr-accent);
      outline-offset: 3px;
    }
    
    /* Screen reader only utility */
    .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }
    
    /* Skip link */
    .skip-link {
      position: absolute;
      top: -100%;
      left: var(--space-4);
      background: var(--clr-cta);
      color: var(--clr-text-inverse);
      padding: var(--space-3) var(--space-6);
      border-radius: 0 0 var(--radius-md) var(--radius-md);
      font-weight: 600;
      z-index: var(--z-toast);
      transition: top var(--duration-base) var(--ease-smooth);
    }
    .skip-link:focus {
      top: 0;
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 2: LAYOUT UTILITIES
       ═══════════════════════════════════════════════════════════════ */
    .container {
      width: 100%;
      max-width: var(--container-max);
      margin-inline: auto;
      padding-inline: var(--space-6);
    }
    
    .container--narrow {
      max-width: var(--container-narrow);
    }
    
    /* ═══════════════════════════════════════════════════════════════
       LAYER 3: HEADER & NAVIGATION — Retro Bar Style
       ═══════════════════════════════════════════════════════════════ */
    .header {
      position: sticky;
      top: 0;
      z-index: var(--z-sticky);
      background: var(--surface-darker);
      border-bottom: 4px solid var(--clr-sunrise-gold);
    }
    
    .header__inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: var(--nav-height);
      gap: var(--space-6);
    }
    
    /* Logo: Vintage badge style */
    .logo {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      text-decoration: none;
      transition: transform var(--duration-base) var(--ease-spring);
    }
    .logo:hover {
      transform: scale(1.02);
    }
    
    .logo__badge {
      width: 52px;
      height: 52px;
      background: var(--clr-sunrise-gold);
      border-radius: var(--radius-full);
      display: grid;
      place-items: center;
      border: 3px solid var(--clr-warm-cream);
      box-shadow: var(--shadow-md);
    }
    
    .logo__badge-inner {
      font-family: var(--font-display);
      font-size: var(--text-lg);
      font-weight: 900;
      color: var(--surface-darker);
      line-height: 1;
    }
    
    .logo__text {
      display: flex;
      flex-direction: column;
    }
    
    .logo__brand {
      font-family: var(--font-display);
      font-size: var(--text-xl);
      font-weight: 700;
      color: var(--clr-warm-cream);
      line-height: 1.1;
      letter-spacing: -0.02em;
    }
    
    .logo__tagline {
      font-size: var(--text-xs);
      color: var(--clr-sunrise-gold);
      text-transform: uppercase;
      letter-spacing: 0.15em;
      font-weight: 500;
    }
    
    /* Navigation */
    .nav {
      display: none;
    }
    
    @media (min-width: 768px) {
      .nav {
        display: flex;
        gap: var(--space-2);
      }
    }
    
    .nav__link {
      position: relative;
      padding: var(--space-3) var(--space-4);
      font-family: var(--font-display);
      font-size: var(--text-base);
      font-weight: 500;
      color: var(--clr-warm-cream);
      border-radius: var(--radius-full);
      transition: all var(--duration-base) var(--ease-smooth);
    }
    
    .nav__link::before {
      content: '';
      position: absolute;
      inset: 0;
      background: var(--clr-sunrise-gold);
      border-radius: inherit;
      opacity: 0;
      transform: scale(0.8);
      transition: all var(--duration-base) var(--ease-smooth);
      z-index: -1;
    }
    
    .nav__link:hover::before,
    .nav__link:focus-visible::before {
      opacity: 1;
      transform: scale(1);
    }
    
    .nav__link:hover,
    .nav__link:focus-visible {
      color: var(--surface-darker);
    }
    
    /* Header Actions */
    .header__actions {
      display: flex;
      align-items: center;
      gap: var(--space-4);
    }
    
    .cart-btn {
      position: relative;
      width: 44px;
      height: 44px;
      background: rgba(255, 248, 231, 0.1);
      border-radius: var(--radius-full);
      display: grid;
      place-items: center;
      color: var(--clr-warm-cream);
      transition: all var(--duration-base) var(--ease-smooth);
    }
    
    .cart-btn:hover {
      background: var(--clr-sunrise-gold);
      color: var(--surface-darker);
      transform: scale(1.05);
    }
    
    .cart-btn__count {
      position: absolute;
      top: -4px;
      right: -4px;
      min-width: 20px;
      height: 20px;
      background: var(--clr-cta);
      color: white;
      font-size: var(--text-xs);
      font-weight: 700;
      border-radius: var(--radius-full);
      display: grid;
      place-items: center;
      border: 2px solid var(--surface-darker);
    }
    
    /* Mobile Menu Toggle */
    .menu-toggle {
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 5px;
      width: 44px;
      height: 44px;
      padding: 10px;
      background: rgba(255, 248, 231, 0.1);
      border-radius: var(--radius-md);
      transition: background var(--duration-base) var(--ease-smooth);
    }
    
    .menu-toggle:hover {
      background: rgba(255, 248, 231, 0.2);
    }
    
    .menu-toggle__line {
      width: 100%;
      height: 2px;
      background: var(--clr-warm-cream);
      border-radius: var(--radius-full);
      transition: all var(--duration-base) var(--ease-smooth);
      transform-origin: center;
    }
    
    .menu-toggle[aria-expanded="true"] .menu-toggle__line:nth-child(1) {
      transform: rotate(45deg) translate(5px, 5px);
    }
    .menu-toggle[aria-expanded="true"] .menu-toggle__line:nth-child(2) {
      opacity: 0;
      transform: scaleX(0);
    }
    .menu-toggle[aria-expanded="true"] .menu-toggle__line:nth-child(3) {
      transform: rotate(-45deg) translate(5px, -5px);
    }
    
    @media (min-width: 768px) {
      .menu-toggle { display: none; }
    }
    
    /* Mobile Menu */
    .mobile-menu {
      position: fixed;
      inset: 0;
      background: var(--surface-darker);
      z-index: var(--z-modal);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: var(--space-8);
      opacity: 0;
      visibility: hidden;
      transition: all var(--duration-slow) var(--ease-smooth);
    }
    
    .mobile-menu.is-active {
      opacity: 1;
      visibility: visible;
    }
    
    .mobile-menu__close {
      position: absolute;
      top: var(--space-4);
      right: var(--space-4);
      width: 48px;
      height: 48px;
      background: rgba(255, 248, 231, 0.1);
      border-radius: var(--radius-full);
      display: grid;
      place-items: center;
      color: var(--clr-warm-cream);
      font-size: var(--text-2xl);
      transition: all var(--duration-base) var(--ease-smooth);
    }
    
    .mobile-menu__close:hover {
      background: var(--clr-cta);
      transform: rotate(90deg);
    }
    
    .mobile-menu__list {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: var(--space-6);
    }
    
    .mobile-menu__link {
      font-family: var(--font-display);
      font-size: var(--text-3xl);
      font-weight: 700;
      color: var(--clr-warm-cream);
      transition: color var(--duration-base) var(--ease-smooth);
    }
    
    .mobile-menu__link:hover {
      color: var(--clr-sunrise-gold);
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 4: HERO SECTION — Sunrise Through Shutters
       ═══════════════════════════════════════════════════════════════ */
    .hero {
      position: relative;
      min-height: min(90vh, 800px);
      display: flex;
      align-items: center;
      background: 
        linear-gradient(135deg, var(--clr-warm-cream) 0%, var(--clr-latte) 50%, #F0D9B5 100%);
      overflow: hidden;
    }
    
    /* Decorative sunburst background */
    .hero::before {
      content: '';
      position: absolute;
      top: -50%;
      right: -20%;
      width: 120%;
      height: 200%;
      background: var(--pattern-sunburst);
      opacity: 0.6;
      animation: slowRotate 120s linear infinite;
    }
    
    @keyframes slowRotate {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    
    /* Scalloped bottom edge */
    .hero::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 40px;
      background: var(--pattern-scallop);
      background-size: 40px 20px;
      background-repeat: repeat-x;
      background-position: bottom;
    }
    
    .hero__container {
      position: relative;
      z-index: var(--z-base);
      display: grid;
      grid-template-columns: 1fr;
      gap: var(--space-12);
      padding-block: var(--space-16);
    }
    
    @media (min-width: 1024px) {
      .hero__container {
        grid-template-columns: 1fr 1fr;
        align-items: center;
        gap: var(--space-16);
      }
    }
    
    .hero__content {
      max-width: 600px;
    }
    
    /* Vintage badge */
    .hero__badge {
      display: inline-flex;
      align-items: center;
      gap: var(--space-2);
      background: var(--surface-darker);
      color: var(--clr-sunrise-gold);
      padding: var(--space-2) var(--space-4);
      border-radius: var(--radius-full);
      font-family: var(--font-display);
      font-size: var(--text-sm);
      font-weight: 600;
      margin-bottom: var(--space-6);
      box-shadow: var(--shadow-md);
      animation: fadeInUp 0.8s var(--ease-out) both;
    }
    
    .hero__badge-icon {
      font-size: var(--text-lg);
    }
    
    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translateY(20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
    
    .hero__title {
      font-family: var(--font-display);
      font-size: var(--text-hero);
      font-weight: 900;
      line-height: 1.05;
      color: var(--clr-text-primary);
      margin-bottom: var(--space-6);
      animation: fadeInUp 0.8s 0.1s var(--ease-out) both;
    }
    
    .hero__title-accent {
      display: block;
      color: var(--clr-cta);
      font-style: italic;
    }
    
    .hero__subtitle {
      font-size: var(--text-xl);
      color: var(--clr-text-secondary);
      line-height: 1.6;
      margin-bottom: var(--space-8);
      max-width: 50ch;
      animation: fadeInUp 0.8s 0.2s var(--ease-out) both;
    }
    
    .hero__ctas {
      display: flex;
      flex-wrap: wrap;
      gap: var(--space-4);
      margin-bottom: var(--space-12);
      animation: fadeInUp 0.8s 0.3s var(--ease-out) both;
    }
    
    /* Primary CTA: Warm & Bold */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: var(--space-2);
      padding: var(--space-4) var(--space-8);
      font-family: var(--font-display);
      font-size: var(--text-lg);
      font-weight: 600;
      border-radius: var(--radius-full);
      transition: all var(--duration-base) var(--ease-spring);
    }
    
    .btn--primary {
      background: var(--clr-cta);
      color: white;
      box-shadow: var(--shadow-md), 0 4px 0 0 #8B3A25;
    }
    
    .btn--primary:hover {
      background: var(--clr-cta-hover);
      transform: translateY(-2px);
      box-shadow: var(--shadow-lg), 0 6px 0 0 #8B3A25;
    }
    
    .btn--primary:active {
      transform: translateY(2px);
      box-shadow: var(--shadow-sm), 0 2px 0 0 #8B3A25;
    }
    
    .btn--secondary {
      background: transparent;
      color: var(--clr-text-primary);
      border: 3px solid var(--clr-text-primary);
    }
    
    .btn--secondary:hover {
      background: var(--clr-text-primary);
      color: var(--clr-warm-cream);
      transform: translateY(-2px);
    }
    
    /* Stats: Retro counter style */
    .hero__stats {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: var(--space-6);
      animation: fadeInUp 0.8s 0.4s var(--ease-out) both;
    }
    
    .stat {
      text-align: center;
    }
    
    .stat__value {
      display: block;
      font-family: var(--font-display);
      font-size: var(--text-4xl);
      font-weight: 900;
      color: var(--clr-cta);
      line-height: 1;
    }
    
    .stat__label {
      font-size: var(--text-sm);
      color: var(--clr-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      margin-top: var(--space-1);
    }
    
    /* Hero Visual: Coffee Cup Illustration */
    .hero__visual {
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      animation: fadeInUp 0.8s 0.3s var(--ease-out) both;
    }
    
    .hero__illustration {
      position: relative;
      width: 100%;
      max-width: 400px;
      aspect-ratio: 1;
    }
    
    /* Decorative coffee cup using CSS */
    .coffee-cup {
      position: absolute;
      inset: 10%;
      background: var(--clr-warm-cream);
      border-radius: 0 0 50% 50%;
      border: 6px solid var(--clr-kopitiam-brown);
      box-shadow: 
        var(--shadow-xl),
        inset 0 -20px 40px rgba(92, 61, 46, 0.1);
    }
    
    .coffee-cup::before {
      content: '';
      position: absolute;
      top: 10%;
      left: 10%;
      right: 10%;
      height: 40%;
      background: linear-gradient(
        to bottom,
        var(--clr-kopitiam-brown) 0%,
        #7A5240 50%,
        #6B4534 100%
      );
      border-radius: 50% 50% 40% 40%;
    }
    
    /* Handle */
    .coffee-cup::after {
      content: '';
      position: absolute;
      right: -25%;
      top: 20%;
      width: 30%;
      height: 40%;
      border: 6px solid var(--clr-kopitiam-brown);
      border-left: none;
      border-radius: 0 50% 50% 0;
    }
    
    /* Steam animation */
    .steam {
      position: absolute;
      top: 5%;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      gap: var(--space-3);
    }
    
    .steam__particle {
      width: 8px;
      height: 30px;
      background: linear-gradient(
        to top,
        rgba(229, 168, 75, 0.6) 0%,
        rgba(229, 168, 75, 0) 100%
      );
      border-radius: var(--radius-full);
      animation: steam 2s ease-in-out infinite;
    }
    
    .steam__particle:nth-child(2) {
      height: 40px;
      animation-delay: 0.3s;
    }
    
    .steam__particle:nth-child(3) {
      animation-delay: 0.6s;
    }
    
    @keyframes steam {
      0%, 100% {
        opacity: 0;
        transform: translateY(0) scaleY(0.5);
      }
      25% {
        opacity: 1;
        transform: translateY(-10px) scaleY(1);
      }
      75% {
        opacity: 0.5;
        transform: translateY(-30px) scaleY(0.8);
      }
    }
    
    /* Decorative ring around cup */
    .cup-ring {
      position: absolute;
      inset: -5%;
      border: 3px dashed var(--clr-sunrise-gold);
      border-radius: 50%;
      opacity: 0.4;
      animation: spin 30s linear infinite;
    }
    
    @keyframes spin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 5: MENU SECTION — Retro Card Grid
       ═══════════════════════════════════════════════════════════════ */
    .menu-section {
      position: relative;
      background: var(--clr-harvest-orange);
      padding-block: var(--space-20);
      overflow: hidden;
    }
    
    /* Tile pattern overlay */
    .menu-section::before {
      content: '';
      position: absolute;
      inset: 0;
      background: var(--pattern-tile);
      opacity: 0.3;
    }
    
    .menu-section__header {
      text-align: center;
      margin-bottom: var(--space-12);
      position: relative;
    }
    
    .section-title {
      font-family: var(--font-display);
      font-size: var(--text-4xl);
      font-weight: 900;
      color: var(--clr-text-inverse);
      margin-bottom: var(--space-3);
    }
    
    .section-subtitle {
      font-size: var(--text-lg);
      color: rgba(255, 248, 231, 0.85);
      max-width: 45ch;
      margin-inline: auto;
    }
    
    /* Decorative divider */
    .section-divider {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: var(--space-3);
      margin-top: var(--space-6);
    }
    
    .section-divider__line {
      width: 60px;
      height: 2px;
      background: var(--clr-sunrise-gold);
      border-radius: var(--radius-full);
    }
    
    .section-divider__icon {
      font-size: var(--text-2xl);
    }
    
    /* Filter tabs */
    .menu-filters {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: var(--space-3);
      margin-bottom: var(--space-10);
      position: relative;
    }
    
    .filter-btn {
      padding: var(--space-3) var(--space-6);
      font-family: var(--font-display);
      font-size: var(--text-base);
      font-weight: 600;
      color: var(--clr-text-inverse);
      background: rgba(255, 248, 231, 0.15);
      border: 2px solid transparent;
      border-radius: var(--radius-full);
      transition: all var(--duration-base) var(--ease-smooth);
    }
    
    .filter-btn:hover {
      background: rgba(255, 248, 231, 0.25);
    }
    
    .filter-btn.is-active {
      background: var(--clr-sunrise-gold);
      color: var(--surface-darker);
      border-color: var(--clr-sunrise-gold);
    }
    
    /* Menu Grid */
    .menu-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: var(--space-6);
      position: relative;
    }
    
    /* Menu Card: Vintage recipe card style */
    .menu-card {
      background: var(--clr-warm-cream);
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      transition: all var(--duration-base) var(--ease-spring);
      position: relative;
    }
    
    .menu-card:hover {
      transform: translateY(-8px) rotate(-1deg);
      box-shadow: var(--shadow-xl);
    }
    
    /* Decorative corner fold */
    .menu-card::before {
      content: '';
      position: absolute;
      top: 0;
      right: 0;
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, transparent 50%, var(--clr-latte) 50%);
      border-radius: 0 var(--radius-xl) 0 0;
      z-index: 2;
    }
    
    .menu-card__image {
      height: 160px;
      background: linear-gradient(135deg, var(--clr-kopitiam-brown), #7A5240);
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
    }
    
    /* Decorative coffee bean icons */
    .menu-card__image::before {
      content: '☕';
      font-size: 4rem;
      opacity: 0.3;
    }
    
    .menu-card__body {
      padding: var(--space-6);
    }
    
    .menu-card__header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: var(--space-3);
    }
    
    .menu-card__title {
      font-family: var(--font-display);
      font-size: var(--text-xl);
      font-weight: 700;
      color: var(--clr-text-primary);
    }
    
    .menu-card__price {
      font-family: var(--font-display);
      font-size: var(--text-xl);
      font-weight: 900;
      color: var(--clr-cta);
    }
    
    .menu-card__desc {
      font-size: var(--text-sm);
      color: var(--clr-text-muted);
      line-height: 1.5;
      margin-bottom: var(--space-4);
    }
    
    .menu-card__meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: var(--space-4);
    }
    
    .menu-card__tag {
      background: var(--clr-sunrise-gold);
      color: var(--surface-darker);
      padding: var(--space-1) var(--space-3);
      border-radius: var(--radius-full);
      font-size: var(--text-xs);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    
    .menu-card__spice {
      color: var(--clr-harvest-orange);
      font-size: var(--text-sm);
    }
    
    .menu-card__cta {
      width: 100%;
      padding: var(--space-3) var(--space-4);
      background: var(--surface-darker);
      color: var(--clr-text-inverse);
      font-family: var(--font-display);
      font-weight: 600;
      border-radius: var(--radius-md);
      transition: all var(--duration-base) var(--ease-smooth);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: var(--space-2);
    }
    
    .menu-card__cta:hover {
      background: var(--clr-cta);
      transform: scale(1.02);
    }
    
    /* View full menu link */
    .menu-section__footer {
      text-align: center;
      margin-top: var(--space-12);
      position: relative;
    }
    
    .link-arrow {
      display: inline-flex;
      align-items: center;
      gap: var(--space-2);
      font-family: var(--font-display);
      font-size: var(--text-xl);
      font-weight: 600;
      color: var(--clr-text-inverse);
      transition: gap var(--duration-base) var(--ease-spring);
    }
    
    .link-arrow:hover {
      gap: var(--space-4);
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 6: HERITAGE SECTION — Storytelling Editorial
       ═══════════════════════════════════════════════════════════════ */
    .heritage-section {
      position: relative;
      background: var(--clr-sunrise-gold);
      padding-block: var(--space-24);
      overflow: hidden;
    }
    
    /* Wood grain texture */
    .heritage-section::before {
      content: '';
      position: absolute;
      inset: 0;
      background: 
        repeating-linear-gradient(
          90deg,
          transparent,
          transparent 30px,
          rgba(92, 61, 46, 0.03) 30px,
          rgba(92, 61, 46, 0.03) 31px
        );
    }
    
    .heritage__grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: var(--space-12);
    }
    
    @media (min-width: 1024px) {
      .heritage__grid {
        grid-template-columns: 1.2fr 1fr;
        align-items: center;
      }
    }
    
    .heritage__content {
      position: relative;
    }
    
    .heritage__lead {
      font-family: var(--font-display);
      font-size: var(--text-2xl);
      font-weight: 500;
      color: var(--surface-darker);
      line-height: 1.6;
      margin-bottom: var(--space-8);
    }
    
    .drop-cap {
      float: left;
      font-family: var(--font-display);
      font-size: var(--text-5xl);
      font-weight: 900;
      line-height: 0.8;
      color: var(--clr-cta);
      margin-right: var(--space-3);
      margin-top: var(--space-2);
    }
    
    /* Quote callout: Vintage paper style */
    .heritage__quote {
      background: var(--clr-warm-cream);
      padding: var(--space-8);
      border-radius: var(--radius-xl);
      margin: var(--space-8) 0;
      position: relative;
      box-shadow: var(--shadow-md);
      transform: rotate(-1deg);
    }
    
    .heritage__quote::before {
      content: '"';
      position: absolute;
      top: var(--space-4);
      left: var(--space-6);
      font-family: var(--font-display);
      font-size: 5rem;
      line-height: 1;
      color: var(--clr-sunrise-gold);
      opacity: 0.5;
    }
    
    .heritage__quote-text {
      font-family: var(--font-display);
      font-size: var(--text-xl);
      font-style: italic;
      color: var(--clr-text-primary);
      line-height: 1.6;
      margin-bottom: var(--space-4);
      padding-top: var(--space-6);
    }
    
    .heritage__quote-author {
      font-family: var(--font-display);
      font-weight: 700;
      color: var(--clr-cta);
    }
    
    /* Values grid */
    .heritage__values {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: var(--space-6);
      margin-top: var(--space-10);
    }
    
    .value-item {
      text-align: center;
    }
    
    .value-item__icon {
      width: 64px;
      height: 64px;
      background: var(--clr-warm-cream);
      border-radius: var(--radius-full);
      display: grid;
      place-items: center;
      margin-inline: auto;
      margin-bottom: var(--space-3);
      font-size: var(--text-2xl);
      box-shadow: var(--shadow-sm);
    }
    
    .value-item__title {
      font-family: var(--font-display);
      font-size: var(--text-lg);
      font-weight: 700;
      color: var(--surface-darker);
      margin-bottom: var(--space-1);
    }
    
    .value-item__desc {
      font-size: var(--text-sm);
      color: var(--clr-text-secondary);
    }
    
    /* Heritage visual: Vintage photo stack */
    .heritage__visual {
      position: relative;
    }
    
    .photo-stack {
      position: relative;
      max-width: 400px;
      margin-inline: auto;
    }
    
    .photo-frame {
      background: var(--clr-warm-cream);
      padding: var(--space-4);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-lg);
      position: relative;
    }
    
    .photo-frame:nth-child(2) {
      position: absolute;
      top: 10%;
      left: -10%;
      transform: rotate(-5deg);
      z-index: -1;
      opacity: 0.7;
    }
    
    .photo-frame:nth-child(3) {
      position: absolute;
      top: 5%;
      right: -8%;
      transform: rotate(3deg);
      z-index: -2;
      opacity: 0.5;
    }
    
    .photo-frame__image {
      width: 100%;
      aspect-ratio: 4/3;
      background: linear-gradient(135deg, #D4C4A8, #C4B498);
      border-radius: var(--radius-md);
      display: grid;
      place-items: center;
    }
    
    .photo-frame__image-placeholder {
      font-family: var(--font-display);
      font-size: var(--text-3xl);
      color: var(--clr-text-muted);
      opacity: 0.5;
    }
    
    .photo-frame__caption {
      text-align: center;
      margin-top: var(--space-3);
      font-size: var(--text-sm);
      color: var(--clr-text-muted);
      font-style: italic;
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 7: LOCATIONS SECTION — Map & Cards
       ═══════════════════════════════════════════════════════════════ */
    .locations-section {
      position: relative;
      background: var(--clr-vintage-teal);
      padding-block: var(--space-20);
      color: var(--clr-text-inverse);
    }
    
    /* Leaf pattern overlay */
    .locations-section::before {
      content: '';
      position: absolute;
      inset: 0;
      background: 
        radial-gradient(circle at 20% 80%, rgba(255, 248, 231, 0.05) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255, 248, 231, 0.03) 0%, transparent 40%);
    }
    
    .locations-section__header {
      text-align: center;
      margin-bottom: var(--space-12);
      position: relative;
    }
    
    .locations-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: var(--space-6);
      position: relative;
    }
    
    @media (min-width: 768px) {
      .locations-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    
    /* Location Card: Arch-topped retro style */
    .location-card {
      background: rgba(255, 248, 231, 0.1);
      border-radius: var(--radius-2xl) var(--radius-2xl) var(--radius-xl) var(--radius-xl);
      overflow: hidden;
      backdrop-filter: blur(8px);
      transition: all var(--duration-base) var(--ease-spring);
      border: 2px solid rgba(255, 248, 231, 0.15);
    }
    
    .location-card:hover {
      transform: translateY(-8px);
      background: rgba(255, 248, 231, 0.15);
      border-color: var(--clr-sunrise-gold);
    }
    
    .location-card__header {
      padding: var(--space-4) var(--space-5);
      background: rgba(0, 0, 0, 0.2);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    
    .location-card__title {
      font-family: var(--font-display);
      font-size: var(--text-xl);
      font-weight: 700;
    }
    
    .location-card__badge {
      background: var(--clr-sunrise-gold);
      color: var(--surface-darker);
      padding: var(--space-1) var(--space-3);
      border-radius: var(--radius-full);
      font-size: var(--text-xs);
      font-weight: 700;
      text-transform: uppercase;
    }
    
    .location-card__visual {
      height: 140px;
      background: rgba(0, 0, 0, 0.1);
      display: grid;
      place-items: center;
      font-size: 3rem;
      opacity: 0.5;
    }
    
    .location-card__body {
      padding: var(--space-5);
    }
    
    .location-card__address {
      font-weight: 600;
      margin-bottom: var(--space-1);
    }
    
    .location-card__hours {
      font-size: var(--text-sm);
      opacity: 0.8;
      margin-bottom: var(--space-4);
    }
    
    .location-card__features {
      display: flex;
      flex-direction: column;
      gap: var(--space-2);
    }
    
    .feature {
      font-size: var(--text-sm);
      opacity: 0.9;
    }
    
    .location-card__actions {
      padding: var(--space-5);
      padding-top: 0;
      display: flex;
      gap: var(--space-3);
    }
    
    .location-card__btn {
      flex: 1;
      padding: var(--space-3);
      background: rgba(255, 248, 231, 0.1);
      color: var(--clr-text-inverse);
      font-weight: 600;
      font-size: var(--text-sm);
      border-radius: var(--radius-md);
      text-align: center;
      border: 1px solid rgba(255, 248, 231, 0.2);
      transition: all var(--duration-base) var(--ease-smooth);
    }
    
    .location-card__btn:hover {
      background: var(--clr-sunrise-gold);
      color: var(--surface-darker);
      border-color: var(--clr-sunrise-gold);
    }
    
    /* Map placeholder */
    .locations-map {
      margin-top: var(--space-12);
      height: 350px;
      background: rgba(0, 0, 0, 0.2);
      border-radius: var(--radius-2xl);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      gap: var(--space-4);
      border: 2px dashed rgba(255, 248, 231, 0.2);
      position: relative;
    }
    
    .locations-map__title {
      font-family: var(--font-display);
      font-size: var(--text-2xl);
      font-weight: 700;
    }
    
    .locations-map__text {
      opacity: 0.8;
    }
    
    /* Map markers */
    .map-markers {
      display: flex;
      gap: var(--space-8);
      margin-top: var(--space-4);
    }
    
    .map-marker {
      width: 24px;
      height: 24px;
      background: var(--clr-sunrise-gold);
      border-radius: var(--radius-full);
      position: relative;
      animation: pulse 2s ease-in-out infinite;
    }
    
    .map-marker::after {
      content: '';
      position: absolute;
      inset: -8px;
      border: 2px solid var(--clr-sunrise-gold);
      border-radius: var(--radius-full);
      opacity: 0.4;
    }
    
    @keyframes pulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.1); }
    }
    
    /* Delivery CTA */
    .locations-section__footer {
      text-align: center;
      margin-top: var(--space-12);
      position: relative;
    }
    
    .delivery-cta {
      background: rgba(255, 248, 231, 0.1);
      padding: var(--space-8);
      border-radius: var(--radius-2xl);
      backdrop-filter: blur(8px);
      border: 2px solid rgba(255, 248, 231, 0.1);
    }
    
    .delivery-cta__text {
      font-size: var(--text-lg);
      margin-bottom: var(--space-4);
    }
    
    .delivery-cta__brands {
      display: flex;
      justify-content: center;
      gap: var(--space-4);
      flex-wrap: wrap;
    }
    
    .delivery-brand {
      background: var(--clr-warm-cream);
      color: var(--clr-text-primary);
      padding: var(--space-2) var(--space-4);
      border-radius: var(--radius-full);
      font-weight: 600;
      font-size: var(--text-sm);
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 8: FOOTER — Warm & Grounded
       ═══════════════════════════════════════════════════════════════ */
    .footer {
      background: var(--surface-darker);
      color: var(--clr-text-inverse);
      padding-block: var(--space-16) var(--space-8);
      position: relative;
    }
    
    /* Scalloped top edge */
    .footer::before {
      content: '';
      position: absolute;
      top: -19px;
      left: 0;
      right: 0;
      height: 20px;
      background: var(--surface-darker);
      clip-path: polygon(
        0% 100%, 5% 0%, 10% 100%, 15% 0%, 20% 100%, 25% 0%, 30% 100%, 35% 0%, 
        40% 100%, 45% 0%, 50% 100%, 55% 0%, 60% 100%, 65% 0%, 70% 100%, 75% 0%, 
        80% 100%, 85% 0%, 90% 100%, 95% 0%, 100% 100%
      );
    }
    
    .footer__grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: var(--space-10);
      margin-bottom: var(--space-12);
    }
    
    @media (min-width: 768px) {
      .footer__grid {
        grid-template-columns: 2fr repeat(3, 1fr);
      }
    }
    
    .footer__brand {
      max-width: 300px;
    }
    
    .footer__logo {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      margin-bottom: var(--space-4);
    }
    
    .footer__logo-badge {
      width: 48px;
      height: 48px;
      background: var(--clr-sunrise-gold);
      border-radius: var(--radius-full);
      display: grid;
      place-items: center;
      font-family: var(--font-display);
      font-size: var(--text-lg);
      font-weight: 900;
      color: var(--surface-darker);
    }
    
    .footer__logo-text {
      font-family: var(--font-display);
      font-size: var(--text-xl);
      font-weight: 700;
    }
    
    .footer__desc {
      font-size: var(--text-sm);
      opacity: 0.8;
      line-height: 1.6;
    }
    
    .footer__section-title {
      font-family: var(--font-display);
      font-size: var(--text-lg);
      font-weight: 700;
      color: var(--clr-sunrise-gold);
      margin-bottom: var(--space-4);
    }
    
    .footer__links {
      display: flex;
      flex-direction: column;
      gap: var(--space-3);
    }
    
    .footer__link {
      font-size: var(--text-sm);
      opacity: 0.8;
      transition: opacity var(--duration-base) var(--ease-smooth);
    }
    
    .footer__link:hover {
      opacity: 1;
      color: var(--clr-sunrise-gold);
    }
    
    .footer__contact-item {
      font-size: var(--text-sm);
      opacity: 0.8;
      margin-bottom: var(--space-2);
    }
    
    .footer__social {
      display: flex;
      gap: var(--space-3);
      margin-top: var(--space-4);
    }
    
    .footer__social-link {
      width: 40px;
      height: 40px;
      background: rgba(255, 248, 231, 0.1);
      border-radius: var(--radius-full);
      display: grid;
      place-items: center;
      transition: all var(--duration-base) var(--ease-smooth);
    }
    
    .footer__social-link:hover {
      background: var(--clr-sunrise-gold);
      color: var(--surface-darker);
    }
    
    .footer__bottom {
      border-top: 1px solid rgba(255, 248, 231, 0.1);
      padding-top: var(--space-6);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: var(--space-2);
      text-align: center;
    }
    
    .footer__copyright {
      font-size: var(--text-sm);
      opacity: 0.6;
    }
    
    .footer__badges {
      display: flex;
      gap: var(--space-4);
      flex-wrap: wrap;
      justify-content: center;
    }
    
    .footer__badge {
      font-size: var(--text-xs);
      opacity: 0.6;
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 9: CART OVERLAY — Warm Modal
       ═══════════════════════════════════════════════════════════════ */
    .cart-overlay {
      position: fixed;
      inset: 0;
      background: rgba(58, 35, 24, 0.7);
      z-index: var(--z-modal);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: var(--space-4);
      opacity: 0;
      visibility: hidden;
      transition: all var(--duration-base) var(--ease-smooth);
      backdrop-filter: blur(4px);
    }
    
    .cart-overlay[aria-hidden="false"] {
      opacity: 1;
      visibility: visible;
    }
    
    .cart-modal {
      background: var(--clr-warm-cream);
      border-radius: var(--radius-2xl);
      width: 100%;
      max-width: 480px;
      max-height: 90vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-xl);
      transform: translateY(20px) scale(0.95);
      transition: transform var(--duration-base) var(--ease-spring);
    }
    
    .cart-overlay[aria-hidden="false"] .cart-modal {
      transform: translateY(0) scale(1);
    }
    
    .cart-modal__header {
      padding: var(--space-5) var(--space-6);
      background: var(--surface-darker);
      color: var(--clr-text-inverse);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    
    .cart-modal__title {
      font-family: var(--font-display);
      font-size: var(--text-xl);
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: var(--space-3);
    }
    
    .cart-modal__count {
      background: var(--clr-cta);
      padding: var(--space-1) var(--space-3);
      border-radius: var(--radius-full);
      font-size: var(--text-sm);
    }
    
    .cart-modal__close {
      width: 40px;
      height: 40px;
      background: rgba(255, 248, 231, 0.1);
      border-radius: var(--radius-full);
      display: grid;
      place-items: center;
      color: var(--clr-text-inverse);
      font-size: var(--text-xl);
      transition: all var(--duration-base) var(--ease-smooth);
    }
    
    .cart-modal__close:hover {
      background: var(--clr-cta);
    }
    
    .cart-modal__body {
      flex: 1;
      overflow-y: auto;
      padding: var(--space-6);
    }
    
    .cart-empty {
      text-align: center;
      padding: var(--space-12) var(--space-6);
      color: var(--clr-text-muted);
    }
    
    .cart-empty__icon {
      font-size: 4rem;
      margin-bottom: var(--space-4);
      opacity: 0.5;
    }
    
    .cart-empty__text {
      font-size: var(--text-lg);
    }
    
    .cart-items {
      display: flex;
      flex-direction: column;
      gap: var(--space-4);
    }
    
    .cart-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: var(--space-4);
      background: var(--clr-ivory);
      border-radius: var(--radius-lg);
      gap: var(--space-4);
    }
    
    .cart-item__info {
      flex: 1;
    }
    
    .cart-item__name {
      font-family: var(--font-display);
      font-weight: 600;
      color: var(--clr-text-primary);
      margin-bottom: var(--space-1);
    }
    
    .cart-item__price {
      font-size: var(--text-sm);
      color: var(--clr-cta);
      font-weight: 600;
    }
    
    .cart-item__controls {
      display: flex;
      align-items: center;
      gap: var(--space-2);
    }
    
    .qty-btn {
      width: 32px;
      height: 32px;
      background: var(--surface-warm);
      border: 1px solid var(--clr-text-muted);
      border-radius: var(--radius-sm);
      display: grid;
      place-items: center;
      font-weight: bold;
      transition: all var(--duration-fast) var(--ease-smooth);
    }
    
    .qty-btn:hover {
      background: var(--clr-sunrise-gold);
      border-color: var(--clr-sunrise-gold);
    }
    
    .qty-display {
      width: 32px;
      text-align: center;
      font-weight: 600;
    }
    
    .cart-item__remove {
      width: 32px;
      height: 32px;
      color: var(--clr-cta);
      font-size: var(--text-lg);
      display: grid;
      place-items: center;
      transition: color var(--duration-fast) var(--ease-smooth);
    }
    
    .cart-item__remove:hover {
      color: #c0392b;
    }
    
    .cart-modal__summary {
      padding: var(--space-6);
      border-top: 2px dashed var(--clr-text-muted);
      background: var(--clr-latte);
    }
    
    .cart-summary-row {
      display: flex;
      justify-content: space-between;
      margin-bottom: var(--space-2);
      font-size: var(--text-sm);
    }
    
    .cart-summary-row--total {
      font-family: var(--font-display);
      font-size: var(--text-xl);
      font-weight: 700;
      color: var(--clr-cta);
      margin-top: var(--space-4);
      padding-top: var(--space-4);
      border-top: 1px solid var(--clr-text-muted);
    }
    
    .cart-modal__actions {
      padding: var(--space-4) var(--space-6);
      background: var(--clr-warm-cream);
      display: flex;
      gap: var(--space-3);
    }
    
    .cart-btn {
      flex: 1;
      padding: var(--space-4);
      border-radius: var(--radius-md);
      font-family: var(--font-display);
      font-weight: 600;
      transition: all var(--duration-base) var(--ease-smooth);
    }
    
    .cart-btn--clear {
      background: var(--surface-warm);
      color: var(--clr-text-secondary);
      border: 1px solid var(--clr-text-muted);
    }
    
    .cart-btn--clear:hover {
      background: var(--clr-text-secondary);
      color: var(--clr-text-inverse);
    }
    
    .cart-btn--checkout {
      background: var(--clr-cta);
      color: white;
    }
    
    .cart-btn--checkout:hover {
      background: var(--clr-cta-hover);
    }
    
    .cart-btn--checkout:disabled {
      background: var(--clr-text-muted);
      cursor: not-allowed;
      opacity: 0.6;
    }
    
    .cart-modal__footer {
      padding: var(--space-4) var(--space-6);
      text-align: center;
      font-size: var(--text-xs);
      color: var(--clr-text-muted);
      border-top: 1px solid var(--surface-warm);
    }
    
    .payment-badges {
      display: flex;
      justify-content: center;
      gap: var(--space-2);
      margin-top: var(--space-2);
    }
    
    .payment-badge {
      background: var(--clr-ivory);
      padding: var(--space-1) var(--space-2);
      border-radius: var(--radius-sm);
      font-size: var(--text-xs);
      font-weight: 500;
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 10: TOAST NOTIFICATIONS
       ═══════════════════════════════════════════════════════════════ */
    .toast {
      position: fixed;
      bottom: var(--space-6);
      right: var(--space-6);
      background: var(--surface-darker);
      color: var(--clr-text-inverse);
      padding: var(--space-4) var(--space-6);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-xl);
      display: flex;
      align-items: center;
      gap: var(--space-3);
      z-index: var(--z-toast);
      opacity: 0;
      transform: translateY(20px);
      transition: all var(--duration-base) var(--ease-spring);
    }
    
    .toast.is-visible {
      opacity: 1;
      transform: translateY(0);
    }
    
    .toast__icon {
      width: 32px;
      height: 32px;
      background: var(--clr-accent);
      border-radius: var(--radius-full);
      display: grid;
      place-items: center;
      font-weight: bold;
    }
    
    .toast__message {
      font-weight: 500;
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 11: ACCESSIBILITY & MOTION
       ═══════════════════════════════════════════════════════════════ */
    @media (prefers-reduced-motion: reduce) {
      *,
      *::before,
      *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
      
      html {
        scroll-behavior: auto;
      }
    }
    
    /* High contrast mode support */
    @media (prefers-contrast: high) {
      :root {
        --clr-text-primary: #000;
        --clr-text-inverse: #fff;
      }
      
      .btn--primary,
      .menu-card__cta,
      .cart-btn--checkout {
        border: 2px solid currentColor;
      }
    }

    /* ═══════════════════════════════════════════════════════════════
       LAYER 12: PRINT STYLES
       ═══════════════════════════════════════════════════════════════ */
    @media print {
      .header,
      .cart-overlay,
      .mobile-menu,
      .hero__ctas,
      .menu-card__cta,
      .location-card__actions,
      .footer__social {
        display: none !important;
      }
      
      body {
        font-size: 12pt;
        color: #000;
        background: #fff;
      }
      
      .menu-section,
      .heritage-section,
      .locations-section {
        background: #fff;
        color: #000;
      }
    }
  </style>
</head>
<body>
  <a href="#main" class="skip-link">Skip to main content</a>

  <!-- ═══════════════════════════════════════════════════════════════
       HEADER: Retro Coffee Bar Navigation
       ═══════════════════════════════════════════════════════════════ -->
  <header class="header" role="banner">
    <div class="container header__inner">
      
      <!-- Logo: Vintage Badge Style -->
      <a href="/" class="logo" aria-label="Morning Brew Collective - Home">
        <div class="logo__badge">
          <span class="logo__badge-inner">MB</span>
        </div>
        <div class="logo__text">
          <span class="logo__brand">Morning Brew</span>
          <span class="logo__tagline">Est. 1973 · Singapore</span>
        </div>
      </a>

      <!-- Desktop Navigation -->
      <nav class="nav" aria-label="Main navigation">
        <a href="#menu" class="nav__link">Menu</a>
        <a href="#heritage" class="nav__link">Our Story</a>
        <a href="#locations" class="nav__link">Visit Us</a>
        <a href="#order" class="nav__link">Order</a>
      </nav>

      <!-- Header Actions -->
      <div class="header__actions">
        <button type="button" class="cart-btn" aria-label="Shopping cart, 0 items" id="cart-toggle">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="9" cy="21" r="1"/>
            <circle cx="20" cy="21" r="1"/>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
          </svg>
          <span class="cart-btn__count" id="cart-count">0</span>
        </button>

        <button type="button" class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
          <span class="menu-toggle__line"></span>
          <span class="menu-toggle__line"></span>
          <span class="menu-toggle__line"></span>
        </button>
      </div>

    </div>
  </header>

  <!-- Mobile Menu -->
  <div class="mobile-menu" id="mobile-menu" aria-hidden="true">
    <button type="button" class="mobile-menu__close" aria-label="Close menu">×</button>
    <nav aria-label="Mobile navigation">
      <ul class="mobile-menu__list">
        <li><a href="#menu" class="mobile-menu__link">Menu</a></li>
        <li><a href="#heritage" class="mobile-menu__link">Our Story</a></li>
        <li><a href="#locations" class="mobile-menu__link">Visit Us</a></li>
        <li><a href="#order" class="mobile-menu__link">Order</a></li>
      </ul>
    </nav>
  </div>

  <main id="main">

    <!-- ═══════════════════════════════════════════════════════════════
         HERO: Sunrise Through Kopitiam Shutters
         ═══════════════════════════════════════════════════════════════ -->
    <section class="hero" id="hero" aria-labelledby="hero-title">
      <div class="container hero__container">
        
        <div class="hero__content">
          <div class="hero__badge">
            <span class="hero__badge-icon">☕</span>
            <span>Serving since 1973</span>
          </div>

          <h1 id="hero-title" class="hero__title">
            Where Every <span class="hero__title-accent">Morning Begins</span>
          </h1>

          <p class="hero__subtitle">
            Step into Singapore's living heritage. Our kopi, pulled fresh using recipes from Uncle Lim's 1970s kopitiam, brings generations together over steaming cups and heartfelt conversations.
          </p>

          <div class="hero__ctas">
            <a href="#menu" class="btn btn--primary">
              Explore Menu
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M5 12h14M12 5l7 7-7 7"/>
              </svg>
            </a>
            <a href="#order" class="btn btn--secondary">Order Now</a>
          </div>

          <div class="hero__stats">
            <div class="stat">
              <span class="stat__value">50+</span>
              <span class="stat__label">Years of Craft</span>
            </div>
            <div class="stat">
              <span class="stat__value">1000+</span>
              <span class="stat__label">Daily Brews</span>
            </div>
            <div class="stat">
              <span class="stat__value">3</span>
              <span class="stat__label">Locations</span>
            </div>
          </div>
        </div>

        <!-- Hero Visual: Stylized Coffee Cup -->
        <div class="hero__visual" aria-hidden="true">
          <div class="hero__illustration">
            <div class="cup-ring"></div>
            <div class="coffee-cup"></div>
            <div class="steam">
              <div class="steam__particle"></div>
              <div class="steam__particle"></div>
              <div class="steam__particle"></div>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ═══════════════════════════════════════════════════════════════
         MENU: Signature Brews — Retro Recipe Cards
         ═══════════════════════════════════════════════════════════════ -->
    <section class="menu-section" id="menu" aria-labelledby="menu-title">
      <div class="container">
        
        <header class="menu-section__header">
          <h2 id="menu-title" class="section-title">Our Signature Brews</h2>
          <p class="section-subtitle">Crafted with precision using beans roasted in-house since 1973</p>
          <div class="section-divider" aria-hidden="true">
            <span class="section-divider__line"></span>
            <span class="section-divider__icon">☕</span>
            <span class="section-divider__line"></span>
          </div>
        </header>

        <div class="menu-filters" role="tablist" aria-label="Filter menu items">
          <button class="filter-btn is-active" data-filter="all" role="tab" aria-selected="true">All</button>
          <button class="filter-btn" data-filter="coffee" role="tab" aria-selected="false">Coffee</button>
          <button class="filter-btn" data-filter="tea" role="tab" aria-selected="false">Tea</button>
          <button class="filter-btn" data-filter="pastries" role="tab" aria-selected="false">Pastries</button>
          <button class="filter-btn" data-filter="breakfast" role="tab" aria-selected="false">Breakfast</button>
        </div>

        <div class="menu-grid" role="tabpanel">
          
          <!-- Menu Card: Traditional Kopi -->
          <article class="menu-card" data-category="coffee">
            <div class="menu-card__image" aria-hidden="true"></div>
            <div class="menu-card__body">
              <header class="menu-card__header">
                <h3 class="menu-card__title">Traditional Kopi</h3>
                <span class="menu-card__price">$3.50</span>
              </header>
              <p class="menu-card__desc">Strong coffee brewed with margarine and sugar, served with evaporated milk — the authentic Singaporean way.</p>
              <div class="menu-card__meta">
                <span class="menu-card__tag">House Specialty</span>
                <span class="menu-card__spice" aria-label="Medium strength">★★☆</span>
              </div>
              <button class="menu-card__cta" data-product="kopi" data-price="3.50">
                Add to Cart
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 5v14M5 12h14"/>
                </svg>
              </button>
            </div>
          </article>

          <!-- Menu Card: Kopi-C -->
          <article class="menu-card" data-category="coffee">
            <div class="menu-card__image" aria-hidden="true"></div>
            <div class="menu-card__body">
              <header class="menu-card__header">
                <h3 class="menu-card__title">Kopi-C</h3>
                <span class="menu-card__price">$3.20</span>
              </header>
              <p class="menu-card__desc">Coffee with evaporated milk and sugar. Creamy, sweet, and perfectly balanced for your morning ritual.</p>
              <div class="menu-card__meta">
                <span class="menu-card__tag">Best Seller</span>
                <span class="menu-card__spice" aria-label="Mild strength">★☆☆</span>
              </div>
              <button class="menu-card__cta" data-product="kopi-c" data-price="3.20">
                Add to Cart
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 5v14M5 12h14"/>
                </svg>
              </button>
            </div>
          </article>

          <!-- Menu Card: Kopi-O -->
          <article class="menu-card" data-category="coffee">
            <div class="menu-card__image" aria-hidden="true"></div>
            <div class="menu-card__body">
              <header class="menu-card__header">
                <h3 class="menu-card__title">Kopi-O</h3>
                <span class="menu-card__price">$3.00</span>
              </header>
              <p class="menu-card__desc">Strong black coffee with sugar. Bold, intense, and unapologetically Singaporean.</p>
              <div class="menu-card__meta">
                <span class="menu-card__tag">Authentic</span>
                <span class="menu-card__spice" aria-label="Strong">★★★</span>
              </div>
              <button class="menu-card__cta" data-product="kopi-o" data-price="3.00">
                Add to Cart
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 5v14M5 12h14"/>
                </svg>
              </button>
            </div>
          </article>

          <!-- Menu Card: Teh Tarik -->
          <article class="menu-card" data-category="tea">
            <div class="menu-card__image" aria-hidden="true"></div>
            <div class="menu-card__body">
              <header class="menu-card__header">
                <h3 class="menu-card__title">Teh Tarik</h3>
                <span class="menu-card__price">$3.20</span>
              </header>
              <p class="menu-card__desc">Pulled tea with condensed milk. Smooth, creamy, and served with that signature frothy top.</p>
              <div class="menu-card__meta">
                <span class="menu-card__tag">Malaysian Heritage</span>
                <span class="menu-card__spice" aria-label="Mild">☆☆☆</span>
              </div>
              <button class="menu-card__cta" data-product="teh-tarik" data-price="3.20">
                Add to Cart
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 5v14M5 12h14"/>
                </svg>
              </button>
            </div>
          </article>

          <!-- Menu Card: Kaya Toast -->
          <article class="menu-card" data-category="pastries">
            <div class="menu-card__image" aria-hidden="true"></div>
            <div class="menu-card__body">
              <header class="menu-card__header">
                <h3 class="menu-card__title">Kaya Toast Set</h3>
                <span class="menu-card__price">$4.50</span>
              </header>
              <p class="menu-card__desc">Crispy toast with house-made coconut jam and butter. Served with soft-boiled eggs and dark soy sauce.</p>
              <div class="menu-card__meta">
                <span class="menu-card__tag">Breakfast Classic</span>
                <span class="menu-card__spice" aria-label="Mild">☆☆☆</span>
              </div>
              <button class="menu-card__cta" data-product="kaya-toast" data-price="4.50">
                Add to Cart
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 5v14M5 12h14"/>
                </svg>
              </button>
            </div>
          </article>

          <!-- Menu Card: Roti Prata -->
          <article class="menu-card" data-category="breakfast">
            <div class="menu-card__image" aria-hidden="true"></div>
            <div class="menu-card__body">
              <header class="menu-card__header">
                <h3 class="menu-card__title">Roti Prata</h3>
                <span class="menu-card__price">$5.00</span>
              </header>
              <p class="menu-card__desc">Flaky, crispy flatbread served with curry dipping sauce. Perfect pairing with any hot beverage.</p>
              <div class="menu-card__meta">
                <span class="menu-card__tag">Indian Influence</span>
                <span class="menu-card__spice" aria-label="Medium spice">★★☆</span>
              </div>
              <button class="menu-card__cta" data-product="roti-prata" data-price="5.00">
                Add to Cart
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 5v14M5 12h14"/>
                </svg>
              </button>
            </div>
          </article>

        </div>

        <footer class="menu-section__footer">
          <a href="#order" class="link-arrow">
            View Full Menu & Order
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 12h14M12 5l7 7-7 7"/>
            </svg>
          </a>
        </footer>

      </div>
    </section>

    <!-- ═══════════════════════════════════════════════════════════════
         HERITAGE: Our Kopitiam Story
         ═══════════════════════════════════════════════════════════════ -->
    <section class="heritage-section" id="heritage" aria-labelledby="heritage-title">
      <div class="container">
        
        <header class="menu-section__header">
          <h2 id="heritage-title" class="section-title" style="color: var(--surface-darker);">Our Kopitiam Heritage</h2>
          <p class="section-subtitle" style="color: var(--clr-text-secondary);">Preserving Singapore's coffee culture since 1973</p>
        </header>

        <div class="heritage__grid">
          
          <div class="heritage__content">
            <p class="heritage__lead">
              <span class="drop-cap">I</span>n 1973, Uncle Lim opened his first kopitiam stall at Tiong Bahru Market. With nothing but a trusty coffee sock, a worn marble table, and recipes passed down through generations, he began serving what would become Singapore's most beloved morning ritual.
            </p>

            <div class="heritage__quote">
              <p class="heritage__quote-text">
                "The kopitiam is more than just a place to drink coffee. It's where lawyers and laborers sit side by side, where deals are made and friendships are forged over steaming cups of kopi."
              </p>
              <cite class="heritage__quote-author">— Uncle Lim, Founder</cite>
            </div>

            <div class="heritage__values">
              <div class="value-item">
                <div class="value-item__icon">☕</div>
                <h3 class="value-item__title">Authentic Recipes</h3>
                <p class="value-item__desc">Uncle Lim's 1973 recipe book</p>
              </div>
              <div class="value-item">
                <div class="value-item__icon">🤝</div>
                <h3 class="value-item__title">Community First</h3>
                <p class="value-item__desc">Three generations strong</p>
              </div>
              <div class="value-item">
                <div class="value-item__icon">🌱</div>
                <h3 class="value-item__title">Sustainable</h3>
                <p class="value-item__desc">ASEAN farm partnerships</p>
              </div>
            </div>
          </div>

          <div class="heritage__visual">
            <div class="photo-stack">
              <div class="photo-frame">
                <div class="photo-frame__image">
                  <span class="photo-frame__image-placeholder">1973</span>
                </div>
                <p class="photo-frame__caption">Uncle Lim's first stall at Tiong Bahru</p>
              </div>
              <div class="photo-frame" aria-hidden="true">
                <div class="photo-frame__image"></div>
              </div>
              <div class="photo-frame" aria-hidden="true">
                <div class="photo-frame__image"></div>
              </div>
            </div>
          
```
