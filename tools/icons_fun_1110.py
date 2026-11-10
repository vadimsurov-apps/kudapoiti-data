"""Иконки робота fun (2026-11-10, ночной проход): 43 места из tools/add_fun_1110.py.
Каждая придумана и нарисована отдельно (правило абсолютной уникальности): свой герой, своя сцена, своя палитра.
Сюжеты сверены с листами icons-catalog и icons-src/subjects.txt (скетчбук, гипсовые тела, рубанок, глиняная тарелочка,
пустышка, толокар, сортер, шар-предсказатель уже заняты — поэтому у этих мест другие герои).
Запуск: python3 tools/icons_fun_1110.py  (пишет icons-src/<id>.svg и печатает строки для subjects.txt)"""
import os, math
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


def kid(x, y, k=1.0, hair="#6B3F23"):
    return (f'<circle cx="{x}" cy="{y}" r="{10*k:.1f}" fill="#FFD9B8" {W(2.4)}/>'
            f'<path d="M{x-10*k:.1f} {y-1*k:.1f} Q{x-8*k:.1f} {y-12*k:.1f} {x} {y-11*k:.1f} Q{x+9*k:.1f} {y-11*k:.1f} {x+10*k:.1f} {y-2*k:.1f} Q{x+2*k:.1f} {y-7*k:.1f} {x-10*k:.1f} {y-1*k:.1f}Z" fill="{hair}" {W(2)}/>'
            + face(x, y + 1 * k, d=4 * k, k=0.42 * k))


def star(cx, cy, r1, r2, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r1 if i % 2 == 0 else r2
        a = math.radians(rot + i * 180 / n)
        pts.append(f"{cx + r*math.cos(a):.1f},{cy + r*math.sin(a):.1f}")
    return " ".join(pts)


I = {}

# ---------------- мастер-классы ----------------
I["tsmit-robotics-zamorenova"] = ("#E6F4FF", "#6FA8DC",
    "робот-жучок из жестяной банки на шести проволочных ножках с батарейкой на спине",
    "ползёт по лабораторному столу к горке винтиков и гаек",
    f'<path d="M-2 98 H130 V130 H-2Z" fill="#B98A5E" {W(3)}/>'
    + "".join(f'<path d="M{x} 74 Q{x+d} 86 {x+d*2} 98" fill="none" {W(3)}/>' for x, d in ((42, -6), (56, -4), (70, 4), (84, 6), (48, -2), (78, 2)))
    + f'<rect x="32" y="48" width="64" height="34" rx="16" fill="#C9D3DE" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 50 V80" stroke="#9AA7B6" stroke-width="2"/>' for x in (48, 64, 80)) +
    f'<rect x="50" y="36" width="28" height="13" rx="3" fill="#FFC21A" {W(2.6)}/><rect x="78" y="40" width="4" height="5" fill="#FFC21A" {W(1.6)}/>'
    f'<path d="M56 42 h6 M59 39 v6" stroke="#fff" stroke-width="2"/>'
    f'<path d="M36 56 Q24 40 30 28" fill="none" stroke="#E8434A" stroke-width="3"/><circle cx="30" cy="27" r="3.5" fill="#E8434A" {W(2)}/>'
    f'<path d="M40 52 Q34 36 44 26" fill="none" stroke="#3E7CE8" stroke-width="3"/><circle cx="44" cy="25" r="3.5" fill="#3E7CE8" {W(2)}/>'
    + face(48, 64, d=7, k=0.6) +
    f'<path d="M100 98 L106 86 L112 98Z" fill="#8F9BAA" {W(2)}/>'
    f'<circle cx="114" cy="92" r="4" fill="none" {W(2.4)}/><path d="M98 92 h8" {W(2.4)}/>')

I["kudryashov-kamenshchiki"] = ("#FFF4E0", "#F4B860",
    "мальчик-поварёнок в высоком белом колпаке",
    "раскатывает тесто скалкой за столом домашней кухни с обоями в цветочек",
    "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#F28FA8" opacity=".55"/><circle cx="{x}" cy="{y}" r="1.6" fill="#FFE27A"/>' for x, y in ((14, 30), (34, 14), (100, 22), (116, 44), (16, 60), (110, 70)))
    + f'<path d="M-2 96 H130 V130 H-2Z" fill="#9C6B43" {W(3)}/>'
    f'<path d="M36 70 Q34 96 40 96 H88 Q94 96 92 70Z" fill="#fff" {W(3)}/>'
    + kid(64, 56, 1.35, "#4A2E1A") +
    f'<path d="M48 42 Q42 20 56 22 Q60 10 70 18 Q84 12 82 28 Q86 38 80 42Z" fill="#fff" {W(3)}/><path d="M48 42 H80" {W(3)}/>'
    f'<ellipse cx="64" cy="98" rx="30" ry="6" fill="#F7E4BE" {W(2.6)}/>'
    f'<rect x="30" y="86" width="68" height="8" rx="4" fill="#D9A066" {W(2.6)}/>'
    f'<rect x="20" y="85" width="12" height="10" rx="3" fill="#B87A42" {W(2.2)}/><rect x="96" y="85" width="12" height="10" rx="3" fill="#B87A42" {W(2.2)}/>')

I["slavich-prechistenka"] = ("#FFF8EE", "#E8C9A0",
    "деревянное веретено с пушистым облачком кудели",
    "кружится, вытягивая тонкую нитку, на фоне вышитого красного узора-рушника",
    f'<path d="M-2 92 H130 V130 H-2Z" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M{x} 104 l6 -6 l6 6 l-6 6Z" fill="#D7263D" {W(1.6)}/>' for x in range(4, 128, 16)) +
    f'<path d="M-2 120 H130" stroke="#D7263D" stroke-width="3"/>'
    f'<path d="M30 30 Q16 22 22 10 Q30 0 42 8 Q52 0 58 12 Q66 16 58 26 Q50 34 30 30Z" fill="#F5F0E6" {W(2.6)}/>'
    f'<path d="M46 26 Q60 44 70 50" fill="none" stroke="#C9B48A" stroke-width="2"/>'
    f'<path d="M72 18 Q78 16 80 22 L86 106 Q80 112 74 106Z" fill="#E2A65C" {W(3)}/>'
    f'<ellipse cx="80" cy="70" rx="15" ry="22" fill="#F1E2C3" {W(3)}/>'
    + "".join(f'<path d="M66 {y} Q80 {y+5} 94 {y}" fill="none" stroke="#C9B48A" stroke-width="1.8"/>' for y in (58, 64, 70, 76, 82)) +
    face(80, 68, d=6, k=0.55) +
    f'<path d="M96 40 a10 10 0 0 1 8 14" fill="none" stroke="#fff" stroke-width="3"/><path d="M60 92 a10 10 0 0 1 -6 -12" fill="none" stroke="#fff" stroke-width="3"/>')

I["eventyon-novinsky"] = ("#F3E8FF", "#B58BE6",
    "розовый кейк-попс на палочке, посыпанный цветной крошкой",
    "подмигивает из деревянной подставки, а рядом пристроились два кейк-попса поменьше",
    f'<rect x="20" y="92" width="88" height="22" rx="4" fill="#C98A55" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="96" r="3" fill="#7A4A26"/>' for x in (36, 64, 92)) +
    f'<path d="M64 96 V60 M36 96 V74 M92 96 V76" stroke="#fff" stroke-width="5"/><path d="M64 96 V60 M36 96 V74 M92 96 V76" {W(2)}/>'
    f'<circle cx="36" cy="66" r="11" fill="#6B3F23" {W(2.6)}/><circle cx="92" cy="68" r="11" fill="#FFF1C2" {W(2.6)}/>'
    f'<circle cx="64" cy="46" r="24" fill="#FF8FC0" {W(3.2)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="5" height="2.4" rx="1.2" fill="{c}" transform="rotate({r} {x} {y})"/>' for x, y, c, r in ((50, 30, "#FFE066", 30), (70, 28, "#3EC1D3", -20), (78, 40, "#7A5CFF", 60), (46, 52, "#5CD65C", -40), (80, 56, "#FFE066", 10), (60, 64, "#3EC1D3", 45)))
    + eye(56, 46, 0.75) + f'<path d="M68 46 q4 -3 8 0" fill="none" {W(2.4)}/>'
    + f'<path d="M58 54 Q64 58 70 54" fill="none" {W(2.4)}/>')

