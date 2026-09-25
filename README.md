# Mind.Media

Mind.Media is an independent mental-wellbeing media site with lead generation. Content, video and free tools bring in visitors, and a matching service turns them into therapy, coaching and workplace-program leads. It earns from AdSense, YouTube, sponsorships, donations, contests and practitioner listings.

- **Live site (GitHub Pages):** https://webworksa1.github.io/mind-media/
- **Build prompt, phase by phase:** [PROMPT.md](PROMPT.md)
- **Concept, revenue model and the 35-site benchmark:** [RESEARCH.md](RESEARCH.md)

## Structure
```
index.html              Home: hero check-in, articles, lead band, videos, tools, contests, donate, FAQ
articles.html           Filterable, searchable library (+ /articles/*.html)
videos.html             YouTube hub, podcast waitlist
tools.html              Breathing, focus, mood, sleep, burnout, gratitude tools
find-support.html       ★ Multi-step lead-gen matching form
for-business.html       ★ B2B workplace proposal lead form
for-practitioners.html  ★ Practitioner listing applications
advertise.html          Sponsorship / media kit requests
donate.html             Tiers, pledge form, use-of-funds
contests.html           Live contest, countdown, entry form, rules
careers.html            Remote roles + application form
about / contact / legal / privacy / terms / disclaimer / 404
_build/                 Python generator: edit, then run `python3 _build/build.py`
```

## Go-live checklist
1. **Forms.** Submit any form once, then click the activation link FormSubmit sends to the owner inbox. The address never appears in the source; it is decoded at runtime.
2. **AdSense.** Set `adsenseClient` in `assets/js/main.js` and add your publisher line to `ads.txt`.
3. **Analytics.** Set `ga4Id` in `assets/js/main.js`.
4. **Donations.** Paste Stripe, PayPal, Ko-fi or BMAC links into `CONFIG.donateLinks`. Until then, the tier buttons scroll to the pledge form.
5. **YouTube.** Update `youtubeChannel` and the `@MindMediaHub` links to your real channel.
6. **Custom domain.** Point Mind.Media DNS to GitHub Pages, add a `CNAME` file, change `SITE` in `_build/build.py`, and rebuild.

© Mind.Media. The site is not affiliated with any company named "Mind Media" or "MindMedia". See legal.html.
