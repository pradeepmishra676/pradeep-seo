#!/usr/bin/env python3
"""Pradeep SEO drift monitor. Usage: drift.py baseline <url|--file path> | compare <url|--file path>
Saves a page snapshot to .pradeep-seo/ and later reports on-page SEO changes."""
import sys, os, json, hashlib, urllib.request
sys.path.insert(0, os.path.dirname(__file__))
from page_check import analyze
def get(args):
    if args[0] == "--file": return open(args[1], encoding="utf-8", errors="replace").read(), args[1]
    return urllib.request.urlopen(urllib.request.Request(args[0], headers={"User-Agent": "PradeepSEO/1.0"}), timeout=20).read().decode("utf-8", "replace"), args[0]
def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("baseline", "compare"): sys.exit(__doc__)
    html, src = get(sys.argv[2:]); cur = analyze(html, src)
    os.makedirs(".pradeep-seo", exist_ok=True)
    path = ".pradeep-seo/" + hashlib.md5(src.encode()).hexdigest()[:10] + ".json"
    if sys.argv[1] == "baseline":
        json.dump(cur, open(path, "w")); print("Baseline saved:", path); return
    if not os.path.exists(path): sys.exit("No baseline found. Run baseline first.")
    old = json.load(open(path))
    ch = {k: {"before": old.get(k), "after": cur.get(k)} for k in cur if k != "source" and old.get(k) != cur.get(k)}
    print(json.dumps(ch or {"result": "No on-page SEO changes since baseline"}, indent=2, ensure_ascii=False))
main()
