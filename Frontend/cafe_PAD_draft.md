# Project Architecture Document — **Merlion Brews** (Reimagined Enterprise-grade Full-Stack Architecture)

**Reference:** static landing-page mockup `cafe.html`
```html
<!DOCTYPE html>
<html lang="en-SG">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Merlion Brews Artisan Roastery • Heritage Coffee Crafted with Peranakan Soul • Singapore's Finest Single-Origin Beans">
    <title>Merlion Brews • Artisan Coffee Roastery</title>
    
    <!-- Preconnect to Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    
    <!-- Preload critical fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Crimson+Pro:wght@400;600&family=Pinyon+Script&display=swap" rel="stylesheet">
    
    <style>
        /* ===== CSS LAYERS ARCHITECTURE ===== */
        @layer tokens, base, components, utilities, overrides;
        
        /* ===== LAYER 1: DESIGN TOKENS ===== */
        @layer tokens {
            :root {
                /* ===== PERANAKAN HERITAGE COLOR SYSTEM ===== */
                --color-nyonya-cream: #F8F3E6;        /* Traditional tile background */
                --color-kopi-brown: #3A2A1F;          /* Deep coffee roast */
                --color-terracotta: #C77966;          /* Traditional pottery accent */
                --color-heritage-blue: #4A6B7D;       /* Peranakan tile accent */
                --color-gold-leaf: #D4AF37;           /* Handcrafted detail */
                
                /* ===== ACCESSIBILITY-SAFE VARIANTS ===== */
                --color-ui-terracotta: #9A5E4A;       /* Darker for WCAG AAA contrast */
                --color-ui-gold: #A68A2E;             /* Darker gold for text/CTAs */
                --color-ui-blue: #3A5463;            /* Darker heritage blue for text */
                
                /* ===== RGB VALUES FOR OPACITY ===== */
                --color-kopi-brown-rgb: 58, 42, 31;
                --color-terracotta-rgb: 199, 121, 102;
                --color-heritage-blue-rgb: 74, 107, 125;
                --color-gold-leaf-rgb: 212, 175, 55;
                
                /* ===== TYPOGRAPHY SYSTEM ===== */
                --font-heading: 'Cormorant Garamond', serif;
                --font-body: 'Crimson Pro', serif;
                --font-decorative: 'Pinyon Script', cursive;
                
                /* ===== FLUID TYPOGRAPHY SCALE - Major Third (1.25 ratio) ===== */
                --text-xs: clamp(0.69rem, 0.66rem + 0.17vw, 0.79rem);
                --text-sm: clamp(0.83rem, 0.79rem + 0.21vw, 0.96rem);
                --text-base: clamp(1.00rem, 0.95rem + 0.26vw, 1.20rem);
                --text-lg: clamp(1.20rem, 1.14rem + 0.31vw, 1.44rem);
                --text-xl: clamp(1.44rem, 1.37rem + 0.37vw, 1.73rem);
                --text-2xl: clamp(1.73rem, 1.64rem + 0.45vw, 2.07rem);
                --text-3xl: clamp(2.07rem, 1.97rem + 0.54vw, 2.49rem);
                --text-4xl: clamp(2.49rem, 2.37rem + 0.65vw, 3.20rem);
                --text-5xl: clamp(3.00rem, 2.80rem + 0.80vw, 4.50rem);
                --text-6xl: clamp(3.50rem, 3.20rem + 1.00vw, 5.50rem);
                
                /* ===== LINE HEIGHTS ===== */
                --leading-tight: 1.2;
                --leading-normal: 1.6;
                --leading-loose: 1.8;
                
                /* ===== LETTER SPACING ===== */
                --tracking-tight: -0.02em;
                --tracking-normal: 0;
                --tracking-loose: 0.1em;
                
                /* ===== SPACING SYSTEM - 4px Baseline Grid ===== */
                --space-1: 0.25rem;    /* 4px - micro spacing */
                --space-2: 0.5rem;     /* 8px - tight spacing */
                --space-3: 0.75rem;    /* 12px - medium tight */
                --space-4: 1rem;       /* 16px - base unit */
                --space-6: 1.5rem;     /* 24px - comfortable */
                --space-8: 2rem;       /* 32px - section spacing */
                --space-12: 3rem;      /* 48px - major spacing */
                --space-16: 4rem;      /* 64px - hero spacing */
                --space-24: 6rem;      /* 96px - massive spacing */
                --space-32: 8rem;      /* 128px - hero vertical padding */
                
                /* ===== SEMANTIC SPACING ===== */
                --space-inside: var(--space-4);    /* Inside containers */
                --space-outside: var(--space-8);   /* Between containers */
                --space-stack: var(--space-6);     /* Between stacked elements */
                --space-inline: var(--space-3);    /* Between inline elements */
                
                /* ===== LAYOUT SYSTEM ===== */
                --container-width: min(100%, 85ch);
                --nav-height: clamp(4rem, 3.5rem + 1.5vw, 5rem);
                --border-radius: 8px;
                --border-radius-sm: 4px;
                --border-radius-lg: 16px;
                
                /* ===== TRANSITIONS & TIMING ===== */
                --duration-fast: 120ms;
                --duration-medium: 250ms;
                --duration-slow: 400ms;
                --easing-smooth: cubic-bezier(0.25, 0.46, 0.45, 0.94); /* Luxury easing */
                --easing-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
                
                /* ===== SHADOWS ===== */
                --shadow-sm: 0 2px 4px rgba(var(--color-kopi-brown-rgb), 0.08);
                --shadow-md: 0 4px 8px rgba(var(--color-kopi-brown-rgb), 0.12);
                --shadow-lg: 0 8px 16px rgba(var(--color-kopi-brown-rgb), 0.15);
                --shadow-xl: 0 12px 24px rgba(var(--color-kopi-brown-rgb), 0.18);
                
                /* ===== Z-INDEX SCALE ===== */
                --z-below: -1;
                --z-base: 0;
                --z-dropdown: 100;
                --z-sticky: 200;
                --z-modal: 300;
                --z-popover: 400;
                --z-toast: 500;
            }
            
            /* ===== ACCESSIBILITY OVERRIDES ===== */
            @media (prefers-contrast: more) {
                :root {
                    --color-nyonya-cream: #FFFFFF;
                    --color-kopi-brown: #000000;
                    --color-ui-terracotta: #000000;
                    --color-ui-gold: #000000;
                    --color-ui-blue: #000000;
                }
            }
            
            /* ===== REDUCED MOTION ===== */
            @media (prefers-reduced-motion: reduce) {
                :root {
                    --duration-fast: 1ms;
                    --duration-medium: 1ms;
                    --duration-slow: 1ms;
                }
            }
        }
        
        /* ===== LAYER 2: BASE STYLES ===== */
        @layer base {
            /* CSS Reset */
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
                line-height: var(--leading-normal);
                color: var(--color-kopi-brown);
                background-color: var(--color-nyonya-cream);
                overflow-x: hidden;
            }
            
            /* Global Texture Overlay - Paper Fiber Effect */
            .texture-overlay {
                position: fixed;
                inset: 0;
                pointer-events: none;
                z-index: var(--z-below);
                opacity: 0.04;
                background-image: 
                    radial-gradient(circle at 10% 10%, rgba(var(--color-kopi-brown-rgb), 0.05) 1px, transparent 1px),
                    radial-gradient(circle at 90% 90%, rgba(var(--color-kopi-brown-rgb), 0.05) 1px, transparent 1px);
                background-size: 24px 24px;
                contain: paint;
            }
            
            /* Typography Scale */
            h1, h2, h3, h4, h5, h6 {
                font-family: var(--font-heading);
                line-height: var(--leading-tight);
                font-weight: 700;
                margin-bottom: var(--space-4);
            }
            
            h1 {
                font-size: var(--text-6xl);
                letter-spacing: var(--tracking-tight);
            }
            
            h2 {
                font-size: var(--text-4xl);
                font-weight: 600;
                letter-spacing: var(--tracking-tight);
            }
            
            h3 {
                font-size: var(--text-3xl);
                font-weight: 600;
                color: var(--color-ui-terracotta);
            }
            
            h4 {
                font-size: var(--text-2xl);
                color: var(--color-heritage-blue);
            }
            
            p {
                margin-bottom: var(--space-4);
                max-width: 65ch;
            }
            
            a {
                color: var(--color-ui-terracotta);
                text-decoration: none;
                transition: color var(--duration-medium) var(--easing-smooth);
            }
            
            a:hover, a:focus {
                color: var(--color-terracotta);
            }
            
            /* Semantic HTML Elements */
            main {
                position: relative;
                z-index: 1;
            }
            
            section {
                padding: var(--space-24) 0;
            }
            
            .container {
                width: 100%;
                max-width: var(--container-width);
                margin: 0 auto;
                padding: 0 var(--space-4);
            }
            
            /* Skip Link for Accessibility */
            .skip-link {
                position: absolute;
                top: -100px;
                left: 0;
                background: var(--color-ui-terracotta);
                color: var(--color-nyonya-cream);
                padding: var(--space-2) var(--space-4);
                z-index: var(--z-modal);
                transition: top var(--duration-medium) var(--easing-smooth);
            }
            
            .skip-link:focus {
                top: var(--space-4);
            }
            
            /* Focus Styles for Accessibility */
            :focus-visible {
                outline: 3px solid var(--color-ui-gold);
                outline-offset: 2px;
            }
        }
        
        /* ===== LAYER 3: COMPONENTS ===== */
        @layer components {
            /* Navigation Component */
            .header {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                height: var(--nav-height);
                background-color: rgba(248, 243, 230, 0.85);
                backdrop-filter: blur(10px);
                border-bottom: 1px solid rgba(var(--color-kopi-brown-rgb), 0.08);
                z-index: var(--z-sticky);
                padding: 0 var(--space-4);
            }
            
            .header-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                height: 100%;
                max-width: var(--container-width);
                margin: 0 auto;
            }
            
            .logo {
                font-family: var(--font-heading);
                font-size: var(--text-2xl);
                color: var(--color-ui-terracotta);
                display: flex;
                align-items: center;
                gap: var(--space-2);
            }
            
            .logo-monogram {
                font-family: var(--font-decorative);
                font-size: var(--text-3xl);
                color: var(--color-gold-leaf);
                line-height: 1;
            }
            
            .logo-text {
                font-weight: 600;
                letter-spacing: -0.5px;
            }
            
            .nav-links {
                display: flex;
                gap: var(--space-8);
            }

            .menu-trigger {
                display: none;
                width: 44px;
                height: 44px;
                align-items: center;
                justify-content: center;
                gap: 6px;
                border: 1px solid rgba(var(--color-kopi-brown-rgb), 0.15);
                border-radius: var(--border-radius);
                background: transparent;
                color: var(--color-kopi-brown);
                cursor: pointer;
            }

            .menu-trigger .line {
                display: block;
                width: 20px;
                height: 2px;
                background-color: currentColor;
                transition: transform var(--duration-medium) var(--easing-smooth), background-color var(--duration-medium) var(--easing-smooth);
            }
            
            .nav-link {
                font-family: var(--font-body);
                font-size: var(--text-lg);
                font-weight: 500;
                color: var(--color-kopi-brown);
                position: relative;
                padding: var(--space-1) var(--space-2);
            }
            
            .nav-link::after {
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 2px;
                background: var(--color-ui-terracotta);
                transform: scaleX(0);
                transform-origin: right;
                transition: transform var(--duration-medium) var(--easing-smooth);
            }
            
            .nav-link:hover::after,
            .nav-link:focus::after {
                transform: scaleX(1);
                transform-origin: left;
            }
            
            /* Coffee Bean Animation */
            .coffee-bean {
                position: absolute;
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: var(--color-kopi-brown);
                opacity: 0.3;
                animation: float var(--duration-slow) infinite ease-in-out;
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.3; }
                50% { transform: translateY(-20px) rotate(15deg); opacity: 0.6; }
            }
            
            /* Hero Component */
            .hero {
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                padding: var(--space-32) var(--space-4);
                position: relative;
                overflow: hidden;
            }
            
            .hero-content {
                max-width: min(100%, 75ch);
                z-index: 1;
                animation: fadeUp var(--duration-slow) var(--easing-smooth) forwards;
                opacity: 0;
                transform: translateY(40px);
            }
            
            .hero-title {
                font-size: var(--text-6xl);
                line-height: 1;
                margin-bottom: var(--space-6);
                color: var(--color-ui-terracotta);
            }
            
            .hero-subtitle {
                font-family: var(--font-decorative);
                font-size: var(--text-3xl);
                color: var(--color-ui-blue);
                margin-bottom: var(--space-8);
                font-weight: 400;
            }
            
            .hero-text {
                font-size: var(--text-xl);
                color: var(--color-kopi-brown);
                margin-bottom: var(--space-12);
                max-width: 60ch;
                margin-left: auto;
                margin-right: auto;
            }
            
            /* Button Component */
            .btn {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: var(--space-2);
                min-height: 3.5rem;
                padding: var(--space-2) var(--space-8);
                font-family: var(--font-body);
                font-size: var(--text-lg);
                font-weight: 600;
                border: 2px solid transparent;
                border-radius: var(--border-radius);
                cursor: pointer;
                transition: all var(--duration-medium) var(--easing-smooth);
                position: relative;
                overflow: hidden;
            }
            
            .btn::before {
                content: '';
                position: absolute;
                inset: 0;
                background: var(--color-ui-terracotta);
                transform: scaleX(0);
                transform-origin: right;
                transition: transform var(--duration-medium) var(--easing-smooth);
                z-index: -1;
            }
            
            .btn-primary {
                background: var(--color-ui-terracotta);
                color: var(--color-nyonya-cream);
            }
            
            .btn-primary::before {
                background: var(--color-terracotta);
            }
            
            .btn-secondary {
                background: transparent;
                border-color: var(--color-ui-terracotta);
                color: var(--color-ui-terracotta);
            }
            
            .btn:hover::before,
            .btn:focus::before {
                transform: scaleX(1);
                transform-origin: left;
            }
            
            .btn:hover,
            .btn:focus {
                color: var(--color-nyonya-cream);
            }
            
            .btn-group {
                display: flex;
                gap: var(--space-4);
                margin-top: var(--space-6);
            }
            
            /* Peranakan Corner Ornaments */
            .peranakan-corner {
                position: absolute;
                width: clamp(80px, 10vw, 150px);
                height: clamp(80px, 10vw, 150px);
                opacity: 0.6;
                z-index: 0;
                fill: var(--color-ui-blue);
                stroke: var(--color-ui-gold);
                stroke-width: 0.5;
            }
            
            .corner-tl {
                top: var(--space-16);
                left: var(--space-16);
                transform: rotate(-15deg);
            }
            
            .corner-tr {
                top: var(--space-16);
                right: var(--space-16);
                transform: rotate(15deg);
            }
            
            .corner-bl {
                bottom: var(--space-16);
                left: var(--space-16);
                transform: rotate(15deg);
            }
            
            .corner-br {
                bottom: var(--space-16);
                right: var(--space-16);
                transform: rotate(-15deg);
            }
            
            /* Scroll Indicator */
            .scroll-indicator {
                position: absolute;
                bottom: var(--space-16);
                left: 50%;
                transform: translateX(-50%);
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: var(--space-2);
                animation: pulse var(--duration-slow) infinite;
            }
            
            .scroll-text {
                font-size: var(--text-sm);
                color: var(--color-kopi-brown);
                letter-spacing: var(--tracking-loose);
            }
            
            .scroll-arrow {
                width: 24px;
                height: 24px;
                border-right: 2px solid var(--color-ui-terracotta);
                border-bottom: 2px solid var(--color-ui-terracotta);
                transform: rotate(45deg);
            }
            
            /* Folio Frame Component */
            .folio-frame {
                position: relative;
                border: 1px solid rgba(var(--color-kopi-brown-rgb), 0.1);
                border-radius: var(--border-radius);
                overflow: hidden;
                transition: all var(--duration-medium) var(--easing-smooth);
            }
            
            .folio-frame::after {
                content: '';
                position: absolute;
                top: 8px;
                left: 8px;
                right: 8px;
                bottom: 8px;
                border: 1px solid rgba(var(--color-gold-leaf-rgb), 0.2);
                border-radius: calc(var(--border-radius) - 2px);
                pointer-events: none;
            }
            
            .folio-frame:hover {
                transform: translateY(-4px);
                box-shadow: var(--shadow-lg);
                border-color: var(--color-ui-terracotta);
            }
            
            .folio-frame:hover::after {
                border-color: var(--color-gold-leaf);
            }
            
            /* Card Component */
            .card {
                background: var(--color-nyonya-cream);
                padding: var(--space-8);
                border-radius: var(--border-radius);
                position: relative;
            }
            
            .card-image {
                position: relative;
                aspect-ratio: 1;
                margin-bottom: var(--space-6);
                overflow: hidden;
                border-radius: var(--border-radius-sm);
            }
            
            .card-image img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                transition: transform var(--duration-medium) var(--easing-smooth);
            }
            
            .card:hover .card-image img {
                transform: scale(1.05);
            }
            
            .card-title {
                font-size: var(--text-2xl);
                color: var(--color-kopi-brown);
                margin-bottom: var(--space-2);
            }
            
            .card-price {
                font-family: var(--font-decorative);
                font-size: var(--text-xl);
                color: var(--color-ui-gold);
                font-weight: 400;
            }
            
            /* Drop Cap Component */
            .drop-cap {
                position: relative;
                max-width: 65ch;
            }
            
            .drop-cap::first-letter {
                float: left;
                font-family: var(--font-decorative);
                font-size: 5rem;
                line-height: 0.9;
                color: var(--color-terracotta);
                margin-right: var(--space-3);
                margin-top: 0.25em;
                padding-right: var(--space-2);
                border-right: 2px solid var(--color-ui-gold);
            }
            
            /* Section Headers */
            .section-header {
                text-align: center;
                margin-bottom: var(--space-12);
            }
            
            .section-title {
                font-size: var(--text-4xl);
                color: var(--color-ui-terracotta);
                margin-bottom: var(--space-4);
                position: relative;
                display: inline-block;
                left: 50%;
                transform: translateX(-50%);
            }
            
            .section-title::after {
                content: '';
                position: absolute;
                bottom: -8px;
                left: 50%;
                transform: translateX(-50%);
                width: 80px;
                height: 2px;
                background: var(--color-ui-terracotta);
            }
            
            .section-subtitle {
                font-family: var(--font-decorative);
                font-size: var(--text-xl);
                color: var(--color-ui-blue);
                margin-top: var(--space-2);
            }
            
            /* Zig-Zag Layout */
            .zigzag-grid {
                display: flex;
                flex-direction: column;
                gap: var(--space-16);
            }
            
            .zigzag-item {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: var(--space-8);
                align-items: center;
            }
            
            .zigzag-item:nth-child(even) {
                direction: rtl;
            }
            
            .zigzag-item:nth-child(even) .zigzag-content,
            .zigzag-item:nth-child(even) .zigzag-image {
                direction: ltr;
            }
            
            .zigzag-image {
                position: relative;
                aspect-ratio: 1;
            }
            
            .zigzag-image img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                border-radius: var(--border-radius);
            }
            
            .zigzag-content {
                padding: var(--space-6) 0;
            }
            
            .zigzag-title {
                font-size: var(--text-3xl);
                margin-bottom: var(--space-4);
                color: var(--color-ui-terracotta);
            }
            
            .zigzag-price {
                font-family: var(--font-decorative);
                font-size: var(--text-2xl);
                color: var(--color-ui-gold);
                margin: var(--space-4) 0;
            }
            
            /* Peranakan Tile Pattern */
            .tile-pattern {
                width: 100%;
                height: 4px;
                background-image: 
                    linear-gradient(45deg, var(--color-ui-blue) 25%, transparent 25%),
                    linear-gradient(-45deg, var(--color-ui-blue) 25%, transparent 25%),
                    linear-gradient(45deg, transparent 75%, var(--color-ui-blue) 75%),
                    linear-gradient(-45deg, transparent 75%, var(--color-ui-blue) 75%);
                background-size: 16px 16px;
                margin: var(--space-8) 0;
            }
            
            /* Form Component */
            .form-group {
                margin-bottom: var(--space-6);
            }
            
            .form-label {
                display: block;
                font-size: var(--text-lg);
                font-weight: 500;
                margin-bottom: var(--space-2);
                color: var(--color-kopi-brown);
            }
            
            .form-input {
                width: 100%;
                padding: var(--space-3) var(--space-4);
                border: 1px solid rgba(var(--color-kopi-brown-rgb), 0.2);
                border-radius: var(--border-radius);
                font-family: var(--font-body);
                font-size: var(--text-lg);
                transition: all var(--duration-medium) var(--easing-smooth);
            }
            
            .form-input:focus {
                outline: none;
                border-color: var(--color-ui-terracotta);
                box-shadow: 0 0 0 3px rgba(var(--color-terracotta-rgb), 0.15);
            }
            
            /* Footer */
            .footer {
                background: rgba(var(--color-kopi-brown-rgb), 0.03);
                padding: var(--space-16) 0;
                border-top: 1px solid rgba(var(--color-kopi-brown-rgb), 0.08);
                text-align: center;
            }
            
            .footer-container {
                max-width: var(--container-width);
                margin: 0 auto;
                padding: 0 var(--space-4);
            }
            
            .footer-title {
                font-family: var(--font-decorative);
                font-size: var(--text-2xl);
                color: var(--color-ui-terracotta);
                margin-bottom: var(--space-2);
            }
            
            .footer-text {
                font-size: var(--text-sm);
                color: var(--color-kopi-brown);
                line-height: var(--leading-loose);
            }
            
            .footer-links {
                display: flex;
                justify-content: center;
                gap: var(--space-6);
                margin: var(--space-8) 0;
            }
            
            .footer-link {
                color: var(--color-ui-blue);
                font-size: var(--text-lg);
            }
            
            .copyright {
                font-size: var(--text-sm);
                color: var(--color-kopi-brown);
                margin-top: var(--space-4);
            }
        }
        
        /* ===== LAYER 4: UTILITIES ===== */
        @layer utilities {
            .text-center {
                text-align: center;
            }
            
            .text-right {
                text-align: right;
            }
            
            .text-left {
                text-align: left;
            }
            
            .max-w-prose {
                max-width: 65ch;
            }
            
            .mx-auto {
                margin-left: auto;
                margin-right: auto;
            }
            
            .mt-4 {
                margin-top: var(--space-4);
            }
            
            .mt-8 {
                margin-top: var(--space-8);
            }
            
            .mb-4 {
                margin-bottom: var(--space-4);
            }
            
            .mb-8 {
                margin-bottom: var(--space-8);
            }
            
            .mb-12 {
                margin-bottom: var(--space-12);
            }
            
            .mb-16 {
                margin-bottom: var(--space-16);
            }
            
            .mt-16 {
                margin-top: var(--space-16);
            }
            
            .py-24 {
                padding-top: var(--space-24);
                padding-bottom: var(--space-24);
            }
            
            .px-4 {
                padding-left: var(--space-4);
                padding-right: var(--space-4);
            }
            
            .flex {
                display: flex;
            }
            
            .flex-col {
                flex-direction: column;
            }
            
            .items-center {
                align-items: center;
            }
            
            .justify-center {
                justify-content: center;
            }
            
            .gap-4 {
                gap: var(--space-4);
            }
            
            .gap-8 {
                gap: var(--space-8);
            }
            
            .gap-12 {
                gap: var(--space-12);
            }
            
            .hidden {
                display: none;
            }
            
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
            
            @media (max-width: 768px) {
                .hidden-mobile {
                    display: none;
                }
                
                .flex-col-mobile {
                    flex-direction: column;
                }
                
                .text-center-mobile {
                    text-align: center;
                }
            }
        }
        
        /* ===== LAYER 5: OVERRIDES & ANIMATIONS ===== */
        @layer overrides {
            /* Keyframe Animations */
            @keyframes fadeUp {
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            @keyframes pulse {
                0%, 100% { opacity: 0.6; }
                50% { opacity: 1; }
            }
            
            /* Peranakan Corner SVG Paths */
            .peranakan-path {
                fill: none;
                stroke: currentColor;
                stroke-width: 0.5;
                stroke-linecap: round;
                stroke-linejoin: round;
            }
            
            /* Focus Styles for Accessibility */
            :focus-visible {
                outline: 3px solid var(--color-ui-terracotta);
                outline-offset: 2px;
            }
        }
        
        /* ===== RESPONSIVE ADJUSTMENTS ===== */
        @media (max-width: 768px) {
            :root {
                --space-32: 6rem;
                --text-6xl: clamp(2.5rem, 2.2rem + 2.0vw, 3.5rem);
            }
            
            .hero-title {
                font-size: var(--text-5xl);
            }
            
            .hero-subtitle {
                font-size: var(--text-2xl);
            }
            
            .hero {
                padding: var(--space-24) var(--space-4);
            }

            body.menu-open {
                overflow: hidden;
            }

            .menu-trigger {
                display: inline-flex;
                flex-direction: column;
            }

            .nav-links {
                position: fixed;
                inset: 0;
                top: var(--nav-height);
                background-color: var(--color-nyonya-cream);
                flex-direction: column;
                align-items: center;
                justify-content: flex-start;
                padding: var(--space-16) var(--space-8);
                gap: var(--space-4);
                overflow-y: auto;
                -webkit-overflow-scrolling: touch;
                opacity: 0;
                visibility: hidden;
                transform: translateY(10px);
                transition: opacity var(--duration-medium) var(--easing-smooth), transform var(--duration-medium) var(--easing-smooth), visibility var(--duration-medium) var(--easing-smooth);
                z-index: var(--z-modal);
            }

            body.menu-open .nav-links {
                opacity: 1;
                visibility: visible;
                transform: translateY(0);
            }

            body.menu-open .menu-trigger .line-1 {
                transform: rotate(45deg) translate(4px, 4px);
                background-color: var(--color-ui-gold);
            }

            body.menu-open .menu-trigger .line-2 {
                transform: rotate(-45deg) translate(4px, -4px);
                background-color: var(--color-ui-gold);
            }

            .nav-link {
                font-size: var(--text-2xl);
                font-family: var(--font-heading);
                line-height: 1.2;
                padding: var(--space-2) var(--space-2);
            }
            
            .zigzag-item {
                grid-template-columns: 1fr;
            }
            
            .zigzag-item:nth-child(even) {
                direction: ltr;
            }
            
            .btn-group {
                flex-direction: column;
                align-items: center;
            }
            
            .btn {
                width: 100%;
                max-width: 300px;
            }
        }
        
        @media (max-width: 480px) {
            :root {
                --space-24: 4rem;
                --space-32: 5rem;
                --text-5xl: clamp(2.0rem, 1.8rem + 1.5vw, 2.5rem);
                --text-6xl: clamp(2.2rem, 2.0rem + 1.8vw, 2.8rem);
                --text-4xl: clamp(1.8rem, 1.6rem + 1.5vw, 2.2rem);
            }
            
            .hero-title {
                font-size: var(--text-4xl);
            }
            
            .section-title {
                font-size: var(--text-3xl);
            }
            
            .zigzag-title {
                font-size: var(--text-2xl);
            }
            
            .card-image {
                aspect-ratio: 3/4;
            }
            
            .peranakan-corner {
                display: none;
            }
            
            .scroll-indicator {
                display: none;
            }
            
            .tile-pattern {
                height: 2px;
                background-size: 8px 8px;
            }
        }
    </style>
</head>
<body>
    <!-- Global Texture Overlay -->
    <div class="texture-overlay" aria-hidden="true"></div>
    
    <!-- Skip to main content link -->
    <a href="#main-content" class="skip-link">Skip to main content</a>
    
    <!-- Navigation -->
    <header class="header" role="banner">
        <div class="header-container">
            <a href="#" class="logo" aria-label="Merlion Brews Artisan Roastery Home">
                <span class="logo-monogram">☕</span>
                <span class="logo-text">Merlion Brews</span>
            </a>
            <button type="button" class="menu-trigger" aria-controls="main-navigation" aria-expanded="false" aria-label="Open navigation">
                <span class="sr-only">Menu</span>
                <span class="line line-1"></span>
                <span class="line line-2"></span>
            </button>
            <nav id="main-navigation" class="nav-links" aria-label="Main navigation">
                <a href="#beans" class="nav-link">Our Beans</a>
                <a href="#story" class="nav-link">Our Story</a>
                <a href="#tasting-room" class="nav-link">Tasting Room</a>
                <a href="#events" class="nav-link">Events</a>
            </nav>
        </div>
    </header>
    
    <main id="main-content">
        <!-- Hero Section with Floating Coffee Beans -->
        <section class="hero" aria-labelledby="hero-heading">
            <div class="container">
                <div class="hero-content">
                    <h1 id="hero-heading" class="hero-title">Artisan Coffee Crafted with Peranakan Soul</h1>
                    <div class="hero-subtitle">Singapore's Heritage in Every Cup</div>
                    <p class="hero-text">Since 2015, we've been roasting single-origin beans using techniques passed down through generations, blending traditional Singaporean coffee culture with contemporary craft roasting methods. Each batch tells a story of our island's rich multicultural heritage.</p>
                    <div class="btn-group">
                        <a href="#beans" class="btn btn-primary" aria-label="Explore our coffee beans">Discover Our Beans</a>
                        <a href="#tasting-room" class="btn btn-secondary" aria-label="Visit our tasting room">Tasting Experience</a>
                    </div>
                </div>
            </div>
            
            <!-- Floating Coffee Beans Animation -->
            <div class="coffee-bean" style="top: 20%; left: 15%; animation-delay: 0s;"></div>
            <div class="coffee-bean" style="top: 40%; left: 85%; animation-delay: 0.5s;"></div>
            <div class="coffee-bean" style="top: 60%; left: 25%; animation-delay: 1s;"></div>
            <div class="coffee-bean" style="top: 75%; left: 75%; animation-delay: 1.5s;"></div>
            <div class="coffee-bean" style="top: 35%; left: 50%; animation-delay: 2s;"></div>
            
            <!-- Peranakan Corner Ornaments -->
            <svg class="peranakan-corner corner-tl" viewBox="0 0 100 100" aria-hidden="true">
                <path class="peranakan-path" d="M20,80 Q40,60 60,80 T100,80 M10,90 Q30,70 50,90 T90,90 M5,95 Q25,75 45,95 T85,95" stroke-width="1" />
                <circle cx="15" cy="85" r="2" fill="currentColor" />
                <circle cx="35" cy="75" r="1.5" fill="currentColor" />
                <circle cx="55" cy="85" r="2" fill="currentColor" />
                <circle cx="75" cy="75" r="1.5" fill="currentColor" />
                <circle cx="95" cy="85" r="2" fill="currentColor" />
            </svg>
            
            <svg class="peranakan-corner corner-tr" viewBox="0 0 100 100" aria-hidden="true">
                <path class="peranakan-path" d="M80,80 Q60,60 40,80 T0,80 M90,90 Q70,70 50,90 T10,90 M95,95 Q75,75 55,95 T15,95" stroke-width="1" />
                <circle cx="85" cy="85" r="2" fill="currentColor" />
                <circle cx="65" cy="75" r="1.5" fill="currentColor" />
                <circle cx="45" cy="85" r="2" fill="currentColor" />
                <circle cx="25" cy="75" r="1.5" fill="currentColor" />
                <circle cx="5" cy="85" r="2" fill="currentColor" />
            </svg>
            
            <svg class="peranakan-corner corner-bl" viewBox="0 0 100 100" aria-hidden="true">
                <path class="peranakan-path" d="M20,20 Q40,40 60,20 T100,20 M10,10 Q30,30 50,10 T90,10 M5,5 Q25,25 45,5 T85,5" stroke-width="1" />
                <circle cx="15" cy="15" r="2" fill="currentColor" />
                <circle cx="35" cy="25" r="1.5" fill="currentColor" />
                <circle cx="55" cy="15" r="2" fill="currentColor" />
                <circle cx="75" cy="25" r="1.5" fill="currentColor" />
                <circle cx="95" cy="15" r="2" fill="currentColor" />
            </svg>
            
            <svg class="peranakan-corner corner-br" viewBox="0 0 100 100" aria-hidden="true">
                <path class="peranakan-path" d="M80,20 Q60,40 40,20 T0,20 M90,10 Q70,30 50,10 T10,10 M95,5 Q75,25 55,5 T15,5" stroke-width="1" />
                <circle cx="85" cy="15" r="2" fill="currentColor" />
                <circle cx="65" cy="25" r="1.5" fill="currentColor" />
                <circle cx="45" cy="15" r="2" fill="currentColor" />
                <circle cx="25" cy="25" r="1.5" fill="currentColor" />
                <circle cx="5" cy="15" r="2" fill="currentColor" />
            </svg>
            
            <div class="scroll-indicator" aria-hidden="true">
                <div class="scroll-arrow"></div>
                <div class="scroll-text">SCROLL TO EXPLORE</div>
            </div>
        </section>
        
        <!-- Featured Beans Section -->
        <section id="beans" class="section-collections" aria-labelledby="beans-heading">
            <div class="container">
                <div class="section-header">
                    <h2 id="beans-heading" class="section-title">Heritage Bean Collection</h2>
                    <div class="section-subtitle">Single-Origin Mastery</div>
                </div>
                
                <div class="tile-pattern" aria-hidden="true"></div>
                
                <div class="drop-cap">
                    <p>In the tradition of Singapore's kopi masters, we source only the finest beans from sustainable growers across Southeast Asia and beyond. Each variety is roasted in small batches using cast-iron drum roasters, with profiles developed through years of experimentation and respect for the bean's natural characteristics.</p>
                </div>
                
                <div class="zigzag-grid">
                    <!-- Collection 1: Singapore Heritage Blend -->
                    <div class="zigzag-item">
                        <div class="zigzag-image folio-frame">
                            <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400' viewBox='0 0 400 400'%3E%3Crect width='400' height='400' fill='%23F8F3E6'/%3E%3Cpath d='M50,200 Q100,100 200,150 T350,200' stroke='%239A5E4A' stroke-width='2' fill='none'/%3E%3Ccircle cx='150' cy='180' r='30' fill='%234A6B7D' opacity='0.2'/%3E%3Ccircle cx='250' cy='220' r='25' fill='%23C77966' opacity='0.2'/%3E%3Ctext x='200' y='220' font-family='Arial' font-size='16' text-anchor='middle' fill='%233A2A1F' opacity='0.3'%3ESingapore Heritage%3C/text%3E%3C/svg%3E" alt="Singapore Heritage Blend featuring robusta beans with traditional roasting">
                        </div>
                        <div class="zigzag-content">
                            <h3 class="zigzag-title">Singapore Heritage Blend</h3>
                            <p>Our signature blend honoring Singapore's kopi culture, featuring 100% Robusta beans roasted with margarine and sugar in the traditional manner. Bold, full-bodied, and nostalgic—this is the taste of Singapore's kopitiams perfected for the modern palate.</p>
                            <div class="zigzag-price">$28.00 SGD (Incl. 9% GST)</div>
                            <a href="#" class="btn btn-secondary">Add to Cart</a>
                        </div>
                    </div>
                    
                    <!-- Collection 2: Peranakan Single-Origin -->
                    <div class="zigzag-item">
                        <div class="zigzag-image folio-frame">
                            <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400' viewBox='0 0 400 400'%3E%3Crect width='400' height='400' fill='%23F8F3E6'/%3E%3Cpath d='M100,100 Q200,50 300,100 T350,250' stroke='%239A5E4A' stroke-width='2' fill='none'/%3E%3Ccircle cx='200' cy='150' r='40' fill='%234A6B7D' opacity='0.1'/%3E%3Ctext x='200' y='200' font-family='Arial' font-size='16' text-anchor='middle' fill='%233A2A1F' opacity='0.3'%3EPeranakan Estate%3C/text%3E%3C/svg%3E" alt="Peranakan Single-Origin from Indonesian highlands">
                        </div>
                        <div class="zigzag-content">
                            <h3 class="zigzag-title">Peranakan Estate</h3>
                            <p>Single-origin Arabica from the highlands of Indonesia, where Peranakan families have cultivated coffee for generations. Medium roast with notes of dark chocolate, candied orange, and spice—this bean carries the legacy of the Straits Settlements in every sip.</p>
                            <div class="zigzag-price">$32.00 SGD (Incl. 9% GST)</div>
                            <a href="#" class="btn btn-secondary">Add to Cart</a>
                        </div>
                    </div>
                    
                    <!-- Collection 3: Straits Sourcing -->
                    <div class="zigzag-item">
                        <div class="zigzag-image folio-frame">
                            <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400' viewBox='0 0 400 400'%3E%3Crect width='400' height='400' fill='%23F8F3E6'/%3E%3Cpath d='M50,300 Q150,250 250,300 T350,250' stroke='%239A5E4A' stroke-width='2' fill='none'/%3E%3Ccircle cx='150' cy='280' r='25' fill='%234A6B7D' opacity='0.3'/%3E%3Ccircle cx='300' cy='260' r='20' fill='%23C77966' opacity='0.3'/%3E%3Ctext x='200' y='230' font-family='Arial' font-size='16' text-anchor='middle' fill='%233A2A1F' opacity='0.3'%3EStraits Sourcing%3C/text%3E%3C/svg%3E" alt="Straits Sourcing blend with beans from Malaysia and Vietnam">
                        </div>
                        <div class="zigzag-content">
                            <h3 class="zigzag-title">Straits Sourcing</h3>
                            <p>A tribute to the spice routes that shaped Singapore, this blend combines beans from Malaysia, Vietnam, and Thailand. Dark roasted with a hint of cardamom and star anise, it evokes the aromatic markets of old Singapore where merchants traded coffee alongside spices and silks.</p>
                            <div class="zigzag-price">$36.00 SGD (Incl. 9% GST)</div>
                            <a href="#" class="btn btn-secondary">Add to Cart</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- Our Story Section -->
        <section id="story" class="section-about" aria-labelledby="story-heading">
            <div class="container">
                <div class="section-header">
                    <h2 id="story-heading" class="section-title">Our Manuscript</h2>
                    <div class="section-subtitle">A Heritage of Craft</div>
                </div>
                
                <div class="tile-pattern" aria-hidden="true"></div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
                    <div class="folio-frame">
                        <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='600' height='400' viewBox='0 0 600 400'%3E%3Crect width='600' height='400' fill='%23F8F3E6'/%3E%3Ccircle cx='150' cy='200' r='80' fill='%234A6B7D' opacity='0.2'/%3E%3Ccircle cx='450' cy='200' r='60' fill='%23C77966' opacity='0.2'/%3E%3Cpath d='M100,300 Q200,200 300,300 T500,300' stroke='%239A5E4A' stroke-width='3' fill='none'/%3E%3Ctext x='300' y='200' font-family='Arial' font-size='24' text-anchor='middle' fill='%233A2A1F' opacity='0.3'%3EMaster Roaster%3C/text%3E%3C/svg%3E" alt="Master roaster at work with traditional equipment" class="w-full h-auto">
                    </div>
                    
                    <div class="drop-cap">
                        <p>In 2015, after a decade studying coffee roasting techniques across Southeast Asia and Europe, I returned to Singapore with a singular vision: to create coffee that honors both our multicultural heritage and the meticulous craftsmanship of traditional roasting methods.</p>
                        <p>Our roastery in Tiong Bahru operates on principles drawn from Singapore's kopitiams and European roasting traditions. Every cast-iron drum roaster is hand-maintained, every batch roasted by ear and smell, and every bag sealed with the care of a craftsman preserving a legacy. We measure success not in volume, but in the moments of connection our coffee creates.</p>
                        
                        <div class="mt-8 flex items-center gap-4">
                            <svg class="alchemical" viewBox="0 0 24 24" aria-hidden="true" width="24" height="24">
                                <circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="1.5"/>
                                <path d="M12,2 L12,22 M2,12 L22,12 M5,5 L19,19 M5,19 L19,5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                            </svg>
                            <p class="italic" style="font-style: italic; color: var(--color-ui-blue);">"In coffee, we transform not just beans, but moments into memories."</p>
                        </div>
                        
                        <div class="mt-6">
                            <p class="font-heading" style="font-family: var(--font-decorative); font-size: var(--text-lg); color: var(--color-ui-terracotta);">
                                — Marcus Lim, Founder & Master Roaster
                            </p>
                            <p class="text-kopi-brown" style="color: var(--color-kopi-brown); font-size: var(--text-sm); margin-top: var(--space-1);">
                                Former roaster at Blue Bottle • Certified Q Grader • Heritage Preservation Advocate
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- Tasting Room Section -->
        <section id="tasting-room" class="section-tasting-room" aria-labelledby="tasting-room-heading">
            <div class="container">
                <div class="section-header">
                    <h2 id="tasting-room-heading" class="section-title">Tasting Room</h2>
                    <div class="section-subtitle">Experience Our Craft</div>
                </div>
                
                <div class="tile-pattern" aria-hidden="true"></div>
                
                <div class="drop-cap">
                    <p>Step into our Tiong Bahru tasting room, where the aroma of freshly roasted beans mingles with the scent of heritage Peranakan tiles. This is where we host intimate cupping sessions, brewing workshops, and private tastings—each experience designed to deepen your appreciation for the art and science of coffee.</p>
                </div>
                
                <div class="grid gap-8 mt-8">
                    <div class="card folio-frame">
                        <h3 class="card-title">Heritage Cupping Session</h3>
                        <p>An immersive journey through three generations of Singaporean coffee culture. Taste traditional kopi alongside our contemporary single-origin roasts, guided by our master roasters who share stories of Singapore's evolving coffee landscape.</p>
                        <div class="card-price">$45.00 per person</div>
                        <button class="btn btn-secondary">Book Experience</button>
                    </div>
                    
                    <div class="card folio-frame">
                        <h3 class="card-title">Brewing Masterclass</h3>
                        <p>Learn the techniques behind perfect pour-over, French press, and traditional sock brewing. Take home your own brew kit and a bag of freshly roasted beans to continue your coffee journey at home.</p>
                        <div class="card-price">$65.00 per person</div>
                        <button class="btn btn-secondary">Book Class</button>
                    </div>
                    
                    <div class="card folio-frame">
                        <h3 class="card-title">Private Tasting Room</h3>
                        <p>Host your next gathering in our intimate tasting room. Perfect for team building, client meetings, or special celebrations. Includes a customized tasting menu, light bites, and dedicated roaster host.</p>
                        <div class="card-price">$350.00 for up to 8 guests</div>
                        <button class="btn btn-secondary">Reserve Room</button>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- Events Section -->
        <section id="events" class="section-events" aria-labelledby="events-heading">
            <div class="container">
                <div class="section-header">
                    <h2 id="events-heading" class="section-title">Cultural Gatherings</h2>
                    <div class="section-subtitle">Community & Connection</div>
                </div>
                
                <div class="tile-pattern" aria-hidden="true"></div>
                
                <div class="drop-cap">
                    <p>Coffee has always been a catalyst for connection. At Merlion Brews, we host regular cultural events that celebrate Singapore's multicultural heritage—from Peranakan tea ceremonies to Malay storytelling nights, each event is designed to bring our community together over shared stories and exceptional coffee.</p>
                </div>
                
                <div class="grid gap-8 mt-8">
                    <div class="card folio-frame">
                        <h3 class="card-title">Peranakan Coffee Ceremony</h3>
                        <p>Experience the ritual of traditional Peranakan coffee preparation, accompanied by kueh and stories of the Straits Settlements. Led by cultural historian Aunty Mei Ling, this monthly gathering honors the women who kept these traditions alive through generations.</p>
                        <p><strong>Next Date:</strong> Saturday, 18 January 2026 • 3:00 PM - 5:00 PM</p>
                        <button class="btn btn-secondary">Reserve Spot</button>
                    </div>
                    
                    <div class="card folio-frame">
                        <h3 class="card-title">Storytelling & Single-Origin</h3>
                        <p>Join local storyteller Raj Verma for an evening of Singaporean folk tales, accompanied by a flight of three single-origin coffees that mirror the stories' themes. This quarterly event celebrates the oral traditions that have shaped our island's identity.</p>
                        <p><strong>Next Date:</strong> Friday, 24 January 2026 • 7:00 PM - 9:00 PM</p>
                        <button class="btn btn-secondary">Reserve Spot</button>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- Newsletter Section -->
        <section id="newsletter" class="section-newsletter" aria-labelledby="newsletter-heading">
            <div class="container text-center">
                <div class="section-header">
                    <h2 id="newsletter-heading" class="section-title">Join Our Manuscript</h2>
                    <div class="section-subtitle">Receive Exclusive Insights</div>
                </div>
                
                <div class="tile-pattern" aria-hidden="true"></div>
                
                <div class="max-w-prose mx-auto">
                    <p class="mb-8">Subscribe to receive quarterly manuscript pages featuring bean discoveries, roasting techniques, and invitations to our private tasting salons in Tiong Bahru. As a welcome gift, receive 15% off your first coffee order.</p>
                    
                    <form class="max-w-md mx-auto">
                        <div class="form-group">
                            <label for="email" class="sr-only">Email address</label>
                            <input type="email" id="email" class="form-input" placeholder="Your illuminated email address..." required>
                        </div>
                        <button type="submit" class="btn btn-primary mx-auto">Seal Your Subscription</button>
                    </form>
                    
                    <p class="mt-4 text-sm" style="color: var(--color-kopi-brown); font-size: var(--text-sm);">
                        We respect your privacy. Your email will never be shared, and you may unsubscribe at any time. 
                        GST is included in all prices for Singapore customers.
                    </p>
                </div>
            </div>
        </section>
    </main>
    
    <!-- Footer -->
    <footer class="footer" role="contentinfo">
        <div class="footer-container">
            <div class="footer-title">☕ Merlion Brews Artisan Roastery</div>
            <p class="footer-text">Heritage coffee crafted with Peranakan soul since 2015</p>
            
            <div class="footer-links">
                <a href="#beans" class="footer-link">Our Beans</a>
                <a href="#story" class="footer-link">Our Story</a>
                <a href="#tasting-room" class="footer-link">Tasting Room</a>
                <a href="#events" class="footer-link">Events</a>
                <a href="#" class="footer-link">Contact</a>
            </div>
            
            <div class="tile-pattern" aria-hidden="true"></div>
            
            <p class="copyright">
                Roastery: 48 Tiong Bahru Road, #01-12, Singapore 168893<br>
                Business Registration: 2015123456K • GST Registration: M9-1234567-8<br>
                © 2026 Merlion Brews Artisan Roastery Pte. Ltd. Singapore • All rights reserved<br>
                Prices displayed in SGD with 9% GST included for Singapore customers
            </p>
        </div>
    </footer>
    
    <script>
        // Intersection Observer for scroll animations
        document.addEventListener('DOMContentLoaded', () => {
            // Hero content animation trigger
            setTimeout(() => {
                document.querySelector('.hero-content').style.animation = 'fadeUp ' + getComputedStyle(document.documentElement).getPropertyValue('--duration-slow') + ' ' + getComputedStyle(document.documentElement).getPropertyValue('--easing-smooth') + ' forwards';
            }, 300);
            
            // Scroll reveal for sections
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                        observer.unobserve(entry.target);
                    }
                });
            }, observerOptions);
            
            // Observe all section content
            document.querySelectorAll('section > .container, .zigzag-item, .card').forEach(element => {
                element.style.opacity = '0';
                element.style.transform = 'translateY(20px)';
                element.style.transition = 'opacity ' + getComputedStyle(document.documentElement).getPropertyValue('--duration-medium') + ' ' + getComputedStyle(document.documentElement).getPropertyValue('--easing-smooth') + ', transform ' + getComputedStyle(document.documentElement).getPropertyValue('--duration-medium') + ' ' + getComputedStyle(document.documentElement).getPropertyValue('--easing-smooth');
                observer.observe(element);
            });
            
            // Form submission prevention for demo
            document.querySelector('form').addEventListener('submit', (e) => {
                e.preventDefault();
                const email = document.getElementById('email').value;
                if (email) {
                    alert('Thank you for joining our manuscript! You will receive a confirmation email shortly with your 15% discount code.');
                    document.getElementById('email').value = '';
                }
            });
            
            // Add coffee bean animation timing variations
            document.querySelectorAll('.coffee-bean').forEach((bean, index) => {
                bean.style.animationDuration = `${3 + index * 0.5}s`;
                bean.style.animationDelay = `${index * 0.3}s`;
            });

            const body = document.body;
            const menuButton = document.querySelector('.menu-trigger');
            const nav = document.getElementById('main-navigation');

            if (menuButton && nav) {
                const setMenuState = (isOpen, options = {}) => {
                    const { focus = true } = options;
                    if (isOpen) {
                        body.classList.add('menu-open');
                        menuButton.setAttribute('aria-expanded', 'true');
                        menuButton.setAttribute('aria-label', 'Close navigation');
                        if (focus) {
                            const firstLink = nav.querySelector('a');
                            if (firstLink) firstLink.focus();
                        }
                        return;
                    }

                    body.classList.remove('menu-open');
                    menuButton.setAttribute('aria-expanded', 'false');
                    menuButton.setAttribute('aria-label', 'Open navigation');
                    if (focus) menuButton.focus();
                };

                menuButton.addEventListener('click', () => {
                    const isOpen = body.classList.contains('menu-open');
                    setMenuState(!isOpen, { focus: true });
                });

                nav.querySelectorAll('a').forEach((link) => {
                    link.addEventListener('click', () => {
                        if (body.classList.contains('menu-open')) {
                            setMenuState(false, { focus: false });
                        }
                    });
                });

                document.addEventListener('keydown', (e) => {
                    if (e.key === 'Escape' && body.classList.contains('menu-open')) {
                        setMenuState(false, { focus: true });
                    }
                });

                window.addEventListener('resize', () => {
                    if (window.innerWidth > 768 && body.classList.contains('menu-open')) {
                        setMenuState(false, { focus: false });
                    }
                });
            }
        });
    </script>
</body>
</html>
```

