from gen_core import IMG, js
from mods_a import TERMS, NEXT

# ============================================================ Modul 3.4
M34 = dict(
    n="3.4", skript="3-4", key="modul3-4-abruf", file="Modul3-4_Abruf_SPA.html", title="Abrufen schlägt Wiederlesen",
    frage="Warum ist Erinnern-Müssen die stärkste Lernaktivität?",
    lead="Seit Modul 1.2 beginnen deine Stunden mit einem Do Now, und jede Sitzung dieser Fortbildung mit einem Abruf. Heute bekommst du die Begründung dafür, gemessen an dir selbst.",
    weg="Nach dem Abruf löst du deinen Selbstversuch aus Modul 3.3 auf. Du erfährst, warum Abrufen wirkt und welche fünf Kriterien aus einem Quiz ein Lernwerkzeug machen. Du erkennst Verstöße in fünf Beispielen, lernst vier Formate kennen und baust ein Do Now nach dem 3-2-1-Muster für deine Klasse.",
    min=25, quellen="McCrea, Memorable Teaching · Lemov „Retrieval Practice“ · Brown u. a., Make It Stick",
    steps=[
        {"id": "donow", "label": "Standard · Do Now nach 3-2-1", "text": "Mein Do Now besteht ab sofort aus Abruffragen nach dem 3-2-1-Muster, und ich sage der Klasse: „Das ist Training, keine Prüfung. Fehler sind hier willkommen.“"},
        {"id": "dump", "label": "Alternative 1 · Alles aufschreiben", "text": "Vor jedem Themenwechsel schreiben alle fünf Minuten lang auf, was sie zum Thema wissen, und gleichen es danach ab."},
        {"id": "rede", "label": "Alternative 2 · Lernberatung", "text": "Ich erkläre meiner Klasse in fünf Minuten, warum Wiederlesen sich gut anfühlt und wenig bringt."},
    ],
    log_title="Wie die Klasse reagiert", log_label="Tag",
    log_hint="Notiere am ersten, dritten und fünften Tag, wie die Klasse auf das Quiz reagiert. Meist ändert es sich schnell.",
    log_fields=[{"f": "prod", "label": "wie viele schreiben wirklich", "ph": "z. B. 22 von 26"}, {"f": "reak", "label": "Reaktion der Klasse", "ph": "…"}, {"f": "aend", "label": "was ich anpasse", "ph": "…"}],
    exit=["Welches Format ich zuerst ausprobiere:", "Was mich an Quizzen ohne Note noch zweifeln lässt:"],
    ausblick="„Beim nächsten Input kommt die unbequemste Erkenntnis des Programms: Die Stunde, die sich am glattesten anfühlt, ist oft nicht die, aus der am meisten bleibt.“",
    fixed=["krit"],
)
M34["screens"] = f"""
<section class="screen" data-title="Der Test">
  <span class="eyebrow">Station 2 · Der Test</span>
  <h2>Zehn Begriffe aus dem Gedächtnis.</h2>
  <p class="lead">In Modul 3.3 hast du zehn Begriffe bekommen und sie an drei Tagen je zwei Minuten gelernt. Schreib jetzt auf, was du noch weißt. Ohne Nachschauen, zwei Minuten.</p>
  <div class="card">
    <div class="field" style="margin-top:0"><label for="expGroupSel">Meine Gruppe</label><select id="expGroupSel"><option value="">bitte wählen</option><option value="A">A · dreimal gelesen</option><option value="B">B · einmal gelesen, zweimal abgefragt</option><option value="X">Ich habe den Versuch nicht gemacht</option></select></div>
    <div class="field"><label for="expRecall">Die zehn Begriffe <span class="sub">einer pro Zeile oder mit Komma getrennt</span></label><textarea id="expRecall" data-store="expRecall" style="min-height:7em" placeholder="…"></textarea></div>
    <p style="margin-top:.7rem"><button class="btn small" id="recallBtn">Auswerten</button></p>
  </div>
  <div class="card reveal" id="recallRes"></div>
  {NEXT}
</section>

<section class="screen" data-title="Warum Abruf wirkt">
  <span class="eyebrow">Station 3 · Warum Abruf wirkt</span>
  <h2>Ein Quiz ist kein Test über das Lernen. Es ist das Lernen.</h2>
  <p class="lead">Wiederlesen legt die Information noch einmal daneben. Abrufen bahnt den Weg zu ihr. Und diesen Weg brauchen Schüler in der Klassenarbeit.</p>
  {IMG('b3-vergessenskurve', 'Vergessenskurve mit drei Abrufen')}
  <div class="scene"><span class="tag">Warum Schüler anders lernen</span>Sie lernen mit Textmarker und Wiederlesen, weil es sich gut anfühlt. Es fühlt sich gut an, weil der Text bekannt vorkommt, und das Gehirn verwechselt Wiedererkennen mit Können. Abrufen fühlt sich holprig an. Genau diese Mühe ist der Lerneffekt.</div>
  <div class="formula-card">
    <h4>Fünf Kriterien</h4>
    <ol class="q-legend">
      <li><b>1</b>Ohne Hilfsmittel: Heft zu, sonst ist es Nachlesen.</li>
      <li><b>2</b>Schriftlich und von allen: Nur wer selbst schreibt, ruft ab.</li>
      <li><b>3</b>Ohne Note: Mit Note werden Fehler versteckt. Sag es der Klasse ausdrücklich.</li>
      <li><b>4</b>Sofortige Auflösung: Sonst setzen sich Irrtümer fest. Am besten korrigieren die Schüler selbst.</li>
      <li><b>5</b>Regelmäßig: jede Stunde kurz, nicht einmal im Monat groß.</li>
    </ol>
    <p>Auch Anwenden ist Abruf: Wer ein Konzept in einer neuen Situation benutzt, holt es aus dem Gedächtnis und verknüpft es neu.</p>
  </div>
  <h3 style="margin-top:1.4rem">Welches Kriterium ist verletzt?</h3>
  <div id="kritList"></div>
  {NEXT}
</section>

<section class="screen" data-title="Vier Formate">
  <span class="eyebrow">Station 4 · Vier Formate</span>
  <h2>Vier Formate, die wenig Vorbereitung brauchen.</h2>
  <p class="lead">Die Fragen gibt es schon: Es sind deine Exit-Ticket-Aufgaben und die Prüfaufgaben zu deinen Mindestzielen aus Block 2.</p>
  <div class="two">
    <div class="card"><h3>Do-Now-Quiz</h3><p style="font-size:.9rem">Sechs Fragen nach dem 3-2-1-Muster, still, schriftlich, danach sofort die Auflösung. Passt an jeden Stundenanfang.</p></div>
    <div class="card"><h3>Alles aufschreiben</h3><p style="font-size:.9rem">„Schreibt drei Minuten lang alles auf, was ihr über … wisst.“ Danach Abgleich mit dem Heft: Was fehlte? Passt vor einem Themenwechsel.</p></div>
    <div class="card"><h3>Whiteboard-Runde</h3><p style="font-size:.9rem">Kurze Fragen, alle schreiben, „drei, zwei, eins, hoch“. Du siehst sofort, was sitzt. Passt mitten in die Stunde.</p></div>
    <div class="card"><h3>Vier Fragen zu einem Begriff</h3><p style="font-size:.9rem">Zu zweit: Was ist es? Warum heißt es so? Wozu dient es? Ein eigenes Beispiel? Passt für Fachbegriffe.</p></div>
  </div>
  <div class="field"><label for="fmtWahl">Welches Format passt zu welcher Situation in deinem Unterricht?</label><textarea id="fmtWahl" data-store="fmtWahl" placeholder="z. B. Whiteboard-Runde nach der Erklärung in der 7b"></textarea></div>
  {NEXT}
</section>

<section class="screen" data-title="Mein Do Now">
  <span class="eyebrow">Station 5 · Mein Do Now nach 3-2-1</span>
  <h2>Sechs Fragen für Montag.</h2>
  <p class="lead">Drei von gestern, zwei von letzter Woche, eine vom letzten Monat. Alle ohne Hilfsmittel lösbar. Warum die Staffelung über die Zeit so viel bringt, klärt das nächste Modul.</p>
  <div class="card">
    <div class="field" style="margin-top:0"><label for="dnKlasse">Klasse und Fach</label><input type="text" id="dnKlasse" data-store="dnKlasse" placeholder="…"></div>
    <div class="field"><label for="dn3">Drei Fragen von gestern</label><textarea id="dn3" data-store="dn3" placeholder="1. …&#10;2. …&#10;3. …"></textarea></div>
    <div class="field"><label for="dn2">Zwei Fragen von letzter Woche</label><textarea id="dn2" data-store="dn2" placeholder="1. …&#10;2. …"></textarea></div>
    <div class="field"><label for="dn1">Eine Frage vom letzten Monat <span class="sub">Ist sie wirklich so alt? Typisch ist, dass alles aus derselben Woche stammt.</span></label><input type="text" id="dn1" data-store="dn1" placeholder="…"></div>
    <label class="self-check"><input type="checkbox" data-store="dnAnw"><span>Mindestens eine Frage verlangt Anwenden, nicht nur Nennen.</span></label>
    <label class="self-check"><input type="checkbox" data-store="dnSatz"><span>Ich habe mir den Satz für die Klasse zurechtgelegt: „Das ist Training, keine Prüfung.“</span></label>
  </div>
  {NEXT}
</section>
"""
M34["js"] = f"""
const TERMS={js([t[0] for t in TERMS])};
const KRIT_OPTS=['mit Hilfsmittel','nicht von allen','mit Note','ohne Auflösung','nur gelegentlich'];
const KRIT=[
 {{t:'Beim Quiz dürfen die Schüler im Heft nachschlagen, „damit niemand frustriert ist“.',ok:0,note:'Dann wird nachgelesen. Besser: leichtere Fragen, Heft zu.'}},
 {{t:'Die Lehrkraft stellt fünf Fragen mündlich und nimmt jeweils einen Melder dran.',ok:1,note:'Abgerufen haben fünf Schüler. Alle schreiben, dann wird aufgelöst.'}},
 {{t:'Die Ergebnisse der Quizze fließen in die Mitarbeitsnote ein.',ok:2,note:'Ein einziges benotetes Quiz reicht, damit Fehler wieder versteckt werden.'}},
 {{t:'Die Zettel werden eingesammelt, die Lösungen gibt es in der nächsten Woche.',ok:3,note:'Bis dahin haben sich die falschen Antworten gefestigt.'}},
 {{t:'Einmal vor jeder Klassenarbeit gibt es ein großes Wiederholungsquiz.',ok:4,note:'Wirksam ist der kurze Abruf in jeder Stunde.'}}
];
function moduleState(){{return {{krit:fill(KRIT.length,-1),expGroup:'',recallN:-1}};}}
function norm(s){{return s.toLowerCase().replace(/[^a-z]/g,'');}}
function recallShow(){{
  $('expGroupSel').value=state.expGroup||'';
  if(state.recallN<0)return;
  const g=state.expGroup;
  $('recallRes').classList.add('on');
  $('recallRes').innerHTML='<h3>Dein Ergebnis: '+state.recallN+' von 10</h3>'
    +'<p style="font-size:.92rem">'+(g==='A'?'Du hast dreimal gelesen.':g==='B'?'Du hast einmal gelesen und dich zweimal abgefragt.':'Du hast ohne den Versuch geantwortet.')+' In der Sitzung vergleicht ihr die beiden Gruppen.</p>'
    +'<p style="font-size:.92rem">In Studien mit vielen Teilnehmenden behält die Gruppe, die sich abfragt, bei gleicher Lernzeit deutlich mehr. Das heißt Testing Effect. In einer kleinen Gruppe kann der Unterschied gering ausfallen oder fehlen; das widerlegt den Befund nicht.</p>'
    +'<p class="hint">Fehlende Begriffe: '+(TERMS.filter(t=>norm(state.expRecall||'').indexOf(norm(t))<0).join(', ')||'keine')+'</p>'
    +'<div class="field"><label for="expFeel">Falls du in Gruppe B warst: Wie hat sich das Abfragen im Vergleich zum Lesen angefühlt?</label><input type="text" id="expFeel" placeholder="…"></div>';
  const f=$('expFeel');f.value=state.expFeel||'';f.oninput=()=>{{state.expFeel=f.value;scheduleSave();}};
}}
function renderModule(){{
  $('expGroupSel').onchange=()=>{{state.expGroup=$('expGroupSel').value;scheduleSave();recallShow();}};
  $('recallBtn').onclick=()=>{{const a=norm($('expRecall').value);state.recallN=TERMS.filter(t=>a.indexOf(norm(t))>-1).length;scheduleSave();recallShow();renderSummary();}};
  recallShow();pickList('krit','kritList',KRIT,KRIT_OPTS);
}}
async function afterInit(){{
  if(state.expGroup)return;
  const prev=await loadOtherModule('modul3-3-aufmerksamkeit');
  if(prev&&prev.expGroup){{state.expGroup=prev.expGroup;scheduleSave();recallShow();}}
}}
function ROWS(){{
  return [['Test',state.recallN>-1?'✓ '+state.recallN+'/10 (Gruppe '+(state.expGroup||'–')+')':'noch offen',state.recallN>-1],pickRow('Kriterien','krit'),['Mein Do Now',val('dn3')&&val('dn1')?'✓ geschrieben':'noch offen',!!(val('dn3')&&val('dn1'))]];
}}
function SECTIONS(){{
  return [['Selbstversuch','Gruppe '+(state.expGroup||'–')+' · '+(state.recallN>-1?state.recallN+' von 10 Begriffen':'nicht ausgewertet')+'\\n'+fld('Gefühl beim Abfragen','expFeel')],
    ['Übungen',pickText('Kriterien','krit')+'\\n'+fld('Formate und Situationen','fmtWahl')],
    ['Mein Do Now',fld('Klasse','dnKlasse')+'\\nGestern: '+(val('dn3')||'–')+'\\nLetzte Woche: '+(val('dn2')||'–')+'\\nLetzter Monat: '+(val('dn1')||'–')]];
}}
"""