I["eventyon-myasnitskaya"] = ("#FFE9D6", "#E8925A",
    "песочное печенье-ромашка с капелькой красного варенья в серединке",
    "выезжает из жаркой духовки на противне, от него поднимается тёплый пар",
    f'<rect x="10" y="24" width="108" height="86" rx="8" fill="#5A5F6B" {W(3)}/>'
    f'<rect x="20" y="34" width="88" height="66" rx="5" fill="#FFB347" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 92 Q{x+6} 86 {x+12} 92" fill="none" stroke="#FF6A00" stroke-width="2.4"/>' for x in (26, 50, 74, 92)) +
    f'<path d="M14 84 H114 L118 96 H10Z" fill="#B7BCC6" {W(3)}/>'
    + "".join(f'<ellipse cx="{64+20*math.cos(math.radians(a)):.1f}" cy="{66+20*math.sin(math.radians(a)):.1f}" rx="12" ry="9" transform="rotate({a} {64+20*math.cos(math.radians(a)):.1f} {66+20*math.sin(math.radians(a)):.1f})" fill="#F3C77A" {W(2.4)}/>' for a in range(0, 360, 45))
    + f'<circle cx="64" cy="66" r="16" fill="#F3C77A" {W(2.6)}/><circle cx="64" cy="66" r="7" fill="#D7263D" {W(2)}/>'
    + face(64, 60, d=11, k=0.5, mouth=False) +
    f'<path d="M40 22 q-4 -8 2 -14 M64 18 q-4 -8 2 -14 M88 22 q-4 -8 2 -14" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["art-sloboda-nagatinskaya"] = ("#E9FFF4", "#61C99A",
    "квадратная формочка-рамка, заполненная цветными стёклышками мозаики",
    "в неё пинцетом кладут последний камешек, и из мозаики складывается солнышко",
    f'<rect x="22" y="30" width="72" height="72" rx="6" fill="#8C6239" {W(3.2)}/><rect x="30" y="38" width="56" height="56" fill="#3A7BD5" {W(2.4)}/>'
    + "".join(f'<rect x="{30+i*8}" y="{38+j*8}" width="7" height="7" fill="{"#FFC93C" if (i-3)**2+(j-3)**2 < 5 else ("#FF8A3C" if (i-3)**2+(j-3)**2 < 8 else "#5DADE2")}"/>' for i in range(7) for j in range(7) if not (i == 6 and j == 0))
    + face(58, 66, d=8, k=0.6) +
    f'<rect x="78" y="38" width="7" height="7" fill="#FFEDB3" stroke="{O}" stroke-width="1.5" transform="translate(16 -20)"/>'
    f'<path d="M98 14 L120 2 M104 22 L124 10" {W(3)}/><path d="M98 14 L92 20 L96 22 L104 22" fill="#C0C7D1" {W(2.4)}/>'
    + sparkle(110, 50, 5) + sparkle(16, 112, 4))

I["vysotskaya-ordzhonikidze"] = ("#E5F6FF", "#5AB0E8",
    "песочное печенье-самолётик с голубой сахарной глазурью",
    "взлетает с противня, оставляя за собой пунктир из сахарной пудры",
    f'<path d="M-2 104 L130 96 V130 H-2Z" fill="#A7AFBA" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#fff"/>' for x, y in ((16, 98), (26, 92), (36, 86), (46, 80)))
    + f'<path d="M50 70 Q60 52 96 46 Q114 44 116 52 Q114 60 96 62 Q70 70 50 70Z" fill="#E9B872" {W(3.2)}/>'
    f'<path d="M78 56 L60 30 L72 30 L94 54Z" fill="#E9B872" {W(3)}/><path d="M80 62 L66 84 L76 84 L94 62Z" fill="#E9B872" {W(3)}/>'
    f'<path d="M50 70 L42 52 L52 54 L58 66Z" fill="#E9B872" {W(2.6)}/>'
    f'<path d="M64 60 Q80 52 106 50" fill="none" stroke="#7FD0F5" stroke-width="5" stroke-linecap="round"/>'
    + f'<circle cx="104" cy="52" r="3" fill="#fff" {W(1.6)}/>' + face(86, 58, d=6, k=0.5))

I["kot-filius-cdm"] = ("#FFF5D6", "#E8B93A",
    "деревянная игрушка-дергунчик — шут в колпаке с бубенчиками",
    "дёргают за ниточку снизу, и он взмахивает ручками и ножками над столом мастерской",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#B07A45" {W(3)}/>'
    f'<path d="M64 84 V118" stroke="#fff" stroke-width="2"/><circle cx="64" cy="118" r="4" fill="#E8434A" {W(2)}/>'
    f'<path d="M50 50 L22 26 L18 34 L46 58Z" fill="#E8434A" {W(2.6)}/><path d="M78 50 L106 26 L110 34 L82 58Z" fill="#2E86DE" {W(2.6)}/>'
    f'<path d="M54 80 L36 106 L44 110 L60 84Z" fill="#2E86DE" {W(2.6)}/><path d="M74 80 L92 106 L84 110 L68 84Z" fill="#E8434A" {W(2.6)}/>'
    f'<rect x="46" y="46" width="36" height="40" rx="6" fill="#F6D58E" {W(3)}/><path d="M46 66 H82" {W(2)}/>'
    f'<circle cx="64" cy="36" r="13" fill="#F6D58E" {W(2.8)}/>'
    f'<path d="M50 30 L40 10 L58 24 L64 6 L70 24 L88 10 L78 30Z" fill="#7A5CFF" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#FFD23F" {W(1.6)}/>' for x, y in ((40, 10), (64, 6), (88, 10)))
    + face(64, 38, d=5, k=0.5))

I["kremlevsky-dom-remesel"] = ("#F6EDE2", "#C79A6B",
    "богородская игрушка — мужик и медведь-кузнецы с молоточками у наковальни",
    "по очереди стучат по наковальне, когда сдвигают планочки, на фоне шатровых башенок",
    "".join(f'<path d="M{x} 54 V30 L{x+8} 14 L{x+16} 30 V54Z" fill="#fff" opacity=".55"/>' for x in (8, 104)) +
    f'<rect x="10" y="94" width="108" height="8" rx="2" fill="#E8C48E" {W(2.6)}/><rect x="16" y="104" width="96" height="8" rx="2" fill="#E8C48E" {W(2.6)}/>'
    f'<path d="M54 94 V82 H74 V94 M48 82 H80 L76 74 H52Z" fill="#7A7F88" {W(2.6)}/>'
    # мужик
    f'<rect x="20" y="58" width="22" height="36" rx="6" fill="#F0D3A8" {W(2.6)}/><circle cx="31" cy="48" r="11" fill="#F0D3A8" {W(2.6)}/>'
    f'<path d="M22 50 Q31 66 40 50" fill="#E8C48E" {W(2)}/>' + face(31, 46, d=4, k=0.4) +
    f'<path d="M40 64 L56 56" {W(3)}/><rect x="52" y="48" width="12" height="8" rx="2" fill="#8C6239" {W(2)}/>'
    # медведь
    f'<rect x="86" y="56" width="24" height="38" rx="8" fill="#B07A45" {W(2.6)}/><circle cx="98" cy="46" r="12" fill="#B07A45" {W(2.6)}/>'
    f'<circle cx="89" cy="36" r="4.5" fill="#B07A45" {W(2.2)}/><circle cx="107" cy="36" r="4.5" fill="#B07A45" {W(2.2)}/>'
    + face(98, 46, d=4.5, k=0.42) +
    f'<path d="M88 64 L74 50" {W(3)}/><rect x="64" y="40" width="12" height="8" rx="2" fill="#8C6239" {W(2)}/>'
    + sparkle(64, 66, 4, "#FFD23F"))

