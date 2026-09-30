# NEXA brand system: build targets. Requires Python 3.10+ (see requirements.txt), Node 18+ and Playwright with Chromium.
.PHONY: all logo imagery library qa public deploy

all: library

logo:             ## brand/logo/*.svg + logo.json, traced from the brandbook vectors
	python3 brand/logo/extract_logo.py reference/NEXA_Brand_Guidelines_2024_v1.0.pdf brand/logo

imagery:          ## generated brand-light textures -> library/src/img/tex-*.jpg
	node brand/imagery/render_textures.js library/src/img

library:          ## library/dist/NEXA_Brand_Asset_Library.html
	python3 library/src/build.py

qa: library       ## screenshots + overflow/error checks into .qa/
	node library/src/shots.js

public: library   ## the folder Netlify publishes
	rm -rf public && mkdir -p public && cp library/dist/NEXA_Brand_Asset_Library.html public/index.html

deploy: public    ## needs NETLIFY_AUTH_TOKEN; creates/links the site "nexa-brand-asset" on first run
	netlify deploy --prod --dir public --site $${NETLIFY_SITE_ID:-nexa-brand-asset}
