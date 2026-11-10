from gen_core import IMG, js

TERMS = [
    ["Cold Call", "ohne Meldung aufrufen, nachdem alle Zeit zum Denken hatten"],
    ["Wait Time", "nach der Frage drei bis fünf Sekunden warten"],
    ["No Opt Out", "nach „Weiß nicht“ zur selben Person zurückkehren, bis sie Erfolg hat"],
    ["Right is Right", "halbrichtige Antworten nicht als richtig gelten lassen"],
    ["Stretch It", "auf eine richtige Antwort eine weiterführende Frage stellen"],
    ["Turn and Talk", "kurzes Partnergespräch mit klarer Frage und knapper Zeit"],
    ["Everybody Writes", "alle schreiben, bevor gesprochen wird"],
    ["Show Call", "eine Schülerarbeit vor der Klasse zeigen und besprechen"],
    ["Affirmative Checking", "Kontrollpunkt, bevor Schüler weiterarbeiten dürfen"],
    ["Own and Track", "Schüler korrigieren und verfolgen ihre Fehler selbst"],
]
NEXT = '<p style="margin-top:1.3rem"><button class="btn" data-nav="next">Weiter →</button></p>'


def mem(id_, titel, text, hinweis):
    return f"""
  <div class="card">
    <h3>{titel}</h3>
    <p style="font-size:.92rem">{text}</p>
    <p style="margin-top:.7rem"><button class="btn small" id="{id_}Btn">5 Sekunden zeigen</button></p>
    <div class="stagebox" id="{id_}Box"><div class="bigshow" id="{id_}Show"></div><p class="hint" style="text-align:center">noch <span class="count">5</span> Sekunden</p></div>
    <div class="stagebox" id="{id_}Stage">
      <div class="field"><label for="{id_}In">{hinweis}</label><input type="text" id="{id_}In" autocomplete="off" placeholder="…"></div>
      <p style="margin-top:.6rem"><button class="btn ghost small" id="{id_}Eval">Auswerten</button></p>
      <p class="quiz-note on" id="{id_}Res" style="border-top:none"></p>
    </div>
  </div>"""


