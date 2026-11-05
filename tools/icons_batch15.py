"""Партия 15: иконки мест 722–741. Каждая — свой сюжет (сверено с icons-src и комментариями партий)."""
import os, json
from draw_icons import svg, s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
R = {}
add = lambda pid, bg, body: R.__setitem__(pid, (bg, body))

# скат-манта
add("manta-club", "blue",
    f'<path d="M64 30 Q84 34 120 66 Q92 70 74 92 L64 100 L54 92 Q36 70 8 66 Q44 34 64 30Z" fill="#4E7FD6" {s()}/>'
    f'<path d="M56 32 Q52 22 46 22 M72 32 Q76 22 82 22" fill="none" {W(4)}/>'
    f'<path d="M64 100 Q66 112 78 120" fill="none" {W(3.5)}/>'
    f'<path d="M44 70 Q64 86 84 70" fill="#CFE3FF" {W(2)}/>' + f(64, 54, d=10, k=0.8)
    + sparkle(22, 28, 5) + sparkle(104, 104, 5))
# ракушка-гребешок
ribs = "".join(f'<path d="M64 104 L{x} 34" stroke="#E07A9A" stroke-width="2.4"/>' for x in (32, 46, 64, 82, 96))
add("morelax-pool", "teal",
    f'<path d="M64 104 Q16 96 18 58 Q22 22 64 18 Q106 22 110 58 Q112 96 64 104Z" fill="#FFC9D6" {s()}/>' + ribs
    + f'<path d="M64 104 Q16 96 18 58 Q22 22 64 18 Q106 22 110 58 Q112 96 64 104Z" fill="none" {s()}/>'
    f'<path d="M48 104 H80 L74 116 H54Z" fill="#FFC9D6" {s()}/>' + f(64, 70, d=11, k=0.8))
# деревянная банная шайка с паром
add("termoland-putilkovo", "orange",
    f'<path d="M24 62 H104 L96 112 H32Z" fill="#D9925A" {s()}/>'
    f'<path d="M30 76 H98 M32 96 H96" stroke="#7A4A2A" stroke-width="5"/>'
    f'<ellipse cx="64" cy="62" rx="40" ry="9" fill="#9ED8F5" {s()}/>'
    f'<path d="M100 60 Q114 48 108 34" fill="none" stroke="#D9925A" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M44 46 Q38 36 46 28 Q54 20 48 10 M64 46 Q58 34 66 26 Q74 18 68 8 M84 46 Q78 36 86 28" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".85"/>'
    + f(64, 86, d=10, k=0.75))
