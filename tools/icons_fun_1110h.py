"""Иконки робота fun (2026-11-10, дневной проход 3, часть 2): литературные музеи и театр из tools/add_fun_1110h.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя палитра фона.
Запуск: python3 tools/icons_fun_1110h.py"""
import os
from draw_icons import s, face, sparkle, eye, O
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# Дом Остроухова в Трубниках — коллекционер картин
I["ostroukhov-house-trubniki"] = ("#FFF4E0", "#B9863A",
    "золочёная резная рама картины с мордашкой на верхнем завитке",
    "висит на стене и держит в себе весенний пейзаж с берёзками и речкой, как открытое окошко, и подмигивает",
    f'<g transform="translate(0 8)"><rect x="20" y="24" width="88" height="80" rx="6" fill="#E3B23C" {W(3.2)}/>'
    f'<rect x="32" y="36" width="64" height="56" fill="#BFE3F5" {W(2.6)}/>'
    f'<path d="M32 74 Q50 66 64 72 Q80 78 96 70 V92 H32Z" fill="#8CCB6A"/>'
    f'<path d="M32 84 Q60 78 96 86" fill="none" stroke="#5FA8D8" stroke-width="4"/>'
    + "".join(f'<path d="M{x} 74 V48" stroke="#fff" stroke-width="3"/><path d="M{x} 50 V72" stroke="{O}" stroke-width="1" stroke-dasharray="2 4"/>'
              f'<ellipse cx="{x}" cy="50" rx="6" ry="9" fill="#A6D86A" opacity=".9"/>' for x in (44, 54, 84)) +
    f'<rect x="32" y="36" width="64" height="56" fill="none" {W(2.6)}/>'
    f'<path d="M48 24 Q64 4 80 24Z" fill="#E3B23C" {W(2.8)}/>'
    f'<path d="M56 16 Q58 19 60 16" fill="none" {W(2)}/>' + eye(68, 15, 0.45) +
    f'<circle cx="20" cy="24" r="6" fill="#F2C85A" {W(2.2)}/><circle cx="108" cy="24" r="6" fill="#F2C85A" {W(2.2)}/>'
    f'<circle cx="20" cy="104" r="6" fill="#F2C85A" {W(2.2)}/><circle cx="108" cy="104" r="6" fill="#F2C85A" {W(2.2)}/>'
    + '</g>' + sparkle(112, 60, 5) + sparkle(14, 64, 4))

# Музей Серебряного века (дом Брюсова) — пишущая машинка
I["silver-age-museum-mira"] = ("#EEF0F7", "#7D86A8",
    "чёрная старинная пишущая машинка с круглыми серебряными клавишами и мордашкой на корпусе",
    "сама печатает стихи: лист выезжает вверх со строчками, а над ним рассыпаются серебряные звёздочки",
    f'<path d="M40 14 H88 V60 H40Z" fill="#FFFFFF" {W(2.6)}/>'
    + "".join(f'<path d="M46 {22+i*8} H{82-(i%2)*10}" stroke="#7D86A8" stroke-width="2.4"/>' for i in range(5)) +
    f'<rect x="26" y="56" width="76" height="12" rx="6" fill="#3A3A48" {W(2.8)}/>'
    f'<circle cx="22" cy="62" r="6" fill="#C9CEDD" {W(2.4)}/><circle cx="106" cy="62" r="6" fill="#C9CEDD" {W(2.4)}/>'
    f'<path d="M18 112 L28 70 H100 L110 112Z" fill="#2E2E3A" {W(3.2)}/>'
    + "".join(f'<circle cx="{34+i*10}" cy="{98}" r="4" fill="#DADFEA" {W(1.6)}/>' for i in range(7)) +
    "".join(f'<circle cx="{39+i*10}" cy="{88}" r="3.6" fill="#DADFEA" {W(1.6)}/>' for i in range(6)) +
    f'<rect x="46" y="72" width="36" height="12" rx="4" fill="#C9CEDD" {W(2)}/>' + face(64, 77, d=8, k=0.5, mouth=False, blush=False)
    + sparkle(100, 20, 6, "#E6E9F5") + sparkle(26, 30, 5, "#E6E9F5") + sparkle(108, 40, 3.5, "#E6E9F5"))

