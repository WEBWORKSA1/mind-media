#!/usr/bin/env python3
"""Mind.Media static site generator. Run: python3 _build/build.py  (outputs to repo root)"""
import os, json, html
from articles import ARTICLES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://webworksa1.github.io/mind-media"   # change to https://mind.media once the domain points here
BRAND = "Mind.Media"
INTEREST = "https://web.works/contact"

NAV = [("index.html", "Home"), ("articles.html", "Read"), ("videos.html", "Watch"), ("tools.html", "Tools"),
       ("find-support.html", "Find Support"), ("for-business.html", "For Business"), ("contests.html", "Contests"),
       ("careers.html", "Careers"), ("donate.html", "Support Us")]

def head(title, desc, path, p, extra_ld=None, og_type="website"):
    url = f"{SITE}/{path}".replace("/index.html", "/")
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": SITE + "/",
           "logo": SITE + "/assets/img/icon.svg"},
          {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": SITE + "/",
           "potentialAction": {"@type": "SearchAction", "target": SITE + "/articles.html?q={q}", "query-input": "required name=q"}}]
    if extra_ld: ld.append(extra_ld)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#5b3df5">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}assets/img/icon.svg" type="image/svg+xml">
<link rel="manifest" href="{p}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/css/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership — <a href="{INTEREST}" target="_blank" rel="noopener">web.works/contact</a></div>
"""

def header(active, p):
    cur = ' aria-current="page"'
    items = "".join(f'<li><a href="{p}{h}"{cur if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f"""<header class="site-header"><div class="container nav">
<a class="logo" href="{p}index.html" aria-label="{BRAND} home"><span class="logo-mark"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8" fill="none" stroke="#fff" stroke-width="2.4"/><path d="M12 4a8 8 0 0 1 0 16z" fill="#fff"/></svg></span><span>Mind<b>.Media</b></span></a>
<nav aria-label="Main"><ul class="nav-links" id="navLinks">{items}</ul></nav>
<div class="nav-cta"><button class="icon-btn" id="themeToggle" aria-label="Toggle dark mode"><svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z" fill="currentColor"/></svg></button>
<a class="btn btn-grad btn-sm btn-sm-hide" href="{p}find-support.html">Get matched</a>
<button class="icon-btn menu-btn" id="menuBtn" aria-label="Menu" aria-expanded="false" aria-controls="navLinks">☰</button></div>
</div></header>
<main id="main">
"""

def footer(p, tools=False):
    return f"""</main>
<footer class="site-footer"><div class="container">
<div class="footer-grid">
<div><a class="logo" href="{p}index.html" style="color:#fff"><span class="logo-mark"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8" fill="none" stroke="#fff" stroke-width="2.4"/><path d="M12 4a8 8 0 0 1 0 16z" fill="#fff"/></svg></span><span>Mind<b>.Media</b></span></a>
<p style="margin-top:14px;max-width:320px">Independent media for a healthier mind — science-backed stories, videos, free tools and a trusted path to real support.</p>
<form class="newsletter" data-form="Newsletter" style="margin-top:16px" data-success="You're in! Watch your inbox for The Weekly Reset.">
<label class="sr-only" for="fnl">Email</label><input id="fnl" type="email" name="email" placeholder="Your email" required>
<div class="hp"><input name="_honey" tabindex="-1" autocomplete="off"></div>
<button class="btn btn-primary btn-sm" type="submit">Subscribe</button></form>
<div class="form-status" style="margin-top:8px"></div>
<div class="socials"><a href="https://www.youtube.com/@MindMediaHub" target="_blank" rel="noopener" aria-label="YouTube">YT</a><a href="#" aria-label="Instagram">IG</a><a href="#" aria-label="TikTok">TT</a><a href="#" aria-label="LinkedIn">in</a><a href="#" aria-label="X">X</a></div>
</div>
<div><h4>Explore</h4><ul><li><a href="{p}articles.html">Articles</a></li><li><a href="{p}videos.html">Videos &amp; Podcasts</a></li><li><a href="{p}tools.html">Free Tools</a></li><li><a href="{p}contests.html">Contests</a></li></ul></div>
<div><h4>Get Support</h4><ul><li><a href="{p}find-support.html">Find a Therapist or Coach</a></li><li><a href="{p}for-business.html">Workplace Wellbeing</a></li><li><a href="{p}for-practitioners.html">List Your Practice</a></li><li><a href="{p}find-support.html#crisis">Crisis Resources</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="{p}about.html">About</a></li><li><a href="{p}careers.html">Careers &amp; Creators</a></li><li><a href="{p}advertise.html">Advertise / Sponsor</a></li><li><a href="{p}donate.html">Support Us</a></li><li><a href="{p}contact.html">Contact</a></li></ul></div>
<div><h4>Legal</h4><ul><li><a href="{p}privacy.html">Privacy Policy</a></li><li><a href="{p}terms.html">Terms of Use</a></li><li><a href="{p}disclaimer.html">Medical Disclaimer</a></li><li><a href="{p}legal.html">Trademark &amp; Copyright</a></li></ul></div>
</div>
<div class="footer-bottom"><span>© <span data-year></span> {BRAND}. All rights reserved. Content is educational and not a substitute for professional care. In crisis? Call your local emergency number (US/Canada: call or text 988).</span>
<span>{BRAND} is an independent publication and is not affiliated with any company named “Mind Media” or similar. <a href="{p}legal.html">Details</a></span></div>
</div></footer>
<a class="btn btn-grad float-cta" href="{p}find-support.html">💬 Get matched free</a>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie consent"><strong>We value your privacy</strong>
<p class="form-note" style="margin-top:6px">We use cookies for analytics and to show ads that keep {BRAND} free. See our <a href="{p}privacy.html">Privacy Policy</a>.</p>
<div class="row"><button class="btn btn-primary btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div></div>
<script src="{p}assets/js/main.js" defer></script>{f'<script src="{p}assets/js/tools.js" defer></script>' if tools else ''}
</body></html>
"""

def ad(slot="", cls=""):
    return f'<div class="ad-slot {cls}" data-slot="{slot}" aria-label="Advertisement">Advertisement</div>'

def status():
    return '<div class="hp"><input name="_honey" tabindex="-1" autocomplete="off"></div><div class="form-status" role="status"></div>'

def consent_box():
    return '<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to the <a href="privacy.html">Privacy Policy</a> and to be contacted about my request.</label>'

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def page(path, title, desc, body, active=None, tools=False, ld=None):
    p = "../" if "/" in path else ""
    write(path, head(title, desc, path, p, ld) + header(active or path, p) + body + footer(p, tools))

def hero(eyebrow, h1, lead, crumbs=None):
    c = f'<div class="breadcrumb"><a href="index.html">Home</a> / {crumbs}</div>' if crumbs else ""
    return f'<section class="page-hero"><div class="container">{c}<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lead">{lead}</p></div></section>'

def article_card(a, p=""):
    return f"""<article class="card article-card reveal" data-cat="{a['cat']}"><div class="thumb {a['t']}" aria-hidden="true">{a['icon']}</div>
