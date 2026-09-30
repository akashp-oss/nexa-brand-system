"""Asset library v3: rebuilt on NEXA's own references.
Sources: NEXA Brand Guidelines v1.0 · NEXA_LogoSystem (official artwork) · NEXA_Typography (N27, Roboto) ·
NEXA_Colors · Asset Inspiration (X-light and slab backgrounds, arcs, banner, business card, MWC video) ·
Healthcare One Pager · Oneview case study one-pager · client social examples (case-study card, night statement,
brandbook Instagram posts) · NEXA Figma visual identity (cut-corner containers).
Type in NEXA's collateral: N27 uppercase headlines · Roboto Light statements · Roboto Bold titles ·
Roboto Black section heads and stats · thin '>' bullets · N27 for contact details."""
from gen import *

F = []
YEAR = '2026'
VEIL = 'rgba(255,255,255,.07)'
BLUE_VEIL = 'rgba(31,31,204,.84)'        # Super Blue over a photo (NEXA case-study card)
CASE = {   # Oneview Healthcare case study (client one-pager, 2025)
    'partner': 'Oneview Healthcare',
    'title': 'Revolutionizing bedside care with the first Google-certified patient engagement solution',
    'challenge': 'Nursing shortages and ageing Windows bedside terminals made the in-room patient experience expensive to run, hard to scale and insecure.',
    'solution': [('Cost-effective hardware', 'An Android-based 22" modular monitor with 5-year availability and over-the-air updates.'),
                 ('Enhanced security', 'Biometric and RFID sign-in, Android Enterprise security and remote management.'),
                 ('Better patient experience', 'Telehealth, meal ordering, records and entertainment at the bedside.')],
    'stats': [('50', '%', 'Lower deployment costs for care facilities around the globe.'),
              ('2', 'K', 'Device rollouts in patient rooms globally.'),
              ('50', '+', 'Integrations with strategic partners.')],
}
HEALTH_USES = ['Clinical trials', 'Remote patient monitoring', 'Chronic care management', 'Telehealth', 'Senior care management',
               'Bedside technology', 'Connected readers', 'Wearables', 'Patient check-in', 'Clinic documentation']
PILLARS = [('device', 'Custom devices', 'Smartphones, tablets, wearables and kiosks, designed and built for you.'),
           ('box', 'Rhino Mobility', 'Enterprise-grade devices, Android Enterprise certified and ready to ship.'),
           ('cycle', 'Managed services', 'Staging, kitting, repair and recycling across the device lifecycle.'),
           ('signal', 'Wireless connectivity', '5G and LTE plans that work for your entire fleet.')]
ABOUT = 'NEXA is the leading provider of enterprise mobility solutions: an IoT design firm building custom devices for the world’s biggest companies.'

def hl(name, content, color, size, l=None, t=None, w=None, r=None, b=None, extra=None):
    return T(name, content, 'hl', color, size, l, t, w, r, b, extra)
def lt(name, content, color, size, l=None, t=None, w=None, r=None, b=None, extra=None):
    """Roboto Light statement (NEXA social / one-pager subheads)."""
    return T(name, content, 'lt', color, size, l, t, w, r, b, extra)
def st(name, content, color, size, l=None, t=None, w=None, r=None, b=None, extra=None):
    return T(name, content, 'st', color, size, l, t, w, r, b, extra)
def hb(name, content, color, size, l=None, t=None, w=None, r=None, b=None):
    """Roboto Black uppercase section head (one-pager)."""
    return T(name, content, 'hb', color, size, l, t, w, r, b)
def up(name, content, color, size, l=None, t=None, w=None, r=None, b=None):
    """Roboto Regular uppercase kicker, e.g. CASE STUDY."""
    return T(name, content, 'sh1', color, size, l, t, w, r, b)
def body(content, color, size, l=None, t=None, w=None, r=None, b=None, name='Body'):
    return T(name, content, 'body', color, size, l, t, w, r, b)
def scrim(l, t, w, h, a=.38, color='0,0,0'):
    return fill('Scrim', f'rgba({color},{a})', l=l, t=t, w=w, h=h)
def bg(key, w, h, pos='50% 50%', name='Background'):
    return photo(name, key, 0, 0, w, h, pos)
def lockrow(w_mark, color, l, t, partner_h=None):
    """NEXA | partner lockup: wordmark, thin divider, partner logo slot."""
    ph = partner_h or round(w_mark * .3)
    wh = round(w_mark * WM['h'] / WM['w'])
    return (wordmark(w_mark, color, l=l, t=t + (ph - wh) / 2) + line('Divider', color, l + w_mark + 36, t - 6, 2, ph + 12)
            + partner_slot(round(w_mark * 1.1), ph, color, l=l + w_mark + 74, t=t))
def button(label_, l, t, color=WHITE, size=22, name='Button'):
    return (f'<div class="abs row" data-name="{name}" style="left:{l}px;top:{t}px;gap:14px;align-items:center;border:1.5px solid {color};padding:{round(size*.7)}px {round(size*1.1)}px">'
            f'{text("Label", label_, "sh3", color, size)}{chev(round(size*.8), color)}</div>')