# Московский дом Достоевского — самовар
I["dostoevsky-house-moscow"] = ("#FFF0E6", "#C0603A",
    "пузатый медный самовар с мордашкой и чайником-короной на макушке",
    "пыхтит паром на круглом столе с вязаной салфеткой, а рядом лежит раскрытая старинная книга с закладкой",
    f'<ellipse cx="64" cy="112" rx="56" ry="12" fill="#7A4A30" {W(3)}/>'
    f'<path d="M30 108 Q64 98 98 108" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 3"/>'
    f'<path d="M50 108 L46 98 H82 L78 108Z" fill="#B8662E" {W(2.6)}/>'
    f'<path d="M40 96 Q34 64 46 50 H82 Q94 64 88 96Z" fill="#D9843A" {W(3.2)}/>'
    f'<path d="M48 58 Q44 76 48 92" fill="none" stroke="#F6C27A" stroke-width="4"/>'
    f'<path d="M40 64 Q28 64 30 78 M88 64 Q100 64 98 78" fill="none" stroke="#8A4A20" stroke-width="5" stroke-linecap="round"/>'
    + face(64, 72, d=9, k=0.75) +
    f'<path d="M86 84 H100 V90 H94" fill="none" stroke="#8A4A20" stroke-width="4"/>'
    f'<path d="M52 50 Q52 40 64 40 Q76 40 76 50Z" fill="#C04A4A" {W(2.6)}/>'
    f'<path d="M58 40 Q58 30 64 30 Q70 30 70 40Z" fill="#E8D7A0" {W(2.4)}/>'
    f'<path d="M64 26 Q58 18 64 12 Q70 6 64 0" fill="none" stroke="#fff" stroke-width="4" opacity=".85"/>'
    f'<path d="M10 104 L24 92 L40 100 L26 112Z" fill="#FFF8E8" {W(2.2)}/><path d="M22 96 L30 100" stroke="#B9AFA0" stroke-width="1.6"/>'
    f'<path d="M28 108 L30 118" stroke="#C04A4A" stroke-width="3"/>' + sparkle(106, 30, 5))

# Дом-музей Герцена — колокол
I["herzen-house-museum"] = ("#E8F4FB", "#3F7FA8",
    "бронзовый колокол с мордашкой и узорным пояском",
    "раскачивается на деревянной перекладине и звонит, а из-под него разлетаются газетные листки с надписью «Колокол»",
    f'<path d="M14 18 H114" stroke="#7A4E2C" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M22 18 V40 M106 18 V40" stroke="#7A4E2C" stroke-width="6"/>'
    f'<g transform="rotate(-12 64 22)">'
    f'<path d="M64 22 V30" stroke="{O}" stroke-width="4"/>'
    f'<path d="M36 86 Q38 40 64 30 Q90 40 92 86 Q64 94 36 86Z" fill="#C98B3A" {W(3.2)}/>'
    f'<path d="M40 74 Q64 80 88 74" fill="none" stroke="#8E5A20" stroke-width="3"/>'
    f'<path d="M44 46 Q46 60 44 70" fill="none" stroke="#F0C27A" stroke-width="4"/>'
    + face(64, 56, d=8, k=0.7) +
    f'<circle cx="64" cy="96" r="6" fill="#8E5A20" {W(2.4)}/></g>'
    f'<path d="M20 104 L40 96 L44 112 L24 120Z" fill="#FFFFFF" {W(2)}/><path d="M26 104 L38 100 M27 109 L40 104" stroke="#7D8C99" stroke-width="1.6"/>'
    f'<path d="M84 104 L106 100 L108 116 L86 120Z" fill="#FFFFFF" {W(2)}/><path d="M90 106 L102 104 M90 111 L104 109" stroke="#7D8C99" stroke-width="1.6"/>'
    f'<path d="M104 54 Q112 50 116 56 M108 64 Q118 62 120 70 M24 54 Q16 50 12 56" fill="none" stroke="#fff" stroke-width="3"/>')

