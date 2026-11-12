"""Иконки робота cafes, 2026-11-12 (14 UTC). Каждая придумана отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1112r.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
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
    "zr_slide": ("#F1FFF6", "#5FC08C"),
    "zr_zaton": ("#E6F7FF", "#3E9AD6"),
    "zr_flour": ("#FFF6EC", "#D9A46A"),
    "zr_pines": ("#FFFBEA", "#9CC76A"),
    "zr_loft": ("#FFF1E6", "#B86B4B"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Тануки (Рязанский пр-т, 12; детская комната): рисовый крекер сэмбэй съезжает с горки игровой
add("cafe-tanuki-ryazansky-12",
    "круглый японский рисовый крекер сэмбэй, обёрнутый полоской нори",
    "с восторгом съезжает с жёлтой волнистой горки детской игровой, подняв обе ручки вверх",
    "zr_slide", f'''
<rect x="92" y="34" width="8" height="90" fill="#E2362F" {W(2.4)}/>
<rect x="78" y="34" width="22" height="8" fill="#E2362F" {W(2.4)}/>
<path d="M86 42 Q70 52 70 66 Q70 80 50 88 Q30 96 24 118 L8 118 Q14 88 38 78 Q56 70 58 58 Q60 44 82 34Z" fill="#FFD23F" {W(3)}/>
<path d="M78 42 Q62 50 62 62 M48 82 Q28 92 20 112" fill="none" stroke="#F0A800" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="50" cy="64" r="24" fill="#E6B26A" {W(3.2)}/>
<circle cx="50" cy="64" r="24" fill="none" stroke="#C98B3E" stroke-width="2" stroke-dasharray="2 6"/>
<path d="M28 74 L72 74 Q68 84 50 88 Q32 84 28 74Z" fill="#1F3A2B" {W(2.4)}/>
<circle cx="40" cy="54" r="1.6" fill="#B07A34"/><circle cx="62" cy="50" r="1.6" fill="#B07A34"/>
{eye(43, 56, 0.8)}{eye(57, 56, 0.8)}
<path d="M45 62 Q50 69 55 62Z" fill="#E24B5B" {W(1.8)}/>
{BL(37, 63)}{BL(63, 63)}
<path d="M30 52 L18 32 M70 52 L80 30" {W(3.4)}/>
<circle cx="18" cy="31" r="3.4" fill="#E6B26A" {W(2)}/><circle cx="80" cy="29" r="3.4" fill="#E6B26A" {W(2)}/>
<path d="M14 92 Q8 96 6 104 M28 96 Q22 102 22 110" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
{sparkle(108, 22, 5)}{sparkle(30, 18, 4)}
''')

# 2. Тануки (ул. Маршала Катукова, Строгино — у Строгинского затона): запечённый ролл на виндсёрфе
add("cafe-tanuki-katukova-23",
    "запечённый японский ролл с румяной сырной шапочкой, подпалённой сверху",
    "мчится на виндсёрфинге с оранжевым парусом по синей воде Строгинского затона, оставляя пенный след",
    "zr_zaton", f'''
<rect x="0" y="92" width="128" height="40" fill="#2F7FC4"/>
<path d="M0 92 Q16 86 32 92 Q48 98 64 92 Q80 86 96 92 Q112 98 128 92" fill="none" stroke="#BFE6FF" stroke-width="3"/>
<path d="M18 104 Q30 100 42 106 M76 112 Q90 108 104 114" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
<path d="M30 98 L104 94 Q112 96 106 100 L34 104Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M78 96 L80 14" {W(3)}/>
<path d="M80 16 Q112 40 108 86 L82 86Z" fill="#FF8A2B" {W(3)}/>
<path d="M84 34 Q100 46 102 70" fill="none" stroke="#FFC08A" stroke-width="3" stroke-linecap="round"/>
<path d="M58 60 L80 56" {W(3)}/>
<path d="M36 94 L36 60 Q36 48 50 48 Q64 48 64 60 L64 94Z" fill="#FFFFFF" {W(3)}/>
<path d="M36 70 L64 70 L64 94 L36 94Z" fill="#1F3A2B" {W(2.6)}/>
<path d="M34 60 Q34 44 50 44 Q66 44 66 60 Q60 56 56 60 Q50 54 44 60 Q38 56 34 60Z" fill="#FFB547" {W(2.8)}/>
<path d="M42 50 Q46 48 48 50 M56 49 Q59 48 61 51" fill="none" stroke="#C7621E" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="50" cy="82" r="5" fill="#FF8E6E" {W(1.6)}/>
{eye(44, 64, 0.75)}{eye(56, 64, 0.75)}
<path d="M46 68 Q50 71 54 68" fill="none" {W(1.8)}/>
<path d="M14 98 Q8 94 4 96 M20 106 Q12 106 8 110" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>
{sparkle(24, 24, 5)}
''')

# 3. Кухня Полли (Строгино; детские мастер-классы): мини-пицца-рожица, собранная ребёнком
add("cafe-kukhnya-polli-strogino",
    "детская мини-пицца, на которой ребёнок выложил рожицу: глаза-оливки, нос-помидорка черри, улыбка из колбаски",
    "только что собрана на детском мастер-классе и лежит на столе, присыпанном мукой, рядом два отпечатка детских ладошек",
    "zr_flour", f'''
<rect x="0" y="84" width="128" height="44" fill="#E9C9A0"/>
<g fill="#FFFFFF" opacity=".85">
<ellipse cx="22" cy="104" rx="8" ry="10"/><ellipse cx="13" cy="96" rx="2.6" ry="5" transform="rotate(-30 13 96)"/><ellipse cx="18" cy="91" rx="2.6" ry="5.4" transform="rotate(-10 18 91)"/><ellipse cx="25" cy="90" rx="2.6" ry="5.4"/><ellipse cx="31" cy="94" rx="2.4" ry="5" transform="rotate(20 31 94)"/>
<ellipse cx="106" cy="106" rx="8" ry="10"/><ellipse cx="115" cy="98" rx="2.6" ry="5" transform="rotate(30 115 98)"/><ellipse cx="110" cy="93" rx="2.6" ry="5.4" transform="rotate(10 110 93)"/><ellipse cx="103" cy="92" rx="2.6" ry="5.4"/><ellipse cx="97" cy="96" rx="2.4" ry="5" transform="rotate(-20 97 96)"/>
</g>
<circle cx="64" cy="68" r="40" fill="#E8A75A" {W(3.2)}/>
<circle cx="64" cy="68" r="33" fill="#E2483A" {W(2.2)}/>
<path d="M36 60 Q40 48 50 44 M80 42 Q92 50 94 64 M40 86 Q48 96 60 98" fill="none" stroke="#FFE59A" stroke-width="5" stroke-linecap="round"/>
<circle cx="50" cy="58" r="7" fill="#2E2A30" {W(2)}/><circle cx="50" cy="58" r="2.4" fill="#E2483A"/>
<circle cx="78" cy="58" r="7" fill="#2E2A30" {W(2)}/><circle cx="78" cy="58" r="2.4" fill="#E2483A"/>
<circle cx="48" cy="56" r="1.6" fill="#fff"/><circle cx="76" cy="56" r="1.6" fill="#fff"/>
<circle cx="64" cy="70" r="6" fill="#FF3B3B" {W(2)}/><path d="M62 64 L64 61 L66 64" stroke="#3E8E3A" stroke-width="2" fill="none"/>
<path d="M46 80 Q64 96 82 80" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M46 80 Q64 96 82 80" fill="none" stroke="#F08A8A" stroke-width="5.5" stroke-linecap="round"/>
<circle cx="52" cy="85" r="1.2" fill="#fff"/><circle cx="64" cy="89" r="1.2" fill="#fff"/><circle cx="76" cy="85" r="1.2" fill="#fff"/>
{sparkle(104, 24, 5)}{sparkle(24, 28, 4)}
''')

# 4. Osteria Mario (Немчиновка, у леса; детская комната): трёхцветный брикет спумони гуляет среди сосен
add("cafe-osteria-nemchinovka",
    "итальянский трёхцветный брикет мороженого спумони — фисташковый, ванильный и клубничный слой — на палочке",
    "шагает по лесной тропинке среди высоких сосен подмосковного посёлка, весело размахивая ручками",
    "zr_pines", f'''
<path d="M0 100 Q64 88 128 100 L128 128 L0 128Z" fill="#7DB65A"/>
<path d="M50 128 Q58 108 64 96 Q70 108 80 128Z" fill="#E7D3A6"/>
<rect x="12" y="40" width="7" height="64" fill="#A0522D" {W(2)}/><path d="M2 60 L16 22 L30 60Z M4 78 L16 44 L28 78Z" fill="#3E8E4E" {W(2.2)}/>
<rect x="108" y="36" width="7" height="68" fill="#A0522D" {W(2)}/><path d="M98 56 L112 18 L126 56Z M100 76 L112 40 L124 76Z" fill="#3E8E4E" {W(2.2)}/>
<rect x="61" y="88" width="6" height="18" rx="2" fill="#E8C690" {W(2)}/>
<path d="M54 106 L50 116 M74 106 L78 116" {W(3.2)}/>
<rect x="40" y="26" width="48" height="64" rx="9" fill="#F2A3B4" {W(3.2)}/>
<rect x="40" y="26" width="48" height="22" rx="9" fill="#A8D47A" {W(3)}/>
<rect x="41.5" y="46" width="45" height="22" fill="#FFF4D6" stroke="none"/>
<path d="M40 46 L88 46 M40 68 L88 68" {W(3)}/>
<circle cx="50" cy="34" r="1.8" fill="#5E8E3A"/><circle cx="76" cy="38" r="1.8" fill="#5E8E3A"/><circle cx="56" cy="80" r="1.6" fill="#C9506A"/><circle cx="76" cy="78" r="1.6" fill="#C9506A"/>
{eye(56, 56, 0.85)}{eye(72, 56, 0.85)}
<path d="M58 62 Q64 67 70 62" fill="none" {W(2)}/>
{BL(48, 61)}{BL(80, 61)}
<path d="M40 58 L28 46 M88 58 L100 70" {W(3.2)}/>
{sparkle(64, 14, 5)}
''')

# 5. «Лофт» (Люберцы, пиццерия с игровой): чесночный хлебный узелок на кирпичной стене лофта
add("cafe-loft-lyubertsy-mitrofanova",
    "пухлый чесночный хлебный узелок, посыпанный зеленью",
    "сидит на выступе красной кирпичной стены лофта под провисшей гирляндой тёплых лампочек и болтает ножками",
    "zr_loft", f'''
<g stroke="#9A4A32" stroke-width="2" fill="#C8644A">
<rect x="0" y="70" width="30" height="14"/><rect x="30" y="70" width="34" height="14"/><rect x="64" y="70" width="34" height="14"/><rect x="98" y="70" width="30" height="14"/>
<rect x="-8" y="84" width="30" height="14"/><rect x="22" y="84" width="34" height="14"/><rect x="56" y="84" width="34" height="14"/><rect x="90" y="84" width="40" height="14"/>
<rect x="0" y="98" width="30" height="14"/><rect x="30" y="98" width="34" height="14"/><rect x="64" y="98" width="34" height="14"/><rect x="98" y="98" width="30" height="14"/>
<rect x="-8" y="112" width="30" height="16"/><rect x="22" y="112" width="34" height="16"/><rect x="56" y="112" width="34" height="16"/><rect x="90" y="112" width="40" height="16"/>
</g>
<rect x="0" y="64" width="128" height="8" fill="#8A8A8A" {W(2.4)}/>
<path d="M4 14 Q64 40 124 14" fill="none" stroke="#3B3355" stroke-width="2"/>
<g fill="#FFD966" stroke="#3B3355" stroke-width="1.6"><circle cx="20" cy="22" r="4.5"/><circle cx="42" cy="29" r="4.5"/><circle cx="64" cy="31" r="4.5"/><circle cx="86" cy="29" r="4.5"/><circle cx="108" cy="22" r="4.5"/></g>
<path d="M54 74 L50 90 M74 74 L78 90" {W(3.2)}/>
<ellipse cx="48" cy="92" rx="5" ry="3" fill="{O}"/><ellipse cx="80" cy="92" rx="5" ry="3" fill="{O}"/>
<path d="M34 58 Q30 38 48 36 Q56 30 66 38 Q84 32 92 46 Q100 60 86 68 L42 68 Q32 66 34 58Z" fill="#F0C27A" {W(3.2)}/>
<path d="M48 40 Q60 54 82 46 M44 60 Q58 50 70 62" fill="none" stroke="#C98B3E" stroke-width="3" stroke-linecap="round"/>
<g fill="#4E9A3A"><circle cx="54" cy="44" r="1.6"/><circle cx="70" cy="42" r="1.6"/><circle cx="80" cy="56" r="1.6"/><circle cx="46" cy="52" r="1.6"/><circle cx="62" cy="64" r="1.4"/></g>
{eye(56, 52, 0.8)}{eye(72, 52, 0.8)}
<path d="M59 58 Q64 62 69 58" fill="none" {W(1.8)}/>
{BL(48, 58)}{BL(80, 58)}
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
