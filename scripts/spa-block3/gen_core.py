#!/usr/bin/env python3
"""Baut die sechs Block-3-SPAs (SPAs/Modul3-*_SPA.html).

Aufruf:  python3 scripts/spa-block3/gen_core.py .

Aussehen und Speicher-/Export-Logik werden aus der SPA 2.6 übernommen.
Inhalte: mods_a.py (3.1–3.3), mods_b.py (3.4–3.6); Quizfragen: quizdata_b3.py
(dieselben Fragen stehen in den Skripten, Anhang 2).
"""
import json, re, sys, os

ROOT = sys.argv[1]
SCR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCR)
import quizdata_b3

REF = open(f"{ROOT}/SPAs/Modul2-6_DoNow-ExitTicket_SPA.html", encoding="utf-8").read()
css_all = REF.split("<style>")[1].split("</style>")[0]
CSS_BASE = css_all.split("/* ---------- Modul 2.6: Tickets sortieren ---------- */")[0]
CSS_TAIL = css_all.split("/* ---------- Einseiter ---------- */")[1]
ENGINE = REF[REF.index("let state=freshState();"):REF.rindex("</script>")]
# In der Vorlage fest verdrahtet: Laufzeit des Action Steps steht schon korrekt ("zwei Wochen").

CSS_EXTRA = """
/* ---------- Block 3: Ergänzungen ---------- */
.check-list{margin:.6rem 0 .2rem 1.2rem;font-size:.92rem;display:grid;gap:.3rem}
.fig{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:10px;margin-top:.9rem;background:#fff}
.bigshow{font-family:var(--display);font-weight:800;font-size:clamp(1.5rem,6.5vw,2.8rem);letter-spacing:.14em;text-align:center;padding:1.6rem .4rem;word-break:break-all}
.count{font-family:var(--display);font-weight:800;color:var(--amber)}
.stagebox{display:none}
.result-row{display:flex;justify-content:space-between;gap:1rem;border-bottom:1px dashed var(--line);padding:.4rem 0;font-size:.92rem}
.result-row b{font-family:var(--display);color:var(--petrol)}
.two{display:grid;gap:.8rem}
@media(min-width:700px){.two{grid-template-columns:1fr 1fr}}
.ko-row{display:grid;grid-template-columns:1fr 2fr auto;gap:.4rem;margin-top:.4rem;align-items:center}
.ko-row input{font-size:.92rem;padding:.45rem .55rem}
.ko-hide .ko-def{color:transparent;background:repeating-linear-gradient(45deg,#E0ECE9,#E0ECE9 6px,#fff 6px,#fff 12px)}
.term{display:grid;grid-template-columns:minmax(8rem,1fr) 2.2fr;gap:.6rem;padding:.45rem 0;border-bottom:1px dashed var(--line);font-size:.92rem}
.term b{font-family:var(--display)}
.hide-def .term span{color:transparent;background:var(--petrol-soft);border-radius:6px;user-select:none}
.ticker{background:#FBF7EE;border-left:4px solid var(--amber);padding:.6rem .8rem;font-size:.95rem;margin-top:.6rem;min-height:3.2em;border-radius:0 10px 10px 0}
.task-row{display:flex;gap:.6rem;align-items:flex-start;padding:.45rem 0;border-bottom:1px dashed var(--line);font-size:.92rem}
@media(max-width:520px){#presBtn{display:none}.head-inner{gap:.45rem}.brand{font-size:.78rem}}
.task-row .no{font-family:var(--display);font-weight:800;color:var(--petrol);width:1.6rem;flex-shrink:0}
"""

