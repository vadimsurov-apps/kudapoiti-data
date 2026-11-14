"""Иконки робота pools, 2026-11-14 (02 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои сверены с реестром icons-src/subjects.txt
(точных совпадений героя и сцены нет), картинки — tools/check_unique.py.
Иконки laguna-detstva-voskresenskoe (рыба-капля), fitnes-holl-shcherbinka (поросёнок с гантелей) и ustinov-beregovaya
(лебедёнок, из tools/icons_pools_1113z.py) нарисованы впрок: места не добавлены (нет точки), svg и строки реестра не
записаны — при добавлении проверить уникальность заново.
Запуск: python3 tools/icons_pools_1114c.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2
import icons_pools_1113z as PZ

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
BL = '<ellipse cx="{}" cy="{}" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>'

# 2. «Лагуна детства» (Воскресенское, с 2 месяцев до 7 лет) — рыба-капля нежится в тёплой лагуне
ICONS["laguna-detstva-voskresenskoe"] = W("#FFF0B8", "#FF9A5C", f'''
<circle cx="98" cy="30" r="15" fill="#FFF7D6" opacity=".9"/>
<path d="M-6 74 Q30 66 64 74 T134 72 V134 H-6Z" fill="#8E7BEA" {s()}/>
<path d="M-6 134 V110 Q30 98 64 110 T134 108 V134Z" fill="#6A56C9" opacity=".55"/>
<path d="M12 62 Q14 30 32 14" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M12 62 Q14 30 32 14" fill="none" stroke="#9A6B3C" stroke-width="4" stroke-linecap="round"/>
<path d="M32 14 Q50 6 62 18 Q46 16 34 22Z M32 14 Q14 2 2 12 Q18 12 28 20Z M32 14 Q40 28 34 42 Q28 30 28 20Z" fill="#3DBE7A" {s(T2)}/>
<path d="M28 84 Q22 60 50 56 Q82 52 100 70 Q110 82 100 96 Q84 110 54 106 Q32 104 28 84Z" fill="#FFA9C4" {s()}/>
<path d="M98 72 l16 -8 q4 12 -2 22Z" fill="#FF86AC" {s(T2)}/>
<path d="M54 86 Q50 100 62 104 Q76 106 76 92 Q74 82 64 82 Q56 82 54 86Z" fill="#FF86AC" {s(T2)}/>
{eye(48, 74, 1.05)}{eye(80, 72, 1.05)}
<path d="M44 96 Q38 100 34 96 M86 98 Q92 102 96 98" fill="none" {s(T2)}/>
{BL.format(40, 86)}{BL.format(90, 84)}
<path d="M64 52 Q62 40 56 36 M64 52 Q66 40 72 36 M64 52 V34" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="54" cy="33" r="2.6" fill="#fff"/><circle cx="64" cy="29" r="2.6" fill="#fff"/><circle cx="74" cy="33" r="2.6" fill="#fff"/>
<path d="M8 118 q9 -5 18 0 M96 120 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 76, 22)
SUBJ["laguna-detstva-voskresenskoe"] = ("розовая рыба-капля с большим висячим носом",
                                        "лежит на поверхности сиреневой лагуны под пальмой и пускает фонтанчик на закатном персиково-оранжевом фоне")

# 3. Детский бассейн «Умка» (Некрасовка, с рождения до 7 лет) — пуховый пингвинёнок прыгает в круглую прорубь «бомбочкой»
ICONS["umka-nekrasovka"] = W("#5B4FB8", "#1B1648", f'''
{sparkle(20, 22, 4)}{sparkle(104, 18, 5)}{sparkle(84, 34, 2.6)}{sparkle(36, 44, 2.4)}
<path d="M-6 92 Q30 84 64 90 T134 88 V134 H-6Z" fill="#EAF6FF" {s()}/>
<ellipse cx="64" cy="108" rx="40" ry="13" fill="#2FB5E0" {s()}/>
<path d="M36 106 q8 -4 16 0 M70 112 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M36 50 Q16 44 14 60 Q22 70 40 64Z M92 50 Q112 44 114 60 Q106 70 88 64Z" fill="#8E97AD" {s()}/>
<ellipse cx="20" cy="56" rx="9" ry="6.5" fill="#FFB02E" {s(T2)} transform="rotate(-20 20 56)"/><ellipse cx="108" cy="56" rx="9" ry="6.5" fill="#FFB02E" {s(T2)} transform="rotate(20 108 56)"/>
<path d="M52 84 Q44 96 56 96 Q62 94 60 86Z M76 84 Q84 96 72 96 Q66 94 68 86Z" fill="#FFB02E" {s(T2)}/>
<path d="M34 54 Q32 16 64 14 Q96 16 94 54 Q94 88 64 88 Q34 88 34 54Z" fill="#A9B2C6" {s()}/>
<path d="M44 44 Q44 26 56 28 Q64 30 64 38 Q64 30 72 28 Q84 26 84 44 Q84 58 64 60 Q44 58 44 44Z" fill="#fff" {s(T2)}/>
<ellipse cx="64" cy="70" rx="17" ry="13" fill="#F4F6FA" {s(T2)}/>
<path d="M50 42 q5 -5 10 0 M68 42 q5 -5 10 0" fill="none" {s(T2)}/>
<path d="M58 49 L64 46 L70 49 L64 56Z" fill="#FF8A1F" {s(T2)}/>
{BL.format(48, 50)}{BL.format(80, 50)}
<path d="M56 16 q4 -9 8 -2 q4 -7 8 2" fill="none" {s(T2)}/>
''', 50, 24)
SUBJ["umka-nekrasovka"] = ("серый пуховый пингвинёнок с белой мордочкой в оранжевых нарукавниках",
                           "зажмурившись и раскинув крылышки, прыгает «бомбочкой» в круглую голубую прорубь-бассейн посреди снега под звёздным полярным небом")

# 4. Школа плавания и водного поло «Акулы» (Троицк, гимназия им. Пушкова, 6–17 лет) — акулёнок-ватерполист бросает мяч
ICONS["akuly-troitsk-letokhova"] = W("#FFE9B0", "#FF8A3D", f'''
<path d="M84 16 H126 V70 H84Z" fill="#fff" opacity=".35"/>
<path d="M84 16 H128 M84 16 V72 M96 16 V72 M108 16 V72 M120 16 V72 M84 30 H128 M84 44 H128 M84 58 H128" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M84 74 V14 H130" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M84 74 V14 H130" fill="none" stroke="#E8443A" stroke-width="4.6" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="66" cy="26" r="12" fill="#FFD23F" {s()}/>
<path d="M56 22 Q66 28 76 22 M62 15 Q60 26 64 37" fill="none" {s('stroke-width="2"')}/>
<path d="M30 60 L18 40 Q32 42 40 54Z" fill="#6E8FB3" {s()}/>
<path d="M14 110 Q10 62 42 54 Q70 50 74 78 Q76 96 70 110Z" fill="#86A7CC" {s()}/>
<path d="M30 110 Q28 84 46 78 Q64 76 66 92 L66 110Z" fill="#F4F8FC" {s(T2)}/>
<path d="M64 70 Q78 52 70 40" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M64 70 Q78 52 70 40" fill="none" stroke="#86A7CC" stroke-width="6.6" stroke-linecap="round"/>
<path d="M22 66 Q30 44 52 48 Q62 52 62 62 Q44 56 22 66Z" fill="#fff" {s()}/>
<circle cx="26" cy="72" r="7" fill="#35A0E8" {s(T2)}/>
<path d="M36 55 h10 M41 50 v10" stroke="#35A0E8" stroke-width="2.6" stroke-linecap="round"/>
{eye(46, 72, 1.1)}
<path d="M48 90 Q58 96 66 88" fill="none" {s(T2)}/>
<path d="M52 92 l3 5 l3 -4 l3 4 l3 -6" fill="#fff" {s('stroke-width="1.6"')}/>
{BL.format(40, 84)}
<path d="M-6 104 Q14 96 34 104 T74 104 T114 104 T140 104 V134 H-6Z" fill="#2E86DE" {s()}/>
<path d="M84 118 q9 -5 18 0 M40 120 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 26)
SUBJ["akuly-troitsk-letokhova"] = ("серо-голубой акулёнок в белой ватерпольной шапочке с голубыми наушниками",
                                   "высунулся из воды по пояс и бросает плавником жёлтый мяч в красные ворота с белой сеткой на оранжевом фоне")

# 5. Школа плавания Magic Swim (бассейн «Серебряный», 7–17 лет) — кролик фокусника в цилиндре-лодочке
ICONS["magic-swim-glagoleva"] = W("#F7B8F0", "#8A2FB8", f'''
{sparkle(22, 30, 5, "#FFE46B")}{sparkle(106, 46, 4, "#FFE46B")}{sparkle(30, 62, 3)}
<path d="M56 34 Q50 8 60 6 Q66 10 64 34Z" fill="#fff" {s()}/><path d="M58 30 Q55 16 60 12 Q62 16 61 30Z" fill="#FFB7CF"/>
<path d="M70 34 Q76 8 86 12 Q86 22 78 38Z" fill="#fff" {s()}/><path d="M73 32 Q77 18 82 17 Q82 24 76 34Z" fill="#FFB7CF"/>
<ellipse cx="66" cy="54" rx="22" ry="21" fill="#fff" {s()}/>
<path d="M44 50 H88" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<circle cx="56" cy="50" r="8.5" fill="#9FF0FF" {s()}/><circle cx="76" cy="50" r="8.5" fill="#9FF0FF" {s()}/>
<circle cx="56" cy="50" r="3.2" fill="{O}"/><circle cx="76" cy="50" r="3.2" fill="{O}"/>
<circle cx="54.6" cy="48.4" r="1.2" fill="#fff"/><circle cx="74.6" cy="48.4" r="1.2" fill="#fff"/>
<ellipse cx="66" cy="62" rx="3" ry="2.4" fill="#FF7FA8"/>
<path d="M61 67 Q66 71 71 67" fill="none" {s(T2)}/>
<path d="M86 62 Q100 54 104 38" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>
<path d="M86 62 Q100 54 104 38" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M100 44 L114 16" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M100 44 L114 16" stroke="#2B2540" stroke-width="3.4" stroke-linecap="round"/>
<path d="M112 20 L115 14" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
{sparkle(118, 10, 6, "#FFE46B")}
<path d="M38 70 H94 L90 106 H42Z" fill="#2B2540" {s()}/>
<ellipse cx="66" cy="70" rx="36" ry="8" fill="#3D3560" {s()}/>
<path d="M41 92 H91" stroke="#FF5A8A" stroke-width="7"/>
<path d="M-6 100 Q14 92 34 100 T74 100 T114 100 T140 100 V134 H-6Z" fill="#40C4E8" {s()}/>
<path d="M10 116 q9 -5 18 0 M56 120 q9 -5 18 0 M98 114 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 40, 20)
SUBJ["magic-swim-glagoleva"] = ("белый кролик фокусника в плавательных очках",
                                "выглядывает из чёрного цилиндра, который плывёт по воде как лодочка, и взмахивает волшебной палочкой со звездой на малиново-фиолетовом фоне")

# 6. Клуб синхронного и спортивного плавания «Время побеждать» (Академия водного транспорта, с 5 лет) — будильник-чемпион
ICONS["vremya-pobezhdat-sudostroitelnaya"] = W("#D8FFF0", "#19B592", f'''
<path d="M-6 90 Q14 82 34 90 T74 90 T114 90 T140 90 V134 H-6Z" fill="#1F6FD1" {s()}/>
<path d="M30 40 L10 14 M98 40 L118 14" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M30 40 L10 14 M98 40 L118 14" stroke="#FF5A5A" stroke-width="5.6" stroke-linecap="round"/>
<circle cx="10" cy="13" r="6.5" fill="#fff" {s(T2)}/><circle cx="118" cy="13" r="6.5" fill="#fff" {s(T2)}/>
<path d="M38 26 Q32 10 46 12 Q56 14 52 24Z M90 26 Q96 10 82 12 Q72 14 76 24Z" fill="#FFD23F" {s()}/>
<path d="M60 16 h8 v8 h-8Z" fill="#FFD23F" {s(T2)}/>
<circle cx="64" cy="60" r="38" fill="#FF5A5A" {s()}/>
<circle cx="64" cy="60" r="29" fill="#FFFDF3" {s()}/>
<path d="M64 36 v5 M64 79 v5 M40 60 h5 M83 60 h5" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<path d="M64 60 L52 44 M64 60 L76 44" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<circle cx="64" cy="60" r="3.4" fill="{O}"/>
{eye(53, 64, 1.0)}{eye(75, 64, 1.0)}
<path d="M57 74 Q64 81 71 74Z" fill="#4A2A45" {s('stroke-width="2"')}/>
{BL.format(46, 72)}{BL.format(82, 72)}
<path d="M18 92 q-6 -12 2 -16 M110 92 q6 -12 -2 -16" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
<path d="M26 108 q9 -5 18 0 M84 110 q9 -5 18 0 M54 120 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 50, 26)
SUBJ["vremya-pobezhdat-sudostroitelnaya"] = ("красный круглый будильник с жёлтыми звоночками и стрелками буквой V",
                                             "выпрыгивает из синей воды, победно вскинув вверх обе руки в красных рукавах, на изумрудно-мятном фоне")

# 7. Бассейн ФОК «Нахабино» (25 м, глубина до 2,08 м, учат с 3 лет) — жирафёнок стоит на дне, над водой только голова
ICONS["fok-nakhabino"] = W("#EAF8FF", "#8ED0F5", f'''
<path d="M-6 50 H134 V134 H-6Z" fill="#33B6E6" {s()}/>
<path d="M-6 118 H134 V134 H-6Z" fill="#7FE0F2" opacity=".8"/>
<path d="M112 50 V118 M106 62 h12 M106 76 h12 M106 90 h12 M106 104 h12" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M52 118 Q46 96 56 88 H82 Q90 98 84 118Z" fill="#FFCB3D" {s()}/>
<path d="M58 88 V46 H76 V88Z" fill="#FFCB3D" {s()}/>
<circle cx="64" cy="62" r="3.6" fill="#D98A1E"/><circle cx="71" cy="76" r="4" fill="#D98A1E"/><circle cx="62" cy="90" r="3.4" fill="#D98A1E"/><circle cx="74" cy="100" r="4" fill="#D98A1E"/><circle cx="60" cy="106" r="3.2" fill="#D98A1E"/>
<path d="M54 10 V2 M74 10 V2" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M54 10 V3 M74 10 V3" stroke="#D98A1E" stroke-width="3.2" stroke-linecap="round"/>
<circle cx="54" cy="2" r="3.6" fill="#8A5A2A" {s('stroke-width="2"')}/><circle cx="74" cy="2" r="3.6" fill="#8A5A2A" {s('stroke-width="2"')}/>
<path d="M40 20 Q30 18 28 26 Q34 32 44 28Z M88 20 Q98 18 100 26 Q94 32 84 28Z" fill="#FFCB3D" {s(T2)}/>
<path d="M44 14 Q64 4 84 14 Q90 26 86 38 Q84 50 64 50 Q44 50 42 38 Q38 26 44 14Z" fill="#FFD95E" {s()}/>
<ellipse cx="64" cy="40" rx="15" ry="9" fill="#FFF0C2" {s(T2)}/>
<circle cx="59" cy="39" r="1.8" fill="{O}"/><circle cx="69" cy="39" r="1.8" fill="{O}"/>
{eye(54, 24, 1.0)}{eye(74, 24, 1.0)}
{BL.format(46, 33)}{BL.format(82, 33)}
<path d="M22 50 q9 -6 18 0 M88 50 q9 -6 18 0" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
{bub(28, 76, 4.5)}{bub(36, 96, 3)}{bub(22, 104, 2.4)}
''', 30, 16)
SUBJ["fok-nakhabino"] = ("жёлтый жирафёнок с рыжими пятнами на длинной шее",
                         "стоит на дне глубокого бассейна в разрезе: вся шея под водой рядом с белой линейкой глубины, над водой только довольная голова, на светло-голубом фоне")

# 8. Фитнес-клуб «Фитнес Холл» (Щербинка, детей учат плавать с 3 лет) — поросёнок-силач плывёт с гантелей
ICONS["fitnes-holl-shcherbinka"] = W("#E9F7C8", "#8CCB3F", f'''
<path d="M-6 76 Q14 68 34 76 T74 76 T114 76 T140 76 V134 H-6Z" fill="#2AA7D8" {s()}/>
<path d="M82 54 Q94 46 90 30" fill="none" stroke="{O}" stroke-width="13" stroke-linecap="round"/>
<path d="M82 54 Q94 46 90 30" fill="none" stroke="#FFB3C7" stroke-width="7.4" stroke-linecap="round"/>
<path d="M72 28 H106" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M72 28 H106" stroke="#C9CED6" stroke-width="3.2" stroke-linecap="round"/>
<rect x="62" y="17" width="12" height="22" rx="4" fill="#E8443A" {s()}/><rect x="101" y="17" width="12" height="22" rx="4" fill="#E8443A" {s()}/>
<path d="M22 44 L14 26 Q28 26 34 38Z M70 40 L82 24 Q86 38 78 46Z" fill="#FF8FAE" {s()}/>
<ellipse cx="50" cy="66" rx="36" ry="30" fill="#FFB3C7" {s()}/>
<ellipse cx="46" cy="74" rx="14" ry="10" fill="#FF8FAE" {s(T2)}/>
<ellipse cx="41" cy="74" rx="2.4" ry="3.6" fill="{O}"/><ellipse cx="51" cy="74" rx="2.4" ry="3.6" fill="{O}"/>
<path d="M18 56 H82" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<circle cx="34" cy="56" r="9" fill="#3D6FD1" {s()}/><circle cx="60" cy="56" r="9" fill="#3D6FD1" {s()}/>
<circle cx="34" cy="56" r="4.6" fill="#BFE9FF"/><circle cx="60" cy="56" r="4.6" fill="#BFE9FF"/>
<circle cx="34" cy="56" r="2.2" fill="{O}"/><circle cx="60" cy="56" r="2.2" fill="{O}"/>
{BL.format(24, 72)}{BL.format(70, 72)}
<path d="M-6 92 Q14 84 34 92 T74 92 T114 92 T140 92 V134 H-6Z" fill="#2AA7D8"/>
<path d="M-6 92 Q14 84 34 92 T74 92 T114 92 T140 92" fill="none" {s()}/>
<path d="M100 96 q10 -10 14 0 q-2 8 -8 4" fill="none" stroke="#FF8FAE" stroke-width="4" stroke-linecap="round"/>
<path d="M14 110 q9 -5 18 0 M60 116 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 24, 24)
SUBJ["fitnes-holl-shcherbinka"] = ("розовый поросёнок в синих плавательных очках",
                                   "плывёт по грудь в воде и одной лапкой поднимает над головой красную гантель, сзади из воды торчит хвостик-завиток, на салатовом фоне")

# 9. Акваклуб «Нептунята» (Троицк, с 2 месяцев до 9 лет, две чаши) — ужонок-Нептун в короне плывёт волной к трезубцу
ICONS["neptunyata-troitsk"] = W("#E8DBFF", "#9A6BE8", f'''
<path d="M-6 70 H134 V134 H-6Z" fill="#1E9BD6" {s()}/>
<path d="M-6 100 H134" stroke="#fff" stroke-width="6" stroke-dasharray="10 12" opacity=".55"/>
<path d="M108 30 V78 M98 22 V38 Q98 46 108 46 Q118 46 118 38 V22 M108 20 V46" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M108 30 V78 M98 22 V38 Q98 46 108 46 Q118 46 118 38 V22 M108 20 V46" fill="none" stroke="#FF8A1F" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M4 78 Q16 44 30 70 Q44 96 56 70 Q64 52 74 62" fill="none" stroke="{O}" stroke-width="21" stroke-linecap="round"/>
<path d="M4 78 Q16 44 30 70 Q44 96 56 70 Q64 52 74 62" fill="none" stroke="#3FB86A" stroke-width="14.6" stroke-linecap="round"/>
<path d="M12 64 l4 4 M24 60 l4 5 M44 80 l5 -3 M56 70 l5 2" stroke="#2A8F4C" stroke-width="3" stroke-linecap="round"/>
<path d="M-6 82 Q10 76 22 82 T48 86 T70 82 V134 H-6Z" fill="#1E9BD6"/>
<g transform="translate(-8 12)">
<ellipse cx="84" cy="56" rx="22" ry="18" fill="#4CC777" {s()}/>
<ellipse cx="66" cy="50" rx="5" ry="6.5" fill="#FFD23F" {s(T2)}/><ellipse cx="84" cy="40" rx="6.5" ry="4.6" fill="#FFD23F" {s(T2)}/>
{eye(80, 54, 1.1)}{eye(96, 54, 1.1)}
<path d="M84 64 Q90 69 96 64" fill="none" {s(T2)}/>
<path d="M104 62 q8 0 10 -4 M106 60 l8 4" stroke="#E8443A" stroke-width="2.4" stroke-linecap="round" fill="none"/>
{BL.format(74, 62)}
<path d="M68 41 l3 -12 l8 8 l7 -10 l7 10 l8 -8 l3 12Z" fill="#FFD23F" {s(T2)}/>
</g>
<path d="M52 90 Q76 82 100 90" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
<path d="M20 116 q9 -5 18 0 M72 118 q9 -5 18 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 22)
SUBJ["neptunyata-troitsk"] = ("зелёный водяной ужонок с жёлтыми пятнышками-ушками в золотой короне Нептуна",
                              "плывёт волной, выгибая спинку двумя горбами над водой, к торчащему из бассейна оранжевому трезубцу на сиреневом фоне")

ICONS["ustinov-beregovaya"] = PZ.ICONS["ustinov-beregovaya"]
SUBJ["ustinov-beregovaya"] = PZ.SUBJ["ustinov-beregovaya"]

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
