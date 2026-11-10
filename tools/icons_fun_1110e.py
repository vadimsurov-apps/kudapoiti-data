"""Иконки робота fun (2026-11-10, дневной проход): 17 мест из tools/add_fun_1110e.py (детские библиотеки и
геологический музей). Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра.
Запуск: python3 tools/icons_fun_1110e.py"""
import os
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


def openbook(x, y, w, h, cover, page="#FFFDF5", lines=True, tilt=6):
    """раскрытая книга: центр корешка (x, y+h), ширина w, высота страниц h"""
    hw = w / 2
    p = (f'<path d="M{x-hw-3} {y+tilt+3} L{x} {y+h+4} L{x+hw+3} {y+tilt+3} L{x+hw+3} {y+tilt+7} L{x} {y+h+8} L{x-hw-3} {y+tilt+7}Z" fill="{cover}" {W(2.6)}/>'
         f'<path d="M{x} {y+h} Q{x-hw/2} {y+h-6} {x-hw} {y+tilt} L{x-hw} {y+tilt-h+8} Q{x-hw/2} {y-h/2+2} {x} {y+2}Z" fill="{page}" {W(2.4)}/>'
         f'<path d="M{x} {y+h} Q{x+hw/2} {y+h-6} {x+hw} {y+tilt} L{x+hw} {y+tilt-h+8} Q{x+hw/2} {y-h/2+2} {x} {y+2}Z" fill="{page}" {W(2.4)}/>')
    if lines:
        for i in range(3):
            yy = y + 8 + i * (h - 14) / 3
            p += (f'<path d="M{x-hw+6} {yy+tilt-h/2+6} Q{x-hw/2} {yy-2} {x-5} {yy+4}" fill="none" stroke="#B9AFA0" stroke-width="1.8"/>'
                  f'<path d="M{x+5} {yy+4} Q{x+hw/2} {yy-2} {x+hw-6} {yy+tilt-h/2+6}" fill="none" stroke="#B9AFA0" stroke-width="1.8"/>')
    return p


I = {}

# 1. сурикат-часовой на стопке книг
I["lib34-kuryanovskaya"] = ("#FFF4D6", "#E3A94B",
    "сурикат песочного цвета с тёмными кругами вокруг глаз",
    "стоит столбиком на стопке из трёх толстых книг и, держа лапками раскрытую книжку, читает её, как часовой в пустыне",
    f'<path d="M-2 112 Q64 100 130 112 V130 H-2Z" fill="#F2D08A" {W(3)}/>'
    f'<rect x="30" y="98" width="68" height="14" rx="3" fill="#2E6BD6" {W(2.6)}/><path d="M34 102 H94" stroke="#fff" stroke-width="2"/>'
    f'<rect x="36" y="86" width="56" height="12" rx="3" fill="#E8434A" {W(2.6)}/><path d="M40 90 H88" stroke="#FFD6D6" stroke-width="2"/>'
    f'<rect x="33" y="74" width="62" height="12" rx="3" fill="#3FAE5A" {W(2.6)}/><path d="M37 78 H91" stroke="#D6F5DC" stroke-width="2"/>'
    f'<path d="M50 74 Q46 40 56 26 Q64 18 72 26 Q82 40 78 74Z" fill="#D9A866" {W(3)}/>'
    f'<path d="M56 74 Q54 54 64 50 Q74 54 72 74Z" fill="#F3D9A8"/>'
    f'<ellipse cx="64" cy="30" rx="13" ry="12" fill="#D9A866" {W(3)}/>'
    f'<ellipse cx="58" cy="29" rx="4.5" ry="5" fill="#5A3D24"/><ellipse cx="70" cy="29" rx="4.5" ry="5" fill="#5A3D24"/>'
    + eye(58, 29, 0.55) + eye(70, 29, 0.55) +
    f'<ellipse cx="64" cy="36" rx="3" ry="2" fill="#3A2A20"/><path d="M60 39 Q64 42 68 39" fill="none" {W(1.8)}/>'
    f'<circle cx="52" cy="24" r="3" fill="#5A3D24" {W(1.6)}/><circle cx="76" cy="24" r="3" fill="#5A3D24" {W(1.6)}/>'
    + openbook(64, 48, 40, 18, "#9C5BD6", tilt=4)
    + sparkle(106, 34, 6) + sparkle(20, 48, 5))