I["tsekh-kreativa-kazenny"] = ("#E8E9FF", "#7B7FE0",
    "катушка цветного радужного скотча",
    "катится по полу и обматывает картонную коробку, превращая её в ракету",
    f'<path d="M78 104 V54 L94 30 L110 54 V104Z" fill="#D9B07A" {W(3)}/><path d="M78 104 L70 116 H118 L110 104" fill="#C98A55" {W(2.6)}/>'
    + "".join(f'<path d="M78 {y} H110" stroke="{c}" stroke-width="5"/>' for y, c in ((62, "#FF5C8A"), (72, "#FFC93C"), (82, "#5CD65C"), (92, "#3EA8E8")))
    + f'<circle cx="94" cy="44" r="5" fill="#BFE6FF" {W(2)}/>'
    f'<path d="M50 88 Q66 84 78 82" stroke="#FF5C8A" stroke-width="6" fill="none"/>'
    f'<circle cx="40" cy="80" r="26" fill="url(#rb)" {W(3.2)}/>'
    f'<defs><linearGradient id="rb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF5C8A"/><stop offset=".35" stop-color="#FFC93C"/><stop offset=".7" stop-color="#5CD65C"/><stop offset="1" stop-color="#3EA8E8"/></linearGradient></defs>'
    f'<circle cx="40" cy="80" r="11" fill="#E8E9FF" {W(2.6)}/>' + face(40, 72, d=12, k=0.5, mouth=False)
    + f'<path d="M36 96 Q40 100 44 96" fill="none" {W(2.4)}/>' + sparkle(24, 30, 5) + sparkle(56, 20, 3))

I["art-zebra-gruzinskaya"] = ("#E3FFE9", "#4CC27A",
    "кисточка с полосатой чёрно-белой ручкой",
    "рисует широкую радужную полосу через белый лист, приклеенный к столу",
    f'<path d="M8 66 L112 52 L118 108 L14 118Z" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M18 {104-i*6} Q60 {90-i*6} 102 {80-i*6}" fill="none" stroke="{c}" stroke-width="6" stroke-linecap="round"/>' for i, c in enumerate(("#3EA8E8", "#5CD65C", "#FFC93C", "#FF5C8A")))
    + f'<g transform="rotate(38 84 44)"><rect x="78" y="-6" width="14" height="58" rx="6" fill="#fff" {W(3)}/>'
    + "".join(f'<path d="M78 {y} H92" stroke="#222" stroke-width="5"/>' for y in (2, 12, 22, 32, 42))
    + f'<rect x="78" y="-6" width="14" height="58" rx="6" fill="none" {W(3)}/><rect x="76" y="50" width="18" height="10" fill="#C0C7D1" {W(2.4)}/>'
    f'<path d="M77 60 Q85 82 93 60Z" fill="#FF5C8A" {W(2.6)}/></g>'
    + face(66, 92, d=8, k=0.55))

I["estetika-severyanovoy"] = ("#FFE6EE", "#E77A9C",
    "фетровый кактус в горшочке, сшитый вручную",
    "его дошивают иголкой с длинной красной ниткой прямо на столе детского мастер-класса",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#F7C6D6" {W(3)}/>'
    f'<path d="M40 84 H88 L82 112 H46Z" fill="#E07A3E" {W(3)}/><rect x="36" y="78" width="56" height="10" rx="3" fill="#F09A5E" {W(2.6)}/>'
    f'<path d="M50 78 V40 Q50 24 64 24 Q78 24 78 40 V78Z" fill="#5CBF6A" {W(3.2)}/>'
    f'<path d="M50 58 H40 Q32 58 32 48 V38" fill="none" stroke="{O}" stroke-width="13" stroke-linecap="round"/><path d="M50 58 H40 Q32 58 32 48 V38" fill="none" stroke="#5CBF6A" stroke-width="7.6" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y} h4" stroke="#fff" stroke-width="1.6" stroke-dasharray="1.5 2"/>' for x, y in ((54, 34), (66, 30), (56, 66), (68, 70), (36, 44)))
    + face(64, 50, d=7, k=0.55) +
    f'<circle cx="64" cy="22" r="5" fill="#FF7FA8" {W(2)}/>'
    f'<path d="M78 50 Q100 36 108 14" fill="none" stroke="#D7263D" stroke-width="2.4"/>'
    f'<path d="M104 24 L114 4" stroke="#C0C7D1" stroke-width="3" stroke-linecap="round"/><ellipse cx="112" cy="8" rx="1.4" ry="2.6" fill="#fff"/>')

I["goncharnoe-delo-ovchinnikovsky"] = ("#E8F1FF", "#7393C9",
    "две глиняные пиалы — большая и маленькая, как мама с малышом",
    "сидят рядышком на гончарном круге и держатся за ручки-завитки после семейного мастер-класса",
    f'<ellipse cx="64" cy="100" rx="52" ry="12" fill="#9AA7B6" {W(3)}/><ellipse cx="64" cy="96" rx="52" ry="12" fill="#C9D3DE" {W(3)}/>'
    f'<path d="M14 60 Q16 92 44 92 Q72 92 74 60Z" fill="#C8875A" {W(3.2)}/><ellipse cx="44" cy="60" rx="30" ry="7" fill="#A86A40" {W(3)}/>'
    + face(44, 74, d=9, k=0.7) +
    f'<path d="M80 74 Q82 92 96 92 Q110 92 112 74Z" fill="#E3A87A" {W(3)}/><ellipse cx="96" cy="74" rx="16" ry="4.5" fill="#C8875A" {W(2.6)}/>'
    + face(96, 82, d=5, k=0.45) +
    f'<path d="M72 74 Q78 66 84 78" fill="none" {W(3)}/>'
    f'<path d="M50 44 Q54 34 60 40 Q64 32 66 42" fill="none" stroke="#FF7FA8" stroke-width="3"/>')

I["simfoniya-vkusa-tikhvinskaya"] = ("#FFF0F0", "#E06666",
    "песочное печенье в форме скрипичного ключа с сахарной обсыпкой",
    "лежит на противне, расчерченном нотными линейками, среди печенек-нот",
    f'<rect x="4" y="30" width="120" height="84" rx="6" fill="#B7BCC6" {W(3)}/>'
    + "".join(f'<path d="M4 {y} H124" stroke="#8F96A3" stroke-width="2"/>' for y in (46, 58, 70, 82, 94)) +
    f'<path d="M58 104 Q44 104 48 92 Q52 84 62 88 Q70 92 64 100 M62 100 L56 30 Q56 16 66 18 Q74 22 66 36 L44 60 Q34 72 46 82 Q60 90 74 80 Q82 70 72 62 Q60 56 56 68" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M58 104 Q44 104 48 92 Q52 84 62 88 Q70 92 64 100 M62 100 L56 30 Q56 16 66 18 Q74 22 66 36 L44 60 Q34 72 46 82 Q60 90 74 80 Q82 70 72 62 Q60 56 56 68" fill="none" stroke="#E9B872" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.3" fill="#fff"/>' for x, y in ((58, 40), (48, 66), (66, 84), (72, 70), (60, 26)))
    + face(58, 74, d=6, k=0.5) +
    "".join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="4.5" fill="#E9B872" {W(2)}/><path d="M{x+5} {y} V{y-16}" {W(2.4)}/>' for x, y in ((96, 82), (108, 58), (22, 58))))

I["mendeleev-center-miusskaya"] = ("#1E2A44", "#0E1424",
    "золотая клеточка таблицы Менделеева «Au 79»",
    "сияет на полке лаборатории между пробирками с цветными растворами",
    f'<circle cx="64" cy="58" r="44" fill="#FFD23F" opacity=".18"/>'
    f'<rect x="38" y="28" width="52" height="58" rx="5" fill="#FFC21A" {W(3.2)}/><rect x="42" y="32" width="44" height="50" rx="3" fill="none" stroke="#FFE38A" stroke-width="2"/>'
    f'<text x="45" y="44" font-family="Arial" font-size="9" font-weight="bold" fill="{O}">79</text>'
    f'<text x="64" y="62" font-family="Arial" font-size="20" font-weight="bold" fill="{O}" text-anchor="middle">Au</text>'
    + face(64, 72, d=9, k=0.45, mouth=True) +
    f'<path d="M-2 94 H130 V100 H-2Z" fill="#8C6239" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 92 V66 h8 V92 Q{x+4} 98 {x} 92Z" fill="#fff" fill-opacity=".25" {W(2.2)}/><path d="M{x+0.5} 92 V80 h7 V92 Q{x+4} 96 {x+0.5} 92Z" fill="{c}"/>' for x, c in ((14, "#5CD65C"), (24, "#FF5C8A"), (98, "#3EC1D3"), (108, "#B07CFF")))
    + sparkle(100, 30, 5, "#FFE066") + sparkle(26, 34, 3, "#FFE066"))

