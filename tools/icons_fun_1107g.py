"""Иконки робота fun (2026-11-07, ночь): 11 мест. Каждая придумана и нарисована отдельно (правило абсолютной
уникальности). Сверено с листами icons-catalog и icons-src/subjects.txt (заняты: ткацкий челнок, лапоть, утюг,
огурчик, терем, дикобраз, носуха, топорик, ситцевый платок — не брать).
Запуск: python3 tools/icons_fun_1107g.py [id ...]  (печатает строки для subjects.txt)"""
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



# 1. Cook&Run — скалка в бандане бежит к финишу
I["cooknrun-strogino"] = ("#FFE3D2", "#E5533D",
    "деревянная скалка в синей бандане", "мчится на ножках по клетчатой кухонной скатерти к финишной ленточке",
    f'<path d="M0 98 H128 V128 H0Z" fill="#fff"/>'
    + "".join(f'<rect x="{x}" y="{98+((x//12)%2)*10}" width="12" height="10" fill="#E5533D" opacity=".85"/>' for x in range(0, 128, 12))
    + "".join(f'<rect x="{x}" y="{108-((x//12)%2)*10}" width="12" height="10" fill="#E5533D" opacity=".85"/>' for x in range(0, 128, 12))
    + f'<path d="M0 98 H128" stroke="{O}" stroke-width="2.4"/>'
    + f'<path d="M108 30 V100" stroke="{O}" stroke-width="3"/><path d="M108 32 L122 38 L108 44Z" fill="#FFD23C" {W(2)}/>'
    + f'<path d="M108 66 Q100 70 92 64" fill="none" stroke="#FF5FA0" stroke-width="3"/>'
    + f'<path d="M40 86 l-8 12 M58 86 l6 12" stroke="{O}" stroke-width="3.4"/>'
    + f'<path d="M28 98 h8 M62 98 h8" stroke="{O}" stroke-width="4"/>'
    + f'<g transform="rotate(-14 50 64)">'
    + rr(6, 58, 14, 12, 5, "#C98B4E") + rr(80, 58, 14, 12, 5, "#C98B4E")
    + rr(18, 46, 64, 36, 16, "#F2C88E")
    + f'<path d="M18 56 Q50 34 82 56 L82 50 Q50 28 18 50Z" fill="#2E6FD8" {W(2.2)}/>'
    + f'<path d="M80 52 l12 -8 l-2 12Z" fill="#2E6FD8" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#fff"/>' for x, y in [(30, 48), (44, 42), (58, 42), (72, 48)])
    + f(50, 64, d=10, k=0.7) + '</g>'
    + "".join(f'<path d="M{x} {y} h-14" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(8, 50), (12, 62), (6, 74)])
    + sp((96, 18, 4), (24, 20, 3)))

# 2. Яндекс Музей — компьютерная мышка на постаменте
I["yandex-museum-avrora"] = ("#3A3550", "#14121E",
    "белая компьютерная мышка с колёсиком", "стоит на музейном постаменте в луче прожектора, провод свернулся хвостиком",
    f'<path d="M64 0 L30 100 H98Z" fill="#FFF6C8" opacity=".22"/>'
    + rr(34, 92, 60, 14, 2, "#E6E1F0") + rr(28, 104, 72, 14, 2, "#CFC8DE")
    + f'<path d="M64 40 Q66 20 82 22 Q100 24 96 12" fill="none" stroke="{O}" stroke-width="5"/>'
    + f'<path d="M64 40 Q66 20 82 22 Q100 24 96 12" fill="none" stroke="#F2F2F6" stroke-width="2.4"/>'
    + f'<path d="M40 64 Q40 38 64 38 Q88 38 88 64 V74 Q88 92 64 92 Q40 92 40 74Z" fill="#F7F7FA" {s()}/>'
    + f'<path d="M40 60 H88 M64 38 V60" stroke="{O}" stroke-width="2.4"/>'
    + rr(60, 44, 8, 12, 4, "#FF4A3A")
    + f(64, 72, d=9, k=0.62)
    + "".join(sparkle(x, y, r, "#FFE79A") for x, y, r in [(18, 30, 4), (110, 46, 3), (102, 84, 2.6)]))

