#!/usr/bin/env python3
"""Pradeep SEO JSON-LD generator. Usage: schema_gen.py <Type> '<json of facts>'
Types: Organization LocalBusiness Article Product FAQPage BreadcrumbList WebSite
Only the facts you pass are used; nothing is invented. Missing recommended fields are listed on stderr."""
import sys, json
REQ = {"Organization": ["name", "url"], "LocalBusiness": ["name", "address", "telephone"],
       "Article": ["headline", "author", "datePublished"], "Product": ["name", "offers"],
       "FAQPage": ["faqs"], "BreadcrumbList": ["items"], "WebSite": ["name", "url"]}
def main():
    if len(sys.argv) < 3 or sys.argv[1] not in REQ: sys.exit(__doc__)
    t, f = sys.argv[1], json.loads(sys.argv[2])
    miss = [k for k in REQ[t] if k not in f]
    if miss: print("Missing recommended fields:", ", ".join(miss), file=sys.stderr)
    d = {"@context": "https://schema.org", "@type": t}
    if t == "FAQPage":
        d["mainEntity"] = [{"@type": "Question", "name": q["q"], "acceptedAnswer": {"@type": "Answer", "text": q["a"]}} for q in f.get("faqs", [])]
    elif t == "BreadcrumbList":
        d["itemListElement"] = [{"@type": "ListItem", "position": i + 1, "name": it["name"], "item": it["url"]} for i, it in enumerate(f.get("items", []))]
    else:
        d.update(f)
    print(json.dumps(d, ensure_ascii=False, indent=2))
main()
