"""Иконки робота fun (2026-11-10, дневной проход 2): 22 детские библиотеки из tools/add_fun_1110f.py.
Каждая придумана и нарисована отдельно: свой герой (ни разу не встречался в реестре), своя сцена, своя палитра.
Запуск: python3 tools/icons_fun_1110f.py"""
import os
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg, openbook

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def book(x, y, w, h, c, rot=0, spine="#fff"):
    """закрытая книга (вид сбоку): прямоугольник с корешком"""
    return (f'<g transform="rotate({rot} {x+w/2} {y+h/2})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2.5" fill="{c}" {W(2.4)}/>'
            f'<path d="M{x+4} {y+h*0.3} H{x+w-4} M{x+4} {y+h*0.7} H{x+w-4}" stroke="{spine}" stroke-width="1.8" opacity=".8"/></g>')


# 1. Измайлово — бурундук в дупле
I["lib85-izmaylovsky"] = ("#FFF0D8", "#E0863A",
    "полосатый бурундук с набитыми щёчками",
    "высунулся по пояс из дупла старой сосны в осеннем парке и держит в лапках раскрытую книжку, а на краю дупла лежат три жёлудя",
    f'<path d="M30 130 Q36 60 44 -4 H86 Q92 60 98 130Z" fill="#9A5B32" {W(3)}/>'
    f'<path d="M50 20 Q54 60 50 110 M80 14 Q76 70 82 120" fill="none" stroke="#7A4424" stroke-width="2.4"/>'
    f'<ellipse cx="64" cy="70" rx="26" ry="30" fill="#3A2416" {W(3)}/>'
    f'<path d="M44 92 Q42 52 64 44 Q86 52 84 92Z" fill="#D98A45" {W(3)}/>'
    f'<path d="M58 48 Q56 70 58 92 M70 48 Q72 70 70 92" stroke="#5A3420" stroke-width="3" fill="none"/>'
    f'<ellipse cx="64" cy="40" rx="18" ry="15" fill="#D98A45" {W(3)}/>'
    f'<ellipse cx="51" cy="45" rx="8" ry="7" fill="#F2C38E" {W(2.2)}/><ellipse cx="77" cy="45" rx="8" ry="7" fill="#F2C38E" {W(2.2)}/>'
    f'<path d="M64 26 V36" stroke="#5A3420" stroke-width="3"/>'
    f'<circle cx="50" cy="27" r="5" fill="#D98A45" {W(2.2)}/><circle cx="78" cy="27" r="5" fill="#D98A45" {W(2.2)}/>'
    + eye(57, 38, 0.6) + eye(71, 38, 0.6) +
    f'<ellipse cx="64" cy="45" rx="2.6" ry="2" fill="#3A2A20"/>'
    + openbook(64, 64, 40, 18, "#3B7DD8", tilt=4) +
    f'<path d="M36 100 Q64 108 92 100 L92 106 Q64 114 36 106Z" fill="#7A4424" {W(2.4)}/>'
    f'<ellipse cx="44" cy="98" rx="4" ry="5" fill="#B87A3A" {W(1.8)}/><path d="M40 95 Q44 91 48 95" fill="#6B4A2A" {W(1.6)}/>'
    f'<ellipse cx="84" cy="98" rx="4" ry="5" fill="#B87A3A" {W(1.8)}/><path d="M80 95 Q84 91 88 95" fill="#6B4A2A" {W(1.6)}/>'
    f'<path d="M106 30 q6 6 0 12 q-6 -6 0 -12Z" fill="#E8B23A" {W(1.6)}/><path d="M18 60 q6 6 0 12 q-6 -6 0 -12Z" fill="#D2552E" {W(1.6)}/>')

# 2. Новокосино — кашалот
I["lib97-suzdalskaya"] = ("#DDF3FA", "#1E5E8C",
    "серо-синий кашалот с огромной квадратной головой",
    "вынырнул из ночного моря, на лбу у него стоит раскрытая книга, а фонтан из дыхала рассыпается в воздухе буквами А, Б и В",
    f'<path d="M-2 92 Q30 86 64 92 Q98 98 130 90 V130 H-2Z" fill="#164A73" {W(3)}/>'
    f'<path d="M10 104 Q20 100 30 104 M96 112 Q106 108 116 112" fill="none" stroke="#7FC0E0" stroke-width="2.4"/>'
    f'<path d="M14 96 Q14 56 40 54 H92 Q110 56 110 80 Q110 98 92 100 H30 Q14 100 14 96Z" fill="#5E7FA8" {W(3.2)}/>'
    f'<path d="M30 92 Q60 98 100 90" fill="none" stroke="#8FA9CA" stroke-width="3"/>'
    + eye(36, 76, 0.75) +
    f'<ellipse cx="30" cy="84" rx="5" ry="3" fill="#FF7FA8" opacity=".6"/>'
    f'<path d="M18 92 Q28 96 40 92" fill="none" {W(2.4)}/>'
    f'<path d="M110 84 Q122 70 124 60 Q116 70 110 74Z" fill="#5E7FA8" {W(2.6)}/>'
    + openbook(70, 36, 34, 16, "#F2A93B", tilt=4) +
    f'<path d="M98 54 Q96 44 92 38" fill="none" stroke="#BDE6F7" stroke-width="3"/>'
    f'<text x="80" y="28" font-family="Arial" font-weight="bold" font-size="13" fill="#fff" stroke="#173A5A" stroke-width="1">А</text>'
    f'<text x="98" y="22" font-family="Arial" font-weight="bold" font-size="12" fill="#fff" stroke="#173A5A" stroke-width="1">Б</text>'
    f'<text x="108" y="38" font-family="Arial" font-weight="bold" font-size="11" fill="#fff" stroke="#173A5A" stroke-width="1">В</text>')

