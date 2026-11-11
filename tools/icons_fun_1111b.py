"""Иконки робота fun (2026-11-11, проход b): места из tools/add_fun_1111b.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1111b.py [id ...]"""
import os, sys, math
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}


def stars(pts, r=3, c="#fff"):
    return "".join(sparkle(x, y, r, c) for x, y in pts)


# 1. Мега Песочница (Мытищи)
I["fun-mega-pesochnitsa-mytishchi"] = ("#DFF6FF", "#5FB8E0",
    "песочный замок с тремя башенками и зубчиками, с мордашкой на стене",
    "стоит на песчаном холмике в игровой, на средней башне трепещет красный флажок, сбоку воткнута синяя лопатка",
    f'<path d="M0 108 Q64 90 128 108 V128 H0Z" fill="#F2CF84" {W(2.6)}/>'
    f'<path d="M26 104 V62 H38 V54 H44 V62 H50 V54 H56 V62 H72 V54 H78 V62 H84 V54 H90 V62 H102 V104Z" fill="#F7D894" {W(3)}/>'
    f'<path d="M48 62 V36 H54 V30 H60 V36 H68 V30 H74 V36 H80 V62Z" fill="#F7D894" {W(3)}/>'
    f'<path d="M64 30 V12" {W(2.6)}/><path d="M64 12 L80 17 L64 22Z" fill="#E8434A" {W(2)}/>'
    f'<path d="M56 104 V90 Q64 80 72 90 V104Z" fill="#C98E3E" {W(2.4)}/>'
    + face(64, 72, d=9, k=0.8) +
    "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#D9A55A"/>' for x, y in ((34, 80), (94, 86), (40, 96), (88, 70), (58, 48)))
    + f'<path d="M110 106 L114 66" stroke="#2F6FD0" stroke-width="4"/><path d="M108 66 Q114 52 122 64 L118 74 Q112 76 108 66Z" fill="#3F8FE8" {W(2.2)}/>'
    + stars(((16, 30), (104, 26)), 4, "#FFFFFF"))

# 2. Игровая «Дети» (Подольск, фудхолл): игровая с няней
I["fun-igrovaya-deti-podolsk"] = ("#FFE6D6", "#F49A6C",
    "улыбчивая девушка-няня с хвостиком и бейджем-сердечком на голубой кофте",
    "ведёт за ручку малыша в жёлтом комбинезоне к разноцветному игровому домику с горкой",
    f'<rect x="0" y="108" width="128" height="20" fill="#FFD3B5"/>'
    f'<path d="M84 108 V70 H120 V108Z" fill="#7CC8F2" {W(2.8)}/><path d="M80 72 L102 50 L124 72Z" fill="#E8434A" {W(2.8)}/>'
    f'<rect x="94" y="84" width="14" height="24" rx="6" fill="#FFD23F" {W(2.4)}/>'
    f'<path d="M84 80 Q72 92 70 108" fill="none" stroke="#4CB07A" stroke-width="6"/>'
    f'<path d="M30 112 L34 72 Q42 64 52 72 L56 112Z" fill="#6FB6E8" {W(3)}/>'
    f'<circle cx="43" cy="52" r="15" fill="#FFD9B8" {W(2.8)}/>'
    f'<path d="M28 50 Q30 34 44 34 Q58 34 58 50 Q50 42 28 50Z" fill="#8A4B2A" {W(2.4)}/>'
    f'<path d="M57 42 Q70 40 66 58 Q62 50 57 48Z" fill="#8A4B2A" {W(2.2)}/>'
    + face(43, 54, d=6, k=0.6) +
    f'<path d="M38 82 Q43 76 48 82 Q48 88 43 90 Q38 88 38 82Z" fill="#FF6FA3" {W(1.6)}/>'
    f'<path d="M54 82 Q62 88 66 92" {W(3)}/>'
    f'<rect x="62" y="94" width="16" height="16" rx="5" fill="#FFC72C" {W(2.6)}/>'
    f'<circle cx="70" cy="86" r="9" fill="#FFD9B8" {W(2.6)}/>'
    + eye(67, 86, 0.45) + eye(73, 86, 0.45) +
    f'<path d="M68 90 Q70 92 72 90" fill="none" {W(1.6)}/>' + stars(((16, 24), (110, 30)), 3, "#FFFFFF"))

