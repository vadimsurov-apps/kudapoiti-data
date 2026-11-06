"""Робот акций 06.11: иконки двух новых картингов (MIKS Karting Academy, Dozari Kart).
Якорь — карт-персонаж сбоку (без водителя, мордочка на корпусе). Шутка: шапка выпускника у «Академии»,
воздушный шарик у детской школы Dozari (пробное для малышей до 9 лет)."""
import os, re
from draw_icons import svg, s, eye, face, sparkle, O

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")


def kart(body="#FF5A5F", nose="#FFC93C"):
    return (
        # выхлоп и задний бампер
        f'<rect x="10" y="78" width="12" height="7" rx="3" fill="#9AA0B8" {s("stroke-width=\"2.4\"")}/>'
        # спинка сиденья
        f'<path d="M30 80 L26 50 Q26 44 32 44 L40 44 Q44 44 44 50 L46 80Z" fill="#3B3355" {s()}/>'
        # руль на колонке
        f'<path d="M84 76 L76 56" fill="none" {s("stroke-width=\"4\"")}/>'
        f'<ellipse cx="75" cy="53" rx="9" ry="4.5" fill="#5A5470" transform="rotate(-25 75 53)" {s("stroke-width=\"2.6\"")}/>'
        # корпус
        f'<path d="M18 88 Q18 72 36 72 L80 72 Q106 74 114 88 Q116 98 104 98 L28 98 Q18 98 18 88Z" fill="{body}" {s()}/>'
        f'<path d="M98 80 Q110 84 113 90 L100 92Z" fill="{nose}" {s("stroke-width=\"2.4\"")}/>'
        # колёса
        f'<circle cx="36" cy="100" r="14" fill="#3B3355" {s()}/><circle cx="36" cy="100" r="5" fill="#C9CDD8"/>'
        f'<circle cx="96" cy="102" r="11" fill="#3B3355" {s()}/><circle cx="96" cy="102" r="4" fill="#C9CDD8"/>'
        + face(66, 82, d=10, k=0.9)
    )


S = {
    "miks-karting-academy": ("карт-персонаж в шапке выпускника («Академия картинга»)", "blue",
        kart("#FF5A5F")
        + f'<path d="M36 36 L60 26 L84 36 L60 46Z" fill="#3B3355" {s("stroke-width=\"2.6\"")}/>'
          f'<path d="M46 40 V50 Q60 56 74 50 V40" fill="#3B3355" {s("stroke-width=\"2.6\"")}/>'
          f'<path d="M82 36 V50" stroke="#FFC93C" stroke-width="3"/><circle cx="82" cy="52" r="3.5" fill="#FFC93C"/>'
        + sparkle(104, 30, 6) + sparkle(20, 30, 4)),
    "dozari-kart": ("карт-персонаж с воздушным шариком на спинке сиденья", "yellow",
        kart("#4FB3F5", "#FF7FA8")
        + f'<path d="M42 46 Q52 46 54 40" fill="none" stroke="{O}" stroke-width="2"/>'
          f'<ellipse cx="54" cy="21" rx="13" ry="16" fill="#FF5A6A" {s()}/>'
          f'<path d="M51 37 L54 41 L57 37Z" fill="#FF5A6A" {s("stroke-width=\"2\"")}/>'
          f'<ellipse cx="49" cy="15" rx="3.5" ry="5.5" fill="#fff" opacity=".6"/>'
        + sparkle(100, 30, 6) + sparkle(110, 52, 4)),
}

if __name__ == "__main__":
    for pid, (subj, bg, body) in S.items():
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    reg = os.path.join(out, "subjects.txt"); txt = open(reg).read()
    for pid in S:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    txt += "".join(f"{pid} — {subj}\n" for pid, (subj, _, _) in S.items())
    open(reg, "w").write(txt)
    print(len(S))
