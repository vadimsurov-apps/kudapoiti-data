"""Иконки робота creative, 14.11 (запуск 1114d). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1114d.py [--subjects] [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# Love Dance, Щербинка (хип-хоп, джаз-фанк): мальчишка в оранжевом худи делает «фриз» на одной руке, кепка слетает
I["love-dance-shcherbinka"] = ("мальчишка в оранжевом худи с капюшоном и мешковатых синих джинсах",
    "застыл в хип-хоп «фризе» на одной руке на сером танцевальном линолеуме, ноги согнуты в воздухе, а его красная кепка слетает с головы",
    bg("#E3FAFC", "#0C8599", f'''
<rect x="-4" y="100" width="136" height="32" fill="#868E96" {s()}/>
<path d="M-4 108 H132" {ln("#ADB5BD", 2)}/>
<path d="M56 100 L60 78" {ln(O, 10)}/><path d="M56 100 L60 78" {ln(SKIN, 6)}/>
<ellipse cx="54" cy="101" rx="7" ry="3" fill="{SKIN}" {s('stroke-width="2"')}/>
<path d="M50 84 Q58 54 84 46 Q96 50 92 62 Q74 70 66 88Z" fill="#FD7E14" {s()}/>
<path d="M70 70 L92 64" {ln("#E8590C", 2.4)}/>
<path d="M84 48 Q100 30 110 40 L104 46 Q96 40 90 52Z" fill="#1971C2" {s()}/>
<path d="M104 44 Q118 52 114 66 L106 64 Q108 54 100 50Z" fill="#1971C2" {s()}/>
<path d="M112 64 h10 q2 6 -2 8 h-10Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M108 38 l6 -10 l6 4 l-6 8Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M52 86 Q42 82 38 72" {ln(O, 9)}/><path d="M52 86 Q42 82 38 72" {ln("#FD7E14", 5)}/>
<circle cx="44" cy="92" r="13" fill="{SKIN}" {s()}/>
<path d="M32 96 Q30 84 40 80 Q46 78 52 84" fill="#5C3D2E" {s('stroke-width="2.4"')}/>
{eye(40, 94, 0.55)}{eye(48, 95, 0.55)}<path d="M41 100 Q45 103 48 100" fill="none" {s('stroke-width="1.8"')}/>
<path d="M14 54 Q20 42 32 46 L34 52 Q24 50 18 58Z" fill="#E03131" {s()}/>
<path d="M30 50 l10 -2" {ln("#E03131", 4)}/>
<path d="M22 66 q2 -5 6 -4 M26 72 q3 -4 7 -2" fill="none" {ln("#fff", 2.2)}/>
{sparkle(100, 92, 5, "#FFE066")}{sparkle(22, 30, 4, "#fff")}
'''))

# Творческая лаборатория Веты Гулливер, Лесной Городок (цокольный этаж): кахон отбивает ритм ладошками
I["veta-gulliver-lesnoy"] = ("деревянный кахон-ящик медового цвета с круглым звуковым окошком-ртом и маленькими ладошками",
    "сидит в уютной студии на цокольном этаже под узким окошком у потолка, лупит себя ладошками по передней стенке, а вокруг разлетаются три сиреневые ноты",
    bg("#F3F0FF", "#7048E8", f'''
<rect x="-4" y="-4" width="136" height="22" fill="#5F3DC4" {s()}/>
<rect x="40" y="2" width="48" height="12" rx="2" fill="#A5D8FF" {s('stroke-width="2.2"')}/>
<path d="M44 12 q4 -6 8 0 q4 -6 8 0 M68 12 q4 -6 8 0" fill="none" {ln("#2F9E44", 2)}/>
<rect x="-4" y="104" width="136" height="28" fill="#845EF7" {s()}/>
<path d="M46 34 L90 34 L94 104 L42 104Z" fill="#E8A852" {s()}/>
<path d="M46 34 L42 104 L34 100 L38 38Z" fill="#C98A3A" {s()}/>
<path d="M50 50 H88 M49 92 H91" {ln("#B9772A", 2)}/>
{eye(60, 58, 0.75)}{eye(78, 58, 0.75)}
<ellipse cx="54" cy="66" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="84" cy="66" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
<circle cx="69" cy="78" r="9" fill="#5C3D2E" {s()}/>
<path d="M64 76 Q69 82 74 76" fill="none" {ln("#E8A852", 1.6)}/>
<path d="M44 70 Q30 66 34 52" {ln(O, 6)}/><path d="M44 70 Q30 66 34 52" {ln("#E8A852", 3)}/>
<path d="M92 70 Q106 66 102 52" {ln(O, 6)}/><path d="M92 70 Q106 66 102 52" {ln("#E8A852", 3)}/>
<ellipse cx="34" cy="48" rx="6" ry="5" fill="#E8A852" {s('stroke-width="2.2"')}/>
<ellipse cx="102" cy="48" rx="6" ry="5" fill="#E8A852" {s('stroke-width="2.2"')}/>
<path d="M24 40 l-4 -4 M28 36 l-2 -5 M112 40 l4 -4 M108 36 l2 -5" {ln("#fff", 2)}/>
{note(16, 70, 0.7, "#D0BFFF")}{note(110, 84, 0.65, "#E5DBFF")}{note(22, 96, 0.5, "#fff")}
'''))

# AVTeam, ЖК «Бутово Парк» (спортивные бальные танцы с 3 лет): пара малышей в латине, у мальчика номер на спине
I["avteam-butovo-park"] = ("пара малышей-бальников: мальчик в чёрной жилетке с номером «12» на спине и девочка в бирюзовом платье с пышной юбкой",
    "крутят латиноамериканский поворот на турнирном паркете — мальчик держит руку девочки высоко над её головой, юбка разлетается колоколом, сверху блестит золотая медаль-подвеска",
    bg("#FFF9DB", "#F08C00", f'''
<rect x="-4" y="102" width="136" height="30" fill="#C08552" {s()}/>
<path d="M10 102 L2 132 M34 102 L30 132 M58 102 L58 132 M82 102 L86 132 M106 102 L114 132" {ln("#A0673A", 2)}/>
<path d="M44 44 L64 26 L80 44" fill="none" {ln(O, 9)}/><path d="M44 44 L64 26 L80 44" fill="none" {ln(SKIN, 5)}/>
<rect x="30" y="50" width="22" height="30" rx="5" fill="#212529" {s()}/>
<rect x="34" y="56" width="14" height="10" rx="2" fill="#fff" {s('stroke-width="1.6"')}/>
<text x="41" y="64.5" font-family="Arial" font-weight="bold" font-size="8" text-anchor="middle" fill="{O}">12</text>
<path d="M36 80 L32 102 M46 80 L50 102" {ln(O, 7)}/><path d="M36 80 L32 102 M46 80 L50 102" {ln("#343A40", 4)}/>
<path d="M28 102 h8 M48 102 h8" {ln(O, 4)}/>
{head(41, 40, 10, "#5C3D2E", 0.5)}
<path d="M86 50 Q76 56 74 70 Q66 92 70 98 Q86 104 104 98 Q110 92 100 70 Q96 56 86 50Z" fill="#20C997" {s()}/>
<path d="M72 92 Q86 98 102 92" fill="none" {ln("#12B886", 2.4)}/>
<path d="M88 98 L86 104 M92 98 L96 104" {ln(O, 4)}/>
{head(87, 42, 10, "#F59F00", 0.5)}
<circle cx="96" cy="32" r="4" fill="#F59F00" {s('stroke-width="2"')}/>
<path d="M64 26 V12" {ln("#E03131", 2)}/>
<circle cx="64" cy="10" r="6" fill="#FCC419" {s('stroke-width="2"')}/>
<path d="M62 10 h4" {ln("#E67700", 1.6)}/>
{sparkle(20, 30, 5, "#fff")}{sparkle(112, 22, 4, "#FFE066")}
'''))

# «Фокус», ЖК «Бутово Парк» (бальные танцы): лакированная туфелька-латина в круге света «наведённого фокуса»
I["fokus-butovo-park"] = ("серебряная лакированная бальная туфелька-«латина» на тонком каблучке с ремешком и мордашкой",
    "делает шаг ча-ча-ча точно в центре круга-прицела наведённого фокуса фотообъектива на тёмно-фиолетовом фоне, вокруг вспыхивают стразы",
    bg("#B197FC", "#3B1F8C", f'''
<circle cx="64" cy="64" r="44" fill="none" {ln("#E5DBFF", 3)}/>
<circle cx="64" cy="64" r="34" fill="#5F3DC4" opacity=".55"/>
<path d="M64 10 V24 M64 104 V118 M10 64 H24 M104 64 H118" {ln("#E5DBFF", 3)}/>
<path d="M20 20 l10 0 M20 20 l0 10 M108 20 l-10 0 M108 20 l0 10 M20 108 l10 0 M20 108 l0 -10 M108 108 l-10 0 M108 108 l0 -10" {ln("#FFE066", 3)}/>
<path d="M34 78 Q34 64 48 62 L72 60 Q90 56 96 44 L100 46 Q100 70 88 80 L42 84 Q34 84 34 78Z" fill="#DEE2E6" {s()}/>
<path d="M88 80 L92 98" {ln(O, 7)}/><path d="M88 80 L92 98" {ln("#ADB5BD", 4)}/>
<path d="M62 62 Q70 46 82 52" fill="none" {ln(O, 5)}/><path d="M62 62 Q70 46 82 52" fill="none" {ln("#CED4DA", 2.6)}/>
<path d="M40 70 Q60 66 86 70" fill="none" {ln("#fff", 2.4)}/>
{eye(52, 74, 0.55)}{eye(64, 73, 0.55)}<path d="M55 79 Q58 82 61 79" fill="none" {s('stroke-width="1.8"')}/>
<ellipse cx="46" cy="78" rx="3" ry="1.8" fill="#FF7FA8" opacity=".7"/>
{sparkle(30, 40, 5, "#fff")}{sparkle(100, 92, 4, "#FFE066")}{sparkle(84, 30, 3, "#fff")}{sparkle(40, 100, 3, "#FCC2D7")}
'''))

# Ансамбль эстрадно-спортивного танца «Карнавал», Восточная ул.: девочка в алом костюме с бахромой — мах ногой под серпантином
I["karnaval-vostochnaya"] = ("девочка с высоким хвостиком в алом эстрадном купальнике с золотой бахромой",
    "в прыжке делает высокий мах прямой ногой над голубым краем сцены, руки раскинуты, а сверху сыплются разноцветный серпантин и конфетти",
    bg("#D0EBFF", "#1864AB", f'''
<rect x="-4" y="104" width="136" height="28" fill="#4DABF7" {s()}/>
<path d="M-4 110 H132" {ln("#A5D8FF", 2)}/>
<path d="M20 4 q6 10 0 18 q-6 8 2 16" fill="none" {ln("#FCC419", 3)}/>
<path d="M108 2 q-6 10 2 18 q6 8 -2 16" fill="none" {ln("#F783AC", 3)}/>
<path d="M84 6 q4 8 -2 14" fill="none" {ln("#69DB7C", 3)}/>
<rect x="36" y="14" width="5" height="5" fill="#FF922B" transform="rotate(20 38 16)"/>
<rect x="96" y="44" width="5" height="5" fill="#FCC419" transform="rotate(-25 98 46)"/>
<rect x="16" y="60" width="5" height="5" fill="#F783AC" transform="rotate(35 18 62)"/>
<circle cx="70" cy="10" r="3" fill="#fff"/><circle cx="110" cy="70" r="3" fill="#FFE066"/>
<path d="M58 78 L44 100" {ln(O, 9)}/><path d="M58 78 L44 100" {ln(SKIN, 5)}/>
<path d="M38 100 h10 q2 4 -2 5 h-9Z" fill="#E03131" {s('stroke-width="2"')}/>
<path d="M64 76 L104 46" {ln(O, 9)}/><path d="M64 76 L104 46" {ln(SKIN, 5)}/>
<path d="M102 40 l8 2 l-2 8 l-6 -2Z" fill="#E03131" {s('stroke-width="2"')}/>
<path d="M52 50 Q50 64 54 80 Q62 84 70 78 Q72 62 66 50Z" fill="#E03131" {s()}/>
<path d="M52 76 l-2 8 M57 80 l-1 8 M62 81 l0 8 M67 79 l1 8" {ln("#FCC419", 2)}/>
<path d="M52 54 L30 42 M66 54 L90 40" {ln(O, 7)}/><path d="M52 54 L30 42 M66 54 L90 40" {ln(SKIN, 3.6)}/>
<circle cx="59" cy="38" r="11" fill="{SKIN}" {s()}/>
<path d="M48 36 Q50 24 62 26 Q70 28 70 36 Q60 30 48 36Z" fill="#212529" {s('stroke-width="2.2"')}/>
<path d="M66 26 Q80 16 84 26 Q78 24 70 30" fill="#212529" {s('stroke-width="2.2"')}/>
<circle cx="66" cy="27" r="2.4" fill="#F783AC"/>
{eye(55, 39, 0.5)}{eye(63, 39, 0.5)}<path d="M56 44 Q59 47 62 44" fill="none" {s('stroke-width="1.6"')}/>
{sparkle(26, 86, 5, "#fff")}{sparkle(92, 92, 4, "#FFE066")}
'''))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    ids = [a for a in sys.argv[1:] if not a.startswith("-")] or list(I)
    for k in ids:
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(I[k][2])
    print(len(ids))