<div class="body"><span class="tag">{a['tag']}</span><h3><a class="stretched" href="{p}articles/{a['slug']}.html">{a['title']}</a></h3><p>{a['desc']}</p><div class="meta">{a['mins']} min read · {a['date']}</div></div></article>"""

VIDEOS = [("iCvmsMzlF7o", "The Power of Vulnerability — Brené Brown", "psychology"),
          ("RcGyVTAoXEU", "How to Make Stress Your Friend — Kelly McGonigal", "stress"),
          ("qzR62JJCMBQ", "All It Takes Is 10 Mindful Minutes — Andy Puddicombe", "mindfulness"),
          ("F2hc2FLOdhI", "How to Practice Emotional First Aid — Guy Winch", "psychology"),
          ("5MuIMqhT8DM", "Sleep Is Your Superpower — Matt Walker", "sleep"),
          ("fLJsdqxnZb0", "The Happy Secret to Better Work — Shawn Achor", "work"),
          ("8KkKuTCFvzI", "What Makes a Good Life? — Robert Waldinger", "psychology"),
          ("arj7oStGLkU", "Inside the Mind of a Master Procrastinator — Tim Urban", "focus")]

def video_card(v):
    return f'<div class="card reveal" data-cat="{v[2]}" style="padding:14px"><div class="video" data-yt="{v[0]}" data-title="{html.escape(v[1])}"></div><h3 style="font-size:1.05rem;margin:12px 4px 4px">{v[1]}</h3><p class="meta" style="margin:0 4px">Featured talk · via YouTube</p></div>'

# Reusable lead form (multi-step matching) ---------------------------------
MATCH_FORM = f"""<form class="form" data-form="Support Match Request" data-success="Thank you. A match coordinator will email you options within 1 business day. If you are in crisis, please contact emergency services or call/text 988 (US/Canada) now." novalidate>
<div class="steps-bar"><i></i><i></i><i></i></div>
<div class="step"><h3>What kind of support are you looking for?</h3>
<div class="choice-grid">
<label class="choice"><input type="radio" name="support_type" value="Therapy / counselling" required><span>🧠 Therapy / counselling</span></label>
<label class="choice"><input type="radio" name="support_type" value="Life or career coaching"><span>🚀 Life or career coaching</span></label>
<label class="choice"><input type="radio" name="support_type" value="Couples / family"><span>💞 Couples / family</span></label>
<label class="choice"><input type="radio" name="support_type" value="Psychiatry / medication review"><span>💊 Psychiatry / medication</span></label>
<label class="choice"><input type="radio" name="support_type" value="Team / workplace program"><span>🏢 For my team or company</span></label>
<label class="choice"><input type="radio" name="support_type" value="Not sure yet"><span>🤔 Not sure yet</span></label>
</div>
<div><label for="mf_focus">Main focus</label><select id="mf_focus" name="focus" required><option value="">Choose one</option><option>Anxiety &amp; stress</option><option>Low mood</option><option>Burnout &amp; work</option><option>Relationships</option><option>Sleep</option><option>Grief &amp; loss</option><option>Trauma</option><option>ADHD / focus</option><option>Confidence &amp; growth</option><option>Other</option></select></div>
<div class="step-nav"><span></span><button class="btn btn-primary" data-next>Continue →</button></div></div>
<div class="step"><h3>Your preferences</h3>
<div class="form-row"><div><label for="mf_format">Format</label><select id="mf_format" name="format"><option>Online video</option><option>In person</option><option>Phone</option><option>Chat / text</option><option>No preference</option></select></div>
<div><label for="mf_budget">Budget per session</label><select id="mf_budget" name="budget"><option>Insurance / EAP</option><option>Under $60</option><option>$60–$120</option><option>$120–$200</option><option>$200+</option><option>Need free / low-cost options</option></select></div></div>
<div class="form-row"><div><label for="mf_loc">Country / region</label><input id="mf_loc" name="location" placeholder="e.g. Ontario, Canada" required></div>
<div><label for="mf_lang">Language</label><input id="mf_lang" name="language" placeholder="English"></div></div>
<div><label for="mf_when">How soon?</label><select id="mf_when" name="urgency"><option>This week</option><option>Within 2 weeks</option><option>This month</option><option>Just exploring</option></select></div>
<div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-primary" data-next>Continue →</button></div></div>
<div class="step"><h3>Where should we send your matches?</h3>
<div class="form-row"><div><label for="mf_name">First name</label><input id="mf_name" name="name" required autocomplete="given-name"></div>
<div><label for="mf_email">Email</label><input id="mf_email" type="email" name="email" required autocomplete="email"></div></div>
<div><label for="mf_phone">Phone (optional)</label><input id="mf_phone" type="tel" name="phone" autocomplete="tel"></div>
<div><label for="mf_note">Anything else? (optional)</label><textarea id="mf_note" name="notes" placeholder="Gender preference, specialties, schedule…"></textarea></div>
{consent_box()}
<div class="step-nav"><button class="btn btn-ghost" data-prev>← Back</button><button class="btn btn-grad" type="submit">Get my free matches</button></div>
<p class="form-note">Free, no obligation. Your details are shared only with the providers you approve.</p></div>
{status()}
</form>"""

def build():
    A = ARTICLES
    # ---------------- HOME ----------------
    home = f"""
<section class="hero"><div class="container hero-grid">
<div><span class="eyebrow">Independent media for a healthier mind</span>
<h1>Understand your mind. <span>Upgrade your life.</span></h1>
<p class="lead">Science-backed articles, expert videos, free interactive tools and a fast, private path to the right therapist, coach or workplace program — all in one place.</p>
<div class="hero-actions"><a class="btn btn-grad" href="find-support.html">Get matched with support — free</a><a class="btn btn-ghost" href="tools.html">Try the free tools</a></div>
<div class="hero-stats"><div><strong>7</strong><span>free mind tools</span></div><div><strong>2 min</strong><span>to get matched</span></div><div><strong>100%</strong><span>free to read</span></div></div>
</div>
<div class="hero-card"><h3 style="margin-bottom:6px">60-second wellbeing check-in</h3><p class="form-note" style="margin-bottom:12px">How have you felt over the past two weeks?</p>
<form id="checkin" class="form">
{''.join(f'<div><label>{q}</label><select><option value="4">Almost always</option><option value="3">Often</option><option value="2" selected>Sometimes</option><option value="1">Rarely</option><option value="0">Almost never</option></select></div>' for q in ["I felt calm and relaxed","I had energy for things I care about","I slept well and woke rested","I felt connected to people around me"])}
<button class="btn btn-primary btn-block" type="submit">See my score</button></form>
<div id="checkinOut" class="result" style="display:none;margin-top:14px"></div></div>
</div></section>

<div class="container"><p class="logos" aria-label="Topics"><span>Psychology</span><span>Neuroscience</span><span>Mindfulness</span><span>Sleep</span><span>Focus</span><span>Relationships</span><span>Work</span></p></div>
{ad("home-top")}

<section><div class="container">
<div class="section-head"><div><span class="eyebrow">Latest</span><h2>Read: fresh from the Mind.Media desk</h2></div><a class="btn btn-ghost btn-sm" href="articles.html">All articles →</a></div>
<div class="grid g3">{''.join(article_card(a) for a in A)}</div></div></section>

<section class="alt"><div class="container">
<div class="lead-band reveal"><div><span class="eyebrow" style="background:rgba(255,255,255,.18);color:#fff">Free matching service</span>
<h2>Find the right therapist, coach or program — in 2 minutes</h2>
<p style="margin-top:12px">Skip hours of searching directories. Tell us what you need and we'll send hand-picked options that fit your concern, budget, language and schedule.</p>
<ul><li>Licensed therapists, psychiatrists &amp; certified coaches</li><li>Online or in-person, insurance and low-cost options</li><li>Private, free and no obligation</li></ul></div>
<div class="hero-card">{MATCH_FORM}</div></div>
</div></section>

<section><div class="container">
<div class="section-head"><div><span class="eyebrow">Watch</span><h2>Talks that change how you think</h2></div><a class="btn btn-ghost btn-sm" href="videos.html">Video hub →</a></div>
<div class="grid g4">{''.join(video_card(v) for v in VIDEOS[:4])}</div></div></section>
{ad("home-mid")}

<section class="alt"><div class="container">
<div class="section-head"><div><span class="eyebrow">Free tools</span><h2>Train your mind in minutes a day</h2><p class="lead">No sign-up. Your data never leaves your device.</p></div><a class="btn btn-ghost btn-sm" href="tools.html">Open all tools →</a></div>
<div class="grid g4">
{''.join(f'<div class="card reveal"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p><a class="stretched" href="tools.html#{h}" aria-label="{t}"></a></div>' for i,t,d,h in [("🫁","Breathing Coach","Box, 4-7-8 and coherent breathing with a visual pacer.","breathing"),("⏱️","Focus Timer","Pomodoro-style deep-work sessions with streaks.","focus"),("😊","Mood Tracker","One tap a day. See your weekly pattern.","mood"),("🌙","Sleep Calculator","Bedtimes that line up with 90-minute cycles.","sleep"),("🔥","Burnout Meter","A quick read on your current strain level.","burnout"),("🙏","Gratitude Journal","Three good things, private to your device.","gratitude"),("📊","Wellbeing Check-in","A 60-second snapshot with next steps.","checkin-tool"),("🏆","Monthly Challenge","Join the community challenge and win prizes.","")])}
</div></div></section>