---

## Executive summary

Deliver a production-ready, maintainable, secure, and scalable full-stack e-commerce platform tailored for Singapore SMB cafés (Merlion Brews).
Stack chosen by you is used as first-class: **Next.js 15 + Tailwind + shadcn-ui** for the frontend (headless), **Laravel 12 (PHP 8.3+)** as the backend API, **Postgres 16** for the data store, and **Docker** for deployment. Architecture is headless, API-first, and modular to allow future mobile apps, POS integration, and marketplace channels.

Key capabilities:

* Content-driven marketing landing page (the provided mockup). 
* Full product catalogue (products, SKUs/variants, pricing with GST calculations).
* Shopping cart + checkout + Stripe payment integration (PCI via Stripe).
* Orders, inventory, fulfillment, receipts.
* Tasting-room events & bookings (calendar, capacity).
* Admin portal (catalog, orders, inventory, events, reports).
* Newsletter & subscription management.
* Robust security, tests, CI/CD, monitoring, backups.

---

# 1. High-level architecture (textual diagram)

```
[User Browsers / Mobile] 
    ↕ HTTPS
[Next.js 15 Frontend (app dir)]  ←→  [Stripe / Email / 3rd-party APIs]
    ↕ REST/GraphQL (API layer)
[API Gateway / Nginx] → [Laravel 12 API (php-fpm)] 
    ↔ Redis (cache & queue)
    ↔ Postgres 16 (primary DB)
    ↔ S3-compatible object storage (media)
    ↔ Workers (queue: payments, email, invoices)
    ↔ Background jobs (Laravel Queues + Horizon)
All services run in Docker containers (compose / k8s manifests)
```

