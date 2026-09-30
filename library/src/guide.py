"""Brand guidelines view: the brandbook rules as 1920 x 1080 boards (logo, colour, type, devices, imagery,
containers, secondary colour study). Kept out of the asset library so the library opens on usable assets."""
from gen import *

F = []
YEAR = '2026'

def hl(name, content, color, size, l=None, t=None, w=None, r=None, b=None, extra=None):
    return T(name, content, 'hl', color, size, l, t, w, r, b, extra)

def scrim(l, t, w, h, a=.38):
    return fill('Scrim', f'rgba(0,0,0,{a})', l=l, t=t, w=w, h=h)

# ---------------------------------------------------------------- 00 BRAND FOUNDATIONS (1920 x 1080 boards)
BW, BH, BM = 1920, 1080, 64

def board_intro(num, label, title, body, color=BLACK, accent=BLUE, rail_color=None):
    return (rail(BW - 2 * BM, rail_color or color, ['NEXA', 'Brand asset library · Version 1.0', YEAR], BM, 36, 14)
            + stack('Intro', [text('Section label', f'{num}  ·  {label}', 'label', accent, 16),
                              text('Headline', title, 'hl', color, 84),
                              text('Body', body, 'body', color, 18, {'max-width': '470px', 'margin-top': '12px'})],
                    l=BM, t=132, w=520, gap=22))

