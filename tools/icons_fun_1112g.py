"""Иконки робота fun (2026-11-12, проход g): места из tools/add_fun_1112g.py.
Каждая придумана и нарисована отдельно: свой герой, своя сцена, своя компоновка и палитра фона.
Запуск: python3 tools/icons_fun_1112g.py [id ...]"""
import os, sys
from draw_icons import s, face, sparkle, eye
from icons_fun_1110e import svg

W = lambda w: s(f'stroke-width="{w}"')
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
I = {}

# 1. Троицкий музей — глиняная крынка под стеклянным колпаком витрины
I["fun-troitsk-muzey-lyalko"] = ("#FBEBD2", "#C98E5A",
    "глиняная крынка с белым волнистым узором и мордашкой",
    "стоит на бордовой бархатной подставке под стеклянным колпаком музейной витрины с табличкой",
    f'<rect x="22" y="100" width="84" height="20" rx="4" fill="#8E2B3A" {W(3)}/>'
    f'<rect x="54" y="106" width="20" height="8" rx="2" fill="#F4D58A" {W(1.6)}/>'
    f'<path d="M28 100 V46 Q28 14 64 14 Q100 14 100 46 V100" fill="#E8F6FF" fill-opacity=".35" {W(3)}/>'
    f'<path d="M38 40 Q40 26 52 22" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".8"/>'
    f'<path d="M52 36 H76 L74 44 Q90 56 88 76 Q86 96 64 98 Q42 96 40 76 Q38 56 54 44Z" fill="#C8693A" {W(3.2)}/>'
    f'<ellipse cx="64" cy="36" rx="13" ry="3.5" fill="#8A4424" {W(2.4)}/>'
    f'<path d="M44 82 Q50 76 56 82 T68 82 T80 82 T88 80" fill="none" stroke="#FFF4E0" stroke-width="2.6"/>'
    + face(64, 64, d=9, k=0.8) + sparkle(96, 26, 4, "#fff") + sparkle(16, 60, 3, "#FFE7A8"))

# 2. Физическая кунсткамера — электроскоп с золотыми лепестками и расчёска
I["fun-fizicheskaya-kunstkamera-troitsk"] = ("#2C3E70", "#0E1530",
    "стеклянная колба-электроскоп с латунным шариком и двумя золотыми лепестками фольги",
    "лепестки внутри разлетаются в стороны, потому что к шарику поднесли натёртую синюю расчёску, сыплются искорки",
    f'<rect x="30" y="104" width="68" height="14" rx="4" fill="#7A5A3A" {W(3)}/>'
    f'<path d="M40 104 Q30 80 40 60 Q48 48 64 48 Q80 48 88 60 Q98 80 88 104Z" fill="#CDEBFF" fill-opacity=".45" {W(3.2)}/>'
    f'<rect x="58" y="38" width="12" height="14" fill="#D9A441" {W(2.4)}/>'
    f'<path d="M64 52 V66" stroke="#D9A441" stroke-width="4"/>'
    f'<path d="M64 66 L48 90 L54 92Z" fill="#FFD23F" {W(2)}/><path d="M64 66 L80 90 L74 92Z" fill="#FFD23F" {W(2)}/>'
    f'<circle cx="64" cy="32" r="10" fill="#F2C14E" {W(3)}/>'
    + face(64, 84, d=7, k=0.6) +
    f'<rect x="78" y="8" width="40" height="12" rx="3" fill="#4D8BFF" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 20 V27" stroke="#3B3355" stroke-width="2"/>' for x in range(82, 116, 5))
    + f'<path d="M76 30 l-3 5 l5 0 l-4 6" fill="none" stroke="#FFE14D" stroke-width="2.4"/>'
    + sparkle(86, 40, 4, "#FFE14D") + sparkle(20, 30, 3, "#fff") + sparkle(108, 70, 3, "#9FD0FF"))

