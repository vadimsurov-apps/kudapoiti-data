"""Партия 14: места с акциями (бассейны, секции, VR, кино...). Каждая иконка — свой сюжет."""
import os, json
from draw_icons import svg, s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
WATER = f'<path d="M-4 100 Q30 90 64 100 Q98 110 132 98 V132 H-4Z" fill="#6CC0F2" {s()}/>'
R = {}
add = lambda pid, bg, body: R.__setitem__(pid, (bg, body))

# гибискус
petals = "".join(f'<ellipse cx="64" cy="34" rx="20" ry="26" fill="#F2557A" {s()} transform="rotate({a} 64 64)"/>' for a in (0, 72, 144, 216, 288))
add("fiji-kids", "teal", petals + f'<circle cx="64" cy="64" r="20" fill="#FFD25E" {s()}/>' + f(64, 64, d=8, k=0.65)
    + f'<path d="M64 84 Q70 104 62 120" fill="none" stroke="#E8304A" stroke-width="5" stroke-linecap="round"/>')
# бегемот
add("hippo-land", "purple",
    f'<ellipse cx="64" cy="58" rx="40" ry="34" fill="#B9A6E8" {s()}/><circle cx="34" cy="30" r="10" fill="#B9A6E8" {s()}/><circle cx="94" cy="30" r="10" fill="#B9A6E8" {s()}/>'
    f'<ellipse cx="64" cy="88" rx="44" ry="26" fill="#D6C9F5" {s()}/><ellipse cx="48" cy="84" rx="5" ry="7" fill="{O}"/><ellipse cx="80" cy="84" rx="5" ry="7" fill="{O}"/>'
    + eye(48, 50, 1) + eye(80, 50, 1) + f'<path d="M50 102 Q64 110 78 102" fill="none" {W(4)}/>')
# дорожный знак «дети»
add("kidway-rodionovskaya", "yellow",
    f'<path d="M64 10 L118 110 H10Z" fill="#fff" stroke="#E8304A" stroke-width="10" stroke-linejoin="round"/><path d="M64 10 L118 110 H10Z" fill="none" {W(2)}/>'
    f'<circle cx="54" cy="52" r="8" fill="{O}"/><path d="M54 60 L50 82 L42 98 M50 82 L60 98 M52 66 L40 74 M52 66 L66 72" fill="none" {W(5)}/>'
    f'<circle cx="80" cy="64" r="6" fill="{O}"/><path d="M80 70 L78 86 L72 98 M78 86 L86 98 M80 74 L68 72" fill="none" {W(4.5)}/>')
# диско-шар
tiles = "".join(f'<path d="M{x} 30 V98" stroke="#8E9AAE" stroke-width="1.6"/>' for x in (44, 64, 84)) + \
        "".join(f'<path d="M30 {y} H98" stroke="#8E9AAE" stroke-width="1.6"/>' for y in (46, 64, 82))
add("m-dance-dolgoprudny", "night",
    f'<path d="M64 4 V30" {W(3)}/><circle cx="64" cy="64" r="34" fill="#D8E1EE" {s()}/>' + tiles
    + f'<circle cx="64" cy="64" r="34" fill="none" {s()}/>' + f(64, 66, d=10, k=0.75)
    + sparkle(20, 30, 6) + sparkle(108, 40, 5) + sparkle(104, 104, 6) + sparkle(22, 100, 4))
# зиплайн
add("skypark-luzhniki", "sky",
    f'<path d="M4 20 L124 64" stroke="{O}" stroke-width="3"/><path d="M60 30 L56 48 M68 34 L64 50" {W(3)}/>'
    f'<rect x="54" y="26" width="18" height="10" rx="3" fill="#FFAE6B" {s()} transform="rotate(20 63 31)"/>'
    f'<circle cx="60" cy="62" r="13" fill="#FFE2B8" {s()}/>' + f(60, 62, d=6, k=0.55)
    + f'<path d="M50 76 Q60 72 70 76 L72 98 H48Z" fill="#7CD26E" {s()}/><path d="M52 98 L46 116 M68 98 L76 114" {W(5)}/>'
    f'<path d="M14 112 Q30 98 48 112 Q66 100 84 114" fill="none" stroke="#7CD26E" stroke-width="8" stroke-linecap="round"/>')
