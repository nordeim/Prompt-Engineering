# Executive summary

I'll deliver a production-ready implementation plan and a complete **single-file static HTML mock-up** for **Atelier Arôme** (Illuminated Manuscript / Renaissance aesthetic). The design follows the provided style guides (token palette, typography, texture, Zig-Zag editorial layout, folio framing, gold accents, accessibility and performance rules). Key design rules are pulled from your guides.   

---

# Plan (phased & validated)

## Phase A — Prepare (tokens + baseline)

* Create design tokens (CSS variables): Stone/Vellum, gold variants, cinnabar, verdigris, spacing scale, fluid typographic scale. (from guides). 
* Import fonts (Cormorant Garamond, Crimson Pro, Great Vibes) with preload & `font-display: swap`. 

## Phase B — Structure & semantics (validation checkpoint)

* Build semantic HTML tree: skip link, header/nav (`role="navigation"`), `<main>` with hero + editorial Zig-Zag product slices, `<footer role="contentinfo">`. Verify heading hierarchy. 

## Phase C — Visual frame & texture

* Global parchment/stone backgrounds, subtle radial-gradient noise overlay (cheap & performant), folio double-border frames.  

## Phase D — Components & micro-interactions

* CTA button with `::before` slide gold interaction, product image hover (dark overlay + centered title), reveal-on-scroll using `IntersectionObserver` with luxury easing. Reduced-motion respected. 

## Phase E — Accessibility, performance & QA

* AAA contrast checks (stone on vellum). Focus styles (3px gold outline). Skip link, aria labels, minimum touch targets. Images use `width`/`height` and `loading="lazy"`. Performance budget: keep assets small; SVG ornaments inline.  

## Phase F — Deliver

* Single static HTML file (below), plus a brief validation checklist to run locally.

---

# What I built (now): single-file static HTML mock-up

* Mobile-first, responsive, uses the Zig-Zag editorial pattern.
* Implements tokens, texture, folio frame, gold gradient headings, drop cap rule sample, slide CTA, reveal animation, accessibility essentials.

> Use this file as a drop-in mockup. Replace image `src` with your production assets (AVIF/WebP preferred), and move tokens into Tailwind config or global CSS when porting to Next.js + Tailwind.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Atelier Arôme — Illuminated Manuscript</title>

<!-- Fonts (preconnect + load) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=Crimson+Pro:wght@300;400;600&family=Great+Vibes&display=swap" rel="stylesheet">

