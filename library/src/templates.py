"""Asset library: social-first templates for NEXA.
Rules: NEXA Brand Guidelines v1.0 (logo, colour, type) + NEXA Figma visual identity (cut-corner containers,
Base Gray slabs, pale X watermark, Roboto Bold statements) + nexamobility.com positioning.
Secondary colour is live (ACC / TINT css variables), photography is natural colour."""
from gen import *

F = []
YEAR = '2026'
LOREM = 'NEXA brings devices, software and services together so enterprises can deploy, manage and support mobility at scale.'
VEIL = 'rgba(255,255,255,.07)'          # X watermark on Super Blue / black

def hl(name, content, color, size, l=None, t=None, w=None, r=None, b=None, extra=None):
    return T(name, content, 'hl', color, size, l, t, w, r, b, extra)
def st(name, content, color, size, l=None, t=None, w=None, r=None, b=None, extra=None):
    """Statement: Roboto Bold, sentence case (NEXA Figma)."""
    return T(name, content, 'st', color, size, l, t, w, r, b, extra)
def lbl(content, color, size, l=None, t=None, r=None, b=None, name='Label'):
    return T(name, content, 'lbl', color, size, l, t, None, r, b)
def body(content, color, size, l=None, t=None, w=None, r=None, b=None, name='Body'):
    return T(name, content, 'body', color, size, l, t, w, r, b)
def scrim(l, t, w, h, a=.38):
    return fill('Scrim', f'rgba(0,0,0,{a})', l=l, t=t, w=w, h=h)
def cta(text_, color, size, l=None, t=None, r=None, b=None, arrow_color=None):
    pos = st_ = {k: px(v) for k, v in (('left', l), ('top', t), ('right', r), ('bottom', b)) if v is not None}
    return (f'<div class="abs row" data-name="CTA" style="{";".join(f"{k}:{v}" for k, v in pos.items())};gap:{round(size*.45)}px;align-items:center">'
            f'{text("CTA", text_, "sh3", color, size)}{arrow(round(size*.8), arrow_color or color)}</div>')
def bullets(items, color, sub_color, size, l, t, w, gap=34, acolor=ACC):
    rows = []
    for a, b_ in items:
        inner = text('Point', a, 'st', color, size) + (text('Detail', b_, 'body', sub_color, round(size * .68)) if b_ else '')
        rows.append(f'<div class="row" data-name="Item" style="gap:{round(size*.6)}px;align-items:flex-start">'
                    f'<div style="padding-top:{round(size*.14)}px">{arrow(round(size*.72), acolor)}</div><div class="stack" data-name="Text" style="gap:6px">{inner}</div></div>')
    return stack('List', rows, l=l, t=t, w=w, gap=gap)

# ============================================================== SQUARE POSTS 1080 x 1080
S, M = 1080, 72
sq = []
def post(aid, name, bg, inner, use='Instagram / LinkedIn / Facebook'):
    F.append(('square', artboard(aid, name, S, S, bg, inner, use, 'post')))

post('sq-spot-health', 'Industry spotlight · Healthcare', WHITE,
     watermark(780, r=-190, t=-60)
     + lbl('HEALTHCARE', BLUE, 22, l=M, t=M)
     + chamfer('Photo container', M, 140, 600, 540, c=100, photo_key='ph-clinician', align='xMidYMid')
     + body('Remote monitoring, telehealth and secure medical gateways on devices designed in the USA.', BLACK, 23, l=776, t=150, w=232)
     + st('Statement', 'Devices built for the bedside, not the back office.', BLACK, 58, l=M, t=736, w=900)
     + wordmark(210, BLUE, r=M, b=M))

post('sq-spot-logistics', 'Industry spotlight · Logistics', TINT,
     lbl('TRANSPORT & LOGISTICS', BLUE, 22, l=M, t=M)
     + st('Statement', 'Every route, every driver, one fleet.', BLUE, 66, l=M, t=140, w=440)
     + body('Purpose-built tablets and handhelds for ELD compliance, asset tracking and route optimisation.', BLACK, 25, l=M, t=520, w=400)
     + chamfer('Photo container', 560, 170, 448, 700, c=96, photo_key='ph-driver', align='xMidYMid')
     + wordmark(210, BLUE, l=M, b=M))

