"""Fixer 07.11: na-naberezhnoy — Вадим: «Не подходящая аватарка для драматического театра» (был ламантин).
Новая идея: пара театральных масок драмы — большая весёлая золотая утешает маленькую грустную голубую,
у грустной слезинка; маски связаны красной лентой с бантом."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def mask_path(cx, cy, w, h):
    return (f"M{cx-w/2} {cy-h*.42} Q{cx} {cy-h*.62} {cx+w/2} {cy-h*.42} "
            f"Q{cx+w*.56} {cy+h*.12} {cx} {cy+h*.5} Q{cx-w*.56} {cy+h*.12} {cx-w/2} {cy-h*.42} Z")


def naberezhnoy():
    b = ""
    # мягкий луч софита сверху
    b += '<path d="M44 -4 L84 -4 L120 128 L8 128 Z" fill="#fff" opacity=".18"/>'
    # ГРУСТНАЯ маска (сзади справа, голубая)
    g = f'<g transform="rotate(16 86 58)">'
    g += f'<path d="{mask_path(86, 58, 44, 56)}" fill="#7FB6F0" {s()}/>'
    g += '<path d="M70 40 Q78 36 84 40" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".6"/>'
    # брови домиком
    g += f'<path d="M70 44 L80 40 M102 44 L92 40" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
    # глаза-прорези вниз
    g += f'<path d="M71 52 Q76 47 81 52 Q76 50 71 52 Z M91 52 Q96 47 101 52 Q96 50 91 52 Z" fill="{O}" {s("stroke-width=\"2.4\"")}/>'
    # рот-подкова вниз
    g += f'<path d="M78 72 Q86 64 94 72 Q86 69 78 72 Z" fill="{O}" {s("stroke-width=\"2.4\"")}/>'
    g += '</g>'
    b += g
    # слезинка
    b += f'<path d="M104 66 Q100 74 104 77 Q108 74 104 66 Z" fill="#CFF0FF" {s("stroke-width=\"2.2\"")}/>'
    # ВЕСЁЛАЯ маска (крупно, слева спереди, золотая)
    v = f'<g transform="rotate(-12 50 70)">'
    v += f'<path d="{mask_path(50, 70, 60, 74)}" fill="#FFC93C" {s()}/>'
    v += '<path d="M28 46 Q38 40 48 44" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" opacity=".7"/>'
    # брови дугой вверх
    v += f'<path d="M30 50 Q36 45 42 49 M58 49 Q64 45 70 50" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
    # смеющиеся глаза-дужки
    v += f'<path d="M31 59 Q37 52 43 59 Q37 56 31 59 Z M57 59 Q63 52 69 59 Q63 56 57 59 Z" fill="{O}" {s("stroke-width=\"2.6\"")}/>'
    # румянец
    v += '<ellipse cx="30" cy="67" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".7"/><ellipse cx="70" cy="67" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".7"/>'
    # широкая улыбка
    v += f'<path d="M36 72 Q50 74 64 72 Q60 88 50 88 Q40 88 36 72 Z" fill="{O}" {s("stroke-width=\"2.6\"")}/>'
    v += '<path d="M43 82 Q50 86 57 82 Q53 88 50 88 Q46 88 43 82 Z" fill="#FF6F8E"/>'
    v += '</g>'
    b += v
    # красная лента с бантом, связывающая маски
    b += f'<path d="M66 34 Q74 30 80 34" fill="none" stroke="#E5394F" stroke-width="5" stroke-linecap="round"/>'
    b += f'<path d="M72 30 L60 22 L62 36 Z M72 30 L84 20 L84 36 Z" fill="#E5394F" {s("stroke-width=\"2.4\"")}/>'
    b += f'<circle cx="72" cy="30" r="4" fill="#E5394F" {s("stroke-width=\"2.4\"")}/>'
    b += f'<path d="M70 33 Q66 44 70 52 M74 33 Q80 42 78 50" fill="none" stroke="#E5394F" stroke-width="3.4" stroke-linecap="round"/>'
    # искорки аплодисментов
    b += sparkle(108, 26, 5, "#fff") + sparkle(20, 24, 4, "#fff") + sparkle(112, 98, 3.5, "#FFF3B0")
    return svg("pink", b)


open(os.path.join(ROOT, "icons-src", "na-naberezhnoy.svg"), "w").write(naberezhnoy())
