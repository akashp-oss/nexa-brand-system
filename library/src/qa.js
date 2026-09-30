// Layout QA: node library/src/qa.js  -> lists, per artboard, text that overlaps other text or a logo,
// text/logos outside the artboard margin, and wordmarks below 120 px wide. Exit code 1 if anything is found.
const { chromium } = require('playwright'), path = require('path');
const ROOT = path.resolve(__dirname, '../..');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1600, height: 1000 } });
  await p.goto('file://' + path.join(ROOT, 'library/dist/NEXA_Brand_Asset_Library.html')); await p.waitForTimeout(1500);
  await p.evaluate(() => window.lib.setFigma(true)); await p.waitForTimeout(300);
  const res = await p.$$eval('.frame', frames => frames.map(f => {
    const ab = f.querySelector('.ab'), R = ab.getBoundingClientRect(), fmt = f.dataset.fmt, issues = [];
    const box = el => { const r = el.getBoundingClientRect(); return { x: r.left - R.left, y: r.top - R.top, w: r.width, h: r.height, n: el.dataset.name }; };
    /* tight text boxes: union of line rects of the text itself */
    const tbox = el => { const rg = document.createRange(); rg.selectNodeContents(el); const rs = [...rg.getClientRects()].filter(r => r.width > 1);
      if (!rs.length) return null; const x0 = Math.min(...rs.map(r => r.left)), y0 = Math.min(...rs.map(r => r.top)), x1 = Math.max(...rs.map(r => r.right)), y1 = Math.max(...rs.map(r => r.bottom));
      const fs = parseFloat(getComputedStyle(el).fontSize), trim = Math.min(fs * .22, (y1 - y0) / 4);   /* glyphs sit inside the line box */
      return { x: x0 - R.left, y: y0 - R.top + trim, w: x1 - x0, h: y1 - y0 - trim * 1.6, n: el.dataset.name }; };
    const ov = (a, c, pad = 0) => a.x < c.x + c.w - pad && c.x < a.x + a.w - pad && a.y < c.y + c.h - pad && c.y < a.y + a.h - pad;
    const texts = [...ab.querySelectorAll('.tx')].filter(t => !t.closest('.logo')).map(tbox).filter(Boolean);
    const logos = [...ab.querySelectorAll('.logo')].map(box).filter(l => !/watermark/i.test(l.n));
    const inside = (a, c) => a.x >= c.x - 1 && a.y >= c.y - 1 && a.x + a.w <= c.x + c.w + 1 && a.y + a.h <= c.y + c.h + 1;
    for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++)
      if (ov(texts[i], texts[j], 2) && !inside(texts[i], texts[j]) && !inside(texts[j], texts[i])) issues.push(`text overlap: "${texts[i].n}" × "${texts[j].n}"`);
    for (const t of texts) for (const l of logos) if (ov(t, l, 2)) issues.push(`text on logo: "${t.n}" × ${l.n}`);
    for (let i = 0; i < logos.length; i++) for (let j = i + 1; j < logos.length; j++) if (ov(logos[i], logos[j], 1)) issues.push(`logo overlap: ${logos[i].n} × ${logos[j].n}`);
    const m = fmt === 'print' ? 24 : fmt === 'doc' ? 20 : 16;
    for (const t of [...texts, ...logos]) if (t.x < m || t.y < m || t.x + t.w > R.width - m || t.y + t.h > R.height - m) issues.push(`outside margin: "${t.n}"`);
    for (const l of logos) if (/wordmark/i.test(l.n) && Math.max(l.w, l.h) < 120 && fmt !== 'doc' && fmt !== 'web') issues.push(`small wordmark: ${Math.round(l.w)}px`);
    return { id: f.id, issues };
  }));
  let n = 0; for (const r of res) if (r.issues.length) { n += r.issues.length; console.log(r.id + '\n  ' + [...new Set(r.issues)].join('\n  ')); }
  console.log(n ? `\n${n} issues` : 'no layout issues'); await b.close(); process.exit(n ? 1 : 0);
})();
