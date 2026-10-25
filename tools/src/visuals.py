
# =====================================================================
# Grafiken: Systemdiagramm, Fachskizzen zu den Herausforderungen, Icons
# =====================================================================
INK, COB, COP, MUT, LIN, PALE, ALU = "#141C26", "#1F44D6", "#B5652F", "#4A5765", "#C9D1D8", "#EEF2FD", "#E8ECEF"

def _t(x, y, s, size=14, w=400, fill=INK, anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{s}</text>'

def _box(x, y, w, h, fill="#fff", stroke=LIN, sw=1.2, r=6, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def _arrow(x1, y1, x2, y2, color=MUT):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.6" marker-end="url(#ah)"/>'

DEFS = f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{MUT}"/></marker></defs>'

def _cells(x, y):
    return "".join(f'<rect x="{x+i*14}" y="{y}" width="10" height="16" rx="2" fill="{ALU}" stroke="#AEB8C2"/>' for i in range(6))

# ---------------- Systemdiagramm (Desktop, horizontal) ----------------
def arch_desktop(L):
    o = [f'<svg class="d" viewBox="0 0 1120 430" role="img" aria-label="{L["aria"]}">', DEFS]
    # Band oben: Systems Engineering
    o.append(_box(20, 14, 1080, 40, fill="#FBF3EC", stroke=COP, sw=1.4))
    o.append(_t(560, 39, L["top"], 14, 600, COP, "middle"))
    # Zellmodule
    o.append(_t(20, 92, L["cells"], 14, 700))
    for i, lab in enumerate(["CMU 1", "CMU 2", "CMU n"]):
        y = 104 + i * 74
        o.append(_box(20, y, 200, 62))
        o.append(_t(32, y + 22, f'{lab} · AFE', 13, 600))
        o.append(_cells(32, y + 32))
    o.append(_t(20, 336, L["cells_sub"], 12, 400, MUT))
    # Pfeil Zellen -> BMU
    o.append(_arrow(222, 210, 286, 210))
    o.append(_t(254, 200, "Daisy Chain", 11, 400, MUT, "middle"))
    # BMU
    o.append(_box(290, 76, 380, 262, fill=PALE, stroke=COB, sw=2.2, r=8))
    o.append(_t(310, 104, L["bmu"], 16, 700, COB))
    pills = L["pills"]
    for i, p in enumerate(pills):
        cx, cy = 310 + (i % 2) * 176, 122 + (i // 2) * 66
        o.append(_box(cx, cy, 164, 52, fill="#fff", stroke=COB, sw=1))
        lines = p.split("|")
        for j, ln in enumerate(lines):
            o.append(_t(cx + 82, cy + (30 if len(lines) == 1 else 22 + j * 16), ln, 13, 600 if j == 0 else 400, INK, "middle"))
    # Pfeil BMU -> HV-Pfad
    o.append(_arrow(672, 210, 726, 210))
    # HV-Pfad
    o.append(_t(730, 92, L["hv"], 14, 700))
    for i, lab in enumerate(L["hv_items"]):
        y = 104 + i * 74
        o.append(_box(730, y, 170, 62))
        o.append(_t(815, y + 37, lab, 13, 600, INK, "middle"))
    # Pfeil -> Fahrzeug
    o.append(_arrow(902, 210, 946, 210))
    # Fahrzeug / Maschine
    o.append(_box(950, 104, 150, 210))
    for j, ln in enumerate(L["veh"]):
        o.append(_t(1025, 136 + j * 18, ln, 13 if j > 1 else 14, 700 if j < 2 else 400, INK if j < 2 else MUT, "middle"))
    # Band unten: funktionale Sicherheit
    o.append(_box(20, 360, 1080, 52, fill=PALE, stroke=COB, sw=1.4))
    o.append(_t(560, 383, L["bot1"], 14, 700, COB, "middle"))
    o.append(_t(560, 401, L["bot2"], 12, 400, MUT, "middle"))
    o.append("</svg>")
    return "".join(o)

# ---------------- Systemdiagramm (Mobil, vertikal) ----------------
def arch_mobile(L):
    o = [f'<svg class="m" viewBox="0 0 360 760" role="img" aria-label="{L["aria"]}">', DEFS]
    o.append(_box(8, 8, 344, 48, fill="#FBF3EC", stroke=COP, sw=1.4))
    for j, ln in enumerate(L["top_m"]):
        o.append(_t(180, 28 + j * 16, ln, 12, 600, COP, "middle"))
    o.append(_t(8, 84, L["cells"], 13, 700))
    for i, lab in enumerate(["CMU 1", "CMU 2", "CMU n"]):
        x = 8 + i * 118
        o.append(_box(x, 94, 108, 46))
        o.append(_t(x + 54, 113, lab, 12, 600, INK, "middle"))
        o.append(_t(x + 54, 130, "AFE", 11, 400, MUT, "middle"))
    o.append(_arrow(180, 144, 180, 172))
    o.append(_box(8, 176, 344, 252, fill=PALE, stroke=COB, sw=2.2, r=8))
    o.append(_t(24, 202, L["bmu"], 14, 700, COB))
    for i, p in enumerate(L["pills"]):
        cx, cy = 24 + (i % 2) * 160, 216 + (i // 2) * 68
        o.append(_box(cx, cy, 152, 56, fill="#fff", stroke=COB, sw=1))
        lines = p.split("|")
        for j, ln in enumerate(lines):
            o.append(_t(cx + 76, cy + (33 if len(lines) == 1 else 25 + j * 15), ln, 12, 600 if j == 0 else 400, INK, "middle"))
    o.append(_arrow(180, 432, 180, 460))
    o.append(_t(8, 482, L["hv"], 13, 700))
    for i, lab in enumerate(L["hv_items_m"]):
        x = 8 + i * 118
        o.append(_box(x, 492, 108, 50))
        for j, ln in enumerate(lab.split("|")):
            o.append(_t(x + 54, 513 + j * 15, ln, 12, 600, INK, "middle"))
    o.append(_arrow(180, 546, 180, 574))
    o.append(_box(8, 578, 344, 70))
    o.append(_t(180, 602, L["veh_m"][0], 13, 700, INK, "middle"))
    o.append(_t(180, 622, L["veh_m"][1], 12, 400, MUT, "middle"))
    o.append(_t(180, 638, L["veh_m"][2], 12, 400, MUT, "middle"))
    o.append(_box(8, 664, 344, 86, fill=PALE, stroke=COB, sw=1.4))
    for j, ln in enumerate(L["bot_m"]):
        o.append(_t(180, 688 + j * 18, ln, 13 if j == 0 else 12, 700 if j == 0 else 400, COB if j == 0 else MUT, "middle"))
    o.append("</svg>")
    return "".join(o)

ARCH_L = {
 "de": dict(
   aria="Schema eines Hochvolt-Batteriesystems: Zellüberwachung, BMU mit BMS-Software, Hochvoltpfad und Fahrzeugschnittstelle, eingerahmt von Systems Engineering und funktionaler Sicherheit",
   top="Systems Engineering: Systemanforderungen, Systemkonzept, Architektur, Lastenheft",
   top_m=["Systems Engineering", "Anforderungen, Konzept, Architektur"],
   cells="Zellüberwachung", cells_sub="Zellspannung, Temperatur, Balancing",
   bmu="BMU · BMS-Software",
   pills=["SOC, SOH, SOP|Zustandsschätzung", "Betriebsmodi", "Schützsteuerung|und Precharge", "Isolations-|überwachung", "Diagnose|UDS, Fehlerspeicher", "Sicherheits-|mechanismen"],
   hv="Hochvoltpfad", hv_items=["Schütze, Precharge", "Pyrofuse", "Strommessung"], hv_items_m=["Schütze,|Precharge", "Pyrofuse", "Strom-|messung"],
   veh=["Fahrzeug /", "Maschine", "", "CAN, CAN FD", "J1939", "", "Laden", "ISO 15118"],
   veh_m=["Fahrzeug / Maschine", "CAN, CAN FD, J1939", "Laden nach ISO 15118"],
   bot1="Funktionale Sicherheit über das ganze System: ISO 26262, ISO 25119, ISO 13849",
   bot2="HARA, Sicherheitskonzept, FMEDA, Fehlertoleranzzeit und sicherer Zustand",
   bot_m=["Funktionale Sicherheit", "ISO 26262, ISO 25119, ISO 13849", "HARA, Sicherheitskonzept, FMEDA,", "FTTI und sicherer Zustand"],
   cap="Wo wir im Hochvolt-Batteriesystem ansetzen. Blau: BMS-Software und funktionale Sicherheit, unser Kern. Kupfer: Systems Engineering über alle Komponenten."),
 "en": dict(
   aria="Schematic of a high-voltage battery system: cell monitoring, BMU with BMS software, high-voltage path and vehicle interface, framed by systems engineering and functional safety",
   top="Systems engineering: system requirements, system concept, architecture, specification",
   top_m=["Systems engineering", "requirements, concept, architecture"],
   cells="Cell monitoring", cells_sub="Cell voltage, temperature, balancing",
   bmu="BMU · BMS software",
   pills=["SOC, SOH, SOP|state estimation", "Mode management", "Contactor control|and precharge", "Insulation|monitoring", "Diagnostics|UDS, fault memory", "Safety|mechanisms"],
   hv="High-voltage path", hv_items=["Contactors, precharge", "Pyrofuse", "Current sensing"], hv_items_m=["Contactors,|precharge", "Pyrofuse", "Current|sensing"],
   veh=["Vehicle /", "machine", "", "CAN, CAN FD", "J1939", "", "Charging", "ISO 15118"],
   veh_m=["Vehicle / machine", "CAN, CAN FD, J1939", "Charging to ISO 15118"],
   bot1="Functional safety across the whole system: ISO 26262, ISO 25119, ISO 13849",
   bot2="HARA, safety concept, FMEDA, fault tolerant time interval and safe state",
   bot_m=["Functional safety", "ISO 26262, ISO 25119, ISO 13849", "HARA, safety concept, FMEDA,", "FTTI and safe state"],
   cap="Where we work in a high-voltage battery system. Blue: BMS software and functional safety, our core. Copper: systems engineering across all components."),
}
def arch(lang):
    L = ARCH_L[lang]
    return f'<figure class="arch">{arch_desktop(L)}{arch_mobile(L)}<figcaption>{L["cap"]}</figcaption></figure>'
ARCH_DE, ARCH_EN = arch("de"), arch("en")

# ---------------- Fachskizzen zu den Herausforderungen ----------------
def _fig(inner, aria, note):
    return (f'<figure class="fig"><svg viewBox="0 0 280 100" role="img" aria-label="{aria}">{DEFS}{inner}'
            f'</svg><figcaption>{note}</figcaption></figure>')

def fig_lfp(lang):
    de = lang == "de"
    ax = f'<line x1="24" y1="84" x2="268" y2="84" stroke="{LIN}"/><line x1="24" y1="84" x2="24" y2="8" stroke="{LIN}"/>'
    c1 = f'<path d="M26,80 C32,52 40,46 62,44 L226,38 C246,36 256,26 266,10" fill="none" stroke="{COB}" stroke-width="2.2"/>'
    c2 = f'<path d="M26,82 C32,58 40,52 62,50 L226,44 C246,42 256,32 266,16" fill="none" stroke="{COB}" stroke-width="1.6" stroke-dasharray="4 3"/>'
    lab = (_t(30, 16, "OCV", 10, 600, MUT) + _t(266, 97, "SOC", 10, 600, MUT, "end")
           + _t(144, 34, "flaches Plateau" if de else "flat plateau", 11, 600, INK, "middle")
           + _t(144, 64, "Hysterese (gestrichelt)" if de else "hysteresis (dashed)", 10, 400, MUT, "middle"))
    return _fig(ax + c1 + c2 + lab, "Schematische OCV-Kennlinie einer LFP-Zelle mit flachem Plateau und Hysterese" if de else "Schematic OCV curve of an LFP cell with flat plateau and hysteresis", "schematisch" if de else "schematic")

def fig_modes(lang):
    de = lang == "de"
    n = ["Aus", "Precharge", "Ein"] if de else ["Off", "Precharge", "On"]
    o = []
    for i, s in enumerate(n):
        x = 8 + i * 94
        o.append(_box(x, 8, 76, 26, fill="#fff", stroke=COB, sw=1.2, r=13))
        o.append(_t(x + 38, 25, s, 11, 600, INK, "middle"))
        if i < 2: o.append(_arrow(x + 78, 21, x + 92, 21, COB))
        o.append(f'<line x1="{x+38}" y1="36" x2="{140 + (i-1)*30}" y2="58" stroke="{COP}" stroke-width="1.4" stroke-dasharray="3 3" marker-end="url(#ah)"/>')
    o.append(_box(60, 60, 160, 26, fill="#FBF3EC", stroke=COP, sw=1.4, r=13))
    o.append(_t(140, 77, "Sicherer Zustand" if de else "Safe state", 11, 700, COP, "middle"))
    return _fig("".join(o), "Betriebsmodi mit Fehlerpfaden in den sicheren Zustand" if de else "Operating modes with fault paths to the safe state", "schematisch" if de else "schematic")

def fig_metrics(lang):
    de = lang == "de"
    o = []
    for i, (name, thr) in enumerate([("SPFM", 99), ("LFM", 90)]):
        y = 14 + i * 36
        o.append(_t(8, y + 12, name, 11, 700, INK))
        o.append(_box(52, y, 200, 16, fill=ALU, stroke=LIN, sw=1, r=3))
        x = 52 + 200 * thr / 100
        o.append(f'<rect x="{x}" y="{y}" width="{252 - x}" height="16" rx="0" fill="{PALE}" stroke="none"/>')
        o.append(f'<line x1="{x}" y1="{y-3}" x2="{x}" y2="{y+19}" stroke="{COB}" stroke-width="2.2"/>')
        o.append(_t(x - 4, y + 12, f"≥ {thr} %", 11, 700, COB, "end"))
    o.append(_t(52, 92, "ASIL D, ISO 26262-5" if de else "ASIL D, ISO 26262-5", 10, 400, MUT))
    return _fig("".join(o), "Mindestwerte der Hardware-Architekturmetriken für ASIL D" if de else "Minimum hardware architectural metrics for ASIL D", "Zielwerte" if de else "targets")

def fig_load(lang):
    de = lang == "de"
    ax = f'<line x1="24" y1="84" x2="268" y2="84" stroke="{LIN}"/><line x1="24" y1="84" x2="24" y2="8" stroke="{LIN}"/>'
    car = f'<polyline points="26,80 40,80 46,54 52,78 70,76 76,60 82,79 104,77 110,52 116,79 140,78 146,64 152,80 176,78 182,56 188,79 210,77 216,62 222,80 266,79" fill="none" stroke="#9AA6B4" stroke-width="1.4"/>'
    trac = f'<polyline points="26,78 34,30 230,28 236,30 240,80 266,80" fill="none" stroke="{COB}" stroke-width="2.4"/>'
    lab = (_t(30, 16, "P", 10, 600, MUT) + _t(266, 97, "t", 10, 600, MUT, "end")
           + _t(130, 22, "Traktor: Dauerlast" if de else "Tractor: continuous load", 11, 700, COB, "middle")
           + _t(130, 46, "Pkw: Lastspitzen" if de else "Car: load peaks", 10, 600, "#7B8794", "middle"))
    return _fig(ax + car + trac + lab, "Schematischer Leistungsverlauf Pkw gegenüber Traktor" if de else "Schematic power profile car versus tractor", "schematisch" if de else "schematic")

FIGS = {
 "Ladezustand bei LFP-Zellen": fig_lfp("de"), "State of charge with LFP cells": fig_lfp("en"),
 "Schütze, Precharge und Fehlerreaktion": fig_modes("de"), "Contactors, precharge and fault reaction": fig_modes("en"),
 "Sicherheitsnachweis nach ISO 26262": fig_metrics("de"), "ISO 26262 safety evidence": fig_metrics("en"),
 "Elektrifizierung von Land- und Baumaschinen": fig_load("de"), "Electrifying agricultural and construction machinery": fig_load("en"),
}

# ---------------- Icons für die Kompetenzen ----------------
_I = lambda body: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'
ICONS = {
 "sys": _I('<rect x="3" y="3" width="18" height="5" rx="1"/><rect x="3" y="10" width="8" height="11" rx="1"/><rect x="13" y="10" width="8" height="11" rx="1"/>'),
 "bms": _I('<rect x="2" y="7" width="17" height="11" rx="2"/><path d="M21 11v3"/><path d="M11 9l-3 4h4l-2 3"/>'),
 "emb": _I('<rect x="6" y="6" width="12" height="12" rx="1.5"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>'),
 "saf": _I('<path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>'),
 "com": _I('<circle cx="5" cy="12" r="2.2"/><circle cx="19" cy="5" r="2.2"/><circle cx="19" cy="19" r="2.2"/><path d="M7 11l10-5M7 13l10 5"/>'),
 "ver": _I('<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="M8.5 12l2.5 2.5 4.5-5"/>'),
}
ICON_LABELS = {
 "Systems Engineering": "sys", "Systems engineering": "sys",
 "BMS-Funktionen": "bms", "BMS functions": "bms",
 "Embedded Software": "emb", "Embedded software": "emb",
 "Funktionale Sicherheit": "saf", "Functional safety": "saf",
 "Diagnose und Kommunikation": "com", "Diagnostics and communication": "com",
 "Verifikation": "ver", "Verification": "ver",
}
def with_icons(html):
    for lab, key in ICON_LABELS.items():
        html = html.replace(f'<div class="skill"><h3>{lab}</h3>', f'<div class="skill"><h3>{ICONS[key]}{lab}</h3>')
    return html