# 3. «Дети при деле» (Подольск): игровое пространство-конструктор
I["fun-deti-pri-dele-podolsk"] = ("#FFF7C9", "#F2C230",
    "большая красная деталь детского конструктора с круглыми пупырышками сверху",
    "лежит на полу игровой, а на неё карабкается малыш в зелёной футболке, держа в руке синюю деталь поменьше",
    f'<rect x="0" y="104" width="128" height="24" fill="#FFE58A"/>'
    f'<rect x="14" y="66" width="100" height="40" rx="5" fill="#E8434A" {W(3.2)}/>'
    + "".join(f'<rect x="{x}" y="56" width="16" height="12" rx="3" fill="#F4645F" {W(2.6)}/>' for x in (20, 44, 68, 92) if x != 68)
    + face(64, 86, d=10, k=0.85) +
    f'<rect x="62" y="30" width="22" height="26" rx="6" fill="#4CB07A" {W(2.8)}/>'
    f'<circle cx="73" cy="20" r="11" fill="#FFD9B8" {W(2.6)}/>'
    f'<path d="M62 18 Q64 8 74 8 Q84 8 84 18 Q76 13 62 18Z" fill="#5A3A1E" {W(2)}/>'
    + eye(69, 21, 0.45) + eye(77, 21, 0.45) +
    f'<path d="M64 54 L62 66 M80 54 L84 66" {W(3.4)}/>'
    f'<path d="M62 36 L48 30" {W(3)}/><rect x="32" y="22" width="16" height="12" rx="3" fill="#3F8FE8" {W(2.4)}/>'
    f'<rect x="35" y="17" width="5" height="5" rx="1" fill="#3F8FE8" {W(1.6)}/><rect x="41" y="17" width="5" height="5" rx="1" fill="#3F8FE8" {W(1.6)}/>'
    f'<path d="M84 36 L96 42" {W(3)}/>' + stars(((110, 24), (18, 46)), 3, "#FFFFFF"))

# 4. «Киндерика» (Королёв): детские праздники
I["fun-kinderika-korolev"] = ("#FFE3F3", "#E36AB0",
    "серебристо-розовый фольгированный шар в форме цифры 5 с мордашкой",
    "парит над праздничным столом, держа в лапке ленточку, а со стола взлетают кругляшки конфетти",
    f'<rect x="0" y="104" width="128" height="24" fill="#FFFFFF" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 104 l6 10 l6 -10" fill="#FF9BCB"/>' for x in range(4, 128, 24))
    + f'<path d="M44 20 H86 V36 H60 L58 50 Q66 46 74 48 Q92 52 92 72 Q92 94 68 94 Q48 94 40 80 L54 74 Q58 82 68 82 Q78 82 78 72 Q78 62 66 62 Q56 62 52 68 L40 64Z" fill="#FFB3D9" {W(3.2)}/>'
    f'<path d="M50 26 H80" stroke="#FFFFFF" stroke-width="3" opacity=".7"/>'
    + face(70, 72, d=6, k=0.6) +
    f'<path d="M64 94 Q58 100 64 106" fill="none" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{c}"/>' for x, y, c in ((20, 40, "#FFD23F"), (104, 30, "#3F8FE8"), (110, 56, "#4CB07A"), (22, 70, "#7B6CD9"), (100, 84, "#FF8A3D")))
    + stars(((24, 20), (108, 96)), 4, "#FFFFFF"))

