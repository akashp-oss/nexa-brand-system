# NEXA brand system: build targets. Requires Python 3.10+ (see requirements.txt), Node 18+ and Playwright with Chromium.
.PHONY: all logo imagery library qa public deploy

all: library

logo:             ## brand/logo/*.svg + logo.json from the official NEXA_LogoSystem SVGs
	node brand/logo/extract_official.js

imagery:          ## (textures now come from Asset Inspiration; generated set kept for reference)
	node brand/imagery/render_textures.js library/src/img

library:          ## library/dist/NEXA_Brand_Asset_Library.html
	python3 library/src/build.py

qa: library       ## screenshots + overflow/error checks into .qa/
	node library/src/shots.js

public: library   ## the folder Netlify publishes
	rm -rf public && mkdir -p public && cp library/dist/NEXA_Brand_Asset_Library.html public/index.html

deploy: public    ## needs NETLIFY_AUTH_TOKEN; creates/links the site "nexa-brand-asset" on first run
	netlify deploy --prod --dir public --site $${NETLIFY_SITE_ID:-nexa-brand-asset}
