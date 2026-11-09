"""Иконки робота fun (2026-11-09, 6-й проход): 59 мест из tools/add_fun_1109g.py.
Каждая придумана и нарисована отдельно (правило абсолютной уникальности): у 19 филиалов «Ирбиса» — 19 разных
предметов театрального закулисья, у остальных — свой предмет игровой/квеста/музея. Сюжеты сверены с subjects.txt.
Запуск: python3 tools/icons_fun_1109g.py  (пишет icons-src/<id>.svg и печатает строки для subjects.txt)"""
import os
from draw_icons import s, face, sparkle, eye, O

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")


def svg(a, b, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


def kid(x, y, k=1.0, hair="#6B3F23", shirt="#4FA3E0"):
    """маленькая голова малыша с чёлкой"""
    return (f'<circle cx="{x}" cy="{y}" r="{10*k:.1f}" fill="#FFD9B8" {W(2.4)}/>'
            f'<path d="M{x-10*k:.1f} {y-1*k:.1f} Q{x-8*k:.1f} {y-12*k:.1f} {x} {y-11*k:.1f} Q{x+9*k:.1f} {y-11*k:.1f} {x+10*k:.1f} {y-2*k:.1f} Q{x+2*k:.1f} {y-7*k:.1f} {x-10*k:.1f} {y-1*k:.1f}Z" fill="{hair}" {W(2)}/>'
            + face(x, y + 1 * k, d=4 * k, k=0.42 * k))


I = {}

# ---------------- «Ирбис»: 19 филиалов — 19 разных предметов театра ----------------
I["irbis-baumanskaya"] = ("#7A2E4E", "#2B0E22",
    "ряд круглых лампочек рампы с мордашками по краю сцены",
    "лампочки зажигаются по очереди, встречая выход артиста, а за ними блестят доски пустой сцены",
    f'<path d="M0 96 H128 V128 H0Z" fill="#9A5B32" {W(3)}/>'
    + "".join(f'<path d="M{x} 100 L{x-6} 128" stroke="#7A4425" stroke-width="2"/>' for x in (20, 46, 72, 98, 124)) +
    f'<rect x="-2" y="82" width="132" height="16" fill="#3B3355"/>'
    + "".join(f'<path d="M{x-14} 82 Q{x} 56 {x+14} 82Z" fill="#FFE68A" opacity=".35"/>' for x in (16, 40, 64, 88, 112))
    + "".join(f'<circle cx="{x}" cy="78" r="10" fill="{c}" {W(2.8)}/>' + face(x, 78, d=3.6, k=0.42)
              for x, c in ((16, "#FFF3B0"), (40, "#FFE066"), (64, "#FFD23F"), (88, "#FFE066"), (112, "#FFF3B0"))) +
    f'<path d="M-2 4 Q20 30 40 10 Q64 34 88 10 Q108 30 130 4 V-2 H-2Z" fill="#C8314E" {W(3)}/>'
    + sparkle(64, 46, 6, "#FFE68A") + sparkle(30, 50, 3.5, "#FFE68A") + sparkle(98, 50, 3.5, "#FFE68A"))

I["irbis-belorusskaya"] = ("#E9FFF6", "#79D3B4",
    "круглая розовая пуховка для пудры с атласной петелькой",
    "подпрыгивает над раскрытой золотой пудреницей и выбивает облачко пудры",
    f'<ellipse cx="64" cy="108" rx="42" ry="10" fill="#E0B24A" {W(3)}/>'
    f'<ellipse cx="64" cy="104" rx="34" ry="7" fill="#F6E2CF" {W(2.4)}/>'
    f'<path d="M30 104 Q28 72 64 70 Q100 72 98 104" fill="none" stroke="#E0B24A" stroke-width="5"/>'
    f'<ellipse cx="64" cy="70" rx="30" ry="4" fill="#B9E7F5" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".9"/>' for x, y, r in ((40, 94, 6), (52, 98, 5), (82, 95, 6), (92, 99, 4), (66, 92, 4))) +
    f'<ellipse cx="64" cy="46" rx="30" ry="24" fill="#FF9EC4" {W(3.2)}/>'
    f'<path d="M38 52 Q64 66 90 52" fill="none" stroke="#F06A9E" stroke-width="2.6"/>'
    f'<path d="M58 22 Q64 8 70 22" fill="none" stroke="#F06A9E" stroke-width="4"/>'
    + face(64, 42, d=9, k=0.8) + sparkle(102, 30, 5) + sparkle(24, 32, 4))

I["irbis-solntsevo"] = ("#F4FFD9", "#98C858",
    "деревянная кибитка бродячих артистов с откидной сценой и полосатым навесом",
    "откинула борт-сцену на летней поляне, над крышей трепещут флажки",
    f'<path d="M-2 104 Q64 92 130 104 V130 H-2Z" fill="#7DBE4E" {W(3)}/>'
    f'<path d="M20 50 H96 V92 H20Z" fill="#E7A35B" {W(3.2)}/>'
    f'<path d="M16 50 Q58 22 100 50Z" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M{16+i*14} 50 Q{23+i*14} {40 if 0<i<5 else 46} {30+i*14} 50Z" fill="#E8434A"/>' for i in range(0, 6, 2)) +
    f'<path d="M30 58 H86 V86 H30Z" fill="#4A2A5A" {W(2.6)}/>'
    f'<path d="M30 58 Q40 74 34 86 H30Z M86 58 Q76 74 82 86 H86Z" fill="#C8314E" {W(2)}/>'
    + sparkle(58, 70, 7, "#FFD23F") +
    f'<path d="M96 70 L120 92 L96 92Z" fill="#C98B4E" {W(2.8)}/>'
    f'<circle cx="38" cy="98" r="10" fill="#8A5A2B" {W(3)}/><circle cx="38" cy="98" r="3" fill="{O}"/>'
    f'<circle cx="80" cy="98" r="10" fill="#8A5A2B" {W(3)}/><circle cx="80" cy="98" r="3" fill="{O}"/>'
    f'<path d="M58 30 V8" {W(2.6)}/><path d="M58 8 L74 13 L58 18Z" fill="#4FA3E0" {W(2)}/>'
    + face(58, 44, d=7, k=0.55, mouth=False))

I["irbis-gorchakova"] = ("#FFFBEA", "#F7C948",
    "круглое пятно света прожектора с мордашкой",
    "бежит по тёмной сцене, догоняя маленькую фигурку артиста в поклоне",
    f'<path d="M0 0 H128 V128 H0Z" fill="#2E2A4A"/>'
    f'<path d="M-2 92 H130 V130 H-2Z" fill="#4B3A6B" {W(3)}/>'
    f'<path d="M110 -4 L44 92 H92 Z" fill="#FFF3B0" opacity=".35"/>'
    f'<ellipse cx="66" cy="96" rx="34" ry="12" fill="#FFF3B0" {W(3)}/>'
    + face(66, 94, d=8, k=0.6) +
    f'<path d="M100 92 Q104 70 110 66 Q116 70 118 92Z" fill="#E8434A" {W(2.4)}/>'
    f'<circle cx="110" cy="60" r="6" fill="#FFD9B8" {W(2.2)}/>'
    f'<path d="M30 100 q-6 -3 -12 0 M30 106 q-8 -2 -14 2" fill="none" stroke="#FFF3B0" stroke-width="2.4" stroke-linecap="round"/>'
    + sparkle(30, 30, 4, "#FFE68A") + sparkle(60, 20, 3, "#FFE68A") + sparkle(20, 60, 3, "#FFE68A"))

I["irbis-kolomenskaya"] = ("#F1E9FF", "#A88BE6",
    "деревянный шарнирный манекен художника с шариками-суставами",
    "делает актёрский поклон с рукой на сердце на квадратной подставке",
    f'<rect x="34" y="104" width="60" height="12" rx="3" fill="#C98B4E" {W(3)}/><path d="M64 104 V92" {W(4)}/>'
    f'<path d="M52 92 L46 66 M76 92 L72 66" stroke="#E8BE86" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M52 92 L46 66 M76 92 L72 66" fill="none" {W(2.4)}/>'
    f'<path d="M44 66 Q42 40 58 34 L74 36 Q80 50 76 66Z" fill="#E8BE86" {W(3)}/>'
    f'<path d="M58 40 L40 54 L56 60" fill="none" stroke="#E8BE86" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M58 40 L40 54 L56 60" fill="none" {W(2.2)}/>'
    f'<path d="M74 40 Q92 46 100 30" fill="none" stroke="#E8BE86" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M74 40 Q92 46 100 30" fill="none" {W(2.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="#B9773E" {W(2)}/>' for x, y in ((40, 54), (88, 42), (46, 66), (74, 66), (52, 92), (76, 92))) +
    f'<ellipse cx="80" cy="24" rx="13" ry="15" fill="#E8BE86" {W(3)}/>'
    + face(80, 26, d=5, k=0.5) +
    f'<path d="M56 56 q-3 -4 0 -6 q3 2 0 6Z" fill="#E8434A"/>' + sparkle(24, 30, 5) + sparkle(108, 80, 4))

I["irbis-preobrazhenskaya"] = ("#CFE3FF", "#3F5CB8",
    "квадратный сценический люк с откинутой крышкой-мордашкой",
    "из открытого люка в полу сцены на пружинке выпрыгивает жёлтая звёздочка-артистка",
    f'<path d="M-2 70 H130 V130 H-2Z" fill="#8A5A3A" {W(3)}/>'
    + "".join(f'<path d="M-2 {y} H130" stroke="#6B4027" stroke-width="2"/>' for y in (84, 100, 116)) +
    f'<path d="M34 92 L94 92 L104 116 L24 116Z" fill="#1E1630" {W(3)}/>'
    f'<path d="M34 92 L94 92 L88 56 L40 56Z" fill="#B97A4A" {W(3)}/>'
    f'<path d="M48 66 H80" stroke="#8A5A3A" stroke-width="2"/>' + face(64, 76, d=8, k=0.6) +
    f'<path d="M64 108 q-8 -4 0 -8 q8 -4 0 -8 q-8 -4 0 -8 q8 -4 0 -8" fill="none" stroke="#C9D3E3" stroke-width="3"/>'
    f'<path d="M64 6 L70 20 L85 21 L73 31 L77 46 L64 38 L51 46 L55 31 L43 21 L58 20Z" fill="#FFD23F" {W(2.8)}/>'
    + face(64, 28, d=4.5, k=0.42) + sparkle(98, 30, 4) + sparkle(28, 40, 3))

I["irbis-krasnye-vorota"] = ("#FFE3F1", "#C46AB5",
    "чёрная театральная дым-машина с соплом и кнопкой",
    "выпускает по сцене стелющийся белый туман, в котором плывёт облачко-сердечко",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#6B4A7A" {W(3)}/>'
    f'<rect x="10" y="66" width="42" height="34" rx="6" fill="#3B3355" {W(3)}/>'
    f'<path d="M52 76 H64 V90 H52" fill="#5A5470" {W(2.6)}/>'
    f'<circle cx="22" cy="74" r="3.5" fill="#E8434A"/><path d="M14 92 H48" stroke="#5A5470" stroke-width="2"/>'
    + face(31, 84, d=7, k=0.55) +
    f'<path d="M66 94 Q72 76 88 82 Q96 66 110 76 Q126 74 124 92 Q130 104 112 106 H70 Q60 104 66 94Z" fill="#fff" {W(2.8)}/>'
    f'<path d="M20 106 Q40 98 60 106 Q80 98 100 106 Q116 100 130 106" fill="none" stroke="#fff" stroke-width="5" opacity=".85"/>'
    f'<path d="M92 44 q-8 -10 -14 -2 q-6 8 14 20 q20 -12 14 -20 q-6 -8 -14 2Z" fill="#FF7FA8" {W(2.6)}/>'
    + sparkle(40, 36, 5) + sparkle(112, 30, 4))

