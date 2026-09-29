import os
import glob
import re

DIR = '/Users/sidsmac/Documents/Home Studio'
html_files = glob.glob(os.path.join(DIR, '*.html'))

old_brands_regex = r'<div style="grid-column: span 3;">\s*<h4 class="mega-column-title">Featured Global Labels</h4>\s*<div class="mega-brand-grid">.*?</div>\s*</div>'

new_brands_html = """<div style="grid-column: span 3;">
              <h4 class="mega-column-title">Featured Global Labels</h4>
              <div class="mega-brand-grid">
                <a href="brand-axor.html" class="mega-brand-item">AXOR</a>
                <a href="brand-blanco.html" class="mega-brand-item">BLANCO</a>
                <a href="brand-carysil.html" class="mega-brand-item">CARYSIL</a>
                <a href="brand-geberit.html" class="mega-brand-item">GEBERIT</a>
                <a href="brand-grohe.html" class="mega-brand-item">GROHE</a>
                <a href="brand-hansgrohe.html" class="mega-brand-item">HANSGROHE</a>
                <a href="brand-jaquar.html" class="mega-brand-item">JAQUAR</a>
                <a href="brand-oyster.html" class="mega-brand-item">OYSTER</a>
                <a href="brand-stiebel.html" class="mega-brand-item">STIEBEL</a>
                <a href="brand-tece.html" class="mega-brand-item">TECE</a>
                <a href="brand-toto.html" class="mega-brand-item">TOTO</a>
              </div>
            </div>"""

for file_path in html_files:
    with open(file_path, 'r') as f:
        content = f.read()

    new_content = re.sub(old_brands_regex, new_brands_html, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated brands menu in {os.path.basename(file_path)}")

print("All navigation menus updated.")
