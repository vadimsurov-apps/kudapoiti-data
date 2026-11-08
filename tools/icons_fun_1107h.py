"""Иконки робота fun (2026-11-08, ночь): 16 мест. Каждая придумана и нарисована отдельно (правило абсолютной
уникальности). Сверено со всеми листами icons-catalog и icons-src/subjects.txt (заняты: парик, начос, кинопроектор,
VR-очки, кинокресло, карты-машинки, книжные стопки, дирижабль, жемчужина — не брать).
Запуск: python3 tools/icons_fun_1107h.py [id ...]  (печатает строки для subjects.txt)"""
import os, sys, math
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
GO = "#F2B632"


def svg(a, b, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


def closed_eye(x, y, k=1.0):
    return f'<path d="M{x-4*k} {y} Q{x} {y-5*k} {x+4*k} {y}" fill="none" {W(2.6*k)}/>'


I = {}


def rr(x, y, w, h, r, fill, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" {s()} {extra}/>'





# 1. Светловка (дети) — ящик библиотечного каталога
I["svetlovka-kids-tishinsky"] = ("#F7EAD8", "#B9875A",
    "деревянный ящик библиотечного каталога с карточками", "выдвинулся из шкафа-картотеки, одна карточка торчит как язычок",
    rr(-6, 92, 140, 40, 4, "#8A5A30")
    + "".join(rr(x, 98, 26, 16, 3, "#A8703E") + f'<circle cx="{x+13}" cy="106" r="2" fill="{GO}"/>' for x in (-2, 104))
    + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="2" fill="#FFFDF6" {W(2)} transform="rotate({r} {x+w/2} {y+20})"/>'
              + f'<path d="M{x+6} {y+8} h{w-12} M{x+6} {y+14} h{w-18}" stroke="#9AB" stroke-width="2" transform="rotate({r} {x+w/2} {y+20})"/>'
              for x, y, w, r in [(30, 26, 60, -6), (34, 22, 60, 4), (36, 30, 56, 0)])
    + f'<path d="M24 52 H104 L100 102 H28Z" fill="#C98B4E" {s()}/>'
    + f'<path d="M24 52 H104" stroke="{O}" stroke-width="3"/>'
    + rr(50, 84, 28, 10, 5, GO) + rr(54, 60, 20, 10, 2, "#FFFDF6")
    + f'<path d="M58 65 h12" stroke="#9AB" stroke-width="2"/>'
    + f(64, 74, d=13, k=0.72, mouth=False)
    + f'<path d="M58 79 Q64 83 70 79" fill="none" {W(2.2)}/>'
    + f'<path d="M60 81 Q58 100 66 104 Q74 100 68 81" fill="#FFFDF6" {W(1.8)}/>'
    + sp((108, 26, 4), (18, 40, 3)))

# 2. Детская библиотека №40 (Хуторская) — книжка-сказка шагает у плетня
I["lib40-khutorskaya"] = ("#FFF2C8", "#E9A23B",
    "толстая книжка-сказка в красной обложке с ленточкой-закладкой", "шагает по деревенской тропинке мимо плетня хутора",
    "".join(f'<path d="M{x} 96 V54" stroke="#7A5230" stroke-width="4"/>' for x in range(4, 128, 18))
    + "".join(f'<path d="M0 {y} Q9 {y-5} 18 {y} T36 {y} T54 {y} T72 {y} T90 {y} T108 {y} T126 {y}" fill="none" stroke="#B5844E" stroke-width="5"/>'
              for y in (62, 72, 82, 90))
    + f'<path d="M0 98 H128 V128 H0Z" fill="#8CC35A" {s()}/>'
    + f'<path d="M40 128 Q56 104 64 98 Q72 104 88 128Z" fill="#E8D19A"/>'
    + f'<path d="M50 96 l-6 16 M78 96 l6 16" stroke="{O}" stroke-width="3.6"/>'
    + f'<path d="M38 112 h10 M80 112 h10" stroke="{O}" stroke-width="4.4" stroke-linecap="round"/>'
    + rr(36, 20, 56, 78, 6, "#E5473A") + rr(86, 22, 10, 74, 4, "#FFF6E0")
    + f'<path d="M88 30 h6 M88 40 h6 M88 50 h6 M88 60 h6 M88 70 h6 M88 80 h6" stroke="#C9B48A" stroke-width="1.6"/>'
    + f'<rect x="42" y="26" width="44" height="66" rx="4" fill="none" stroke="{GO}" stroke-width="2.4"/>'
    + f'<path d="M64 30 l4 8 l8 1 l-6 5 l2 8 l-8 -4 l-8 4 l2 -8 l-6 -5 l8 -1Z" fill="{GO}" {W(1.6)}/>'
    + f(64, 66, d=10, k=0.75)
    + f'<path d="M78 98 V112 l4 -4 l4 4 V96" fill="#3A7BD5" {W(1.8)}/>'
    + f'<path d="M36 60 Q24 66 28 78 M92 60 Q104 52 100 42" fill="none" stroke="{O}" stroke-width="3.4"/>'
    + sp((112, 22, 4), (20, 24, 3)))

# 3. ЦДБ №152 — стремянка на колёсиках у стеллажа
I["lib152-voronezhskaya"] = ("#E4E0FF", "#7A6BD8",
    "библиотечная лестница-стремянка на колёсиках", "подкатилась к высокому книжному стеллажу с разноцветными корешками",
    rr(62, -4, 80, 120, 2, "#9C6B3E")
    + "".join(f'<path d="M62 {y} H130" stroke="{O}" stroke-width="3"/>' for y in (30, 64, 98))
    + "".join(rr(x, y, 7, h, 1.5, c) for x, y, h, c in [
        (68, 8, 22, "#FF6B6B"), (76, 12, 18, "#4FC3F7"), (84, 6, 24, GO), (92, 10, 20, "#7BD389"), (100, 8, 22, "#B388FF"),
        (108, 12, 18, "#FF9F43"), (68, 42, 22, "#4FC3F7"), (76, 44, 20, "#FF6B6B"), (84, 40, 24, "#7BD389"), (92, 46, 18, GO),
        (100, 42, 22, "#FF9F43"), (108, 44, 20, "#4FC3F7"), (68, 76, 22, "#B388FF"), (76, 78, 20, GO), (84, 74, 24, "#FF6B6B"),
        (92, 80, 18, "#4FC3F7"), (100, 76, 22, "#7BD389")])
    + f'<path d="M0 112 H128 V128 H0Z" fill="#C7B8F0" {s()}/>'
    + f'<path d="M22 108 L46 18 M58 108 L72 22" stroke="#E2A64E" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M22 108 L46 18 M58 108 L72 22" stroke="{O}" stroke-width="2" fill="none"/>'
    + "".join(f'<path d="M{24+ (108-y)*0.27:.1f} {y} L{58+(108-y)*0.16:.1f} {y}" stroke="#C47F2E" stroke-width="6" stroke-linecap="round"/>'
              for y in (90, 72, 54))
    + rr(36, 20, 40, 18, 5, "#F2C26E")
    + f(56, 28, d=9, k=0.6)
    + "".join(f'<circle cx="{x}" cy="112" r="5.5" fill="#555" {W(2)}/><circle cx="{x}" cy="112" r="2" fill="#ccc"/>' for x in (22, 58))
    + sp((18, 30, 4), (30, 60, 2.6)))

# 4. ЦДБ Долгопрудный — закладка-помпон в книге на подоконнике
I["dolgoprudny-kids-library"] = ("#FFE9F0", "#F28AA8",
    "закладка-кисточка с пушистым помпоном", "выглядывает из раскрытой книги, лежащей на подоконнике",
    rr(10, -6, 108, 92, 4, "#BFE6FF") + f'<path d="M64 -6 V86 M10 40 H118" stroke="#fff" stroke-width="6"/>'
    + f'<path d="M64 -6 V86 M10 40 H118" stroke="{O}" stroke-width="1.6"/>'
    + f'<ellipse cx="96" cy="22" rx="12" ry="6" fill="#fff" opacity=".9"/>'
    + f'<path d="M-4 86 H132 V128 H-4Z" fill="#FFFDF6" {s()}/>'
    + f'<path d="M14 104 Q40 94 64 104 Q88 94 114 104 L112 118 Q88 108 64 118 Q40 108 16 118Z" fill="#fff" {s()}/>'
    + f'<path d="M64 104 V118" stroke="{O}" stroke-width="2"/>'
    + f'<path d="M22 106 Q40 100 56 106 M72 106 Q88 100 106 106" fill="none" stroke="#C8C8D8" stroke-width="2"/>'
    + f'<path d="M64 104 Q60 80 64 64" fill="none" stroke="#7A3FB0" stroke-width="4"/>'
    + "".join(f'<circle cx="{64+22*math.cos(a)}" cy="{40+22*math.sin(a)}" r="9" fill="#C77DFF" {W(2)}/>'
              for a in [i*math.pi/6 for i in range(12)])
    + f'<circle cx="64" cy="40" r="22" fill="#C77DFF"/>'
    + f(64, 40, d=9, k=0.72)
    + sp((20, 70, 3), (108, 64, 3.4)))

# 5. Baza VR — шагающий мех на неоновой арене
I["baza-vr-shchelkovskoe"] = ("#16324A", "#081320",
    "шагающий робот-мех с кабиной-визором", "стоит на неоновой платформе виртуальной арены среди голограмм-треугольников",
    f'<ellipse cx="64" cy="110" rx="46" ry="10" fill="none" stroke="#3FF2E0" stroke-width="3"/>'
    + f'<ellipse cx="64" cy="110" rx="30" ry="6" fill="#3FF2E0" opacity=".3"/>'
    + "".join(f'<path d="M{x} {y} l7 12 h-14Z" fill="none" stroke="#FF5FD2" stroke-width="2"/>' for x, y in [(18, 36), (106, 28), (100, 70)])
    + f'<path d="M44 76 L34 92 L40 108 M84 76 L94 92 L88 108" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M44 76 L34 92 L40 108 M84 76 L94 92 L88 108" fill="none" stroke="#9FB3C8" stroke-width="5" stroke-linecap="round"/>'
    + rr(30, 104, 18, 8, 3, "#5C6E82") + rr(80, 104, 18, 8, 3, "#5C6E82")
    + f'<path d="M28 50 Q28 26 64 26 Q100 26 100 50 V68 Q100 82 64 82 Q28 82 28 68Z" fill="#E8EEF5" {s()}/>'
    + rr(36, 40, 56, 24, 12, "#1B1F3A") + rr(38, 42, 52, 20, 10, "#3FF2E0", 'opacity=".25"')
    + eye(54, 52, 0.75) + eye(74, 52, 0.75)
    + f'<path d="M58 58 Q64 62 70 58" fill="none" stroke="#3FF2E0" stroke-width="2.2"/>'
    + f'<path d="M64 26 V16" stroke="{O}" stroke-width="3"/><circle cx="64" cy="14" r="4" fill="#FF5FD2" {W(2)}/>'
    + f'<path d="M28 56 h-10 v12 M100 56 h10 v12" fill="none" stroke="{O}" stroke-width="5"/>'
    + "".join(sparkle(x, y, r, "#3FF2E0") for x, y, r in [(20, 80, 3), (112, 50, 3)]))

# 6. Le Mans (Магистральная) — стартовые огни над картом
I["karting-lemans-magistralnaya"] = ("#EEEEF4", "#8A8FA8",
    "перекладина стартовых огней с пятью лампами", "зажгла зелёный над синим картом на клетчатой стартовой линии крытого картодрома",
    f'<path d="M0 92 H128 V128 H0Z" fill="#4A4E5C"/>'
    + "".join(f'<rect x="{x}" y="{96+((x//8)%2)*6}" width="8" height="6" fill="#fff"/>' for x in range(0, 128, 8))
    + "".join(f'<rect x="{x}" y="{102-((x//8)%2)*6}" width="8" height="6" fill="#fff"/>' for x in range(0, 128, 8))
    + f'<path d="M14 92 V20 M114 92 V20" stroke="{O}" stroke-width="6"/><path d="M14 92 V20 M114 92 V20" stroke="#C9CCD8" stroke-width="3"/>'
    + rr(6, 14, 116, 34, 10, "#2B2E3A")
    + "".join(f'<circle cx="{x}" cy="31" r="8" fill="#5CE16A" {W(2)}/>' for x in (24, 44, 84, 104))
    + f'<circle cx="64" cy="31" r="10" fill="#5CE16A" {W(2)}/>' + f(64, 30, d=4, k=0.5)
    + "".join(f'<path d="M{x} 46 v6" stroke="#5CE16A" stroke-width="2.4"/>' for x in (24, 44, 64, 84, 104))
    + f'<path d="M22 108 L30 78 H94 L108 108Z" fill="#2E6FD8" {s()}/>'
    + rr(50, 62, 26, 20, 6, "#FFD23C") + f'<path d="M60 64 h8" stroke="{O}" stroke-width="2"/>'
    + "".join(f'<circle cx="{x}" cy="108" r="10" fill="#222" {W(2)}/><circle cx="{x}" cy="108" r="3.4" fill="#888"/>' for x in (32, 98))
    + f'<path d="M56 72 Q64 64 72 72" fill="none" stroke="{O}" stroke-width="3.4"/>'
    + sp((112, 62, 3)))

# 7. Театр иллюзии (Перовская) — распиленный ящик фокусника
I["illusion-theatre-perovskaya"] = ("#F6D6FF", "#8E3FB0",
    "ящик фокусника, распиленный на три части", "из одного конца торчит улыбающаяся голова, из другого — ноги в башмаках, на сцене под красным занавесом",
    f'<path d="M-4 -4 H30 Q24 50 30 128 H-4Z M132 -4 H98 Q104 50 98 128 H132Z" fill="#D8263A" {s()}/>'
    + f'<path d="M8 0 Q6 60 10 128 M120 0 Q122 60 118 128" stroke="#A81A2C" stroke-width="3"/>'
    + f'<path d="M0 104 H128 V128 H0Z" fill="#7A4A2A" {s()}/>'
    + f'<path d="M44 84 V104 M84 84 V104" stroke="{O}" stroke-width="4"/>'
    + rr(32, 58, 20, 26, 3, "#2E6FD8") + rr(56, 58, 18, 26, 3, "#FFD23C") + rr(78, 58, 20, 26, 3, "#2E6FD8")
    + "".join(f'<circle cx="{x}" cy="71" r="3" fill="#fff"/>' for x in (42, 65, 88))
    + f'<path d="M66 20 L60 64" stroke="#C9CCD8" stroke-width="6"/><path d="M66 20 L60 64" stroke="{O}" stroke-width="1.4"/>'
    + rr(60, 10, 14, 12, 3, "#C98B4E")
    + f'<circle cx="20" cy="70" r="13" fill="#FFD8B8" {s()}/>' + eye(16, 68, 0.55) + eye(24, 68, 0.55)
    + f'<path d="M16 74 Q20 78 24 74" fill="none" {W(1.8)}/>'
    + f'<path d="M10 62 Q20 50 30 62" fill="#6B3A1E" {W(1.8)}/>'
    + f'<path d="M98 64 L108 58 L114 62 L104 70Z M98 76 L110 74 L114 80 L100 82Z" fill="#3A2A1A" {W(1.6)}/>'
    + sp((50, 34, 4), (84, 40, 3)))

# 8. Дом-музей Бокова — колодец-журавль
I["bokov-house-museum"] = ("#E6F2D0", "#93B04A",
    "деревенский колодец-журавль", "зачерпнул ведро у избы, на срубе лежит раскрытая книжечка стихов",
    f'<path d="M0 100 H128 V128 H0Z" fill="#6FA03A" {s()}/>'
    + f'<path d="M96 60 L114 44 L132 60 V100 H96Z" fill="#B57A44" {s()}/>' + rr(104, 70, 12, 12, 1, "#BFE6FF")
    + f'<path d="M84 104 L80 22" stroke="{O}" stroke-width="7"/><path d="M84 104 L80 22" stroke="#9C6B3E" stroke-width="4"/>'
    + f'<path d="M14 6 L112 50" stroke="{O}" stroke-width="7"/><path d="M14 6 L112 50" stroke="#C98B4E" stroke-width="4"/>'
    + f'<path d="M30 13 V60" stroke="{O}" stroke-width="2"/>'
    + f'<path d="M24 58 H36 L34 70 H26Z" fill="#8A8F98" {W(2)}/>'
    + "".join(rr(18, y, 64, 10, 5, "#C98B4E") for y in (72, 82, 92))
    + rr(22, 64, 56, 10, 5, "#B57A44")
    + f(50, 88, d=11, k=0.7, mouth=False) + f'<path d="M45 94 Q50 98 55 94" fill="none" {W(2)}/>'
    + f'<path d="M40 64 Q50 58 60 64 Q50 66 40 64Z M60 64 Q70 58 76 62 L74 66 Q66 64 60 64Z" fill="#fff" {W(1.6)}/>'
    + sp((112, 20, 4), (60, 30, 3)))

# 9. Музей землеведения МГУ — Земля в разрезе
I["zemlevedenie-msu"] = ("#E0F7F4", "#3FA59A",
    "планета Земля с вырезанной долькой, где видны слои до горячего ядра", "стоит на подставке рядом со шпилем высотки МГУ",
    f'<path d="M100 128 V58 L106 50 V30 L108 16 L110 30 V50 L116 58 V128Z" fill="#E9E1D0" {W(2)}/>'
    + f'<circle cx="108" cy="12" r="3" fill="{GO}" {W(1.4)}/>'
    + f'<path d="M40 104 L56 92 H72 L88 104Z" fill="#8A5A30" {s()}/>' + rr(36, 102, 56, 8, 3, "#6E4A2A")
    + f'<circle cx="64" cy="58" r="36" fill="#4FA7E8" {s()}/>'
    + f'<path d="M36 46 Q46 34 56 40 Q60 52 48 54 Q40 60 36 46Z M70 80 Q80 72 90 78 Q86 90 74 90Z M76 26 Q88 28 92 38 L80 36Z" fill="#6CC46A" {W(1.6)}/>'
    + f'<path d="M64 58 L64 22 A36 36 0 0 1 100 58Z" fill="#8A5A30" {s()}/>'
    + f'<path d="M64 58 L64 30 A28 28 0 0 1 92 58Z" fill="#FF8A3D"/>'
    + f'<path d="M64 58 L64 40 A18 18 0 0 1 82 58Z" fill="#FFC23C"/>'
    + f'<path d="M64 58 L64 48 A10 10 0 0 1 74 58Z" fill="#FF4A3A"/>'
    + f'<path d="M64 58 V22 M64 58 H100" stroke="{O}" stroke-width="2.4"/>'
    + f(48, 68, d=8, k=0.62)
    + sp((20, 24, 4), (24, 96, 3)))

# 10. «Журавлиная родина» — клюква на кочке
I["zhuravlinaya-rodina-bog-museum"] = ("#FFE8EE", "#C9667E",
    "ягодка клюквы с листиками", "сидит на моховой кочке посреди болота, над ней пролетает журавль",
    f'<path d="M0 96 Q30 90 64 96 T128 94 V128 H0Z" fill="#5C7F7A" {s()}/>'
    + f'<path d="M0 108 Q64 100 128 108" stroke="#A9D6E0" stroke-width="3" fill="none"/>'
    + f'<path d="M18 104 Q20 68 64 66 Q108 68 110 104Z" fill="#7DB04A" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#A7D46A"/>' for x, y in [(30, 92), (42, 80), (86, 82), (98, 94), (60, 74), (74, 92)])
    + f'<path d="M64 36 Q62 26 70 22" fill="none" stroke="#5A3A22" stroke-width="3"/>'
    + f'<path d="M66 26 Q78 16 86 24 Q76 30 66 26Z M64 30 Q52 22 46 30 Q56 34 64 30Z" fill="#4FA24A" {W(1.8)}/>'
    + f'<circle cx="64" cy="58" r="24" fill="#D8263A" {s()}/>'
    + f'<ellipse cx="56" cy="48" rx="7" ry="4" fill="#fff" opacity=".45"/>'
    + f(64, 60, d=8, k=0.66)
    + f'<path d="M86 14 Q96 10 104 16 L118 10 L108 20 Q112 22 120 22 Q106 26 98 20 Q92 24 80 24 Q90 20 86 14Z" fill="#7A7F8A" {W(1.6)}/>'
    + f'<path d="M92 14 l4 -4" stroke="#D8263A" stroke-width="2.4"/>'
    + sp((20, 30, 3.4)))

