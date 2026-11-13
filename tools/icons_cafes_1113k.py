"""Иконки робота cafes, 2026-11-13 (16 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1113k.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
BL = lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="3.6" ry="2.1" fill="#FF7FA8" opacity=".7"/>'
draw_icons.BG.update({
    "kk_rosecoffee": ("#FBE3DC", "#C97B6E"),
    "kk_limejungle": ("#EFFAD0", "#9CC43A"),
    "kk_deepteal": ("#D2F2F0", "#2E8C8A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Сливки (кофейня, Старая Купавна): сифон для сливок наклонился над чашкой и выдавил башню сливок
add("cafe-slivki-staraya-kupavna",
    "серебристый сифон для взбитых сливок с красной насадкой-звёздочкой и мордашкой на боку",
    "наклонился над розовой чашкой кофе и выдавил на неё высоченную башню-спираль из белых сливок, сам удивился",
    "kk_rosecoffee", f'''
<g transform="rotate(-38 82 46)">
<rect x="66" y="10" width="32" height="56" rx="14" fill="#D9E1E8" {W(3.2)}/>
<rect x="71" y="14" width="5" height="46" rx="2.5" fill="#FFFFFF" opacity=".8"/>
<rect x="64" y="56" width="36" height="8" rx="4" fill="#9AA7B4" {W(2.4)}/>
<path d="M76 66 L88 66 L85 78 L79 78Z" fill="#E2403E" {W(2.4)}/>
{eye(76, 32, 0.9)}{eye(89, 32, 0.9)}
<ellipse cx="82" cy="44" rx="3.6" ry="4.4" fill="{O}"/>
</g>
<path d="M30 88 L30 112 Q30 120 40 120 L74 120 Q84 120 84 112 L84 88Z" fill="#FF9DB5" {W(3.2)}/>
<path d="M84 94 Q98 94 96 104 Q94 112 84 110" fill="none" {W(3)}/>
<ellipse cx="57" cy="88" rx="27" ry="6" fill="#8A5A3C" {W(3)}/>
<path d="M30 88 Q24 78 36 74 Q30 62 44 60 Q42 50 54 50 Q56 40 64 44 Q74 50 68 58 Q80 62 76 72 Q88 76 82 88 Q57 96 30 88Z" fill="#FFFDF8" {W(3)}/>
<path d="M38 80 Q56 86 74 80 M46 66 Q58 70 68 64" fill="none" stroke="#E8D9CC" stroke-width="2.6" stroke-linecap="round"/>
<g fill="#FFFFFF" stroke="{O}" stroke-width="1.6"><circle cx="70" cy="46" r="2.4"/><circle cx="74" cy="40" r="1.8"/></g>
{sparkle(20, 40, 5)}{sparkle(110, 96, 4)}{sparkle(30, 22, 3)}
''')

# 2. Динозаврия (кафе с детской комнатой, Зеленоград): стегозаврик облизывает леденец-спираль
add("cafe-dinozavriya-zelenograd",
    "сиреневый малыш-стегозавр с ромбиками-пластинами цвета мяты вдоль спины",
    "стоит на четырёх лапках и, зажмурившись от счастья, лижет розовым языком огромный радужный леденец-спираль на палочке",
    "kk_limejungle", f'''
<path d="M26 76 L18 62 L32 66 L30 50 L42 60 L46 44 L56 56 L62 44 L66 60" fill="#7FE0C2" {W(2.8)}/>
<path d="M14 98 Q2 100 4 90 Q12 94 20 88" fill="#B79BF0" {W(3)}/>
<path d="M16 96 Q14 72 44 64 Q66 60 74 76 Q78 96 64 102 Q40 108 16 96Z" fill="#B79BF0" {W(3.2)}/>
<path d="M24 98 L24 114 M38 102 L38 116 M54 102 L54 116 M66 98 L66 112" {W(9)}/>
<path d="M24 98 L24 114 M38 102 L38 116 M54 102 L54 116 M66 98 L66 112" stroke="#B79BF0" stroke-width="5.4" stroke-linecap="round"/>
<circle cx="78" cy="74" r="17" fill="#B79BF0" {W(3.2)}/>
<path d="M68 72 Q72 68 76 72 M80 72 Q84 68 88 72" fill="none" {W(2.6)}/>
{BL(70, 80)}{BL(88, 80)}
<path d="M84 82 Q90 84 92 80" fill="none" {W(2.2)}/>
<path d="M90 80 Q98 78 98 72 Q92 72 89 77Z" fill="#FF6F9A" {W(2)}/>
<line x1="106" y1="72" x2="110" y2="118" {W(6)}/><line x1="106" y1="72" x2="110" y2="118" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
<circle cx="104" cy="52" r="20" fill="#FFE066" {W(3.2)}/>
<path d="M104 52 m0 -3 a3 3 0 1 1 -3 3 a7 7 0 1 1 7 7 a11 11 0 1 1 -11 -11 a15 15 0 1 1 15 15" fill="none" stroke="#FF5C8A" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="104" cy="52" r="20" fill="none" {W(3.2)}/>
{sparkle(30, 26, 5)}{sparkle(76, 30, 3.5)}
''')

# 3. Додо Пицца (Щербинка): нож-колесо для пиццы катится по пицце, как моноцикл
add("cafe-dodo-shcherbinka-zheleznodorozhnaya",
    "роликовый нож для пиццы — блестящее стальное колесо с красной ручкой и мордашкой на втулке",
    "лихо катится, как цирковой моноцикл, по огромной пицце с пепперони и оставляет за собой ровный разрез",
    "kk_deepteal", f'''
<ellipse cx="64" cy="100" rx="58" ry="22" fill="#E9A44A" {W(3.2)}/>
<ellipse cx="64" cy="100" rx="48" ry="16" fill="#FFD45E"/>
<path d="M18 100 Q22 92 30 96" fill="none" stroke="#E07B2A" stroke-width="2" stroke-linecap="round"/>
<g fill="#D8343E" stroke="#8E1E26" stroke-width="1.4"><ellipse cx="34" cy="98" rx="6" ry="3.6"/><ellipse cx="54" cy="110" rx="6" ry="3.6"/><ellipse cx="92" cy="106" rx="6" ry="3.6"/><ellipse cx="96" cy="92" rx="5" ry="3"/></g>
<path d="M14 104 L60 104" stroke="{O}" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="0"/>
<path d="M16 108 Q30 104 44 106" fill="none" stroke="#FFFFFF" stroke-width="1.6" opacity=".7"/>
<circle cx="74" cy="72" r="30" fill="#DCE4EA" {W(3.4)}/>
<circle cx="74" cy="72" r="24" fill="#F4F7F9"/>
<path d="M56 56 A24 24 0 0 1 90 54" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" opacity=".9"/>
<circle cx="74" cy="72" r="14" fill="#C9D3DB" {W(2.6)}/>
{eye(69, 70, 0.85)}{eye(79, 70, 0.85)}
{BL(64, 77)}{BL(84, 77)}
<path d="M70 78 Q74 82 78 78" fill="none" {W(2.2)}/>
<path d="M74 58 L100 22" {W(9)}/><path d="M74 58 L100 22" stroke="#E2403E" stroke-width="5" stroke-linecap="round"/>
<path d="M96 26 L104 16" {W(11)}/><path d="M96 26 L104 16" stroke="#E2403E" stroke-width="7" stroke-linecap="round"/>
<path d="M30 56 L44 56 M26 66 L40 66 M32 76 L42 76" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity=".85"/>
{sparkle(22, 30, 5)}{sparkle(112, 52, 3.5)}
''')


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(ICONS[pid])
    if not sys.argv[1:]:
        p = os.path.join(OUT, "subjects.txt")
        have = {l.split(" — ", 1)[0] for l in open(p, encoding="utf-8")}
        with open(p, "a", encoding="utf-8") as f:
            for pid in ids:
                if pid not in have:
                    h, sc = SUBJ[pid]
                    f.write(f"{pid} — герой: {h} | сцена: {sc}\n")
    print("svg", len(ids))
