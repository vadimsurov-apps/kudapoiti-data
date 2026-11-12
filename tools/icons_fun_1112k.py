"""Иконки робота fun (2026-11-12, проход k): места из tools/add_fun_1112k.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1112k.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Комната матери и ребёнка в парке Фили — кулер с бутылью наливает тёплую воду в бутылочку, за окном снег
I["chg-park-fili"] = ("#E3F1FF", "#7FA7D9",
    "белый офисный кулер с голубой бутылью воды на макушке и мордашкой на корпусе",
    "наливает тёплую воду из краника в детскую бутылочку для смеси, а за окошком комнатки в парке падает снег",
    # окошко со снегом
    f'<rect x="84" y="18" width="34" height="34" rx="4" fill="#2F4C8A" {W(2.6)}/>'
    f'<path d="M101 18 V52 M84 35 H118" stroke="#3B3355" stroke-width="2.4"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#fff"/>' for x, y in ((90, 24), (110, 26), (94, 44), (112, 46), (104, 30)))
    # бутыль
    + f'<path d="M40 40 Q36 18 52 14 H64 Q80 18 76 40Z" fill="#7CC8FF" fill-opacity=".85" {W(3)}/>'
    f'<path d="M46 22 Q46 32 50 38" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>'
    f'<rect x="52" y="38" width="12" height="6" fill="#4D8BFF" {W(2.2)}/>'
    # корпус
    f'<rect x="32" y="44" width="52" height="74" rx="8" fill="#FBFBFF" {W(3.2)}/>'
    + face(58, 64, d=9, k=0.85) +
    # краник и ниша
    f'<rect x="40" y="84" width="36" height="22" rx="4" fill="#DDE6F5" {W(2.4)}/>'
    f'<rect x="52" y="80" width="10" height="7" rx="2" fill="#FF6B6B" {W(2)}/>'
    f'<path d="M57 88 V94" stroke="#7CC8FF" stroke-width="3" stroke-linecap="round"/>'
    # бутылочка
    f'<path d="M53 94 h8 l1 3 h-10Z" fill="#FFB3CF" {W(1.8)}/>'
    f'<rect x="51" y="97" width="12" height="9" rx="2" fill="#fff" {W(2)}/>'
    f'<rect x="51" y="102" width="12" height="4" fill="#BDE3FF"/>'
    + sparkle(20, 70, 4, "#fff") + sparkle(100, 92, 3, "#fff"))

# 2. «Время игры» — деревянная ложка-кукла на катушке ниток
I["fun-vremya-igry-palikha"] = ("#FFF0D6", "#F0A35E",
    "деревянная ложка-кукла с нарисованным лицом, косичками из красных ниток и юбочкой из лоскута в горошек",
    "стоит на большой катушке ниток, как на сцене, и машет протянутой к ней детской ладошке",
    # катушка
    f'<rect x="34" y="94" width="56" height="10" rx="3" fill="#C98E5A" {W(2.8)}/>'
    f'<rect x="40" y="104" width="44" height="12" fill="#4D8BFF" {W(2.6)}/>'
    + "".join(f'<path d="M40 {y} H84" stroke="#2E6BE0" stroke-width="1.4"/>' for y in (108, 112))
    + f'<rect x="34" y="116" width="56" height="10" rx="3" fill="#C98E5A" {W(2.8)}/>'
    # ручка ложки
    f'<rect x="58" y="56" width="8" height="40" rx="4" fill="#E2B072" {W(2.6)}/>'
    # юбочка
    f'<path d="M48 94 L54 66 H70 L76 94Z" fill="#FF6F91" {W(2.8)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#fff"/>' for x, y in ((56, 74), (66, 72), (60, 84), (70, 86), (54, 90)))
    # голова-ложка
    + f'<ellipse cx="62" cy="38" rx="20" ry="24" fill="#E8B878" {W(3.2)}/>'
    f'<path d="M44 26 Q36 40 40 56" fill="none" stroke="#D63A3A" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M80 26 Q88 40 84 56" fill="none" stroke="#D63A3A" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M46 22 Q62 10 78 22" fill="none" stroke="#D63A3A" stroke-width="5" stroke-linecap="round"/>'
    + face(62, 40, d=8, k=0.8) +
    # машущая ручка-нитка и детская ладошка
    f'<path d="M70 70 Q84 60 88 48" fill="none" stroke="#3B3355" stroke-width="2.6" stroke-linecap="round"/>'
    f'<path d="M104 70 Q96 66 98 58 Q100 50 104 56 L106 46 Q110 44 110 50 L112 44 Q116 44 115 52 L118 48 Q122 50 118 60 Q116 70 108 74Z" fill="#FFD9B8" {W(2.4)}/>'
    + sparkle(20, 30, 4, "#fff") + sparkle(104, 24, 3, "#fff"))

# 3. Арт-Тир — круглый холст на вертушке, в который летят шарики с краской
I["fun-art-tir-krasina"] = ("#2B2340", "#0F0B1A",
    "круглый белый холст на вращающейся вертушке с мордашкой",
    "кружится, а в него со всех сторон летят разноцветные шарики с краской и разлетаются кляксами-брызгами",
    f'<rect x="58" y="96" width="12" height="22" fill="#9AA0B5" {W(2.6)}/>'
    f'<ellipse cx="64" cy="118" rx="24" ry="6" fill="#6B7189" {W(2.6)}/>'
    f'<circle cx="64" cy="62" r="36" fill="#FFFFFF" {W(3.2)}/>'
    # кляксы-спирали
    f'<path d="M64 62 Q78 46 92 56 Q84 50 74 54Z" fill="#FF3D7F"/>'
    f'<path d="M64 62 Q50 80 36 70 Q44 78 54 74Z" fill="#2EC4FF"/>'
    f'<path d="M64 62 Q80 80 76 94 Q74 84 68 76Z" fill="#FFD23F"/>'
    f'<path d="M64 62 Q46 44 52 30 Q54 42 60 50Z" fill="#6BE36B"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x, y, r, c in ((82, 40, 6, "#FF3D7F"), (88, 46, 3, "#FF3D7F"), (42, 82, 6, "#2EC4FF"), (36, 76, 3, "#2EC4FF"), (78, 88, 5, "#FFD23F"), (46, 38, 5, "#6BE36B"), (40, 44, 2.6, "#6BE36B")))
    + f'<circle cx="64" cy="62" r="36" fill="none" {W(3.2)}/>'
    + face(64, 62, d=9, k=0.8) +
    # летящие шарики с хвостами
    "".join(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{c}" stroke-width="3" stroke-dasharray="3 4" stroke-linecap="round"/>'
            f'<circle cx="{x2}" cy="{y2}" r="5" fill="{c}" {W(2)}/>'
            for x1, y1, x2, y2, c in ((6, 24, 22, 32, "#FF3D7F"), (122, 20, 106, 30, "#FFD23F"),
                                      (8, 104, 22, 96, "#6BE36B"), (124, 100, 108, 92, "#2EC4FF")))
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="{c}"/>' for x, y, c in ((30, 44, "#FF3D7F"), (100, 44, "#FFD23F"), (32, 88, "#6BE36B"), (98, 82, "#2EC4FF"))))

# 4. Дедушкин чердак — латунная переговорная труба на чердачной балке
I["fun-dedushkin-cherdak"] = ("#FBE6C4", "#B9784A",
    "латунная переговорная труба с двумя раструбами-воронками, у каждого раструба своя мордашка",
    "изогнулась дугой через деревянную балку под скатом чердачной крыши: один раструб кричит «Ау!», другой слушает, за круглым окошком — звёзды",
    # скат крыши
    f'<path d="M0 40 L64 0 L128 40" fill="none" stroke="#7A4A2A" stroke-width="8"/>'
    f'<circle cx="64" cy="28" r="10" fill="#2C3E70" {W(2.4)}/>'
    + sparkle(61, 25, 3, "#FFE14D") + sparkle(68, 32, 2, "#fff")
    # балка
    + f'<rect x="8" y="58" width="112" height="12" rx="2" fill="#A0673E" {W(2.8)}/>'
    f'<path d="M20 64 h14 M80 63 h20" stroke="#7A4A2A" stroke-width="2"/>'
    # труба
    f'<path d="M30 88 Q30 40 64 40 Q98 40 98 88" fill="none" stroke="#3B3355" stroke-width="13" stroke-linecap="round"/>'
    f'<path d="M30 88 Q30 40 64 40 Q98 40 98 88" fill="none" stroke="#E0A93A" stroke-width="7" stroke-linecap="round"/>'
    # раструбы
    f'<path d="M14 112 L24 88 H36 L46 112Z" fill="#F2C14E" {W(3)}/>'
    f'<path d="M82 112 L92 88 H104 L114 112Z" fill="#F2C14E" {W(3)}/>'
    f'<ellipse cx="30" cy="112" rx="16" ry="4" fill="#B5832A" {W(2.4)}/><ellipse cx="98" cy="112" rx="16" ry="4" fill="#B5832A" {W(2.4)}/>'
    + face(30, 100, d=5, k=0.6) + face(98, 100, d=5, k=0.6, mouth=False) +
    f'<ellipse cx="98" cy="106" rx="3" ry="2.4" fill="#3B3355"/>'
    f'<path d="M6 84 q-4 -6 2 -10 M12 78 q-3 -8 4 -12" fill="none" stroke="#3B3355" stroke-width="2.2" stroke-linecap="round"/>'
    f'<path d="M118 82 q5 -5 1 -10" fill="none" stroke="#3B3355" stroke-width="2.2" stroke-linecap="round"/>')

# 5. Дворец Впечатлений — девочка в бесконечном коридоре зеркальных рамок
I["fun-dvorets-vpechatleniy"] = ("#F6E3FF", "#7B4FD8",
    "девочка с хвостиками в оранжевой кофточке",
    "стоит перед бесконечным зеркальным коридором из уменьшающихся рамок и машет — каждое отражение в глубине машет ей в ответ",
    "".join(f'<rect x="{64-w/2}" y="{60-w/2}" width="{w}" height="{w}" rx="4" fill="{c}" {W(2.6)}/>'
            for w, c in ((104, "#C9A7FF"), (80, "#B08CFF"), (58, "#9A72F5"), (38, "#8460E6"), (22, "#6F4FD0")))
    # маленькие отражения
    + "".join(f'<circle cx="64" cy="{y}" r="{r}" fill="#FFD2B0" {W(1.4)}/><rect x="{64-r}" y="{y+r}" width="{2*r}" height="{r*1.6}" rx="{r/2}" fill="#FF9A3C" {W(1.2)}/>'
              for y, r in ((54, 2.6), (50, 4), (44, 5.6)))
    # девочка на переднем плане
    + f'<path d="M44 128 Q44 96 64 96 Q84 96 84 128Z" fill="#FF8A2A" {W(3)}/>'
    f'<circle cx="64" cy="82" r="16" fill="#FFD2B0" {W(3)}/>'
    f'<path d="M48 78 Q50 62 64 64 Q78 62 80 78 Q72 70 64 72 Q56 70 48 78Z" fill="#6B3A1E" {W(2.4)}/>'
    f'<circle cx="44" cy="74" r="6" fill="#6B3A1E" {W(2.2)}/><circle cx="84" cy="74" r="6" fill="#6B3A1E" {W(2.2)}/>'
    + face(64, 84, d=6, k=0.6) +
    f'<path d="M84 104 Q98 96 100 82" fill="none" stroke="#3B3355" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M84 104 Q98 96 100 82" fill="none" stroke="#FF8A2A" stroke-width="3.6" stroke-linecap="round"/>'
    f'<circle cx="100" cy="80" r="5" fill="#FFD2B0" {W(2.2)}/>'
    + sparkle(22, 20, 4, "#fff") + sparkle(108, 22, 3, "#fff"))

# 6. Тайны самоцветов — синий сапфир с лупой разоблачает стекляшку
I["fun-tainy-samotsvetov-stroiteley"] = ("#DFF7EE", "#2FA57A",
    "огранённый синий сапфир с мордашкой и ювелирной лупой в руке",
    "разглядывает через лупу зелёную стекляшку-подделку, которая смущённо краснеет и прячется за бархатную подушечку",
    # подушечка
    f'<path d="M64 112 Q64 92 92 92 Q122 92 120 112 Q120 124 92 124 Q64 124 64 112Z" fill="#B0263A" {W(2.8)}/>'
    # стекляшка
    f'<path d="M84 98 L92 86 L104 86 L110 98 L97 112Z" fill="#9CF0B0" fill-opacity=".85" {W(2.4)}/>'
    f'<path d="M84 98 H110 M92 86 L97 98 L104 86" fill="none" stroke="#3B3355" stroke-width="1.6"/>'
    f'<ellipse cx="92" cy="104" rx="3" ry="1.8" fill="#FF6B8A"/><ellipse cx="103" cy="104" rx="3" ry="1.8" fill="#FF6B8A"/>'
    f'<path d="M94 101 h2 M100 101 h2" stroke="#3B3355" stroke-width="2" stroke-linecap="round"/>'
    # сапфир
    f'<path d="M14 54 L28 30 L60 30 L74 54 L44 98Z" fill="#2E6BE0" {W(3.2)}/>'
    f'<path d="M14 54 H74 M28 30 L36 54 L44 30 L52 54 L60 30 M36 54 L44 98 L52 54" fill="none" stroke="#9FC4FF" stroke-width="2"/>'
    f'<path d="M14 54 L28 30 L60 30 L74 54 L44 98Z" fill="none" {W(3.2)}/>'
    + face(44, 64, d=8, k=0.75) +
    # лупа
    f'<path d="M66 66 L78 78" stroke="#3B3355" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M66 66 L78 78" stroke="#7A4A2A" stroke-width="3.6" stroke-linecap="round"/>'
    f'<circle cx="86" cy="68" r="12" fill="#E8F6FF" fill-opacity=".6" {W(3)}/>'
    f'<path d="M80 62 Q84 58 90 60" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(100, 26, 5, "#fff") + sparkle(16, 104, 3, "#fff") + sparkle(60, 16, 3, "#BFE3FF"))

# 7. Мир Какаду — арахис в скорлупке и большой клюв какаду
I["fun-mir-kakadu-tolmachevsky"] = ("#FFF7D6", "#FFB84D",
    "арахис в скорлупке с мордашкой",
    "сидит на детской ладошке и сам тянется к огромному загнутому клюву, выглядывающему сверху из-под пушистого жёлтого хохолка",
    # голова какаду с хохолком и клювом
    f'<g transform="translate(-8 12)">'
    f'<path d="M86 22 L78 2 L92 16 L94 -2 L100 16 L110 4 L106 22Z" fill="#FFE14D" {W(2.6)}/>'
    f'<circle cx="96" cy="38" r="20" fill="#FFFFFF" {W(3)}/>'
    f'<path d="M80 40 Q70 40 66 50 Q64 60 72 62 Q70 54 78 52 Q84 50 84 44Z" fill="#4A4A5A" {W(2.6)}/>'
    f'<circle cx="92" cy="32" r="3.6" fill="#3B3355"/><circle cx="91" cy="31" r="1.3" fill="#fff"/>'
    f'<ellipse cx="102" cy="44" rx="4.5" ry="2.6" fill="#FF7FA8" opacity=".6"/></g>'
    # ладошка
    f'<path d="M14 120 Q10 96 30 90 L92 86 Q102 88 98 96 Q94 100 84 100 L96 104 Q104 108 96 114 Q70 122 40 124Z" fill="#FFD9B8" {W(2.8)}/>'
    f'<path d="M60 102 Q72 104 84 100" fill="none" stroke="#3B3355" stroke-width="2" stroke-linecap="round"/>'
    # арахис
    f'<path d="M42 92 Q30 92 32 78 Q34 70 42 70 Q46 64 54 66 Q66 68 64 80 Q64 92 52 94 Q48 96 42 92Z" fill="#D9A15A" {W(3)}/>'
    f'<path d="M38 80 l4 2 M46 74 l3 3 M56 76 l3 2 M52 86 l3 2" stroke="#A86F2E" stroke-width="2" stroke-linecap="round"/>'
    + face(48, 80, d=6, k=0.6)
    + sparkle(20, 40, 4, "#fff") + sparkle(40, 22, 3, "#fff"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
