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
        
    # Check if Brands link is already in mobile menu
    if 'href="bathroom-fittings.html" class="mobile-nav-link' in content:
        continue
        
    # Determine if Brands is the active page
    is_active = filename == 'bathroom-fittings.html' or filename.startswith('brand-')
    
    # We will search for:
    # <a href="products.html" class="mobile-nav-link...">Products</a>
    # and insert the Brands link below it.
    
    pattern = r'(<a href="products\.html"[^>]*>Products</a>)'
    
    if is_active:
        # If brands is active, we also need to make sure Products is NOT active (remove text-gold from products link if present)
        # and add text-gold to brands link.
        def replace_func(match):
            prod_link = match.group(1)
            # Remove text-gold from products if active (just in case)
            prod_link = prod_link.replace(' text-gold', '')
            brands_link = '\n      <a href="bathroom-fittings.html" class="mobile-nav-link text-gold">Brands</a>'
            return prod_link + brands_link
    else:
        def replace_func(match):
            prod_link = match.group(1)
            brands_link = '\n      <a href="bathroom-fittings.html" class="mobile-nav-link">Brands</a>'
            return prod_link + brands_link
            
    new_content = re.sub(pattern, replace_func, content)
    
    # If we made a replacement, write it back
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        count += 1

print(f"Added mobile Brands link to {count} files.")
