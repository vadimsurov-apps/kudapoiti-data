"""Иконки робота cafes, 2026-11-14 (07–09 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1114e.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
BL = lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="3.4" ry="2" fill="#FF7FA8" opacity=".75"/>'
draw_icons.BG.update({
    "ke_dawn": ("#FFF1E0", "#E86A4A"),
    "ke_azure": ("#EAF7FF", "#3F8FE0"),
    "ke_river": ("#E9FFF6", "#2FA58A"),
    "ke_berry": ("#FFF0F4", "#D9467A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Тануки в Солнцеве (3 этаж, панорамные окна): желток на рисе сияет, как солнце, в панорамном окне над многоэтажками
add("cafe-tanuki-bogdanova-52a",
    "чёрная лаковая пиала с горкой белого риса, на вершине которой лежит круглый желток-солнышко с мордашкой",
    "желток сияет лучами, как восходящее солнце, на фоне большого панорамного окна, за которым виднеются крыши многоэтажек",
    "ke_dawn", f"""
<rect x="10" y="14" width="108" height="78" rx="6" fill="#FFE7B8" {W(3)}/>
<path d="M64 14 L64 92 M10 54 L118 54" stroke="#3B3355" stroke-width="2.6" opacity=".55"/>
<g fill="#B98CD9" {W(2.2)}>
<path d="M12 92 L12 66 L28 66 L28 92Z"/><path d="M30 92 L30 58 L46 58 L46 92Z"/>
<path d="M84 92 L84 62 L100 62 L100 92Z"/><path d="M102 92 L102 70 L116 70 L116 92Z"/>
</g>
<g fill="#FFF3A6"><rect x="16" y="72" width="4" height="4"/><rect x="22" y="80" width="4" height="4"/><rect x="34" y="64" width="4" height="4"/><rect x="40" y="76" width="4" height="4"/><rect x="88" y="68" width="4" height="4"/><rect x="94" y="80" width="4" height="4"/><rect x="106" y="76" width="4" height="4"/></g>
<g stroke="#FFB21E" stroke-width="4" stroke-linecap="round">
<path d="M64 22 L64 30"/><path d="M38 34 L44 40"/><path d="M90 34 L84 40"/><path d="M28 56 L36 57"/><path d="M100 56 L92 57"/>
</g>
<path d="M30 92 Q30 120 64 120 Q98 120 98 92Z" fill="#2B2230" {W(3.2)}/>
<path d="M36 98 Q64 104 92 98" fill="none" stroke="#D2343F" stroke-width="3"/>
<path d="M26 92 Q30 64 64 62 Q98 64 102 92Z" fill="#FFFFFF" {W(3)}/>
<g fill="#E9E4EF"><ellipse cx="44" cy="84" rx="3" ry="1.6"/><ellipse cx="58" cy="76" rx="3" ry="1.6"/><ellipse cx="80" cy="82" rx="3" ry="1.6"/><ellipse cx="88" cy="88" rx="3" ry="1.6"/></g>
<circle cx="64" cy="58" r="17" fill="#FFB21E" {W(3)}/>
<ellipse cx="58" cy="52" rx="5" ry="3" fill="#FFE07A"/>
{eye(58, 58, .8)}{eye(70, 58, .8)}
<path d="M59 65 Q64 70 69 65" fill="none" {W(2.4)}/>
{BL(53, 64)}{BL(75, 64)}
<path d="M84 74 L90 70 M88 80 L95 78" stroke="#2E7D32" stroke-width="3" stroke-linecap="round"/>
""")

# 2. Сыроварня на Небесном бульваре: скаморца-грушка на бечёвке летит в небе, как воздушный шар с корзинкой
add("cafe-syrovarnya-nebesny-1",
    "сыр скаморца — светлая грушка, перетянутая бечёвкой у макушки, с мордашкой",
    "парит высоко в небе, как воздушный шар, а снизу на бечёвке висит маленькая плетёная корзинка; вокруг пушистые облака",
    "ke_azure", f"""
<path d="M8 96 Q8 84 22 86 Q26 76 38 80 Q46 74 54 82 Q60 90 52 96Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M86 30 Q86 22 96 23 Q100 16 110 20 Q120 20 120 30Z" fill="#FFFFFF" {W(2.6)}/>
<path d="M64 14 Q60 22 64 26 Q68 22 64 14Z" fill="#E8D49A" {W(2.6)}/>
<path d="M58 26 L70 26" stroke="#A86B3C" stroke-width="3.4" stroke-linecap="round"/>
<path d="M64 26 Q38 34 36 60 Q36 86 64 88 Q92 86 92 60 Q90 34 64 26Z" fill="#F8E3A8" {W(3.2)}/>
<path d="M64 28 Q46 40 46 62" fill="none" stroke="#FFF6D6" stroke-width="5" stroke-linecap="round"/>
<path d="M44 46 Q64 54 84 46" fill="none" stroke="#A86B3C" stroke-width="2.6"/>
{eye(56, 64, .9)}{eye(72, 64, .9)}
<path d="M58 72 Q64 78 70 72" fill="none" {W(2.6)}/>
{BL(49, 71)}{BL(79, 71)}
<path d="M50 84 L54 104 M78 84 L74 104" stroke="#A86B3C" stroke-width="2.4"/>
<path d="M50 104 L78 104 L75 118 L53 118Z" fill="#C98A4B" {W(2.8)}/>
<path d="M52 110 L76 110 M58 104 L58 118 M64 104 L64 118 M70 104 L70 118" stroke="#8C5A2B" stroke-width="1.8"/>
{sparkle(26, 40, 5)}{sparkle(106, 72, 4)}
""")

# 3. Ла Рива («берег» по-итальянски, у Москвы-реки): ракушка вонголе в канотье плывёт в лодке-чиабатте, гребёт веточкой петрушки
add("cafe-la-riva-beregovoy-3",
    "ракушка вонголе с приоткрытыми полосатыми створками в соломенной шляпе-канотье с красной лентой",
    "плывёт по реке в лодке из половинки чиабатты, загребая веточкой петрушки вместо весла",
    "ke_river", f"""