# 11. Дворцовое село Ильинское — коромысло с вёдрами
I["ilyinskoe-village-museum"] = ("#E2F3FF", "#2F7FC0",
    "расписное коромысло с двумя вёдрами воды", "шагает по деревянным мосткам у реки возле села",
    f'<path d="M0 92 Q32 86 64 92 T128 90 V128 H0Z" fill="#3E8FD0"/>'
    + f'<path d="M10 104 h20 M60 112 h24 M96 102 h18" stroke="#BFE6FF" stroke-width="3" stroke-linecap="round"/>'
    + rr(-4, 82, 136, 10, 2, "#B57A44")
    + "".join(f'<path d="M{x} 92 V112" stroke="{O}" stroke-width="4"/>' for x in (20, 64, 108))
    + f'<path d="M24 52 Q64 14 104 52" fill="none" stroke="{O}" stroke-width="16" stroke-linecap="round"/>'
    + f'<path d="M24 52 Q64 14 104 52" fill="none" stroke="#E5473A" stroke-width="11" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="{GO}"/>' for x, y in [(36, 40), (48, 32), (80, 32), (92, 40)])
    + f'<path d="M24 52 V62 M104 52 V62" stroke="{O}" stroke-width="2.4"/>'
    + f'<path d="M10 62 H38 L34 88 H14Z" fill="#9AA6B4" {s()}/><path d="M90 62 H118 L114 88 H94Z" fill="#9AA6B4" {s()}/>'
    + f'<ellipse cx="24" cy="63" rx="13" ry="3.4" fill="#7CC8F0"/><ellipse cx="104" cy="63" rx="13" ry="3.4" fill="#7CC8F0"/>'
    + f(64, 36, d=8, k=0.62)
    + sp((60, 64, 3), (100, 12, 3.4)))

