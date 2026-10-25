
# =====================================================================
# Startseiten – Freelance-Positionierung
# =====================================================================
def module_svg(aria):
    cols, rows, p, r0 = 12, 6, 30, 12.5
    on = round(cols * rows * 0.8); gap = 12
    X = lambda c: 24 + c * p + (c // 3) * gap
    W = X(cols - 1) + 24; H = 24 + rows * p
    out = [f'<line class="bus" x1="{(X(g*3-1)+X(g*3))/2}" y1="8" x2="{(X(g*3-1)+X(g*3))/2}" y2="{H-6}"/>' for g in range(1, 4)]
    i = 0
    for c in range(cols):
        for rr in range(rows):
            cls = "cell on" if i < on else "cell"
            st = f' style="animation-delay:{0.25 + i*0.022:.3f}s"' if i < on else ""
            out.append(f'<circle class="{cls}"{st} cx="{X(c)}" cy="{24 + rr*p}" r="{r0}"/>'); i += 1
    return f'<svg viewBox="0 0 {W} {H+2}" role="img" aria-label="{aria}">' + "".join(out) + "</svg>"

def faq_html(f): return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in f)
def faq_schema(f): return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in f]}
TODO = lambda s: f'<span class="todo">{s}</span>'

KW_DE = ("Freelancer Automotive, Freiberufler Automotive, BMS Software Freelancer, Batteriemanagementsystem, BMS Entwickler, Embedded Software Entwickler Automotive, "
         "AUTOSAR Freelancer, MATLAB Simulink Freelancer, Functional Safety Freelancer, ISO 26262, FuSa, Funktionale Sicherheit, Hochvolt Batterie, Elektromobilität, "
         "Embedded C, Software Integrator, Automotive SPICE, ASPICE, HIL Test, Requirements Engineering, Software-Defined Vehicle, Batteriepass, Ingenieur freiberuflich München, "
         "externe Unterstützung Automotive, Projektunterstützung Embedded, Interim Engineering")
KW_EN = ("freelance BMS engineer, battery management system software, automotive freelancer Germany, embedded software engineer automotive, AUTOSAR freelancer, "
         "MATLAB Simulink freelancer, functional safety engineer ISO 26262, FuSa consultant, high-voltage battery software, Automotive SPICE, HIL testing, contractor Munich")

HOME_FAQ_DE = [
 ("Ab wann sind Sie verfügbar?", "Unsere aktuelle Verfügbarkeit steht im Steckbrief oben auf dieser Seite. Fragen Sie auch kurzfristige Einsätze gerne direkt an, Sie bekommen innerhalb von zwei Werktagen eine Antwort."),
 ("Arbeiten Sie remote oder vor Ort?", "Beides. Wir arbeiten überwiegend remote und kommen für Workshops, Integration und Tests zu Ihnen, im Raum München, Ingolstadt, Regensburg und Stuttgart regelmäßig, europaweit nach Absprache."),
 ("Wie rechnen Sie ab?", "Im Dienstvertrag nach Stunden oder Tagen, im Werkvertrag zum Festpreis für ein definiertes Ergebnis. Unseren Stunden- oder Tagessatz nennen wir Ihnen mit dem Angebot."),
 ("Können wir Sie über einen Personaldienstleister beauftragen?", "Ja. Sie können uns direkt beauftragen oder über Ihren Personaldienstleister beziehungsweise Ihre Vermittlungsplattform."),
 ("Arbeiten Sie in Arbeitnehmerüberlassung?", "Nein. Wir arbeiten als selbstständige Ingenieure im Dienst- oder Werkvertrag mit eigener Ausstattung und klar beschriebenen Leistungen, nicht in Arbeitnehmerüberlassung."),
 ("Arbeiten Sie mit unseren Werkzeugen und Rechnern?", "Ja, wenn Ihre IT-Richtlinien das verlangen. Ansonsten arbeiten wir mit eigener Ausstattung. Projektspezifische Lizenzen, etwa für MATLAB/Simulink oder Vector-Werkzeuge, stellt in der Regel der Auftraggeber."),
 ("Übernehmen Sie bestehende Software-Module?", "Ja. Wir übernehmen bestehende Module, arbeiten uns strukturiert ein und dokumentieren so, dass Ihr Team sie später selbst weiterführen kann."),
 ("Unterschreiben Sie eine Geheimhaltungsvereinbarung?", "Selbstverständlich, vor dem ersten fachlichen Austausch."),
]
HOME_FAQ_EN = [
 ("When are you available?", "Our current availability is shown in the profile at the top of this page. Short-notice requests are welcome; you get an answer within two business days."),
 ("Do you work remotely or on site?", "Both. We mostly work remotely and come on site for workshops, integration and testing, regularly in the Munich, Ingolstadt, Regensburg and Stuttgart areas and across Europe by arrangement."),
 ("How do you charge?", "Time and materials by the hour or day, or a fixed price for a defined deliverable. We quote our rate with the offer."),
 ("Can we engage you through an agency?", "Yes. You can contract us directly or through your staffing agency or freelance platform."),
 ("Do you take over existing software modules?", "Yes. We take over existing modules, get up to speed in a structured way and document them so your team can carry them forward."),
 ("Do you sign an NDA?", "Of course, before any technical exchange."),
]

