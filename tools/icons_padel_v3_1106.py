"""Падел v3 (06.11). Метод «Якорь + Характер + Шутка» (см. CLAUDE.md, раздел «Как рисовать иконки»):
ЯКОРЬ — канонический силуэт падел-ракетки (сплошная лопасть с дырочками, короткая ручка, темляк), крупно, по центру;
ХАРАКТЕР — у ракетки лицо; ШУТКА — один аксессуар по названию/месту клуба. Мяч — лаймовый."""
import math, os
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
BALL = "#D7F25A"


def ball(x, y, r=8, smile=False):
    b = (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{BALL}" {W(2.4)}/>'
         f'<path d="M{x-r*0.8:.1f} {y-r*0.3:.1f} Q{x} {y+r*0.5:.1f} {x+r*0.8:.1f} {y-r*0.3:.1f}" fill="none" stroke="#fff" stroke-width="2"/>')
    return b + (face(x, y + 1, d=r * 0.35, k=r / 26, blush=False) if smile else "")


def paddle(col="#5CB7F2", x=64, y=60, rot=0, sc=1.0, mood="smile"):
    """ЯКОРЬ: падел-ракетка с лицом. Лопасть ~ 56×64, дырочки по краю (лицо в центре свободно)."""
    holes = [(-16, -18), (-6, -24), (6, -24), (16, -18), (-22, -6), (22, -6), (-22, 6), (22, 6), (-14, 18), (14, 18), (0, 22)]
    h = "".join(f'<circle cx="{hx}" cy="{hy}" r="3.2" fill="#fff" fill-opacity=".95"/>' for hx, hy in holes)
    mouth = {"smile": 'M-7 6 Q0 12 7 6', "open": 'M-6 5 Q0 14 6 5 Z', "grin": 'M-9 4 Q0 14 9 4'}[mood]
    fc = (eye(-9, -4, 0.85) + eye(9, -4, 0.85)
          + f'<path d="{mouth}" fill="{"#E8554A" if mood == "open" else "none"}" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
          + '<ellipse cx="-17" cy="4" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="17" cy="4" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>')
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})">'
            f'<rect x="-6" y="28" width="12" height="26" rx="5" fill="#3B3355"/>'
            f'<path d="M0 54 Q-9 64 0 68 Q9 64 0 54" fill="none" stroke="#3B3355" stroke-width="2.6"/>'
            f'<path d="M-30 -2 Q-30 -36 0 -36 Q30 -36 30 -2 Q30 26 10 32 H-10 Q-30 26 -30 -2Z" fill="{col}" {s()}/>'
            f'{h}{fc}</g>')


