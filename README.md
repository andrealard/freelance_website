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

Die Seite ist als Cloudflare Worker mit statischen Assets konfiguriert (`wrangler.toml`, Ordner `site`). Veröffentlicht wird per GitHub Action (`.github/workflows/deploy.yml`) bei jedem Push auf `main`. Die Cloudflare-GitHub-App wird dafür nicht gebraucht, so bleibt der dolavolt-Account unabhängig von anderen Cloudflare-Accounts.

Einmalig einrichten:

1. Cloudflare (dolavolt-Account): **My Profile → API Tokens → Create Token → Vorlage „Edit Cloudflare Workers“**, bei *Account Resources* den dolavolt-Account wählen, Token erstellen und kopieren.
2. GitHub: **Settings → Secrets and variables → Actions → New repository secret**
   - `CLOUDFLARE_API_TOKEN` = das Token
   - `CLOUDFLARE_ACCOUNT_ID` = Account-ID des dolavolt-Accounts
3. Cloudflare: **Workers & Pages → freelance-website → Settings → Build → Disable builds**, damit nicht doppelt veröffentlicht wird.
4. GitHub: **Actions → Deploy to Cloudflare → Run workflow** für den ersten Lauf.

Eigene Domain: **Settings → Domains & Routes** → `www.dolavolt.de` und `dolavolt.de`; Weiterleitung ohne www → mit www über **Rules → Redirect Rules** (301).

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
