"""Иконки робота fun (2026-11-09, ночь, поиск по районам): 28 мест. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности). Сверено со всеми листами icons-catalog (01–43) и icons-src/subjects.txt.
Заняты и НЕ брать: мозаика, гуашь, мелок, свистулька, гирлянда-человечки, непроливайка, тюбик, бюст, качели-гнездо,
носорог, одуванчик, водомерка, головастик, кувшинка, лоскутное одеяло, ткацкий станок, микрофон, программка,
люстра, фрисби, калейдоскоп, клубок со спицами, фломастеры-человечки, ёжик, скамейка.
Запуск: python3 tools/icons_fun_1109.py [id ...]  (печатает строки для subjects.txt)"""
import os, sys
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
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


def kid(cx, cy, k=1.0, hair="#6B3F23", skin="#FFD9B8"):
    r = 13 * k
    return (f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="{skin}" {W(2.8)}/>'
            f'<path d="M{cx-r:.1f} {cy-2*k:.1f} Q{cx-r:.1f} {cy-r-3*k:.1f} {cx:.1f} {cy-r-2*k:.1f} '
            f'Q{cx+r:.1f} {cy-r-3*k:.1f} {cx+r:.1f} {cy-2*k:.1f} Q{cx+4*k:.1f} {cy-9*k:.1f} {cx-r:.1f} {cy-2*k:.1f}Z" '
            f'fill="{hair}" {W(2.4)}/>'
            + face(cx, cy + 2 * k, d=5 * k, k=0.5 * k))


I = {}

# 1. Клаускидс — сортер-домик
I["klauskids-rassvet"] = ("#FFF0D0", "#F7A54A",
    "розовый пластмассовый сортер-домик с фигурными окошками",
    "малыш просовывает жёлтую звёздочку в окошко-звезду на крыше под рассветным солнцем",
    f'<circle cx="100" cy="30" r="12" fill="#FFD84A" {W(2.4)}/>'
    f'<path d="M24 62 L64 28 L104 62Z" fill="#F0507A" {W(3.2)}/>'
    f'<rect x="30" y="60" width="68" height="52" rx="6" fill="#FF8FB4" {W(3.2)}/>'
    f'<circle cx="46" cy="96" r="7" fill="#5B3C7A" {W(2.4)}/>'
    f'<rect x="76" y="89" width="13" height="13" fill="#5B3C7A" {W(2.4)}/>'
    f'<path d="M64 38 l3 7 7 0 -6 5 2 7 -6 -4 -6 4 2 -7 -6 -5 7 0Z" fill="#5B3C7A" {W(2)}/>'
    + f(64, 74, d=10, k=0.85) +
    f'<path d="M78 24 l4 9 10 1 -8 6 3 10 -9 -5 -9 5 3 -10 -8 -6 10 -1Z" fill="#FFD84A" {W(2.4)}/>'
    f'<path d="M92 44 Q100 50 108 48" fill="none" {W(2.6)}/><circle cx="110" cy="47" r="5" fill="#FFD9B8" {W(2.4)}/>')

# 2. Чемодан — дорожный чемодан-сцена
I["teatr-chemodan-voykovskaya"] = ("#F3E6FF", "#8C5BD6",
    "потёртый коричневый дорожный чемодан с наклейками",
    "крышка распахнута как сцена: внутри красные шторки, а на краю стоит картонная луна на палочке",
    f'<rect x="20" y="22" width="88" height="40" rx="6" fill="#A0663C" {W(3.2)}/>'
    f'<path d="M24 26 Q38 40 24 58 M104 26 Q90 40 104 58" fill="#E2483F" {W(2.6)}/>'
    f'<path d="M58 30 Q66 36 60 48 Q74 46 74 34 Q70 28 58 30Z" fill="#FFE27A" {W(2.4)}/>'
    f'<path d="M66 46 V60" {W(2.6)}/>'
    f'<rect x="16" y="62" width="96" height="50" rx="8" fill="#B87443" {W(3.2)}/>'
    f'<rect x="52" y="58" width="24" height="7" rx="3" fill="#5A3A22" {W(2.4)}/>'
    f'<circle cx="32" cy="98" r="8" fill="#6CC0F2" {W(2.2)}/><rect x="86" y="72" width="16" height="11" rx="2" fill="#FFD84A" {W(2.2)}/>'
    + f(64, 86, d=11, k=0.9) +
    sparkle(30, 40, 3, "#FFF3D6") + sparkle(96, 40, 3, "#FFF3D6"))

# 3. Иголочка — игольница-помидор
I["igolochka-yuzhnobutovskaya"] = ("#E4FFF2", "#4DBE8E",
    "игольница-помидор с разноцветными булавками",
    "иголка с красной ниткой выводит над ней петельку-сердечко на швейном столе",
    f'<rect x="0" y="100" width="128" height="30" fill="#E8C79A" {W(2.4)}/>'
    f'<ellipse cx="62" cy="76" rx="38" ry="30" fill="#EE3E3A" {W(3.2)}/>'
    f'<path d="M62 46 Q60 76 62 106 M34 60 Q48 76 34 96 M90 60 Q76 76 90 96" fill="none" {W(2)}/>'
    f'<path d="M50 48 L62 40 L74 48 L66 50 L62 44 L58 50Z" fill="#4CB050" {W(2.4)}/>'
    f'<path d="M40 54 L30 36 M84 52 L92 34 M56 50 L52 32" {W(2.4)}/>'
    f'<circle cx="30" cy="34" r="4" fill="#FFD84A" {W(2)}/><circle cx="93" cy="32" r="4" fill="#6CC0F2" {W(2)}/><circle cx="52" cy="30" r="4" fill="#B48CF0" {W(2)}/>'
    + f(62, 76, d=12, k=0.9) +
    f'<path d="M100 20 L84 46" stroke="#C9CDD8" stroke-width="3.4" stroke-linecap="round"/>'
    f'<path d="M84 46 Q76 56 92 60 Q108 62 106 48 Q104 38 96 44" fill="none" stroke="#E8304A" stroke-width="2.4"/>')

