"""Иконки робота cafes, 2026-11-13 (01 UTC). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности):
герои и сцены сверены поиском по icons-src/subjects.txt; палитры фона — свои.
Запуск: python3 tools/icons_cafes_1113a.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
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
    "za_rug": ("#FFF4E8", "#E7A9C8"),
    "za_terrace": ("#F2FFE6", "#8CC96A"),
    "za_belfry": ("#E9F4FF", "#7DA7E0"),
    "za_bloom": ("#FFFFF4", "#B9D98F"),
    "za_burrow": ("#FFF3C9", "#E9B04B"),
    "za_steam": ("#F6EDE4", "#A9805E"),
    "za_dusk": ("#5A4C9C", "#22204F"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Здрасте (Ясеневая ул., 12к5): мячик-погремушка катится по ковру детского уголка
add("cafe-zdraste-yasenevaya-12",
    "мягкий тряпичный мячик-погремушка из шести разноцветных долек с бубенчиком внутри",
    "катится по полосатому ковру детского уголка кофейни, за ним разлетаются звонкие «дзынь»-чёрточки",
    "za_rug", f'''
<path d="M-4 96 L132 86 L132 132 L-4 132Z" fill="#7FC6E8" {W(3)}/>
<path d="M-4 106 L132 96 M-4 117 L132 107" stroke="#FFFFFF" stroke-width="5" opacity=".75"/>
<path d="M14 54 L22 58 M10 66 L20 66 M14 78 L22 74" stroke="{O}" stroke-width="2.8" stroke-linecap="round"/>
<circle cx="66" cy="62" r="36" fill="#FFD25A" {W(3.4)}/>
<path d="M66 26 Q44 44 46 62 Q48 82 66 98 Q60 80 60 62 Q60 44 66 26Z" fill="#F2667A"/>
<path d="M66 26 Q88 44 86 62 Q84 82 66 98 Q72 80 72 62 Q72 44 66 26Z" fill="#5FB7F0"/>
<path d="M66 26 Q34 36 30 62 Q34 82 66 98 Q42 82 44 62 Q46 42 66 26Z" fill="#7BCF6A"/>
<path d="M66 26 Q98 36 102 62 Q98 82 66 98 Q90 82 88 62 Q86 42 66 26Z" fill="#B48CF0"/>
<circle cx="66" cy="62" r="36" fill="none" {W(3.4)}/>
<path d="M66 26 Q46 44 46 62 Q48 82 66 98 M66 26 Q86 44 86 62 Q84 82 66 98 M66 26 Q36 38 32 62 M66 26 Q96 38 100 62" fill="none" stroke="{O}" stroke-width="2" opacity=".55"/>
<rect x="50" y="56" width="32" height="24" rx="11" fill="#FFF8EC" {W(2.4)}/>
{eye(59, 66, 0.8)}{eye(73, 66, 0.8)}
<path d="M62 73 Q66 77 70 73" fill="none" {W(2)}/>
{BL(54, 74)}{BL(78, 74)}
<circle cx="112" cy="34" r="5" fill="#FFD25A" {W(2)}/><path d="M110 38 L114 38" {W(1.6)}/>
''')

# 2. Додо (Пушкино, ул. Чехова): кусок пиццы-скрипач на летней веранде
add("cafe-dodo-pushkino-chekhova",
    "треугольный кусок пиццы-скрипач с кружками колбаски и тянущимся сыром",
    "играет на маленькой скрипке, водя смычком-палочкой гриссини, на летней веранде с гирляндой лампочек",
    "za_terrace", f'''
<path d="M2 22 Q64 40 126 20" fill="none" stroke="{O}" stroke-width="2"/>
<g {W(1.8)}><circle cx="20" cy="27" r="4" fill="#FFE07A"/><circle cx="44" cy="32" r="4" fill="#FF9E7A"/><circle cx="84" cy="32" r="4" fill="#9DE0FF"/><circle cx="108" cy="26" r="4" fill="#FFE07A"/></g>
<path d="M0 104 L128 104 L128 128 L0 128Z" fill="#C98A55" {W(3)}/>
<path d="M30 104 L30 128 M64 104 L64 128 M98 104 L98 128" stroke="{O}" stroke-width="2" opacity=".5"/>
<path d="M30 44 L92 44 L62 104Z" fill="#FFCF5A" {W(3.4)}/>
<path d="M26 40 Q61 30 96 40 Q98 48 92 50 L30 50 Q24 48 26 40Z" fill="#E09A4A" {W(3)}/>
<g fill="#D9473C" stroke="{O}" stroke-width="1.8"><circle cx="44" cy="60" r="5"/><circle cx="74" cy="58" r="4.6"/></g>
<path d="M54 86 Q52 94 56 96" fill="none" stroke="#FFE9A0" stroke-width="3" stroke-linecap="round"/>
{eye(52, 68, 0.8)}{eye(66, 68, 0.8)}
<path d="M55 76 Q59 80 63 76" fill="none" {W(2)}/>
<path d="M78 74 Q88 64 100 70 Q110 76 104 86 Q112 94 102 100 Q92 104 86 96 Q76 98 76 88 Q70 80 78 74Z" fill="#B5652E" {W(2.8)}/>
<path d="M90 76 L108 54" {W(3)}/>
<rect x="104" y="46" width="7" height="10" rx="2" fill="#7A3D1C" {W(2)}/>
<path d="M86 82 L92 92 M92 82 L86 92" stroke="{O}" stroke-width="1.6" opacity=".6"/>
<path d="M60 92 L118 62" stroke="#E8C27A" stroke-width="5" stroke-linecap="round"/>
<path d="M60 92 L118 62" fill="none" {W(1.8)} opacity=".6"/>
<path d="M18 74 Q22 68 18 62 M14 88 L14 80 Q20 78 20 84" fill="none" stroke="{O}" stroke-width="2.4"/>
''')

# 3. Додо (Сергиев Посад, 1-я Рыбная): кусок пиццы-звонарь у колоколов
add("cafe-dodo-sergiev-posad-rybnaya",
    "кусок пиццы-звонарь в красной косоворотке с кружками пепперони",
    "стоит на белой звоннице под тремя золотыми колоколами и тянет за их верёвки, колокола звенят",
    "za_belfry", f'''
<path d="M8 40 L120 40 L112 30 L16 30Z" fill="#FFFFFF" {W(2.8)}/>
<path d="M14 40 L14 110 M114 40 L114 110" {W(4)}/>
<rect x="8" y="104" width="112" height="24" fill="#F4F0E8" {W(3)}/>
<g fill="#F2C53D" stroke="{O}" stroke-width="2.6">
<path d="M26 44 Q26 58 20 64 L44 64 Q38 58 38 44 Q32 40 26 44Z"/>
<path d="M56 44 Q56 56 51 62 L77 62 Q72 56 72 44 Q64 39 56 44Z"/>
<path d="M90 44 Q90 58 84 64 L108 64 Q102 58 102 44 Q96 40 90 44Z"/></g>
<g fill="{O}"><circle cx="32" cy="66" r="2.6"/><circle cx="64" cy="64" r="2.8"/><circle cx="96" cy="66" r="2.6"/></g>
<path d="M32 68 Q36 80 46 86 M64 66 L64 80 M96 68 Q92 80 82 86" fill="none" stroke="#8A5A2B" stroke-width="2.2"/>
<path d="M44 82 L84 82 L64 116Z" fill="#FFCF5A" {W(3.2)}/>
<path d="M42 78 Q64 70 86 78 Q88 84 84 86 L44 86 Q40 84 42 78Z" fill="#E09A4A" {W(2.8)}/>
<path d="M50 88 L78 88 L72 98 L56 98Z" fill="#E2483F" opacity=".9"/>
<g fill="#B8322B" stroke="{O}" stroke-width="1.4"><circle cx="58" cy="102" r="3"/><circle cx="70" cy="101" r="2.6"/></g>
{eye(58, 92, 0.7)}{eye(70, 92, 0.7)}
<path d="M18 50 Q14 46 16 40 M110 50 Q114 46 112 40" fill="none" stroke="{O}" stroke-width="2.4"/>
<path d="M8 20 Q12 16 16 20 M112 14 Q116 10 120 14" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
''')

# 4. Здрасте (Новочерёмушкинская, 17): печенье-цветок черёмухи в пакетике с собой
add("cafe-zdraste-novocheremushkinskaya-17",
    "песочное печенье в форме цветка черёмухи — пять белых глазурных лепестков и жёлтая серединка",
    "выглядывает из крафтового бумажного пакетика с собой, сверху на него падают белые лепестки",
    "za_bloom", f'''
<g fill="#FFFFFF" stroke="{O}" stroke-width="1.4"><ellipse cx="18" cy="24" rx="4" ry="2.6" transform="rotate(30 18 24)"/><ellipse cx="104" cy="18" rx="4" ry="2.6" transform="rotate(-20 104 18)"/><ellipse cx="112" cy="50" rx="3.6" ry="2.4"/><ellipse cx="26" cy="56" rx="3.6" ry="2.4" transform="rotate(50 26 56)"/></g>
<path d="M30 70 L98 70 L104 124 L24 124Z" fill="#C99A62" {W(3.4)}/>
<path d="M30 70 L36 64 L44 70 L52 64 L60 70 L68 64 L76 70 L84 64 L92 70 L98 64" fill="none" {W(2.6)}/>
<path d="M40 88 L88 88" stroke="#A67A46" stroke-width="3" stroke-linecap="round"/>
<g fill="#FFFDF7" stroke="{O}" stroke-width="3">
<circle cx="64" cy="30" r="15"/><circle cx="88" cy="47" r="15"/><circle cx="79" cy="74" r="15"/><circle cx="49" cy="74" r="15"/><circle cx="40" cy="47" r="15"/></g>
<circle cx="64" cy="54" r="17" fill="#FFD44D" {W(3)}/>
<g fill="#E9B32E"><circle cx="58" cy="44" r="1.4"/><circle cx="72" cy="46" r="1.4"/><circle cx="64" cy="64" r="1.4"/></g>
{eye(58, 53, 0.75)}{eye(70, 53, 0.75)}
<path d="M61 60 Q64 63 67 60" fill="none" {W(1.8)}/>
{BL(53, 59)}{BL(75, 59)}
''')

# 5. Додо (ТЦ «Нора», пр-т Андропова, 22): кружок пепперони выглядывает из норки в сырном холме
add("cafe-dodo-andropova-nora",
    "кружок пепперони-малыш с белыми крапинками жира",
    "выглядывает из круглой норки с деревянной дверцей в склоне большого сырного холма с дырочками",
    "za_burrow", f'''
<path d="M-4 128 L-4 80 Q20 34 64 32 Q108 34 132 76 L132 128Z" fill="#FFD95E" {W(3.4)}/>
<g fill="#F0B83A" stroke="{O}" stroke-width="2"><ellipse cx="24" cy="76" rx="7" ry="5"/><ellipse cx="104" cy="70" rx="8" ry="6"/><ellipse cx="96" cy="108" rx="6" ry="4.4"/><ellipse cx="18" cy="108" rx="5" ry="3.6"/></g>
<ellipse cx="62" cy="82" rx="30" ry="28" fill="#5A3A22" {W(3.2)}/>
<path d="M84 64 Q98 70 96 98 L88 104 Q90 78 80 70Z" fill="#B87A44" {W(2.6)}/>
<circle cx="90" cy="86" r="2" fill="{O}"/>
<circle cx="58" cy="86" r="20" fill="#D63E35" {W(3.2)}/>
<g fill="#FFE3D6"><circle cx="46" cy="80" r="1.8"/><circle cx="70" cy="78" r="1.6"/><circle cx="64" cy="98" r="1.6"/><circle cx="48" cy="96" r="1.4"/></g>
{eye(52, 86, 0.8)}{eye(64, 86, 0.8)}
<path d="M55 93 Q58 96 61 93" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
<path d="M40 90 Q34 88 36 82 M76 90 Q82 88 80 82" fill="none" {W(2.6)}/>
{sparkle(34, 22, 5)}{sparkle(100, 26, 4)}
''')

# 6. Капучинофф (пр-т Андропова, 37): молочник наливает пенку и рисует листик
add("cafe-kapuchinoff-andropova-37",
    "стальной молочник-питчер с длинным носиком и ручкой-петелькой",
    "наклонился над широкой белой чашкой на блюдце и тонкой струйкой рисует на кофейной пенке листик",
    "za_steam", f'''
<ellipse cx="60" cy="108" rx="46" ry="10" fill="#FFFFFF" {W(3)}/>
<path d="M22 82 Q22 108 60 108 Q98 108 98 82Z" fill="#FFFFFF" {W(3.2)}/>
<path d="M98 86 Q112 86 110 96 Q108 104 96 102" fill="none" {W(3)}/>
<ellipse cx="60" cy="82" rx="38" ry="9" fill="#B4774A" {W(3)}/>
<ellipse cx="60" cy="82" rx="30" ry="6.5" fill="#F3E2CC"/>
<path d="M44 82 Q60 74 76 82 Q60 90 44 82Z" fill="#C08A5E" opacity=".8"/>
<path d="M48 82 L74 82" stroke="#F3E2CC" stroke-width="1.6"/>
<path d="M60 40 L60 80" stroke="#FFF6EA" stroke-width="3.4" stroke-linecap="round"/>
<g transform="rotate(-38 82 36)">
<path d="M62 22 L100 22 L104 58 Q84 64 64 58Z" fill="#D7DEE6" {W(3.2)}/>
<path d="M62 22 Q56 22 50 30 L62 30Z" fill="#D7DEE6" {W(2.6)}/>
<path d="M104 30 Q116 32 114 42 Q112 50 102 48" fill="none" {W(3.2)}/>
<path d="M70 28 L72 52" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity=".8"/>
{eye(80, 40, 0.8)}{eye(92, 40, 0.8)}
<path d="M83 48 Q86 51 89 48" fill="none" {W(1.8)}/>
{BL(76, 47)}{BL(96, 47)}
</g>
<path d="M30 68 Q26 60 30 52 M40 64 Q36 58 40 50" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
''')

# 7. Додо (Жуковский, ул. Баженова): пицца-НЛО зависла над крышами и опускает луч
add("cafe-dodo-zhukovsky-bazhenova",
    "круглая пицца-летающая тарелка с прозрачным куполом и сырными огоньками по краю",
    "зависла в сумерках над крышами домов и опускает жёлтый луч на коробку пиццы во дворе",
    "za_dusk", f'''
<g fill="#FFFFFF"><circle cx="16" cy="24" r="1.4"/><circle cx="108" cy="18" r="1.4"/><circle cx="96" cy="40" r="1"/><circle cx="24" cy="48" r="1"/></g>
<path d="M44 66 L84 66 L100 112 L28 112Z" fill="#FFE27A" opacity=".45"/>
<g {W(2.6)}><path d="M0 128 L0 96 L18 96 L18 88 L34 88 L34 128Z" fill="#3B3570"/><path d="M96 128 L96 90 L112 90 L112 98 L128 98 L128 128Z" fill="#3B3570"/></g>
<g fill="#FFE27A"><rect x="6" y="102" width="5" height="5"/><rect x="22" y="94" width="5" height="5"/><rect x="102" y="96" width="5" height="5"/><rect x="116" y="104" width="5" height="5"/></g>
<rect x="50" y="104" width="28" height="12" rx="2" fill="#F07A3A" {W(2.6)}/>
<path d="M50 108 L78 108" stroke="{O}" stroke-width="1.6"/>
<path d="M44 42 Q44 22 64 22 Q84 22 84 42Z" fill="#BFE9FF" {W(3)} opacity=".95"/>
<ellipse cx="64" cy="52" rx="48" ry="16" fill="#E8A447" {W(3.4)}/>
<ellipse cx="64" cy="49" rx="40" ry="10" fill="#FFD25A"/>
<g fill="#D9473C" stroke="{O}" stroke-width="1.6"><circle cx="40" cy="50" r="4"/><circle cx="88" cy="50" r="4"/></g>
{eye(56, 50, 0.75)}{eye(72, 50, 0.75)}
<path d="M61 56 Q64 59 67 56" fill="none" {W(1.8)}/>
<g fill="#FFF3A6" stroke="{O}" stroke-width="1.6"><circle cx="22" cy="58" r="3"/><circle cx="40" cy="64" r="3"/><circle cx="64" cy="67" r="3"/><circle cx="88" cy="64" r="3"/><circle cx="106" cy="58" r="3"/></g>
<path d="M56 32 Q60 28 64 30" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
''')

draw_icons.BG.update({
    "zb_latte": ("#FFF8EE", "#D9A77A"),
    "zb_river": ("#EAF8FF", "#6FB4D8"),
    "zb_izba": ("#FFF0E6", "#D98A6A"),
    "zb_rock": ("#F0F4F8", "#8FA3B8"),
    "zb_ember": ("#FFE9D6", "#E0633A"),
    "zb_dune": ("#FFF6DC", "#E2B65A"),
    "zb_ice": ("#F0FBFF", "#8ECFF0"),
})

# 8. Миндаль и кофе (Первомайская, 52): миндальный орешек плавает в чашке кофе, как в бассейне
add("cafe-mindal-kofe-pervomayskaya-52",
    "миндальный орешек-малыш в бархатной коричневой кожице",
    "плавает в широкой кофейной чашке с молочной пенкой, как в бассейне, держась ручками за край",
    "zb_latte", f'''
<ellipse cx="64" cy="112" rx="50" ry="9" fill="#FFFFFF" {W(3)}/>
<path d="M16 70 Q16 108 64 108 Q112 108 112 70Z" fill="#5FA6D6" {W(3.4)}/>
<path d="M24 84 Q34 80 44 84 M84 92 Q94 88 104 92" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
<path d="M112 76 Q126 76 124 88 Q122 98 108 96" fill="none" {W(3.2)}/>
<ellipse cx="64" cy="70" rx="48" ry="12" fill="#A8693E" {W(3.2)}/>
<ellipse cx="64" cy="70" rx="40" ry="8.5" fill="#F4E4CE"/>
<path d="M64 26 Q86 34 86 58 Q84 76 64 78 Q44 76 42 58 Q42 34 64 26Z" fill="#B27445" {W(3.2)}/>
<path d="M54 36 Q50 48 52 62 M74 36 Q78 48 76 62 M64 30 L64 42" fill="none" stroke="#8C5530" stroke-width="2" stroke-linecap="round"/>
{eye(56, 54, 0.85)}{eye(72, 54, 0.85)}
<path d="M60 63 Q64 67 68 63" fill="none" {W(2)}/>
{BL(50, 61)}{BL(78, 61)}
<path d="M42 62 Q32 64 30 70 M86 62 Q96 64 98 70" fill="none" stroke="#B27445" stroke-width="5" stroke-linecap="round"/>
<path d="M42 62 Q32 64 30 70 M86 62 Q96 64 98 70" fill="none" {W(1.6)}/>
<ellipse cx="38" cy="74" rx="7" ry="2.4" fill="#FFFFFF" opacity=".9"/><ellipse cx="92" cy="74" rx="7" ry="2.4" fill="#FFFFFF" opacity=".9"/>
''')

# 9. Додо (Лобня, ул. Катюшки): кусок пиццы-Катюша поёт на высоком берегу
add("cafe-dodo-lobnya-katyushki",
    "кусок пиццы-Катюша в синем платочке с двумя светлыми косичками",
    "стоит на высоком зелёном берегу над рекой у тонкой берёзки и поёт, вокруг летят ноты",
    "zb_river", f'''
<path d="M0 98 Q40 92 80 100 Q104 104 128 98 L128 128 L0 128Z" fill="#4F9CD0" {W(2.6)}/>
<path d="M14 110 Q24 106 34 110 M70 116 Q80 112 90 116" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" opacity=".8"/>
<path d="M-4 104 L-4 76 Q40 66 100 82 L92 102Z" fill="#7BCF6A" {W(3)}/>
<path d="M104 96 L106 36" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path d="M104 96 L106 36" fill="none" {W(2)}/>
<path d="M102 52 L106 52 M104 66 L108 66 M103 80 L107 80" stroke="{O}" stroke-width="2"/>
<g fill="#9AD86A" stroke="{O}" stroke-width="1.6"><ellipse cx="96" cy="40" rx="6" ry="4"/><ellipse cx="114" cy="46" rx="6" ry="4"/><ellipse cx="98" cy="58" rx="5" ry="3.4"/></g>
<path d="M30 40 L82 40 L56 96Z" fill="#FFCF5A" {W(3.2)}/>
<path d="M28 36 Q56 28 84 36 Q86 44 80 44 L32 44 Q26 42 28 36Z" fill="#E09A4A" {W(2.8)}/>
<path d="M30 40 Q30 20 56 18 Q82 20 82 40 Q74 32 56 32 Q38 32 30 40Z" fill="#3D6FD1" {W(3)}/>
<g fill="#FFFFFF"><circle cx="44" cy="26" r="1.6"/><circle cx="58" cy="22" r="1.6"/><circle cx="70" cy="26" r="1.6"/></g>
<path d="M32 42 Q24 54 28 66 M80 42 Q88 54 84 66" fill="none" stroke="#F2D27A" stroke-width="5" stroke-linecap="round"/>
<path d="M32 42 Q24 54 28 66 M80 42 Q88 54 84 66" fill="none" {W(1.6)}/>
<g fill="#D9473C" stroke="{O}" stroke-width="1.4"><circle cx="28" cy="68" r="3"/><circle cx="84" cy="68" r="3"/></g>
<g fill="#D9473C" stroke="{O}" stroke-width="1.6"><circle cx="48" cy="70" r="3.6"/><circle cx="62" cy="76" r="3.4"/></g>
{eye(49, 52, 0.75)}{eye(63, 52, 0.75)}
<ellipse cx="56" cy="61" rx="3" ry="3.6" fill="#B03A4A" {W(1.6)}/>
<path d="M14 30 L14 20 L20 18 L20 28 M12 30 a2.6 2 0 1 0 0.1 0 M18 28 a2.6 2 0 1 0 0.1 0" fill="{O}" stroke="{O}" stroke-width="1.6"/>
<path d="M92 16 L92 8 M90 16 a2.4 1.8 0 1 0 0.1 0" fill="{O}" stroke="{O}" stroke-width="1.6"/>
''')

# 10. Шале (Клин): кувшин брусничного морса наливает в два стаканчика
add("cafe-shale-klin-mira",
    "пузатый глиняный кувшин брусничного морса с ягодками на горлышке",
    "наклонился над деревянным столом у окна с клетчатой занавеской и разливает морс в два маленьких стаканчика",
    "zb_izba", f'''
<rect x="8" y="10" width="58" height="46" rx="3" fill="#CFEFFF" {W(2.6)}/>
<path d="M37 10 L37 56 M8 33 L66 33" stroke="{O}" stroke-width="2"/>
<path d="M6 8 L28 8 Q24 30 6 40Z M68 8 L46 8 Q50 30 68 40Z" fill="#E86A6A" {W(2.2)}/>
<path d="M10 14 L24 14 M10 22 L22 22 M58 14 L64 14 M56 22 L64 22" stroke="#FFFFFF" stroke-width="2" opacity=".8"/>
<path d="M0 104 L128 104 L128 128 L0 128Z" fill="#B8814E" {W(3)}/>
<path d="M0 114 L128 114" stroke="{O}" stroke-width="1.8" opacity=".5"/>
<g fill="#FFFFFF" stroke="{O}" stroke-width="2.6"><path d="M22 84 L42 84 L40 104 L24 104Z"/><path d="M48 88 L66 88 L64 104 L50 104Z"/></g>
<path d="M24 92 L40 92 L40 104 L24 104Z M50 96 L64 96 L64 104 L50 104Z" fill="#C8243C" opacity=".85"/>
<g transform="rotate(-28 92 62)">
<path d="M80 34 Q76 46 72 54 Q64 72 72 90 Q82 102 98 102 Q114 102 120 88 Q126 72 116 54 Q112 46 108 34Z" fill="#D07A43" {W(3.2)}/>
<path d="M78 34 L110 34 L106 26 L82 26Z" fill="#D07A43" {W(2.8)}/>
<path d="M82 26 L74 20" {W(3)}/>
<path d="M118 58 Q132 60 128 76 Q124 86 116 82" fill="none" {W(3.2)}/>
<path d="M74 70 Q96 78 120 70" fill="none" stroke="#F4E2C6" stroke-width="4"/>
{eye(90, 60, 0.8)}{eye(104, 60, 0.8)}
<path d="M93 68 Q97 71 101 68" fill="none" {W(1.8)}/>
{BL(84, 66)}{BL(110, 66)}
<g fill="#C8243C" stroke="{O}" stroke-width="1.4"><circle cx="86" cy="32" r="3"/><circle cx="92" cy="30" r="3"/><circle cx="98" cy="32" r="3"/></g>
<path d="M92 26 Q94 20 100 20" fill="none" stroke="#3E8B3E" stroke-width="2.4"/>
</g>
<path d="M58 66 Q48 72 34 84" fill="none" stroke="#C8243C" stroke-width="3.2" stroke-linecap="round"/>
''')

# 11. Додо (Дмитров): кусок пиццы-скалолаз лезет по сырной стене
add("cafe-dodo-dmitrov-moskovskaya",
    "кусок пиццы-скалолаз в оранжевой каске и с обвязкой",
    "лезет вверх по отвесной сырной стене, хватаясь за дырочки-зацепы, сверху свисает страховочная верёвка",
    "zb_rock", f'''
<path d="M40 -4 L132 -4 L132 132 L30 132 Q26 64 40 -4Z" fill="#FFD95E" {W(3.4)}/>
<g fill="#F0B83A" stroke="{O}" stroke-width="2"><ellipse cx="96" cy="20" rx="8" ry="6"/><ellipse cx="112" cy="58" rx="6" ry="5"/><ellipse cx="100" cy="104" rx="9" ry="6"/><ellipse cx="54" cy="16" rx="5" ry="4"/><ellipse cx="50" cy="112" rx="6" ry="4"/></g>
<path d="M76 -4 L76 40" stroke="#E2483F" stroke-width="3" stroke-linecap="round"/>
<path d="M76 -4 L76 40" fill="none" {W(1.2)}/>
<g transform="rotate(-12 70 70)">
<path d="M48 48 L94 48 L72 112Z" fill="#FFCF5A" {W(3.2)}/>
<path d="M44 44 Q70 36 98 44 Q100 52 94 54 L48 54 Q42 52 44 44Z" fill="#E09A4A" {W(2.8)}/>
<path d="M52 44 Q52 26 71 26 Q90 26 90 44Z" fill="#F07A2A" {W(3)}/>
<path d="M60 30 Q66 27 72 28" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round"/>
<g fill="#D9473C" stroke="{O}" stroke-width="1.6"><circle cx="60" cy="80" r="3.6"/><circle cx="80" cy="76" r="3.4"/></g>
{eye(64, 62, 0.8)}{eye(78, 62, 0.8)}
<path d="M67 70 Q71 73 75 70" fill="none" {W(1.8)}/>
<path d="M56 88 L88 84" stroke="#3D6FD1" stroke-width="4" stroke-linecap="round"/>
<path d="M50 60 Q40 50 38 40 M92 60 Q102 50 104 40" fill="none" stroke="{O}" stroke-width="3.2"/>
</g>
<circle cx="76" cy="42" r="3" fill="none" {W(2)}/>
''')

# 12. Традиции вкуса (Щёлково, Пролетарский пр-т): кирпичная дровяная печь для пиццы
add("cafe-traditsii-vkusa-proletarsky-8",
    "кирпичная дровяная печь-купол для пиццы с трубой",
    "в её огненном арочном устье печётся круглая пицца, из трубы поднимаются колечки дыма",
    "zb_ember", f'''
<path d="M0 108 L128 108 L128 128 L0 128Z" fill="#7A4B2E" {W(3)}/>
<path d="M78 30 L78 10 L94 10 L94 36Z" fill="#B5543A" {W(3)}/>
<g fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" opacity=".85"><circle cx="90" cy="2" r="4"/><circle cx="100" cy="-6" r="3"/></g>
<path d="M14 108 Q14 34 64 32 Q114 34 114 108Z" fill="#C9603F" {W(3.4)}/>
<g stroke="{O}" stroke-width="1.6" opacity=".45" fill="none">
<path d="M22 70 L106 70 M18 88 L110 88 M30 52 L98 52"/>
<path d="M44 52 L44 70 M70 52 L70 70 M32 70 L32 88 M58 70 L58 88 M84 70 L84 88 M100 70 L100 88"/></g>
<path d="M36 108 L36 88 Q36 70 64 70 Q92 70 92 88 L92 108Z" fill="#3A2420" {W(3)}/>
<path d="M44 106 Q46 92 52 98 Q54 84 62 94 Q66 82 72 96 Q78 88 82 106Z" fill="#FF9E3A"/>
<path d="M52 106 Q56 98 60 102 Q64 94 68 102 Q72 98 74 106Z" fill="#FFE07A"/>
<ellipse cx="64" cy="104" rx="20" ry="4.6" fill="#FFCF5A" {W(2.2)}/>
<g fill="#D9473C"><circle cx="56" cy="104" r="2"/><circle cx="70" cy="103" r="2"/></g>
{eye(52, 52, 0.85)}{eye(76, 52, 0.85)}
<path d="M60 60 Q64 64 68 60" fill="none" {W(2)}/>
{BL(44, 60)}{BL(84, 60)}
''')

# 13. Халиф (Раменское): медная джезва с восточным кофе на горячем песке
add("cafe-khalif-ramenskoe",
    "медная восточная джезва-турка с длинной деревянной ручкой и чеканным узором",
    "стоит по пояс в горячем золотом песке, над ней ароматный пар закручивается в завиток-полумесяц",
    "zb_dune", f'''
<path d="M84 22 Q96 14 104 24 Q94 22 92 32 Q90 40 98 44 Q84 44 82 34 Q80 28 84 22Z" fill="#FFF3C0" {W(2.2)}/>
<path d="M58 40 Q50 32 58 24 Q66 16 58 8" fill="none" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" opacity=".9"/>
<path d="M70 42 Q64 34 70 28" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
<path d="M38 52 Q34 44 30 42 L40 44 L88 44 Q86 52 84 58 L90 104 Q64 112 36 104 L42 58 Q40 54 38 52Z" fill="#D58A45" {W(3.4)}/>
<path d="M40 50 L86 50" stroke="#F4C27A" stroke-width="3"/>
<path d="M46 76 Q54 70 62 76 Q70 82 78 76" fill="none" stroke="#9C5A26" stroke-width="2.2"/>
<g fill="#9C5A26"><circle cx="50" cy="90" r="1.8"/><circle cx="64" cy="92" r="1.8"/><circle cx="78" cy="90" r="1.8"/></g>
<path d="M86 64 L124 52" stroke="#8A5A2B" stroke-width="7" stroke-linecap="round"/>
<path d="M86 64 L124 52" fill="none" {W(1.8)}/>
{eye(56, 64, 0.85)}{eye(72, 64, 0.85)}
<path d="M60 70 Q64 73 68 70" fill="none" {W(1.8)}/>
<path d="M-4 128 L-4 96 Q30 86 64 98 Q98 108 132 92 L132 128Z" fill="#F2C35A" {W(3)}/>
<path d="M16 108 Q24 104 32 108 M92 112 Q100 108 108 112" fill="none" stroke="#D99A2E" stroke-width="2.4" stroke-linecap="round"/>
''')

# 14. Додо (Видное): кусок пиццы-фигуристка кружится на льду пруда
add("cafe-dodo-vidnoe-komsomola",
    "кусок пиццы-фигуристка в розовой юбочке и белых коньках",
    "кружится на одном коньке на льду замёрзшего пруда, вокруг — завитки следов и снежинки",
    "zb_ice", f'''
<ellipse cx="64" cy="108" rx="60" ry="16" fill="#DDF4FF" {W(3)}/>
<path d="M30 108 Q48 98 66 108 Q84 116 98 104" fill="none" stroke="#9BCDE8" stroke-width="2.4" stroke-linecap="round"/>
<path d="M50 30 L86 36 L60 92Z" fill="#FFCF5A" {W(3.2)}/>
<path d="M46 26 Q70 24 90 34 Q90 42 84 42 L50 36 Q44 32 46 26Z" fill="#E09A4A" {W(2.8)}/>
<g fill="#D9473C" stroke="{O}" stroke-width="1.6"><circle cx="62" cy="62" r="3.4"/></g>
{eye(60, 46, 0.75)}{eye(72, 48, 0.75)}
<path d="M63 54 Q66 57 69 55" fill="none" {W(1.8)}/>
<path d="M50 68 Q60 60 76 66 L82 78 Q62 86 44 78Z" fill="#FF8FB8" {W(2.6)}/>
<path d="M56 34 Q42 22 34 28 M82 40 Q96 30 102 36" fill="none" {W(3)}/>
<path d="M58 84 L56 98 M64 84 L74 94" {W(3)}/>
<path d="M48 98 L62 98 L62 92 L54 92Z" fill="#FFFFFF" {W(2.2)}/><path d="M46 102 L64 102" {W(2.4)}/>
<path d="M70 90 L80 96 L82 92 L74 88Z" fill="#FFFFFF" {W(2.2)}/>
{sparkle(20, 50, 5)}{sparkle(108, 64, 4)}{sparkle(98, 20, 4)}
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
