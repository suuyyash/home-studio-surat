import os
import re

DIR = '/Users/sidsmac/Documents/Home Studio'

with open(os.path.join(DIR, 'about.html'), 'r') as f:
    base_template = f.read()

# Extract header and footer
mobile_drawer_end_str = '<div class="mobile-overlay"></div>'
mobile_drawer_end_idx = base_template.find(mobile_drawer_end_str) + len(mobile_drawer_end_str)
header_html = base_template[:mobile_drawer_end_idx]

footer_start_idx = base_template.find('<!-- Detailed Footer -->')
footer_html = base_template[footer_start_idx:]

# Custom CSS for Brand Pages
brand_css = """
  <style>
    /* Product Focused Brand Pages */
    .brand-header-minimal {
      padding-top: calc(var(--header-height) + 4rem);
      padding-bottom: 2rem;
      text-align: center;
      background-color: var(--bg-primary);
    }
    
    .brand-logo-large {
      max-width: 350px;
      max-height: 120px;
      margin: 0 auto 1.5rem;
      display: block;
      object-fit: contain;
    }
    
    .brand-main-feature {
      background-color: var(--bg-primary);
      padding-bottom: 5rem;
    }
    
    .main-feature-media {
      width: 100%;
      border-radius: var(--radius-lg);
      box-shadow: 0 20px 50px rgba(0,0,0,0.5);
      overflow: hidden;
      aspect-ratio: 16/9;
      background: #000;
    }
    
    .main-video, .main-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    
    /* Hero Product Section (Split Screen) */
    .hero-product-section {
      background-color: var(--bg-secondary);
      border-top: 1px solid var(--border-color);
      padding: 6rem 0;
    }
    
    .hero-product-split {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4rem;
      align-items: center;
    }
    
    .hero-product-img {
      width: 100%;
      border-radius: var(--radius-lg);
      box-shadow: 0 20px 40px rgba(0,0,0,0.4);
      object-fit: cover;
      aspect-ratio: 4/5;
      background-color: #fff;
    }
    
    .brand-products-section {
      background-color: var(--bg-primary);
      border-top: 1px solid var(--border-color);
      padding: 6rem 0;
    }
    
    .product-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 2.5rem;
    }
    
    .product-card {
      background-color: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    
    .product-card:hover {
      transform: translateY(-8px);
      box-shadow: 0 15px 35px rgba(0,0,0,0.5);
      border-color: var(--accent);
    }
    
    .product-img-wrapper {
      position: relative;
      aspect-ratio: 4/3;
      overflow: hidden;
      background-color: #fff;
    }
    
    .product-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }
    
    .product-card:hover .product-img {
      transform: scale(1.05);
    }
    
    .product-info {
      padding: 2rem;
      text-align: center;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      justify-content: space-between;
      background-color: var(--bg-tertiary);
    }
    
    .product-title {
      font-family: var(--font-serif);
      font-size: 1.6rem;
      margin-bottom: 1.5rem;
      color: var(--text-primary);
      letter-spacing: 0.05em;
    }
    
    .product-action .btn-secondary {
      width: 100%;
      display: inline-block;
      padding: 1.2rem;
      font-size: 0.9rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      border: 1px solid var(--accent);
      background: transparent;
      color: var(--accent);
      transition: all 0.3s ease;
    }
    
    .product-action .btn-secondary:hover {
      background: var(--accent);
      color: var(--bg-primary);
    }
    
    @media (max-width: 900px) {
      .hero-product-split { grid-template-columns: 1fr; gap: 3rem; }
    }
  </style>
</head>
"""

header_html = header_html.replace('</head>', brand_css)
title_replace = r'<title>.*?</title>'

# ==========================================
# GENERATE HANSGROHE
# ==========================================
hansgrohe_header = re.sub(title_replace, '<title>HANSGROHE Products | Home Studio Surat</title>', header_html)