post('sq-spot-safety', 'Industry spotlight · Public safety', BLACK,
     chamfer('Photo container', M, M, 936, 560, c=110, photo_key='ph-crew', align='xMidYMid')
     + lbl('PUBLIC SAFETY', ACC, 22, l=M, t=700)
     + st('Statement', 'When every second counts, the device can’t be the weak link.', WHITE, 50, l=M, t=744, w=900)
     + wordmark(210, BLUE, l=M, b=M) + emblem(60, ACC, r=M, b=M))

post('sq-insight', 'Insight card', TINT,
     chamfer('Insight container', M, M, 936, 780, c=130, fill=BLUE, inner=
             emblem(380, VEIL, l=520, t=330, name='X watermark')
             + lbl('INSIGHT', ACC, 22, l=64, t=150)
             + st('Statement', 'Consumer phones were never built to be managed by the thousand.', WHITE, 64, l=64, t=200, w=800)
             + body('Private-label devices are specified, imaged and supported for one job: yours.', GRAY, 26, l=64, t=560, w=560))
     + wordmark(210, BLUE, l=M, b=M) + cta('Read more', BLUE, 26, r=M, b=78))

post('sq-stat', 'Big number', BLUE,
     emblem(900, VEIL, r=-240, b=-150, name='X watermark')
     + lbl('BY THE NUMBERS', ACC, 22, l=M, t=M) + emblem(60, ACC, r=M, t=M)
     + T('Stat', '15M+', 'num', WHITE, 300, l=M - 14, t=230)
     + st('Statement', 'Devices deployed globally.', WHITE, 54, l=M, t=560, w=900)
     + body('Handhelds, tablets, wearables and IoT, designed in the USA and certified worldwide.', GRAY, 26, l=M, t=640, w=720)
     + wordmark(210, GRAY, l=M, b=M) + T('Source', 'Source: nexamobility.com', 'small', GRAY, 16, r=M, b=80))

post('sq-news', 'News · Rebrand', BLACK,
     lbl('NEWS', ACC, 22, l=M, t=M)
     + hl('Headline', 'SOCIAL MOBILE\nIS NOW', WHITE, 100, l=M, t=210)
     + chevron(150, ACC, 'open', l=M, t=470) + wordmark(560, WHITE, l=200, t=492, tm=True) + chevron(150, ACC, 'close', l=800, t=470)
     + body('Fourteen years in, one focus: enterprise mobility. Same team, new name.', GRAY, 28, l=M, t=720, w=780)
     + T('URL', 'nexamobility.com', 'sh3', WHITE, 22, l=M, b=M))

post('sq-product', 'Product · Rugged device', TINT,
     emblem(760, WHITE, l=420, t=220, name='X watermark')
     + lbl('RUGGED · MISSION-CRITICAL', BLUE, 22, l=M, t=M)
     + hl('Headline', 'BUILT TO\nTAKE THE\nHIT', BLUE, 96, l=M, t=150)
     + body('Sonim, a NEXA company: rugged phones and accessories for first responders and the field.', BLACK, 25, l=M, t=500, w=420)
     + chamfer('Product frame', 580, 120, 428, 820, c=100, stroke=BLACK, sw=3)
     + f'<img class="abs cutout" data-name="Product" data-img="pr-xp5" alt="Product" style="left:612px;top:170px;width:364px;height:720px;object-fit:contain">'
     + wordmark(210, BLUE, l=M, b=M))

post('sq-quote', 'Customer quote', WHITE,
     watermark(640, r=-120, b=-120)
     + chamfer('Portrait', M, M, 300, 300, c=60, photo_key='ph-firefighter', align='xMidYMid')
     + T('Quote mark', '“', 'hl', BLUE, 220, l=860, t=40)
     + st('Quote', 'When the call comes in, the device can’t be the thing that fails.', BLACK, 58, l=M, t=430, w=900)
     + T('Name', 'Name Surname', 'sh3', BLUE, 26, l=M, t=720) + body('Role · Customer organisation', BLACK, 22, l=M, t=756)
     + wordmark(210, BLUE, l=M, b=M))

post('sq-tips', 'Checklist', BLUE,
     emblem(700, VEIL, r=-220, t=-120, name='X watermark')
     + lbl('CHECKLIST', ACC, 22, l=M, t=M)
     + hl('Headline', '3 SIGNS YOU’VE\nOUTGROWN\nCONSUMER DEVICES', WHITE, 72, l=M, t=140)
     + bullets([('IT images every phone by hand.', ''), ('Devices go end-of-life before your contract does.', ''), ('Cases, chargers and docks never match.', '')],
               WHITE, GRAY, 36, M, 480, 900, gap=34)
     + wordmark(210, GRAY, l=M, b=M))