I["irbis-lermontovsky"] = ("#FFF4D6", "#E3A23B",
    "холщовый мешок-противовес с песком на канате колосников",
    "опускается вниз, а занавес на другом конце каната ползёт вверх",
    f'<circle cx="64" cy="10" r="10" fill="#9AA8BB" {W(3)}/><circle cx="64" cy="10" r="3" fill="{O}"/>'
    f'<path d="M54 10 V52 M74 10 V40" {W(3)}/>'
    f'<path d="M74 40 H124 V128 H74Z" fill="#C8314E" {W(3)}/>'
    + "".join(f'<path d="M{x} 42 V128" stroke="#9E2240" stroke-width="2.4"/>' for x in (86, 98, 110)) +
    f'<path d="M74 40 H124" stroke="#E0B24A" stroke-width="5"/>'
    f'<path d="M98 30 l-4 6 h8Z" fill="{O}"/><path d="M98 24 V32" {W(2.4)}/>'
    f'<path d="M30 60 Q28 52 40 52 H68 Q80 52 78 60 L82 104 Q82 112 70 112 H38 Q26 112 26 104Z" fill="#D9C08E" {W(3.2)}/>'
    f'<path d="M40 52 Q54 62 68 52" fill="none" {W(2.4)}/>'
    + face(54, 82, d=9, k=0.75) +
    f'<path d="M30 116 q4 -4 8 0 M58 118 q4 -4 8 0" fill="none" stroke="#C9A26A" stroke-width="2.2"/>'
    f'<path d="M14 66 v14 m-5 -5 l5 5 l5 -5" fill="none" {W(2.6)}/>')

I["irbis-myakinino"] = ("#E2FBFF", "#5CC3D6",
    "складной стул режиссёра с парусиновой спинкой и надписью «РЕЖ»",
    "надел клетчатую кепку и следит из зала за маленькой освещённой сценой",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#3F7F8C" {W(3)}/>'
    f'<path d="M84 50 H126 V96 H84Z" fill="#2E2A4A" {W(3)}/><ellipse cx="105" cy="92" rx="16" ry="4" fill="#FFF3B0"/>'
    f'<path d="M84 50 Q96 60 92 96 H84Z M126 50 Q114 60 118 96 H126Z" fill="#C8314E" {W(2)}/>'
    f'<path d="M30 62 L66 112 M66 62 L30 112" stroke="#B9773E" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M30 62 L66 112 M66 62 L30 112" fill="none" {W(2)}/>'
    f'<rect x="24" y="78" width="48" height="10" rx="3" fill="#2F6FB3" {W(2.8)}/>'
    f'<path d="M28 78 V34 M68 78 V34" stroke="#B9773E" stroke-width="5" stroke-linecap="round"/>'
    f'<rect x="24" y="34" width="48" height="28" rx="3" fill="#2F6FB3" {W(3)}/>'
    f'<text x="48" y="58" font-family="Arial" font-weight="bold" font-size="9" fill="#fff" text-anchor="middle">РЕЖ</text>'
    + face(48, 44, d=8, k=0.55, mouth=False) +
    f'<path d="M30 30 Q34 16 50 16 Q66 16 68 30Z" fill="#9AA8BB" {W(2.6)}/><path d="M66 30 H78" {W(3.4)}/>'
    f'<path d="M38 20 L44 30 M50 17 V30 M60 20 L56 30" stroke="#6B7A8F" stroke-width="1.6"/>')

I["irbis-novogireevo"] = ("#FFE4E4", "#E26A6A",
    "широкополая синяя шляпа с длинным белым пером",
    "сама снимается в театральном поклоне над половицами сцены, перо описывает дугу",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#A86A44" {W(3)}/>'
    f'<path d="M20 84 Q16 70 40 64 Q64 58 92 64 Q116 70 110 84 Q64 98 20 84Z" fill="#2F4F9E" {W(3.2)}/>'
    f'<path d="M40 66 Q42 36 66 34 Q90 36 90 64 Q64 72 40 66Z" fill="#3D63BF" {W(3)}/>'
    f'<path d="M42 62 Q66 70 89 62" fill="none" stroke="#FFD23F" stroke-width="5"/>'
    f'<path d="M84 58 Q100 20 82 6 Q92 24 76 44 Q86 30 74 22 Q80 40 70 52" fill="#fff" {W(2.6)}/>'
    + face(64, 50, d=8, k=0.6) +
    f'<path d="M14 40 Q24 20 46 18" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="4 5"/>'
    + sparkle(110, 36, 5) + sparkle(24, 96, 3.5))

I["irbis-novokosino"] = ("#F6F6FA", "#9AA0B8",
    "пара белых перчаток мима",
    "упираются раскрытыми ладонями в невидимое стекло, по которому бегут голубые блики",
    f'<path d="M88 4 L108 124 M98 4 L118 124" stroke="#BFE3FF" stroke-width="5" opacity=".9"/>'
    f'<path d="M64 0 V128" stroke="#C9E7FF" stroke-width="3" stroke-dasharray="6 6"/>'
    + "".join(
        f'<g transform="translate({dx} {dy})"><path d="M0 36 Q-4 6 4 4 Q8 3 9 18 L10 -2 Q12 -8 17 -4 L18 16 L20 -4 Q24 -9 28 -2 L28 18 L31 4 Q36 0 37 8 L36 40 Q34 58 18 60 Q2 60 0 36Z" fill="#fff" {W(3)}/>'
        f'<path d="M4 58 H32 V70 H4Z" fill="#E8E8F0" {W(2.6)}/></g>' for dx, dy in ((22, 22), (66, 50))) +
    face(40, 56, d=6, k=0.5) + face(84, 84, d=6, k=0.5, mouth=False) +
    f'<path d="M80 92 q4 3 8 0" fill="none" {W(2.4)}/>' + sparkle(108, 22, 5, "#BFE3FF") + sparkle(20, 104, 4, "#BFE3FF"))

I["irbis-oktyabrskoe-pole"] = ("#FFF0E2", "#E9A27A",
    "макет сцены-шкатулка с порталом и крошечными бархатными кулисами",
    "стоит на столе художника-постановщика, внутри картонный домик и солнышко на ниточке",
    f'<path d="M-2 100 H130 V130 H-2Z" fill="#C98B4E" {W(3)}/>'
    f'<path d="M18 28 H110 V102 H18Z" fill="#7A3E5A" {W(3.2)}/>'
    f'<path d="M28 40 H100 V96 H28Z" fill="#FFF6D6" {W(2.6)}/>'
    f'<path d="M18 28 Q64 10 110 28" fill="#E0B24A" {W(3)}/>'
    f'<path d="M28 40 Q40 64 32 96 H28Z M100 40 Q88 64 96 96 H100Z" fill="#C8314E" {W(2)}/>'
    f'<path d="M50 96 V74 L62 64 L74 74 V96Z" fill="#9AD0F5" {W(2.4)}/><path d="M58 96 V84 H66 V96" fill="#fff" {W(2)}/>'
    f'<path d="M84 40 V52" {W(1.6)}/><circle cx="84" cy="58" r="6" fill="#FFD23F" {W(2.2)}/>'
    + face(64, 84, d=4, k=0.35) +
    f'<rect x="18" y="102" width="92" height="6" fill="#5A2A44"/>' + sparkle(116, 16, 4) + sparkle(12, 60, 3.5))

I["irbis-otradnoe"] = ("#D8FBF6", "#3FB5A6",
    "тростевая кукла-девочка в широком платье на двух длинных тростях-руках",
    "машет зрителям над ширмой, а снизу её ведёт рука кукловода",
    f'<path d="M-2 92 H130 V130 H-2Z" fill="#2F6F86" {W(3)}/>'
    + "".join(f'<path d="M{x} 92 V130" stroke="#24566A" stroke-width="2"/>' for x in (24, 52, 80, 108)) +
    f'<path d="M64 96 V128" stroke="#8A5A2B" stroke-width="5"/><path d="M40 52 L28 128 M92 52 L100 128" stroke="#5A4630" stroke-width="2.4"/>'
    f'<path d="M46 50 Q64 40 82 50 L92 92 H36Z" fill="#F2A541" {W(3)}/>'
    f'<path d="M40 70 Q64 80 88 70" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 5"/>'
    f'<path d="M48 52 Q40 46 38 50 M80 52 Q90 40 94 46" fill="none" stroke="#F2A541" stroke-width="6" stroke-linecap="round"/>'
    f'<circle cx="64" cy="32" r="15" fill="#FFE3C8" {W(3)}/>'
    f'<path d="M50 28 Q52 12 64 14 Q78 12 80 28 Q72 18 64 22 Q56 18 50 28Z" fill="#B5432F" {W(2.2)}/>'
    f'<circle cx="50" cy="36" r="4" fill="#B5432F" {W(1.6)}/><circle cx="78" cy="36" r="4" fill="#B5432F" {W(1.6)}/>'
    + face(64, 33, d=5.5, k=0.5) + sparkle(108, 22, 5) + sparkle(18, 40, 4))

I["irbis-tverskaya"] = ("#FFE9C2", "#B8322F",
    "золочёная театральная ложа-балкончик с красным бархатным барьером",
    "из неё выглядывает девочка в шляпке с цветком и громко хлопает спектаклю",
    f'<path d="M0 0 H128 V40 H0Z" fill="#8E1F2B" opacity=".5"/>'
    f'<path d="M20 70 Q64 56 108 70 L104 104 Q64 118 24 104Z" fill="#E0B24A" {W(3.2)}/>'
    f'<path d="M24 72 Q64 60 104 72 L102 84 Q64 74 26 84Z" fill="#C8314E" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{96 + abs(64-x)//8}" r="4" fill="#F7D774" {W(1.8)}/>' for x in (36, 50, 64, 78, 92)) +
    f'<circle cx="64" cy="50" r="16" fill="#FFD9B8" {W(3)}/>'
    f'<path d="M44 42 Q46 24 64 24 Q82 24 84 42 Z" fill="#6FC3E8" {W(2.8)}/><path d="M38 44 H90" {W(3.6)}/>'
    f'<circle cx="80" cy="30" r="5" fill="#FF7FA8" {W(2)}/>'
    + face(64, 54, d=6, k=0.55) +
    f'<path d="M40 66 l-8 -8 m4 12 l-10 -2 M88 66 l8 -8 m-4 12 l10 -2" {W(2.4)}/>'
    f'<ellipse cx="48" cy="72" rx="6" ry="5" fill="#FFD9B8" {W(2.4)}/><ellipse cx="80" cy="72" rx="6" ry="5" fill="#FFD9B8" {W(2.4)}/>')

