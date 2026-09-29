import os
import glob

DIR = '/Users/sidsmac/Documents/Home Studio'

html_files = glob.glob(os.path.join(DIR, '*.html'))

target_string = '<a href="brand-axor.html" class="mega-brand-item">AXOR</a>'
replacement_string = '<a href="brand-artize.html" class="mega-brand-item">ARTIZE</a>\n                <a href="brand-axor.html" class="mega-brand-item">AXOR</a>'

count = 0
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
        
    if target_string in content and '<a href="brand-artize.html"' not in content:
        content = content.replace(target_string, replacement_string)
        with open(file, 'w') as f:
            f.write(content)
        count += 1

print(f"Added ARTIZE to the dropdown menu in {count} HTML files.")
