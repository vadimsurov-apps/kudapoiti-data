"""Иконки робота fun (2026-11-08, полдень): 6 мест. Каждая придумана и нарисована отдельно (правило абсолютной
уникальности). Сверено со всеми листами icons-catalog и icons-src/subjects.txt (заняты: танк, пилотка со звездой,
полевая кухня, фляга, треугольник-письмо, перо с чернильницей, веер, цилиндр, сокол, медали — не брать).
Запуск: python3 tools/icons_fun_1108d.py [id ...]  (печатает строки для subjects.txt)"""
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

# ЦАГИ — продувочная модель самолёта на державке в круглом сопле аэродинамической трубы
I["tsagi-demo-center-zhukovsky"] = ("#F2F6FF", "#9AA9C9",
    "серебристая продувочная модель самолёта со стреловидным крылом на державке",
    "висит в круглом сопле аэродинамической трубы, её обтекают голубые линии воздушного потока",
    f'<circle cx="64" cy="64" r="50" fill="#5B6B8C" {W(3)}/>'
    + f'<circle cx="64" cy="64" r="42" fill="#DCEBFF" {W(2.6)}/>'
    + "".join(f'<circle cx="{64+46*c:.1f}" cy="{64+46*s_:.1f}" r="2.4" fill="#DCE3F0"/>'
              for c, s_ in [(1, 0), (-1, 0), (0, 1), (0, -1), (.707, .707), (-.707, .707), (.707, -.707), (-.707, -.707)])
    + "".join(f'<path d="M14 {y} Q40 {y-6*k} 64 {y-10*k} T118 {y}" fill="none" stroke="#5FB4F5" stroke-width="2.6" '
              f'stroke-linecap="round" stroke-dasharray="10 6"/>' for y, k in [(36, -.2), (48, .6), (82, -.6), (94, .2)])
    + f'<path d="M64 74 V112" stroke="#8A93A8" stroke-width="5"/><path d="M61 74 V112 M67 74 V112" {W(1.6)}/>'
    + f'<path d="M30 64 Q34 56 50 56 H96 Q106 58 108 64 Q106 70 96 72 H50 Q34 72 30 64Z" fill="#E8ECF4" {W(3)}/>'
    + f'<path d="M58 60 L80 34 H88 L76 60Z" fill="#C9D1E2" {W(2.6)}/>'
    + f'<path d="M58 68 L80 94 H88 L76 68Z" fill="#B6BFD3" {W(2.6)}/>'
    + f'<path d="M96 58 L104 46 H109 L106 60Z" fill="#E2453C" {W(2.2)}/>'
    + f'<path d="M34 61 Q38 59 42 60" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
    + f(52, 64, d=6, k=0.55)
    + sparkle(100, 26, 3.2, "#fff") + sparkle(26, 100, 2.6, "#fff"))

# Музей боевой славы (Коломна) — «Катюша» на грузовике
I["kolomna-battle-glory-museum"] = ("#FFF4D6", "#E9B85C",
    "зелёная реактивная установка «Катюша» на грузовике, фары — глаза",
    "стоит на весенней поляне с тюльпанами, направляющие рельсы подняты к небу",
    f'<path d="M0 98 Q64 90 128 98 V128 H0Z" fill="#8FCB6B" {W(2.4)}/>'
    + "".join(f'<path d="M{x} 100 V92" stroke="#3E8A3A" stroke-width="2.4"/>'
              f'<path d="M{x-4} 86 Q{x-4} 94 {x} 94 Q{x+4} 94 {x+4} 86 L{x+2} 89 L{x} 85 L{x-2} 89Z" fill="#FF5A6A" {W(1.8)}/>'
              for x in (12, 116, 106))
    + f'<path d="M40 64 L100 30 L106 40 L46 74Z" fill="#7C9A55" {W(3)}/>'
    + "".join(f'<path d="M{44+12*i} {66-6.8*i} L{48+12*i} {72-6.8*i}" {W(1.8)}/>' for i in range(5))
    + f'<path d="M50 70 L58 82 M86 50 L90 80" {W(3)}/>'
    + f'<rect x="22" y="78" width="66" height="16" rx="3" fill="#5E7A3E" {W(3)}/>'
    + f'<path d="M88 94 V64 Q88 58 94 58 H106 Q112 58 114 66 L118 80 V94Z" fill="#6C8C48" {W(3)}/>'
    + f'<path d="M94 62 H106 Q109 62 110 66 L112 74 H94Z" fill="#CFE9FF" {W(2.4)}/>'
    + f'<path d="M100 62 V74" {W(1.6)}/>'
    + f'<path d="M14 82 L22 78" {W(2.6)}/>'
    + f'<circle cx="34" cy="98" r="9" fill="#4A4A5A" {W(2.8)}/><circle cx="34" cy="98" r="3.4" fill="#B8B8C8"/>'
    + f'<circle cx="62" cy="98" r="9" fill="#4A4A5A" {W(2.8)}/><circle cx="62" cy="98" r="3.4" fill="#B8B8C8"/>'
    + f'<circle cx="104" cy="98" r="9" fill="#4A4A5A" {W(2.8)}/><circle cx="104" cy="98" r="3.4" fill="#B8B8C8"/>'
    + f'<circle cx="116" cy="84" r="4" fill="#FFE07A" {W(2)}/>'
    + eye(98, 84, 0.6) + eye(108, 84, 0.6)
    + f'<path d="M100 89 Q103 92 106 89" fill="none" {W(2)}/>'
    + f'<path d="M66 82 l3 -6 l3 6 l-6 -4 h6z" fill="#E2453C"/>'
    + sparkle(30, 30, 3.4, "#fff") + sparkle(60, 18, 2.4, "#fff"))

