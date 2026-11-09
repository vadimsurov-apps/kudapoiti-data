"""Иконки робота fun (2026-11-09, 7-й проход): 56 мест из tools/add_fun_1109h.py.
Каждая придумана и нарисована отдельно (правило абсолютной уникальности): свой герой, своя сцена, своя палитра.
Сюжеты сверены с листами icons-catalog и icons-src/subjects.txt (паровозы, гнёзда, пчёлы, юла, роботы, витражи,
журавлики и т.п. уже заняты — поэтому у «Паровозово» колесо, билетик, дрезина, сумка кондуктора; у «Гнёзд» — качели-гнездо).
Запуск: python3 tools/icons_fun_1109h.py  (пишет icons-src/<id>.svg и печатает строки для subjects.txt)"""
import os, math
from draw_icons import s, face, sparkle, eye, O

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")


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


def kid(x, y, k=1.0, hair="#6B3F23"):
    return (f'<circle cx="{x}" cy="{y}" r="{10*k:.1f}" fill="#FFD9B8" {W(2.4)}/>'
            f'<path d="M{x-10*k:.1f} {y-1*k:.1f} Q{x-8*k:.1f} {y-12*k:.1f} {x} {y-11*k:.1f} Q{x+9*k:.1f} {y-11*k:.1f} {x+10*k:.1f} {y-2*k:.1f} Q{x+2*k:.1f} {y-7*k:.1f} {x-10*k:.1f} {y-1*k:.1f}Z" fill="{hair}" {W(2)}/>'
            + face(x, y + 1 * k, d=4 * k, k=0.42 * k))


def star(cx, cy, r1, r2, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r1 if i % 2 == 0 else r2
        a = math.radians(rot + i * 180 / n)
        pts.append(f"{cx + r*math.cos(a):.1f},{cy + r*math.sin(a):.1f}")
    return " ".join(pts)


I = {}

# ---------------- игровые комнаты ----------------
I["igrovaya-deti-lapshinka"] = ("#E8F7FF", "#7FC8F0",
    "голубой массажный мячик с мягкими пупырышками",
    "подпрыгивает на разноцветных мягких матах игровой, оставляя дугу прыжка",
    f'<path d="M-2 100 H40 V128 H-2Z" fill="#FF8FB1" {W(3)}/><path d="M40 100 H88 V128 H40Z" fill="#FFD25E" {W(3)}/>'
    f'<path d="M88 100 H130 V128 H88Z" fill="#8BE08B" {W(3)}/>'
    f'<path d="M20 92 Q40 30 64 40" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 6"/>'
    + "".join(f'<circle cx="{64+30*math.cos(math.radians(a)):.1f}" cy="{56+30*math.sin(math.radians(a)):.1f}" r="5" fill="#2F8FD8" {W(2.2)}/>' for a in range(0, 360, 30)) +
    f'<circle cx="64" cy="56" r="30" fill="#4FB0F0" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#BFE6FF"/>' for x, y in ((50, 40), (78, 40), (44, 60), (84, 62), (56, 76), (72, 78), (64, 34)))
    + face(64, 56, d=9, k=0.85) + f'<ellipse cx="64" cy="98" rx="20" ry="4" fill="#000" opacity=".12"/>')

I["colorumba-dekabristov"] = ("#FFF0FB", "#E58BD0",
    "праздничная пиньята-звезда с бумажной бахромой",
    "висит на ленте над праздником, а из открывшегося лучика сыплются конфеты",
    f'<path d="M64 -4 V28" {W(3)}/>'
    f'<polygon points="{star(64, 60, 34, 16)}" fill="#FFC93C" {W(3.2)}/>'
    + "".join(f'<path d="M{x} {y} l-4 8 M{x+4} {y} l-4 8" stroke="{c}" stroke-width="2.4" stroke-linecap="round"/>' for x, y, c in ((44, 56, "#FF5C8A"), (78, 56, "#3EC1D3"), (60, 70, "#7A5CFF")))
    + face(64, 58, d=8, k=0.8) +
    "".join(f'<rect x="{x}" y="{y}" width="9" height="6" rx="3" fill="{c}" {W(1.8)} transform="rotate({r} {x+4} {y+3})"/>' for x, y, c, r in ((86, 92, "#FF5C8A", 20), (98, 104, "#3EC1D3", -30), (78, 108, "#7DDB5A", 10), (92, 118, "#FFC93C", 40)))
    + sparkle(26, 34, 5) + sparkle(104, 30, 4))

I["kokosiki-selskokhozyaystvennaya"] = ("#F3FFE9", "#9BD87C",
    "мохнатый коричневый кокос с тремя тёмными точками-глазками",
    "съезжает по жёлтой детской горке игровой комнаты, раскинув лапки",
    f'<path d="M6 40 H40 L112 112 H78Z" fill="#FFD84A" {W(3.2)}/><path d="M40 40 L112 112" stroke="#F2B705" stroke-width="3"/>'
    f'<path d="M6 40 V120 M40 40 V60" {W(4)}/>'
    f'<circle cx="74" cy="68" r="24" fill="#8A5A34" {W(3.2)}/>'
    + "".join(f'<path d="M{74+20*math.cos(math.radians(a)):.1f} {68+20*math.sin(math.radians(a)):.1f} l{5*math.cos(math.radians(a)):.1f} {5*math.sin(math.radians(a)):.1f}" stroke="#5C3A1E" stroke-width="2"/>' for a in range(0, 360, 25)) +
    f'<circle cx="68" cy="52" r="2.4" fill="#3B2412"/><circle cx="80" cy="52" r="2.4" fill="#3B2412"/><circle cx="74" cy="58" r="2.4" fill="#3B2412"/>'
    + face(74, 70, d=8, k=0.75) +
    f'<path d="M52 66 l-12 -6 M96 66 l12 -8" {W(3)}/>' + sparkle(108, 36, 5))

I["chudo-cherdachok"] = ("#FFF6E5", "#E7B07A",
    "круглое чердачное окошко с распахнутыми зелёными ставнями",
    "под скатом крыши в окошке горит тёплый свет, а на подоконнике сидит плюшевый зайчик",
    f'<path d="M-4 70 L64 8 L132 70 V132 H-4Z" fill="#C0614A" {W(3.2)}/>'
    + "".join(f'<path d="M{8+i*16} {62-i*0} h12" stroke="#9E4A36" stroke-width="2"/>' for i in range(0)) +
    "".join(f'<path d="M{-4} {y} L132 {y}" stroke="#A84E3A" stroke-width="2" opacity=".6"/>' for y in (90, 108)) +
    f'<path d="M30 60 L18 44 V92 L30 84Z" fill="#6CC070" {W(2.6)}/><path d="M98 60 L110 44 V92 L98 84Z" fill="#6CC070" {W(2.6)}/>'
    f'<circle cx="64" cy="66" r="32" fill="#FFE59A" {W(3.4)}/>'
    f'<path d="M64 34 V98 M32 66 H96" stroke="#C0614A" stroke-width="3"/>'
    f'<ellipse cx="64" cy="94" rx="30" ry="5" fill="#8A4A2E" {W(2.4)}/>'
    f'<ellipse cx="60" cy="72" rx="7" ry="13" fill="#fff" {W(2.4)}/><ellipse cx="70" cy="72" rx="7" ry="13" fill="#fff" {W(2.4)}/>'
    f'<circle cx="65" cy="84" r="10" fill="#fff" {W(2.6)}/>' + face(65, 85, d=4, k=0.45))

I["star-lab-pervomayskaya"] = ("#3A3C8E", "#141640",
    "ночник-звёздочка на круглой подставке",
    "светит в тёмной комнате, рассыпая по стенам маленькие звёзды",
    f'<path d="M64 60 L10 128 H118Z" fill="#FFE98A" opacity=".18"/>'
    + "".join(sparkle(x, y, r, "#FFE98A") for x, y, r in ((20, 40, 4), (30, 78, 3), (100, 44, 5), (108, 82, 3), (86, 22, 3), (40, 20, 3))) +
    f'<rect x="44" y="96" width="40" height="12" rx="6" fill="#B9C3FF" {W(3)}/>'
    f'<path d="M64 96 V86" {W(4)}/>'
    f'<polygon points="{star(64, 58, 30, 14)}" fill="#FFE066" {W(3.2)}/>'
    + face(64, 58, d=7, k=0.7, mouth=False) +
    f'<path d="M59 66 Q64 70 69 66" fill="none" {W(2.4)}/>')

I["pautinka-kaleidoskop"] = ("#FFF4F0", "#F4A07F",
    "пушистый клубок шерстяных ниток",
    "размотался по игровой и связал ниточкой весёлую паутинку между столбиками",
    f'<path d="M12 30 L116 104 M12 104 L116 30 M64 12 V120 M0 66 H128" stroke="#7FA7E8" stroke-width="2.6"/>'
    + "".join(f'<circle cx="64" cy="66" r="{r}" fill="none" stroke="#7FA7E8" stroke-width="2.2"/>' for r in (22, 40, 56)) +
    f'<circle cx="64" cy="70" r="28" fill="#5D8FE0" {W(3.2)}/>'
    f'<path d="M40 60 Q64 48 88 64 M38 74 Q62 62 90 80 M46 88 Q66 78 86 90" fill="none" stroke="#3B6CC0" stroke-width="2.6"/>'
    + face(64, 70, d=8, k=0.8) + f'<path d="M90 82 Q108 96 100 116" fill="none" stroke="#5D8FE0" stroke-width="3"/>')

