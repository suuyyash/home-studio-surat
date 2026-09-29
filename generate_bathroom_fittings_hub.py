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

# Update title and styling for Bathroom Fittings page
title_replace = r'<title>.*?</title>'
header_html = re.sub(title_replace, '<title>Luxury Brands Hub | Home Studio Surat</title>', header_html)

# Custom css for the hub
hub_css = """
  <style>
    .page-hero {
        padding-top: 150px;
        padding-bottom: 80px;
        text-align: center;
        background-color: var(--bg-secondary);
        border-bottom: 1px solid var(--border-color);
    }
    .page-title {
        font-family: var(--font-serif);
        font-size: clamp(3rem, 6vw, 5rem);
        color: var(--accent);
        margin-bottom: 1rem;
    }
    .page-subtitle {
        font-size: 1.2rem;
        color: var(--text-secondary);
        max-width: 700px;
        margin: 0 auto;
    }
    
    .brand-section {
        padding: 6rem 0;
        border-bottom: 1px solid var(--border-color);
    }
    .brand-section:nth-child(even) {
        background-color: var(--bg-tertiary);
    }
    .brand-section:nth-child(odd) {
        background-color: var(--bg-primary);
    }
    
    .brand-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    .brand-logo {
        max-width: 250px;
        max-height: 100px;
        object-fit: contain;
        margin: 0 auto;
        display: block;
        background: white;
        padding: 10px;
        border-radius: 8px;
    }
    
    .brand-video-container {
        width: 100%;
        max-width: 1000px;
        margin: 0 auto 3rem;
        border-radius: var(--radius-lg);
        overflow: hidden;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        background: #000;
        aspect-ratio: 16/9;
    }
    .brand-video {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }
    
    .brand-gallery {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
        margin-bottom: 3rem;
    }
    .gallery-item {
        border-radius: var(--radius-md);
        overflow: hidden;
        aspect-ratio: 4/3;
        background: var(--bg-tertiary);
        border: 1px solid var(--border-color);
    }
    .gallery-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
    }
    .gallery-item:hover .gallery-img {
        transform: scale(1.05);
    }
    
    .explore-brand-btn-container {
        text-align: center;
        margin-top: 3rem;
    }
    
    .explore-brand-btn-container .btn-secondary {
        padding: 1.2rem 3.5rem;
        font-size: 0.95rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        border: 1px solid var(--accent);
        background: transparent;
        color: var(--accent);
        transition: all 0.3s ease;
        display: inline-block;
    }
    .explore-brand-btn-container .btn-secondary:hover {
        background: var(--accent);
        color: var(--bg-primary);
    }
  </style>
</head>
"""

header_html = header_html.replace('</head>', hub_css)

