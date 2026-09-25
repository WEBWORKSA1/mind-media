/* Mind.Media — interactive wellbeing tools (all data stays in the visitor's browser) */
(function () {
  'use strict';
  function $(s) { return document.querySelector(s); }
  function store(k, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem(k) || 'null'); localStorage.setItem(k, JSON.stringify(v)); } catch (e) { return null; } }
  var track = (window.MM && window.MM.track) || function () {};

  /* ---------- Breathing coach ---------- */
  var orb = $('#orb');
  if (orb) {
    var patterns = { box: [['Inhale', 4, 1], ['Hold', 4, 1], ['Exhale', 4, .6], ['Hold', 4, .6]], relax: [['Inhale', 4, 1], ['Hold', 7, 1], ['Exhale', 8, .6]], calm: [['Inhale', 5, 1], ['Exhale', 5, .6]] };
    var timer = null, running = false;
    function run() {
      var p = patterns[$('#breathPattern').value], i = 0, cycles = 0;
      function phase() {
        if (!running) return;
        var ph = p[i]; orb.textContent = ph[0] + ' · ' + ph[1] + 's';
        orb.style.transitionDuration = ph[1] + 's'; orb.style.transform = 'scale(' + ph[2] + ')';
        i = (i + 1) % p.length; if (i === 0) { cycles++; $('#breathCycles').textContent = cycles; }
        timer = setTimeout(phase, ph[1] * 1000);
      }
      phase();
    }
    $('#breathBtn').addEventListener('click', function () {
      running = !running; this.textContent = running ? 'Stop' : 'Start breathing';
      if (running) { run(); track('tool_use', { tool: 'breathing' }); } else { clearTimeout(timer); orb.textContent = 'Ready'; orb.style.transform = 'scale(.6)'; }
    });
  }

  /* ---------- Focus timer ---------- */
  var ft = $('#focusTime');
  if (ft) {
    var left = 25 * 60, iv = null, mode = 'focus', sessions = store('mm-focus') || 0;
    $('#focusCount').textContent = sessions;
    function draw() { ft.textContent = String(Math.floor(left / 60)).padStart(2, '0') + ':' + String(left % 60).padStart(2, '0'); }
    function set(m) { mode = m; left = (m === 'focus' ? +$('#focusLen').value : 5) * 60; $('#focusMode').textContent = m === 'focus' ? 'Focus session' : 'Short break'; draw(); }
    $('#focusStart').addEventListener('click', function () {
      if (iv) { clearInterval(iv); iv = null; this.textContent = 'Resume'; return; }
      this.textContent = 'Pause'; track('tool_use', { tool: 'focus' });
      iv = setInterval(function () {
        left--; draw();
        if (left <= 0) {
          clearInterval(iv); iv = null; $('#focusStart').textContent = 'Start';
          if (mode === 'focus') { sessions++; store('mm-focus', sessions); $('#focusCount').textContent = sessions; set('break'); } else set('focus');
          try { new AudioContext().resume(); } catch (e) {}
        }
      }, 1000);
    });
    $('#focusReset').addEventListener('click', function () { clearInterval(iv); iv = null; $('#focusStart').textContent = 'Start'; set('focus'); });
    $('#focusLen').addEventListener('change', function () { if (!iv) set('focus'); });
    draw();
  }

  /* ---------- Mood tracker ---------- */
  var mr = $('#moodRow');
  if (mr) {
    var log = store('mm-mood') || [];
    function render() {
      var last = log.slice(-7), bars = $('#moodBars');
      bars.innerHTML = last.length ? last.map(function (m) { return '<span title="' + m.d + '" style="height:' + (m.v * 20) + '%"></span>'; }).join('') : '<p class="form-note">Log your first mood to see your week.</p>';
      var avg = last.length ? (last.reduce(function (a, b) { return a + b.v; }, 0) / last.length).toFixed(1) : '–';
      $('#moodAvg').textContent = avg;
    }
    mr.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      mr.querySelectorAll('button').forEach(function (x) { x.classList.remove('sel'); }); b.classList.add('sel');
      var today = new Date().toISOString().slice(0, 10);
      log = log.filter(function (m) { return m.d !== today; }); log.push({ d: today, v: +b.dataset.v }); log = log.slice(-60);
      store('mm-mood', log); render(); track('tool_use', { tool: 'mood' });
    });
    render();
  }

  /* ---------- Sleep cycle calculator ---------- */
  var sb = $('#sleepBtn');
  if (sb) sb.addEventListener('click', function () {
    var v = $('#wakeTime').value; if (!v) return;
    var p = v.split(':'), wake = new Date(); wake.setHours(+p[0], +p[1], 0, 0);
    var out = [6, 5, 4].map(function (c) { var d = new Date(wake.getTime() - (c * 90 + 15) * 6e4); return '<b>' + d.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' }) + '</b> (' + c + ' cycles, ' + (c * 1.5) + 'h)'; });
    $('#sleepOut').innerHTML = 'For a ' + v + ' wake-up, aim to be asleep by: ' + out.join(' · ') + '<br><span class="form-note">Includes ~15 minutes to fall asleep. Educational estimate only.</span>';
    track('tool_use', { tool: 'sleep' });
  });

  /* ---------- Wellbeing check-in (non-clinical) ---------- */
  var wq = $('#checkin');
  if (wq) wq.addEventListener('submit', function (e) {
    e.preventDefault();
    var total = 0, n = 0;
    wq.querySelectorAll('select').forEach(function (s) { total += +s.value; n++; });
    var pct = Math.round(total / (n * 4) * 100), msg, cls;
    if (pct >= 70) { msg = 'You are in a strong place. Keep the habits that are working — the Focus and Mood tools help you protect them.'; }
    else if (pct >= 45) { msg = 'Mixed week. Small, consistent changes (sleep timing, 5-minute breathing, one honest conversation) tend to move this score quickly.'; }
    else { msg = 'Things feel heavy right now. You do not have to handle it alone — a licensed professional or coach can help. Our free matching service takes 2 minutes.'; }
    $('#checkinOut').innerHTML = '<div class="kpi">' + pct + '/100</div><p>' + msg + '</p><p style="margin-top:10px"><a class="btn btn-grad btn-sm" href="find-support.html">Get matched with support →</a></p><p class="form-note" style="margin-top:10px">This check-in is educational, not a diagnosis.</p>';
    $('#checkinOut').style.display = 'block';
    track('tool_use', { tool: 'checkin', score: pct });
  });

  /* ---------- Gratitude journal ---------- */
  var gj = $('#gratForm');
  if (gj) {
    var list = store('mm-grat') || [];
    function paint() { $('#gratList').innerHTML = list.slice(-5).reverse().map(function (g) { return '<li><b>' + g.d + '</b> — ' + g.t.replace(/[<>&]/g, '') + '</li>'; }).join('') || '<li class="form-note">Your entries stay private on this device.</li>'; }
    gj.addEventListener('submit', function (e) {
      e.preventDefault(); var v = $('#gratText').value.trim(); if (!v) return;
      list.push({ d: new Date().toLocaleDateString(), t: v }); list = list.slice(-100); store('mm-grat', list); $('#gratText').value = ''; paint();
      track('tool_use', { tool: 'gratitude' });
    });
    paint();
  }

  /* ---------- Burnout risk quick-score ---------- */
  var br = $('#burnout');
  if (br) br.addEventListener('input', function () {
    var s = 0; br.querySelectorAll('input[type=range]').forEach(function (r) { s += +r.value; });
    var max = br.querySelectorAll('input[type=range]').length * 10, pct = Math.round(s / max * 100);
    $('#burnoutPct').textContent = pct + '%';
    $('#burnoutBar').style.width = pct + '%';
    $('#burnoutMsg').textContent = pct < 35 ? 'Low strain. Keep recovery rituals in your calendar.' : pct < 65 ? 'Moderate strain. Watch sleep debt and protect one no-meeting block daily.' : 'High strain. Consider talking to a coach or clinician — and flag workload with your manager.';
  });
})();
