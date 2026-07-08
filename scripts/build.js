#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const { marked } = require("marked");

const ROOT_DIR = path.join(__dirname, "..");
const SRC_DIR = path.join(ROOT_DIR, "src");
const OUT_DIR = path.join(ROOT_DIR, "docs");
const STYLE_SRC = path.join(__dirname, "style.css");

// Reihenfolge & Gruppierung der Dokumente auf der Startseite.
// Dateien, die hier nicht auftauchen, werden automatisch unter "Weitere Dokumente" einsortiert.
const GROUPS = [
  {
    title: "Curriculum",
    files: ["Fortbildungscurriculum_Quereinsteiger.md"],
  },
  {
    title: "Skripte",
    files: [
      "Skript_Woche00_Auftakt.md",
      "Skript_Woche02.md",
      "Skript_Woche03.md",
      "Skript_Woche04.md",
      "Skript_Woche05.md",
      "Skript_Woche06.md",
      "Skript_Woche07.md",
      "Skript_Woche08.md",
    ],
  },
  {
    title: "Drehbücher",
    files: [
      "Drehbuch_Woche1.md",
      "Drehbuecher_Block1.md",
      "Drehbuecher_Block2.md",
      "Drehbuecher_Block3.md",
      "Drehbuecher_Block4.md",
      "Drehbuecher_Block5.md",
      "Drehbuecher_Block6.md",
    ],
  },
];

const IGNORE_FILES = new Set(["README.md"]);

marked.setOptions({ gfm: true, breaks: false });

function slugify(filename) {
  return filename.replace(/\.md$/i, "").toLowerCase().replace(/[^a-z0-9]+/g, "-");
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

  const groupedFiles = new Set(GROUPS.flatMap((g) => g.files));
  const groups = GROUPS.map((g) => ({
    title: g.title,
    docs: g.files.filter((f) => docByFile.has(f)).map((f) => docByFile.get(f)),
  }));

  const remaining = allMdFiles.filter((f) => !groupedFiles.has(f));
  if (remaining.length > 0) {
    groups.push({
      title: "Weitere Dokumente",
      docs: remaining.map((f) => docByFile.get(f)),
    });
  }

  fs.writeFileSync(path.join(OUT_DIR, "index.html"), indexTemplate({ groups }));
  console.log(`gebaut: docs/index.html`);
  console.log(`\nFertig. ${allMdFiles.length} Dokumente in "${path.relative(ROOT_DIR, OUT_DIR)}/" erzeugt.`);
}

main();
