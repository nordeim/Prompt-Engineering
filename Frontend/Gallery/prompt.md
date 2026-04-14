Design a photographer galleryblog, for Photography and .

Visual Strategy:
Imagery: Photography work, , Composition, color.
Photography: showcase, .
Composition: , work.

Color Palette:
Primary Colors: pure white, dark gray, black.
Accent Colors: multicolor(the artworks themselves).
Background: pure white or pure black.

Typography:
Headings: elegant serif, convey artistic elegance.
Body Text: small font size, comfortable line spacing.
work use .

Page Structure:
Hero Section: Photographybio+.
work categories: ///.
Artwork Details: + parameters+storiesBackground.
functions: Topic Categories.
Contact Information: booking+ link.

Overall Vibe: , visual, elegant, professional.

---

Below is a reference design for your deep review and consideration for a complete photographer gallery & blog website — elegant, visual, and fully functional with category filtering, lightbox viewing, artwork details, and booking contact.

```html
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Elara Voss — Photography</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            serif: ['"Playfair Display"', 'serif'],
            sans: ['"Inter"', 'sans-serif'],
          }
        }
      }
    }
  </script>
  <style>
    ::selection { background-color: #000; color: #fff; }
    .hide-scrollbar::-webkit-scrollbar { display: none; }
    .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
    
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(30px); }
      to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
    @keyframes slideUp {
      from { opacity: 0; transform: translateY(60px); }
      to { opacity: 1; transform: translateY(0); }
    }
    @keyframes scaleIn {
      from { opacity: 0; transform: scale(0.9); }
      to { opacity: 1; transform: scale(1); }
    }
    .animate-fade-up { animation: fadeUp 0.8s ease-out forwards; }
    .animate-fade-in { animation: fadeIn 0.6s ease-out forwards; }
    .animate-slide-up { animation: slideUp 0.7s ease-out forwards; }
    .animate-scale-in { animation: scaleIn 0.5s ease-out forwards; }
    
    .delay-100 { animation-delay: 0.1s; }
    .delay-200 { animation-delay: 0.2s; }
    .delay-300 { animation-delay: 0.3s; }
    .delay-400 { animation-delay: 0.4s; }
    .delay-500 { animation-delay: 0.5s; }
    .delay-600 { animation-delay: 0.6s; }
    
    .gallery-item { opacity: 0; }
    .gallery-item.visible { animation: fadeUp 0.7s ease-out forwards; }
    
    .lightbox-open { overflow: hidden; }
    
    .img-reveal {
      transition: transform 700ms cubic-bezier(0.4, 0, 0.2, 1), filter 500ms ease;
    }
    .img-reveal:hover {
      transform: scale(1.05);
    }
    
    .masonry-grid {
      columns: 1;
      column-gap: 1rem;
    }
    @media (min-width: 768px) {
      .masonry-grid { columns: 2; }
    }
    @media (min-width: 1024px) {
      .masonry-grid { columns: 3; }
    }
    .masonry-grid .gallery-item {
      break-inside: avoid;
      margin-bottom: 1rem;
    }
    
    .nav-blend { mix-blend-mode: difference; }
    
    .text-stroke {
      -webkit-text-stroke: 1px rgba(255,255,255,0.3);
      color: transparent;
    }
    
    input:focus, textarea:focus {
      outline: none;
      border-color: #000;
    }
    
    .toast {
      position: fixed;
      bottom: 2rem;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #000;
      color: #fff;
      padding: 12px 24px;
      border-radius: 0;
      font-family: 'Inter', sans-serif;
      font-size: 14px;
      z-index: 9999;
      transition: transform 0.4s ease;
    }
    .toast.show {
      transform: translateX(-50%) translateY(0);
    }
  </style>
</head>

<body class="bg-white text-black font-sans antialiased">

  <!-- Toast -->
  <div id="toast" class="toast">Message sent successfully</div>

  <!-- Navigation -->
  <nav id="navbar" class="fixed top-0 left-0 right-0 z-50 transition-all duration-500">
    <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
      <a href="#hero" class="font-serif text-xl tracking-tight text-white nav-blend">Elara Voss</a>
      
      <!-- Desktop Nav -->
      <div class="hidden md:flex items-center gap-8">
        <a href="#work" class="text-[11px] font-semibold uppercase tracking-[0.2em] text-white/70 hover:text-white nav-blend transition-colors duration-300">Work</a>
        <a href="#about" class="text-[11px] font-semibold uppercase tracking-[0.2em] text-white/70 hover:text-white nav-blend transition-colors duration-300">About</a>
        <a href="#stories" class="text-[11px] font-semibold uppercase tracking-[0.2em] text-white/70 hover:text-white nav-blend transition-colors duration-300">Stories</a>
        <a href="#contact" class="text-[11px] font-semibold uppercase tracking-[0.2em] text-white/70 hover:text-white nav-blend transition-colors duration-300">Contact</a>
      </div>
      
      <!-- Mobile Menu Button -->
      <button id="menuBtn" class="md:hidden text-white nav-blend" onclick="toggleMenu()">
        <iconify-icon icon="lucide:menu" width="22"></iconify-icon>
      </button>
    </div>
    
    <!-- Mobile Menu -->
    <div id="mobileMenu" class="hidden md:hidden bg-black/95 backdrop-blur-md">
      <div class="px-6 py-8 flex flex-col gap-6">
        <a href="#work" onclick="toggleMenu()" class="text-[11px] font-semibold uppercase tracking-[0.2em] text-white/70 hover:text-white transition-colors">Work</a>
        <a href="#about" onclick="toggleMenu()" class="text-[11px] font-semibold uppercase tracking-[0.2em] text-white/70 hover:text-white transition-colors">About</a>
        <a href="#stories" onclick="toggleMenu()" class="text-[11px] font-semibold uppercase tracking-[0.2em] text-white/70 hover:text-white transition-colors">Stories</a>
        <a href="#contact" onclick="toggleMenu()" class="text-[11px] font-semibold uppercase tracking-[0.2em] text-white/70 hover:text-white transition-colors">Contact</a>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <section id="hero" class="relative h-screen overflow-hidden bg-black">
    <div class="absolute inset-0">
      <img src="https://picsum.photos/seed/hero-photo-studio/1920/1080.jpg" alt="Hero" class="w-full h-full object-cover opacity-60 animate-fade-in">
      <div class="absolute inset-0 bg-gradient-to-t from-black via-black/30 to-transparent"></div>
    </div>
    
    <div class="relative z-10 h-full flex flex-col justify-end pb-20 px-6 md:px-12 max-w-7xl mx-auto">
      <div class="animate-fade-up" style="opacity:0; animation-delay: 0.3s;">
        <p class="text-[11px] font-semibold uppercase tracking-[0.25em] text-white/50 mb-4">Photographer & Visual Storyteller</p>
      </div>
      <h1 class="font-serif text-5xl md:text-7xl lg:text-[6.5rem] font-normal text-white leading-[0.95] tracking-tight animate-fade-up" style="opacity:0; animation-delay: 0.5s;">
        Capturing<br>
        <em class="text-white/80">Light</em> &<br>
        Emotion
      </h1>
      <div class="mt-8 flex items-center gap-6 animate-fade-up" style="opacity:0; animation-delay: 0.7s;">
        <a href="#work" class="inline-flex items-center gap-2 bg-white text-black px-6 py-3 text-[11px] font-semibold uppercase tracking-[0.15em] hover:bg-white/90 transition-colors duration-300">
          View Work
          <iconify-icon icon="lucide:arrow-down" width="14"></iconify-icon>
        </a>
        <a href="#about" class="inline-flex items-center gap-2 border border-white/20 text-white px-6 py-3 text-[11px] font-semibold uppercase tracking-[0.15em] hover:bg-white/10 transition-colors duration-300">
          About Me
        </a>
      </div>
      
      <!-- Scroll indicator -->
      <div class="absolute bottom-8 right-6 md:right-12 animate-fade-up" style="opacity:0; animation-delay: 1s;">
        <div class="flex flex-col items-center gap-2">
          <span class="text-[9px] uppercase tracking-[0.2em] text-white/30" style="writing-mode: vertical-rl;">Scroll</span>
          <div class="w-px h-12 bg-white/20 relative overflow-hidden">
            <div class="w-full h-1/2 bg-white/60 animate-bounce"></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Category Stats Bar -->
  <section class="border-b border-black/10">
    <div class="max-w-7xl mx-auto px-6 md:px-12">
      <div class="grid grid-cols-2 md:grid-cols-4 divide-x divide-black/10">
        <div class="py-8 px-4 text-center">
          <p class="font-serif text-3xl md:text-4xl tracking-tight">247</p>
          <p class="text-[11px] uppercase tracking-[0.15em] text-black/40 mt-1">Portraits</p>
        </div>
        <div class="py-8 px-4 text-center">
          <p class="font-serif text-3xl md:text-4xl tracking-tight">189</p>
          <p class="text-[11px] uppercase tracking-[0.15em] text-black/40 mt-1">Landscapes</p>
        </div>
        <div class="py-8 px-4 text-center">
          <p class="font-serif text-3xl md:text-4xl tracking-tight">312</p>
          <p class="text-[11px] uppercase tracking-[0.15em] text-black/40 mt-1">Street</p>
        </div>
        <div class="py-8 px-4 text-center">
          <p class="font-serif text-3xl md:text-4xl tracking-tight">98</p>
          <p class="text-[11px] uppercase tracking-[0.15em] text-black/40 mt-1">Editorial</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Work / Gallery Section -->
  <section id="work" class="py-20 md:py-32">
    <div class="max-w-7xl mx-auto px-6 md:px-12">
      <!-- Section Header -->
      <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-6 mb-12">
        <div>
          <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-black/40 mb-3">Portfolio</p>
          <h2 class="font-serif text-4xl md:text-5xl tracking-tight">Selected Work</h2>
        </div>
        
        <!-- Category Filters -->
        <div class="flex flex-wrap gap-2" id="filters">
          <button onclick="filterGallery('all')" class="filter-btn active px-4 py-2 text-[11px] font-semibold uppercase tracking-[0.15em] border border-black/20 hover:bg-black hover:text-white transition-all duration-300" data-filter="all">All</button>
          <button onclick="filterGallery('portrait')" class="filter-btn px-4 py-2 text-[11px] font-semibold uppercase tracking-[0.15em] border border-black/20 hover:bg-black hover:text-white transition-all duration-300" data-filter="portrait">Portrait</button>
          <button onclick="filterGallery('landscape')" class="filter-btn px-4 py-2 text-[11px] font-semibold uppercase tracking-[0.15em] border border-black/20 hover:bg-black hover:text-white transition-all duration-300" data-filter="landscape">Landscape</button>
          <button onclick="filterGallery('street')" class="filter-btn px-4 py-2 text-[11px] font-semibold uppercase tracking-[0.15em] border border-black/20 hover:bg-black hover:text-white transition-all duration-300" data-filter="street">Street</button>
          <button onclick="filterGallery('editorial')" class="filter-btn px-4 py-2 text-[11px] font-semibold uppercase tracking-[0.15em] border border-black/20 hover:bg-black hover:text-white transition-all duration-300" data-filter="editorial">Editorial</button>
        </div>
      </div>
      
      <!-- Masonry Gallery Grid -->
      <div id="gallery" class="masonry-grid">
        
        <!-- Item 1 -->
        <div class="gallery-item visible" data-category="portrait" onclick="openLightbox(0)">
          <div class="relative group overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/seed/portrait-woman-bw/600/800.jpg" alt="Portrait Study" class="w-full img-reveal">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors duration-500 flex items-end">
              <div class="p-6 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-500">
                <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/60">Portrait</p>
                <h3 class="font-serif text-lg text-white mt-1">Silent Dialogues</h3>
                <p class="text-xs text-white/50 mt-1">f/1.8 · 85mm · ISO 200</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Item 2 -->
        <div class="gallery-item visible" data-category="landscape" onclick="openLightbox(1)">
          <div class="relative group overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/seed/mountain-dawn-mist/600/400.jpg" alt="Mountain Dawn" class="w-full img-reveal">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors duration-500 flex items-end">
              <div class="p-6 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-500">
                <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/60">Landscape</p>
                <h3 class="font-serif text-lg text-white mt-1">Dawn Over Aethelgard</h3>
                <p class="text-xs text-white/50 mt-1">f/11 · 24mm · ISO 100</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Item 3 -->
        <div class="gallery-item visible" data-category="street" onclick="openLightbox(2)">
          <div class="relative group overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/seed/street-tokyo-rain/600/750.jpg" alt="Tokyo Rain" class="w-full img-reveal">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors duration-500 flex items-end">
              <div class="p-6 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-500">
                <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/60">Street</p>
                <h3 class="font-serif text-lg text-white mt-1">Rainy Season, Shibuya</h3>
                <p class="text-xs text-white/50 mt-1">f/2.8 · 35mm · ISO 800</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Item 4 -->
        <div class="gallery-item visible" data-category="editorial" onclick="openLightbox(3)">
          <div class="relative group overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/seed/editorial-fashion-dark/600/900.jpg" alt="Editorial Fashion" class="w-full img-reveal">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors duration-500 flex items-end">
              <div class="p-6 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-500">
                <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/60">Editorial</p>
                <h3 class="font-serif text-lg text-white mt-1">Vogue Noir</h3>
                <p class="text-xs text-white/50 mt-1">f/4 · 70mm · ISO 160</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Item 5 -->
        <div class="gallery-item visible" data-category="portrait" onclick="openLightbox(4)">
          <div class="relative group overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/seed/portrait-natural-light/600/700.jpg" alt="Natural Light Portrait" class="w-full img-reveal">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors duration-500 flex items-end">
              <div class="p-6 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-500">
                <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/60">Portrait</p>
                <h3 class="font-serif text-lg text-white mt-1">Golden Hour</h3>
                <p class="text-xs text-white/50 mt-1">f/2 · 50mm · ISO 100</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Item 6 -->
        <div class="gallery-item visible" data-category="landscape" onclick="openLightbox(5)">
          <div class="relative group overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/seed/ocean-cliff-sunset/600/450.jpg" alt="Ocean Cliffs" class="w-full img-reveal">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors duration-500 flex items-end">
              <div class="p-6 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-500">
                <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/60">Landscape</p>
                <h3 class="font-serif text-lg text-white mt-1">Edge of the World</h3>
                <p class="text-xs text-white/50 mt-1">f/8 · 16mm · ISO 200</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Item 7 -->
        <div class="gallery-item visible" data-category="street" onclick="openLightbox(6)">
          <div class="relative group overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/seed/street-market-color/600/600.jpg" alt="Street Market" class="w-full img-reveal">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors duration-500 flex items-end">
              <div class="p-6 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-500">
                <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/60">Street</p>
                <h3 class="font-serif text-lg text-white mt-1">Spice Market, Marrakech</h3>
                <p class="text-xs text-white/50 mt-1">f/4 · 50mm · ISO 400</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Item 8 -->
        <div class="gallery-item visible" data-category="editorial" onclick="openLightbox(7)">
          <div class="relative group overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/seed/editorial-minimalist/600/850.jpg" alt="Minimalist Editorial" class="w-full img-reveal">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors duration-500 flex items-end">
              <div class="p-6 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-500">
                <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/60">Editorial</p>
                <h3 class="font-serif text-lg text-white mt-1">Less Is More</h3>
                <p class="text-xs text-white/50 mt-1">f/5.6 · 85mm · ISO 100</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Item 9 -->
        <div class="gallery-item visible" data-category="portrait" onclick="openLightbox(8)">
          <div class="relative group overflow-hidden cursor-pointer">
            <img src="https://picsum.photos/seed/portrait-shadow-art/600/750.jpg" alt="Shadow Portrait" class="w-full img-reveal">
            <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors duration-500 flex items-end">
              <div class="p-6 translate-y-4 group-hover:translate-y-0 opacity-0 group-hover:opacity-100 transition-all duration-500">
                <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/60">Portrait</p>
                <h3 class="font-serif text-lg text-white mt-1">Chiaroscuro</h3>
                <p class="text-xs text-white/50 mt-1">f/2.8 · 135mm · ISO 320</p>
              </div>
            </div>
          </div>
        </div>
        
      </div>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="bg-black text-white py-20 md:py-32">
    <div class="max-w-7xl mx-auto px-6 md:px-12">
      <div class="grid md:grid-cols-2 gap-12 md:gap-20 items-center">
        <!-- Image -->
        <div class="relative">
          <div class="overflow-hidden">
            <img src="https://picsum.photos/seed/photographer-self-portrait/700/900.jpg" alt="Elara Voss" class="w-full h-[500px] md:h-[650px] object-cover grayscale hover:grayscale-0 transition-all duration-700">
          </div>
          <div class="absolute -bottom-4 -right-4 md:-bottom-6 md:-right-6 border border-white/10 p-4 md:p-6 bg-black">
            <p class="font-serif text-3xl md:text-4xl">12+</p>
            <p class="text-[10px] uppercase tracking-[0.15em] text-white/40 mt-1">Years of Craft</p>
          </div>
        </div>
        
        <!-- Bio Text -->
        <div>
          <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-white/40 mb-4">About</p>
          <h2 class="font-serif text-4xl md:text-5xl tracking-tight mb-8">The Eye<br>Behind the Lens</h2>
          <div class="space-y-5 text-sm font-light leading-relaxed text-white/60">
            <p>I'm Elara Voss — a photographer based between Berlin and Tokyo. My work explores the intersection of light, identity, and the quiet moments that exist between breaths.</p>
            <p>Having studied under master photographers in Florence and spent years documenting life across six continents, I've developed a style that blends documentary authenticity with fine-art composition.</p>
            <p>Every frame I capture tells a story. Not the obvious one — but the one beneath the surface. The glance you almost missed. The light that won't return. The emotion that words can't carry.</p>
          </div>
          
          <!-- Tools -->
          <div class="mt-10 pt-8 border-t border-white/10">
            <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/30 mb-4">Primary Tools</p>
            <div class="flex flex-wrap gap-3">
              <span class="px-3 py-1.5 border border-white/10 text-[11px] text-white/50">Hasselblad X2D</span>
              <span class="px-3 py-1.5 border border-white/10 text-[11px] text-white/50">Leica M11</span>
              <span class="px-3 py-1.5 border border-white/10 text-[11px] text-white/50">Sony A7R V</span>
              <span class="px-3 py-1.5 border border-white/10 text-[11px] text-white/50">Capture One</span>
              <span class="px-3 py-1.5 border border-white/10 text-[11px] text-white/50">Natural Light</span>
            </div>
          </div>
          
          <!-- Awards -->
          <div class="mt-8 pt-8 border-t border-white/10">
            <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/30 mb-4">Recognition</p>
            <div class="space-y-3">
              <div class="flex justify-between items-center">
                <span class="text-sm text-white/60">IPA Photographer of the Year</span>
                <span class="text-[11px] text-white/30">2024</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-sm text-white/60">Sony World Photography Awards</span>
                <span class="text-[11px] text-white/30">2023</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-sm text-white/60">Magnum Foundation Fellow</span>
                <span class="text-[11px] text-white/30">2022</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Stories / Blog Section -->
  <section id="stories" class="py-20 md:py-32 border-b border-black/10">
    <div class="max-w-7xl mx-auto px-6 md:px-12">
      <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-6 mb-14">
        <div>
          <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-black/40 mb-3">Blog</p>
          <h2 class="font-serif text-4xl md:text-5xl tracking-tight">Stories & Insights</h2>
        </div>
        <a href="#" class="text-[11px] font-semibold uppercase tracking-[0.15em] text-black/50 hover:text-black transition-colors flex items-center gap-2">
          All Articles
          <iconify-icon icon="lucide:arrow-right" width="14"></iconify-icon>
        </a>
      </div>
      
      <div class="grid md:grid-cols-3 gap-8">
        <!-- Story 1 -->
        <article class="group cursor-pointer">
          <div class="overflow-hidden mb-5">
            <img src="https://picsum.photos/seed/blog-chasing-light/600/400.jpg" alt="Chasing Light" class="w-full aspect-[4/3] object-cover img-reveal">
          </div>
          <div class="flex items-center gap-3 mb-3">
            <span class="text-[10px] font-semibold uppercase tracking-[0.15em] text-black/40">Behind the Shot</span>
            <span class="text-black/20">·</span>
            <span class="text-[10px] text-black/30">Dec 14, 2024</span>
          </div>
          <h3 class="font-serif text-xl tracking-tight mb-2 group-hover:text-black/60 transition-colors">Chasing Light in the Atlas Mountains</h3>
          <p class="text-sm font-light leading-relaxed text-black/50">How a 4AM hike led to the most extraordinary golden hour I've ever witnessed — and the single frame that changed my perspective.</p>
        </article>
        
        <!-- Story 2 -->
        <article class="group cursor-pointer">
          <div class="overflow-hidden mb-5">
            <img src="https://picsum.photos/seed/blog-portrait-psychology/600/400.jpg" alt="Portrait Psychology" class="w-full aspect-[4/3] object-cover img-reveal">
          </div>
          <div class="flex items-center gap-3 mb-3">
            <span class="text-[10px] font-semibold uppercase tracking-[0.15em] text-black/40">Technique</span>
            <span class="text-black/20">·</span>
            <span class="text-[10px] text-black/30">Nov 28, 2024</span>
          </div>
          <h3 class="font-serif text-xl tracking-tight mb-2 group-hover:text-black/60 transition-colors">The Psychology of Portraiture</h3>
          <p class="text-sm font-light leading-relaxed text-black/50">Understanding the silent conversation between photographer and subject — techniques to capture genuine emotion beyond the pose.</p>
        </article>
        
        <!-- Story 3 -->
        <article class="group cursor-pointer">
          <div class="overflow-hidden mb-5">
            <img src="https://picsum.photos/seed/blog-street-philosophy/600/400.jpg" alt="Street Philosophy" class="w-full aspect-[4/3] object-cover img-reveal">
          </div>
          <div class="flex items-center gap-3 mb-3">
            <span class="text-[10px] font-semibold uppercase tracking-[0.15em] text-black/40">Essay</span>
            <span class="text-black/20">·</span>
            <span class="text-[10px] text-black/30">Oct 15, 2024</span>
          </div>
          <h3 class="font-serif text-xl tracking-tight mb-2 group-hover:text-black/60 transition-colors">What Street Photography Taught Me</h3>
          <p class="text-sm font-light leading-relaxed text-black/50">Ten years of wandering cities with a camera has taught me more about humanity than any classroom ever could.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- Featured Artwork Detail -->
  <section class="py-20 md:py-32 bg-stone-50">
    <div class="max-w-7xl mx-auto px-6 md:px-12">
      <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-black/40 mb-3">Featured Piece</p>
      <h2 class="font-serif text-4xl md:text-5xl tracking-tight mb-14">Artwork in Detail</h2>
      
      <div class="grid md:grid-cols-2 gap-12 items-start">
        <div class="overflow-hidden">
          <img src="https://picsum.photos/seed/featured-artwork-detail/800/1000.jpg" alt="Featured Artwork" class="w-full object-cover hover:scale-105 transition-transform duration-700">
        </div>
        
        <div>
          <h3 class="font-serif text-3xl tracking-tight mb-2">The Last Fisherman</h3>
          <p class="text-sm text-black/40 mb-8">Setúbal, Portugal — November 2024</p>
          
          <div class="grid grid-cols-2 gap-6 mb-10">
            <div class="border-t border-black/10 pt-4">
              <p class="text-[10px] font-semibold uppercase tracking-[0.15em] text-black/30 mb-1">Camera</p>
              <p class="text-sm">Leica M11</p>
            </div>
            <div class="border-t border-black/10 pt-4">
              <p class="text-[10px] font-semibold uppercase tracking-[0.15em] text-black/30 mb-1">Lens</p>
              <p class="text-sm">Summilux 35mm f/1.4</p>
            </div>
            <div class="border-t border-black/10 pt-4">
              <p class="text-[10px] font-semibold uppercase tracking-[0.15em] text-black/30 mb-1">Settings</p>
              <p class="text-sm">f/2.8 · 1/250s · ISO 400</p>
            </div>
            <div class="border-t border-black/10 pt-4">
              <p class="text-[10px] font-semibold uppercase tracking-[0.15em] text-black/30 mb-1">Film Simulation</p>
              <p class="text-sm">Custom BW + Grain</p>
            </div>
          </div>
          
          <div class="space-y-4 text-sm font-light leading-relaxed text-black/60 border-t border-black/10 pt-8">
            <p>I met João on the docks of Setúbal at 5 in the morning. He was 72 years old and had been fishing these waters since he was fourteen. His hands told stories his lips never would.</p>
            <p>This was the last frame on my roll. The sun had just broken through the morning haze, casting a single beam of light across his weathered face. He looked up at that exact moment — not at me, but at something far beyond the horizon.</p>
            <p>He told me later that his father used to say: <em>"The sea gives and the sea takes, but it never stops moving."</em> João retired the following week. This photograph is my tribute to a lifetime on the water.</p>
          </div>
          
          <div class="mt-8 flex gap-3">
            <button class="px-6 py-3 bg-black text-white text-[11px] font-semibold uppercase tracking-[0.15em] hover:bg-black/80 transition-colors flex items-center gap-2">
              <iconify-icon icon="lucide:maximize-2" width="14"></iconify-icon>
              Full Resolution
            </button>
            <button class="px-6 py-3 border border-black/20 text-[11px] font-semibold uppercase tracking-[0.15em] hover:bg-black hover:text-white transition-all flex items-center gap-2">
              <iconify-icon icon="lucide:share-2" width="14"></iconify-icon>
              Share
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Services -->
  <section class="py-20 md:py-32">
    <div class="max-w-7xl mx-auto px-6 md:px-12">
      <div class="text-center mb-14">
        <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-black/40 mb-3">Services</p>
        <h2 class="font-serif text-4xl md:text-5xl tracking-tight">How We Can Work Together</h2>
      </div>
      
      <div class="grid md:grid-cols-4 gap-px bg-black/10">
        <div class="bg-white p-8 group hover:bg-black hover:text-white transition-colors duration-500 cursor-pointer">
          <iconify-icon icon="lucide:user" width="28" class="text-black/40 group-hover:text-white/60 transition-colors mb-6 block"></iconify-icon>
          <h3 class="font-serif text-xl tracking-tight mb-3">Portrait Sessions</h3>
          <p class="text-sm font-light leading-relaxed text-black/50 group-hover:text-white/50 transition-colors">Intimate portrait sessions in studio or on location. Natural light or strobe — tailored to your vision.</p>
          <p class="mt-6 text-sm font-medium">From €800</p>
        </div>
        
        <div class="bg-white p-8 group hover:bg-black hover:text-white transition-colors duration-500 cursor-pointer">
          <iconify-icon icon="lucide:book-open" width="28" class="text-black/40 group-hover:text-white/60 transition-colors mb-6 block"></iconify-icon>
          <h3 class="font-serif text-xl tracking-tight mb-3">Editorial</h3>
          <p class="text-sm font-light leading-relaxed text-black/50 group-hover:text-white/50 transition-colors">Fashion, lifestyle, and brand editorials for magazines, campaigns, and commercial storytelling.</p>
          <p class="mt-6 text-sm font-medium">From €2,500</p>
        </div>
        
        <div class="bg-white p-8 group hover:bg-black hover:text-white transition-colors duration-500 cursor-pointer">
          <iconify-icon icon="lucide:building-2" width="28" class="text-black/40 group-hover:text-white/60 transition-colors mb-6 block"></iconify-icon>
          <h3 class="font-serif text-xl tracking-tight mb-3">Brand Identity</h3>
          <p class="text-sm font-light leading-relaxed text-black/50 group-hover:text-white/50 transition-colors">Complete visual identity packages — from brand photography to art direction and visual language systems.</p>
          <p class="mt-6 text-sm font-medium">From €5,000</p>
        </div>
        
        <div class="bg-white p-8 group hover:bg-black hover:text-white transition-colors duration-500 cursor-pointer">
          <iconify-icon icon="lucide:calendar" width="28" class="text-black/40 group-hover:text-white/60 transition-colors mb-6 block"></iconify-icon>
          <h3 class="font-serif text-xl tracking-tight mb-3">Workshops</h3>
          <p class="text-sm font-light leading-relaxed text-black/50 group-hover:text-white/50 transition-colors">One-on-one mentoring and group workshops on portraiture, street photography, and visual storytelling.</p>
          <p class="mt-6 text-sm font-medium">From €400</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Testimonial -->
  <section class="py-20 md:py-28 bg-black text-white overflow-hidden">
    <div class="max-w-4xl mx-auto px-6 text-center">
      <iconify-icon icon="lucide:quote" width="40" class="text-white/20 mb-8 block mx-auto"></iconify-icon>
      <blockquote class="font-serif text-2xl md:text-4xl leading-snug tracking-tight mb-8">
        "Elara doesn't take photographs — she captures the invisible threads that connect us to the world. Working with her was a revelation."
      </blockquote>
      <div>
        <p class="text-sm font-medium">Isabelle Moreau</p>
        <p class="text-xs text-white/40 mt-1">Creative Director, Maison Lumière</p>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="py-20 md:py-32">
    <div class="max-w-7xl mx-auto px-6 md:px-12">
      <div class="grid md:grid-cols-2 gap-16">
        <!-- Contact Info -->
        <div>
          <p class="text-[11px] font-semibold uppercase tracking-[0.2em] text-black/40 mb-3">Get in Touch</p>
          <h2 class="font-serif text-4xl md:text-5xl tracking-tight mb-8">Let's Create<br>Something Beautiful</h2>
          <p class="text-sm font-light leading-relaxed text-black/50 mb-10">Whether you have a project in mind, want to book a session, or simply want to connect — I'd love to hear from you.</p>
          
          <div class="space-y-6">
            <div class="flex items-center gap-4">
              <div class="w-10 h-10 border border-black/10 flex items-center justify-center">
                <iconify-icon icon="lucide:mail" width="16" class="text-black/40"></iconify-icon>
              </div>
              <div>
                <p class="text-[10px] uppercase tracking-[0.15em] text-black/30">Email</p>
                <p class="text-sm">hello@elaravoss.com</p>
              </div>
            </div>
            
            <div class="flex items-center gap-4">
              <div class="w-10 h-10 border border-black/10 flex items-center justify-center">
                <iconify-icon icon="lucide:map-pin" width="16" class="text-black/40"></iconify-icon>
              </div>
              <div>
                <p class="text-[10px] uppercase tracking-[0.15em] text-black/30">Based In</p>
                <p class="text-sm">Berlin, DE · Tokyo, JP</p>
              </div>
            </div>
            
            <div class="flex items-center gap-4">
              <div class="w-10 h-10 border border-black/10 flex items-center justify-center">
                <iconify-icon icon="lucide:clock" width="16" class="text-black/40"></iconify-icon>
              </div>
              <div>
                <p class="text-[10px] uppercase tracking-[0.15em] text-black/30">Response Time</p>
                <p class="text-sm">Within 24 hours</p>
              </div>
            </div>
          </div>
          
          <!-- Social Links -->
          <div class="mt-10 pt-8 border-t border-black/10">
            <p class="text-[10px] uppercase tracking-[0.15em] text-black/30 mb-4">Follow Along</p>
            <div class="flex gap-4">
              <a href="#" class="w-10 h-10 border border-black/10 flex items-center justify-center hover:bg-black hover:text-white transition-all duration-300">
                <iconify-icon icon="lucide:instagram" width="16"></iconify-icon>
              </a>
              <a href="#" class="w-10 h-10 border border-black/10 flex items-center justify-center hover:bg-black hover:text-white transition-all duration-300">
                <iconify-icon icon="lucide:twitter" width="16"></iconify-icon>
              </a>
              <a href="#" class="w-10 h-10 border border-black/10 flex items-center justify-center hover:bg-black hover:text-white transition-all duration-300">
                <iconify-icon icon="lucide:youtube" width="16"></iconify-icon>
              </a>
              <a href="#" class="w-10 h-10 border border-black/10 flex items-center justify-center hover:bg-black hover:text-white transition-all duration-300">
                <iconify-icon icon="lucide:facebook" width="16"></iconify-icon>
              </a>
            </div>
          </div>
        </div>
        
        <!-- Contact Form -->
        <div>
          <form id="contactForm" onsubmit="handleSubmit(event)" class="space-y-6">
            <div class="grid grid-cols-2 gap-6">
              <div>
                <label class="text-[10px] uppercase tracking-[0.15em] text-black/30 mb-2 block">First Name</label>
                <input type="text" required class="w-full border-b border-black/10 py-3 text-sm bg-transparent transition-colors duration-300 placeholder:text-black/20" placeholder="Elara">
              </div>
              <div>
                <label class="text-[10px] uppercase tracking-[0.15em] text-black/30 mb-2 block">Last Name</label>
                <input type="text" required class="w-full border-b border-black/10 py-3 text-sm bg-transparent transition-colors duration-300 placeholder:text-black/20" placeholder="Voss">
              </div>
            </div>
            
            <div>
              <label class="text-[10px] uppercase tracking-[0.15em] text-black/30 mb-2 block">Email</label>
              <input type="email" required class="w-full border-b border-black/10 py-3 text-sm bg-transparent transition-colors duration-300 placeholder:text-black/20" placeholder="hello@example.com">
            </div>
            
            <div>
              <label class="text-[10px] uppercase tracking-[0.15em] text-black/30 mb-2 block">Project Type</label>
              <select class="w-full border-b border-black/10 py-3 text-sm bg-transparent text-black/60 cursor-pointer">
                <option>Portrait Session</option>
                <option>Editorial / Fashion</option>
                <option>Brand Identity</option>
                <option>Workshop / Mentoring</option>
                <option>Print Purchase</option>
                <option>Other</option>
              </select>
            </div>
            
            <div>
              <label class="text-[10px] uppercase tracking-[0.15em] text-black/30 mb-2 block">Budget Range</label>
              <select class="w-full border-b border-black/10 py-3 text-sm bg-transparent text-black/60 cursor-pointer">
                <option>€500 – €1,000</option>
                <option>€1,000 – €3,000</option>
                <option>€3,000 – €5,000</option>
                <option>€5,000+</option>
                <option>Let's discuss</option>
              </select>
            </div>
            
            <div>
              <label class="text-[10px] uppercase tracking-[0.15em] text-black/30 mb-2 block">Tell Me About Your Vision</label>
              <textarea rows="4" class="w-full border-b border-black/10 py-3 text-sm bg-transparent transition-colors duration-300 resize-none placeholder:text-black/20" placeholder="Share your ideas, timeline, and any references..."></textarea>
            </div>
            
            <button type="submit" class="w-full bg-black text-white py-4 text-[11px] font-semibold uppercase tracking-[0.15em] hover:bg-black/80 transition-colors duration-300 flex items-center justify-center gap-2">
              Send Inquiry
              <iconify-icon icon="lucide:arrow-right" width="14"></iconify-icon>
            </button>
            
            <p class="text-[11px] text-black/30 text-center">Typically respond within 24 hours</p>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-black text-white py-16">
    <div class="max-w-7xl mx-auto px-6 md:px-12">
      <div class="grid md:grid-cols-4 gap-10 mb-14">
        <div class="md:col-span-2">
          <p class="font-serif text-2xl mb-4">Elara Voss</p>
          <p class="text-sm font-light leading-relaxed text-white/40 max-w-sm">Photographer & visual storyteller. Capturing light, emotion, and the quiet moments that define us.</p>
        </div>
        <div>
          <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/30 mb-4">Navigation</p>
          <div class="space-y-2">
            <a href="#work" class="block text-sm text-white/50 hover:text-white transition-colors">Work</a>
            <a href="#about" class="block text-sm text-white/50 hover:text-white transition-colors">About</a>
            <a href="#stories" class="block text-sm text-white/50 hover:text-white transition-colors">Stories</a>
            <a href="#contact" class="block text-sm text-white/50 hover:text-white transition-colors">Contact</a>
          </div>
        </div>
        <div>
          <p class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/30 mb-4">Connect</p>
          <div class="space-y-2">
            <a href="#" class="block text-sm text-white/50 hover:text-white transition-colors">Instagram</a>
            <a href="#" class="block text-sm text-white/50 hover:text-white transition-colors">Twitter / X</a>
            <a href="#" class="block text-sm text-white/50 hover:text-white transition-colors">YouTube</a>
            <a href="#" class="block text-sm text-white/50 hover:text-white transition-colors">Behance</a>
          </div>
        </div>
      </div>
      
      <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="text-[11px] text-white/30">&copy; 2024 Elara Voss. All rights reserved.</p>
        <div class="flex gap-6">
          <a href="#" class="text-[11px] text-white/30 hover:text-white/60 transition-colors">Privacy</a>
          <a href="#" class="text-[11px] text-white/30 hover:text-white/60 transition-colors">Terms</a>
          <a href="#" class="text-[11px] text-white/30 hover:text-white/60 transition-colors">Colophon</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Lightbox Modal -->
  <div id="lightbox" class="fixed inset-0 z-[60] bg-black/95 backdrop-blur-md hidden items-center justify-center" onclick="closeLightboxOutside(event)">
    <button onclick="closeLightbox()" class="absolute top-6 right-6 text-white/50 hover:text-white transition-colors z-10">
      <iconify-icon icon="lucide:x" width="28"></iconify-icon>
    </button>
    
    <button onclick="prevImage()" class="absolute left-4 md:left-8 top-1/2 -translate-y-1/2 w-12 h-12 border border-white/10 flex items-center justify-center text-white/50 hover:text-white hover:border-white/30 transition-all z-10">
      <iconify-icon icon="lucide:chevron-left" width="24"></iconify-icon>
    </button>
    
    <button onclick="nextImage()" class="absolute right-4 md:right-8 top-1/2 -translate-y-1/2 w-12 h-12 border border-white/10 flex items-center justify-center text-white/50 hover:text-white hover:border-white/30 transition-all z-10">
      <iconify-icon icon="lucide:chevron-right" width="24"></iconify-icon>
    </button>
    
    <div class="max-w-5xl w-full mx-4 flex flex-col md:flex-row items-center gap-8">
      <div class="flex-1 overflow-hidden">
        <img id="lightboxImg" src="" alt="" class="w-full max-h-[70vh] object-contain animate-scale-in">
      </div>
      <div class="md:w-72 text-white flex-shrink-0">
        <p id="lightboxCategory" class="text-[10px] font-semibold uppercase tracking-[0.2em] text-white/40 mb-2"></p>
        <h3 id="lightboxTitle" class="font-serif text-2xl tracking-tight mb-4"></h3>
        <div class="space-y-3 border-t border-white/10 pt-4">
          <div class="flex justify-between">
            <span class="text-[10px] uppercase tracking-[0.15em] text-white/30">Aperture</span>
            <span id="lightboxAperture" class="text-sm text-white/60"></span>
          </div>
          <div class="flex justify-between">
            <span class="text-[10px] uppercase tracking-[0.15em] text-white/30">Focal Length</span>
            <span id="lightboxFocal" class="text-sm text-white/60"></span>
          </div>
          <div class="flex justify-between">
            <span class="text-[10px] uppercase tracking-[0.15em] text-white/30">ISO</span>
            <span id="lightboxISO" class="text-sm text-white/60"></span>
          </div>
        </div>
        <p id="lightboxStory" class="text-xs font-light leading-relaxed text-white/40 mt-4"></p>
      </div>
    </div>
  </div>

  <script>
    // Gallery Data
    const galleryData = [
      { src: 'https://picsum.photos/seed/portrait-woman-bw/1200/1600.jpg', category: 'portrait', title: 'Silent Dialogues', aperture: 'f/1.8', focal: '85mm', iso: '200', story: 'A study in stillness — capturing the unspoken connection between subject and self.' },
      { src: 'https://picsum.photos/seed/mountain-dawn-mist/1200/800.jpg', category: 'landscape', title: 'Dawn Over Aethelgard', aperture: 'f/11', focal: '24mm', iso: '100', story: 'The mountains revealed themselves for exactly 47 seconds before the clouds swallowed them again.' },
      { src: 'https://picsum.photos/seed/street-tokyo-rain/1200/1500.jpg', category: 'street', title: 'Rainy Season, Shibuya', aperture: 'f/2.8', focal: '35mm', iso: '800', story: 'The neon reflections on wet asphalt turned an ordinary crossing into a cathedral of light.' },
      { src: 'https://picsum.photos/seed/editorial-fashion-dark/1200/1800.jpg', category: 'editorial', title: 'Vogue Noir', aperture: 'f/4', focal: '70mm', iso: '160', story: 'Darkness as a design element — every shadow intentionally placed to sculpt the narrative.' },
      { src: 'https://picsum.photos/seed/portrait-natural-light/1200/1400.jpg', category: 'portrait', title: 'Golden Hour', aperture: 'f/2', focal: '50mm', iso: '100', story: 'Thirty minutes before sunset, the world softens. This is when magic happens.' },
      { src: 'https://picsum.photos/seed/ocean-cliff-sunset/1200/900.jpg', category: 'landscape', title: 'Edge of the World', aperture: 'f/8', focal: '16mm', iso: '200', story: 'Standing at the cliff edge, where the land ends and the infinite begins.' },
      { src: 'https://picsum.photos/seed/street-market-color/1200/1200.jpg', category: 'street', title: 'Spice Market, Marrakech', aperture: 'f/4', focal: '50mm', iso: '400', story: 'Color so intense you can taste it. The market is a symphony for all senses.' },
      { src: 'https://picsum.photos/seed/editorial-minimalist/1200/1700.jpg', category: 'editorial', title: 'Less Is More', aperture: 'f/5.6', focal: '85mm', iso: '100', story: 'Stripping away everything until only the essential remains. The hardest kind of creation.' },
      { src: 'https://picsum.photos/seed/portrait-shadow-art/1200/1500.jpg', category: 'portrait', title: 'Chiaroscuro', aperture: 'f/2.8', focal: '135mm', iso: '320', story: 'Inspired by Caravaggio — using a single light source to reveal and conceal in equal measure.' },
    ];
    
    let currentImageIndex = 0;
    
    // Gallery Filter
    function filterGallery(category) {
      const items = document.querySelectorAll('.gallery-item');
      const buttons = document.querySelectorAll('.filter-btn');
      
      buttons.forEach(btn => {
        btn.classList.remove('bg-black', 'text-white');
        if (btn.dataset.filter === category) {
          btn.classList.add('bg-black', 'text-white');
        }
      });
      
      items.forEach((item, i) => {
        const cat = item.dataset.category;
        if (category === 'all' || cat === category) {
          item.style.display = '';
          item.style.opacity = '0';
          setTimeout(() => {
            item.classList.add('visible');
            item.style.opacity = '1';
          }, i * 80);
        } else {
          item.style.display = 'none';
          item.classList.remove('visible');
        }
      });
    }
    
    // Init active filter
    document.querySelector('.filter-btn[data-filter="all"]').classList.add('bg-black', 'text-white');
    
    // Lightbox
    function openLightbox(index) {
      currentImageIndex = index;
      updateLightbox();
      const lb = document.getElementById('lightbox');
      lb.classList.remove('hidden');
      lb.classList.add('flex');
      document.body.classList.add('lightbox-open');
    }
    
    function closeLightbox() {
      const lb = document.getElementById('lightbox');
      lb.classList.add('hidden');
      lb.classList.remove('flex');
      document.body.classList.remove('lightbox-open');
    }
    
    function closeLightboxOutside(e) {
      if (e.target === document.getElementById('lightbox')) {
        closeLightbox();
      }
    }
    
    function updateLightbox() {
      const data = galleryData[currentImageIndex];
      document.getElementById('lightboxImg').src = data.src;
      document.getElementById('lightboxCategory').textContent = data.category;
      document.getElementById('lightboxTitle').textContent = data.title;
      document.getElementById('lightboxAperture').textContent = data.aperture;
      document.getElementById('lightboxFocal').textContent = data.focal;
      document.getElementById('lightboxISO').textContent = data.iso;
      document.getElementById('lightboxStory').textContent = data.story;
    }
    
    function nextImage() {
      currentImageIndex = (currentImageIndex + 1) % galleryData.length;
      updateLightbox();
    }
    
    function prevImage() {
      currentImageIndex = (currentImageIndex - 1 + galleryData.length) % galleryData.length;
      updateLightbox();
    }
    
    // Keyboard nav
    document.addEventListener('keydown', (e) => {
      if (document.getElementById('lightbox').classList.contains('hidden')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowRight') nextImage();
      if (e.key === 'ArrowLeft') prevImage();
    });
    
    // Mobile Menu
    function toggleMenu() {
      const menu = document.getElementById('mobileMenu');
      menu.classList.toggle('hidden');
    }
    
    // Form Submit
    function handleSubmit(e) {
      e.preventDefault();
      showToast('Thank you! Your inquiry has been sent successfully.');
      e.target.reset();
    }
    
    // Toast
    function showToast(message) {
      const toast = document.getElementById('toast');
      toast.textContent = message;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 3000);
    }
    
    // Navbar background on scroll
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
      const navbar = document.getElementById('navbar');
      const scrollY = window.scrollY;
      
      if (scrollY > 100) {
        navbar.style.background = 'rgba(255,255,255,0.95)';
        navbar.style.backdropFilter = 'blur(12px)';
        navbar.style.borderBottom = '1px solid rgba(0,0,0,0.05)';
        navbar.querySelectorAll('a, button').forEach(el => {
          el.style.mixBlendMode = 'normal';
          el.classList.remove('text-white');
          if (el.tagName === 'A' && !el.classList.contains('font-serif')) {
            el.style.color = 'rgba(0,0,0,0.5)';
          } else if (el.classList.contains('font-serif')) {
            el.style.color = '#000';
          }
        });
      } else {
        navbar.style.background = 'transparent';
        navbar.style.backdropFilter = 'none';
        navbar.style.borderBottom = 'none';
        navbar.querySelectorAll('a, button').forEach(el => {
          el.style.mixBlendMode = '';
          el.style.color = '';
        });
      }
    });
    
    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('.gallery-item').forEach(item => {
      observer.observe(item);
    });
  </script>

</body>
</html>
```

Here's what this photographer gallery/blog includes:

**Sections:**
- **Hero** — Full-screen dramatic introduction with bio tagline and dual CTAs, scroll indicator
- **Stats Bar** — Count display for each photography category (Portrait, Landscape, Street, Editorial)
- **Gallery** — Masonry grid with **working category filters** (All / Portrait / Landscape / Street / Editorial), hover reveals with EXIF data overlays
- **Lightbox** — Full image viewer with keyboard navigation (← → Esc), EXIF parameters, and story text
- **About** — Split layout with grayscale→color image hover, bio text, tools, and awards
- **Stories/Blog** — 3-column article grid with category tags and dates
- **Featured Artwork** — Detailed breakdown with camera settings, film simulation, and the story behind the shot
- **Services** — 4-column pricing grid with hover color inversion
- **Testimonial** — Centered quote with attribution
- **Contact** — Full booking form with project type/budget selectors + social links
- **Footer** — Navigation, social, and legal links

**Interactive features:**
- Gallery category filtering with smooth animations
- Lightbox with previous/next navigation and keyboard support
- Navbar transitions from transparent (hero) to white on scroll
- Toast notification on form submission
- Mobile responsive hamburger menu
- Scroll-triggered fade-up animations
