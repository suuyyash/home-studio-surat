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

# Custom CSS for Brand Pages v3 (Refined Product Focus + Hero Product)
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
# GENERATE OYSTER
# ==========================================
oyster_header = re.sub(title_replace, '<title>OYSTER Bath Concepts | Home Studio Surat</title>', header_html)

oyster_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/OYSTER/images.jpeg" alt="OYSTER Logo" class="brand-logo-large" style="background: white; padding: 15px; border-radius: 8px;">
      <h1 style="font-size: 1.8rem; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent);">Wellness and Luxury</h1>
    </div>
  </section>

  <!-- Main Feature Video -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <video class="main-video" autoplay muted loop playsinline controls>
          <source src="BRAND/OYSTER/DREAM WAVE.mp4" type="video/mp4">
        </video>
      </div>
    </div>
  </section>

  <!-- Hero Product (Split Screen) -->
  <section class="hero-product-section" style="border-top: none;">
    <div class="container">
      <div class="hero-product-split">
        <div class="reveal">
          <img src="BRAND/OYSTER/DREAM WAVE.png" alt="OYSTER Dream Wave" class="hero-product-img" style="object-fit: contain; padding: 2rem;">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">Hero Product</span>
          <h2 class="section-title">Dream Wave</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8; font-size: 1.1rem; color: var(--text-secondary);">
            The Dream Wave bathtub represents the pinnacle of hydrotherapy and relaxation. Designed with ergonomic precision, it transforms your bathroom into a personal spa oasis. Let the waves of tranquility wash over you.
          </p>
          <a href="contact.html?product=OYSTER+Dream+Wave" class="btn-primary magnetic-btn" style="margin-top: 1.5rem;">Enquire About Dream Wave</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">The OYSTER Portfolio</h2>
      </div>
      
      <div class="product-grid">
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/OYSTER/ARIKA.png" alt="OYSTER Arika" class="product-img" style="object-fit: contain;">
          </div>
          <div class="product-info">
            <h3 class="product-title">Arika Collection</h3>
            <div class="product-action">
              <a href="contact.html?product=OYSTER+Arika" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/OYSTER/CASCADIA.png" alt="OYSTER Cascadia" class="product-img" style="object-fit: contain;">
          </div>
          <div class="product-info">
            <h3 class="product-title">Cascadia Collection</h3>
            <div class="product-action">
              <a href="contact.html?product=OYSTER+Cascadia" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 3 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/OYSTER/RIVEERA.png" alt="OYSTER Riveera" class="product-img" style="object-fit: contain;">
          </div>
          <div class="product-info">
            <h3 class="product-title">Riveera Collection</h3>
            <div class="product-action">
              <a href="contact.html?product=OYSTER+Riveera" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 4 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/OYSTER/SPA.jpeg" alt="OYSTER SPA" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">SPA Systems</h3>
            <div class="product-action">
              <a href="contact.html?product=OYSTER+SPA+Systems" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-oyster.html'), 'w') as f:
    f.write(oyster_header + oyster_content + footer_html)


# ==========================================
# GENERATE STIEBEL
# ==========================================
stiebel_header = re.sub(title_replace, '<title>STIEBEL ELTRON Products | Home Studio Surat</title>', header_html)

stiebel_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/STIEBEL/images.png" alt="STIEBEL ELTRON Logo" class="brand-logo-large" style="background: white; padding: 15px; border-radius: 8px;">
      <h1 style="font-size: 1.8rem; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent);">Advanced Water Heating</h1>
    </div>
  </section>

  <!-- Main Feature Image (Fallback for Video) -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <img src="BRAND/STIEBEL/Showroom_5083_767x480.jpg" alt="STIEBEL ELTRON Showroom" class="main-img">
      </div>
    </div>
  </section>

  <!-- Hero Product (Split Screen) -->
  <section class="hero-product-section" style="border-top: none;">
    <div class="container">
      <div class="hero-product-split">
        <div class="reveal">
          <img src="BRAND/STIEBEL/images.jpeg" alt="STIEBEL ELTRON Water Heater" class="hero-product-img" style="object-fit: contain; padding: 2rem;">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">Hero Product</span>
          <h2 class="section-title">Instant Water Heaters</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8; font-size: 1.1rem; color: var(--text-secondary);">
            Experience unmatched German engineering with STIEBEL ELTRON's instantaneous water heaters. Energy-efficient, incredibly compact, and providing an endless supply of hot water right when you need it.
          </p>
          <a href="contact.html?product=STIEBEL+Instant+Heater" class="btn-primary magnetic-btn" style="margin-top: 1.5rem;">Enquire About Heaters</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">The STIEBEL ELTRON Portfolio</h2>
      </div>
      
      <div class="product-grid" style="grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));">
        
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/STIEBEL/images.jpeg" alt="STIEBEL Water Heater" class="product-img" style="object-fit: contain;">
          </div>
          <div class="product-info">
            <h3 class="product-title">Instant Water Heater</h3>
            <div class="product-action">
              <a href="contact.html?product=STIEBEL+Instant+Heater" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/STIEBEL/Showroom_5083_767x480.jpg" alt="STIEBEL Showroom Products" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Heating Systems</h3>
            <div class="product-action">
              <a href="contact.html?product=STIEBEL+Heating+Systems" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-stiebel.html'), 'w') as f:
    f.write(stiebel_header + stiebel_content + footer_html)


# ==========================================
# GENERATE TECE
# ==========================================
tece_header = re.sub(title_replace, '<title>TECE Products | Home Studio Surat</title>', header_html)

tece_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/TECE/menulogo.svg" alt="TECE Logo" class="brand-logo-large" style="background: white; padding: 15px; border-radius: 8px;">
      <h1 style="font-size: 1.8rem; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent);">Intelligent Building Technology</h1>
    </div>
  </section>

  <!-- Main Feature Image (Fallback for Video) -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <img src="BRAND/TECE/TECEdrainprofile_Kollektionsteaser_2.jpg" alt="TECEdrainprofile" class="main-img">
      </div>
    </div>
  </section>

  <!-- Hero Product (Split Screen) -->
  <section class="hero-product-section" style="border-top: none;">
    <div class="container">
      <div class="hero-product-split">
        <div class="reveal">
          <img src="BRAND/TECE/COL_TECEdrainway_1064x765_if-Design.jpg" alt="TECEdrainway" class="hero-product-img">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">Hero Product</span>
          <h2 class="section-title">TECEdrainway</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8; font-size: 1.1rem; color: var(--text-secondary);">
            Award-winning shower drainage. The TECEdrainway shower channel offers unparalleled aesthetics and reliable performance. Seamlessly integrating into your shower floor, it provides a barrier-free, minimalist design that defines modern bathroom luxury.
          </p>
          <a href="contact.html?product=TECEdrainway" class="btn-primary magnetic-btn" style="margin-top: 1.5rem;">Enquire About TECEdrainway</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">The TECE Portfolio</h2>
      </div>
      
      <div class="product-grid" style="grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));">
        
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/TECE/COL_TECEdrainway_1064x765_if-Design.jpg" alt="TECEdrainway" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">TECEdrainway</h3>
            <div class="product-action">
              <a href="contact.html?product=TECEdrainway" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/TECE/TECEdrainprofile_Kollektionsteaser_2.jpg" alt="TECEdrainprofile" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">TECEdrainprofile</h3>
            <div class="product-action">
              <a href="contact.html?product=TECEdrainprofile" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-tece.html'), 'w') as f:
    f.write(tece_header + tece_content + footer_html)

print("Generated brand-oyster.html, brand-stiebel.html, and brand-tece.html")
