"""Иконки робота fun (2026-11-09, 5-й проход): 12 мест из tools/add_fun_1109f.py.
Каждая придумана и нарисована отдельно (правило абсолютной уникальности); сюжеты сверены с subjects.txt.
Запуск: python3 tools/icons_fun_1109f.py  (пишет icons-src/<id>.svg и печатает строки для subjects.txt)"""
import os
from draw_icons import s, face, sparkle, O

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


I = {}

# A4 Kids City — город профессий от «Влада А4»: сам лист А4 примеряет профессию врача
I["a4-kids-city-columbus"] = ("#F2FBFF", "#7CC6F0",
    "белый лист бумаги формата А4 с мордашкой и загнутым уголком",
    "надел белую докторскую шапочку с красным крестиком и слушает стетоскопом плюшевого мишку",
    f'<path d="M30 30 H82 L96 44 V112 H30Z" fill="#fff" {W(3.2)}/>'
    f'<path d="M82 30 V44 H96" fill="#E3EEF7" {W(3)}/>'
    f'<path d="M34 22 Q63 6 92 22 L90 34 H36Z" fill="#fff" {W(3)}/>'
    f'<path d="M60 14 H66 V18 H70 V24 H66 V28 H60 V24 H56 V18 H60Z" fill="#E8434A"/>'
    + face(60, 64, d=9, k=0.85) +
    f'<path d="M48 80 Q46 96 62 98 Q78 98 76 86" fill="none" stroke="#5B6B8C" stroke-width="3.2"/>'
    f'<circle cx="76" cy="84" r="5" fill="#C9D3E3" {W(2.4)}/>'
    f'<circle cx="104" cy="96" r="13" fill="#C98B4E" {W(2.8)}/><circle cx="95" cy="85" r="5" fill="#C98B4E" {W(2.4)}/>'
    f'<circle cx="113" cy="85" r="5" fill="#C98B4E" {W(2.4)}/>'
    + face(104, 96, d=4.5, k=0.45) +
    sparkle(18, 50, 5) + sparkle(110, 26, 4))

# «Сделал Сам» — детская столярная мастерская: киянка забивает гвоздик в скворечник
I["sdelal-sam-kutuzovsky"] = ("#FFF6E6", "#E9B26E",
    "деревянная киянка-колотушка столяра с толстым бочонком-головой",
    "забивает гвоздик в недостроенный скворечник на верстаке, а вокруг разлетаются опилки",
    f'<rect x="6" y="100" width="116" height="12" fill="#B9773E" {W(3)}/><path d="M18 112 V128 M110 112 V128" {W(5)}/>'
    f'<path d="M78 100 V62 L96 48 L114 62 V100Z" fill="#E7C08A" {W(3)}/>'
    f'<path d="M74 64 L96 44 L118 64" fill="none" stroke="#9A5B2A" stroke-width="5" stroke-linecap="round"/>'
    f'<circle cx="96" cy="76" r="7" fill="#5A3A22" {W(2.4)}/>'
    f'<path d="M80 60 L72 58" {W(2.6)}/><circle cx="70" cy="58" r="2" fill="{O}"/>'
    f'<g transform="rotate(-28 44 58)"><rect x="40" y="58" width="9" height="52" rx="4" fill="#D9A066" {W(2.8)}/>'
    f'<rect x="20" y="30" width="50" height="32" rx="10" fill="#E8B57A" {W(3.2)}/>'
    f'<path d="M30 30 V62 M60 30 V62" stroke="#B9773E" stroke-width="2"/>'
    + face(45, 46, d=8, k=0.75) + '</g>'
    f'<path d="M64 40 L58 34 M70 46 L76 40 M66 50 L74 52" stroke="#9A5B2A" stroke-width="2.6" stroke-linecap="round"/>'
    f'<path d="M30 96 q3 -4 6 0 M44 98 q3 -4 6 0 M58 94 q3 -4 6 0" fill="none" stroke="#C98B4E" stroke-width="2.2"/>')

