# NEXA brand asset library generator helpers -> one self-contained HTML file.
# Every template is plain positioned HTML so it can be edited in the browser, copied to Figma as SVG,
# or imported with an HTML-to-Figma plugin. Layer names come from data-name.
import json, re, html as H
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]          # repo root

# ---------------------------------------------------------------- brand palette (brandbook p.14)
BLUE, GRAY, TURQ, PINK, PURPLE, BLACK = '#1F1FCC', '#C9C7C9', '#36FFE8', '#FF5FEB', '#2D0685', '#000000'
WHITE = '#FFFFFF'
# Secondary / accent colour is a live CSS variable so the library can compare options (see ACCENTS).
ACC, TINT = 'var(--acc)', 'var(--tint)'
# Extended palette sampled from NEXA's own assets (Asset Inspiration, MWC video, one-pagers)
MIDNIGHT, ELECTRIC, SKY = '#00133A', '#0068F4', '#00A1F6'
ACCENTS = [  # key, name, accent (marks and labels on blue/midnight), tint (light grounds, X watermark), note
    ('azure', 'Electric Azure', '#3AA8FF', '#E9F2FF', 'Recommended. Sampled from NEXA’s own backgrounds and MWC visuals: light, not neon. Pairs with Midnight #00133A.'),
    ('turquoise', 'Bright Turquoise', '#36FFE8', '#E3FFFC', 'Brandbook tertiary. Use as a thin line of light, never as a flat fill.'),
    ('lavender', 'Periwinkle', '#A6A8FF', '#ECECFC', 'Earlier experiment. Soft and premium, but not seen in NEXA’s own work.'),
    ('stone', 'Base Gray', '#C9C7C9', '#F1F0F1', 'The brandbook secondary on its own. Quiet and very safe.'),
]
PALETTE = [  # name, hex, rgb, cmyk, pantone, role
    ('Super Blue', BLUE, '31 31 204', '88 85 0 0', '2736 C', 'Primary'),
    ('Base Gray', GRAY, '201 199 201', '21 18 16 0', 'Cool Gray 3 U', 'Secondary'),
    ('Bright Turquoise', TURQ, '54 255 232', '60 0 27 0', '333 C', 'Tertiary'),
    ('Bright Pink', PINK, '255 95 235', '15 75 0 0', '807 C', 'Tertiary'),
    ('Dark Purple', PURPLE, '45 6 133', '93 100 7 9', '2685 C', 'Tertiary'),
    ('Space Black', BLACK, '0 0 0', '75 68 67 90', 'Black C', 'Tertiary'),
]
# approved background -> logo pairings (brandbook p.15) and forbidden pairs (p.16)
PAIRS_OK = [(TURQ, BLUE), (GRAY, BLUE), (PURPLE, TURQ), (BLACK, BLUE), (BLUE, GRAY), (TURQ, PURPLE)]
PAIRS_NO = [(PINK, TURQ), (PURPLE, BLUE), (BLACK, PURPLE), (BLUE, PURPLE), (GRAY, TURQ), (TURQ, PINK)]

HEAD = "'N27','Saira',sans-serif"          # N27 is licensed; Saira is the open stand-in
BODY = "Roboto,Arial,sans-serif"

LOGO = json.load(open(ROOT / 'brand/logo/logo.json'))
WM, WMN, WMT, EM = LOGO['wordmark'], LOGO['wordmark_notm'], LOGO['wordmark_tagline'], LOGO['emblem']
EM_HALF = EM['half']
def _clipmarkup(inner):
    """clipPath can't hold <g>: move the group's translate onto each shape."""
    m = re.match(r'<g transform="([^"]+)">(.*)</g>$', inner, re.S)
    return re.sub(r'<(path|polygon|rect)\b', lambda k: f'<{k.group(1)} transform="{m.group(1)}"', m.group(2))
EM_CLIP = _clipmarkup(EM['inner'])

def esc(s): return H.escape(s, quote=True)
def st(d): return ';'.join(f'{k}:{v}' for k, v in d.items() if v is not None)
def px(v): return f'{v}px' if isinstance(v, (int, float)) else v

def box(name, l=None, t=None, w=None, h=None, r=None, b=None, cls='', style=None, inner='', tag='div'):
    s = {'left': px(l) if l is not None else None, 'top': px(t) if t is not None else None, 'right': px(r) if r is not None else None,
         'bottom': px(b) if b is not None else None, 'width': px(w) if w is not None else None, 'height': px(h) if h is not None else None}
    s.update(style or {})
    positioned = any(v is not None for v in (l, t, r, b))
    return f'<{tag} class="{"abs " if positioned else ""}{cls}" data-name="{esc(name)}" style="{st(s)}">{inner}</{tag}>'