# 3. Эмалис — бирюзовый кулон-сердечко над голубым огоньком горелки
I["fun-emalis-taganskiy-park"] = ("#F3E3FF", "#9A6BD8",
    "бирюзовое эмалевое сердечко-кулон в золотой оправе",
    "висит на тонкой цепочке над голубым язычком пламени горелки, эмаль плавится и блестит",
    f'<path d="M64 0 V30" stroke="#D9A441" stroke-width="2.6" stroke-dasharray="4 3"/>'
    f'<path d="M64 46 Q50 28 36 38 Q24 50 36 66 L64 92 L92 66 Q104 50 92 38 Q78 28 64 46Z" fill="#D9A441" {W(3.2)}/>'
    f'<path d="M64 52 Q52 38 42 44 Q32 52 42 64 L64 84 L86 64 Q96 52 86 44 Q76 38 64 52Z" fill="#2EC4B6"/>'
    f'<path d="M46 50 Q50 46 54 48" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    f'<circle cx="64" cy="34" r="5" fill="#D9A441" {W(2.4)}/>'
    + face(64, 62, d=8, k=0.7) +
    f'<rect x="50" y="112" width="28" height="16" rx="3" fill="#6A6A7A" {W(2.6)}/>'
    f'<path d="M64 112 Q52 104 58 96 Q62 100 64 92 Q66 100 70 96 Q76 104 64 112Z" fill="#5AB8FF" {W(2)}/>'
    + sparkle(100, 30, 4, "#fff") + sparkle(26, 92, 3, "#fff") + sparkle(98, 88, 3, "#2EC4B6"))

# 4. Музей карамели — золотая лента карамели тянется между ладонями в белых перчатках
I["fun-muzey-karameli-arbat"] = ("#FFE0EC", "#E86A9A",
    "золотая лента горячей тянущейся карамели с мордашкой",
    "растягивается мостиком-дугой между двумя ладонями в белых перчатках карамельщика",
    f'<path d="M24 78 Q64 18 104 78" fill="none" stroke="#3B3355" stroke-width="22" stroke-linecap="round"/>'
    f'<path d="M24 78 Q64 18 104 78" fill="none" stroke="#F2A71B" stroke-width="16" stroke-linecap="round"/>'
    f'<path d="M34 64 Q64 28 94 64" fill="none" stroke="#FFE08A" stroke-width="4" stroke-linecap="round"/>'
    + face(64, 50, d=8, k=0.7) +
    f'<path d="M6 92 Q8 74 22 72 Q34 72 36 84 L34 104 Q20 112 8 104Z" fill="#fff" {W(3)}/>'
    f'<path d="M122 92 Q120 74 106 72 Q94 72 92 84 L94 104 Q108 112 120 104Z" fill="#fff" {W(3)}/>'
    f'<path d="M14 84 H30 M98 84 H114" stroke="#D0C8D8" stroke-width="2"/>'
    + sparkle(64, 92, 5, "#fff") + sparkle(40, 22, 3, "#FFE08A") + sparkle(96, 20, 3, "#fff"))

# 5. Живая история — деревянная набойка печатает синий цветок на белом полотне
I["fun-zhivaya-istoriya-kurskaya"] = ("#F4F0E6", "#A8B8C8",
    "деревянная резная доска-набойка с ручкой и мордашкой",
    "приподнялась над белым льняным полотном и оставила на нём синий отпечаток цветка",
    f'<path d="M0 84 L128 76 V128 H0Z" fill="#FFFFFF" {W(2.6)}/>'
    f'<path d="M0 96 L128 88 M0 110 L128 102" stroke="#E4DDCC" stroke-width="1.6"/>'
    f'<g transform="translate(36 100)">'
    + "".join(f'<ellipse cx="{dx}" cy="{dy}" rx="6" ry="6" fill="#2B5FB8"/>' for dx, dy in ((0, -9), (9, 0), (0, 9), (-9, 0)))
    + f'<circle cx="0" cy="0" r="4" fill="#9CC2FF"/></g>'
    f'<rect x="54" y="38" width="52" height="34" rx="5" fill="#B9773E" {W(3.2)}/>'
    f'<rect x="58" y="72" width="44" height="6" fill="#2B5FB8" {W(2)}/>'
    f'<path d="M72 38 Q72 16 80 14 Q88 16 88 38" fill="#9A5E2C" {W(3)}/>'
    + face(80, 54, d=9, k=0.75)
    + sparkle(30, 72, 3, "#2B5FB8") + sparkle(108, 22, 3, "#fff"))