I["irbis-vernadskogo"] = ("#DDF6FF", "#5B5FC7",
    "поворотный круг сцены, разделённый на день и ночь",
    "вращается по стрелкам: на дневной половине — деревце под солнцем, на ночной — домик под месяцем",
    f'<ellipse cx="64" cy="84" rx="54" ry="26" fill="#8A5A3A" {W(3)}/>'
    f'<path d="M10 84 A54 26 0 0 0 118 84Z" fill="#6B4027"/>'
    f'<ellipse cx="64" cy="78" rx="54" ry="26" fill="#C98B4E" {W(3.2)}/>'
    f'<path d="M64 52 V104" {W(2.6)}/>'
    f'<path d="M14 78 A50 22 0 0 1 64 56 V100 A50 22 0 0 1 14 78Z" fill="#FFE9A0" opacity=".6"/>'
    f'<path d="M64 56 A50 22 0 0 1 114 78 A50 22 0 0 1 64 100Z" fill="#3E4AA0" opacity=".6"/>'
    f'<path d="M36 76 V58" stroke="#8A5A2B" stroke-width="4"/><circle cx="36" cy="52" r="10" fill="#7CD26E" {W(2.6)}/>'
    f'<circle cx="24" cy="32" r="7" fill="#FFD23F" {W(2.4)}/>'
    f'<path d="M82 78 V62 L92 54 L102 62 V78Z" fill="#E8EEF7" {W(2.4)}/><rect x="88" y="66" width="7" height="7" fill="#FFD23F"/>'
    f'<path d="M104 26 a9 9 0 1 0 6 16 a7 7 0 1 1 -6 -16Z" fill="#FFF3B0" {W(2.2)}/>'
    f'<path d="M20 110 Q64 124 108 110" fill="none" {W(2.8)}/><path d="M108 110 l-8 -2 l4 7Z" fill="{O}"/>'
    + face(64, 90, d=8, k=0.5) + sparkle(74, 30, 3.5, "#FFF3B0"))

I["irbis-rechnoy-vokzal"] = ("#E7F3FF", "#7E9CE8",
    "малыш-артист в полётной обвязке с крылышками из марли",
    "летит на тросе высоко над сценой, раскинув руки, а внизу колышется синяя ткань-море",
    f'<path d="M64 -2 V36" stroke="#5B6B8C" stroke-width="2.4"/>'
    f'<path d="M-2 100 Q16 90 32 100 Q48 110 64 100 Q80 90 96 100 Q112 110 130 100 V130 H-2Z" fill="#2F7FC1" {W(3)}/>'
    f'<path d="M-2 112 Q20 104 40 112 Q60 120 80 112 Q100 104 130 112" fill="none" stroke="#9BD3FF" stroke-width="3"/>'
    f'<path d="M50 52 Q30 34 18 44 Q28 56 50 60Z M78 52 Q98 34 110 44 Q100 56 78 60Z" fill="#fff" opacity=".9" {W(2.4)}/>'
    f'<path d="M50 52 H78 L76 74 H52Z" fill="#7C5CC4" {W(2.8)}/>'
    f'<path d="M52 56 L78 70 M76 56 L52 70" stroke="#FFD23F" stroke-width="3"/>'
    f'<path d="M52 72 L44 88 M76 72 L84 88" stroke="#7C5CC4" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M50 56 L26 60 M78 56 L102 60" stroke="#FFD9B8" stroke-width="6" stroke-linecap="round"/>'
    + kid(64, 40, 1.1, hair="#E0A23B") + sparkle(26, 22, 5) + sparkle(104, 22, 4))

I["irbis-skhodnenskaya"] = ("#F2FFE8", "#8FCB6B",
    "театральная ветродуйка — деревянный барабан с натянутой парусиной и ручкой",
    "её крутят за кулисой, и на сцену летят завитки ветра и кленовый листок",
    f'<path d="M-2 106 H130 V130 H-2Z" fill="#9A6A3A" {W(3)}/>'
    f'<path d="M30 106 L40 70 M70 106 L60 70" stroke="#8A5A2B" stroke-width="6" stroke-linecap="round"/>'
    f'<ellipse cx="50" cy="62" rx="30" ry="22" fill="#E7D3A8" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 41 Q{x+3} 62 {x} 83" fill="none" stroke="#B9773E" stroke-width="2.4"/>' for x in (32, 44, 56, 68)) +
    f'<circle cx="50" cy="62" r="5" fill="#8A5A2B" {W(2.2)}/><path d="M50 62 L22 50 L18 58" fill="none" stroke="#8A5A2B" stroke-width="4" stroke-linecap="round"/>'
    + face(50, 66, d=9, k=0.6) +
    f'<path d="M84 46 Q100 40 108 48 Q114 56 104 58 M86 62 Q104 58 118 66 M84 78 Q98 78 106 86 Q110 92 102 92" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M108 24 l4 6 l6 -2 l-2 6 l6 4 l-7 2 l1 7 l-6 -4 l-4 5 l-2 -7 l-7 0 l4 -6 l-4 -5 l7 0Z" fill="#F2803A" {W(2)}/>')

I["irbis-tulskaya"] = ("#E8ECF5", "#6C7896",
    "подвешенный жестяной лист для театрального грома",
    "по нему бьёт войлочная колотушка, и вокруг разлетаются молнии с надписью «БУМ»",
    f'<path d="M40 4 V18 M88 4 V18" {W(2.6)}/>'
    f'<path d="M30 18 H98 Q104 60 96 104 H34 Q26 60 30 18Z" fill="#C9D3E3" {W(3.2)}/>'
    f'<path d="M36 34 Q64 44 92 34 M36 64 Q64 54 92 66 M36 90 Q64 98 92 88" fill="none" stroke="#9AA8BB" stroke-width="2.4"/>'
    + face(64, 60, d=10, k=0.75) +
    f'<path d="M100 96 L118 74" stroke="#8A5A2B" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="96" cy="100" rx="9" ry="7" fill="#E8434A" {W(2.6)}/>'
    f'<path d="M12 40 L22 50 L14 54 L26 66" fill="none" stroke="#FFD23F" stroke-width="4" stroke-linejoin="round"/>'
    f'<path d="M108 20 L114 32 L106 34 L114 46" fill="none" stroke="#FFD23F" stroke-width="4" stroke-linejoin="round"/>'
    f'<text x="22" y="112" font-family="Arial Black,Arial" font-weight="900" font-size="15" fill="#FFD23F" stroke="{O}" stroke-width="1.2">БУМ</text>')

I["irbis-elektrozavodskaya"] = ("#FFF1F8", "#E58BC0",
    "кукла-носок в полоску с пуговичными глазами и красным фетровым языком",
    "надета на руку и разыгрывает сценку над краем стола, напевая нотки",
    f'<path d="M-2 98 H130 V130 H-2Z" fill="#7C5CC4" {W(3)}/>'
    f'<path d="M40 128 L44 74 Q46 40 76 38 Q106 38 104 62 Q102 76 86 76 L84 128Z" fill="#7FD6B8" {W(3.2)}/>'
    + "".join(f'<path d="M{44 if y>60 else 52} {y} Q66 {y-4} {86 if y>60 else 100} {y}" fill="none" stroke="#fff" stroke-width="5"/>' for y in (54, 92, 112)) +
    f'<path d="M104 62 Q92 66 86 76 Q96 80 104 62Z" fill="#E8434A" {W(2.4)}/>'
    f'<circle cx="70" cy="50" r="7" fill="#fff" {W(2.4)}/><circle cx="70" cy="50" r="2" fill="{O}"/>'
    f'<circle cx="88" cy="48" r="7" fill="#fff" {W(2.4)}/><circle cx="88" cy="48" r="2" fill="{O}"/>'
    f'<path d="M102 30 v12 a3.5 2.6 0 1 1 -2 -2.4 V30 l9 -3 v10 a3.5 2.6 0 1 1 -2 -2.4 V28" fill="{O}" stroke="{O}"/>'
    + sparkle(22, 40, 5) + sparkle(116, 84, 3.5))

# ---------------- Развлекательные центры и игровые ----------------
I["zamania-deily-mytishchi"] = ("#FFF9E8", "#F5B54A",
    "радужный игровой парашют-купол из восьми цветных клиньев",
    "двое малышей держат его за края, а под куполом подлетает красный мячик",
    f'<path d="M10 78 Q64 6 118 78Z" fill="#fff" {W(3.2)}/>'
    + "".join(f'<path d="M64 26 L{10+i*13.5} 78 L{23.5+i*13.5} 78Z" fill="{c}"/>'
              for i, c in enumerate(("#E8434A", "#F2803A", "#FFD23F", "#7CD26E", "#3FB5A6", "#4FA3E0", "#7C5CC4", "#F06A9E"))) +
    f'<path d="M10 78 Q64 6 118 78" fill="none" {W(3.2)}/><path d="M10 78 H118" {W(3)}/>'
    + face(64, 54, d=9, k=0.7) +
    f'<circle cx="64" cy="98" r="9" fill="#E8434A" {W(2.6)}/><path d="M64 90 q4 8 0 16" fill="none" stroke="#fff" stroke-width="2"/>'
    + kid(18, 96, 0.9) + kid(110, 96, 0.9, hair="#2B2B2B") +
    f'<path d="M18 86 V78 M110 86 V78" {W(3)}/>' + sparkle(64, 14, 4) + sparkle(98, 112, 3.5))

I["teikaboom-crocus-mall"] = ("#E5F2FF", "#6FA8E8",
    "надувной замок-батут с круглыми башенками в красно-жёлтую полоску",
    "пружинит под малышом, который подлетает выше башен с поднятыми руками",
    f'<path d="M14 112 H114 V122 H14Z" fill="#2F7FC1" {W(3)}/>'
    f'<path d="M20 112 V64 Q20 56 28 56 Q36 56 36 64 V74 H92 V64 Q92 56 100 56 Q108 56 108 64 V112Z" fill="#FFD23F" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 74 V112" stroke="#E8434A" stroke-width="6"/>' for x in (46, 64, 82)) +
    f'<path d="M20 112 V64 Q20 56 28 56 Q36 56 36 64 V74 H92 V64 Q92 56 100 56 Q108 56 108 64 V112Z" fill="none" {W(3.2)}/>'
    f'<path d="M20 60 Q28 44 36 60 M92 60 Q100 44 108 60" fill="#E8434A" {W(2.6)}/>'
    f'<path d="M40 112 Q40 92 64 92 Q88 92 88 112Z" fill="#E8434A" {W(2.8)}/>'
    + face(64, 104, d=7, k=0.5) +
    f'<path d="M54 48 L44 30 M74 48 L84 30" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M54 44 H74 L72 62 H56Z" fill="#7CD26E" {W(2.4)}/>' + kid(64, 34, 0.9, hair="#C26A2B") +
    f'<path d="M50 78 q14 6 28 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4"/>')

I["teikaboom-botanika"] = ("#EAFBF0", "#5FC48A",
    "прозрачная воздушная труба-пылесос для поролоновых мячиков",
    "с шумом втягивает жёлтый мячик снизу и выстреливает им в сетчатую корзину",
    f'<path d="M34 128 V40 Q34 22 52 22 H84" fill="none" stroke="#fff" stroke-width="18" opacity=".7"/>'
    f'<path d="M25 128 V40 Q25 13 52 13 H84 M43 128 V40 Q43 31 52 31 H84" fill="none" {W(3)}/>'
    f'<path d="M84 8 L96 6 V38 L84 36Z" fill="#4FA3E0" {W(2.6)}/>'
    + "".join(f'<circle cx="34" cy="{y}" r="6" fill="{c}" {W(2)}/>' for y, c in ((104, "#FFD23F"), (78, "#E8434A"), (54, "#7C5CC4"))) +
    f'<circle cx="64" cy="22" r="6" fill="#F2803A" {W(2)}/>'
    + face(34, 100, d=3, k=0.32) +
    f'<path d="M80 74 H122 L114 104 H88Z" fill="#fff" opacity=".6" {W(2.8)}/>'
    + "".join(f'<path d="M{x} 74 L{x+4} 104" stroke="#3B3355" stroke-width="1.4"/>' for x in (88, 98, 108)) +
    f'<path d="M84 86 H118 M86 96 H116" stroke="#3B3355" stroke-width="1.4"/>'
    f'<circle cx="104" cy="50" r="7" fill="#FFD23F" {W(2.2)}/><path d="M98 38 q6 -6 12 0" fill="none" stroke="#fff" stroke-width="2.4"/>'
    + face(104, 50, d=3, k=0.32) + sparkle(110, 20, 4))

