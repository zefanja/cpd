#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const { marked } = require("marked");

const ROOT_DIR = path.join(__dirname, "..");
const SRC_DIR = path.join(ROOT_DIR, "src");
const OUT_DIR = path.join(ROOT_DIR, "docs");
const STYLE_SRC = path.join(__dirname, "style.css");
const SPA_SRC_DIR = path.join(ROOT_DIR, "SPAs");
const SPA_OUT_DIR = path.join(OUT_DIR, "spas");

// Reihenfolge & Gruppierung der Dokumente auf der Startseite.
// Gruppen mit `files` verwenden eine feste Liste, Gruppen mit `match` sammeln
// automatisch alle passenden Dateien aus src/ und sortieren sie natürlich.
// Dateien, die in keine Gruppe fallen, werden unter "Weitere Dokumente" einsortiert.
const GROUPS = [
  {
    title: "Curriculum",
    files: ["Fortbildungscurriculum_Quereinsteiger.md"],
  },
  {
    title: "Austausch & Vertiefung",
    files: ["Vertiefung_Austauschwochen.md"],
  },
  {
    title: "Skripte",
    match: (f) => /^Skript_/i.test(f),
  },
  {
    title: "Drehbücher",
    match: (f) => /^Drehb/i.test(f),
  },
];

const IGNORE_FILES = new Set(["README.md"]);

// Alte URLs aus der Zeit der Wochen-Nummerierung (Woche N -> Modul Block.Thema).
// Für jede alte Datei wird in docs/ eine kleine Weiterleitungsseite erzeugt,
// damit Lesezeichen, geteilte Links und login.html?next=… weiter funktionieren.
// Query-String (z. B. ?preview=1) und Anker bleiben erhalten. Die Seiten
// tauchen in keiner Übersicht auf.
const LEGACY_REDIRECTS = [
  ["spas/Modul1_Woche01_SPA.html", "Modul1-1_Hohe-Erwartungen_SPA.html"],
  ["spas/Modul2_Woche02_SPA.html", "Modul1-2_Zaesuren_SPA.html"],
  ["spas/Modul3_Woche03_SPA.html", "Modul1-3_Signal-Anweisung-Uebergang_SPA.html"],
  ["spas/Modul4_Woche04_SPA.html", "Modul1-4_Praesenz_SPA.html"],
  ["spas/Modul5_Woche05_SPA.html", "Modul1-5_Interventionsleiter_SPA.html"],
  ["spas/Modul6_Woche06_SPA.html", "Modul1-6_Framing-Praise_SPA.html"],
  ["spas/Modul7_Woche07_SPA.html", "Modul1-7_WIN-Gespraech_SPA.html"],
  ["spas/Modul8_Woche08_SPA.html", "Modul2-1_Fuenf-Fragen_SPA.html"],
  ["spas/Modul9_Woche09_SPA.html", "Modul2-2_Lernziele_SPA.html"],
  ["spas/Modul10_Woche10_SPA.html", "Modul2-3_Modellieren_SPA.html"],
  ["spas/Modul11_Woche11_SPA.html", "Modul2-4_WeDo_SPA.html"],
  ["spas/Modul12_Woche12_SPA.html", "Modul2-5_YouDo_SPA.html"],
  ["spas/Modul13_Woche13_SPA.html", "Modul2-6_DoNow-ExitTicket_SPA.html"],
  ["skript-woche00-auftakt.html", "skript-modul0-auftakt.html"],
  ["skript-woche01.html", "skript-modul1-1.html"],
  ["skript-woche02.html", "skript-modul1-2.html"],
  ["skript-woche03.html", "skript-modul1-3.html"],
  ["skript-woche04.html", "skript-modul1-4.html"],
  ["skript-woche05.html", "skript-modul1-5.html"],
  ["skript-woche06.html", "skript-modul1-6.html"],
  ["skript-woche07.html", "skript-modul1-7.html"],
  ["skript-woche08.html", "skript-modul2-1.html"],
  ["skript-woche09.html", "skript-modul2-2.html"],
  ["skript-woche10.html", "skript-modul2-3.html"],
  ["skript-woche11.html", "skript-modul2-4.html"],
  ["skript-woche12.html", "skript-modul2-5.html"],
  ["skript-woche13.html", "skript-modul2-6.html"],
  ["skript-woche14.html", "skript-modul3-1.html"],
  ["skript-woche15.html", "skript-modul3-2.html"],
  ["skript-woche16.html", "skript-modul3-3.html"],
  ["skript-woche17.html", "skript-modul3-4.html"],
  ["skript-woche18.html", "skript-modul3-5.html"],
  ["skript-woche19.html", "skript-modul3-6.html"],
  ["skript-woche20.html", "skript-modul4-1.html"],
  ["skript-woche21.html", "skript-modul4-2.html"],
  ["skript-woche22.html", "skript-modul4-3.html"],
  ["skript-woche23.html", "skript-modul4-4.html"],
  ["skript-woche24.html", "skript-modul4-5.html"],
  ["skript-woche25.html", "skript-modul4-6.html"],
  ["skript-woche26.html", "skript-modul5-1.html"],
  ["skript-woche27.html", "skript-modul5-2.html"],
  ["skript-woche28.html", "skript-modul5-3.html"],
  ["skript-woche29.html", "skript-modul5-4.html"],
  ["skript-woche30.html", "skript-modul5-5.html"],
  ["skript-woche31.html", "skript-modul6-1.html"],
  ["skript-woche32.html", "skript-modul6-2.html"],
  ["skript-woche33.html", "skript-modul6-3.html"],
  ["skript-woche34.html", "skript-modul6-4.html"],
  ["skript-woche35.html", "skript-modul6-5.html"],
];


