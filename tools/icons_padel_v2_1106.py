"""Падел v2 (06.11, Вадим: иконки должны характеризовать именно падел, околоспортивные не подходят).
В каждой иконке — узнаваемый элемент падела (ракетка с дырочками, мяч, корт со стеклянными стенами и сеткой),
а сцена/сюжет у каждого клуба свой. Корт сверху (Ходынка) и кубок с падел-ракеткой (Терехово) остаются."""
import math, os
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda x, y, d=6, k=0.5, **kw: face(x, y, d=d, k=k, **kw)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
BALL = "#D7F25A"


def ball(x, y, r=8, smile=False):
    b = (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{BALL}" {W(2.4)}/>'
         f'<path d="M{x-r*0.8:.1f} {y-r*0.3:.1f} Q{x} {y+r*0.5:.1f} {x+r*0.8:.1f} {y-r*0.3:.1f}" fill="none" stroke="#fff" stroke-width="2"/>')
    return b + (f(x, y + 1, d=r * 0.35, k=r / 28, blush=False) if smile else "")


def racket(x, y, rot=0, sc=1.0, col="#5CB7F2"):
    """падел-ракетка: сплошная лопасть с дырочками + короткая ручка с темляком"""
    holes = "".join(f'<circle cx="{hx}" cy="{hy}" r="2.6" fill="#fff"/>'
                    for hx, hy in [(-8, -14), (0, -16), (8, -14), (-10, -4), (0, -6), (10, -4), (-8, 6), (0, 4), (8, 6), (0, 14)])
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})">'
            f'<path d="M-18 -4 Q-18 -26 0 -26 Q18 -26 18 -4 Q18 18 6 24 H-6 Q-18 18 -18 -4Z" fill="{col}" {s()}/>'
            f'{holes}<rect x="-4" y="22" width="8" height="20" rx="3" fill="#3B3355"/>'
            f'<path d="M0 42 Q-6 50 0 54 Q6 50 0 42" fill="none" stroke="#3B3355" stroke-width="2"/></g>')


def court(x, y, w, h, glass="#DFF3FF"):
    """корт сбоку: стеклянные торцевые стены, сетка-ограда, сетка посередине"""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="#3E9BE0" {W(3)}/>'
            f'<rect x="{x}" y="{y-h*0.9:.0f}" width="{w*0.22:.0f}" height="{h*0.9:.0f}" fill="{glass}" fill-opacity=".85" {W(2.4)}/>'
            f'<rect x="{x+w*0.78:.0f}" y="{y-h*0.9:.0f}" width="{w*0.22:.0f}" height="{h*0.9:.0f}" fill="{glass}" fill-opacity=".85" {W(2.4)}/>'
            f'<path d="M{x+w*0.22:.0f} {y-h*0.5:.0f} H{x+w*0.78:.0f}" stroke="#9AA0B8" stroke-width="2" stroke-dasharray="3 3"/>'
            f'<path d="M{x+w/2:.0f} {y} V{y-h*0.35:.0f}" {W(3)}/>'
            f'<path d="M{x+w*0.3:.0f} {y-h*0.3:.0f} H{x+w*0.7:.0f}" stroke="#fff" stroke-width="3"/>')


S = {}  # id: (сюжет, фон, тело)
S["padlhub-yasenevo"] = ("ребёнок в прыжке бьёт «бандеху» падел-ракеткой", "orange",
    f'<circle cx="52" cy="36" r="13" fill="#FFD9B8" {s()}/>' + f(52, 37, d=4.5, k=0.42)
    + f'<path d="M52 49 V80 M52 80 L40 106 M52 80 L66 102 M52 58 L34 70 M52 58 L74 44" fill="none" {W(5)}/>'
    + racket(84, 32, rot=35, sc=0.75) + ball(108, 70, 8) + sparkle(24, 24, 6))
S["padlhub-nagatino"] = ("большая и маленькая детская падел-ракетки — мама и малыш", "pink",
    racket(46, 50, rot=-12, sc=1.1, col="#FF7FA8") + f(46, 46, d=6, k=0.5)
    + racket(94, 74, rot=14, sc=0.62, col="#FFD25E") + f(94, 71, d=3.6, k=0.32, blush=False)
    + ball(100, 26, 7) + sparkle(20, 108, 6))
S["padlhub-kuntsevo"] = ("две падел-ракетки крест-накрест — парная игра", "sky",
    racket(48, 54, rot=-28, sc=0.95, col="#5CB7F2") + racket(80, 54, rot=28, sc=0.95, col="#FF8A3D")
    + ball(64, 100, 9, smile=True) + sparkle(20, 22, 6) + sparkle(108, 22, 6))
