// node brand/logo/extract_official.js : reads the official NEXA_LogoSystem SVGs (Super Blue versions),
// crops each to its artwork bounds and writes brand/logo/logo.json (markup with fills removed) + clean SVGs.
const { chromium } = require('playwright'), fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '../..'), LS = path.join(ROOT, 'NEXA_LogoSystem');
const SRC = { wordmark: 'NEXA_MainWordmark/SVG/NEXA_MainWordmark_SuperBlue.svg',
              wordmark_tagline: 'NEXA_MainWordmark_Tagline/SVG/NEXA_MainWordmark_Tagline_SuperBlue.svg',
              emblem: 'NEXA_Emblem/SVG/NEXA_Emblem_SuperBlue-01.svg' };
(async () => {
  const b = await chromium.launch(), p = await b.newPage(), out = {};
  for (const [k, f] of Object.entries(SRC)) {
    await p.setContent(fs.readFileSync(path.join(LS, f), 'utf8'));
    out[k] = await p.evaluate(() => {
      const svg = document.querySelector('svg');
      const shapes = [...svg.querySelectorAll('path,polygon,rect,circle,ellipse,polyline')].filter(e => !e.closest('defs,clipPath'));
      const r = (n) => Math.round(n * 100) / 100;
      let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
      const parts = shapes.map(e => { const bb = e.getBBox(); x0 = Math.min(x0, bb.x); y0 = Math.min(y0, bb.y); x1 = Math.max(x1, bb.x + bb.width); y1 = Math.max(y1, bb.y + bb.height);
        const c = e.cloneNode(); ['class', 'id', 'style', 'fill'].forEach(a => c.removeAttribute(a));
        return { html: c.outerHTML.replace(/ xmlns="[^"]*"/, '').replace(/\s+/g, ' '), x: bb.x, w: bb.width, h: bb.height }; });
      return { x: r(x0), y: r(y0), w: r(x1 - x0), h: r(y1 - y0), parts };
    });
  }
  await b.close();
  const g = (o, parts) => `<g transform="translate(${-o.x} ${-o.y})">${parts.map(q => q.html).join('')}</g>`;
  const wm = out.wordmark, tmLimit = wm.x + wm.w * 0.97;
  const noTm = wm.parts.filter(q => q.h > wm.h * 0.3);           // drop the small TM glyphs
  const nx1 = Math.max(...noTm.map(q => q.x + q.w));
  const em = out.emblem, halves = em.parts.slice().sort((a, b) => a.x - b.x);   // [left '>', right '<']
  const json = {
    source: 'NEXA_LogoSystem (official Illustrator SVG exports), cropped to artwork bounds',
    wordmark: { w: wm.w, h: wm.h, inner: g(wm, wm.parts) },
    wordmark_notm: { w: Math.round((nx1 - wm.x) * 100) / 100, h: wm.h, inner: g(wm, noTm) },
    wordmark_tagline: { w: out.wordmark_tagline.w, h: out.wordmark_tagline.h, inner: g(out.wordmark_tagline, out.wordmark_tagline.parts) },
    emblem: { w: em.w, h: em.h, inner: g(em, em.parts), left: g(em, [halves[0]]), right: g(em, [halves[1]]), half: Math.round((halves[1].x - em.x) * 100) / 100 },
  };
  fs.writeFileSync(path.join(__dirname, 'logo.json'), JSON.stringify(json, null, 1));
  const cols = { 'super-blue': '#1F1FCC', white: '#FFFFFF', black: '#000000', 'base-gray': '#C9C7C9' };
  for (const k of ['wordmark', 'wordmark_tagline', 'emblem']) for (const [cn, c] of Object.entries(cols))
    fs.writeFileSync(path.join(__dirname, `nexa-${k.replace('_', '-')}-${cn}.svg`),
      `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${json[k].w} ${json[k].h}" fill="${c}">${json[k].inner}</svg>\n`);
  console.log(Object.fromEntries(Object.entries(json).filter(([k]) => k !== 'source').map(([k, v]) => [k, [v.w, v.h, v.inner.length]])));
})();
