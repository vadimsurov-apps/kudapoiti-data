"""Падел v6 (06.11): больше разнообразия и понятности. Ракетка-персонаж — только у тех, что Вадим одобрил;
остальные — мяч-персонаж с понятной эмоцией/действием или ребёнок в РАЗНЫХ позах. Никаких мелких непонятных деталей."""
import os, re
from draw_icons import svg, s, eye, face, sparkle, O
from icons_padel_v3_1106 import ball, paddle, BALL, W, out
from icons_padel_v4_1106 import ballchar
from icons_padel_v5_1106 import S as V5


def kid(x, y, pose, shirt="#FF7A8A", hair=None):
    """ребёнок-игрок в разных позах: smash, lunge, glide, serve, stand"""
    head = f'<circle cx="{x}" cy="{y}" r="13" fill="#FFD9B8" {s()}/>' + face(x, y + 1, d=4.5, k=0.42)
    if hair == "tails":
        head = f'<path d="M{x-12} {y-4} Q{x-24} {y} {x-22} {y+12} M{x+12} {y-4} Q{x+24} {y} {x+22} {y+12}" fill="none" stroke="#A86F3E" stroke-width="5" stroke-linecap="round"/>' + head
    if hair == "beret":
        head += f'<ellipse cx="{x}" cy="{y-11}" rx="13" ry="5" fill="#E8554A" {W(2.2)}/>'
    P = {  # тело (линии), ракетка (x, y, rot)
        "lunge": (f'M{x} {y+13} L{x+10} {y+40} M{x+10} {y+40} L{x+34} {y+56} M{x+10} {y+40} L{x-14} {y+62} M{x+4} {y+22} L{x-16} {y+16} M{x+4} {y+22} L{x+26} {y+30}',
                  (x + 44, y + 34, 70), f'M{x-4} {y+14} L{x+10} {y+16} L{x+14} {y+40} L{x+4} {y+40}Z'),
        "glide": (f'M{x} {y+13} V{y+40} M{x} {y+40} L{x-4} {y+64} M{x} {y+40} L{x+30} {y+52} M{x} {y+22} L{x-22} {y+14} M{x} {y+22} L{x+20} {y+30}',
                  (x + 34, y + 20, 30), None),
        "serve": (f'M{x} {y+13} V{y+40} M{x} {y+40} L{x-12} {y+62} M{x} {y+40} L{x+12} {y+62} M{x} {y+22} L{x-16} {y+8} M{x} {y+22} L{x+20} {y+38}',
                  (x + 30, y + 50, 110), None),
        "stand": (f'M{x} {y+13} V{y+40} M{x} {y+40} L{x-10} {y+62} M{x} {y+40} L{x+10} {y+62} M{x} {y+22} L{x-18} {y+32} M{x} {y+22} L{x+18} {y+10}',
                  (x + 26, y - 10, 20), None),
    }[pose]
    body, (rx, ry, rr), _ = P
    torso = f'<path d="M{x-9} {y+15} H{x+9} L{x+7} {y+40} H{x-7}Z" fill="{shirt}" {W(2.6)}/>'
    skates = ""
    if pose == "glide":
        skates = (f'<path d="M{x-12} {y+66} H{x+6} M{x+22} {y+58} L{x+40} {y+50}" stroke="#9AA0B8" stroke-width="4" stroke-linecap="round"/>')
    return (f'<path d="{body}" fill="none" {W(5)}/>' + torso + head + skates
            + paddle("#5CB7F2", rx, ry, rr, 0.5))


V6 = {
    "padlhub-yasenevo": ("девочка с хвостиками в выпаде дотягивается ракеткой до мяча", "orange",
        kid(46, 34, "lunge", "#7CD26E", "tails") + ball(108, 92, 9, smile=True)
        + f'<path d="M14 112 H114" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".7"/>'),
    "padel-lunda-konstruktor": ("ракетка отбивает мяч — «БАМ!» звёздочка удара", "teal",
        f'<path d="M78 40 L84 22 L90 40 L108 34 L96 48 L112 58 L94 60 L98 78 L86 66 L76 80 L74 62 L58 64 L70 52 L58 40Z" fill="#FFC93C" {W(2.6)}/>'
        + ballchar(84, 52, 20, mood="open") + paddle("#5CB7F2", 42, 76, -40, 0.85)),
    "padel-rink-skolkovo": ("малыш скользит на коньках с падел-ракеткой («The Rink»)", "sky",
        kid(46, 30, "glide", "#3E9BE0")
        + f'<path d="M10 108 Q64 98 118 108" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
        + ball(100, 24, 8, smile=True) + sparkle(110, 74, 6)),
    "padel-pari": ("малыш в берете подаёт мяч снизу («Пари»)", "purple",
        kid(46, 30, "serve", "#FF8A3D", "beret") + ball(82, 82, 9, smile=True)
        + f'<path d="M82 64 V70" stroke="#fff" stroke-width="3" stroke-dasharray="2 3"/>' + sparkle(104, 26, 6)),
    "padel-buenos-skladochnaya": ("падел-мяч влюбился в ракетку — глаза-сердечки («Buenos»)", "yellow",
        f'<circle cx="58" cy="62" r="34" fill="{BALL}" {s()}/>'
        f'<path d="M26 50 Q58 90 90 50" fill="none" stroke="#fff" stroke-width="5" opacity=".9"/>'
        + "".join(f'<path d="M{cx} {58} q-6 -8 -12 -2 q-4 6 12 16 q16 -10 12 -16 q-6 -6 -12 2Z" fill="#E8554A" {W(1.6)}/>' for cx in (46, 70))
        + f'<path d="M48 76 Q58 84 68 76" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
        + paddle("#5CB7F2", 104, 92, 20, 0.45)
        + f'<path d="M96 30 q-4 -6 -8 -1 q-3 4 8 11 q11 -7 8 -11 q-4 -5 -8 1Z" fill="#FF5A8A"/>'),
    "padel-vnukovo-sport": ("падел-мяч летит, как комета, хвост из полосок («Внуково»)", "sky",
        f'<path d="M14 98 L60 66 M10 80 L56 58 M24 112 L66 76" stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".85"/>'
        + ballchar(80, 50, 26, mood="open") + sparkle(26, 30, 6) + sparkle(110, 100, 5)),
    "padel-berta-village": ("падел-мяч восходит, как солнышко, над холмом («деревня»)", "sky",
        f'<path d="M4 96 Q40 70 70 86 Q96 74 124 88 V124 H4Z" fill="#7CD26E" {W(2.4)}/>'
        + "".join(f'<path d="M64 52 L{64+44*__import__("math").cos(a):.1f} {52+44*__import__("math").sin(a):.1f}" stroke="#FFC93C" stroke-width="5" stroke-linecap="round"/>'
                  for a in [i * 0.5236 - 3.1416 for i in range(7)])
        + ballchar(64, 58, 24) + paddle("#FF8A3D", 104, 100, 20, 0.36)),
}
S = {pid: V6.get(pid, v) for pid, v in V5.items()}

if __name__ == "__main__":
    for pid, (subj, bg, body) in V6.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    reg = os.path.join(out, "subjects.txt"); txt = open(reg).read()
    for pid in V6:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    txt += "".join(f"{pid} — {subj}\n" for pid, (subj, _, _) in V6.items())
    open(reg, "w").write(txt)
    print(len(V6))
