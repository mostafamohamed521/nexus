/* ============================================================
   NEXUS — Main JavaScript
   Handles: Nav scroll, mobile menu, animations, form UX
   ============================================================ */

'use strict';

/* ── Nav: add .scrolled class on scroll ─────────────────── */
const nav = document.querySelector('.nav');
if (nav) {
  const onScroll = () => {
    nav.classList.toggle('scrolled', window.scrollY > 20);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* ── Mobile nav toggle ───────────────────────────────────── */
const toggle = document.querySelector('.nav__toggle');
const navLinks = document.querySelector('.nav__links');
const navActions = document.querySelector('.nav__actions');

if (toggle) {
  toggle.addEventListener('click', () => {
    const isOpen = toggle.classList.toggle('open');
    navLinks?.classList.toggle('open', isOpen);
    navActions?.classList.toggle('open', isOpen);
    toggle.setAttribute('aria-expanded', isOpen);
  });

  // Close on outside click
  document.addEventListener('click', (e) => {
    if (!nav.contains(e.target)) {
      toggle.classList.remove('open');
      navLinks?.classList.remove('open');
      navActions?.classList.remove('open');
    }
  });
}

/* ── Scroll-triggered animations ────────────────────────── */
const observerOpts = { threshold: 0.12, rootMargin: '0px 0px -40px 0px' };

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, observerOpts);

// Stagger children of [data-stagger] containers
document.querySelectorAll('[data-stagger] > *').forEach((el, i) => {
  el.style.animationDelay = `${i * 80}ms`;
  el.classList.add('reveal');
  revealObserver.observe(el);
});

// Single-element reveals
document.querySelectorAll('[data-reveal]').forEach((el) => {
  el.classList.add('reveal');
  revealObserver.observe(el);
});

// CSS for reveal (injected once)
const style = document.createElement('style');
style.textContent = `
  .reveal {
    opacity: 0;
    transform: translateY(24px);
    transition: opacity 0.6s cubic-bezier(0.22,1,0.36,1), transform 0.6s cubic-bezier(0.22,1,0.36,1);
  }
  .reveal.visible { opacity: 1; transform: none; }
`;
document.head.appendChild(style);

/* ── Counter animation (for hero stats) ─────────────────── */
function animateCounter(el) {
  const target = parseInt(el.dataset.count, 10);
  const duration = 1800;
  const start = performance.now();

  const step = (now) => {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3); // ease-out-cubic
    el.textContent = Math.floor(eased * target).toLocaleString() + (el.dataset.suffix || '');
    if (progress < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      animateCounter(entry.target);
      counterObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('[data-count]').forEach((el) => counterObserver.observe(el));

/* ── Active nav link highlighting ────────────────────────── */
const currentPath = window.location.pathname;
document.querySelectorAll('.nav__links a').forEach((link) => {
  const href = link.getAttribute('href');
  if (href === currentPath || (href !== '/' && currentPath.startsWith(href))) {
    link.classList.add('active');
  }
});

/* ── Auto-dismiss alerts ─────────────────────────────────── */
document.querySelectorAll('.alert').forEach((alert) => {
  const close = alert.querySelector('.alert-close');
  if (close) {
    close.addEventListener('click', () => {
      alert.style.transition = 'opacity 0.3s, transform 0.3s';
      alert.style.opacity = '0';
      alert.style.transform = 'translateX(10px)';
      setTimeout(() => alert.remove(), 350);
    });
  }
  // Auto-dismiss success messages
  if (alert.classList.contains('success')) {
    setTimeout(() => {
      if (alert.isConnected) {
        alert.style.transition = 'opacity 0.5s';
        alert.style.opacity = '0';
        setTimeout(() => alert.remove(), 500);
      }
    }, 5000);
  }
});

/* ── Smooth scroll for anchor links ─────────────────────── */
document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener('click', (e) => {
    const target = document.querySelector(link.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

/* ── Form: disable submit on pending, show loading ───────── */
document.querySelectorAll('form').forEach((form) => {
  form.addEventListener('submit', (e) => {
    const submit = form.querySelector('[type="submit"]');
    if (submit && !submit.disabled) {
      submit.disabled = true;
      const original = submit.innerHTML;
      submit.innerHTML = '<span style="display:inline-flex;gap:6px;align-items:center"><svg width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="2" stroke-dasharray="28" stroke-dashoffset="10" style="animation:spin 0.8s linear infinite;transform-origin:center"></svg> Sending...</span>';
      // Re-enable if there's a validation error (Django will reload the page anyway)
      setTimeout(() => { submit.disabled = false; submit.innerHTML = original; }, 8000);
    }
  });
});
