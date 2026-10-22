# -*- coding: utf-8 -*-
"""Authoritative external sources per page, and the contextual internal-link map."""
import re

BLS_RECEP = ("U.S. Bureau of Labor Statistics: Receptionists (pay and outlook)", "https://www.bls.gov/ooh/office-and-administrative-support/receptionists.htm")
BLS_CSR = ("U.S. Bureau of Labor Statistics: Customer Service Representatives", "https://www.bls.gov/ooh/office-and-administrative-support/customer-service-representatives.htm")
FTC_TSR = ("FTC: Telemarketing Sales Rule", "https://www.ftc.gov/legal-library/browse/rules/telemarketing-sales-rule")
DNC = ("National Do Not Call Registry: access for telemarketers", "https://telemarketing.donotcall.gov/")
FCC_CALLS = ("FCC: Stop unwanted robocalls and texts", "https://www.fcc.gov/consumers/guides/stop-unwanted-robocalls-and-texts")
GOOGLE_REVIEWS = ("Google: Maps user-contributed content policy", "https://support.google.com/contributionpolicy/answer/7400114")
FTC_REVIEWS = ("FTC: Rule on the use of consumer reviews and testimonials", "https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-465-trade-regulation-rule-use-consumer-reviews-testimonials-final-rule")
CPSC_CO = ("CPSC: Carbon Monoxide Information Center", "https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center")
NFPA = ("National Fire Protection Association (NFPA)", "https://www.nfpa.org/")
SBA_FIN = ("SBA: Manage your business finances", "https://www.sba.gov/business-guide/manage-your-business/manage-your-finances")
IRS_SB = ("IRS: Small business and self-employed tax center", "https://www.irs.gov/businesses/small-businesses-self-employed")
EF_EPI = ("EF English Proficiency Index", "https://www.ef.com/wwen/epi/")
IBPAP = ("IT & Business Process Association of the Philippines (IBPAP)", "https://www.ibpap.org/")
ST = ("ServiceTitan", "https://www.servicetitan.com/")
HCP = ("Housecall Pro", "https://www.housecallpro.com/")
JOBBER = ("Jobber", "https://www.getjobber.com/")

SERVICE_SOURCES = {
 "virtual-receptionist": [BLS_RECEP, HCP, ST],
 "dispatch": [ST, HCP, JOBBER],
 "after-hours-answering": [CPSC_CO, NFPA, BLS_RECEP],
 "appointment-setting": [JOBBER, HCP, ST],
 "cold-calling": [FTC_TSR, DNC, FCC_CALLS],
 "back-office-support": [SBA_FIN, IRS_SB],
 "reporting-analytics": [SBA_FIN, ST],
 "customer-support": [GOOGLE_REVIEWS, FTC_REVIEWS],
}
INDUSTRY_SOURCES = {
 "hvac-answering-service": [("Air Conditioning Contractors of America (ACCA)","https://www.acca.org/"),("U.S. Department of Energy: Energy Saver","https://www.energy.gov/energysaver/energy-saver"),CPSC_CO],
 "plumbing-answering-service": [("Plumbing-Heating-Cooling Contractors Association (PHCC)","https://www.phccweb.org/"),("EPA WaterSense","https://www.epa.gov/watersense")],
 "electrician-answering-service": [("Electrical Safety Foundation (ESFI)","https://www.esfi.org/"),NFPA],
 "locksmith-answering-service": [("Associated Locksmiths of America (ALOA)","https://www.aloa.org/")],
 "roofing-answering-service": [("National Roofing Contractors Association (NRCA)","https://www.nrca.net/"),("National Weather Service","https://www.weather.gov/")],
 "garage-door-answering-service": [("Door & Access Systems Manufacturers Association (DASMA)","https://www.dasma.com/"),("International Door Association (IDA)","https://www.doors.org/")],
 "pest-control-answering-service": [("National Pest Management Association (NPMA)","https://www.npmapestworld.org/"),("EPA: Safe pest control","https://www.epa.gov/safepestcontrol")],
 "cleaning-business-answering-service": [("ISSA, the worldwide cleaning industry association","https://www.issa.com/")],
 "landscaping-answering-service": [("National Association of Landscape Professionals (NALP)","https://www.landscapeprofessionals.org/")],
 "contractor-answering-service": [("National Association of the Remodeling Industry (NARI)","https://www.nari.org/"),("National Association of Home Builders (NAHB)","https://www.nahb.org/")],
 "security-alarm-answering-service": [("The Monitoring Association (TMA)","https://tma.us/")],
 "chimney-answering-service": [("Chimney Safety Institute of America (CSIA)","https://www.csia.org/"),NFPA],
 "air-duct-cleaning-answering-service": [("National Air Duct Cleaners Association (NADCA)","https://nadca.com/"),("EPA: Indoor air quality","https://www.epa.gov/indoor-air-quality-iaq")],
 "medical-spa-answering-service": [("American Med Spa Association (AmSpa)","https://americanmedspa.org/")],
}
PAGE_SOURCES = {
 "/call-center-services/": [BLS_CSR, IBPAP, EF_EPI],
 "/answering-service/": [BLS_RECEP, FCC_CALLS],
 "/pricing/": [BLS_RECEP, BLS_CSR],
 "/": [BLS_RECEP, EF_EPI, IBPAP],
 "/services/": [BLS_RECEP, BLS_CSR],
 "/industries/": [BLS_RECEP],
 "/why-the-philippines/": [EF_EPI, IBPAP],
 "/guides/answering-service-cost/": [BLS_RECEP, BLS_CSR],
 "/guides/ai-receptionist-vs-human-receptionist/": [FCC_CALLS, BLS_RECEP],
 "/guides/how-to-hire-a-virtual-receptionist/": [BLS_RECEP, FTC_TSR],
}