I["polyana-leninsky-99"] = ("#F2FFE0", "#9BD35A",
    "детский фартучек весь в разноцветных кляксах краски",
    "висит на крючке над столом изостудии, а из кармашка торчат кисточки",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#E6D3A8" {W(3)}/>'
    f'<circle cx="64" cy="16" r="4" fill="#8F9BAA" {W(2)}/><path d="M52 30 Q64 10 76 30" fill="none" {W(3)}/>'
    f'<path d="M48 30 H80 V46 Q96 48 96 64 L90 100 Q64 108 38 100 L32 64 Q32 48 48 46Z" fill="#fff" {W(3.2)}/>'
    + "".join(f'<path d="M{x} {y} q4 -6 8 0 q6 2 2 8 q-2 6 -8 2 q-6 -2 -2 -10Z" fill="{c}"/>' for x, y, c in ((40, 60, "#FF5C8A"), (74, 56, "#3EA8E8"), (58, 84, "#FFC93C"), (80, 82, "#7A5CFF"), (42, 86, "#5CD65C")))
    + f'<rect x="52" y="62" width="24" height="16" rx="3" fill="#FFE8A3" {W(2.4)}/>'
    f'<path d="M58 62 V44 M66 62 V40 M72 62 V46" {W(2.4)}/><path d="M56 44 l2 -6 l2 6Z M64 40 l2 -6 l2 6Z" fill="#FF5C8A" {W(1.6)}/>'
    + face(64, 92, d=7, k=0.45) + sparkle(110, 34, 5) + sparkle(18, 40, 4))

I["germes-lineyny"] = ("#E0F4FF", "#3E8FD6",
    "крылатая сандалия с ремешками-ленточками",
    "летит над облаками и несёт на ремешке золотую медальку за творчество",
    "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*0.45:.1f}" fill="#fff" opacity=".85"/>' for x, y, r in ((24, 100, 22), (96, 108, 26), (60, 116, 18)))
    + f'<path d="M26 82 Q30 70 46 70 H86 Q104 70 104 82 Q104 88 96 88 H34 Q26 88 26 82Z" fill="#C98A55" {W(3.2)}/>'
    f'<path d="M44 74 L84 52 M58 76 L96 56 M48 54 L86 74" fill="none" stroke="#8C6239" stroke-width="5" stroke-linecap="round"/><path d="M44 74 L84 52 M58 76 L96 56 M48 54 L86 74" fill="none" stroke="#E8C48E" stroke-width="2" stroke-linecap="round"/>'
    f'<path d="M30 74 Q8 64 6 46 Q20 56 22 50 Q14 40 18 30 Q28 46 34 44 Q32 34 38 26 Q42 46 44 64Z" fill="#fff" {W(2.8)}/>'
    f'<path d="M92 50 L100 66" stroke="#E8434A" stroke-width="3"/><circle cx="102" cy="70" r="9" fill="#FFC21A" {W(2.6)}/>'
    f'<polygon points="{star(102, 70, 5, 2.2)}" fill="#fff"/>'
    + face(66, 80, d=8, k=0.5))

# ---------------- квесты ----------------
I["wonderloom-izmaylovsky"] = ("#2A1B3D", "#140B22",
    "волшебный деревянный ткацкий станок со светящимися нитями",
    "в тёмной комнате сам ткёт полотно, на котором проступает карта с крестиком",
    f'<path d="M24 20 V112 M104 20 V112" stroke="#8C6239" stroke-width="8"/><path d="M24 20 V112 M104 20 V112" fill="none" {W(2)}/>'
    f'<rect x="18" y="14" width="92" height="10" rx="3" fill="#B07A45" {W(2.6)}/><rect x="18" y="100" width="92" height="10" rx="3" fill="#B07A45" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 24 V58" stroke="#9EF0FF" stroke-width="1.6"/>' for x in range(32, 100, 6)) +
    f'<rect x="30" y="58" width="68" height="42" fill="#F2E3C2" {W(2.6)}/>'
    + "".join(f'<path d="M30 {y} H98" stroke="#E2CDA0" stroke-width="1.4"/>' for y in range(62, 100, 5)) +
    f'<path d="M38 92 Q50 70 64 82 T88 66" fill="none" stroke="#B07A45" stroke-width="2" stroke-dasharray="3 3"/>'
    f'<path d="M84 62 l8 8 M92 62 l-8 8" stroke="#E8434A" stroke-width="3"/>'
    f'<rect x="28" y="50" width="72" height="8" rx="3" fill="#D9A066" {W(2.4)}/>'
    + face(64, 40, d=9, k=0.55) + sparkle(14, 50, 4, "#9EF0FF") + sparkle(116, 38, 5, "#9EF0FF") + sparkle(64, 8, 3, "#FFE066"))

I["podzemka-veskovsky"] = ("#8A6440", "#4A321E",
    "крот в жёлтой шахтёрской каске с фонарём на лбу",
    "прокопал подземный ход и освещает фонарём сундучок, светящийся в конце тоннеля",
    f'<path d="M-2 40 Q40 30 70 52 T130 60 V130 H-2Z" fill="#5E4129"/>'
    f'<ellipse cx="96" cy="88" rx="30" ry="22" fill="#2B1C10" {W(3)}/>'
    f'<path d="M58 54 L100 76 L100 100 L58 70Z" fill="#FFF3A0" opacity=".45"/>'
    f'<rect x="88" y="82" width="22" height="14" rx="2" fill="#C98A55" {W(2.4)}/><path d="M88 86 H110" {W(2)}/><circle cx="99" cy="89" r="2" fill="#FFD23F"/>'
    f'<ellipse cx="38" cy="82" rx="26" ry="24" fill="#5A5560" {W(3.2)}/>'
    f'<ellipse cx="50" cy="90" rx="8" ry="5" fill="#FFB3C7" {W(2.2)}/>'
    f'<path d="M14 64 Q38 40 62 64Z" fill="#FFC21A" {W(3)}/><rect x="10" y="62" width="56" height="6" rx="3" fill="#FFC21A" {W(2.4)}/>'
    f'<rect x="52" y="52" width="10" height="9" rx="2" fill="#fff" {W(2)}/>'
    + eye(32, 78, 0.55) + eye(46, 78, 0.55) +
    f'<path d="M14 100 q-6 4 -4 10 M20 104 q-4 6 0 10" fill="none" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#7A5638"/>' for x, y in ((20, 26), (60, 30), (112, 30), (10, 50))))