# вейкборд на волне
add("sportstation-kozhukhovo", "blue", WATER
    + f'<path d="M10 86 Q40 60 70 76 Q98 60 120 74" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
    + f'<g transform="rotate(-18 64 64)"><rect x="18" y="52" width="92" height="24" rx="12" fill="#FF7A3A" {s()}/>'
    + f'<rect x="42" y="56" width="12" height="16" rx="3" fill="{O}"/><rect x="74" y="56" width="12" height="16" rx="3" fill="{O}"/></g>'
    + f(64, 66, d=8, k=0.6) + sparkle(104, 24, 6))
# VR-контроллер
add("vr-mania", "purple",
    f'<circle cx="64" cy="40" r="24" fill="none" stroke="#5CCDBA" stroke-width="8"/><circle cx="64" cy="40" r="24" fill="none" {W(2.4)}/>'
    f'<path d="M52 56 L46 112 Q46 120 56 120 H72 Q82 120 82 112 L76 56Z" fill="#3E4AA0" {s()}/>'
    f'<circle cx="64" cy="72" r="6" fill="#FFD25E" {W(2)}/>' + f(64, 94, d=7, k=0.55)
    + f'<path d="M30 22 L22 14 M98 22 L106 14 M28 44 H18" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')
# вихрь-портал
add("unreal-place", "night",
    f'<path d="M64 64 m0 -6 a6 6 0 1 1 -6 6 a14 14 0 1 1 14 14 a24 24 0 1 1 -24 -24 a36 36 0 1 1 36 36" fill="none" stroke="#E6DAFF" stroke-width="10" stroke-linecap="round"/>'
    f'<path d="M64 64 m0 -6 a6 6 0 1 1 -6 6 a14 14 0 1 1 14 14 a24 24 0 1 1 -24 -24 a36 36 0 1 1 36 36" fill="none" stroke="#C86BF0" stroke-width="4" stroke-linecap="round"/>'
    + f(64, 62, d=6, k=0.55, blush=False) + sparkle(18, 22, 6) + sparkle(110, 20, 4) + sparkle(20, 110, 4))
# шапочка для плавания
add("aqua-class-alekseevskaya", "blue", WATER
    + f'<path d="M22 78 Q20 22 64 20 Q108 22 106 78Z" fill="#FFD25E" {s()}/>'
    + f'<path d="M30 78 Q64 70 98 78" fill="none" stroke="#E0A830" stroke-width="4"/>'
    + f'<circle cx="46" cy="40" r="6" fill="#fff" opacity=".7"/>' + f(64, 54, d=10, k=0.75))
# мыльные пузыри с рожицами
add("aquapups", "sky",
    f'<circle cx="50" cy="70" r="30" fill="#E4F6FF" {s()}/><circle cx="92" cy="40" r="20" fill="#E4F6FF" {s()}/><circle cx="98" cy="94" r="13" fill="#E4F6FF" {s()}/>'
    f'<path d="M34 54 Q38 46 46 44" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
    + f(50, 74, d=10, k=0.8) + f(92, 42, d=6, k=0.55) + f(98, 95, d=4, k=0.4, blush=False))
# капля воды
add("akvaroom", "teal",
    f'<path d="M64 10 Q98 56 98 78 A34 34 0 0 1 30 78 Q30 56 64 10Z" fill="#6CC0F2" {s()}/>'
    f'<path d="M44 70 Q44 54 54 42" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".7"/>'
    + f(66, 80, d=10, k=0.8) + sparkle(106, 28, 6))
# пуанты
shoe = lambda x, r: (f'<g transform="rotate({r} {x} 70)"><path d="M{x-12} 40 Q{x-14} 96 {x} 108 Q{x+14} 96 {x+12} 40 Q{x} 32 {x-12} 40Z" fill="#FFB7CE" {s()}/>'
                     f'<path d="M{x-8} 44 Q{x} 56 {x+8} 44" fill="#F58CB8" {W(2)}/></g>')
add("bolshoi-ballet-zelenograd", "pink", shoe(48, -12) + shoe(82, 12)
    + f'<path d="M40 40 Q20 20 30 8 M90 40 Q110 20 100 8 M40 40 Q64 26 90 40" fill="none" stroke="#F2557A" stroke-width="3"/>'
    + f(48, 74, d=5, k=0.5) + f(84, 74, d=5, k=0.5))