<path d="M0 100 Q16 94 32 100 Q48 106 64 100 Q80 94 96 100 Q112 106 128 100 L128 128 L0 128Z" fill="#4FB7E0"/>
<path d="M8 112 Q20 108 32 112 M84 114 Q96 110 108 114" fill="none" stroke="#DFF6FF" stroke-width="2.6" stroke-linecap="round"/>
<path d="M16 84 Q20 104 64 104 Q108 104 112 84Z" fill="#E6B26A" {W(3.2)}/>
<path d="M16 84 Q64 92 112 84" fill="none" stroke="#F7F0DE" stroke-width="5"/>
<g fill="#C58B44"><ellipse cx="40" cy="96" rx="3" ry="1.6"/><ellipse cx="64" cy="98" rx="3" ry="1.6"/><ellipse cx="88" cy="96" rx="3" ry="1.6"/></g>
<path d="M40 82 Q40 54 64 52 Q88 54 88 82Z" fill="#E9D8C4" {W(3)}/>
<path d="M48 80 Q50 62 64 56 M64 56 L64 80 M80 80 Q78 62 64 56" fill="none" stroke="#B89B7E" stroke-width="2"/>
{eye(57, 68, .85)}{eye(71, 68, .85)}
<path d="M60 75 Q64 79 68 75" fill="none" {W(2.2)}/>
{BL(51, 74)}{BL(77, 74)}
<ellipse cx="64" cy="52" rx="24" ry="5" fill="#F2D27A" {W(2.8)}/>
<path d="M50 50 L52 36 L76 36 L78 50Z" fill="#F2D27A" {W(2.8)}/>
<path d="M51 45 L77 45 L78 50 L50 50Z" fill="#D63A3A"/>
<path d="M92 66 L114 104" stroke="#3E8E2E" stroke-width="3.4" stroke-linecap="round"/>
<g fill="#5DBB3F" {W(2)}><path d="M92 66 Q84 58 90 54 Q96 58 92 66Z"/><path d="M95 72 Q104 66 104 74 Q98 78 95 72Z"/><path d="M90 62 Q82 66 84 72 Q90 70 90 62Z"/></g>
<path d="M84 76 Q88 74 92 70" fill="none" {W(2.4)}/>
{sparkle(24, 34, 5)}{sparkle(108, 28, 4)}
""")

# 4. Неваляшка (семейное кафе, пицца, игровая с горкой): кусок пиццы с ростбифом качается в красной люльке-неваляшке
add("cafe-nevalyashka-nebesny-1",
    "треугольный кусок пиццы с ломтиками розового ростбифа и зелёными листиками рукколы",
    "сидит в круглой красной люльке-неваляшке с белым донышком, раскачивается из стороны в сторону и болтает ножками",
    "ke_berry", f"""
<path d="M10 112 Q64 122 118 112" fill="none" stroke="#FFFFFF" stroke-width="3" opacity=".6"/>
<g transform="rotate(-10 64 86)">
<path d="M28 74 Q28 116 64 116 Q100 116 100 74Z" fill="#E53950" {W(3.2)}/>
<path d="M40 106 Q64 116 88 106 Q86 114 64 114 Q42 114 40 106Z" fill="#FFFFFF"/>
<g fill="#FFD54A" {W(1.8)}><circle cx="44" cy="92" r="4"/><circle cx="84" cy="92" r="4"/><circle cx="64" cy="98" r="4"/></g>
<path d="M44 40 L84 40 Q86 40 85 43 L66 80 Q64 84 62 80 L43 43 Q42 40 44 40Z" fill="#FFCF5A" {W(3)}/>
<path d="M42 36 Q64 30 86 36 Q88 42 84 44 Q64 38 44 44 Q40 42 42 36Z" fill="#D9934A" {W(3)}/>
<g fill="#E58C8C" stroke="#B85A5A" stroke-width="1.4"><path d="M50 48 Q56 46 58 52 Q54 56 50 48Z"/><path d="M68 50 Q74 48 76 52 Q72 58 68 50Z"/></g>
<g fill="#4FAE3B"><path d="M58 60 Q62 56 66 60 Q62 62 58 60Z"/><path d="M48 46 Q50 42 54 44Z"/><path d="M76 46 Q80 44 80 48Z"/></g>
{eye(57, 54, .75)}{eye(70, 54, .75)}
<path d="M60 62 Q64 66 68 62" fill="none" {W(2.2)}/>
<path d="M54 74 L48 86 M74 74 L80 86" fill="none" {W(3)}/>
<g fill="#FF8FAE" {W(2)}><ellipse cx="47" cy="88" rx="4" ry="2.6"/><ellipse cx="81" cy="88" rx="4" ry="2.6"/></g>
</g>
<path d="M12 70 Q8 84 14 96 M116 70 Q120 84 114 96" fill="none" stroke="#FFFFFF" stroke-width="3.4" stroke-linecap="round"/>
{sparkle(22, 30, 5)}{sparkle(106, 26, 4)}
""")


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    if not sys.argv[1:]:
        reg = os.path.join(OUT, "subjects.txt")
        have = open(reg).read()
        with open(reg, "a") as f:
            for pid in ids:
                if pid + " —" not in have:
                    f.write(f"{pid} — герой: {SUBJ[pid][0]} | сцена: {SUBJ[pid][1]}\n")
    print("svg:", len(ids))
