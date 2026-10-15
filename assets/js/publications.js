(function () {
  'use strict';
  const root = document.querySelector('[data-publications]');
  if (!root) return;
  const papers = Array.from(root.querySelectorAll('.publication'));
  const filters = root.querySelector('.publication-filters');
  const buttons = Array.from(root.querySelectorAll('[data-publication-filter]'));
  let selected = 'all';

  function matchesFilter(paper, filter) {
    const contribution = paper.dataset.role;
    const isLead = contribution === 'lead' || contribution === 'cofirst';
    return filter === 'all' ||
      (filter === 'featured' && (isLead || contribution === 'mentored')) ||
      paper.dataset.topics.split(' ').includes(filter);
  }

  buttons.forEach(function (button) {
    const count = papers.filter(function (paper) {
      return matchesFilter(paper, button.dataset.publicationFilter);
    }).length;
    const label = button.textContent.trim();
    const counter = document.createElement('span');
    counter.className = 'publication-filter-count';
    counter.textContent = count;
    counter.setAttribute('aria-hidden', 'true');
    button.appendChild(counter);
    button.setAttribute('aria-label', label + ', ' + count + (count === 1 ? ' publication' : ' publications'));
  });

  function update() {
    let count = 0;
    papers.forEach(function (paper) {
      paper.hidden = !matchesFilter(paper, selected);
      if (!paper.hidden) count += 1;
    });
    buttons.forEach(function (button) {
      button.setAttribute('aria-pressed', String(button.dataset.publicationFilter === selected));
    });
    root.querySelector('.publication-results').textContent =
      'Showing ' + count + ' of ' + papers.length + ' publications';
  }

  root.addEventListener('click', function (event) {
    const button = event.target.closest('[data-publication-filter]');
    if (!button || !root.contains(button)) return;
    selected = button.dataset.publicationFilter;
    update();
  });

  update();
  filters.hidden = false;
})();