# армейская фляга
add("garnizon-a", "green",
    f'<path d="M54 14 H74 V28 H54Z" fill="#8E9AAE" {s()}/><path d="M40 34 Q64 22 88 34 Q104 52 102 80 Q98 112 64 114 Q30 112 26 80 Q24 52 40 34Z" fill="#6E8B3D" {s()}/>'
    f'<path d="M36 52 Q48 46 54 56 Q46 64 36 60Z M74 82 Q86 76 92 86 Q84 96 74 90Z M58 92 Q66 88 68 98 Q60 102 56 98Z" fill="#4F6B2A"/>'
    f'<path d="M30 56 H98" stroke="#C98A4B" stroke-width="8"/>' + f(64, 76, d=9, k=0.75))
# золотой шар боулинга
add("zolotoy-shar-krasnogorsk", "night",
    f'<path d="M96 30 Q86 50 92 70 Q100 90 92 112 H116 Q108 90 114 70 Q120 50 110 30 Q103 18 96 30Z" fill="#fff" {s()}/>'
    f'<path d="M93 52 H113" stroke="#E8304A" stroke-width="5"/>'
    f'<circle cx="52" cy="76" r="38" fill="#FFC83A" {s()}/><circle cx="40" cy="58" r="5" fill="{O}"/><circle cx="54" cy="54" r="5" fill="{O}"/><circle cx="48" cy="70" r="5" fill="{O}"/>'
    f'<path d="M26 66 Q30 50 42 44" fill="none" stroke="#FFF3A0" stroke-width="5" stroke-linecap="round"/>' + f(56, 90, d=8, k=0.65)
    + sparkle(20, 22, 6))
# хвост китёнка над водой
add("kitenok-orekhovo", "sky",
    f'<path d="M64 98 Q60 70 62 52 Q40 52 26 30 Q48 26 64 40 Q80 26 102 30 Q88 52 66 52 Q68 70 64 98Z" fill="#5C8FE0" {s()}/>'
    + WATER + f'<path d="M30 94 Q40 84 50 94 M80 96 Q90 86 100 96" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
    + f(64, 70, d=5, k=0.45, blush=False) + sparkle(18, 64, 5) + sparkle(110, 60, 4))
# голова куклы в пробирке
add("kuklab-theatre", "purple",
    f'<path d="M40 10 H88 M46 10 V96 A18 18 0 0 0 82 96 V10" fill="#E4F6FF" {s()}/>'
    f'<path d="M48 70 H80 V96 A16 16 0 0 1 48 96Z" fill="#9DF0D0"/>'
    f'<circle cx="64" cy="56" r="16" fill="#FFE2B8" {s()}/><path d="M48 50 Q50 34 64 36 Q78 34 80 50 Q72 42 64 46 Q56 42 48 50Z" fill="#E8654F" {W(2.4)}/>'
    + f(64, 60, d=6, k=0.55) + f'<path d="M46 10 V96 A18 18 0 0 0 82 96 V10" fill="none" {s()}/>' + sparkle(104, 40, 6))
# морская звезда
star = " ".join(f'{64+42*__import__("math").sin(i*3.14159/5):.0f},{66-42*__import__("math").cos(i*3.14159/5):.0f}' if i % 2 == 0 else
                f'{64+18*__import__("math").sin(i*3.14159/5):.0f},{66-18*__import__("math").cos(i*3.14159/5):.0f}' for i in range(10))
add("malysh-i-more", "blue", f'<polygon points="{star}" fill="#FF9466" stroke="{O}" stroke-width="5" stroke-linejoin="round"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.5" fill="#FFD7C2"/>' for x, y in [(64, 36), (40, 56), (88, 56), (50, 90), (78, 90)])
    + f(64, 68, d=8, k=0.65))
# нарукавники
arm = lambda x: (f'<rect x="{x}" y="26" width="34" height="76" rx="17" fill="#FF7A3A" {s()}/><rect x="{x+8}" y="34" width="18" height="60" rx="9" fill="#E4F6FF" {W(2.4)}/>'
                 f'<path d="M{x} 64 H{x+34}" stroke="#FFD25E" stroke-width="6"/>')
add("mama-ya-plyvu-preobrazhenka", "teal", arm(22) + arm(72) + f(39, 50, d=5, k=0.45, blush=False) + f(89, 50, d=5, k=0.45, blush=False)
    + f'<path d="M14 118 Q40 108 64 118 Q88 128 114 116" fill="none" stroke="#6CC0F2" stroke-width="6" stroke-linecap="round"/>')
