

## Phase 1: Strategic Pivot — "The Morning Alchemy"

**Re-Analysis & Direction Shift**
Acknowledged. We are pivoting from "Monsoon Tropics" (Dark/Industrial) to **"The Morning Alchemy"** (Light/Organic).

*   **Psychological Shift:** Moving from "Cozy Shelter" to "Energizing Clarity."
*   **Visual Language:**
    *   **Palette:** Creamy Whites, Deep Espressos, and Golden Caramels (Aromatic/Cheerful).
    *   **Texture:** Paper-fiber noise to avoid the "sterile clinical" look of pure white.
    *   **Atmosphere:** Instead of rain, we will simulate **Aromatic Steam** rising using a new Canvas engine.
*   **UX refinement:** Lighter backgrounds demand sharper contrast for accessibility. We will use rich coffee browns for text rather than grey to ensure the "freshness" remains readable.

---

## Phase 2: Implementation

Here is the meticulously re-imagined solution. The architecture remains modular, but the styling and atmospheric engine have been completely rewritten to capture that "first sip of coffee" feeling.

```html
<!DOCTYPE html>
<html lang="en-SG">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CHANGI ROASTERS | Morning Alchemy</title>
    <meta name="description" content="Freshly roasted coffee in Singapore. Aromatic, cheerful, and crafted for the morning light.">

    <!-- Preconnect -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    
    <!-- Typography: 'Playfair Display' (Editorial) & 'Inter' (Clean/Modern) -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">

    <style>
        /* 
         * DESIGN SYSTEM: "MORNING ALCHEMY"
         * Palette: Cream, Espresso, Golden Caramel, Soft Sage
         */
        :root {
            /* Colors */
            --c-bg: #FAF9F6;          /* Creamy White (Porcelain) */
            --c-surface: #FFFFFF;     /* Pure White (Cards) */
            --c-text-main: #3E3228;   /* Deep Espresso (High Contrast) */
            --c-text-muted: #8C7B70;  /* Latte Brown */
            --c-accent: #D97706;      /* Golden Caramel (Cheerful CTAs) */
            --c-accent-hover: #B45309;
            --c-success: #059669;    /* Fresh Green */
            
            /* Gradients */
            --grad-glow: radial-gradient(circle at top right, rgba(217, 119, 6, 0.1), transparent 40%);

            /* Typography */
            --font-serif: 'Playfair Display', serif;
            --font-sans: 'Inter', sans-serif;
            
            /* Spacing */
            --space-xs: 0.5rem;
            --space-sm: 1rem;
            --space-md: 2rem;
            --space-lg: 4rem;
            --space-xl: 6rem;
            --container: 1280px;
            
            /* Shadows & Borders */
            --shadow-card: 0 10px 30px rgba(62, 50, 40, 0.06);
            --shadow-hover: 0 20px 40px rgba(62, 50, 40, 0.1);
            --radius-sm: 8px;
            --radius-md: 16px;
            --radius-full: 9999px;
        }

        /* RESET & BASE */
        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--c-bg);
            color: var(--c-text-main);
            font-family: var(--font-sans);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* TEXTURE: High Quality Paper */
        .texture-paper {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='paperFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paperFilter)' opacity='0.03'/%3E%3C/svg%3E");
            pointer-events: none;
            z-index: 9998;
            mix-blend-mode: multiply;
        }

        /* CANVAS: Steam Engine */
        #steam-canvas {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            z-index: -1;
            pointer-events: none;
        }

        /* UTILITIES */
        .container {
            max-width: var(--container);
            margin: 0 auto;
            padding: 0 var(--space-md);
            position: relative;
            z-index: 1;
        }

        /* BUTTONS */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: var(--c-accent);
            color: #fff;
            padding: 1rem 2rem;
            font-family: var(--font-sans);
            font-weight: 600;
            text-decoration: none;
            border: none;
            cursor: pointer;
            border-radius: var(--radius-full);
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-shadow: 0 4px 12px rgba(217, 119, 6, 0.3);
        }

        .btn:hover {
            background: var(--c-accent-hover);
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(217, 119, 6, 0.4);
        }

        .btn-outline {
            background: transparent;
            border: 2px solid var(--c-text-main);
            color: var(--c-text-main);
            box-shadow: none;
        }

        .btn-outline:hover {
            background: var(--c-text-main);
            color: #fff;
        }

        /* HEADER */
        header {
            position: fixed;
            top: 0; width: 100%;
            padding: var(--space-sm) 0;
            background: rgba(250, 249, 246, 0.85); /* Cream tint */
            backdrop-filter: blur(16px);
            z-index: 100;
            border-bottom: 1px solid rgba(62, 50, 40, 0.05);
            transition: padding 0.3s;
        }

        header.scrolled {
            padding: var(--space-xs) 0;
            box-shadow: 0 4px 20px rgba(62, 50, 40, 0.04);
        }

        .nav-inner {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-family: var(--font-serif);
            font-weight: 700;
            font-size: 1.5rem;
            color: var(--c-text-main);
            text-decoration: none;
            letter-spacing: -0.02em;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .logo svg {
            fill: var(--c-accent);
            width: 24px;
            height: 24px;
        }

        .nav-links {
            display: flex;
            gap: var(--space-md);
        }

        .nav-links a {
            color: var(--c-text-muted);
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 500;
            transition: color 0.2s;
        }

        .nav-links a:hover {
            color: var(--c-accent);
        }

        .cart-trigger {
            position: relative;
            padding: 8px;
            border-radius: 50%;
            transition: background 0.2s;
        }
        
        .cart-trigger:hover { background: rgba(0,0,0,0.04); }

        .cart-count {
            position: absolute;
            top: 0; right: 0;
            background: var(--c-text-main);
            color: #fff;
            font-size: 0.65rem;
            width: 18px; height: 18px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transform: scale(0);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .cart-count.visible {
            opacity: 1;
            transform: scale(1);
        }

        /* HERO SECTION */
        .hero {
            min-height: 90vh;
            display: flex;
            align-items: center;
            padding-top: 80px;
            position: relative;
            overflow: hidden;
        }

        /* Subtle background glow */
        .hero::before {
            content: '';
            position: absolute;
            top: -20%; right: -10%;
            width: 600px; height: 600px;
            background: var(--grad-glow);
            border-radius: 50%;
            z-index: -1;
            filter: blur(80px);
        }

        .hero-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--space-lg);
            align-items: center;
        }

        .hero-content h1 {
            font-family: var(--font-serif);
            font-size: clamp(3rem, 5vw, 4.5rem);
            line-height: 1.1;
            color: var(--c-text-main);
            margin-bottom: var(--space-md);
        }

        .hero-content p {
            font-size: 1.2rem;
            color: var(--c-text-muted);
            margin-bottom: var(--space-lg);
            max-width: 90%;
        }

        .hero-image-wrapper {
            position: relative;
        }

        .hero-img {
            width: 100%;
            height: auto;
            border-radius: var(--radius-md);
            /* Organic shape mask via border-radius */
            border-radius: 200px 200px 20px 20px;
            box-shadow: var(--shadow-hover);
            transform: rotate(-2deg);
            transition: transform 0.5s ease;
        }

        .hero-image-wrapper:hover .hero-img {
            transform: rotate(0deg) scale(1.02);
        }

        /* PRODUCTS SECTION */
        .products {
            padding: var(--space-xl) 0;
        }

        .section-head {
            text-align: center;
            margin-bottom: var(--space-lg);
        }

        .section-head h2 {
            font-family: var(--font-serif);
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .section-head p {
            color: var(--c-accent);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-size: 0.85rem;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: var(--space-md);
        }

        .card {
            background: var(--c-surface);
            border-radius: var(--radius-md);
            overflow: hidden;
            box-shadow: var(--shadow-card);
            transition: all 0.3s ease;
            position: relative;
            border: 1px solid rgba(62, 50, 40, 0.04);
        }

        .card:hover {
            transform: translateY(-8px);
            box-shadow: var(--shadow-hover);
        }

        .card-img-box {
            height: 300px;
            overflow: hidden;
            position: relative;
        }

        .card-img-box img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }

        .card:hover .card-img-box img {
            transform: scale(1.08);
        }

        .card-body {
            padding: var(--space-md);
        }

        .card-title {
            font-family: var(--font-serif);
            font-size: 1.5rem;
            margin-bottom: 0.25rem;
        }

        .card-price {
            color: var(--c-accent);
            font-weight: 700;
            font-size: 1.1rem;
            margin-bottom: var(--space-sm);
            display: block;
        }

        .tags {
            display: flex;
            gap: 8px;
            margin-bottom: var(--space-md);
            flex-wrap: wrap;
        }

        .tag {
            font-size: 0.75rem;
            background: #F3F4F6;
            color: var(--c-text-muted);
            padding: 4px 10px;
            border-radius: 4px;
        }

        .add-btn {
            width: 100%;
            padding: 12px;
            background: var(--c-text-main);
            color: #fff;
            border: none;
            border-radius: var(--radius-sm);
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .add-btn:hover {
            background: var(--c-accent);
        }

        /* ABOUT SECTION */
        .about {
            background: var(--c-surface);
            padding: var(--space-xl) 0;
            margin: var(--space-xl) 0;
            border-top: 1px solid rgba(62, 50, 40, 0.05);
            border-bottom: 1px solid rgba(62, 50, 40, 0.05);
        }

        .about-layout {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--space-xl);
            align-items: center;
        }

        .about-text h2 {
            font-family: var(--font-serif);
            font-size: 2.5rem;
            margin-bottom: var(--space-md);
            line-height: 1.2;
        }

        .stat-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--space-md);
            margin-top: var(--space-md);
        }

        .stat-card {
            padding: var(--space-sm);
            background: var(--c-bg);
            border-radius: var(--radius-sm);
            text-align: center;
        }

        .stat-num {
            font-family: var(--font-serif);
            font-size: 2rem;
            color: var(--c-accent);
            display: block;
        }

        .stat-label {
            font-size: 0.8rem;
            color: var(--c-text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        /* TOAST */
        .toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(20px);
            background: var(--c-text-main);
            color: #fff;
            padding: 12px 24px;
            border-radius: var(--radius-full);
            font-size: 0.9rem;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            z-index: 9999;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .toast.active {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }

        .toast svg { fill: var(--c-accent); width: 18px; height: 18px; }

        /* Footer */
        footer {
            text-align: center;
            padding: var(--space-lg) 0;
            color: var(--c-text-muted);
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .hero-grid, .about-layout { grid-template-columns: 1fr; }
            .hero { text-align: center; padding-top: 100px; }
            .hero-content h1 { font-size: 2.5rem; }
            .nav-links { display: none; } /* Simplified mobile nav for demo */
        }
    </style>
</head>
<body>

    <!-- Atmospheric Layers -->
    <div class="texture-paper"></div>
    <canvas id="steam-canvas"></canvas>

    <!-- Header -->
    <header id="header">
        <div class="container nav-inner">
            <a href="#" class="logo">
                <!-- Simple SVG Coffee Bean Icon -->
                <svg viewBox="0 0 24 24">
                    <path d="M12,22c4.97,0,9-4.03,9-9c0-4.97-9-13-9-13S3,8.03,3,13C3,17.97,7.03,22,12,22z M12,20c-3.87,0-7-3.13-7-7 c0-2.5,3.5-6.88,5.5-9.17C11.39,6.3,12,7.6,12,7.6s0.61-1.3,1.5-2.77C15.5,7.12,19,11.5,19,13C19,16.87,15.87,20,12,20z"/>
                    <path d="M12,6c-1.5,2-4,5.5-4,7c0,2.21,1.79,4,4,4s4-1.79,4-4C16,11.5,13.5,8,12,6z M12,15c-1.1,0-2-0.9-2-2 c0-0.72,1.12-2.51,2-4c0.88,1.49,2,3.28,2,4C14,14.1,13.1,15,12,15z" opacity="0.3"/>
                </svg>
                CHANGI ROASTERS
            </a>
            <nav class="nav-links">
                <a href="#brews">Brews</a>
                <a href="#story">Story</a>
                <a href="#visit">Visit Us</a>
            </nav>
            <div class="cart-trigger" onclick="alert('Cart view would open here')">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="9" cy="21" r="1"></circle>
                    <circle cx="20" cy="21" r="1"></circle>
                    <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
                </svg>
                <div id="cart-badge" class="cart-count">0</div>
            </div>
        </div>
    </header>

    <main>
        <!-- Hero Section -->
        <section class="hero">
            <div class="container hero-grid">
                <div class="hero-content">
                    <span style="color: var(--c-accent); font-weight: 600; letter-spacing: 1px; text-transform: uppercase; font-size: 0.8rem; display: block; margin-bottom: 1rem;">Fresh Roasted Daily</span>
                    <h1>Wake Up to <br><span style="font-style: italic; color: var(--c-accent);">Sunlight</span> & Aroma.</h1>
                    <p>Experience the cheerful warmth of a perfect morning brew. Single-origin beans, roasted with precision to unlock their brightest, most vibrant notes.</p>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <a href="#brews" class="btn">Shop Our Brews</a>
                        <a href="#story" class="btn btn-outline">Our Story</a>
                    </div>
                </div>
                <div class="hero-image-wrapper">
                    <!-- Bright, warm imagery -->
                    <img src="https://images.unsplash.com/photo-1497935586351-b67a49e012bf?q=80&w=2073&auto=format&fit=crop" alt="Fresh coffee pour in sunlight" class="hero-img">
                </div>
            </div>
        </section>

        <!-- Product Showcase -->
        <section id="brews" class="products">
            <div class="container">
                <div class="section-head">
                    <p>Seasonal Selection</p>
                    <h2>The Morning Collection</h2>
                </div>
                
                <div class="grid">
                    <!-- Card 1 -->
                    <div class="card">
                        <div class="card-img-box">
                            <img src="https://images.unsplash.com/photo-1559056199-641a0ac8b55e?q=80&w=1974&auto=format&fit=crop" alt="Ethiopian Yirgacheffe">
                        </div>
                        <div class="card-body">
                            <h3 class="card-title">Ethiopian Sunrise</h3>
                            <span class="card-price">$24.00</span>
                            <div class="tags">
                                <span class="tag">Floral</span>
                                <span class="tag">Citrus</span>
                                <span class="tag">Light</span>
                            </div>
                            <button class="add-btn" onclick="addToCart('Ethiopian Sunrise')">
                                Add to Cart
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                            </button>
                        </div>
                    </div>

                    <!-- Card 2 -->
                    <div class="card">
                        <div class="card-img-box">
                            <img src="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?q=80&w=1974&auto=format&fit=crop" alt="Colombia Supremo">
                        </div>
                        <div class="card-body">
                            <h3 class="card-title">Colombia Gold</h3>
                            <span class="card-price">$22.00</span>
                            <div class="tags">
                                <span class="tag">Caramel</span>
                                <span class="tag">Nutty</span>
                                <span class="tag">Medium</span>
                            </div>
                            <button class="add-btn" onclick="addToCart('Colombia Gold')">
                                Add to Cart
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                            </button>
                        </div>
                    </div>

                    <!-- Card 3 -->
                    <div class="card">
                        <div class="card-img-box">
                            <img src="https://images.unsplash.com/photo-1584225064785-c62a8b43d148?q=80&w=1980&auto=format&fit=crop" alt="House Blend">
                        </div>
                        <div class="card-body">
                            <h3 class="card-title">Changi House Blend</h3>
                            <span class="card-price">$20.00</span>
                            <div class="tags">
                                <span class="tag">Chocolate</span>
                                <span class="tag">Smooth</span>
                                <span class="tag">Dark</span>
                            </div>
                            <button class="add-btn" onclick="addToCart('Changi House Blend')">
                                Add to Cart
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section id="story" class="about">
            <div class="container about-layout">
                <div class="about-img-wrapper">
                    <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?q=80&w=2069&auto=format&fit=crop" style="width:100%; border-radius: 16px; box-shadow: var(--shadow-card);" alt="Cafe Interior">
                </div>
                <div class="about-text">
                    <span style="color: var(--c-accent); font-weight: 700; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px;">Our Philosophy</span>
                    <h2>Crafting Joy, <br>One Cup at a Time.</h2>
                    <p style="color: var(--c-text-muted); margin-bottom: 1.5rem;">
                        We believe coffee is more than caffeine—it's a moment of pause, a burst of energy, and a ritual of comfort. Our roastery in the heart of Singapore is bathed in natural light, reflecting the bright, cheerful profiles we aim for in every roast.
                    </p>
                    <div class="stat-grid">
                        <div class="stat-card">
                            <span class="stat-num">100%</span>
                            <span class="stat-label">Arabica Beans</span>
                        </div>
                        <div class="stat-card">
                            <span class="stat-num">24h</span>
                            <span class="stat-label">Fresh Roast</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2024 Changi Roasters. Brewed with Sunshine.</p>
        </div>
    </footer>

    <!-- Toast Element -->
    <div id="toast" class="toast">
        <svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
        <span id="toast-message">Added to cart</span>
    </div>

    <script>
        /**
         * STEAM ENGINE
         * Generates rising steam particles to simulate aromatic fresh coffee.
         * Uses Canvas API for performance.
         */
        const initSteam = () => {
            const canvas = document.getElementById('steam-canvas');
            const ctx = canvas.getContext('2d');
            
            let width, height;
            const particles = [];

            const resize = () => {
                width = canvas.width = window.innerWidth;
                height = canvas.height = window.innerHeight;
            };

            window.addEventListener('resize', resize);
            resize();

            class SteamParticle {
                constructor() {
                    this.reset(true);
                }

                reset(initial = false) {
                    this.x = Math.random() * width;
                    this.y = initial ? Math.random() * height : height + Math.random() * 100;
                    this.size = Math.random() * 40 + 20;
                    this.speedY = Math.random() * 1 + 0.5;
                    this.opacity = 0; // Fade in initially
                    this.fadeState = 'in'; // in, hold, out
                    this.life = Math.random() * 200 + 100;
                    this.wobble = Math.random() * Math.PI * 2;
                    this.wobbleSpeed = Math.random() * 0.02 + 0.01;
                }

                update() {
                    this.y -= this.speedY;
                    this.wobble += this.wobbleSpeed;
                    this.x += Math.sin(this.wobble) * 0.5;

                    // Opacity lifecycle
                    if (this.fadeState === 'in') {
                        this.opacity += 0.005;
                        if (this.opacity >= 0.15) this.fadeState = 'hold';
                    } else {
                        this.life--;
                        if (this.life <= 0) {
                            this.opacity -= 0.01;
                            if (this.opacity <= 0) this.reset();
                        }
                    }
                }

                draw() {
                    ctx.beginPath();
                    // Create a soft radial gradient for the puff
                    const gradient = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, this.size);
                    gradient.addColorStop(0, `rgba(255, 255, 255, ${this.opacity})`);
                    gradient.addColorStop(1, `rgba(255, 255, 255, 0)`);
                    
                    ctx.fillStyle = gradient;
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fill();
                }
            }

            // Initialize particles
            for(let i = 0; i < 50; i++) {
                particles.push(new SteamParticle());
            }

            const animate = () => {
                ctx.clearRect(0, 0, width, height);
                particles.forEach(p => {
                    p.update();
                    p.draw();
                });
                requestAnimationFrame(animate);
            };

            animate();
        };

        /**
         * UI INTERACTION LOGIC
         */
        const state = {
            cart: 0
        };

        function addToCart(productName) {
            state.cart++;
            
            // Update Badge
            const badge = document.getElementById('cart-badge');
            badge.textContent = state.cart;
            badge.classList.add('visible');
            
            // Trigger toast animation
            const toast = document.getElementById('toast');
            const msg = document.getElementById('toast-message');
            msg.textContent = `Added ${productName} to cart`;
            toast.classList.add('active');

            // Hide toast after delay
            setTimeout(() => {
                toast.classList.remove('active');
            }, 3000);
        }

        // Header Scroll Effect
        window.addEventListener('scroll', () => {
            const header = document.getElementById('header');
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            initSteam();
        });

    </script>
</body>
</html>
```

https://chat.z.ai/s/0ad5ebc2-2474-4b41-a70e-50970261d0ef
