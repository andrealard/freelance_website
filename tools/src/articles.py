
# =====================================================================
# Fachartikel
# =====================================================================

# ---------- 1: Batteriespeicher / Artikel 12 ----------
article(
 "batteriespeicher-sicherheit-artikel-12",
 "Sicherheit stationärer Batteriespeicher: Artikel 12 der Batterieverordnung erklärt | dolavolt",
 "Was Artikel 12 der EU-Batterieverordnung von Herstellern und Integratoren stationärer Batteriespeicher verlangt, welche elf Sicherheitsparameter geprüft werden und welche Rolle das BMS dabei spielt.",
 "Batteriespeicher sicher nachweisen: Was Artikel 12 der Batterieverordnung verlangt",
 "Für stationäre Batteriespeicher gibt es im EU-Recht eine eigene Sicherheitsvorschrift. Viele Integratoren stützen sich dabei auf die Datenblätter ihrer Zell- und BMS-Lieferanten. Das allein reicht selten, denn die Verordnung verlangt den Nachweis für das System, das Sie in Verkehr bringen, nicht für seine Bauteile.",
 '''
<div class="box"><p><strong>Kurz gesagt:</strong> Artikel 12 der Verordnung (EU) 2023/1542 verlangt, dass stationäre Batteriespeicher bei normalem Betrieb und bestimmungsgemäßer Verwendung sicher sind. Seit dem 18. August 2024 muss das in den technischen Unterlagen belegt sein, unter anderem durch Prüfungen zu elf Sicherheitsparametern aus Anhang V. Bei mehreren davon wird im Kern geprüft, ob das Batteriemanagementsystem richtig reagiert.</p></div>

<h2>Was Artikel 12 verlangt</h2>
<p>Die Grundanforderung ist knapp formuliert: Ein stationäres Batterie-Energiespeichersystem muss bei normalem Betrieb und bestimmungsgemäßer Verwendung sicher sein. Die technischen Unterlagen müssen das belegen. Konkret gehören dazu:</p>
<ul>
<li>Nachweise über erfolgreich bestandene Prüfungen zu den Sicherheitsparametern aus Anhang V, durchgeführt nach dem Stand der Technik,</li>
<li>eine Bewertung von Sicherheitsrisiken, die Anhang V nicht abdeckt, und der Nachweis, dass sie gemindert und geprüft wurden,</li>
<li>Anweisungen, wie sich Risiken im Fall eines Brands oder einer Explosion verringern lassen,</li>
<li>eine Überarbeitung der Unterlagen, wenn eine Batterie für Wiederverwendung, Umnutzung oder Wiederaufarbeitung vorbereitet wird.</li>
</ul>
<p>Die Parameter in Anhang V sind dabei nur relevant, soweit unter den vom Hersteller vorgesehenen Bedingungen tatsächlich eine entsprechende Gefährdung besteht. Diese Einschätzung müssen Sie begründen können.</p>

<h2>Die elf Sicherheitsparameter aus Anhang V</h2>
<p>Die Tabelle zeigt, welcher Teil des Systems bei den einzelnen Parametern typischerweise die Schutzwirkung trägt. Die Zuordnung ist unsere fachliche Einschätzung, keine Vorgabe der Verordnung.</p>
<table>
<tr><th>Parameter</th><th>Wer die Schutzwirkung trägt</th></tr>
<tr><td>Überladeschutz</td><td><strong>BMS</strong> mit Schütz oder Halbleiterschalter</td></tr>
<tr><td>Tiefentladeschutz</td><td><strong>BMS</strong></td></tr>
<tr><td>Übertemperaturschutz</td><td><strong>BMS</strong> und Thermomanagement</td></tr>
<tr><td>Schutz vor externem Kurzschluss</td><td><strong>BMS</strong> zusammen mit Sicherung und Schütz</td></tr>
<tr><td>Schutz vor thermischer Ausbreitung</td><td>Systemdesign, unterstützt durch Früherkennung im BMS</td></tr>
<tr><td>Gasemission</td><td>Systemdesign, Lüftung und Detektion</td></tr>
<tr><td>Thermischer Schock und Temperaturwechsel</td><td>Zelle und Mechanik</td></tr>
<tr><td>Mechanische Beschädigung durch äußere Kräfte</td><td>Gehäuse und Mechanik</td></tr>
<tr><td>Interner Kurzschluss</td><td>Zelle</td></tr>
<tr><td>Thermischer Missbrauch</td><td>Zelle</td></tr>
<tr><td>Feuer</td><td>Systemdesign und Aufstellung</td></tr>
</table>
<p>Nach unserer Einschätzung trägt das BMS bei vier der elf Parameter die Schutzwirkung maßgeblich mit, bei zwei weiteren ist es Teil der Lösung.</p>

<h2>Warum ein Datenblatt nicht reicht</h2>
<p>Ein Datenblatt zeigt, dass eine Schutzfunktion existiert. Ein Nachweis zeigt, dass sie auch dann greift, wenn ein Temperatursensor falsche Werte liefert, ein Schütz verschweißt ist oder die Kommunikation zum Wechselrichter abbricht. Genau diese Fehlerfälle sind es, die in der Praxis zu Schäden führen, und genau hier unterscheidet sich ein BMS, das funktioniert, von einem, das nachweisbar sicher ist.</p>
<p>In der Pkw-Entwicklung ist diese Denkweise seit Jahren Standard: Jede Schutzfunktion wird mit ihren möglichen Fehlern analysiert, die Diagnose dagegen wird bewertet, und das Ergebnis ist bis in den Code nachvollziehbar. Für stationäre Speicher bietet IEC 61508 den Rahmen, um dieselbe Sorgfalt nachzuweisen.</p>

<h2>Welche Normen bis zur Harmonisierung helfen</h2>
<p>Harmonisierte Normen begründen die Konformitätsvermutung. Die EU-Kommission hat dafür einen Normungsauftrag erteilt (M/579). Für Artikel 12 ist bislang keine harmonisierte Norm im Amtsblatt gelistet, Sie müssen den Stand der Technik also selbst begründen. In der Praxis stützen sich Hersteller auf etablierte Normen:</p>
<table>
<tr><th>Norm</th><th>Worum es geht</th></tr>
<tr><td>IEC 62619</td><td>Sicherheit von Lithium-Zellen und -Batterien für industrielle Anwendungen, einschließlich Anforderungen an das Batteriesystem und sein BMS</td></tr>
<tr><td>IEC 62933-5-2</td><td>Sicherheitsanforderungen an netzgekoppelte elektrochemische Energiespeichersysteme</td></tr>
<tr><td>VDE-AR-E 2510-50</td><td>Sicherheit stationärer Lithium-Speicher, vor allem im Heimspeicherbereich</td></tr>
<tr><td>UL 9540 / UL 9540A</td><td>Systemsicherheit von Energiespeichern beziehungsweise Prüfmethode für die thermische Ausbreitung; häufig von Versicherern und Projektfinanzierern angefragt</td></tr>
<tr><td>UL 1973</td><td>Batterien für stationäre Anwendungen und Hilfsantriebe, etwa in Schienenfahrzeugen</td></tr>
<tr><td>IEC 61508</td><td>Funktionale Sicherheit elektronischer Steuerungen; Grundlage für sicherheitsrelevante BMS-Software</td></tr>
</table>

<h2>Zweites Leben braucht neue Unterlagen</h2>
<p>Wer Fahrzeugbatterien als stationären Speicher weiterverwendet, muss die technischen Unterlagen überarbeiten. Das betrifft vor allem die Schutzfunktionen: Grenzwerte, Diagnose und Zustandsschätzung, die für das Fahrzeug ausgelegt wurden, passen selten unverändert zu einem neuen Lastprofil.</p>

<h2>Checkliste für Integratoren</h2>
<ol>
<li>Klären Sie, wer das System in Verkehr bringt. Wer Module zu einem Speicher zusammenbaut, ist häufig selbst Hersteller.</li>
<li>Prüfen Sie für jeden der elf Parameter, ob eine Gefährdung besteht, und dokumentieren Sie die Begründung.</li>
<li>Fordern Sie vom BMS-Lieferanten mehr als ein Datenblatt: Sicherheitshandbuch, Fehleranalysen, Diagnoseabdeckung und Grenzen des Einsatzbereichs.</li>
<li>Bewerten Sie Risiken außerhalb von Anhang V, etwa Kommunikationsausfall oder fehlerhafte Software-Updates.</li>
<li>Legen Sie fest, welche Normen Sie als Stand der Technik heranziehen, und begründen Sie die Wahl.</li>
<li>Planen Sie die Überarbeitung der Unterlagen bei Änderungen, Updates und Wiederverwendung ein.</li>
</ol>
''',
 [("Gilt Artikel 12 der Batterieverordnung schon?", "Ja. Für stationäre Batterie-Energiespeichersysteme müssen seit dem 18. August 2024 technische Unterlagen vorliegen, die die Sicherheit belegen, unter anderem durch Prüfungen zu den Sicherheitsparametern aus Anhang V."),
  ("Welche Sicherheitsparameter nennt Anhang V?", "Thermischer Schock und Temperaturwechsel, Schutz vor externem Kurzschluss, Überladeschutz, Tiefentladeschutz, Übertemperaturschutz, Schutz vor thermischer Ausbreitung, mechanische Beschädigung, interner Kurzschluss, thermischer Missbrauch, Feuer und Gasemission."),
  ("Reicht das Prüfzertifikat des Zell- oder BMS-Lieferanten?", "In der Regel nicht allein. Die Nachweispflicht gilt für das System, das Sie in Verkehr bringen. Prüfberichte der Lieferanten sind wertvolle Bausteine, ersetzen aber nicht die Bewertung des Gesamtsystems."),
  ("Gilt Artikel 12 auch für Heimspeicher?", "Artikel 12 gilt für stationäre Batterie-Energiespeichersysteme. Ob und wie ein konkretes Produkt erfasst ist, sollte im Einzelfall anhand der Begriffsbestimmungen der Verordnung geprüft werden.")],
 "Batteriespeicher-Sicherheit")

