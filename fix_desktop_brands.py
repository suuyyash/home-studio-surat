import os
import glob
import re

DIR = '/Users/sidsmac/Documents/Home Studio'
html_files = glob.glob(os.path.join(DIR, '*.html'))

count = 0
for filepath in html_files:
    filename = os.path.basename(filepath)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Let's fix the desktop header first.
    # Look for: <a href="products.html" class="nav-link">Products</a> followed by the mobile brand link
    # and remove the mobile brand link.
    
    desktop_pattern_1 = r'(<a href="products\.html" class="nav-link">Products</a>\s*<a href="bathroom-fittings\.html" class="mobile-nav-link">Brands</a>)'
    desktop_pattern_2 = r'(<a href="products\.html" class="nav-link">Products</a>\s*<a href="bathroom-fittings\.html" class="mobile-nav-link text-gold">Brands</a>)'
    
    new_content = re.sub(desktop_pattern_1, r'<a href="products.html" class="nav-link">Products</a>', content)
    new_content = re.sub(desktop_pattern_2, r'<a href="products.html" class="nav-link">Products</a>', new_content)
    
    # Ensure that inside mobile-nav-list, there is ONLY ONE Brands link.
    # We will search inside the <nav class="mobile-nav-list">...</nav> block
    # and make sure it has the Brands link.
    
    mobile_nav_pattern = r'(<nav class="mobile-nav-list">[\s\S]*?</nav>)'
    
    def fix_mobile_nav(match):
        nav_block = match.group(1)
        # Remove any Brands link from it first so we don't duplicate
        nav_block = re.sub(r'\s*<a href="bathroom-fittings\.html" class="mobile-nav-link[^>]*>Brands</a>', '', nav_block)
        
        # Now insert it cleanly after the Products link in the mobile menu
        is_active = filename == 'bathroom-fittings.html' or filename.startswith('brand-')
        active_class = "mobile-nav-link text-gold" if is_active else "mobile-nav-link"
        
        # Replace products link inside the mobile drawer with products link + brand link
        nav_block = re.sub(
            r'(<a href="products\.html" class="mobile-nav-link[^>]*>Products</a>)',
            rf'\1\n      <a href="bathroom-fittings.html" class="{active_class}">Brands</a>',
            nav_block
        )
        return nav_block

    new_content = re.sub(mobile_nav_pattern, fix_mobile_nav, new_content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        count += 1

print(f"Fixed navigation in {count} files.")
