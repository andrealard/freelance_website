
# =====================================================================
# Startseite nach dem Muster echter Expertenseiten
# =====================================================================
def sol(title, today, withus, href, linktext, lab=("Heute", "Mit dolavolt")):
    return (f'<div class="sol"><h3>{title}</h3>{FIGS.get(title, "")}<p class="today"><b>{lab[0]}</b>{today}</p>'
            f'<p class="with"><b>{lab[1]}</b>{withus}</p><p class="more"><a href="{href}">{linktext}</a></p></div>')

LAB_DE = ("Herausforderung", "Unser Ansatz")
LAB_EN = ("Challenge", "Our approach")

def exp(rows): return '<div class="skills">' + "".join(f'<div class="skill"><h3>{k}</h3><p>{v}</p></div>' for k, v in rows) + "</div>"


def form(lang):
    de = lang == "de"
    L = (dict(n="Name", c="Unternehmen", e="E-Mail", p="Telefon (optional)", t="Thema", m="Ihr Anliegen",
              mp="Worum geht es, in welcher Phase ist das Projekt, ab wann und in welchem Umfang brauchen Sie Unterstützung?",
              opts=["BMS-Softwareentwicklung", "Funktionale Sicherheit", "Elektrifizierung Land- und Baumaschinen", "Systems Engineering und Architektur", "Sonstiges"],
              b="Anfrage senden", note='Wir nutzen Ihre Angaben nur zur Beantwortung der Anfrage.' + (' Details in der <a href="{r}datenschutz.html">Datenschutzerklärung</a>.' if LEGAL else ''),
              alt="Oder direkt per E-Mail:")
         if de else
         dict(n="Name", c="Company", e="Email", p="Phone (optional)", t="Topic", m="Your request",
              mp="What is it about, what phase is the project in, from when and to what extent do you need support?",
              opts=["BMS software development", "Functional safety", "Electrifying agricultural and construction machinery", "Systems engineering and architecture", "Other"],
              b="Send request", note='We use your details only to answer your request.' + (' See our <a href="{r}datenschutz.html">privacy policy</a>.' if LEGAL else ''),
              alt="Or email us directly:"))
    o = "".join(f"<option>{x}</option>" for x in L["opts"])
    return f"""<form class="cform" method="post" action="/anfrage">
   <input type="hidden" name="lang" value="{lang}">
   <div class="hp" aria-hidden="true"><label>Website <input name="website" tabindex="-1" autocomplete="off"></label></div>
   <div class="row2"><label>{L['n']}<input name="name" required maxlength="120" autocomplete="name"></label><label>{L['c']}<input name="company" maxlength="160" autocomplete="organization"></label></div>
   <div class="row2"><label>{L['e']}<input type="email" name="email" required maxlength="200" autocomplete="email"></label><label>{L['p']}<input type="tel" name="phone" maxlength="60" autocomplete="tel"></label></div>
   <label>{L['t']}<select name="topic">{o}</select></label>
   <label>{L['m']}<textarea name="message" required minlength="20" maxlength="5000" rows="6" placeholder="{L['mp']}"></textarea></label>
   <button class="btn" type="submit">{L['b']}</button>
   <p class="fnote">{L['note']}</p>
   <p class="fnote">{L['alt']} <a href="mailto:hallo@dolavolt.de">hallo@dolavolt.de</a></p>
  </form>"""
FORM_DE, FORM_EN = form("de"), form("en")