# ---------- 2: Maschinenverordnung ----------
article(
 "maschinenverordnung-2027-batteriesystem",
 "Maschinenverordnung 2027: Was elektrische Maschinen beim Batteriesystem beachten müssen | dolavolt",
 "Ab 20. Januar 2027 gilt die Maschinenverordnung (EU) 2023/1230. Was sie für Software, Sicherheitsfunktionen und das Batteriesystem elektrischer Bau- und Landmaschinen sowie Flurförderzeuge bedeutet.",
 "Maschinenverordnung 2027: Was sie für das Batteriesystem elektrischer Maschinen bedeutet",
 "Am 20. Januar 2027 löst die Maschinenverordnung (EU) 2023/1230 die bisherige Maschinenrichtlinie ab. Für Hersteller elektrischer Bau- und Landmaschinen sowie Flurförderzeuge rückt damit ein Bauteil in den Fokus, das meist zugekauft wird: das Batteriesystem mit seiner Software.",
 '''
<div class="box"><p><strong>Kurz gesagt:</strong> Ab dem 20. Januar 2027 gilt die Maschinenverordnung verbindlich. Sie erfasst ausdrücklich Software mit Sicherheitsfunktion, verlangt Schutz gegen Korrumpierung, die Protokollierung von Eingriffen und Softwareversionen und eine Risikobeurteilung über den gesamten Lebenszyklus, die auch Software-Updates einschließt. Übernimmt das BMS Sicherheitsfunktionen, gehört es in die Risikobeurteilung der Maschine. Die Verantwortung dafür trägt, wie schon bisher, der Maschinenhersteller, auch wenn das Batteriesystem zugekauft ist.</p></div>

<h2>Was sich gegenüber der Maschinenrichtlinie ändert</h2>
<p>Die Maschinenrichtlinie stammt aus einer Zeit, in der Sicherheit vor allem Mechanik und Schaltungstechnik bedeutete. Die Verordnung trägt dem Umstand Rechnung, dass heute Software über Sicherheit entscheidet:</p>
<ul>
<li><strong>Software als Sicherheitsbauteil:</strong> Auch reine Software kann ein Sicherheitsbauteil sein, wenn sie eine Sicherheitsfunktion erfüllt.</li>
<li><strong>Schutz gegen Korrumpierung:</strong> Software, Firmware und Schnittstellen mit Sicherheitsbezug müssen gegen unbeabsichtigte und böswillige Veränderung geschützt sein. Dieser Schutz fließt in die Konformitätsbewertung der Maschine ein; welche Pflichten konkret gelten, hängt von Produkt, Sicherheitsfunktion und Konformitätsbewertungsverfahren ab.</li>
<li><strong>Nachvollziehbarkeit:</strong> Eingriffe und Softwareversionen sicherheitsrelevanter Software müssen protokolliert werden. Die Risikobeurteilung umfasst den gesamten Lebenszyklus, also auch Änderungen durch Updates.</li>
<li><strong>Lernende Systeme:</strong> Sicherheitsbauteile und Maschinen, deren Sicherheitsfunktionen auf selbstlernendem Verhalten beruhen, brauchen eine Konformitätsbewertung durch eine benannte Stelle.</li>
</ul>

<h2>Warum das Batteriesystem dazugehört</h2>
<p>Das BMS einer elektrischen Maschine trennt die Batterie bei Überstrom, Überspannung oder Übertemperatur vom Antrieb. Versagt eine dieser Funktionen, ist das kein reines Batterieproblem mehr, sondern ein Risiko für Bediener und Umgebung. Damit gehört das BMS in die Risikobeurteilung der Maschine, und seine Schutzfunktionen müssen dieselben Anforderungen erfüllen wie jede andere Sicherheitsfunktion.</p>
<p>Ein Beispiel für die Größenordnung: Monolithic Power Systems hat ein Sicherheitskonzept für ein BMS nach ISO 13849 veröffentlicht, in dem zehn Schutzfunktionen von Über- und Unterspannung bis Übertemperatur jeweils mit Performance Level c bewertet sind. Welcher Level für Ihre Maschine nötig ist, ergibt sich allerdings aus Ihrer Risikobeurteilung, nicht aus dem Datenblatt der Batterie.</p>

<h2>Die passenden Normen</h2>
<table>
<tr><th>Norm</th><th>Anwendungsbereich</th></tr>
<tr><td>ISO 13849</td><td>Sicherheitsbezogene Teile von Steuerungen, allgemein für Maschinen; Bewertung über Performance Level</td></tr>
<tr><td>ISO 25119</td><td>Sicherheitsbezogene Teile von Steuerungen an Traktoren und Maschinen der Land- und Forstwirtschaft</td></tr>
<tr><td>ISO 19014</td><td>Funktionale Sicherheit von Erdbaumaschinen</td></tr>
<tr><td>IEC 62619</td><td>Sicherheit von Lithium-Industriebatterien einschließlich BMS</td></tr>
<tr><td>IEC 61508</td><td>Grundnorm der funktionalen Sicherheit, auf die sich die Branchennormen stützen</td></tr>
</table>

<h2>Die Zulieferfalle</h2>
<p>Die meisten Maschinenhersteller kaufen das Batteriesystem zu. Die Pflichten aus der Maschinenverordnung, einschließlich Risikobeurteilung und Konformitätsbewertung, liegen in erster Linie beim Hersteller der Maschine. Ein in die Maschine eingebautes BMS ist nicht automatisch ein eigenständiges Sicherheitsbauteil mit eigener CE-Kennzeichnung. Umgekehrt kann ein Batteriesystem oder BMS mit Sicherheitsfunktion, das separat in Verkehr gebracht wird, unter Umständen selbst als Sicherheitsbauteil gelten. Ob und welche Herstellerpflichten den Lieferanten dann treffen, hängt von der Produktrolle und dem Konformitätsbewertungsverfahren ab und sollte im Einzelfall geprüft werden. Wer vom Batterielieferanten nur ein Datenblatt bekommt, kann die Schutzfunktionen weder bewerten noch in die eigene Sicherheitsbetrachtung übernehmen. Diese Unterlagen sollten Sie anfordern:</p>
<ol>
<li>ein Sicherheitshandbuch mit allen Sicherheitsfunktionen, ihren Reaktionszeiten und dem sicheren Zustand,</li>
<li>die erreichte Sicherheitsintegrität je Funktion (Performance Level oder SIL) mit Begründung,</li>
<li>Fehleranalysen und Diagnoseabdeckung,</li>
<li>eine Beschreibung des Update-Prozesses und des Schutzes gegen Korrumpierung,</li>
<li>die Grenzen des Einsatzbereichs: Temperatur, Strom, Lastprofil, Einbaulage.</li>
</ol>
<p>Fehlen diese Unterlagen, gibt es zwei Wege: Der Lieferant liefert nach, oder Sie bewerten das System selbst. Beides kostet Zeit, und der 20. Januar 2027 lässt nicht mehr viel davon.</p>
''',
 [("Ab wann gilt die neue Maschinenverordnung?", "Die Verordnung (EU) 2023/1230 gilt ab dem 20. Januar 2027 verbindlich und ersetzt die Maschinenrichtlinie 2006/42/EG."),
  ("Fällt das BMS unter die Maschinenverordnung?", "Übernimmt das BMS Sicherheitsfunktionen der Maschine, etwa das Abschalten bei Überstrom oder Übertemperatur, gehört es zur Sicherheitsbetrachtung der Maschine. Die Verordnung erfasst ausdrücklich auch Software mit Sicherheitsfunktion."),
  ("Wer ist verantwortlich, wenn die Batterie zugekauft ist?", "Der Hersteller der Maschine trägt, wie schon unter der Maschinenrichtlinie, die Verantwortung für die Konformität der gesamten Maschine. Er braucht dafür ausreichende Unterlagen vom Batterielieferanten oder muss das System selbst bewerten."),
  ("Welche Norm gilt für Sicherheitsfunktionen in Bau- und Landmaschinen?", "Allgemein ISO 13849, für Land- und Forstmaschinen ISO 25119 und für Erdbaumaschinen ISO 19014. Für die Batterie selbst ist IEC 62619 maßgeblich.")],
 "Maschinenverordnung")

