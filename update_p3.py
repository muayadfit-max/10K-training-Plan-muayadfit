import re
import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. Remove Testimonials section completely
html = re.sub(r'<!-- Testimonials -->\s*<section class="section testimonials">.*?</section>\s*', '', html, flags=re.DOTALL)

# 2. Remove Final CTA section completely
html = re.sub(r'<!-- Final CTA -->\s*<section class="final-cta">.*?</section>\s*', '', html, flags=re.DOTALL)

# 3. Update the plansData to align training to start on Sunday
plans_data_old_pattern = r'const plansData = \{.*?\n        \};'
plans_data_new = """const plansData = {
            'A': [
                ['1', '10x (30s run / 1m walk)', 'Cross Train 30m', 'Rest', '10x (1m run / 1m walk)', 'Cross Train 30m', '12x (1m run / 1m walk)', 'Rest'],
                ['2', '10x (90s run / 1m walk)', 'Cross Train 25m', 'Rest', '8x (2m run / 1m walk)', 'Cross Train 30m', '10x (90s run / 30s walk)', 'Rest'],
                ['3', '8x (2:30 run / 1m walk)', 'Cross Train 30m', 'Rest', '8x (3m run / 1m walk)', 'Cross Train 30m', '6x (4m run / 1m walk)', 'Rest'],
                ['4', '5x (5m run / 1m walk)', 'Cross Train 35m', 'Rest', '2x (10m run / 1m walk)', 'Cross Train 30m', '2x (10m run / 30s walk)', 'Rest'],
                ['5', 'Easy 40m', 'Cross Train 35m', 'Rest', 'Run 15m or Cross 30m', 'Easy/Cross 30m', 'Easy 3.2km (Continuous)', 'Rest'],
                ['6', 'Easy 45m', 'Cross Train 40m', 'Rest', 'Run 15m or Cross 30m', 'Easy/Cross 30m', 'Easy 4.8km', 'Rest'],
                ['7', 'Easy 5.6km', 'Cross Train 45m', 'Rest', 'Run 15m or Cross 30m', 'Easy/Cross 30m', 'Fartlek 5.6km (10x 1m hard)', 'Rest'],
                ['8', 'Easy 7.2km', 'Cross Train 50m', 'Rest', 'Run 15m or Cross 30m', 'Easy/Cross 30m', 'Fartlek 6.4km (10x 1m hard)', 'Rest'],
                ['9', 'Easy 7.2km', 'Cross Train 50m', 'Rest', 'Run 20m or Cross 30m', 'Easy/Cross 30m', 'Fartlek 7.2km (6x 2m hard)', 'Rest'],
                ['10', 'Easy 8km', 'Cross Train 60m', 'Rest', 'Run 20m or Cross 30m', 'Easy/Cross 30m', 'Fartlek 8km (4x 3m hard)', 'Rest'],
                ['11', 'Easy 9.6km', 'Cross Train 55m', 'Rest', 'Easy 8.8km', 'Run 6.4km (2x 5m hard)', 'Easy 6.4km (2x 5m hard)', 'Rest'],
                ['12', 'Easy 6.4km', 'Cross Train 35m', 'Easy 45m', 'Rest', 'Shake Out 3-4km', 'RACE DAY! 10K', 'Rest']
            ],
            'B': [
                ['1', '10x (30s run / 1m walk)', 'Cross Train 30m', 'Rest', '8x (3m run / 1m walk)', 'Cross Train 30m', '6x (4m run / 1m walk)', 'Rest'],
                ['2', '10x (90s run / 1m walk)', 'Cross Train 35m', 'Rest', '2x (10m run / 30s walk)', 'Cross Train 30m', 'Easy 3km', 'Rest'],
                ['3', 'Easy 4km', 'Cross Train 45m', 'Rest', 'Easy 5km', 'Easy/Cross 30m', 'Easy 5.5km', 'Rest'],
                ['4', 'Easy 6.5km', 'Cross Train 45m', 'Rest', 'Interval 5km (10x 1m hard)', 'Easy/Cross 30m', 'Easy 7km', 'Rest'],
                ['5', 'Easy 8km', 'Cross Train 50m', 'Rest', 'Interval 8km (10x 1m hard)', 'Easy 20m / Cross 30m', 'Easy 9-10km', 'Rest'],
                ['6', 'Easy 6.5km', 'Cross Train 45m', 'Rest', 'Taper 20m + 4x75m strides', 'Rest', 'RACE DAY! 10K', 'Rest']
            ],
            'C': [
                ['1', '5x (30s jog / 30s walk) + 10m jog', 'Rest', 'Easy Jog 15m', 'Rest', 'Rest', '10x (1m jog / 30s walk) + 15m jog', 'Rest'],
                ['2', '10x (30s jog / 30s walk) + 10m jog', 'Rest', 'Easy Jog 20m', 'Rest', 'Rest', '5x (5m jog / 1m walk) + Walk 40m', 'Rest'],
                ['3', '3x (10m jog / 90s walk)', 'Rest', 'Easy Jog 25m', 'Rest', 'Active Rest: Jog 10m', '10m jog, 3m walk, 10m jog', 'Rest'],
                ['4', '10x (3m jog / 1m walk)', 'Rest', 'Easy Jog 25m', 'Rest', 'Rest', '20m jog, 90s walk, 10m jog', 'Rest'],
                ['5', '6x (5m jog / 1m walk)', 'Rest', 'Easy Jog 25m', 'Rest', '15m jog, 90s walk, 15m jog', 'Walk 45m', 'Rest'],
                ['6', '10x (4m jog / 60s walk)', 'Rest', 'Easy 30m', 'Rest', '15m jog, 90s walk, 15m jog', 'Easy 35m', 'Rest'],
                ['7', 'Tempo 30m + 4x100m strides', 'Rest', 'Intervals (4x var. run/walk)', 'Rest', 'Easy 45m', 'Walk 45m', 'Rest'],
                ['8', 'Tempo 30m + 4x100m strides', 'Rest', '20m jog, 90s walk, 10m jog', 'Rest', 'Easy 50m', 'Walk 60m', 'Rest'],
                ['9', 'Tempo 30m + 4x100m strides', 'Rest', '10x (1m jog / 1m walk) x2', 'Rest', 'Easy 5km', 'Walk 45m', 'Rest'],
                ['10', 'Tempo 30m + 4x100m strides', 'Rest', 'Pyramid Intervals', 'Rest', 'Taper Easy 15m', 'RACE DAY! 10K', 'Rest']
            ]
        };"""