# 4. Дети Райка — девочка в бумажной короне читает стихи на табуретке
I["deti-rayka-butovo"] = ("#FFE9E0", "#E76F51",
    "девочка в бумажной золотой короне и красном плаще",
    "стоит на табуретке и с выражением читает стихи, раскинув руку, как на сцене",
    f'<rect x="44" y="96" width="40" height="8" rx="2" fill="#C88A4E" {W(2.8)}/>'
    f'<path d="M50 104 L46 126 M78 104 L82 126" {W(4)}/>'
    f'<path d="M46 96 Q44 60 64 56 Q84 60 82 96Z" fill="#D62E3A" {W(3)}/>'
    f'<path d="M58 62 L56 92 L72 92 L70 62Z" fill="#7FD0F5" {W(2.4)}/>'
    f'<path d="M78 66 Q96 54 104 40" fill="none" {W(3)}/><circle cx="105" cy="38" r="5" fill="#FFD9B8" {W(2.4)}/>'
    + kid(64, 42, k=1.15, hair="#B0602A") +
    f'<path d="M50 30 L52 18 L58 25 L64 14 L70 25 L76 18 L78 30Z" fill="#FFD23F" {W(2.6)}/>'
    + sparkle(22, 30, 4, "#fff") + sparkle(108, 70, 3, "#FFF3D6"))

# 5. ЦДТ Свиблово — карандашница
I["cdt-sviblovo-amundsena"] = ("#E8F4FF", "#5E8FE0",
    "бумажный стаканчик-карандашница с мордашкой",
    "держит букет цветных карандашей и кисточку на столе кружка, рядом лежит вырезанная звёздочка",
    f'<rect x="0" y="104" width="128" height="30" fill="#F2D7A6" {W(2.4)}/>'
    + "".join(f'<path d="M{x} {y} L{x+dx} {y-44} L{x+dx+4} {y-50} L{x+dx+8} {y-44}" fill="{c}" {W(2.4)}/>'
              for x, y, dx, c in [(40, 60, -8, "#F25C54"), (52, 58, -2, "#FFD23F"), (66, 58, 2, "#58C26B"), (80, 60, 8, "#B48CF0")]) +
    f'<path d="M92 60 L104 22" {W(3.4)}/><path d="M100 20 Q106 10 110 18 Q108 26 102 26Z" fill="#6B3F23" {W(2.2)}/>'
    f'<path d="M34 56 H96 L90 110 H40Z" fill="#FFE27A" {W(3.2)}/>'
    f'<path d="M36 70 H94 M38 96 H92" stroke="#F7A54A" stroke-width="5"/>'
    + f(65, 84, d=11, k=0.9) +
    f'<path d="M18 112 l3 6 7 1 -5 5 1 7 -6 -3 -6 3 1 -7 -5 -5 7 -1Z" fill="#FF8FB4" {W(2)}/>')

# 6. Клёвый — шалаш из пледа
I["klevy-klub-yasenevo"] = ("#2E3A78", "#151C45",
    "шалаш-крепость из клетчатого пледа и диванных подушек",
    "из щели между подушками выглядывает малыш с фонариком, луч рисует звёздочку на стене",
    f'<path d="M14 112 L64 30 L114 112Z" fill="#F0A13A" {W(3.2)}/>'
    f'<path d="M30 86 L98 86 M22 100 L106 100 M50 50 L78 50 M40 66 L88 66" stroke="#D2452F" stroke-width="4"/>'
    f'<path d="M48 112 L64 70 L80 112Z" fill="#1B1F3B" {W(2.8)}/>'
    + kid(64, 94, k=0.85) +
    f'<rect x="8" y="104" width="30" height="16" rx="6" fill="#7CC3F0" {W(2.6)}/><rect x="90" y="104" width="30" height="16" rx="6" fill="#8BD47A" {W(2.6)}/>'
    f'<path d="M72 98 L106 52 L114 64Z" fill="#FFF3A6" opacity=".55"/>'
    f'<path d="M110 40 l3 6 7 1 -5 5 1 7 -6 -3 -6 3 1 -7 -5 -5 7 -1Z" fill="#FFE27A"/>'
    + sparkle(24, 30, 3, "#fff") + sparkle(98, 24, 2.4, "#fff"))