# 12. Усадьба Кузьминки — кованые ворота
I["kuzminki-estate-museum"] = ("#E9F7E1", "#4E9A5C",
    "кованые усадебные ворота с завитками", "распахнуты в липовую аллею к пруду",
    f'<ellipse cx="64" cy="70" rx="30" ry="6" fill="#7CC8F0" {W(1.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#3E8E3E" {W(1.6)}/>' for x, y, r in [(40, 54, 10), (88, 54, 10), (50, 46, 7), (78, 46, 7)])
    + f'<path d="M54 128 L60 74 H68 L74 128Z" fill="#E8D19A"/>'
    + rr(4, 40, 20, 88, 2, "#F2EDE2") + rr(104, 40, 20, 88, 2, "#F2EDE2")
    + f'<path d="M6 40 Q14 24 22 40Z M106 40 Q114 24 122 40Z" fill="#F2EDE2" {W(2)}/>'
    + f'<circle cx="14" cy="22" r="5" fill="#F2EDE2" {W(2)}/><circle cx="114" cy="22" r="5" fill="#F2EDE2" {W(2)}/>'
    + f'<path d="M24 46 L52 52 V112 L24 118Z M104 46 L76 52 V112 L104 118Z" fill="none" stroke="#2B2E3A" stroke-width="3.4"/>'
    + "".join(f'<path d="M{x} {48+(x-24)*0.21 if x<64 else 48+(104-x)*0.21:.0f} V{116-(x-24)*0.21 if x<64 else 116-(104-x)*0.21:.0f}" stroke="#2B2E3A" stroke-width="2.4"/>'
              for x in (31, 38, 45, 83, 90, 97))
    + "".join(f'<path d="M{cx-6} {cy} q6 -10 12 0 q-6 6 -6 0" fill="none" stroke="{GO}" stroke-width="2.4"/>' for cx, cy in [(38, 70), (90, 70)])
    + f'<path d="M24 46 Q38 30 52 52 M104 46 Q90 30 76 52" fill="none" stroke="#2B2E3A" stroke-width="3"/>'
    + f(38, 92, d=6, k=0.5) + f(90, 92, d=6, k=0.5)
    + sp((64, 20, 4)))

