# NEXA brand asset library generator helpers -> one self-contained HTML file.
# Every template is plain positioned HTML so it can be edited in the browser, copied to Figma as SVG,
# or imported with an HTML-to-Figma plugin. Layer names come from data-name.
import json, html as H
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]          # repo root

# ---------------------------------------------------------------- brand palette (brandbook p.14)
BLUE, GRAY, TURQ, PINK, PURPLE, BLACK = '#1F1FCC', '#C9C7C9', '#36FFE8', '#FF5FEB', '#2D0685', '#000000'
WHITE = '#FFFFFF'
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
WM, EM = LOGO['wordmark'], LOGO['emblem']
EM_HALF = EM['w'] / 2

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
def _paths(d): return ''.join(f'<path d="{p}"/>' for p in d)

def wordmark(w, color, l=None, t=None, r=None, b=None, name='NEXA wordmark', tm=True):
    """Primary wordmark. Brandbook: never under 200 px wide on screen; clear space = height of the X on every side."""
    h = round(w * WM['h'] / WM['w'], 1)
    svg = f'<svg data-name="Wordmark" width="{w}" height="{h}" viewBox="0 0 {WM["w"]} {WM["h"]}" fill="{color}">{_paths(WM["d"] if tm else WM["d"][:3])}</svg>'
    return box(name, l=l, t=t, r=r, b=b, w=w, h=h, cls='logo', inner=svg)

def wordmark_tagline(w, color, l=None, t=None, r=None, b=None, name='NEXA wordmark + tagline'):
    """Wordmark with 'Next Generation Enterprise' tagline (brandbook p.7), tagline set in Roboto Medium, centred."""
    h = round(w * WM['h'] / WM['w'], 1); ts = round(w * 0.074, 1)
    inner = (f'<svg data-name="Wordmark" width="{w}" height="{h}" viewBox="0 0 {WM["w"]} {WM["h"]}" fill="{color}">{_paths(WM["d"])}</svg>'
             + text('Tagline', 'NEXT GENERATION ENTERPRISE', 'tagline', color, ts, {'margin-top': px(round(h * 0.28)), 'width': px(round(w * 0.95)), 'text-align': 'center'}))
    return box(name, l=l, t=t, r=r, b=b, w=w, cls='logo stack', style={'align-items': 'flex-start'}, inner=inner)

def emblem(w, color, l=None, t=None, r=None, b=None, name='NEXA emblem', color2=None):
    """The X emblem: two chevrons meeting. color2 colours the left chevron (e.g. the two-tone construction view)."""
    h = round(w * EM['h'] / EM['w'], 1)
    d0, d1 = EM['d'][0], EM['d'][1]
    inner = f'<path d="{d0}"/>' + (f'<path d="{d1}" fill="{color2}"/>' if color2 else f'<path d="{d1}"/>')
    svg = f'<svg data-name="Emblem" width="{w}" height="{h}" viewBox="0 0 {EM["w"]} {EM["h"]}" fill="{color}">{inner}</svg>'
    return box(name, l=l, t=t, r=r, b=b, w=w, h=h, cls='logo', inner=svg)

def chevron(h, color, side, l=None, t=None, r=None, b=None, name=None):
    """One half of the emblem. side='open' is '>' (points right), side='close' is '<' (points left).
    Brandbook p.5: the brackets '><' hold images and focal points - the convergence of two worlds."""
    w = round(h * EM_HALF / EM['h'], 1)
    d, vx = (EM['d'][1], 0) if side == 'open' else (EM['d'][0], EM_HALF)
    svg = f'<svg data-name="Chevron" width="{w}" height="{h}" viewBox="{vx} 0 {EM_HALF} {EM["h"]}" fill="{color}"><path d="{d}"/></svg>'
    return box(name or ('Bracket >' if side == 'open' else 'Bracket <'), l=l, t=t, r=r, b=b, w=w, h=h, cls='graphic', inner=svg)

_clip_n = [0]
def xwindow(name, key, l, t, w, align='xMidYMid', zoom=1.0):
    """Photo seen through the X emblem (brandbook p.36 social example). Vector clip, photo stays replaceable."""
    _clip_n[0] += 1; cid = f'xw{_clip_n[0]}'
    h = round(w * EM['h'] / EM['w'], 1)
    iw, ih = EM['w'] * zoom, EM['h'] * zoom
    ix, iy = (EM['w'] - iw) / 2, (EM['h'] - ih) / 2
    svg = (f'<svg data-name="X window" width="{w}" height="{h}" viewBox="0 0 {EM["w"]} {EM["h"]}">'
           f'<defs><clipPath id="{cid}">{_paths(EM["d"])}</clipPath></defs>'
           f'<g clip-path="url(#{cid})"><image data-img="{key}" x="{ix:.1f}" y="{iy:.1f}" width="{iw:.1f}" height="{ih:.1f}" preserveAspectRatio="{align} slice"/></g></svg>')
    return box(name, l=l, t=t, w=w, h=h, cls='graphic xwin', inner=svg)

def lockup(industry, size, color, accent=TURQ, l=None, t=None, r=None, b=None, name=None, gap=None):
    """'INDUSTRY  X  MOBILITY' (brandbook in-situ pages): Roboto uppercase either side of the emblem."""
    g = gap if gap is not None else round(size * 0.9)
    ew = round(size * 1.6)
    inner = (text('Industry', industry.upper(), 'lock', color, size)
             + f'<div class="logo" data-name="Emblem" style="width:{ew}px;height:{round(ew * EM["h"] / EM["w"], 1)}px;flex:none">'
             + f'<svg width="{ew}" height="{round(ew * EM["h"] / EM["w"], 1)}" viewBox="0 0 {EM["w"]} {EM["h"]}" fill="{accent}">{_paths(EM["d"])}</svg></div>'
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
            f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{color}"><path d="M4 3h9l7 9-7 9H4l7-9z"/></svg></div>')

def artboard(aid, name, w, h, bg, inner, use, fmt, em=None):
    style = f'width:{w}px;height:{h}px;background:{bg}' + (f';--em:{em}' if em else '')
    return (f'<figure class="frame" id="{aid}" data-fmt="{fmt}">'
            f'<figcaption class="frame-meta"><b>{esc(name)}</b><span>{w} × {h} px · {esc(use)}</span></figcaption>'
            f'<div class="ab-wrap" style="width:{w}px;height:{h}px"><div class="ab" data-name="{esc(name)} · {w}×{h}" style="{style}">'
            f'{inner}</div></div></figure>')