def cta(text_, color, size, l=None, t=None, r=None, b=None):
    pos = ';'.join(f'{k}:{px(v)}' for k, v in (('left', l), ('top', t), ('right', r), ('bottom', b)) if v is not None)
    return (f'<div class="abs row" data-name="CTA" style="{pos};gap:{round(size*.45)}px;align-items:center">'
            f'{text("CTA", text_, "sh3", color, size)}{chev(round(size*.8), color)}</div>')

# ============================================================== SQUARE POSTS 1080 x 1080
S, M = 1080, 72
def post(aid, name, bg_, inner, use='Instagram / LinkedIn / Facebook'):
    F.append(('square', artboard(aid, name, S, S, bg_, inner, use, 'post')))

post('sq-night', 'Statement · Night photo', MIDNIGHT,
     bg('phn-driver', S, S, '60% 50%') + fill('Shade', 'linear-gradient(180deg,rgba(0,10,40,.55),rgba(0,10,40,0) 60%)', l=0, t=0, w=S, h=S)
     + lt('Statement', 'Custom-built\nmobility solutions\nfor enterprise.', WHITE, 76, l=M, t=M, w=820)
     + wordmark(230, WHITE, l=M, b=M))

post('sq-case', 'Case study · Card', BLUE,
     bg('ph-clinician', S, S, '40% 50%') + fill('Super Blue veil', BLUE_VEIL, l=0, t=0, w=S, h=S)
     + slash('Slash outline', 590, 250, 420, 250, WHITE, 2)
     + lockrow(230, WHITE, M, 300)
     + up('Kicker', 'CASE STUDY', WHITE, 46, l=M, t=470)
     + st('Title', 'Revolutionizing bedside care with the first Google-certified patient engagement solution', WHITE, 50, l=M, t=548, w=900)
     + cta('Read the case study', WHITE, 24, l=M, b=M))

post('sq-xlight', 'Headline · X of light', MIDNIGHT,
     bg('tex-xlight', S, S, '78% 50%')
     + hl('Headline', 'THE NEXT\nGENERATION\nENTERPRISE', WHITE, 88, l=M, t=M)
     + lt('Sub', 'Private-label mobility,\ndesigned in the USA.', WHITE, 36, l=M, t=420)
     + wordmark(230, WHITE, l=M, b=M))

post('sq-stat', 'Stat · Arcs of light', MIDNIGHT,
     bg('tex-arcs', S, S, '35% 50%')
     + up('Kicker', 'HEALTHCARE', ACC, 26, l=M, t=M)
     + lt('Lead', 'By 2027 up to', WHITE, 44, l=M, t=210)
     + stat('60', '%', WHITE, 320, l=M - 12, t=270)
     + lt('Statement', 'of patient interactions\nwill be virtual.', WHITE, 50, l=M, t=610)
     + wordmark(230, WHITE, l=M, b=M) + T('Source', 'Source: NEXA Healthcare One Pager', 'small', WHITE, 16, r=M, b=80))

post('sq-highlights', 'Case study · Key highlights', WHITE,
     up('Kicker', 'CASE STUDY · ONEVIEW HEALTHCARE', BLUE, 22, l=M, t=M)
     + hb('Section head', 'KEY HIGHLIGHTS', BLACK, 56, l=M, t=120)
     + ''.join(stat(n, sfx, BLUE, 150, l=M, t=240 + i * 210) + body(d, BLACK, 30, l=380, t=280 + i * 210, w=620) for i, (n, sfx, d) in enumerate(CASE['stats']))
     + wordmark(230, BLUE, l=M, b=M))

post('sq-usecases', 'List · Use cases', BLUE,
     emblem(760, VEIL, r=-260, b=-160, name='X watermark')
     + hl('Headline', 'HEALTHCARE\nUSE CASES', WHITE, 76, l=M, t=M)
     + chev_list(HEALTH_USES[:5], WHITE, 30, M, 330, 440, cls='lt')
     + chev_list(HEALTH_USES[5:], WHITE, 30, 560, 330, 440, cls='lt')
     + wordmark(230, WHITE, l=M, b=M))

