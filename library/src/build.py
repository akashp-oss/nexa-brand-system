"""Build library/dist/NEXA_Brand_Asset_Library.html: one self-contained file (fonts, images, logo inlined)."""
import sys, base64, os, json, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from gen import *
import templates as TP
import guide as GD
import re

def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()
IMG = {}
for f in sorted(os.listdir(HERE / 'img')):
    k, ext = f.rsplit('.', 1)
    IMG[k] = f'data:image/{"jpeg" if ext == "jpg" else ext};base64,' + b64(HERE / 'img' / f)
FONTS = (f"@font-face{{font-family:'Saira';src:url(data:font/woff2;base64,{b64(ROOT / 'brand/fonts/Saira-Variable.woff2')}) format('woff2');font-weight:100 900;font-display:block}}"
         f"@font-face{{font-family:'Roboto';src:url(data:font/woff2;base64,{b64(ROOT / 'brand/fonts/Roboto-Variable.woff2')}) format('woff2');font-weight:100 900;font-display:block}}")
# N27 (licensed): embedded automatically when its files are in brand/fonts (any sub-folder). Check the web-embedding licence.
_W = {'thin': 100, 'extralight': 200, 'light': 300, 'regular': 400, 'medium': 500, 'semibold': 600, 'bold': 700, 'black': 900}
_MIME = {'woff2': 'font/woff2', 'woff': 'font/woff', 'otf': 'font/otf', 'ttf': 'font/ttf'}
_FMT = {'woff2': 'woff2', 'woff': 'woff', 'otf': 'opentype', 'ttf': 'truetype'}
N27 = {}
for f in sorted([*(ROOT / 'brand/fonts').rglob('*'), *(ROOT / 'NEXA_Typography').rglob('*')]):
    ext = f.suffix.lower().lstrip('.')
    if 'n27' not in f.name.lower() or ext not in _MIME or 'italic' in f.name.lower(): continue
    key = re.sub(r'[^a-z]', '', f.stem.lower().replace('n27', ''))
    w = next((v for k, v in sorted(_W.items(), key=lambda kv: -len(kv[0])) if key.endswith(k)), 400)
    if w not in N27 or ext == 'woff2': N27[w] = (f, ext)
for w, (f, ext) in sorted(N27.items()):
    FONTS += f"@font-face{{font-family:'N27';src:url(data:{_MIME[ext]};base64,{b64(f)}) format('{_FMT[ext]}');font-weight:{w};font-display:block}}"
HEAD_NAME = 'N27' if N27 else 'Saira (N27 stand-in)'

MARGINS = {'board': 64, 'post': 72, 'story': 72, 'land': 48, 'slide': 64, 'web': 64, 'print': 64, 'doc': 64}

sections_html, nav, tiles = [], [], []
for view, mod in (('library', TP), ('guide', GD)):
    for i, (sid, title, intro) in enumerate(mod.SECTION_META):
        frames = [h for s_, h in mod.F if s_ == sid]
        num = f'{i + 1:02d}' if view == 'library' else 'BG'
        nav.append(f'<a class="nav-item" href="#sec-{sid}" data-sec="{sid}" data-view="{view}"><i>{num}</i><span>{esc(title)}</span><em>{len(frames)}</em></a>')
        if view == 'library':
            tiles.append(f'<a class="set-tile" href="#sec-{sid}"><i>{num}</i><b>{esc(title)}</b><em>{len(frames)} assets</em></a>')
        sections_html.append(
            f'<section class="lib-section" id="sec-{sid}" data-view="{view}" data-name="{esc(title)}">'
            f'<header class="sec-head"><div class="sec-rail"><span>NEXA</span><span>{"Asset set " + num if view == "library" else "Brand guidelines"}</span><span>{len(frames)} {"assets" if view == "library" else "boards"}</span></div>'
            f'<div class="sec-body"><div class="sec-num">{num}</div><div><h2>{esc(title)}</h2><p>{esc(intro)}</p></div></div></header>'
            f'<h2 class="figma-title" data-name="{esc(title)} title">{esc(title)}</h2>'
            f'<div class="frames">{"".join(frames)}</div></section>')
