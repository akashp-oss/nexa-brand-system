"""Presentation template (16:9, 1920 x 1080), rebuilt from NEXA's strategy decks and aligned to the brandbook:
headlines in N27 uppercase (the decks used Roboto Bold), Roboto Light for body, frosted cut-corner cards,
the right-hand wordmark rail, confidential footer, Midnight/Electric light grounds, photo panels."""
from gen import *

F = []
D, DH = 1920, 1080
L0, RAIL = 110, 200
RULE_ = '#D6D6DC'            # content left edge; right rail width
CW = D - L0 - RAIL - 40         # content width
FOOT_Y = DH - 44

def T_(name, content, cls, color, size, **k): return T(name, content, cls, color, size, **k)
def hl(n, c, col, s, **k): return T(n, c, 'hl', col, s, **k)
def lt(n, c, col, s, **k): return T(n, c, 'lt', col, s, **k)
def st(n, c, col, s, **k): return T(n, c, 'st', col, s, **k)
def kicker(c, col, **k): return T('Kicker', c, 'lbl', col, 22, **k)

def rail(color, line_col=None, top=60):
    """Right rail: hairline, vertical wordmark, hairline (NEXA deck furniture)."""
    x = D - RAIL + 40; wl = 300; lc = line_col or color
    wt = (DH - wl) // 2
    return (line('Rail line', lc, x + 20, top, 1.5, wt - top - 40) + vwordmark(wl, color, l=x, t=wt)
            + line('Rail line', lc, x + 20, wt + wl + 40, 1.5, DH - (wt + wl + 40) - 60))

def footer(color, l=L0):
    return T('Confidential', CONFIDENTIAL, 'small', color, 11, l=l, t=FOOT_Y, w=D - RAIL - 140 - l, extra={'opacity': '.75'})

def page(n, color):
    return T('Page', f'{n:02d}', 'n27', color, 18, r=RAIL + 40, t=FOOT_Y - 6)

def dark(key='tex-aurora-a', pos='50% 50%'):
    """Light ground; the bright aurora frames get a Midnight veil so type keeps its contrast."""
    veil = fill('Midnight veil', 'rgba(0,19,58,.42)', l=0, t=0, w=D, h=DH) if 'aurora' in key else ''
    return photo('Background', key, 0, 0, D, DH, pos) + veil

def slide(aid, name, bg_, inner, use):
    F.append(('slides', artboard(aid, name, D, DH, bg_, inner, use, 'slide')))

def dot_list(items, color, size, l, t, w, gap=10):
    rows = ''.join(f'<div class="row" data-name="Item" style="gap:12px;align-items:flex-start">'
                   f'<div data-name="Dot" style="width:5px;height:5px;margin-top:{round(size*.55)}px;background:{color};flex:none"></div>'
                   f'{text("Item", it, "lt", color, size)}</div>' for it in items)
    return box('List', l=l, t=t, w=w, cls='stack', style={'gap': px(gap)}, inner=rows)

# ---------------------------------------------------------------- 01 cover A: X of light
slide('dk-cover', 'Deck · Cover (X of light)', MIDNIGHT,
      dark('tex-xlight', '85% 50%') + wordmark(260, WHITE, l=L0, t=90)
      + kicker('STRATEGY 2026', ACC, l=L0, t=380)
      + hl('Title', 'PRESENTATION\nTITLE GOES HERE', WHITE, 110, l=L0, t=420)
      + lt('Subtitle', 'Subtitle or presenter name  ·  Month 2026', WHITE, 34, l=L0, t=680)
      + footer(WHITE), 'Title slide')

# ---------------------------------------------------------------- 02 cover B: photo container
slide('dk-cover-photo', 'Deck · Cover (photo)', WHITE,
      chamfer('Photo', 1000, 0, 920, DH, c=190, photo_key='ph-paramedics', align='xMidYMid')
      + wordmark(240, BLUE, l=L0, t=90)
      + kicker('AMERICAN TECHNOLOGY FOR THE FRONT LINE', BLUE, l=L0, t=390)
      + hl('Title', 'CRITICAL\nCOMMUNICATIONS\nROADMAP', BLACK, 80, l=L0, t=430)
      + lt('Subtitle', 'Presenter name  ·  Month 2026', BLACK, 32, l=L0, t=780)
      + footer('#6F6F6F'), 'Title slide')

