import os
import re

DIR = '/Users/sidsmac/Documents/Home Studio'

with open(os.path.join(DIR, 'about.html'), 'r') as f:
    base_template = f.read()

# We need to extract the header and footer.
mobile_drawer_end_str = '<div class="mobile-overlay"></div>'
mobile_drawer_end_idx = base_template.find(mobile_drawer_end_str) + len(mobile_drawer_end_str)
header_html = base_template[:mobile_drawer_end_idx]

footer_start_idx = base_template.find('<!-- Detailed Footer -->')
footer_html = base_template[footer_start_idx:]

# Custom CSS for Brand Pages v2 (Product Focused)
brand_css = """
  <style>
    /* Product Focused Brand Pages */
    .brand-header-minimal {
      padding-top: calc(var(--header-height) + 4rem);
      padding-bottom: 3rem;
      text-align: center;
      background-color: var(--bg-primary);
    }
    
    .brand-logo-large {
      max-width: 350px;
      max-height: 150px;
      margin: 0 auto 2rem;
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
    
    .brand-products-section {
      background-color: var(--bg-secondary);
      border-top: 1px solid var(--border-color);
      padding: 6rem 0;
    }
    
    .product-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 3rem;
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
      transform: translateY(-5px);
      box-shadow: 0 15px 30px rgba(0,0,0,0.4);
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
      object-fit: contain;
      transition: transform 0.6s ease;
      padding: 2rem;
    }
    
    .product-card:hover .product-img {
      transform: scale(1.08);
    }
    
    .product-info {
      padding: 2rem;
      text-align: center;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      justify-content: space-between;
    }
    
    .product-title {
      font-family: var(--font-serif);
      font-size: 1.5rem;
      margin-bottom: 1rem;
      color: var(--text-primary);
    }
    
    .product-action {
      margin-top: auto;
    }
    
    .product-action .btn-secondary {
      width: 100%;
      display: inline-block;
      padding: 1rem;
    }
  </style>
</head>
"""

header_html = header_html.replace('</head>', brand_css)
title_replace = r'<title>.*?</title>'

# GENERATE AXOR
axor_header = re.sub(title_replace, '<title>AXOR Products | Home Studio Surat</title>', header_html)

axor_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/AXOR/logo.png" alt="AXOR Logo" class="brand-logo-large">
      <h1 style="font-size: 2.2rem; font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase;">The Luxury Collection</h1>
    </div>
  </section>

  <!-- Main Feature Video -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <video class="main-video" autoplay muted loop playsinline controls>
          <source src="BRAND/AXOR/AXOR ShowerHeaven 1200.mp4" type="video/mp4">
        </video>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">Explore AXOR Products</h2>
      </div>
      
      <div class="product-grid">
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/AXOR/axor shower heaven.jpg" alt="AXOR ShowerHeaven" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">AXOR ShowerHeaven</h3>
            <div class="product-action">
              <a href="contact.html?product=AXOR+ShowerHeaven" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/AXOR/axor_showerselect id.jpg" alt="AXOR ShowerSelect ID" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">AXOR ShowerSelect ID</h3>
            <div class="product-action">
              <a href="contact.html?product=AXOR+ShowerSelect+ID" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 3 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/AXOR/axor-axorstarckv.jpg" alt="AXOR Starck V" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">AXOR Starck V</h3>
            <div class="product-action">
              <a href="contact.html?product=AXOR+Starck+V" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 4 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/AXOR/axor-massaud.jpg" alt="AXOR Massaud" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">AXOR Massaud</h3>
            <div class="product-action">
              <a href="contact.html?product=AXOR+Massaud" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 5 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/AXOR/axor_archivio.jpg" alt="AXOR Archivio" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">AXOR Archivio</h3>
            <div class="product-action">
              <a href="contact.html?product=AXOR+Archivio" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-axor.html'), 'w') as f:
    f.write(axor_header + axor_content + footer_html)


# GENERATE BLANCO
blanco_header = re.sub(title_replace, '<title>BLANCO Products | Home Studio Surat</title>', header_html)

blanco_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/BLANCO/blanco.svg" alt="BLANCO Logo" class="brand-logo-large" style="filter: brightness(0) invert(1);">
      <h1 style="font-size: 2.2rem; font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase;">Premium Kitchen Solutions</h1>
    </div>
  </section>

  <!-- Main Feature Image (Fallback for Video) -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <img src="BRAND/BLANCO/quatrus-usupersingle.jpg" alt="BLANCO Quatrus" class="main-img">
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">Explore BLANCO Products</h2>
      </div>
      
      <div class="product-grid">
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/BLANCO/quatrus-usupersingle.jpg" alt="BLANCO Quatrus Super Single" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">BLANCO Quatrus Super Single</h3>
            <div class="product-action">
              <a href="contact.html?product=BLANCO+Quatrus+Super+Single" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/BLANCO/hafele_kitchen_sinks.webp" alt="BLANCO Kitchen Sink Collection" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">BLANCO Sink Collection</h3>
            <div class="product-action">
              <a href="contact.html?product=BLANCO+Sink+Collection" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-blanco.html'), 'w') as f:
    f.write(blanco_header + blanco_content + footer_html)

print("Generated completely redesigned, product-centric brand pages for AXOR and BLANCO.")