LIB = r"""
/* ================= Gemeinsame Bausteine Block 3 ================= */
const RATE=['gewusst','teilweise','nicht gewusst'];
function fill(n,v){return Array.from({length:n},()=>v);}
function val(k){return (state[k]==null?'':String(state[k])).trim();}
function fld(label,k){return label+': '+(val(k)||'–');}
function $(id){return document.getElementById(id);}

/* Auswahlkarten: items=[{tag,t,ok,note,opts?}] */
const PICKS={};
function pickList(key,elId,items,opts){PICKS[key]={elId:elId,items:items,opts:opts};renderPick(key);}
function renderPick(key){
  const P=PICKS[key],wrap=$(P.elId);if(!wrap)return;wrap.innerHTML='';
  P.items.forEach((it,i)=>{
    const sel=state[key][i],o=it.opts||P.opts,long=!!it.opts;
    const div=document.createElement('div');div.className='quiz-item';
    let btn='';
    o.forEach((t,j)=>{
      let c=long?'quiz-opt':'cat-chip';
      if(sel>-1){if(j===it.ok)c+=long?' right':' correct';else if(j===sel)c+=' wrong';}
      btn+='<button class="'+c+'" data-i="'+i+'" data-j="'+j+'"'+(sel>-1?' disabled':'')+'>'+t+'</button>';
    });
    div.innerHTML=(it.tag?'<span class="step-label" style="margin-top:0;display:block">'+it.tag+'</span>':'')
      +'<p class="quiz-q" style="font-weight:500">'+it.t+'</p><div class="'+(long?'quiz-opts':'chip-row')+'">'+btn+'</div>'
      +(sel>-1?'<p class="quiz-note on">'+(sel===it.ok?'✓ Richtig. ':'✗ Nicht ganz. ')+it.note+'</p>':'');
    wrap.appendChild(div);
  });
  wrap.querySelectorAll('[data-i]').forEach(b=>b.addEventListener('click',()=>{state[key][+b.dataset.i]=+b.dataset.j;scheduleSave();renderPick(key);renderSummary();}));
}
function pickDone(key){return state[key].filter(v=>v>-1).length;}
function pickScore(key){return state[key].reduce((a,v,i)=>a+(v===PICKS[key].items[i].ok?1:0),0);}
function pickRow(label,key){const n=PICKS[key].items.length,d=pickDone(key);return [label,d===n?'✓ '+pickScore(key)+'/'+n+' richtig':d+'/'+n,d===n];}
function pickText(label,key){return label+': '+pickScore(key)+' von '+PICKS[key].items.length+' richtig';}

/* Karten zur Selbstkontrolle: cards=[{q,a}] */
const FLASHES={};
function flashList(key,elId,cards,resId){FLASHES[key]={elId:elId,cards:cards,resId:resId};renderFlashes(key);}
function renderFlashes(key){
  const F=FLASHES[key],wrap=$(F.elId);if(!wrap)return;wrap.innerHTML='';
  const open=state[key+'Open'],rate=state[key+'Rate'];
  F.cards.forEach((f,i)=>{
    const div=document.createElement('div');div.className='flash'+(open[i]?' open':'');
    let chips='';RATE.forEach((r,j)=>{chips+='<button class="cat-chip'+(rate[i]===j?' sel':'')+'" data-r="'+i+'" data-j="'+j+'">'+r+'</button>';});
    div.innerHTML='<div class="fq">'+(i+1)+'. '+f.q+'</div>'
      +(open[i]?'':'<p style="margin-top:.5rem"><button class="btn ghost small" data-o="'+i+'">Antwort zeigen</button></p>')
      +'<div class="fa">'+f.a+'<div class="chip-row">'+chips+'</div></div>';
    wrap.appendChild(div);
  });
  wrap.querySelectorAll('[data-o]').forEach(b=>b.addEventListener('click',()=>{open[+b.dataset.o]=true;scheduleSave();renderFlashes(key);}));
  wrap.querySelectorAll('[data-r]').forEach(b=>b.addEventListener('click',()=>{rate[+b.dataset.r]=+b.dataset.j;scheduleSave();renderFlashes(key);renderSummary();}));
  const c=flashCounts(key),done=c[0]+c[1]+c[2],res=$(F.resId);
  if(res){
    const weak=F.cards.map((f,i)=>rate[i]===2?(i+1):null).filter(Boolean);
    res.innerHTML=done?'<h3>Dein Stand</h3><p>'+c[0]+' gewusst · '+c[1]+' teilweise · '+c[2]+' nicht gewusst ('+done+' von '+F.cards.length+' bewertet)</p>'
      +(weak.length?'<p class="hint">Nicht gewusst: Frage '+weak.join(', ')+'. Genau diese Fragen lohnen sich für deine nächste Wiederholung.</p>':'')
      :'<p class="hint">Beantworte jede Frage zuerst im Kopf oder auf einem Zettel. Deck dann auf und bewerte ehrlich.</p>';
  }
}
function flashCounts(key){const c=[0,0,0];state[key+'Rate'].forEach(v=>{if(v>-1)c[v]++;});return c;}
function flashRow(label,key){const c=flashCounts(key),d=c[0]+c[1]+c[2],n=FLASHES[key].cards.length;return [label,d===n?'✓ '+c[0]+' gewusst, '+c[1]+' teilweise, '+c[2]+' nicht':d+'/'+n+' bewertet',d===n];}
function flashText(key){const c=flashCounts(key),F=FLASHES[key];return c[0]+' gewusst · '+c[1]+' teilweise · '+c[2]+' nicht gewusst\nNicht gewusst: '+(F.cards.map((f,i)=>state[key+'Rate'][i]===2?(i+1)+'. '+f.q:null).filter(Boolean).join(' | ')||'–');}

/* Etwas für n Sekunden zeigen */
function timedShow(boxId,secs,done){
  const box=$(boxId);box.style.display='block';let left=secs;
  const c=box.querySelector('.count');if(c)c.textContent=left;
  box.scrollIntoView({block:'center',behavior:'smooth'});
  const iv=setInterval(()=>{left--;if(c)c.textContent=left;if(left<=0){clearInterval(iv);box.style.display='none';done();}},1000);
  return iv;
}
/* Aufdecken per Knopf: <button data-reveal="id"> */
function bindReveals(){
  document.querySelectorAll('[data-reveal]').forEach(b=>{
    const id=b.dataset.reveal,el=$(id);
    if(state['rv_'+id])el.classList.add('on');
    b.onclick=()=>{el.classList.add('on');state['rv_'+id]=true;scheduleSave();};
  });
}
/* Ankreuzlisten: items=[text] */
function checkList(key,elId,items){
  const wrap=$(elId);if(!wrap)return;
  wrap.innerHTML=items.map((t,i)=>'<label class="self-check"><input type="checkbox" data-c="'+i+'"'+(state[key][i]?' checked':'')+'><span>'+t+'</span></label>').join('');
  wrap.querySelectorAll('[data-c]').forEach(c=>c.addEventListener('change',()=>{state[key][+c.dataset.c]=c.checked;scheduleSave();renderSummary();}));
}

/* ---- Zustand, Zusammenfassung, Druck: aus den Angaben des Moduls ---- */
function freshState(){
  const s={v:STATE_VERSION,name:'',quizSel:QUIZ.map(()=>0),transferAnswer:'',actionStep:ACTIONSTEPS[0].id,log:emptyLog(),
    exitMit:'',exitSorge:'',commit:false,screen:0,submitted:false,submittedAt:null,submissionText:'',
    starterOpen:fill(STARTER.length,false),starterRate:fill(STARTER.length,-1)};
  document.querySelectorAll('[data-store]').forEach(el=>{const k=el.dataset.store;if(!(k in s))s[k]=el.type==='checkbox'?false:'';});
  return Object.assign(s,moduleState());
}
function normalizeModule(f){
  Object.keys(f).forEach(k=>{
    if(state[k]===undefined){state[k]=f[k];return;}
    if(Array.isArray(f[k])&&(!Array.isArray(state[k])||(FIXED_ARRAYS.indexOf(k)>-1&&state[k].length!==f[k].length)))state[k]=f[k];
  });
}
function refreshModuleUI(){bindReveals();flashList('starter','starterList',STARTER,'starterResult');renderModule();}
function summaryRows(){
  return [flashRow('Abruf','starter')].concat(ROWS()).concat([
    ['Quiz',quizDone()===QUIZ.length?'✓ '+quizScore()+'/'+QUIZ.length+' richtig':quizDone()+'/'+QUIZ.length+' beantwortet',quizDone()===QUIZ.length],
    ['Action Step',state.commit?'✓ verbindlich':'noch nicht bestätigt',!!state.commit]]);
}
function ALLSECTIONS(){return [['Abruf zu Beginn',flashText('starter')]].concat(SECTIONS());}
function summaryText(){let t=summaryHead();ALLSECTIONS().forEach(s=>{t+='— '+s[0].toUpperCase()+' —\n'+s[1]+'\n\n';});return t+summaryTail();}
function buildPrint(){let h=printHead();ALLSECTIONS().forEach(s=>{h+='<h2>'+esc(s[0])+'</h2><div class="ans">'+esc(s[1])+'</div>';});return h+printActionBlock()+printTail();}
"""

