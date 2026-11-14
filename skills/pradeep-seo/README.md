# Pradeep SEO

An SEO toolkit packaged as an Agent Skill (`SKILL.md` open format). Give your AI assistant a URL or the page's HTML and it audits technical SEO, on-page, content quality (E-E-A-T), schema, AI-search (GEO) readiness, local SEO, hreflang, sitemaps and more, with a 0-100 score and prioritized fixes.

## What's inside

- `SKILL.md` : router and rules
- `references/` : 25 modules (audit, page, technical, content, schema, sitemap, images, geo, agentic, local, maps, plan, programmatic, competitor-pages, hreflang, flow, backlinks, google, cluster, drift, sxo, ecommerce, dataforseo, image-gen, firecrawl)
- `scripts/` : Python 3 helpers (page_check, robots_check, sitemap_check, schema_gen, drift). Standard library only.
- `LICENSE` : MIT

Also distributed as `pradeep-seo.zip` (upload-ready, one skill folder at the root) and `pradeep-seo-single-file.md` (everything in one text file for tools without skill support).

## Install

Menu names change over time, so check each product's current Skills help page if a step looks different.

**Claude (claude.ai):** Settings, Skills (under Features or Capabilities), upload `pradeep-seo.zip`. Needs a plan that supports custom skills with code execution enabled.

**Claude Code:** copy the `pradeep-seo` folder to `~/.claude/skills/` (all projects) or `.claude/skills/` (one project). Restart the session.

**ChatGPT:** Skills, Create, Upload from your computer, choose `pradeep-seo.zip`. ChatGPT scans uploaded skills, so a review step may appear. Availability depends on your plan and workspace settings.

**Codex and other agents that support Agent Skills:** place the `pradeep-seo` folder in that tool's skills directory (many also read `.claude/skills/` or `.agents/skills/`).

**Tools without skill support:** add `pradeep-seo-single-file.md` as a Project file, Knowledge file or `AGENTS.md`. It is about 24 KB, so it will not fit short custom-instruction boxes. Scripts will not run there, so paste the page HTML and the assistant applies the checks by hand.

## Use it

- `/pradeep audit https://example.com` or "audit my site"
- `/pradeep page <url>`, `/pradeep schema <url>`, `/pradeep geo <url>` ...
- Or just describe the task: "check my product page's schema".

## Limits (read this)

- Scripts need Python 3 and network access to fetch live URLs. Many chat sandboxes have no network; paste the HTML instead.
- It cannot see rankings, traffic, backlinks or real speed scores unless you provide exports or connect a tool. It is built not to invent them.
- Modules `maps`, `backlinks`, `google`, `dataforseo`, `firecrawl` and `image-gen` need your own data, accounts or tools.
- Advice improves the odds; nothing here guarantees rankings or AI citations.

## License

MIT License. Copyright (c) 2026 Pradeep Mishra. See `LICENSE`.
