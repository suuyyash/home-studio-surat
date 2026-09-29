import os
import re

CITIES = [
  'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 
  'Ahmedabad', 'Chennai', 'Kolkata', 'Pune', 
  'Jaipur', 'Surat'
]

DIR = '/Users/sidsmac/Documents/Home Studio'

with open(os.path.join(DIR, 'about.html'), 'r') as f:
    base_template = f.read()

header_end = '<!-- Mobile Drawer Menu -->'
footer_start = '<!-- Detailed Footer -->'

header_end_idx = base_template.find(header_end)
footer_start_idx = base_template.find(footer_start)

if header_end_idx != -1 and footer_start_idx != -1:
    footer_and_tail = base_template[footer_start_idx:]
    mobile_drawer_end_str = '<div class="mobile-overlay"></div>'
    mobile_drawer_end_idx = base_template.find(mobile_drawer_end_str) + len(mobile_drawer_end_str)
    
    # We will inject some custom CSS right before </head> for the new components
    true_head_and_header = base_template[:mobile_drawer_end_idx]
    
    custom_css = """
  <style>
    /* Premium SEO Page Components */
    .hero-seo {
      position: relative;
      height: 90vh;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('images/showroom-interior.jpg') no-repeat center center/cover;
      color: #fff;
      padding-top: var(--header-height);
    }
    
    .stats-banner {
      background-color: #0c0b0a;
      color: #fff;
      padding: 6rem 0;
      border-top: 1px solid rgba(255,255,255,0.1);
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 2rem;
      text-align: center;
    }
    .stat-number {
      font-family: var(--font-serif);
      font-size: 4rem;
      color: var(--accent);
      margin-bottom: 0.5rem;
      line-height: 1;
    }
    .stat-label {
      font-size: 0.85rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: #9c9993;
    }
    
    .card-grid-premium {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 3rem;
    }
    .premium-hover-card {
      position: relative;
      overflow: hidden;
      border-radius: var(--radius-lg);
      aspect-ratio: 4/3;
      group: hover;
    }
    .premium-hover-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.8s ease;
    }
    .premium-hover-card:hover .premium-hover-img {
      transform: scale(1.05);
    }
    .premium-hover-content {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      padding: 3rem 2rem;
      background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%);
      color: #fff;
    }
    
    .testimonials-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 2.5rem;
    }
    .testimonial-card {
      background-color: var(--bg-tertiary);
      padding: 3rem 2rem;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      position: relative;
    }
    .quote-icon {
      font-family: var(--font-serif);
      font-size: 4rem;
      color: var(--accent);
      opacity: 0.3;
      position: absolute;
      top: 1rem;
      left: 2rem;
      line-height: 1;
    }
    
    /* Accordion */
    .faq-accordion {
      max-width: 900px;
      margin: 0 auto;
    }
    .accordion-item {
      border-bottom: 1px solid var(--border-color);
      margin-bottom: 1rem;
    }
    .accordion-header {
      width: 100%;
      text-align: left;
      padding: 1.5rem 0;
      font-family: var(--font-serif);
      font-size: 1.5rem;
      color: var(--text-primary);
      background: none;
      border: none;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: color 0.3s ease;
    }
    .accordion-header:hover {
      color: var(--accent);
    }
    .accordion-content {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.4s ease, padding 0.4s ease;
    }
    .accordion-content p {
      font-weight: 300;
      padding-bottom: 1.5rem;
    }
    .accordion-item.active .accordion-content {
      max-height: 800px; /* arbitrary large max-height */
    }
    .accordion-icon {
      font-size: 1.5rem;
      color: var(--accent);
      transition: transform 0.3s ease;
    }
    .accordion-item.active .accordion-icon {
      transform: rotate(45deg);
    }

    @media (max-width: 900px) {
      .stats-grid { grid-template-columns: repeat(2, 1fr); }
      .card-grid-premium { grid-template-columns: 1fr; }
      .testimonials-grid { grid-template-columns: 1fr; }
    }
  </style>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const accordions = document.querySelectorAll('.accordion-header');
      accordions.forEach(acc => {
        acc.addEventListener('click', function() {
          this.parentElement.classList.toggle('active');
        });
      });
    });
  </script>
</head>
"""
    # We need to inject custom_css right before </head>
    true_head_and_header = true_head_and_header.replace('</head>', custom_css)

    for city in CITIES:
        page = true_head_and_header
        
        # Replace title and meta description
        page = re.sub(r'<title>.*?</title>', f'<title>Luxury Interior Design & Premium Bath Fittings in {city} | Home Studio</title>', page)
        page = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="Elevate your {city} property with bespoke luxury bathroom fittings, smart sanitary ware, imported marble tiles, and wellness spas curated by Home Studio.">', page)

        city_content = f"""
  <!-- Hero Section -->
  <section class="hero-seo">
    <div class="container reveal" style="position: relative; z-index: 10;">
      <span class="section-tag" style="color: var(--accent); text-shadow: 0 2px 4px rgba(0,0,0,0.5);">Exclusive Architecture in {city}</span>
      <h1 style="color: #fff; text-shadow: 0 4px 20px rgba(0,0,0,0.6); margin-bottom: 2rem;">The Pinnacle of Luxury<br>Bath & Surfaces</h1>
      <p style="color: #eaeaea; max-width: 700px; margin: 0 auto 3rem; font-size: 1.2rem; text-shadow: 0 2px 8px rgba(0,0,0,0.5); font-weight: 300;">
        Transforming {city}'s finest residences and commercial developments with world-class sanitary ware, imported tiles, and elite wellness systems.
      </p>
      <a href="contact.html" class="btn-primary magnetic-btn">Book Your Consultation</a>
    </div>
  </section>

  <!-- Architectural Context Split-Screen -->
  <section class="section-padding" style="background-color: var(--bg-primary);">
    <div class="container">
      <div class="editorial-grid">
        <div class="editorial-col-6 reveal">
          <div class="editorial-img-wrap" style="aspect-ratio: 4/5;">
            <img src="images/bathroom-fittings.jpg" alt="Luxury Bathroom Interior in {city}">
          </div>
        </div>
        <div class="editorial-col-6 reveal reveal-delay-1" style="padding-left: 2rem;">
          <span class="section-tag">Bespoke Living</span>
          <h2 class="section-title">Elevating {city}'s Real Estate</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300;">
            The architectural landscape of {city} demands nothing short of perfection. At Home Studio, we bridge the gap between global design hubs and {city}'s elite property developers, bringing you unparalleled access to the world's most luxurious bathroom and surface materials.
          </p>
          <p style="margin-bottom: 2.5rem; font-weight: 300;">
            Whether you are designing a high-altitude penthouse that requires minimalist, intelligent water systems or a sprawling heritage villa demanding ornate brushed-gold fixtures, our curation ensures your project in {city} is executed flawlessly. We collaborate directly with leading interior designers and architects to supply materials that offer robust longevity and cutting-edge aesthetics.
          </p>
          <a href="about.html" class="btn-secondary">Discover Our Legacy</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Curated Collections (Card Grid) -->
  <section class="section-padding" style="background-color: var(--bg-secondary); border-top: 1px solid var(--border-color);">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 5rem;">
        <span class="section-tag">Master Curation</span>
        <h2 class="section-title">Exclusive Collections for {city}</h2>
        <p class="section-desc">Four pillars of luxury living, engineered for exceptional performance.</p>
      </div>

      <div class="card-grid-premium">
        <!-- Card 1 -->
        <div class="premium-hover-card reveal">
          <img src="images/bathroom-fittings.jpg" alt="Luxury Faucets {city}" class="premium-hover-img">
          <div class="premium-hover-content">
            <h3 style="font-family: var(--font-serif); font-size: 2rem; margin-bottom: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">Haute Couture Faucets</h3>
            <p style="font-weight: 300; font-size: 0.95rem; text-shadow: 0 1px 2px rgba(0,0,0,0.8);">Engineered in Germany and Italy. Featuring PVD coatings highly resistant to scratching and {city}'s specific water conditions.</p>
          </div>
        </div>
        <!-- Card 2 -->
        <div class="premium-hover-card reveal reveal-delay-1">
          <img src="images/sanitary-ware.jpg" alt="Smart Toilets {city}" class="premium-hover-img">
          <div class="premium-hover-content">
            <h3 style="font-family: var(--font-serif); font-size: 2rem; margin-bottom: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">Intelligent Sanitary Ware</h3>
            <p style="font-weight: 300; font-size: 0.95rem; text-shadow: 0 1px 2px rgba(0,0,0,0.8);">Next-generation smart toilets and rimless WCs offering radar-guided lids, heated seating, and UV self-cleaning technologies.</p>
          </div>
        </div>
        <!-- Card 3 -->
        <div class="premium-hover-card reveal">
          <img src="images/tiles.jpg" alt="Imported Marble Tiles {city}" class="premium-hover-img">
          <div class="premium-hover-content">
            <h3 style="font-family: var(--font-serif); font-size: 2rem; margin-bottom: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">Large-Format Tiles</h3>
            <p style="font-weight: 300; font-size: 0.95rem; text-shadow: 0 1px 2px rgba(0,0,0,0.8);">Imported directly from Italy and Spain. Massive ceramic slabs and authentic marble that eliminate grout lines for vast, seamless expanses.</p>
          </div>
        </div>
        <!-- Card 4 -->
        <div class="premium-hover-card reveal reveal-delay-1">
          <img src="images/showroom-interior.jpg" alt="Luxury Wellness Spa {city}" class="premium-hover-img">
          <div class="premium-hover-content">
            <h3 style="font-family: var(--font-serif); font-size: 2rem; margin-bottom: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">Bespoke Wellness</h3>
            <p style="font-weight: 300; font-size: 0.95rem; text-shadow: 0 1px 2px rgba(0,0,0,0.8);">Transform your {city} residence with custom dry-heat saunas, advanced steam rooms, and pressurized multi-jet spa cabins.</p>
          </div>
        </div>
      </div>
      
      <div style="text-align: center; margin-top: 4rem;" class="reveal">
        <a href="products.html" class="btn-primary magnetic-btn">Explore Full Directory</a>
      </div>
    </div>
  </section>

  <!-- Stats / Trust Banner -->
  <section class="stats-banner">
    <div class="container">
      <div class="stats-grid">
        <div class="reveal">
          <div class="stat-number">25+</div>
          <div class="stat-label">Years of Excellence</div>
        </div>
        <div class="reveal reveal-delay-1">
          <div class="stat-number">50+</div>
          <div class="stat-label">Global Brands</div>
        </div>
        <div class="reveal reveal-delay-2">
          <div class="stat-number">1000+</div>
          <div class="stat-label">Projects Supplied</div>
        </div>
        <div class="reveal reveal-delay-3">
          <div class="stat-number">100%</div>
          <div class="stat-label">Authentic Imports</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Brand Showcase -->
  <section class="section-padding" style="background-color: var(--bg-tertiary);">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <span class="section-tag">Brand Partners</span>
        <h2 class="section-title">The World's Elite, Delivered to {city}</h2>
        <p class="section-desc">We are the authorized purveyors for the most prestigious names in bathroom architecture.</p>
      </div>
      
      <div class="mega-brand-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem;">
        <a href="brand-toto.html" class="mega-brand-item">TOTO (Japan)</a>
        <a href="brand-heisenberg.html" class="mega-brand-item">HEISENBERG</a>
        <a href="brand-hansgrohe.html" class="mega-brand-item">HANSGROHE (Germany)</a>
        <a href="brand-kohler.html" class="mega-brand-item">KOHLER (USA)</a>
        <a href="brand-gessi.html" class="mega-brand-item">GESSI (Italy)</a>
      </div>
    </div>
  </section>

  <!-- Client Testimonials -->
  <section class="section-padding" style="background-color: var(--bg-secondary); border-top: 1px solid var(--border-color);">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 5rem;">
        <span class="section-tag">Social Proof</span>
        <h2 class="section-title">Trusted by {city}'s Finest</h2>
      </div>

      <div class="testimonials-grid">
        <div class="testimonial-card reveal">
          <span class="quote-icon">"</span>
          <p style="font-style: italic; margin-bottom: 2rem; font-size: 1.05rem; position: relative; z-index: 2;">"Home Studio's ability to source specific Gessi finishes for our {city} high-rise project was unmatched. Their logistics team handled the fragile marble tiles flawlessly."</p>
          <h4 style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 0.2rem;">Ar. Vikram S.</h4>
          <span style="font-size: 0.8rem; color: var(--accent); text-transform: uppercase; letter-spacing: 0.1em;">Principal Architect, {city}</span>
        </div>
        <div class="testimonial-card reveal reveal-delay-1">
          <span class="quote-icon">"</span>
          <p style="font-style: italic; margin-bottom: 2rem; font-size: 1.05rem; position: relative; z-index: 2;">"The technical consultation we received for the wellness spa installation in our luxury villa saved us weeks of guesswork. A truly premium partner."</p>
          <h4 style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 0.2rem;">Priya M.</h4>
          <span style="font-size: 0.8rem; color: var(--accent); text-transform: uppercase; letter-spacing: 0.1em;">Interior Designer, {city}</span>
        </div>
        <div class="testimonial-card reveal reveal-delay-2">
          <span class="quote-icon">"</span>
          <p style="font-style: italic; margin-bottom: 2rem; font-size: 1.05rem; position: relative; z-index: 2;">"Visiting their massive Experience Center before finalizing our {city} home was the best decision. Experiencing live smart-toilets changed our entire design approach."</p>
          <h4 style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 0.2rem;">Rahul D.</h4>
          <span style="font-size: 0.8rem; color: var(--accent); text-transform: uppercase; letter-spacing: 0.1em;">Private Homeowner, {city}</span>
        </div>
      </div>
      
      <div style="text-align: center; margin-top: 4rem;" class="reveal">
        <a href="contact.html" class="btn-secondary">Read More Reviews</a>
      </div>
    </div>
  </section>

  <!-- Interactive FAQ Accordion (SEO Density) -->
  <section class="section-padding" style="background-color: var(--bg-primary);">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <span class="section-tag">Knowledge Base</span>
        <h2 class="section-title">Project Logistics & Consultation in {city}</h2>
        <p class="section-desc">Detailed answers regarding supply, warranties, and architectural coordination.</p>
      </div>

      <div class="faq-accordion reveal">
        <!-- Q1 -->
        <div class="accordion-item">
          <button class="accordion-header">
            <span>Do you deliver luxury tiles and sanitary ware directly to {city}?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-content">
            <p>Absolutely. While our sprawling 19,500 sqft Experience Center is located in Surat, we have a robust, highly secure logistics network that facilitates seamless delivery of premium tiles, bathtubs, and fittings directly to residential and commercial construction sites anywhere in {city}. From the moment your order is curated, our project managers coordinate directly with your on-site contractors. We ensure that deliveries are phased according to your construction schedule, preventing on-site clutter and minimizing the risk of damage. All shipments to {city} are fully insured against transit damage.</p>
          </div>
        </div>
        <!-- Q2 -->
        <div class="accordion-item">
          <button class="accordion-header">
            <span>How can architects in {city} collaborate with Home Studio?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-content">
            <p>We operate a dedicated architectural support division specifically for commercial and luxury residential projects. Architects and interior designers based in {city} can share their CAD drawings and 3D renders with us. Our technical team will propose a curated selection of fixtures that match the design language, ensure plumbing compatibility, and provide detailed technical specs (including rough-in dimensions) for the contractor's reference in {city}.</p>
          </div>
        </div>
        <!-- Q3 -->
        <div class="accordion-item">
          <button class="accordion-header">
            <span>Are imported brands compatible with {city}'s water pressure standards?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-content">
            <p>Yes. This is a critical advantage of working with our technical team. We specifically curate product lines from global brands that are engineered to function optimally within Indian plumbing infrastructure. We also consult on the necessary pressure pumps, concealed cistern requirements, and filtration systems needed to ensure fixtures like rain showers, wellness spas, and smart toilets operate flawlessly in {city}.</p>
          </div>
        </div>
        <!-- Q4 -->
        <div class="accordion-item">
          <button class="accordion-header">
            <span>Do you offer installation services in {city}?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-content">
            <p>We operate primarily as a premium supply and consulting partner. While we do not deploy physical installation teams to {city}, we provide exhaustive technical support. We supply detailed installation manuals, plumbing schematics, and our engineers are available for video consultations to guide your local plumbing and masonry teams in {city} through complex installations of steam rooms, saunas, and concealed thermostatic valves.</p>
          </div>
        </div>
        <!-- Q5 -->
        <div class="accordion-item">
          <button class="accordion-header">
            <span>What is the lead time for specialized luxury fixtures to {city}?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-content">
            <p>We maintain a vast inventory of popular premium lines ready for immediate dispatch to {city}. However, for highly specialized bespoke finishes—such as brushed red gold faucets, custom-cut Italian marble, or massive freestanding bathtubs—the lead time from European manufacturing facilities typically ranges from 8 to 12 weeks. We strongly advise our {city} clients to begin material selection during the early architectural planning phase.</p>
          </div>
        </div>
        <!-- Q6 -->
        <div class="accordion-item">
          <button class="accordion-header">
            <span>Is it worth traveling from {city} to visit the Experience Center?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-content">
            <p>Unequivocally, yes. Viewing luxury fittings in a catalog cannot substitute experiencing them in person. Our massive showroom features fully pressurized, live-water displays. You can test the exact spray patterns of showers, feel the texture of imported marble, and test the functionality of smart toilets before making a significant investment for your {city} property. We regularly host architects who fly in exclusively for a guided tour.</p>
          </div>
        </div>
        <!-- Q7 -->
        <div class="accordion-item">
          <button class="accordion-header">
            <span>What warranties apply to clients purchasing from {city}?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-content">
            <p>Because we are authorized direct distributors for brands like TOTO, Hansgrohe, Gessi, and Kohler, every product we supply to {city} is backed by the manufacturer's full official warranty in India. Should you face any manufacturing defects, the official service networks for these respective brands will honor the warranty directly at your location in {city}. You do not have to rely on unauthorized third-party repairs.</p>
          </div>
        </div>
        <!-- Q8 -->
        <div class="accordion-item">
          <button class="accordion-header">
            <span>Do you cater to commercial projects like luxury hotels in {city}?</span>
            <span class="accordion-icon">+</span>
          </button>
          <div class="accordion-content">
            <p>Yes, our Commercial Projects division handles large-scale procurements for hospitality chains, luxury resorts, commercial offices, and high-end corporate towers in {city}. We offer specialized project pricing, bulk logistics management, and work closely with commercial developers to ensure timely, phased deliveries that perfectly align with massive construction schedules.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Final CTA -->
  <section class="section-padding" style="background-color: var(--bg-tertiary); text-align: center; border-top: 1px solid var(--border-color);">
    <div class="container">
      <h2 class="section-title reveal" style="font-size: clamp(2.5rem, 5vw, 4rem);">Realize Your Vision in {city}</h2>
      <p class="section-desc reveal" style="max-width: 700px; margin: 0 auto 3.5rem; font-size: 1.15rem;">
        Don't compromise on the sanctuary of your dreams. Whether you are ready to finalize your material selections or seeking expert consultation for a new build in {city}, our team is prepared to assist you.
      </p>
      <div class="reveal">
        <a href="contact.html" class="btn-primary magnetic-btn" style="margin-right: 1.5rem;">Start Your Project</a>
        <a href="showroom.html" class="btn-secondary">Visit Our Showroom</a>
      </div>
    </div>
  </section>
"""
        
        full_page = page + city_content + '\n  ' + footer_and_tail
        filepath = os.path.join(DIR, f'luxury-home-studio-{city.lower()}.html')
        
        with open(filepath, 'w') as f:
            f.write(full_page)
        
        print(f"Generated ultra-premium page for {city}. Word count est: {len(full_page.split())} words.")

print("All Premium SEO pages generated successfully.")
