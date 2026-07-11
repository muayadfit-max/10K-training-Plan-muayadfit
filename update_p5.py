import re
import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. Update Hero HTML
old_hero_html = """    <!-- Hero -->
    <header class="hero">
        <div class="container">
            <h1 data-i18n="hero_title">Discover Your Ideal <span>10K Plan</span></h1>
            <p data-i18n="hero_sub">Expert, science-based running programs designed for the Gulf climate. Find the perfect progression for your current fitness level in 30 seconds.</p>
            <a href="#assessment" class="btn btn-primary" data-i18n="hero_cta">Start Free Assessment</a>
        </div>
    </header>"""

new_hero_html = """    <!-- Hero -->
    <header class="hero">
        <div class="container hero-container">
            <div class="hero-content">
                <h1 data-i18n="hero_title">Discover Your Ideal <span>10K Plan</span></h1>
                <p data-i18n="hero_sub" class="hero-subtext">Expert, science-based running programs designed for the Gulf climate. Find the perfect progression for your current fitness level in 30 seconds.</p>
                <a href="#assessment" class="btn btn-primary" data-i18n="hero_cta">Start Free Assessment</a>
            </div>
            <div class="hero-image">
                <img src="Hero%20image.jpg" alt="Muayad Fit 10K Plan" />
            </div>
        </div>
    </header>"""
html = html.replace(old_hero_html, new_hero_html)

# 2. Update Hero CSS
old_hero_css = """        /* Hero */
        .hero {
            padding-top: 140px;
            padding-bottom: 80px;
            background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 100%);
            text-align: center;
        }

        .hero h1 {
            font-size: clamp(2.5rem, 5vw, 4.5rem);
            margin-bottom: 24px;
            letter-spacing: -1px;
            color: var(--black);
            max-width: 900px;
            margin-inline: auto;
        }

        .hero h1 span {
            color: var(--primary);
        }

        .hero p {
            font-size: clamp(1.1rem, 2vw, 1.3rem);
            color: var(--gray-600);
            max-width: 700px;
            margin-inline: auto;
            margin-bottom: 40px;
            line-height: 1.6;
        }"""

new_hero_css = """        /* Hero */
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
html = html.replace(old_hero_css, new_hero_css)

# 3. Add Mobile Adjustments for Hero Flex layout
mobile_css = """
            .hero-container {
                flex-direction: column;
                text-align: center;
            }
            [dir="rtl"] .hero-container { text-align: center; }
            .hero-content { margin-bottom: 16px; }
            .hero { padding-top: 120px; padding-bottom: 60px; }"""
html = html.replace('/* Mobile Adjustments */', '/* Mobile Adjustments */' + mobile_css)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Updates applied successfully.")