# 6. Музей Далёкой Галактики — серебристый звездолёт летит из страниц раскрытой книги
I["fun-muzey-dalekoy-galaktiki"] = ("#5B2B8C", "#1A0B33",
    "маленький серебристый звездолёт с треугольными крыльями и круглым иллюминатором",
    "вылетает наискосок вверх из страниц раскрытой библиотечной книги, оставляя голубой хвост пламени",
    f'<path d="M14 112 Q40 98 64 108 Q88 98 114 112 L114 120 Q88 106 64 116 Q40 106 14 120Z" fill="#FFF6E0" {W(3)}/>'
    f'<path d="M64 108 V116" stroke="#3B3355" stroke-width="2"/>'
    f'<path d="M60 100 Q52 92 44 98 Q50 86 62 92Z" fill="#6FD3FF" opacity=".9"/>'
    f'<g transform="rotate(-38 76 64)">'
    f'<path d="M76 30 Q90 48 90 76 H62 Q62 48 76 30Z" fill="#D8DCE8" {W(3)}/>'
    f'<path d="M62 66 L46 86 L62 82Z M90 66 L106 86 L90 82Z" fill="#FF6B6B" {W(2.6)}/>'
    f'<circle cx="76" cy="56" r="8" fill="#7FE0FF" {W(2.6)}/>'
    f'<path d="M66 76 L70 94 L76 84 L82 94 L86 76Z" fill="#FFB84D" {W(2)}/></g>'
    + eye(73, 56, 0.6) + eye(80, 53, 0.6)
    + sparkle(20, 24, 4, "#fff") + sparkle(108, 18, 3, "#FFE14D") + sparkle(28, 70, 3, "#fff") + sparkle(112, 60, 2.5, "#fff"))

# 7. Музей лозоплетения — недоплетённое лукошко, из донышка лучами торчат прутья
I["fun-muzey-lozopleteniya-ruza"] = ("#E9F7D0", "#8DBB4A",
    "недоплетённое лукошко из ивовой лозы с мордашкой на боку",
    "стоит на траве, сверху лучами торчат неоплетённые прутья, а один зелёный прут с листиком сам вплетается в ряд",
    f'<path d="M0 108 Q64 96 128 108 V128 H0Z" fill="#5E9A2E"/>'
    + "".join(f'<path d="M{64+(x-64)*0.8:.0f} 70 Q{x} 40 {x+(x-64)*0.3:.0f} 18" fill="none" stroke="#B07A3C" stroke-width="3.4" stroke-linecap="round"/>'
              for x in (34, 46, 58, 70, 82, 94))
    + f'<path d="M30 66 H98 L90 108 Q64 116 38 108Z" fill="#C8904A" {W(3.2)}/>'
    + "".join(f'<path d="M{32+i*0} {74+i*9} Q64 {80+i*9} 96 {74+i*9}" fill="none" stroke="#8A5A26" stroke-width="2.4"/>' for i in range(4))
    + face(64, 88, d=9, k=0.8) +
    f'<path d="M98 66 Q112 56 116 40" fill="none" stroke="#7CC242" stroke-width="3.4" stroke-linecap="round"/>'
    f'<ellipse cx="116" cy="36" rx="5" ry="8" fill="#7CC242" transform="rotate(30 116 36)" {W(2)}/>'
    + sparkle(14, 30, 3, "#fff"))

