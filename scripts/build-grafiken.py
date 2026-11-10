#!/usr/bin/env python3
"""Erzeugt die Grafiken für die Blöcke 3–6 als SVG.

Aufruf:  python3 scripts/build-grafiken.py
Ausgabe: SPAs/assets/images/grafiken/*.svg

Die Dateien werden von den SPAs eingebunden und eignen sich als Folien.
Texte und Zahlen stehen unten in den einzelnen Funktionen und lassen sich dort ändern.
"""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "SPAs", "assets", "images", "grafiken")
os.makedirs(OUT, exist_ok=True)

BG, CARD, INK, MUTED, LINE = "#ECEEE7", "#FFFFFF", "#1C2422", "#5E6862", "#D6DAD0"
PETROL, PSOFT, AMBER = "#0E5B54", "#E0ECE9", "#C98A1B"
ROT, GELB, GRUEN, BLAU, GRAU = "#B0433A", "#D9A21E", "#4E7A38", "#2E5E8C", "#8E9892"
RSOFT, YSOFT, GSOFT = "#F5E4E2", "#FBF3DF", "#EAF1E5"
FONT = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def T(x, y, s, size=16, weight=400, fill=INK, anchor="start", lh=1.3, italic=False):
    lines = str(s).split("\n")
    st = ' font-style="italic"' if italic else ""
    out = f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{st}>'
    for i, ln in enumerate(lines):
        dy = 0 if i == 0 else size * lh
        out += f'<tspan x="{x}" dy="{dy}">{esc(ln)}</tspan>'
    return out + "</text>"


