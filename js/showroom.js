document.addEventListener('DOMContentLoaded', () => {
  initShowroomHotspots();
  initShowroomTour();
});

/* --- Showroom Hotspots Interactive Panel --- */
function initShowroomHotspots() {
  const hotspots = document.querySelectorAll('.hotspot');
  const detailsPanel = document.getElementById('hotspot-details');
  const detailTitle = document.getElementById('detail-title');
  const detailDesc = document.getElementById('detail-desc');
  const detailBrand = document.getElementById('detail-brand');
  const detailCategory = document.getElementById('detail-category');
  
  // Hotspot details data map
  const hotspotData = {
    1: {
      title: "ToTo Neorest Smart Suite",
      brand: "ToTo Japan",
      category: "Sanitary Ware",
      description: "A live demonstration of the world's most advanced smart toilet systems. Experience integrated bidet features, auto open/close, heated seating, custom warm-air drying, and advanced Actilight sanitizing technology."
    },
    2: {
      title: "Heisenberg Thermostatic Rain Shower Zone",
      brand: "Heisenberg",
      category: "Bathroom Fittings & Faucets",
      description: "Experience a live demonstration of smart thermostatic shower valves. The zone displays overhead rain showers with cascading waterfalls, atomizing body mists, and custom pressure selectors with instant temperature response."
    },
    3: {
      title: "Bespoke Wellness Spa & Sauna Cabin",
      brand: "Home Studio Import Curation",
      category: "Sauna, Steam & Spas",
      description: "An authentic glass-fronted sauna cabin displaying Canadian Hemlock timber construction, integrated chromotherapy lighting, precise dry-heat controls, and steam generators representing the pinnacle of personal wellness."
    },
    4: {
      title: "Luxury Faucet & CP Fitting Gallary",
      brand: "Hansgrohe / Axor / Gessi",
      category: "Faucets & Bath Accessories",
      description: "A curated display table featuring designer faucets in exotic finishes. Browse brushed copper, matte gold, anthracite, and gunmetal finishes, alongside high-end ceramic countertop washbasins from Europe's elite design houses."
    }
  };

  hotspots.forEach(hotspot => {
    hotspot.addEventListener('click', () => {
      const id = hotspot.dataset.id;
      const data = hotspotData[id];
      
      if (!data) return;
      
      // Deactivate other hotspots
      hotspots.forEach(h => h.classList.remove('active'));
      hotspot.classList.add('active');
      
      // Update details content
      detailTitle.textContent = data.title;
      detailBrand.textContent = data.brand;
      detailCategory.textContent = data.category;
      detailDesc.textContent = data.description;
      
      // Highlight details panel visually
      detailsPanel.classList.add('highlight');
      setTimeout(() => {
        detailsPanel.classList.remove('highlight');
      }, 500);
    });
  });
  
  // Set initial hotspot (Hotspot 1) active on load
  if (hotspots.length > 0) {
    hotspots[0].click();
  }
}

/* --- Guided Tour Step-by-Step Navigation --- */
function initShowroomTour() {
  const steps = document.querySelectorAll('.tour-step-btn');
  const displayTitle = document.getElementById('tour-display-title');
  const displayDesc = document.getElementById('tour-display-desc');
  const displayImage = document.getElementById('tour-display-image');
  
  // Tour steps content database
  const tourData = {
    1: {
      title: "1. The Grand Entrance & Curated Gallery",
      description: "Welcome to our 19,500 sqft showroom on Udhana-Magdalla Road. Your tour begins in the entry gallery, displaying a hand-selected collection of premium ceramic tiles, imported artifacts, and artistic washbasins sourced from Italy and Spain.",
      image: "images/showroom-interior.jpg"
    },
    2: {
      title: "2. The Live Shower Demonstration Zone",
      description: "Step into our wet area simulation. Here, we demonstrate fully pressurized rain showers, multi-flow heads, and smart digital thermostatic controllers. You can feel the water pressure, see the spray patterns, and witness smart bathroom technologies in action.",
      image: "images/bathroom-fittings.jpg"
    },
    3: {
      title: "3. Sanitary Ware & ToTo Luxury Center",
      description: "Move next to our dedicated sanitaryware wing, highlighting our partnership with ToTo. Experience the Neorest smart suite alongside a sprawling array of premium matte-finish bathtubs, minimalist washbasins, and space-saving wall-hung WCs.",
      image: "images/sanitary-ware.jpg"
    },
    4: {
      title: "4. Architectural Tile & Surfaces Library",
      description: "Browse the tile library containing large-format porcelain slabs, book-matched marble textures, designer mosaic tiles, and high-durability outdoor pavings. Touch the textures, evaluate the finishes under color-accurate architectural lighting.",
      image: "images/tiles.jpg"
    },
    5: {
      title: "5. Wellness Sanctuary: Steam, Sauna & Spa",
      description: "Conclude your tour in the Wellness Sanctuary. Explore our working models of Jacuzzi tubs, steam generators, and custom dry-sauna cabins. Learn how our engineering team integrates custom installations into your luxury home.",
      image: "images/windows.jpg" // Using window as landscape/spa visualization asset
    }
  };

  steps.forEach(step => {
    step.addEventListener('click', () => {
      const stepNum = step.dataset.step;
      const data = tourData[stepNum];
      
      if (!data) return;
      
      // Update step active classes
      steps.forEach(s => s.classList.remove('active'));
      step.classList.add('active');
      
      // Fade out transition animation
      const textContainer = document.querySelector('.tour-visual-text');
      const imgContainer = document.querySelector('.tour-visual-img');
      
      textContainer.style.opacity = '0';
      textContainer.style.transform = 'translateY(15px)';
      imgContainer.style.opacity = '0';
      imgContainer.style.transform = 'scale(0.98)';
      
      setTimeout(() => {
        displayTitle.textContent = data.title;
        displayDesc.textContent = data.description;
        displayImage.src = data.image;
        
        textContainer.style.opacity = '1';
        textContainer.style.transform = 'translateY(0)';
        imgContainer.style.opacity = '1';
        imgContainer.style.transform = 'scale(1)';
      }, 300);
    });
  });
}