# ============================================================ Modul 3.1
M31 = dict(
    n="3.1", skript="3-1", key="modul3-1-gedaechtnis", file="Modul3-1_Gedaechtnis_SPA.html", title="Wie das Gedächtnis arbeitet",
    frage="Was passiert im Kopf, wenn jemand etwas lernt?",
    lead="In Block 1 und 2 hast du Werkzeuge bekommen. Bei vielen Warum-Fragen hieß es: „Kommt in Block 3.“ Jetzt ist es so weit. Du beginnst mit drei kurzen Versuchen an dir selbst.",
    weg="Zuerst rufst du ab, was aus Block 1 und 2 geblieben ist. Dann machst du drei Selbstversuche und bekommst drei Sätze, die den ganzen Block tragen. Mit drei Fragen deutest du typische Unterrichtsprobleme, und du übst, zwei verbreiteten Lernmythen freundlich zu widersprechen.",
    min=25, quellen="McCrea, Memorable Teaching · Willingham · Ebbinghaus",
    abruf_h="Acht Fragen zu Block 1 und 2.",
    abruf_lead="Nach Ferien ist Auffrischen wichtiger als Neues. Das gilt für dich wie für deine Klassen. Ohne Unterlagen.",
    steps=[
        {"id": "last", "label": "Standard · Belastung senken", "text": "Ich finde in einer meiner Stunden die drei Stellen, an denen am meisten Neues gleichzeitig kommt, und entschärfe eine davon."},
        {"id": "raster", "label": "Alternative 1 · Drei Fragen", "text": "Jedes Mal, wenn ich denke „Die verstehen es einfach nicht“, notiere ich die drei Fragen und meine Antwort darauf."},
        {"id": "neustart", "label": "Alternative 2 · Routinen-Neustart", "text": "Ich führe nach den Ferien zwei Routinen ausdrücklich neu ein: Erwartung nennen, begründen, prüfen, einmal üben."},
    ],
    log_title="Meine Stellen mit hoher Belastung", log_label="Stelle",
    log_hint="Trag nach drei Stunden ein, wo viel Neues gleichzeitig kam, was du geändert hast und was sich gezeigt hat.",
    log_fields=[{"f": "wo", "label": "wo genau", "ph": "z. B. vier neue Begriffe in zwei Minuten"}, {"f": "neu", "label": "geändert", "ph": "…"}, {"f": "wirk", "label": "Wirkung", "ph": "…"}],
    exit=["Der Satz aus diesem Modul, der bei mir hängen bleibt:", "Eine Situation aus meinem Unterricht, die ich jetzt anders deute:"],
    ausblick="„Beim nächsten Input geht es um dein Material: Wie du Folien, Arbeitsblätter und deine eigene Sprache von unnötiger Belastung befreist. Bring deine schlimmste eigene Folie mit. Ja, genau die.“",
    fixed=["rast", "fall", "myth"],
)
M31["screens"] = f"""
<section class="screen" data-title="Drei Selbstversuche">
  <span class="eyebrow">Station 2 · Drei Selbstversuche</span>
  <h2>Versuchsperson: du.</h2>
  <p class="lead">Jeder Versuch dauert eine Minute. Mach sie der Reihe nach und ohne Zettel.</p>
  {mem('v1', 'Versuch 1 · Eine Zahl rückwärts', 'Du siehst gleich fünf Sekunden lang eine elfstellige Zahl. Danach tippst du sie <strong>rückwärts</strong> ein.', 'Die Zahl rückwärts')}
  <div class="card reveal" id="v1After"><p style="font-size:.92rem">Und jetzt: dein Geburtsdatum, rückwärts, im Kopf. Das geht mühelos. Der Unterschied: Die Zahl musstest du im <strong>Arbeitsgedächtnis</strong> halten, und das hat nur etwa vier bis sieben Plätze. Dein Geburtsdatum liegt im <strong>Langzeitgedächtnis</strong> und belegt keinen dieser Plätze.</p></div>
  {mem('v2', 'Versuch 2 · Dreizehn Buchstaben', 'Du siehst fünf Sekunden lang dreizehn Buchstaben. Danach tippst du sie in der richtigen Reihenfolge ein.', 'Die Buchstaben der Reihe nach')}
  {mem('v3', 'Versuch 2b · Dieselben Buchstaben, anders gruppiert', 'Noch einmal dreizehn Buchstaben, wieder fünf Sekunden.', 'Die Buchstaben der Reihe nach')}
  <div class="card reveal" id="v3After"><p style="font-size:.92rem">Es waren dieselben dreizehn Buchstaben. Beim zweiten Mal wurden daraus vier Einheiten, weil dein Langzeitgedächtnis die Muster kennt. <strong>Vorwissen schafft Platz im Arbeitsgedächtnis.</strong> Wer viel weiß, kann mehr denken, nicht umgekehrt.</p></div>
  <div class="card">
    <h3>Versuch 3 · Vorgestern Abend</h3>
    <div class="field" style="margin-top:.4rem"><label for="v4">Was genau hast du vorgestern zu Abend gegessen, und worüber hast du dabei nachgedacht?</label><textarea id="v4" data-store="v4" placeholder="…"></textarea></div>
    <p style="margin-top:.6rem"><button class="btn ghost small" data-reveal="v4After">Auflösung</button></p>
    <p class="quiz-note reveal" id="v4After">Die meisten wissen es nicht mehr. Vergessen ist kein Betriebsunfall, sondern der Normalfall. Unterricht, der das Vergessen nicht einplant, bekommt es trotzdem.</p>
  </div>
  {NEXT}
</section>

<section class="screen" data-title="Drei Sätze">
  <span class="eyebrow">Station 3 · Drei Sätze</span>
  <h2>Drei Sätze tragen den ganzen Block.</h2>
  <div class="formula-card"><h4>1 · Lernen ist eine dauerhafte Veränderung im Langzeitgedächtnis.</h4><p style="margin-top:0">Was dort nicht ankommt, wurde nicht gelernt, egal wie lebendig die Stunde war.</p></div>
  <div class="formula-card"><h4>2 · Erinnert wird, worüber nachgedacht wurde.</h4><p style="margin-top:0">Nicht, was du gesagt hast, und nicht, was auf der Folie stand. Wer beim Versuch über den Knall staunt, behält den Knall (Willingham).</p></div>
  <div class="formula-card"><h4>3 · Vergessen ist der Normalfall.</h4><p style="margin-top:0">Wiederholung ist deshalb keine verlorene Zeit. Sie ist der einzige bekannte Weg, die Kurve zu brechen.</p></div>
  <img class="fig" src="./assets/images/Gedaechtnismodell.png" alt="Gedächtnismodell: Umwelt, Aufmerksamkeit, Arbeitsgedächtnis, Langzeitgedächtnis" loading="lazy">
  {IMG('b3-vergessenskurve', 'Vergessenskurve mit drei Abrufen in wachsenden Abständen')}
  <h3 style="margin-top:1.4rem">Du hast das alles schon benutzt.</h3>
  <p class="lead">Jedes Werkzeug aus Block 1 und 2 antwortet auf einen dieser Sätze.</p>
  {IMG('b3-kaskade', 'Die drei Kernsätze und die Werkzeuge aus Block 1 und 2')}
  {NEXT}
</section>

<section class="screen" data-title="Drei Fragen">
  <span class="eyebrow">Station 4 · Drei Fragen</span>
  <h2>Drei Fragen an jedes „Die verstehen es nicht“.</h2>
  <div class="formula-card">
    <h4>Das Raster</h4>
    <ol class="q-legend"><li><b>1</b>War das Arbeitsgedächtnis überlastet?</li><li><b>2</b>Ist es nie im Langzeitgedächtnis angekommen, fehlt der Abruf?</li><li><b>3</b>Wurde über etwas anderes nachgedacht?</li></ol>
    <p>Jede Frage führt zu einer anderen Konsequenz. Deshalb lohnt es sich, sie auseinanderzuhalten.</p>
  </div>
  <h3 style="margin-top:1.4rem">Welche Frage trifft?</h3>
  <div id="rastList"></div>
  {NEXT}
</section>

<section class="screen" data-title="Vier Fälle">
  <span class="eyebrow">Station 5 · Vier Fälle</span>
  <h2>Vier Klassiker aus dem Lehrerzimmer.</h2>
  <p class="lead">Wähle die Deutung, die am besten trägt. Die Rückmeldung nennt jeweils ein Werkzeug, das du schon kennst.</p>
  <div id="fallList"></div>
  {NEXT}
</section>

<section class="screen" data-title="Lernmythen">
  <span class="eyebrow">Station 6 · Lernmythen</span>
  <h2>Freundlich widersprechen.</h2>
  <p class="lead">Du wirst in Konferenzen sitzen, in denen mit diesen Sätzen Unterricht begründet wird. Gesucht ist die Antwort, die den wahren Kern anerkennt und trotzdem genau ist. Recht haben reicht nicht, wenn der Ton belehrt.</p>
  <div id="mythList"></div>
  {NEXT}
</section>
"""
M31["js"] = f"""
const RAST_OPTS=['1 · Arbeitsgedächtnis überlastet','2 · nicht angekommen, kein Abruf','3 · über etwas anderes nachgedacht'];
const RAST=[
 {{t:'Du erklärst drei neue Begriffe in einem Satz und gibst gleichzeitig den Arbeitsauftrag.',ok:0,note:'Zu viel Neues auf einmal. Konsequenz: ein Schritt nach dem anderen (Halbier-Regel, M2.3).'}},
 {{t:'Vor zwei Wochen konnten es alle. Seitdem kam das Thema nicht mehr vor. Heute weiß es kaum jemand.',ok:1,note:'Es war nur zu Besuch. Konsequenz: altes Material ins Do Now (M2.6).'}},
 {{t:'Die Klasse gestaltet zwei Stunden lang Plakate zur Photosynthese. Im Test weiß sie viel über Schriftarten und wenig über Photosynthese.',ok:2,note:'Nachgedacht wurde über die Gestaltung. Konsequenz: Aufgaben, die den Inhalt verlangen (M3.3).'}},
 {{t:'Während du den Rechenweg erklärst, schreiben alle von der Tafel ab.',ok:0,note:'Zuhören und Abschreiben gleichzeitig überfordert. Konsequenz: Stifte weg beim Vormachen (M2.3).'}},
 {{t:'Nach dem Versuch mit dem lauten Knall erinnern sich alle an den Knall, niemand an die Reaktionsgleichung.',ok:2,note:'Der Knall hat die Aufmerksamkeit gebunden. Konsequenz: vorher einen Beobachtungsauftrag geben.'}},
 {{t:'Die Vokabeln wurden einmal eingeführt und danach nie abgefragt.',ok:1,note:'Ohne Abruf zerfällt der Zugriff. Konsequenz: regelmäßig abfragen, ohne Note (M3.4).'}}
];
const FALL_OPTS=['Arbeitsgedächtnis überlastet','nicht angekommen, kein Abruf','über etwas anderes nachgedacht','liegt an der Person'];
const FALL=[
 {{tag:'Fall 1',t:'„In der Stunde konnten sie es, im Test eine Woche später nicht.“',ok:1,note:'In der Stunde war es noch frisch. Danach wurde es nie wieder abgerufen. Werkzeug: Do Now mit altem Stoff, Aufgaben aus früheren Themen. Mehr dazu in M3.5.'}},
 {{tag:'Fall 2',t:'„Nach dem spektakulären Filmeinstieg können alle den Film nacherzählen, keiner beantwortet die Fachfrage.“',ok:2,note:'Nachgedacht wurde über die Handlung. Werkzeug: ein genauer Beobachtungsauftrag vor dem Film. Die Auflösung kommt in M3.3.'}},
 {{tag:'Fall 3',t:'„Die neue Schülerin kann sich einfach nichts merken“, sagt die Klassenkonferenz.',ok:0,note:'Ihr fehlt Vorwissen, deshalb belegt jedes Detail einen eigenen Platz. Das ist keine Eigenschaft der Person. Werkzeug: Vorwissen aufbauen, kleinere Schritte.'}},
 {{tag:'Fall 4',t:'„Beim Sachtext scheitern viele, dabei können sie flüssig lesen.“',ok:0,note:'Ohne Vorwissen zum Thema bleibt jeder Satz eine Folge einzelner Wörter, wie die dreizehn Buchstaben. Werkzeug: Schlüsselbegriffe vor dem Text klären.'}}
];
const MYTH=[
 {{tag:'Ein Kollege sagt',t:'„Der ist halt ein visueller Typ, dem musst du das aufmalen.“',ok:2,note:'Erst der wahre Kern (Vorlieben gibt es), dann die Korrektur, dann eine brauchbare Alternative.',
   opts:['„Lerntypen sind längst widerlegt, das weiß man doch.“','„Stimmt, ich mache ihm ein Extrablatt mit Bildern.“','„Vorlieben haben viele, das stimmt. Besser lernen sie damit aber nicht. Ich frage eher: Welche Darstellung passt zum Inhalt? Die hilft dann allen.“']}},
 {{tag:'Eine Kollegin sagt',t:'„Man behält 10 % vom Lesen und 90 % vom Lehren. Deshalb lasse ich nur noch Referate halten.“',ok:0,note:'Der Kern stimmt, die Zahlen nicht. So bleibt das Gespräch offen.',
   opts:['„Der Kern stimmt: Selbst erklären wirkt besser als nur zuhören. Für die Prozentzahlen gibt es allerdings keine Quelle.“','„Die Pyramide ist erfunden. Das solltest du nicht mehr verwenden.“','„Guter Punkt, das probiere ich auch.“']}},
 {{tag:'Ein Kollege sagt',t:'„Wir nutzen ja nur 10 % unseres Gehirns. Da ist noch viel Luft.“',ok:1,note:'Freundlich im Ton, klar in der Sache.',
   opts:['„Spannend, daran müsste man im Unterricht arbeiten.“','„Schön wäre es. Aufnahmen des Gehirns zeigen aber: Wir nutzen alle Bereiche, nur nicht alle gleichzeitig.“','„Das ist ein Werbemythos, das glaubt doch keiner mehr.“']}},
 {{tag:'Eine Kollegin sagt',t:'„Die heutige Generation lernt anders. Die brauchen kurze Clips statt Texte.“',ok:2,note:'Gewohnheiten ändern sich, das Gedächtnis nicht.',
   opts:['„Stimmt, Texte kann man denen nicht mehr zumuten.“','„Das ist wissenschaftlich nicht haltbar.“','„Ihre Gewohnheiten sind anders, das merke ich auch. Das Gedächtnis arbeitet aber wie bei uns: Sie behalten, worüber sie nachdenken, und vergessen ohne Wiederholung.“']}}
];
const MEM={{v1:['0 1 7 6 4 4 9 2 3 1 8','81329446710'],v2:['B M W F B I U S A A D A C','BMWFBIUSAADAC'],v3:['BMW · FBI · USA · ADAC','BMWFBIUSAADAC']}};
function moduleState(){{return {{rast:fill(RAST.length,-1),fall:fill(FALL.length,-1),myth:fill(MYTH.length,-1),v1Score:-1,v2Score:-1,v3Score:-1,v1In:'',v2In:'',v3In:''}};}}
function memShow(id){{
  if(state[id+'Score']>-1){{
    $(id+'Stage').style.display='block';$(id+'In').value=state[id+'In']||'';
    $(id+'Res').innerHTML='<strong>'+state[id+'Score']+' von '+MEM[id][1].length+'</strong> Stellen an der richtigen Position.';
    if(id==='v1')$('v1After').classList.add('on');
    if(id==='v3')$('v3After').classList.add('on');
  }}
}}
function memInit(id){{
  $(id+'Show').textContent=MEM[id][0];
  $(id+'Btn').onclick=()=>{{$(id+'Btn').disabled=true;timedShow(id+'Box',5,()=>{{$(id+'Stage').style.display='block';$(id+'In').focus();}});}};
  $(id+'Eval').onclick=()=>{{
    const a=$(id+'In').value.toUpperCase().replace(/[^A-Z0-9]/g,''),t=MEM[id][1];let n=0;
    for(let i=0;i<t.length;i++)if(a[i]===t[i])n++;
    state[id+'Score']=n;state[id+'In']=$(id+'In').value;scheduleSave();memShow(id);renderSummary();
  }};
  memShow(id);
}}
function renderModule(){{
  ['v1','v2','v3'].forEach(memInit);
  pickList('rast','rastList',RAST,RAST_OPTS);pickList('fall','fallList',FALL,FALL_OPTS);pickList('myth','mythList',MYTH,null);
}}
function ROWS(){{
  const v=['v1','v2','v3'].filter(k=>state[k+'Score']>-1).length;
  return [['Selbstversuche',v===3?'✓ alle drei':v+'/3',v===3],pickRow('Drei Fragen','rast'),pickRow('Vier Fälle','fall'),pickRow('Lernmythen','myth')];
}}
function SECTIONS(){{
  return [['Selbstversuche','Zahl rückwärts: '+(state.v1Score>-1?state.v1Score+' von 11':'–')+'\\nBuchstaben einzeln: '+(state.v2Score>-1?state.v2Score+' von 13':'–')+'\\nBuchstaben gruppiert: '+(state.v3Score>-1?state.v3Score+' von 13':'–')+'\\n'+fld('Vorgestern Abend','v4')],
    ['Übungen',pickText('Drei Fragen','rast')+'\\n'+pickText('Vier Fälle','fall')+'\\n'+pickText('Lernmythen','myth')]];
}}
"""

