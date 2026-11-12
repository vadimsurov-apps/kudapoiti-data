"""Иконки робота cafes, 2026-11-12 (20 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1112v.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
BL = lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="3.8" ry="2.2" fill="#FF7FA8" opacity=".7"/>'
draw_icons.BG.update({
    "zv_ikat": ("#EAF3FF", "#3F6FC4"),
    "zv_space": ("#2B2F5E", "#7A5BC9"),
    "zv_beanbag": ("#FFF6E8", "#E9A04B"),
    "zv_flour": ("#FFFDF7", "#D8C3A0"),
    "zv_pond": ("#E6FFF3", "#3FAE86"),
    "zv_night": ("#1E2A4A", "#4B5F9E"),
    "zv_snow": ("#F2FAFF", "#8CC4E8"),
    "zv_ramp": ("#FFF0E6", "#E8664A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Урюк by Osh: узбекская урама — спиральная булочка-розочка танцует с лентой теста
add("cafe-uryk-by-osh-kirovogradskaya-13a",
    "узбекская урама — румяная спиральная булочка-розочка из тонко скрученного теста, посыпанная сахарной пудрой",
    "кружится на одной ножке, раскручивая свой хвостик-ленточку из теста над головой, как гимнастка ленту",
    "zv_ikat", f'''
<path d="M90 40 Q112 20 102 6 Q88 0 96 18 Q104 32 118 30" fill="none" stroke="#E9B062" stroke-width="7" stroke-linecap="round"/>
<path d="M90 40 Q112 20 102 6 Q88 0 96 18 Q104 32 118 30" fill="none" {W(2)} opacity=".5"/>
<path d="M58 104 L54 120 M70 104 L72 112" {W(3.4)}/>
<ellipse cx="53" cy="121" rx="6" ry="3" fill="#C1593A" {W(2)}/>
<circle cx="64" cy="70" r="36" fill="#E9A54F" {W(3.4)}/>
<path d="M64 70 m0 -6 a6 6 0 1 1 -6 6 a12 12 0 1 1 12 12 a18 18 0 1 1 -18 -18 a24 24 0 1 1 24 24 a30 30 0 1 1 -30 -30" fill="none" stroke="#B9702A" stroke-width="3" stroke-linecap="round"/>
<g fill="#FFFFFF" opacity=".85"><circle cx="46" cy="50" r="2"/><circle cx="80" cy="48" r="1.8"/><circle cx="88" cy="74" r="1.8"/><circle cx="44" cy="86" r="1.8"/><circle cx="70" cy="96" r="1.6"/></g>
{eye(54, 64, 0.85)}{eye(74, 64, 0.85)}
<path d="M58 75 Q64 82 70 75Z" fill="#E24B5B" {W(1.8)}/>
{BL(46, 74)}{BL(82, 74)}
<path d="M96 60 Q104 52 92 42" fill="none" {W(3.2)}/>
<path d="M30 62 Q18 54 14 62" fill="none" {W(3.2)}/>
<path d="M18 104 Q30 98 40 104 M90 112 Q100 106 112 112" fill="none" stroke="#3F6FC4" stroke-width="2.4" stroke-linecap="round" opacity=".6"/>
{sparkle(20, 24, 5)}{sparkle(36, 12, 3)}
''')

# 2. iL Патио (Кировоградская, 13А, 4 этаж): кусок пиццы-ракета стартует
add("cafe-ilpatio-kirovogradskaya-13a",
    "треугольный кусок пиццы-ракета с кружками пепперони-иллюминаторами и корочкой-соплом",
    "стартует в звёздное небо мимо маленькой планеты-оливки, из корочки вырываются языки пламени из тянущегося сыра",
    "zv_space", f'''
<g fill="#FFFFFF"><circle cx="18" cy="20" r="1.6"/><circle cx="104" cy="16" r="1.4"/><circle cx="112" cy="58" r="1.6"/><circle cx="14" cy="70" r="1.2"/><circle cx="30" cy="40" r="1"/></g>
<path d="M48 100 Q40 118 50 126 Q54 114 58 110 Q62 122 70 126 Q78 116 72 100Z" fill="#FFD64A" {W(2.6)}/>
<path d="M54 102 Q52 114 58 118 Q62 110 66 102Z" fill="#FFF3B0"/>
<path d="M60 8 L88 92 Q60 102 32 92Z" fill="#FFC94A" {W(3.2)}/>
<path d="M36 84 Q60 94 84 84" fill="none" stroke="#E8553B" stroke-width="5" opacity=".7"/>
<path d="M30 92 Q60 104 90 92 L92 100 Q60 112 28 100Z" fill="#C98A3E" {W(3)}/>
<g fill="#C9302C" {W(2.2)}><circle cx="60" cy="38" r="8"/><circle cx="52" cy="64" r="7"/><circle cx="70" cy="66" r="6.5"/></g>
<g fill="#FFFFFF" opacity=".55"><circle cx="57" cy="35" r="2.4"/><circle cx="50" cy="61" r="2"/><circle cx="68" cy="63" r="2"/></g>
<path d="M36 80 L22 96 L34 94Z M84 80 L98 96 L86 94Z" fill="#E8553B" {W(2.4)}/>
{eye(55, 50, 0.7)}{eye(66, 50, 0.7)}
<path d="M58 56 Q61 59 64 56" fill="none" {W(1.6)}/>
<circle cx="100" cy="34" r="9" fill="#3E3E3E" {W(2.4)}/><circle cx="100" cy="34" r="3.4" fill="#8A6BC9"/>
<ellipse cx="100" cy="34" rx="15" ry="4" fill="none" stroke="#C6B6F5" stroke-width="2"/>
{sparkle(22, 52, 4)}{sparkle(110, 86, 3.5)}
''')

# 3. Хинкали-Gали! (Митинская, 16): ачма листает свои слои, как книжку, в кресле-мешке
add("cafe-hinkali-gali-mitinskaya-16",
    "квадратная грузинская ачма — пирог из волнистых слоёв теста с белым сыром между ними",
    "развалилась в оранжевом кресле-мешке и листает свои верхние слои, как страницы книжки",
    "zv_beanbag", f'''
<path d="M14 120 Q8 82 34 74 Q64 64 94 74 Q122 84 114 120Z" fill="#F08A3C" {W(3.2)}/>
<path d="M30 92 Q36 100 30 112 M98 92 Q92 102 98 114" fill="none" stroke="#C9631F" stroke-width="2.4" stroke-linecap="round"/>
<g {W(3)}>
<path d="M32 98 Q48 94 64 98 Q80 102 96 98 L96 76 Q80 80 64 76 Q48 72 32 76Z" fill="#E9B567"/>
</g>
<path d="M32 90 Q48 86 64 90 Q80 94 96 90" fill="none" stroke="#FFFFFF" stroke-width="3"/>
<path d="M32 83 Q48 79 64 83 Q80 87 96 83" fill="none" stroke="#C88A3C" stroke-width="2"/>
<path d="M32 76 Q48 72 64 76 L60 44 Q46 40 30 46Z" fill="#F2C67A" {W(3)}/>
<path d="M64 76 Q80 80 96 76 L104 46 Q86 42 66 46Z" fill="#F7D594" {W(3)}/>
<path d="M36 54 L56 52 M36 60 L56 58 M70 54 L96 54 M70 60 L94 60" stroke="#C88A3C" stroke-width="2" stroke-linecap="round"/>
<path d="M64 76 L64 46" {W(2.4)}/>
{eye(44, 86, 0.8)}{eye(82, 86, 0.8)}
<path d="M58 92 Q64 96 70 92" fill="none" {W(1.8)}/>
{BL(38, 94)}{BL(90, 94)}
<path d="M30 80 Q22 64 30 52 M98 80 Q108 66 102 52" fill="none" {W(3)}/>
{sparkle(20, 22, 5)}{sparkle(108, 26, 4)}
''')

# 4. Хинкальная Кинза (детские кулинарные мастер-классы): шарик теста с отпечатками ладошек
add("cafe-kinza-vernadskogo-6",
    "пухлый белый шарик теста, на боку которого отпечатались две маленькие детские ладошки",
    "сидит на присыпанной мукой деревянной доске, на макушке маленький поварской колпак, рядом свиток-диплом с красной ленточкой",
    "zv_flour", f'''
<rect x="8" y="88" width="112" height="30" rx="6" fill="#D9A867" {W(3)}/>
<path d="M14 98 L114 98 M14 108 L114 108" stroke="#B9874A" stroke-width="1.6"/>
<g fill="#FFFFFF" opacity=".85"><circle cx="20" cy="92" r="2.4"/><circle cx="34" cy="94" r="1.8"/><circle cx="98" cy="92" r="2"/><circle cx="110" cy="96" r="1.6"/><circle cx="86" cy="95" r="1.4"/></g>
<ellipse cx="58" cy="70" rx="38" ry="28" fill="#FFF8EC" {W(3.2)}/>
<g fill="#F0DEC2"><path d="M30 70 q-2 -10 2 -12 q2 4 2 8 q0 -10 3 -11 q2 4 1 11 q2 -8 5 -8 q1 4 -1 10 q3 -5 5 -4 q0 6 -5 10 q-4 6 -10 4Z"/>
<path d="M74 82 q-2 -10 2 -12 q2 4 2 8 q0 -10 3 -11 q2 4 1 11 q2 -8 5 -8 q1 4 -1 10 q3 -5 5 -4 q0 6 -5 10 q-4 6 -10 4Z"/></g>
<path d="M44 42 Q36 30 46 26 Q50 14 62 20 Q74 14 76 28 Q86 30 76 42Z" fill="#FFFFFF" {W(2.8)}/>
<rect x="44" y="38" width="32" height="8" rx="2" fill="#FFFFFF" {W(2.4)}/>
{eye(50, 64, 0.85)}{eye(68, 64, 0.85)}
<path d="M54 74 Q59 79 64 74" fill="none" {W(1.8)}/>
{BL(42, 72)}{BL(76, 70)}
<g transform="rotate(-18 106 64)"><rect x="96" y="44" width="16" height="40" rx="3" fill="#FFF3D6" {W(2.4)}/>
<ellipse cx="104" cy="44" rx="10" ry="4" fill="#F3E2BE" {W(2.2)}/><ellipse cx="104" cy="84" rx="10" ry="4" fill="#F3E2BE" {W(2.2)}/>
<path d="M96 64 L112 64" stroke="#E2362F" stroke-width="4"/><path d="M104 64 L98 74 M104 64 L110 74" stroke="#E2362F" stroke-width="2.6" stroke-linecap="round"/></g>
{sparkle(18, 22, 5, "#E9C46A")}{sparkle(100, 18, 4, "#E9C46A")}
''')

# 5. VillaMio (у Воронцовских прудов): лягушонок-оливка плывёт на мини-пицце, как на кувшинке
add("cafe-villamio-vorontsovskie-prudy-11",
    "лягушонок из целой зелёной оливки с красной перчинкой-языком",
    "сидит на круглой мини-пицце, которая плывёт по пруду, как лист кувшинки, и гребёт веточкой базилика",
    "zv_pond", f'''
<rect x="0" y="74" width="128" height="54" fill="#5CC2B0"/>
<path d="M0 74 Q32 70 64 74 Q96 78 128 74" fill="none" stroke="#C9F2E8" stroke-width="3"/>
<path d="M10 112 Q20 108 30 112 M96 116 Q106 112 116 116" fill="none" stroke="#DDF8F1" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="62" cy="92" rx="48" ry="14" fill="#D9963A" {W(3.2)}/>
<ellipse cx="62" cy="89" rx="40" ry="10" fill="#E8553B"/>
<g fill="#FFF6D8"><ellipse cx="40" cy="88" rx="7" ry="3"/><ellipse cx="82" cy="90" rx="7" ry="3"/><ellipse cx="62" cy="94" rx="6" ry="2.4"/></g>
<path d="M100 84 L118 60" stroke="#7A5A2E" stroke-width="3.4" stroke-linecap="round"/>
<path d="M114 64 Q126 56 124 46 Q112 48 112 60Z" fill="#3E9B50" {W(2.2)}/>
<ellipse cx="62" cy="66" rx="26" ry="20" fill="#7DBB3A" {W(3.2)}/>
<ellipse cx="62" cy="72" rx="15" ry="10" fill="#B8E07A"/>
<circle cx="50" cy="46" r="9" fill="#7DBB3A" {W(3)}/><circle cx="74" cy="46" r="9" fill="#7DBB3A" {W(3)}/>
{eye(50, 46, 0.8)}{eye(74, 46, 0.8)}
<path d="M54 60 Q62 66 70 60" fill="none" {W(2)}/>
<path d="M62 63 Q60 72 66 74 Q70 70 64 63Z" fill="#E2362F" {W(1.6)}/>
{BL(44, 62)}{BL(80, 62)}
<path d="M86 66 Q96 70 100 78" fill="none" {W(3)}/>
<path d="M40 80 Q36 86 40 88 M84 80 Q88 86 84 88" fill="none" {W(2.6)}/>
<g fill="#FFFFFF" opacity=".9"><circle cx="20" cy="24" r="6"/><circle cx="28" cy="22" r="8"/><circle cx="36" cy="25" r="6"/></g>
''')

# 6. Лунный Свет (кафе-кофейня с детским уголком): сырник-луна над спящими домиками
add("cafe-lunny-svet-dmitrovskoe-107a",
    "круглый румяный сырник с изюминками-кратерами",
    "светит вместо полной луны над тёмными крышами спящего квартала, вокруг мерцают звёзды из сахарной пудры",
    "zv_night", f'''
<g fill="#FFF3C4"><circle cx="16" cy="18" r="1.8"/><circle cx="110" cy="14" r="1.6"/><circle cx="118" cy="46" r="1.4"/><circle cx="12" cy="56" r="1.4"/></g>
{sparkle(24, 36, 4, "#FFF3C4")}{sparkle(104, 30, 3.6, "#FFF3C4")}
<circle cx="64" cy="52" r="40" fill="#FFE29A" opacity=".25"/>
<circle cx="64" cy="52" r="32" fill="#F2B860" {W(3.4)}/>
<circle cx="64" cy="52" r="24" fill="#F7CF83"/>
<g fill="#6B3A2A"><ellipse cx="46" cy="40" rx="3.4" ry="2.4"/><ellipse cx="82" cy="42" rx="3" ry="2.2"/><ellipse cx="78" cy="68" rx="3.2" ry="2.4"/><ellipse cx="50" cy="70" rx="2.8" ry="2"/></g>
<path d="M50 50 Q55 54 60 50 M68 50 Q73 54 78 50" fill="none" {W(2.4)}/>
<path d="M58 60 Q64 64 70 60" fill="none" {W(2)}/>
{BL(48, 58)}{BL(80, 58)}
<g {W(2.6)}>
<path d="M4 128 L4 100 L20 88 L36 100 L36 128Z" fill="#3A4670"/>
<path d="M34 128 L34 94 L56 94 L56 128Z" fill="#46548A"/>
<path d="M54 128 L54 104 L72 90 L90 104 L90 128Z" fill="#3A4670"/>
<path d="M88 128 L88 96 L124 96 L124 128Z" fill="#46548A"/></g>
<g fill="#FFD66B"><rect x="14" y="106" width="8" height="8" rx="1"/><rect x="96" y="104" width="7" height="7" rx="1"/></g>
<g fill="#26304F"><rect x="40" y="102" width="7" height="7" rx="1"/><rect x="66" y="110" width="8" height="8" rx="1"/><rect x="110" y="114" width="7" height="7" rx="1"/></g>
''')

# 7. Хинкали-Gали! (Дмитровское ш., 100): хинкали в шарфе мчится с горки на ватрушке
add("cafe-hinkali-gali-dmitrovskoe-100",
    "пузатый хинкали со складочками и хвостиком-узелком, в полосатом красно-белом шарфе",
    "мчится вниз по снежной горке на красной надувной ватрушке-тюбинге, шарф и хвостик развеваются на ветру",
    "zv_snow", f'''
<path d="M0 60 Q60 70 128 118 L128 128 L0 128Z" fill="#FFFFFF" {W(3)}/>
<path d="M10 74 L22 76 M28 80 L40 84" stroke="#B7DDF3" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="72" cy="98" rx="36" ry="13" fill="#E5383B" {W(3.2)} transform="rotate(22 72 98)"/>
<ellipse cx="72" cy="96" rx="16" ry="5" fill="#9E1F24" transform="rotate(22 72 96)"/>
<path d="M44 84 Q40 54 62 46 Q84 40 96 62 Q102 80 92 92 Q66 100 44 84Z" fill="#F6EEDC" {W(3.2)}/>
<path d="M58 48 Q62 60 60 76 M70 46 Q72 60 74 78 M82 50 Q82 64 86 80" fill="none" stroke="#D8C7A4" stroke-width="2.2" stroke-linecap="round"/>
<path d="M62 46 Q60 34 54 30 Q62 26 70 34 Q72 40 70 46Z" fill="#EADBB8" {W(2.6)}/>
<path d="M54 30 L40 22" stroke="#EADBB8" stroke-width="5" stroke-linecap="round"/>
<path d="M54 30 L40 22" fill="none" {W(1.6)} opacity=".6"/>
<path d="M50 66 Q72 72 96 66 L96 74 Q72 80 50 74Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M56 67 L56 76 M66 68 L66 78 M76 69 L76 78 M86 68 L86 77" stroke="#E5383B" stroke-width="3.4"/>
<path d="M52 70 Q34 64 22 70 L22 78 Q36 74 52 76Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M30 68 L30 77 M40 68 L40 76" stroke="#E5383B" stroke-width="3.4"/>
{eye(66, 58, 0.75)}{eye(80, 58, 0.75)}
<path d="M70 82 Q74 86 78 82Z" fill="#E24B5B" {W(1.6)}/>
{BL(60, 82)}{BL(90, 80)}
<path d="M14 40 L24 42 M8 50 L22 52 M18 30 L28 32" stroke="#8CC4E8" stroke-width="2.4" stroke-linecap="round"/>
<g fill="#FFFFFF" {W(1.2)}><circle cx="104" cy="22" r="3"/><circle cx="114" cy="40" r="2.4"/><circle cx="88" cy="16" r="2"/></g>
''')

# 8. Тануки (Дмитровское ш., 108Б): нигири с креветкой делает трюк, как скейтер, на рампе
add("cafe-tanuki-dmitrovskoe-108b",
    "нигири с полосатой розово-белой креветкой, лежащей на белом рисовом брусочке",
    "делает трюк в прыжке над деревянной рампой, как скейтер, рисовый брусочек вместо доски, ручки раскинуты",
    "zv_ramp", f'''
<path d="M0 128 L0 96 Q30 96 40 128Z" fill="#C98A4E" {W(3)}/>
<path d="M128 128 L128 96 Q98 96 88 128Z" fill="#C98A4E" {W(3)}/>
<path d="M6 104 L22 106 M106 106 L122 104" stroke="#9A6532" stroke-width="2"/>
<path d="M30 92 Q22 84 26 76 M100 92 Q108 84 104 76" fill="none" stroke="#E8664A" stroke-width="2.4" stroke-linecap="round" opacity=".7"/>
<g transform="rotate(-12 64 64)">
<rect x="28" y="66" width="72" height="24" rx="11" fill="#FFFFFF" {W(3.2)}/>
<g fill="#EDEDED"><ellipse cx="44" cy="80" rx="4" ry="2.4"/><ellipse cx="60" cy="84" rx="4" ry="2.4"/><ellipse cx="76" cy="80" rx="4" ry="2.4"/><ellipse cx="88" cy="84" rx="3.4" ry="2"/></g>
<rect x="76" y="60" width="13" height="32" rx="2" fill="#2E4A3A" {W(2.2)}/>
<path d="M24 66 Q22 44 50 40 Q82 36 100 50 L108 44 L112 58 L104 62 Q80 70 24 66Z" fill="#FF9E80" {W(3.2)}/>
<path d="M40 44 Q42 54 38 64 M54 41 Q56 53 52 65 M68 40 Q70 52 66 65 M82 42 Q84 54 80 64" fill="none" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>
<path d="M104 48 L112 40 L114 50 L120 54 L110 58Z" fill="#E2552E" {W(2.4)}/>
</g>
{eye(48, 58, 0.8)}{eye(64, 56, 0.8)}
<path d="M52 66 Q57 70 62 65" fill="none" {W(1.8)}/>
{BL(42, 66)}{BL(72, 62)}
<path d="M30 70 Q16 60 12 46 M96 54 Q108 40 118 36" fill="none" {W(3)}/>
{sparkle(20, 22, 5)}{sparkle(64, 14, 3.6)}{sparkle(104, 18, 4)}
''')


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    if not sys.argv[1:]:
        reg = os.path.join(OUT, "subjects.txt")
        have = {l.split(" — ", 1)[0] for l in open(reg, encoding="utf-8")}
        with open(reg, "a", encoding="utf-8") as f:
            for pid in ICONS:
                if pid not in have:
                    f.write(f"{pid} — герой: {SUBJ[pid][0]} | сцена: {SUBJ[pid][1]}\n")
    print("svg:", len(ids))
