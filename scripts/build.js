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
    title: "Skripte",
    match: (f) => /^Skript_/i.test(f),
  },
  {
    title: "Drehbücher",
    match: (f) => /^Drehb/i.test(f),
  },
];

const IGNORE_FILES = new Set(["README.md"]);

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
    <a class="brand" href="index.html">CPD Fortbildung</a>
    <nav><a href="index.html">Übersicht</a></nav>
  </div>
</header>
<main>
  <a class="back-link" href="index.html">&larr; Zur Übersicht</a>
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
    <a class="brand" href="index.html">CPD Fortbildung</a>
  </div>
</header>
<main>
  <h1 class="page-title">CPD Fortbildung</h1>
  <p class="intro">Alle Dokumente des Fortbildungscurriculums für Quereinsteiger:innen.</p>
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

  // Interaktive SPAs: alle .html-Dateien aus SPAs/ werden automatisch
  // eingebunden, natürlich sortiert und nach docs/spas/ kopiert.
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

    fs.mkdirSync(SPA_OUT_DIR, { recursive: true });
    fs.copyFileSync(srcPath, path.join(SPA_OUT_DIR, file));
    console.log(`kopiert: SPAs/${file} -> docs/spas/${file}`);
    return { title, href: `spas/${file}` };
  });
  if (spaDocs.length > 0) {
    groups.push({ title: "Interaktive Module (SPAs)", docs: spaDocs });
  }

  if (overviewDocs.length > 0) {
    groups.unshift({ title: "Überblick", docs: overviewDocs });
  }

  fs.writeFileSync(path.join(OUT_DIR, "index.html"), indexTemplate({ groups }));
  console.log(`gebaut: docs/index.html`);
  console.log(`\nFertig. ${allMdFiles.length} Dokumente in "${path.relative(ROOT_DIR, OUT_DIR)}/" erzeugt.`);
}

main();