hansgrohe_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/HANSGROHE/logo.png" alt="HANSGROHE Logo" class="brand-logo-large" style="background: white; padding: 15px; border-radius: 8px;">
      <h1 style="font-size: 1.8rem; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent);">Meet the Beauty of Water</h1>
    </div>
  </section>

  <!-- Main Feature Video -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <video class="main-video" autoplay muted loop playsinline controls>
          <source src="BRAND/HANSGROHE/AVALEGRA.mp4" type="video/mp4">
        </video>
      </div>
    </div>
  </section>

  <!-- Hero Product (Split Screen) -->
  <section class="hero-product-section" style="border-top: none;">
    <div class="container">
      <div class="hero-product-split">
        <div class="reveal">
          <img src="BRAND/HANSGROHE/Rain infinity series.jpeg" alt="HANSGROHE Rain Infinity" class="hero-product-img" style="object-fit: contain; padding: 2rem;">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">Hero Product</span>
          <h2 class="section-title">Rain Infinity</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8; font-size: 1.1rem; color: var(--text-secondary);">
            Immerse yourself in a shower experience like no other. The Rain Infinity series from Hansgrohe features an innovative, slightly concave spray disc and microfine water droplets that cocoon your body entirely, bringing a new dimension to your daily wellness routine.
          </p>
          <a href="contact.html?product=HANSGROHE+Rain+Infinity" class="btn-primary magnetic-btn" style="margin-top: 1.5rem;">Enquire About Rain Infinity</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">The HANSGROHE Portfolio</h2>
      </div>
      
      <div class="product-grid">
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/HANSGROHE/avalegra_brushed-bronze.jpg" alt="HANSGROHE Avalegra" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Avalegra Brushed Bronze</h3>
            <div class="product-action">
              <a href="contact.html?product=HANSGROHE+Avalegra" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/HANSGROHE/ecostat-comfort-.jpg" alt="HANSGROHE Ecostat" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Ecostat Comfort</h3>
            <div class="product-action">
              <a href="contact.html?product=HANSGROHE+Ecostat+Comfort" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 3 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/HANSGROHE/lavapura-element-s.jpg" alt="HANSGROHE Lavapura" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Lavapura Element S</h3>
            <div class="product-action">
              <a href="contact.html?product=HANSGROHE+Lavapura" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 4 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/HANSGROHE/raindance-alive.jpg" alt="HANSGROHE Raindance" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Raindance Alive</h3>
            <div class="product-action">
              <a href="contact.html?product=HANSGROHE+Raindance+Alive" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-hansgrohe.html'), 'w') as f:
    f.write(hansgrohe_header + hansgrohe_content + footer_html)


# ==========================================
# GENERATE ARTIZE
# ==========================================
artize_header = re.sub(title_replace, '<title>ARTIZE Products | Home Studio Surat</title>', header_html)

artize_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/ARTIZE/download.png" alt="ARTIZE Logo" class="brand-logo-large" style="background: white; padding: 15px; border-radius: 8px;">
      <h1 style="font-size: 1.8rem; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent);">Born From Art</h1>
    </div>
  </section>

  <!-- Main Feature Image (Fallback for Video) -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <img src="BRAND/ARTIZE/navia-morning-stories-5.jpg" alt="ARTIZE Showroom Experience" class="main-img" style="object-position: center;">
      </div>
    </div>
  </section>

  <!-- Hero Product (Split Screen) -->
  <section class="hero-product-section" style="border-top: none;">
    <div class="container">
      <div class="hero-product-split">
        <div class="reveal">
          <img src="BRAND/ARTIZE/navia-morning-stories-1.jpg" alt="ARTIZE Navia Collection" class="hero-product-img">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">Hero Product</span>
          <h2 class="section-title">Navia Collection</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8; font-size: 1.1rem; color: var(--text-secondary);">
            Discover absolute luxury with the Artize Navia series. Crafted to perfection, Navia blurs the lines between art and functionality, elevating the bathing space into an artistic masterpiece meant to be admired as much as it is to be experienced.
          </p>
          <a href="contact.html?product=ARTIZE+Navia" class="btn-primary magnetic-btn" style="margin-top: 1.5rem;">Enquire About Navia</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">The ARTIZE Portfolio</h2>
      </div>
      
      <div class="product-grid">
        
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/ARTIZE/6717af93b674ce964ff03a67.avif" alt="ARTIZE Basin Mixer" class="product-img" style="object-fit: contain;">
          </div>
          <div class="product-info">
            <h3 class="product-title">Luxury Basin Mixer</h3>
            <div class="product-action">
              <a href="contact.html?product=ARTIZE+Basin+Mixer" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/ARTIZE/Q.jpg" alt="ARTIZE Showers" class="product-img" style="object-fit: contain;">
          </div>
          <div class="product-info">
            <h3 class="product-title">Q-Series Showers</h3>
            <div class="product-action">
              <a href="contact.html?product=ARTIZE+Q+Series" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-artize.html'), 'w') as f:
    f.write(artize_header + artize_content + footer_html)

print("Generated brand-hansgrohe.html and brand-artize.html")
