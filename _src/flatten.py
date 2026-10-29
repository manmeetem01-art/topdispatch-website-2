import os,re,json,shutil
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
HERE=pathlib.Path(__file__).resolve().parent
SRC=str(HERE/"_site"); OUT=str(HERE.parent); D=__import__("content").DOMAIN

def fix(t):
    t=t.replace('"/assets/','"/').replace(D+"/assets/",D+"/")
    t=re.sub(r'('+re.escape(D)+r'|href=")(/[a-z0-9][a-z0-9\-/]*?)/(?=["#\s\)<\]])',r'\1\2',t)
    return t
rew=[]; pages=[]
for d,_,fs in os.walk(SRC):
    for f in fs:
        if f!="index.html": continue
        p=d[len(SRC):] or ""
        name="index.html" if p=="" else p.strip("/").replace("/","-")+".html"
        open(f"{OUT}/{name}","w").write(fix(open(os.path.join(d,f)).read()))
        url="/" if p=="" else p
        pages.append(url)
        if p.count("/")>=2: rew.append({"source":url,"destination":"/"+name[:-5]})
open(OUT+"/404.html","w").write(fix(open(SRC+"/404.html").read()))
for f in os.listdir(SRC+"/assets"): shutil.copy(f"{SRC}/assets/{f}",f"{OUT}/{f}")
for f in ["favicon.ico","robots.txt"]: shutil.copy(f"{SRC}/{f}",f"{OUT}/{f}")
open(OUT+"/site.webmanifest","w").write(open(SRC+"/site.webmanifest").read().replace('"/assets/','"/'))
open(OUT+"/llms.txt","w").write(fix(open(SRC+"/llms.txt").read()).replace(D+"/)",D+"/)"))
# llms has markdown links (url) -> fix trailing slash
t=open(OUT+"/llms.txt").read(); t=re.sub(r'('+re.escape(D)+r'/[a-z0-9\-/]+?)/\)',r'\1)',t); open(OUT+"/llms.txt","w").write(t)
pages.sort(key=lambda u:(u!="/",u))
pri=lambda u:"1.0" if u=="/" else "0.8"
open(OUT+"/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{D}{'' if u=='/' else u}{'/' if u=='/' else ''}</loc><lastmod>2026-10-29</lastmod><priority>{pri(u)}</priority></url>" for u in pages)+"</urlset>\n")
old=[("/ServicesPage","/services"),("/AboutPage","/about"),("/ReviewsPage","/reviews"),("/FAQPage","/faq"),("/IndustriesPage","/industries"),("/ContactPage","/contact")]
cfg={"cleanUrls":True,"trailingSlash":False,"rewrites":rew,
 "redirects":[{"source":"/:path*","has":[{"type":"host","value":"topdispatch-website-2.vercel.app"}],"destination":D+"/:path*","permanent":True}]+[{"source":a,"destination":b,"permanent":True} for a,b in old],
 "headers":[{"source":"/(.*)\\.(png|ico|css|js)","headers":[{"key":"Cache-Control","value":"public, max-age=86400"}]},
            {"source":"/(.*)","headers":[{"key":"X-Content-Type-Options","value":"nosniff"},{"key":"Referrer-Policy","value":"strict-origin-when-cross-origin"},{"key":"X-Frame-Options","value":"SAMEORIGIN"}]}]}
open(OUT+"/vercel.json","w").write(json.dumps(cfg,indent=1))
print(len(pages),"pages,",len(rew),"rewrites,",len(os.listdir(OUT)),"files")
