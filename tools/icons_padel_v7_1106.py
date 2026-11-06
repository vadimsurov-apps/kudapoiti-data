"""Падел v7 (06.11): юмор только в контексте падела (Вадим: солнце над холмом, коньки, кораблик — не про падел;
мелкие непонятные детали убрать). Правки 5 иконок."""
import os, re
from draw_icons import svg, s, eye, face, sparkle, O
from icons_padel_v3_1106 import ball, paddle, BALL, W, out
from icons_padel_v4_1106 import ballchar
from icons_padel_v6_1106 import S as V6, kid

V7 = {
    "a-padel-khodynka": ("малыш в кепке с пропеллером прыгает со смэшем", "blue",
        kid(48, 40, "stand", "#FF8A3D").replace("", "")
        + f'<path d="M36 34 Q48 22 60 34Z" fill="#5CB7F2" {W(2.4)}/><path d="M48 26 V20 M42 19 H54" {W(2.4)}/>'
        + ball(104, 26, 8, smile=True)),
    "padel-rink-skolkovo": ("падел-мяч устал после долгого розыгрыша — повязка и капли пота", "sky",
        ballchar(62, 66, 32)
        + f'<path d="M32 50 Q62 36 92 50" fill="none" stroke="#E8554A" stroke-width="8" stroke-linecap="round"/>'
        + f'<path d="M98 44 q4 8 0 12 q-4 -4 0 -12Z M104 62 q4 8 0 12 q-4 -4 0 -12Z" fill="#9ED3FF" {W(1.6)}/>'
        + paddle("#FF8A3D", 24, 100, -30, 0.42)),
    "padel-berta-village": ("падел-мяч отскакивает от стеклянной стены корта", "green",
        f'<rect x="78" y="14" width="34" height="100" rx="5" fill="#DFF3FF" fill-opacity=".95" {s()}/>'
        f'<path d="M86 26 L100 40" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
        f'<path d="M14 104 Q40 40 72 58" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="6 6"/>'
        + ballchar(52, 64, 20, mood="open") + paddle("#5CB7F2", 22, 100, -20, 0.4)),
    "padel-lunda-rechnoy": ("падел-корт с сеткой прямо на палубе кораблика («Речной»)", "blue",
        f'<path d="M10 74 H118 L100 102 H28Z" fill="#FF8A3D" {s()}/><rect x="22" y="64" width="84" height="10" fill="#3E9BE0" {W(2.4)}/>'
        f'<path d="M64 64 V40" {W(4)}/><path d="M64 40 L64 26 L84 34Z" fill="#E8554A" {W(2)}/>'
        f'<rect x="40" y="48" width="48" height="16" fill="#fff" fill-opacity=".6" {W(2.4)}/>'
        + "".join(f'<path d="M{x} 48 V64" stroke="#9AA0B8" stroke-width="1.6"/>' for x in range(46, 88, 7))
        + ball(30, 40, 8, smile=True) + paddle("#5CB7F2", 102, 44, 25, 0.38)
        + f'<path d="M6 114 Q20 106 34 114 T62 114 T90 114 T118 114" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'),
}
V7["padel-luzhniki-academy"] = ("падел-мяч в шапочке выпускника", "green",
    ballchar(62, 70, 32) + f'<path d="M28 36 L62 22 L96 36 L62 50Z" fill="#3B3355" {W(2.6)}/><rect x="48" y="40" width="28" height="10" fill="#3B3355"/>'
    f'<path d="M94 36 V54" stroke="#FFC93C" stroke-width="3"/><circle cx="94" cy="56" r="3.5" fill="#FFC93C"/>')
_m = V6["padel-cooltennis-malevich"]
V7["padel-cooltennis-malevich"] = ("падел-ракетка-художник с палитрой", _m[1],
    paddle("#7CD26E", 56, 66)
    + f'<path d="M84 84 Q80 64 98 62 Q120 60 120 80 Q120 100 102 102 Q96 102 98 94 Q100 86 92 88 Q86 90 84 84Z" fill="#FFE3A3" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4.5" fill="{c}"/>' for x, y, c in [(98, 70, "#E8554A"), (110, 72, "#3E9BE0"), (112, 86, "#FFC93C"), (102, 92, "#3B3355")]))
S = {pid: V7.get(pid, v) for pid, v in V6.items()}

if __name__ == "__main__":
    for pid, (subj, bg, body) in V7.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    reg = os.path.join(out, "subjects.txt"); txt = open(reg).read()
    for pid in V7:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    txt += "".join(f"{pid} — {subj}\n" for pid, (subj, _, _) in V7.items())
    open(reg, "w").write(txt)
    print(len(V7))
