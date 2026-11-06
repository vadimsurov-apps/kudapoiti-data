"""Падел v4 (06.11, Вадим: «ракетки супер, но добавь разнообразия — интересно разглядывать все иконки темы»).
Ракетка-персонаж остаётся у половины клубов (v3). У остальных — другие якоря падела:
мяч-персонаж, игрок в прыжке с ракеткой, сетка/корт со стеклянными стенами. Шутка по названию — как была."""
import os, re
from draw_icons import svg, s, eye, face, sparkle, O
from icons_padel_v3_1106 import S as V3, ball, paddle, BALL, W, out


def ballchar(x=64, y=66, r=30, mood="smile"):
    """мяч-персонаж: лаймовый мяч с белым швом и лицом"""
    m = {"smile": f"M{x-7} {y+8} Q{x} {y+15} {x+7} {y+8}", "open": f"M{x-7} {y+7} Q{x} {y+18} {x+7} {y+7}Z"}[mood]
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{BALL}" {s()}/>'
            f'<path d="M{x-r*0.92:.0f} {y-r*0.35:.0f} Q{x} {y+r*0.45:.0f} {x+r*0.92:.0f} {y-r*0.35:.0f}" fill="none" stroke="#fff" stroke-width="5" opacity=".9"/>'
            + eye(x - 10, y, 0.9) + eye(x + 10, y, 0.9)
            + f'<path d="{m}" fill="{"#E8554A" if mood == "open" else "none"}" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
            + f'<ellipse cx="{x-19}" cy="{y+8}" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/><ellipse cx="{x+19}" cy="{y+8}" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/>')


def kid(x, y, shirt="#FF7A8A", cap=""):
    """игрок в прыжке: тело-«звёздочка», рука с ракеткой вверх"""
    return (f'<path d="M{x} {y+14} V{y+40} M{x} {y+40} L{x-14} {y+62} M{x} {y+40} L{x+12} {y+60} M{x} {y+22} L{x-18} {y+30}" fill="none" {W(5)}/>'
            f'<path d="M{x-9} {y+16} H{x+9} L{x+7} {y+40} H{x-7}Z" fill="{shirt}" {W(2.6)}/>'
            f'<circle cx="{x}" cy="{y}" r="13" fill="#FFD9B8" {s()}/>' + face(x, y + 1, d=4.5, k=0.42) + cap
            + f'<path d="M{x+6} {y+20} L{x+22} {y+4}" {W(5)}/>' + paddle("#5CB7F2", x + 32, y - 12, 40, 0.55))


def glass_court(y=112, h=34):
    return (f'<rect x="10" y="{y-6}" width="108" height="8" rx="3" fill="#3E9BE0" {W(2.6)}/>'
            f'<rect x="12" y="{y-h}" width="26" height="{h-6}" fill="#DFF3FF" fill-opacity=".9" {W(2.4)}/>'
            f'<rect x="90" y="{y-h}" width="26" height="{h-6}" fill="#DFF3FF" fill-opacity=".9" {W(2.4)}/>'
            f'<path d="M64 {y-6} V{y-h*0.55:.0f}" {W(3)}/><path d="M44 {y-h*0.5:.0f} H84" stroke="#fff" stroke-width="3"/>')


