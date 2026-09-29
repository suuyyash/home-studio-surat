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
    true_head_and_header = base_template[:mobile_drawer_end_idx]

    for city in CITIES:
        page = true_head_and_header
        
        # Replace title and meta description
        page = re.sub(r'<title>.*?</title>', f'<title>Ultimate Luxury Bathroom Fittings, Tiles & Sanitary Ware in {city} | Home Studio</title>', page)
        page = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="Transform your {city} home with Home Studio, the premier destination for luxury bathroom fittings, smart sanitary ware, imported tiles, and elite wellness spas. Trusted by top architects in {city}.">', page)

        city_content = f"""
  <!-- Hero Section -->
  <section class="section-padding" style="margin-top: var(--header-height); background-color: var(--bg-primary);">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag">Unrivaled Luxury in {city}</span>
        <h1 style="margin-bottom: 2rem;">The Pinnacle of Luxury Bathroom Architecture in {city}</h1>
        <p class="section-desc" style="max-width: 800px; margin-bottom: 1.5rem;">
          Welcome to the definitive destination for luxury bathroom fittings, imported tiles, and high-end sanitary ware tailored for the most prestigious residential and commercial projects in {city}. At Home Studio, we understand that designing a home in {city} is an exercise in creating a personal sanctuary, an oasis that reflects your sophisticated lifestyle and appreciation for world-class design. Our unparalleled curation of global brands guarantees that whether you are developing a luxury high-rise apartment overlooking the skyline or constructing an expansive standalone villa, your spaces will exude an uncompromising standard of elegance and innovation.
        </p>
        <p class="section-desc" style="max-width: 800px;">
          Architects, interior designers, and discerning homeowners in {city} constantly seek materials that not only meet stringent aesthetic requirements but also deliver robust longevity and cutting-edge functionality. By bridging the gap between international design hubs and {city}, we provide direct access to the world’s most sought-after collections, ensuring your architectural vision is executed with flawless precision and an extraordinary attention to detail.
        </p>
      </div>
      
      <div class="editorial-img-wrap reveal" style="aspect-ratio: 21/9; margin-top: 4rem;">
        <img src="images/showroom-interior.jpg" alt="Luxury Bathroom Interior Design {city}">
      </div>
    </div>
  </section>

  <!-- Local Context Section -->
  <section class="section-padding" style="background-color: var(--bg-secondary); border-top: 1px solid var(--border-color);">
    <div class="container">
      <div class="editorial-grid">
        <div class="editorial-col-6 reveal">
          <span class="section-tag">Architectural Evolution</span>
          <h2 class="section-title">Redefining {city}'s Architectural Landscape</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300;">
            The real estate and architectural landscape in {city} is undergoing a dramatic renaissance. There is a palpable shift toward integrating wellness, smart technology, and minimalist luxury into everyday living spaces. Home Studio is at the forefront of this evolution in {city}, offering bespoke solutions that cater precisely to this sophisticated demographic. From sleek, contemporary penthouses that demand minimalist matte-black finishes, to grand heritage-inspired estates requiring classic gold and brushed nickel fixtures, our catalog is meticulously curated to fulfill the diverse stylistic demands of {city}'s elite property owners.
          </p>
          <p style="margin-bottom: 1.5rem; font-weight: 300;">
            We don't merely supply products; we collaborate with {city}'s top-tier design professionals to engineer spaces of tranquility. The high humidity, varying water pressures, and specific climatic conditions of {city} require plumbing and sanitary ware that is as durable as it is beautiful. Our technical experts possess an intimate understanding of these regional nuances, ensuring that every faucet, shower system, and wellness spa we recommend will perform flawlessly year after year in the {city} environment.
          </p>
          <p style="font-weight: 300;">
            This localized expertise, combined with our vast global inventory, makes Home Studio the undisputed partner of choice for luxury developers, hospitality chains, and private homeowners throughout {city}. When you choose us, you are investing in a legacy of quality that will dramatically elevate the value and comfort of your property.
          </p>
        </div>
        <div class="editorial-col-6 reveal reveal-delay-1">
          <div class="card-img-wrap" style="border-radius: var(--radius-lg); height: 100%;">
            <img src="images/bathroom-fittings.jpg" alt="Premium CP Fittings in {city}" class="card-img" style="height: 100%;">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Deep Dive Product Categories -->
  <section class="section-padding" style="background-color: var(--bg-primary);">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 5rem;">
        <span class="section-tag">Our Master Curation</span>
        <h2 class="section-title">Uncompromising Collections Available in {city}</h2>
        <p class="section-desc">Delve into our four core pillars of luxury living, each selected for its uncompromising quality, award-winning design, and technological superiority.</p>
      </div>

      <div class="editorial-grid" style="margin-bottom: 5rem;">
        <div class="editorial-col-5 reveal">
          <h3 style="font-size: 2rem; margin-bottom: 1rem;">1. Haute Couture CP Fittings & Faucets</h3>
          <p style="font-weight: 300; margin-bottom: 1rem;">
            The jewelry of any bathroom, our luxury CP (Chrome Plated) fittings and faucets represent the zenith of metallurgical artistry and fluid dynamics. For our clients in {city}, we offer an expansive range of finishes including brushed bronze, polished gold, matte black, and classic chrome. 
          </p>
          <p style="font-weight: 300;">
            These fixtures are not mass-produced; they are engineered by master craftsmen in Germany, Italy, and Japan. They feature advanced ceramic cartridges for drip-free operation, specialized aerators to optimize water flow while minimizing waste, and PVD (Physical Vapor Deposition) coatings that are highly resistant to scratching, tarnishing, and the specific water conditions found in {city}. Whether you desire a sleek, angular cascade faucet for a modern powder room or an ornate, cross-handle mixer for a classic master bath, our collection guarantees a tactile and visual experience that is truly second to none.
          </p>
        </div>
        <div class="editorial-col-7 reveal reveal-delay-1">
          <div class="editorial-img-wrap" style="aspect-ratio: 16/9;">
            <img src="images/bathroom-fittings.jpg" alt="Haute Couture Faucets in {city}">
          </div>
        </div>
      </div>

      <div class="editorial-grid" style="margin-bottom: 5rem; direction: rtl;">
        <div class="editorial-col-5 reveal" style="direction: ltr;">
          <h3 style="font-size: 2rem; margin-bottom: 1rem;">2. Intelligent Sanitary Ware & Smart Toilets</h3>
          <p style="font-weight: 300; margin-bottom: 1rem;">
            The modern bathroom in {city} is incomplete without the integration of intelligent sanitary technology. We proudly present the latest generation of smart toilets, washlets, and automated bidets that redefine personal hygiene and comfort.
          </p>
          <p style="font-weight: 300;">
            Featuring radar-guided auto-open/close lids, personalized warm water cleansing, heated seating, automatic deodorizers, and self-cleaning UV technologies, these fixtures are marvels of modern engineering. Furthermore, our collection of luxury bathtubs—ranging from freestanding solid surface soaking tubs to advanced hydrotherapy jacuzzis—transforms routine bathing into an immersive, spa-like ritual. For {city} homes looking to push the boundaries of design, our rimless wall-hung WCs offer a seamless, floating aesthetic that makes spaces appear larger while dramatically simplifying cleaning and maintenance.
          </p>
        </div>
        <div class="editorial-col-7 reveal reveal-delay-1" style="direction: ltr;">
          <div class="editorial-img-wrap" style="aspect-ratio: 16/9;">
            <img src="images/sanitary-ware.jpg" alt="Smart Sanitary Ware in {city}">
          </div>
        </div>
      </div>

      <div class="editorial-grid" style="margin-bottom: 5rem;">
        <div class="editorial-col-5 reveal">
          <h3 style="font-size: 2rem; margin-bottom: 1rem;">3. Imported Large-Format Ceramic & Marble Tiles</h3>
          <p style="font-weight: 300; margin-bottom: 1rem;">
            The foundation of any breathtaking architectural space lies in its surfaces. For our discerning {city} clientele, we import an elite selection of large-format ceramic slabs, vitrified porcelain, and authentic marble tiles directly from premier quarries and manufacturing houses in Italy and Spain.
          </p>
          <p style="font-weight: 300;">
            Large-format slabs minimize grout lines, creating vast, uninterrupted expanses that simulate the grandeur of solid stone blocks. Our collection includes hyper-realistic natural stone veining, striking onyx patterns, minimalist concretes, and warm timber-look ceramics. These tiles are engineered for exceptional durability, offering high resistance to impact, staining, and moisture. This makes them ideal not just for luxury bathroom walls and floors in {city}, but also for expansive living room floors, striking kitchen backsplashes, and dramatic exterior building facades.
          </p>
        </div>
        <div class="editorial-col-7 reveal reveal-delay-1">
          <div class="editorial-img-wrap" style="aspect-ratio: 16/9;">
            <img src="images/tiles.jpg" alt="Imported Marble Tiles in {city}">
          </div>
        </div>
      </div>

      <div class="editorial-grid" style="direction: rtl;">
        <div class="editorial-col-5 reveal" style="direction: ltr;">
          <h3 style="font-size: 2rem; margin-bottom: 1rem;">4. Bespoke Wellness: Steam, Sauna & Spa</h3>
          <p style="font-weight: 300; margin-bottom: 1rem;">
            Recognizing the intense, fast-paced lifestyle of {city}, we believe your home should offer a dedicated sanctuary for physical and mental restoration. Our bespoke wellness solutions bring the amenities of a five-star luxury resort directly into your private residence.
          </p>
          <p style="font-weight: 300;">
            We design, supply, and consult on the installation of fully operational dry-heat Finnish sauna cabins crafted from premium hemlock or cedar woods, advanced steam room generators with integrated aromatherapy and chromotherapy lighting, and pressurized multi-jet shower cabins. These systems are highly customizable to fit the specific spatial dimensions of your {city} property. By integrating these wellness features, you create an environment that actively promotes relaxation, detoxification, and cardiovascular health, elevating your standard of living to unprecedented heights.
          </p>
        </div>
        <div class="editorial-col-7 reveal reveal-delay-1" style="direction: ltr;">
          <div class="editorial-img-wrap" style="aspect-ratio: 16/9;">
            <img src="images/bathroom-fittings.jpg" alt="Luxury Wellness Spa in {city}">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Comparison Matrix -->
  <section class="section-padding" style="background-color: var(--bg-tertiary); border-top: 1px solid var(--border-color);">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <span class="section-tag">The Home Studio Advantage</span>
        <h2 class="section-title">Why {city}'s Architects Choose Us Over Local Retailers</h2>
        <p class="section-desc">A side-by-side comparison illustrating our commitment to absolute excellence in the luxury segment.</p>
      </div>

      <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; text-align: left;">
          <thead>
            <tr style="border-bottom: 2px solid var(--accent);">
              <th style="padding: 1.5rem; font-family: var(--font-serif); font-size: 1.5rem; width: 25%;">Feature</th>
              <th style="padding: 1.5rem; font-family: var(--font-serif); font-size: 1.5rem; color: var(--accent); width: 37.5%;">Home Studio Luxury Curation</th>
              <th style="padding: 1.5rem; font-family: var(--font-serif); font-size: 1.5rem; color: var(--text-secondary); width: 37.5%;">Typical {city} Retailers</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid var(--border-color-light);">
              <td style="padding: 1.5rem; font-weight: 600;">Brand Authenticity</td>
              <td style="padding: 1.5rem; font-weight: 300;">100% genuine imports directly sourced from global manufacturers (Germany, Italy, Japan) with full international warranties.</td>
              <td style="padding: 1.5rem; font-weight: 300; color: var(--text-secondary);">Often rely on grey-market imports, mixed inventories, or replicas lacking official warranty support.</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color-light);">
              <td style="padding: 1.5rem; font-weight: 600;">Architectural Consultation</td>
              <td style="padding: 1.5rem; font-weight: 300;">Dedicated design directors and technical engineers to assist with plumbing schematics, CAD layouts, and load calculations for your {city} project.</td>
              <td style="padding: 1.5rem; font-weight: 300; color: var(--text-secondary);">Primarily transactional sales staff lacking technical plumbing and structural engineering knowledge.</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color-light);">
              <td style="padding: 1.5rem; font-weight: 600;">Experiential Showroom</td>
              <td style="padding: 1.5rem; font-weight: 300;">Access to our massive 19,500 sqft Experience Center featuring fully pressurized, live-water demonstration zones for showers and smart toilets.</td>
              <td style="padding: 1.5rem; font-weight: 300; color: var(--text-secondary);">Static, unplumbed displays that require you to guess how a product will actually perform.</td>
            </tr>
            <tr style="border-bottom: 1px solid var(--border-color-light);">
              <td style="padding: 1.5rem; font-weight: 600;">Logistics & Supply</td>
              <td style="padding: 1.5rem; font-weight: 300;">Secure, insured, and deeply managed logistics ensuring safe delivery of fragile tiles and complex machinery to any site in {city}.</td>
              <td style="padding: 1.5rem; font-weight: 300; color: var(--text-secondary);">Outsourced, unreliable local transport leading to high breakage rates and delayed project timelines.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- Brand Deep Dive -->
  <section class="section-padding" style="background-color: var(--bg-secondary);">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag">Global Partners</span>
        <h2 class="section-title">The World's Elite Brands, Now in {city}</h2>
        <p class="section-desc" style="max-width: 800px;">
          We are proud to serve as the premier purveyor for the most prestigious names in luxury bath and surface design. For our {city} clientele, this means unparalleled access to exclusive collections.
        </p>
      </div>

      <div class="values-grid">
        <div class="value-box reveal">
          <h3 class="value-title text-gold">TOTO (Japan)</h3>
          <p style="font-size: 0.95rem; font-weight: 300;">
            The undisputed global leader in intelligent bathroom technology. TOTO brings Japanese precision to {city} with their legendary Neorest smart toilets, featuring tornado flush systems, electrolyzed water cleaning (Ewater+), and CeFiONtect glaze. Perfect for homes that prioritize absolute hygiene and futuristic automation.
          </p>
        </div>
        <div class="value-box reveal reveal-delay-1">
          <h3 class="value-title text-gold">Hansgrohe (Germany)</h3>
          <p style="font-size: 0.95rem; font-weight: 300;">
            Synonymous with German engineering and environmental sustainability. Hansgrohe and their luxury sub-brand, AXOR, provide {city} architects with flawlessly crafted shower systems and faucets. Their EcoSmart technology reduces water consumption by up to 60% without compromising on the luxurious shower experience.
          </p>
        </div>
        <div class="value-box reveal reveal-delay-2">
          <h3 class="value-title text-gold">Gessi (Italy)</h3>
          <p style="font-size: 0.95rem; font-weight: 300;">
            Italian passion and high-fashion design injected into bathroom architecture. Gessi transforms brass into breathtaking sculptures. Known for their Private Wellness programs and striking silhouettes, Gessi fixtures are the ultimate statement piece for any avant-garde luxury villa in {city}.
          </p>
        </div>
        <div class="value-box reveal reveal-delay-3">
          <h3 class="value-title text-gold">Kohler (USA)</h3>
          <p style="font-size: 0.95rem; font-weight: 300;">
            A titan of American industrial design, offering a vast, versatile portfolio that seamlessly blends classic elegance with modern boldness. Kohler brings incredibly durable cast-iron bathtubs, artist-edition artistically painted sinks, and robust, powerful flushing technologies to the {city} market.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Logistics and Supply -->
  <section class="section-padding" style="background-color: var(--bg-primary);">
    <div class="container">
      <div class="editorial-grid">
        <div class="editorial-col-7 reveal">
          <span class="section-tag">Project Execution</span>
          <h2 class="section-title">Flawless Logistics & Delivery to {city}</h2>
          <p style="margin-bottom: 1.5rem; font-weight: 300;">
            Supplying materials for a luxury real estate project is a complex logistical challenge. Delicate large-format marble tiles, heavy cast-iron bathtubs, and sensitive electronic smart toilets require meticulous handling. Our centralized warehousing and dedicated logistics framework are specifically designed to manage secure, timely deliveries to any location within {city}.
          </p>
          <p style="margin-bottom: 1.5rem; font-weight: 300;">
            From the moment your order is curated at our Surat hub, our project managers coordinate directly with your on-site contractors in {city}. We ensure that deliveries are phased according to your construction schedule, preventing on-site clutter and minimizing the risk of damage during the build. Every item is heavily insured and packaged using industry-leading protective materials. 
          </p>
          <p style="font-weight: 300;">
            Furthermore, our technical support extends beyond delivery. We provide comprehensive installation manuals, plumbing schematics, and offer video-consultation support to your local plumbers in {city} to guarantee that the sophisticated internal mechanisms of imported shower valves and concealed cisterns are installed with absolute perfection.
          </p>
        </div>
        <div class="editorial-col-5 reveal reveal-delay-1">
          <div class="editorial-img-wrap" style="aspect-ratio: 4/5;">
            <img src="images/showroom-interior.jpg" alt="Logistics and Supply to {city}">
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Comprehensive FAQ Section -->
  <section class="section-padding" style="background-color: var(--bg-secondary); border-top: 1px solid var(--border-color);">
    <div class="container">
      <div class="section-header reveal" style="text-align: center; margin: 0 auto 4rem;">
        <span class="section-tag">Knowledge Base</span>
        <h2 class="section-title">Frequently Asked Questions: {city}</h2>
        <p class="section-desc">Essential information for our clients planning luxury builds in {city}.</p>
      </div>

      <div style="max-width: 900px; margin: 0 auto;">
        
        <div style="margin-bottom: 2.5rem; border-bottom: 1px solid var(--border-color-light); padding-bottom: 1.5rem;" class="reveal">
          <h4 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 1rem; color: var(--accent);">Do you deliver luxury tiles and sanitary ware directly to {city}?</h4>
          <p style="font-weight: 300; line-height: 1.6;">Absolutely. While our sprawling 19,500 sqft Experience Center is located in Surat, we have a robust, highly secure logistics network that facilitates seamless delivery of premium tiles, bathtubs, and fittings directly to residential and commercial construction sites anywhere in {city}. All shipments are fully insured against transit damage.</p>
        </div>

        <div style="margin-bottom: 2.5rem; border-bottom: 1px solid var(--border-color-light); padding-bottom: 1.5rem;" class="reveal">
          <h4 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 1rem; color: var(--accent);">How can architects in {city} collaborate with Home Studio?</h4>
          <p style="font-weight: 300; line-height: 1.6;">We have a dedicated architectural support division. Architects and interior designers based in {city} can share their CAD drawings and 3D renders with us. Our technical team will then propose a curated selection of fixtures that match the design language, ensure plumbing compatibility, and provide detailed technical specs for the contractor's reference.</p>
        </div>

        <div style="margin-bottom: 2.5rem; border-bottom: 1px solid var(--border-color-light); padding-bottom: 1.5rem;" class="reveal">
          <h4 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 1rem; color: var(--accent);">Are the imported brands you sell compatible with {city}'s water pressure and plumbing standards?</h4>
          <p style="font-weight: 300; line-height: 1.6;">Yes. This is a critical advantage of working with Home Studio. We specifically curate product lines from global brands that are engineered to function optimally within Indian plumbing infrastructure. We also consult on the necessary pressure pumps and filtration systems required to ensure fixtures like rain showers and smart toilets operate flawlessly in {city}.</p>
        </div>

        <div style="margin-bottom: 2.5rem; border-bottom: 1px solid var(--border-color-light); padding-bottom: 1.5rem;" class="reveal">
          <h4 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 1rem; color: var(--accent);">Do you offer installation services in {city}?</h4>
          <p style="font-weight: 300; line-height: 1.6;">We operate primarily as a premium supply and consulting partner. While we do not deploy physical installation teams to {city}, we provide exhaustive technical support. We supply detailed installation manuals, CAD schematics, and our engineers are available for video consultations to guide your local plumbing and masonry teams in {city} through complex installations.</p>
        </div>

        <div style="margin-bottom: 2.5rem; border-bottom: 1px solid var(--border-color-light); padding-bottom: 1.5rem;" class="reveal">
          <h4 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 1rem; color: var(--accent);">What is the typical lead time for importing specialized luxury fixtures to {city}?</h4>
          <p style="font-weight: 300; line-height: 1.6;">We maintain a vast inventory of popular premium lines ready for immediate dispatch to {city}. However, for highly specialized bespoke finishes (like brushed red gold or custom-cut marble), the lead time from European manufacturing facilities typically ranges from 8 to 12 weeks. We strongly advise {city} clients to begin material selection during the early architectural planning phase.</p>
        </div>

        <div style="margin-bottom: 2.5rem; border-bottom: 1px solid var(--border-color-light); padding-bottom: 1.5rem;" class="reveal">
          <h4 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 1rem; color: var(--accent);">Is it worth traveling from {city} to visit the Surat Experience Center?</h4>
          <p style="font-weight: 300; line-height: 1.6;">Unequivocally, yes. Viewing luxury fittings in a catalog cannot substitute experiencing them in person. Our Surat showroom features fully pressurized, live-water displays where you can test the exact spray patterns of showers and the functionality of smart toilets before making a significant investment for your {city} property. We regularly host clients and architects who fly in exclusively for a guided tour.</p>
        </div>

        <div style="margin-bottom: 2.5rem; border-bottom: 1px solid var(--border-color-light); padding-bottom: 1.5rem;" class="reveal">
          <h4 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 1rem; color: var(--accent);">What warranties apply to clients purchasing from {city}?</h4>
          <p style="font-weight: 300; line-height: 1.6;">Because we are authorized distributors for brands like TOTO, Hansgrohe, and Gessi, every product we supply to {city} is backed by the manufacturer's full official warranty in India. Should you face any manufacturing defects, the official service networks for these brands will honor the warranty directly at your location.</p>
        </div>

        <div style="margin-bottom: 2.5rem; padding-bottom: 1.5rem;" class="reveal">
          <h4 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 1rem; color: var(--accent);">Do you cater to commercial projects like luxury hotels in {city}?</h4>
          <p style="font-weight: 300; line-height: 1.6;">Yes, our Commercial Projects division handles large-scale procurements for hospitality chains, luxury resorts, and high-end corporate towers in {city}. We offer specialized project pricing, bulk logistics management, and work closely with commercial developers to ensure timely, phased deliveries that align with massive construction schedules.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Final CTA -->
  <section class="section-padding" style="background-color: var(--bg-primary); text-align: center; border-top: 1px solid var(--border-color);">
    <div class="container">
      <h2 class="section-title reveal" style="font-size: clamp(2.5rem, 5vw, 4rem);">Realize Your Architectural Vision in {city}</h2>
      <p class="section-desc reveal" style="max-width: 700px; margin: 0 auto 3.5rem; font-size: 1.15rem;">
        Don't compromise on the sanctuary of your dreams. Whether you are ready to finalize your material selections or seeking expert consultation for a new build in {city}, our team is prepared to assist you with unparalleled expertise.
      </p>
      <div class="reveal">
        <a href="showroom.html" class="btn-primary magnetic-btn" style="margin-right: 1.5rem;">Plan Your Showroom Visit</a>
        <a href="contact.html" class="btn-secondary">Request a Virtual Consultation</a>
      </div>
    </div>
  </section>
"""
        
        full_page = page + city_content + '\n  ' + footer_and_tail
        filepath = os.path.join(DIR, f'luxury-home-studio-{city.lower()}.html')
        
        with open(filepath, 'w') as f:
            f.write(full_page)
        
        print(f"Generated 2000+ word page for {city}. Word count est: {len(full_page.split())} words.")

print("All SEO pages generated successfully.")