# 3. Кузьминки — капибара в тёплом источнике
I["cbs1-kids-volgogradsky-91"] = ("#E8FFF4", "#3FB59A",
    "спокойная рыжевато-бурая капибара с мандарином на макушке",
    "по шею сидит в круглой деревянной купели с горячей водой, от которой идёт пар, и читает книгу, положенную на бортик",
    f'<ellipse cx="64" cy="104" rx="52" ry="18" fill="#A8693A" {W(3)}/>'
    f'<path d="M12 104 V122 Q64 140 116 122 V104" fill="#8A5530" {W(3)}/>'
    f'<path d="M30 108 V128 M50 112 V132 M78 112 V132 M98 108 V128" stroke="#6B4022" stroke-width="2"/>'
    f'<ellipse cx="64" cy="102" rx="46" ry="13" fill="#7FD3E8" {W(2.6)}/>'
    f'<path d="M30 60 Q30 30 64 28 Q98 30 98 60 Q98 100 64 100 Q30 100 30 60Z" fill="#B57A48" {W(3.2)}/>'
    f'<rect x="42" y="56" width="44" height="26" rx="12" fill="#9C6538" {W(2.6)}/>'
    f'<ellipse cx="52" cy="64" rx="2.2" ry="3" fill="#3A2416"/><ellipse cx="76" cy="64" rx="2.2" ry="3" fill="#3A2416"/>'
    f'<path d="M56 74 Q64 78 72 74" fill="none" {W(2.2)}/>'
    + eye(48, 46, 0.6) + eye(80, 46, 0.6) +
    f'<ellipse cx="38" cy="32" rx="5" ry="4" fill="#9C6538" {W(2)}/><ellipse cx="90" cy="32" rx="5" ry="4" fill="#9C6538" {W(2)}/>'
    f'<circle cx="64" cy="22" r="9" fill="#FF9A1F" {W(2.6)}/><path d="M64 13 Q68 8 72 10" fill="#3FAE5A" {W(1.8)}/>'
    + book(88, 86, 30, 9, "#E8434A", rot=-8) +
    f'<path d="M20 40 Q16 32 20 24 M108 70 Q104 62 108 54" fill="none" stroke="#fff" stroke-width="3" opacity=".8"/>')

# 4. Толстой — Филипок
I["lib11-tolstoy-novatorov"] = ("#EEF6FF", "#7FA6D6",
    "маленький мальчик Филипок в огромной отцовской шапке, съехавшей на нос",
    "один шагает по сугробам деревенской улицы в школу, прижимая к груди букварь, а за ним тянется цепочка следов",
    f'<path d="M-2 96 Q40 88 70 96 Q100 104 130 94 V130 H-2Z" fill="#FFFFFF" {W(3)}/>'
    f'<ellipse cx="22" cy="110" rx="5" ry="2.4" fill="#C9D8EA"/><ellipse cx="34" cy="104" rx="5" ry="2.4" fill="#C9D8EA"/>'
    f'<ellipse cx="18" cy="98" rx="5" ry="2.4" fill="#C9D8EA"/>'
    f'<path d="M48 64 Q44 96 46 104 H82 Q84 96 80 64Z" fill="#8B5A2E" {W(3)}/>'
    f'<path d="M64 64 V104" stroke="#5E3A1A" stroke-width="2"/><path d="M46 92 H82" stroke="#C1272D" stroke-width="4"/>'
    f'<rect x="50" y="104" width="12" height="10" rx="3" fill="#5E3A1A" {W(2.4)}/><rect x="68" y="104" width="12" height="10" rx="3" fill="#5E3A1A" {W(2.4)}/>'
    f'<circle cx="64" cy="52" r="14" fill="#FFD9B8" {W(3)}/>'
    + eye(58, 54, 0.6) + eye(70, 54, 0.6) +
    f'<path d="M60 60 Q64 63 68 60" fill="none" {W(1.8)}/>'
    f'<path d="M34 46 Q30 62 36 70 Q44 64 42 50Z M94 46 Q98 62 92 70 Q84 64 86 50Z" fill="#B88A5A" {W(2.6)}/>'
    f'<path d="M32 48 Q34 18 64 16 Q94 18 96 48 Q80 42 64 46 Q48 42 32 48Z" fill="#6B4022" {W(3)}/>'
    f'<path d="M30 48 Q64 38 98 48 Q98 54 94 54 Q64 46 34 54 Q30 54 30 48Z" fill="#C89A6A" {W(2.6)}/>'
    f'<rect x="54" y="72" width="22" height="16" rx="2" fill="#E8B23A" {W(2.4)}/>'
    f'<text x="58" y="85" font-family="Arial" font-weight="bold" font-size="11" fill="#5A3A10">АБ</text>'
    f'<circle cx="104" cy="28" r="2.4" fill="#fff"/><circle cx="20" cy="36" r="2" fill="#fff"/><circle cx="110" cy="62" r="2.4" fill="#fff"/>'
    f'<circle cx="16" cy="70" r="2" fill="#fff"/>')

# 5. Весенняя ул. — синица на ветке с почками
I["lib117-vesennyaya"] = ("#F6FFE0", "#9CCB4A",
    "синица-лазоревка с голубой шапочкой и жёлтым брюшком",
    "сидит на весенней ветке с набухшими почками, придерживая лапкой крошечную раскрытую книжку, и звонко читает её вслух",
    f'<path d="M-2 92 Q40 84 80 88 Q110 92 130 80" fill="none" stroke="#6B4A2A" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M28 88 Q24 76 30 70 M98 86 Q104 74 98 68" fill="none" stroke="#6B4A2A" stroke-width="4" stroke-linecap="round"/>'
    f'<ellipse cx="30" cy="68" rx="5" ry="7" fill="#7ACB4A" {W(2)}/><ellipse cx="98" cy="66" rx="5" ry="7" fill="#7ACB4A" {W(2)}/>'
    f'<ellipse cx="14" cy="88" rx="4" ry="6" fill="#7ACB4A" {W(2)}/>'
    f'<path d="M84 64 L112 72 L106 80Z" fill="#3D6FB8" {W(2.6)}/>'
    f'<ellipse cx="64" cy="64" rx="26" ry="22" fill="#FFD43B" {W(3.2)}/>'
    f'<path d="M80 50 Q96 60 88 80 Q76 76 72 64Z" fill="#4A88D6" {W(2.6)}/>'
    f'<circle cx="54" cy="40" r="17" fill="#fff" {W(3)}/>'
    f'<path d="M38 36 Q52 18 70 34 Q54 30 38 36Z" fill="#3D8BE0" {W(2.4)}/>'
    f'<path d="M40 44 Q50 48 62 44" stroke="#1E3A6A" stroke-width="3" fill="none"/>'
    + eye(50, 38, 0.6) +
    f'<path d="M36 42 L28 44 L36 47Z" fill="#3A3A3A" {W(1.8)}/>'
    f'<path d="M54 86 V94 M66 86 V94" {W(2.4)}/>'
    + openbook(34, 60, 22, 10, "#E8434A", lines=False, tilt=2) +
    f'<path d="M24 26 q4 -6 8 0 M14 34 q4 -6 8 0" fill="none" {W(2)}/>' + sparkle(108, 30, 6))