I["parovozovo-columbus"] = ("#FFF2E0", "#F28C3A",
    "большое красное колесо паровоза с шатуном",
    "катится по рельсам и выпускает над собой колечко белого пара",
    f'<path d="M-2 104 H130" stroke="#6B4A3A" stroke-width="5"/>'
    + "".join(f'<rect x="{x}" y="104" width="10" height="16" fill="#9A6A4A" {W(2)}/>' for x in (6, 34, 62, 90, 118)) +
    f'<circle cx="64" cy="66" r="36" fill="#E8434A" {W(3.4)}/><circle cx="64" cy="66" r="26" fill="#FF7A6E" {W(2.6)}/>'
    + "".join(f'<path d="M64 66 L{64+26*math.cos(math.radians(a)):.1f} {66+26*math.sin(math.radians(a)):.1f}" stroke="#B82A33" stroke-width="3"/>' for a in range(0, 360, 45)) +
    f'<circle cx="64" cy="66" r="12" fill="#FFD25E" {W(2.6)}/>' + face(64, 66, d=4.5, k=0.45) +
    f'<path d="M64 66 L118 80" stroke="#7C8796" stroke-width="7" stroke-linecap="round"/><path d="M64 66 L118 80" {W(2)} fill="none"/>'
    f'<ellipse cx="40" cy="20" rx="14" ry="9" fill="#fff" {W(2.4)}/><ellipse cx="40" cy="20" rx="6" ry="3.5" fill="#F7B26A"/>')

I["neofun-columbus"] = ("#2A1446", "#0B0618",
    "неоновая палочка-светяшка, изогнутая в широкую улыбку",
    "светится розовым и бирюзовым в тёмном зале, вокруг искры",
    f'<path d="M24 52 Q64 112 104 52" fill="none" stroke="#FF4FD8" stroke-width="16" stroke-linecap="round" opacity=".35"/>'
    f'<path d="M24 52 Q64 112 104 52" fill="none" stroke="#FF8BEA" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M24 52 Q64 112 104 52" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="44" cy="38" r="9" fill="#38F2E6" opacity=".4"/><circle cx="44" cy="38" r="5" fill="#9FFFF8"/>'
    f'<circle cx="84" cy="38" r="9" fill="#38F2E6" opacity=".4"/><circle cx="84" cy="38" r="5" fill="#9FFFF8"/>'
    + sparkle(20, 92, 5, "#FFE066") + sparkle(108, 96, 4, "#38F2E6") + sparkle(64, 20, 4, "#FF8BEA"))

I["neyroigrovaya-shchelkovsky"] = ("#F2FFF8", "#6FD3A7",
    "деревянная коробка-сортер с фигурными прорезями",
    "жёлтая звёздочка ныряет в прорезь-звезду, а кружок и треугольник ждут очереди",
    f'<path d="M24 64 H104 V114 H24Z" fill="#E7B47A" {W(3.2)}/><path d="M24 64 L36 50 H116 L104 64Z" fill="#F4CF9A" {W(3)}/>'
    f'<path d="M104 64 L116 50 V100 L104 114Z" fill="#C9935A" {W(3)}/>'
    f'<ellipse cx="52" cy="57" rx="7" ry="3" fill="{O}"/><path d="M80 54 l6 6 h-12z" fill="{O}"/>'
    + face(64, 90, d=10, k=0.8) +
    f'<polygon points="{star(64, 30, 16, 7)}" fill="#FFD23F" {W(2.8)}/>'
    f'<circle cx="22" cy="40" r="9" fill="#FF6F8E" {W(2.6)}/><path d="M104 22 l10 16 h-20z" fill="#4FA3E0" {W(2.6)}/>')

I["gnezda-likhobory"] = ("#FFFBEF", "#E3C27B",
    "круглые качели-гнездо из плетёной верёвки",
    "раскачиваются под потолком лофта, в них уютно лежат три пёстрые подушки",
    f'<path d="M30 -4 L44 70 M98 -4 L84 70 M64 -4 V58" {W(3)}/>'
    f'<ellipse cx="64" cy="80" rx="44" ry="18" fill="#7A5236" {W(3.2)}/>'
    f'<ellipse cx="64" cy="76" rx="36" ry="12" fill="#F5E2C0" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 68 L{x+10} 92" stroke="#5A3A24" stroke-width="2"/>' for x in range(26, 104, 10)) +
    f'<ellipse cx="46" cy="70" rx="12" ry="7" fill="#FF8FB1" {W(2.4)}/><ellipse cx="64" cy="66" rx="12" ry="7" fill="#7FD0F5" {W(2.4)}/>'
    f'<ellipse cx="82" cy="70" rx="12" ry="7" fill="#9BE07A" {W(2.4)}/>'
    + face(64, 86, d=12, k=0.8) + sparkle(110, 36, 5))

I["veselkin-kukhmisterova"] = ("#FFEFF0", "#F3797E",
    "праздничная дудка-язычок с пёрышком на конце",
    "разворачивается с писком над тортом со свечками",
    f'<path d="M26 92 H102 V116 H26Z" fill="#FFF4E8" {W(3)}/><path d="M26 92 Q34 100 42 92 Q50 100 58 92 Q66 100 74 92 Q82 100 90 92 Q96 100 102 92" fill="#FF9EC0" {W(2.4)}/>'
    + "".join(f'<rect x="{x}" y="76" width="5" height="16" fill="#7FC8F0" {W(1.8)}/><path d="M{x+2.5} 70 q3 4 0 6 q-3 -2 0 -6" fill="#FFB020"/>' for x in (44, 62, 80)) +
    f'<rect x="4" y="38" width="30" height="14" rx="6" fill="#FFD23F" {W(2.8)}/>'
    f'<path d="M34 45 Q60 20 84 42 Q100 58 112 38" fill="none" stroke="#3EB8E0" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M34 45 Q60 20 84 42 Q100 58 112 38" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 6"/>'
    f'<path d="M112 38 q10 -8 8 -18" fill="none" stroke="#FF5C8A" stroke-width="3"/>' + face(19, 45, d=5, k=0.42))

I["smile-school-zvenigorodskaya"] = ("#EAFBFF", "#64C6D8",
    "детская зелёная лейка с длинным носиком",
    "поливает на подоконнике цветок, и он расцветает широкой улыбкой",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#F5E6CF" {W(3)}/>'
    f'<path d="M84 104 L88 82 H108 L112 104Z" fill="#E8834E" {W(2.8)}/><path d="M98 82 V62" stroke="#3E9A4A" stroke-width="3"/>'
    + "".join(f'<ellipse cx="{98+9*math.cos(math.radians(a)):.1f}" cy="{54+9*math.sin(math.radians(a)):.1f}" rx="6" ry="4" fill="#FF8FB1" {W(1.8)} transform="rotate({a} {98+9*math.cos(math.radians(a)):.1f} {54+9*math.sin(math.radians(a)):.1f})"/>' for a in range(0, 360, 60)) +
    f'<circle cx="98" cy="54" r="7" fill="#FFD23F" {W(2)}/><path d="M94 55 Q98 60 102 55" fill="none" {W(1.8)}/>'
    f'<path d="M18 62 Q18 48 32 48 H58 Q70 48 70 62 V86 Q70 96 58 96 H30 Q18 96 18 86Z" fill="#5CC46A" {W(3.2)}/>'
    f'<path d="M66 60 L86 40" stroke="#5CC46A" stroke-width="7" stroke-linecap="round"/><path d="M66 60 L86 40" {W(2)}/>'
    f'<path d="M26 48 Q34 30 50 48" fill="none" {W(3.2)}/>'
    + face(44, 72, d=8, k=0.75) +
    "".join(f'<path d="M{x} {y} q2 4 0 6" stroke="#4FA3E0" stroke-width="2.4" fill="none"/>' for x, y in ((88, 44), (92, 50), (86, 52))))

I["parovozovo-okeania"] = ("#E5F9FF", "#4CB6D8",
    "кожаная сумка кондуктора на ремешке с компостером",
    "висит на крючке у вагона, из кармашка торчат разноцветные билетики",
    f'<path d="M22 -4 Q64 40 106 -4" fill="none" stroke="#8A5A2B" stroke-width="5"/>'
    f'<circle cx="64" cy="18" r="4" fill="#C9CED6" {W(2)}/>'
    f'<path d="M28 44 H100 V104 Q100 112 92 112 H36 Q28 112 28 104Z" fill="#B5713C" {W(3.2)}/>'
    f'<path d="M28 44 H100 V66 Q64 78 28 66Z" fill="#8F5326" {W(3)}/>'
    f'<rect x="58" y="62" width="12" height="10" rx="2" fill="#FFD23F" {W(2.2)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="12" height="22" rx="2" fill="{c}" {W(2)} transform="rotate({r} {x+6} {y+11})"/>' for x, y, c, r in ((36, 26, "#FF8FB1", -14), (50, 22, "#7FD0F5", -4), (78, 26, "#9BE07A", 12)))
    + face(64, 92, d=10, k=0.8))