post('sq-poll', 'Poll / question', TINT,
     lbl('QUICK POLL', BLUE, 22, l=M, t=M)
     + hl('Headline', 'WHAT’S NEXT\nFOR YOUR FLEET?', BLUE, 84, l=M, t=140)
     + ''.join(chamfer(f'Option {k}', M, 380 + i * 112, 936, 88, c=24, fill=WHITE, slab=None, inner=
                       T('Letter', k, 'hl', BLUE, 30, l=40, t=27) + T('Option', o, 'sh2', BLACK, 30, l=96, t=26))
               for i, (k, o) in enumerate(zip('ABCD', ['Rugged handhelds', 'Custom tablets', 'Wearables', 'IoT gateways'])))
     + wordmark(210, BLUE, l=M, b=M) + body('Vote in the comments', BLACK, 22, r=M, b=78))

post('sq-hiring', 'Careers · We’re hiring', BLACK,
     chamfer('Photo container', M, M, 936, 520, c=110, photo_key='ph-team', align='xMidYMid')
     + lbl('CAREERS', ACC, 22, l=M, t=650)
     + hl('Headline', 'WE’RE HIRING', WHITE, 96, l=M, t=694)
     + body('Engineering · Product · Sales · Hollywood, Florida', GRAY, 26, l=M, t=812)
     + wordmark(210, BLUE, l=M, b=M) + cta('See open roles', ACC, 24, r=M, b=76))

post('sq-event', 'Event · Booth', BLUE,
     photo('Brand light', 'tex-ribbon', 0, 0, S, S, '72% 50%')
     + rail(S - 2 * M, ACC, ['NEXA', 'Event', YEAR], M, 52, 16)
     + lbl('MEET US AT', ACC, 24, l=M, t=190)
     + hl('Headline', 'BOOTH\n1204', WHITE, 130, l=M, t=236)
     + chamfer('Details', M, 610, 600, 210, c=46, stroke=WHITE, sw=3, slab=ACC, slab_w=40, inner=
               st('Event', 'Event Name 2026', WHITE, 40, l=48, t=52) + body('12–14 November · City, State', ACC, 26, l=48, t=112))
     + wordmark(210, GRAY, l=M, b=M))

post('sq-webinar', 'Webinar · Speaker', WHITE,
     watermark(820, r=-240, t=-100)
     + lbl('LIVE WEBINAR', BLUE, 22, l=M, t=M)
     + hl('Headline', 'SCALING\nPRIVATE-LABEL\nMOBILITY', BLACK, 82, l=M, t=140)
     + chamfer('Speaker', M, 520, 300, 360, c=60, photo_key='ph-dispatcher', align='xMidYMid')
     + st('Speaker name', 'Speaker Name', BLACK, 36, l=410, t=540) + body('Role, NEXA', BLACK, 24, l=410, t=588)
     + chamfer('Date chip', 410, 680, 560, 100, c=28, fill=BLUE, slab=GRAY, slab_w=24, inner=
               T('Date', 'Thu 15 Oct · 11:00 ET', 'sh3', WHITE, 30, l=44, t=32))
     + wordmark(210, BLUE, r=M, b=M))

post('sq-xwindow', 'X window', TINT,
     rail(S - 2 * M, BLUE, ['NEXA', 'Emergency medical services', YEAR], M, 52, 16)
     + xwindow('X window', 'ph-paramedics', 110, 130, 860, 'xMidYMid', 1.15)
     + hl('Headline', 'CARE THAT\nMOVES WITH YOU', BLUE, 72, l=M, t=790, w=760)
     + wordmark(210, BLUE, r=M, b=M))

post('sq-brackets', 'Brackets', BLACK,
     lbl('FIELD READY', ACC, 22, l=M, t=M)
     + photo('Photo', 'ph-heli', M, 120, S - 2 * M, 700, '50% 60%')
     + chevron(150, ACC, 'open', l=M - 54, t=395) + chevron(150, ACC, 'close', r=M - 54, t=395)
     + hl('Headline', 'READY WHEN IT MATTERS', WHITE, 56, l=M, t=870)
     + wordmark(210, BLUE, r=M, b=M))

