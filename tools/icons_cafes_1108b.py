"""Робот cafes, 2026-11-08 (04 UTC): иконки 10 новых кафе. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя компоновка и палитра фона).
Запуск из корня: python3 tools/icons_cafes_1108b.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def W(w):
    return s(f'stroke-width="{w}"')


def svg2(a, b, body, cx="38%", cy="28%"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="{cx}" cy="{cy}" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


def dots(pts, r, fill):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>' for x, y in pts)


I = {}

# 1 Laksa&Wok — миска лаксы, палочки поднимают лапшу зигзагом
I["cafe-laksa-wok-istra"] = (svg2("#DDFBF2", "#2E9C86", f'''
<path d="M78 8 L60 50 M92 12 L66 52" stroke="#8A5A2B" stroke-width="5" stroke-linecap="round"/>
<path d="M62 50 L56 58 L68 64 L56 70 L66 76" fill="none" stroke="#FFF1C9" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M66 52 L72 60 L62 66 L72 72" fill="none" stroke="#FFF1C9" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M26 40 q-6 -8 0 -14 q6 -6 0 -12 M40 36 q-6 -8 0 -14" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<path d="M14 74 H114 Q112 116 64 118 Q16 116 14 74Z" fill="#FFFFFF" {s()}/>
<path d="M18 88 Q64 96 110 88" fill="none" stroke="#2E9C86" stroke-width="4"/>
<path d="M24 100 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5 l6 -5 l6 5" fill="none" stroke="#2E9C86" stroke-width="2"/>
<ellipse cx="64" cy="74" rx="50" ry="11" fill="#F29A2E" {s()}/>
<ellipse cx="58" cy="72" rx="26" ry="5" fill="#FFC36B"/>
<circle cx="94" cy="72" r="8" fill="#B6E36A" {W(2)}/><path d="M94 64 V80 M86 72 H102" stroke="#7DBB3A" stroke-width="1.6"/>
{dots([(36,74),(44,70),(78,76),(30,70)],2,"#D9492B")}
<path d="M38 66 q4 -6 8 0" fill="#3E9B4A"/>
{face(64, 104, d=11, k=0.85)}
'''), "герой: миска оранжевой малайской лаксы с кокосовым молоком и долькой лайма | сцена: деревянные палочки поднимают из супа лапшу зигзагом, над миской вьётся пар")

# 2 Джива — маковый рулет на доске рядом с чашечкой эспрессо
I["cafe-dzhiva-istra"] = (svg2("#F5EAFF", "#7E4FA8", f'''
<rect x="6" y="94" width="116" height="16" rx="6" fill="#C98B4E" {s()}/>
<path d="M14 102 H60 M70 104 H112" stroke="#A86B33" stroke-width="2"/>
<path d="M22 56 H74 V94 H22Z" fill="#E7B472" {s()}/>
<path d="M30 60 Q48 54 66 60 M30 70 Q48 64 66 70 M30 80 Q48 74 66 80" fill="none" stroke="#F6D9A8" stroke-width="2.4"/>
<circle cx="74" cy="75" r="22" fill="#F2C98E" {s()}/>
<path d="M74 75 m0 -3 a3 3 0 1 1 -3 3 a6 6 0 1 1 6 6 a10 10 0 1 1 -10 -10 a14 14 0 1 1 14 14 a17 17 0 1 1 -17 -17" fill="none" stroke="#3A2E4A" stroke-width="3.2" stroke-linecap="round"/>
{dots([(28,52),(40,50),(54,51),(66,50),(46,46)],1.6,"#fff")}
{dots([(60,58),(84,56),(90,90)],1.2,"#fff")}
<path d="M98 80 H118 V92 Q118 98 112 98 H104 Q98 98 98 92Z" fill="#fff" {W(2.6)}/>
<path d="M118 83 q6 0 6 5 q0 5 -6 5" fill="none" {W(2.4)}/>
<ellipse cx="108" cy="80" rx="10" ry="2.6" fill="#6B3F1F"/>
<path d="M104 72 q-3 -5 1 -9 M111 72 q-3 -5 1 -9" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<path d="M30 72 q3 -3 6 0 M44 72 q3 -3 6 0" fill="none" {W(2.4)}/>
<ellipse cx="30" cy="80" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".6"/><ellipse cx="51" cy="80" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".6"/>
<path d="M37 82 Q40 85 43 82" fill="none" {W(2.2)}/>
'''), "герой: маковый рулет в сахарной пудре со спиралью-срезом | сцена: сладко потягивается на деревянной доске рядом с крошечной чашкой эспрессо")

# 3 Дворянское гнездо — кусок «Наполеона» на крыльце усадьбы с колоннами
I["cafe-dvoryanskoe-gnezdo-gorki2"] = (svg2("#EAF4FF", "#5F8FD0", f'''
<path d="M10 40 L64 14 L118 40Z" fill="#FFFFFF" {s()}/>
<circle cx="64" cy="31" r="5" fill="#BFD6F2" {W(2)}/>
<rect x="12" y="40" width="104" height="8" fill="#F4F0E6" {s()}/>
<g fill="#FFFFFF" stroke="{O}" stroke-width="2.4">
<rect x="16" y="48" width="10" height="56"/><rect x="38" y="48" width="10" height="56"/>
<rect x="80" y="48" width="10" height="56"/><rect x="102" y="48" width="10" height="56"/>
</g>
<rect x="6" y="104" width="116" height="8" fill="#E6DCC8" {s()}/>
<rect x="0" y="112" width="128" height="16" fill="#D8CBB0" {s()}/>
<path d="M36 64 H94 V106 H36Z" fill="#F6E7C4" {s()}/>
<path d="M36 74 H94 M36 84 H94 M36 94 H94" stroke="#C88B45" stroke-width="5"/>
<path d="M36 72 H94 M36 82 H94 M36 92 H94" stroke="#FFFDF4" stroke-width="2"/>
<path d="M34 64 Q36 56 42 60 Q48 54 54 60 Q60 54 66 60 Q72 54 78 60 Q84 54 90 60 Q96 58 96 64Z" fill="#E7B36A" {s()}/>
{dots([(44,58),(58,57),(72,58),(86,58)],1.5,"#fff")}
{face(65, 88, d=9, k=0.75)}
'''), "герой: квадратный кусок торта «Наполеон» с кремовыми слоями и крошкой сверху | сцена: стоит на крыльце дворянской усадьбы между белыми колоннами под фронтоном")

# 4 Гастромаркет — фалафель в пите под полосатым навесом прилавка
I["cafe-gastromarket-pushkino"] = (svg2("#FFF5D8", "#DDA235", f'''
<path d="M0 6 H128 V30 H0Z" fill="#fff"/>
<path d="M0 6 H16 V30 H0Z M32 6 H48 V30 H32Z M64 6 H80 V30 H64Z M96 6 H112 V30 H96Z" fill="#E2453B"/>
<path d="M0 30 Q8 40 16 30 Q24 40 32 30 Q40 40 48 30 Q56 40 64 30 Q72 40 80 30 Q88 40 96 30 Q104 40 112 30 Q120 40 128 30" fill="#E2453B" {s()}/>
<rect x="0" y="100" width="128" height="28" fill="#9C6436" {s()}/>
<path d="M0 108 H128" stroke="#7E4C26" stroke-width="2"/>
<circle cx="44" cy="62" r="15" fill="#8C6A2E" {s()}/>
<circle cx="84" cy="62" r="15" fill="#8C6A2E" {s()}/>
<circle cx="64" cy="54" r="16" fill="#9C7A33" {s()}/>
{dots([(38,58),(50,66),(78,58),(90,66),(60,48),(70,58)],1.6,"#6E9B3B")}
<path d="M28 66 Q30 58 40 62 Q44 54 52 60 M76 60 Q84 54 92 62 Q100 58 102 68" fill="#7CC456" {W(2)}/>
<path d="M22 70 H106 Q104 106 64 108 Q24 106 22 70Z" fill="#F2DBA6" {s()}/>
<path d="M30 78 Q64 86 98 78" fill="none" stroke="#D9B577" stroke-width="2.4"/>
{dots([(40,92),(56,98),(76,96),(90,88)],1.6,"#C9A060")}
{eye(56, 56, 0.6)}{eye(72, 56, 0.6)}
<path d="M60 62 Q64 65 68 62" fill="none" {W(1.8)}/>
{eye(39, 64, 0.5)}{eye(49, 64, 0.5)}{eye(79, 64, 0.5)}{eye(89, 64, 0.5)}
{face(64, 88, d=12, k=0.8, mouth=True)}
'''), "герой: три золотисто-зелёных шарика фалафеля в кармашке питы | сцена: выглядывают из-под красно-белого полосатого навеса рыночного прилавка")

# 5 ПаноРама — трёхъярусный шоколадный фонтан, в него макают клубнику
I["cafe-panorama-ramenskoe"] = (svg2("#FFE6EE", "#D9506F", f'''
<ellipse cx="58" cy="112" rx="44" ry="8" fill="#B5BCC9" {s()}/>
<path d="M14 104 H102 L94 112 H22Z" fill="#DDE2EA" {s()}/>
<rect x="55" y="20" width="6" height="84" fill="#C9CFD9" {W(2)}/>
<path d="M20 98 Q20 86 58 86 Q96 86 96 98Z" fill="#6B3A22" {s()}/>
<path d="M30 76 Q30 66 58 66 Q86 66 86 76Z" fill="#7A4428" {s()}/>
<path d="M40 54 Q40 46 58 46 Q76 46 76 54Z" fill="#8A4F2E" {s()}/>
<path d="M40 54 Q38 64 32 76 M76 54 Q78 64 84 76 M30 76 Q26 88 22 98 M86 76 Q90 88 94 98" fill="none" stroke="#5A2E18" stroke-width="5" stroke-linecap="round"/>
<path d="M50 30 Q58 20 66 30 Q66 40 58 46 Q50 40 50 30Z" fill="#8A4F2E" {s()}/>
{dots([(28,108),(46,110),(72,110),(88,108)],2,"#5A2E18")}
{face(58, 78, d=9, k=0.65)}
<path d="M124 30 L86 60" stroke="#E8C891" stroke-width="3" stroke-linecap="round"/>
<path d="M82 56 Q74 58 76 68 Q80 76 90 70 Q96 62 90 56Z" fill="#E8344A" {s()}/>
<path d="M76 66 Q80 76 90 70 Q86 66 76 66Z" fill="#5A2E18"/>
<path d="M88 54 l4 -6 l2 6 l6 -2" fill="#4BA74E" {W(1.8)}/>
{dots([(80,62),(84,66),(86,60)],1,"#FFE08A")}
{sparkle(104, 86, 5)}{sparkle(20, 40, 4)}
'''), "герой: трёхъярусный шоколадный фонтан на серебряной подставке | сцена: в его шоколадные струи макают клубнику на длинной шпажке")

# 6 Метрополь Холл — Париж-Брест на серебряном подносе под хрустальной люстрой
I["cafe-metropol-hall-vidnoe"] = (svg2("#EEE9FF", "#43397F", f'''
<path d="M64 0 V12" stroke="#E8C35A" stroke-width="3"/>
<path d="M40 22 Q64 34 88 22" fill="none" stroke="#E8C35A" stroke-width="3"/>
<ellipse cx="64" cy="16" rx="12" ry="5" fill="#F4D77A" {W(2)}/>
<path d="M44 24 v8 M54 28 v10 M64 30 v10 M74 28 v10 M84 24 v8" stroke="#DCEBFF" stroke-width="2"/>
{dots([(44,34),(54,40),(64,42),(74,40),(84,34)],2.6,"#DCEBFF")}
{sparkle(30, 30, 4)}{sparkle(100, 32, 4)}
<ellipse cx="64" cy="102" rx="54" ry="14" fill="#D9DEE8" {s()}/>
<ellipse cx="64" cy="100" rx="44" ry="9" fill="#EEF1F6"/>
<ellipse cx="64" cy="80" rx="44" ry="22" fill="#D9963F" {s()}/>
<ellipse cx="64" cy="76" rx="16" ry="7" fill="#43397F" opacity=".35" {W(2)}/>
<path d="M24 76 Q30 64 40 70 Q46 60 56 66 Q64 58 72 66 Q82 60 88 70 Q98 64 104 76 Q98 84 88 80 Q80 88 72 82 Q64 90 56 82 Q48 88 40 80 Q30 84 24 76Z" fill="#F3E1BE" {W(2.4)}/>
<g fill="#FFF3D6" stroke="#B9873E" stroke-width="1">
<ellipse cx="34" cy="70" rx="4" ry="2" transform="rotate(-20 34 70)"/><ellipse cx="52" cy="64" rx="4" ry="2" transform="rotate(15 52 64)"/>
<ellipse cx="76" cy="64" rx="4" ry="2" transform="rotate(-10 76 64)"/><ellipse cx="94" cy="70" rx="4" ry="2" transform="rotate(25 94 70)"/>
</g>
{face(64, 90, d=12, k=0.8)}
'''), "герой: заварное кольцо «Париж-Брест» с кремом и миндальными лепестками | сцена: красуется на серебряном подносе под сияющей хрустальной люстрой банкетного зала")

# 7 Империя — донер-кебаб на вертеле, стружка падает в питу
I["cafe-imperiya-voskresensk"] = (svg2("#FFEBDD", "#C54A2E", f'''
<rect x="58" y="4" width="6" height="112" fill="#BFC5CF" {W(2)}/>
<path d="M36 22 H86 L80 98 H42Z" fill="#B5652E" {s()}/>
<path d="M38 36 L84 32 M39 50 L83 46 M40 64 L82 60 M41 78 L81 74 M42 92 L80 88" stroke="#7A3A16" stroke-width="3"/>
<path d="M38 30 L84 26 M40 58 L82 54 M41 86 L81 82" stroke="#E39A5C" stroke-width="2"/>
<rect x="30" y="16" width="62" height="7" rx="3" fill="#D7DCE4" {s()}/>
<rect x="34" y="98" width="54" height="7" rx="3" fill="#D7DCE4" {s()}/>
{face(61, 56, d=9, k=0.85)}
<path d="M92 66 q6 2 6 8 M96 78 q6 2 4 8" fill="none" stroke="#B5652E" stroke-width="4" stroke-linecap="round"/>
<path d="M86 104 Q104 88 122 104 Q104 116 86 104Z" fill="#F3D9A2" {s()}/>
<path d="M94 102 q4 -4 8 0 q4 -4 8 0" fill="none" stroke="#B5652E" stroke-width="3" stroke-linecap="round"/>
<path d="M98 98 q2 -4 6 -2" stroke="#59B04A" stroke-width="3" stroke-linecap="round"/>
<path d="M18 50 q-4 -6 0 -12 M24 42 q-4 -6 0 -12" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
'''), "герой: донер-кебаб на вертикальном вертеле с полосками жара | сцена: медленно вертится, а тонкая мясная стружка падает в лепёшку-питу у его основания")

# 8 Пельменная (Ершово) — девочка в красной косынке лепит пельмени в облачке муки
I["cafe-pelmennaya-ershovo"] = (svg2("#FFF0E2", "#E88A62", f'''
<path d="M16 50 q-8 -10 2 -16 q6 -10 16 -4" fill="#fff" opacity=".85"/>
<circle cx="104" cy="40" r="10" fill="#fff" opacity=".8"/><circle cx="114" cy="50" r="6" fill="#fff" opacity=".8"/>
<path d="M36 92 Q36 66 64 66 Q92 66 92 92Z" fill="#FFFFFF" {s()}/>
<path d="M50 72 L56 92 M78 72 L72 92" stroke="#E0D6CC" stroke-width="2"/>
<circle cx="64" cy="44" r="20" fill="#FFD8B8" {s()}/>
<path d="M42 44 Q42 20 64 20 Q86 20 86 44 Q76 34 64 34 Q52 34 42 44Z" fill="#E23B3B" {s()}/>
{dots([(52,28),(64,25),(76,28),(58,34),(70,34)],1.8,"#fff")}
<path d="M84 40 l10 8 l-4 -12Z" fill="#E23B3B" {W(2)}/>
{face(64, 46, d=7, k=0.75)}
<rect x="6" y="90" width="116" height="38" fill="#C78B52" {s()}/>
<ellipse cx="64" cy="98" rx="40" ry="5" fill="#FFF8EC" opacity=".9"/>
<path d="M22 104 Q30 96 38 104Z M42 106 Q50 98 58 106Z M82 106 Q90 98 98 106Z" fill="#FFF6E6" {W(2)}/>
<circle cx="50" cy="86" r="7" fill="#FFD8B8" {W(2.4)}/><circle cx="78" cy="86" r="7" fill="#FFD8B8" {W(2.4)}/>
<path d="M54 86 Q64 76 74 86 Q64 92 54 86Z" fill="#FFF6E6" {W(2.2)}/>
{dots([(30,82),(40,78),(92,80),(100,76),(86,72)],1.6,"#fff")}
'''), "герой: девочка в красной косынке в горошек и белом фартуке | сцена: лепит пельмень за деревянным столом, рядом рядок готовых, вокруг облачка муки")

# 9 Пловная № 1 — рисинка-парашютист спускается на тюбетейке в казан плова
I["cafe-plovnaya1-mytishchi"] = (svg2("#FFFBE6", "#57B9E2", f'''
<path d="M26 34 Q26 8 64 8 Q102 8 102 34Z" fill="#1F5B4A" {s()}/>
<path d="M26 34 H102" {W(3)}/>
<path d="M40 30 l6 -10 l6 10Z M58 30 l6 -12 l6 12Z M76 30 l6 -10 l6 10Z" fill="#FFFFFF" opacity=".95"/>
<path d="M30 34 L56 62 M98 34 L72 62 M64 34 V58" stroke="{O}" stroke-width="1.6"/>
<ellipse cx="64" cy="70" rx="11" ry="15" fill="#FFFFFF" {s()}/>
{face(64, 68, d=5, k=0.55)}
<path d="M53 70 l-8 -6 M75 70 l8 -6" {W(2.6)}/>
<path d="M16 96 H112 Q110 124 64 126 Q18 124 16 96Z" fill="#2F2F38" {s()}/>
<path d="M10 96 H20 M108 96 H118" {W(5)}/>
<path d="M18 96 Q30 84 44 90 Q54 80 66 88 Q78 80 88 90 Q100 84 110 96Z" fill="#F2B544" {s()}/>
<path d="M30 92 l6 -3 M48 88 l6 -2 M72 88 l5 -3 M92 90 l6 -2" stroke="#E2622B" stroke-width="3" stroke-linecap="round"/>
{dots([(38,94),(58,90),(82,92),(98,94)],1.6,"#FFF3C2")}
{sparkle(108, 60, 5)}{sparkle(20, 60, 4)}
'''), "герой: рисинка-малыш | сцена: спускается на парашюте-тюбетейке прямо в чёрный казан с золотым пловом и морковкой")

# 10 ВьетСоул — бань-сео плывёт в лодке-сампане по зелёной реке
I["cafe-vietsoul-yaroslavskoe"] = (svg2("#F0FFDD", "#3E9A55", f'''
<path d="M0 98 Q16 92 32 98 Q48 104 64 98 Q80 92 96 98 Q112 104 128 98 V128 H0Z" fill="#5CC3B0" {s()}/>
<path d="M10 112 q8 -4 16 0 M54 116 q8 -4 16 0 M96 112 q8 -4 16 0" fill="none" stroke="#C9F2EA" stroke-width="2.4" stroke-linecap="round"/>
<path d="M98 30 Q104 20 112 24 M102 44 Q110 36 118 42" fill="none" stroke="#2C7A3E" stroke-width="3" stroke-linecap="round"/>
<path d="M6 82 H122 Q112 102 64 102 Q16 102 6 82Z" fill="#9A5B2C" {s()}/>
<path d="M14 88 H114" stroke="#7A4420" stroke-width="2"/>
<path d="M24 82 Q24 34 64 34 Q104 34 104 82Z" fill="#F5C531" {s()}/>
<path d="M30 80 Q34 46 64 42 Q94 46 98 80" fill="none" stroke="#E39E1B" stroke-width="2"/>
{dots([(40,56),(52,48),(84,52),(90,66),(36,70),(70,46)],2,"#D98A12")}
<path d="M98 70 q10 -6 14 4 q-6 6 -14 0Z" fill="#FF9C86" {W(2)}/>
<path d="M30 74 q-8 -2 -10 -8 M34 66 q-8 -4 -8 -10" stroke="#F7F3DA" stroke-width="3" stroke-linecap="round"/>
<path d="M98 76 q6 4 10 2" stroke="#4BA74E" stroke-width="3" stroke-linecap="round"/>
{face(64, 64, d=10, k=0.9)}
'''), "герой: жёлтый хрустящий блин бань-сео, сложенный полумесяцем, с ростками и креветкой | сцена: плывёт в деревянной лодке-сампане по зелёной реке")

if __name__ == "__main__":
    lines = []
    for pid, (svg, subj) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg)
        lines.append(f"{pid} — {subj}")
    p = os.path.join(ROOT, "icons-src", "subjects.txt")
    have = open(p, encoding="utf-8").read()
    keep = [l for l in have.splitlines() if l.split(" — ")[0] not in I]
    open(p, "w", encoding="utf-8").write("\n".join(keep + lines) + "\n")
    print("icons", len(I))