S["padel-lunda-konstruktor"] = ("мяч отскакивает от стеклянной стены корта", "teal",
    f'<rect x="70" y="16" width="34" height="96" rx="4" fill="#DFF3FF" fill-opacity=".9" {s()}/>'
    f'<path d="M78 26 L92 40 M78 40 L86 48" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M14 98 Q40 40 68 54 Q44 70 30 104" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="5 5"/>'
    + ball(66, 54, 9, smile=True) + f'<path d="M14 112 H104" {W(4)}/>')
S["padel-lunda-rechnoy"] = ("сетка посередине падел-корта и мяч над ней", "green",
    f'<rect x="10" y="88" width="108" height="22" rx="4" fill="#3E9BE0" {W(3)}/>'
    f'<path d="M24 60 V96 M104 60 V96" {W(5)}/><rect x="24" y="60" width="80" height="22" fill="#fff" fill-opacity=".6" {W(3)}/>'
    + "".join(f'<path d="M{x} 60 V82" stroke="#9AA0B8" stroke-width="1.6"/>' for x in range(32, 104, 8))
    + f'<path d="M24 66 H104 M24 74 H104" stroke="#9AA0B8" stroke-width="1.6"/><path d="M24 60 H104" stroke="#fff" stroke-width="5"/>'
    + ball(64, 34, 9, smile=True) + sparkle(102, 22, 6))
S["padel-luzhniki-academy"] = ("падел-мяч крупно — талисман академии", "yellow",
    f'<circle cx="64" cy="64" r="40" fill="{BALL}" {s()}/>'
    f'<path d="M28 50 Q64 84 100 50 M30 82 Q64 52 98 82" fill="none" stroke="#fff" stroke-width="5"/>'
    + f(64, 66, d=11, k=0.8) + racket(104, 98, rot=40, sc=0.5) + sparkle(22, 22, 7))
S["padel-friends-luzhniki"] = ("двое друзей дают пять падел-ракетками", "purple",
    f'<circle cx="34" cy="64" r="11" fill="#FFD9B8" {s()}/>' + f(34, 65, d=4, k=0.38)
    + f'<circle cx="94" cy="64" r="11" fill="#FFD9B8" {s()}/>' + f(94, 65, d=4, k=0.38)
    + f'<path d="M34 75 V104 M94 75 V104" {W(5)}/>'
    + racket(52, 38, rot=30, sc=0.6, col="#FF8A3D") + racket(76, 38, rot=-30, sc=0.6, col="#5CB7F2")
    + f'<path d="M58 14 L64 6 L70 14 M64 22 V10" stroke="#FFD25E" stroke-width="3" stroke-linecap="round"/>')
S["padel-sky-afimall"] = ("падел-корт на крыше среди небоскрёбов Сити", "night",
    f'<path d="M16 72 V30 H30 V72 M36 72 V14 L46 6 L56 14 V72 M90 72 V22 H104 V72 M62 72 V36 H82 V72" fill="#5A5470" {W(2.6)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="4" height="4" fill="#FFD25E"/>' for x, y in [(20, 40), (42, 24), (48, 40), (94, 32), (68, 46), (96, 52)])
    + court(18, 110, 92, 26) + ball(98, 78, 6))
S["padel-tennisru-riviera"] = ("мяч в металлической сетке-ограде падел-корта", "blue",
    f'<rect x="16" y="16" width="96" height="96" rx="6" fill="#DCE3EE" {s()}/>'
    + "".join(f'<path d="M{16+i*12} 16 L{16+i*12-48} 112" stroke="#9AA0B8" stroke-width="2"/><path d="M{16+i*12-48} 16 L{16+i*12} 112" stroke="#9AA0B8" stroke-width="2"/>' for i in range(0, 13))
    + f'<rect x="16" y="16" width="96" height="96" rx="6" fill="none" {s()}/>' + ball(64, 64, 14, smile=True))
S["padel-first-club"] = ("неоновая вывеска PADEL с ракеткой", "night",
    f'<rect x="12" y="30" width="104" height="58" rx="12" fill="#2A2440" {s()}/>'
    f'<text x="64" y="70" text-anchor="middle" font-family="Arial Rounded MT Bold,Arial" font-weight="700" font-size="26" fill="#FF7FA8" stroke="#FFC6DA" stroke-width="1">PADEL</text>'
    + racket(100, 100, rot=-30, sc=0.5, col="#9AE6D8") + f'<path d="M40 30 V16 M88 30 V16" {W(3)}/>' + sparkle(20, 108, 6))
S["padel-park-belokamenny"] = ("крытый падел-корт под куполом-ангаром", "green",
    f'<path d="M10 104 Q10 30 64 26 Q118 30 118 104Z" fill="#fff" fill-opacity=".85" {s()}/>'
    f'<path d="M36 104 Q36 46 64 42 Q92 46 92 104" fill="none" stroke="#9AA0B8" stroke-width="2.4"/>'
    + court(26, 104, 76, 24) + ball(64, 54, 7, smile=True))
