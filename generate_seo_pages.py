import os
import re

CITIES = [
  'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 
  'Ahmedabad', 'Chennai', 'Kolkata', 'Pune', 
  'Jaipur', 'Surat'
]

DIR = '/Users/sidsmac/Documents/Home Studio'

files = [f for f in os.listdir(DIR) if f.endswith('.html')]

# 1. Update style.css
style_path = os.path.join(DIR, 'css', 'style.css')
with open(style_path, 'r') as f:
    style = f.read()

style = style.replace('grid-template-columns: 2fr 1fr 1fr 1.5fr;', 'grid-template-columns: 2fr 1fr 1fr 1fr 1.5fr;')
style = style.replace('grid-template-columns: 1.5fr 1fr 1fr;', 'grid-template-columns: 1.5fr 1fr 1fr 1fr;')

with open(style_path, 'w') as f:
    f.write(style)

# 2. Prepare footer HTML snippet to insert
city_links = "\n".join([f'          <li><a href="luxury-home-studio-{c.lower()}.html">{c}</a></li>' for c in CITIES])

locations_html = f"""      <div>
        <h4 class="footer-col-title">Locations</h4>
        <ul class="footer-links">
{city_links}
        </ul>
      </div>
"""

# 3. Update existing HTML files with the new footer column
for file in files:
    if file.startswith('luxury-home-studio-'):
        continue
    filepath = os.path.join(DIR, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    if '<h4 class="footer-col-title">Locations</h4>' not in content:
        insert_point = '<div>\n        <h4 class="footer-col-title">Experience Center</h4>'
        if insert_point in content:
            content = content.replace(insert_point, locations_html + '      ' + insert_point)
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"Updated footer in {file}")
        else:
            alt_insert_point = '<div>\n\t\t\t\t<h4 class="footer-col-title">Experience Center</h4>'
            if alt_insert_point in content:
                content = content.replace(alt_insert_point, locations_html + '\t\t\t' + alt_insert_point)
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"Updated footer in {file}")
            else:
                regex = r'<div[^>]*>\s*<h4[^>]*>Experience Center</h4>'
                def replace_func(match):
                    return locations_html + '      ' + match.group(0)
                content = re.sub(regex, replace_func, content)
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"Updated footer via regex in {file}")

# 4. Generate the city landing pages based on about.html
with open(os.path.join(DIR, 'about.html'), 'r') as f:
    base_template = f.read()

for city in CITIES:
    page = base_template
    
    # Replace title and meta description
    page = re.sub(r'<title>.*?</title>', f'<title>Luxury Bathroom Fittings, Tiles & Sanitary Ware in {city} | Home Studio</title>', page)
    page = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="Discover premium international brands for luxury bathroom fittings, tiles, and sanitary ware in {city} at Home Studio. Elevate your architectural projects.">', page)

    # Replace content between </header> and <footer>
    header_end = '<!-- Mobile Drawer Menu -->'
    footer_start = '<!-- Detailed Footer -->'
    
    header_end_idx = page.find(header_end)
    footer_start_idx = page.find(footer_start)
    
    if header_end_idx != -1 and footer_start_idx != -1:
        footer_and_tail = page[footer_start_idx:]
        
        mobile_drawer_end_str = '<div class="mobile-overlay"></div>'
        mobile_drawer_end_idx = page.find(mobile_drawer_end_str) + len(mobile_drawer_end_str)
        
        true_head_and_header = page[:mobile_drawer_end_idx]
        
        city_content = f"""
  <!-- Hero Section -->
  <section class="section-padding" style="margin-top: var(--header-height); background-color: var(--bg-primary);">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag">Premium Curation in {city}</span>
        <h1 style="margin-bottom: 2rem;">Elevate Your {city} Home</h1>
        <p class="section-desc" style="max-width: 700px;">
          Supplying architects, designers, and homeowners in {city} with the finest luxury bathroom fittings, exquisite tiles, and premium sanitary ware from global brands.
        </p>
      </div>
      
      <div class="editorial-img-wrap reveal" style="aspect-ratio: 21/9; margin-top: 4rem;">
        <img src="images/showroom-interior.jpg" alt="Luxury Bathroom Interior in {city}">
      </div>
    </div>
  </section>

  <!-- Luxury Offerings -->
  <section class="section-padding" style="background-color: var(--bg-secondary); border-top: 1px solid var(--border-color);">
    <div class="container">
      <div class="editorial-grid">
        <div class="editorial-col-6 reveal">
          <span class="section-tag">Our Collections</span>
          <h2 class="section-title">Curated for {city}'s Elite Spaces</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300;">
            At Home Studio, we understand the architectural demands of {city}. Whether you are designing a high-rise luxury apartment or a sprawling villa, our handpicked selections ensure perfection.
          </p>
          <ul style="margin-bottom: 2rem;">
             <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 1rem;"><span class="text-gold">✔</span> Luxury CP Fittings & Faucets</li>
             <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 1rem;"><span class="text-gold">✔</span> Smart Toilets & Sanitary Ware</li>
             <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 1rem;"><span class="text-gold">✔</span> Imported Ceramic & Marble Tiles</li>
             <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 1rem;"><span class="text-gold">✔</span> Wellness Spas, Steam & Saunas</li>
          </ul>
          <a href="products.html" class="btn-secondary">Explore Products</a>
        </div>
        <div class="editorial-col-6 reveal reveal-delay-1">
          <div class="card-img-wrap" style="border-radius: var(--radius-lg);">
            <img src="images/bathroom-fittings.jpg" alt="Premium CP Fittings" class="card-img">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Brands -->
  <section class="section-padding" style="background-color: var(--bg-tertiary);">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <span class="section-tag">Global Partners</span>
        <h2 class="section-title">International Brands in {city}</h2>
        <p class="section-desc">Experience the world's finest craftsmanship delivered to your doorstep in {city}.</p>
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

  <!-- CTA -->
  <section class="section-padding" style="background-color: var(--bg-primary); text-align: center; border-top: 1px solid var(--border-color);">
    <div class="container">
      <h2 class="section-title reveal">Ready to transform your {city} project?</h2>
      <p class="section-desc reveal" style="max-width: 600px; margin: 0 auto 3rem;">
        Visit our main Experience Center in Surat or contact our bespoke architectural consultation team for exclusive deliveries and support in {city}.
      </p>
      <div class="reveal">
        <a href="showroom.html" class="btn-primary magnetic-btn" style="margin-right: 1rem;">Visit Showroom</a>
        <a href="contact.html" class="btn-secondary">Contact Us</a>
      </div>
    </div>
  </section>
"""
        
        page = true_head_and_header + city_content + '\n  ' + footer_and_tail
        
        with open(os.path.join(DIR, f'luxury-home-studio-{city.lower()}.html'), 'w') as f:
            f.write(page)
        print(f"Created luxury-home-studio-{city.lower()}.html")