I["ambiland-khoroshevskoe"] = ("#FFF8DD", "#F5B83C",
    "надувной мяч-прыгун с ручками-рожками",
    "скачет по игровому центру, на нём сидит малыш и держится за рожки",
    f'<ellipse cx="64" cy="114" rx="30" ry="6" fill="#000" opacity=".15"/>'
    f'<circle cx="64" cy="80" r="30" fill="#FF6F61" {W(3.2)}/>'
    f'<path d="M48 54 Q42 40 50 36 Q56 44 54 54 M80 54 Q86 40 78 36 Q72 44 74 54" fill="#FF6F61" {W(2.8)}/>'
    + face(64, 86, d=9, k=0.8) + kid(64, 36, 1.1, "#3A2A1A") +
    f'<path d="M52 44 Q48 50 50 54 M76 44 Q80 50 78 54" {W(3)} fill="none"/>'
    f'<path d="M22 70 l-8 -4 M22 84 l-10 0 M106 70 l8 -4 M106 84 l10 0" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["parovozovo-khoroshevskoe"] = ("#F0F3FF", "#8C9BEA",
    "высокая водоразборная колонка для паровоза с поворотным хоботом",
    "поливает водой маленький паровозик-котёл, вокруг брызги",
    f'<rect x="20" y="30" width="18" height="84" rx="4" fill="#5A6578" {W(3)}/>'
    f'<path d="M30 36 H90 Q100 36 100 46 V54" fill="none" stroke="#5A6578" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M30 36 H90 Q100 36 100 46 V54" fill="none" {W(2)}/>'
    f'<circle cx="29" cy="30" r="9" fill="#E8434A" {W(2.6)}/>' + face(29, 64, d=4, k=0.42) +
    "".join(f'<path d="M{x} {y} q2 5 0 8" stroke="#3EA8E8" stroke-width="3" fill="none"/>' for x, y in ((96, 60), (100, 66), (104, 60))) +
    f'<rect x="64" y="84" width="52" height="24" rx="10" fill="#3F8E5A" {W(3)}/><rect x="74" y="72" width="10" height="14" fill="#3F8E5A" {W(2.4)}/>'
    f'<circle cx="76" cy="110" r="7" fill="#333" {W(2)}/><circle cx="104" cy="110" r="7" fill="#333" {W(2)}/>'
    + face(96, 94, d=5, k=0.5))

I["detsky-klub-aviapark"] = ("#F2FBFF", "#9FD9F7",
    "посадочный талон с самолётиком и улыбкой",
    "проходит через турникет-калитку прямо в детский клуб",
    f'<path d="M-2 100 H130 V130 H-2Z" fill="#DDE7F2" {W(3)}/>'
    f'<rect x="84" y="62" width="14" height="40" rx="3" fill="#7C8796" {W(2.6)}/><path d="M84 72 H58" stroke="#E8434A" stroke-width="6" stroke-linecap="round"/>'
    f'<g transform="rotate(-10 52 56)"><rect x="18" y="34" width="70" height="42" rx="6" fill="#fff" {W(3.2)}/>'
    f'<path d="M66 34 V76" stroke="{O}" stroke-width="2" stroke-dasharray="3 4"/>'
    f'<path d="M72 48 l14 6 l-14 6 l3 -6z" fill="#4FA3E0" {W(1.8)}/>' + face(42, 54, d=7, k=0.7) + "</g>"
    + sparkle(106, 30, 5, "#fff") + sparkle(24, 96, 3))

I["igralife-festivalnaya"] = ("#F6F0FF", "#B18CF0",
    "пружинка-радуга",
    "шагает сама вниз по ступенькам, перекидываясь дугой",
    f'<path d="M-2 56 H40 V80 H72 V104 H104 V130 H-2Z" fill="#F0D9FF" {W(3)}/>'
    + "".join(f'<path d="M{24+i*3} 56 Q{48+i*3} {10+i*2} {70+i*3} 80" fill="none" stroke="{c}" stroke-width="5"/>' for i, c in enumerate(("#FF5C5C", "#FF9F40", "#FFD23F", "#5CD65C", "#3EA8E8", "#7A5CFF"))) +
    f'<ellipse cx="32" cy="54" rx="14" ry="5" fill="#FF7A7A" {W(2.4)}/><ellipse cx="80" cy="78" rx="14" ry="5" fill="#8E7AFF" {W(2.4)}/>'
    + face(54, 38, d=6, k=0.6))

I["malysh-maklysh-flotskaya"] = ("#FFF9EC", "#F7C86B",
    "белый детский стульчик для кормления с подносом",
    "стоит у столика фуд-корта, на подносе тарелка каши с ложкой",
    f'<path d="M36 70 H92 L84 120 M44 70 L36 120 M86 120 H34" {W(4)} fill="none"/>'
    f'<path d="M40 30 H88 V74 H40Z" fill="#fff" {W(3.2)}/>' + face(64, 50, d=8, k=0.75) +
    f'<rect x="28" y="70" width="72" height="10" rx="5" fill="#7FD0F5" {W(3)}/>'
    f'<ellipse cx="64" cy="68" rx="16" ry="5" fill="#FFE7B0" {W(2.4)}/><path d="M74 66 L92 54" stroke="#9AA5B4" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(104, 28, 5) + sparkle(22, 96, 4))

I["parovozovo-belomorskaya"] = ("#E7F8FF", "#70B9E8",
    "ручная дрезина с рычагом-коромыслом",
    "едет по рельсам вдоль моря, рычаг качается вверх-вниз",
    f'<path d="M-2 76 Q30 70 64 76 T130 76 V96 H-2Z" fill="#4FA3E0" {W(2.6)}/>'
    f'<path d="M-2 108 H130" stroke="#6B4A3A" stroke-width="5"/>'
    f'<rect x="24" y="84" width="80" height="16" rx="3" fill="#E8A44A" {W(3)}/>'
    f'<circle cx="40" cy="104" r="8" fill="#555" {W(2.4)}/><circle cx="88" cy="104" r="8" fill="#555" {W(2.4)}/>'
    f'<path d="M64 84 V56" {W(4)}/><path d="M34 46 L94 64" stroke="#C0392B" stroke-width="7" stroke-linecap="round"/><path d="M34 46 L94 64" {W(2)}/>'
    f'<circle cx="64" cy="56" r="5" fill="#FFD23F" {W(2)}/>' + face(64, 92, d=10, k=0.6) + sparkle(104, 26, 5))

I["flotiliya-loft"] = ("#F4FBFF", "#A6D6F2",
    "гирлянда морских сигнальных флажков",
    "натянута над праздничным столом с тортом-корабликом",
    f'<path d="M-2 22 Q64 52 130 22" fill="none" {W(2.6)}/>'
    + "".join(f'<rect x="{x-9}" y="{y}" width="18" height="18" fill="{a}" {W(2.2)}/><path d="M{x-9} {y} L{x+9} {y+18}" stroke="{b}" stroke-width="5"/>' for x, y, a, b in ((14, 26, "#FFD23F", "#2F6FD8"), (40, 34, "#fff", "#E8434A"), (64, 38, "#2F6FD8", "#fff"), (88, 34, "#E8434A", "#FFD23F"), (114, 26, "#fff", "#2F6FD8")))
    + f'<path d="M14 104 H114" stroke="#9A6A4A" stroke-width="6"/>'
    f'<path d="M38 82 H90 L82 100 H46Z" fill="#fff" {W(3)}/><path d="M64 82 V62 L82 78Z" fill="#FF8FB1" {W(2.4)}/>'
    + face(64, 90, d=8, k=0.55))

I["yula-park-cheremushkinskaya"] = ("#FFF0F6", "#F28DB2",
    "трёхлопастный спиннер с подшипниками-глазками",
    "волчком крутится на пальчике малыша, оставляя цветной круг",
    f'<circle cx="64" cy="56" r="44" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="6 8" opacity=".8"/>'
    + "".join(f'<circle cx="{64+24*math.cos(math.radians(a)):.1f}" cy="{56+24*math.sin(math.radians(a)):.1f}" r="15" fill="{c}" {W(3)}/><circle cx="{64+24*math.cos(math.radians(a)):.1f}" cy="{56+24*math.sin(math.radians(a)):.1f}" r="6" fill="#C9CED6" {W(2)}/>' for a, c in ((-90, "#7A5CFF"), (30, "#3EC1D3"), (150, "#FFB020")))
    + f'<circle cx="64" cy="56" r="13" fill="#FF5C8A" {W(3)}/>' + face(64, 56, d=4.5, k=0.45) +
    f'<path d="M58 70 Q56 100 50 124 H78 Q72 100 70 70Z" fill="#FFD9B8" {W(2.8)}/>')

I["skazochny-gorod-kashirskoe"] = ("#F2FFEA", "#7CC56A",
    "сказочный деревянный колодец-журавль",
    "журавль наклонился, а из ведёрка на цепочке выглядывает лягушонок в короне",
    f'<path d="M-2 104 Q64 96 130 104 V130 H-2Z" fill="#5FAE4E" {W(3)}/>'
    f'<rect x="30" y="74" width="40" height="34" fill="#B07A48" {W(3)}/>'
    + "".join(f'<path d="M30 {y} H70" stroke="#7A5032" stroke-width="2"/>' for y in (84, 96)) +
    f'<path d="M96 106 V40" {W(5)}/><path d="M104 22 L38 58" stroke="#8A5A2B" stroke-width="6" stroke-linecap="round"/><path d="M104 22 L38 58" {W(2)}/>'
    f'<path d="M40 58 V66" {W(2.4)}/><path d="M32 66 H50 L48 76 H34Z" fill="#9AA5B4" {W(2.4)}/>'
    f'<ellipse cx="41" cy="64" rx="7" ry="5" fill="#7DDB5A" {W(2)}/><path d="M36 58 l2 -4 2 3 2 -4 2 3 2 -4 1 6z" fill="#FFD23F" {W(1.4)}/>'
    + face(50, 90, d=7, k=0.55))

I["tusa-dzhusa-sevastopolsky"] = ("#FFFCE6", "#FFC24A",
    "коробочка сока с трубочкой",
    "пританцовывает на праздничном столе под конфетти, держа трубочку как микрофон",
    f'<path d="M38 44 H90 V112 H38Z" fill="#FF9F40" {W(3.2)}/><path d="M38 44 L46 32 H82 L90 44Z" fill="#FFC27A" {W(3)}/>'
    f'<circle cx="64" cy="64" r="12" fill="#FFE066" {W(2.4)}/><path d="M58 60 l12 -2" stroke="#5CB85C" stroke-width="3"/>'
    + face(64, 90, d=9, k=0.75) +
    f'<path d="M74 32 V12 L86 6" fill="none" stroke="#FF5C8A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M38 70 Q24 64 20 50 M90 70 Q104 78 110 92" {W(3.4)} fill="none"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="5" height="9" fill="{c}" transform="rotate({r} {x} {y})"/>' for x, y, c, r in ((16, 28, "#3EC1D3", 20), (104, 34, "#FF5C8A", -30), (110, 60, "#7A5CFF", 15), (18, 92, "#7DDB5A", -20))))