# 7. Учим рисовать — ластик
I["uchim-risovat-snezhnaya"] = ("#FFF7DA", "#F2C94C",
    "розовый школьный ластик с синим кончиком",
    "старательно стирает лишнюю каракулю на детском рисунке солнышка",
    f'<rect x="12" y="20" width="104" height="94" rx="4" fill="#FFFFFF" {W(3)}/>'
    f'<circle cx="40" cy="48" r="13" fill="#FFD23F" {W(2.4)}/>'
    + "".join(f'<path d="M{40+19*c} {48+19*s_} L{40+26*c} {48+26*s_}" stroke="#F7A54A" stroke-width="3" stroke-linecap="round"/>'
              for c, s_ in [(1, 0), (-1, 0), (0, 1), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)]) +
    f'<path d="M24 92 Q40 80 52 96 Q60 104 70 86" fill="none" stroke="#5E8FE0" stroke-width="3" stroke-dasharray="3 4"/>'
    f'<g transform="rotate(-24 82 80)"><rect x="56" y="66" width="52" height="30" rx="6" fill="#FF8FB4" {W(3.2)}/>'
    f'<rect x="56" y="66" width="18" height="30" rx="6" fill="#5E8FE0" {W(3.2)}/>' + f(90, 80, d=8, k=0.75) + '</g>'
    f'<circle cx="50" cy="104" r="2" fill="#F5B8C8"/><circle cx="58" cy="108" r="1.6" fill="#F5B8C8"/>')

# 8. ЦРТДиЮ «Пресня» — Петрушка
I["crtdiyu-presnya"] = ("#E6FFE0", "#5BBF5A",
    "кукла-петрушка в красном колпаке с бубенчиком",
    "весело машет ручками из-за ширмы кукольного кружка",
    f'<path d="M30 36 Q64 50 98 36" fill="none" {W(3)}/>'
    f'<path d="M48 54 Q42 34 58 30 L80 18 Q86 16 84 24 L76 30 Q86 40 80 54Z" fill="#E2302E" {W(3)}/>'
    f'<circle cx="86" cy="18" r="5" fill="#FFD23F" {W(2.4)}/>'
    f'<circle cx="64" cy="64" r="18" fill="#FFD9B8" {W(3)}/>' + f(64, 64, d=7, k=0.75) +
    f'<circle cx="64" cy="70" r="3" fill="#F25C54"/>'
    f'<path d="M40 52 Q34 70 30 76 M88 52 Q94 70 98 76" fill="none" {W(3)}/>'
    f'<circle cx="28" cy="78" r="5" fill="#FFD9B8" {W(2.4)}/><circle cx="100" cy="78" r="5" fill="#FFD9B8" {W(2.4)}/>'
    f'<path d="M46 80 Q64 74 82 80 L86 92 H42Z" fill="#FFD23F" {W(2.8)}/>'
    f'<rect x="6" y="88" width="116" height="40" fill="#3E6FD8" {W(3)}/>'
    f'<path d="M6 96 H122" stroke="#FFD23F" stroke-width="4"/><circle cx="20" cy="110" r="4" fill="#FFD23F"/><circle cx="108" cy="110" r="4" fill="#FFD23F"/>')

# 9. ЦДиТ «Пресня» — шапка из газеты
I["cdit-presnya-kostikova"] = ("#DDF4FF", "#3FA1C9",
    "бумажная шапка-треуголка, сложенная из газеты",
    "надета набекрень на малыша с валиком, который красит в жёлтый бок картонного домика",
    f'<rect x="72" y="58" width="40" height="52" fill="#C9A06A" {W(3)}/><path d="M68 60 L92 36 L116 60Z" fill="#B47A45" {W(3)}/>'
    f'<rect x="72" y="76" width="22" height="34" fill="#FFD23F"/><rect x="72" y="58" width="40" height="52" fill="none" {W(3)}/>'
    f'<path d="M30 112 Q30 84 46 82 Q62 84 62 112Z" fill="#5BBF5A" {W(3)}/>'
    + kid(46, 68, k=1.15) +
    f'<path d="M24 58 L46 24 L68 58Z" fill="#F4F2EA" {W(3)}/>'
    f'<path d="M34 46 H58 M38 40 H54 M30 52 H62" stroke="#9AA0AE" stroke-width="2"/>'
    f'<path d="M60 92 L74 80" {W(3.4)}/><rect x="70" y="70" width="10" height="18" rx="3" fill="#FFD23F" {W(2.6)}/>')

# 10. Пикабу — игра в ку-ку
I["pikabu-moskovsky"] = ("#FFE6F3", "#D96BB0",
    "смеющийся малыш в полосатой кофточке",
    "играет в «ку-ку»: выглядывает одним глазком из-за раздвинутых пальчиков",
    f'<path d="M18 128 Q20 92 64 90 Q108 92 110 128Z" fill="#6CC0F2" {W(3.2)}/>'
    f'<path d="M24 104 H104 M20 118 H108" stroke="#FFFFFF" stroke-width="6"/>'
    f'<path d="M18 128 Q20 92 64 90 Q108 92 110 128Z" fill="none" {W(3.2)}/>'
    f'<circle cx="64" cy="58" r="32" fill="#FFD9B8" {W(3.2)}/>'
    f'<path d="M34 50 Q36 20 64 22 Q92 20 94 50 Q78 34 64 40 Q50 32 34 50Z" fill="#F2C14E" {W(2.8)}/>'
    f'{eye(76, 58, 1.1)}'
    f'<path d="M56 74 Q64 84 72 74Z" fill="#E2483F" {W(2.4)}/>'
    f'<ellipse cx="86" cy="70" rx="5" ry="3" fill="#FF7FA8" opacity=".7"/>'
    + "".join(f'<rect x="{x}" y="38" width="8" height="34" rx="4" fill="#FFCBA4" {W(2.4)}/>' for x in (34, 43, 52)) +
    f'<rect x="28" y="62" width="30" height="20" rx="8" fill="#FFCBA4" {W(2.4)}/>'
    + sparkle(104, 30, 4, "#fff") + sparkle(20, 34, 3, "#fff"))

