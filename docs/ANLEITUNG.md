# dolavolt – Website live schalten (Cloudflare Pages)

## 1. Vor dem Upload ersetzen
- **Gelb markierte Platzhalter:** alle Angaben im Impressum.
- **Kompetenzliste ehrlich halten:** Der Block „Kompetenzen und Werkzeuge“ und die Werkzeug-Absätze auf den Leistungsseiten nennen viele Tools (z. B. Vector DaVinci, EB tresos, dSPACE, ECU-TEST, TargetLink, AURIX, S32K). **Streicht alles, was ihr nicht wirklich beherrscht.** Kunden und Agenturen fragen genau danach, und falsche Angaben schaden mehr als eine kurze Liste.
- **Domain und E-Mail:** `https://www.dolavolt.de` und `hallo@dolavolt.de` ggf. ersetzen (am besten in `tools/src/` ersetzen und `python3 tools/build.py` ausführen).
- **Zusagen prüfen:** Antwort innerhalb von zwei Werktagen, Einsatzorte München/Ingolstadt/Regensburg/Stuttgart.

## 2. Deployment
Siehe `README.md` im Repository-Root: Cloudflare Worker mit statischen Assets aus `site`, Deploy-Befehl `npx wrangler deploy`. `site/_headers` setzt Security-Header (CSP, HSTS usw.) und Caching automatisch.

## 3. Gefunden werden als Freelancer
1. **Google Search Console und Bing Webmaster Tools:** Domain verifizieren, `sitemap.xml` einreichen.
2. **Profile auf Freelance-Plattformen** (freelancermap, freelance.de, GULP, Malt) mit denselben Keywords anlegen und auf die Website verlinken. Ein Großteil der Automotive-Projekte läuft über diese Plattformen und über Personaldienstleister (Hays, SOLCOM, Etengo).
3. **LinkedIn:** persönliche Profile mit „Freelance BMS Software Engineer“ o. Ä. im Titel, „Open to work“ für Freelance, Unternehmensseite dolavolt verlinken.
4. **Google Unternehmensprofil** für dolavolt in München anlegen (hilft bei „Freelancer BMS München“).
5. **Profil-PDF** pro Ingenieur vorbereiten – wird fast immer angefragt.
6. **Status klären:** Vor dem ersten Auftrag Nebentätigkeit bzw. Wettbewerbsverbot beim aktuellen Arbeitgeber klären, und das Thema Scheinselbstständigkeit (mehrere Auftraggeber, eigene Ausstattung, klare Leistungsbeschreibung) im Blick behalten.

## Dateien
| Datei | Zweck |
|---|---|
| `index.html` / `en/index.html` | Startseite DE / EN |
| `leistungen/` | 7 Leistungsseiten inkl. Elektrifizierung Land- und Baumaschinen, plus Übersicht mit Kompetenzliste |
| `wissen/` | 6 Fachartikel (neu: Euro 7 und GB 38031) |
| `impressum.html`, `datenschutz.html`, `404.html` | Rechtliches |
| `sitemap.xml`, `robots.txt`, `_headers` | Suchmaschinen und Sicherheit |
