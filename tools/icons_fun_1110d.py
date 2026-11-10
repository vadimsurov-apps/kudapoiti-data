"""Иконки робота fun (2026-11-10, утренний проход): 3 места из tools/add_fun_1110d.py.
Каждая придумана и нарисована отдельно. Запуск: python3 tools/icons_fun_1110d.py"""
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

# лимузин гаража особого назначения
I["fso-garage-museum-vdnh"] = ("#E3F1EC", "#3E8C78",
    "длинный чёрный правительственный лимузин с хромированной решёткой-улыбкой и двумя флажками на крыльях",
    "гордо выезжает из распахнутых ворот павильона на ВДНХ по красной ковровой дорожке",
    f'<path d="M6 30 H122 V96 H6Z" fill="#F4E9D2" {W(3)}/>'
    f'<path d="M20 96 V48 Q64 30 108 48 V96" fill="#5A4636" {W(3)}/>'
    f'<path d="M30 130 L44 92 H84 L98 130Z" fill="#D7263D" {W(3)}/>'
    f'<path d="M14 84 Q16 66 34 64 L46 50 Q64 44 82 50 L94 64 Q112 66 114 84 V92 H14Z" fill="#1E2430" {W(3.2)}/>'
    f'<path d="M50 54 Q64 50 78 54 L86 64 H42Z" fill="#9CC8E8" {W(2.4)}/><path d="M64 52 V64" {W(2)}/>'
    f'<rect x="40" y="76" width="48" height="12" rx="4" fill="#D9DEE6" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 77 V87" stroke="#8B95A5" stroke-width="1.6"/>' for x in range(46, 86, 6)) +
    f'<circle cx="26" cy="80" r="6" fill="#FFF3B0" {W(2.2)}/><circle cx="102" cy="80" r="6" fill="#FFF3B0" {W(2.2)}/>'
    f'<circle cx="30" cy="96" r="9" fill="#2B2B2B" {W(2.6)}/><circle cx="98" cy="96" r="9" fill="#2B2B2B" {W(2.6)}/>'
    f'<circle cx="30" cy="96" r="3.5" fill="#D9DEE6"/><circle cx="98" cy="96" r="3.5" fill="#D9DEE6"/>'
    + face(64, 69, d=10, k=0.5, mouth=False) +
    f'<path d="M22 66 V52" {W(2)}/><path d="M22 52 h9 v6 h-9Z" fill="#fff" stroke="{O}" stroke-width="1.6"/><path d="M22 54 h9 v2 h-9Z" fill="#2E6BD6"/><path d="M22 56 h9 v2 h-9Z" fill="#D7263D"/>'
    f'<path d="M106 66 V52" {W(2)}/><path d="M106 52 h-9 v6 h9Z" fill="#fff" stroke="{O}" stroke-width="1.6"/><path d="M106 54 h-9 v2 h9Z" fill="#2E6BD6"/><path d="M106 56 h-9 v2 h9Z" fill="#D7263D"/>'
    f'<rect x="54" y="34" width="20" height="10" rx="2" fill="#FFC21A" {W(2)}/><path d="M58 39 h12" stroke="{O}" stroke-width="1.8"/>')