f1 = (photo('Brand light', 'tex-aurora-a', 0, 0, BW, BH)
      + rail(BW - 2 * BM, WHITE, ['NEXA', 'Brand asset library · Version 1.0', YEAR], BM, BH - 60, 14)
      + hl('Kicker', 'WHAT’S NEXT', ACC, 40, l=BM, t=64)
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
            + box('Clear space', l=cs_l, t=cs_t, w=cs_w, h=cs_h, cls='guide-line', style={'border': f'1.5px dashed {ACC}'})
            + ''.join(fill('X unit', '#1B1B1B', l=cs_l + dx, t=cs_t + dy, w=xs, h=xs, style={'outline': '1px solid #3A3A3A'})
                      for dx, dy in [(0, 0), (cs_w - xs, 0), (0, cs_h - xs), (cs_w - xs, cs_h - xs)])
            + wordmark(wm_w, WHITE, l=cs_l + xs, t=cs_t + xs)
            + T('Caption', 'Clear space = height of the X on every side', 'small', GRAY, 14, l=24, b=20))
      + ''.join(box(f'Tile {i+1}', l=720 + i * 385, t=620, w=366, h=360, cls='group', inner=inner)
                + T('Tile caption', cap, 'small', BLACK, 14, l=720 + i * 385, t=994, w=366)
                for i, (inner, cap) in enumerate([
                    (fill('Tile fill', BLUE, l=0, t=0, w=366, h=360) + wordmark_tagline(250, GRAY, l=58, t=146),
                     'Wordmark + tagline “Next Generation Enterprise”'),
                    (fill('Tile fill', BLACK, l=0, t=0, w=366, h=360) + emblem(150, ACC, l=108, t=128),
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
rows = [('HEADER', 'hl', 120, 'N27 Regular · 120 pt', 'Uppercase'),
        ('SUB-HEADER 1', 'sh1', 48, 'Roboto Regular · 48 pt', 'Uppercase'),
        ('Sub-Header 2', 'sh2', 36, 'Roboto Regular · 36 pt', 'Title Case'),
        ('Sub-Header 3', 'sh3', 24, 'Roboto Bold · 24 pt', 'Title Case')]
f5 = (board_intro('03', 'Typography', 'CLEAR,\nBOLD, NEXT',
                  'N27 for headlines, always uppercase and never bold, and for contact details. Roboto Light for statements, '
                  'Roboto Bold for titles, Roboto Black for section heads and big numbers. Each level steps by about 1.5×.')
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
                  'and the X joins an industry to mobility.', WHITE, ACC, GRAY)
      + tile(0, 'Brackets', fill('Fill', BLUE, l=0, t=0, w=gw, h=gh) + photo('Image', 'ph-command', 70, 40, gw - 140, gh - 80, '60% 50%')
             + chevron(110, ACC, 'open', l=36, t=145) + chevron(110, ACC, 'close', r=36, t=145),
             'Brackets  ><  frame an image or a focal point. Secondary colour on Super Blue or black.')
      + tile(1, 'X window', fill('Fill', GRAY, l=0, t=0, w=gw, h=gh) + xwindow('X window', 'ph-clinician', 99, 32, 400, 'xMidYMid', 1.25),
             'X window: a photo seen through the emblem, on Base Gray or the secondary tint.')
      + tile(2, 'Industry x Mobility', photo('Photo', 'ph-dispatcher', 0, 0, gw / 2, gh, '40% 50%') + scrim(0, 0, gw / 2, gh) + fill('Panel', BLUE, l=gw / 2, t=0, w=gw / 2, h=gh)
             + lockup('Public safety', 26, WHITE, l=86, t=178),
             'INDUSTRY  X  MOBILITY lockup across a split: two worlds converging.')
      + tile(3, 'Rail and arrow', fill('Fill', BLUE, l=0, t=0, w=gw, h=gh) + rail(gw - 64, ACC, ['NEXA', 'Version 1.0', YEAR], 32, 28, 13)
             + stack('List', [f'<div class="row" data-name="Item" style="gap:16px;align-items:center">{arrow(22, ACC)}{text("Item", t_, "sh2", WHITE, 28)}</div>'
                              for t_ in ['Deploy', 'Manage', 'Support']], l=32, t=120, gap=22)
             + T('Index', '003', 'num', WHITE, 110, r=32, b=16),
             'Meta rail, forward-arrow bullets and index numbers give pages rhythm.'))
F.append(('found', artboard('fd-devices', 'Foundations · Graphic devices', BW, BH, BLACK, f6, 'Brand board', 'board')))

# imagery
f7 = (board_intro('05', 'Imagery', 'REAL WORK,\nIN THREE TONES',
                  'People and devices at work, cropped into the action. Three treatments, as in NEXA’s own posts: natural colour; '
                  'night tone for statements over a photo; and a Super Blue veil for case-study cards. Light comes from NEXA’s '
                  'own backgrounds and the MWC video, never from stock effects.')
      + T('Row label', 'NATURAL  ·  NIGHT TONE  ·  SUPER BLUE VEIL (CASE STUDIES)', 'label', BLUE, 15, l=640, t=112)
      + ''.join(photo(n, k, 640 + i * 412, 142, 392, 380, p) for i, (n, k, p) in enumerate([('Natural', 'ph-crew', '50% 50%'), ('Night tone', 'phn-driver', '50% 50%'), ('Super Blue veil', 'ph-clinician', '40% 40%')]))
      + fill('Veil', 'rgba(31,31,204,.84)', l=1464, t=142, w=392, h=380)
      + T('Row label', 'LIGHT · FROM NEXA’S OWN BACKGROUNDS AND MWC VIDEO', 'label', BLUE, 15, l=640, t=566)
      + ''.join(photo(n, k, 640 + i * 412, 596, 392, 380, p) for i, (n, k, p) in enumerate([('X of light', 'tex-xlight', '80% 50%'), ('Arcs of light', 'tex-arcs', '40% 50%'), ('Aurora (MWC video)', 'tex-aurora-b', '50% 50%')]))
      + T('Note', 'Photos are placeholders from the Sonim library. Replace with licensed NEXA photography.', 'small', BLACK, 13, l=640, t=1000))
F.append(('found', artboard('fd-imagery', 'Foundations · Imagery', BW, BH, WHITE, f7, 'Brand board', 'board')))


# containers (from the NEXA Figma "Visual identity" page)
f8 = (board_intro('06', 'Containers', 'CUT CORNERS,\nCLEAR SPACE',
                  'Content sits in a rectangle with the top-left and bottom-right corners cut, echoing the angles of the X. '
                  'Nothing is added outside the shape. Keep the live area equally inset from every edge, cuts included.')
      + chamfer('Container', 760, 330, 420, 420, c=64, stroke=BLACK, sw=3)
      + chamfer('Container with live area', 1330, 150, 460, 620, c=100, stroke=BLACK, sw=3, live=(26, '#FFD6E8'),
                inner=T('Live area text', 'The live area\nshould be equally\ninset from the\nedge of the\nrectangle.', 'st', BLACK, 42, l=40, t=140, w=400))
      + stack('Rules', [f'<div class="row" data-name="Rule" style="gap:14px;align-items:flex-start">{chev(18, BLUE)}{text("Rule", r_, "body", BLACK, 17)}</div>'
                        for r_ in ['Cut only the top-left and bottom-right corners, at the same angle.',
                                   'Cut ≈ 16% of the short side; vertical run ≈ 1.2 × horizontal run.',
                                   'Fill with a photo, Super Blue, white or a light tint; outline in black on white.',
                                   'No flaps, shadows or extra shapes around the container.']],
              l=BM, t=640, w=520, gap=14))
F.append(('found', artboard('fd-containers', 'Foundations · Containers', BW, BH, WHITE, f8, 'Brand board', 'board')))

# secondary colour study (static swatches, independent of the live switcher)
def study_col(i, key, name, acc, tint, note):
    x, cw = 640 + i * 250, 232
    post = (fill('Post', BLUE, l=0, t=0, w=cw, h=cw) + T('Label', 'INSIGHT', 'lbl', acc, 13, l=18, t=18)
            + T('Line', 'What’s\nnext.', 'st', WHITE, 30, l=18, t=70) + emblem(34, acc, r=16, b=16) + wordmark(120, GRAY, l=18, b=20))
    dark = (fill('Dark', BLACK, l=0, t=0, w=cw, h=110) + T('Number', '15M+', 'num', WHITE, 52, l=16, t=20) + T('Caption', 'DEVICES DEPLOYED', 'lbl', acc, 11, l=18, t=80))
    light = (fill('Tint', tint, l=0, t=0, w=cw, h=150) + chamfer('Chip', 18, 20, 120, 60, c=16, fill=BLUE)
             + T('Tint hex', tint.upper(), 'small', BLACK, 13, l=18, t=110))
    return box(f'{name} study', l=x, t=150, w=cw, h=800, cls='group', inner=
               T('Name', name.upper(), 'lbl', BLUE if key != 'lavender' else BLUE, 15, l=0, t=-40)
               + box('On blue', l=0, t=0, w=cw, h=cw, cls='group', inner=post)
               + box('On black', l=0, t=252, w=cw, h=110, cls='group', inner=dark)
               + box('Tint', l=0, t=382, w=cw, h=150, cls='group', inner=light)
               + fill('Swatch', acc, l=0, t=552, w=cw, h=56) + T('Accent hex', acc.upper(), 'sh3', BLACK, 15, l=0, t=620)
               + T('Note', note, 'small', BLACK, 14, l=0, t=648, w=cw)
               + (T('Pick', 'RECOMMENDED', 'lbl', BLUE, 12, l=0, t=760) if key == 'lavender' else ''))
f9 = (board_intro('07', 'Secondary colour', 'LIGHT,\nNOT NEON',
                  'NEXA’s own backgrounds answer the question: Midnight grounds lit by Electric Blue and Sky. Electric Azure '
                  'is the secondary for marks and labels; Bright Turquoise stays as a thin line of light. Compare them live '
                  'with the Secondary switcher.')
      + ''.join(fill(n, c, l=BM + i * 176, t=760, w=160, h=120) + T('Name', n.upper(), 'label', BLACK, 12, l=BM + i * 176, t=892)
                + T('Hex', c, 'small', BLACK, 13, l=BM + i * 176, t=912)
                for i, (n, c) in enumerate([('Midnight', MIDNIGHT), ('Electric', ELECTRIC), ('Sky', SKY)]))
      + ''.join(study_col(i, *a) for i, a in enumerate(ACCENTS)))
F.append(('found', artboard('fd-secondary', 'Foundations · Secondary colour study', BW, BH, WHITE, f9, 'Brand board', 'board')))

SECTION_META = [
    ('found', 'Brand guidelines', 'The rules on one board each: logo, colour, pairings, type, graphic devices, imagery, containers and the secondary colour study. Present them, or copy them into Figma as a reference.'),
]