# ---------- 3: Batteriepass ----------
article(
 "eu-batteriepass-2027",
 "EU-Batteriepass 2027 für Speicher-, Industrie- und EV-Batterien: Pflichten und Fristen | dolavolt",
 "Ab 18. Februar 2027 Pflicht für EV-Batterien, Industriebatterien über 2 kWh und Batteriespeicher: Wer den Batteriepass ausstellen muss, welche Daten aus dem BMS kommen und wie Sie sich vorbereiten.",
 "EU-Batteriepass 2027: Was das BMS jetzt liefern muss",
 "Am 18. Februar 2027 wird der digitale Batteriepass Pflicht, nicht nur für Elektroautos, sondern auch für Batteriespeicher, Staplerbatterien und jede andere Industriebatterie über 2 kWh. Viele Unternehmen behandeln ihn als IT-Projekt. Ein Teil der wichtigsten Daten entsteht aber im Batteriemanagementsystem.",
 '''
<div class="box"><p><strong>Kurz gesagt:</strong> Ab dem 18. Februar 2027 brauchen EV-Batterien, Batterien für leichte Verkehrsmittel und Industriebatterien über 2&nbsp;kWh, die in der EU in Verkehr gebracht werden, einen digitalen Batteriepass, erreichbar über einen QR-Code. Ohne Pass dürfen sie nicht in Verkehr gebracht werden. Rechtsgrundlage ist Artikel 77 der Batterieverordnung (EU) 2023/1542.</p></div>

<h2>Die wichtigsten Termine</h2>
<table>
<tr><th>Datum</th><th>Was gilt</th></tr>
<tr><td>18.02.2024</td><td>Die Batterieverordnung gilt, ihre Pflichten treten schrittweise in Kraft</td></tr>
<tr><td>18.08.2024</td><td>Sicherheitsnachweis für stationäre Batteriespeicher nach Artikel 12</td></tr>
<tr><td>ab 18.02.2025</td><td>Erklärung zum CO₂-Fußabdruck für EV-Batterien; Geltung hängt vom Inkrafttreten der delegierten Rechtsakte zur Berechnungsmethode ab; aktuellen Stand prüfen</td></tr>
<tr><td>20.07.2026</td><td>Das EU-Register für Batteriepässe wurde geöffnet</td></tr>
<tr><td><strong>18.02.2027</strong></td><td><strong>Batteriepass-Pflicht</strong>, QR-Code, Anforderungen an Entnehmbarkeit und Austauschbarkeit</td></tr>
<tr><td>18.08.2027</td><td>Sorgfaltspflichten in der Lieferkette (verschoben durch Verordnung (EU) 2025/1561)</td></tr>
</table>

<h2>Wer den Pass ausstellen muss</h2>
<p>Verantwortlich ist, wer die Batterie in der EU in Verkehr bringt, in der Regel also, wer sie fertigstellt. Für Speicherintegratoren heißt das: Wer Module in der EU zu einem System zusammenbaut, ist häufig selbst Hersteller im Sinne der Verordnung. Wer Arbeit an Dienstleister vergibt, gibt damit die Verantwortung nicht ab. Ein BMS-Zulieferer ist dagegen nicht automatisch selbst passpflichtig; er liefert aber die Daten, auf denen die dynamischen Angaben beruhen.</p>

<h2>Warum der Batteriepass ein BMS-Thema ist</h2>
<p>Der Pass ist kein einmal ausgefülltes Datenblatt, sondern ein Datensatz, der die Batterie über ihr ganzes Leben begleitet. Ein Teil der Angaben ist statisch: Hersteller, Typ, Chemie. Ein anderer Teil ist dynamisch, allen voran Leistung und Haltbarkeit. Angaben zum Gesundheitszustand (State of Health) betreffen Batterien mit BMS und werden je nach Batteriekategorie und Zugriffsberechtigung bereitgestellt, nicht pauschal öffentlich. Damit wird die Qualität der SoH-Schätzung im Steuergerät zu einer Größe, die nach außen sichtbar wird.</p>
<ul>
<li><strong>Nachvollziehbare Zustandsschätzung:</strong> Kapazitäts- und Innenwiderstandsschätzung müssen dokumentiert, validiert und für die eingesetzte Zellchemie geeignet sein.</li>
<li><strong>Sicherer Datenpfad:</strong> Die Werte müssen zuverlässig und manipulationssicher vom BMS ins Backend gelangen.</li>
<li><strong>Rückverfolgbarkeit:</strong> Von der Zellcharge über das Modul bis zum System muss die Zuordnung stimmen, auch nach Reparatur oder Wiederaufarbeitung.</li>
<li><strong>Update-Fähigkeit:</strong> Verbesserte Algorithmen müssen kontrolliert ins Feld kommen, ohne die Sicherheitsfunktionen zu gefährden.</li>
</ul>

<h2>Was das für Speicher und Industriebatterien heißt</h2>
<p>Viele stationäre Speicher und Staplerbatterien nutzen LFP-Zellen. Deren Spannungskennlinie ist über weite Bereiche fast flach, was die Zustandsschätzung deutlich schwieriger macht als bei NMC-Zellen. Ein SoH-Wert, auf den sich Berechtigte etwa beim Weiterverkauf oder bei der Wiederaufarbeitung stützen, muss trotzdem belastbar sein.</p>
<p>Hinzu kommt das zweite Leben: Für Batterien, die für die Wiederverwendung vorbereitet, umgenutzt oder wiederaufgearbeitet werden, sieht die Batterieverordnung einen neuen, mit dem ursprünglichen verknüpften Pass vor. Wer dafür verantwortlich ist und welche Angaben fortgeschrieben werden, richtet sich nach den konkreten Regeln der Verordnung und sollte im Einzelfall geprüft werden.</p>

<h2>Klein anfangen, groß planen</h2>
<p>Zum Start liegt der Schwerpunkt auf Identifikation, Typ, Modell und technischen Kerndaten. CO₂-Fußabdruck, Rezyklatanteile und Angaben zu Sorgfaltspflichten kommen schrittweise hinzu, weitere delegierte Rechtsakte sind zu erwarten. Legen Sie Datenmodell und Schnittstellen deshalb so an, dass Sie künftige Felder ohne Neuentwicklung ergänzen können.</p>

<h2>Checkliste</h2>
<ol>
<li>Klären Sie, wer die Batterie in Verkehr bringt.</li>
<li>Ordnen Sie jede Pflichtangabe einer Quelle zu: Fertigung, BMS oder Lieferant.</li>
<li>Bewerten Sie Ihre SoH-Schätzung: Genauigkeit, Validierung, Eignung für die Zellchemie.</li>
<li>Sichern Sie den Datenpfad vom BMS bis zur Pass-Plattform ab.</li>
<li>Legen Sie fest, wie Änderungen und Updates im Pass nachgeführt werden.</li>
<li>Bereiten Sie die Registrierung im EU-Register vor.</li>
</ol>
''',
 [("Ab wann gilt der EU-Batteriepass?", "Ab dem 18. Februar 2027 für EV-Batterien, Batterien für leichte Verkehrsmittel und Industriebatterien über 2 kWh, die in der EU in Verkehr gebracht werden."),
  ("Brauchen Batteriespeicher einen Batteriepass?", "Ja, sofern es sich um Industriebatterien mit mehr als 2 kWh handelt, was bei stationären Speichern üblicherweise der Fall ist."),
  ("Was hat das BMS mit dem Batteriepass zu tun?", "Dynamische Angaben wie der Gesundheitszustand werden im Batteriemanagementsystem berechnet. Ihre Qualität und ein sicherer Datenpfad ins Backend sind Voraussetzung für einen belastbaren Pass."),
  ("Braucht eine umgenutzte Fahrzeugbatterie einen neuen Pass?", "Ja. Wird eine Batterie wiederaufgearbeitet oder für einen anderen Zweck umgenutzt, braucht sie einen neuen Batteriepass.")],
 "Batteriepass")

