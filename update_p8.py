import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# Replace 1
old_text_1 = 'ابدا التقييم المجاني'
new_text_1 = 'ابدا التقييم (خفيف لطيف)'
html = html.replace(old_text_1, new_text_1)

# Replace 2
old_text_2 = 'برامج جري مدروسة ومصممة خصيصاً لأجواء الخليج. اعرف خطتك المناسبة لمستواك في 30 ثانية بس.'
new_text_2 = 'برامج جري مدروسة 3-4 مرات في الاسبوع. اعرف خطتك المناسبة لمستواك في 30 ثانية بس.'
html = html.replace(old_text_2, new_text_2)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Text replaced successfully.")
