/* Views (Asset library / Brand guidelines) and the live secondary-colour switcher. */
(function () {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const ACCENTS = __ACCENTS__;
  const store = { get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } },
                  set: (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} } };
  const IMG = JSON.parse(document.getElementById('img-data').textContent);
  $$('[data-ui-img]').forEach(el => { if (IMG[el.dataset.uiImg]) el.setAttribute('href', IMG[el.dataset.uiImg]); });

  function setView(v, scroll) {
    document.body.dataset.view = v;
    $$('[data-view-btn]').forEach(b => b.classList.toggle('on', b.dataset.viewBtn === v));
    if (window.lib) window.lib.layout();
    if (scroll !== false) window.scrollTo(0, 0);
    const u = new URL(location.href); if (v === 'guide') u.searchParams.set('view', 'guide'); else u.searchParams.delete('view');
    history.replaceState(null, '', u.pathname + u.search + u.hash);
  }
  $$('[data-view-btn]').forEach(b => b.onclick = () => setView(b.dataset.viewBtn));
  /* deep links: ?view=guide, or a hash that points into the other view */
  const target = location.hash && document.getElementById(location.hash.slice(1));
  const tv = target && target.closest('[data-view]');
  setView(new URLSearchParams(location.search).get('view') === 'guide' || (tv && tv.dataset.view === 'guide') ? 'guide' : 'library', false);
  if (target) setTimeout(() => target.scrollIntoView(), 50);

  function setAccent(key) {
    const a = ACCENTS.find(x => x.key === key) || ACCENTS[0];
    document.documentElement.style.setProperty('--acc', a.acc);
    document.documentElement.style.setProperty('--tint', a.tint);
    $$('[data-accent]').forEach(b => b.classList.toggle('on', b.dataset.accent === a.key));
    store.set('nexa-accent', a.key);
    return a;
  }
  setAccent(store.get('nexa-accent') || ACCENTS[0].key);
  $$('[data-accent]').forEach(b => b.onclick = () => {
    const a = setAccent(b.dataset.accent);
    const t = $('#toast'); t.textContent = `Secondary colour: ${a.name} ${a.acc}`; t.classList.add('show');
    clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('show'), 2200);
  });
})();
