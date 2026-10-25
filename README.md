# dolavolt – Website

Statische Website (HTML/CSS, kein JavaScript, keine Cookies) für dolavolt: Batteriemanagement und funktionale Sicherheit für Hochvolt-Batteriesysteme.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `site/` | Die fertige Website – genau dieser Ordner wird ausgeliefert |
| `site/_headers` | Security- und Cache-Header für Cloudflare Pages |
| `site/404.html` | Fehlerseite (wird von Cloudflare Pages automatisch genutzt) |
| `tools/build.py` | Erzeugt alle Seiten, `sitemap.xml` und `robots.txt` aus `tools/src/` neu |
| `tools/src/` | Texte und Seitenvorlagen (Startseite, Leistungen, Fachartikel, Rechtliches) |
| `docs/` | Anleitung zum Livegang und Keyword-Recherche |
| `wrangler.toml` | Cloudflare-Pages-Konfiguration (Ausgabeordner `site`) |

## Hosting auf Cloudflare Pages (Git-Anbindung)

1. Cloudflare-Dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
2. GitHub verbinden und das Repository `andrealard/freelance_website` auswählen.
3. Build-Einstellungen:
   - **Production branch:** `main`
   - **Framework preset:** `None`
   - **Build command:** *leer lassen*
   - **Build output directory:** `site`
4. **Save and Deploy.** Die Seite ist danach unter `https://<projektname>.pages.dev` erreichbar.
5. **Custom domains** → `www.dolavolt.de` und `dolavolt.de` hinzufügen (Domain muss bei Cloudflare liegen oder per CNAME zeigen).
6. Weiterleitung `dolavolt.de` → `https://www.dolavolt.de`: **Rules → Redirect Rules**, 301.

Jeder Push auf `main` veröffentlicht die Seite automatisch neu. Pushes auf andere Branches erzeugen eine Vorschau-URL.

Alternativ ohne Git-Anbindung: `npx wrangler pages deploy` im Repository-Root (liest `wrangler.toml`).

## Inhalte ändern

Texte in `tools/src/*.py` bearbeiten, dann:

```bash
python3 tools/build.py
```

und die geänderten Dateien in `site/` committen. Kleine Korrekturen können auch direkt in `site/*.html` gemacht werden – sie werden aber beim nächsten Build überschrieben.

## Vor dem Livegang

Siehe `docs/ANLEITUNG.md`. Wichtig:

- Impressum ausfüllen (gelb markierte Platzhalter in `impressum.html` bzw. `tools/src/legal_sitemap.py`)
- Domain und E-Mail (`www.dolavolt.de`, `hallo@dolavolt.de`) prüfen
- Kompetenz- und Werkzeuglisten auf das kürzen, was tatsächlich beherrscht wird
- Name „dolavolt“ im Marken- und Handelsregister sowie die Domain prüfen
