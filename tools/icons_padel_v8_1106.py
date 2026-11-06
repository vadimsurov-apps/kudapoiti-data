"""Падел v8 (06.11): Вадим зачеркнул «БАМ», корабль с кортом и стеклянную стену. Три простые сцены без мелочей."""
import os, re
from draw_icons import svg, s, eye, face, sparkle, O
from icons_padel_v3_1106 import ball, paddle, BALL, W, out
from icons_padel_v4_1106 import ballchar
from icons_padel_v7_1106 import S as V7

V8 = {
    "padel-lunda-konstruktor": ("падел-ракетка подмигивает", "teal",
        f'<g>{paddle("#5CB7F2", 64, 62)}</g>'
        .replace(eye(9, -4, 0.85), f'<path d="M3 -4 Q9 -9 15 -4" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>')
        + ball(108, 98, 9) + sparkle(22, 26, 7)),
    "padel-lunda-rechnoy": ("падел-мяч в бескозырке («Речной»)", "blue",
        ballchar(64, 70, 34)
        + f'<ellipse cx="64" cy="38" rx="30" ry="9" fill="#fff" {s()}/><rect x="40" y="38" width="48" height="9" fill="#3B3355"/>'
        + f'<path d="M86 44 L100 58 M88 46 L96 64" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/>'),
    "padel-berta-village": ("падел-мячики-близнецы обнимаются", "green",
        ballchar(44, 70, 26) + ballchar(86, 70, 26)
        + f'<path d="M58 30 q-4 -6 -8 -1 q-3 4 8 11 q11 -7 8 -11 q-4 -5 -8 1Z" fill="#FF5A8A" transform="translate(7 0)"/>'
        + sparkle(18, 28, 6) + sparkle(110, 30, 6)),
}
S = {pid: V8.get(pid, v) for pid, v in V7.items()}

if __name__ == "__main__":
    for pid, (subj, bg, body) in V8.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    reg = os.path.join(out, "subjects.txt"); txt = open(reg).read()
    for pid in V8:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    txt += "".join(f"{pid} — {subj}\n" for pid, (subj, _, _) in V8.items())
    open(reg, "w").write(txt)
    print(len(V8))