# 2. муравей тащит книгу больше себя
I["kids-library-domodedovskaya-1"] = ("#E7FAEE", "#5DBE7A",
    "чёрный муравей-силач в красной кепке",
    "в одиночку тащит на поднятых лапках огромную закрытую оранжевую книгу, которая в десять раз больше его",
    f'<path d="M-2 104 Q40 96 130 106 V130 H-2Z" fill="#8FCB6A" {W(3)}/>'
    f'<g transform="rotate(-10 70 50)"><rect x="34" y="22" width="72" height="50" rx="5" fill="#FF8F3C" {W(3.2)}/>'
    f'<rect x="34" y="66" width="72" height="8" rx="2" fill="#FFF6E0" {W(2.4)}/>'
    f'<rect x="40" y="22" width="8" height="50" fill="#E8643A" {W(2)}/>'
    f'<circle cx="76" cy="44" r="12" fill="#FFD84D" {W(2.4)}/>' + face(76, 45, d=6, k=0.45) + '</g>'
    f'<ellipse cx="52" cy="98" rx="11" ry="8" fill="#2B2B2B" {W(2.6)}/><ellipse cx="66" cy="94" rx="7" ry="6" fill="#2B2B2B" {W(2.4)}/>'
    f'<circle cx="78" cy="88" r="8" fill="#2B2B2B" {W(2.6)}/>'
    f'<path d="M72 82 Q78 74 88 80 L90 84 H72Z" fill="#E8434A" {W(2)}/>'
    f'<circle cx="81" cy="87" r="2.6" fill="#fff"/><circle cx="81.6" cy="87.4" r="1.2" fill="#000"/>'
    f'<path d="M80 93 Q83 95 86 92" fill="none" stroke="#fff" stroke-width="1.6"/>'
    f'<path d="M84 82 L96 70" {W(2.4)}/><path d="M70 90 L66 74" {W(2.4)}/><path d="M62 92 L58 76" {W(2.4)}/>'
    f'<path d="M46 104 L40 112 M54 106 L54 114 M64 100 L70 110" {W(2.4)}/>'
    + sparkle(22, 30, 6) + sparkle(112, 98, 5))

# 3. тюлень на льдине
I["lib141-chertanovskaya"] = ("#E6F4FF", "#3F7FC4",
    "белый пушистый тюленёнок-белёк с чёрными глазками-пуговками",
    "лежит на животе на льдине посреди синего моря и, болтая задними ластами, читает раскрытую книжку",
    f'<path d="M-2 86 Q30 80 64 86 Q96 92 130 86 V130 H-2Z" fill="#2F64B0" {W(3)}/>'
    f'<path d="M10 100 Q20 96 30 100 M90 108 Q100 104 110 108" fill="none" stroke="#9CC8E8" stroke-width="2.4"/>'
    f'<path d="M14 92 L110 88 L104 104 L22 106Z" fill="#F2FAFF" {W(3)}/><path d="M22 106 L104 104 L104 98" fill="none" stroke="#B8DDF5" stroke-width="3"/>'
    f'<path d="M28 88 Q24 66 44 62 Q64 58 74 70 L88 84 Q60 94 28 88Z" fill="#fff" {W(3)}/>'
    f'<path d="M30 86 Q16 78 12 66 Q22 70 30 76" fill="#fff" {W(2.6)}/>'
    f'<circle cx="80" cy="66" r="16" fill="#fff" {W(3)}/>'
    + eye(74, 63, 0.75) + eye(86, 63, 0.75) +
    f'<ellipse cx="80" cy="70" rx="3" ry="2.2" fill="#2B2B2B"/><path d="M76 74 Q80 77 84 74" fill="none" {W(1.8)}/>'
    f'<circle cx="69" cy="70" r="2.6" fill="#FF7FA8" opacity=".7"/><circle cx="91" cy="70" r="2.6" fill="#FF7FA8" opacity=".7"/>'
    + openbook(56, 74, 30, 13, "#E8434A", tilt=3)
    + sparkle(28, 30, 7) + sparkle(104, 26, 5))

# 4. фолиант историка Москвы
I["lib206-zabelin-kremenchugskaya"] = ("#FBEFE2", "#A86A3C",
    "старинный толстый фолиант в коричневом кожаном переплёте с медными застёжками",
    "раскрылся на дубовом столе, и со страницы поднимается рисованная красная кремлёвская башня со звездой",
    f'<path d="M-2 100 H130 V130 H-2Z" fill="#7A4E2D" {W(3)}/><path d="M-2 108 H130" stroke="#5E3A20" stroke-width="2"/>'
    f'<path d="M14 96 L64 104 L114 96 L114 102 L64 110 L14 102Z" fill="#6B3F23" {W(3)}/>'
    f'<path d="M64 102 Q40 96 16 96 L16 70 Q40 70 64 78Z" fill="#F7E9C8" {W(2.6)}/>'
    f'<path d="M64 102 Q88 96 112 96 L112 70 Q88 70 64 78Z" fill="#F7E9C8" {W(2.6)}/>'
    f'<path d="M20 98 V104 M108 98 V104" stroke="#E0A800" stroke-width="5" stroke-linecap="round"/>'
    f'<rect x="52" y="44" width="24" height="36" fill="#D9543F" {W(2.8)}/>'
    f'<path d="M48 44 H80 L76 38 H52Z" fill="#B8392A" {W(2.4)}/><rect x="56" y="28" width="16" height="10" fill="#D9543F" {W(2.4)}/>'
    f'<path d="M54 28 L64 8 L74 28Z" fill="#3FAE5A" {W(2.6)}/>'
    f'<path d="M64 0 l2.4 5 5.4 .6 -4 3.6 1.2 5.4 -5 -2.8 -5 2.8 1.2 -5.4 -4 -3.6 5.4 -.6Z" fill="#E8434A" {W(1.6)}/>'
    f'<rect x="58" y="62" width="12" height="18" rx="6" fill="#5A2A1E" {W(2)}/>'
    + face(64, 52, d=7, k=0.5) +
    f'<path d="M24 82 Q36 78 52 84 M76 84 Q92 78 104 82" fill="none" stroke="#B9A57A" stroke-width="1.8"/>'
    + sparkle(22, 40, 6) + sparkle(104, 30, 6))

