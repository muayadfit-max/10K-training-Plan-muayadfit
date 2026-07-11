import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Coach Section
html = re.sub(r'<!-- Coach Section -->.*?<!-- Testimonials -->', '<!-- Testimonials -->', html, flags=re.DOTALL)

# 2. Add Modal CSS and Marketing CSS
css_to_add = """
        /* Modal & Table */
        .modal {
            display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%;
            background-color: rgba(0,0,0,0.7); backdrop-filter: blur(5px);
        }
        .modal-content {
            background-color: var(--white); margin: 5% auto; padding: 32px;
            border-radius: var(--border-radius-xl); width: 95%; max-width: 1000px;
            max-height: 85vh; overflow-y: auto; position: relative;
        }
        .close-modal {
            color: var(--gray-500); position: absolute; top: 20px; right: 24px;
            font-size: 28px; font-weight: bold; cursor: pointer; line-height: 1;
        }
        [dir="rtl"] .close-modal { right: auto; left: 24px; }
        .close-modal:hover { color: var(--black); }
        
        .table-responsive { overflow-x: auto; margin-top: 24px; }
        .plan-table { width: 100%; border-collapse: collapse; text-align: left; min-width: 800px; }
        [dir="rtl"] .plan-table { text-align: right; }
        .plan-table th, .plan-table td { padding: 12px 16px; border: 1px solid var(--gray-200); font-size: 0.9rem; vertical-align: top; }
        .plan-table th { background-color: var(--gray-100); color: var(--gray-800); font-weight: 700; position: sticky; top: 0;}
        .plan-table tr:nth-child(even) { background-color: var(--gray-50); }
        .week-cell { background-color: var(--primary-light) !important; color: var(--primary); font-weight: 800; text-align: center; width: 80px; }

        /* Marketing */
        .marketing-section {
            background-color: #090c0e; color: var(--white); padding: 80px 24px; position: relative;
        }
        .marketing-section::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
            background: linear-gradient(90deg, #f5c842, #1a9df1, #f5c842);
        }
        .marketing-section h2 { color: var(--white); margin-bottom: 16px; font-size: clamp(2rem, 3vw, 2.5rem); }
        .marketing-section p { color: rgba(255,255,255,0.7); max-width: 700px; margin: 0 auto 32px; font-size: 1.1rem; }
        .btn-gold { background-color: #f5c842; color: #111; box-shadow: 0 4px 14px 0 rgba(245,200,66,0.39); }
        .btn-gold:hover { background-color: #e0b433; color: #111; box-shadow: 0 6px 20px rgba(245,200,66,0.23); }
        .text-center { text-align: center; }
"""
html = html.replace('/* Mobile Adjustments */', css_to_add + '\n        /* Mobile Adjustments */')

# 3. Add Modal HTML and Marketing Section HTML before Footer
marketing_and_modal = """
    <!-- Marketing Section -->
    <section class="marketing-section">
        <div class="container text-center">
            <h2 data-i18n="marketing_title">Looking for More?</h2>
            <p data-i18n="marketing_desc">If you want a specific nutrition and training program tailored exactly to your body and goals, check out our premium coaching on muayadfit.com. All the information and packages are available there.</p>
            <a href="https://muayadfit.com" target="_blank" class="btn btn-primary btn-gold" data-i18n="marketing_btn">Visit muayadfit.com</a>
        </div>
    </section>

    <!-- Modal -->
    <div id="planModal" class="modal">
        <div class="modal-content">
            <span class="close-modal" onclick="closeModal()">&times;</span>
            <h2 id="modalTitle" style="margin-bottom: 8px;">Training Schedule</h2>
            <p style="color: var(--gray-600); font-size: 0.95rem; margin-bottom: 16px;" data-i18n="modal_sub">Follow this day-by-day progression. Listen to your body and never skip rest days.</p>
            <div class="table-responsive">
                <table class="plan-table">
                    <thead>
                        <tr>
                            <th data-i18n="week_th">Week</th>
                            <th data-i18n="day_1">Monday</th>
                            <th data-i18n="day_2">Tuesday</th>
                            <th data-i18n="day_3">Wednesday</th>
                            <th data-i18n="day_4">Thursday</th>
                            <th data-i18n="day_5">Friday</th>
                            <th data-i18n="day_6">Saturday</th>
                            <th data-i18n="day_7">Sunday</th>
                        </tr>
                    </thead>
                    <tbody id="modalTableBody">
                    </tbody>
                </table>
            </div>
        </div>
    </div>
"""
html = html.replace('<!-- Footer -->', marketing_and_modal + '\n    <!-- Footer -->')

