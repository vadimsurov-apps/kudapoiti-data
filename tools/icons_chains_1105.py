"""Иконки для сверки сетей 05.11: освободившиеся сюжеты удалённых филиалов переходят новым + 4 новых сюжета."""
import os, shutil
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); src = os.path.join(here, "..", "icons-src")
MOVE = {"cafe-anderson-vdnh": "cafe-anderson-domodedovo", "cafe-anderson-sokol": "cafe-anderson-vorontsovsky",
        "cafe-anderson-krasnoselskaya": "cafe-anderson-afanasyevsky", "cafe-anderson-strastnoy": "cafe-anderson-donskoy",
        "cafe-anderson-bratislavskaya": "cafe-anderson-medvedkovo", "cafe-anderson-mitino": "cafe-anderson-mitino-dubravnaya",
        "cafe-anderson-zhulebino": "cafe-anderson-tsaritsyno", "cafe-anderson-festival": "cafe-anderson-fort-yasenevo",
        "cafe-anderson-korolev": "cafe-anderson-pushkino", "cafe-chaihona-polyanka": "cafe-chaihona1-altufevo",
        "cafe-chaihona-gruzinskaya": "cafe-chaihona1-vernadskogo", "cafe-chaihona-prazhskaya": "cafe-chaihona1-zhukovka"}
NEW = {
    "cafe-chaihona1-marino": ("orange",   # юрта
        f'<path d="M14 98 V70 Q14 58 26 54 L64 34 L102 54 Q114 58 114 70 V98Z" fill="#F7EEDB" {s()}/>'
        f'<path d="M26 54 Q64 20 102 54 Q64 44 26 54Z" fill="#E8654F" {s()}/><path d="M60 26 H68 V36 H60Z" fill="#A86F3E" {W(2.4)}/>'
        f'<path d="M14 72 H114" stroke="#E8654F" stroke-width="6"/><path d="M14 72 L24 64 L34 72 L44 64 L54 72 L64 64 L74 72 L84 64 L94 72 L104 64 L114 72" fill="none" stroke="#FFD25E" stroke-width="3"/>'
        f'<path d="M52 98 V82 Q52 74 64 74 Q76 74 76 82 V98Z" fill="#A86F3E" {s()}/>' + f(40, 86, d=6, k=0.55) + sparkle(110, 24, 6)),
    "cafe-chaihona1-mitino": ("yellow",   # чак-чак
        f'<path d="M20 92 Q64 112 108 92 L102 104 Q64 120 26 104Z" fill="#A86F3E" {s()}/>'
        + "".join(f'<rect x="{x}" y="{y}" width="16" height="9" rx="4" fill="#F2B544" {W(2.4)} transform="rotate({r} {x+8} {y+4})"/>'
                  for x, y, r in [(26, 82, 10), (44, 86, -8), (62, 84, 15), (80, 82, -12), (34, 70, -15), (52, 72, 8), (70, 70, -6),
                                  (44, 58, 12), (60, 58, -10), (52, 46, 5)])
        + f'<path d="M88 40 Q92 54 86 62" fill="none" stroke="#F2B544" stroke-width="5" stroke-linecap="round"/>' + f(64, 92, d=6, k=0.5, blush=False)
        + sparkle(26, 30, 6)),
    "cafe-chaihona1-novokosino": ("teal",   # тюбетейка
        f'<path d="M20 84 Q18 40 64 36 Q110 40 108 84Z" fill="#3E4AA0" {s()}/><path d="M20 84 H108 V96 H20Z" fill="#2E3A80" {s()}/>'
        f'<path d="M40 82 Q44 58 64 54 Q84 58 88 82" fill="none" stroke="#fff" stroke-width="4"/><path d="M64 38 V82" stroke="#fff" stroke-width="3"/>'
        f'<path d="M48 60 Q56 52 64 60 Q72 52 80 60" fill="none" stroke="#FFD25E" stroke-width="3"/>' + f(64, 70, d=7, k=0.55, blush=False)
        + f'<path d="M30 90 H98" stroke="#FFD25E" stroke-width="3" stroke-dasharray="6 5"/>'),
    "cafe-chaihona1-tushino": ("purple",   # гроздь винограда
        f'<path d="M64 14 Q66 24 64 30 M64 22 Q80 10 92 18 Q84 30 66 26" fill="#7CD26E" {W(3)}/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="#8E5CC8" {W(3)}/>' for x, y in
                  [(44, 40), (64, 38), (84, 40), (54, 58), (74, 58), (34, 58), (94, 58), (44, 76), (64, 76), (84, 76), (54, 94), (74, 94), (64, 110)])
        + f(64, 76, d=5, k=0.45, blush=False) + sparkle(20, 22, 5)),
}
if __name__ == "__main__":
    for old, new in MOVE.items():
        shutil.copy(os.path.join(src, old + ".svg"), os.path.join(src, new + ".svg"))
    for pid, (bg, body) in NEW.items():
        open(os.path.join(src, pid + ".svg"), "w").write(svg(bg, body))
    # освобождённые сюжеты удалённых мест убираем из каталога (кекс «Бутово» остаётся свободным)
    for old in list(MOVE) + ["cafe-anderson-butovo"]:
        p = os.path.join(src, old + ".svg")
        if os.path.exists(p): os.remove(p)
    print(len(MOVE) + len(NEW))