I["kvest-sdaetsya-kvartira"] = ("#FFF7E0", "#D9B44A",
    "круглая кнопка дверного звонка с латунной рамкой",
    "трезвонит у загадочной двери с табличкой «СДАЁТСЯ», и от неё разлетаются звонкие волны",
    f'<rect x="14" y="14" width="56" height="112" rx="4" fill="#7A4A2A" {W(3.2)}/>'
    f'<rect x="22" y="24" width="40" height="38" rx="3" fill="none" stroke="#5A3418" stroke-width="2.4"/><rect x="22" y="70" width="40" height="44" rx="3" fill="none" stroke="#5A3418" stroke-width="2.4"/>'
    f'<circle cx="58" cy="78" r="3.5" fill="#FFC21A" {W(2)}/>'
    f'<rect x="20" y="34" width="44" height="14" rx="2" fill="#fff" {W(2)}/>'
    f'<text x="42" y="44.5" font-family="Arial" font-size="7.5" font-weight="bold" fill="#D7263D" text-anchor="middle">СДАЁТСЯ</text>'
    f'<circle cx="94" cy="64" r="22" fill="#D9A43A" {W(3.2)}/><circle cx="94" cy="64" r="14" fill="#FFF3D0" {W(2.6)}/>'
    + face(94, 62, d=5, k=0.45) +
    "".join(f'<path d="M{94+r} {64-r*0.8:.0f} a{r} {r} 0 0 1 0 {r*1.6:.0f}" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for r in (28, 34)))

I["komponent-boensky"] = ("#E5FFF8", "#3FB8A0",
    "красный проводок-змейка с зубастыми зажимами-крокодильчиками на концах",
    "соединяет две половинки загадочного пульта, и на пульте загорается зелёная лампочка",
    f'<rect x="10" y="62" width="48" height="50" rx="6" fill="#5A6472" {W(3)}/><rect x="70" y="62" width="48" height="50" rx="6" fill="#5A6472" {W(3)}/>'
    f'<circle cx="34" cy="80" r="8" fill="#9BE36A" {W(2.4)}/><circle cx="34" cy="80" r="14" fill="#9BE36A" opacity=".3"/>'
    + "".join(f'<rect x="{x}" y="96" width="8" height="8" rx="2" fill="{c}" {W(1.8)}/>' for x, c in ((18, "#FFC93C"), (30, "#FF5C8A"), (42, "#3EA8E8"), (78, "#3EA8E8"), (90, "#FFC93C"), (102, "#FF5C8A")))
    + f'<circle cx="94" cy="80" r="7" fill="#C9D3DE" {W(2.4)}/><path d="M94 80 l4 -4" {W(2)}/>'
    f'<path d="M30 64 Q30 20 64 26 Q98 32 96 64" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/><path d="M30 64 Q30 20 64 26 Q98 32 96 64" fill="none" stroke="#E8434A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M24 60 L36 60 L34 70 L26 70Z" fill="#C0C7D1" {W(2)}/><path d="M90 60 L102 60 L100 70 L92 70Z" fill="#C0C7D1" {W(2)}/>'
    + face(64, 30, d=6, k=0.42) + sparkle(110, 18, 4) + sparkle(14, 30, 3))

# ---------------- игровые, клубы, праздники ----------------
I["davayte-vmeste-sretensky"] = ("#FFEBD9", "#F08A4B",
    "семейка из трёх вязаных варежек — папиной, маминой и малышовой — на одной верёвочке",
    "сушатся рядышком на тёплой батарее, держась за общий шнурок",
    f'<rect x="4" y="88" width="120" height="30" rx="4" fill="#E9EDF2" {W(3)}/>'
    + "".join(f'<path d="M{x} 90 V116" stroke="#C3CAD4" stroke-width="3"/>' for x in range(14, 124, 10)) +
    f'<path d="M6 30 Q64 52 122 30" fill="none" stroke="#fff" stroke-width="3"/>'
    + "".join(f'<path d="M{x} {y} q0 -6 6 -6 h{w-12} q6 0 6 6 v{h} q0 {w/2:.0f} -{w/2:.0f} {w/2:.0f} q-{w/2:.0f} 0 -{w/2:.0f} -{w/2:.0f}Z" fill="{c}" {W(3)}/>'
              f'<ellipse cx="{x-3}" cy="{y+h*0.5:.0f}" rx="{w*0.22:.1f}" ry="{h*0.3:.1f}" fill="{c}" {W(2.4)}/>'
              f'<rect x="{x}" y="{y-6}" width="{w}" height="8" rx="3" fill="#fff" {W(2)}/>'
              + face(x + w / 2, y + h * 0.5, d=w * 0.18, k=w / 60) for x, y, w, h, c in ((14, 40, 30, 34, "#3E7CE8"), (52, 46, 26, 30, "#E8434A"), (86, 52, 20, 22, "#FFC21A"))))

I["grusha-berzarina"] = ("#E9F7FF", "#8CC8EE",
    "зайчик, вылепленный из кинетического песка",
    "сидит в песочнице игровой комнаты рядом с перевёрнутой формочкой-звездой",
    f'<rect x="-2" y="80" width="132" height="50" fill="#F2D49B" {W(3)}/>'
    f'<path d="M-2 80 H130" stroke="#C99A55" stroke-width="5"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.3" fill="#C99A55"/>' for x, y in ((14, 96), (30, 110), (100, 98), (116, 112), (80, 118), (50, 120)))
    + f'<path d="M48 36 Q44 6 54 6 Q62 8 58 38Z M70 38 Q66 8 74 6 Q84 6 80 36Z" fill="#F7B6C8" {W(2.8)}/>'
    f'<ellipse cx="64" cy="82" rx="26" ry="18" fill="#F7B6C8" {W(3)}/><circle cx="64" cy="54" r="20" fill="#F7B6C8" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1" fill="#E58AA6"/>' for x, y in ((52, 48), (74, 62), (58, 86), (72, 90), (50, 80), (66, 44)))
    + face(64, 54, d=7, k=0.6) +
    f'<polygon points="{star(104, 96, 13, 6)}" fill="#5DADE2" {W(2.6)}/><path d="M86 70 l6 8 M96 66 l2 8" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>')

I["krylatye-kacheli-yamskogo"] = ("#F0E9FF", "#9C7BE8",
    "доска-качели с белыми крылышками",
    "взмывает под самый потолок игровой, а внизу ждут мягкие разноцветные маты",
    f'<path d="M30 -2 L52 70 M98 -2 L76 70" stroke="#8C6239" stroke-width="3"/>'
    + "".join(f'<rect x="{x}" y="108" width="34" height="22" rx="4" fill="{c}" {W(3)}/>' for x, c in ((-6, "#FF8FB1"), (28, "#FFD25E"), (62, "#7FD0F5"), (96, "#8BE08B")))
    + f'<path d="M44 66 Q20 46 8 58 Q16 64 12 72 Q26 70 30 78Z" fill="#fff" {W(2.8)}/><path d="M84 66 Q108 46 120 58 Q112 64 116 72 Q102 70 98 78Z" fill="#fff" {W(2.8)}/>'
    f'<rect x="36" y="66" width="56" height="14" rx="5" fill="#FF7A45" {W(3)}/>'
    + face(64, 72, d=9, k=0.5) +
    f'<path d="M28 96 q4 -4 8 0 M94 92 q4 -4 8 0" fill="none" stroke="#fff" stroke-width="2.4"/>' + sparkle(64, 30, 6) + sparkle(110, 26, 3))

I["parovozovo-salyama-adilya"] = ("#FFEDE8", "#E5735E",
    "железнодорожная стрелка с рычагом и красно-белым флажком",
    "переводит игрушечную дорогу на ковре игровой, и рельсы расходятся в две стороны",
    f'<path d="M-2 70 H130 V130 H-2Z" fill="#7BC6A4" {W(3)}/>'
    f'<path d="M20 130 L56 70 M48 130 L70 70" stroke="#8C6239" stroke-width="4"/>'
    f'<path d="M56 70 Q60 60 40 40 M70 70 Q74 56 54 36" fill="none" stroke="#8C6239" stroke-width="4"/>'
    f'<path d="M56 70 Q70 54 100 46 M70 70 Q84 62 108 58" fill="none" stroke="#8C6239" stroke-width="4"/>'
    + "".join(f'<path d="M{x} {y} l{dx} 0" stroke="#C9A06A" stroke-width="4"/>' for x, y, dx in ((26, 120, 26), (34, 104, 24), (42, 88, 22)))
    + f'<rect x="78" y="86" width="30" height="14" rx="3" fill="#5A6472" {W(2.6)}/>'
    f'<path d="M92 88 L104 50" stroke="{O}" stroke-width="6" stroke-linecap="round"/><path d="M92 88 L104 50" stroke="#C0C7D1" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="104" cy="48" r="7" fill="#E8434A" {W(2.4)}/>'
    f'<path d="M104 42 V20 L124 26 L104 32" fill="#fff" {W(2.4)}/><path d="M104 20 L114 23 L114 29 L104 32Z" fill="#E8434A"/>'
    + face(93, 93, d=5, k=0.38))

I["osminozhki-korabelnaya"] = ("#E3F7FF", "#56B4D8",
    "пара зелёных резиновых сапожек с лягушачьими глазками на носках",
    "прыгают по лужам у входа в детский клуб, разбрызгивая капли",
    f'<ellipse cx="64" cy="112" rx="54" ry="12" fill="#7FC4E8" {W(3)}/>'
    + "".join(f'<path d="M{x} 30 V{y} Q{x} {y+16} {x+14} {y+16} H{x+34} Q{x+40} {y+16} {x+40} {y+8} Q{x+40} {y} {x+28} {y} H{x+20} V30Z" fill="#4CBF5A" {W(3.2)}/>'
              f'<rect x="{x-2}" y="26" width="24" height="8" rx="3" fill="#E8434A" {W(2.4)}/>'
              f'<circle cx="{x+28}" cy="{y-2}" r="6" fill="#fff" {W(2.4)}/><circle cx="{x+36}" cy="{y-2}" r="6" fill="#fff" {W(2.4)}/>'
              f'<circle cx="{x+29}" cy="{y-1}" r="2.6" fill="{O}"/><circle cx="{x+37}" cy="{y-1}" r="2.6" fill="{O}"/>'
              f'<path d="M{x+26} {y+8} Q{x+32} {y+12} {x+38} {y+8}" fill="none" {W(2.2)}/>' for x, y in ((10, 82), (58, 74)))
    + "".join(f'<path d="M{x} {y} q3 -6 6 0 q0 4 -3 4 q-3 0 -3 -4Z" fill="#BFE6FF" {W(1.6)}/>' for x, y in ((8, 100), (110, 92), (100, 70), (24, 64))))

