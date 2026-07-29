// Confialy — shared front-end behavior (no build step, vanilla JS)

document.addEventListener('DOMContentLoaded', () => {
  // Mobile nav toggle
  const toggle = document.querySelector('.nav__toggle');
  const links = document.querySelector('.nav__links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('nav__links--open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Contact form handling
  const form = document.getElementById('contact-form');
  if (form) {
    const msg = document.getElementById('form-msg');
    const submitBtn = form.querySelector('button[type="submit"]');
    const msgs = {
      ok: form.dataset.msgOk,
      notConnected: form.dataset.msgNotConnected,
      serverErr: form.dataset.msgServerErr,
      sending: form.dataset.msgSending,
      submit: form.dataset.msgSubmit,
    };

    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      // Honeypot spam trap — if filled, silently pretend success and stop.
      if (form.querySelector('input[name="company_website"]').value) {
        showMsg('ok', msgs.ok);
        form.reset();
        return;
      }

      const endpoint = form.getAttribute('data-endpoint');
      const placeholder = !endpoint || endpoint.includes('YOUR_FORM_ID');

      if (placeholder) {
        // No live form backend configured yet — explain instead of failing silently.
        showMsg('err', msgs.notConnected);
        return;
      }

      submitBtn.disabled = true;
      submitBtn.textContent = msgs.sending;

      try {
        const res = await fetch(endpoint, {
          method: 'POST',
          headers: { Accept: 'application/json' },
          body: new FormData(form),
        });

        if (res.ok) {
          showMsg('ok', msgs.ok);
          form.reset();
        } else {
          showMsg('err', msgs.serverErr);
        }
      } catch (err) {
        showMsg('err', msgs.serverErr);
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = msgs.submit;
      }
    });

    function showMsg(type, text) {
      msg.textContent = text;
      msg.className = 'form-msg form-msg--' + type;
      msg.style.display = 'block';
      msg.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  // Mark current nav link
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__links a').forEach((a) => {
    const href = a.getAttribute('href');
    if (href === path || (path === '' && href === 'index.html')) {
      a.setAttribute('aria-current', 'page');
    }
  });
});
