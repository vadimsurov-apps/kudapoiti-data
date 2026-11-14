"""Робот «художник», 14.11 ~08:00 UTC.
check_unique.py: 12 пар похожих картинок (одна фигура на одинаковом сиреневом/персиковом/розовом/бирюзовом фоне).
Перерисованы 6 иконок, покрывающих все пары; у каждой своя идея, свой герой и своя палитра фона.
Запуск из корня: python3 tools/icons_artist_1114_0800.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}
SK = "#FFD9B8"   # кожа

# FD (Беляево) — гимнастический мостик-трамплин подкидывает мальчика вверх
I["fd-profsoyuznaya-83"] = (
    "зелёный гимнастический мостик-трамплин с жёлтым настилом и мордашкой",
    "подкидывает высоко вверх мальчика в синем трико, который летит свечкой с поднятыми руками над коралловым залом",
    ("#FFE6DC", "#E25A45"), f'''
<path d="M0 110 H128 V128 H0Z" fill="#2E4FA8"/>
<path d="M0 110 H128" {W(2.6)}/>
<path d="M16 110 L108 110 L108 92 L16 104Z" fill="#3BA55C" {W(3)}/>
<path d="M16 104 L108 92 L108 86 L16 99Z" fill="#F7D27A" {W(3)}/>
{eye(70, 101, .55)}{eye(84, 99.5, .55)}
{smile(77, 103, 3, .7)}
<path d="M56 82 Q64 88 72 82 M52 88 Q64 96 76 88" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".85"/>
<path d="M59 62 L58 78 M69 62 L70 78" {W(8)}/>
<path d="M59 62 L58 78 M69 62 L70 78" stroke="#2B4FC2" stroke-width="4.6" stroke-linecap="round"/>
<ellipse cx="57.5" cy="79" rx="3.4" ry="2.2" fill="{SK}" {W(2)}/><ellipse cx="70.5" cy="79" rx="3.4" ry="2.2" fill="{SK}" {W(2)}/>
<path d="M57 46 L43 22 M71 46 L85 22" {W(7.5)}/>
<path d="M57 46 L43 22 M71 46 L85 22" stroke="{SK}" stroke-width="4.2" stroke-linecap="round"/>
<rect x="54" y="44" width="20" height="21" rx="7" fill="#2B4FC2" {W(3)}/>
<circle cx="64" cy="36" r="10" fill="{SK}" {W(3)}/>
<path d="M54 34 Q56 24 64 25 Q72 24 74 34 Q68 29 64 31 Q60 29 54 34Z" fill="#7A4A26" {W(2.2)}/>
{eye(60, 37, .5)}{eye(68, 37, .5)}{blush(56.5, 41, .5)}{blush(71.5, 41, .5)}
<ellipse cx="64" cy="42" rx="2.2" ry="2.6" fill="{O}"/>
{sparkle(28, 40, 5)}{sparkle(100, 30, 4)}{sparkle(98, 62, 3)}''')

# FD (Видное) — девочка идёт по бревну, а за ней так же важно шагает воробей
I["fd-vidnoe-olimpiyskaya"] = (
    "девочка в жёлтом купальнике с двумя хвостиками на макушке",
    "идёт на носочках по гимнастическому бревну, раскинув руки, а за ней, раскинув крылышки, так же важно шагает воробей",
    ("#F0FCDD", "#62AE36"), f'''
<path d="M30 92 L26 128 M98 92 L102 128" {W(7)}/><path d="M30 92 L26 128 M98 92 L102 128" stroke="#8E5A2B" stroke-width="3.8"/>
<rect x="6" y="82" width="116" height="11" rx="4" fill="#E9B97A" {W(3)}/>
<path d="M51 66 L49 81 M59 66 L60 81" {W(7.5)}/>
<path d="M51 66 L49 81 M59 66 L60 81" stroke="{SK}" stroke-width="4.2" stroke-linecap="round"/>
<path d="M47 82 Q49 79 52 82Z M58 82 Q61 79 63 82Z" fill="{SK}" {W(2)}/>
<path d="M50 50 L26 47 M60 50 L84 47" {W(7.5)}/>
<path d="M50 50 L26 47 M60 50 L84 47" stroke="{SK}" stroke-width="4.2" stroke-linecap="round"/>
<path d="M47 47 Q55 44 63 47 L62 62 Q60 69 55 68 Q50 69 48 62Z" fill="#FFCC1F" {W(3)}/>
{sparkle(52, 55, 1.8)}{sparkle(58, 60, 1.4)}
<circle cx="55" cy="35" r="10" fill="{SK}" {W(3)}/>
<path d="M45 33 Q47 24 55 24 Q63 24 65 33 Q60 28 55 29 Q50 28 45 33Z" fill="#5A3317" {W(2.2)}/>
<path d="M47 27 Q40 18 36 24 Q40 28 47 29Z M63 27 Q70 18 74 24 Q70 28 63 29Z" fill="#5A3317" {W(2)}/>
<circle cx="47" cy="27" r="2" fill="#FF4F8B"/><circle cx="63" cy="27" r="2" fill="#FF4F8B"/>
{eye(51, 36, .5)}{eye(59, 36, .5)}{blush(47.5, 40, .5)}{blush(62.5, 40, .5)}{smile(55, 40, 2.6, .6)}
<path d="M98 74 L96 82 M104 74 L105 82" {W(2.2)}/>
<ellipse cx="101" cy="68" rx="10" ry="8" fill="#A0673A" {W(2.6)}/>
<ellipse cx="102" cy="71" rx="6" ry="4.5" fill="#F3DDBE"/>
<path d="M95 64 Q86 54 82 60 Q86 66 95 67Z" fill="#7B4A24" {W(2.2)}/>
<path d="M107 64 Q116 54 120 60 Q116 66 108 67Z" fill="#7B4A24" {W(2.2)}/>
<path d="M110 70 L118 76 L110 75Z" fill="#7B4A24" {W(2)}/>
<circle cx="96" cy="58" r="6.5" fill="#A0673A" {W(2.4)}/>
<path d="M90 58 L85 60 L90 61Z" fill="#F2A33A" {W(1.6)}/>
{eye(94.5, 57, .38)}''')

# «Амадина» (Северное Бутово) — скакалка дугой, через неё прыгает птичка-амадина
I["amadina-kulikovskaya"] = (
    "красная гимнастическая скакалка с деревянными ручками-мордашками",
    "раскачивается петлёй вниз между раскинутыми ручками, а над ней подпрыгивает маленькая птичка-амадина с оранжевым клювом",
    ("#FFF7D1", "#E9A90E"), f'''
<path d="M24 44 C26 132 102 132 104 44" fill="none" {W(8.5)}/>
<path d="M24 44 C26 132 102 132 104 44" fill="none" stroke="#E8243C" stroke-width="5" stroke-linecap="round"/>
<g transform="rotate(-28 22 34)"><rect x="14" y="16" width="16" height="32" rx="8" fill="#D99A55" {W(3)}/>
{eye(19, 30, .45)}{eye(25, 30, .45)}{smile(22, 35, 2.4, .6)}</g>
<g transform="rotate(28 106 34)"><rect x="98" y="16" width="16" height="32" rx="8" fill="#D99A55" {W(3)}/>
{eye(103, 30, .45)}{eye(109, 30, .45)}{smile(106, 35, 2.4, .6)}</g>
<path d="M80 56 L92 50 L91 56 L92 62Z" fill="#3B3355" {W(1.8)}/>
<path d="M84 53 L88 51 M84 59 L88 61" stroke="#fff" stroke-width="1.6"/>
<ellipse cx="68" cy="58" rx="15" ry="12" fill="#A3A1AE" {W(3)}/>
<ellipse cx="66" cy="63" rx="9" ry="6" fill="#FFF4E8"/>
<ellipse cx="74" cy="56" rx="7.5" ry="4.5" fill="#7F7D8A" transform="rotate(-15 74 56)" {W(2.2)}/>
<ellipse cx="57" cy="57" rx="4" ry="3.2" fill="#F28C38"/>
<path d="M54 49 L45 52 L54 55Z" fill="#F25C1E" {W(1.8)}/>
{eye(59, 50, .45)}
<path d="M64 70 L62 76 M70 70 L71 76" {W(2)}/>
<path d="M54 84 Q64 90 74 84" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".8"/>
{sparkle(64, 26, 4.5)}{sparkle(98, 80, 3)}{sparkle(30, 80, 3)}''')

# FD (Коммунарка) — акробатическая пирамида из трёх ребят
I["fd-kommunarka"] = (
    "три ребёнка-акробата: двое крепышей внизу и малышка в розовом сверху",
    "строят пирамиду на голубом мате: малышка стоит у друзей на плечах и раскинула руки буквой V под звёздами",
    ("#AEB8F6", "#27337F"), f'''
<path d="M0 114 H128 V128 H0Z" fill="#8FD3F2"/><path d="M0 114 H128" {W(2.4)}/>
<path d="M40 100 L39 114 M48 100 L49 114" {W(7)}/><path d="M40 100 L39 114 M48 100 L49 114" stroke="{SK}" stroke-width="3.8" stroke-linecap="round"/>
<path d="M80 100 L79 114 M88 100 L89 114" {W(7)}/><path d="M80 100 L79 114 M88 100 L89 114" stroke="{SK}" stroke-width="3.8" stroke-linecap="round"/>
<rect x="33" y="78" width="22" height="25" rx="7" fill="#E53935" {W(3)}/>
<rect x="73" y="78" width="22" height="25" rx="7" fill="#2EAD5B" {W(3)}/>
<path d="M54 84 L74 84" {W(7)}/><path d="M54 84 L74 84" stroke="{SK}" stroke-width="3.8" stroke-linecap="round"/>
<path d="M34 82 L26 98 M94 82 L102 98" {W(7)}/><path d="M34 82 L26 98 M94 82 L102 98" stroke="{SK}" stroke-width="3.8" stroke-linecap="round"/>
<circle cx="44" cy="69" r="9" fill="{SK}" {W(2.8)}/><path d="M35 67 Q37 59 44 59 Q51 59 53 67 Q48 63 44 64 Q40 63 35 67Z" fill="#2E2A3A"/>
{eye(40.5, 70, .42)}{eye(47.5, 70, .42)}{smile(44, 74, 2.2, .55)}
<circle cx="84" cy="69" r="9" fill="{SK}" {W(2.8)}/><path d="M75 67 Q77 59 84 59 Q91 59 93 67 Q88 63 84 64 Q80 63 75 67Z" fill="#C46A22"/>
{eye(80.5, 70, .42)}{eye(87.5, 70, .42)}{smile(84, 74, 2.2, .55)}
<path d="M60 56 L54 78 M68 56 L74 78" {W(6.5)}/><path d="M60 56 L54 78 M68 56 L74 78" stroke="{SK}" stroke-width="3.4" stroke-linecap="round"/>
<path d="M56 40 L46 18 M72 40 L82 18" {W(6.5)}/><path d="M56 40 L46 18 M72 40 L82 18" stroke="{SK}" stroke-width="3.4" stroke-linecap="round"/>
<path d="M56 38 Q64 35 72 38 L70 54 Q64 60 58 54Z" fill="#FF5FA2" {W(2.8)}/>
<circle cx="64" cy="28" r="8.5" fill="{SK}" {W(2.8)}/>
<path d="M55.5 27 Q57 19 64 19 Q71 19 72.5 27 Q68 23 64 24 Q60 23 55.5 27Z" fill="#F2C14E"/>
<circle cx="64" cy="18" r="3.2" fill="#F2C14E" {W(1.8)}/>
{eye(61, 29, .4)}{eye(67, 29, .4)}{smile(64, 32.5, 2, .5)}
{sparkle(24, 40, 4.5, "#FFE680")}{sparkle(104, 36, 4, "#FFE680")}{sparkle(98, 58, 2.6)}{sparkle(30, 58, 2.4)}''')

# «АйДаКодить» — лесенка цветных блоков визуального кода, верхний «старт» с мордашкой
I["codims-proizvodstvennaya"] = (
    "стопка цветных блоков визуального программирования с зубчиками",
    "сцепились лесенкой: улыбчивый зелёный блок «старт» с флажком сверху, под ним оранжевый «шаг вперёд» и фиолетовый «повторить»",
    ("#E2F4FF", "#2F8BD6"), f'''
<path d="M20 50 Q20 30 40 30 L56 30 Q64 22 72 30 L84 30 Q90 30 90 36 L90 50 L44 50 L42 54 L34 54 L32 50Z" fill="#3CC46A" {W(3)}/>
{eye(46, 40, .55)}{eye(58, 40, .55)}{blush(41, 45, .55)}{blush(63, 45, .55)}{smile(52, 44, 3, .7)}
<path d="M74 46 V32" {W(2.4)}/><path d="M74 32 L84 35 L74 39Z" fill="#FFE14D" {W(2)}/>
<path d="M30 54 L32 54 L34 58 L42 58 L44 54 L100 54 Q104 54 104 58 L104 70 Q104 74 100 74 L56 74 L54 78 L46 78 L44 74 L34 74 Q30 74 30 70Z" fill="#FF9A1F" {W(3)}/>
<path d="M60 64 H84 M78 58 L85 64 L78 70" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M42 78 L44 78 L46 82 L54 82 L56 78 L108 78 Q112 78 112 82 L112 96 Q112 100 108 100 L46 100 Q42 100 42 96Z" fill="#8E5BE8" {W(3)}/>
<path d="M84 89 A7 7 0 1 1 77 82" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/>
<path d="M75 78 L79 82 L74 85" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
{sparkle(104, 34, 4.5)}{sparkle(24, 82, 3.5)}{sparkle(30, 108, 2.6)}''')

# FD (Бибирево) — ёжик-гимнаст делает кувырок по мату
I["fd-konenkova"] = (
    "колючий ёжик-гимнаст с розовым бантиком на иголке",
    "делает кувырок вперёд по синему гимнастическому мату и, перевернувшись вверх тормашками, улыбается, а за ним тянется дуга-след",
    ("#FFEDD3", "#EE7A12"), f'''
<rect x="8" y="98" width="112" height="16" rx="5" fill="#2F5FD0" {W(3)}/>
<path d="M30 98 V114 M64 98 V114 M98 98 V114" stroke="#1E3F95" stroke-width="2"/>
<path d="M14 88 Q22 46 50 40" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-dasharray="2 7" opacity=".9"/>
<path d="M66 32 L70 24 L74 33 L80 26 L82 36 L89 31 L89 41 L97 39 L94 48 L102 50 L96 56 L103 62 L95 65 L100 73 L91 74 L93 82 L84 80 L83 89 L76 84 L71 92 L67 84 L60 90 L58 81 L50 84 L51 75 L42 74 L47 67 L39 62 L46 57 L40 50 L49 48 L46 40 L55 41 L56 32 L62 37Z" fill="#7A4E2C" {W(2.8)}/>
<circle cx="70" cy="61" r="21" fill="#F4D8B0" {W(2.8)}/>
<path d="M67 83 Q63 92 57 92" fill="none" {W(2.4)}/>
<g transform="rotate(180 70 61)">
{eye(63, 58, .6)}{eye(77, 58, .6)}
<ellipse cx="70" cy="66" rx="3" ry="2.2" fill="{O}"/>
{blush(59, 65, .6)}{blush(81, 65, .6)}
<path d="M66 69 Q70 73 74 69" fill="none" {W(2.2)}/>
</g>
<ellipse cx="56" cy="88" rx="5" ry="3.4" fill="#F4D8B0" {W(2.2)}/><ellipse cx="86" cy="88" rx="5" ry="3.4" fill="#F4D8B0" {W(2.2)}/>
<path d="M78 26 Q70 18 70 26 Q70 32 78 28 Q86 32 86 26 Q86 18 78 26Z" fill="#FF5FA2" {W(2)}/>
<circle cx="78" cy="27" r="2.2" fill="#FF5FA2" {W(1.6)}/>
{sparkle(108, 26, 4.5)}{sparkle(24, 24, 3.5)}{sparkle(110, 84, 3)}''')

if __name__ == "__main__":
    for pid, (hero, scene, (a, b), body) in I.items():
        open(os.path.join(ROOT, "icons-src", f"{pid}.svg"), "w").write(bgsvg(a, b, body))
    reg = os.path.join(ROOT, "icons-src", "subjects.txt"); txt = open(reg, encoding="utf-8").read()
    for pid in I:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    if not txt.endswith("\n"):
        txt += "\n"
    txt += "".join(f"{pid} — герой: {h} | сцена: {sc}\n" for pid, (h, sc, _, _) in I.items())
    open(reg, "w", encoding="utf-8").write(txt)
    print(" ".join(I))
