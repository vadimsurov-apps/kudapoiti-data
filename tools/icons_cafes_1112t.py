"""Иконки робота cafes, 2026-11-12 (17 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1112t.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
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
    "zt_taro": ("#FBF0FF", "#B58AD9"),
    "zt_mint": ("#EFFFF8", "#6CCFA8"),
    "zt_vdnh": ("#FFF8E4", "#E3B24A"),
    "zt_pond": ("#EAFBFF", "#5FB7C9"),
    "zt_soy": ("#FFF3EE", "#E07A5F"),
    "zt_ink": ("#EEF1FF", "#5B6BC9"),
    "zt_wine": ("#FFF0F3", "#C2465E"),
    "zt_wheat": ("#FFFBEF", "#C9A15A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Здрасте (Лобненская, 13к4; кофейня с детской комнатой): бабл-ти машет «здрасте!»
add("cafe-zdraste-lobnenskaya-13",
    "прозрачный стакан бабл-ти с молочным чаем, тёмными шариками тапиоки на дне и толстой розовой трубочкой",
    "приветливо машет высоко поднятой ручкой «здрасте!», а рядом облачко-реплика с восклицательным знаком",
    "zt_taro", f'''
<path d="M70 8 L62 40" stroke="#FF6FA3" stroke-width="9" stroke-linecap="round"/>
<path d="M70 8 L62 40" fill="none" stroke="{O}" stroke-width="2.4" stroke-dasharray="0" opacity=".0"/>
<path d="M38 38 L90 38 L84 112 Q64 118 44 112Z" fill="#F4E3CC" {W(3.2)}/>
<path d="M38 38 L90 38 L89 48 L39 48Z" fill="#FFFFFF" {W(2.6)}/>
<g fill="#3A2A2A"><circle cx="50" cy="104" r="5"/><circle cx="61" cy="107" r="5"/><circle cx="72" cy="105" r="5"/><circle cx="56" cy="97" r="5"/><circle cx="68" cy="97" r="5"/><circle cx="78" cy="99" r="4.5"/></g>
<g fill="#fff" opacity=".7"><circle cx="49" cy="102" r="1.4"/><circle cx="60" cy="105" r="1.4"/><circle cx="71" cy="103" r="1.4"/></g>
<rect x="66" y="6" width="8" height="40" rx="3" fill="#FF6FA3" {W(2.4)} transform="rotate(14 70 26)"/>
{eye(55, 66, 0.9)}{eye(73, 66, 0.9)}
<path d="M58 74 Q64 81 70 74Z" fill="#E24B5B" {W(1.8)}/>
{BL(48, 73)}{BL(80, 73)}
<path d="M88 66 Q100 56 104 40" fill="none" {W(3.4)}/>
<g fill="#F4E3CC" {W(2.2)}><circle cx="105" cy="37" r="5"/></g>
<path d="M98 30 L95 25 M106 28 L107 22 M113 33 L118 30" stroke="{O}" stroke-width="2" stroke-linecap="round"/>
<path d="M40 76 Q30 84 32 94" fill="none" {W(3.4)}/>
<g transform="translate(6 14)"><path d="M8 20 Q8 10 22 10 L34 10 Q46 10 46 20 Q46 30 34 30 L22 30 L14 36 L16 29 Q8 27 8 20Z" fill="#FFFFFF" {W(2.4)}/>
<path d="M27 14 L27 22" stroke="#E2362F" stroke-width="3.4" stroke-linecap="round"/><circle cx="27" cy="26.5" r="1.9" fill="#E2362F"/></g>
''')

# 2. Здрасте (Красулинская, 19; детская зона): вафля пересчитывает свои клеточки
add("cafe-zdraste-krasulinskaya-19",
    "квадратная бельгийская вафля в клеточку с шапкой сливочного крема и половинкой клубники",
    "сидит на мятном блюдце и, высунув язычок, пересчитывает пальчиком свои клеточки, а над ней парят цифры 1, 2, 3",
    "zt_mint", f'''
<ellipse cx="64" cy="104" rx="50" ry="12" fill="#FFFFFF" {W(3)}/>
<ellipse cx="64" cy="102" rx="38" ry="7" fill="#DFF6EC"/>
<rect x="30" y="46" width="64" height="54" rx="8" fill="#E8A951" {W(3.2)}/>
<g fill="#C7832E" opacity=".9">
<rect x="36" y="52" width="11" height="11" rx="2"/><rect x="51" y="52" width="11" height="11" rx="2"/><rect x="66" y="52" width="11" height="11" rx="2"/><rect x="81" y="52" width="8" height="11" rx="2"/>
<rect x="36" y="84" width="11" height="11" rx="2"/><rect x="51" y="84" width="11" height="11" rx="2"/><rect x="66" y="84" width="11" height="11" rx="2"/><rect x="81" y="84" width="8" height="11" rx="2"/>
</g>
<path d="M40 48 Q38 34 52 36 Q56 26 66 32 Q78 26 82 38 Q92 38 88 48Z" fill="#FFFDF5" {W(2.8)}/>
<path d="M58 30 Q62 16 74 22 Q78 30 70 36 Q62 38 58 30Z" fill="#E8344A" {W(2.4)}/>
<g fill="#FFE07A"><circle cx="64" cy="27" r="1"/><circle cx="70" cy="25" r="1"/><circle cx="68" cy="31" r="1"/></g>
<path d="M66 20 Q70 14 76 16" fill="none" stroke="#3E9B50" stroke-width="3" stroke-linecap="round"/>
{eye(52, 70, 0.85)}{eye(72, 70, 0.85)}
<path d="M57 77 Q62 81 67 77" fill="none" {W(1.8)}/><path d="M61 79 Q62 85 65 80" fill="#FF7FA8" {W(1.4)}/>
{BL(44, 77)}{BL(80, 77)}
<path d="M94 74 Q106 70 104 58" fill="none" {W(3.2)}/>
<circle cx="104" cy="55" r="3.6" fill="#E8A951" {W(2)}/>
<g font-family="Arial Rounded MT Bold, Arial, sans-serif" font-weight="bold" fill="#2E8C66" stroke="#fff" stroke-width="1" paint-order="stroke">
<text x="20" y="44" font-size="15">1</text><text x="32" y="28" font-size="14">2</text><text x="92" y="30" font-size="15">3</text></g>
''')

# 3. iL Патио (ВДНХ, 2-я Останкинская, 3): арка главного входа ВДНХ из макарон-пенне
add("cafe-ilpatio-vdnh",
    "парадная арка главного входа ВДНХ, у которой колонны — огромные макароны-пенне, а наверху вместо снопа — треугольный кусок пиццы",
    "стоит над красной ковровой дорожкой, по которой к входу катится маленький мячик-фрикаделька",
    "zt_vdnh", f'''
<path d="M54 128 L58 84 L70 84 L74 128Z" fill="#E2362F" {W(2.6)}/>
<rect x="10" y="44" width="108" height="14" rx="3" fill="#FFF3D6" {W(3)}/>
<g fill="#F7C653" {W(3)}>
<rect x="16" y="58" width="16" height="56" rx="3"/><rect x="38" y="58" width="16" height="56" rx="3"/>
<rect x="74" y="58" width="16" height="56" rx="3"/><rect x="96" y="58" width="16" height="56" rx="3"/></g>
<g stroke="#D89B2B" stroke-width="2.4" stroke-linecap="round">
<path d="M19 66 L29 62 M19 76 L29 72 M19 86 L29 82 M19 96 L29 92 M19 106 L29 102"/>
<path d="M41 66 L51 62 M41 76 L51 72 M41 86 L51 82 M41 96 L51 92 M41 106 L51 102"/>
<path d="M77 66 L87 62 M77 76 L87 72 M77 86 L87 82 M77 96 L87 92 M77 106 L87 102"/>
<path d="M99 66 L109 62 M99 76 L109 72 M99 86 L109 82 M99 96 L109 92 M99 106 L109 102"/></g>
<path d="M54 58 Q64 70 74 58" fill="none" {W(3)}/>
<path d="M40 44 L64 6 L88 44Z" fill="#FFC94A" {W(3)}/>
<path d="M40 44 L88 44 L86 38 L42 38Z" fill="#D9963A" {W(2.4)}/>
<path d="M50 34 L64 12 L78 34Z" fill="#E8553B"/>
<g fill="#B8241E" {W(1.4)}><circle cx="58" cy="30" r="3.4"/><circle cx="70" cy="28" r="3.2"/><circle cx="64" cy="20" r="2.8"/></g>
{eye(58, 36, 0.6)}{eye(70, 36, 0.6)}
<path d="M61 40 Q64 42 67 40" fill="none" {W(1.6)}/>
<circle cx="64" cy="112" r="7" fill="#9A5A35" {W(2.4)}/>
{eye(61, 111, 0.45)}{eye(67, 111, 0.45)}
<path d="M54 118 L48 120 M52 112 L46 112" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
{sparkle(108, 22, 5)}{sparkle(20, 24, 4)}
''')

# 4. Гарда (Дрожжино, на берегу пруда): бифштекс с глазуньей болтает ножками в воде
add("cafe-garda-drozhzhino",
    "румяный бифштекс-котлета с яйцом-глазуньей на макушке, как в белой панамке с жёлтой серединкой",
    "сидит на деревянном бережке пруда и болтает ножками в воде, от пяток разбегаются круги",
    "zt_pond", f'''
<rect x="0" y="86" width="128" height="42" fill="#3E9CB8"/>
<path d="M0 86 Q20 82 40 86 Q60 90 80 86 Q100 82 128 86" fill="none" stroke="#BDEBF5" stroke-width="3"/>
<ellipse cx="54" cy="108" rx="14" ry="4" fill="none" stroke="#DDF6FB" stroke-width="2.4"/>
<ellipse cx="78" cy="110" rx="14" ry="4" fill="none" stroke="#DDF6FB" stroke-width="2.4"/>
<ellipse cx="54" cy="108" rx="24" ry="7" fill="none" stroke="#DDF6FB" stroke-width="1.6" opacity=".7"/>
<rect x="18" y="72" width="92" height="12" rx="2" fill="#B07A4A" {W(3)}/>
<path d="M30 72 L30 84 M52 72 L52 84 M74 72 L74 84 M96 72 L96 84" stroke="#7E5230" stroke-width="2"/>
<path d="M54 82 L52 104 M76 82 L78 104" {W(3.4)}/>
<ellipse cx="52" cy="105" rx="4" ry="2.6" fill="#8B4A2B" {W(1.8)}/><ellipse cx="78" cy="105" rx="4" ry="2.6" fill="#8B4A2B" {W(1.8)}/>
<ellipse cx="64" cy="58" rx="34" ry="20" fill="#8B4A2B" {W(3.2)}/>
<path d="M38 52 L50 46 M56 64 L70 58 M78 50 L88 46" stroke="#5E2E18" stroke-width="2.6" stroke-linecap="round"/>
<path d="M36 40 Q34 26 50 28 Q56 16 70 22 Q86 18 90 32 Q100 36 92 44 Q64 50 36 40Z" fill="#FFFFFF" {W(2.8)}/>
<circle cx="64" cy="31" r="9" fill="#FFC21A" {W(2.4)}/>
<circle cx="61" cy="28" r="2.4" fill="#fff" opacity=".8"/>
{eye(54, 60, 0.85)}{eye(74, 60, 0.85)}
<path d="M58 67 Q64 73 70 67Z" fill="#E24B5B" {W(1.8)}/>
{BL(46, 66)}{BL(82, 66)}
<path d="M30 60 Q20 66 22 74 M98 60 Q108 66 106 74" fill="none" {W(3)}/>
<g fill="#5BAE4A" {W(2)}><path d="M108 96 Q118 92 122 98 Q114 104 108 96Z"/></g>
{sparkle(20, 22, 4)}
''')

# 5. Тануки (Чертановская, 36с1; детская комната, анимация): ролл «Филадельфия» перепрыгивает лужицу соевого соуса
add("cafe-tanuki-chertanovskaya-36",
    "толстый ролл «Филадельфия» в розовой шубке из ломтиков лосося, с белым сливочным сыром внутри",
    "в длинном прыжке перелетает через лужицу соевого соуса на тёмной сланцевой доске, растопырив ручки",
    "zt_soy", f'''
<path d="M0 98 L128 90 L128 128 L0 128Z" fill="#4A4A55" {W(3)}/>
<ellipse cx="68" cy="106" rx="26" ry="7" fill="#5A2E14" {W(2.4)}/>
<ellipse cx="62" cy="104" rx="8" ry="2" fill="#9A5A35" opacity=".8"/>
<path d="M18 92 Q30 70 46 60" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="4 5" stroke-linecap="round"/>
<g transform="rotate(-12 70 52)">
<ellipse cx="70" cy="56" rx="26" ry="22" fill="#FF8C78" {W(3.2)}/>
<path d="M46 50 Q58 40 70 46 Q82 40 94 50 M46 62 Q58 54 70 60 Q82 54 94 62" fill="none" stroke="#FFD2C6" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="70" cy="40" rx="20" ry="8" fill="#1F3A2B" {W(2.6)}/>
<ellipse cx="70" cy="39" rx="15" ry="5.4" fill="#FFFFFF"/>
<ellipse cx="70" cy="39" rx="7" ry="2.8" fill="#FFF6E0" {W(1.4)}/>
{eye(62, 60, 0.85)}{eye(78, 60, 0.85)}
<path d="M66 67 Q70 72 74 67Z" fill="#B8243A" {W(1.6)}/>
{BL(56, 66)}{BL(84, 66)}
</g>
<path d="M44 58 Q32 50 30 40 M96 48 Q108 42 110 30" fill="none" {W(3.2)}/>
<path d="M56 76 L48 88 M80 74 L90 84" {W(3.2)}/>
<circle cx="30" cy="38" r="3.4" fill="#FF8C78" {W(1.8)}/><circle cx="110" cy="28" r="3.4" fill="#FF8C78" {W(1.8)}/>
<g fill="#5A2E14"><circle cx="96" cy="100" r="2"/><circle cx="100" cy="96" r="1.4"/></g>
{sparkle(108, 64, 4)}{sparkle(22, 20, 4)}
''')

# 6. Тануки (Преображенская, 5/7; детская игровая): ломтик сашими делает «мостик»
add("cafe-tanuki-preobrazhenskaya-5",
    "оранжевый ломтик сашими из лосося с белыми полосками",
    "делает гимнастический «мостик» над синей пиалой, опираясь ручками и ножками на её края, а сверху сыплются кунжутинки",
    "zt_ink", f'''
<path d="M18 92 Q64 132 110 92Z" fill="#2E4FA8" {W(3.2)}/>
<ellipse cx="64" cy="92" rx="46" ry="10" fill="#1B2E66" {W(3)}/>
<path d="M34 106 Q50 112 64 112" fill="none" stroke="#fff" stroke-width="2.4" opacity=".6" stroke-linecap="round"/>
<g fill="#FFFFFF" {W(1.6)}><circle cx="40" cy="116" r="3"/><circle cx="64" cy="120" r="3"/><circle cx="88" cy="116" r="3"/></g>
<path d="M22 88 Q26 40 64 36 Q102 40 106 88 L92 88 Q90 54 64 52 Q38 54 36 88Z" fill="#FF8A4C" {W(3.2)}/>
<path d="M30 70 Q40 48 56 44 M38 84 Q44 62 60 58 M98 70 Q88 48 72 44 M90 84 Q84 62 68 58" fill="none" stroke="#FFF1E6" stroke-width="3" stroke-linecap="round"/>
<path d="M22 88 L18 92 M36 88 L38 92 M92 88 L90 92 M106 88 L110 92" {W(3.2)}/>
{eye(57, 44, 0.8)}{eye(71, 44, 0.8)}
<path d="M60 48 Q64 52 68 48" fill="none" {W(1.8)}/>
{BL(50, 48)}{BL(78, 48)}
<g fill="#FFF6DC" stroke="{O}" stroke-width="1.2">
<ellipse cx="44" cy="16" rx="2" ry="3.2" transform="rotate(20 44 16)"/><ellipse cx="62" cy="10" rx="2" ry="3.2"/><ellipse cx="82" cy="18" rx="2" ry="3.2" transform="rotate(-20 82 18)"/><ellipse cx="96" cy="28" rx="2" ry="3.2"/></g>
''')

# 7. Suluguni (Шелепихинская наб., 34к2; детская комната): жареный сулугуни выдувает сырный пузырь
add("cafe-suluguni-shelepikha",
    "золотистый ломтик жареного сулугуни в маленькой глиняной сковородке-кеци",
    "тянет из себя сырную ниточку и надувает из неё большой сырный пузырь, как из жвачки",
    "zt_wine", f'''
<ellipse cx="60" cy="98" rx="42" ry="16" fill="#A0522D" {W(3.2)}/>
<ellipse cx="60" cy="92" rx="36" ry="10" fill="#7A3A1E" {W(2.6)}/>
<path d="M98 94 L118 102" stroke="#A0522D" stroke-width="7" stroke-linecap="round"/><path d="M98 94 L118 102" stroke="{O}" stroke-width="1.6" fill="none" opacity=".0"/>
<path d="M28 90 Q24 62 44 56 Q60 50 76 56 Q96 62 92 90 Q60 98 28 90Z" fill="#F6C760" {W(3.2)}/>
<path d="M36 70 Q44 62 54 66 M70 64 Q80 62 86 70" fill="none" stroke="#D99A2B" stroke-width="3" stroke-linecap="round"/>
<g fill="#C77B1E"><circle cx="40" cy="80" r="2"/><circle cx="82" cy="82" r="2.2"/><circle cx="62" cy="62" r="1.6"/></g>
{eye(50, 74, 0.85)}{eye(68, 74, 0.85)}
{BL(42, 81)}{BL(76, 81)}
<path d="M58 82 Q64 84 70 80 Q86 66 90 50" fill="none" stroke="#FFF2C2" stroke-width="4" stroke-linecap="round"/>
<path d="M58 82 Q64 84 70 80 Q86 66 90 50" fill="none" {W(1.4)}/>
<circle cx="94" cy="34" r="20" fill="#FFF2C2" opacity=".85" {W(2.8)}/>
<ellipse cx="86" cy="26" rx="6" ry="4" fill="#fff" opacity=".9"/>
{sparkle(20, 30, 5)}{sparkle(36, 14, 3.5)}
''')

# 8. Грано (Отрадное, ЖК «Левел Лесной»; детская комната): зёрнышко-повар посыпает пиццу мукой
add("cafe-grano-otradnoe",
    "пшеничное зёрнышко с бороздкой посередине в высоком поварском колпаке",
    "стоит на краю круглой пиццы-маргариты и посыпает её мукой из маленького ситечка, мука сыплется белым облачком",
    "zt_wheat", f'''
<ellipse cx="62" cy="100" rx="54" ry="20" fill="#E9B866" {W(3.2)}/>
<ellipse cx="62" cy="98" rx="44" ry="14" fill="#E1452E"/>
<g fill="#FFF8E8" {W(1.6)}><ellipse cx="44" cy="96" rx="9" ry="5"/><ellipse cx="72" cy="104" rx="10" ry="5"/><ellipse cx="80" cy="92" rx="7" ry="4"/></g>
<g fill="#3E9B50"><path d="M54 104 Q58 98 62 104 Q58 108 54 104Z"/><path d="M60 90 Q64 84 68 90 Q64 94 60 90Z"/></g>
<g fill="#FFFFFF" opacity=".95"><circle cx="40" cy="70" r="2.4"/><circle cx="34" cy="80" r="2"/><circle cx="46" cy="80" r="2.2"/><circle cx="40" cy="88" r="1.8"/><circle cx="30" cy="90" r="1.6"/><circle cx="50" cy="90" r="1.6"/></g>
<path d="M88 86 L86 96 M100 86 L102 96" {W(3)}/>
<ellipse cx="94" cy="66" rx="16" ry="22" fill="#E6B45A" {W(3.2)}/>
<path d="M94 46 Q90 66 94 88" fill="none" stroke="#B9822E" stroke-width="2.6" stroke-linecap="round"/>
<path d="M80 46 Q76 30 86 30 Q90 18 100 24 Q112 22 110 36 Q112 46 106 48 L82 48Z" fill="#FFFFFF" {W(2.8)}/>
<rect x="80" y="44" width="28" height="6" rx="2" fill="#FFFFFF" {W(2.4)}/>
{eye(88, 62, 0.75)}{eye(101, 62, 0.75)}
<path d="M91 70 Q94 73 98 70" fill="none" {W(1.8)}/>
{BL(84, 70)}{BL(105, 70)}
<path d="M80 66 Q66 60 56 58" fill="none" {W(3)}/>
<circle cx="46" cy="58" r="10" fill="#E8EEF5" {W(2.6)}/>
<path d="M38 58 L54 58 M46 50 L46 66 M40 52 L52 64 M52 52 L40 64" stroke="#9AA7B8" stroke-width="1.2"/>
<path d="M56 58 L60 58" {W(3)}/>
{sparkle(20, 24, 4.5)}{sparkle(60, 18, 3.5)}
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
