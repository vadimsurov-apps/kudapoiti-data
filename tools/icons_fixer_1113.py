"""Перерисовка иконки по сообщению Вадима 13.11 (робот fixer): cafe-la-riva — «Не подходит аватарка»
(была рыбалка, не про ресторан). Итальянский ресторан: свой сюжет — неаполитанские струффоли (в реестре нет).
Запуск: python3 tools/icons_fixer_1113.py → icons-src/cafe-la-riva.svg"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, eye, face, sparkle, s, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
draw_icons.BG["zz_lariva"] = ("#FFF0F6", "#E0679A")

balls = []
rows = [(5, 92), (4, 80), (3, 68), (2, 56)]
for n, y in rows:
    x0 = 64 - (n - 1) * 10.5
    for i in range(n):
        balls.append((x0 + i * 21, y))
SPR = ["#FF4F7B", "#4FC3F7", "#7CD26E", "#FFFFFF", "#B57CF0", "#FFB21E"]
body = '<ellipse cx="64" cy="104" rx="50" ry="13" fill="#FFFFFF" ' + s() + '/>'
body += '<ellipse cx="64" cy="102" rx="38" ry="7" fill="none" stroke="#9FD8F0" stroke-width="2.4"/>'
for k, (x, y) in enumerate(balls):
    body += f'<circle cx="{x:.1f}" cy="{y}" r="11.5" fill="#F2A93B" {s()}/>'
    body += f'<ellipse cx="{x-3.5:.1f}" cy="{y-4}" rx="3.6" ry="2.4" fill="#FFE1A0"/>'
    for j in range(2):
        c = SPR[(k * 2 + j) % len(SPR)]
        dx, dy = (-4 + j * 8, 3 - j * 2)
        body += f'<path d="M{x+dx-2:.1f} {y+dy} l3.5 -1.6" stroke="{c}" stroke-width="2.6" stroke-linecap="round"/>'
# лицо горки — на среднем ряду
body += face(64, 84, d=11, k=1.25)
# верхний шарик съезжает по склону вправо, как ребёнок с горки
bx, by = 98, 50
body += f'<path d="M82 44 q-6 -3 -12 -2 M84 36 q-6 -4 -12 -3" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>'
body += f'<circle cx="{bx}" cy="{by}" r="11.5" fill="#F7B547" {s()}/>'
body += f'<ellipse cx="{bx-3}" cy="{by-4}" rx="3.6" ry="2.4" fill="#FFE1A0"/>'
body += eye(bx - 4, by + 1, 0.6) + eye(bx + 4, by + 1, 0.6)
body += f'<ellipse cx="{bx}" cy="{by+6.5}" rx="3" ry="2.6" fill="{O}"/>'
body += sparkle(30, 34, 6) + sparkle(104, 82, 4.5)
open(os.path.join(OUT, "cafe-la-riva.svg"), "w").write(svg("zz_lariva", body))
print("ok")
