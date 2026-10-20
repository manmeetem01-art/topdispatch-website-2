# Top Dispatch website

Static site: 38 pages, no build step. Deploys as-is to Vercel, Netlify or any static host.

## Deploy to Vercel
1. Push this folder to a GitHub repo (or run `npx vercel` inside it).
2. In Vercel: New Project, import the repo, Framework preset "Other", no build command, output directory `.`
3. Add the domain topdispatchcrm.com in Project Settings > Domains.
4. Submit https://topdispatchcrm.com/sitemap.xml in Google Search Console and Bing Webmaster Tools.

`vercel.json` already sets clean URLs, trailing slashes, caching, security headers and 301 redirects from the old Base44 URLs (/ServicesPage, /AboutPage, /ReviewsPage, /FAQPage, /IndustriesPage, /ContactPage).

## Lead form
`contact/index.html` has `<form ... data-endpoint="">`. Paste a Formspree, Web3Forms, Make or n8n webhook URL there.
Until you do, the form opens the visitor's email app addressed to support@topdispatchcrm.com.

## Editing content
All copy lives in `_generator/content.py` (services, industries, reviews) and `_generator/build.py` (page layouts, FAQs, guides).
Edit, then run `python3 _generator/build.py` after changing `OUT` at the top of build.py to this folder's path.
