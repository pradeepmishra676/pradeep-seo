#!/usr/bin/env python3
"""Pradeep SEO page parser. Usage: page_check.py <url> | --file <path>. Prints JSON. Stdlib only."""
import sys, json, re, urllib.request
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(s):
        super().__init__()
        s.d = dict(title="", meta={}, canonical=None, lang=None, viewport=None,
                   headings=[], images=0, images_with_alt=0, links_internal=0,
                   links_external=0, generic_anchors=0, jsonld=[], og={}, hreflang=[], text=[])
        s._t = s._h = s._ld = s._a = None; s._buf = ""; s._skip = 0
    def handle_starttag(s, tag, a):
        a = dict(a)
        if tag == "html": s.d["lang"] = a.get("lang")
        elif tag == "title": s._t = True
        elif tag == "meta":
            n = (a.get("name") or a.get("property") or "").lower()
            if n == "viewport": s.d["viewport"] = a.get("content")
            if n.startswith(("og:", "twitter:")): s.d["og"][n] = a.get("content")
            elif n: s.d["meta"][n] = a.get("content")
        elif tag == "link":
            r = (a.get("rel") or "").lower()
            if r == "canonical": s.d["canonical"] = a.get("href")
            if r == "alternate" and a.get("hreflang"): s.d["hreflang"].append(a["hreflang"])
        elif tag in ("h1","h2","h3","h4"): s._h = tag; s._buf = ""
        elif tag == "img":
            s.d["images"] += 1
            if (a.get("alt") or "").strip(): s.d["images_with_alt"] += 1
        elif tag == "a":
            h = a.get("href") or ""; s._a = True; s._buf = ""
            if h.startswith(("http://","https://","//")): s.d["links_external"] += 1
            elif h and not h.startswith(("#","mailto:","tel:","javascript:")): s.d["links_internal"] += 1
        elif tag == "script" and (a.get("type") or "").lower() == "application/ld+json": s._ld = True; s._buf = ""
        elif tag in ("script","style","noscript"): s._skip += 1
    def handle_endtag(s, tag):
        if tag == "title": s._t = None
        elif tag == s._h: s.d["headings"].append([tag, s._buf.strip()]); s._h = None
        elif tag == "a" and s._a:
            if s._buf.strip().lower() in ("click here","here","read more","more","link"): s.d["generic_anchors"] += 1
            s._a = None
        elif tag == "script" and s._ld: s.d["jsonld"].append(s._buf); s._ld = None
        elif tag in ("script","style","noscript") and s._skip: s._skip -= 1
    def handle_data(s, t):
        if s._t: s.d["title"] += t
        if s._h or s._a or s._ld: s._buf += t
        if not s._skip and not s._ld: s.d["text"].append(t)

def analyze(html, src):
    p = P(); p.feed(html); d = p.d
    types = []
    for raw in d.pop("jsonld"):
        try:
            j = json.loads(raw)
            for it in (j if isinstance(j, list) else j.get("@graph", [j])):
                t = it.get("@type"); types += t if isinstance(t, list) else [t]
        except Exception: types.append("INVALID_JSON")
    words = len(re.findall(r"\w+", " ".join(d.pop("text"))))
    out = dict(source=src, title=d["title"].strip(), title_length=len(d["title"].strip()),
        meta_description=d["meta"].get("description"), robots_meta=d["meta"].get("robots"),
        canonical=d["canonical"], lang=d["lang"], viewport=d["viewport"],
        h1_count=sum(1 for h in d["headings"] if h[0]=="h1"), headings=d["headings"][:40],
        images=d["images"], images_with_alt=d["images_with_alt"],
        links_internal=d["links_internal"], links_external=d["links_external"],
        generic_anchor_links=d["generic_anchors"], schema_types=[t for t in types if t],
        open_graph=d["og"], hreflang=d["hreflang"], word_count=words)
    return out

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    if sys.argv[1] == "--file":
        html = open(sys.argv[2], encoding="utf-8", errors="replace").read(); src = sys.argv[2]
    else:
        src = sys.argv[1]
        req = urllib.request.Request(src, headers={"User-Agent": "PradeepSEO/1.0"})
        html = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
    print(json.dumps(analyze(html, src), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
