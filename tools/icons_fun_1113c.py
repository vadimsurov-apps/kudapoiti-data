"""Иконки робота fun (2026-11-13, проход c): места из tools/add_fun_1113c.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1113c.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. РИО Ленинский — подогреватель бутылочек: белый стаканчик-прибор с бутылочкой внутри, пар сердечками
I["chg-trc-rio-leninsky"] = ("#E3FFF6", "#3FB59B",
    "белый электрический подогреватель для детских бутылочек с синей кнопкой-колёсиком",
    "греет торчащую из него бутылочку с молоком, а над соской поднимается пар тремя сердечками",
    # бутылочка: соска, кольцо, корпус
    f'<path d="M58 22 Q64 8 70 22Z" fill="#F7B267" {W(2.6)}/>'
    f'<rect x="52" y="22" width="24" height="9" rx="3" fill="#7C9CF2" {W(2.6)}/>'
    f'<rect x="50" y="31" width="28" height="34" rx="6" fill="#FFFBEF" {W(3)}/>'
    f'<path d="M50 44 H78" stroke="#BFD7FF" stroke-width="2"/>'
    # подогреватель
    f'<path d="M30 52 H98 L92 112 Q64 120 36 112Z" fill="#FFFFFF" {W(3.4)}/>'
    f'<path d="M30 52 H98" stroke="{O}" stroke-width="3.4"/>'
    f'<ellipse cx="64" cy="52" rx="34" ry="5" fill="#DDF3EC" {W(2.6)}/>'
    f'<circle cx="64" cy="100" r="7" fill="#3D6CE0" {W(2.6)}/><path d="M64 95 V100" stroke="#fff" stroke-width="2.2"/>'
    + face(64, 78, d=10, k=0.95)
    # пар-сердечки
    + "".join(f'<path d="M{x} {y} c-3 -4 -9 -1 -6 4 l6 6 l6 -6 c3 -5 -3 -8 -6 -4Z" fill="#FF8FB1" {W(1.8)}/>'
              for x, y in ((40, 18), (90, 12), (100, 32)))
    + sparkle(22, 70, 4, "#fff") + sparkle(110, 80, 4, "#fff"))

# 2. «Новомосковский» — пеленальный комод: верхний ящик приоткрыт, из него свисает полосатый носочек
I["chg-novomoskovsky"] = ("#F2E8FF", "#9B7FD6",
    "белый пеленальный комод с тремя круглыми ручками-пуговками и мятным матрасиком сверху",
    "приоткрыл верхний ящик, из которого свесился полосатый детский носочек, и широко улыбается",
    # матрасик
    f'<rect x="24" y="30" width="80" height="14" rx="7" fill="#9FE6CB" {W(3)}/>'
    f'<path d="M36 37 H92" stroke="#fff" stroke-width="2" stroke-dasharray="4 4"/>'
    # корпус
    f'<rect x="26" y="44" width="76" height="66" rx="5" fill="#FFFFFF" {W(3.4)}/>'
    f'<path d="M32 110 V120 M96 110 V120" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
    # ящики
    f'<rect x="30" y="70" width="68" height="17" rx="3" fill="#F5F0FF" {W(2.6)}/>'
    f'<rect x="30" y="90" width="68" height="17" rx="3" fill="#F5F0FF" {W(2.6)}/>'
    f'<rect x="24" y="48" width="80" height="18" rx="3" fill="#F5F0FF" {W(2.8)}/>'
    + "".join(f'<circle cx="64" cy="{y}" r="3.6" fill="#FFC857" {W(2)}/>' for y in (57, 78, 98))
    # носочек из верхнего ящика
    + f'<path d="M86 64 V84 Q86 92 94 92 H100 Q106 92 104 86 L98 84 V64Z" fill="#FF8A8A" {W(2.6)}/>'
    f'<path d="M86 70 H98 M86 77 H98" stroke="#fff" stroke-width="3"/>'
    + eye(50, 80, 0.9) + eye(76, 80, 0.9)
    + f'<path d="M54 96 Q63 104 72 96" fill="none" stroke="{O}" stroke-width="2.8" stroke-linecap="round"/>'
    + sparkle(14, 40, 5, "#fff") + sparkle(114, 50, 4, "#fff"))

# 3. «Гранд» Химки — настенная откидная пеленальная станция на кафельной стене
I["chg-grand-khimki"] = ("#E6F3FF", "#7FB2E5",
    "серая настенная откидная пеленальная станция с пиктограммой малыша и ремешком-пряжкой",
    "откинута, как столик в поезде, от голубой кафельной стены туалета и гостеприимно подставила полку",
    # кафель
    "".join(f'<path d="M0 {y} H128" stroke="#C7E0F7" stroke-width="2"/>' for y in (20, 44, 68, 92, 116))
    + "".join(f'<path d="M{x} 0 V128" stroke="#C7E0F7" stroke-width="2"/>' for x in (24, 52, 80, 108))
    # корпус на стене (вид спереди: верхняя часть-короб + откинутая полка в перспективе)
    + f'<rect x="30" y="18" width="68" height="42" rx="8" fill="#B9BCC6" {W(3.2)}/>'
    f'<circle cx="64" cy="34" r="6" fill="#FFFFFF" {W(2)}/><path d="M56 48 Q64 40 72 48Z" fill="#FFFFFF" {W(2)}/>'
    f'<path d="M30 60 L14 98 H114 L98 60Z" fill="#D9DCE3" {W(3.2)}/>'
    f'<path d="M22 98 L28 104 H100 L106 98" fill="#B9BCC6" {W(2.6)}/>'
    # ремешок с пряжкой
    f'<path d="M24 82 H104" stroke="#3D8BFF" stroke-width="5"/>'
    f'<rect x="58" y="76" width="12" height="12" rx="2" fill="#FFD166" {W(2.2)}/>'
    + face(64, 70, d=10, k=0.8)
    + sparkle(112, 30, 5, "#fff") + sparkle(16, 34, 4, "#fff"))

# 4. «Цветной» — букет из свёрнутых розочкой пелёнок в стеклянной вазе
I["chg-tsvetnoy"] = ("#FFF0E6", "#F29C7A",
    "букет из трёх свёрнутых розочкой пелёнок — розовой, жёлтой и голубой — с зелёными листиками",
    "стоит в высокой стеклянной вазе на полочке и подмигивает средней розочкой",
    # ваза
    f'<path d="M46 72 H82 L78 116 Q64 122 50 116Z" fill="#E7F7FF" opacity=".9" {W(3)}/>'
    f'<path d="M52 84 H76" stroke="#9AD3F0" stroke-width="2.4"/>'
    f'<rect x="20" y="116" width="88" height="8" rx="3" fill="#B07A4B" {W(2.6)}/>'
    # стебли и листики
    f'<path d="M64 74 V56 M54 74 Q50 60 40 52 M74 74 Q78 60 88 52" fill="none" stroke="#3E9C5A" stroke-width="4"/>'
    f'<path d="M58 64 q-10 -2 -12 -10 q10 0 12 10Z M70 64 q10 -2 12 -10 q-10 0 -12 10Z" fill="#6CCB7E" {W(2)}/>'
    # розочки-пелёнки (спирали)
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" {W(2.8)}/>'
              f'<path d="M{x} {y} m-{r*0.55:.1f} 0 a{r*0.55:.1f} {r*0.55:.1f} 0 1 1 {r*0.55:.1f} {r*0.55:.1f} a{r*0.3:.1f} {r*0.3:.1f} 0 1 1 -{r*0.3:.1f} -{r*0.3:.1f}" '
              f'fill="none" stroke="#fff" stroke-width="2.2" opacity=".9"/>'
              for x, y, r, c in ((38, 44, 15, "#FF9EC4"), (90, 44, 15, "#8FC8FF")))
    + f'<circle cx="64" cy="34" r="19" fill="#FFE07A" {W(3)}/>'
    f'<path d="M50 30 Q64 18 78 30" fill="none" stroke="#fff" stroke-width="2.4" opacity=".8"/>'
    + eye(57, 36, 0.85)
    + f'<path d="M67 36 q4 -3 8 0" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    f'<path d="M58 44 q6 5 12 0" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    + sparkle(112, 88, 5, "#fff") + sparkle(16, 90, 4, "#fff"))

# 5. «Форт Боярд» Бутово — золотая монета-боярд подброшена над детской ладошкой
I["fun-fort-boyard-butovo"] = ("#3E5BA8", "#14214F",
    "толстая золотая монета-боярд с выбитым силуэтом крепости и румяной мордашкой",
    "подброшена высоко над раскрытой детской ладошкой и сверкает, кувыркаясь в воздухе",
    # ладошка снизу
    f'<path d="M30 128 Q30 104 40 98 L44 84 Q46 78 51 80 L53 96 L56 76 Q58 70 63 72 L64 94 L68 74 Q71 68 75 72 L74 96 '
    f'L80 80 Q84 76 87 81 L84 104 Q90 96 96 100 Q100 104 92 114 L84 128Z" fill="#FFD3B0" {W(3)}/>'
    # дуги полёта
    f'<path d="M48 70 Q40 50 50 34 M80 70 Q90 52 80 36" fill="none" stroke="#9FB4FF" stroke-width="2.4" stroke-dasharray="3 5"/>'
    # монета
    f'<ellipse cx="64" cy="36" rx="27" ry="27" fill="#F5B82E" {W(3.4)}/>'
    f'<ellipse cx="64" cy="36" rx="20" ry="20" fill="#FFD95A" stroke="#D9951A" stroke-width="2.4"/>'
    f'<path d="M52 30 V24 H55 V27 H58 V24 H61 V27 H67 V24 H70 V27 H73 V24 H76 V30Z" fill="#D9951A"/>'
    + face(64, 40, d=9, k=0.8)
    + sparkle(20, 24, 6, "#FFF3C2") + sparkle(108, 20, 5, "#FFF3C2") + sparkle(104, 62, 4, "#fff") + sparkle(22, 64, 3.5, "#fff"))

# 6. «Ха-ха Шоу» — коробка-сюрприз, из которой на пружине выскочил хохочущий шут
I["fun-hahashow-baumanskaya"] = ("#FFF6C8", "#FFB23F",
    "красно-синяя коробка-сюрприз, из которой на пружине выскочил шут в двурогом колпаке с бубенцами",
    "шут качается на пружине и хохочет до слёз, а крышка коробки ещё подпрыгивает",
    # коробка
    f'<rect x="30" y="80" width="68" height="42" rx="4" fill="#E8463C" {W(3.4)}/>'
    f'<path d="M30 94 H98 M30 108 H98" stroke="#FFD24A" stroke-width="3"/>'
    f'<text x="64" y="104" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="12" fill="#fff">?</text>'
    f'<path d="M98 80 L118 62 L120 70 L100 86Z" fill="#3C6EE0" {W(3)}/>'
    # пружина
    f'<path d="M64 80 q-10 -3 0 -6 q10 -3 0 -6 q-10 -3 0 -6 q10 -3 0 -6" fill="none" stroke="{O}" stroke-width="3"/>'
    # голова шута
    f'<circle cx="64" cy="46" r="16" fill="#FFE2C6" {W(3)}/>'
    f'<path d="M48 40 Q40 18 26 22 Q38 30 50 36Z" fill="#3C6EE0" {W(2.6)}/><path d="M80 40 Q88 18 102 22 Q90 30 78 36Z" fill="#E8463C" {W(2.6)}/>'
    f'<path d="M48 40 Q64 26 80 40" fill="#FFD24A" {W(2.6)}/>'
    f'<circle cx="26" cy="22" r="4" fill="#FFD24A" {W(2)}/><circle cx="102" cy="22" r="4" fill="#FFD24A" {W(2)}/>'
    # хохочущее лицо: зажмуренные глаза, открытый рот, слёзки
    f'<path d="M55 45 l4 3 l-4 3 M73 45 l-4 3 l4 3" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    f'<path d="M56 54 Q64 66 72 54Z" fill="#B3263A" {W(2.2)}/>'
    f'<path d="M50 52 q-3 5 0 7 M78 52 q3 5 0 7" fill="none" stroke="#5BC0FF" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(16, 60, 5, "#fff") + sparkle(112, 100, 4, "#fff"))

# 7. «Бэнгер» — пульт ведущего с тремя кнопками-грибочками
I["fun-banger-markos-mall"] = ("#2B2F5C", "#0E1030",
    "чёрный пульт ведущего игры с тремя большими кнопками-грибочками — красной, жёлтой и синей",
    "стоит на сцене-подиуме в луче света, синяя кнопка нажата и горит, вокруг разлетаются серпантинки",
    # луч
    f'<path d="M44 0 H84 L112 128 H16Z" fill="#FFFFFF" opacity=".08"/>'
    # подиум
    f'<ellipse cx="64" cy="112" rx="50" ry="10" fill="#6A4CC2" {W(3)}/>'
    # корпус пульта
    f'<path d="M22 70 H106 L112 104 H16Z" fill="#33364A" {W(3.4)}/>'
    f'<path d="M22 70 H106" stroke="#5B6080" stroke-width="2"/>'
    # кнопки
    + "".join(f'<ellipse cx="{x}" cy="78" rx="13" ry="5" fill="#222" {W(2)}/>'
              f'<path d="M{x-11} 78 Q{x-11} {y} {x} {y} Q{x+11} {y} {x+11} 78Z" fill="{c}" {W(2.8)}/>'
              for x, y, c in ((38, 62, "#F2453D"), (64, 62, "#FFC93C")))
    + f'<ellipse cx="90" cy="78" rx="13" ry="5" fill="#222" {W(2)}/>'
    f'<path d="M79 78 Q79 70 90 70 Q101 70 101 78Z" fill="#5AB8FF" {W(2.8)}/>'
    f'<circle cx="90" cy="70" r="16" fill="#5AB8FF" opacity=".25"/>'
    + face(64, 90, d=12, k=0.85)
    # серпантинки
    + f'<path d="M86 52 q6 -8 0 -14 q-6 -6 2 -12" fill="none" stroke="#FF6FB0" stroke-width="2.6" stroke-linecap="round"/>'
    f'<path d="M100 56 q10 -4 10 -14" fill="none" stroke="#7CF29A" stroke-width="2.6" stroke-linecap="round"/>'
    f'<path d="M30 50 q-8 -6 -4 -16" fill="none" stroke="#FFC93C" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(110, 26, 4, "#fff") + sparkle(18, 28, 3.5, "#fff"))

# 8. «Нереальность» — голубой пришелец-агент в чёрном костюме держит VR-шлем
I["fun-nerealnost-gudzon"] = ("#3C3A78", "#16133A",
    "голубой пришелец-агент с одной антенной, в чёрном костюме с белой рубашкой и в тёмных очках",
    "изумлённо держит в руках VR-шлем, из линз которого вылетают фиолетовые пиксели",
    # тело-костюм
    f'<path d="M40 128 Q40 92 64 90 Q88 92 88 128Z" fill="#1C1C24" {W(3)}/>'
    f'<path d="M58 90 L64 108 L70 90Z" fill="#FFFFFF" {W(2)}/><path d="M62 96 L64 104 L66 96Z" fill="#1C1C24"/>'
    # голова
    f'<path d="M64 30 V18" stroke="{O}" stroke-width="3"/><circle cx="64" cy="16" r="5" fill="#B6FF6A" {W(2.4)}/>'
    f'<ellipse cx="64" cy="58" rx="28" ry="30" fill="#7FD6FF" {W(3.2)}/>'
    f'<path d="M40 52 H88 Q88 62 78 62 Q68 62 66 54 H62 Q60 62 50 62 Q40 62 40 52Z" fill="#14141C" {W(2.4)}/>'
    f'<path d="M46 54 L52 54" stroke="#fff" stroke-width="2" opacity=".7"/>'
    f'<ellipse cx="64" cy="76" rx="6" ry="5" fill="#2D3E6E"/>'
    # руки с VR-шлемом
    f'<rect x="78" y="94" width="40" height="22" rx="8" fill="#F2F2F7" {W(3)}/>'
    f'<circle cx="90" cy="105" r="5" fill="#4B3FA8" {W(2)}/><circle cx="106" cy="105" r="5" fill="#4B3FA8" {W(2)}/>'
    f'<path d="M84 104 Q78 100 74 104" fill="none" stroke="#7FD6FF" stroke-width="6" stroke-linecap="round"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="5" height="5" fill="#C58BFF"/>' for x, y in ((96, 84), (104, 78), (112, 86), (100, 72)))
    + sparkle(20, 24, 4, "#fff") + sparkle(106, 30, 5, "#fff") + sparkle(24, 96, 3, "#fff"))

# 9. «Три метлы» (Коломна) — три соломенные метлы-сестрички под луной
I["fun-tri-metly-kolomna"] = ("#7D5CC9", "#2C1D5C",
    "три соломенные метлы-сестрички разного роста с мордашками на вязанках прутьев",
    "стоят рядком, прислонившись к стене старого замка под жёлтой луной, средняя подмигивает",
    # луна
    f'<circle cx="98" cy="26" r="13" fill="#FFE27A" {W(2.4)}/>'
    # стена замка
    f'<path d="M0 74 H128 V128 H0Z" fill="#5A4A8A"/>'
    + "".join(f'<rect x="{x}" y="66" width="14" height="10" fill="#5A4A8A"/>' for x in (4, 34, 64, 94))
    + "".join(f'<path d="M{x} {y} H{x+16}" stroke="#4A3B78" stroke-width="2"/>' for x, y in ((8, 88), (40, 100), (80, 92), (20, 114), (90, 116)))
    # метлы: (x низа, высота древка, цвет вязанки, наклон)
    + "".join(
        f'<path d="M{x} {top} L{x+tilt} 92" stroke="#8A5A2B" stroke-width="5" stroke-linecap="round"/>'
        f'<path d="M{x+tilt-12} 122 L{x+tilt-6} 92 H{x+tilt+6} L{x+tilt+12} 122Z" fill="{c}" {W(2.8)}/>'
        f'<path d="M{x+tilt-6} 96 H{x+tilt+6}" stroke="#C0392B" stroke-width="3"/>'
        for x, top, c, tilt in ((34, 46, "#F2C36B", 0), (64, 30, "#F7D78A", 0), (94, 52, "#E9B45A", 0)))
    + eye(30, 108, 0.7) + eye(38, 108, 0.7)
    + f'<path d="M58 106 l4 2 M68 106 q2 2 4 0" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>' + eye(60, 106, 0.7)
    + eye(90, 108, 0.7) + eye(98, 108, 0.7)
    + sparkle(20, 22, 4, "#fff") + sparkle(60, 14, 3, "#fff"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
