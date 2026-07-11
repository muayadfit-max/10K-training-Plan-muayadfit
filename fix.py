import os
import codecs

if os.path.exists("Hero image.jpg"):
    os.rename("Hero image.jpg", "hero-image.jpg")

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

html = html.replace('Hero%20image.jpg', 'hero-image.jpg')
html = html.replace('Hero image.jpg', 'hero-image.jpg')

old_ar = 'hero_title: "اكتشف خطتك المثالية لسباق <span>10 كم</span>",'
new_ar = 'hero_title: "خلا نقفل ملف <span>الـ 10 كم</span>",'
html = html.replace(old_ar, new_ar)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Fixes applied.")
