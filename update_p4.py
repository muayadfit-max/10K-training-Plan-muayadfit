import re
import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. Remove Safety Box HTML
safety_box_pattern = r'<div class="safety-note-box">.*?</div>\s*</div>'
html = re.sub(safety_box_pattern, '', html, flags=re.DOTALL)

# Also remove the resSafetyText JS assignments to prevent errors
html = re.sub(r'const resSafetyText = document\.getElementById\(\'resSafetyText\'\);\s*', '', html)
html = re.sub(r'resSafetyText\.textContent = currentLang === \'en\'\s*\?\s*".*?"\s*:\s*".*?";\s*', '', html, flags=re.DOTALL)

# 2. Update How It Works Step 2 description
html = html.replace('how_step2_desc: "Our algorithm categorizes your needs focusing heavily on joint safety and pacing.",', 'how_step2_desc: "We will check which plan suits you best.",')
html = html.replace('how_step2_desc: "نظامنا يحلل بياناتك ويركز بشكل كبير على سلامة مفاصلك وتنظيم سرعتك.",', 'how_step2_desc: "راح نشيك أي خطة تناسبك أكثر.",')

# 3. Rename the plans (Translations)
# 12W
html = html.replace('plan_12w_title: "Steady Beginner",', 'plan_12w_title: "12 Weeks to 10K",')
html = html.replace('plan_12w_title: "المبتدئ المستمر",', 'plan_12w_title: "12 أسبوع للـ 10 كم",')
# 10W
html = html.replace('plan_10w_title: "Couch to 10K",', 'plan_10w_title: "10 Weeks to 10K",')
html = html.replace('plan_10w_title: "من الكنب لـ 10 كم",', 'plan_10w_title: "10 أسابيع للـ 10 كم",')
# 6W
html = html.replace('plan_6w_title: "Active Beginner",', 'plan_6w_title: "6 Weeks to 10K",')
html = html.replace('plan_6w_title: "المبتدئ النشط",', 'plan_6w_title: "6 أسابيع للـ 10 كم",')

# 4. Rename the plans (JS renderResults)
# A
html = html.replace("resTitle.textContent = currentLang === 'en' ? '12-Week Steady Beginner Plan' : 'خطة المبتدئ المستمر (12 أسبوعاً)';", "resTitle.textContent = currentLang === 'en' ? '12 Weeks to 10K' : '12 أسبوع للـ 10 كم';")
# B
html = html.replace("resTitle.textContent = currentLang === 'en' ? '6-Week Active Beginner Plan' : 'خطة المبتدئ النشط (6 أسابيع)';", "resTitle.textContent = currentLang === 'en' ? '6 Weeks to 10K' : '6 أسابيع للـ 10 كم';")
# C
html = html.replace("resTitle.textContent = currentLang === 'en' ? '10-Week Couch to 10K Plan' : 'من الأريكة إلى 10 كم (10 أسابيع)';", "resTitle.textContent = currentLang === 'en' ? '10 Weeks to 10K' : '10 أسابيع للـ 10 كم';")

# 5. Rename the plans (JS openPlanModal)
# A
html = html.replace("if (planType === 'A') planName = currentLang === 'en' ? '12-Week Steady Beginner' : 'المبتدئ المستمر - 12 أسبوعاً';", "if (planType === 'A') planName = currentLang === 'en' ? '12 Weeks to 10K' : '12 أسبوع للـ 10 كم';")
# B
html = html.replace("if (planType === 'B') planName = currentLang === 'en' ? '6-Week Active Beginner' : 'المبتدئ النشط - 6 أسابيع';", "if (planType === 'B') planName = currentLang === 'en' ? '6 Weeks to 10K' : '6 أسابيع للـ 10 كم';")
# C
html = html.replace("if (planType === 'C') planName = currentLang === 'en' ? '10-Week Couch to 10K' : 'من الأريكة إلى 10 كم - 10 أسابيع';", "if (planType === 'C') planName = currentLang === 'en' ? '10 Weeks to 10K' : '10 أسابيع للـ 10 كم';")

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Updates applied successfully.")
