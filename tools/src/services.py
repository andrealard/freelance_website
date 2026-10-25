
# =====================================================================
# Leistungs-Landingpages (je ein Keyword-Cluster)
# =====================================================================
def service_page(slug, title, desc, keywords, h1, intro, tasks, results, tools, faq, extra="", audience=None):
    url = f"{BASE}/leistungen/{slug}.html"
    name = dict(SERVICES)[slug]
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "name": h1, "serviceType": name, "description": desc, "url": url,
         "provider": {"@type": "Organization", "name": "dolavolt", "url": BASE + "/"},
         "areaServed": ["DE", "AT", "CH", "EU"], "audience": {"@type": "BusinessAudience", "audienceType": "Automobilhersteller, Zulieferer, Batteriehersteller, Engineering-Dienstleister"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Start", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Leistungen", "item": BASE + "/leistungen/"},
            {"@type": "ListItem", "position": 3, "name": name, "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    others = "".join(f'<li><a href="{s}.html">{n}</a></li>' for s, n in SERVICES if s != slug)
    faq_h = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    body = f'''<article class="article">
<nav class="crumbs" aria-label="Brotkrumen"><a href="{{r}}">Start</a> / <a href="{{r}}leistungen/">Leistungen</a></nav>
<h1>{h1}</h1>
<p class="lead">{intro}</p>
<h2>Was wir übernehmen</h2>
<ul>{li(tasks)}</ul>
{extra}
<h2>Was Sie am Ende in der Hand haben</h2>
<ul>{li(results)}</ul>
<h2>Werkzeuge und Standards</h2>
<p>{tools}</p>
<h2>Häufige Fragen</h2>
{faq_h}
<h2>Weitere Leistungen</h2>
<ul class="related">{others}</ul>
<div class="article-cta"><h2>Passt das zu Ihrem Projekt?</h2><p>Schicken Sie uns Aufgabe, Zeitraum und Einsatzort. Sie bekommen innerhalb von zwei Werktagen eine Rückmeldung.</p><a class="btn" href="{{r}}#kontakt">Projekt anfragen</a></div>
</article>'''
    page(f"leistungen/{slug}.html", title, desc, body, schema, ogtype="article",
         extra_head=f'<meta name="keywords" content="{keywords}">\n')

TOOLS_FLAG = ""

service_page(
 "bms-softwareentwicklung",
 "BMS-Softwareentwicklung: Batteriemanagement-Software für Hochvolt-Batterien | dolavolt",
 "BMS-Softwareentwicklung für Hochvolt-Batteriesysteme: SoC-, SoH- und SoP-Schätzung, Zellüberwachung, Balancing, Schützsteuerung, Isolationsüberwachung und Ladesteuerung. Remote oder vor Ort in München.",
 "BMS Experten, Batteriemanagementsystem Entwicklung, AFE, BMU, CMU, Pyrofuse, Crashabschaltung, Lastenheft BMS, Euro 7 SOH, Thermal Runaway Erkennung, Hochvolt Batterie Software, SoC Schätzung, SoH Schätzung, State of Health, State of Charge, State of Power, Kalman-Filter Batterie, Zellüberwachung, Balancing, Schützsteuerung, Contactor Management, Precharge, Isolationsüberwachung, HVIL, Ladesteuerung, 800 V, BMS Embedded Software, BMS Simulink, Batteriepass BMS",
 "BMS-Softwareentwicklung für Hochvolt-Batteriesysteme",
 "Wir entwickeln BMS-Software für Hochvolt-Batterien, als Verstärkung Ihres Teams oder als abgegrenztes Arbeitspaket, mit der Erfahrung aus der Pkw-Serienentwicklung.",
 ["Systemanforderungen, Lasten- und Pflichtenhefte und Systemkonzepte für das BMS",
  "Zustandsschätzung: Ladezustand (SoC), Gesundheitszustand (SoH) und Leistungsprognose (SoP), zum Beispiel mit Kalman-Filtern und Ersatzschaltbildmodellen",
  "Zellspannungs-, Strom- und Temperaturüberwachung über AFE-Bausteine in BMU/CMU-Architekturen, mit Plausibilisierung und Sensordiagnose",
  "Crashabschaltung und Ansteuerung von Pyrofuses",
  "Balancing-Strategien für passives und aktives Balancing",
  "Schützsteuerung (Contactor Management), Vorladung (Precharge) und Erkennung verschweißter Schütze",
  "Betriebsmodi und Zustandsautomaten (Mode Management) für Fahren, Laden, Parken und Fehlerfälle",
  "Isolationsüberwachung und HV-Interlock (HVIL)",
  "Ladesteuerung für AC- und DC-Laden, 400-Volt- und 800-Volt-Systeme, Ladekommunikation nach ISO 15118 und DIN 70121",
  "Derating, Degradationskonzepte, Diagnose und Fehlerspeicher",
  "Erkennung thermischer Ereignisse und definierte Reaktion in allen Betriebszuständen",
  "SOH- und SOCE-Bereitstellung für Euro 7 und den EU-Batteriepass"],
 ["Software-Anforderungen und Architektur der BMS-Funktion",
  "Simulink-Modelle oder C-Code mit Unit- und Integrationstests",
  "integrierte, getestete Softwarekomponente im Steuergerät",
  "Dokumentation und Arbeitsprodukte für Automotive SPICE und ISO 26262"],
 "MATLAB/Simulink, Stateflow, Embedded Coder, AUTOSAR Classic, C, MISRA C, Vector CANoe, XCP, ISO 15118, DIN 70121, Polarion oder DOORS, ISO 26262, Automotive SPICE, ECE-R100, Euro 7, GB 38031, EU-Batterieverordnung.",
 [("Für welche Zellchemien entwickeln Sie BMS-Software?", "Für Lithium-Ionen-Chemien wie NMC und LFP. LFP stellt wegen der flachen Spannungskennlinie besondere Anforderungen an die Ladezustandsschätzung."),
  ("Arbeiten Sie modellbasiert oder in C?", "Beides. Wir richten uns nach Ihrer Toolchain: Funktionsentwicklung in MATLAB/Simulink mit Codegenerierung oder Implementierung in C innerhalb einer AUTOSAR-Architektur."),
  ("Übernehmen Sie auch bestehende BMS-Software?", "Ja. Wir übernehmen bestehende Module, etwa Schützsteuerung oder Betriebsmodi, arbeiten uns strukturiert ein und dokumentieren so, dass Ihr Team sie später selbst weiterführen kann.")])

service_page(
 "funktionale-sicherheit-iso-26262",
 "Funktionale Sicherheit nach ISO 26262: Safety Engineering für Hochvolt-Batteriesysteme | dolavolt",
 "Funktionale Sicherheit nach ISO 26262: HARA, Sicherheitskonzepte, FMEA, FTA, FMEDA, DFA und Safety Case für Hochvolt-Batteriesysteme und Steuergeräte.",
 "Functional Safety Experte, Funktionale Sicherheit ISO 26262, Verifikation Sicherheitsziele, Zertifizierung sicherheitskritischer Systeme, ECE-R100, IEC 62619, Safety Engineer Automotive, HARA, ASIL, Sicherheitskonzept, Functional Safety Concept, Technical Safety Concept, FMEA, FTA, FMEDA, DFA, Safety Case, Freedom from Interference, Werkzeugqualifizierung, IEC 61508, ISO/SAE 21434",
 "Funktionale Sicherheit nach ISO 26262 für Hochvolt-Batteriesysteme",
 "Überladung, Kurzschluss oder Übertemperatur können zu thermischem Durchgehen führen. Für Hochvolt-Batteriesysteme ergeben sich Sicherheitsziele deshalb typischerweise bis ASIL C oder D. Wir übernehmen Safety-Arbeitspakete von der Gefährdungsanalyse bis zum Safety Case.",
 ["Gefährdungs- und Risikoanalyse (HARA) und Sicherheitsziele mit ASIL-Einstufung",
  "Funktionales Sicherheitskonzept (FSC)",
  "Technisches Sicherheitskonzept (TSC) und Sicherheitsanforderungen an Hardware und Software",
  "Sicherheitsanalysen: FMEA, Fehlerbaumanalyse (FTA), FMEDA und Analyse abhängiger Ausfälle (DFA)",
  "Software-Sicherheitsanalysen und Nachweis der Rückwirkungsfreiheit (Freedom from Interference)",
  "Safety Plan, Safety Case und Vorbereitung der Bestätigungsmaßnahmen",
  "Bewertung von Software-Werkzeugen nach ISO 26262-8",
  "Verifikation der Sicherheitsanforderungen, Unterstützung der Sicherheitsvalidierung sowie von Audits und Assessments",
  "Abstimmung mit Cybersecurity nach ISO/SAE 21434"],
 ["review-fähige Sicherheitskonzepte und Sicherheitsanalysen",
  "durchgängige Rückverfolgbarkeit vom Sicherheitsziel über die Anforderung bis zum Test",
  "Arbeitsprodukte nach ISO 26262 Teil 3 bis 6, vorbereitet für das Functional Safety Assessment"],
 "ISO 26262, IEC 61508, ISO 13849, IEC 62619, ECE-R100, ISO/SAE 21434, Automotive SPICE, Polarion, DOORS, codebeamer, Werkzeuge für FMEA und FTA nach Projektvorgabe.",
 [("Übernehmen Sie die Rolle des Safety Managers?", "Wir übernehmen die operative Safety-Arbeit und unterstützen Ihren Safety Manager. Ob wir die Rolle selbst übernehmen, stimmen wir je nach Projektumfang ab."),
  ("Führen Sie auch das Functional Safety Assessment durch?", "Nein. Bestätigungsmaßnahmen wie das Functional Safety Assessment verlangen Unabhängigkeit vom Entwicklungsteam. Wir bereiten sie vor, durchführen sollte sie eine unabhängige Stelle."),
  ("Arbeiten Sie auch nach IEC 61508?", "Ja. Für Batteriesysteme außerhalb des Pkw, etwa in stationären Speichern oder Maschinen, ist IEC 61508 oft die Grundlage.")])

service_page(
 "autosar-embedded-software",
 "AUTOSAR und Embedded-Software-Entwicklung für Automotive-Steuergeräte | dolavolt",
 "Embedded-Software-Entwicklung für Automotive-Steuergeräte: AUTOSAR Classic und Adaptive, Embedded C und C++, RTE- und BSW-Konfiguration, UDS-Diagnose, CAN FD und Automotive Ethernet.",
 "Embedded Software Entwickler Automotive, AUTOSAR Classic, AUTOSAR Adaptive, Software Integrator, RTE Konfiguration, BSW Konfiguration, Vector DaVinci, MICROSAR, EB tresos, UDS Diagnose, DEM, DCM, CAN FD, LIN, Automotive Ethernet, MISRA C, Steuergerätesoftware, Software-Defined Vehicle",
 "AUTOSAR und Embedded Software für Automotive-Steuergeräte",
 "Wir entwickeln und integrieren Embedded Software für Automotive-Steuergeräte nach AUTOSAR, in C und C++. Als erfahrene Embedded-Entwickler und Software-Integratoren steigen wir ohne lange Anlaufzeit in Ihre bestehende Architektur und Toolchain ein.",
 ["Entwicklung von AUTOSAR-Softwarekomponenten (SWC)",
  "RTE- und BSW-Konfiguration, etwa Com, Dcm, Dem, NvM und WdgM",
  "Integration von generiertem Modellcode und Handcode",
  "Diagnose nach UDS (ISO 14229), Fehlerspeicher und DTC-Handling",
  "Kommunikation über CAN, CAN FD, LIN und Automotive Ethernet",
  "MISRA-C-konforme Implementierung, statische Codeanalyse, Laufzeit- und Speicheroptimierung",
  "AUTOSAR Adaptive und service-orientierte Architekturen für das Software-Defined Vehicle",
  "Bootloader, Flash-Prozesse und Software-Updates"],
 ["lauffähige, integrierte Steuergerätesoftware",
  "konfigurierte Basissoftware mit dokumentierten Entscheidungen",
  "Unit-Tests, Integrationstests und Analyseberichte"],
 "AUTOSAR Classic und Adaptive, C, C++, Vector DaVinci Developer und Configurator, MICROSAR, EB tresos, Lauterbach TRACE32, Polyspace, Git, Jenkins, MISRA C.",
 [("AUTOSAR Classic oder Adaptive?", "Beides. Der Schwerpunkt liegt auf AUTOSAR Classic für sicherheitskritische Steuergeräte wie das BMS. AUTOSAR Adaptive kommt bei Zentralrechnern im Software-Defined Vehicle ins Spiel."),
  ("Arbeiten Sie mit unserer Toolchain?", "Ja. Wir arbeiten in Ihren Werkzeugen, Repositories und Prozessen. Projektspezifische Lizenzen stellt in der Regel der Auftraggeber."),
  ("Übernehmen Sie auch Software-Integration?", "Ja. Integration von Komponenten verschiedener Lieferanten, Konfiguration der Basissoftware und Integrationstests gehören zu unseren typischen Aufgaben.")])

service_page(
 "matlab-simulink-modellbasierte-entwicklung",
 "MATLAB/Simulink: Modellbasierte Entwicklung für Automotive | dolavolt",
 "Modellbasierte Entwicklung mit MATLAB/Simulink und Stateflow: Funktionsentwicklung, Seriencodegenerierung mit Embedded Coder, MIL, SIL und Back-to-Back-Tests nach ISO 26262.",
 "modellbasierte Entwicklung Automotive, Model-Based Design, Stateflow, Embedded Coder, Seriencodegenerierung, MIL, SIL, Back-to-Back-Test, Simulink Test, Modellierrichtlinien, MAB Guidelines, Polyspace, Batteriemodell, Simulink BMS",
 "MATLAB/Simulink und modellbasierte Entwicklung",
 "Viele BMS- und Steuergerätefunktionen entstehen heute modellbasiert. Wir entwickeln Simulink- und Stateflow-Modelle, die sich sauber in Seriencode übersetzen, testen und nach ISO 26262 absichern lassen.",
 ["Funktionsentwicklung in Simulink und Stateflow",
  "Seriencodegenerierung mit Embedded Coder",
  "Modellierrichtlinien (MAB) und automatische Modellprüfung",
  "Model-in-the-Loop (MIL), Software-in-the-Loop (SIL) und Back-to-Back-Tests",
  "anforderungsbasierte Tests mit Simulink Test, Modell- und Codeabdeckung",
  "Analyse von Laufzeitfehlern mit Polyspace",
  "Zell- und Batteriemodelle für Simulation und Algorithmenentwicklung"],
 ["review-fähige, richtlinienkonforme Modelle",
  "generierter Seriencode mit Back-to-Back-Nachweis",
  "Testberichte mit Abdeckungsmetriken für ISO 26262"],
 "MATLAB, Simulink, Stateflow, Embedded Coder, Simulink Test, Simulink Check, Polyspace, MAB-Richtlinien, ISO 26262.",
 [("Arbeiten Sie auch mit TargetLink?", "Unser Schwerpunkt ist Embedded Coder. TargetLink-Projekte prüfen wir im Einzelfall."),
  ("Können Sie bestehende Modelle übernehmen und aufräumen?", "Ja. Wir prüfen Modelle gegen Richtlinien, beheben Befunde und dokumentieren die Struktur, damit Ihr Team effizient weiterarbeiten kann."),
  ("Entwickeln Sie auch Batteriemodelle für die Simulation?", "Ja, etwa Ersatzschaltbildmodelle für Zellen, die als Grundlage für Zustandsschätzung und Tests dienen.")])

service_page(
 "test-absicherung-hil",
 "Software-Test und HIL-Absicherung für BMS und Steuergeräte | dolavolt",
 "Absicherung von Steuergerätesoftware: anforderungsbasierte Tests, Unit- und Integrationstests, HIL-Tests, Testautomatisierung und Fehlerinjektion nach Automotive SPICE und ISO 26262.",
 "Hardware-in-the-Loop, dSPACE, Vector CANoe, vTESTstudio, ECU-TEST, Testautomatisierung Python, Fehlerinjektion, Integrationstest, SWE.4, SWE.5, SWE.6, BMS Test, Steuergerätetest, Restbussimulation",
 "Software-Test und HIL-Absicherung für BMS und Steuergeräte",
 "Ein BMS ist nur so gut wie seine Absicherung. Wir testen anforderungsbasiert, von Modul- und Integrationstests bis zum Hardware-in-the-Loop, und liefern die Verifikationsnachweise für ISO 26262 sowie die Arbeitsprodukte für Automotive-SPICE-Assessments.",
 ["Testspezifikation aus System- und Softwareanforderungen",
  "Unit-Tests und Software-Integrationstests (SWE.4, SWE.5)",
  "Softwarequalifizierungstests (SWE.6)",
  "Hardware-in-the-Loop-Tests (HIL)",
  "Testautomatisierung mit CANoe, vTESTstudio, ECU-TEST oder Python",
  "Fehlerinjektion und Tests der Sicherheitsmechanismen",
  "Restbussimulation und Diagnose-Tests",
  "Testberichte mit Rückverfolgbarkeit zu den Anforderungen"],
 ["automatisierte, wiederholbare Testfälle",
  "Testberichte mit Abdeckung der Anforderungen",
  "nachvollziehbare Nachweise für Assessments und Audits"],
 "Vector CANoe und vTESTstudio, dSPACE HIL, ECU-TEST, Python, Polarion oder DOORS, Automotive SPICE, ISO 26262.",
 [("Testen Sie auch Sicherheitsmechanismen?", "Ja. Mit Fehlerinjektion prüfen wir, ob Schutzfunktionen wie Abschaltung bei Überspannung oder Übertemperatur auch bei Sensor- oder Kommunikationsfehlern greifen."),
  ("Bringen Sie eigene HIL-Hardware mit?", "Nein. Wir arbeiten auf Ihren Prüfständen oder entwickeln Tests remote, die dann auf Ihrer Infrastruktur laufen."),
  ("Automatisieren Sie bestehende manuelle Tests?", "Ja. Die Automatisierung bestehender Testfälle ist oft der schnellste Weg zu kürzeren Releasezyklen.")])

service_page(
 "requirements-architektur-aspice",
 "Requirements Engineering, Softwarearchitektur und Automotive SPICE | dolavolt",
 "Requirements Engineering, Softwarearchitektur und Automotive SPICE: System- und Softwareanforderungen, Architektur, Rückverfolgbarkeit und Vorbereitung von ASPICE-Assessments.",
 "Requirements Engineering Automotive, Softwarearchitektur Automotive, Automotive SPICE, ASPICE Assessment, ASPICE Level 2, SYS.2, SWE.1, SWE.2, Rückverfolgbarkeit, Traceability, Polarion, DOORS, codebeamer, Systems Engineering",
 "Requirements Engineering, Softwarearchitektur und Automotive SPICE",
 "Saubere Anforderungen und eine klare Architektur entscheiden, ob ein Projekt im Assessment besteht und ob die Software über Jahre wartbar bleibt. Wir bringen Struktur in Anforderungen, Architektur und Nachweise.",
 ["System- und Softwareanforderungen (SYS.2, SWE.1)",
  "Softwarearchitektur, Schnittstellen und Ressourcenbetrachtung (SWE.2)",
  "Feindesign von Softwarekomponenten (SWE.3)",
  "Rückverfolgbarkeit in Polarion, DOORS oder codebeamer",
  "Vorbereitung von Automotive-SPICE-Assessments",
  "Review- und Änderungsprozesse",
  "Übergabe und Dokumentation bestehender Softwaremodule"],
 ["prüfbare, eindeutige Anforderungen",
  "dokumentierte Softwarearchitektur",
  "vollständige Rückverfolgbarkeit für Assessments"],
 "Automotive SPICE, ISO 26262, Polarion, IBM DOORS, codebeamer, Enterprise Architect, Jira.",
 [("Helfen Sie bei der Vorbereitung eines ASPICE-Assessments?", "Ja. Wir prüfen Arbeitsprodukte und Rückverfolgbarkeit gegen die Prozessanforderungen und schließen Lücken vor dem Assessment."),
  ("Dokumentieren Sie bestehende Software, deren Entwickler das Projekt verlassen?", "Ja. Strukturierte Übergaben mit Architekturdokumentation und Wissenstransfer gehören zu unseren typischen Aufgaben."),
  ("Mit welchen ALM-Werkzeugen arbeiten Sie?", "Mit Polarion, IBM DOORS und codebeamer, je nach Projektvorgabe.")])

service_page(
 "elektrifizierung-land-baumaschinen",
 "Elektrifizierung von Landmaschinen und Baumaschinen: Batteriesystem, BMS und Sicherheit | dolavolt",
 "Partner für die Elektrifizierung von Land-, Bau- und Kommunalmaschinen: Batteriesystem-Konzept, BMS-Software, Hochvolt-Integration und Sicherheitskonzept nach ISO 25119, ISO 13849 und Maschinenverordnung 2027.",
 "Elektrifizierung Landmaschinen, Elektrifizierung Baumaschinen, Elektrotraktor BMS, LFP LTO Off-Highway, Bergbau Batterie, Nutzfahrzeug Hochvoltbatterie, elektrischer Traktor, Elektro-Traktor, batterieelektrische Landmaschine, Off-Highway Elektrifizierung, Batteriesystem Landtechnik, BMS Landmaschine, BMS Baumaschine, Hochvolt mobile Arbeitsmaschine, elektrisches Kommunalfahrzeug, ISO 25119, ISO 13849, ISO 19014, Maschinenverordnung 2027, Partner Elektrifizierung",
 "Elektrifizierung von Land- und Baumaschinen",
 "Zunehmend werden auch Traktoren, Hoflader, Bagger und Kommunalfahrzeuge elektrisch angetrieben. Die Batterietechnik dafür kommt aus dem Pkw, die Anforderungen sind andere: hohe Dauerlasten, Staub, Vibration, lange Standzeiten und eigene Sicherheitsnormen. Wir bringen unsere Erfahrung aus der Hochvolt-BMS-Serienentwicklung in Ihr Elektrifizierungsprojekt, vom Konzept bis zur sicheren Integration.",
 ["Anforderungen an das Batteriesystem aus Einsatzprofilen und Lastzyklen ableiten",
  "Konzept für Batteriesystem und Hochvoltarchitektur, Bewertung von Spannungslage und Kapazität",
  "Auswahl und technische Bewertung von Batterie- und BMS-Lieferanten",
  "BMS-Software: Zustandsschätzung, Schutzfunktionen, Schützsteuerung, Betriebsmodi und Derating für Arbeitslasten",
  "Ladekonzept für Hof, Baustelle und Depot",
  "Sicherheitskonzept nach ISO 25119, ISO 13849 oder ISO 19014",
  "Unterstützung bei der CE-Konformität nach Maschinenverordnung (EU) 2023/1230 oder der Typgenehmigung nach Verordnung (EU) 167/2013",
  "Integration ins Maschinennetzwerk und Diagnose"],
 ["ein belastbares Lastenheft für das Batteriesystem",
  "ein Sicherheitskonzept, das in die Risikobeurteilung der Maschine passt",
  "integrierte und getestete BMS-Funktionen",
  "Unterlagen für CE-Kennzeichnung oder Typgenehmigung und Batteriepass"],
 "ISO 25119, ISO 13849, ISO 19014, IEC 62619, IEC 61508, Maschinenverordnung (EU) 2023/1230, EU-Batterieverordnung, MATLAB/Simulink, CAN, SAE J1939, CCS2-Laden.",
 [("Haben Sie Erfahrung mit Landmaschinen?", "Unsere Serienerfahrung stammt aus Hochvolt-Batteriesystemen für Pkw. Die Batterietechnik ist im Kern dieselbe. Die Unterschiede bei Lastprofilen, Umgebung und Normen gehen wir gezielt an."),
  ("Welche Sicherheitsnorm gilt für das Batteriesystem einer Landmaschine?", "Für sicherheitsbezogene Steuerungen an Traktoren sowie Land- und Forstmaschinen ISO 25119, für Erdbaumaschinen ISO 19014, allgemein ISO 13849. Für die Batterie wird häufig IEC 62619 herangezogen."),
  ("Was ändert die Maschinenverordnung 2027 für elektrische Maschinen?", "Ab dem 20. Januar 2027 erfasst sie ausdrücklich Software mit Sicherheitsfunktion und verlangt Schutz gegen Korrumpierung. Übernimmt das BMS Sicherheitsfunktionen, gehört es in die Risikobeurteilung der Maschine.")],
 extra='''<h2>Was anders ist als im Pkw</h2>
<ul>
<li><strong>Lastprofil:</strong> hohe Dauerleistung über Stunden statt kurzer Leistungsspitzen</li>
<li><strong>Umgebung:</strong> Staub, Feuchte, Vibration und große Temperaturschwankungen</li>
<li><strong>Standzeiten:</strong> Maschinen stehen saisonal monatelang, Tiefentladeschutz und Lagerstrategie werden wichtig</li>
<li><strong>Normen und Zulassung:</strong> je nach Maschine und Funktion ISO 25119, ISO 13849 oder ISO 19014 statt ISO 26262; für selbstfahrende Arbeitsmaschinen CE-Kennzeichnung nach Maschinenverordnung, für Traktoren Typgenehmigung nach Verordnung (EU) 167/2013</li>
<li><strong>Stückzahlen:</strong> kleine Serien mit vielen Varianten, die Software muss skalieren</li>
</ul>
<p>Mehr dazu im Fachartikel <a href="{r}wissen/maschinenverordnung-2027-batteriesystem.html">Maschinenverordnung 2027 und das Batteriesystem</a>.</p>''',
 audience="Für Hersteller von Land-, Forst-, Bau- und Kommunalmaschinen sowie ihre Zulieferer, die den Schritt zum batterieelektrischen Antrieb gehen und dafür Unterstützung bei Hochvolt- und BMS-Themen brauchen.")

# Leistungsübersicht
rows = [
 ("bms-softwareentwicklung", "Zustandsschätzung, Zellüberwachung, Balancing, Schützsteuerung, Betriebsmodi, Isolationsüberwachung und Ladesteuerung."),
 ("funktionale-sicherheit-iso-26262", "HARA, Sicherheitskonzepte, FMEA, FTA, FMEDA, DFA und Safety Case."),
 ("autosar-embedded-software", "AUTOSAR Classic und Adaptive, Embedded C, RTE und BSW, UDS-Diagnose, CAN FD."),
 ("matlab-simulink-modellbasierte-entwicklung", "Simulink, Stateflow, Embedded Coder, MIL, SIL und Back-to-Back-Tests."),
 ("test-absicherung-hil", "Anforderungsbasierte Tests, HIL, Testautomatisierung und Fehlerinjektion."),
 ("requirements-architektur-aspice", "Anforderungen, Softwarearchitektur, Rückverfolgbarkeit und ASPICE-Assessments."),
]
svc_rows = "".join(f'<a class="read" href="{s}.html"><span class="topic">Leistung</span><div><h3>{dict(SERVICES)[s]}</h3><p>{d}</p></div><span class="go">Mehr</span></a>' for s, d in rows)
page("leistungen/index.html", "Leistungen: Experten für BMS-Software, ISO 26262, AUTOSAR und Simulink | dolavolt",
     "Übersicht unserer Engineering-Leistungen für Hochvolt-Batteriesysteme: BMS-Software, funktionale Sicherheit nach ISO 26262, AUTOSAR, MATLAB/Simulink, Test und HIL, Requirements und ASPICE.",
     f'<section><div class="wrap"><div class="head"><h1>Leistungen</h1><p class="lead">Expertise für Automotive-Entwicklungsteams, von der Anforderung bis zur Serie.</p></div><div class="reads">{svc_rows}</div></div></section>')
