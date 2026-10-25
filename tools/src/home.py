
# =====================================================================
# Startseite nach dem Muster echter Expertenseiten
# =====================================================================
def sol(title, today, withus, href, linktext, lab=("Heute", "Mit dolavolt")):
    return (f'<div class="sol"><h3>{title}</h3><p class="today"><b>{lab[0]}</b>{today}</p>'
            f'<p class="with"><b>{lab[1]}</b>{withus}</p><p class="more"><a href="{href}">{linktext}</a></p></div>')

LAB_DE = ("Herausforderung", "Unser Ansatz")
LAB_EN = ("Challenge", "Our approach")

def exp(rows): return '<div class="skills">' + "".join(f'<div class="skill"><h3>{k}</h3><p>{v}</p></div>' for k, v in rows) + "</div>"


HOME_DE = f'''
<section class="hero solo">
 <div class="wrap">
  <h1>Experten für<br>Batterie&shy;management und funktionale Sicherheit.</h1>
  <p class="lead">Ihr Engineering-Partner für Hochvolt-Batteriesysteme: von der Systemanforderung über die BMS-Software bis zum Sicherheitsnachweis. Für Pkw, Nutzfahrzeuge und elektrische Arbeitsmaschinen.</p>
  <div class="actions"><a class="btn" href="#kontakt">Mit einem BMS-Ingenieur sprechen</a><a class="btn quiet" href="#kompetenzen">Kompetenzen ansehen</a></div>
 </div>
</section>

<section id="kompetenzen" class="band">
 <div class="wrap">
  <div class="head"><h2>Kompetenzen</h2><p class="lead">Was wir in Ihr Projekt einbringen. <a href="{{r}}leistungen/">Alle Leistungen im Detail</a></p></div>
  <div class="skills"><div class="skill"><h3>Systems Engineering</h3><p>Systemanforderungen, Lasten- und Pflichtenhefte, Systemkonzepte und Architektur für Hochvolt-Batteriesysteme.</p></div><div class="skill"><h3>BMS-Funktionen</h3><p>Zellüberwachung über AFE in BMU/CMU-Architekturen, Strommessung, Balancing, SOC-, SOH- und SOP-Schätzung, Schützsteuerung und Precharge, Isolationsüberwachung, Fehlerbehandlung und Degradation.</p></div><div class="skill"><h3>Embedded Software</h3><p>Seriensoftware in C auf AUTOSAR-Basis (SWC, RTE, BSW), modellbasiert mit MATLAB/Simulink und Stateflow.</p></div><div class="skill"><h3>Funktionale Sicherheit</h3><p>Serienerfahrung nach ISO 26262 bis ASIL D, auf dieser Grundlage auch IEC 61508, ISO 13849 und ISO 25119: Sicherheitskonzepte, Sicherheitsanalysen, Sicherheitsmechanismen mit Fehlertoleranzzeit und sicherem Zustand.</p></div><div class="skill"><h3>Diagnose und Kommunikation</h3><p>UDS, Fehlerspeicher, XCP, CAN, CAN FD, LIN und J1939, Ladekommunikation nach ISO 15118 und DIN 70121.</p></div><div class="skill"><h3>Verifikation</h3><p>Unit-Tests, statische Codeanalyse nach MISRA C, SIL und HIL, Verifikationsnachweise und Arbeitsprodukte für Automotive-SPICE-Assessments.</p></div></div>
 </div>
</section>

<section id="loesungen">
 <div class="wrap">
  <div class="head"><h2>Wo BMS-Projekte hängen bleiben</h2><p class="lead">Vier Themen, die in BMS-Projekten häufig Aufwand verursachen.</p></div>
  <div class="sols">
   {sol("Ladezustand bei LFP-Zellen", "Im flachen Bereich der Kennlinie ändert sich die Ruhespannung (OCV) einer LFP-Zelle typischerweise um weniger als ein Millivolt pro Prozent Ladezustand. Hinzu kommt eine Hysterese, die von Zelltyp, Temperatur und Vorgeschichte abhängt. Korrekturen über die OCV greifen kaum, Coulomb-Counting driftet mit jedem Offset des Stromsensors.", "Modellbasierte Zustandsschätzer, etwa adaptive Kalman-Filter, abgestimmt auf reale Fahr- und Ladeprofile. Ruhephasen und die steileren Kennlinienbereiche bei niedrigem und hohem Ladezustand nutzen wir zur Rekalibrierung, soweit Relaxationszeit und Temperatur eine belastbare Korrektur zulassen.", "{r}leistungen/bms-softwareentwicklung.html", "BMS-Softwareentwicklung", LAB_DE)}
   {sol("Schütze, Precharge und Fehlerreaktion", "Ein verschweißtes Schütz, ein abgebrochener Precharge, ein Isolationswiderstand unter dem Grenzwert von 100&nbsp;Ω/V für Gleichspannungskreise nach UN-R100: Kritisch sind selten die Nominalzustände, sondern die Übergänge zwischen Fahren, Laden und Abschalten.", "Wir entwickeln Betriebsmodi und Schützsteuerung von den Fehlerfällen her und legen in der Auslegung für jeden Übergang fest, welcher sichere Zustand innerhalb welcher Fehlertoleranzzeit (FTTI) erreicht werden muss.", "{r}leistungen/bms-softwareentwicklung.html", "Schützsteuerung und Betriebsmodi", LAB_DE)}
   {sol("Sicherheitsnachweis nach ISO 26262", "Für ASIL D verlangt ISO 26262 Hardware-Architekturmetriken von mindestens 99&nbsp;% (SPFM) und 90&nbsp;% (LFM). Werden die nötigen Diagnosen spät festgelegt, folgen Iterationen in Hard- und Software.", "Diagnosen, Sicherheitsmechanismen und das Hardware-Software-Interface (HSI) definieren wir parallel zum Systementwurf. Der Sicherheitsnachweis entsteht so mit der Entwicklung.", "{r}leistungen/funktionale-sicherheit-iso-26262.html", "Funktionale Sicherheit nach ISO 26262", LAB_DE)}
   {sol("Elektrifizierung von Land- und Baumaschinen", "Ein Traktor arbeitet stundenlang unter hoher Dauerlast, steht monatelang still und ist dabei Staub, Feuchte und Vibration ausgesetzt. Die Zelltechnik aus dem Pkw lässt sich oft übernehmen, die Betriebsstrategie nicht. An die Stelle von ISO 26262 tritt meist ISO 25119 mit AgPL-Einstufung, je nach Maschine und Funktion ergänzt um ISO 13849 oder ISO 19014.", "Wir übernehmen aus dem Automotive, was passt, und passen an, was die Maschine verlangt: Derating auf Dauerlast, Schutz vor Tiefentladung bei langen Standzeiten und ein Sicherheitskonzept nach der Risikobeurteilung der Maschine (AgPL bzw. PL).", "{r}leistungen/elektrifizierung-land-baumaschinen.html", "Elektrifizierung von Land- und Baumaschinen", LAB_DE)}
  </div>
 </div>
</section>

<section id="trends" class="band">
 <div class="wrap">
  <div class="head"><h2>Was BMS-Teams 2026 und 2027 beschäftigt</h2><p class="lead">Mehrere Vorschriften stellen neue Anforderungen an Zustandsschätzung und Fehlerreaktion.</p></div>
  <div class="trends">
   <div class="trend"><span class="when">01.07.2026</span><h3>China: GB 38031-2025</h3><p>Für neue Typgenehmigungen darf das Batteriesystem bei thermischem Durchgehen einer Zelle weder brennen noch explodieren. Erfüllt wird das vor allem über die Auslegung des Batteriesystems, das BMS liefert Detektion und Warnung. <a href="{{r}}wissen/euro-7-gb-38031-bms.html">Was das für das BMS heißt</a></p></div>
   <div class="trend urgent"><span class="when">29.11.2026</span><h3>Euro 7: Batteriehaltbarkeit</h3><p>Neue Pkw-Typen müssen nach fünf Jahren oder 100.000&nbsp;km noch 80&nbsp;% ihrer zertifizierten Energie haben, nach acht Jahren oder 160.000&nbsp;km noch 72&nbsp;%. Die Genauigkeit der SOH-Schätzung bekommt damit regulatorisches Gewicht.</p></div>
   <div class="trend urgent"><span class="when">20.01.2027</span><h3>Maschinenverordnung</h3><p>Software mit Sicherheitsfunktion und Schutz gegen Korrumpierung werden Teil der CE-Kennzeichnung, auch beim Batteriesystem elektrischer Bau- und selbstfahrender Landmaschinen. Traktoren unterliegen der Typgenehmigung nach Verordnung (EU) 167/2013. <a href="{{r}}wissen/maschinenverordnung-2027-batteriesystem.html">Mehr dazu</a></p></div>
   <div class="trend"><span class="when">18.02.2027</span><h3>EU-Batteriepass</h3><p>Pflicht für EV-Batterien und Industriebatterien über 2&nbsp;kWh. Angaben zum Gesundheitszustand kommen aus dem BMS. <a href="{{r}}wissen/eu-batteriepass-2027.html">Mehr dazu</a></p></div>
   <div class="trend"><span class="when">In Serie</span><h3>Elektrische Traktoren</h3><p>Mit dem Fendt e107 Vario ist ein Elektrotraktor mit 100&nbsp;kWh und DC-Laden bis 80&nbsp;kW in Serie. Dauerlast, lange Standzeiten und Feldbedingungen stellen andere Anforderungen an das BMS als der Pkw.</p></div>
  </div>
 </div>
</section>

<section id="erfahrung">
 <div class="wrap">
  <div class="head"><h2>Worauf unsere Arbeit beruht</h2><p class="lead">Langjährige Erfahrung in der Serienentwicklung von Hochvolt-Batteriemanagementsystemen.</p></div>
  {exp([("BMS-Entwicklung", "Entwicklung von Hochvolt-BMS-Software für die Pkw-Serie nach ISO 26262 und Automotive SPICE, von der Anforderung bis zum Release."),
        ("Konzeption", "System-, Betriebs- und Sicherheitskonzepte für Hochvolt-Batteriesysteme."),
        ("Architektur", "System- und Softwarearchitekturen für das BMS, von der Funktionsaufteilung bis zur Schnittstelle zwischen Hardware und Software.")])}
 </div>
</section>

<section id="faq" class="band">
 <div class="wrap">
  <div class="head"><h2>Häufige Fragen</h2><p></p></div>
  <div class="faq">{faq_html(FAQ_DE)}</div>
 </div>
</section>

<section id="kontakt" class="contact">
 <div class="wrap contact-grid">
  <div><h2>Wo hängt Ihr BMS-Projekt?</h2><p>Schildern Sie uns das technische Problem. Sie bekommen innerhalb von zwei Werktagen eine Antwort von einem Ingenieur.</p></div>
  <div><a class="mail" href="mailto:hallo@dolavolt.de?subject=Projektanfrage">hallo@dolavolt.de</a></div>
 </div>
</section>'''

