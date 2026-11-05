"""Перерисовка 12 иконок партии 15, повторявших существующие сюжеты."""
import os, json
from draw_icons import svg, s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
R = {}
add = lambda pid, bg, body: R.__setitem__(pid, (bg, body))

add("termoland-fizteh", "orange",   # войлочная банная шапка-колпак
    f'<path d="M24 96 Q30 40 64 14 Q98 40 104 96Z" fill="#E9D9B8" {s()}/><path d="M16 96 H112 Q114 110 100 110 H28 Q14 110 16 96Z" fill="#D8C49A" {s()}/>'
    f'<path d="M40 60 Q64 52 88 60" fill="none" stroke="#C9A86E" stroke-width="4"/>' + f(64, 80, d=9, k=0.75)
    + f'<path d="M30 30 Q24 18 32 8 M100 28 Q108 16 100 6" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')
add("termoland-butovo", "teal",   # банные песочные часы
    f'<rect x="30" y="12" width="68" height="12" rx="4" fill="#A86F3E" {s()}/><rect x="30" y="104" width="68" height="12" rx="4" fill="#A86F3E" {s()}/>'
    f'<path d="M40 24 H88 Q88 52 66 64 Q88 76 88 104 H40 Q40 76 62 64 Q40 52 40 24Z" fill="#E4F6FF" {s()}/>'
    f'<path d="M46 34 H82 Q78 50 64 58 Q50 50 46 34Z" fill="#FFD25E"/><path d="M64 64 V96 M46 100 Q64 84 82 100Z" fill="#FFD25E" stroke="#FFD25E" stroke-width="3"/>'
    + f(64, 44, d=6, k=0.5, blush=False))
add("jump-park-istra", "green",   # ребёнок в прыжке «звёздочкой»
    f'<circle cx="64" cy="28" r="14" fill="#FFE2B8" {s()}/>' + f(64, 28, d=6, k=0.55)
    + f'<path d="M64 42 V76 M64 50 L30 30 M64 50 L98 30 M64 76 L36 104 M64 76 L92 104" stroke="{O}" stroke-width="14" stroke-linecap="round"/>'
    + f'<path d="M64 42 V76 M64 50 L30 30 M64 50 L98 30 M64 76 L36 104 M64 76 L92 104" stroke="#FF7A3A" stroke-width="8" stroke-linecap="round"/>'
    + f'<path d="M16 118 H112" stroke="#2E2E3A" stroke-width="6" stroke-linecap="round"/>' + sparkle(18, 64, 6) + sparkle(110, 66, 6))
add("nebo-sokol", "sky",   # малыш прыгает на облаке
    f'<path d="M20 96 Q8 96 10 82 Q12 70 26 72 Q28 56 46 58 Q56 44 72 52 Q88 44 96 60 Q114 58 116 76 Q122 96 104 96Z" fill="#fff" {s()}/>'
    + f(64, 80, d=8, k=0.65)
    + f'<circle cx="64" cy="22" r="11" fill="#FFE2B8" {s()}/>' + f(64, 22, d=5, k=0.45, blush=False)
    + f'<path d="M64 33 V44 M56 38 L48 30 M72 38 L80 30" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M50 50 Q64 56 78 50" fill="none" stroke="#9DD6F5" stroke-width="3" stroke-dasharray="4 4"/>')
tiles = [(30, 40, "#F2557A"), (50, 32, "#FFD25E"), (70, 32, "#5CCDBA"), (88, 40, "#A98BF0"), (40, 58, "#6CC0F2"),
         (60, 54, "#FF9A3A"), (80, 58, "#7CD26E"), (50, 76, "#F58CB8"), (70, 76, "#FFD25E"), (60, 94, "#F2557A")]
add("joki-joya-mozaika", "pink",   # сердце из мозаики
    f'<path d="M64 112 Q14 76 18 44 Q22 18 46 20 Q58 22 64 36 Q70 22 82 20 Q106 18 110 44 Q114 76 64 112Z" fill="#FFF3D6" {s()}/>'
    + "".join(f'<rect x="{x-8}" y="{y-8}" width="16" height="16" rx="3" fill="{c}" {W(2)}/>' for x, y, c in tiles)
    + f'<path d="M64 112 Q14 76 18 44 Q22 18 46 20 Q58 22 64 36 Q70 22 82 20 Q106 18 110 44 Q114 76 64 112Z" fill="none" {s()}/>')
add("wanderia-zhukovsky", "green",   # походный рюкзак
    f'<path d="M44 26 Q44 12 64 12 Q84 12 84 26" fill="none" {W(5)}/><rect x="28" y="24" width="72" height="88" rx="20" fill="#FF7A3A" {s()}/>'
    f'<rect x="40" y="70" width="48" height="30" rx="8" fill="#FFAE6B" {s()}/><path d="M40 82 H88" stroke="{O}" stroke-width="2.4"/>'
    f'<path d="M28 44 Q14 50 18 78" fill="none" stroke="#3E9A50" stroke-width="6" stroke-linecap="round"/>' + f(64, 48, d=9, k=0.7)
    + f'<rect x="58" y="78" width="12" height="8" rx="2" fill="#FFD25E" {W(2)}/>')
