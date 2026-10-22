# SEO log

## 2026-10-20
- Rebuilt site (40 pages) in topdispatchcrm.com design; flat file structure for reliable Vercel deploys.
- Deepened all 8 service pages (~1,250 words) and 14 industry pages (~850-1,100 words): playbooks, intake questions, emergency rules, KPIs, extra FAQs.
- New landing pages: /call-center-services, /answering-service.
- Pending (owner): point topdispatchcrm.com to Vercel, Google Search Console + sitemap, Google Business Profile, directory listings.
- Next: guide "How much does a virtual receptionist cost", then city pages for top HVAC/plumbing metros.

## 2026-10-22: Re-audit and fixes
- Competitor research: SERPs for "HVAC answering service", "virtual receptionist cost", "Filipino virtual receptionist" are led by AI-receptionist vendors (Retell, CloudTalk, Rosie, Goodcall), live services (Smith.ai, Ruby, AnswerConnect, AnswerForce, Nexa), Philippine VA agencies (Stealth Agents, OurAssistants) and "best X" listicles. They publish price ranges and comparison tables.
- Added "Sources & further reading" with authoritative external links (BLS, FTC, FCC, CPSC, EPA, SBA, IRS, EF EPI, IBPAP, trade associations) to all service, industry, landing, guide and hub pages, with "Last updated" date.
- Contextual internal links added automatically inside page copy (_src/links.py LINK_MAP), 5-10 per page.
- Pricing page + cost guide: US market cost table (BLS receptionist median $18.27/hr, $38,010/yr, May 2025; published answering-service and AI ranges). Cost guide expanded to ~1,050 words (cost per booked job, price drivers, questions to ask).
- Industry pages: trade-specific service cards instead of the same six on every page. Footer logo alt text.
- CRITICAL still open: topdispatchcrm.com serves the Base44 CRM, while every page canonical points there. Owner must either move the CRM to a subdomain and point the root domain to Vercel, or choose a different domain.
- Next: "Best answering service for HVAC companies (2026)" comparison guide; city pages.
