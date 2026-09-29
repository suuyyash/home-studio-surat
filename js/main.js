document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initCustomCursor();
  initMobileNav();
  initScrollReveals();
  initMegaMenuHover();
  initParallax();
  initAccordions();
  initVideoFadeIn();
  initHeaderScroll();
});


/* --- Theme Management --- */
function initTheme() {
  const themeToggleBtns = document.querySelectorAll('.theme-toggle-btn');
  
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const initialTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
  
  document.documentElement.setAttribute('data-theme', initialTheme);
  
  themeToggleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
    });
  });
}

/* --- Custom Cursor Logic (Dynamic Labels & Trailing) --- */
function initCustomCursor() {
  const cursorDot = document.querySelector('.custom-cursor');
  const cursorOutline = document.querySelector('.custom-cursor-outline');
  
  if (!cursorDot || !cursorOutline) return;
  
  // Inject the label element dynamically inside the outline circle
  let label = cursorOutline.querySelector('.cursor-label');
  if (!label) {
    label = document.createElement('span');
    label.className = 'cursor-label';
    label.textContent = 'Enquire';
    cursorOutline.appendChild(label);
  }
  
  let mouseX = 0;
  let mouseY = 0;
  let outlineX = 0;
  let outlineY = 0;
  
  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    
    cursorDot.style.left = `${mouseX}px`;
    cursorDot.style.top = `${mouseY}px`;
  });
  
  function animateOutline() {
    const delay = 8;
    outlineX += (mouseX - outlineX) / delay;
    outlineY += (mouseY - outlineY) / delay;
    
    cursorOutline.style.left = `${outlineX}px`;
    cursorOutline.style.top = `${outlineY}px`;
    
    requestAnimationFrame(animateOutline);
  }
  animateOutline();
  
  // Custom cursor states based on target parameters
  const interactives = document.querySelectorAll('a, button, input, textarea, select, .mega-brand-item, .brand-logo-text, .hotspot, .spec-accordion-header, .tour-step-btn');
  
  interactives.forEach(el => {
    el.addEventListener('mouseenter', () => {
      document.body.classList.add('hovering-link');
      
      // Determine what to display inside the cursor circle
      if (el.tagName === 'A' && el.href.includes('contact.html')) {
        label.textContent = 'Enquire';
      } else if (el.classList.contains('hotspot')) {
        label.textContent = 'Explore';
      } else if (el.classList.contains('spec-accordion-header')) {
        label.textContent = 'Specs';
      } else if (el.classList.contains('theme-toggle-btn')) {
        label.textContent = 'Mode';
      } else if (el.classList.contains('hamburger')) {
        label.textContent = 'Menu';
      } else {
        // Check for data attribute or default to View
        label.textContent = el.getAttribute('data-cursor') || 'View';
      }
    });
    
    el.addEventListener('mouseleave', () => {
      document.body.classList.remove('hovering-link');
    });
  });
}

/* --- Mobile Navigation Menu Drawer --- */
function initMobileNav() {
  const hamburger = document.querySelector('.hamburger');
  const drawer = document.querySelector('.mobile-drawer');
  const overlay = document.querySelector('.mobile-overlay');
  
  if (!hamburger || !drawer || !overlay) return;
  
  const toggleMenu = () => {
    hamburger.classList.toggle('open');
    drawer.classList.toggle('open');
    overlay.classList.toggle('active');
    document.body.style.overflow = drawer.classList.contains('open') ? 'hidden' : '';
  };
  
  hamburger.addEventListener('click', toggleMenu);
  overlay.addEventListener('click', toggleMenu);
  
  // Mobile Nav Accordion Header Toggles with Dynamic Smooth Height Calculation
  const accordionHeaders = drawer.querySelectorAll('.mobile-nav-accordion-header');
  accordionHeaders.forEach(header => {
    header.addEventListener('click', (e) => {
      // If clicking directly on an anchor link, allow normal navigation
      if (e.target.tagName === 'A') return;
      e.stopPropagation();

      const parent = header.closest('.mobile-nav-item-accordion');
      if (!parent) return;

      const body = parent.querySelector(':scope > .mobile-nav-accordion-body');
      if (!body) return;

      const isOpen = parent.classList.contains('open');

      if (isOpen) {
        // Prepare closing: lock current height explicitly before transitioning to 0
        body.style.maxHeight = body.scrollHeight + 'px';
        body.offsetHeight; // Force reflow
        parent.classList.remove('open');
        body.style.maxHeight = '0px';
      } else {
        // Prepare opening: set target scrollHeight
        parent.classList.add('open');
        body.style.maxHeight = body.scrollHeight + 'px';

        setTimeout(() => {
          if (parent.classList.contains('open')) {
            body.style.maxHeight = 'none';
          }
        }, 400); // 400ms is slightly longer than the 350ms CSS transition
      }
    });
  });

  const mobileNavLinks = drawer.querySelectorAll('a');
  mobileNavLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (drawer.classList.contains('open')) toggleMenu();
    });
  });

  // Auto-close mobile drawer when resized to desktop view
  window.addEventListener('resize', () => {
    if (window.innerWidth > 900 && drawer.classList.contains('open')) {
      hamburger.classList.remove('open');
      drawer.classList.remove('open');
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    }
  });
}