I["teikaboom-kvartal-west"] = ("#FDEBFF", "#B97ADB",
    "вращающаяся тарелка-карусель для малышей с ручками по краю",
    "крутится, а двое малышей держатся за ручки и визжат от восторга",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#6A4C93" {W(3)}/>'
    f'<path d="M60 104 V86 H68 V104Z" fill="#9AA8BB" {W(2.4)}/>'
    f'<ellipse cx="64" cy="84" rx="48" ry="14" fill="#F06A9E" {W(3.2)}/>'
    f'<ellipse cx="64" cy="80" rx="48" ry="14" fill="#FF9EC4" {W(3)}/>'
    f'<path d="M30 74 V60 M98 74 V60" stroke="#FFD23F" stroke-width="5" stroke-linecap="round"/>'
    + face(64, 84, d=10, k=0.6) + kid(40, 56, 1.0) + kid(88, 56, 1.0, hair="#2B2B2B") +
    f'<path d="M10 70 Q4 58 12 50 M118 70 Q124 58 116 50" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(64, 26, 5) + sparkle(110, 26, 3.5))

I["ambiland-columbus"] = ("#F4FFF6", "#9DDB9A",
    "белый коврик «Твистер» с рядами цветных кругов",
    "стрелка рулетки показывает «правая рука на зелёный», и малыш тянется ладошкой к кругу",
    f'<path d="M10 72 L118 72 L126 124 L2 124Z" fill="#fff" {W(3)}/>'
    + "".join(f'<ellipse cx="{24+c*27+ (r*2)}" cy="{82+r*14}" rx="9" ry="5" fill="{col}" {W(1.8)}/>'
              for r in range(3) for c, col in enumerate(("#E8434A", "#4FA3E0", "#FFD23F", "#2EAA4A"))) +
    face(64, 108, d=8, k=0.45) +
    f'<circle cx="64" cy="36" r="24" fill="#fff" {W(3)}/>'
    f'<path d="M64 36 L64 12 A24 24 0 0 1 88 36Z" fill="#2EAA4A"/><path d="M64 36 L88 36 A24 24 0 0 1 64 60Z" fill="#FFD23F"/>'
    f'<path d="M64 36 L64 60 A24 24 0 0 1 40 36Z" fill="#4FA3E0"/><path d="M64 36 L40 36 A24 24 0 0 1 64 12Z" fill="#E8434A"/>'
    f'<circle cx="64" cy="36" r="24" fill="none" {W(3)}/><path d="M64 36 L80 20" {W(4)}/><circle cx="64" cy="36" r="4" fill="{O}"/>'
    f'<path d="M104 82 Q110 70 106 58" stroke="#FFD9B8" stroke-width="6" stroke-linecap="round" fill="none"/>'
    f'<circle cx="106" cy="56" r="4" fill="#FFD9B8" {W(1.8)}/>')

I["ambiland-okeania"] = ("#FFF4EC", "#F29A6B",
    "игрушечная плита с четырьмя конфорками и дверцей-окошком",
    "малыш-поварёнок в колпаке помешивает в кастрюльке игрушечный суп",
    f'<rect x="54" y="58" width="60" height="62" rx="6" fill="#fff" {W(3.2)}/>'
    f'<rect x="62" y="80" width="44" height="30" rx="4" fill="#9AD0F5" {W(2.6)}/>'
    + face(84, 94, d=8, k=0.5) +
    f'<circle cx="64" cy="66" r="3" fill="#E8434A"/><circle cx="74" cy="66" r="3" fill="#FFD23F"/>'
    f'<ellipse cx="88" cy="56" rx="18" ry="4" fill="#9AA8BB" {W(2.4)}/>'
    f'<path d="M72 56 V40 Q88 34 104 40 V56Z" fill="#E8434A" {W(2.8)}/><path d="M66 44 H72 M104 44 H110" {W(3)}/>'
    f'<path d="M80 30 q-4 -8 0 -14 M92 30 q4 -8 0 -14" fill="none" stroke="#fff" stroke-width="2.6"/>'
    f'<path d="M58 72 L80 36" stroke="#C98B4E" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M14 120 Q16 84 34 82 Q52 84 54 120Z" fill="#fff" {W(2.8)}/>'
    + kid(34, 66, 1.1, hair="#8A4B2A") +
    f'<path d="M22 56 Q18 40 30 42 Q34 32 42 40 Q52 38 46 56Z" fill="#fff" {W(2.4)}/>'
    f'<path d="M48 92 L58 74" stroke="#FFD9B8" stroke-width="6" stroke-linecap="round"/>')

I["gorod-stroiteley-riviera"] = ("#FFF6D8", "#F2B33D",
    "игрушечная бетономешалка с барабаном в оранжевую полоску",
    "вываливает на мягкую стройплощадку горку пёстрых кубиков-модулей",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#C9A26A" {W(3)}/>'
    f'<rect x="12" y="74" width="74" height="22" rx="6" fill="#4FA3E0" {W(3)}/>'
    f'<rect x="64" y="52" width="28" height="44" rx="5" fill="#4FA3E0" {W(3)}/><rect x="70" y="58" width="16" height="14" rx="3" fill="#E5F6FF" {W(2)}/>'
    f'<g transform="rotate(-18 42 58)"><ellipse cx="42" cy="58" rx="26" ry="20" fill="#F2803A" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 40 Q{x+8} 58 {x} 76" fill="none" stroke="#fff" stroke-width="4"/>' for x in (30, 44)) +
    f'<path d="M66 50 L76 46 L78 66 L66 64Z" fill="#F2803A" {W(2.4)}/></g>'
    + face(40, 60, d=8, k=0.6) +
    f'<circle cx="28" cy="100" r="9" fill="{O}"/><circle cx="28" cy="100" r="3.5" fill="#C9D3E3"/>'
    f'<circle cx="72" cy="100" r="9" fill="{O}"/><circle cx="72" cy="100" r="3.5" fill="#C9D3E3"/>'
    f'<rect x="92" y="92" width="14" height="14" fill="#E8434A" {W(2.2)}/><rect x="106" y="96" width="14" height="12" fill="#7CD26E" {W(2.2)}/>'
    f'<rect x="98" y="80" width="13" height="12" fill="#FFD23F" {W(2.2)}/><rect x="112" y="84" width="11" height="11" fill="#7C5CC4" {W(2.2)}/>')

I["pogruzhenie-mega-khimki"] = ("#BDEBFF", "#1D5C9E",
    "круглый жёлтый батискаф с большим иллюминатором и прожектором",
    "опускается на тросе к морскому дну, где лежит сундучок с загадкой и знаком вопроса",
    f'<path d="M64 -2 V26" stroke="#E5F6FF" stroke-width="3"/>'
    f'<path d="M-2 108 Q30 98 64 108 Q96 118 130 104 V130 H-2Z" fill="#E8C98A" {W(3)}/>'
    f'<circle cx="60" cy="56" r="28" fill="#FFD23F" {W(3.2)}/>'
    f'<circle cx="60" cy="58" r="15" fill="#9AD0F5" {W(3)}/>' + face(60, 58, d=5.5, k=0.5) +
    f'<rect x="54" y="24" width="12" height="8" fill="#F2803A" {W(2.4)}/>'
    f'<path d="M86 56 L96 52 V62Z" fill="#C9D3E3" {W(2.4)}/><path d="M96 54 L120 44 V72 L96 60" fill="#FFF3B0" opacity=".6"/>'
    f'<path d="M36 78 L28 90 M84 78 L92 90" {W(3)}/>'
    f'<rect x="92" y="94" width="24" height="16" rx="3" fill="#B9773E" {W(2.6)}/><path d="M92 100 H116" {W(2)}/>'
    f'<text x="104" y="92" font-family="Arial" font-weight="bold" font-size="14" fill="#FFD23F" text-anchor="middle" stroke="{O}" stroke-width=".8">?</text>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#E5F6FF" stroke-width="2"/>' for x, y, r in ((28, 30, 4), (22, 44, 3), (100, 26, 3))))

I["flik-flyak-pushkino"] = ("#FFF2F6", "#F48FB1",
    "мягкое поролоновое кольцо-перекат в голубую полоску",
    "катится колесом по ковру игровой, а внутри кувыркается малыш вверх ногами",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#7CD26E" {W(3)}/>'
    f'<circle cx="64" cy="66" r="42" fill="#4FA3E0" {W(3.2)}/><circle cx="64" cy="66" r="26" fill="#FFF2F6" {W(3)}/>'
    + "".join(f'<path d="M{64+26*__import__("math").cos(a)} {66+26*__import__("math").sin(a)} L{64+42*__import__("math").cos(a)} {66+42*__import__("math").sin(a)}" stroke="#fff" stroke-width="5"/>' for a in (0.3, 1.1, 1.9, 2.7, 3.5, 4.3, 5.1, 5.9)) +
    f'<circle cx="64" cy="66" r="42" fill="none" {W(3.2)}/><circle cx="64" cy="66" r="26" fill="none" {W(3)}/>'
    f'<g transform="rotate(180 64 66)">{kid(64, 58, 0.9, hair="#E0A23B")}</g>'
    f'<path d="M56 54 L50 44 M72 54 L78 44" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>' +
    f'<path d="M14 104 q-6 -4 -10 0 M22 96 q-8 -4 -14 0" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(112, 20, 5))

I["strana-chudes-pavposad"] = ("#FFF8E1", "#C9A0E8",
    "кривое зеркало в волнистой фиолетовой раме",
    "отражает обычного малыша смешным круглым толстячком, и малыш хохочет",
    f'<path d="M50 14 Q66 6 82 14 Q96 30 90 64 Q98 98 82 116 Q66 124 50 116 Q34 98 42 64 Q36 30 50 14Z" fill="#9B6BD8" {W(3.2)}/>'
    f'<path d="M54 22 Q66 16 78 22 Q88 36 82 64 Q90 94 78 108 Q66 114 54 108 Q42 94 50 64 Q44 36 54 22Z" fill="#E4F6FF" {W(2.6)}/>'
    f'<ellipse cx="66" cy="78" rx="18" ry="16" fill="#F2803A" {W(2.6)}/>'
    + kid(66, 52, 1.25, hair="#6B3F23") +
    f'<path d="M58 30 L64 40 M74 30 L68 40" stroke="#fff" stroke-width="3" opacity=".8"/>'
    f'<path d="M18 120 V96 Q18 88 26 88 Q34 88 34 96 V120Z" fill="#F2803A" {W(2.4)}/>'
    + kid(26, 78, 0.85, hair="#6B3F23") + sparkle(110, 30, 6) + sparkle(104, 100, 4))

I["nevidaliya-sergiev-posad"] = ("#E8FFF0", "#6CC79A",
    "пушистый жёлтый зверёк-невидаль с ушами-пропеллерами и одним рожком",
    "любопытно подглядывает из-за поворота игровой горки-трубы",
    f'<path d="M-2 40 Q40 30 70 52 Q96 72 130 66 V96 Q96 102 66 82 Q36 62 -2 70Z" fill="#E8434A" {W(3.2)}/>'
    f'<path d="M-2 52 Q40 44 68 64 Q96 84 130 80" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/>'
    f'<path d="M58 100 Q52 60 78 56 Q104 56 104 92 Q102 112 80 112 Q60 112 58 100Z" fill="#FFD84A" {W(3.2)}/>'
    + "".join(f'<path d="M{x} {y} l-4 6 M{x+4} {y+2} l-2 7" stroke="#E0B024" stroke-width="2"/>' for x, y in ((68, 72), (90, 70), (78, 96))) +
    f'<path d="M80 56 L84 38 L88 56" fill="#fff" {W(2.4)}/>'
    f'<path d="M66 60 Q50 46 54 40 Q64 44 70 58Z M96 60 Q112 46 108 40 Q98 44 92 58Z" fill="#FFD84A" {W(2.4)}/>'
    + face(81, 80, d=8, k=0.75) + sparkle(30, 100, 5) + sparkle(110, 28, 4))

I["zanzibar-xl-dmitrovka"] = ("#E0FFFA", "#2FB9B0",
    "соломенная хижина-бунгало на сваях с крышей-шапкой",
    "из её двери прямо в бассейн из шариков спускается маленькая горка",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#4FA3E0" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}" {W(1.6)}/>' for x, y, c in ((10, 110, "#E8434A"), (22, 116, "#FFD23F"), (36, 110, "#7C5CC4"), (50, 118, "#fff"), (64, 110, "#F2803A"), (100, 112, "#7CD26E"), (114, 118, "#E8434A"), (122, 108, "#FFD23F"))) +
    f'<path d="M32 104 V72 M88 104 V72" stroke="#8A5A2B" stroke-width="5"/>'
    f'<rect x="26" y="50" width="68" height="26" fill="#E7C08A" {W(3)}/>'
    f'<path d="M14 54 L60 18 L106 54Z" fill="#D9A84E" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 54 L{60+(x-60)*0.3:.0f} 26" stroke="#B5833A" stroke-width="2"/>' for x in (28, 44, 60, 76, 92)) +
    f'<rect x="52" y="56" width="16" height="20" fill="#7A4A22" {W(2.4)}/>'
    f'<path d="M68 76 Q96 80 112 104" fill="none" stroke="#FFD23F" stroke-width="8"/><path d="M68 76 Q96 80 112 104" fill="none" {W(2)}/>'
    + face(40, 64, d=5, k=0.45) + sparkle(110, 28, 5))

