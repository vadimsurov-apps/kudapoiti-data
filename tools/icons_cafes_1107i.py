"""Робот cafes, 2026-11-07 (19 UTC): иконки 17 новых кафе. Каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя компоновка и палитра фона).
Запуск из корня: python3 tools/icons_cafes_1107i.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
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

# 1 Корчма — картофельный дерун со сметаной перепрыгивает через плетёный тын у белёной хаты
I["cafe-korchma-odintsovo"] = (svg2("#EAF7FF", "#8CCB6A", f'''
<path d="M70 70 L92 52 L118 70Z" fill="#E8B84A" {s()}/>
<rect x="74" y="70" width="40" height="30" fill="#FFFFFF" {s()}/>
<rect x="88" y="78" width="12" height="12" fill="#7EC8F2" {W(2.4)}/>
<path d="M0 104 H128 V128 H0Z" fill="#6DBA4E"/>
<g fill="none" stroke="#9A6A3A" stroke-width="3">
<path d="M8 86 V112 M24 86 V112 M40 86 V112 M56 86 V112"/>
<path d="M4 92 Q16 88 28 92 Q40 96 60 92 M4 100 Q16 96 28 100 Q40 104 60 100 M4 108 Q16 104 28 108 Q40 112 60 108" stroke="#B8844E" stroke-width="4"/>
</g>
<path d="M14 66 Q22 56 30 62" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<g transform="rotate(-12 54 48)">
<ellipse cx="54" cy="50" rx="30" ry="24" fill="#E9A23B" {s()}/>
<path d="M32 44 l5 3 M38 64 l6 -2 M70 66 l4 -4 M76 40 l-5 3 M48 30 l3 4" stroke="#B86E1E" stroke-width="2.6" stroke-linecap="round"/>
<path d="M38 30 Q46 18 58 22 Q70 16 74 30 Q60 34 38 30Z" fill="#FFFFFF" {s()}/>
{face(54, 50, d=10, k=0.95)}
<path d="M30 60 L18 74 M78 60 L92 70" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
</g>
'''), "герой: картофельный дерун со сметанной шапочкой | сцена: перепрыгивает через плетёный тын у белёной хаты")

# 2 Встреча — большое канапе на шпажке встречает гостей у распахнутой двери банкетного зала
I["cafe-vstrecha-odintsovo"] = (svg2("#FFE9E0", "#B5384A", f'''
<rect x="78" y="22" width="40" height="88" fill="#FFE7A8" {s()}/>
<path d="M78 22 L100 30 V118 L78 110Z" fill="#8B2C3A" {s()}/>
<circle cx="94" cy="72" r="2.6" fill="#F2C14E"/>
<path d="M96 30 v6 M112 40 v6 M106 60 v6" stroke="#fff" stroke-width="2" opacity=".7"/>
<path d="M46 8 V118" stroke="#C99A5A" stroke-width="4" stroke-linecap="round"/>
<circle cx="46" cy="16" r="10" fill="#2E2A3A" {s()}/>
<ellipse cx="43" cy="12" rx="3" ry="2" fill="#fff" opacity=".6"/>
<ellipse cx="46" cy="44" rx="24" ry="12" fill="#F28AA0" {s()}/>
<g fill="#FFFFFF">{dots([(36,42),(50,38),(58,46),(42,50)],2.4,'#FFFFFF')}</g>
<rect x="22" y="58" width="48" height="44" rx="6" fill="#FFD43A" {s()}/>
{dots([(30,94),(62,66),(60,92)],3,'#F0B21A')}
{face(46, 78, d=10, k=1.0)}
<path d="M22 72 Q8 62 6 50 M70 72 Q82 62 84 50" fill="none" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
'''), "герой: большое канапе на шпажке — кубик сыра, кружок колбасы и маслинка | сцена: раскинув руки, встречает гостей у распахнутой двери банкетного зала")

# 3 Алекс Экспресс — миска овсянки с ягодной улыбкой мчится на роликах по утренней дорожке
I["cafe-alex-express-sergiev-posad"] = (svg2("#FFF3D6", "#FFB07A", f'''
<circle cx="98" cy="34" r="14" fill="#FFD84A" {s()}/>
<path d="M0 110 H128 V128 H0Z" fill="#B9A6D9"/>
<path d="M8 50 H30 M4 64 H26 M10 78 H28" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M34 62 H102 Q100 96 68 98 Q36 96 34 62Z" fill="#5BB7E8" {s()}/>
<path d="M40 76 Q68 82 96 76" fill="none" stroke="#fff" stroke-width="3"/>
<ellipse cx="68" cy="62" rx="34" ry="9" fill="#F6E3B8" {s()}/>
{dots([(52,58),(80,60),(66,56)],3.2,'#3A57C8')}
<circle cx="74" cy="62" r="3.4" fill="#E5484D"/>
{face(68, 82, d=11, k=0.9)}
<rect x="44" y="98" width="48" height="6" rx="3" fill="#E5484D" {s()}/>
{dots([(50,108),(64,108),(78,108),(90,108)],4.2,'#FFFFFF')}
<g fill="none" {W(2)}>{''.join(f'<circle cx="{x}" cy="108" r="4.2"/>' for x in (50,64,78,90))}</g>
'''), "герой: миска овсянки с ягодной улыбкой | сцена: мчится на роликовых коньках по утренней дорожке навстречу солнцу")

# 4 Пекин — печенье с предсказанием раскрылось на красном лаковом подносе
I["cafe-pekin-pavlovsky-posad"] = (svg2("#FFE6C2", "#D9363E", f'''
<ellipse cx="64" cy="104" rx="52" ry="14" fill="#9E1F2A" {s()}/>
<ellipse cx="64" cy="100" rx="42" ry="8" fill="#C22E38"/>
<path d="M26 98 Q44 94 50 100 M78 100 Q86 94 102 98" fill="none" stroke="#F2C14E" stroke-width="2.4"/>
<path d="M20 80 Q22 40 60 34 Q66 58 64 78 Q44 92 20 80Z" fill="#F2B54A" {s()}/>
<path d="M108 80 Q106 40 68 34 Q62 58 64 78 Q84 92 108 80Z" fill="#E9A23B" {s()}/>
<path d="M60 36 Q64 50 64 78" fill="none" stroke="#C47A1E" stroke-width="2.6"/>
<path d="M58 54 L88 16 L104 26 L72 62Z" fill="#FFFFFF" {s()}/>
<path d="M84 34 c-3 -5 4 -8 5 -3 c2 -5 9 -1 5 3 l-5 6Z" fill="#E5484D"/>
{face(40, 64, d=8, k=0.8)}
{closed(88, 66, d=6, k=0.7)}
'''), "герой: печенье с предсказанием | сцена: раскрылось на красном лаковом подносе, и из него выглядывает бумажная ленточка с сердечком")

# 5 Сити — кусок торта «Наполеон» на крыше высотки любуется ночным городом
I["cafe-siti-kolomna"] = (svg2("#5A5FB8", "#23205A", f'''
<circle cx="104" cy="22" r="8" fill="#FFF3B0"/>
{sparkle(20, 20, 4)}{sparkle(80, 10, 3)}
<rect x="0" y="92" width="20" height="40" fill="#3A3A80" {s()}/>
<rect x="108" y="84" width="22" height="44" fill="#3A3A80" {s()}/>
{dots([(7,102),(14,114),(115,94),(122,106),(115,118)],2.4,'#FFE27A')}
<rect x="18" y="106" width="92" height="30" fill="#4B4BA0" {s()}/>
{dots([(30,118),(48,118),(80,118),(98,118)],2.8,'#FFE27A')}
<path d="M18 104 L104 82 V60 L18 82Z" fill="#E7B66B" {s()}/>
<path d="M18 96 L104 74 M18 89 L104 67" stroke="#FFF6E6" stroke-width="4"/>
<path d="M18 82 L104 60 L96 50 L14 72Z" fill="#F9E6C4" {s()}/>
{dots([(30,70),(46,66),(62,62),(78,58),(90,54)],2,'#E3B474')}
<path d="M104 60 V82 L114 78 V56 L96 50Z" fill="#D9A256" {s()}/>
{face(58, 88, d=10, k=0.9)}
'''), "герой: кусок торта «Наполеон» с хрустящими слоями | сцена: стоит на крыше высотного дома и любуется ночным городом с огоньками окон")
# 6 Глиссада — треугольный блинчик парит, как дельтаплан, над взлётной полосой
I["cafe-glissada-kolomna"] = (svg2("#EAF8FF", "#7FC4F0", f'''
<path d="M0 108 L128 100 V128 H0Z" fill="#7CC46A"/>
<path d="M40 128 L58 104 H72 L90 128Z" fill="#6C6C80" {s()}/>
<path d="M65 108 V112 M65 118 V124" stroke="#fff" stroke-width="3"/>
<ellipse cx="22" cy="24" rx="12" ry="5" fill="#fff"/><ellipse cx="110" cy="22" rx="10" ry="4" fill="#fff"/>
<path d="M4 74 L64 18 L124 74 Q64 64 4 74Z" fill="#F5C76A" {s()}/>
<path d="M64 18 L64 68" stroke="#D9922E" stroke-width="2.4"/>
{dots([(34,60),(50,44),(80,46),(96,60),(44,64),(86,66)],2.6,'#D9922E')}
<path d="M64 68 V90 M44 90 H84" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>
{face(64, 50, d=10, k=0.95)}
<path d="M10 92 H26 M6 100 H20" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: треугольный блинчик-конвертик | сцена: парит, как дельтаплан, над взлётной полосой аэрограда")
# 7 Оазис Garden — медовые соты отдыхают в тени пальмы у пруда-оазиса
I["cafe-oasis-garden-domodedovo"] = (svg2("#FFF6D8", "#F2C46A", f'''
<path d="M0 92 Q64 80 128 92 V128 H0Z" fill="#F6D58C"/>
<ellipse cx="86" cy="106" rx="34" ry="10" fill="#4FC7D8" {s()}/>
<path d="M70 104 Q78 100 86 104" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M104 104 Q100 70 110 40" fill="none" stroke="#9A6A3A" stroke-width="6" stroke-linecap="round"/>
<path d="M110 40 Q92 30 80 40 M110 40 Q118 22 104 14 M110 40 Q128 34 128 50 M110 40 Q100 52 92 58" fill="none" stroke="#3E9E3A" stroke-width="7" stroke-linecap="round"/>
<path d="M30 46 l14 -8 l14 8 v16 l-14 8 l-14 -8Z" fill="#FFC531" {s()}/>
<path d="M58 46 l14 -8 l14 8 v16 l-14 8 l-14 -8Z" fill="#FFC531" {s()}/>
<path d="M44 70 l14 -8 l14 8 v16 l-14 8 l-14 -8Z" fill="#FFB21E" {s()}/>
<path d="M16 70 l14 -8 l14 8 v16 l-14 8 l-14 -8Z" fill="#FFC531" {s()}/>
<path d="M58 94 q2 8 -2 10 q-4 -2 -2 -10Z" fill="#FFB21E" {W(2)}/>
{face(58, 76, d=7, k=0.75)}
'''), "герой: медовые соты с капелькой мёда | сцена: отдыхают в тени пальмы у голубого пруда-оазиса среди песка")

# 8 Моккано — кунжутный шарик цзяньдуй катается по бамбуковой циновке
I["cafe-mokkano-voskresensk"] = (svg2("#F4F9E6", "#9CC36A", f'''
<path d="M0 92 L128 80 V128 H0Z" fill="#E9D49A" {s()}/>
<path d="M0 100 L128 88 M0 110 L128 98 M0 120 L128 108" stroke="#C9AE6A" stroke-width="2.4"/>
<path d="M12 18 V70 M22 10 V64" stroke="#5DA84A" stroke-width="6"/>
<path d="M12 34 h4 M12 52 h4 M22 28 h4 M22 46 h4" stroke="#3E7E36" stroke-width="2"/>
<path d="M16 30 Q30 22 34 30" fill="none" stroke="#5DA84A" stroke-width="4" stroke-linecap="round"/>
<circle cx="70" cy="62" r="32" fill="#E9A84A" {s()}/>
<g fill="#FFF6DC">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="2.4" ry="1.4" transform="rotate({r} {x} {y})"/>' for x,y,r in [(52,44,20),(62,36,-30),(78,38,40),(90,50,-10),(96,64,30),(88,82,-40),(54,82,10),(46,64,-20),(70,90,50),(80,46,0)])}</g>
{face(70, 64, d=10, k=0.95)}
{''.join(f'<ellipse cx="{x}" cy="{y}" rx="2.4" ry="1.4" fill="#FFF6DC" {W(1)}/>' for x,y in [(28,100),(38,96),(108,92)])}
<path d="M34 80 Q28 76 24 78 M30 92 Q24 90 20 94" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
'''), "герой: китайский кунжутный шарик цзяньдуй | сцена: катается по бамбуковой циновке, рассыпая кунжутные зёрнышки")

# 9 Купеческий — блин-трубочка с красной икрой едет в расписных санях по зимней дороге
I["cafe-kupechesky-rogozinino"] = (svg2("#F2F8FF", "#9CC0E8", f'''
{dots([(18,20),(40,12),(98,18),(116,40),(10,48)],2.6,'#FFFFFF')}
<path d="M0 100 Q64 88 128 100 V128 H0Z" fill="#FFFFFF" {s()}/>
<path d="M14 104 Q64 96 118 104" fill="none" stroke="#C8D8EE" stroke-width="3"/>
<path d="M18 96 H104 Q118 96 114 84" fill="none" stroke="#C9A24A" stroke-width="4" stroke-linecap="round"/>
<path d="M22 60 H94 Q100 60 100 70 V90 H26 Q20 90 18 80Z" fill="#D9363E" {s()}/>
<path d="M30 74 q6 -8 12 0 q6 8 12 0 q6 -8 12 0 q6 8 12 0" fill="none" stroke="#F2C14E" stroke-width="3"/>
<path d="M18 80 Q8 60 16 44" fill="none" stroke="#D9363E" stroke-width="7" stroke-linecap="round"/>
<path d="M18 80 Q8 60 16 44" fill="none" stroke="{O}" stroke-width="1.2" opacity=".0"/>
<rect x="38" y="30" width="56" height="30" rx="15" fill="#F6CE7E" {s()}/>
<ellipse cx="94" cy="45" rx="7" ry="14" fill="#E9B45E" {s()}/>
{dots([(91,38),(96,42),(92,48),(97,51),(94,44)],2.4,'#F05A28')}
{face(62, 44, d=9, k=0.8)}
'''), "герой: блин, свёрнутый трубочкой, с красной икрой | сцена: едет в расписных купеческих санях по зимней дороге")

# 10 Сакура — розовый сакура-моти в листе сидит под цветущей веткой
I["cafe-sakura-kubinka"] = (svg2("#FFF0F6", "#E7A6D0", f'''
<path d="M0 30 Q40 22 70 8" fill="none" stroke="#6B4A3A" stroke-width="5" stroke-linecap="round"/>
<path d="M40 22 Q46 34 44 40" fill="none" stroke="#6B4A3A" stroke-width="3" stroke-linecap="round"/>
{''.join(f'<g transform="translate({x} {y})"><circle r="6" fill="#FFC2DA" {W(1.8)}/><circle r="2" fill="#E5487D"/></g>' for x,y in [(14,26),(30,18),(52,14),(44,40),(66,10)])}
<path d="M90 30 q4 -4 6 0 q-3 4 -6 0Z M104 52 q4 -4 6 0 q-3 4 -6 0Z M22 60 q4 -4 6 0 q-3 4 -6 0Z" fill="#FF9FC2"/>
<ellipse cx="64" cy="112" rx="44" ry="8" fill="#C784B8" opacity=".5"/>
<path d="M24 102 Q20 70 52 56 Q88 46 106 78 Q112 96 98 106Z" fill="#5FAE52" {s()}/>
<path d="M30 98 Q64 66 104 84" fill="none" stroke="#3E8A36" stroke-width="2.6"/>
<ellipse cx="66" cy="84" rx="30" ry="24" fill="#FFB3CC" {s()}/>
<path d="M52 66 q4 -6 8 0 q-4 5 -8 0Z" fill="#FFE1EC" {W(1.6)}/>
{face(66, 86, d=10, k=0.9)}
'''), "герой: розовый пирожок сакура-моти в зелёном листе | сцена: сидит под веткой цветущей сакуры, и лепестки падают ему на макушку")

# 11 Парус — рогалик с повидлом стоит у штурвала лодочки под белым парусом
I["cafe-parus-protvino"] = (svg2("#E6F7FF", "#3FA0D8", f'''
<path d="M0 98 Q16 92 32 98 T64 98 T96 98 T128 98 V128 H0Z" fill="#2F7FC8" {s()}/>
<path d="M16 86 H112 L100 106 H28Z" fill="#B0703A" {s()}/>
<path d="M22 94 H106" stroke="#8A5228" stroke-width="2.4"/>
<path d="M78 86 V16" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>
<path d="M80 18 Q112 46 82 80Z" fill="#FFFFFF" {s()}/>
<path d="M78 16 l12 4 l-12 4Z" fill="#E5484D" {W(2)}/>
<g transform="translate(48 86) scale(1.5) translate(-51 -84)"><path d="M30 84 Q30 54 52 50 Q74 54 72 84Z" fill="#F0B65A" {s()}/>
<path d="M36 62 Q52 56 68 62 M34 72 Q52 66 70 72" fill="none" stroke="#C47A2E" stroke-width="2.6"/>
<path d="M44 52 Q52 46 60 52 Q52 58 44 52Z" fill="#C2264A" {W(2)}/>
{face(51, 70, d=7, k=0.75)}</g>
'''), "герой: рогалик с повидлом | сцена: плывёт на палубе деревянной лодочки под белым парусом с красным флажком")

# 12 Бела Кава — кубик рафинада ныряет с блюдца в белую чашку кофе
I["cafe-bela-kava-fryazino"] = (svg2("#FFF4E6", "#B88458", f'''
<ellipse cx="58" cy="114" rx="50" ry="10" fill="#FFFFFF" {s()}/>
<path d="M14 80 H98 Q96 112 56 112 Q16 112 14 80Z" fill="#FFFFFF" {s()}/>
<path d="M98 86 Q116 86 114 98 Q112 108 94 106" fill="none" stroke="{O}" stroke-width="9"/>
<path d="M98 86 Q116 86 114 98 Q112 108 94 106" fill="none" stroke="#FFFFFF" stroke-width="4"/>
<ellipse cx="56" cy="80" rx="42" ry="9" fill="#7A4524" {s()}/>
<ellipse cx="56" cy="80" rx="30" ry="5" fill="#C69468"/>
{dots([(30,66),(84,64),(40,58),(76,56)],3,'#9A6038')}
<g transform="rotate(18 62 38)">
<rect x="38" y="14" width="48" height="48" rx="7" fill="#FFFFFF" {s()}/>
<path d="M38 24 l10 -10 h38 l-10 10Z" fill="#F1ECE4" {W(2.4)}/>
{dots([(46,54),(78,24),(54,28),(80,50)],1.6,'#D8D2C8')}
{face(62, 40, d=9, k=0.9)}
</g>
<path d="M100 26 Q108 18 116 24 M104 42 Q112 38 118 44" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
'''), "герой: кубик сахара-рафинада | сцена: ныряет с края блюдца в белую чашку кофе, разбрызгивая капли")
# 13 Фламинго — розовое пирожное-купол на одной ножке, как фламинго, среди конфетти
I["cafe-flamingo-klin"] = (svg2("#E8FFF6", "#5CCDA8", f'''
{''.join(f'<rect x="{x}" y="{y}" width="6" height="3" rx="1" fill="{c}" transform="rotate({r} {x} {y})"/>' for x,y,c,r in [(16,24,'#FF7AA8',20),(30,12,'#FFD43A',-30),(100,20,'#6C8CFF',40),(112,40,'#FF9A3C',-10),(18,52,'#B47AE8',60),(98,60,'#FFD43A',15)])}
<ellipse cx="64" cy="114" rx="22" ry="5" fill="#2F8F70" opacity=".4"/>
<path d="M64 84 V112 M64 98 Q74 94 76 84" fill="none" stroke="#F06A98" stroke-width="4" stroke-linecap="round"/>
<path d="M58 112 H72" stroke="#F06A98" stroke-width="4" stroke-linecap="round"/>
<rect x="30" y="74" width="68" height="12" rx="4" fill="#8A5A3A" {s()}/>
<path d="M30 76 Q30 24 64 22 Q98 24 98 76Z" fill="#FF8DB5" {s()}/>
<path d="M40 40 Q46 30 56 28" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".8"/>
<circle cx="64" cy="20" r="6" fill="#E5484D" {s()}/>
{face(64, 56, d=11, k=1.0)}
'''), "герой: розовое пирожное-купол с зеркальной глазурью | сцена: стоит на одной тонкой ножке, как фламинго, среди праздничного конфетти")

# 14 PepePizza — прямоугольный ломтик римской пиццы катается на скейтборде по рампе
I["cafe-pepepizza-aprelevka"] = (svg2("#FFEFD8", "#FF8A4A", f'''
<path d="M0 128 V96 Q40 96 70 120 L74 128Z" fill="#5A7BD8" {s()}/>
<path d="M128 128 V70 Q100 70 92 128Z" fill="#5A7BD8" {s()}/>
<g transform="rotate(-18 60 58)">
<rect x="26" y="30" width="68" height="46" rx="6" fill="#F4C064" {s()}/>
<rect x="32" y="36" width="56" height="34" rx="4" fill="#E5533A"/>
<path d="M34 44 Q44 40 50 46 Q60 52 70 44 Q80 40 86 46" fill="none" stroke="#FFE7A0" stroke-width="5" stroke-linecap="round"/>
<g fill="#C9A27A" {W(1.8)}><path d="M38 60 a5 5 0 0 1 10 0Z"/><path d="M74 62 a5 5 0 0 1 10 0Z"/></g>
{face(60, 56, d=9, k=0.85)}
<rect x="22" y="84" width="76" height="7" rx="3.5" fill="#2E2A3A" {s()}/>
<circle cx="36" cy="96" r="5" fill="#FFD43A" {s()}/><circle cx="84" cy="96" r="5" fill="#FFD43A" {s()}/>
<path d="M44 76 V84 M76 76 V84" stroke="{O}" stroke-width="3.6" stroke-linecap="round"/>
</g>
<path d="M104 30 h12 M100 42 h14" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
'''), "герой: прямоугольный ломтик римской пиццы с грибами | сцена: катается на скейтборде по синей рампе")

# 15 CrazyBrothers — три наггетса-братца корчат рожицы в бумажной коробочке-лодочке
I["cafe-crazy-brothers-domodedovo"] = (svg2("#F3FFD9", "#A6D84A", f'''
<path d="M14 80 H114 L104 116 H24Z" fill="#E5484D" {s()}/>
<path d="M22 92 H106 M26 104 H102" stroke="#FFFFFF" stroke-width="3"/>
<path d="M18 74 Q16 46 40 44 Q60 48 54 74Z" fill="#E7A23B" {s()}/>
<path d="M50 72 Q46 34 66 30 Q88 32 80 74Z" fill="#F0B04A" {s()}/>
<path d="M76 74 Q76 48 96 46 Q116 50 110 74Z" fill="#E39A30" {s()}/>
{dots([(28,54),(44,66),(60,42),(74,56),(92,58),(102,68)],1.8,'#B86E1E')}
{eye(30, 60, 0.75)}{eye(42, 58, 0.75)}
<path d="M30 68 Q36 72 42 68" fill="none" {W(2.2)}/><path d="M35 70 v4" stroke="#FF7FA8" stroke-width="3.4" stroke-linecap="round"/>
<path d="M58 46 l6 4 M70 50 l6 -4" {W(2.4)}/><circle cx="61" cy="53" r="2.4" fill="{O}"/><circle cx="73" cy="53" r="2.4" fill="{O}"/>
<ellipse cx="67" cy="63" rx="4" ry="5" fill="{O}"/>
{eye(88, 60, 0.7)}<circle cx="102" cy="58" r="4.6" fill="#fff" {W(2)}/><circle cx="103" cy="59" r="2" fill="{O}"/>
<path d="M88 68 Q95 64 102 68" fill="none" {W(2.2)}/>
'''), "герой: три наггетса-братца | сцена: корчат смешные рожицы, сидя рядком в красной бумажной коробочке")

# 16 Чайхана Бухара — три пухлых манты сидят на бухарском ковре под бирюзовым куполом
I["cafe-buhara-lobnya"] = (svg2("#E3F8FF", "#3AAFC8", f'''
<path d="M30 52 Q30 14 64 10 Q98 14 98 52Z" fill="#2BB3B8" {s()}/>
<path d="M44 52 V30 M64 52 V14 M84 52 V30" stroke="#1C8A90" stroke-width="2.4"/>
<path d="M64 10 V2" stroke="#F2C14E" stroke-width="3"/>
<rect x="22" y="52" width="84" height="10" fill="#F2C14E" {s()}/>
<path d="M4 128 L16 88 H112 L124 128Z" fill="#B3263A" {s()}/>
<path d="M14 98 H114 M10 112 H118" stroke="#F2C14E" stroke-width="2.6"/>
<g fill="#1F3E9A">{''.join(f'<path d="M{x} 105 l5 -5 l5 5 l-5 5Z"/>' for x in (22, 42, 62, 82, 100))}</g>
<g {s()} fill="#FFF4E0">
<path d="M18 96 Q16 72 36 64 Q40 58 44 64 Q60 72 56 96Z"/>
<path d="M48 92 Q44 62 64 54 Q68 48 72 54 Q90 62 84 92Z"/>
<path d="M76 96 Q72 72 88 64 Q92 58 96 64 Q114 72 110 96Z"/>
</g>
<path d="M38 66 L40 76 M66 56 L68 68 M90 66 L92 76" stroke="#D8C8A8" stroke-width="2"/>
{face(37, 84, d=6, k=0.6)}{face(66, 78, d=7, k=0.7)}{face(93, 84, d=6, k=0.6)}
'''), "герой: три пухлых манты-тройняшки | сцена: сидят на бухарском ковре под бирюзовым куполом с золотым шпилем")

# 17 Господа Ковбои — жестяная кружка печёных бобов у походного костра в прерии под звёздами
I["cafe-gospoda-kovboi-aprelevka"] = (svg2("#B58ADF", "#3E2F78", f'''
{sparkle(20, 24, 4)}{sparkle(104, 18, 3)}{sparkle(60, 12, 2.6)}
<path d="M0 100 Q30 92 64 98 Q96 104 128 94 V128 H0Z" fill="#C97A3A"/>
<path d="M110 96 V62 M110 74 Q120 74 120 64 M110 82 Q100 82 100 72" fill="none" stroke="#3E8A36" stroke-width="7" stroke-linecap="round"/>
<path d="M8 112 L30 104 M12 104 L28 114" stroke="#7A4A22" stroke-width="5" stroke-linecap="round"/>
<path d="M12 106 Q10 88 20 82 Q20 92 26 90 Q24 80 32 76 Q34 94 28 106Z" fill="#FF9A3C" {s()}/>
<path d="M18 104 Q18 96 22 92 Q24 100 26 100" fill="#FFD84A"/>
<path d="M84 60 Q102 60 100 76 Q98 90 82 88" fill="none" stroke="{O}" stroke-width="9"/>
<path d="M84 60 Q102 60 100 76 Q98 90 82 88" fill="none" stroke="#5B8FD8" stroke-width="4"/>
<path d="M38 52 H88 V104 Q88 112 80 112 H46 Q38 112 38 104Z" fill="#5B8FD8" {s()}/>
<ellipse cx="63" cy="52" rx="25" ry="7" fill="#FFFFFF" {s()}/>
<ellipse cx="63" cy="50" rx="19" ry="4" fill="#C2402A"/>
{''.join(f'<ellipse cx="{x}" cy="{y}" rx="4" ry="2.8" fill="#8A3A1E" {W(1.4)}/>' for x,y in [(52,46),(62,42),(72,46),(58,50),(68,50),(64,38)])}
{face(63, 80, d=10, k=0.95)}
'''), "герой: жестяная кружка печёных бобов в томате | сцена: греется у походного костра в прерии под звёздным небом рядом с кактусом")

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
