"""Робот «художник», 07.11 ~05:00 UTC: 40 иконок из auto/icon-repeats.json (больше всего похожих пар —
серии баскетбола/волейбола/шахмат/бассейнов и кафе старого генератора). Каждая придумана и нарисована
отдельно, вручную: свой герой по теме места, своя сцена, свой ракурс и своя палитра фона.
Запуск из корня: python3 tools/icons_artist_1107_0500.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

# ---------- БАСКЕТБОЛ ----------

# 1. IBASKET Реутов — девочка ведёт мяч по паркету
I["ibasket-reutov"] = ("девочка с двумя хвостиками в красной майке", "ведёт баскетбольный мяч низким дриблингом по паркету", ("#E6F4FF", "#3F74D0"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#E8B57A" {W(2.4)}/><path d="M20 104 L14 128 M52 104 L50 128 M86 104 L90 128 M118 104 L126 128" stroke="#C98E52" stroke-width="2"/>
<path d="M46 80 L36 102 L28 102 M62 80 L74 100 L82 96" fill="none" {W(5)}/>
<path d="M46 80 L36 102 L28 102 M62 80 L74 100 L82 96" fill="none" stroke="#FFD9B8" stroke-width="2"/>
<path d="M42 78 Q54 84 66 78 L64 88 Q54 92 44 88Z" fill="#2A2F5A" {W(2.6)}/>
<path d="M42 52 Q54 46 66 52 L66 80 Q54 84 42 80Z" fill="#E8384A" {W(3)}/>
<text x="54" y="74" font-family="Arial" font-weight="bold" font-size="14" fill="#fff" text-anchor="middle">7</text>
<path d="M44 58 L30 72 M64 58 L84 76" fill="none" {W(5)}/><path d="M44 58 L30 72 M64 58 L84 76" fill="none" stroke="#FFD9B8" stroke-width="2"/>
<circle cx="54" cy="34" r="15" fill="#FFD9B8" {W(3)}/>
<path d="M39 32 Q42 16 56 18 Q68 20 69 32 Q60 24 48 28Z" fill="#7A4424" {W(2.4)}/>
<path d="M40 26 Q28 22 26 34 Q32 32 38 34Z M68 26 Q80 22 82 34 Q76 32 70 34Z" fill="#7A4424" {W(2.2)}/>
{eye(49, 36, .45)}{eye(60, 36, .45)}{smile(55, 42, 3, .6)}{blush(45, 41, .5)}{blush(64, 41, .5)}
<circle cx="92" cy="92" r="12" fill="#F2892A" {W(3)}/><path d="M80 92 H104 M92 80 V104 M84 83 Q90 92 84 101 M100 83 Q94 92 100 101" fill="none" stroke="{O}" stroke-width="1.8"/>
<path d="M90 70 V76 M98 70 V76 M106 74 L102 79" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 2. «Стремление» Тимирязевская — трёхочковый бросок по пунктирной дуге
I["stremlenie-basket-timiryazevskaya"] = ("баскетбольный мяч в полёте с зажмуренными от азарта глазами", "летит по пунктирной дуге трёхочкового броска из угла площадки прямо в кольцо", ("#E4FFF6", "#2A9C86"), f'''
<path d="M-10 128 Q20 92 60 128" fill="none" stroke="#fff" stroke-width="3"/>
<rect x="84" y="14" width="34" height="26" rx="3" fill="#fff" {W(3)}/><rect x="94" y="22" width="14" height="11" fill="none" stroke="#E8384A" stroke-width="2.6"/>
<path d="M101 40 V46" {W(3)}/>
<path d="M90 48 L94 66 L108 66 L112 48" fill="none" stroke="#fff" stroke-width="2"/><path d="M94 48 L100 66 M101 48 L101 66 M108 48 L102 66" stroke="#fff" stroke-width="1.6"/>
<ellipse cx="101" cy="48" rx="12" ry="3.5" fill="none" stroke="#F25A2A" stroke-width="3.4"/>
<path d="M44 84 Q60 26 96 40" fill="none" stroke="#fff" stroke-width="2.6" stroke-dasharray="5 5"/>
<circle cx="34" cy="92" r="21" fill="#F2892A" {W(3)}/>
<path d="M13 92 H55 M34 71 V113 M20 77 Q30 92 20 107 M48 77 Q38 92 48 107" fill="none" stroke="{O}" stroke-width="2"/>
<path d="M24 92 Q27 88 30 92 M38 92 Q41 88 44 92" fill="none" {W(2.2)}/><path d="M29 99 Q34 104 39 99" fill="#fff" {W(2)}/>
{sparkle(70, 24, 5)}{sparkle(58, 52, 3.5)}''')

# 3. IBASKET Строгино — мяч на ободе кольца: залетит или нет?
I["ibasket-strogino"] = ("баскетбольный мяч с испуганной мордочкой", "балансирует на самом краю оранжевого обода кольца — залетит или нет", ("#F3EAFF", "#7E5CCB"), f'''
<rect x="8" y="10" width="112" height="46" rx="4" fill="#fff" opacity=".9" {W(3)}/><rect x="42" y="24" width="44" height="30" fill="none" stroke="#E8384A" stroke-width="3"/>
<path d="M54 56 V66 M74 56 V66" {W(3)}/>
<path d="M22 76 L36 116 H92 L106 76" fill="none" stroke="#fff" stroke-width="2.6"/>
<path d="M36 76 L50 116 M54 76 L58 116 M74 76 L70 116 M92 76 L78 116 M28 96 H100" stroke="#fff" stroke-width="2"/>
<ellipse cx="64" cy="74" rx="44" ry="10" fill="none" stroke="{O}" stroke-width="8"/>
<ellipse cx="64" cy="74" rx="44" ry="10" fill="none" stroke="#F25A2A" stroke-width="4.4"/>
<circle cx="30" cy="54" r="18" fill="#F2892A" {W(3)}/>
<path d="M12 54 H48 M30 36 V72 M18 40 Q26 54 18 68 M42 40 Q34 54 42 68" fill="none" stroke="{O}" stroke-width="1.8"/>
{eye(25, 52, .5)}{eye(36, 52, .5)}<ellipse cx="30" cy="61" rx="3" ry="2.4" fill="{O}"/>
<path d="M47 40 Q50 34 48 30 Q44 36 47 40Z" fill="#8FD8FF" {W(1.6)}/>
<path d="M8 66 Q2 60 6 52 M52 66 Q58 60 54 52" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 4. IBASKET Переяславская — малыш на плечах у папы кладёт мяч в кольцо
I["ibasket-pereyaslavskaya"] = ("малыш в зелёной майке на плечах у папы", "дотягивается до кольца и аккуратно кладёт в него баскетбольный мяч", ("#F1FFE9", "#4CAF5C"), f'''
<rect x="78" y="8" width="44" height="30" rx="3" fill="#fff" {W(3)}/><rect x="92" y="18" width="18" height="14" fill="none" stroke="#E8384A" stroke-width="2.6"/>
<path d="M88 44 L92 62 H108 L112 44" fill="none" stroke="#fff" stroke-width="2"/><path d="M94 44 L98 62 M100 44 V62 M106 44 L102 62" stroke="#fff" stroke-width="1.6"/>
<ellipse cx="100" cy="44" rx="13" ry="3.6" fill="none" stroke="#F25A2A" stroke-width="3.6"/>
<path d="M30 128 Q30 92 52 88 Q74 92 74 128Z" fill="#3A6AD8" {W(3)}/>
<circle cx="52" cy="76" r="13" fill="#E8B48A" {W(3)}/><path d="M39 72 Q42 62 52 62 Q62 62 65 72 Q54 66 39 72Z" fill="#4A3020" {W(2)}/>
<path d="M47 78 Q49 76 51 78 M55 78 Q57 76 59 78" fill="none" {W(1.8)}/><path d="M48 84 Q52 87 56 84" fill="none" {W(2)}/>
<path d="M40 64 L32 78 M64 64 L70 78" fill="none" {W(5)}/><path d="M40 64 L32 78 M64 64 L70 78" fill="none" stroke="#FFD9B8" stroke-width="2"/>
<path d="M40 42 Q52 38 64 44 L62 64 Q52 66 42 64Z" fill="#4CC85A" {W(3)}/>
<path d="M60 46 L80 34" fill="none" {W(5)}/><path d="M60 46 L80 34" fill="none" stroke="#FFD9B8" stroke-width="2"/>
<circle cx="50" cy="30" r="11" fill="#FFD9B8" {W(2.8)}/><path d="M40 28 Q42 18 52 19 Q60 20 61 28 Q52 24 40 28Z" fill="#E8B030" {W(2)}/>
{eye(47, 31, .38)}{eye(55, 31, .38)}<path d="M48 36 Q51 38 54 36" fill="none" {W(1.8)}/>
<circle cx="88" cy="32" r="11" fill="#F2892A" {W(2.8)}/><path d="M77 32 H99 M88 21 V43 M80 24 Q85 32 80 40 M96 24 Q91 32 96 40" fill="none" stroke="{O}" stroke-width="1.6"/>
{sparkle(20, 40, 4)}{sparkle(112, 80, 3.4)}''')

# 5. «Стремление» Медведково — мальчик висит на кольце после броска сверху
I["stremlenie-basket-medvedkovo"] = ("мальчик-баскетболист в жёлтой форме", "висит на кольце после броска сверху, а мяч проваливается в сетку", ("#FFEDE6", "#DA5440"), f'''
<rect x="26" y="4" width="76" height="30" rx="3" fill="#fff" {W(3)}/><rect x="50" y="12" width="28" height="18" fill="none" stroke="#E8384A" stroke-width="2.6"/>
<path d="M46 40 L52 62 H76 L82 40" fill="none" stroke="#fff" stroke-width="2"/><path d="M54 40 L58 62 M64 40 V62 M74 40 L70 62" stroke="#fff" stroke-width="1.6"/>
<circle cx="64" cy="66" r="9" fill="#F2892A" {W(2.4)}/><path d="M55 66 H73 M64 57 V75" stroke="{O}" stroke-width="1.6"/>
<ellipse cx="64" cy="40" rx="19" ry="4" fill="none" stroke="#F25A2A" stroke-width="3.6"/>
<path d="M90 40 L92 34 M100 42 L98 36" fill="none" {W(2)}/>
<path d="M82 40 L94 56 M86 38 L100 54" fill="none" {W(5)}/><path d="M82 40 L94 56 M86 38 L100 54" fill="none" stroke="#C88A5A" stroke-width="2"/>
<circle cx="96" cy="62" r="11" fill="#C88A5A" {W(3)}/><path d="M86 58 Q90 48 100 50 Q106 52 106 60 Q98 54 90 60Z" fill="{O}"/>
{eye(92, 64, .4)}{eye(101, 64, .4)}<path d="M93 69 Q97 72 101 69" fill="none" {W(2)}/>
<path d="M88 72 Q96 70 104 72 L106 98 H86Z" fill="#FFD23F" {W(3)}/><text x="96" y="91" font-family="Arial" font-weight="bold" font-size="11" fill="#D2402A" text-anchor="middle">23</text>
<path d="M86 98 H106 L104 108 H88Z" fill="#2A2F5A" {W(2.4)}/>
<path d="M90 108 L86 122 M102 108 L106 122" fill="none" {W(5)}/><path d="M90 108 L86 122 M102 108 L106 122" fill="none" stroke="#C88A5A" stroke-width="2"/>
<path d="M78 124 H90 M102 124 H114" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<path d="M20 70 L30 74 M16 86 L28 86 M22 100 L32 96" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

# ---------- ВОЛЕЙБОЛ (жёлто-синий мяч) ----------

# 6. Nevsky Bears Люблино — мяч-канатоходец на сетке
I["nevsky-bears-lyublino"] = ("жёлто-синий волейбольный мяч-канатоходец", "идёт по верхней ленте волейбольной сетки, раскинув ручки для равновесия", ("#FFE9F2", "#BC4A84"), f'''
<path d="M12 70 V128 M116 70 V128" stroke="{O}" stroke-width="7"/><path d="M12 70 V128 M116 70 V128" stroke="#fff" stroke-width="3" stroke-dasharray="6 6"/>
<path d="M12 76 H116 V112 H12Z" fill="none" stroke="#fff" stroke-width="1.6"/>
<path d="M12 84 H116 M12 92 H116 M12 100 H116 M24 76 V112 M36 76 V112 M48 76 V112 M60 76 V112 M72 76 V112 M84 76 V112 M96 76 V112 M108 76 V112" stroke="#fff" stroke-width="1.4" opacity=".85"/>
<rect x="10" y="70" width="108" height="7" rx="2" fill="#fff" {W(2.4)}/>
<path d="M40 50 L22 40 M88 50 L106 40" fill="none" {W(3)}/><circle cx="21" cy="39" r="3" fill="#fff" {W(2)}/><circle cx="107" cy="39" r="3" fill="#fff" {W(2)}/>
<path d="M56 68 V72 M72 68 V72" {W(3)}/>
<circle cx="64" cy="46" r="22" fill="#FFD23F" {W(3)}/>
<path d="M42 44 Q56 36 64 24 M86 48 Q70 50 62 68 M50 30 Q66 46 84 34" fill="none" stroke="#2D5BD1" stroke-width="5"/>
<path d="M42 44 Q56 36 64 24 M86 48 Q70 50 62 68 M50 30 Q66 46 84 34" fill="none" stroke="{O}" stroke-width="1.4"/>
{eye(57, 48, .45)}{eye(70, 48, .45)}<path d="M59 56 Q64 59 69 56" fill="none" {W(2.2)}/>''')

# 7. Nevsky Bears Печатники — девочка принимает мяч снизу
I["nevsky-bears-pechatniki"] = ("девочка-волейболистка в белых наколенниках", "присев, принимает мяч снизу, сцепив руки «замком»", ("#EAF8FF", "#2A86B0"), f'''
<path d="M0 112 H128 V128 H0Z" fill="#3C9A6A" {W(2.4)}/>
<path d="M48 84 L40 98 L46 110 M66 84 L76 96 L72 110" fill="none" {W(6)}/><path d="M48 84 L40 98 L46 110 M66 84 L76 96 L72 110" fill="none" stroke="#FFD9B8" stroke-width="2.6"/>
<rect x="35" y="92" width="10" height="9" rx="3" fill="#fff" {W(2)}/><rect x="71" y="90" width="10" height="9" rx="3" fill="#fff" {W(2)}/>
<path d="M40 112 H50 M68 112 H80" stroke="#E8384A" stroke-width="6" stroke-linecap="round"/>
<path d="M44 78 Q57 74 70 78 L68 88 H46Z" fill="#1E2A5A" {W(2.4)}/>
<path d="M44 54 Q57 48 70 54 L70 80 Q57 84 44 80Z" fill="#1EB6C8" {W(3)}/>
<path d="M50 60 L84 80 M64 60 L86 76" fill="none" {W(5)}/><path d="M50 60 L84 80 M64 60 L86 76" fill="none" stroke="#FFD9B8" stroke-width="2"/>
<circle cx="57" cy="38" r="14" fill="#FFD9B8" {W(3)}/>
<path d="M43 36 Q44 22 58 22 Q70 22 71 34 Q60 28 50 32Z" fill="#2A1A14" {W(2.2)}/><path d="M44 30 Q34 36 36 48" fill="none" stroke="#2A1A14" stroke-width="5" stroke-linecap="round"/>
{eye(53, 40, .42)}{eye(63, 40, .42)}<path d="M55 46 Q58 48 61 46" fill="none" {W(2)}/>
<circle cx="98" cy="50" r="16" fill="#FFD23F" {W(3)}/>
<path d="M82 48 Q94 44 98 34 M114 52 Q102 52 98 66 M88 38 Q100 50 112 42" fill="none" stroke="#2D5BD1" stroke-width="4"/>
<path d="M100 70 V76 M92 70 L90 76" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 8. Nevsky Bears Алексеевская — мяч шлёпается у линии: ас!
I["nevsky-bears-alekseevskaya"] = ("сплющенный от удара жёлто-синий мяч", "шлёпается о площадку у самой белой линии — ас! — и разлетаются искры", ("#FBFFE6", "#86B530"), f'''
<path d="M0 84 L128 70 V128 H0Z" fill="#F08A3C" {W(2.6)}/>
<path d="M0 104 L128 88" stroke="#fff" stroke-width="5"/>
<ellipse cx="62" cy="88" rx="30" ry="15" fill="#FFD23F" {W(3)}/>
<path d="M34 86 Q50 82 58 74 M90 90 Q74 92 66 102 M44 77 Q62 90 84 80" fill="none" stroke="#2D5BD1" stroke-width="4.4"/>
<path d="M53 88 L58 86 M66 85 L71 87" {W(2.4)}/><path d="M57 94 Q62 96 67 93" fill="none" {W(2)}/>
<path d="M22 70 L12 62 M30 62 L26 50 M96 66 L104 54 M104 76 L116 70 M62 64 V50" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
<path d="M88 22 L82 46 M98 24 L90 48 M108 26 L98 50" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".9"/>
<text x="40" y="40" font-family="Arial" font-weight="bold" font-size="20" fill="#fff" stroke="{O}" stroke-width="1.6" text-anchor="middle">АС!</text>''')

# 9. Nevsky Bears ЦСКА — верхняя передача
I["nevsky-bears-tsska"] = ("мальчик-связующий в синей форме", "делает верхнюю передачу пальцами над головой, глядя на мяч", ("#F0EEFF", "#4448B0"), f'''
<circle cx="64" cy="22" r="15" fill="#FFD23F" {W(3)}/>
<path d="M49 20 Q60 18 64 8 M79 24 Q68 24 64 36 M54 12 Q64 22 76 14" fill="none" stroke="#2D5BD1" stroke-width="4"/>
<path d="M44 46 L50 82 M84 46 L78 82" fill="none" {W(6)}/><path d="M44 46 L50 82 M84 46 L78 82" fill="none" stroke="#F4C79C" stroke-width="2.6"/>
<path d="M40 46 Q44 36 50 40 L48 48Z M88 46 Q84 36 78 40 L80 48Z" fill="#F4C79C" {W(2.4)}/>
<path d="M46 86 Q64 78 82 86 L84 120 H44Z" fill="#2D5BD1" {W(3)}/>
<text x="64" y="110" font-family="Arial" font-weight="bold" font-size="16" fill="#fff" text-anchor="middle">1</text>
<circle cx="64" cy="70" r="15" fill="#F4C79C" {W(3)}/>
<path d="M49 66 Q52 52 66 54 Q78 56 79 66 Q70 60 58 64Z" fill="#E0A040" {W(2.2)}/>
<ellipse cx="58" cy="70" rx="2.6" ry="3.4" fill="{O}"/><ellipse cx="70" cy="70" rx="2.6" ry="3.4" fill="{O}"/>
<circle cx="57.6" cy="68.6" r="1" fill="#fff"/><circle cx="69.6" cy="68.6" r="1" fill="#fff"/>
<ellipse cx="64" cy="78" rx="3" ry="2.4" fill="#C2405A"/>{blush(53, 76, .5)}{blush(75, 76, .5)}
<path d="M30 30 Q26 22 32 16 M98 30 Q102 22 96 16" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 10. «Фотон» Медведково — светящийся мяч-фотон над сеткой ночного зала
I["foton-volley-medvedkovo"] = ("сияющий жёлто-синий мяч-фотон", "летит над волейбольной сеткой ночного зала, оставляя световой след", ("#3B4196", "#0F1342"), f'''
<path d="M0 90 H128" stroke="#fff" stroke-width="5"/><path d="M0 98 H128 M0 106 H128 M0 114 H128 M10 90 V128 M26 90 V128 M42 90 V128 M58 90 V128 M74 90 V128 M90 90 V128 M106 90 V128 M122 90 V128" stroke="#8C94E0" stroke-width="1.4"/>
<path d="M10 82 Q40 70 60 52" fill="none" stroke="#FFE98A" stroke-width="10" stroke-linecap="round" opacity=".35"/>
<path d="M18 80 Q44 68 60 52" fill="none" stroke="#FFF6C0" stroke-width="4" stroke-linecap="round" opacity=".8"/>
<circle cx="76" cy="44" r="30" fill="#FFF2A0" opacity=".25"/><circle cx="76" cy="44" r="25" fill="#FFF2A0" opacity=".3"/>
<circle cx="76" cy="44" r="19" fill="#FFD23F" {W(3)}/>
<path d="M57 42 Q70 38 76 25 M95 46 Q82 46 76 63 M63 30 Q76 44 91 36" fill="none" stroke="#2D5BD1" stroke-width="4.2"/>
{eye(70, 46, .42)}{eye(82, 46, .42)}<path d="M72 53 Q76 56 80 53" fill="none" {W(2)}/>
{sparkle(108, 22, 5)}{sparkle(30, 26, 4)}{sparkle(110, 72, 3)}''')

# ---------- ШАХМАТЫ ----------

# 11. Шахматная школа №1, Филёвский парк — доска на пне
I["chess1-filevsky"] = ("шахматная доска на старом пне", "в Филёвском парке на клетку доски падает кленовый лист, рядом стоит белая пешка", ("#ECF8D8", "#3B8538"), f'''
<path d="M10 70 Q14 40 24 70Z M104 72 Q114 36 122 72Z" fill="#2E6E2E" {W(2.4)}/>
<path d="M30 92 Q28 116 22 124 H106 Q100 116 98 92Z" fill="#9A6236" {W(3)}/>
<path d="M44 100 V122 M64 98 V124 M84 100 V122" stroke="#7A4826" stroke-width="2"/>
<path d="M14 88 L64 70 L114 88 L64 106Z" fill="#F7E6C4" {W(3)}/>
<g transform="matrix(12.5,-4.5,12.5,4.5,14,88)"><path d="M1 0 H2 V1 H1Z M3 0 H4 V1 H3Z M0 1 H1 V2 H0Z M2 1 H3 V2 H2Z M1 2 H2 V3 H1Z M3 2 H4 V3 H3Z M0 3 H1 V4 H0Z M2 3 H3 V4 H2Z" fill="#7A4826"/></g>
<path d="M50 84 Q50 76 58 75 Q56 66 60 60 H68 Q72 66 70 75 Q78 76 78 84Z" fill="#fff" {W(2.6)}/>
<rect x="56" y="56" width="16" height="5" rx="2" fill="#fff" {W(2.4)}/>
<circle cx="64" cy="48" r="9" fill="#fff" {W(2.6)}/>
{eye(60, 49, .35)}{eye(68, 49, .35)}<path d="M61 53 Q64 55 67 53" fill="none" {W(1.8)}/>
<path d="M92 30 L96 40 L104 36 L102 44 L110 46 L102 50 L104 56 L96 52 L92 60 L88 52 L80 56 L82 50 L74 46 L82 44 L80 36 L88 40Z" fill="#F2742A" {W(2.2)} transform="rotate(-20 92 46)"/>
<path d="M86 64 Q90 58 92 52" fill="none" {W(2)}/>
<path d="M98 66 Q104 72 98 78" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 4"/>''')

# 12. «Север», Вятская — белый слон мчится по диагонали
I["sever-chess-vyatskaya"] = ("белый шахматный слон с прорезью на макушке", "мчится по диагонали доски, оставляя пунктирный след", ("#E6FAFF", "#4FA6CF"), f'''
<path d="M0 64 H128 V128 H0Z" fill="#fff"/>
<path d="M0 64 H16 V80 H0Z M32 64 H48 V80 H32Z M64 64 H80 V80 H64Z M96 64 H112 V80 H96Z M16 80 H32 V96 H16Z M48 80 H64 V96 H48Z M80 80 H96 V96 H80Z M112 80 H128 V96 H112Z M0 96 H16 V112 H0Z M32 96 H48 V112 H32Z M64 96 H80 V112 H64Z M96 96 H112 V112 H96Z M16 112 H32 V128 H16Z M48 112 H64 V128 H48Z M80 112 H96 V128 H80Z M112 112 H128 V128 H112Z" fill="#2A5A86"/>
<path d="M0 64 H128" {W(3)}/>
<path d="M24 120 L76 68" fill="none" stroke="#FF5A6A" stroke-width="3.4" stroke-dasharray="6 5"/>
<path d="M18 112 L12 118 M30 116 L24 122" stroke="#FF5A6A" stroke-width="3" stroke-linecap="round"/>
<path d="M70 80 Q66 68 74 60 L106 60 Q114 68 110 80Z" fill="#F4F8FF" {W(3)}/>
<path d="M76 60 Q70 40 90 22 Q110 40 104 60Z" fill="#F4F8FF" {W(3)}/>
<path d="M92 30 L84 44" {W(2.6)}/><circle cx="90" cy="18" r="5" fill="#F4F8FF" {W(2.6)}/>
<rect x="74" y="56" width="32" height="7" rx="3" fill="#C8DCF0" {W(2.4)}/>
{eye(85, 46, .42)}{eye(96, 46, .42)}<path d="M87 52 Q90 54 94 52" fill="none" {W(2)}/>
<path d="M60 40 H40 M64 30 H48 M60 50 H46" stroke="#fff" stroke-width="3" stroke-linecap="round"/>''')

# 13. «Восток», Новогиреево — деревянный конь прыгает буквой Г на рассвете
I["vostok-chess-novogireevo"] = ("рыжий деревянный шахматный конь", "на рассвете прыгает буквой «Г» по доске, стрелка показывает его ход", ("#FFF1D6", "#EE7A44"), f'''
<circle cx="100" cy="94" r="18" fill="#FFE27A" opacity=".9"/>
<path d="M0 98 H128 V128 H0Z" fill="#F7E3C4" {W(2.4)}/>
<path d="M0 98 H20 V113 H0Z M40 98 H60 V113 H40Z M80 98 H100 V113 H80Z M120 98 H128 V113 H120Z M20 113 H40 V128 H20Z M60 113 H80 V128 H60Z M100 113 H120 V128 H100Z" fill="#B0703E"/>
<path d="M24 92 V40 H60" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-dasharray="1 8"/>
<path d="M56 32 L68 40 L56 48" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M70 92 Q66 82 74 78 H104 Q112 82 108 92Z" fill="#D88A48" {W(3)}/>
<path d="M76 78 Q70 60 78 48 Q72 44 72 38 L82 30 Q84 22 92 22 Q108 24 110 48 Q112 64 104 78Z" fill="#E89A52" {W(3)}/>
<path d="M90 24 L94 14 L98 24" fill="#E89A52" {W(2.4)}/>
<path d="M104 30 Q110 40 108 56" fill="none" stroke="#B0703E" stroke-width="3"/>
{eye(88, 36, .45)}<ellipse cx="76" cy="40" rx="2" ry="1.6" fill="{O}"/>{blush(86, 44, .5)}
<path d="M28 108 L18 114 M36 112 L28 120" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 14. Школа Яна Непомнящего, Москва-Сити — ладьи-небоскрёбы на доске
I["nepo-chess-school"] = ("три стеклянные ладьи-небоскрёба Москва-Сити", "стоят на шахматной доске вместо башен, средняя самая высокая подмигивает", ("#E6EEFF", "#2C4DA6"), f'''
<path d="M0 104 L64 92 L128 104 V128 H0Z" fill="#fff" {W(2.4)}/>
<path d="M16 101 L32 98 L36 106 L18 110Z M48 95 L64 92 L66 99 L50 102Z M80 98 L96 101 L100 108 L84 105Z M30 116 L50 112 L52 122 L32 126Z M70 112 L88 115 L92 124 L72 121Z M110 104 L128 107 V114 L114 112Z" fill="#20305A"/>
<path d="M18 100 V60 H40 V100Z" fill="#7FB8F0" {W(3)}/><path d="M16 60 V52 H21 V56 H26 V52 H32 V56 H37 V52 H42 V60Z" fill="#7FB8F0" {W(2.6)}/>
<path d="M88 100 V54 H110 V100Z" fill="#9AD0F8" {W(3)}/><path d="M86 54 V46 H91 V50 H96 V46 H102 V50 H107 V46 H112 V54Z" fill="#9AD0F8" {W(2.6)}/>
<path d="M48 98 V34 H80 V98Z" fill="#5A9AE8" {W(3)}/><path d="M45 34 V24 H52 V29 H59 V24 H69 V29 H76 V24 H83 V34Z" fill="#5A9AE8" {W(2.6)}/>
<path d="M54 76 H74 M54 84 H74 M54 92 H74 M23 70 H35 M23 78 H35 M23 86 H35 M93 66 H105 M93 74 H105 M93 82 H105 M93 90 H105" stroke="#fff" stroke-width="2" opacity=".8"/>
{eye(58, 52, .45)}<path d="M66 52 Q70 49 74 52" fill="none" {W(2.4)}/><path d="M59 60 Q64 64 70 60" fill="none" {W(2.2)}/>{blush(55, 58, .5)}{blush(74, 58, .5)}
{sparkle(30, 30, 4)}{sparkle(104, 28, 3.4)}''')

# ---------- ДРУГИЕ СЕКЦИИ ----------

# 15. «Фигурист ВАО», СК «Вымпел» — девочка крутит вращение на льду
I["figurist-vao-vympel"] = ("девочка-фигуристка в бирюзовом платье", "крутится волчком на одной ноге на льду, подняв руки над головой", ("#FBEAFF", "#A75FCC"), f'''
<ellipse cx="64" cy="112" rx="58" ry="14" fill="#E8F8FF" {W(2.4)}/>
<ellipse cx="64" cy="110" rx="20" ry="5" fill="none" stroke="#9AC8E8" stroke-width="2"/><ellipse cx="64" cy="110" rx="32" ry="8" fill="none" stroke="#9AC8E8" stroke-width="1.6"/>
<path d="M58 22 L64 8 L70 22" fill="none" {W(5)}/><path d="M58 22 L64 8 L70 22" fill="none" stroke="#FFDCC0" stroke-width="2"/>
<path d="M58 22 L60 46 M70 22 L68 46" fill="none" {W(5)}/><path d="M58 22 L60 46 M70 22 L68 46" fill="none" stroke="#FFDCC0" stroke-width="2"/>
<circle cx="64" cy="44" r="10" fill="#FFDCC0" {W(2.8)}/><path d="M54 42 Q56 32 64 32 Q72 32 74 42 Q66 38 58 42Z" fill="#E8B030" {W(2)}/><circle cx="64" cy="32" r="4" fill="#E8B030" {W(2)}/>
<path d="M60 46 Q62 48 64 46 M66 46 Q68 48 70 46" fill="none" {W(1.6)}/><path d="M62 50 Q64 52 66 50" fill="none" {W(1.6)}/>
<path d="M58 54 H70 L80 80 Q64 86 48 80Z" fill="#2BC2C2" {W(3)}/>
<path d="M50 78 Q64 84 78 78" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M62 82 V100 M66 82 L72 90 L68 94" fill="none" {W(4.6)}/><path d="M62 82 V100 M66 82 L72 90 L68 94" fill="none" stroke="#FFDCC0" stroke-width="1.8"/>
<path d="M58 98 H68 L68 106 H58Z" fill="#fff" {W(2.4)}/><path d="M54 110 H72" {W(2.6)}/>
<path d="M30 60 Q24 72 32 84 M98 60 Q104 72 96 84 M38 40 Q30 48 32 58 M90 40 Q98 48 96 58" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/>
{sparkle(104, 26, 4.4)}{sparkle(24, 30, 3.4)}''')

# 16. Tennis Capital, Каширское — мальчик-болбой бежит за мячом у сетки
I["tennis-capital-kashirskaya"] = ("мальчик-болбой в синей кепке", "бежит пригнувшись вдоль теннисной сетки за жёлтым мячом на грунтовом корте", ("#FFEFE4", "#CF6236"), f'''
<path d="M0 96 H128 V128 H0Z" fill="#D9774A"/>
<path d="M0 110 H128" stroke="#fff" stroke-width="3"/>
<path d="M4 58 V96 M124 58 V96" stroke="{O}" stroke-width="5"/>
<path d="M4 62 H124 V92 H4Z" fill="none" stroke="#fff" stroke-width="1.2"/>
<path d="M4 70 H124 M4 78 H124 M4 86 H124 M16 62 V92 M28 62 V92 M40 62 V92 M52 62 V92 M64 62 V92 M76 62 V92 M88 62 V92 M100 62 V92 M112 62 V92" stroke="#fff" stroke-width="1.1" opacity=".75"/>
<rect x="2" y="58" width="124" height="5" fill="#fff" {W(2)}/>
<path d="M50 84 L40 100 L32 98 M60 84 L72 98 L80 96" fill="none" {W(5)}/><path d="M50 84 L40 100 L32 98 M60 84 L72 98 L80 96" fill="none" stroke="#F0C090" stroke-width="2"/>
<path d="M46 64 Q58 58 70 66 L64 86 Q54 88 46 84Z" fill="#fff" {W(3)}/>
<path d="M66 70 L86 80" fill="none" {W(5)}/><path d="M66 70 L86 80" fill="none" stroke="#F0C090" stroke-width="2"/>
<circle cx="70" cy="50" r="12" fill="#F0C090" {W(2.8)}/>
<path d="M58 46 Q60 36 72 36 Q82 38 82 46Z" fill="#2D5BD1" {W(2.4)}/><path d="M80 46 L92 48" {W(4)}/>
{eye(68, 52, .38)}{eye(76, 52, .38)}<path d="M70 57 Q73 59 76 57" fill="none" {W(1.8)}/>
<circle cx="100" cy="88" r="9" fill="#D8F23A" {W(2.6)}/><path d="M93 82 Q100 88 93 94 M107 82 Q100 88 107 94" fill="none" stroke="#fff" stroke-width="1.8"/>
<path d="M114 84 H122 M114 92 H124" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M22 70 H34 M18 80 H30" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 17. СШОР по бадминтону, школа № 1347 — волан прыгает в высоту через сетку
I["mgfso-badminton-school-1347"] = ("белый волан-прыгун в высоту", "перелетает спиной вперёд через высокую бадминтонную сетку, как прыгун на соревнованиях", ("#FFFBE2", "#D9B126"), f'''
<path d="M6 76 V128 M122 76 V128" stroke="{O}" stroke-width="5"/>
<path d="M6 80 H122 V100 H6Z" fill="none" stroke="#fff" stroke-width="1.2"/>
<path d="M6 86 H122 M6 93 H122 M14 80 V100 M24 80 V100 M34 80 V100 M44 80 V100 M54 80 V100 M64 80 V100 M74 80 V100 M84 80 V100 M94 80 V100 M104 80 V100 M114 80 V100" stroke="#fff" stroke-width="1.1" opacity=".8"/>
<rect x="4" y="76" width="120" height="5" fill="#fff" {W(2)}/>
<path d="M18 112 Q40 30 64 30 Q88 30 110 112" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="4 5"/>
<g transform="rotate(115 64 44)">
<path d="M64 50 L46 18 Q64 8 82 18Z" fill="#fff" {W(3)}/>
<path d="M56 47 L50 20 M64 50 V14 M72 47 L78 20" stroke="#C8C8D8" stroke-width="1.6"/>
<path d="M52 32 Q64 28 76 32" fill="none" stroke="#2D5BD1" stroke-width="2.6"/>
<ellipse cx="64" cy="56" rx="12" ry="11" fill="#F4E2C4" {W(3)}/>
<g transform="rotate(-115 64 56)">{eye(59, 55, .4)}{eye(69, 55, .4)}<path d="M61 61 Q64 63 67 61" fill="none" {W(1.8)}/></g>
</g>
{sparkle(104, 30, 4.4)}{sparkle(24, 40, 3.4)}''')

# 18. EXTREME KIDS Одинцово — мальчик на роликах перепрыгивает барьер
I["extremekids-roller-odintsovo"] = ("мальчик на мятных роликах в оранжевом шлеме", "перепрыгивает через низкий полосатый барьер-планку", ("#F1F5FF", "#7489B4"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#8A8FA8"/><path d="M10 118 H30 M50 118 H70 M90 118 H110" stroke="#fff" stroke-width="2.4"/>
<path d="M36 108 V90 M92 108 V90" {W(3.4)}/>
<rect x="30" y="86" width="68" height="8" rx="2" fill="#fff" {W(2.6)}/>
<path d="M38 86 H48 V94 H38Z M58 86 H68 V94 H58Z M78 86 H88 V94 H78Z" fill="#E8384A"/>
<g transform="translate(0 -10)"><path d="M56 56 L44 64 L48 74 M66 56 L80 62 L86 72" fill="none" {W(5)}/><path d="M56 56 L44 64 L48 74 M66 56 L80 62 L86 72" fill="none" stroke="#F4C9A0" stroke-width="2"/>
<path d="M40 70 H54 V80 H40Z M80 68 L94 70 L92 80 L78 78Z" fill="#6FE0B8" {W(2.6)}/>
<circle cx="43" cy="83" r="2.6" fill="#FFD23F" {W(1.6)}/><circle cx="51" cy="83" r="2.6" fill="#FFD23F" {W(1.6)}/><circle cx="81" cy="81" r="2.6" fill="#FFD23F" {W(1.6)}/><circle cx="89" cy="82" r="2.6" fill="#FFD23F" {W(1.6)}/>
<path d="M52 36 Q62 32 72 38 L68 58 Q60 60 54 56Z" fill="#3A6AD8" {W(3)}/>
<path d="M54 40 L38 32 M70 40 L88 30" fill="none" {W(5)}/><path d="M54 40 L38 32 M70 40 L88 30" fill="none" stroke="#F4C9A0" stroke-width="2"/>
<circle cx="64" cy="24" r="11" fill="#F4C9A0" {W(2.8)}/>
<path d="M51 22 Q52 8 64 8 Q78 8 77 22Z" fill="#FF8A1E" {W(2.6)}/><path d="M60 10 V18 M68 10 V18" stroke="#fff" stroke-width="2"/>
{eye(60, 26, .38)}{eye(68, 26, .38)}<path d="M61 31 Q64 33 67 31" fill="none" {W(1.8)}/>
</g><path d="M16 60 H30 M12 72 H26" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/>''')

# 19. Кинозал «Пегас», Егорьевск — зрители смотрят мультфильм с последнего ряда
I["egoryevsk-pegas-cinema"] = ("ряд детских макушек в тёмном кинозале", "из последнего ряда смотрят на большом экране мультфильм про крылатую лошадку", ("#5A2A4C", "#1C0C1C"), f'''
<path d="M30 20 L98 20 L128 70 L0 70Z" fill="#FFF6D8" opacity=".18"/>
<rect x="18" y="14" width="92" height="50" rx="3" fill="#BDE8FF" {W(3)}/>
<path d="M18 50 Q64 40 110 52 V64 H18Z" fill="#9AE07A"/>
<path d="M50 44 Q48 34 58 32 L74 32 Q80 30 82 24 Q88 26 86 34 Q86 44 76 44 Z" fill="#fff" {W(2.4)}/>
<path d="M54 44 V52 M76 44 V52" {W(2.6)}/>
<path d="M62 32 Q60 20 70 18 Q66 26 72 30" fill="#FFE6F2" {W(2)}/>
<circle cx="83" cy="29" r="1.4" fill="{O}"/>
<path d="M0 96 H128 V128 H0Z" fill="#B0283A" {W(2.4)}/><path d="M32 96 V128 M64 96 V128 M96 96 V128" stroke="#7A1A28" stroke-width="2.4"/>
<circle cx="30" cy="92" r="14" fill="#3A2A2A" {W(2.4)}/><circle cx="64" cy="88" r="16" fill="#E8A040" {W(2.4)}/><circle cx="98" cy="92" r="14" fill="#5A3A20" {W(2.4)}/>
<path d="M54 76 Q58 70 62 74 M66 74 Q70 70 74 76" fill="none" stroke="#E8A040" stroke-width="3" stroke-linecap="round"/>
<path d="M88 82 Q86 74 92 76 M104 82 Q108 74 102 76" fill="#5A3A20" {W(2)}/>
<rect x="104" y="98" width="14" height="16" fill="#fff" {W(2)}/><circle cx="108" cy="96" r="3" fill="#FFF2B0" {W(1.4)}/><circle cx="114" cy="96" r="3" fill="#FFF2B0" {W(1.4)}/>''')

# 20. Серпуховский театр — букет летит на сцену к поклону
I["serpukhov-theatre"] = ("букет красных роз в белой бумаге", "летит из зала на сцену к маленькой актрисе, которая кланяется между кулисами", ("#FFF3E2", "#A82A28"), f'''
<path d="M0 0 H128 V10 Q96 18 64 10 Q32 18 0 10Z" fill="#8A1A1E" {W(2.4)}/>
<path d="M0 8 Q20 40 14 96 H0Z M128 8 Q108 40 114 96 H128Z" fill="#C8303A" {W(2.6)}/>
<path d="M6 20 Q12 50 8 90 M122 20 Q116 50 120 90" fill="none" stroke="#8A1A1E" stroke-width="2"/>
<path d="M0 96 H128 V128 H0Z" fill="#8A5A34" {W(2.6)}/><path d="M0 104 H128" stroke="#6A4224" stroke-width="2"/>
<path d="M88 96 L92 78 L104 78 L108 96Z" fill="#FF8AB8" {W(2.6)}/>
<path d="M96 78 Q88 70 82 74" fill="none" {W(4)}/><path d="M100 78 Q108 72 112 76" fill="none" {W(4)}/>
<circle cx="86" cy="68" r="8" fill="#FFDCC0" {W(2.6)}/><path d="M80 64 Q86 56 94 64" fill="#6A3A1A" {W(2)}/>
<path d="M83 70 Q85 72 87 70" fill="none" {W(1.6)}/>
<g transform="rotate(-35 44 66)">
<path d="M34 72 L44 108 L54 72Z" fill="#fff" {W(2.8)}/>
<path d="M40 74 L44 64 M48 74 L44 64" {W(2)}/>
<circle cx="36" cy="64" r="8" fill="#E8304A" {W(2.4)}/><circle cx="52" cy="64" r="8" fill="#E8304A" {W(2.4)}/><circle cx="44" cy="54" r="8" fill="#F04A5A" {W(2.4)}/>
<path d="M33 63 Q36 60 39 64 M49 63 Q52 60 55 64 M41 53 Q44 50 47 54" fill="none" stroke="#9A1A2A" stroke-width="1.6"/>
<path d="M30 70 Q24 68 26 62 Q30 64 30 70Z M58 70 Q64 68 62 62 Q58 64 58 70Z" fill="#4AB84A" {W(1.6)}/>
</g>
<path d="M20 108 Q26 96 30 90" fill="none" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4"/>
{sparkle(66, 30, 4)}{sparkle(104, 40, 3.4)}''')

# ---------- БАССЕЙНЫ ----------

# 21. «Китёнок», пр-т Мира — мальчик плывёт кролем
I["kitenok-rizhskaya"] = ("мальчик-пловец в оранжевой шапочке", "плывёт кролем, повернув голову на вдох, одна рука взлетает над водой", ("#E6FAFF", "#2394D2"), f'''
<path d="M0 72 Q16 66 32 72 T64 72 T96 72 T128 72 V128 H0Z" fill="#3AB0E8" {W(2.6)}/>
<path d="M20 86 Q50 80 92 84 Q106 86 110 92 Q90 100 50 98 Q28 96 20 86Z" fill="#7FD0F4" opacity=".9"/>
<path d="M84 86 L104 90 L110 84" fill="none" {W(5)}/><path d="M84 86 L104 90 L110 84" fill="none" stroke="#F4C9A0" stroke-width="2"/>
<path d="M40 82 Q38 46 62 34" fill="none" {W(6)}/><path d="M40 82 Q38 46 62 34" fill="none" stroke="#F4C9A0" stroke-width="2.6"/>
<ellipse cx="64" cy="33" rx="5" ry="4" fill="#F4C9A0" {W(2.4)}/>
<circle cx="34" cy="76" r="14" fill="#F4C9A0" {W(3)}/>
<path d="M20 74 Q22 60 36 62 Q48 64 48 74 Q34 68 20 74Z" fill="#FF8A1E" {W(2.6)}/>
<rect x="24" y="74" width="20" height="7" rx="3.5" fill="#2A2F5A" {W(1.8)}/><circle cx="29" cy="77.5" r="2.4" fill="#8FE0FF"/><circle cx="39" cy="77.5" r="2.4" fill="#8FE0FF"/>
<path d="M31 85 Q34 88 38 85" fill="#fff" {W(1.8)}/>
<path d="M112 70 Q116 60 120 70 M100 62 Q104 54 108 62 M70 40 Q72 30 76 40" fill="#fff" {W(1.8)}/>
<circle cx="116" cy="54" r="2.6" fill="#fff"/><circle cx="82" cy="30" r="2.2" fill="#fff"/>
<path d="M10 100 Q24 96 38 100 M60 108 Q76 104 92 108" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 22. «Шторм», Братеево — девочка-ватерполистка бросает мяч в ворота
I["shtorm-brateevo"] = ("девочка-ватерполистка в шапочке с ушными чашками", "по пояс в воде бросает жёлтый мяч в плавающие ворота", ("#DDE8F5", "#2E4C78"), f'''
<path d="M80 40 H120 V82 H80Z" fill="none" stroke="#fff" stroke-width="1.4"/>
<path d="M80 50 H120 M80 60 H120 M80 70 H120 M90 40 V82 M100 40 V82 M110 40 V82" stroke="#fff" stroke-width="1.2" opacity=".8"/>
<path d="M80 82 V40 H120 V82" fill="none" stroke="#fff" stroke-width="5"/><path d="M80 82 V40 H120 V82" fill="none" {W(1.6)}/>
<path d="M0 78 Q16 72 32 78 T64 78 T96 78 T128 78 V128 H0Z" fill="#2A8ACB" {W(2.6)}/>
<path d="M14 92 Q30 88 46 92 M70 100 Q86 96 102 100" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
<path d="M28 84 Q30 66 42 64 Q54 62 58 80" fill="#E0505A" {W(3)}/>
<path d="M50 70 L58 44 L64 34" fill="none" {W(6)}/><path d="M50 70 L58 44 L64 34" fill="none" stroke="#F0C79C" stroke-width="2.6"/>
<path d="M30 72 L18 82" fill="none" {W(6)}/><path d="M30 72 L18 82" fill="none" stroke="#F0C79C" stroke-width="2.6"/>
<circle cx="42" cy="52" r="13" fill="#F0C79C" {W(3)}/>
<path d="M29 50 Q30 36 43 37 Q56 38 55 50 Q42 44 29 50Z" fill="#fff" {W(2.4)}/>
<circle cx="30" cy="54" r="4" fill="#fff" {W(2)}/><circle cx="54" cy="54" r="4" fill="#fff" {W(2)}/>
<text x="42" y="46" font-family="Arial" font-weight="bold" font-size="8" fill="#2E4C78" text-anchor="middle">7</text>
{eye(38, 55, .38)}{eye(46, 55, .38)}<path d="M39 60 Q42 62 45 60" fill="none" {W(1.8)}/>
<circle cx="72" cy="26" r="11" fill="#FFD83A" {W(2.8)}/><path d="M62 22 Q72 28 82 22 M64 32 Q72 26 80 32" fill="none" stroke="#2E4C78" stroke-width="1.8"/>
<path d="M66 42 Q76 30 88 30" fill="none" stroke="#fff" stroke-width="2.2" stroke-dasharray="3 4"/>''')

# 23. «Китёнок», Гурьянова — малыш лежит на воде звёздочкой (вид сверху)
I["kitenok-pechatniki"] = ("малыш в зелёной шапочке", "лежит на спине звёздочкой на голубой воде бассейна, вид сверху", ("#DCFCF6", "#1FAFA6"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#5CD4E8"/>
<path d="M0 20 H128 M0 108 H128" stroke="#fff" stroke-width="4" stroke-dasharray="8 6"/>
<path d="M0 20 H128 M0 108 H128" stroke="#E8384A" stroke-width="4" stroke-dasharray="8 6" stroke-dashoffset="7"/>
<path d="M14 44 Q22 40 30 44 M96 86 Q104 82 112 86 M100 40 Q108 36 116 40 M12 84 Q20 80 28 84" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<path d="M54 60 L30 44 M74 60 L98 44 M58 78 L44 102 M70 78 L84 102" fill="none" {W(7)}/>
<path d="M54 60 L30 44 M74 60 L98 44 M58 78 L44 102 M70 78 L84 102" fill="none" stroke="#FFD9B8" stroke-width="3.4"/>
<path d="M50 56 Q64 50 78 56 L76 82 Q64 86 52 82Z" fill="#FF5AA0" {W(3)}/>
<path d="M54 64 H74 M54 72 H74" stroke="#fff" stroke-width="2.4"/>
<circle cx="64" cy="42" r="14" fill="#FFD9B8" {W(3)}/>
<path d="M50 40 Q50 26 64 26 Q78 26 78 40 Q64 34 50 40Z" fill="#46C84A" {W(2.6)}/>
<path d="M57 44 Q59 42 61 44 M67 44 Q69 42 71 44" fill="none" {W(2)}/><path d="M60 49 Q64 52 68 49" fill="none" {W(2)}/>{blush(54, 48, .5)}{blush(74, 48, .5)}''')

# 24. «Китёнок», Дмитровское ш. — девочка плывёт брассом прямо на нас
I["kitenok-likhobory"] = ("девочка в полосатом купальнике и фиолетовой шапочке", "плывёт брассом прямо на нас, голова над водой, позади расходятся волны-усы", ("#EEF5FF", "#5671DA"), f'''
<path d="M0 58 Q32 54 64 58 T128 58 V128 H0Z" fill="#4FC2EE" {W(2.6)}/>
<path d="M64 74 L10 112 M64 74 L118 112" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M64 78 L24 116 M64 78 L104 116" stroke="#C8F0FF" stroke-width="2" stroke-linecap="round"/>
<path d="M40 70 Q30 64 22 70 M88 70 Q98 64 106 70" fill="none" {W(6)}/><path d="M40 70 Q30 64 22 70 M88 70 Q98 64 106 70" fill="none" stroke="#FFD9B8" stroke-width="2.6"/>
<ellipse cx="20" cy="71" rx="5" ry="3.4" fill="#FFD9B8" {W(2.2)}/><ellipse cx="108" cy="71" rx="5" ry="3.4" fill="#FFD9B8" {W(2.2)}/>
<path d="M44 72 Q64 64 84 72 Q64 80 44 72Z" fill="#FFE04A" {W(2.4)}/><path d="M50 70 Q64 66 78 70" stroke="#E8384A" stroke-width="2.2" fill="none"/>
<circle cx="64" cy="54" r="17" fill="#FFD9B8" {W(3)}/>
<path d="M47 52 Q47 34 64 34 Q81 34 81 52 Q64 44 47 52Z" fill="#9A5ADF" {W(2.6)}/>
{eye(58, 56, .45)}{eye(70, 56, .45)}<ellipse cx="64" cy="64" rx="3" ry="2.4" fill="{O}"/>{blush(52, 62, .5)}{blush(76, 62, .5)}
<circle cx="44" cy="40" r="2.4" fill="#fff"/><circle cx="86" cy="36" r="3" fill="#fff"/>''')

# 25. «Детская бухта», Реутов — ладони тренера держат малыша на воде
I["detskaya-bukhta-reutov"] = ("большие ладони тренера по плаванию", "бережно держат малыша на воде — первое индивидуальное занятие", ("#F3FFEE", "#56B892"), f'''
<path d="M0 66 Q32 60 64 66 T128 66 V128 H0Z" fill="#66CBEA" {W(2.6)}/>
<path d="M12 84 Q28 80 44 84 M84 92 Q100 88 116 92" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
<path d="M14 98 Q20 80 46 80 L54 84 L52 90 L40 90 Q30 94 26 108Z" fill="#E8B48A" {W(3)}/>
<path d="M114 98 Q108 80 82 80 L74 84 L76 90 L88 90 Q98 94 102 108Z" fill="#E8B48A" {W(3)}/>
<path d="M36 70 Q64 58 94 70 Q96 80 64 82 Q32 80 36 70Z" fill="#FFD84A" {W(3)}/>
<path d="M90 68 L104 60 M90 74 L106 74" fill="none" {W(5)}/><path d="M90 68 L104 60 M90 74 L106 74" fill="none" stroke="#FFE2C8" stroke-width="2"/>
<path d="M40 66 L30 56 M44 72 L28 70" fill="none" {W(5)}/><path d="M40 66 L30 56 M44 72 L28 70" fill="none" stroke="#FFE2C8" stroke-width="2"/>
<circle cx="64" cy="58" r="15" fill="#FFE2C8" {W(3)}/>
<path d="M56 46 Q60 40 66 44" fill="none" {W(2.2)}/>
<path d="M56 58 Q58 56 60 58 M68 58 Q70 56 72 58" fill="none" {W(2)}/><ellipse cx="64" cy="65" rx="3" ry="2.6" fill="{O}"/>{blush(54, 63, .5)}{blush(74, 63, .5)}
<path d="M58 30 Q64 22 70 30 Q64 38 58 30Z" fill="#FF7FA8" {W(1.8)}/>''')

# 26. «Китёнок», 3-я Владимирская — дорожка из поплавков
I["kitenok-perovo"] = ("разделительная дорожка из красно-белых поплавков", "улыбчивой гусеницей тянется через бассейн, за неё держится малыш", ("#FFF0F0", "#E36A6A"), f'''
<path d="M0 0 H128 V128 H0Z" fill="#66D2F0"/>
<path d="M0 22 H128 M0 106 H128" stroke="#2A7CB8" stroke-width="4"/>
<path d="M10 40 Q18 36 26 40 M96 30 Q104 26 112 30 M14 90 Q22 86 30 90 M100 92 Q108 88 116 92" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<circle cx="10" cy="66" r="8" fill="#fff" {W(2.4)}/><circle cx="26" cy="64" r="8" fill="#E8384A" {W(2.4)}/><circle cx="42" cy="66" r="8" fill="#fff" {W(2.4)}/>
<circle cx="58" cy="64" r="8" fill="#E8384A" {W(2.4)}/><circle cx="74" cy="66" r="8" fill="#fff" {W(2.4)}/><circle cx="90" cy="64" r="8" fill="#E8384A" {W(2.4)}/>
<circle cx="110" cy="62" r="13" fill="#fff" {W(2.8)}/>{eye(106, 61, .4)}{eye(115, 61, .4)}<path d="M107 67 Q110 70 114 67" fill="none" {W(1.8)}/>
<circle cx="50" cy="84" r="11" fill="#FFD9B8" {W(2.8)}/><path d="M39 82 Q40 70 51 71 Q62 72 61 82 Q50 78 39 82Z" fill="#FFD23F" {W(2.4)}/>
<path d="M47 86 Q49 84 51 86 M53 86 Q55 84 57 86" fill="none" {W(1.6)}/>
<path d="M58 78 L58 70 M44 76 L42 70" fill="none" {W(4.6)}/><path d="M58 78 L58 70 M44 76 L42 70" fill="none" stroke="#FFD9B8" stroke-width="1.8"/>''')

# 27. Aqua Baby Club, Химки — младенец ныряет под водой
I["aquababy-khimki-molodezhnaya"] = ("младенец-ныряльщик с надутыми щёчками", "ныряет под водой с открытыми глазами, а вверх бегут пузыри", ("#BDEBFF", "#1470B4"), f'''
<path d="M0 0 H128 V18 Q96 24 64 18 Q32 12 0 18Z" fill="#E6FAFF" opacity=".8"/>
<path d="M20 30 L40 120 M60 26 L70 120 M100 30 L90 120" stroke="#fff" stroke-width="6" opacity=".12"/>
<circle cx="70" cy="40" r="4" fill="none" stroke="#fff" stroke-width="2"/><circle cx="78" cy="28" r="3" fill="none" stroke="#fff" stroke-width="2"/><circle cx="66" cy="22" r="2.4" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M78 70 L106 58 M78 84 L104 92" fill="none" {W(7)}/><path d="M78 70 L106 58 M78 84 L104 92" fill="none" stroke="#FFDCC4" stroke-width="3.4"/>
<path d="M38 68 L18 56 M40 80 L20 92" fill="none" {W(7)}/><path d="M38 68 L18 56 M40 80 L20 92" fill="none" stroke="#FFDCC4" stroke-width="3.4"/>
<ellipse cx="62" cy="76" rx="22" ry="16" fill="#FFDCC4" {W(3)}/>
<path d="M48 82 Q62 90 78 82 L78 90 Q62 96 46 90Z" fill="#FF8AB8" {W(2.4)}/>
<circle cx="62" cy="54" r="17" fill="#FFDCC4" {W(3)}/>
<path d="M54 38 Q60 30 64 38 Q68 32 70 40" fill="none" stroke="#C88A3A" stroke-width="2.4" stroke-linecap="round"/>
{eye(55, 52, .5)}{eye(69, 52, .5)}<circle cx="49" cy="61" r="5" fill="#FF9AB8" opacity=".75"/><circle cx="75" cy="61" r="5" fill="#FF9AB8" opacity=".75"/>
<ellipse cx="62" cy="63" rx="2.6" ry="2" fill="{O}"/>''')

# 28. The Bassein, Сокольники — малыш в полотенце-пончо выходит из бассейна
I["pool-the-bassein"] = ("малыш в жёлтом полотенце-пончо с капюшоном", "выходит из бассейна и оставляет на плитке мокрые следы", ("#FFF8EA", "#E8A03A"), f'''
<path d="M0 0 H128 V60 H0Z" fill="#53C6E6"/>
<path d="M12 22 Q22 18 32 22 M80 16 Q90 12 100 16 M46 40 Q56 36 66 40" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
<path d="M0 60 H128 V128 H0Z" fill="#F4EEE4"/>
<path d="M0 60 H128" {W(3)}/><path d="M0 88 H128 M0 112 H128 M24 60 V128 M56 60 V128 M88 60 V128 M120 60 V128" stroke="#DCD2C4" stroke-width="1.6"/>
<path d="M44 96 Q36 70 52 50 Q64 34 76 50 Q92 70 84 96 Z" fill="#FFD23F" {W(3)}/>
<path d="M48 54 Q64 44 80 54 Q78 76 64 78 Q50 76 48 54Z" fill="#FFE07A" {W(2.4)}/>
<path d="M48 90 H80" stroke="#FF8A3A" stroke-width="3"/>
<circle cx="64" cy="60" r="11" fill="#FFD9B8" {W(2.6)}/>
{eye(60, 60, .38)}{eye(68, 60, .38)}<path d="M61 65 Q64 67 67 65" fill="none" {W(1.8)}/>{blush(56, 64, .45)}{blush(72, 64, .45)}
<path d="M56 96 V104 H62 M70 96 V104 H76" fill="none" {W(4.6)}/><path d="M56 96 V104 M70 96 V104" stroke="#FFD9B8" stroke-width="1.8"/>
<ellipse cx="38" cy="112" rx="4" ry="6" fill="#9AD8F0"/><ellipse cx="30" cy="96" rx="4" ry="6" fill="#9AD8F0"/><ellipse cx="44" cy="80" rx="3.4" ry="5" fill="#9AD8F0" opacity=".7"/>
<path d="M88 74 Q90 70 92 74 Q90 78 88 74Z M96 84 Q98 80 100 84 Q98 88 96 84Z" fill="#7FCBEA"/>''')

# ---------- КАФЕ ----------

# 29. Kitchen, Ходынка — клубничный молочный коктейль пускает пузыри-сердечки
I["cafe-kitchen-grizodubovoy"] = ("клубничный молочный коктейль с горкой сливок", "пускает через полосатую трубочку пузыри-сердечки", ("#FFF0F6", "#E2639A"), f'''
<path d="M40 50 L46 116 H82 L88 50Z" fill="#FFB3CC" {W(3)}/>
<path d="M42 66 Q64 72 86 66" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M36 52 Q34 38 48 38 Q50 26 64 28 Q78 26 80 38 Q94 38 92 52Z" fill="#FFFBF2" {W(3)}/>
<circle cx="64" cy="26" r="6" fill="#E8304A" {W(2.4)}/><path d="M64 20 Q66 14 70 12" fill="none" {W(2)}/>
<path d="M76 40 L96 10" stroke="{O}" stroke-width="8" stroke-linecap="round"/><path d="M76 40 L96 10" stroke="#fff" stroke-width="4.6" stroke-linecap="round"/>
<path d="M80 34 L84 28 M88 22 L92 16" stroke="#E8384A" stroke-width="4.6"/>
{eye(56, 86, .5)}{eye(72, 86, .5)}{smile(64, 94, 4, .7)}{blush(50, 94, .6)}{blush(78, 94, .6)}
<path d="M104 30 Q100 24 104 22 Q108 20 108 26 Q110 20 114 22 Q116 26 108 34Z" fill="#fff" {W(1.8)}/>
<path d="M18 40 Q14 34 18 32 Q22 30 22 36 Q24 30 28 32 Q30 36 22 44Z" fill="#fff" {W(1.8)}/>
<path d="M104 56 Q101 52 104 50 Q107 49 107 53 Q109 49 112 50 Q113 53 107 59Z" fill="#fff" {W(1.6)}/>''')

# 30. Чайхана «Дюшес», Красногорск — бутылка грушевого лимонада
I["cafe-dyushes-krasnogorsk"] = ("стеклянная бутылка грушевого лимонада «Дюшес»", "открылась с хлопком, и из горлышка вылетают пузыри-грушки", ("#F7FFE4", "#A3C83A"), f'''
<path d="M54 34 V48 Q40 58 40 74 V114 Q40 120 46 120 H82 Q88 120 88 114 V74 Q88 58 74 48 V34Z" fill="#B8F07A" opacity=".95" {W(3)}/>
<path d="M44 76 H84 V102 H44Z" fill="#FFF6D0" {W(2.4)}/>
<path d="M64 80 Q70 82 70 90 Q72 98 64 98 Q56 98 58 90 Q58 82 64 80Z" fill="#F2D23A" {W(2)}/><path d="M64 80 Q66 76 68 76" fill="none" {W(1.8)}/>
<rect x="52" y="28" width="24" height="8" rx="2" fill="#E8C02A" {W(2.4)}/>
{eye(56, 62, .45)}{eye(72, 62, .45)}<path d="M60 68 Q64 72 68 68" fill="none" {W(2)}/>
<path d="M50 52 Q46 60 46 70" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M42 18 Q46 14 48 18 Q52 22 46 26 Q40 24 42 18Z M78 10 Q82 6 84 10 Q88 14 82 18 Q76 16 78 10Z M98 26 Q102 22 104 26 Q108 30 102 34 Q96 32 98 26Z" fill="#F2E25A" {W(2)}/>
<circle cx="62" cy="16" r="3" fill="#fff" {W(1.6)}/><circle cx="26" cy="34" r="2.6" fill="#fff" {W(1.4)}/><circle cx="96" cy="46" r="2.4" fill="#fff" {W(1.4)}/>
<path d="M30 20 L36 26 M98 14 L92 20" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 31. Kitchen, Академика Анохина — суп с буквами складывает «МАМА»
I["cafe-kitchen-anokhina"] = ("тарелка куриного супа с лапшой-буквами", "буквы-макаронины сами складываются в слово «МАМА»", ("#EFF6FF", "#5C8FD8"), f'''
<ellipse cx="64" cy="80" rx="54" ry="30" fill="#fff" {W(3)}/>
<ellipse cx="64" cy="76" rx="42" ry="20" fill="#FFD66A" {W(2.4)}/>
<text x="64" y="82" font-family="Arial" font-weight="bold" font-size="17" fill="#FFF6D8" stroke="{O}" stroke-width="1.4" text-anchor="middle" letter-spacing="1">МАМА</text>
<circle cx="34" cy="72" r="3" fill="#F28A2A" {W(1.4)}/><circle cx="94" cy="70" r="3" fill="#F28A2A" {W(1.4)}/><circle cx="88" cy="86" r="2.4" fill="#4AB84A"/>
<path d="M44 46 Q40 38 44 32 M64 44 Q60 34 64 26 M84 46 Q80 38 84 32" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{eye(52, 100, .45)}{eye(76, 100, .45)}<path d="M60 104 Q64 107 68 104" fill="none" {W(2)}/>{blush(44, 104, .5)}{blush(84, 104, .5)}
<path d="M110 38 L100 82" stroke="{O}" stroke-width="8" stroke-linecap="round"/><path d="M110 38 L100 82" stroke="#C8D0DC" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="111" cy="34" rx="7" ry="9" fill="#C8D0DC" {W(2.6)}/>''')

# 32. Сыроварня, Аутлет Внуково — фондю тянет сырную нитку
I["cafe-syrovarnya-vnukovo-outlet"] = ("медная кастрюлька сырного фондю на огоньке", "кусочек хлеба на длинной вилке тянет из неё сырную нитку, как канат", ("#FFF7E6", "#C98A3A"), f'''
<path d="M50 112 Q56 102 64 112 Q72 102 78 112" fill="#FF8A2A" {W(2.2)}/>
<path d="M40 112 H88" {W(3)}/><path d="M44 112 L40 122 M84 112 L88 122" {W(3)}/>
<path d="M28 70 H100 Q100 106 64 106 Q28 106 28 70Z" fill="#D07A3A" {W(3)}/>
<path d="M100 76 H118" {W(5)}/>
<ellipse cx="64" cy="70" rx="36" ry="8" fill="#FFD84A" {W(2.6)}/>
<path d="M58 70 Q62 50 76 36" fill="none" stroke="#FFD84A" stroke-width="5" stroke-linecap="round"/><path d="M58 70 Q62 50 76 36" fill="none" stroke="#E8B02A" stroke-width="1.6"/>
<path d="M80 36 L112 8" {W(3)}/><path d="M80 36 L74 34 M80 36 L82 30" {W(2.2)}/>
<rect x="68" y="26" width="16" height="14" rx="3" fill="#E8B880" {W(2.6)} transform="rotate(-40 76 33)"/>
{eye(52, 88, .5)}{eye(76, 88, .5)}{smile(64, 95, 4, .7)}{blush(44, 94, .6)}{blush(84, 94, .6)}''')

# 33. Гамбринус, Перово — три колбаски поют хором на доске
I["cafe-gambrinus-perovo"] = ("три баварские колбаски-гриль", "поют хором на деревянной доске рядом с бочонком горчицы", ("#EAF2FF", "#3C66B8"), f'''
<rect x="12" y="84" width="104" height="22" rx="8" fill="#C8884A" {W(3)}/><path d="M18 94 H110" stroke="#A86A32" stroke-width="2"/>
<rect x="88" y="62" width="22" height="24" rx="5" fill="#FFD23F" {W(2.6)}/><ellipse cx="99" cy="62" rx="11" ry="4" fill="#E8B02A" {W(2.2)}/>
<path d="M90 70 H108 M90 78 H108" stroke="#A86A32" stroke-width="1.6"/>
<rect x="18" y="40" width="16" height="46" rx="8" fill="#F0A06A" {W(3)}/>
<rect x="40" y="34" width="16" height="52" rx="8" fill="#E8905A" {W(3)}/>
<rect x="62" y="42" width="16" height="44" rx="8" fill="#F2AA74" {W(3)}/>
<path d="M20 60 L32 56 M20 70 L32 66 M42 56 L54 52 M42 66 L54 62 M64 62 L76 58 M64 72 L76 68" stroke="#A8502A" stroke-width="2"/>
<path d="M23 48 Q26 46 28 48 M28 48 Q30 46 32 48" fill="none" {W(1.6)}/><ellipse cx="26" cy="53" rx="2.4" ry="3" fill="{O}"/>
<path d="M44 42 Q46 40 48 42 M50 42 Q52 40 54 42" fill="none" {W(1.6)}/><ellipse cx="48" cy="47" rx="2.6" ry="3.4" fill="{O}"/>
<path d="M66 50 Q68 48 70 50 M72 50 Q74 48 76 50" fill="none" {W(1.6)}/><ellipse cx="70" cy="55" rx="2.4" ry="3" fill="{O}"/>
<path d="M24 24 V34 Q20 36 22 32 M60 16 V28 Q56 30 58 26 M86 26 V36 Q82 38 84 34" fill="none" {W(2.4)}/>
<circle cx="21" cy="34" r="3" fill="{O}"/><circle cx="57" cy="28" r="3" fill="{O}"/><circle cx="83" cy="36" r="3" fill="{O}"/>''')

# 34. Casa la Famiglia, Новогиреево — семья ложек у тарелки минестроне
I["cafe-casa-la-famiglia"] = ("тарелка итальянского супа минестроне", "к ней тянутся три ложки — большая, средняя и маленькая, как вся семья", ("#FFF5EC", "#D86A4A"), f'''
<ellipse cx="64" cy="92" rx="50" ry="24" fill="#fff" {W(3)}/>
<ellipse cx="64" cy="88" rx="38" ry="15" fill="#F07A4A" {W(2.4)}/>
<circle cx="46" cy="86" r="3.4" fill="#FFD23F" {W(1.4)}/><circle cx="74" cy="82" r="3" fill="#4AB84A" {W(1.4)}/><rect x="56" y="90" width="7" height="5" fill="#FFE8A0" {W(1.4)}/><circle cx="84" cy="92" r="3" fill="#FFD23F" {W(1.4)}/>
<path d="M58 80 Q64 76 70 80 Q64 84 58 80Z" fill="#4AB84A" {W(1.4)}/>
{eye(54, 104, .42)}{eye(74, 104, .42)}<path d="M61 108 Q64 110 67 108" fill="none" {W(1.8)}/>
<path d="M20 20 L44 76" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M20 20 L44 76" stroke="#E2E8F0" stroke-width="3.4" stroke-linecap="round"/><ellipse cx="46" cy="80" rx="7" ry="9" fill="#E2E8F0" {W(2.4)} transform="rotate(-24 46 80)"/>
<path d="M64 16 V72" stroke="{O}" stroke-width="6" stroke-linecap="round"/><path d="M64 16 V72" stroke="#E2E8F0" stroke-width="2.8" stroke-linecap="round"/><ellipse cx="64" cy="74" rx="6" ry="7.4" fill="#E2E8F0" {W(2.2)}/>
<path d="M104 40 L88 76" stroke="{O}" stroke-width="5" stroke-linecap="round"/><path d="M104 40 L88 76" stroke="#E2E8F0" stroke-width="2.2" stroke-linecap="round"/><ellipse cx="86" cy="79" rx="4.4" ry="5.6" fill="#E2E8F0" {W(2)} transform="rotate(24 86 79)"/>
<path d="M24 16 Q20 10 24 8 Q28 6 28 12 Q30 6 34 8 Q36 12 28 20Z" fill="#E8384A" opacity=".85"/>''')

# 35. IL Патио, МЕГА Химки — палочки гриссини рисуют соусом сердечко
I["cafe-ilpatio-mega-khimki"] = ("хрустящие палочки гриссини в высоком стакане", "одна палочка вылезла и рисует томатным соусом сердечко на тарелке", ("#F2FFF6", "#3BA772"), f'''
<ellipse cx="78" cy="104" rx="40" ry="14" fill="#fff" {W(3)}/>
<path d="M66 102 Q60 94 66 92 Q72 90 74 98 Q78 90 84 92 Q90 96 76 108Z" fill="none" stroke="#E8384A" stroke-width="4" stroke-linecap="round"/>
<path d="M22 50 L28 112 H56 L62 50Z" fill="#E6F6FF" opacity=".9" {W(3)}/>
<path d="M30 52 L26 14 M38 52 L38 8 M46 52 L48 12" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M30 52 L26 14 M38 52 L38 8 M46 52 L48 12" stroke="#E8C080" stroke-width="4.4" stroke-linecap="round"/>
<path d="M27 20 L29 18 M38 16 L40 14 M48 20 L50 18 M38 28 L40 26" stroke="#fff" stroke-width="1.6"/>
<path d="M58 40 L74 98" stroke="{O}" stroke-width="9" stroke-linecap="round"/><path d="M58 40 L74 98" stroke="#E8C080" stroke-width="5.4" stroke-linecap="round"/>
<path d="M73 94 L75 100" stroke="#E8384A" stroke-width="5" stroke-linecap="round"/>
{eye(60, 52, .38)}{eye(66, 50, .38)}<path d="M62 58 Q65 60 68 57" fill="none" {W(1.6)}/>
{eye(36, 78, .45)}{eye(48, 78, .45)}<path d="M39 85 Q42 88 46 85" fill="none" {W(1.8)}/>''')

# 36. Казбек, ул. 1905 года — кувшин тархуна у снежной вершины
I["cafe-kazbek-1905"] = ("глиняный кувшин зелёного лимонада тархун", "стоит рядом с полным изумрудным стаканом у подножия снежной вершины Казбека", ("#E8F4FF", "#6A8CC8"), f'''
<path d="M-4 84 L40 26 L58 44 L74 20 L132 84Z" fill="#8A9AB8" {W(2.6)}/>
<path d="M30 40 L40 26 L48 36 L42 34 L36 42Z M66 30 L74 20 L84 32 L78 30 L72 36Z" fill="#fff" {W(2)}/>
<path d="M0 84 H128 V128 H0Z" fill="#E8D2B0" {W(2.4)}/>
<path d="M24 56 Q24 46 34 44 L34 38 H50 V44 Q64 48 62 62 Q66 84 52 108 H32 Q18 84 24 56Z" fill="#C86A3A" {W(3)}/>
<path d="M60 56 Q72 56 70 72 Q68 80 58 84" fill="none" {W(3.4)}/>
<path d="M26 72 Q42 78 60 72" fill="none" stroke="#FFE0B0" stroke-width="2.4"/>
<path d="M34 40 Q30 36 26 40 Q22 44 26 46" fill="#C86A3A" {W(2.4)}/>
{eye(36, 88, .45)}{eye(48, 88, .45)}<path d="M39 94 Q42 96 45 94" fill="none" {W(1.8)}/>
<path d="M80 72 L84 112 H104 L108 72Z" fill="#E8FAFF" opacity=".9" {W(2.8)}/>
<path d="M82 84 L85 110 H103 L106 84Z" fill="#3AD07A"/>
<path d="M90 78 Q88 90 92 98" fill="none" stroke="#fff" stroke-width="2" opacity=".8"/>
<path d="M98 76 Q102 70 104 74" fill="#4AB84A" {W(1.6)}/>''')

# 37. IL Патио, ТЦ «Весна» — апельсиновый сорбет на весенней клумбе
I["cafe-ilpatio-vesna"] = ("апельсиновый сорбет в половинке апельсиновой корки", "сидит на весенней клумбе среди распустившихся тюльпанов", ("#F4FFE8", "#7CC24A"), f'''
<path d="M0 100 Q64 88 128 100 V128 H0Z" fill="#6A4A2A" {W(2.4)}/>
<path d="M18 100 V74 M110 100 V70 M100 102 V82" stroke="#3E9A3A" stroke-width="3.4"/>
<path d="M18 84 Q10 78 12 70 Q18 74 18 84Z M110 82 Q118 76 116 68 Q110 72 110 82Z" fill="#4AB84A" {W(1.6)}/>
<path d="M10 66 L12 56 L16 62 L18 54 L22 62 L26 56 L26 66 Q18 74 10 66Z" fill="#FF5A8A" {W(2.2)}/>
<path d="M102 62 L104 52 L108 58 L110 50 L114 58 L118 52 L118 62 Q110 70 102 62Z" fill="#FFD23F" {W(2.2)}/>
<path d="M92 80 L94 72 L98 76 L100 70 L102 76 L106 72 L106 80 Q99 86 92 80Z" fill="#B57AF0" {W(2)}/>
<path d="M30 70 Q30 110 64 110 Q98 110 98 70Z" fill="#FF9A2A" {W(3)}/>
<path d="M34 70 Q34 104 64 104 Q94 104 94 70" fill="none" stroke="#FFE0A0" stroke-width="3"/>
<path d="M32 70 Q30 52 46 50 Q48 34 64 34 Q80 34 82 50 Q98 52 96 70Z" fill="#FFC27A" {W(3)}/>
<path d="M48 54 Q52 48 58 50 M70 48 Q76 46 80 52" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M64 34 Q60 22 70 18 Q72 28 64 34Z" fill="#4AB84A" {W(2)}/>
{eye(56, 86, .5)}{eye(72, 86, .5)}{smile(64, 93, 4, .7)}{blush(48, 92, .6)}{blush(80, 92, .6)}
{sparkle(104, 28, 4)}<circle cx="26" cy="30" r="9" fill="#FFF3A0" opacity=".9"/>''')

# 38. Kitchen, Марфино — клаб-сэндвич ставит флажок на горе картошки фри
I["cafe-kitchen-marfino"] = ("клаб-сэндвич треугольником на шпажке", "забрался на вершину горы из картошки фри и водрузил флажок, как альпинист", ("#EAF0FF", "#6A6FD0"), f'''
<path d="M4 120 L30 74 L42 84 L56 58 L72 80 L88 64 L124 120Z" fill="#FFD23F" {W(3)}/>
<path d="M30 74 L26 100 M42 84 L46 110 M56 58 L54 96 M72 80 L76 112 M88 64 L96 108 M14 104 L20 92 M110 110 L104 96" stroke="#E8A82A" stroke-width="2.6"/>
<path d="M2 122 Q64 112 126 122 V128 H2Z" fill="#E8384A" {W(2.4)}/>
<path d="M40 54 L64 20 L88 54Z" fill="#F7D9A8" {W(3)}/>
<path d="M44 48 L84 48" stroke="#4AB84A" stroke-width="4"/><path d="M47 43 L81 43" stroke="#E8384A" stroke-width="3.4"/><path d="M51 37 L77 37" stroke="#FFD23F" stroke-width="3"/>
<path d="M40 54 L64 20 L88 54Z" fill="none" {W(3)}/>
<path d="M64 20 V4" {W(2.6)}/><path d="M64 4 L80 8 L64 13Z" fill="#2D5BD1" {W(2)}/>
{eye(58, 30, .38)}{eye(70, 30, .38)}<path d="M61 34 Q64 36 67 34" fill="none" {W(1.6)}/>
<path d="M50 54 L44 64 M78 54 L84 62" fill="none" {W(4)}/>
{sparkle(104, 34, 4)}{sparkle(22, 40, 3.2)}''')

# 39. Рыжий Лис, Солнцево — тыквенный суп в тыкве, пар закручивается лисьим хвостом
I["cafe-ryzhiy-lis"] = ("густой тыквенный суп-пюре в горшочке-тыкве", "над ним рыжий пар закручивается пушистым лисьим хвостом", ("#FFF6EA", "#9A5A2E"), f'''
<path d="M60 64 Q30 52 38 30 Q46 10 72 14 Q94 18 92 36 Q84 26 72 28 Q58 32 62 44 Q66 54 78 60Z" fill="#FF8A3A" {W(3)}/>
<path d="M92 36 Q84 26 72 28 Q76 20 84 20 Q92 24 92 36Z" fill="#fff" {W(2.4)}/>
<path d="M44 36 Q46 26 56 22 M50 48 Q48 40 52 34" fill="none" stroke="#FFC08A" stroke-width="2.4" stroke-linecap="round"/>
<path d="M18 74 Q16 116 64 118 Q112 116 110 74Z" fill="#F28A2A" {W(3)}/>
<path d="M40 76 Q36 98 44 114 M64 76 V118 M88 76 Q92 98 84 114" fill="none" stroke="#C8621A" stroke-width="2.4"/>
<ellipse cx="64" cy="72" rx="46" ry="12" fill="#FFB14A" {W(3)}/>
<path d="M48 72 Q64 66 80 72" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="56" cy="70" r="1.8" fill="#4A3A2A"/><circle cx="74" cy="74" r="1.8" fill="#4A3A2A"/><circle cx="66" cy="68" r="1.6" fill="#4A3A2A"/>
{eye(50, 94, .5)}{eye(78, 94, .5)}{smile(64, 101, 4, .7)}{blush(42, 100, .6)}{blush(86, 100, .6)}''')

# 40. «Красный Октябрь» — какао-боб едет по конвейеру шоколадной фабрики
I["tour-krasny-oktyabr"] = ("какао-боб в маленькой поварской косынке", "едет по ленте конвейера шоколадной фабрики мимо готовых конфет", ("#FFEFE6", "#B23A3A"), f'''
<path d="M70 14 H96 V40 L86 54 H80 L70 40Z" fill="#D8DEE8" {W(2.6)}/><path d="M83 54 Q82 62 84 66" fill="none" stroke="#6A3A1E" stroke-width="5" stroke-linecap="round"/>
<rect x="8" y="88" width="112" height="14" rx="7" fill="#5A5A6A" {W(3)}/>
<circle cx="18" cy="95" r="4" fill="#C8C8D8" {W(1.8)}/><circle cx="46" cy="95" r="4" fill="#C8C8D8" {W(1.8)}/><circle cx="82" cy="95" r="4" fill="#C8C8D8" {W(1.8)}/><circle cx="110" cy="95" r="4" fill="#C8C8D8" {W(1.8)}/>
<path d="M30 102 V122 M98 102 V122" {W(4)}/>
<rect x="84" y="74" width="16" height="14" rx="4" fill="#6A3A1E" {W(2.4)}/><path d="M86 80 Q92 76 98 80" fill="none" stroke="#fff" stroke-width="1.6"/>
<rect x="104" y="74" width="16" height="14" rx="4" fill="#8A4A26" {W(2.4)}/><circle cx="112" cy="79" r="2" fill="#E8304A"/>
<ellipse cx="50" cy="66" rx="20" ry="22" fill="#9A5A2E" {W(3)}/>
<path d="M50 44 Q44 66 50 88" fill="none" stroke="#6A3A1E" stroke-width="2.4"/>
<path d="M30 54 Q50 36 70 54 L66 58 Q50 46 34 58Z" fill="#fff" {W(2.4)}/><path d="M68 54 L76 50 L74 58Z" fill="#fff" {W(2)}/>
{eye(43, 68, .45)}{eye(57, 68, .45)}<path d="M46 75 Q50 78 54 75" fill="none" {W(2)}/>{blush(38, 75, .5)}{blush(62, 75, .5)}
<path d="M10 70 H22 M6 80 H18" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')


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
    print("нарисовано:", len(I))