I["funky-world-titan"] = ("#2A1B4D", "#120A2A",
    "высокая лава-лампа с переливающимися пузырями-каплями",
    "светится на танцполе, а капли внутри тянутся вверх и пританцовывают",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#3C2A6E" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="104" width="22" height="26" fill="{c}" opacity=".7"/>' for x, c in ((0, "#F06A9E"), (44, "#4FA3E0"), (88, "#FFD23F"))) +
    f'<path d="M50 20 H78 L70 8 H58Z" fill="#C9D3E3" {W(2.6)}/>'
    f'<path d="M50 20 Q38 60 48 92 H80 Q90 60 78 20Z" fill="#7C3CC4" {W(3.2)}/>'
    f'<ellipse cx="62" cy="40" rx="7" ry="9" fill="#FF7A3D"/><ellipse cx="70" cy="66" rx="10" ry="12" fill="#FF7A3D"/><circle cx="56" cy="82" r="6" fill="#FF7A3D"/>'
    + face(68, 66, d=4.5, k=0.42) +
    f'<path d="M44 92 H84 L90 104 H38Z" fill="#C9D3E3" {W(2.8)}/>'
    f'<path d="M20 60 q-8 6 0 12 M108 60 q8 6 0 12" fill="none" stroke="#FF7A3D" stroke-width="3"/>'
    + sparkle(24, 30, 5, "#FFD23F") + sparkle(104, 28, 4, "#7FE3FF") + sparkle(108, 90, 3, "#F06A9E"))

I["trend-toys-titan"] = ("#F2FFFC", "#58C6C0",
    "квадратная игрушка-антистресс поп-ит с рядами пупырышек",
    "малыш продавливает пупырышки пальцем, и они весело щёлкают «поп!»",
    f'<g transform="rotate(-8 60 70)"><rect x="22" y="34" width="76" height="76" rx="14" fill="#B47CF0" {W(3.2)}/>'
    + "".join(f'<circle cx="{36+c*16}" cy="{48+r*16}" r="6" fill="{["#F06A9E", "#FFD23F", "#7CD26E", "#4FA3E0", "#F2803A"][r]}" {W(1.6)}/>' for r in range(5) for c in range(5) if not (r == 2 and c in (1, 2, 3))) +
    f'<rect x="38" y="74" width="44" height="16" rx="8" fill="#B47CF0"/></g>'
    + face(60, 80, d=10, k=0.6) +
    f'<path d="M104 26 L92 46" stroke="#FFD9B8" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M104 26 L92 46" fill="none" {W(2)}/>'
    f'<text x="98" y="20" font-family="Arial Black,Arial" font-weight="900" font-size="12" fill="#F06A9E">поп!</text>'
    + sparkle(18, 22, 4))

I["trend-toys-tishinka"] = ("#FFF5E9", "#F4A55C",
    "игрушечный шуруповёрт с жёлтой ручкой и синим корпусом",
    "закручивает огромный пластиковый болт в деревянную дощечку с дырочками",
    f'<rect x="10" y="96" width="108" height="20" rx="4" fill="#E7C08A" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="106" r="4" fill="#B9773E"/>' for x in (24, 44, 84, 104)) +
    f'<path d="M64 106 V70" stroke="#7CD26E" stroke-width="10"/><path d="M58 76 H70 M58 86 H70 M58 96 H70" stroke="#4E9E3F" stroke-width="2.4"/>'
    f'<path d="M64 106 V70" fill="none" {W(2)}/><rect x="52" y="62" width="24" height="10" rx="3" fill="#7CD26E" {W(2.6)}/>'
    f'<path d="M64 52 V62" stroke="#C9D3E3" stroke-width="5"/>'
    f'<path d="M40 20 H92 Q100 20 100 30 V44 Q100 52 92 52 H40 Q32 52 32 40 V32 Q32 20 40 20Z" fill="#2F6FB3" {W(3.2)}/>'
    f'<path d="M78 52 L84 86 H104 L98 52Z" fill="#FFD23F" {W(3)}/>'
    + face(58, 36, d=8, k=0.6) +
    f'<path d="M22 60 Q14 70 22 80 M106 64 Q114 72 108 82" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["joy-stars-ramenskoe"] = ("#F8F1FF", "#9C8CF0",
    "деревянная радужная доска-качалка в форме дуги",
    "качается, как лодочка, а в ней сидит малыш и машет звёздочкам",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#C7B6F5" {W(3)}/>'
    + "".join(f'<path d="M{14+i*6} 64 Q64 {130-i*6} {114-i*6} 64" fill="none" stroke="{c}" stroke-width="7"/>'
              for i, c in enumerate(("#E8434A", "#F2803A", "#FFD23F", "#7CD26E", "#4FA3E0"))) +
    f'<path d="M11 64 Q64 134 117 64" fill="none" {W(3)}/><path d="M42 64 Q64 102 86 64" fill="none" {W(3)}/>'
    + face(64, 104, d=8, k=0.5) + kid(64, 58, 1.0, hair="#E0A23B") +
    f'<path d="M56 66 Q64 72 72 66 L74 80 H54Z" fill="#F06A9E" {W(2.4)}/>'
    f'<path d="M74 66 L88 52" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y-6} L{x+2} {y-2} L{x+6} {y-1} L{x+3} {y+2} L{x+4} {y+6} L{x} {y+4} L{x-4} {y+6} L{x-3} {y+2} L{x-6} {y-1} L{x-2} {y-2}Z" fill="#FFD23F" {W(1.6)}/>' for x, y in ((98, 30), (30, 26), (112, 52))))

I["misty-park-zhukovsky"] = ("#FFF0F0", "#EE7B8B",
    "красная фотобудка с полосатой шторкой",
    "мигает вспышкой, и из щели выползает ленточка из четырёх смешных фото",
    f'<rect x="20" y="16" width="66" height="104" rx="6" fill="#E8434A" {W(3.2)}/>'
    f'<rect x="28" y="38" width="30" height="74" fill="#FFD23F" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 38 V112" stroke="#F2A541" stroke-width="3"/>' for x in (34, 40, 46, 52)) +
    f'<rect x="64" y="40" width="16" height="12" rx="3" fill="#2E2A4A" {W(2.4)}/><circle cx="72" cy="46" r="3.5" fill="#9AD0F5"/>'
    f'<path d="M72 30 l4 -10 M82 34 l10 -6 M62 30 l-4 -10" stroke="#FFF3B0" stroke-width="3" stroke-linecap="round"/>'
    f'<text x="53" y="31" font-family="Arial" font-weight="bold" font-size="9" fill="#fff" text-anchor="middle">ФОТО</text>'
    f'<rect x="64" y="70" width="18" height="4" fill="{O}"/>'
    f'<g transform="rotate(14 92 92)"><rect x="80" y="70" width="24" height="56" fill="#fff" {W(2.4)}/>'
    + "".join(f'<rect x="84" y="{74+i*12}" width="16" height="10" fill="#9AD0F5"/><circle cx="92" cy="{79+i*12}" r="3" fill="#FFD9B8"/>' for i in range(4)) + '</g>' + face(72, 60, d=6, k=0.45) + sparkle(110, 24, 5))

I["goodlandia-lytkarino"] = ("#EFFBFF", "#7CC0E8",
    "кукольный домик в разрезе с тремя комнатками и розовой крышей",
    "в окошках горит свет: в одной комнате кукла машет рукой, в другой спит плюшевый мишка",
    f'<path d="M14 50 L64 12 L114 50Z" fill="#F06A9E" {W(3.2)}/>'
    f'<rect x="20" y="50" width="88" height="66" fill="#FFF3D6" {W(3.2)}/>'
    f'<path d="M64 50 V116 M20 84 H108" {W(3)}/>'
    f'<rect x="24" y="54" width="36" height="26" fill="#FFE9A0"/><rect x="68" y="54" width="36" height="26" fill="#C9F0D8"/>'
    f'<rect x="24" y="88" width="36" height="24" fill="#D8E6FF"/><rect x="68" y="88" width="36" height="24" fill="#FFD9E6"/>'
    f'<circle cx="42" cy="64" r="6" fill="#FFD9B8" {W(2)}/><path d="M36 80 Q42 66 48 80Z" fill="#E8434A" {W(2)}/><path d="M48 70 L54 62" stroke="#FFD9B8" stroke-width="3" stroke-linecap="round"/>'
    f'<rect x="74" y="100" width="26" height="8" fill="#4FA3E0" {W(1.8)}/><circle cx="82" cy="98" r="6" fill="#C98B4E" {W(2)}/>'
    f'<path d="M92 92 q3 -3 6 0" fill="none" stroke="{O}" stroke-width="1.6"/>'
    + face(64, 32, d=6, k=0.5) +
    f'<rect x="80" y="64" width="16" height="12" fill="#7CD26E" {W(1.8)}/><circle cx="36" cy="100" r="5" fill="#FFD23F" {W(1.8)}/>'
    + sparkle(112, 22, 4))

