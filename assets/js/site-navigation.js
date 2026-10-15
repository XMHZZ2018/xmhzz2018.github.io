(function () {
  'use strict';
  const nav = document.querySelector('.site-navigation');
  if (!nav) return;
  const links = Array.from(nav.querySelectorAll('.site-navigation__links a'));
  const sections = links.map(function (link) {
    return {link: link, element: document.getElementById(new URL(link.href).hash.slice(1))};
  }).filter(function (section) { return section.element; });
  if (!sections.length) return;

  function updateCurrent() {
    let current = sections[0];
    const threshold = nav.getBoundingClientRect().bottom + 40;
    sections.forEach(function (section) {
      if (section.element.getBoundingClientRect().top <= threshold) current = section;
    });
    if (window.scrollY > 0 && window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2) {
      current = sections[sections.length - 1];
    }
    sections.forEach(function (section) {
      if (section === current) section.link.setAttribute('aria-current', 'location');
      else section.link.removeAttribute('aria-current');
    });
  }

  // Handle navigation before the theme's older jQuery scroll handler.
  nav.addEventListener('click', function (event) {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const link = event.target.closest('a');
    if (!link) return;
    const url = new URL(link.href);
    if (url.origin !== location.origin || url.pathname !== location.pathname) return;
    const target = document.getElementById(url.hash.slice(1));
    if (url.hash && !target) return;
    event.preventDefault();
    event.stopPropagation();
    const top = !target || target.id === 'about-me' ? 0 :
      target.getBoundingClientRect().top + window.scrollY - nav.offsetHeight - 24;
    history.pushState(null, '', url.pathname + url.search + url.hash);
    window.scrollTo({top: Math.max(0, top), behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
  }, true);

  let pending = false;
  window.addEventListener('scroll', function () {
    if (pending) return;
    pending = true;
    requestAnimationFrame(function () { updateCurrent(); pending = false; });
  }, {passive: true});
  window.addEventListener('resize', updateCurrent);
  updateCurrent();
})();
