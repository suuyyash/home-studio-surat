const fs = require('fs');
const path = require('path');

const CITIES = [
  'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 
  'Ahmedabad', 'Chennai', 'Kolkata', 'Pune', 
  'Jaipur', 'Surat'
];

const DIR = '/Users/sidsmac/Documents/Home Studio';

const files = fs.readdirSync(DIR).filter(f => f.endsWith('.html'));

// 1. Update style.css
let stylePath = path.join(DIR, 'css', 'style.css');
let style = fs.readFileSync(stylePath, 'utf8');
style = style.replace('grid-template-columns: 2fr 1fr 1fr 1.5fr;', 'grid-template-columns: 2fr 1fr 1fr 1fr 1.5fr;');
style = style.replace('grid-template-columns: 1.5fr 1fr 1fr;', 'grid-template-columns: 1.5fr 1fr 1fr 1fr;');
fs.writeFileSync(stylePath, style);

// 2. Prepare footer HTML snippet to insert
const locationsHTML = `
      <div>
        <h4 class="footer-col-title">Locations</h4>
        <ul class="footer-links">
${CITIES.map(c => `          <li><a href="luxury-home-studio-${c.toLowerCase()}.html">${c}</a></li>`).join('\n')}
        </ul>
      </div>
`;

// 3. Update existing HTML files with the new footer column
for (const file of files) {
  let content = fs.readFileSync(path.join(DIR, file), 'utf8');
  
  // Check if it already has Locations
  if (!content.includes('<h4 class="footer-col-title">Locations</h4>')) {
    // Insert before "Experience Center"
    const insertPoint = '<div>\n        <h4 class="footer-col-title">Experience Center</h4>';
    if (content.includes(insertPoint)) {
      content = content.replace(insertPoint, locationsHTML + '      ' + insertPoint);
      fs.writeFileSync(path.join(DIR, file), content);
      console.log(`Updated footer in ${file}`);
    } else {
        const altInsertPoint = '<div>\n\t\t\t\t<h4 class="footer-col-title">Experience Center</h4>';
        if (content.includes(altInsertPoint)) {
            content = content.replace(altInsertPoint, locationsHTML + '\t\t\t' + altInsertPoint);
            fs.writeFileSync(path.join(DIR, file), content);
            console.log(`Updated footer in ${file}`);
        } else {
             // Let's try matching with regex
             const regex = /<div[^>]*>\s*<h4[^>]*>Experience Center<\/h4>/g;
             content = content.replace(regex, match => locationsHTML + '      ' + match);
             fs.writeFileSync(path.join(DIR, file), content);
             console.log(`Updated footer via regex in ${file}`);
        }
    }
  }
}

// 4. Generate the city landing pages based on about.html
const baseTemplate = fs.readFileSync(path.join(DIR, 'about.html'), 'utf8');

for (const city of CITIES) {
  let page = baseTemplate;
  
  // Replace title and meta description
  page = page.replace(
    /<title>.*?<\/title>/,
    `<title>Luxury Bathroom Fittings, Tiles & Sanitary Ware in ${city} | Home Studio</title>`
  );
  page = page.replace(
    /<meta name="description" content=".*?">/,
    `<meta name="description" content="Discover premium international brands for luxury bathroom fittings, tiles, and sanitary ware in ${city} at Home Studio. Elevate your architectural projects.">`
  );

  // Replace content between </header> and <footer>
  const headerEnd = '<!-- Mobile Drawer Menu -->';
  const footerStart = '<!-- Detailed Footer -->';
  
  const headerEndIdx = page.indexOf(headerEnd);
  const footerStartIdx = page.indexOf(footerStart);
  
  if (headerEndIdx !== -1 && footerStartIdx !== -1) {
    const headAndHeader = page.substring(0, headerEndIdx);
    const footerAndTail = page.substring(footerStartIdx);
    
    // Extract the mobile drawer overlay as well (it's between header and main content)
    // Actually, mobile drawer starts at "<!-- Mobile Drawer Menu -->" and ends after "<div class="mobile-overlay"></div>"
    const mobileDrawerEndStr = '<div class="mobile-overlay"></div>';
    const mobileDrawerEndIdx = page.indexOf(mobileDrawerEndStr) + mobileDrawerEndStr.length;
    
    const trueHeadAndHeader = page.substring(0, mobileDrawerEndIdx);
    
    const cityContent = `
  <!-- Hero Section -->
  <section class="section-padding" style="margin-top: var(--header-height); background-color: var(--bg-primary);">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag">Premium Curation in ${city}</span>
        <h1 style="margin-bottom: 2rem;">Elevate Your ${city} Home</h1>
        <p class="section-desc" style="max-width: 700px;">
          Supplying architects, designers, and homeowners in ${city} with the finest luxury bathroom fittings, exquisite tiles, and premium sanitary ware from global brands.
        </p>
      </div>
      
      <div class="editorial-img-wrap reveal" style="aspect-ratio: 21/9; margin-top: 4rem;">
        <img src="images/showroom-interior.jpg" alt="Luxury Bathroom Interior in ${city}">
      </div>
    </div>
  </section>

  <!-- Luxury Offerings -->
  <section class="section-padding" style="background-color: var(--bg-secondary); border-top: 1px solid var(--border-color);">
    <div class="container">
      <div class="editorial-grid">
        <div class="editorial-col-6 reveal">
          <span class="section-tag">Our Collections</span>
          <h2 class="section-title">Curated for ${city}'s Elite Spaces</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300;">
            At Home Studio, we understand the architectural demands of ${city}. Whether you are designing a high-rise luxury apartment or a sprawling villa, our handpicked selections ensure perfection.
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
        <h2 class="section-title">International Brands in ${city}</h2>
        <p class="section-desc">Experience the world's finest craftsmanship delivered to your doorstep in ${city}.</p>
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
      <h2 class="section-title reveal">Ready to transform your ${city} project?</h2>
      <p class="section-desc reveal" style="max-width: 600px; margin: 0 auto 3rem;">
        Visit our main Experience Center in Surat or contact our bespoke architectural consultation team for exclusive deliveries and support in ${city}.
      </p>
      <div class="reveal">
        <a href="showroom.html" class="btn-primary magnetic-btn" style="margin-right: 1rem;">Visit Showroom</a>
        <a href="contact.html" class="btn-secondary">Contact Us</a>
      </div>
    </div>
  </section>
`;
    
    page = trueHeadAndHeader + cityContent + '\n  ' + footerAndTail;
    
    fs.writeFileSync(path.join(DIR, `luxury-home-studio-${city.toLowerCase()}.html`), page);
    console.log(`Created luxury-home-studio-${city.toLowerCase()}.html`);
  }
}