# «Чудеса» — мастер-классы: тюбик с блёстками украшает открытку
I["chudesa-maryino"] = ("#FCEFFF", "#C77BE0",
    "тюбик с золотыми блёстками и мордашкой на этикетке",
    "щедро посыпает сверкающей пылью открытку с нарисованной ёлочкой на столе мастер-класса",
    f'<rect x="10" y="78" width="70" height="44" rx="3" fill="#fff" {W(3)}/>'
    f'<path d="M45 86 L33 104 H40 L30 116 H60 L50 104 H57Z" fill="#4CC38A" {W(2.4)}/>'
    f'<g transform="rotate(35 82 52)"><rect x="66" y="20" width="32" height="62" rx="8" fill="#FFD23F" {W(3.2)}/>'
    f'<rect x="72" y="8" width="20" height="14" rx="3" fill="#B06BD8" {W(2.8)}/>'
    f'<rect x="66" y="40" width="32" height="24" fill="#fff" {W(2.4)}/>'
    + face(82, 50, d=7, k=0.65) + '</g>'
    + "".join(sparkle(x, y, r, "#FFC93C") for x, y, r in [(52, 72, 4), (40, 66, 3), (62, 82, 3.5), (28, 74, 2.5), (48, 92, 2.5), (66, 96, 3)])
    + sparkle(110, 104, 6) + sparkle(22, 30, 5))

# «Клевер» — каллиграфия: перьевая ручка выводит завиток в прописи
I["clever-kids-chelyuskinskaya"] = ("#EEFBEA", "#7FCB7A",
    "перьевая ручка с золотым пером и мордашкой на корпусе",
    "выводит в прописи завиток каллиграфической буквы «К», от усердия высунув язык",
    f'<path d="M4 88 L124 82 V128 H4Z" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M4 {y} L124 {y-6}" stroke="#9CC4E8" stroke-width="1.4"/>' for y in (100, 112, 124)) +
    f'<path d="M20 116 Q14 96 30 94 M30 94 Q22 106 34 112 Q46 116 40 100" fill="none" stroke="#2C4A9A" stroke-width="3.4" stroke-linecap="round"/>'
    f'<path d="M48 108 Q56 92 66 104" fill="none" stroke="#2C4A9A" stroke-width="3.4" stroke-linecap="round"/>'
    f'<g transform="rotate(38 84 56)"><rect x="72" y="2" width="24" height="70" rx="11" fill="#2F7D5B" {W(3.2)}/>'
    f'<rect x="72" y="20" width="24" height="7" fill="#FFD23F" {W(2)}/>'
    f'<path d="M74 72 H94 L84 98Z" fill="#FFC93C" {W(3)}/><path d="M84 80 V96" {W(2)}/>'
    f'<circle cx="84" cy="44" r="0"/></g>'
    + face(78, 46, d=7, k=0.7, mouth=False) +
    f'<path d="M72 56 Q78 62 84 56" fill="none" {W(2.4)}/><path d="M80 59 q3 6 6 1" fill="#FF7FA8" {W(1.8)}/>'
    + sparkle(110, 30, 5) + sparkle(24, 40, 4))