HOME_EN = f'''
<section class="hero solo">
 <div class="wrap">
  <h1>Experts in battery management and functional safety.</h1>
  <p class="lead">Your engineering partner for high-voltage battery systems: from system requirements and BMS software to the safety case. For passenger cars, commercial vehicles and electric working machines.</p>
  <div class="actions"><a class="btn" href="#contact">Talk to a BMS engineer</a><a class="btn quiet" href="#skills">See our skills</a></div>
 </div>
</section>

<section id="skills" class="band">
 <div class="wrap">
  <div class="head"><h2>Competencies</h2><p class="lead">What we bring to your project.</p></div>
  <div class="skills"><div class="skill"><h3>Systems engineering</h3><p>System requirements, specifications, system concepts and architecture for high-voltage battery systems.</p></div><div class="skill"><h3>BMS functions</h3><p>Cell monitoring via AFE in BMU/CMU architectures, current measurement, balancing, SOC, SOH and SOP estimation, contactor control and precharge, insulation monitoring, fault handling and degradation.</p></div><div class="skill"><h3>Embedded software</h3><p>Production software in C on AUTOSAR, model-based with MATLAB/Simulink and Stateflow.</p></div><div class="skill"><h3>Functional safety</h3><p>Series experience under ISO 26262 up to ASIL D, and on that basis IEC 61508, ISO 13849 and ISO 25119: safety concepts, safety analyses, safety mechanisms with fault tolerant time interval and safe state.</p></div><div class="skill"><h3>Diagnostics and communication</h3><p>UDS, fault memory, XCP, CAN, CAN FD, LIN and J1939, charging communication to ISO 15118 and DIN 70121.</p></div><div class="skill"><h3>Verification</h3><p>Unit testing, MISRA C static analysis, SIL and HIL, verification evidence and work products for Automotive SPICE assessments.</p></div></div>
 </div>
</section>

<section id="solutions">
 <div class="wrap">
  <div class="head"><h2>Where BMS projects get stuck</h2><p class="lead">Four topics that often cost time in BMS projects.</p></div>
  <div class="sols">
   {sol("State of charge with LFP cells", "In the flat region of the curve, the open-circuit voltage (OCV) of an LFP cell typically changes by less than one millivolt per percent of state of charge, plus hysteresis that depends on cell type, temperature and history. OCV-based correction barely works, and coulomb counting drifts with every current-sensor offset.", "Model-based state estimators, such as adaptive Kalman filters, tuned on real driving and charging profiles. We use rest phases and the steeper parts of the curve at low and high state of charge for recalibration, where relaxation time and temperature allow a reliable correction.", "{r}leistungen/bms-softwareentwicklung.html", "BMS software development (DE)", LAB_EN)}
   {sol("Contactors, precharge and fault reaction", "A welded contactor, an aborted precharge, insulation resistance below the UN R100 limit of 100&nbsp;Ω/V for DC circuits: the critical moments are rarely the nominal states but the transitions between driving, charging and shutdown.", "We design mode and contactor management from the failure cases and, during design, define for every transition the safe state and the fault tolerant time interval (FTTI) within which it must be reached.", "{r}leistungen/bms-softwareentwicklung.html", "Contactor and mode management (DE)", LAB_EN)}
   {sol("ISO 26262 safety evidence", "For ASIL D, ISO 26262 requires hardware architectural metrics of at least 99&nbsp;% (SPFM) and 90&nbsp;% (LFM). If the necessary diagnostics are defined late, iterations in hardware and software follow.", "We define diagnostics, safety mechanisms and the hardware-software interface (HSI) alongside the system design, so the safety case grows with the development.", "{r}leistungen/funktionale-sicherheit-iso-26262.html", "Functional safety (DE)", LAB_EN)}
   {sol("Electrifying agricultural and construction machinery", "A tractor works for hours under high continuous load, sits idle for months and is exposed to dust, moisture and vibration throughout. Cell technology from cars often carries over; the operating strategy does not. ISO 25119 with AgPL ratings usually takes the place of ISO 26262, supplemented by ISO 13849 or ISO 19014 depending on machine and function.", "We keep what fits from automotive and adapt what the machine demands: derating for continuous load, deep-discharge protection for long idle periods and a safety concept based on the machine's risk assessment (AgPL or PL).", "{r}leistungen/elektrifizierung-land-baumaschinen.html", "Electrifying machinery (DE)", LAB_EN)}
  </div>
 </div>
</section>

<section id="trends" class="band">
 <div class="wrap">
  <div class="head"><h2>What keeps BMS teams busy in 2026 and 2027</h2><p class="lead">Several regulations set new requirements for state estimation and fault reaction.</p></div>
  <div class="trends">
   <div class="trend"><span class="when">1 Jul 2026</span><h3>China: GB 38031-2025</h3><p>For new type approvals, the battery system must neither catch fire nor explode if a cell goes into thermal runaway. This is achieved mainly through pack design; the BMS provides detection and warning.</p></div>
   <div class="trend urgent"><span class="when">29 Nov 2026</span><h3>Euro 7: battery durability</h3><p>New passenger-car types must retain 80&nbsp;% of certified energy after five years or 100,000&nbsp;km and 72&nbsp;% after eight years or 160,000&nbsp;km. The accuracy of SOH estimation gains regulatory weight.</p></div>
   <div class="trend urgent"><span class="when">20 Jan 2027</span><h3>EU Machinery Regulation</h3><p>Software with a safety function and protection against corruption become part of CE marking, including for the battery system of electric construction and self-propelled agricultural machinery. Tractors fall under EU type approval (Regulation (EU) 167/2013).</p></div>
   <div class="trend"><span class="when">18 Feb 2027</span><h3>EU battery passport</h3><p>Mandatory for EV batteries and industrial batteries above 2&nbsp;kWh. State-of-health data comes from the BMS.</p></div>
   <div class="trend"><span class="when">In production</span><h3>Electric tractors</h3><p>The Fendt e107 Vario, an electric tractor with 100&nbsp;kWh and DC charging up to 80&nbsp;kW, is in series production. Continuous load, long idle periods and field conditions place different demands on the BMS than a car.</p></div>
  </div>
 </div>
</section>

<section id="experience">
 <div class="wrap">
  <div class="head"><h2>What our work is built on</h2><p class="lead">Many years of experience in series development of high-voltage battery management systems.</p></div>
  {exp([("BMS development", "Development of high-voltage BMS software for passenger-car series production to ISO 26262 and Automotive SPICE, from requirements to release."),
        ("Concepts", "System, operating and safety concepts for high-voltage battery systems."),
        ("Architecture", "System and software architectures for the BMS, from function allocation to the hardware-software interface.")])}
 </div>
</section>

<section id="faq" class="band">
 <div class="wrap"><div class="head"><h2>Questions</h2><p></p></div><div class="faq">{faq_html(FAQ_EN)}</div></div>
</section>

<section id="contact" class="contact">
 <div class="wrap contact-grid">
  <div><h2>Where is your BMS project stuck?</h2><p>Describe the technical problem. Within two business days you get an answer from an engineer.</p></div>
  <div><a class="mail" href="mailto:hallo@dolavolt.de?subject=Project%20inquiry">hallo@dolavolt.de</a></div>
 </div>
</section>'''


