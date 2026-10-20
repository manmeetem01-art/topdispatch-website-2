# -*- coding: utf-8 -*-
import json, os, html, datetime
from content import *

OUT = "/home/claude/site"
TODAY = "2026-10-20"
E = html.escape

# ---------- icons (lucide-style strokes) ----------
P = {
 "phone":'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 "activity":'<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
 "headphones":'<path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/>',
 "workflow":'<rect x="3" y="3" width="8" height="8" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect x="13" y="13" width="8" height="8" rx="2"/>',
 "barchart":'<path d="M3 3v18h18"/><path d="M8 17v-5M13 17V8M18 17v-3"/>',
 "shield":'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 "users":'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 "target":'<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
 "award":'<circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/>',
 "clock":'<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "globe":'<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/>',
 "heart":'<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7z"/>',
 "message":'<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22z"/>',
 "dollar":'<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
 "usercheck":'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="m16 11 2 2 4-4"/>',
 "thumbsup":'<path d="M7 10v12M15 5.9 14 10h5.8a2 2 0 0 1 2 2.3l-1.4 8A2 2 0 0 1 18.4 22H7V10l4-8a3 3 0 0 1 4 3.9z"/>',
 "wind":'<path d="M17.7 7.7A2.5 2.5 0 1 1 19.5 12H2M9.6 4.6A2 2 0 1 1 11 8H2M12.6 19.4A2 2 0 1 0 14 16H2"/>',
 "key":'<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6M15.5 7.5l3 3L22 7l-3-3"/>',
 "hammer":'<path d="m15 12-8.4 8.4a2.1 2.1 0 0 1-3-3L12 9M17.6 15 22 10.6M20 11.5l-1.9-1.9a2.4 2.4 0 0 1-.7-1.7V6.7l-2.3-2.3a5.9 5.9 0 0 0-4.1-1.7H9l.9.9a6.2 6.2 0 0 1 1.8 4.4V9l2 2h1.2c.6 0 1.2.3 1.7.7L18.5 13"/>',
 "droplets":'<path d="M7 16.3c2.2 0 4-1.8 4-4 0-1.2-.6-2.3-1.8-3.3S7.1 6.6 7 5.3c-.2 1.3-1 2.6-2.2 3.6S3 11.1 3 12.3c0 2.2 1.8 4 4 4z"/><path d="M12.6 6.6A11 11 0 0 0 14 3.5c.5 2.5 2 4.9 4 6.5s3 3.5 3 5.5a6.98 6.98 0 0 1-11.9 5"/>',
 "zap":'<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
 "sparkles":'<path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3z"/><path d="M5 3v4M3 5h4M19 17v4M17 19h4"/>',
 "leaf":'<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10z"/><path d="M2 21c0-3 1.9-5.4 5.1-6C9.5 14.5 12 13 13 12"/>',
 "bug":'<path d="m8 2 1.9 1.9M14.1 3.9 16 2M9 7.1v-1a3 3 0 1 1 6 0v1"/><path d="M12 20c-3.3 0-6-2.7-6-6v-3a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v3c0 3.3-2.7 6-6 6M12 20v-9M6.5 9C4.6 8.8 3 7.1 3 5M6 13H2M3 21c0-2.1 1.7-3.9 3.8-4M20.97 5c0 2.1-1.6 3.8-3.5 4M22 13h-4M17.2 17c2.1.1 3.8 1.9 3.8 4"/>',
 "flame":'<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3.4.3 1.6 1.5 2.9 2.5 2.9z"/>',
 "garage":'<path d="M3 21V8l9-5 9 5v13"/><path d="M7 21v-9h10v9M7 15h10M7 18h10"/>',
 "home":'<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
 "stethoscope":'<path d="M4.8 2.3A.3.3 0 1 0 5 2H4a2 2 0 0 0-2 2v5a6 6 0 0 0 6 6 6 6 0 0 0 6-6V4a2 2 0 0 0-2-2h-1a.2.2 0 1 0 .3.3"/><path d="M8 15v1a6 6 0 0 0 6 6 6 6 0 0 0 6-6v-4"/><circle cx="20" cy="10" r="2"/>',
 "wrench":'<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
 "star":'<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 "mail":'<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 "pin":'<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "check":'<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
 "arrow":'<path d="M5 12h14M12 5l7 7-7 7"/>',
 "send":'<path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/>',
 "moon":'<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9z"/>',
 "calendar":'<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 "menu":'<path d="M4 6h16M4 12h16M4 18h16"/>',
 "chev":'<path d="m6 9 6 6 6-6"/>',
 "quote":'<path d="M3 21c3 0 7-1 7-8V5c0-1.3-.8-2-2-2H4c-1.3 0-2 .7-2 2v6c0 1.3.7 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 0-1 1v3c0 1 0 1 1 1zM15 21c3 0 7-1 7-8V5c0-1.3-.8-2-2-2h-4c-1.3 0-2 .7-2 2v6c0 1.3.7 2 2 2h.8c0 2.3-.3 4-2.8 4v3c0 1 0 1 1 1z"/>',
 "book":'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V2H6.5A2.5 2.5 0 0 0 4 4.5z"/><path d="M4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5"/>',
}
def I(name, cls=""):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{(" class=%s" % cls) if cls else ""}>{P[name]}</svg>'
STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>'

NAV = [("Home","/"),("About","/about/"),("Services","/services/"),("Industries","/industries/"),("Pricing","/pricing/"),("Reviews","/reviews/"),("Guides","/guides/"),("FAQ","/faq/")]

ORG = {"@type":"Organization","@id":DOMAIN+"/#org","name":BRAND,"alternateName":["Top Dispatch CRM","TopNotch Dispatch Services"],
       "url":DOMAIN+"/","logo":{"@type":"ImageObject","url":DOMAIN+"/assets/logo.png","width":512,"height":512},
       "email":EMAIL,"telephone":PHONE_E164,"foundingDate":"2023",
       "description":"Dedicated remote receptionists, dispatchers and back-office assistants from the Philippines for US home service businesses.",
       "address":{"@type":"PostalAddress","addressLocality":"Beverly Hills","addressRegion":"CA","postalCode":"90212","addressCountry":"US"},
       "areaServed":{"@type":"Country","name":"United States"},
       "contactPoint":[{"@type":"ContactPoint","telephone":PHONE_E164,"email":EMAIL,"contactType":"sales","areaServed":"US","availableLanguage":["English"]}]}

def crumbs_ld(items):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":DOMAIN+u} for i,(n,u) in enumerate(items)]}
def faq_ld(faqs):
    return {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}

def _trim(d):
    if len(d)<=158: return d
    cut=d[:155].rsplit(' ',1)[0].rstrip(',;:')
    return cut+'…'
def page(path, title, desc, body, active=None, ld=None, crumbs=None, ogtype="website"):
    url = DOMAIN + path
    desc = _trim(desc)
    graph = [ORG, {"@type":"WebSite","@id":DOMAIN+"/#web","url":DOMAIN+"/","name":BRAND,"publisher":{"@id":DOMAIN+"/#org"},"inLanguage":"en-US"}]
    if crumbs: graph.append(crumbs_ld(crumbs))
    if ld: graph += ld
    ldjson = json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False).replace("</","<\\/")
    nav = "".join(f'<li><a href="{u}"{" aria-current=\"page\"" if active==n else ""}>{n}</a></li>' for n,u in NAV)
    html_ = f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#1b2350">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="{DOMAIN}/assets/og.png">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/assets/logo-96.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap">
<link rel="stylesheet" href="/assets/styles.css">
<script type="application/ld+json">{ldjson}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
 <div class="wrap nav">
  <a class="brand" href="/" aria-label="{BRAND} home"><img src="/assets/logo-96.png" alt="{BRAND} logo" width="40" height="40">{BRAND}</a>
  <nav aria-label="Main"><ul class="nav-links">{nav}</ul></nav>
  <div class="nav-cta"><a class="btn btn-sm" href="/contact/">Leave Details</a>
   <button class="menu-btn" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">{I("menu")}</button></div>
 </div>
 <div class="mobile-nav" id="mobile-nav"><ul>{nav}<li><a href="/contact/">Contact</a></li><li><a href="tel:{PHONE_E164}">Call {PHONE}</a></li></ul><a class="btn" href="/contact/">Leave Details</a></div>