# 3. Талдом (Салтыков-Щедрин) — премудрый пескарь в норке
I["taldom-museum"] = ("#C8EEF2", "#2C8C9C",
    "пугливый серебристый пескарь с большими глазами", "выглядывает из норки под речной корягой на песчаном дне",
    f'<path d="M0 96 Q40 88 70 96 T128 94 V128 H0Z" fill="#E9D29A" {s()}/>'
    + f'<path d="M10 76 Q20 50 52 46 Q90 42 118 58 L122 70 Q96 62 74 68 Q78 96 52 100 Q20 102 10 76Z" fill="#6B4A2E" {s()}/>'
    + f'<path d="M118 58 l8 -10 M100 52 l4 -12" stroke="{O}" stroke-width="3.4"/>'
    + f'<ellipse cx="42" cy="78" rx="26" ry="18" fill="#2A1C12" {W(2.2)}/>'
    + '<g transform="translate(42 78) scale(1.45) translate(-42 -78)">'
    + f'<path d="M24 80 Q36 64 60 72 Q64 78 60 84 Q36 92 24 80Z" fill="#B9C6CF" {s()}/>'
    + f'<path d="M60 72 L70 66 L68 78 L70 90 L60 84Z" fill="#9DAAB4" {W(2)}/>'
    + f'<path d="M34 72 Q40 66 46 70" fill="none" stroke="#8B98A2" stroke-width="2"/>'
    + "".join(f'<circle cx="{x}" cy="86" r="1.6" fill="#7C8994"/>' for x in (38, 44, 50))
    + f'<circle cx="32" cy="76" r="6" fill="#fff" {W(1.8)}/>' + eye(32, 76, 0.75)
    + f'<path d="M24 84 q3 2 6 0" fill="none" {W(1.6)}/>' + '</g>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".8" {W(1.4)}/>' for x, y, r in [(20, 56, 3), (14, 44, 4.4), (22, 30, 3)])
    + "".join(f'<path d="M{x} 96 q-4 -12 0 -22 q4 10 0 22" fill="#4FA25A" {W(1.6)}/>' for x in (96, 106)))

# 4. Озёры — медный рукомойник
I["ozery-museum"] = ("#FFF0DA", "#C9875A",
    "медный деревенский рукомойник с носиком", "висит на бревенчатой стене избы и капает водичкой в деревянную кадушку",
    "".join(f'<rect x="0" y="{y}" width="128" height="15" rx="7" fill="#C99A62" {W(1.6)}/>' for y in range(4, 90, 16))
    + f'<path d="M0 92 H128 V128 H0Z" fill="#9C6B3E" {s()}/>'
    + f'<path d="M30 92 L36 122 H92 L98 92Z" fill="#B57A44" {s()}/>'
    + f'<path d="M32 102 H96 M34 114 H94" stroke="#6E4A2A" stroke-width="3"/>'
    + f'<ellipse cx="64" cy="92" rx="34" ry="6" fill="#7CC8F0" {W(2.2)}/>'
    + f'<path d="M64 10 V20" stroke="{O}" stroke-width="3"/><circle cx="64" cy="8" r="3" fill="none" {W(2)}/>'
    + f'<path d="M38 26 Q38 18 64 18 Q90 18 90 26 L86 62 Q64 72 42 62Z" fill="#E09A50" {s()}/>'
    + f'<path d="M40 30 Q64 36 88 30" fill="none" stroke="#B86E30" stroke-width="2.4"/>'
    + f'<path d="M58 66 L58 74 Q64 78 70 74 L70 66" fill="#C47A3A" {W(2.4)}/>'
    + f'<path d="M86 34 Q100 34 98 50" fill="none" stroke="{O}" stroke-width="3"/>'
    + f(64, 46, d=10, k=0.68)
    + "".join(f'<path d="M64 {y} q-3 5 0 7 q3 -2 0 -7Z" fill="#7CC8F0" {W(1.2)}/>' for y in (78, 86))
    + sp((104, 76, 3), (20, 72, 3)))