# ============================================================ Modul 3.5
M35 = dict(
    n="3.5", skript="3-5", key="modul3-5-verteilen-mischen", file="Modul3-5_Verteilen-Mischen_SPA.html", title="Verteilen und Mischen",
    frage="Wann sollte ich wiederholen, und warum ist es gut, wenn schon etwas vergessen wurde?",
    lead="Abrufen wirkt, das hast du an dir selbst gemessen. Heute geht es um den Zeitpunkt: verteilt statt am Stück, gemischt statt sortiert.",
    weg="Nach dem Abruf denkst du an deine beste Stunde der letzten Wochen und fragst dich, woran du sie gemessen hast. Du lernst den Unterschied zwischen Leistung in der Stunde und Lernen kennen, prüfst fünf Aussagen, baust ein Übungsblatt um und legst für drei eigene Themen fest, wann sie wiederkehren.",
    min=25, quellen="McCrea, Memorable Teaching · Bjork (erwünschte Erschwernisse) · Rohrer &amp; Pashler",
    steps=[
        {"id": "blatt", "label": "Standard · Alter Stoff auf dem Übungsblatt", "text": "Ich baue in mein nächstes Übungsblatt mindestens drei Aufgaben aus früheren Themen ein und kündige an: Ab jetzt enthält jede Klassenarbeit alten Stoff, geübt wird er in unseren Quizzen."},
        {"id": "karte", "label": "Alternative 1 · Landkarte", "text": "Ich stelle die Wiederholungs-Landkarte für mein Halbjahr fertig und bespreche sie im Coaching."},
        {"id": "ticket", "label": "Alternative 2 · Am Folgetag messen", "text": "Zwei Wochen lang beurteile ich Stunden nicht danach, wie glatt sie liefen, sondern nach dem Do Now am nächsten Tag."},
    ],
    log_title="Glatt gelaufen oder gelernt?", log_label="Stunde",
    log_hint="Vergleiche drei Stunden: dein Eindruck direkt danach und das Ergebnis am nächsten Tag.",
    log_fields=[{"f": "ein", "label": "mein Eindruck danach", "ph": "z. B. lief glatt"}, {"f": "tag", "label": "Do Now am Folgetag", "ph": "z. B. 11 von 26 sicher"}, {"f": "folg", "label": "was ich daraus schließe", "ph": "…"}],
    exit=["Das Thema, das bei mir nach der Einheit nie wieder auftaucht:", "Wie meine Klasse auf gemischte Aufgaben reagieren wird:"],
    ausblick="„Beim nächsten Input schließt Block 3: Wie Wissen sich vernetzt, statt sich zu stapeln. Und es ist der Meilenstein zum Ende des ersten Programmjahres. Bring dein Playbook mit und hab deine laufende Unterrichtseinheit im Kopf.“",
    fixed=["stim", "umb"],
)
M35["screens"] = f"""
<section class="screen" data-title="Deine beste Stunde">
  <span class="eyebrow">Station 2 · Deine beste Stunde</span>
  <h2>Woran hast du gemerkt, dass sie gut war?</h2>
  <p class="lead">Denk an die Stunde der letzten Wochen, nach der du dachtest: Heute lief es.</p>
  <div class="card">
    <div class="field" style="margin-top:0"><label for="best">Woran habe ich das festgemacht?</label><textarea id="best" data-store="best" placeholder="…"></textarea></div>
    <p style="margin-top:.7rem"><button class="btn ghost small" data-reveal="bestAfter">Weiter</button></p>
    <div class="reveal" id="bestAfter">
      <p style="font-size:.92rem;margin-top:.7rem">Vermutlich: Es lief flüssig. Die Aufgaben klappten, es gab wenig Fehler, das Tempo stimmte. Genau dieses Gefühl ist ein unzuverlässiger Zeuge.</p>
      {IMG('b3-paradox', 'Am Stück geübt gegen verteilt geübt: Ende der Stunde und Test nach vier Wochen')}
      <p style="font-size:.92rem;margin-top:.7rem">Zwei Klassen üben denselben Stoff gleich lang. Die eine am Stück, die andere in Portionen über Wochen. Am Ende der Stunde liegt die erste vorn. Vier Wochen später hat sich das Verhältnis umgekehrt. <strong>Leistung in der Stunde ist nicht Lernen.</strong> Was in der Stunde schwerer aussieht, kann langfristig besser wirken.</p>
    </div>
  </div>
  {NEXT}
</section>

<section class="screen" data-title="Verteilen und Mischen">
  <span class="eyebrow">Station 3 · Verteilen und Mischen</span>
  <h2>Was halb vergessen ist, lässt sich am besten üben.</h2>
  <div class="formula-card"><h4>Verteilen</h4><p style="margin-top:0">Wer nach einer Lücke abruft, muss sich mehr anstrengen, und genau das festigt. Du brauchst dafür keine Tabelle mit idealen Abständen. Zwei Regeln reichen:</p>
    <ol class="q-legend"><li><b>1</b>Jedes Quiz enthält alten Stoff. Mit 3-2-1 läuft das schon.</li><li><b>2</b>Jedes Übungsblatt besteht zu mindestens einem Viertel aus früheren Themen.</li></ol></div>
  <div class="formula-card"><h4>Mischen</h4><p style="margin-top:0">Zehnmal derselbe Aufgabentyp: Nach der dritten Aufgabe weiß die Hand, was zu tun ist. Auf einem gemischten Blatt muss man bei jeder Aufgabe erst entscheiden, welches Verfahren passt. Das ist die eigentliche Schwierigkeit in der Klassenarbeit, denn dort steht über keiner Aufgabe, welches Verfahren dran ist.</p></div>
  <div class="formula-card"><h4>Klassenarbeiten mit altem Stoff</h4><p style="margin-top:0">„Jede Klassenarbeit enthält Aufgaben aus früheren Themen.“ Dieser Satz verändert das Lernverhalten stärker als jede Lernberatung. Fair ist er nur, wenn er angekündigt ist und der alte Stoff in den Quizzen laufend geübt wird.</p></div>
  {IMG('b3-wiederholungslandkarte', 'Beispiel einer Wiederholungs-Landkarte für ein Halbjahr')}
  <h3 style="margin-top:1.4rem">Stimmt das?</h3>
  <div id="stimList"></div>
  {NEXT}
</section>

<section class="screen" data-title="Ein Blatt umbauen">
  <span class="eyebrow">Station 4 · Ein Blatt umbauen</span>
  <h2>Zehn Aufgaben, alle vom selben Typ.</h2>
  <p class="lead">Mathematik, Klasse 7: zehn lineare Gleichungen der Form ax + b = c, steigend im Schwierigkeitsgrad. Drei davon sollen durch Aufgaben aus früheren Themen ersetzt werden. Welche Aufgaben eignen sich, und wohin gehören sie?</p>
  <div id="umbList"></div>
  <div class="card">
    <h3>Wenn die Klasse protestiert</h3>
    <p class="hint">„Früher konnten wir das besser!“ Schreib deine Antwort in drei Sätzen: das Gefühl ernst nehmen, den Grund nennen, den Nutzen für die Arbeit zeigen.</p>
    <div class="field" style="margin-top:.5rem"><textarea id="protest" data-store="protest" placeholder="…"></textarea></div>
    <p style="margin-top:.6rem"><button class="btn ghost small" data-reveal="protestMuster">Muster anzeigen</button></p>
    <p class="quiz-note reveal" id="protestMuster">„Euch kommt das gemischte Blatt schwerer vor, und das stimmt. Beim alten Blatt wusste eure Hand ab der dritten Aufgabe, was zu tun ist. In der Arbeit steht aber über keiner Aufgabe, welches Verfahren dran ist. Genau das üben wir jetzt: erkennen, was dran ist. Es fühlt sich holpriger an und bleibt dafür.“</p>
  </div>
  {NEXT}
</section>

<section class="screen" data-title="Meine Landkarte">
  <span class="eyebrow">Station 5 · Meine Landkarte</span>
  <h2>Drei Themen, drei Wiederkehr-Punkte.</h2>
  <p class="lead">Nimm drei Kernthemen deines Halbjahres. Lege für jedes fest, wann es wieder auftaucht. Faustlinie: nach einer Woche, nach vier Wochen, nach zehn Wochen.</p>
  <div class="card">
    <div class="field" style="margin-top:0"><label for="lkKlasse">Klasse und Fach</label><input type="text" id="lkKlasse" data-store="lkKlasse" placeholder="…"></div>
    <div id="lkRows"></div>
    <div class="field"><label for="lkWaise">Ein Thema, das bisher nach seiner Einheit nie wieder auftaucht, und wo ich es einbaue</label><textarea id="lkWaise" data-store="lkWaise" placeholder="…"></textarea></div>
    <div class="field"><label for="lkAnk">Meine Ankündigung an die Klasse, wörtlich</label><textarea id="lkAnk" data-store="lkAnk" placeholder="z. B. „Ab jetzt enthält jede Klassenarbeit auch Aufgaben aus früheren Themen. Damit das fair ist, üben wir sie in jedem Do Now.“"></textarea></div>
  </div>
  {NEXT}
</section>
"""
M35["js"] = r"""
const STIM_OPTS=['stimmt','stimmt nicht'];
const STIM=[
 {t:'Wenn die Übungsphase fast fehlerfrei läuft, wurde in der Stunde gut gelernt.',ok:1,note:'Es zeigt die Leistung von heute. Ob es bleibt, zeigt erst der Abruf nach einer Lücke.'},
 {t:'Wiederholen lohnt sich am meisten, wenn schon etwas vergessen wurde.',ok:0,note:'Der schwerere Abruf festigt stärker.'},
 {t:'Für verteiltes Üben muss man die idealen Abstände genau berechnen.',ok:1,note:'Regelmäßige Quizze mit altem Stoff und gemischte Übungsblätter reichen.'},
 {t:'Gemischte Aufgaben trainieren, das passende Verfahren zu erkennen.',ok:0,note:'Das ist ihr Vorteil gegenüber sortierten Blättern.'},
 {t:'Ein Thema ist abgeschlossen, wenn die Klassenarbeit geschrieben ist.',ok:1,note:'Mit dem Abschluss der Einheit beginnt die Wiederholung.'}
];
const UMB=[
 {tag:'Position',t:'An welche Stelle des Blatts gehört die erste Aufgabe aus einem früheren Thema?',ok:1,note:'Erst zwei, drei Aufgaben im neuen Typ zum Hineinkommen, dann mischen.',opts:['An die erste Stelle, zum Aufwärmen','Frühestens an die vierte Stelle','Ans Ende, als Zusatz']},
 {tag:'Kandidat',t:'„Vereinfache: 3x + 5 + 2x − 1“ (Terme, kein Gleichheitszeichen)',ok:0,note:'Sieht ähnlich aus und verlangt etwas anderes. Die Unterscheidung ist die Übung.',opts:['gut geeignet','weniger geeignet']},
 {tag:'Kandidat',t:'„Lisa ist doppelt so alt wie Tom, zusammen sind sie 36. Wie alt ist Tom?“ (Textaufgabe)',ok:0,note:'Muss erst in eine Gleichung übersetzt werden. Man muss erkennen, dass eine Gleichung gebraucht wird.',opts:['gut geeignet','weniger geeignet']},
 {tag:'Kandidat',t:'„Berechne den Flächeninhalt eines Rechtecks mit a = 4 cm und b = 7 cm.“',ok:1,note:'Wiederholung ja, aber keine Verwechslungsgefahr mit Gleichungen. Besser im Do Now aufgehoben.',opts:['gut geeignet','weniger geeignet']},
 {tag:'Kandidat',t:'„Berechne: 3/4 + 2/3“ (Bruchrechnung)',ok:0,note:'Ein Klassiker, der in Gleichungen mit Brüchen wieder gebraucht wird.',opts:['gut geeignet','weniger geeignet']}
];
function moduleState(){return {stim:fill(STIM.length,-1),umb:fill(UMB.length,-1)};}
function lkRender(){
  $('lkRows').innerHTML=[1,2,3].map(i=>'<div class="plan-row c-petrol"><div class="q">Thema '+i+'</div>'
    +'<div class="field"><input type="text" data-lk="lkT'+i+'" placeholder="Thema"></div>'
    +'<div class="field"><input type="text" data-lk="lkW'+i+'" placeholder="kehrt wieder: im Do Now am …, auf dem Übungsblatt …, in der Arbeit …"></div></div>').join('');
  document.querySelectorAll('[data-lk]').forEach(el=>{const k=el.dataset.lk;el.value=state[k]||'';el.oninput=()=>{state[k]=el.value;scheduleSave();renderSummary();};});
}
function renderModule(){pickList('stim','stimList',STIM,STIM_OPTS);pickList('umb','umbList',UMB,null);lkRender();}
function lkN(){return [1,2,3].filter(i=>val('lkT'+i)&&val('lkW'+i)).length;}
function ROWS(){
  return [['Beste Stunde',val('best')?'✓ notiert':'noch offen',!!val('best')],pickRow('Stimmt das?','stim'),pickRow('Blatt umbauen','umb'),['Meine Landkarte',lkN()===3?'✓ drei Themen':lkN()+'/3 Themen',lkN()===3]];
}
function SECTIONS(){
  return [['Meine beste Stunde',fld('Woran festgemacht','best')],
    ['Übungen',pickText('Stimmt das?','stim')+'\n'+pickText('Blatt umbauen','umb')+'\n'+fld('Antwort auf den Protest','protest')],
    ['Meine Landkarte',fld('Klasse','lkKlasse')+'\n'+[1,2,3].map(i=>'Thema '+i+': '+(val('lkT'+i)||'–')+' → '+(val('lkW'+i)||'–')).join('\n')+'\n'+fld('Bisher ohne Wiederkehr','lkWaise')+'\n'+fld('Ankündigung','lkAnk')]];
}
"""

