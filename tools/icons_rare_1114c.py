"""Иконки робота rare 2026-11-14 (1114c) — каждая придумана и нарисована отдельно (абсолютная уникальность).
Реестр строк — в SUBJ ниже (дописываются в icons-src/subjects.txt). Запуск: python3 tools/icons_rare_1114c.py [id…]
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons as d

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
SUBJ = {}
O = d.O


def save(pid, bg, body, hero, scene):
    open(os.path.join(OUT, pid + ".svg"), "w").write(d.svg(bg, body))
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def blade(x1, x2, y, col="#AEB9CF", w=4.5):
    return f'<path d="M{x1} {y} H{x2} Q{x2 + 6} {y} {x2 + 6} {y - 6}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'


# 1. Дейнега, КСК «Битца» (конный комплекс): конёк-горбунок — фигурный ботинок с лошадиной гривой
def deinega_bitsa():
    b = '<path d="M0 108 Q64 100 128 108 V128 H0Z" fill="#F3E2C6" ' + d.s('stroke-width="2.4"') + '/>'
    # ботинок
    b += ('<path d="M34 92 V40 Q34 30 44 30 H66 Q74 30 74 40 V66 Q96 68 100 80 Q102 92 92 92Z" fill="#FFFFFF" '
          + d.s() + '/>')
    b += '<path d="M48 40 L60 46 M48 50 L60 56 M48 60 L60 66" stroke="#C8553D" stroke-width="2.6" stroke-linecap="round"/>'
    # грива и хвост
    b += '<path d="M34 34 Q22 40 26 52 Q16 58 24 68 Q16 76 26 84" fill="none" stroke="#D9822B" stroke-width="7" stroke-linecap="round"/>'
    b += '<path d="M68 30 Q74 18 86 22 Q78 26 80 32" fill="#D9822B" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M44 30 L48 20 L54 30" fill="#FFFFFF" ' + d.s('stroke-width="2.4"') + '/>'
    b += d.face(62, 78, d=8, k=0.8)
    # лезвие с зубцами
    b += '<path d="M38 92 V98 M88 92 V98" stroke="#3B3355" stroke-width="3"/>'
    b += '<path d="M28 100 H96 Q104 100 104 92" fill="none" stroke="#AEB9CF" stroke-width="5" stroke-linecap="round"/>'
    b += '<path d="M22 96 l4 -4 M22 104 l4 4" stroke="#AEB9CF" stroke-width="3" stroke-linecap="round"/>'
    for x in (108, 116):
        b += f'<path d="M{x} 112 q3 -4 6 0" fill="none" stroke="#B88A55" stroke-width="2.4" stroke-linecap="round"/>'
    save("deinega-skating-bitsa", "orange", b,
         "белый фигурный ботинок-конёк с рыжей лошадиной гривой, ушками и хвостиком — «конёк-горбунок»",
         "скачет галопом по льду конноспортивного манежа, оставляя на песке следы подковок")


# 2. «Монстр хоккея»: оранжевый лохматый трёхрогий монстрик в синем шлеме бьёт по шайбе
def monster_hockey():
    b = '<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#EAF8FF" ' + d.s('stroke-width="2.4"') + '/>'
    b += ('<path d="M30 96 Q22 70 34 52 Q30 44 38 42 Q44 30 60 32 Q76 28 86 40 Q96 42 94 52 Q104 70 96 96Z" '
          'fill="#FF9A3C" ' + d.s() + '/>')
    for x, y in [(30, 70), (28, 82), (98, 72), (100, 86), (40, 96), (88, 96)]:
        b += f'<path d="M{x} {y} l-4 3" stroke="#3B3355" stroke-width="2.4" stroke-linecap="round"/>'
    b += '<path d="M40 50 Q42 30 64 28 Q86 30 88 50 Z" fill="#2F6FD6" ' + d.s() + '/>'
    b += '<path d="M42 50 H86" stroke="#FFFFFF" stroke-width="3"/>'
    for x in (50, 64, 78):
        b += f'<path d="M{x - 4} 30 L{x} 16 L{x + 4} 30" fill="#FFE07A" ' + d.s('stroke-width="2.4"') + '/>'
    b += d.eye(54, 64, 1.0) + d.eye(74, 64, 1.0)
    b += '<path d="M54 78 Q64 86 74 78" fill="#7A2E2E" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<rect x="61" y="78" width="5" height="4" fill="#FFFFFF"/>'
    # клюшка и шайба
    b += '<path d="M96 60 L80 104 Q78 110 70 110 H58" fill="none" stroke="#3B3355" stroke-width="8" stroke-linecap="round"/>'
    b += '<path d="M96 60 L80 104 Q78 110 70 110 H58" fill="none" stroke="#C99A5B" stroke-width="4.5" stroke-linecap="round"/>'
    b += '<ellipse cx="34" cy="110" rx="10" ry="4.5" fill="#222" ' + d.s('stroke-width="2"') + '/>'
    b += '<path d="M14 106 H22 M12 112 H22" stroke="#9DD6F5" stroke-width="2.6" stroke-linecap="round"/>'
    save("monster-hockey-bitsa", "teal", b,
         "оранжевый лохматый монстрик с тремя жёлтыми рожками, торчащими сквозь синий хоккейный шлем",
         "щербато улыбается и со всей силы лупит клюшкой по чёрной шайбе на льду")


# 3. Arena Play Юг (Коммунарка): южная пальма в шарфе впервые на коньках
def arenaplay_yug():
    b = '<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#E6F6FF" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M60 96 Q56 70 62 44" fill="none" stroke="#3B3355" stroke-width="13" stroke-linecap="round"/>'
    b += '<path d="M60 96 Q56 70 62 44" fill="none" stroke="#B9824C" stroke-width="8" stroke-linecap="round"/>'
    for y in (56, 68, 80):
        b += f'<path d="M55 {y} H65" stroke="#8A5E3A" stroke-width="2"/>'
    for p in ["M62 42 Q40 22 18 36 Q40 32 62 42Z", "M62 42 Q86 20 110 34 Q86 30 62 42Z",
              "M62 42 Q50 16 60 6 Q62 24 62 42Z", "M62 42 Q30 42 22 60 Q40 46 62 42Z", "M62 42 Q96 40 104 58 Q86 46 62 42Z"]:
        b += f'<path d="{p}" fill="#3DBB6A" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<circle cx="56" cy="46" r="5" fill="#8A5E3A" ' + d.s('stroke-width="2"') + '/><circle cx="67" cy="47" r="5" fill="#8A5E3A" ' + d.s('stroke-width="2"') + '/>'
    b += d.face(60, 64, d=6, k=0.6)
    b += '<path d="M50 74 Q60 80 70 74 L72 80 Q60 86 48 80Z" fill="#E8463C" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<path d="M68 80 L74 94 L80 92 L72 78" fill="#E8463C" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<path d="M52 78 H56 M60 80 H64" stroke="#FFFFFF" stroke-width="2"/>'
    b += '<path d="M44 96 H56 Q58 90 54 90 H46Z M64 96 H76 Q78 90 74 90 H66Z" fill="#FFFFFF" ' + d.s('stroke-width="2.2"') + '/>'
    b += blade(40, 56, 101, w=3.6) + blade(60, 76, 101, w=3.6)
    b += '<path d="M24 86 q-6 -4 -10 2 M104 86 q6 -4 10 2" fill="none" stroke="#7FB8E6" stroke-width="2.4" stroke-linecap="round"/>'
    save("arenaplay-yug-kommunarka", "sky", b,
         "зелёная южная пальма с двумя кокосами и красным вязаным шарфом",
         "впервые встала на коньки на крытом льду и машет листьями-руками для равновесия")


# 4. «Лёд» (Ногинск), с 3,5 лет: малышка в розовом комбинезоне на льду
def led_noginsk():
    b = '<path d="M0 102 Q64 94 128 102 V128 H0Z" fill="#F2FBFF" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M44 92 Q40 66 50 56 H78 Q88 66 84 92Z" fill="#FF8FC0" ' + d.s() + '/>'
    b += '<path d="M64 58 V90" stroke="#3B3355" stroke-width="2.2"/>'
    b += '<path d="M48 62 Q30 64 24 54" fill="none" stroke="#3B3355" stroke-width="10" stroke-linecap="round"/>'
    b += '<path d="M48 62 Q30 64 24 54" fill="none" stroke="#FF8FC0" stroke-width="6" stroke-linecap="round"/>'
    b += '<path d="M80 62 Q98 64 104 54" fill="none" stroke="#3B3355" stroke-width="10" stroke-linecap="round"/>'
    b += '<path d="M80 62 Q98 64 104 54" fill="none" stroke="#FF8FC0" stroke-width="6" stroke-linecap="round"/>'
    b += '<circle cx="24" cy="52" r="5" fill="#7CD26E" ' + d.s('stroke-width="2"') + '/><circle cx="104" cy="52" r="5" fill="#7CD26E" ' + d.s('stroke-width="2"') + '/>'
    b += '<circle cx="64" cy="40" r="17" fill="#FFE0C8" ' + d.s() + '/>'
    b += '<path d="M46 38 Q48 18 64 18 Q80 18 82 38 Q72 30 64 30 Q56 30 46 38Z" fill="#FFFFFF" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<circle cx="64" cy="14" r="6" fill="#FF8FC0" ' + d.s('stroke-width="2.4"') + '/>'
    b += d.face(64, 42, d=6, k=0.6)
    b += '<path d="M48 92 H60 V98 H48Z M68 92 H80 V98 H68Z" fill="#FFFFFF" ' + d.s('stroke-width="2.2"') + '/>'
    b += blade(44, 60, 102, w=3.4) + blade(66, 82, 102, w=3.4)
    for x, y, r in [(18, 24, 4), (110, 24, 4), (104, 82, 3), (22, 84, 3)]:
        b += d.sparkle(x, y, r, "#FFFFFF")
    save("led-noginsk", "blue", b,
         "малышка лет трёх в пушистом розовом комбинезоне, белой шапке с помпоном и зелёных варежках",
         "делает первые шаги на льду на маленьких белых коньках, широко раскинув руки, а вокруг искрятся снежинки")


# 5. Pro Hockey, «Резиденции Берёзки»: берёзовое полено-вратарь
def pro_hockey_soloslovo():
    b = '<path d="M0 104 Q64 98 128 104 V128 H0Z" fill="#EDF9FF" ' + d.s('stroke-width="2.4"') + '/>'
    # ворота
    b += '<path d="M14 104 V58 H54 V104" fill="none" stroke="#E8463C" stroke-width="5" stroke-linejoin="round"/>'
    for x in (24, 34, 44):
        b += f'<path d="M{x} 60 V104" stroke="#FFFFFF" stroke-width="1.6" opacity=".9"/>'
    for y in (70, 82, 94):
        b += f'<path d="M16 {y} H52" stroke="#FFFFFF" stroke-width="1.6" opacity=".9"/>'
    # полено
    b += '<rect x="54" y="40" width="40" height="62" rx="12" fill="#FFFFFF" ' + d.s() + '/>'
    for x, y, w in [(60, 56, 10), (78, 64, 12), (62, 86, 8), (80, 92, 10)]:
        b += f'<path d="M{x} {y} H{x + w}" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    b += '<ellipse cx="74" cy="40" rx="20" ry="6" fill="#F2D6A2" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<ellipse cx="74" cy="40" rx="9" ry="2.6" fill="none" stroke="#C9A06A" stroke-width="1.8"/>'
    b += '<path d="M54 40 Q54 18 74 18 Q94 18 94 40" fill="#FFC531" ' + d.s() + '/>'
    b += '<path d="M58 34 H90" stroke="#3B3355" stroke-width="2"/>'
    b += d.face(74, 72, d=7, k=0.7)
    b += '<path d="M94 50 Q104 46 108 36" fill="none" stroke="#3E8E55" stroke-width="3" stroke-linecap="round"/>'
    b += '<path d="M106 38 Q114 30 116 38 Q110 42 106 38Z" fill="#7CD26E" ' + d.s('stroke-width="1.8"') + '/>'
    # клюшка вратаря
    b += '<path d="M56 80 L40 108 H58" fill="none" stroke="#3B3355" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    b += '<path d="M56 80 L40 108 H58" fill="none" stroke="#6B4A2E" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
    b += '<ellipse cx="104" cy="104" rx="8" ry="3.5" fill="#222" ' + d.s('stroke-width="1.8"') + '/>'
    save("pro-hockey-soloslovo", "green", b,
         "берёзовое полено в жёлтом хоккейном шлеме, с чёрными чёрточками на белой коре и зелёной веточкой",
         "стоит вратарём у красных ворот с сеткой и ловко отбивает клюшкой летящую шайбу")


# 6. «Сокол — Территория спорта»: ракетка в соломенной панаме на белом песке
def sokol_tt():
    b = '<path d="M0 98 Q40 90 64 96 Q90 102 128 94 V128 H0Z" fill="#FFF7E8" ' + d.s('stroke-width="2.4"') + '/>'
    for x, y in [(20, 108), (40, 116), (96, 112), (110, 104), (70, 118)]:
        b += f'<circle cx="{x}" cy="{y}" r="1.6" fill="#E3C89A"/>'
    b += '<path d="M60 92 L56 110" stroke="#3B3355" stroke-width="10" stroke-linecap="round"/>'
    b += '<path d="M60 92 L56 110" stroke="#C99A5B" stroke-width="6" stroke-linecap="round"/>'
    b += '<circle cx="64" cy="62" r="30" fill="#E23B3B" ' + d.s() + '/>'
    b += '<circle cx="64" cy="62" r="23" fill="none" stroke="#B42828" stroke-width="2"/>'
    b += '<path d="M34 44 Q36 32 64 30 Q92 32 94 44 Z" fill="#F2D07A" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M22 46 Q64 38 106 46 Q64 54 22 46Z" fill="#F2D07A" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M38 42 Q64 36 90 42" fill="none" stroke="#4E7BF2" stroke-width="3"/>'
    b += d.face(64, 64, d=9, k=0.85)
    b += '<circle cx="104" cy="22" r="7" fill="#FF9A3C" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<path d="M92 34 q4 -4 6 -6" stroke="#FF9A3C" stroke-width="2" stroke-dasharray="2 3" fill="none"/>'
    b += '<path d="M8 82 q6 -6 12 0 q6 6 12 0" fill="none" stroke="#FFC37A" stroke-width="2" opacity=".8"/>'
    save("sokol-tt-leningradsky", "yellow", b,
         "красная ракетка для настольного тенниса в соломенной пляжной панаме с синей лентой",
         "стоит на белом тёплом песке зала пляжного волейбола и подбрасывает вверх оранжевый мячик")


# 7. Каток «Маяк»: корабельная рында звонит, открывая дискотеки на льду
def mayak_rink():
    b = '<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#DFF3FF" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M40 22 H88" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/>'
    b += '<path d="M64 22 V30" stroke="#3B3355" stroke-width="4"/>'
    b += '<path d="M48 36 Q48 28 64 28 Q80 28 80 36 L86 82 Q64 90 42 82Z" fill="#F2B632" ' + d.s() + '/>'
    b += '<path d="M44 74 Q64 80 84 74" fill="none" stroke="#B9822A" stroke-width="2.6"/>'
    b += '<path d="M42 82 Q64 90 86 82 L88 88 Q64 96 40 88Z" fill="#E09A1E" ' + d.s('stroke-width="2.6"') + '/>'
    b += d.face(64, 54, d=8, k=0.8)
    b += '<path d="M64 92 Q72 98 70 106" fill="none" stroke="#3B3355" stroke-width="2.4"/>'
    b += '<circle cx="70" cy="106" r="4" fill="#E8463C" ' + d.s('stroke-width="2"') + '/>'
    b += '<path d="M44 100 H58 Q60 94 56 94 H48Z M70 100 H84 Q86 94 82 94 H74Z" fill="#2E3A55" ' + d.s('stroke-width="2"') + '/>'
    b += blade(40, 58, 104, w=3.4) + blade(68, 84, 104, w=3.4)
    for x, y, c in [(20, 40, "#FF5FA2"), (106, 46, "#5FD3FF"), (18, 70, "#FFE05F"), (110, 74, "#9B7BFF")]:
        b += f'<path d="M{x} {y} m-6 0 q6 -8 12 0" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"/>'
        b += f'<circle cx="{x}" cy="{y + 6}" r="2.4" fill="{c}"/>'
    save("mayak-rink-krasny-mayak", "night", b,
         "латунная корабельная рында-колокол с мордашкой и красным язычком на шнурке",
         "встала на чёрные коньки и звонит в себя, а по вечернему катку разлетаются разноцветные ноты дискотеки")


# 8. Ice Fenix: огненное перо на коньке выписывает восьмёрку
def ice_fenix():
    b = '<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#E9F7FF" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M30 112 C10 104 30 92 50 104 C70 116 92 116 98 106 C104 96 80 92 64 104" fill="none" stroke="#9DD6F5" stroke-width="2.6" stroke-dasharray="5 4"/>'
    b += ('<path d="M64 92 Q38 76 40 48 Q42 26 66 12 Q60 30 72 34 Q70 22 82 18 Q78 34 88 44 Q96 70 64 92Z" '
          'fill="#FF7A2E" ' + d.s() + '/>')
    b += '<path d="M64 88 Q50 72 54 52 Q58 40 68 34 Q66 50 78 56 Q82 74 64 88Z" fill="#FFC531"/>'
    b += '<path d="M64 92 Q62 70 66 40" fill="none" stroke="#B4401A" stroke-width="2.6" stroke-linecap="round"/>'
    for y in (54, 64, 74):
        b += f'<path d="M64 {y} l-8 -6 M65 {y} l8 -6" stroke="#B4401A" stroke-width="1.8" stroke-linecap="round"/>'
    b += d.face(65, 62, d=8, k=0.7)
    b += '<path d="M52 92 V84 Q52 80 56 80 H70 Q74 80 74 84 V92Z" fill="#FFFFFF" ' + d.s('stroke-width="2.4"') + '/>'
    b += blade(48, 74, 97, w=4)
    b += '<path d="M52 97 V93 M72 97 V93" stroke="#3B3355" stroke-width="2.4"/>'
    b += d.sparkle(102, 28, 5, "#FFE08A") + d.sparkle(24, 40, 4, "#FFE08A")
    save("ice-fenix-sokolniki", "pink", b,
         "огненно-оранжевое перо с жёлтой серединкой и мордашкой",
         "встало на один белый фигурный конёк и выписывает на льду пунктирную восьмёрку")


# 9. Каток «Луч»: электрическая лампочка на коньках освещает лёд
def luch_rink():
    b = '<path d="M0 100 Q64 92 128 100 V128 H0Z" fill="#CFE6FF" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M64 66 L16 128 H112Z" fill="#FFF3A6" opacity=".55"/>'
    b += '<path d="M44 44 Q44 18 64 18 Q84 18 84 44 Q84 56 74 64 V72 H54 V64 Q44 56 44 44Z" fill="#FFE45E" ' + d.s() + '/>'
    b += '<path d="M58 58 Q60 46 64 52 Q68 46 70 58" fill="none" stroke="#E0A21E" stroke-width="2.4"/>'
    b += '<rect x="54" y="72" width="20" height="14" rx="3" fill="#AEB9CF" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M54 77 H74 M54 82 H74" stroke="#3B3355" stroke-width="1.8"/>'
    b += d.face(64, 38, d=8, k=0.75)
    b += '<path d="M56 86 V94 M72 86 V94" stroke="#3B3355" stroke-width="3"/>'
    b += '<path d="M46 98 H58 Q60 92 56 92 H50Z M70 98 H82 Q84 92 80 92 H74Z" fill="#E8463C" ' + d.s('stroke-width="2"') + '/>'
    b += blade(42, 58, 102, w=3.4) + blade(68, 82, 102, w=3.4)
    for a, x2, y2 in [(0, 22, 26), (1, 106, 26), (2, 30, 8), (3, 98, 8)]:
        x1 = 38 if x2 < 64 else 90
        y1 = 34 if y2 > 20 else 20
        b += f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>'
    save("luch-rink-volokolamskoe", "night", b,
         "жёлтая электрическая лампочка с цоколем и мордашкой",
         "надела красные коньки и катится по тёмному вечернему льду, освещая его широким тёплым лучом")


# 10. Ледовая арена им. Петрусевой (Павловский Посад): павлин на коньках
def petruseva_rink():
    b = '<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#EEF9FF" ' + d.s('stroke-width="2.4"') + '/>'
    for i, (x, y) in enumerate([(20, 70), (26, 44), (42, 24), (64, 16), (86, 24), (102, 44), (108, 70)]):
        b += f'<path d="M64 80 L{x} {y}" stroke="#2E8B6E" stroke-width="3"/>'
        b += f'<ellipse cx="{x}" cy="{y}" rx="10" ry="8" fill="#2DB37A" ' + d.s('stroke-width="2.2"') + '/>'
        b += f'<circle cx="{x}" cy="{y}" r="4.5" fill="#2F6FD6"/><circle cx="{x}" cy="{y}" r="2" fill="#F2C14E"/>'
    b += '<ellipse cx="64" cy="80" rx="15" ry="18" fill="#2F6FD6" ' + d.s() + '/>'
    b += '<path d="M64 64 Q58 52 62 40 Q70 36 72 44 Q70 54 66 64" fill="#2F6FD6" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M66 32 V38 M62 33 L64 38 M70 33 L68 38" stroke="#3B3355" stroke-width="1.8"/>'
    b += '<path d="M72 44 L80 46 L72 48Z" fill="#F2C14E" ' + d.s('stroke-width="1.8"') + '/>'
    b += d.eye(68, 43, 0.6)
    b += '<path d="M58 96 V100 M70 96 V100" stroke="#3B3355" stroke-width="3"/>'
    b += blade(50, 64, 102, w=3.4) + blade(64, 78, 102, w=3.4)
    save("petruseva-rink-pposad", "purple", b,
         "сине-зелёный павлин с хвостом-веером из «глазков»",
         "распустил хвост во весь круг и важно едет на двух коньках по льду ледовой арены")


# 11. Черневская горка (Красногорск): горный козёл-архар на горных лыжах
def chernevskaya():
    b = '<path d="M0 40 L128 112 V128 H0Z" fill="#FFFFFF" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M96 24 L104 10 L112 24Z M100 36 L108 20 L116 36Z" fill="#3E8E55" ' + d.s('stroke-width="2"') + '/>'
    b += '<path d="M108 36 V44" stroke="#6B4A2E" stroke-width="3"/>'
    b += '<ellipse cx="60" cy="70" rx="24" ry="14" fill="#B07A4A" ' + d.s() + ' transform="rotate(28 60 70)"/>'
    b += '<path d="M48 80 L42 96 M58 86 L54 100 M70 80 L74 94" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/>'
    b += '<circle cx="40" cy="50" r="13" fill="#B07A4A" ' + d.s() + '/>'
    b += '<path d="M36 40 Q20 30 22 46 Q26 52 32 46" fill="none" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/>'
    b += '<path d="M36 40 Q20 30 22 46 Q26 52 32 46" fill="none" stroke="#D9C39A" stroke-width="2.6" stroke-linecap="round"/>'
    b += '<path d="M46 38 Q60 28 60 44 Q56 50 50 46" fill="none" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/>'
    b += '<path d="M46 38 Q60 28 60 44 Q56 50 50 46" fill="none" stroke="#D9C39A" stroke-width="2.6" stroke-linecap="round"/>'
    b += d.eye(38, 50, 0.6) + d.eye(46, 52, 0.6)
    b += '<path d="M34 60 Q36 68 40 62" fill="#EDE3D0" ' + d.s('stroke-width="1.8"') + '/>'
    b += '<path d="M26 38 L18 34 L22 30 L30 34Z" fill="#E8463C" ' + d.s('stroke-width="1.6"') + '/>'
    # лыжи
    b += '<path d="M26 92 L82 116 Q90 120 92 114" fill="none" stroke="#E8463C" stroke-width="5" stroke-linecap="round"/>'
    b += '<path d="M40 86 L96 110 Q104 114 106 108" fill="none" stroke="#2F6FD6" stroke-width="5" stroke-linecap="round"/>'
    b += '<path d="M30 64 L14 100 M80 66 L84 104" stroke="#3B3355" stroke-width="2.6"/>'
    b += '<circle cx="14" cy="100" r="3" fill="none" stroke="#3B3355" stroke-width="2"/><circle cx="84" cy="104" r="3" fill="none" stroke="#3B3355" stroke-width="2"/>'
    save("chernevskaya-gorka-krasnogorsk", "sky", b,
         "бурый горный козёл-архар с закрученными светлыми рогами и красным помпоном-шапочкой",
         "мчится вниз по снежному склону на красной и синей горных лыжах, оттолкнувшись палками от ёлок")


ALL = [deinega_bitsa, monster_hockey, arenaplay_yug, led_noginsk, pro_hockey_soloslovo, sokol_tt, mayak_rink, ice_fenix,
       luch_rink, petruseva_rink, chernevskaya]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for f in ALL:
        f()
    for pid, line in SUBJ.items():
        if not only or pid in only:
            print(line)
