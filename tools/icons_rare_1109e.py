"""Иконки робота rare, 2026-11-09 (12 UTC) — места из tools/add_rare_1109e.py.
АБСОЛЮТНАЯ уникальность: каждая придумана отдельно. Просмотрены листы icons-catalog 03, 19, 27, 45, 46, 50
(батуты, цирк, скалодромы, картинг, теннис) и реестр subjects.txt (купол/тент, тумба, стойка, жонглёры, шарф).
Запуск: python3 tools/icons_rare_1109e.py → icons-src/<id>.svg + строки реестра в subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, eye, face, sparkle, O
from icons_sections_1107c import G
from icons_sections_1108g import rect, circ, ell, path, SKIN
from icons_rare_1109 import racket, tball

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
draw_icons.BG.update({
    "re_snow": ("#EAF6FF", "#5C86C9"), "re_ring": ("#FFF1E0", "#D9534F"),
})


def add(pid, bg, body, hero, scene):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def flake(x, y, r):
    return path(f"M{x-r} {y} H{x+r} M{x} {y-r} V{y+r} M{x-r*.7} {y-r*.7} L{x+r*.7} {y+r*.7} M{x-r*.7} {y+r*.7} L{x+r*.7} {y-r*.7}",
                "none", 2).replace(O, "#ffffff", 1)


# 1. ВТБ Арена (крытые тентовые корты, круглый год тепло) — синяя ракетка выглядывает из арки белого тента в снегопад
add("vtb-arena-tennis-dinamo", "re_snow",
    # белый тент-ангар
    path("M8 122 L8 70 Q64 4 120 70 L120 122Z", "#FFFFFF", 3)
    + path("M30 122 V48 M98 122 V48 M64 122 V24", "none", 1.6).replace(O, "#C9D6E8", 1)
    # тёплый проём
    + path("M30 122 V86 Q64 40 98 86 V122Z", "#FFD27A", 2.8)
    + G(64, 78, racket("#1F4FB5", rx=19, ry=24, face_k=0.5), 0)
    + tball(86, 108, 7, fc=True, k=0.36)
    + flake(18, 40, 5) + flake(108, 30, 4) + flake(14, 92, 3.5) + flake(116, 100, 4) + flake(40, 18, 3.5),
    "тёмно-синяя теннисная ракетка с белыми струнами",
    "стоит в тёплом жёлтом проёме белого тентового ангара, а снаружи кружится снег; у её ручки греется жёлтый мячик")

# 2. United Circus Studio — мальчик-акробат делает стойку на руках на цирковой тумбе под лучом прожектора
add("united-circus-studio-moskovsky", "re_ring",
    # луч прожектора
    path("M52 0 L76 0 L112 128 L16 128Z", "#FFF6C2", 0).replace(f'stroke="{O}"', 'stroke="none"', 1)
    # занавес-фестон сверху
    + "".join(path(f"M{x} 4 Q{x+8} 22 {x+16} 4Z", "#C62828", 2.2) for x in range(0, 128, 16)) + rect(0, -4, 128, 9, "#C62828", 0, 2.2)
    # тумба
    + path("M38 100 L90 100 L84 126 L44 126Z", "#2E6FD8", 2.8)
    + rect(34, 92, 60, 10, "#FFC107", 3, 2.8)
    + G(64, 113, path("M0 -7 L2 -2 L7 -2 L3 1 L5 6 L0 3 L-5 6 L-3 1 L-7 -2 L-2 -2Z", "#FFF59D", 1.6))
    # мальчик в стойке на руках (голова внизу)
    + path("M52 92 L55 76 M76 92 L73 76", "none", 8) + path("M52 92 L55 76 M76 92 L73 76", "none", 5).replace(O, SKIN, 1)
    + circ(64, 72, 9, SKIN, 2.6) + face(64, 70, 3.2, 0.4)
    + rect(55, 34, 18, 32, "#2EBD6B", 7, 2.6)
    + path("M55 42 H73 M55 50 H73 M55 58 H73", "none", 2).replace(O, "#FFFFFF", 1)
    + path("M58 34 L52 14 M70 34 L78 16", "none", 6).replace(O, "#2EBD6B", 1)
    + path("M58 34 L52 14 M70 34 L78 16", "none", 1.2)
    + ell(51, 12, 5, 3.4, "#E53935", 2.2) + ell(79, 14, 5, 3.4, "#E53935", 2.2)
    + sparkle(22, 52, 6) + sparkle(106, 46, 5) + sparkle(98, 80, 3.5),
    "мальчик-акробат в зелёном полосатом трико и красных чешках",
    "делает стойку на руках, ноги в шпагат вверх, на синей цирковой тумбе со звездой под лучом прожектора и красным фестоном занавеса")

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for pid, s_ in ICONS.items():
        if not only or pid in only:
            open(os.path.join(OUT, pid + ".svg"), "w").write(s_)
    reg = os.path.join(OUT, "subjects.txt")
    keep = [l for l in open(reg).read().splitlines() if l.split(" — ")[0] not in SUBJ]
    open(reg, "w").write("\n".join(keep + [SUBJ[p] for p in SUBJ]) + "\n")
    print("icons", len(ICONS))