**Design notes**

* Next.js uses server components for marketing pages and client components for cart/checkout interactions. Use incremental/static rendering where appropriate to maximize performance.
* Laravel is headless API (JSON) serving business logic, authorization, webhooks, admin UI APIs, and reports.
* Postgres stores transactional data; Redis used for session/cache/queue.
* S3 or S3-compatible (MinIO) for media and product images.
* Stripe for payments; webhooks handled by Laravel.
* Docker for development and production images (multi-stage builds). Optionally deploy to Kubernetes for scale.

---

# 2. Domain model & major entities

Core entities (tables shown later in schema):

* `users` (customers + staff, role-based)
* `products` (catalog)
* `product_variants` (SKU, weight/pack sizes)
* `prices` (list price, currency, GST included flag)
* `inventory` (stock_count per sku/location)
* `orders`, `order_items`, `payments`
* `events` (tasting sessions), `bookings`
* `subscriptions` (newsletter)
* `pages`/`cms_entries` (marketing content)
* `media_assets`
* `audit_logs` / `activity_logs`

---

# 3. API design (sample endpoints — RESTful)

Use JSON:API-style structure or REST with consistent shapes. Authentication: **Laravel Sanctum (token)** for single-page app and cookie-based for admin sessions. Use scoped tokens for API clients.

