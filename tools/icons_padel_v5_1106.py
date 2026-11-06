"""Падел v5 (06.11): Вадим зачеркнул 9 иконок v4. Понравились простые, «читаемые с одного взгляда» сцены
(малыш в прыжке, корона, шапка выпускника, шарик, мама-малыш, обнимашки, очки Sky, мяч в сетке, медаль, жемчуг).
Не понравились: корт фоном (каша из линий), непонятные аксессуары (багет-лестница, мате, каска), белая ракетка,
мяч-мороженое/мяч с крыльями. Две сцены «мяч на ракетке» не повторять. Перерисованы 9 — одна понятная шутка, без корта на фоне."""
import os, re
from draw_icons import svg, s, eye, face, sparkle, O
from icons_padel_v3_1106 import ball, paddle, BALL, W, out
from icons_padel_v4_1106 import S as V4, ballchar

V5 = {
    "padel-lunda-konstruktor": ("падел-ракетка балансирует мячом на макушке", "teal",
        paddle("#5CB7F2", 64, 74) + ball(64, 22, 11, smile=True)
        + f'<path d="M50 30 Q46 26 48 20 M78 30 Q82 26 80 20" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' + sparkle(104, 40, 6)),
    "padel-lunda-rechnoy": ("падел-ракетка плывёт в бумажном кораблике по реке", "blue",
        paddle("#FF8A3D", 64, 50, 0, 0.82)
        + f'<path d="M22 88 H106 L92 106 H36Z" fill="#fff" {s()}/><path d="M64 88 L80 70 L64 72Z" fill="#fff" {W(2.4)}/>'
        + f'<path d="M8 112 Q22 104 36 112 T64 112 T92 112 T120 112" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'),
    "padel-rink-skolkovo": ("падел-ракетка в полосатой вязаной шапке с помпоном («The Rink»)", "sky",
        paddle("#FF8A3D", 64, 70)
        + f'<path d="M36 44 Q36 16 64 16 Q92 16 92 44Z" fill="#3E9BE0" {W(3)}/>'
        + f'<path d="M38 34 H90 M40 26 H88" stroke="#fff" stroke-width="4"/><rect x="34" y="40" width="60" height="9" rx="4" fill="#3E9BE0" {W(2.6)}/>'
        + f'<circle cx="64" cy="12" r="7" fill="#fff" {W(2.4)}/>' + sparkle(18, 30, 5) + sparkle(108, 96, 6) + sparkle(20, 96, 4)),
    "padel-vnukovo-sport": ("падел-ракетка в лётных очках, рядом бумажный самолётик", "sky",
        paddle("#FF8A3D", 58, 70)
        + f'<path d="M30 44 Q58 30 86 44" fill="none" stroke="#A86F3E" stroke-width="6"/>'
        + f'<circle cx="46" cy="44" r="9" fill="#9ED3FF" {W(3)}/><circle cx="70" cy="44" r="9" fill="#9ED3FF" {W(3)}/><path d="M55 44 H61" {W(3)}/>'
        + f'<path d="M86 30 L120 16 L104 44 L98 34Z" fill="#fff" {s()}/><path d="M98 34 L120 16" {W(2)}/>'
        + f'<path d="M84 34 Q74 40 78 50" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 4"/>'),
    "padel-pari": ("падел-ракетка и маленькая Эйфелева башня («Пари»)", "purple",
        paddle("#FF8A3D", 52, 68)
        + f'<path d="M100 18 L92 64 H108Z" fill="#9AA0B8" {W(2.6)}/><path d="M86 108 L96 64 H104 L114 108 H106 Q100 92 94 108Z" fill="#9AA0B8" {W(2.6)}/>'
        + f'<path d="M94 50 H106 M90 76 H110" {W(3)}/>' + sparkle(108, 14, 5) + ball(24, 26, 7)),
    "padel-berta-village": ("падел-ракетка с подсолнухом («деревня»)", "green",
        paddle("#5CB7F2", 58, 70)
        + f'<path d="M100 112 Q96 80 100 56" fill="none" stroke="#5CB04F" stroke-width="5"/><path d="M98 88 Q86 82 84 90 Q92 96 98 92Z" fill="#7CD26E" {W(2)}/>'
        + "".join(f'<ellipse cx="100" cy="36" rx="5" ry="12" fill="#FFC93C" {W(1.8)} transform="rotate({a} 100 50)"/>' for a in range(0, 360, 40))
        + f'<circle cx="100" cy="50" r="10" fill="#8A5530" {W(2.4)}/>' + ball(22, 26, 7)),
    "padel-cooltennis-malevich": ("падел-ракетка-художник с палитрой и кистью", "orange",
        paddle("#7CD26E", 56, 66)
        + f'<path d="M84 84 Q80 64 98 62 Q120 60 120 80 Q120 100 102 102 Q96 102 98 94 Q100 86 92 88 Q86 90 84 84Z" fill="#FFE3A3" {s()}/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}"/>' for x, y, c in [(98, 70, "#E8554A"), (110, 72, "#3E9BE0"), (112, 86, "#FFC93C"), (102, 92, "#3B3355")])
        + f'<path d="M22 108 L44 82" stroke="#A86F3E" stroke-width="5" stroke-linecap="round"/><path d="M44 82 L50 74" stroke="#E8554A" stroke-width="8" stroke-linecap="round"/>'),
    "padel-buenos-skladochnaya": ("падел-мяч танцует танго с розой в зубах («Buenos»)", "yellow",
        ballchar(60, 66, 30)
        + f'<path d="M72 80 L96 70" stroke="#5CB04F" stroke-width="4" stroke-linecap="round"/><circle cx="100" cy="68" r="10" fill="#E8554A" {W(2.6)}/>'
        + f'<path d="M96 64 Q100 70 104 64" fill="none" stroke="#B03A30" stroke-width="2"/>'
        + f'<path d="M14 34 Q20 26 26 34 M104 104 Q110 96 116 104" fill="none" {W(2.4)}/>' + paddle("#5CB7F2", 30, 104, -30, 0.4)),
    "padel-buenos-vdnh": ("малыш с падел-ракеткой и мороженым на ВДНХ", "teal",
        __import__("icons_padel_v4_1106").kid(52, 44, "#FFC93C")
        + f'<path d="M30 76 L22 96 L14 76Z" fill="#E0A830" {W(2.4)}/><circle cx="22" cy="72" r="7" fill="#FF7FA8" {W(2.4)}/>'
        + ball(106, 100, 8, smile=True) + sparkle(108, 60, 5)),
}
S = {pid: V5.get(pid, v) for pid, v in V4.items()}

if __name__ == "__main__":
    for pid, (subj, bg, body) in V5.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    reg = os.path.join(out, "subjects.txt"); txt = open(reg).read()
    for pid in V5:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    txt += "".join(f"{pid} — {subj}\n" for pid, (subj, _, _) in V5.items())
    open(reg, "w").write(txt)
    print(len(V5))