# 11. ЧудоОстров — островок из подушек
I["chudoostrov-elektrostal"] = ("#D8FBFF", "#2FB3C6",
    "островок из мягких разноцветных подушек-пуфиков с поролоновой пальмой",
    "плавает посреди игровой, а на нём кувыркается малыш в оранжевых носочках",
    f'<path d="M0 96 Q32 88 64 96 Q96 104 128 96 V128 H0Z" fill="#5BC8F0" {W(2.4)}/>'
    f'<ellipse cx="40" cy="92" rx="22" ry="12" fill="#FF8FB4" {W(3)}/><ellipse cx="86" cy="92" rx="24" ry="12" fill="#FFD23F" {W(3)}/>'
    f'<ellipse cx="62" cy="80" rx="22" ry="11" fill="#8BD47A" {W(3)}/>'
    f'<path d="M92 82 Q90 50 96 32" fill="none" stroke="#B5763C" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M96 32 Q80 20 70 32 M96 32 Q112 20 118 34 M96 32 Q92 16 104 12 M96 32 Q108 40 112 50" fill="none" stroke="#3E9E57" stroke-width="7" stroke-linecap="round"/>'
    + kid(54, 56, k=0.9) +
    f'<path d="M64 64 Q74 58 78 66" fill="none" {W(3)}/><ellipse cx="80" cy="68" rx="5" ry="4" fill="#F7A54A" {W(2.2)}/>'
    f'<ellipse cx="34" cy="68" rx="5" ry="4" fill="#F7A54A" {W(2.2)}/><path d="M36 66 Q42 62 46 64" fill="none" {W(3)}/>')

# 12. Мир искусства — кисти в банке
I["mir-iskusstva-elektrostal"] = ("#FFF1E6", "#C9805A",
    "стеклянная банка с мутной разноцветной водой и пучком кисточек",
    "кисточки торчат как букет, с одной капает синяя капля на палитру-листок",
    f'<rect x="34" y="52" width="60" height="60" rx="10" fill="#E8F4FF" opacity=".9" {W(3.2)}/>'
    f'<path d="M37 74 Q64 66 91 74 V104 Q91 109 86 109 H42 Q37 109 37 104Z" fill="#A98BF0" opacity=".75"/>'
    f'<path d="M40 82 Q58 76 88 86" stroke="#5BC8F0" stroke-width="4" fill="none" opacity=".8"/>'
    + "".join(f'<path d="M{x0} 96 L{x1} 22" stroke="#B5763C" stroke-width="4" stroke-linecap="round"/>'
              f'<path d="M{x1-4} 26 Q{x1} {10} {x1+4} 26Z" fill="{c}" {W(2.2)}/>'
              for x0, x1, c in [(54, 40, "#E2302E"), (62, 60, "#FFD23F"), (70, 82, "#3E9E57"), (76, 100, "#3E6FD8")]) +
    f'<rect x="34" y="52" width="60" height="60" rx="10" fill="none" {W(3.2)}/>'
    + f(64, 92, d=10, k=0.85) +
    f'<path d="M104 32 Q100 40 104 42 Q108 40 104 32Z" fill="#3E6FD8" {W(1.6)}/>')

# 13. Выставочный зал Коняшина — гипсовые тела
I["konyashin-hall-elektrostal"] = ("#EAE6FF", "#6D5BC7",
    "белые гипсовые геометрические тела — куб, шар и пирамида",
    "позируют для рисования на синей драпировке под лампой выставочного зала",
    f'<path d="M0 98 Q30 84 64 98 Q98 112 128 96 V128 H0Z" fill="#3E6FD8" {W(3)}/>'
    f'<path d="M20 98 Q30 104 26 116" fill="none" stroke="#2D52A8" stroke-width="3"/>'
    f'<path d="M64 14 V30" {W(2.6)}/><path d="M52 30 H76 L70 38 H58Z" fill="#FFD23F" {W(2.4)}/>'
    f'<path d="M58 38 L30 96 H100 L70 38Z" fill="#FFF7C8" opacity=".35"/>'
    f'<path d="M22 66 L38 58 L60 64 V94 L42 102 L22 94Z" fill="#F7F5EE" {W(3)}/>'
    f'<path d="M22 66 L42 72 L60 64 M42 72 V102" fill="none" {W(2.6)}/>'
    f'<path d="M90 40 L110 98 H74Z" fill="#F7F5EE" {W(3)}/><path d="M90 40 L94 98" fill="none" {W(2)}/>'
    f'<circle cx="62" cy="88" r="16" fill="#FFFFFF" {W(3)}/>'
    + f(62, 88, d=6, k=0.6) + f(40, 82, d=6, k=0.55) + f(92, 80, d=5, k=0.5, mouth=False))