post('sq-split', 'Industry × Mobility · Split', BLUE,
     photo('Industry photo', 'ph-rescue', 0, 0, S / 2, S, '45% 50%')
     + emblem(560, VEIL, l=640, t=260, name='X watermark')
     + hl('Industry', 'PUBLIC\nSAFETY', WHITE, 72, l=612, t=300) + emblem(96, ACC, l=612, t=470) + hl('Mobility', 'MOBILITY', WHITE, 72, l=612, t=600)
     + wordmark(210, GRAY, r=M, b=M))

post('sq-brandlight', 'Brand light · Split (Super Blue grade)', BLACK,
     photo('Industry photo', 'phb-crowd', 0, 0, S / 2, S, '50% 50%') + photo('Brand light', 'tex-fiber', S / 2, 0, S / 2, S, '72% 40%')
     + wordmark(700, WHITE, l=190, t=430) + lockup('Retail', 30, WHITE, l=310, t=920))

# ============================================================== PORTRAIT 4:5 + CAROUSEL 1080 x 1350
PW, PH = 1080, 1350
def portrait(aid, name, bg, inner, use):
    F.append(('portrait', artboard(aid, name, PW, PH, bg, inner, use, 'post')))

portrait('cr-cover', 'Carousel 1/4 · Cover', BLUE,
         emblem(1100, VEIL, r=-420, t=320, name='X watermark')
         + lbl('GUIDE', ACC, 22, l=M, t=M) + T('Page', '01 / 04', 'lbl', ACC, 22, r=M, t=M)
         + hl('Headline', '3 QUESTIONS\nTO ASK BEFORE\nA PRIVATE-LABEL\nROLLOUT', WHITE, 96, l=M, t=250)
         + body('A short guide for IT and operations leaders.', GRAY, 30, l=M, t=720, w=700)
         + cta('Swipe', ACC, 30, r=M, b=M)
         + wordmark(210, GRAY, l=M, b=M), 'Instagram / LinkedIn carousel')

portrait('cr-inner-1', 'Carousel 2/4 · Point', WHITE,
         rail(PW - 2 * M, BLUE, ['NEXA', 'Private-label guide', '02 / 04'], M, 56, 16)
         + T('Number', '01', 'num', BLUE, 280, l=M - 12, t=150)
         + st('Question', 'Who owns the device roadmap?', BLACK, 64, l=M, t=480, w=900)
         + body('Consumer models change every year. A private-label roadmap is set with you, so the device you certify is the device you can still buy in year five.', BLACK, 30, l=M, t=640, w=880)
         + chamfer('Tip', M, 950, 936, 260, c=56, fill=TINT, slab=GRAY, inner=
                   lbl('TIP', BLUE, 20, l=56, t=60) + body('Ask for a written lifecycle commitment and a last-time-buy window.', BLACK, 28, l=56, t=104, w=780)),
         'Instagram / LinkedIn carousel')

portrait('cr-inner-2', 'Carousel 3/4 · Point with photo', WHITE,
         rail(PW - 2 * M, BLUE, ['NEXA', 'Private-label guide', '03 / 04'], M, 56, 16)
         + chamfer('Photo container', M, 120, 936, 620, c=110, photo_key='ph-firefighter', align='xMidYMid')
         + T('Number', '02', 'num', BLUE, 150, l=M - 8, t=800)
         + st('Question', 'Will it survive a real shift?', BLACK, 56, l=330, t=812, w=680)
         + body('Drops, heat, gloves, rain. Test in the field with the people who will carry it, not on a desk.', BLACK, 28, l=330, t=960, w=680),
         'Instagram / LinkedIn carousel')

portrait('cr-end', 'Carousel 4/4 · Call to action', BLUE,
         emblem(64, ACC, r=M, t=M)
         + hl('Headline', 'READY FOR\nWHAT’S\nNEXT?', WHITE, 120, l=M, t=260)
         + body('Talk to the team that has deployed more than 15 million enterprise devices.', GRAY, 30, l=M, t=700, w=760)
         + chamfer('Button', M, 880, 620, 110, c=30, fill=ACC, slab=None, inner=T('URL', 'nexamobility.com', 'sh3', BLUE, 36, l=48, t=33))
         + wordmark(210, GRAY, l=M, b=M), 'Instagram / LinkedIn carousel')