# 5. VR-клуб «Другие Миры» (Королёв)
I["fun-drugie-miry-korolev"] = ("#5B4BC4", "#1A1240",
    "фиолетово-бирюзовая спиральная воронка-портал с мордашкой в центре",
    "кружится в тёмном космосе и затягивает в себя звёздочки и маленькую планету с кольцом",
    "".join(f'<circle cx="64" cy="64" r="{r}" fill="none" stroke="{c}" stroke-width="7" stroke-dasharray="{d}" transform="rotate({a} 64 64)"/>'
            for r, c, d, a in ((48, "#7B6CD9", "70 20", 0), (38, "#4FD1C5", "50 16", 40), (28, "#B48CF0", "34 12", 80), (18, "#8AF0E0", "22 8", 120)))
    + f'<circle cx="64" cy="64" r="14" fill="#E6DAFF" {W(2.6)}/>' + face(64, 63, d=5, k=0.5) +
    f'<circle cx="104" cy="24" r="9" fill="#FFB347" {W(2.2)}/><ellipse cx="104" cy="24" rx="16" ry="4" fill="none" {W(2.2)} transform="rotate(-20 104 24)"/>'
    + stars(((18, 22), (22, 104), (110, 100), (30, 60)), 3, "#FFF6A8"))

# 6. Portal VR (Люберцы)
I["fun-portal-vr-lyubertsy"] = ("#D6E4FF", "#3D63D6",
    "белая VR-перчатка с голубыми огоньками-сенсорами на кончиках пальцев",
    "растопырив пальцы, ловит в воздухе светящийся виртуальный кубик из сетки линий",
    f'<path d="M34 120 L36 78 Q30 56 34 40 Q38 34 42 40 L44 62 L46 28 Q50 22 54 28 L56 58 L60 22 Q64 16 68 22 L68 58 L74 30 Q78 24 82 30 L80 66 Q90 58 96 64 Q98 70 92 76 Q80 92 74 120Z" fill="#FFFFFF" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#5FD3FF" {W(1.6)}/>' for x, y in ((38, 40), (50, 28), (64, 22), (78, 30), (94, 66)))
    + f'<rect x="38" y="92" width="38" height="12" rx="4" fill="#3D63D6" {W(2.4)}/>'
    + face(56, 76, d=7, k=0.6) +
    f'<g transform="translate(92 6)"><path d="M4 10 L18 4 L32 10 L18 16Z M4 10 V26 L18 32 V16 M32 10 V26 L18 32" fill="#9FE6FF" fill-opacity=".5" stroke="#5FD3FF" stroke-width="2"/></g>'
    + stars(((16, 20), (110, 52)), 3, "#FFFFFF"))

# 7. Арт-студия Tk School (Видное): живопись и смола
I["fun-tk-school-vidnoe"] = ("#FFF4D6", "#E9B44C",
    "круглый срез дерева, залитый синей эпоксидной смолой «море» с белой пеной у края",
    "лежит на рабочем столе студии и улыбается, а сверху из стаканчика капает ещё одна бирюзовая капля",
    f'<rect x="0" y="100" width="128" height="28" fill="#C48A55"/>'
    f'<ellipse cx="60" cy="82" rx="46" ry="24" fill="#B9844B" {W(3)}/>'
    f'<ellipse cx="60" cy="76" rx="46" ry="24" fill="#E3B57A" {W(3)}/>'
    f'<path d="M30 70 Q44 60 62 66 Q80 72 96 64 Q104 78 90 90 Q60 100 30 90 Q20 80 30 70Z" fill="#2E86DE" {W(2.4)}/>'
    f'<path d="M30 70 Q44 60 62 66 Q80 72 96 64" fill="none" stroke="#FFFFFF" stroke-width="4"/>'
    + face(62, 80, d=8, k=0.65) +
    f'<path d="M92 16 L112 16 L108 40 H96Z" fill="#FFFFFF" {W(2.6)}/><path d="M95 30 H109 L108 40 H96Z" fill="#26C6DA"/>'
    f'<path d="M94 40 Q88 46 86 54" stroke="#26C6DA" stroke-width="3"/><path d="M86 52 Q82 58 86 61 Q90 58 86 52Z" fill="#26C6DA" {W(1.4)}/>'
    + stars(((18, 22), (40, 34)), 3, "#FFFFFF"))

