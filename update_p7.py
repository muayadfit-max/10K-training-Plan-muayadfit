import os
import codecs
import re

# 1. Rename 'red profile.jpg'
if os.path.exists("red profile.jpg"):
    os.rename("red profile.jpg", "red-profile.jpg")

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# 2. Replace SVG with Image inside .nav-brand
nav_brand_pattern = r'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">.*?<path d="M18 8h1a4 4 0 0 1 0 8h-1"></path>.*?<path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path>.*?<line x1="6" y1="1" x2="6" y2="4"></line>.*?<line x1="10" y1="1" x2="10" y2="4"></line>.*?<line x1="14" y1="1" x2="14" y2="4"></line>.*?</svg>'
new_img_html = '<img src="red-profile.jpg" alt="Muayad Fit" style="width: 36px; height: 36px; border-radius: 50%; object-fit: cover;">'

if re.search(nav_brand_pattern, html, flags=re.DOTALL):
    html = re.sub(nav_brand_pattern, new_img_html, html, flags=re.DOTALL)
    print("Avatar replaced successfully.")
else:
    # Just in case the format changed, do a more generic search between <a href="#" class="nav-brand"> and <span data-i18n="nav_brand">
    generic_pattern = r'(<a href="#" class="nav-brand">\s*)<svg.*?</svg>(\s*<span data-i18n="nav_brand">)'
    if re.search(generic_pattern, html, flags=re.DOTALL):
        html = re.sub(generic_pattern, r'\1' + new_img_html + r'\2', html, flags=re.DOTALL)
        print("Avatar replaced via generic pattern.")
    else:
        print("Warning: Could not find SVG to replace!")

# 3. Update the marketing text in JS
old_text = 'marketing_title: "تحتاج برنامج تدريبي وغذائي مخصص لك؟",'
new_text = 'marketing_title: "تحتاج برنامج تدريبي وغذائي مخصص لك؟ #شابه",'
if old_text in html:
    html = html.replace(old_text, new_text)
    print("Marketing text replaced successfully.")
else:
    print("Warning: Old marketing text not found.")

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)