KW_DE = KW_DE + ", Experten Batteriemanagement, Systemingenieur BMS, Lastenheft Batteriesystem, Euro 7 Batteriehaltbarkeit, SOCE, GB 38031, thermisches Durchgehen, Thermal Runaway Erkennung, ECE-R100, IEC 62619, J1939, Nutzfahrzeug Hochvoltbatterie, Elektrotraktor, Fendt e107"
KW_EN = KW_EN + ", BMS experts, BMS systems engineer, Euro 7 battery durability, SOCE, GB 38031, thermal runaway detection, J1939, commercial vehicle battery"
page("index.html", "Experten für Batteriemanagement (BMS) und funktionale Sicherheit nach ISO 26262 | dolavolt",
     "Experten für Batteriemanagement-Software und funktionale Sicherheit: Systemkonzepte, SOC/SOH/SOP, Schützsteuerung, AUTOSAR, MATLAB/Simulink, ISO 26262 bis ASIL D, ISO 25119. Für Pkw, Nutzfahrzeuge und elektrische Land- und Baumaschinen. Auch als Freelancer, aus München.",
     HOME_DE, {"@context": "https://schema.org", "@graph": [ORG, SERVICE, {"@type": "WebSite", "url": BASE + "/", "name": "dolavolt", "inLanguage": "de-DE"}, faq_schema(FAQ_DE)]},
     extra_head=HREFLANG + f'<meta name="keywords" content="{KW_DE}">\n')
page("en/index.html", "Experts in Battery Management (BMS) and ISO 26262 Functional Safety | dolavolt",
     "Experts in battery management software and functional safety: system concepts, SOC/SOH/SOP, contactor control, AUTOSAR, MATLAB/Simulink, ISO 26262 up to ASIL D, ISO 25119. For cars, commercial vehicles and electric agricultural and construction machinery. Freelance or fixed-price, based in Munich.",
     HOME_EN, {"@context": "https://schema.org", "@graph": [ORG, faq_schema(FAQ_EN)]}, lang="en",
     extra_head=HREFLANG + f'<meta name="keywords" content="{KW_EN}">\n')
