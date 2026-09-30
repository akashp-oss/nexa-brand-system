"""Print and PDF documents (US Letter 816 x 1056 at 96 dpi): case studies, one-pagers, letterheads, stationery.
Built from the NEXA Healthcare One Pager, the Oneview case study, the letterhead and business-card mock-ups, and the
brandbook. Every layout shares one grid: 48 px margins, 12-column feel, N27 uppercase heads, Roboto body."""
from gen import *

F = []
W, H, M = 816, 1056, 48
GREY_T = '#5E5E66'
RULE = '#D6D6DC'
PAPER = '#F5F5F7'

def doc(sec, aid, name, bg_, inner, use):
    F.append((sec, artboard(aid, name, W, H, bg_, inner, use, 'doc')))

def hl(n, c, col, s, **k): return T(n, c, 'hl', col, s, **k)
def lt(n, c, col, s, **k): return T(n, c, 'lt', col, s, **k)
def st(n, c, col, s, **k): return T(n, c, 'st', col, s, **k)
def hb(n, c, col, s, **k): return T(n, c, 'hb', col, s, **k)
def lbl(c, col, s=11, **k): return T('Label', c, 'lbl', col, s, **k)
def sm(n, c, col, s, **k): return T(n, c, 'small', col, s, **k)

def lock(l, t, col, wm=100, ph=30):
    wh = round(wm * WM['h'] / WM['w'])
    return (wordmark(wm, col, l=l, t=t + (ph - wh) / 2) + line('Divider', col, l + wm + 16, t - 4, 1.5, ph + 8)
            + partner_slot(round(wm * 1.05), ph, col, l=l + wm + 34, t=t))

def legal(col, t=H - 30):
    return sm('Legal', '© 2026 NEXA. NEXA, Rhino Mobility and Mambo Mobility are trademarks of MW International Ventures LLC dba NEXA.', col, 7.5, l=M, t=t)

def contact_block(col, l, t, qr=True, qcol=BLACK):
    return ((qr_dots('https://nexamobility.com', 56, qcol, l=l, t=t) if qr else '')
            + T('Contact', 'Sales      sales@nexamobility.com\nWebsite  nexamobility.com\nSupport  support.nexamobility.com', 'small', col, 9.5, l=l + (72 if qr else 0), t=t + 2))

CASE = {
    'title': 'Revolutionizing bedside care with the first Google-certified patient engagement solution',
    'overview': 'Oneview Healthcare, with NEXA, developed the first 22" Google-certified all-in-one patient engagement solution to enhance bedside care and streamline clinical workflows.',
    'challenge': 'Amid nursing shortages and reliance on outdated equipment, Oneview needed to replace legacy Windows bedside terminals that were expensive to maintain, hard to scale and disconnected from today’s digital healthcare ecosystem.',
    'solution': 'Oneview partnered with NEXA to develop a 22" modular monitor integrated with its MyStay Mobile SaaS platform, delivering stronger security and a more engaging patient experience at the bedside.',
    'points': [('Cost-effective hardware', 'A lightweight Android alternative with 5-year availability and over-the-air updates.'),
               ('Enhanced security', 'Biometric and RFID sign-in, Android Enterprise security and remote management.'),
               ('Better patient experience', 'Telehealth, meal ordering, records and entertainment at the bedside.')],
    'stats': [('50', '%', 'Lower deployment costs'), ('2', 'K', 'Patient-room rollouts'), ('50', '+', 'Partner integrations')],
    'conclusion': 'Oneview Healthcare and NEXA have redefined patient care and clinical workflows with a seamless, connected bedside experience.',
}
ABOUT = 'NEXA is the leading provider of enterprise mobility solutions: an IoT design firm building custom devices for the world’s biggest companies, and a validated Android Enterprise Gold partner.'

def stats_row(col, sub, l, t, gap=160, size=46):
    return ''.join(stat(n, s, col, size, l=l + i * gap, t=t) + sm('Stat text', d, sub, 10, l=l + i * gap, t=t + size * .95, w=gap - 20)
                   for i, (n, s, d) in enumerate(CASE['stats']))