# ---------------------------------------------------------------- 03 agenda
AG = ['Where we are today', 'Our vision for U.S. critical industries', 'Strategic growth plan', 'Why NEXA', 'Next steps']
slide('dk-agenda', 'Deck · Agenda', MIDNIGHT,
      dark('tex-aurora-a') + rail(WHITE, 'rgba(255,255,255,.5)')
      + hl('Title', 'AGENDA', WHITE, 96, l=L0, t=110)
      + ''.join(line('Rule', 'rgba(255,255,255,.3)', 760, 170 + i * 150, 900, 1.5)
                + T('Number', f'{i+1:02d}', 'n27', WHITE, 30, l=760, t=200 + i * 150)
                + lt('Item', a, WHITE, 46, l=860, t=192 + i * 150) for i, a in enumerate(AG))
      + footer(WHITE) + page(2, WHITE), 'Agenda')

# ---------------------------------------------------------------- 04 section divider
slide('dk-section', 'Deck · Section divider', MIDNIGHT,
      dark('tex-arcs') + rail(WHITE, 'rgba(255,255,255,.5)')
      + T('Index', '03', 'hl', WHITE, 300, l=L0 - 12, t=100)
      + hl('Title', 'STRATEGIC\nGROWTH PLAN', WHITE, 120, l=L0, t=620)
      + footer(WHITE), 'Section divider')

# ---------------------------------------------------------------- 05 four frosted cards
CARDS = [('device', 'Stronger Sonim portfolio', ['Expand rugged devices and PTT; advance Sidelink and carrier / private network compatibility.', 'Grow through carrier and direct enterprise relationships.']),
         ('chip', 'U.S. cellular modules', ['Design and manufacture U.S. modules anchored by NEXA / Sonim demand.', 'Supply OEMs in defense, utilities, energy, mining, healthcare and transport.']),
         ('factory', 'U.S. assembly and manufacturing', ['Assemble Sonim devices, government devices and drone controllers.', 'Offer EMS, testing and secure provisioning.']),
         ('rocket', 'U.S. innovation and lifecycle support', ['Launch the Innovation-to-Deployment Center for customer qualification.', 'Expand U.S. engineering and DM / FOTA.'])]
cw_, ch_ = 360, 560
slide('dk-cards', 'Deck · Four pillars (frosted cards)', MIDNIGHT,
      dark('tex-aurora-b') + rail(WHITE, 'rgba(255,255,255,.5)')
      + hl('Title', 'STRATEGIC GROWTH PLAN', WHITE, 76, l=L0, t=100)
      + lt('Intro', 'NEXA will position itself as the go-to U.S. partner for critical communications and enterprise,\nbringing secure mobile solutions to market.', WHITE, 28, l=L0, t=200, w=1400)
      + ''.join(glass(f'Card {i+1}', L0 + i * (cw_ + 28), 360, cw_, ch_, c=34, solid=('rgba(31,31,204,.9)' if i == 0 else None), inner=
                      T('Number', f'{i+1:02d}', 'n27', WHITE, 20, l=34, t=40) + icon(k, 40, WHITE, t_, r=30, t=30)
                      + st('Card title', t_, WHITE, 32, l=34, t=110, w=290)
                      + line('Rule', 'rgba(255,255,255,.35)', 34, 230, cw_ - 68, 1)
                      + dot_list(bs, WHITE, 19, 34, 256, cw_ - 68, 14))
                for i, (k, t_, bs) in enumerate(CARDS))
      + footer(WHITE) + page(4, WHITE), 'Four-up content')

# ---------------------------------------------------------------- 06 photo + numbered rows
ROWS = [('Power the downstream innovation ecosystem', 'Bring Qualcomm, Google, carriers and software partners together on common platforms.'),
        ('Critical industries and enterprise', 'Aggregate demand across utilities, energy, mining, healthcare and transport.'),
        ('National security and U.S. supply', 'Serve government and defense primes through U.S. engineering and assembly.'),
        ('Day-zero releases for critical comms', 'Align Sonim and partner roadmaps with new Qualcomm and Google platform releases.')]
slide('dk-vision', 'Deck · Photo + numbered rows', MIDNIGHT,
      dark('tex-aurora-c') + photo('Photo', 'ph-heli', 0, 0, 640, DH, '55% 50%')
      + fill('Photo shade', 'linear-gradient(0deg,rgba(0,19,58,.95),rgba(0,19,58,.6) 38%,rgba(0,19,58,0) 62%)', l=0, t=0, w=640, h=DH)
      + hl('Title', 'OUR VISION\nFOR U.S.\nCRITICAL\nINDUSTRIES', WHITE, 64, l=64, t=690)
      + rail(WHITE, 'rgba(255,255,255,.5)')
      + ''.join((line('Rule', 'rgba(255,255,255,.3)', 720, 90 + i * 225, 960, 1.5) if i else '')
                + T('Number', f'{i+1:02d}', 'n27', WHITE, 20, l=720, t=130 + i * 225)
                + st('Row title', a, WHITE, 30, l=790, t=122 + i * 225, w=380)
                + lt('Row text', b, WHITE, 22, l=1220, t=124 + i * 225, w=460) for i, (a, b) in enumerate(ROWS))
      + footer(WHITE, 720) + page(5, WHITE), 'Content with photo')

