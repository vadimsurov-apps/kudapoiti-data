"""Робот cafes, 2026-11-08 (01 UTC): иконки 28 новых кафе. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя компоновка и палитра фона).
Запуск из корня: python3 tools/icons_cafes_1108.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
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


def omouth(cx, cy, k=1.0):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{3.2*k}" ry="{4*k}" fill="#C0392B" {W(2*k)}/>'


def dots(pts, r, fill):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>' for x, y in pts)


I = {}

# 1 Якитория Дмитров — чаша маття, внутри кружится бамбуковый венчик-тясэн
I["cafe-yakitoriya-dmitrov"] = (svg2("#F1F8DA", "#5E9E4A", f'''
<ellipse cx="64" cy="112" rx="44" ry="8" fill="#3F6E33" opacity=".35"/>
<g transform="rotate(-14 70 44)">
<rect x="62" y="6" width="12" height="34" rx="5" fill="#E8C98A" {s()}/>
<path d="M54 40 H82 L90 70 H46Z" fill="#F5DFA8" {s()}/>
<path d="M52 46 L48 68 M58 44 L56 70 M64 44 V70 M70 44 L72 70 M76 44 L80 68 M82 46 L86 66" stroke="{O}" stroke-width="1.8"/>
</g>
<path d="M18 66 H110 Q108 108 64 110 Q20 108 18 66Z" fill="#2E2A3A" {s()}/>
<path d="M24 76 Q64 84 104 76" fill="none" stroke="#6E6880" stroke-width="3"/>
<ellipse cx="64" cy="66" rx="46" ry="11" fill="#7DBE4E" {s()}/>
<ellipse cx="60" cy="65" rx="22" ry="5" fill="#B9E28C"/>
{dots([(44,63),(80,67),(90,63),(52,69)],2.4,"#D8F5B5")}
<path d="M30 54 Q22 48 28 40 M98 54 Q108 46 100 38" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{face(64, 92, d=11, k=0.95)}
'''), "герой: чёрная чаша-тяван с ярко-зелёным маття | сцена: бамбуковый венчик-тясэн кружится в ней, взбивая пузырчатую пенку")

# 2 Якитория Пушкино — такояки в лодочке-фунэ, хлопья тунца пляшут на горячих шариках
I["cafe-yakitoriya-pushkino"] = (svg2("#FFE9CC", "#E07B39", f'''
<path d="M10 82 H118 L104 108 H24Z" fill="#D9A25E" {s()}/>
<path d="M18 90 H110" stroke="#B57B3C" stroke-width="2.5"/>
<circle cx="38" cy="72" r="19" fill="#E9A44B" {s()}/>
<circle cx="90" cy="72" r="19" fill="#E9A44B" {s()}/>
<circle cx="64" cy="64" r="23" fill="#F0B055" {s()}/>
<path d="M22 66 Q38 58 54 66 M74 66 Q90 58 106 66 M44 54 Q64 46 84 56" fill="none" stroke="#5A2E1A" stroke-width="5" stroke-linecap="round"/>
<path d="M48 58 Q56 54 62 60 Q70 54 80 60" fill="none" stroke="#FFF6D8" stroke-width="2.4" stroke-linecap="round"/>
{dots([(32,64),(96,64),(58,52),(72,56)],1.8,"#4E9A3A")}
<path d="M30 46 q4 -10 10 -4 q-6 4 -10 4Z M86 40 q8 -8 10 2 q-6 0 -10 -2Z M60 30 q6 -10 12 -2 q-8 2 -12 2Z" fill="#F7C9A8" {W(1.6)}/>
<path d="M44 34 q-2 -6 2 -10 M96 30 q2 -6 -2 -10" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round"/>
{face(64, 72, d=9, k=0.85)}
{closed(38, 78, d=5, k=0.6)}{closed(90, 78, d=5, k=0.6)}
'''), "герой: три шарика такояки в деревянной лодочке-фунэ под соусом | сцена: на горячих шариках пляшут лепестки тунцовой стружки")

# 3 Якитория Раменское — дайфуку с клубникой, разрезанный пополам, половинки кланяются
I["cafe-yakitoriya-ramenskoe"] = (svg2("#FFE6F0", "#D86A9A", f'''
<path d="M6 104 Q64 82 122 104 L122 128 H6Z" fill="#6DB36A" {s()}/>
<path d="M14 104 Q64 88 116 104" fill="none" stroke="#A6DA8F" stroke-width="3"/>
<g transform="rotate(-16 38 80)">
<path d="M14 98 Q12 52 40 50 Q62 52 62 98Z" fill="#FFFFFF" {s()}/>
<path d="M60 98 Q60 60 44 58 Q28 66 30 98Z" fill="#F5E6EE"/>
<path d="M58 96 Q58 66 46 64 Q36 70 38 96Z" fill="#E5484D" {W(2)}/>
{dots([(44,72),(48,82),(42,88)],1.4,"#FFE08A")}
{closed(26, 76, d=5, k=0.65)}
</g>
<g transform="rotate(16 90 80)">
<path d="M66 98 Q66 52 90 50 Q116 52 114 98Z" fill="#FFFFFF" {s()}/>
<path d="M68 96 Q68 66 80 64 Q92 70 90 96Z" fill="#E5484D" {W(2)}/>
{dots([(80,72),(76,82),(84,88)],1.4,"#FFE08A")}
{closed(102, 76, d=5, k=0.65)}
</g>
<path d="M60 26 Q64 18 68 26 Q64 32 60 26Z" fill="#FF7FA8"/>
<path d="M52 36 Q64 28 76 36 Q64 46 52 36Z" fill="#FF7FA8" opacity=".85"/>
'''), "герой: рисовое моти-дайфуку с клубникой внутри, разрезанное пополам | сцена: две половинки вежливо кланяются друг другу на зелёном листе")

# 4 Якитория Видное — унадон: угорь улёгся на рис в лакированной миске
I["cafe-yakitoriya-vidnoe"] = (svg2("#FFF3CF", "#C98B2B", f'''
<path d="M12 70 H116 Q114 114 64 116 Q14 114 12 70Z" fill="#B3262C" {s()}/>
<path d="M18 84 Q64 92 110 84" fill="none" stroke="#7A1418" stroke-width="3"/>
<path d="M14 70 Q24 50 44 56 Q64 46 84 56 Q104 50 114 70Z" fill="#FFFFFF" {s()}/>
{dots([(34,62),(52,58),(72,57),(92,62),(60,64),(82,65)],1.6,"#EEE8DC")}
<path d="M14 64 Q30 40 56 50 Q78 58 98 44 Q110 36 118 46 Q110 58 98 56 Q78 70 56 62 Q32 54 20 70Z" fill="#8A4A1E" {s()}/>
<path d="M30 54 l6 6 M44 52 l6 7 M60 56 l6 6 M76 56 l6 5 M92 50 l5 5" stroke="#5A2C10" stroke-width="2.4" stroke-linecap="round"/>
<path d="M30 52 Q56 60 96 46" fill="none" stroke="#C47A3E" stroke-width="2" opacity=".8"/>
{eye(110, 46, 0.6)}
<path d="M114 52 q2 2 4 0" fill="none" {W(1.8)}/>
<path d="M40 36 q-4 -8 2 -14 M60 32 q-4 -8 2 -14 M80 30 q-4 -8 2 -14" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round"/>
{face(64, 96, d=12, k=0.9)}
'''), "герой: лакированная красная миска унадона с угрём на рисе | сцена: угорь растянулся по рису, как на перине, и греется в пару")

# 5 Тануки Мытищи — удон прыгает через лапшу-скакалку над миской
I["cafe-tanuki-mytishchi"] = (svg2("#E4E8FF", "#5865C8", f'''
<path d="M22 84 H106 Q104 116 64 118 Q24 116 22 84Z" fill="#F4F1EA" {s()}/>
<path d="M24 96 H104" stroke="#5865C8" stroke-width="4"/>
<path d="M30 104 H98" stroke="#5865C8" stroke-width="2"/>
<ellipse cx="64" cy="84" rx="42" ry="9" fill="#E8C78E" {s()}/>
<path d="M36 84 C30 40 46 14 64 14 C82 14 98 40 92 84" fill="none" stroke="#FFF2D2" stroke-width="7" stroke-linecap="round"/>
<path d="M36 84 C30 40 46 14 64 14 C82 14 98 40 92 84" fill="none" stroke="{O}" stroke-width="1.6" stroke-dasharray="0" opacity=".5"/>
<rect x="50" y="44" width="28" height="26" rx="9" fill="#FFF2D2" {s()}/>
<path d="M54 70 l-4 10 M74 70 l4 10" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
{face(64, 56, d=6, k=0.6)}
<path d="M50 52 L34 76 M78 52 L94 76" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<path d="M44 84 Q52 78 60 84 Q68 78 76 84" fill="none" stroke="#FFF2D2" stroke-width="4" stroke-linecap="round"/>
<circle cx="86" cy="82" r="5" fill="#fff" {W(1.6)}/><circle cx="86" cy="82" r="2" fill="#F5A3C0"/>
{sparkle(20, 40, 5)}{sparkle(108, 34, 4)}
'''), "герой: толстая лапшинка удон | сцена: прыгает через скакалку из другой лапшины прямо над фарфоровой миской с бульоном")

# 6 Тануки Подольск — толстый футомаки-колесо катится по бамбуковому коврику
I["cafe-tanuki-podolsk"] = (svg2("#DAFFF1", "#2FAE8C", f'''
<path d="M0 98 L128 86 L128 128 L0 128Z" fill="#E6C77C" {s()}/>
{''.join(f'<path d="M{x} {98-x*0.094:.1f} V128" stroke="#B9944A" stroke-width="2"/>' for x in range(8, 128, 12))}
<circle cx="70" cy="60" r="34" fill="#1F3A2E" {s()}/>
<circle cx="70" cy="60" r="27" fill="#FFFFFF" {W(2)}/>
<path d="M70 60 L70 36 A24 24 0 0 1 91 50Z" fill="#F07A55"/>
<path d="M70 60 L91 50 A24 24 0 0 1 86 78Z" fill="#7BC86C"/>
<path d="M70 60 L86 78 A24 24 0 0 1 54 79Z" fill="#FFD45E"/>
<path d="M70 60 L54 79 A24 24 0 0 1 47 50Z" fill="#F5A3C0"/>
<circle cx="70" cy="60" r="11" fill="#FFFFFF" {W(1.6)}/>
{face(70, 58, d=5, k=0.55)}
<path d="M30 52 H14 M28 64 H8 M32 76 H16" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{dots([(26,94),(18,96),(36,92)],2.2,"#FFFFFF")}
'''), "герой: толстый ролл-футомаки с разноцветной начинкой-радугой | сцена: катится колесом по бамбуковому коврику-макису, роняя рисинки")

# 7 Планета Суши Чехов — бутылочка-рыбка с соевым соусом капает на нигири, нигири раскрыл рот
I["cafe-planeta-sushi-chekhov"] = (svg2("#E8F7FF", "#4AA3DF", f'''
<ellipse cx="64" cy="114" rx="46" ry="8" fill="#2D6E9E" opacity=".3"/>
<rect x="20" y="96" width="88" height="12" rx="4" fill="#3B3355" {s()}/>
<path d="M30 96 Q28 74 64 74 Q100 74 98 96Z" fill="#FFFFFF" {s()}/>
<path d="M26 82 Q30 64 64 66 Q100 64 104 82 Q90 90 64 86 Q38 90 26 82Z" fill="#FF8A5B" {s()}/>
<path d="M44 74 l6 8 M60 70 l6 10 M76 72 l6 8" stroke="#FFD3BF" stroke-width="3" stroke-linecap="round"/>
{eye(52, 90, 0.7)}{eye(76, 90, 0.7)}
<ellipse cx="64" cy="94" rx="5" ry="3.4" fill="#C0392B" {W(1.6)}/>
<g transform="rotate(28 70 30)">
<path d="M36 30 Q50 14 74 22 Q86 26 92 30 Q86 34 74 38 Q50 46 36 30Z" fill="#E8F3FF" opacity=".9" {s()}/>
<path d="M44 30 Q56 22 72 26 Q80 28 84 30 Q80 32 72 34 Q56 38 44 30Z" fill="#5A2C10"/>
<path d="M92 30 L104 22 L104 38Z" fill="#E8F3FF" {s()}/>
<rect x="24" y="26" width="14" height="8" rx="3" fill="#E5484D" {s()}/>
{eye(76, 26, 0.6)}
</g>
<path d="M44 52 Q40 60 44 64 Q48 60 44 52Z" fill="#5A2C10" {W(1.4)}/>
'''), "герой: пластиковая бутылочка-рыбка с соевым соусом | сцена: наклонилась и капает соус на нигири, а нигири с удивлением раскрыл рот")

# 8 IL Патио Сергиев Посад — пицца крутится на ребре, как волчок
I["cafe-ilpatio-sergiev-posad"] = (svg2("#FBE8FF", "#9B51E0", f'''
<ellipse cx="64" cy="112" rx="30" ry="6" fill="#5B2C8F" opacity=".35"/>
<path d="M20 50 Q10 64 22 80 M106 46 Q118 62 108 82" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M14 40 Q6 64 16 90 M112 36 Q124 62 116 92" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".5"/>
<g transform="rotate(-12 64 70)">
<ellipse cx="64" cy="70" rx="44" ry="30" fill="#E9B062" {s()}/>
<ellipse cx="64" cy="68" rx="37" ry="23" fill="#E5484D"/>
<ellipse cx="64" cy="66" rx="34" ry="19" fill="#FFE7A3"/>
<circle cx="44" cy="62" r="6" fill="#E5484D" {W(1.6)}/><circle cx="86" cy="64" r="6" fill="#E5484D" {W(1.6)}/>
<path d="M60 56 q6 -6 10 0 q-6 4 -10 0Z M76 78 q6 -6 10 0 q-6 4 -10 0Z" fill="#3E9B4A"/>
<path d="M58 100 L64 112 L70 100" fill="#E9B062" {s()}/>
{face(64, 72, d=9, k=0.8)}
</g>
<path d="M98 26 q6 -6 12 0 q-6 6 -12 0Z" fill="#3E9B4A" {W(1.6)}/>
<path d="M22 22 q6 -6 12 0 q-6 6 -12 0Z" fill="#3E9B4A" {W(1.6)}/>
'''), "герой: круглая пицца-маргарита | сцена: вращается на столе на одном кончике, как волчок, и с неё разлетаются листики базилика")

# 9 IL Патио «Красный кит» — гора спагетти болоньезе, тёрка сыплет сырный снег
I["cafe-ilpatio-krasny-kit"] = (svg2("#FFEDE8", "#E2574C", f'''
<ellipse cx="64" cy="104" rx="52" ry="14" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="102" rx="38" ry="8" fill="#F2EEE8"/>
<path d="M26 100 Q30 56 64 50 Q98 56 102 100Z" fill="#F7D774" {s()}/>
<path d="M34 92 Q44 70 60 86 Q72 66 88 90 M40 80 Q52 60 70 74 Q82 60 94 82 M48 66 Q60 54 76 64" fill="none" stroke="#E2B444" stroke-width="2.6"/>
<path d="M38 66 Q50 44 64 52 Q80 42 92 66 Q78 74 64 66 Q50 76 38 66Z" fill="#B9442E" {s()}/>
{dots([(52,60),(70,58),(80,64)],2.4,"#7A2A18")}
{face(64, 84, d=10, k=0.85)}
<g transform="rotate(18 98 24)">
<path d="M86 4 H108 L112 40 H82Z" fill="#C9CED6" {s()}/>
{dots([(90,14),(96,14),(102,14),(92,22),(98,22),(104,22),(90,30),(96,30),(102,30)],1.4,O)}
<rect x="90" y="-6" width="14" height="12" rx="4" fill="#3B3355"/>
</g>
{dots([(80,44),(86,40),(76,36),(90,48),(70,42),(84,32)],1.8,"#FFF6CF")}
'''), "герой: горка спагетти болоньезе с мясным соусом на макушке | сцена: над ней металлическая тёрка натирает сырный снег, и он сыплется хлопьями")

# 10 Моремания Мытищи — стейк лосося на решётке над углями поднимает веточку укропа, как флажок
I["cafe-moremania-mytishchi"] = (svg2("#2F4A8A", "#101A3C", f'''
<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#3A2A2A"/>
{dots([(20,108),(40,112),(62,106),(86,112),(106,108),(30,118),(74,118),(96,120)],7,"#E5642F")}
{dots([(20,108),(62,106),(106,108),(74,118)],3.5,"#FFC14D")}
<path d="M8 92 H120" stroke="#9AA3B5" stroke-width="4" stroke-linecap="round"/>
<path d="M18 92 V100 M110 92 V100" stroke="#9AA3B5" stroke-width="4"/>
<path d="M22 88 Q20 54 50 50 Q66 34 92 44 Q112 54 106 88Z" fill="#FF8C6B" {s()}/>
<path d="M30 84 Q28 60 52 58 Q66 46 88 52 Q102 60 98 84" fill="none" stroke="#FFD0BF" stroke-width="4"/>
<path d="M40 82 Q38 66 56 66 M70 58 Q86 60 88 80" fill="none" stroke="#FFD0BF" stroke-width="3"/>
<path d="M36 56 L54 88 M56 46 L76 88 M78 44 L96 84" stroke="#6E2E1E" stroke-width="3.4" stroke-linecap="round" opacity=".85"/>
<path d="M66 64 Q66 52 74 46" fill="none" stroke="#FFFFFF" stroke-width="1"/>
{face(62, 72, d=10, k=0.8)}
<path d="M98 54 L110 18" stroke="#3E9B4A" stroke-width="3" stroke-linecap="round"/>
<path d="M108 24 l-8 -4 M107 30 l9 -2 M105 36 l-9 -4 M104 42 l9 -1 M110 18 l-4 -8 M110 18 l6 -6" stroke="#5CC05A" stroke-width="2.4" stroke-linecap="round"/>
<path d="M40 34 q-4 -8 2 -14 M84 30 q-4 -8 2 -14" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".7"/>
'''), "герой: стейк лосося с полосками от гриля | сцена: лежит на решётке над тлеющими углями и поднимает веточку укропа, как флажок")

# 11 Up Sushi Одинцово — темаки-рожок стоит в стаканчике-подставке, как букет
I["cafe-up-sushi-odintsovo"] = (svg2("#FFFBD6", "#F2C94C", f'''
<path d="M44 92 H84 L80 120 H48Z" fill="#E8F4FF" opacity=".9" {s()}/>
<path d="M48 100 H80" stroke="#9CC7E8" stroke-width="2"/>
<path d="M30 36 Q64 20 98 36 L66 106Z" fill="#1F3A2E" {s()}/>
<path d="M40 40 L64 92 L90 40" fill="none" stroke="#2E5444" stroke-width="2"/>
<path d="M28 36 Q30 16 50 18 Q64 8 80 18 Q100 16 100 36 Q64 46 28 36Z" fill="#FFFFFF" {s()}/>
<path d="M44 22 Q42 4 52 2 Q56 14 54 24Z" fill="#7BC86C" {s()}/>
<path d="M70 22 Q76 2 92 6 Q88 18 80 26Z" fill="#FF8A5B" {s()}/>
<path d="M76 10 l6 6 M82 8 l4 6" stroke="#FFD3BF" stroke-width="2"/>
{dots([(60,22),(64,18),(66,24),(58,26)],3,"#FF6A2A")}
{face(64, 58, d=9, k=0.8)}
'''), "герой: рожок темаки из нори с рисом, лососем и огурцом | сцена: стоит в прозрачном стаканчике-подставке, как букет цветов")

# 12 Mamma Italia — два птенчика-фрикадельки в гнезде из спагетти, вилка-мама несёт им базилик
I["cafe-mamma-italia-rekintso"] = (svg2("#ECFFE4", "#6FCF97", f'''
<path d="M16 86 Q64 128 112 86 Q100 74 64 76 Q28 74 16 86Z" fill="#F4D27A" {s()}/>
<path d="M22 88 Q40 80 60 90 Q80 78 104 88 M28 96 Q48 86 66 98 Q86 86 100 96 M38 104 Q56 96 76 106" fill="none" stroke="#E2B444" stroke-width="2.6"/>
<circle cx="50" cy="76" r="15" fill="#A0452B" {s()}/>
<circle cx="80" cy="74" r="15" fill="#A0452B" {s()}/>
<path d="M38 70 Q50 64 60 70 M68 68 Q80 62 92 68" fill="none" stroke="#E5484D" stroke-width="4" stroke-linecap="round"/>
{eye(45, 76, 0.6)}{eye(55, 76, 0.6)}{eye(75, 74, 0.6)}{eye(85, 74, 0.6)}
{omouth(50, 84, 0.8)}{omouth(80, 82, 0.8)}
<g transform="rotate(30 92 30)">
<rect x="88" y="20" width="8" height="40" rx="4" fill="#C9CED6" {s()}/>
<path d="M80 2 V18 Q80 24 92 24 Q104 24 104 18 V2" fill="none" stroke="{O}" stroke-width="3"/>
<path d="M86 2 V20 M92 2 V22 M98 2 V20" stroke="#C9CED6" stroke-width="3"/>
</g>
<path d="M62 40 Q70 28 82 34 Q74 46 62 40Z" fill="#3E9B4A" {s()}/>
<path d="M64 40 L80 34" stroke="#2C6E34" stroke-width="1.4"/>
'''), "герой: две фрикадельки-птенчика в томатном соусе | сцена: сидят в гнезде из спагетти и раскрыли рты, а вилка-мама несёт им листик базилика")

# 13 Vasilchuki Chaihona Vegas — гора плова с головкой чеснока, изюминка-альпинист с флажком
I["cafe-chaihona-vegas-kashirskoe"] = (svg2("#FFD9AE", "#B5543C", f'''
<circle cx="100" cy="30" r="12" fill="#FFE9A8" opacity=".9"/>
<ellipse cx="64" cy="108" rx="56" ry="12" fill="#2F7FC4" {s()}/>
<ellipse cx="64" cy="106" rx="46" ry="7" fill="#58A6E8"/>
<path d="M14 104 Q30 50 64 36 Q98 50 114 104Z" fill="#F2B544" {s()}/>
{dots([(36,90),(44,80),(56,70),(72,72),(84,84),(94,94),(62,92),(50,98),(78,98),(66,58)],2,"#FFE3A0")}
{dots([(40,96),(70,84),(88,92),(58,80)],2.6,"#E8743B")}
<path d="M52 38 Q50 22 64 20 Q78 22 76 38 Q64 46 52 38Z" fill="#FFF8F0" {s()}/>
<path d="M64 20 V40 M58 24 Q56 32 58 40 M70 24 Q72 32 70 40" stroke="#E6D6C8" stroke-width="2" fill="none"/>
<path d="M64 20 Q62 12 66 8" fill="none" stroke="#9BBF5A" stroke-width="3" stroke-linecap="round"/>
{face(64, 72, d=11, k=0.85)}
<g transform="rotate(-24 96 62)">
<ellipse cx="96" cy="66" rx="5" ry="7" fill="#4A2A4A" {W(1.6)}/>
<path d="M99 60 V44" stroke="{O}" stroke-width="2"/>
<path d="M99 44 L110 48 L99 52Z" fill="#E5484D" {W(1.4)}/>
</g>
'''), "герой: горка узбекского плова с целой головкой чеснока на вершине | сцена: изюминка-альпинист с красным флажком взбирается к чесночной макушке")

# 14 Vasilchuki Chaihona Красногорск — пиала шурпы с большой картофелиной, морковкой и паром
I["cafe-chaihona-krasnogorsk-lenina"] = (svg2("#DDE7FF", "#2F5BD3", f'''
<path d="M16 64 H112 Q110 110 64 112 Q18 110 16 64Z" fill="#FFFFFF" {s()}/>
<path d="M24 78 Q34 70 44 78 Q54 70 64 78 Q74 70 84 78 Q94 70 104 78" fill="none" stroke="#2F5BD3" stroke-width="3.4"/>
<path d="M30 92 l6 6 l6 -6 l6 6 l6 -6 l6 6 l6 -6 l6 6 l6 -6 l6 6 l6 -6" fill="none" stroke="#2F5BD3" stroke-width="2.4"/>
<ellipse cx="64" cy="64" rx="48" ry="11" fill="#E7A54A" {s()}/>
<ellipse cx="54" cy="60" rx="18" ry="11" fill="#F3D9A0" {s()}/>
{face(54, 58, d=6, k=0.6)}
<path d="M80 58 L104 62 L82 68Z" fill="#F07A2A" {W(2)}/>
<path d="M86 60 l2 6 M94 61 l1 4" stroke="#C25418" stroke-width="1.6"/>
<circle cx="34" cy="64" r="4" fill="#3E9B4A"/><circle cx="76" cy="70" r="3" fill="#3E9B4A"/>
<path d="M44 44 q-6 -10 2 -18 q8 -8 0 -18 M64 40 q-6 -10 2 -18 q8 -8 0 -18 M84 44 q-6 -10 2 -18 q8 -8 0 -18" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>
'''), "герой: картофелина в горячей шурпе с морковкой | сцена: отдыхает в бело-синей узбекской пиале, а над ней в три струйки поднимается пар")

# 15 Без сахара — баночка чиа-пудинга, черничка выглядывает из-под крышки
I["cafe-bez-sahara-domodedovo"] = (svg2("#F5ECFF", "#B892E8", f'''
<rect x="30" y="38" width="68" height="78" rx="12" fill="#EAF6FF" opacity=".95" {s()}/>
<path d="M32 80 H96 V104 Q96 114 86 114 H42 Q32 114 32 104Z" fill="#F7F0E6"/>
{dots([(40,88),(48,96),(58,90),(68,100),(80,92),(88,104),(52,106),(74,108),(44,100),(84,86)],1.4,"#3B3355")}
<path d="M32 64 H96 V80 H32Z" fill="#F07A9A"/>
<path d="M32 64 Q48 70 64 64 Q80 70 96 64" fill="none" stroke="#C94A70" stroke-width="2"/>
<rect x="30" y="38" width="68" height="78" rx="12" fill="none" {s()}/>
{face(64, 92, d=10, k=0.8)}
<g transform="rotate(-18 64 34)">
<rect x="24" y="26" width="80" height="14" rx="5" fill="#9B6BD8" {s()}/>
</g>
<circle cx="88" cy="40" r="8" fill="#4A4FA8" {s()}/>
<path d="M86 34 l2 -3 l2 3" fill="none" stroke="#2A2E70" stroke-width="1.6"/>
{eye(86, 41, 0.45)}{eye(91, 41, 0.45)}
<path d="M98 22 q4 -6 8 0 M104 30 q4 -4 6 2" fill="none" stroke="#fff" stroke-width="2"/>
'''), "герой: стеклянная баночка чиа-пудинга с ягодным слоем | сцена: черничка приподняла крышку изнутри и с любопытством выглядывает наружу")

# 16 ЖАРъ — курица-гриль крутится на вертеле над языками пламени, зажмурившись
I["cafe-zhar-egorevsk"] = (svg2("#7A2E14", "#2A0F08", f'''
<path d="M14 128 Q20 100 30 112 Q34 90 46 108 Q52 86 64 106 Q76 86 82 108 Q94 90 98 112 Q108 100 114 128Z" fill="#F2762E"/>
<path d="M30 128 Q36 110 44 118 Q52 102 64 116 Q76 102 84 118 Q92 110 98 128Z" fill="#FFC14D"/>
<path d="M14 30 V100 M114 30 V100" stroke="#5A4A4A" stroke-width="5" stroke-linecap="round"/>
<path d="M4 56 H124" stroke="#C9CED6" stroke-width="4" stroke-linecap="round"/>
<circle cx="118" cy="56" r="6" fill="#C9CED6" {s()}/>
<path d="M118 50 V40" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<path d="M28 58 Q26 30 64 28 Q102 30 100 58 Q98 88 64 90 Q30 88 28 58Z" fill="#D9782E" {s()}/>
<path d="M36 50 Q50 36 70 38" fill="none" stroke="#F2B060" stroke-width="4" stroke-linecap="round"/>
<path d="M24 74 Q14 80 20 90 Q28 92 34 82 M104 74 Q114 80 108 90 Q100 92 94 82" fill="#D9782E" {s()}/>
<circle cx="18" cy="92" r="4" fill="#FFFFFF" {W(1.6)}/><circle cx="110" cy="92" r="4" fill="#FFFFFF" {W(1.6)}/>
{closed(64, 64, d=10, k=0.9)}
<path d="M58 74 Q64 80 70 74" fill="none" {W(2.4)}/>
<path d="M10 40 q4 -6 0 -12 M110 22 q4 -6 0 -12" stroke="#FFC14D" stroke-width="2" fill="none" opacity=".7"/>
'''), "герой: румяная курица-гриль | сцена: зажмурившись от удовольствия, крутится на вертеле над языками пламени")

# 17 Алькасар — шаурма выглядывает из бойницы зубчатой башни
I["cafe-alkasar-egorevsk"] = (svg2("#E3F3FF", "#86C5F0", f'''
<path d="M0 116 Q64 104 128 116 V128 H0Z" fill="#8CCB6E"/>
<path d="M28 120 V40 H38 V30 H50 V40 H60 V30 H72 V40 H82 V30 H94 V40 H100 V120Z" fill="#E9C48C" {s()}/>
<path d="M28 60 H100 M28 84 H100 M48 60 V84 M76 60 V84 M40 84 V120 M88 84 V120 M60 40 V60" stroke="#C99E62" stroke-width="2"/>
<rect x="46" y="48" width="36" height="54" rx="18" fill="#5A3A2A" {s()}/>
<g transform="rotate(-8 64 74)">
<path d="M48 108 L52 56 Q64 44 76 56 L80 108Z" fill="#FFFFFF" {s()}/>
<path d="M50 60 Q64 52 78 60 L78 70 Q64 64 50 70Z" fill="#F2D29A" {W(1.6)}/>
<path d="M54 58 l4 -6 M64 56 l2 -8 M72 58 l4 -6" stroke="#3E9B4A" stroke-width="3" stroke-linecap="round"/>
<path d="M58 54 l2 -4 M68 54 l2 -4" stroke="#E5484D" stroke-width="3" stroke-linecap="round"/>
<path d="M50 96 H78" stroke="#E5484D" stroke-width="3"/>
{face(64, 80, d=8, k=0.75)}
</g>
<path d="M44 18 V30 M44 18 L56 22 L44 26" fill="#E5484D" {W(1.6)}/>
'''), "герой: шаурма в белой бумажной обёртке с зеленью сверху | сцена: выглядывает из арки-бойницы зубчатой песочной крепостной башни")

# 18 Бунькофф — ржаная буханка выглядывает из бумажного пакета с ручками
I["cafe-bunkoff-elektrostal"] = (svg2("#FFF1E3", "#D4A373", f'''
<path d="M30 52 Q30 20 56 22 Q66 6 82 18 Q100 20 98 52Z" fill="#7A4A2A" {s()}/>
<path d="M44 34 L52 26 M62 30 L70 20 M78 32 L86 24" stroke="#4A2A14" stroke-width="3" stroke-linecap="round"/>
{dots([(48,44),(60,40),(74,44),(86,40),(56,48),(80,48)],1.6,"#E8C99A")}
{face(64, 40, d=10, k=0.8)}
<path d="M24 52 H104 L98 120 H30Z" fill="#E2B57A" {s()}/>
<path d="M24 52 L30 62 L36 52 L42 62 L48 52 L54 62 L60 52 L66 62 L72 52 L78 62 L84 52 L90 62 L96 52 L102 62 L104 52" fill="#E2B57A" {W(2)}/>
<path d="M44 52 Q44 40 52 40 M84 52 Q84 40 76 40" fill="none" stroke="#B5844A" stroke-width="3"/>
<rect x="46" y="80" width="36" height="22" rx="4" fill="#FFF6E8" {W(2)}/>
<path d="M52 88 H76 M52 94 H70" stroke="#B5844A" stroke-width="2"/>
'''), "герой: тёмная ржаная буханка-кирпичик с надрезами и тмином | сцена: выглядывает из бумажного крафт-пакета с ручками, как из окошка")

# 19 Solo — нью-йоркский чизкейк поёт соло в луче прожектора, микрофон-ложечка
I["cafe-solo-fryazino"] = (svg2("#3A2C66", "#110A24", f'''
<path d="M44 0 L84 0 L118 112 L10 112Z" fill="#FFF3B0" opacity=".28"/>
<ellipse cx="64" cy="112" rx="50" ry="10" fill="#FFF3B0" opacity=".35"/>
<path d="M0 112 H128 V128 H0Z" fill="#7A3A8A"/>
<path d="M22 104 L22 70 L100 50 L106 104Z" fill="#FFF0C8" {s()}/>
<path d="M22 70 L100 50 L106 60 L22 82Z" fill="#E9C27A"/>
<path d="M22 96 L106 96 L106 104 L22 104Z" fill="#C98A4A" {W(2)}/>
<path d="M22 70 Q40 62 60 66 Q80 56 100 50 L102 58 Q86 62 76 70 Q72 80 66 70 Q50 70 40 76 Q36 86 32 76 Q26 76 22 78Z" fill="#E5484D" {s()}/>
{face(62, 84, d=10, k=0.8)}
<ellipse cx="62" cy="96" rx="4" ry="3" fill="#C0392B"/>
<g transform="rotate(-30 92 80)">
<rect x="89" y="74" width="6" height="30" rx="3" fill="#C9CED6" {s()}/>
<ellipse cx="92" cy="72" rx="7" ry="8" fill="#C9CED6" {s()}/>
</g>
<path d="M14 40 q4 -8 10 -2 M20 26 v12 M104 30 q4 -8 10 -2 M110 16 v14" fill="none" stroke="#FFD45E" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="20" cy="38" r="3.5" fill="#FFD45E"/><circle cx="110" cy="30" r="3.5" fill="#FFD45E"/>
'''), "герой: треугольный кусок нью-йоркского чизкейка с клубничным топпингом | сцена: поёт соло в луче прожектора, держа ложечку как микрофон")

# 20 Samarkand — детская игровая: горка с бирюзовым куполом, малыш выглядывает из окошка, мячик скатывается
I["cafe-samarkand-ivanteevka"] = (svg2("#FFEADC", "#F08C6E", f'''
<path d="M0 112 H128 V128 H0Z" fill="#B85A3E"/>
{dots([(14,108),(24,112),(34,108),(104,108),(114,112),(120,106)],5,"#FFD45E")}
{dots([(20,104),(110,104)],5,"#5CC0E8")}
<rect x="30" y="58" width="44" height="54" fill="#FFF4E0" {s()}/>
<path d="M30 76 H74 M30 94 H74" stroke="#2BA4B8" stroke-width="3"/>
<path d="M26 58 Q26 22 52 18 Q78 22 78 58Z" fill="#2BB3C8" {s()}/>
<path d="M36 40 Q52 30 68 40 M32 52 Q52 44 72 52" fill="none" stroke="#7FE0EC" stroke-width="2.4"/>
<path d="M52 18 V8" stroke="{O}" stroke-width="2.4"/><circle cx="52" cy="7" r="3" fill="#FFD45E" {W(1.6)}/>
<rect x="42" y="62" width="20" height="24" rx="10" fill="#5A3A2A" {s()}/>
<circle cx="52" cy="74" r="8" fill="#FFD9B8" {W(2)}/>
<path d="M44 70 Q52 62 60 70" fill="#E5484D" {W(1.6)}/>
{eye(49, 75, 0.45)}{eye(55, 75, 0.45)}
<path d="M74 66 Q100 76 108 108 L96 110 Q90 84 74 80Z" fill="#FFB238" {s()}/>
<circle cx="96" cy="84" r="6" fill="#E5484D" {W(2)}/>
<path d="M86 76 q4 -4 8 -2" fill="none" stroke="#fff" stroke-width="2"/>
'''), "герой: игровой домик-лабиринт с бирюзовым узорным куполом и жёлтой горкой | сцена: малыш выглядывает из арочного окошка, а по горке катится красный мячик в сухой бассейн")

# 21 Чашка — капучино сверху: на пенке латте-арт мишка
I["cafe-chashka-kashira"] = (svg2("#F6E6D2", "#A0673E", f'''
<ellipse cx="66" cy="68" rx="54" ry="54" fill="#FFFFFF" {s()}/>
<path d="M112 46 Q130 52 124 74 Q118 86 108 82" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M112 46 Q130 52 124 74 Q118 86 108 82" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
<circle cx="64" cy="66" r="38" fill="#FFFFFF" {s()}/>
<circle cx="64" cy="66" r="34" fill="#B5753E"/>
<circle cx="64" cy="66" r="34" fill="none" stroke="#8A5228" stroke-width="3"/>
<circle cx="46" cy="50" r="8" fill="#FFF3E2"/><circle cx="82" cy="50" r="8" fill="#FFF3E2"/>
<ellipse cx="64" cy="70" rx="22" ry="19" fill="#FFF3E2"/>
<ellipse cx="64" cy="78" rx="7" ry="5" fill="#E9CBA8"/>
<circle cx="64" cy="76" r="2.4" fill="#5A3218"/>
<circle cx="56" cy="66" r="2.6" fill="#5A3218"/><circle cx="72" cy="66" r="2.6" fill="#5A3218"/>
<path d="M60 82 Q64 85 68 82" fill="none" stroke="#5A3218" stroke-width="1.6"/>
{sparkle(104, 108, 5)}
'''), "герой: чашка капучино, вид сверху | сцена: на молочной пенке нарисована мордочка медвежонка, который улыбается тому, кто заглянул в чашку")

# 22 Блинвуд — блин-звезда на «аллее славы» под двумя прожекторами
I["cafe-blinwood-klin"] = (svg2("#5B3FA8", "#21144A", f'''
<path d="M10 0 L40 0 L76 92 L54 96Z" fill="#FFF3B0" opacity=".22"/>
<path d="M118 0 L88 0 L52 92 L74 96Z" fill="#FFF3B0" opacity=".22"/>
<path d="M0 88 L128 82 V128 H0Z" fill="#8E8A9C"/>
<path d="M0 104 L128 100 M42 86 L38 128 M86 84 L90 128" stroke="#6E6A7C" stroke-width="2.4"/>
<path d="M64 46 L74 66 L96 68 L80 82 L86 104 L64 92 L42 104 L48 82 L32 68 L54 66Z" fill="#F2B755" {s()}/>
<path d="M64 54 L71 68 L86 70 L75 80 L79 96 L64 88 L49 96 L53 80 L42 70 L57 68Z" fill="#F7CD7A"/>
{dots([(58,62),(72,84),(52,86),(78,72)],2,"#D9913A")}
{face(64, 78, d=7, k=0.7)}
<rect x="8" y="10" width="14" height="10" rx="3" fill="#3B3355" {s()} transform="rotate(30 15 15)"/>
<rect x="106" y="10" width="14" height="10" rx="3" fill="#3B3355" {s()} transform="rotate(-30 113 15)"/>
{sparkle(30, 40, 4)}{sparkle(100, 46, 5)}{sparkle(18, 70, 3)}
'''), "герой: румяный блин в форме пятиконечной звезды | сцена: лежит на звёздной аллее славы, а на него светят два скрещённых прожектора")

# 23 Пицца Пацца — кусок пиццы держат как зонтик над маслинкой под дождём
I["cafe-pizza-pazza-kolomna"] = (svg2("#E2EAF4", "#7E92AE", f'''
{''.join(f'<path d="M{x} {y} l-4 10" stroke="#4E6FA0" stroke-width="2.4" stroke-linecap="round"/>' for x, y in [(14,20),(30,8),(104,14),(118,34),(12,52),(112,62),(22,84),(116,90),(94,6),(40,24)])}
<path d="M0 116 Q64 106 128 116 V128 H0Z" fill="#9FB2C8"/>
<ellipse cx="80" cy="116" rx="14" ry="3" fill="#7E92AE"/>
<path d="M20 54 Q64 14 108 54 Q64 46 20 54Z" fill="#E9B062" {s()}/>
<path d="M26 52 Q64 22 102 52 Q64 46 26 52Z" fill="#FFD45E"/>
{dots([(44,42),(64,34),(84,42),(56,48)],5,"#D9432F")}
{dots([(74,46),(50,36)],2.4,"#3E9B4A")}
<path d="M20 54 Q64 46 108 54" fill="none" {s()}/>
<path d="M64 46 V96" stroke="{O}" stroke-width="3"/>
<path d="M64 96 Q64 104 58 104" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="74" cy="86" rx="14" ry="17" fill="#2E2A3A" {s()}/>
<ellipse cx="74" cy="80" rx="5" ry="3" fill="#56506A"/>
{eye(68, 86, 0.55)}{eye(80, 86, 0.55)}
<path d="M70 94 Q74 97 78 94" fill="none" stroke="#fff" stroke-width="1.6"/>
<path d="M60 84 Q64 80 66 86" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
'''), "герой: треугольный кусок пиццы пепперони | сцена: служит зонтиком маленькой маслинке, которая прячется под ним от дождя")

# 24 Strawbusta — три клубнички в шоколаде стоят в бумажном кульке-букете
I["cafe-strawbusta-naro-fominsk"] = (svg2("#E2FBFF", "#38B6D4", f'''
<g transform="rotate(-20 40 50)">
<path d="M28 24 Q40 14 52 24 Q56 50 40 66 Q24 50 28 24Z" fill="#E5384D" {s()}/>
<path d="M28 40 Q40 48 54 40 Q54 54 40 66 Q26 54 28 40Z" fill="#6B3A22" {W(2)}/>
<path d="M30 22 L36 14 L40 22 L44 14 L50 22" fill="#3E9B4A" {W(1.6)}/>
<path d="M40 66 V96" stroke="#E8D3A8" stroke-width="3"/>
</g>
<g transform="rotate(18 88 50)">
<path d="M76 24 Q88 14 100 24 Q104 50 88 66 Q72 50 76 24Z" fill="#E5384D" {s()}/>
<path d="M76 42 Q88 50 102 42 Q102 54 88 66 Q74 54 76 42Z" fill="#F5F0E6" {W(2)}/>
<path d="M80 50 l4 4 M92 52 l4 -4" stroke="#F07A9A" stroke-width="2"/>
<path d="M78 22 L84 14 L88 22 L92 14 L98 22" fill="#3E9B4A" {W(1.6)}/>
<path d="M88 66 V96" stroke="#E8D3A8" stroke-width="3"/>
</g>
<path d="M50 30 Q64 18 78 30 Q82 58 64 76 Q46 58 50 30Z" fill="#E5384D" {s()}/>
<path d="M50 48 Q64 56 80 48 Q78 64 64 76 Q50 64 50 48Z" fill="#6B3A22" {W(2)}/>
{dots([(58,40),(70,38),(64,30)],1.4,"#FFE08A")}
<path d="M52 28 L58 18 L64 28 L70 18 L76 28" fill="#3E9B4A" {W(1.6)}/>
{face(64, 42, d=6, k=0.55)}
<path d="M30 70 L98 70 L68 122 L60 122Z" fill="#F3D9A8" {s()}/>
<path d="M30 70 L64 96 L98 70" fill="none" stroke="#D9B47A" stroke-width="2.4"/>
<path d="M54 98 Q64 92 74 98 L70 104 Q64 100 58 104Z" fill="#E5484D" {W(1.6)}/>
'''), "герой: клубника, наполовину окунутая в шоколад | сцена: стоит с двумя сестрёнками на шпажках в бумажном кульке, как в букете")

# 25 Машенькины пироги — стопка из трёх осетинских пирогов, верхний подмигивает
I["cafe-mashenkiny-pirogi-odintsovo"] = (svg2("#E2F2F6", "#3C7F94", f'''
<ellipse cx="64" cy="112" rx="50" ry="8" fill="#245566" opacity=".35"/>
<ellipse cx="64" cy="100" rx="48" ry="13" fill="#D99A4E" {s()}/>
<ellipse cx="64" cy="84" rx="46" ry="13" fill="#E3A85C" {s()}/>
<ellipse cx="64" cy="66" rx="44" ry="18" fill="#EDB86A" {s()}/>
<ellipse cx="64" cy="62" rx="34" ry="11" fill="#F6CF8A"/>
<path d="M64 56 V66 M58 61 H70" stroke="#C8843C" stroke-width="2.6" stroke-linecap="round"/>
{eye(52, 70, 0.7)}
<path d="M72 70 Q76 66 80 70" fill="none" {W(2.4)}/>
<path d="M58 77 Q64 82 70 77" fill="none" {W(2.4)}/>
<ellipse cx="44" cy="76" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="86" cy="76" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
<path d="M44 34 q-4 -8 2 -14 M64 30 q-4 -8 2 -14 M84 34 q-4 -8 2 -14" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round"/>
<path d="M30 94 Q40 98 50 94 M78 110 Q88 112 98 108" fill="none" stroke="#B87A34" stroke-width="2"/>
'''), "герой: стопка из трёх круглых осетинских пирогов с крестиком на верхнем | сцена: верхний пирог подмигивает, а над стопкой поднимаются три струйки пара")

# 26 ОтVинта — куриное крылышко-лётчик в шлеме и очках взлетает с соусницы-аэродрома
I["cafe-otvinta-podolsk"] = (svg2("#FFF4C8", "#F5A623", f'''
<path d="M4 102 Q30 92 44 104" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="6 6" stroke-linecap="round"/>
<ellipse cx="26" cy="112" rx="24" ry="9" fill="#E5484D" {s()}/>
<ellipse cx="26" cy="109" rx="18" ry="5" fill="#F07A55"/>
<g transform="rotate(-28 72 64)">
<path d="M34 72 Q34 50 62 48 Q86 44 100 54 Q110 62 100 74 Q86 86 62 82 Q36 86 34 72Z" fill="#D9782E" {s()}/>
<path d="M44 66 Q60 58 80 60" fill="none" stroke="#F2B060" stroke-width="4" stroke-linecap="round"/>
<path d="M62 48 Q66 34 82 36 Q96 38 98 52 Q84 46 62 48Z" fill="#7A4A2A" {s()}/>
<rect x="66" y="50" width="28" height="10" rx="5" fill="#5A3A2A" {W(2)}/>
<circle cx="74" cy="55" r="5" fill="#9ED8F5" {W(2)}/><circle cx="88" cy="55" r="5" fill="#9ED8F5" {W(2)}/>
<path d="M76 68 Q82 72 88 68" fill="none" {W(2.4)}/>
<path d="M60 52 Q48 40 40 44" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
</g>
<g transform="translate(106 26)">
<circle r="4" fill="#3B3355"/>
<path d="M0 0 L-4 -16 L4 -16Z M0 0 L14 6 L12 12Z M0 0 L-12 10 L-16 4Z" fill="#C9CED6" {W(1.6)}/>
</g>
{sparkle(30, 30, 5)}
'''), "герой: куриное крылышко-лётчик в кожаном шлеме и очках | сцена: взлетает с красной соусницы, как с аэродрома, а рядом крутится пропеллер")

# 27 Вкусняшка Руза — торт «Муравейник» горкой, шоколадный муравьишка карабкается на вершину
I["cafe-vkusnyashka-ruza"] = (svg2("#EEF9E6", "#8CC97A", f'''
<ellipse cx="64" cy="110" rx="52" ry="10" fill="#FFFFFF" {s()}/>
<path d="M18 106 Q28 54 64 34 Q100 54 110 106Z" fill="#C98A4A" {s()}/>
{''.join(f'<rect x="{x}" y="{y}" width="9" height="5" rx="2" fill="#E2B070" stroke="{O}" stroke-width="1.4" transform="rotate({r} {x} {y})"/>' for x, y, r in [(34,90,-20),(50,96,15),(70,92,-10),(88,94,25),(42,74,10),(60,70,-25),(78,76,20),(54,54,10),(70,56,-15)])}
<path d="M34 92 Q46 84 56 94 M72 84 Q84 78 94 90" fill="none" stroke="#5A3218" stroke-width="3" stroke-linecap="round"/>
{dots([(40,82),(66,82),(86,82),(56,64),(74,66),(62,46),(48,98),(80,100)],1.6,"#3B2A1A")}
{face(64, 84, d=10, k=0.8)}
<g transform="rotate(30 80 40)">
<ellipse cx="74" cy="40" rx="4" ry="3.4" fill="#4A2A14" {W(1.4)}/>
<ellipse cx="81" cy="40" rx="4" ry="3.4" fill="#4A2A14" {W(1.4)}/>
<circle cx="88" cy="39" r="4" fill="#4A2A14" {W(1.4)}/>
<path d="M90 35 l3 -5 M87 35 l0 -6 M74 43 l-3 5 M80 43 v6 M84 43 l3 5" stroke="{O}" stroke-width="1.4" stroke-linecap="round"/>
<circle cx="89" cy="38" r="1" fill="#fff"/>
</g>
'''), "герой: торт «Муравейник» горкой с кусочками печенья | сцена: на его вершину карабкается маленький шоколадный муравьишка")

# 28 Всё своё — пирожки-близнецы выглядывают из-под вышитого полотенца на деревянной доске
I["cafe-vsyo-svoyo-aprelevka"] = (svg2("#FFF4EC", "#D9534F", f'''
<rect x="10" y="88" width="108" height="22" rx="6" fill="#B8783E" {s()}/>
<path d="M18 96 H110 M18 102 H110" stroke="#9A5E2A" stroke-width="1.6"/>
<path d="M22 84 Q22 56 46 56 Q66 56 66 84Z" fill="#E9A24E" {s()}/>
<path d="M62 84 Q62 56 84 56 Q106 56 106 84Z" fill="#E9A24E" {s()}/>
<path d="M30 60 Q44 52 58 60 M70 60 Q84 52 98 60" fill="none" stroke="#B86E28" stroke-width="2.6"/>
{face(44, 72, d=6, k=0.6)}{face(84, 72, d=6, k=0.6)}
<path d="M4 64 Q30 30 64 34 Q98 30 124 64 L124 54 Q98 22 64 26 Q30 22 4 54Z" fill="#FFFFFF" {s()}/>
<path d="M14 54 Q40 34 64 36 Q88 34 114 54" fill="none" stroke="#E5484D" stroke-width="3" stroke-dasharray="4 4"/>
<path d="M20 60 l4 -6 l4 6 M100 60 l4 -6 l4 6 M60 32 l4 -6 l4 6" fill="none" stroke="#E5484D" stroke-width="2.4"/>
<path d="M4 54 L0 70 M124 54 L128 70" stroke="#E5484D" stroke-width="3"/>
'''), "герой: два румяных домашних пирожка-близнеца | сцена: выглядывают из-под белого полотенца с красной вышивкой на деревянной доске")

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