<section><div class="container grid g3">
<div class="card reveal"><div class="ico">🏢</div><h3>For employers</h3><p>Workshops, manager training and wellbeing programs that reduce burnout and turnover.</p><a class="btn btn-primary btn-sm" href="for-business.html" style="margin-top:12px">Request a proposal</a></div>
<div class="card reveal"><div class="ico">🩺</div><h3>For practitioners</h3><p>Therapists and coaches: receive pre-qualified client requests and grow your practice.</p><a class="btn btn-primary btn-sm" href="for-practitioners.html" style="margin-top:12px">Apply to be listed</a></div>
<div class="card reveal"><div class="ico">📣</div><h3>For brands</h3><p>Reach a mindful, high-intent audience with sponsorships, newsletters and video integrations.</p><a class="btn btn-primary btn-sm" href="advertise.html" style="margin-top:12px">View media kit</a></div>
</div></section>

<section class="alt"><div class="container grid g2" style="align-items:center">
<div class="reveal"><span class="eyebrow">Contest</span><h2>The Calm Creator Challenge</h2><p class="lead" style="margin:12px 0 18px">Share a 60-second video, poem, photo or illustration about what helps your mind. Winners get cash prizes, features and a spot on our creator roster.</p>
<div class="countdown" data-countdown="2026-12-15T23:59:00"></div><a class="btn btn-warm" href="contests.html" style="margin-top:18px">Enter now</a></div>
<div class="card reveal"><span class="eyebrow">Support independent media</span><h3>Keep Mind.Media free for everyone</h3><p>Reader support funds new tools, expert reviews, contests and our creator fund. Every contribution helps.</p>
<div style="margin:16px 0"><div class="progress"><i style="width:38%"></i></div><p class="meta">38% of this quarter's goal</p></div>
<a class="btn btn-grad" href="donate.html">Support us</a> <a class="btn btn-ghost" href="donate.html#membership">Become a member</a></div>
</div></section>

<section><div class="container center"><span class="eyebrow">The Weekly Reset</span><h2>One email. Five minutes. A calmer week.</h2>
<p class="lead" style="margin:12px auto 20px">The best new research, one tool to try and one talk worth watching — every Sunday.</p>
<form class="newsletter" data-form="Newsletter" style="margin:0 auto" data-success="You're in! Watch your inbox for The Weekly Reset."><label class="sr-only" for="hnl">Email</label><input id="hnl" type="email" name="email" placeholder="you@example.com" required><div class="hp"><input name="_honey" tabindex="-1" autocomplete="off"></div><button class="btn btn-grad" type="submit">Subscribe free</button></form><div class="form-status" style="max-width:520px;margin:10px auto 0"></div>
</div></section>

<section class="alt"><div class="container" style="max-width:860px"><div class="center"><span class="eyebrow">FAQ</span><h2>Common questions</h2></div><div style="margin-top:24px">
<details><summary>Is Mind.Media free?</summary><p>Yes. All articles, videos and tools are free, supported by advertising, sponsorships and reader contributions.</p></details>
<details><summary>How does the support matching work?</summary><p>You answer a few questions about your needs, budget and format. We review your request and email suitable options from our network of licensed professionals and certified coaches. It's free and there's no obligation.</p></details>
<details><summary>Is this a replacement for therapy or medical care?</summary><p>No. Our content and tools are educational. For diagnosis or treatment, speak with a qualified professional.</p></details>
<details><summary>What if I'm in crisis?</summary><p>Please contact your local emergency number now. In the US and Canada, call or text 988. See our <a href="find-support.html#crisis">crisis resources</a>.</p></details>
</div></div></section>

<div class="modal" id="leadModal" role="dialog" aria-modal="true" aria-label="Get The Weekly Reset"><div class="card"><button class="icon-btn" data-close style="position:absolute;right:14px;top:14px" aria-label="Close">✕</button>
<span class="eyebrow">Before you go</span><h3>Get our free 7-Day Calm Reset</h3><p style="margin:8px 0 14px">A short daily email plan with one tool and one habit each day.</p>
<form class="form" data-form="Lead Magnet — 7-Day Calm Reset" data-success="Check your inbox — Day 1 is on its way."><input type="email" name="email" placeholder="Your email" required aria-label="Email">{status()}<button class="btn btn-grad btn-block" type="submit">Send me the plan</button></form></div></div>
"""
    page("index.html", "Mind.Media — Psychology, Mindfulness & Mental Wellbeing Media + Free Tools",
         "Science-backed articles, expert videos and free tools for a healthier mind — plus free matching with therapists, coaches and workplace wellbeing programs.",
         home, tools=True)

    # ---------------- ARTICLES ----------------
    cats = [("all", "All"), ("mindfulness", "Mindfulness"), ("psychology", "Psychology"), ("sleep", "Sleep"), ("focus", "Focus"), ("work", "Work & Burnout"), ("therapy", "Therapy")]
    body = hero("The Library", "Articles for a healthier mind", "Clear, practical, research-informed reads on psychology, mindfulness, sleep, focus and work.", "Articles") + f"""
<section style="padding-top:10px"><div class="container">
<div class="section-head"><div class="filters" data-filter-group>{''.join(f'<button class="pill{" active" if k=="all" else ""}" data-f="{k}">{n}</button>' for k,n in cats)}</div>
<input class="search" id="librarySearch" type="search" placeholder="Search articles…" aria-label="Search articles"></div>
<div class="grid g3">{''.join(article_card(a) for a in A)}</div>
{ad("articles-mid")}
<div class="card center" style="margin-top:20px"><h3>Want to write for Mind.Media?</h3><p>We pay contributors and feature licensed experts. <a href="careers.html#write">Pitch us →</a></p></div>
</div></section>"""
    page("articles.html", "Articles — Psychology, Sleep, Focus & Mindfulness | Mind.Media", "Browse practical, research-informed articles on anxiety, burnout, sleep, focus, mindfulness and therapy.", body)

    for i, a in enumerate(A):
        rel = [x for x in A if x is not a][:3]
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
              "datePublished": a["date"], "author": {"@type": "Organization", "name": "Mind.Media Editorial"},
              "publisher": {"@type": "Organization", "name": BRAND}, "mainEntityOfPage": f"{SITE}/articles/{a['slug']}.html"}
        parts = a["body"].split("</h2>", 2)
        body_html = a["body"]
        # insert an in-article ad after the second section heading's first paragraph
        idx = body_html.find("<h2", body_html.find("<h2") + 1)
        if idx > 0: body_html = body_html[:idx] + ad("in-article", "ad-inline") + body_html[idx:]
        b = f"""<div class="readbar"></div>
<section style="padding-top:40px"><div class="container"><article class="article">
<div class="breadcrumb"><a href="../index.html">Home</a> / <a href="../articles.html">Articles</a> / {a['tag']}</div>
<span class="tag">{a['tag']}</span><h1>{a['title']}</h1>
<div class="byline"><span>By Mind.Media Editorial</span><span>·</span><span>{a['date']}</span><span>·</span><span>{a['mins']} min read</span></div>
<div class="share"><button class="btn btn-ghost btn-sm" data-share="x">Share on X</button><button class="btn btn-ghost btn-sm" data-share="fb">Facebook</button><button class="btn btn-ghost btn-sm" data-share="li">LinkedIn</button><button class="btn btn-ghost btn-sm" data-share="wa">WhatsApp</button><button class="btn btn-ghost btn-sm" data-share="copy">Copy link</button></div>
<div class="crisis"><strong>Educational content.</strong> Not medical advice. If you are in crisis, call your local emergency number (US/Canada: call or text 988).</div>
{body_html}
<div class="lead-band" style="margin:36px 0;grid-template-columns:1fr"><div><h2 style="font-size:1.6rem">Ready for personalised support?</h2><p style="margin-top:8px">Get matched with a licensed therapist or certified coach — free, private, 2 minutes.</p><a class="btn btn-ghost" href="../find-support.html" style="margin-top:14px">Get my free matches →</a></div></div>
<div class="card" style="margin-bottom:20px"><h3>Get The Weekly Reset</h3><form class="newsletter" data-form="Newsletter (article)" style="margin-top:10px"><input type="email" name="email" placeholder="you@example.com" required aria-label="Email"><div class="hp"><input name="_honey" tabindex="-1" autocomplete="off"></div><button class="btn btn-primary" type="submit">Subscribe</button></form><div class="form-status" style="margin-top:8px"></div></div>
<p class="form-note">Reviewed for accuracy by the Mind.Media editorial team. Found an error? <a href="../contact.html">Tell us</a>.</p>
</article>
{ad("article-bottom")}
<h2 style="margin:30px 0 18px;text-align:center">Keep reading</h2><div class="grid g3">{''.join(article_card(x, "../") for x in rel)}</div>
</div></section>"""
        page(f"articles/{a['slug']}.html", f"{a['title']} | Mind.Media", a["desc"], b, active="articles.html", ld=ld)

    # ---------------- VIDEOS ----------------
    vc = [("all", "All"), ("psychology", "Psychology"), ("stress", "Stress"), ("mindfulness", "Mindfulness"), ("sleep", "Sleep"), ("work", "Work"), ("focus", "Focus")]
    body = hero("Watch & Listen", "The Mind.Media video hub", "Hand-picked talks, guided sessions and our own originals. Subscribe on YouTube for new episodes every week.", "Videos") + f"""
