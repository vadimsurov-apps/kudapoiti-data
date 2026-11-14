"""Иконки робота pools, 2026-11-14 (17 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои сверены с реестром icons-src/subjects.txt
(колюшки, турпана и качурки в реестре нет), картинки — tools/check_unique.py.
Запуск: python3 tools/icons_pools_1114s.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}

# 1. SwimRocket, ФОК «Касатка» (с 4 лет) — рыбка-колюшка с тремя шипами-стабилизаторами всплывает ракетой
ICONS["swimrocket-kasatka"] = W("#8FE9F5", "#0C3F94", f'''
<path d="M40 -6 Q96 6 134 44 V-6Z" fill="#D9FBFF" opacity=".75"/>
<g transform="rotate(-38 64 66)">
<path d="M-22 58 H8 M-26 68 H6 M-20 78 H8" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".8"/>
<path d="M26 66 L4 46 L10 66 L4 86Z" fill="#F0503C" {s()}/>
<path d="M22 66 Q44 38 86 48 Q108 54 116 66 Q108 80 86 86 Q44 94 22 66Z" fill="#DCE8EE" {s()}/>
<path d="M22 66 Q44 38 86 48 Q108 54 116 66 Q70 58 22 66Z" fill="#3F9D7A"/>
<path d="M40 78 Q66 92 96 80 Q70 74 40 78Z" fill="#F0503C"/>
<path d="M22 66 Q44 38 86 48 Q108 54 116 66 Q108 80 86 86 Q44 94 22 66Z" fill="none" {s()}/>
<path d="M44 49 L47 28 L56 46Z M60 45 L64 24 L72 44Z M76 46 L81 30 L87 48Z" fill="#FFE27A" {s(T2)}/>
<path d="M70 70 Q62 82 74 84 Q80 78 78 70Z" fill="#FFE27A" {s(T2)}/>
{eye(98, 63, 1.35)}
<path d="M108 72 q4 2 7 -1" fill="none" {s(T2)}/>
</g>
{bub(22, 104, 6)}{bub(12, 118, 4)}{bub(36, 116, 3.4)}
''', 76, 14)
SUBJ["swimrocket-kasatka"] = ("трёхиглая рыбка-колюшка с зелёной спинкой, красным брюшком и тремя жёлтыми шипами на спине",
                              "ракетой всплывает по диагонали из синей глубины к светлой поверхности, за красным хвостом — три белые струи и пузыри")

# 2. «Мама, я плыву», Беломорская (0–9 лет, малыш + тренер) — мама-турпан везёт пухового птенца на спине
ICONS["mama-ya-plyvu-belomorskaya"] = W("#FFF4E2", "#FFAE9C", f'''
<circle cx="100" cy="30" r="13" fill="#FFE27A" opacity=".9"/>
<path d="M92 70 Q112 52 120 62 Q112 70 104 84Z" fill="#23232B" {s()}/>
<ellipse cx="66" cy="84" rx="42" ry="22" fill="#2E2E38" {s()}/>
<path d="M44 84 Q66 70 96 80" fill="none" stroke="#55556A" stroke-width="3.4" stroke-linecap="round"/>
<path d="M28 82 Q20 60 30 50 L46 56 Q42 70 48 84Z" fill="#2E2E38" {s()}/>
<circle cx="34" cy="46" r="16" fill="#2E2E38" {s()}/>
<path d="M20 44 L-2 50 Q6 58 22 56Z" fill="#FF8A1F" {s()}/>
<path d="M-2 50 q6 -1 9 2" fill="none" stroke="#E8483F" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="36" cy="42" r="5.6" fill="#fff"/><circle cx="36.6" cy="42.4" r="3" fill="{O}"/>
<path d="M40 48 q6 3 4 9" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/>
<circle cx="76" cy="56" r="14" fill="#C9CFDA" {s()}/>
<path d="M86 50 Q100 38 100 52 Q94 56 88 58Z" fill="#AEB6C4" {s(T2)}/>
<path d="M63 54 L54 57 L63 60Z" fill="#555C6B" {s(T2)}/>
{eye(70, 53, 0.9)}
<ellipse cx="72" cy="61" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".8"/>
<path d="M-6 96 Q20 88 44 96 T92 96 T134 94 V134 H-6Z" fill="#6C8FE6" {s()}/>
<path d="M10 110 q8 -5 16 0 M52 116 q8 -5 16 0 M92 108 q8 -5 16 0" fill="none" stroke="#DCE6FF" stroke-width="3" stroke-linecap="round"/>
''', 76, 22)
SUBJ["mama-ya-plyvu-belomorskaya"] = ("чёрная морская утка турпан с оранжевым клювом и белой запятой у глаза и её серый пуховый птенец",
                                      "мама плывёт по сиреневой утренней воде, птенец сидит у неё на спине и машет крылышком низкому солнцу, фон персиковый")

# 3. Школа плавания № 1, «Курьяново» (7–13 лет: «держусь на воде, хочу технику») — качурка, которая умеет бегать по воде
ICONS["ss1-kuryanovo"] = W("#F6FFD8", "#9ED45C", f'''
<rect x="-6" y="88" width="140" height="46" fill="#19B3CC" {s()}/>
<path d="M-6 104 H134" stroke="#fff" stroke-width="5"/>
<path d="M-6 104 H134" stroke="#E8483F" stroke-width="5" stroke-dasharray="10 10"/>
<path d="M52 44 Q30 8 14 6 Q22 30 40 56Z" fill="#3D302C" {s()}/>
<path d="M70 42 Q86 4 106 4 Q100 30 84 54Z" fill="#5A4640" {s()}/>
<path d="M30 60 L14 72 L34 72Z" fill="#3D302C" {s()}/>
<ellipse cx="60" cy="58" rx="30" ry="17" fill="#4A3B36" {s()}/>
<path d="M32 56 Q36 48 46 48 Q42 58 36 64Z" fill="#fff" {s(T2)}/>
<circle cx="90" cy="46" r="14" fill="#4A3B36" {s()}/>
<path d="M102 44 H116 Q120 48 114 52 L102 50Z" fill="#20242E" {s(T2)}/>
{eye(93, 43, 1.1)}
<ellipse cx="88" cy="52" rx="3.8" ry="2.2" fill="#FF7FA8" opacity=".8"/>
<path d="M52 74 L46 88 M70 74 L78 88" stroke="{O}" stroke-width="4.4" stroke-linecap="round"/>
<path d="M38 88 H54 L46 82Z M70 88 H86 L78 82Z" fill="#FFB02E" {s(T2)}/>
<ellipse cx="46" cy="92" rx="14" ry="3.6" fill="none" stroke="#fff" stroke-width="3"/>
<ellipse cx="78" cy="92" rx="14" ry="3.6" fill="none" stroke="#fff" stroke-width="3"/>
''', 30, 20)
SUBJ["ss1-kuryanovo"] = ("маленькая тёмно-бурая морская птичка качурка с белым пятном над хвостом и чёрным клювом-крючком",
                         "держится на воде: семенит оранжевыми лапками по поверхности бассейна у красно-белой дорожки, подняв крылья галочкой, от лапок расходятся круги, фон салатовый")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg, encoding="utf-8").read().rstrip("\n").split("\n")
    have = {l.split(" — ")[0] for l in lines if " — " in l}
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w", encoding="utf-8").write(ICONS[pid])
        if pid not in have:
            lines.append(f"{pid} — герой: {SUBJ[pid][0]} | сцена: {SUBJ[pid][1]}")
    open(reg, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("svg:", len(ids))