# ============================================================== CASE STUDIES
doc('cases', 'cs-classic', 'Case study · Classic (from the Oneview one-pager)', WHITE,
    fill('Hero', BLUE, l=0, t=0, w=520, h=212) + photo('Photo', 'ph-clinician', 520, 0, 296, 212, '60% 50%')
    + lock(32, 34, WHITE, 80, 26) + T('Kicker', 'CASE STUDY', 'sh1', WHITE, 18, l=32, t=84)
    + st('Title', 'Revolutionizing bedside care with the first\nGoogle-certified patient engagement solution', WHITE, 18.5, l=32, t=124, w=470)
    + fill('Side column', PAPER, l=0, t=212, w=292, h=844)
    + hb('Head', 'OVERVIEW', BLACK, 16, l=32, t=240) + lt('Text', CASE['overview'], BLACK, 11, l=32, t=268, w=236)
    + hb('Head', 'KEY HIGHLIGHTS', BLACK, 16, l=32, t=410)
    + ''.join(stat(n, s, BLUE, 40, l=32, t=446 + i * 66) + lt('Detail', d, BLACK, 10.5, l=112, t=458 + i * 66, w=160) for i, (n, s, d) in enumerate(CASE['stats']))
    + hb('Head', 'PARTNERS', BLACK, 16, l=32, t=660) + partner_slot(100, 34, '#9A9A9A', l=32, t=692) + partner_slot(100, 34, '#9A9A9A', l=146, t=692)
    + hb('Head', 'NEXA', BLACK, 16, l=32, t=760) + lt('About', ABOUT, BLACK, 10.5, l=32, t=786, w=236)
    + sm('Link', 'Visit nexamobility.com for more.', BLACK, 10.5, l=32, t=900)
    + hb('Head', 'CHALLENGE', BLACK, 16, l=330, t=240) + lt('Text', CASE['challenge'], BLACK, 11, l=330, t=268, w=450)
    + hb('Head', 'SOLUTION', BLACK, 16, l=330, t=374) + lt('Text', CASE['solution'], BLACK, 11, l=330, t=402, w=450)
    + ''.join(st('Point', a + ':', BLUE, 12, l=330, t=478 + i * 56) + lt('Detail', b_, BLACK, 11, l=330, t=496 + i * 56, w=450) for i, (a, b_) in enumerate(CASE['points']))
    + hb('Head', 'CONCLUSION', BLACK, 16, l=330, t=660) + lt('Text', CASE['conclusion'], BLACK, 11, l=330, t=688, w=210)
    + chamfer('Product photo', 560, 680, 220, 220, c=36, photo_key='ph-dispatcher', align='xMidYMid')
    + wordmark(96, BLUE, r=36, b=36), 'US Letter case study')

doc('cases', 'cs-midnight', 'Case study · Midnight cover', WHITE,
    photo('Background', 'tex-xlight', 0, 0, W, 470, '85% 50%')
    + lock(M, 44, WHITE, 90, 28)
    + lbl('CASE STUDY  ·  HEALTHCARE', ACC, 11, l=M, t=150)
    + hl('Title', 'REVOLUTIONIZING\nBEDSIDE CARE', WHITE, 50, l=M, t=176)
    + lt('Sub', 'The first Google-certified all-in-one patient engagement solution.', WHITE, 17, l=M, t=300, w=420)
    + chamfer('Stats band', M, 400, W - 2 * M, 130, c=28, fill=BLUE, inner=
              ''.join(stat(n, s, WHITE, 52, l=36 + i * 240, t=30) + sm('Stat text', d, WHITE, 10.5, l=36 + i * 240, t=86, w=200) for i, (n, s, d) in enumerate(CASE['stats'])))
    + hb('Head', 'CHALLENGE', BLUE, 15, l=M, t=570) + lt('Text', CASE['challenge'], BLACK, 11, l=M, t=596, w=340)
    + hb('Head', 'SOLUTION', BLUE, 15, l=428, t=570) + lt('Text', CASE['solution'], BLACK, 11, l=428, t=596, w=340)
    + line('Rule', RULE, M, 730, W - 2 * M, 1)
    + ''.join(icon(k, 24, BLUE, a, l=M + i * 244, t=752) + st('Point', a, BLACK, 12.5, l=M + i * 244, t=786, w=220) + lt('Detail', b_, GREY_T, 10.5, l=M + i * 244, t=806, w=220)
              for i, ((a, b_), k) in enumerate(zip(CASE['points'], ['device', 'lock', 'heart'])))
    + line('Rule', RULE, M, 900, W - 2 * M, 1)
    + wordmark(90, BLUE, l=M, t=924) + sm('About', ABOUT, GREY_T, 8.5, l=M, t=950, w=330)
    + contact_block(BLUE, 470, 922) + legal(GREY_T), 'US Letter case study')

