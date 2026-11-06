"""Замечания Вадима из бота (06.11 вечер): «Китёнок» (Жулебино) и Ломаковский музей — непонятные иконки."""
import os, re
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")

# Китёнок: малыш плывёт кролем по дорожке, из шапочки бьёт фонтанчик, как у китёнка
kit = (f'<rect x="0" y="66" width="128" height="62" fill="#3E9BE0"/>'
       + "".join(f'<circle cx="{x}" cy="104" r="5" fill="{c}" {W(1.8)}/>' for x, c in zip(range(6, 128, 13), ["#E8554A", "#fff"] * 6))
       + f'<path d="M0 66 Q16 58 32 66 T64 66 T96 66 T128 66" fill="#9ED3FF" {W(2.6)}/>'
       + f'<path d="M78 70 Q92 40 104 50" fill="none" stroke="#FFD9B8" stroke-width="9" stroke-linecap="round"/><path d="M78 70 Q92 40 104 50" fill="none" {W(2.4)} stroke-dasharray="0"/>'
       + f'<circle cx="56" cy="62" r="20" fill="#FFD9B8" {s()}/>'
       + f'<path d="M36 58 Q36 38 56 38 Q76 38 76 58Z" fill="#FF5A8A" {s()}/>'
       + f'<rect x="38" y="54" width="36" height="9" rx="4.5" fill="#3B3355"/><circle cx="47" cy="58.5" r="5" fill="#9ED3FF" {W(2)}/><circle cx="65" cy="58.5" r="5" fill="#9ED3FF" {W(2)}/>'
       + f'<path d="M50 70 Q56 75 62 70" fill="none" {W(2.4)}/><ellipse cx="42" cy="68" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="70" cy="68" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>'
       + f'<path d="M56 36 V22 M56 24 Q46 8 36 18 M56 24 Q66 8 76 18" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
       + f'<path d="M56 36 V22 M56 24 Q46 8 36 18 M56 24 Q66 8 76 18" fill="none" stroke="#6CC0F2" stroke-width="2" stroke-linecap="round"/>'
       + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff"/>' for x, y in [(34, 22), (78, 22), (30, 30), (82, 30)]))

# Ломаковка: старинный автомобиль-персонаж: высокая кабина, спицы, фары-глаза, клаксон-груша
def wheel(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="15" fill="#3B3355" {s()}/><circle cx="{x}" cy="{y}" r="9" fill="#FFE3A3" {W(2)}/>'
            + "".join(f'<path d="M{x} {y} L{x + 9 * c:.1f} {y + 9 * sn:.1f}" {W(1.6)}/>' for c, sn in [(1, 0), (0, 1), (-1, 0), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)])
            + f'<circle cx="{x}" cy="{y}" r="3" fill="{O}"/>')
car = (f'<path d="M20 88 V70 Q20 62 30 62 H52 V34 Q52 28 58 28 H92 Q98 28 98 34 V62 H104 Q112 62 112 72 V88Z" fill="#E8554A" {s()}/>'
       + f'<rect x="60" y="36" width="30" height="22" rx="4" fill="#C9EEFF" {W(2.6)}/>'
       + f'<path d="M48 26 H102" {W(5)}/><path d="M50 24 Q75 12 100 24" fill="#3B3355" {W(2.6)}/>'
       + f'<path d="M14 88 H116" {W(4)}/>'
       + wheel(38, 94) + wheel(94, 94)
       + f'<circle cx="16" cy="66" r="9" fill="#FFE3A3" {s()}/>' + eye(16, 66, 0.75)
       + f'<circle cx="34" cy="66" r="9" fill="#FFE3A3" {s()}/>' + eye(34, 66, 0.75)
       + f'<path d="M20 78 Q25 82 30 78" fill="none" {W(2.4)}/>'
       + f'<path d="M104 62 V50 L114 44" fill="none" {W(3)}/><path d="M112 40 L122 34 L124 50 Z" fill="#FFC93C" {W(2.4)}/><circle cx="104" cy="66" r="0"/>'
       + f'<ellipse cx="98" cy="56" rx="6" ry="5" fill="#3B3355"/>'
       + sparkle(116, 20, 6))

S = {"kitenok-zhulebino": ("малыш в шапочке плывёт кролем, из шапочки бьёт фонтанчик, как у китёнка", "sky", kit),
     "lomakovka": ("старинный автомобиль-персонаж с фарами-глазками и клаксоном", "yellow", car)}
if __name__ == "__main__":
    reg = os.path.join(out, "subjects.txt"); txt = open(reg).read()
    for pid, (subj, bg, body) in S.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M) + f"{pid} — {subj}\n"
    open(reg, "w").write(txt)