# 13. Усадьба Щапово — деревянный фотоаппарат-гармошка
I["shchapovo-museum"] = ("#F4E1D2", "#A86E52",
    "деревянный фотоаппарат-гармошка на треноге", "фотографирует усадебный дом с белыми колоннами",
    f'<path d="M0 98 H128 V128 H0Z" fill="#7DB04A" {s()}/>'
    + f'<path d="M88 66 H128 V98 H88Z" fill="#FFF3D6" {s()}/><path d="M84 66 L108 52 L132 66Z" fill="#B85C3C" {s()}/>'
    + "".join(f'<path d="M{x} 70 V98" stroke="#C9B48A" stroke-width="3"/>' for x in (96, 106, 116))
    + f'<path d="M40 74 L22 122 M52 74 V124 M64 74 L82 122" stroke="{O}" stroke-width="5"/>'
    + f'<path d="M40 74 L22 122 M52 74 V124 M64 74 L82 122" stroke="#C98B4E" stroke-width="2.4"/>'
    + rr(18, 30, 30, 44, 4, "#9C6B3E")
    + f'<path d="M48 36 L70 40 V64 L48 68Z" fill="#2B2E3A" {s()}/>'
    + "".join(f'<path d="M{x} {37+(x-48)*0.18:.0f} V{67-(x-48)*0.18:.0f}" stroke="#555" stroke-width="1.6"/>' for x in (54, 60, 66))
    + rr(70, 40, 10, 24, 2, "#C98B4E")
    + f'<circle cx="84" cy="52" r="8" fill="#5A6170" {s()}/><circle cx="84" cy="52" r="4" fill="#9FD3FF"/>'
    + f'<path d="M18 30 Q8 50 16 74 L20 74 Z" fill="#2B2E3A" {W(1.6)}/>'
    + f(33, 52, d=7, k=0.58)
    + f'<path d="M92 40 l8 -6 M94 50 h10 M92 60 l8 6" stroke="#FFD23C" stroke-width="2.6" stroke-linecap="round"/>'
    + sp((108, 20, 4), (24, 14, 3)))