V4 = {
    "a-padel-khodynka": ("малыш в кепке с пропеллером прыгает с падел-ракеткой", "blue",
        kid(48, 40, "#FF8A3D", cap=f'<path d="M36 34 Q48 22 60 34Z" fill="#5CB7F2" {W(2.4)}/><path d="M48 26 V20 M42 19 H54" {W(2.4)}/>')
        + ball(106, 24, 8, smile=True) + glass_court(124, 14)),
    "padlhub-yasenevo": ("девочка с хвостиками бьёт смэш падел-ракеткой", "orange",
        kid(46, 42, "#7CD26E", cap=f'<path d="M34 36 Q26 34 26 46 M58 36 Q66 34 66 46" fill="none" stroke="#A86F3E" stroke-width="5" stroke-linecap="round"/>')
        + ball(104, 22, 9) + f'<path d="M96 30 L84 40 M100 34 L92 44" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' + sparkle(22, 108, 6)),
    "padel-luzhniki-academy": ("падел-мяч в шапочке выпускника с дипломом", "green",
        ballchar(62, 70, 32) + f'<path d="M28 36 L62 22 L96 36 L62 50Z" fill="#3B3355" {W(2.6)}/><rect x="48" y="40" width="28" height="10" fill="#3B3355"/>'
        f'<path d="M94 36 V54" stroke="#FFC93C" stroke-width="3"/><circle cx="94" cy="56" r="3.5" fill="#FFC93C"/>'
        f'<rect x="96" y="84" width="22" height="12" rx="6" fill="#fff" {W(2.4)}/><path d="M104 84 V96" stroke="#E8554A" stroke-width="3"/>'),
    "padel-lunda-rechnoy": ("падел-мяч в бескозырке плывёт по корту, как по реке", "blue",
        glass_court(116, 40) + ballchar(64, 64, 24)
        + f'<ellipse cx="64" cy="42" rx="20" ry="6" fill="#fff" {W(2.6)}/><rect x="48" y="42" width="32" height="6" fill="#3B3355"/>'
        f'<path d="M82 46 L92 54" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
        f'<path d="M30 96 Q44 90 58 96 T86 96 T110 96" fill="none" stroke="#fff" stroke-width="3"/>'),
    "padel-korty-setki": ("падел-мяч запутался в сетке корта и смеётся", "orange",
        f'<path d="M14 70 V108 M114 70 V108" {W(6)}/><rect x="14" y="58" width="100" height="40" fill="#fff" fill-opacity=".5" {W(3)}/>'
        + ballchar(64, 74, 22, mood="open")
        + "".join(f'<path d="M{x} 58 V98" stroke="#5A5470" stroke-width="1.8" opacity=".8"/>' for x in range(22, 114, 10))
        + "".join(f'<path d="M14 {y} H114" stroke="#5A5470" stroke-width="1.8" opacity=".8"/>' for y in range(66, 98, 10))
        + f'<path d="M14 58 H114" stroke="#fff" stroke-width="6"/><path d="M14 58 H114" {W(1.6)}/>' + paddle("#5CB7F2", 100, 28, 30, 0.42)),
    "padel-rink-skolkovo": ("падел-мяч катается на коньках («The Rink»)", "sky",
        ballchar(64, 54, 28) + f'<path d="M48 82 V96 H66 M80 82 V96 H62" fill="none" {W(3)}/>'
        f'<rect x="42" y="78" width="14" height="14" rx="3" fill="#fff" {W(2.6)}/><rect x="72" y="78" width="14" height="14" rx="3" fill="#fff" {W(2.6)}/>'
        f'<path d="M38 102 H62 M66 102 H90" stroke="#9AA0B8" stroke-width="4" stroke-linecap="round"/>'
        f'<path d="M14 116 Q40 108 64 116 T114 116" fill="none" stroke="#fff" stroke-width="3"/>' + paddle("#FF8A3D", 104, 34, 25, 0.4)),
    "padel-buenos-vdnh": ("падел-мяч — шарик мороженого в вафельном рожке (ВДНХ)", "teal",
        f'<path d="M40 70 L64 120 L88 70Z" fill="#E0A830" {s()}/><path d="M46 80 L82 80 M52 94 L76 94 M56 70 L74 104 M72 70 L54 104" stroke="#C08A20" stroke-width="2"/>'
        + ballchar(64, 52, 28) + f'<circle cx="58" cy="26" r="4" fill="#FF5A6A" {W(1.6)}/>' + paddle("#FF7FA8", 104, 40, 30, 0.42)),
    "padel-vnukovo-sport": ("падел-мяч с крыльями и в лётных очках летит над кортом («Внуково»)", "sky",
        glass_court(118, 30)
        + f'<path d="M36 58 Q14 40 10 50 Q18 64 38 66Z M92 58 Q114 40 118 50 Q110 64 90 66Z" fill="#fff" {s()}/>'
        + ballchar(64, 58, 26)
        + f'<path d="M40 48 Q64 36 88 48" fill="none" stroke="#A86F3E" stroke-width="5"/><circle cx="54" cy="50" r="7" fill="#9ED3FF" {W(2.4)}/><circle cx="74" cy="50" r="7" fill="#9ED3FF" {W(2.4)}/>'),
    "padel-berta-village": ("падел-корт в поле, на сетке сидит мяч в соломенной шляпе", "yellow",
        f'<circle cx="104" cy="22" r="11" fill="#FFC93C" {W(2.4)}/><path d="M6 80 Q40 68 64 76 T122 74 V122 H6Z" fill="#9BD86A" {W(2)}/>'
        + glass_court(118, 40) + ballchar(64, 60, 18)
        + f'<path d="M42 50 Q64 40 86 50 Q80 38 64 38 Q48 38 42 50Z" fill="#FFE3A3" {W(2.4)}/>'
        + "".join(f'<path d="M{x} 92 Q{x+2} 80 {x+4} 74" fill="none" stroke="#E0A830" stroke-width="2.4"/>' for x in (16, 22, 104, 110))),
    "padel-sky-afimall": V3["padel-sky-afimall"],
}
# у остальных — ракетка-персонаж из v3
S = {pid: V4.get(pid, v) for pid, v in V3.items()}

if __name__ == "__main__":
    for pid, (subj, bg, body) in S.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    reg = os.path.join(out, "subjects.txt"); txt = open(reg).read()
    for pid in S:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    txt += "".join(f"{pid} — {subj}\n" for pid, (subj, _, _) in S.items())
    open(reg, "w").write(txt)
    print(len(S), "из них новых якорей:", sum(1 for k in V4 if V4[k] is not V3.get(k)))