### Public (no-auth)

* `GET /api/v1/products?category=&q=&page=&limit=`
* `GET /api/v1/products/{id}`
* `GET /api/v1/collections`
* `POST /api/v1/cart` — create cart / add item
* `PUT /api/v1/cart/{cart_id}` — update cart items
* `POST /api/v1/checkout` — create order (guest) → returns `checkout_session`
* `POST /api/v1/webhooks/stripe` — Stripe webhooks (payment_intent, charge.succeeded)

### Customer (token)

* `POST /api/v1/auth/register`
* `POST /api/v1/auth/login`
* `GET /api/v1/users/me`
* `GET /api/v1/orders` (customer order history)
* `POST /api/v1/subscriptions` (newsletter)

### Admin (role-protected)

* `GET /api/v1/admin/products`
* `POST /api/v1/admin/products`
* `PATCH /api/v1/admin/products/{id}`
* `POST /api/v1/admin/inventory/adjust`
* `GET /api/v1/admin/orders`
* `POST /api/v1/admin/events`
* `GET /api/v1/admin/reports/sales?from=&to=`

**Example request/response (checkout)**

`POST /api/v1/checkout`

```json
{
  "cart_id":"abc123",
  "customer": { "email":"a@example.com", "name":"Alex" },
  "shipping": { "method":"pickup", "location_id": "tongbahru" },
  "payment_method": "stripe"
}
```