ORG = {"@type": "Organization", "@id": BASE + "/#org", "name": "dolavolt", "url": BASE + "/", "logo": BASE + "/assets/og.png", "email": "hallo@dolavolt.de",
       "description": "Expertise für BMS-Software, Embedded Software, MATLAB/Simulink, AUTOSAR und funktionale Sicherheit nach ISO 26262 im Automotive, auch als Freelancer im Dienst- oder Werkvertrag.",
       "address": {"@type": "PostalAddress", "addressLocality": "München", "addressCountry": "DE"},
       "knowsLanguage": ["de", "en", "it"],
       "knowsAbout": ["Batteriemanagementsystem", "BMS-Software", "Hochvolt-Batteriesysteme", "State of Charge", "State of Health", "Schützsteuerung", "ISO 26262", "Funktionale Sicherheit",
                      "AUTOSAR", "Embedded C", "MATLAB/Simulink", "Stateflow", "Embedded Coder", "Automotive SPICE", "HIL-Test", "UDS-Diagnose", "CAN FD", "ISO/SAE 21434", "EU-Batteriepass", "Software-Defined Vehicle"]}
SERVICE = {"@type": "ProfessionalService", "name": "dolavolt", "url": BASE + "/", "parentOrganization": {"@id": BASE + "/#org"},
           "address": {"@type": "PostalAddress", "addressLocality": "München", "addressCountry": "DE"},
           "areaServed": [{"@type": "City", "name": n} for n in ["München", "Ingolstadt", "Regensburg", "Stuttgart"]] + [{"@type": "Country", "name": n} for n in ["Deutschland", "Österreich", "Schweiz"]],
           "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Leistungen", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": f"{BASE}/leistungen/{s}.html"}} for s, n in SERVICES]}}
HREFLANG = f'<link rel="alternate" hreflang="de" href="{BASE}/">\n<link rel="alternate" hreflang="en" href="{BASE}/en/">\n<link rel="alternate" hreflang="x-default" href="{BASE}/">\n'

SVC_DE = [
 ("bms-softwareentwicklung", "Zustandsschätzung (SoC, SoH, SoP), Zellüberwachung, Balancing, Schützsteuerung, Betriebsmodi, Isolationsüberwachung und Ladesteuerung für Hochvolt-Batterien."),
 ("funktionale-sicherheit-iso-26262", "Gefährdungsanalyse (HARA), Sicherheitskonzepte, FMEA, FTA, FMEDA und Safety Case, als Functional Safety Engineer auf Zeit."),
 ("autosar-embedded-software", "AUTOSAR Classic und Adaptive, Embedded C und C++, RTE- und BSW-Konfiguration, UDS-Diagnose und Software-Integration."),
 ("matlab-simulink-modellbasierte-entwicklung", "Funktionsentwicklung in Simulink und Stateflow, Seriencode mit Embedded Coder, MIL, SIL und Back-to-Back-Tests."),
 ("test-absicherung-hil", "Anforderungsbasierte Tests, HIL-Absicherung, Testautomatisierung und Fehlerinjektion nach ASPICE und ISO 26262."),
 ("requirements-architektur-aspice", "System- und Softwareanforderungen, Softwarearchitektur, Rückverfolgbarkeit und Vorbereitung von ASPICE-Assessments."),
]
SVC_EN = [
 ("bms-softwareentwicklung", "BMS software", "State estimation (SoC, SoH, SoP), cell monitoring, balancing, contactor management, mode management, insulation monitoring and charge control for high-voltage batteries."),
 ("funktionale-sicherheit-iso-26262", "Functional safety (ISO 26262)", "HARA, safety concepts, FMEA, FTA, FMEDA and safety case, as an interim functional safety engineer."),
 ("autosar-embedded-software", "AUTOSAR and embedded software", "AUTOSAR Classic and Adaptive, embedded C and C++, RTE and BSW configuration, UDS diagnostics and software integration."),
 ("matlab-simulink-modellbasierte-entwicklung", "MATLAB/Simulink", "Function development in Simulink and Stateflow, production code with Embedded Coder, MIL, SIL and back-to-back testing."),
 ("test-absicherung-hil", "Testing and HIL", "Requirements-based testing, HIL validation, test automation and fault injection to ASPICE and ISO 26262."),
 ("requirements-architektur-aspice", "Requirements and ASPICE", "System and software requirements, software architecture, traceability and ASPICE assessment readiness."),
]

TOPIC = {"bms-softwareentwicklung":"Batterie","funktionale-sicherheit-iso-26262":"Safety","autosar-embedded-software":"Software","matlab-simulink-modellbasierte-entwicklung":"Modelle","test-absicherung-hil":"Test","requirements-architektur-aspice":"Prozess"}

SKILLS_DE = [
 ("Normen und Prozesse", "ISO 26262, IEC 61508, ISO/SAE 21434, Automotive SPICE, AUTOSAR, MISRA C, UN-R155, UN-R156, ISO 15118, EU-Batterieverordnung"),
 ("Programmiersprachen", "C, C++, Python, MATLAB"),
 ("Modellbasierte Entwicklung", "MATLAB/Simulink, Stateflow, Embedded Coder, Simulink Test, Simulink Check, Polyspace"),
 ("AUTOSAR und Embedded", "AUTOSAR Classic, AUTOSAR Adaptive, Vector DaVinci, MICROSAR, EB tresos, Lauterbach TRACE32, Infineon AURIX, NXP S32K"),
 ("Test und Diagnose", "Vector CANoe, CANalyzer, vTESTstudio, dSPACE HIL, ECU-TEST, UDS, XCP, CANape, INCA"),
 ("Anforderungen und ALM", "Polarion, IBM DOORS, codebeamer, Jira, Confluence, Git, Jenkins"),
 ("Batterietechnik", "Lithium-Ionen (NMC, LFP), Hochvolt-Systeme mit 400 V und 800 V, Zellalterung, Thermomanagement, Lade- und Entladestrategien"),
]
SKILLS_EN = [
 ("Standards and processes", "ISO 26262, IEC 61508, ISO/SAE 21434, Automotive SPICE, AUTOSAR, MISRA C, UN R155, UN R156, ISO 15118, EU Battery Regulation"),
 ("Languages", "C, C++, Python, MATLAB"),
 ("Model-based design", "MATLAB/Simulink, Stateflow, Embedded Coder, Simulink Test, Simulink Check, Polyspace"),
 ("AUTOSAR and embedded", "AUTOSAR Classic, AUTOSAR Adaptive, Vector DaVinci, MICROSAR, EB tresos, Lauterbach TRACE32, Infineon AURIX, NXP S32K"),
 ("Testing and diagnostics", "Vector CANoe, CANalyzer, vTESTstudio, dSPACE HIL, ECU-TEST, UDS, XCP, CANape, INCA"),
 ("Requirements and ALM", "Polarion, IBM DOORS, codebeamer, Jira, Confluence, Git, Jenkins"),
 ("Battery technology", "Lithium-ion (NMC, LFP), 400 V and 800 V high-voltage systems, cell ageing, thermal management, charge and discharge strategies"),
]
skills_html = lambda S: "".join(f'<div class="skill"><h3>{g}</h3><p>{v}</p></div>' for g, v in S)

