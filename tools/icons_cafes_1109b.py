"""Иконки робота cafes, 2026-11-09 (вторая партия). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно (свой герой по кухне/названию, своя сцена, своя компоновка и палитра фона). Сверено с icons-src/subjects.txt
и листами icons-catalog. Запуск: python3 tools/icons_cafes_1109b.py [id…]"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=8, k=0.7, **kw: face(cx, cy, d=d, k=k, **kw)
draw_icons.BG.update({
    "j9_velvet": ("#FFF0F3", "#C2416B"),
    "j9_cabin": ("#F4EBDD", "#8A6A48"),
    "j9_saffron": ("#FFF6DA", "#E59A2C"),
    "j9_marsh": ("#EEF7EA", "#7FA36A"),
    "j9_dacha": ("#F3FFF0", "#9BCB6E"),
    "j9_cave": ("#3C2E5C", "#1F1838"),
    "j9_stair": ("#FFF4E6", "#C98B5B"),
    "j9_aragvi": ("#EAF6FF", "#5D8FB8"),
    "j9_sunset": ("#FFE9D2", "#F07A55"),
    "j9_tale": ("#FFF2F8", "#E59BC8"),
    "j9_steam": ("#F6F6F2", "#B9B49A"),
    "j9_peak": ("#F0F4FF", "#7C8FD0"),
    "j9_carpet": ("#FFEFE6", "#B5452F"),
    "j9_garden": ("#F7FFE8", "#A3C94F"),
    "j9_pond": ("#E6FBF6", "#3FB39A"),
    "j9_zen": ("#F2F2EE", "#8E9A86"),
    "j9_pass": ("#F2FBFF", "#4E9CC9"),
    "j9_letter": ("#FFFBEA", "#D4B04A"),
    "j9_year": ("#F5F0FF", "#7A62C9"),
    "j9_greek": ("#F0F8FF", "#2F6FB8"),
    "j9_pier": ("#E9F7FF", "#2F86A8"),
    "j9_espresso": ("#F6EDE6", "#6B4532"),
    "j9_mall": ("#FFF0FA", "#C873B2"),
    "j9_bamboo": ("#F1FAE6", "#5E9A3A"),
    "j9_ice": ("#EEF8FF", "#9BB8D6"),
    "j9_lacquer": ("#2A2A2E", "#0F0F12"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Пицца Императрица — пицца с бортиком-короной на бархатной подушке
add("cafe-pizza-imperatritsa-lukhmanovskaya",
    "пицца, у которой бортик-корка вырос зубцами императорской короны",
    "лежит на красной бархатной подушке с золотыми кисточками", "j9_velvet", f'''
<path d="M14 100 Q64 82 114 100 Q118 114 104 118 H24 Q10 114 14 100Z" fill="#B3123E" {s()}/>
<circle cx="16" cy="112" r="5" fill="#F6C343" {s()}/><circle cx="112" cy="112" r="5" fill="#F6C343" {s()}/>
<path d="M26 88 L30 48 L44 66 L54 38 L64 62 L74 38 L84 66 L98 48 L102 88Z" fill="#F2B45A" {s()}/>
<ellipse cx="64" cy="88" rx="38" ry="12" fill="#FFD36E" {s()}/>
<circle cx="54" cy="38" r="4" fill="#E8344F" {W(2)}/><circle cx="74" cy="38" r="4" fill="#3E7FD9" {W(2)}/>
<circle cx="30" cy="48" r="3.5" fill="#5CC08A" {W(2)}/><circle cx="98" cy="48" r="3.5" fill="#5CC08A" {W(2)}/>
<circle cx="44" cy="88" r="5" fill="#D9452F"/><circle cx="82" cy="86" r="5" fill="#D9452F"/><circle cx="64" cy="92" r="4" fill="#D9452F"/>
''' + f(64, 68, d=9, k=0.75))

# 2. Сытый Лось — лосиные рога-вешалка с гирляндой сосисок на бревенчатой стене
add("cafe-sytyy-los-shirokaya",
    "лосиные рога-вешалка, на которых висит гирлянда сосисок",
    "прибиты к бревенчатой стене охотничьей избы", "j9_cabin", f'''
''' + "".join(f'<rect x="0" y="{y}" width="128" height="14" rx="7" fill="#B98B5E" {W(2)}/>' for y in (8, 24, 40, 56, 72, 88, 104)) + f'''
<path d="M50 56 Q30 50 22 30 M30 46 L18 42 M34 52 L26 58 M78 56 Q98 50 106 30 M98 46 L110 42 M94 52 L102 58 M24 30 L20 22 M104 30 L108 22"
 fill="none" stroke="#F1E2C6" stroke-width="7" stroke-linecap="round"/>
<path d="M50 56 Q30 50 22 30 M30 46 L18 42 M34 52 L26 58 M78 56 Q98 50 106 30 M98 46 L110 42 M94 52 L102 58 M24 30 L20 22 M104 30 L108 22"
 fill="none" {W(2.2)} opacity=".6"/>
<rect x="46" y="50" width="36" height="22" rx="8" fill="#7A4E2D" {s()}/>
''' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="5" fill="#E07A5F" {W(2.2)} transform="rotate({r} {x} {y})"/>'
              for x, y, r in [(26, 70, 40), (38, 82, 20), (52, 90, 8), (64, 92, 0), (76, 90, -8), (90, 82, -20), (102, 70, -40)]) + f'''
<path d="M20 62 Q64 104 108 62" fill="none" stroke="#5B3A22" stroke-width="1.6"/>
''' + f(64, 60, d=8, k=0.6).replace(O, "#FFF3D6"))

# 3. Чайхона №1 (Донского) — хоровод чучвары вокруг пиалы бульона
add("cafe-chaihona1-donskogo",
    "крошечные узбекские пельмешки чучвара",
    "водят хоровод вокруг синей пиалы с бульоном", "j9_saffron", f'''
<path d="M30 70 Q64 112 98 70Z" fill="#2E6FD0" {s()}/><ellipse cx="64" cy="70" rx="34" ry="9" fill="#F5C76A" {s()}/>
<path d="M40 86 Q64 96 88 86" fill="none" stroke="#fff" stroke-width="2.5"/>
''' + "".join(f'<g transform="translate({64+44*math.cos(a)-0:.1f} {66+30*math.sin(a):.1f})"><path d="M-9 4 Q-10 -8 0 -9 Q10 -8 9 4Z" fill="#FFF4E0" {W(2.2)}/><path d="M-4 -8 Q0 -14 4 -8" fill="none" {W(2)}/></g>'
              for a in [math.radians(x) for x in (200, 245, 290, 335, 25)]) + f'''
<path d="M50 112 Q64 120 78 112" fill="none" stroke="#fff" stroke-width="2" opacity=".7"/>
''' + f(64, 98, d=8, k=0.55).replace(O, "#fff") + sparkle(104, 26, 6))

# 4. Тесто (Талдом) — печенье-журавль на кочке из крема
add("cafe-testo-taldom",
    "песочное печенье в форме журавля с белой глазурью",
    "стоит на одной ноге на болотной кочке из заварного крема", "j9_marsh", f'''
<ellipse cx="64" cy="108" rx="34" ry="12" fill="#FFE7A3" {s()}/>
<path d="M44 104 Q50 96 56 104 M70 104 Q76 96 82 104" fill="none" stroke="#E0B54A" stroke-width="2.4"/>
<path d="M62 106 V78" {W(4)}/><path d="M62 92 L70 96" {W(3)}/>
<path d="M34 64 Q40 44 64 46 Q92 48 98 66 Q80 80 56 78 Q40 76 34 64Z" fill="#E7B672" {s()}/>
<path d="M44 62 Q64 56 86 66" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 4"/>
<path d="M92 58 Q96 34 84 24" fill="none" stroke="#E7B672" stroke-width="9" stroke-linecap="round"/>
<path d="M92 58 Q96 34 84 24" fill="none" {W(2)} opacity=".5"/>
<circle cx="82" cy="22" r="9" fill="#E7B672" {s()}/><path d="M80 14 Q84 10 88 14" fill="#E8344F" {W(2)}/>
<path d="M74 22 L58 26 L74 28Z" fill="#4A4A4A" {W(2)}/>
''' + eye(84, 21, 0.7) + f'<path d="M36 64 L20 74 L34 72Z" fill="#3B3355"/>' + sparkle(24, 28, 6))

# 5. Rublevka Village — торт «Птичье молоко» на дачном столике
add("cafe-rublevka-village",
    "кусок торта «Птичье молоко» в шоколадной глазури",
    "отдыхает на дачном столике в саду, над ним порхает бабочка-капустница", "j9_dacha", f'''
<rect x="18" y="96" width="92" height="8" rx="3" fill="#C98A55" {s()}/><path d="M28 104 V124 M100 104 V124" {W(5)}/>
<path d="M30 58 L94 58 L98 94 H26Z" fill="#FFF8EC" {s()}/>
<path d="M30 58 L94 58 L94 66 Q80 72 62 66 Q46 72 30 66Z" fill="#5A3420" {s()}/>
<path d="M28 80 H98" stroke="#F3D9B0" stroke-width="5"/><path d="M27 90 H98" stroke="#C98A55" stroke-width="4"/>
<path d="M92 26 Q84 18 86 30 Q78 36 90 34 M92 26 Q100 18 98 30 Q106 36 94 34" fill="#fff" {W(2)}/><path d="M92 26 V36" {W(2)}/>
''' + f(62, 76, d=9, k=0.7) + sparkle(28, 30, 7))

# 6. Сезам — булочка с кунжутом открывается, как пещера с сокровищами
add("cafe-sezam-khutorskaya",
    "пышная булочка с кунжутом, похожая на пещеру",
    "верхняя половинка поднимается, как дверь «Сезам, откройся», а внутри сияет золото", "j9_cave", f'''
<path d="M20 104 Q20 82 64 82 Q108 82 108 104 Q108 114 64 114 Q20 114 20 104Z" fill="#E9A85A" {s()}/>
<path d="M30 92 Q64 70 98 92" fill="#FFE07A" opacity=".9"/>
<circle cx="52" cy="88" r="5" fill="#FFD23F" {W(2)}/><circle cx="68" cy="84" r="6" fill="#FFD23F" {W(2)}/><circle cx="82" cy="90" r="4" fill="#FFD23F" {W(2)}/>
<path d="M24 74 Q24 30 70 32 Q110 34 104 66 Q100 76 60 76 Q30 78 24 74Z" fill="#F0B866" {s()} transform="rotate(-14 30 76)"/>
''' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.4" ry="1.4" fill="#FFF6DD" transform="rotate({r} {x} {y})"/>'
              for x, y, r in [(42, 40, 20), (56, 34, -10), (70, 36, 30), (84, 42, -20), (50, 50, 10), (66, 48, -30), (78, 54, 15), (38, 56, -15)]) + f'''
''' + f(64, 100, d=9, k=0.7) + sparkle(100, 92, 6, "#FFE07A") + sparkle(26, 92, 4, "#FFE07A"))

# 7. Сытая Утка (Дмитровское) — блинчик по-пекински съезжает по перилам лестницы
add("cafe-sytaya-utka-dmitrovskoe",
    "свёрнутый рулетиком блинчик по-пекински с огуречной соломкой и пёрышком зелёного лука",
    "съезжает по перилам деревянной лестницы со второго яруса", "j9_stair", f'''
''' + "".join(f'<rect x="{x}" y="{y}" width="26" height="12" fill="#B07A4C" {W(2)}/>' for x, y in [(10, 112), (34, 100), (58, 88), (82, 76), (106, 64)]) + f'''
<path d="M14 86 L120 30" stroke="#7A4E2D" stroke-width="6" stroke-linecap="round"/>
''' + "".join(f'<path d="M{x} {112-(x-10)*0.5:.0f} V{86-(x-14)*0.53:.0f}" {W(2)}/>' for x in (22, 46, 70, 94)) + f'''
<g transform="rotate(-27 64 58)">
<rect x="34" y="44" width="58" height="24" rx="12" fill="#FFF0D4" {s()}/>
<path d="M88 46 Q102 36 108 40 M90 50 Q104 46 110 50" fill="none" stroke="#6BBF59" stroke-width="3.4" stroke-linecap="round"/>
<path d="M90 64 L104 70" stroke="#6BBF59" stroke-width="4" stroke-linecap="round"/>
<path d="M40 48 Q46 56 40 64" fill="none" stroke="#E7C79A" stroke-width="2"/>
</g>''' + f(60, 58, d=8, k=0.6) + sparkle(24, 24, 7))

# 8. Натахтари — сладкая када плывёт по реке Арагви
add("cafe-natakhtari-shchelkovsky",
    "сладкая слоёная грузинская када с ореховой начинкой",
    "плывёт, как плот, по реке Арагви мимо старой каменной башни", "j9_aragvi", f'''
<path d="M86 30 H104 V84 H86Z" fill="#CFC4B0" {s()}/><path d="M84 30 L95 18 L106 30Z" fill="#9C5A3C" {s()}/><rect x="91" y="44" width="8" height="12" rx="4" fill="#3B3355"/>
<path d="M0 84 Q32 76 64 84 T128 84 V128 H0Z" fill="#4FA3D9"/>
<path d="M0 98 Q24 92 48 98 T96 98 T144 98" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>
<path d="M18 82 Q20 60 54 58 Q84 58 86 80 Q70 94 50 94 Q24 94 18 82Z" fill="#E9B25C" {s()}/>
<path d="M28 72 Q52 64 76 74" fill="none" stroke="#B9763A" stroke-width="2.4"/><path d="M30 80 Q52 74 74 82" fill="none" stroke="#B9763A" stroke-width="2.4"/>
<circle cx="40" cy="66" r="2.2" fill="#8A5634"/><circle cx="62" cy="64" r="2.2" fill="#8A5634"/>
''' + f(52, 74, d=8, k=0.6) + sparkle(30, 26, 7))

# 9. Ривьера — лимонный тарт садится в море, как солнце
add("cafe-riviera-60-oktyabrya",
    "лимонный тарт с волнистым песочным бортиком",
    "садится в море, как вечернее солнце, рядом качается пальма", "j9_sunset", f'''
<circle cx="58" cy="72" r="34" fill="#E9A85A" {s()}/><circle cx="58" cy="72" r="26" fill="#FFE45C" {W(2.4)}/>
''' + "".join(f'<circle cx="{58+31*math.cos(math.radians(a)):.1f}" cy="{72+31*math.sin(math.radians(a)):.1f}" r="3" fill="#F5C87A"/>' for a in range(0, 360, 30)) + f'''
<path d="M0 84 H128 V128 H0Z" fill="#2F8FD0"/><path d="M10 96 H46 M70 96 H110 M24 108 H60 M80 112 H118" stroke="#FFE45C" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M104 84 Q100 60 106 40" fill="none" stroke="#8A5634" stroke-width="5" stroke-linecap="round"/>
<path d="M106 40 Q90 30 80 40 M106 40 Q118 26 126 34 M106 40 Q100 22 108 14 M106 40 Q124 40 126 52" fill="none" stroke="#3E9E4E" stroke-width="5" stroke-linecap="round"/>
''' + f(58, 66, d=9, k=0.75))

# 10. Гуси-Лебеди — молочная речка с кисельными берегами, по ней плывёт ложка-лодочка
add("cafe-gusi-lebedi-izmaylovo",
    "сказочная молочная речка с розовыми кисельными берегами",
    "по ней плывёт деревянная ложка-лодочка под парусом-листочком", "j9_tale", f'''
<path d="M0 40 Q30 50 40 70 Q50 96 30 128 H0Z" fill="#F36C9B" {s()}/><path d="M128 36 Q96 50 92 72 Q86 98 104 128 H128Z" fill="#F36C9B" {s()}/>
<path d="M10 56 Q22 60 28 70 M114 54 Q102 60 98 72" fill="none" stroke="#FFB3CD" stroke-width="4" stroke-linecap="round"/>
<path d="M40 70 Q50 96 30 128 H104 Q86 98 92 72 Q64 64 40 70Z" fill="#FFFDF8"/>
<path d="M50 104 Q64 100 78 104" fill="none" stroke="#E6E0D6" stroke-width="2.4"/>
<path d="M30 84 Q64 108 98 84 Q90 98 64 98 Q38 98 30 84Z" fill="#D49A5C" {s()}/><path d="M98 84 Q112 74 122 76" fill="none" stroke="#D49A5C" stroke-width="7" stroke-linecap="round"/>
<path d="M62 86 V40" {W(2.6)}/><path d="M62 42 Q90 56 62 80Z" fill="#7CD26E" {W(2.4)}/>
''' + f(56, 90, d=7, k=0.6).replace(O, "#5A3420") + sparkle(64, 24, 7))

# 11. Зизифора — манты пагодой в облаке пара
add("cafe-zizifora-zelenodolskaya",
    "узбекские манты, сложенные в три яруса",
    "стоят пагодой в густом облаке пара, на вершине — веточка зизифоры", "j9_steam", f'''
<path d="M10 96 Q14 80 30 84 Q34 70 50 76 Q60 64 74 74 Q90 64 98 80 Q116 78 118 96Z" fill="#fff" opacity=".85"/>
''' + "".join(f'<path d="M{64-w} {y} Q{64-w} {y-h} 64 {y-h-4} Q{64+w} {y-h} {64+w} {y}Z" fill="#FFF8EA" {s()}/>'
              f'<path d="M{64-w*0.5:.0f} {y-h*0.5:.0f} Q64 {y-h*0.9:.0f} {64+w*0.5:.0f} {y-h*0.5:.0f}" fill="none" stroke="#E2D2B8" stroke-width="2"/>'
              for y, w, h in [(108, 40, 22), (86, 30, 18), (66, 20, 16)]) + f'''
<path d="M64 46 V30" stroke="#5C8F3A" stroke-width="3"/><circle cx="58" cy="34" r="4" fill="#B48ED8" {W(1.8)}/><circle cx="70" cy="30" r="4" fill="#B48ED8" {W(1.8)}/><circle cx="64" cy="24" r="4" fill="#B48ED8" {W(1.8)}/>
''' + f(64, 96, d=10, k=0.75))

# 12. Кавказская пленница — рог изобилия из лаваша на горном уступе
add("cafe-kavkazskaya-plennitsa",
    "рог изобилия, свёрнутый из лаваша",
    "лежит на горном уступе, из него сыплются гранатовые зёрна и грецкие орехи", "j9_peak", f'''
<path d="M-4 128 L40 60 L66 88 L96 40 L132 128Z" fill="#9AA6C8" {s()}/><path d="M86 56 L96 40 L106 58 L98 54 L92 60Z" fill="#fff"/>
<path d="M10 112 H118" {W(3)}/>
<path d="M22 50 Q52 40 74 60 Q90 76 92 100 Q70 98 50 84 Q28 70 22 50Z" fill="#F3D9A4" {s()}/>
<path d="M30 56 Q50 54 64 66 M40 70 Q56 70 70 82" fill="none" stroke="#D9B577" stroke-width="2.4"/>
<ellipse cx="88" cy="98" rx="10" ry="6" fill="#F7E7C0" {s()}/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="2.8" fill="#D0263F" {W(1.4)}/>' for x, y in [(96, 104), (102, 108), (92, 110), (106, 102)]) + f'''
<ellipse cx="78" cy="108" rx="5" ry="4" fill="#B98552" {W(1.8)}/><ellipse cx="110" cy="112" rx="5" ry="4" fill="#B98552" {W(1.8)}/>
''' + f(52, 66, d=8, k=0.6))

# 13. Дудук — матнакаш стоит на вершине Арарата, как ковчег
add("cafe-duduk-simonovsky",
    "овальный армянский хлеб матнакаш с бороздками",
    "стоит на снежной вершине двуглавого Арарата, как ковчег", "j9_carpet", f'''
<path d="M-6 128 L50 50 L72 76 L88 62 L134 128Z" fill="#E6D5C8" {s()}/>
<path d="M38 66 L50 50 L62 66 L54 62 L46 68Z" fill="#fff"/><path d="M80 72 L88 62 L96 72Z" fill="#fff"/>
<path d="M0 116 H128" stroke="#8A2A1C" stroke-width="10"/><path d="M0 116 H128" stroke="#F2C24E" stroke-width="2" stroke-dasharray="6 6"/>
<ellipse cx="50" cy="40" rx="34" ry="16" fill="#E8A653" {s()}/>
''' + "".join(f'<path d="M{x} 30 Q{x+2} 40 {x} 50" fill="none" stroke="#B26E2E" stroke-width="2.4"/>' for x in (34, 44, 54, 64)) + f'''
''' + f(50, 40, d=7, k=0.55) + sparkle(104, 28, 7))

# 14. Август13 — макароны-пенне растут на грядке, как морковки
add("cafe-avgust13-dmitrovskoe",
    "макароны-пенне, растущие на грядке, как морковки",
    "их поливает маленькая садовая лейка, а ботва — из листьев базилика", "j9_garden", f'''
<path d="M0 90 Q64 80 128 90 V128 H0Z" fill="#8A5634"/><path d="M8 100 Q64 92 120 100" fill="none" stroke="#6E4428" stroke-width="3"/>
''' + "".join(f'<g transform="rotate({r} {x} 90)"><rect x="{x-7}" y="66" width="14" height="34" rx="3" fill="#F6C75A" {W(2.2)}/>'
              f'<path d="M{x-7} 74 H{x+7} M{x-7} 82 H{x+7} M{x-7} 90 H{x+7}" stroke="#D9A23A" stroke-width="2"/>'
              f'<path d="M{x} 66 Q{x-10} 54 {x-6} 46 Q{x+2} 56 {x} 66 Q{x+10} 54 {x+8} 46 Q{x} 56 {x} 66" fill="#4FAE4E" {W(1.8)}/></g>'
              for x, r in [(36, -6), (64, 0), (92, 6)]) + f'''
<path d="M86 20 H112 L108 40 H90Z" fill="#5BA4D9" {s()} transform="rotate(20 98 30)"/><path d="M86 30 L70 40" {W(4)}/>
<path d="M68 44 l-3 6 M74 46 l-2 7 M62 46 l-4 5" stroke="#5BA4D9" stroke-width="2.4" stroke-linecap="round"/>
''' + f(64, 80, d=4, k=0.45, blush=False))

# 15. Все Лень — пышка в сахарной пудре дремлет на кувшинке
add("cafe-vse-len-vdnh",
    "пышка в сахарной пудре",
    "дремлет на круглом листе кувшинки посреди пруда, над ней «z-z-z»", "j9_pond", f'''
<ellipse cx="64" cy="98" rx="50" ry="16" fill="#58B65E" {s()}/><path d="M64 98 L108 92 L106 104Z" fill="#2F8E7A"/>
<circle cx="64" cy="80" r="26" fill="#F2BE7A" {s()}/><circle cx="64" cy="80" r="8" fill="#2F8E7A" {W(2)}/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#fff"/>' for x, y in [(48, 66), (56, 60), (72, 62), (80, 70), (46, 84), (84, 88), (60, 98), (74, 96)]) + f'''
<path d="M50 78 Q54 82 58 78 M70 78 Q74 82 78 78" fill="none" {W(2.4)}/>
<path d="M60 90 Q64 92 68 90" fill="none" {W(2.2)}/>
<text x="88" y="44" font-family="Arial" font-weight="bold" font-size="14" fill="#fff" stroke="{O}" stroke-width="1">z</text>
<text x="98" y="32" font-family="Arial" font-weight="bold" font-size="18" fill="#fff" stroke="{O}" stroke-width="1">Z</text>
<circle cx="22" cy="40" r="6" fill="#FF9EC3" {W(1.8)}/>''')

# 16. Menza — соба в плетёной корзинке под водопадом в саду камней
add("cafe-menza-vernadskogo",
    "холодная лапша соба на бамбуковой плетёной решётке-дзару",
    "охлаждается под тонким водопадом в японском саду камней", "j9_zen", f'''
<rect x="56" y="0" width="16" height="70" fill="#9CD7F0" opacity=".8"/><path d="M60 0 V66 M68 0 V66" stroke="#fff" stroke-width="2"/>
<path d="M0 108 H128 V128 H0Z" fill="#E6E2D4"/><path d="M0 114 Q16 110 32 114 T64 114 T96 114 T128 114" fill="none" stroke="#B7AF96" stroke-width="2"/>
<ellipse cx="18" cy="106" rx="14" ry="9" fill="#8C8F86" {s()}/><ellipse cx="112" cy="104" rx="11" ry="8" fill="#A3A69B" {s()}/>
<path d="M24 74 H104 L96 98 H32Z" fill="#D9B577" {s()}/><path d="M28 80 H100 M32 88 H96" stroke="#B48A4C" stroke-width="2"/>
''' + "".join(f'<path d="M{x} 74 Q{x+6} 60 {x+2} 52" fill="none" stroke="#8C6A4A" stroke-width="3" stroke-linecap="round"/>' for x in (40, 52, 64, 76, 88)) + f'''
''' + f(64, 86, d=9, k=0.65))

# 17. ZAGORAMI — снеговик из трёх хинкали на перевале между горами
add("cafe-zagorami-bakuninskaya",
    "хинкали-снеговик из трёх хинкали разного размера",
    "стоит на снежном перевале между двумя горами, руки-веточки машут", "j9_pass", f'''
<path d="M-8 100 L30 30 L64 92 L98 26 L136 100Z" fill="#7C8FB8" {s()}/><path d="M20 48 L30 30 L40 48 L32 44Z" fill="#fff"/><path d="M88 44 L98 26 L108 44 L100 40Z" fill="#fff"/>
<path d="M0 98 Q64 88 128 98 V128 H0Z" fill="#fff" {s()}/>
''' + "".join(f'<path d="M{64-r} {y} Q{64-r} {y-r*1.3:.0f} 64 {y-r*1.5:.0f} Q{64+r} {y-r*1.3:.0f} {64+r} {y}Q64 {y+r*0.5:.0f} {64-r} {y}Z" fill="#F7EAD2" {s()}/>'
              f'<path d="M{64-r*0.5:.0f} {y-r*0.4:.0f} L64 {y-r*1.4:.0f} L{64+r*0.5:.0f} {y-r*0.4:.0f}" fill="none" stroke="#D9C4A0" stroke-width="2"/>'
              for y, r in [(108, 20), (82, 15), (60, 11)]) + f'''
<path d="M50 74 L32 62 M78 74 L96 60" stroke="#7A4E2D" stroke-width="3" stroke-linecap="round"/>
''' + f(64, 50, d=5, k=0.45, blush=False) + f(64, 96, d=7, k=0.55))

# 18. GEORGES — чвиштари читает газету в кресле-качалке
add("cafe-georges-salaris",
    "кукурузная лепёшка чвиштари с сыром",
    "читает газету в плетёном кресле-качалке", "j9_letter", f'''
<path d="M20 112 Q64 126 108 112" fill="none" stroke="#8A5634" stroke-width="5" stroke-linecap="round"/>
<path d="M30 110 L36 50 Q38 38 50 40 H82 Q92 40 94 52 L100 110" fill="#C98A55" {s()}/>
<path d="M40 60 H90 M38 76 H94 M36 92 H96" stroke="#A86E3E" stroke-width="2.4"/>
<ellipse cx="66" cy="84" rx="26" ry="20" fill="#F7C948" {s()}/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#FFF3C4"/>' for x, y in [(52, 76), (80, 74), (60, 96), (78, 94)]) + f'''
<path d="M40 112 L46 92 L90 92 L96 112Z" fill="#fff" {s()}/><path d="M68 92 V112" {W(1.8)}/>
<path d="M52 98 H64 M50 104 H64 M72 98 H86 M72 104 H88" stroke="#9AA6B8" stroke-width="2"/>
''' + f(66, 78, d=8, k=0.65))

# 19. SEASONS — круглый торт из четырёх долей-сезонов вращается, как часы
add("cafe-seasons-leninsky",
    "круглый торт из четырёх долей: снежная, цветочная, солнечная и осенняя",
    "вращается на подставке, как циферблат, а стрелка-ложечка показывает сезон", "j9_year", f'''
<rect x="58" y="104" width="12" height="12" fill="#C9D3E0" {W(2)}/><ellipse cx="64" cy="118" rx="26" ry="5" fill="#C9D3E0" {s()}/>
<path d="M64 64 L64 22 A42 42 0 0 1 106 64Z" fill="#FFFFFF" {s()}/>
<path d="M64 64 L106 64 A42 42 0 0 1 64 106Z" fill="#9DD86B" {s()}/>
<path d="M64 64 L64 106 A42 42 0 0 1 22 64Z" fill="#FFD23F" {s()}/>
<path d="M64 64 L22 64 A42 42 0 0 1 64 22Z" fill="#F08A3A" {s()}/>
<circle cx="80" cy="38" r="2.4" fill="#9CC9F0"/><circle cx="90" cy="48" r="2.4" fill="#9CC9F0"/><circle cx="76" cy="50" r="2" fill="#9CC9F0"/>
<circle cx="84" cy="82" r="4" fill="#FF7FA8"/><circle cx="76" cy="92" r="3" fill="#FF7FA8"/>
<circle cx="44" cy="84" r="6" fill="#FFF6C4" {W(1.6)}/>
<path d="M40 40 q6 -6 10 2 q-6 6 -10 -2Z" fill="#B5452F" {W(1.6)}/>
<path d="M64 64 L86 30" stroke="#8C9DB0" stroke-width="4" stroke-linecap="round"/><circle cx="88" cy="27" r="5" fill="#C9D3E0" {W(2)}/>
''' + f(58, 70, d=7, k=0.55))

# 20. Molon Lave — оливка-спартанец со щитом-питой у колонны
add("cafe-molon-lave",
    "зелёная оливка-спартанец в бронзовом шлеме с гребнем",
    "держит круглый щит из питы и стоит на страже у греческой колонны", "j9_greek", f'''
<rect x="94" y="30" width="22" height="90" fill="#F4F1EA" {s()}/><rect x="90" y="24" width="30" height="8" fill="#F4F1EA" {s()}/>
<path d="M100 34 V118 M106 34 V118 M112 34 V118" stroke="#D8D2C4" stroke-width="2"/>
<ellipse cx="54" cy="80" rx="22" ry="30" fill="#8DB33A" {s()}/>
<path d="M32 62 Q34 36 54 36 Q74 36 76 62 L70 62 Q68 48 54 48 Q40 48 38 62Z" fill="#D49A3A" {s()}/>
<path d="M40 38 Q54 14 70 40" fill="none" stroke="#D0263F" stroke-width="8" stroke-linecap="round"/>
<circle cx="80" cy="92" r="20" fill="#F2D29A" {s()}/><circle cx="80" cy="92" r="12" fill="none" stroke="#C9A060" stroke-width="2.4"/>
<path d="M74 86 l4 2 M82 96 l4 -2 M86 86 l-3 3" stroke="#C9A060" stroke-width="2.4" stroke-linecap="round"/>
''' + f(52, 72, d=8, k=0.6))

# 21. Клево — спагетти на катушке спиннинга, клюёт
add("cafe-klevo-petrovka",
    "спагетти, намотанные на катушку спиннинга",
    "кто-то клюёт: удочка гнётся над прудом, леска-спагеттина натянута", "j9_pier", f'''
<path d="M0 84 Q32 78 64 84 T128 84 V128 H0Z" fill="#3E9FCF"/><path d="M8 100 Q30 96 52 100 M70 108 Q92 104 114 108" fill="none" stroke="#fff" stroke-width="2.4" opacity=".7"/>
<path d="M14 116 L92 22" stroke="#7A4E2D" stroke-width="5" stroke-linecap="round"/>
<path d="M92 22 Q112 40 108 94" fill="none" stroke="#F6C75A" stroke-width="3"/>
<circle cx="108" cy="96" r="5" fill="#E8344F" {W(2)}/><path d="M100 98 Q108 90 116 98" fill="none" stroke="#fff" stroke-width="2"/>
<circle cx="42" cy="82" r="18" fill="#F6C75A" {s()}/>
''' + "".join(f'<path d="M{42-r} 82 A{r} {r} 0 0 1 {42+r} 82" fill="none" stroke="#D9A23A" stroke-width="2"/>' for r in (6, 11, 15)) + f'''
<path d="M42 82 L30 94" {W(3)}/><circle cx="28" cy="96" r="4" fill="#C9D3E0" {W(2)}/>
''' + f(42, 80, d=6, k=0.5))

# 22. FIGO — бискотти строит мостик между двумя чашками эспрессо
add("cafe-figo-smolenskaya",
    "миндальное печенье бискотти",
    "лежит мостиком между двумя чашками эспрессо, по нему шагает кофейное зёрнышко", "j9_espresso", f'''
''' + "".join(f'<path d="M{x-16} 70 H{x+16} L{x+12} 100 H{x-12}Z" fill="#FFFFFF" {s()}/><path d="M{x+16} 76 Q{x+26} 80 {x+14} 92" fill="none" {W(3)}/>'
              f'<ellipse cx="{x}" cy="70" rx="16" ry="4" fill="#5A3420" {W(2)}/><ellipse cx="{x}" cy="104" rx="22" ry="4" fill="#E7EEF5" {W(2)}/>'
              for x in (26, 98)) + f'''
<path d="M22 64 Q62 46 102 64 L100 72 Q62 56 24 72Z" fill="#E7B672" {s()}/>
<ellipse cx="46" cy="60" rx="3" ry="2" fill="#F7E3C0"/><ellipse cx="62" cy="56" rx="3" ry="2" fill="#F7E3C0"/><ellipse cx="80" cy="60" rx="3" ry="2" fill="#F7E3C0"/>
<ellipse cx="64" cy="42" rx="8" ry="10" fill="#6B3A20" {s()}/><path d="M64 33 Q60 42 64 51" fill="none" stroke="#C98A55" stroke-width="2"/>
''' + f(62, 66, d=8, k=0.55) + sparkle(104, 30, 6))

# 23. Мамина пицца — пицца-мама везёт в коляске мини-пиццетту
add("cafe-mamina-pizza-columbus",
    "большая круглая пицца-мама",
    "везёт в детской коляске малышку-пиццетту по галерее торгового центра", "j9_mall", f'''
<path d="M0 112 H128" stroke="#E6B9D8" stroke-width="10"/>
<circle cx="42" cy="66" r="28" fill="#F2B45A" {s()}/><circle cx="42" cy="66" r="21" fill="#FF8A4A"/>
<circle cx="34" cy="56" r="4" fill="#C0283C"/><circle cx="54" cy="70" r="4" fill="#C0283C"/><circle cx="32" cy="78" r="3.5" fill="#C0283C"/>
<path d="M28 92 L22 110 M56 92 L62 110" {W(4)}/>
<path d="M66 70 L82 70" {W(4)}/>
<path d="M78 70 H118 Q118 100 98 100 Q78 100 78 70Z" fill="#7EC8E3" {s()}/><path d="M80 70 Q98 52 118 70Z" fill="#5BA4D9" {s()}/>
<circle cx="86" cy="106" r="6" fill="#fff" {W(2.4)}/><circle cx="112" cy="106" r="6" fill="#fff" {W(2.4)}/>
<circle cx="100" cy="76" r="10" fill="#F2B45A" {W(2.2)}/><circle cx="97" cy="74" r="2" fill="#C0283C"/>
''' + f(42, 66, d=8, k=0.65) + f(100, 78, d=4, k=0.35, blush=False))

# 24. Шикари — вьетнамский бань-ми крадётся сквозь бамбук
add("cafe-shikari-leninsky",
    "вьетнамский багет-сэндвич бань-ми с зеленью",
    "крадётся на цыпочках сквозь заросли бамбука, как охотник", "j9_bamboo", f'''
''' + "".join(f'<rect x="{x}" y="-4" width="10" height="136" rx="4" fill="#7CBF4A" {W(2)}/><path d="M{x} 30 H{x+10} M{x} 70 H{x+10} M{x} 108 H{x+10}" {W(1.8)}/>'
              for x in (6, 104, 116)) + f'''
<path d="M114 40 Q100 30 92 38 M8 60 Q22 50 30 58" fill="none" stroke="#5E9A3A" stroke-width="4" stroke-linecap="round"/>
<path d="M22 66 Q30 50 64 52 Q98 54 104 70 Q98 84 64 84 Q30 82 22 66Z" fill="#E9B25C" {s()}/>
<path d="M28 68 Q64 76 100 70" fill="none" {W(2)}/>
<path d="M34 70 l4 -6 l4 6 l4 -6 l4 6 l4 -6 l4 6 l4 -6 l4 6 l4 -6 l4 6 l4 -6 l4 6 l4 -6 l4 6" fill="none" stroke="#4FAE4E" stroke-width="3"/>
<path d="M40 52 Q46 48 52 52 M66 50 Q72 46 78 50" fill="none" stroke="#C98A55" stroke-width="2"/>
<path d="M40 84 L34 100 L42 100 M86 84 L92 100 L100 100" fill="none" {W(3.4)}/>
''' + f(64, 60, d=8, k=0.55))

# 25. Рыбная мануфактура №1 — банка шпрот открывается ключом
add("cafe-rybnaya-manufaktura-krasny-kit",
    "золотистые шпроты в плоской консервной банке",
    "банку открыли ключом-закруткой, и рыбки выглядывают, лёжа на льду витрины", "j9_ice", f'''
<path d="M0 100 H128 V128 H0Z" fill="#DDEFFC"/>
''' + "".join(f'<path d="M{x} 104 l6 -5 l6 5 l-6 5Z" fill="#fff" {W(1.4)}/>' for x in (8, 30, 98, 112)) + f'''
<rect x="20" y="62" width="88" height="42" rx="12" fill="#C9D3E0" {s()}/><rect x="26" y="68" width="76" height="30" rx="8" fill="#F2D48C"/>
''' + "".join(f'<path d="M30 {y} Q60 {y-6} 92 {y} L98 {y-4} L98 {y+4} L92 {y} Q60 {y+6} 30 {y}Z" fill="#D99A3A" {W(1.8)}/>' for y in (74, 83, 92)) + f'''
<path d="M20 64 Q40 30 96 34 Q110 36 108 46" fill="#E7EEF5" {s()}/>
<path d="M96 34 Q112 22 116 30 Q118 38 108 40" fill="none" {W(3)}/>
''' + eye(38, 74, 0.5) + eye(38, 83, 0.5) + eye(38, 92, 0.5))

# 26. Кикухана — ролл-хризантема на чёрной тарелке рядом с игральным кубиком
add("cafe-kikukhana-kvartal",
    "ролл-хризантема с лепестками из ломтиков лосося",
    "распускается на чёрной лаковой тарелке рядом с игральным кубиком", "j9_lacquer", f'''
<ellipse cx="60" cy="80" rx="48" ry="32" fill="#1C1C20" stroke="#C9A060" stroke-width="2.4"/>
''' + "".join(f'<ellipse cx="{60+20*math.cos(math.radians(a)):.1f}" cy="{74+20*math.sin(math.radians(a)):.1f}" rx="12" ry="6" fill="#FF8A5B" {W(1.8)} transform="rotate({a} {60+20*math.cos(math.radians(a)):.1f} {74+20*math.sin(math.radians(a)):.1f})"/>'
              for a in range(0, 360, 40)) + f'''
<circle cx="60" cy="74" r="14" fill="#FFFFFF" {s()}/><circle cx="60" cy="74" r="7" fill="#F7C948"/>
<rect x="94" y="28" width="22" height="22" rx="4" fill="#fff" {s()} transform="rotate(12 105 39)"/>
<circle cx="100" cy="34" r="2.2" fill="{O}"/><circle cx="106" cy="40" r="2.2" fill="{O}"/><circle cx="112" cy="46" r="2.2" fill="{O}"/>
''' + f(60, 72, d=5, k=0.45, blush=False) + sparkle(24, 30, 6, "#F7C948"))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w").write(ICONS[i])
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg).read().splitlines()
    have = {l.split(" — ")[0] for l in lines}
    for i in ids:
        h, sc = SUBJ[i]
        line = f"{i} — герой: {h} | сцена: {sc}"
        if i in have:
            lines = [line if l.split(" — ")[0] == i else l for l in lines]
        else:
            lines.append(line)
    open(reg, "w").write("\n".join(lines) + "\n")
    print("svg", len(ids))