# ---------------------------------------------------------------- 07 why NEXA: stats + list
WHY = [('Established ecosystem relationships', 'Google, Honeywell and all major telcos.'), ('Private, profitable, long-term vision', 'Free to think strategically and focus on long-term partnerships.'),
       ('Proven enterprise success', 'Global enterprises across retail, travel, healthcare and energy.'), ('U.S. leadership in critical communications', '1M+ devices sold on FirstNet.'),
       ('Government expansion underway', 'A U.S. company with federal and defense experience.')]
slide('dk-why', 'Deck · Stats column + list', MIDNIGHT,
      dark('tex-aurora-a') + chamfer('Photo', 0, 0, 560, DH, c=0, photo_key='ph-team', align='xMidYMid')
      + fill('Photo shade', 'linear-gradient(180deg,rgba(0,19,58,.8),rgba(0,19,58,0) 40%)', l=0, t=0, w=560, h=DH)
      + hl('Title', 'WHY NEXA IS\nTHE RIGHT\nPARTNER', WHITE, 60, l=64, t=90)
      + rail(WHITE, 'rgba(255,255,255,.5)')
      + ''.join(T('Stat', n, 'stat', WHITE, 84, l=640, t=110 + i * 225) + T('Stat label', lb, 'lt', WHITE, 20, l=644, t=196 + i * 225)
                for i, (n, lb) in enumerate([('15M+', 'Devices deployed'), ('100%', 'Client retention*'), ('2011', 'Founded'), ('USA', 'Designed in')]))
      + ''.join((line('Rule', 'rgba(255,255,255,.3)', 960, 100 + i * 180, 720, 1.5) if i else '')
                + T('Number', f'{i+1:02d}', 'n27', WHITE, 18, l=960, t=132 + i * 180)
                + st('Row title', a, WHITE, 26, l=1020, t=126 + i * 180, w=660) + lt('Row text', b, WHITE, 20, l=1020, t=166 + i * 180, w=660) for i, (a, b) in enumerate(WHY))
      + T('Note', '* Replace with sourced figures before use.', 'small', WHITE, 13, l=640, t=FOOT_Y - 30)
      + footer(WHITE, 640) + page(6, WHITE), 'Proof points')

# ---------------------------------------------------------------- 08 statement: photo + blue panel
slide('dk-statement', 'Deck · Statement (photo + panel)', WHITE,
      chamfer('Photo', 0, 0, 760, DH, c=0, photo_key='ph-paramedics', align='xMidYMid')
      + chamfer('Ambition panel', 110, 600, 560, 330, c=56, fill=BLUE, inner=
                lt('Ambition', 'Our ambition is to become the premier U.S. deployment partner for secure connected devices, edge intelligence and domestic modules.', WHITE, 28, l=48, t=70, w=470))
      + hl('Title', 'AMERICAN\nTECHNOLOGY FOR\nTHE FRONT LINE', BLACK, 84, l=880, t=150)
      + st('Subhead', 'Government, first responders, telcos, enterprise and utilities', BLACK, 28, l=880, t=470, w=780)
      + line('Rule', BLACK, 880, 540, 200, 2)
      + lt('Body', 'We are moving forward with our domestic plan, building on an established enterprise business.\n\nWe want to be Qualcomm’s strategic partner for enterprise, critical communications and key segments.', BLACK, 26, l=880, t=580, w=720)
      + rail(BLUE, 'rgba(31,31,204,.4)') + footer('#6F6F6F', 880) + page(7, BLUE), 'Statement')

# ---------------------------------------------------------------- 09 quote
slide('dk-quote', 'Deck · Quote', BLUE,
      emblem(1300, 'rgba(255,255,255,.06)', r=-200, t=-120, name='X watermark')
      + T('Quote mark', '“', 'hl', ACC, 240, l=L0 - 10, t=40)
      + lt('Quote', 'Improve connected care experiences, everyday.', WHITE, 96, l=L0, t=330, w=1300)
      + st('Name', 'Oneview Healthcare', WHITE, 30, l=L0, t=720) + lt('Role', 'Mission statement  ·  NEXA customer', WHITE, 24, l=L0, t=764)
      + rail(WHITE, 'rgba(255,255,255,.5)') + footer(WHITE) + page(8, WHITE), 'Quote')

