(function () {
  // Mobile navigation
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('mobile-nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Missed-call calculator
  var calc = document.querySelector('[data-calc]');
  if (calc) {
    var f = function (n) { return Number(calc.querySelector('[name="' + n + '"]').value) || 0; };
    var out = calc.querySelector('[data-out]');
    var jobs = calc.querySelector('[data-jobs]');
    var run = function () {
      var j = f('missed') * (f('rate') / 100) * 4.33;
      out.textContent = '$' + Math.round(j * f('value')).toLocaleString('en-US');
      jobs.textContent = j.toFixed(1);
    };
    calc.addEventListener('input', run);
    run();
  }

  // Lead form. Set data-endpoint on the form to a Formspree / Web3Forms / n8n webhook URL.
  // With no endpoint, the form opens the visitor's email app with the details filled in.
  document.querySelectorAll('form[data-lead]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('.form-status');
      var data = new FormData(form);
      if (data.get('company_website')) return; // honeypot
      var required = ['name', 'email', 'phone'];
      for (var i = 0; i < required.length; i++) {
        if (!String(data.get(required[i]) || '').trim()) {
          status.className = 'form-status err';
          status.textContent = 'Add your ' + required[i] + ' so we can reach you.';
          form.querySelector('[name="' + required[i] + '"]').focus();
          return;
        }
      }
      var endpoint = form.getAttribute('data-endpoint');
      if (!endpoint) {
        var body = 'Name: ' + data.get('name') + '\nEmail: ' + data.get('email') + '\nPhone: ' + data.get('phone') +
          '\nTrade: ' + (data.get('trade') || '') + '\n\n' + (data.get('message') || '');
        window.location.href = 'mailto:support@topdispatchcrm.com?subject=' +
          encodeURIComponent('New lead from website: ' + data.get('name')) + '&body=' + encodeURIComponent(body);
        status.className = 'form-status ok';
        status.textContent = 'Your email app is opening with your details. Send it and we reply within a few hours.';
        return;
      }
      var b = form.querySelector('button[type="submit"]');
      b.disabled = true;
      var payload = {};
      data.forEach(function (v, k) { if (k !== 'company_website') payload[k] = v; });
      payload.page = window.location.href;
      fetch(endpoint, { method: 'POST', body: JSON.stringify(payload), headers: { 'Content-Type': 'application/json', Accept: 'application/json' } })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || String(res.j && res.j.success) === 'false') throw new Error();
          form.reset();
          status.className = 'form-status ok';
          status.textContent = 'Details sent. Our team will contact you within a few hours.';
        })
        .catch(function () {
          status.className = 'form-status err';
          status.textContent = 'Your details did not send. Call (833) 505-4136 or email support@topdispatchcrm.com.';
        })
        .finally(function () { b.disabled = false; });
    });
  });
})();