# ---------- 4: KI in der funktionalen Sicherheit ----------
article(
 "ki-funktionale-sicherheit",
 "KI in der sicherheitskritischen Entwicklung: Was ISO 26262 und IEC 61508 zulassen | dolavolt",
 "Dürfen KI-Werkzeuge Anforderungen, Tests und Code für sicherheitskritische Systeme erzeugen? Was ISO 26262 und IEC 61508 zur Werkzeugqualifizierung verlangen und welche Regeln sich in der Praxis bewähren.",
 "KI in der sicherheitskritischen Entwicklung: Was ISO 26262 und IEC 61508 zulassen",
 "KI-Werkzeuge schreiben Anforderungen, Testfälle und Code in Minuten. In der funktionalen Sicherheit lautet die Frage deshalb nicht mehr, ob Teams KI nutzen, sondern wie, ohne den Sicherheitsnachweis zu gefährden.",
 '''
<div class="box"><p><strong>Kurz gesagt:</strong> ISO 26262 und IEC 61508 kennen keine Sonderregeln für KI. KI-Werkzeuge werden wie jedes andere Software-Werkzeug behandelt, und ihre Ergebnisse gelten nicht automatisch als Sicherheitsnachweis. Werkzeuge, deren Fehler sich auf das Produkt oder den Nachweis auswirken können, müssen nach ISO 26262-8 Abschnitt 11 oder IEC 61508-3 bewertet und gegebenenfalls qualifiziert werden. Bewährt hat sich außerdem die Regel, dass ein Mensch Autor und verantwortlich für jedes Ergebnis bleibt; wörtlich vorgeschrieben ist das in den Normen nicht.</p></div>

<h2>Wo KI wirklich hilft</h2>
<p>Den größten Nutzen bringt KI auf der linken Seite des V-Modells, wo viel Text entsteht und Vollständigkeit zählt:</p>
<ul>
<li>erste Entwürfe von Anforderungen und Sicherheitsanforderungen,</li>
<li>Ableitung von Testfällen, einschließlich Grenzwert- und Fehlerfällen,</li>
<li>Prüfung der Rückverfolgbarkeit zwischen Anforderungen, Architektur, Code und Tests,</li>
<li>Pflege von Dokumentation, die sonst veraltet,</li>
<li>Code-Review als zusätzliches Augenpaar.</li>
</ul>

<h2>Wo das Risiko liegt</h2>
<p>Auf der rechten Seite des V-Modells geht es um Nachweise: Verifikation, Integration und Sicherheitsargumentation. Ein Sprachmodell, das falsch liegt, liegt überzeugend falsch. Wer seine Ergebnisse ungeprüft in die Nachweiskette übernimmt, riskiert Befunde im Assessment und im schlimmsten Fall ein Produkt, dessen Sicherheit nur behauptet ist.</p>

<h2>Was die Normen verlangen</h2>
<h3>ISO 26262-8, Abschnitt 11</h3>
<p>Für jedes Software-Werkzeug wird ein Tool Confidence Level (TCL) bestimmt. Es ergibt sich aus zwei Fragen: Kann ein Fehler des Werkzeugs einen Fehler ins Produkt bringen oder einen Fehler unentdeckt lassen (Tool Impact)? Und wie wahrscheinlich ist es, dass ein solcher Fehler verhindert oder entdeckt wird (Tool Error Detection)? Bei TCL1 sind keine Qualifizierungsmaßnahmen erforderlich; für TCL2 und TCL3 nennt die Norm, abhängig vom ASIL, Methoden zur Werkzeugqualifizierung.</p>
<h3>IEC 61508-3</h3>
<p>Offline-Werkzeuge werden in drei Klassen eingeteilt: T1 erzeugt keine Ausgaben, die direkt oder indirekt zum ausführbaren Code beitragen; T2 unterstützt Test oder Verifikation und kann Fehler übersehen, aber nicht selbst erzeugen; T3 erzeugt Ausgaben, die direkt oder indirekt zum ausführbaren Code des sicherheitsbezogenen Systems beitragen. Je höher die Klasse, desto mehr Nachweis wird für das Werkzeug verlangt.</p>
<h3>Was daraus folgt</h3>
<p>Ein Sprachmodell zu qualifizieren, ist praktisch kaum möglich, zumal sich Modelle laufend ändern. Ein möglicher Weg führt über die Fehlererkennung: Ist die nachfolgende Verifikation so gestaltet, dass Fehler im KI-Ergebnis mit hoher Wahrscheinlichkeit gefunden werden, kann sich daraus ein niedrigeres Tool Confidence Level ergeben. Ob das trägt, muss für den konkreten Verwendungszweck begründet und dokumentiert werden. KI-Ergebnisse werden dann wie Arbeit eines neuen Kollegen behandelt: hilfreich, aber nie ungeprüft.</p>

<h2>Fünf Regeln, die sich bewähren</h2>
<ol>
<li><strong>Herkunft protokollieren:</strong> Prompt, Modell und Version, Eingaben, Ausgabe und Prüfer werden zum Zeitpunkt der Erzeugung festgehalten.</li>
<li><strong>Ein Mensch ist Autor:</strong> Jedes Artefakt hat einen verantwortlichen Ingenieur, der es geprüft hat.</li>
<li><strong>Modellwechsel ist eine Konfigurationsänderung:</strong> Eine neue Modellversion wird behandelt wie ein neues Werkzeug.</li>
<li><strong>Keine KI als alleinige Verifikation:</strong> KI darf zusätzlich prüfen, aber nicht die einzige Prüfung sein, solange das Werkzeug dafür nicht qualifiziert ist.</li>
<li><strong>Vertrauliche Daten schützen:</strong> Nur freigegebene Werkzeuge mit geklärter Datenverarbeitung kommen an Kundenunterlagen.</li>
</ol>
<p>Assessoren nach Automotive SPICE dürften künftig genau danach fragen: wer oder was ein Artefakt erzeugt hat, was seine Richtigkeit belegt und wie es rückverfolgbar ist. Wer diese Fragen beantworten kann, gewinnt mit KI Zeit, ohne Nachweisqualität zu verlieren.</p>
''',
 [("Darf KI-generierter Code in sicherheitskritischer Software verwendet werden?", "Ja, wenn er wie jeder andere Code entwickelt, geprüft und verifiziert wird. Entscheidend ist, dass Fehler des Werkzeugs durch die nachfolgende Verifikation sicher entdeckt werden und ein Mensch für das Ergebnis verantwortlich ist."),
  ("Muss ein Sprachmodell nach ISO 26262 qualifiziert werden?", "Nur wenn sich aus Tool Impact und Tool Error Detection ein Tool Confidence Level von TCL2 oder TCL3 ergibt. Über eine wirksame nachgelagerte Fehlererkennung lässt sich unter Umständen ein niedrigeres TCL begründen; das muss im Einzelfall nachgewiesen werden."),
  ("Was ist ein Tool Confidence Level?", "Eine Einstufung nach ISO 26262-8, die angibt, wie viel Vertrauen in ein Software-Werkzeug nötig ist. Sie ergibt sich aus der möglichen Auswirkung eines Werkzeugfehlers und der Wahrscheinlichkeit, ihn zu erkennen.")],
 "KI%20und%20funktionale%20Sicherheit")