# Усадьба Гончаровых (Ярополец) — медальон-камея с силуэтом дамы
I["yaropolets-goncharov-estate"] = ("#FCEBFF", "#C79BE0",
    "овальный золотой медальон-камея с белым силуэтом дамы в высокой причёске",
    "покачивается на голубой атласной ленточке, завязанной бантом на ветке старой липы",
    f'<path d="M-4 18 Q50 6 132 20" fill="none" stroke="#7A5434" stroke-width="8" stroke-linecap="round"/>'
    + f'<path d="M-4 18 Q50 6 132 20" fill="none" {W(1.6)}/>'
    + "".join(f'<path d="M{x} {y} q8 -10 16 0 q-8 10 -16 0z" fill="#7FC66A" {W(1.8)}/>' for x, y in [(6, 26), (96, 26), (110, 14), (20, 12)])
    + f'<path d="M64 12 L64 30" stroke="#79B8F0" stroke-width="4"/>'
    + f'<path d="M64 14 Q50 4 46 14 Q50 22 64 14 Q78 4 82 14 Q78 22 64 14Z" fill="#8CC8FF" {W(2.2)}/>'
    + f'<circle cx="64" cy="15" r="3.4" fill="#8CC8FF" {W(2)}/>'
    + f'<ellipse cx="64" cy="72" rx="34" ry="42" fill="#F2C14E" {W(3.2)}/>'
    + "".join(f'<circle cx="{64+34*__import__("math").cos(a/10):.1f}" cy="{72+42*__import__("math").sin(a/10):.1f}" r="2.6" fill="#FFE59A" {W(1.4)}/>'
              for a in range(0, 63, 6))
    + f'<ellipse cx="64" cy="72" rx="25" ry="32" fill="#E58A9E" {W(2.6)}/>'
    + f'<path d="M44 100 Q46 86 58 84 L60 76 Q52 74 52 66 Q48 64 52 60 Q52 46 64 44 Q78 44 78 58 Q78 70 70 76 L72 84 Q84 86 86 100Z" fill="#FFF8F2" {W(2)}/>'
    + f'<circle cx="70" cy="40" r="7" fill="#FFF8F2" {W(2)}/>'
    + f'<path d="M64 44 Q70 46 74 50" fill="none" {W(1.6)}/>'
    + eye(61, 62, 0.6) + f'<ellipse cx="62" cy="69" rx="3.4" ry="2" fill="#FF7FA8" opacity=".7"/>'
    + f'<path d="M53 69 Q56 71 58 69" fill="none" {W(1.6)}/>'
    + sparkle(94, 50, 3.4, "#fff") + sparkle(30, 100, 2.6, "#fff") + sparkle(104, 104, 2, "#fff"))

# Музей Героев-панфиловцев — ушанка со звездой на снегу у берёзки
I["panfilov-heroes-museum-nelidovo"] = ("#EAF3FF", "#9DBCE0",
    "солдатская серая шапка-ушанка с красной звёздочкой",
    "лежит на снежном сугробе у тонкой берёзки, сверху кружатся крупные снежинки",
    f'<path d="M0 92 Q40 80 80 90 Q108 96 128 88 V128 H0Z" fill="#fff" {W(2.6)}/>'
    + f'<path d="M106 92 V10" stroke="#fff" stroke-width="8"/><path d="M102 92 V10 M110 92 V10" {W(1.6)}/>'
    + "".join(f'<path d="M{102 if i%2 else 106} {y} h4" {W(2.2)}/>' for i, y in enumerate((24, 40, 56, 72)))
    + f'<path d="M106 34 Q118 30 124 38 M106 54 Q94 50 90 58" fill="none" {W(1.8)}/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="3" ry="1.8" fill="#F2C94C" transform="rotate(-30 {x} {y})"/>'
              for x, y in [(120, 36), (92, 56), (116, 30)])
    + f'<path d="M22 88 Q20 50 58 46 Q96 50 92 88Z" fill="#8E949E" {W(3.2)}/>'
    + f'<path d="M14 92 Q12 70 24 66 Q30 76 30 96 Q22 100 14 92Z" fill="#A9AEB8" {W(2.8)}/>'
    + f'<path d="M100 92 Q102 70 90 66 Q84 76 84 96 Q92 100 100 92Z" fill="#A9AEB8" {W(2.8)}/>'
    + f'<path d="M26 60 Q58 40 90 60 L92 72 Q58 58 24 72Z" fill="#B5BAC4" {W(2.8)}/>'
    + f'<path d="M58 50 l3.2 6.6 7.2 .8 -5.4 5 1.6 7.2 -6.6 -3.8 -6.6 3.8 1.6 -7.2 -5.4 -5 7.2 -.8z" fill="#E2453C" {W(1.8)}/>'
    + f(58, 80, d=10, k=0.75)
    + "".join(sparkle(x, y, r, "#fff") for x, y, r in [(20, 24, 4), (54, 16, 3), (84, 30, 3.4), (36, 40, 2.4), (122, 70, 2.6)]))

