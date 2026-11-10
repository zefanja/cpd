# Quizdaten Block 3. Format:
#   "head": Überschrift Teil 1; "starter": [(Frage, Lösung)]
#   "mc": [(Frage, [(Option, Rückmeldung)], Index der richtigen Option)]
GC = "prüft das Mindestziel / in 3–5 Minuten allein lösbar / schriftlich, von allen / in höchstens 10 Minuten auswertbar"
LEITER = "nonverbal → positive Gruppenkorrektur → anonyme Einzelkorrektur → private Einzelkorrektur → blitzschnelle öffentliche Korrektur → Konsequenz"
BID = "Hinweis → Beispiel → Regel → erster Schritt → erst dann die Lösung"

DATA = {}

DATA["3-1"] = {
 "head": "Reaktivierungs-Quiz (8 Fragen zu Block 1 und 2)",
 "starter": [
  ("Skizziere den Planungsbogen aus M2.6 aus dem Kopf.", "Ziel (Mindestziel, Meilensteine, Idealantwort) → Einstieg (Do Now) → Erklären → gemeinsam üben → allein üben → Exit Ticket"),
  ("Bei welcher Erfolgsquote gehst du vom gemeinsamen Üben in die Einzelarbeit, und welche Quote ist das Ziel der Einzelarbeit?", "etwa vier von fünf richtig; in der Einzelarbeit fast fehlerfrei"),
  ("Welche vier Punkte prüft der Gütecheck für ein Exit Ticket?", GC),
  ("Nenne die sechs Stufen der Interventionsleiter.", LEITER),
  ("In welcher Reihenfolge gibst du Hilfen, wenn ein Schüler hängt (Break It Down)?", BID),
  ("Aus welchen drei Zeiträumen stammen die Wiederholungsfragen im Do Now (M2.6)?", "gestern, letzte Woche, letzter Monat"),
  ("Mit welcher Formel formulierst du eine Negativ-Ansage um (M1.6)?", "„Ich sehe [was schon erfüllt ist] – ich will [Zielzustand].“"),
  ("(Szene) Erste Woche nach den Ferien: Welche zwei Dinge führst du ausdrücklich neu ein, und wie gehst du dabei vor?", "z. B. Begrüßungsroutine und Aufmerksamkeitssignal; Erwartung nennen, begründen, prüfen, ob sie verstanden ist, und einmal üben"),
 ],
 "mc": [
  ("In der Klassenkonferenz heißt es über eine neue Schülerin: „Sie kann sich einfach nichts merken.“ Welche Erklärung ist am wahrscheinlichsten?", [
    ("Ihr Arbeitsgedächtnis ist kleiner als das der anderen.", "Möglich, aber selten der Grund. Ohne Vorwissen wirkt jedes Arbeitsgedächtnis klein."),
    ("Ihr fehlt Vorwissen, deshalb ist für sie jedes Detail neu und belegt einen eigenen Platz.", "Vorwissen bündelt Einzelheiten. Wer es nicht hat, ist schneller überlastet. Das lässt sich aufbauen."),
    ("Sie lernt eher über Bilder als über Texte.", "Das ist die Lerntypen-Annahme. Sie ist nicht belegt."),
    ("Sie strengt sich im Unterricht zu wenig an.", "Das ist eine Zuschreibung, keine Erklärung. Erst das Vorwissen prüfen."),
  ], 1),
  ("Nach deinem Filmeinstieg können alle den Film nacherzählen, aber kaum jemand beantwortet die Fachfrage. Was erklärt das am besten?", [
    ("Die Klasse hat über die Handlung nachgedacht, nicht über das Konzept.", "Erinnert wird, worüber nachgedacht wurde. Der Film braucht einen Auftrag, der zum Konzept führt."),
    ("Der Film war zu lang, die Aufmerksamkeit hat nachgelassen.", "Dann könnten sie ihn nicht nacherzählen."),
    ("Filme erreichen nur einen Teil der Lerntypen.", "Lerntypen sind nicht belegt."),
    ("Die Fachfrage war für diese Klasse zu schwer.", "Möglich, erklärt aber nicht, warum der Film so gut hängen blieb."),
  ], 0),
  ("Eine Kollegin plant ihre Stunden nach Lerntypen (visuell, auditiv, kinästhetisch). Was sagt die Forschung dazu?", [
    ("Der Ansatz ist gut belegt, vor allem für schwächere Schüler.", "Dafür gibt es keine belastbaren Belege."),
    ("Der Ansatz wirkt, wenn jeder Typ gleich oft bedient wird.", "Auch das ist nicht belegt."),
    ("Der Ansatz ist belegt, aber nur für die Grundschule.", "Nein, in keiner Altersstufe."),
    ("Schüler haben Vorlieben, lernen mit „passendem“ Material aber nicht besser. Die Darstellung soll zum Inhalt passen.", "Karten für Geografie, Hören für Aussprache: Der Inhalt bestimmt die Form, für alle."),
  ], 3),
  ("Ein Kollege sagt: „Wissen kann man googeln, wichtig sind Kompetenzen.“ Was antwortet die Gedächtnisforschung?", [
    ("Das stimmt für Fakten, aber nicht für Verfahren.", "Auch über Fakten kann nur nachdenken, wer sie im Kopf hat."),
    ("Das stimmt, sofern die Schüler gut recherchieren können.", "Wer wenig weiß, versteht auch das Gefundene schlechter."),
    ("Denken braucht Wissen im Langzeitgedächtnis. Wer alles nachschlagen muss, hat keinen Platz mehr zum Denken.", "Wissen im Langzeitgedächtnis entlastet das Arbeitsgedächtnis. Deshalb ist es die Grundlage von Kompetenz."),
    ("Faktenwissen schadet nicht, bringt für das Denken aber wenig.", "Im Gegenteil: Es ist das Material, mit dem gedacht wird."),
  ], 2),
  ("Deine Stunde war lebendig, alle waren beschäftigt, die Stimmung war gut. Was weißt du damit über das Lernen?", [
    ("Viel: Hohe Beteiligung zeigt, dass gelernt wurde.", "Beschäftigt sein und lernen sind nicht dasselbe."),
    ("Wenig: Entscheidend ist, was später noch abrufbar ist. Das zeigt zum Beispiel ein Exit Ticket oder das Do Now am nächsten Tag.", "Lernen ist, was im Langzeitgedächtnis bleibt. Das sieht man erst später."),
    ("Nichts Gutes: Lebendige Stunden lenken meist vom Stoff ab.", "Das ist die Überkorrektur. Lebendig und lernwirksam schließen sich nicht aus."),
    ("Genug, wenn die Klasse am Ende sagt, dass alles klar ist.", "Selbstauskunft ist keine verlässliche Auskunft (mehr dazu in Modul 4.1)."),
  ], 1),
 ],
}