# 6. Кассиль — телескоп и выдуманная страна
I["lib22-kassil-leningradskoe"] = ("#5A4A9E", "#1C1446",
    "медный телескоп на трёх деревянных ножках",
    "смотрит в ночное небо, где вместо луны висит книжка-остров с маленьким замком на страницах, а вокруг мерцают звёзды",
    f'<path d="M-2 110 Q64 100 130 110 V130 H-2Z" fill="#2E2468" {W(3)}/>'
    f'<path d="M36 114 L50 84 L64 114 M50 84 L50 116" fill="none" stroke="#8A5A2E" stroke-width="4.5" stroke-linecap="round"/>'
    f'<g transform="rotate(-34 50 80)"><rect x="18" y="70" width="64" height="20" rx="6" fill="#D8A04A" {W(3)}/>'
    f'<rect x="78" y="66" width="12" height="28" rx="3" fill="#B87A2A" {W(2.6)}/><rect x="10" y="74" width="10" height="12" rx="2" fill="#B87A2A" {W(2.4)}/></g>'
    + eye(44, 80, 0.55) + eye(55, 73, 0.55) +
    f'<path d="M46 88 Q52 88 56 82" fill="none" {W(1.8)}/>'
    + openbook(92, 34, 40, 16, "#3FAE8A", tilt=3) +
    f'<path d="M84 34 V24 H88 V20 H92 V24 H96 V34Z" fill="#E8434A" {W(1.8)}/><path d="M90 20 V14 L96 16 L90 18" fill="#FFD84D" {W(1.2)}/>'
    + sparkle(22, 22, 5) + sparkle(64, 16, 4) + sparkle(112, 66, 5) + sparkle(30, 48, 3) + sparkle(116, 16, 3))

# 7. ул. Степана Супруна — аксолотль в аквариуме
I["lib32-supruna"] = ("#E0FBFF", "#3FC1C9",
    "розовый аксолотль с пушистыми жабрами-веточками по бокам головы",
    "лежит на дне аквариума среди камушков и водорослей и листает размокшую книжку, а вверх поднимаются пузырьки",
    f'<path d="M-2 104 Q64 96 130 104 V130 H-2Z" fill="#E8D7A8" {W(3)}/>'
    f'<circle cx="20" cy="106" r="5" fill="#9AA8B8" {W(2)}/><circle cx="108" cy="108" r="6" fill="#B8A8C8" {W(2)}/>'
    f'<path d="M14 104 Q8 80 18 60 Q22 80 20 104 M114 104 Q120 84 112 70 Q108 86 110 104" fill="#3FAE5A" {W(2.4)}/>'
    f'<path d="M78 94 Q110 92 118 76 Q104 82 86 84Z" fill="#FFB0C8" {W(2.6)}/>'
    f'<ellipse cx="64" cy="88" rx="24" ry="12" fill="#FFB0C8" {W(3)}/>'
    f'<ellipse cx="54" cy="58" rx="26" ry="20" fill="#FFB0C8" {W(3.2)}/>'
    f'<path d="M30 48 Q18 40 16 30 M30 56 Q14 54 10 46 M32 64 Q18 68 14 62" fill="none" stroke="#E8437A" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M78 48 Q90 40 92 30 M78 56 Q94 54 98 46 M76 64 Q90 68 94 62" fill="none" stroke="#E8437A" stroke-width="4" stroke-linecap="round"/>'
    + eye(46, 54, 0.6) + eye(62, 54, 0.6) +
    f'<path d="M46 66 Q54 72 62 66" fill="none" {W(2.2)}/>'
    + book(40, 92, 30, 10, "#3B7DD8", rot=-4) +
    f'<circle cx="74" cy="30" r="4" fill="none" stroke="#fff" stroke-width="2.2"/><circle cx="82" cy="18" r="3" fill="none" stroke="#fff" stroke-width="2"/>'
    f'<circle cx="68" cy="14" r="2.4" fill="none" stroke="#fff" stroke-width="1.8"/>')

# 8. Куусинена — броненосец-«конверт»
I["lib43-kuusinena"] = ("#FFF1EA", "#E07A5F",
    "броненосец с полосатым панцирем-гармошкой",
    "свернулся полукольцом вокруг толстой книги, как обложка, и выглядывает из-за её верхнего края на песчаной дюне",
    f'<path d="M-2 100 Q50 88 130 100 V130 H-2Z" fill="#F2C890" {W(3)}/>'
    f'<path d="M30 98 Q14 70 34 42 Q50 26 72 30 Q100 36 104 68 Q106 92 90 100 Q86 74 78 60 L74 96 Q60 104 30 98Z" fill="#A89488" {W(3.2)}/>'
    + "".join(f'<path d="M{40+i*10} {34+abs(i-2)*2} Q{46+i*9} {66} {42+i*10} {98-abs(i-2)*2}" fill="none" stroke="#7A6458" stroke-width="2.4"/>' for i in range(5)) +
    f'<path d="M70 30 Q78 14 92 20 Q98 28 90 36 Q80 40 70 30Z" fill="#C8B4A6" {W(2.8)}/>'
    f'<path d="M80 18 L78 8 L84 16 M88 18 L92 10 L92 20" fill="#C8B4A6" {W(2)}/>'
    + eye(84, 26, 0.55) +
    f'<ellipse cx="96" cy="29" rx="2.4" ry="1.8" fill="#3A2A20"/>'
    f'<g transform="rotate(-8 64 76)"><rect x="40" y="50" width="44" height="54" rx="3" fill="#2E8FBF" {W(3.2)}/>'
    f'<rect x="40" y="50" width="9" height="54" fill="#1F6E99" {W(2)}/>'
    f'<circle cx="68" cy="74" r="10" fill="#FFD84D" {W(2.2)}/></g>'
    f'<ellipse cx="38" cy="80" rx="7" ry="5" fill="#C8B4A6" {W(2.2)}/><ellipse cx="92" cy="76" rx="7" ry="5" fill="#C8B4A6" {W(2.2)}/>'
    + sparkle(112, 44, 5) + sparkle(18, 30, 5))