def fill(name, color, style=None, **k):
    sty = {'background': color}; sty.update(style or {})
    return box(name, cls='shape', style=sty, **k)

def line(name, color, l, t, w=None, h=None):
    return fill(name, color, l=l, t=t, w=w if w is not None else 1, h=h if h is not None else 1)

def text(name, content, cls, color=None, size=None, extra=None, tag='div'):
    """content: \\n = line break, **x** = accent run (colour from --em on the artboard or `extra['--em']`)."""
    parts = []
    for i, seg in enumerate(content.split('**')):
        seg = esc(seg).replace('\n', '<br>')
        parts.append(f'<span class="em" data-name="Accent">{seg}</span>' if i % 2 else seg)
    s = {'color': color, 'font-size': px(size) if size else None}
    s.update(extra or {})
    return f'<{tag} class="tx {cls}" data-name="{esc(name)}" style="{st(s)}">{"".join(parts)}</{tag}>'

def T(name, content, cls, color, size, l=None, t=None, w=None, r=None, b=None, extra=None):
    """positioned text"""
    e = {'left': px(l) if l is not None else None, 'top': px(t) if t is not None else None, 'width': px(w) if w is not None else None,
         'right': px(r) if r is not None else None, 'bottom': px(b) if b is not None else None}
    e.update(extra or {})
    return text(name, content, cls + ' abs', color, size, e)

def stack(name, items, l=None, t=None, w=None, gap=0, r=None, b=None, style=None, cls=''):
    s = {'gap': px(gap)}; s.update(style or {})
    return box(name, l=l, t=t, w=w, r=r, b=b, cls='stack ' + cls, style=s, inner=''.join(items))

def photo(name, key, l=0, t=0, w=100, h=100, pos='50% 50%', r=None, b=None):
    return (f'<img class="abs photo" data-name="{esc(name)}" data-img="{key}" alt="{esc(name)}" '
            f'style="{st({"left": px(l) if l is not None else None, "top": px(t) if t is not None else None, "right": px(r) if r is not None else None, "bottom": px(b) if b is not None else None, "width": px(w), "height": px(h), "object-position": pos})}">')

# ---------------------------------------------------------------- logo
def svgfill(color):
    """SVG fill attribute + style: CSS variables can't live in presentation attributes, so route them through color."""
    return ('fill="currentColor" style="color:%s"' % color) if str(color).startswith('var(') else f'fill="{color}"'

def _paths(d): return ''.join(f'<path d="{p}"/>' for p in d)

def wordmark(w, color, l=None, t=None, r=None, b=None, name='NEXA wordmark', tm=True):
    """Primary wordmark. Brandbook: never under 200 px wide on screen; clear space = height of the X on every side."""
    L = WM if tm else WMN
    h = round(w * L['h'] / L['w'], 1)
    svg = f'<svg data-name="Wordmark" width="{w}" height="{h}" viewBox="0 0 {L["w"]} {L["h"]}" {svgfill(color)}>{L["inner"]}</svg>'
    return box(name, l=l, t=t, r=r, b=b, w=w, h=h, cls='logo', inner=svg)

def wordmark_tagline(w, color, l=None, t=None, r=None, b=None, name='NEXA wordmark + tagline'):
    """Official wordmark + NEXT GENERATION ENTERPRISE lockup (NEXA_LogoSystem)."""
    h = round(w * WMT['h'] / WMT['w'], 1)
    svg = f'<svg data-name="Wordmark + tagline" width="{w}" height="{h}" viewBox="0 0 {WMT["w"]} {WMT["h"]}" {svgfill(color)}>{WMT["inner"]}</svg>'
    return box(name, l=l, t=t, r=r, b=b, w=w, h=h, cls='logo', inner=svg)

def emblem(w, color, l=None, t=None, r=None, b=None, name='NEXA emblem', color2=None):
    """The X emblem: two chevrons meeting. color2 colours the left chevron (e.g. the two-tone construction view)."""
    h = round(w * EM['h'] / EM['w'], 1)
    inner = EM['right'] + (f'<g {svgfill(color2)}>{EM["left"]}</g>' if color2 else EM['left'])
    svg = f'<svg data-name="Emblem" width="{w}" height="{h}" viewBox="0 0 {EM["w"]} {EM["h"]}" {svgfill(color)}>{inner}</svg>'
    return box(name, l=l, t=t, r=r, b=b, w=w, h=h, cls='logo', inner=svg)

