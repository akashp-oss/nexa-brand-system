from gen import *

# ============================================================================
# NEXA SYSTEM RULES (from NEXA Brand Guidelines v1.0, 2024)
#   colour   Super Blue leads, Base Gray supports, tertiaries sparingly; only brandbook p.15 pairings
#   type     Headline N27 Regular UPPERCASE (Saira stand-in) · Sub-header 1 Roboto Regular UPPERCASE
#            Sub-header 2 Roboto Regular Title Case · Sub-header 3 Roboto Bold Title Case · body Roboto
#            1.5x (perfect fifth) steps between levels
#   logo     wordmark >= 200 px, emblem >= 50 px, clear space = X height; emblem top-right,
#            wordmark bottom-left on the margin (brandbook p.15 layout)
#   devices  '><' brackets hold images · X window · INDUSTRY X MOBILITY lockup · split convergence
#            · meta rail (NEXA · topic · year) · forward arrow
#   imagery  Super Blue grade for photography; generated brand-light for texture
# ============================================================================

F = []
YEAR = '2026'
LOREM = 'NEXA brings devices, software and services together so enterprises can deploy, manage and support mobility at scale.'

def scrim(l, t, w, h, a=.38):
    """Space Black veil so white type holds on bright photos (photo stays graded underneath)."""
    return fill('Scrim', f'rgba(0,0,0,{a})', l=l, t=t, w=w, h=h)

def hl(name, content, color, size, l=None, t=None, w=None, r=None, b=None, extra=None):
    return T(name, content, 'hl', color, size, l, t, w, r, b, extra)

# ---------------------------------------------------------------- 00 BRAND FOUNDATIONS (1920 x 1080 boards)
BW, BH, BM = 1920, 1080, 64

def board_intro(num, label, title, body, color=BLACK, accent=BLUE, rail_color=None):
    return (rail(BW - 2 * BM, rail_color or color, ['NEXA', 'Brand asset library · Version 1.0', YEAR], BM, 36, 14)
            + stack('Intro', [text('Section label', f'{num}  ·  {label}', 'label', accent, 16),
                              text('Headline', title, 'hl', color, 84),
                              text('Body', body, 'body', color, 18, {'max-width': '470px', 'margin-top': '12px'})],
                    l=BM, t=132, w=520, gap=22))