HOME_DE = f'''
<section class="hero solo">
 <div class="wrap">
  <h1>Experten für<br>Batterie&shy;management und funktionale Sicherheit</h1>
  <p class="lead">Ihr Engineering-Partner für Hochvolt-Batteriesysteme, von der Anforderung bis zum Sicherheitsnachweis. Für Pkw, Nutzfahrzeuge und elektrische Arbeitsmaschinen.</p>
  <div class="actions"><a class="btn" href="#kontakt">Projekt anfragen</a><a class="btn quiet" href="#kompetenzen">Kompetenzen ansehen</a></div>
 </div>
</section>

<section id="kompetenzen" class="band">
 <div class="wrap">
  <div class="head"><h2>Kompetenzen</h2><p class="lead">Was wir in Ihr Projekt einbringen. <a href="{{r}}leistungen/">Alle Leistungen im Detail</a></p></div>
  <div class="skills"><div class="skill"><h3>Systems Engineering</h3><p>Systemanforderungen, Lastenhefte, Systemkonzepte und Architektur.</p></div><div class="skill"><h3>BMS-Funktionen</h3><p>Zellüberwachung, Strommessung, Balancing, Schätzung von Ladezustand, Alterung und verfügbarer Leistung (SOC, SOH, SOP), Schützsteuerung, Isolationsüberwachung und Fehlerbehandlung.</p></div><div class="skill"><h3>Embedded Software</h3><p>Seriensoftware in C auf AUTOSAR, modellbasiert mit MATLAB/Simulink.</p></div><div class="skill"><h3>Funktionale Sicherheit</h3><p>ISO 26262 bis ASIL D, außerdem ISO 25119 und ISO 13849: Sicherheitskonzepte, Sicherheitsanalysen und Sicherheitsmechanismen.</p></div><div class="skill"><h3>Diagnose und Kommunikation</h3><p>UDS, XCP, CAN FD und J1939, Laden nach ISO 15118, Cybersecurity nach ISO/SAE 21434 und Over-the-Air-Updates.</p></div><div class="skill"><h3>Verifikation</h3><p>Unit-Tests, MISRA C, SIL und HIL, Nachweise für ISO 26262 und Automotive SPICE.</p></div></div>
 </div>
</section>

<section id="loesungen">
 <div class="wrap">
  <div class="head"><h2>Wo Erfahrung den Unterschied macht</h2><p class="lead">Vier Kernthemen der BMS-Entwicklung und unser Ansatz dazu</p></div>
  <div class="sols">
   {sol("Ladezustand bei LFP-Zellen", "Im flachen Bereich der Kennlinie ändert sich die Ruhespannung einer LFP-Zelle typischerweise um weniger als 1&nbsp;mV pro Prozent Ladezustand, dazu kommt Hysterese. OCV-Korrekturen greifen kaum, Coulomb-Counting driftet.", "Modellbasierte Schätzer wie adaptive Kalman-Filter, abgestimmt auf reale Fahr- und Ladeprofile. Ruhephasen und steile Kennlinienbereiche nutzen wir zur Rekalibrierung.", "{r}leistungen/bms-softwareentwicklung.html", "BMS-Softwareentwicklung", LAB_DE)}
   {sol("Schütze, Precharge und Fehlerreaktion", "Verschweißtes Schütz, abgebrochener Precharge, Isolationsfehler: Kritisch sind selten die Nominalzustände, sondern die Übergänge zwischen Fahren, Laden und Abschalten.", "Normalbetrieb und Fehlerfälle spezifizieren wir gemeinsam. Für jeden sicherheitsrelevanten Fehler sind Erkennung und sicherer Zustand festgelegt und gegen die Fehlertoleranzzeit (FTTI) abgesichert.", "{r}leistungen/bms-softwareentwicklung.html", "Schützsteuerung und Betriebsmodi", LAB_DE)}
   {sol("Sicherheitsnachweis nach ISO 26262", "Für Sicherheitsziele mit ASIL D verlangt ISO 26262 Hardware-Metriken von mindestens 99&nbsp;% (SPFM) und 90&nbsp;% (LFM). Werden Diagnosen spät festgelegt, folgen Iterationen in Hard- und Software.", "Diagnosen, Sicherheitsmechanismen und HSI definieren wir parallel zum Systementwurf. Der Nachweis wächst mit der Entwicklung.", "{r}leistungen/funktionale-sicherheit-iso-26262.html", "Funktionale Sicherheit nach ISO 26262", LAB_DE)}
   {sol("Elektrifizierung von Land- und Baumaschinen", "Ein Traktor arbeitet stundenlang unter Dauerlast und steht monatelang still, bei Staub, Feuchte und Vibration. Die Zellen lassen sich oft aus dem Pkw übernehmen, die Betriebsstrategie nicht.", "Derating auf Dauerlast, Tiefentladeschutz für lange Standzeiten und ein Sicherheitskonzept nach der Risikobeurteilung der Maschine.", "{r}leistungen/elektrifizierung-land-baumaschinen.html", "Elektrifizierung von Land- und Baumaschinen", LAB_DE)}
  </div>
 </div>
</section>

<section id="trends" class="band">
 <div class="wrap">
  <div class="head"><h2>Aktuelle Entwicklungen</h2><p class="lead">Mehrere Vorschriften stellen neue Anforderungen an Zustandsschätzung, Fehlerreaktion und Software-Updates</p></div>
  <div class="trends">
   <div class="trend"><span class="when">01.07.2026</span><h3>China: GB 38031-2025</h3><p>Seit 1.7.2026 in Kraft: In der Propagationsprüfung darf das Batteriesystem weder brennen noch explodieren, eine Warnung muss rechtzeitig kommen. Das BMS liefert Detektion, Warnung und Fehlerreaktion. <a href="{{r}}wissen/euro-7-gb-38031-bms.html">Was das für das BMS heißt</a></p></div>
   <div class="trend"><span class="when">29.11.2026</span><h3>Euro 7: Batteriehaltbarkeit</h3><p>Neue Pkw-Typen brauchen nach fünf Jahren oder 100.000&nbsp;km noch 80&nbsp;% ihrer zertifizierten Energie, nach acht Jahren oder 160.000&nbsp;km noch 72&nbsp;%. Die SOCE-Ermittlung wird typgenehmigungsrelevant.</p></div>
   <div class="trend"><span class="when">20.01.2027</span><h3>Maschinenverordnung</h3><p>Software mit Sicherheitsfunktion und der Schutz gegen Korrumpierung fließen in die Konformitätsbewertung ein, je nach Funktion auch beim Batteriesystem elektrischer Arbeitsmaschinen. <a href="{{r}}wissen/maschinenverordnung-2027-batteriesystem.html">Mehr dazu</a></p></div>
   <div class="trend"><span class="when">18.02.2027</span><h3>EU-Batteriepass</h3><p>Pflicht für EV-Batterien und Industriebatterien über 2&nbsp;kWh. Angaben zum Gesundheitszustand kommen aus dem BMS. <a href="{{r}}wissen/eu-batteriepass-2027.html">Mehr dazu</a></p></div>
   <div class="trend"><span class="when">Laufend</span><h3>Software-Defined Vehicle</h3><p>Seit Juli 2024 gelten in der EU für alle Neufahrzeuge UN R155 (Cybersecurity) und R156 (Software-Updates). Jedes BMS-Update muss sicher, nachvollziehbar und im Sicherheitsnachweis abgedeckt sein. <a href="{{r}}wissen/software-defined-vehicle-bms.html">Mehr dazu</a></p></div>
  </div>
 </div>
</section>

<section id="erfahrung">
 <div class="wrap">
  <div class="head"><h2>Erfahrung</h2><p class="lead">Langjährige Erfahrung mit Batteriesystemen in der Pkw-Entwicklung, im Hoch- und im Niedervolt</p></div>
  {exp([("BMS-Entwicklung", "Hochvolt-BMS-Software für Pkw-Serienprojekte führender Automobilhersteller, entwickelt nach ISO 26262 und Automotive SPICE."),
        ("Konzepte und Architektur", "System-, Betriebs- und Sicherheitskonzepte sowie System- und Softwarearchitekturen für das BMS."),
        ("OEM-Integration", "Enge Zusammenarbeit mit Automobilherstellern bei der Integration ihrer Softwarekomponenten in das BMS."),
        ("Niedervoltspeicher", "Entwicklung von Niedervolt-Batteriespeichern im Pkw.")])}
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
  <div><h2>Sprechen wir über Ihr Projekt</h2><p>Beschreiben Sie kurz Aufgabe, Projektphase und Zeitrahmen. Sie bekommen innerhalb von zwei Werktagen eine Antwort von uns.</p></div>
  <div>{FORM_DE}</div>
 </div>
</section>'''