content_html = """
  <section class="page-hero">
    <div class="container reveal">
      <h1 class="page-title">Masterpieces in Water</h1>
      <p class="page-subtitle">Explore our exclusive curation of the world's most elite bathroom fittings, sanitary ware, and wellness brands.</p>
    </div>
  </section>

  <!-- Brands Showcase -->
  
  <!-- ARTIZE -->
  <section class="brand-section" id="artize">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/ARTIZE/download.png" alt="ARTIZE Logo" class="brand-logo">
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/ARTIZE/navia-morning-stories-1.jpg" alt="ARTIZE" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/ARTIZE/6717af93b674ce964ff03a67.avif" alt="ARTIZE" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/ARTIZE/Q.jpg" alt="ARTIZE" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-artize.html" class="btn-secondary">Explore ARTIZE</a>
      </div>
    </div>
  </section>

  <!-- AXOR -->
  <section class="brand-section" id="axor">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/AXOR/logo.png" alt="AXOR Logo" class="brand-logo">
      </div>
      <div class="brand-video-container reveal">
        <video class="brand-video" autoplay muted loop playsinline>
          <source src="BRAND/AXOR/AXOR ShowerHeaven 1200.mp4" type="video/mp4">
        </video>
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/AXOR/axor shower heaven.jpg" alt="AXOR" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/AXOR/axor_showerselect id.jpg" alt="AXOR" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/AXOR/axor-axorstarckv.jpg" alt="AXOR" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-axor.html" class="btn-secondary">Explore AXOR</a>
      </div>
    </div>
  </section>

  <!-- BLANCO -->
  <section class="brand-section" id="blanco">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/BLANCO/blanco.svg" alt="BLANCO Logo" class="brand-logo" style="filter: brightness(0); background: transparent; padding: 0;">
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/BLANCO/quatrus-usupersingle.jpg" alt="BLANCO" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/BLANCO/hafele_kitchen_sinks.webp" alt="BLANCO" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-blanco.html" class="btn-secondary">Explore BLANCO</a>
      </div>
    </div>
  </section>

  <!-- CARYSIL -->
  <section class="brand-section" id="carysil">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/CARYSIL/images.png" alt="CARYSIL Logo" class="brand-logo">
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/CARYSIL/CarysilKristallCollection.webp" alt="CARYSIL" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/CARYSIL/product-jpeg.jpg" alt="CARYSIL" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/CARYSIL/stainless steel kitchen fitting.jpg" alt="CARYSIL" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-carysil.html" class="btn-secondary">Explore CARYSIL</a>
      </div>
    </div>
  </section>

  <!-- GEBERIT -->
  <section class="brand-section" id="geberit">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/GEBERIT/images.png" alt="GEBERIT Logo" class="brand-logo">
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/GEBERIT/Geberit-Sigma70-all-colours.jpg" alt="GEBERIT" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/GEBERIT/SIGMA 40 PLATES.avif" alt="GEBERIT" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/GEBERIT/SIGMA 50.jpg" alt="GEBERIT" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-geberit.html" class="btn-secondary">Explore GEBERIT</a>
      </div>
    </div>
  </section>

  <!-- GROHE -->
  <section class="brand-section" id="grohe">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/GROHE/images.png" alt="GROHE Logo" class="brand-logo">
      </div>
      <div class="brand-video-container reveal">
        <video class="brand-video" autoplay muted loop playsinline>
          <source src="BRAND/GROHE/ICON 3D.mp4" type="video/mp4">
        </video>
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/GROHE/AQUA CONCEAL.webp" alt="GROHE" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/GROHE/GROHE 3D ICON.jpg" alt="GROHE" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/GROHE/GROHE PLATES.webp" alt="GROHE" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-grohe.html" class="btn-secondary">Explore GROHE</a>
      </div>
    </div>
  </section>

  <!-- HANSGROHE -->
  <section class="brand-section" id="hansgrohe">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/HANSGROHE/logo.png" alt="HANSGROHE Logo" class="brand-logo">
      </div>
      <div class="brand-video-container reveal">
        <video class="brand-video" autoplay muted loop playsinline>
          <source src="BRAND/HANSGROHE/AVALEGRA.mp4" type="video/mp4">
        </video>
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/HANSGROHE/Rain infinity series.jpeg" alt="HANSGROHE" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/HANSGROHE/avalegra_brushed-bronze.jpg" alt="HANSGROHE" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/HANSGROHE/raindance-alive.jpg" alt="HANSGROHE" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-hansgrohe.html" class="btn-secondary">Explore HANSGROHE</a>
      </div>
    </div>
  </section>

  <!-- JAQUAR -->
  <section class="brand-section" id="jaquar">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/JAQUAR/download.png" alt="JAQUAR Logo" class="brand-logo">
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/JAQUAR/0055444_queens-prime_400.webp" alt="JAQUAR" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/JAQUAR/0096401_Laguna-375x450-copy-2.jpeg" alt="JAQUAR" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/JAQUAR/mode-1.jpg" alt="JAQUAR" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-jaquar.html" class="btn-secondary">Explore JAQUAR</a>
      </div>
    </div>
  </section>

  <!-- OYSTER -->
  <section class="brand-section" id="oyster">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/OYSTER/images.jpeg" alt="OYSTER Logo" class="brand-logo">
      </div>
      <div class="brand-video-container reveal">
        <video class="brand-video" autoplay muted loop playsinline>
          <source src="BRAND/OYSTER/DREAM WAVE.mp4" type="video/mp4">
        </video>
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/OYSTER/DREAM WAVE.png" alt="OYSTER" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/OYSTER/ARIKA.png" alt="OYSTER" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/OYSTER/CASCADIA.png" alt="OYSTER" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-oyster.html" class="btn-secondary">Explore OYSTER</a>
      </div>
    </div>
  </section>

  <!-- STIEBEL ELTRON -->
  <section class="brand-section" id="stiebel">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/STIEBEL/images.png" alt="STIEBEL Logo" class="brand-logo">
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/STIEBEL/Showroom_5083_767x480.jpg" alt="STIEBEL" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/STIEBEL/images.jpeg" alt="STIEBEL" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-stiebel.html" class="btn-secondary">Explore STIEBEL</a>
      </div>
    </div>
  </section>

  <!-- TECE -->
  <section class="brand-section" id="tece">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/TECE/menulogo.svg" alt="TECE Logo" class="brand-logo">
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/TECE/COL_TECEdrainway_1064x765_if-Design.jpg" alt="TECE" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/TECE/TECEdrainprofile_Kollektionsteaser_2.jpg" alt="TECE" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-tece.html" class="btn-secondary">Explore TECE</a>
      </div>
    </div>
  </section>

  <!-- TOTO -->
  <section class="brand-section" id="toto">
    <div class="container">
      <div class="brand-header reveal">
        <img src="BRAND/TOTO/download.png" alt="TOTO Logo" class="brand-logo">
      </div>
      <div class="brand-video-container reveal">
        <video class="brand-video" autoplay muted loop playsinline>
          <source src="BRAND/TOTO/TOTO FLOATATION.mp4" type="video/mp4">
        </video>
      </div>
      <div class="brand-gallery">
        <div class="gallery-item reveal"><img src="BRAND/TOTO/NX1.webp" alt="TOTO" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/TOTO/RW WASHLET.jpg" alt="TOTO" class="gallery-img" loading="lazy"></div>
        <div class="gallery-item reveal"><img src="BRAND/TOTO/FLOATATION.jpg" alt="TOTO" class="gallery-img" loading="lazy"></div>
      </div>
      <div class="explore-brand-btn-container reveal">
        <a href="brand-toto.html" class="btn-secondary">Explore TOTO</a>
      </div>
    </div>
  </section>
"""

with open(os.path.join(DIR, 'bathroom-fittings.html'), 'w') as f:
    f.write(header_html + content_html + footer_html)

print("Regenerated bathroom-fittings.html correctly with Explore buttons placed below the gallery section.")