# 5. хамелеон стал полосатым, как обложка
I["lib130-guryevsky"] = ("#F0FFE0", "#8CC63F",
    "хамелеон с закрученным в спираль хвостом",
    "сидит на ветке и, читая книгу в полосатой сине-жёлтой обложке, сам от увлечения перекрасился в такие же полоски",
    f'<path d="M-4 92 Q40 82 132 88" fill="none" stroke="#7A4E2D" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M-4 92 Q40 82 132 88" fill="none" {W(2)}/>'
    f'<path d="M100 84 Q112 70 104 62 Q96 56 92 64 Q90 72 98 72" fill="none" stroke="#2E6BD6" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M30 84 Q30 60 54 56 Q82 54 98 70 Q100 82 92 86 Z" fill="#2E6BD6" {W(3)}/>'
    f'<clipPath id="ch"><path d="M30 84 Q30 60 54 56 Q82 54 98 70 Q100 82 92 86 Z"/></clipPath>'
    f'<g clip-path="url(#ch)">' + "".join(f'<rect x="{x}" y="50" width="7" height="40" fill="#FFD23F"/>' for x in range(38, 100, 14)) + '</g>'
    f'<path d="M30 84 Q30 60 54 56 Q82 54 98 70 Q100 82 92 86 Z" fill="none" {W(3)}/>'
    f'<path d="M14 66 Q16 48 34 50 Q44 54 42 70 Q30 78 14 66Z" fill="#2E6BD6" {W(3)}/>'
    f'<circle cx="28" cy="58" r="7" fill="#fff" {W(2.2)}/><circle cx="29" cy="58" r="3" fill="#2B2B2B"/>'
    f'<path d="M16 68 Q22 72 30 70" fill="none" {W(2)}/>'
    f'<path d="M44 86 L42 92 M80 86 L82 92" {W(3)}/>'
    f'<g transform="rotate(-8 40 34)"><rect x="22" y="16" width="38" height="30" rx="3" fill="#2E6BD6" {W(2.8)}/>'
    + "".join(f'<rect x="{x}" y="16" width="5" height="30" fill="#FFD23F"/>' for x in (28, 38, 48)) +
    f'<rect x="22" y="16" width="38" height="30" rx="3" fill="none" {W(2.8)}/></g>'
    f'<circle cx="31" cy="68" r="2.4" fill="#FF7FA8" opacity=".8"/>'
    + sparkle(112, 28, 6) + sparkle(84, 18, 4))

# 6. дальневосточный леопард на кедре
I["lib161-ussuriyskaya"] = ("#FFF0DA", "#E07B39",
    "пятнистый детёныш дальневосточного леопарда с длинным пушистым хвостом",
    "развалился на толстой ветке кедра в уссурийской тайге, свесив хвост, и читает книжку, прижав её лапами",
    f'<path d="M-2 116 L18 84 L38 116Z M90 120 L110 80 L130 120Z" fill="#2F6B3F" {W(2.6)}/>'
    f'<path d="M-4 74 Q60 64 132 70" fill="none" stroke="#6B4A2E" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M-4 68 Q60 58 132 64" fill="none" {W(2)}/>'
    f'<path d="M92 68 Q104 86 98 106 Q96 112 102 114" fill="none" stroke="#F2B347" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M92 68 Q104 86 98 106 Q96 112 102 114" fill="none" {W(1.6)}/>'
    f'<path d="M34 64 Q36 46 60 44 Q88 44 96 62 Z" fill="#F2B347" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="none" stroke="#5A3A1E" stroke-width="2.2"/>' for x, y in ((50, 54), (62, 50), (74, 52), (86, 56), (68, 58)))
    + f'<circle cx="32" cy="44" r="16" fill="#F2B347" {W(3)}/>'
    f'<circle cx="20" cy="32" r="5" fill="#F2B347" {W(2.4)}/><circle cx="44" cy="32" r="5" fill="#F2B347" {W(2.4)}/>'
    f'<ellipse cx="32" cy="50" rx="7" ry="5" fill="#FFF3D6"/>'
    + face(32, 44, d=10, k=0.6) +
    f'<circle cx="24" cy="38" r="1.6" fill="#5A3A1E"/><circle cx="40" cy="38" r="1.6" fill="#5A3A1E"/>'
    + openbook(52, 68, 34, 14, "#3FAE5A", tilt=3)
    + sparkle(104, 24, 6) + sparkle(70, 18, 4))

