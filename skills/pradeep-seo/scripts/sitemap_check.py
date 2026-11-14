#!/usr/bin/env python3
"""Pradeep SEO sitemap check. Usage: sitemap_check.py <sitemap-url> | --file <sitemap.xml>. Prints JSON."""
import sys, json, urllib.request, xml.etree.ElementTree as ET
from collections import Counter
def load(src, is_file):
    if is_file: return open(src, "rb").read()
    return urllib.request.urlopen(urllib.request.Request(src, headers={"User-Agent": "PradeepSEO/1.0"}), timeout=20).read()
def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    is_file = a[0] == "--file"; src = a[1] if is_file else a[0]
    root = ET.fromstring(load(src, is_file))
    tag = lambda e: e.tag.split("}")[-1]
    out = dict(source=src, type="sitemapindex" if tag(root) == "sitemapindex" else "urlset")
    if out["type"] == "sitemapindex":
        out["child_sitemaps"] = [e.findtext("{*}loc") for e in root.findall("{*}sitemap")]
    else:
        urls = [e.findtext("{*}loc") for e in root.findall("{*}url")]
        lastmods = [e.findtext("{*}lastmod") for e in root.findall("{*}url")]
        dup = [u for u, c in Counter(urls).items() if c > 1]
        out.update(url_count=len(urls), over_50000_limit=len(urls) > 50000,
            non_https=[u for u in urls if u and not u.startswith("https://")][:20],
            with_parameters=[u for u in urls if u and "?" in u][:20], duplicates=dup[:20],
            lastmod_present=sum(1 for l in lastmods if l), sample=urls[:5])
    print(json.dumps(out, indent=2))
main()