# 9. Народного Ополчения — лемур вниз головой на хвосте
I["lib98-narodnogo-opolcheniya"] = ("#F3EAFF", "#9B7FD4",
    "кольцехвостый лемур с огромными оранжевыми глазами",
    "обвил чёрно-белым полосатым хвостом горизонтальную ветку и висит вниз головой, держа обеими лапами книгу тоже вверх тормашками",
    f'<path d="M-2 18 Q64 10 130 20" fill="none" stroke="#6B4A2A" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M100 18 Q98 8 108 4 M30 14 Q26 4 34 0" fill="none" stroke="#6B4A2A" stroke-width="4"/>'
    f'<ellipse cx="108" cy="6" rx="7" ry="4" fill="#3FAE5A" {W(1.8)}/>'
    + "".join(f'<path d="M{70+i*0} {20+i*7} h0" />' for i in range(1)) +
    f'<path d="M64 20 Q76 22 78 34 Q80 46 70 52" fill="none" stroke="#2B2B2B" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M64 20 Q76 22 78 34 Q80 46 70 52" fill="none" stroke="#fff" stroke-width="9" stroke-dasharray="6 6" stroke-linecap="butt"/>'
    f'<ellipse cx="62" cy="68" rx="16" ry="20" fill="#B8B0B8" {W(3)}/>'
    f'<path d="M50 60 Q36 66 36 80 M74 60 Q90 66 90 80" fill="none" stroke="#B8B0B8" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M50 60 Q36 66 36 80 M74 60 Q90 66 90 80" fill="none" stroke="{O}" stroke-width="1"/>'
    + book(32, 78, 62, 10, "#E8434A", rot=180) +
    f'<path d="M62 92 Q46 96 44 112 Q52 124 62 124 Q72 124 80 112 Q78 96 62 92Z" fill="#fff" {W(3)}/>'
    f'<path d="M48 110 Q62 102 76 110 Q70 122 62 122 Q54 122 48 110Z" fill="#2B2B2B"/>'
    f'<circle cx="54" cy="110" r="5.5" fill="#FF9A1F" {W(1.8)}/><circle cx="70" cy="110" r="5.5" fill="#FF9A1F" {W(1.8)}/>'
    f'<circle cx="54" cy="110" r="2.4" fill="#000"/><circle cx="70" cy="110" r="2.4" fill="#000"/>'
    f'<circle cx="53" cy="109" r=".9" fill="#fff"/><circle cx="69" cy="109" r=".9" fill="#fff"/>'
    f'<path d="M58 100 Q62 96 66 100" fill="none" {W(1.8)}/>'
    f'<path d="M42 100 L36 92 L46 96 M82 100 L88 92 L78 96" fill="#B8B0B8" {W(2)}/>' + sparkle(108, 64, 6) + sparkle(18, 54, 5))

# 10. Краснобогатырская — петух-богатырь
I["lib57-krasnobogatyrskaya"] = ("#FFE9D6", "#E8553A",
    "рыжий петух в остроконечном богатырском шлеме",
    "стоит на камне-распутье, раскрыв перед собой большую книгу былин, и уверенно ведёт крылом по строчке",
    f'<path d="M-2 108 Q64 98 130 108 V130 H-2Z" fill="#8FCB6A" {W(3)}/>'
    f'<path d="M30 112 Q32 94 52 92 H76 Q96 94 98 112Z" fill="#A6A6A6" {W(3)}/>'
    f'<path d="M48 92 V86 M60 92 V86" {W(2.6)}/>'
    f'<path d="M80 74 Q104 60 104 36 Q94 48 86 46 Q100 30 96 18 Q86 34 78 40Z" fill="#2E7D4A" {W(2.6)}/>'
    f'<path d="M86 50 Q96 34 104 34 Q96 50 86 60Z" fill="#1F5FAF" {W(2.2)}/>'
    f'<ellipse cx="62" cy="68" rx="24" ry="20" fill="#E8742A" {W(3.2)}/>'
    f'<path d="M48 40 Q46 62 54 72 Q66 78 70 62 Q72 44 62 36Z" fill="#E8742A" {W(3)}/>'
    f'<circle cx="56" cy="38" r="13" fill="#F28C3A" {W(3)}/>'
    f'<path d="M44 34 Q44 18 56 14 Q68 18 68 34Z" fill="#B8C4D0" {W(2.6)}/><path d="M56 14 V4" stroke="#B8C4D0" stroke-width="3"/>'
    f'<path d="M44 34 H68" {W(2.4)}/>'
    + eye(52, 40, 0.55) +
    f'<path d="M42 42 L32 45 L42 48Z" fill="#FFC23A" {W(2)}/>'
    f'<path d="M44 50 Q40 58 46 60 Q50 56 48 50Z" fill="#E8203A" {W(1.8)}/>'
    + openbook(46, 74, 36, 14, "#8B3A1A", tilt=3))