# ============================================================ Modul 3.2
M32 = dict(
    n="3.2", skript="3-2", key="modul3-2-kognitive-last", file="Modul3-2_Kognitive-Last_SPA.html", title="Material und Sprache entlasten",
    frage="Wie halte ich den Kopf meiner Schüler frei für das, worauf es ankommt?",
    lead="Das Arbeitsgedächtnis ist eng, das weißt du aus Modul 3.1. Heute geht es darum, was es unnötig füllt: überladene Folien, vorgelesene Texte, Anweisungen, die nur gesagt werden.",
    weg="Nach dem Abruf erlebst du denselben Inhalt zweimal: einmal auf einer überladenen Folie, einmal entschlackt. Du lernst drei Quellen unnötiger Belastung kennen, ordnest Unterrichtsmomente zu und operierst eine Folie. Zum Schluss prüfst du ein eigenes Material mit der Checkliste.",
    min=25, quellen="McCrea, Memorable Teaching · Sweller (Cognitive Load) · Lemov „Board = Paper“",
    steps=[
        {"id": "folie", "label": "Standard · Checkliste und nichts vorlesen", "text": "Ich überarbeite die Folien meiner nächsten Einheit mit der Checkliste und lese in keiner Stunde vor, was die Klasse selbst sieht."},
        {"id": "tafel", "label": "Alternative 1 · Tafel", "text": "Die Kernschritte jeder Erklärung bleiben bis zum Stundenende an der Tafel stehen."},
        {"id": "schrift", "label": "Alternative 2 · Anweisungen", "text": "Jede Anweisung mit zwei oder mehr Schritten steht schriftlich an Tafel, Folie oder Blatt."},
    ],
    log_title="Meine Strichliste", log_label="Tag",
    log_hint="Sei ehrlich: Wie oft hast du dich beim Vorlesen ertappt? Die Zahl soll über die Tage fallen.",
    log_fields=[{"f": "n", "label": "wie oft ertappt", "ph": "z. B. 3"}, {"f": "wo", "label": "in welcher Situation", "ph": "…"}, {"f": "statt", "label": "was ich stattdessen tat", "ph": "…"}],
    exit=["Was ich an meinem Material als Erstes ändere:", "Wo mir das Weglassen schwerfällt:"],
    ausblick="„Der Kopf ist jetzt frei. Beim nächsten Input geht es darum, wohin die Aufmerksamkeit geht, mit einem Versuch, der zeigt, wie eigenwillig deine eigene ist. Und mit der Antwort auf den Fall mit dem Filmeinstieg.“",
    fixed=["r1", "r2", "quel", "make", "mat"],
)
M32["screens"] = f"""
<section class="screen" data-title="Ein Versuch">
  <span class="eyebrow">Station 2 · Ein Versuch</span>
  <h2>Derselbe Inhalt, zweimal.</h2>
  <p class="lead">Du siehst zweimal 30 Sekunden lang eine Folie zum Wasserkreislauf. Unter der Folie läuft mit, was die Lehrkraft dazu sagt. Danach kommen drei Fragen.</p>
  <div class="card">
    <h3>Durchgang 1</h3>
    <p style="margin-top:.5rem"><button class="btn small" id="r1Btn">Folie 30 Sekunden zeigen</button></p>
    <div class="stagebox" id="r1Box">{IMG('b3-horrorfolie', 'Überladene Folie zum Wasserkreislauf')}<div class="ticker" id="r1Tick"></div><p class="hint">noch <span class="count">30</span> Sekunden</p></div>
    <div class="stagebox" id="r1Stage"><div id="r1List"></div>
      <div class="field"><label for="r1Muehe">Wie anstrengend war das Aufnehmen?</label><select id="r1Muehe" data-store="r1Muehe"><option value="">bitte wählen</option><option>1 · mühelos</option><option>2</option><option>3</option><option>4</option><option>5 · sehr anstrengend</option></select></div>
    </div>
  </div>
  <div class="card">
    <h3>Durchgang 2</h3>
    <p class="hint">Erst nach Durchgang 1.</p>
    <p style="margin-top:.5rem"><button class="btn small" id="r2Btn">Folie 30 Sekunden zeigen</button></p>
    <div class="stagebox" id="r2Box">{IMG('b3-zwillingsfolie', 'Entschlackte Folie zum Wasserkreislauf')}<div class="ticker">Die Lehrkraft erklärt frei und zeigt dabei nacheinander auf die vier Stationen.</div><p class="hint">noch <span class="count">30</span> Sekunden</p></div>
    <div class="stagebox" id="r2Stage"><div id="r2List"></div>
      <div class="field"><label for="r2Muehe">Wie anstrengend war das Aufnehmen?</label><select id="r2Muehe" data-store="r2Muehe"><option value="">bitte wählen</option><option>1 · mühelos</option><option>2</option><option>3</option><option>4</option><option>5 · sehr anstrengend</option></select></div>
    </div>
  </div>
  <div class="card reveal" id="rResult"></div>
  {NEXT}
</section>

<section class="screen" data-title="Drei Quellen">
  <span class="eyebrow">Station 3 · Drei Quellen</span>
  <h2>Schwer darf die Sache sein, nicht der Weg zu ihr.</h2>
  <p class="lead">Es geht nicht darum, Unterricht leicht zu machen. Die Schwierigkeit der Sache selbst ist erwünscht, an ihr wird gelernt. Bekämpft wird alles drumherum, das Platz belegt, ohne dass etwas gelernt wird.</p>
  {IMG('b3-lastquellen', 'Drei Quellen unnötiger Belastung: Split Attention, Redundanz, Transienz')}
  <div class="formula-card">
    <h4>Bild und gesprochenes Wort</h4>
    <p style="margin-top:0">Auge und Ohr ergänzen sich, wenn das Auge ein Schaubild bekommt und das Ohr die Erklärung (Dual Coding). Bild plus Textblock plus Vortrag ist das Gegenteil davon.</p>
    <p><strong>Faustregel für jede Folie:</strong> ein Gedanke, ein Träger (Bild oder Text), der Rest kommt aus deinem Mund.</p>
  </div>
  <h3 style="margin-top:1.4rem">Welche Quelle ist es?</h3>
  <div id="quelList"></div>
  {NEXT}
</section>

<section class="screen" data-title="Folie operieren">
  <span class="eyebrow">Station 4 · Folie operieren</span>
  <h2>Was bleibt, was sagst du, was fliegt raus?</h2>
  <p class="lead">Hier ist die Folie aus Durchgang 1 noch einmal. Entscheide für jedes Element.</p>
  {IMG('b3-horrorfolie', 'Überladene Folie zum Wasserkreislauf')}
  <div id="makeList"></div>
  <div class="card reveal" id="makeAfter"><h3>So sieht das Ergebnis aus</h3>{IMG('b3-zwillingsfolie', 'Entschlackte Folie')}</div>
  {NEXT}
</section>

<section class="screen" data-title="Mein Material">
  <span class="eyebrow">Station 5 · Mein Material</span>
  <h2>Jetzt deine eigene Folie oder dein Arbeitsblatt.</h2>
  <p class="lead">Nimm ein Material, das du in den nächsten zwei Wochen einsetzt. Am besten das, bei dem du schon ahnst, dass es zu voll ist.</p>
  <div class="card">
    <div class="field" style="margin-top:0"><label for="matWas">Welches Material? <span class="sub">Fach, Klasse, Thema</span></label><input type="text" id="matWas" data-store="matWas" placeholder="…"></div>
    <div class="field"><label for="matGedanke">Der eine Gedanke dieser Folie oder dieses Blatts</label><input type="text" id="matGedanke" data-store="matGedanke" placeholder="Wenn sich kein einzelner Gedanke nennen lässt, sind es zwei Folien."></div>
    <h3 style="margin-top:1rem">Checkliste</h3>
    <div id="matList"></div>
    <div class="field"><label for="matRaus">Was fliegt raus, was sage ich stattdessen?</label><textarea id="matRaus" data-store="matRaus" placeholder="…"></textarea></div>
  </div>
  {NEXT}
</section>
"""
M32["js"] = r"""
const TICK=['„Der Wasserkreislauf beschreibt den ständigen Transport und die Speicherung von Wasser …“ (die Lehrkraft liest den Folientext vor)','„Übrigens: 86 Prozent der Verdunstung stammen aus den Ozeanen.“','„… wobei das Wasser in der Atmosphäre aufsteigt und dort abkühlt …“','„Und merkt euch: Ein Wassertropfen bleibt im Schnitt etwa neun Tage in der Luft.“','„… bis es als Niederschlag wieder zur Erde fällt, versickert oder abfließt …“','„… sodass man zusammenfassend auch von Evapotranspiration spricht.“'];
const R1=[
 {t:'Welche Station folgt auf die Kondensation?',ok:1,note:'Niederschlag.',opts:null},
 {t:'Wie viel Prozent der Verdunstung stammen aus den Ozeanen?',ok:2,note:'86 %. Die Zahl wurde nur gesagt und stand nirgends.'},
 {t:'Wie lange bleibt Wasser im Schnitt in der Luft?',ok:1,note:'Etwa neun Tage. Auch das wurde nur gesagt.'}
];
const R1_OPTS=[['Verdunstung','Niederschlag','Abfluss','Versickerung'],['56 %','71 %','86 %','93 %'],['2 Tage','9 Tage','3 Wochen','40 Tage']];
const R2=[
 {t:'Welche Station kommt direkt vor dem Niederschlag?',ok:0,note:'Kondensation.'},
 {t:'Woher stammt der größte Teil der Verdunstung?',ok:2,note:'Aus den Ozeanen, 86 %. Die Zahl stand am Pfeil.'},
 {t:'Wofür steht die Angabe „etwa 9 Tage“?',ok:3,note:'Für die Zeit, die Wasser im Schnitt in der Luft bleibt.'}
];
const R2_OPTS=[['Kondensation','Abfluss','Verdunstung','Versickerung'],['aus Flüssen','von Landflächen','aus den Ozeanen','von Pflanzen'],['Dauer eines ganzen Kreislaufs','Zeit bis zum Versickern','Dauer der Verdunstung','Zeit in der Luft']];
const QUEL_OPTS=['Split Attention','Redundanz','Transienz'];
const QUEL=[
 {t:'Die Hausaufgabe wird beim Einpacken in den Raum gerufen.',ok:2,note:'Gesprochenes ist sofort weg. Sie gehört an die Tafel, bevor eingepackt wird.'},
 {t:'Du liest den Merksatz vor, der an der Tafel steht.',ok:1,note:'Dasselbe doppelt. Lass ihn still lesen oder sag ihn, ohne dass er dasteht.'},
 {t:'Die Klasse schreibt das Tafelbild ab, während du den nächsten Schritt erklärst.',ok:0,note:'Zwei Dinge gleichzeitig. Erst zuhören, dann abschreiben (M2.3).'},
 {t:'Die Legende steht auf Seite 12, die Karte auf Seite 13.',ok:0,note:'Was zusammengehört, muss beieinanderstehen. Beschrifte direkt in der Karte.'},
 {t:'Drei Arbeitsschritte, nur mündlich angesagt. Nach dem ersten fragt jemand: „Was sollten wir noch mal?“',ok:2,note:'Ab zwei Schritten schriftlich.'},
 {t:'Das Arbeitsblatt erklärt die Grafik noch einmal in einem langen Absatz, obwohl die Grafik für sich verständlich ist.',ok:1,note:'Der Absatz bringt nichts Neues und muss trotzdem verarbeitet werden.'}
];
const MAKE_OPTS=['bleibt auf der Folie','sage ich','streichen'];
const MAKE=[
 {t:'Der Titel „Der Wasserkreislauf – Grundlagen, Teilprozesse und Sonderfälle im Überblick“',ok:0,note:'Bleibt, gekürzt auf „Der Wasserkreislauf“.'},
 {t:'Die elf Zeilen Fließtext',ok:1,note:'Das ist deine Erklärung. Sie gehört in deinen Mund, nicht auf die Folie.'},
 {t:'Das kleine Kreislauf-Diagramm unten rechts',ok:0,note:'Bleibt und wird groß. Es ist der Träger der Folie.'},
 {t:'Die Namen der vier Stationen',ok:0,note:'Als Beschriftung direkt im Diagramm.'},
 {t:'Die Zahlen 86 % und 9 Tage',ok:0,note:'Als Beschriftung an den Pfeilen. Nur gesagt wären sie sofort weg.'},
 {t:'Die Sonderfälle in drei Gliederungsebenen',ok:1,note:'Kurz erwähnen oder in eine spätere Stunde verschieben. Auf dieser Folie lenken sie vom Kreislauf ab.'},
 {t:'Die Sonne mit Sonnenbrille',ok:2,note:'Dekoration zieht Aufmerksamkeit ab.'},
 {t:'„Folie 7 von 43“',ok:2,note:'Trägt nichts zum Inhalt bei.'}
];
const MAT=['Ein Gedanke pro Folie oder Abschnitt','Träger gewählt: Bild oder Text, nicht beides gegeneinander','Nichts wird vorgelesen, was dasteht','Anweisungen ab zwei Schritten stehen schriftlich da','Die Kernschritte bleiben an der Tafel stehen','Dekoration ist entfernt'];
function moduleState(){return {r1:fill(3,-1),r2:fill(3,-1),r1Shown:false,r2Shown:false,quel:fill(QUEL.length,-1),make:fill(MAKE.length,-1),mat:fill(MAT.length,false)};}
function rounds(){
  R1.forEach((q,i)=>q.optsShort=R1_OPTS[i]);R2.forEach((q,i)=>q.optsShort=R2_OPTS[i]);
  [['r1',R1],['r2',R2]].forEach(([k,items])=>{
    const wrap=$(k+'List');wrap.innerHTML='';
    items.forEach((it,i)=>{
      const sel=state[k][i];const div=document.createElement('div');div.className='quiz-item';
      div.innerHTML='<p class="quiz-q" style="font-weight:500">'+it.t+'</p><div class="chip-row">'+it.optsShort.map((o,j)=>'<button class="cat-chip'+(sel>-1?(j===it.ok?' correct':(j===sel?' wrong':'')):'')+'" data-k="'+k+'" data-i="'+i+'" data-j="'+j+'"'+(sel>-1?' disabled':'')+'>'+o+'</button>').join('')+'</div>'+(sel>-1?'<p class="quiz-note on">'+(sel===it.ok?'✓ ':'✗ ')+it.note+'</p>':'');
      wrap.appendChild(div);
    });
    wrap.querySelectorAll('[data-k]').forEach(b=>b.addEventListener('click',()=>{state[b.dataset.k][+b.dataset.i]=+b.dataset.j;scheduleSave();rounds();renderSummary();}));
    if(state[k+'Shown'])$(k+'Stage').style.display='block';
  });
  const d1=state.r1.every(v=>v>-1),d2=state.r2.every(v=>v>-1);
  $('r2Btn').disabled=!d1||state.r2Shown;$('r1Btn').disabled=state.r1Shown;
  if(d1&&d2){
    const s=k=>state[k].reduce((a,v,i)=>a+(v===(k==='r1'?R1:R2)[i].ok?1:0),0);
    $('rResult').classList.add('on');
    $('rResult').innerHTML='<h3>Dein Ergebnis</h3><div class="result-row"><span>Durchgang 1 · überladene Folie, Text vorgelesen</span><b>'+s('r1')+' von 3</b></div><div class="result-row"><span>Durchgang 2 · ein Schaubild, frei erklärt</span><b>'+s('r2')+' von 3</b></div>'
      +'<p style="font-size:.92rem;margin-top:.7rem">In Durchgang 1 solltest du lesen, während jemand anderes sprach. Der Text wurde vorgelesen, den du schneller selbst gelesen hättest. Und die beiden Zahlen wurden nur gesagt. Deine Schüler erleben das täglich. Sie können nur nicht benennen, warum sie aussteigen.</p>'
      +'<p class="hint">Der zweite Durchgang war auch deshalb leichter, weil du den Inhalt schon einmal gesehen hattest. Aussagekräftiger ist deine eigene Einschätzung: Wie anstrengend war das Aufnehmen im Vergleich?</p>';
  }
}
function renderModule(){
  $('r1Btn').onclick=()=>{$('r1Btn').disabled=true;let i=0;$('r1Tick').textContent=TICK[0];const iv=setInterval(()=>{i++;if(i<TICK.length)$('r1Tick').textContent=TICK[i];else clearInterval(iv);},5000);
    timedShow('r1Box',30,()=>{state.r1Shown=true;scheduleSave();rounds();});};
  $('r2Btn').onclick=()=>{$('r2Btn').disabled=true;timedShow('r2Box',30,()=>{state.r2Shown=true;scheduleSave();rounds();});};
  rounds();
  pickList('quel','quelList',QUEL,QUEL_OPTS);pickList('make','makeList',MAKE,MAKE_OPTS);
  checkList('mat','matList',MAT);
  if(pickDone('make')===MAKE.length)$('makeAfter').classList.add('on');
}
const _renderPick=renderPick;
renderPick=function(key){_renderPick(key);if(key==='make'&&pickDone('make')===MAKE.length)$('makeAfter').classList.add('on');};
function ROWS(){
  const d=state.r1.concat(state.r2).filter(v=>v>-1).length;
  return [['Versuch',d===6?'✓ beide Durchgänge':d+'/6 Fragen',d===6],pickRow('Drei Quellen','quel'),pickRow('Folie operieren','make'),['Mein Material',val('matWas')?'✓ '+state.mat.filter(Boolean).length+'/'+MAT.length+' Punkte erfüllt':'noch offen',!!val('matWas')]];
}
function SECTIONS(){
  const s=(k,R)=>state[k].reduce((a,v,i)=>a+(v===R[i].ok?1:0),0);
  return [['Versuch','Durchgang 1: '+s('r1',R1)+' von 3, Anstrengung '+(val('r1Muehe')||'–')+'\nDurchgang 2: '+s('r2',R2)+' von 3, Anstrengung '+(val('r2Muehe')||'–')],
    ['Übungen',pickText('Drei Quellen','quel')+'\n'+pickText('Folie operieren','make')],
    ['Mein Material',fld('Material','matWas')+'\n'+fld('Der eine Gedanke','matGedanke')+'\nCheckliste: '+state.mat.filter(Boolean).length+' von '+MAT.length+' Punkten\n'+fld('Was rausfliegt','matRaus')]];
}
"""