doc('cases', 'cs-photo', 'Case study · Photo container', WHITE,
    watermark(560, r=-160, t=-80)
    + lock(M, 44, BLUE, 90, 28)
    + chamfer('Photo', M, 110, 440, 400, c=66, photo_key='ph-paramedics', align='xMidYMid')
    + lbl('CASE STUDY', BLUE, 11, l=520, t=130)
    + hl('Title', 'CARE THAT\nMOVES WITH\nTHE PATIENT', BLACK, 34, l=520, t=154)
    + lt('Sub', 'How a regional EMS fleet moved to one device, one console and one partner.', BLACK, 14, l=520, t=290, w=250)
    + T('Quote mark', '“', 'hl', BLUE, 60, l=520, t=340)
    + lt('Quote', 'Short customer quote that captures the outcome in one or two lines.', BLACK, 14, l=520, t=402, w=250)
    + sm('Attribution', 'Name Surname, Role, Customer', BLUE, 10.5, l=520, t=470)
    + hb('Head', 'THE CHALLENGE', BLACK, 14, l=M, t=548) + lt('Text', 'Describe the customer’s situation, the constraint and why it mattered. Two to four sentences.', BLACK, 11, l=M, t=572, w=330)
    + hb('Head', 'THE SOLUTION', BLACK, 14, l=428, t=548) + lt('Text', 'Describe what NEXA designed, deployed or manages, and how it fits the workflow. Two to four sentences.', BLACK, 11, l=428, t=572, w=330)
    + chev_list(['Custom rugged handheld with PTT', 'Staged, kitted and enrolled before shipping', 'Managed repair and replacement'], BLACK, 11, M, 660, 330, gap=6, ccolor=BLUE, cls='lt')
    + chev_list(['FirstNet-ready connectivity', 'Single console for devices and apps', 'Five-year device availability'], BLACK, 11, 428, 660, 330, gap=6, ccolor=BLUE, cls='lt')
    + fill('Results band', BLUE, l=0, t=780, w=W, h=190)
    + lbl('RESULTS', ACC, 11, l=M, t=806)
    + ''.join(stat(n, s, WHITE, 50, l=M + i * 245, t=834) + sm('Stat text', d, WHITE, 10.5, l=M + i * 245, t=890, w=200)
              for i, (n, s, d) in enumerate([('00', '%', 'Result metric one'), ('00', 'K', 'Result metric two'), ('00', '+', 'Result metric three')]))
    + wordmark(90, BLUE, l=M, t=992) + sm('URL', 'nexamobility.com', BLUE, 10, r=M, t=1000), 'US Letter case study (blank)')

doc('cases', 'cs-sidebar', 'Case study · Super Blue sidebar', WHITE,
    fill('Sidebar', BLUE, l=0, t=0, w=260, h=H)
    + wordmark(110, WHITE, l=36, t=44)
    + lbl('AT A GLANCE', 'rgba(255,255,255,.7)', 11, l=36, t=150)
    + ''.join(stat(n, s, WHITE, 64, l=36, t=184 + i * 150) + lt('Stat text', d, WHITE, 12, l=36, t=256 + i * 150, w=190)
              for i, (n, s, d) in enumerate(CASE['stats']))
    + line('Rule', 'rgba(255,255,255,.4)', 36, 650, 188, 1)
    + lbl('CUSTOMER', 'rgba(255,255,255,.7)', 11, l=36, t=672) + partner_slot(160, 40, WHITE, l=36, t=696)
    + lbl('INDUSTRY', 'rgba(255,255,255,.7)', 11, l=36, t=762) + lt('Industry', 'Healthcare', WHITE, 13, l=36, t=784)
    + lbl('SOLUTION', 'rgba(255,255,255,.7)', 11, l=36, t=820) + lt('Solution', 'Custom 22" Android\nmodular monitor', WHITE, 13, l=36, t=842)
    + sm('URL', 'nexamobility.com', WHITE, 10, l=36, t=1000)
    + lbl('CASE STUDY', BLUE, 11, l=300, t=52)
    + hl('Title', 'FIRST GOOGLE-CERTIFIED\nBEDSIDE SOLUTION', BLACK, 30, l=300, t=80)
    + chamfer('Photo', 300, 220, 468, 250, c=44, photo_key='ph-clinician', align='xMidYMid')
    + hb('Head', 'OVERVIEW', BLACK, 14, l=300, t=500) + lt('Text', CASE['overview'], BLACK, 11, l=300, t=524, w=468)
    + hb('Head', 'CHALLENGE', BLACK, 14, l=300, t=596) + lt('Text', CASE['challenge'], BLACK, 11, l=300, t=620, w=468)
    + hb('Head', 'SOLUTION', BLACK, 14, l=300, t=712) + lt('Text', CASE['solution'], BLACK, 11, l=300, t=736, w=468)
    + chamfer('Conclusion', 300, 828, 468, 140, c=26, fill=PAPER, inner=
              T('Quote mark', '“', 'hl', BLUE, 40, l=24, t=8) + lt('Conclusion', CASE['conclusion'], BLACK, 12.5, l=24, t=60, w=420))
    + sm('Legal', '© 2026 NEXA. All rights reserved.', GREY_T, 7.5, l=300, t=H - 30), 'US Letter case study')

