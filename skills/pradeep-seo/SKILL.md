---
name: pradeep-seo
description: SEO toolkit to audit a URL or HTML for technical, on-page, content (E-E-A-T), schema, GEO/AI search, local, hreflang and sitemap issues with a 0-100 score. Use for any SEO or website audit question.
license: MIT
---

# Pradeep SEO

Practical SEO analysis for a website or a single page. Every finding needs evidence (the tag, URL or text found), why it matters, and a concrete fix. Works from a URL, pasted HTML, an uploaded file, or exports the user provides.

## Commands

The user may type `/pradeep <command> <url>` or just describe the task. Pick the module, then read its file before answering. If several apply, read each. If the request is vague ("check my SEO"), run **audit**.

| Command | Use it for | Read |
|---|---|---|
| audit | full check with 0-100 score | references/audit.md |
| page | deep single-page analysis | references/page.md |
| technical | crawl, indexing, robots, speed hints | references/technical.md |
| content | E-E-A-T and content quality | references/content.md |
| schema | detect, validate, generate JSON-LD | references/schema.md |
| sitemap | analyze or build XML sitemaps | references/sitemap.md |
| images | image optimization | references/images.md |
| geo | AI Overviews, ChatGPT, Perplexity visibility | references/geo.md |
| agentic | AI agent readiness, llms.txt | references/agentic.md |
| local | Google Business Profile, citations, reviews | references/local.md |
| maps | geo-grid and map pack analysis (needs data) | references/maps.md |
| plan | 90-day strategy by site type | references/plan.md |
| programmatic | template pages at scale, quality gates | references/programmatic.md |
| competitor-pages | "X vs Y" and alternatives pages | references/competitor-pages.md |
| hreflang | international / multi-language SEO | references/hreflang.md |
| flow | staged SEO workflow, step by step | references/flow.md |
| backlinks | link profile review (needs export) | references/backlinks.md |
| google | Search Console, PageSpeed, CrUX, GA4 data | references/google.md |
| cluster | keyword and topic clusters | references/cluster.md |
| drift | detect SEO changes after releases | references/drift.md |
| sxo | search experience vs intent | references/sxo.md |
| ecommerce | product and category SEO | references/ecommerce.md |
| dataforseo | live SERP/keyword data (optional, needs account) | references/dataforseo.md |
| image-gen | SEO image briefs/generation (optional) | references/image-gen.md |
| firecrawl | full-site crawl analysis (optional) | references/firecrawl.md |

## Getting the data

Scripts (Python 3, standard library only) live in `scripts/`:
- `python scripts/page_check.py <url>` or `--file page.html`: page facts as JSON
- `python scripts/robots_check.py <site-url> [paths]`: robots.txt rules and sitemap lines
- `python scripts/sitemap_check.py <sitemap-url>` or `--file`: sitemap health
- `python scripts/schema_gen.py <Type> '<json facts>'`: JSON-LD from facts you give it
- `python scripts/drift.py baseline|compare <url>`: before/after snapshots

If you cannot run code or have no network: ask the user to paste the page source (View Source), robots.txt, or sitemap, or upload files, then read them directly and apply the same checks by hand. Say plainly which checks you could not do. Never guess values you did not see.

## Rules

- Never claim rankings, traffic, search volume, backlinks or speed scores unless the user supplied them or a real tool returned them.
- Keep verified facts separate from inferences; label hypotheses.
- Prioritize fixes High / Medium / Low by impact and effort.
- Do not invent reviews, ratings, credentials, prices, addresses or competitor facts.
- No guarantees ("will rank #1", "will get a rich result"). Use "improves the odds".
- Keep reports short: top issues first.

## Output format

1. **Score** (0-100) when a full audit is requested, with the point breakdown
2. **Top 5 fixes**, High priority first
3. **Findings** by area, each: Evidence, Why it matters, Fix
4. **What I could not check** (speed, backlinks, Search Console data, etc.)