</header>
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/main.js" defer></script>
</body>
</html>'''
    d = OUT + path
    os.makedirs(d, exist_ok=True)
    fn = d + "index.html" if path.endswith("/") else d
    with open(fn, "w", encoding="utf-8") as f: f.write(html_)
    SITEMAP.append(path)

SITEMAP = []

def footer():
    svc = "".join(f'<li><a href="/services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    ind = "".join(f'<li><a href="/industries/{i["slug"]}/">{i["name"]}</a></li>' for i in INDUSTRIES[:10])
    return f'''<footer class="site-footer">
 <div class="wrap">
  <div class="foot">
   <div><img src="/assets/logo-96.png" alt="" width="44" height="44" loading="lazy"><p>Professional virtual secretaries, receptionists and dispatchers for US home service businesses. Founded 2023.</p></div>
   <div><h2>Services</h2><ul>{svc}</ul></div>
   <div><h2>Industries</h2><ul>{ind}<li><a href="/industries/">All industries</a></li></ul></div>
   <div><h2>Company</h2><ul><li><a href="/about/">About us</a></li><li><a href="/how-it-works/">How it works</a></li><li><a href="/why-the-philippines/">Why the Philippines</a></li><li><a href="/pricing/">Pricing</a></li><li><a href="/reviews/">Client reviews</a></li><li><a href="/guides/">Guides</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/contact/">Leave details</a></li></ul></div>
   <div><h2>Contact</h2><ul>
    <li class="contact-li">{I("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
    <li class="contact-li">{I("phone")}<a href="tel:{PHONE_E164}">{PHONE}</a></li>
    <li class="contact-li">{I("pin")}<span>{STREET}</span></li>
    <li class="contact-li">{I("clock")}<span>24/7 support available</span></li></ul></div>
  </div>
  <div class="foot-bottom"><span>&copy; 2026 {BRAND}. All rights reserved.</span><nav aria-label="Legal"><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a><a href="/sitemap.xml">Sitemap</a></nav></div>
 </div>
</footer>'''

# ---------- components ----------
def btn(label="Leave Details", href="/contact/", cls=""):
    return f'<a class="btn {cls}" href="{href}">{label} {I("arrow")}</a>'
def hero_sub(badge_icon, badge, h1a, h1b, lead, crumbs, amber=False, extra=""):
    cr = "".join(f'<li>{f"<a href=\"{u}\">{n}</a>" if i < len(crumbs)-1 else f"<span aria-current=\"page\">{n}</span>"}</li>' for i,(n,u) in enumerate(crumbs))
    g = "grad-amber" if amber else "grad"
    return f'''<section class="hero hero-sub"><div class="wrap">
<ol class="crumbs" aria-label="Breadcrumb">{cr}</ol>
<span class="badge{' badge-amber' if amber else ''}">{I(badge_icon)}{badge}</span>
<h1>{h1a} <span class="{g}">{h1b}</span></h1>
<p class="lead">{lead}</p>{extra}
</div></section>'''
def cta(h, p, label="Leave Details"):
    return f'<section class="cta bg-navy"><div class="wrap"><h2>{h}</h2><p>{p}</p>{btn(label, cls="btn-lg")}</div></section>'
def stats(items):
    return '<section class="bg-navy"><div class="wrap stats">' + "".join(f'<div class="stat">{I(ic) if ic else ""}<b>{v}</b><span>{l}</span></div>' for ic,v,l in items) + '</div></section>'
def faq_block(faqs):
    return '<div class="faq">' + "".join(f'<details><summary>{E(q)}{I("chev")}</summary><div class="ans"><p>{a}</p></div></details>' for q,a in faqs) + '</div>'
def initials(n): return "".join(w[0] for w in n.split()[:2])
def review_card(r, hidden=False):
    n,role,t = r
    return f'''<article class="card review"{' aria-hidden="true"' if hidden else ''}>{I("quote","q")}<div class="stars" aria-label="5 out of 5 stars">{STAR*5}</div><blockquote>&ldquo;{E(t)}&rdquo;</blockquote><div class="who-row"><span class="avatar">{initials(n)}</span><div><b>{n}</b><span>{role}</span></div></div></article>'''
def checks(items, one=False):
    return f'<ul class="checks{" one" if one else ""}">' + "".join(f"<li>{I('check')}<span>{E(html.unescape(x))}</span></li>" for x in items) + "</ul>"
def answer_box(q, a, facts=None):
    f = ""
    if facts: f = '<div class="facts">' + "".join(f"<div><b>{v}</b><span>{l}</span></div>" for v,l in facts) + "</div>"
    return f'<section class="section-tight"><div class="wrap"><div class="answer"><h2>{q}</h2><p>{a}</p>{f}</div></div></section>'
FACTS = [("1 dedicated person","Same receptionist daily"),("48–72 hours","Sign-up to first shift"),("Month to month","No setup fees"),("Your time zone","ET, CT, MT or PT")]

WHY_PH = [("message","t-cyan","Fluent English Speakers","Filipino professionals speak clear, neutral English, so your American customers have natural conversations every time."),
          ("globe","t-green","US Business Culture","Deeply familiar with American business etiquette, customer expectations and home service industry standards."),
          ("dollar","t-amber","Cost-Effective Solution","Get experienced professional support without the payroll taxes, benefits and overhead of a local hire."),
          ("clock","t-indigo","Your Timezone, Your Hours","Your team works your schedule, whether EST, CST, MST or PST. We adapt to your business hours, not the other way round.")]
STEPS = [("usercheck","t-cyan","#3aa6c9","Sign Up & Tell Us Your Needs","Fill out a quick form about your business, industry and the type of support you need. It takes less than five minutes."),
         ("users","t-violet","#7c6ef0","Get Matched With Your Secretary","We hand-pick a secretary with experience in your industry. You interview them before they start, so you feel confident."),
         ("thumbsup","t-green","#3fae6e","Start Growing Your Business","Your secretary is briefed on your business and starts handling calls, bookings and back-office tasks. You focus on the field.")]
def steps_block():
    return '<div class="grid g3 steps">' + "".join(f'<div class="card step {t}" style="--a:{c}"><span class="num">0{i+1}</span><div class="ic" style="margin:0 auto">{I(ic)}</div><h3>{h}</h3><p>{p}</p></div>' for i,(ic,t,c,h,p) in enumerate(STEPS)) + "</div>"
def why_block():
    return '<div class="grid g4">' + "".join(f'<div class="card center {t}"><div class="ic">{I(ic)}</div><h3 style="font-size:1rem">{h}</h3><p style="font-size:.84rem">{p}</p></div>' for ic,t,h,p in WHY_PH) + "</div>"
def svc_card(s):
    return f'<a class="card tint {s["tint"]}" href="/services/{s["slug"]}/"><div class="ic">{I(s["icon"])}</div><h3>{s["name"]}</h3><p>{s["short"]}</p><span class="more">Learn more {I("arrow")}</span></a>'
def ind_tiles(items):
    return '<div class="grid g5">' + "".join(f'<a class="card tile {i["tint"]}" href="/industries/{i["slug"]}/"><span class="ic">{I(i["icon"])}</span>{i["name"]}</a>' for i in items) + "</div>"
def calc_block():
    return f'''<div class="calc" data-calc>
 <div class="card">
  <div class="field"><label for="c-missed">Calls you miss in a typical week</label><input id="c-missed" name="missed" type="number" min="0" value="10" inputmode="numeric"></div>
  <div class="field"><label for="c-rate">Share of those callers who would have booked (%)</label><input id="c-rate" name="rate" type="number" min="0" max="100" value="30" inputmode="numeric"></div>
  <div class="field" style="margin:0"><label for="c-value">Average job value ($)</label><input id="c-value" name="value" type="number" min="0" value="350" inputmode="numeric"></div>
  <p class="muted mt-s" style="font-size:.78rem;margin-bottom:0">The starting numbers are examples. Replace them with yours.</p>
 </div>
 <div class="card result" aria-live="polite"><span class="muted" style="font-size:.85rem">Revenue left on the table each month</span><b class="grad" data-out>$0</b><small>About <strong data-jobs>0</strong> jobs a month that rang and went elsewhere.</small></div>
</div>'''
def compare_table():
    rows = [("Who picks up","The same trained person every shift","Whichever agent in the pool is free","A software voice agent","Your employee"),
            ("How you pay","Flat monthly fee, part-time or full-time","Per minute or per call, plus overage","Monthly plan sized by call volume","Hourly wage plus payroll taxes and benefits"),
            ("Knows your business","Learns your service area, price book and technicians","Works from a script you supply","Works from the answers you load into it","Yes"),
            ("Dispatching","Assigns jobs, calls technicians, updates the customer","Usually takes a message or pages on-call","Can book a slot; can't sort a schedule clash","Yes"),
            ("Your software","Logs in to your job system as a user","Varies by provider and plan","Through integrations, where they exist","Yes"),
            ("Fits best","Shops with steady daily call volume","Low volume, overflow or message taking","After-hours overflow and simple bookings","Shops that need someone on site")]
    body = "".join(f'<tr><th scope="row">{r[0]}</th><td class="us">{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td></tr>' for r in rows)
    return f'''<div class="table-wrap"><table><caption>Four ways to cover a home service phone line</caption><thead><tr><th scope="col"></th><th scope="col" class="us">Top Dispatch dedicated receptionist</th><th scope="col">Shared answering service</th><th scope="col">AI receptionist</th><th scope="col">In-house hire</th></tr></thead><tbody>{body}</tbody></table></div>'''

HOME_FAQ = [
 ("What does Top Dispatch do?","Top Dispatch places dedicated remote receptionists and dispatchers from the Philippines with US home service businesses. Your receptionist answers calls in your company's name, books jobs, dispatches technicians, follows up on estimates and keeps your CRM up to date."),
 ("Do your secretaries speak fluent English?","Yes. Every secretary passes English proficiency testing before placement and is trained to work with American customers. You interview your candidate before they start, so you can judge for yourself."),
 ("How quickly can I get started?","Most clients are live within 48 to 72 hours of signing up. We match you with a secretary who has worked in your trade, brief them on your business and they start taking calls."),
 ("What industries do you specialize in?","Home services: HVAC, plumbing, electrical, locksmith, roofing, garage door, pest control, cleaning, landscaping, construction, security, chimney, air duct and medical spa businesses."),
 ("Can I choose my own secretary?","Yes. We put forward matched candidates and you interview them before committing. If you ever want a different person, we find a replacement."),
 ("What does the service include?","Call answering, appointment setting, dispatch coordination, cold calling, back-office admin, reporting and customer support. You choose the mix, and most clients start with the phones."),
 ("What are the working hours?","Your business hours, in your time zone. If you need early starts, evenings, weekends or overnight cover, we build the schedule around that."),
 ("Is there a minimum commitment?","No long-term contract. Service runs month to month with no setup fees. You can scale up, scale down or cancel with 30 days' notice."),
 ("How do you ensure quality?","Every secretary is vetted, English-tested and trained on your industry before placement. You get call summaries and reports, and a dedicated account manager reviews performance with you."),
]

# ================= HOME =================
def home():
    rev = REVIEWS
    track1 = "".join(review_card(r) for r in rev) + "".join(review_card(r, True) for r in rev)
    rev2 = rev[4:]+rev[:4]
    track2 = "".join(review_card(r) for r in rev2) + "".join(review_card(r, True) for r in rev2)
    body = f'''
<section class="hero"><div class="wrap">
 <span class="badge">{I("star")}Trusted by 153+ businesses across the US</span>
 <h1><span class="line">Scale Your</span><span class="line grad">Remote Team</span></h1>
 <p class="lead">Professional virtual secretaries based in the Philippines, handling your calls, scheduling and back-office operations so you can focus on growing your business.</p>
 <p class="tag">Dedicated remote receptionists &amp; dispatchers for US home service businesses</p>
 <div class="actions">{btn(cls="btn-lg")}<span class="phone">or call <a href="tel:{PHONE_E164}">{PHONE}</a></span></div>
</div></section>
{stats([("users","153+","Active Clients"),("target","5&#9733;","Client Satisfaction"),("award","2-5 yrs","Avg. Experience"),("clock","24/7","Support Available")])}

<section class="section"><div class="wrap split">
 <div class="prose">
  <span class="badge">{I("heart")}Our Story</span>
  <h2 class="mt-s">Who We Are</h2>
  <p>Founded in 2023, <strong>Top Dispatch</strong> was built with one mission: to give service businesses access to world-class virtual secretaries at an affordable price.</p>
  <p>Our team of highly trained professionals based in the Philippines brings <strong>2 to 5 years of hands-on experience</strong> in appointment setting, cold calling, dispatch coordination and back-office management.</p>
  <p>We specialize in <strong>home service industries</strong>, from HVAC and roofing to locksmith and plumbing, giving your business the professional support it deserves without the overhead of a local hire.</p>
 </div>
 <div class="grid g2">
  <div class="card card-sm t-cyan"><div class="ic ic-sm">{I("globe")}</div><h3>Based in Philippines</h3><p>Professional team with US business culture training</p></div>
  <div class="card card-sm t-green"><div class="ic ic-sm">{I("award")}</div><h3>2-5 Yrs Experience</h3><p>Every secretary is vetted and trained before placement</p></div>
  <div class="card card-sm t-violet"><div class="ic ic-sm">{I("users")}</div><h3>153+ Active Clients</h3><p>Growing network of satisfied US businesses</p></div>
  <div class="card card-sm t-rose"><div class="ic ic-sm">{I("heart")}</div><h3>Founded in 2023</h3><p>Built from scratch with passion for small business growth</p></div>
 </div>
</div></section>

<section class="section bg-3"><div class="wrap">
 <div class="head"><h2>What We Do</h2><p>Our virtual secretaries are trained across the most in-demand service roles for US home service businesses.</p></div>
 <div class="svc-grid">{"".join(svc_card(s) for s in SERVICES)}</div>
</div></section>

<section class="section"><div class="wrap">
 <div class="head"><h2>Dedicated Receptionist vs. the Alternatives</h2><p>A virtual receptionist for a small business comes in four shapes. Here is how a dedicated Top Dispatch secretary compares with an answering service, an AI receptionist and a local hire.</p></div>
 {compare_table()}
 <p class="center muted mt-m" style="font-size:.88rem">Want the numbers? Read <a class="grad" href="/guides/answering-service-cost/">how much an answering service costs</a> and <a class="grad" href="/guides/ai-receptionist-vs-human-receptionist/">AI receptionist or a human one</a>.</p>
</div></section>

<section class="section bg-2"><div class="wrap">
 <div class="head"><h2>How It Works</h2><p>Get your virtual secretary up and running in 3 simple steps.</p></div>
 {steps_block()}
 <p class="center mt-l"><a class="more" href="/how-it-works/">See the full onboarding {I("arrow")}</a></p>
</div></section>

<section class="section bg-3"><div class="wrap">
 <div class="head"><h2>Why the Philippines?</h2><p>The world's leading destination for professional remote staffing.</p></div>
 {why_block()}
 <p class="center mt-l"><a class="more" href="/why-the-philippines/">Why our team is in the Philippines {I("arrow")}</a></p>
</div></section>

<section class="section"><div class="wrap">
 <div class="head"><h2>Industries We Serve</h2><p>Specialized experience across the most demanding home service sectors.</p></div>
 {ind_tiles([i for i in INDUSTRIES if i["slug"] in ("hvac-answering-service","locksmith-answering-service","contractor-answering-service","plumbing-answering-service","electrician-answering-service","cleaning-business-answering-service","landscaping-answering-service","pest-control-answering-service","security-alarm-answering-service","garage-door-answering-service")])}
 <p class="center mt-l"><a class="more" href="/industries/">See all 14 industries {I("arrow")}</a></p>
</div></section>

<section class="section bg-2"><div class="wrap">
 <div class="head"><h2>What Are Missed Calls Costing You?</h2><p>A caller who reaches voicemail often rings the next company on the list. Put in your own numbers and see what that adds up to each month.</p></div>
 {calc_block()}
</div></section>

<section class="section bg-navy"><div class="wrap">
 <div class="head"><h2>Simple, Transparent Pricing</h2><p>No contracts, no hidden fees. Flexible plans tailored to your needs.</p></div>
 <div class="price-box">
  {checks(["Professional English-speaking secretary","2–5 years of relevant industry experience","Full-time or part-time availability","Real-time call &amp; dispatch handling","Back office &amp; CRM management","Monthly billing, no long-term contracts"])}
  <p>Contact us to find the right plan for your business needs.</p>
  {btn()}
 </div>
</div></section>

<section class="section" aria-labelledby="rev-h"><div class="head wrap"><h2 id="rev-h">What Our Clients Say</h2><p>Real results from real businesses across the US.</p></div>
 <div class="marquee"><div class="track">{track1}</div></div>
 <div class="marquee rev"><div class="track">{track2}</div></div>
 <p class="center mt-l"><a class="more" href="/reviews/">Read all client reviews {I("arrow")}</a></p>
</section>

<section class="section bg-2"><div class="wrap">
 <div class="head"><h2>FAQ</h2><p>Everything you need to know before getting started.</p></div>
 {faq_block(HOME_FAQ)}
 <p class="center mt-l"><a class="more" href="/faq/">All frequently asked questions {I("arrow")}</a></p>
</div></section>
{cta("Ready to Grow Your Business?","Join 153+ businesses that trust Top Dispatch to manage their operations. Get started today with no contracts and no risk.")}
'''
    ld = [{"@type":"ProfessionalService","@id":DOMAIN+"/#service","name":BRAND,"url":DOMAIN+"/","image":DOMAIN+"/assets/og.png","logo":DOMAIN+"/assets/logo.png",
           "telephone":PHONE_E164,"email":EMAIL,"priceRange":"$$","address":ORG["address"],"areaServed":"US","parentOrganization":{"@id":DOMAIN+"/#org"},
           "openingHoursSpecification":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"},
           "hasOfferCatalog":{"@type":"OfferCatalog","name":"Remote staffing services","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":s["name"],"url":f'{DOMAIN}/services/{s["slug"]}/'}} for s in SERVICES]}},
          faq_ld(HOME_FAQ)]
    page("/", "Virtual Receptionists for Home Services | Top Dispatch",
         "Dedicated virtual secretaries from the Philippines for US home service businesses: call answering, dispatch, appointment setting and back office. Month to month, live in 48–72 hours.",
         body, "Home", ld)

# ================= SERVICES =================
def services_hub():
    rows = "".join(f'''<article class="card tint row-card {s["tint"]}"><div class="ic">{I(s["icon"])}</div><div style="flex:1"><h3><a href="/services/{s["slug"]}/">{s["name"]}</a></h3><p>{s["short"]}</p>{checks(s["includes"][:6])}<a class="more" href="/services/{s["slug"]}/">Explore {s["name"].lower()} {I("arrow")}</a></div></article>''' for s in SERVICES)
    body = hero_sub("sparkles","Everything You Need","Our","Services","Comprehensive virtual staffing solutions designed specifically for US home service businesses.",[("Home","/"),("Services","/services/")]) + \
      answer_box("What services does Top Dispatch offer?","Top Dispatch provides eight remote staffing services for US home service companies: virtual receptionist, dispatch coordination, after-hours answering, appointment setting, cold calling and lead generation, back-office management, reporting and analytics, and customer support. Each is delivered by one dedicated, trained secretary who works your hours inside your existing software.", FACTS) + \
      f'<section class="section-tight"><div class="wrap stack">{rows}</div></section>' + \
      cta("Ready to Get Started?","Let us match you with the perfect virtual secretary for your business.")
    ld = [{"@type":"ItemList","name":"Top Dispatch services","itemListElement":[{"@type":"ListItem","position":i+1,"url":f'{DOMAIN}/services/{s["slug"]}/',"name":s["name"]} for i,s in enumerate(SERVICES)]}]
    page("/services/","Receptionist, Dispatch & Back-Office Services | Top Dispatch",
         "Virtual receptionist, dispatch, after-hours answering, appointment setting, cold calling, back-office, reporting and customer support services for US home service businesses.",
         body,"Services",ld,[("Home","/"),("Services","/services/")])

def service_page(s):
    path = f'/services/{s["slug"]}/'
    cr = [("Home","/"),("Services","/services/"),(s["name"],path)]
    log = "".join(f'<div class="log-item {s["tint"]}"><div><div class="k">{k}</div><div class="t">{t}</div></div><div><p>{c}</p><p class="out"><span class="pill{" b" if o.split(":")[0] in ("Dispatched","Updated","Scheduled","Sent","Listed","Prepared","Followed up") else ""}">{o.split(":")[0]}</span>{o.split(":",1)[1].strip()}</p></div></div>' for k,t,c,o in s["scenarios"])
    hw = "".join(f'<div class="card step {s["tint"]}" style="--a:var(--a)"><span class="num" style="color:#030616">0{i+1}</span><h3 style="margin-top:6px">{h}</h3><p>{p}</p></div>' for i,(h,p) in enumerate(s["how"]))
    others = [x for x in SERVICES if x["slug"]!=s["slug"]][:3]
    body = hero_sub(s["icon"], s["name"], s["h1a"], s["h1b"], s["lead"], cr, extra=f'<div class="actions">{btn("Get matched")}<span class="phone">or call <a href="tel:{PHONE_E164}">{PHONE}</a></span></div>') + \
      answer_box(s["q"], s["answer"], FACTS) + f'''
<section class="section"><div class="wrap split" style="align-items:start">
 <div class="prose"><h2>What's included</h2><p>Your {s["name"].lower()} specialist is one dedicated person who learns your business and works inside your tools. Typical tasks include:</p>{checks(s["includes"])}<div class="mt-m">{btn()}</div></div>
 <div><h2 style="font-size:1.5rem;margin-bottom:18px">A sample shift</h2><div class="log">{log}</div><p class="muted mt-s" style="font-size:.78rem">Illustrative examples of the call types a {s["name"].lower()} specialist handles.</p></div>
</div></section>
<section class="section bg-2"><div class="wrap"><div class="head"><h2>How {s["name"]} Works</h2><p>From sign-up to first shift in 48 to 72 hours for most clients.</p></div><div class="grid g3 steps">{hw}</div></div></section>
<section class="section"><div class="wrap"><div class="head"><h2>Built for Your Trade</h2><p>{s["name"]} for the home service industries we know best.</p></div>
 <div class="links">{"".join(f'<a href="/industries/{i["slug"]}/">{i["name"]}</a>' for i in INDUSTRIES)}</div></div></section>
<section class="section bg-2"><div class="wrap"><div class="head"><h2>{s["name"]} FAQ</h2><p>Straight answers to the questions owners ask most.</p></div>{faq_block(s["faqs"])}</div></section>
<section class="section"><div class="wrap"><div class="head"><h2>Pair It With</h2><p>Most clients combine two or three roles in one secretary's day.</p></div><div class="svc-grid">{"".join(svc_card(x) for x in others)}</div></div></section>
''' + cta(f"Get a Dedicated {s['name']} Specialist","Tell us what you need covered. You interview your match before they start, and most clients are live in 48 to 72 hours.")
    ld = [{"@type":"Service","@id":DOMAIN+path+"#service","name":s["name"],"serviceType":s["name"],"description":s["answer"],"url":DOMAIN+path,
           "provider":{"@id":DOMAIN+"/#org"},"areaServed":{"@type":"Country","name":"United States"},
           "audience":{"@type":"BusinessAudience","audienceType":"Home service businesses"},
           "offers":{"@type":"Offer","priceSpecification":{"@type":"PriceSpecification","priceCurrency":"USD","description":"Flat monthly fee based on hours and scope. No setup fees."},"availability":"https://schema.org/InStock"}},
          faq_ld(s["faqs"])]
    page(path, s["title"], s["meta"], body, "Services", ld, cr)

# ================= INDUSTRIES =================
def industries_hub():
    allind = INDUSTRIES
    cards = "".join(f'''<article class="card {i["tint"]}" style="display:flex;gap:16px"><div class="ic">{I(i["icon"])}</div><div><h3 style="margin:0 0 6px;font-size:1.15rem"><a href="/industries/{i["slug"]}/">{i["name"]}</a></h3><p style="font-size:.84rem;color:var(--muted)">{i["short"]}</p>{checks(i["calls"][:4])}<a class="more" href="/industries/{i["slug"]}/">{i["name"]} answering service {I("arrow")}</a></div></article>''' for i in allind)
    g = GENERAL
    cards += f'<article class="card {g["tint"]}" style="display:flex;gap:16px"><div class="ic">{I(g["icon"])}</div><div><h3 style="margin:0 0 6px;font-size:1.15rem">{g["name"]}</h3><p style="font-size:.84rem;color:var(--muted)">{g["short"]}</p>{checks(["Custom workflow adaptation","Industry-specific training","Flexible scheduling support","Dedicated account manager"])}</div></article>'
    body = hero_sub("wrench","Industry Expertise","Industries","We Serve","Specialized experience across the most demanding home service sectors. Our secretaries know your industry.",[("Home","/"),("Industries","/industries/")]) + \
      answer_box("Which industries does Top Dispatch serve?","Top Dispatch staffs remote receptionists and dispatchers for US home service trades: HVAC, plumbing, electrical, locksmith, roofing, garage door, pest control, cleaning, landscaping, construction and general contracting, security and alarm, chimney, air duct cleaning and medical spas. Each secretary is trained on the vocabulary and call types of the trade they support.") + \
      f'<section class="section-tight"><div class="wrap grid g2">{cards}</div></section>' + \
      cta("Don't See Your Industry?","We adapt to any home service business. Contact us and we'll tailor a solution for you.")
    ld = [{"@type":"ItemList","name":"Industries served","itemListElement":[{"@type":"ListItem","position":k+1,"url":f'{DOMAIN}/industries/{i["slug"]}/',"name":i["name"]+" answering service"} for k,i in enumerate(allind)]}]
    page("/industries/","Answering Service by Industry | Top Dispatch",
         "Dedicated remote receptionists for HVAC, plumbing, electrical, locksmith, roofing, garage door, pest control, cleaning, landscaping, contractors, security, chimney, air duct and med spas.",
         body,"Industries",ld,[("Home","/"),("Industries","/industries/")])

def lc(x): return x if x.isupper() else x.lower()
def art(x): return "an" if x[0].upper() in "AEIOU" or x.isupper() and x[0] in "HFLMNRSX" else "a"
def industry_page(i):
    path = f'/industries/{i["slug"]}/'
    nm = i["name"]
    label = nm if nm!="Construction & Contractors" else "Contractor"
    cr = [("Home","/"),("Industries","/industries/"),(nm,path)]
    caller, asked, outcome = i["scen"]
    rel = [x for x in INDUSTRIES if x["slug"]!=i["slug"]][:5]
    body = hero_sub(i["icon"], f"{nm} Specialists", label, "Answering Service", i["lead"], cr, extra=f'<div class="actions">{btn("Get matched")}<span class="phone">or call <a href="tel:{PHONE_E164}">{PHONE}</a></span></div>') + \
      answer_box(f"What does {art(label)} {lc(label)} answering service do?", i["answer"], FACTS) + f'''
<section class="section"><div class="wrap split" style="align-items:start">
 <div class="prose"><h2>Calls We Handle for {label} Companies</h2><p>Your receptionist is trained on {lc(label)} call types before day one, so callers aren't explaining the basics.</p>{checks(i["calls"])}</div>
 <div class="card {i["tint"]}"><div class="ic">{I("phone")}</div><h3>Example call</h3>
  <div class="log mt-s"><div class="log-item {i["tint"]}"><div><div class="k">Caller</div></div><div><p>{caller}</p></div></div>
  <div class="log-item {i["tint"]}"><div><div class="k">Asked</div></div><div><p>{asked}</p></div></div>
  <div class="log-item {i["tint"]}"><div><div class="k">Outcome</div></div><div><p class="out" style="margin:0"><span class="pill">Handled</span>{outcome}</p></div></div></div>
  <p class="muted mt-s" style="font-size:.78rem;margin-bottom:0">Works inside the software you already run, including {i["software"]}.</p></div>
</div></section>
<section class="section bg-2"><div class="wrap"><div class="head"><h2>What Your {label} Secretary Takes Off Your Plate</h2><p>Start with the phones. Add dispatch, follow-ups and admin as you grow.</p></div><div class="svc-grid">{"".join(svc_card(s) for s in SERVICES[:6])}</div></div></section>
<section class="section"><div class="wrap"><div class="head"><h2>How It Works</h2><p>Live in 48 to 72 hours with a secretary who has worked in {lc(label)}.</p></div>{steps_block()}</div></section>
<section class="section bg-2"><div class="wrap"><div class="head"><h2>{label} Answering Service FAQ</h2><p>What {lc(label)} owners ask before they sign up.</p></div>{faq_block(i["faqs"])}</div></section>
<section class="section-tight"><div class="wrap"><div class="head" style="margin-bottom:24px"><h2 style="font-size:1.6rem">Other Trades We Support</h2></div><div class="links">{"".join(f'<a href="/industries/{x["slug"]}/">{x["name"]}</a>' for x in rel)}<a href="/industries/">All industries</a></div></div></section>
''' + cta(f"Hand Over Your {label} Phones","We match you with a secretary who has worked in your trade. You interview them first.")
    ld = [{"@type":"Service","name":f"{label} answering service","serviceType":"Answering service and remote dispatch","description":i["answer"],"url":DOMAIN+path,
           "provider":{"@id":DOMAIN+"/#org"},"areaServed":{"@type":"Country","name":"United States"},
           "audience":{"@type":"BusinessAudience","audienceType":f"{label} businesses"}}, faq_ld(i["faqs"])]
    page(path, i["title"], i["meta"], body, "Industries", ld, cr)

# ================= ABOUT =================
def about():
    vals = [("shield","t-cyan","Integrity","We operate with full transparency: no hidden fees, no surprises. What we promise, we deliver."),
            ("star","t-amber","Excellence","Every secretary undergoes vetting, English testing and industry-specific training before placement."),
            ("heart","t-rose","Partnership","We don't just provide a service. We become an extension of your team and care about your growth."),
            ("zap","t-indigo","Speed","Most clients are up and running within 48–72 hours. We move fast without cutting corners.")]
    team = [("Alex Turner","Founder & CEO","Built Top Dispatch to solve a problem he faced as a home service business owner: finding reliable, professional support without local overhead."),
            ("Maria Reyes","Head of Operations","8 years of experience managing remote teams across the US and the Philippines. Makes sure every client is matched with the right secretary within 48 hours."),
            ("James Kim","Director of Training","Developed the industry-specific training curriculum that prepares every secretary for real US home service environments from day one.")]
    cr=[("Home","/"),("About","/about/")]
    body = hero_sub("heart","Our Story","About","Top Dispatch","Founded in 2023 with one mission: give service businesses access to world-class virtual secretaries.",cr) + f'''
<section class="section"><div class="wrap split">
 <div class="prose"><h2>Who We Are</h2>
  <p>Founded in 2023, <strong>Top Dispatch</strong> was built with one mission: to give service businesses access to world-class virtual secretaries at a professional price point.</p>
  <p>Our team of highly trained professionals based in the Philippines brings <strong>2 to 5 years of hands-on experience</strong> in appointment setting, cold calling, dispatch coordination and back-office management.</p>
  <p>We specialize in <strong>home service industries</strong>, from HVAC and roofing to locksmith and plumbing, giving your business the professional support it deserves.</p>
  <p>We are headquartered in Beverly Hills, California, and serve owners in every US time zone.</p></div>
 <div class="grid g2">
  <div class="card card-sm t-cyan"><div class="ic ic-sm">{I("globe")}</div><h3>Based in Philippines</h3><p>Professional team with deep US business culture training</p></div>
  <div class="card card-sm t-green"><div class="ic ic-sm">{I("award")}</div><h3>2-5 Yrs Experience</h3><p>Every secretary vetted and trained before placement</p></div>
  <div class="card card-sm t-violet"><div class="ic ic-sm">{I("users")}</div><h3>153+ Active Clients</h3><p>Growing network of satisfied US businesses</p></div>
  <div class="card card-sm t-rose"><div class="ic ic-sm">{I("clock")}</div><h3>Founded 2023</h3><p>Built from the ground up with passion for small business</p></div>
 </div></div></section>
<section class="section bg-2"><div class="wrap"><div class="head"><h2>Our Core Values</h2></div><div class="grid g4">{"".join(f'<div class="card center {t}"><div class="ic">{I(ic)}</div><h3>{h}</h3><p>{p}</p></div>' for ic,t,h,p in vals)}</div></div></section>
<section class="section"><div class="wrap"><div class="head"><h2>Meet the Team</h2></div><div class="grid g3 team">{"".join(f'<div class="card center"><span class="avatar">{initials(n)}</span><h3>{n}</h3><div class="role">{r}</div><p>{p}</p></div>' for n,r,p in team)}</div></div></section>
''' + cta("Join Our Growing Family","153+ businesses already trust Top Dispatch. You're next.")
    ld=[{"@type":"AboutPage","url":DOMAIN+"/about/","name":"About Top Dispatch","about":{"@id":DOMAIN+"/#org"}}]+[{"@type":"Person","name":n,"jobTitle":r,"worksFor":{"@id":DOMAIN+"/#org"}} for n,r,_ in team]
    page("/about/","About Top Dispatch | Remote Staffing for Home Service Businesses",
         "Founded in 2023, Top Dispatch places trained virtual secretaries from the Philippines with US home service businesses. Meet the team and our values.",body,"About",ld,cr)

# ================= REVIEWS =================
def reviews():
    cr=[("Home","/"),("Reviews","/reviews/")]
    body = hero_sub("star","Real Results, Real Businesses","Client","Reviews","Don't take our word for it. Hear directly from the business owners who trust us every day.",cr,amber=True) + \
      stats([("", "153+","Happy Clients"),("","5.0&#9733;","Average Rating"),("","97%","Retention Rate"),("","48h","Avg. Onboarding Time")]) + \
      f'<section class="section"><div class="wrap grid g3">{"".join(review_card(r) for r in REVIEWS)}</div></section>' + \
      cta("Be Our Next Success Story","Join 153+ businesses that transformed their operations with Top Dispatch.")
    page("/reviews/","Top Dispatch Reviews | What Home Service Owners Say",
         "Reviews from HVAC, plumbing, roofing, locksmith, cleaning and pest control owners who use a Top Dispatch virtual secretary. 153+ clients, 97% retention.",body,"Reviews",None,cr)

# ================= FAQ =================
FAQ_GROUPS = [
 ("Getting Started",[HOME_FAQ[2],HOME_FAQ[4],HOME_FAQ[7],
   ("What do you need from me to start?","A short intake form, your greeting and call script, your price sheet, your service area, and user logins to your phone system and job software. We guide you through each item."),
   ("Can I try before committing long term?","Yes. Service is month to month, so your first month works as a trial with 30 days' notice to cancel.")]),
 ("About Our Team",[HOME_FAQ[1],HOME_FAQ[3],HOME_FAQ[8],
   ("Why are your secretaries in the Philippines?","The Philippines has a large, experienced English-speaking workforce that already works US hours. See <a href=\"/why-the-philippines/\">why the Philippines</a>."),
   ("Is it the same person every day?","Yes. You get one dedicated secretary, not a rotating pool. A briefed backup covers sick days and leave.")]),
 ("Services & Billing",[HOME_FAQ[5],HOME_FAQ[6],
   ("How does billing work?","You pay a flat monthly fee based on the hours and scope you need, billed monthly. There are no setup fees, per-minute charges or long-term contracts. See <a href=\"/pricing/\">pricing</a>."),
   ("Do you charge per call or per minute?","No. Unlike many answering services, Top Dispatch charges a flat monthly fee for a dedicated person."),
   ("Which software can my secretary use?","ServiceTitan, Housecall Pro, Jobber, FieldEdge, Workiz, QuickBooks, Google Workspace, Microsoft 365 and most common CRMs and phone systems.")]),
 ("Security & Quality",[
   ("How is my customer data protected?","Your secretary uses their own login for each tool you share, with only the permissions the work needs. You can remove access at any time."),
   ("How do I know calls are handled well?","You get call summaries and regular reports, and you can review call recordings in your own phone system if it records calls."),
   ("What if I'm not happy with my secretary?","Tell us. We address it quickly, and if the fit isn't right we find a replacement.")]),
]
def faq_page():
    cr=[("Home","/"),("FAQ","/faq/")]
    groups = "".join(f'<div class="faq-group"><h2>{g}</h2>{faq_block(items)}</div>' for g,items in FAQ_GROUPS)
    allq = [x for _,items in FAQ_GROUPS for x in items]
    body = hero_sub("message","Common Questions","Frequently Asked","Questions","Everything you need to know before getting started. Can't find your answer? Contact us directly.",cr) + \
      f'<section class="section-tight"><div class="wrap">{groups}</div></section>' + cta("Still Have Questions?","Our team is happy to help. Reach out and we'll get back to you within the hour.")
    page("/faq/","FAQ: Virtual Receptionist & Dispatch Service | Top Dispatch",
         "Answers on getting started, English fluency, hours, software, billing, contracts and quality for Top Dispatch virtual secretaries.",body,"FAQ",[faq_ld([(q,a.replace('<a href="/why-the-philippines/">why the Philippines</a>','why the Philippines').replace('<a href="/pricing/">pricing</a>','pricing')) for q,a in allq])],cr)

# ================= CONTACT =================
def contact():
    cr=[("Home","/"),("Contact","/contact/")]
    trades = "".join(f'<option>{i["name"]}</option>' for i in INDUSTRIES) + "<option>Other</option>"
    body = f'''<section class="hero hero-sub" style="padding-bottom:30px"><div class="wrap"><ol class="crumbs" aria-label="Breadcrumb"><li><a href="/">Home</a></li><li><span aria-current="page">Contact</span></li></ol>
<h1>Let's Talk Business</h1><p class="lead">Leave your details below and our team will get in touch to show you how Top Dispatch can transform your operations.</p></div></section>
<section class="section-tight" style="padding-bottom:96px"><div class="wrap split" style="align-items:start">
 <div class="stack">
  <div class="card" style="padding:28px"><h2 style="font-size:1.35rem">Why Partner With Us?</h2>
   <div class="feature t-cyan"><span class="ic ic-sm">{I("users")}</span><div><b>Dedicated Professionals</b><p>Fluent English speakers with 2–5 years of US home service experience, ready to integrate into your team.</p></div></div>
   <div class="feature t-blue"><span class="ic ic-sm">{I("shield")}</span><div><b>Reliable &amp; Secure</b><p>We handle your calls, scheduling and CRM with professionalism, care and data security.</p></div></div>
   <div class="feature t-indigo"><span class="ic ic-sm">{I("star")}</span><div><b>Trusted by 150+ Companies</b><p>From HVAC to locksmiths, businesses across the US rely on Top Dispatch to scale.</p></div></div>
  </div>
  <div class="grid g2">
   <a class="card center t-cyan" href="mailto:{EMAIL}"><span class="ic ic-round">{I("mail")}</span><h3 style="font-size:1rem">Email Us</h3><p style="font-size:.8rem">{EMAIL}</p></a>
   <a class="card center t-blue" href="tel:{PHONE_E164}"><span class="ic ic-round">{I("phone")}</span><h3 style="font-size:1rem">Call Us</h3><p style="font-size:.8rem">{PHONE} · 24/7</p></a>
  </div>
 </div>
 <form class="form-card" data-lead data-endpoint="" novalidate>
  <h2>Leave Your Details</h2><p class="sub">Fill out the form and our team will get back to you within a few hours.</p>
  <div class="field"><label for="f-name">Full Name</label><input id="f-name" name="name" autocomplete="name" placeholder="John Doe" required></div>
  <div class="form-row"><div class="field"><label for="f-email">Email Address</label><input id="f-email" type="email" name="email" autocomplete="email" placeholder="john@example.com" required></div>
  <div class="field"><label for="f-phone">Phone Number</label><input id="f-phone" type="tel" name="phone" autocomplete="tel" placeholder="(555) 123-4567" required></div></div>
  <div class="field"><label for="f-trade">Your Trade</label><select id="f-trade" name="trade"><option value="">Select your industry</option>{trades}</select></div>
  <div class="field"><label for="f-msg">How can we help?</label><textarea id="f-msg" name="message" placeholder="Tell us a bit about your business and what you're looking for..."></textarea></div>
  <div class="sr"><label for="f-hp">Leave blank</label><input id="f-hp" name="company_website" tabindex="-1" autocomplete="off"></div>
  <button class="btn" type="submit">Send Details {I("send")}</button>
  <p class="form-status" role="status" aria-live="polite"></p>
  <p class="form-note">By sending, you agree to be contacted about Top Dispatch services. See our <a href="/privacy/" style="text-decoration:underline">privacy policy</a>.</p>
 </form>
</div></section>'''
    ld=[{"@type":"ContactPage","url":DOMAIN+"/contact/","name":"Contact Top Dispatch","about":{"@id":DOMAIN+"/#org"}}]
    page("/contact/","Contact Top Dispatch | Get Matched With a Virtual Receptionist",
         "Leave your details and get matched with a dedicated virtual receptionist or dispatcher for your home service business. Call (833) 505-4136.",body,None,ld,cr)

# ================= PRICING =================
def pricing():
    cr=[("Home","/"),("Pricing","/pricing/")]
    plans = [("Part-Time","For owner-operators who need the busiest hours covered.","Up to 4–6 hours a day",["Dedicated secretary","Call answering &amp; booking","CRM updates","Monthly billing"],False),
             ("Full-Time","For shops with steady daily call volume.","8 hours a day, your time zone",["Everything in Part-Time","Dispatch coordination","Estimate follow-ups","Back-office tasks in quiet hours"],True),
             ("Extended Coverage","For 24/7 trades and multi-truck teams.","Evenings, weekends or overnight",["Everything in Full-Time","After-hours emergency dispatch","On-call paging","Multi-person scheduling"],False)]
    pc = "".join(f'<div class="card plan{" featured" if f else ""}"><h3>{n}</h3><div class="who">{h}</div><p>{d}</p>{checks(items,True)}<a class="btn{"" if f else " btn-ghost"}" href="/contact/">Get a quote {I("arrow")}</a></div>' for n,d,h,items,f in plans)
    pf = [("How much does a virtual receptionist cost?","Top Dispatch charges a flat monthly fee based on the hours you need and the work involved, with no setup fees. Tell us what you want covered and we send a quote, usually the same day."),
          ("Are there per-minute or per-call charges?","No. You pay for a dedicated person's hours, not for each call or minute."),
          ("Is there a contract?","No long-term contract. Service is month to month and you can scale up, scale down or cancel with 30 days' notice."),
          ("What affects the price?","Hours per day, shift timing (business hours versus overnight), and the mix of work such as reception, dispatch, outbound calling or back office."),
          ("How does this compare with hiring locally?","A remote secretary avoids payroll taxes, benefits, office space and recruiting time. Use the calculator on this page to see what missed calls are costing you today.")]
    body = hero_sub("dollar","No Contracts, No Hidden Fees","Simple,","Transparent Pricing","A flat monthly fee for a dedicated secretary. No setup fees, no per-minute meter, no long-term contract.",cr) + \
      answer_box("How does Top Dispatch pricing work?","Top Dispatch charges one flat monthly fee for a dedicated remote secretary, sized by the hours you need (part-time, full-time or extended coverage) and the type of work. There are no setup fees, no per-call or per-minute charges and no long-term contract: service is month to month with 30 days' notice.", FACTS) + f'''
<section class="section"><div class="wrap"><div class="head"><h2>Choose Your Coverage</h2><p>Every plan includes a dedicated, vetted secretary who works your hours.</p></div><div class="grid g3">{pc}</div></div></section>
<section class="section bg-2"><div class="wrap"><div class="head"><h2>What Are Missed Calls Costing You?</h2><p>Compare a flat monthly fee with the work going to voicemail today.</p></div>{calc_block()}</div></section>
<section class="section"><div class="wrap"><div class="head"><h2>How We Compare</h2></div>{compare_table()}</div></section>
<section class="section bg-2"><div class="wrap"><div class="head"><h2>Pricing FAQ</h2></div>{faq_block(pf)}</div></section>''' + cta("Get Your Custom Quote","Tell us the hours and tasks you need covered. We reply within a few hours.")
    page("/pricing/","Virtual Receptionist Pricing, No Contracts | Top Dispatch",
         "Flat monthly pricing for a dedicated virtual receptionist or dispatcher. Part-time, full-time or 24/7 coverage. No setup fees, no per-minute charges, month to month.",body,"Pricing",[faq_ld(pf)],cr)

# ================= HOW IT WORKS =================
def how():
    cr=[("Home","/"),("How It Works","/how-it-works/")]
    need = ["Your greeting and how you want calls answered","Your price sheet, fees and services you don't offer","Your service area by ZIP code or map","Technicians, skills and on-call rota","Logins for your phone system and job software","Emergency rules and escalation contacts"]
    hf=[("How long does onboarding take?","Most clients are live within 48 to 72 hours of signing up."),("Do I interview the candidate?","Yes. You interview your matched secretary before anything starts."),("How do calls reach my secretary?","Usually by forwarding your business line or adding your secretary to your phone system's ring group. Your number doesn't change."),("What happens in the first week?","Your secretary shadows your scripts, you review call summaries daily and we fine-tune the rules together.")]
    timeline = [("Day 0","Tell us what you need","Short intake form: trade, hours, tasks. Under five minutes."),("Day 1","Meet your match","We put forward secretaries with experience in your trade. You interview and choose."),("Day 2","Briefing &amp; access","We set up logins, load your scripts and price sheet, and test call forwarding."),("Day 3","First shift","Your secretary starts answering, booking and dispatching. You get a daily summary."),("Week 2+","Optimise","We review results with you and add tasks such as follow-ups or back office.")]
    tl = "".join(f'<div class="log-item t-cyan"><div><div class="k">{d}</div></div><div><p><strong>{h}</strong></p><p class="out">{p}</p></div></div>' for d,h,p in timeline)
    body = hero_sub("zap","48–72 Hours to Live","How It","Works","Three steps from sign-up to a dedicated secretary answering your phones.",cr) + \
      f'<section class="section"><div class="wrap">{steps_block()}</div></section>' + f'''
<section class="section bg-2"><div class="wrap split" style="align-items:start">
 <div><h2 style="margin-bottom:18px">Your Onboarding Timeline</h2><div class="log">{tl}</div></div>
 <div class="prose"><h2>What We Need From You</h2><p>Gather these before your briefing and your secretary sounds like part of the team from the first call.</p>{checks(need,True)}<div class="mt-m">{btn()}</div></div>
</div></section>
<section class="section"><div class="wrap"><div class="head"><h2>Onboarding FAQ</h2></div>{faq_block(hf)}</div></section>''' + cta("Ready to Get Started?","Tell us what you need and meet your match this week.")
    ld=[{"@type":"HowTo","name":"How to get a Top Dispatch virtual secretary","totalTime":"P3D","step":[{"@type":"HowToStep","position":k+1,"name":h,"text":p} for k,(_,_,_,h,p) in enumerate(STEPS)]},faq_ld(hf)]
    page("/how-it-works/","How It Works: Get a Virtual Receptionist in 48–72 Hours | Top Dispatch",
         "Sign up, interview your matched secretary and hand over the phones. See the Top Dispatch onboarding timeline and what we need from you.",body,None,ld,cr)

# ================= WHY PHILIPPINES =================
def why():
    cr=[("Home","/"),("Why the Philippines","/why-the-philippines/")]
    wf=[("Is it safe to hire a virtual assistant from the Philippines?","Working through a managed provider like Top Dispatch means candidates are vetted, trained and supervised, with replacements if a fit isn't right, and access is limited to the tools you share."),
        ("Will a Filipino receptionist understand American customers?","Our secretaries are trained on US business culture, home service vocabulary and customer expectations, and you interview them before they start."),
        ("How do time zones work?","Manila is UTC+8, roughly 12 to 16 hours ahead of the mainland US. Your secretary works night shift there to cover your day here."),
        ("Is it cheaper than a local hire?","Usually, because there are no US payroll taxes, benefits, office costs or recruiting fees. You pay one flat monthly fee.")]
    body = hero_sub("globe","Remote Staffing Done Right","Why the","Philippines?","A large, experienced, English-speaking workforce that already works US hours.",cr) + \
      answer_box("Why hire a virtual receptionist from the Philippines?","The Philippines combines strong English proficiency, deep familiarity with American business culture and one of the world's largest IT and business-process workforces, much of which already works US hours. That makes it a practical place to hire experienced receptionists and dispatchers for US home service businesses at a lower total cost than a local hire.") + \
      f'<section class="section"><div class="wrap">{why_block()}</div></section>' + \
      stats([("message","#28","Global rank, EF English Proficiency Index 2025"),("users","1.9M","IT &amp; business-process workers (IBPAP, 2025)"),("award","2-5 yrs","Experience per Top Dispatch secretary"),("clock","48-72h","From sign-up to first shift")]) + f'''
<section class="section"><div class="narrow prose">
 <h2>Your Receptionist Works Your Clock</h2>
 <p>Manila runs 12 to 16 hours ahead of the mainland US, depending on daylight saving time. Your secretary works the Philippine night shift so they are fully on during your business day, whether you are in New York, Chicago, Denver or Los Angeles.</p>
 <h3>Experience that transfers</h3>
 <p>Many of our secretaries come from US-facing call centers and BPO roles where they handled scheduling, customer service and outbound calling. We add trade-specific training so they understand furnaces, sewer lines and torsion springs before day one.</p>
 <h3>Sources</h3>
 <p>English ranking: <a href="https://www.ef.com/wwen/epi/" rel="noopener">EF English Proficiency Index</a>. Workforce figure: IBPAP industry estimates reported for end of 2025.</p>
</div></section>
<section class="section bg-2"><div class="wrap"><div class="head"><h2>Hiring in the Philippines FAQ</h2></div>{faq_block(wf)}</div></section>''' + cta("Meet Your Philippine-Based Secretary","Interview your match before you commit. Live in 48 to 72 hours.")
    page("/why-the-philippines/","Why Hire a Virtual Receptionist from the Philippines | Top Dispatch",
         "English proficiency, US business culture and a 1.9M-strong BPO workforce. Why Top Dispatch staffs home service receptionists from the Philippines.",body,None,[faq_ld(wf)],cr)

# ================= GUIDES =================
GUIDES = [
 dict(slug="answering-service-cost", title="How Much Does an Answering Service Cost? (2026 Guide for Home Services)",
  h1a="How Much Does an", h1b="Answering Service Cost?",
  meta="Answering service pricing explained for contractors: per-minute, per-call and flat-rate models, hidden fees, and when a dedicated receptionist costs less.",
  lead="Per minute, per call or a flat monthly fee. Here's how answering service pricing works for home service companies and how to compare options fairly.",
  answer="Answering service cost depends on the pricing model. Shared answering services usually charge per minute or per call with a monthly minimum, plus overage, holiday or after-hours fees. AI receptionists charge a monthly plan sized by call volume. A dedicated remote receptionist, like Top Dispatch, charges a flat monthly fee for a set number of hours, so the cost doesn't rise with call volume.",
  sections=[
   ("The three pricing models","<p><strong>Per minute.</strong> The most common model for shared answering services. You buy a bundle of minutes each month and pay overage when you go over. Watch how minutes are counted: some providers round each call up, or count hold and transfer time.</p><p><strong>Per call.</strong> A set price per answered call. Simple to budget at low volume, but expensive in a busy season and it often doesn't include booking or dispatch.</p><p><strong>Flat monthly.</strong> You pay for a person's time, regardless of how many calls come in. This is how Top Dispatch prices a dedicated receptionist.</p>"),
   ("Fees to ask about","<ul><li>Setup or onboarding fees</li><li>Monthly minimums</li><li>Overage rates</li><li>After-hours, weekend or holiday surcharges</li><li>Charges for appointment booking, warm transfers or software integration</li><li>Long-term contract and cancellation terms</li></ul><p>Top Dispatch has no setup fees and no long-term contract. Service is month to month.</p>"),
   ("When per-minute gets expensive","<p>Home service calls are rarely short. A good intake call for a no-heat emergency or a water heater quote takes several minutes, and busy seasons multiply volume. At steady daily volume, the per-minute bill can match or exceed the cost of a dedicated person who also books, dispatches and follows up.</p>"),
   ("How to compare fairly","<p>Estimate your monthly call count and average call length, then price each option against the same month. Add the value of what happens after the call: a message taken versus a job booked and dispatched. Our <a href=\"/pricing/\">missed-call calculator</a> helps put a number on calls that currently go to voicemail.</p>"),
   ("Bottom line","<p>Low volume or overflow only? A shared service may be enough. Steady daily calls and you need booking and dispatch? A dedicated receptionist is usually better value. <a href=\"/contact/\">Get a quote</a> for your hours.</p>")]),
 dict(slug="ai-receptionist-vs-human-receptionist", title="AI Receptionist vs. Human Receptionist for Home Services",
  h1a="AI Receptionist", h1b="vs. Human Receptionist",
  meta="Should a contractor use an AI receptionist or a human one? Compare call handling, dispatch, cost and customer experience for home service businesses.",
  lead="AI voice agents are getting better fast. Here's where they work for home service companies, where a trained human still wins, and how to combine both.",
  answer="An AI receptionist is good at answering instantly, handling simple FAQs and booking open slots, especially after hours. A human receptionist is better at judgment calls: triaging emergencies, calming upset customers, ringing a technician and reshuffling the schedule when jobs collide. Many home service businesses use a human for business hours and dispatch, with AI covering overflow.",
  sections=[
   ("Where AI receptionists do well","<ul><li>Answering every call instantly, even at 3 AM</li><li>Common questions: hours, service area, basic pricing</li><li>Booking into open calendar slots through integrations</li><li>Handling overflow when lines are busy</li></ul>"),
   ("Where a human receptionist wins","<ul><li>Emergency triage with follow-up questions that depend on the answer</li><li>Talking a caller to the water shutoff or out of a gas smell</li><li>Calling a technician and solving a schedule clash</li><li>Handling complaints, upset customers and sensitive situations</li><li>Following up on estimates and selling maintenance plans</li></ul>"),
   ("Cost comparison","<p>AI plans are usually priced by call volume or minutes. A dedicated human costs a flat monthly fee but also covers dispatch, follow-ups and back-office work in quiet hours. Compare what each option actually <em>does</em> per dollar, not just answer rate. See <a href=\"/guides/answering-service-cost/\">how answering service pricing works</a>.</p>"),
   ("A practical combination","<p>Use a dedicated human for your business day and dispatch, and an AI or after-hours human for overflow and nights. Top Dispatch offers <a href=\"/services/after-hours-answering/\">after-hours answering</a> with a real person if you want humans around the clock.</p>")]),
 dict(slug="how-to-hire-a-virtual-receptionist", title="How to Hire a Virtual Receptionist for Your Home Service Business",
  h1a="How to Hire a", h1b="Virtual Receptionist",
  meta="A step-by-step checklist for hiring a virtual receptionist for HVAC, plumbing, electrical and other trades: what to prepare, what to ask and how to onboard.",
  lead="A practical checklist for owners: what to prepare, what to ask providers, and how to get your new receptionist productive in the first week.",
  answer="To hire a virtual receptionist, first define the hours and tasks you need covered, then compare providers on whether you get a dedicated person, trade experience, software access, pricing model and contract terms. Interview the candidate, prepare your call script, price sheet and emergency rules, set up logins and call forwarding, and review call summaries daily during the first week.",
  sections=[
   ("1. Define what you need","<p>List the hours that need cover and the tasks: answering, booking, dispatch, estimate follow-up, admin. Most owners start with the phones and add tasks once the receptionist knows the business.</p>"),
   ("2. Questions to ask providers","<ul><li>Will I have the same person every day?</li><li>Have they worked in my trade?</li><li>Can I interview them first?</li><li>Will they work inside my software?</li><li>How is pricing calculated, and is there a contract?</li><li>What happens when they're sick?</li></ul>"),
   ("3. Prepare your playbook","<p>Write down your greeting, services and exclusions, price sheet, service area, technician skills, on-call rota and emergency rules. This is what turns a good receptionist into <em>your</em> receptionist.</p>"),
   ("4. Set up access","<p>Create a user login in your field-service software and phone system with only the permissions needed. Forward your line or add the receptionist to your ring group.</p>"),
   ("5. Run the first week closely","<p>Read call summaries daily, correct anything early and add notes to the playbook. By week two most owners are spending far less time on the phone. <a href=\"/how-it-works/\">See how Top Dispatch onboarding works</a>.</p>")]),
]
def guides_hub():
    cr=[("Home","/"),("Guides","/guides/")]
    cards="".join(f'<a class="card t-cyan" href="/guides/{g["slug"]}/"><div class="ic">{I("book")}</div><h3>{g["h1a"]} {g["h1b"]}</h3><p>{g["lead"]}</p><span class="more">Read the guide {I("arrow")}</span></a>' for g in GUIDES)
    body = hero_sub("book","Owner Resources","Guides for","Home Service Owners","Plain-English guides on answering services, receptionists and running a tighter front office.",cr) + \
      f'<section class="section-tight" style="padding-bottom:96px"><div class="wrap grid g3">{cards}</div></section>' + cta("Prefer to Talk It Through?","Tell us about your business and we'll recommend the right coverage.")
    page("/guides/","Guides for Home Service Owners | Top Dispatch",
         "Guides for home service owners on answering service costs, AI vs. human receptionists and how to hire a virtual receptionist.",body,"Guides",
         [{"@type":"CollectionPage","url":DOMAIN+"/guides/","name":"Top Dispatch guides","hasPart":[{"@type":"Article","headline":g["title"],"url":f'{DOMAIN}/guides/{g["slug"]}/'} for g in GUIDES]}],cr)
def guide_page(g):
    path=f'/guides/{g["slug"]}/'
    cr=[("Home","/"),("Guides","/guides/"),(g["h1a"]+" "+g["h1b"],path)]
    ids=[f"s{k}" for k in range(len(g["sections"]))]
    toc="".join(f'<li><a href="#{ids[k]}">{h}</a></li>' for k,(h,_) in enumerate(g["sections"]))
    secs="".join(f'<h2 id="{ids[k]}">{h}</h2>{c}' for k,(h,c) in enumerate(g["sections"]))
    others="".join(f'<a href="/guides/{x["slug"]}/">{x["h1a"]} {x["h1b"]}</a>' for x in GUIDES if x["slug"]!=g["slug"])
    body = hero_sub("book","Guide",g["h1a"],g["h1b"],g["lead"],cr,extra=f'<p class="meta">By the Top Dispatch team · Updated <time datetime="{TODAY}">October 20, 2026</time></p>') + \
      answer_box("The short answer", g["answer"]) + \
      f'<article class="article"><div class="narrow prose"><nav class="toc" aria-label="Contents"><b>In this guide</b><ol>{toc}</ol></nav>{secs}<div class="mt-l">{btn("Get matched with a receptionist")}</div></div></article>' + \
      f'<section class="section-tight bg-2"><div class="wrap"><div class="head" style="margin-bottom:24px"><h2 style="font-size:1.6rem">More Guides</h2></div><div class="links">{others}</div></div></section>' + \
      cta("Stop Sending Calls to Voicemail","A dedicated receptionist who knows your trade. Month to month, live in 48 to 72 hours.")
    ld=[{"@type":"Article","headline":g["title"],"description":g["meta"],"url":DOMAIN+path,"mainEntityOfPage":DOMAIN+path,"datePublished":TODAY,"dateModified":TODAY,
         "author":{"@type":"Organization","name":BRAND,"url":DOMAIN+"/"},"publisher":{"@id":DOMAIN+"/#org"},"image":DOMAIN+"/assets/og.png"}]
    page(path,(g["title"] if len(g["title"])<=60 else g["h1a"]+" "+g["h1b"])+" | Top Dispatch",g["meta"],body,"Guides",ld,cr,"article")

# ================= LEGAL =================
def legal(path, name, intro, sections):
    cr=[("Home","/"),(name,path)]
    secs="".join(f"<h2>{h}</h2><p>{p}</p>" for h,p in sections)
    body = hero_sub("shield","Legal",name.split()[0],(" ".join(name.split()[1:])),intro,cr,extra=f'<p class="meta">Last updated <time datetime="{TODAY}">October 20, 2026</time></p>') + f'<article class="article"><div class="narrow prose">{secs}<p>Questions? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></article>'
    page(path,f"{name} | Top Dispatch",f"{name} for the Top Dispatch website and services.",body,None,None,cr)

def build_legal():
    legal("/privacy/","Privacy Policy","How Top Dispatch collects, uses and protects your information.",[
     ("Information we collect","When you leave your details we collect your name, email, phone number, trade and any message you send. Our website may also collect standard technical data such as browser type and pages visited."),
     ("How we use it","We use your information to respond to your inquiry, provide and improve our services, and send service-related communications. We do not sell your personal information."),
     ("Client data","When you use our services, our staff access your systems only as needed to perform the agreed work, using credentials and permissions you control."),
     ("Sharing","We share information only with service providers that help us operate (for example email and hosting), when required by law, or with your consent."),
     ("Your choices","You can ask us to access, correct or delete your personal information by emailing us. You can opt out of marketing messages at any time."),
     ("Security","We use reasonable administrative and technical safeguards. No method of transmission over the internet is completely secure."),
     ("Changes","We may update this policy and will post the new date at the top of this page.")])
    legal("/terms/","Terms of Service","The terms that apply when you use the Top Dispatch website.",[
     ("Use of this website","By using this website you agree to these terms. The content is provided for general information about our services."),
     ("Services","Services are provided under a separate agreement with each client, which governs scope, fees, notice periods and responsibilities."),
     ("Month-to-month service","Unless your agreement states otherwise, service is month to month and may be cancelled with 30 days' notice."),
     ("No professional advice","Guides on this site are general information, not legal, financial or compliance advice. Consult your own advisor."),
     ("Intellectual property","The Top Dispatch name, logo and website content belong to Top Dispatch and may not be used without permission."),
     ("Limitation of liability","To the extent permitted by law, Top Dispatch is not liable for indirect or consequential losses arising from use of this website."),
     ("Governing law","These terms are governed by the laws of the State of California.")])

def not_found():
    body=f'<section class="hero" style="padding:120px 0"><div class="wrap"><span class="badge">404</span><h1 style="font-size:clamp(2.4rem,5vw,3.6rem)">This page isn\'t on the schedule</h1><p class="lead">The link may be old or mistyped. Try one of these instead.</p><div class="links mt-m"><a href="/">Home</a><a href="/services/">Services</a><a href="/industries/">Industries</a><a href="/pricing/">Pricing</a><a href="/contact/">Leave details</a></div></div></section>'
    page("/404/","Page not found | Top Dispatch","The page you were looking for could not be found.",body)
    os.replace(OUT+"/404/index.html", OUT+"/404.html"); os.rmdir(OUT+"/404"); SITEMAP.remove("/404/")

def extras():
    pri = lambda p: "1.0" if p=="/" else ("0.9" if p in ("/services/","/industries/","/pricing/","/contact/") else ("0.8" if p.startswith(("/services/","/industries/")) else "0.6"))
    urls="".join(f"<url><loc>{DOMAIN}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pri(p)}</priority></url>" for p in SITEMAP)
    open(OUT+"/sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open(OUT+"/robots.txt","w").write(f"""User-agent: *
Allow: /

# AI search and answer engines are welcome
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Applebot-Extended
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
""")
    svc="\n".join(f'- [{s["name"]}]({DOMAIN}/services/{s["slug"]}/): {s["short"]}' for s in SERVICES)
    ind="\n".join(f'- [{i["name"]} answering service]({DOMAIN}/industries/{i["slug"]}/): {i["short"]}' for i in INDUSTRIES)
    gd="\n".join(f'- [{g["title"]}]({DOMAIN}/guides/{g["slug"]}/)' for g in GUIDES)
    faqs="\n".join(f"- Q: {q}\n  A: {a}" for q,a in HOME_FAQ)
    open(OUT+"/llms.txt","w").write(f"""# Top Dispatch

> Top Dispatch places dedicated remote receptionists, dispatchers and back-office assistants from the Philippines with US home service businesses (HVAC, plumbing, electrical, locksmith, roofing, garage door, pest control, cleaning, landscaping, contractors and more). One trained person works your hours inside your software. Flat monthly fee, no setup fees, month to month, live in 48 to 72 hours.

## Key facts
- Founded: 2023
- Headquarters: Beverly Hills, CA 90212, USA
- Team location: Philippines
- Clients: 153+ active US businesses
- Staff experience: 2 to 5 years in appointment setting, dispatch, cold calling or back office
- Onboarding: 48 to 72 hours; clients interview their match first
- Pricing: flat monthly fee by hours and scope; no per-minute charges, no setup fees, 30 days' notice to cancel
- Coverage: client's US time zone; business hours, after hours, weekends or 24/7
- Phone: {PHONE}
- Email: {EMAIL}

## Services
{svc}

## Industries
{ind}

## Company
- [About]({DOMAIN}/about/)
- [How it works]({DOMAIN}/how-it-works/)
- [Pricing]({DOMAIN}/pricing/)
- [Why the Philippines]({DOMAIN}/why-the-philippines/)
- [Reviews]({DOMAIN}/reviews/)
- [FAQ]({DOMAIN}/faq/)
- [Contact]({DOMAIN}/contact/)

## Guides
{gd}

## Frequently asked questions
{faqs}
""")
    open(OUT+"/site.webmanifest","w").write(json.dumps({"name":BRAND,"short_name":BRAND,"icons":[{"src":"/assets/logo-192.png","sizes":"192x192","type":"image/png"},{"src":"/assets/logo.png","sizes":"512x512","type":"image/png"}],"theme_color":"#1b2350","background_color":"#030616","display":"standalone","start_url":"/"},indent=1))
    open(OUT+"/vercel.json","w").write(json.dumps({"cleanUrls":True,"trailingSlash":True,
      "redirects":[{"source":"/ServicesPage","destination":"/services/","permanent":True},{"source":"/AboutPage","destination":"/about/","permanent":True},
                   {"source":"/ReviewsPage","destination":"/reviews/","permanent":True},{"source":"/FAQPage","destination":"/faq/","permanent":True},
                   {"source":"/IndustriesPage","destination":"/industries/","permanent":True},{"source":"/ContactPage","destination":"/contact/","permanent":True}],
      "headers":[{"source":"/assets/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]},
                 {"source":"/(.*)","headers":[{"key":"X-Content-Type-Options","value":"nosniff"},{"key":"Referrer-Policy","value":"strict-origin-when-cross-origin"},{"key":"X-Frame-Options","value":"SAMEORIGIN"}]}]},indent=1))

if __name__=="__main__":
    home(); services_hub(); [service_page(s) for s in SERVICES]
    industries_hub(); [industry_page(i) for i in INDUSTRIES]
    about(); reviews(); faq_page(); contact(); pricing(); how(); why()
    guides_hub(); [guide_page(g) for g in GUIDES]; build_legal(); not_found(); extras()
    print(len(SITEMAP),"pages")