I["tusa-dzhusa-sokol"] = ("#F3EEFF", "#9E86E8",
    "конверт-приглашение с сургучной печатью-сердечком",
    "летит на крылышках к имениннику, из-под клапана выглядывает открытка",
    f'<path d="M14 46 Q2 30 18 26 Q30 30 28 44Z M114 46 Q126 30 110 26 Q98 30 100 44Z" fill="#fff" {W(2.6)}/>'
    f'<rect x="24" y="40" width="80" height="56" rx="6" fill="#FFF6E8" {W(3.2)}/>'
    f'<path d="M30 30 H98 V60 H30Z" fill="#7FD0F5" {W(2.4)}/>'
    f'<path d="M24 40 L64 72 L104 40" fill="#FFE7C2" {W(3)}/>'
    f'<path d="M64 66 Q54 56 60 52 Q64 52 64 56 Q64 52 68 52 Q74 56 64 66Z" fill="#E8434A" {W(2.2)}/>'
    + face(64, 84, d=10, k=0.65) + sparkle(18, 104, 4) + sparkle(110, 106, 5))

I["atmosfera-usievicha"] = ("#FFF6EE", "#E9A47B",
    "шалаш из клетчатого пледа на подушках",
    "из-под пледа светит фонарик и выглядывают две пары детских глаз",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#C88660" {W(3)}/>'
    f'<path d="M16 108 L64 26 L112 108Z" fill="#4E9B6A" {W(3.4)}/>'
    + "".join(f'<path d="M{64-(y-26)*0.58:.1f} {y} H{64+(y-26)*0.58:.1f}" stroke="#3B7A52" stroke-width="3"/>' for y in (50, 72, 94)) +
    "".join(f'<path d="M{x} {26+abs(x-64)*1.7:.0f} V108" stroke="#E8434A" stroke-width="2.4" opacity=".7"/>' for x in (48, 64, 80)) +
    f'<path d="M44 108 Q64 66 84 108Z" fill="#2E2240" {W(3)}/>'
    + eye(56, 92, 0.7) + eye(64, 92, 0.7) + eye(70, 98, 0.6) + eye(77, 98, 0.6) +
    f'<path d="M64 26 L62 14" {W(3)}/><circle cx="62" cy="12" r="4" fill="#FFE066" {W(2)}/>'
    f'<ellipse cx="24" cy="106" rx="16" ry="8" fill="#FFB3C7" {W(2.6)}/><ellipse cx="104" cy="106" rx="16" ry="8" fill="#8FD3F5" {W(2.6)}/>')

I["kids-town-volokolamskoe"] = ("#EEF9FF", "#7BB4E8",
    "синий уличный почтовый ящик на ножке",
    "проглатывает письмо-рисунок с солнышком, которое опускает малыш",
    f'<path d="M-2 110 H130 V130 H-2Z" fill="#B7C7D8" {W(3)}/>'
    f'<path d="M70 110 V92" {W(5)}/>'
    f'<path d="M48 40 Q48 24 70 24 Q92 24 92 40 V92 H48Z" fill="#2F6FD8" {W(3.2)}/>'
    f'<rect x="56" y="44" width="28" height="6" rx="3" fill="{O}"/>' + face(70, 66, d=8, k=0.75) +
    f'<g transform="rotate(-20 46 40)"><rect x="30" y="28" width="26" height="20" fill="#fff" {W(2.4)}/><circle cx="43" cy="38" r="5" fill="#FFD23F"/></g>'
    + kid(22, 70, 1.0) + f'<path d="M22 80 V108 M14 108 H30" {W(3.4)}/><path d="M24 84 L36 52" {W(3)}/>')

I["kulikova-igrovoy-tsentr"] = ("#FFF4FA", "#F2A7CA",
    "розовая соска-пустышка с колечком",
    "дремлет в мягкой колыбельке из подушек под луной-погремушкой",
    f'<path d="M14 96 Q64 130 114 96 Q114 84 102 84 H26 Q14 84 14 96Z" fill="#B9E3FF" {W(3.2)}/>'
    f'<ellipse cx="64" cy="80" rx="22" ry="12" fill="#fff" {W(2.6)}/>'
    f'<ellipse cx="64" cy="66" rx="26" ry="16" fill="#FF8FB8" {W(3.2)}/>'
    f'<circle cx="64" cy="44" r="14" fill="none" stroke="#FF6FA2" stroke-width="5"/>'
    f'<ellipse cx="64" cy="84" rx="10" ry="8" fill="#FFD0E2" {W(2.4)}/>'
    + face(64, 66, d=10, k=0.7, mouth=False) +
    f'<path d="M54 66 q4 3 0 0 M70 66 q4 3 0 0" fill="none"/>'
    f'<text x="90" y="34" font-size="12" font-family="Arial" font-weight="700" fill="#fff">z</text>'
    f'<path d="M104 14 A14 14 0 1 0 112 36 A11 11 0 1 1 104 14Z" fill="#FFE066" {W(2.4)}/>')

I["pchelki-loft-orekhovo"] = ("#FFFDE8", "#E9D35A",
    "пушистый одуванчик",
    "дует ветер, и его пушинки разлетаются по лофту как праздничное конфетти",
    f'<path d="M50 128 Q52 96 54 70" fill="none" stroke="#4E9B4E" stroke-width="5"/>'
    f'<path d="M52 104 Q36 96 32 104 Q40 112 52 108" fill="#6CC070" {W(2.4)}/>'
    + "".join(f'<path d="M54 60 L{54+30*math.cos(math.radians(a)):.1f} {60+30*math.sin(math.radians(a)):.1f}" stroke="#fff" stroke-width="2"/><circle cx="{54+30*math.cos(math.radians(a)):.1f}" cy="{60+30*math.sin(math.radians(a)):.1f}" r="4" fill="#fff" {W(1.4)}/>' for a in range(0, 360, 24)) +
    f'<circle cx="54" cy="60" r="13" fill="#F4F1E0" {W(2.6)}/>' + face(54, 60, d=4.5, k=0.45) +
    "".join(f'<path d="M{x} {y} l{6} {-6}" stroke="#fff" stroke-width="2"/><circle cx="{x+7}" cy="{y-7}" r="3.6" fill="#fff" {W(1.2)}/>' for x, y in ((92, 40), (104, 58), (98, 80), (112, 34)))
    + f'<path d="M6 30 Q20 24 30 30" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>')