# ---------- 5: Cloud-BMS ----------
article(
 "cloud-bms-digitaler-zwilling",
 "Cloud-BMS & digitaler Zwilling für Batteriespeicher und Flotten | dolavolt",
 "Wie Cloud-BMS und digitale Batterie-Zwillinge Alterung vorhersagen, Garantierisiken senken und Second Life ermöglichen – für Speicherparks, Maschinen- und Fahrzeugflotten.",
 "Cloud-BMS und digitaler Zwilling: Wie Betriebsdaten Batterien wertvoller machen",
 "Ein BMS sieht eine Batterie. Ein Cloud-BMS sieht Hunderte, ob in einem Speicherpark, einer Maschinenflotte oder einer Fahrzeugflotte. Daraus können bessere Alterungsmodelle, belastbarere Garantieaussagen und eine fundiertere Restwertbewertung entstehen, vorausgesetzt, Batterie und Backend sind sauber verbunden.",
 '''
<h2>Was ist ein Cloud-BMS?</h2>
<p>Ein Cloud-BMS ergänzt das Batteriemanagement vor Ort um eine Backend-Komponente. Das Steuergerät bleibt für Echtzeit und Sicherheit zuständig, in der Cloud laufen rechenintensive Modelle, die aus den Daten vieler Batterien lernen. Die Ergebnisse fließen als verbesserte Parameter oder Software-Update zurück.</p>

<h2>Der digitale Zwilling der Batterie</h2>
<p>Ein digitaler Zwilling ist ein laufend aktualisiertes Modell einer konkreten Batterie: Nutzungshistorie, Temperaturprofil, Ladeverhalten, geschätzter Gesundheitszustand. Er beantwortet Fragen wie: Wie viel Kapazität hat dieser Speicher in fünf Jahren noch? Hält die Garantiezusage? Lohnt sich ein zweites Leben?</p>

<h2>Wofür sich das lohnt</h2>
<ul>
<li><strong>Batteriepass:</strong> belastbare SoH-Werte über das ganze Batterieleben.</li>
<li><strong>Garantie und Restwert:</strong> Bessere Prognosen können Rückstellungen senken und gebrauchte Batterien bewertbar machen.</li>
<li><strong>Frühwarnung:</strong> Auffällige Zellen oder Module werden erkannt, bevor sie ausfallen.</li>
<li><strong>Betrieb von Speichern:</strong> Wer die Alterung kennt, kann Fahrpläne und Vermarktung so planen, dass die Batterie die zugesagte Lebensdauer erreicht.</li>
<li><strong>Bessere Algorithmen:</strong> Zustandsschätzung wird mit echten Felddaten kalibriert, gerade bei LFP-Zellen ein großer Gewinn.</li>
</ul>

<h2>Was es vor Ort dafür braucht</h2>
<ol>
<li><strong>Die richtigen Daten:</strong> nicht alles senden, sondern sinnvoll verdichten, etwa als Histogramme, Ereignisse und Kennwerte.</li>
<li><strong>Sichere Übertragung:</strong> Authentisierung und Integritätsschutz vom BMS bis ins Backend.</li>
<li><strong>Klare Rollenteilung:</strong> Sicherheitsfunktionen dürfen nie von der Verbindung abhängen.</li>
<li><strong>Kontrollierte Rückführung:</strong> Was die Cloud lernt, kommt geprüft und rückverfolgbar zurück ins System.</li>
</ol>

<h2>Unser Ansatz</h2>
<p>Wir denken Cloud-BMS vom Steuergerät aus: Welche Signale sind belastbar, wie werden sie verdichtet, wie werden Modelle validiert und wie kommt das Ergebnis sicher zurück? So entsteht ein Datenkreislauf, der Sicherheit, Batteriepass und Geschäftsmodell gleichzeitig bedient.</p>
''',
 [("Ersetzt ein Cloud-BMS das BMS vor Ort?", "Nein. Schutzfunktionen und Echtzeitregelung bleiben im System. Die Cloud ergänzt Analysen, Prognosen und Kalibrierung."),
  ("Welche Daten braucht ein digitaler Batterie-Zwilling?", "Typischerweise Strom-, Spannungs- und Temperaturverläufe in verdichteter Form, Lade- und Nutzungsereignisse sowie die geschätzten Zustandsgrößen des BMS."),
  ("Hilft ein Cloud-BMS beim Batteriepass?", "Ja. Es liefert über das ganze Batterieleben nachvollziehbare Zustandsdaten wie den Gesundheitszustand.")],
 "Cloud-BMS")