DATA["3-2"] = {
 "starter": [
  ("Wie lauten die drei Fragen des Diagnose-Rasters aus M3.1?", "War das Arbeitsgedächtnis überlastet? / Ist es nie im Langzeitgedächtnis angekommen, fehlt der Abruf? / Wurde über etwas anderes nachgedacht?"),
  ("Was leistet Vorwissen für das Arbeitsgedächtnis?", "Es bündelt viele Einzelheiten zu einer Einheit (BMW, FBI). Dadurch bleibt Platz zum Denken."),
  ("(Szene) Ein Kollege zeigt die Lernpyramide: „10 % behält man vom Lesen, 90 % vom Lehren.“ Was antwortest du in zwei Sätzen?", "Die Zahlen haben keine Quelle. Richtig ist nur der Kern: Aktiv verarbeiten wirkt besser als nur zuhören."),
  ("Welche vier Punkte prüft der Gütecheck für ein Exit Ticket (M2.6)?", GC),
  ("Was besagt die Halbier-Regel (M2.3)?", "die Schrittgröße halbieren, die sich für mich als Fachperson richtig anfühlt"),
  ("Welche vier Punkte prüft der Vierercheck für eine Anweisung (M1.3)?", "konkret / der Reihe nach, nummeriert / beobachtbar / höchstens 12 Wörter pro Schritt"),
 ],
 "mc": [
  ("Du liest den Text auf deiner Folie wörtlich vor, damit auch die Schwächeren mitkommen. Was passiert dabei?", [
    ("Es hilft: Hören und Lesen zusammen prägen sich doppelt ein.", "So fühlt es sich an. Tatsächlich stören sich die beiden Sprachkanäle."),
    ("Es hilft, solange du langsam genug liest.", "Das Tempo ändert nichts am doppelten Aufwand."),
    ("Die Schüler lesen und hören dasselbe und müssen beides abgleichen. Es bleibt weniger hängen.", "Das ist Redundanz. Regel: Was dasteht, wird nicht vorgelesen."),
    ("Es schadet nur den Stärkeren, die schneller lesen als du sprichst.", "Es belastet alle, die Schwächeren sogar stärker."),
  ], 2),
  ("Deine Aufgabe soll anspruchsvoll bleiben. Welche Belastung senkst du trotzdem?", [
    ("Die Belastung durch Layout, Suchen und gleichzeitige Kanäle.", "Schwer darf die Sache sein, nicht der Weg zu ihr."),
    ("Die Schwierigkeit der Aufgabe selbst.", "Die ist erwünscht. An ihr wird gelernt."),
    ("Beide gleichmäßig, damit niemand überfordert wird.", "Dann wird die Aufgabe leichter, als sie sein soll."),
    ("Keine: Wer sich durchbeißt, lernt am meisten.", "Mühe beim Suchen und Entziffern bringt für das Lernziel nichts."),
  ], 0),
  ("Du rufst die Hausaufgabe in den Lärm des Einpackens. Am nächsten Tag hat die halbe Klasse sie nicht. Was ist die wahrscheinlichste Ursache?", [
    ("Die Klasse hat aus Desinteresse nicht zugehört.", "Erst die einfachere Erklärung prüfen: Die Information war nicht mehr da."),
    ("Die Aufgabe war zu umfangreich.", "Das erklärt nicht, warum viele gar nicht wussten, was auf war."),
    ("Die Ansage kam zu spät in der Stunde.", "Der Zeitpunkt ist ein Teil des Problems. Entscheidend ist, dass nichts stehen blieb."),
    ("Gesprochenes ist sofort weg. Was wichtig ist, muss lesbar stehen bleiben.", "Das ist Transienz. Die Hausaufgabe gehört an die Tafel, bevor eingepackt wird (M1.2)."),
  ], 3),
  ("Welche Folie nutzt Auge und Ohr so, dass sie sich ergänzen?", [
    ("Ein Schaubild mit Fließtext daneben, dazu dein Vortrag.", "Drei Quellen gleichzeitig: Text und Vortrag stören sich."),
    ("Ein Schaubild mit wenigen Beschriftungen, das du frei erklärst.", "Bild für das Auge, Erklärung für das Ohr. Das ist Dual Coding."),
    ("Ein Fließtext, den du Satz für Satz vorliest.", "Derselbe Inhalt auf zwei Sprachkanälen: Redundanz."),
    ("Stichpunkte mit einem auflockernden Bild daneben.", "Ein Bild ohne Bezug zum Inhalt lenkt ab."),
  ], 1),
  ("Eine Kollegin setzt auf jede Folie ein animiertes Männchen: „Das lockert auf.“ Was bewirkt es?", [
    ("Es hält die Aufmerksamkeit bei der Folie.", "Bei der Folie ja, aber beim Männchen statt beim Inhalt."),
    ("Es hilft vor allem jüngeren Klassen.", "Gerade Jüngere lassen sich davon stärker ablenken."),
    ("Es zieht Aufmerksamkeit vom Inhalt ab.", "Bewegtes und Witziges gewinnt gegen Wichtiges. Dekoration ist unnötige Last."),
    ("Es schadet nicht, bringt aber auch nichts.", "Es schadet: Aufmerksamkeit ist begrenzt."),
  ], 2),
 ],
}