Response:

```json
{ "order_id": 987, "status":"pending_payment", "stripe_checkout_url": "https://checkout.stripe.com/..." }
```

**Webhooks**: Validate signatures, idempotency keys, and update order/payment statuses.

---

# 4. Database schema (core tables — Postgres 16)

Below are representative `CREATE TABLE` examples (truncated). Use UUID PKs for public-facing IDs.

```sql
-- extensions
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE users (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  email text UNIQUE NOT NULL,
  password_hash text,
  name text,
  role text NOT NULL DEFAULT 'customer', -- customer|admin|staff
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

CREATE TABLE products (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  slug text UNIQUE NOT NULL,
  title text NOT NULL,
  description text,
  published boolean DEFAULT true,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

CREATE TABLE product_variants (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  product_id uuid REFERENCES products(id) ON DELETE CASCADE,
  sku text UNIQUE NOT NULL,
  weight_g int,
  price_cents int NOT NULL, -- store cents
  currency text DEFAULT 'SGD',
  gst_included boolean DEFAULT true,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now()
);

CREATE TABLE inventory (
  sku text PRIMARY KEY,
  stock_count int NOT NULL DEFAULT 0,
  location text DEFAULT 'main_roastery',
  updated_at timestamptz DEFAULT now()
);

CREATE TABLE orders (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid REFERENCES users(id),
  total_cents int NOT NULL,
  currency text DEFAULT 'SGD',
  status text NOT NULL DEFAULT 'draft', -- draft, placed, paid, fulfilled, cancelled
  metadata jsonb,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE order_items (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id uuid REFERENCES orders(id) ON DELETE CASCADE,
  variant_id uuid REFERENCES product_variants(id),
  sku text,
  quantity int NOT NULL,
  unit_price_cents int NOT NULL,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE payments (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  order_id uuid REFERENCES orders(id),
  provider text,
  provider_payment_id text,
  amount_cents int,
  currency text,
  status text,
  raw_response jsonb,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE events (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  title text,
  description text,
  start_at timestamptz,
  end_at timestamptz,
  capacity int,
  price_cents int,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE bookings (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  event_id uuid REFERENCES events(id),
  user_id uuid REFERENCES users(id),
  seats int,
  status text DEFAULT 'confirmed',
  created_at timestamptz DEFAULT now()
);

CREATE TABLE subscriptions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  email text NOT NULL UNIQUE,
  verified boolean DEFAULT false,
  created_at timestamptz DEFAULT now()
);
```

