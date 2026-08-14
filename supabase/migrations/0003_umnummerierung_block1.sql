-- ============================================================================
-- Umnummerierung nach der Verdichtung von Block 1 (36 -> 35 Modulwochen)
-- ----------------------------------------------------------------------------
-- Hintergrund: Das frühere Modul 1 („Fünf mentale Modelle") ist Teil 2 der
-- Auftaktwoche geworden (Kickoff jetzt 90 Minuten). Dadurch verschiebt sich
-- ab Modul 2 alles um eine Nummer nach unten.
--
-- WICHTIG: Es werden ausschließlich UPDATEs ausgeführt – die module.id bleibt
-- erhalten. Damit bleiben alle Einträge in progress und course_modules
-- unverändert gültig; kein Teilnehmerfortschritt geht verloren.
--
-- Reihenfolge beachten: erst modul3 -> modul2, dann modul2 -> modul1,
-- sonst kollidiert der unique-Index auf modules.key.
-- ============================================================================

begin;

-- 1) Altes Modul 1 wird Teil 2 des Onboardings
update modules set
  key        = 'modul0b-mentale-modelle',
  title      = 'Modul 0 · Teil 2 – Die fünf mentalen Modelle',
  file       = 'Modul0b_Mentale-Modelle_SPA.html',
  sort_order = 1
where key = 'modul1-woche01-fuenf-mentale-modelle';

-- 2) Altes Modul 3 -> Modul 2 (zuerst, um Key-Kollisionen zu vermeiden)
update modules set
  key        = 'modul2-woche02-zaesuren',
  title      = 'Modul 2 · Woche 2 – Starker Start, geordnetes Ende',
  file       = 'Modul2_Woche02_SPA.html',
  sort_order = 3
where key = 'modul3-woche03-starker-stundenstart';

-- 3) Altes Modul 2 -> Modul 1
update modules set
  key        = 'modul1-woche01-hohe-erwartungen',
  title      = 'Modul 1 · Woche 1 – Hohe Erwartungen',
  file       = 'Modul1_Woche01_SPA.html',
  sort_order = 2
where key = 'modul2-woche02-hohe-erwartungen';

-- 4) Titel des Onboardings an das 90-Minuten-Format anpassen
update modules set
  title = 'Modul 0 · Kickoff – Handwerk ist lernbar (90 min)'
where key = 'modul0-onboarding';

commit;

-- Kontrolle:
-- select key, title, file, sort_order from modules order by sort_order;
