import re
import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. Remove Trust Bar
trust_bar_pattern = r'<!-- Trust Bar -->\s*<div class="trust-bar">.*?</div>\s*</div>\s*</div>'
html = re.sub(trust_bar_pattern, '', html, flags=re.DOTALL)

# 2. Shift Headers in Modal
modal_headers_old = """                            <th data-i18n="day_1">Monday</th>
                            <th data-i18n="day_2">Tuesday</th>
                            <th data-i18n="day_3">Wednesday</th>
                            <th data-i18n="day_4">Thursday</th>
                            <th data-i18n="day_5">Friday</th>
                            <th data-i18n="day_6">Saturday</th>
                            <th data-i18n="day_7">Sunday</th>"""

modal_headers_new = """                            <th data-i18n="day_1">Sunday</th>
                            <th data-i18n="day_2">Monday</th>
                            <th data-i18n="day_3">Tuesday</th>
                            <th data-i18n="day_4">Wednesday</th>
                            <th data-i18n="day_5">Thursday</th>
                            <th data-i18n="day_6">Friday</th>
                            <th data-i18n="day_7">Saturday</th>"""
html = html.replace(modal_headers_old, modal_headers_new)

# 3. JS Data update (Shift arrays and update En strings)
plans_data_old_pattern = r'const plansData = \{.*?\n        \};'
plans_data_new = """const plansData = {
            'A': [
                ['1', 'Rest', '10x (30s run / 1m walk)', 'Cross Train 30m', 'Rest', '10x (1m run / 1m walk)', 'Cross Train 30m', '12x (1m run / 1m walk)'],
                ['2', 'Rest', '10x (90s run / 1m walk)', 'Cross Train 25m', 'Rest', '8x (2m run / 1m walk)', 'Cross Train 30m', '10x (90s run / 30s walk)'],
                ['3', 'Rest', '8x (2:30 run / 1m walk)', 'Cross Train 30m', 'Rest', '8x (3m run / 1m walk)', 'Cross Train 30m', '6x (4m run / 1m walk)'],
                ['4', 'Rest', '5x (5m run / 1m walk)', 'Cross Train 35m', 'Rest', '2x (10m run / 1m walk)', 'Cross Train 30m', '2x (10m run / 30s walk)'],
                ['5', 'Rest', 'Easy 40m', 'Cross Train 35m', 'Rest', 'Run 15m or Cross 30m', 'Easy/Cross 30m', 'Easy 3.2km (Continuous)'],
                ['6', 'Rest', 'Easy 45m', 'Cross Train 40m', 'Rest', 'Run 15m or Cross 30m', 'Easy/Cross 30m', 'Easy 4.8km'],
                ['7', 'Rest', 'Easy 5.6km', 'Cross Train 45m', 'Rest', 'Run 15m or Cross 30m', 'Easy/Cross 30m', 'Fartlek 5.6km (10x 1m hard)'],
                ['8', 'Rest', 'Easy 7.2km', 'Cross Train 50m', 'Rest', 'Run 15m or Cross 30m', 'Easy/Cross 30m', 'Fartlek 6.4km (10x 1m hard)'],
                ['9', 'Rest', 'Easy 7.2km', 'Cross Train 50m', 'Rest', 'Run 20m or Cross 30m', 'Easy/Cross 30m', 'Fartlek 7.2km (6x 2m hard)'],
                ['10', 'Rest', 'Easy 8km', 'Cross Train 60m', 'Rest', 'Run 20m or Cross 30m', 'Easy/Cross 30m', 'Fartlek 8km (4x 3m hard)'],
                ['11', 'Rest', 'Easy 9.6km', 'Cross Train 55m', 'Rest', 'Easy 8.8km', 'Run 6.4km (2x 5m hard)', 'Easy 6.4km (2x 5m hard)'],
                ['12', 'Rest', 'Easy 6.4km', 'Cross Train 35m', 'Easy 45m', 'Rest', 'Shake Out 3-4km', 'RACE DAY! 10K']
            ],
            'B': [
                ['1', 'Rest', '10x (30s run / 1m walk)', 'Cross Train 30m', 'Rest', '8x (3m run / 1m walk)', 'Cross Train 30m', '6x (4m run / 1m walk)'],
                ['2', 'Rest', '10x (90s run / 1m walk)', 'Cross Train 35m', 'Rest', '2x (10m run / 30s walk)', 'Cross Train 30m', 'Easy 3km'],
                ['3', 'Rest', 'Easy 4km', 'Cross Train 45m', 'Rest', 'Easy 5km', 'Easy/Cross 30m', 'Easy 5.5km'],
                ['4', 'Rest', 'Easy 6.5km', 'Cross Train 45m', 'Rest', 'Interval 5km (10x 1m hard)', 'Easy/Cross 30m', 'Easy 7km'],
                ['5', 'Rest', 'Easy 8km', 'Cross Train 50m', 'Rest', 'Interval 8km (10x 1m hard)', 'Easy 20m / Cross 30m', 'Easy 9-10km'],
                ['6', 'Rest', 'Easy 6.5km', 'Cross Train 45m', 'Rest', 'Taper 20m + 4x75m strides', 'Rest', 'RACE DAY! 10K']
            ],
            'C': [
                ['1', '10x (1m jog / 30s walk) + 15m jog', 'Rest', '5x (30s jog / 30s walk) + 10m jog', 'Rest', 'Easy Jog 15m', 'Rest', 'Rest'],
                ['2', '5x (5m jog / 1m walk) + Walk 40m', 'Rest', '10x (30s jog / 30s walk) + 10m jog', 'Rest', 'Easy Jog 20m', 'Rest', 'Rest'],
                ['3', '10m jog, 3m walk, 10m jog', 'Rest', '3x (10m jog / 90s walk)', 'Rest', 'Easy Jog 25m', 'Rest', 'Active Rest: Jog 10m'],
                ['4', '20m jog, 90s walk, 10m jog', 'Rest', '10x (3m jog / 1m walk)', 'Rest', 'Easy Jog 25m', 'Rest', 'Rest'],
                ['5', 'Walk 45m', 'Rest', '6x (5m jog / 1m walk)', 'Rest', 'Easy Jog 25m', 'Rest', '15m jog, 90s walk, 15m jog'],
                ['6', 'Easy 35m', 'Rest', '10x (4m jog / 60s walk)', 'Rest', 'Easy 30m', 'Rest', '15m jog, 90s walk, 15m jog'],
                ['7', 'Walk 45m', 'Rest', 'Tempo 30m + 4x100m strides', 'Rest', 'Intervals (4x var. run/walk)', 'Rest', 'Easy 45m'],
                ['8', 'Walk 60m', 'Rest', 'Tempo 30m + 4x100m strides', 'Rest', '20m jog, 90s walk, 10m jog', 'Rest', 'Easy 50m'],
                ['9', 'Walk 45m', 'Rest', 'Tempo 30m + 4x100m strides', 'Rest', '10x (1m jog / 1m walk) x2', 'Rest', 'Easy 5km'],
                ['10', 'RACE DAY! 10K', 'Rest', 'Tempo 30m + 4x100m strides', 'Rest', 'Pyramid Intervals', 'Rest', 'Taper Easy 15m']
            ]
        };"""
