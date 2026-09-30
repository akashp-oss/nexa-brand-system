# NEXA brand system: context

## 1. Background

NEXA is the parent brand (“Next Generation Enterprise”, enterprise mobility across industries). Sonim Technologies
is a NEXA company; its brand system (`akashp-oss/sonim-brand-system`) came first and this repo follows its approach.
NEXA has a brandbook (`reference/NEXA_Brand_Guidelines_2024_v1.0.pdf`, 39 pages) but no social media guideline, so
the social, deck, web and stationery layouts here are new work derived from the brandbook.

## 2. Brand rules, as implemented

| Area | Brandbook | Where it lives |
|---|---|---|
| Idea | “What’s next”. Tone: contemporary, bold, dynamic, progressive | copy in templates |
| Wordmark | NEXA with arrow in the E; X made of two brackets `><`. ™ included | `brand/logo/nexa-wordmark-*.svg` |
| Tagline | NEXT GENERATION ENTERPRISE, set under the wordmark | `wordmark_tagline()` in `gen.py` |
| Emblem | the X alone; use for avatars and small spaces | `brand/logo/nexa-emblem-*.svg` |
| Clear space | height of the X on every side | Foundations · Logo system |
| Minimum size | wordmark 200 px (2.5 in); emblem 50 px (0.5 in) | all templates respect it |
| Don’ts | no stretch, angle, spread, outline, effects, gradients, added elements, low contrast, altered structure | sidebar “Never” |
| Colour | Super Blue #1F1FCC (primary), Base Gray #C9C7C9 (secondary), Bright Turquoise #36FFE8, Bright Pink #FF5FEB, Dark Purple #2D0685, Space Black #000 | `PALETTE` in `gen.py` |
| Pairings | logo on: Turquoise→Blue, Gray→Blue, Purple→Turquoise, Black→Blue, Blue→Gray, Turquoise→Purple | `PAIRS_OK` |
| Avoid | Pink+Turquoise, Purple on Blue, Purple on Black, Blue+Purple, Turquoise on Gray, Pink on Turquoise | `PAIRS_NO` |
| Headline | N27 Regular, UPPERCASE, never bold | `.hl` |
| Sub-header 1 / 2 / 3 | Roboto Regular UPPERCASE / Roboto Regular Title Case / Roboto Bold Title Case | `.sh1` `.sh2` `.sh3` |
| Scale | perfect fifth, about 1.5× per level (120 / 48 / 36 / 24 pt in the book) | per template |
| Page furniture | three-point rail “NEXA · Version 1.0 · 2024” | `rail()` |
| In situ | split images (industry photo + tech texture), white wordmark centred, “HEALTH X MOBILITY” lockup, blue-graded photography | `lockup()`, Super Blue grade |

**Fonts.** The real **N27 Regular** (`NEXA_Typography/N27-Regular.otf`) and Roboto are embedded in the HTML; Saira
remains only as a fallback. The N27 file allows embedding (fsType 8), but check the licence covers a public website.

## 3. Graphic devices (new, derived from the brandbook)

1. **Brackets `><`**: the two halves of the X frame an image or focal point (brandbook p.5 and the Instagram mock-up on p.36).
2. **X window**: a photo seen through the emblem, on Base Gray inside a Turquoise frame (p.36).
3. **INDUSTRY X MOBILITY lockup** across a **split convergence** layout: industry photo on one side, brand light on the other (p.22–33).
4. **Meta rail** and **index numerals** (“003”, “A.1”) from the brandbook page furniture and web mock-up.
5. **Forward arrow** from the E, used as bullet and CTA marker.
6. **Layout:** emblem top-right, wordmark bottom-left (colour variation page, p.15).

## 3b. Round 2 direction (client feedback)

