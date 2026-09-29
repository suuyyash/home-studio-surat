import os
import glob

DIR = '/Users/sidsmac/Documents/Home Studio'
html_files = glob.glob(os.path.join(DIR, '*.html'))

count = 0
for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Replace the "Brand Directory" link
    target_link = 'href="products.html#brands"'
    replacement_link = 'href="bathroom-fittings.html"'
    
    if target_link in content:
        content = content.replace(target_link, replacement_link)
        with open(filepath, 'w') as f:
            f.write(content)
        count += 1

print(f"Updated brand directory link to bathroom-fittings.html in {count} files.")
