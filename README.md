# NEXA brand system

Brand asset library for **NEXA** (Next Generation Enterprise), built from the NEXA Brand Guidelines v1.0 (2024).
It follows the same approach as the Sonim brand system: plain HTML, so every asset can be edited in the browser
and copied into Figma.

**Start with [`CONTEXT.md`](CONTEXT.md)**: the brand rules as implemented, the graphic devices, the file map and open items.

## Open it

| What | File |
|---|---|
| Brand asset library: 71 assets in 9 sets (social, LinkedIn, web, a 16-slide deck, case studies, one-pagers, stationery), plus a Brand guidelines view (9 boards) | [`library/dist/NEXA_Brand_Asset_Library.html`](library/dist/NEXA_Brand_Asset_Library.html) |
| Official logo artwork (SVG, EPS, PNG, JPG) | [`NEXA_LogoSystem/`](NEXA_LogoSystem/) |
| Fonts (N27, Roboto) | [`NEXA_Typography/`](NEXA_Typography/) |
| Client references and inspiration | [`Asset Inspiration/`](Asset%20Inspiration/), [`reference/`](reference/) |
| Brand guidelines (source) | [`reference/NEXA_Brand_Guidelines_2024_v1.0.pdf`](reference/) |

Download the HTML file and open it in Chrome or Edge. It is self-contained: fonts, images and logo are embedded.

## Using the library

- **Asset library / Brand guidelines:** the library opens on the assets; the brandbook boards live behind **Brand guidelines** (or `?view=guide`).
- **Secondary:** switch the secondary colour live (Electric Azure by default; Bright Turquoise, Periwinkle, Base Gray). It recolours every asset and Copy SVG exports the chosen colour.
- **Zoom:** Fit, 25%, 50% or 100%.
- **Guides:** shows margins and the story safe zones.
- **Edit:** click any text to change it; double-click an image (including the X window) to replace it. **Save file** keeps a copy with your edits.
- **Copy SVG:** hover an asset, click **Copy SVG**, then press Ctrl/⌘ + V in Figma. Text stays editable in N27 and Roboto (install both in Figma), the logo stays vector.
- **Figma import view:** true size with no labels; pick a set and run an HTML-to-Figma plugin such as html.to.design. Link straight to a set with `?figma=square`, `?figma=stories`, `?figma=slides` and so on.

## Build

Requires Python 3.10+ (`pip install -r requirements.txt`), Node 18+ and Playwright with Chromium.

```bash
make library   # library/dist/NEXA_Brand_Asset_Library.html
make qa        # screenshots into .qa/ plus layout checks (overlaps, margins, logo size)
make logo      # rebuild logo.json from NEXA_LogoSystem
make imagery   # re-render the generated brand-light textures
make deploy    # publish to Netlify (needs NETLIFY_AUTH_TOKEN)
```

## Hosting on Netlify

The site is called **nexa-brand-asset**. `netlify.toml` publishes only a `public/` folder holding the library as
`index.html`, never the repo root (which holds the brandbook PDF). Two ways to publish:

- **From GitHub:** in Netlify, *Add new site → Import from Git*, pick this repo, set the site name to `nexa-brand-asset`.
  Every push then redeploys.
- **From the CLI:** `export NETLIFY_AUTH_TOKEN=…` then `make deploy`. The first run links the site.

## Structure

```
brand/       logo.json + clean SVGs built from NEXA_LogoSystem, fallback fonts, imagery tools
library/     asset library: src/ (gen.py helpers; templates.py social/web; deck.py slides; docs.py print; guide.py boards; qa.js) → dist/
reference/   NEXA Brand Guidelines v1.0 (client document; keep the repo private)
```