# 14. Музей истории Лефортово — треуголка-кораблик на Яузе
I["lefortovo-history-museum"] = ("#D6F0F7", "#3A8DB0",
    "чёрная треуголка петровских времён с золотой кокардой", "плывёт корабликом по Яузе под горбатым мостиком",
    f'<path d="M-4 40 Q64 -6 132 40 V52 Q64 12 -4 52Z" fill="#C9B48A" {s()}/>'
    + "".join(f'<path d="M{x} {28 - abs(x-64)*0.3:.0f} V{44 - abs(x-64)*0.12:.0f}" stroke="#9C8A62" stroke-width="2"/>' for x in range(14, 120, 14))
    + f'<path d="M0 80 Q32 74 64 80 T128 78 V128 H0Z" fill="#2F7FC0"/>'
    + f'<path d="M12 98 h18 M90 104 h22 M50 114 h20" stroke="#BFE6FF" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M14 72 Q30 92 64 92 Q98 92 114 72 Q100 60 64 64 Q28 60 14 72Z" fill="#26252E" {s()}/>'
    + f'<path d="M24 74 Q64 54 104 74" fill="none" stroke="{GO}" stroke-width="3"/>'
    + f'<path d="M40 64 Q64 34 88 64Z" fill="#26252E" {s()}/>'
    + f'<circle cx="64" cy="56" r="6" fill="{GO}" {W(2)}/><circle cx="64" cy="56" r="2.4" fill="#fff"/>'
    + "".join(eye(x, 78, 0.7) for x in (54, 74))
    + f'<path d="M60 84 Q64 87 68 84" fill="none" stroke="#fff" stroke-width="2"/>'
    + f'<ellipse cx="46" cy="84" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="82" cy="84" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>'
    + sp((106, 60, 3.4), (20, 60, 3)))