# ---------- 6: Euro 7 und GB 38031 ----------
article(
 "euro-7-gb-38031-bms",
 "Euro 7 und GB 38031-2025: Was neue Vorschriften für das BMS bedeuten | dolavolt",
 "Euro 7 legt Mindestanforderungen an die Haltbarkeit von Antriebsbatterien fest, GB 38031-2025 verschärft in China seit 1.7.2026 die Anforderungen an die thermische Sicherheit. Was das für SOCE-Ermittlung, Überwachung thermischer Ereignisse und Fehlerreaktion im BMS bedeutet.",
 "Euro 7 und GB 38031: Was neue Vorschriften für das BMS bedeuten",
 "Zwei Regelwerke rücken die Haltbarkeit und die Sicherheit von Traktionsbatterien stärker in den Fokus. Die Euro-7-Verordnung legt Mindestanforderungen an die Haltbarkeit von Antriebsbatterien fest. Die chinesische Sicherheitsnorm GB 38031-2025 konkretisiert unter anderem die Anforderungen an die thermische Sicherheit. Für BMS-Entwickler ergeben sich daraus Aufgaben bei Zustandsschätzung, Überwachung thermischer Ereignisse, Fehlerreaktion und Validierung.",
 '''
<div class="box"><p><strong>Kurz gesagt:</strong> Für Elektro- und Plug-in-Hybrid-Pkw der Klasse M1 sieht Euro 7 mindestens 80&nbsp;% der zertifizierten Energie bis fünf Jahre oder 100.000&nbsp;km und mindestens 72&nbsp;% bis acht Jahre oder 160.000&nbsp;km vor, für leichte Nutzfahrzeuge (N1) 75&nbsp;% beziehungsweise 67&nbsp;%. GB 38031-2025 ist seit dem 1.7.2026 in China in Kraft: In der vorgeschriebenen thermischen Propagationsprüfung darf das Batteriesystem weder Feuer fangen noch explodieren, und es muss rechtzeitig ein Warnsignal ausgegeben werden.</p></div>

<h2>Euro 7: Batteriehaltbarkeit wird typgenehmigungsrelevant</h2>
<p>Die Euro-7-Verordnung (EU) 2024/1257 führt Mindestanforderungen an die Haltbarkeit von Traktionsbatterien in Elektro- und Plug-in-Hybridfahrzeugen ein. Bezugsgröße ist der State of Certified Energy (SOCE): der Anteil der bei der Typgenehmigung zertifizierten Batterieenergie, der zu einem Zeitpunkt noch verfügbar ist. Die Prüfmethoden und Anforderungen konkretisiert die Durchführungsverordnung (EU) 2026/1764.</p>
<table>
<tr><th>Fahrzeugklasse</th><th>5 Jahre oder 100.000 km</th><th>8 Jahre oder 160.000 km</th></tr>
<tr><td>Pkw (M1)</td><td>80 %</td><td>72 %</td></tr>
<tr><td>Leichte Nutzfahrzeuge (N1)</td><td>75 %</td><td>67 %</td></tr>
</table>
<p>Maßgeblich ist jeweils die Grenze, die zuerst erreicht wird. Euro 7 gilt ab dem 29.11.2026 für neue Typen von Pkw und leichten Nutzfahrzeugen und ab dem 29.11.2027 für alle neuen Fahrzeuge dieser Klassen. Für schwere Nutzfahrzeuge und Busse sind noch keine Werte festgelegt. Euro 7 sieht außerdem einen Umweltpass des Fahrzeugs vor; welche Batteriedaten er im Einzelnen enthält, ergibt sich aus den Durchführungsbestimmungen.</p>
<h3>Was das für die BMS-Entwicklung bedeutet</h3>
<p>Die folgenden Punkte sind fachliche Schlussfolgerungen, keine wörtlichen Anforderungen der Verordnung.</p>
<ul>
<li><strong>SOCE ist nicht gleich SOH.</strong> SOCE ist eine regulatorisch definierte, typgenehmigungsbezogene Größe. Ein beliebiger interner SOH-Wert des BMS genügt dafür nicht. Die Ermittlung des SOCE muss zur vorgeschriebenen Mess- und Bewertungsmethode passen und nachvollziehbar validiert sein.</li>
<li><strong>Auslesbarkeit.</strong> Die Verordnung sieht vor, dass Daten zur Batteriehaltbarkeit über die OBD-Schnittstelle bereitgestellt werden. Datenpfad und Datenqualität müssen dafür ausgelegt sein.</li>
<li><strong>Langzeitverhalten.</strong> Sensoroffsets, Temperaturfehler und seltene Vollzyklen wirken über Jahre. Bei LFP-Zellen mit flacher Kennlinie ist der Einfluss besonders groß.</li>
</ul>

<h2>GB 38031-2025: kein Feuer, keine Explosion in der Propagationsprüfung</h2>
<p>GB 38031-2025 ersetzt GB 38031-2020 und ist seit dem 1.7.2026 in Kraft. Für die Umstellung bestehender Zertifizierungen nennt das China Quality Certification Centre (CQC) den 1.7.2027 sowie weitere Stufen für Aussetzung und Entzug von Zertifikaten. Das ist ein Zertifizierungsübergang, keine allgemeine Frist für alle Fahrzeugtypen; maßgeblich sind die jeweilige Zertifizierungsregel und das konkrete Verfahren.</p>
<p>Kern der Neufassung: In der vorgeschriebenen thermischen Propagationsprüfung darf das Batteriesystem weder Feuer fangen noch explodieren. Ein thermisches Warnsignal muss innerhalb der vorgegebenen Frist ausgegeben werden, und in einem festgelegten Zeitfenster darf kein Rauch in den Fahrzeuginnenraum gelangen; die Norm unterscheidet dabei zwischen Prüfungen auf System- und auf Fahrzeugebene. Neu sind außerdem ein Unterboden-Aufpralltest und ein externer Kurzschlusstest nach 300 Schnellladezyklen, bei dem ebenfalls weder Feuer noch Explosion auftreten dürfen.</p>
<h3>Was das für die BMS-Entwicklung bedeutet</h3>
<p>Die Norm stellt Anforderungen an das Batteriesystem, nicht an eine bestimmte BMS-Software. Erfüllt werden sie über das Zusammenspiel von Zellchemie, thermischen Barrieren, Entgasung und mechanischer Auslegung. Das BMS trägt Detektion, Warnung und definierte Steuerungsreaktionen bei. Die folgenden Punkte sind Engineering-Empfehlungen, keine ausdrücklichen Normpflichten.</p>
<ul>
<li><strong>Detektion.</strong> Spannungseinbrüche und Temperaturgradienten zuverlässig und ohne Fehlalarme auswerten; je nach Systemkonzept auch Gas- oder Drucksensorik.</li>
<li><strong>Reaktion.</strong> Die Systemreaktion auf ein erkanntes Ereignis, vom Öffnen der Schütze bis zur Warnung, für alle Betriebszustände definieren und absichern, auch beim Laden und im Stand.</li>
<li><strong>Schnellladen.</strong> Der Test nach 300 Schnellladezyklen macht die Schnellladestrategie und ihre Grenzwerte zu einem sicherheitsrelevanten Thema.</li>
</ul>
<p>Auch wer nicht für den chinesischen Markt entwickelt, sollte die Norm kennen: Sie setzt einen Maßstab, an dem sich Kunden und Wettbewerber orientieren.</p>

<h2>Checkliste</h2>
<ol>
<li>SOCE-Ermittlung gegen die Euro-7-Methodik prüfen: Herleitung, Validierung, Langzeitverhalten.</li>
<li>Bereitstellung der Haltbarkeitsdaten über OBD und den Weg in den Umweltpass klären.</li>
<li>Detektionskette für thermische Ereignisse analysieren: Signale, Schwellen, Fehlalarmrate.</li>
<li>Fehlerreaktion für alle Betriebszustände definieren und mit Fehlerinjektion prüfen.</li>
<li>Schnellladestrategie und Alterungsmodell auf häufiges DC-Laden auslegen.</li>
</ol>
<p>Für eine verbindliche Bewertung ist der vollständige Wortlaut der jeweils geltenden Verordnung, der Durchführungsbestimmungen und der Norm einschließlich der Übergangsregeln heranzuziehen.</p>
''',
 [("Ab wann gelten die Euro-7-Anforderungen an die Batteriehaltbarkeit?", "Ab dem 29.11.2026 für neue Typen von Pkw und leichten Nutzfahrzeugen, ab dem 29.11.2027 für alle neuen Fahrzeuge dieser Klassen."),
  ("Welche Mindestwerte schreibt Euro 7 für Pkw vor?", "80 % der zertifizierten Batterieenergie bis fünf Jahre oder 100.000 km und 72 % bis acht Jahre oder 160.000 km, je nachdem, was zuerst erreicht wird."),
  ("Ist der SOH-Wert des BMS dasselbe wie der SOCE nach Euro 7?", "Nein. Der SOCE ist eine regulatorisch definierte, typgenehmigungsbezogene Größe. Seine Ermittlung muss zur vorgeschriebenen Methode passen; ein beliebiger interner SOH-Wert genügt nicht."),
  ("Was verlangt GB 38031-2025?", "Seit dem 1.7.2026 darf ein Batteriesystem in der vorgeschriebenen thermischen Propagationsprüfung weder Feuer fangen noch explodieren, und ein Warnsignal muss rechtzeitig erfolgen. Hinzu kommen ein Unterboden-Aufpralltest und ein externer Kurzschlusstest nach 300 Schnellladezyklen.")],
 "Euro%207%20und%20GB%2038031")


