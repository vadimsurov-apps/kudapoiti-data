"""Иконки робота cafes, 2026-11-10 (08:10 UTC). Правило АБСОЛЮТНОЙ уникальности: каждая придумана и нарисована
отдельно. Сверено с icons-src/subjects.txt: барабулька, цыплёнок табака, печёное яблоко, стаканчик армуду — в реестре нет.
Запуск: python3 tools/icons_cafes_1110d.py [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons
from draw_icons import svg, s, eye, face, sparkle, O

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
W = lambda w: s(f'stroke-width="{w}"')
draw_icons.BG.update({
    "k16_blacksea": ("#D8FBFF", "#2E9CC8"),
    "k16_saffron": ("#FFF7DA", "#F2A93B"),
    "k16_dune": ("#FFF6E8", "#88C9C2"),
    "k16_garden": ("#F2FFE9", "#6FAF6A"),
})


def add(pid, hero, scene, bg, body):
    ICONS[pid] = svg(bg, body)
    SUBJ[pid] = (hero, scene)


# 1. Клёво (Усачёвский рынок) — черноморская кухня, название «Клёво»: рыбка клюнула и висит на леске
add("cafe-klevo-usacheva",
    "красная черноморская рыбка-барабулька с жёлтой полоской вдоль бока",
    "клюнула на крючок и висит на леске над синей волной, удивлённо округлив рот", "k16_blacksea", f'''
<path d="M64 0 L64 30" stroke="#3B3355" stroke-width="2.4"/>
<path d="M64 30 Q64 42 56 42 Q50 42 51 36" fill="none" stroke="#6B6B7A" stroke-width="3" stroke-linecap="round"/>
<g transform="rotate(-40 64 64)">
<path d="M22 70 Q34 46 66 48 Q92 50 100 70 Q92 90 66 92 Q34 94 22 70Z" fill="#F0605A" {s()}/>
<path d="M30 74 Q60 80 96 72" fill="none" stroke="#FFD34E" stroke-width="5" stroke-linecap="round"/>
<path d="M100 70 L118 54 L114 70 L118 86Z" fill="#F0605A" {s()}/>
<path d="M50 50 Q60 36 74 48" fill="#F58A7E" {W(2.4)}/>
{eye(36, 64, 1.0)}
<ellipse cx="26" cy="74" rx="3.6" ry="4.4" fill="#7A2E3A"/>
<ellipse cx="42" cy="78" rx="4.2" ry="2.4" fill="#FF7FA8" opacity=".6"/>
</g>
<path d="M0 108 Q16 98 32 108 T64 108 T96 108 T128 108 L128 128 L0 128Z" fill="#1E6FA8" {W(2.4)}/>
<path d="M10 104 Q16 100 22 104 M74 104 Q80 100 86 104" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/>
''' + sparkle(98, 26, 4) + sparkle(28, 30, 3))

# 2. PRO.Хинкали (Бутырская) — грузинская кухня, по выходным аниматор: цыплёнок табака делает зарядку
add("cafe-prokhinkali-butyrskaya",
    "румяный цыплёнок табака, расплющенный в золотистое сердечко с полосками от сковороды",
    "делает зарядку на синей тарелке — раскинул ножки в шпагат и поднял крылышки вверх", "k16_saffron", f'''
<ellipse cx="64" cy="104" rx="52" ry="14" fill="#3E6FD8" {s()}/>
<ellipse cx="64" cy="102" rx="40" ry="8" fill="#6E96EC"/>
<path d="M44 86 L12 86" stroke="#C8762E" stroke-width="9" stroke-linecap="round"/>
<path d="M84 86 L116 86" stroke="#C8762E" stroke-width="9" stroke-linecap="round"/>
<circle cx="10" cy="86" r="6" fill="#FFF3DC" {W(2.4)}/><circle cx="118" cy="86" r="6" fill="#FFF3DC" {W(2.4)}/>
<path d="M64 98 Q22 70 30 46 Q38 26 64 42 Q90 26 98 46 Q106 70 64 98Z" fill="#E59A3C" {s()}/>
<path d="M44 52 L56 64 M56 46 L74 64 M72 46 L86 60" stroke="#A95E20" stroke-width="3" stroke-linecap="round"/>
<path d="M34 50 Q22 34 26 18" fill="none" stroke="#C8762E" stroke-width="8" stroke-linecap="round"/>
<path d="M94 50 Q106 34 102 18" fill="none" stroke="#C8762E" stroke-width="8" stroke-linecap="round"/>
<g>{face(64, 72, d=11, k=1.0)}</g>
<path d="M58 34 Q64 24 70 34" fill="#3FA34D" {W(2)}/>
''' + sparkle(16, 40, 3.5) + sparkle(112, 40, 3.5))

# 3. Берег (Строгинский лесопарк, вид на залив) — печёное яблоко отдыхает на песчаном берегу
add("cafe-bereg-strogino",
    "печёное красное яблоко с трещинками на кожуре, корицей-палочкой вместо хвостика и каплей мёда",
    "сидит на песчаном берегу залива, а за ним по воде скользит маленький белый парусник", "k16_dune", f'''
<path d="M0 72 L128 72 L128 128 L0 128Z" fill="#59B9D6"/>
<path d="M0 92 Q40 82 76 90 Q104 96 128 88 L128 128 L0 128Z" fill="#F2D49A" {W(2.4)}/>
<path d="M96 70 L96 46 L112 66Z" fill="#FFFFFF" {W(2)}/>
<path d="M90 70 L114 70 L110 76 L94 76Z" fill="#E86A5A" {W(2)}/>
<path d="M62 46 Q30 40 30 74 Q32 104 64 106 Q96 104 98 74 Q98 40 66 46Z" fill="#D9363E" {s()}/>
<path d="M44 58 L50 64 M84 62 L80 70 M48 90 L54 86" stroke="#8E1E2A" stroke-width="2.4" stroke-linecap="round"/>
<rect x="60" y="28" width="7" height="22" rx="2" fill="#9A5A2E" {W(2.2)} transform="rotate(10 64 40)"/>
<path d="M70 44 Q86 34 92 42 Q82 52 70 46Z" fill="#6CBF5A" {W(2.2)}/>
<path d="M74 48 Q80 56 76 62 Q72 56 74 48Z" fill="#FFC531" {W(1.8)}/>
<g>{face(62, 78, d=11, k=1.0)}</g>
''' + sparkle(24, 30, 3.5) + sparkle(42, 18, 2.6))

# 4. Успенские встречи — восточная кухня и гостеприимство: стаканчик армуду встречает гостей у калитки сада
add("cafe-uspenskie-vstrechi",
    "грушевидный стеклянный стаканчик армуду с янтарным чаем на маленьком красном блюдце",
    "стоит у открытой зелёной калитки загородного сада и приветливо машет гостям поднятой ручкой", "k16_garden", f'''
<path d="M6 104 L6 50 M30 104 L30 50" stroke="#2E7D4A" stroke-width="5" stroke-linecap="round"/>
<path d="M6 60 L30 60 M6 92 L30 92 M6 60 L30 92" stroke="#2E7D4A" stroke-width="4" stroke-linecap="round"/>
<circle cx="18" cy="44" r="10" fill="#7CC46A" {W(2.2)}/><circle cx="110" cy="40" r="12" fill="#7CC46A" {W(2.2)}/>
<ellipse cx="68" cy="106" rx="40" ry="10" fill="#D8343A" {s()}/>
<ellipse cx="68" cy="104" rx="26" ry="5" fill="#F06A6A"/>
<path d="M50 24 L86 24 Q82 40 78 50 Q94 70 86 92 Q80 102 68 102 Q56 102 50 92 Q42 70 58 50 Q54 40 50 24Z" fill="#E4F6FF" fill-opacity=".85" {s()}/>
<path d="M54 56 Q68 52 82 56 Q90 72 84 90 Q78 98 68 98 Q58 98 52 90 Q46 72 54 56Z" fill="#C8641E"/>
<path d="M58 30 L62 46" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity=".9"/>
<g fill="#FFFFFF">{face(68, 74, d=9, k=0.9)}</g>
<path d="M88 66 Q100 56 104 46" fill="none" stroke="#3B3355" stroke-width="3.4" stroke-linecap="round"/>
<circle cx="105" cy="44" r="6" fill="#E4F6FF" {W(2.4)}/>
<path d="M60 18 Q56 12 60 6 M70 18 Q66 12 70 6" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round" opacity=".85"/>
''' + sparkle(40, 30, 3))


def main(ids):
    ids = ids or list(ICONS)
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w").write(ICONS[pid])
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    have = {l.split(" — ", 1)[0] for l in lines if " — " in l}
    with open(reg, "a", encoding="utf-8") as f:
        for pid in ids:
            if pid not in have:
                h, sc = SUBJ[pid]
                f.write(f"{pid} — герой: {h} | сцена: {sc}\n")
    print("svg", len(ids))


if __name__ == "__main__":
    main(sys.argv[1:])