portrait('pt-case', 'Portrait · Case study', WHITE,
         photo('Photo', 'ph-paramedics', 0, 0, PW, 860, '50% 45%')
         + chamfer('Text panel', M, 700, 936, 580, c=110, fill=WHITE, inner=
                   lbl('CASE STUDY', BLUE, 22, l=64, t=130)
                   + st('Statement', 'How an EMS fleet moved to one device, one console and one partner.', BLACK, 50, l=64, t=176, w=820)
                   + wordmark(210, BLUE, l=64, t=470)),
         'Instagram / LinkedIn portrait')

portrait('pt-product', 'Portrait · Product', BLACK,
         lbl('SONIM · A NEXA COMPANY', ACC, 22, l=M, t=M)
         + hl('Headline', 'RUGGED\nBY DESIGN', WHITE, 110, l=M, t=140)
         + chevron(220, ACC, 'open', l=150, t=720) + chevron(220, ACC, 'close', l=772, t=720)
         + f'<img class="abs cutout" data-name="Product" data-img="pr-xp5" alt="Product" style="left:340px;top:460px;width:400px;height:760px;object-fit:contain">'
         + wordmark(210, BLUE, l=M, b=M), 'Instagram / LinkedIn portrait')

# ============================================================== STORIES 1080 x 1920 (safe: top 250, bottom 340)
SW, SH = 1080, 1920
def story(aid, name, bg, inner):
    F.append(('stories', artboard(aid, name, SW, SH, bg, inner, 'Instagram / Facebook / LinkedIn story', 'story')))

story('st-spot', 'Story · Industry spotlight', WHITE,
      watermark(1100, r=-420, t=250)
      + lbl('HEALTHCARE', BLUE, 26, l=M, t=280)
      + hl('Headline', 'CARE,\nCONNECTED', BLACK, 130, l=M, t=330)
      + chamfer('Photo container', M, 680, 936, 760, c=150, photo_key='ph-clinician', align='xMidYMid')
      + wordmark(260, BLUE, l=M, t=1500))

story('st-stat', 'Story · Big number', BLUE,
      emblem(1300, VEIL, r=-500, t=500, name='X watermark')
      + lbl('BY THE NUMBERS', ACC, 26, l=M, t=280)
      + T('Stat', '15M+', 'num', WHITE, 330, l=M - 16, t=520)
      + st('Statement', 'Devices deployed\nglobally.', WHITE, 72, l=M, t=900)
      + body('Designed in the USA. Certified worldwide.', GRAY, 34, l=M, t=1090)
      + wordmark(260, GRAY, l=M, t=1500) + emblem(76, ACC, r=M, t=1490))

story('st-event', 'Story · Event countdown', BLACK,
      photo('Brand light', 'tex-tunnel', 0, 0, SW, 900)
      + lbl('SEE YOU THERE', ACC, 26, l=M, t=280)
      + hl('Headline', 'THREE DAYS\nTO GO', WHITE, 120, l=M, t=960)
      + chamfer('Details', M, 1230, 936, 200, c=46, stroke=WHITE, sw=3, slab=ACC, slab_w=40, inner=
                st('Event', 'Event Name · Booth 1204', WHITE, 40, l=48, t=48) + body('12–14 November · City, State', ACC, 28, l=48, t=112))
      + wordmark(260, BLUE, l=M, t=1500))

story('st-announce', 'Story · Announcement', BLUE,
      photo('Brand light', 'tex-ribbon', 0, 0, SW, SH, '70% 50%')
      + rail(SW - 2 * M, ACC, ['NEXA', 'Announcement', YEAR], M, 280, 16)
      + hl('Headline', 'WHAT’S\nNEXT IS\nHERE', WHITE, 150, l=M, t=360)
      + body('The next generation enterprise starts with one connected partner.', WHITE, 40, l=M, t=900, w=720)
      + cta('Learn more', ACC, 36, l=M, t=1140)
      + wordmark(300, GRAY, l=M, t=1480))

# ============================================================== LINKEDIN & X 1200 x 627, banner 1584 x 396
LW, LH, LM = 1200, 627, 56
def land(aid, name, bg, inner, w=LW, h=LH, use='LinkedIn / X feed image'):
    F.append(('linkedin', artboard(aid, name, w, h, bg, inner, use, 'land')))

land('li-spot', 'LinkedIn · Spotlight', WHITE,
     watermark(560, l=-120, b=-160)
     + lbl('TRANSPORT & LOGISTICS', BLUE, 18, l=LM, t=LM)
     + st('Statement', 'Every route, every driver, one fleet.', BLACK, 54, l=LM, t=110, w=520)
     + body('Purpose-built tablets and handhelds for fleet management and ELD compliance.', BLACK, 21, l=LM, t=330, w=460)
     + chamfer('Photo container', 640, LM, 504, 515, c=90, photo_key='ph-driver', align='xMidYMid')
     + wordmark(200, BLUE, l=LM, b=LM))