# ============================================================== ONE-PAGERS
USES = ['Clinical trials', 'Remote patient monitoring', 'Chronic care management', 'Telehealth', 'Senior care management',
        'Bedside technology', 'Connected readers', 'Wearables', 'Patient check-in', 'Clinic documentation']
PILLARS = [('device', 'Custom devices', 'Smartphones, tablets, wearables and kiosks, designed and built for you.'),
           ('box', 'Rhino Mobility', 'Enterprise-grade devices, Android Enterprise certified and ready to ship.'),
           ('cycle', 'Managed services', 'Staging, kitting, repair and recycling across the device lifecycle.'),
           ('signal', 'Wireless connectivity', '5G and LTE plans that work for your entire fleet.')]

doc('onepagers', 'op-industry', 'One-pager · Industry (healthcare)', WHITE,
    fill('Hero', BLUE, l=0, t=0, w=W, h=372) + photo('Photo', 'ph-clinician', 500, 0, 316, 372, '70% 50%')
    + fill('Blend', 'rgba(31,31,204,.5)', l=500, t=0, w=316, h=372)
    + wordmark(96, WHITE, l=M, t=36)
    + hl('Headline', 'ENTERPRISE MOBILITY\nFOR HEALTHCARE', WHITE, 40, l=M, t=80)
    + lt('Sub', 'Advancing the patient experience\nwith Android Enterprise solutions.', WHITE, 19, l=M, t=190)
    + chev_list(['Custom, enterprise-grade devices for hospitals and providers', 'Improve the patient experience, remote or in-person', 'Streamline the device lifecycle end to end'], WHITE, 12, M, 262, 420, gap=6)
    + lt('Intro', 'Smartphones, tablets and wearables are changing healthcare: telehealth, remote patient monitoring, clinical trials. A custom mobility solution keeps those devices purpose-built, secure and available for up to five years.', BLACK, 12, l=M, t=400, w=480)
    + sm('Stat lead', 'By 2027 up to', BLACK, 11, l=600, t=400) + stat('60', '%', BLUE, 72, l=600, t=426) + sm('Stat detail', 'of patient interactions\nwill be virtual.', BLACK, 11, l=600, t=498)
    + line('Rule', RULE, M, 560, W - 2 * M, 1)
    + hb('Section head', 'HEALTHCARE\nUSE CASES AND\nAPPLICATIONS', BLUE, 21, l=M, t=582)
    + chev_list(USES[:5], BLACK, 11.5, 300, 584, 220, gap=4, ccolor=BLUE, cls='lt') + chev_list(USES[5:], BLACK, 11.5, 540, 584, 220, gap=4, ccolor=BLUE, cls='lt')
    + line('Rule', RULE, M, 720, W - 2 * M, 1)
    + ''.join(icon(k, 26, BLUE, t_, l=M + i * 184, t=740) + hb('Title', t_.upper(), BLUE, 13, l=M + i * 184, t=776, w=164) + lt('Detail', d, BLACK, 10.5, l=M + i * 184, t=798, w=164)
              for i, (k, t_, d) in enumerate(PILLARS))
    + line('Rule', RULE, M, 900, W - 2 * M, 1)
    + wordmark(96, BLUE, l=M, t=920) + sm('About', ABOUT, BLACK, 8.5, l=M, t=946, w=320)
    + contact_block(BLUE, 470, 918) + legal(BLACK), 'US Letter one-pager')