# медвежья лапа + прицел
add("lazertag-medved", "night",
    f'<ellipse cx="60" cy="78" rx="28" ry="24" fill="#A86F3E" {s()}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="11" fill="#A86F3E" {s()}/>' for x, y in [(30, 46), (48, 34), (72, 34), (90, 46)])
    + f'<ellipse cx="60" cy="82" rx="16" ry="12" fill="#D9A06E"/>' + f(60, 80, d=7, k=0.6)
    + f'<circle cx="104" cy="98" r="14" fill="none" stroke="#FF3A5A" stroke-width="4"/><path d="M104 78 V118 M84 98 H124" stroke="#FF3A5A" stroke-width="3"/>')
# верблюд
add("mirage-maryino", "yellow",
    f'<path d="M4 108 Q40 92 70 104 Q100 92 132 106 V132 H4Z" fill="#F2C46E" {s()}/>'
    f'<path d="M24 74 Q30 44 46 58 Q56 36 70 58 Q78 66 86 54 L94 34 Q100 26 108 34 L110 42 L102 44 L96 70 Q92 82 80 84 H34 Q22 84 24 74Z" fill="#D9A06E" {s()}/>'
    f'<path d="M36 84 V106 M48 84 V106 M70 84 V106 M82 84 V104" {W(5)}/>' + eye(104, 36, 0.7)
    + f'<circle cx="22" cy="22" r="10" fill="#FFD25E" {W(2.4)}/>')
# солнце в тёмных очках с плёнкой
rays = "".join(f'<path d="M64 64 L{64+52*x:.0f} {64+52*y:.0f}" stroke="#FFAE6B" stroke-width="7" stroke-linecap="round"/>'
               for x, y in [(1, 0), (0.7, 0.7), (0, 1), (-0.7, 0.7), (-1, 0), (-0.7, -0.7), (0, -1), (0.7, -0.7)])
add("relizpark-solnechnogorsk", "sky", rays + f'<circle cx="64" cy="64" r="30" fill="#FFD25E" {s()}/>'
    + f'<path d="M38 54 H90" {W(3)}/><rect x="40" y="52" width="20" height="12" rx="5" fill="{O}"/><rect x="68" y="52" width="20" height="12" rx="5" fill="{O}"/>'
    + f'<path d="M54 76 Q64 84 74 76" fill="none" {W(3.5)}/>'
    + f'<rect x="10" y="98" width="46" height="20" rx="3" fill="{O}"/>' + "".join(f'<rect x="{x}" y="102" width="6" height="12" fill="#fff"/>' for x in (16, 28, 40)))
# куртка самбо
add("sambo-chalykh", "orange",
    f'<path d="M40 20 L64 34 L88 20 L114 40 L102 62 L92 56 V112 H36 V56 L26 62 L14 40Z" fill="#E8304A" {s()}/>'
    f'<path d="M40 20 L64 70 L88 20" fill="none" stroke="#fff" stroke-width="6"/><path d="M36 82 H92" stroke="{O}" stroke-width="8"/>'
    f'<path d="M64 82 L56 102 M64 82 L72 102" {W(5)}/>' + f(64, 52, d=6, k=0.5, blush=False))
# боксёрская груша
add("nosov-martial-arts", "pink",
    f'<path d="M64 4 V20 M50 20 L64 10 L78 20" fill="none" {W(3)}/>'
    f'<rect x="40" y="20" width="48" height="90" rx="20" fill="#C83A3A" {s()}/><path d="M40 38 H88 M40 92 H88" stroke="#8A2020" stroke-width="5"/>'
    f'<path d="M50 32 V84" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".5"/>' + f(66, 62, d=8, k=0.65)
    + f'<path d="M12 60 L24 64 M10 74 H24 M12 88 L24 84" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')
# узел чёрного пояса
add("karate-zakharov-reutov", "yellow",
    f'<path d="M6 54 H122 V74 H6Z" fill="#2E2E3A" {s()}/><path d="M54 70 L36 116 L52 116 L64 82 L76 116 L92 116 L74 70Z" fill="#2E2E3A" {s()}/>'
    f'<rect x="48" y="48" width="32" height="32" rx="8" fill="#2E2E3A" {s()}/><path d="M42 108 L36 116 M86 108 L92 116" stroke="#FFD25E" stroke-width="4"/>'
    + face(64, 64, d=7, k=0.55, blush=False).replace(O, "#fff"))