# 5. Верея — гусарский кивер на валу
I["vereya-museum"] = ("#DDEBFF", "#6F8FC9",
    "чёрный гусарский кивер с белым султаном и кокардой", "стоит на зелёном земляном валу старинного городища у белого собора с золотым куполом",
    f'<rect x="92" y="40" width="22" height="34" fill="#FBF7EE" {W(2)}/><path d="M92 40 Q103 26 114 40Z" fill="#FBF7EE" {W(2)}/>'
    + f'<ellipse cx="103" cy="26" rx="6" ry="7" fill="#F2B632" {W(2)}/><path d="M103 19 V10 M99 13 H107" stroke="{O}" stroke-width="2"/>'
    + f'<path d="M100 74 V62 Q103 58 106 62 V74Z" fill="#6A7B9A"/>'
    + f'<path d="M0 90 Q40 66 80 78 Q108 86 128 76 V128 H0Z" fill="#5DB24E" {s()}/>'
    + f'<path d="M0 108 Q64 96 128 106 V128 H0Z" fill="#3E8E3E"/>'
    + f'<path d="M30 86 L34 34 H78 L82 86Z" fill="#26252E" {s()}/>'
    + f'<path d="M28 84 H84 V92 Q56 98 28 92Z" fill="#26252E" {s()}/>'
    + f'<path d="M34 40 H78" stroke="#F2B632" stroke-width="4"/>'
    + f'<path d="M32 76 Q56 82 80 76" fill="none" stroke="#F2B632" stroke-width="3"/>'
    + f'<circle cx="56" cy="48" r="6" fill="#F2B632" {W(2)}/><circle cx="56" cy="48" r="2.4" fill="#C4302B"/>'
    + f'<path d="M56 34 Q46 22 52 8 Q58 18 62 8 Q68 22 56 34Z" fill="#fff" {W(2.2)}/>'
    + f(56, 62, d=10, k=0.66)
    + sp((18, 22, 4), (120, 92, 3)))

# 6. Пущино — одуванчик над Окой
I["pushchino-eco-museum"] = ("#E8F7FF", "#7BBEE6",
    "пушистый белый одуванчик-шарик", "отпускает пушинки-парашютики лететь над синей рекой и зелёным берегом",
    f'<path d="M0 88 Q64 78 128 88 V102 Q64 94 0 102Z" fill="#3E86D0" {W(2)}/>'
    + f'<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#7CCB5E" {s()}/>'
    + f'<path d="M56 124 Q58 100 60 76" fill="none" stroke="#4F9A3E" stroke-width="4"/>'
    + f'<path d="M58 112 Q44 104 40 92 Q54 96 58 108Z" fill="#6CC45C" {W(2)}/>'
    + "".join(f'<path d="M60 52 L{60+30*math.cos(math.radians(a)):.1f} {52+30*math.sin(math.radians(a)):.1f}" stroke="#D8E2EA" stroke-width="1.6"/>' for a in range(0, 360, 15))
    + "".join(f'<circle cx="{60+30*math.cos(math.radians(a)):.1f}" cy="{52+30*math.sin(math.radians(a)):.1f}" r="3.4" fill="#fff" {W(1.2)}/>' for a in range(0, 360, 15))
    + f'<circle cx="60" cy="52" r="20" fill="#fff" {s()}/>'
    + f(60, 50, d=8, k=0.6)
    + "".join(f'<g transform="rotate({r} {x} {y})"><path d="M{x} {y} v12" stroke="#B8C6D0" stroke-width="1.4"/><path d="M{x-6} {y} Q{x} {y-6} {x+6} {y}" fill="none" stroke="#fff" stroke-width="2.4"/></g>' for x, y, r in [(100, 30, 20), (112, 54, 35), (96, 14, 10), (24, 16, -15)]))