def chevron(h, color, side, l=None, t=None, r=None, b=None, name=None):
    """One half of the emblem. side='open' is '>' (points right), side='close' is '<' (points left).
    Brandbook p.5: the brackets '><' hold images and focal points - the convergence of two worlds."""
    w = round(h * EM_HALF / EM['h'], 1)
    d, vx = (EM['left'], 0) if side == 'open' else (EM['right'], EM_HALF)
    vw = EM['w'] - EM_HALF if side != 'open' else EM_HALF
    svg = f'<svg data-name="Chevron" width="{w}" height="{h}" viewBox="{vx} 0 {vw} {EM["h"]}" {svgfill(color)}>{d}</svg>'
    return box(name or ('Bracket >' if side == 'open' else 'Bracket <'), l=l, t=t, r=r, b=b, w=w, h=h, cls='graphic', inner=svg)

_clip_n = [0]
def xwindow(name, key, l, t, w, align='xMidYMid', zoom=1.0):
    """Photo seen through the X emblem (brandbook p.36 social example). Vector clip, photo stays replaceable."""
    _clip_n[0] += 1; cid = f'xw{_clip_n[0]}'
    h = round(w * EM['h'] / EM['w'], 1)
    iw, ih = EM['w'] * zoom, EM['h'] * zoom
    ix, iy = (EM['w'] - iw) / 2, (EM['h'] - ih) / 2
    svg = (f'<svg data-name="X window" width="{w}" height="{h}" viewBox="0 0 {EM["w"]} {EM["h"]}">'
           f'<defs><clipPath id="{cid}">{EM_CLIP}</clipPath></defs>'
           f'<g clip-path="url(#{cid})"><image data-img="{key}" x="{ix:.1f}" y="{iy:.1f}" width="{iw:.1f}" height="{ih:.1f}" preserveAspectRatio="{align} slice"/></g></svg>')
    return box(name, l=l, t=t, w=w, h=h, cls='graphic xwin', inner=svg)

def lockup(industry, size, color, accent=ACC, l=None, t=None, r=None, b=None, name=None, gap=None):
    """'INDUSTRY  X  MOBILITY' (brandbook in-situ pages): Roboto uppercase either side of the emblem."""
    g = gap if gap is not None else round(size * 0.9)
    ew = round(size * 1.6)
    inner = (text('Industry', industry.upper(), 'lock', color, size)
             + f'<div class="logo" data-name="Emblem" style="width:{ew}px;height:{round(ew * EM["h"] / EM["w"], 1)}px;flex:none">'
             + f'<svg width="{ew}" height="{round(ew * EM["h"] / EM["w"], 1)}" viewBox="0 0 {EM["w"]} {EM["h"]}" {svgfill(accent)}>{EM["inner"]}</svg></div>'
             + text('Mobility', 'MOBILITY', 'lock', color, size))
    return box(name or f'{industry} x Mobility lockup', l=l, t=t, r=r, b=b, cls='row', style={'gap': px(g), 'align-items': 'center'}, inner=inner)

def rail(w, color, items, l, t, size=13, name='Meta rail'):
    """Three-point meta rail from the brandbook page furniture: NEXA · Version 1.0 · 2024."""
    a, bb, c = items
    inner = (text('Left', a, 'rail', color, size) + text('Centre', bb, 'rail', color, size, {'position': 'absolute', 'left': '50%', 'transform': 'translateX(-50%)'})
             + text('Right', c, 'rail', color, size, {'margin-left': 'auto'}))
    return box(name, l=l, t=t, w=w, cls='row', style={'position': 'absolute'}, inner=inner)

def arrow(size, color, name='Arrow'):
    """The E's forward arrow, used as a bullet / CTA marker."""
    return (f'<div class="graphic" data-name="{name}" style="width:{size}px;height:{size}px;flex:none">'
            f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" {svgfill(color)}><path d="M4 3h9l7 9-7 9H4l7-9z"/></svg></div>')

def artboard(aid, name, w, h, bg, inner, use, fmt, em=None):
    style = f'width:{w}px;height:{h}px;background:{bg}' + (f';--em:{em}' if em else '')
    return (f'<figure class="frame" id="{aid}" data-fmt="{fmt}">'
            f'<figcaption class="frame-meta"><b>{esc(name)}</b><span>{w} × {h} px · {esc(use)}</span></figcaption>'
            f'<div class="ab-wrap" style="width:{w}px;height:{h}px"><div class="ab" data-name="{esc(name)} · {w}×{h}" style="{style}">'
            f'{inner}</div></div></figure>')


# ---------------------------------------------------------------- container system (NEXA Figma "visual identity")
def _pts(pts): return ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)

