/* Mind.Media — site runtime (no dependencies) */
(function () {
  'use strict';

  /* ================= CONFIG — edit these to go live ================= */
  var CONFIG = {
    adsenseClient: '',            // e.g. 'ca-pub-1234567890123456' — leave empty until AdSense approves
    ga4Id: '',                    // e.g. 'G-XXXXXXX'
    youtubeChannel: 'https://www.youtube.com/@MindMediaHub', // replace with your channel
    donateLinks: {                // paste Stripe Payment Links / PayPal hosted-button / Ko-fi URLs here
      stripe: '', paypal: '', kofi: '', bmac: ''
    },
    interestUrl: 'https://web.works/contact'
  };
  window.MM_CONFIG = CONFIG;

  /* ================= Contact routing (address never rendered) ================= */
  var _k = [116,118,106,53,115,112,104,116,110,71,56,104,122,114,121,118,126,105,108,126];
  function route() { return _k.slice().reverse().map(function (c) { return String.fromCharCode(c - 7); }).join(''); }
  function endpoint() { return 'https://formsubmit.co/ajax/' + route(); }

  // Links with [data-contact] open the mail client only on click; href never contains the address
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-contact]');
    if (!a) return;
    e.preventDefault();
    var subj = encodeURIComponent(a.getAttribute('data-contact') || 'Mind.Media inquiry');
    window.location.href = 'mai' + 'lto:' + route() + '?subject=' + subj;
  });

  /* ================= Theme ================= */
  var root = document.documentElement;
  try { var t = localStorage.getItem('mm-theme'); if (t) root.setAttribute('data-theme', t); } catch (e) {}
  var tbtn = document.getElementById('themeToggle');
  if (tbtn) tbtn.addEventListener('click', function () {
    var dark = root.getAttribute('data-theme') === 'dark' ||
      (!root.getAttribute('data-theme') && matchMedia('(prefers-color-scheme: dark)').matches);
    var next = dark ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('mm-theme', next); } catch (e) {}
  });

  /* ================= Mobile menu ================= */
  var mbtn = document.getElementById('menuBtn'), links = document.getElementById('navLinks');
  if (mbtn && links) mbtn.addEventListener('click', function () {
    var o = links.classList.toggle('open'); mbtn.setAttribute('aria-expanded', o);
  });

  /* ================= Year ================= */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ================= Reveal on scroll ================= */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: .12 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });

  /* ================= Forms → email relay ================= */
  document.querySelectorAll('form[data-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('.form-status');
      if (form.querySelector('.hp input') && form.querySelector('.hp input').value) return; // bot
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var data = {};
      new FormData(form).forEach(function (v, k) {
        if (k === '_honey') return;
        data[k] = data[k] ? data[k] + ', ' + v : v;
      });
      data._subject = '[Mind.Media] ' + form.getAttribute('data-form') + ' — ' + (data.name || data.email || 'new submission');
      data._template = 'table';
      data._captcha = 'false';
      data.page = location.href;
      var btn = form.querySelector('[type=submit]'); var label = btn ? btn.innerHTML : '';
      if (btn) { btn.disabled = true; btn.innerHTML = 'Sending…'; }
      fetch(endpoint(), { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || res.j.success === 'false') throw new Error('fail');
          if (status) { status.className = 'form-status ok'; status.textContent = form.getAttribute('data-success') || 'Thank you — we received your submission and will respond within 1–2 business days.'; }
          form.reset(); resetSteps(form);
          track('generate_lead', { form: form.getAttribute('data-form') });
        })
        .catch(function () {
          if (status) { status.className = 'form-status err'; status.textContent = 'Could not send right now. Please try again in a moment.'; }
        })
        .finally(function () { if (btn) { btn.disabled = false; btn.innerHTML = label; } });
    });
  });

  /* ================= Multi-step forms ================= */
  function showStep(form, i) {
    var steps = form.querySelectorAll('.step'); var bars = form.querySelectorAll('.steps-bar i');
    steps.forEach(function (s, n) { s.classList.toggle('active', n === i); });
    bars.forEach(function (b, n) { b.classList.toggle('on', n <= i); });
    form.dataset.step = i;
  }
  function resetSteps(form) { if (form.querySelector('.step')) showStep(form, 0); }
  document.querySelectorAll('form .step').length && document.querySelectorAll('form').forEach(function (form) {
    if (!form.querySelector('.step')) return;
    showStep(form, 0);
    form.addEventListener('click', function (e) {
      var n = e.target.closest('[data-next]'), p = e.target.closest('[data-prev]');
      var i = +form.dataset.step;
      if (n) {
        e.preventDefault();
        var cur = form.querySelectorAll('.step')[i];
        var bad = Array.prototype.find.call(cur.querySelectorAll('input,select,textarea'), function (f) { return !f.checkValidity(); });
        if (bad) { bad.reportValidity(); return; }
        showStep(form, i + 1);
      }
      if (p) { e.preventDefault(); showStep(form, Math.max(0, i - 1)); }
    });
  });

  /* ================= Cookie consent + ads/analytics loader ================= */
  var cookie = document.getElementById('cookie');
  function consent() { try { return localStorage.getItem('mm-consent'); } catch (e) { return null; } }
  function loadThirdParty() {
    if (CONFIG.adsenseClient && !document.getElementById('adsbygoogle-js')) {
      var s = document.createElement('script');
      s.id = 'adsbygoogle-js'; s.async = true; s.crossOrigin = 'anonymous';
      s.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + CONFIG.adsenseClient;
      document.head.appendChild(s);
      document.querySelectorAll('.ad-slot').forEach(function (slot) {
        slot.classList.add('filled'); slot.innerHTML = '';
        var ins = document.createElement('ins');
        ins.className = 'adsbygoogle'; ins.style.display = 'block';
        ins.setAttribute('data-ad-client', CONFIG.adsenseClient);
        if (slot.dataset.slot) ins.setAttribute('data-ad-slot', slot.dataset.slot);
        ins.setAttribute('data-ad-format', slot.dataset.format || 'auto');
        ins.setAttribute('data-full-width-responsive', 'true');
        slot.appendChild(ins);
        (window.adsbygoogle = window.adsbygoogle || []).push({});
      });
    }
    if (CONFIG.ga4Id && !window.gtag) {
      var g = document.createElement('script'); g.async = true;
      g.src = 'https://www.googletagmanager.com/gtag/js?id=' + CONFIG.ga4Id; document.head.appendChild(g);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { dataLayer.push(arguments); };
      gtag('js', new Date()); gtag('config', CONFIG.ga4Id);
    }
  }
  function track(ev, p) { if (window.gtag) gtag('event', ev, p || {}); }
  if (cookie) {
    var c = consent();
    if (!c) cookie.classList.add('show'); else if (c === 'all') loadThirdParty();
    cookie.addEventListener('click', function (e) {
      var b = e.target.closest('[data-consent]'); if (!b) return;
      try { localStorage.setItem('mm-consent', b.dataset.consent); } catch (er) {}
      cookie.classList.remove('show');
      if (b.dataset.consent === 'all') loadThirdParty();
    });
  }

  /* ================= YouTube lite embeds ================= */
  document.querySelectorAll('.video[data-yt]').forEach(function (v) {
    var id = v.dataset.yt;
    v.innerHTML = '<img loading="lazy" alt="' + (v.dataset.title || 'Video') + '" src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg"><div class="play"><b>▶</b></div>';
    v.setAttribute('role', 'button'); v.setAttribute('tabindex', '0');
    function play() { v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (v.dataset.title || 'Video') + '" allow="accelerometer;autoplay;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe>'; track('video_play', { id: id }); }
    v.addEventListener('click', play, { once: true });
    v.addEventListener('keydown', function (e) { if (e.key === 'Enter') play(); });
  });

  /* ================= Filters + search (library pages) ================= */
  var fwrap = document.querySelector('[data-filter-group]');
  if (fwrap) {
    var items = document.querySelectorAll('[data-cat]'), q = document.getElementById('librarySearch'), active = 'all';
    function apply() {
      var term = q ? q.value.toLowerCase().trim() : '';
      items.forEach(function (it) {
        var okCat = active === 'all' || it.dataset.cat.split(' ').indexOf(active) > -1;
        var okQ = !term || it.textContent.toLowerCase().indexOf(term) > -1;
        it.style.display = okCat && okQ ? '' : 'none';
      });
    }
    fwrap.addEventListener('click', function (e) {
      var b = e.target.closest('.pill'); if (!b) return;
      fwrap.querySelectorAll('.pill').forEach(function (p) { p.classList.remove('active'); });
      b.classList.add('active'); active = b.dataset.f; apply();
    });
    if (q) q.addEventListener('input', apply);
  }

  /* ================= Countdowns ================= */
  document.querySelectorAll('[data-countdown]').forEach(function (el) {
    var end = new Date(el.dataset.countdown).getTime();
    function tick() {
      var d = Math.max(0, end - Date.now());
      var parts = [Math.floor(d / 864e5), Math.floor(d / 36e5) % 24, Math.floor(d / 6e4) % 60, Math.floor(d / 1e3) % 60];
      el.innerHTML = ['Days', 'Hrs', 'Min', 'Sec'].map(function (l, i) { return '<div><b>' + parts[i] + '</b><small>' + l + '</small></div>'; }).join('');
    }
    tick(); setInterval(tick, 1000);
  });

  /* ================= Reading progress ================= */
  var rb = document.querySelector('.readbar');
  if (rb) window.addEventListener('scroll', function () {
    var h = document.documentElement; var p = h.scrollTop / (h.scrollHeight - h.clientHeight);
    rb.style.width = Math.min(100, p * 100) + '%';
  }, { passive: true });

  /* ================= Share ================= */
  document.querySelectorAll('[data-share]').forEach(function (b) {
    b.addEventListener('click', function () {
      var u = encodeURIComponent(location.href), t = encodeURIComponent(document.title), k = b.dataset.share, url;
      if (k === 'x') url = 'https://twitter.com/intent/tweet?url=' + u + '&text=' + t;
      if (k === 'fb') url = 'https://www.facebook.com/sharer/sharer.php?u=' + u;
      if (k === 'li') url = 'https://www.linkedin.com/sharing/share-offsite/?url=' + u;
      if (k === 'wa') url = 'https://wa.me/?text=' + t + '%20' + u;
      if (k === 'copy') { navigator.clipboard && navigator.clipboard.writeText(location.href); b.textContent = 'Link copied'; return; }
      if (k === 'native' && navigator.share) { navigator.share({ title: document.title, url: location.href }); return; }
      if (url) window.open(url, '_blank', 'noopener,width=620,height=560');
    });
  });

  /* ================= Floating CTA + exit-intent lead capture ================= */
  var fc = document.querySelector('.float-cta');
  if (fc) window.addEventListener('scroll', function () { fc.classList.toggle('show', window.scrollY > 900); }, { passive: true });
  var modal = document.getElementById('leadModal');
  if (modal) {
    var shown = false; try { shown = sessionStorage.getItem('mm-modal') === '1'; } catch (e) {}
    function openModal() { if (shown) return; shown = true; modal.classList.add('show'); try { sessionStorage.setItem('mm-modal', '1'); } catch (e) {} }
    document.addEventListener('mouseout', function (e) { if (!e.relatedTarget && e.clientY < 5) openModal(); });
    setTimeout(openModal, 45000);
    modal.addEventListener('click', function (e) { if (e.target === modal || e.target.closest('[data-close]')) modal.classList.remove('show'); });
  }

  /* ================= Donation helpers ================= */
  document.querySelectorAll('[data-amount]').forEach(function (b) {
    b.addEventListener('click', function () {
      var inp = document.getElementById('donAmount'); if (inp) inp.value = b.dataset.amount;
      document.querySelectorAll('[data-amount]').forEach(function (x) { x.classList.remove('active'); }); b.classList.add('active');
    });
  });
  document.querySelectorAll('[data-pay]').forEach(function (b) {
    var link = CONFIG.donateLinks[b.dataset.pay];
    if (link) { b.href = link; b.target = '_blank'; b.rel = 'noopener'; }
    else b.addEventListener('click', function (e) {
      e.preventDefault(); var f = document.getElementById('pledge'); if (f) f.scrollIntoView({ behavior: 'smooth' });
    });
  });

  /* Careers: pre-select role */
  document.querySelectorAll('[data-role]').forEach(function (a) {
    a.addEventListener('click', function () { var s = document.getElementById('j_role'); if (s) s.value = a.dataset.role; });
  });

  /* Library: ?q= deep link */
  var qs = new URLSearchParams(location.search).get('q'), ls = document.getElementById('librarySearch');
  if (qs && ls) { ls.value = qs; ls.dispatchEvent(new Event('input')); }

  /* expose for tools.js */
  window.MM = { track: track };
})();