# 8. Студия Левандовских (Одинцово): керамика
I["fun-levandovskikh-odintsovo"] = ("#F3E6FF", "#9C6FD6",
    "керамический колокольчик с ручкой-петелькой и синими точками росписи",
    "сам себя раскачивает и звенит, а из-под юбочки вылетают три нотки",
    f'<path d="M64 10 Q74 10 74 20 Q74 28 64 28 Q54 28 54 20 Q54 10 64 10Z" fill="none" stroke="#C4683A" stroke-width="6"/>'
    f'<path d="M64 26 Q40 28 38 64 Q36 86 24 96 H104 Q92 86 90 64 Q88 28 64 26Z" fill="#F5DEC4" {W(3.2)}/>'
    f'<path d="M24 96 H104 Q106 104 98 104 H30 Q22 104 24 96Z" fill="#E6C29E" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#2F6FD0"/>' for x, y in ((48, 50), (80, 50), (44, 76), (84, 76), (64, 40), (56, 90), (72, 90)))
    + face(64, 62, d=8, k=0.7) +
    f'<circle cx="64" cy="110" r="7" fill="#C4683A" {W(2.4)}/>'
    + "".join(f'<path d="M{x} {y} v-12 l7 -2 v12" fill="none" {W(2)}/><ellipse cx="{x-2}" cy="{y}" rx="3" ry="2.4" fill="{O}"/><ellipse cx="{x+5}" cy="{y-2}" rx="3" ry="2.4" fill="{O}"/>'
              for x, y in ((14, 60), (106, 46)))
    + stars(((22, 30), (110, 90)), 3, "#FFFFFF"))

# 9. «Мастерим» (Подольск): картина + фетровая игрушка
I["fun-masterim-podolsk"] = ("#E7F7F2", "#55B79A",
    "мягкая фетровая сова с пунктирными стежками по краю и пуговицами-глазами",
    "сидит на верхнем краю холста, на котором акрилом нарисована жёлтая луна над холмами",
    f'<rect x="20" y="52" width="88" height="66" fill="#2C3E7A" {W(3)}/>'
    f'<circle cx="84" cy="74" r="10" fill="#FFE066"/><path d="M20 106 Q48 88 70 100 Q90 90 108 102 V118 H20Z" fill="#4CB07A"/>'
    f'<rect x="20" y="52" width="88" height="66" fill="none" {W(3)}/>'
    f'<path d="M40 54 Q30 40 36 22 L44 30 Q56 22 68 30 L76 22 Q82 40 72 54Z" fill="#E98A3C" {W(3)}/>'
    f'<path d="M40 52 Q32 40 37 25 M72 52 Q80 40 75 25" fill="none" stroke="#FFFFFF" stroke-width="1.6" stroke-dasharray="3 3"/>'
    f'<circle cx="49" cy="38" r="7" fill="#FFFFFF" {W(2.2)}/><circle cx="63" cy="38" r="7" fill="#FFFFFF" {W(2.2)}/>'
    f'<circle cx="49" cy="38" r="3" fill="{O}"/><circle cx="63" cy="38" r="3" fill="{O}"/>'
    f'<circle cx="48" cy="37" r="1" fill="#fff"/><circle cx="62" cy="37" r="1" fill="#fff"/>'
    f'<path d="M53 44 L56 49 L59 44Z" fill="#FFC72C" {W(1.6)}/>'
    f'<path d="M44 54 l3 4 M52 54 l2 4 M62 54 l-2 4 M70 54 l-3 4" {W(2)}/>'
    + stars(((100, 22), (16, 30), (40, 70)), 3, "#FFFFFF"))