def _inset(P, d):
    """Inset a convex clockwise polygon (screen coords) by d on every edge."""
    n = len(P); L = []
    for i in range(n):
        (x1, y1), (x2, y2) = P[i], P[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1; ln = (dx * dx + dy * dy) ** .5
        nx, ny = -dy / ln, dx / ln                     # inward normal for clockwise order in y-down space
        L.append(((x1 + nx * d, y1 + ny * d), (dx, dy)))
    out = []
    for i in range(n):
        (p, r), (q, s_) = L[i - 1], L[i]
        den = r[0] * s_[1] - r[1] * s_[0]
        t = ((q[0] - p[0]) * s_[1] - (q[1] - p[1]) * s_[0]) / den
        out.append((p[0] + r[0] * t, p[1] + r[1] * t))
    return out

CUT_RATIO = 1.19   # cut is steeper than 45 degrees: vertical run = 1.19 x horizontal run (NEXA Figma, ~ the emblem's stroke angle)

def chamfer(name, l, t, w, h, c=None, fill=None, stroke=None, sw=3, photo_key=None, align='xMidYMid', live=None, inner='', **_):
    """NEXA container (Figma "Visual identity"): a rectangle with the top-left and bottom-right corners cut.
    c = horizontal run of the cut; the vertical run is c * CUT_RATIO. No extra shapes: the grey flaps in the Figma
    were construction guides only. Optional photo clipped to the shape; live = (inset, colour) draws the live area,
    equally inset from every edge including the cuts."""
    _clip_n[0] += 1; cid = f'ch{_clip_n[0]}'
    c = c if c is not None else round(min(w, h) * .16)
    cy = c * CUT_RATIO
    P = [(c, 0), (w, 0), (w, h - cy), (w - c, h), (0, h), (0, cy)]
    parts = []
    if fill: parts.append(f'<polygon data-name="Fill" points="{_pts(P)}" {svgfill(fill)}/>')
    if photo_key:
        parts.append(f'<defs><clipPath id="{cid}"><polygon points="{_pts(P)}"/></clipPath></defs>'
                     f'<g clip-path="url(#{cid})"><image data-img="{photo_key}" x="0" y="0" width="{w}" height="{h}" preserveAspectRatio="{align} slice"/></g>')
    if live:
        d, col = live
        parts.append(f'<polygon data-name="Live area" points="{_pts(_inset(P, d))}" {svgfill(col)}/>')
    if stroke: parts.append(f'<polygon data-name="Outline" points="{_pts(P)}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="miter"/>')
    svg = f'<svg data-name="Container" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{"".join(parts)}</svg>'
    return box(name, l=l, t=t, w=w, h=h, cls='graphic' + (' xwin' if photo_key else ''), inner=svg + inner)

def watermark(w, l=None, t=None, r=None, b=None, color=TINT, name='X watermark'):
    """Oversized pale emblem behind content (NEXA Figma). Crop it off the edge; never behind small text."""
    return emblem(w, color, l=l, t=t, r=r, b=b, name=name)


# ---------------------------------------------------------------- details seen in NEXA collateral
def chev(size, color, name='Bullet'):
    """Thin outline chevron '>' used as the bullet in NEXA one-pagers."""
    return (f'<div class="graphic" data-name="{name}" style="width:{size}px;height:{size}px;flex:none">'
            f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" style="color:{color}" stroke-width="2.2" stroke-linecap="square"><path d="M8 3l9 9-9 9"/></svg></div>')

def chev_list(items, color, size, l, t, w, gap=None, ccolor=None, cls='sh2'):
    gap = gap if gap is not None else round(size * .55)
    rows = ''.join(f'<div class="row" data-name="Item" style="gap:{round(size*.6)}px;align-items:flex-start">'
                   f'<div style="padding-top:{round(size*.12)}px">{chev(round(size*.9), ccolor or color)}</div>{text("Item", it, cls, color, size)}</div>' for it in items)
    return box('List', l=l, t=t, w=w, cls='stack', style={'gap': px(gap)}, inner=rows)

ICONS = {  # 24px line icons in the one-pager style (1.6 stroke)
    'device': '<rect x="7" y="2.5" width="10" height="19" rx="1.5"/><circle cx="12" cy="6" r=".6"/>',
    'box': '<path d="M12 2.8l8 4.4v9.6l-8 4.4-8-4.4V7.2z"/><path d="M4 7.2l8 4.4 8-4.4M12 11.6v9.6"/>',
    'signal': '<path d="M4 20h16M6 20v-3M10 20v-7M14 20v-11M18 20V4"/><path d="M4 20L18 4"/>',
    'shield': '<path d="M12 2.8l7.5 3v6.2c0 4.6-3.2 8-7.5 9.2-4.3-1.2-7.5-4.6-7.5-9.2V5.8z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    'cycle': '<path d="M19.5 12a7.5 7.5 0 01-13.3 4.8M4.5 12a7.5 7.5 0 0113.3-4.8"/><path d="M18 3.5v3.8h-3.8M6 20.5v-3.8h3.8"/>',
    'heart': '<path d="M12 20s-7.5-4.6-7.5-10.2A4.3 4.3 0 0112 7.3a4.3 4.3 0 017.5 2.5C19.5 15.4 12 20 12 20z"/><path d="M6 12h3l1.5-2.5 2 5 1.5-2.5h4"/>',
    'truck': '<path d="M2.5 6.5h11v9h-11zM13.5 9.5h4l3 3v3h-7z"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    'cart': '<path d="M3 4h2.5l2.2 11h10.6l2-8H7"/><circle cx="9" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/>',
}
def icon(key, size, color, name=None, l=None, t=None, r=None, b=None):
    pos = ''.join(f'{k}:{px(v)};' for k, v in (('left', l), ('top', t), ('right', r), ('bottom', b)) if v is not None)
    return (f'<div class="graphic{" abs" if pos else ""}" data-name="{esc(name or key)} icon" style="{pos}width:{size}px;height:{size}px;flex:none">'
            f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" style="color:{color}" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round">{ICONS[key]}</svg></div>')

def stat(num, suffix, color, size, l=None, t=None, name='Stat'):
    """Big number in Roboto Black with a small suffix (NEXA case study style: 50%, 2K, 50+)."""
    inner = text('Number', num, 'stat', color, size) + (text('Suffix', suffix, 'stat', color, round(size * .34), {'margin-bottom': px(round(size * .12))}) if suffix else '')
    return box(name, l=l, t=t, cls='row', style={'align-items': 'flex-end', 'gap': '2px'}, inner=inner)

def partner_slot(w, h, color, l=None, t=None, r=None, b=None, name='Partner logo'):
    """Placeholder for a partner / customer logo (replace in Figma)."""
    return box(name, l=l, t=t, r=r, b=b, w=w, h=h, cls='row', style={'border': f'1.5px dashed {color}', 'align-items': 'center', 'justify-content': 'center'},
               inner=text('Placeholder', 'PARTNER LOGO', 'lbl', color, round(h * .22)))

def qr_dots(data, size, color, l=None, t=None, r=None, b=None, name='QR code'):
    """QR code drawn as dots with round finder eyes (NEXA business card)."""
    import qrcode
    q = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(data); q.make()
    M = q.get_matrix(); n = len(M); parts = []
    eyes = [(0, 0), (n - 7, 0), (0, n - 7)]
    in_eye = lambda x, y: any(ex <= x < ex + 7 and ey <= y < ey + 7 for ex, ey in eyes)
    for y in range(n):
        for x in range(n):
            if M[y][x] and not in_eye(x, y): parts.append(f'<circle cx="{x + .5}" cy="{y + .5}" r=".42"/>')
    for ex, ey in eyes:
        parts.append(f'<circle cx="{ex + 3.5}" cy="{ey + 3.5}" r="3" fill="none" stroke="currentColor" stroke-width="1"/><circle cx="{ex + 3.5}" cy="{ey + 3.5}" r="1.5"/>')
    svg = f'<svg data-name="QR" width="{size}" height="{size}" viewBox="0 0 {n} {n}" fill="currentColor" style="color:{color}">{"".join(parts)}</svg>'
    return box(name, l=l, t=t, r=r, b=b, w=size, h=size, cls='graphic', inner=svg)

def slash(name, l, t, w, h, stroke=WHITE, sw=2, fill_key=None, skew=None):
    """The slanted band (NEXA CTA section / case-study card): a parallelogram of light, or just its outline."""
    _clip_n[0] += 1; cid = f'sl{_clip_n[0]}'
    k = skew if skew is not None else h * .78
    P = f'{k:.1f},0 {w:.1f},0 {w - k:.1f},{h:.1f} 0,{h:.1f}'
    body = ''
    if fill_key:
        body = (f'<defs><clipPath id="{cid}"><polygon points="{P}"/></clipPath></defs>'
                f'<g clip-path="url(#{cid})"><image data-img="{fill_key}" x="0" y="0" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice"/></g>')
    if stroke: body += f'<polygon points="{P}" fill="none" stroke="{stroke}" stroke-width="{sw}"/>'
    return box(name, l=l, t=t, w=w, h=h, cls='graphic' + (' xwin' if fill_key else ''), inner=f'<svg data-name="Slash" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>')

ICONS.update({
    'chip': '<rect x="6.5" y="6.5" width="11" height="11" rx="1"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 3.5v3M12 3.5v3M15 3.5v3M9 17.5v3M12 17.5v3M15 17.5v3M3.5 9h3M3.5 12h3M3.5 15h3M17.5 9h3M17.5 12h3M17.5 15h3"/>',
    'factory': '<path d="M3 20.5V9l5 3.2V9l5 3.2V9l5 3.2V4.5h3v16z"/><path d="M7 16.5h2M12 16.5h2M17 16.5h1"/>',
    'rocket': '<path d="M14.5 4.5c2.8-1.1 4.9-1 5-1 0 .1.1 2.2-1 5l-6.3 6.3-4-4z"/><path d="M8.2 10.8L5 10.5l-1.5 2.4 3.6 1M13.2 15.8l.3 3.2-2.4 1.5-1-3.6M6 18l-2 2.5M8 19.5l-1 1.5M4.5 16l-1.5 1"/><circle cx="15.8" cy="8.2" r="1.3"/>',
    'globe': '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.4 2.4 3.6 5.2 3.6 8.5s-1.2 6.1-3.6 8.5c-2.4-2.4-3.6-5.2-3.6-8.5S9.6 5.9 12 3.5z"/>',
    'lock': '<rect x="5" y="10.5" width="14" height="10" rx="1.5"/><path d="M8 10.5V7.5a4 4 0 018 0v3M12 14.5v2.5"/>',
    'users': '<circle cx="9" cy="8.5" r="3.2"/><path d="M3 19.5c.6-3.3 3-5.2 6-5.2s5.4 1.9 6 5.2"/><circle cx="17" cy="9.5" r="2.4"/><path d="M16.5 14.4c2.3.2 4 1.8 4.5 4.6"/>',
    'check': '<circle cx="12" cy="12" r="8.5"/><path d="M8 12.3l2.7 2.7L16.2 9.5"/>',
    'pin': '<path d="M12 21s-6.5-6.1-6.5-11a6.5 6.5 0 0113 0c0 4.9-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    'mail': '<rect x="3" y="5.5" width="18" height="13" rx="1.5"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/>',
    'phone': '<path d="M6.5 3.5h3l1.5 4.5-2 1.5a11 11 0 005.5 5.5l1.5-2 4.5 1.5v3a2 2 0 01-2 2A16 16 0 014.5 5.5a2 2 0 012-2z"/>',
})

def vwordmark(length, color, l=None, t=None, r=None, b=None, name='NEXA wordmark (vertical)'):
    """Wordmark rotated to read bottom-to-top, as on the right-hand rail of NEXA's decks."""
    th = round(length * WM['h'] / WM['w'], 1)
    svg = (f'<svg data-name="Wordmark" width="{th}" height="{length}" viewBox="0 0 {WM["h"]} {WM["w"]}" {svgfill(color)}>'
           f'<g transform="translate(0 {WM["w"]}) rotate(-90)">{WM["inner"]}</g></svg>')
    return box(name, l=l, t=t, r=r, b=b, w=th, h=length, cls='logo', inner=svg)

def glass(name, l, t, w, h, c=None, inner='', solid=None, alpha=.07, line_a=.26):
    """Frosted cut-corner card for dark grounds (NEXA strategy decks). solid = fill colour for the highlighted card."""
    return chamfer(name, l, t, w, h, c=c if c is not None else round(min(w, h) * .09),
                   fill=solid or f'rgba(255,255,255,{alpha})', stroke=None if solid else f'rgba(255,255,255,{line_a})', sw=1.5, inner=inner)

CONFIDENTIAL = ('Confidential. Proprietary information that may not be used or disclosed outside of NEXA and its affiliates '
                'except pursuant to a written agreement. Copyright © NEXA. All rights reserved.')
