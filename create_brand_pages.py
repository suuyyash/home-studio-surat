import os
import re

DIR = '/Users/sidsmac/Documents/Home Studio'

with open(os.path.join(DIR, 'about.html'), 'r') as f:
    base_template = f.read()

# We need to extract the header and footer.
# header_end corresponds to the end of the mobile drawer.
mobile_drawer_end_str = '<div class="mobile-overlay"></div>'
mobile_drawer_end_idx = base_template.find(mobile_drawer_end_str) + len(mobile_drawer_end_str)
header_html = base_template[:mobile_drawer_end_idx]

# footer_start corresponds to <!-- Detailed Footer -->
footer_start_idx = base_template.find('<!-- Detailed Footer -->')
footer_html = base_template[footer_start_idx:]

# Custom CSS for Brand Pages
brand_css = """
  <style>
    /* Premium Brand Page Components */
    .brand-hero {
      position: relative;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      background-color: var(--bg-primary);
      color: #fff;
      padding-top: var(--header-height);
      overflow: hidden;
    }
    
    .brand-hero-video {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.6;
      z-index: 1;
    }
    
    .brand-hero-content {
      position: relative;
      z-index: 10;
      max-width: 800px;
      padding: 0 2rem;
    }
    
    .brand-hero-logo {
      max-width: 300px;
      max-height: 120px;
      margin-bottom: 2rem;
      object-fit: contain;
    }
    
    .brand-intro-section {
      background-color: var(--bg-secondary);
      border-top: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }
    
    .brand-split {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4rem;
      align-items: center;
    }
    
    .brand-split-img {
      width: 100%;
      border-radius: var(--radius-lg);
      box-shadow: 0 20px 40px rgba(0,0,0,0.4);
      object-fit: cover;
      aspect-ratio: 4/5;
    }
    
    .brand-gallery-section {
      background-color: var(--bg-primary);
    }
    
    .brand-gallery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
      gap: 2rem;
    }
    
    .brand-gallery-item {
      position: relative;
      overflow: hidden;
      border-radius: var(--radius-md);
      aspect-ratio: 1;
      background: var(--bg-tertiary);
    }
    
    .brand-gallery-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }
    
    .brand-gallery-item:hover .brand-gallery-img {
      transform: scale(1.05);
    }
    
    @media (max-width: 900px) {
      .brand-split { grid-template-columns: 1fr; gap: 2rem; }
    }
  </style>
</head>
"""

# Replace </head> with brand_css
header_html = header_html.replace('</head>', brand_css)

# Generate AXOR Page
axor_title_replace = r'<title>.*?</title>'
axor_header = re.sub(axor_title_replace, '<title>AXOR | Home Studio Surat</title>', header_html)