# 15. Музей платка и шали — платок с розами кружится
I["pavposad-shawl-museum"] = ("#3B2440", "#1B0F22",
    "павловопосадский платок с красными розами и бахромой", "кружится в вихре танца, раскинув кисти",
    f'<path d="M14 104 Q64 126 114 104" fill="none" stroke="#FFD23C" stroke-width="2.4" stroke-dasharray="4 5"/>'
    + f'<path d="M10 30 Q30 12 52 10" fill="none" stroke="#FFD23C" stroke-width="2.4" stroke-dasharray="4 5"/>'
    + "".join(f'<path d="M{x} {y} l{dx} {dy}" stroke="#E8C77A" stroke-width="2"/>'
              for i in range(9) for x, y, dx, dy in [(64 - 46 + i*5.1, 62 - i*5.1 + 2, -3, -3), (64 + i*5.1 + 2, 16 + i*5.1, 3, -3)])
    + f'<path d="M64 14 L114 64 L64 114 L14 64Z" fill="#1E1A2E" {s()}/>'
    + f'<path d="M64 22 L106 64 L64 106 L22 64Z" fill="none" stroke="#E5473A" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#E5473A" {W(1.6)}/><path d="M{x-r*0.5} {y} q{r*0.5} {-r*0.6} {r} 0" fill="none" stroke="#A81A2C" stroke-width="1.6"/>'
              for x, y, r in [(64, 30, 6), (98, 64, 6), (64, 98, 6), (30, 64, 6)])
    + "".join(f'<path d="M{x} {y} q6 -6 10 0 q-6 4 -10 0Z" fill="#4FA24A"/>' for x, y in [(70, 36), (90, 70), (52, 92), (34, 56)])
    + f'<circle cx="64" cy="64" r="20" fill="#FF5A6E" {s()}/>'
    + f(64, 64, d=8, k=0.62)
    + sp((112, 22, 4), (18, 108, 3)))