I["dzhungli-siti-4daily"] = ("#F0FFE0", "#5DAA4A",
    "огромный резной лист монстеры, изогнутый горкой",
    "по нему, как по горке, с визгом скатывается малыш прямо в бассейн из шариков",
    f'<path d="M-2 106 H130 V130 H-2Z" fill="#FFF3D6" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}" {W(1.6)}/>' for x, y, c in ((70, 108, "#E8434A"), (82, 114, "#FFD23F"), (94, 108, "#4FA3E0"), (106, 116, "#F06A9E"), (118, 108, "#7CD26E"), (60, 116, "#F2803A"))) +
    f'<path d="M8 20 Q50 10 64 56 Q74 92 100 102 Q60 108 40 80 Q14 50 8 20Z" fill="#2E9E4A" {W(3.2)}/>'
    f'<path d="M14 24 Q48 40 60 66 Q72 92 98 100" fill="none" stroke="#1F7A36" stroke-width="2.6"/>'
    + "".join(f'<path d="M{x} {y} q8 -2 12 6" fill="none" stroke="#C9F0B8" stroke-width="4" stroke-linecap="round"/>' for x, y in ((26, 30), (38, 50), (50, 70))) +
    f'<path d="M64 76 L58 66 M78 80 L82 70" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M62 78 L78 82 L76 94 L60 90Z" fill="#FFD23F" {W(2.2)}/>' + kid(64, 64, 0.85, hair="#3B2A1A") +
    face(34, 42, d=6, k=0.5) + sparkle(100, 30, 5) + sparkle(116, 64, 3.5))

I["dubi-dubi-varshavka"] = ("#FFFBE8", "#EFC24A",
    "игрушка-каталка на длинной палочке с бабочкой, хлопающей крыльями",
    "малыш катит её по полу игровой, и крылья хлопают при каждом обороте колёс",
    f'<path d="M-2 110 H130 V130 H-2Z" fill="#9BD3FF" {W(3)}/>'
    f'<path d="M30 40 L74 98" stroke="#C98B4E" stroke-width="5" stroke-linecap="round"/>'
    f'<circle cx="72" cy="102" r="8" fill="#4FA3E0" {W(2.6)}/><circle cx="96" cy="102" r="8" fill="#4FA3E0" {W(2.6)}/>'
    f'<rect x="68" y="88" width="34" height="8" rx="3" fill="#E8434A" {W(2.4)}/>'
    f'<path d="M84 88 Q64 62 70 52 Q84 54 84 86Z" fill="#F06A9E" {W(2.6)}/><path d="M86 88 Q106 62 100 52 Q86 54 86 86Z" fill="#FFD23F" {W(2.6)}/>'
    f'<ellipse cx="85" cy="78" rx="4" ry="12" fill="#7C5CC4" {W(2.2)}/>'
    + face(85, 72, d=2.6, k=0.3, blush=False) +
    f'<path d="M82 66 Q78 58 74 58 M88 66 Q92 58 96 58" fill="none" {W(1.8)}/>'
    + kid(26, 46, 1.05, hair="#8A4B2A") +
    f'<path d="M18 60 Q26 54 34 60 L34 80 H18Z" fill="#7CD26E" {W(2.4)}/><path d="M34 62 L30 44" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M110 70 q6 -4 10 2 M108 80 q8 -2 12 4" fill="none" stroke="#fff" stroke-width="2.4"/>')

I["etalosha-butovo"] = ("#FFF7E6", "#E5B36A",
    "пластмассовая мельница для песка с красным колесом-черпалками",
    "крутится под струйкой песка, которая сыплется из жёлтого совочка",
    f'<path d="M-2 104 Q64 94 130 104 V130 H-2Z" fill="#F2D48C" {W(3)}/>'
    f'<path d="M38 104 L48 54 H80 L90 104Z" fill="#4FA3E0" {W(3.2)}/>'
    f'<path d="M44 54 H84 L78 42 H50Z" fill="#7CD26E" {W(2.8)}/>'
    f'<circle cx="64" cy="76" r="20" fill="#E8434A" {W(3)}/>'
    + "".join(f'<path d="M64 76 L{64+20*__import__("math").cos(a):.1f} {76+20*__import__("math").sin(a):.1f}" stroke="#fff" stroke-width="3"/>' for a in (0, 1.05, 2.1, 3.14, 4.19, 5.24)) +
    f'<circle cx="64" cy="76" r="7" fill="#FFD23F" {W(2.4)}/>' + face(64, 76, d=2.6, k=0.28, blush=False) +
    f'<path d="M82 14 Q102 10 104 22 L86 30Z" fill="#FFD23F" {W(2.6)}/><path d="M104 18 L118 8" stroke="#FFD23F" stroke-width="5" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{82-i*2}" cy="{34+i*4}" r="1.6" fill="#C9A26A"/>' for i in range(4)) +
    face(64, 98, d=8, k=0.5) + sparkle(20, 40, 5))

I["igralife-pererva"] = ("#F0F6FF", "#7E97E0",
    "надувной молоточек-пищалка в красно-жёлтую полоску",
    "стукает по выскочившим из норок плюшевым кротам на игровом автомате",
    f'<rect x="8" y="80" width="112" height="44" rx="8" fill="#7C5CC4" {W(3.2)}/>'
    + "".join(f'<ellipse cx="{x}" cy="90" rx="13" ry="5" fill="#2E2A4A" {W(2)}/>' for x in (30, 64, 98)) +
    f'<path d="M22 90 Q22 70 30 70 Q38 70 38 90" fill="#9A6A4A" {W(2.4)}/><circle cx="30" cy="78" r="2.6" fill="#F06A9E"/>'
    f'<path d="M90 90 Q90 74 98 74 Q106 74 106 90" fill="#9A6A4A" {W(2.4)}/><circle cx="98" cy="81" r="2.6" fill="#F06A9E"/>'
    f'<path d="M58 90 Q58 84 64 84 Q70 84 70 90" fill="#9A6A4A" {W(2.4)}/>'
    f'<path d="M58 80 l-6 -6 M64 78 V70 M70 80 l6 -6" stroke="#FFD23F" stroke-width="3" stroke-linecap="round"/>'
    f'<g transform="rotate(30 74 40)"><rect x="70" y="40" width="8" height="40" rx="3" fill="#FFD23F" {W(2.4)}/>'
    f'<rect x="48" y="18" width="52" height="26" rx="12" fill="#E8434A" {W(3)}/>'
    f'<path d="M62 18 V44 M86 18 V44" stroke="#FFD23F" stroke-width="5"/>' + face(74, 31, d=6, k=0.5) + '</g>'
    + "".join(f'<rect x="{x}" y="108" width="14" height="8" rx="2" fill="#FFD23F"/>' for x in (24, 57, 90)))

I["igralife-signalny"] = ("#FFFDEB", "#F0C74A",
    "пирамида из шести пёстрых жестяных банок",
    "в неё врезается тряпичный мячик, и верхняя банка с удивлением летит вверх",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#B9773E" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="20" height="22" rx="2" fill="{c}" {W(2.6)}/><path d="M{x} {y+6} H{x+20} M{x} {y+16} H{x+20}" stroke="#fff" stroke-width="1.8"/>'
              for x, y, c in ((34, 82, "#E8434A"), (56, 82, "#4FA3E0"), (78, 82, "#7CD26E"), (45, 60, "#F2803A"), (67, 60, "#7C5CC4"))) +
    f'<g transform="rotate(-24 70 26)"><rect x="60" y="14" width="20" height="22" rx="2" fill="#F06A9E" {W(2.6)}/></g>'
    + face(70, 26, d=4, k=0.42) +
    f'<circle cx="20" cy="56" r="10" fill="#fff" {W(2.6)}/><path d="M12 52 Q20 58 28 52 M14 62 Q20 56 26 62" fill="none" stroke="#E8434A" stroke-width="2"/>'
    f'<path d="M6 56 q-4 -2 -8 0 M8 64 q-4 0 -8 2" fill="none" stroke="#fff" stroke-width="2.4"/>'
    f'<path d="M92 24 l6 -6 M96 32 l8 -2 M50 20 l-6 -6" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>')

I["akuna-matata-butovo-park"] = ("#FFF3D9", "#F2A33A",
    "толстый баобаб — игровой домик с окошком-дуплом и верёвочной лесенкой",
    "из дупла машет малыш, а сбоку по стволу вьётся жёлтая горка",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#D9A84E" {W(3)}/>'
    f'<path d="M40 108 Q44 70 38 44 H90 Q84 70 88 108Z" fill="#B88A64" {W(3.2)}/>'
    f'<path d="M24 46 Q18 30 34 30 Q38 14 54 22 Q64 10 76 22 Q92 14 96 30 Q112 30 104 46Z" fill="#6DBE4E" {W(3)}/>'
    f'<path d="M38 44 L26 32 M64 44 V26 M90 44 L102 32" stroke="#8A5A3A" stroke-width="4" stroke-linecap="round"/>'
    f'<ellipse cx="62" cy="68" rx="12" ry="14" fill="#5A3A22" {W(2.6)}/>' + kid(62, 70, 0.8, hair="#2B2B2B") +
    f'<path d="M74 66 L82 58" stroke="#FFD9B8" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M86 60 Q112 70 102 90 Q96 100 118 108" fill="none" stroke="#FFD23F" stroke-width="8"/><path d="M86 60 Q112 70 102 90 Q96 100 118 108" fill="none" {W(2)}/>'
    f'<path d="M30 70 V108 M38 70 V108" stroke="#C98B4E" stroke-width="2.4"/>'
    + "".join(f'<path d="M30 {y} H38" stroke="#C98B4E" stroke-width="2.4"/>' for y in (78, 88, 98)) +
    face(64, 94, d=8, k=0.5) + sparkle(110, 18, 5))

I["bum-park-lesnoy-gorodok"] = ("#EAF7FF", "#62A9E6",
    "прозрачный надувной бампербол, из которого торчат ножки в кедах",
    "сталкивается с другим шаром посреди игровой, и между ними вспыхивает «БУМ!»",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#7CD26E" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="70" r="30" fill="{c}" opacity=".55" {W(3)}/>' for x, c in ((34, "#C9F0FF"), (96, "#FFE0EC"))) +
    kid(34, 62, 1.0, hair="#C26A2B") + kid(96, 62, 1.0, hair="#2B2B2B") +
    f'<path d="M26 100 L22 112 M42 100 L46 112 M88 100 L84 112 M104 100 L108 112" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M18 112 H28 M42 112 H52 M80 112 H90 M104 112 H114" stroke="#E8434A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M64 28 L68 40 L80 36 L72 46 L82 54 L68 52 L64 64 L60 52 L46 54 L56 46 L48 36 L60 40Z" fill="#FFD23F" {W(2.4)}/>'
    f'<text x="64" y="22" font-family="Arial Black,Arial" font-weight="900" font-size="13" fill="#E8434A" text-anchor="middle" stroke="{O}" stroke-width=".8">БУМ!</text>')

