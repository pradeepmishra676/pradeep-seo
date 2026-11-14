#!/usr/bin/env python3
"""Pradeep SEO robots.txt check. Usage: robots_check.py <site-url> [path ...] | --file <robots.txt> [path ...]. Prints JSON."""
import sys, json, urllib.request, urllib.robotparser
def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    if a[0] == "--file":
        txt = open(a[1], encoding="utf-8", errors="replace").read(); base = "https://example.com"; paths = a[2:]
    else:
        base = a[0].rstrip("/"); paths = a[1:]
        req = urllib.request.Request(base + "/robots.txt", headers={"User-Agent": "PradeepSEO/1.0"})
        txt = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
    rp = urllib.robotparser.RobotFileParser(); rp.parse(txt.splitlines())
    lines = [l.strip() for l in txt.splitlines()]
    sitemaps = [l.split(":", 1)[1].strip() for l in lines if l.lower().startswith("sitemap:")]
    flags = []
    cur = None
    for l in lines:
        low = l.lower()
        if low.startswith("user-agent:"): cur = l.split(":", 1)[1].strip()
        if low.replace(" ", "") == "disallow:/": flags.append(f"Site-wide block for user-agent '{cur}'")
    if not sitemaps: flags.append("No Sitemap: line found")
    checks = {p: rp.can_fetch("*", base + p) for p in paths}
    print(json.dumps(dict(sitemaps=sitemaps, flags=flags, path_allowed_for_all_bots=checks, lines=len(lines)), indent=2))
main()