f1 = (photo('Brand light', 'tex-streaks', 0, 0, BW, BH)
      + rail(BW - 2 * BM, WHITE, ['NEXA', 'Brand asset library · Version 1.0', YEAR], BM, BH - 60, 14)
      + hl('Kicker', 'WHAT’S NEXT', TURQ, 40, l=BM, t=64)
      + wordmark(1560, GRAY, l=(BW - 1560) // 2 - 20, t=(BH - round(1560 * WM['h'] / WM['w'])) // 2))
F.append(('found', artboard('fd-cover', 'Foundations · Cover', BW, BH, BLACK, f1, 'Brand board, deck cover', 'board')))

# logo system
wm_w = 600; wm_h = round(wm_w * WM['h'] / WM['w'], 1); xs = wm_h            # clear space = X height
cs_w, cs_h = wm_w + 2 * xs, wm_h + 2 * xs
pan_l, pan_t, pan_w, pan_h = 720, 120, 1136, 470
cs_l, cs_t = (pan_w - cs_w) / 2, (pan_h - cs_h) / 2
f2 = (board_intro('01', 'Logo system', 'SYMBOL OF\nPROGRESS',
                  'The arrow in the E points forward. The X is two brackets, ><, meeting: two worlds brought together. '
                  'Use the artwork as supplied and scale it only in proportion.')
      + box('Clear space panel', l=pan_l, t=pan_t, w=pan_w, h=pan_h, cls='group', inner=
            fill('Panel', BLACK, l=0, t=0, w=pan_w, h=pan_h)
            + box('Clear space', l=cs_l, t=cs_t, w=cs_w, h=cs_h, cls='guide-line', style={'border': f'1.5px dashed {TURQ}'})
            + ''.join(fill('X unit', '#1B1B1B', l=cs_l + dx, t=cs_t + dy, w=xs, h=xs, style={'outline': '1px solid #3A3A3A'})
                      for dx, dy in [(0, 0), (cs_w - xs, 0), (0, cs_h - xs), (cs_w - xs, cs_h - xs)])
            + wordmark(wm_w, WHITE, l=cs_l + xs, t=cs_t + xs)
            + T('Caption', 'Clear space = height of the X on every side', 'small', GRAY, 14, l=24, b=20))
      + ''.join(box(f'Tile {i+1}', l=720 + i * 385, t=620, w=366, h=360, cls='group', inner=inner)
                + T('Tile caption', cap, 'small', BLACK, 14, l=720 + i * 385, t=994, w=366)
                for i, (inner, cap) in enumerate([
                    (fill('Tile fill', BLUE, l=0, t=0, w=366, h=360) + wordmark_tagline(250, GRAY, l=58, t=146),
                     'Wordmark + tagline “Next Generation Enterprise”'),
                    (fill('Tile fill', BLACK, l=0, t=0, w=366, h=360) + emblem(150, TURQ, l=108, t=128, color2='#1FA89A'),
                     'Emblem: the X. Use for avatars and small spaces'),
                    (fill('Tile fill', WHITE, l=0, t=0, w=366, h=360, style={'outline': '1px solid #D8D8D8', 'outline-offset': '-1px'})
                     + wordmark(200, BLACK, l=40, t=100) + T('Min', '200 px', 'small', BLACK, 13, l=40, t=150)
                     + emblem(50, BLACK, l=40, t=220) + T('Min', '50 px', 'small', BLACK, 13, l=40, t=262)
                     + T('Note', 'Minimum\nsizes', 'sh3', BLACK, 18, r=36, t=100, extra={'text-align': 'right'}),
                     'Never smaller: wordmark 200 px (2.5 in), emblem 50 px (0.5 in)')])))
F.append(('found', artboard('fd-logo', 'Foundations · Logo system', BW, BH, WHITE, f2, 'Brand board', 'board')))

# colour
bars_l = 600
def swatch_text(name, hx, rgb, cmyk, pan, c, small=False):
    s = 13 if small else 15
    return stack('Specs', [text('Name', name.upper().replace(' ', '\n'), 'hl', c, 26 if small else 40),
                           text('HEX', hx, 'sh3', c, 17 if small else 22, {'margin-top': '18px'}),
                           text('Pantone', f'PANTONE {pan}', 'small', c, s), text('RGB', f'RGB {rgb}', 'small', c, s), text('CMYK', f'CMYK {cmyk}', 'small', c, s)],
                 l=28, t=36, gap=6)
tc = {BLUE: WHITE, GRAY: BLACK, TURQ: PURPLE, PINK: BLACK, PURPLE: WHITE, BLACK: WHITE}
cols = [(bars_l, 0, 520, BH), (bars_l + 520, 0, 340, BH), (bars_l + 860, 0, 230, BH / 2), (bars_l + 1090, 0, 230, BH / 2), (bars_l + 860, BH / 2, 230, BH / 2), (bars_l + 1090, BH / 2, 230, BH / 2)]
f3 = (board_intro('02', 'Colour', 'SUPER BLUE\nLEADS',
                  'Super Blue is the primary colour: trust, reliability, technology. Base Gray is the calm backdrop. '
                  'Turquoise, Pink, Dark Purple and Space Black are accents. Bar widths show the balance to aim for.')
      + ''.join(box(f'{n} swatch', l=x, t=y, w=w, h=h, cls='group', inner=fill('Fill', hx, l=0, t=0, w=w, h=h) + swatch_text(n, hx, rgb, cmyk, pan, tc[hx], small=w < 300))
                for (n, hx, rgb, cmyk, pan, role), (x, y, w, h) in zip(PALETTE, cols)))
F.append(('found', artboard('fd-colour', 'Foundations · Colour palette', BW, BH, WHITE, f3, 'Brand board', 'board')))

# pairings
def pair_tile(bg, fg, w, h):
    return (fill('Fill', bg, l=0, t=0, w=w, h=h) + emblem(round(w * .13), fg, r=round(w * .06), t=round(w * .06))
            + wordmark(round(w * .62), fg, l=round(w * .06), b=round(w * .06)))
f4 = (board_intro('02', 'Colour pairings', 'APPROVED\nPAIRS',
                  'Set the logo and headlines only in these combinations. Keep contrast high and never pair two tertiaries that fight: '
                  'turquoise with pink, or purple on blue.')
      + T('Row label', 'USE', 'label', BLUE, 15, l=680, t=112)
      + ''.join(box('Approved pair', l=680 + (i % 3) * 398, t=140 + (i // 3) * 262, w=380, h=244, cls='group', inner=pair_tile(bg, fg, 380, 244))
                for i, (bg, fg) in enumerate(PAIRS_OK))
      + T('Row label', 'AVOID', 'label', BLUE, 15, l=680, t=700)
      + ''.join(box('Pair to avoid', l=680 + i * 199, t=728, w=180, h=180, cls='group', inner=
                    fill('Fill', bg, l=0, t=0, w=180, h=180) + fill('Dot', fg, l=45, t=45, w=90, h=90, style={'border-radius': '50%'})
                    + T('Cross', '✕', 'sh3', '#FF2D2D', 22, l=12, t=8))
                for i, (bg, fg) in enumerate(PAIRS_NO))
      + T('Note', 'Pink + Turquoise · Purple on Blue · Purple on Black · Blue + Purple · Turquoise on Gray · Pink on Turquoise', 'small', BLACK, 14, l=680, t=926))
F.append(('found', artboard('fd-pairs', 'Foundations · Colour pairings', BW, BH, WHITE, f4, 'Brand board', 'board')))

# typography
rows = [('HEADER', 'hl', 120, 'N27 Regular (Saira) · 120 pt', 'Uppercase'),
        ('SUB-HEADER 1', 'sh1', 48, 'Roboto Regular · 48 pt', 'Uppercase'),
        ('Sub-Header 2', 'sh2', 36, 'Roboto Regular · 36 pt', 'Title Case'),
        ('Sub-Header 3', 'sh3', 24, 'Roboto Bold · 24 pt', 'Title Case')]
f5 = (board_intro('03', 'Typography', 'CLEAR,\nBOLD, NEXT',
                  'N27 for headlines, always uppercase and never bold. Roboto for sub-headers and body. '
                  'Each level steps by about 1.5× (a perfect fifth). If N27 is not installed, Saira stands in.')
      + fill('Panel', '#DCDBDC', l=680, t=0, w=1240, h=BH)
      + ''.join(line('Rule', '#9E9C9E', 680, y, 1240) for y in (300, 450, 580, 700, 830))
      + ''.join(T('Spec', spec, 'small', BLACK, 14, l=720, t=y - 36) + T('Case', case, 'small', BLACK, 14, l=1050, t=y - 36)
                + T('Sample', s, cls, BLACK, size, r=64, b=BH - y + 14, extra={'text-align': 'right'})
                for (s, cls, size, spec, case), y in zip(rows, (300, 450, 580, 700)))
      + T('Spec', 'Roboto Regular / Bold · 16 pt', 'small', BLACK, 14, l=720, t=804)
      + T('Body regular', 'Nam ullamcorper condimentum tortor, eget mattis enim. In libero augue, mollis id justo eu, congue convallis metus. Sed augue elit, porta vel velit vitae.', 'body', BLACK, 16, l=1080, t=860, w=360)
      + T('Body bold', 'Nam ullamcorper condimentum tortor, eget mattis enim. In libero augue, mollis id justo eu, congue convallis metus. Sed augue elit, porta vel velit vitae.', 'body', BLACK, 16, l=1476, t=860, w=380, extra={'font-weight': '700'}))
F.append(('found', artboard('fd-type', 'Foundations · Typography', BW, BH, WHITE, f5, 'Brand board', 'board')))

# graphic devices
gx, gw, gh = 640, 598, 400
def tile(i, name, inner, cap):
    l, t = gx + (i % 2) * (gw + 20), 120 + (i // 2) * 470
    return box(name, l=l, t=t, w=gw, h=gh, cls='group', inner=inner) + T('Caption', cap, 'small', GRAY, 14, l=l, t=t + gh + 14, w=gw)
f6 = (board_intro('04', 'Graphic devices', 'BRACKETS\nHOLD IDEAS',
                  'Everything comes from the logo. The X splits into two brackets that frame images, the emblem becomes a window, '
                  'and the X joins an industry to mobility.', WHITE, TURQ, GRAY)
      + tile(0, 'Brackets', fill('Fill', BLUE, l=0, t=0, w=gw, h=gh) + photo('Image', 'tex-tunnel', 70, 40, gw - 140, gh - 80)
             + chevron(110, TURQ, 'open', l=36, t=145) + chevron(110, TURQ, 'close', r=36, t=145),
             'Brackets  ><  frame an image or a focal point. Turquoise on Super Blue or black.')
      + tile(1, 'X window', fill('Fill', GRAY, l=0, t=0, w=gw, h=gh) + xwindow('X window', 'ph-clinician', 99, 32, 400, 'xMidYMid', 1.25),
             'X window: a photo seen through the emblem. Base Gray or Turquoise behind.')
      + tile(2, 'Industry x Mobility', photo('Photo', 'ph-dispatcher', 0, 0, gw / 2, gh, '40% 50%') + scrim(0, 0, gw / 2, gh) + photo('Brand light', 'tex-fiber', gw / 2, 0, gw / 2, gh, '70% 40%')
             + lockup('Public safety', 26, WHITE, l=86, t=178),
             'INDUSTRY  X  MOBILITY lockup across a split: two worlds converging.')
      + tile(3, 'Rail and arrow', fill('Fill', BLUE, l=0, t=0, w=gw, h=gh) + rail(gw - 64, TURQ, ['NEXA', 'Version 1.0', YEAR], 32, 28, 13)
             + stack('List', [f'<div class="row" data-name="Item" style="gap:16px;align-items:center">{arrow(22, TURQ)}{text("Item", t_, "sh2", WHITE, 28)}</div>'
                              for t_ in ['Deploy', 'Manage', 'Support']], l=32, t=120, gap=22)
             + T('Index', '003', 'num', WHITE, 110, r=32, b=16),
             'Meta rail, forward-arrow bullets and index numbers give pages rhythm.'))
F.append(('found', artboard('fd-devices', 'Foundations · Graphic devices', BW, BH, BLACK, f6, 'Brand board', 'board')))

# imagery
f7 = (board_intro('05', 'Imagery', 'SUPER BLUE\nGRADE',
                  'Photography is graded into Super Blue so every industry reads as one brand. Brand light (generated fibre, '
                  'ribbons, light trails) adds energy behind type. People and devices at work, never staged stock smiles.')
      + T('Row label', 'PHOTOGRAPHY · SUPER BLUE GRADE', 'label', BLUE, 15, l=640, t=112)
      + ''.join(photo(n, k, 640 + i * 412, 142, 392, 380, p) for i, (n, k, p) in enumerate([('Health', 'ph-clinician', '40% 40%'), ('Public safety', 'ph-command', '60% 50%'), ('Retail and venues', 'ph-crowd', '50% 50%')]))
      + T('Row label', 'BRAND LIGHT · TEXTURES', 'label', BLUE, 15, l=640, t=566)
      + ''.join(photo(n, k, 640 + i * 412, 596, 392, 380, p) for i, (n, k, p) in enumerate([('Fibre', 'tex-fiber', '70% 40%'), ('Ribbon', 'tex-ribbon', '75% 50%'), ('Light trails', 'tex-streaks', '50% 50%')]))
      + T('Note', 'Photos: placeholders graded with brand/imagery/grade.py. Replace with licensed NEXA photography.', 'small', BLACK, 13, l=640, t=1000))
F.append(('found', artboard('fd-imagery', 'Foundations · Imagery', BW, BH, WHITE, f7, 'Brand board', 'board')))

# ---------------------------------------------------------------- 01 SOCIAL POSTS 1080 x 1080
S, M = 1080, 72
p1 = (fill('Frame', TURQ, l=0, t=0, w=S, h=S) + fill('Field', GRAY, l=20, t=20, w=S - 40, h=S - 40)
      + rail(S - 2 * M, BLUE, ['NEXA', 'Healthcare', YEAR], M, 52, 15)
      + xwindow('X window', 'ph-clinician', 150, 118, 780, 'xMidYMid', 1.18)
      + hl('Headline', 'CARE THAT\nMOVES WITH YOU', BLUE, 76, l=M, t=774, w=780)
      + wordmark(220, BLUE, r=M, b=M))
F.append(('social', artboard('ig-xwindow', 'Post · X window', S, S, GRAY, p1, 'Instagram / LinkedIn square', 'post')))

p2 = (rail(S - 2 * M, TURQ, ['NEXA', 'Enterprise mobility', 'A.1'], M, 44, 15)
      + photo('Image', 'tex-tunnel', M, 100, S - 2 * M, 740)
      + chevron(150, TURQ, 'open', l=M - 54, t=395) + chevron(150, TURQ, 'close', r=M - 54, t=395)
      + T('Index', '00', 'num', WHITE, 44, r=M + 24, t=780)
      + hl('Headline', 'CONNECT WHAT’S NEXT', WHITE, 60, l=M, t=880, w=720)
      + wordmark(200, GRAY, r=M, b=M))
F.append(('social', artboard('ig-brackets', 'Post · Brackets', S, S, BLUE, p2, 'Instagram / LinkedIn square', 'post')))

p3 = (photo('Industry photo', 'ph-paramedics', 0, 0, S / 2, S, '38% 50%') + photo('Brand light', 'tex-fiber', S / 2, 0, S / 2, S, '72% 40%')
      + wordmark(700, WHITE, l=190, t=430)
      + lockup('Health', 30, WHITE, l=300, t=920))
F.append(('social', artboard('ig-split', 'Post · Industry × Mobility', S, S, BLACK, p3, 'Instagram / LinkedIn square', 'post')))

p4 = (emblem(96, PURPLE, r=M, t=M)
      + hl('Headline', 'BUILT FOR\nWHAT’S\nNEXT', PURPLE, 150, l=M, t=250)
      + T('Sub-header', 'Devices, software and services for the next generation enterprise.', 'sh2', PURPLE, 32, l=M, t=760, w=780)
      + wordmark(300, PURPLE, l=M, b=M))
F.append(('social', artboard('ig-statement', 'Post · Statement', S, S, TURQ, p4, 'Instagram / LinkedIn square', 'post')))

p5 = (rail(S - 2 * M, GRAY, ['NEXA', 'By the numbers', YEAR], M, 52, 15)
      + T('Stat', '360°', 'num', WHITE, 300, l=M - 10, t=190)
      + T('Sub-header 1', 'DEVICE LIFECYCLE,\nONE PARTNER', 'sh1', TURQ, 48, l=M, t=560)
      + T('Body', 'Procure, deploy, manage, repair and recycle. One partner from first order to end of life.', 'body', GRAY, 26, l=M, t=700, w=760)
      + wordmark(240, BLUE, l=M, b=M) + emblem(64, TURQ, r=M, b=M))
F.append(('social', artboard('ig-stat', 'Post · Big number', S, S, BLACK, p5, 'Instagram / LinkedIn square', 'post')))

p6 = (photo('Brand light', 'tex-wave', 0, 0, S, 560, '50% 55%')
      + rail(S - 2 * M, WHITE, ['NEXA', 'Live webinar', YEAR], M, 52, 15)
      + T('Label', 'WEBINAR', 'label', TURQ, 22, l=M, t=620)
      + hl('Headline', 'MOBILITY AT\nTHE EDGE', WHITE, 96, l=M, t=660)
      + T('Date', 'Thursday 15 October · 11:00 ET', 'sh3', TURQ, 28, l=M, t=880)
      + wordmark(220, TURQ, r=M, b=M))
F.append(('social', artboard('ig-event', 'Post · Event', S, S, PURPLE, p6, 'Instagram / LinkedIn square', 'post')))

# ---------------------------------------------------------------- 02 STORIES 1080 x 1920
SW, SH = 1080, 1920
s1 = (photo('Industry photo', 'ph-command', 0, 0, SW, SH / 2, '62% 40%') + scrim(0, 0, SW, SH / 2) + photo('Brand light', 'tex-fiber', 0, SH / 2, SW, SH / 2, '70% 35%')
      + wordmark(760, WHITE, l=150, t=SH / 2 - 76)
      + lockup('Public sector', 34, WHITE, l=190, t=1480))
F.append(('stories', artboard('st-split', 'Story · Industry × Mobility', SW, SH, BLACK, s1, 'Instagram / Facebook story', 'story')))

s2 = (photo('Brand light', 'tex-ribbon', 0, 0, SW, SH, '70% 50%')
      + rail(SW - 2 * M, TURQ, ['NEXA', 'Announcement', YEAR], M, 280, 16)
      + hl('Headline', 'WHAT’S\nNEXT IS\nHERE', WHITE, 150, l=M, t=360)
      + T('Sub-header', 'The next generation enterprise starts with one connected partner.', 'sh2', WHITE, 40, l=M, t=900, w=720)
      + f'<div class="abs row" data-name="CTA" style="left:{M}px;top:1140px;gap:16px;align-items:center">{arrow(30, TURQ)}{text("CTA", "Learn more", "sh3", TURQ, 36)}</div>'
      + wordmark(300, GRAY, l=M, t=1480))
F.append(('stories', artboard('st-announce', 'Story · Announcement', SW, SH, BLUE, s2, 'Instagram / Facebook story', 'story')))

# ---------------------------------------------------------------- 03 LINKEDIN & LANDSCAPE 1200 x 627
LW, LH, LM = 1200, 627, 48
l1 = (fill('Panel', BLUE, l=0, t=0, w=560, h=LH) + photo('Photo', 'ph-driver', 560, 0, LW - 560, LH, '45% 50%')
      + chevron(120, TURQ, 'open', l=530, t=250)
      + T('Label', 'TRANSPORT & LOGISTICS', 'label', TURQ, 16, l=LM, t=LM)
      + hl('Headline', 'EVERY ROUTE,\nCONNECTED', WHITE, 62, l=LM, t=150)
      + T('Body', LOREM, 'body', WHITE, 19, l=LM, t=320, w=440)
      + wordmark(200, GRAY, l=LM, b=LM))
F.append(('linkedin', artboard('li-split', 'LinkedIn · Split', LW, LH, BLUE, l1, 'LinkedIn / X feed image', 'land')))

l2 = (photo('Brand light', 'tex-tunnel', 600, 0, 600, LH)
      + chevron(90, TURQ, 'open', l=570, t=268)
      + rail(LW - 2 * LM, GRAY, ['NEXA', 'Event', YEAR], LM, 30, 13)
      + T('Label', 'MEET US AT', 'label', TURQ, 16, l=LM, t=120)
      + hl('Headline', 'RETAIL\nTECH EXPO', WHITE, 72, l=LM, t=150)
      + T('Date', 'Booth 1204 · 12–14 November', 'sh3', WHITE, 22, l=LM, t=330)
      + lockup('Retail', 18, WHITE, l=LM, t=400)
      + wordmark(200, BLUE, l=LM, b=LM))
F.append(('linkedin', artboard('li-event', 'LinkedIn · Event', LW, LH, BLACK, l2, 'LinkedIn / X feed image', 'land')))

# ---------------------------------------------------------------- 04 PRESENTATION 1920 x 1080
D, DH, DM = 1920, 1080, 64
d1 = (photo('Industry photo', 'ph-crowd', 0, 0, D / 2, DH, '50% 50%') + scrim(0, 0, D / 2, DH) + photo('Brand light', 'tex-fiber', D / 2, 0, D / 2, DH, '70% 40%')
      + rail(D - 2 * DM, WHITE, ['NEXA', 'Presentation title', YEAR], DM, 40, 16)
      + wordmark(900, WHITE, l=500, t=450)
      + lockup('Retail', 34, WHITE, l=662, t=900))
F.append(('slides', artboard('sl-cover', 'Slide · Cover', D, DH, BLACK, d1, 'Title slide', 'slide')))

d2 = (rail(D - 2 * DM, TURQ, ['NEXA', 'Section', YEAR], DM, 40, 16)
      + T('Index', '02', 'num', GRAY, 360, l=DM - 16, t=110)
      + hl('Headline', 'OUR\nPLATFORM', WHITE, 120, l=DM, t=770)
      + T('Body', 'Section intro. One or two sentences that set up what follows, set in Roboto Regular.', 'body', WHITE, 24, l=1180, t=820, w=620))
F.append(('slides', artboard('sl-section', 'Slide · Section divider', D, DH, BLUE, d2, 'Section divider', 'slide')))

d3 = (rail(D - 2 * DM, BLACK, ['NEXA', 'Presentation title', '03'], DM, 40, 16)
      + T('Label', 'SUB-HEADER 1', 'sh1', BLUE, 32, l=DM, t=140)
      + hl('Headline', 'ONE PARTNER,\nEVERY DEVICE', BLACK, 88, l=DM, t=196)
      + T('Sub-header 2', 'From procurement to recycling, managed as one.', 'sh2', BLACK, 36, l=DM, t=420, w=800)
      + stack('Points', [f'<div class="row" data-name="Point" style="gap:18px;align-items:flex-start">{arrow(22, BLUE)}'
                         f'<div class="stack" data-name="Text" style="gap:6px">{text("Title", a, "sh3", BLACK, 24)}{text("Detail", b_, "body", BLACK, 20)}</div></div>'
                         for a, b_ in [('Deploy', 'Kitted, configured and delivered ready to work.'), ('Manage', 'Devices, apps and data under one console.'), ('Support', 'Repair, replace and recycle with one call.')]],
              l=DM, t=560, w=760, gap=30)
      + photo('Photo', 'ph-dispatcher', 1080, 140, 700, 800, '40% 50%')
      + chevron(160, BLUE, 'open', l=1020, t=460) + chevron(160, BLUE, 'close', l=1726, t=460)
      + emblem(56, BLUE, l=DM, b=48))
F.append(('slides', artboard('sl-content', 'Slide · Content + image', D, DH, WHITE, d3, 'Content slide', 'slide')))

d4 = (rail(D - 2 * DM, GRAY, ['NEXA', 'Presentation title', '04'], DM, 40, 16)
      + hl('Headline', 'AT A GLANCE', WHITE, 88, l=DM, t=140)
      + ''.join(box('Stat', l=DM + i * 610, t=420, w=570, cls='stack', style={'gap': '18px'}, inner=
                    line('Rule', GRAY, 0, 0, 570) + text('Number', n, 'num', WHITE, 180, {'margin-top': '30px'}) + text('Label', lb, 'sh1', TURQ, 30) + text('Detail', dt, 'body', GRAY, 20, {'max-width': '480px'}))
                for i, (n, lb, dt) in enumerate([('24/7', 'SUPPORT', 'Replace with a sourced figure.'), ('360°', 'LIFECYCLE', 'Replace with a sourced figure.'), ('1', 'PARTNER', 'Replace with a sourced figure.')]))
      + emblem(56, TURQ, l=DM, b=48))
F.append(('slides', artboard('sl-stats', 'Slide · Stats', D, DH, BLACK, d4, 'Data slide', 'slide')))

d5 = (wordmark(1100, BLUE, l=(D - 1100) // 2, t=(DH - round(1100 * WM['h'] / WM['w'])) // 2)
      + rail(D - 2 * DM, GRAY, ['NEXA', 'nexa.com', YEAR], DM, DH - 60, 16))
F.append(('slides', artboard('sl-close', 'Slide · Closing', D, DH, BLACK, d5, 'End slide', 'slide')))

# ---------------------------------------------------------------- 05 WEB & EMAIL
w1 = (photo('Brand light', 'tex-grid', 0, 0, 1440, 720)
      + wordmark(200, WHITE, l=64, t=40)
      + box('Nav', r=64, t=48, cls='row', style={'gap': '40px'}, inner=''.join(text('Link', t_, 'sh2', WHITE, 17) for t_ in ['Solutions', 'Industries', 'Services', 'Contact']))
      + T('Index', '003', 'num', WHITE, 72, r=64, t=150)
      + hl('Headline', 'THE NEXT\nGENERATION\nENTERPRISE', WHITE, 96, l=64, t=230)
      + T('Sub-header', 'Mobility for every industry, delivered as one.', 'sh2', WHITE, 26, l=64, t=560)
      + f'<div class="abs row" data-name="Button" style="left:64px;top:620px;gap:14px;align-items:center;border:1.5px solid {WHITE};padding:14px 22px">'
        f'{text("Label", "Talk to us", "sh3", WHITE, 18)}{arrow(16, TURQ)}</div>')
F.append(('web', artboard('wb-hero', 'Web · Hero', 1440, 720, BLUE, w1, 'Website hero', 'web')))

w2 = (fill('Panel', BLUE, l=0, t=0, w=1200, h=400) + photo('Brand light', 'tex-ribbon', 640, 0, 560, 400, '70% 50%')
      + wordmark(200, GRAY, l=48, t=48)
      + hl('Headline', 'WHAT’S NEXT\nIN MOBILITY', WHITE, 60, l=48, t=150)
      + T('Sub-header', 'The NEXA newsletter · October', 'sh2', TURQ, 22, l=48, t=310))
F.append(('web', artboard('wb-email', 'Email · Header', 1200, 400, BLUE, w2, 'Newsletter header', 'web')))

w3 = (emblem(64, BLUE, l=24, t=36) + line('Divider', GRAY, 112, 24, 1, 112)
      + T('Name', 'FIRST LAST', 'hl', BLACK, 24, l=132, t=26)
      + T('Title', 'Job Title · Department', 'sh2', BLUE, 15, l=132, t=60)
      + T('Contact', '+1 000 000 0000 · name@nexa.com · nexa.com', 'small', BLACK, 13, l=132, t=96))
F.append(('web', artboard('wb-signature', 'Email · Signature', 600, 160, WHITE, w3, 'Email signature', 'web')))

# ---------------------------------------------------------------- 06 STATIONERY
c1 = wordmark(820, BLUE, l=64, b=64) + emblem(60, TURQ, r=64, t=64)
F.append(('print', artboard('pr-card-front', 'Business card · Front', 1050, 600, BLACK, c1, '3.5 × 2 in at 300 ppi', 'print')))
c2 = (T('Name', 'FIRST LAST', 'hl', BLUE, 44, l=64, t=64) + T('Title', 'Job Title', 'sh2', BLUE, 26, l=64, t=124)
      + stack('Contact', [text('Line', t_, 'small', BLUE, 20) for t_ in ['Mobile  +1 (000) 000 0000', 'Email  name@nexa.com', 'Address  Street, City, ST 00000', 'Web  nexa.com']], l=64, b=64, gap=8)
      + emblem(60, BLUE, r=64, b=64))
F.append(('print', artboard('pr-card-back', 'Business card · Back', 1050, 600, GRAY, c2, '3.5 × 2 in at 300 ppi', 'print')))

lt = (fill('Edge', BLUE, l=0, t=0, w=10, h=1056)
      + wordmark(200, PURPLE, l=64, t=56) + T('Department', 'ENGINEERING', 'sh1', PURPLE, 13, r=64, t=70)
      + stack('Addressee', [text('To', 'To', 'small', BLACK, 11), text('Name', 'John Smeeth', 'sh3', BLACK, 14), text('Address', '1 Palmer Road, London NW7 8B', 'small', BLACK, 11)], l=64, t=170, gap=4)
      + T('Date', 'Date · 30 September 2026', 'small', BLACK, 11, r=64, t=170)
      + stack('Letter', [text('Salutation', 'Dear Sir,', 'sh3', BLACK, 13)] + [text('Paragraph', LOREM + ' ' + LOREM, 'body', BLACK, 12) for _ in range(3)], l=64, t=290, w=560, gap=14)
      + stack('Sign-off', [text('Name', 'James Smith', 'sh3', BLACK, 13), text('Role', 'Manager', 'small', BLACK, 11)], l=64, t=700, gap=4)
      + line('Rule', GRAY, 64, 960, 688)
      + T('Footer', 'NEXA · Street, City, ST 00000 · +1 000 000 0000 · nexa.com', 'small', BLACK, 10, l=64, t=978)
      + emblem(28, BLUE, r=64, t=974))
F.append(('print', artboard('pr-letterhead', 'Letterhead', 816, 1056, WHITE, lt, 'US Letter', 'doc')))

SECTION_META = [
    ('found', 'Brand foundations', 'The rules on one page each: logo, colour, pairings, type, graphic devices and imagery. Present them, or copy them into Figma as a reference.'),
    ('social', 'Social posts', 'Square posts for Instagram and LinkedIn. Six layouts, each built from one brand device.'),
    ('stories', 'Stories', 'Vertical 9:16. Keep type out of the top 250 px and bottom 340 px (turn on Guides).'),
    ('linkedin', 'LinkedIn & landscape', '1200 × 627 feed images for LinkedIn and X.'),
    ('slides', 'Presentation', '16:9 slides: cover, section divider, content, data and close.'),
    ('web', 'Web & email', 'Website hero, newsletter header and email signature.'),
    ('print', 'Stationery', 'Business cards and letterhead.'),
]