<section style="padding-top:10px"><div class="container">
<div class="section-head"><div class="filters" data-filter-group>{''.join(f'<button class="pill{" active" if k=="all" else ""}" data-f="{k}">{n}</button>' for k,n in vc)}</div>
<a class="btn btn-warm btn-sm" href="https://www.youtube.com/@MindMediaHub" target="_blank" rel="noopener">▶ Subscribe on YouTube</a></div>
<div class="grid g3">{''.join(video_card(v) for v in VIDEOS)}</div>
{ad("videos-mid")}
<div class="grid g3" style="margin-top:30px">
<div class="card"><div class="ico">🎧</div><h3>Mind.Media Podcast</h3><p>Weekly 20-minute conversations with psychologists, researchers and creators. Launching soon on all major platforms.</p><a class="btn btn-ghost btn-sm" href="#notify" style="margin-top:10px">Get notified</a></div>
<div class="card"><div class="ico">🧘</div><h3>Guided sessions</h3><p>5–15 minute guided breathing, body-scan and sleep wind-down audio. Try the live <a href="tools.html#breathing">Breathing Coach</a>.</p></div>
<div class="card"><div class="ico">🎬</div><h3>Create with us</h3><p>Are you a video creator or expert? Pitch a series, collaborate or sponsor an episode.</p><a class="btn btn-ghost btn-sm" href="careers.html#creators" style="margin-top:10px">Pitch a series</a></div>
</div>
<div class="card center" id="notify" style="margin-top:30px"><h3>Be first to hear new episodes</h3><form class="newsletter" data-form="Podcast Waitlist" style="margin:12px auto 0"><input type="email" name="email" placeholder="you@example.com" required aria-label="Email"><div class="hp"><input name="_honey" tabindex="-1" autocomplete="off"></div><button class="btn btn-primary" type="submit">Notify me</button></form><div class="form-status" style="max-width:520px;margin:10px auto 0"></div></div>
<p class="form-note" style="margin-top:20px">Third-party videos are embedded from YouTube and remain the property of their respective owners. Embedding does not imply endorsement.</p>
</div></section>"""
    page("videos.html", "Video Hub — Psychology & Mindfulness Talks | Mind.Media", "Watch hand-picked talks on stress, sleep, vulnerability, focus and happiness, plus Mind.Media originals and guided sessions.", body)

    # ---------------- TOOLS ----------------
    body = hero("Free tools", "Your mind gym", "Seven free interactive tools. No accounts, no tracking of your entries — everything stays on your device.", "Tools") + f"""
<section style="padding-top:10px"><div class="container grid g2">
<div class="card tool" id="breathing"><h2 style="font-size:1.5rem">🫁 Breathing Coach</h2><p>Follow the orb. Expand on the inhale, soften on the exhale.</p>
<select id="breathPattern" aria-label="Breathing pattern"><option value="box">Box breathing 4-4-4-4 (focus)</option><option value="relax">4-7-8 (sleep &amp; wind-down)</option><option value="calm">Coherent 5-5 (balance)</option></select>
<div class="breath-orb" id="orb">Ready</div><p class="center meta">Cycles completed: <b id="breathCycles">0</b></p><button class="btn btn-grad" id="breathBtn">Start breathing</button></div>
<div class="card tool" id="focus"><h2 style="font-size:1.5rem">⏱️ Focus Timer</h2><p id="focusMode">Focus session</p>
<div class="timer" id="focusTime">25:00</div>
<div class="form-row"><select id="focusLen" aria-label="Session length"><option value="25">25 min</option><option value="50">50 min</option><option value="15">15 min</option><option value="90">90 min</option></select><div style="display:flex;gap:8px"><button class="btn btn-primary" id="focusStart" style="flex:1">Start</button><button class="btn btn-ghost" id="focusReset">Reset</button></div></div>
<p class="meta">Sessions completed on this device: <b id="focusCount">0</b></p></div>
<div class="card tool" id="mood"><h2 style="font-size:1.5rem">😊 Mood Tracker</h2><p>How are you feeling today?</p>
<div class="mood-row" id="moodRow"><button data-v="1" aria-label="Very low">😞</button><button data-v="2" aria-label="Low">🙁</button><button data-v="3" aria-label="Okay">😐</button><button data-v="4" aria-label="Good">🙂</button><button data-v="5" aria-label="Great">😄</button></div>
<div class="bars" id="moodBars"></div><p class="meta">7-day average: <b id="moodAvg">–</b> / 5</p></div>
<div class="card tool" id="sleep"><h2 style="font-size:1.5rem">🌙 Sleep Cycle Calculator</h2><p>What time do you need to wake up?</p>
<div class="form-row"><input type="time" id="wakeTime" value="07:00" aria-label="Wake time"><button class="btn btn-primary" id="sleepBtn">Calculate bedtimes</button></div><div class="result" id="sleepOut">Your ideal bedtimes will appear here.</div></div>
<div class="card tool" id="burnout"><h2 style="font-size:1.5rem">🔥 Burnout Risk Meter</h2><p>Slide to rate the past month (0 = never, 10 = constantly).</p>
{''.join(f'<div><label>{q}</label><input type="range" min="0" max="10" value="3"></div>' for q in ["I feel drained before the day starts","I feel cynical or detached about my work","My effort doesn't feel like it matters","I can't switch off after work","I've pulled back from people and hobbies"])}
<div class="progress"><i id="burnoutBar" style="width:30%"></i></div><p><b id="burnoutPct">30%</b> — <span id="burnoutMsg">Low strain. Keep recovery rituals in your calendar.</span></p><a href="articles/early-signs-of-burnout.html">Read: 12 early signs of burnout →</a></div>
<div class="card tool" id="gratitude"><h2 style="font-size:1.5rem">🙏 Gratitude Journal</h2><p>Write one good thing from today.</p>
<form id="gratForm" class="newsletter" style="max-width:none"><input id="gratText" maxlength="200" placeholder="Something that went well…" aria-label="Gratitude entry"><button class="btn btn-primary" type="submit">Save</button></form><ul id="gratList" style="list-style:none;display:grid;gap:6px"></ul></div>
</div>
{ad("tools-mid")}
<div class="container" id="checkin-tool"><div class="lead-band"><div><h2>Want a human to help?</h2><p style="margin-top:10px">Tools build habits; people help you work through what's underneath. Get matched with a licensed therapist or certified coach — free.</p></div><div><a class="btn btn-ghost" href="find-support.html">Get matched in 2 minutes →</a></div></div></div>
</section>"""
    page("tools.html", "Free Mental Wellbeing Tools — Breathing, Focus, Mood, Sleep | Mind.Media", "Free interactive tools: breathing coach, focus timer, mood tracker, sleep cycle calculator, burnout meter and gratitude journal.", body, tools=True)

    # ---------------- FIND SUPPORT (LEAD GEN) ----------------
    body = hero("Free matching service", "Find the right support — fast", "Tell us what you need. We'll send hand-picked therapists, psychiatrists or coaches who fit your concern, budget, format and language.", "Find Support") + f"""