HEAD = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Modul {n} · {title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>

<header>
  <div class="head-inner">
    <button class="head-btn" id="backBtn" title="Zurück">← Zurück</button>
    <span class="brand">MODUL {n}</span>
    <span class="station-label" id="stationLabel"></span>
    <button class="head-btn" id="presBtn" aria-pressed="false" title="Größere Schrift für Beamer">🖥 Präsentation</button>
    <button class="head-btn" id="menuBtn">☰ Stationen</button>
  </div>
  <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
</header>

<main id="main">
"""

FOOT = """
</main>

<nav class="navbar" aria-label="Modulnavigation">
  <div class="nav-inner">
    <button class="head-btn" data-nav="prev" id="prevBtn">← Zurück</button>
    <div class="dots" id="dots"></div>
    <button class="head-btn" data-nav="next" id="nextBtn">Weiter →</button>
  </div>
</nav>

<div class="menu-overlay" id="menuOverlay">
  <div class="menu-panel" id="menuPanel" role="dialog" aria-label="Stationen"></div>
</div>

<div class="toast" id="toast"></div>
<div id="printReport"></div>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.js"></script>
<script src="./shared/cpd-config.js"></script>
<script src="./shared/cpd-client.js" data-module-key="{key}"></script>
<script>
"use strict";
{script}
</script>
</body>
</html>
"""


def js(v):
    return json.dumps(v, ensure_ascii=False)


def IMG(name, alt):
    return f'<img class="fig" src="./assets/images/grafiken/{name}.svg" alt="{alt}" loading="lazy">'


def start(m):
    return f"""
<section class="screen" data-title="Start">
  <span class="eyebrow">Modul {m['n']} · Block 3 · Fortbildung Sek I/II</span>
  <h1>{m['frage']}</h1>
  <p class="lead">{m['lead']}</p>
  <div class="card">
    <h3>Dein Weg durch dieses Modul</h3>
    <p style="font-size:.9rem">{m['weg']}</p>
  </div>
  <div class="field" id="tnNameField">
    <label for="tnName">Dein Name <span class="sub">Erscheint auf dem PDF-Export für deinen Coach.</span></label>
    <input type="text" id="tnName" data-store="name" placeholder="Vorname Nachname" autocomplete="name">
  </div>
  <p class="hint" id="startStoreHint" style="margin-top:.8rem"></p>
  <div class="badge-row">
    <span class="badge">⏱ ca. {m['min']} Min.</span>
    <span class="badge">📖 Kernquellen: {m['quellen']}</span>
    <span class="badge">🔒 Ergebnisse nur für dich &amp; deinen Coach</span>
  </div>
  <p style="margin-top:1.4rem"><button class="btn" data-nav="next">Los geht es →</button></p>
</section>
"""


def abruf(m, nr):
    return f"""
<section class="screen" data-title="Abruf">
  <span class="eyebrow">Station {nr} · Abruf</span>
  <h2>{m.get('abruf_h', 'Sechs Fragen, bevor es losgeht.')}</h2>
  <p class="lead">{m.get('abruf_lead', 'Drei zum letzten Modul, zwei zu älteren, eine aus einem früheren Block. Ohne Unterlagen. Dass die älteren schwerer fallen, ist gewollt.')}</p>
  <div id="starterList"></div>
  <div class="card" id="starterResult"></div>
  <p style="margin-top:1.3rem"><button class="btn" data-nav="next">Weiter →</button></p>
</section>
"""


def quiz(m, nr):
    return f"""
<section class="screen" data-title="Quiz">
  <span class="eyebrow">Station {nr} · Quiz</span>
  <h2>Fünf Fragen zu Modul {m['n']}.</h2>
  <p class="lead">Zu jeder Antwort bekommst du eine kurze Rückmeldung, auch zu den falschen.</p>
  <div id="quizList"></div>
  <div class="quiz-item">
    <p class="quiz-q">F6 (Freitext): {m['f6q']}</p>
    <textarea id="transferAnswer" data-store="transferAnswer" style="margin-top:.8rem" placeholder="…"></textarea>
    <p style="margin-top:.7rem"><button class="btn ghost small" data-reveal="transferNote">Muster anzeigen</button></p>
    <p class="quiz-note reveal" id="transferNote" style="border-top:1px dashed var(--line)">{m['f6a']}</p>
  </div>
  <p style="margin-top:1.3rem"><button class="btn" data-nav="next">Weiter →</button></p>
</section>
"""


def action(m, nr):
    extra = m.get("action_extra", "")
    return f"""
<section class="screen" data-title="Action Step &amp; Export">
  <span class="eyebrow">Station {nr} · Action Step</span>
  <h2>Dein Action Step bis zum nächsten Input.</h2>
  <p class="lead">Wähle einen Action Step. Er gilt für zwei Wochen; in der Austauschwoche schärfst du ihn nach.</p>
  <div id="stepList"></div>
  <div class="commit-box">
    <input type="checkbox" id="commitCheck" data-store="commit">
    <label for="commitCheck" style="font-weight:600" id="commitLabel"></label>
  </div>
  <div class="card">
    <h3>{m['log_title']}</h3>
    <p class="hint">{m['log_hint']}</p>
    <div id="logList" style="margin-top:.4rem"></div>
  </div>
  {extra}
  <div class="card">
    <h3>Exit-Karte <span class="hint" style="font-weight:400">(fließt ins nächste Coaching-Gespräch ein)</span></h3>
    <div class="field" style="margin-top:.5rem"><label for="exitMit">{m['exit'][0]}</label><textarea id="exitMit" data-store="exitMit" placeholder="…"></textarea></div>
    <div class="field"><label for="exitSorge">{m['exit'][1]}</label><textarea id="exitSorge" data-store="exitSorge" placeholder="…"></textarea></div>
  </div>
  <div class="card">
    <h3>Deine Ergebnisse teilen</h3>
    <div class="summary-status" id="summaryStatus"></div>
    <div class="export-actions">
      <button class="btn" id="submitBtn">✅ Bei Coach einreichen</button>
      <button class="btn ghost" id="pdfBtn">📄 Als PDF exportieren</button>
      <button class="btn ghost" id="copyBtn">📋 Als Text kopieren</button>
      <button class="btn ghost" id="saveFileBtn">💾 Fortschritt als Datei sichern</button>
    </div>
    <p class="hint" id="submitStatus" style="margin-top:.6rem"></p>
    <p class="hint" style="margin-top:.7rem">„Bei Coach einreichen“ schickt deine Antworten an deinen Coach. Der PDF-Export öffnet zusätzlich den Druckdialog deines Geräts.</p>
  </div>
  <p class="hint" style="margin-top:1rem" id="storeHint"></p>
  <div style="border-left:4px solid var(--amber);padding:.2rem 0 .2rem 1rem;margin-top:1.4rem;font-style:italic;color:#3E4A45">{m['ausblick']}</div>
</section>
"""


def build(m):
    key = m["skript"]
    qd = quizdata_b3.DATA[key]
    quizjs = [{"q": f"F{i+1}. {q}", "opts": [{"t": o, "ok": j == ok, "note": note} for j, (o, note) in enumerate(opts)]} for i, (q, opts, ok) in enumerate(qd["mc"])]
    starter = [{"q": q, "a": a} for q, a in qd["starter"]]
    md = open(f"{ROOT}/src/Skript_Modul{key}.md", encoding="utf-8").read()
    f6 = re.search(r"\*\*F6 \(Transfer, Freitext\):\*\* (.*?) \*\((.*)\)\*", md, re.S)
    m.setdefault("f6q", f6.group(1).strip())
    m.setdefault("f6a", f6.group(2).strip())
    screens = m["screens"]
    n_content = screens.count('<section class="screen"')
    html_screens = start(m) + abruf(m, 1) + screens
    nr = 2 + n_content
    html_screens += quiz(m, nr)
    for extra in m.get("after_quiz", []):
        nr += 1
        html_screens += extra.replace("{NR}", str(nr))
    html_screens += action(m, nr + 1)
    consts = (
        f"const MOD={js({'n': m['n'], 'key': m['key'], 'file': m['key'], 'title': m['title']})};\n"
        f"const STATE_VERSION=1;\nconst STARTER={js(starter)};\nconst QUIZ={js(quizjs)};\n"
        f"const ACTIONSTEPS={js(m['steps'])};\n"
        f"const LOG_ROWS={m.get('log_rows', 3)}, LOG_ROW_LABEL={js(m.get('log_label', 'Stunde'))}, LOG_TITLE={js(m['log_title'])};\n"
        f"const LOG_FIELDS={js(m['log_fields'])};\nconst EXIT_LABELS={js(m['exit'])};\n"
        f"const FIXED_ARRAYS={js(m.get('fixed', []))}.concat(['starterOpen','starterRate']);\n"
    )
    script = consts + LIB + m["js"] + "\n" + ENGINE
    out = HEAD.format(n=m["n"], title=m["title"], css=CSS_BASE + CSS_TAIL + CSS_EXTRA) + html_screens + FOOT.format(key=m["key"], script=script)
    path = f"{ROOT}/SPAs/{m['file']}"
    open(path, "w", encoding="utf-8").write(out)
    print("gebaut:", m["file"], f"({len(out)//1000} kB, {html_screens.count('<section')} Stationen)")


if __name__ == "__main__":
    import mods_a, mods_b
    for m in mods_a.MODS + mods_b.MODS:
        build(m)