# Музей-усадьба «Даровое» — деревянная соха в борозде («Мужик Марей»)
I["darovoe-dostoevsky-estate"] = ("#FFF7E0", "#F0C77A",
    "деревянная крестьянская соха с двумя железными сошниками",
    "стоит в борозде свежевспаханного поля под берёзовой рощей и летним солнцем",
    f'<circle cx="104" cy="24" r="12" fill="#FFD24A" {W(2.6)}/>'
    + "".join(f'<path d="M{x} 80 V40" stroke="#fff" stroke-width="5"/><path d="M{x-2.5} 80 V40 M{x+2.5} 80 V40" {W(1.4)}/>'
              f'<ellipse cx="{x}" cy="38" rx="11" ry="14" fill="#9FD46A" {W(2.2)}/>' for x in (14, 30, 118))
    + f'<path d="M0 80 Q64 70 128 80 V128 H0Z" fill="#9C6A44" {W(2.6)}/>'
    + "".join(f'<path d="M{-10+i*20} 128 Q{20+i*12} 98 {54+i*4} 80" fill="none" stroke="#7A4E2E" stroke-width="2.4"/>' for i in range(7))
    + f'<path d="M12 50 L70 86" stroke="#B9783E" stroke-width="8" stroke-linecap="round"/><path d="M12 50 L70 86" {W(1.6)}/>'
    + f'<path d="M66 92 L96 36 M84 94 L110 44" stroke="#B9783E" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M66 92 L96 36 M84 94 L110 44" {W(1.4)}/>'
    + f'<path d="M92 38 L112 46" stroke="#B9783E" stroke-width="5" stroke-linecap="round"/>'
    + f'<path d="M56 74 Q76 66 96 76 L92 100 Q76 108 60 100Z" fill="#D9A36A" {W(3)}/>'
    + f'<path d="M60 100 L54 118 L70 104Z M88 102 L94 120 L82 106Z" fill="#B8BCC9" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#6E4426"/>' for x, y, r in [(46, 116, 4), (104, 114, 3.4), (40, 104, 2.6), (110, 102, 2.4)])
    + f(76, 86, d=7, k=0.6)
    + sparkle(104, 52, 2.6, "#fff") + sparkle(20, 104, 2.2, "#FFE9B0"))

# Соколиный двор (Коломенское) — клобучок на сокольничьей рукавице
I["kolomenskoe-falcon-yard"] = ("#E6F7EF", "#77C2A0",
    "красный бархатный клобучок (шапочка для ловчей птицы) с золотым узором и пёрышком-плюмажем",
    "сидит, как на троне, на толстой кожаной сокольничьей рукавице, рядом свисают кожаные ремешки",
    f'<path d="M-4 128 L10 96 L40 112 L28 128Z" fill="#D49A62" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} l-4 8" {W(2)}/>' for x, y in [(4, 104), (12, 110), (20, 114), (28, 118)])
    + f'<path d="M14 98 Q20 76 40 72 L92 70 Q112 70 112 84 Q112 96 100 98 L96 104 Q90 112 80 110 Q72 116 62 112 Q52 116 44 110 L38 110Z" fill="#B97A45" {W(3.2)}/>'
    + f'<path d="M100 98 Q90 96 88 88 M80 110 Q74 104 74 96 M62 112 Q58 106 58 98" fill="none" {W(2.2)}/>'
    + f'<path d="M92 70 Q104 54 112 60 Q116 66 106 78" fill="#C4864F" {W(2.8)}/>'
    + f'<path d="M30 80 Q60 86 90 78" fill="none" stroke="#8A5530" stroke-width="2" stroke-dasharray="4 4"/>'
    + f'<path d="M36 72 Q32 36 64 28 Q96 36 92 72 Q64 80 36 72Z" fill="#C0283C" {W(3.2)}/>'
    + f'<path d="M40 58 Q64 66 88 58" fill="none" stroke="#FFD24A" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#FFD24A" {W(1.2)}/>' for x, y in [(48, 44), (64, 38), (80, 44), (54, 68), (74, 68)])
    + f'<path d="M64 28 V16" {W(2.4)}/>'
    + f'<path d="M64 18 Q54 2 68 4 Q76 8 66 18Z" fill="#FFF6E0" {W(2)}/>'
    + f'<path d="M64 18 Q74 2 84 8 Q82 16 66 19Z" fill="#7FC66A" {W(2)}/>'
    + f(64, 52, d=9, k=0.7)
    + sparkle(106, 30, 3.4, "#fff") + sparkle(18, 50, 2.6, "#fff"))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