# 14. Парк «Восточный» — песочный пирожок-звезда
I["vostochny-park-elektrostal"] = ("#FFF4C8", "#E8B43A",
    "песочный пирожок-звезда из формочки",
    "только что вытряхнут на бортик песочницы, рядом малыш с зелёным совочком",
    f'<rect x="0" y="92" width="128" height="40" fill="#F0CF86" {W(2.4)}/>'
    f'<rect x="6" y="82" width="116" height="12" rx="3" fill="#E2483F" {W(2.8)}/>'
    f'<path d="M48 26 L58 50 L84 50 L64 66 L72 92 L48 76 L24 92 L32 66 L12 50 L38 50Z" fill="#E6B35A" {W(3.2)}/>'
    f'<circle cx="40" cy="60" r="2" fill="#B88A3A"/><circle cx="56" cy="70" r="2" fill="#B88A3A"/><circle cx="30" cy="74" r="1.6" fill="#B88A3A"/>'
    + f(48, 62, d=8, k=0.75) +
    f'<path d="M86 112 Q86 92 100 90 Q114 92 114 112Z" fill="#B48CF0" {W(3)}/>'
    + kid(100, 72, k=0.95, hair="#2E2E2E") +
    f'<path d="M86 96 L72 104" {W(3.2)}/><path d="M66 100 Q62 110 72 110 L76 104Z" fill="#58C26B" {W(2.4)}/>')

# 15. Джуманджия — игра-коробка с лианами
I["dzhumandzhiya-kolomna"] = ("#E0F6D8", "#2F7A3C",
    "старинная деревянная игра-коробка с резными барабанчиками",
    "крышка распахнулась, и из неё полезли зелёные лианы с цветами и выкатились два кубика",
    f'<path d="M30 76 Q20 40 40 14 M64 70 Q60 40 72 8 M96 76 Q110 46 98 18" fill="none" stroke="#3E9E57" stroke-width="7" stroke-linecap="round"/>'
    f'<ellipse cx="36" cy="40" rx="8" ry="5" fill="#7CD26E" {W(2)}/><ellipse cx="104" cy="44" rx="8" ry="5" fill="#7CD26E" {W(2)}/>'
    f'<circle cx="40" cy="14" r="6" fill="#FF6FA8" {W(2.2)}/><circle cx="72" cy="10" r="6" fill="#FFD23F" {W(2.2)}/><circle cx="98" cy="18" r="6" fill="#F7A54A" {W(2.2)}/>'
    f'<path d="M18 74 L28 60 H100 L110 74Z" fill="#9C5E2E" {W(3)}/>'
    f'<rect x="18" y="74" width="92" height="36" rx="4" fill="#B87443" {W(3.2)}/>'
    f'<circle cx="34" cy="92" r="7" fill="#D9A35E" {W(2.4)}/><circle cx="94" cy="92" r="7" fill="#D9A35E" {W(2.4)}/>'
    + f(64, 90, d=10, k=0.8) +
    f'<rect x="78" y="108" width="14" height="14" rx="3" fill="#fff" {W(2.4)}/><circle cx="85" cy="115" r="2" fill="{O}"/>'
    f'<rect x="96" y="104" width="14" height="14" rx="3" fill="#fff" {W(2.4)} transform="rotate(18 103 111)"/>')

# 16. Развивайся — кокон и бабочка
I["razvivaysya-kolomna"] = ("#F6E8FF", "#B06BD6",
    "зелёный кокон на веточке",
    "из треснувшего кокона выбирается сонная бабочка и расправляет оранжевые крылья",
    f'<path d="M10 22 Q60 18 118 30" fill="none" stroke="#8A5A2E" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M50 22 V28" {W(3)}/>'
    f'<path d="M50 28 Q34 40 38 66 Q42 92 52 98 Q62 92 64 66 Q66 40 50 28Z" fill="#9BD86A" {W(3)}/>'
    f'<path d="M42 50 Q50 54 60 50 M40 66 Q50 70 62 66 M44 82 Q52 86 60 82" fill="none" {W(2)}/>'
    f'<path d="M56 74 L64 70 L60 80" fill="none" {W(2.4)}/>'
    f'<path d="M76 72 Q96 44 116 58 Q112 80 84 82Z" fill="#F7A54A" {W(3)}/>'
    f'<path d="M78 86 Q100 90 108 108 Q88 112 74 94Z" fill="#FFD23F" {W(3)}/>'
    f'<circle cx="100" cy="64" r="4" fill="#fff"/><circle cx="94" cy="100" r="3" fill="#fff"/>'
    f'<ellipse cx="72" cy="84" rx="7" ry="13" fill="#5B3C7A" {W(2.6)}/>'
    f'<path d="M70 72 Q64 60 58 60 M74 72 Q78 60 84 58" fill="none" {W(2)}/>'
    + f(72, 82, d=3, k=0.4, blush=False) + f(50, 62, d=6, k=0.6))

# 17. ЦДТ Коломна — картофельный штамп
I["cdt-kolomna-tekhnicheskaya"] = ("#E3F0FF", "#4D7AC9",
    "половинка картошки — штамп со звёздочкой",
    "шлёпает по листу бумаги и оставляет ровный ряд синих звёзд",
    f'<rect x="12" y="72" width="104" height="50" rx="4" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<path d="M{x} {y-9} l3 6 7 1 -5 5 1 7 -6 -3 -6 3 1 -7 -5 -5 7 -1Z" fill="#3E6FD8"/>' for x, y in [(28, 96), (52, 104), (100, 104)]) +
    f'<ellipse cx="76" cy="86" rx="12" ry="5" fill="#3E6FD8" opacity=".45"/>'
    f'<path d="M40 52 Q38 16 70 14 Q104 14 104 46 Q104 60 96 64 H48 Q40 62 40 52Z" fill="#D9A35E" {W(3.2)}/>'
    f'<circle cx="58" cy="26" r="2" fill="#9C6A2E"/><circle cx="88" cy="22" r="2" fill="#9C6A2E"/><circle cx="96" cy="40" r="1.6" fill="#9C6A2E"/>'
    f'<rect x="46" y="60" width="54" height="8" rx="3" fill="#F4E6C8" {W(2.6)}/>'
    f'<path d="M73 66 l3 6 7 1 -5 5 1 7 -6 -3 -6 3 1 -7 -5 -5 7 -1Z" fill="#3E6FD8" {W(1.6)}/>'
    + f(72, 40, d=11, k=0.85))