land('li-insight', 'LinkedIn · Insight', BLUE,
     emblem(620, VEIL, r=-160, t=-60, name='X watermark')
     + chevron(160, ACC, 'open', l=LM, t=150) + chevron(160, ACC, 'close', r=LM, t=150)
     + st('Statement', 'Consumer phones were never built to be managed by the thousand.', WHITE, 48, l=220, t=150, w=760)
     + wordmark(200, GRAY, l=LM, b=LM) + cta('Read the insight', ACC, 22, r=LM, b=LM + 4))

land('li-news', 'LinkedIn · News', BLACK,
     lbl('NEWS', ACC, 18, l=LM, t=LM)
     + hl('Headline', 'SOCIAL MOBILE IS NOW', WHITE, 60, l=LM, t=150)
     + chevron(120, ACC, 'open', l=LM, t=270) + wordmark(460, WHITE, l=170, t=290) + chevron(120, ACC, 'close', l=660, t=270)
     + body('Same team, new name, one focus: enterprise mobility.', GRAY, 22, l=LM, t=450)
     + T('URL', 'nexamobility.com', 'sh3', WHITE, 18, l=LM, b=LM))

land('li-hiring', 'LinkedIn · Hiring', WHITE,
     chamfer('Photo container', LM, LM, 540, 515, c=90, photo_key='ph-team', align='xMidYMid')
     + lbl('CAREERS', BLUE, 18, l=660, t=LM)
     + hl('Headline', 'WE’RE\nHIRING', BLACK, 76, l=660, t=100)
     + body('Engineering · Product · Sales\nHollywood, Florida', BLACK, 22, l=660, t=290)
     + cta('See open roles', BLUE, 22, l=660, t=390)
     + wordmark(200, BLUE, l=660, b=LM))

land('li-event', 'LinkedIn · Event', BLACK,
     photo('Brand light', 'tex-tunnel', 600, 0, 600, LH)
     + chevron(90, ACC, 'open', l=570, t=268)
     + rail(LW - 2 * LM, GRAY, ['NEXA', 'Event', YEAR], LM, 30, 13)
     + lbl('MEET US AT', ACC, 18, l=LM, t=120)
     + hl('Headline', 'RETAIL\nTECH EXPO', WHITE, 72, l=LM, t=150)
     + body('Booth 1204 · 12–14 November', WHITE, 22, l=LM, t=330)
     + lockup('Retail', 18, WHITE, l=LM, t=400)
     + wordmark(200, BLUE, l=LM, b=LM))

land('li-banner', 'LinkedIn · Company banner', BLUE,
     photo('Brand light', 'tex-ribbon', 700, 0, 884, 396, '60% 50%')
     + emblem(420, VEIL, l=300, t=-40, name='X watermark')
     + hl('Headline', 'NEXT GENERATION\nENTERPRISE MOBILITY', WHITE, 50, l=560, t=120)
     + T('URL', 'nexamobility.com', 'sh3', ACC, 20, l=560, t=260),
     w=1584, h=396, use='LinkedIn company page cover (keep the left third clear for the logo)')

# ============================================================== PRESENTATION 1920 x 1080
D, DH, DM = 1920, 1080, 64
def slide(aid, name, bg, inner, use):
    F.append(('slides', artboard(aid, name, D, DH, bg, inner, use, 'slide')))

slide('sl-cover', 'Slide · Cover', WHITE,
      watermark(1100, l=-260, t=260)
      + rail(D - 2 * DM, BLACK, ['NEXA', 'Presentation title', YEAR], DM, 40, 16)
      + lbl('ENTERPRISE MOBILITY', BLUE, 26, l=DM, t=260)
      + hl('Headline', 'PRESENTATION\nTITLE GOES\nHERE', BLACK, 120, l=DM, t=310)
      + body('Subtitle or presenter name · Month 2026', BLACK, 28, l=DM, t=720)
      + chamfer('Photo container', 1060, 120, 796, 840, c=150, photo_key='ph-crew', align='xMidYMid')
      + wordmark(260, BLUE, l=DM, b=DM), 'Title slide')

