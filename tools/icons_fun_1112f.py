"""Иконки робота fun (2026-11-12, проход f): места из tools/add_fun_1112f.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1112f.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def stars(pts, r=3, c="#fff"):
    return "".join(sparkle(x, y, r, c) for x, y in pts)


def bub(x, y, r):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" fill-opacity=".55" stroke="#FFFFFF" stroke-width="1.6"/>'
            f'<circle cx="{x - r * .35:.1f}" cy="{y - r * .35:.1f}" r="{r * .22:.1f}" fill="#FFFFFF"/>')


# 1. Авиапарк — ложечка-самолётик летит к тарелке
I["chg-aviapark"] = ("#E3F4FF", "#5AA9E6",
    "оранжевая силиконовая детская ложечка с крылышками и хвостиком, как у самолёта",
    "с мордашкой на черпачке летит к белой тарелке на присоске с зелёным горошком и морковным пюре",
    f'<ellipse cx="44" cy="100" rx="34" ry="12" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M44 88 V112 M16 96 L44 100 M72 96 L44 100" stroke="#C9D6E3" stroke-width="2"/>'
    f'<ellipse cx="44" cy="100" rx="34" ry="12" fill="none" {W(3)}/>'
    f'<circle cx="30" cy="96" r="3" fill="#7BC74D"/><circle cx="36" cy="94" r="3" fill="#7BC74D"/><circle cx="32" cy="101" r="3" fill="#7BC74D"/>'
    f'<ellipse cx="58" cy="97" rx="9" ry="4" fill="#FF9F43"/>'
    f'<ellipse cx="44" cy="112" rx="10" ry="3" fill="#9BD3F7" {W(2)}/>'
    f'<path d="M36 50 L84 40" stroke="#FF8A3D" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M36 50 L84 40" fill="none" {W(2)} opacity=".35"/>'
    f'<path d="M50 46 L44 28 L58 30 L62 44Z" fill="#FFB36B" {W(2.6)}/>'
    f'<path d="M54 46 L50 62 L62 60 L64 44Z" fill="#FFB36B" {W(2.6)}/>'
    f'<path d="M36 50 L28 40 L32 54Z" fill="#FFB36B" {W(2.4)}/>'
    f'<ellipse cx="94" cy="38" rx="16" ry="12" fill="#FF8A3D" {W(3)}/>'
    + face(94, 36, d=6, k=.62) +
    f'<path d="M24 60 Q16 62 10 58 M26 66 Q18 70 12 68" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>'
    + stars(((106, 70), (18, 24), (74, 16)), 3.2))

# 2. Афимолл — мочалка-рукавичка в пене
I["chg-afimall"] = ("#F1E6FF", "#9A7BE0",
    "мятная махровая мочалка-рукавичка с большим пальцем",
    "машет «ладошкой» из горы белой пены и пускает мыльные пузыри",
    f'<path d="M14 112 Q20 92 34 96 Q40 82 54 88 Q64 78 76 88 Q90 80 98 94 Q112 92 114 112Z" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M40 96 V48 Q40 36 52 36 H70 Q82 36 82 48 V96Z" fill="#7FE0C6" {W(3.2)}/>'
    f'<path d="M40 64 Q28 62 26 50 Q26 42 34 44 Q40 46 40 54" fill="#7FE0C6" {W(3)}/>'
    + "".join(f'<path d="M{44 + i * 6} 84 v8" stroke="#5BC4AA" stroke-width="1.6"/>' for i in range(7))
    + f'<path d="M40 82 H82" stroke="#FFFFFF" stroke-width="3"/>'
    + face(61, 58, d=8, k=.85) +
    f'<path d="M20 96 Q34 90 44 98 Q56 90 66 98 Q80 90 90 98 Q102 92 110 100" fill="none" stroke="#E7E1F7" stroke-width="3"/>'
    + bub(96, 40, 9) + bub(104, 64, 6) + bub(24, 28, 7) + bub(88, 20, 4)
    + stars(((112, 24),), 3))

# 3. Ереван Плаза — распашонка на пеленальном столике
I["chg-erevan-plaza"] = ("#FFEBDD", "#F29B6B",
    "белая распашонка в голубой горошек с длинными рукавами, завязками и кармашком",
    "разложена на пеленальном столике и машет рукавами, как будто зовёт малыша переодеться",
    f'<rect x="8" y="104" width="112" height="10" rx="4" fill="#FFFFFF" {W(2.8)}/>'
    f'<path d="M18 114 V126 M110 114 V126" {W(3)}/>'
    f'<path d="M46 30 Q64 40 82 30 L104 44 L120 30 L126 44 L100 68 L92 60 V102 H36 V60 L28 68 L2 44 L8 30 L24 44Z" fill="#FFFFFF" {W(3.2)}/>'
    f'<path d="M46 30 Q64 40 82 30" fill="none" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#8CC8F2"/>' for x, y in ((44, 46), (84, 46), (52, 94), (78, 94), (42, 74), (86, 72), (14, 40), (114, 40), (64, 98)))
    + f'<path d="M64 38 V102" stroke="#C9D6E3" stroke-width="2"/>'
    f'<path d="M64 52 Q56 56 54 62 M64 52 Q72 56 74 62" fill="none" stroke="#FF8FB3" stroke-width="2.4"/>'
    + face(64, 72, d=9, k=.8) +
    stars(((20, 18), (108, 16), (112, 88)), 3.2))

# 4. Принц Плаза — мыло-корона
I["chg-princ-plaza"] = ("#D9FFF6", "#3CB8A6",
    "брусок детского мыла кремового цвета в форме короны с тремя зубцами",
    "с мордашкой скользит по мыльной пене, а за ним тянется дорожка из пузырей",
    f'<path d="M0 96 Q20 86 40 94 Q62 84 84 94 Q106 86 128 94 V128 H0Z" fill="#FFFFFF" {W(2.6)}/>'
    f'<path d="M30 92 L26 50 L44 66 L64 40 L84 66 L102 50 L98 92Z" fill="#FFE8A3" {W(3.2)}/>'
    f'<circle cx="26" cy="48" r="5" fill="#FFB3C7" {W(2.2)}/><circle cx="64" cy="38" r="5" fill="#9BD3F7" {W(2.2)}/>'
    f'<circle cx="102" cy="48" r="5" fill="#B9E37A" {W(2.2)}/>'
    + face(64, 74, d=10, k=.85) +
    bub(16, 74, 6) + bub(10, 56, 4) + bub(112, 76, 5) + bub(30, 24, 5)
    + stars(((96, 22), (114, 34)), 3))

# 5. Океания — флакон шампуня «без слёз»
I["chg-okeaniya"] = ("#CDEBFF", "#2F6FCF",
    "голубой флакон детского шампуня в форме капельки с белой крышкой-дозатором",
    "покачивается на волне, а из дозатора поднимаются радужные пузыри",
    f'<path d="M0 98 Q16 88 32 98 T64 98 T96 98 T128 98 V128 H0Z" fill="#7CC6FF" {W(2.6)}/>'
    f'<path d="M0 110 Q16 102 32 110 T64 110 T96 110 T128 110" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>'
    f'<path d="M64 36 Q40 66 42 86 Q44 104 64 104 Q84 104 86 86 Q88 66 64 36Z" fill="#5FB8FF" {W(3.2)}/>'
    f'<rect x="57" y="22" width="14" height="14" rx="3" fill="#FFFFFF" {W(2.6)}/>'
    f'<path d="M71 26 H80" {W(3)}/>'
    f'<rect x="50" y="78" width="28" height="14" rx="4" fill="#FFFFFF" {W(2)}/>'
    f'<path d="M58 85 Q64 81 70 85" fill="none" stroke="#5FB8FF" stroke-width="2"/>'
    + face(64, 66, d=8, k=.75) +
    bub(88, 18, 7) + bub(100, 34, 5) + bub(98, 10, 3) + bub(20, 46, 5)
    + stars(((26, 22),), 3))

# 6. Columbus — грелка-сердечко
I["chg-columbus"] = ("#FFF4E0", "#F2B24C",
    "красная грелка-сердечко с вишнёвыми косточками внутри и строчкой по краю",
    "лежит на мятном пеленальном коврике и греет — от неё поднимаются тёплые волны",
    f'<rect x="8" y="88" width="112" height="28" rx="10" fill="#9EE6CF" {W(3)}/>'
    f'<path d="M14 102 H114" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="5 4"/>'
    f'<path d="M64 100 Q22 76 26 50 Q30 32 48 34 Q60 36 64 48 Q68 36 80 34 Q98 32 102 50 Q106 76 64 100Z" fill="#E8434A" {W(3.2)}/>'
    f'<path d="M64 92 Q30 72 33 52 Q36 41 48 42 Q58 44 64 56 Q70 44 80 42 Q92 41 95 52 Q98 72 64 92Z" fill="none" stroke="#FFFFFF" stroke-width="1.6" stroke-dasharray="3 3"/>'
    + face(64, 64, d=10, k=.9) +
    f'<path d="M40 26 Q36 20 40 14 Q44 8 40 2 M64 24 Q60 18 64 12 Q68 6 64 0 M88 26 Q84 20 88 14 Q92 8 88 2" fill="none" stroke="#FF8A3D" stroke-width="3" stroke-linecap="round"/>'
    + stars(((112, 40), (14, 40)), 3))

# 7. Гагаринский — козырёк для купания как кольцо Сатурна
I["chg-gagarinsky"] = ("#3E4AA0", "#141A4A",
    "голубой мягкий козырёк для купания малышей — кольцо от шампуня",
    "надет на жёлтую планету-мордашку, как кольцо Сатурна, и кружит среди звёзд",
    f'<path d="M14 72 Q64 96 114 72" fill="none" stroke="#7FD3FF" stroke-width="14" stroke-linecap="round"/>'
    f'<circle cx="64" cy="62" r="30" fill="#FFD23F" {W(3.2)}/>'
    f'<path d="M40 50 Q48 46 52 52 M74 82 Q80 76 88 80" fill="none" stroke="#F2A900" stroke-width="2.4"/>'
    + face(64, 60, d=10, k=.9) +
    f'<path d="M14 72 Q64 46 114 72" fill="none" stroke="#7FD3FF" stroke-width="14" stroke-linecap="round" opacity="0"/>'
    f'<path d="M16 70 Q64 92 112 70" fill="none" {W(2)} opacity=".6"/>'
    f'<path d="M16 76 Q64 102 112 76" fill="none" {W(2)} opacity=".6"/>'
    + stars(((20, 26), (104, 24), (28, 104), (100, 104), (64, 16)), 3.4, "#FFF6C4"))

# 8. Город Лефортово — ёршик для бутылочек
I["chg-gorod-lefortovo"] = ("#FFE3EE", "#E46C9A",
    "ёршик для детских бутылочек с жёлтой губкой на конце и сиреневой ручкой",
    "с мордашкой на ручке ныряет в прозрачную бутылочку и отмывает её до блеска, сверху шапка пены",
    f'<path d="M52 118 V60 Q52 50 60 46 H84 Q92 50 92 60 V118Z" fill="#E6F6FF" fill-opacity=".85" {W(3)}/>'
    f'<path d="M58 62 H66 M58 76 H64 M58 90 H66 M58 104 H64" stroke="#9AA3B5" stroke-width="1.8"/>'
    f'<path d="M54 50 Q50 36 64 38 Q70 28 80 36 Q94 34 90 50Z" fill="#FFFFFF" {W(2.6)}/>'
    f'<path d="M72 112 L72 60" stroke="#9AA3B5" stroke-width="3"/>'
    + "".join(f'<path d="M64 {64 + i * 7} L80 {66 + i * 7}" stroke="#FFFFFF" stroke-width="2.4"/>' for i in range(6))
    + f'<ellipse cx="72" cy="112" rx="8" ry="5" fill="#FFD23F" {W(2.4)}/>'
    f'<path d="M58 40 L28 14" stroke="#B48BEA" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M58 40 L28 14" fill="none" {W(2)} opacity=".3"/>'
    f'<circle cx="30" cy="22" r="13" fill="#B48BEA" {W(2.8)}/>'
    + face(30, 22, d=5, k=.5) +
    bub(104, 34, 6) + bub(110, 54, 4) + bub(22, 60, 5)
    + stars(((110, 96), (24, 96)), 3))

# 9. Мозаика — мягкий решётчатый мячик
I["chg-mozaika"] = ("#FFF8C9", "#F2C531",
    "мягкий решётчатый мячик для малышей из разноцветных колечек-сот",
    "с мордашкой в середине катится по пеленальному коврику, за ним — пунктир следа",
    f'<rect x="0" y="100" width="128" height="28" fill="#FFFFFF" fill-opacity=".7"/>'
    f'<path d="M0 100 H128" {W(2.4)}/>'
    f'<circle cx="70" cy="64" r="34" fill="none" {W(3.2)}/>'
    + "".join(f'<circle cx="{70 + dx}" cy="{64 + dy}" r="11" fill="none" stroke="{c}" stroke-width="6"/>'
              for dx, dy, c in ((0, -22, "#E8434A"), (19, -11, "#3F8FE8"), (19, 11, "#7BC74D"), (0, 22, "#FF9F1C"),
                                (-19, 11, "#B48BEA"), (-19, -11, "#2EC4B6")))
    + f'<circle cx="70" cy="64" r="12" fill="#FFE066" {W(2.6)}/>'
    + face(70, 63, d=5, k=.5) +
    f'<path d="M6 106 H26 M30 106 H38" stroke="#C9A227" stroke-width="2.4" stroke-dasharray="4 4"/>'
    + stars(((16, 30), (112, 22), (22, 70)), 3.2))

# 10. Хорошо! — шезлонг для младенца
I["chg-khorosho"] = ("#E4FAD9", "#5DBB63",
    "детский шезлонг-качалка с мягким сиденьем в зелёную полоску и белой дугой-перекладиной",
    "покачивается на изогнутых ножках, на дуге висит игрушка-облачко",
    f'<path d="M18 112 Q64 124 110 112" fill="none" {W(4)}/>'
    f'<path d="M30 112 L42 92 M98 112 L86 92" {W(3.4)}/>'
    f'<path d="M24 60 Q30 96 64 98 Q96 98 108 76 L92 70 Q84 84 64 84 Q42 84 38 58Z" fill="#9EE07A" {W(3.2)}/>'
    + "".join(f'<path d="M{40 + i * 10} {70 + (i % 2) * 2} V{90}" stroke="#FFFFFF" stroke-width="3"/>' for i in range(6))
    + f'<path d="M24 60 Q30 96 64 98 Q96 98 108 76" fill="none" {W(3.2)}/>'
    + face(66, 76, d=9, k=.75) +
    f'<path d="M30 58 Q64 10 104 72" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M30 58 Q64 10 104 72" fill="none" {W(1.6)} opacity=".5"/>'
    f'<path d="M64 34 V44" {W(2)}/>'
    f'<path d="M54 52 Q50 44 58 44 Q60 38 66 40 Q74 38 74 46 Q80 48 76 54Z" fill="#FFFFFF" {W(2.4)}/>'
    + stars(((16, 28), (112, 30)), 3.2))

# 11. Детский Черкизовский парк — клетчатый плед у пруда
I["chg-cherkizovsky-park"] = ("#E7F7EE", "#6FB7A4",
    "вязаное детское одеяльце в красно-белую клетку, сложенное квадратиком",
    "лежит на деревянной скамейке у пруда с камышами и улыбается",
    f'<path d="M0 96 Q64 88 128 96 V128 H0Z" fill="#7CC6FF" {W(2.4)}/>'
    f'<path d="M14 108 Q24 104 34 108 M84 112 Q94 108 104 112" fill="none" stroke="#FFFFFF" stroke-width="2"/>'
    f'<path d="M104 96 V60 M110 96 V66 M116 96 V58" stroke="#5A8F3C" stroke-width="3"/>'
    f'<ellipse cx="104" cy="58" rx="3" ry="8" fill="#8A5A2B"/><ellipse cx="116" cy="56" rx="3" ry="8" fill="#8A5A2B"/>'
    f'<rect x="14" y="76" width="86" height="8" rx="3" fill="#C98B4E" {W(2.6)}/>'
    f'<path d="M22 84 V98 M92 84 V98" {W(3.2)}/>'
    f'<rect x="28" y="42" width="58" height="34" rx="6" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<rect x="{30 + i * 14}" y="44" width="7" height="30" fill="#E8434A" opacity=".75"/>' for i in range(4))
    + "".join(f'<rect x="30" y="{46 + j * 10}" width="54" height="5" fill="#E8434A" opacity=".5"/>' for j in range(3))
    + f'<rect x="28" y="42" width="58" height="34" rx="6" fill="none" {W(3)}/>'
    + face(57, 58, d=8, k=.75) +
    stars(((20, 22), (100, 22)), 3.2))

# 12. Дети Марии — цианотипия
I["fun-deti-marii-dmitrovsky"] = ("#FFF7DE", "#F4C86A",
    "синий лист цианотипии с белым отпечатком листа папоротника",
    "сохнет на верёвочке на деревянных прищепках под ярким солнцем",
    f'<circle cx="104" cy="24" r="14" fill="#FFD23F" {W(2.6)}/>'
    + "".join(f'<path d="M{104 + 20 * c} {24 + 20 * sn} L{104 + 26 * c} {24 + 26 * sn}" stroke="#FF9F1C" stroke-width="2.6" stroke-linecap="round"/>'
              for c, sn in ((-1, 0), (-.7, .7), (0, 1), (-.7, -.7)))
    + f'<path d="M4 34 Q64 46 124 34" fill="none" {W(2.4)}/>'
    f'<rect x="28" y="40" width="64" height="76" rx="3" fill="#1F4FA8" {W(3)}/>'
    f'<g transform="rotate(-20 60 86)"><path d="M60 112 Q56 84 64 58" fill="none" stroke="#FFFFFF" stroke-width="2.6"/>'
    + "".join(f'<ellipse cx="{60 - 6 - (7 - i) * 1.2:.1f}" cy="{104 - i * 6}" rx="{4 + (7 - i) * .9:.1f}" ry="2.4" transform="rotate(-50 {60 - 6 - (7 - i) * 1.2:.1f} {104 - i * 6})" fill="#FFFFFF"/>'
              f'<ellipse cx="{66 + (7 - i) * 1.2:.1f}" cy="{104 - i * 6}" rx="{4 + (7 - i) * .9:.1f}" ry="2.4" transform="rotate(50 {66 + (7 - i) * 1.2:.1f} {104 - i * 6})" fill="#FFFFFF"/>' for i in range(7)) + '</g>'
    + f'<rect x="38" y="34" width="6" height="14" rx="2" fill="#C98B4E" {W(2)}/><rect x="76" y="36" width="6" height="14" rx="2" fill="#C98B4E" {W(2)}/>'
    + face(60, 52, d=7, k=.6)
    + stars(((14, 60), (110, 70), (16, 104)), 3.2))

# 13. Сошью — сантиметровая лента
I["fun-soshyu-krasnobogatyrskaya"] = ("#FFE9F2", "#E8789F",
    "жёлтая портновская сантиметровая лента, свернувшаяся змейкой, с металлическим кончиком",
    "обвивает рулон голубой ткани в горошек и с мордашкой измеряет его",
    f'<rect x="20" y="70" width="88" height="34" rx="17" fill="#8CC8F2" {W(3)}/>'
    + "".join(f'<circle cx="{30 + i * 12}" cy="{80 + (i % 2) * 12}" r="3" fill="#FFFFFF"/>' for i in range(7))
    + f'<ellipse cx="108" cy="87" rx="8" ry="17" fill="#B9DFF7" {W(3)}/>'
    f'<ellipse cx="108" cy="87" rx="3" ry="6" fill="#FFFFFF" {W(1.8)}/>'
    f'<path d="M14 98 Q40 66 64 84 Q88 102 96 70 Q102 44 74 40 Q52 38 52 26" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round"/>'
    f'<path d="M14 98 Q40 66 64 84 Q88 102 96 70 Q102 44 74 40 Q52 38 52 26" fill="none" stroke="#FFD23F" stroke-width="10.4" stroke-linecap="round"/>'
    f'<path d="M14 98 Q40 66 64 84 Q88 102 96 70 Q102 44 74 40 Q52 38 52 26" fill="none" stroke="{O}" stroke-width="3" stroke-dasharray="1 5" opacity=".7"/>'
    f'<rect x="44" y="12" width="16" height="12" rx="2" fill="#C0C7D2" {W(2.4)}/>'
    f'<circle cx="52" cy="40" r="0" fill="none"/>'
    + face(52, 18, d=4, k=.42, blush=False) +
    stars(((20, 24), (108, 26), (112, 54)), 3.2))

# 14. Makeup Kitchen — флакончик блеска для губ
I["fun-makeup-kitchen-avtozavodskaya"] = ("#FFE2F0", "#D9479A",
    "розовый стеклянный флакончик детского блеска для губ с золотой крышечкой-палочкой",
    "приоткрыл крышечку, и из него разлетаются блёстки и маленькие сердечки",
    f'<rect x="44" y="52" width="40" height="62" rx="12" fill="#FF8FC2" {W(3.2)}/>'
    f'<rect x="50" y="58" width="10" height="40" rx="5" fill="#FFFFFF" opacity=".5"/>'
    f'<rect x="54" y="44" width="20" height="10" rx="2" fill="#FFD23F" {W(2.6)}/>'
    f'<path d="M74 28 L96 12" stroke="#FFD23F" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M74 28 L96 12" fill="none" {W(1.8)} opacity=".4"/>'
    f'<ellipse cx="70" cy="34" rx="6" ry="8" transform="rotate(-36 70 34)" fill="#FF5FA8" {W(2.4)}/>'
    + face(64, 84, d=9, k=.85) +
    f'<path d="M28 34 q-4 -6 0 -8 q3 -1 4 3 q1 -4 4 -3 q4 2 0 8 l-4 4z" fill="#FF5FA8" {W(1.6)}/>'
    f'<path d="M100 56 q-4 -6 0 -8 q3 -1 4 3 q1 -4 4 -3 q4 2 0 8 l-4 4z" fill="#FFFFFF" {W(1.6)}/>'
    f'<path d="M22 84 q-3 -5 0 -6 q2 -1 3 2 q1 -3 3 -2 q3 1 0 6 l-3 3z" fill="#FFD23F" {W(1.4)}/>'
    + stars(((44, 22), (106, 34), (108, 86), (26, 60), (60, 18)), 2.6, "#FFF6C4"))

# 15. Шей смелей — джинсовая куртка с нашивками
I["fun-shey-smeley-melnikova"] = ("#E2F0FF", "#4F7FD6",
    "голубая джинсовая куртка с отворотами, медными пуговицами и мордашкой на кармане",
    "к её рукаву иголка с красной ниткой пришивает яркую нашивку-звезду",
    f'<path d="M30 30 L50 22 Q64 30 78 22 L98 30 L112 84 L98 88 L94 60 V112 H34 V60 L30 88 L16 84Z" fill="#6FA3E8" {W(3.2)}/>'
    f'<path d="M50 22 L60 52 L64 112 M78 22 L68 52 L64 112" fill="none" {W(2.4)}/>'
    f'<path d="M50 22 L44 40 L58 46 Z M78 22 L84 40 L70 46Z" fill="#9DC2F2" {W(2.4)}/>'
    f'<circle cx="64" cy="70" r="2.6" fill="#C98B4E" {W(1.4)}/><circle cx="64" cy="88" r="2.6" fill="#C98B4E" {W(1.4)}/>'
    f'<rect x="38" y="62" width="20" height="20" rx="3" fill="#9DC2F2" {W(2.4)}/>'
    + face(48, 70, d=4.4, k=.42) +
    f'<path d="M34 104 H94" stroke="#FFD23F" stroke-width="1.6" stroke-dasharray="3 3"/>'
    f'<path d="M98 50 l3.5 7 7.5 1 -5.5 5 1.5 7.5 -7 -3.5 -7 3.5 1.5 -7.5 -5.5 -5 7.5 -1z" fill="#FFD23F" {W(2)}/>'
    f'<path d="M110 18 L92 44" stroke="#C0C7D2" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M110 18 Q120 30 108 40 Q96 52 104 58" fill="none" stroke="#E8434A" stroke-width="2.4"/>'
    + stars(((18, 22), (22, 104)), 3.2))

# 16. Страна Традиций — соломенная куколка-оберег
I["fun-strana-traditsiy-skobelevskaya"] = ("#FFF1D6", "#D99A4E",
    "золотистая соломенная куколка-оберег с перевязанной красной ниткой талией и косынкой",
    "стоит рядом с пучком соломы и раскинула руки-снопики, приглашая на мастер-класс",
    f'<path d="M0 108 H128 V128 H0Z" fill="#C98B4E" {W(2.4)}/>'
    f'<path d="M64 48 L36 108 H92Z" fill="#F2D27A" {W(3.2)}/>'
    + "".join(f'<path d="M64 52 L{40 + i * 6} 106" stroke="#D9B45A" stroke-width="1.6"/>' for i in range(9))
    + f'<path d="M24 58 H104" stroke="#F2D27A" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M24 58 H104" fill="none" {W(1.6)} opacity=".4"/>'
    f'<path d="M22 54 L16 50 M22 62 L16 66 M106 54 L112 50 M106 62 L112 66" stroke="#D9B45A" stroke-width="2.4"/>'
    f'<path d="M30 54 H34 M94 54 H98 M30 62 H34 M94 62 H98" stroke="#E8434A" stroke-width="2.4"/>'
    f'<path d="M50 76 H78" stroke="#E8434A" stroke-width="4"/>'
    f'<circle cx="64" cy="36" r="15" fill="#F2D27A" {W(3)}/>'
    f'<path d="M48 34 Q64 14 80 34 L84 42 L74 36 Q64 30 54 36 L44 42Z" fill="#E8434A" {W(2.4)}/>'
    + face(64, 40, d=5.5, k=.5) +
    f'<path d="M104 108 L112 76 M108 108 L118 80 M100 108 L104 78" stroke="#D9B45A" stroke-width="3"/>'
    f'<path d="M100 96 H114" stroke="#E8434A" stroke-width="2.4"/>'
    + stars(((20, 26), (108, 22)), 3.2))

# 17. Детская школа дизайна и моды — бумажная выкройка
I["fun-kids-design-school-milyutinsky"] = ("#F3E8FF", "#B07CE0",
    "бумажная выкройка платья с пунктирными линиями и мордашкой",
    "приколота двумя булавками к сиреневой ткани, рядом лежит маленький мелок",
    f'<path d="M6 40 L118 30 L122 118 L10 122Z" fill="#D6B8F5" {W(3)}/>'
    f'<path d="M44 26 L54 32 Q64 38 74 32 L84 26 L96 44 L88 52 L84 48 L94 112 H34 L44 48 L40 52 L32 44Z" fill="#FFF6DD" {W(3)}/>'
    f'<path d="M48 36 L54 38 Q64 44 74 38 L80 36 M40 106 H88" fill="none" stroke="#E8434A" stroke-width="1.8" stroke-dasharray="4 3"/>'
    f'<path d="M64 52 V100" stroke="#3F8FE8" stroke-width="1.6" stroke-dasharray="2 3"/>'
    + face(64, 72, d=8, k=.75) +
    f'<path d="M36 64 L22 50" stroke="#C0C7D2" stroke-width="2.4"/><circle cx="21" cy="49" r="4" fill="#E8434A" {W(1.6)}/>'
    f'<path d="M92 64 L106 50" stroke="#C0C7D2" stroke-width="2.4"/><circle cx="107" cy="49" r="4" fill="#FFD23F" {W(1.6)}/>'
    f'<path d="M96 116 L116 100 L120 108Z" fill="#7FD3FF" {W(2.2)}/>'
    + stars(((18, 18), (110, 16)), 3.2))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
