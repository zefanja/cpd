# Umstellung: Block 1 verdichtet, Jahr auf 35 Modulwochen

Betrifft `src/`, `SPAs/`, `supabase/` und `Fortbildungsprogramm_Ueberblick.html`.

## Was sich geändert hat

**Die Auftaktwoche dauert jetzt 90 Minuten** und trägt zwei Funktionen: den Programm-Vertrag
(Kickoff) und das Grundlagenmodul „Fünf mentale Modelle". Sie liegt vor Unterrichtsbeginn, deshalb
ist die Länge organisierbar. Das frühere Modul „Woche 1" entfällt als eigene Sitzung; sein
Perspektivwechsel („Es war nicht persönlich – es war eine Norm") bleibt vollständig erhalten, die
beiden Fallbeispiele sind Reserve- und SPA-Material geworden.

**Block 1 hat sieben statt acht Wochen.** Drei Inhalte sind dorthin gewandert, wo ihr Bauprinzip
ohnehin steht – gestrichen wurde keiner:

| Inhalt | vorher | jetzt | Begründung |
|---|---|---|---|
| Stundenende (Puffer, Pack-Signal, Reservekarten) | W8 | **W2** | Das Ende ist der Spiegel der Begrüßung – dieselbe Zäsur, gespiegelt |
| Übergänge (nummerieren, Kante, Do It Again) | W8 | **W3** | Ein Übergang *ist* eine nummerierte What-to-Do-Anweisung mit scharfen Kanten |
| Warm/Strict | W7 | **W4** | Kein Wortschatz, sondern ein Registerwechsel – gehört zur Präsenz |

Dadurch wird die alte W8 zur neuen **W7** und ganz dem W.I.N.-Gespräch plus Meilenstein 1 gewidmet
(vorher drei Themen in 60 Minuten, mit dem Hinweis „notfalls den Übergangs-Teil kürzen"). Die alte
W7 (neue W6) trägt zwei Sprachwerkzeuge statt dreien – bei doppelter Übungsmenge.

**Alles ab der alten Woche 2 ist um eine Nummer nach vorn gerückt.** Das Jahr hat 35 statt 36
Modulwochen.

| | vorher | jetzt |
|---|---|---|
| Block 1 | 1–8 | **1–7** |
| Block 2 | 9–14 | **8–13** |
| Block 3 | 15–20 | **14–19** |
| Block 4 | 21–26 | **20–25** |
| Block 5 | 27–31 | **26–30** |
| Block 6 | 32–36 | **31–35** |
| Kompetenzmatrix (Vollerhebung) | W0/W20/W36 | **W0/W19/W35** |
| Matrix-Teilupdates | W8/W14/W26/W31 | **W7/W13/W25/W30** |
| Meilenstein-Gespräche | W8/W20/W36 | **W7/W19/W35** |
| Video-Selbstanalysen | W1 (Baseline), 8, 20, 34 | **W1 (Baseline), 7, 19, 33** |
| Gruppenhospitationen | W6, 14, 20, 26, 31 | **W5, 13, 19, 25, 30** |

Die drei Versprechen, die drei Bitten, die drei Formate, ein Action Step pro Woche, das versiegelte
Baseline-Video und das Abschluss-Kolloquium sind unverändert.

## Was angefasst wurde

- `src/Skript_Woche00_Auftakt.md` – neu geschrieben (90 Minuten, mit den fünf Modellen)
- `src/Skript_Woche01.md` … `Skript_Woche35.md` – umbenannt (alt 02–36), alle Querverweise verschoben
- `src/Skript_Woche02/03/04/06/07.md` – zusätzlich inhaltlich umgebaut, Zeitraster neu austariert
- `src/Fortbildungscurriculum_Quereinsteiger.md` – Jahresstruktur, Blockgrenzen, Meilensteine, Modulbeschreibungen Block 1
- `src/Drehbuecher_Block1.md` … `Block6.md` – Querverweise, Kickoff-Drehbuch, Block-1-Umbauten
- `src/Fortbildungsprogramm_Ueberblick.html` + Kopie im Wurzelverzeichnis – Moduldaten, Meilensteine, Jahreskreis, Rahmentexte
- `SPAs/` – Module umnummeriert (siehe unten), Jahreskreis im Onboarding auf 7+6+6+6+5+5 = 35 Wochen
- `old/Skript_Woche01_ARCHIV_fuenf-modelle.md`, `old/Drehbuch_Woche1_ARCHIV.md` – alte Fassungen archiviert

## SPAs und Datenbank

| Datei vorher | Datei jetzt | Modul-Key vorher | Modul-Key jetzt |
|---|---|---|---|
| `Modul0_Onboarding_SPA.html` | unverändert | `modul0-onboarding` | unverändert |
| `Modul1_Woche01_SPA.html` | `Modul0b_Mentale-Modelle_SPA.html` | `modul1-woche01-fuenf-mentale-modelle` | `modul0b-mentale-modelle` |
| `Modul2_Woche02_SPA.html` | `Modul1_Woche01_SPA.html` | `modul2-woche02-hohe-erwartungen` | `modul1-woche01-hohe-erwartungen` |
| `Modul3_Woche03_SPA.html` | `Modul2_Woche02_SPA.html` | `modul3-woche03-starker-stundenstart` | `modul2-woche02-zaesuren` |

**Erledigt (2026-08-14):** `supabase/migrations/0003_umnummerierung_block1.sql` wurde gegen die
Produktionsdatenbank ausgeführt und verifiziert. Die Modulkarten in „Meine Module" zeigen jetzt auf
die neuen Dateinamen; `module.id` blieb erhalten, kein Teilnehmerfortschritt ging verloren.

Inhaltlich offen: Die SPA zur neuen Woche 2 deckt bisher nur den Stundenstart ab – das Stundenende
fehlt dort noch. Für die neue Woche 3 (Aufmerksamkeit, Anweisungen, Übergänge) gibt es noch keine SPA.

## Aufräumen

`_to_delete/` enthält zwei alte `docs/`-Stände und eine Git-Lock-Datei, die beim Arbeiten über die
Cowork-Verbindung nicht gelöscht werden konnten. Der Ordner kann komplett gelöscht werden – `docs/`
steht in `.gitignore` und wird von GitHub Actions bei jedem Push neu gebaut.

## Zurücknehmen

Nichts ist committet:

```
git status                       # Überblick (Umbenennungen sind als R vorgemerkt)
git diff && git diff --cached    # alle Änderungen
git reset && git checkout -- .   # alles zurücknehmen
```