# 8. Легровая — радужная арка из кирпичиков конструктора, под ней ползёт малыш
I["fun-legrovaya-butovo-mall"] = ("#DDF1FF", "#5AA4E0",
    "радужная арка из шести разноцветных кирпичиков конструктора с шипами",
    "под аркой на четвереньках проползает малыш в оранжевом комбинезоне",
    f'<rect x="0" y="108" width="128" height="20" fill="#F4E6C8"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="22" height="16" rx="2" fill="{c}" {W(2.6)}/>'
              f'<rect x="{x+3}" y="{y-4}" width="6" height="4" fill="{c}" {W(1.6)}/><rect x="{x+13}" y="{y-4}" width="6" height="4" fill="{c}" {W(1.6)}/>'
              for x, y, c in ((12, 92, "#FF4D4D"), (14, 72, "#FF9F1C"), (28, 52, "#FFE14D"), (52, 42, "#4CD964"), (76, 52, "#2E9BFF"), (92, 72, "#8E5BFF")))
    + f'<rect x="94" y="92" width="22" height="16" rx="2" fill="#FF6FB5" {W(2.6)}/>'
    f'<ellipse cx="62" cy="96" rx="18" ry="9" fill="#FF8A2B" {W(2.8)}/>'
    f'<path d="M50 100 V108 M74 100 V108" {W(4)}/>'
    f'<circle cx="80" cy="86" r="10" fill="#FFD9B8" {W(2.8)}/>'
    + face(81, 87, d=4.5, k=0.5) + f'<path d="M74 78 Q80 72 88 78" fill="#6B4226"/>'
    + sparkle(108, 26, 4, "#fff") + sparkle(64, 22, 3, "#fff"))