# «Мы вместе» — кукольный уголок театральной студии: пальчиковые зайчик и лисичка обнимаются
I["my-vmeste-michurinsky"] = ("#FFF1EC", "#F59A86",
    "две вязаные пальчиковые куклы — серый зайчик и рыжая лисичка",
    "обнимаются над краем маленькой полосатой ширмы кукольного уголка",
    f'<rect x="8" y="86" width="112" height="42" fill="#5B8DEF" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="86" width="14" height="42" fill="#FFE07A"/>' for x in (22, 50, 78, 106)) +
    f'<rect x="8" y="86" width="112" height="42" fill="none" {W(3)}/><rect x="4" y="80" width="120" height="10" rx="4" fill="#E8434A" {W(3)}/>'
    f'<path d="M30 82 V48 Q30 34 44 34 Q58 34 58 48 V82Z" fill="#C9CED8" {W(3)}/>'
    f'<path d="M36 38 Q30 8 38 6 Q46 10 44 36Z" fill="#C9CED8" {W(2.8)}/><path d="M48 36 Q50 8 58 10 Q62 18 54 38Z" fill="#C9CED8" {W(2.8)}/>'
    + face(44, 54, d=6, k=0.6) +
    f'<path d="M70 82 V50 Q70 38 84 38 Q98 38 98 50 V82Z" fill="#FF8A3D" {W(3)}/>'
    f'<path d="M72 44 L70 22 L84 38Z M96 44 L100 22 L86 38Z" fill="#FF8A3D" {W(2.8)}/>'
    f'<path d="M76 62 Q84 74 92 62 Q84 66 76 62Z" fill="#fff"/>'
    + face(84, 54, d=6, k=0.6) +
    f'<path d="M58 62 Q66 58 72 66" fill="none" stroke="#C9CED8" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M58 62 Q66 58 72 66" fill="none" {W(1.6)}/>'
    f'<path d="M64 26 q-6 -8 0 -10 q6 2 0 10Z" fill="#FF6B8B"/><path d="M64 26 q6 -8 0 -10" fill="#FF6B8B"/>'
    + sparkle(110, 30, 5) + sparkle(16, 30, 4))

# «Ирбис» (Кутузовская) — репетиция: сценарий со скрепкой читает роль, стоя на табуретке
I["irbis-kutuzovskaya"] = ("#FFF9E0", "#F2C94C",
    "пачка листов сценария со скрепкой и мордашкой",
    "стоит на деревянной табуретке и с выражением читает роль, вскинув руку к потолку",
    f'<path d="M44 98 H84 V106 H44Z" fill="#B9773E" {W(3)}/><path d="M50 106 L44 128 M78 106 L84 128 M48 118 H80" {W(3.6)}/>'
    f'<rect x="44" y="26" width="46" height="62" rx="3" fill="#F4F0E6" {W(2.6)}/>'
    f'<rect x="38" y="20" width="46" height="66" rx="3" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M46 {y} H76" stroke="#B9C2D3" stroke-width="2"/>' for y in (64, 70, 76)) +
    f'<path d="M48 14 V30 Q48 34 52 34 Q56 34 56 30 V18" fill="none" stroke="#8A97AD" stroke-width="2.8"/>'
    + face(61, 46, d=8, k=0.75, mouth=False) +
    f'<ellipse cx="61" cy="57" rx="5" ry="4" fill="#E8434A" {W(2)}/>'
    f'<path d="M84 44 Q96 30 102 14" fill="none" {W(3)}/><circle cx="103" cy="12" r="4" fill="#fff" {W(2.4)}/>'
    f'<path d="M38 56 Q28 64 30 76" fill="none" {W(3)}/>'
    f'<path d="M64 98 V88 M54 98 V88" {W(3)}/>'
    + sparkle(20, 30, 5) + sparkle(110, 50, 4) + sparkle(104, 84, 3))

# «Ирбис» (Братиславская) — декорация моря из картонных волн, по ней плывёт бумажный кораблик
I["irbis-bratislavskaya"] = ("#EAF3FF", "#5D7FD6",
    "картонная декорация-волна из трёх синих гребней на деревянной подпорке",
    "качается на сцене, изображая бурное море, а по гребню скользит бумажный кораблик",
    f'<rect x="0" y="104" width="128" height="24" fill="#8E5A34" {W(3)}/>'
    f'<path d="M30 104 L44 86 M98 104 L84 86" stroke="#B9773E" stroke-width="5"/>'
    f'<path d="M6 92 Q16 52 34 62 Q42 70 36 74 Q50 40 70 52 Q78 60 72 64 Q88 34 108 46 Q120 54 122 92Z" fill="#3E7BE0" {W(3.2)}/>'
    f'<path d="M14 92 Q24 74 40 84 M48 92 Q62 70 80 84 M86 92 Q100 72 116 84" fill="none" stroke="#9CC8FF" stroke-width="3"/>'
    + face(66, 76, d=9, k=0.8) +
    f'<path d="M88 36 H112 L106 46 H94Z" fill="#fff" {W(2.6)}/><path d="M100 36 V18 L112 32Z" fill="#fff" {W(2.4)}/>'
    + sparkle(22, 28, 5) + sparkle(50, 22, 3.5))

