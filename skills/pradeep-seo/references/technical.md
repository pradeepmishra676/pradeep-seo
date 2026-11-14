# Technical module

Check, in order, using page_check output and anything the user provides:

1. HTTPS and redirects: the page loads on https; http redirects to it; no mixed content visible in the HTML.
2. Indexability: robots meta, canonical, and (if you can fetch it) /robots.txt rules that block important paths.
3. Sitemap: look for a Sitemap line in robots.txt or /sitemap.xml; check it lists canonical, indexable URLs only.
4. URL hygiene: short, readable, lowercase, hyphens; flag session IDs and long parameter strings.
5. Mobile: viewport meta present; no fixed-width layout hints in HTML.
6. Performance hints visible in HTML: very large inline scripts, many render-blocking scripts in head, images without width/height, no lazy loading on below-the-fold images. Say these are hints, not measured speed.
7. International: if multiple languages, check hreflang pairs are reciprocal and include a self reference.
8. Structured and social tags: see schema.md and the Open Graph fields.
9. Duplicate risk: trailing-slash and www/non-www variants, printable versions, parameter pages without canonical.

Real speed (Core Web Vitals) needs PageSpeed Insights or Search Console data; ask the user for it rather than guessing.