<section style="padding-top:10px"><div class="container grid g2" style="align-items:start">
<div class="card" style="padding:30px">{MATCH_FORM}</div>
<div class="grid" style="gap:16px">
<div class="card"><h3>How it works</h3><ol style="padding-left:20px;margin-top:8px;color:var(--ink-2)"><li><b>Tell us</b> what you're looking for (2 min).</li><li><b>We review</b> your request against our vetted network.</li><li><b>You receive</b> 2–3 options by email, usually within 1 business day.</li><li><b>You choose</b> — no obligation, no fees from us.</li></ol></div>
<div class="card"><h3>Why people use Mind.Media matching</h3><ul style="padding-left:20px;margin-top:8px;color:var(--ink-2)"><li>Licensed professionals &amp; certified coaches</li><li>Online, in-person, insurance and sliding-scale options</li><li>Specialties: anxiety, burnout, relationships, trauma, ADHD and more</li><li>Private by design — shared only with providers you approve</li></ul></div>
<div class="crisis" id="crisis"><strong>In crisis or thinking about harming yourself?</strong> Do not wait for a match. Call your local emergency number. <b>US &amp; Canada:</b> call or text 988. <b>UK &amp; Ireland:</b> Samaritans 116 123. <b>India:</b> Tele-MANAS 14416. Elsewhere, find a line at <a href="https://findahelpline.com" target="_blank" rel="noopener">findahelpline.com</a>.</div>
</div></div></section>
<section class="alt"><div class="container"><div class="center"><span class="eyebrow">Browse by need</span><h2>What can support help with?</h2></div>
<div class="grid g4" style="margin-top:26px">{''.join(f'<div class="card"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in [("😰","Anxiety & stress","Worry, panic, overwhelm and chronic stress."),("🌧️","Low mood","Sadness, low motivation and loss of interest."),("🔥","Burnout","Exhaustion, cynicism and work overload."),("💞","Relationships","Couples, family and communication."),("🌙","Sleep","Insomnia and racing thoughts at night."),("🕊️","Grief","Loss, change and life transitions."),("⚡","ADHD & focus","Attention, organisation and follow-through."),("🚀","Growth & confidence","Career, performance and self-esteem.")])}</div></div></section>
<section><div class="container" style="max-width:860px"><h2 class="center">Matching FAQ</h2><div style="margin-top:20px">
<details><summary>Does this cost anything?</summary><p>No. Matching is free for you. Providers may pay a listing fee; that never affects which options we recommend first.</p></details>
<details><summary>Is Mind.Media a healthcare provider?</summary><p>No. We are a media and referral service. Care is delivered by independent licensed professionals and coaches.</p></details>
<details><summary>Which countries do you cover?</summary><p>We focus on the US, Canada, UK, India and Australia, with online options available in many other regions.</p></details>
</div></div></section>"""
    page("find-support.html", "Find a Therapist or Coach — Free Matching | Mind.Media", "Get matched free with licensed therapists, psychiatrists and certified coaches. Online or in-person, insurance and low-cost options. 2-minute form.", body)

    # ---------------- FOR BUSINESS (B2B LEAD GEN) ----------------
    body = hero("Workplace wellbeing", "Healthier minds. Stronger teams.", "Evidence-informed workshops, manager training and digital wellbeing programs that help teams prevent burnout and do their best work.", "For Business") + f"""
<section style="padding-top:10px"><div class="container grid g3">
{''.join(f'<div class="card reveal"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in [("🎤","Live workshops","60–90 minute sessions on stress, focus, burnout prevention, sleep and resilience — virtual or on-site."),("🧭","Manager training","Equip leaders to spot early warning signs and have supportive conversations."),("📱","Wellbeing hub","A white-label version of our tools, content and challenges for your employees."),("📈","Pulse surveys","Anonymous wellbeing check-ins with team-level reporting."),("🤝","Coaching access","Discounted 1:1 coaching and a fast referral path to licensed care."),("🏆","Team challenges","30-day focus, sleep and movement challenges with prizes.")])}
</div></section>
<section class="alt"><div class="container grid g2" style="align-items:start">
<div><span class="eyebrow">Request a proposal</span><h2>Tell us about your team</h2><p class="lead" style="margin:12px 0 20px">We'll reply within one business day with a tailored plan and pricing.</p>
<div class="table-wrap"><table class="table"><tr><th>Package</th><th>Best for</th><th>Includes</th></tr>
<tr><td><b>Spark</b></td><td>Teams up to 50</td><td>1 workshop + resource kit</td></tr>
<tr><td><b>Thrive</b></td><td>50–500</td><td>Quarterly workshops, manager training, hub access</td></tr>
<tr><td><b>Enterprise</b></td><td>500+</td><td>Full program, surveys, coaching, custom content</td></tr></table></div></div>
<div class="card" style="padding:30px"><form class="form" data-form="B2B Workplace Proposal">
<div class="form-row"><div><label for="b_name">Full name</label><input id="b_name" name="name" required></div><div><label for="b_email">Work email</label><input id="b_email" type="email" name="email" required></div></div>
<div class="form-row"><div><label for="b_co">Company</label><input id="b_co" name="company" required></div><div><label for="b_role">Your role</label><input id="b_role" name="role"></div></div>
<div class="form-row"><div><label for="b_size">Team size</label><select id="b_size" name="team_size"><option>1–49</option><option>50–199</option><option>200–499</option><option>500–1,999</option><option>2,000+</option></select></div>
<div><label for="b_int">Interested in</label><select id="b_int" name="interest"><option>Workshops</option><option>Manager training</option><option>Wellbeing hub</option><option>Full program</option><option>Not sure</option></select></div></div>
<div class="form-row"><div><label for="b_budget">Budget range</label><select id="b_budget" name="budget"><option>Under $2,500</option><option>$2,500–$10,000</option><option>$10,000–$50,000</option><option>$50,000+</option><option>To be defined</option></select></div><div><label for="b_time">Timeline</label><select id="b_time" name="timeline"><option>This month</option><option>This quarter</option><option>Next quarter</option><option>Researching</option></select></div></div>
<div><label for="b_msg">Goals or challenges</label><textarea id="b_msg" name="message"></textarea></div>
{consent_box()}<button class="btn btn-grad" type="submit">Request my proposal</button>{status()}</form></div>
</div></section>"""
    page("for-business.html", "Workplace Mental Wellbeing Programs & Workshops | Mind.Media", "Burnout prevention workshops, manager training, team challenges and a white-label wellbeing hub for companies. Request a tailored proposal.", body)

    # ---------------- FOR PRACTITIONERS ----------------
    body = hero("For therapists & coaches", "Grow your practice with qualified clients", "Join the Mind.Media network to receive pre-qualified client requests and feature your expertise to a large, engaged audience.", "For Practitioners") + f"""
<section style="padding-top:10px"><div class="container grid g2" style="align-items:start">
<div class="grid" style="gap:16px">
<div class="card"><h3>What you get</h3><ul style="padding-left:20px;margin-top:8px;color:var(--ink-2)"><li>Matched client requests by specialty, location, language and budget</li><li>A profile page and expert byline opportunities</li><li>Guest spots on our video and podcast channels</li><li>Workshop and corporate-program referrals</li></ul></div>
<div class="card"><h3>Plans</h3><div class="table-wrap"><table class="table"><tr><th>Plan</th><th>Features</th></tr><tr><td><b>Basic</b> — Free</td><td>Directory profile</td></tr><tr><td><b>Pro</b></td><td>Priority matching, featured profile, analytics</td></tr><tr><td><b>Partner</b></td><td>Pro + expert content, workshops, sponsorship</td></tr></table></div></div>
</div>
<div class="card" style="padding:30px"><form class="form" data-form="Practitioner Application">
<div class="form-row"><div><label for="p_name">Full name</label><input id="p_name" name="name" required></div><div><label for="p_email">Email</label><input id="p_email" type="email" name="email" required></div></div>
<div class="form-row"><div><label for="p_type">Profession</label><select id="p_type" name="profession"><option>Psychologist</option><option>Licensed therapist / counsellor</option><option>Social worker</option><option>Psychiatrist</option><option>Certified coach</option><option>Other</option></select></div><div><label for="p_lic">License / certification #</label><input id="p_lic" name="license"></div></div>
<div class="form-row"><div><label for="p_loc">Location(s) served</label><input id="p_loc" name="location" required></div><div><label for="p_fmt">Formats</label><select id="p_fmt" name="formats"><option>Online</option><option>In person</option><option>Both</option></select></div></div>
<div><label for="p_spec">Specialties</label><input id="p_spec" name="specialties" placeholder="Anxiety, CBT, couples…"></div>
<div class="form-row"><div><label for="p_plan">Plan interest</label><select id="p_plan" name="plan"><option>Basic</option><option>Pro</option><option>Partner</option></select></div><div><label for="p_web">Website</label><input id="p_web" type="url" name="website" placeholder="https://"></div></div>
{consent_box()}<button class="btn btn-grad" type="submit">Apply to join</button>{status()}</form></div>
</div></section>"""
    page("for-practitioners.html", "List Your Practice — Therapists & Coaches | Mind.Media", "Therapists, psychologists and coaches: join the Mind.Media network to receive pre-qualified client requests and grow your practice.", body)

    # ---------------- ADVERTISE ----------------
    body = hero("Advertise & sponsor", "Reach a mindful, high-intent audience", "Sponsorships, newsletter placements, video integrations, tool sponsorships and contest partnerships.", "Advertise") + f"""
<section style="padding-top:10px"><div class="container grid g4">
{''.join(f'<div class="card tier"><div class="ico" style="margin:0 auto">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i,t,d in [("📰","Sponsored content","Expert-reviewed articles and series, clearly labelled."),("✉️","Newsletter","Primary and secondary placements in The Weekly Reset."),("🎬","Video integrations","Pre-roll reads and sponsored episodes on YouTube."),("🧰","Tool sponsorship","'Presented by' placement on a free tool page."),("🏆","Contest partner","Fund prizes and co-brand a monthly challenge."),("🏢","Category exclusivity","Own a topic (e.g. Sleep) for a quarter."),("🎟️","Events & webinars","Co-host a live session with our experts."),("🤝","Affiliate & referral","Performance-based partnerships.")])}
</div></section>
<section class="alt"><div class="container grid g2" style="align-items:start">
<div><h2>Our standards</h2><p class="lead" style="margin:12px 0">We only partner with brands that fit our readers' wellbeing. We decline products making unsupported medical claims. All sponsored content is clearly disclosed.</p>
<p>For domain, website acquisition or strategic partnership enquiries, you can also reach the owner at <a href="{INTEREST}" target="_blank" rel="noopener">web.works/contact</a>.</p></div>
<div class="card" style="padding:30px"><form class="form" data-form="Advertising / Sponsorship Inquiry">
<div class="form-row"><div><label for="a_name">Name</label><input id="a_name" name="name" required></div><div><label for="a_email">Email</label><input id="a_email" type="email" name="email" required></div></div>
<div class="form-row"><div><label for="a_co">Company / brand</label><input id="a_co" name="company" required></div><div><label for="a_type">Interested in</label><select id="a_type" name="interest"><option>Sponsorship</option><option>Advertising</option><option>Newsletter</option><option>Video integration</option><option>Contest partnership</option><option>Partnership / acquisition</option></select></div></div>
<div><label for="a_budget">Budget</label><select id="a_budget" name="budget"><option>Under $1,000</option><option>$1,000–$5,000</option><option>$5,000–$25,000</option><option>$25,000+</option></select></div>
<div><label for="a_msg">Campaign goals</label><textarea id="a_msg" name="message"></textarea></div>
{consent_box()}<button class="btn btn-grad" type="submit">Request media kit</button>{status()}</form></div>
</div></section>"""
    page("advertise.html", "Advertise & Sponsor | Mind.Media", "Sponsorship, newsletter, video and contest partnership opportunities with Mind.Media.", body)

    # ---------------- DONATE ----------------
    body = hero("Support independent media", "Keep Mind.Media free for everyone", "Reader support funds free tools, expert reviews, creator grants, contests and our operations. Thank you for being part of it.", "Support Us") + f"""
<section style="padding-top:10px"><div class="container">
<div class="card" style="max-width:760px;margin:0 auto 30px"><h3>This quarter's goal</h3><div class="progress" style="margin:12px 0"><i style="width:38%"></i></div><p class="meta">38% funded · Goal covers hosting, 2 new tools, 4 expert-reviewed guides and the Calm Creator prize pool.</p></div>
<div class="grid g4">
<div class="card tier"><h3>Supporter</h3><div class="amt">$5</div><p>One-time or monthly. Keeps a tool online for a week.</p><a class="btn btn-ghost btn-block" href="#pledge" data-pay="kofi" style="margin-top:12px">Give $5</a></div>
<div class="card tier featured"><span class="tag">Most popular</span><h3>Member</h3><div class="amt">$10<small style="font-size:1rem">/mo</small></div><p>Ad-light reading, member newsletter and early tool access.</p><a class="btn btn-grad btn-block" href="#pledge" data-pay="stripe" style="margin-top:12px">Become a member</a></div>
<div class="card tier"><h3>Champion</h3><div class="amt">$50</div><p>Funds one creator micro-grant. Name in our supporters list.</p><a class="btn btn-ghost btn-block" href="#pledge" data-pay="paypal" style="margin-top:12px">Give $50</a></div>
<div class="card tier"><h3>Patron</h3><div class="amt">$250+</div><p>Sponsor a contest prize or a free community workshop.</p><a class="btn btn-ghost btn-block" href="#pledge" data-pay="bmac" style="margin-top:12px">Become a patron</a></div>
</div></div></section>
<section class="alt" id="membership"><div class="container grid g2" style="align-items:start">
<div><h2>Where your support goes</h2><div class="grid g2" style="margin-top:18px">
{''.join(f'<div class="card"><div class="kpi">{p}</div><p>{t}</p></div>' for p,t in [("35%","Content & expert review"),("25%","Tools & operations"),("20%","Creators, talent & contests"),("20%","Promotion & outreach")])}</div>
<p class="form-note" style="margin-top:14px">Mind.Media is an independent publication, not a registered charity; contributions are not tax-deductible.</p></div>
<div class="card" style="padding:30px" id="pledge"><h3>Pledge your support</h3><p class="form-note" style="margin-bottom:12px">Choose an amount and we'll email you a secure payment link (card, PayPal, UPI or bank transfer).</p>
<form class="form" data-form="Donation Pledge" data-success="Thank you! We'll email your secure payment link shortly.">
<div class="amount-grid">{''.join(f'<button type="button" class="pill" data-amount="{a}">${a}</button>' for a in [5,10,25,50,100,250,500,1000])}</div>
<div class="form-row"><div><label for="donAmount">Amount (USD)</label><input id="donAmount" name="amount" type="number" min="1" required></div><div><label for="d_freq">Frequency</label><select id="d_freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div><label for="d_purpose">Direct my support to</label><select id="d_purpose" name="purpose"><option>Where it's needed most</option><option>Operations &amp; tools</option><option>Promotion &amp; marketing</option><option>Hiring creators &amp; talent</option><option>Contests &amp; prizes</option></select></div>
<div class="form-row"><div><label for="d_name">Name</label><input id="d_name" name="name" required></div><div><label for="d_email">Email</label><input id="d_email" type="email" name="email" required></div></div>
<label class="check"><input type="checkbox" name="public_thanks" value="yes"> List my name on the supporters wall</label>
{consent_box()}<button class="btn btn-grad" type="submit">Pledge support</button>{status()}</form></div>
</div></section>"""
    page("donate.html", "Support Mind.Media — Donate or Become a Member", "Support independent mental wellbeing media. Donations fund free tools, expert content, creator grants, contests and operations.", body)

    # ---------------- CONTESTS ----------------
    body = hero("Contests & prizes", "Create. Share. Win.", "Monthly creative challenges with cash prizes, features and paid creator opportunities.", "Contests") + f"""
<section style="padding-top:10px"><div class="container grid g2" style="align-items:start">
<div class="card" style="padding:30px"><span class="tag warm">Open now</span><h2 style="margin:10px 0">The Calm Creator Challenge</h2>
<p>Share a 60-second video, short poem, photo or illustration answering: <b>“What helps your mind reset?”</b></p>
<div class="countdown" data-countdown="2026-12-15T23:59:00" style="margin:18px 0"></div>
<div class="table-wrap"><table class="table"><tr><th>Prize</th><th>Reward</th></tr><tr><td>🥇 Grand prize</td><td>$1,000 + featured video + paid creator contract</td></tr><tr><td>🥈 Runner-up (2)</td><td>$300 each + feature</td></tr><tr><td>🥉 Community choice</td><td>$200 + merch pack</td></tr><tr><td>🎖️ Honourable mentions (10)</td><td>Feature on Mind.Media &amp; socials</td></tr></table></div>
<p class="form-note" style="margin-top:12px">Prize amounts are funded by sponsors and supporters. <a href="advertise.html">Sponsor a prize →</a></p></div>
<div class="card" style="padding:30px"><h3>Submit your entry</h3><form class="form" data-form="Contest Entry — Calm Creator Challenge" data-success="Entry received! We'll confirm eligibility by email. Good luck!">
<div class="form-row"><div><label for="c_name">Full name</label><input id="c_name" name="name" required></div><div><label for="c_email">Email</label><input id="c_email" type="email" name="email" required></div></div>
<div class="form-row"><div><label for="c_cat">Category</label><select id="c_cat" name="category"><option>Video (60s)</option><option>Poem / short writing</option><option>Photo</option><option>Illustration</option></select></div><div><label for="c_country">Country</label><input id="c_country" name="country" required></div></div>
<div><label for="c_link">Link to your entry</label><input id="c_link" type="url" name="entry_link" placeholder="YouTube, Instagram, Drive, Dropbox…" required></div>
<div><label for="c_desc">Short description</label><textarea id="c_desc" name="description" maxlength="600"></textarea></div>
<div><label for="c_handle">Social handle (for credit)</label><input id="c_handle" name="social_handle" placeholder="@yourname"></div>
<label class="check"><input type="checkbox" name="age_18" value="yes" required> I am 18 or older (or have parental consent) and this is my original work.</label>
<label class="check"><input type="checkbox" name="rules" value="yes" required> I accept the <a href="#rules">official rules</a>.</label>
<button class="btn btn-warm" type="submit">Submit entry</button>{status()}</form></div>
</div></section>
<section class="alt" id="rules"><div class="container" style="max-width:860px"><h2>Official rules (summary)</h2>
<details><summary>Eligibility</summary><p>Open worldwide where legally permitted. Entrants must be 18+ or have parental/guardian consent. Void where prohibited. Employees of Mind.Media and sponsors are not eligible.</p></details>
<details><summary>Judging</summary><p>Entries are judged on originality (40%), relevance to theme (30%) and craft (30%) by an editorial panel. Community choice is decided by public vote on our social channels.</p></details>
<details><summary>Rights</summary><p>You keep ownership of your work. By entering, you grant Mind.Media a non-exclusive licence to feature your entry with credit across our channels.</p></details>
<details><summary>Content standards</summary><p>No hateful, graphic or unsafe content, and no content that depicts self-harm. Entries must not infringe anyone's copyright or trademark.</p></details>
<details><summary>Prizes</summary><p>Winners are notified by email within 14 days of the deadline and must respond within 14 days. Prizes are paid digitally; winners are responsible for applicable taxes. No purchase necessary.</p></details>
</div></section>
<section><div class="container"><h2 class="center">Upcoming challenges</h2><div class="grid g3" style="margin-top:22px">
<div class="card"><span class="tag">January</span><h3>30-Day Focus Streak</h3><p>Log focus sessions daily. Top streaks win premium gear.</p></div>
<div class="card"><span class="tag teal">March</span><h3>Sleep Reset Challenge</h3><p>Build a consistent wake time. Weekly prize draws.</p></div>
<div class="card"><span class="tag warm">May</span><h3>Mental Health Month Film Fest</h3><p>Short films under 5 minutes. $2,500 prize pool target.</p></div>
</div></div></section>"""
    page("contests.html", "Contests & Prizes — Calm Creator Challenge | Mind.Media", "Enter Mind.Media creative contests for cash prizes, features and paid creator contracts. Video, writing, photo and illustration categories.", body)

    # ---------------- CAREERS ----------------
    WID = ' id="write"'
    roles = [("Freelance Writer — Psychology & Wellbeing", "Remote · Per article", "writing"), ("Licensed Clinical Reviewer", "Remote · Contract", "review"),
             ("YouTube Video Editor", "Remote · Per project", "creators"), ("Short-form Creator (Reels/TikTok/Shorts)", "Remote · Per project", "creators"),
             ("SEO & Growth Marketer", "Remote · Part-time", "growth"), ("Partnerships & Sponsorship Lead", "Remote · Commission + retainer", "growth"),
             ("Community & Contest Manager", "Remote · Part-time", "growth"), ("Podcast Host / Producer", "Remote · Contract", "creators")]
    body = hero("Careers & creators", "Build the future of mind media with us", "We hire writers, clinicians, video creators and growth talent from anywhere. Remote-first, paid, flexible.", "Careers") + f"""
<section style="padding-top:10px"><div class="container">
<div class="grid g2">{''.join(f'<div class="card"{WID if i==0 else ""}><span class="tag">{c.title()}</span><h3>{r}</h3><p class="meta">{l}</p><a class="btn btn-ghost btn-sm" href="#apply" style="margin-top:10px" data-role="{r}">Apply →</a></div>' for i,(r,l,c) in enumerate(roles))}</div>
</div></section>
<section class="alt" id="creators"><div class="container grid g2" style="align-items:start">
<div><h2>Why work with Mind.Media</h2><ul style="padding-left:20px;margin-top:14px;color:var(--ink-2);display:grid;gap:8px"><li>Paid work with clear rates and fast payouts</li><li>Bylines and portfolio-building features</li><li>Revenue share on sponsored series for creators</li><li>Remote-first — work from anywhere</li><li>A mission that matters: making mental wellbeing knowledge accessible</li></ul>
<div class="card" style="margin-top:20px"><h3>Not seeing your role?</h3><p>Send a general application — we're always meeting talented people.</p></div></div>
<div class="card" style="padding:30px" id="apply"><h3>Apply or pitch</h3><form class="form" data-form="Careers / Talent Application">
<div class="form-row"><div><label for="j_name">Full name</label><input id="j_name" name="name" required></div><div><label for="j_email">Email</label><input id="j_email" type="email" name="email" required></div></div>
<div><label for="j_role">Role</label><select id="j_role" name="role">{''.join(f'<option>{r}</option>' for r,_,_ in roles)}<option>General application</option><option>Content pitch</option></select></div>
<div class="form-row"><div><label for="j_port">Portfolio / LinkedIn / channel</label><input id="j_port" type="url" name="portfolio" placeholder="https://" required></div><div><label for="j_loc">Location / time zone</label><input id="j_loc" name="location"></div></div>
<div><label for="j_msg">Tell us about you (or your pitch)</label><textarea id="j_msg" name="message" required></textarea></div>
{consent_box()}<button class="btn btn-grad" type="submit">Send application</button>{status()}</form></div>
</div></section>"""
    page("careers.html", "Careers, Writers & Creators | Mind.Media", "Remote paid opportunities for writers, clinical reviewers, video creators, podcast producers and growth marketers.", body)

    # ---------------- ABOUT ----------------
    body = hero("About", "Media for the mind", "Mind.Media is an independent digital publication making psychology, mindfulness and mental wellbeing knowledge practical, free and easy to act on.", "About") + f"""
<section style="padding-top:10px"><div class="container grid g3">
<div class="card"><div class="ico">🔬</div><h3>Evidence-informed</h3><p>We translate research into clear, practical guidance and review sensitive topics with qualified professionals.</p></div>
<div class="card"><div class="ico">🌍</div><h3>Free &amp; accessible</h3><p>Articles, videos and tools are free — funded by ads, sponsors and readers.</p></div>
<div class="card"><div class="ico">🤝</div><h3>A bridge to real help</h3><p>Content helps; people help more. Our matching service connects readers to qualified support.</p></div>
</div></section>
<section class="alt"><div class="container" style="max-width:860px"><h2>Editorial standards</h2>
<p style="margin-top:12px">We avoid sensationalism and unsupported claims. Health-related content is written for education and reviewed for accuracy; it is never a substitute for professional diagnosis or treatment. Sponsored content is always labelled, and advertisers never influence editorial decisions. Corrections are made promptly and transparently.</p>
<h2 style="margin-top:30px">How we make money</h2><p style="margin-top:12px">Display advertising (including Google AdSense), YouTube, clearly labelled sponsorships, provider listing fees, workplace programs and reader contributions. We never sell personal data.</p>
<p style="margin-top:20px"><a class="btn btn-primary" href="contact.html">Contact us</a> <a class="btn btn-ghost" href="careers.html">Join the team</a></p></div></section>"""
    page("about.html", "About Mind.Media — Independent Mental Wellbeing Media", "Mind.Media is an independent publication making psychology and wellbeing knowledge practical, free and actionable.", body)

    # ---------------- CONTACT ----------------
    body = hero("Contact", "Get in touch", "Questions, corrections, partnerships or press — send us a message and we'll reply within 1–2 business days.", "Contact") + f"""
<section style="padding-top:10px"><div class="container grid g2" style="align-items:start">
<div class="card" style="padding:30px"><form class="form" data-form="General Contact">
<div class="form-row"><div><label for="ct_name">Name</label><input id="ct_name" name="name" required></div><div><label for="ct_email">Email</label><input id="ct_email" type="email" name="email" required></div></div>
<div><label for="ct_topic">Topic</label><select id="ct_topic" name="topic"><option>General question</option><option>Editorial / correction</option><option>Press</option><option>Partnership</option><option>Advertising / sponsorship</option><option>Domain / website acquisition</option><option>Technical issue</option></select></div>
<div><label for="ct_msg">Message</label><textarea id="ct_msg" name="message" required></textarea></div>
{consent_box()}<button class="btn btn-grad" type="submit">Send message</button>{status()}</form></div>
<div class="grid" style="gap:16px">
<div class="card"><h3>Quick links</h3><ul style="list-style:none;display:grid;gap:8px;margin-top:8px"><li>🧠 <a href="find-support.html">Find a therapist or coach</a></li><li>🏢 <a href="for-business.html">Workplace programs</a></li><li>📣 <a href="advertise.html">Advertise / sponsor</a></li><li>💼 <a href="careers.html">Careers &amp; pitches</a></li><li>✉️ <a href="#" data-contact="Mind.Media — direct email">Open email app</a></li></ul></div>
<div class="card"><h3>Interested in this website or domain?</h3><p>For acquisition, sponsorship, advertising or partnership: <a href="{INTEREST}" target="_blank" rel="noopener">web.works/contact</a></p></div>
<div class="crisis"><strong>We can't respond to emergencies.</strong> If you or someone else is in danger, call your local emergency number (US/Canada: call or text 988).</div>
</div></div></section>"""
    page("contact.html", "Contact Mind.Media", "Contact Mind.Media for questions, corrections, press, partnerships and advertising.", body)

    # ---------------- LEGAL PAGES ----------------
    def legal(path, title, h1, content):
        page(path, f"{title} | Mind.Media", f"{title} for Mind.Media.", hero("Legal", h1, "Last updated: September 2026", title) + f'<section style="padding-top:0"><div class="container"><div class="article">{content}</div></div></section>')

    legal("legal.html", "Trademark & Copyright Disclosure", "Trademark &amp; copyright disclosure", f"""
<h2>Independent publication</h2><p>“Mind.Media” is the name of this independent website, operated on the domain Mind.Media. It is used descriptively — combining “mind” (psychology and wellbeing) and “media” (publishing and video).</p>
<h2>No affiliation</h2><p>Mind.Media is <strong>not affiliated with, endorsed by, sponsored by or connected to</strong> any company, product or trademark using the name “Mind Media,” “MindMedia” or similar, including — without limitation — any biofeedback or neurofeedback equipment manufacturer, marketing or creative agency, media production company or publisher operating under such a name in any country. Any similarity in name is coincidental. We do not offer biofeedback hardware or agency services.</p>
<h2>Third-party marks</h2><p>All third-party names, trademarks, logos and brands mentioned on this website (including YouTube, TED, Google and others) are the property of their respective owners and are used for identification or reference only. Their use does not imply endorsement.</p>
<h2>Embedded content</h2><p>Videos embedded from YouTube remain the property of their creators and are displayed using YouTube's standard embed functionality under YouTube's Terms of Service.</p>
<h2>Copyright</h2><p>Unless otherwise stated, all original text, design, code and graphics on this website are © {BRAND}. All rights reserved. You may share links and short quotations with attribution. Reproduction of full articles requires written permission.</p>
<h2>Notice &amp; takedown</h2><p>If you believe any content on this website infringes your copyright or trademark, please use our <a href="contact.html">contact form</a> (topic: “Editorial / correction”) with the work, the URL and your contact details. We review all notices promptly and remove infringing material where appropriate.</p>
<h2>Domain enquiries</h2><p>For enquiries about this website or domain name, visit <a href="{INTEREST}" target="_blank" rel="noopener">web.works/contact</a>.</p>""")

    legal("privacy.html", "Privacy Policy", "Privacy policy", """
<p>This policy explains what information Mind.Media collects and how it is used.</p>
<h2>Information you give us</h2><p>When you submit a form (support matching, newsletter, business proposal, practitioner application, contest entry, donation pledge, careers or contact), we receive the details you provide. We use them only to respond to your request, deliver the service you asked for, and — where you opted in — send our newsletter. Form submissions are relayed securely by a third-party form-processing service.</p>
<h2>Support matching</h2><p>Information you share in the matching form is used to identify suitable providers. We share your details only with providers you agree to be introduced to. Please do not include information you are not comfortable sharing.</p>
<h2>Tools</h2><p>Entries in our free tools (mood, gratitude, focus sessions) are stored only in your browser's local storage on your device. We cannot see them. Clearing your browser data removes them.</p>
<h2>Cookies &amp; advertising</h2><p>With your consent, we use Google Analytics to understand site usage and Google AdSense to display ads. Google and its partners may use cookies to serve ads based on your visits to this and other websites. You can opt out of personalised advertising at <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>. You can change your choice at any time by clearing site data.</p>
<h2>Embedded videos</h2><p>Videos load from YouTube's privacy-enhanced domain only when you press play.</p>
<h2>Your rights</h2><p>Depending on where you live (e.g. GDPR, CCPA/CPRA, PIPEDA, Quebec Law 25, India DPDP Act), you may have rights to access, correct or delete your data. Contact us via the <a href="contact.html">contact form</a>.</p>
<h2>Children</h2><p>Mind.Media is intended for adults. We do not knowingly collect information from children under 13.</p>
<h2>Changes</h2><p>We may update this policy and will revise the date above.</p>""")

    legal("terms.html", "Terms of Use", "Terms of use", """
<p>By using Mind.Media you agree to these terms.</p>
<h2>Educational purpose</h2><p>All content and tools are for general information and education only and do not constitute medical, psychological or professional advice. See our <a href="disclaimer.html">Medical Disclaimer</a>.</p>
<h2>Referral service</h2><p>Mind.Media is not a healthcare provider. Providers introduced through our matching service are independent, and you are responsible for evaluating their suitability. We are not liable for services they provide.</p>
<h2>Acceptable use</h2><p>Do not misuse the site, submit false information, spam forms, scrape content at scale or upload unlawful material.</p>
<h2>Contests</h2><p>Contests are governed by their official rules on the <a href="contests.html">Contests page</a>.</p>
<h2>Contributions</h2><p>Donations and memberships support operations and are generally non-refundable. Mind.Media is not a registered charity.</p>
<h2>Intellectual property</h2><p>See our <a href="legal.html">Trademark &amp; Copyright Disclosure</a>.</p>
<h2>Limitation of liability</h2><p>The site is provided “as is.” To the fullest extent permitted by law, Mind.Media is not liable for any damages arising from its use.</p>""")

    legal("disclaimer.html", "Medical Disclaimer", "Medical disclaimer", """
<div class="crisis"><strong>If you are in crisis</strong>, call your local emergency number now. US &amp; Canada: call or text 988. UK &amp; Ireland: Samaritans 116 123. India: Tele-MANAS 14416. Elsewhere: <a href="https://findahelpline.com" target="_blank" rel="noopener">findahelpline.com</a>.</div>
<h2>Not medical advice</h2><p>Content on Mind.Media — including articles, videos, tools, check-ins and newsletters — is for educational purposes only. It is not intended to diagnose, treat, cure or prevent any condition and is not a substitute for advice from a qualified healthcare professional.</p>
<h2>Tools and scores</h2><p>Scores from our check-ins and meters are non-clinical and are not validated diagnostic instruments.</p>
<h2>Always consult a professional</h2><p>Never disregard professional advice or delay seeking it because of something you read here. Do not start or stop any medication without consulting your doctor.</p>""")

    # ---------------- 404 ----------------
    page("404.html", "Page not found | Mind.Media", "Page not found.", hero("404", "This page took a mindful pause", "It may have moved. Try one of these instead.") +
         '<section style="padding-top:0"><div class="container center"><a class="btn btn-grad" href="index.html">Go home</a> <a class="btn btn-ghost" href="articles.html">Read articles</a> <a class="btn btn-ghost" href="tools.html">Free tools</a></div></section>')

    # ---------------- sitemap / robots ----------------
    pages = ["", "articles.html", "videos.html", "tools.html", "find-support.html", "for-business.html", "for-practitioners.html", "advertise.html",
             "donate.html", "contests.html", "careers.html", "about.html", "contact.html", "legal.html", "privacy.html", "terms.html", "disclaimer.html"] + [f"articles/{a['slug']}.html" for a in A]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"  <url><loc>{SITE}/{u}</loc><changefreq>weekly</changefreq></url>\n" for u in pages) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /_build/\nSitemap: {SITE}/sitemap.xml\n")
    print("built", len(pages) + 1, "pages")

if __name__ == "__main__":
    build()