HOME_EN = f'''
<section class="hero solo">
 <div class="wrap">
  <h1>Experts in battery management and functional safety</h1>
  <p class="lead">Your engineering partner for high-voltage battery systems, from requirements to the safety case. For passenger cars, commercial vehicles and electric working machines.</p>
  <div class="actions"><a class="btn" href="#contact">Discuss your project</a><a class="btn quiet" href="#skills">See our skills</a></div>
 </div>
</section>

<section id="skills" class="band">
 <div class="wrap">
  <div class="head"><h2>Competencies</h2><p class="lead">What we bring to your project.</p></div>
  <div class="skills"><div class="skill"><h3>Systems engineering</h3><p>System requirements, specifications, system concepts and architecture.</p></div><div class="skill"><h3>BMS functions</h3><p>Cell monitoring, current measurement, balancing, estimation of state of charge, state of health and available power (SOC, SOH, SOP), contactor control, insulation monitoring and fault handling.</p></div><div class="skill"><h3>Embedded software</h3><p>Production software in C on AUTOSAR, model-based with MATLAB/Simulink.</p></div><div class="skill"><h3>Functional safety</h3><p>ISO 26262 up to ASIL D, plus ISO 25119 and ISO 13849: safety concepts, safety analyses and safety mechanisms.</p></div><div class="skill"><h3>Diagnostics and communication</h3><p>UDS, XCP, CAN FD and J1939, charging to ISO 15118, cybersecurity to ISO/SAE 21434 and over-the-air updates.</p></div><div class="skill"><h3>Verification</h3><p>Unit testing, MISRA C, SIL and HIL, evidence for ISO 26262 and Automotive SPICE.</p></div></div>
 </div>
</section>

<section id="solutions">
 <div class="wrap">
  <div class="head"><h2>Where experience makes the difference</h2><p class="lead">Four core topics in BMS development and how we approach them</p></div>
  <div class="sols">
   {sol("State of charge with LFP cells", "In the flat region of the curve, the rest voltage of an LFP cell typically changes by less than 1&nbsp;mV per percent of state of charge, plus hysteresis. OCV correction barely works, coulomb counting drifts.", "Model-based estimators such as adaptive Kalman filters, tuned on real driving and charging profiles. We use rest phases and steep parts of the curve for recalibration.", "{r}leistungen/bms-softwareentwicklung.html", "BMS software development (DE)", LAB_EN)}
   {sol("Contactors, precharge and fault reaction", "Welded contactor, aborted precharge, insulation fault: the critical moments are rarely the nominal states but the transitions between driving, charging and shutdown.", "We specify normal operation and failure cases together. For every safety-relevant fault, detection and safe state are defined and verified against the fault tolerant time interval (FTTI).", "{r}leistungen/bms-softwareentwicklung.html", "Contactor and mode management (DE)", LAB_EN)}
   {sol("ISO 26262 safety evidence", "For ASIL D safety goals, ISO 26262 requires hardware metrics of at least 99&nbsp;% (SPFM) and 90&nbsp;% (LFM). If diagnostics are defined late, iterations in hardware and software follow.", "We define diagnostics, safety mechanisms and HSI alongside the system design. The safety case grows with the development.", "{r}leistungen/funktionale-sicherheit-iso-26262.html", "Functional safety (DE)", LAB_EN)}
   {sol("Electrifying agricultural and construction machinery", "A tractor works for hours under continuous load and sits idle for months, in dust, moisture and vibration. Cells often carry over from cars, the operating strategy does not.", "Derating for continuous load, deep-discharge protection for long idle periods and a safety concept based on the machine's risk assessment.", "{r}leistungen/elektrifizierung-land-baumaschinen.html", "Electrifying machinery (DE)", LAB_EN)}
  </div>
 </div>
</section>

<section id="trends" class="band">
 <div class="wrap">
  <div class="head"><h2>Current developments</h2><p class="lead">Several regulations set new requirements for state estimation, fault reaction and software updates</p></div>
  <div class="trends">
   <div class="trend"><span class="when">1 Jul 2026</span><h3>China: GB 38031-2025</h3><p>In force since 1 July 2026: in the propagation test the battery system must neither catch fire nor explode, and a timely warning is required. The BMS provides detection, warning and fault reaction.</p></div>
   <div class="trend"><span class="when">29 Nov 2026</span><h3>Euro 7: battery durability</h3><p>New passenger-car types must retain 80&nbsp;% of certified energy after five years or 100,000&nbsp;km and 72&nbsp;% after eight years or 160,000&nbsp;km. SOCE determination becomes relevant for type approval.</p></div>
   <div class="trend"><span class="when">20 Jan 2027</span><h3>EU Machinery Regulation</h3><p>Software with a safety function and protection against corruption feed into the conformity assessment, depending on the function also for the battery system of electric work machines.</p></div>
   <div class="trend"><span class="when">18 Feb 2027</span><h3>EU battery passport</h3><p>Mandatory for EV batteries and industrial batteries above 2&nbsp;kWh. State-of-health data comes from the BMS.</p></div>
   <div class="trend"><span class="when">Ongoing</span><h3>Software-defined vehicle</h3><p>Since July 2024, UN R155 (cybersecurity) and R156 (software updates) apply to all new vehicles in the EU. Every BMS update must be secure, traceable and covered by the safety case.</p></div>
  </div>
 </div>
</section>

<section id="experience">
 <div class="wrap">
  <div class="head"><h2>Experience</h2><p class="lead">Many years of experience with battery systems in passenger-car development, high and low voltage</p></div>
  {exp([("BMS development", "High-voltage BMS software for passenger-car series projects of leading carmakers, developed to ISO 26262 and Automotive SPICE."),
        ("Concepts and architecture", "System, operating and safety concepts as well as system and software architectures for the BMS."),
        ("OEM integration", "Close cooperation with carmakers on integrating their software components into the BMS."),
        ("Low-voltage storage", "Development of low-voltage battery storage for passenger cars.")])}
 </div>
</section>

<section id="faq" class="band">
 <div class="wrap"><div class="head"><h2>Questions</h2><p></p></div><div class="faq">{faq_html(FAQ_EN)}</div></div>
</section>

<section id="contact" class="contact">
 <div class="wrap contact-grid">
  <div><h2>Let’s talk about your project</h2><p>Briefly describe the task, project phase and timeline. You will hear from us within two business days.</p></div>
  <div>{FORM_EN}</div>
 </div>
</section>'''