# id: (сюжет, фон, тело)   — у всех ракетка-якорь крупно; шутка — по названию/месту
S = {
    "a-padel-khodynka": ("падел-ракетка в детской кепке с пропеллером", "blue",
        paddle("#FF8A3D", 62, 66, -6) + f'<path d="M38 34 Q62 14 86 34Z" fill="#5CB7F2" {W(3)}/><path d="M86 34 H98" {W(4)}/>'
        f'<path d="M62 22 V12 M50 10 H74" {W(3)}/>' + ball(104, 96, 8)),
    "padlhub-terekhovo": ("падел-ракетка-чемпион с короной", "yellow",
        paddle("#5CB7F2", 62, 68, 6) + f'<path d="M42 34 L46 16 L56 28 L64 12 L72 28 L82 16 L86 34Z" fill="#FFC93C" {W(3)}/>' + ball(24, 104, 8) + sparkle(106, 24, 7)),
    "padlhub-yasenevo": ("падел-ракетка в спортивной повязке в прыжке за мячом", "orange",
        paddle("#7CD26E", 58, 66, -18, mood="open") + f'<path d="M30 40 Q58 26 84 44" fill="none" stroke="#E8554A" stroke-width="7" stroke-linecap="round"/>'
        f'<path d="M84 44 L96 38 M84 44 L94 52" stroke="#E8554A" stroke-width="5" stroke-linecap="round"/>' + ball(104, 22, 9, smile=True)
        + f'<path d="M30 112 Q44 106 58 112" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'),
    "padlhub-nagatino": ("большая и маленькая падел-ракетки — мама и малыш", "pink",
        paddle("#FF7FA8", 50, 58, -10) + paddle("#FFD25E", 98, 82, 12, 0.5) + ball(104, 26, 7)),
    "padlhub-kuntsevo": ("две падел-ракетки крест-накрест — парная игра", "sky",
        paddle("#5CB7F2", 46, 60, -24, 0.78) + paddle("#FF8A3D", 82, 60, 24, 0.78) + ball(64, 108, 8, smile=True)),
    "padel-lunda-konstruktor": ("падел-ракетка в строительной каске («Конструктор»)", "teal",
        paddle("#5CB7F2", 64, 68) + f'<path d="M34 38 Q34 12 64 12 Q94 12 94 38Z" fill="#FFC93C" {W(3)}/><path d="M28 38 H100" {W(5)}/>'
        f'<path d="M64 12 V26" stroke="#E0A830" stroke-width="5"/>' + ball(106, 100, 8)),
    "padel-lunda-rechnoy": ("падел-ракетка в бескозырке у причала («Речной»)", "blue",
        paddle("#FF8A3D", 64, 68) + f'<ellipse cx="64" cy="34" rx="28" ry="8" fill="#fff" {W(3)}/><rect x="40" y="34" width="48" height="8" fill="#3B3355"/>'
        f'<path d="M86 40 L100 50 M86 42 L96 56" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
        f'<path d="M10 116 Q24 108 38 116 T66 116" fill="none" stroke="#fff" stroke-width="4"/>' + ball(22, 30, 7)),
    "padel-luzhniki-academy": ("падел-ракетка в академической шапочке выпускника", "green",
        paddle("#5CB7F2", 64, 68) + f'<path d="M30 30 L64 16 L98 30 L64 44Z" fill="#3B3355" {W(2.6)}/><rect x="50" y="34" width="28" height="10" fill="#3B3355"/>'
        f'<path d="M96 30 V48" stroke="#FFC93C" stroke-width="3"/><circle cx="96" cy="50" r="3.5" fill="#FFC93C"/>' + ball(22, 102, 8, smile=True)),
    "padel-friends-luzhniki": ("падел-ракетка и мяч — лучшие друзья, обнимаются", "purple",
        paddle("#FF8A3D", 54, 62, -8) + ball(96, 70, 16, smile=True)
        + f'<path d="M80 66 Q90 56 100 60" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>'
        + f'<path d="M102 30 Q96 22 102 18 Q108 22 102 30Z M108 36 Q114 30 118 34 Q114 40 108 36Z" fill="#FF5A8A"/>'),
    "padel-sky-afimall": ("падел-ракетка в тёмных очках на фоне небоскрёбов («Sky»)", "night",
        f'<path d="M8 120 V70 H20 V120 M100 120 V58 L110 50 L120 58 V120" fill="#5A5470" {W(2.4)}/>'
        + paddle("#9AE6D8", 62, 62)
        + f'<path d="M44 54 H80 M44 54 Q44 64 52 64 Q58 64 59 56 M65 56 Q66 64 72 64 Q80 64 80 54" fill="#3B3355" {W(3)}/>' + sparkle(104, 22, 7) + ball(24, 30, 6)),
    "padel-tennisru-riviera": ("падел-ракетка в соломенной шляпе на Ривьере", "yellow",
        paddle("#5CB7F2", 64, 70) + f'<ellipse cx="64" cy="38" rx="40" ry="9" fill="#FFE3A3" {W(3)}/><path d="M42 38 Q42 18 64 18 Q86 18 86 38" fill="#FFE3A3" {W(3)}/>'
        f'<path d="M42 32 H86" stroke="#E8554A" stroke-width="5"/>' + ball(108, 104, 8)),
    "padel-first-club": ("падел-ракетка с медалью «1»", "orange",
        paddle("#7CD26E", 58, 60) + f'<path d="M88 64 L96 84 M108 64 L100 84" stroke="#5CB7F2" stroke-width="5"/>'
        f'<circle cx="98" cy="96" r="14" fill="#FFC93C" {W(3)}/><text x="98" y="102" text-anchor="middle" font-family="Arial" font-weight="700" font-size="16" fill="#3B3355">1</text>'),
    "padel-park-belokamenny": ("падел-ракетка гуляет в парке с воздушным шариком", "green",
        paddle("#FF8A3D", 56, 66, -6) + f'<path d="M84 88 Q90 60 96 40" fill="none" {W(2)}/><ellipse cx="98" cy="28" rx="13" ry="16" fill="#FF5A6A" {W(3)}/>'
        f'<path d="M14 116 Q26 104 38 116" fill="#7CD26E" {W(2)}/>' + ball(22, 34, 7)),
    "padel-rink-skolkovo": ("падел-ракетка на коньках («The Rink»)", "sky",
        paddle("#5CB7F2", 64, 52, 0, 0.9)
        + f'<path d="M44 92 V104 H62 M84 92 V104 H66" fill="none" {W(3)}/><rect x="40" y="86" width="14" height="14" rx="3" fill="#fff" {W(2.6)}/>'
        f'<rect x="74" y="86" width="14" height="14" rx="3" fill="#fff" {W(2.6)}/><path d="M36 108 H60 M70 108 H94" stroke="#9AA0B8" stroke-width="4" stroke-linecap="round"/>' + ball(108, 30, 7)),
    "padel-pari": ("падел-ракетка в берете с багетом («Пари»)", "purple",
        paddle("#FF8A3D", 60, 68) + f'<ellipse cx="60" cy="34" rx="22" ry="9" fill="#E8554A" {W(3)}/><path d="M60 24 V18" {W(4)}/>'
        f'<path d="M92 50 L112 98" stroke="#E0A830" stroke-width="12" stroke-linecap="round"/><path d="M92 50 L112 98" stroke="{O}" stroke-width="2"/>'
        f'<path d="M98 62 l6 -3 M102 74 l6 -3 M106 86 l6 -3" stroke="#fff" stroke-width="2"/>'),
    "padel-korty-setki": ("падел-ракетка ловит мяч сачком («Сетки»)", "orange",
        paddle("#5CB7F2", 52, 70, -8) + f'<path d="M78 62 L104 26" {W(4)}/><circle cx="106" cy="22" r="14" fill="#fff" fill-opacity=".7" {W(2.6)}/>'
        f'<path d="M96 14 L116 30 M94 24 L112 36 M100 10 L118 22" stroke="#9AA0B8" stroke-width="1.6"/>' + ball(106, 22, 6, smile=True)),
    "padel-buenos-skladochnaya": ("падел-ракетка пьёт мате из калабасы («Buenos»)", "yellow",
        paddle("#5CB7F2", 56, 62, -6) + f'<path d="M86 84 Q84 110 100 110 Q116 110 114 84Z" fill="#A86F3E" {W(3)}/>'
        f'<path d="M106 84 L114 58" stroke="#C0C4D0" stroke-width="4" stroke-linecap="round"/><ellipse cx="100" cy="84" rx="14" ry="4" fill="#7CD26E" {W(2)}/>'
        + sparkle(24, 24, 7)),
    "padel-buenos-vdnh": ("падел-ракетка с мороженым-рожком на ВДНХ", "teal",
        paddle("#FF7FA8", 56, 64, -4) + f'<path d="M90 70 L100 108 L110 70Z" fill="#E0A830" {W(3)}/>'
        f'<circle cx="100" cy="62" r="12" fill="#fff" {W(3)}/><circle cx="96" cy="52" r="3" fill="#FF7FA8"/>' + ball(22, 104, 7)),
    "padel-vnukovo-sport": ("падел-ракетка-пилот в шлеме и очках («Внуково»)", "sky",
        paddle("#FF8A3D", 64, 68) + f'<path d="M34 42 Q34 14 64 14 Q94 14 94 42Z" fill="#A86F3E" {W(3)}/>'
        f'<circle cx="52" cy="38" r="8" fill="#9ED3FF" {W(2.6)}/><circle cx="76" cy="38" r="8" fill="#9ED3FF" {W(2.6)}/><path d="M60 38 H68" {W(2.6)}/>'
        f'<path d="M94 40 Q112 46 118 60" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>' + ball(20, 102, 7)),
    "padel-zhukovka": ("падел-ракетка с жемчужным ожерельем и бантом («Рублёвка»)", "pink",
        paddle("#9AE6D8", 64, 60) + "".join(f'<circle cx="{64+24*math.cos(a):.1f}" cy="{96+8*math.sin(a):.1f}" r="4" fill="#fff" {W(1.6)}/>' for a in [i * math.pi / 6 for i in range(7)])
        + f'<path d="M64 26 L48 16 V36Z M64 26 L80 16 V36Z" fill="#FF5A8A" {W(2.6)}/><circle cx="64" cy="26" r="4" fill="#FF5A8A" {W(2)}/>' + sparkle(108, 30, 7)),
    "padel-berta-village": ("падел-ракетка в соломенной шляпе с колоском («деревня»)", "green",
        paddle("#FF8A3D", 62, 68) + f'<path d="M30 40 Q62 30 94 40 Q86 22 62 20 Q38 22 30 40Z" fill="#FFE3A3" {W(3)}/>'
        f'<path d="M100 104 Q96 70 104 44" fill="none" stroke="#E0A830" stroke-width="3"/>'
        + "".join(f'<ellipse cx="{102+(i%2)*6-3}" cy="{50+i*7}" rx="3" ry="5" fill="#FFC93C" {W(1.4)}/>' for i in range(4)) + ball(22, 104, 7)),
    "padel-cooltennis-malevich": ("падел-ракетка-художник в берете с супрематическими квадратами", "orange",
        paddle("#fff", 60, 66) + f'<rect x="40" y="70" width="12" height="12" fill="#3B3355" transform="rotate(-10 46 76)"/>'
        f'<rect x="66" y="72" width="16" height="6" fill="#E8554A" transform="rotate(14 74 75)"/>'
        f'<ellipse cx="60" cy="32" rx="22" ry="8" fill="#3B3355" {W(2)}/><path d="M60 24 V18" {W(4)}/>'
        f'<path d="M96 104 L112 72" stroke="#A86F3E" stroke-width="5" stroke-linecap="round"/><path d="M110 68 L116 60" stroke="#3E9BE0" stroke-width="7" stroke-linecap="round"/>'),
}

if __name__ == "__main__":
    import re
    for pid, (subj, bg, body) in S.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    reg = os.path.join(out, "subjects.txt"); txt = open(reg).read()
    for pid in S:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    txt += "".join(f"{pid} — {subj}\n" for pid, (subj, _, _) in S.items())
    open(reg, "w").write(txt)
    print(len(S))