# 10. «Юный мастер» (Подольск): столярный кружок
I["fun-yunyy-master-podolsk"] = ("#E6F2FF", "#7FA7D9",
    "самодельный деревянный грузовичок с кузовом и колёсами-спилами",
    "весело катится по верстаку, а в кузове везёт горку завитых стружек",
    f'<rect x="0" y="100" width="128" height="28" fill="#C98E52" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 106 H{x+14}" stroke="#A86E38" stroke-width="2"/>' for x in (8, 50, 96))
    + f'<rect x="14" y="56" width="58" height="34" rx="3" fill="#E7B87A" {W(3)}/>'
    + "".join(f'<path d="M14 {y} H72" stroke="#C9935A" stroke-width="1.8"/>' for y in (66, 76))
    + f'<path d="M72 90 V48 H96 L110 66 V90Z" fill="#F2C98C" {W(3)}/>'
    f'<path d="M78 54 H94 L104 66 H78Z" fill="#BFE6FF" {W(2.4)}/>'
    + face(92, 78, d=6, k=0.55) +
    "".join(f'<circle cx="{x}" cy="94" r="11" fill="#D9A766" {W(2.8)}/><circle cx="{x}" cy="94" r="6" fill="none" stroke="#A86E38" stroke-width="1.6"/><circle cx="{x}" cy="94" r="2" fill="#A86E38"/>' for x in (32, 92))
    + "".join(f'<path d="M{x} 56 q-6 -10 2 -14 q8 -2 4 8" fill="#FFE2B0" {W(1.8)}/>' for x in (24, 38, 52, 62))
    + stars(((110, 24), (24, 24)), 3, "#FFFFFF"))

# 11. «Туки-Туки» (Реутов): столярная мастерская
I["fun-tuki-tuki-reutov"] = ("#FFF1E0", "#D97B3C",
    "деревянная игрушка-дятел в красной шапочке на высоком шесте с пружинкой",
    "съезжает по шесту вниз и стучит клювом «тук-тук», а от шеста разлетаются щепочки-звёздочки",
    f'<rect x="26" y="110" width="76" height="12" rx="3" fill="#B07A45" {W(2.8)}/>'
    f'<rect x="60" y="8" width="8" height="104" rx="3" fill="#E3B57A" {W(2.8)}/>'
    f'<path d="M64 30 q-10 4 0 8 q10 4 0 8 q-10 4 0 8 q10 4 0 8" fill="none" stroke="#9AA3B5" stroke-width="3"/>'
    f'<ellipse cx="46" cy="66" rx="18" ry="22" fill="#F2C98C" {W(3)}/>'
    f'<path d="M30 56 Q34 38 50 42 Q58 46 56 56 Q44 50 30 56Z" fill="#E8434A" {W(2.6)}/>'
    f'<path d="M58 60 L62 62 L58 66Z" fill="#FFC72C" {W(2)}/>'
    f'<path d="M58 58 L64 63 L58 67" fill="#FFC72C" {W(2)}/>'
    + eye(48, 62, 0.6) +
    f'<ellipse cx="40" cy="70" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>'
    f'<path d="M30 74 Q22 86 32 92 L40 80" fill="#D9A766" {W(2.4)}/>'
    f'<path d="M44 88 L42 98 M50 88 L52 98" {W(2.6)}/>'
    + "".join(f'<path d="M{x} {y} l6 -3" stroke="#B07A45" stroke-width="3"/>' for x, y in ((74, 58), (78, 66), (76, 74)))
    + stars(((94, 30), (104, 70), (20, 30)), 4, "#FFFFFF"))

# 12. Арт-студия «Смарт» (Мичуринский): кружок для малышей
I["fun-art-smart-michurinsky"] = ("#E0FBFF", "#41B6C4",
    "детские ножницы с зелёными круглыми ручками и закруглёнными кончиками",
    "вырезают из голубого листа бумаги снежинку, и обрезки-завитки сыплются вниз",
    f'<path d="M14 18 H76 L82 70 H20Z" fill="#9FD8FF" {W(3)}/>'
    f'<path d="M48 30 v28 M36 38 l24 12 M60 38 l-24 12" stroke="#FFFFFF" stroke-width="4"/>'
    f'<circle cx="48" cy="44" r="4" fill="#FFFFFF"/>'
    f'<path d="M66 60 L96 88" stroke="#C9CED8" stroke-width="7"/><path d="M76 56 L96 88" stroke="#E4E8EF" stroke-width="7"/>'
    f'<path d="M66 60 L96 88 M76 56 L96 88" fill="none" {W(2)}/>'
    f'<circle cx="96" cy="88" r="4" fill="#9AA3B5" {W(2)}/>'
    f'<circle cx="92" cy="106" r="13" fill="#4CB07A" {W(3)}/><circle cx="92" cy="106" r="6" fill="#E0FBFF" {W(2)}/>'
    f'<circle cx="112" cy="94" r="11" fill="#4CB07A" {W(3)}/><circle cx="112" cy="94" r="5" fill="#E0FBFF" {W(2)}/>'
    + eye(86, 99, 0.45) + eye(98, 99, 0.45) +
    "".join(f'<path d="M{x} {y} q4 4 0 8 q-4 4 0 8" fill="none" stroke="#6CC0F2" stroke-width="3"/>' for x, y in ((24, 84), (40, 96), (56, 86)))
    + stars(((108, 24), (98, 50)), 3, "#FFFFFF"))