/* --- Scroll-Reveal Animations (Intersection Observer) --- */
function initScrollReveals() {
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .draw-line');
  
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.12
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  revealElements.forEach(el => {
    observer.observe(el);
  });
}

/* --- Mega Menu Hover Delay Timing --- */
function initMegaMenuHover() {
  const navItems = document.querySelectorAll('.nav-item');
  
  navItems.forEach(item => {
    const megaMenu = item.querySelector('.mega-menu');
    if (!megaMenu) return;
    
    let timeoutId;
    
    item.addEventListener('mouseenter', () => {
      clearTimeout(timeoutId);
      megaMenu.style.display = 'grid';
      setTimeout(() => {
        megaMenu.style.opacity = '1';
        megaMenu.style.visibility = 'visible';
        megaMenu.style.transform = 'translateY(0)';
        megaMenu.style.pointerEvents = 'auto';
      }, 50);
    });
    
    item.addEventListener('mouseleave', () => {
      timeoutId = setTimeout(() => {
        megaMenu.style.opacity = '0';
        megaMenu.style.visibility = 'hidden';
        megaMenu.style.transform = 'translateY(-10px)';
        megaMenu.style.pointerEvents = 'none';
      }, 150);
    });
  });
}

/* --- Scroll-Driven Parallax physics --- */
function initParallax() {
  const parallaxBgs = document.querySelectorAll('.hero-video-bg, .brand-hero-video');
  if (parallaxBgs.length === 0) return;
  
  window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    parallaxBgs.forEach(bg => {
      // Offset position slowly by scrolled factor
      bg.style.transform = `translate3d(0, ${scrolled * 0.18}px, 0)`;
    });
  });
}

/* --- Collapsible Accordions (Specifications panels) --- */
function initAccordions() {
  const headers = document.querySelectorAll('.spec-accordion-header');
  headers.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentElement;
      const content = item.querySelector('.spec-accordion-content');
      const isActive = item.classList.contains('active');
      
      // Close other accordion blocks in the same container for clean accordion toggle
      const container = item.parentElement;
      container.querySelectorAll('.spec-accordion-item').forEach(i => {
        if (i !== item) {
          i.classList.remove('active');
          const c = i.querySelector('.spec-accordion-content');
          if (c) c.style.maxHeight = null;
        }
      });
      
      if (isActive) {
        item.classList.remove('active');
        content.style.maxHeight = null;
      } else {
        item.classList.add('active');
        content.style.maxHeight = content.scrollHeight + "px";
      }
    });
  });
}

/* --- Smooth Hero Video Fade In --- */
function initVideoFadeIn() {
  const videos = document.querySelectorAll('.hero-video-bg, .brand-hero-video');
  videos.forEach(video => {
    // If video is already playing / loaded, trigger fade-in immediately
    if (video.readyState >= 3) {
      video.classList.add('video-playing');
    }
    
    // Add event listeners for playing states
    video.addEventListener('playing', () => {
      video.classList.add('video-playing');
    });
    
    // Fallback if playing event is not caught
    video.addEventListener('loadeddata', () => {
      video.classList.add('video-playing');
    });
  });
}

/* --- Transparent Header Scroll Physics --- */
function initHeaderScroll() {
  const header = document.querySelector('header');
  if (!header) return;
  
  const handleScroll = () => {
    if (window.scrollY > 20) {
      header.classList.add('header-scrolled');
    } else {
      header.classList.remove('header-scrolled');
    }
  };
  
  window.addEventListener('scroll', handleScroll);
  handleScroll();
}
