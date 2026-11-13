"""Иконки робота rare 2026-11-13 (1113e) — каждая придумана и нарисована отдельно (абсолютная уникальность):
- rink-yurlovsky-mass  — герой: красная варежка-конькобежец | сцена: скользит на коньке по катку, оставляя петлю-след
- rink-ionova-elektrostal — герой: голубая снежинка-фигуристка | сцена: крутит пируэт на одном коньке, вьётся морозная спираль
- badm-malkov-ramenskoe — герой: бадминтонный волан-ракета | сцена: стоит на перьях как ракета на старте, снизу клубы дыма, готов взлететь
- climb-oskal-andropova — герой: тигрёнок-скалолаз с широким оскалом | сцена: карабкается по стене с цветными зацепами (оскал — по названию «О'скал»)
Запуск: python3 tools/icons_rare_1113e.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons as d

O = d.O
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")


def ice(col="#EAF7FF", line="#9FCFE6"):
    return (f'<rect x="-4" y="100" width="136" height="32" fill="{col}"/>'
            f'<path d="M-4 100 H132" stroke="{line}" stroke-width="2.4" fill="none" stroke-linecap="round"/>')


# ---------- 1. Варежка-конькобежец (Юрловский, массовое катание) ----------
def yurlovsky():
    b = ice()
    # петля-след на льду
    b += ('<path d="M22 118 Q40 108 58 116 Q72 122 86 112 Q98 104 110 110" fill="none" '
          'stroke="#BBDCF2" stroke-width="2.6" stroke-linecap="round"/>')
    # конёк под варежкой
    b += ('<path d="M44 108 H84 Q90 108 88 102 H46Z" fill="#DCE6F2" ' + d.s('stroke-width="3.0"') + '/>'
          '<path d="M44 115 H92 Q96 115 94 111 H44Z" fill="#CFE0FF" ' + d.s('stroke-width="2.8"') + '/>'
          '<path d="M46 111 H90" stroke="#9FB4D6" stroke-width="1.6" fill="none" stroke-linecap="round"/>')
    # варежка (красная) — тело + большой палец
    b += ('<path d="M40 44 Q40 28 60 28 Q80 28 80 46 L80 92 Q80 104 64 104 Q48 104 48 92 Z" '
          'fill="#E8464F" ' + d.s('stroke-width="3.2"') + '/>')
    # большой палец сбоку
    b += ('<path d="M80 54 Q98 50 98 66 Q98 78 82 78 Z" fill="#E8464F" ' + d.s('stroke-width="3.0"') + '/>')
    # вязаная манжета с помпоном
    b += ('<rect x="44" y="90" width="40" height="16" rx="5" fill="#F7C6CD" ' + d.s('stroke-width="3.0"') + '/>'
          '<path d="M50 90 V106 M58 90 V106 M66 90 V106 M74 90 V106" stroke="#D98691" stroke-width="1.8" fill="none" stroke-linecap="round"/>'
          '<circle cx="64" cy="112" r="6" fill="#FFFFFF" ' + d.s('stroke-width="2.6"') + '/>')
    # узор-снежинка на варежке
    b += ('<g stroke="#FFD7DC" stroke-width="2.2" stroke-linecap="round">'
          '<path d="M60 58 V74 M52 66 H68 M54 60 L66 72 M66 60 L54 72"/></g>')
    # мордочка
    b += d.face(60, 48, d=8, k=1.0)
    d.save = None
    open(os.path.join(OUT, "rink-yurlovsky-mass.svg"), "w").write(d.svg("purple", b))


# ---------- 2. Снежинка-фигуристка (Ионова, Электросталь) ----------
def ionova():
    b = ice("#EAF7FF", "#9FCFE6")
    # морозная спираль-след пируэта
    b += ('<path d="M64 112 Q50 108 54 98 Q58 90 70 94 Q80 98 74 106" fill="none" '
          'stroke="#BBDCF2" stroke-width="2.6" stroke-linecap="round"/>')
    # конёк, на котором стоит
    b += ('<path d="M52 104 H78 Q82 104 80 99 H54Z" fill="#DCE6F2" ' + d.s('stroke-width="2.8"') + '/>'
          '<path d="M52 110 H84 Q88 110 86 106 H52Z" fill="#CFE0FF" ' + d.s('stroke-width="2.6"') + '/>')
    # шесть лучей снежинки (тело героя), крупно по центру
    arms = ''
    import math
    for i in range(6):
        a = math.radians(i * 60 - 90)
        x1, y1 = 64 + 7 * math.cos(a), 56 + 7 * math.sin(a)
        x2, y2 = 64 + 30 * math.cos(a), 56 + 30 * math.sin(a)
        # боковые веточки
        ax, ay = 64 + 20 * math.cos(a), 56 + 20 * math.sin(a)
        bx1, by1 = ax + 8 * math.cos(a + 1.0), ay + 8 * math.sin(a + 1.0)
        bx2, by2 = ax + 8 * math.cos(a - 1.0), ay + 8 * math.sin(a - 1.0)
        arms += (f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="{O}" stroke-width="7.4" fill="none" stroke-linecap="round"/>'
                 f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="#BFE6FF" stroke-width="4.2" fill="none" stroke-linecap="round"/>'
                 f'<path d="M{ax:.1f} {ay:.1f} L{bx1:.1f} {by1:.1f} M{ax:.1f} {ay:.1f} L{bx2:.1f} {by2:.1f}" stroke="{O}" stroke-width="4.6" fill="none" stroke-linecap="round"/>'
                 f'<path d="M{ax:.1f} {ay:.1f} L{bx1:.1f} {by1:.1f} M{ax:.1f} {ay:.1f} L{bx2:.1f} {by2:.1f}" stroke="#BFE6FF" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    b += arms
    # центральный круг-лицо
    b += f'<circle cx="64" cy="56" r="18" fill="#EAF7FF" ' + d.s('stroke-width="3.0"') + '/>'
    b += d.face(64, 54, d=7, k=1.0)
    # поднятые ручки-искорки
    b += d.sparkle(96, 40, 5, "#FFFFFF") + d.sparkle(30, 44, 4, "#FFFFFF") + d.sparkle(100, 76, 4, "#FFFFFF")
    open(os.path.join(OUT, "rink-ionova-elektrostal.svg"), "w").write(d.svg("teal", b))


# ---------- 3. Волан-ракета на старте (бадминтон Малькова) ----------
def malkov():
    b = ('<rect x="-4" y="104" width="136" height="28" fill="#FFE6CC"/>'
         '<path d="M-4 104 H132" stroke="#E7B987" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
    # пусковой дым снизу
    b += ('<g fill="#FFFFFF" opacity="0.92">'
          '<circle cx="54" cy="108" r="9"/><circle cx="64" cy="112" r="11"/><circle cx="76" cy="108" r="9"/>'
          '<circle cx="46" cy="112" r="6"/><circle cx="84" cy="112" r="6"/></g>')
    # перья волана (юбка) — как сопло ракеты, стоит вертикально
    feathers = ''
    for i, dx in enumerate((-26, -13, 0, 13, 26)):
        feathers += (f'<path d="M{64+dx*0.42:.1f} 74 L{64+dx:.1f} 104 L{64+dx+9:.1f} 104 Z" '
                     f'fill="#FFFFFF" ' + d.s('stroke-width="2.6"') + '/>')
    b += feathers
    # ободок
    b += ('<path d="M52 72 Q64 66 76 72 L74 80 Q64 75 54 80 Z" fill="#FFE08A" ' + d.s('stroke-width="2.6"') + '/>')
    # пробковая головка-нос ракеты (крупно, сверху)
    b += ('<path d="M50 54 Q50 24 64 18 Q78 24 78 54 Q64 62 50 54 Z" fill="#F2A54B" ' + d.s('stroke-width="3.2"') + '/>')
    b += ('<path d="M57 26 Q64 22 71 26" fill="none" stroke="#C97E2E" stroke-width="2.0" stroke-linecap="round"/>')
    # мордочка на головке
    b += d.face(64, 42, d=7.5, k=1.0)
    # огонёк-искры запуска сверху (летит вверх)
    b += ('<path d="M64 14 L61 6 M64 14 L67 6" stroke="#FF8A2B" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
    b += d.sparkle(30, 46, 4, "#FFFFFF") + d.sparkle(98, 50, 4.5, "#FFFFFF") + d.sparkle(92, 26, 3.5, "#FFFFFF")
    open(os.path.join(OUT, "badm-malkov-ramenskoe.svg"), "w").write(d.svg("orange", b))


# ---------- 4. Тигрёнок-скалолаз с оскалом (О'скал) ----------
def oskal():
    # стена скалодрома с цветными зацепами
    b = ('<rect x="-4" y="-4" width="136" height="136" fill="#CDEBB6"/>'
         '<rect x="70" y="-4" width="62" height="136" fill="#B7E09A"/>'
         '<path d="M70 -4 V132" stroke="#8FC773" stroke-width="2.2" fill="none"/>')
    holds = [(92, 20, "#E8464F"), (108, 46, "#F2A54B"), (86, 60, "#5FA9E8"),
             (110, 84, "#A98BF0"), (90, 100, "#FFD45E")]
    for x, y, c in holds:
        b += f'<path d="M{x} {y} q7 -4 9 4 q1 7 -7 7 q-7 0 -2 -11Z" fill="{c}" ' + d.s('stroke-width="2.2"') + '/>'
    # хвост тигрёнка
    b += ('<path d="M40 92 Q22 96 24 80 Q25 70 34 74" fill="none" stroke="#F2A24A" stroke-width="7" stroke-linecap="round"/>'
          '<path d="M27 86 L24 86 M30 80 L27 79 M33 76 L31 73" stroke="#3B3355" stroke-width="2.2" stroke-linecap="round"/>')
    # тело тигрёнка (карабкается, крупно)
    b += ('<path d="M40 60 Q36 96 56 100 Q78 102 76 74 Q74 56 56 56 Q44 56 40 60Z" '
          'fill="#F2A24A" ' + d.s('stroke-width="3.2"') + '/>')
    # полоски на теле
    b += ('<g stroke="#3B3355" stroke-width="2.6" stroke-linecap="round">'
          '<path d="M48 70 Q52 72 56 70"/><path d="M46 82 Q52 85 58 82"/><path d="M50 94 Q56 96 62 93"/></g>')
    # лапки на зацепах
    b += ('<path d="M72 64 Q86 58 86 60" fill="none" stroke="#F2A24A" stroke-width="8" stroke-linecap="round"/>'
          '<path d="M60 56 Q66 44 86 56" fill="none" stroke="#F2A24A" stroke-width="8" stroke-linecap="round"/>')
    # голова тигрёнка
    b += ('<circle cx="52" cy="48" r="20" fill="#F7B861" ' + d.s('stroke-width="3.2"') + '/>')
    # ушки
    b += ('<circle cx="40" cy="34" r="7" fill="#F2A24A" ' + d.s('stroke-width="2.6"') + '/>'
          '<circle cx="64" cy="34" r="7" fill="#F2A24A" ' + d.s('stroke-width="2.6"') + '/>')
    # щёчки-полоски
    b += ('<g stroke="#3B3355" stroke-width="2.4" stroke-linecap="round">'
          '<path d="M36 44 H44 M36 50 H44 M60 44 H68 M60 50 H68"/></g>')
    # глазки
    b += d.eye(46, 44, 0.95) + d.eye(58, 44, 0.95)
    # нос
    b += '<path d="M49 52 H55 L52 56Z" fill="#E86A8E" ' + d.s('stroke-width="1.8"') + '/>'
    # ОСКАЛ — широкая улыбка с зубами (по названию «О'скал»)
    b += ('<path d="M42 58 Q52 70 62 58 Q58 56 52 56 Q46 56 42 58Z" fill="#FFFFFF" ' + d.s('stroke-width="2.4"') + '/>'
          '<path d="M46 57 L48 61 M52 56 L52 62 M58 57 L56 61" stroke="#3B3355" stroke-width="1.6" stroke-linecap="round"/>')
    open(os.path.join(OUT, "climb-oskal-andropova.svg"), "w").write(d.svg("green", b))


if __name__ == "__main__":
    yurlovsky(); ionova(); malkov(); oskal()
    print("нарисовано: rink-yurlovsky-mass, rink-ionova-elektrostal, badm-malkov-ramenskoe, climb-oskal-andropova")