KW_DE = KW_DE + ", Experten Batteriemanagement, Systemingenieur BMS, Lastenheft Batteriesystem, Euro 7 Batteriehaltbarkeit, SOCE, GB 38031, thermisches Durchgehen, Thermal Runaway Erkennung, ECE-R100, IEC 62619, J1939, Nutzfahrzeug Hochvoltbatterie, Elektrotraktor, elektrische Arbeitsmaschine"
KW_EN = KW_EN + ", BMS experts, BMS systems engineer, Euro 7 battery durability, SOCE, GB 38031, thermal runaway detection, J1939, commercial vehicle battery"
HOME_DE, HOME_EN = with_icons(HOME_DE), with_icons(HOME_EN)
page("index.html", "Experten für Batteriemanagement (BMS) und funktionale Sicherheit nach ISO 26262 | dolavolt",
     "Experten für Batteriemanagement-Software und funktionale Sicherheit: Systemkonzepte, SOC/SOH/SOP, Schützsteuerung, AUTOSAR, MATLAB/Simulink, ISO 26262 bis ASIL D, ISO 25119. Für Pkw, Nutzfahrzeuge und elektrische Land- und Baumaschinen. Remote oder vor Ort.",
     HOME_DE, {"@context": "https://schema.org", "@graph": [ORG, SERVICE, {"@type": "WebSite", "url": BASE + "/", "name": "dolavolt", "inLanguage": "de-DE"}, faq_schema(FAQ_DE)]},
     extra_head=HREFLANG + f'<meta name="keywords" content="{KW_DE}">\n')
page("en/index.html", "Experts in Battery Management (BMS) and ISO 26262 Functional Safety | dolavolt",
     "Experts in battery management software and functional safety: system concepts, SOC/SOH/SOP, contactor control, AUTOSAR, MATLAB/Simulink, ISO 26262 up to ASIL D, ISO 25119. For cars, commercial vehicles and electric agricultural and construction machinery. Remote or on site.",
     HOME_EN, {"@context": "https://schema.org", "@graph": [ORG, faq_schema(FAQ_EN)]}, lang="en",
     extra_head=HREFLANG + f'<meta name="keywords" content="{KW_EN}">\n')
