"""Иконки робота fun (2026-11-12, проход z): места из tools/add_fun_1112z.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1112z.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
O = "#3B3355"
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Пеленальная в ТРК «Шоколад» — пара вязаных пинеток на краю пеленального матрасика, шоколадный фон
I["chg-trk-shokolad-reutov"] = ("#F3E1D3", "#9B6A4C",
    "пара вязаных розовых пинеток с белыми помпонами и мордашками",
    "одна пинетка стоит на краешке мягкого пеленального матрасика, а вторая весело подпрыгнула рядом",
    # матрасик
    f'<rect x="8" y="88" width="112" height="22" rx="10" fill="#FFF4E6" {W(3)}/>'
    f'<path d="M30 92 V106 M64 92 V106 M98 92 V106" stroke="#E7CBB0" stroke-width="2.4"/>'
    # левая пинетка (стоит)
    f'<path d="M22 86 L22 58 Q22 48 34 48 L44 48 Q50 48 50 58 L50 72 Q66 72 70 80 Q72 88 62 88 L26 88 Q22 88 22 86Z" fill="#FF9EC4" {W(3)}/>'
    f'<path d="M22 60 H50" stroke="{O}" stroke-width="2.4"/>'
    + "".join(f'<path d="M{x} 50 V58" stroke="#E46E9E" stroke-width="2"/>' for x in (28, 34, 40, 46))
    + f'<circle cx="36" cy="44" r="6" fill="#fff" {W(2.4)}/>'
    + face(48, 79, d=5, k=0.55) +
    # правая пинетка (в прыжке, наклонена)
    f'<g transform="rotate(-16 92 52)">'
    f'<path d="M78 70 L78 42 Q78 32 90 32 L100 32 Q106 32 106 42 L106 56 Q122 56 126 64 Q128 72 118 72 L82 72 Q78 72 78 70Z" fill="#FFB8D6" {W(3)}/>'
    f'<path d="M78 44 H106" stroke="{O}" stroke-width="2.4"/>'
    + "".join(f'<path d="M{x} 34 V42" stroke="#E46E9E" stroke-width="2"/>' for x in (84, 90, 96, 102))
    + f'<circle cx="92" cy="28" r="6" fill="#fff" {W(2.4)}/>'
    + face(104, 63, d=5, k=0.55) + '</g>'
    f'<path d="M86 84 q4 -3 8 0 M100 82 q4 -3 8 0" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/>'
    + sparkle(62, 26, 5, "#fff") + sparkle(14, 30, 3, "#fff"))

# 2. Пеленальная в ТРЦ «РИО» — голубой конверт-кокон с ушками, малыш спит, над ним три звёздочки
I["chg-trc-rio-dmitrovka"] = ("#E3F0FF", "#5B8BD9",
    "голубой стёганый конверт-кокон для новорождённого с капюшоном-ушками",
    "малыш сладко спит внутри, закрыв глазки, а над капюшоном мерцают три жёлтые звёздочки",
    # кокон
    f'<path d="M30 54 Q30 26 64 26 Q98 26 98 54 L98 92 Q98 116 64 116 Q30 116 30 92Z" fill="#9CC8FF" {W(3.2)}/>'
    # ушки капюшона
    f'<ellipse cx="38" cy="30" rx="9" ry="11" fill="#9CC8FF" {W(3)}/>'
    f'<ellipse cx="90" cy="30" rx="9" ry="11" fill="#9CC8FF" {W(3)}/>'
    f'<ellipse cx="38" cy="31" rx="4.5" ry="6" fill="#FFC6DA"/>'
    f'<ellipse cx="90" cy="31" rx="4.5" ry="6" fill="#FFC6DA"/>'
    # лицо малыша
    f'<circle cx="64" cy="56" r="20" fill="#FFE0C7" {W(3)}/>'
    f'<path d="M54 54 q4 4 8 0 M66 54 q4 4 8 0" fill="none" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>'
    f'<ellipse cx="52" cy="62" rx="4" ry="2.6" fill="#FF9EB5" opacity=".7"/>'
    f'<ellipse cx="76" cy="62" rx="4" ry="2.6" fill="#FF9EB5" opacity=".7"/>'
    f'<path d="M60 66 q4 3 8 0" fill="none" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    # стёжка
    + "".join(f'<path d="M36 {y} Q64 {y+8} 92 {y}" fill="none" stroke="#6E9FE6" stroke-width="2.2" stroke-dasharray="4 4"/>' for y in (84, 98))
    + f'<path d="M64 76 V114" stroke="#6E9FE6" stroke-width="2.2" stroke-dasharray="4 4"/>'
    # звёздочки
    + "".join(f'<path d="M{x} {y-6} L{x+2} {y-2} L{x+6} {y} L{x+2} {y+2} L{x} {y+6} L{x-2} {y+2} L{x-6} {y} L{x-2} {y-2}Z" fill="#FFD23F" {W(1.6)}/>'
              for x, y in ((18, 16), (64, 12), (110, 18))))

# 3. «Моресвинок» — кораблик из сена с парусом-листиком, плывёт по волнам, на корме розовые ушки
I["fun-moresvinok-taganka"] = ("#DDF3FF", "#3E9AD6",
    "кораблик из золотистого сена с парусом из зелёного листа салата и мордашкой на борту",
    "плывёт по синим волнам, а с кормы выглядывают два розовых круглых ушка и чёрный носик-пуговка",
    # волны
    f'<path d="M-4 98 Q12 90 28 98 T60 98 T92 98 T124 98 T140 98 V132 H-4Z" fill="#2E7CC0" {W(3)}/>'
    f'<path d="M10 112 q8 -5 16 0 M70 116 q8 -5 16 0" fill="none" stroke="#BDE6FF" stroke-width="2.4" stroke-linecap="round"/>'
    # корпус из сена
    f'<path d="M14 72 L114 72 Q108 98 64 98 Q22 98 14 72Z" fill="#F2C24E" {W(3.2)}/>'
    + "".join(f'<path d="M{x} 76 q4 8 -2 16" fill="none" stroke="#C9952A" stroke-width="2"/>' for x in (28, 44, 60, 76, 92))
    + face(64, 84, d=7, k=0.7) +
    # мачта и парус-листик
    f'<path d="M58 72 V22" stroke="{O}" stroke-width="3.2" stroke-linecap="round"/>'
    f'<path d="M60 24 Q92 30 96 62 Q78 66 60 64Z" fill="#7BD66A" {W(3)}/>'
    f'<path d="M62 28 Q76 44 92 60 M70 40 L80 36 M76 50 L88 46" fill="none" stroke="#3E9A3A" stroke-width="2"/>'
    # ушки и носик на корме
    f'<circle cx="24" cy="64" r="6" fill="#FFB3C7" {W(2.6)}/>'
    f'<circle cx="38" cy="62" r="6" fill="#FFB3C7" {W(2.6)}/>'
    f'<ellipse cx="31" cy="70" rx="3.2" ry="2.4" fill="{O}"/>'
    + sparkle(108, 22, 4, "#fff") + sparkle(22, 30, 3, "#fff"))

# 4. Музей «Фабрика ёлочных игрушек» — кисточка с золотыми блёстками выводит снежинку на прозрачном шаре
I["fun-elka-museum-tkatskaya"] = ("#E9E4FF", "#6B5BD6",
    "тонкая кисточка-художница с золотыми блёстками на кончике и мордашкой на ручке",
    "выводит золотую снежинку на прозрачном стеклянном ёлочном шаре, который стоит на деревянной подставке-подсвечнике",
    # подставка
    f'<path d="M24 112 H84 L76 100 H32Z" fill="#B97A4A" {W(3)}/>'
    # шар
    f'<circle cx="54" cy="66" r="32" fill="#DFF3FF" fill-opacity=".85" {W(3.2)}/>'
    f'<ellipse cx="42" cy="52" rx="8" ry="5" fill="#fff" opacity=".8" transform="rotate(-30 42 52)"/>'
    # колпачок и петелька
    f'<rect x="46" y="28" width="16" height="9" rx="2" fill="#E6B23A" {W(2.6)}/>'
    f'<path d="M50 28 Q54 18 58 28" fill="none" stroke="{O}" stroke-width="2.4"/>'
    # снежинка
    + "".join(f'<path d="M54 70 L{54+18*c:.1f} {70+18*s_:.1f}" stroke="#E6B23A" stroke-width="3" stroke-linecap="round"/>'
              for c, s_ in ((1, 0), (-1, 0), (0.5, 0.87), (-0.5, 0.87), (0.5, -0.87), (-0.5, -0.87)))
    + f'<circle cx="54" cy="70" r="3.4" fill="#E6B23A" {W(1.6)}/>'
    # кисточка (по диагонали справа)
    f'<g transform="rotate(38 96 46)">'
    f'<rect x="90" y="8" width="12" height="56" rx="6" fill="#FF6B6B" {W(3)}/>'
    f'<rect x="89" y="62" width="14" height="10" fill="#C9CED6" {W(2.6)}/>'
    f'<path d="M89 72 Q96 92 103 72Z" fill="#F5C542" {W(2.6)}/>'
    + face(96, 34, d=5, k=0.55) + '</g>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#FFD23F"/>' for x, y in ((80, 76), (86, 84), (76, 90), (90, 72)))
    + sparkle(110, 96, 5, "#FFE680") + sparkle(18, 24, 4, "#fff"))

# 5. Павильон Московского транспорта — транспортная карта прикладывается к валидатору, тот светится зелёным
I["fun-pavilion-transport-kievsky"] = ("#E2F7EC", "#3FA372",
    "синяя транспортная карта с мордашкой и белой полоской",
    "прикладывается к жёлтому валидатору на стойке, а экран валидатора загорается зелёной галочкой",
    # стойка валидатора
    f'<rect x="64" y="70" width="14" height="52" fill="#9AA3B2" {W(3)}/>'
    f'<rect x="46" y="22" width="52" height="56" rx="10" fill="#FFD23F" {W(3.2)}/>'
    f'<rect x="54" y="30" width="36" height="20" rx="4" fill="#2BB673" {W(2.6)}/>'
    f'<path d="M63 40 L70 46 L82 33" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<circle cx="72" cy="64" r="7" fill="#FFF3B0" {W(2.4)}/>'
    f'<path d="M66 64 q6 -6 12 0 M68 67 q4 -4 8 0" fill="none" stroke="{O}" stroke-width="1.6"/>'
    # карта (наклонена, прикладывается)
    f'<g transform="rotate(-18 34 78)">'
    f'<rect x="8" y="60" width="54" height="36" rx="6" fill="#2F6FDE" {W(3.2)}/>'
    f'<rect x="8" y="68" width="54" height="8" fill="#fff"/>'
    f'<rect x="8" y="60" width="54" height="36" rx="6" fill="none" {W(3.2)}/>'
    + face(30, 87, d=6, k=0.6) + '</g>'
    f'<path d="M52 54 q-6 -4 -8 -10 M44 58 q-8 -2 -12 -8" fill="none" stroke="#2BB673" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(108, 92, 4, "#fff") + sparkle(20, 22, 3, "#fff"))

# 6. «Инсектопия» — ящерица тегу на коряге тянет язычок к ложечке с фруктовым пюре
I["fun-insectopia-begovaya"] = ("#FFF1D6", "#E39B3A",
    "чёрно-белая полосатая ящерица тегу с длинным хвостом и розовым раздвоенным язычком",
    "лежит на коряге и тянет язычок к маленькой ложечке с оранжевым фруктовым пюре, которую протягивают справа",
    # коряга
    f'<path d="M-4 96 Q40 86 84 94 Q100 98 132 92 V112 Q90 118 50 110 Q20 108 -4 114Z" fill="#9C6B3E" {W(3)}/>'
    f'<path d="M20 100 q10 3 18 0 M60 102 q8 3 14 0" fill="none" stroke="#6E4523" stroke-width="2"/>'
    # хвост
    f'<path d="M30 80 Q8 82 6 70 Q6 62 14 64" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
    f'<path d="M30 80 Q8 82 6 70 Q6 62 14 64" fill="none" stroke="#3F3F4A" stroke-width="5" stroke-linecap="round"/>'
    # тело
    f'<ellipse cx="48" cy="80" rx="24" ry="11" fill="#3F3F4A" {W(3)}/>'
    + "".join(f'<path d="M{x} 71 q3 9 0 18" fill="none" stroke="#F5F2EA" stroke-width="3" stroke-linecap="round"/>' for x in (34, 44, 54))
    # лапки
    + f'<path d="M34 88 L28 96 M60 88 L66 96" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>'
    # голова
    f'<path d="M64 72 Q74 62 88 68 Q94 72 88 78 Q76 84 64 86Z" fill="#3F3F4A" {W(3)}/>'
    f'<path d="M72 70 q2 4 0 8" fill="none" stroke="#F5F2EA" stroke-width="2.4" stroke-linecap="round"/>'
    f'<circle cx="80" cy="70" r="3.6" fill="#fff" {W(1.6)}/><circle cx="80.6" cy="70.4" r="1.8" fill="{O}"/>'
    f'<path d="M89 74 L98 72 M98 72 l3 -3 M98 72 l3 2" fill="none" stroke="#FF6FA0" stroke-width="2.6" stroke-linecap="round"/>'
    # ложечка с пюре
    f'<path d="M132 52 L110 66" stroke="#C9CED6" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M132 52 L110 66" stroke="{O}" stroke-width="1.6" stroke-linecap="round" opacity=".5"/>'
    f'<ellipse cx="106" cy="69" rx="8" ry="5" fill="#C9CED6" {W(2.4)} transform="rotate(-30 106 69)"/>'
    f'<ellipse cx="105" cy="68" rx="5" ry="3" fill="#FF9A3C" transform="rotate(-30 105 68)"/>'
    + sparkle(100, 26, 5, "#fff") + sparkle(34, 34, 3, "#fff"))

# 7. «Моторы войны» — зелёный танк Т-34 с красной звездой на подиуме под лучом прожектора
I["fun-motory-voiny-rogozhsky"] = ("#E6E9DF", "#6E7A5E",
    "зелёный танк Т-34 с красной звездой на башне и мордашкой",
    "гордо стоит на выставочном подиуме, сверху на него падает жёлтый луч прожектора",
    # луч
    f'<path d="M52 0 L76 0 L112 96 L16 96Z" fill="#FFF3B0" opacity=".75"/>'
    # подиум
    f'<path d="M8 100 H120 L114 118 H14Z" fill="#B0B6BF" {W(3)}/>'
    # гусеница
    f'<rect x="20" y="78" width="88" height="20" rx="10" fill="#4A4F45" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="88" r="5" fill="#8C927F" {W(2)}/>' for x in (32, 46, 60, 74, 88, 100))
    # корпус
    + f'<path d="M16 80 L28 64 H100 L112 80Z" fill="#5E8A3E" {W(3)}/>'
    # башня
    f'<path d="M40 64 Q42 44 62 42 Q82 44 84 64Z" fill="#6E9C4A" {W(3)}/>'
    f'<rect x="82" y="48" width="34" height="7" rx="3" fill="#5E8A3E" {W(2.8)}/>'
    f'<path d="M62 46 l2.6 5.4 6 .8 -4.4 4.2 1 6 -5.2 -2.8 -5.2 2.8 1 -6 -4.4 -4.2 6 -.8Z" fill="#E53935" {W(1.6)}/>'
    + face(48, 72, d=7, k=0.65) +
    sparkle(108, 22, 4, "#fff") + sparkle(20, 30, 3, "#fff"))

# 8. Exotag на Нижегородской — девочка в шлеме с антенной тянется к светящемуся кристаллу среди лазерных лучей
I["fun-exotag-nizhegorodskaya"] = ("#2B2250", "#120E2E",
    "алый инопланетный кристалл-трофей на неоновом пьедестале",
    "девочка в белом шлеме с антенной тянется к нему, а над ней крест-накрест проходят голубой и розовый лазерные лучи",
    # лучи
    f'<path d="M-4 30 L132 70" stroke="#4FE3FF" stroke-width="3" opacity=".9"/>'
    f'<path d="M-4 66 L132 22" stroke="#FF5FC8" stroke-width="3" opacity=".9"/>'
    # пьедестал
    f'<path d="M70 112 L78 84 H110 L118 112Z" fill="#3A2F7A" {W(3)}/>'
    f'<path d="M76 92 H112" stroke="#4FE3FF" stroke-width="2.6"/>'
    # кристалл
    f'<path d="M94 40 L108 60 L94 84 L80 60Z" fill="#FF4D6D" {W(3)}/>'
    f'<path d="M94 40 L94 84 M80 60 H108" stroke="#FFB3C2" stroke-width="2"/>'
    + face(94, 64, d=5, k=0.5) +
    # девочка
    f'<path d="M26 118 Q26 92 44 90 Q60 92 60 118Z" fill="#7A5BE6" {W(3)}/>'
    f'<path d="M56 98 L76 74" stroke="{O}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M56 98 L76 74" stroke="#FFD9B8" stroke-width="4" stroke-linecap="round"/>'
    f'<circle cx="44" cy="76" r="15" fill="#FFD9B8" {W(3)}/>'
    f'<path d="M28 74 Q30 58 44 58 Q58 58 60 74Z" fill="#F4F6FF" {W(3)}/>'
    f'<path d="M50 59 L56 46" stroke="#F4F6FF" stroke-width="2.6"/><circle cx="56" cy="45" r="3" fill="#4FE3FF" {W(1.6)}/>'
    + face(46, 79, d=6, k=0.6) +
    sparkle(20, 20, 4, "#4FE3FF") + sparkle(112, 18, 3, "#FF9EE0"))


if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
