import os
import glob
import re

DIR = '/Users/sidsmac/Documents/Home Studio'
html_files = glob.glob(os.path.join(DIR, '*.html'))

# Pattern to search for the Products mega menu.
# We will match the Products mega menu block up to the mega-featured div.
pattern = re.compile(
    r'(<a href="products\.html"[^>]*>Products</a>\s*<div class="mega-menu">).*?(<div class="mega-featured">)',
    re.DOTALL
)

replacement = r'''\1
            <div class="mega-column">
              <h4 class="mega-column-title">CP Fittings</h4>
              <ul class="mega-list">
                <li><a href="#">Bathroom Fittings</a></li>
                <li><a href="#">Kitchen Sink</a></li>
                <li><a href="#">Sanitaryware</a></li>
                <li><a href="#">Steam & Sauna System</a></li>
              </ul>
            </div>
            <div class="mega-column">
              <h4 class="mega-column-title">Tiles</h4>
              <ul class="mega-list">
                <li><a href="#">Domestic Tiles</a></li>
              </ul>
            </div>
            <div class="mega-column">
              <h4 class="mega-column-title">Windows</h4>
              <ul class="mega-list">
                <li><a href="#">Premium Windows</a></li>
              </ul>
            </div>
            \2'''

count = 0
for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
        
    new_content, num_subs = pattern.subn(replacement, content)
    if num_subs > 0 and new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        count += 1

print(f"Updated Products mega menu in {count} HTML files.")
