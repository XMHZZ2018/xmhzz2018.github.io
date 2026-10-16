(function () {
  'use strict';
  const gallery = document.querySelector('.author__portraits');
  if (!gallery) return;
  const toggle = gallery.querySelector('.author__photo-toggle');
  const frame = gallery.querySelector('.author__avatar');
  const photos = Array.from(toggle.querySelectorAll('img'));
  const status = gallery.querySelector('.author__photo-status');
  let current = 0;
  let ready = false;
  let pressedPointerType = '';
  const hover = matchMedia('(hover: hover)');

  function show(index, announce) {
    if (!ready || current === index) return;
    current = index;
    photos.forEach(function (photo, i) {
      photo.classList.toggle('is-active', i === current);
      photo.setAttribute('aria-hidden', String(i !== current));
    });
    if (announce) status.textContent = 'Photo ' + (current + 1) + ' of ' + photos.length;
  }

  // Keep the original photo if the second image cannot load.
  function enable() {
    if (ready || !photos[1].naturalWidth) return;
    ready = true;
    photos[1].hidden = false;
    gallery.classList.add('has-secondary');
    toggle.disabled = false;
    if (hover.matches && frame.matches(':hover')) show(1);
  }
  photos[1].addEventListener('load', enable, {once: true});
  if (photos[1].complete) enable();

  frame.addEventListener('pointerenter', function (event) {
    if (hover.matches && event.pointerType === 'mouse') show(1);
  });
  frame.addEventListener('pointerleave', function (event) {
    if (hover.matches && event.pointerType === 'mouse') show(0);
  });
  toggle.addEventListener('pointerdown', function (event) {
    pressedPointerType = event.pointerType;
  });
  toggle.addEventListener('pointercancel', function () {
    pressedPointerType = '';
  });
  toggle.addEventListener('click', function (event) {
    // Safari can label a touch-generated click as mouse: use the actual press.
    const input = pressedPointerType || event.pointerType;
    pressedPointerType = '';
    if (hover.matches && input === 'mouse' && event.detail > 0) return;
    show(1 - current, true);
  });
  toggle.addEventListener('keydown', function (event) {
    if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight') return;
    event.preventDefault();
    show(1 - current, true);
  });
})();