slide('sl-section', 'Slide · Section divider', BLUE,
      emblem(1200, VEIL, r=-300, t=-100, name='X watermark')
      + rail(D - 2 * DM, ACC, ['NEXA', 'Section', YEAR], DM, 40, 16)
      + T('Index', '02', 'num', GRAY, 360, l=DM - 16, t=110)
      + hl('Headline', 'OUR\nPLATFORM', WHITE, 120, l=DM, t=770)
      + body('Section intro. One or two sentences that set up what follows, set in Roboto Regular.', WHITE, 24, l=1180, t=820, w=620), 'Section divider')

slide('sl-content', 'Slide · Content + image', WHITE,
      rail(D - 2 * DM, BLACK, ['NEXA', 'Presentation title', '03'], DM, 40, 16)
      + lbl('WHAT WE DO', BLUE, 26, l=DM, t=140)
      + hl('Headline', 'ONE PARTNER,\nEVERY DEVICE', BLACK, 88, l=DM, t=190)
      + T('Sub-header 2', 'From design to recycling, managed as one.', 'sh2', BLACK, 36, l=DM, t=410, w=800)
      + bullets([('Design', 'Private-label hardware, software and packaging.'), ('Deploy', 'Kitted, configured and delivered ready to work.'), ('Support', 'Repair, replace and recycle with one call.')],
                BLACK, BLACK, 30, DM, 540, 780, gap=30, acolor=BLUE)
      + chamfer('Photo container', 1000, 140, 856, 800, c=140, photo_key='ph-dispatcher', align='xMidYMid')
      + emblem(56, BLUE, l=DM, b=48), 'Content slide')

slide('sl-stats', 'Slide · Stats', BLACK,
      rail(D - 2 * DM, GRAY, ['NEXA', 'Presentation title', '04'], DM, 40, 16)
      + hl('Headline', 'AT A GLANCE', WHITE, 88, l=DM, t=140)
      + ''.join(box('Stat', l=DM + i * 610, t=420, w=570, cls='stack', style={'gap': '18px'}, inner=
                    line('Rule', GRAY, 0, 0, 570) + text('Number', n, 'num', WHITE, 180, {'margin-top': '30px'}) + text('Label', lb, 'lbl', ACC, 26) + text('Detail', dt, 'body', GRAY, 20, {'max-width': '480px'}))
                for i, (n, lb, dt) in enumerate([('15M+', 'DEVICES DEPLOYED', 'Handhelds, tablets, wearables and IoT worldwide.'), ('2011', 'FOUNDED', 'As Social Mobile. NEXA since 2025.'), ('USA', 'DESIGNED IN', 'Globally certified, built for long deployments.')]))
      + T('Source', 'Source: nexamobility.com', 'small', GRAY, 14, r=DM, b=48)
      + emblem(56, ACC, l=DM, b=48), 'Data slide')

