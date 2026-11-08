"""Иконки робота fun (2026-11-08, утро): 10 мест. Каждая придумана и нарисована отдельно (правило абсолютной
уникальности). Сверено со всеми листами icons-catalog и icons-src/subjects.txt (заняты: кинохлопушка, кинокресло,
плёнка, режиссёрский стул, открытая книга, настольная лампа, палитра, баночка гуаши, тюбик краски, книжка-раскладушка,
клён-вертолётики, одуванчик, скакалка, белка-летяга, сойка, деревянный манекен, ракета — не брать).
Запуск: python3 tools/icons_fun_1108b.py [id ...]  (печатает строки для subjects.txt)"""
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

# Кинопарк «Москино» — фанерный фасад салуна из «Ковбойского городка», подпёртый сзади брусьями
I["kinopark-moskino"] = ("#FFF1C9", "#F2B45E",
    "плоский фанерный фасад салуна с дверцами-«крыльями» — киношная декорация",
    "стоит на песке ковбойского городка, сбоку видно, что он тонкий и держится на косых брусьях, рядом кактус",
    f'<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="#E8C27E" {W(2.6)}/>'
    + f'<path d="M92 100 L116 62 M100 100 L116 76" stroke="#9A6A3C" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M92 100 L116 62 M100 100 L116 76" fill="none" {W(2.2)}/>'
    + f'<path d="M30 100 V46 H40 V36 H80 V46 H90 V100Z" fill="#D9874A" {W(3.2)}/>'
    + f'<path d="M90 100 V46 L95 48 V102Z" fill="#B0652F" {W(2.4)}/>'
    + f'<path d="M30 60 H90 M30 74 H90 M30 88 H90" {W(1.4)} opacity=".35"/>'
    + f'<rect x="42" y="40" width="36" height="12" rx="2" fill="#FFF3C4" {W(2.4)}/>'
    + f'<path d="M54 46 Q60 40 66 46" fill="none" {W(2.4)}/>'
    + f'<path d="M48 76 H59 V98 H48Z M61 76 H72 V98 H61Z" fill="#F2CF5B" {W(2.6)}/>'
    + f'<path d="M48 82 H59 M61 82 H72" {W(1.8)}/>'
    + f(60, 62, d=9, k=0.62)
    + f'<path d="M14 100 V62 Q14 56 19 56 Q24 56 24 62 V100Z" fill="#5DBB63" {W(2.6)}/>'
    + f'<path d="M14 78 H8 V68 M24 72 H30 V62" fill="none" stroke="#5DBB63" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M14 78 H8 V68 M24 72 H30 V62" fill="none" {W(1.6)}/>'
    + sparkle(104, 28, 5, "#fff") + sparkle(20, 34, 3, "#fff"))

# Театр «Крылья» (Жаворонки) — ребёнок в костюме бабочки кланяется на сцене
I["krylya-theatre-zhavoronki"] = ("#F7D6FF", "#A361D9",
    "малыш-актёр в костюме бабочки с большими картонными крыльями",
    "низко кланяется на деревянной сцене между двумя половинками бордового занавеса",
    f'<path d="M4 4 Q22 60 14 128 H0 V0Z M124 4 Q106 60 114 128 H128 V0Z" fill="#9B1B3A" {W(2.6)}/>'
    + f'<path d="M0 100 H128 V128 H0Z" fill="#C98A4B" {W(2.6)}/>'
    + f'<path d="M20 112 H108" {W(2)} opacity=".5"/>'
    + f'<path d="M62 70 Q30 30 22 54 Q18 78 58 80Z" fill="#FFB547" {W(3)}/>'
    + f'<path d="M66 70 Q98 30 106 54 Q110 78 70 80Z" fill="#FFB547" {W(3)}/>'
    + f'<path d="M58 80 Q34 92 38 104 Q50 104 62 84Z M70 80 Q94 92 90 104 Q78 104 66 84Z" fill="#FF7FA8" {W(2.8)}/>'
    + '<circle cx="38" cy="58" r="5" fill="#fff" opacity=".8"/><circle cx="90" cy="58" r="5" fill="#fff" opacity=".8"/>'
    + f'<path d="M56 100 L60 76 H68 L72 100" fill="#6B4FBB" {W(2.6)}/>'
    + f'<circle cx="64" cy="70" r="12" fill="#FFD9B8" {W(3)}/>'
    + f'<path d="M58 58 Q54 48 50 46 M70 58 Q74 48 78 46" fill="none" {W(2.4)}/>'
    + '<circle cx="50" cy="46" r="2.8" fill="#3B3355"/><circle cx="78" cy="46" r="2.8" fill="#3B3355"/>'
    + f'<path d="M58 72 Q60 70 62 72 M66 72 Q68 70 70 72" fill="none" {W(2.2)}/>'
    + '<ellipse cx="56" cy="76" rx="3" ry="1.8" fill="#FF7FA8" opacity=".7"/><ellipse cx="72" cy="76" rx="3" ry="1.8" fill="#FF7FA8" opacity=".7"/>'
    + sparkle(64, 24, 5, "#FFF2A8") + sparkle(40, 22, 3, "#fff") + sparkle(88, 22, 3, "#fff"))