# 7. Лыткарино — оптическая линза
I["lytkarino-museum"] = ("#2E3A6E", "#0E1430",
    "большая прозрачная оптическая линза в латунной оправе", "собирает солнечный луч в яркий зайчик-блик на чёрном фоне",
    f'<circle cx="16" cy="18" r="14" fill="#FFD23C" {W(2)}/>'
    + f'<path d="M24 26 L64 38 L64 90Z" fill="#FFE98A" opacity=".55"/>'
    + f'<path d="M64 40 L112 66 L64 88Z" fill="#FFE98A" opacity=".75"/>'
    + f'<ellipse cx="64" cy="64" rx="18" ry="44" fill="#C9973C" {s()}/>'
    + f'<ellipse cx="64" cy="64" rx="13" ry="38" fill="#CFEFFF" {W(2.2)}/>'
    + f'<path d="M58 34 Q54 50 56 66" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + eye(60, 56, 0.6) + eye(70, 56, 0.6)
    + f'<path d="M61 66 Q65 70 69 66" fill="none" {W(2)}/>'
    + f'<ellipse cx="56" cy="62" rx="3" ry="2" fill="#FF7FA8" opacity=".6"/><ellipse cx="73" cy="62" rx="3" ry="2" fill="#FF7FA8" opacity=".6"/>'
    + sparkle(112, 66, 12, "#FFF3A0") + sparkle(112, 66, 5, "#fff")
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#fff" opacity=".7"/>' for x, y in [(30, 100), (100, 20), (110, 108), (20, 70)]))

# 8. Шаховская — наконечник стрелы в витрине
I["shakhovskaya-museum"] = ("#F3E6FF", "#8C6AB8",
    "древний кремнёвый наконечник стрелы", "гордо лежит на красной бархатной подушечке в музейной витрине под стеклянной крышкой",
    rr(14, 82, 100, 36, 4, "#8A5A3A")
    + f'<path d="M14 92 H114" stroke="#6A4028" stroke-width="2"/>'
    + f'<path d="M20 82 V40 H108 V82" fill="#E8F6FF" opacity=".55" {s()}/>'
    + f'<path d="M30 46 L44 76 M86 44 L98 66" stroke="#fff" stroke-width="3" opacity=".9"/>'
    + f'<path d="M30 82 Q30 70 64 70 Q98 70 98 82Z" fill="#C4302B" {s()}/>'
    + f'<circle cx="34" cy="80" r="3" fill="#F2B632" {W(1.2)}/><circle cx="94" cy="80" r="3" fill="#F2B632" {W(1.2)}/>'
    + f'<path d="M64 20 L84 58 Q74 66 64 74 Q54 66 44 58Z" fill="#9AA0A8" {s()}/>'
    + f'<path d="M64 26 L60 40 M70 40 L64 54 M56 52 L52 58" stroke="#C6CCD2" stroke-width="2.2"/>'
    + f(64, 54, d=7, k=0.55)
    + sp((112, 30, 4), (16, 30, 3)))

# 9. Луховицы — чашечные весы на прилавке
I["lukhovitsy-museum"] = ("#E6FFE0", "#58A85A",
    "старинные латунные чашечные весы с гирькой", "взвешивают на деревянном базарном прилавке корзинку свежих огурчиков",
    rr(8, 96, 112, 30, 3, "#B57A44")
    + f'<path d="M8 106 H120" stroke="#8A5A30" stroke-width="2.4"/>'
    + rr(40, 88, 48, 10, 3, "#C9973C")
    + f'<path d="M64 88 V40" stroke="{O}" stroke-width="5"/><path d="M64 88 V40" stroke="#E2B54E" stroke-width="2.6"/>'
    + f'<path d="M22 46 L106 34" stroke="{O}" stroke-width="5"/><path d="M22 46 L106 34" stroke="#E2B54E" stroke-width="2.6"/>'
    + f'<circle cx="64" cy="40" r="5" fill="#E2B54E" {W(2)}/>'
    + f'<path d="M22 46 L12 68 M22 46 L32 68 M106 34 L96 56 M106 34 L116 56" stroke="{O}" stroke-width="1.8"/>'
    + f'<path d="M8 68 H36 Q34 80 22 80 Q10 80 8 68Z" fill="#E2B54E" {s()}/>'
    + f'<path d="M92 56 H120 Q118 68 106 68 Q94 68 92 56Z" fill="#E2B54E" {s()}/>'
    + f'<path d="M100 56 V48 Q106 42 112 48 V56Z" fill="#5A5E6A" {W(2)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="3.6" fill="#5DB24E" transform="rotate({r} {x} {y})" {W(1.6)}/>' for x, y, r in [(16, 64, -20), (26, 62, 15), (22, 58, -5)])
    + f(64, 66, d=7, k=0.5)
    + sp((40, 18, 4), (98, 82, 3)))