_hw, _hh, _hc = 480, 500, 88
_hcy = round(_hc * CUT_RATIO)
HERO_ART = (f'<svg viewBox="0 0 {_hw} {_hh}"><defs><clipPath id="heroclip"><polygon points="{_hc},0 {_hw},0 {_hw},{_hh-_hcy} {_hw-_hc},{_hh} 0,{_hh} 0,{_hcy}"/></clipPath></defs>'
            f'<image data-ui-img="ph-crew" width="{_hw}" height="{_hh}" preserveAspectRatio="xMidYMid slice" clip-path="url(#heroclip)"/></svg>')
ALL_META = [(s_, t_) for s_, t_, _ in TP.SECTION_META + GD.SECTION_META]
N_LIB, N_GUIDE = len(TP.F), len(GD.F)

def paths(inner): return inner
def svg_logo(inner, w, h, fill, cls=''):
    return f'<svg class="{cls}" viewBox="0 0 {w} {h}" fill="{fill}" aria-hidden="true">{inner}</svg>'
WM_UI = svg_logo(WM['inner'], WM['w'], WM['h'], '#fff', 'wm')
EM_UI = svg_logo(EM['inner'], EM['w'], EM['h'], 'currentColor', 'em')
FAVICON = 'data:image/svg+xml,' + urllib.parse.quote(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="{BLUE}"/>'
    f'<g transform="translate(10 16.6) scale({44 / EM["w"]})" fill="#3AA8FF">{EM["inner"]}</g></svg>')

