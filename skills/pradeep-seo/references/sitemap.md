# Sitemap module
Analyze: run `python scripts/robots_check.py <site>` to find sitemap lines, then `python scripts/sitemap_check.py <sitemap-url>`.
Check: only canonical, indexable, https URLs; no duplicates; no parameter URLs; under 50,000 URLs and 50 MB per file (use a sitemap index beyond that); lastmod present and truthful; no redirected, 404 or noindex URLs (spot-check a sample).
Generate: when asked, build XML from a URL list the user provides, with correct namespace, and tell them to reference it in robots.txt and submit it in Search Console. Never add URLs you were not given.