DATA["3-3"] = {
 "starter": [
  ("Welche drei Quellen unnötiger Belastung hast du in M3.2 kennengelernt?", "Split Attention (geteilte Aufmerksamkeit), Redundanz (dasselbe doppelt), Transienz (Gesprochenes ist weg)"),
  ("Was unterscheidet die erwünschte von der unnötigen Belastung? Nenne je ein Beispiel.", "erwünscht: die Schwierigkeit der Sache selbst; unnötig: Suchen auf der Folie, Entziffern, zwei Kanäle gleichzeitig"),
  ("(Szene) Deine Folie zeigt ein Bild und 60 Wörter Text, und du sprichst dazu. Was änderst du?", "Bild behalten, Text streichen und sagen, nur die Kernbegriffe als Beschriftung"),
  ("Wie lautet Willinghams Satz aus M3.1?", "„Erinnert wird, worüber nachgedacht wurde.“"),
  ("Was ist das Mindestziel, und welche drei Kriterien prüft die Ampel bei Meilensteinen (M2.2)?", "was am Ende alle können sollen; aufbauend, ansteigend, prüfbar"),
  ("Was tust du zuerst, wenn dich ein Schüler provoziert (M1.4)?", "den Reset-Anker nutzen (ausatmen, fester Stand), erst dann reagieren"),
 ],
 "mc": [
  ("Vor einem Video sagst du: „Schaut aufmerksam zu.“ Was passiert am ehesten?", [
    ("Die meisten achten auf das Wichtige, weil sie vorgewarnt sind.", "Vorgewarnt ja, aber worauf? Das weiß niemand."),
    ("Die Schwächeren schalten ab, die Stärkeren finden das Wichtige selbst.", "Auch Starke folgen dem Auffälligen."),
    ("Alle schreiben mit und verpassen dadurch die Bilder.", "Ohne Auftrag schreibt kaum jemand mit."),
    ("Jeder achtet auf etwas anderes, meist auf das Auffälligste.", "Ohne konkreten Auftrag ist offen, worüber nachgedacht wird."),
  ], 3),
  ("Deine Schüler erinnern sich an deine spannende Anekdote, aber nicht an das Prinzip dahinter. Was machst du beim nächsten Mal?", [
    ("Ich lasse die Anekdote weg.", "Das ist die Überkorrektur. Dann fehlt das, was im Gedächtnis bleibt."),
    ("Ich verbinde die Anekdote mit einem Auftrag, der zum Prinzip führt.", "Zum Beispiel: „Diese Geschichte zeigt Prinzip X. Erklärt zu zweit, wo genau.“"),
    ("Ich erzähle sie erst nach dem Prinzip.", "Die Reihenfolge allein ändert nicht, worüber nachgedacht wird."),
    ("Ich erzähle mehrere Anekdoten, dann bleibt mehr hängen.", "Es bleiben mehr Anekdoten hängen, nicht mehr vom Prinzip."),
  ], 1),
  ("Mit welcher Frage prüfst du am sichersten, ob eine Aufgabe das Zielwissen trainiert?", [
    ("Was muss man denken, um sie zu lösen, und geht es auch ohne diesen Gedanken?", "Lässt sich die Aufgabe durch Abschreiben oder Raten lösen, übt sie Abschreiben oder Raten."),
    ("Wie lange brauchen die Schüler dafür?", "Die Dauer sagt nichts darüber, was gedacht wird."),
    ("Können alle Leistungsniveaus sie lösen?", "Wichtig, aber eine andere Frage."),
    ("Kommt das Thema der Stunde in der Aufgabe vor?", "Das Thema kann vorkommen, ohne dass man darüber nachdenken muss."),
  ], 0),
  ("Die Aufgabe lautet: „Unterstreiche alle Adjektive im Text.“ Was üben die Schüler dabei vor allem?", [
    ("Sie verstehen, wie Adjektive die Wirkung eines Textes verändern.", "Über die Wirkung muss man dafür nicht nachdenken."),
    ("Sie lesen den ganzen Text genau.", "Man kann Wort für Wort absuchen, ohne den Text zu verstehen."),
    ("Sie suchen Wörter nach äußeren Merkmalen. Über die Funktion müssen sie dafür kaum nachdenken.", "Umbau: „Ersetze drei Adjektive so, dass die Stimmung kippt, und erkläre die Wirkung.“"),
    ("Sie wenden Grammatikregeln selbstständig an.", "Nur auf der Stufe des Wiedererkennens."),
  ], 2),
  ("Worauf richtet sich die Aufmerksamkeit, wenn niemand sie lenkt?", [
    ("Auf das, was die Lehrkraft für wichtig hält.", "Nur, wenn sie es ausdrücklich markiert."),
    ("Auf das, was in der Prüfung drankommt.", "Das wissen die Schüler in dem Moment nicht."),
    ("Auf das, was groß und in der Mitte steht.", "Größe hilft, verliert aber gegen Bewegtes und Witziges."),
    ("Auf Neues, Bewegtes, Witziges und alles, was mit anderen Menschen zu tun hat.", "Deshalb gewinnt der Cartoon gegen die Achsenbeschriftung."),
  ], 3),
 ],
}

