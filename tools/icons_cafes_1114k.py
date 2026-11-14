"""Иконки робота cafes, 2026-11-14 (16–18 UTC, запуск 1114k). Каждая придумана и нарисована отдельно (правило АБСОЛЮТНОЙ уникальности).
Запуск: python3 tools/icons_cafes_1114k.py [id…]  (без аргументов — все + строки реестра в subjects.txt)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
BL = lambda x, y: f'<ellipse cx="{x}" cy="{y}" rx="3.4" ry="2" fill="#FF7FA8" opacity=".75"/>'
draw_icons.BG.update({
    "kk_sky": ("#EAF8FF", "#3F9BD8"),
    "kk_coral": ("#FFF1EA", "#E86A4A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Алло! Пицца в Северном Измайлове (детская комната, в меню пицца «Мехико»): пицца «Мехико» раскачивается на канате над матами
add("cafe-allo-pizza-konstantina-fedina-11",
    "круглая пицца «Мехико» с зелёными колечками халапеньо, жёлтыми зёрнами кукурузы и красной фасолью",
    "держится одной рукой за толстый канат с узелками и раскачивается, как на лиане, над синими мягкими матами игровой",
    "kk_sky", f"""
<path d="M64 -4 Q66 20 70 40" fill="none" stroke="#C99A5B" stroke-width="5" stroke-linecap="round"/>
<path d="M64 -4 Q66 20 70 40" fill="none" stroke="#8E6A3A" stroke-width="1.6" stroke-dasharray="3 4"/>
<circle cx="65.5" cy="14" r="4" fill="#C99A5B" {W(2)}/>
<circle cx="67.5" cy="28" r="4" fill="#C99A5B" {W(2)}/>
<g {W(2.8)}>
<rect x="-4" y="104" width="46" height="26" rx="5" fill="#3A6FD8"/>
<rect x="42" y="104" width="44" height="26" rx="5" fill="#5B8EF0"/>
<rect x="86" y="104" width="46" height="26" rx="5" fill="#3A6FD8"/>
</g>
<g transform="rotate(14 64 70)">
<circle cx="62" cy="70" r="30" fill="#E8A54B" {W(3.2)}/>
<circle cx="62" cy="70" r="24" fill="#E8503A"/>
<path d="M44 62 Q52 54 62 60 Q74 52 82 64 Q86 78 74 86 Q62 92 50 84 Q40 74 44 62Z" fill="#FFE08A" opacity=".9"/>
<g fill="none" stroke="#3E9B3A" stroke-width="2.6"><circle cx="48" cy="62" r="4"/><circle cx="78" cy="74" r="4"/><circle cx="58" cy="86" r="4"/></g>
<g fill="#FFD23F" stroke="#C99A1A" stroke-width=".8"><circle cx="72" cy="58" r="2"/><circle cx="76" cy="62" r="2"/><circle cx="46" cy="76" r="2"/><circle cx="70" cy="86" r="2"/><circle cx="54" cy="56" r="2"/></g>
<g fill="#9B2335"><ellipse cx="80" cy="84" rx="3" ry="2"/><ellipse cx="44" cy="70" rx="3" ry="2"/><ellipse cx="66" cy="52" rx="3" ry="2"/></g>
{eye(56, 70, .8)}{eye(70, 70, .8)}
<path d="M57 77 Q63 83 69 77" fill="#7A2A1A" {W(2.2)}/>
{BL(51, 76)}{BL(75, 76)}
<path d="M88 76 L100 82" fill="none" {W(3)}/>
<path d="M40 82 L30 92" fill="none" {W(3)}/>
</g>
<path d="M72 44 L70 40" fill="none" {W(3.2)}/>
<circle cx="70" cy="40" r="5" fill="#E8A54B" {W(2.4)}/>
<path d="M22 50 Q16 56 22 62 M18 44 Q8 54 18 66" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
{sparkle(104, 26, 5)}{sparkle(24, 24, 4)}
""")

# 2. Якитория у «Семёновской» (подборка «Рестораны с аниматором для детей»): палочка якитори за детским диджейским пультом
add("cafe-yakitoriya-semenovskaya-pl-2",
    "палочка якитори — три кусочка курицы в блестящей коричневой глазури тарэ на бамбуковой шпажке, между ними перья зелёного лука",
    "в больших оранжевых наушниках крутит пластинку за детским диджейским пультом на празднике, вокруг прыгают музыкальные ноты",
    "kk_coral", f"""
