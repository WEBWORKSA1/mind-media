# Mind.Media — Phase-Wise Build Prompt

Use these prompts in order with any AI coding assistant, or a dev team, to rebuild or extend Mind.Media. Each phase has to pass its acceptance checks before the next one starts.

---

## Phase 0 — Global rules (paste this at the top of every phase)

```
You are building Mind.Media (domain: Mind.Media), an independent mental-wellbeing media brand
with a therapist/coach/workplace matching service. Stack: static HTML + one CSS file + vanilla JS,
no build step required to host, deployable on GitHub Pages free plan (relative paths only, .nojekyll).

Hard rules:
1. Every page starts with a top bar: "Contact, if you are interested in this website/domain
   name/Sponsorship/Advertisement/Partnership" linking to https://web.works/contact.
2. All forms and mail links route to ONE owner inbox. The address must NEVER appear in HTML,
   JS strings, sitemap or any public file: store it as shifted, reversed char codes and decode it
   at runtime only; submit via https://formsubmit.co/ajax/<decoded>. Mail links use data-contact
   and build mailto: only on click.
3. Brand is always "Mind.Media" (with the dot). Never imply affiliation with any "Mind Media"
   company. Include a trademark/copyright disclosure page and a footer non-affiliation line.
4. Health content is educational; show crisis resources (988 US/CA, 116 123 UK/IE, 14416 India,
   findahelpline.com) on support pages and articles. Self-checks say "not a diagnosis".
5. Mobile-first, WCAG AA contrast, dark mode, no horizontal scroll at 360px, Lighthouse ≥ 90.
6. AdSense and GA4 load ONLY after cookie consent and only when IDs are set in CONFIG.
```

## Phase 1 — Foundation and design system
```
Create assets/css/style.css with design tokens (light + dark via prefers-color-scheme and
[data-theme]), fonts Fraunces (headings) + Inter (body), gradient brand #5b3df5 → #8e5cf7 → #12b5a5.
Components: sticky blurred header, mobile hamburger (<1180px), buttons (primary, gradient, ghost,
warm), cards, tags, pills/filters, forms, multi-step form, choice tiles, lead band, ad slot,
lite YouTube embed, countdown, progress bar, accordion, cookie banner, modal, floating CTA,
footer with 5 columns + newsletter. Write a Python generator (_build/build.py) that stamps
the shared head/topbar/header/footer onto every page, plus JSON-LD (Organization, WebSite,
Article) and OG tags.
Acceptance: every page has the top bar; nav works at 390px; no console errors.
```

## Phase 2 — Content engine (AdSense readiness)
```
Build articles.html (filterable, searchable library) and at least 6 original, 600–900 word
articles in /articles with: breadcrumb, byline, read time, share buttons, crisis note, TOC-ready
h2 ids, in-article ad slot after section 1, lead-gen band, newsletter box, related reads.
Topics: breathing, burnout, sleep/anxiety, attention reset, choosing a therapist, procrastination.
Add sitemap.xml, robots.txt, ads.txt placeholder, 404.html, privacy (AdSense cookie language),
terms, medical disclaimer.
Acceptance: all internal links resolve; every article has a unique title and meta description.
Roadmap: scale to 30+ articles before applying to AdSense; add author bios and a reviewer.
```

## Phase 3 — Video hub (YouTube revenue)
```
videos.html: category filters, lite-YouTube embeds (thumbnail first, iframe from
youtube-nocookie.com on click), a subscribe CTA pointing at the brand channel, podcast waitlist
form, creator pitch CTA, and a third-party content disclaimer. Put a 4-video strip on the home page.
Acceptance: no iframe loads until the user clicks; every video ID is verified live.
```

## Phase 4 — Interactive tools (engagement + return visits)
```
tools.html + assets/js/tools.js: Breathing Coach (box / 4-7-8 / coherent, animated orb),
Focus Timer (15/25/50/90, streak counter), Mood Tracker (1–5 emoji, 7-day bar chart,
localStorage), Sleep Cycle Calculator (90-minute cycles + 15-minute sleep latency),
Burnout Risk Meter (5 sliders), Gratitude Journal (localStorage), and a 60-second Wellbeing
Check-in on the home hero whose low scores route to find-support.html.
Acceptance: all data stays on the device; each tool fires a GA4 tool_use event.
```

## Phase 5 — Lead generation (primary revenue)
```
find-support.html: a 3-step matching form (need → preferences: format, budget incl. insurance/EAP,
location, language, urgency → contact + consent), with a progress bar, a how-it-works panel,
trust bullets, crisis box, browse-by-need grid and FAQ. Reuse the same form in the home-page
lead band.
for-business.html: B2B proposal form (company, team size, interest, budget, timeline) + package table.
for-practitioners.html: practitioner application (profession, license, specialties, plan).
Add an exit-intent / 45-second modal offering a "7-Day Calm Reset" email course, and a floating
"Get matched free" CTA after scrolling.
Acceptance: each form posts JSON to the relay with a subject tag, honeypot and required consent;
success and error states render; a generate_lead event fires.
```

## Phase 6 — Community monetization: donations, contests, talent, sponsors
```
donate.html: quarterly goal progress bar, 4 tiers (Supporter, Member, Champion, Patron) whose
buttons read Stripe/PayPal/Ko-fi/BMAC links from CONFIG and fall back to a pledge form; amount
chips; a "direct my support to" selector (operations, promotion & marketing, hiring talent,
contests & prizes); use-of-funds breakdown; a "not a registered charity" note.
contests.html: live contest with countdown, prize table, entry form (URL-based, 18+ and rules
checkboxes), official-rules accordion, upcoming challenges.
careers.html: 8 remote role cards with one-click role preselect and an application/pitch form.
advertise.html: 8 sponsorship products, ad standards, a media-kit request form, and a link to the
domain/partnership contact.
Acceptance: every form reaches the inbox; tier buttons never dead-end.
```

## Phase 7 — Legal, trust and launch
```
legal.html: independent-publication statement, explicit non-affiliation with any "Mind Media /
MindMedia" entity, third-party marks, YouTube embeds, copyright, notice & takedown, domain
enquiries. about.html: editorial standards + how we make money. contact.html: general form +
data-contact mail link + web.works/contact box.
Deploy: push to GitHub (WEBWORKSA1/Mind-Media), serve from gh-pages (root), add .nojekyll.
Acceptance: grep the repo for the owner email → zero hits; the live URL returns 200.
```

## Phase 8 — Growth and scale (post-launch)
```
1. Point Mind.Media DNS to GitHub Pages, add CNAME, update SITE in build.py, rebuild.
2. Activate FormSubmit (confirm the first email), then switch to its hashed alias endpoint.
3. Apply for AdSense once 30+ quality articles exist; set CONFIG.adsenseClient and ads.txt.
4. Launch the YouTube channel; add 2 originals per week; embed each on a matching article.
5. Sign 10–20 practitioners on Pro; add 1–2 therapy/coaching affiliate programs as overflow.
6. Programmatic SEO: "therapist for {concern} in {city}" landing pages, generated by build.py.
7. Add a Supabase-backed directory and member accounts when lead volume justifies it.
```
