"""Fixer 07.11: перерисовка по замечаниям Вадима.
ilikeice-kristall — «Не подходит аватар»: мальчик-фигурист скользит «ласточкой», лезвие рисует завиток на льду.
rink-luzhniki — «Там нет хоккея. Просто очень красивый каток с подсветкой»: конёк-персонаж под аркой гирлянды на сияющем ночном льду."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def limb(d, w, col):
    return (f'<path d="{d}" fill="none" stroke="{O}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w-5.4}" stroke-linecap="round" stroke-linejoin="round"/>')


def boot(x, y, ang=0):
    # белый ботинок фигурного конька с лезвием, носок вправо
    return (f'<g transform="rotate({ang} {x} {y})">'
            f'<path d="M{x-9} {y-12} H{x+1} L{x+3} {y-3} Q{x+12} {y-2} {x+12} {y+3} H{x-10} Z" fill="#fff" {s("stroke-width=\"2.6\"")}/>'
            f'<path d="M{x-10} {y+8} H{x+14} Q{x+17} {y+8} {x+16} {y+5}" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
            f'<path d="M{x-6} {y+3} V{y+8} M{x+8} {y+3} V{y+8}" stroke="{O}" stroke-width="2.4"/></g>')


def kristall():
    b = ""
    # лёд
    b += '<ellipse cx="64" cy="118" rx="70" ry="22" fill="#EAF6FF" stroke="#3B3355" stroke-width="3"/>'
    # след-завиток от лезвия
    b += '<path d="M14 112 Q30 100 46 108 Q58 116 52 106 Q48 100 60 104" fill="none" stroke="#7FB8E8" stroke-width="2.6" stroke-linecap="round"/>'
    # опорная нога и конёк
    b += limb("M62 66 L60 96", 15, "#3E5BC9")
    b += boot(60, 100)
    # свободная нога назад-вверх («ласточка»)
    b += limb("M66 62 L100 48", 15, "#3E5BC9")
    b += boot(106, 44, -22)
    # задняя рука вверх-назад
    b += limb("M54 56 L74 34", 12, "#FFD9B8")
    # туловище — синий костюм, наклон вперёд
    b += f'<path d="M36 52 Q50 42 68 54 L66 68 Q50 70 40 64 Z" fill="#4F6FE0" {s()}/>'
    b += '<path d="M44 52 Q52 56 62 56" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>'
    # передняя рука вперёд
    b += limb("M42 58 L16 60", 12, "#FFD9B8")
    # голова
    b += f'<circle cx="32" cy="42" r="13" fill="#FFD9B8" {s()}/>'
    b += f'<path d="M20 40 Q22 26 36 29 Q44 31 45 39 Q36 33 28 36 Z" fill="#8A5A3C" {s("stroke-width=\"2.6\"")}/>'
    b += f'<circle cx="27" cy="44" r="2.3" fill="{O}"/><circle cx="35" cy="44" r="2.3" fill="{O}"/>'
    b += '<circle cx="26.3" cy="43.2" r=".8" fill="#fff"/><circle cx="34.3" cy="43.2" r=".8" fill="#fff"/>'
    b += f'<path d="M28 49 Q31 52 34 49" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/>'
    b += '<ellipse cx="23" cy="48" rx="2.6" ry="1.5" fill="#FF7FA8" opacity=".8"/><ellipse cx="39" cy="48" rx="2.6" ry="1.5" fill="#FF7FA8" opacity=".8"/>'
    # искры-кристаллики («Кристалл»)
    b += sparkle(96, 22, 7, "#fff") + sparkle(110, 72, 4, "#fff") + sparkle(20, 86, 4, "#fff")
    return svg("purple", b)


def bulb(x, y, col):
    return (f'<path d="M{x-2} {y-4} H{x+2}" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
            f'<circle cx="{x}" cy="{y+12}" r="12" fill="{col}" opacity=".25"/>'
            f'<ellipse cx="{x}" cy="{y+3}" rx="4.6" ry="6" fill="{col}" stroke="{O}" stroke-width="2.2"/>'
            f'<ellipse cx="{x-1.5}" cy="{y+1}" rx="1.4" ry="2" fill="#fff" opacity=".8"/>')


def luzhniki():
    b = ""
    # сияющий лёд с отражениями
    b += '<ellipse cx="64" cy="112" rx="72" ry="30" fill="#BFE3FF" stroke="#3B3355" stroke-width="3"/>'
    b += '<ellipse cx="64" cy="112" rx="56" ry="20" fill="#E6F4FF" opacity=".8"/>'
    for x, c in ((30, "#FF6FA8"), (52, "#FFD54A"), (76, "#5FE0C0"), (98, "#B78CFF")):
        b += f'<path d="M{x} 92 V128" stroke="{c}" stroke-width="5" opacity=".35" stroke-linecap="round"/>'
    # гирлянда — арка проводом
    b += '<path d="M2 30 Q64 70 126 30" fill="none" stroke="#3B3355" stroke-width="2.4"/>'
    pts = [(14, 38, "#FF6FA8"), (34, 48, "#FFD54A"), (54, 52.5, "#5FE0C0"), (74, 52.5, "#FF8A3D"), (94, 48, "#B78CFF"), (114, 38, "#FF6FA8")]
    for x, y, c in pts:
        b += bulb(x, y, c)
    # конёк-персонаж: белый ботинок, красный шарфик
    b += '<ellipse cx="64" cy="112" rx="34" ry="5" fill="#3B3355" opacity=".18"/>'
    b += f'<path d="M42 64 H70 Q74 64 74 70 L76 84 Q98 86 98 96 V100 H42 Z" fill="#fff" {s()}/>'
    b += f'<path d="M42 96 H98" stroke="#DDE6F5" stroke-width="5"/>'
    b += f'<path d="M42 64 H70 Q74 64 74 70 L76 84 Q98 86 98 96 V100 H42 Z" fill="none" {s()}/>'
    # шнуровка
    b += ''.join(f'<path d="M{72+i*5} {72+i*4} l6 -2" stroke="{O}" stroke-width="2" stroke-linecap="round"/>' for i in range(3))
    # лезвие
    b += f'<path d="M48 100 V106 M90 100 V106" stroke="{O}" stroke-width="3"/>'
    b += f'<path d="M38 108 H100 Q106 108 104 102" fill="none" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>'
    b += '<path d="M40 107 H98" stroke="#E8EEF7" stroke-width="1.4"/>'
    # шарфик
    b += f'<path d="M40 66 H74 V74 H40 Z" fill="#FF4F6D" {s("stroke-width=\"2.6\"")}/>'
    b += f'<path d="M44 74 L40 90 L48 90 L50 74 Z" fill="#FF4F6D" {s("stroke-width=\"2.6\"")}/>'
    # мордочка
    b += f'<ellipse cx="52" cy="84" rx="2.8" ry="3.4" fill="{O}"/><circle cx="51.1" cy="82.7" r="1.2" fill="#fff"/>'
    b += f'<ellipse cx="64" cy="84" rx="2.8" ry="3.4" fill="{O}"/><circle cx="63.1" cy="82.7" r="1.2" fill="#fff"/>'
    b += f'<path d="M55 90 Q58 93 61 90" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    b += '<ellipse cx="47" cy="89" rx="3" ry="1.7" fill="#FF7FA8" opacity=".8"/><ellipse cx="69" cy="89" rx="3" ry="1.7" fill="#FF7FA8" opacity=".8"/>'
    # движение
    b += '<path d="M14 80 H30 M8 90 H26" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>'
    b += sparkle(104, 16, 4, "#fff") + sparkle(24, 16, 3, "#fff") + sparkle(112, 70, 3.5, "#fff")
    return svg("night", b)


open(os.path.join(ROOT, "icons-src", "ilikeice-kristall.svg"), "w").write(kristall())
open(os.path.join(ROOT, "icons-src", "rink-luzhniki.svg"), "w").write(luzhniki())
print("ok")