# 16. «Синема Стар» Румянцево — кинолента-серпантин со звёздочкой
I["cinemastar-rumyantsevo"] = ("#2B2B3A", "#101018",
    "кинолента с дырочками-перфорацией", "вьётся петлёй-серпантином и выпускает из кадра золотую звёздочку",
    f'<path d="M14 116 Q10 70 46 72 Q86 74 84 44 Q82 20 104 14" fill="none" stroke="{O}" stroke-width="30" stroke-linecap="round"/>'
    + f'<path d="M14 116 Q10 70 46 72 Q86 74 84 44 Q82 20 104 14" fill="none" stroke="#3A3D4A" stroke-width="26" stroke-linecap="round"/>'
    + f'<path d="M14 116 Q10 70 46 72 Q86 74 84 44 Q82 20 104 14" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 6" transform="translate(-8 -6)"/>'
    + f'<path d="M14 116 Q10 70 46 72 Q86 74 84 44 Q82 20 104 14" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 6" transform="translate(8 6)"/>'
    + rr(28, 58, 32, 28, 3, "#9FD3FF")
    + f(44, 70, d=7, k=0.55)
    + f'<path d="M104 22 l5 10 l11 1 l-8 7 l3 11 l-11 -6 l-10 6 l3 -11 l-8 -7 l11 -1Z" fill="{GO}" {W(2)}/>'
    + "".join(sparkle(x, y, r, "#FFE79A") for x, y, r in [(98, 64, 3), (116, 80, 2.6), (24, 26, 3)]))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
