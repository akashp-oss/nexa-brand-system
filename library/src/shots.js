// QA screenshots: node library/src/shots.js  ->  .qa/ui-*.png and .qa/ab-<id>.png (every artboard at 100%)
// Also fails on page errors and on any template whose text overflows its artboard.
const { chromium } = require('playwright'), path = require('path'), fs = require('fs');
const ROOT = path.resolve(__dirname, '../..'), OUT = path.join(ROOT, '.qa');
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch(); const errs = [];
  const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + path.join(ROOT, 'library/dist/NEXA_Brand_Asset_Library.html')); await p.waitForTimeout(1200);
  await p.screenshot({ path: path.join(OUT, 'ui-top.png') });
  await p.evaluate(() => document.querySelector('#sec-found').scrollIntoView()); await p.waitForTimeout(300);
  await p.screenshot({ path: path.join(OUT, 'ui-section.png') });
  const m = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  await m.goto('file://' + path.join(ROOT, 'library/dist/NEXA_Brand_Asset_Library.html')); await m.waitForTimeout(1200);
  await m.screenshot({ path: path.join(OUT, 'ui-mobile.png') });
  const hscroll = await m.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
  await p.evaluate(() => window.lib.setFigma(true)); await p.addStyleTag({ content: '.figma-bar,.toast{display:none!important}' }); await p.waitForTimeout(300);
  const ids = await p.$$eval('.frame', fs => fs.map(f => f.id));
  const overflow = await p.$$eval('.ab', abs => abs.flatMap(ab => { const R = ab.getBoundingClientRect();
    return [...ab.querySelectorAll('.tx')].filter(t => { const r = t.getBoundingClientRect(); return r.right > R.right + 1 || r.bottom > R.bottom + 1 || r.left < R.left - 1; })
      .map(t => ab.dataset.name + ' → ' + t.dataset.name); }));
  for (const id of ids) await (await p.$('#' + id + ' .ab')).screenshot({ path: path.join(OUT, 'ab-' + id + '.png') });
  console.log(ids.length, 'artboards'); if (overflow.length) console.log('TEXT OVERFLOW:', overflow);
  if (hscroll) console.log('MOBILE: horizontal scroll');
  if (errs.length) console.log('ERRORS:', errs);
  await b.close(); process.exit(errs.length ? 1 : 0);
})();