# 18. Новые Водники — кнехт
I["novye-vodniki-dolgoprudny"] = ("#DDF2FF", "#2F86C9",
    "чугунный швартовный кнехт-тумба с толстым канатом",
    "стоит на набережной водохранилища, а за ним по волнам скользят маленькие белые паруса",
    f'<path d="M0 70 Q16 64 32 70 T64 70 T96 70 T128 70 V100 H0Z" fill="#4AA6E0" {W(2.4)}/>'
    f'<path d="M86 64 L96 40 L98 64Z" fill="#fff" {W(2)}/><path d="M18 66 L24 50 L26 66Z" fill="#fff" {W(2)}/>'
    f'<rect x="0" y="96" width="128" height="32" fill="#C6C1B6" {W(2.8)}/>'
    f'<path d="M44 96 V62 H84 V96Z" fill="#4A4F63" {W(3.2)}/>'
    f'<rect x="36" y="52" width="56" height="14" rx="7" fill="#5C6278" {W(3)}/>'
    f'<path d="M30 74 Q64 92 98 74 Q102 82 96 86 Q64 102 32 86 Q26 82 30 74Z" fill="#F2D18A" {W(2.8)}/>'
    f'<path d="M40 82 L44 88 M52 86 L56 92 M64 88 L68 94 M76 86 L80 92 M88 82 L92 88" {W(1.8)}/>'
    + f(64, 64, d=10, k=0.7))

# 19. КДЦ «Полёт» — вертушка-пропеллер
I["kdc-polet-dolgoprudny"] = ("#FFF0F6", "#E06A9A",
    "пластмассовая вертушка-пропеллер на палочке",
    "взлетает высоко над малышом, который только что запустил её ладошками",
    f'<g transform="rotate(-12 64 34)"><ellipse cx="44" cy="30" rx="24" ry="7" fill="#3EC6C6" {W(3)}/>'
    f'<ellipse cx="84" cy="30" rx="24" ry="7" fill="#FFD23F" {W(3)}/><circle cx="64" cy="30" r="7" fill="#F25C54" {W(2.6)}/>'
    f'<path d="M64 36 V64" stroke="#F25C54" stroke-width="5" stroke-linecap="round"/></g>'
    f'<path d="M30 44 Q24 52 30 58 M98 34 Q106 40 102 48" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + f(64, 28, d=10, k=0.55, mouth=False) +
    f'<path d="M40 128 Q40 104 64 102 Q88 104 88 128Z" fill="#58C26B" {W(3)}/>'
    + kid(64, 88, k=1.05, hair="#F2C14E") +
    f'<path d="M46 108 Q36 92 44 78 M82 108 Q92 92 84 78" fill="none" {W(3)}/>'
    f'<circle cx="44" cy="76" r="5" fill="#FFD9B8" {W(2.2)}/><circle cx="84" cy="76" r="5" fill="#FFD9B8" {W(2.2)}/>')

# 20. Два берега — галька-блинчик
I["dva-berega-khimki"] = ("#E2FAF6", "#3AA79A",
    "гладкий серый камешек-голыш с мордашкой",
    "скачет «блинчиками» по реке от одного берега к другому, оставляя круги на воде",
    f'<path d="M0 30 Q30 40 0 60Z" fill="#7CD26E" {W(2.6)}/><path d="M128 72 Q96 86 128 108Z" fill="#7CD26E" {W(2.6)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*.35:.1f}" fill="none" stroke="#fff" stroke-width="2.4"/>' for x, y, r in [(26, 82, 10), (52, 74, 12), (82, 66, 9)]) +
    f'<path d="M26 82 Q38 56 52 74 Q66 50 82 66 Q90 52 96 56" fill="none" stroke="#2F6F6A" stroke-width="2" stroke-dasharray="3 5"/>'
    f'<ellipse cx="96" cy="46" rx="24" ry="15" fill="#A8AFBD" {W(3.2)}/>'
    f'<ellipse cx="90" cy="40" rx="8" ry="3" fill="#fff" opacity=".6"/>'
    + f(96, 48, d=8, k=0.75) + sparkle(30, 22, 3, "#fff"))

# 21. Парк Величко — рукоход
I["velichko-park-skhodnya"] = ("#FFEBD6", "#E87A3E",
    "красный уличный рукоход-лестница на двух стойках",
    "по нему, перехватывая перекладины, перебирается мальчик в синих шортах",
    f'<rect x="0" y="108" width="128" height="24" fill="#8BD47A" {W(2.4)}/>'
    f'<path d="M14 118 V30 M114 118 V30" stroke="#E2302E" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M14 30 H114" stroke="#E2302E" stroke-width="7" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} 24 V36" stroke="#FFD23F" stroke-width="4" stroke-linecap="round"/>' for x in (30, 46, 62, 78, 94)) +
    f'<path d="M46 32 L56 50 M78 32 L68 50" fill="none" {W(3.4)}/>'
    + kid(62, 58, k=0.95) +
    f'<path d="M52 70 H72 L74 90 H50Z" fill="#FFD23F" {W(2.8)}/>'
    f'<path d="M50 88 H74 L72 98 H52Z" fill="#3E6FD8" {W(2.6)}/>'
    f'<path d="M56 98 L50 110 M68 98 L76 108" {W(3.4)}/>')

