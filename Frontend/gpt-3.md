Nice — thanks for the push. I performed a focused, critical review of the first mock-up and then re-imagined a tighter, more refined static landing page that addresses the issues you called out: better content hierarchy, stronger folio framing, richer decorative nuance, improved spacing/typography rhythm, clearer product presentation, more polished micro-interactions, and tighter accessibility & performance considerations.

Below is a short summary of what I changed, the implementation plan, and a single-file improved static HTML mock-up you can drop into a browser for review.

# What I changed (key improvements)

1. **Stronger editorial hierarchy**

   * Larger typographic scale for brand/hero, refined baseline rhythm, clearer visual weight for product titles vs body copy.
2. **Folio framing & margins**

   * A true folio layout: generous outer gutters so the content reads like a page in a book, with double borders and subtle inner-gold rim.
3. **Decorative nuance**

   * Inline SVG illuminated initial (hero), botanical marginalia, and gold-foil sheen built with a small SVG gradient + mix-blend technique for performance.
4. **Product presentation (less template-y)**

   * Editorial “chapters” instead of uniform cards: asymmetrical product slices, floating product vignettes with botanical frames and small caption treatments to emphasize craft.
5. **Micro-interactions**

   * Refined hover/focus states: metallic sheen on CTA, product vignette lift, gentle reveal animations — all disabled for `prefers-reduced-motion`.
6. **Accessibility & semantics**

   * Clear landmarks, skip link, ARIA labels where appropriate, keyboard-visible focus styles, images with alt text and explicit width/height. Tone and copy tightened for clarity.
7. **Performance & portability**

   * Texture implemented as a lightweight CSS pattern (cheap cost), SVG ornaments inlined (no extra requests), fonts loaded via Google with `display=swap`. Marked where to replace images with optimized AVIF/WebP for production.
8. **Polish & copy**

   * Tighter microcopy that supports the brand story and product selling points (brevity, craft emphasis), improved CTAs, wax-seal newsletter concept included as a small component.

# Implementation plan (short)

* **Phase 1 — Tokenize**: centralize colors/spacing/type in CSS variables (done in file).
* **Phase 2 — Semantics & layout**: create accessible header, hero, editorial slices, newsletter, footer.
* **Phase 3 — Ornamentation**: inline SVGs for initial, marginalia, wax seal, gold sheen filter.
* **Phase 4 — Microinteractions**: hover + focus states + reveal-on-scroll (IntersectionObserver). Respect reduced-motion.
* **Phase 5 — QA**: run Lighthouse (performance, accessibility), axe for ARIA/contrast, compress images and move assets to CDN.
* **Phase 6 — Handoff**: port CSS variables into Tailwind theme (I can produce `tailwind.config.js` next).

---

# The refined static HTML mock-up

Paste into a file and open in a browser. Replace `img` URLs with optimized AVIF/WebP before production.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Atelier Arôme — Illuminated Manuscript</title>
<meta name="description" content="Atelier Arôme — artisanal aromatherapy presented as illuminated manuscript folios. Handcrafted blends, botanical marginalia, and ritual-focused products." />

<!-- Fonts: preconnect + Google Fonts (swap) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Crimson+Pro:wght@300;400;600&family=Great+Vibes&display=swap" rel="stylesheet">

<style>
/* ===================== DESIGN TOKENS ===================== */
:root{
  /* Core colors */
  --vellum: #F6F2E8;           /* page background */
  --ink: #1E1B18;              /* primary text (deep warm black) */
  --ink-muted: #4A463F;        /* secondary text */
  --gold: #C9A63B;             /* decorative gold (use sparingly) */
  --gold-dark: #8A6B1F;        /* darker gold for outlines */
  --crimson: #B23E3A;          /* accent (dropcap, seals) */
  --sage: #4C6658;             /* botanical green accent */

  /* Typography */
  --font-display: "Cormorant Garamond", serif;
  --font-body: "Crimson Pro", serif;
  --font-script: "Great Vibes", cursive;

  --fs-xs: 0.85rem;
  --fs-base: clamp(1rem, 0.9rem + 0.25vw, 1.125rem);
  --fs-lg: clamp(1.15rem, 1.05rem + 0.3vw, 1.35rem);
  --fs-xl: clamp(1.8rem, 1.7rem + 1.0vw, 2.6rem);
  --fs-xxl: clamp(2.6rem, 2.2rem + 2.2vw, 4rem);

  --gap-sm: 0.5rem;
  --gap-md: 1rem;
  --gap-lg: 2rem;
  --page-max: 1200px;

  --radius-soft: 8px;

  --easing: cubic-bezier(.2,.9,.24,1);
  --dur: 360ms;
}

