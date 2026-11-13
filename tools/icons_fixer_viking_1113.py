"""Перерисовка viking-fc-solntsevo по сообщению Вадима 13.11 («Аватарка не подходит»)."""
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from draw_icons import svg, s, eye, face, sparkle, O

def pent(cx, cy, r, rot=-90):
    pts = " ".join(f"{cx+r*math.cos(math.radians(rot+72*i)):.1f},{cy+r*math.sin(math.radians(rot+72*i)):.1f}" for i in range(5))
    return f'<polygon points="{pts}" fill="#2E2A3D"/>'

cx, cy, R = 64, 72, 36
b = []
# газон
b.append('<path d="M0 104 Q64 94 128 104 L128 128 L0 128Z" fill="#6CC04A"/>')
# тень
b.append(f'<ellipse cx="{cx}" cy="{cy+R+1}" rx="30" ry="5" fill="#2E2A3D" opacity=".25"/>')
# мяч
b.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#FFFFFF" {s()}/>')
b.append(f'<g clip-path="url(#bc)"><clipPath id="bc"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath>')
b.append(pent(cx, cy+16, 9, 90))
for a in (-162, -18, 54, 126, 198):
    x = cx + 37*math.cos(math.radians(a)); y = cy + 37*math.sin(math.radians(a))
    b.append(pent(x, y, 11, a))
b.append('</g>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" {s()}/>')
# лицо
b.append(face(cx, cy-2, d=11, k=1.05))
# шлем викинга (маленький, сверху)
b.append(f'<path d="M40 50 Q64 22 88 50 Z" fill="#B9C3CF" {s()}/>')
b.append(f'<rect x="38" y="46" width="52" height="7" rx="3" fill="#E0A23A" {s("stroke-width=\"2.4\"")}/>')
b.append(f'<path d="M42 46 Q22 46 18 30 Q30 38 44 37 Z" fill="#FFF1D6" {s("stroke-width=\"2.4\"")}/>')
b.append(f'<path d="M86 46 Q106 46 110 30 Q98 38 84 37 Z" fill="#FFF1D6" {s("stroke-width=\"2.4\"")}/>')
b.append(f'<circle cx="64" cy="36" r="2.5" fill="#E0A23A"/>')
b.append(sparkle(108, 70, 6))
open(os.path.join(os.path.dirname(__file__), "..", "icons-src", "viking-fc-solntsevo.svg"), "w").write(svg("teal", "".join(b)))
