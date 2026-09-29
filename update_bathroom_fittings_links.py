import os
import re

DIR = '/Users/sidsmac/Documents/Home Studio'
filepath = os.path.join(DIR, 'bathroom-fittings.html')

with open(filepath, 'r') as f:
    content = f.read()

# We want to add an <a href="brand-axor.html" class="btn-primary" style="margin-top: 1rem;">Explore AXOR</a>
# right under the brand-header or brand-video-container.

def insert_explore_link(match):
    brand_id = match.group(1) # e.g., axor
    brand_name = brand_id.upper()
    link_html = f'\n                <div style="text-align: center; margin-bottom: 3rem; margin-top: -1rem;" class="reveal"><a href="brand-{brand_id}.html" class="btn-secondary">Explore {brand_name}</a></div>\n'
    
    # We will append this right before the <div class="brand-gallery">
    # The regex matches up to <div class="brand-gallery">
    original_text = match.group(0)
    # inject just before <div class="brand-gallery">
    return original_text.replace('<div class="brand-gallery">', link_html + '            <div class="brand-gallery">')

# Pattern to find the section and inject the link before brand-gallery
pattern = re.compile(r'(<section class="brand-section" id="([a-z]+)">.*?<div class="brand-gallery">)', re.DOTALL)

new_content = pattern.sub(insert_explore_link, content)

with open(filepath, 'w') as f:
    f.write(new_content)

print("Updated bathroom-fittings.html with Explore Brand links.")
