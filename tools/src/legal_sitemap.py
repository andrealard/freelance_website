# ---------- Impressum / Datenschutz / 404 ----------
TD = lambda s: f'<span class="todo">{s}</span>'
page("impressum.html", "Impressum | dolavolt", "Impressum der dolavolt.",
 f'''<div class="legal-page"><h1>Impressum</h1>
<p>Angaben gemäß § 5 DDG</p>
<p>dolavolt {TD("[Rechtsform, z. B. GmbH / UG (haftungsbeschränkt) / GbR]")}<br>{TD("[Straße Hausnummer]")}<br>{TD("[PLZ]")} München<br>Deutschland</p>
<h2>Vertreten durch</h2><p>{TD("[Geschäftsführer/Gesellschafter: Vorname Nachname, Vorname Nachname]")}</p>
<h2>Kontakt</h2><p>E-Mail: hallo@dolavolt.de<br>Telefon: {TD("[optional]")}</p>
<h2>Registereintrag</h2><p>{TD("[Registergericht, HRB-Nummer – entfällt bei GbR]")}</p>
<h2>Umsatzsteuer-ID</h2><p>{TD("[USt-IdNr. gemäß § 27a UStG, sobald vorhanden]")}</p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2><p>{TD("[Vorname Nachname, Anschrift wie oben]")}</p>
<h2>EU-Streitschlichtung</h2><p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
</div>''', robots="noindex,follow")

page("datenschutz.html", "Datenschutzerklärung | dolavolt", "Datenschutzerklärung der dolavolt.",
 f'''<div class="legal-page"><h1>Datenschutzerklärung</h1>
<p class="todo">Vorlage – vor Veröffentlichung prüfen bzw. mit einem Generator (z.&nbsp;B. eRecht24) oder anwaltlich abgleichen.</p>
<h2>1. Verantwortlicher</h2><p>Verantwortlich im Sinne der DSGVO ist die im <a href="impressum.html">Impressum</a> genannte Stelle.</p>
<h2>2. Hosting über Cloudflare</h2><p>Diese Website wird über Cloudflare Pages ausgeliefert (Cloudflare, Inc., 101 Townsend St., San Francisco, CA 94107, USA). Beim Aufruf verarbeitet Cloudflare technisch notwendige Daten wie IP-Adresse, Zeitpunkt, aufgerufene Seite und Browserinformationen, um die Seite auszuliefern und vor Angriffen zu schützen. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Cloudflare ist unter dem EU-US Data Privacy Framework zertifiziert; zusätzlich besteht ein Auftragsverarbeitungsvertrag {TD("[mit Cloudflare abschließen: Data Processing Addendum im Dashboard]")}.</p>
<h2>3. Keine Cookies, kein Tracking</h2><p>Diese Website setzt keine Cookies und verwendet keine Analyse- oder Marketing-Tools. Schriften werden nicht von Drittanbietern geladen. {TD("[Falls Cloudflare Web Analytics aktiviert wird: cookielos, hier ergänzen]")}</p>
<h2>4. Kontaktformular und E-Mail</h2><p>Wenn Sie uns über das Kontaktformular oder per E-Mail kontaktieren, verarbeiten wir die von Ihnen angegebenen Daten (Name, Unternehmen, E-Mail-Adresse, optional Telefonnummer, Thema und Nachricht). Formularanfragen werden über Cloudflare (Cloudflare, Inc., USA; Auftragsverarbeitung, EU-Standardvertragsklauseln und Zertifizierung unter dem EU-U.S. Data Privacy Framework) als E-Mail an uns weitergeleitet und dort nicht gespeichert. Wir verarbeiten Ihre Angaben zur Bearbeitung der Anfrage (Art. 6 Abs. 1 lit. b bzw. f DSGVO) und löschen sie, sobald sie nicht mehr erforderlich sind und keine gesetzlichen Aufbewahrungspflichten bestehen.</p>
<h2>5. Ihre Rechte</h2><p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht auf Beschwerde bei einer Aufsichtsbehörde, z.&nbsp;B. dem Bayerischen Landesamt für Datenschutzaufsicht.</p>
</div>''', robots="noindex,follow")

page("404.html", "Seite nicht gefunden | dolavolt", "Diese Seite existiert nicht.",
 '<section><div class="wrap"><h1>Hier ist keine Seite.</h1><p class="lead" style="margin:24px 0 32px">Die Adresse existiert nicht oder wurde verschoben.</p><a class="btn" href="/">Zur Startseite</a></div></section>',
 robots="noindex", absolute=True)

# ---------- Sitemap / robots ----------
urls = [("/", "1.0", [("de", "/"), ("en", "/en/")]), ("/en/", "0.9", [("de", "/"), ("en", "/en/")]),
        ("/leistungen/", "0.9", None)] + [(f"/leistungen/{s}.html", "0.9", None) for s, _ in SERVICES] + [("/wissen/", "0.7", None)] + [(f"/wissen/{s}.html", "0.7", None) for s, *_ in items]
x = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for u, p, alt in urls:
    x.append(f"  <url><loc>{BASE}{u}</loc><lastmod>{DATE}</lastmod><priority>{p}</priority>")
    for l, h in (alt or []):
        x.append(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{BASE}{h}"/>')
    x.append("  </url>")
x.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(x) + "\n")
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
print("ok")