# ---------------- квесты ----------------
I["quest-corporation-pervomayskaya"] = ("#3C2B22", "#170E09",
    "старинная книга-тайник с вырезанными страницами",
    "раскрылась на столе при свече, в углублении блестит маленький золотой ключик",
    f'<path d="M14 72 L64 82 L114 72 L114 108 L64 118 L14 108Z" fill="#7A3B2E" {W(3.2)}/>'
    f'<path d="M20 70 L64 78 L108 70 L108 98 L64 106 L20 98Z" fill="#F3E2C2" {W(2.6)}/>'
    f'<path d="M64 78 V106" {W(2)}/>'
    f'<rect x="72" y="80" width="26" height="16" rx="2" fill="#B98A5A" {W(2)}/>'
    f'<circle cx="78" cy="88" r="4" fill="none" stroke="#FFC93C" stroke-width="2.6"/><path d="M82 88 H94 M90 88 V92" stroke="#FFC93C" stroke-width="2.6"/>'
    + face(40, 88, d=6, k=0.6) +
    f'<rect x="96" y="30" width="10" height="30" rx="2" fill="#FFF4D6" {W(2.4)}/><path d="M101 30 q5 -8 0 -14 q-5 6 0 14" fill="#FFB020" {W(1.6)}/>'
    f'<circle cx="101" cy="22" r="18" fill="#FFB020" opacity=".18"/>')

I["komponent-vladimirskaya"] = ("#E6FFF0", "#3FBF85",
    "огромный круглый глаз-циклоп в дверном глазке",
    "подглядывает в глазок двери квеста: кто пришёл на «Монстров на каникулах»?",
    f'<rect x="20" y="4" width="88" height="128" rx="6" fill="#8E5BC8" {W(3.4)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="30" height="34" rx="3" fill="none" stroke="#6E3FA8" stroke-width="2.6"/>' for x, y in ((30, 16), (68, 16), (30, 90), (68, 90))) +
    f'<circle cx="64" cy="64" r="24" fill="#C9CED6" {W(3.4)}/><circle cx="64" cy="64" r="18" fill="#fff" {W(2.4)}/>'
    f'<circle cx="64" cy="64" r="11" fill="#5CC46A" {W(2)}/><circle cx="64" cy="64" r="5" fill="{O}"/><circle cx="61" cy="61" r="2" fill="#fff"/>'
    f'<path d="M48 52 Q64 42 80 52" fill="none" {W(2.6)}/>'
    f'<circle cx="94" cy="78" r="5" fill="#FFD23F" {W(2.4)}/>')

I["igra-sudby-dzhungli-kurkino"] = ("#E9FFE2", "#3E9A4A",
    "хищное растение-мухоловка с зубастыми листьями-челюстями",
    "в чаще джунглей пытается поймать пролетающего светлячка, но тот хихикает",
    f'<path d="M-4 20 Q20 40 8 70 M132 10 Q104 36 120 70" fill="none" stroke="#2E7A38" stroke-width="5"/>'
    f'<path d="M58 128 Q60 100 64 86" fill="none" stroke="#3B8A3F" stroke-width="5"/>'
    f'<path d="M64 86 Q30 80 30 54 Q46 62 64 72Z" fill="#7DCB5A" {W(3)}/><path d="M64 86 Q100 78 100 50 Q82 60 64 72Z" fill="#E8434A" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} l-3 -6 l6 1z" fill="#fff" {W(1.4)}/>' for x, y in ((38, 60), (46, 64), (54, 68))) +
    "".join(f'<path d="M{x} {y} l3 -6 l-6 1z" fill="#fff" {W(1.4)}/>' for x, y in ((92, 56), (84, 62), (76, 66))) +
    eye(48, 76, 0.7) + eye(80, 72, 0.7) +
    f'<ellipse cx="86" cy="26" rx="7" ry="5" fill="#FFE066" {W(2)}/><circle cx="86" cy="26" r="12" fill="#FFE066" opacity=".3"/>'
    f'<path d="M82 21 q-4 -6 -8 -2 M90 21 q4 -6 8 -2" fill="none" {W(1.6)}/>'
    f'<path d="M104 112 Q96 100 108 96 Q116 104 104 112Z" fill="#5FAE4E" {W(2.2)}/>')

I["gravity-falls-chertanovo"] = ("#2D2A55", "#100E26",
    "хрустальный шар гадалки на подставке-лапках",
    "в нём клубится зелёный туман и проступает силуэт таинственной хижины в соснах",
    f'<path d="M36 104 H92 L86 116 H42Z" fill="#8A5A2B" {W(3)}/>'
    f'<path d="M40 104 Q36 94 44 92 M88 104 Q92 94 84 92 M64 104 V94" {W(3)}/>'
    f'<circle cx="64" cy="64" r="34" fill="#BFE9FF" opacity=".35" {W(3.2)}/>'
    f'<path d="M36 70 Q50 58 64 70 T92 66" fill="none" stroke="#7DFFB0" stroke-width="5" opacity=".7"/>'
    f'<path d="M50 84 L64 64 L78 84Z" fill="#3E2A1E"/><path d="M42 86 l6 -14 l6 14z M76 86 l6 -16 l6 16z" fill="#1F4A2A"/>'
    f'<rect x="61" y="74" width="5" height="6" fill="#FFE066"/>'
    f'<ellipse cx="52" cy="46" rx="8" ry="4" fill="#fff" opacity=".6"/>'
    + sparkle(20, 30, 4, "#BFE9FF") + sparkle(106, 24, 5, "#7DFFB0") + sparkle(110, 70, 3, "#fff"))

I["vr-planets-kuzminki"] = ("#1C2A5A", "#060B22",
    "квадратная пиксельная планета из цветных кубиков-вокселей",
    "парит в космосе на орбите вокруг VR-контроллера с кнопкой",
    f'<ellipse cx="64" cy="60" rx="52" ry="14" fill="none" stroke="#7FD0F5" stroke-width="3" transform="rotate(-14 64 60)"/>'
    + "".join(f'<rect x="{40+i*12}" y="{36+j*12}" width="12" height="12" fill="{c}" {W(1.8)}/>' for i in range(4) for j in range(4)
              for c in [("#3EC1D3", "#5CD65C", "#3EC1D3", "#5CD65C", "#5CD65C", "#3EC1D3", "#FFD23F", "#3EC1D3", "#3EC1D3", "#5CD65C", "#3EC1D3", "#5CD65C", "#5CD65C", "#3EC1D3", "#5CD65C", "#3EC1D3")[i * 4 + j]])
    + face(64, 60, d=8, k=0.7) +
    f'<path d="M86 96 Q100 88 108 100 L104 118 Q96 124 90 116Z" fill="#E6E9F0" {W(2.6)}/><circle cx="98" cy="100" r="4" fill="#FF5C8A" {W(1.6)}/>'
    + sparkle(20, 26, 4) + sparkle(24, 100, 3) + sparkle(108, 28, 3))

I["chudopolis-botsad"] = ("#FFF1F8", "#F09BC2",
    "чудо-дерево, на ветках которого растут леденцы и пряники",
    "стоит посреди праздника, а с ветки сам падает в ладошки леденец",
    f'<path d="M58 128 L60 82 Q52 70 40 66 M62 84 Q72 70 88 64 M60 84 V56" fill="none" stroke="#8A5A2B" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M58 128 L60 82 Q52 70 40 66 M62 84 Q72 70 88 64 M60 84 V56" fill="none" {W(2)}/>'
    f'<circle cx="62" cy="44" r="30" fill="#7DCB7A" {W(3.2)}/><circle cx="36" cy="58" r="18" fill="#7DCB7A" {W(3)}/><circle cx="92" cy="56" r="18" fill="#7DCB7A" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}" {W(2)}/><path d="M{x-4} {y-2} Q{x} {y+4} {x+4} {y-2}" stroke="#fff" stroke-width="1.6" fill="none"/>' for x, y, c in ((48, 30, "#FF5C8A"), (78, 34, "#3EC1D3"), (32, 58, "#FFD23F"), (96, 54, "#FF8F3C")))
    + f'<path d="M62 44 l8 0 l-2 8 h-4z" fill="#C98B4E" {W(1.6)}/>' + face(62, 58, d=7, k=0.6) +
    f'<circle cx="94" cy="100" r="6" fill="#B28CFF" {W(2)}/><path d="M94 106 V116" {W(2.4)}/>')

I["proekt-luch-yasenevo"] = ("#FFFCEB", "#F5D06A",
    "солнечный зайчик от маленького круглого зеркальца",
    "прыгает пятнышком по стене, а котёнок вытягивает лапку, пытаясь его поймать",
    f'<path d="M-2 100 H130 V130 H-2Z" fill="#E9C27E" {W(3)}/>'
    f'<path d="M22 74 L96 30" stroke="#FFF6B0" stroke-width="12" opacity=".6"/>'
    f'<circle cx="22" cy="76" r="12" fill="#C9E8FF" {W(3)}/><path d="M22 88 V100" {W(4)}/>'
    f'<circle cx="98" cy="30" r="15" fill="#FFF3A0" {W(2.4)}/>' + face(98, 30, d=5, k=0.5) +
    f'<ellipse cx="80" cy="92" rx="18" ry="12" fill="#F7A65A" {W(3)}/><circle cx="68" cy="80" r="12" fill="#F7A65A" {W(3)}/>'
    f'<path d="M58 74 L60 62 L66 70 M72 70 L78 62 L78 74" fill="#F7A65A" {W(2.4)}/>' + face(68, 82, d=4.5, k=0.45) +
    f'<path d="M86 84 L94 50" stroke="#F7A65A" stroke-width="6" stroke-linecap="round"/><path d="M86 84 L94 50" {W(2)} fill="none"/>')