html = re.sub(plans_data_old_pattern, plans_data_new, html, flags=re.DOTALL)

# 4. Update the text for the Marketing Section (English)
html = html.replace('marketing_title: "Looking for More?",', 'marketing_title: "Need Custom Training & Nutrition?",')
html = html.replace('marketing_desc: "If you want a specific nutrition and training program tailored exactly to your body and goals, check out our premium coaching on muayadfit.com. All the information and packages are available there.",', 'marketing_desc: "If you need any help in terms of training and nutrition plans, and working with me one-on-one online, I can help with that. Check my website for all the details and see which plan suits you best.",')

# 5. Update the text for the Marketing Section (Arabic)
html = html.replace('marketing_title: "تبي شيء مخصص لك؟",', 'marketing_title: "تحتاج برنامج تدريبي وغذائي مخصص لك؟",')
html = html.replace('marketing_desc: "إذا كنت تدور برنامج غذائي وتدريبي مفصل على جسمك وأهدافك بالضبط، شيك على التدريب الشخصي في muayadfit.com. كل التفاصيل والباقات موجودة هناك.",', 'marketing_desc: "إذا كنت محتاج أي مساعدة بخصوص البرامج الغذائية والتدريبية وتبي تشتغل معي أونلاين بشكل شخصي، أقدر أساعدك في هذا الشيء. شيك على موقعي لكل التفاصيل واختار الباقة اللي تناسبك.",')

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Updates applied successfully.")