# 7. светлячок светит на страницу ночью
I["lib163-bogdanova"] = ("#3B3F8C", "#141A3D",
    "светлячок с сияющим жёлто-зелёным брюшком-фонариком",
    "ночью в шалаше из одеяла зависает над раскрытой книгой и подсвечивает страницу, чтобы её можно было дочитать",
    f'<path d="M-4 130 L40 40 L64 34 L88 40 L132 130Z" fill="#6A5ACD" {W(3)}/>'
    f'<path d="M40 40 L30 130 M88 40 L98 130" stroke="#584AB8" stroke-width="3"/>'
    f'<circle cx="64" cy="50" r="34" fill="#FFF7A8" opacity=".35"/><circle cx="64" cy="50" r="20" fill="#FFF7A8" opacity=".45"/>'
    + openbook(64, 78, 76, 28, "#E8434A", tilt=6) +
    f'<ellipse cx="54" cy="36" rx="9" ry="6" fill="#C8E6FF" opacity=".9" {W(1.8)}/><ellipse cx="74" cy="36" rx="9" ry="6" fill="#C8E6FF" opacity=".9" {W(1.8)}/>'
    f'<ellipse cx="64" cy="52" rx="9" ry="11" fill="#E4FF5A" {W(2.6)}/>'
    f'<circle cx="64" cy="38" r="9" fill="#3A3A5A" {W(2.6)}/>'
    f'<circle cx="60.5" cy="37" r="2.8" fill="#fff"/><circle cx="67.5" cy="37" r="2.8" fill="#fff"/>'
    f'<circle cx="61" cy="37.4" r="1.3" fill="#000"/><circle cx="68" cy="37.4" r="1.3" fill="#000"/>'
    f'<path d="M61 42 Q64 44 67 42" fill="none" stroke="#fff" stroke-width="1.6"/>'
    f'<path d="M60 30 Q56 22 52 22 M68 30 Q72 22 76 22" fill="none" stroke="#3A3A5A" stroke-width="2"/>'
    + sparkle(18, 30, 4, "#FFF7A8") + sparkle(110, 26, 4, "#FFF7A8") + sparkle(102, 56, 3, "#FFF7A8"))

# 8. ленивец вверх ногами
I["lib58-rimskogo-korsakova"] = ("#E3F7F2", "#4FB09A",
    "серо-бурый ленивец с тёмной маской вокруг глаз и длинными коготками",
    "висит вниз головой на лиане, зацепившись за неё всеми лапами, и неторопливо читает книжку, тоже перевёрнутую вверх ногами",
    f'<path d="M-4 18 Q64 30 132 16" fill="none" stroke="#3E8C3E" stroke-width="7" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y} q6 8 0 14 q-6 -6 0 -14Z" fill="#7BCB6A" {W(1.8)}/>' for x, y in ((14, 18), (104, 20), (118, 16)))
    + f'<path d="M44 26 Q42 40 50 56 M84 26 Q86 40 78 56" fill="none" stroke="#9A8670" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M44 26 Q42 40 50 56 M84 26 Q86 40 78 56" fill="none" {W(1.6)}/>'
    f'<path d="M40 22 l4 6 M44 22 l2 6 M88 22 l-4 6 M84 22 l-2 6" {W(2)}/>'
    f'<ellipse cx="64" cy="62" rx="22" ry="18" fill="#B8A48C" {W(3)}/>'
    f'<circle cx="64" cy="88" r="17" fill="#B8A48C" {W(3)}/><ellipse cx="64" cy="90" rx="12" ry="10" fill="#F2E6D0"/>'
    f'<path d="M52 94 Q56 86 60 92 M68 92 Q72 86 76 94" fill="#5A4636" stroke="#5A4636" stroke-width="5" stroke-linecap="round"/>'
    + eye(57, 92, 0.6) + eye(71, 92, 0.6) +
    f'<ellipse cx="64" cy="98" rx="2.6" ry="1.8" fill="#2B2B2B"/><path d="M60 84 Q64 81 68 84" fill="none" {W(1.8)}/>'
    f'<path d="M48 70 Q40 84 46 100 M80 70 Q88 84 82 100" fill="none" stroke="#9A8670" stroke-width="8" stroke-linecap="round"/>'
    f'<g transform="rotate(180 64 108)">' + openbook(64, 100, 44, 14, "#FF8F3C", tilt=4) + '</g>'
    + sparkle(20, 60, 6) + sparkle(108, 70, 5))