CSS = r"""
:root{--blue:#1F1FCC;--gray:#C9C7C9;--turq:#36FFE8;--pink:#FF5FEB;--purple:#2D0685;--black:#000;
  --acc:#3AA8FF;--tint:#E9F2FF;--canvas:#EFEEF0;--line:#E2E1E2;--muted:#6F6D6F;--ui:Roboto,Arial,sans-serif;--head:'N27','Saira',sans-serif;--top:64px;--side:300px}
*{box-sizing:border-box}
html{scroll-padding-top:calc(var(--top) + 16px)}
html,body{margin:0;background:var(--canvas);color:#000;font-family:var(--ui)}
button{font-family:var(--ui)}
:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
*{scrollbar-width:thin;scrollbar-color:#BDBBBD transparent}
::-webkit-scrollbar{width:8px;height:8px}::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#BDBBBD;border:2px solid transparent;background-clip:padding-box}
/* ---------- app bar ---------- */
.topbar{position:fixed;top:0;left:0;right:0;height:var(--top);background:#000;color:#fff;display:flex;align-items:center;gap:8px;padding:0 16px 0 0;z-index:30}
.topbar .mark{width:var(--top);height:var(--top);background:var(--blue);display:grid;place-items:center;flex:none;margin-right:20px}
.topbar .mark .em{width:30px;height:auto;display:block;color:var(--acc)}
.topbar .brand{display:flex;align-items:center;gap:18px;margin-right:24px;flex:none}
.topbar .spacer{flex:1}
.topbar .brand .wm{width:92px;height:auto;display:block;flex:none}
.topbar .brand b{font:400 15px/1 var(--head);letter-spacing:.08em;text-transform:uppercase;white-space:nowrap;border-left:1px solid #333;padding-left:18px}
.topbar .brand span{font-size:12px;color:#8E8C8E;white-space:nowrap}
.btn{font:500 13px/1 var(--ui);color:#fff;background:transparent;border:1px solid #3A3A3A;border-radius:0;height:38px;padding:0 16px;transition:background .15s,border-color .15s,color .15s;cursor:pointer;white-space:nowrap}
.btn:hover{border-color:#fff}.btn.on{background:#fff;color:#000;border-color:#fff}
.btn.primary{background:var(--blue);border-color:var(--blue)}
.btn.primary:hover,.btn.primary.on{background:var(--acc);border-color:var(--acc);color:#000}
.seg{display:flex}.seg .btn+.btn{margin-left:-1px}
.sep{width:1px;height:26px;background:#333;margin:0 4px}
#btn-menu{display:none}
.side-views{display:none;margin:0 24px 20px;gap:0}.side-views button{flex:1;font:500 13px/1 var(--ui);height:38px;border:1px solid #D0CFD2;background:#fff;cursor:pointer}.side-views button.on{background:var(--blue);border-color:var(--blue);color:#fff}
.views{display:flex;margin-right:10px}.views .btn{height:38px}.views .btn+.btn{margin-left:-1px}
.views .btn.on{background:var(--blue);border-color:var(--blue);color:#fff}
.accents{display:flex;align-items:center;gap:6px;padding:0 6px;font-size:11px;color:#8E8C8E}
.accents button{width:20px;height:20px;border-radius:50%;border:2px solid #000;outline:1px solid #3A3A3A;cursor:pointer;padding:0}
.accents button.on{outline:2px solid #fff}
#sec-found .sec-head{display:none}
body[data-view=library]:not(.figma) [data-view=guide],body[data-view=guide]:not(.figma) [data-view=library]{display:none!important}
/* ---------- sidebar ---------- */
.sidebar{position:fixed;top:var(--top);bottom:0;left:0;width:var(--side);background:#fff;overflow:auto;padding:28px 0 32px;z-index:20}
.side-h{font:400 13px/1 var(--head);letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin:0 24px 12px}
.nav-item{display:grid;grid-template-columns:28px 1fr auto;align-items:center;padding:9px 24px 9px 20px;color:#000;text-decoration:none;font-size:14px;font-weight:500;border-left:4px solid transparent}
.nav-item i{font:400 12px/1 var(--head);font-style:normal;color:var(--muted)}
.nav-item em{font-style:normal;font-weight:400;font-size:12px;color:var(--muted)}
.nav-item:hover{background:#F4F4F4}.nav-item.on{border-left-color:var(--blue);color:var(--blue)}.nav-item.on i{color:var(--blue)}
.rules{margin:24px 0 0;padding:24px 24px 0;border-top:1px solid var(--line)}
.rules .side-h{margin:0 0 14px}
.rule{padding:14px 0;border-top:1px solid var(--line)}
.rule:first-of-type{border-top:0;padding-top:0}
.rule h4{font-size:12px;margin:0 0 10px;font-weight:700}
.rule p,.rule li{font-size:12px;line-height:1.45;margin:0}
.rule ul{list-style:none;margin:0;padding:0;display:grid;gap:4px}
.rule li{display:flex;gap:8px;align-items:baseline}
.rule li i{font-style:normal;font-weight:700;flex:none;width:10px}
.chips{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:10px}
.chip{display:flex;align-items:center;gap:8px;padding:6px;border:1px solid var(--line);background:#fff;cursor:pointer;text-align:left;font:11px/1.25 var(--ui);color:#000}
.chip:hover{border-color:#000}
.chip s{display:block;width:24px;height:24px;flex:none;border:1px solid rgba(0,0,0,.08)}
.chip b{display:block;font-size:11px;font-weight:500}
.pairs{display:grid;grid-template-columns:repeat(6,1fr);gap:4px;margin-bottom:8px}
.pair{aspect-ratio:1;display:grid;place-items:center}
.pair svg{width:56%;height:auto}
.sample{font:400 22px/1 var(--head);text-transform:uppercase;margin:2px 0 6px;color:var(--blue)}
.sample2{font-size:13px;margin:0 0 10px}
.kv{display:grid;grid-template-columns:auto 1fr;gap:4px 10px;font-size:12px;line-height:1.4}
.kv dt{font-weight:700}.kv dd{margin:0}
.hint{margin:16px 24px 0;padding:14px;background:#000;color:#fff;font-size:12px;line-height:1.5}
.hint b{display:block;margin-bottom:4px;font:400 12px/1.2 var(--head);letter-spacing:.1em;text-transform:uppercase;color:var(--acc)}
.hint strong{font-weight:500;color:var(--acc)}
.scrim{display:none}
/* ---------- canvas ---------- */
.canvas{margin:var(--top) 0 0 var(--side);padding:0 56px 160px}
.hero{position:relative;margin:0 -56px 72px;padding:56px 56px 56px;background:#fff;overflow:hidden;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:48px;align-items:center}
.hero .wmk{position:absolute;right:-120px;top:-80px;width:560px;color:var(--tint);pointer-events:none}
.hero>*{position:relative;z-index:1}
.hero .kicker{font:400 14px/1 var(--head);letter-spacing:.1em;color:var(--blue);margin:0 0 18px}
.hero h1{font:400 64px/.98 var(--head);text-transform:uppercase;margin:0 0 18px}
.hero p{font-size:16px;line-height:1.55;margin:0 0 32px;max-width:600px;color:#222}
.hero-art{position:relative;padding:0 56px}.hero-art svg{display:block;width:100%;height:auto;overflow:visible}
.set-tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:8px}
.set-tile{display:flex;flex-direction:column;gap:6px;padding:16px 16px 18px;background:var(--tint);color:#000;text-decoration:none;transition:background .15s,color .15s;clip-path:polygon(14px 0,100% 0,100% calc(100% - 17px),calc(100% - 14px) 100%,0 100%,0 17px)}
.set-tile:hover{background:var(--blue);color:#fff}
.set-tile:hover i,.set-tile:hover em{color:#fff}
.guide-head{margin:0 -56px 56px;padding:56px;background:#000;color:#fff;position:relative;overflow:hidden}
.guide-head .wmk{position:absolute;right:-80px;top:-60px;width:520px;color:rgba(255,255,255,.07)}
.guide-head .kicker{font:400 14px/1 var(--head);letter-spacing:.1em;color:var(--acc);margin:0 0 16px}
.guide-head h1{font:400 56px/.98 var(--head);text-transform:uppercase;margin:0 0 16px}
.guide-head p{font-size:16px;line-height:1.55;margin:0;max-width:680px;color:#D8D8E0}
.set-tile i{font:400 13px/1 var(--head);font-style:normal;color:var(--blue)}
.set-tile b{font-size:14px;font-weight:500}
.set-tile em{font-style:normal;font-size:12px;color:#55535A}
.lib-section{padding-bottom:120px}
.lib-section+.lib-section{padding-top:56px}
.sec-head{margin:0 0 40px}
.sec-rail{display:flex;justify-content:space-between;font-size:12px;color:var(--muted);padding-bottom:10px;border-bottom:1px solid #CFCDCF;margin-bottom:28px}
.sec-body{display:flex;gap:28px;align-items:flex-start}
.sec-num{font:300 88px/.8 var(--head);color:var(--blue);flex:none;min-width:120px}
.sec-head h2{font:400 44px/1 var(--head);text-transform:uppercase;margin:0 0 12px}
.sec-head p{font-size:15px;line-height:1.5;margin:0;max-width:680px}
.frames{display:flex;flex-wrap:wrap;gap:64px 48px;align-items:flex-start}
.frame{margin:0;min-width:0}
.frame-meta{display:flex;flex-direction:column;gap:3px;margin-bottom:12px;font-size:12px;line-height:1.35;color:var(--muted)}
.frame-meta b{font-size:13px;font-weight:500;color:#000}
.ab-wrap{position:relative;z-index:0;overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,.08),0 8px 24px rgba(0,0,0,.08)}
.frame-tools{position:absolute;top:8px;right:8px;display:flex;gap:4px;opacity:0;transform:translateY(-4px);transition:opacity .15s,transform .15s;z-index:60}
.ab-wrap:hover .frame-tools,.frame-tools:focus-within{opacity:1;transform:none}
.frame.tiny .ab-wrap{overflow:visible}
.frame.tiny .frame-tools{bottom:auto;top:calc(100% + 6px);right:auto;left:0;opacity:1;transform:none}
.frame.tiny{margin-bottom:34px}
.tool{font:500 12px/1 var(--ui);height:32px;padding:0 14px;border:0;background:var(--blue);color:#fff;cursor:pointer;display:flex;align-items:center;gap:6px;white-space:nowrap}
.tool:hover{background:#000}.tool.done{background:#000;color:var(--acc)}
.tool:disabled{cursor:progress;opacity:.7}
/* ---------- artboard primitives (these become Figma layers) ---------- */
.ab{position:relative;overflow:hidden;transform-origin:0 0;font-family:var(--ui);color:#000;--em:#36FFE8}
.ab .abs{position:absolute}
.ab .stack{display:flex;flex-direction:column}
.ab .row{display:flex;flex-direction:row}
.ab .tx{margin:0;white-space:normal}
.ab .em{color:var(--em)}
.ab img{display:block;max-width:none}
.ab .photo{object-fit:cover}
.ab svg{display:block;overflow:visible}
/* type roles from the brandbook hierarchy; sizes are set per template */
.ab .hl{font-family:var(--head);font-weight:400;line-height:.98;letter-spacing:.005em}
.ab .num{font-family:var(--head);font-weight:300;line-height:.86;letter-spacing:-.01em}
.ab .sh1{font-weight:400;line-height:1.1;letter-spacing:.01em}
.ab .sh2{font-weight:400;line-height:1.2}
.ab .sh3{font-weight:700;line-height:1.2}
.ab .body{font-weight:400;line-height:1.45}
.ab .small{font-weight:400;line-height:1.35}
.ab .label{font-weight:500;line-height:1.1;letter-spacing:.12em}
.ab .rail{font-weight:400;line-height:1;white-space:nowrap}
.ab .lock{font-weight:400;line-height:1;letter-spacing:.02em;white-space:nowrap}
.ab .st{font-weight:700;line-height:1.06;letter-spacing:-.015em}
.ab .lt{font-weight:300;line-height:1.14;letter-spacing:-.005em}
.ab .hb{font-weight:900;line-height:1.02;letter-spacing:.01em}
.ab .stat{font-weight:900;line-height:.8;letter-spacing:-.03em}
.ab .n27{font-family:var(--head);font-weight:400;line-height:1.38}
.ab .lbl{font-family:var(--head);font-weight:400;line-height:1;letter-spacing:.09em;white-space:nowrap}
.ab .cutout{object-fit:contain}
.ab .tagline{font-weight:500;line-height:1;letter-spacing:.01em;white-space:nowrap}
/* ---------- editing + guides (never exported) ---------- */
body.editing .ab .tx{cursor:text}
body.editing .ab .tx:hover{outline:1px dashed var(--blue)}
body.editing .ab img,body.editing .ab .xwin{cursor:copy}
.ab [contenteditable]:focus{outline:2px solid var(--acc)}
.guide{position:absolute;pointer-events:none;z-index:50}
.guide.margin{border:1px dashed #FF5FEB}
.guide.safe{background:rgba(255,95,235,.14);border-top:1px dashed #FF5FEB;border-bottom:1px dashed #FF5FEB}
.toast{position:fixed;left:50%;bottom:24px;transform:translate(-50%,8px);background:#000;color:#fff;font:500 12px/1.4 var(--ui);padding:10px 16px;border-left:4px solid var(--acc);max-width:calc(100vw - 32px);opacity:0;transition:opacity .2s,transform .2s;z-index:80;pointer-events:none}
.toast.show{opacity:1;transform:translate(-50%,0)}
/* ---------- responsive ---------- */
@media (max-width:1280px){.topbar .brand span{display:none}}
@media (max-width:1060px){
  #btn-menu{display:block}
  .sidebar{transform:translateX(-100%);transition:transform .2s;z-index:40;width:min(300px,86vw);box-shadow:0 0 40px rgba(0,0,0,.2)}
  body.nav-open .sidebar{transform:none}
  body.nav-open .scrim{display:block;position:fixed;inset:var(--top) 0 0 0;background:rgba(0,0,0,.35);z-index:35}
  .canvas{margin-left:0;padding:0 24px 96px}.hero{margin:0 -24px 56px;padding:40px 24px;grid-template-columns:1fr}.hero-art{display:none}.guide-head{margin:0 -24px 48px;padding:40px 24px}
  .accents span{display:none}
  .side-views{display:flex}
  .seg,.sep{display:none}
}
@media (max-width:640px){
  .topbar .mark{margin-right:8px}.topbar .brand b,#btn-guides,#btn-save,#btn-figma{display:none}
  .canvas{padding:0 16px 80px}.hero{margin:0 -16px 48px;padding:32px 16px}.hero h1,.guide-head h1{font-size:38px}.guide-head{margin:0 -16px 40px;padding:32px 16px}.views,.accents{display:none}
  .sec-num{font-size:56px;min-width:0}.sec-head h2{font-size:30px}.sec-body{gap:16px}
  .frame-tools{opacity:1;transform:none}
}
@media (hover:none){.frame-tools{opacity:1;transform:none}}
/* ---------- Figma import view: true size, no chrome ---------- */
body.figma .topbar,body.figma .sidebar,body.figma .sec-head,body.figma .frame-meta,body.figma .frame-tools,body.figma .scrim,body.figma .hero,body.figma .guide-head{display:none}
body.figma .canvas{margin:0;padding:60px}
body.figma .frames{gap:120px}
body.figma .ab-wrap{box-shadow:none}
body.figma,body.figma .canvas{background:#fff}
body.figma .toast{z-index:95}
.figma-bar,.figma-title{display:none}
body.figma .figma-bar{display:flex;position:fixed;top:0;left:0;right:0;z-index:90;align-items:center;gap:16px;padding:12px 16px;background:#000;color:#fff;font-size:12px}
.figma-bar b{white-space:nowrap;font:400 13px/1 var(--head);letter-spacing:.08em;text-transform:uppercase}
.chips-row{display:flex;gap:4px;overflow-x:auto;flex:1;scrollbar-width:thin}
.fchip{font:500 12px/1 var(--ui);height:34px;padding:0 12px;border:1px solid #3A3A3A;background:transparent;color:#fff;cursor:pointer;white-space:nowrap}
.fchip:hover{border-color:#fff}.fchip.on{background:var(--blue);border-color:var(--blue)}
.figma-bar kbd{font:400 10px var(--ui);border:1px solid currentColor;padding:1px 4px;margin-left:4px}
body.figma .canvas{padding-top:110px}
body.figma .figma-title{display:block;font:400 40px/1 var(--head);text-transform:uppercase;margin:0 0 40px}
body.figma .lib-section{margin-bottom:160px;padding-top:0;padding-bottom:0}
@media print{.figma-bar,.topbar,.sidebar,.sec-head,.frame-meta,.frame-tools,.hero,.guide-head{display:none}.canvas{margin:0;padding:0}.frame{break-after:page}}
"""