# бутса
add("schoolball-kuntsevo", "green",
    f'<path d="M24 40 Q24 30 34 30 H56 Q62 50 80 58 L108 66 Q120 70 118 84 V92 H22Z" fill="#3E4AA0" {s()}/>'
    f'<path d="M22 92 H118" {W(5)}/>' + "".join(f'<path d="M{x} 94 V104" stroke="{O}" stroke-width="6" stroke-linecap="round"/>' for x in (34, 54, 78, 100, 112))
    + f'<path d="M60 52 L70 44 M66 58 L76 50 M72 62 L82 54" stroke="#fff" stroke-width="3"/><path d="M30 70 H70" stroke="#FFD25E" stroke-width="6"/>'
    + f(42, 54, d=6, k=0.55) + sparkle(104, 28, 6))
# борцовки
hi = lambda x: (f'<path d="M{x} 20 H{x+26} V82 L{x+44} 88 Q{x+52} 92 {x+48} 104 H{x-4} V24Z" fill="#2F7FD8" {s()}/>'
                f'<path d="M{x+4} 32 H{x+22} M{x+4} 44 H{x+22} M{x+4} 56 H{x+22} M{x+4} 68 H{x+22}" stroke="#fff" stroke-width="3"/>')
add("sambo-svao", "sky", hi(14) + hi(66) + f(28, 90, d=5, k=0.45, blush=False) + f(80, 90, d=5, k=0.45, blush=False))
# розовая нудл-аркой
add("flamingo-naro-fominsk", "blue", WATER
    + f'<path d="M18 104 Q18 28 64 28 Q110 28 110 104" fill="none" stroke="{O}" stroke-width="26" stroke-linecap="round"/>'
    + f'<path d="M18 104 Q18 28 64 28 Q110 28 110 104" fill="none" stroke="#FF8FB8" stroke-width="18" stroke-linecap="round"/>'
    + f'<path d="M30 70 Q34 46 54 40" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".7"/>' + f(64, 30, d=5, k=0.45, blush=False))
# голова тигра
add("lionsland", "orange",
    f'<circle cx="30" cy="32" r="13" fill="#FF9A3A" {s()}/><circle cx="98" cy="32" r="13" fill="#FF9A3A" {s()}/>'
    f'<ellipse cx="64" cy="66" rx="46" ry="44" fill="#FF9A3A" {s()}/>'
    f'<path d="M64 22 V38 M50 26 L54 40 M78 26 L74 40 M20 62 H34 M22 76 H34 M108 62 H94 M106 76 H94" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="86" rx="22" ry="16" fill="#FFF3D6"/>' + eye(48, 60, 1) + eye(80, 60, 1)
    + f'<path d="M58 78 H70 L64 86Z" fill="{O}"/><path d="M64 86 V92 M56 94 Q64 98 72 94" fill="none" {W(3)}/>')
# свисток тренера
add("chaika-swim-school", "teal",
    f'<path d="M20 20 Q30 70 48 66" fill="none" stroke="#E8304A" stroke-width="5"/>'
    f'<path d="M40 56 H90 Q112 56 112 80 Q112 106 86 106 Q60 106 60 84 H40Z" fill="#FFD25E" {s()}/>'
    f'<rect x="30" y="54" width="14" height="32" rx="4" fill="#8E9AAE" {s()}/>' + f(88, 82, d=8, k=0.65)
    + f'<path d="M18 46 L8 40 M16 62 H4 M18 78 L8 84" stroke="#fff" stroke-width="4" stroke-linecap="round"/>')
# парящий остров
add("another-world-odintsovo", "night",
    f'<path d="M20 64 H108 L90 86 L74 110 L64 96 L52 112 L38 86Z" fill="#A86F3E" {s()}/>'
    f'<path d="M18 64 Q20 54 34 56 H96 Q110 54 110 64Z" fill="#7CD26E" {s()}/>'
    f'<path d="M80 58 V30" {W(4)}/><circle cx="80" cy="28" r="14" fill="#3E9A50" {s()}/>'
    f'<path d="M44 56 Q42 40 52 36 Q60 34 60 46 V56" fill="#FFF3D6" {W(2.4)}/>' + f(64, 76, d=6, k=0.55)
    + sparkle(22, 28, 5) + sparkle(110, 104, 5) + sparkle(30, 110, 3))


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    places = json.load(open(os.path.join(here, "..", "places.json")))["places"]
    ids = [p["id"] for p in places[691:]]
    assert set(ids) == set(R), (set(ids) - set(R), set(R) - set(ids))
    os.makedirs(os.path.join(here, "svg14"), exist_ok=True)
    for pid in ids:
        bg, body = R[pid]
        for d in ("../icons-src",):
            open(os.path.join(here, d, f"{pid}.svg"), "w").write(svg(bg, body))
    print(len(ids))