I["iqbabymall-leningradsky"] = ("#F3FFF0", "#8BCF7A",
    "проволочный лабиринт с цветными бусинами на деревянной подставке",
    "малыш пухлыми пальчиками ведёт красную бусину через самую высокую петлю",
    f'<rect x="16" y="98" width="96" height="18" rx="5" fill="#E7C08A" {W(3)}/>'
    f'<path d="M24 98 Q24 40 52 40 Q70 40 70 70 Q70 26 96 30 Q110 34 104 98" fill="none" stroke="#4FA3E0" stroke-width="4"/>'
    f'<path d="M36 98 Q34 66 54 64 Q80 64 92 98" fill="none" stroke="#E8434A" stroke-width="4"/>'
    f'<path d="M48 98 Q60 80 80 98" fill="none" stroke="#FFD23F" stroke-width="4"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(2)}/>' for x, y, r, c in ((28, 70, 5, "#FFD23F"), (90, 36, 6, "#E8434A"), (66, 66, 5, "#7C5CC4"), (60, 86, 4.5, "#4FA3E0"), (100, 60, 5, "#7CD26E"), (42, 74, 4.5, "#F2803A"))) +
    face(64, 107, d=8, k=0.42) +
    f'<path d="M108 14 Q100 30 94 34" stroke="#FFD9B8" stroke-width="9" stroke-linecap="round"/><path d="M108 14 Q100 30 94 34" fill="none" {W(2)}/>'
    + sparkle(18, 24, 4))

I["postroyka-domodedovo"] = ("#FFF4EA", "#EF9A5C",
    "деревянная стучалка со скамеечкой и пёстрыми колышками",
    "малыш стукает молоточком, и колышки по очереди уходят вниз, а с обратной стороны выскакивают",
    f'<rect x="20" y="80" width="88" height="20" rx="4" fill="#C98B4E" {W(3.2)}/>'
    f'<path d="M28 100 V116 M100 100 V116" stroke="#9A5B2A" stroke-width="7" stroke-linecap="round"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="12" height="{80-y}" rx="5" fill="{c}" {W(2.4)}/>' for x, y, c in ((32, 62, "#E8434A"), (50, 74, "#FFD23F"), (68, 60, "#4FA3E0"), (86, 66, "#7CD26E"))) +
    face(64, 90, d=9, k=0.5) +
    f'<g transform="rotate(-30 64 30)"><rect x="60" y="28" width="7" height="34" rx="3" fill="#E7C08A" {W(2.2)}/>'
    f'<rect x="48" y="18" width="30" height="14" rx="5" fill="#7C5CC4" {W(2.6)}/></g>'
    f'<path d="M50 74 l-6 -6 M56 72 V64" stroke="{O}" stroke-width="2" stroke-linecap="round"/>' + sparkle(108, 30, 5) + sparkle(18, 40, 3.5))

I["bambino-pavposad"] = ("#FFF0F5", "#F29BBE",
    "пара вязаных пинеток с помпончиками и мордашками",
    "топают по мягкому коврику-пазлу игровой, оставляя следы-сердечки",
    + "".join(f'<rect x="{x}" y="{y}" width="32" height="32" fill="{c}" {W(2.4)}/>' for x, y, c in ((0, 84, "#9BD3FF"), (32, 84, "#FFE066"), (64, 84, "#9EE6A0"), (96, 84, "#FFB3C7"), (16, 116, "#FFB3C7"), (48, 116, "#9BD3FF"), (80, 116, "#FFE066"))) if False else
    "".join(f'<rect x="{x}" y="{y}" width="32" height="32" fill="{c}" {W(2.4)}/>' for x, y, c in ((0, 84, "#9BD3FF"), (32, 84, "#FFE066"), (64, 84, "#9EE6A0"), (96, 84, "#FFB3C7"), (16, 116, "#FFB3C7"), (48, 116, "#9BD3FF"), (80, 116, "#FFE066"))) +
    f'<path d="M20 74 Q16 52 30 46 L40 46 Q48 48 48 60 Q58 64 58 74 Q58 84 44 84 H28 Q20 84 20 74Z" fill="#7FC8F0" {W(3)}/>'
    f'<path d="M68 64 Q64 42 78 36 L88 36 Q96 38 96 50 Q106 54 106 64 Q106 74 92 74 H76 Q68 74 68 64Z" fill="#FF9EC4" {W(3)}/>'
    f'<path d="M30 46 H40 M78 36 H88" stroke="#fff" stroke-width="4"/>'
    f'<circle cx="35" cy="40" r="6" fill="#fff" {W(2.2)}/><circle cx="83" cy="30" r="6" fill="#fff" {W(2.2)}/>'
    + face(42, 66, d=5.5, k=0.45) + face(90, 56, d=5.5, k=0.45) +
    f'<path d="M110 100 q-4 -5 -8 0 q4 6 8 8 q4 -2 8 -8 q-4 -5 -8 0Z" fill="#E8434A"/>' + sparkle(112, 24, 4))

I["drugie-miry-inzhenernaya"] = ("#1E1A4A", "#0B0920",
    "маленькая кубическая воксельная планета с травой, водой и домиком",
    "висит в светящейся цифровой сетке виртуального мира, вокруг мигают пиксели",
    "".join(f'<path d="M{x} 0 V128" stroke="#3FE0D0" stroke-width="1" opacity=".35"/>' for x in range(8, 128, 16)) +
    "".join(f'<path d="M0 {y} H128" stroke="#3FE0D0" stroke-width="1" opacity=".35"/>' for y in range(8, 128, 16)) +
    f'<path d="M64 26 L100 44 V86 L64 104 L28 86 V44Z" fill="#8A5A3A" {W(3)}/>'
    f'<path d="M64 26 L100 44 L64 62 L28 44Z" fill="#6DBE4E" {W(3)}/>'
    f'<path d="M64 62 V104 L100 86 V44Z" fill="#6B4027"/><path d="M64 62 V104 M64 62 L100 44" fill="none" {W(3)}/>'
    f'<path d="M44 46 L56 40 L68 46 L56 52Z" fill="#4FA3E0" {W(1.8)}/>'
    f'<path d="M72 36 L80 32 L88 36 V44 L80 48 L72 44Z" fill="#E8EEF7" {W(1.8)}/><path d="M72 36 L80 28 L88 36" fill="#E8434A" {W(1.8)}/>'
    + face(46, 74, d=7, k=0.55) +
    "".join(f'<rect x="{x}" y="{y}" width="6" height="6" fill="{c}"/>' for x, y, c in ((16, 22, "#F06A9E"), (108, 24, "#FFD23F"), (14, 104, "#7FE3FF"), (106, 100, "#7CD26E"), (96, 12, "#7FE3FF"))))

# ---------------- Квесты ----------------
I["inkubo-galushkina"] = ("#FFF4E0", "#C98B4E",
    "старинный книжный шкаф с потайной дверью",
    "одна книга-рычаг наклонилась, шкаф приоткрылся, и из щели льётся загадочный зелёный свет",
    f'<path d="M60 16 L104 10 V122 L60 114Z" fill="#2E2A4A" {W(3)}/><path d="M64 20 L100 16 V116 L64 110Z" fill="#7FF0B0" opacity=".45"/>'
    f'<rect x="14" y="14" width="56" height="102" fill="#8A5A3A" {W(3.2)}/>'
    + "".join(f'<path d="M14 {y} H70" {W(2.6)}/>' for y in (44, 74)) +
    "".join(f'<rect x="{x}" y="{y}" width="7" height="24" fill="{c}" {W(1.6)}/>' for x, y, c in ((18, 20, "#E8434A"), (26, 20, "#4FA3E0"), (34, 20, "#FFD23F"), (50, 20, "#7CD26E"), (58, 20, "#7C5CC4"), (18, 50, "#F2803A"), (26, 50, "#2EAA4A"), (42, 50, "#E8434A"), (50, 50, "#4FA3E0"), (58, 50, "#FFD23F"))) +
    f'<g transform="rotate(-28 44 44)"><rect x="40" y="20" width="8" height="24" fill="#C8314E" {W(1.8)}/></g>'
    + face(42, 94, d=9, k=0.6) +
    f'<path d="M108 30 l8 -4 M108 60 h10 M108 92 l8 4" stroke="#7FF0B0" stroke-width="3" stroke-linecap="round"/>' + sparkle(116, 116, 4))

I["inkubo-rizhsky"] = ("#EEF2F8", "#8C9AB6",
    "железный щиток с тремя рубильниками и круглой лампочкой",
    "последний рубильник опущен — лампочка вспыхнула и на табло загорелся ответ «ОК»",
    f'<rect x="20" y="20" width="88" height="94" rx="8" fill="#6C7896" {W(3.2)}/>'
    f'<rect x="28" y="28" width="72" height="20" rx="3" fill="#1E2B1E" {W(2.4)}/>'
    f'<text x="64" y="44" font-family="Arial Black,Arial" font-weight="900" font-size="14" fill="#7CFF9A" text-anchor="middle">ОК</text>'
    + "".join(f'<rect x="{x}" y="60" width="16" height="36" rx="3" fill="#2E2A4A" {W(2.2)}/>' for x in (32, 56, 80)) +
    f'<path d="M40 78 L40 62" stroke="#E8434A" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M64 78 L64 62" stroke="#FFD23F" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M88 78 L88 96" stroke="#4FA3E0" stroke-width="6" stroke-linecap="round"/>'
    f'<circle cx="64" cy="106" r="5" fill="#FFF3B0" {W(2)}/>' +
    f'<circle cx="64" cy="10" r="9" fill="#FFE066" {W(2.6)}/><path d="M50 8 l-6 -2 M78 8 l6 -2 M64 -2 v0" stroke="#FFE066" stroke-width="3" stroke-linecap="round"/>'
    + face(64, 10, d=3.4, k=0.34, blush=False))

I["inkubo-dmitrovskoe"] = ("#E9F7EE", "#4E9E6E",
    "зелёный жестяной перископ с круглым глазком-окуляром",
    "высовывается из-за пирамиды ящиков и высматривает спрятанную подсказку-конверт",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#7A5A3A" {W(3)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="34" height="26" fill="#C98B4E" {W(2.6)}/><path d="M{x} {y} L{x+34} {y+26} M{x+34} {y} L{x} {y+26}" stroke="#9A5B2A" stroke-width="1.8"/>'
              for x, y in ((14, 82), (48, 82), (31, 56))) +
    f'<rect x="68" y="30" width="14" height="78" fill="#3F8A5A" {W(3)}/>'
    f'<path d="M68 30 V18 Q68 12 74 12 H96 V32 H82" fill="#3F8A5A" {W(3)}/>'
    f'<ellipse cx="98" cy="22" rx="5" ry="10" fill="#9AD0F5" {W(2.6)}/>' + face(75, 66, d=4, k=0.38) +
    f'<rect x="102" y="88" width="20" height="14" fill="#fff" {W(2.2)}/><path d="M102 88 L112 96 L122 88" fill="none" {W(2)}/>'
    f'<path d="M104 30 Q112 60 110 84" fill="none" stroke="#FFF3B0" stroke-width="2.4" stroke-dasharray="3 4"/>')

I["fort-boyard-filion"] = ("#FFF1D6", "#B88A4E",
    "тяжёлая кованая решётка-герса крепостных ворот на цепях",
    "медленно поднимается, и под ней на четвереньках проскальзывает малыш-участник",
    f'<path d="M0 10 H128 V128 H0Z" fill="#A89A86"/>'
    + "".join(f'<path d="M0 {y} H128" stroke="#8C7E6A" stroke-width="2"/>' for y in (30, 50, 70, 90, 110)) +
    f'<path d="M24 128 V48 Q64 8 104 48 V128Z" fill="#2E2A3A" {W(3.2)}/>'
    f'<path d="M30 76 V44 Q64 14 98 44 V76" fill="none" stroke="#5A5470" stroke-width="2"/>'
    + "".join(f'<path d="M{x} 30 V80 l-3 6 h6 l-3 -6" fill="#4A4458" stroke="#4A4458" stroke-width="5"/>' for x in (36, 50, 64, 78, 92)) +
    "".join(f'<path d="M28 {y} H100" stroke="#4A4458" stroke-width="5"/>' for y in (44, 64)) +
    face(64, 54, d=10, k=0.6) +
    f'<path d="M30 20 V44 M98 20 V44" stroke="#C9D3E3" stroke-width="3" stroke-dasharray="4 3"/>'
    f'<path d="M50 112 Q62 98 82 106 L84 114 H48Z" fill="#E8434A" {W(2.4)}/>' + kid(44, 104, 0.8, hair="#E0A23B"))