JS = (open(HERE / 'export.js').read() + '\n' + open(HERE / 'app.js').read()).replace('__MARGINS__', json.dumps(MARGINS))
JS += "\n" + open(HERE / 'views.js').read().replace('__ACCENTS__', json.dumps([{'key': k, 'name': n, 'acc': a, 'tint': t} for k, n, a, t, _ in ACCENTS]))

CHIPS = ''.join(f'<button class="chip" data-hex="{h}" title="Copy {h}"><s style="background:{h}"></s><span><b>{n}</b>{h}</span></button>' for n, h, *_ in PALETTE)
PAIRS = ''.join(f'<div class="pair" style="background:{bg}" title="Logo {fg} on {bg}">{svg_logo(EM["inner"], EM["w"], EM["h"], fg)}</div>' for bg, fg in PAIRS_OK)
RULES = f"""
<div class="rules" data-name="Brand rules">
  <div class="side-h">Brand rules</div>
  <div class="rule"><h4>Colour</h4><div class="chips">{CHIPS}</div><p>Super Blue leads, Base Gray supports, the four tertiaries are accents. Click a chip to copy its HEX.</p></div>
  <div class="rule"><h4>Approved logo pairs</h4><div class="pairs">{PAIRS}</div><p>Never: pink with turquoise, purple on blue or black, turquoise on gray.</p></div>
  <div class="rule"><h4>Type</h4>
    <div class="sample">What’s next</div><div class="sample2">Roboto for sub-headers and body.</div>
    <dl class="kv"><dt>Headline</dt><dd>N27 Regular, UPPERCASE. Now: {HEAD_NAME}.</dd><dt>Statement</dt><dd>Roboto Bold, sentence case</dd><dt>Sub-heads</dt><dd>Roboto Regular / Bold</dd><dt>Scale</dt><dd>1.5× per level (perfect fifth)</dd></dl></div>
  <div class="rule"><h4>Secondary colour (experiment)</h4><p>Electric Azure, sampled from NEXA’s own backgrounds and MWC visuals, is the default. Switch it live in the top bar to compare with the brandbook turquoise.</p></div>
  <div class="rule"><h4>Containers</h4><dl class="kv"><dt>Shape</dt><dd>Rectangle, top-left + bottom-right corners cut</dd><dt>Cut</dt><dd>≈16% of the short side, slightly steeper than 45°</dd><dt>Live area</dt><dd>Equally inset from every edge</dd></dl></div>
  <div class="rule"><h4>Logo</h4>
    <dl class="kv"><dt>Place</dt><dd>Wordmark bottom-left, emblem top-right</dd><dt>Space</dt><dd>X height on every side</dd><dt>Min</dt><dd>Wordmark 200 px · emblem 50 px</dd></dl></div>
  <div class="rule"><h4>Never</h4><ul>
    <li><i>×</i>Stretch, angle, outline or respace the logo</li><li><i>×</i>Add effects, gradients or elements to it</li>
    <li><i>×</i>Bold or lowercase N27 headlines</li><li><i>×</i>A blue overlay on every photo</li></ul></div>
</div>
<div class="hint"><b>Copy to Figma</b>Hover any asset and click <strong>Copy SVG</strong>, then press Ctrl/⌘ + V in Figma. For a whole set, open <strong>Figma import view</strong>, pick the set and run your HTML to Figma plugin.</div>
"""

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NEXA brand asset library</title>
<link rel="icon" type="image/svg+xml" href="{FAVICON}">
<style>{FONTS}{CSS}</style>
</head>
<body data-view="library">
<header class="topbar" data-name="App bar">
  <div class="mark">{EM_UI}</div>
  <button class="btn" id="btn-menu" aria-label="Asset sets">Menu</button>
  <div class="brand">{WM_UI}</div>
  <div class="views" role="group" aria-label="View"><button class="btn on" data-view-btn="library">Asset library</button><button class="btn" data-view-btn="guide">Brand guidelines</button></div>
  <span class="spacer"></span><div class="accents" role="group" aria-label="Secondary colour"><span>Secondary</span>{''.join(f'<button data-accent="{k}" title="{n}: {a}" style="background:{a}"></button>' for k, n, a, t, _ in ACCENTS)}</div>
  <div class="seg" role="group" aria-label="Zoom"><button class="btn on" data-zoom="fit">Fit</button><button class="btn" data-zoom="0.25">25%</button><button class="btn" data-zoom="0.5">50%</button><button class="btn" data-zoom="1">100%</button></div>
  <span class="sep"></span>
  <button class="btn" id="btn-guides" title="Show margins and story safe zones">Guides</button>
  <button class="btn" id="btn-edit" title="Edit text and replace images">Edit</button>
  <button class="btn" id="btn-save" title="Save a self-contained copy with your edits">Save file</button>
  <button class="btn primary" id="btn-figma" title="True size, no labels: use this view for HTML to Figma import">Figma import view</button>
