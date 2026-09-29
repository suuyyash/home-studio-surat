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

# GENERATE GROHE
grohe_header = re.sub(title_replace, '<title>GROHE Products | Home Studio Surat</title>', header_html)

grohe_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/GROHE/images.png" alt="GROHE Logo" class="brand-logo-large" style="background: white; padding: 15px; border-radius: 8px;">
      <h1 style="font-size: 1.8rem; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent);">Pure Freude an Wasser</h1>
    </div>
  </section>

  <!-- Main Feature Video -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <video class="main-video" autoplay muted loop playsinline controls>
          <source src="BRAND/GROHE/ICON 3D.mp4" type="video/mp4">
        </video>
      </div>
    </div>
  </section>

  <!-- Hero Product (Split Screen) -->
  <section class="hero-product-section" style="border-top: none;">
    <div class="container">
      <div class="hero-product-split">
        <div class="reveal">
          <img src="BRAND/GROHE/AQUA CONCEAL.webp" alt="GROHE Aqua Conceal" class="hero-product-img" style="object-fit: contain; padding: 2rem;">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">Hero Product</span>
          <h2 class="section-title">Aqua Conceal</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8; font-size: 1.1rem; color: var(--text-secondary);">
            Experience seamless bathroom design with GROHE's concealed solutions. The Aqua Conceal systems offer minimalistic elegance while hiding the complex plumbing behind the wall, giving you more space and freedom in your luxury bathroom.
          </p>
          <a href="contact.html?product=GROHE+Aqua+Conceal" class="btn-primary magnetic-btn" style="margin-top: 1.5rem;">Enquire About Aqua Conceal</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">The GROHE Portfolio</h2>
      </div>
      
      <div class="product-grid">
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GROHE/GROHE 3D ICON.jpg" alt="GROHE 3D Icon" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Icon 3D Printed Faucet</h3>
            <div class="product-action">
              <a href="contact.html?product=GROHE+Icon+3D+Faucet" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GROHE/GROHE PLATES.webp" alt="GROHE Flush Plates" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Designer Flush Plates</h3>
            <div class="product-action">
              <a href="contact.html?product=GROHE+Flush+Plates" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 3 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GROHE/GROHE_SPA_Grohtherm_Aqua_Tiles_.jpg" alt="GROHE SPA Grohtherm" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">SPA Grohtherm Aqua</h3>
            <div class="product-action">
              <a href="contact.html?product=GROHE+SPA+Grohtherm" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 4 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GROHE/Grohe_Icon_3D.webp" alt="GROHE Icon 3D Collection" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Icon 3D Collection</h3>
            <div class="product-action">
              <a href="contact.html?product=GROHE+Icon+3D+Collection" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 5 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GROHE/GROHE-SPA-Icon-3D-NEW.jpg" alt="GROHE SPA Icon 3D" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">SPA Icon 3D</h3>
            <div class="product-action">
              <a href="contact.html?product=GROHE+SPA+Icon+3D" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 6 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/GROHE/SPA_GROHE_Icon_3D_8.avif" alt="GROHE SPA Elements" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">SPA Elements</h3>
            <div class="product-action">
              <a href="contact.html?product=GROHE+SPA+Elements" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-grohe.html'), 'w') as f:
    f.write(grohe_header + grohe_content + footer_html)


# GENERATE JAQUAR
jaquar_header = re.sub(title_replace, '<title>JAQUAR Products | Home Studio Surat</title>', header_html)

jaquar_content = """
  <!-- Minimal Header -->
  <section class="brand-header-minimal">
    <div class="container reveal">
      <img src="BRAND/JAQUAR/download.png" alt="JAQUAR Logo" class="brand-logo-large" style="background: white; padding: 15px; border-radius: 8px;">
      <h1 style="font-size: 1.8rem; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; color: var(--accent);">Experience Bathing</h1>
    </div>
  </section>

  <!-- Main Feature Image (Fallback for Video) -->
  <section class="brand-main-feature">
    <div class="container">
      <div class="main-feature-media reveal reveal-delay-1">
        <img src="BRAND/JAQUAR/0096401_Laguna-375x450-copy-2.jpeg" alt="JAQUAR Laguna Collection" class="main-img" style="object-position: top;">
      </div>
    </div>
  </section>

  <!-- Hero Product (Split Screen) -->
  <section class="hero-product-section" style="border-top: none;">
    <div class="container">
      <div class="hero-product-split">
        <div class="reveal">
          <img src="BRAND/JAQUAR/0055444_queens-prime_400.webp" alt="JAQUAR Queens Prime" class="hero-product-img" style="object-fit: contain; padding: 2rem;">
        </div>
        <div class="reveal reveal-delay-1">
          <span class="section-tag" style="color: var(--accent);">Hero Product</span>
          <h2 class="section-title">Queens Prime</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8; font-size: 1.1rem; color: var(--text-secondary);">
            The Queens Prime collection brings a royal touch to your bathroom spaces. With its elegant curves and majestic stance, it reflects Jaquar's commitment to flawless craftsmanship and enduring style.
          </p>
          <a href="contact.html?product=JAQUAR+Queens+Prime" class="btn-primary magnetic-btn" style="margin-top: 1.5rem;">Enquire About Queens Prime</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Product Grid -->
  <section class="brand-products-section">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <h2 class="section-title">The JAQUAR Portfolio</h2>
      </div>
      
      <div class="product-grid" style="grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));">
        
        <!-- Product 1 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/JAQUAR/mode-1.jpg" alt="JAQUAR Mode Collection" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Mode Collection</h3>
            <div class="product-action">
              <a href="contact.html?product=JAQUAR+Mode+Collection" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

        <!-- Product 2 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/JAQUAR/mode-4-b.jpg" alt="JAQUAR Mode Basin Mixer" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Mode Basin Mixer</h3>
            <div class="product-action">
              <a href="contact.html?product=JAQUAR+Mode+Basin+Mixer" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>
        
        <!-- Product 3 -->
        <div class="product-card reveal">
          <div class="product-img-wrapper">
            <img src="BRAND/JAQUAR/0096401_Laguna-375x450-copy-2.jpeg" alt="JAQUAR Laguna" class="product-img">
          </div>
          <div class="product-info">
            <h3 class="product-title">Laguna Series</h3>
            <div class="product-action">
              <a href="contact.html?product=JAQUAR+Laguna" class="btn-secondary">Enquire Now</a>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'brand-jaquar.html'), 'w') as f:
    f.write(jaquar_header + jaquar_content + footer_html)

print("Generated brand-grohe.html and brand-jaquar.html")
