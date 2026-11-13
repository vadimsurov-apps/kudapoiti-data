"""Иконки робота pools, 2026-11-13 (20 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои проверены по реестру icons-src/subjects.txt
(водоворот, селезень, йети, китовая акула, гурами, манта, лысуха, водопад — в реестре не встречались), картинки —
tools/check_unique.py. Иконки пяти мест прошлого запуска (ss1-mei, akvabulko-reutov, world-swim-reutov,
akvadarina-reutov, torpeda-ivanteevka) нарисованы тогда же — tools/icons_pools_1113u.py.
Запуск: python3 tools/icons_pools_1113x.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
BL = '<ellipse cx="{}" cy="{}" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>'

# 1. Flowswim «Яуза» («Плыви в потоке», группы 7+) — весёлый водоворот крутит плавательную доску
ICONS["flowswim-yauza"] = W("#FFF0FA", "#E66DB6", f'''
<circle cx="62" cy="68" r="47" fill="#2D8FE6" {s()}/>
<path d="M62 24 A44 44 0 0 1 106 68" fill="none" stroke="#8ED3FF" stroke-width="8" stroke-linecap="round"/>
<path d="M62 112 A44 44 0 0 1 18 68" fill="none" stroke="#8ED3FF" stroke-width="8" stroke-linecap="round"/>
<circle cx="62" cy="68" r="31" fill="#4DB2F5" {s(T2)}/>
<path d="M36 52 A31 31 0 0 1 78 41" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".85"/>
<path d="M88 84 A31 31 0 0 1 46 95" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".85"/>
<circle cx="62" cy="68" r="17" fill="#BFE8FF" {s(T2)}/>
{eye(55, 65, .95)}{eye(69, 65, .95)}
<path d="M56 73 Q62 79 68 73" fill="none" {s(T2)}/>
<g transform="rotate(38 100 34)"><rect x="82" y="25" width="36" height="18" rx="9" fill="#FFD23F" {s()}/><path d="M92 34 h16" stroke="#F09A1A" stroke-width="3" stroke-linecap="round"/></g>
<path d="M14 26 q4 -8 8 0 q0 6 -4 6 q-4 0 -4 -6Z M108 104 q4 -8 8 0 q0 6 -4 6 q-4 0 -4 -6Z M22 110 q3 -6 6 0 q0 5 -3 5 q-3 0 -3 -5Z" fill="#fff" {s(T2)}/>
''', 30, 24)
SUBJ["flowswim-yauza"] = ("синий водоворот-воронка с мордашкой в самой серединке",
                          "закручивает белые струи потока по кругу и катает по краю жёлтую плавательную доску на малиново-розовом фоне")

# 2. Flowswim «Баланс» (малая чаша для 3–6 лет) — селезень держит равновесие на одной лапке
ICONS["flowswim-balans"] = W("#FFFBE0", "#FFB23F", f'''
<path d="M-6 96 Q28 88 62 96 T134 94 V134 H-6Z" fill="#3E9BE6" {s()}/>
<rect x="26" y="88" width="76" height="13" rx="6.5" fill="#FF6FA5" {s()}/>
<path d="M64 88 V74" stroke="#FF9A2E" stroke-width="5" stroke-linecap="round"/>
<path d="M56 88 h16 l-8 -6Z" fill="#FF9A2E" {s(T2)}/>
<path d="M78 70 l12 8 -3 5" fill="none" stroke="#FF9A2E" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M40 60 Q14 50 8 34 Q30 36 46 48Z" fill="#B9C2D2" {s()}/>
<path d="M88 60 Q114 50 120 34 Q98 36 82 48Z" fill="#B9C2D2" {s()}/>
<ellipse cx="64" cy="60" rx="27" ry="19" fill="#DDE2EC" {s()}/>
<path d="M46 50 Q64 40 82 50 Q76 64 64 64 Q52 64 46 50Z" fill="#8B5A3C" {s(T2)}/>
<circle cx="64" cy="30" r="16" fill="#1F9E6A" {s()}/>
<path d="M50 40 Q64 48 78 40" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round"/>
<path d="M54 34 Q64 30 74 34 Q72 43 64 43 Q56 43 54 34Z" fill="#FFD23F" {s(T2)}/>
{eye(57, 26, .85)}{eye(71, 26, .85)}
<path d="M10 110 q9 -5 18 0 M96 114 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 64, 16)
SUBJ["flowswim-balans"] = ("селезень с зелёной головой, белым ошейником и жёлтым клювом",
                           "стоит на одной оранжевой лапке на розовой плавательной доске, раскинув серые крылья для равновесия, на солнечно-жёлтом фоне")

# 3. Flowswim «Северный» (50 м) — йети плывёт кролем под северным сиянием
ICONS["flowswim-severny"] = W("#3F52AE", "#10173F", f'''
<path d="M-4 22 Q30 4 62 22 T132 16" fill="none" stroke="#5CF2B0" stroke-width="7" stroke-linecap="round" opacity=".85"/>
<path d="M-4 36 Q34 18 66 36 T132 30" fill="none" stroke="#B48CFF" stroke-width="5" stroke-linecap="round" opacity=".8"/>
{sparkle(104, 46, 4)}{sparkle(18, 52, 3)}
<path d="M84 62 Q96 26 116 30 Q122 42 100 70Z" fill="#fff" {s()}/>
<path d="M112 30 l4 -7 M117 33 l7 -4 M118 39 l8 1" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<path d="M24 82 Q20 52 46 46 Q50 38 58 44 Q66 36 74 46 Q98 50 96 82Z" fill="#fff" {s()}/>
<path d="M36 70 Q40 58 60 58 Q80 58 84 70 Q80 84 60 84 Q40 84 36 70Z" fill="#CFE6FF" {s(T2)}/>
<rect x="38" y="62" width="44" height="9" rx="4.5" fill="#1E6FE0" {s(T2)}/>
<circle cx="50" cy="66.500" r="7" fill="#7FD4FF" {s(T2)}/><circle cx="70" cy="66.500" r="7" fill="#7FD4FF" {s(T2)}/>
<circle cx="50" cy="67" r="2.6" fill="{O}"/><circle cx="70" cy="67" r="2.6" fill="{O}"/>
<path d="M54 77 Q60 82 66 77" fill="none" {s(T2)}/>
<path d="M-6 86 Q28 78 62 86 T134 84 V134 H-6Z" fill="#2C8FD8" {s()}/>
<path d="M-6 100 Q28 93 62 100 T134 98 V134 H-6Z" fill="#55B4F2"/>
<path d="M14 92 l-8 -10 M26 88 l-2 -12 M100 88 l4 -11" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/>
<path d="M30 114 q9 -5 18 0 M78 112 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 50, 60)
SUBJ["flowswim-severny"] = ("белый лохматый йети в синих плавательных очках",
                            "плывёт кролем, занеся над водой мохнатую лапу, ночью под зелёно-сиреневыми лентами северного сияния")

# 4. «Акулы брасса» (Дмитров) — китовая акула в горошек плывёт брассом прямо на зрителя
ICONS["akuly-brassa-dmitrov"] = W("#FFF0F1", "#FF7E8E", f'''
<path d="M30 70 Q4 66 2 92 Q20 94 36 84Z" fill="#4E7FB8" {s()}/>
<path d="M98 70 Q124 66 126 92 Q108 94 92 84Z" fill="#4E7FB8" {s()}/>
<path d="M64 18 Q72 4 78 22Z" fill="#3F6AA0" {s()}/>
<path d="M20 66 Q20 22 64 20 Q108 22 108 66 Q108 100 64 102 Q20 100 20 66Z" fill="#5E90CC" {s()}/>
<path d="M30 76 Q64 68 98 76 Q94 98 64 98 Q34 98 30 76Z" fill="#fff" {s(T2)}/>
<path d="M40 82 Q64 94 88 82" fill="none" {s(T2)}/>
<circle cx="40" cy="38" r="3.2" fill="#fff"/><circle cx="56" cy="30" r="3.2" fill="#fff"/><circle cx="74" cy="31" r="3.2" fill="#fff"/><circle cx="90" cy="40" r="3.2" fill="#fff"/>
<circle cx="48" cy="48" r="2.6" fill="#fff"/><circle cx="64" cy="42" r="2.6" fill="#fff"/><circle cx="80" cy="48" r="2.6" fill="#fff"/>
<circle cx="30" cy="52" r="2.4" fill="#fff"/><circle cx="98" cy="52" r="2.4" fill="#fff"/>
{eye(34, 66, 1.0)}{eye(94, 66, 1.0)}
{BL.format(40, 75)}{BL.format(88, 75)}
{bub(14, 28, 5)}{bub(112, 24, 4)}{bub(104, 108, 3.4)}{bub(22, 110, 3)}
''', 64, 30)
SUBJ["akuly-brassa-dmitrov"] = ("сине-голубая китовая акула в белый горошек с широкой белой улыбкой",
                                "плывёт брассом прямо на зрителя, разведя грудные плавники в стороны, на кораллово-розовом фоне")

# 5. «Золотой Моржик» (Видное, 0–7 лет) — золотой гурами с мальком
ICONS["zolotoy-morzhik-vidnoe"] = W("#F7EEFF", "#A77BEA", f'''
<path d="M24 58 L4 40 Q10 60 4 82Z" fill="#FF9A2E" {s()}/>
<path d="M40 40 Q58 22 80 36Z" fill="#FF9A2E" {s()}/>
<path d="M20 60 Q44 30 78 38 Q102 46 104 62 Q100 80 76 86 Q44 92 20 60Z" fill="#FFC93A" {s()}/>
<path d="M34 66 Q56 84 88 76 Q64 90 34 66Z" fill="#FFE590"/>
<path d="M70 78 Q66 106 50 118 M78 78 Q80 104 70 120" fill="none" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<path d="M70 78 Q66 106 50 118 M78 78 Q80 104 70 120" fill="none" stroke="#FF9A2E" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="58" cy="56" r="3" fill="#E07B12"/><circle cx="44" cy="60" r="2.6" fill="#E07B12"/>
{eye(86, 56, 1.05)}
<path d="M95 68 Q100 71 103 66" fill="none" {s(T2)}/>
{BL.format(80, 67)}
<path d="M100 96 L90 88 Q92 97 90 106Z" fill="#FF9A2E" {s(T2)}/>
<ellipse cx="108" cy="97" rx="11" ry="8" fill="#FFC93A" {s()}/>
{eye(112, 95, .6)}
{bub(112, 40, 5)}{bub(120, 26, 3.4)}{bub(104, 22, 2.6)}
''', 70, 26)
SUBJ["zolotoy-morzhik-vidnoe"] = ("золотой гурами с двумя длинными усиками-ниточками и рыжими крапинками на боку",
                                  "плывёт вправо, а за ним спешит крошечный золотой малёк, на сиреневом фоне с пузырьками")

# 6. «Афалина» (Дмитров, бассейн «Бриз») — манта парит в лучах света
ICONS["afalina-dmitrov"] = W("#D8FDFF", "#149DBB", f'''
<path d="M40 -4 L20 60 M70 -4 L64 46 M100 -4 L112 56" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".35"/>
<path d="M64 84 Q70 108 58 126" fill="none" stroke="{O}" stroke-width="5.5" stroke-linecap="round"/>
<path d="M64 84 Q70 108 58 126" fill="none" stroke="#2E3F8F" stroke-width="2.4" stroke-linecap="round"/>
<path d="M64 34 Q90 42 124 30 Q112 70 78 86 Q64 92 50 86 Q16 70 4 30 Q38 42 64 34Z" fill="#34479E" {s()}/>
<path d="M50 34 Q44 22 52 16 Q58 22 58 34Z M78 34 Q84 22 76 16 Q70 22 70 34Z" fill="#34479E" {s()}/>
<path d="M46 60 Q64 52 82 60 Q78 80 64 82 Q50 80 46 60Z" fill="#E9F1FF" {s(T2)}/>
<path d="M56 74 Q64 79 72 74" fill="none" {s(T2)}/>
{eye(54, 64, .85)}{eye(74, 64, .85)}
<path d="M22 44 q8 6 16 6 M106 44 q-8 6 -16 6" fill="none" stroke="#7C90E6" stroke-width="3" stroke-linecap="round"/>
{bub(104, 92, 4.5)}{bub(114, 80, 3)}{bub(18, 96, 3.6)}
''', 64, 10)
SUBJ["afalina-dmitrov"] = ("тёмно-синий скат-манта с белым животиком и двумя рожками-плавниками на голове",
                           "парит, широко раскинув крылья-плавники, в косых лучах света в бирюзовой глубине")

# 7. «Детки-Рыбки» (Дмитров) — мама-лысуха ведёт птенцов гуськом
ICONS["detki-rybki-dmitrov"] = W("#F6FFE6", "#86D45E", f'''
<path d="M-6 74 Q28 66 62 74 T134 72 V134 H-6Z" fill="#3FA7E0" {s()}/>
<path d="M22 78 Q16 52 40 48 L52 50 Q70 46 76 62 Q78 80 56 84 H34Z" fill="#2B2B3F" {s()}/>
<path d="M16 60 Q8 52 10 44 Q20 48 26 56Z" fill="#2B2B3F" {s()}/>
<circle cx="72" cy="42" r="14" fill="#2B2B3F" {s()}/>
<path d="M76 30 Q86 30 86 42 L98 46 L84 50 Q78 48 76 40Z" fill="#fff" {s(T2)}/>
<circle cx="70" cy="40" r="3.4" fill="#E0342B"/><circle cx="70" cy="40" r="1.5" fill="{O}"/>
<ellipse cx="100" cy="76" rx="10" ry="7.5" fill="#4A4A5E" {s()}/><circle cx="108" cy="68" r="6.5" fill="#F0843C" {s(T2)}/>
<circle cx="110" cy="67" r="1.5" fill="{O}"/><path d="M114 69 l5 1 -5 2Z" fill="#fff" {s('stroke-width="1.6"')}/>
<ellipse cx="14" cy="84" rx="8" ry="6" fill="#4A4A5E" {s()}/><circle cx="20" cy="77" r="5.5" fill="#F0843C" {s(T2)}/>
<circle cx="21.500" cy="76" r="1.3" fill="{O}"/>
<path d="M-6 88 Q28 82 62 88 T134 86 V134 H-6Z" fill="#62C0F2"/>
<path d="M30 102 q10 -5 20 0 M70 108 q10 -5 20 0 M36 118 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 40, 20)
SUBJ["detki-rybki-dmitrov"] = ("чёрная птица лысуха с белой бляшкой на лбу и белым клювом",
                               "плывёт по голубой воде, а за ней и перед ней — два серых птенца с рыжими головками, на светло-зелёном фоне")

# 8. Школа плавания Mad Wave (ДС «Янтарь»: в малом бассейне водопад и детская горка) — водопад-персонаж
ICONS["madwave-strogino"] = W("#FFFFFF", "#FF9F6B", f'''
<rect x="18" y="14" width="92" height="16" rx="5" fill="#E9EEF5" {s()}/>
<path d="M40 14 v16 M64 14 v16 M88 14 v16" stroke="{O}" stroke-width="2.2"/>
<path d="M34 30 H94 V96 Q94 104 86 104 H42 Q34 104 34 96Z" fill="#35B8F0" {s()}/>
<path d="M46 34 V92 M82 34 V92" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".65"/>
<path d="M58 36 V52 M70 36 V50" stroke="#fff" stroke-width="3.4" stroke-linecap="round" opacity=".65"/>
{eye(55, 66, 1.15)}{eye(73, 66, 1.15)}
<path d="M56 78 Q64 88 72 78Z" fill="#fff" {s(T2)}/>
{BL.format(47, 76)}{BL.format(81, 76)}
<path d="M-6 104 Q28 96 62 104 T134 102 V134 H-6Z" fill="#1E86D8" {s()}/>
<circle cx="30" cy="102" r="10" fill="#fff" {s(T2)}/><circle cx="46" cy="106" r="8" fill="#fff" {s(T2)}/><circle cx="84" cy="106" r="8" fill="#fff" {s(T2)}/><circle cx="98" cy="102" r="10" fill="#fff" {s(T2)}/><circle cx="64" cy="108" r="8" fill="#fff" {s(T2)}/>
<path d="M22 118 q9 -5 18 0 M86 120 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 64, 60)
SUBJ["madwave-strogino"] = ("голубой водопад с мордашкой и румяными щёчками",
                            "льётся широкой лентой с кафельного бортика в бассейн и взбивает внизу белую пену на персиковом фоне")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
