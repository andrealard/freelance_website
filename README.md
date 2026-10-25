# dolavolt – Website

Statische Website (HTML/CSS, kein JavaScript, keine Cookies) für dolavolt: Batteriemanagement und funktionale Sicherheit für Hochvolt-Batteriesysteme.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `site/` | Die fertige Website – genau dieser Ordner wird ausgeliefert |
| `site/_headers` | Security- und Cache-Header |
| `site/404.html` | Fehlerseite (über `not_found_handling`) |
| `tools/build.py` | Erzeugt alle Seiten, `sitemap.xml` und `robots.txt` aus `tools/src/` neu |
| `tools/src/` | Texte und Seitenvorlagen (Startseite, Leistungen, Fachartikel, Rechtliches) |
| `docs/` | Anleitung zum Livegang und Keyword-Recherche |
| `wrangler.toml` | Cloudflare-Konfiguration (Worker mit statischen Assets aus `site`) |

## Hosting auf Cloudflare (Workers mit statischen Assets)

Das Projekt ist als Cloudflare Worker mit statischen Assets konfiguriert (`wrangler.toml`, Ordner `site`). Es gibt keinen Build-Schritt.

1. Cloudflare-Dashboard → **Workers & Pages** → **Create** → **Import a repository** → `andrealard/freelance_website`.
2. Build-Einstellungen: **Build command** leer lassen, **Deploy command** `npx wrangler deploy` (Standard).
3. Deploy. Die Seite ist danach unter `https://<worker-name>.<account>.workers.dev` erreichbar.
4. **Settings → Domains & Routes** → Custom Domain `www.dolavolt.de` und `dolavolt.de` hinzufügen.
5. Weiterleitung `dolavolt.de` → `https://www.dolavolt.de`: **Rules → Redirect Rules**, 301.

Der `name` in `wrangler.toml` muss dem Worker-Namen im Dashboard entsprechen. Weicht er ab, öffnet Cloudflare automatisch einen Pull Request, der ihn korrigiert – einfach mergen.

Jeder Push auf `main` veröffentlicht die Seite automatisch neu.

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