# Дом-музей Королёва — чертёжная доска с эскизом ракеты
I["korolev-memorial-house"] = ("#7E8FE0", "#2C3480",
    "наклонная чертёжная доска на ножках-кронштейне с карандашным эскизом ракеты",
    "стоит в кабинете у тёмного окна со звёздами, на доске — рейсшина и красный карандаш",
    f'<rect x="80" y="14" width="34" height="40" rx="3" fill="#1D2360" {W(2.6)}/>'
    + f'<path d="M97 14 V54 M80 34 H114" {W(2)}/>'
    + sparkle(88, 24, 3, "#FFE79A") + sparkle(106, 44, 2.6, "#FFE79A") + sparkle(104, 22, 2, "#fff")
    + f'<path d="M64 92 L50 120 M64 92 L78 120 M42 120 H86" fill="none" {W(4)}/>'
    + f'<path d="M20 40 L104 58 L94 98 L12 80Z" fill="#F7F3E6" {W(3.2)}/>'
    + f'<path d="M14 86 L96 104" stroke="#8A6A4B" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M14 86 L96 104" fill="none" {W(2)}/>'
    + f'<path d="M48 58 Q56 46 66 60 L62 80 L44 76Z" fill="none" stroke="#3D5AFE" stroke-width="2.6" stroke-linejoin="round"/>'
    + f'<path d="M44 76 L36 84 L46 82 M62 80 L66 90 L58 84" fill="none" stroke="#3D5AFE" stroke-width="2.4" stroke-linejoin="round"/>'
    + '<circle cx="55" cy="64" r="3" fill="none" stroke="#3D5AFE" stroke-width="2"/>'
    + f'<path d="M72 56 L98 50" stroke="#E53935" stroke-width="5" stroke-linecap="round"/><path d="M98 50 L104 49" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    + f(30, 66, d=6, k=0.55))

# Экостанция «Царская охота» (Лосиный остров, Балашиха) — кормушка-ясли с сеном для лосей
I["tsarskaya-okhota-balashikha"] = ("#EAF6FF", "#8EC3E8",
    "лесная кормушка-ясли с сеном под двускатной крышей",
    "стоит в заснеженном лесу, на крыше шапка снега, а к ней по сугробу тянутся лосиные следы",
    f'<path d="M0 98 Q64 86 128 98 V128 H0Z" fill="#F4FAFF" {W(2.6)}/>'
    + f'<path d="M10 70 L20 44 L30 70Z M98 64 L110 34 L122 64Z" fill="#3E9A6A" {W(2.4)}/>'
    + f'<path d="M36 96 V56 M92 96 V56" stroke="#8A5A33" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M36 96 V56 M92 96 V56" fill="none" {W(2.4)}/>'
    + f'<path d="M40 64 L88 64 L82 88 L46 88Z" fill="#B07A45" {W(3)}/>'
    + f'<path d="M48 64 L52 88 M58 64 L60 88 M70 64 L68 88 M80 64 L76 88" {W(2)}/>'
    + f'<path d="M42 64 Q50 52 58 62 Q66 50 74 62 Q82 52 88 64Z" fill="#F2CF5B" {W(2.6)}/>'
    + f'<path d="M26 58 L64 30 L102 58" fill="#C46B3A" {W(3.2)}/>'
    + f'<path d="M24 56 Q30 44 44 44 L64 28 L84 44 Q98 44 104 56 L64 34Z" fill="#fff" {W(2.6)}/>'
    + f(64, 76, d=8, k=0.6)
    + "".join(f'<path d="M{x} {y} q-2 4 0 6 M{x+4} {y} q2 4 0 6" fill="none" {W(2)}/>' for x, y in [(14, 102), (28, 108), (100, 102), (112, 108)])
    + sparkle(50, 18, 3, "#fff") + sparkle(84, 14, 2.6, "#fff"))

# Детский отдел библиотеки искусств им. Боголюбова — книга с нотами и картинкой
I["bogolyubov-lib-kids"] = ("#FFF6C8", "#F5C04A",
    "раскрытая книга: на левой странице скрипичный ключ, на правой — нарисованный пейзаж с солнцем",
    "лежит на столе, а из разворота вылетают ноты и цветной мазок краски",
    f'<path d="M12 86 Q36 74 62 84 V108 Q36 98 12 110Z" fill="#fff" {W(3)}/>'
    + f'<path d="M116 86 Q92 74 66 84 V108 Q92 98 116 110Z" fill="#fff" {W(3)}/>'
    + f'<path d="M12 110 Q36 100 62 108 L66 108 Q92 100 116 110 L116 116 Q92 106 66 114 L62 114 Q36 106 12 116Z" fill="#E05A47" {W(2.6)}/>'
    + f'<path d="M36 102 Q28 94 34 86 Q42 80 40 92 Q38 102 34 106 Q30 110 28 104" fill="none" stroke="#3B3355" stroke-width="2.6" stroke-linecap="round"/>'
    + f'<path d="M72 102 Q84 92 108 98" fill="none" stroke="#6CC56A" stroke-width="6" stroke-linecap="round"/>'
    + '<circle cx="98" cy="88" r="5" fill="#FFB547"/>'
    + f'<path d="M34 66 V44 L46 40 V62" fill="none" {W(3)}/>'
    + f'<ellipse cx="30" cy="66" rx="6" ry="4.5" fill="#3B3355"/><ellipse cx="42" cy="62" rx="6" ry="4.5" fill="#3B3355"/>'
    + f'<path d="M74 22 V44" fill="none" {W(3)}/><ellipse cx="70" cy="44" rx="6" ry="4.5" fill="#3B3355"/>'
    + f'<path d="M74 22 Q82 26 80 32" fill="none" {W(3)}/>'
    + f'<path d="M84 70 Q96 50 112 58 Q104 70 90 74Z" fill="#7E6BF2" {W(2.6)}/>'
    + f'<path d="M86 72 Q96 66 104 62" fill="none" stroke="#B9AEFF" stroke-width="2.4" stroke-linecap="round"/>'
    + f(64, 96, d=10, k=0.55, blush=False)
    + sparkle(56, 28, 4, "#fff") + sparkle(100, 30, 3, "#fff"))

# Библиотека №200 «Истоки» (детский отдел) — из книги течёт ручеёк
I["lib200-istoki-kids"] = ("#E2FAD2", "#6CC16A",
    "толстая зелёная книга, из страниц которой вытекает голубой ручеёк",
    "лежит на травяном бугорке, а по ручейку вниз плывёт кораблик из листика",
    f'<path d="M0 84 Q40 70 70 80 Q100 88 128 78 V128 H0Z" fill="#A8E07E" {W(2.6)}/>'
    + f'<path d="M64 74 Q60 92 74 100 Q92 110 84 128 L108 128 Q114 104 92 94 Q80 88 80 74Z" fill="#7FD3FF" {W(2.6)}/>'
    + f'<path d="M82 104 Q90 108 92 116" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    + f'<path d="M24 74 L40 34 L96 30 L80 70Z" fill="#3E9A6A" {W(3.2)}/>'
    + f'<path d="M24 74 L80 70 L82 78 L26 82Z" fill="#FFF8E6" {W(2.6)}/>'
    + f'<path d="M30 78 L80 74" {W(1.6)} opacity=".5"/>'
    + f'<path d="M44 40 L88 37" stroke="#F2CF5B" stroke-width="3" stroke-linecap="round"/>'
    + f(60, 54, d=9, k=0.65)
    + f'<path d="M88 112 Q96 104 104 112 Q96 118 88 112Z" fill="#F2A33A" {W(2.2)}/>'
    + f'<path d="M96 112 V104" {W(2)}/>'
    + sparkle(106, 20, 4, "#fff") + sparkle(18, 30, 3, "#fff"))

# Детское отделение библиотеки №255 (Зеленоград) — библиотечная тележка с книгами
I["lib255-zelenograd-kids"] = ("#D4FBF3", "#4FBFAE",
    "библиотечная тележка на колёсиках, полная разноцветных книг",
    "сама катится по полу читального зала, а верхняя книжка машет закладкой-ленточкой",
    f'<path d="M0 104 H128 V128 H0Z" fill="#E9C9A0" {W(2.6)}/>'
    + f'<path d="M26 54 H96 L92 96 H30Z" fill="#E8EEF5" {W(3.2)}/>'
    + f'<path d="M28 76 H94" {W(3)}/>'
    + f'<path d="M96 54 L106 40 Q110 34 116 38" fill="none" {W(4)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{c}" {W(2.2)}/>' for x, y, w, h, c in [
        (32, 58, 9, 18, "#E05A47"), (42, 60, 8, 16, "#FFB547"), (51, 57, 10, 19, "#7E6BF2"), (62, 59, 8, 17, "#4FA3F0"),
        (71, 58, 10, 18, "#6CC56A"), (82, 61, 9, 15, "#FF7FA8"),
        (34, 80, 10, 16, "#4FA3F0"), (45, 79, 9, 17, "#F2CF5B"), (55, 81, 10, 15, "#E05A47"), (66, 79, 9, 17, "#7E6BF2"), (76, 80, 12, 16, "#6CC56A")])
    + f'<rect x="44" y="30" width="34" height="24" rx="3" fill="#F2A33A" {W(3)}/>'
    + f'<path d="M72 30 Q78 18 86 22 Q80 28 76 32" fill="#E05A47" {W(2.2)}/>'
    + f(61, 42, d=7, k=0.55)
    + "".join(f'<circle cx="{x}" cy="102" r="6" fill="#4A4F63" {W(2.4)}/><circle cx="{x}" cy="102" r="2" fill="#fff"/>' for x in (36, 86))
    + f'<path d="M14 92 H22 M10 100 H20" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    + sparkle(104, 20, 4, "#fff"))

# Петровский парк — каштан выглядывает из колючей скорлупки
I["petrovsky-park"] = ("#FFE9C2", "#F2A65A",
    "блестящий каштан в раскрытой колючей зелёной скорлупке",
    "висит на ветке с пятипалым листом и выглядывает из скорлупки, как из люльки",
    f'<path d="M0 30 Q50 20 76 34" fill="none" stroke="#7A4E2D" stroke-width="7" stroke-linecap="round"/>'
    + f'<path d="M0 30 Q50 20 76 34" fill="none" {W(2.2)}/>'
    + "".join(f'<ellipse cx="22" cy="44" rx="5" ry="14" fill="#4CAF50" transform="rotate({r} 22 30) translate(0 0)" {W(2.2)}/>' for r in (-70, -35, 0, 35, 70))
    + f'<circle cx="22" cy="30" r="3" fill="#7A4E2D"/>'
    + f'<path d="M64 34 V50" {W(3)}/>'
    + f'<path d="M30 78 Q30 50 64 48 Q98 50 98 78 Q98 112 64 114 Q30 112 30 78Z" fill="#8BD06A" {W(3.2)}/>'
    + "".join(f'<path d="M{x} {y} l{dx} {dy}" {W(2.4)}/>' for x, y, dx, dy in [
        (30, 70, -8, -2), (30, 88, -8, 4), (36, 104, -6, 7), (98, 70, 8, -2), (98, 88, 8, 4), (92, 104, 6, 7), (64, 114, 0, 8), (48, 112, -3, 8), (80, 112, 3, 8)])
    + f'<path d="M40 70 Q64 56 88 70 Q88 100 64 104 Q40 100 40 70Z" fill="#F4F0D0" {W(2.6)}/>'
    + f'<ellipse cx="64" cy="82" rx="20" ry="18" fill="#8B4A22" {W(3)}/>'
    + '<ellipse cx="57" cy="74" rx="6" ry="3.5" fill="#fff" opacity=".45"/>'
    + f'<path d="M50 92 Q64 98 78 92" fill="none" stroke="#D9B48A" stroke-width="3" stroke-linecap="round"/>'
    + f(64, 82, d=8, k=0.6)
    + sparkle(104, 26, 4, "#fff") + sparkle(110, 52, 2.6, "#fff"))

# Парк «Чермянка» — деревянный мостик-горбик через речку
I["chermyanka-park"] = ("#E6F7FF", "#7FC8EE",
    "деревянный мостик-горбик с перилами",
    "перекинут через речку между зелёными берегами, на середине стоит малыш в жёлтом дождевике и смотрит на рыбку",
    f'<path d="M0 74 Q30 70 44 84 L40 128 H0Z M128 74 Q98 70 84 84 L88 128 H128Z" fill="#7CCB62" {W(2.6)}/>'
    + f'<path d="M44 84 Q64 92 84 84 L88 128 H40Z" fill="#4FA3F0" {W(2.6)}/>'
    + f'<path d="M54 104 Q60 100 66 104 M66 116 Q72 112 78 116" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    + f'<path d="M58 110 Q64 104 70 110 Q64 116 58 110Z M70 110 l5 -4 v8Z" fill="#FF9A3C" {W(2)}/>'
    + f'<path d="M16 84 Q64 44 112 84 L112 92 Q64 54 16 92Z" fill="#C98A4B" {W(3)}/>'
    + "".join(f'<path d="M{x} {y} V{y-16}" {W(2.6)}/>' for x, y in [(26, 80), (44, 66), (64, 60), (84, 66), (102, 80)])
    + f'<path d="M24 64 Q64 28 104 64" fill="none" {W(3)}/>'
    + f'<path d="M58 60 L56 42 Q64 36 72 42 L70 60Z" fill="#FFD23F" {W(2.6)}/>'
    + f'<circle cx="64" cy="34" r="8" fill="#FFD9B8" {W(2.6)}/>'
    + f'<path d="M55 32 Q64 20 73 32Z" fill="#FFD23F" {W(2.4)}/>'
    + f'<path d="M60 37 Q62 39 64 37 M66 37 Q68 39 70 37" fill="none" {W(1.8)}/>'
    + sparkle(104, 22, 4, "#fff") + sparkle(22, 30, 3, "#fff"))

# Студия творчества «Лайн-арт» (Жуковский) — скетчбук с акварельным закатом
I["line-art-zhukovsky"] = ("#FFE3F0", "#F28DB8",
    "скетчбук на металлической спирали с акварельным закатом на странице",
    "лежит раскрытым на траве, рядом кисточка с каплей краски, вокруг разноцветные брызги",
    f'<path d="M0 100 Q64 90 128 100 V128 H0Z" fill="#9CD86B" {W(2.6)}/>'
    + f'<path d="M18 40 L102 34 L110 98 L24 104Z" fill="#FFFFFF" {W(3.2)}/>'
    + f'<path d="M28 50 L98 45 L102 74 L31 79Z" fill="#FFC36A"/>'
    + f'<path d="M28 50 L98 45 L99 56 L29 61Z" fill="#B79BFF" opacity=".85"/>'
    + f'<circle cx="64" cy="70" r="10" fill="#FF6F61"/>'
    + f'<path d="M31 79 L102 74 L103 84 L32 89Z" fill="#4FA3F0"/>'
    + f'<path d="M40 84 Q48 82 54 84 M70 82 Q78 80 86 82" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{18+i*10.6}" cy="{40-i*0.75}" r="4" fill="none" {W(2.4)}/>' for i in range(9))
    + f(66, 94, d=9, k=0.55, blush=False)
    + f'<path d="M86 116 L120 60" stroke="#C98A4B" stroke-width="6" stroke-linecap="round"/>'
    + f'<path d="M86 116 L120 60" fill="none" {W(1.8)}/>'
    + f'<path d="M116 60 L124 66 L126 52Z" fill="#7E6BF2" {W(2.2)}/>'
    + f'<path d="M124 48 Q128 42 126 40" fill="none" {W(1)}/>'
    + '<circle cx="14" cy="118" r="4" fill="#7E6BF2"/><circle cx="26" cy="112" r="3" fill="#FFB547"/><circle cx="110" cy="20" r="4" fill="#4FA3F0"/>'
    + sparkle(40, 22, 4, "#fff"))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
