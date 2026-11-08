"""Иконки робота fun (2026-11-08, вечер): 5 мест. Каждая придумана и нарисована отдельно (правило абсолютной
уникальности). Сверено со всеми листами icons-catalog (01–38) и icons-src/subjects.txt. Заняты и НЕ брать:
попкорн, бобина/катушка, киноплёнка, хлопушка, 3D-очки, неоновая вывеска «КИНО», кресло, экран-с-картинкой, луч
проектора, кинокамеры, билет, будка кассы; шлем-ведро, рыцари, щит с мечом; ладьи, ферзи, короли, конь-сыщик;
алмаз/кристаллы/изумруд, короны.
Запуск: python3 tools/icons_fun_1108e.py [id ...]  (печатает строки для subjects.txt)"""
import os, sys
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")


def svg(a, b, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


I = {}

# Оружейный подвал — латная рукавица машет из сводчатого подвального окошка
bricks = "".join(f'<path d="M0 {y} H128" stroke="#B5552F" stroke-width="1.6"/>' for y in range(14, 128, 14))
bricks += "".join(f'<path d="M{x + (14 if (y // 14) % 2 else 0)} {y} V{y+14}" stroke="#B5552F" stroke-width="1.6"/>'
                  for y in range(0, 128, 14) for x in range(0, 128, 28))
I["oruzheyny-podval"] = ("#F7B48A", "#C9643A",
    "стальная латная рукавица рыцаря с заклёпками и пальцами-пластинками",
    "весело машет «привет» из тёмного сводчатого окошка кирпичного подвала",
    bricks
    + f'<path d="M22 128 V70 Q22 30 64 30 Q106 30 106 70 V128Z" fill="#E9A06E" {W(3)}/>'
    + f'<path d="M30 128 V72 Q30 40 64 40 Q98 40 98 72 V128Z" fill="#3D2E45" {W(2.6)}/>'
    # рукав-наруч
    + f'<path d="M46 128 L50 92 H80 L84 128Z" fill="#AEB8C6" {W(3)}/>'
    + f'<path d="M48 108 H82 M47 118 H83" {W(2)}/>'
    # ладонь
    + f'<path d="M48 94 Q44 70 52 62 H80 Q88 70 84 94Z" fill="#D5DDE8" {W(3)}/>'
    # пальцы-пластинки
    + "".join(f'<path d="M{x} 64 V{t} Q{x+5} {t-5} {x+10} {t} V64" fill="#E6ECF4" {W(2.6)}/>'
              + f'<path d="M{x} {t+10} H{x+10} M{x} {t+20} H{x+10}" {W(1.6)}/>'
              for x, t in [(52, 36), (62, 32), (72, 38)])
    + f'<path d="M82 76 Q94 66 98 54 Q102 50 104 56 Q102 70 86 86Z" fill="#E6ECF4" {W(2.6)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2" fill="#7D8798"/>' for x, y in [(54, 88), (78, 88), (54, 100), (76, 100)])
    + f(66, 76, d=7, k=0.62)
    + f'<path d="M104 40 q6 -4 10 0 M106 32 q6 -6 12 -2" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(16, 24, 3, "#FFE7C9"))

# Музей шахмат — янтарная пешка с мушкой внутри в музейной витрине
I["chess-museum-gogolevsky"] = ("#BFEDE6", "#2F8F8A",
    "янтарная шахматная пешка с крошечной застывшей мушкой внутри",
    "светится медовым светом на бархатной подушечке в стеклянной музейной витрине с табличкой",
    f'<rect x="10" y="100" width="108" height="30" fill="#8C5A3C" {W(3)}/>'
    + f'<rect x="88" y="106" width="22" height="10" rx="2" fill="#FFF3D6" {W(2)}/>'
    + f'<path d="M92 111 H106" stroke="#B89B6E" stroke-width="1.6"/>'
    + f'<rect x="24" y="22" width="80" height="80" rx="4" fill="#E9FBFF" fill-opacity=".45" {W(3)}/>'
    + f'<path d="M32 30 L44 30 L32 46Z" fill="#fff" opacity=".7"/>'
    + f'<path d="M34 98 Q34 86 64 86 Q94 86 94 98Z" fill="#7A2F55" {W(2.8)}/>'
    + f'<path d="M44 88 Q48 70 54 62 Q46 58 48 48 Q50 36 64 36 Q78 36 80 48 Q82 58 74 62 Q80 70 84 88Z" '
      f'fill="#F2A33A" {W(3.2)}/>'
    + f'<path d="M54 44 Q58 40 62 41" fill="none" stroke="#FFE6A8" stroke-width="3" stroke-linecap="round"/>'
    + f'<path d="M52 82 Q50 72 56 66" fill="none" stroke="#FFD27A" stroke-width="2.6" stroke-linecap="round"/>'
    # мушка внутри
    + f'<ellipse cx="68" cy="68" rx="4.6" ry="3" fill="#FFF8E6" fill-opacity=".85" stroke="#5A3A1E" stroke-width="1.2" transform="rotate(-35 68 68)"/>'
    + f'<ellipse cx="77" cy="68" rx="4.6" ry="3" fill="#FFF8E6" fill-opacity=".85" stroke="#5A3A1E" stroke-width="1.2" transform="rotate(35 77 68)"/>'
    + f'<ellipse cx="72.5" cy="74" rx="3" ry="4.6" fill="#5A3A1E"/>'
    + f'<circle cx="72.5" cy="69" r="2.2" fill="#5A3A1E"/>'
    + f(64, 56, d=7, k=0.6)
    + sparkle(96, 34, 3.4, "#fff") + sparkle(30, 66, 2.4, "#FFF2C2") + sparkle(84, 60, 2, "#FFF2C2"))

# Алмазный фонд — царская держава с сапфиром под лучом прожектора
I["diamond-fund-kremlin"] = ("#7E2B3E", "#2A0E1E",
    "золотая царская держава с синим сапфиром и крестиком на макушке, пояс из бриллиантов",
    "гордо сидит на чёрной бархатной подушке с кисточками под лучом прожектора в тёмной сокровищнице",
    f'<path d="M48 -4 H80 L116 120 H12Z" fill="#FFF4C8" opacity=".26"/>'
    + f'<path d="M14 112 Q14 96 64 96 Q114 96 114 112 Q114 124 64 124 Q14 124 14 112Z" fill="#2B2235" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="111" r="3.4" fill="#E2B33C" {W(1.4)}/>' for x in (20, 108))
    + f'<circle cx="64" cy="72" r="32" fill="#F2C230" {W(3.2)}/>'
    + f'<path d="M32 72 Q64 82 96 72" fill="none" stroke="#C99A1A" stroke-width="7"/>'
    + f'<path d="M32 72 Q64 82 96 72" fill="none" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#fff" {W(1)}/>' for x, y in [(40, 75), (50, 77.5), (78, 77.5), (88, 75)])
    + f'<path d="M64 40 V48" stroke="#C99A1A" stroke-width="6"/>'
    + f'<path d="M58 30 Q64 22 70 30 L68 40 H60Z" fill="#3E7BEA" {W(2.6)}/>'
    + f'<path d="M64 6 V22 M58 12 H70" stroke="#F2C230" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M64 6 V22 M58 12 H70" fill="none" {W(1.6)}/>'
    + f'<path d="M42 56 Q48 46 58 44" fill="none" stroke="#FFF1A6" stroke-width="3.4" stroke-linecap="round"/>'
    + f(64, 62, d=9, k=0.72)
    + f'<circle cx="64" cy="77" r="3.4" fill="#E2453C" {W(1.4)}/>'
    + sparkle(100, 36, 4.4, "#FFE58A") + sparkle(24, 44, 3, "#FFE58A") + sparkle(106, 80, 2.4, "#fff")
    + sparkle(74, 26, 2.4, "#fff"))