# резиновая уточка
add("termoland-fizteh", "sky",
    f'<path d="M-4 100 Q30 92 64 100 Q98 108 132 98 V132 H-4Z" fill="#6CC0F2" {s()}/>'
    f'<path d="M22 72 Q20 104 60 106 Q104 106 106 78 Q92 82 82 74 Q94 62 90 46 Q84 26 62 28 Q40 30 40 52 Q40 62 48 70 Q34 74 22 72Z" fill="#FFD25E" {s()}/>'
    f'<path d="M86 48 Q104 46 108 54 Q100 62 86 60Z" fill="#FF8A3A" {s()}/>'
    + eye(70, 44, 1) + f'<path d="M40 86 Q56 94 72 86" fill="none" stroke="#E0A830" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(24, 30, 6) + sparkle(112, 22, 4))
# фонтан-грибок
add("termoland-butovo", "blue",
    f'<path d="M-4 104 Q30 96 64 104 Q98 112 132 102 V132 H-4Z" fill="#6CC0F2" {s()}/>'
    f'<rect x="54" y="56" width="20" height="50" rx="8" fill="#FFF3D6" {s()}/>'
    f'<path d="M18 60 Q20 20 64 18 Q108 20 110 60Z" fill="#FF6B6B" {s()}/>'
    f'<circle cx="44" cy="38" r="6" fill="#fff"/><circle cx="76" cy="32" r="5" fill="#fff"/><circle cx="92" cy="48" r="4" fill="#fff"/>'
    f'<path d="M20 62 Q14 80 18 98 M34 62 Q30 80 32 96 M108 62 Q114 80 110 98 M94 62 Q98 80 96 96" fill="none" stroke="#E4F6FF" stroke-width="4" stroke-linecap="round"/>'
    + f(64, 80, d=6, k=0.55))
# лупа над отпечатком пальца
prints = "".join(f'<path d="M{64-r} 74 Q{64-r} {74-r*1.3} 64 {74-r*1.3} Q{64+r} {74-r*1.3} {64+r} 74 Q{64+r} {74+r*0.8} {64+r*0.5} {74+r*1.1}" fill="none" stroke="#8E6CD8" stroke-width="3" stroke-linecap="round"/>' for r in (6, 12, 18, 24))
add("questkinder-among-us", "purple",
    f'<ellipse cx="64" cy="76" rx="32" ry="38" fill="#FFF3D6" {s()}/>' + prints
    + f'<circle cx="80" cy="46" r="26" fill="#E4F6FF" fill-opacity=".55" stroke="{O}" stroke-width="7"/>'
    f'<path d="M98 64 L118 86" stroke="{O}" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M98 64 L118 86" stroke="#C86BF0" stroke-width="6" stroke-linecap="round"/>' + f(80, 46, d=7, k=0.6))
# мешочек для магнезии
add("redpoint-climb", "orange",
    f'<path d="M30 40 H98 L94 108 Q64 118 34 108Z" fill="#E8304A" {s()}/>'
    f'<rect x="26" y="30" width="76" height="16" rx="8" fill="#fff" {s()}/>'
    f'<path d="M34 38 Q20 46 22 60" fill="none" {W(3)}/><circle cx="22" cy="62" r="4" fill="#FFD25E" {W(2)}/>'
    f'<path d="M44 26 Q50 12 58 22 Q66 8 74 20 Q84 10 86 26" fill="#fff" {W(2.4)}/>'
    + f(64, 76, d=11, k=0.85) + f'<path d="M104 100 L118 94 M104 82 L120 80" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')
# пружинка-попрыгунчик
coil = "".join(f'<ellipse cx="64" cy="{y}" rx="26" ry="7" fill="none" stroke="#5CCDBA" stroke-width="7"/><ellipse cx="64" cy="{y}" rx="26" ry="7" fill="none" {W(2)}/>' for y in (82, 94, 106))
add("jump-park-istra", "green", coil
    + f'<circle cx="64" cy="48" r="26" fill="#FFD25E" {s()}/>' + f(64, 48, d=9, k=0.8)
    + f'<path d="M30 30 L22 22 M98 30 L106 22 M64 14 V6" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
    f'<rect x="30" y="112" width="68" height="8" rx="4" fill="{O}"/>')
# воздушный змей
add("nebo-sokol", "sky",
    f'<path d="M64 10 L100 50 L64 96 L28 50Z" fill="#FF8A3A" {s()}/>'
    f'<path d="M64 10 L64 96 M28 50 H100" stroke="{O}" stroke-width="2.4"/>'
    f'<path d="M64 10 L100 50 L64 50Z" fill="#FFD25E"/><path d="M64 50 L28 50 L64 96Z" fill="#FFD25E"/>'
    f'<path d="M64 10 L100 50 L64 96 L28 50Z" fill="none" {s()}/>'
    f'<path d="M64 96 Q54 106 66 112 Q78 118 66 126" fill="none" {W(2.6)}/>'
    f'<path d="M58 106 L52 102 L54 110Z M70 116 L78 114 L74 120Z" fill="#E8304A" {W(1.6)}/>'
    + f(64, 52, d=8, k=0.65) + sparkle(20, 22, 5) + sparkle(108, 96, 6))
# кусочек пазла
add("joki-joya-mozaika", "pink",
    f'<path d="M30 40 H52 Q46 24 64 22 Q82 24 76 40 H98 V62 Q112 56 114 72 Q112 88 98 82 V106 H30 V84 Q16 90 14 74 Q16 58 30 64Z" fill="#7CD26E" {s()}/>'
    + f(64, 72, d=11, k=0.85) + sparkle(110, 22, 6) + sparkle(20, 110, 5))
# компас
add("wanderia-zhukovsky", "green",
    f'<circle cx="64" cy="66" r="44" fill="#FFF3D6" {s()}/><circle cx="64" cy="66" r="36" fill="none" stroke="#C9A06A" stroke-width="3"/>'
    f'<rect x="58" y="14" width="12" height="10" rx="3" fill="#C9A06A" {s()}/>'
    f'<path d="M64 34 L74 66 L64 98 L54 66Z" fill="#E8304A" {W(2.4)}/><path d="M64 66 L74 66 L64 98 L54 66Z" fill="#8E9AAE"/>'
    f'<path d="M64 34 L74 66 L64 98 L54 66Z" fill="none" {W(2.4)}/>'
    f'<path d="M64 28 V32 M64 100 V104 M26 66 H30 M98 66 H102" {W(3)}/>' + eye(52, 56, 0.6) + eye(76, 56, 0.6))
# дракончик
add("drakosha-chekhov", "teal",
    f'<path d="M40 104 Q30 70 44 52 Q56 38 76 44 Q96 52 92 80 Q90 100 78 106Z" fill="#7CD26E" {s()}/>'
    f'<path d="M78 104 Q104 110 112 92 Q116 82 108 78" fill="none" stroke="#7CD26E" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M78 104 Q104 110 112 92 Q116 82 108 78" fill="none" {W(2)}/>'
    f'<path d="M50 46 L48 30 L58 40 L62 26 L68 40 L76 30 L76 46" fill="#FFAE6B" {W(2.4)}/>'
    f'<path d="M36 70 Q14 56 20 40 Q32 52 42 58Z" fill="#B9E8A8" {W(2.4)}/>'
    f'<ellipse cx="64" cy="90" rx="16" ry="12" fill="#E4F7C8" {W(2)}/>' + f(62, 64, d=9, k=0.75))
# кресло кинозала
add("mori-cinema-mytishchi", "night",
    f'<path d="M30 30 Q30 18 44 18 H84 Q98 18 98 30 V80 H30Z" fill="#E8304A" {s()}/>'
    f'<path d="M44 26 V74 M64 26 V74 M84 26 V74" stroke="#B8203A" stroke-width="3"/>'
    f'<rect x="22" y="76" width="84" height="20" rx="8" fill="#F2557A" {s()}/>'
    f'<rect x="14" y="56" width="14" height="40" rx="6" fill="#B8203A" {s()}/><rect x="100" y="56" width="14" height="40" rx="6" fill="#B8203A" {s()}/>'
    f'<path d="M40 96 V114 M88 96 V114" {W(6)}/>' + f(64, 48, d=10, k=0.8)
    + sparkle(110, 20, 5, "#FFD25E") + sparkle(18, 22, 4, "#FFD25E"))
# садовая лейка с буквой «М»
add("metro-na-dache", "green",
    f'<path d="M30 50 H86 L82 108 H34Z" fill="#8E9AAE" {s()}/>'
    f'<path d="M86 60 L114 36" stroke="#8E9AAE" stroke-width="10" stroke-linecap="round"/><path d="M86 60 L114 36" {W(2)}/>'
    f'<path d="M108 30 L120 42 L116 26Z" fill="#8E9AAE" {W(2.4)}/>'
    f'<path d="M36 50 Q58 22 80 50" fill="none" {W(5)}/>'
    f'<path d="M44 92 V68 L58 84 L72 68 V92" fill="none" stroke="#E8304A" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>'
    f'<path d="M118 50 L122 60 M112 54 L114 64" stroke="#6CC0F2" stroke-width="4" stroke-linecap="round"/>' + eye(48, 60, 0.55) + eye(68, 60, 0.55))
# корона над крошечным домиком
add("tsar-maket", "yellow",
    f'<path d="M30 64 L64 36 L98 64 V106 H30Z" fill="#FFAE6B" {s()}/>'
    f'<rect x="56" y="80" width="16" height="26" rx="3" fill="#7A4A2A" {s()}/>'
    f'<rect x="38" y="70" width="12" height="12" fill="#C9EEFF" {W(2)}/><rect x="78" y="70" width="12" height="12" fill="#C9EEFF" {W(2)}/>'
    f'<path d="M40 30 L46 10 L56 22 L64 6 L72 22 L82 10 L88 30Z" fill="#FFD25E" {s()}/>'
    f'<circle cx="64" cy="18" r="3" fill="#E8304A"/>' + f(64, 58, d=7, k=0.55)
    + f'<path d="M10 112 H118" {W(4)}/>')
# гвоздика с лентой
frill = "".join(f'<circle cx="{64+22*__import__("math").cos(i*0.785)}" cy="{40+16*__import__("math").sin(i*0.785)}" r="12" fill="#E8304A" {s()}/>' for i in range(8))
add("mk-zoya", "sky",
    f'<path d="M64 120 Q60 90 64 56" fill="none" stroke="#4F8A3A" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M62 92 Q44 84 40 70 Q56 74 62 86Z" fill="#7CD26E" {W(2)}/>'
    f'<path d="M56 58 L64 70 L72 58Z" fill="#7CD26E" {W(2)}/>' + frill
    + f'<circle cx="64" cy="40" r="16" fill="#F2557A" {s()}/><circle cx="64" cy="40" r="7" fill="#FF8FA8"/>'
    f'<path d="M50 102 L78 102 L72 114 L64 106 L56 114Z" fill="#FF8A3A" {W(2)}/>'
    f'<path d="M50 102 H78" stroke="#3B3355" stroke-width="5"/>' + sparkle(104, 90, 5) + sparkle(24, 96, 4))
# мятный леденец-завиток
add("minty-elephant", "green",
    f'<circle cx="64" cy="58" r="40" fill="#fff" {s()}/>'
    + "".join(f'<path d="M64 58 L{64+40*__import__("math").cos(a)} {58+40*__import__("math").sin(a)} A40 40 0 0 1 {64+40*__import__("math").cos(a+0.52)} {58+40*__import__("math").sin(a+0.52)}Z" fill="#5CCDBA"/>' for a in [i*1.047 for i in range(6)])
    + f'<circle cx="64" cy="58" r="40" fill="none" {s()}/>'
    f'<rect x="59" y="96" width="10" height="28" rx="5" fill="#FFF3D6" {s()}/>' + f(64, 58, d=10, k=0.8)
    + sparkle(110, 24, 6) + sparkle(18, 100, 5))
# шляпа с пером
add("ato-theatre", "purple",
    f'<ellipse cx="64" cy="88" rx="54" ry="16" fill="#3E4AA0" {s()}/>'
    f'<path d="M34 86 Q30 42 64 40 Q98 42 94 86Z" fill="#3E4AA0" {s()}/>'
    f'<path d="M36 76 Q64 84 92 76 L93 84 Q64 92 35 84Z" fill="#FFD25E" {W(2)}/>'
    f'<path d="M84 74 Q110 46 104 14 Q94 40 80 50 Q88 32 82 18 Q76 44 78 70Z" fill="#F2557A" {W(2.4)}/>'
    f'<path d="M80 72 Q92 44 102 18" fill="none" {W(1.6)}/>' + f(56, 62, d=8, k=0.65))
# божья коровка на листе
add("ecobiocentre", "yellow",
    f'<path d="M14 100 Q20 30 104 18 Q110 96 14 100Z" fill="#7CD26E" {s()}/>'
    f'<path d="M14 100 Q56 62 104 18" fill="none" stroke="#4F8A3A" stroke-width="3"/>'
    f'<circle cx="64" cy="64" r="26" fill="#E8304A" {s()}/><path d="M64 38 V90" {W(2.4)}/>'
    f'<circle cx="52" cy="58" r="5" fill="{O}"/><circle cx="76" cy="58" r="5" fill="{O}"/><circle cx="54" cy="76" r="4" fill="{O}"/><circle cx="74" cy="76" r="4" fill="{O}"/>'
    f'<path d="M48 44 Q52 30 64 30 Q76 30 80 44Z" fill="{O}"/>'
    f'<path d="M56 32 L48 20 M72 32 L80 20" {W(2.4)}/><circle cx="48" cy="20" r="3" fill="{O}"/><circle cx="80" cy="20" r="3" fill="{O}"/>'
    + eye(57, 38, 0.45) + eye(71, 38, 0.45))
# голова зебры
stripes = "".join(f'<path d="M{x} 30 Q{x+6} 50 {x} 66" fill="none" stroke="{O}" stroke-width="5" stroke-linecap="round"/>' for x in (46, 60, 74))
add("safari-park-mozhaysk", "orange",
    f'<path d="M40 30 L32 10 L52 24Z M88 30 L96 10 L76 24Z" fill="#fff" {s()}/>'
    f'<path d="M64 20 Q96 22 94 62 Q92 92 80 106 Q64 116 48 106 Q36 92 34 62 Q32 22 64 20Z" fill="#fff" {s()}/>' + stripes
    + f'<path d="M58 14 Q64 4 70 14 L70 30 H58Z" fill="{O}"/>'
    f'<ellipse cx="64" cy="98" rx="20" ry="14" fill="#C8B9D8" {s()}/><ellipse cx="57" cy="98" rx="3" ry="4" fill="{O}"/><ellipse cx="71" cy="98" rx="3" ry="4" fill="{O}"/>'
    + eye(50, 70, 0.9) + eye(78, 70, 0.9))


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    places = json.load(open(os.path.join(here, "..", "places.json")))["places"]
    ids = [p["id"] for p in places[721:]]
    assert set(ids) == set(R), (set(ids) - set(R), set(R) - set(ids))
    for pid in ids:
        bg, body = R[pid]
        open(os.path.join(here, "..", "icons-src", f"{pid}.svg"), "w").write(svg(bg, body))
    print(len(ids))