**Schema notes**

* Store money as integer cents for accuracy.
* Use JSONB `metadata` for flexible extensions.
* Add indexes on `orders.status`, `product_variants.sku`, `events.start_at` for query performance.

---

# 5. Frontend architecture (Next.js 15 + Tailwind + shadcn-ui)

Folder layout (recommended `app/` directory):

```
/app
  /(marketing)
    /layout.tsx         -- site layout + header/footer
    /page.tsx           -- landing hero, uses static props
  /shop
    /page.tsx           -- product listing (ISR)
    /products/[slug]/page.tsx -- product detail
  /cart
    /page.tsx
  /checkout
    /page.tsx
  /dashboard (optional admin SPA)
  /api (edge functions or server actions)
 /components
  /ui (shadcn wrappers)
  /product
  /cart
  /layout
  /icons (lucide-react)
```

**Rendering strategy**

* Landing page and content: SSG/ISR (static generation + revalidate).
* Product pages: Incremental static regenerate on product update (webhook trigger).
* Checkout flow: client-side with server session: call backend create checkout, redirect to Stripe checkout, or do PaymentIntents with client secret.
* Use `use-swrlike` for cart cache or React Query for async state.

**Styling**

* Tailwind with design tokens (adapt from `cafe.html` tokens).
* shadcn-ui primitives for accessible components. Build a `ui` layer that maps the Peranakan design tokens to Tailwind variables.

**Accessibility**

* WCAG AAA target where feasible for contrast and keyboard focus states (mockup already includes good a11y patterns). 

---

# 6. Backend architecture (Laravel 12 specifics)

**Structure**

* HTTP controllers: `ProductController`, `CartController`, `CheckoutController`, `OrderController`, `EventController`, `Admin\ProductController`, ...
* API Resources for consistent JSON serialization.
* Policies & Gates for RBAC (roles: admin/staff/customer).
* Jobs & Queues: `ProcessPayment`, `SendOrderEmail`, `GenerateInvoice`.
* Notifications: Emails (Mailables), Push (if needed).
* Use Laravel Sanctum for SPA auth; use OAuth tokens for third-party API clients if needed.

**Key packages**

* `laravel/sanctum` (auth)
* `laravel/passport` (optional)
* `spatie/laravel-permission` (roles & permissions)
* `spatie/laravel-activitylog` (audit)
* `spatie/laravel-medialibrary` (media)
* `laravel/horizon` (queue monitoring)
* `laravel/telescope` (dev only)
* `spatie/laravel-backup` (backups)

**Inventory & concurrency**

* Use DB-level transactions for order creation and inventory decrement. Prefer `SELECT ... FOR UPDATE` or `UPDATE ... WHERE stock_count >= n` patterns to avoid oversell.
* Leverage optimistic locking / versioning if multiple warehouses.

---

# 7. Payments & GST handling (Singapore specifics)

* Use Stripe Checkout or Payment Intents. PCI scope is minimized using Stripe hosted pages or Elements.
* Compute GST (9% as in mockup) at order creation: store both `subtotal_cents` and `gst_cents`, `total_cents`.
* Display prices inclusive of GST on storefront as per Singapore rules; show breakdown on checkout page.
* Ensure invoices include business registration & GST registration details (mockup footer shows these). 

Tax example:

```
gst_cents = round(subtotal_cents * 0.09)
total = subtotal_cents + gst_cents + shipping_cents
```

---

# 8. DevOps & deployment (Docker-first)

**Docker services (compose)**:

* `nginx` (reverse proxy)
* `web` (Next.js build & server — or Vercel for Next)
* `php` (php-fpm + Laravel)
* `worker` (queue worker)
* `postgres` (Postgres 16)
* `redis` (cache & queue)
* `minio` or `s3` for media
* `traefik` or ingress if k8s

**Sample `docker-compose` (skeleton)**

```yaml
version: '3.8'
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: merch
      POSTGRES_USER: laravel
      POSTGRES_PASSWORD: secure
    volumes:
      - db_data:/var/lib/postgresql/data
  redis:
    image: redis:7
  php:
    build: ./docker/php
    depends_on: [postgres, redis]
  nginx:
    image: nginx:stable
    ports: ["80:80", "443:443"]
    depends_on: [php]
  next:
    build: ./frontend
    environment:
      NEXT_PUBLIC_API_URL: "https://api.example.com"
volumes:
  db_data:
```

**CI/CD**

* GitHub Actions pipeline:

  * Lint + typecheck (frontend), phpstan + php-cs-fixer (backend)
  * Test suites: `npm test`, `composer test`
  * Build artifacts: frontend static export (for Vercel) or Docker image push to registry
  * Deploy via Helm/Flux or cloud provider (ECS/EKS/Cloud Run)

**Secrets**

* Use secrets manager (AWS Secrets Manager / Vault) — never bake secrets into images.
* Configure per-environment `.env` injected at runtime.

---

# 9. Observability, monitoring, backups

* Logs: centralized (ELK / Grafana Loki)
* Metrics: Prometheus + Grafana (requests, DB locks, queue length)
* Error reporting: Sentry
* Backups: daily DB dump to object store, retention policy 30 days
* Healthchecks and uptime probes for services

---

# 10. Testing & QA

* Unit tests (Laravel: PHPUnit; Next: Vitest/React Testing Library)
* Integration tests for API endpoints
* End-to-end tests with Cypress (checkout flows, bookings)
* Accessibility audits (axe-core)
* Load test critical paths (orders/checkout) with k6

---

# 11. Security checklist

* HTTPS everywhere (HSTS)
* CSP, X-Frame-Options, X-XSS-Protection headers
* Rate limiting (login, checkout, webhooks)
* Input validation + output encoding
* Use prepared statements; avoid raw SQL where possible
* Implement role-based access control (spatie/permission)
* Webhook signature verification (Stripe signing)
* Secure cookies + CSRF protection for forms (Laravel default)
* Regular dependency vulnerability scanning (Snyk or Dependabot)

---

# 12. Performance & cost optimizations

* CDN for public assets & images (Cloudflare / Cloudfront)
* Image optimization (next/image or external optimizer)
* SSR + SSG judiciously for SEO and speed (marketing pages static)
* Caching: product listing cache + stale-while-revalidate
* Database indexing and read replicas if traffic grows

---

# 13. UX & Frontend implementation notes (mapping from `cafe.html`)

* Preserve the Peranakan token system (colors, typography) as Tailwind design tokens. The mockup's tokens should be implemented as CSS variables and mapped in `tailwind.config.js`. 
* Use shadcn-ui components for accessible buttons/inputs; wrap them to implement the unique microinteractions (floating beans, peranakan corners, folio-frame).
* Handle UI states thoroughly: loading, error, empty, success.
* Mobile-first breakpoints, test keyboard navigation for burger menu interactions (the mockup already has menu handling that will be ported to React). 

---

# 14. Operational concerns & edge cases (risk assessment)

**Risks & mitigations**

* *Oversell inventory during concurrent checkouts* → Use DB transactions and `UPDATE inventory SET stock_count = stock_count - n WHERE stock_count >= n` pattern; confirm order only after successful decrement.
* *Payment failure mid-checkout* → hold order in `pending_payment`. Retry webhooks idempotently and provide user-friendly status updates.
* *GDPR/PDPA* → For Singapore PDPA: minimal data collection, clear privacy policy, opt-in newsletters, easy unsubscribe.
* *Third-party outages (Stripe)* → fallback: allow offline/CC on invoice (admin) and queue actions.
* *Scale* → prepare for horizontal scaling: stateless app servers, central Redis, read replicas for Postgres.

---

# 15. Validation checklist (pre-implementation gates)