# Кинотеатр «Москва» — два премьерных прожектора на крыше скрещивают лучи
def lamp(x, y, ang):
    return (f'<g transform="rotate({ang} {x} {y})">'
            f'<rect x="{x-13}" y="{y-6}" width="26" height="26" rx="5" fill="#9AA3B5" {W(3)}/>'
            f'<ellipse cx="{x}" cy="{y-6}" rx="15" ry="9" fill="#FFF6C8" {W(3)}/>'
            f'<ellipse cx="{x}" cy="{y-6}" rx="9" ry="5" fill="none" stroke="#F2D27A" stroke-width="2"/>'
            f'</g>')


I["cin-moskva-okhotny"] = ("#5B4BC4", "#1C1640",
    "два премьерных прожектора-близнеца на крыше кинотеатра",
    "скрещивают голубые лучи в ночном небе над вывеской «КИНО», в точке скрещения горит звёздочка",
    f'<path d="M30 74 L98 -6 H124 L46 82Z" fill="#BFE6FF" opacity=".4"/>'
    + f'<path d="M98 74 L30 -6 H4 L82 82Z" fill="#BFE6FF" opacity=".4"/>'
    + f'<rect x="8" y="98" width="112" height="34" fill="#C7343F" {W(3)}/>'
    + f'<rect x="38" y="104" width="52" height="16" rx="3" fill="#FFE58A" {W(2.4)}/>'
    + f'<text x="64" y="117" font-family="Arial Black, Arial" font-weight="900" font-size="12" '
      f'text-anchor="middle" fill="#C7343F">КИНО</text>'
    + "".join(f'<circle cx="{x}" cy="102" r="1.8" fill="#FFF6C8"/>' for x in range(16, 120, 8))
    + f'<path d="M26 98 L34 86 L42 98 M86 98 L94 86 L102 98" {W(3)}/>'
    + lamp(34, 80, 40) + lamp(94, 80, -40)
    + f'<g transform="rotate(40 34 74)">{f(34, 74, d=4, k=0.45)}</g>'
    + f'<g transform="rotate(-40 94 74)">{f(94, 74, d=4, k=0.45)}</g>'
    + sparkle(64, 34, 8, "#FFE58A") + sparkle(64, 34, 3.4, "#fff")
    + sparkle(18, 54, 2, "#fff") + sparkle(110, 52, 2.4, "#fff") + sparkle(64, 10, 1.8, "#fff"))

