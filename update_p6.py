import re
import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. Update Hero HTML using regex
hero_html_pattern = r'<!-- Hero -->\s*<header class="hero">.*?<div class="container">.*?<h1 data-i18n="hero_title">.*?</h1>.*?<p data-i18n="hero_sub">.*?</p>.*?<a href="#assessment" class="btn btn-primary" data-i18n="hero_cta">.*?</a>.*?</div>\s*</header>'

new_hero_html = """<!-- Hero -->
    <header class="hero">
        <div class="container hero-container">
            <div class="hero-content">
                <h1 data-i18n="hero_title">Discover Your Ideal <span>10K Plan</span></h1>
                <p data-i18n="hero_sub" class="hero-subtext">Expert, science-based running programs designed for the Gulf climate. Find the perfect progression for your current fitness level in 30 seconds.</p>
                <a href="#assessment" class="btn btn-primary" data-i18n="hero_cta">Start Free Assessment</a>
            </div>
            <div class="hero-image">
                <img src="hero-image.jpg" alt="Muayad Fit 10K Plan" />
            </div>
        </div>
    </header>"""

if re.search(hero_html_pattern, html, flags=re.DOTALL):
    html = re.sub(hero_html_pattern, new_hero_html, html, flags=re.DOTALL)
    print("Hero HTML replaced successfully.")
else:
    print("Warning: Hero HTML pattern not found!")

# 2. Update Hero CSS using regex
hero_css_pattern = r'/\*\s*Hero\s*\*/\s*\.hero\s*\{.*?\.hero p\s*\{.*?\}'

new_hero_css = """/* Hero */
        .hero {
            padding-top: 140px;
            padding-bottom: 80px;
            background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 100%);
            text-align: left;
        }
        
        [dir="rtl"] .hero { text-align: right; }

        .hero-container {
            display: flex;
            align-items: center;
            gap: 40px;
            justify-content: space-between;
        }

        .hero-content {
            flex: 1;
            max-width: 580px;
        }

        .hero-image {
            flex: 1;
            max-width: 500px;
            margin: 0 auto;
        }

        .hero-image img {
            width: 100%;
            height: auto;
            border-radius: var(--border-radius-xl);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            object-fit: cover;
            aspect-ratio: 4/5;
        }

        .hero h1 {
            font-size: clamp(2.5rem, 4vw, 4rem);
            margin-bottom: 24px;
            letter-spacing: -1px;
            color: var(--black);
            line-height: 1.1;
        }

        .hero h1 span {
            color: var(--primary);
        }

        .hero p.hero-subtext {
            font-size: clamp(1.1rem, 2vw, 1.25rem);
            color: var(--gray-600);
            margin-bottom: 40px;
            line-height: 1.6;
        }"""

if re.search(hero_css_pattern, html, flags=re.DOTALL):
    html = re.sub(hero_css_pattern, new_hero_css, html, flags=re.DOTALL)
    print("Hero CSS replaced successfully.")
else:
    print("Warning: Hero CSS pattern not found!")

# 3. Add Mobile Adjustments (only if not already added)
mobile_css = """
            .hero-container {
                flex-direction: column;
                text-align: center;
            }
            [dir="rtl"] .hero-container { text-align: center; }
            .hero-content { margin-bottom: 16px; }
            .hero { padding-top: 120px; padding-bottom: 60px; }"""

if ".hero-container" not in html[html.find('/* Mobile Adjustments */'):]:
    html = html.replace('/* Mobile Adjustments */', '/* Mobile Adjustments */' + mobile_css)
    print("Mobile CSS appended.")

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)