S["padel-rink-skolkovo"] = ("мяч вылетает из падел-корта через дверь — «пор трес»", "sky",
    court(10, 106, 84, 26)
    + f'<path d="M40 82 Q70 20 108 40" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="5 5"/>'
    + ball(108, 40, 9, smile=True) + f'<path d="M96 106 V80 H112 V106" fill="#fff" {W(2.6)}/>' + sparkle(20, 24, 6))
S["padel-pari"] = ("падел-ракетка с дырочками крупным планом", "purple",
    racket(64, 54, rot=-15, sc=1.6, col="#FF8A3D") + ball(104, 100, 8) + sparkle(22, 24, 7))
S["padel-korty-setki"] = ("банка падел-мячей с тремя мячами", "orange",
    f'<rect x="40" y="26" width="48" height="88" rx="10" fill="#fff" fill-opacity=".8" {s()}/>'
    f'<rect x="38" y="18" width="52" height="12" rx="5" fill="#5CB7F2" {W(3)}/>'
    + ball(64, 46, 11) + ball(64, 70, 11, smile=True) + ball(64, 94, 11)
    + f'<path d="M48 34 V104" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')
S["padel-buenos-skladochnaya"] = ("падел-ракетка с аргентинским солнцем", "yellow",
    f'<circle cx="64" cy="60" r="44" fill="#9ED3FF" {W(2)}/>'
    + "".join(f'<path d="M{64+30*math.cos(a):.1f} {48+30*math.sin(a):.1f} L{64+40*math.cos(a):.1f} {48+40*math.sin(a):.1f}" stroke="#FFC93C" stroke-width="4" stroke-linecap="round"/>' for a in [i * math.pi / 8 for i in range(16)])
    + f'<circle cx="64" cy="48" r="22" fill="#FFC93C" {W(3)}/>' + f(64, 49, d=7, k=0.6)
    + racket(64, 98, rot=0, sc=0.62, col="#fff"))
S["padel-buenos-vdnh"] = ("падел-корт у павильона со шпилем ВДНХ", "teal",
    f'<path d="M40 70 V44 H88 V70 M50 44 V30 H78 V44 M64 30 V8" fill="#FFE3A3" {W(3)}/><path d="M60 12 L64 4 L68 12Z" fill="#FFC93C" {W(2)}/>'
    + court(14, 112, 100, 28) + ball(98, 64, 6))
S["padel-vnukovo-sport"] = ("открытый падел-корт и самолёт над ним", "sky",
    f'<path d="M20 34 L74 22 L98 14 Q110 12 106 22 L84 34 L74 50 H64 L68 36 L40 42 L32 50 H24 L28 38Z" fill="#fff" {s()}/>'
    + court(12, 112, 104, 30) + ball(40, 64, 6, smile=True))
S["padel-zhukovka"] = ("падел-корт среди сосен", "green",
    "".join(f'<path d="M{x} {y} L{x-14} {y+30} H{x+14}Z M{x} {y+14} L{x-17} {y+44} H{x+17}Z" fill="#2E9E6A" {W(2.4)}/><path d="M{x} {y+44} V{y+54}" stroke="#8A5530" stroke-width="5"/>' for x, y in [(22, 12), (106, 14)])
    + court(20, 112, 88, 28) + ball(64, 52, 7, smile=True))
S["padel-berta-village"] = ("падел-корт у загородного озера", "yellow",
    f'<circle cx="98" cy="26" r="12" fill="#FFC93C" {W(2.4)}/><path d="M8 66 Q40 56 64 64 T120 64 V78 H8Z" fill="#5CB7F2" {W(2.4)}/>'
    + court(16, 114, 96, 28) + ball(36, 40, 6, smile=True))
S["padel-cooltennis-malevich"] = ("падел-корт в стиле супрематизма", "orange",
    f'<rect x="16" y="16" width="96" height="96" fill="#fff" {s()}/><rect x="26" y="30" width="42" height="42" fill="#3B3355" transform="rotate(-8 47 51)"/>'
    f'<rect x="64" y="58" width="40" height="12" fill="#E8554A" transform="rotate(20 84 64)"/><rect x="30" y="84" width="70" height="8" fill="#3E9BE0"/>'
    + racket(92, 34, rot=20, sc=0.5, col="#FFC93C") + ball(48, 98, 6))

if __name__ == "__main__":
    import re
    for pid, (subj, bg, body) in S.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    reg = os.path.join(out, "subjects.txt"); txt = open(reg).read()
    for pid, (subj, _, _) in S.items():
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    txt += "".join(f"{pid} — {subj}\n" for pid, (subj, _, _) in S.items())
    open(reg, "w").write(txt)
    print(len(S))