# 4. Replace Google Doc Links
# Result Area CTA
result_btn_old = r'<a href="https://docs.google.com/document/d/placeholder-link" target="_blank" class="btn btn-primary" style="padding: 18px 40px; font-size: 1.15rem;">\s*<span data-i18n="res_cta">View Full Week-by-Week Schedule</span>\s*<svg.*?</svg>\s*</a>'
result_btn_new = r'<button type="button" onclick="openCurrentPlanModal()" class="btn btn-primary" style="padding: 18px 40px; font-size: 1.15rem;"><span data-i18n="res_cta">View Full Week-by-Week Schedule</span><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg></button>'
html = re.sub(result_btn_old, result_btn_new, html, flags=re.DOTALL)

# Previews Area CTAs
# Plan 12W (A)
html = re.sub(r'<a href="https://docs.google.com/document/d/placeholder-link" target="_blank" class="btn btn-outline" data-i18n="plan_btn">View Schedule</a>', r'<button onclick="openPlanModal(\'A\')" class="btn btn-outline" data-i18n="plan_btn">View Schedule</button>', html, count=1)
# Plan 10W (C)
html = re.sub(r'<a href="https://docs.google.com/document/d/placeholder-link" target="_blank" class="btn btn-outline" data-i18n="plan_btn">View Schedule</a>', r'<button onclick="openPlanModal(\'C\')" class="btn btn-outline" data-i18n="plan_btn">View Schedule</button>', html, count=1)
# Plan 6W (B)
html = re.sub(r'<a href="https://docs.google.com/document/d/placeholder-link" target="_blank" class="btn btn-outline" data-i18n="plan_btn">View Schedule</a>', r'<button onclick="openPlanModal(\'B\')" class="btn btn-outline" data-i18n="plan_btn">View Schedule</button>', html, count=1)

# 5. Add JS Data and Logic
js_data = """
        let currentRecommendedPlan = 'A';

        const plansData = {
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
                ['1', 'Rest', '5x (30s jog / 30s walk) + 10m jog', 'Rest', 'Easy Jog 15m', 'Rest', 'Rest', '10x (1m jog / 30s walk) + 15m jog'],
                ['2', 'Rest', '10x (30s jog / 30s walk) + 10m jog', 'Rest', 'Easy Jog 20m', 'Rest', 'Rest', '5x (5m jog / 1m walk) + Walk 40m'],
                ['3', 'Rest', '3x (10m jog / 90s walk)', 'Rest', 'Easy Jog 25m', 'Rest', 'Active Rest: Jog 10m', '10m jog, 3m walk, 10m jog'],
                ['4', 'Rest', '10x (3m jog / 1m walk)', 'Rest', 'Easy Jog 25m', 'Rest', 'Rest', '20m jog, 90s walk, 10m jog'],
                ['5', 'Rest', '6x (5m jog / 1m walk)', 'Rest', 'Easy Jog 25m', 'Rest', '15m jog, 90s walk, 15m jog', 'Walk 45m'],
                ['6', 'Rest', '10x (4m jog / 60s walk)', 'Rest', 'Easy 30m', 'Rest', '15m jog, 90s walk, 15m jog', 'Easy 35m'],
                ['7', 'Rest', 'Tempo 30m + 4x100m strides', 'Rest', 'Intervals (4x var. run/walk)', 'Rest', 'Easy 45m', 'Walk 45m'],
                ['8', 'Rest', 'Tempo 30m + 4x100m strides', 'Rest', '20m jog, 90s walk, 10m jog', 'Rest', 'Easy 50m', 'Walk 60m'],
                ['9', 'Rest', 'Tempo 30m + 4x100m strides', 'Rest', '10x (1m jog / 1m walk) x2', 'Rest', 'Easy 5km', 'Walk 45m'],
                ['10', 'Rest', 'Tempo 30m + 4x100m strides', 'Rest', 'Pyramid Intervals', 'Rest', 'Taper Easy 15m', 'RACE DAY! 10K']
            ]
        };

        function openCurrentPlanModal() {
            openPlanModal(currentRecommendedPlan);
        }

        function openPlanModal(planType) {
            const tbody = document.getElementById('modalTableBody');
            const title = document.getElementById('modalTitle');
            tbody.innerHTML = '';
            
            let planName = '';
            if (planType === 'A') planName = currentLang === 'en' ? '12-Week Steady Beginner' : 'المبتدئ المستمر - 12 أسبوعاً';
            if (planType === 'B') planName = currentLang === 'en' ? '6-Week Active Beginner' : 'المبتدئ النشط - 6 أسابيع';
            if (planType === 'C') planName = currentLang === 'en' ? '10-Week Couch to 10K' : 'من الأريكة إلى 10 كم - 10 أسابيع';
            
            title.textContent = planName;
            
            plansData[planType].forEach(row => {
                const tr = document.createElement('tr');
                row.forEach((cell, idx) => {
                    const td = document.createElement('td');
                    if (idx === 0) {
                        td.className = 'week-cell';
                        td.textContent = (currentLang === 'en' ? 'W' : 'أسبوع ') + cell;
                    } else {
                        td.textContent = cell;
                    }
                    tr.appendChild(td);
                });
                tbody.appendChild(tr);
            });
            
            document.getElementById('planModal').style.display = 'block';
        }

        function closeModal() {
            document.getElementById('planModal').style.display = 'none';
        }

        // Close modal if clicked outside
        window.onclick = function(event) {
            const modal = document.getElementById('planModal');
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
"""
# insert js_data inside <script>
html = html.replace('let currentLang = \'en\';', js_data + '\n        let currentLang = \'en\';')

