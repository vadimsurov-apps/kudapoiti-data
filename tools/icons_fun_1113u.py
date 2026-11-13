"""Иконки робота fun (2026-11-13, проход u): места из tools/add_fun_1113u.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1113u.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Грачёвский парк — на территории «старейшее дерево Москвы»: седой дед-дерево и росток-внучок
I["fun-grachevsky-park"] = ("#E9F7D8", "#8CCB6A",
    "седое дерево-долгожитель с бровями-кустиками, морщинками на коре и тростью-сучком",
    "рядом из травы пробился крошечный росток-внучок с двумя листиками и тянется к нему ростом",
    # трава
    f'<path d="M-4 112 Q30 100 64 106 Q100 100 132 110 L132 132 L-4 132Z" fill="#5FB548" {W(3)}/>'
    # ствол
    f'<path d="M40 112 Q46 84 44 62 L80 62 Q78 86 86 112Z" fill="#9A6A44" {W(3)}/>'
    f'<path d="M50 104 q4 -8 0 -16 M74 100 q-4 -10 0 -18" fill="none" stroke="#6E4A2E" stroke-width="2.4" stroke-linecap="round"/>'
    # крона — седая, серо-зелёная
    f'<path d="M14 58 Q8 36 28 30 Q32 10 56 14 Q70 4 86 16 Q110 14 112 36 Q124 50 108 64 Q96 74 80 66 Q64 76 48 66 Q24 74 14 58Z" fill="#9FBF8A" {W(3)}/>'
    f'<path d="M34 40 q6 -6 12 0 M70 30 q6 -6 12 0 M90 48 q6 -6 12 0" fill="none" stroke="#7FA06C" stroke-width="2.4" stroke-linecap="round"/>'
    # брови-кустики и лицо на стволе
    f'<path d="M46 74 q6 -6 12 -1 M66 73 q6 -5 12 1" fill="none" stroke="#E8E8E0" stroke-width="4" stroke-linecap="round"/>'
    + eye(52, 80, 0.7) + eye(72, 80, 0.7)
    + f'<path d="M56 90 Q62 95 68 90" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    # трость-сучок
    f'<path d="M88 84 L100 112" stroke="#6E4A2E" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M84 80 Q90 76 94 82" fill="none" stroke="#6E4A2E" stroke-width="5" stroke-linecap="round"/>'
    # росток-внучок
    f'<path d="M24 108 L24 92" stroke="#3E8E2E" stroke-width="3" stroke-linecap="round"/>'
    f'<path d="M24 94 Q14 84 10 92 Q16 98 24 94Z M24 92 Q32 80 38 88 Q32 96 24 92Z" fill="#7EE05A" {W(2)}/>'
    + eye(21, 101, 0.45) + eye(27, 101, 0.45)
    + sparkle(112, 88, 4, "#FFF6A8"))

# 2. Парк «Торфянка» — пирс и смотровая площадка у пруда: деревянный пирс с удочкой
I["fun-park-torfyanka"] = ("#DDF3FF", "#5EB3E6",
    "деревянный пирс на сваях с мордашкой на крайней доске",
    "вытянулся над голубым прудом, с него свешивается удочка с красным поплавком, по воде расходятся круги",
    # вода
    f'<rect x="-4" y="74" width="136" height="60" fill="#3E9AD6"/>'
    f'<path d="M-4 74 Q16 70 32 74 Q48 78 64 74 Q80 70 96 74 Q112 78 132 74" fill="none" stroke="#BFE6FF" stroke-width="3"/>'
    # берег слева
    f'<path d="M-4 66 Q14 62 26 70 L26 80 L-4 82Z" fill="#7CC560" {W(3)}/>'
    # сваи
    + "".join(f'<rect x="{x}" y="70" width="7" height="30" fill="#7A5236" {W(2.4)}/>' for x in (34, 58, 82))
    # настил пирса — в перспективе
    + f'<path d="M14 62 L100 54 L104 66 L14 74Z" fill="#C88A55" {W(3)}/>'
    + "".join(f'<path d="M{x} {74 - (x-14)*0.13:.1f} L{x+2} {62 - (x-14)*0.093:.1f}" stroke="#8C5A34" stroke-width="2"/>' for x in (32, 50, 68, 86))
    # мордашка на крайней доске
    + eye(92, 61, 0.55) + eye(100, 60, 0.55)
    + f'<path d="M93 65 q3 2 6 0" fill="none" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>'
    # удочка
    f'<path d="M70 58 L112 26" stroke="#5B3A22" stroke-width="3.4" stroke-linecap="round"/>'
    f'<path d="M112 26 Q118 54 114 86" fill="none" stroke="#fff" stroke-width="1.6"/>'
    f'<ellipse cx="114" cy="90" rx="5" ry="6" fill="#F04A3A" {W(2)}/><path d="M109 90 H119" stroke="#fff" stroke-width="2"/>'
    f'<ellipse cx="114" cy="96" rx="12" ry="3" fill="none" stroke="#BFE6FF" stroke-width="2"/>'
    f'<ellipse cx="114" cy="97" rx="20" ry="5" fill="none" stroke="#BFE6FF" stroke-width="1.6" opacity=".7"/>'
    # камыш
    f'<path d="M8 82 L6 50 M14 82 L16 54" stroke="#4E8B33" stroke-width="2.6"/>'
    f'<rect x="3" y="46" width="6" height="14" rx="3" fill="#8A5A30"/><rect x="13" y="50" width="6" height="12" rx="3" fill="#8A5A30"/>'
    + sparkle(36, 26, 6, "#fff") + sparkle(60, 100, 3, "#fff"))

# 3. Милютинский сад — маленький сад с детской площадкой и настольным теннисом: стриженый куст в кадке
I["fun-milyutinsky-sad"] = ("#FFF0DA", "#F2B36B",
    "куст-топиарий, подстриженный тремя шарами, в деревянной кадке",
    "держит на макушке белый шарик для настольного тенниса у дорожки маленького городского сада",
    # дорожка
    f'<path d="M30 132 L52 96 L76 96 L98 132Z" fill="#F7DDB5" {W(2.6)}/>'
    # кадка
    f'<path d="M40 92 L88 92 L82 118 L46 118Z" fill="#B0703F" {W(3)}/>'
    f'<path d="M42 100 H86 M44 110 H84" stroke="#7E4C26" stroke-width="2.4"/>'
    # стволик
    f'<path d="M64 92 V30" stroke="#7E4C26" stroke-width="4"/>'
    # три шара
    f'<circle cx="64" cy="78" r="17" fill="#4FAE48" {W(3)}/>'
    f'<circle cx="64" cy="50" r="13" fill="#5CC152" {W(3)}/>'
    f'<circle cx="64" cy="28" r="9" fill="#6AD15E" {W(3)}/>'
    + eye(57, 76, 0.75) + eye(71, 76, 0.75)
    + f'<path d="M58 84 Q64 89 70 84" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    f'<ellipse cx="52" cy="82" rx="3.6" ry="2" fill="#FF7FA8" opacity=".6"/><ellipse cx="76" cy="82" rx="3.6" ry="2" fill="#FF7FA8" opacity=".6"/>'
    # шарик для пинг-понга на макушке
    f'<circle cx="64" cy="13" r="6" fill="#fff" {W(2.4)}/>'
    + sparkle(64, 13, 0, "#fff")
    # ракетка для настольного тенниса у кадки
    + f'<circle cx="104" cy="98" r="11" fill="#E8473C" {W(2.6)}/><rect x="101" y="107" width="6" height="14" rx="2" fill="#C98B4A" {W(2.4)}/>'
    + sparkle(24, 40, 5, "#fff") + sparkle(102, 36, 4, "#fff"))

# 4. «Лаки Лама» в Истре — семейный парк с горками и сухим бассейном: радужная горка
I["fun-lucky-lama-istra"] = ("#E8F0FF", "#8EA6F0",
    "радужная пластиковая горка с мордашкой на верхней площадке",
    "с неё друг за другом съезжают в сухой бассейн три шарика — красный, синий и жёлтый",
    # сухой бассейн
    f'<rect x="56" y="96" width="76" height="40" rx="6" fill="#FFFFFF" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}" {W(1.8)}/>' for x, y, c in
              ((64, 104, "#FF5A4E"), (78, 102, "#3FA0FF"), (92, 104, "#FFD23F"), (106, 102, "#5CCB5F"), (120, 104, "#FF8FC8"),
               (70, 114, "#FFD23F"), (86, 114, "#FF5A4E"), (100, 114, "#3FA0FF"), (114, 114, "#9B6BFF")))
    # площадка и лесенка
    + f'<rect x="10" y="36" width="34" height="14" rx="3" fill="#FFB341" {W(3)}/>'
    f'<path d="M14 50 L14 120 M38 50 L38 120" stroke="{O}" stroke-width="3.2"/>'
    + "".join(f'<path d="M14 {y} H38" stroke="{O}" stroke-width="2.6"/>' for y in (64, 78, 92, 106))
    # горка-радуга
    + f'<path d="M40 40 Q86 46 100 96" fill="none" stroke="{O}" stroke-width="26" stroke-linecap="round"/>'
    f'<path d="M40 40 Q86 46 100 96" fill="none" stroke="#FF5A4E" stroke-width="20" stroke-linecap="round"/>'
    f'<path d="M40 40 Q86 46 100 96" fill="none" stroke="#FFD23F" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M40 40 Q86 46 100 96" fill="none" stroke="#3FA0FF" stroke-width="5" stroke-linecap="round"/>'
    # мордашка на площадке
    + eye(21, 43, 0.55) + eye(32, 43, 0.55)
    + f'<path d="M23 47 q4 2.5 8 0" fill="none" stroke="{O}" stroke-width="1.8" stroke-linecap="round"/>'
    # три шарика на горке
    f'<circle cx="62" cy="36" r="6" fill="#FF5A4E" {W(2)}/>'
    f'<circle cx="80" cy="50" r="6" fill="#3FA0FF" {W(2)}/>'
    f'<circle cx="92" cy="68" r="6" fill="#FFD23F" {W(2)}/>'
    + sparkle(110, 26, 5, "#fff") + sparkle(66, 18, 3, "#fff"))

# 5. Клуб «Джунгли» (Нахабино-Ясное) — игровой центр с лабиринтом и батутом: красноглазая квакша
I["fun-dzhungli-nakhabino-yasnoe"] = ("#D6F5D0", "#3FA36A",
    "красноглазая древесная квакша с оранжевыми лапками-присосками",
    "прилипла к стволу пальмы над сеткой батута и весело показывает язык",
    # батут внизу
    f'<ellipse cx="64" cy="114" rx="50" ry="10" fill="#2B2F55" {W(3)}/>'
    f'<ellipse cx="64" cy="112" rx="40" ry="6" fill="#4A56B8"/>'
    f'<path d="M20 116 L16 132 M108 116 L112 132" stroke="{O}" stroke-width="3.2"/>'
    # ствол пальмы
    f'<path d="M80 108 Q74 70 82 24" fill="none" stroke="{O}" stroke-width="17" stroke-linecap="round"/>'
    f'<path d="M80 108 Q74 70 82 24" fill="none" stroke="#B9875A" stroke-width="11" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x-6} {y} q6 4 12 0" fill="none" stroke="#8A5E38" stroke-width="2"/>' for x, y in ((79, 96), (77, 82), (77, 68), (78, 54), (80, 40)))
    # листья пальмы
    + f'<path d="M82 24 Q58 6 30 18 Q58 18 82 26Z M82 24 Q104 4 126 16 Q102 18 82 26Z M82 24 Q96 34 112 50 Q92 36 80 28Z M82 24 Q64 30 52 46 Q68 32 82 28Z" fill="#4CC24A" {W(2.6)}/>'
    # квакша — прилипла к стволу слева
    f'<ellipse cx="62" cy="66" rx="17" ry="14" fill="#5BD65A" {W(3)}/>'
    f'<path d="M50 70 Q48 76 56 76" fill="#3B7FE0" {W(2)}/>'
    # глаза красные навыкате
    f'<circle cx="54" cy="54" r="7.5" fill="#E8333A" {W(2.6)}/><circle cx="70" cy="54" r="7.5" fill="#E8333A" {W(2.6)}/>'
    f'<ellipse cx="54" cy="54" rx="2.2" ry="4" fill="{O}"/><ellipse cx="70" cy="54" rx="2.2" ry="4" fill="{O}"/>'
    f'<circle cx="52.5" cy="51.5" r="1.4" fill="#fff"/><circle cx="68.5" cy="51.5" r="1.4" fill="#fff"/>'
    # рот и язык
    f'<path d="M54 68 Q62 74 70 68" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>'
    f'<path d="M62 71 Q60 80 64 82 Q68 80 66 72Z" fill="#FF7FA8" {W(1.8)}/>'
    # лапки-присоски на стволе
    + "".join(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#5BD65A" stroke-width="4.5" stroke-linecap="round"/>'
              f'<circle cx="{x2}" cy="{y2}" r="3.6" fill="#FF9A2E" {W(1.6)}/>'
              for x1, y1, x2, y2 in ((74, 60, 78, 50), (74, 74, 78, 84), (50, 60, 42, 52), (52, 76, 44, 86)))
    + sparkle(22, 40, 5, "#FFF6A8") + sparkle(112, 88, 4, "#fff"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
