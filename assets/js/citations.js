(function () {
  'use strict';
  const settings = document.currentScript.dataset;
  const badge = document.getElementById('scholar-citations');
  if (!badge) return;
  let displayedAt = -Infinity;

  function render(data) {
    const updatedAt = Date.parse(data.updated);
    if (data.scholar_id !== settings.scholarId || !Number.isFinite(updatedAt) ||
        updatedAt < displayedAt || !Number.isInteger(data.citedby) || data.citedby < 0) return;
    displayedAt = updatedAt;
    const count = data.citedby.toLocaleString('en-US');
    const date = new Date(updatedAt).toLocaleDateString('en-US', {
      year: 'numeric', month: 'short', day: 'numeric', timeZone: 'UTC'
    });
    document.getElementById('total_cit').textContent = count;
    badge.title = 'Google Scholar · Updated ' + date + ' (UTC)';
    badge.setAttribute('aria-label', 'Google Scholar: ' + count + ' citations. Updated ' + date);
    badge.hidden = false;
  }

  async function load(url) {
    const controller = new AbortController();
    const timeout = setTimeout(function () { controller.abort(); }, 8000);
    try {
      const response = await fetch(url, {signal: controller.signal, cache: 'no-cache'});
      if (response.ok) render(await response.json());
    } catch (_) {
      // Keep the last successful snapshot when the remote data is unavailable.
    } finally {
      clearTimeout(timeout);
    }
  }

  load(settings.fallbackUrl);
  load(settings.scholarUrl);
})();