# Пять звёзд на Павелецкой — паровозик из фильма Люмьеров въезжает из экрана в зал
I["cin-5zvezd-paveletskaya"] = ("#E8505B", "#6E1424",
    "чёрно-белый паровозик из первого фильма братьев Люмьер",
    "выезжает из киноэкрана прямо в тёмный зал, малыши в первом ряду ахают и отклоняются",
    f'<rect x="10" y="10" width="108" height="66" rx="4" fill="#ECECEC" {W(3)}/>'
    + f'<path d="M14 62 H114" stroke="#B9B9B9" stroke-width="2"/>'
    + f'<path d="M14 66 L50 46 M114 66 L78 46" stroke="#9A9A9A" stroke-width="2"/>'
    # паровоз анфас, вылезает из экрана
    + f'<rect x="38" y="46" width="52" height="44" rx="8" fill="#4A4A55" {W(3.2)}/>'
    + f'<rect x="50" y="28" width="12" height="20" fill="#2F2F38" {W(2.8)}/>'
    + f'<path d="M48 28 H64" {W(3.4)}/>'
    + f'<circle cx="56" cy="20" r="6" fill="#fff" {W(2)}/><circle cx="66" cy="12" r="4.4" fill="#fff" {W(1.8)}/>'
    + f'<circle cx="64" cy="64" r="15" fill="#D9D9DE" {W(3)}/>'
    + f'<path d="M34 90 H94 L100 100 H28Z" fill="#6A6A75" {W(3)}/>'
    + "".join(f'<path d="M{x} 92 V100" {W(2)}/>' for x in (44, 54, 64, 74, 84))
    + f'<circle cx="80" cy="50" r="4" fill="#FFE58A" {W(2)}/>'
    + f(64, 62, d=6, k=0.62)
    # головы малышей в первом ряду (вид сзади)
    + f'<circle cx="26" cy="118" r="13" fill="#7A4A2A" {W(3)}/>'
    + f'<circle cx="64" cy="122" r="12" fill="#F2C14E" {W(3)}/>'
    + f'<circle cx="104" cy="118" r="13" fill="#3B3355" {W(3)}/>'
    + f'<path d="M14 104 l-6 -6 M38 104 l6 -8 M92 104 l-6 -8 M116 104 l6 -6" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    + sparkle(110, 30, 3, "#fff") + sparkle(20, 30, 2.4, "#fff"))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