# 13. «Глинка» (проспект 60-летия Октября): гончарная мастерская
I["fun-glinka-60-oktyabrya"] = ("#FDEBDD", "#C7724A",
    "мокрый ком рыжей глины, вытягивающийся в высокий цилиндр, с мордашкой",
    "кружится на гончарном станке и растёт вверх, разбрызгивая по сторонам капельки воды",
    f'<ellipse cx="64" cy="104" rx="48" ry="12" fill="#8C96A8" {W(3)}/>'
    f'<ellipse cx="64" cy="98" rx="48" ry="12" fill="#B9C2D0" {W(3)}/>'
    f'<path d="M40 96 Q36 70 46 50 Q50 34 48 22 H80 Q78 34 82 50 Q92 70 88 96Z" fill="#D9824E" {W(3.2)}/>'
    f'<ellipse cx="64" cy="22" rx="16" ry="5" fill="#B5643A" {W(2.4)}/>'
    + "".join(f'<path d="M{a} {y} Q64 {y+6} {b} {y}" fill="none" stroke="#B5643A" stroke-width="2"/>' for a, b, y in ((44, 84, 80), (46, 82, 88)))
    + face(64, 60, d=8, k=0.7) +
    f'<path d="M14 80 q8 -6 16 0 M98 80 q8 -6 16 0" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>'
    + "".join(f'<path d="M{x} {y} q-3 5 0 7 q3 -2 0 -7Z" fill="#7CC8F2" {W(1.2)}/>' for x, y in ((20, 50), (108, 46), (14, 64), (114, 62)))
    + stars(((24, 22), (104, 20)), 3, "#FFFFFF"))

# 14. Stem Lab (Видное): IT и инженерия
I["fun-stem-lab-vidnoe"] = ("#E4FFE9", "#1F9E6E",
    "зелёная печатная плата-жучок с ножками-контактами и светодиодными усиками",
    "ползёт по белому листу, оставляя за собой дорожку из жёлтых линий схемы",
    f'<path d="M0 96 H128 V128 H0Z" fill="#FFFFFF" opacity=".7"/>'
    f'<path d="M6 110 H30 V98 H44" fill="none" stroke="#FFC72C" stroke-width="3"/><circle cx="6" cy="110" r="3" fill="#FFC72C"/>'
    + "".join(f'<path d="M{x} {y} l{dx} 10" {W(3)}/>' for x, y, dx in ((40, 64, -10), (40, 80, -12), (88, 64, 10), (88, 80, 12), (52, 92, -6), (76, 92, 6)))
    + f'<rect x="38" y="44" width="52" height="52" rx="10" fill="#2EAD6B" {W(3.2)}/>'
    f'<rect x="52" y="70" width="24" height="16" rx="2" fill="#2B2B3A" {W(2)}/>'
    + "".join(f'<path d="M{x} 70 v-3 M{x} 86 v3" {W(1.6)}/>' for x in (56, 62, 68, 74))
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#FFC72C"/>' for x, y in ((44, 50), (84, 50), (44, 90), (84, 90)))
    + face(64, 56, d=8, k=0.6, blush=False) +
    f'<path d="M54 44 Q48 30 40 26 M74 44 Q80 30 88 26" fill="none" {W(2.4)}/>'
    f'<circle cx="40" cy="24" r="5" fill="#FF5A5A" {W(2)}/><circle cx="88" cy="24" r="5" fill="#5FD3FF" {W(2)}/>'
    + stars(((108, 40), (18, 40)), 3, "#FFFFFF"))