# покровский собор — спиральный купол
I["pokrovsky-sobor-red-square"] = ("#F3EAFF", "#9C7BD8",
    "главный луковичный купол собора в красно-зелёную спираль с золотым крестиком",
    "стоит на кирпичном барабане Красной площади, а рядом выглядывает маленький сине-белый купол-зигзаг",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#B9B3AE" {W(3)}/>'
    + "".join(f'<path d="M{x} 108 l6 22" stroke="#8E8780" stroke-width="2"/>' for x in range(0, 128, 14)) +
    f'<rect x="86" y="66" width="24" height="42" fill="#D9543F" {W(2.6)}/>'
    f'<path d="M86 66 Q86 48 98 40 Q110 48 110 66Z" fill="#fff" {W(2.6)}/>'
    f'<path d="M88 60 l5 -6 l5 6 l5 -6 l5 6" fill="none" stroke="#2E6BD6" stroke-width="3"/><path d="M90 50 l4 -4 l4 4 l4 -4" fill="none" stroke="#2E6BD6" stroke-width="2.6"/>'
    f'<path d="M98 40 V32" {W(2)}/>'
    f'<rect x="36" y="74" width="44" height="34" fill="#C8442F" {W(3)}/>'
    + "".join(f'<path d="M{x} 80 v20 a4 4 0 0 0 8 0 v-20Z" fill="#7A2A1E" {W(1.8)}/>' for x in (42, 54, 66)) +
    f'<path d="M30 74 Q26 50 46 36 Q58 28 58 16 Q58 28 70 36 Q90 50 86 74Z" fill="#3FAE5A" {W(3.2)}/>'
    f'<clipPath id="dome"><path d="M30 74 Q26 50 46 36 Q58 28 58 16 Q58 28 70 36 Q90 50 86 74Z"/></clipPath>'
    f'<g clip-path="url(#dome)">' + "".join(f'<path d="M{x} 80 Q{x+18} 50 {x+44} 20" stroke="#E8434A" stroke-width="8" fill="none"/>' for x in (6, 24, 42, 60)) + '</g>'
    f'<path d="M30 74 Q26 50 46 36 Q58 28 58 16 Q58 28 70 36 Q90 50 86 74Z" fill="none" {W(3.2)}/>'
    f'<ellipse cx="58" cy="60" rx="17" ry="10" fill="#FFF6E0" {W(2.2)}/>'
    + face(58, 58, d=7, k=0.5) +
    f'<path d="M58 16 V4 M53 9 H63" stroke="#E0A800" stroke-width="3.4" stroke-linecap="round"/>')

# мультимедиа-арт-музей — робот из телевизоров
I["mamm-ostozhenka"] = ("#FFE3F4", "#C84FA2",
    "робот-инсталляция из трёх старых ламповых телевизоров: голова-экран с глазками, туловище с радужной настроечной таблицей",
    "машет ручками-антеннами в зале музея медиаискусства, а сбоку моргает маленький телевизор-спутник",
    f'<path d="M-2 108 H130 V130 H-2Z" fill="#5B4A6B" {W(3)}/>'
    f'<rect x="40" y="62" width="48" height="40" rx="6" fill="#E9D8B4" {W(3)}/>'
    f'<rect x="46" y="68" width="30" height="28" rx="4" fill="#fff" {W(2.4)}/>'
    + "".join(f'<rect x="{46+i*5}" y="68" width="5" height="20" fill="{c}"/>' for i, c in enumerate(("#FFFFFF", "#FFE14D", "#4DD8E8", "#5CD65C", "#E84DC4", "#E8434A")))
    + f'<rect x="46" y="88" width="30" height="8" fill="#3A3A5A"/><rect x="46" y="68" width="30" height="28" rx="4" fill="none" {W(2.4)}/>'
    f'<circle cx="82" cy="74" r="2.6" fill="#7A5A3A"/><circle cx="82" cy="84" r="2.6" fill="#7A5A3A"/>'
    f'<rect x="46" y="102" width="8" height="6" fill="#3A2A20"/><rect x="74" y="102" width="8" height="6" fill="#3A2A20"/>'
    f'<rect x="42" y="22" width="44" height="38" rx="7" fill="#9AD0EC" {W(3)}/>'
    f'<rect x="48" y="28" width="32" height="26" rx="5" fill="#2B3A55" {W(2.4)}/>'
    + eye(57, 40, 0.75) + eye(71, 40, 0.75) +
    f'<path d="M60 47 Q64 51 68 47" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>'
    f'<path d="M56 22 L48 8 M72 22 L80 8" {W(2.6)}/><circle cx="48" cy="8" r="3" fill="#FFC21A" {W(1.8)}/><circle cx="80" cy="8" r="3" fill="#FFC21A" {W(1.8)}/>'
    f'<path d="M40 72 Q26 66 22 52" fill="none" {W(3)}/><path d="M88 72 Q102 66 106 52" fill="none" {W(3)}/>'
    f'<rect x="98" y="84" width="22" height="18" rx="3" fill="#FF8F3C" {W(2.4)}/><rect x="101" y="87" width="16" height="12" rx="2" fill="#B8F0FF" {W(1.8)}/>'
    f'<path d="M105 93 h3 M111 93 h3" stroke="{O}" stroke-width="2" stroke-linecap="round"/>'
    + sparkle(18, 30, 6) + sparkle(110, 26, 5))

if __name__ == "__main__":
    for pid, (a, b, hero, scene, body) in I.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
