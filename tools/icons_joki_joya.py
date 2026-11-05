"""Иконки 19 новых парков Joki Joya — у каждого свой сюжет (проверено по icons-catalog: в каталоге их нет):
обруч, чёртик из коробки, американские горки, лабиринт, ксилофон, счёты, свисток, хамелеон, аксолотль,
утконос, броненосец, павлин, морской конёк, морж, нарвал, пеликан, лемур, домино, калейдоскоп."""
import os
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")

I = {
    # обруч с ребёнком
    "joki-joya-columbus": ("pink",
        f'<circle cx="64" cy="34" r="12" fill="#FFD9B8" {s()}/>' + f(64, 34, d=4.5, k=0.4, blush=False)
        + f'<path d="M64 46 V80 M64 80 L54 104 M64 80 L74 104 M64 56 L46 46 M64 56 L82 46" fill="none" {W(4)}/>'
        + f'<ellipse cx="64" cy="66" rx="34" ry="10" fill="none" stroke="#FF8A3D" stroke-width="7"/>'
        + f'<ellipse cx="64" cy="66" rx="34" ry="10" fill="none" {W(2)}/>' + sparkle(104, 40, 6) + sparkle(22, 92, 5)),
    # чёртик из коробки
    "joki-joya-iyun-mytishchi": ("yellow",
        f'<path d="M28 74 H100 V112 H28Z" fill="#E8654F" {s()}/><path d="M28 74 L16 62 M100 74 L112 62" {W(3)}/>'
        f'<path d="M28 74 L14 60 H34 Z" fill="#FF9A7A" {W(2.6)}/>'
        + f'<path d="M64 74 Q50 68 64 62 Q78 56 64 50 Q50 44 64 40" fill="none" stroke="#9AA0B8" stroke-width="5"/>'
        + f'<circle cx="64" cy="30" r="16" fill="#FFD9B8" {s()}/>' + f(64, 30, d=6, k=0.5)
        + f'<path d="M48 22 L40 10 L56 16 M80 22 L88 10 L72 16" fill="#7CD26E" {W(2.4)}/>'
        + f'<path d="M54 92 L64 84 L74 92 L64 100Z" fill="#FFD25E" {W(2.4)}/>'),
    # американские горки
    "joki-joya-vegas-kuntsevo": ("sky",
        f'<path d="M8 100 Q30 30 52 70 Q64 96 76 60 Q88 20 120 60" fill="none" stroke="#E8654F" stroke-width="6"/>'
        f'<path d="M20 100 V68 M40 100 V56 M64 100 V86 M88 100 V44 M108 100 V54" stroke="#3B3355" stroke-width="3"/>'
        f'<path d="M8 104 H120" {W(3)}/>'
        + f'<rect x="72" y="40" width="26" height="14" rx="5" fill="#FFD25E" {s()} transform="rotate(-35 85 47)"/>'
        + f'<circle cx="80" cy="36" r="6" fill="#FFD9B8" {W(2)}/><circle cx="90" cy="30" r="6" fill="#FFD9B8" {W(2)}/>'
        + sparkle(28, 26, 6)),
    # лабиринт
    "joki-joya-spektr": ("green",
        f'<rect x="22" y="22" width="84" height="84" rx="10" fill="#F7EEDB" {s()}/>'
        f'<path d="M22 46 H82 M46 46 V82 M46 82 H82 M70 64 H106 M70 64 V82 M34 64 V106 M58 22 V34 M82 82 V96" fill="none" {W(4)}/>'
        + f'<circle cx="34" cy="34" r="7" fill="#FF8A3D" {W(2.4)}/>' + f(34, 33, d=2.8, k=0.25, mouth=False, blush=False)
        + f'<path d="M92 92 l6 -10 l6 10 z" fill="#E8654F" {W(2)}/><path d="M98 82 V72" {W(2)}/>'),
    # ксилофон
    "joki-joya-edelweiss": ("purple",
        f'<path d="M18 50 L110 62 M22 98 L106 88" {W(4)}/>'
        + "".join(f'<rect x="{x}" y="{y}" width="12" height="{h}" rx="4" fill="{c}" {W(2.6)}/>'
                  for x, y, h, c in [(24, 44, 58, "#E8654F"), (40, 46, 52, "#FF9A3D"), (56, 48, 46, "#FFD25E"),
                                     (72, 50, 40, "#7CD26E"), (88, 52, 34, "#5CB7F2")])
        + f(64, 70, d=6, k=0.5)
        + f'<path d="M84 30 L104 14" {W(3)}/><circle cx="106" cy="12" r="6" fill="#E8654F" {W(2.4)}/>'),
    # счёты
    "joki-joya-otrada": ("orange",
        f'<rect x="18" y="24" width="92" height="80" rx="8" fill="#C0732E" {s()}/><rect x="28" y="34" width="72" height="60" rx="4" fill="#FFF3D6" {W(2.4)}/>'
        + "".join(f'<path d="M28 {y} H100" {W(2)}/>' + "".join(f'<circle cx="{x}" cy="{y}" r="5.5" fill="{c}" {W(2)}/>' for x in xs)
                  for y, xs, c in [(44, (36, 46, 56, 86), "#E8654F"), (60, (36, 66, 76, 86), "#5CB7F2"), (76, (36, 46, 76, 86, 94), "#7CD26E")])
        + f(64, 90, d=6, k=0.42, blush=False) + sparkle(110, 18, 6)),
    # свисток
    "joki-joya-shchelkovsky": ("teal",
        f'<path d="M26 54 Q26 40 40 40 H96 V60 H74 Q80 70 76 82 Q66 100 46 96 Q24 92 26 70Z" fill="#5CB7F2" {s()}/>'
        f'<rect x="92" y="40" width="14" height="20" rx="3" fill="#3E7FC8" {W(2.6)}/>'
        f'<circle cx="52" cy="72" r="11" fill="#FFD25E" {W(2.4)}/>' + f(46, 54, d=5, k=0.42, blush=False)
        + f'<path d="M110 34 l8 -6 M112 50 h10 M110 64 l8 6" {W(3)}/>'
        + f'<path d="M30 44 Q14 30 22 16" fill="none" stroke="#E8654F" stroke-width="3"/>'),
    # хамелеон
    "joki-joya-vesna": ("green",
        f'<path d="M28 72 Q28 44 60 42 Q90 40 96 64 Q100 80 84 84 H40 Q28 84 28 72Z" fill="#7CD26E" {s()}/>'
        f'<path d="M86 84 Q104 90 104 104 Q104 116 92 114 Q84 112 88 104" fill="none" stroke="#7CD26E" stroke-width="8" stroke-linecap="round"/>'
        f'<path d="M86 84 Q104 90 104 104 Q104 116 92 114 Q84 112 88 104" fill="none" {W(2)}/>'
        f'<path d="M40 84 V96 M60 84 V98 M76 84 V96" {W(5)}/>'
        f'<circle cx="44" cy="58" r="10" fill="#B8EAA6" {W(2.4)}/>' + eye(46, 58, 0.8)
        + f'<path d="M30 70 Q22 72 14 66" fill="none" stroke="#FF7FA8" stroke-width="4" stroke-linecap="round"/>'
        f'<path d="M58 50 Q66 58 74 50 M70 62 Q78 70 86 62" fill="none" stroke="#FFD25E" stroke-width="3"/>'),
    # аксолотль
    "joki-joya-mega-belaya-dacha": ("pink",
        f'<ellipse cx="64" cy="76" rx="30" ry="22" fill="#FFB3CF" {s()}/>'
        f'<path d="M92 80 Q114 76 116 96 Q100 96 90 88" fill="#FFB3CF" {W(2.6)}/>'
        f'<ellipse cx="64" cy="54" rx="30" ry="22" fill="#FFC6DA" {s()}/>'
        + "".join(f'<path d="M{x} {y} q{dx} -6 {dx*1.6:.0f} 4" fill="none" stroke="#E8558A" stroke-width="4" stroke-linecap="round"/>'
                  for x, y, dx in [(34, 46, -12), (34, 56, -14), (36, 64, -12), (94, 46, 12), (94, 56, 14), (92, 64, 12)])
        + f(64, 56, d=11, k=0.7)),
    # утконос
    "joki-joya-riga-mall": ("blue",
        f'<ellipse cx="66" cy="78" rx="34" ry="22" fill="#A86F3E" {s()}/>'
        f'<path d="M96 80 Q116 78 116 92 Q104 98 94 90" fill="#8A5530" {W(2.6)}/>'
        f'<circle cx="54" cy="54" r="20" fill="#B8814E" {s()}/>'
        f'<path d="M20 56 Q22 44 38 48 Q42 58 38 66 Q22 70 20 56Z" fill="#3B3355" {W(2)}/>'
        + eye(52, 48, 0.7) + eye(64, 48, 0.7)
        + f'<path d="M44 96 l-6 10 M84 96 l6 10" {W(4)}/>' + sparkle(100, 28, 6)),
    # броненосец
    "joki-joya-mari": ("yellow",
        f'<path d="M24 86 Q24 42 66 42 Q104 42 106 86Z" fill="#C9A27A" {s()}/>'
        + "".join(f'<path d="M{x} 44 Q{x+4} 64 {x} 86" fill="none" {W(2.4)}/>' for x in (44, 58, 72, 86))
        + f'<path d="M24 80 Q10 78 10 92 Q16 96 28 90Z" fill="#E0BE96" {W(2.6)}/>' + eye(18, 84, 0.55)
        + f'<path d="M20 74 l-2 -8 l6 4" fill="#E0BE96" {W(2)}/>'
        + f'<path d="M106 82 Q120 84 118 96" fill="none" {W(3)}/><path d="M40 86 V96 M88 86 V96" {W(5)}/>'
        + sparkle(100, 26, 6)),
    # павлин
    "joki-joya-kosino": ("teal",
        "".join(f'<ellipse cx="64" cy="60" rx="12" ry="40" fill="#2FA88E" {W(2)} transform="rotate({a} 64 92)"/>'
                f'<circle cx="64" cy="28" r="6" fill="#3E4AA0" stroke="#FFD25E" stroke-width="3" transform="rotate({a} 64 92)"/>'
                for a in (-60, -30, 0, 30, 60))
        + f'<ellipse cx="64" cy="88" rx="14" ry="18" fill="#3E7FC8" {s()}/><circle cx="64" cy="66" r="10" fill="#3E7FC8" {s()}/>'
        + eye(60, 64, 0.5) + eye(68, 64, 0.5) + f'<path d="M64 70 l-3 4 h6z" fill="#FFB347"/>'
        + f'<path d="M64 56 V48 M60 50 L64 46 L68 50" {W(2)}/>'),
    # морской конёк
    "joki-joya-rostokino": ("sky",
        f'<path d="M56 26 Q82 22 84 42 Q86 54 74 58 Q90 70 80 88 Q74 100 64 100 Q50 104 54 114 Q42 108 52 96 Q60 88 58 76 Q46 66 52 54 L40 50 Q38 42 44 40 Q46 30 56 26Z" fill="#FFB347" {s()}/>'
        f'<path d="M84 64 Q98 62 96 76 Q88 76 82 70" fill="#FF8A3D" {W(2.4)}/>'
        + eye(64, 38, 0.65) + f'<path d="M62 64 h12 M60 74 h14 M60 84 h12" stroke="#E8654F" stroke-width="3"/>'
        + f'<circle cx="28" cy="80" r="5" fill="#fff" {W(2)}/><circle cx="22" cy="64" r="3.5" fill="#fff" {W(1.6)}/>' + sparkle(104, 28, 6)),
    # морж
    "joki-joya-evropeisky": ("blue",
        f'<path d="M22 108 Q20 54 64 50 Q108 54 106 108Z" fill="#A87A5E" {s()}/>'
        + eye(50, 70, 0.7) + eye(78, 70, 0.7)
        + f'<ellipse cx="56" cy="86" rx="10" ry="8" fill="#C79A7E" {W(2.4)}/><ellipse cx="72" cy="86" rx="10" ry="8" fill="#C79A7E" {W(2.4)}/>'
        + f'<path d="M54 92 Q52 108 58 112 Q60 100 60 92Z M74 92 Q76 108 70 112 Q68 100 68 92Z" fill="#fff" {W(2.2)}/>'
        + f'<circle cx="64" cy="80" r="4" fill="#3B3355"/>' + sparkle(104, 26, 6) + sparkle(22, 32, 5)),
    # нарвал
    "joki-joya-gagarinsky": ("night",
        f'<path d="M18 74 Q22 50 56 52 Q90 54 100 72 Q108 62 118 64 Q112 74 116 86 Q104 84 98 78 Q86 96 54 94 Q20 92 18 74Z" fill="#9AB8E8" {s()}/>'
        f'<path d="M24 58 L4 30" stroke="#FFF3D6" stroke-width="6" stroke-linecap="round"/><path d="M24 58 L4 30" {W(2)}/>'
        + f(44, 72, d=7, k=0.6) + f'<path d="M56 94 Q64 104 74 98" fill="#9AB8E8" {W(2.4)}/>'
        + sparkle(96, 26, 7) + sparkle(70, 30, 4)),
    # пеликан
    "joki-joya-lefortovo": ("sky",
        f'<ellipse cx="70" cy="86" rx="28" ry="20" fill="#fff" {s()}/><circle cx="52" cy="46" r="16" fill="#fff" {s()}/>'
        f'<path d="M40 50 Q22 52 10 58 Q14 74 40 66Z" fill="#FFB347" {s()}/>' + eye(52, 42, 0.65)
        + f'<path d="M58 60 Q60 72 52 80" fill="none" {W(3)}/>'
        + f'<path d="M84 76 Q100 70 104 84" fill="none" {W(3)}/><path d="M62 106 V116 M78 106 V116" stroke="#FF8A3D" stroke-width="4"/>'
        + f'<path d="M4 108 Q30 100 60 108 T124 108" fill="none" stroke="#5CB7F2" stroke-width="4"/>'),
    # лемур
    "joki-joya-oblaka": ("purple",
        f'<path d="M86 96 Q118 92 112 62 Q108 44 96 40" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round"/>'
        f'<path d="M86 96 Q118 92 112 62 Q108 44 96 40" fill="none" stroke="#3B3355" stroke-width="11" stroke-dasharray="6 7" stroke-linecap="butt" opacity=".85"/>'
        f'<ellipse cx="62" cy="88" rx="24" ry="22" fill="#B4B4C4" {s()}/>'
        f'<path d="M36 52 Q40 28 62 28 Q84 28 88 52 Q86 70 62 72 Q38 70 36 52Z" fill="#C8C8D6" {s()}/>'
        f'<path d="M40 34 L32 22 L46 28 M84 34 L92 22 L78 28" fill="#C8C8D6" {W(2.4)}/>'
        f'<circle cx="52" cy="50" r="9" fill="#3B3355"/><circle cx="72" cy="50" r="9" fill="#3B3355"/>'
        f'<circle cx="52" cy="50" r="5" fill="#FFD25E"/><circle cx="72" cy="50" r="5" fill="#FFD25E"/>'
        f'<circle cx="52" cy="50" r="2" fill="#3B3355"/><circle cx="72" cy="50" r="2" fill="#3B3355"/>'
        f'<path d="M58 62 Q62 66 66 62" fill="none" {W(2.4)}/>'),
    # домино
    "joki-joya-kuzminki": ("orange",
        "".join(f'<g transform="rotate({a} {x} 70)"><rect x="{x-14}" y="40" width="28" height="56" rx="6" fill="#fff" {s()}/>'
                f'<path d="M{x-14} 68 H{x+14}" {W(2.4)}/>'
                + "".join(f'<circle cx="{x+dx}" cy="{y}" r="3.4" fill="#3B3355"/>' for dx, y in d) + '</g>'
                for a, x, d in [(-14, 34, [(0, 54)]), (0, 64, [(-6, 50), (6, 60), (-6, 78), (6, 78), (0, 86)]),
                                (14, 94, [(-6, 50), (6, 60), (0, 84)])])
        + f(64, 106, d=6, k=0.45, blush=False) + sparkle(108, 26, 6)),
    # калейдоскоп
    "joki-joya-rio-leninsky": ("night",
        f'<rect x="12" y="56" width="62" height="24" rx="8" fill="#E8654F" {s()} transform="rotate(-20 43 68)"/>'
        f'<path d="M22 76 L66 60" stroke="#FFD25E" stroke-width="4" transform="rotate(0)"/>'
        + f(40, 70, d=6, k=0.45, blush=False)
        + f'<circle cx="92" cy="48" r="26" fill="#fff" {s()}/>'
        + "".join(f'<path d="M92 48 L{92+22*__import__("math").cos(a*0.5236):.1f} {48+22*__import__("math").sin(a*0.5236):.1f} '
                  f'L{92+22*__import__("math").cos((a+1)*0.5236):.1f} {48+22*__import__("math").sin((a+1)*0.5236):.1f}Z" fill="{c}"/>'
                  for a, c in zip(range(12), ["#E8654F", "#FFD25E", "#7CD26E", "#5CB7F2", "#A98BF0", "#FF7FA8"] * 2))
        + f'<circle cx="92" cy="48" r="26" fill="none" {s()}/><circle cx="92" cy="48" r="5" fill="#fff" {W(2)}/>'
        + sparkle(28, 30, 6)),
}

for pid, (bg, body) in I.items():
    open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
print(len(I))