I["alfi-detki-magellana"] = ("#FFF0FA", "#E78ACB",
    "игрушка-каталка на длинной палочке с хлопающими крыльями-бабочкой",
    "малыш катит её по ковру клуба, и крылышки на колёсиках весело хлопают",
    f'<path d="M-2 104 H130 V130 H-2Z" fill="#FFD9EC" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="114" r="3" fill="#F5A3CF"/>' for x in range(10, 128, 18)) +
    f'<path d="M64 98 L108 22" stroke="#E2A65C" stroke-width="6" stroke-linecap="round"/><path d="M64 98 L108 22" fill="none" {W(2)}/>'
    f'<circle cx="108" cy="20" r="5" fill="#E8434A" {W(2.2)}/>'
    f'<path d="M60 86 Q30 52 18 70 Q14 86 48 92Z" fill="#7A5CFF" {W(3)}/><path d="M68 86 Q98 50 110 68 Q114 84 80 92Z" fill="#FFC93C" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#fff" opacity=".8"/>' for x, y in ((30, 72), (98, 70)))
    + f'<ellipse cx="64" cy="88" rx="8" ry="14" fill="#FF5C8A" {W(2.6)}/>' + face(64, 84, d=3.5, k=0.32) +
    f'<circle cx="50" cy="102" r="7" fill="#3EA8E8" {W(2.6)}/><circle cx="78" cy="102" r="7" fill="#3EA8E8" {W(2.6)}/>'
    f'<path d="M22 54 q-6 -4 -6 -10 M106 54 q6 -4 6 -10" fill="none" stroke="#fff" stroke-width="2.4"/>')

I["rumvil-monakhovoy"] = ("#7A4FB8", "#2E2250",
    "праздничная свечка в форме цифры «5» с огоньком",
    "подмигивает гостям в комнате для праздника под гирляндой из флажков",
    f'<path d="M-2 18 Q64 44 130 18" fill="none" stroke="#fff" stroke-width="2"/>'
    + "".join(f'<path d="M{x} {18+12*math.sin(math.pi*(x+2)/132):.0f} l6 12 l6 -12Z" fill="{c}" {W(1.6)}/>' for x, c in ((10, "#FF5C8A"), (28, "#FFC93C"), (46, "#3EC1D3"), (70, "#5CD65C"), (88, "#FF8F3C"), (106, "#FF5C8A")))
    + f'<path d="M48 104 H80" stroke="#fff" stroke-width="3"/><ellipse cx="64" cy="108" rx="34" ry="8" fill="#FFE3F0" {W(3)}/>'
    f'<path d="M82 46 H52 L48 72 Q60 64 72 68 Q84 74 80 88 Q74 104 52 98" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M82 46 H52 L48 72 Q60 64 72 68 Q84 74 80 88 Q74 104 52 98" fill="none" stroke="#5BC0F8" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M58 46 V36" {W(2.4)}/><path d="M58 36 Q50 26 58 16 Q66 26 58 36Z" fill="#FFC21A" {W(2.4)}/><path d="M58 33 Q55 28 58 23 Q61 28 58 33Z" fill="#FF7A00"/>'
    + eye(62, 80, 0.6) + f'<path d="M70 78 q4 -3 8 0" fill="none" {W(2.4)}/>'
    + sparkle(104, 74, 5, "#FFE066") + sparkle(22, 80, 4, "#FFE066"))

I["skazkadarium-fadeeva"] = ("#EAF8E3", "#7CC46A",
    "румяный колобок",
    "катится по лесной тропинке мимо пенька с грибочком",
    f'<path d="M-2 82 Q64 70 130 86 V130 H-2Z" fill="#6DB35A" {W(3)}/>'
    f'<path d="M30 130 Q50 96 80 84 Q100 78 130 80 V96 Q98 94 82 100 Q60 110 54 130Z" fill="#E6C88E" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 74 L{x+12} 34 L{x+24} 74Z" fill="#2F8A4A" {W(2.4)}/>' for x in (-4, 96))
    + f'<path d="M16 96 V82 H34 V96Z" fill="#B07A45" {W(2.6)}/><ellipse cx="25" cy="82" rx="9" ry="3" fill="#E2B57E" {W(2)}/>'
    f'<path d="M36 96 V90" {W(2)}/><path d="M30 90 Q36 80 42 90Z" fill="#E8434A" {W(2)}/>'
    f'<circle cx="74" cy="72" r="26" fill="#F7B544" {W(3.2)}/><ellipse cx="66" cy="62" rx="9" ry="5" fill="#FFD98A" opacity=".8"/>'
    + face(78, 74, d=8, k=0.7) +
    f'<path d="M40 64 h-12 M44 76 h-16 M40 88 h-10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

# ---------------- третья партия ----------------
I["mamin-sadik-karetny"] = ("#FFF9EE", "#EAB676",
    "полосатый тканевый гамак с подушкой-облачком",
    "мерно качается между двумя деревьями сада, а в нём сладко дремлет малыш",
    f'<path d="M14 130 V40 M114 130 V40" stroke="#8C6239" stroke-width="9"/><path d="M14 130 V40 M114 130 V40" fill="none" {W(2)}/>'
    f'<circle cx="14" cy="34" r="20" fill="#6DBF5A" {W(3)}/><circle cx="114" cy="34" r="20" fill="#6DBF5A" {W(3)}/>'
    f'<path d="M14 58 Q64 104 114 58" fill="none" {W(2.6)}/>'
    f'<path d="M20 60 Q64 112 108 60 Q64 92 20 60Z" fill="#FF8FB1" {W(3)}/>'
    + "".join(f'<path d="M{x} {64+0.9*(x-20) if x < 64 else 64+0.9*(108-x):.0f} Q{x+2} {90 if 40 < x < 88 else 76} {x+4} {64+0.9*(x-16) if x < 64 else 64+0.9*(104-x):.0f}" fill="none" stroke="#fff" stroke-width="3"/>' for x in (36, 52, 68, 84))
    + f'<ellipse cx="44" cy="72" rx="12" ry="7" fill="#fff" {W(2.4)}/>'
    + kid(56, 72, 0.9, "#E2A65C") +
    f'<path d="M80 52 q4 -6 8 0 M90 42 q3 -5 6 0" fill="none" stroke="#7A5CFF" stroke-width="2.4"/>'
    f'<text x="94" y="34" font-family="Arial" font-size="10" font-weight="bold" fill="#7A5CFF">z</text>')

I["maksimum-barklaya"] = ("#E8F0F8", "#7E98B5",
    "синяя столярная струбцина",
    "крепко сжимает две дощечки на верстаке, пока подсыхает клей, а рядом лежат опилки",
    f'<path d="M-2 98 H130 V130 H-2Z" fill="#C98A55" {W(3)}/>'
    + "".join(f'<path d="M{x} 96 q3 -4 6 0" fill="none" stroke="#F2D49B" stroke-width="2.4"/>' for x in (12, 22, 100, 110))
    + f'<rect x="20" y="70" width="88" height="12" rx="2" fill="#F2D49B" {W(2.6)}/><rect x="20" y="82" width="88" height="12" rx="2" fill="#E6C07A" {W(2.6)}/>'
    f'<path d="M36 30 H92 V42 H48 V106 H36Z" fill="#2E6BD6" {W(3)}/>'
    f'<rect x="80" y="42" width="12" height="28" fill="#2E6BD6" {W(2.6)}/>'
    f'<path d="M86 94 V118" {W(4)}/><rect x="76" y="94" width="20" height="6" rx="2" fill="#C0C7D1" {W(2.2)}/>'
    f'<path d="M74 118 H98" stroke="{O}" stroke-width="6" stroke-linecap="round"/><path d="M74 118 H98" stroke="#E8434A" stroke-width="3" stroke-linecap="round"/>'
    + face(64, 54, d=8, k=0.55) + sparkle(112, 24, 5))