doc('onepagers', 'op-dark', 'One-pager · Midnight (logistics)', WHITE,
    photo('Background', 'tex-slab', 0, 0, W, 430, '70% 50%')
    + wordmark(96, WHITE, l=M, t=36)
    + lbl('TRANSPORT & LOGISTICS', ACC, 11, l=M, t=120)
    + hl('Headline', 'EVERY ROUTE,\nEVERY DRIVER,\nONE FLEET', WHITE, 44, l=M, t=144)
    + lt('Sub', 'Purpose-built tablets and handhelds for fleet management, ELD compliance and real-time route optimisation.', WHITE, 15, l=M, t=312, w=400)
    + chamfer('Photo', 500, 250, 268, 290, c=44, photo_key='ph-driver', align='xMidYMid')
    + ''.join(stat(n, s, BLUE, 44, l=M + i * 150, t=470) + sm('Stat text', d, BLACK, 10, l=M + i * 150, t=516, w=130)
              for i, (n, s, d) in enumerate([('15', 'M+', 'Devices deployed'), ('5', 'YR', 'Device availability'), ('1', '', 'Partner, end to end')]))
    + line('Rule', RULE, M, 580, W - 2 * M, 1)
    + hb('Head', 'USE CASES', BLACK, 15, l=M, t=600)
    + chev_list(['Electronic logging (ELD)', 'Proof of delivery', 'Fleet and asset tracking', 'Route optimisation'], BLACK, 11.5, M, 630, 330, gap=5, ccolor=BLUE, cls='lt')
    + chev_list(['Driver workflow apps', 'In-cab mounting and charging', 'Warehouse scanning', 'Yard management'], BLACK, 11.5, 300, 630, 330, gap=5, ccolor=BLUE, cls='lt')
    + ''.join(chamfer(f'{t_} card', 520 + (i % 2) * 128, 600 + (i // 2) * 128, 118, 118, c=16, fill=PAPER, inner=
                      icon(k, 24, BLUE, t_, l=12, t=12) + st('Title', t_, BLACK, 11, l=12, t=50, w=100))
              for i, (k, t_, _) in enumerate(PILLARS))
    + line('Rule', RULE, M, 880, W - 2 * M, 1)
    + wordmark(96, BLUE, l=M, t=906) + sm('About', ABOUT, BLACK, 8.5, l=M, t=932, w=320)
    + contact_block(BLUE, 470, 904) + legal(BLACK), 'US Letter one-pager')

doc('onepagers', 'op-solution', 'One-pager · Solution sheet (managed services)', PAPER,
    fill('Top', WHITE, l=0, t=0, w=W, h=300)
    + wordmark(96, BLUE, l=M, t=36) + lbl('SOLUTION SHEET', BLUE, 11, r=M, t=42)
    + hl('Headline', 'MANAGED\nSERVICES', BLACK, 56, l=M, t=96)
    + lt('Sub', 'Let us handle device logistics so you can focus on your business. Our global warehouse teams run the whole device lifecycle.', BLACK, 15, l=M, t=230, w=420)
    + chamfer('Photo', 500, 60, 268, 300, c=44, photo_key='ph-team', align='xMidYMid')
    + ''.join(chamfer(f'Step {i+1}', M + i * 184, 390, 170, 250, c=24, fill=BLUE if i == 0 else WHITE, inner=
                      T('Number', f'{i+1:02d}', 'n27', ACC if i == 0 else BLUE, 12, l=18, t=20)
                      + icon(k, 26, WHITE if i == 0 else BLUE, a, l=18, t=48)
                      + hb('Title', a.upper(), WHITE if i == 0 else BLUE, 14, l=18, t=92, w=140)
                      + lt('Detail', b_, WHITE if i == 0 else BLACK, 10.5, l=18, t=120, w=136))
              for i, (k, a, b_) in enumerate([('box', 'Staging & kitting', 'Devices, accessories and packaging assembled to your spec.'),
                                             ('shield', 'Enrolment', 'MDM enrolment, apps and settings before it ships.'),
                                             ('truck', 'Deployment', 'Delivered to sites, ready to use out of the box.'),
                                             ('cycle', 'Repair & recycle', 'Swap, repair and responsibly recycle at end of life.')]))
    + hb('Head', 'WHY IT MATTERS', BLACK, 15, l=M, t=680)
    + chev_list(['Fewer IT hours spent imaging and shipping devices', 'Consistent devices across every site', 'One partner accountable from order to end of life'], BLACK, 12, M, 710, 360, gap=6, ccolor=BLUE, cls='lt')
    + chamfer('Callout', 440, 680, 328, 170, c=26, fill=BLUE, inner=
              lt('Callout', 'Ask about a pilot: one site, one fleet, fully managed.', WHITE, 16, l=24, t=28, w=280) + T('CTA', 'sales@nexamobility.com', 'n27', ACC, 12, l=24, t=118))
    + line('Rule', RULE, M, 890, W - 2 * M, 1)
    + wordmark(96, BLUE, l=M, t=914) + sm('About', ABOUT, BLACK, 8.5, l=M, t=940, w=320)
    + contact_block(BLUE, 470, 912) + legal(BLACK), 'US Letter one-pager')

# ============================================================== LETTERHEADS & STATIONERY
BODY = ('This is a sample letter placed to demonstrate the typing format on the NEXA letterhead. When positioned properly, it will '
        'serve to work in harmony with all of the other elements on the page, and project an image of professionalism and reliability.')
def letter(l, t, w, col=BLACK):
    return (stack('Addressee', [text('To', 'To', 'small', GREY_T, 10), text('Name', 'Recipient Name', 'sh3', col, 14), text('Role', 'Title, Company', 'small', GREY_T, 10), text('Address', 'Street, City, ST 00000', 'small', GREY_T, 10)], l=l, t=t, gap=3)
            + sm('Date', 'Date · 30 September 2026', GREY_T, 10, l=l, t=t + 100)
            + stack('Letter', [text('Salutation', 'Dear Name,', 'sh3', col, 13)] + [text('Paragraph', BODY, 'body', col, 11.5) for _ in range(3)], l=l, t=t + 150, w=w, gap=14)
            + stack('Sign-off', [text('Close', 'Kind regards,', 'body', col, 11.5), text('Name', 'Sender Name', 'sh3', col, 13), text('Role', 'Job Title', 'small', GREY_T, 10)], l=l, t=t + 470, gap=4))
def contacts_col(col, l, t):
    return stack('Contact details', [text(k, v, 'n27', col, 9.5) for k, v in [('Phone', '+1 (000) 000-0000'), ('Email', 'hello@nexamobility.com'), ('Web', 'nexamobility.com'), ('Address', '2057 Coolidge Street'), ('City', 'Hollywood, FL 33020')]], l=l, t=t, gap=3)

doc('stationery', 'lh-edge', 'Letterhead · Edge bar (from the mock-up)', WHITE,
    fill('Edge', BLUE, l=0, t=0, w=10, h=H)
    + wordmark(150, MIDNIGHT, l=64, t=56) + T('Department', 'ENGINEERING', 'sh3', MIDNIGHT, 12, r=M, t=72)
    + letter(64, 170, 560) + contacts_col(GREY_T, 64, 930), 'US Letter')

doc('stationery', 'lh-band', 'Letterhead · Midnight band', WHITE,
    photo('Band', 'tex-xbanner', 0, 0, W, 120, '85% 50%')
    + wordmark(150, WHITE, l=M, t=44) + T('Department', 'ENGINEERING', 'lbl', BLUE, 10, r=M, t=150)
    + letter(M, 180, 580) + line('Rule', RULE, M, 972, W - 2 * M, 1)
    + T('Footer', '+1 (000) 000-0000   ·   hello@nexamobility.com   ·   nexamobility.com   ·   2057 Coolidge Street, Hollywood, FL 33020', 'n27', GREY_T, 9, l=M, t=990), 'US Letter')

doc('stationery', 'lh-watermark', 'Letterhead · X watermark', WHITE,
    watermark(620, r=-180, b=-120)
    + wordmark(140, BLUE, l=M, t=52) + contacts_col(GREY_T, 560, 50)
    + line('Rule', BLUE, M, 150, W - 2 * M, 2)
    + letter(M, 190, 560), 'US Letter')

doc('stationery', 'lh-column', 'Letterhead · Side column', WHITE,
    fill('Column', PAPER, l=0, t=0, w=200, h=H)
    + vwordmark(260, BLUE, l=40, t=64)
    + contacts_col(GREY_T, 40, 900)
    + T('Department', 'ENGINEERING', 'lbl', BLUE, 10, l=240, t=64)
    + letter(240, 120, 520), 'US Letter')

def pr(aid, name, w, h, bg_, inner, use, fmt='print'):
    F.append(('stationery', artboard(aid, name, w, h, bg_, inner, use, fmt)))

pr('bc-front-blue', 'Business card · Front (Super Blue)', 1050, 600, BLUE,
   wordmark(560, WHITE, l=245, t=(600 - round(560 * WM['h'] / WM['w'])) // 2), '3.5 × 2 in at 300 ppi')
pr('bc-front-light', 'Business card · Front (X of light)', 1050, 600, MIDNIGHT,
   photo('Background', 'tex-xlight', 0, 0, 1050, 600, '80% 50%') + wordmark(420, WHITE, l=64, b=64), '3.5 × 2 in at 300 ppi')
pr('bc-back', 'Business card · Back (from the NEXA card)', 1050, 600, WHITE,
   T('Name', 'First Last', 'sh2', BLACK, 50, l=48, t=48)
   + T('Details', 'Job Title\n+1 (000) 000-0000\nname@nexamobility.com', 'n27', '#6F6F6F', 26, l=48, t=128)
   + T('Address', '2057 Coolidge Street\nHollywood, FL, 33020\nUnited States', 'n27', '#6F6F6F', 26, l=48, t=344)
   + T('Web', 'www.nexamobility.com', 'n27', '#6F6F6F', 26, l=48, t=500)
   + qr_dots('https://nexamobility.com', 190, BLUE, r=48, t=52)
   + wordmark(146, BLUE, r=48, b=64), '3.5 × 2 in at 300 ppi')
pr('bc-back-blue', 'Business card · Back (Super Blue)', 1050, 600, BLUE,
   T('Name', 'First Last', 'sh2', WHITE, 50, l=48, t=48)
   + T('Details', 'Job Title\n+1 (000) 000-0000\nname@nexamobility.com', 'n27', WHITE, 26, l=48, t=128)
   + T('Web', 'nexamobility.com', 'n27', ACC, 26, l=48, t=500)
   + qr_dots('https://nexamobility.com', 190, WHITE, r=48, t=52)
   + emblem(90, WHITE, r=48, b=56), '3.5 × 2 in at 300 ppi')
pr('env-dl', 'Envelope · #10', 912, 396, WHITE,
   wordmark(150, BLUE, l=40, t=40) + T('Return', '2057 Coolidge Street\nHollywood, FL 33020', 'n27', GREY_T, 11, l=40, t=90)
   + T('Recipient', 'Recipient Name\nCompany\nStreet Address\nCity, ST 00000', 'body', BLACK, 15, l=420, t=190)
   + fill('Edge', BLUE, l=0, t=386, w=912, h=10), '9.5 × 4.125 in')
pr('fold-cover', 'Presentation folder · Cover', 816, 1056, MIDNIGHT,
   photo('Background', 'tex-xlight', 0, 0, 816, 1056, '80% 50%')
   + hl('Headline', 'THE NEXT\nGENERATION\nENTERPRISE', WHITE, 58, l=M, t=120)
   + wordmark(220, WHITE, l=M, b=64) + T('URL', 'nexamobility.com', 'n27', WHITE, 14, r=M, b=72), '9 × 12 in folder (shown at letter size)', 'doc')

SECTION_META = [
    ('cases', 'Case studies', 'Four case-study layouts: the classic Oneview one-pager, a midnight cover, a photo container with results band (blank template), and a Super Blue sidebar.'),
    ('onepagers', 'One-pagers', 'Industry, midnight and solution-sheet one-pagers on one shared grid, rebuilt from the NEXA Healthcare One Pager.'),
    ('stationery', 'Letterheads & stationery', 'Four letterheads, three business-card sides, an envelope and a folder cover.'),
]