<rect x="16" y="88" width="96" height="30" rx="7" fill="#4A4A6A" {W(3)}/>
<circle cx="40" cy="98" r="11" fill="#22223A" {W(2.4)}/><circle cx="40" cy="98" r="3.6" fill="#FFD23F"/>
<circle cx="88" cy="98" r="11" fill="#22223A" {W(2.4)}/><circle cx="88" cy="98" r="3.6" fill="#4FC3F7"/>
<path d="M33 93 Q40 88 47 93" fill="none" stroke="#6E6E9A" stroke-width="1.6"/>
<rect x="56" y="94" width="16" height="4" rx="2" fill="#8BD46A"/><rect x="56" y="102" width="16" height="4" rx="2" fill="#FF6B6B"/>
<path d="M66 112 L66 4" stroke="#D9B26F" stroke-width="5" stroke-linecap="round"/>
<path d="M66 112 L66 4" fill="none" {W(1.2)}/>
<g {W(2.8)}>
<path d="M54 22 Q52 14 60 12 Q70 10 76 14 Q80 20 76 26 Q68 30 58 28 Q54 26 54 22Z" fill="#B0682E"/>
<path d="M50 52 Q48 38 60 36 Q74 34 82 40 Q86 50 80 60 Q70 66 58 64 Q50 60 50 52Z" fill="#A65F2A"/>
<path d="M54 84 Q52 76 60 74 Q72 72 78 78 Q80 86 74 90 Q64 92 58 90 Q54 88 54 84Z" fill="#B0682E"/>
<rect x="58" y="28.5" width="16" height="7" rx="3" fill="#5BBF4A"/>
<rect x="58" y="65.5" width="16" height="7.5" rx="3" fill="#5BBF4A"/>
</g>
<path d="M58 16 Q64 13 70 15 M55 42 Q63 38 72 40 M59 78 Q65 75 71 77" fill="none" stroke="#E6A15F" stroke-width="2.2" stroke-linecap="round"/>
<path d="M57 22 Q66 26 75 21 M53 56 Q66 62 79 54 M57 86 Q66 89 75 85" fill="none" stroke="#6E3A14" stroke-width="1.6" opacity=".6"/>
<g fill="#F7EBD0"><circle cx="62" cy="20" r="1"/><circle cx="70" cy="18" r="1"/><circle cx="76" cy="47" r="1"/><circle cx="64" cy="84" r="1"/></g>
{eye(60, 50, .72)}{eye(72, 50, .72)}
<path d="M62 56 Q66 59.5 70 56" fill="none" {W(2)}/>
{BL(55, 56)}{BL(77, 56)}
<path d="M44 48 Q44 26 66 24 Q88 26 88 48" fill="none" stroke="#FF8A1E" stroke-width="3.8"/>
<rect x="40" y="42" width="10" height="16" rx="4" fill="#FF8A1E" {W(2.4)}/>
<rect x="82" y="42" width="10" height="16" rx="4" fill="#FF8A1E" {W(2.4)}/>
<path d="M51 60 L38 76 Q36 80 40 82 M81 60 L88 74" fill="none" {W(3)}/>
<g fill="#3B3355"><ellipse cx="22" cy="44" rx="4" ry="3"/><path d="M25.5 44 L25.5 30 L31 33" fill="none" stroke="#3B3355" stroke-width="2"/>
<ellipse cx="104" cy="36" rx="4" ry="3"/><ellipse cx="114" cy="32" rx="4" ry="3"/><path d="M107.5 36 L107.5 22 L117.5 18 L117.5 32" fill="none" stroke="#3B3355" stroke-width="2"/></g>
{sparkle(30, 70, 4)}{sparkle(100, 64, 5)}
"""
)

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    if not sys.argv[1:]:
        reg = os.path.join(OUT, "subjects.txt")
        have = open(reg).read()
        with open(reg, "a") as f:
            for pid in ids:
                if pid + " —" not in have:
                    f.write(f"{pid} — герой: {SUBJ[pid][0]} | сцена: {SUBJ[pid][1]}\n")
    print("svg:", len(ids))