marked.setOptions({ gfm: true, breaks: false });

function slugify(filename) {
  return filename.replace(/\.md$/i, "").toLowerCase().replace(/[^a-z0-9]+/g, "-");
}

function naturalCompare(a, b) {
  const chunk = (s) => s.match(/\d+|\D+/g) || [];
  const chunksA = chunk(a);
  const chunksB = chunk(b);
  const len = Math.max(chunksA.length, chunksB.length);
  for (let i = 0; i < len; i++) {
    const ca = chunksA[i] ?? "";
    const cb = chunksB[i] ?? "";
    if (ca === cb) continue;
    const na = Number(ca);
    const nb = Number(cb);
    if (!Number.isNaN(na) && !Number.isNaN(nb)) return na - nb;
    return ca < cb ? -1 : 1;
  }
  return 0;
}

function extractHtmlTitle(html, fallback) {
  const match = html.match(/<title>(.*?)<\/title>/i);
  if (!match) return fallback;
  return match[1].trim();
}

function extractTitle(markdown, fallback) {
  const match = markdown.match(/^#\s+(.+)$/m);
  if (!match) return fallback;
  return match[1].replace(/^["„]|["“]$/g, "").trim();
}

function pageTemplate({ title, bodyHtml }) {
  return `<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
  <div class="inner">
    <a class="brand" href="uebersicht.html">CPD Fortbildung</a>
    <nav><a href="uebersicht.html">Übersicht</a></nav>
  </div>
</header>
<main>
  <a class="back-link" href="uebersicht.html">&larr; Zur Übersicht</a>
  <h1 class="page-title">${title}</h1>
  <article>
${bodyHtml}
  </article>
</main>
<footer class="site-footer">Erstellt aus Markdown-Quellen in <code>src/</code>.</footer>
</body>
</html>
`;
}

function redirectTemplate({ to }) {
  return `<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url=${to}">
<title>CPD Fortbildung</title>
<link rel="canonical" href="${to}">
<script>window.location.replace(${JSON.stringify(to)});</script>
</head>
<body>
<p>Weiter zu <a href="${to}">${to}</a> …</p>
</body>
</html>
`;
}

function legacyRedirectTemplate({ to }) {
  return `<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Weiterleitung · CPD Fortbildung</title>
<script>window.location.replace(${JSON.stringify(to)} + window.location.search + window.location.hash);</script>
<noscript><meta http-equiv="refresh" content="0; url=${to}"></noscript>
</head>
<body>
<p>Diese Seite ist umgezogen: <a href="${to}">${to}</a></p>
</body>
</html>
`;
}

function indexTemplate({ groups }) {
  const groupsHtml = groups
    .filter((g) => g.docs.length > 0)
    .map(
      (g) => `  <section class="doc-group">
    <h2>${g.title}</h2>
    <ul class="doc-list">
${g.docs
  .map(
    (d) => `      <li><a href="${d.href}"><span class="doc-title">${d.title}</span></a></li>`
  )
  .join("\n")}
    </ul>
  </section>`
    )
    .join("\n");

  return `<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CPD Fortbildung</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
  <div class="inner">
    <a class="brand" href="uebersicht.html">CPD Fortbildung</a>
  </div>
</header>
<main>
  <h1 class="page-title">CPD Fortbildung</h1>
  <p class="intro">Alle Dokumente des Fortbildungscurriculums für Quereinsteiger.</p>
${groupsHtml}
</main>
<footer class="site-footer">Erstellt aus Markdown-Quellen in <code>src/</code>.</footer>
</body>
</html>
`;
}

function main() {
  if (!fs.existsSync(SRC_DIR)) {
    console.error(`Quellordner nicht gefunden: ${SRC_DIR}`);
    process.exit(1);
  }

  fs.rmSync(OUT_DIR, { recursive: true, force: true });
  fs.mkdirSync(OUT_DIR, { recursive: true });
  fs.copyFileSync(STYLE_SRC, path.join(OUT_DIR, "style.css"));

  // Fertige, eigenständige HTML-Seiten direkt in src/ (z.B. interaktive
  // Präsentations-Überblicke) werden unverändert nach docs/ kopiert und als
  // eigene Gruppe ganz oben auf der Startseite verlinkt.
  const overviewHtmlFiles = fs
    .readdirSync(SRC_DIR)
    .filter((f) => f.toLowerCase().endsWith(".html"))
    .sort(naturalCompare);

  const overviewDocs = overviewHtmlFiles.map((file) => {
    const srcPath = path.join(SRC_DIR, file);
    const html = fs.readFileSync(srcPath, "utf8");
    const title = extractHtmlTitle(html, file.replace(/\.html$/i, ""));
    fs.writeFileSync(path.join(OUT_DIR, file), html);
    console.log(`kopiert: src/${file} -> docs/${file}`);
    return { title, href: file };
  });

  const allMdFiles = fs
    .readdirSync(SRC_DIR)
    .filter((f) => f.toLowerCase().endsWith(".md"))
    .filter((f) => !IGNORE_FILES.has(f));

  const docByFile = new Map();

  for (const file of allMdFiles) {
    const srcPath = path.join(SRC_DIR, file);
    const markdown = fs.readFileSync(srcPath, "utf8");
    const title = extractTitle(markdown, file.replace(/\.md$/i, ""));
    const bodyHtml = marked.parse(markdown);
    const outFile = `${slugify(file)}.html`;

    fs.writeFileSync(
      path.join(OUT_DIR, outFile),
      pageTemplate({ title, bodyHtml })
    );

    docByFile.set(file, { title, href: outFile });
    console.log(`gebaut: ${file} -> docs/${outFile}`);
  }

  const groupedFiles = new Set();
  const groups = GROUPS.map((g) => {
    let files;
    if (g.match) {
      files = allMdFiles.filter((f) => g.match(f)).sort(naturalCompare);
    } else {
      files = g.files.filter((f) => docByFile.has(f));
    }
    files.forEach((f) => groupedFiles.add(f));
    return { title: g.title, docs: files.map((f) => docByFile.get(f)) };
  });

  const remaining = allMdFiles.filter((f) => !groupedFiles.has(f)).sort(naturalCompare);
  if (remaining.length > 0) {
    groups.push({
      title: "Weitere Dokumente",
      docs: remaining.map((f) => docByFile.get(f)),
    });
  }

  // Interaktive SPAs: der komplette SPAs/-Baum (inkl. shared/-Assets, Login,
  // Lehrer- und Coach-Seiten in Unterordnern) wird 1:1 nach docs/spas/ kopiert.
  // Für die Startseite werden nur die Top-Level-.html-Dateien verlinkt
  // (Module, Login, Lehrer-Übersicht) – der Coach-Bereich unter spas/coach/
  // bleibt unverlinkt und wird direkt per URL aufgerufen.
  if (fs.existsSync(SPA_SRC_DIR)) {
    fs.cpSync(SPA_SRC_DIR, SPA_OUT_DIR, { recursive: true });
    console.log(`kopiert: SPAs/ -> docs/spas/ (rekursiv)`);
  }

  for (const [from, to] of LEGACY_REDIRECTS) {
    const outPath = path.join(OUT_DIR, from);
    if (fs.existsSync(outPath)) continue; // nie eine echte Seite überschreiben
    fs.mkdirSync(path.dirname(outPath), { recursive: true });
    fs.writeFileSync(outPath, legacyRedirectTemplate({ to }));
  }
  console.log(`gebaut: ${LEGACY_REDIRECTS.length} Weiterleitungen für alte Wochen-URLs`);

  const spaFiles = fs.existsSync(SPA_SRC_DIR)
    ? fs
        .readdirSync(SPA_SRC_DIR)
        .filter((f) => f.toLowerCase().endsWith(".html"))
        .sort(naturalCompare)
    : [];

  const spaDocs = spaFiles.map((file) => {
    const srcPath = path.join(SPA_SRC_DIR, file);
    const html = fs.readFileSync(srcPath, "utf8");
    const title = extractHtmlTitle(html, file.replace(/\.html$/i, ""));
    return { title, href: `spas/${file}` };
  });
  if (spaDocs.length > 0) {
    groups.push({ title: "Interaktive Module (SPAs)", docs: spaDocs });
  }

  if (overviewDocs.length > 0) {
    groups.unshift({ title: "Überblick", docs: overviewDocs });
  }

  fs.writeFileSync(path.join(OUT_DIR, "uebersicht.html"), indexTemplate({ groups }));
  console.log(`gebaut: docs/uebersicht.html`);

  // Startseite: Lehrkräfte landen direkt auf der Login-Seite. Die bisherige
  // Dokumenten-Übersicht bleibt unter uebersicht.html erreichbar (verlinkt
  // im Footer von SPAs/login.html).
  fs.writeFileSync(
    path.join(OUT_DIR, "index.html"),
    redirectTemplate({ to: "spas/login.html" })
  );
  console.log(`gebaut: docs/index.html (Weiterleitung -> spas/login.html)`);

  console.log(`\nFertig. ${allMdFiles.length} Dokumente in "${path.relative(ROOT_DIR, OUT_DIR)}/" erzeugt.`);
}

main();