DATA["3-4"] = {
 "starter": [
  ("Welche drei Hebel lenken die Aufmerksamkeit (M3.3)?", "ein konkreter Beachtungsauftrag vor jedem Medium / Markierungen im Vortrag („Der wichtigste Satz kommt jetzt“) / Aufgaben, die sich nur mit dem Zielgedanken lösen lassen"),
  ("Mit welcher Frage prüfst du eine Aufgabe?", "„Was muss man denken, um sie zu lösen, und geht es auch ohne?“"),
  ("(Szene) Du zeigst gleich ein Diagramm. Formuliere einen Beachtungsauftrag.", "konkret und abhakbar, vor dem Zeigen, z. B. „Vergleicht die Balken von A und B: Um welchen Faktor unterscheiden sie sich?“"),
  ("Welche drei Quellen unnötiger Belastung gibt es (M3.2)?", "Split Attention, Redundanz, Transienz"),
  ("Wie heißen die vier Stufen der Treppe (M2.4)?", "Vollbeispiel → Lückenbeispiel → nur der Anfang → ohne Hilfe"),
  ("Wie lauten die Stufen 1 bis 3 der Interventionsleiter (M1.5)?", "nonverbal → positive Gruppenkorrektur → anonyme Einzelkorrektur"),
 ],
 "mc": [
  ("Wiederlesen fühlt sich flüssig an, sich selbst abfragen fühlt sich mühsam an. Was folgt daraus?", [
    ("Wiederlesen ist wirksamer, weil dabei weniger Fehler passieren.", "Das Gefühl täuscht: Wiedererkennen ist noch nicht Können."),
    ("Beides wirkt gleich gut, es ist eine Frage des Typs.", "Der Vorsprung des Abrufens ist sehr gut belegt."),
    ("Die Mühe beim Abrufen ist der Lerneffekt.", "Was sich holprig anfühlt, bleibt. Diese Verwechslung erklärt, warum so viele mit Textmarker lernen."),
    ("Abfragen lohnt sich nur bei reinem Faktenwissen.", "Auch Anwenden ist Abruf."),
  ], 2),
  ("Wie setzt du Abruf-Quizze so ein, dass sie dem Lernen dienen?", [
    ("Benotet, damit die Klasse sie ernst nimmt.", "Mit Note wird aus Training eine Bedrohung. Fehler werden dann versteckt."),
    ("Unangekündigt und schwer, damit sie wachrütteln.", "Das erzeugt Angst, keinen Abruf."),
    ("Vor allem in der Woche vor der Klassenarbeit.", "Dann fehlt der Abstand, der den Abruf wirksam macht."),
    ("Ohne Note, regelmäßig und mit sofortiger Auflösung.", "Dazu gehört der Satz an die Klasse: „Das ist Training, keine Prüfung.“"),
  ], 3),
  ("Beim Do-Now-Quiz haben viele das Heft aufgeschlagen. Wie reagierst du?", [
    ("Ich lasse es laufen. Hauptsache, die Antworten stimmen.", "Dann wird nachgelesen, nicht abgerufen."),
    ("Hefte zu. Mit offenem Heft ist es Nachlesen, kein Abruf.", "Nur wer aus dem Kopf schreibt, ruft ab. Die Auflösung kommt direkt danach."),
    ("Ich erlaube es den Schwächeren.", "Gerade sie brauchen den Abruf. Besser: leichtere Fragen, gleiches Verfahren."),
    ("Ich erlaube es bei den schweren Fragen.", "Schwere Fragen dürfen falsch beantwortet werden. Die Auflösung klärt sie."),
  ], 1),
  ("Ein Schüler lernt mit Textmarker und liest seine Zusammenfassung dreimal. Was rätst du ihm?", [
    ("Heft zu, sich selbst abfragen, dann kontrollieren.", "Dieselbe Zeit, mehr bleibt. Es fühlt sich schwerer an, und das ist richtig so."),
    ("Öfter lesen, aber über mehrere Tage verteilt.", "Verteilen hilft. Ohne Abruf bleibt es trotzdem Wiederlesen."),
    ("Die Zusammenfassung noch einmal sauber abschreiben.", "Abschreiben ist Kopieren. Es wird nichts aus dem Gedächtnis geholt."),
    ("Mehr Farben für wichtige Stellen verwenden.", "Markieren fühlt sich nach Arbeit an, bringt aber wenig."),
  ], 0),
  ("Was bedeutet der Satz „Auch Anwenden ist Abruf“?", [
    ("Anwendungsaufgaben ersetzen das Abfragen von Fakten.", "Sie ergänzen es. Fakten und Anwendung gehören beide dazu."),
    ("Anwenden kommt erst, wenn die Fakten sitzen.", "Beides kann von Anfang an nebeneinander laufen."),
    ("Wer Wissen in einer neuen Situation benutzt, holt es aus dem Gedächtnis und verknüpft es neu.", "Deshalb gehören auch Anwendungsfragen ins Do Now."),
    ("Anwenden ist wichtiger als Erinnern.", "Ohne Erinnern gibt es nichts anzuwenden."),
  ], 2),
 ],
}

