"""Иконки робота creative, 13.11 (запуск 1113d). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1113d.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# 1 KeyDance (хип-хоп, хаус, шаффл с 4 лет, Митино): светящаяся плитка танцпола пляшет шаффл, зажигая соседние плитки
I["keydance-mitino"] = ("квадратная плитка светящегося танцпола с мордашкой, в белых кроссовках",
    "отплясывает шаффл, и от каждого шага вокруг неё вспыхивают соседние разноцветные плитки пола", bg("#3A2470", "#140A33", f'''
<g {s('stroke-width="2"')}>
<path d="M0 96 L20 84 H52 L40 96Z" fill="#FF4FA3"/><path d="M88 96 L76 84 H108 L128 96Z" fill="#3BE0FF"/>
<path d="M0 116 L20 100 H40 L28 116Z" fill="#B8FF3B"/><path d="M100 116 L88 100 H108 L128 116Z" fill="#FFD43B"/>
<path d="M30 128 L40 112 H88 L98 128Z" fill="#7C5CFF"/>
</g>
<rect x="38" y="30" width="52" height="52" rx="8" fill="#FFB020" {s()}/>
<rect x="44" y="36" width="40" height="40" rx="5" fill="#FFD66B"/>
{face(64, 52, 9, 0.8)}
{limb(48, 46, 30, 30, "#FFB020", 4.5)}{limb(80, 46, 100, 56, "#FFB020", 4.5)}
{limb(54, 82, 46, 104, "#FFB020", 4.5)}{limb(74, 82, 90, 96, "#FFB020", 4.5)}
<path d="M36 102 h14 q2 6 -4 6 h-12 q-2 -6 2 -6Z" fill="#fff" {s('stroke-width="2.4"')}/>
<path d="M86 92 h14 q2 6 -4 6 h-12 q-2 -6 2 -6Z" fill="#fff" {s('stroke-width="2.4"')}/>
<path d="M104 70 l6 -4 M106 78 h8 M22 22 l-6 -4" {ln("#3BE0FF", 2.6)}/>
{sparkle(20, 60, 4, "#FF4FA3")}{sparkle(110, 24, 4, "#B8FF3B")}
'''))

# 2 ДМШ им. Молчанова (фортепиано, струнные, духовые, вокал, ИЗО, театр): пузатый контрабас сам играет смычком
I["dmsh-molchanova-klinskaya"] = ("пузатый коричневый контрабас с мордашкой на деке",
    "сам водит по своим струнам длинным смычком, стоя на шпиле посреди школьной сцены, а над грифом всплывают басовые ноты", bg("#FFF1DC", "#F2B66D", f'''
<rect x="0" y="108" width="128" height="20" fill="#B5652E"/>
<path d="M0 108 H128" {ln(O, 3)}/>
<path d="M64 110 V100" {ln(O, 3.5)}/>
<path d="M64 100 C42 100 36 86 44 76 C36 70 38 58 48 54 C46 46 54 40 64 40 C74 40 82 46 80 54 C90 58 92 70 84 76 C92 86 86 100 64 100Z" fill="#B85C24" {s()}/>
<path d="M58 40 V8 M70 40 V8" {ln(O, 3)}/><rect x="58" y="6" width="12" height="40" fill="#3B2A1F" {s('stroke-width="2.4"')}/>
<path d="M61 8 V94 M64 8 V94 M67 8 V94" stroke="#E8D9B8" stroke-width="1"/>
<rect x="56" y="88" width="16" height="5" rx="1" fill="#3B2A1F" {s('stroke-width="1.8"')}/>
<path d="M50 74 q2 4 0 8 M78 74 q-2 4 0 8" fill="none" {ln(O, 2)}/>
{face(64, 66, 9, 0.7)}
<path d="M18 92 L108 70" {ln(O, 5)}/><path d="M18 92 L108 70" {ln("#E9C46A", 2.2)}/>
<rect x="12" y="88" width="10" height="8" rx="2" fill="#3B2A1F" {s('stroke-width="2"')}/>
{note(92, 34, 1.0)}{note(26, 50, 0.9)}{note(104, 52, 0.7)}
'''))

# 3 Artпозитив (ИЗО 4–14 лет, проспект Мира): детский рисунок — солнце-улыбка на листе, приколотом к пробковой доске
I["artpozitiv-mira"] = ("детский рисунок жёлтого солнца с широкой улыбкой и лучами-мазками",
    "сияет с белого листа, приколотого красными кнопками к пробковой доске, а внизу из стаканчика торчат три кисточки", bg("#D7B98E", "#A87B4F", f'''
<g fill="#C49A6C" opacity=".6"><circle cx="20" cy="30" r="2"/><circle cx="108" cy="40" r="2"/><circle cx="30" cy="100" r="2"/><circle cx="100" cy="98" r="1.6"/><circle cx="14" cy="64" r="1.6"/></g>
<rect x="24" y="16" width="80" height="72" rx="3" fill="#fff" {s()} transform="rotate(-4 64 52)"/>
<g transform="rotate(-4 64 52)">
<path d="M64 26 V20 M64 84 V78 M38 52 H32 M96 52 H90 M46 34 L42 30 M82 34 L86 30 M46 70 L42 74 M82 70 L86 74" {ln("#FF9F1C", 5)}/>
<circle cx="64" cy="52" r="20" fill="#FFD43B" stroke="#FF9F1C" stroke-width="3"/>
{eye(57, 48, 0.7)}{eye(71, 48, 0.7)}
<path d="M54 56 Q64 68 74 56" fill="#E8590C" {s('stroke-width="2.2"')}/>
<circle cx="30" cy="22" r="4" fill="#E03131" {s('stroke-width="1.8"')}/><circle cx="98" cy="22" r="4" fill="#E03131" {s('stroke-width="1.8"')}/>
</g>
<path d="M50 96 H78 L74 124 H54Z" fill="#74C0FC" {s()}/>
<path d="M56 98 L48 76 M64 98 V72 M72 98 L82 78" {ln(O, 4)}/>
<path d="M56 98 L48 76 M64 98 V72 M72 98 L82 78" {ln("#F4C27A", 2)}/>
<circle cx="47" cy="74" r="3.5" fill="#E64980" {s('stroke-width="1.6"')}/><circle cx="64" cy="70" r="3.5" fill="#40C057" {s('stroke-width="1.6"')}/><circle cx="83" cy="76" r="3.5" fill="#4C6EF5" {s('stroke-width="1.6"')}/>
'''))

# 4 Студия балета Ирины Ждановой (балет 3+, «Танец с мамой» 2+, Саларьево): большой мамин пуант и крошечный детский
I["zhdanova-ballet-salarevo"] = ("мама-балерина в белой пачке и дочка-малышка в розовой пачке",
    "стоят друг напротив друга в одинаковом арабеске, держась за руки, на фоне высокого зеркала танцкласса", bg("#E3F2FF", "#8EC5F0", f'''
<rect x="20" y="10" width="88" height="96" rx="4" fill="#CFE8FF" opacity=".7" {s('stroke-width="2"')}/>
<path d="M30 20 L44 34 M90 18 L100 28" stroke="#fff" stroke-width="3" opacity=".8"/>
<rect x="0" y="104" width="128" height="24" fill="#D9B38C"/><path d="M0 104 H128" {ln(O, 2.6)}/>
{limb(40, 74, 40, 104, SKIN, 4)}{limb(40, 72, 12, 62, SKIN, 4)}
<ellipse cx="40" cy="70" rx="17" ry="5" fill="#fff" {s()}/>
<path d="M34 46 H46 L46 70 H34Z" fill="#fff" {s()}/>
{limb(46, 50, 66, 62, SKIN, 3.5)}{limb(34, 50, 22, 34, SKIN, 3.5)}
{head(40, 36, 10, "#5C3A21", 0.5)}<circle cx="40" cy="24" r="4" fill="#5C3A21" {s('stroke-width="1.8"')}/>
{limb(88, 88, 88, 104, SKIN, 3.2)}{limb(88, 86, 108, 80, SKIN, 3.2)}
<ellipse cx="88" cy="86" rx="11" ry="3.5" fill="#FF9FC4" {s('stroke-width="2.4"')}/>
<path d="M84 70 H92 L92 86 H84Z" fill="#FF9FC4" {s('stroke-width="2.4"')}/>
{limb(84, 74, 68, 64, SKIN, 3)}{limb(92, 74, 102, 64, SKIN, 3)}
{head(88, 62, 7, "#E0A458", 0.4)}<circle cx="88" cy="53" r="3" fill="#E0A458" {s('stroke-width="1.6"')}/>
{sparkle(64, 24, 5)}{sparkle(112, 40, 3.5)}{sparkle(16, 86, 3)}
'''))

# 5 Splash-Сенсация (эстрадный танец, партерная гимнастика, акробатика с 4 лет, Долгопрудный): мостик под фонтаном блёсток
I["splash-sensaciya-dolgoprudny"] = ("девочка в бирюзовом купальнике с серебряными блёстками",
    "делает гимнастический «мостик» на краю сцены, а над её животом взлетает фонтан брызг-блёсток", bg("#5B2A86", "#22103D", f'''
<path d="M0 104 H128 V128 H0Z" fill="#8B5A2B"/><path d="M0 104 H128" {ln("#C08A4F", 3)}/>
<g fill="#FFE066" opacity=".9"><circle cx="16" cy="100" r="3"/><circle cx="40" cy="100" r="3"/><circle cx="88" cy="100" r="3"/><circle cx="112" cy="100" r="3"/></g>
{limb(36, 104, 46, 84, SKIN, 4.5)}{limb(92, 104, 82, 82, SKIN, 4.5)}
{limb(30, 104, 40, 82, SKIN, 4)}{limb(98, 104, 88, 80, SKIN, 4)}
<path d="M42 84 C46 62 82 60 86 82 L80 86 C74 72 54 72 48 86Z" fill="#20C9B6" {s()}/>
<circle cx="56" cy="74" r="1.6" fill="#fff"/><circle cx="66" cy="70" r="1.6" fill="#fff"/><circle cx="76" cy="74" r="1.6" fill="#fff"/>
{head(30, 92, 9, "#6B3E26", 0.5)}
<path d="M64 62 C60 46 52 34 44 26 M64 62 C64 44 64 30 64 18 M64 62 C68 46 78 34 86 26" fill="none" {ln("#9EEBFF", 3)}/>
<g fill="#E9FBFF" {s('stroke-width="1.6"')}><circle cx="42" cy="22" r="4"/><circle cx="64" cy="14" r="4.5"/><circle cx="88" cy="22" r="4"/></g>
{sparkle(30, 40, 5)}{sparkle(100, 42, 5)}{sparkle(52, 30, 3)}{sparkle(78, 32, 3)}
'''))

# 6 Школа мюзикла Стаса Чунихина (Долгопрудный, 3,5–15 лет: мюзикл, театр, вокал): мальчик подбросил канотье на финальной ноте
I["chunikhin-musical-dolgoprudny"] = ("мальчик в красном жилете с бабочкой и соломенным канотье",
    "широко раскинул руки и тянет финальную ноту песни, подбросив канотье над рампой с круглыми лампочками", bg("#FF8A5B", "#B3261E", f'''
<path d="M0 108 H128 V128 H0Z" fill="#2B1B3D"/>
<g fill="#FFF3B0" {s('stroke-width="1.6"')}><circle cx="10" cy="108" r="4"/><circle cx="30" cy="108" r="4"/><circle cx="50" cy="108" r="4"/><circle cx="70" cy="108" r="4"/><circle cx="90" cy="108" r="4"/><circle cx="110" cy="108" r="4"/></g>
{limb(58, 86, 54, 106, "#2B2B3A", 5)}{limb(70, 86, 74, 106, "#2B2B3A", 5)}
<path d="M52 56 H76 L78 88 H50Z" fill="#E03131" {s()}/>
<path d="M60 56 L64 66 L68 56" fill="#fff" {s('stroke-width="1.8"')}/>
<path d="M58 58 l6 3 6 -3 v6 l-6 -3 -6 3Z" fill="#1E1E2E" {s('stroke-width="1.4"')}/>
{limb(54, 60, 28, 46, "#E03131", 4.5)}{limb(74, 60, 100, 46, "#E03131", 4.5)}
<circle cx="25" cy="44" r="4.5" fill="{SKIN}" {s('stroke-width="2"')}/><circle cx="103" cy="44" r="4.5" fill="{SKIN}" {s('stroke-width="2"')}/>
<circle cx="64" cy="40" r="13" fill="{SKIN}" {s()}/>
<path d="M51 38 Q52 26 64 26 Q76 26 77 38 Q70 32 64 33 Q58 32 51 38Z" fill="#7A4A1F" {s('stroke-width="2.2"')}/>
{eye(59, 40, 0.5)}{eye(69, 40, 0.5)}
<ellipse cx="64" cy="47" rx="3.5" ry="4" fill="#7A1F1F" {s('stroke-width="1.6"')}/>
<g transform="rotate(-15 78 14)"><ellipse cx="78" cy="16" rx="16" ry="4" fill="#F2D27A" {s('stroke-width="2.2"')}/>
<rect x="69" y="6" width="18" height="10" rx="2" fill="#F2D27A" {s('stroke-width="2.2"')}/><rect x="69" y="11" width="18" height="3" fill="#1C3D8F"/></g>
{note(20, 22, 0.9, "#FFF3B0")}{note(108, 70, 0.8, "#FFF3B0")}
'''))

# 7 Художественная студия «Артдом» (Раменское, рисование 5–15 лет): девочка валиком красит радугу на заборе
I["artdom-ramenskoe"] = ("девочка с косичками в джинсовом комбинезоне, перепачканном краской",
    "широким малярным валиком на длинной ручке красит огромную радугу на деревянном заборе, стоя на перевёрнутом ведре", bg("#E6FCF5", "#96F2D7", f'''
<g {s('stroke-width="2"')} fill="#E9C99A">
<path d="M4 50 l8 -8 8 8 V128 H4Z"/><path d="M24 50 l8 -8 8 8 V128 H24Z"/><path d="M44 50 l8 -8 8 8 V128 H44Z"/>
<path d="M64 50 l8 -8 8 8 V128 H64Z"/><path d="M84 50 l8 -8 8 8 V128 H84Z"/><path d="M104 50 l8 -8 8 8 V128 H104Z"/>
</g>
<path d="M10 100 A50 50 0 0 1 110 100" fill="none" stroke="#FA5252" stroke-width="7"/>
<path d="M18 100 A42 42 0 0 1 102 100" fill="none" stroke="#FFA94D" stroke-width="7"/>
<path d="M26 100 A34 34 0 0 1 94 100" fill="none" stroke="#FFE066" stroke-width="7"/>
<path d="M34 100 A26 26 0 0 1 86 100" fill="none" stroke="#69DB7C" stroke-width="7"/>
<path d="M90 120 L112 120 L108 104 L94 104Z" fill="#868E96" {s()}/>
{limb(98, 104, 96, 90, SKIN, 3.5)}{limb(104, 104, 106, 90, SKIN, 3.5)}
<path d="M92 92 H110 L108 74 H94Z" fill="#4C6EF5" {s()}/>
<circle cx="98" cy="84" r="1.8" fill="#FA5252"/><circle cx="104" cy="80" r="1.8" fill="#FFE066"/>
{limb(94, 78, 78, 64, SKIN, 3.5)}
<path d="M80 66 L62 34" {ln(O, 4)}/><path d="M80 66 L62 34" {ln("#ADB5BD", 2)}/>
<rect x="46" y="26" width="26" height="10" rx="4" fill="#74C0FC" {s('stroke-width="2.4"')} transform="rotate(-30 59 31)"/>
{head(101, 64, 9, "#C2410C", 0.5)}
<path d="M92 64 l-5 8 M110 64 l5 8" {ln("#C2410C", 3)}/>
'''))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    for k, (_, _, svg) in I.items():
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(svg)
    print(len(I))