Before coding, validate these items (each is a checkpoint):

* [ ] **Vision & scope**: final acceptance of features (catalog, checkout, events, admin, newsletter).
* [ ] **Data model accepted**: product/variant/price/inventory tables match business rules (GST inclusive, returns policy).
* [ ] **Payment provider selected**: Stripe (or alternate) — merchant account & test keys available.
* [ ] **Hosting & domain**: production hosting chosen (Vercel for Next, self-hosted Docker / k8s for Laravel) and TLS certs procured.
* [ ] **Third-party integrations**: SMTP provider, analytics, CDN selected and credentials available.
* [ ] **Compliance**: PDPA/GST invoicing requirements validated.
* [ ] **Admin user list**: initial admins created for deployment.

I have validated the PAD against the supplied static mockup (design tokens, layout intent, event/newsletter flows) and the architecture described above is consistent with the mockup's structure and features. 

---

# 16. Implementation plan (phases & checklists) — high level (no time estimates)

**Phase A — Validate & bootstrap**

* Confirm checkpoints in section 15.
* Create Git monorepo: `/frontend` (Next), `/backend` (Laravel).
* Create CI skeleton, Dockerfiles, `docker-compose.dev.yml`.

**Phase B — Backend core**

* Implement DB schema migrations.
* Build Product & Variant APIs + seeders (example data from mockup).
* Implement authentication (Sanctum), admin role scaffolding.
* Implement inventory & order transactions.
* Setup Stripe integration and webhook endpoint.
* Add email templates & queue workers.

**Phase C — Frontend**

* Scaffold Next.js app directory and Tailwind config (map design tokens).
* Recreate landing page from `cafe.html` (static), using shadcn UI components.
* Build product listing/detail, cart, checkout flow.
* Integrate with backend APIs for dynamic data.

**Phase D — Events & Bookings**

* Build event CRUD on backend and booking flow on frontend.
* Calendar availability checks and seat counts.

**Phase E — Admin & Reports**

* Admin endpoints and simple admin UI (could be Next.js protected route or Laravel Nova / custom panel).
* Sales, bookings, inventory reports.

**Phase F — Hardening & release**

* Run full test suite, accessibility audit.
* Setup logging, monitoring, backups.
* Production deploy (Docker images to registry, infra).

**Phase G — Post-launch**

* Monitoring, iterative UX fixes, payment reconciliation, marketing analytics.

---

# 17. Deliverables I will provide (if you want me to implement next)

* Complete repository structure for frontend & backend.
* Production-ready `Dockerfile`/`docker-compose` and Kubernetes manifests (optional).
* Full set of Laravel migrations, models, controllers, API resources, and tests for core flows.
* Next.js components/pages implementing the landing page and shop flows, with Tailwind tokens and shadcn wrappers.
* End-to-end test suite (Cypress) for critical customer flows.
* CI/CD GitHub Actions workflows.
* Runbook: deployment steps, rollback, backup/restore, incident triage.

---

# 18. Assumptions & open questions (explicit)

I validated the plan against the mockup and business context. These assumptions were made — callouts you should confirm before implementation:

1. **Payment provider**: default to Stripe. If alternative (e.g., PayNow integration required), that changes the payment/checkout design.
2. **Fulfilment**: default single pickup location (Tiong Bahru) + shipping absent. If nationwide delivery needed, shipping rates & logistics integration required. 
3. **Admin scope**: we assume a web admin panel is acceptable; if you require POS offline integration, that is a separate module.
4. **Localization**: default English (Singapore). Multi-language adds content work.
5. **Hosting**: assume container-based hosting. If you prefer managed Next.js (Vercel) + Laravel on PaaS, we adapt.

---

# 19. Acceptance criteria (what “done” looks like)

* Landing page faithfully rendered from `cafe.html` and fully responsive. 
* Product catalogue + product pages working through API.
* Cart + checkout flow that charges successfully via Stripe and creates `orders` in Postgres.
* Admin can view orders, adjust inventory, create/edit products, and create events.
* Events display and booking flow create `bookings` and reduce availability.
* Tests: unit coverage for core business logic; e2e for checkout.
* Deployable via Docker, with backups and alerts configured.

---

# 20. Immediate next steps (what I will do now if you want me to proceed)

I have validated this PAD against the mockup and stacks you provided. If you want me to **implement**, I will begin by generating the repository scaffolding (monorepo), initial Docker configs, and core migrations — producing first PRs that you can review.

*(I will not start implementing automatically without your explicit “go ahead.” If you prefer, tell me which artifact to generate first — e.g., `Initial Laravel migrations + Dockerfile`, or `Next.js landing page replica` — and I will produce that code immediately.)*

---

Now, please think deeper and think harder to deeply explore thoroughly and systematically 3 different ways to critique and re-imagine your initial PAD, then plan and create an improved and refined PAD. Use extensive web searches to explore and validate your thinking and assumptions, and to ground yourself in the best practices on the design and architectural details.

---

# Re-imagining the PAD — three rigorous critique lenses, and a refined, production-ready PAD

Great — I dug in critically and reframed the original PAD across three different, deep critique perspectives (each with clear trade-offs and concrete design changes). I used current vendor and standards docs to validate assumptions and ground recommendations. After the three critiques I present a single **improved, refined PAD** (actionable, copy-pasteable checkpoints, and validation gates) you can take straight into engineering.

> Citations: I reference vendor/standards sources for the most important claims below (Next.js 15 behavior, Laravel 12 notes, Postgres 16 capabilities, Singapore GST rules, Stripe webhook/idempotency). See inline citations after the relevant paragraphs.

---

# Part A — Three distinct critiques (each is a different way to rethink the PAD)

### Critique 1 — **Architectural topology: Monolith API-first → BFF vs Microservices vs Edge-first**

**Summary:** The original PAD assumes a monolithic Laravel API + Next.js frontend. That’s fine—but it locks some choices (hosting, scale patterns, offline POS integration). Three viable alternatives:

1. **Refined Monolith (API-first + headless Laravel) — incremental, pragmatic**

   * Keep one Laravel API (bounded contexts in the same codebase), use Next.js as headless storefront/BFF.
   * Pros: simpler operational model, lower DevOps overhead, faster time-to-market for SMB.
   * Cons: harder to independently scale hot paths (checkout), risk of coupling admin and public traffic spikes.
   * When to choose: MVP → mature single-region operations, limited team.

2. **BFF (Backend-for-Frontend) hybrid — Next.js takes BFF role for UX-critical flows**

   * Let Next.js handle time-sensitive, UX-first logic (caching, edge server actions, personalization), while Laravel becomes a set of domain services (orders, inventory, events).
   * Pros: best of both worlds — Next.js can use server components/edge to speed critical UX; Laravel focuses on business rules and data integrity.
   * Cons: more cross-layer contracts; requires disciplined API versioning.
   * When to choose: you want low-latency UX (cart/checkout), SEO on marketing pages, and still need a robust backend for transactional consistency.

3. **Event-driven microservices (domain services + queue + read-models)**

   * Decompose orders, inventory, payments, and events into services communicating via events (Kafka/Redis Streams).
   * Pros: scales well, easier to add POS integration, offline sync, and multi-region replication.
   * Cons: significantly higher complexity, observability burden, and cost.
   * When to choose: multiple sales channels, future POS integration, high concurrent traffic, or planned multi-location growth.

**Recommendation (practical):** Start with **BFF hybrid** (option 2). It gives higher-perceived performance on storefront and keeps Laravel as the canonical domain authority for transactions and inventory. You can refactor further toward microservices later with event boundaries already defined.

> Grounding: Next.js 15’s App Router + server components empower using Next as a high-performance BFF and edge-powered rendering layer. ([Next.js][1])

---

### Critique 2 — **Data integrity and inventory concurrency (DB & transaction design)**

**Problem:** e-commerce inventory is a classic race condition — simultaneous checkouts can oversell stock if handled incorrectly. The original PAD mentions transactions but needs explicit DB patterns and fallback guarantees.

**Three approaches to inventory safety:**

1. **DB pessimistic locking (SELECT FOR UPDATE) inside a single transactional boundary** — reliable, simple, works with single DB primary. Best for low-to-moderate concurrency.
2. **Atomic `UPDATE ... WHERE stock_count >= n` pattern with affected-row check** — safe, lower lock impact; good for moderate concurrency.
3. **CQRS + event sourcing (write model separate from read model)** — use a write-side service to serialize inventory decrements, publish events to read-models. Best for high throughput and eventual consistency scenarios.

**Recommendation:** Use *atomic DB updates with transactional confirmation* for the order path to prevent oversell, and add a **compensating job** to reconcile mismatches (queue-driven). For long-term scaling, adopt a CQRS pattern and migrate the inventory write path to a small service that serializes updates. Leverage Postgres 16 performance and replication features for scale. ([PostgreSQL][2])

---

### Critique 3 — **Developer experience, deployment and cost: managed serverless vs container-first**

**Problem:** The PAD assumes Docker for everything. That’s sensible, but there are nuanced choices about hosting Next.js (Vercel/Edge), Laravel (managed containers/PaaS), and cost for SMBs.

**Three hosting patterns:**

1. **Frontend: Vercel (managed) + Backend: Managed Docker (Fargate / App Platform / DigitalOcean Apps)**

   * Fast iteration, infra reduced; Vercel optimizes Next builds & incremental static regeneration. Great DX. But mixing providers increases operational surface.
2. **Full containerized stack (Docker Compose / Kubernetes)**

   * Highest control and portability but higher operational cost and complexity.
3. **Hybrid (Next.js on Vercel or edge, Laravel as containers on a single cloud provider)**

   * Balanced: Vercel for CDN/edge, Laravel containers in one cloud for data locality (compliance).

**Recommendation:** For Singapore SMB cafés, choose **Hybrid**: Next.js on Vercel (or similar edge hosting) for best storefront performance and CDN benefits, Laravel in containerized managed service (Fargate / App Platform) to keep a single-region DB and lower ops cost. This reduces latency for customers while keeping backend control and lower ops burden.

**Grounding:** Next.js docs and release notes emphasize App Router/server components and edge performance benefits; this pattern is industry-standard for performant storefronts. ([Next.js][1])

---

# Part B — The improved, refined PAD (actionable & validated)

Below is a concise, production-ready PAD that implements the BFF hybrid recommendation, plus all operational and security improvements from the critiques.

## Executive summary (single paragraph)

A headless, API-first e-commerce platform for Singapore cafés: **Next.js 15 (App Router + server components) on the edge** as the storefront and BFF for UX flows; **Laravel 12 (PHP 8.3-compatible)** as the authoritative domain API for orders, inventory, events, and admin; **Postgres 16** as the transactional data store; **Redis** for cache & jobs; **Stripe** for payments; **Docker** for backend deployment; **Vercel** (or equivalent) for frontend hosting. This hybrid enables fast UX, strong transactional guarantees, easy admin tooling, and a clear migration path to event-driven architecture if needed.