DATA["3-5"] = {
 "starter": [
  ("Welche fünf Kriterien machen aus einem Quiz ein Lernwerkzeug (M3.4)?", "ohne Hilfsmittel / schriftlich, von allen / ohne Note / sofortige Auflösung / regelmäßig"),
  ("Wie ist ein Do Now nach dem 3-2-1-Muster aufgebaut?", "drei Fragen von gestern, zwei von letzter Woche, eine vom letzten Monat"),
  ("(Szene) Ein Kollege sagt: „Quizze sind bloß Abfragerei.“ Was antwortest du in zwei Sätzen?", "Abrufen ist selbst Lernen, es unterbricht das Vergessen. Ohne Note und regelmäßig eingesetzt ist es Training, keine Kontrolle."),
  ("Was zeigt die Vergessenskurve, und was ändert ein Abruf daran (M3.1)?", "Ohne Auffrischung geht der Zugriff schnell verloren. Jeder Abruf setzt neu an, danach fällt die Kurve flacher."),
  ("Was ist der Prüf-Fokus beim Rundgang (M2.5)?", "vorher in einem Satz festlegen, was ich in den Heften prüfe, z. B. die Scheiter-Stelle"),
  ("Was heißt Warm/Strict (M1.4)?", "warmer Ton und klare Sache im selben Satz"),
 ],
 "mc": [
  ("Die Übungsphase lief glatt, fast alle Aufgaben waren richtig. Was sagt das darüber, was in vier Wochen noch da ist?", [
    ("Viel: Wer heute sicher rechnet, kann es auch später.", "Die Leistung von heute stützt sich auf das noch frische Gedächtnis."),
    ("Wenig: Es zeigt die Leistung von heute, nicht das Behalten.", "Leistung in der Stunde und Lernen sind zweierlei. Das Do Now in zwei Wochen zeigt mehr."),
    ("Die Aufgaben waren zu leicht.", "Eine hohe Erfolgsquote ist gewollt. Offen bleibt nur, ob es hält."),
    ("Das Thema kann abgeschlossen werden.", "Jetzt beginnt die Wiederholung erst."),
  ], 1),
  ("Du gibst zum ersten Mal ein gemischtes Übungsblatt aus. Die Klasse protestiert: „Früher konnten wir das besser!“ Was tust du?", [
    ("Ich gehe zurück zu sortierten Blättern, bis das Thema sicher sitzt.", "Dann fehlt genau die Übung, die in der Arbeit gebraucht wird."),
    ("Ich mische nur noch für die Stärkeren.", "Alle müssen in der Arbeit das Verfahren selbst erkennen."),
    ("Ich mische erst kurz vor der Klassenarbeit.", "Dann ist es zu spät, um sich daran zu gewöhnen."),
    ("Ich erkläre: Es fühlt sich schwerer an, weil man das Verfahren selbst wählen muss. Genau das verlangt die Arbeit.", "Gefühl ernst nehmen, Grund nennen, Nutzen für die Arbeit zeigen."),
  ], 3),
  ("Was üben Schüler auf einem gemischten Blatt, was sie auf einem sortierten nicht üben?", [
    ("Zu erkennen, welches Verfahren zur Aufgabe passt.", "Über keiner Prüfungsaufgabe steht, welches Verfahren dran ist."),
    ("Schneller zu rechnen.", "Das Tempo sinkt anfangs eher."),
    ("Länger durchzuhalten.", "Ausdauer ist nicht der Punkt."),
    ("Sorgfältiger aufzuschreiben.", "Das hängt nicht vom Mischen ab."),
  ], 0),
  ("Unter welcher Bedingung sind Klassenarbeiten mit Stoff aus früheren Themen fair?", [
    ("Wenn der alte Stoff weniger Punkte bringt.", "Die Gewichtung macht es nicht fair. Die Vorbereitung tut es."),
    ("Wenn sie unangekündigt kommen, wie Prüfungen im Leben.", "Das ist eine Falle und kostet Vertrauen."),
    ("Wenn sie angekündigt sind und der alte Stoff in den Quizzen laufend geübt wird.", "Ankündigen, trainieren, dann prüfen."),
    ("Wenn nur das letzte Thema davor vorkommt.", "Dann lohnt sich das Vergessen aller älteren Themen."),
  ], 2),
  ("Die Einheit „Bruchrechnung“ ist abgeschlossen. Was geschieht jetzt mit dem Thema?", [
    ("Es wird am Schuljahresende noch einmal wiederholt.", "Eine einzelne späte Wiederholung reicht nicht."),
    ("Es taucht ab jetzt regelmäßig auf: im Do Now, auf Übungsblättern, in Klassenarbeiten.", "Ein Thema ist nie „durch“. Mit dem Abschluss der Einheit beginnt die Wiederholung."),
    ("Es kommt im nächsten Schuljahr laut Lehrplan wieder.", "Bis dahin ist das meiste vergessen."),
    ("Es wird wiederholt, falls die Arbeit schlecht ausfällt.", "Wiederholung ist der Normalfall, nicht die Reparatur."),
  ], 1),
 ],
}

