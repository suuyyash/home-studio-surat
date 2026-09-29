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

# GENERATE CARYSIL
carysil_header = re.sub(title_replace, '<title>CARYSIL Products | Home Studio Surat</title>', header_html)

carysil_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/CARYSIL/images.png" alt="CARYSIL Logo" class="brand-logo-large" style="background: white; padding: 10px; border-radius: 8px;">
      <h1 style="font-size: 1.8rem; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent);">Innovative Kitchen Solutions</h1>
    </div>
  </section>

  <!-- Main Feature Image (Fallback for Video) -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <img src="BRAND/CARYSIL/stainless steel kitchen fitting.jpg" alt="CARYSIL Stainless Steel Kitchen Fitting" class="main-img">
      </div>
    </div>
  </section>

  <!-- Hero Product (Split Screen) -->
  <section class="hero-product-section" style="border-top: none;">
    <div class="container">
      <div class="hero-product-split">
        <div class="reveal">
          <img src="BRAND/CARYSIL/CarysilKristallCollection.webp" alt="CARYSIL Kristall Collection" class="hero-product-img">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">Hero Product</span>
          <h2 class="section-title">Kristall Collection</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8; font-size: 1.1rem; color: var(--text-secondary);">
            The Carysil Kristall Collection redefines the modern kitchen space with its stunning aesthetics and unparalleled durability. Engineered with precision, these quartz sinks offer resistance to scratches, heat, and stains, delivering a pristine look that lasts a lifetime.
          </p>
          <a href="contact.html?product=CARYSIL+Kristall+Collection" class="btn-primary magnetic-btn" style="margin-top: 1.5rem;">Enquire About Kristall</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">The CARYSIL Portfolio</h2>
      </div>
      
      <div class="product-grid" style="grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));">
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/CARYSIL/CarysilKristallCollection.webp" alt="CARYSIL Kristall Collection" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Kristall Collection</h3>
            <div class="product-action">
              <a href="contact.html?product=CARYSIL+Kristall+Collection" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/CARYSIL/product-jpeg.jpg" alt="CARYSIL Granite Sink" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Granite Sink</h3>
            <div class="product-action">
              <a href="contact.html?product=CARYSIL+Granite+Sink" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 3 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/CARYSIL/stainless steel kitchen fitting.jpg" alt="CARYSIL Stainless Steel Fitting" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Stainless Steel Sink</h3>
            <div class="product-action">
              <a href="contact.html?product=CARYSIL+Stainless+Steel+Sink" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-carysil.html'), 'w') as f:
    f.write(carysil_header + carysil_content + footer_html)


# GENERATE GEBERIT
geberit_header = re.sub(title_replace, '<title>GEBERIT Products | Home Studio Surat</title>', header_html)

geberit_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/GEBERIT/images.png" alt="GEBERIT Logo" class="brand-logo-large" style="background: white; padding: 10px; border-radius: 8px;">
      <h1 style="font-size: 1.8rem; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent);">Swiss Sanitary Engineering</h1>
    </div>
  </section>

  <!-- Main Feature Image (Fallback for Video) -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <img src="BRAND/GEBERIT/TANK.jpg" alt="GEBERIT Concealed Cistern" class="main-img">
      </div>
    </div>
  </section>

  <!-- Hero Product (Split Screen) -->
  <section class="hero-product-section" style="border-top: none;">
    <div class="container">
      <div class="hero-product-split">
        <div class="reveal">
          <img src="BRAND/GEBERIT/Geberit-Sigma70-all-colours.jpg" alt="GEBERIT Sigma70 Actuator Plates" class="hero-product-img">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">Hero Product</span>
          <h2 class="section-title">Sigma70 Flush Plates</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8; font-size: 1.1rem; color: var(--text-secondary);">
            The Geberit Sigma70 actuator plate brings floating elegance to the bathroom. With its seemingly weightless design and reliable, smooth pneumatic flush actuation, it represents the pinnacle of modern Swiss sanitary technology. Available in a wide array of exquisite colors and finishes.
          </p>
          <a href="contact.html?product=GEBERIT+Sigma70" class="btn-primary magnetic-btn" style="margin-top: 1.5rem;">Enquire About Sigma70</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">The GEBERIT Portfolio</h2>
      </div>
      
      <div class="product-grid" style="grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));">
        
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GEBERIT/Geberit-Sigma70-all-colours.jpg" alt="GEBERIT Sigma70" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Sigma70 Actuator Plate</h3>
            <div class="product-action">
              <a href="contact.html?product=GEBERIT+Sigma70" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GEBERIT/SIGMA 40 PLATES.avif" alt="GEBERIT Sigma40 Plates" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Sigma40 Flush Plates</h3>
            <div class="product-action">
              <a href="contact.html?product=GEBERIT+Sigma40+Plates" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 3 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GEBERIT/SIGMA 40.jpg" alt="GEBERIT Sigma40 System" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Sigma40 System</h3>
            <div class="product-action">
              <a href="contact.html?product=GEBERIT+Sigma40" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 4 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GEBERIT/SIGMA 50.jpg" alt="GEBERIT Sigma50" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Sigma50 Actuator Plate</h3>
            <div class="product-action">
              <a href="contact.html?product=GEBERIT+Sigma50" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 5 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GEBERIT/TANK.jpg" alt="GEBERIT Concealed Cistern" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Concealed Cistern System</h3>
            <div class="product-action">
              <a href="contact.html?product=GEBERIT+Concealed+Cistern" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-geberit.html'), 'w') as f:
    f.write(geberit_header + geberit_content + footer_html)

print("Generated brand-carysil.html and brand-geberit.html")