axor_content = """
  <!-- Hero Section -->
  <section class="brand-hero">
    <video class="brand-hero-video" autoplay muted loop playsinline>
      <source src="BRAND/AXOR/AXOR ShowerHeaven 1200.mp4" type="video/mp4">
    </video>
    <div class="brand-hero-content reveal">
      <img src="BRAND/AXOR/logo.png" alt="AXOR Logo" class="brand-hero-logo">
      <h1 style="font-size: 2.5rem; text-shadow: 0 4px 20px rgba(0,0,0,0.8); margin-bottom: 1.5rem;">Form Follows Perfection</h1>
      <p style="font-size: 1.2rem; text-shadow: 0 2px 8px rgba(0,0,0,0.8); font-weight: 300;">Discover avant-garde design and extraordinary water experiences engineered in Germany.</p>
    </div>
  </section>

  <!-- Split Screen Intro -->
  <section class="section-padding brand-intro-section">
    <div class="container">
      <div class="brand-split">
        <div class="reveal">
          <img src="BRAND/AXOR/axor shower heaven.jpg" alt="AXOR Shower Heaven" class="brand-split-img">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">The Collection</span>
          <h2 class="section-title">AXOR ShowerHeaven</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8;">
            A magnificent stage for water. The AXOR ShowerHeaven offers an unparalleled shower experience. With its generously proportioned, flat aesthetic, it is a masterpiece of precision engineering and striking visual presence.
          </p>
          <p style="margin-bottom: 2.5rem; font-weight: 300; line-height: 1.8;">
            Designed for those who view the bathroom as a sanctuary, AXOR collaborates with the world's most renowned designers—including Philippe Starck, Antonio Citterio, and Jean-Marie Massaud—to create objects that redefine the very nature of luxury living.
          </p>
          <a href="contact.html" class="btn-primary magnetic-btn">Enquire Now</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Gallery -->
  <section class="section-padding brand-gallery-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <span class="section-tag">Signature Pieces</span>
        <h2 class="section-title">The AXOR Portfolio</h2>
      </div>
      <div class="brand-gallery-grid">
        <div class="brand-gallery-item reveal">
          <img src="BRAND/AXOR/axor_archivio.jpg" alt="AXOR Archivio" class="brand-gallery-img">
        </div>
        <div class="brand-gallery-item reveal reveal-delay-1">
          <img src="BRAND/AXOR/axor_showerselect id.jpg" alt="AXOR ShowerSelect ID" class="brand-gallery-img">
        </div>
        <div class="brand-gallery-item reveal">
          <img src="BRAND/AXOR/axor-axorstarckv.jpg" alt="AXOR Starck V" class="brand-gallery-img">
        </div>
        <div class="brand-gallery-item reveal reveal-delay-1">
          <img src="BRAND/AXOR/axor-massaud.jpg" alt="AXOR Massaud" class="brand-gallery-img">
        </div>
      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-axor.html'), 'w') as f:
    f.write(axor_header + axor_content + footer_html)


# Generate BLANCO Page
blanco_header = re.sub(axor_title_replace, '<title>BLANCO | Home Studio Surat</title>', header_html)

blanco_content = """
  <!-- Hero Section -->
  <section class="brand-hero" style="background: linear-gradient(135deg, #111, #222);">
    <div class="brand-hero-content reveal">
      <img src="BRAND/BLANCO/blanco.svg" alt="BLANCO Logo" class="brand-hero-logo" style="filter: brightness(0) invert(1);">
      <h1 style="font-size: 2.5rem; text-shadow: 0 4px 20px rgba(0,0,0,0.8); margin-bottom: 1.5rem;">The Kitchen Water Hub</h1>
      <p style="font-size: 1.2rem; text-shadow: 0 2px 8px rgba(0,0,0,0.8); font-weight: 300;">Seamless workflow and impeccable design with premium sinks and mixer taps.</p>
    </div>
  </section>

  <!-- Split Screen Intro -->
  <section class="section-padding brand-intro-section">
    <div class="container">
      <div class="brand-split">
        <div class="reveal">
          <img src="BRAND/BLANCO/quatrus-usupersingle.jpg" alt="BLANCO Quatrus" class="brand-split-img">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">German Engineering</span>
          <h2 class="section-title">Uncompromising Quality</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8;">
            BLANCO has been synonymous with premium kitchen water hubs for over 90 years. We offer beautifully integrated sink and faucet systems that transform the functional center of your kitchen into a statement of pure luxury.
          </p>
          <p style="margin-bottom: 2.5rem; font-weight: 300; line-height: 1.8;">
            Constructed from SILGRANIT® or premium stainless steel, BLANCO products guarantee incredible durability, heat resistance, and an effortlessly elegant aesthetic. Our curated collection offers the ultimate in hygiene and ease of maintenance.
          </p>
          <a href="contact.html" class="btn-primary magnetic-btn">Enquire Now</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Gallery -->
  <section class="section-padding brand-gallery-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <span class="section-tag">Signature Pieces</span>
        <h2 class="section-title">The BLANCO Portfolio</h2>
      </div>
      <div class="brand-gallery-grid" style="grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));">
        <div class="brand-gallery-item reveal">
          <img src="BRAND/BLANCO/hafele_kitchen_sinks.webp" alt="BLANCO Kitchen Sink" class="brand-gallery-img">
        </div>
        <div class="brand-gallery-item reveal reveal-delay-1">
          <img src="BRAND/BLANCO/quatrus-usupersingle.jpg" alt="BLANCO Quatrus Sink" class="brand-gallery-img">
        </div>
      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-blanco.html'), 'w') as f:
    f.write(blanco_header + blanco_content + footer_html)

print("Generated brand-axor.html and brand-blanco.html")