</header>
<nav class="sidebar" data-name="Sections">
  <div class="side-views"><button data-view-btn="library">Asset library</button><button data-view-btn="guide">Brand guidelines</button></div>
  <div class="side-h" data-view="library">Asset sets</div><div class="side-h" data-view="guide">Brand guidelines</div>
  {''.join(nav)}
  {RULES}
</nav>
<div class="scrim"></div>
<div class="figma-bar" data-name="Figma view bar">
  <b>Figma import view</b>
  <div class="chips-row"><button class="fchip on" data-only="">All</button>{''.join(f'<button class="fchip" data-only="{sid}">{esc(t)}</button>' for sid, t in ALL_META)}</div>
  <button class="btn" id="btn-exit-figma">Exit <kbd>Esc</kbd></button>
</div>
<main class="canvas" data-name="Canvas">
<div class="hero" data-view="library">
  <svg class="wmk" viewBox="0 0 {EM['w']} {EM['h']}" fill="currentColor" aria-hidden="true">{EM['inner']}</svg>
  <div>
    <div class="kicker">NEXA · BRAND ASSET LIBRARY</div>
    <h1>One brand.<br>Every channel.</h1>
    <p>{N_LIB} ready-to-use assets for NEXA, led by social: posts, carousels, stories and LinkedIn, plus slides, web and stationery. Edit any of them in the browser, or copy them into Figma. The rules live under <b>Brand guidelines</b>.</p>
    <div class="set-tiles">{''.join(tiles)}</div>
  </div>
  <div class="hero-art" aria-hidden="true">{HERO_ART}</div>
</div>
<div class="guide-head" data-view="guide">
  <svg class="wmk" viewBox="0 0 {EM['w']} {EM['h']}" fill="currentColor" aria-hidden="true">{EM['inner']}</svg>
  <div class="kicker">NEXA · BRAND GUIDELINES</div>
  <h1>The rules behind<br>every asset.</h1>
  <p>{N_GUIDE} boards from the NEXA Brand Guidelines v1.0 and the NEXA Figma visual identity: logo, colour, type, graphic devices, imagery, containers and the secondary colour study.</p>
</div>
{''.join(sections_html)}
</main>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script id="img-data" type="application/json">{json.dumps(IMG)}</script>
<script>{JS}</script>
</body>
</html>"""
out = HERE.parent / 'dist' / 'NEXA_Brand_Asset_Library.html'
out.parent.mkdir(exist_ok=True)
open(out, 'w').write(page)
print(round(len(page) / 1e6, 2), 'MB', N_LIB, 'assets +', N_GUIDE, 'boards · headline font:', HEAD_NAME)