# ---------------------------------------------------------------- 10 content + image (light)
slide('dk-content', 'Deck · Content + image', WHITE,
      kicker('WHAT WE DO', BLUE, l=L0, t=110)
      + hl('Title', 'ONE PARTNER,\nEVERY DEVICE', BLACK, 90, l=L0, t=150)
      + lt('Intro', 'From design to recycling, managed as one.', BLACK, 36, l=L0, t=380)
      + chev_list(['Custom devices: smartphones, tablets, wearables, kiosks', 'Rhino Mobility: enterprise-grade devices, ready to ship', 'Managed services: staging, kitting, repair, recycling', 'Wireless connectivity: 5G and LTE for the whole fleet'], BLACK, 26, L0, 480, 780, gap=20, ccolor=BLUE, cls='lt')
      + chamfer('Photo', 960, 110, 720, 820, c=120, photo_key='ph-dispatcher', align='xMidYMid')
      + rail(BLUE, 'rgba(31,31,204,.4)') + footer('#6F6F6F') + page(9, BLUE), 'Content slide')

# ---------------------------------------------------------------- 11 two columns: comparison
LEFT = ['Consumer models change every year', 'Imaged and managed by hand', 'Accessories rarely match', 'End-of-life before the contract ends']
RIGHT = ['Roadmap set with you, available up to 5 years', 'Staged, kitted and enrolled before it ships', 'Cases, docks and chargers designed together', 'Repair, replace and recycle with one call']
slide('dk-compare', 'Deck · Comparison', WHITE,
      hl('Title', 'CONSUMER DEVICES VS\nA NEXA PROGRAM', BLACK, 72, l=L0, t=100)
      + chamfer('Left card', L0, 360, 760, 480, c=60, fill='#F1F1F3', inner=
                T('Label', 'OFF THE SHELF', 'lbl', '#6F6F6F', 22, l=56, t=60) + chev_list(LEFT, BLACK, 30, 56, 130, 640, gap=40, ccolor='#9A9A9A', cls='lt'))
      + chamfer('Right card', L0 + 800, 360, 760, 480, c=60, fill=BLUE, inner=
                T('Label', 'WITH NEXA', 'lbl', ACC, 22, l=56, t=60) + chev_list(RIGHT, WHITE, 30, 56, 130, 640, gap=40, ccolor=ACC, cls='lt'))
      + rail(BLUE, 'rgba(31,31,204,.4)') + footer('#6F6F6F') + page(10, BLUE), 'Comparison')

# ---------------------------------------------------------------- 12 timeline
TL = [('2011', 'Founded as Social Mobile', 'Custom devices for the enterprise.'), ('YEAR', 'Milestone', 'Short description of the milestone.'),
      ('YEAR', '15M+ devices deployed', 'Across healthcare, retail, logistics and more.'), ('2025', 'Social Mobile becomes NEXA', 'One focus: enterprise mobility.'), ('NEXT', 'U.S. critical industries', 'Modules, assembly and lifecycle support.')]
slide('dk-timeline', 'Deck · Timeline', MIDNIGHT,
      dark('tex-aurora-c') + rail(WHITE, 'rgba(255,255,255,.5)')
      + hl('Title', 'OUR JOURNEY', WHITE, 84, l=L0, t=110)
      + line('Timeline', 'rgba(255,255,255,.45)', L0, 560, 1290, 2)
      + ''.join(fill('Node', ACC if i == len(TL) - 1 else WHITE, l=L0 + i * 318, t=551, w=20, h=20, style={'border-radius': '50%'})
                + T('Year', y, 'hl', ACC if i == len(TL) - 1 else WHITE, 52, l=L0 + i * 318, t=462)
                + st('Milestone', a, WHITE, 25, l=L0 + i * 318, t=610, w=280) + lt('Detail', b, WHITE, 20, l=L0 + i * 318, t=690, w=280)
                for i, (y, a, b) in enumerate(TL))
      + T('Note', 'YEAR = replace with confirmed dates.', 'small', WHITE, 13, l=L0, t=FOOT_Y - 30)
      + footer(WHITE) + page(11, WHITE), 'Timeline')

