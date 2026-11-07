"""Робот cafes, 2026-11-07 (22 UTC): иконки 24 новых кафе. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя компоновка и палитра фона).
Запуск из корня: python3 tools/icons_cafes_1107j.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
import os, sys, math
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


def closed(cx, cy, d=8, k=1.0):
    return (f'<path d="M{cx-d-4*k} {cy} Q{cx-d} {cy-4*k} {cx-d+4*k} {cy} M{cx+d-4*k} {cy} Q{cx+d} {cy-4*k} {cx+d+4*k} {cy}" '
            f'fill="none" {W(2.4*k)}/>'
            f'<ellipse cx="{cx-d-4*k}" cy="{cy+6*k}" rx="{4*k}" ry="{2.3*k}" fill="#FF7FA8" opacity=".6"/>'
            f'<ellipse cx="{cx+d+4*k}" cy="{cy+6*k}" rx="{4*k}" ry="{2.3*k}" fill="#FF7FA8" opacity=".6"/>')


def dots(pts, r, fill):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>' for x, y in pts)


I = {}

# 1 Здрасте (Подольск) — купол торта «Сметанник» машет «здрасте» из окошка раздачи под полосатым козырьком
I["cafe-zdraste-podolsk-lenina"] = (svg2("#E6EEFF", "#5A78D8", f'''
<rect x="14" y="34" width="100" height="84" rx="6" fill="#FFF4DE" {s()}/>
<path d="M10 26 H118 L112 44 H16Z" fill="#fff" {s()}/>
<path d="M24 26 L22 44 M42 26 L40 44 M60 26 V44 M78 26 L80 44 M96 26 L98 44" stroke="#E5484D" stroke-width="9"/>
<path d="M10 26 H118 L112 44 H16Z" fill="none" {s()}/>
<rect x="26" y="52" width="76" height="52" rx="4" fill="#9FD4F5" {s()}/>
<rect x="20" y="100" width="88" height="10" rx="3" fill="#C98A4A" {s()}/>
<g transform="rotate(-6 62 84)">
<path d="M30 100 Q30 60 64 60 Q98 60 98 100Z" fill="#E8B060" {s()}/>
<path d="M40 100 Q42 74 64 72 Q86 74 88 100Z" fill="#FFF8E8" {s()}/>
<path d="M36 72 Q46 64 56 66" fill="none" stroke="#FFD89A" stroke-width="3" stroke-linecap="round"/>
{face(64, 88, d=9, k=0.85)}
</g>
<path d="M92 72 Q104 60 100 46" fill="none" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<circle cx="100" cy="44" r="5" fill="#E8B060" {W(2)}/>
<path d="M106 38 l5 -4 M108 46 l6 0 M104 32 l2 -5" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
'''), "герой: купол торта «Сметанник» с белым кремом | сцена: высунулся из окошка раздачи под полосатым козырьком и машет ручкой «здрасте»")

# 2 Здрасте (Апрелевка) — кружка горячего шоколада со сливками, пар сердечком, за окном снег
I["cafe-zdraste-aprelevka"] = (svg2("#7C4D8F", "#2C1A3E", f'''
<rect x="8" y="10" width="54" height="50" rx="4" fill="#4E7BC4" {s()}/>
<path d="M35 10 V60 M8 35 H62" stroke="{O}" stroke-width="3"/>
{sparkle(20, 22, 3.5)}{sparkle(48, 46, 3)}{sparkle(50, 20, 2.4)}{sparkle(22, 50, 2.4)}
<path d="M0 108 H128 V128 H0Z" fill="#B9774A"/>
<path d="M80 40 Q72 30 80 22 Q88 14 96 22 Q104 14 112 22 Q120 30 112 40 L96 54Z" fill="#FF8FB1" opacity=".9" {W(2.4)}/>
<path d="M88 60 Q84 50 90 46 M100 60 Q104 52 98 48" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M98 78 Q120 78 118 92 Q116 106 98 104" fill="none" stroke="{O}" stroke-width="10"/>
<path d="M98 78 Q120 78 118 92 Q116 106 98 104" fill="none" stroke="#F2F2F2" stroke-width="5"/>
<path d="M36 66 H102 V106 Q102 116 92 116 H46 Q36 116 36 106Z" fill="#F7F7F7" {s()}/>
<path d="M36 66 Q42 52 54 58 Q60 48 70 56 Q80 46 88 56 Q98 52 102 66Z" fill="#FFFFFF" {s()}/>
<ellipse cx="69" cy="67" rx="31" ry="4" fill="#7A4524"/>
{face(69, 88, d=11, k=1.0)}
'''), "герой: белая кружка горячего шоколада с горкой сливок | сцена: пар над ней сложился в розовое сердечко у окна со снежинками")

# 3 Карабас-Барабас — шоколадный пончик с посыпкой выглядывает из-за ширмы кукольного театра
I["cafe-karabas-egorevsk"] = (svg2("#FFD9A8", "#E2603A", f'''
<path d="M6 8 H122 V30 Q94 40 64 30 Q34 40 6 30Z" fill="#B3202E" {s()}/>
<path d="M6 30 Q14 64 10 120 M122 30 Q114 64 118 120" fill="none" stroke="#B3202E" stroke-width="12"/>
<circle cx="64" cy="58" r="30" fill="#E8B060" {s()}/>
<path d="M36 52 Q38 30 64 28 Q90 30 92 52 Q86 58 78 54 Q70 62 62 56 Q52 62 46 54 Q40 60 36 52Z" fill="#5A2E1A" {s()}/>
{''.join(f'<rect x="{x}" y="{y}" width="6" height="2.6" rx="1.3" fill="{c}" transform="rotate({r} {x} {y})"/>' for x,y,c,r in [(46,40,"#FF6FA3",20),(58,34,"#4FC3F7",-30),(72,38,"#FFE14A",40),(80,46,"#7CE07C",-10),(52,48,"#FFFFFF",60),(66,44,"#FF8A3C",0)])}
<ellipse cx="64" cy="62" rx="9" ry="6" fill="#FFD9A8" {W(2.4)}/>
{face(64, 72, d=13, k=0.85)}
<path d="M30 74 L18 60 M98 74 L110 60" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<rect x="10" y="80" width="108" height="48" fill="#3F7F5A" {s()}/>
<path d="M10 90 H118" stroke="#F2C14E" stroke-width="4"/>
{''.join(f'<circle cx="{x}" cy="104" r="3" fill="#F2C14E"/>' for x in (24,44,64,84,104))}
'''), "герой: пончик в шоколадной глазури с цветной посыпкой | сцена: выглядывает из-за зелёной ширмы кукольного театра между красными кулисами")

# 4 Клякса — шоколадная клякса растеклась по тарелке и рисует пальчиком ромашку
I["cafe-klyaksa-chernogolovka"] = (svg2("#F4FFF8", "#6CCB9A", f'''
<ellipse cx="64" cy="70" rx="56" ry="46" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="70" rx="44" ry="35" fill="none" stroke="#CFE9DD" stroke-width="3"/>
<path d="M30 70 Q24 56 38 52 Q36 38 52 42 Q58 30 70 40 Q84 34 86 48 Q100 50 94 62 Q104 72 92 80 Q94 94 78 90 Q70 100 60 90 Q44 96 44 84 Q28 84 30 70Z" fill="#6B3A22" {s()}/>
<circle cx="102" cy="90" r="4" fill="#6B3A22" {W(2)}/><circle cx="26" cy="44" r="3" fill="#6B3A22" {W(2)}/>
<ellipse cx="50" cy="56" rx="6" ry="3" fill="#fff" opacity=".35"/>
{face(62, 64, d=10, k=0.95)}
<path d="M86 74 Q96 76 100 66" fill="none" stroke="#6B3A22" stroke-width="6" stroke-linecap="round"/>
<g fill="#FFFFFF" {W(1.6)}>
{''.join(f'<ellipse cx="{104+9*__import__("math").cos(a)}" cy="{48+9*__import__("math").sin(a)}" rx="5" ry="3" transform="rotate({a*57.3} {104+9*__import__("math").cos(a)} {48+9*__import__("math").sin(a)})"/>' for a in [i*0.785 for i in range(8)])}
</g>
<circle cx="104" cy="48" r="5" fill="#FFD84A" {W(1.8)}/>
'''), "герой: шоколадная клякса с глазками | сцена: растеклась по белой тарелке и рисует пальчиком ромашку на краю")

# 5 СладкоЕШЬко — торт «Муравейник» горкой, по нему ползут муравьишки
I["cafe-sladkoeshko-dmitrov"] = (svg2("#F7FFD6", "#9CC83A", f'''
<ellipse cx="64" cy="110" rx="56" ry="10" fill="#FFFFFF" {s()}/>
<path d="M14 108 Q20 60 64 26 Q108 60 114 108Z" fill="#C88A4A" {s()}/>
{''.join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="#A8692E" {W(1.4)}/>' for x,y in [(40,96),(54,100),(72,98),(88,96),(48,82),(80,84),(60,56),(70,64),(44,70),(90,74),(64,40)])}
<path d="M30 92 Q34 74 46 66 M98 92 Q94 74 82 66" fill="none" stroke="#5A2E1A" stroke-width="3" stroke-linecap="round"/>
<g fill="#2E2A3A">{''.join(f'<circle cx="{x+1.5*i}" cy="{y}" r="1.5"/>' for x,y in [(52,48),(58,72),(76,58),(36,88),(86,88),(70,90)] for i in range(2))}</g>
{face(64, 78, d=12, k=1.0)}
<g transform="translate(96 40)"><ellipse cx="0" cy="0" rx="5" ry="4" fill="#2E2A3A"/><ellipse cx="-8" cy="1" rx="4" ry="3.4" fill="#2E2A3A"/><circle cx="7" cy="-2" r="3.4" fill="#2E2A3A"/>
<path d="M-6 3 l-3 6 M0 3 l0 7 M4 3 l3 6 M8 -5 l3 -6" stroke="#2E2A3A" stroke-width="1.8" stroke-linecap="round"/><circle cx="8" cy="-3" r="1" fill="#fff"/></g>
<rect x="84" y="28" width="6" height="6" rx="1" fill="#FFF4D6" {W(1.4)}/>
'''), "герой: торт «Муравейник» горкой из шоколадных кусочков | сцена: улыбается на блюде, а по склону маленький муравей тащит сахарную крошку")

# 6 Небо (Клин) — имбирное печенье-звезда светится в ночном небе над крышами
I["cafe-nebo-klin"] = (svg2("#2B3C8C", "#101A4A", f'''
{sparkle(20, 30, 3)}{sparkle(108, 26, 3.5)}{sparkle(28, 80, 2.4)}{sparkle(100, 66, 2.4)}
<circle cx="64" cy="58" r="44" fill="#FFE27A" opacity=".18"/>
<path d="M0 104 L18 92 L32 104 L48 88 L64 104 V128 H0Z M64 104 L82 90 L100 104 L114 94 L128 104 V128 H64Z" fill="#1A2560" {s()}/>
<rect x="22" y="104" width="6" height="6" fill="#FFD84A"/><rect x="88" y="106" width="6" height="6" fill="#FFD84A"/>
<path d="M64 14 L76 42 L106 44 L83 63 L91 92 L64 76 L37 92 L45 63 L22 44 L52 42Z" fill="#D88A3E" {s()}/>
<path d="M64 24 L73 44 L95 46 L78 60 M50 44 L33 46" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-dasharray="4 3" stroke-linecap="round"/>
{face(64, 58, d=9, k=0.95)}
'''), "герой: имбирное печенье-звезда с белой глазурью | сцена: светится в тёмно-синем ночном небе над крышами города")

# 7 Кушай слушай — лагман-миска в больших наушниках, лапша пляшет нотами
I["cafe-kushay-slushay-khimki"] = (svg2("#DFFAF7", "#2BA79A", f'''
<path d="M24 40 Q22 8 64 8 Q106 8 104 40" fill="none" stroke="{O}" stroke-width="8"/>
<path d="M24 40 Q22 8 64 8 Q106 8 104 40" fill="none" stroke="#FF6FA3" stroke-width="4"/>
<path d="M44 46 Q38 30 50 28 Q58 38 50 50 M64 44 Q60 26 72 26 Q80 34 70 48 M84 46 Q80 32 90 32" fill="none" stroke="#F5D58A" stroke-width="5" stroke-linecap="round"/>
<path d="M14 54 H114 Q112 98 64 108 Q16 98 14 54Z" fill="#2E6BC4" {s()}/>
<path d="M22 66 Q40 74 64 74 Q88 74 106 66" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="6 5"/>
<ellipse cx="64" cy="54" rx="50" ry="8" fill="#F5D58A" {s()}/>
<rect x="12" y="34" width="16" height="28" rx="7" fill="#FF6FA3" {s()}/>
<rect x="100" y="34" width="16" height="28" rx="7" fill="#FF6FA3" {s()}/>
<path d="M50 112 H78 L74 120 H54Z" fill="#2E6BC4" {s()}/>
{face(64, 84, d=12, k=0.95)}
<path d="M106 18 v12 a3 3 0 1 1 -3 -3 M112 14 v10" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
'''), "герой: синяя пиала лагмана в больших розовых наушниках | сцена: лапша пляшет над пиалой под музыку")

# 8 Ранчо — кукурузный початок-гриль скачет на лошадке-палочке по прерии мимо кактуса
I["cafe-rancho-reutov"] = (svg2("#FFF1C9", "#E0A050", f'''
<circle cx="102" cy="26" r="12" fill="#FFE27A" {s()}/>
<path d="M0 104 Q40 96 70 102 Q100 108 128 100 V128 H0Z" fill="#D9A15A"/>
<path d="M18 104 V70 M18 82 Q8 82 8 72 M18 90 Q28 90 28 80" fill="none" stroke="#4E9A3E" stroke-width="7" stroke-linecap="round"/>
<path d="M30 118 L98 52" stroke="#9A6A3A" stroke-width="5" stroke-linecap="round"/>
<path d="M92 56 Q96 40 110 42 Q120 44 118 54 L106 56 Q100 62 92 56Z" fill="#F5F0E6" {s()}/>
<path d="M98 44 Q96 36 102 34" fill="none" stroke="#7A4A22" stroke-width="4" stroke-linecap="round"/>
<circle cx="110" cy="48" r="2" fill="{O}"/>
<g transform="rotate(-18 58 70)">
<path d="M46 34 Q58 22 70 34 L72 96 Q58 108 44 96Z" fill="#FFD23F" {s()}/>
{''.join(f'<path d="M48 {y} H70" stroke="#E0A020" stroke-width="2"/>' for y in (44,54,64,74,84))}
<path d="M51 30 V100 M58 26 V102 M65 30 V100" stroke="#E0A020" stroke-width="1.6" opacity=".7"/>
<path d="M50 52 l6 -2 M60 70 l7 -2 M52 86 l6 -2" stroke="#7A4A22" stroke-width="3" stroke-linecap="round"/>
<path d="M44 96 Q30 80 36 62 Q42 82 52 90 M72 96 Q86 80 80 62 Q74 82 64 90" fill="#6CB34A" {s()}/>
{face(58, 60, d=7, k=0.85)}
</g>
'''), "герой: жёлтый початок кукурузы-гриль с подпалинками | сцена: скачет верхом на лошадке-палочке по прерии мимо кактуса")

# 9 На бережке — эскимо на палочке сидит на мостках у реки, рядом выпрыгивает рыбка
I["cafe-na-berezhke-ivanteevka"] = (svg2("#E8FBFF", "#3BA0C8", f'''
<path d="M0 30 Q30 20 60 30 Q90 40 128 28 V44 H0Z" fill="#7CC46A"/>
<path d="M0 82 Q20 78 40 82 Q60 86 80 82 Q100 78 128 82 V128 H0Z" fill="#2E86B8"/>
<path d="M10 96 Q20 92 30 96 M60 108 Q70 104 80 108 M96 94 Q106 90 116 94" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".7"/>
<rect x="0" y="74" width="72" height="10" fill="#B8844E" {s()}/>
<path d="M14 84 V112 M54 84 V112" stroke="#8A5A2E" stroke-width="6"/>
<path d="M44 74 V36 Q44 22 58 22 Q72 22 72 36 V74Z" fill="#5A2E1A" {s()}/>
<path d="M44 40 Q50 46 56 40 Q62 46 72 40" fill="none" stroke="#FFF3D6" stroke-width="3"/>
<rect x="55" y="74" width="6" height="22" rx="2" fill="#F5D6A0" {s()}/>
{face(58, 54, d=7, k=0.85)}
<path d="M90 70 Q104 54 116 66 Q108 70 104 66 Q100 76 90 70Z" fill="#FF9A3C" {s()}/>
<circle cx="108" cy="62" r="1.6" fill="{O}"/>
<path d="M86 80 Q90 74 94 80" fill="none" stroke="#fff" stroke-width="2.4"/>
'''), "герой: эскимо в шоколаде на палочке | сцена: сидит на деревянных мостках у реки и болтает палочкой в воде, рядом выпрыгивает рыбка")

# 10 Дворикъ — открытый вишнёвый пирог остывает на столике во дворе под яблоней
I["cafe-dvorik-stupino"] = (svg2("#EFFFE0", "#5DA84A", f'''
<path d="M96 0 V60" stroke="#7A4A22" stroke-width="10"/>
<ellipse cx="96" cy="16" rx="40" ry="26" fill="#4E9A3E" {s()}/>
{''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#E5484D" {W(1.6)}/>' for x,y in [(74,14),(92,24),(110,10),(118,28),(84,4)])}
<rect x="8" y="88" width="34" height="18" fill="#F2D27A" {s()}/>
<path d="M14 88 Q20 80 26 88" fill="#E8C060"/>
<rect x="30" y="76" width="92" height="8" rx="2" fill="#C98A4A" {s()}/>
<path d="M40 84 V118 M112 84 V118" stroke="#8A5A2E" stroke-width="6"/>
<ellipse cx="76" cy="74" rx="38" ry="8" fill="#FFFFFF" {s()}/>
<path d="M44 72 Q44 44 76 44 Q108 44 108 72Z" fill="#E8A64A" {s()}/>
<path d="M54 50 L96 70 M66 46 L104 64 M48 62 L78 72 M98 50 L56 70 M86 46 L48 64 M106 60 L80 72" stroke="#B8442E" stroke-width="4" stroke-linecap="round"/>
{face(76, 60, d=10, k=0.85)}
'''), "герой: открытый вишнёвый пирог с решёткой из теста | сцена: остывает на деревянном столике во дворе под яблоней, рядом песочница")

# 11 Вознесенская — шарик пломбира в креманке взлетает на воздушных шариках над колокольней
I["cafe-voznesenskaya-sergiev"] = (svg2("#E8F0FF", "#F09AC8", f'''
<path d="M10 128 V96 L18 84 L26 96 V128Z" fill="#FFFFFF" {s()}/>
<path d="M12 84 Q18 68 24 84Z" fill="#3E7FD0" {s()}/>
<path d="M18 68 V60 M15 63 H21" stroke="#F2C14E" stroke-width="2.4"/>
<path d="M58 66 L44 34 M64 66 L66 24 M70 66 L90 32" stroke="{O}" stroke-width="1.8"/>
<ellipse cx="42" cy="26" rx="12" ry="14" fill="#FF6FA3" {s()}/>
<ellipse cx="66" cy="16" rx="12" ry="14" fill="#FFD84A" {s()}/>
<ellipse cx="92" cy="24" rx="12" ry="14" fill="#5BC0EB" {s()}/>
<path d="M38 20 Q40 16 44 16 M62 10 Q64 6 68 6 M88 18 Q90 14 94 14" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M50 118 H82 L76 110 H56Z" fill="#B9E3F7" {s()}/>
<path d="M64 110 V100" stroke="{O}" stroke-width="5"/>
<path d="M34 80 H94 Q92 100 64 102 Q36 100 34 80Z" fill="#B9E3F7" {s()}/>
<path d="M36 82 Q36 56 64 56 Q92 56 92 82Z" fill="#FFF8EC" {s()}/>
<circle cx="64" cy="52" r="6" fill="#D9263A" {s()}/>
{face(64, 72, d=10, k=0.9)}
<path d="M100 60 l6 -2 M102 70 l7 1 M24 52 l-6 -3" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
'''), "герой: шарик пломбира с вишенкой в стеклянной креманке | сцена: взлетает на трёх воздушных шариках над белой колокольней")

# 12 Философия — торт-сова в очках сидит на стопке книг и задумчиво подпирает щёку
I["cafe-filosofiya-sergiev"] = (svg2("#FBEBD6", "#A0703A", f'''
<rect x="22" y="100" width="84" height="14" rx="2" fill="#3E7FD0" {s()}/>
<rect x="28" y="88" width="74" height="12" rx="2" fill="#E5484D" {s()}/>
<rect x="18" y="114" width="92" height="12" rx="2" fill="#4E9A3E" {s()}/>
<path d="M30 92 H96 M26 104 H100" stroke="#fff" stroke-width="2" opacity=".6"/>
<path d="M30 88 Q26 40 44 30 L40 14 L54 26 Q64 22 74 26 L88 14 L84 30 Q102 40 98 88Z" fill="#8A5230" {s()}/>
<path d="M36 70 Q64 80 92 70 M38 56 Q64 64 90 56" fill="none" stroke="#F5E6C8" stroke-width="4"/>
<ellipse cx="64" cy="76" rx="16" ry="10" fill="#F5E6C8" {W(2)}/>
<circle cx="52" cy="46" r="10" fill="#FFF4D6" {s()}/><circle cx="76" cy="46" r="10" fill="#FFF4D6" {s()}/>
<path d="M62 46 H66" stroke="{O}" stroke-width="2.6"/>
{eye(52, 46, 0.8)}{eye(76, 46, 0.8)}
<path d="M60 56 L64 62 L68 56Z" fill="#F2A33A" {W(2)}/>
<path d="M96 74 Q108 66 100 54 Q96 48 88 52" fill="#8A5230" {s()}/>
<circle cx="108" cy="28" r="3" fill="#fff" opacity=".8"/><circle cx="116" cy="18" r="5" fill="#fff" opacity=".8"/>
<text x="110" y="22" font-size="9" font-family="Arial" font-weight="bold" fill="{O}">?</text>
'''), "герой: шоколадный торт в форме совы в круглых очках | сцена: сидит на стопке книг и задумчиво подпирает щёку крылом")

# 13 Застолье — румяная запечённая курица на блюде в центре праздничного стола, по краям бокалы морса
I["cafe-zastolye-voskresensk"] = (svg2("#FFF6D0", "#E8B020", f'''
<path d="M0 84 Q64 70 128 84 V128 H0Z" fill="#FFFFFF" {s()}/>
<path d="M0 96 Q64 84 128 96" fill="none" stroke="#E5484D" stroke-width="3" stroke-dasharray="6 6"/>
<ellipse cx="64" cy="98" rx="46" ry="12" fill="#5BC0EB" {s()}/>
<path d="M24 94 Q20 54 64 48 Q108 54 104 94 Q64 104 24 94Z" fill="#D9883A" {s()}/>
<ellipse cx="28" cy="78" rx="12" ry="18" transform="rotate(-62 28 78)" fill="#D9883A" {s()}/>
<ellipse cx="100" cy="78" rx="12" ry="18" transform="rotate(62 100 78)" fill="#D9883A" {s()}/>
<path d="M16 70 L6 62 M112 70 L122 62" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<path d="M6 62 l-3 -5 M6 62 l-6 0 M122 62 l3 -5 M122 62 l6 0" stroke="{O}" stroke-width="2"/>
<path d="M38 64 Q50 56 60 60" fill="none" stroke="#FFD08A" stroke-width="4" stroke-linecap="round"/>
<g fill="#6CB34A">{''.join(f'<circle cx="{x}" cy="{y}" r="3.4"/>' for x,y in [(28,100),(40,104),(88,104),(100,100)])}</g>
{face(64, 76, d=11, k=0.95)}
{sparkle(20, 20, 4)}{sparkle(108, 18, 3.4)}
'''), "герой: румяная запечённая курица на голубом блюде | сцена: в центре праздничного стола на белой скатерти с красной каймой, вокруг веточки укропа")

# 14 Старый Баку — гогал (круглая слоёная булочка) летит на ковре-самолёте над крепостной стеной
I["cafe-stary-baku-naro-fominsk"] = (svg2("#1E6C7A", "#0E3440", f'''
{sparkle(18, 22, 3)}{sparkle(110, 14, 3)}
<path d="M88 12 A14 14 0 1 0 102 34 A11 11 0 1 1 88 12Z" fill="#FFE27A"/>
<path d="M0 128 V104 H10 V98 H20 V104 H30 V98 H40 V104 H50 V98 H60 V104 H70 V98 H80 V104 H90 V98 H100 V104 H110 V98 H120 V104 H128 V128Z" fill="#C9A26A" {s()}/>
<path d="M106 98 V70 H116 V98" fill="#C9A26A" {s()}/>
<path d="M104 70 H118 L111 60Z" fill="#C9A26A" {s()}/>
<path d="M12 82 Q40 72 64 82 Q88 92 116 80 L112 92 Q88 104 64 94 Q40 84 16 94Z" fill="#B3202E" {s()}/>
<path d="M22 86 Q42 78 64 87 Q86 96 108 86" fill="none" stroke="#F2C14E" stroke-width="2.6" stroke-dasharray="4 3"/>
<path d="M16 94 l-4 6 M20 92 l-2 7 M112 92 l4 6 M108 94 l2 7" stroke="#F2C14E" stroke-width="2" stroke-linecap="round"/>
<circle cx="64" cy="58" r="28" fill="#F0B24A" {s()}/>
<path d="M64 58 m-18 0 a18 18 0 1 1 18 18 a12 12 0 1 1 -12 -12 a6 6 0 1 1 6 6" fill="none" stroke="#C47A1E" stroke-width="3"/>
{''.join(f'<circle cx="{x}" cy="{y}" r="1.3" fill="#3B2A1A"/>' for x,y in [(50,42),(76,40),(84,62),(46,72),(70,78)])}
{face(64, 58, d=10, k=0.9)}
'''), "герой: гогал — круглая слоёная булочка-спиралька с чёрным тмином | сцена: летит на красном ковре-самолёте под месяцем над старой крепостной стеной")

# 15 Анталия — симит (бублик с кунжутом) загорает в шезлонге под пляжным зонтиком у моря
I["cafe-antalya-serpukhov"] = (svg2("#FFE9C9", "#2E9CD8", f'''
<circle cx="24" cy="24" r="12" fill="#FFD84A" {s()}/>
<path d="M0 70 Q32 64 64 70 Q96 76 128 68 V92 H0Z" fill="#2E86C8"/>
<path d="M0 88 Q64 80 128 88 V128 H0Z" fill="#F5D9A0"/>
<path d="M96 120 L82 34" stroke="{O}" stroke-width="4"/>
<path d="M50 44 Q76 6 116 28 Q86 30 50 44Z" fill="#FF6F61" {s()}/>
<path d="M62 36 Q80 18 100 24 M78 30 Q90 22 116 28" fill="none" stroke="#FFFFFF" stroke-width="4"/>
<path d="M22 110 L44 84 L94 92 L84 112" fill="none" stroke="#3E7FD0" stroke-width="5" stroke-linecap="round"/>
<path d="M30 102 L48 82 L92 90" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-dasharray="5 5"/>
<g transform="rotate(-10 62 82)">
<ellipse cx="62" cy="80" rx="28" ry="22" fill="#D9883A" {s()}/>
<ellipse cx="62" cy="80" rx="11" ry="7" fill="#F5D9A0" {s()}/>
<path d="M36 74 Q44 60 62 58 Q80 60 88 74" fill="none" stroke="#B5651E" stroke-width="3"/>
{''.join(f'<ellipse cx="{x}" cy="{y}" rx="1.8" ry="1" fill="#FFF3D0"/>' for x,y in [(42,72),(50,64),(60,62),(70,62),(80,66),(86,76),(40,86),(84,88),(56,98),(70,98)])}
<rect x="44" y="66" width="12" height="6" rx="3" fill="{O}"/><rect x="66" y="66" width="12" height="6" rx="3" fill="{O}"/><path d="M56 68 H66" stroke="{O}" stroke-width="2"/>
<path d="M54 90 Q62 94 70 90" fill="none" {W(2.4)}/>
</g>
'''), "герой: турецкий симит — бублик в кунжуте в тёмных очках | сцена: загорает в шезлонге под красным пляжным зонтиком у моря")

# 16 Piccolino — крошечная пицца-малышка тянется на цыпочках к огромной пицце на столе
I["cafe-piccolino-kozino"] = (svg2("#FFE0D6", "#E04A3A", f'''
<rect x="0" y="66" width="128" height="10" fill="#FFFFFF"/>
<path d="M0 66 h16 v10 h16 v-10 h16 v10 h16 v-10 h16 v10 h16 v-10 h16 v10 h16 v-10" fill="#2E9E4A"/>
<path d="M0 76 H128 V128 H0Z" fill="#B9774A"/>
<circle cx="70" cy="40" r="40" fill="#F0B24A" {s()}/>
<circle cx="70" cy="40" r="32" fill="#E5484D"/>
{''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="#FFF3D6" {W(1.6)}/>' for x,y in [(52,24),(84,20),(92,48),(56,56),(74,40)])}
{''.join(f'<path d="M{x} {y} q3 -4 6 0" fill="none" stroke="#3E8A36" stroke-width="3"/>' for x,y in [(64,22),(86,34),(46,40),(74,58)])}
<ellipse cx="88" cy="70" rx="6" ry="2" fill="#5A3A22" opacity=".3"/>
<path d="M26 112 V100 M38 112 V100" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="25" cy="114" rx="4" ry="2.2" fill="{O}"/><ellipse cx="39" cy="114" rx="4" ry="2.2" fill="{O}"/>
<circle cx="32" cy="88" r="15" fill="#F0B24A" {s()}/>
<circle cx="32" cy="88" r="11" fill="#E5484D"/>
<circle cx="26" cy="80" r="2.6" fill="#FFF3D6"/><circle cx="40" cy="96" r="2.6" fill="#FFF3D6"/>
{face(32, 88, d=5, k=0.6)}
<path d="M42 80 Q48 70 50 62" fill="none" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>
'''), "герой: крошечная пицца-малышка на тонких ножках | сцена: тянется на цыпочках к огромной пицце на столе в красно-зелёную клетку")

# 17 Мангал (Фрязино) — купаты: колбаска-гриль, свёрнутая колечком, прыгает пружинкой с пенька
I["cafe-mangal-fryazino"] = (svg2("#DDF5D0", "#3C8A3C", f'''
<path d="M0 100 Q64 88 128 100 V128 H0Z" fill="#4E9A3E"/>
<path d="M6 116 V96 Q6 88 24 88 Q42 88 42 96 V116Z" fill="#9A6A3A" {s()}/>
<ellipse cx="24" cy="92" rx="18" ry="6" fill="#E6C38A" {s()}/>
<path d="M30 84 Q40 60 52 56 M38 90 Q50 72 58 70" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 5" stroke-linecap="round"/>
<path d="M78.2 62.8 L78.0 63.0 L77.8 63.2 L77.5 63.5 L77.3 63.7 L77.0 63.9 L76.7 64.1 L76.4 64.3 L76.1 64.5 L75.7 64.7 L75.3 64.9 L74.9 65.0 L74.5 65.1 L74.1 65.2 L73.7 65.3 L73.2 65.4 L72.8 65.4 L72.3 65.5 L71.8 65.5 L71.3 65.5 L70.8 65.4 L70.3 65.4 L69.8 65.3 L69.3 65.2 L68.8 65.0 L68.2 64.9 L67.7 64.7 L67.2 64.5 L66.7 64.3 L66.2 64.0 L65.7 63.7 L65.3 63.4 L64.8 63.1 L64.4 62.7 L63.9 62.3 L63.5 61.9 L63.1 61.5 L62.7 61.0 L62.4 60.6 L62.1 60.1 L61.8 59.5 L61.5 59.0 L61.2 58.4 L61.0 57.9 L60.8 57.3 L60.7 56.7 L60.6 56.1 L60.5 55.4 L60.4 54.8 L60.4 54.2 L60.4 53.5 L60.5 52.8 L60.6 52.2 L60.7 51.5 L60.9 50.8 L61.1 50.2 L61.4 49.5 L61.7 48.9 L62.0 48.2 L62.4 47.6 L62.8 46.9 L63.3 46.3 L63.8 45.7 L64.4 45.1 L64.9 44.5 L65.6 43.9 L66.2 43.4 L66.9 42.9 L67.6 42.4 L68.4 41.9 L69.2 41.5 L70.0 41.0 L70.9 40.7 L71.8 40.3 L72.7 40.0 L73.6 39.7 L74.6 39.5 L75.6 39.2 L76.6 39.1 L77.6 38.9 L78.7 38.8 L79.7 38.8 L80.8 38.8 L81.9 38.8 L82.9 38.9 L84.0 39.0 L85.1 39.2 L86.2 39.4 L87.3 39.6 L88.3 39.9 L89.4 40.3 L90.5 40.7 L91.5 41.1 L92.5 41.6 L93.5 42.1 L94.5 42.7 L95.5 43.3 L96.4 43.9 L97.3 44.6 L98.1 45.4 L99.0 46.2 L99.8 47.0 L100.5 47.8 L101.2 48.7 L101.9 49.6 L102.5 50.6 L103.1 51.6 L103.6 52.6 L104.1 53.6 L104.5 54.7 L104.8 55.7 L105.1 56.9 L105.4 58.0 L105.6 59.1 L105.7 60.3 L105.7 61.4 L105.7 62.6 L105.6 63.8 L105.5 65.0 L105.3 66.2 L105.0 67.4 L104.7 68.5 L104.3 69.7 L103.8 70.9 L103.3 72.0 L102.7 73.2 L102.0 74.3 L101.3 75.4 L100.5 76.4 L99.6 77.5 L98.7 78.5 L97.7 79.5 L96.7 80.5 L95.6 81.4 L94.4 82.3 L93.2 83.1 L92.0 83.9 L90.6 84.6 L89.3 85.3 L87.9 86.0 L86.4 86.6 L85.0 87.1 L83.4 87.6 L81.9 88.1 L80.3 88.4 L78.7 88.7 L77.0 89.0 L75.4 89.2 L73.7 89.3 L72.0 89.4 L70.3 89.3 L68.6 89.3 L66.9 89.1 L65.2 88.9 L63.5 88.6 L61.8 88.3 L60.1 87.9 L58.4 87.4 L56.8 86.8 L55.1 86.2 L53.5 85.5 L52.0 84.8 L50.4 83.9 L48.9 83.1 L47.5 82.1 L46.1 81.1 L44.7 80.0 L43.4 78.9 L42.1 77.7 L40.9 76.5 L39.8 75.2 L38.7 73.9 L37.7 72.5 L36.8 71.1 L35.9 69.6 L35.2 68.1 L34.5 66.6 L33.8 65.0 L33.3 63.4 L32.9 61.8 L32.5 60.1" fill="none" stroke="{O}" stroke-width="17" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M78.2 62.8 L78.0 63.0 L77.8 63.2 L77.5 63.5 L77.3 63.7 L77.0 63.9 L76.7 64.1 L76.4 64.3 L76.1 64.5 L75.7 64.7 L75.3 64.9 L74.9 65.0 L74.5 65.1 L74.1 65.2 L73.7 65.3 L73.2 65.4 L72.8 65.4 L72.3 65.5 L71.8 65.5 L71.3 65.5 L70.8 65.4 L70.3 65.4 L69.8 65.3 L69.3 65.2 L68.8 65.0 L68.2 64.9 L67.7 64.7 L67.2 64.5 L66.7 64.3 L66.2 64.0 L65.7 63.7 L65.3 63.4 L64.8 63.1 L64.4 62.7 L63.9 62.3 L63.5 61.9 L63.1 61.5 L62.7 61.0 L62.4 60.6 L62.1 60.1 L61.8 59.5 L61.5 59.0 L61.2 58.4 L61.0 57.9 L60.8 57.3 L60.7 56.7 L60.6 56.1 L60.5 55.4 L60.4 54.8 L60.4 54.2 L60.4 53.5 L60.5 52.8 L60.6 52.2 L60.7 51.5 L60.9 50.8 L61.1 50.2 L61.4 49.5 L61.7 48.9 L62.0 48.2 L62.4 47.6 L62.8 46.9 L63.3 46.3 L63.8 45.7 L64.4 45.1 L64.9 44.5 L65.6 43.9 L66.2 43.4 L66.9 42.9 L67.6 42.4 L68.4 41.9 L69.2 41.5 L70.0 41.0 L70.9 40.7 L71.8 40.3 L72.7 40.0 L73.6 39.7 L74.6 39.5 L75.6 39.2 L76.6 39.1 L77.6 38.9 L78.7 38.8 L79.7 38.8 L80.8 38.8 L81.9 38.8 L82.9 38.9 L84.0 39.0 L85.1 39.2 L86.2 39.4 L87.3 39.6 L88.3 39.9 L89.4 40.3 L90.5 40.7 L91.5 41.1 L92.5 41.6 L93.5 42.1 L94.5 42.7 L95.5 43.3 L96.4 43.9 L97.3 44.6 L98.1 45.4 L99.0 46.2 L99.8 47.0 L100.5 47.8 L101.2 48.7 L101.9 49.6 L102.5 50.6 L103.1 51.6 L103.6 52.6 L104.1 53.6 L104.5 54.7 L104.8 55.7 L105.1 56.9 L105.4 58.0 L105.6 59.1 L105.7 60.3 L105.7 61.4 L105.7 62.6 L105.6 63.8 L105.5 65.0 L105.3 66.2 L105.0 67.4 L104.7 68.5 L104.3 69.7 L103.8 70.9 L103.3 72.0 L102.7 73.2 L102.0 74.3 L101.3 75.4 L100.5 76.4 L99.6 77.5 L98.7 78.5 L97.7 79.5 L96.7 80.5 L95.6 81.4 L94.4 82.3 L93.2 83.1 L92.0 83.9 L90.6 84.6 L89.3 85.3 L87.9 86.0 L86.4 86.6 L85.0 87.1 L83.4 87.6 L81.9 88.1 L80.3 88.4 L78.7 88.7 L77.0 89.0 L75.4 89.2 L73.7 89.3 L72.0 89.4 L70.3 89.3 L68.6 89.3 L66.9 89.1 L65.2 88.9 L63.5 88.6 L61.8 88.3 L60.1 87.9 L58.4 87.4 L56.8 86.8 L55.1 86.2 L53.5 85.5 L52.0 84.8 L50.4 83.9 L48.9 83.1 L47.5 82.1 L46.1 81.1 L44.7 80.0 L43.4 78.9 L42.1 77.7 L40.9 76.5 L39.8 75.2 L38.7 73.9 L37.7 72.5 L36.8 71.1 L35.9 69.6 L35.2 68.1 L34.5 66.6 L33.8 65.0 L33.3 63.4 L32.9 61.8 L32.5 60.1" fill="none" stroke="#B8462A" stroke-width="11.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M59.8 57.5 l4 4" stroke="#5A1E0E" stroke-width="2.6" stroke-linecap="round"/><path d="M61.8 43.7 l4 4" stroke="#5A1E0E" stroke-width="2.6" stroke-linecap="round"/><path d="M80.9 36.9 l4 4" stroke="#5A1E0E" stroke-width="2.6" stroke-linecap="round"/><path d="M101.1 49.6 l4 4" stroke="#5A1E0E" stroke-width="2.6" stroke-linecap="round"/><path d="M98.5 74.4 l4 4" stroke="#5A1E0E" stroke-width="2.6" stroke-linecap="round"/><path d="M68.3 87.3 l4 4" stroke="#5A1E0E" stroke-width="2.6" stroke-linecap="round"/><path d="M35.7 70.5 l4 4" stroke="#5A1E0E" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="76" cy="58" r="13" fill="#B8462A" {s()}/>
{face(76, 56, d=6, k=0.7)}
<path d="M66 108 Q74 100 82 108 Q90 100 98 108" fill="none" stroke="#2E6A2A" stroke-width="3" stroke-linecap="round"/>
'''), "герой: купаты — колбаска-гриль, свёрнутая колечком | сцена: прыгает пружинкой с лесного пенька на полянку")

# 18 Казбеги — аджарский хачапури-лодочка с желтком плывёт по горной реке под снежной вершиной
I["cafe-kazbegi-klin"] = (svg2("#F0F6FF", "#7C9CC8", f'''
<path d="M0 70 L34 24 L52 44 L76 8 L128 70Z" fill="#8A93B8" {s()}/>
<path d="M66 24 L76 8 L88 26 L82 22 L76 28 L70 22Z" fill="#FFFFFF" {W(2)}/>
<path d="M26 36 L34 24 L42 34 L36 31Z" fill="#FFFFFF" {W(2)}/>
<path d="M0 70 Q64 62 128 70 V128 H0Z" fill="#4FB0E0"/>
<path d="M8 116 Q20 110 32 116 M92 120 Q104 114 116 120 M100 76 Q110 72 120 76" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
<path d="M4 84 Q14 58 64 60 Q114 58 124 84 Q108 112 64 112 Q20 112 4 84Z" fill="#E8A64A" {s()}/>
<path d="M4 84 Q0 74 6 70 M124 84 Q128 74 122 70" fill="none" stroke="#E8A64A" stroke-width="8" stroke-linecap="round"/>
<path d="M30 76 Q44 68 64 68 Q84 68 98 76 Q86 84 64 84 Q42 84 30 76Z" fill="#FFF4D6" {s()}/>
<circle cx="64" cy="76" r="7" fill="#FFB52E" {W(2.2)}/>
<rect x="76" y="72" width="9" height="5" rx="2" fill="#FFF0A0" {W(1.4)}/>
{face(64, 96, d=13, k=0.95)}
'''), "герой: аджарский хачапури-лодочка с желтком и кусочком масла | сцена: плывёт по горной реке под снежной вершиной Казбека")

# 20 Сыр да мука — мешок муки обнимает головку сыра
I["cafe-syr-da-muka-pushkino"] = (svg2("#FFF8E6", "#D9B66A", f'''
<path d="M0 108 H128 V128 H0Z" fill="#B88A50"/>
<path d="M18 112 Q12 70 22 46 Q24 36 34 36 L58 36 Q68 36 70 46 Q80 70 74 112Z" fill="#F5EFE3" {s()}/>
<path d="M28 36 Q46 24 64 36" fill="#F5EFE3" {s()}/>
<path d="M30 30 Q46 40 62 30" fill="none" stroke="#C98A4A" stroke-width="4"/>
<text x="30" y="70" font-size="13" font-family="Arial" font-weight="bold" fill="#C98A4A">МУКА</text>
{face(46, 84, d=9, k=0.85)}
<ellipse cx="34" cy="48" rx="6" ry="3" fill="#fff"/>
<circle cx="24" cy="26" r="2" fill="#fff" opacity=".9"/><circle cx="70" cy="22" r="2.4" fill="#fff" opacity=".9"/>
<path d="M66 112 Q62 84 84 74 Q106 70 116 84 Q122 100 112 112Z" fill="#FFC93C" {s()}/>
<ellipse cx="92" cy="80" rx="22" ry="7" fill="#FFE07A" {s()}/>
<circle cx="80" cy="96" r="4" fill="#E8A82A"/><circle cx="104" cy="100" r="3" fill="#E8A82A"/><circle cx="96" cy="90" r="2.6" fill="#E8A82A"/>
{face(92, 100, d=7, k=0.7, mouth=False)}
<path d="M72 92 Q78 102 84 96" fill="none" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<path d="M72 92 Q78 102 84 96" fill="none" stroke="#F5EFE3" stroke-width="2.4" stroke-linecap="round"/>
'''), "герой: мешок муки с надписью «МУКА» | сцена: обнимает круглую головку жёлтого сыра на деревянном полу пекарни")

# 22 Павлин — павлин распустил хвост из разноцветных печений-макарон на лужайке
I["cafe-pavlin-protvino"] = (svg2("#D6F7FF", "#1C6FB0", f'''
<path d="M0 106 Q64 96 128 106 V128 H0Z" fill="#5DB84A"/>
{''.join(f'<g transform="rotate({a} 64 92)"><rect x="60" y="34" width="8" height="58" rx="4" fill="#2E9E7A"/><ellipse cx="64" cy="30" rx="10" ry="6.5" fill="{c}" {W(2)}/><path d="M55 30 H73" stroke="#FFF4E0" stroke-width="2.6"/></g>' for a,c in [(-70,"#FF8FB1"),(-47,"#FFD84A"),(-23,"#9FE07A"),(0,"#B69CF0"),(23,"#FF9A5A"),(47,"#7FD3F7"),(70,"#FF8FB1")])}
<path d="M52 108 Q46 80 56 68 Q60 52 64 46 Q72 52 72 68 Q82 80 76 108Z" fill="#1E5FC8" {s()}/>
<circle cx="64" cy="48" r="11" fill="#1E5FC8" {s()}/>
<path d="M60 36 L58 28 M64 36 V26 M68 36 L70 28" stroke="{O}" stroke-width="1.8"/>
<circle cx="58" cy="28" r="2.4" fill="#2E9E7A"/><circle cx="64" cy="26" r="2.4" fill="#2E9E7A"/><circle cx="70" cy="28" r="2.4" fill="#2E9E7A"/>
{face(64, 48, d=5, k=0.6, mouth=False)}
<path d="M62 54 L64 58 L66 54Z" fill="#F2A33A" {W(1.4)}/>
<path d="M58 108 V116 M70 108 V116" stroke="#F2A33A" stroke-width="3"/>
'''), "герой: синий павлин с хвостом-веером из разноцветных печений макарон | сцена: распустил хвост на зелёной лужайке")

# 23 Маковка — маковый рулет съезжает с луковичного купола-маковки, как с горки
I["cafe-makovka-elektrostal"] = (svg2("#FFEFD9", "#9A5AC8", f'''
<rect x="66" y="78" width="54" height="50" fill="#FFFFFF" {s()}/>
<path d="M84 128 V104 Q93 94 102 104 V128" fill="#9A5AC8" {s()}/>
<path d="M60 80 Q58 40 93 18 Q128 40 126 80Z" fill="#F2C14E" {s()}/>
<path d="M93 18 V2 M87 8 H99" stroke="#F2C14E" stroke-width="4"/>
<path d="M76 62 Q93 54 112 62" fill="none" stroke="#D99A1E" stroke-width="3"/>
<path d="M2 116 Q30 112 60 80" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="4 6" stroke-linecap="round"/>
<g transform="rotate(-38 40 70)">
<rect x="14" y="56" width="56" height="30" rx="14" fill="#E8B060" {s()}/>
<circle cx="70" cy="71" r="15" fill="#E8B060" {s()}/>
<path d="M70 71 m-10 0 a10 10 0 1 1 10 10 a6 6 0 1 1 -6 -6 a3 3 0 1 1 3 3" fill="none" stroke="#2E2A3A" stroke-width="4"/>
{''.join(f'<circle cx="{x}" cy="{y}" r="1.1" fill="#2E2A3A"/>' for x,y in [(22,62),(30,60),(40,62),(26,80),(36,82),(48,60),(50,82)])}
{face(36, 71, d=8, k=0.8)}
</g>
'''), "герой: маковый рулет-спиралька | сцена: весело съезжает с золотого луковичного купола-маковки, как с горки")

# 24 Bonbon — карамелька в полосатом фантике качается на качелях в детской игровой
I["cafe-bonbon-dubna"] = (svg2("#FFF0F6", "#F06A9A", f'''
<path d="M0 108 H128 V128 H0Z" fill="#7FD3F7"/>
<path d="M0 108 h16 v20 h-16z M32 108 h16 v20 h-16z M64 108 h16 v20 h-16z M96 108 h16 v20 h-16z" fill="#FFE07A"/>
<path d="M16 0 V30 M112 0 V30" stroke="{O}" stroke-width="3"/>
<path d="M8 4 H120" stroke="#9A5AC8" stroke-width="8" stroke-linecap="round"/>
<g transform="rotate(10 64 0)">
<path d="M30 4 V82 M98 4 V82" stroke="{O}" stroke-width="2.6"/>
<rect x="24" y="82" width="80" height="8" rx="3" fill="#FF8A3C" {s()}/>
<path d="M42 64 L22 52 L24 76Z M86 64 L106 52 L104 76Z" fill="#FFFFFF" {s()}/>
<path d="M26 58 L30 72 M100 58 L98 72" stroke="#E5484D" stroke-width="3"/>
<ellipse cx="64" cy="64" rx="24" ry="18" fill="#FFFFFF" {s()}/>
<clipPath id="cb"><ellipse cx="64" cy="64" rx="23" ry="17"/></clipPath>
<g clip-path="url(#cb)">{''.join(f'<path d="M{x} 40 L{x+20} 90" stroke="#E5484D" stroke-width="6"/>' for x in (28,44,60,76,92))}</g>
<ellipse cx="64" cy="64" rx="24" ry="18" fill="none" {s()}/>
<rect x="50" y="60" width="28" height="16" rx="7" fill="#FFFFFF" opacity=".85"/>
{face(64, 64, d=8, k=0.75)}
</g>
'''), "герой: карамелька-бонбон в красно-белом полосатом фантике | сцена: раскачивается на верёвочных качелях в детской игровой комнате")

if __name__ == "__main__":
    reg = os.path.join(ROOT, "icons-src", "subjects.txt")
    have = open(reg, encoding="utf-8").read()
    lines = []
    for pid, (svg, subj) in I.items():
        open(os.path.join(ROOT, "icons-src", f"{pid}.svg"), "w").write(svg)
        if f"\n{pid} — " not in "\n" + have:
            lines.append(f"{pid} — {subj}")
    if lines:
        with open(reg, "a", encoding="utf-8") as f:
            if not have.endswith("\n"):
                f.write("\n")
            f.write("\n".join(lines) + "\n")
    print("иконок:", len(I))
