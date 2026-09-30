import pymupdf as fitz, json, sys
PDF=sys.argv[1]; OUT=sys.argv[2]
d=fitz.open(PDF)
def pathd(dr,ox,oy):
    s=[];cur=None
    for it in dr["items"]:
        op=it[0]
        if op=="l":
            a,b=it[1],it[2]
            if cur is None or abs(cur.x-a.x)>.01 or abs(cur.y-a.y)>.01: s.append(f"M{a.x-ox:.2f} {a.y-oy:.2f}")
            s.append(f"L{b.x-ox:.2f} {b.y-oy:.2f}");cur=b
        elif op=="c":
            a,c1,c2,b=it[1:5]
            if cur is None or abs(cur.x-a.x)>.01 or abs(cur.y-a.y)>.01: s.append(f"M{a.x-ox:.2f} {a.y-oy:.2f}")
            s.append(f"C{c1.x-ox:.2f} {c1.y-oy:.2f} {c2.x-ox:.2f} {c2.y-oy:.2f} {b.x-ox:.2f} {b.y-oy:.2f}");cur=b
    return "".join(s)+"Z"
G=(0.07450000196695328,)*3
def grab(pn, n=None):
    dr=[x for x in d[pn].get_drawings() if x.get("fill")==G]
    if n: dr=dr[:n]
    x0=min(x["rect"].x0 for x in dr); y0=min(x["rect"].y0 for x in dr)
    x1=max(x["rect"].x1 for x in dr); y1=max(x["rect"].y1 for x in dr)
    return [pathd(x,x0,y0) for x in dr], x1-x0, y1-y0
wm,W,H=grab(5)          # A, X-right, N-E-X-left, T, M
em,EW,EH=grab(7,2)      # emblem: two chevrons
# wordmark without TM: first three paths
nt=wm[:3]; import re
NW=max(float(v) for p in nt for v in re.findall(r"[ML ]?(-?\d+\.\d+) -?\d+\.\d+",p))
data={"wordmark":{"w":round(W,2),"h":round(H,2),"d":wm},"wordmark_notm":{"w":round(1756.87-84.0,2),"h":round(H,2),"d":nt},
      "emblem":{"w":round(EW,2),"h":round(EH,2),"d":em}}
json.dump(data,open(OUT+"/logo.json","w"),indent=1)
def svg(k,fill,title):
    v=data[k]; return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {v["w"]} {v["h"]}" role="img" aria-label="{title}">'
      f'<title>{title}</title><g fill="{fill}">'+"".join(f'<path d="{p}"/>' for p in v["d"])+"</g></svg>\n")
for name,fill in [("black","#000000"),("white","#FFFFFF"),("super-blue","#1F1FCC"),("base-gray","#C9C7C9"),("turquoise","#36FFE8")]:
    open(f"{OUT}/nexa-wordmark-{name}.svg","w").write(svg("wordmark",fill,"NEXA"))
    open(f"{OUT}/nexa-emblem-{name}.svg","w").write(svg("emblem",fill,"NEXA emblem"))
print(data["wordmark"]["w"],data["wordmark"]["h"],data["emblem"]["w"],data["emblem"]["h"])
