# Manmeet-CRM: Top Dispatch website

Instructions for Claude (Cowork / Claude Code) working in this repo. Read this before every change.

## What this is
Marketing site for Top Dispatch (brand of topdispatchcrm.com): dedicated remote receptionists,
dispatchers and call center agents from the Philippines for US home service businesses.
Goal: rank #1 in the USA and generate leads from businesses that want to hire a call center,
answering service or receptionist. Every page must be SEO, AEO and GEO optimised.

- Live: https://topdispatch-website-2.vercel.app (Vercel auto-deploys every push to `main`)
- Final domain: https://topdispatchcrm.com (canonical URLs already use it)
- Phone (833) 505-4136 · support@topdispatchcrm.com · Beverly Hills, CA 90212

## Golden rules
1. Never ask the owner to download or upload files. Edit here, commit, push to `main`.
2. Never edit the root `*.html` files by hand. They are generated. Edit `_src/`, then run `_src/build.sh`.
3. Keep the design exactly as it is (dark navy, cyan-to-blue gradient, Inter, pill buttons, logo).
4. After every push, open the live site and check the changed pages return 200 and look right.
5. Log what you did in `SEO-LOG.md` (date, pages changed, keywords targeted).

## How the site is built
- `_src/content.py`: services, industries, reviews, contact details.
- `_src/deep_services.py`, `_src/deep_industries.py`: long-form sections per service / industry.
- `_src/build.py`: page templates, FAQs, guides (`GUIDES` list), landing pages, schema, sitemap, llms.txt.
- `_src/flatten.py`: writes flat files to the repo root (`services-dispatch.html` etc.) and the
  `vercel.json` rewrites that map `/services/dispatch` to them. The flat layout exists because
  folder uploads broke an earlier deploy. Keep it.
- Run: `sh _src/build.sh` then `git add -A && git commit -m "..." && git push`.

## Adding a page
- New guide: add a dict to `GUIDES` in `_src/build.py` (slug, title, h1a, h1b, meta, lead, answer, sections).
- New service / industry: add to `content.py` and its deep file. Links, sitemap, schema and rewrites update automatically.
- Every page needs: unique title (<=60 chars + " | Top Dispatch"), meta description (<=155 chars),
  one H1, a 40-60 word direct answer box, 6+ FAQs, internal links to 3+ related pages.

## Content standards
- 1,500+ words for money pages and guides. Specific and practical: real call scripts, intake
  questions, emergency rules, KPIs, examples. No filler, no invented statistics, cite real sources.
- Write for US home service owners. Plain English, short sentences, active voice.
- Never invent reviews, client names or results. Pricing stays "flat monthly fee, get a quote".

## Daily SEO task
1. Read `SEO-LOG.md` to see what was done last.
2. Do one main task, rotating through:
   - a new 1,500+ word guide targeting a buyer keyword (e.g. "virtual receptionist cost",
     "answering service for HVAC", "call center vs virtual receptionist", "best answering service for plumbers")
   - a city page for a high-value US metro (e.g. "HVAC answering service Dallas") with genuinely local detail
   - deepen one existing page and add internal links to it
3. Rebuild, check links, commit, push, verify live, update `SEO-LOG.md`.
4. Report back to the owner in Hinglish: what changed, live URLs, next suggested task.
