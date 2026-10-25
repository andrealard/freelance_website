
# =====================================================================
# Startseiten – schlank, zwei Schwerpunkte
# =====================================================================
KW_DE = KW_DE + ", Elektrifizierung Landmaschinen, Elektrifizierung Baumaschinen, elektrischer Traktor, Off-Highway Elektrifizierung, ISO 25119, Maschinenverordnung 2027"
KW_EN = KW_EN + ", electrification of agricultural machinery, electric tractor, off-highway electrification, construction machinery battery system, ISO 25119"

SHORT_DE = [
 ("bms-softwareentwicklung", "Batterie", "SoC, SoH und SoP, Schützsteuerung, Betriebsmodi, Isolationsüberwachung, Ladesteuerung."),
 ("elektrifizierung-land-baumaschinen", "Maschinen", "Batteriekonzept, BMS und Sicherheitskonzept für elektrische Arbeitsmaschinen."),
 ("funktionale-sicherheit-iso-26262", "Safety", "HARA, Sicherheitskonzepte, FMEA, FTA und Safety Case."),
 ("autosar-embedded-software", "Software", "AUTOSAR Classic und Adaptive, Embedded C, Diagnose und Integration."),
 ("matlab-simulink-modellbasierte-entwicklung", "Modelle", "Simulink, Stateflow, Embedded Coder, MIL und SIL."),
 ("test-absicherung-hil", "Test", "Anforderungsbasierte Tests, HIL und Testautomatisierung."),
 ("requirements-architektur-aspice", "Prozess", "Anforderungen, Softwarearchitektur und Automotive SPICE."),
]
SHORT_EN = [
 ("bms-softwareentwicklung", "BMS software", "SoC, SoH and SoP, contactor and mode management, insulation monitoring, charge control."),
 ("elektrifizierung-land-baumaschinen", "Electrifying agricultural and construction machinery", "Battery concept, BMS and safety concept for electric working machines."),
 ("funktionale-sicherheit-iso-26262", "Functional safety (ISO 26262)", "HARA, safety concepts, FMEA, FTA and safety case."),
 ("autosar-embedded-software", "AUTOSAR and embedded software", "AUTOSAR Classic and Adaptive, embedded C, diagnostics and integration."),
 ("matlab-simulink-modellbasierte-entwicklung", "MATLAB/Simulink", "Simulink, Stateflow, Embedded Coder, MIL and SIL."),
 ("test-absicherung-hil", "Testing and HIL", "Requirements-based testing, HIL and test automation."),
 ("requirements-architektur-aspice", "Requirements and ASPICE", "Requirements, software architecture and Automotive SPICE."),
]
FAQ_DE = [
 ("Wie arbeiten wir zusammen?", "Als Verstärkung Ihres Teams auf Stunden- oder Tagesbasis im Dienstvertrag oder mit klar abgegrenzten Arbeitspaketen zum Festpreis im Werkvertrag. Sie beauftragen uns direkt oder über Ihren Personaldienstleister."),
 ("Arbeiten Sie remote oder vor Ort?", "Überwiegend remote. Für Workshops, Integration und Tests kommen wir zu Ihnen, im Raum München, Ingolstadt, Regensburg und Stuttgart regelmäßig, europaweit nach Absprache."),
 ("Arbeiten Sie auch außerhalb des Pkw?", "Ja. Wir unterstützen auch Projekte zur Elektrifizierung von Land-, Bau- und Kommunalmaschinen, mit den dort gültigen Normen wie ISO 25119 und ISO 13849 sowie Maschinenverordnung oder Typgenehmigung für Traktoren."),
 ("Übernehmen Sie bestehende Software-Module?", "Ja. Wir übernehmen bestehende Module, arbeiten uns strukturiert ein und dokumentieren so, dass Ihr Team sie später selbst weiterführen kann."),
]
FAQ_EN = [
 ("How do we work together?", "As part of your team on an hourly or daily basis, or through clearly scoped fixed-price work packages. Contract us directly or through your staffing agency."),
 ("Do you work remotely or on site?", "Mostly remotely. We come on site for workshops, integration and testing, regularly around Munich, Ingolstadt, Regensburg and Stuttgart, and across Europe by arrangement."),
 ("Do you work outside passenger cars?", "Yes. We also support projects electrifying agricultural, construction and municipal machinery, under the standards that apply there, such as ISO 25119 and ISO 13849, and the Machinery Regulation or tractor type approval."),
 ("Do you take over existing software modules?", "Yes. We take over existing modules, get up to speed in a structured way and document them so your team can carry them forward."),
]

def facts(rows): return '<dl class="facts">' + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows) + "</dl>"

