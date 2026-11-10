-- ============================================================================
-- Block 3 (Module 3.1–3.6): sechs neue Selbstlern-SPAs registrieren
-- ----------------------------------------------------------------------------
-- Legt die Module in der Tabelle modules an. Danach lassen sie sich im
-- Coach-Dashboard pro Kurs freischalten (course_modules.visible).
--
-- Hinweise:
-- * Die Dateinummer (0014) bitte an die tatsächlich letzte Migration anpassen.
-- * sort_order schließt an Modul 2.6 an. Vorher prüfen:
--     select key, sort_order from modules order by sort_order;
--   Falls 2.6 nicht auf 14 liegt, die Werte unten entsprechend verschieben.
-- * Mehrfaches Ausführen ist unschädlich (on conflict aktualisiert nur
--   Titel, Datei und Reihenfolge; Teilnehmerfortschritt bleibt erhalten).
-- ============================================================================

begin;

insert into modules (key, title, file, sort_order) values
  ('modul3-1-gedaechtnis',        'Modul 3.1 · Wie das Gedächtnis arbeitet',            'Modul3-1_Gedaechtnis_SPA.html',        15),
  ('modul3-2-kognitive-last',     'Modul 3.2 · Material und Sprache entlasten',         'Modul3-2_Kognitive-Last_SPA.html',     16),
  ('modul3-3-aufmerksamkeit',     'Modul 3.3 · Aufmerksamkeit lenken',                  'Modul3-3_Aufmerksamkeit_SPA.html',     17),
  ('modul3-4-abruf',              'Modul 3.4 · Abrufen schlägt Wiederlesen',            'Modul3-4_Abruf_SPA.html',              18),
  ('modul3-5-verteilen-mischen',  'Modul 3.5 · Verteilen und Mischen',                  'Modul3-5_Verteilen-Mischen_SPA.html',  19),
  ('modul3-6-vernetzen',          'Modul 3.6 · Wissen vernetzen · Abschluss Block 3',   'Modul3-6_Vernetzen_SPA.html',          20)
on conflict (key) do update set
  title      = excluded.title,
  file       = excluded.file,
  sort_order = excluded.sort_order;

commit;

-- Kontrolle:
-- select key, title, file, sort_order from modules order by sort_order;
