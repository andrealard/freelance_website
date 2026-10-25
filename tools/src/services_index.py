# Leistungsübersicht mit Kompetenzen und Zusammenarbeit (von der Startseite hierher verschoben)
svc_rows = "".join(f'<a class="read" href="{s}.html"><span class="topic">{t}</span><div><h3>{dict(SERVICES)[s]}</h3><p>{d}</p></div><span class="go">Mehr</span></a>' for s, t, d in SHORT_DE)
page("leistungen/index.html", "Leistungen: Experten für BMS-Software, ISO 26262, AUTOSAR, Simulink und Elektrifizierung von Landmaschinen | dolavolt",
     "Übersicht unserer Engineering-Leistungen: BMS-Software, Elektrifizierung von Land- und Baumaschinen, funktionale Sicherheit nach ISO 26262, AUTOSAR, MATLAB/Simulink, Test und HIL, Requirements und ASPICE. Auch als Freelancer.",
     f'''<section><div class="wrap"><div class="head"><h1>Leistungen</h1><p class="lead">Expertise für Entwicklungsteams in Automotive und Landtechnik, von der Anforderung bis zur Serie.</p></div><div class="reads">{svc_rows}</div></div></section>
<section class="band"><div class="wrap"><div class="head"><h2>Kompetenzen und Werkzeuge</h2><p class="lead">Die Normen, Technologien und Werkzeuge, mit denen wir arbeiten.</p></div><div class="skills">{skills_html(SKILLS_DE)}</div></div></section>
<section><div class="wrap"><div class="head"><h2>So arbeiten wir mit Ihnen</h2><p class="lead">Flexibel in der Form, verbindlich im Ergebnis.</p></div>
<div class="reasons">
 <div><h3>Im Team auf Zeit</h3><p>Als Teil Ihres Entwicklungsteams auf Stunden- oder Tagesbasis im Dienstvertrag, in Ihren Werkzeugen und Prozessen.</p></div>
 <div><h3>Arbeitspakete zum Festpreis</h3><p>Klar abgegrenzte Aufgaben, etwa ein Sicherheitskonzept oder ein Softwaremodul, im Werkvertrag mit definiertem Ergebnis.</p></div>
 <div><h3>Remote und vor Ort</h3><p>Überwiegend remote, für Workshops, Integration und Tests bei Ihnen: München, Ingolstadt, Regensburg, Stuttgart und europaweit nach Absprache.</p></div>
</div></div></section>''',
     extra_head=f'<meta name="keywords" content="{KW_DE}">\n')