I["ostrov-diskaveri-prince-plaza"] = ("#E3FBFF", "#46B9D2",
    "стеклянная бутылка с запиской-свитком внутри",
    "приплыла на волне к песчаному берегу острова, пробка подмигивает",
    f'<path d="M-2 92 Q30 84 64 92 T130 90 V130 H-2Z" fill="#2E8FC8" {W(3)}/>'
    f'<path d="M60 104 Q94 96 130 108 V130 H60Z" fill="#F4D58D" {W(3)}/>'
    f'<g transform="rotate(-28 62 68)"><path d="M40 52 H74 Q84 52 84 60 V64 H96 V74 H84 V78 Q84 86 74 86 H40 Q30 86 30 76 V62 Q30 52 40 52Z" fill="#BFF3E0" opacity=".85" {W(3)}/>'
    f'<rect x="96" y="62" width="8" height="14" rx="2" fill="#C98B4E" {W(2)}/>'
    f'<rect x="40" y="60" width="32" height="18" rx="3" fill="#FFF4D6" {W(2)}/><path d="M44 66 H66 M44 72 H60" stroke="#8A5A2B" stroke-width="1.6"/></g>'
    + face(54, 78, d=7, k=0.55) + sparkle(102, 28, 5, "#fff"))

I["ostrov-diskaveri-flotskaya"] = ("#FFF7E0", "#F2A541",
    "бамбуковый плот с парусом из полосатой рубашки",
    "плывёт по бирюзовой воде к острову, на мачте развевается флажок",
    f'<path d="M-2 86 Q30 80 64 86 T130 84 V130 H-2Z" fill="#3EC1C9" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="78" width="12" height="18" rx="5" fill="#D8B45A" {W(2.4)}/>' for x in range(24, 104, 13)) +
    f'<path d="M64 78 V20" {W(4)}/><path d="M64 26 Q92 40 64 66Z" fill="#fff" {W(2.8)}/>'
    + "".join(f'<path d="M66 {y} Q{72+ (y-26)*0.5:.0f} {y+2} {66+ (26 if y<46 else 18)} {y+3}" stroke="#2F6FD8" stroke-width="3" fill="none"/>' for y in (34, 44, 54)) +
    f'<path d="M64 20 L80 14 L64 8Z" fill="#E8434A" {W(2)}/>' + face(46, 87, d=6, k=0.55) +
    f'<path d="M104 70 Q112 58 120 70 Z" fill="#5FAE4E" {W(2)}/>')

I["kapitan-kvest-stroiteley"] = ("#2A3A6E", "#0D1530",
    "латунный секстант с зеркальцами",
    "ловит путеводную звезду над ночной палубой",
    f'<path d="M-2 100 H130 V130 H-2Z" fill="#8A5A2B" {W(3)}/>' + "".join(f'<path d="M{x} 100 V130" stroke="#6B4423" stroke-width="2"/>' for x in (20, 48, 76, 104)) +
    f'<path d="M30 92 A40 40 0 0 1 98 92Z" fill="none" stroke="#E0A82E" stroke-width="7"/><path d="M30 92 A40 40 0 0 1 98 92" fill="none" {W(2)}/>'
    + "".join(f'<path d="M{64+40*math.cos(math.radians(a)):.1f} {92-40*math.sin(math.radians(a)):.1f} l{-4*math.cos(math.radians(a)):.1f} {4*math.sin(math.radians(a)):.1f}" stroke="{O}" stroke-width="2"/>' for a in range(10, 171, 16)) +
    f'<path d="M64 92 L64 44 M64 92 L88 52" {W(3.4)}/><rect x="56" y="40" width="16" height="10" rx="2" fill="#BFE9FF" {W(2.4)}/>'
    f'<circle cx="64" cy="92" r="7" fill="#FFC93C" {W(2.4)}/>' + face(64, 70, d=7, k=0.6) +
    f'<polygon points="{star(98, 22, 10, 4)}" fill="#FFE066" {W(1.8)}/>' + sparkle(24, 30, 3) + sparkle(40, 14, 2.5))

# ---------------- мастер-классы ----------------
I["kulibin-serebryakova"] = ("#FBF2E8", "#D49A6A",
    "глиняная свистулька-окарина в форме птички",
    "сохнет на полке мастерской и пробует свистеть: из клюва вылетают ноты",
    f'<path d="M-2 98 H130 V110 H-2Z" fill="#A86E44" {W(3)}/>'
    f'<path d="M30 80 Q28 54 56 52 Q82 50 92 66 L112 62 L98 76 Q92 96 60 96 Q34 96 30 80Z" fill="#E7A26A" {W(3.2)}/>'
    f'<path d="M40 60 Q50 44 66 52" fill="#E7A26A" {W(2.8)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#7A4425"/>' for x, y in ((50, 82), (62, 84), (74, 82))) +
    face(58, 68, d=7, k=0.6) +
    f'<path d="M106 40 V26 l8 -3 v13" fill="none" {W(2.4)}/><circle cx="104" cy="41" r="3" fill="{O}"/><circle cx="112" cy="37" r="3" fill="{O}"/>'
    f'<path d="M20 30 V20" {W(2.4)}/><circle cx="18" cy="31" r="3" fill="{O}"/>')

I["artclay-katukova"] = ("#EAF3FF", "#7FA3D8",
    "квадратная керамическая плитка-изразец с синей птицей",
    "сохнет на подставке рядом с кисточкой и баночкой глазури",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#E7D6C0" {W(3)}/>'
    f'<rect x="28" y="24" width="70" height="70" rx="6" fill="#FFF8EC" {W(3.4)}/>'
    f'<rect x="34" y="30" width="58" height="58" rx="4" fill="none" stroke="#2F6FD8" stroke-width="3"/>'
    f'<path d="M44 68 Q50 50 66 52 Q74 44 82 50 L90 48 L82 56 Q78 70 62 72 L52 78Z" fill="#4F86E8" {W(2.4)}/>'
    + eye(74, 54, 0.5) +
    "".join(f'<path d="M{x} {y} l3 3 l-3 3 l-3 -3z" fill="#2F6FD8"/>' for x, y in ((40, 34), (86, 34), (40, 82), (86, 82))) +
    f'<rect x="102" y="80" width="16" height="24" rx="3" fill="#7FD0F5" {W(2.4)}/>'
    f'<path d="M108 60 L104 100" stroke="#C98B4E" stroke-width="4" stroke-linecap="round"/>'
    + face(63, 100, d=7, k=0.5))

I["nemalevichi-sirenevy"] = ("#FFF4EC", "#F7A08A",
    "мятый тюбик масляной краски",
    "выдавливает на холст длинную радужную змейку, свернувшуюся в улыбку",
    f'<rect x="10" y="66" width="92" height="56" rx="4" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M24 {100-i*4} Q56 {124-i*4} 88 {96-i*4}" fill="none" stroke="{c}" stroke-width="4"/>' for i, c in enumerate(("#7A5CFF", "#3EA8E8", "#5CD65C", "#FFD23F", "#FF5C5C"))) +
    f'<g transform="rotate(30 84 40)"><path d="M62 28 H100 L104 52 H58Z" fill="#E6E9F0" {W(3)}/>'
    f'<rect x="100" y="34" width="10" height="12" rx="2" fill="#E8434A" {W(2)}/>'
    f'<path d="M58 30 V50" stroke="#9AA5B4" stroke-width="3"/>' + face(80, 40, d=6, k=0.55) + "</g>"
    + sparkle(24, 30, 5))

I["nemalevichi-profsoyuznaya-156"] = ("#F4FFE8", "#A7D86A",
    "бумажная лягушка-оригами",
    "прыгает с листа цветной бумаги, оставляя сгибы-лучики",
    f'<rect x="14" y="88" width="56" height="34" fill="#FFB3C7" {W(2.6)}/><path d="M14 88 L70 122" stroke="#F28DB2" stroke-width="2"/>'
    f'<rect x="62" y="96" width="50" height="30" fill="#8FD3F5" {W(2.6)}/>'
    f'<path d="M40 76 L64 30 L92 66 L76 84 Z" fill="#46B85A" {W(3)}/>'
    f'<path d="M64 30 L66 70 L40 76 M66 70 L92 66 M66 70 L76 84" stroke="#2E8A40" stroke-width="2" fill="none"/>'
    f'<path d="M40 76 L26 88 L46 84 M76 84 L80 100 L86 84" fill="#46B85A" {W(2.4)}/>'
    + eye(58, 48, 0.6) + eye(70, 48, 0.6) +
    f'<path d="M94 30 q8 -4 12 2 M100 44 q8 0 10 6" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>')