post('sq-pillars', 'Grid · What we do', WHITE,
     hl('Headline', 'ONE PARTNER,\nEVERY STEP', BLUE, 72, l=M, t=M)
     + ''.join(box(f'{t_} block', l=M + (i % 2) * 480, t=330 + (i // 2) * 300, w=420, cls='stack', style={'gap': '14px'}, inner=
                   icon(k, 56, BLUE, t_) + text('Title', t_.upper(), 'hb', BLUE, 30) + text('Detail', d, 'body', BLACK, 22))
               for i, (k, t_, d) in enumerate(PILLARS))
     + wordmark(200, BLUE, r=M, t=M + 16))

post('sq-android', 'Credential · Partner status', MIDNIGHT,
     bg('tex-aurora-a', S, S)
     + up('Kicker', 'WHY NEXA', WHITE, 26, l=M, t=M)
     + lt('Statement', 'One of Google’s validated Android Enterprise Gold partners.', WHITE, 66, l=M, t=260, w=880)
     + body('Every device built with Android Enterprise and Google Play Protect certified.', WHITE, 28, l=M, t=620, w=760)
     + partner_slot(300, 90, WHITE, r=M, b=M, name='Partner badge')
     + wordmark(230, WHITE, l=M, b=M + 12))

post('sq-family', 'Brand family', MIDNIGHT,
     bg('tex-aurora-b', S, S)
     + up('Kicker', 'THE NEXA FAMILY', WHITE, 26, l=M, t=M)
     + lt('Statement', 'One family of\nenterprise mobility\nbrands.', WHITE, 66, l=M, t=210)
     + partner_slot(240, 70, WHITE, l=M, t=820, name='Rhino Mobility logo')
     + wordmark(240, WHITE, l=420, t=842)
     + partner_slot(240, 70, WHITE, r=M, t=820, name='Sonim logo'))

post('sq-cta', 'Call to action · Slab of light', MIDNIGHT,
     bg('tex-slab', S, S, '72% 50%')
     + hl('Headline', 'READY FOR\nWHAT’S NEXT?', WHITE, 88, l=M, t=M)
     + lt('Sub', 'Talk to the team behind 15M+\nenterprise devices.', WHITE, 36, l=M, t=330)
     + button('Talk to us', M, 480)
     + wordmark(230, WHITE, l=M, b=M))

post('sq-xwindow', 'X window · Brandbook', GRAY,
     fill('Frame', ACC, l=0, t=0, w=S, h=S) + fill('Field', GRAY, l=22, t=22, w=S - 44, h=S - 44)
     + xwindow('X window', 'ph-crew', 110, 110, 860, 'xMidYMid', 1.15)
     + T('Tagline', 'NEXT GENERATION ENTERPRISE', 'sh3', BLUE, 22, l=M, b=M)
     + wordmark(210, BLUE, r=M, b=M))

post('sq-brackets', 'Brackets · Brandbook', BLUE,
     T('Index', '60', 'n27', WHITE, 22, l=M, t=44) + T('Topic', 'PUBLIC SAFETY', 'n27', WHITE, 22, r=M, t=44)
     + photo('Photo', 'ph-command', M, 100, S - 2 * M, 740, '60% 50%')
     + chevron(150, ACC, 'open', l=M - 54, t=395) + chevron(150, ACC, 'close', r=M - 54, t=395)
     + T('Code', 'A.1', 'hl', WHITE, 48, l=M, t=880) + T('Count', '00', 'hl', WHITE, 48, r=M, t=880)
     + wordmark(200, WHITE, l=M, b=M - 20))

post('sq-quote', 'Quote · Customer mission', WHITE,
     watermark(640, r=-120, b=-120)
     + chamfer('Photo container', M, M, 300, 300, c=60, photo_key='ph-clinician', align='xMidYMid')
     + T('Quote mark', '“', 'hl', BLUE, 200, l=870, t=40)
     + lt('Quote', 'Improve connected care experiences, everyday.', BLACK, 72, l=M, t=440, w=900)
     + T('Name', 'Oneview Healthcare', 'sh3', BLUE, 26, l=M, t=720) + body('Mission statement · NEXA customer', BLACK, 22, l=M, t=756)
     + wordmark(210, BLUE, l=M, b=M))

post('sq-news', 'News · Rebrand', MIDNIGHT,
     bg('tex-xbanner', S, S, '85% 50%') + scrim(0, 0, S, S, .25)
     + up('Kicker', 'NEWS', WHITE, 26, l=M, t=M)
     + hl('Headline', 'SOCIAL MOBILE\nIS NOW', WHITE, 96, l=M, t=210)
     + wordmark(620, WHITE, l=M, t=480)
     + lt('Sub', 'Same team, new name. One focus:\nenterprise mobility.', WHITE, 36, l=M, t=720)
     + T('URL', 'nexamobility.com', 'n27', WHITE, 22, l=M, b=M))

post('sq-spotlight', 'Industry spotlight · Container', WHITE,
     watermark(760, r=-190, t=-60)
     + up('Kicker', 'TRANSPORT & LOGISTICS', BLUE, 24, l=M, t=M)
     + chamfer('Photo container', M, 140, 600, 540, c=100, photo_key='ph-driver', align='xMidYMid')
     + body('Tablets and handhelds for fleet management, ELD compliance and asset tracking.', BLACK, 23, l=776, t=150, w=232)
     + lt('Statement', 'Every route, every driver, one fleet.', BLACK, 60, l=M, t=740, w=900)
     + wordmark(210, BLUE, r=M, b=M))

post('sq-hiring', 'Careers · We’re hiring', WHITE,
     chamfer('Photo container', M, M, 936, 520, c=110, photo_key='ph-team', align='xMidYMid')
     + up('Kicker', 'CAREERS', BLUE, 24, l=M, t=650)
     + hl('Headline', 'WE’RE HIRING', BLACK, 96, l=M, t=694)
     + body('Engineering · Product · Sales · Hollywood, Florida', BLACK, 26, l=M, t=812)
     + wordmark(210, BLUE, l=M, b=M) + cta('See open roles', BLUE, 24, r=M, b=76))

post('sq-event', 'Event · Booth', MIDNIGHT,
     bg('tex-aurora-c', S, S)
     + up('Kicker', 'MEET US AT', WHITE, 26, l=M, t=M)
     + hl('Headline', 'EVENT\nNAME 2026', WHITE, 120, l=M, t=140)
     + slash('Slash', 560, 470, 440, 250, WHITE, 2)
     + lt('Booth', 'Booth 1204', WHITE, 56, l=M, t=560) + body('12–14 November · City, State', WHITE, 28, l=M, t=640)
     + wordmark(230, WHITE, l=M, b=M))

post('sq-poll', 'Poll / question', WHITE,
     up('Kicker', 'QUICK POLL', BLUE, 24, l=M, t=M)
     + hl('Headline', 'WHAT’S NEXT\nFOR YOUR FLEET?', BLUE, 84, l=M, t=140)
     + ''.join(chamfer(f'Option {k}', M, 380 + i * 112, 936, 88, c=24, fill=TINT, inner=
                       T('Letter', k, 'hl', BLUE, 30, l=40, t=27) + T('Option', o, 'lt', BLACK, 32, l=96, t=24))
               for i, (k, o) in enumerate(zip('ABCD', ['Rugged handhelds', 'Custom tablets', 'Wearables', 'IoT gateways'])))
     + wordmark(210, BLUE, l=M, b=M) + body('Vote in the comments', BLACK, 22, r=M, b=78))

# ============================================================== CAROUSEL + PORTRAIT 1080 x 1350
PW, PH = 1080, 1350
def portrait(aid, name, bg_, inner, use='Instagram / LinkedIn carousel'):
    F.append(('portrait', artboard(aid, name, PW, PH, bg_, inner, use, 'post')))
def page_no(n, color):
    return T('Page', f'{n:02d} / 05', 'n27', color, 22, r=M, t=M)

portrait('cr-1', 'Case carousel 1/5 · Cover', BLUE,
         fill('Top panel', BLUE, l=0, t=0, w=PW, h=720) + photo('Photo', 'ph-clinician', 0, 720, PW, 630, '40% 40%')
         + lockrow(230, WHITE, M, M + 10) + page_no(1, WHITE)
         + up('Kicker', 'CASE STUDY', WHITE, 46, l=M, t=260)
         + st('Title', CASE['title'], WHITE, 54, l=M, t=340, w=900)
         + cta('Swipe', WHITE, 26, r=M, t=640))

portrait('cr-2', 'Case carousel 2/5 · Challenge', WHITE,
         up('Kicker', 'ONEVIEW HEALTHCARE × NEXA', BLUE, 22, l=M, t=M) + page_no(2, BLUE)
         + T('Number', '01', 'hl', BLUE, 200, l=M - 8, t=180)
         + hb('Section head', 'CHALLENGE', BLACK, 60, l=M, t=420)
         + lt('Text', CASE['challenge'], BLACK, 44, l=M, t=510, w=920)
         + chamfer('Photo container', 560, 950, 448, 300, c=70, photo_key='ph-crew', align='xMidYMid')
         + wordmark(200, BLUE, l=M, b=M))

portrait('cr-3', 'Case carousel 3/5 · Solution', '#F7F7F8',
         up('Kicker', 'ONEVIEW HEALTHCARE × NEXA', BLUE, 22, l=M, t=M) + page_no(3, BLUE)
         + T('Number', '02', 'hl', BLUE, 200, l=M - 8, t=180)
         + hb('Section head', 'SOLUTION', BLACK, 60, l=M, t=420)
         + ''.join(st('Point', a, BLUE, 38, l=M, t=530 + i * 210) + body(b_, BLACK, 30, l=M, t=582 + i * 210, w=900) for i, (a, b_) in enumerate(CASE['solution']))
         + wordmark(200, BLUE, l=M, b=M))

portrait('cr-4', 'Case carousel 4/5 · Results', BLUE,
         emblem(1000, VEIL, r=-380, t=260, name='X watermark')
         + up('Kicker', 'ONEVIEW HEALTHCARE × NEXA', WHITE, 22, l=M, t=M) + page_no(4, WHITE)
         + hb('Section head', 'KEY HIGHLIGHTS', WHITE, 60, l=M, t=180)
         + ''.join(stat(n, sfx, WHITE, 190, l=M, t=300 + i * 290) + lt('Detail', d, WHITE, 32, l=M, t=500 + i * 290, w=880) for i, (n, sfx, d) in enumerate(CASE['stats'])))

portrait('cr-5', 'Case carousel 5/5 · Call to action', MIDNIGHT,
         bg('tex-slab', PW, PH, '70% 50%') + page_no(5, WHITE)
         + hl('Headline', 'READY FOR\nWHAT’S\nNEXT?', WHITE, 120, l=M, t=220)
         + lt('Sub', 'Custom devices, managed services and connectivity from one partner.', WHITE, 38, l=M, t=660, w=820)
         + button('nexamobility.com', M, 860, WHITE, 28)
         + wordmark(230, WHITE, l=M, b=M))

portrait('pt-onepager', 'Portrait · Healthcare feature', WHITE,
         fill('Top panel', BLUE, l=0, t=0, w=PW, h=820) + photo('Photo', 'ph-clinician', 560, 0, 520, 820, '72% 50%')
         + fill('Blend', 'rgba(31,31,204,.55)', l=560, t=0, w=520, h=820)
         + wordmark(210, WHITE, l=M, t=M)
         + hl('Headline', 'ENTERPRISE\nMOBILITY FOR\nHEALTHCARE', WHITE, 84, l=M, t=190)
         + lt('Sub', 'Advancing the patient experience with Android Enterprise solutions.', WHITE, 38, l=M, t=500, w=720)
         + chev_list(['Custom devices for hospitals and providers', 'Remote or in-person patient experience', 'Lifecycle from manufacture to management'], BLUE, 30, M, 900, 900, cls='lt', ccolor=BLUE)
         + T('URL', 'nexamobility.com/healthcare', 'n27', BLUE, 24, l=M, b=M), 'Instagram / LinkedIn portrait')

# ============================================================== STORIES 1080 x 1920 (safe: top 250, bottom 340)
SW, SH = 1080, 1920
def story(aid, name, bg_, inner):
    F.append(('stories', artboard(aid, name, SW, SH, bg_, inner, 'Instagram / Facebook / LinkedIn story', 'story')))

story('st-night', 'Story · Night statement', MIDNIGHT,
      bg('phn-dispatcher', SW, SH, '35% 50%') + fill('Shade', 'linear-gradient(180deg,rgba(0,10,40,.6),rgba(0,10,40,0) 55%)', l=0, t=0, w=SW, h=SH)
      + lt('Statement', 'Custom-built\nmobility\nsolutions for\nenterprise.', WHITE, 100, l=M, t=280)
      + wordmark(300, WHITE, l=M, t=1480))
story('st-stat', 'Story · Stat', MIDNIGHT,
      bg('tex-arcs', SW, SH, '40% 50%')
      + up('Kicker', 'HEALTHCARE', ACC, 30, l=M, t=280)
      + lt('Lead', 'By 2027 up to', WHITE, 56, l=M, t=520)
      + stat('60', '%', WHITE, 400, l=M - 14, t=590)
      + lt('Statement', 'of patient\ninteractions will\nbe virtual.', WHITE, 72, l=M, t=1020)
      + wordmark(300, WHITE, l=M, t=1480))
story('st-case', 'Story · Case study', BLUE,
      bg('ph-clinician', SW, SH, '40% 50%') + fill('Super Blue veil', BLUE_VEIL, l=0, t=0, w=SW, h=SH)
      + slash('Slash outline', 560, 300, 460, 280, WHITE, 2)
      + lockrow(260, WHITE, M, 660)
      + up('Kicker', 'CASE STUDY', WHITE, 56, l=M, t=860)
      + st('Title', CASE['title'], WHITE, 64, l=M, t=950, w=930)
      + cta('Read more', WHITE, 32, l=M, t=1480))
story('st-event', 'Story · Event', MIDNIGHT,
      bg('tex-aurora-b', SW, SH)
      + up('Kicker', 'SEE YOU THERE', WHITE, 30, l=M, t=280)
      + hl('Headline', 'EVENT\nNAME\n2026', WHITE, 160, l=M, t=360)
      + lt('Booth', 'Booth 1204', WHITE, 72, l=M, t=960) + body('12–14 November · City, State', WHITE, 34, l=M, t=1060)
      + wordmark(300, WHITE, l=M, t=1480))

# ============================================================== LINKEDIN & X
LW, LH, LM = 1200, 627, 56
def land(aid, name, bg_, inner, w=LW, h=LH, use='LinkedIn / X feed image'):
    F.append(('linkedin', artboard(aid, name, w, h, bg_, inner, use, 'land')))

land('li-case', 'LinkedIn · Case study card', BLUE,
     bg('ph-clinician', LW, LH, '40% 40%') + fill('Super Blue veil', BLUE_VEIL, l=0, t=0, w=LW, h=LH)
     + slash('Slash outline', 760, 60, 380, 220, WHITE, 2)
     + lockrow(190, WHITE, LM, 120)
     + up('Kicker', 'CASE STUDY', WHITE, 36, l=LM, t=250)
     + st('Title', 'Revolutionizing bedside care with the first\nGoogle-certified patient engagement solution', WHITE, 38, l=LM, t=320, w=1080))
land('li-statement', 'LinkedIn · X of light', MIDNIGHT,
     bg('tex-xlight', LW, LH, '80% 50%')
     + hl('Headline', 'THE NEXT\nGENERATION\nENTERPRISE', WHITE, 64, l=LM, t=LM)
     + lt('Sub', 'Private-label mobility, designed in the USA.', WHITE, 24, l=LM, t=300)
     + wordmark(200, WHITE, l=LM, b=LM))
land('li-stat', 'LinkedIn · Stat', MIDNIGHT,
     bg('tex-arcs', LW, LH, '50% 50%')
     + lt('Lead', 'By 2027 up to', WHITE, 30, l=LM, t=LM)
     + stat('60', '%', WHITE, 230, l=LM - 8, t=100)
     + lt('Statement', 'of patient interactions\nwill be virtual.', WHITE, 38, l=LM, t=350)
     + wordmark(200, WHITE, l=LM, b=LM))
land('li-hiring', 'LinkedIn · Hiring', WHITE,
     chamfer('Photo container', LM, LM, 540, 515, c=90, photo_key='ph-team', align='xMidYMid')
     + up('Kicker', 'CAREERS', BLUE, 20, l=660, t=LM)
     + hl('Headline', 'WE’RE\nHIRING', BLACK, 76, l=660, t=100)
     + body('Engineering · Product · Sales\nHollywood, Florida', BLACK, 22, l=660, t=290)
     + cta('See open roles', BLUE, 22, l=660, t=390)
     + wordmark(200, BLUE, l=660, b=LM))
land('li-event', 'LinkedIn · Event', MIDNIGHT,
     bg('tex-aurora-c', LW, LH)
     + up('Kicker', 'MEET US AT', WHITE, 20, l=LM, t=LM)
     + hl('Headline', 'EVENT NAME 2026', WHITE, 72, l=LM, t=110)
     + lt('Booth', 'Booth 1204 · 12–14 November · City, State', WHITE, 28, l=LM, t=210)
     + slash('Slash', 760, 330, 380, 220, WHITE, 2)
     + wordmark(200, WHITE, l=LM, b=LM))
land('li-banner', 'LinkedIn · Company banner', MIDNIGHT,
     bg('tex-xbanner', 1584, 396, '80% 50%')
     + lt('Statement', 'Custom-built mobility\nsolutions for enterprise.', WHITE, 44, l=560, t=110)
     + T('URL', 'nexamobility.com', 'n27', WHITE, 20, l=560, t=250),
     w=1584, h=396, use='LinkedIn company cover (keep the left third clear for the logo)')

# ============================================================== SALES COLLATERAL (US Letter)
CW, CH = 816, 1056
def coll(aid, name, inner, use):
    F.append(('collateral', artboard(aid, name, CW, CH, WHITE, inner, use, 'doc')))

coll('co-onepager', 'One-pager · Industry', (
    fill('Hero', BLUE, l=0, t=0, w=CW, h=372) + photo('Photo', 'ph-clinician', 500, 0, 316, 372, '70% 50%')
    + fill('Blend', 'rgba(31,31,204,.5)', l=500, t=0, w=316, h=372)
    + wordmark(96, WHITE, l=44, t=36)
    + hl('Headline', 'ENTERPRISE MOBILITY\nFOR HEALTHCARE', WHITE, 44, l=44, t=78)
    + lt('Sub', 'Advancing the patient experience\nwith Android Enterprise solutions.', WHITE, 21, l=44, t=196)
    + chev_list(['Custom, enterprise-grade devices for hospitals and providers', 'Improve the patient experience, remote or in-person', 'Streamline the device lifecycle end to end'], WHITE, 12, 44, 262, 420, gap=6)
    + lt('Intro', 'Smartphones, tablets and wearables are changing healthcare: telehealth, remote patient monitoring, clinical trials. A custom mobility solution keeps those devices purpose-built, secure and available for up to five years.', BLACK, 12.5, l=52, t=400, w=470)
    + T('Stat lead', 'By 2027 up to', 'small', BLACK, 11, l=600, t=404) + stat('60', '%', BLUE, 76, l=600, t=420) + T('Stat detail', 'of patient interactions\nwill be virtual.', 'small', BLACK, 11, l=600, t=500)
    + line('Rule', '#BDBDBD', 44, 560, 728)
    + hb('Section head', 'HEALTHCARE\nUSE CASES AND\nAPPLICATIONS', BLUE, 23, l=52, t=580)
    + chev_list(HEALTH_USES[:5], BLACK, 11.5, 300, 584, 220, gap=4, ccolor=BLUE, cls='lt') + chev_list(HEALTH_USES[5:], BLACK, 11.5, 540, 584, 220, gap=4, ccolor=BLUE, cls='lt')
    + line('Rule', '#BDBDBD', 44, 720, 728)
    + ''.join(box(f'{t_} column', l=52 + i * 182, t=738, w=164, cls='stack', style={'gap': '6px'}, inner=
                  icon(k, 26, BLUE, t_) + text('Title', t_.upper(), 'hb', BLUE, 14) + text('Detail', d, 'lt', BLACK, 10.5))
              for i, (k, t_, d) in enumerate(PILLARS))
    + line('Rule', '#BDBDBD', 44, 900, 728)
    + wordmark(96, BLUE, l=44, t=918) + T('About', ABOUT, 'small', BLACK, 8.5, l=44, t=944, w=300)
    + qr_dots('https://nexamobility.com/healthcare', 60, BLACK, l=470, t=918)
    + T('Contact', 'Sales      sales@nexamobility.com\nWebsite  nexamobility.com\nSupport  support.nexamobility.com', 'small', BLUE, 9.5, l=560, t=920)
    + T('Legal', '© 2026 NEXA. All rights reserved.', 'small', BLACK, 7.5, l=44, t=1020)), 'US Letter one-pager')

coll('co-casestudy', 'Case study · One-pager', (
    fill('Hero', BLUE, l=0, t=0, w=520, h=212) + photo('Photo', 'ph-clinician', 520, 0, 296, 212, '60% 50%')
    + lockrow(80, WHITE, 32, 34) + up('Kicker', 'CASE STUDY', WHITE, 18, l=32, t=84)
    + st('Title', 'Revolutionizing bedside care with the first\nGoogle-certified patient engagement solution', WHITE, 18.5, l=32, t=124, w=470)
    + fill('Side column', '#F6F6F7', l=0, t=212, w=292, h=844)
    + hb('Head', 'OVERVIEW', BLACK, 17, l=32, t=240) + lt('Text', 'Oneview Healthcare, with NEXA, developed the first 22" Google-certified all-in-one patient engagement solution.', BLACK, 11.5, l=32, t=270, w=236)
    + hb('Head', 'KEY HIGHLIGHTS', BLACK, 17, l=32, t=400)
    + ''.join(stat(n, sfx, BLUE, 40, l=32, t=436 + i * 66) + T('Detail', d, 'lt', BLACK, 10.5, l=112, t=440 + i * 66, w=160) for i, (n, sfx, d) in enumerate(CASE['stats']))
    + hb('Head', 'PARTNERS', BLACK, 17, l=32, t=650) + partner_slot(100, 34, '#9A9A9A', l=32, t=682) + partner_slot(100, 34, '#9A9A9A', l=146, t=682)
    + hb('Head', 'NEXA', BLACK, 17, l=32, t=750) + lt('About', ABOUT, BLACK, 11, l=32, t=778, w=236)
    + T('Link', 'Visit nexamobility.com for more.', 'small', BLACK, 11, l=32, t=880)
    + hb('Head', 'CHALLENGE', BLACK, 17, l=330, t=240) + lt('Text', CASE['challenge'], BLACK, 11.5, l=330, t=270, w=450)
    + hb('Head', 'SOLUTION', BLACK, 17, l=330, t=360)
    + ''.join(st('Point', a + ':', BLUE, 12.5, l=330, t=392 + i * 70) + lt('Detail', b_, BLACK, 11.5, l=330, t=412 + i * 70, w=450) for i, (a, b_) in enumerate(CASE['solution']))
    + hb('Head', 'CONCLUSION', BLACK, 17, l=330, t=620)
    + lt('Text', 'Oneview Healthcare and NEXA have redefined patient care and clinical workflows with a seamless, connected bedside experience.', BLACK, 11.5, l=330, t=650, w=200)
    + chamfer('Product photo', 560, 640, 220, 200, c=36, photo_key='ph-dispatcher', align='xMidYMid')
    + wordmark(96, BLUE, r=36, b=36)), 'US Letter case study')

# ============================================================== PRESENTATION 1920 x 1080
D, DH, DM = 1920, 1080, 80
def slide(aid, name, bg_, inner, use):
    F.append(('slides', artboard(aid, name, D, DH, bg_, inner, use, 'slide')))

slide('sl-cover', 'Slide · Cover', MIDNIGHT,
      bg('tex-xlight', D, DH, '85% 50%')
      + wordmark(260, WHITE, l=DM, t=DM)
      + hl('Headline', 'PRESENTATION\nTITLE GOES HERE', WHITE, 120, l=DM, t=360)
      + lt('Sub', 'Subtitle or presenter name · Month 2026', WHITE, 36, l=DM, t=640), 'Title slide')
slide('sl-section', 'Slide · Section divider', MIDNIGHT,
      bg('tex-arcs', D, DH)
      + T('Index', '02', 'hl', WHITE, 300, l=DM - 12, t=DM)
      + hl('Headline', 'OUR PLATFORM', WHITE, 120, l=DM, t=820), 'Section divider')
slide('sl-content', 'Slide · Content + image', WHITE,
      up('Kicker', 'WHAT WE DO', BLUE, 30, l=DM, t=DM)
      + hl('Headline', 'ONE PARTNER,\nEVERY DEVICE', BLACK, 96, l=DM, t=140)
      + lt('Sub', 'From design to recycling, managed as one.', BLACK, 40, l=DM, t=380, w=820)
      + chev_list([p[1] + ': ' + p[2] for p in PILLARS], BLACK, 28, DM, 500, 820, gap=22, ccolor=BLUE, cls='lt')
      + chamfer('Photo container', 1020, 120, 820, 840, c=140, photo_key='ph-dispatcher', align='xMidYMid')
      + wordmark(200, BLUE, l=DM, b=DM - 20), 'Content slide')
slide('sl-stats', 'Slide · Key highlights', BLUE,
      emblem(1200, VEIL, r=-300, t=-100, name='X watermark')
      + up('Kicker', 'CASE STUDY · ONEVIEW HEALTHCARE', WHITE, 28, l=DM, t=DM)
      + hb('Section head', 'KEY HIGHLIGHTS', WHITE, 80, l=DM, t=140)
      + ''.join(box('Stat', l=DM + i * 600, t=420, w=540, cls='stack', style={'gap': '20px'}, inner=
                    line('Rule', WHITE, 0, 0, 540) + stat(n, sfx, WHITE, 200).replace('class="abs ', 'class="') + text('Detail', d, 'lt', WHITE, 30))
                for i, (n, sfx, d) in enumerate(CASE['stats']))
      + wordmark(200, WHITE, l=DM, b=DM - 20), 'Data slide')
slide('sl-close', 'Slide · Closing', BLACK,
      wordmark(1100, BLUE, l=(D - 1100) // 2, t=(DH - round(1100 * WM['h'] / WM['w'])) // 2)
      + T('URL', 'nexamobility.com', 'n27', GRAY, 28, l=DM, b=DM), 'End slide')

# ============================================================== WEB & EMAIL
def web(aid, name, w, h, bg_, inner, use):
    F.append(('web', artboard(aid, name, w, h, bg_, inner, use, 'web')))

web('wb-hero', 'Web · Hero', 1440, 720, MIDNIGHT,
    bg('tex-xlight', 1440, 720, '80% 50%')
    + wordmark(180, WHITE, l=64, t=40)
    + box('Nav', r=64, t=46, cls='row', style={'gap': '40px'}, inner=''.join(text('Link', t_, 'sh2', WHITE, 16) for t_ in ['Solutions', 'Industries', 'Why NEXA', 'News', 'Contact']))
    + hl('Headline', 'THE NEXT\nGENERATION\nENTERPRISE', WHITE, 88, l=64, t=200)
    + lt('Sub', 'Private-label devices, software and services, designed in the USA and deployed at scale.', WHITE, 22, l=64, t=500, w=560)
    + button('Talk to us', 64, 590, WHITE, 18), 'Website hero')
web('wb-cta', 'Web · CTA section', 1440, 560, MIDNIGHT,
    bg('tex-slab', 1440, 560, '70% 50%')
    + hl('Headline', 'READY FOR\nWHAT’S NEXT?', WHITE, 72, l=64, t=140)
    + lt('Sub', 'Talk to our enterprise mobility team.', WHITE, 24, l=64, t=320)
    + button('Contact sales', 64, 400, WHITE, 18), 'Website call-to-action band')
web('wb-email', 'Email · Header', 1200, 400, MIDNIGHT,
    bg('tex-aurora-a', 1200, 400)
    + wordmark(180, WHITE, l=48, t=48)
    + hl('Headline', 'WHAT’S NEXT\nIN MOBILITY', WHITE, 60, l=48, t=150)
    + lt('Sub', 'The NEXA newsletter · October', WHITE, 22, l=48, t=310), 'Newsletter header')
web('wb-signature', 'Email · Signature', 600, 160, WHITE,
    emblem(64, BLUE, l=24, t=46) + line('Divider', GRAY, 112, 24, 1, 112)
    + T('Name', 'First Last', 'sh2', BLACK, 22, l=132, t=24)
    + T('Title', 'Job Title', 'lt', BLACK, 15, l=132, t=56)
    + T('Contact', '+1 (000) 000-0000  ·  name@nexamobility.com\nnexamobility.com', 'n27', '#6F6F6F', 13, l=132, t=90), 'Email signature')

# ============================================================== STATIONERY
def pr(aid, name, w, h, bg_, inner, use, fmt='print'):
    F.append(('print', artboard(aid, name, w, h, bg_, inner, use, fmt)))

pr('pr-card-front', 'Business card · Front', 1050, 600, BLUE, wordmark(560, WHITE, l=(1050 - 560) // 2, t=(600 - round(560 * WM['h'] / WM['w'])) // 2), '3.5 × 2 in at 300 ppi')
pr('pr-card-back', 'Business card · Back', 1050, 600, WHITE,
   T('Name', 'First Last', 'sh2', BLACK, 50, l=48, t=48)
   + T('Details', 'Job Title\n+1 (000) 000-0000\nname@nexamobility.com', 'n27', '#6F6F6F', 26, l=48, t=128)
   + T('Address', '2057 Coolidge Street\nHollywood, FL, 33020\nUnited States', 'n27', '#6F6F6F', 26, l=48, t=344)
   + T('Web', 'www.nexamobility.com', 'n27', '#6F6F6F', 26, l=48, t=500)
   + qr_dots('https://nexamobility.com', 190, BLUE, r=48, t=52)
   + wordmark(146, BLUE, r=48, b=64), '3.5 × 2 in at 300 ppi (from the NEXA card)')
pr('pr-letterhead', 'Letterhead', 816, 1056, WHITE,
   fill('Edge', BLUE, l=0, t=0, w=10, h=1056)
   + wordmark(170, MIDNIGHT, l=64, t=56) + T('Department', 'ENGINEERING', 'sh3', MIDNIGHT, 13, r=64, t=72)
   + stack('Addressee', [text('To', 'To', 'small', BLACK, 11), text('Name', 'Recipient Name', 'sh3', BLACK, 14), text('Address', 'Street, City, Postcode', 'small', BLACK, 11)], l=64, t=170, gap=4)
   + T('Date', 'Date · 30 September 2026', 'small', BLACK, 11, r=64, t=170)
   + stack('Letter', [text('Salutation', 'Dear Name,', 'sh3', BLACK, 13)] + [text('Paragraph', ABOUT + ' ' + ABOUT, 'body', BLACK, 12) for _ in range(3)], l=64, t=290, w=560, gap=14)
   + stack('Sign-off', [text('Name', 'Sender Name', 'sh3', BLACK, 13), text('Role', 'Job Title', 'small', BLACK, 11)], l=64, t=700, gap=4)
   + T('Footer', '2057 Coolidge Street, Hollywood, FL 33020 · nexamobility.com', 'n27', '#6F6F6F', 10, l=64, t=990), 'US Letter', 'doc')

SECTION_META = [
    ('square', 'Social · Square posts', 'Eighteen 1080 × 1080 posts built from NEXA’s own references: night statements, case-study cards, X and slab of light, arcs, aurora, highlights, use cases, brandbook posts and containers.'),
    ('portrait', 'Social · Carousel & portrait', 'A five-slide case-study carousel (Oneview Healthcare) and a healthcare feature post, 1080 × 1350.'),
    ('stories', 'Social · Stories', 'Vertical 9:16. Keep type out of the top 250 px and bottom 340 px (turn on Guides).'),
    ('linkedin', 'LinkedIn & X', '1200 × 627 feed images and the 1584 × 396 company banner.'),
    ('collateral', 'Sales collateral', 'US Letter one-pager and case-study templates, rebuilt from the NEXA healthcare and Oneview one-pagers.'),
    ('slides', 'Presentation', '16:9 slides: cover, section divider, content, highlights and close.'),
    ('web', 'Web & email', 'Website hero and CTA band, newsletter header, email signature.'),
    ('print', 'Stationery', 'Business card (from the NEXA card) and letterhead.'),
]
