import json, os, sys
ROOT = sys.argv[1]
BASE = "https://www.dolavolt.de"
# Impressum und Datenschutz vorerst ausgeblendet: auf True setzen, sobald die Angaben stehen
LEGAL = False
LEGAL_PAGES = ("impressum.html", "datenschutz.html")
DATE = "2026-10-15"

LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true"><rect x="2" y="8" width="24" height="16" rx="2.5" fill="none" stroke="currentColor" stroke-width="2.6"/><rect x="26.5" y="13" width="3.5" height="6" rx="1" fill="#B5652F"/><rect x="6" y="12" width="4" height="8" fill="#1F44D6"/><rect x="12" y="12" width="4" height="8" fill="#1F44D6"/><rect x="18" y="12" width="4" height="8" fill="#1F44D6" opacity=".35"/></svg>'

T = {
 "de": dict(nav=[("#kompetenzen","Kompetenzen"),("leistungen/","Leistungen"),("#trends","Trends"),("#erfahrung","Erfahrung"),("wissen/","Wissen")], other=("en/","English","en"),
            cta="Projekt anfragen", skip="Zum Inhalt springen", tagline="BMS-Experten für Hochvolt-Batteriesysteme in Automotive und Landtechnik. Aus München.",
            fh=("Leistungen","Wissen","Kontakt"), imp="Impressum", dsg="Datenschutz", navlabel="Hauptnavigation"),
 "en": dict(nav=[("#skills","Competencies"),("#trends","Trends"),("#experience","Experience")], other=("","Deutsch","de"),
            cta="Discuss your project", skip="Skip to content", tagline="BMS experts for high-voltage battery systems in automotive and agricultural machinery. Based in Munich.",
            fh=("Services (DE)","Insights (DE)","Contact"), imp="Legal notice", dsg="Privacy", navlabel="Main navigation"),
}

SERVICES = [
 ("bms-softwareentwicklung", "BMS-Softwareentwicklung"),
 ("elektrifizierung-land-baumaschinen", "Elektrifizierung Land- und Baumaschinen"),
 ("funktionale-sicherheit-iso-26262", "Funktionale Sicherheit ISO 26262"),
 ("autosar-embedded-software", "AUTOSAR und Embedded Software"),
 ("matlab-simulink-modellbasierte-entwicklung", "MATLAB/Simulink"),
 ("test-absicherung-hil", "Test und HIL-Absicherung"),
 ("requirements-architektur-aspice", "Requirements und ASPICE"),
]

def header(r, lang):
    t = T[lang]; home = r + ("en/" if lang == "en" else "")
    items = "".join(f'<li><a href="{r}{h if not h.startswith("#") else h}">{l}</a></li>' if not h.startswith("#") else f'<li><a href="{home}{h}">{l}</a></li>' for h, l in t["nav"])
    o = t["other"]
    ctah = f'{home}#{"kontakt" if lang=="de" else "contact"}'
    return f'''<header class="site-header">
 <nav class="wrap nav" aria-label="{t["navlabel"]}">
  <a class="logo" href="{home}">{LOGO}dolavolt</a>
  <ul>{items}</ul>
  <div class="nav-right">
   <a class="lang" href="{r}{o[0]}" hreflang="{o[2]}" lang="{o[2]}">{o[1]}</a>
   <a class="btn small" href="{ctah}">{t["cta"]}</a>
  </div>
 </nav>
</header>'''