# 11. Байкальская — глухарь на пне
I["lib71-baykalskaya"] = ("#E6F2E6", "#2F6B45",
    "чёрный глухарь с красными бровями и веером хвоста",
    "распустил хвост веером на таёжном пне и, вытянув шею, токует над раскрытой книгой, лежащей на мху",
    f'<path d="M14 18 L24 -2 L34 18 L28 18 L36 34 L12 34 L20 18Z" fill="#1F5A36" {W(2.2)}/>'
    f'<path d="M98 26 L108 6 L118 26 L112 26 L120 42 L96 42 L104 26Z" fill="#1F5A36" {W(2.2)}/>'
    f'<path d="M30 118 V96 Q64 88 98 96 V118Z" fill="#8A5530" {W(3)}/><ellipse cx="64" cy="96" rx="34" ry="8" fill="#C89A64" {W(2.6)}/>'
    f'<path d="M-2 118 Q64 108 130 118 V130 H-2Z" fill="#5E9E4A" {W(3)}/>'
    f'<path d="M40 76 Q20 50 30 26 Q44 42 46 62 Q50 36 64 28 Q66 50 58 70Z" fill="#2B2B2B" {W(2.6)}/>'
    + "".join(f'<path d="M{40+i*4} {72} L{24+i*8} {34+abs(i-2)*4}" stroke="#555" stroke-width="1.6"/>' for i in range(5)) +
    f'<ellipse cx="66" cy="78" rx="22" ry="14" fill="#3A3A40" {W(3)}/>'
    f'<path d="M78 72 Q84 50 92 44" fill="none" stroke="#3A3A40" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M78 72 Q84 50 92 44" fill="none" stroke="#2F7A5A" stroke-width="3"/>'
    f'<circle cx="94" cy="40" r="10" fill="#3A3A40" {W(2.8)}/>'
    f'<path d="M88 33 Q94 28 100 33" fill="none" stroke="#E8203A" stroke-width="3.4"/>'
    + eye(95, 38, 0.5) +
    f'<path d="M103 40 L110 44 L102 46Z" fill="#F2E3C0" {W(1.8)}/>'
    + openbook(90, 82, 26, 10, "#E8B23A", lines=False, tilt=2) + sparkle(64, 14, 5))

# 12. Сторожевая — морская свинка в книжном домике
I["lib72-storozhevaya"] = ("#FFF3EC", "#F2A07A",
    "рыже-белая морская свинка с хохолком-розеткой на макушке",
    "выглядывает из круглого окошка домика, сложенного из толстых книг, как из сторожевой будки, а над окошком висит колокольчик",
    f'<path d="M-2 110 Q64 102 130 110 V130 H-2Z" fill="#E6C29A" {W(3)}/>'
    + book(24, 96, 80, 14, "#3B7DD8") + book(28, 82, 72, 14, "#3FAE5A") + book(24, 68, 80, 14, "#9C5BD6")
    + book(28, 54, 72, 14, "#E8B23A") +
    f'<path d="M18 56 L64 22 L110 56Z" fill="#E8434A" {W(3)}/>'
    f'<path d="M64 22 V30" stroke="#8A5A1A" stroke-width="2"/><path d="M58 34 Q64 26 70 34 Z" fill="#FFD84D" {W(1.8)}/>'
    f'<circle cx="64" cy="80" r="20" fill="#5A3A2A" {W(3)}/>'
    f'<ellipse cx="64" cy="84" rx="17" ry="14" fill="#E8913A" {W(2.6)}/>'
    f'<path d="M56 74 Q64 84 72 74 L74 98 H54Z" fill="#fff"/>'
    f'<path d="M58 70 L64 64 L70 70 L64 74Z" fill="#E8913A" {W(1.8)}/>'
    + eye(57, 82, 0.55) + eye(71, 82, 0.55) +
    f'<ellipse cx="64" cy="89" rx="2.4" ry="1.8" fill="#C8507A"/><path d="M60 92 Q64 95 68 92" fill="none" {W(1.6)}/>'
    f'<ellipse cx="48" cy="76" rx="4" ry="3" fill="#E8913A" {W(1.8)}/><ellipse cx="80" cy="76" rx="4" ry="3" fill="#E8913A" {W(1.8)}/>')

# 13. Шатурская — гепард-спринтер
I["lib77-shaturskaya"] = ("#FFFBE0", "#F2C23A",
    "пятнистый гепард с чёрными «слёзными» полосками у глаз",
    "мчится в длинном прыжке по саванне, и раскрытая книга в его лапах трепещет страницами от встречного ветра",
    f'<path d="M-2 108 Q64 100 130 108 V130 H-2Z" fill="#D8B060" {W(3)}/>'
    f'<path d="M8 50 H30 M4 64 H22 M10 78 H28" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M18 74 Q4 66 0 50" fill="none" stroke="#E8B03A" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M24 76 Q30 56 60 56 Q84 56 92 68 Q86 84 60 84 Q36 86 24 76Z" fill="#F2BE4A" {W(3)}/>'
    f'<path d="M30 80 L18 98 M42 82 L40 100 M76 80 L92 96 M84 76 L104 88" stroke="#F2BE4A" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M30 80 L18 98 M42 82 L40 100 M76 80 L92 96 M84 76 L104 88" stroke="{O}" stroke-width="1" fill="none"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#3A2A20"/>' for x, y in [(36, 66), (46, 62), (56, 70), (66, 62), (74, 72), (50, 76), (40, 74)]) +
    f'<circle cx="98" cy="58" r="14" fill="#F2BE4A" {W(3)}/>'
    f'<circle cx="90" cy="46" r="4" fill="#F2BE4A" {W(2)}/><circle cx="106" cy="46" r="4" fill="#F2BE4A" {W(2)}/>'
    + eye(93, 56, 0.55) + eye(104, 56, 0.55) +
    f'<path d="M93 61 Q91 66 92 70 M104 61 Q106 66 105 70" stroke="#2B2B2B" stroke-width="2" fill="none"/>'
    f'<ellipse cx="99" cy="64" rx="2.4" ry="1.8" fill="#2B2B2B"/>'
    + openbook(106, 82, 26, 10, "#3B7DD8", lines=False, tilt=6) +
    f'<path d="M114 76 Q122 72 124 66 M110 74 Q116 66 116 60" fill="none" stroke="#fff" stroke-width="2"/>')