<style>
  /* ===== Design tokens (Stone & Vellum system) ===== */
  :root{
    --color-vellum: #F3EFE6;         /* warm paper */
    --color-stone:  #282826;        /* warm charcoal */
    --color-stone-light: #4A4A48;
    --color-bone: #F0EDE5;          /* text on dark */
    --color-gold-ui: #8A6B1F;       /* UI gold (contrast-safe) */
    --color-gold-deco: #C5A028;     /* decorative gold */
    --color-verdigris: #4B6655;
    --color-cinnabar: #B8413D;

    /* typography */
    --font-heading: "Cormorant Garamond", serif;
    --font-body: "Crimson Pro", serif;
    --font-deco: "Great Vibes", cursive;

    /* fluid type (example) */
    --text-base: clamp(1rem, 0.95rem + 0.26vw, 1.125rem);
    --text-lg: clamp(1.2rem, 1.14rem + 0.31vw, 1.44rem);
    --text-3xl: clamp(2.1rem, 1.9rem + 1.0vw, 3.2rem);
    --text-4xl: clamp(3rem, 3.6rem + 1.2vw, 4.8rem);

    /* spacing */
    --space-2: 0.5rem;
    --space-4: 1rem;
    --space-8: 2rem;
    --space-12: 3rem;
    --space-16: 4rem;

    /* motion */
    --easing-lux: cubic-bezier(0.25, 0.46, 0.45, 0.94);
    --duration-medium: 420ms;
  }

  /* ===== reset & base ===== */
  *,*::before,*::after{box-sizing:border-box}
  html,body{height:100%}
  body{
    margin:0;
    background: linear-gradient(180deg, var(--color-vellum) 0%, #EFEAE0 100%);
    color:var(--color-stone);
    font-family: var(--font-body);
    font-size:var(--text-base);
    -webkit-font-smoothing:antialiased;
    -moz-osx-font-smoothing:grayscale;
    line-height:1.6;
  }

  /* subtle global texture (radial pattern - performant) */
  .texture-overlay{
    position:fixed; inset:0; pointer-events:none; z-index:999;
    opacity:0.04;
    background-image:
      radial-gradient(circle at 12% 12%, rgba(40,40,38,0.05) 1px, transparent 1px),
      radial-gradient(circle at 78% 78%, rgba(40,40,38,0.05) 1px, transparent 1px);
    background-size: 24px 24px;
    mix-blend-mode:normal;
  }

  /* layout container */
  .site{max-width:1100px; margin:0 auto; padding:var(--space-8)}
  .skip-link{
    position:absolute; left:0; top:-120px; background:var(--color-gold-ui); color:var(--color-vellum);
    padding:0.5rem 1rem; z-index:1000; transition:top .2s;
  }
  .skip-link:focus{ top:1rem; }

  header{display:flex; align-items:center; justify-content:space-between; gap:1rem; padding:1rem 0;}
  .brand{
    display:flex; align-items:center; gap:0.75rem; text-decoration:none; color:var(--color-stone);
  }
  .brand .monogram{
    font-family:var(--font-heading); font-weight:300; font-size:1.9rem; color:var(--color-gold-deco);
    line-height:1;
  }
  nav a{color:var(--color-stone-light); text-decoration:none; padding:0.25rem 0.5rem; font-size:0.95rem}
  nav a:focus-visible{outline:3px solid var(--color-gold-ui); outline-offset:3px}

  /* hero */
  .hero{
    background: linear-gradient(180deg, #2D2B29 0%, #282826 100%);
    color:var(--color-bone);
    border-radius:6px;
    padding: var(--space-12);
    margin-bottom:var(--space-12);
    position:relative;
    overflow:hidden;
  }
  .hero .title{
    font-family:var(--font-heading);
    font-size:var(--text-4xl);
    line-height:1;
    margin:0 0 .5rem;
    background: linear-gradient(to bottom, var(--color-gold-deco) 0%, #FCF6BA 45%, #B08D22 100%);
    -webkit-background-clip:text; background-clip:text; color:transparent;
    -webkit-text-fill-color:transparent;
  }
  .hero .subtitle{ font-family:var(--font-deco); font-size:1.4rem; opacity:0.95; margin-bottom:var(--space-8) }
  .hero p.lead{ max-width:65ch; font-size:var(--text-lg); color:rgba(240,237,229,0.9) }

  /* CTA - slide effect */
  .btn {
    position:relative; display:inline-block; padding:0.75rem 1.25rem; border:2px solid var(--color-gold-ui);
    background:transparent; color:var(--color-bone); font-weight:600; text-decoration:none;
    overflow:hidden; border-radius:4px; cursor:pointer;
  }
  .btn::before{
    content:""; position:absolute; left:-100%; top:0; bottom:0; width:100%; background:var(--color-gold-deco);
    transition: transform var(--duration-medium) var(--easing-lux); transform:translateX(0) translateX(0);
    transform: translateX(0);
  }
  .btn span{ position:relative; z-index:2; color:var(--color-bone); transition:color var(--duration-medium) var(--easing-lux) }
  .btn:hover::before{ transform: translateX(100%); left:0; }
  .btn:hover{ color:var(--color-stone); }
  .btn:focus-visible{ outline:3px solid var(--color-gold-ui); outline-offset:4px }

  /* folio frame */
  .folio{ border:1px solid rgba(40,40,38,0.08); padding:var(--space-6); position:relative; background:var(--color-vellum);}
  .folio::after{
    content:""; position:absolute; inset:8px; border:1px solid rgba(197,160,40,0.14); pointer-events:none;
  }

  /* editorial Zig-Zag */
  .editorial{ display:grid; gap:var(--space-12); margin-bottom:var(--space-16) }
  .slice{ display:grid; grid-template-columns:1fr; gap:var(--space-8); align-items:center; }
  .slice .image{ width:100%; aspect-ratio:4/5; background:linear-gradient(180deg,#e9e1cf,#d7cdb3); display:block; border-radius:4px; overflow:hidden; position:relative }
  .slice .image img{ width:100%; height:100%; object-fit:cover; display:block }

  .slice .meta h3{ font-family:var(--font-heading); font-size:1.4rem; margin:0 0 .5rem; color:var(--color-stone) }
  .slice .meta p{ margin:0 0 var(--space-4); color:var(--color-stone-light) }

  /* Zig-Zag on wider screens */
  @media (min-width:900px){
    .slice{ grid-template-columns: 1.2fr 1fr; gap:var(--space-12) }
    .slice.alt{ grid-template-columns:1fr 1.2fr } /* alternate */
  }

  /* drop cap example */
  .dropcap::first-letter{
    float:left; font-family:var(--font-heading); font-size:4.5rem; color:var(--color-cinnabar);
    line-height:0.8; margin-right:.5rem; font-weight:400;
  }

  /* reveal animation (initial state) */
  .reveal{ opacity:0; transform:translateY(30px); transition: opacity var(--duration-medium) var(--easing-lux), transform var(--duration-medium) var(--easing-lux) }
  .reveal.is-visible{ opacity:1; transform:none }

  footer{ padding:var(--space-8) 0; color:rgba(240,237,229,0.85); background:linear-gradient(180deg,#282826 0%, #232221 100%); margin-top:var(--space-12) }
  footer .col{ max-width:240px }

  /* focus visible styling for keyboard users */
  :focus{ outline-offset:3px }

  /* reduced motion */
  @media (prefers-reduced-motion: reduce){
    .reveal, .btn::before{ transition:none !important; animation:none !important }
  }
</style>
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <div class="texture-overlay" aria-hidden="true"></div>

  <div class="site">
    <header role="banner">
      <a href="#" class="brand" aria-label="Atelier Arôme home">
        <span class="monogram" aria-hidden="true">A</span>
        <div>
          <div style="font-family:var(--font-heading); font-size:0.98rem;">Atelier Arôme</div>
          <div style="font-size:0.78rem; color:var(--color-stone-light)">Artisanal Aromatherapy</div>
        </div>
      </a>
      <nav role="navigation" aria-label="Main navigation">
        <a href="#collections">Collections</a>
        <a href="#story">Our Story</a>
        <a href="#contact">Contact</a>
      </nav>
    </header>

    <!-- HERO -->
    <main id="main" role="main">
      <section class="hero folio" aria-labelledby="hero-title">
        <h1 id="hero-title" class="title">Atelier Arôme</h1>
        <div class="subtitle">Illuminated Manuscripts • Artisanal Aromatherapy</div>
        <p class="lead dropcap reveal">Handcrafted blends inspired by historical apothecaries — each bottle a page from an illuminated folio: botanicals, alchemical sketches, and carefully sourced essential oils curated for ritual and repose.</p>
        <p style="margin-top:var(--space-8)">
          <a href="#collections" class="btn" role="button"><span>Explore the Apothecary</span></a>
        </p>
      </section>

      <!-- EDITORIAL / PRODUCTS (Zig-Zag) -->
      <section class="editorial" aria-label="Featured products">
        <!-- Slice 1: Image left, text right -->
        <article class="slice folio reveal" aria-labelledby="p1-title">
          <div class="image" aria-hidden="true">
            <img src="https://images.unsplash.com/photo-1501004318641-b39e6451bec6?q=80&w=1000&auto=format&fit=crop" alt="Glass apothecary bottle with amber oil" width="600" height="750" loading="lazy">
          </div>
          <div class="meta">
            <h3 id="p1-title">Botanical Tincture — Amber No.1</h3>
            <p>Hand-pressed bergamot and spikenard, steeped and matured in small batches. Presented with a decorative folio label and botanical marginalia.</p>
            <p><strong>SGD $48</strong></p>
            <p><a class="btn" href="#buy">View</a></p>
          </div>
        </article>

        <!-- Slice 2: Text left, image right (alt) -->
        <article class="slice alt folio reveal" aria-labelledby="p2-title">
          <div class="meta">
            <h3 id="p2-title">Nocturne Salve — Sleep Ritual</h3>
            <p>Lavender, oakmoss and a whisper of myrrh in a balm for evening practice — crafted for calm and ritual application.</p>
            <p><strong>SGD $34</strong></p>
            <p><a class="btn" href="#buy2">View</a></p>
          </div>
          <div class="image" aria-hidden="true">
            <img src="https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?q=80&w=800&auto=format&fit=crop" alt="Small tin of aromatic salve with botanical illustration" width="600" height="750" loading="lazy">
          </div>
        </article>
      </section>
    </main>

    <!-- Footer (colophon style) -->
    <footer role="contentinfo">
      <div style="display:flex; gap:var(--space-8); justify-content:space-between; align-items:flex-start; padding:var(--space-8); max-width:1100px; margin:0 auto;">
        <div class="col">
          <div style="font-family:var(--font-heading); color:var(--color-gold-deco); font-size:1.1rem">Atelier Arôme</div>
          <div style="color:var(--color-bone); opacity:0.8; margin-top:0.5rem; max-width:36ch;">
            A small atelier preserving craft traditions. GST and local shipping supported.
          </div>
        </div>
        <div class="col" aria-hidden="true">
          <svg width="160" height="40" viewBox="0 0 160 40" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="decorative divider"><path d="M0 20 H160" stroke="#C5A028" stroke-width="0.8" stroke-opacity="0.18"/></svg>
          <div style="margin-top:0.5rem; color:var(--color-bone); opacity:0.75; font-size:0.85rem">© Atelier Arôme</div>
        </div>
      </div>
    </footer>
  </div>

<script>
(function(){
  // Reveal on scroll (IntersectionObserver) - respects reduced motion
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.reveal').forEach(el=>el.classList.add('is-visible'));
    return;
  }
  const obs = new IntersectionObserver((entries, o)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        e.target.classList.add('is-visible');
        o.unobserve(e.target);
      }
    });
  }, {threshold: 0.15});
  document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
})();
</script>
</body>
</html>
```

---

# Quick validation checklist (what I checked for)

* Tokens: Stone/Vellum + two gold variants + cinnabar + verdigris implemented as CSS variables. 
* Texture: radial gradient grain overlay (light, performant alternative to heavy SVG). 
* Layout: mobile-first + Zig-Zag slices that flip at `min-width:900px`. 
* Typography: Cormorant Garamond / Crimson Pro / Great Vibes loaded; drop cap example used. 
* Interaction: CTA slide `::before` pattern + IntersectionObserver reveal + reduced motion respects. 
* Accessibility: skip link, semantic elements, focus-visible outlines, images include width/height and `loading="lazy"`. 
* Performance: inline small SVG ornament, radial pattern for texture (cheap), fonts loaded with `display=swap`. 

---

# Next steps & handoff notes

1. Replace placeholder images with optimized AVIF/WebP versions sized to target breakpoints; keep hero assets <150KB. 
2. Move tokens into `tailwind.config.js` and port the CSS variables into Tailwind theme for Next.js implementation (if you want I can produce that). 
3. Run an accessibility/contrast check (axe or Lighthouse) and an LCP/CSS/JS budget audit. 

---

If you want, I’ll now:

* (A) Produce a Tailwind 4 `tailwind.config.js` snippet and PostCSS/Next.js notes to port the mockup to Next.js 15, **or**
* (B) Expand this mock-up with 6 product slices, SVG marginalia assets, and a small responsive product grid for larger catalogs.

Which of (A) or (B) should I do next?

---

https://chatgpt.com/share/695df8ba-2184-800c-b4e5-757166df2963