# ============================================================ Modul 3.6
MATRIX = ["1 · Routinen & Stundenstart", "2 · Anweisungen & Aufmerksamkeit", "3 · Intervention & Präsenz", "4 · Erklären & Modellieren", "5 · Übungsphasen führen",
          "6 · Verstehen prüfen", "7 · Beteiligung & Fragenkultur", "8 · Planung & Arbeitsökonomie", "9 · Gedächtnis & Wiederholung", "10 · Motivation, Beziehung & Eltern"]
M36 = dict(
    n="3.6", skript="3-6", key="modul3-6-vernetzen", file="Modul3-6_Vernetzen_SPA.html", title="Wissen vernetzen · Abschluss Block 3",
    frage="Wie helfe ich Schülern, Wissen zu vernetzen, statt es zu stapeln?",
    lead="Abrufen bringt Wissen ins Langzeitgedächtnis, Verteilen hält es dort. Heute geht es darum, wie es dort liegt: als lose Fakten oder als Netz. Und Block 3 endet mit dem Meilenstein zum Ende des ersten Programmjahres.",
    weg="Du beginnst mit dem Block-3-Quiz, am besten vor der Sitzung. Dann lernst du fünf Fragetypen kennen, die Verknüpfung verlangen, prüfst Aufträge, vergleichst zwei Knowledge Organizer und baust einen eigenen für deine laufende Einheit. Du skizzierst zehn Minuten Lernberatung für deine Klasse und schätzt dich in der Kompetenzmatrix neu ein.",
    min=35, quellen="McCrea, Memorable Teaching · Lemov „Knowledge Organizers“ · Willingham",
    abruf_h="Block-3-Quiz: zwanzig Fragen, zurück bis Modul 1.1.",
    abruf_lead="Am besten vor der Sitzung. Beantworte jede Frage zuerst im Kopf oder auf einem Zettel, deck dann auf und bewerte ehrlich. In der Sitzung werden nur die Fragen besprochen, die am häufigsten nicht gewusst wurden.",
    steps=[
        {"id": "ko", "label": "Standard · Organizer und Lernberatung", "text": "Ich gebe meiner Klasse vor der nächsten Arbeit den Knowledge Organizer aus und zeige ihr in zehn Minuten, wie man damit lernt: abdecken, antworten, aufdecken."},
        {"id": "map", "label": "Alternative 1 · Mindmap mit beschrifteten Linien", "text": "Bei der nächsten Mindmap-Aufgabe muss an jeder Linie stehen, wie die Begriffe zusammenhängen."},
        {"id": "frage", "label": "Alternative 2 · Eine Verknüpfungsfrage pro Stunde", "text": "Jede Stunde endet mit einer Frage, die Verknüpfung verlangt (Warum? Worin anders als …? Eigenes Beispiel?)."},
    ],
    log_title="Was die Klasse daraus macht", log_label="Stunde",
    log_hint="Frag nach der Lernberatung per Whiteboard: „Wie lernt ihr jetzt für die Arbeit? Drei Stichworte.“ Notiere, was kommt.",
    log_fields=[{"f": "was", "label": "was ich eingesetzt habe", "ph": "z. B. Organizer + Lernberatung"}, {"f": "stich", "label": "Stichworte der Klasse", "ph": "…"}, {"f": "beob", "label": "was ich beobachtet habe", "ph": "…"}],
    exit=["Mein wertvollstes Konzept aus Block 3:", "Was ich meinen Schülern davon zuerst weitergebe:"],
    ausblick="„Damit endet das erste Programmjahr. Im Meilenstein-Gespräch legt dein Coach die Matrix aus Modul 0 neben die von heute. Nach den Sommerferien beginnt Block 4 mit der Frage, die sich durch alles zieht: Woher weiß ich während der Stunde, was in 28 Köpfen passiert?“",
    fixed=["verk", "kov", "ko", "matrix"],
)
M36["screens"] = f"""
<section class="screen" data-title="Vernetzen">
  <span class="eyebrow">Station 2 · Vernetzen</span>
  <h2>Gestapelt oder vernetzt?</h2>
  <p class="lead">Erinnere dich an die dreizehn Buchstaben aus Modul 3.1: Nur vernetztes Wissen lässt sich bündeln. Vernetzung entsteht, wenn Neues aktiv mit Bekanntem verknüpft wird.</p>
  <div class="formula-card">
    <h4>Fünf Fragen, die Verknüpfung verlangen</h4>
    <ol class="q-legend">
      <li><b>1</b>Warum ist das so?</li>
      <li><b>2</b>Worin unterscheidet sich X von Y?</li>
      <li><b>3</b>Nenne ein eigenes Beispiel.</li>
      <li><b>4</b>Erkläre es einem Fünftklässler.</li>
      <li><b>5</b>Was wäre, wenn …?</li>
    </ol>
    <p>Die Prüffrage an jeden solchen Auftrag: Muss man verknüpfen, oder genügt es, etwas wiederzugeben?</p>
  </div>
  <div class="formula-card"><h4>Beispiele und Gegenbeispiele nebeneinander</h4><p style="margin-top:0">Ein neuer Begriff ist am Anfang unscharf. Scharf wird er, wenn Schüler sehen, was sich ändern darf und was nicht: drei sehr verschiedene Dreiecke und zwei Figuren, die knapp keine sind. Ähnliche Begriffe (Fläche und Umfang) führst du erst getrennt ein und stellst sie später bewusst gegenüber.</p></div>
  {IMG('b3-mindmap', 'Dieselbe Mindmap ohne und mit beschrifteten Linien')}
  <p class="hint">Eine Mindmap vernetzt nur, wenn an den Linien steht, wie die Begriffe zusammenhängen.</p>
  <h3 style="margin-top:1.4rem">Muss man hier verknüpfen?</h3>
  <div id="verkList"></div>
  <div class="card">
    <h3>Zwei Fragen zu meinem aktuellen Thema</h3>
    <div class="field" style="margin-top:.4rem"><label for="vf1">Frage 1 <span class="sub">aus einem der fünf Typen</span></label><input type="text" id="vf1" data-store="vf1" placeholder="…"></div>
    <div class="field"><label for="vf2">Frage 2 <span class="sub">aus einem anderen Typ</span></label><input type="text" id="vf2" data-store="vf2" placeholder="…"></div>
  </div>
  {NEXT}
</section>

<section class="screen" data-title="Zwei Organizer">
  <span class="eyebrow">Station 3 · Zwei Organizer</span>
  <h2>Das Kernwissen einer Einheit auf einer Seite.</h2>
  <p class="lead">Ein Knowledge Organizer ist ein Auszug, kein Archiv. Gib ihn am besten schon zu Beginn der Einheit aus: Dann sehen alle, was kommt, und du kannst von der ersten Woche an daraus abfragen. Er dient dreifach: Schüler können sich damit abfragen, Schüler und Eltern sehen, was am Ende sitzen muss, und du merkst beim Schreiben, ob du den Kern kennst.</p>
  {IMG('b3-ko-gut', 'Gelungener Knowledge Organizer: Wasser als Stoff, Chemie Klasse 8')}
  <h3 style="margin-top:1.4rem">Und dieser?</h3>
  {IMG('b3-ko-ueberladen', 'Überladener Knowledge Organizer zur Weimarer Republik')}
  <div class="card"><h3>Was ist hier schiefgegangen? Kreuze an, was du findest.</h3><div id="kovList"></div>
    <p style="margin-top:.6rem"><button class="btn ghost small" data-reveal="kovAfter">Auflösung</button></p>
    <p class="quiz-note reveal" id="kovAfter">Alle fünf treffen zu. Der häufigste Grund ist die Sorge, etwas Wichtiges wegzulassen. Wer aber alles aufschreibt, hat nicht entschieden, was der Kern ist.</p>
  </div>
  <div class="formula-card"><h4>Gütecheck</h4><ol class="q-legend"><li><b>1</b>Eine Seite</li><li><b>2</b>Nur Kernwissen</li><li><b>3</b>Zum Abfragen geeignet: Erklärungen lassen sich abdecken</li><li><b>4</b>In Schülersprache</li></ol></div>
  {NEXT}
</section>

<section class="screen" data-title="Mein Organizer">
  <span class="eyebrow">Station 4 · Mein Organizer</span>
  <h2>Zehn Minuten für deine laufende Einheit.</h2>
  <p class="lead">Höchstens zwölf Begriffe. Was in zehn Minuten nicht aufs Blatt will, ist vermutlich kein Kernwissen. Wenn du fertig bist: Streich noch einen.</p>
  <div class="card">
    <div class="field" style="margin-top:0"><label for="koThema">Einheit, Fach, Klasse</label><input type="text" id="koThema" data-store="koThema" placeholder="…"></div>
    <p style="margin-top:.8rem;display:flex;gap:.6rem;align-items:center;flex-wrap:wrap"><button class="btn ghost small" id="koHideBtn">Erklärungen verdecken</button><span class="hint" id="koCount"></span></p>
    <div id="koRows"></div>
    <div class="field"><label for="koZus">Zwei bis drei Zusammenhänge <span class="sub">als Wenn-dann-Sätze oder Ursache und Wirkung</span></label><textarea id="koZus" data-store="koZus" placeholder="Wenn …, dann …"></textarea></div>
    <div class="field"><label for="koBild">Welches Schaubild gehört dazu?</label><input type="text" id="koBild" data-store="koBild" placeholder="z. B. Zeitstrahl mit sechs Marken"></div>
  </div>
  <div class="card"><h3>Härtetest</h3><p class="hint">Verdecke die Erklärungen und frag dich eine Minute lang selbst ab. Funktioniert das Blatt als Abfragewerkzeug?</p>
    <label class="self-check"><input type="checkbox" data-store="koTest"><span>Ja, jede Erklärung lässt sich aus dem Begriff heraus aufsagen.</span></label></div>
  {NEXT}
</section>

<section class="screen" data-title="Zehn Minuten Lernberatung">
  <span class="eyebrow">Station 5 · Zehn Minuten Lernberatung</span>
  <h2>Gib die Werkzeuge weiter.</h2>
  <p class="lead">Abrufen schlägt Wiederlesen, verteilt schlägt den Vorabend: Das gehört auch deinen Schülern. Sie lernen mit Textmarker und in Nachtschichten, weil ihnen niemand etwas anderes gezeigt hat.</p>
  <div class="card">
    <div class="plan-row c-rot"><div class="q">1 · Einstieg (2 Min.)</div><div class="field"><textarea data-store="rd1" placeholder="z. B. „Wer lernt mit Textmarker und Durchlesen? Das fühlt sich gut an. Und genau deshalb bringt es wenig. Ich zeige euch, warum.“"></textarea></div></div>
    <div class="plan-row c-gruen"><div class="q">2 · Selbstabfrage vormachen (4 Min.)</div><div class="field"><textarea data-store="rd2" placeholder="Organizer austeilen, rechte Spalte abdecken, zwei Schüler machen es vor: abdecken, antworten, aufdecken, Haken oder Kreis."></textarea></div></div>
    <div class="plan-row c-blau"><div class="q">3 · Der Wochenplan (2 Min.)</div><div class="field"><textarea data-store="rd3" placeholder="z. B. „Dreimal 15 Minuten, verteilt, bringen mehr als zwei Stunden am Vorabend.“"></textarea></div></div>
    <div class="plan-row c-gelb"><div class="q">4 · Prüfen, was ankam (2 Min.)</div><div class="field"><textarea data-store="rd4" placeholder="Whiteboards: „Wie lernst du jetzt für die Arbeit? Drei Stichworte.“"></textarea></div></div>
  </div>
  {NEXT}
</section>
"""
M36["after_quiz"] = [f"""
<section class="screen" data-title="Meilenstein Jahr 1">
  <span class="eyebrow">Station {{NR}} · Meilenstein zum Ende von Jahr 1</span>
  <h2>Kompetenzmatrix, zweite Erhebung.</h2>
  <p class="lead">Zehn Felder, vier Stufen, wie in Modul 0. Schätze den Normalfall deiner letzten Wochen ein. Dein Coach legt im Meilenstein-Gespräch beide Bögen nebeneinander.</p>
  <div class="card"><p class="hint" id="m0Hint">Wenn du Modul 0 in dieser App bearbeitet hast, erscheint dein damaliger Wert neben jedem Feld.</p><div id="matrixList"></div></div>
  <div class="card"><h3>Vor dem Meilenstein-Gespräch</h3>
    <label class="self-check"><input type="checkbox" data-store="msVideo"><span>Video-Selbstanalyse Nr. 2 ist aufgenommen und angesehen (Anleitung wie in Modul 1.7, Fokus aus Block 2 oder 3 frei wählbar).</span></label>
    <div class="field"><label for="msSieht">Was ich heute in meinem Unterricht sehe, das ich in Modul 1.7 noch nicht gesehen hätte</label><textarea id="msSieht" data-store="msSieht" placeholder="…"></textarea></div>
  </div>
  {NEXT}
</section>
"""]
M36["js"] = f"""
const MATRIX={js(MATRIX)};
const LEVELS=['Anfang','Grundlagen','sicher','flüssig'];
const VERK_OPTS=['verlangt Verknüpfung','Wiedergabe genügt'];
const VERK=[
 {{t:'„Nenne die drei Aggregatzustände.“',ok:1,note:'Reines Nennen. Als Abruf in Ordnung, vernetzt aber nichts.'}},
 {{t:'„Warum schwimmt Eis auf Wasser, obwohl beides derselbe Stoff ist?“',ok:0,note:'Man muss Dichte und Aggregatzustand zusammenbringen.'}},
 {{t:'„Worin unterscheidet sich eine Metapher von einem Vergleich? Gib je ein eigenes Beispiel.“',ok:0,note:'Abgrenzen und selbst erzeugen.'}},
 {{t:'„Erstellt eine Mindmap zur Weimarer Republik.“',ok:1,note:'Ohne beschriftete Linien genügt es, Begriffe aufzuschreiben und zu verbinden.'}},
 {{t:'„Was wäre mit den Jahreszeiten, wenn die Erdachse nicht geneigt wäre?“',ok:0,note:'Die Veränderung prüft, ob der Zusammenhang verstanden ist.'}},
 {{t:'„Schreibe die Definition aus dem Buch ab und lerne sie.“',ok:1,note:'Abschreiben und Aufsagen kommt ohne Verständnis aus.'}}
];
const KOV=['Viel zu viele Begriffe (etwa 40)','Fließtext statt Begriff und Erklärung','Keine erkennbare Rangfolge, drei Schriftgrößen','Lehrersprache („epochenspezifische Kontingenzerfahrungen“)','Passt nicht auf eine Seite („Teil 1 von 2“)'];
function moduleState(){{return {{verk:fill(VERK.length,-1),kov:fill(KOV.length,false),ko:Array.from({{length:12}},()=>({{b:'',d:''}})),koHide:false,matrix:fill(MATRIX.length,-1),m0:null}};}}
function koN(){{return state.ko.filter(r=>r.b.trim()&&r.d.trim()).length;}}
function koRender(){{
  const wrap=$('koRows');wrap.className=state.koHide?'ko-hide':'';
  wrap.innerHTML=state.ko.map((r,i)=>'<div class="ko-row"><input type="text" data-ko="'+i+'" data-f="b" value="'+esc(r.b)+'" placeholder="Begriff '+(i+1)+'"><input type="text" class="ko-def" data-ko="'+i+'" data-f="d" value="'+esc(r.d)+'" placeholder="Erklärung in einem Satz"><span></span></div>').join('');
  wrap.querySelectorAll('[data-ko]').forEach(el=>el.addEventListener('input',()=>{{state.ko[+el.dataset.ko][el.dataset.f]=el.value;scheduleSave();$('koCount').textContent=koN()+' von höchstens 12 Begriffen';renderSummary();}}));
  $('koCount').textContent=koN()+' von höchstens 12 Begriffen';
  $('koHideBtn').textContent=state.koHide?'Erklärungen zeigen':'Erklärungen verdecken';
  $('koHideBtn').onclick=()=>{{state.koHide=!state.koHide;scheduleSave();koRender();}};
}}
function matrixRender(){{
  const wrap=$('matrixList');wrap.innerHTML='';
  MATRIX.forEach((m,i)=>{{
    const old=state.m0&&state.m0[i]>0?' <span class="hint">· Modul 0: '+LEVELS[state.m0[i]-1]+'</span>':'';
    const div=document.createElement('div');div.className='matrix-row';
    div.innerHTML='<strong style="font-size:.92rem">'+m+'</strong>'+old+'<div class="chip-row">'+LEVELS.map((l,j)=>'<button class="cat-chip'+(state.matrix[i]===j?' sel':'')+'" data-m="'+i+'" data-j="'+j+'">'+l+'</button>').join('')+'</div>';
    wrap.appendChild(div);
  }});
  wrap.querySelectorAll('[data-m]').forEach(b=>b.addEventListener('click',()=>{{state.matrix[+b.dataset.m]=+b.dataset.j;scheduleSave();matrixRender();renderSummary();}}));
}}
function renderModule(){{pickList('verk','verkList',VERK,VERK_OPTS);checkList('kov','kovList',KOV);koRender();matrixRender();}}
async function afterInit(){{
  const prev=await loadOtherModule('modul0-onboarding');
  if(prev&&Array.isArray(prev.matrix)){{state.m0=prev.matrix;matrixRender();}}
}}
function matrixText(){{return MATRIX.map((m,i)=>m+': '+(state.matrix[i]>-1?LEVELS[state.matrix[i]]:'–')+(state.m0&&state.m0[i]>0?' (Modul 0: '+LEVELS[state.m0[i]-1]+')':'')).join('\\n');}}
function ROWS(){{
  const md=state.matrix.filter(v=>v>-1).length,rd=['rd1','rd2','rd3','rd4'].filter(k=>val(k)).length;
  return [pickRow('Verknüpfen','verk'),['Mein Organizer',koN()>=6?'✓ '+koN()+' Begriffe':koN()+' Begriffe',koN()>=6],['Lernberatung',rd===4?'✓ skizziert':rd+'/4 Schritte',rd===4],['Kompetenzmatrix',md===MATRIX.length?'✓ vollständig':md+'/'+MATRIX.length,md===MATRIX.length]];
}}
function SECTIONS(){{
  return [['Verknüpfen',pickText('Aufträge','verk')+'\\n'+fld('Frage 1','vf1')+'\\n'+fld('Frage 2','vf2')],
    ['Mein Knowledge Organizer',fld('Einheit','koThema')+'\\n'+(state.ko.filter(r=>r.b.trim()).map(r=>r.b+': '+(r.d||'–')).join('\\n')||'–')+'\\n'+fld('Zusammenhänge','koZus')+'\\n'+fld('Schaubild','koBild')+'\\nHärtetest bestanden: '+(state.koTest?'ja':'nein')],
    ['Zehn Minuten Lernberatung',fld('1 Einstieg','rd1')+'\\n'+fld('2 Vormachen','rd2')+'\\n'+fld('3 Wochenplan','rd3')+'\\n'+fld('4 Prüfen','rd4')],
    ['Kompetenzmatrix, Erhebung 2',matrixText()+'\\nVideo-Selbstanalyse Nr. 2: '+(state.msVideo?'erledigt':'offen')+'\\n'+fld('Was ich heute sehe','msSieht')]];
}}
"""

MODS = [M34, M35, M36]