# Дом-музей Есенина — гармонь-тальянка
I["esenin-house-strochenovsky"] = ("#FFF0F0", "#C84A5A",
    "рязанская гармонь-тальянка с красными мехами и мордашкой на корпусе",
    "сама растягивает меха на завалинке деревенской избы, а из мехов вместо нот вылетают жёлтые кленовые листья",
    f'<path d="M-2 92 H130 V130 H-2Z" fill="#A8743E" {W(3)}/>'
    f'<path d="M-2 92 H130" stroke="{O}" stroke-width="3"/>'
    + "".join(f'<path d="M-2 {100+i*8} H130" stroke="#8A5A2A" stroke-width="2"/>' for i in range(3)) +
    f'<rect x="12" y="44" width="24" height="44" rx="4" fill="#3A6FC2" {W(3)}/>'
    + "".join(f'<circle cx="{20+(i%2)*8}" cy="{52+(i//2)*8}" r="2.6" fill="#fff" {W(1.2)}/>' for i in range(8)) +
    f'<rect x="92" y="44" width="24" height="44" rx="4" fill="#3A6FC2" {W(3)}/>'
    + "".join(f'<path d="M{36+i*7} 44 L{40+i*7} 50 L{36+i*7} 56 L{40+i*7} 62 L{36+i*7} 68 L{40+i*7} 74 L{36+i*7} 80 L{40+i*7} 88" fill="none" stroke="{O}" stroke-width="2"/>' for i in range(8)) +
    f'<path d="M36 44 H92 V88 H36Z" fill="#E8434A" opacity=".85"/>'
    + "".join(f'<path d="M{38+i*7} 44 V88" stroke="#B82E38" stroke-width="2.4"/>' for i in range(8)) +
    f'<rect x="36" y="44" width="56" height="44" fill="none" {W(2.6)}/>'
    + face(104, 66, d=5, k=0.5, mouth=True) +
    "".join(f'<path d="M{x} {y} l5 -6 l5 6 l-2 6 h-6Z" fill="#F2B33A" {W(1.6)}/>' for x, y in ((52, 30), (70, 20), (88, 32))) +
    sparkle(30, 20, 5))

# Театр на Покровке — сундук с реквизитом
I["theatre-na-pokrovke"] = ("#FCEBFF", "#8E3FB0",
    "старый деревянный сундук с театральным реквизитом и мордашкой на замочке",
    "распахнул крышку, а из него, как из волшебной шкатулки, выскакивают золотая корона, шпага и пёстрая шляпа с пером",
    f'<ellipse cx="64" cy="114" rx="46" ry="7" fill="#6A2A88" opacity=".5"/>'
    f'<path d="M20 70 H108 V112 H20Z" fill="#A86A3A" {W(3.2)}/>'
    f'<path d="M20 70 L26 42 H102 L108 70Z" fill="#C4864A" {W(3)} transform="rotate(-8 20 70)"/>'
    f'<path d="M20 84 H108 M20 100 H108" stroke="#7A4A22" stroke-width="3"/>'
    f'<path d="M40 70 V112 M88 70 V112" stroke="#E2B34A" stroke-width="4"/>'
    f'<rect x="54" y="78" width="20" height="18" rx="3" fill="#E2B34A" {W(2.4)}/>'
    + face(64, 85, d=4.5, k=0.45) +
    f'<path d="M30 58 L34 40 L42 50 L48 36 L54 50 L62 40 L64 58Z" fill="#F7C934" {W(2.6)}/>'
    f'<circle cx="48" cy="48" r="2.6" fill="#E8434A"/>'
    f'<path d="M74 66 L98 18" stroke="#C9D2DE" stroke-width="5" stroke-linecap="round"/><path d="M70 62 L82 70" stroke="#E2B34A" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M84 56 Q96 44 112 50 Q104 60 84 56Z" fill="#2F9E7E" {W(2.4)}/>'
    f'<path d="M100 48 Q112 30 120 34" fill="none" stroke="#E8434A" stroke-width="4" stroke-linecap="round"/>'
    + sparkle(22, 34, 5) + sparkle(64, 22, 4))

if __name__ == "__main__":
    for pid, v in I.items():
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
