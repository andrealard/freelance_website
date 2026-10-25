
# ---------- Designtest: Startseite mit warm.css unter /design-test/ (nicht indexiert) ----------
page("design-test/index.html", "Designtest | dolavolt", "Designtest der Startseite.", HOME_DE, robots="noindex,nofollow")
_dt = os.path.join(ROOT, "design-test", "index.html")
_h = open(_dt, encoding="utf-8").read()
import re
_h = re.sub(r'(<link rel="stylesheet" href="([^"]*)assets/styles\.css[^"]*">)', lambda m: m.group(1) + f'\n<link rel="preload" href="{m.group(2)}assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>\n<link rel="stylesheet" href="{m.group(2)}assets/warm.css?v=1">', _h, count=1)
open(_dt, "w", encoding="utf-8").write(_h)