# phrase -> target. Longer / more specific phrases first. Matched case-insensitively, whole words,
# first occurrence only, never inside headings or existing links, never to the current page.
LINK_MAP = [
 ("24/7 answering service", "/answering-service/"),
 ("answering service", "/answering-service/"),
 ("outsourced call center", "/call-center-services/"),
 ("call center", "/call-center-services/"),
 ("virtual receptionist", "/services/virtual-receptionist/"),
 ("after-hours", "/services/after-hours-answering/"),
 ("after hours", "/services/after-hours-answering/"),
 ("on-call", "/services/after-hours-answering/"),
 ("dispatcher", "/services/dispatch/"),
 ("dispatch", "/services/dispatch/"),
 ("estimate follow-up", "/services/appointment-setting/"),
 ("open estimates", "/services/appointment-setting/"),
 ("confirm", "/services/appointment-setting/"),
 ("past customers", "/services/cold-calling/"),
 ("outbound", "/services/cold-calling/"),
 ("invoices", "/services/back-office-support/"),
 ("invoicing", "/services/back-office-support/"),
 ("weekly report", "/services/reporting-analytics/"),
 ("reviews", "/services/customer-support/"),
 ("complaints", "/services/customer-support/"),
 ("flat monthly fee", "/pricing/"),
 ("Philippines", "/why-the-philippines/"),
 ("AI receptionist", "/guides/ai-receptionist-vs-human-receptionist/"),
 ("HVAC", "/industries/hvac-answering-service/"),
 ("plumbing", "/industries/plumbing-answering-service/"),
 ("plumber", "/industries/plumbing-answering-service/"),
 ("electrician", "/industries/electrician-answering-service/"),
 ("roofing", "/industries/roofing-answering-service/"),
 ("locksmith", "/industries/locksmith-answering-service/"),
 ("garage door", "/industries/garage-door-answering-service/"),
 ("pest control", "/industries/pest-control-answering-service/"),
]

SKIP_TAGS = {"a", "h1", "h2", "h3", "h4", "th", "summary", "button", "title", "script", "style"}

def autolink(html_str, self_path, max_links=9):
    """Insert contextual internal links into prose. Returns new HTML."""
    used_targets = {self_path}
    count = 0
    parts = re.split(r"(<[^>]+>)", html_str)
    stack = []
    out = []
    for part in parts:
        if part.startswith("<"):
            m = re.match(r"<(/?)([a-zA-Z0-9]+)", part)
            if m:
                closing, tag = m.group(1) == "/", m.group(2).lower()
                if tag in SKIP_TAGS:
                    if closing:
                        if tag in stack:
                            stack.remove(tag)
                    elif not part.endswith("/>"):
                        stack.append(tag)
            out.append(part)
            continue
        if stack or count >= max_links or not part.strip():
            out.append(part)
            continue
        text = part
        for phrase, target in LINK_MAP:
            if count >= max_links:
                break
            if target in used_targets:
                continue
            rx = re.compile(r"(?<![\w/-])(" + re.escape(phrase) + r")(?![\w-])", re.I)
            # search only outside anchors already inserted into this text node
            pieces = re.split(r"(<a [^>]+>.*?</a>)", text)
            for k, pc in enumerate(pieces):
                if pc.startswith("<a "):
                    continue
                mm = rx.search(pc)
                if mm:
                    pieces[k] = pc[:mm.start()] + f'<a href="{target}">{mm.group(1)}</a>' + pc[mm.end():]
                    used_targets.add(target)
                    count += 1
                    break
            text = "".join(pieces)
        out.append(text)
    return "".join(out)

def sources_box(items, updated="October 22, 2026"):
    if not items:
        return ""
    lis = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{label}</a></li>' for label, u in items)
    return (f'<section class="section-tight"><div class="narrow"><div class="card"><h2 style="font-size:1.1rem;margin-bottom:8px">Sources &amp; further reading</h2>'
            f'<ul class="prose" style="margin:0;padding-left:1.1em;font-size:.9rem">{lis}</ul>'
            f'<p class="muted" style="font-size:.78rem;margin:12px 0 0">Last updated {updated}. External links open in a new tab.</p></div></div></section>')