def footer(r, lang):
    t = T[lang]; home = r + ("en/" if lang == "en" else "")
    return f'''<footer>
 <div class="wrap">
  <div class="foot">
   <div><a class="logo" href="{home}">{LOGO}dolavolt</a><p>{t["tagline"]}</p></div>
   <div><h4>{t["fh"][0]}</h4><ul>{"".join(f'<li><a href="{r}leistungen/{sl}.html">{nm}</a></li>' for sl, nm in SERVICES)}</ul></div>
   <div><h4>{t["fh"][1]}</h4><ul><li><a href="{r}wissen/euro-7-gb-38031-bms.html">Euro 7 und GB 38031</a></li><li><a href="{r}wissen/eu-batteriepass-2027.html">Batteriepass 2027</a></li><li><a href="{r}wissen/ki-funktionale-sicherheit.html">KI und ISO 26262</a></li><li><a href="{r}wissen/cloud-bms-digitaler-zwilling.html">Cloud-BMS</a></li><li><a href="{r}wissen/">{"Alle Artikel" if lang=="de" else "All articles (German)"}</a></li></ul></div>
   <div><h4>{t["fh"][2]}</h4><ul><li><a href="mailto:hallo@dolavolt.de">hallo@dolavolt.de</a></li><li><a href="{r}{t["other"][0]}">{t["other"][1]}</a></li></ul></div>
  </div>
  <div class="legal"><span>© 2026 dolavolt</span>{f'<span><a href="{r}impressum.html">{t["imp"]}</a>&ensp;<a href="{r}datenschutz.html">{t["dsg"]}</a></span>' if LEGAL else ""}</div>
 </div>
</footer>'''

def page(path, title, desc, body, schema=None, robots="index,follow", ogtype="website", lang="de", extra_head="", absolute=False):
    if not LEGAL and path in LEGAL_PAGES: return
    depth = path.count("/")
    r = "/" if absolute else ("../" * depth if depth else "./")
    a = "/" if absolute else ("../" * depth)  # asset prefix
    url = BASE + "/" + path.replace("index.html", "")
    s = ('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + "</script>") if schema else ""
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#E8ECEF">
<meta name="author" content="dolavolt">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="dolavolt">
<meta property="og:locale" content="{"de_DE" if lang=="de" else "en_US"}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
{extra_head}<link rel="icon" href="{a}favicon.svg" type="image/svg+xml">
<link rel="preload" href="{a}assets/fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{a}assets/styles.css?v=4">
{s}
</head>
<body>
<a class="skip" href="#main">{T[lang]["skip"]}</a>
{header(r, lang)}
<main id="main">
{body.replace("{r}", r)}
</main>
{footer(r, lang)}
</body>
</html>
'''
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    open(full, "w", encoding="utf-8").write(html)

def article(slug, title, desc, headline, intro, content, faq, subj):
    url = f"{BASE}/wissen/{slug}.html"
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": headline, "description": desc, "inLanguage": "de-DE",
         "datePublished": DATE, "dateModified": DATE, "mainEntityOfPage": url, "image": f"{BASE}/assets/og.png",
         "author": {"@type": "Organization", "name": "dolavolt", "url": BASE + "/"},
         "publisher": {"@type": "Organization", "name": "dolavolt", "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/og.png"}}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Start", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Wissen", "item": BASE + "/wissen/"},
            {"@type": "ListItem", "position": 3, "name": headline, "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    body = f'''<article class="article">
<nav class="crumbs" aria-label="Brotkrumen"><a href="{{r}}">Start</a> / <a href="{{r}}wissen/">Wissen</a></nav>
<h1>{headline}</h1>
<p class="meta">Stand: 15. Oktober 2026</p>
<p class="lead">{intro}</p>
{content}
<h2>Häufige Fragen</h2>
{faq_html}
<div class="article-cta"><h2>Sie brauchen Verstärkung für Ihr BMS-Projekt?</h2><p>Wir bringen Serienerfahrung in BMS-Software, AUTOSAR, MATLAB/Simulink und funktionaler Sicherheit nach ISO 26262 in Ihr Team. Remote oder vor Ort.</p><a class="btn" href="mailto:hallo@dolavolt.de?subject=Projektanfrage%20({subj})">Projekt besprechen</a></div>
</article>'''
    page(f"wissen/{slug}.html", title, desc, body, schema, ogtype="article")