# 14. Шолохов — малыш-горилла с книгой-подушкой
I["lib80-sholokhov"] = ("#E4F1F2", "#5B8C93",
    "малыш-горилла с серебристой шёрсткой на макушке",
    "сидит, обхватив огромную зелёную книгу, как подушку, и, положив на неё подбородок, задумчиво читает строчку на обложке",
    f'<path d="M-2 106 Q64 98 130 106 V130 H-2Z" fill="#7FB07A" {W(3)}/>'
    f'<ellipse cx="64" cy="66" rx="34" ry="34" fill="#3A3A42" {W(3.2)}/>'
    f'<path d="M44 36 Q64 26 84 36" fill="none" stroke="#B8BCC8" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="54" rx="20" ry="16" fill="#7A6A64" {W(2.6)}/>'
    + eye(56, 50, 0.6) + eye(72, 50, 0.6) +
    f'<ellipse cx="60" cy="58" rx="1.8" ry="1.4" fill="#2B2B2B"/><ellipse cx="68" cy="58" rx="1.8" ry="1.4" fill="#2B2B2B"/>'
    f'<path d="M58 63 Q64 66 70 63" fill="none" {W(1.8)}/>'
    f'<circle cx="30" cy="54" r="6" fill="#3A3A42" {W(2.4)}/><circle cx="98" cy="54" r="6" fill="#3A3A42" {W(2.4)}/>'
    f'<rect x="28" y="70" width="72" height="38" rx="6" fill="#2E9E5A" {W(3.2)}/>'
    f'<rect x="28" y="100" width="72" height="8" rx="2" fill="#FFF6E0" {W(2.2)}/>'
    f'<path d="M40 82 H88 M40 90 H76" stroke="#CFEFD8" stroke-width="2.6"/>'
    f'<ellipse cx="30" cy="80" rx="9" ry="7" fill="#3A3A42" {W(2.6)}/><ellipse cx="98" cy="80" rx="9" ry="7" fill="#3A3A42" {W(2.6)}/>'
    + sparkle(110, 26, 6) + sparkle(18, 30, 4))

# 15. Алтуфьевское — тапир листает носом
I["lib91-altufyevskoe"] = ("#EAFBEA", "#4FAF6A",
    "чёрно-белый малайский тапир с подвижным хоботком",
    "стоит в джунглях у плоского камня и переворачивает страницу раскрытой книги кончиком хоботка",
    f'<path d="M-2 104 Q64 96 130 104 V130 H-2Z" fill="#3E8A4A" {W(3)}/>'
    f'<path d="M110 20 Q96 30 92 46 Q108 40 118 26Z M10 30 Q26 34 30 50 Q14 46 6 36Z" fill="#2E7D3A" {W(2.4)}/>'
    f'<path d="M62 104 L66 86 H118 L114 104Z" fill="#9AA0A6" {W(3)}/>'
    + openbook(92, 72, 40, 14, "#D24A8A", tilt=3) +
    f'<path d="M12 70 Q12 44 40 44 Q60 44 62 62 Q62 84 40 86 Q16 88 12 70Z" fill="#2B2B30" {W(3)}/>'
    f'<path d="M14 62 Q34 54 52 62 Q52 80 34 84 Q16 82 14 62Z" fill="#F2F2F2" {W(2.4)}/>'
    f'<path d="M20 86 V100 M34 88 V102 M46 86 V100" stroke="#2B2B30" stroke-width="7" stroke-linecap="round"/>'
    f'<circle cx="62" cy="54" r="13" fill="#2B2B30" {W(3)}/>'
    f'<path d="M72 56 Q84 56 86 66 Q86 72 82 72" fill="none" stroke="#2B2B30" stroke-width="8" stroke-linecap="round"/>'
    f'<ellipse cx="54" cy="42" rx="4" ry="5" fill="#2B2B30" {W(2)}/><ellipse cx="54" cy="42" rx="1.6" ry="2.4" fill="#fff"/>'
    + eye(64, 52, 0.55) + sparkle(100, 30, 5))

# 16. Жуковский, ул. Гудкова — ехидна с книгами на колючках
I["zhukovsky-kids-library4"] = ("#E8FBF8", "#5BC2B2",
    "колючая ехидна с длинным тонким носиком",
    "бежит по тропинке, нанизав на свои иголки три маленькие разноцветные книжки, — несёт их домой почитать",
    f'<path d="M-2 104 Q64 96 130 104 V130 H-2Z" fill="#B8D88A" {W(3)}/>'
    f'<path d="M24 96 Q20 60 58 52 Q96 50 104 86 Q104 98 96 100 H30Z" fill="#6B4A32" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} L{x+dx} {y-18}" stroke="#F2E6CF" stroke-width="3.4" stroke-linecap="round"/><path d="M{x} {y} L{x+dx} {y-18}" stroke="{O}" stroke-width=".8"/>'
              for x, y, dx in [(32, 72, -8), (40, 62, -4), (52, 56, 0), (66, 54, 4), (78, 58, 8), (90, 66, 12), (98, 78, 14), (46, 76, -4), (70, 70, 4)]) +
    book(22, 40, 18, 12, "#E8434A", rot=-30) + book(54, 26, 18, 12, "#3B7DD8", rot=0) + book(88, 36, 18, 12, "#E8B23A", rot=30) +
    f'<path d="M100 84 Q114 84 124 90" fill="none" stroke="#5A3A24" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="96" cy="86" rx="12" ry="10" fill="#8A6A50" {W(2.6)}/>'
    + eye(98, 83, 0.5) +
    f'<path d="M34 100 L30 108 M52 100 L52 108 M78 100 L80 108" stroke="#5A3A24" stroke-width="5" stroke-linecap="round"/>')

# 17. Жуковский, ул. Макаревского — муравьед на пне
I["zhukovsky-kids-library6"] = ("#FFF6E8", "#D8A26A",
    "рыжевато-серый муравьед с длинной трубочкой-мордой и пушистым хвостом-веником",
    "сидит на пне, накрывшись хвостом, как пледом, и аккуратно переворачивает кончиком морды страницу книги на коленях",
    f'<path d="M-2 110 Q64 102 130 110 V130 H-2Z" fill="#9CC86A" {W(3)}/>'
    f'<path d="M34 116 V94 H94 V116Z" fill="#A8693A" {W(3)}/><ellipse cx="64" cy="94" rx="30" ry="7" fill="#E0B07A" {W(2.4)}/>'
    f'<path d="M30 94 Q6 70 20 34 Q34 20 42 40 Q34 64 48 88Z" fill="#7A6A5A" {W(3)}/>'
    + "".join(f'<path d="M{20+i*5} {44+i*9} q-6 -2 -10 2" fill="none" stroke="#5A4A3A" stroke-width="1.8"/>' for i in range(5)) +
    f'<ellipse cx="62" cy="72" rx="20" ry="22" fill="#B89A7A" {W(3)}/>'
    f'<path d="M48 60 L70 86" stroke="#2B2B2B" stroke-width="8"/><path d="M50 58 L72 84" stroke="#F2E6CF" stroke-width="3"/>'
    f'<ellipse cx="66" cy="44" rx="12" ry="11" fill="#B89A7A" {W(3)}/>'
    f'<path d="M74 46 Q92 52 100 72" fill="none" stroke="#B89A7A" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M74 46 Q92 52 100 72" fill="none" stroke="{O}" stroke-width="1"/>'
    f'<circle cx="60" cy="34" r="4" fill="#B89A7A" {W(2)}/>'
    + eye(66, 42, 0.5) +
    openbook(84, 78, 34, 12, "#2E8FBF", tilt=3) + sparkle(110, 30, 5))