slide('sl-close', 'Slide · Closing', BLACK,
      wordmark(1100, BLUE, l=(D - 1100) // 2, t=(DH - round(1100 * WM['h'] / WM['w'])) // 2)
      + rail(D - 2 * DM, GRAY, ['NEXA', 'nexamobility.com', YEAR], DM, DH - 60, 16), 'End slide')

# ============================================================== WEB & EMAIL
def web(aid, name, w, h, bg, inner, use):
    F.append(('web', artboard(aid, name, w, h, bg, inner, use, 'web')))

web('wb-hero', 'Web · Hero', 1440, 720, WHITE,
    watermark(760, r=-140, b=-220)
    + wordmark(200, BLUE, l=64, t=40)
    + box('Nav', r=64, t=48, cls='row', style={'gap': '40px'}, inner=''.join(text('Link', t_, 'sh2', BLACK, 17) for t_ in ['Solutions', 'Industries', 'Why NEXA', 'News', 'Contact']))
    + lbl('ENTERPRISE MOBILITY', BLUE, 18, l=64, t=190)
    + hl('Headline', 'THE NEXT\nGENERATION\nENTERPRISE', BLACK, 88, l=64, t=230)
    + body('Private-label devices, software and services, designed in the USA and deployed at scale.', BLACK, 22, l=64, t=530, w=560)
    + chamfer('Button', 64, 610, 260, 64, c=18, fill=BLUE, slab=None, inner=T('Label', 'Talk to us', 'sh3', WHITE, 18, l=34, t=21))
    + chamfer('Photo container', 760, 150, 616, 520, c=100, photo_key='ph-command', align='xMidYMid'),
    'Website hero')

web('wb-email', 'Email · Header', 1200, 400, BLUE,
    photo('Brand light', 'tex-ribbon', 640, 0, 560, 400, '70% 50%')
    + wordmark(200, GRAY, l=48, t=48)
    + hl('Headline', 'WHAT’S NEXT\nIN MOBILITY', WHITE, 60, l=48, t=150)
    + T('Sub-header', 'The NEXA newsletter · October', 'sh2', ACC, 22, l=48, t=310), 'Newsletter header')

web('wb-signature', 'Email · Signature', 600, 160, WHITE,
    emblem(64, BLUE, l=24, t=36) + line('Divider', GRAY, 112, 24, 1, 112)
    + T('Name', 'FIRST LAST', 'hl', BLACK, 24, l=132, t=26)
    + T('Title', 'Job Title · Department', 'sh2', BLUE, 15, l=132, t=60)
    + T('Contact', '+1 000 000 0000 · name@nexamobility.com · nexamobility.com', 'small', BLACK, 13, l=132, t=96), 'Email signature')

# ============================================================== STATIONERY
def pr(aid, name, w, h, bg, inner, use, fmt='print'):
    F.append(('print', artboard(aid, name, w, h, bg, inner, use, fmt)))

pr('pr-card-front', 'Business card · Front', 1050, 600, BLACK, wordmark(820, BLUE, l=64, b=64) + emblem(60, ACC, r=64, t=64), '3.5 × 2 in at 300 ppi')
pr('pr-card-back', 'Business card · Back', 1050, 600, GRAY,
   T('Name', 'FIRST LAST', 'hl', BLUE, 44, l=64, t=64) + T('Title', 'Job Title', 'sh2', BLUE, 26, l=64, t=124)
   + stack('Contact', [text('Line', t_, 'small', BLUE, 20) for t_ in ['Mobile  +1 (000) 000 0000', 'Email  name@nexamobility.com', 'Address  Street, City, ST 00000', 'Web  nexamobility.com']], l=64, b=64, gap=8)
   + emblem(60, BLUE, r=64, b=64), '3.5 × 2 in at 300 ppi')
pr('pr-letterhead', 'Letterhead', 816, 1056, WHITE,
   fill('Edge', BLUE, l=0, t=0, w=10, h=1056)
   + wordmark(200, PURPLE, l=64, t=56) + T('Department', 'ENGINEERING', 'sh1', PURPLE, 13, r=64, t=70)
   + stack('Addressee', [text('To', 'To', 'small', BLACK, 11), text('Name', 'Recipient Name', 'sh3', BLACK, 14), text('Address', 'Street, City, Postcode', 'small', BLACK, 11)], l=64, t=170, gap=4)
   + T('Date', 'Date · 30 September 2026', 'small', BLACK, 11, r=64, t=170)
   + stack('Letter', [text('Salutation', 'Dear Name,', 'sh3', BLACK, 13)] + [text('Paragraph', LOREM + ' ' + LOREM, 'body', BLACK, 12) for _ in range(3)], l=64, t=290, w=560, gap=14)
   + stack('Sign-off', [text('Name', 'Sender Name', 'sh3', BLACK, 13), text('Role', 'Job Title', 'small', BLACK, 11)], l=64, t=700, gap=4)
   + line('Rule', GRAY, 64, 960, 688)
   + T('Footer', 'NEXA · Street, City, ST 00000 · +1 000 000 0000 · nexamobility.com', 'small', BLACK, 10, l=64, t=978)
   + emblem(28, BLUE, r=64, t=974), 'US Letter', 'doc')

SECTION_META = [
    ('square', 'Social · Square posts', 'Seventeen 1080 × 1080 posts for Instagram, LinkedIn and Facebook: industry spotlights, insights, numbers, news, product, quotes, polls, careers and events.'),
    ('portrait', 'Social · Carousels & portrait', '4:5 posts (1080 × 1350) take the most room in the feed. A four-slide carousel plus two single posts.'),
    ('stories', 'Social · Stories', 'Vertical 9:16. Keep type out of the top 250 px and bottom 340 px (turn on Guides).'),
    ('linkedin', 'LinkedIn & X', '1200 × 627 feed images and the 1584 × 396 company banner.'),
    ('slides', 'Presentation', '16:9 slides: cover, section divider, content, data and close.'),
    ('web', 'Web & email', 'Website hero, newsletter header and email signature.'),
    ('print', 'Stationery', 'Business cards and letterhead.'),
]