# «Ирбис» (Крылатское) — накладные усы на палочке примеряют роль капитана
I["irbis-krylatskoe"] = ("#F0FFF7", "#3FB98A",
    "чёрные накладные усы-подкрутка на палочке",
    "крутятся у круглого зеркала, пробуя роль усатого капитана, рядом лежит капитанская фуражка",
    f'<circle cx="92" cy="54" r="30" fill="#DDF3FF" {W(3.2)}/><circle cx="92" cy="54" r="24" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>'
    f'<path d="M92 84 V100 M80 100 H104" {W(4)}/>'
    f'<rect x="44" y="70" width="6" height="56" rx="3" fill="#C98B4E" {W(2.4)}/>'
    f'<path d="M47 66 Q34 54 20 62 Q10 68 14 76 Q18 70 24 72 Q36 78 47 72 Q58 78 70 72 Q76 70 80 76 Q84 68 74 62 Q60 54 47 66Z" fill="#3B3355" {W(2.4)}/>'
    + face(47, 50, d=10, k=0.8, mouth=False, blush=True) +
    f'<path d="M20 112 Q22 96 44 96 L46 112Z" fill="#fff" {W(2.6)}/><rect x="14" y="110" width="40" height="8" rx="3" fill="#1F2D5C" {W(2.4)}/>'
    f'<circle cx="34" cy="103" r="3.5" fill="#FFC93C" {W(1.6)}/>'
    + sparkle(110, 24, 5) + sparkle(18, 30, 4))

# «Ирбис» (Бабушкинская) — третий звонок перед спектаклем
I["irbis-babushkinskaya"] = ("#FFF0F3", "#E86A8E",
    "латунный ручной звонок-колокольчик с деревянной ручкой",
    "трезвонит в фойе театра — третий звонок, спектакль начинается",
    f'<g transform="rotate(-18 64 66)">'
    f'<rect x="58" y="10" width="13" height="30" rx="6" fill="#8E5A34" {W(3)}/>'
    f'<path d="M64 40 Q38 42 34 80 L30 92 H98 L94 80 Q90 42 64 40Z" fill="#F5C242" {W(3.2)}/>'
    f'<path d="M44 54 Q42 70 40 84" fill="none" stroke="#FFF2B8" stroke-width="4" stroke-linecap="round"/>'
    + face(64, 68, d=10, k=0.85) +
    f'<circle cx="64" cy="100" r="7" fill="#D9A21F" {W(2.6)}/></g>'
    f'<path d="M14 54 Q8 64 14 74 M22 50 Q14 64 22 78" fill="none" {W(2.8)}/>'
    f'<path d="M104 70 Q112 80 106 92 M98 74 Q104 82 100 90" fill="none" {W(2.8)}/>'
    f'<text x="98" y="38" font-family="Arial" font-weight="700" font-size="22" fill="#B83B63">3</text>'
    + sparkle(20, 24, 5) + sparkle(110, 112, 4))

# «Палана» (ЖК «Москва А101») — названа как камчатский посёлок: мягкий вулкан-горка извергает шарики
I["palana-kommunarka"] = ("#FFF4E5", "#FF9F5A",
    "мягкий поролоновый вулкан-горка с мордашкой",
    "из жерла вместо лавы радостно вылетают разноцветные шарики сухого бассейна",
    f'<path d="M4 120 L40 50 H88 L124 120Z" fill="#8C6BD8" {W(3.2)}/>'
    f'<path d="M40 50 Q50 58 56 52 Q64 60 72 52 Q80 60 88 50" fill="#FF6B6B" {W(2.6)}/>'
    f'<path d="M60 118 Q70 96 92 92 L106 120" fill="#B9A2F0" {W(2.6)}/>'
    + face(62, 82, d=10, k=0.85) +
    "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}" {W(2.2)}/>' for x, y, c in
            [(52, 30, "#FFD23F"), (70, 18, "#4CC38A"), (86, 34, "#5B8DEF"), (36, 16, "#FF6B8B"), (98, 14, "#FF8A3D")])
    + sparkle(116, 50, 4) + sparkle(14, 50, 4))