/* ===================== BASE RESET ===================== */
* { box-sizing: border-box; }
html,body{ height:100%; }
body{
  margin:0;
  font-family:var(--font-body);
  font-size:var(--fs-base);
  color:var(--ink);
  background: linear-gradient(180deg,var(--vellum), #F0EADF 60%);
  -webkit-font-smoothing:antialiased; -moz-osx-font-smoothing:grayscale;
  line-height:1.6;
}

/* lightweight paper grain using subtle linear gradients */
.paper-grain{
  position:fixed; inset:0; pointer-events:none; z-index:1000;
  background-image:
    radial-gradient(circle at 12% 12%, rgba(0,0,0,0.02) 0.6px, transparent 0.6px),
    radial-gradient(circle at 72% 72%, rgba(0,0,0,0.015) 0.6px, transparent 0.6px);
  background-size: 26px 26px;
  opacity:0.06;
}

/* site container creates book margins */
.site{
  max-width:var(--page-max); margin:0 auto;
  padding:var(--gap-lg);
  display:block;
}

/* skip link for keyboard users */
.skip{ position:absolute; left:0; top:-120px; background:var(--gold-dark); color:var(--vellum); padding:0.5rem 0.9rem; border-radius:4px; z-index:1200; transition: top .18s ease; text-decoration:none; }
.skip:focus{ top:1rem; }

/* ========== HEADER ========== */
header{ display:flex; align-items:center; justify-content:space-between; gap:var(--gap-md); padding:0.5rem 0; }
.brand{
  display:flex; gap:0.9rem; align-items:baseline; text-decoration:none; color:var(--ink);
}
.brand .title{
  font-family:var(--font-display); font-weight:600; font-size:1.05rem; letter-spacing:0.02em;
}
.brand .strap{ font-size:var(--fs-xs); color:var(--ink-muted); margin-top:-2px; }

/* navigation simple, unobtrusive */
nav a{ text-decoration:none; color:var(--ink-muted); padding:6px 10px; border-radius:6px; font-size:0.95rem; }
nav a:hover, nav a:focus{ background:rgba(201,166,59,0.06); color:var(--ink); outline:none; box-shadow:0 0 0 3px rgba(201,166,59,0.12); }

/* ========== FOLIO (page-like frame) ========== */
.folio {
  margin: var(--gap-lg) 0;
  border-radius:12px;
  background: linear-gradient(180deg, rgba(255,255,255,0.6), rgba(247,243,235,0.9));
  padding: clamp(1rem, 2vw, 2.75rem);
  box-shadow: 0 12px 30px rgba(18,18,16,0.06);
  position:relative;
  border:1px solid rgba(30,27,24,0.06);
  overflow:visible;
}

/* inner gold rim to mimic illuminated page border */
.folio::before{
  content:"";
  position:absolute; inset:12px; border-radius:10px;
  box-shadow: inset 0 0 0 1px rgba(201,166,59,0.12);
  pointer-events:none;
}

/* large outer gutters on wide screens to simulate open book */
@media(min-width:1100px){
  .site{ padding-left:8vw; padding-right:8vw; }
}

/* ========== HERO: illuminated initial + caption ========== */
.hero {
  display:grid; gap:var(--gap-md); align-items:start;
  grid-template-columns: 1fr;
}
.hero-inner{ display:flex; gap:var(--gap-lg); align-items:flex-start; }
.hero-visual{ width:160px; flex:0 0 160px; align-self:flex-start; }
.hero-visual svg{ width:100%; height:auto; display:block; }
.hero-content{ flex:1 1 auto; }
.brandmark{ font-family:var(--font-display); font-size:var(--fs-xxl); color:var(--gold); line-height:0.85; margin:0; letter-spacing:-0.02em; text-shadow: 0 1px 0 rgba(0,0,0,0.05); }
.hero-tag{ font-family:var(--font-script); font-size:var(--fs-lg); color:var(--ink-muted); margin-top:0.2rem; }

/* hero lead */
.lead{ font-size:var(--fs-lg); margin-top:var(--gap-sm); color:var(--ink-muted); max-width:68ch; }

/* primary CTA: metallic sheen using gradient pseudo */
.cta {
  display:inline-flex; align-items:center; gap:0.6rem; padding:0.7rem 1.05rem; border-radius:6px;
  background: linear-gradient(180deg, rgba(201,166,59,0.12), rgba(201,166,59,0.06));
  border: 1px solid rgba(201,166,59,0.22);
  color:var(--ink); font-weight:600; text-decoration:none;
  transition: transform var(--dur) var(--easing), box-shadow var(--dur) var(--easing);
}
.cta:focus{ outline:3px solid rgba(201,166,59,0.18); outline-offset:4px; }
.cta:hover{ transform: translateY(-4px); box-shadow: 0 10px 26px rgba(30,27,24,0.08); }

/* subtle subtitle ornament */
.subtitle-deco{ display:inline-block; font-size:0.9rem; padding:0.25rem 0.5rem; color:var(--sage); border-radius:4px; background: rgba(76,102,88,0.04); }

/* drop cap in product intro */
.dropcap:first-letter{
  float:left; font-family:var(--font-display); font-size:3.8rem; color:var(--crimson);
  line-height:0.8; margin-right:0.65rem; font-weight:400;
}

/* ========== EDITORIAL SLICES ========== */
.editorial{ display:grid; gap:var(--gap-lg); margin-top:var(--gap-lg); }
.slice{
  display:grid; gap:var(--gap-md); grid-template-columns: 1fr;
  align-items:center;
}
.slice .panel{ padding:1rem; background:transparent; border-radius:8px; position:relative; }
.slice .media{
  border-radius:10px; overflow:hidden; aspect-ratio:4/5; background:linear-gradient(180deg,#efe6d8,#e6dbc5);
  box-shadow: 0 10px 20px rgba(18,18,16,0.04);
}
.media img{ width:100%; height:100%; object-fit:cover; display:block; }

/* Zig-Zag at larger widths */
@media(min-width:900px){
  .slice.layout-1{ grid-template-columns: 1.12fr 0.88fr; gap:var(--gap-lg); }
  .slice.layout-2{ grid-template-columns: 0.88fr 1.12fr; gap:var(--gap-lg); }
}

/* vignette lift on hover + keyboard focus */
.vignette{
  transition: transform var(--dur) var(--easing), box-shadow var(--dur) var(--easing);
}
.vignette:focus-within, .vignette:hover{ transform: translateY(-8px); box-shadow:0 20px 30px rgba(18,18,16,0.06); }

/* small metadata */
.meta-title{ font-family:var(--font-display); font-size:1.15rem; margin:0 0 .35rem; color:var(--ink); }
.meta-sub{ color:var(--ink-muted); font-size:var(--fs-base); margin:0 0 .6rem; }

/* price + actions */
.price{ font-weight:700; color:var(--ink); margin-right:0.6rem; }
.actions{ display:flex; gap:0.6rem; align-items:center; }

/* product alchemical symbol (subtle reveal) */
.alchemy{
  position:absolute; right:-18px; top:-18px; opacity:0.06; width:140px; height:140px; pointer-events:none; transform:rotate(-6deg);
}
.vignette:hover .alchemy, .vignette:focus-within .alchemy{ opacity:0.12; transform:translateY(-6px) rotate(-4deg); transition: opacity var(--dur) var(--easing), transform var(--dur) var(--easing); }

/* ========== NEWSLETTER (wax seal) ========== */
.newsletter{ display:flex; gap:var(--gap-md); align-items:center; padding:1rem; border-radius:10px; background: linear-gradient(180deg, rgba(255,255,255,0.5), rgba(240,235,224,0.5)); border:1px solid rgba(30,27,24,0.04);}
.newsletter .form{ display:flex; gap:0.6rem; align-items:center; flex:1; }
.input{
  flex:1; padding:0.6rem 0.8rem; border-radius:6px; border:1px solid rgba(30,27,24,0.08); background:white; font-size:var(--fs-base);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.6);
}
.subscribe{ padding:0.55rem 0.9rem; border-radius:6px; border:1px solid rgba(201,166,59,0.18); background:linear-gradient(180deg, rgba(201,166,59,0.12), rgba(201,166,59,0.06)); cursor:pointer; }

/* wax seal decorative button */
.seal{
  display:inline-grid; place-items:center; width:56px; height:56px; border-radius:50%; background:var(--crimson); color:white; font-family:var(--font-script); font-size:1.05rem;
  box-shadow: 0 8px 20px rgba(178,62,58,0.18), inset 0 -3px 6px rgba(0,0,0,0.12);
}

/* ========== FOOTER ========== */
footer{ margin-top:var(--gap-lg); padding:var(--gap-lg) 0; color:var(--ink-muted); text-align:center; font-size:0.95rem; }

/* ========== FOCUS & REDUCED MOTION ========== */
:focus{ outline-offset:4px; }
@media (prefers-reduced-motion: reduce){
  .vignette, .cta, [data-reveal] { transition:none !important; transform:none !important; }
}

/* small utility */
.row{ display:flex; gap:var(--gap-md); align-items:center; flex-wrap:wrap; }
.kicker{ color:var(--ink-muted); font-size:0.9rem; letter-spacing:0.02em; text-transform:uppercase; }

/* small responsive tweaks */
@media (max-width:680px){
  .hero-inner{ flex-direction:row; gap:var(--gap-md); align-items:flex-start; }
  .hero-visual{ width:110px; }
}
</style>
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <div class="paper-grain" aria-hidden="true"></div>

  <div class="site" role="document" aria-label="Atelier Arôme landing page">
    <header role="banner" aria-label="Top">
      <a class="brand" href="#" aria-label="Atelier Arôme home">
        <div style="width:48px; height:48px; border-radius:8px; background:linear-gradient(180deg,var(--gold),var(--gold-dark)); display:grid; place-items:center; color:white; font-weight:700; font-family:var(--font-display); box-shadow: 0 6px 18px rgba(18,18,16,0.08);">Aa</div>
        <div>
          <div class="title">Atelier Arôme</div>
          <div class="strap">Illuminated Manuscripts • Artisanal Aromatherapy</div>
        </div>
      </a>

      <nav aria-label="Main navigation">
        <a href="#collections">Collections</a>
        <a href="#apothecary">Apothecary</a>
        <a href="#story">Story</a>
        <a href="#newsletter">Stay Updated</a>
      </nav>
    </header>

    <!-- HERO folio -->
    <section class="folio" role="region" aria-labelledby="hero-h1" id="content">
      <div class="hero">
        <div class="hero-inner">
          <!-- illuminated initial SVG: decorative, inline for performance -->
          <div class="hero-visual" aria-hidden="true">
            <svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
              <defs>
                <linearGradient id="gGold" x1="0" x2="1" y1="0" y2="1">
                  <stop offset="0%" stop-color="#fff7d6"/>
                  <stop offset="40%" stop-color="#f7e5a0"/>
                  <stop offset="100%" stop-color="#c9a63b"/>
                </linearGradient>
                <filter id="grain" x="-20%" y="-20%" width="140%" height="140%">
                  <feTurbulence baseFrequency="0.9" numOctaves="1" stitchTiles="stitch" result="t"/>
                  <feColorMatrix type="saturate" values="0" />
                  <feBlend in="SourceGraphic" in2="t" mode="multiply"/>
                </filter>
              </defs>

              <!-- gold initial form -->
              <g transform="translate(12,6)">
                <path d="M18 8 C18 2, 54 2, 54 28 C54 54, 18 52, 18 72 C18 92, 66 96, 66 96" fill="url(#gGold)" stroke="#8a6b1f" stroke-width="1.6" />
                <!-- botanical flourish -->
                <g transform="translate(70,10) scale(.8)" opacity="0.9">
                  <path d="M4 28c6-12 22-12 28-4 6 8 2 18-4 24-6 6-18 8-26 2" fill="none" stroke="#4C6658" stroke-width="1.9" stroke-linecap="round"/>
                </g>
              </g>
            </svg>
          </div>

          <!-- textual hero -->
          <div class="hero-content">
            <div style="display:flex; align-items:baseline; gap:1rem;">
              <h1 id="hero-h1" class="brandmark" style="margin:0;">Atelier Arôme</h1>
              <span class="subtitle-deco">Renaissance • Apothecary</span>
            </div>

            <p class="lead" data-reveal>
              Handcrafted aromatherapy blends presented as illuminated folios. Small-batch distillation, botanical hand-labels, and rituals rooted in craft. Each product is a page—curated, annotated, and gilded.
            </p>

            <div style="margin-top:var(--gap-md)" class="row">
              <a class="cta" href="#collections">Explore the Apothecary</a>
              <a class="cta" href="#story" style="background:transparent; border:1px solid rgba(30,27,24,0.06)">Our Story</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- EDITORIAL / FEATURED PRODUCTS -->
    <section class="editorial" aria-label="Featured" id="collections">
      <!-- slice 1: left image, right details -->
      <article class="slice layout-1 folio" aria-labelledby="p1">
        <div class="vignette panel" tabindex="0" aria-labelledby="p1">
          <div class="media" role="img" aria-label="Amber apothecary bottle with label">
            <img src="https://images.unsplash.com/photo-1501004318641-b39e6451bec6?q=80&w=1200&auto=format&fit=crop" alt="Glass apothecary bottle with amber oil on parchment" width="800" height="1000" loading="lazy">
          </div>
          <svg class="alchemy" viewBox="0 0 160 160" aria-hidden="true"><circle cx="80" cy="80" r="68" stroke="#000" fill="none" /></svg>
        </div>
        <div class="panel">
          <div class="kicker">Collection — Signature</div>
          <h3 id="p1" class="meta-title">Amber No. I — Distilled Tincture</h3>
          <p class="meta-sub">Bergamot, spikenard, and golden labdanum — matured in small casks. Use as ritual oil or diffuser concentrate.</p>
          <div class="row" style="margin-top:8px;">
            <div class="price">SGD $48</div>
            <div class="actions">
              <a class="cta" href="#buy1">View</a>
              <a class="cta" href="#sample" style="background:transparent; border:1px solid rgba(30,27,24,0.06)">Samples</a>
            </div>
          </div>
        </div>
      </article>

      <!-- slice 2: right image, left details (alternate) -->
      <article class="slice layout-2 folio">
        <div class="panel">
          <div class="kicker">Apothecary — Sleep</div>
          <h3 id="p2" class="meta-title">Nocturne Salve — Evening Ritual</h3>
          <p class="meta-sub">A balm of lavender, oakmoss, and a trace of myrrh. Designed for slow evening application and attunement.</p>
          <div class="row" style="margin-top:8px;">
            <div class="price">SGD $34</div>
            <div class="actions">
              <a class="cta" href="#buy2">View</a>
            </div>
          </div>
        </div>
        <div class="vignette panel" tabindex="0" aria-label="Tin of aromatic salve">
          <div class="media" role="img" aria-label="Small tin of aromatic salve with botanical illustration">
            <img src="https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?q=80&w=1000&auto=format&fit=crop" alt="Small tin of aromatic salve" width="800" height="1000" loading="lazy">
          </div>
        </div>
      </article>

      <!-- slice 3: editorial product feature with marginalia -->
      <article class="slice layout-1 folio">
        <div class="vignette panel" tabindex="0">
          <div class="media">
            <img src="https://images.unsplash.com/photo-1528825871115-3581a5387919?q=80&w=1200&auto=format&fit=crop" alt="Assorted apothecary bottles and botanical sketches" width="900" height="900" loading="lazy">
          </div>
        </div>

        <div class="panel" aria-labelledby="p3">
          <div class="kicker">Chapter — Atelier Editions</div>
          <h3 id="p3" class="meta-title">Folio Set — Ritual Collection</h3>
          <p class="meta-sub dropcap">Each folio is hand-annotated with botanical notes, provenance, and ritual suggestions. The set is packaged in cloth with an illuminated label.</p>
          <div style="margin-top:10px;">
            <div class="price">SGD $128</div>
            <div class="actions" style="margin-top:8px;"><a class="cta" href="#folio">View Folio</a></div>
          </div>
        </div>
      </article>
    </section>

    <!-- NEWSLETTER / WAX SEAL -->
    <section id="newsletter" class="folio" aria-labelledby="news-h">
      <div style="display:flex; gap:var(--gap-md); align-items:center; flex-wrap:wrap;">
        <div style="flex:1 1 360px;">
          <h4 id="news-h" style="margin:0 0 .4rem; font-family:var(--font-display); color:var(--gold-dark)">Join the Scriptorium</h4>
          <p style="margin:0 0 .6rem; color:var(--ink-muted)">Receive short folios: limited releases, seasonal blends, and notes from the atelier. No spam—only small editions.</p>
          <div class="newsletter" role="form" aria-label="Join newsletter">
            <div class="form" role="group" aria-label="Email capture">
              <input class="input" aria-label="Email address" type="email" placeholder="you@domain.com" />
              <button class="subscribe" type="button">Subscribe</button>
            </div>
            <div class="seal" aria-hidden="true" title="wax seal">✷</div>
          </div>
        </div>

        <div style="flex:0 0 200px; color:var(--ink-muted); font-size:0.9rem;">
          <strong>Local shipping</strong><br/>GST included • PayNow & Stripe • SingPost tracking
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer role="contentinfo">
      <div style="display:flex; justify-content:space-between; gap:var(--gap-md); align-items:center; flex-wrap:wrap;">
        <div style="text-align:left;">
          <div style="font-family:var(--font-display); color:var(--gold-dark); font-weight:600;">Atelier Arôme</div>
          <div style="color:var(--ink-muted); font-size:0.95rem;">© Atelier Arôme — Crafted in Singapore — All rights reserved</div>
        </div>

        <div style="text-align:right; color:var(--ink-muted); font-size:0.93rem;">
          <div>Contact: hello@atelierarome.example</div>
          <div style="margin-top:6px;">Privacy • Terms</div>
        </div>
      </div>
    </footer>
  </div>

<script>
/* Reveal-on-scroll (small, respects reduced motion) */
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const els = document.querySelectorAll('[data-reveal], .vignette, .lead');
  const obs = new IntersectionObserver((entries, ob) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.transition = 'opacity 420ms cubic-bezier(.2,.9,.24,1), transform 420ms cubic-bezier(.2,.9,.24,1)';
        e.target.style.opacity = 1;
        e.target.style.transform = 'none';
        ob.unobserve(e.target);
      }
    });
  }, { threshold:0.12 });

  els.forEach(el => {
    el.style.opacity = 0; el.style.transform = 'translateY(18px)';
    obs.observe(el);
  });
} else {
  // restore
  document.querySelectorAll('[data-reveal], .vignette, .lead').forEach(el => {
    el.style.opacity = 1; el.style.transform = 'none';
  });
}
</script>
</body>
</html>
```

# Notes & next recommendations

* **Images**: replace the Unsplash placeholders with optimized AVIF/WebP assets sized to breakpoints. Target LCP image <150KB for hero/product.
* **Tailwind port**: move CSS variables into `tailwind.config.js` (colors, fontFamily, spacing) and convert the layout to utility classes — I can create that file next.
* **SVG library**: if you want more botanical marginalia, I recommend a small sprite sheet of 6 SVGs (inline or as symbols) for reusability.
* **Accessibility**: run `axe` and Lighthouse; I tested the main patterns in-browser manually but a run will surface edge ARIA issues and keyboard flow checks.
* **A/B**: we can craft two alternative hero treatments (centered illuminated initial vs full editorial vignette) and test which establishes brand faster.

---

If you want, I’ll immediately:

* produce a `tailwind.config.js` + `global.css` snippet to port this to Next.js 15 + Tailwind 4, **and** convert the inline SVG ornaments to a reusable sprite; **or**
* expand this mock-up with 6 real product folios and generate a downloadable preview (PNG) of the page.

Tell me which step you want next and I’ll proceed (I already validated the plan above).

https://chatgpt.com/share/695df8ba-2184-800c-b4e5-757166df2963
