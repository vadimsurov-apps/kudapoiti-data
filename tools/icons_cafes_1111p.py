"""Иконки робота cafes, 2026-11-11 (17 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана отдельно,
герои сверены с subjects.txt (окономияки, шаверма, пити, кастелла, рибай, харумаки, этажерка с пирожными,
суп в хлебной чаше, пицца-шар, кубдари на батуте — таких героев/сцен в реестре нет).
Запуск: python3 tools/icons_cafes_1111p.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "p_teppan": ("#FFE8C8", "#B5562E"),
    "p_slide": ("#F0FFD9", "#8DCB3E"),
    "p_baku": ("#BFE9F0", "#1F6F8B"),
    "p_svan": ("#FFE3E8", "#C8435C"),
    "p_bomba": ("#FFF4C2", "#F08A1C"),
    "p_bamboo": ("#E6F7E9", "#4F9E6A"),
    "p_lantern": ("#FFEFE0", "#9E2B2B"),
    "p_grill": ("#F2E3D8", "#5A3A2C"),
    "p_lilac": ("#F7ECFF", "#B48AD8"),
    "p_bread": ("#FFF6E6", "#D89A4A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Якитория (Варшавское ш., 26): окономияки, над которым вьются стружки тунца
add("cafe-yakitoriya-varshavskoe-26",
    "японская лепёшка окономияки с сеточкой майонеза и коричневым соусом",
    "над ней, как кудряшки на ветру, вьются розовые стружки тунца кацуобуси, а она удивлённо косится наверх",
    "p_teppan", f'''
<ellipse cx="64" cy="98" rx="50" ry="14" fill="#FFFFFF" {W(3)}/>
<path d="M18 84 Q18 62 64 60 Q110 62 110 84 Q110 100 64 102 Q18 100 18 84Z" fill="#D88A3E" {W(3)}/>
<path d="M24 80 Q24 66 64 65 Q104 66 104 80 Q104 92 64 94 Q24 92 24 80Z" fill="#7A3E22"/>
<path d="M30 70 L40 88 L50 68 L60 90 L70 68 L80 90 L90 68 L98 84" fill="none" stroke="#FFF7E6" stroke-width="3" stroke-linejoin="round"/>
<g fill="#5FB04A"><circle cx="36" cy="78" r="1.6"/><circle cx="58" cy="74" r="1.6"/><circle cx="84" cy="78" r="1.6"/><circle cx="70" cy="86" r="1.6"/><circle cx="46" cy="86" r="1.6"/></g>
<circle cx="54" cy="80" r="6" fill="#fff" {W(2)}/><circle cx="74" cy="80" r="6" fill="#fff" {W(2)}/>
<circle cx="55" cy="77" r="2.6" fill="{O}"/><circle cx="75" cy="77" r="2.6" fill="{O}"/>
<ellipse cx="64" cy="91" rx="3.4" ry="2.6" fill="{O}"/>
<g fill="#F8B7A8" {W(2)}>
<path d="M40 58 Q30 44 40 34 Q46 42 44 58Z"/>
<path d="M56 56 Q50 34 62 22 Q66 40 62 56Z"/>
<path d="M72 56 Q78 38 92 34 Q86 46 78 58Z"/>
<path d="M86 60 Q100 52 104 40 Q108 54 92 64Z"/>
</g>
<path d="M44 46 q-2 -4 0 -8 M60 44 q-2 -6 1 -12 M80 46 q3 -4 7 -6" fill="none" stroke="#E08A7A" stroke-width="1.6"/>
''')

# 2. Лебонтьяно (Электролитный пр.): шаверма съезжает с детской горки
add("cafe-lebontyano-elektrolitny",
    "шаверма в лаваше и бумажной обёртке с выглядывающей зеленью",
    "весело съезжает с жёлтой детской горки на площадке, подняв руки вверх",
    "p_slide", f'''
<path d="M14 40 L30 40 L30 118 M24 52 h-10 M24 66 h-10 M24 80 h-10" fill="none" stroke="{O}" stroke-width="3"/>
<path d="M28 40 L44 40 L112 108 L112 118 L96 118 Z" fill="#FFD43B" {W(3)}/>
<path d="M36 44 L104 112" stroke="#F2B90F" stroke-width="3"/>
<g transform="rotate(42 66 72)">
<rect x="50" y="46" width="32" height="56" rx="12" fill="#F6E1B8" {W(3)}/>
<path d="M50 74 L82 74 L82 92 Q82 104 66 104 Q50 104 50 92Z" fill="#FFFFFF" {W(3)}/>
<path d="M50 80 L82 86 M50 90 L82 96" stroke="#E2554A" stroke-width="2.4"/>
<path d="M54 48 Q58 38 62 46 Q66 36 70 46 Q74 38 78 48" fill="#6BC24A" {W(2.4)}/>
<circle cx="60" cy="50" r="2.4" fill="#E2554A"/><circle cx="72" cy="51" r="2.2" fill="#E2554A"/>
{face(66, 62, d=7, k=0.85)}
</g>
<path d="M76 40 Q78 30 84 26 M58 54 Q50 46 52 38" fill="none" {W(3)}/>
<circle cx="85" cy="25" r="3.2" fill="#F6E1B8" {W(2)}/><circle cx="52" cy="37" r="3.2" fill="#F6E1B8" {W(2)}/>
{sparkle(102, 34, 5)}{sparkle(110, 52, 3)}
''')

# 3. Бакинский бульвар (Стартовая ул.): пити гуляет по приморскому бульвару
add("cafe-bakinsky-bulvar-startovaya",
    "азербайджанский суп пити в высоком глиняном горшочке с крышкой",
    "вечером гуляет по приморскому бульвару под кованым фонарём, за парапетом блестит море",
    "p_baku", f'''
<path d="M0 84 Q32 80 64 84 T128 84 L128 98 L0 98Z" fill="#2E8FB0"/>
<path d="M10 90 h14 M40 92 h12 M86 90 h16" stroke="#BFEFFF" stroke-width="2" stroke-linecap="round"/>
<rect x="0" y="96" width="128" height="32" fill="#E8D6B0" {W(2.6)}/>
<path d="M0 96 h128" stroke="{O}" stroke-width="3"/>
<path d="M100 96 L100 34" stroke="{O}" stroke-width="5"/><path d="M100 96 L100 34" stroke="#3B4A5A" stroke-width="2.6"/>
<path d="M90 34 h20 l-4 -12 h-12Z" fill="#FFE07A" {W(2.4)}/><path d="M94 22 h12 l-6 -6Z" fill="#3B4A5A" {W(2)}/>
<circle cx="100" cy="30" r="16" fill="#FFF3A6" opacity=".3"/>
<path d="M36 56 Q30 60 30 76 Q30 104 56 108 Q82 104 82 76 Q82 60 76 56Z" fill="#C9683A" {W(3)}/>
<path d="M34 70 Q56 76 78 70" fill="none" stroke="#E79A68" stroke-width="3"/>
<rect x="34" y="48" width="44" height="10" rx="5" fill="#B4552C" {W(2.8)}/>
<path d="M44 48 Q56 34 68 48Z" fill="#B4552C" {W(2.8)}/><circle cx="56" cy="38" r="4" fill="#B4552C" {W(2.4)}/>
{face(56, 84, d=8, k=0.95)}
<path d="M44 108 l-4 10 M68 108 l4 10" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
{sparkle(20, 30, 4)}{sparkle(36, 18, 2.6)}
''')

# 4. Сатрапезо (Олимпийская деревня): кубдари подпрыгивает на батуте
add("cafe-satrapezo-olimpiyskaya-derevnya",
    "круглый сванский пирог кубдари с мясной начинкой и надрезом в середине",
    "подпрыгивает на детском батуте с синей сеткой, и из надреза вылетает струйка пара",
    "p_svan", f'''
<ellipse cx="64" cy="104" rx="50" ry="10" fill="#2B6CC4" {W(3)}/>
<ellipse cx="64" cy="102" rx="40" ry="6" fill="#4C8FE0"/>
<path d="M22 106 L18 124 M106 106 L110 124 M64 114 L64 126" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<path d="M30 86 Q24 90 22 96 M98 86 Q104 90 106 96" fill="none" stroke="#2B6CC4" stroke-width="2" stroke-dasharray="3 3"/>
<ellipse cx="64" cy="58" rx="40" ry="24" fill="#E6A24E" {W(3)}/>
<ellipse cx="64" cy="54" rx="34" ry="16" fill="#F4C474"/>
<path d="M56 46 L72 46" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<path d="M57 46 Q64 50 71 46" fill="#8A3F24"/>
<path d="M64 40 Q58 32 64 26 Q70 20 64 12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{face(64, 62, d=10, k=1.0)}
<path d="M40 82 l-2 10 M88 82 l2 10" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<path d="M30 44 q-6 -2 -10 2 M98 44 q6 -2 10 2" fill="none" {W(2.4)}/>
''')

# 5. La Pizza Bomba (Филёвский бул.): пицца-бомбочка с фитилём-розмарином и конфетти
add("cafe-la-pizza-bomba-filevsky",
    "пицца, свёрнутая в круглый шар-бомбочку с кружками пепперони и фитилём-веточкой розмарина",
    "из фитиля вместо искр сыплется разноцветное праздничное конфетти, а бомбочка зажмурилась от восторга",
    "p_bomba", f'''
<circle cx="58" cy="76" r="38" fill="#F5C45A" {W(3)}/>
<path d="M26 64 Q40 50 58 52 Q80 52 92 66 Q84 80 58 82 Q34 82 26 64Z" fill="#E8553D" opacity=".85"/>
<g fill="#C0362A" {W(2)}><circle cx="42" cy="62" r="6"/><circle cx="70" cy="60" r="6"/><circle cx="56" cy="98" r="5"/><circle cx="80" cy="92" r="5"/><circle cx="34" cy="90" r="5"/></g>
<path d="M44 74 q4 -4 8 0 M64 74 q4 -4 8 0" fill="none" {W(2.6)}/>
<path d="M52 84 Q58 90 64 84" fill="#C0362A" {W(2.4)}/>
<ellipse cx="40" cy="82" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".7"/><ellipse cx="76" cy="82" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".7"/>
<rect x="72" y="36" width="16" height="10" rx="3" transform="rotate(35 80 41)" fill="#7A6A5A" {W(2.4)}/>
<path d="M86 34 Q94 24 100 22" fill="none" stroke="#3E7A2E" stroke-width="3"/>
<g fill="#4E9A3E"><path d="M90 30 l-4 -5 l6 1Z"/><path d="M95 25 l-2 -6 l5 3Z"/><path d="M92 28 l5 3 l-6 1Z"/></g>
<g {W(1.4)}><rect x="104" y="12" width="6" height="4" fill="#4CC3F0" transform="rotate(20 107 14)"/><rect x="110" y="30" width="6" height="4" fill="#FF6FA5"/>
<rect x="98" y="6" width="5" height="4" fill="#9B6BF0"/><circle cx="114" cy="22" r="2.6" fill="#7CD26E"/><circle cx="104" cy="38" r="2.4" fill="#FFE04A"/>
<rect x="116" y="40" width="5" height="4" fill="#FF9A3C" transform="rotate(-25 118 42)"/></g>
''')

# 6. Тануки (Народного Ополчения): харумаки играют в чехарду на бамбуковой циновке
add("cafe-tanuki-narodnogo-opolcheniya",
    "два золотистых хрустящих ролла харумаки",
    "играют в чехарду на бамбуковой циновке-макису: один пригнулся, другой перепрыгивает через него",
    "p_bamboo", f'''
<rect x="8" y="98" width="112" height="26" rx="3" fill="#D9C27A" {W(3)}/>
<path d="M8 104 h112 M8 110 h112 M8 116 h112" stroke="#B59A4A" stroke-width="2"/>
<rect x="24" y="76" width="50" height="22" rx="11" fill="#E9A43C" {W(3)}/>
<path d="M34 78 l4 18 M46 78 l4 18 M58 78 l4 18" stroke="#C9822A" stroke-width="2"/>
{face(40, 86, d=5, k=0.65)}
<g transform="rotate(-30 78 50)">
<rect x="54" y="38" width="50" height="22" rx="11" fill="#F0B54A" {W(3)}/>
<path d="M64 40 l4 18 M76 40 l4 18 M88 40 l4 18" stroke="#CF8D30" stroke-width="2"/>
{face(90, 48, d=5, k=0.65)}
</g>
<path d="M60 70 Q62 76 58 80 M74 62 Q80 70 74 78" fill="none" {W(2.6)}/>
<path d="M30 60 Q38 54 46 60 M100 26 q4 -4 8 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(22, 40, 4)}
''')

# 7. Тануки (Красная Пресня): кастелла шагает с красным бумажным фонариком
add("cafe-tanuki-krasnaya-presnya",
    "жёлтый брусок японского бисквита кастелла с коричневой корочкой сверху",
    "шагает в праздничном шествии и несёт на палочке красный бумажный фонарик",
    "p_lantern", f'''
<path d="M86 14 L86 30" stroke="{O}" stroke-width="3"/>
<path d="M74 32 h24 M74 66 h24" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="86" cy="49" rx="16" ry="17" fill="#E23A3A" {W(3)}/>
<path d="M72 42 h28 M71 50 h30 M72 58 h28" stroke="#B31F1F" stroke-width="1.8"/>
<path d="M86 66 v8" stroke="{O}" stroke-width="2.4"/><path d="M83 74 h6 v6 h-6Z" fill="#FFD43B" {W(1.6)}/>
<path d="M70 14 L90 14" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<path d="M60 80 L72 18" stroke="#8A5B30" stroke-width="3" stroke-linecap="round"/>
<rect x="22" y="56" width="48" height="50" rx="6" fill="#FFD95A" {W(3)}/>
<path d="M22 64 Q22 56 28 56 L64 56 Q70 56 70 64 L70 68 L22 68Z" fill="#8A4A22" {W(3)}/>
{face(46, 84, d=9, k=0.95)}
<path d="M66 80 Q72 78 64 74" fill="none" {W(3)}/>
<path d="M34 106 l-4 12 M58 106 l6 12" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
{sparkle(20, 34, 4)}{sparkle(110, 92, 3)}
''')

# 8. Стейк-хаус Muu (Рублёвское ш., 101): рибай на сковороде-гриль, пар складывается в «МУ»
add("cafe-muu-rublevskoe",
    "сочный стейк рибай с мраморными прожилками и полосками от гриля",
    "шкворчит на чугунной сковороде-гриль, а пар над ним складывается в буквы «МУ»",
    "p_grill", f'''
<path d="M100 88 L124 80" stroke="{O}" stroke-width="9" stroke-linecap="round"/><path d="M100 88 L124 80" stroke="#2E2A2A" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="60" cy="94" rx="48" ry="20" fill="#2E2A2A" {W(3)}/>
<ellipse cx="60" cy="90" rx="42" ry="14" fill="#4A4444"/>
<path d="M28 74 Q24 58 44 54 Q66 48 86 56 Q100 64 92 80 Q80 94 54 92 Q32 90 28 74Z" fill="#A9483A" {W(3)}/>
<path d="M40 62 Q52 68 48 78 M66 58 Q60 70 72 80 M84 64 Q76 70 80 82" fill="none" stroke="#F3D6C6" stroke-width="2.4"/>
<path d="M36 70 L50 58 M50 82 L74 58 M70 86 L90 66" stroke="#5A2218" stroke-width="3.4" stroke-linecap="round"/>
{face(62, 74, d=8, k=0.85)}
<path d="M34 42 L34 26 L40 34 L46 26 L46 42" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M54 26 L54 36 Q54 42 60 42 Q66 42 66 36 L66 26" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
<path d="M76 46 q-4 -6 0 -12 q4 -6 0 -12 M88 50 q-4 -6 0 -12" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
''')

# 9. Здрасте (Корабельная ул.): двухэтажная этажерка — внизу играют макаронс, наверху эклеры
add("cafe-zdraste-korabelnaya",
    "двухъярусная этажерка с пирожными",
    "на нижнем ярусе резвятся три разноцветных макаронса-малыша, а на верхнем чинно сидят два эклера, как родители на втором этаже",
    "p_lilac", f'''
<path d="M64 14 L64 112" stroke="{O}" stroke-width="5"/><path d="M64 14 L64 112" stroke="#D4AF37" stroke-width="2.6"/>
<circle cx="64" cy="12" r="5" fill="#D4AF37" {W(2.4)}/>
<ellipse cx="64" cy="112" rx="24" ry="5" fill="#fff" {W(2.6)}/>
<ellipse cx="64" cy="54" rx="34" ry="7" fill="#fff" {W(3)}/>
<rect x="36" y="38" width="26" height="12" rx="6" fill="#E9B46A" {W(2.4)}/><path d="M38 40 h22" stroke="#6B3A1E" stroke-width="4" stroke-linecap="round"/>
<rect x="66" y="38" width="26" height="12" rx="6" fill="#E9B46A" {W(2.4)}/><path d="M68 40 h22" stroke="#F6E7C8" stroke-width="4" stroke-linecap="round"/>
<circle cx="45" cy="45" r="1.4" fill="{O}"/><circle cx="53" cy="45" r="1.4" fill="{O}"/>
<circle cx="75" cy="45" r="1.4" fill="{O}"/><circle cx="83" cy="45" r="1.4" fill="{O}"/>
<ellipse cx="64" cy="98" rx="50" ry="9" fill="#fff" {W(3)}/>
<g {W(2.6)}>
<ellipse cx="32" cy="84" rx="13" ry="10" fill="#FF9EC0"/><path d="M19 84 h26" stroke="#FFF2C2" stroke-width="3"/>
<ellipse cx="62" cy="80" rx="13" ry="10" fill="#9EDC8A" transform="rotate(-15 62 80)"/>
<ellipse cx="94" cy="86" rx="13" ry="10" fill="#9BC6FF"/><path d="M81 86 h26" stroke="#FFF2C2" stroke-width="3"/>
</g>
{face(32, 80, d=4, k=0.55)}{face(62, 76, d=4, k=0.55)}{face(94, 82, d=4, k=0.55)}
<path d="M48 72 q-4 -4 -6 0 M76 68 q4 -6 8 -2" fill="none" {W(2.2)}/>
{sparkle(104, 28, 5)}{sparkle(22, 32, 3)}
''')

# 10. Точно вкусно (Раменки): суп в хлебной чаше подмигивает из-под горбушки-крышки
add("cafe-tochno-vkusno-ramenki",
    "круглая хлебная чаша с горячим супом и крышечкой-горбушкой",
    "приподнимает крышку-горбушку, как шляпу, и подмигивает, а из-под неё поднимается ароматный пар",
    "p_bread", f'''
<ellipse cx="64" cy="108" rx="46" ry="10" fill="#FFFFFF" {W(3)}/>
<path d="M24 70 Q22 106 64 108 Q106 106 104 70Z" fill="#C98A3E" {W(3)}/>
<path d="M34 84 l6 4 M88 86 l6 -4 M60 98 l8 0" stroke="#A86A28" stroke-width="2.4" stroke-linecap="round"/>
<ellipse cx="64" cy="70" rx="40" ry="10" fill="#E07A3A" {W(3)}/>
<ellipse cx="54" cy="68" rx="4" ry="2" fill="#FFE29A"/><ellipse cx="74" cy="72" rx="3" ry="1.6" fill="#FFE29A"/>
<g transform="rotate(-24 40 44)">
<path d="M14 48 Q16 24 44 22 Q72 24 74 48Z" fill="#B87430" {W(3)}/>
<path d="M24 36 l8 -4 M40 30 l8 0 M56 32 l8 4" stroke="#E2B06A" stroke-width="2.4" stroke-linecap="round"/>
</g>
<path d="M72 54 q-4 -6 0 -12 q4 -6 0 -12 M86 58 q-4 -6 0 -12 q4 -6 0 -12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{eye(52, 88, 0.9)}<path d="M72 88 q4 -3 8 0" fill="none" {W(2.6)}/>
<path d="M58 94 Q64 99 70 94" fill="none" {W(2.4)}/>
<ellipse cx="44" cy="94" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/><ellipse cx="84" cy="94" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/>
''')


def main(ids):
    ids = ids or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    have = {l.split(" — ", 1)[0] for l in lines if " — " in l}
    with open(reg, "a", encoding="utf-8") as f:
        for pid in ids:
            if pid not in have:
                h, sc = SUBJ[pid]
                f.write(f"{pid} — герой: {h} | сцена: {sc}\n")
    print("svg", len(ids))


if __name__ == "__main__":
    main(sys.argv[1:])