# «Остров детства» (Ступино) — карусель-тарелка для малышей
I["ostrov-detstva-stupino"] = ("#E8FFF6", "#3CC6A8",
    "крутящаяся тарелка-вертушка для малышей с мордашкой на ободе",
    "раскручивает трёх плюшевых зверят — у них развеваются ушки и хвостики",
    f'<ellipse cx="64" cy="98" rx="54" ry="18" fill="#FF7A59" {W(3.2)}/>'
    f'<ellipse cx="64" cy="92" rx="50" ry="14" fill="#FFD7A8" {W(3)}/>'
    f'<circle cx="64" cy="92" r="6" fill="#FF7A59" {W(2.4)}/>'
    + face(64, 106, d=11, k=0.75, mouth=True) +
    # зайчик
    f'<circle cx="34" cy="78" r="10" fill="#fff" {W(2.6)}/><path d="M28 70 Q18 54 26 52 Q32 58 32 68 M38 68 Q40 54 48 54 Q48 64 40 70" fill="#fff" {W(2.4)}/>'
    + face(34, 78, d=3.5, k=0.38) +
    # мишка
    f'<circle cx="64" cy="62" r="11" fill="#C98B4E" {W(2.6)}/><circle cx="55" cy="53" r="4.5" fill="#C98B4E" {W(2.2)}/><circle cx="73" cy="53" r="4.5" fill="#C98B4E" {W(2.2)}/>'
    + face(64, 62, d=3.8, k=0.4) +
    # котик
    f'<circle cx="94" cy="78" r="10" fill="#9FA8BA" {W(2.6)}/><path d="M86 72 L88 60 L94 68 M102 72 L102 60 L95 68" fill="#9FA8BA" {W(2.2)}/>'
    + face(94, 78, d=3.5, k=0.38) +
    f'<path d="M14 60 Q22 40 44 36 M114 60 Q106 40 84 36" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>'
    + sparkle(64, 22, 5))

# Гончарная мастерская Завацких — глиняная свистулька-рыбка поёт над гончарным кругом
I["zavatsky-pottery-kolomna"] = ("#FFF3E8", "#D98B5F",
    "глиняная свистулька-рыбка с точечной росписью-чешуёй",
    "сидит на краю вращающегося гончарного круга и насвистывает нотки из хвоста",
    f'<ellipse cx="64" cy="108" rx="52" ry="12" fill="#6B7A8F" {W(3)}/><ellipse cx="64" cy="104" rx="46" ry="9" fill="#9AA8BB" {W(2.6)}/>'
    f'<path d="M30 102 Q40 96 50 102 M78 102 Q88 96 98 102" fill="none" stroke="#fff" stroke-width="2" opacity=".8"/>'
    f'<path d="M24 66 Q40 36 74 46 Q86 50 92 62 L110 48 Q104 66 110 84 L92 72 Q84 92 60 94 Q30 94 24 66Z" fill="#E7915A" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#FFF3D6"/>' for x, y in [(56, 60), (66, 66), (56, 74), (70, 80), (78, 62), (46, 82)]) +
    f'<path d="M40 60 Q46 74 40 86" fill="none" stroke="#B5582F" stroke-width="2.4"/>'
    + face(34, 66, d=5, k=0.55, mouth=False) +
    f'<circle cx="30" cy="78" r="3.5" fill="#3B3355"/>'
    f'<path d="M110 30 v14 a4 3 0 1 1 -2 -3 V30 l10 -3 v12 a4 3 0 1 1 -2 -3 V30" fill="#3B3355" stroke="#3B3355" stroke-width="1"/>'
    f'<path d="M96 24 v12 a4 3 0 1 1 -2 -3 V24" fill="none" stroke="#3B3355" stroke-width="2.2"/>'
    + sparkle(20, 30, 5) + sparkle(60, 22, 4))

if __name__ == "__main__":
    for pid, (a, b, hero, scene, body) in I.items():
        open(os.path.join(out, pid + ".svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
