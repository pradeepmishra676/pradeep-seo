# Pradeep SEO

An SEO toolkit packaged as an Agent Skill (`SKILL.md` open format). Give your AI assistant a URL or the page's HTML and it audits technical SEO, on-page, content quality (E-E-A-T), schema, AI-search (GEO) readiness, local SEO, hreflang, sitemaps and more, with a 0-100 score and prioritized fixes.

## Install

Menu names change over time, so check each product's current Skills help page if a step looks different.

**Claude (claude.ai) and ChatGPT:** download `pradeep-seo.zip` from the [latest release](../../releases/latest), then upload it in Settings, Skills (Claude) or Skills, Create, Upload from your computer (ChatGPT). Custom skills need a plan that supports them.

**Claude Code and other Agent Skills tools:** copy the `skills/pradeep-seo` folder to `~/.claude/skills/` (all projects) or `.claude/skills/` (one project), then restart the session.

**Tools without skill support:** add `pradeep-seo-single-file.md` as a Project file, Knowledge file or `AGENTS.md`. It is about 24 KB, so it will not fit short custom-instruction boxes, and scripts will not run there. Paste the page HTML instead.

## Use it

- `/pradeep audit https://example.com` or "audit my site"
- `/pradeep page <url>`, `/pradeep schema <url>`, `/pradeep geo <url>` ...

## What's inside

25 modules in `skills/pradeep-seo/references/`: audit, page, technical, content, schema, sitemap, images, geo, agentic, local, maps, plan, programmatic, competitor-pages, hreflang, flow, backlinks, google, cluster, drift, sxo, ecommerce, dataforseo, image-gen, firecrawl. Python 3 helper scripts (standard library only) are in `skills/pradeep-seo/scripts/`.

## Limits

- Scripts need Python 3 and network access to fetch live URLs. Many chat sandboxes have no network; paste the HTML instead.
- It cannot see rankings, traffic, backlinks or real speed scores unless you provide exports or connect a tool. It is built not to invent them.
- Modules `maps`, `backlinks`, `google`, `dataforseo`, `firecrawl` and `image-gen` need your own data, accounts or tools.
- Advice improves the odds; nothing here guarantees rankings or AI citations.

## License

MIT License. Copyright (c) 2026 Pradeep Mishra. See [LICENSE](LICENSE).
