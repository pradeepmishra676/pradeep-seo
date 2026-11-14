# Drift monitoring module
Purpose: catch unintended on-page SEO changes (title, meta, canonical, robots meta, headings, schema, hreflang) after releases.
Use: `python scripts/drift.py baseline <url>` saves a snapshot in .pradeep-seo/; later `python scripts/drift.py compare <url>` lists before/after changes. Works on a local folder of snapshots; it does not run in the background.
Interpret: mark each change as expected, needs review, or likely harmful (e.g. noindex added, canonical changed, H1 removed, schema lost). Suggest running compare after every deploy.