# 22. Опалиховский пруд — отражение луны
I["opalikha-pond-krasnogorsk"] = ("#3A4A8C", "#121A42",
    "круглая жёлтая луна-персонаж",
    "смотрится в тихий пруд, как в зеркало, и её отражение дрожит дорожкой среди камышинок",
    f'<circle cx="64" cy="36" r="20" fill="#FFE27A" {W(3)}/>' + f(64, 36, d=7, k=0.65) +
    f'<rect x="0" y="66" width="128" height="62" fill="#22346E" {W(2.4)}/>'
    + "".join(f'<rect x="{64-w/2}" y="{y}" width="{w}" height="4" rx="2" fill="#FFE27A" opacity="{op}"/>' for w, y, op in [(30, 74, .9), (22, 84, .75), (34, 94, .6), (18, 104, .5), (26, 114, .4)]) +
    f'<path d="M14 66 Q16 44 12 30 M22 66 Q22 50 26 40 M110 66 Q108 46 114 34" fill="none" stroke="#5BBF5A" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(100, 20, 3, "#fff") + sparkle(28, 18, 2.4, "#fff"))

# 23. Глуховский парк — шкафчик буккроссинга
I["glukhovsky-park-noginsk"] = ("#E9F7DD", "#6FA84A",
    "деревянный домик-шкафчик буккроссинга на столбике",
    "дверца открыта, и одна книжка выпорхнула из полки, хлопая страницами как крыльями",
    f'<rect x="0" y="110" width="128" height="20" fill="#7CC35A" {W(2.4)}/>'
    f'<rect x="38" y="84" width="10" height="30" fill="#8A5A2E" {W(2.6)}/>'
    f'<path d="M14 42 L43 18 L72 42Z" fill="#C0392B" {W(3)}/>'
    f'<rect x="18" y="42" width="50" height="44" fill="#D9A35E" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="48" width="6" height="16" fill="{c}" {W(1.6)}/>' for x, c in [(22, "#3E6FD8"), (29, "#F25C54"), (36, "#FFD23F"), (43, "#58C26B")]) +
    f'<path d="M20 66 H66" {W(2.4)}/>' + f(43, 76, d=7, k=0.6) +
    f'<path d="M68 42 L88 48 V84 L68 86Z" fill="#E8C08A" {W(2.6)}/>'
    f'<path d="M96 40 Q86 28 74 34 L96 46 L118 34 Q106 28 96 40Z" fill="#fff" {W(2.6)}/>'
    f'<path d="M96 40 V46" {W(2)}/><rect x="86" y="44" width="20" height="4" fill="#B48CF0" {W(1.6)}/>'
    + sparkle(110, 60, 3, "#fff"))

# 24. Музей музыкальных традиций — клавиша
I["flier-music-museum-oz"] = ("#FFF3E0", "#B9772E",
    "белая клавиша рояля-персонаж",
    "выпрыгнула из клавиатуры и пляшет над чёрными клавишами, звеня нотками",
    f'<rect x="-4" y="86" width="136" height="40" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M{x} 86 V126" {W(2)}/>' for x in range(12, 128, 16)) +
    "".join(f'<rect x="{x}" y="86" width="9" height="22" rx="2" fill="#2B2A3A"/>' for x in (7, 23, 55, 71, 87, 119)) +
    f'<rect x="34" y="96" width="16" height="30" fill="#2B2A3A"/>'
    f'<g transform="rotate(10 52 50)"><rect x="40" y="22" width="26" height="66" rx="4" fill="#FFFFFF" {W(3.2)}/>' + f(53, 46, d=6, k=0.6) + '</g>'
    f'<path d="M34 90 L28 98 M66 90 L74 96" {W(3)}/>'
    f'<path d="M88 30 V52" {W(2.6)}/><ellipse cx="84" cy="54" rx="5" ry="4" fill="{O}"/><path d="M88 30 Q96 34 98 42" fill="none" {W(2.6)}/>'
    f'<path d="M104 52 V66 M114 48 V62 M104 52 L114 48" {W(2.6)}/><ellipse cx="100" cy="68" rx="4.5" ry="3.5" fill="{O}"/><ellipse cx="110" cy="64" rx="4.5" ry="3.5" fill="{O}"/>')