- Library opens on assets; brandbook boards moved to a separate **Brand guidelines** view.
- **Secondary colour** is an experiment, switchable live. Recommendation: **Periwinkle #A6A8FF** (tint #ECECFC), a
  softer member of the Super Blue family that matches the pale X in the NEXA Figma. Alternatives: Bright Turquoise
  (brandbook), Ice Mint #9FE8DC, Signal Coral #FF7A5C, Base Gray. Defined in `ACCENTS` (`gen.py`).
- **Photography in natural colour.** The Super Blue grade is kept only for the brand-light split post.
- **Containers** from the NEXA Figma "Visual identity" page: top-left and bottom-right corners cut at 45°, Base Gray
  slabs echoing each cut outward, pale X watermark, live area equally inset (`chamfer()`, `watermark()`).
- **Statements** in Roboto Bold, sentence case (as in the Figma), alongside uppercase N27 headlines.
- Copy uses public NEXA facts (nexamobility.com, press): formerly Social Mobile (rebrand 2025), founded 2011,
  15M+ devices deployed, designed in the USA, verticals: healthcare, retail, hospitality, transportation & logistics,
  public safety, defense. Sonim is a NEXA company.

## 3c. Round 3: rebuilt on NEXA's own references

Sources read in full: `NEXA_LogoSystem/` (official wordmark, tagline lockup, emblem), `NEXA_Typography/`,
`reference/NEXA_Colors.pdf`, `Asset Inspiration/` (X-light and slab backgrounds, arcs, banner, CTA section,
business card, Healthcare One Pager, MWC video), `reference/NEXA_Case_Study_Oneview_One_Pager.pdf`,
`reference/social-examples/` (case-study card, night statement, letterhead and web mock-ups, brandbook posts).

What NEXA's own work does, and the library now follows:
- **Logo:** official artwork (`brand/logo/extract_official.js` reads the SVGs); white on dark, Super Blue on white.
- **Colour in practice:** Super Blue for panels and case studies; **Midnight #00133A → Electric #0068F4 → Sky #00A1F6**
  light for dark grounds. Secondary default is now **Electric Azure #3AA8FF**, sampled from those visuals.
  Bright Turquoise remains as an option, used as a line of light, not a fill.
- **Type in practice:** N27 uppercase headlines; **Roboto Light** statements ("Custom-Built Mobility Solutions for
  Enterprise."); Roboto Bold titles; **Roboto Black** uppercase section heads and big numbers with small suffixes
  (50%, 2K, 50+); N27 for contact details (business card); thin `>` chevron bullets.
- **Devices:** the X of light and the slanted slab of light (web backgrounds), the outline slash (case-study card),
  Super Blue veil over photos for case studies, night tone for statements, NEXA | partner lockup, dot QR code.
- **Copy** from the collateral: Oneview Healthcare case study (50% / 2K / 50+), healthcare use cases,
  "By 2027 up to 60% of patient interactions will be virtual", four pillars (Custom Devices, Rhino Mobility,
  Managed Services, Wireless Connectivity), Android Enterprise Gold partner.

## 4. Imagery

- **Light:** `tex-xlight`, `tex-slab`, `tex-arcs`, `tex-xbanner` (from Asset Inspiration) and `tex-aurora-*`
  (frames of the MWC video with the logo row removed).
- **Photos:** natural colour; `phn-*` night tone for statements; Super Blue veil applied in layout for case studies.
- **Placeholders:** the `ph-*` photos come from the Sonim system (mostly Pexels). Replace with NEXA photography.

## 5. Asset sets (v3)

Library (48): Square posts (18) · Carousel & portrait (6) · Stories (4) · LinkedIn & X (6) · Sales collateral (2) ·
Presentation (5) · Web & email (4) · Stationery (3). Brand guidelines: 9 boards.

## 6. Open items

- Partner and customer logos are dashed placeholders (Oneview, InfoBionic, Android, Rhino, Sonim).
- Real NEXA photography; the healthcare product shot from the one-pager if a clean file exists.
- Confirm the secondary colour (Electric Azure recommended) and N27 web-embedding licence.
- The Figma social page is still unseen (figma.com is not reachable from the build environment); export it as PNG/PDF.