# 10. Ивантеевка — саженец сосны в питомнике
I["ivanteevka-museum"] = ("#FFF8D8", "#E0B44C",
    "крошечный саженец сосны с пушистой макушкой", "гордо растёт первым в длинном рядке питомника, за ним — взрослые сосны",
    "".join(f'<path d="M{x} 74 L{x-10} 74 L{x} 30 L{x+10} 74Z" fill="#3E7E4A" opacity=".55"/><rect x="{x-2}" y="74" width="4" height="8" fill="#7A5A3A" opacity=".55"/>' for x in (14, 40, 92, 116))
    + f'<path d="M0 82 H128 V128 H0Z" fill="#8A5E36" {s()}/>'
    + "".join(f'<path d="M0 {y} H128" stroke="#6E4628" stroke-width="2"/>' for y in (96, 112))
    + "".join(f'<path d="M{x} 96 v-8 M{x-3} 90 l3 -3 l3 3" stroke="#4F9A3E" stroke-width="2"/>' for x in (82, 96, 110, 124))
    + f'<rect x="58" y="78" width="10" height="24" fill="#9C6B3E" {s()}/>'
    + f'<path d="M63 22 L34 62 H92Z" fill="#5DB24E" {s()}/>'
    + f'<path d="M63 40 L28 82 H98Z" fill="#4FA24A" {s()}/>'
    + f(63, 64, d=10, k=0.7)
    + sp((104, 20, 5), (20, 22, 3)))

# 11. Зоосад «Дивный» — фенек у забора
I["divny-zoosad"] = ("#FFE9C8", "#F09A4A",
    "ушастый песочный фенек", "выглядывает из-за дощатого забора зоосада, над воротами висит подкова на счастье",
    "".join(f'<path d="M{x} 128 V70 L{x+7} 62 L{x+14} 70 V128Z" fill="#C98B4E" {W(2)}/>' for x in range(-2, 128, 15))
    + f'<path d="M0 86 H128 M0 112 H128" stroke="#8A5A30" stroke-width="5"/>'
    + f'<path d="M50 20 Q50 6 64 6 Q78 6 78 20" fill="none" stroke="#9AA0A8" stroke-width="7"/>'
    + f'<path d="M50 20 Q50 6 64 6 Q78 6 78 20" fill="none" stroke="{O}" stroke-width="1.6"/>'
    + f'<path d="M30 64 L18 14 L52 46Z" fill="#F2C88E" {s()}/><path d="M30 54 L24 26 L44 46Z" fill="#FFB0B8"/>'
    + f'<path d="M98 64 L110 14 L76 46Z" fill="#F2C88E" {s()}/><path d="M98 54 L104 26 L84 46Z" fill="#FFB0B8"/>'
    + f'<path d="M30 70 Q30 44 64 44 Q98 44 98 70 Q98 84 64 98 Q30 84 30 70Z" fill="#F2C88E" {s()}/>'
    + f'<path d="M48 80 Q64 92 80 80 Q72 96 64 98 Q56 96 48 80Z" fill="#FFF6E8"/>'
    + eye(52, 68, 0.8) + eye(76, 68, 0.8)
    + f'<ellipse cx="64" cy="82" rx="4" ry="3" fill="{O}"/>'
    + f'<ellipse cx="42" cy="78" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/><ellipse cx="86" cy="78" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/>'
    + f'<path d="M24 96 Q20 88 28 86 M104 96 Q108 88 100 86" fill="#F2C88E" {W(2.4)}/>'
    + sp((112, 30, 3)))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