I["detskie-mk-shchelkovsky"] = ("#FFF0F4", "#E87FA0",
    "пушистый помпон из пряжи на картонном колечке",
    "только что вырос из двух колечек, рядом лежат детские ножницы с круглыми кончиками",
    "".join(f'<path d="M64 60 l{30*math.cos(math.radians(a)):.1f} {30*math.sin(math.radians(a)):.1f}" stroke="{c}" stroke-width="5" stroke-linecap="round"/>' for a, c in zip(range(0, 360, 15), ["#FFC93C", "#FF8F3C"] * 12))
    + f'<circle cx="64" cy="60" r="24" fill="#FFB020" {W(3)}/>'
    f'<ellipse cx="64" cy="98" rx="28" ry="8" fill="#C9935A" {W(2.6)}/><ellipse cx="64" cy="98" rx="14" ry="4" fill="#F28DB2"/>'
    + face(64, 60, d=8, k=0.75) +
    f'<path d="M96 104 L118 88 M96 88 L118 104" stroke="#9AA5B4" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="92" cy="108" r="6" fill="none" stroke="#3EA8E8" stroke-width="4"/><circle cx="92" cy="84" r="6" fill="none" stroke="#3EA8E8" stroke-width="4"/>')

I["art-chudo-pervomayskaya"] = ("#F1FFF4", "#86C99A",
    "глиняная тарелочка с отпечатком кленового листа",
    "лежит на гончарном столе, рядом настоящий кленовый лист и стека",
    f'<ellipse cx="64" cy="72" rx="48" ry="40" fill="#E9B98C" {W(3.4)}/><ellipse cx="64" cy="72" rx="38" ry="31" fill="#F2CFA8" {W(2.4)}/>'
    f'<path d="M64 46 L70 58 L82 54 L78 66 L90 72 L76 76 L80 88 L68 82 L64 96 L60 82 L48 88 L52 76 L38 72 L50 66 L46 54 L58 58Z" fill="#D49464" {W(2.2)}/>'
    f'<path d="M64 56 V92" stroke="#B7774A" stroke-width="2"/>' + face(64, 72, d=7, k=0.6) +
    f'<path d="M100 22 L106 32 L116 28 L112 38 L120 42 L110 46 L112 56 L104 50 L100 60 L96 50 L88 54 L90 44 L82 40 L90 36 L88 26 L96 30Z" fill="#E8634A" {W(2)}/>'
    f'<path d="M14 26 L40 34" stroke="#8A5A2B" stroke-width="4" stroke-linecap="round"/>')

I["glazalmaz-izmaylovsky"] = ("#F5EEFF", "#A88AE0",
    "кудрявый театральный парик на деревянной болванке-голове",
    "подмигивает из гримёрки перед спектаклем, рядом лампочки зеркала",
    "".join(f'<circle cx="{x}" cy="16" r="5" fill="#FFF3A0" {W(1.8)}/>' for x in (14, 38, 90, 114)) +
    f'<path d="M48 112 H80 L76 96 H52Z" fill="#B07A48" {W(3)}/>'
    f'<ellipse cx="64" cy="70" rx="22" ry="28" fill="#E7C49A" {W(3)}/>'
    + "".join(f'<circle cx="{64+28*math.cos(math.radians(a)):.1f}" cy="{58+26*math.sin(math.radians(a)):.1f}" r="11" fill="#FF8F3C" {W(2.6)}/>' for a in range(170, 375, 22)) +
    f'<circle cx="64" cy="34" r="11" fill="#FF8F3C" {W(2.6)}/>'
    + eye(56, 70, 0.75) + f'<path d="M68 70 q4 -4 8 0" fill="none" {W(2.4)}/>'
    f'<path d="M58 82 Q64 88 70 82" fill="none" {W(2.4)}/>')

I["tvori-vytvoryay-milashenkova"] = ("#E8FBFF", "#5EC4D9",
    "пинцет, держащий кусочек цветной смальты",
    "укладывает последнюю плитку в мозаичную рыбку на столе",
    f'<path d="M86 78 L114 58 V102Z" fill="#FF5C8A" {W(3)}/>'
    f'<ellipse cx="56" cy="80" rx="38" ry="24" fill="#FFB020" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 56 V104" stroke="#fff" stroke-width="2"/>' for x in range(26, 94, 10))
    + "".join(f'<path d="M16 {y} H96" stroke="#fff" stroke-width="2"/>' for y in (68, 80, 92))
    + f'<ellipse cx="56" cy="80" rx="38" ry="24" fill="none" {W(3.2)}/>'
    f'<rect x="56" y="70" width="10" height="10" fill="#E9F7FB"/>'
    + eye(34, 76, 0.7) + f'<path d="M26 88 Q30 92 34 88" fill="none" {W(2.2)}/>'
    f'<path d="M112 8 L64 64 M120 16 L68 68" {W(3.6)}/><path d="M112 8 L120 16" {W(4)}/>'
    f'<rect x="60" y="62" width="10" height="10" rx="2" fill="#3EC1D3" {W(1.8)}/>' + sparkle(24, 30, 5))

I["artroom-kashenkin-lug"] = ("#FFFBEA", "#E9CB6C",
    "скетчбук на металлической пружине",
    "открыт, а из его страницы выпрыгивает нарисованная собачка",
    f'<rect x="14" y="40" width="100" height="70" rx="4" fill="#fff" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="40" r="4" fill="none" stroke="#7C8796" stroke-width="2.6"/>' for x in range(24, 112, 10)) +
    f'<path d="M64 40 V110" stroke="#D0D6DE" stroke-width="2"/>'
    f'<path d="M22 96 Q30 80 40 92 T58 92" fill="none" stroke="#4FA3E0" stroke-width="2.4"/>'
    f'<path d="M74 92 Q76 66 92 62 Q104 58 106 70 Q108 84 96 90 L98 102" fill="#fff" {W(2.6)}/>'
    f'<path d="M92 62 Q86 52 82 58" fill="#C98B4E" {W(2.2)}/><path d="M104 64 Q112 56 110 66" fill="#C98B4E" {W(2.2)}/>'
    + face(96, 74, d=5, k=0.45) + f'<path d="M74 92 l-6 6 M100 100 l6 6" {W(2.4)}/>'
    f'<path d="M8 30 L30 18" stroke="#FF5C8A" stroke-width="5" stroke-linecap="round"/>')

I["eventyon-kuntsevo"] = ("#FFF3EA", "#F2A67A",
    "капкейк в бумажной гофрированной формочке",
    "поднялся шапочкой из детской духовки и машет ложкой крема",
    f'<rect x="16" y="66" width="96" height="58" rx="8" fill="#E6E9F0" {W(3.2)}/><rect x="26" y="76" width="76" height="38" rx="5" fill="#3B3355"/>'
    f'<rect x="26" y="76" width="76" height="38" rx="5" fill="#FF9F40" opacity=".35"/>'
    f'<path d="M44 82 L50 112 H78 L84 82Z" fill="#7FD0F5" {W(2.8)}/>'
    + "".join(f'<path d="M{x} 82 L{x+2} 112" stroke="#4FA3E0" stroke-width="2"/>' for x in (54, 62, 70)) +
    f'<path d="M38 84 Q36 54 64 50 Q92 54 90 84Z" fill="#FFB3D1" {W(3)}/>'
    f'<circle cx="64" cy="46" r="5" fill="#E8434A" {W(2)}/>' + face(64, 70, d=8, k=0.65) +
    f'<path d="M92 66 L110 40" stroke="#9AA5B4" stroke-width="4" stroke-linecap="round"/><ellipse cx="112" cy="36" rx="6" ry="8" fill="#9AA5B4" {W(2)}/>'
    f'<circle cx="24" cy="30" r="6" fill="#fff" opacity=".7"/><circle cx="34" cy="20" r="4" fill="#fff" opacity=".7"/>')

I["bereza-zorge"] = ("#F2FBEA", "#A3D27C",
    "стройная берёзка с серёжками и чёрными чёрточками на коре",
    "в её дупле живёт кисточка, а на ветке висит маленькая картина",
    f'<path d="M-2 112 Q64 104 130 112 V130 H-2Z" fill="#7DBE4E" {W(3)}/>'
    f'<path d="M56 114 L58 20 H70 L72 114Z" fill="#fff" {W(3.2)}/>'
    + "".join(f'<path d="M{x} {y} h6" stroke="{O}" stroke-width="3"/>' for x, y in ((58, 34), (64, 48), (58, 90), (64, 104))) +
    f'<ellipse cx="64" cy="66" rx="5" ry="7" fill="#5A3A24"/><path d="M64 64 L72 52" stroke="#C98B4E" stroke-width="3"/><path d="M72 52 l3 -4" stroke="#FF5C8A" stroke-width="4"/>'
    f'<path d="M62 30 Q40 34 24 26 M66 40 Q90 40 104 32" fill="none" {W(2.6)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="4" fill="#9BD86A" {W(1.6)}/>' for x, y in ((30, 22), (44, 34), (90, 30), (100, 40), (36, 30))) +
    f'<path d="M24 26 V36" stroke="#C9A36A" stroke-width="3"/><path d="M104 32 V40" {W(1.6)}/><rect x="96" y="40" width="18" height="14" fill="#FFE066" {W(2)}/>'
    + face(64, 80, d=4, k=0.4))