# 9. Пришвин: шмель на клевере
I["lib65-prishvin-severnaya"] = ("#FFF8E0", "#F2C14E",
    "пушистый полосатый шмель в маленьких круглых очках",
    "уселся на розовую головку клевера посреди лесной поляны и, держа крошечную книжку о природе, читает её вслух ромашкам",
    f'<path d="M-2 98 Q64 86 130 98 V130 H-2Z" fill="#7BCB6A" {W(3)}/>'
    f'<path d="M30 130 Q32 100 40 88" fill="none" stroke="#3E8C3E" stroke-width="4"/>'
    + "".join(f'<circle cx="{40+dx}" cy="{80+dy}" r="6" fill="#F27BB0" {W(1.8)}/>' for dx, dy in ((-6, 4), (6, 4), (0, -4), (-8, -6), (8, -6), (0, -14)))
    + "".join(f'<g><circle cx="{x}" cy="{y}" r="7" fill="#fff" {W(1.8)}/><circle cx="{x}" cy="{y}" r="3" fill="#FFC21A"/></g>' for x, y in ((102, 96), (114, 110), (16, 112)))
    + f'<ellipse cx="72" cy="52" rx="16" ry="10" fill="#E6F6FF" opacity=".9" {W(2)} transform="rotate(-20 72 52)"/>'
    f'<ellipse cx="84" cy="56" rx="12" ry="8" fill="#E6F6FF" opacity=".9" {W(2)} transform="rotate(10 84 56)"/>'
    f'<ellipse cx="66" cy="70" rx="24" ry="18" fill="#FFC21A" {W(3)}/>'
    f'<path d="M58 53 Q54 70 58 87 M72 53 Q76 70 72 87" fill="none" stroke="#2B2B2B" stroke-width="7"/>'
    f'<ellipse cx="66" cy="70" rx="24" ry="18" fill="none" {W(3)}/>'
    f'<circle cx="44" cy="64" r="14" fill="#2B2B2B" {W(2.6)}/>'
    f'<circle cx="39" cy="62" r="5" fill="#fff" stroke="#E0A800" stroke-width="2"/><circle cx="50" cy="62" r="5" fill="#fff" stroke="#E0A800" stroke-width="2"/>'
    f'<circle cx="39" cy="62" r="2" fill="#000"/><circle cx="50" cy="62" r="2" fill="#000"/><path d="M44 62 H45" stroke="#E0A800" stroke-width="2"/>'
    f'<path d="M40 70 Q44 73 48 70" fill="none" stroke="#fff" stroke-width="1.8"/>'
    f'<path d="M40 50 Q36 40 30 40 M48 50 Q50 40 56 38" fill="none" {W(2)}/>'
    f'<rect x="22" y="70" width="18" height="14" rx="2" fill="#3FAE5A" {W(2.2)}/><path d="M31 70 V84" {W(1.6)}/>'
    + sparkle(104, 24, 6) + sparkle(20, 34, 5))