# 18. Клин — Щелкунчик
I["klin-kids-library-krasnaya"] = ("#FFE6EC", "#A8213A",
    "деревянный Щелкунчик в красном мундире и высоком чёрном кивере",
    "стоит навытяжку у нарядной ёлки и вместо ореха держит в челюстях раскрытую нотную книжку, а с веток свисают стеклянные шары",
    f'<path d="M86 8 L120 66 H104 L124 104 H74 L96 66 H80Z" fill="#2E8A4A" {W(2.6)}/>'
    f'<circle cx="94" cy="60" r="4" fill="#FFD84D" {W(1.6)}/><circle cx="108" cy="88" r="4" fill="#3B9BE0" {W(1.6)}/><circle cx="86" cy="94" r="3.4" fill="#fff" {W(1.4)}/>'
    f'<path d="M-2 114 Q64 108 130 114 V130 H-2Z" fill="#FFFFFF" {W(3)}/>'
    f'<rect x="38" y="64" width="34" height="32" rx="4" fill="#D8202E" {W(3)}/>'
    f'<path d="M55 64 V96" stroke="#FFD84D" stroke-width="2.4"/><circle cx="55" cy="72" r="1.8" fill="#FFD84D"/><circle cx="55" cy="82" r="1.8" fill="#FFD84D"/>'
    f'<rect x="40" y="96" width="12" height="18" fill="#1E3A8A" {W(2.4)}/><rect x="58" y="96" width="12" height="18" fill="#1E3A8A" {W(2.4)}/>'
    f'<rect x="38" y="110" width="15" height="6" rx="2" fill="#2B2B2B" {W(1.8)}/><rect x="57" y="110" width="15" height="6" rx="2" fill="#2B2B2B" {W(1.8)}/>'
    f'<rect x="42" y="36" width="26" height="28" rx="5" fill="#FFD9B8" {W(3)}/>'
    f'<rect x="40" y="10" width="30" height="26" rx="3" fill="#1A1A1A" {W(2.8)}/><path d="M40 30 H70" stroke="#FFD84D" stroke-width="3"/>'
    f'<path d="M50 10 L55 2 L60 10" fill="#E8203A" {W(1.8)}/>'
    + eye(50, 44, 0.5) + eye(60, 44, 0.5) +
    f'<path d="M42 54 H68" stroke="#fff" stroke-width="5"/><path d="M44 54 V60 M50 54 V60 M56 54 V60 M62 54 V60" stroke="#999" stroke-width="1"/>'
    + openbook(55, 56, 26, 8, "#2B2B2B", lines=False, tilt=2) +
    f'<path d="M30 70 Q26 82 32 90" fill="none" stroke="#D8202E" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M80 70 Q84 80 78 88" fill="none" stroke="#D8202E" stroke-width="7" stroke-linecap="round"/>'
    + sparkle(18, 30, 5) + sparkle(24, 60, 3))

# 19. Руза — вомбат в норке
I["ruza-kids-library"] = ("#EAF4FF", "#7A5A3A",
    "коренастый вомбат-квадратик с маленькими круглыми ушками",
    "устроился в своей подземной норе под корнями дерева, под крышей из травы, и читает при свете гриба-светлячка",
    f'<rect x="-2" y="-2" width="132" height="40" fill="#BFE3FF"/>'
    f'<path d="M-2 36 Q64 28 130 38 V130 H-2Z" fill="#8A6040" {W(3)}/>'
    f'<path d="M-2 36 Q64 28 130 38" fill="none" stroke="#5EAF4A" stroke-width="6"/>'
    f'<path d="M64 34 Q60 46 50 54 M64 34 Q70 48 82 52" fill="none" stroke="#5A3A20" stroke-width="3.4"/>'
    f'<path d="M64 34 V18" stroke="#5A3A20" stroke-width="5"/><circle cx="64" cy="10" r="12" fill="#5EAF4A" {W(2.4)}/>'
    f'<ellipse cx="64" cy="86" rx="50" ry="34" fill="#4A3020" {W(3)}/>'
    f'<rect x="34" y="66" width="52" height="46" rx="20" fill="#8E8478" {W(3.2)}/>'
    f'<circle cx="38" cy="66" r="6" fill="#8E8478" {W(2.4)}/><circle cx="82" cy="66" r="6" fill="#8E8478" {W(2.4)}/>'
    f'<ellipse cx="60" cy="86" rx="10" ry="7" fill="#7A5A3A" {W(2.2)}/>'
    + eye(50, 78, 0.55) + eye(70, 78, 0.55) +
    f'<path d="M51 82 Q60 76 69 82 Q66 89 60 89 Q54 89 51 82Z" fill="#2B2B2B"/>'
    + openbook(60, 96, 34, 12, "#E8434A", lines=False, tilt=3) +
    f'<path d="M98 112 V96" stroke="#F2E6CF" stroke-width="4"/><path d="M88 98 Q98 82 108 98Z" fill="#FFE04A" {W(2.4)}/>'
    f'<circle cx="98" cy="92" r="14" fill="#FFF3A0" opacity=".35"/>')

