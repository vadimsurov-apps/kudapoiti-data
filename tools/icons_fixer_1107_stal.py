"""Fixer 07.11: перерисовка stal-fencing-1905 по замечанию Вадима («Аватар не подходит»).
Идея: ребёнок-фехтовальщик в белом костюме и маске в классическом выпаде, клинок рапиры блестит («Сталь»)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def limb(d, w=17):
    return (f'<path d="{d}" fill="none" stroke="{O}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="#fff" stroke-width="{w-5.4}" stroke-linecap="round" stroke-linejoin="round"/>')


def stal():
    b = ""
    S3 = s('stroke-width="3"')
    S26 = s('stroke-width="2.6"')
    # пол-тень
    b += '<ellipse cx="56" cy="112" rx="40" ry="5" fill="#3B3355" opacity=".15"/>'
    # клинок рапиры (сталь) — от гарды вправо, чуть вверх
    b += f'<path d="M86 60 L121 49" stroke="#3B3355" stroke-width="4.5" stroke-linecap="round" fill="none"/>'
    b += '<path d="M86 60 L121 49" stroke="#E8EEF7" stroke-width="2" stroke-linecap="round"/>'
    b += sparkle(110, 46, 6, "#fff")
    # задняя нога (прямая, назад-влево)
    b += limb("M54 80 L24 106")
    # передняя нога (согнута в колене)
    b += limb("M58 80 L76 92 L80 106")
    # обувь
    b += f'<ellipse cx="18" cy="108" rx="9" ry="5" fill="#5B6BD6" {S26}/>'
    b += f'<ellipse cx="86" cy="108" rx="10" ry="5" fill="#5B6BD6" {S26}/>'
    # задняя рука вверх дугой
    b += limb("M48 58 Q30 54 32 34", 15)
    # туловище — белая куртка
    b += f'<path d="M42 54 Q55 46 67 54 L65 84 Q54 88 44 84Z" fill="#fff" {s()}/>'
    # синяя полоска на куртке
    b += '<path d="M55 52 L54 83" stroke="#5B6BD6" stroke-width="3"/>'
    # передняя рука вперёд
    b += limb("M60 60 L82 60", 15)
    # гарда-чашка и рукоять
    b += f'<path d="M83 50 Q92 60 83 70 Z" fill="#C9D3E3" {S26}/>'
    # голова: маска (тёмная сетка) с белым нагрудником
    b += f'<path d="M44 44 Q52 56 62 46 L60 52 Q52 58 46 52Z" fill="#fff" {S26}/>'
    b += f'<ellipse cx="54" cy="34" rx="14" ry="15" fill="#4A4466" {s()}/>'
    mesh = "".join(f'<path d="M{x} 20 V50" stroke="#8A85A6" stroke-width="1.2"/>' for x in range(42, 68, 4))
    mesh += "".join(f'<path d="M38 {y} H70" stroke="#8A85A6" stroke-width="1.2"/>' for y in range(22, 50, 4))
    b += f'<clipPath id="mk"><ellipse cx="54" cy="34" rx="12" ry="13"/></clipPath><g clip-path="url(#mk)">{mesh}</g>'
    b += f'<ellipse cx="54" cy="34" rx="14" ry="15" fill="none" {s()}/>'
    # глазки и улыбка за сеткой
    b += '<ellipse cx="49" cy="32" rx="3.4" ry="4" fill="#fff"/><ellipse cx="60" cy="32" rx="3.4" ry="4" fill="#fff"/>'
    b += f'<circle cx="49.6" cy="32.6" r="1.8" fill="{O}"/><circle cx="60.6" cy="32.6" r="1.8" fill="{O}"/>'
    b += '<path d="M51 40 Q54.5 43.5 58 40" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
    b += '<ellipse cx="45" cy="38" rx="2.6" ry="1.5" fill="#FF7FA8" opacity=".8"/><ellipse cx="64" cy="38" rx="2.6" ry="1.5" fill="#FF7FA8" opacity=".8"/>'
    b += sparkle(24, 26, 5)
    return svg("teal", b)


open(os.path.join(ROOT, "icons-src", "stal-fencing-1905.svg"), "w").write(stal())
print("ok")