---

## 1) Tech decisions & rationale (short)

* **Frontend:** Next.js 15 App Router, Tailwind CSS 4, shadcn UI. Use server components for marketing + SSR; client components for cart/checkout interactivity. (Performance & modern React features). ([Next.js][3])
* **Backend:** Laravel 12, API-first (JSON), Sanctum tokens for SPA auth, Role-based policies via `spatie/laravel-permission`. Laravel handles transactional domain logic and webhooks. ([Laravel][4])
* **DB:** Postgres 16 (UUID PKs, integer cents for money, logical replication for read-scaling later), use `UPDATE ... WHERE stock_count >= n` + transactions pattern. ([PostgreSQL][2])
* **Payments:** Stripe Checkout or Payment Intents; implement webhook signature verification and idempotency. ([Stripe Documentation][5])
* **Hosting:** Next.js on edge (Vercel) + Laravel in managed container service (AWS Fargate / DigitalOcean App Platform) with Docker images; S3-compatible object storage for media.
* **Infra:** Redis for cache & queues; MinIO or S3 for assets; GitHub Actions for CI/CD.

---

## 2) Critical schema adjustments (improvements from earlier PAD)

**Inventory model (improved)**

```sql
-- inventory table: separate stock ledger + snapshots for audit
CREATE TABLE inventory (
  sku text PRIMARY KEY,
  stock_count int NOT NULL DEFAULT 0,
  reserved_count int NOT NULL DEFAULT 0, -- used for temporary reservation
  location text DEFAULT 'main',
  updated_at timestamptz DEFAULT now()
);

CREATE TABLE inventory_ledger (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  sku text NOT NULL,
  change int NOT NULL, -- +/-
  reason text, -- 'order_created','order_canceled','adjustment'
  reference_id uuid, -- order id or adjustment id
  created_at timestamptz DEFAULT now()
);
```

**Why:** ledger enables reconciliation and audit; `reserved_count` supports reservation windows for checkout holds.

**Orders & payments**

* Add `checkout_reserved_at` and `reservation_expires_at` to orders to manage temporary holds.
* Orders move from `draft` → `reserved` → `placed` → `paid` with idempotent webhook handling.

---

## 3) Checkout / Inventory algorithm (transactional pattern)

1. **Reserve phase (Quick, idempotent):**

   * API receives `reserve` request for cart items.
   * For each SKU: `UPDATE inventory SET reserved_count = reserved_count + N WHERE stock_count - reserved_count >= N RETURNING 1`
   * If any update fails, rollback / release partial reservations.
   * Create `order` in `reserved` state with reservation timestamps, add ledger entries (async).

2. **Checkout & payment:**

   * Create Stripe PaymentIntent / Checkout Session with an `order_id` metadata and return client-side redirect.
   * Use Stripe idempotency key for server-side requests. ([Stripe Documentation][6])

3. **Webhook (payment succeeded):**

   * Verify Stripe signature.
   * Use `event.id` idempotency check in DB; mark order `paid` and atomically decrement `stock_count` and reduce `reserved_count` inside a transaction (or use atomic `UPDATE ... WHERE` if preferred). Save ledger entries. ([Stripe Documentation][5])

4. **Reservation expiry:**

   * Background worker releases reservations (`reserved_count` decrement and ledger log) if `reservation_expires_at` reached.

**Why this approach**

* Keeps UI snappy (reserve quickly).
* Prevents oversell via DB constraints and atomic updates.
* Handles Stripe duplicates and webhook replay via idempotency checks. ([Stripe Documentation][6])

---

## 4) Improved API contract (concise)

* `POST /api/v1/cart/reserve` → returns `reservation_id`, `reservation_expires_at`.
* `POST /api/v1/checkout` with `reservation_id` → returns `stripe_checkout_url`.
* `POST /api/v1/webhooks/stripe` → handles events with signature verification and idempotency.

---

## 5) Security hardening (concrete checklist)

* Verify Stripe webhook signatures and implement idempotency storage. ([Stripe Documentation][5])
* CSP + secure headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options). Follow OWASP Header & CSP cheat sheets. ([OWASP Cheat Sheet Series][7])
* OWASP Top 10-driven secure defaults in CI (SAST dependency scans, dependency upgrades). ([OWASP Foundation][8])
* Rate limiting for login/checkout endpoints and webhook endpoints.

---

## 6) DevOps & deployment (concrete)

* **Dockerfiles:** multi-stage builds for Laravel and Next (production node build → static output / server) with `.dockerignore`.
* **CI (GitHub Actions):** lint → typecheck → unit tests → build images → push to registry → deploy.
* **Environments:** `dev`, `staging` (with test Stripe keys), `prod` (live Stripe keys). Use secrets manager for keys.
* **Backups:** nightly Postgres dumps to S3 with 30-day retention and point-in-time recovery configured.

---

## 7) Observability & QA

* Instrument critical metrics (checkout latency, reservation failure rate, queue length).
* Error reporting (Sentry) and trace logging.
* E2E tests (Cypress) for checkout and bookings; accessibility test (axe-core).
* Load test checkout path (k6) paying special attention to inventory update path.

---

## 8) Singapore-specific compliance (GST implementation)

* Business must show prices inclusive of GST (9% as of 1 Jan 2024). Ensure storefront displays GST-inclusive pricing and breakdown at checkout; invoice templates must contain business GST registration where applicable. Validate output against IRAS guidance and transitional rules. ([Default][9])

---

## 9) Risk register & mitigations (concise)

* **Oversell:** mitigation = reservation + atomic decrement + background reconciliation.
* **Payment webhook replay:** mitigation = event idempotency + signature verification. ([Stripe Documentation][5])
* **Third-party outages (Stripe):** mitigation = fallback offline order creation w/ reconciliation.
* **Regulatory (GST misdisplay):** mitigation = automated re-price scripts and a/b price snapshot for audit.

---

## 10) Validation gates (pre-implementation)

Before writing code, confirm:

* [ ] Payment provider & test/live keys available.
* [ ] GST rules validated (9% inclusive) and invoicing requirements confirmed. ([Default][9])
* [ ] Hosting decision: Vercel + managed containers or full container infra.
* [ ] Initial admin user list and seed data (products/variants).

---

# Part C — Implementation plan (phases, checklists, and deliverables)

Phases with concrete deliverables (useful for PRs):

**Phase 0 — Repo & infra skeleton**

* Monorepo: `/frontend` (Next.js) and `/backend` (Laravel).
* `docker-compose.dev.yml`, `Dockerfile` for backend and frontend.
* CI skeleton with lint/typecheck.

**Phase 1 — Backend core**

* Migrations for improved schema (inventory ledger, order states).
* Product API + seeders.
* Auth (Sanctum) and RBAC (spatie).
* Implement reservation endpoint + tests.

**Phase 2 — Payments & order flow**

* Stripe integration (PaymentIntent/Checkout) with idempotency keys; create webhook endpoint with signature verification and idempotent handling. ([Stripe Documentation][5])
* Orders lifecycle + worker to finalize inventory.

**Phase 3 — Frontend**

* Landing page replication from `cafe.html` (static via App Router SSG).
* BFF routes for cart/reserve/checkout flows (server actions or route handlers).
* Use shadcn UI wrappers for consistent accessible components.

**Phase 4 — Admin & events**

* Admin endpoints (product CRUD, inventory adj).
* Event booking system + calendar UI.

**Phase 5 — QA & hardening**

* E2E tests, load tests, accessibility audit.
* Observability, Sentry, monitoring.

**Phase 6 — Release**

* Production deploy and runbook.

---

# Part D — Five load-bearing facts (sources)

1. Next.js 15 extends App Router and introduces features aligned with React 19 and server components — useful when making Next.js the BFF/edge layer. ([Next.js][1])
2. Laravel 12 continues as the stable PHP backend option with updated dependency notes and starter kits — validates choice of Laravel 12 as backend. ([Laravel][4])
3. Postgres 16 contains performance and logical replication improvements that we can leverage for read-scaling and replication strategies. ([PostgreSQL][2])
4. Singapore GST: the rate moved to 9% with effect from 1 Jan 2024 — prices and invoicing must reflect GST-inclusive statements as required by IRAS. Implement price displays and invoice templates accordingly. ([Default][9])
5. Stripe webhook and idempotency practices: verify signatures and implement idempotency to avoid duplicate charges or duplicated order fulfillment. ([Stripe Documentation][5])

---

# Part E — Short, concrete next steps I will produce *if you want me to* (pick one — I’ll generate it immediately)

(Do not ask for confirmation; tell me which artifact you want next and I’ll output it in this reply.)

1. **Initial Laravel migrations + reservation/order schema SQL + Laravel model stubs** (includes tests for inventory atomic updates).
2. **Next.js landing page conversion from `cafe.html`** using Tailwind tokens + shadcn wrapper components (single file preview).
3. **Docker + CI skeleton**: `Dockerfile`s for frontend & backend, `docker-compose.dev.yml`, and a GitHub Actions workflow skeleton.

(You pick 1, 2, or 3. I’ll produce the code/artifact right away.)

---

# Final notes (short)

* I recommend the **BFF hybrid** path — it preserves developer velocity for an SMB while delivering top-tier storefront performance and a clean domain model for transactions and inventory. ([Next.js][1])
* I’ve biased for pragmatic, testable patterns (reservations + atomic DB updates + idempotent webhook handling) so you avoid the two most common failures on SMB e-commerce builds: oversell and duplicate payments. ([Stripe Documentation][5])

Which artifact should I generate *right now* (migrations, Next.js landing page, or Docker+CI skeleton)?

[1]: https://nextjs.org/blog/next-15?utm_source=chatgpt.com "Next.js 15"
[2]: https://www.postgresql.org/about/news/postgresql-16-released-2715/?utm_source=chatgpt.com "PostgreSQL 16 Released!"
[3]: https://nextjs.org/docs?utm_source=chatgpt.com "Next.js Docs | Next.js"
[4]: https://laravel.com/docs/12.x/releases?utm_source=chatgpt.com "Release Notes - Laravel 12.x - The PHP Framework For Web Artisans"
[5]: https://docs.stripe.com/webhooks?utm_source=chatgpt.com "Receive Stripe events in your webhook endpoint"
[6]: https://docs.stripe.com/api/idempotent_requests?utm_source=chatgpt.com "Idempotent requests | Stripe API Reference"
[7]: https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html?utm_source=chatgpt.com "Content Security Policy - OWASP Cheat Sheet Series"
[8]: https://owasp.org/www-project-top-ten/?utm_source=chatgpt.com "OWASP Top Ten Web Application Security Risks"
[9]: https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-rate-change/gst-rate-change-for-consumers1?utm_source=chatgpt.com "GST Rate Change for Consumers - Singapore - IRAS"