# 10. семейное чтение: книга-мама и книжка-малыш
I["lib14-dubininskaya"] = ("#FFE9EE", "#E06A8C",
    "большая книга-мама в бордовой обложке и маленькая книжка-малыш в розовой обложке",
    "идут, держась за руки-закладки, по полу читального зала к креслу для семейного чтения",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#C9A27A" {W(3)}/>'
    + "".join(f'<path d="M{x} 104 V130" stroke="#A9825C" stroke-width="2"/>' for x in range(10, 128, 22))
    + f'<path d="M92 104 V72 Q92 62 104 62 H124 V104" fill="#4FB0C6" {W(3)}/><rect x="88" y="84" width="40" height="14" rx="4" fill="#3E95AA" {W(2.6)}/>'
    f'<rect x="20" y="30" width="44" height="60" rx="4" fill="#9E2A4A" {W(3.2)}/><rect x="58" y="32" width="8" height="56" fill="#FFF6E0" {W(2)}/>'
    f'<path d="M30 30 V20 l4 4 4 -4 V30" fill="#FFC21A" {W(2)}/>'
    + face(42, 56, d=10, k=0.6) +
    f'<path d="M30 90 V102 M50 90 V102" {W(3)}/>'
    f'<rect x="70" y="62" width="22" height="30" rx="3" fill="#FF8FB3" {W(2.8)}/><rect x="88" y="63" width="5" height="28" fill="#FFF6E0" {W(1.8)}/>'
    + face(81, 75, d=6, k=0.42) +
    f'<path d="M76 92 V102 M86 92 V102" {W(2.6)}/>'
    f'<path d="M64 64 Q68 62 70 70" fill="none" stroke="#FFC21A" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(104, 30, 6) + sparkle(76, 22, 5))

# 11. Щукино: читательский формуляр со штампом
I["lib27-bochvara"] = ("#E8F0FF", "#6C8FD8",
    "читательский формуляр — картонная карточка с полосатыми строчками и уголком-кармашком",
    "высовывается из кармашка на обложке синей книги, машет уголком и радостно показывает фиолетовый штамп «выдано»",
    f'<rect x="20" y="40" width="76" height="72" rx="6" fill="#2E6BD6" {W(3.2)}/><rect x="90" y="42" width="10" height="68" fill="#FFF6E0" {W(2.2)}/>'
    f'<path d="M34 76 H86 V108 H34Z" fill="#C9DBFF" {W(2.6)}/>'
    f'<g transform="rotate(-12 60 54)"><rect x="40" y="14" width="48" height="74" rx="3" fill="#FFF6D6" {W(3)}/>'
    + "".join(f'<path d="M46 {y} H82" stroke="#7AA7E8" stroke-width="1.8"/>' for y in (28, 36, 44, 64, 72, 80)) +
    f'<circle cx="74" cy="66" r="9" fill="none" stroke="#8C4FC4" stroke-width="2.6"/><path d="M69 66 l3 3 6 -6" fill="none" stroke="#8C4FC4" stroke-width="2.4"/>'
    + face(58, 52, d=8, k=0.5) + '</g>'
    + sparkle(110, 24, 6) + sparkle(16, 28, 5) + sparkle(112, 100, 4))

# 12. Зеленоград: стеллаж-радуга
I["lib250-zelenograd"] = ("#F5F0FF", "#8C6CD0",
    "высокий книжный стеллаж с корешками книг всех цветов радуги",
    "одна жёлтая книга сама выдвинулась с полки и подмигивает, а на верхней полке стоит горшок с кактусом",
    f'<rect x="22" y="18" width="84" height="104" rx="4" fill="#B07A4A" {W(3.2)}/>'
    + "".join(f'<rect x="28" y="{y}" width="72" height="26" fill="#6B4A2E"/><path d="M26 {y+26} H102" {W(2.6)}/>' for y in (24, 56, 88))
    + "".join(f'<rect x="{x}" y="{y+(26-h)}" width="7" height="{h}" fill="{c}" {W(1.6)}/>'
              for y in (24, 56, 88)
              for x, h, c in ((30, 24, "#E8434A"), (38, 20, "#FF8F3C"), (46, 24, "#3FAE5A"), (54, 22, "#2E6BD6"), (70, 24, "#9C5BD6"), (78, 18, "#E8434A"), (86, 24, "#3FAE5A"), (94, 21, "#FF8F3C"))
              if not (y == 56 and x == 54))
    + f'<rect x="48" y="52" width="26" height="34" rx="2" fill="#FFD23F" {W(2.8)}/>'
    f'<circle cx="56" cy="66" r="2.6" fill="#2B2B2B"/><path d="M64 66 h5" {W(2.4)}/>'
    f'<path d="M56 74 Q61 78 66 74" fill="none" {W(2)}/><circle cx="53" cy="72" r="2.2" fill="#FF7FA8" opacity=".8"/>'
    f'<rect x="80" y="8" width="14" height="10" fill="#E07A4A" {W(2.2)}/><path d="M87 8 V-2 M83 4 H87 M87 0 H91" stroke="#3FAE5A" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(14, 50, 5) + sparkle(116, 60, 5))

# 13. Чехов: рыжая собачка Каштанка
I["chekhov-kids-library"] = ("#FFF1E6", "#D98A4E",
    "рыжая собачка-дворняжка Каштанка с вислыми ушками",
    "сидит на стопке книг, а у ног у неё раскрыта книжка с рассказом про неё саму — она узнала себя на картинке и виляет хвостом",
    f'<path d="M-2 106 H130 V130 H-2Z" fill="#9C6B45" {W(3)}/>'
    f'<rect x="38" y="88" width="56" height="12" rx="3" fill="#2E6BD6" {W(2.6)}/><rect x="34" y="98" width="62" height="12" rx="3" fill="#3FAE5A" {W(2.6)}/>'
    f'<path d="M88 80 Q104 70 102 56" fill="none" stroke="#D2691E" stroke-width="6" stroke-linecap="round"/><path d="M96 66 l6 -2 M98 74 l6 0" {W(1.6)}/>'
    f'<path d="M48 88 Q44 60 64 56 Q86 56 86 88Z" fill="#D2691E" {W(3)}/><path d="M58 88 Q58 72 66 70 Q74 72 74 88Z" fill="#F6C99A"/>'
    f'<circle cx="64" cy="40" r="18" fill="#D2691E" {W(3)}/>'
    f'<path d="M46 32 Q36 40 42 58 Q50 52 50 38Z M82 32 Q92 40 86 58 Q78 52 78 38Z" fill="#8B4513" {W(2.6)}/>'
    f'<ellipse cx="64" cy="48" rx="8" ry="6" fill="#F6C99A"/>'
    + eye(57, 38, 0.7) + eye(71, 38, 0.7) +
    f'<ellipse cx="64" cy="45" rx="3.2" ry="2.4" fill="#2B2B2B"/><path d="M60 50 Q64 54 68 50" fill="none" {W(1.8)}/>'
    f'<path d="M64 52 q2 6 -1 7" fill="#FF7FA8" {W(1.4)}/>'
    + openbook(26, 92, 30, 12, "#E8434A", tilt=3) +
    f'<circle cx="20" cy="88" r="4" fill="#D2691E" {W(1.4)}/>'
    + sparkle(110, 26, 6) + sparkle(20, 30, 5))

# 14. Раменское: верблюжонок с книгами между горбами
I["ramenskoe-kids-library1"] = ("#FFF6D8", "#E8B64C",
    "двугорбый верблюжонок с длинными ресницами",
    "шагает по жёлтым барханам, а в ложбинке между горбами везёт стопку книг, перевязанную бечёвкой",
    f'<path d="M-2 104 Q30 90 64 102 Q98 112 130 98 V130 H-2Z" fill="#F2C36B" {W(3)}/>'
    f'<circle cx="104" cy="28" r="12" fill="#FFE14D" {W(2.4)}/>'
    f'<path d="M30 92 Q28 66 44 64 Q48 48 58 50 Q64 58 70 52 Q80 46 84 62 Q96 64 94 92Z" fill="#C98F55" {W(3)}/>'
    f'<path d="M38 92 V112 M50 92 V112 M78 92 V112 M88 92 V112" stroke="#C98F55" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M38 92 V112 M50 92 V112 M78 92 V112 M88 92 V112" {W(1.4)}/>'
    f'<path d="M92 70 Q102 58 100 40" fill="none" stroke="#C98F55" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M92 70 Q102 58 100 40" fill="none" {W(1.6)}/>'
    f'<ellipse cx="104" cy="36" rx="13" ry="10" fill="#C98F55" {W(2.8)}/>'
    f'<circle cx="106" cy="33" r="2.4" fill="#2B2B2B"/><path d="M103 30 l-2 -3 M106 29 v-3 M109 30 l2 -3" {W(1.4)}/>'
    f'<path d="M110 41 Q113 43 116 40" fill="none" {W(1.8)}/><circle cx="100" cy="40" r="2.2" fill="#FF7FA8" opacity=".8"/>'
    f'<rect x="54" y="46" width="22" height="7" rx="2" fill="#E8434A" {W(2)}/><rect x="52" y="38" width="26" height="8" rx="2" fill="#2E6BD6" {W(2)}/>'
    f'<rect x="56" y="31" width="20" height="7" rx="2" fill="#3FAE5A" {W(2)}/><path d="M66 30 V54" stroke="#8B5A2B" stroke-width="2"/>'
    + sparkle(20, 34, 6) + sparkle(40, 20, 4))

# 15. Жуковский: воздушный шар с корзиной-книгой
I["zhukovsky-kids-library3"] = ("#E0F4FF", "#5AA9E6",
    "полосатый красно-белый воздушный шар",
    "вместо корзины у него раскрытая книга, и он плывёт над аэродромом, где маленький самолёт выруливает на взлётную полосу",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#8FCB6A" {W(3)}/><path d="M-2 116 H130" stroke="#6B6B6B" stroke-width="8"/>'
    f'<path d="M10 116 h10 M34 116 h10 M58 116 h10 M82 116 h10 M106 116 h10" stroke="#fff" stroke-width="2"/>'
    f'<path d="M92 108 h20 l4 -4 h-6 l-4 -6 h-3 l2 6 h-10 l-3 -3 h-3 Z" fill="#fff" {W(1.8)}/>'
    f'<path d="M30 52 Q24 10 64 8 Q104 10 98 52 Q92 70 72 80 H56 Q36 70 30 52Z" fill="#fff" {W(3.2)}/>'
    f'<clipPath id="bal"><path d="M30 52 Q24 10 64 8 Q104 10 98 52 Q92 70 72 80 H56 Q36 70 30 52Z"/></clipPath>'
    f'<g clip-path="url(#bal)"><path d="M40 0 Q34 40 58 84 H46 Q20 40 26 0Z M88 0 Q94 40 70 84 H82 Q108 40 102 0Z" fill="#E8434A"/></g>'
    f'<path d="M30 52 Q24 10 64 8 Q104 10 98 52 Q92 70 72 80 H56 Q36 70 30 52Z" fill="none" {W(3.2)}/>'
    + face(64, 44, d=11, k=0.65) +
    f'<path d="M56 80 L50 88 M72 80 L78 88" {W(2)}/>'
    + openbook(64, 86, 40, 12, "#2E6BD6", tilt=3)
    + sparkle(16, 24, 5) + sparkle(112, 30, 6))

# 16. Наро-Фоминск: комикс
I["naro-fominsk-kids-library"] = ("#FFEFE0", "#F06C4E",
    "толстый комикс в яркой обложке с облачком реплики «!»",
    "выпрыгивает из книжной полки подросткового зала, растопырив страницы-кадры веером, а из облачка вылетает восклицательный знак",
    f'<path d="M-2 100 H130 V130 H-2Z" fill="#3A3F5A" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="104" width="8" height="26" fill="{c}" {W(1.6)}/>' for x, c in ((6, "#4FB0C6"), (16, "#FFC21A"), (26, "#9C5BD6"), (92, "#3FAE5A"), (102, "#E8434A"), (112, "#2E6BD6")))
    + f'<path d="M38 96 L28 40 L64 30 L100 40 L90 96Z" fill="#fff" {W(3)}/>'
    f'<path d="M64 30 V96" {W(2.2)}/>'
    f'<rect x="34" y="44" width="24" height="18" fill="#9CC8E8" {W(1.8)}/><rect x="36" y="66" width="24" height="22" fill="#FFE14D" {W(1.8)}/>'
    f'<rect x="70" y="44" width="24" height="22" fill="#FFB3C6" {W(1.8)}/><rect x="70" y="70" width="22" height="18" fill="#B6E39A" {W(1.8)}/>'
    + face(48, 77, d=8, k=0.5) +
    f'<path d="M74 50 l5 10 l5 -10 l5 10" fill="none" stroke="#E8434A" stroke-width="2.4"/>'
    f'<path d="M86 6 Q118 4 120 22 Q120 36 98 36 L92 44 L92 34 Q80 30 82 20 Q82 8 86 6Z" fill="#fff" {W(2.8)}/>'
    f'<path d="M101 12 V25" stroke="#E8434A" stroke-width="5" stroke-linecap="round"/><circle cx="101" cy="31" r="2.6" fill="#E8434A"/>'
    + sparkle(16, 30, 6) + sparkle(30, 14, 4))

# 17. геологический музей: трилобит
I["geology-museum-vernadsky"] = ("#EEF2F7", "#7C8FA8",
    "древний трилобит с ребристым панцирем из трёх долей",
    "выползает из серой каменной плиты в музейной витрине, отряхивая каменную крошку, а за ним в стекле сверкает друза кварца",
    f'<rect x="-2" y="18" width="132" height="94" fill="#DDE8F2" {W(3)}/>'
    f'<path d="M-2 18 L20 18 L-2 40Z" fill="#fff" opacity=".6"/>'
    f'<path d="M100 76 l6 -22 l5 22Z M108 76 l6 -16 l4 16Z M94 76 l4 -12 l4 12Z" fill="#D7C8F5" {W(2)}/>'
    f'<path d="M-2 112 H130 V130 H-2Z" fill="#6B5A4A" {W(3)}/>'
    f'<path d="M12 104 L20 70 L74 62 L88 100 L60 110Z" fill="#A6A6A6" {W(3)}/>'
    f'<path d="M24 80 L40 76 M30 96 L50 92" stroke="#8A8A8A" stroke-width="2"/>'
    f'<path d="M58 96 Q44 66 60 40 Q70 30 82 40 Q96 66 82 96 Q70 104 58 96Z" fill="#C79A5A" {W(3.2)}/>'
    f'<path d="M66 40 Q62 70 66 98 M74 40 Q78 70 74 98" fill="none" {W(2.2)}/>'
    + "".join(f'<path d="M{54+abs(i-3)*0} {50+i*7} Q70 {46+i*7} {86} {50+i*7}" fill="none" stroke="#8B6A3A" stroke-width="2"/>' for i in range(1, 7))
    + f'<path d="M60 40 Q70 22 80 40 Q70 46 60 40Z" fill="#D9AF6E" {W(2.8)}/>'
    + eye(66, 34, 0.6) + eye(75, 34, 0.6) +
    f'<path d="M67 40 Q70.5 43 74 40" fill="none" {W(1.8)}/>'
    f'<circle cx="46" cy="104" r="2.4" fill="#A6A6A6" {W(1.4)}/><circle cx="96" cy="104" r="2" fill="#A6A6A6" {W(1.4)}/>'
    + sparkle(110, 46, 5) + sparkle(30, 34, 5))

if __name__ == "__main__":
    for pid, (a, b, hero, scene, body) in I.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