# 9. Нескучай-ка — красное йо-йо раскручивает малыш
I["fun-neskuchayka-butovo-mall"] = ("#FFF0C0", "#F2A23A",
    "красное йо-йо с белой полоской и мордашкой",
    "летит вниз на нитке петлёй, малыш в зелёной футболке держит нитку на пальце и смеётся",
    f'<circle cx="38" cy="44" r="16" fill="#FFD9B8" {W(3)}/>'
    + face(38, 46, d=6, k=0.6) + f'<path d="M24 36 Q38 22 52 36" fill="#3A2A1A" {W(2)}/>'
    f'<path d="M22 60 Q38 54 54 60 L58 104 H18Z" fill="#3CB371" {W(3)}/>'
    f'<path d="M54 66 Q66 56 66 44" fill="none" {W(5)}/><path d="M54 66 Q66 56 66 44" fill="none" stroke="#FFD9B8" stroke-width="3"/>'
    f'<path d="M66 42 Q96 40 88 70 Q84 84 84 88" fill="none" stroke="#3B3355" stroke-width="1.8"/>'
    f'<circle cx="86" cy="94" r="22" fill="#E8283C" {W(3.4)}/>'
    f'<path d="M64 94 H108" stroke="#fff" stroke-width="5"/><path d="M64 94 H108" stroke="#3B3355" stroke-width="1.2" stroke-dasharray="2 22"/>'
    + face(86, 104, d=6, k=0.6) +
    f'<path d="M112 80 q6 6 0 14 M116 74 q10 12 0 26" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(100, 30, 4, "#fff") + sparkle(14, 88, 3, "#fff"))

# 10. Атмокидс — синяя дверца в каменной стене, из замочной скважины льётся свет
I["fun-atmokids-novinsky"] = ("#E2E2EA", "#6F6F86",
    "маленькая синяя дверца-арка с медной ручкой и мордашкой",
    "закрыта в каменной стене подземелья, а из огромной замочной скважины льётся золотой свет и вылетают звёздочки-подсказки",
    "".join(f'<rect x="{x}" y="{y}" width="30" height="16" rx="3" fill="#9C9CB0" {W(2)}/>'
            for y in range(4, 128, 18) for x in range(-14 + (y // 18 % 2) * 15, 128, 32))
    + f'<path d="M30 124 V54 Q30 24 64 24 Q98 24 98 54 V124Z" fill="#2E5BBA" {W(3.4)}/>'
    f'<path d="M64 26 V124" stroke="#1F3F85" stroke-width="2.4"/>'
    f'<path d="M58 84 a6 6 0 1 1 12 0 l3 16 h-18Z" fill="#FFE14D" {W(2.4)}/>'
    f'<path d="M66 92 L118 70 L118 120Z" fill="#FFE680" opacity=".5"/>'
    f'<circle cx="84" cy="80" r="4" fill="#D98A3A" {W(2)}/>'
    + face(64, 56, d=8, k=0.75)
    + sparkle(104, 82, 5, "#FFE14D") + sparkle(112, 104, 3.5, "#fff") + sparkle(96, 64, 3, "#FFE14D"))

# 11. Кто Круче — красная кнопка-зуммер телешоу под прожектором
I["fun-kto-kruche-baumanskaya"] = ("#FF7A59", "#8A1530",
    "большая красная кнопка-зуммер телевикторины на чёрной подставке",
    "по ней с размаху хлопает детская ладошка под лучом студийного прожектора, кнопка кричит «БЗЗ»",
    f'<path d="M50 0 H78 L106 128 H22Z" fill="#FFF2A8" opacity=".35"/>'
    f'<path d="M24 98 L32 78 H96 L104 98Z" fill="#2A2238" {W(3)}/>'
    f'<rect x="20" y="96" width="88" height="16" rx="4" fill="#3B3355" {W(3)}/>'
    f'<ellipse cx="64" cy="78" rx="30" ry="10" fill="#B0102A" {W(3)}/>'
    f'<path d="M34 78 V66 Q64 50 94 66 V78" fill="#F21B3F" {W(3)}/>'
    f'<ellipse cx="64" cy="66" rx="30" ry="10" fill="#FF4D6A" {W(3)}/>'
    + face(64, 72, d=7, k=0.6) +
    f'<path d="M54 52 Q50 36 56 30 L58 18 Q60 12 64 14 Q67 16 66 22 L70 12 Q73 8 76 11 Q78 14 76 20 L80 14 Q83 12 85 16 L82 30 Q86 28 88 32 Q86 44 74 54Z" fill="#FFD9B8" {W(2.6)}/>'
    f'<text x="12" y="44" font-family="Arial Black,Arial" font-weight="900" font-size="15" fill="#FFE14D" stroke="#3B3355" stroke-width="1.2">БЗЗ</text>'
    + sparkle(104, 30, 5, "#FFE14D") + sparkle(108, 56, 3, "#fff"))

# 12. КукуРуза — кукурузный початок в VR-шлеме среди пикселей
I["fun-kukuruza-vr-ruza"] = ("#C8F7F0", "#2AA198",
    "жёлтый кукурузный початок в чёрном VR-шлеме с розовым светящимся визором",
    "выглядывает из распахнутых зелёных листьев-обёртки, а вокруг него в воздухе висят квадратные цветные пиксели",
    f'<path d="M64 118 Q30 100 26 60 Q44 80 58 96Z" fill="#5DBB46" {W(3)}/>'
    f'<path d="M64 118 Q98 100 102 60 Q84 80 70 96Z" fill="#4CA83A" {W(3)}/>'
    f'<path d="M64 14 Q86 18 88 60 Q88 96 64 108 Q40 96 40 60 Q42 18 64 14Z" fill="#FFD23F" {W(3.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#F2A71B"/>' for y in range(66, 104, 9) for x in range(50 + (y % 2) * 3, 80, 9))
    + f'<rect x="38" y="34" width="52" height="24" rx="8" fill="#2A2238" {W(3)}/>'
    f'<rect x="43" y="39" width="42" height="14" rx="5" fill="#FF5FD2"/>'
    f'<path d="M48 44 h8 M62 44 h6" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    f'<path d="M54 64 Q64 72 74 64" fill="none" {W(2.6)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{w}" fill="{c}" {W(1.6)}/>'
              for x, y, w, c in ((12, 28, 9, "#FF5FD2"), (104, 22, 8, "#4D8BFF"), (16, 92, 7, "#FFE14D"), (108, 88, 9, "#FF7A59"), (100, 50, 6, "#fff")))
    + sparkle(30, 12, 3, "#fff"))

if __name__ == "__main__":
    want = set(sys.argv[1:])
    for pid, v in I.items():
        if want and pid not in want:
            continue
        a, b, hero, scene, body = v
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
