#!/usr/bin/env python3
"""Builds pradeep-seo-single-file.md: the whole skill as one text file, for tools without skill support
(paste into custom instructions, a Project, a custom GPT, or AGENTS.md). Run from the skill folder."""
import os, re
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
body = re.sub(r"^---.*?---\s*", "", open(os.path.join(root, "SKILL.md")).read(), flags=re.S)
body = body.replace("references/", "## MODULE: ").replace(".md", "")
parts = ["# Pradeep SEO (single-file edition)\n\nMIT License. Copyright (c) 2026 Pradeep Mishra.\n\nNo scripts or files are available in this edition. Ask the user to paste page HTML, robots.txt or sitemap content, then apply the checks by hand. Module sections are below; follow the matching section.\n\n", body, "\n\n---\n"]
for f in sorted(os.listdir(os.path.join(root, "references"))):
    t = open(os.path.join(root, "references", f)).read().strip()
    parts.append("\n" + t.replace("# ", "## MODULE: ", 1) + "\n\n---\n")
open(os.path.join(os.path.dirname(root), "pradeep-seo-single-file.md"), "w").write("".join(parts))
print("written")