# 20. Дубна, Большая Волга — ламантин
I["dubna-kids-library-volga"] = ("#E2F6F0", "#3A8FA0",
    "серый ламантин с круглым хвостом-веслом и усатой мордочкой",
    "дрейфует на спине по широкой реке, положив раскрытую книгу на живот, а рядом медленно проплывает кувшинка",
    f'<path d="M-2 66 Q64 58 130 66 V130 H-2Z" fill="#4AA6B8" {W(3)}/>'
    f'<path d="M-2 40 Q30 34 64 38 Q100 42 130 36 V66 Q64 58 -2 66Z" fill="#9CCB6A" {W(2.4)}/>'
    f'<path d="M14 84 Q22 80 30 84 M98 104 Q106 100 114 104 M44 112 Q52 108 60 112" fill="none" stroke="#BDEAF2" stroke-width="2.4"/>'
    f'<path d="M22 86 Q20 70 50 68 H90 Q106 70 104 86 Q102 100 84 100 H40 Q22 100 22 86Z" fill="#8C96A0" {W(3.2)}/>'
    f'<path d="M104 84 Q118 72 124 80 Q122 96 104 92Z" fill="#8C96A0" {W(2.8)}/>'
    f'<circle cx="26" cy="80" r="13" fill="#9AA4AE" {W(3)}/>'
    f'<ellipse cx="22" cy="86" rx="7" ry="5" fill="#B8C0C8" {W(2)}/>'
    f'<path d="M16 84 l-6 -2 M16 88 l-6 2 M28 84 l6 -2" stroke="#2B2B2B" stroke-width="1.4"/>'
    + eye(24, 76, 0.5) +
    openbook(64, 54, 34, 14, "#E8742A", tilt=3) +
    f'<ellipse cx="98" cy="116" rx="12" ry="5" fill="#3FAE5A" {W(2.2)}/><path d="M94 112 Q98 102 102 112Z" fill="#FFB0C8" {W(1.8)}/>'
    + sparkle(110, 22, 5))

# 21. Сходня — хомяк набил щёки книжками
I["skhodnya-kids-library"] = ("#FFEFF5", "#E87AA8",
    "золотистый хомячок с огромными раздутыми щеками",
    "сидит в своей кучке опилок и запихивает за щёку уже третью крошечную книжку, а за другой щекой выпирают ещё две",
    f'<path d="M-2 104 Q64 92 130 104 V130 H-2Z" fill="#F2DDA8" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} l6 -2" stroke="#C8A86A" stroke-width="2"/>' for x, y in [(14, 112), (30, 106), (90, 110), (106, 104), (60, 118)]) +
    f'<ellipse cx="64" cy="82" rx="30" ry="24" fill="#E8B060" {W(3)}/>'
    f'<ellipse cx="64" cy="90" rx="18" ry="14" fill="#FFF1D8"/>'
    f'<ellipse cx="36" cy="58" rx="20" ry="18" fill="#F2C27A" {W(3)}/><ellipse cx="92" cy="58" rx="20" ry="18" fill="#F2C27A" {W(3)}/>'
    f'<rect x="84" y="50" width="12" height="9" rx="1.6" fill="#3B7DD8" opacity=".55" {W(1.4)}/><rect x="90" y="60" width="12" height="9" rx="1.6" fill="#3FAE5A" opacity=".55" {W(1.4)}/>'
    f'<ellipse cx="64" cy="50" rx="20" ry="18" fill="#E8B060" {W(3)}/>'
    f'<circle cx="48" cy="32" r="6" fill="#E8B060" {W(2.2)}/><circle cx="80" cy="32" r="6" fill="#E8B060" {W(2.2)}/>'
    f'<circle cx="48" cy="32" r="3" fill="#FFB0C8"/><circle cx="80" cy="32" r="3" fill="#FFB0C8"/>'
    + eye(57, 46, 0.55) + eye(71, 46, 0.55) +
    f'<ellipse cx="64" cy="54" rx="2.4" ry="1.8" fill="#C8507A"/>'
    + book(24, 52, 16, 11, "#E8434A", rot=-20) +
    f'<ellipse cx="34" cy="66" rx="5" ry="4" fill="#FFD9B8" {W(1.8)}/>'
    + sparkle(110, 28, 6) + sparkle(16, 28, 4))

# 22. Воскресенск — игуана загорает на книгах
I["voskresensk-central-kids-library"] = ("#FFF3D6", "#F28C28",
    "зелёная игуана с гребнем из шипов вдоль спины и мешочком под подбородком",
    "загорает, растянувшись на стопке книг под настольной лампой, как под солнцем, и читает верхнюю книжку, подперев голову лапой",
    f'<path d="M-2 112 Q64 104 130 112 V130 H-2Z" fill="#C8763A" {W(3)}/>'
    f'<path d="M96 112 V40 Q96 26 84 22" fill="none" stroke="#3A3A42" stroke-width="5"/>'
    f'<path d="M66 18 Q84 6 98 22 L82 36Z" fill="#E8434A" {W(2.6)}/>'
    f'<path d="M80 34 L56 70 L104 70Z" fill="#FFF6B0" opacity=".45"/>'
    f'<rect x="86" y="108" width="22" height="6" rx="2" fill="#3A3A42"/>'
    + book(10, 96, 76, 14, "#2E8FBF") + book(14, 84, 70, 12, "#9C5BD6") +
    f'<path d="M20 80 Q12 74 4 80 Q12 86 20 84" fill="#5EB84A" {W(2.4)}/>'
    f'<path d="M18 82 Q30 64 56 66 Q76 68 80 80 Q60 88 18 82Z" fill="#6CC24A" {W(3)}/>'
    + "".join(f'<path d="M{30+i*8} {70-i*0.4} l3 -8 l3 8" fill="#3E8A2E" {W(1.4)}/>' for i in range(5)) +
    f'<ellipse cx="80" cy="70" rx="12" ry="9" fill="#6CC24A" {W(2.8)}/>'
    f'<path d="M74 78 Q76 90 84 84" fill="#A8E07A" {W(2)}/>'
    + eye(84, 67, 0.5) +
    f'<path d="M52 80 L54 90 M66 82 L66 90" stroke="#5EB84A" stroke-width="5" stroke-linecap="round"/>'
    + openbook(44, 66, 20, 7, "#E8B23A", lines=False, tilt=2) + sparkle(116, 50, 5))

if __name__ == "__main__":
    for pid, v in I.items():
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