# ============================================================ Modul 3.3
M33 = dict(
    n="3.3", skript="3-3", key="modul3-3-aufmerksamkeit", file="Modul3-3_Aufmerksamkeit_SPA.html", title="Aufmerksamkeit lenken",
    frage="Wie stelle ich sicher, dass alle über das Richtige nachdenken?",
    lead="Erinnert wird, worüber nachgedacht wurde. Die Frage ist also, worauf deine Schüler achten, wenn du „Schaut mal“ sagst. Ein Versuch zeigt dir, worauf du selbst achtest.",
    weg="Nach dem Abruf machst du einen kurzen Versuch mit einer Folie. Dann lernst du drei Hebel kennen, mit denen sich Aufmerksamkeit lenken lässt, sortierst Aufträge und prüfst Aufgaben darauf, ob sie den Zielgedanken wirklich verlangen. Du schreibst drei Sätze für deine nächste Stunde. Am Ende startet ein Selbstversuch, der bis zum nächsten Input läuft.",
    min=25, quellen="McCrea, Memorable Teaching · Willingham · Forschung zu „seductive details“",
    steps=[
        {"id": "auftrag", "label": "Standard · Beachtungsauftrag", "text": "Vor jedem Medium (Grafik, Text, Video, Versuch) gebe ich einen konkreten Auftrag, der sich abhaken lässt. Nie nur „Schaut mal“."},
        {"id": "pruefen", "label": "Alternative 1 · Aufgaben prüfen", "text": "Ich prüfe jede selbst gestellte Aufgabe mit der Frage „Was muss man denken, um sie zu lösen?“ und baue pro Tag eine um."},
        {"id": "koppeln", "label": "Alternative 2 · Koppeln", "text": "Jedes spannende Element (Anekdote, Video, Versuch) bekommt einen Auftrag, der zum Konzept führt."},
    ],
    log_title="Meine Beachtungsaufträge", log_label="Stunde",
    log_hint="Notiere drei Aufträge wörtlich und was du beobachtet hast. Die zwei besten hebst du auf.",
    log_fields=[{"f": "med", "label": "Medium", "ph": "z. B. Diagramm"}, {"f": "auf", "label": "mein Auftrag, wörtlich", "ph": "…"}, {"f": "wirk", "label": "was ich beobachtet habe", "ph": "…"}],
    exit=["Wo meine Schüler bisher auf das Falsche achten:", "Eine Aufgabe, die ich umbauen werde:"],
    ausblick="„Beim nächsten Input geht es um die stärkste Lernaktivität, die wir kennen: sich erinnern müssen. Dein Selbstversuch läuft bis dahin. Halte dich an deine drei Termine, und sprich mit niemandem über die zehn Begriffe.“",
    fixed=["exp", "auft", "roe"],
)
M33["screens"] = f"""
<section class="screen" data-title="Ein Versuch">
  <span class="eyebrow">Station 2 · Ein Versuch</span>
  <h2>Schau dir diese Folie aufmerksam an.</h2>
  <p class="lead">Sie stammt aus einer Biologiestunde. Du hast 20 Sekunden.</p>
  <div class="card">
    <p style="margin-top:0"><button class="btn small" id="expBtn">Folie 20 Sekunden zeigen</button></p>
    <div class="stagebox" id="expBox">{IMG('b3-experimentfolie', 'Folie aus einer Biologiestunde')}<p class="hint">noch <span class="count">20</span> Sekunden</p></div>
    <div class="stagebox" id="expStage"><div id="expList"></div></div>
  </div>
  <div class="card reveal" id="expResult"></div>
  {NEXT}
</section>

<section class="screen" data-title="Drei Hebel">
  <span class="eyebrow">Station 3 · Drei Hebel</span>
  <h2>Wer nicht lenkt, überlässt es dem Zufall.</h2>
  <p class="lead">Aufmerksamkeit entscheidet, was überhaupt im Arbeitsgedächtnis ankommt. Sie hat Vorlieben: Neues vor Bekanntem, Bewegtes vor Stillem, Witziges vor Wichtigem, Menschen vor Sachen.</p>
  <div class="formula-card"><h4>1 · Der Beachtungsauftrag vor jedem Medium</h4><p style="margin-top:0">Konkret und abhakbar, und er kommt <em>vor</em> dem Zeigen. Statt „Schaut auf die Grafik“: „Vergleicht die Balken von Gehirn und Herz. Um welchen Faktor unterscheiden sie sich?“</p></div>
  <div class="formula-card"><h4>2 · Markierungen im Vortrag</h4><p style="margin-top:0">„Der wichtigste Satz der Stunde kommt jetzt.“ · „Das ist der häufigste Fehler in der Arbeit.“ · „Erstens, zweitens, drittens.“ Dazu die Pause davor und die Stimme nach unten (M1.4). Und ein festes Layout: Steht die Merkregel immer im selben Kasten, wird sie gefunden.</p></div>
  <div class="formula-card"><h4>3 · Aufgaben, die den Zielgedanken verlangen</h4><p style="margin-top:0">Die verlässlichste Lenkung ist eine Aufgabe, die sich nur lösen lässt, wenn man über den Inhalt nachdenkt. Die Prüffrage: <strong>Was muss man denken, um sie zu lösen, und geht es auch ohne?</strong></p></div>
  <div class="scene"><span class="tag">Der Fall aus Modul 3.1</span>Nach dem spektakulären Filmeinstieg kennen alle den Film und keiner das Konzept. Die falsche Konsequenz wäre, Filme und Anekdoten zu streichen. Die richtige: <strong>koppeln</strong>. „Dieses Video ist ein Beispiel für Prinzip X. Erklärt danach zu zweit, wo genau.“ Das Spannende darf bleiben, es muss nur für das Konzept arbeiten.</div>
  <h3 style="margin-top:1.4rem">Lenkt dieser Auftrag?</h3>
  <div id="auftList"></div>
  {NEXT}
</section>

<section class="screen" data-title="Aufgaben prüfen">
  <span class="eyebrow">Station 4 · Aufgaben prüfen</span>
  <h2>Was muss man denken, um das zu lösen?</h2>
  <p class="lead">Sechs Aufgaben aus sechs Fächern. Entscheide, ob der Zielgedanke nötig ist. Wo es ohne geht, zeigt die Rückmeldung einen Umbau. Oft genügt ein kleiner Dreh: begründe, entscheide, vergleiche, was wäre, wenn.</p>
  <div id="roeList"></div>
  <div class="card">
    <h3>Eine eigene Aufgabe</h3>
    <div class="field" style="margin-top:.4rem"><label for="aufAlt">Eine Aufgabe, die ich demnächst stelle</label><textarea id="aufAlt" data-store="aufAlt" placeholder="wörtlich"></textarea></div>
    <div class="field"><label for="aufDenk">Was muss man denken, um sie zu lösen? Geht es auch ohne?</label><input type="text" id="aufDenk" data-store="aufDenk" placeholder="…"></div>
    <div class="field"><label for="aufNeu">Umgebaut <span class="sub">nur falls nötig</span></label><textarea id="aufNeu" data-store="aufNeu" placeholder="…"></textarea></div>
  </div>
  {NEXT}
</section>

<section class="screen" data-title="Drei Sätze für morgen">
  <span class="eyebrow">Station 5 · Drei Sätze für morgen</span>
  <h2>Schreib sie wörtlich auf.</h2>
  <p class="lead">Für eine echte Stunde der nächsten Woche. Wörtlich, weil du sie sonst im Moment doch wieder durch „Schaut mal“ ersetzt.</p>
  <div class="card">
    <div class="field" style="margin-top:0"><label for="mkMed">Mein Medium <span class="sub">Grafik, Text, Video, Versuch</span></label><input type="text" id="mkMed" data-store="mkMed" placeholder="…"></div>
    <div class="field"><label for="mkAuf">Mein Beachtungsauftrag davor</label><textarea id="mkAuf" data-store="mkAuf" placeholder="z. B. „Zählt mit, wie oft … und notiert, was direkt davor passiert.“"></textarea></div>
    <label class="self-check"><input type="checkbox" data-store="mkCheck"><span>Der Auftrag lässt sich abhaken: Man kann danach sagen, ob er erledigt ist.</span></label>
    <div class="field"><label for="mkKern">Der Kernsatz der Stunde und wie ich ihn ankündige</label><textarea id="mkKern" data-store="mkKern" placeholder="z. B. „Wenn ihr einen Satz mitnehmt, dann diesen: …“"></textarea></div>
    <div class="field"><label for="mkKop">Mein spannendes Element und der Auftrag, der es ans Konzept koppelt <span class="sub">falls vorhanden</span></label><textarea id="mkKop" data-store="mkKop" placeholder="z. B. „Der Versuch zeigt Regel Y. Formuliert danach, warum.“"></textarea></div>
  </div>
  {NEXT}
</section>

<section class="screen" data-title="Selbstversuch">
  <span class="eyebrow">Station 6 · Selbstversuch bis zum nächsten Input</span>
  <h2>Zehn Begriffe, sechs Minuten, drei Tage.</h2>
  <p class="lead">Die Hälfte der Gruppe lernt nach Verfahren A, die andere nach Verfahren B. Beim nächsten Input wird verglichen. Bitte halte dich genau an dein Verfahren und sprich mit niemandem über die Begriffe.</p>
  <div class="formula-card" id="grpCard"></div>
  <div class="card">
    <p style="margin-top:0"><button class="btn ghost small" id="hideBtn">Erklärungen verdecken</button></p>
    <div id="termList" style="margin-top:.5rem"></div>
  </div>
  <div class="card">
    <h3>Meine drei Termine</h3>
    <label class="self-check"><input type="checkbox" data-store="expT1"><span>Tag 1 erledigt (2 Minuten)</span></label>
    <label class="self-check"><input type="checkbox" data-store="expT2"><span>Tag 2 erledigt (2 Minuten)</span></label>
    <label class="self-check"><input type="checkbox" data-store="expT3"><span>Tag 3 erledigt (2 Minuten)</span></label>
    <div class="field"><label for="expGefuehl">Wie hat sich das Lernen angefühlt? <span class="sub">Ein Satz, nach dem dritten Termin.</span></label><input type="text" id="expGefuehl" data-store="expGefuehl" placeholder="…"></div>
  </div>
  {NEXT}
</section>
"""
M33["js"] = f"""
const TERMS={js(TERMS)};
const EXP_OPTS=[['Leber','Gehirn','Muskeln','Herz'],['Kilokalorien pro Tag','% des Grundumsatzes','Watt','Gramm Glukose'],['Es stemmte eine Hantel','Es las ein Buch','Es schlief','Es rannte']];
const EXP=[{{t:'Welches Organ hatte den zweithöchsten Verbrauch?',ok:1,note:'Das Gehirn mit 19 %.'}},{{t:'Was stand an der senkrechten Achse?',ok:1,note:'„% des Grundumsatzes“.'}},{{t:'Was tat das Cartoon-Gehirn?',ok:0,note:'Es stemmte eine Hantel („Leg day!“).'}}];
const AUFT_OPTS=['lenkt','überlässt es dem Zufall'];
const AUFT=[
 {{t:'„Schaut euch die Grafik genau an.“',ok:1,note:'Worauf? Das bleibt offen.'}},
 {{t:'„Vergleicht die Balken von Gehirn und Herz: Um welchen Faktor unterscheiden sie sich?“',ok:0,note:'Konkret und abhakbar.'}},
 {{t:'„Lest den Text aufmerksam.“',ok:1,note:'Aufmerksam worauf?'}},
 {{t:'„Unterstreicht die zwei Stellen, an denen der Autor seine These abschwächt.“',ok:0,note:'Man muss die These verstanden haben, um die Stellen zu finden.'}},
 {{t:'„Achtet beim Video auf das Wichtigste.“',ok:1,note:'Was wichtig ist, wissen die Schüler vorher nicht.'}},
 {{t:'„Zählt mit, wie oft sich die Zelle teilt, und notiert, was direkt davor passiert.“',ok:0,note:'Zwei klare Dinge, die man danach vorweisen kann.'}},
 {{t:'„Passt beim Versuch gut auf.“',ok:1,note:'Alle passen auf, nur jeder auf etwas anderes.'}},
 {{t:'„Notiert die Farbe der Flamme, bevor und nachdem ich das Salz dazugebe.“',ok:0,note:'Der Blick liegt dort, wo das Konzept sichtbar wird.'}}
];
const ROE_OPTS=['Zielgedanke nötig','geht auch ohne'];
const ROE=[
 {{tag:'Geschichte',t:'„Lies den Abschnitt und nenne drei Folgen der Industrialisierung.“',ok:1,note:'Lösbar durch Abschreiben der Aufzählung. Umbau: „… und ordne sie: Welche Folge wiegt heute am schwersten? Begründe in zwei Sätzen.“'}},
 {{tag:'Mathematik',t:'„Entscheide, ohne zu rechnen: Ist 4/7 + 3/8 größer oder kleiner als 1? Begründe.“',ok:0,note:'Verlangt eine Vorstellung von der Größe der Brüche.'}},
 {{tag:'Deutsch',t:'„Unterstreiche alle Adjektive im Text.“',ok:1,note:'Suche nach äußeren Merkmalen. Umbau: „Ersetze drei Adjektive so, dass die Stimmung kippt, und erkläre die Wirkung.“'}},
 {{tag:'Englisch',t:'„Yesterday, last week, since 2020, already: Ordne die Signalwörter den Zeitformen zu und schreibe zu zwei davon je einen eigenen Satz.“',ok:0,note:'Zuordnen und anwenden.'}},
 {{tag:'Physik',t:'„Zeichne den Stromkreis so um, dass Lampe 2 auch leuchtet, wenn Lampe 1 kaputt ist.“',ok:0,note:'Ohne das Prinzip der Parallelschaltung nicht lösbar.'}},
 {{tag:'Politik',t:'„Fasse den Zeitungsartikel zusammen.“',ok:1,note:'Ein Grenzfall: Ohne Fokus entsteht oft ein gekürzter Abschrieb. Umbau: „Fasse in 25 Wörtern zusammen und nenne die eine Information, die der Überschrift widerspricht.“'}}
];
function moduleState(){{return {{exp:fill(3,-1),expShown:false,auft:fill(AUFT.length,-1),roe:fill(ROE.length,-1),expGroup:'',hideDef:false}};}}
function expRender(){{
  const wrap=$('expList');wrap.innerHTML='';
  EXP.forEach((it,i)=>{{
    const sel=state.exp[i];const div=document.createElement('div');div.className='quiz-item';
    div.innerHTML='<p class="quiz-q" style="font-weight:500">'+it.t+'</p><div class="chip-row">'+EXP_OPTS[i].map((o,j)=>'<button class="cat-chip'+(sel>-1?(j===it.ok?' correct':(j===sel?' wrong':'')):'')+'" data-i="'+i+'" data-j="'+j+'"'+(sel>-1?' disabled':'')+'>'+o+'</button>').join('')+'</div>'+(sel>-1?'<p class="quiz-note on">'+(sel===it.ok?'✓ ':'✗ ')+it.note+'</p>':'');
    wrap.appendChild(div);
  }});
  wrap.querySelectorAll('[data-i]').forEach(b=>b.addEventListener('click',()=>{{state.exp[+b.dataset.i]=+b.dataset.j;scheduleSave();expRender();renderSummary();}}));
  if(state.expShown){{$('expStage').style.display='block';$('expBtn').disabled=true;}}
  if(state.exp.every(v=>v>-1)){{
    const fach=(state.exp[0]===1?1:0)+(state.exp[1]===1?1:0),cart=state.exp[2]===0;
    $('expResult').classList.add('on');
    $('expResult').innerHTML='<h3>Wohin deine Aufmerksamkeit lief</h3><div class="result-row"><span>Fragen zum Diagramm</span><b>'+fach+' von 2</b></div><div class="result-row"><span>Frage zum Cartoon</span><b>'+(cart?'gewusst':'nicht gewusst')+'</b></div>'
      +'<p style="font-size:.92rem;margin-top:.7rem">Die meisten wissen genau, was das Gehirn tat, und kaum jemand kennt die Achsenbeschriftung. Du warst aufmerksam, nur nicht auf die Achsen. Deine Schüler sind nicht unaufmerksamer als du. Ihre Aufmerksamkeit ist nur genauso eigensinnig. „Schaut euch das genau an“ ist deshalb keine Lenkung.</p>';
  }}
}}
function termRender(){{
  if(!state.expGroup){{state.expGroup=Math.random()<0.5?'A':'B';scheduleSave();}}
  const A=state.expGroup==='A';
  $('grpCard').innerHTML='<h4>Du bist in Gruppe '+state.expGroup+'</h4>'+(A
    ?'<p style="margin-top:0"><strong>Verfahren A · Lesen.</strong> An drei verschiedenen Tagen liest du die Liste jeweils zwei Minuten lang aufmerksam durch. Nicht abfragen, nicht abdecken.</p>'
    :'<p style="margin-top:0"><strong>Verfahren B · Abfragen.</strong> An Tag 1 liest du die Liste zwei Minuten lang. An Tag 2 und Tag 3 verdeckst du die Erklärungen, sagst sie dir zwei Minuten lang selbst auf und kontrollierst danach kurz.</p>')
    +'<p class="hint">Beide Gruppen lernen genau sechs Minuten. Stell dir für jeden Termin einen Wecker auf zwei Minuten.</p>';
  $('termList').className=state.hideDef?'hide-def':'';
  $('termList').innerHTML=TERMS.map(t=>'<div class="term"><b>'+t[0]+'</b><span>'+t[1]+'</span></div>').join('');
  $('hideBtn').style.display=A?'none':'';
  $('hideBtn').textContent=state.hideDef?'Erklärungen zeigen':'Erklärungen verdecken';
  $('hideBtn').onclick=()=>{{state.hideDef=!state.hideDef;scheduleSave();termRender();}};
}}
function renderModule(){{
  $('expBtn').onclick=()=>{{$('expBtn').disabled=true;timedShow('expBox',20,()=>{{state.expShown=true;scheduleSave();expRender();}});}};
  expRender();termRender();
  pickList('auft','auftList',AUFT,AUFT_OPTS);pickList('roe','roeList',ROE,ROE_OPTS);
}}
function ROWS(){{
  const e=state.exp.filter(v=>v>-1).length,t=[state.expT1,state.expT2,state.expT3].filter(Boolean).length;
  return [['Versuch',e===3?'✓ ausgewertet':e+'/3',e===3],pickRow('Aufträge','auft'),pickRow('Aufgaben prüfen','roe'),
    ['Drei Sätze für morgen',val('mkAuf')?'✓ geschrieben':'noch offen',!!val('mkAuf')],['Selbstversuch (Gruppe '+(state.expGroup||'–')+')',t===3?'✓ drei Termine':t+'/3 Termine',t===3]];
}}
function SECTIONS(){{
  return [['Versuch','Fragen zum Diagramm: '+((state.exp[0]===1?1:0)+(state.exp[1]===1?1:0))+' von 2 · Cartoon: '+(state.exp[2]===0?'gewusst':'nicht gewusst')],
    ['Übungen',pickText('Aufträge','auft')+'\\n'+pickText('Aufgaben prüfen','roe')+'\\n'+fld('Eigene Aufgabe','aufAlt')+'\\n'+fld('Was man denken muss','aufDenk')+'\\n'+fld('Umgebaut','aufNeu')],
    ['Drei Sätze für morgen',fld('Medium','mkMed')+'\\n'+fld('Beachtungsauftrag','mkAuf')+'\\n'+fld('Kernsatz und Ankündigung','mkKern')+'\\n'+fld('Kopplung','mkKop')],
    ['Selbstversuch','Gruppe '+(state.expGroup||'–')+' · Termine: '+[state.expT1,state.expT2,state.expT3].filter(Boolean).length+' von 3\\n'+fld('Gefühl beim Lernen','expGefuehl')]];
}}
"""

MODS = [M31, M32, M33]