I["quest-land-izmaylovskoe"] = ("#16324A", "#0A1A2A",
    "старинная латунная подзорная труба",
    "выглядывает из-за угла тёмного коридора квеста и высматривает светящийся крестик-подсказку",
    f'<rect x="-2" y="-2" width="44" height="132" fill="#24435E" {W(3)}/>'
    + "".join(f'<path d="M-2 {y} H42" stroke="#1A3348" stroke-width="2"/>' for y in range(14, 128, 16)) +
    f'<path d="M30 72 L96 48" stroke="#FFF3A0" stroke-width="18" opacity=".12" stroke-linecap="round"/>'
    f'<path d="M34 80 L58 72 L60 86 L36 92Z" fill="#B8862E" {W(2.6)}/><path d="M56 70 L80 62 L84 80 L60 88Z" fill="#E0B04A" {W(2.8)}/>'
    f'<path d="M78 58 L100 50 L106 72 L84 80Z" fill="#F2C75E" {W(3)}/><ellipse cx="103" cy="61" rx="4" ry="11" transform="rotate(-18 103 61)" fill="#9EE7FF" {W(2.4)}/>'
    + face(70, 76, d=5, k=0.42) +
    f'<path d="M100 98 l12 12 M112 98 l-12 12" stroke="#FFE066" stroke-width="4" stroke-linecap="round"/><circle cx="106" cy="104" r="12" fill="#FFE066" opacity=".2"/>'
    + sparkle(90, 22, 4, "#FFE066") + sparkle(116, 34, 3, "#FFE066"))

I["znatok-lab-leningradsky"] = ("#FFE8F0", "#F07CA8",
    "наэлектризованный голубой воздушный шарик",
    "только что потёрли о свитер, и он поднимает волосы мальчика дыбом на опыте в лаборатории",
    f'<path d="M14 130 Q16 100 40 98 Q64 96 66 130Z" fill="#7A5CFF" {W(3)}/>'
    f'<circle cx="40" cy="80" r="17" fill="#FFD9B8" {W(2.6)}/>'
    + "".join(f'<path d="M{40+14*math.cos(math.radians(a)):.1f} {80+14*math.sin(math.radians(a)):.1f} L{40+30*math.cos(math.radians(a)):.1f} {80+30*math.sin(math.radians(a)):.1f}" stroke="#E2A65C" stroke-width="3.5" stroke-linecap="round"/>' for a in range(-160, -10, 15))
    + face(40, 82, d=6, k=0.55) +
    f'<ellipse cx="88" cy="40" rx="22" ry="25" fill="#5BC0F8" {W(3.2)}/><path d="M88 65 l-4 6 h8Z" fill="#5BC0F8" {W(2)}/>'
    f'<path d="M88 71 Q80 90 92 108" fill="none" {W(2)}/><ellipse cx="80" cy="30" rx="6" ry="9" fill="#fff" opacity=".5"/>'
    + face(90, 42, d=7, k=0.55) +
    f'<path d="M62 52 l4 6 -6 2 4 6 M108 70 l4 6 -6 2 4 6" fill="none" stroke="#FFE066" stroke-width="3" stroke-linejoin="round"/>')

I["polycent-krasnoarmeyskaya"] = ("#E9FBFF", "#4FC3D9",
    "3D-ручка с тёплым носиком",
    "рисует прямо в воздухе объёмную пластиковую бабочку из оранжевой нити",
    f'<g transform="rotate(-40 82 82)"><rect x="70" y="46" width="22" height="66" rx="10" fill="#7A5CFF" {W(3.2)}/>'
    f'<rect x="74" y="58" width="14" height="8" rx="3" fill="#B9A6FF" {W(2)}/><circle cx="81" cy="76" r="3" fill="#5CD65C" {W(1.6)}/>'
    f'<path d="M72 112 L81 128 L90 112Z" fill="#C0C7D1" {W(2.6)}/></g>'
    + face(82, 80, d=5, k=0.45) +
    f'<path d="M48 104 Q30 104 34 84" fill="none" stroke="#FF8F3C" stroke-width="3"/>'
    f'<path d="M50 50 Q22 18 18 42 Q16 60 50 56Z M50 56 Q22 66 30 82 Q42 90 50 60Z" fill="none" stroke="#FF8F3C" stroke-width="3.6" stroke-linejoin="round"/>'
    f'<path d="M54 50 Q82 18 86 42 Q88 60 54 56Z M54 56 Q80 66 74 82 Q62 90 54 60Z" fill="none" stroke="#FF8F3C" stroke-width="3.6" stroke-linejoin="round"/>'
    f'<path d="M52 44 V72" stroke="#FF8F3C" stroke-width="4" stroke-linecap="round"/><path d="M52 44 q-4 -10 -8 -12 M52 44 q4 -10 8 -12" fill="none" stroke="#FF8F3C" stroke-width="2.4"/>'
    + sparkle(110, 24, 5) + sparkle(20, 104, 4))

I["vysotskaya-leningradsky"] = ("#FDF1E4", "#C98B5A",
    "сладкая колбаска из печенья и какао, перевязанная кулинарной ниткой",
    "лежит на разделочной доске, а отрезанный кружочек с орешками улыбается рядом",
    f'<rect x="8" y="78" width="112" height="34" rx="10" fill="#E2B57E" {W(3)}/><circle cx="112" cy="95" r="4" fill="#FDF1E4" {W(2)}/>'
    f'<rect x="14" y="42" width="78" height="34" rx="17" fill="#7A4A26" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 42 V76" stroke="#fff" stroke-width="2.4"/><path d="M{x-3} 42 l3 -4 l3 4" fill="none" stroke="#fff" stroke-width="2"/>' for x in (32, 52, 72))
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#F3D7A8"/>' for x, y in ((22, 52), (42, 66), (62, 50), (82, 64), (26, 68)))
    + face(48, 56, d=7, k=0.5) +
    f'<ellipse cx="96" cy="88" rx="16" ry="14" fill="#7A4A26" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#F3D7A8" {W(1.2)}/>' for x, y in ((88, 82), (102, 84), (92, 94), (104, 94)))
    + f'<path d="M92 90 Q96 94 100 90" fill="none" stroke="#fff" stroke-width="2"/>' + sparkle(110, 30, 5))

I["tis-ceramics-skakovaya"] = ("#EAF3FF", "#94B6E8",
    "глиняная подставка-ёжик, ощетинившаяся цветными карандашами",
    "стоит на полке керамической мастерской у окна высоко над городом",
    f'<rect x="78" y="10" width="44" height="54" rx="4" fill="#CFE6FF" {W(3)}/><path d="M100 10 V64 M78 37 H122" {W(2.4)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="6" height="{h}" fill="#9AB3D1"/>' for x, y, h in ((82, 50, 14), (90, 44, 20), (104, 54, 10), (112, 48, 16)))
    + f'<path d="M-2 98 H130 V106 H-2Z" fill="#B07A45" {W(2.6)}/>'
    + "".join(f'<g transform="rotate({a} 52 84)"><rect x="49" y="34" width="7" height="34" fill="{c}" {W(2)}/><path d="M49 34 l3.5 -8 l3.5 8Z" fill="#F3D7A8" {W(1.6)}/></g>' for a, c in ((-50, "#FF5C8A"), (-30, "#FFC93C"), (-10, "#5CD65C"), (10, "#3EA8E8"), (30, "#7A5CFF"), (50, "#FF8F3C")))
    + f'<path d="M22 98 Q20 70 52 66 Q84 66 88 86 L100 90 Q96 98 86 98Z" fill="#C8875A" {W(3.2)}/>'
    f'<circle cx="98" cy="90" r="2.6" fill="{O}"/>' + eye(76, 82, 0.6) +
    f'<ellipse cx="70" cy="90" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><path d="M84 94 q3 2 6 0" fill="none" {W(2)}/>')

I["laserland-vavilova"] = ("#0F2A22", "#06140F",
    "жилет лазертага с мигающими огоньками-датчиками",
    "стоит в тёмном неоновом лабиринте, а над ним перекрещиваются красный и зелёный лучи",
    f'<path d="M-2 34 L130 96" stroke="#FF3B5C" stroke-width="3"/><path d="M-2 100 L130 28" stroke="#3BFF8F" stroke-width="3"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="6" fill="#1F4F40"/>' for x, y, w in ((-2, 14, 40), (90, 112, 40), (100, 10, 30)))
    + f'<path d="M40 32 L52 28 Q64 40 76 28 L88 32 L94 108 Q64 118 34 108Z" fill="#2F3A46" {W(3.2)}/>'
    f'<path d="M52 28 L50 48 M76 28 L78 48" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}" {W(2.2)}/><circle cx="{x}" cy="{y}" r="11" fill="{c}" opacity=".25"/>' for x, y, c in ((46, 60, "#3BFF8F"), (82, 60, "#3BFF8F"), (64, 96, "#FF3B5C")))
    + face(64, 72, d=8, k=0.55))