# ---------- Wissen-Index ----------
items = [
 ("euro-7-gb-38031-bms", "Regulierung", "Euro 7 und GB 38031: Was neue Vorschriften für das BMS bedeuten", "SOCE nach Euro 7 und die thermische Propagationsprüfung nach GB 38031-2025."),
 ("batteriespeicher-sicherheit-artikel-12", "Speicher", "Batteriespeicher sicher nachweisen: Was Artikel 12 verlangt", "Die elf Sicherheitsparameter, die Rolle des BMS und welche Normen bis zur Harmonisierung helfen."),
 ("maschinenverordnung-2027-batteriesystem", "Maschinen", "Maschinenverordnung 2027 und das Batteriesystem", "Software als Sicherheitsbauteil, Schutz gegen Korrumpierung und was Sie vom Batterielieferanten verlangen sollten."),
 ("eu-batteriepass-2027", "Regulierung", "EU-Batteriepass 2027: Was das BMS jetzt liefern muss", "Wer den Pass ausstellt, welche Daten aus dem BMS kommen und was für Speicher und Industriebatterien gilt."),
 ("ki-funktionale-sicherheit", "Entwicklung", "KI in der sicherheitskritischen Entwicklung", "Was ISO 26262 und IEC 61508 zu KI-Werkzeugen sagen und fünf Regeln für die Praxis."),
 ("cloud-bms-digitaler-zwilling", "Daten", "Cloud-BMS und digitaler Zwilling", "Wie Betriebsdaten Alterung vorhersagbar und Batterien wertvoller machen."),
]
cards = "".join(f'<a class="read" href="{s}.html"><span class="topic">{t}</span><div><h3>{h}</h3><p>{d}</p></div><span class="go">Lesen</span></a>' for s, t, h, d in items)
page("wissen/index.html", "Wissen: BMS, Batteriesicherheit und Regulierung | dolavolt",
     "Fachartikel zu Batterieverordnung, Maschinenverordnung 2027, Batteriepass, KI in der funktionalen Sicherheit und Cloud-BMS. Kompakt erklärt von dolavolt.",
     f'<section><div class="wrap"><div class="head"><h1>Wissen</h1><p class="lead">Was Hersteller von Batteriesystemen bis 2027 wissen müssen, erklärt von Ingenieuren, die BMS und Sicherheitsnachweise selbst entwickeln.</p></div><div class="reads">{cards}</div></div></section>')