# 15. Инжинириум МГТУ (Королёв): инженерные курсы
I["fun-inzhinirium-korolev"] = ("#EEF0F5", "#8A94A8",
    "маленький электромоторчик-цилиндр с медными клеммами и красным пропеллером",
    "стоит на батарейке, подключённый двумя проводками, и так быстро крутит пропеллер, что подпрыгивает",
    f'<rect x="30" y="94" width="68" height="22" rx="6" fill="#FFC72C" {W(3)}/>'
    f'<rect x="30" y="94" width="20" height="22" rx="6" fill="#2B2B3A" {W(3)}/><rect x="98" y="100" width="6" height="10" rx="2" fill="#C9CED8" {W(2)}/>'
    f'<path d="M84 94 Q90 80 86 72 M40 94 Q34 80 40 72" fill="none" stroke="#E8434A" stroke-width="3"/>'
    f'<rect x="36" y="44" width="54" height="32" rx="14" fill="#C9CED8" {W(3.2)}/>'
    f'<rect x="36" y="44" width="16" height="32" rx="8" fill="#E39A4C" {W(2.6)}/>'
    + face(68, 58, d=7, k=0.6) +
    f'<path d="M90 60 H100" {W(3)}/>'
    f'<path d="M100 60 Q96 36 104 26 Q110 40 100 60 Q104 84 96 94 Q92 80 100 60Z" fill="#E8434A" {W(2.4)}/>'
    f'<circle cx="100" cy="60" r="3.4" fill="{O}"/>'
    f'<path d="M110 30 q8 6 6 16 M112 74 q8 -4 8 -12" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>'
    + stars(((18, 24), (40, 26)), 3, "#FFFFFF"))

# 16. Робоцентр «Полигон» (Алтуфьево): робототехника
I["fun-robocentr-poligon-altufyevo"] = ("#FFE9E9", "#E05A5A",
    "робот-паук с округлым оранжевым корпусом-панцирем и шестью лапками на шарнирах",
    "шагает по полигону с чёрно-белой линией, обходя синий конус, и мигает антенной",
    f'<path d="M0 100 H128 V128 H0Z" fill="#FFFFFF" opacity=".8"/>'
    f'<path d="M0 112 Q40 104 70 112 T128 108" fill="none" stroke="#2B2B3A" stroke-width="5"/>'
    f'<path d="M100 104 L108 80 L116 104Z" fill="#3F8FE8" {W(2.4)}/><path d="M104 94 H112" stroke="#FFFFFF" stroke-width="3"/>'
    + "".join(f'<path d="M{x0} {y0} L{x1} {y1} L{x2} {y2}" fill="none" {W(3.4)}/><circle cx="{x1}" cy="{y1}" r="3" fill="#9AA3B5" {W(1.6)}/>'
              for x0, y0, x1, y1, x2, y2 in ((40, 68, 18, 60, 12, 92), (42, 76, 22, 80, 20, 104), (48, 82, 36, 94, 34, 108),
                                             (88, 68, 104, 56, 112, 84), (86, 76, 100, 78, 98, 102), (80, 82, 88, 94, 86, 108)))
    + f'<ellipse cx="64" cy="66" rx="28" ry="22" fill="#FF8A3D" {W(3.2)}/>'
    f'<path d="M44 58 Q64 40 84 58" fill="none" stroke="#FFFFFF" stroke-width="3" opacity=".6"/>'
    f'<rect x="48" y="62" width="32" height="14" rx="7" fill="#2B2B3A" {W(2)}/>'
    f'<circle cx="57" cy="69" r="3.6" fill="#5FD3FF"/><circle cx="71" cy="69" r="3.6" fill="#5FD3FF"/>'
    f'<path d="M64 44 V28" {W(2.6)}/><circle cx="64" cy="24" r="5" fill="#FFD23F" {W(2)}/>'
    + stars(((20, 24), (100, 26), (64, 12)), 3, "#FFFFFF"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
