"""fixer 09.11: перерисовка olimp-ice-loko по сообщению Вадима (был пакет со льдом).
Сиреневый фигурный конёк в прыжке над льдом, под ним на льду вычерчена «восьмёрка»."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, face, sparkle, O

BOOT = "#B98BEF"; BOOT2 = "#9C6BE0"; BLADE = "#E9EEF5"
body = (
    # лёд
    '<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="#EAF7FF" ' + s('stroke-width="2.6"') + '/>'
    # восьмёрка, вычерченная на льду
    + '<path d="M40 110 Q52 102 64 110 Q76 118 88 110 Q76 102 64 110 Q52 118 40 110Z" fill="none" stroke="#7FC4EC" stroke-width="2.6" stroke-linecap="round"/>'
    # дуга прыжка (оборот)
    + '<path d="M22 86 Q14 50 40 30" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 8" opacity=".95"/>'
    # конёк, наклонён в прыжке
    + '<g transform="translate(14 4) scale(0.8) rotate(-14 66 62)">'
    # стойки лезвия
    + f'<path d="M42 86 V93 M86 86 V93" fill="none" {s("stroke-width=\"5\"")}/>'
    # лезвие с зубцами спереди
    + f'<path d="M32 96 Q32 93 36 93 H98 Q106 93 106 98 L102 99 L104 101 L99 102 Q96 103 90 103 H36 Q32 103 32 99Z" fill="{BLADE}" {s()}/>'
    # ботинок
    + f'<path d="M36 88 Q32 60 40 36 Q44 26 56 28 L66 30 Q72 32 72 42 L74 62 Q90 66 98 74 Q104 82 98 88Z" fill="{BOOT}" {s()}/>'
    # каблук
    + f'<path d="M36 88 Q34 80 38 76 H50 V88Z" fill="{BOOT2}" {s("stroke-width=\"2.6\"")}/>'
    # язычок и шнуровка
    + f'<path d="M56 28 Q62 20 70 26 L72 40" fill="{BOOT2}" {s("stroke-width=\"2.6\"")}/>'
    + '<path d="M64 40 L72 46 M64 48 L73 54 M66 56 L76 62 M72 40 L64 46 M73 48 L64 54" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + face(54, 62, d=7, k=0.85)
    + '</g>'
    + sparkle(104, 34, 7) + sparkle(92, 20, 4) + sparkle(18, 104, 4)
)
out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "icons-src", "olimp-ice-loko.svg")
open(out, "w").write(svg("purple", body))
print("ok", out)
