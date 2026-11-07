"""Робот cafes, 2026-11-07 (16 UTC): иконки 39 новых кафе. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя компоновка и палитра фона).
Запуск из корня: python3 tools/icons_cafes_1107h.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
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

# 1 Навруз — росток пшеницы (сумаляк) в узорной пиале тянется к весеннему солнцу
I["cafe-navruz-klin"] = (svg2("#F4FFE0", "#9BD86A", f'''
<circle cx="100" cy="28" r="12" fill="#FFD84A" {s()}/>
<path d="M100 8 V12 M118 28 H114 M113 15 L110 18 M87 15 L90 18" {W(2.6)}/>
<path d="M64 74 Q58 52 46 40 M64 74 Q66 46 62 26 M64 74 Q72 50 86 40" fill="none" stroke="#3E9E3A" stroke-width="5" stroke-linecap="round"/>
<path d="M46 40 Q38 34 40 26 Q50 30 46 40Z M62 26 Q58 16 64 10 Q70 18 62 26Z M86 40 Q96 36 96 28 Q86 28 86 40Z" fill="#7BD35A" {W(2.4)}/>
<path d="M26 72 H102 Q100 108 64 110 Q28 108 26 72Z" fill="#2F7FD0" {s()}/>
<path d="M30 80 H98" stroke="#fff" stroke-width="3"/>
<g fill="#fff">{''.join(f'<path d="M{x} 90 l5 -5 l5 5 l-5 5Z"/>' for x in (36, 54, 72, 88))}</g>
<ellipse cx="64" cy="72" rx="38" ry="7" fill="#8CD46A" {s()}/>
{face(64, 98, d=12, k=0.8)}
'''), "герой: зелёный росток пшеницы-сумаляк в синей узорной пиале | сцена: тянет листочки к весеннему солнцу на празднике Навруз")

# 2 Маленький Токио — белая кошка манэки-нэко машет лапкой с красной лакированной подставки
I["cafe-malenkiy-tokio-klin"] = (svg2("#FFE3E3", "#E5484D", f'''
<rect x="22" y="96" width="84" height="18" rx="4" fill="#B3262B" {s()}/>
<path d="M28 104 H100" stroke="#F2C14E" stroke-width="2.4"/>
<ellipse cx="64" cy="80" rx="30" ry="20" fill="#FFFFFF" {s()}/>
<path d="M86 66 Q104 52 98 36" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round"/>
<path d="M86 66 Q104 52 98 36" fill="none" stroke="#FFFFFF" stroke-width="9" stroke-linecap="round"/>
<ellipse cx="96" cy="34" rx="8" ry="9" fill="#fff" {s()}/>
<path d="M92 30 v6 M96 29 v7 M100 30 v6" {W(1.8)}/>
<circle cx="64" cy="54" r="26" fill="#FFFFFF" {s()}/>
<path d="M42 40 L44 20 L58 32Z M86 40 L84 20 L70 32Z" fill="#fff" {s()}/>
<path d="M47 34 L48 25 L54 31Z M81 34 L80 25 L74 31Z" fill="#FF9FB5"/>
<circle cx="78" cy="40" r="5" fill="#FF9A3C"/><circle cx="50" cy="66" r="4" fill="#3B3355" opacity=".85"/>
{face(64, 54, d=10, k=0.95)}
<path d="M40 72 Q64 82 88 72" fill="none" stroke="#E5484D" stroke-width="5"/>
<circle cx="64" cy="82" r="5" fill="#FFD43A" {W(2.2)}/>
'''), "герой: белая кошка манэки-нэко с колокольчиком | сцена: машет поднятой лапкой гостям с красной лакированной подставки")

# 3 Провинция — малосольный огурчик в вышиванке пляшет вприсядку на деревянной лавке
I["cafe-provintsiya-klin"] = (svg2("#FFF8E6", "#E6B86A", f'''
<rect x="10" y="98" width="108" height="10" rx="3" fill="#B07A45" {s()}/>
<path d="M24 108 V124 M104 108 V124" stroke="#8A5A33" stroke-width="7" stroke-linecap="round"/>
<path d="M44 92 L30 98 M84 92 L98 98" stroke="#3B8F3A" stroke-width="7" stroke-linecap="round"/>
<ellipse cx="64" cy="58" rx="22" ry="36" fill="#5DBA4C" {s()}/>
<g fill="#3B8F3A">{dots([(52,30),(74,34),(48,48),(80,52),(54,86),(76,84)],2.4,'#3B8F3A')}</g>
<path d="M44 64 H84 L82 84 Q64 92 46 84Z" fill="#FFFFFF" {s()}/>
<path d="M50 70 l4 4 l4 -4 l4 4 l4 -4 l4 4 l4 -4 l4 4" fill="none" stroke="#D83A3A" stroke-width="2.4"/>
<path d="M42 66 Q26 56 30 42 M86 66 Q102 56 98 42" fill="none" stroke="#5DBA4C" stroke-width="7" stroke-linecap="round"/>
{face(64, 46, d=9, k=0.85)}
<path d="M22 30 q4 -6 8 0 M104 24 q4 -6 8 0" fill="none" {W(2)}/>
'''), "герой: малосольный огурчик в белой вышиванке | сцена: пляшет вприсядку, раскинув руки, на деревянной лавке")

# 4 Бэп Вьет — багет банх-ми с кинзой подмигивает на красной табуретке
I["cafe-bep-viet-klin"] = (svg2("#E8FFF6", "#38B58A", f'''
<rect x="38" y="84" width="52" height="8" rx="3" fill="#E5373D" {s()}/>
<path d="M44 92 L38 122 M84 92 L90 122 M48 108 H80" stroke="#E5373D" stroke-width="6" stroke-linecap="round"/>
<path d="M44 92 L38 122 M84 92 L90 122" fill="none" {W(2)} opacity=".5"/>
<path d="M14 66 Q16 40 64 38 Q112 40 114 66 Q112 84 64 84 Q16 84 14 66Z" fill="#F2B45A" {s()}/>
<path d="M18 62 Q64 72 110 62 L110 70 Q64 80 18 70Z" fill="#F7E3B5"/>
<path d="M22 64 l6 -6 l6 6 l6 -6 l6 6 M76 64 l6 -6 l6 6 l6 -6 l6 6" fill="#58C25A" {W(2)}/>
<circle cx="56" cy="66" r="4" fill="#E5534B"/><circle cx="70" cy="68" r="4" fill="#E5534B"/>
<path d="M36 46 l8 -4 M58 42 l8 -2 M80 44 l8 2" {W(2.2)}/>
{eye(52, 52, 0.8)}<path d="M72 52 Q76 48 80 52" fill="none" {W(2.4)}/>
<path d="M60 58 Q66 62 72 58" fill="none" {W(2.4)}/>
'''), "герой: вьетнамский багет банх-ми с кинзой и редисом | сцена: подмигивает, развалившись на красной уличной табуретке")

# 5 Гранд кафе ЧайковскиЙ — эклер-дирижёр взмахивает палочкой среди кружащихся нот
I["cafe-grand-chaikovsky-klin"] = (svg2("#F1E6FF", "#6E4FC8", f'''
<path d="M30 30 q0 -10 6 -10 v14 M98 22 q0 -10 6 -10 v14 M96 86 q0 -10 6 -10 v14" fill="none" {W(2.6)}/>
<ellipse cx="34" cy="34" rx="5" ry="4" fill="{O}"/><ellipse cx="102" cy="26" rx="5" ry="4" fill="{O}"/><ellipse cx="100" cy="90" rx="5" ry="4" fill="{O}"/>
<path d="M32 110 Q30 52 64 46 Q98 52 96 110Z" fill="#F7D79C" {s()}/>
<path d="M30 68 Q30 46 64 42 Q98 46 98 68 Q64 76 30 68Z" fill="#5A3420" {s()}/>
<path d="M50 52 Q60 48 70 50" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<path d="M54 92 L64 98 L74 92 L74 104 L64 98 L54 104Z" fill="#3B3355"/>
{face(64, 82, d=10, k=0.85)}
<path d="M90 82 L112 52" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M90 82 L112 52" fill="none" {W(1.6)}/>
<circle cx="90" cy="84" r="5" fill="#F7D79C" {W(2.2)}/>
'''), "герой: шоколадный эклер-дирижёр с бабочкой | сцена: взмахивает палочкой, а вокруг кружатся ноты")

# 6 Снежная Королева — меренга-безе-принцесса катится на серебряных санях по снежному склону
I["cafe-snezhnaya-koroleva-klin"] = (svg2("#F2FBFF", "#7FB6E8", f'''
<path d="M0 92 Q60 70 128 104 V128 H0Z" fill="#FFFFFF" {s()}/>
<path d="M30 92 Q58 98 92 92 Q100 92 102 84" fill="none" stroke="#B8C6D8" stroke-width="5" stroke-linecap="round"/>
<path d="M30 92 Q58 98 92 92 Q100 92 102 84" fill="none" {W(2)}/>
<path d="M36 88 V80 M84 88 V80" {W(2.6)}/>
<path d="M30 80 H90 Q96 64 82 62 H38 Q28 66 30 80Z" fill="#C9D3E2" {s()}/>
<path d="M44 64 Q40 44 52 36 Q50 26 60 24 Q62 14 72 20 Q82 22 78 34 Q88 40 80 54 Q78 64 44 64Z" fill="#FFFFFF" {s()}/>
<path d="M56 24 L58 14 L64 20 L70 12 L72 22" fill="#BEE6FF" {W(2.2)}/>
{face(62, 46, d=8, k=0.8)}
{sparkle(20, 40, 6)}{sparkle(108, 46, 5)}{sparkle(98, 22, 4)}
'''), "герой: меренга-безе с ледяной короной | сцена: катится на серебряных санях по снежному склону")

# 7 Иль Соле Иль Мондо — спагетти-глобус, над которым восходит помидорное солнце
I["cafe-il-sole-solnechnogorsk"] = (svg2("#FFF3E0", "#FF8A4C", f'''
<circle cx="64" cy="30" r="16" fill="#F2453D" {s()}/>
<path d="M58 16 L64 10 L70 16 L64 18Z" fill="#4CAF50" {W(2)}/>
<path d="M40 22 L32 18 M88 22 L96 18 M38 36 L28 38 M90 36 L100 38" stroke="#FFE07A" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="64" cy="114" rx="46" ry="8" fill="#FFFFFF" {s()}/>
<circle cx="64" cy="78" r="32" fill="#FFD36B" {s()}/>
<path d="M64 46 Q44 78 64 110 Q84 78 64 46 M34 70 Q64 80 94 70 M36 90 Q64 98 92 90 M40 58 Q64 64 88 58" fill="none" stroke="#E8A93A" stroke-width="2.6"/>
<path d="M44 62 Q50 56 58 60 L56 70 Q48 70 44 62Z M72 84 Q82 80 86 88 Q80 96 72 92Z" fill="#6FBF4A" {W(2)}/>
{face(64, 80, d=11, k=0.85)}
'''), "герой: тарелка спагетти в виде земного шара с материками-базиликом | сцена: над ней восходит помидорное солнце")

# 8 Монпансье — круглая жестяная баночка леденцов, крышка приоткрылась и леденцы выпрыгивают
I["cafe-monpansie-solnechnogorsk"] = (svg2("#FFF0F7", "#F06BA8", f'''
<ellipse cx="64" cy="106" rx="40" ry="10" fill="#C8E8F7" {s()}/>
<path d="M24 76 V104 Q64 120 104 104 V76Z" fill="#7FD3F0" {s()}/>
<ellipse cx="64" cy="76" rx="40" ry="10" fill="#B9EAFA" {s()}/>
<path d="M32 90 Q64 98 96 90" fill="none" stroke="#fff" stroke-width="3"/>
<ellipse cx="78" cy="52" rx="40" ry="10" fill="#FFD84A" transform="rotate(-20 78 52)" {s()}/>
{dots([(40,86),(88,86)],0,'none')}
<circle cx="38" cy="54" r="8" fill="#FF6B6B" {s()}/><circle cx="56" cy="36" r="7" fill="#7BD35A" {s()}/>
<circle cx="30" cy="30" r="6" fill="#FFB43A" {s()}/><circle cx="100" cy="24" r="6" fill="#A98BF0" {s()}/>
{face(64, 96, d=11, k=0.8)}
{sparkle(84, 30, 4)}
'''), "герой: круглая жестяная баночка леденцов монпансье | сцена: крышка приоткрылась, и разноцветные леденцы выпрыгивают наружу")

# 9 Wow Pizza — пицца-фрисби летит над травой, за ней бежит щенок
I["cafe-wow-pizza-solnechnogorsk"] = (svg2("#E9F9FF", "#74C8F0", f'''
<path d="M0 100 Q64 88 128 100 V128 H0Z" fill="#7CD26E" {s()}/>
<g transform="rotate(-12 74 46)">
<ellipse cx="74" cy="46" rx="34" ry="14" fill="#E89A3C" {s()}/>
<ellipse cx="74" cy="44" rx="28" ry="10" fill="#FFD95A"/>
<circle cx="62" cy="42" r="4" fill="#E5473D"/><circle cx="84" cy="44" r="4" fill="#E5473D"/><circle cx="74" cy="48" r="3" fill="#4CAF50"/>
</g>
{eye(68, 40, 0.75)}{eye(80, 37, 0.75)}
<ellipse cx="75" cy="47" rx="3" ry="3.6" fill="#8A2E3B" transform="rotate(-12 75 47)"/>
<path d="M20 30 h10 M16 40 h12 M22 50 h8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="38" cy="94" rx="18" ry="11" fill="#E7B98A" {s()}/>
<circle cx="24" cy="82" r="11" fill="#E7B98A" {s()}/>
<path d="M18 74 Q10 80 14 90" fill="#9A6A40" {W(2.2)}/>
<path d="M54 90 Q62 84 60 78" fill="none" stroke="#E7B98A" stroke-width="5" stroke-linecap="round"/>
{eye(22, 80, 0.6)}<circle cx="16" cy="86" r="2.4" fill="{O}"/>
<path d="M28 106 v8 M46 106 v8" stroke="#E7B98A" stroke-width="5" stroke-linecap="round"/>
'''), "герой: пицца-фрисби с изумлёнными глазами | сцена: летит над зелёной лужайкой, а за ней бежит щенок")

# 10 Relax — сырник-йог в позе лотоса на коврике
I["cafe-relax-voskresensk"] = (svg2("#F3FFF4", "#8FD9A8", f'''
<path d="M14 100 L114 100 L120 112 L8 112Z" fill="#B99BFF" {s()}/>
<path d="M30 98 Q64 84 98 98 Q64 104 30 98Z" fill="#E8A65A" {s()}/>
<ellipse cx="64" cy="64" rx="28" ry="24" fill="#F6C27A" {s()}/>
<ellipse cx="64" cy="48" rx="20" ry="6" fill="#E89A4A" opacity=".6"/>
<path d="M38 68 Q24 70 22 82 M90 68 Q104 70 106 82" fill="none" stroke="#F6C27A" stroke-width="7" stroke-linecap="round"/>
<circle cx="22" cy="84" r="4" fill="#F6C27A" {W(2)}/><circle cx="106" cy="84" r="4" fill="#F6C27A" {W(2)}/>
{closed(64, 64, d=9, k=0.9)}
<path d="M60 74 Q64 77 68 74" fill="none" {W(2.4)}/>
<path d="M58 34 Q56 24 64 18 Q72 24 70 34" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="64" cy="40" r="5" fill="#E04F7A" {W(2)}/>
'''), "герой: сырник-йог с капелькой варенья на макушке | сцена: медитирует в позе лотоса на сиреневом коврике")

# 11 Траттерия — панна-котта пляшет на блюдце, с неё стекает ягодный соус
I["cafe-tratteria-tsyurupy"] = (svg2("#FFFBEA", "#F0C04A", f'''
<ellipse cx="64" cy="108" rx="44" ry="10" fill="#FFFFFF" {s()}/>
<path d="M34 102 L40 50 Q64 40 88 50 L94 102 Q64 112 34 102Z" fill="#FFF4DC" {s()}/>
<path d="M40 50 Q64 40 88 50 Q90 60 82 62 Q80 72 74 64 Q66 60 62 70 Q58 60 50 62 Q44 70 42 60 Q36 58 40 50Z" fill="#C2234E" {s()}/>
<circle cx="62" cy="40" r="6" fill="#E5374D" {W(2)}/><path d="M62 34 Q66 26 72 28" fill="none" stroke="#3E9E3A" stroke-width="2.6"/>
{face(64, 82, d=11, k=0.85)}
<path d="M22 86 q-4 -6 0 -12 M106 86 q4 -6 0 -12 M16 96 q-4 -6 0 -12 M112 96 q4 -6 0 -12" fill="none" {W(2.2)}/>
'''), "герой: панна-котта с ягодным соусом и ягодкой | сцена: весело покачивается на блюдце, соус стекает по бокам")

# 12 Семейный очаг — семейство из трёх оладушек сидит на сковородке-диванчике
I["cafe-semeyny-ochag-vinogradovo"] = (svg2("#FFF0E0", "#D9824A", f'''
<path d="M8 82 Q8 112 64 114 Q120 112 120 82Z" fill="#4A4A5A" {s()}/>
<path d="M120 88 L128 84" stroke="#4A4A5A" stroke-width="8"/>
<ellipse cx="64" cy="82" rx="56" ry="8" fill="#6A6A7A" {s()}/>
<ellipse cx="36" cy="66" rx="22" ry="17" fill="#F2B860" {s()}/>
<ellipse cx="88" cy="64" rx="24" ry="19" fill="#E8A44A" {s()}/>
<ellipse cx="62" cy="74" rx="13" ry="10" fill="#FFD27A" {s()}/>
{face(36, 64, d=7, k=0.65)}{face(88, 62, d=8, k=0.7)}{face(62, 72, d=5, k=0.5)}
<path d="M54 52 l-4 -6 M76 46 l2 -6" {W(2)}/>
<path d="M60 40 Q64 32 68 40 Q72 34 74 42 Q64 52 60 40Z" fill="#FF7FA8" {W(2)}/>
'''), "герой: семья из трёх оладушек — папа, мама и малыш | сцена: сидят в обнимку на чугунной сковородке, как на диванчике")

# 13 Жар-птица — медовик с огненным пером на макушке на резной деревянной подставке
I["cafe-zhar-ptitsa-egorevsk"] = (svg2("#FFF2D6", "#E0482E", f'''
<path d="M30 112 H98 L92 100 H36Z" fill="#9A5E2E" {s()}/>
<path d="M44 106 h6 M60 106 h6 M76 106 h6" stroke="#E0B07A" stroke-width="3"/>
<rect x="30" y="56" width="68" height="44" rx="6" fill="#F0B04A" {s()}/>
<path d="M30 70 H98 M30 84 H98" stroke="#C47A2A" stroke-width="3"/>
<path d="M30 60 Q64 52 98 60" fill="none" {W(2)} opacity=".4"/>
<path d="M64 56 Q50 30 66 12 Q66 28 78 22 Q72 40 64 56Z" fill="#FF7A1A" {s()}/>
<path d="M64 52 Q58 36 66 24 Q68 36 72 34 Q68 44 64 52Z" fill="#FFD84A"/>
{face(64, 78, d=12, k=0.85)}
{sparkle(28, 34, 5, "#FFE07A")}{sparkle(100, 30, 6, "#FFE07A")}
'''), "герой: медовик с огненным пером жар-птицы на макушке | сцена: сияет на резной деревянной подставке")

# 14 Кельты — картофелина в клетчатом килте играет на волынке на зелёном холме
I["cafe-kelty-egorevsk"] = (svg2("#EAF7FF", "#5E9BD6", f'''
<path d="M0 98 Q50 80 128 96 V128 H0Z" fill="#5DBA4C" {s()}/>
<path d="M44 88 L84 88 L88 108 L40 108Z" fill="#2E8B57" {s()}/>
<path d="M50 88 L48 108 M64 88 V108 M78 88 L80 108 M42 96 H86" stroke="#D83A3A" stroke-width="2.4"/>
<ellipse cx="64" cy="64" rx="24" ry="28" fill="#D9A866" {s()}/>
<circle cx="54" cy="48" r="2" fill="#A87A3E"/><circle cx="76" cy="76" r="2.4" fill="#A87A3E"/><circle cx="70" cy="44" r="1.8" fill="#A87A3E"/>
{face(62, 60, d=8, k=0.8)}
<ellipse cx="94" cy="70" rx="13" ry="10" fill="#7E4BBF" {s()}/>
<path d="M90 62 L98 30 M98 64 L108 36 M102 68 L116 46" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/>
<path d="M84 72 L74 70" stroke="#3B3355" stroke-width="3.4" stroke-linecap="round"/>
<path d="M86 66 Q80 62 78 66" fill="none" stroke="#D9A866" stroke-width="6" stroke-linecap="round"/>
<path d="M20 30 q0 -8 5 -8 v12" fill="none" {W(2.2)}/><ellipse cx="22" cy="34" rx="4" ry="3" fill="{O}"/>
'''), "герой: картофелина в клетчатом килте | сцена: играет на волынке, стоя на зелёном холме")

# 15 Крендель — хала-косичка с бантиком лежит на расшитом полотенце
I["cafe-krendel-egorevsk"] = (svg2("#FFF7EE", "#E7A574", f'''
<path d="M8 84 L120 84 L120 112 L8 112Z" fill="#FFFFFF" {s()}/>
<path d="M8 104 H120" stroke="#D83A3A" stroke-width="3"/>
<g fill="#D83A3A">{''.join(f'<path d="M{x} 92 l4 4 l-4 4 l-4 -4Z"/>' for x in range(18, 120, 14))}</g>
<ellipse cx="38" cy="70" rx="18" ry="15" fill="#E8A24A" {s()}/>
<ellipse cx="64" cy="66" rx="18" ry="17" fill="#F0B45A" {s()}/>
<ellipse cx="90" cy="70" rx="18" ry="15" fill="#E8A24A" {s()}/>
<path d="M26 62 Q34 70 46 62 M78 62 Q88 70 100 62" fill="none" stroke="#B9732A" stroke-width="2.4"/>
<g fill="#fff">{dots([(34,62),(44,68),(58,58),(70,60),(86,62),(96,68)],1.6,'#FFFBEA')}</g>
{face(64, 68, d=8, k=0.75)}
<path d="M90 50 L80 42 L80 56Z M90 50 L100 42 L100 56Z" fill="#4DA3FF" {W(2.2)}/><circle cx="90" cy="50" r="3.4" fill="#4DA3FF" {W(2)}/>
'''), "герой: плетёная хала-косичка с голубым бантиком | сцена: лежит на расшитом красным узором полотенце")

# 16 La Bicicleta — велосипед с колёсами-дольками апельсина, в корзинке багет
I["cafe-la-bicicleta-dubna"] = (svg2("#FFFDE8", "#F2C94C", f'''
<path d="M0 108 H128" stroke="#C49A3A" stroke-width="3"/>
{''.join(f'<circle cx="{cx}" cy="86" r="22" fill="#FF9A2E" {s()}/><circle cx="{cx}" cy="86" r="16" fill="#FFD27A"/>' + ''.join(f'<path d="M{cx} 86 L{cx+16*math.cos(a):.1f} {86+16*math.sin(a):.1f}" stroke="#FF9A2E" stroke-width="2.4"/>' for a in [i*math.pi/4 for i in range(8)]) for cx in (30, 98))}
<path d="M30 86 L52 56 L84 56 L98 86 M52 56 L64 86 L84 56 M64 86 L30 86" fill="none" stroke="#2F7FD0" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M48 48 H60 M84 56 L90 40 L100 40" fill="none" {W(4)}/>
<path d="M90 30 H114 L110 46 H94Z" fill="#C98A4A" {s()}/>
<path d="M96 32 L108 8" stroke="#F0B45A" stroke-width="7" stroke-linecap="round"/>
<path d="M96 32 L108 8" fill="none" {W(2)} opacity=".5"/>
<circle cx="64" cy="86" r="5" fill="#3B3355"/>
{eye(26, 84, 0.6)}{eye(34, 84, 0.6)}{eye(94, 84, 0.6)}{eye(102, 84, 0.6)}
'''), "герой: синий велосипед с колёсами из долек апельсина | сцена: везёт в плетёной корзинке хрустящий багет")

# 17 Иберия — лепёшка-мчади делает колесо на траве у гор
I["cafe-iberia-dubna"] = (svg2("#EAF4FF", "#8FA8E8", f'''
<path d="M0 84 L30 44 L54 72 L80 34 L128 86 V128 H0Z" fill="#9FB0D8" {s()}/>
<path d="M22 54 L30 44 L38 54 Q30 58 22 54Z M72 44 L80 34 L88 46 Q80 50 72 44Z" fill="#fff"/>
<path d="M0 100 Q64 88 128 100 V128 H0Z" fill="#6FC35A" {s()}/>
<g transform="rotate(-25 64 74)">
<ellipse cx="64" cy="74" rx="22" ry="20" fill="#F3C845" {s()}/>
<path d="M52 66 l6 2 M70 64 l6 2 M60 84 l6 1" stroke="#D9A02A" stroke-width="2.4" stroke-linecap="round"/>
<rect x="56" y="66" width="16" height="12" rx="3" fill="#FFF8E6" {W(2)}/>
<path d="M44 76 L22 70 M84 76 L106 70 M58 92 L52 112 M70 92 L80 110" stroke="#F3C845" stroke-width="6" stroke-linecap="round"/>
</g>
{face(64, 66, d=8, k=0.7)}
'''), "герой: кукурузная лепёшка-мчади с ломтиком сулугуни | сцена: делает колесо на зелёной лужайке у снежных гор")

# 18 Бастурма — армянская гата с узором катается на качелях-лодочке в парке
I["cafe-basturma-dubna"] = (svg2("#F0FFF0", "#5FB86A", f'''
<path d="M20 4 L40 50 M108 4 L88 50" stroke="#8A5A33" stroke-width="5" stroke-linecap="round"/>
<path d="M30 6 H98" stroke="#8A5A33" stroke-width="6" stroke-linecap="round"/>
<path d="M28 76 Q64 100 100 76 L96 72 Q64 90 32 72Z" fill="#D9543A" {s()}/>
<path d="M40 50 L36 74 M88 50 L92 74" {W(2.6)}/>
<circle cx="64" cy="62" r="24" fill="#E9B85A" {s()}/>
<circle cx="64" cy="62" r="17" fill="none" stroke="#B87A2A" stroke-width="2.2" stroke-dasharray="4 3"/>
<path d="M64 44 V80 M46 62 H82" stroke="#B87A2A" stroke-width="1.6" opacity=".6"/>
{face(64, 62, d=8, k=0.75)}
<path d="M0 112 Q64 104 128 112 V128 H0Z" fill="#7CD26E" {s()}/>
<path d="M104 30 q6 -4 10 0 M14 40 q6 -4 10 0" fill="none" {W(2)}/>
'''), "герой: круглая армянская гата с узором-штампом | сцена: качается на красных качелях-лодочке в парке")

# 19 Кинза — пучок кинзы с хвостиком поливает сам себя из маленькой лейки
I["cafe-kinza-dubna"] = (svg2("#F6FFE6", "#B7D94A", f'''
<path d="M56 112 L60 74 M64 112 V70 M72 112 L68 74" stroke="#3E8E3A" stroke-width="5" stroke-linecap="round"/>
<path d="M54 100 H74" stroke="#E04F7A" stroke-width="6" stroke-linecap="round"/>
<path d="M30 52 Q30 26 52 28 Q58 12 76 18 Q96 16 98 38 Q110 52 96 66 Q88 80 64 76 Q40 80 34 66 Q22 62 30 52Z" fill="#5CC24A" {s()}/>
<path d="M44 42 q6 -6 10 0 M70 30 q6 -6 10 0 M84 54 q6 -6 10 0 M42 62 q6 -6 10 0" fill="none" stroke="#3E9E3A" stroke-width="2.4"/>
{face(64, 52, d=9, k=0.85)}
<path d="M100 24 L112 18 L116 32 L104 34Z" fill="#4DA3FF" {s()}/>
<path d="M104 26 L88 16" stroke="#4DA3FF" stroke-width="5" stroke-linecap="round"/>
<path d="M84 14 l-4 4 M80 22 l-4 4 M88 22 l-3 5" stroke="#4DA3FF" stroke-width="2.6" stroke-linecap="round"/>
'''), "герой: пучок кинзы с розовой ленточкой | сцена: поливает сам себя из маленькой голубой лейки")

# 20 Усадьба Бушарино — печёное яблоко в шали сидит на крыльце усадьбы с колоннами
I["cafe-busharino"] = (svg2("#FFF6F0", "#C9A0D8", f'''
<path d="M14 40 L64 14 L114 40Z" fill="#F3E6D8" {s()}/>
<rect x="18" y="40" width="92" height="56" fill="#FFF8F0" {s()}/>
<path d="M30 40 V96 M46 40 V96 M82 40 V96 M98 40 V96" stroke="#E0CBB5" stroke-width="6"/>
<path d="M30 40 V96 M46 40 V96 M82 40 V96 M98 40 V96" fill="none" {W(1.6)}/>
<rect x="8" y="96" width="112" height="10" fill="#D8C2AA" {s()}/><rect x="0" y="106" width="128" height="22" fill="#C8B09A" {s()}/>
<circle cx="64" cy="76" r="20" fill="#D9473A" {s()}/>
<path d="M64 56 Q62 48 68 44" fill="none" stroke="#7A4A28" stroke-width="3"/>
<path d="M44 82 Q64 70 84 82 L80 96 Q64 104 48 96Z" fill="#7E4BBF" {s()}/>
<g fill="#FFD84A">{dots([(54,88),(64,92),(74,88)],2.4,'#FFD84A')}</g>
{face(64, 72, d=7, k=0.7)}
'''), "герой: печёное яблоко в фиолетовой шали | сцена: сидит на крыльце белой усадьбы с колоннами")

# 21 Здесь был Чехов — булочка в пенсне читает книжку, сидя на стопке книг
I["cafe-zdes-byl-chekhov-zvenigorod"] = (svg2("#F2F6FF", "#7D8FB8", f'''
<rect x="28" y="96" width="72" height="12" rx="2" fill="#C0392B" {s()}/>
<rect x="34" y="84" width="62" height="12" rx="2" fill="#2E7D5B" {s()}/>
<path d="M30 102 H98 M36 90 H94" stroke="#fff" stroke-width="1.6" opacity=".6"/>
<path d="M32 84 Q30 46 64 42 Q98 46 96 84Z" fill="#E9A85A" {s()}/>
<path d="M44 52 Q50 46 56 52 M72 52 Q78 46 84 52" fill="none" stroke="#FFF2D0" stroke-width="3" stroke-linecap="round"/>
<circle cx="54" cy="64" r="7" fill="#fff" fill-opacity=".4" {W(2.2)}/><circle cx="74" cy="64" r="7" fill="#fff" fill-opacity=".4" {W(2.2)}/>
<path d="M61 64 H67 M47 64 Q40 70 42 78" fill="none" {W(1.8)}/>
{eye(54, 64, 0.6)}{eye(74, 64, 0.6)}
<path d="M60 74 Q64 77 68 74" fill="none" {W(2.2)}/>
<path d="M40 78 L64 84 L88 78 L88 70 L64 76 L40 70Z" fill="#FFFFFF" {s()}/>
<path d="M64 76 V84" {W(1.8)}/>
'''), "герой: сдобная булочка в пенсне | сцена: читает раскрытую книжку, сидя на стопке старых книг")

# 22 Таёжные дачи — черничная ватрушка-грибник с корзинкой в тайге под ёлками
I["cafe-taezhnye-dachi"] = (svg2("#E8F5EC", "#2F7A55", f'''
<path d="M10 92 L24 40 L38 92Z M92 94 L108 34 L124 94Z" fill="#1F6B45" {s()}/>
<path d="M0 104 Q64 94 128 104 V128 H0Z" fill="#6B8F3A" {s()}/>
<circle cx="60" cy="72" r="26" fill="#F2C98A" {s()}/>
<circle cx="60" cy="72" r="15" fill="#4B3B8C" {s()}/>
<g fill="#7A6AD0">{dots([(54,68),(64,66),(58,78),(66,76)],2.6,'#7A6AD0')}</g>
<path d="M30 52 Q40 30 60 34 Q80 30 90 52 Q60 44 30 52Z" fill="#E7C27A" {s()}/>
<path d="M58 34 L56 26" {W(2.4)}/>
{eye(50, 60, 0.6)}{eye(70, 60, 0.6)}
<path d="M88 84 H110 L106 100 H92Z" fill="#B07A45" {s()}/><path d="M90 84 Q99 70 108 84" fill="none" {W(2.6)}/>
<circle cx="96" cy="82" r="3.5" fill="#4B3B8C"/><circle cx="103" cy="81" r="3" fill="#4B3B8C"/>
'''), "герой: черничная ватрушка в панамке | сцена: собирает ягоды в лукошко в тайге между ёлками")

# 23 Величъ — гранола-парфе в стакане загорает в шезлонге у бассейна
I["cafe-velich-suponevo"] = (svg2("#E6FBFF", "#3FBBD6", f'''
<rect x="0" y="94" width="128" height="34" fill="#53C6F0" {s()}/>
<path d="M10 104 q8 -4 16 0 q8 4 16 0 M70 112 q8 -4 16 0 q8 4 16 0" fill="none" stroke="#fff" stroke-width="2.6"/>
<path d="M16 90 L104 90 L112 70" fill="none" stroke="#F4F4F4" stroke-width="8" stroke-linecap="round"/>
<path d="M16 90 L104 90 L112 70" fill="none" {W(2)}/>
<path d="M30 90 L26 98 M96 90 L100 98" {W(3)}/>
<path d="M42 86 L48 36 H82 L88 86Z" fill="#FFFFFF" fill-opacity=".85" {s()}/>
<path d="M44 74 H86 L87 86 H43Z" fill="#F7E6C4"/>
<path d="M45 60 H85 L86 74 H44Z" fill="#F06B8A"/>
<path d="M46 48 H84 L85 60 H45Z" fill="#FFF8E8"/>
<g fill="#C98A4A">{dots([(54,78),(64,80),(76,78),(70,82)],2.2,'#C98A4A')}</g>
<path d="M42 86 L48 36 H82 L88 86Z" fill="none" {s()}/>
<circle cx="56" cy="34" r="5" fill="#5B4BC0" {W(2)}/><circle cx="68" cy="32" r="5" fill="#E5374D" {W(2)}/>
<path d="M54 40 Q64 36 76 40 L74 46 H56Z" fill="#222" opacity=".85"/>
<path d="M60 56 Q65 59 70 56" fill="none" {W(2.2)}/>
'''), "герой: гранола-парфе в стакане в тёмных очках | сцена: загорает в шезлонге у бассейна загородного клуба")

# 24 Олимпик — шарик мороженого-штангист поднимает штангу из двух вишенок
I["cafe-olimpik-aprelevka"] = (svg2("#FFF0F5", "#F28AB2", f'''
<path d="M48 76 L64 118 L80 76Z" fill="#E8B060" {s()}/>
<path d="M54 84 L72 100 M60 80 L76 92 M52 92 L66 106 M74 82 L58 100" stroke="#C48A3A" stroke-width="2"/>
<circle cx="64" cy="62" r="22" fill="#B9F0D6" {s()}/>
<path d="M42 66 Q50 74 58 68 Q64 76 72 68 Q80 74 86 66" fill="#B9F0D6" {s()}/>
{face(64, 60, d=8, k=0.8)}
<path d="M42 58 Q30 46 26 36 M86 58 Q98 46 102 36" fill="none" stroke="#B9F0D6" stroke-width="7" stroke-linecap="round"/>
<path d="M14 32 H114" stroke="#5A5A6A" stroke-width="4" stroke-linecap="round"/>
<circle cx="14" cy="30" r="12" fill="#E5374D" {s()}/><circle cx="114" cy="30" r="12" fill="#E5374D" {s()}/>
<path d="M14 18 Q18 8 26 8 M114 18 Q110 8 102 8" fill="none" stroke="#3E9E3A" stroke-width="2.6"/>
<circle cx="10" cy="26" r="3" fill="#fff" opacity=".7"/><circle cx="110" cy="26" r="3" fill="#fff" opacity=".7"/>
'''), "герой: мятный шарик мороженого в рожке | сцена: поднимает над головой штангу из двух вишенок")

# 25 Kappa Cafe — башенка капрезе балансирует с листиком базилика наверху
I["cafe-kappa-aprelevka"] = (svg2("#F5FFF0", "#67B85A", f'''
<ellipse cx="64" cy="114" rx="40" ry="8" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="102" rx="26" ry="9" fill="#F5F5F0" {s()}/>
<ellipse cx="64" cy="90" rx="24" ry="9" fill="#E5373D" {s()}/>
<ellipse cx="64" cy="76" rx="26" ry="10" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="62" rx="24" ry="9" fill="#F2453D" {s()}/>
<ellipse cx="64" cy="46" rx="22" ry="12" fill="#FFFFFF" {s()}/>
{face(64, 46, d=8, k=0.7)}
<path d="M64 34 Q56 18 64 8 Q74 20 64 34Z" fill="#3EAE3A" {s()}/>
<path d="M64 32 V14" stroke="#2E8B2A" stroke-width="1.8"/>
<path d="M30 60 Q22 56 24 48 M98 60 Q106 56 104 48" fill="none" {W(2.2)}/>
'''), "герой: башенка капрезе из моцареллы и томатов | сцена: балансирует, держа на макушке листик базилика")

# 26 Сценарио — блинный рулет-свиток со звёздами разворачивается как сценарий
I["cafe-scenario-odintsovo"] = (svg2("#2B2D5A", "#14163A", f'''
{sparkle(20, 30, 5)}{sparkle(108, 22, 6, "#FFE07A")}{sparkle(100, 100, 4)}
<path d="M30 46 H98 V100 H30Z" fill="#F7D79C" {s()}/>
<ellipse cx="30" cy="73" rx="10" ry="27" fill="#E8B060" {s()}/>
<ellipse cx="30" cy="73" rx="5" ry="14" fill="#C9883A"/>
<ellipse cx="98" cy="73" rx="10" ry="27" fill="#E8B060" {s()}/>
<ellipse cx="98" cy="73" rx="5" ry="14" fill="#C9883A"/>
{sparkle(52, 88, 5, "#E5374D")}{sparkle(78, 90, 4, "#E5374D")}
<path d="M46 52 H82 M50 58 H78" stroke="#C48A3A" stroke-width="2.4" stroke-linecap="round"/>
{face(64, 72, d=11, k=0.85)}
'''), "герой: блинный рулет-свиток сценария | сцена: разворачивается на тёмной сцене, а на нём нарисованы красные звёздочки")

# 27 Стамбул — кумпир (печёная картошка с начинкой) плывёт в лодочке по Босфору мимо минарета
I["cafe-stambul-odintsovo"] = (svg2("#FFEFE0", "#E9875A", f'''
<path d="M96 20 V78 M90 78 H102 L100 30 H92Z" fill="#FFF4E8" {s()}/>
<path d="M92 30 Q96 18 100 30Z" fill="#4DA3FF" {W(2)}/>
<path d="M96 14 V8" {W(2)}/>
<path d="M0 92 Q64 84 128 92 V128 H0Z" fill="#2F9FD0" {s()}/>
<path d="M10 104 q8 -4 16 0 M50 110 q8 -4 16 0 M94 104 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M14 82 H86 L76 98 H24Z" fill="#B0573A" {s()}/>
<ellipse cx="50" cy="66" rx="28" ry="18" fill="#C48A4A" {s()}/>
<path d="M28 62 Q50 50 72 62 Q50 70 28 62Z" fill="#FFE27A" {W(2)}/>
<g>{dots([(38,58),(48,54)],3,'#E5473D')}{dots([(58,56),(64,60)],3,'#4CAF50')}{dots([(44,62)],2.6,'#FF9A2E')}</g>
{face(50, 72, d=9, k=0.75)}
'''), "герой: кумпир — печёная картошка с пёстрой начинкой | сцена: плывёт в лодочке по Босфору мимо белого минарета")

# 28 Утиные истории — картошка фри в бумажном кораблике плывёт по пруду с кувшинками
I["cafe-utinye-istorii-odintsovo"] = (svg2("#E6F7FF", "#5AA9D8", f'''
<rect x="0" y="86" width="128" height="42" fill="#3E9BD0" {s()}/>
<ellipse cx="18" cy="104" rx="14" ry="5" fill="#4CAF50" {s()}/><circle cx="18" cy="100" r="4" fill="#FF8FB5" {W(1.8)}/>
<ellipse cx="108" cy="114" rx="14" ry="5" fill="#4CAF50" {s()}/>
<path d="M30 80 L98 80 L84 100 L44 100Z" fill="#FFFFFF" {s()}/>
<path d="M64 80 L64 42 L42 80Z" fill="#F4F4F4" {s()}/>
<path d="M68 80 V44 M76 80 V38 M84 80 V46" stroke="#F7C948" stroke-width="7" stroke-linecap="round"/>
<path d="M68 80 V44 M76 80 V38 M84 80 V46" fill="none" {W(1.6)} opacity=".5"/>
<path d="M60 80 L62 40" stroke="#F7C948" stroke-width="7" stroke-linecap="round"/>
<rect x="56" y="66" width="34" height="18" rx="3" fill="#E5373D" {s()}/>
{face(73, 74, d=7, k=0.6)}
'''), "герой: картошка фри в красном стаканчике | сцена: плывёт в бумажном кораблике по пруду с кувшинками")

# 29 Сербия — плескавица танцует хоровод-коло с двумя луковыми колечками
I["cafe-serbia-odintsovo"] = (svg2("#FFF6F6", "#C8484A", f'''
<path d="M0 108 H128" stroke="#fff" stroke-width="3" opacity=".6"/>
<ellipse cx="64" cy="64" rx="26" ry="24" fill="#8A4B2E" {s()}/>
<path d="M46 56 l8 -4 M70 50 l8 2 M50 76 l8 2 M74 74 l8 -2" stroke="#5A2E1A" stroke-width="3" stroke-linecap="round"/>
{face(64, 62, d=9, k=0.8)}
<path d="M40 70 L28 76 M88 70 L100 76 M54 86 L48 104 M74 86 L82 104" stroke="#8A4B2E" stroke-width="6" stroke-linecap="round"/>
<ellipse cx="18" cy="80" rx="12" ry="14" fill="none" stroke="#FFF2D6" stroke-width="7"/>
<ellipse cx="18" cy="80" rx="12" ry="14" fill="none" {W(1.6)}/>
<ellipse cx="110" cy="80" rx="12" ry="14" fill="none" stroke="#FFF2D6" stroke-width="7"/>
<ellipse cx="110" cy="80" rx="12" ry="14" fill="none" {W(1.6)}/>
{eye(15, 80, 0.5)}{eye(21, 80, 0.5)}{eye(107, 80, 0.5)}{eye(113, 80, 0.5)}
<path d="M58 30 L64 24 L70 30 L64 36Z" fill="#2F5FB0" {W(2)}/>
'''), "герой: сербская плескавица с румяной корочкой | сцена: танцует хоровод-коло, держась за руки с двумя луковыми колечками")

# 30 Мечтать не вредно — клубничка в ночном колпаке на подушке-маршмеллоу смотрит на падающую звезду
I["cafe-mechtat-odintsovo"] = (svg2("#6D63C8", "#2E2A6E", f'''
<path d="M86 14 L118 36" stroke="#FFE07A" stroke-width="3" stroke-linecap="round" opacity=".7"/>
{sparkle(86, 14, 7, "#FFE07A")}{sparkle(24, 24, 4)}{sparkle(110, 64, 3)}
<rect x="18" y="86" width="92" height="26" rx="13" fill="#FFF0F6" {s()}/>
<path d="M30 96 H98" stroke="#F7C6DA" stroke-width="3"/>
<path d="M44 86 Q36 56 64 50 Q92 56 84 86Z" fill="#F0384E" {s()}/>
<g fill="#FFE27A">{dots([(54,64),(72,62),(62,76),(50,78),(76,78)],1.8,'#FFE27A')}</g>
<path d="M46 58 Q50 30 76 26 Q72 40 82 56 Q64 50 46 58Z" fill="#7FC7F2" {s()}/>
<circle cx="76" cy="24" r="5" fill="#fff" {W(2)}/>
{eye(56, 70, 0.6)}{eye(70, 68, 0.6)}
<path d="M60 78 Q64 80 68 78" fill="none" {W(2)}/>
'''), "герой: клубничка в голубом ночном колпаке | сцена: лежит на подушке-маршмеллоу и мечтательно смотрит на падающую звезду")

# 31 Три восьмёрки — сосиска в тесте, свернувшаяся восьмёркой, катится по дорожке
I["cafe-tri-vosmerki-borodino"] = (svg2("#F0FAFF", "#A6C8E8", f'''
<path d="M0 104 H128 V128 H0Z" fill="#D8C2A0" {s()}/>
<path d="M10 116 h14 M40 116 h14 M70 116 h14 M100 116 h14" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M64 64 C40 40 40 16 64 18 C88 16 88 40 64 64 C40 88 40 104 64 104 C88 104 88 88 64 64Z" fill="none" stroke="#C25A3A" stroke-width="14" stroke-linecap="round"/>
<path d="M64 64 C40 40 40 16 64 18 C88 16 88 40 64 64 C40 88 40 104 64 104 C88 104 88 88 64 64Z" fill="none" stroke="#F2C27A" stroke-width="8" stroke-dasharray="10 5"/>
{face(64, 84, d=8, k=0.7)}
<path d="M14 70 h12 M10 82 h14 M16 94 h10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: сосиска в тесте, свернувшаяся восьмёркой | сцена: катится колесом по песчаной дорожке")

# 32 PanDuri — глиняный горшочек лобио играет на трёхструнном пандури
I["cafe-panduri-ramenskoe"] = (svg2("#FFF4E6", "#B9694A", f'''
<path d="M36 70 Q30 108 64 110 Q98 108 92 70Z" fill="#C2643A" {s()}/>
<path d="M40 82 Q64 90 88 82" fill="none" stroke="#F2C9A0" stroke-width="3"/>
<ellipse cx="64" cy="70" rx="30" ry="8" fill="#7A2E2E" {s()}/>
<g fill="#A83A3A">{dots([(54,68),(64,72),(74,68)],3,'#A83A3A')}</g>
{face(64, 92, d=10, k=0.75)}
<g transform="rotate(-35 92 52)">
<ellipse cx="92" cy="62" rx="12" ry="16" fill="#E0A55A" {s()}/>
<rect x="88" y="14" width="8" height="34" rx="2" fill="#B07A45" {s()}/>
<path d="M90 20 V70 M92 20 V70 M94 20 V70" stroke="#3B3355" stroke-width="0.8"/>
<circle cx="92" cy="60" r="3" fill="#5A3420"/>
</g>
<path d="M36 76 Q28 66 40 58" fill="none" stroke="#C2643A" stroke-width="6" stroke-linecap="round"/>
<path d="M18 30 q0 -8 5 -8 v12" fill="none" {W(2.2)}/><ellipse cx="20" cy="34" rx="4" ry="3" fill="{O}"/>
'''), "герой: глиняный горшочек красного лобио | сцена: играет на трёхструнном пандури")

# 33 Халиф — рахат-лукум в чалме сидит на расшитой подушке под аркой дворца
I["cafe-khalif-noginsk"] = (svg2("#FFF3D6", "#D6A23A", f'''
<path d="M14 128 V54 Q14 14 64 10 Q114 14 114 54 V128" fill="none" stroke="#8A3FB0" stroke-width="8"/>
<path d="M14 128 V54 Q14 14 64 10 Q114 14 114 54 V128" fill="none" {W(2)}/>
<path d="M22 96 H106 L100 112 H28Z" fill="#C0392B" {s()}/>
<g fill="#FFD84A">{dots([(22,96),(106,96),(28,112),(100,112)],3.4,'#FFD84A')}</g>
<rect x="40" y="56" width="48" height="40" rx="8" fill="#F7A8C4" {s()}/>
<g fill="#fff">{dots([(48,64),(60,60),(76,66),(82,84),(46,86),(66,88)],1.8,'#fff')}</g>
<path d="M38 56 Q40 32 64 30 Q88 32 90 56 Q64 48 38 56Z" fill="#FFFFFF" {s()}/>
<path d="M42 48 Q64 40 86 48" fill="none" stroke="#E0E0E0" stroke-width="2.4"/>
<circle cx="64" cy="40" r="5" fill="#2EB8A0" {W(2)}/><path d="M64 34 Q70 22 78 22" fill="none" stroke="#E5374D" stroke-width="3"/>
{face(64, 74, d=10, k=0.8)}
'''), "герой: розовый рахат-лукум в белой чалме с изумрудом | сцена: сидит на расшитой подушке под аркой дворца")

# 34 СтандАрт — квадратный тост меряет себя линейкой и сияет
I["cafe-standart-noginsk"] = (svg2("#EEFAF2", "#4FAE8A", f'''
<rect x="28" y="34" width="56" height="62" rx="10" fill="#E9B266" {s()}/>
<rect x="34" y="40" width="44" height="50" rx="7" fill="#FFF2D2"/>
{face(56, 64, d=9, k=0.85)}
<path d="M28 100 V114 M84 100 V114 M28 108 H84" stroke="#3B3355" stroke-width="2.4" stroke-linecap="round"/>
<rect x="94" y="22" width="14" height="88" rx="2" fill="#FFD84A" {s()}/>
<path d="M94 32 h6 M94 42 h4 M94 52 h6 M94 62 h4 M94 72 h6 M94 82 h4 M94 92 h6 M94 102 h4" {W(1.8)}/>
<path d="M84 60 Q90 56 94 58" fill="none" stroke="#E9B266" stroke-width="6" stroke-linecap="round"/>
{sparkle(20, 30, 5)}{sparkle(18, 72, 4)}
'''), "герой: идеально квадратный тост | сцена: меряет себя жёлтой линейкой и сияет от гордости")

# 35 Дриада — бургер в венке из цветов сидит на ветке дуба
I["cafe-driada-noginsk"] = (svg2("#F0FFE8", "#6DBF5A", f'''
<path d="M0 96 Q60 82 128 70" fill="none" stroke="#7A4A28" stroke-width="12" stroke-linecap="round"/>
<path d="M0 96 Q60 82 128 70" fill="none" {W(2)} opacity=".5"/>
<path d="M100 74 Q108 58 120 60 Q116 74 100 74Z M22 92 Q16 106 26 112 Q32 100 22 92Z" fill="#3E9E3A" {W(2)}/>
<path d="M38 58 Q38 32 64 30 Q90 32 90 58Z" fill="#E8A44A" {s()}/>
<rect x="36" y="58" width="56" height="10" rx="3" fill="#6FCB4A" {s()}/>
<rect x="38" y="66" width="52" height="10" rx="4" fill="#7A3E22" {s()}/>
<path d="M38 76 H90 Q90 86 64 86 Q38 86 38 76Z" fill="#E8A44A" {s()}/>
<g>{dots([(48,40),(58,36),(70,36),(80,40)],1.6,'#FFF2D0')}</g>
<g>{''.join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{c}" {W(1.6)}/><circle cx="{x}" cy="{y}" r="1.6" fill="#FFD84A"/>' for x, y, c in [(42,32,"#FF8FB5"),(54,26,"#FFFFFF"),(64,24,"#B99BFF"),(74,26,"#FF8FB5"),(86,32,"#FFFFFF")])}</g>
{face(64, 46, d=9, k=0.75)}
'''), "герой: бургер в венке из полевых цветов | сцена: сидит на толстой ветке дуба, как лесная дриада")

# 36 Бархат — кусочек торта «Красный бархат» в мантии раскланивается перед занавесом
I["cafe-barkhat-elektrostal"] = (svg2("#FFE6EC", "#8E1E3C", f'''
<path d="M0 0 H128 V16 Q96 26 64 16 Q32 26 0 16Z" fill="#B0183A" {s()}/>
<path d="M0 0 Q20 60 6 128 H0Z M128 0 Q108 60 122 128 H128Z" fill="#B0183A" {s()}/>
<rect x="0" y="108" width="128" height="20" fill="#7A3E22" {s()}/>
<path d="M34 104 L94 104 L94 66 L34 52Z" fill="#C8243E" {s()}/>
<path d="M34 66 L94 78 M34 80 L94 90" stroke="#FFFFFF" stroke-width="5"/>
<path d="M34 52 L94 66" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>
<circle cx="80" cy="54" r="6" fill="#E5374D" {W(2)}/>
<path d="M30 56 Q24 80 34 104 M98 70 Q104 88 94 104" fill="none" stroke="#5A2A8A" stroke-width="5"/>
{closed(62, 84, d=8, k=0.75)}
<path d="M58 94 Q62 97 66 94" fill="none" {W(2)}/>
'''), "герой: кусочек торта «Красный бархат» в фиолетовой мантии | сцена: раскланивается на сцене перед бархатным занавесом")

# 37 Соль и перец — картошка по-деревенски жмурится под дождём из солинок и перчинок
I["cafe-sol-perets-dmitrov"] = (svg2("#FFFFFF", "#B8B8C8", f'''
<g>{dots([(30,20),(50,14),(72,22),(94,16),(40,34),(84,32),(62,38),(104,30),(24,40)],2.6,'#FFFFFF')}</g>
<g fill="none" stroke="#3B3355" stroke-width="1.4">{''.join(f'<rect x="{x-2.4}" y="{y-2.4}" width="4.8" height="4.8"/>' for x, y in [(30,20),(72,22),(40,34),(104,30)])}</g>
<g>{dots([(50,14),(94,16),(84,32),(62,38),(24,40)],2.6,'#3B3355')}</g>
<ellipse cx="64" cy="112" rx="46" ry="9" fill="#FFFFFF" {s()}/>
<path d="M22 102 Q20 64 52 58 Q60 82 46 106Z" fill="#E8B05A" {s()}/>
<path d="M106 102 Q108 64 76 58 Q68 82 82 106Z" fill="#E8B05A" {s()}/>
<path d="M40 104 Q38 54 64 48 Q90 54 88 104Z" fill="#F2C46A" {s()}/>
<path d="M44 60 Q64 50 84 60" fill="none" stroke="#C9883A" stroke-width="5" stroke-linecap="round"/>
<path d="M50 76 l6 3 l-6 3 M78 76 l-6 3 l6 3" fill="none" {W(2.4)}/>
<path d="M58 90 Q64 94 70 90" fill="none" {W(2.4)}/>
<ellipse cx="48" cy="88" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="80" cy="88" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
'''), "герой: дольки картошки по-деревенски | сцена: жмурятся от удовольствия под дождём из крупинок соли и перчинок")

# 38 Дон Батон — батон в бархатном берете с пером кланяется, сняв шляпу
I["cafe-don-baton-zelenograd"] = (svg2("#F7F0FF", "#9A7FD0", f'''
<ellipse cx="64" cy="112" rx="40" ry="6" fill="#7A5FB0" opacity=".4"/>
<g transform="rotate(-18 64 74)">
<path d="M46 110 Q38 68 52 40 Q64 28 76 40 Q90 68 82 110 Q64 118 46 110Z" fill="#E9A24E" {s()}/>
<path d="M52 56 Q64 50 76 56 M50 72 Q64 66 78 72 M50 88 Q64 82 78 88" fill="none" stroke="#FFE2A8" stroke-width="3.4" stroke-linecap="round"/>
</g>
{face(60, 64, d=8, k=0.75)}
<path d="M86 84 Q100 80 108 66" fill="none" stroke="#E9A24E" stroke-width="7" stroke-linecap="round"/>
<ellipse cx="108" cy="58" rx="14" ry="6" fill="#3B2A6A" {s()}/>
<path d="M98 56 Q108 42 118 56" fill="#3B2A6A" {s()}/>
<path d="M112 50 Q124 30 116 20" fill="none" stroke="#E5374D" stroke-width="5" stroke-linecap="round"/>
'''), "герой: нарезной батон-дон | сцена: галантно кланяется, сняв бархатный берет с красным пером")

# 39 Чайхана «Вкус Востока» — финики катаются с горы на узорном блюде-лягане как на санках
I["cafe-vkus-vostoka-sergiev"] = (svg2("#E8F6FF", "#3E7FC8", f'''
<ellipse cx="64" cy="100" rx="56" ry="20" fill="#FFFFFF" {s()}/>
<ellipse cx="64" cy="98" rx="44" ry="13" fill="#2F6FD0"/>
<path d="M28 98 Q64 86 100 98" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="6 4"/>
<g fill="#fff">{''.join(f'<path d="M{x} 104 l4 -4 l4 4 l-4 4Z"/>' for x in (34, 50, 66, 82))}</g>
<path d="M30 92 Q60 30 98 92Z" fill="#8A4A22" {s()}/>
{''.join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="4.5" fill="#A85A28" transform="rotate({r} {x} {y})" {W(1.6)}/>' for x, y, r in [(52,76,-20),(66,62,10),(76,80,30),(60,86,0),(84,88,10)])}
<g transform="rotate(30 96 60)"><ellipse cx="96" cy="60" rx="12" ry="8" fill="#B8652C" {s()}/></g>
{eye(92, 58, 0.55)}{eye(100, 62, 0.55)}
<path d="M24 34 Q30 30 34 36" fill="none" {W(2)}/>
<ellipse cx="34" cy="50" rx="10" ry="7" fill="#B8652C" transform="rotate(-25 34 50)" {s()}/>
{eye(31, 49, 0.5)}{eye(38, 46, 0.5)}
<path d="M108 76 h10 M110 86 h10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: финики-сладкоежки | сцена: катаются, как на санках, с горки фиников на узорном синем блюде-лягане")

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