# Add marketing translations and remove coach translations
html = html.replace('coach_title: "Meet Coach Muayad Alabri",', 'marketing_title: "Looking for More?",\n                marketing_desc: "If you want a specific nutrition and training program tailored exactly to your body and goals, check out our premium coaching on muayadfit.com. All the information and packages are available there.",\n                marketing_btn: "Visit muayadfit.com",\n                week_th: "Week",\n                day_1: "Monday",\n                day_2: "Tuesday",\n                day_3: "Wednesday",\n                day_4: "Thursday",\n                day_5: "Friday",\n                day_6: "Saturday",\n                day_7: "Sunday",\n                modal_sub: "Follow this day-by-day progression. Listen to your body and never skip rest days.",')
html = html.replace('coach_desc1: "With years of experience training runners across Oman and the GCC, Coach Muayad specializes in evidence-based programming that respects the unique demands of our climate.",', '')
html = html.replace('coach_desc2: "His philosophy centers on safe progression, injury prevention, and building a sustainable love for running, regardless of your starting point or body type.",', '')
html = html.replace('coach_cta: "Visit muayadfit.com",', '')

html = html.replace('coach_title: "تعرف على الكابتن مؤيد العبري",', 'marketing_title: "تبحث عن المزيد؟",\n                marketing_desc: "إذا كنت ترغب في برنامج غذائي وتدريبي مخصص يناسب جسمك وأهدافك بالضبط، تحقق من التدريب المتميز على muayadfit.com. جميع المعلومات والباقات متاحة هناك.",\n                marketing_btn: "زيارة muayadfit.com",\n                week_th: "الأسبوع",\n                day_1: "الاثنين",\n                day_2: "الثلاثاء",\n                day_3: "الأربعاء",\n                day_4: "الخميس",\n                day_5: "الجمعة",\n                day_6: "السبت",\n                day_7: "الأحد",\n                modal_sub: "اتبع هذا التقدم يوماً بيوم. استمع لجسمك ولا تفوت أيام الراحة أبداً.",')
html = html.replace('coach_desc1: "مع سنوات من الخبرة في تدريب العدائين في عمان ودول الخليج، يتخصص الكابتن مؤيد في البرامج المبنية على أسس علمية والتي تحترم المتطلبات الفريدة لمناخنا.",', '')
html = html.replace('coach_desc2: "تتركز فلسفته على التقدم الآمن، والوقاية من الإصابات، وبناء حب مستدام للجري، بغض النظر عن نقطة بدايتك أو نوع جسمك.",', '')
html = html.replace('coach_cta: "زيارة muayadfit.com",', '')

# Ensure currentRecommendedPlan updates in renderResults
html = html.replace("let planType = ''; // 'A', 'B', or 'C'", "let planType = ''; // 'A', 'B', or 'C'")
html = html.replace("resHighlights.innerHTML = ''; // Clear previous", "currentRecommendedPlan = planType;\n            resHighlights.innerHTML = ''; // Clear previous")

# Also remove navbar coach link
html = re.sub(r'<li><a href="#coach" class="nav-item" data-i18n="nav_coach">Coach Muayad</a></li>', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