DATA["3-6"] = {
 "head": "Block-3-Quiz (20 Fragen, zurück bis Modul 1.1)",
 "starter": [
  ("Wie lauten die drei Kernsätze aus M3.1?", "Lernen ist eine dauerhafte Veränderung im Langzeitgedächtnis. / Erinnert wird, worüber nachgedacht wurde. / Vergessen ist der Normalfall."),
  ("Wie lauten die drei Fragen des Diagnose-Rasters?", "Arbeitsgedächtnis überlastet? / nie im Langzeitgedächtnis angekommen? / über etwas anderes nachgedacht?"),
  ("Was leistet Vorwissen für das Arbeitsgedächtnis?", "Es bündelt Einzelheiten und schafft Platz zum Denken."),
  ("Welche drei Quellen unnötiger Belastung gibt es?", "Split Attention, Redundanz, Transienz"),
  ("Was unterscheidet erwünschte von unnötiger Belastung?", "Schwierigkeit der Sache selbst gegen Aufwand durch Layout, Suchen, parallele Kanäle"),
  ("Was ist Dual Coding, richtig verstanden?", "Bild und gesprochenes Wort ergänzen sich; nicht Bild plus Text plus Vortrag"),
  ("Welche drei Hebel lenken die Aufmerksamkeit?", "Beachtungsauftrag / Markierungen im Vortrag / Aufgaben, die den Zielgedanken erzwingen"),
  ("Mit welcher Frage prüfst du eine Aufgabe?", "„Was muss man denken, um sie zu lösen, und geht es auch ohne?“"),
  ("Was besagt der Testing Effect?", "Abrufen stärkt das Behalten mehr als erneutes Lesen."),
  ("Warum lernen viele Schüler mit Textmarker und Wiederlesen?", "Es fühlt sich flüssig an; Wiedererkennen wird mit Können verwechselt."),
  ("Welche fünf Kriterien gelten für Abruf-Quizze?", "ohne Hilfsmittel / schriftlich, alle / ohne Note / sofortige Auflösung / regelmäßig"),
  ("Wie ist ein Do Now nach 3-2-1 aufgebaut?", "drei von gestern, zwei von letzter Woche, eine vom letzten Monat"),
  ("Was bedeutet „Leistung in der Stunde ist nicht Lernen“?", "Was heute flüssig klappt, kann in vier Wochen weg sein."),
  ("Warum wirkt verteiltes Üben?", "Nach einer Lücke ist der Abruf schwerer und festigt deshalb stärker."),
  ("Was üben Schüler bei gemischten Aufgaben zusätzlich?", "das passende Verfahren zu erkennen"),
  ("Welche Regel gilt für Klassenarbeiten mit altem Stoff?", "ankündigen und in Quizzen laufend üben"),
  ("(Block 1) Nenne die sechs Stufen der Interventionsleiter.", LEITER),
  ("(Block 2) Was heißt „von der Idealantwort her planen“?", "die ideale Schülerantwort zum Mindestziel vorher selbst ausformulieren"),
  ("(Block 2) Welche vier Punkte prüft der Gütecheck für ein Exit Ticket?", GC),
  ("(Szene) Ein Kollege sagt: „Meine Stunden laufen super, aber in den Arbeiten ist alles weg.“ Deute das mit drei Konzepten aus Block 3 und nenne je eine Konsequenz.", "Leistung ist nicht Lernen → am Ticket vom Folgetag messen; kein Abruf → 3-2-1 im Do Now; alles am Stück geübt → verteilen und mischen"),
 ],
 "mc": [
  ("Was gehört auf einen Knowledge Organizer?", [
    ("Möglichst alles, was in der Einheit vorkommt.", "Dann ist es ein Archiv. Der Nutzen liegt in der Auswahl."),
    ("Die Tafelbilder der Einheit in Kurzform.", "Tafelbilder zeigen Erklärwege, nicht das Kernwissen."),
    ("Das Kernwissen einer Einheit auf einer Seite, so angeordnet, dass man sich selbst abfragen kann.", "Begriffe links, Definitionen rechts zum Abdecken."),
    ("Die Aufgabentypen der kommenden Klassenarbeit.", "Das wäre eine Aufgabensammlung."),
  ], 2),
  ("Der Auftrag lautet: „Erstellt eine Mindmap zum Thema.“ Unter welcher Bedingung vernetzen die Schüler dabei wirklich Wissen?", [
    ("Immer, denn die Verbindungen sind ja sichtbar.", "Linien kann man ziehen, ohne über den Zusammenhang nachzudenken."),
    ("Wenn sie an jede Linie schreiben müssen, wie die Begriffe zusammenhängen.", "Die beschriftete Linie erzwingt den Gedanken."),
    ("Wenn sie mit mehreren Farben arbeiten.", "Farben ordnen, sie erklären nichts."),
    ("Wenn sie in Gruppen arbeiten.", "Die Sozialform ändert nicht, was gedacht werden muss."),
  ], 1),
  ("Warum wirkt der Auftrag „Erkläre es einem Fünftklässler“?", [
    ("Fachwörter kann man nachsprechen. Einfach erklären kann nur, wer es verstanden hat.", "Vereinfachen zwingt dazu, den Zusammenhang selbst herzustellen."),
    ("Der Rollenwechsel motiviert.", "Mag sein, ist aber nicht der Grund für die Wirkung."),
    ("Er verlangt kürzere Antworten.", "Einfache Erklärungen sind oft länger."),
    ("Er trainiert das freie Sprechen.", "Ein Nebeneffekt."),
  ], 0),
  ("Vor der Klassenarbeit überlegst du, ob zehn Minuten „So lernt man für meine Arbeit“ gut investiert sind. Sind sie es?", [
    ("Nein, das ist Aufgabe der Eltern und der Schüler.", "Die meisten haben es nie gezeigt bekommen."),
    ("Nein, die Zeit fehlt dann für den Stoff.", "Zehn Minuten, die viele Stunden häuslichen Lernens wirksamer machen."),
    ("Nur in der Unterstufe.", "Auch Oberstufenschüler lernen oft mit Wiederlesen."),
    ("Ja: Viele lernen wirkungslos, weil ihnen niemand etwas anderes gezeigt hat.", "Mit dem Knowledge Organizer und einer kurzen Vorführung der Selbstabfrage."),
  ], 3),
  ("Du bekommst das Wissen deiner Einheit nicht auf eine Seite. Was bedeutet das?", [
    ("Ich sollte kleiner schreiben.", "Dann wird es unlesbar und bleibt zu viel."),
    ("Ich sollte zwei Seiten zulassen.", "Dann weicht die Auswahl nur aus."),
    ("Ich habe noch nicht entschieden, was der Kern ist.", "Die eine Seite zwingt zur Entscheidung. Das ist Planung vom Ziel her (M2.2)."),
    ("Die Einheit eignet sich nicht für einen Knowledge Organizer.", "Jede Einheit hat einen Kern."),
  ], 2),
 ],
}