I["dom-masterov-mosfilmovskaya"] = ("#FFF4F4", "#E08A8A",
    "серебряный напёрсток с дырочками",
    "стоит на катушке красных ниток, из которой торчит иголка",
    f'<path d="M34 92 H94 V118 H34Z" fill="#E8434A" {W(3.2)}/><rect x="28" y="84" width="72" height="10" rx="3" fill="#C98B4E" {W(2.6)}/>'
    f'<rect x="28" y="116" width="72" height="10" rx="3" fill="#C98B4E" {W(2.6)}/>'
    + "".join(f'<path d="M34 {y} H94" stroke="#B82A33" stroke-width="2"/>' for y in (100, 108)) +
    f'<path d="M42 84 L46 36 Q64 24 82 36 L86 84Z" fill="#C9CED6" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#8A93A0"/>' for x in range(52, 80, 7) for y in (40, 48)) +
    face(64, 66, d=8, k=0.7) +
    f'<path d="M100 96 L118 40" stroke="#9AA5B4" stroke-width="3" stroke-linecap="round"/><ellipse cx="117" cy="44" rx="1.6" ry="3" fill="#fff" {W(1)}/>'
    f'<path d="M117 44 Q108 70 94 104" fill="none" stroke="#E8434A" stroke-width="2"/>')

I["art-start-lavochkina"] = ("#EFF4FF", "#7E9CE8",
    "толстый детский фломастер в низком старте",
    "срывается со стартовой линии и рисует за собой цветную дорожку",
    f'<path d="M14 116 L30 20" stroke="#fff" stroke-width="5" stroke-dasharray="6 5"/>'
    f'<path d="M30 96 Q70 112 122 70" fill="none" stroke="#FF5C8A" stroke-width="8" stroke-linecap="round"/>'
    f'<g transform="rotate(-30 74 58)"><rect x="42" y="44" width="62" height="24" rx="10" fill="#FF5C8A" {W(3)}/>'
    f'<rect x="88" y="44" width="16" height="24" rx="6" fill="#B82A5A" {W(2.4)}/><path d="M42 50 L28 56 L42 62Z" fill="#fff" {W(2.4)}/>'
    + face(66, 56, d=7, k=0.6) + "</g>"
    + "".join(f'<path d="M{x} {y} h-14" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in ((112, 96), (118, 108), (104, 116))))

I["tvori-so-mnoy-rodnikovaya"] = ("#FFF7EE", "#F0B07C",
    "гирлянда бумажных человечков, держащихся за руки",
    "растянулась на подоконнике между горшком с фиалкой и ножницами",
    f'<path d="M-2 98 H130 V130 H-2Z" fill="#fff" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="56" r="8" fill="{c}" {W(2.4)}/><path d="M{x-12} 70 H{x+12} M{x} 64 V84 L{x-8} 98 M{x} 84 L{x+8} 98" stroke="{c}" stroke-width="7" stroke-linecap="round"/><path d="M{x-12} 70 H{x+12} M{x} 64 V84 L{x-8} 98 M{x} 84 L{x+8} 98" {W(2)} fill="none"/>' + face(x, 57, d=3, k=0.3) for x, c in ((26, "#7FD0F5"), (52, "#FFD23F"), (78, "#FF8FB1"), (104, "#9BE07A")))
    + sparkle(20, 24, 4) + sparkle(110, 26, 5))

I["kulibinpro-vdnh"] = ("#FFF9E6", "#E2B84A",
    "катапульта из палочек от мороженого и резинки",
    "запускает пушистый помпон через стол изобретателя",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#9A6A4A" {W(3)}/>'
    f'<rect x="26" y="88" width="56" height="12" rx="3" fill="#F6D58E" {W(2.6)}/><rect x="40" y="76" width="10" height="14" fill="#F6D58E" {W(2.4)}/>'
    f'<path d="M32 88 L96 48" stroke="#F6D58E" stroke-width="9" stroke-linecap="round"/><path d="M32 88 L96 48" {W(2)}/>'
    f'<path d="M42 82 Q46 76 50 80" stroke="#E8434A" stroke-width="3" fill="none"/>'
    f'<ellipse cx="96" cy="46" rx="10" ry="5" fill="#E8434A" {W(2.4)}/>'
    + face(54, 94, d=6, k=0.5) +
    f'<path d="M98 36 Q100 20 112 14" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 5"/>'
    f'<circle cx="114" cy="12" r="8" fill="#7FD0F5" {W(2.2)}/>')

I["cdt-strogino"] = ("#FFEFF6", "#E486AE",
    "бумажный фонарик-гармошка с хвостиком из ленточек",
    "висит под потолком кружка и светится, а под ним сушатся детские рисунки",
    f'<path d="M64 -4 V20" {W(3)}/><rect x="52" y="18" width="24" height="8" rx="2" fill="#E8434A" {W(2.4)}/>'
    f'<path d="M40 30 Q64 22 88 30 L92 70 Q64 80 36 70Z" fill="#FFD23F" {W(3.2)}/>'
    + "".join(f'<path d="M{38+i*0} {y} Q64 {y+6} {90} {y}" fill="none" stroke="#E8A400" stroke-width="2"/>' for i, y in enumerate((40, 50, 60))) +
    face(64, 52, d=8, k=0.65) +
    f'<rect x="52" y="74" width="24" height="6" rx="2" fill="#E8434A" {W(2)}/>'
    + "".join(f'<path d="M{x} 80 Q{x+3} 92 {x-2} 100" stroke="{c}" stroke-width="2.6" fill="none"/>' for x, c in ((56, "#3EA8E8"), (64, "#7A5CFF"), (72, "#5CD65C"))) +
    f'<path d="M-2 100 Q64 110 130 100" fill="none" {W(2)}/>'
    + "".join(f'<rect x="{x}" y="102" width="20" height="16" fill="#fff" {W(2)}/><circle cx="{x+10}" cy="110" r="4" fill="{c}"/>' for x, c in ((10, "#FF8F3C"), (100, "#3EC1D3"))))

I["neotkrytye-ostrova-svobody"] = ("#E8FFFB", "#5CC7B7",
    "лодочка из половинки грецкого ореха с парусом-листиком",
    "плывёт по волнам к неизвестному острову с одной пальмой",
    f'<path d="M-2 82 Q30 74 64 82 T130 80 V130 H-2Z" fill="#3E9AD6" {W(3)}/>'
    f'<path d="M92 80 Q106 64 124 80Z" fill="#F4D58D" {W(2.4)}/><path d="M108 74 V54" stroke="#8A5A2B" stroke-width="3"/>'
    f'<path d="M108 54 q-12 -2 -16 6 M108 54 q12 -2 16 6 M108 54 q-4 -10 -12 -10" fill="none" stroke="#3E9A4A" stroke-width="3"/>'
    f'<path d="M22 84 Q24 108 52 108 Q80 108 82 84Z" fill="#B5793F" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 88 q4 8 0 16" stroke="#8A5A2B" stroke-width="2" fill="none"/>' for x in (36, 52, 68)) +
    f'<path d="M52 84 V36" {W(3)}/><path d="M52 38 Q80 50 52 78Z" fill="#7DCB5A" {W(2.8)}/><path d="M52 42 Q64 58 52 74" stroke="#4E9B3A" stroke-width="2" fill="none"/>'
    + face(52, 96, d=8, k=0.55) + sparkle(24, 30, 5, "#fff"))

I["robbo-turistskaya"] = ("#202B3A", "#0B1018",
    "красный светодиод-человечек с двумя проволочными ножками",
    "воткнут в макетную плату и мигает, когда к нему подключают зелёный проводок",
    f'<rect x="10" y="78" width="108" height="40" rx="5" fill="#F0F2F5" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#9AA5B4"/>' for x in range(18, 114, 8) for y in (88, 96, 104, 110)) +
    f'<path d="M56 74 V92 M72 74 V100" stroke="#9AA5B4" stroke-width="3"/>'
    f'<path d="M48 76 V48 Q48 28 64 28 Q80 28 80 48 V76Z" fill="#FF4D4D" {W(3.2)}/><rect x="44" y="72" width="40" height="8" rx="2" fill="#FF4D4D" {W(2.4)}/>'
    f'<circle cx="64" cy="48" r="38" fill="#FF4D4D" opacity=".18"/>' + face(64, 52, d=7, k=0.65) +
    f'<path d="M14 64 Q30 60 40 86" fill="none" stroke="#3FBF6A" stroke-width="4"/>'
    + sparkle(100, 26, 5, "#FFE066") + sparkle(26, 30, 3, "#FFE066"))

if __name__ == "__main__":
    for pid, (a, b, hero, scene, body) in I.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