# 25. Дулёвский парк — клумба-сердце
I["dulevo-park"] = ("#FFF8D6", "#A6C24A",
    "клумба в форме сердца из оранжевых бархатцев",
    "улыбается посреди газона, а над ней кружит полосатый шмель",
    f'<rect x="0" y="40" width="128" height="90" fill="#8BD47A"/>'
    f'<path d="M64 112 Q20 84 22 58 Q24 38 44 38 Q58 38 64 52 Q70 38 84 38 Q104 38 106 58 Q108 84 64 112Z" fill="#7A4A26" {W(3.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#FF9A2E" {W(1.8)}/><circle cx="{x}" cy="{y}" r="2" fill="#B5501A"/>'
              for x, y in [(36, 52), (50, 46), (78, 46), (92, 52), (98, 64), (30, 64), (40, 78), (88, 78), (54, 92), (74, 92), (64, 102)]) +
    f(64, 70, d=10, k=0.85) +
    f'<ellipse cx="100" cy="22" rx="10" ry="8" fill="#FFD23F" {W(2.6)}/><path d="M96 16 V28 M102 15 V29" stroke="{O}" stroke-width="2.6"/>'
    f'<ellipse cx="96" cy="12" rx="6" ry="4" fill="#fff" opacity=".9" {W(1.8)}/>'
    f'<path d="M88 24 Q76 30 80 40" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 4"/>')

# 26. Гуслица — фабричная труба
I["guslitsa-ilinsky-pogost"] = ("#FFE4DA", "#C2563C",
    "старая кирпичная фабричная труба с мордашкой",
    "вместо дыма из неё вылетают разноцветные ленточки и мазки краски над крышей мастерской",
    f'<rect x="0" y="94" width="128" height="36" fill="#B04A32" {W(2.8)}/>'
    + "".join(f'<path d="M{x} 94 L{x+14} 80 L{x+28} 94" fill="#C9603F" {W(2.4)}/>' for x in (0, 28, 84, 100)) +
    f'<path d="M48 112 L54 30 H74 L80 112Z" fill="#D2694A" {W(3.2)}/>'
    + "".join(f'<path d="M{50+i*0.3} {44+i*10} H{78-i*0.3}" stroke="#A8462E" stroke-width="2"/>' for i in range(7)) +
    f'<rect x="50" y="24" width="28" height="8" rx="2" fill="#8A3A26" {W(2.6)}/>'
    + f(64, 62, d=7, k=0.7) +
    f'<path d="M58 22 Q46 8 30 14" fill="none" stroke="#FF6FA8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M64 22 Q66 6 82 4" fill="none" stroke="#FFD23F" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M70 22 Q88 14 104 22" fill="none" stroke="#5BC8F0" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M62 20 Q54 12 58 2" fill="none" stroke="#58C26B" stroke-width="4" stroke-linecap="round"/>')

# 27. ДК «Химик» — подиум с хором
I["dk-khimik-voskresensk"] = ("#FCE4FF", "#9A3FB0",
    "трёхступенчатый деревянный подиум для хора",
    "на ступеньках в три ряда поют малыши в белых рубашках с красными бантами, рты буквой «о»",
    f'<rect x="10" y="102" width="108" height="26" fill="#B87443" {W(3)}/>'
    f'<rect x="24" y="80" width="80" height="22" fill="#C98A52" {W(3)}/>'
    f'<rect x="40" y="58" width="48" height="22" fill="#D9A35E" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="#FFD9B8" {W(2.4)}/>{eye(x-3, y-1, 0.45)}{eye(x+3, y-1, 0.45)}'
              f'<ellipse cx="{x}" cy="{y+4}" rx="2" ry="2.6" fill="#B3263A"/>'
              f'<path d="M{x-7} {y+8} H{x+7} L{x+6} {y+16} H{x-6}Z" fill="#fff" {W(2)}/>'
              f'<path d="M{x-3} {y+10} L{x} {y+12} L{x+3} {y+10}" fill="#E2302E" {W(1.4)}/>'
              for x, y in [(54, 42), (74, 42), (38, 64), (64, 64), (90, 64), (26, 86), (50, 86), (78, 86), (102, 86)]) +
    f'<path d="M106 26 V40" {W(2.4)}/><ellipse cx="103" cy="41" rx="4" ry="3" fill="{O}"/><path d="M18 20 V32" {W(2.4)}/><ellipse cx="15" cy="33" rx="4" ry="3" fill="{O}"/>')

# 28. Зарайский парк — ротонда
I["zaraysk-central-park"] = ("#E4F7FF", "#6FB8DA",
    "белая парковая ротонда с колоннами и зелёным куполом",
    "стоит на холмике среди лип, а между её колонн развешаны бумажные флажки к детскому празднику",
    f'<path d="M0 104 Q64 84 128 104 V128 H0Z" fill="#7CC35A" {W(2.6)}/>'
    f'<circle cx="16" cy="70" r="16" fill="#58A84A" {W(2.6)}/><circle cx="112" cy="70" r="16" fill="#58A84A" {W(2.6)}/>'
    f'<path d="M30 42 Q64 4 98 42Z" fill="#4CB08A" {W(3.2)}/><path d="M64 12 V4" {W(2.6)}/><circle cx="64" cy="4" r="3" fill="#FFD23F" {W(2)}/>'
    f'<rect x="28" y="42" width="72" height="10" rx="2" fill="#fff" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="52" width="8" height="40" fill="#fff" {W(2.6)}/>' for x in (34, 52, 68, 86)) +
    f'<rect x="24" y="92" width="80" height="10" rx="2" fill="#fff" {W(3)}/>'
    f'<path d="M38 58 Q64 70 90 58" fill="none" {W(1.6)}/>'
    + "".join(f'<path d="M{x} {y} l5 0 -2.5 6Z" fill="{c}"/>' for x, y, c in [(44, 61, "#F25C54"), (56, 64, "#FFD23F"), (68, 64, "#3E6FD8"), (80, 61, "#58C26B")]) +
    f(64, 80, d=8, k=0.7))

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
