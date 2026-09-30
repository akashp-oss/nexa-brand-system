/* Artboard exporter (UI only, never part of an artboard).
   toSVG(ab) -> SVG markup: rects, clipped images, vector logo/notches/icons, live <text>.
                Paste straight into Figma (Ctrl/Cmd+V) for editable layers.
   Measures the artboard at 100% (the zoom transform is lifted while measuring). */
(function () {
  const N = v => Math.round(v * 100) / 100;
  const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  function hex(c) {
    const m = String(c).match(/rgba?\(([^)]+)\)/); if (!m) return c;
    const [r, g, b, a] = m[1].split(',').map(parseFloat);
    if (a === 0) return null;
    return '#' + [r, g, b].map(v => Math.round(v).toString(16).padStart(2, '0')).join('').toUpperCase();
  }
  const alpha = c => { const m = String(c).match(/rgba\([^)]*,\s*([\d.]+)\)/); return m ? parseFloat(m[1]) : 1; };
  const visible = el => { const cs = getComputedStyle(el); return cs.display !== 'none' && cs.visibility !== 'hidden'; };
  const skip = el => el.classList && (el.classList.contains('guide') || el.classList.contains('frame-tools'));
  const layerName = el => (el.dataset && el.dataset.name) || (el.tagName === 'IMG' ? 'Image' : 'Group');

  /* measure with the zoom transform removed so every coordinate is in artboard px */
  function measured(ab, fn) {
    const t = ab.style.transform; ab.style.transform = '';
    try { return fn(ab.getBoundingClientRect()); } finally { ab.style.transform = t; }
  }
  const relTo = R => el => { const r = el.getBoundingClientRect(); return { x: r.left - R.left, y: r.top - R.top, w: r.width, h: r.height }; };

  /* image placement for object-fit / object-position (px or %) */
  function imgBox(el, r) {
    const cs = getComputedStyle(el), nw = el.naturalWidth, nh = el.naturalHeight;
    const fit = cs.objectFit;
    const k = fit === 'cover' ? Math.max(r.w / nw, r.h / nh) : fit === 'contain' ? Math.min(r.w / nw, r.h / nh) : fit === 'none' ? 1 : null;
    const dw = k === null ? r.w : nw * k, dh = k === null ? r.h : nh * k;
    const pos = cs.objectPosition.split(' ');
    const off = (v, free) => v.endsWith('%') ? free * parseFloat(v) / 100 : parseFloat(v) || 0;
    return { fit, dw, dh, ox: off(pos[0] || '50%', r.w - dw), oy: off(pos[1] || '50%', r.h - dh) };
  }

  /* inline <svg> re-expressed as a transformed group (Figma keeps it as vectors) */
  function svgInner(el) {
    /* resolve currentColor per element (accent colours are CSS variables routed through `color`) */
    const cl = el.cloneNode(true), src = [el, ...el.querySelectorAll('*')], dst = [cl, ...cl.querySelectorAll('*')];
    src.forEach((s, i) => { const d = dst[i]; ['fill', 'stroke'].forEach(a => { if (s.getAttribute(a) === 'currentColor') d.setAttribute(a, hex(getComputedStyle(s).color) || '#000000'); });
      if (d.getAttribute('style') && /color:/.test(d.getAttribute('style'))) d.removeAttribute('style'); });
    const ser = new XMLSerializer();
    return [...cl.childNodes].map(n => ser.serializeToString(n)).join('').replace(/ xmlns="http:\/\/www\.w3\.org\/2000\/svg"/g, '');
  }
  function svgAttrs(el) {
    const color = hex(getComputedStyle(el).color) || '#000000';
    return ['fill', 'stroke', 'stroke-width', 'stroke-linecap', 'stroke-linejoin', 'fill-rule']
      .filter(a => el.hasAttribute(a)).map(a => `${a}="${esc(el.getAttribute(a).replace('currentColor', color))}"`).join(' ');
  }

  /* ascent share of the line box for the element's font (N27/Saira, Roboto), measured once per font */
  const _asc = new Map(), _cv = document.createElement('canvas').getContext('2d');
  function ascRatio(cs) {
    const key = cs.fontWeight + ' ' + cs.fontFamily; if (_asc.has(key)) return _asc.get(key);
    _cv.font = `${cs.fontWeight} 100px ${cs.fontFamily}`; const m = _cv.measureText('Hg');
    const v = m.fontBoundingBoxAscent / (m.fontBoundingBoxAscent + m.fontBoundingBoxDescent) || 0.8; _asc.set(key, v); return v;
  }
  /* the one family Figma should use: N27 if this machine has it, else the stand-in actually rendering (Saira / Roboto) */
  const _fam = new Map();
  function famName(stack) {
    if (_fam.has(stack)) return _fam.get(stack);
    const fams = stack.split(',').map(s => s.trim().replace(/^["']|["']$/g, ''));
    const w = f => { _cv.font = `72px "${f}", monospace`; return _cv.measureText('NEXA WHAT’S NEXT 0123').width; };
    const mono = (() => { _cv.font = '72px monospace'; return _cv.measureText('NEXA WHAT’S NEXT 0123').width; })();
    const pick = fams.find(f => /^(sans-serif|serif|monospace)$/.test(f) || Math.abs(w(f) - mono) > 0.5) || fams[0];
    _fam.set(stack, pick); return pick;
  }
  /* borders (dashed guides, outlined buttons) become stroked rects */
  function borderRect(el, r, cs) {
    const w = parseFloat(cs.borderTopWidth); if (!w || cs.borderTopStyle === 'none') return '';
    const dash = cs.borderTopStyle === 'dashed' ? ` stroke-dasharray="${N(w * 4)} ${N(w * 3)}"` : '';
    return `<rect x="${N(r.x + w / 2)}" y="${N(r.y + w / 2)}" width="${N(r.w - w)}" height="${N(r.h - w)}" fill="none" stroke="${hex(cs.borderTopColor)}" stroke-width="${N(w)}"${dash}/>`;
  }

  /* text: measure every character, group into runs by line and style, emit exact baselines */
  function textRuns(el, rel) {
    const runs = []; const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let n;
    const rg = document.createRange();
    while ((n = walker.nextNode())) {
      const p = n.parentElement, cs = getComputedStyle(p), fs = parseFloat(cs.fontSize);
      const style = { fill: hex(cs.color), weight: cs.fontWeight, size: fs, family: cs.fontFamily, ls: cs.letterSpacing === 'normal' ? 0 : parseFloat(cs.letterSpacing) };
      for (let i = 0; i < n.data.length; i++) {
        rg.setStart(n, i); rg.setEnd(n, i + 1);
        const b = rg.getClientRects()[0]; if (!b || b.width === 0) continue;
        const r = rel({ getBoundingClientRect: () => b });
        const ch = n.data[i].replace(/\s/, ' ');
        const last = runs[runs.length - 1];
        const baseline = r.y + r.h * ascRatio(cs);   // font ascent / content-area height, measured per font
        if (last && last.style.fill === style.fill && last.style.weight === style.weight && last.style.size === style.size && last.style.family === style.family && Math.abs(last.baseline - baseline) < fs * 0.3) last.text += ch;
        else runs.push({ style, x: r.x, baseline, text: ch });
      }
    }
    return runs.map(r => ({ ...r, text: r.text.replace(/\s+$/, '') })).filter(r => r.text);
  }

  function toSVG(ab) {
    return measured(ab, R => {
      const rel = relTo(R), defs = [], names = new Map(); let clipN = 0;
      const id = el => { const n = layerName(el); const c = (names.get(n) || 0) + 1; names.set(n, c); return esc(c > 1 ? `${n} ${c}` : n); };
      const clip = r => { const c = 'clip' + (++clipN); defs.push(`<clipPath id="${c}"><rect x="${N(r.x)}" y="${N(r.y)}" width="${N(r.w)}" height="${N(r.h)}"/></clipPath>`); return c; };
      function node(el) {
        if (el.nodeType !== 1 || skip(el) || !visible(el)) return '';
        const r = rel(el), cs = getComputedStyle(el);
        if (el.tagName.toLowerCase() === 'svg') {
          const vb = el.viewBox.baseVal; if (!vb || !vb.width) return '';
          let sx = r.w / vb.width, sy = r.h / vb.height, tx = r.x, ty = r.y;
          if (!/none/.test(el.getAttribute('preserveAspectRatio') || '')) { const k = Math.min(sx, sy); tx += (r.w - vb.width * k) / 2; ty += (r.h - vb.height * k) / 2; sx = sy = k; }
          return `<g id="${id(el)}" transform="translate(${N(tx - vb.x * sx)} ${N(ty - vb.y * sy)}) scale(${N(sx * 1e4) / 1e4} ${N(sy * 1e4) / 1e4})" ${svgAttrs(el)}>${svgInner(el)}</g>`;
        }
        if (el.tagName === 'IMG') {
          if (!el.naturalWidth) return '';
          const b = imgBox(el, r);
          const img = `<image xlink:href="${el.src}" x="${N(r.x + b.ox)}" y="${N(r.y + b.oy)}" width="${N(b.dw)}" height="${N(b.dh)}" preserveAspectRatio="none"/>`;
          return b.fit === 'cover' || b.dw > r.w + .5 || b.dh > r.h + .5 ? `<g id="${id(el)}" clip-path="url(#${clip(r)})">${img}</g>` : `<g id="${id(el)}">${img}</g>`;
        }
        let out = '';
        const bg = hex(cs.backgroundColor);
        const rad = parseFloat(cs.borderTopLeftRadius) || 0;
        if (bg) out += `<rect id="${el.classList.contains('shape') ? id(el) : 'Fill'}" x="${N(r.x)}" y="${N(r.y)}" width="${N(r.w)}" height="${N(r.h)}"${rad ? ` rx="${N(Math.min(rad, r.w / 2))}"` : ''} fill="${bg}"${alpha(cs.backgroundColor) < 1 ? ` fill-opacity="${N(alpha(cs.backgroundColor))}"` : ''}/>`;
        out += borderRect(el, r, cs);
        const gi = cs.backgroundImage;
        if (gi && gi.startsWith('linear-gradient(')) {   /* vertical gradients (photo shades) */
          const gid = 'grad' + (++clipN);
          const stops = [...gi.matchAll(/(rgba?\([^)]+\))\s*([\d.]+%)?/g)].map((m, i, a) => {
            const c = m[1].match(/[\d.]+/g).map(Number); const off = m[2] || (i / Math.max(1, a.length - 1) * 100 + '%');
            return `<stop offset="${off}" stop-color="${hex('rgb(' + c.slice(0, 3).join(',') + ')')}" stop-opacity="${c[3] ?? 1}"/>`; }).join('');
          defs.push(`<linearGradient id="${gid}" x1="0" y1="0" x2="0" y2="1">${stops}</linearGradient>`);
          out += `<rect id="${id(el)}" x="${N(r.x)}" y="${N(r.y)}" width="${N(r.w)}" height="${N(r.h)}" fill="url(#${gid})"/>`;
        }
        if (el.classList.contains('tx')) {
          const spans = textRuns(el, rel).map(t => `<tspan x="${N(t.x)}" y="${N(t.baseline)}" fill="${t.style.fill}" font-size="${N(t.style.size)}" font-family="${esc(famName(t.style.family))}" font-weight="${t.style.weight}"${t.style.ls ? ` letter-spacing="${N(t.style.ls)}"` : ''}>${esc(t.text)}</tspan>`).join('');
          return out + `<text id="${id(el)}" xml:space="preserve">${spans}</text>`;
        }
        const kids = [...el.children].map(node).join('');
        if (el.classList.contains('shape')) return out + kids;
        const clipAttr = cs.overflow === 'hidden' ? ` clip-path="url(#${clip(r)})"` : '';
        return kids ? `<g id="${id(el)}"${clipAttr}>${out}${kids}</g>` : out;
      }
      const W = N(R.width), H = N(R.height), bg = hex(getComputedStyle(ab).backgroundColor) || '#FFFFFF';
      const body = [...ab.children].map(node).join('');
      return `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`
        + `<defs>${defs.join('')}<clipPath id="artboard"><rect width="${W}" height="${H}"/></clipPath></defs>`
        + `<g id="${esc(ab.dataset.name || 'Artboard')}" clip-path="url(#artboard)"><rect id="Background" width="${W}" height="${H}" fill="${bg}"/>${body}</g></svg>`;
    });
  }

  window.nexaExport = { toSVG };
})();
