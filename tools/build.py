"""Erzeugt alle HTML-Seiten, sitemap.xml und robots.txt neu.

Aufruf:  python3 tools/build.py            (schreibt nach ./site)
         python3 tools/build.py <zielordner>

Die Inhalte stehen in tools/src/*.py. Die Teile werden in fester Reihenfolge
zusammengefügt, weil spätere Teile Funktionen aus früheren nutzen.
"""
import pathlib
import sys

PARTS = ["layout", "articles", "services", "home_helpers", "home_data", "visuals", "home", "design_test", "services_index", "legal_sitemap"]
here = pathlib.Path(__file__).resolve().parent
target = sys.argv[1] if len(sys.argv) > 1 else str(here.parent / "site")
code = "\n".join((here / "src" / f"{p}.py").read_text(encoding="utf-8") for p in PARTS)
sys.argv = [sys.argv[0], target]
exec(compile(code, "dolavolt-build", "exec"), {"__name__": "__main__"})