# ---------------------------------------------------------------- 13 case study slide
slide('dk-case', 'Deck · Case study', WHITE,
      fill('Hero', BLUE, l=0, t=0, w=D, h=420) + photo('Photo', 'ph-clinician', 1180, 0, 740, 420, '55% 40%')
      + fill('Blend', 'rgba(31,31,204,.35)', l=1180, t=0, w=740, h=420)
      + wordmark(200, WHITE, l=L0, t=80) + line('Divider', WHITE, L0 + 236, 70, 2, 70) + partner_slot(220, 60, WHITE, l=L0 + 272, t=76)
      + T('Kicker', 'CASE STUDY', 'sh1', WHITE, 34, l=L0, t=210)
      + st('Title', 'Revolutionizing bedside care with the first\nGoogle-certified patient engagement solution', WHITE, 40, l=L0, t=270, w=1040)
      + ''.join(T('Head', h_, 'hb', BLACK, 28, l=L0 + i * 560, t=490) + lt('Text', tx, BLACK, 22, l=L0 + i * 560, t=540, w=500)
                for i, (h_, tx) in enumerate([('CHALLENGE', 'Ageing Windows bedside terminals were expensive to maintain, hard to scale and insecure.'),
                                               ('SOLUTION', 'A 22" Android modular monitor with MyStay Mobile: 5-year availability, OTA updates, RFID sign-in.'),
                                               ('RESULTS', 'Lower deployment costs, 2K rollouts and 50+ partner integrations.')]))
      + ''.join(line('Rule', RULE_, L0 + i * 560, 740, 500, 1) + stat(n, s, BLUE, 120, l=L0 + i * 560, t=770) + lt('Stat text', d, BLACK, 22, l=L0 + i * 560, t=900, w=460)
                for i, (n, s, d) in enumerate([('50', '%', 'Lower deployment costs'), ('2', 'K', 'Patient-room rollouts'), ('50', '+', 'Partner integrations')]))
      + footer('#6F6F6F') + page(12, BLUE), 'Case study')

# ---------------------------------------------------------------- 14 key highlights (dark)
slide('dk-highlights', 'Deck · Key numbers', MIDNIGHT,
      dark('tex-arcs', '30% 50%') + rail(WHITE, 'rgba(255,255,255,.5)')
      + hl('Title', 'AT A GLANCE', WHITE, 84, l=L0, t=110)
      + ''.join(line('Rule', 'rgba(255,255,255,.45)', L0 + i * 530, 420, 470, 1.5)
                + T('Stat', n, 'stat', WHITE, 150, l=L0 + i * 530, t=460)
                + T('Label', lb, 'lbl', ACC, 22, l=L0 + i * 530, t=620) + lt('Detail', d, WHITE, 22, l=L0 + i * 530, t=660, w=440)
                for i, (n, lb, d) in enumerate([('15M+', 'DEVICES DEPLOYED', 'Handhelds, tablets, wearables and IoT worldwide.'), ('1M+', 'ON FIRSTNET', 'Devices sold for frontline operations.'), ('2011', 'FOUNDED', 'As Social Mobile. NEXA since 2025.')]))
      + footer(WHITE) + page(13, WHITE), 'Data slide')

# ---------------------------------------------------------------- 15 team
slide('dk-team', 'Deck · Team', WHITE,
      hl('Title', 'LEADERSHIP', BLACK, 84, l=L0, t=100)
      + ''.join(chamfer(f'Portrait {i+1}', L0 + i * 400, 300, 360, 440, c=60, photo_key=k, align='xMidYMid')
                + st('Name', 'Name Surname', BLACK, 30, l=L0 + i * 400, t=776) + lt('Role', 'Job title', BLACK, 22, l=L0 + i * 400, t=818)
                for i, k in enumerate(['ph-dispatcher', 'ph-firefighter', 'ph-clinician', 'ph-driver']))
      + rail(BLUE, 'rgba(31,31,204,.4)') + footer('#6F6F6F') + page(14, BLUE), 'Team')

# ---------------------------------------------------------------- 16 closing
slide('dk-close', 'Deck · Closing', MIDNIGHT,
      dark('tex-slab', '72% 50%')
      + hl('Title', 'THANK YOU', WHITE, 130, l=L0, t=300)
      + lt('Sub', 'Let’s build what’s next together.', WHITE, 40, l=L0, t=470)
      + ''.join(icon(k, 32, ACC, k, l=L0, t=620 + i * 60)
                + T('Contact', v, 'n27', WHITE, 26, l=L0 + 56, t=620 + i * 60) for i, (k, v) in enumerate([('mail', 'sales@nexamobility.com'), ('globe', 'nexamobility.com'), ('pin', '2057 Coolidge Street, Hollywood, FL 33020')]))
      + wordmark(300, WHITE, r=RAIL, b=90) + footer(WHITE), 'End slide')

SECTION_META = [('slides', 'Presentation', 'A 16-slide deck from NEXA’s strategy presentations, aligned to the brandbook: N27 headlines, frosted cut-corner cards, the wordmark rail and the confidential footer.')]