I["kornilova-art-novorogozhskaya"] = ("#F5F0E6", "#C2B49A",
    "угольный карандаш-палочка в бумажной обёртке",
    "рисует на листе ватмана римскую арку с колоннами, оставляя чёрную пыльцу",
    f'<rect x="8" y="30" width="96" height="84" fill="#fff" {W(3)}/>'
    f'<path d="M22 104 V60 Q22 34 50 34 Q78 34 78 60 V104" fill="none" stroke="#3A3A3A" stroke-width="3"/>'
    f'<path d="M32 104 V62 Q32 44 50 44 Q68 44 68 62 V104" fill="none" stroke="#3A3A3A" stroke-width="2"/>'
    f'<path d="M16 104 H84 M18 58 H82" stroke="#3A3A3A" stroke-width="2"/>'
    + "".join(f'<path d="M{x} 62 V104" stroke="#8A8A8A" stroke-width="1.4"/>' for x in (25, 75))
    + f'<g transform="rotate(35 96 60)"><rect x="88" y="20" width="14" height="68" rx="3" fill="#2B2B2B" {W(3)}/>'
    f'<rect x="88" y="40" width="14" height="30" fill="#E8C48E" {W(2.4)}/></g>'
    + face(91, 58, d=4, k=0.4) +
    "".join(f'<circle cx="{x}" cy="{y}" r="1.2" fill="#3A3A3A"/>' for x, y in ((74, 96), (70, 100), (78, 102))))

I["sovenok-monakhovoy"] = ("#FFF3D9", "#F5A623",
    "погремушка с прозрачным шариком, полным цветных бусин",
    "задорно гремит в ручке малыша на мягком коврике игровой",
    f'<path d="M-2 102 H130 V130 H-2Z" fill="#9BD3F2" {W(3)}/>'
    f'<path d="M66 76 L44 116" stroke="{O}" stroke-width="12" stroke-linecap="round"/><path d="M66 76 L44 116" stroke="#FF5C8A" stroke-width="7" stroke-linecap="round"/>'
    f'<circle cx="44" cy="116" r="7" fill="#FFC93C" {W(2.4)}/>'
    f'<circle cx="74" cy="50" r="30" fill="#E8F8FF" fill-opacity=".85" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{c}" {W(1.6)}/>' for x, y, c in ((62, 62, "#FF5C8A"), (74, 68, "#5CD65C"), (86, 62, "#3EA8E8"), (68, 70, "#FFC93C"), (82, 70, "#7A5CFF")))
    + face(74, 42, d=8, k=0.6) +
    f'<path d="M30 30 q-6 6 0 12 M22 24 q-10 12 0 24 M110 30 q6 6 0 12 M118 24 q10 12 0 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')

I["play-today-skandinavsky"] = ("#E0FBF2", "#2EC4A0",
    "мягкая горка-волна из поролона с глазками",
    "по ней на животе съезжает малыш, раскинув руки, прямо на мягкий пол игровой",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#FFE08A" {W(3)}/>'
    f'<path d="M6 108 Q10 40 40 40 Q64 40 74 70 Q84 96 124 96 V108Z" fill="#7A5CFF" {W(3.2)}/>'
    f'<path d="M14 98 Q20 54 40 52 Q58 52 66 76" fill="none" stroke="#B9A6FF" stroke-width="4"/>'
    + face(30, 72, d=8, k=0.65) +
    f'<g transform="rotate(28 92 74)"><rect x="76" y="68" width="30" height="12" rx="6" fill="#FF8F3C" {W(2.6)}/>'
    f'<path d="M78 70 L66 62 M78 78 L66 86" {W(3)}/></g>'
    + kid(106, 76, 0.8, "#4A2E1A") + sparkle(100, 30, 5) + sparkle(64, 20, 3))

I["kulinarim-elektrozavodskaya"] = ("#FFEFF5", "#F59BB8",
    "кондитерский мешок с розовым кремом и звёздчатой насадкой",
    "выдавливает кремовую волну-улыбку на большой круглый пряник",
    f'<ellipse cx="60" cy="96" rx="44" ry="22" fill="#C98A55" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#fff"/>' for x, y in ((30, 96), (90, 96), (60, 110)))
    + f'<path d="M30 92 q6 -8 12 0 q6 -8 12 0 q6 -8 12 0" fill="none" stroke="#FF8FC0" stroke-width="6" stroke-linecap="round"/>'
    + eye(46, 84, 0.5) + eye(66, 84, 0.5) +
    f'<path d="M66 92 L74 76" stroke="#FF8FC0" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M72 72 L60 24 Q82 6 106 18 L80 72Z" fill="#fff" {W(3.2)}/><path d="M72 72 L80 72 L78 82 L74 82Z" fill="#C0C7D1" {W(2.4)}/>'
    f'<path d="M64 38 Q84 28 100 30" fill="none" stroke="#FF8FC0" stroke-width="10" opacity=".7"/>'
    + face(82, 44, d=6, k=0.5))

I["a101-family-prokshinsky"] = ("#DDE8FF", "#5D7FD8",
    "большой семейный зонтик в разноцветную полоску",
    "укрывает от дождика папу, маму и малыша, идущих за руки",
    "".join(f'<path d="M{x} {y} l-3 8" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>' for x, y in ((14, 20), (30, 8), (100, 10), (118, 26), (10, 50), (122, 56)))
    + "".join(f'<path d="M64 34 L{x1} 62 Q{(x1+x2)/2:.0f} 54 {x2} 62Z" fill="{c}" {W(2.6)}/>' for x1, x2, c in ((14, 39, "#FF5C8A"), (39, 64, "#FFC93C"), (64, 89, "#5CD65C"), (89, 114, "#3EA8E8")))
    + f'<path d="M64 26 V34" {W(3)}/><path d="M64 62 V104 Q64 110 70 108" fill="none" {W(3)}/>'
    + face(64, 48, d=8, k=0.45) +
    "".join(f'<path d="M{x} {y+8} V{y+30}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFD9B8" {W(2.2)}/>' for x, y, r, w, c in ((36, 74, 7, 9, "#2E6BD6"), (88, 76, 6.5, 8, "#D7263D"), (62, 88, 5, 7, "#FF8F3C")))
    + f'<path d="M40 92 Q50 96 58 98 M66 98 Q76 96 84 94" fill="none" {W(2.2)}/>')

I["masteryata-sevilsky"] = ("#FFF4DE", "#F0A43C",
    "поделка-львёнок из бумажной тарелки с гривой из цветных бумажных полосок",
    "подсыхает на столе детской мастерской рядом с клеем-карандашом",
    f'<path d="M-2 102 H130 V130 H-2Z" fill="#8FC9E8" {W(3)}/>'
    + "".join(f'<path d="M{60+30*math.cos(math.radians(a)):.1f} {56+30*math.sin(math.radians(a)):.1f} L{60+48*math.cos(math.radians(a)):.1f} {56+48*math.sin(math.radians(a)):.1f}" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
              f'<path d="M{60+30*math.cos(math.radians(a)):.1f} {56+30*math.sin(math.radians(a)):.1f} L{60+48*math.cos(math.radians(a)):.1f} {56+48*math.sin(math.radians(a)):.1f}" stroke="{("#B5651D", "#E07A1F", "#8B4513")[i % 3]}" stroke-width="5" stroke-linecap="round"/>' for i, a in enumerate(range(0, 360, 20)))
    + f'<circle cx="60" cy="56" r="32" fill="#fff" {W(3)}/><circle cx="60" cy="58" r="24" fill="#F7C45A" {W(2.6)}/>'
    f'<circle cx="42" cy="38" r="7" fill="#F7C45A" {W(2.4)}/><circle cx="78" cy="38" r="7" fill="#F7C45A" {W(2.4)}/>'
    + eye(51, 54, 0.6) + eye(69, 54, 0.6) +
    f'<ellipse cx="60" cy="66" rx="9" ry="6" fill="#FFF1D6" {W(2)}/><path d="M56 62 l4 4 l4 -4Z" fill="#6B3F23"/>'
    f'<path d="M50 66 h-12 M50 70 h-11 M70 66 h12 M70 70 h11" stroke="{O}" stroke-width="1.6"/>'
    f'<rect x="100" y="84" width="14" height="30" rx="4" fill="#5CD65C" {W(2.6)}/><rect x="100" y="76" width="14" height="10" rx="3" fill="#fff" {W(2.4)}/>')

if __name__ == "__main__":
    for pid, (a, b, hero, scene, body) in I.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