def R(x, y, w, h, fill=CARD, stroke=LINE, rx=10, sw=1.5, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def L(x1, y1, x2, y2, stroke=MUTED, sw=2, dash="", arrow=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = ' marker-end="url(#pf)"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{m}/>'


def P(d, stroke=PETROL, sw=3, fill="none", dash="", arrow=False):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    m = ' marker-end="url(#pf)"' if arrow else ""
    return f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="{fill}" stroke-linecap="round" stroke-linejoin="round"{ds}{m}/>'


def C(cx, cy, r, fill=PETROL, stroke="none", sw=0):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def save(name, w, h, body, title="", bg=BG):
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="{FONT}" role="img" aria-label="{esc(title)}">'
            f'<title>{esc(title)}</title>'
            '<defs><marker id="pf" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>')
    t = T(40, 52, title, 26, 800) if title else ""
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(head + t + "".join(body) + "</svg>")
    print("gebaut:", name + ".svg")


# ===================================================================== Block 3
def vergessenskurve():
    b = []
    x0, y0, w, h = 90, 110, 760, 330
    b += [L(x0, y0 + h, x0 + w, y0 + h, INK, 2, arrow=True), L(x0, y0 + h, x0, y0 - 10, INK, 2, arrow=True)]
    b += [T(x0 - 14, y0 + 8, "100 %", 13, 600, MUTED, "end"), T(x0 + w, y0 + h + 30, "Zeit", 14, 600, MUTED, "end"),
          T(x0 - 50, y0 + h / 2, "abrufbar", 14, 600, MUTED, "middle")]

    def curve(xs, k, top=0.0):
        pts = []
        for i in range(0, 61):
            t = i / 60
            x = xs + t * (x0 + w - xs)
            y = y0 + top * h + (1 - top) * h * (1 - math.exp(-k * t * (x0 + w - xs) / 100)) * 0.92
            pts.append(f"{x:.1f},{y:.1f}")
        return "M" + " L".join(pts)

    b.append(P(curve(x0, 1.1), ROT, 3, dash="7 6"))
    xs = [x0, x0 + 150, x0 + 340, x0 + 560]
    ks = [1.1, 0.62, 0.36, 0.2]
    for i, (a, k) in enumerate(zip(xs, ks)):
        end = xs[i + 1] if i + 1 < len(xs) else x0 + w
        pts = []
        for j in range(0, 41):
            x = a + j / 40 * (end - a)
            y = y0 + h * (1 - math.exp(-k * (x - a) / 100)) * 0.92
            pts.append(f"{x:.1f},{y:.1f}")
        b.append(P("M" + " L".join(pts), PETROL, 4))
        if i + 1 < len(xs):
            yl = y0 + h * (1 - math.exp(-k * (end - a) / 100)) * 0.92
            b += [L(end, yl, end, y0 + 4, PETROL, 2.5, "4 4"), C(end, y0, 7, AMBER),
                  T(end, y0 - 16, f"Abruf {i + 1}", 13, 700, AMBER, "middle")]
    b += [T(x0 + 330, y0 + h - 44, "ohne Wiederholung", 14, 600, ROT), T(x0 + 580, y0 + 200, "mit Abruf in\nwachsenden Abständen", 14, 700, PETROL)]
    b.append(T(40, 505, "Jeder Abruf setzt neu an, danach fällt die Kurve flacher. Schematische Darstellung nach Ebbinghaus.", 14, 400, MUTED))
    save("b3-vergessenskurve", 900, 530, b, "Vergessen ist der Normalfall – Abruf bricht die Kurve")


def kaskade():
    b = []
    rows = [("Das Arbeitsgedächtnis ist eng.", ["kleine Schritte, Halbier-Regel (M2.3)", "Routinen schaffen Platz zum Denken (Block 1)", "Material entlasten (M3.2)"], BLAU),
            ("Erinnert wird, worüber\nnachgedacht wurde.", ["Aufmerksamkeit lenken (M3.3)", "Stifte weg beim Vormachen (M2.3)", "Aufgaben, die den Zielgedanken verlangen"], AMBER),
            ("Vergessen ist der Normalfall.", ["Do Now mit altem Stoff (M2.6)", "Abruf ohne Note (M3.4)", "verteilen und mischen (M3.5)"], PETROL)]
    y = 90
    for satz, tools, col in rows:
        b += [R(40, y, 300, 120, CARD, col, 12, 3), T(190, y + (56 if "\n" in satz else 66), satz, 17, 700, INK, "middle")]
        b.append(L(340, y + 60, 398, y + 60, col, 3, arrow=True))
        for i, tl in enumerate(tools):
            b += [R(405, y + i * 42, 455, 36, CARD, LINE, 8), C(423, y + i * 42 + 18, 5, col), T(438, y + i * 42 + 23, tl, 14.5)]
        y += 150
    b.append(T(40, y + 6, "Block 1 und 2 waren angewandte Gedächtnispsychologie.", 15, 600, MUTED))
    save("b3-kaskade", 900, 570, b, "Drei Kernsätze und die Werkzeuge, die darauf antworten")


def wasserkreislauf(x, y, s, labels=True, zahlen=True):
    """Kreislauf-Diagramm; s = Skalierung."""
    b = [f'<g transform="translate({x},{y}) scale({s})">']
    b.append('<path d="M0 230 Q60 205 120 230 T240 230 T360 230 L360 290 L0 290z" fill="#BFD7EA"/>')
    b.append('<path d="M360 290 L360 200 L470 90 L560 180 L620 150 L620 290z" fill="#C9CFB8"/>')
    b.append('<ellipse cx="180" cy="55" rx="80" ry="30" fill="#FFFFFF" stroke="#9AA6AA" stroke-width="2"/>')
    b.append('<ellipse cx="455" cy="50" rx="75" ry="28" fill="#DDE3E6" stroke="#9AA6AA" stroke-width="2"/>')
    b.append(P("M120 215 C100 160 120 120 150 92", BLAU, 4, arrow=True))
    b.append(P("M262 50 L372 48", BLAU, 4, arrow=True))
    for dx in (430, 455, 480):
        b.append(L(dx, 85, dx - 10, 125, BLAU, 3))
    b.append(P("M520 200 C470 250 420 262 372 250", BLAU, 4, arrow=True))
    if labels:
        b += [T(-45, 200, "1 Verdunstung", 17, 700), T(95, 16, "2 Kondensation", 17, 700),
              T(500, 112, "3 Niederschlag", 17, 700), T(405, 282, "4 Abfluss", 17, 700)]
    if zahlen:
        b += [T(-45, 150, "86 % aus\nden Ozeanen", 14, 600, PETROL), T(272, 8, "etwa 9 Tage\nin der Luft", 14, 600, PETROL)]
    b.append("</g>")
    return b


def horrorfolie():
    b = [R(20, 20, 920, 520, CARD, LINE, 6)]
    b.append(T(40, 62, "Der Wasserkreislauf – Grundlagen, Teilprozesse und Sonderfälle im Überblick", 21, 700))
    text = ("Der Wasserkreislauf beschreibt den ständigen Transport und die Speicherung von Wasser auf der Erde,\n"
            "wobei das Wasser, das an der Oberfläche der Ozeane und in geringerem Maß auch an Landflächen durch\n"
            "die Energie der Sonne verdunstet, in der Atmosphäre aufsteigt und dort, sobald es in höheren und damit\n"
            "kälteren Schichten abkühlt, an kleinsten Teilchen zu Tröpfchen kondensiert, aus denen sich Wolken\n"
            "bilden, die vom Wind verfrachtet werden, bis die Tröpfchen so schwer geworden sind, dass sie als\n"
            "Niederschlag in Form von Regen, Schnee oder Hagel wieder zur Erde fallen, wo das Wasser teils\n"
            "versickert und das Grundwasser speist, teils oberirdisch über Bäche und Flüsse abfließt und\n"
            "schließlich wieder ins Meer gelangt, womit der Kreislauf von vorn beginnt, wobei zu beachten ist,\n"
            "dass ein Teil des Niederschlags bereits vor Erreichen des Bodens wieder verdunstet und ein weiterer\n"
            "Teil von Pflanzen aufgenommen und über die Blätter abgegeben wird (Transpiration), sodass man\n"
            "zusammenfassend auch von Evapotranspiration spricht.")
    b.append(T(40, 96, text, 12.5, 400, INK, lh=1.42))
    b.append(T(40, 310, "• Sonderfälle", 14, 700))
    b.append(T(58, 332, "– Sublimation (Eis → Wasserdampf)\n     · v. a. in Hochgebirgen und Polargebieten\n– Interzeption (Benetzung der Vegetation)\n     · abhängig von Blattfläche und Niederschlagsart\n– Oberflächenabfluss vs. Zwischenabfluss vs. Basisabfluss\n     · siehe Abflussganglinie (nächste Stunde)", 12.5, 400, INK, lh=1.5))
    b += wasserkreislauf(620, 360, 0.48, labels=False, zahlen=False)
    # Clipart-Sonne mit Sonnenbrille
    b += [C(830, 300, 34, "#F4C430", "#D9A21E", 3)]
    for a in range(0, 360, 30):
        r1, r2 = 40, 54
        b.append(L(830 + r1 * math.cos(math.radians(a)), 300 + r1 * math.sin(math.radians(a)),
                   830 + r2 * math.cos(math.radians(a)), 300 + r2 * math.sin(math.radians(a)), "#D9A21E", 4))
    b += [R(808, 288, 20, 13, INK, INK, 4), R(832, 288, 20, 13, INK, INK, 4), L(828, 292, 832, 292, INK, 3),
          P("M815 314 Q830 326 845 314", INK, 3)]
    b.append(T(915, 525, "Folie 7 von 43", 11, 400, MUTED, "end"))
    save("b3-horrorfolie", 960, 560, b, "", "#F3F3F3")


def zwillingsfolie():
    b = [R(20, 20, 920, 520, CARD, LINE, 6), T(50, 70, "Der Wasserkreislauf", 28, 800)]
    b += wasserkreislauf(170, 130, 1.18)
    save("b3-zwillingsfolie", 960, 560, b, "", "#F3F3F3")


def lastquellen():
    b = []
    cols = [("Split Attention", "Zwei Quellen wollen\ngleichzeitig gelesen werden.", "Beispiel: Die Klasse liest die Folie,\nwährend du etwas anderes erzählst.", ROT),
            ("Redundanz", "Dasselbe kommt doppelt\nund muss abgeglichen werden.", "Beispiel: Du liest den Folientext\nwörtlich vor.", AMBER),
            ("Transienz", "Gesprochenes ist sofort weg.", "Beispiel: Die Anweisung mit drei\nSchritten gibt es nur mündlich.", BLAU)]
    for i, (name, was, bsp, col) in enumerate(cols):
        x = 40 + i * 290
        b += [R(x, 85, 270, 370, CARD, LINE, 12), R(x, 85, 270, 8, col, col, 4), T(x + 135, 128, name, 21, 800, col, "middle")]
        cx, cy = x + 135, 215
        if i == 0:
            b += [R(cx - 100, cy - 35, 70, 50, PSOFT, PETROL, 6), T(cx - 65, cy - 4, "Folie", 13, 600, PETROL, "middle"),
                  R(cx + 30, cy - 35, 70, 50, YSOFT, AMBER, 6), T(cx + 65, cy - 4, "Rede", 13, 600, AMBER, "middle"),
                  P(f"M{cx - 65} {cy + 18} L{cx - 8} {cy + 58}", PETROL, 3, arrow=True), P(f"M{cx + 65} {cy + 18} L{cx + 8} {cy + 58}", AMBER, 3, arrow=True),
                  C(cx, cy + 72, 15, CARD, ROT, 3), T(cx, cy + 78, "!", 18, 800, ROT, "middle")]
        elif i == 1:
            b += [R(cx - 80, cy - 35, 160, 34, PSOFT, PETROL, 6), T(cx, cy - 13, "Text lesen", 13, 600, PETROL, "middle"),
                  R(cx - 80, cy + 8, 160, 34, PSOFT, PETROL, 6), T(cx, cy + 30, "denselben Text hören", 12, 600, PETROL, "middle"),
                  T(cx, cy + 76, "= 2 × Aufwand, 1 × Inhalt", 13, 700, AMBER, "middle")]
        else:
            for k, op in enumerate([1, .6, .3, .1]):
                b.append(f'<text x="{cx - 104 + k * 74}" y="{cy + 10}" font-size="14" font-weight="700" fill="{BLAU}" opacity="{op}">Schritt {k + 1}</text>' if k < 3 else "")
            b += [P(f"M{cx - 96} {cy + 40} L{cx + 86} {cy + 40}", BLAU, 2.5, dash="2 7", arrow=True), T(cx, cy + 72, "verweht", 13, 700, BLAU, "middle", italic=True)]
        b += [T(x + 135, 325, was, 15, 600, INK, "middle"), T(x + 135, 392, bsp, 13, 400, MUTED, "middle")]
    b.append(R(40, 475, 850, 54, PSOFT, PETROL, 10))
    b.append(T(465, 508, "Schwer darf die Sache sein – nicht der Weg zu ihr.", 18, 700, PETROL, "middle"))
    save("b3-lastquellen", 930, 550, b, "Drei Quellen unnötiger Belastung")


def experimentfolie():
    b = [R(20, 20, 860, 500, CARD, LINE, 6), T(50, 66, "Energieverbrauch von Organen in Ruhe", 23, 800)]
    x0, y0, h = 150, 110, 310
    b += [L(x0, y0, x0, y0 + h, INK, 2), L(x0, y0 + h, x0 + 480, y0 + h, INK, 2)]
    for v in (0, 10, 20, 30):
        y = y0 + h - v * 10
        b += [L(x0 - 6, y, x0 + 480, y, LINE, 1), T(x0 - 12, y + 5, str(v), 13, 400, MUTED, "end")]
    b.append(f'<text x="{x0 - 62}" y="{y0 + h / 2}" font-size="13" fill="{MUTED}" text-anchor="middle" transform="rotate(-90 {x0 - 62} {y0 + h / 2})">% des Grundumsatzes</text>')
    for i, (n, v) in enumerate([("Leber", 27), ("Gehirn", 19), ("Muskeln", 18), ("Herz", 7)]):
        x = x0 + 40 + i * 110
        b += [R(x, y0 + h - v * 10, 70, v * 10, PETROL, PETROL, 3), T(x + 35, y0 + h - v * 10 - 8, str(v), 14, 700, INK, "middle"), T(x + 35, y0 + h + 24, n, 15, 600, INK, "middle")]
    # Cartoon-Gehirn mit Hantel
    gx, gy = 745, 395
    b += [f'<path d="M{gx - 42} {gy} q-12 -34 22 -42 q14 -22 42 -8 q30 -4 30 26 q14 20 -8 36 q-10 20 -40 12 q-34 10 -46 -24z" fill="#F2B8C0" stroke="#B0433A" stroke-width="3"/>',
          P(f"M{gx - 20} {gy - 26} q14 10 6 26 M{gx + 10} {gy - 34} q-6 18 12 26 M{gx - 26} {gy + 6} q20 -4 30 12", ROT, 2.5),
          C(gx - 8, gy - 4, 4, INK), C(gx + 16, gy - 4, 4, INK), P(f"M{gx - 6} {gy + 12} q10 8 22 0", INK, 2.5),
          L(gx - 78, gy - 66, gx + 74, gy - 66, INK, 5), R(gx - 92, gy - 82, 16, 32, INK, INK, 3), R(gx + 72, gy - 82, 16, 32, INK, INK, 3),
          L(gx - 34, gy - 26, gx - 50, gy - 64, ROT, 4), L(gx + 44, gy - 22, gx + 54, gy - 64, ROT, 4),
          R(gx - 22, gy - 138, 108, 38, CARD, INK, 12, 2), T(gx + 32, gy - 112, "Leg day!", 17, 800, INK, "middle"),
          P(f"M{gx + 14} {gy - 100} l-6 16 l18 -16", INK, 2, CARD)]
    b.append(f'<text x="652" y="150" font-size="24" fill="{BLAU}" font-family="\'Segoe Print\',\'Bradley Hand\',\'Comic Sans MS\',cursive" transform="rotate(-8 652 150)">krass, oder?!</text>')
    save("b3-experimentfolie", 900, 540, b, "", "#F3F3F3")


def paradox():
    b = []
    x0, y0, h = 110, 100, 300
    b += [L(x0, y0 + h, 820, y0 + h, INK, 2), L(x0, y0, x0, y0 + h, INK, 2)]
    for v in (0, 25, 50, 75, 100):
        y = y0 + h - v * 3
        b += [L(x0, y, 820, y, LINE, 1), T(x0 - 10, y + 5, f"{v} %", 13, 400, MUTED, "end")]
    data = [("Ende der Übungsstunde", 85, 65, 180), ("Test nach vier Wochen", 45, 70, 520)]
    for lab, g, v, x in data:
        b += [R(x, y0 + h - g * 3, 90, g * 3, ROT, ROT, 3), T(x + 45, y0 + h - g * 3 - 9, f"{g} %", 15, 700, ROT, "middle"),
              R(x + 110, y0 + h - v * 3, 90, v * 3, PETROL, PETROL, 3), T(x + 155, y0 + h - v * 3 - 9, f"{v} %", 15, 700, PETROL, "middle"),
              T(x + 100, y0 + h + 28, lab, 16, 700, INK, "middle")]
    b += [T(280, y0 + h + 52, "Leistung in der Stunde", 14, 400, MUTED, "middle"), T(620, y0 + h + 52, "Lernen", 14, 400, MUTED, "middle")]
    b += [R(640, 78, 16, 16, ROT, ROT, 3), T(664, 92, "am Stück geübt", 14, 600), R(640, 102, 16, 16, PETROL, PETROL, 3), T(664, 116, "verteilt geübt", 14, 600)]
    b.append(T(40, 510, "Gleiche Übungszeit, zwei Arten zu üben. Werte zur Veranschaulichung im Rahmen typischer Befunde (Bjork u. a.).", 13.5, 400, MUTED))
    save("b3-paradox", 900, 530, b, "Was heute glatt läuft, ist nicht, was bleibt")


def landkarte_wdh():
    b = []
    x0, y0, cw = 190, 100, 34
    for wk in range(1, 21):
        b.append(T(x0 + (wk - 1) * cw + cw / 2, y0 - 10, str(wk), 12, 600, MUTED, "middle"))
    b.append(T(x0 - 14, y0 - 10, "Woche", 12, 600, MUTED, "end"))
    themen = [("Bruchrechnung", 1, 4, BLAU, [5, 8, 14]), ("Terme", 5, 8, AMBER, [9, 12, 18]), ("Gleichungen", 9, 13, PETROL, [14, 17]), ("Geometrie", 14, 17, GRUEN, [18]), ("Zuordnungen", 18, 20, ROT, [])]
    for i, (name, a, e, col, wd) in enumerate(themen):
        y = y0 + i * 62
        b += [R(40, y + 6, 140, 40, CARD, LINE, 8), T(110, y + 31, name, 14, 700, col, "middle")]
        for wk in range(1, 21):
            b.append(R(x0 + (wk - 1) * cw, y + 6, cw - 4, 40, CARD, LINE, 4, 1))
        b.append(R(x0 + (a - 1) * cw, y + 6, (e - a + 1) * cw - 4, 40, col, col, 4))
        b.append(T(x0 + (a - 1) * cw + ((e - a + 1) * cw - 4) / 2, y + 31, "Einheit", 12, 700, "#fff", "middle"))
        for wk in wd:
            b.append(C(x0 + (wk - 1) * cw + cw / 2 - 2, y + 26, 10, CARD, col, 3.5))
    y = y0 + 5 * 62 + 20
    b += [R(40, y, 24, 16, MUTED, MUTED, 3), T(72, y + 13, "Einheit läuft", 13), C(210, y + 8, 8, CARD, MUTED, 3), T(226, y + 13, "kehrt wieder: im Do Now, auf dem Übungsblatt, in der Klassenarbeit", 13)]
    b.append(T(40, y + 46, "Faustlinie für die Abstände: nach 1 Woche, nach 4 Wochen, nach 10 Wochen. Kein Thema bleibt ohne Wiederkehr. (Beispiel: Mathematik, Kl. 7)", 13.5, 400, MUTED))
    save("b3-wiederholungslandkarte", 900, 520, b, "Wiederholungs-Landkarte für ein Halbjahr")


def ko_gut():
    b = [R(30, 30, 840, 590, CARD, LINE, 6), T(55, 72, "Knowledge Organizer · Wasser als Stoff · Chemie, Klasse 8", 20, 800, PETROL)]
    begriffe = [("Molekül", "Teilchen aus mindestens zwei verbundenen Atomen"), ("Aggregatzustand", "fest, flüssig oder gasförmig"),
                ("Schmelzen", "Übergang von fest zu flüssig (bei Wasser 0 °C)"), ("Sieden", "Übergang von flüssig zu gasförmig (100 °C)"),
                ("Kondensieren", "Übergang von gasförmig zu flüssig"), ("Dichte", "Masse pro Volumen (g/cm³)"),
                ("Anomalie", "Wasser ist bei 4 °C am dichtesten; Eis schwimmt"), ("Lösung", "Gemisch aus Lösungsmittel und gelöstem Stoff")]
    b += [T(55, 108, "Begriff", 13, 700, MUTED), T(215, 108, "Erklärung (zum Abdecken)", 13, 700, MUTED)]
    for i, (k, v) in enumerate(begriffe):
        y = 120 + i * 34
        b += [R(50, y, 155, 28, PSOFT, PSOFT, 5), T(60, y + 19, k, 14, 700), R(210, y, 350, 28, CARD, LINE, 5, 1), T(220, y + 19, v, 13)]
    b.append(L(207, 112, 207, 392, AMBER, 2, "5 5"))
    b += [T(590, 108, "Schaubild: Teilchenmodell", 13, 700, MUTED)]
    for j, (lab, n, gap) in enumerate([("fest", 9, 16), ("flüssig", 7, 21), ("gasförmig", 3, 34)]):
        bx = 590 + j * 92
        b += [R(bx, 120, 80, 80, BG, LINE, 6, 1), T(bx + 40, 218, lab, 12, 600, INK, "middle")]
        pos = [(k % 3, k // 3) for k in range(n)]
        for (px, py) in pos:
            off = (py % 2) * 5 if j == 1 else 0
            b.append(C(bx + 16 + px * gap * (1 if j < 2 else .9) + off, 136 + py * gap, 7, BLAU))
    b += [T(590, 262, "Drei Zusammenhänge", 13, 700, MUTED)]
    for i, s in enumerate(["Wenn Wasser erwärmt wird, dann\nbewegen sich die Teilchen schneller.", "Wenn Wasser gefriert,\ndann dehnt es sich aus.", "Wenn die Dichte kleiner ist als die\nvon Wasser, dann schwimmt der Stoff."]):
        b += [R(590, 272 + i * 50, 262, 42, YSOFT, GELB, 6, 1), T(600, 290 + i * 50 + (0 if "\n" in s else 8), s, 12.5)]
    b += [T(55, 430, "Zwei Zahlen", 13, 700, MUTED), R(50, 440, 250, 34, CARD, LINE, 5, 1), T(60, 462, "Schmelztemperatur: 0 °C", 13.5), R(310, 440, 250, 34, CARD, LINE, 5, 1), T(320, 462, "Siedetemperatur: 100 °C", 13.5)]
    b.append(R(50, 500, 800, 96, GSOFT, GRUEN, 10))
    b.append(T(70, 530, "Warum dieser Organizer taugt", 15, 800, GRUEN))
    b.append(T(70, 555, "✓ eine Seite   ✓ nur Kernwissen (8 Begriffe)   ✓ rechte Spalte lässt sich abdecken   ✓ Schülersprache", 14))
    b.append(T(70, 580, "So lernt man damit: abdecken → antworten → aufdecken → Haken oder Kreis.", 14, 600))
    save("b3-ko-gut", 900, 650, b, "")


def ko_ueberladen():
    b = [R(30, 30, 840, 560, CARD, LINE, 6), T(55, 64, "WEIMARER REPUBLIK – Gesamtübersicht (Teil 1 von 2)", 15, 800), T(560, 64, "epochenspezifische Kontingenzerfahrungen", 11, 400, INK, italic=True)]
    import random
    random.seed(4)
    w = ("Novemberrevolution Rätebewegung Dolchstoßlegende Spartakusaufstand Nationalversammlung Reichsverfassung Artikel 48 Versailler Vertrag Reparationen "
         "Kapp-Putsch Ruhrkampf Hyperinflation Rentenmark Dawes-Plan Locarno Völkerbund Goldene Zwanziger Weltwirtschaftskrise Präsidialkabinette Notverordnung "
         "Harzburger Front Reichstagswahl Machtübertragung Ermächtigungsgesetz Parteienzersplitterung Verhältniswahlrecht Legitimationsdefizit Republikfeindschaft "
         "Freikorps Fememorde Young-Plan Brüning Papen Schleicher Hindenburg Ebert Stresemann Rathenau Erzberger Scheidemann").split(" ")
    boxes = [(45, 80, 270, 235), (325, 80, 250, 150), (585, 80, 270, 190), (325, 240, 250, 190), (45, 325, 270, 250), (585, 280, 270, 295), (325, 440, 250, 135)]
    k = 0
    for (x, y, bw, bh) in boxes:
        b.append(R(x, y, bw, bh, random.choice([CARD, YSOFT, "#F1F1F1", PSOFT]), MUTED, 2, 1))
        size = random.choice([8.5, 9.5, 11])
        lines, line = [], ""
        maxc = int(bw / (size * 0.56))
        while len(lines) * size * 1.35 < bh - 24:
            word = w[k % len(w)]; k += 1
            filler = random.choice([" und ", ", wobei ", " (vgl. ", " sowie ", " – siehe auch ", " infolge der "])
            if len(line) + len(word) + len(filler) > maxc:
                lines.append(line); line = ""
            line += word + filler
        b.append(T(x + 8, y + 16, "\n".join(lines), size, 400, INK, lh=1.35))
    b.append(R(50, 600, 800, 0, CARD, CARD))
    save("b3-ko-ueberladen", 900, 620, b + [R(40, 596, 820, 2, BG, BG, 0, 0)], "")


def mindmap():
    b = []
    for off, title, beschriftet in [(0, "ohne beschriftete Linien", False), (460, "mit beschrifteten Linien", True)]:
        col = PETROL if beschriftet else GRAU
        b += [R(30 + off, 80, 420, 400, CARD, LINE, 12), T(240 + off, 112, title, 17, 800, col, "middle")]
        cx, cy = 240 + off, 290
        nodes = [("Inflation 1923", -130, -100, "zerstört\nErsparnisse"), ("Versailler\nVertrag", 130, -100, "belastet durch\nReparationen"), ("Notverordnungen", -130, 110, "umgehen das\nParlament"), ("Wirtschafts-\nkrise 1929", 130, 110, "treibt Wähler zu\nden Extremen")]
        for name, dx, dy, lab in nodes:
            b.append(L(cx, cy, cx + dx, cy + dy, col, 2.5))
            if beschriftet:
                b += [R(cx + dx / 2 - 58, cy + dy / 2 - 19, 116, 38, YSOFT, GELB, 6, 1), T(cx + dx / 2, cy + dy / 2 - 3, lab, 11.5, 600, INK, "middle", 1.2)]
        for name, dx, dy, lab in nodes:
            b += [R(cx + dx - 62, cy + dy - 24, 124, 48, CARD, col, 10, 2), T(cx + dx, cy + dy + (-3 if "\n" in name else 5), name, 13, 700, INK, "middle", 1.2)]
        b += [R(cx - 70, cy - 28, 140, 56, col, col, 12), T(cx, cy - 2, "Scheitern der\nRepublik", 14, 800, "#fff", "middle", 1.2)]
    b += [T(240, 510, "Begriffe verbinden geht ohne Nachdenken.", 14, 600, MUTED, "middle"), T(700, 510, "An der Linie steht, WIE es zusammenhängt.", 14, 700, PETROL, "middle")]
    save("b3-mindmap", 920, 540, b, "Dieselbe Mindmap – einmal Dekoration, einmal Denkarbeit")


def blockkarte(name, title, frage, module, rueck, col):
    b = [R(40, 78, 860, 54, PSOFT, col, 10), T(470, 112, frage, 17, 700, col, "middle")]
    n = len(module)
    w = (860 - (n - 1) * 14) / n
    for i, (nr, t, kern) in enumerate(module):
        x = 40 + i * (w + 14)
        b += [R(x, 160, w, 170, CARD, LINE, 12), R(x, 160, w, 8, col, col, 4), T(x + w / 2, 196, nr, 20, 800, col, "middle"),
              T(x + w / 2, 222, t, 13, 700, INK, "middle", 1.25), T(x + w / 2, 282, kern, 11.5, 400, MUTED, "middle", 1.3)]
        if i < n - 1:
            b.append(L(x + w + 1, 245, x + w + 13, 245, col, 2.5, arrow=True))
    b.append(T(40, 372, "Baut auf", 14, 800, MUTED))
    rw = (860 - (len(rueck) - 1) * 14) / len(rueck)
    for i, r_ in enumerate(rueck):
        x = 40 + i * (rw + 14)
        b += [R(x, 384, rw, 58, CARD, LINE, 10, 1.5, 'stroke-dasharray="5 4"'), T(x + rw / 2, 408 + (0 if "\n" in r_ else 8), r_, 12.5, 500, INK, "middle", 1.3)]
    save(name, 940, 470, b, title)


# ===================================================================== Block 4
def frage_pause_name():
    b = []
    for row, (lab, segs, col, note) in enumerate([
        ("So denken alle:", [("Frage", 250, PETROL), ("Pause 3–5 Sek.", 300, AMBER), ("Name", 110, BLAU)], PETROL, "Bis der Name fällt, kann jeder gemeint sein."),
        ("So denkt einer:", [("Name", 110, BLAU), ("Frage", 250, GRAU), ("Antwort", 190, GRAU)], ROT, "Mit dem Namen wissen alle anderen: Ich bin nicht gemeint.")]):
        y = 110 + row * 190
        b.append(T(40, y, lab, 18, 800, col))
        x = 40
        for (t, w, c) in segs:
            b += [R(x, y + 16, w - 6, 56, c, c, 8), T(x + (w - 6) / 2, y + 51, t, 16, 700, "#fff", "middle")]
            x += w
        # Köpfe
        for k in range(14):
            aktiv = (row == 0) or k == 3
            b.append(C(60 + k * 46, y + 112, 15, PSOFT if aktiv else "#E4E6E0", PETROL if aktiv else LINE, 2.5))
            if aktiv:
                b.append(T(60 + k * 46, y + 118, "💭" if False else "…", 16, 800, PETROL, "middle"))
        b.append(T(710, y + 118, note, 13.5, 600, col, lh=1.3) if False else T(40, y + 152, note, 14, 600, col))
    save("b4-frage-pause-name", 900, 480, b, "Frage – Pause – Name: Die Reihenfolge entscheidet")


def heatmap():
    b = [R(330, 78, 240, 30, INK, INK, 4), T(450, 99, "Tafel", 14, 700, "#fff", "middle")]
    import random
    random.seed(11)
    counts = [[4, 5, 3, 4, 2, 1], [3, 4, 2, 2, 1, 0], [2, 1, 1, 1, 0, 0], [1, 0, 0, 1, 0, 0]]
    for r_, row in enumerate(counts):
        for c_, n in enumerate(row):
            x, y = 110 + c_ * 118, 135 + r_ * 84
            fill = [CARD, "#F9E9C9", "#F2C27A", "#E79A4A", "#D26A3A", "#B0433A"][n]
            b += [R(x, y, 100, 64, fill, LINE, 8)]
            for k in range(n):
                b.append(C(x + 16 + k * 17, y + 32, 6, INK if k % 2 else CARD, INK, 2))
            if n == 0:
                b.append(T(x + 50, y + 38, "–", 16, 400, MUTED, "middle"))
    b += [R(456, 290, 366, 190, "none", BLAU, 12, 3, 'stroke-dasharray="8 6"'), T(626, 500, "kalte Zone: seit Wochen keine Stimme", 14, 700, BLAU, "middle")]
    b += [C(120, 510, 6, CARD, INK, 2), T(134, 515, "Aufruf ohne Meldung", 13), C(300, 510, 6, INK, INK, 2), T(314, 515, "Meldung", 13)]
    b.append(T(40, 548, "Der Coach setzt für jeden Aufruf einen Punkt auf den Sitzplan. Zwei kalte Zonen werden zum Ziel der nächsten Woche.", 13.5, 400, MUTED))
    save("b4-heatmap", 900, 570, b, "Beteiligungs-Heatmap: Wer kommt dran?")


def choreografie():
    b = []
    segs = [("Alle schreiben", "1–3 Min.", "Aufgabe + Zeit ansagen,\n„Stift läuft“", 330, PETROL),
            ("Partnergespräch", "30–90 Sek.", "feste Partner,\nLehrkraft hört zu", 190, AMBER),
            ("Aufrufen", "2–3 Aufrufe", "davon einer: „Was hat\ndein Partner gesagt?“", 300, BLAU)]
    x = 40
    for i, (t, zeit, sub, w, c) in enumerate(segs):
        b += [R(x, 110, w - 10, 90, c, c, 10), T(x + (w - 10) / 2, 148, t, 19, 800, "#fff", "middle"), T(x + (w - 10) / 2, 178, zeit, 15, 600, "#fff", "middle"),
              T(x + (w - 10) / 2, 236, sub, 14, 400, INK, "middle")]
        if i < 2:
            b += [L(x + w - 5, 92, x + w - 5, 218, INK, 2.5, "4 4"), T(x + w - 5, 84, "Signal", 12, 700, INK, "middle")]
        x += w
    b.append(R(40, 300, 820, 150, CARD, LINE, 12))
    b.append(T(60, 332, "Vier Fehler, an denen das Format scheitert", 16, 800))
    for i, (f, fix) in enumerate([("zu lang", "beenden, solange das Gespräch dicht ist"), ("ungenaue Frage", "eine Entscheidung einbauen: einigt euch, wählt, ordnet"),
                                  ("keine Auswertung", "immer zwei bis drei Aufrufe danach"), ("Lehrkraft am Pult", "herumgehen und zuhören")]):
        yy = 360 + i * 22
        b += [T(60, yy, "✗ " + f, 14, 700, ROT), T(250, yy, "→ " + fix, 14)]
    save("b4-choreografie", 900, 480, b, "Schreiben – Sprechen – Aufrufen")


def entscheidungsbaum():
    b = [R(320, 78, 260, 52, PETROL, PETROL, 10), T(450, 110, "1 Welches Muster?", 17, 800, "#fff", "middle")]
    b += [L(400, 130, 220, 180, MUTED, 2.5, arrow=True), L(500, 130, 680, 180, MUTED, 2.5, arrow=True)]
    b += [R(60, 184, 330, 50, CARD, PETROL, 10, 2), T(225, 215, "ein Fehler bei vielen", 16, 700, INK, "middle"),
          R(510, 184, 330, 50, CARD, AMBER, 10, 2), T(675, 215, "viele verschiedene Fehler", 16, 700, INK, "middle")]
    opts = [(40, "mehr als ein Drittel", "10 Minuten für\ndie ganze Klasse", ROT), (250, "10 bis 30 %", "Kleingruppe, während\nder Rest übt", GELB), (460, "einzelne", "Hinweis beim\nRundgang", GRUEN),
            (670, "verstreut", "Checkpoints, Kleingruppen\nim Wechsel, Einzelhinweise", AMBER)]
    for x, kopf, text, c in opts:
        b += [R(x, 290, 195, 110, CARD, LINE, 10), R(x, 290, 195, 34, c, c, 8), T(x + 97, 313, kopf, 14, 800, "#fff" if c != GELB else INK, "middle"), T(x + 97, 350, text, 13.5, 500, INK, "middle")]
    for x in (137, 347, 557):
        b.append(L(225 if x < 600 else 675, 234, x, 286, MUTED, 2, arrow=True))
    b.append(L(675, 234, 767, 286, MUTED, 2, arrow=True))
    b += [R(362, 248, 180, 30, BG, BG, 6), T(452, 269, "2 Welches Format?", 16, 800, PETROL, "middle")]
    b += [R(40, 430, 825, 70, PSOFT, PETROL, 10), T(452, 458, "3 Welcher NEUE Zugang?", 16, 800, PETROL, "middle"),
          T(452, 484, "anderes Beispiel · andere Darstellung · eine Stufe der Treppe tiefer – nie dieselbe Erklärung noch einmal", 13.5, 500, INK, "middle")]
    save("b4-entscheidungsbaum", 905, 525, b, "Vom Stapel zur Entscheidung: drei Fragen")


def set_a_b():
    b = []
    sets = [("Set A", [("richtig", 13, GRUEN), ("Klammer falsch aufgelöst", 10, ROT), ("leer", 2, GRAU)], "Ein Muster → neuer Anlauf für alle", PETROL),
            ("Set B", [("richtig", 14, GRUEN), ("Klammer", 3, ROT), ("Vorzeichen", 3, AMBER), ("Rechenfehler", 2, BLAU), ("kein Ansatz", 3, GRAU)], "Vier Ursachen → gezielt reagieren", AMBER)]
    for i, (name, parts, fazit, col) in enumerate(sets):
        x0 = 40 + i * 440
        b += [R(x0, 80, 410, 400, CARD, LINE, 12), T(x0 + 20, 116, name + " · 25 Tickets", 18, 800)]
        k = 0
        for lab, n, c in parts:
            for _ in range(n):
                b.append(R(x0 + 20 + (k % 10) * 37, 136 + (k // 10) * 34, 31, 27, c, c, 4)); k += 1
        y = 256
        for lab, n, c in parts:
            b += [R(x0 + 20, y, 14, 14, c, c, 3), T(x0 + 42, y + 12, f"{n} × {lab}", 14)]; y += 24
        falsch = 25 - parts[0][1]
        b += [T(x0 + 20, 410, f"{falsch} von 25 mit Fehlern", 15, 700, MUTED), R(x0 + 20, 424, 370, 40, PSOFT if col == PETROL else YSOFT, col, 8), T(x0 + 205, 450, fazit, 15, 800, col, "middle")]
    b.append(T(40, 512, "Aufgabe: „Löse 3(x − 2) = 15 und erkläre deinen ersten Schritt.“ Fast gleiche Fehlerquote, andere Verteilung, andere Entscheidung.", 13.5, 400, MUTED))
    save("b4-set-a-b", 900, 535, b, "Fast gleiche Fehlerquote – verschiedene Entscheidungen")


# ===================================================================== Block 5
def evk():
    b = [R(40, 78, 860, 96, CARD, PETROL, 14, 2.5)]
    b.append(T(470, 138, "Anstrengung  =  Erwartung  ×  Wert  ÷  Kosten", 30, 800, PETROL, "middle"))
    b += [T(380, 196, "„Schaffe ich das?“", 13.5, 600, BLAU, "middle"), T(583, 196, "„Bringt es mir etwas?“", 13.5, 600, GRUEN, "middle"), T(770, 196, "„Was riskiere ich?“", 13.5, 600, ROT, "middle")]
    tr = [("1 Secure Success", "Erfolg ermöglichen", "Erwartung ↑", BLAU, "hohe Erfolgsquote, leichter\nEinstieg, Lob aufs Vorgehen"),
          ("2 Run Routines", "Routinen entlasten", "Kosten ↓", ROT, "jeder weiß, was zu tun ist;\nFehler sind sicher"),
          ("3 Nudge Norms", "Normen lenken", "Wert ↑", GRUEN, "die arbeitende Mehrheit\nsichtbar machen"),
          ("4 Build Belonging", "Zugehörigkeit", "Wert ↑  Kosten ↓", AMBER, "kurzer echter Kontakt,\nZusagen halten"),
          ("5 Boost Buy-in", "Zustimmung", "Wert ↑", GRUEN, "begründen, echte Wahl\nim Wie, System erklären")]
    for i, (en, de, wirk, c, bsp) in enumerate(tr):
        x = 40 + i * 174
        b += [R(x, 232, 164, 220, CARD, LINE, 12), R(x, 232, 164, 8, c, c, 4), T(x + 82, 268, en, 14.5, 800, INK, "middle"), T(x + 82, 290, de, 13.5, 500, MUTED, "middle"),
              R(x + 14, 306, 136, 34, c, c, 8), T(x + 82, 329, wirk, 14, 800, "#fff", "middle"), T(x + 82, 372, bsp, 11, 400, INK, "middle", 1.4)]
    b.append(T(40, 490, "Ist die Erwartung null, bleibt das Ergebnis null – egal wie spannend das Thema ist. Deshalb zuerst die Erwartung prüfen.", 14, 600, MUTED))
    save("b5-evk-treiber", 940, 515, b, "Warum Menschen sich anstrengen – und die fünf Treiber")


def eskalationsleiter():
    b = []
    stufen = ["1 Nonverbal: Blick, Geste, Nähe", "2 Positive Gruppenkorrektur", "3 Anonyme Einzelkorrektur", "4 Private Einzelkorrektur", "5 Blitzschnelle öffentliche Korrektur", "6 Konsequenz (Kette der Schule)"]
    for i, s in enumerate(stufen):
        y = 420 - i * 58
        c = [GRUEN, GRUEN, GELB, GELB, AMBER, ROT][i]
        b += [R(40 + i * 26, y, 420, 48, CARD, c, 8, 2.5), T(56 + i * 26, y + 30, s, 14.5, 700)]
    b += [T(40, 496, "Interventionsleiter aus Modul 1.5: immer die kleinste wirksame Stufe.", 13.5, 400, MUTED)]
    b += [R(640, 88, 250, 104, RSOFT, ROT, 10, 2), T(765, 114, "Stufe 6 im Detail (M5.4)", 14.5, 800, ROT, "middle"),
          T(765, 138, "angekündigt · ruhig · verhältnismäßig\nvorher: Rechnet er mit dem Scheitern?", 12.5, 500, INK, "middle", 1.5)]
    b.append(L(596, 150, 636, 140, ROT, 2.5, arrow=True))
    nach = [("Danach: Gespräch (W.I.N.)", "Die Konsequenz beendet den Vorfall,\ndas Gespräch verhindert den nächsten.", PETROL), ("Protokoll", "nur Beobachtungen, Uhrzeit,\nwörtliche Zitate – keine Wertungen", BLAU), ("Hilfe holen", "Lage – was ich versucht habe –\nmeine Frage", AMBER)]
    for i, (t, s, c) in enumerate(nach):
        y = 212 + i * 92
        b += [R(640, y, 250, 80, CARD, c, 10, 2), T(765, y + 26, t, 14.5, 800, c, "middle"), T(765, y + 48, s, 12, 400, INK, "middle", 1.4)]
        if i:
            b.append(L(765, y - 12, 765, y - 2, MUTED, 2, arrow=True))
    b.append(L(765, 192, 765, 210, MUTED, 2, arrow=True))
    save("b5-eskalationsleiter", 930, 520, b, "Wenn die Leiter nicht reicht: Stufe 6 und was danach kommt")


# ===================================================================== Block 6
def canvas():
    b = []
    b += [R(40, 80, 400, 150, CARD, ROT, 12, 2.5), T(58, 108, "1 Klassenarbeit skizzieren (zuerst!)", 15.5, 800, ROT),
          T(58, 134, "A1 Geraden zeichnen (Wiedergabe) · 8 P.\nA2 Steigung aus zwei Punkten (Anwendung) · 10 P.\nA3 Handytarife vergleichen (Transfer) · 8 P.\nA4 Bruchrechnung, alter Stoff (angekündigt) · 4 P.", 13, 400, INK, lh=1.5)]
    b += [R(460, 80, 440, 150, CARD, PETROL, 12, 2.5), T(478, 108, "2 Meilensteine der Einheit", 15.5, 800, PETROL),
          T(478, 134, "kann Punkte ablesen und eintragen\nkann eine Gerade aus der Gleichung zeichnen\nkann die Steigung bestimmen\nkann eine Sachsituation als Gleichung schreiben", 13, 400, INK, lh=1.5)]
    b += [R(40, 250, 860, 150, CARD, BLAU, 12, 2.5), T(58, 278, "3 Stundenkette (mit Bleistift) und Puffer", 15.5, 800, BLAU)]
    st = [("Std. 1", "Punkte"), ("Std. 2", "Zeichnen"), ("Std. 3", "Steigung"), ("Std. 4", "Steigung"), ("Std. 5", "Sach-\naufgaben"), ("Puffer", "frei"), ("Arbeit", "")]
    for i, (a, t) in enumerate(st):
        x = 58 + i * 118
        puf = a == "Puffer"
        b += [R(x, 294, 106, 62, YSOFT if puf else (RSOFT if a == "Arbeit" else PSOFT), AMBER if puf else LINE, 8, 2 if puf else 1, 'stroke-dasharray="6 4"' if puf else ""),
              T(x + 53, 316, a, 13.5, 800, INK, "middle"), T(x + 53, 334, t, 12, 400, INK, "middle", 1.15)]
    b.append(T(58, 384, "Nach jedem Exit Ticket: fünf Minuten am Abend – was ändert sich morgen?", 13, 600, MUTED))
    b += [R(40, 420, 860, 86, CARD, GRUEN, 12, 2.5), T(58, 448, "4 Stellen für die Wiederholung", 15.5, 800, GRUEN),
          T(58, 474, "Stoff aus Std. 1 kehrt in Std. 4 zurück (Do Now) · alte Einheit „Bruchrechnung“: Do Now ☑  Übungsblatt ☑  Arbeit ☑", 13, 400, INK)]
    save("b6-einheiten-canvas", 940, 530, b, "Eine Einheit rückwärts planen (Beispiel: Lineare Funktionen)")


def wcf():
    b = []
    steps = [("1 Lesen", "ohne Stift,\n30 Sek. je Arbeit", 15), ("2 Ein Bogen", "3 Stärken,\n3 Fehlermuster", 10), ("3 Feedback-\nstunde", "Stärken zeigen,\nneuer Zugang", 15), ("4 Überarbeiten", "grüner Stift,\nkonkreter Auftrag", 15), ("5 Stichprobe", "5–6 Arbeiten\nansehen", 10)]
    for i, (t, s, m) in enumerate(steps):
        x = 40 + i * 172
        c = AMBER if i == 3 else PETROL
        b += [R(x, 90, 160, 150, CARD, c, 12, 3 if i == 3 else 1.5), T(x + 80, 124 if "\n" not in t else 116, t, 16, 800, c, "middle", 1.15), T(x + 80, 172, s, 13, 400, INK, "middle", 1.4),
              T(x + 80, 224, f"{m} Min." + (" Stundenzeit" if i in (2, 3) else ""), 12.5, 700, MUTED, "middle")]
        if i < 4:
            b.append(L(x + 161, 165, x + 171, 165, PETROL, 2.5, arrow=True))
    b.append(T(646, 262, "Hier wird gelernt: Die Schüler arbeiten mit ihren Fehlern.", 13, 700, AMBER, "middle"))
    y = 310
    b += [T(40, y, "Lehrerzeit für einen Klassensatz Übungsarbeiten", 15, 800)]
    b += [R(40, y + 16, 820, 40, ROT, ROT, 6), T(52, y + 42, "Randkommentare an jeder Arbeit: etwa 7 Stunden", 14.5, 700, "#fff")]
    b += [R(40, y + 68, 110, 40, PETROL, PETROL, 6), T(162, y + 94, "Rückmeldung an die ganze Klasse: 45–60 Minuten", 14.5, 700, PETROL)]
    b.append(T(40, y + 142, "Gilt für Übungsformate. Bei benoteten Arbeiten bleiben die Vorgaben von Land und Fachkonferenz bestehen.", 13.5, 400, MUTED))
    save("b6-wcf-fuenfschritt", 900, 480, b, "Rückmeldung an die ganze Klasse in fünf Schritten")


def plateau():
    b = []
    x0, y0, w, h = 100, 100, 720, 300
    b += [L(x0, y0 + h, x0 + w + 20, y0 + h, INK, 2, arrow=True), L(x0, y0 + h, x0, y0 - 10, INK, 2, arrow=True), T(x0 + w + 20, y0 + h + 34, "Berufsjahre", 14, 600, MUTED, "end")]
    b.append(f'<text x="{x0 - 30}" y="{y0 + h / 2}" font-size="14" font-weight="600" fill="{MUTED}" text-anchor="middle" transform="rotate(-90 {x0 - 30} {y0 + h / 2})">Wirksamkeit</text>')
    for j in (1, 5, 10, 15, 20):
        x = x0 + j / 20 * w
        b += [L(x, y0 + h, x, y0 + h + 6, INK, 2), T(x, y0 + h + 22, str(j), 13, 400, MUTED, "middle")]
    fa = lambda t: 0.62 * (1 - math.exp(-t / 1.6)) + 0.004 * t
    fb = lambda t: 0.62 * (1 - math.exp(-t / 1.6)) + 0.016 * max(0, t - 1.5)
    for f, c, sw in ((fa, GRAU, 4), (fb, PETROL, 5)):
        pts = [f"{x0 + t / 20 * w:.1f},{y0 + h - f(t) * h:.1f}" for t in [i / 4 for i in range(0, 81)]]
        b.append(P("M" + " L".join(pts), c, sw))
    b += [T(x0 + w - 4, y0 + h - fa(20) * h + 26, "Erfahrung allein", 14.5, 700, GRAU, "end"), T(x0 + w - 4, y0 + h - fb(20) * h - 14, "gezielt üben, mit Rückmeldung", 14.5, 800, PETROL, "end")]
    xi, yi = x0 + 2 / 20 * w, y0 + h - fa(2) * h
    b += [C(xi, yi, 9, AMBER), L(xi + 12, yi + 10, xi + 70, yi + 52, AMBER, 2), T(xi + 76, yi + 62, "Ihr – heute (Ende Jahr 2)", 14.5, 800, AMBER)]
    x10 = x0 + 10 / 20 * w
    b += [L(x10, y0 + h - fa(10) * h - 6, x10, y0 + h - fb(10) * h + 6, INK, 2, "4 4"), T(x10 + 12, y0 + h - fa(10) * h + 26, "Der Abstand: kein Talent – ein System", 13.5, 700)]
    b.append(T(40, 480, "Schematisch. Der Zuwachs flacht nach den ersten Jahren ab; weiter wächst, wer gezielt übt und Rückmeldung bekommt.", 13.5, 400, MUTED))
    save("b6-plateau", 900, 505, b, "Zwei Wege nach dem Berufseinstieg")


for fn in (vergessenskurve, kaskade, horrorfolie, zwillingsfolie, lastquellen, experimentfolie, paradox, landkarte_wdh, ko_gut, ko_ueberladen, mindmap,
           frage_pause_name, heatmap, choreografie, entscheidungsbaum, set_a_b, evk, eskalationsleiter, canvas, wcf, plateau):
    fn()

blockkarte("b3-landkarte", "Block 3 · Lernpsychologie und Gedächtnis", "Warum funktioniert, was in Block 1 und 2 funktioniert hat?",
           [("3.1", "Gedächtnis", "eng, vergesslich,\nauf Vorwissen gebaut"), ("3.2", "Belastung", "schwere Sache,\nschlanker Weg"), ("3.3", "Aufmerk-\nsamkeit", "wer nicht lenkt,\nüberlässt es dem Zufall"),
            ("3.4", "Abruf", "erinnern müssen\nist Lernen"), ("3.5", "Verteilen\nund Mischen", "Leistung heute ist\nnicht Lernen"), ("3.6", "Vernetzen", "Kernwissen auf\neiner Seite")],
           ["Routinen (Block 1)\nschaffen Platz zum Denken", "kleine Schritte, Treppe\n(M2.3, M2.4)", "Do Now und Exit Ticket\n(M2.6)", "Idealantwort und\nMindestziel (M2.2)"], PETROL)
blockkarte("b4-landkarte", "Block 4 · Verstehen prüfen und alle beteiligen", "Woher weiß ich in der Stunde, was in 28 Köpfen passiert?",
           [("4.1", "Fehlerkultur", "Fehler sicher machen,\nSelbstauskunft ersetzen"), ("4.2", "Aufrufen ohne\nMeldung", "Frage, Pause, Name"), ("4.3", "Anspruch\nhalten", "zurückkommen,\nnicht aufrunden"),
            ("4.4", "Schreiben und\nSprechen", "alle denken,\nnicht nur einer"), ("4.5", "Sichtbar\nmachen", "sehen und\nentscheiden"), ("4.6", "Entscheiden", "Muster, Format,\nneuer Zugang")],
           ["Klassenführung und warmer Ton\n(Block 1)", "Mini-Whiteboards, Treppe\n(M2.4)", "Exit Ticket sortieren\n(M2.6)", "Abruf ohne Note\n(M3.4)"], BLAU)
blockkarte("b5-landkarte", "Block 5 · Motivation und Beziehung", "Warum strengen sich Menschen an – und was tue ich, wenn nichts mehr greift?",
           [("5.1", "Erfolg", "Erwartung × Wert\n÷ Kosten"), ("5.2", "Routinen\nund Normen", "Kosten senken, die\nMehrheit zeigen"), ("5.3", "Zugehörig-\nkeit", "niemand bleibt\nunsichtbar"),
            ("5.4", "Zustimmung,\nErnstfälle", "Grenze setzen,\nHilfe holen"), ("5.5", "Eltern", "gleiche Seite\ndes Tisches")],
           ["Playbook aus Block 1", "Erfolgsquote, Treppe\n(Block 2)", "Fehlerkultur, Arbeiten zeigen\n(Block 4)", "W.I.N.-Gespräch\n(M1.7)"], AMBER)
blockkarte("b6-landkarte", "Block 6 · Planung, Arbeitsökonomie, eigene Entwicklung", "Wie halte ich das alles mit vertretbarem Aufwand durch?",
           [("6.1", "Schlank\nplanen", "Ziel zuerst,\n20 Minuten"), ("6.2", "Einheiten", "Klassenarbeit zuerst,\nPuffer einplanen"), ("6.3", "Korrigieren", "Rückmeldung, die\nÜberarbeitung auslöst"),
            ("6.4", "Weiter\nwachsen", "gezielt üben,\nTermine setzen"), ("6.5", "Kolloquium", "vorher und nachher")],
           ["Planungsbogen (M2.6)", "Wiederholungs-Landkarte\n(M3.5)", "Daten aus Block 4", "Routinen senken Kosten\n(M5.2)"], GRUEN)