add("drakosha-chekhov", "teal",   # волчок
    f'<path d="M64 6 V26" {W(6)}/><path d="M64 26 Q108 40 108 64 Q100 90 64 114 Q28 90 20 64 Q20 40 64 26Z" fill="#F2557A" {s()}/>'
    f'<path d="M22 60 Q64 72 106 60" fill="none" stroke="#FFD25E" stroke-width="10"/><path d="M30 80 Q64 90 98 80" fill="none" stroke="#6CC0F2" stroke-width="8"/>'
    + f(64, 48, d=8, k=0.65) + f'<path d="M10 104 Q30 112 40 100 M118 104 Q98 112 88 100" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')
stripes = "".join(f'<path d="M{x} 54 L{x+3} 118" stroke="#E8304A" stroke-width="7"/>' for x in (40, 56, 72, 88))
add("mori-cinema-mytishchi", "night",   # ведёрко попкорна
    f'<path d="M30 54 H98 L90 118 H38Z" fill="#fff" {s()}/>' + stripes + f'<path d="M30 54 H98 L90 118 H38Z" fill="none" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="#FFF3C4" {W(2.4)}/>' for x, y in [(38, 46), (54, 38), (70, 40), (86, 46), (62, 26), (46, 28), (80, 28)])
    + f(64, 84, d=9, k=0.7))
add("tsar-maket", "yellow",   # ладонь с крошечным человечком
    f'<path d="M20 70 Q18 56 30 56 Q38 56 40 66 V40 Q40 30 48 30 Q56 30 56 40 V34 Q56 24 64 24 Q72 24 72 34 V40 Q72 32 80 32 Q88 32 88 42 V76 Q102 60 110 68 Q116 74 104 90 Q88 112 64 114 Q30 114 20 70Z" fill="#FFE2B8" {s()}/>'
    f'<circle cx="64" cy="62" r="6" fill="#3E4AA0" {W(2)}/><path d="M64 68 V82 M58 74 H70 M64 82 L60 90 M64 82 L68 90" stroke="#3E4AA0" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(100, 24, 7) + sparkle(22, 30, 4))
add("mk-zoya", "sky",   # фронтовое письмо-треугольник
    f'<path d="M14 40 H114 L64 110Z" fill="#F7EEDB" {s()}/><path d="M14 40 L64 76 L114 40" fill="none" {W(3)}/>'
    f'<path d="M34 54 L50 66 M84 54 L72 64" stroke="#8E9AAE" stroke-width="2"/><path d="M58 88 L64 80 L70 88 L64 96Z" fill="#E8304A" {W(2)}/>'
    + f(64, 58, d=7, k=0.6))
add("ecobiocentre", "green",   # улитка
    f'<path d="M14 100 Q14 86 30 86 H88 Q108 86 112 70 Q114 60 106 58 Q98 58 98 66" fill="#B9E08E" {s()}/>'
    f'<circle cx="64" cy="62" r="30" fill="#E8A65A" {s()}/><path d="M64 62 m0 -6 a6 6 0 1 1 -6 6 a12 12 0 1 1 12 12 a20 20 0 1 1 -20 -20" fill="none" stroke="#A86F3E" stroke-width="4"/>'
    f'<path d="M14 100 H96" {W(4)}/><path d="M104 58 L100 40 M110 60 L116 44" {W(3)}/><circle cx="100" cy="38" r="3" fill="{O}"/><circle cx="116" cy="42" r="3" fill="{O}"/>'
    + f(36, 90, d=5, k=0.45, blush=False))
add("safari-park-mozhaysk", "orange",   # сафари-джип
    f'<path d="M14 84 V60 Q14 52 22 52 H40 L52 34 H88 Q96 34 98 44 L104 52 H110 Q118 52 118 62 V84Z" fill="#C9A86E" {s()}/>'
    f'<path d="M56 40 H84 V52 H48Z" fill="#E4F6FF" {W(2.4)}/><path d="M40 30 H96" {W(4)}/><path d="M50 30 V40 M90 30 V40" {W(3)}/>'
    f'<circle cx="38" cy="88" r="13" fill="{O}"/><circle cx="38" cy="88" r="5" fill="#8E9AAE"/><circle cx="96" cy="88" r="13" fill="{O}"/><circle cx="96" cy="88" r="5" fill="#8E9AAE"/>'
    + f(80, 68, d=7, k=0.6) + f'<path d="M24 64 H34" stroke="#FFD25E" stroke-width="5" stroke-linecap="round"/>')
add("redpoint-climb", "orange",   # мешочек для магнезии
    f'<path d="M34 40 H94 L90 110 Q64 120 38 110Z" fill="#2F7FD8" {s()}/><ellipse cx="64" cy="40" rx="30" ry="9" fill="#fff" {s()}/>'
    f'<path d="M48 30 Q56 18 64 30 Q72 18 80 30" fill="#fff" {W(2.4)}/><path d="M34 70 H94" stroke="#FFD25E" stroke-width="6"/>'
    f'<path d="M4 76 H34 M94 76 H124" stroke="#3E3E4A" stroke-width="8" stroke-linecap="round"/><path d="M80 44 Q92 60 86 72" fill="none" stroke="#E8304A" stroke-width="3"/><rect x="82" y="70" width="8" height="12" rx="3" fill="#E8304A" {W(2)}/>' + f(64, 88, d=8, k=0.65)
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" opacity=".8"/>' for x, y in [(26, 22), (100, 18), (20, 40)]))

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    for pid, (bg, body) in R.items():
        open(os.path.join(here, "..", "icons-src", f"{pid}.svg"), "w").write(svg(bg, body))
    print(len(R))