I["fort-boyard-tomilino"] = ("#E5F8FF", "#4A9CC7",
    "большая витая морская раковина-рог с перламутровым раструбом",
    "трубит с зубчатой стены крепости, объявляя начало испытания, звуковые волны летят над морем",
    f'<path d="M-2 92 Q30 84 64 92 Q96 100 130 90 V130 H-2Z" fill="#2F7FC1" {W(3)}/>'
    f'<path d="M-2 72 H24 V64 H38 V72 H56 V64 H70 V72 H90 V64 H104 V72 H130 V100 H-2Z" fill="#C9B79A" {W(3)}/>'
    + "".join(f'<path d="M{x} 80 V100" stroke="#A89474" stroke-width="2"/>' for x in (20, 48, 76, 104)) +
    f'<path d="M30 58 Q24 36 42 28 Q60 22 66 36 Q76 30 88 34 L104 18 Q114 34 106 54 L90 48 Q84 62 66 62 Q42 66 30 58Z" fill="#FFE3CC" {W(3.2)}/>'
    f'<path d="M104 18 Q114 34 106 54 Q96 38 104 18Z" fill="#FF9EC4" {W(2.4)}/>'
    f'<path d="M40 34 Q48 44 44 58 M52 30 Q62 42 58 60 M66 36 Q74 46 72 60" fill="none" stroke="#E0A88A" stroke-width="2.2"/>'
    + face(48, 48, d=6, k=0.5) +
    f'<path d="M112 12 q8 8 2 18 M118 6 q12 12 4 28" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' + sparkle(18, 22, 4))

I["action-lasertag-ramenskoe"] = ("#1F2B1F", "#0C140C",
    "баррикада из ярких автомобильных покрышек, сложенных стопками",
    "из-за неё в темноте лазертага выглядывает малыш, а над головой проносятся красные и зелёные лучи",
    f'<path d="M-2 0 L130 46" stroke="#FF3B5C" stroke-width="2.6" opacity=".9"/><path d="M-2 40 L130 10" stroke="#3BFF8A" stroke-width="2.6" opacity=".9"/>'
    f'<path d="M-2 116 H130 V130 H-2Z" fill="#3A3A3A" {W(3)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="20" ry="9" fill="{c}" {W(3)}/><ellipse cx="{x}" cy="{y}" rx="9" ry="3.6" fill="#1A1A1A"/>'
              for x, y, c in ((26, 108, "#F2803A"), (66, 108, "#4FA3E0"), (106, 108, "#FFD23F"), (26, 92, "#7CD26E"), (66, 92, "#E8434A"), (106, 92, "#7C5CC4"), (46, 76, "#FFD23F"), (86, 76, "#F2803A"))) +
    kid(66, 58, 1.05, hair="#3B2A1A") +
    f'<path d="M74 64 H96" stroke="#9AA8BB" stroke-width="5" stroke-linecap="round"/><circle cx="98" cy="64" r="3" fill="#3BFF8A"/>' + sparkle(110, 24, 4, "#3BFF8A"))

# ---------------- Музеи и экскурсии ----------------
I["rekordium-novy-arbat"] = ("#F2F7FF", "#86A6E8",
    "серебристая канцелярская скрепка-рекордсменка с медалькой «№1»",
    "тянет за собой бесконечную цепочку разноцветных скрепок, которая убегает за край круга",
    f'<path d="M30 20 V92 Q30 108 46 108 Q62 108 62 92 V34 Q62 26 54 26 Q46 26 46 34 V88" fill="none" stroke="#9AA8BB" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M30 20 V92 Q30 108 46 108 Q62 108 62 92 V34 Q62 26 54 26 Q46 26 46 34 V88" fill="none" {W(2.4)}/>' +
    "".join(f'<g transform="rotate({ang} {x} {y})"><rect x="{x-12}" y="{y-5}" width="24" height="10" rx="5" fill="none" stroke="{c}" stroke-width="4"/></g>'
            for x, y, ang, c in ((70, 104, 10, "#E8434A"), (90, 100, -20, "#FFD23F"), (106, 86, -50, "#7CD26E"), (114, 66, -80, "#4FA3E0"), (114, 46, -100, "#F06A9E"), (108, 28, -130, "#7C5CC4"), (96, 14, -160, "#F2803A"))) +
    f'<circle cx="46" cy="56" r="14" fill="#FFD23F" {W(2.6)}/><text x="46" y="61" font-family="Arial Black,Arial" font-weight="900" font-size="11" fill="{O}" text-anchor="middle">№1</text>'
    f'<path d="M40 42 L36 30 M52 42 L56 30" stroke="#E8434A" stroke-width="3"/>'
    + face(46, 84, d=5, k=0.42) + sparkle(18, 110, 4))

I["national-center-rossiya"] = ("#F3F7FF", "#7F9BD6",
    "гирлянда из семи круглых часиков с разным временем",
    "висит над картой страны: на каждых часах свой часовой пояс, от рассвета до ночи",
    f'<path d="M14 92 Q24 76 46 80 Q60 70 78 76 Q96 70 112 82 Q120 96 104 106 Q80 114 60 108 Q34 112 20 104 Q8 100 14 92Z" fill="#9EE6A0" {W(3)}/>'
    f'<path d="M30 92 Q46 88 56 96 M70 88 Q86 92 96 98" fill="none" stroke="#4E9E6E" stroke-width="2"/>'
    f'<path d="M4 26 Q64 62 124 26" fill="none" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="{c}" {W(2.4)}/><path d="M{x} {y} V{y-6} M{x} {y} L{x+4} {y+2}" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>'
              for x, y, c in ((14, 36, "#FFE9A0"), (32, 46, "#FFD39A"), (50, 52, "#FFB3A0"), (64, 54, "#F7A3C8"), (78, 52, "#C9B3F5"), (96, 46, "#9EB3F0"), (114, 36, "#6C7FD6"))) + face(62, 94, d=8, k=0.5) +
    f'<circle cx="14" cy="16" r="5" fill="#FFD23F"/><path d="M110 10 a6 6 0 1 0 6 8 a4.5 4.5 0 1 1 -6 -8Z" fill="#FFF3B0" {W(1.6)}/>')

I["french-kiss-factory-tour"] = ("#FFF4F8", "#E8A0BE",
    "горсть разноцветных глянцевых драже-горошин",
    "с весёлым стуком сыплются из вращающегося медного дражировочного котла на фабрике",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#C9D3E3" {W(3)}/>'
    f'<path d="M86 104 V70" stroke="#6C7896" stroke-width="6"/>'
    f'<g transform="rotate(-25 70 52)"><ellipse cx="70" cy="52" rx="38" ry="30" fill="#D9853B" {W(3.2)}/>'
    f'<ellipse cx="44" cy="52" rx="10" ry="20" fill="#5A3A22" {W(2.6)}/>'
    f'<path d="M78 26 Q100 40 96 74" fill="none" stroke="#F2B36A" stroke-width="4"/></g>'
    + face(78, 58, d=10, k=0.6) +
    "".join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="5" fill="{c}" {W(1.8)}/><ellipse cx="{x-2}" cy="{y-2}" rx="2" ry="1.4" fill="#fff" opacity=".8"/>'
            for x, y, c in ((30, 74, "#E8434A"), (22, 88, "#FFD23F"), (36, 92, "#7CD26E"), (16, 100, "#4FA3E0"), (30, 104, "#F06A9E"), (44, 102, "#7C5CC4"), (24, 62, "#F2803A"))) +
    sparkle(110, 22, 5) + sparkle(16, 30, 3.5))

# ---------------- Мастер-классы ----------------
I["kot-filius-rio-dmitrovskoe"] = ("#F2FBFF", "#73C2E8",
    "фигурный дырокол с рычажком, выбивающий звёздочки",
    "щёлкает по листу цветной бумаги, и из-под него вылетают бумажные звёздочки-конфетти",
    f'<path d="M14 92 L104 84 L116 108 L22 118Z" fill="#FFD23F" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} l2 4 l4 0 l-3 3 l1 4 l-4 -2 l-4 2 l1 -4 l-3 -3 l4 0Z" fill="#fff" {W(1.4)}/>' for x, y in ((40, 98), (60, 96), (80, 94))) +
    f'<rect x="30" y="62" width="64" height="30" rx="8" fill="#F06A9E" {W(3.2)}/>'
    f'<path d="M40 62 L80 30 Q88 26 92 32 L96 40 L54 62Z" fill="#7C5CC4" {W(3)}/>'
    + face(62, 76, d=9, k=0.6) +
    "".join(f'<path d="M{x} {y} l2.6 5 l5.4 .4 l-4 3.6 l1.4 5.4 l-5.4 -3 l-5 3 l1.2 -5.4 l-4 -3.6 l5.4 -.4Z" fill="{c}" {W(1.6)}/>'
            for x, y, c in ((104, 46, "#FFD23F"), (112, 64, "#4FA3E0"), (20, 40, "#7CD26E"), (14, 62, "#F2803A"), (100, 20, "#E8434A"))))

I["detskaya-lepka-khoroshevskoe"] = ("#FFF8EE", "#E9B07C",
    "пластиковый пресс-шприц для пластилина с поршнем-ручкой",
    "выдавливает зелёную пластилиновую «лапшу»-травку на полянку, где уже стоит пластилиновый грибок",
    f'<ellipse cx="64" cy="108" rx="52" ry="14" fill="#9AD0F5" {W(3)}/>'
    + "".join(f'<path d="M{x} 104 Q{x+2} 92 {x-2} 86" fill="none" stroke="#5DBB4E" stroke-width="4" stroke-linecap="round"/>' for x in (36, 44, 52, 60)) +
    f'<path d="M84 104 V90" stroke="#FFF3D6" stroke-width="8"/><path d="M80 104 V90 H88 V104" fill="none" {W(2)}/>'
    f'<path d="M72 92 Q84 72 96 92Z" fill="#E8434A" {W(2.6)}/><circle cx="80" cy="86" r="2" fill="#fff"/><circle cx="88" cy="84" r="2" fill="#fff"/>'
    f'<g transform="rotate(-35 50 46)"><rect x="34" y="26" width="32" height="44" rx="6" fill="#FFD23F" {W(3.2)}/>'
    f'<path d="M42 70 H58 L54 82 H46Z" fill="#FFD23F" {W(2.6)}/><path d="M50 26 V8" {W(4)}/><rect x="38" y="2" width="24" height="8" rx="3" fill="#7C5CC4" {W(2.6)}/>'
    f'<rect x="40" y="34" width="20" height="20" rx="3" fill="#7CD26E"/></g>'
    + face(48, 50, d=6, k=0.5) + sparkle(108, 30, 5) + sparkle(18, 30, 3.5))

if __name__ == "__main__":
    for pid, (a, b, hero, scene, body) in I.items():
        open(os.path.join(out, pid + ".svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
