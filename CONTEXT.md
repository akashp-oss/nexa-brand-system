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

**Fonts.** N27 is licensed and not in the repo. Everything renders in **Saira** (OFL), the closest open face to N27's
squared, technical forms, with `N27` first in the font stack so it takes over wherever it is installed.
Roboto (Apache 2.0) is the brand's own second face. Both are embedded in the HTML.

## 3. Graphic devices (new, derived from the brandbook)

1. **Brackets `><`**: the two halves of the X frame an image or focal point (brandbook p.5 and the Instagram mock-up on p.36).
2. **X window**: a photo seen through the emblem, on Base Gray inside a Turquoise frame (p.36).
3. **INDUSTRY X MOBILITY lockup** across a **split convergence** layout: industry photo on one side, brand light on the other (p.22–33).
4. **Meta rail** and **index numerals** (“003”, “A.1”) from the brandbook page furniture and web mock-up.
5. **Forward arrow** from the E, used as bullet and CTA marker.
6. **Layout:** emblem top-right, wordmark bottom-left (colour variation page, p.15).

## 4. Imagery

- **Super Blue grade** (`brand/imagery/grade.py`): photos mapped Space Black → Super Blue → pale blue, matching the in-situ pages.
- **Brand light** (`brand/imagery/textures.html`): generated fibre burst, light trails, neon tunnel, ribbon X, data wave and horizon grid. No licence needed.
- **Placeholders:** the `ph-*` photos are reused from the Sonim system (mostly Pexels; `ph-clinician` comes from Sonim's site collage and its source is unknown). Replace them all with licensed NEXA photography before publishing externally.

## 5. Asset sets (v1)

Foundations (7 boards) · Social posts (6) · Stories (2) · LinkedIn & landscape (2) · Presentation (5) · Web & email (3) · Stationery (3).

## 6. Open items

- Licensed N27 font files, to check the Saira stand-in against the real face.
- Official logo artwork from NEXA. The SVGs here are traced from the brandbook's vectors, so they are exact, but confirm with the source files.
- Real NEXA photography and industry list (the in-situ pages show Health, Retail and Defense).
- Stats on the stats slide are placeholders: replace them with sourced figures.
- Netlify site `nexa-brand-asset` still has to be created: connect this repo in Netlify, or run `make deploy` with a token.