html = re.sub(plans_data_old_pattern, plans_data_new, html, flags=re.DOTALL)

# EN Translation shift
html = html.replace('day_1: "Monday",', 'day_1: "Sunday",')
html = html.replace('day_2: "Tuesday",', 'day_2: "Monday",')
html = html.replace('day_3: "Wednesday",', 'day_3: "Tuesday",')
html = html.replace('day_4: "Thursday",', 'day_4: "Wednesday",')
html = html.replace('day_5: "Friday",', 'day_5: "Thursday",')
html = html.replace('day_6: "Saturday",', 'day_6: "Friday",')
html = html.replace('day_7: "Sunday",', 'day_7: "Saturday",')

# 4. Replace entire 'ar: { ... }' object
ar_regex = r'ar:\s*\{.*?\}'

ar_new = """ar: {
                nav_brand: "مؤيد فت",
                nav_how: "كيف الطريقة",
                nav_plans: "الخطط",
                nav_safety: "السلامة",
                nav_book: "احجز تدريبك",
                hero_title: "اكتشف خطتك المثالية لسباق <span>10 كم</span>",
                hero_sub: "برامج جري مدروسة ومصممة خصيصاً لأجواء الخليج. اعرف خطتك المناسبة لمستواك في 30 ثانية بس.",
                hero_cta: "ابدا التقييم المجاني",
                trust_text: "",
                how_title: "كيف الطريقة",
                how_sub: "طريقة بسيطة ومخصصة توصلك لخط نهاية الـ 10 كم بأمان وقوة.",
                how_step1_title: "1. أدخل بياناتك",
                how_step1_desc: "دخل وزنك وأقصى مسافة تقدر تجريها بشكل متواصل حالياً.",
                how_step2_title: "2. تحليل النتائج",
                how_step2_desc: "نظامنا يحلل بياناتك ويركز بشكل كبير على سلامة مفاصلك وتنظيم سرعتك.",
                how_step3_title: "3. استلم خطتك",
                how_step3_desc: "احصل على جدول تدريبي لـ 6 أو 10 أو 12 أسبوع مصمم خصيصاً لمستواك.",
                form_title: "حاسبة التقييم",
                form_sub: "عبي الخانتين تحت عشان تكتشف الخطة الأنسب لك.",
                form_weight: "الوزن (كجم)",
                form_distance: "أقصى مسافة جري متواصل (كم)",
                form_error_weight: "الرجاء إدخال وزن صحيح.",
                form_error_distance: "الرجاء إدخال مسافة صحيحة.",
                form_submit: "اكتشف خطتي",
                res_badge: "الخطة الموصى بها",
                res_safety_title: "تنبيه السلامة لأجواء الخليج",
                res_highlights_title: "أبرز نقاط الخطة والتقدم",
                res_cta: "عرض الجدول الأسبوعي الكامل",
                preview_title: "استكشف خططنا",
                preview_sub: "اطلع على المسارات المختلفة اللي نقدمها. ننصحك تستخدم الحاسبة فوق عشان تعرف الخطة المناسبة لمستواك.",
                plan_12w_dur: "12 أسبوع",
                plan_12w_title: "المبتدئ المستمر",
                plan_12w_desc: "تركز الخطة على المشي والجري مع بعض عشان نرفع لياقتك ونحمي مفاصلك. ممتازة جداً للأوزان الثقيلة أو اللي بيبدأون من الصفر.",
                plan_10w_dur: "10 أسابيع",
                plan_10w_title: "من الكنب لـ 10 كم",
                plan_10w_desc: "تدرج مريح من المشي والجري الخفيف إلى الجري المتواصل. تناسب اللي يقدرون يهرولون خفيف بس يحتاجون يرفعون المسافة.",
                plan_6w_dur: "6 أسابيع",
                plan_6w_title: "المبتدئ النشط",
                plan_6w_desc: "للعدائين اللي يركضون 4 كم وفوق. نركز فيها على تمارين الفترات (الإنترفل) والتمبو وزيادة المسافة بشكل مدروس.",
                plan_btn: "عرض الجدول",
                safety_title: "إرشادات السلامة وأجواء الخليج",
                safety_sub: "الجري عندنا يحتاج تكتيك مختلف. اتبع هذي النصائح الأساسية عشان تتمرن بأمان.",
                safety_1_title: "التوقيت جداً مهم",
                safety_1_desc: "دايماً خل تمرينك الصباح بدري (قبل 7) أو في المساء عشان تتجنب الشمس والإجهاد الحراري.",
                safety_2_title: "طريقة شرب الماي",
                safety_2_desc: "لا تنتظر لين تعطش. اشرب ماي قبل التمرين واستخدم أملاح (إلكتروليتس) لتمارينك اللي تطوف 45 دقيقة.",
                safety_3_title: "اسمع لجسمك",
                safety_3_desc: "العضلات تبني نفسها وقت الراحة. لا تسحب على أيام الراحة المجدولة، وإذا حسيت بضغط على مفاصلك بدل التمرين لسباحة أو سيكل.",
                safety_4_title: "السرعة ونبض القلب",
                safety_4_desc: "اركض بسرعة خفيفة تقدر تسولف فيها. إذا حسيت إنك تلهث، خفف السرعة أو امش. طبيعي النبض يرتفع مع الحر.",
                marketing_title: "تبي شيء مخصص لك؟",
                marketing_desc: "إذا كنت تدور برنامج غذائي وتدريبي مفصل على جسمك وأهدافك بالضبط، شيك على التدريب الشخصي في muayadfit.com. كل التفاصيل والباقات موجودة هناك.",
                marketing_btn: "زور muayadfit.com",
                test_title: "قصص نجاح",
                test_sub: "شوف تجارب اللي طبقوا هذي الجداول وحققوا أهدافهم في الـ 10 كم.",
                test_1_text: '\\"كشخص وزنه ثقيل، كنت خايف جداً على ركبي. نظام المشي والجري في خطة الـ 12 أسبوع كان خيالي. خلصت أول 10 كم لي وبدون أي إصابات أو ألم.\\"',
                test_1_name: "أحمد س.",
                test_1_plan: "12 أسبوع - المبتدئ المستمر",
                test_2_text: '\\"خطة من الكنب للـ 10 كم شدتني صح وبنفس الوقت حافظت علي في حر مسقط. نصايح الكابتن مؤيد للترطيب أنقذت جرياتي الطويلة!\\"',
                test_2_name: "مها ك.",
                test_2_plan: "10 أسابيع - من الكنب لـ 10 كم",
                test_3_text: '\\"كنت أقدر أجري 4 كم بس أتعب بسرعة. خطة الـ 6 أسابيع دخلت فيها تمارين تمبو وفترات غيرت طريقتي في تنظيم السرعة بالكامل. وحطمت رقمي!\\"',
                test_3_name: "طارق م.",
                test_3_plan: "6 أسابيع - المبتدئ النشط",
                cta_title: "جاهز تبدأ رحلتك؟",
                cta_desc: "سوي التقييم الحين وخذ خطتك المبنية على أسس علمية اليوم.",
                cta_btn: "سوي التقييم",
                footer_brand: "مؤيد فت",
                footer_credit: "هذي الأداة تم تطويرها بواسطة مؤيد فت • <a href='https://muayadfit.com' target='_blank'>muayadfit.com</a>",
                week_th: "الأسبوع",
                day_1: "الأحد",
                day_2: "الاثنين",
                day_3: "الثلاثاء",
                day_4: "الأربعاء",
                day_5: "الخميس",
                day_6: "الجمعة",
                day_7: "السبت",
                modal_sub: "امش على هذا الجدول يوماً بيوم. اسمع لجسمك ولا تفوت أيام الراحة."
            }"""

html = re.sub(ar_regex, ar_new, html, flags=re.DOTALL)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Updates applied successfully.")
