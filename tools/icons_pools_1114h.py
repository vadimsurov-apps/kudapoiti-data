"""Иконки робота pools, 2026-11-14 (08 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои сверены с реестром icons-src/subjects.txt
(таких героев в реестре нет), картинки — tools/check_unique.py.
Записаны svg и строки реестра 6 добавленных мест. Иконки kitik-veshnyakovskaya (плавунчик), laguna-boba-borisovsky (шилоклювка)
и chayka-gazoprovod (чайка-моевка с доской) нарисованы впрок: места не добавлены (нет точки) — при добавлении проверить
уникальность заново.
Запуск: python3 tools/icons_pools_1114h.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
BL = '<ellipse cx="{}" cy="{}" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>'

# 1. Детский бассейн «Китик» (с рождения до 7 лет) — куличок-плавунчик кружится на воде волчком
ICONS["kitik-veshnyakovskaya"] = W("#FFF0DC", "#FF9E7A", f'''
<ellipse cx="64" cy="92" rx="70" ry="44" fill="#22B7C9" {s()}/>
<path d="M14 92 a50 24 0 1 0 100 0 a40 18 0 1 0 -80 0 a30 12 0 1 0 60 0" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" opacity=".85"/>
<path d="M98 72 L116 58 Q116 78 100 84Z" fill="#5E6E82" {s(T2)}/>
<path d="M36 80 Q36 58 64 58 Q92 58 102 76 Q92 92 64 92 Q44 92 36 80Z" fill="#8FA3B8" {s()}/>
<path d="M58 70 Q76 62 94 74 Q78 80 58 70Z" fill="#5E6E82" {s(T2)}/>
<path d="M40 82 Q64 96 96 82 Q82 92 64 92 Q48 92 40 82Z" fill="#fff"/>
<path d="M34 62 Q30 76 44 82 Q54 78 54 64Z" fill="#D9622B" {s(T2)}/>
<circle cx="42" cy="50" r="15" fill="#fff" {s()}/>
<path d="M28 46 Q42 28 56 46 Q42 40 28 46Z" fill="#4B586B" {s(T2)}/>
<path d="M28 52 L8 55 L28 58Z" fill="{O}" {s(T2)}/>
{eye(40, 51, 1.1)}
{BL.format(49, 58)}
{bub(104, 40, 4)}{bub(112, 28, 2.6)}
''', 30, 20)
SUBJ["kitik-veshnyakovskaya"] = ("куличок-плавунчик с рыжей шейкой, серой спинкой и тонким чёрным клювом",
                                 "кружится на воде волчком — вокруг него по бирюзовой глади расходится белая спираль ряби, небо персиковое")

# 2. Детский бассейн «Глубина» (2 месяца – 7 лет) — усатый морской заяц ныряет в глубину за жёлтым кольцом
ICONS["glubina-berzarina"] = W("#3D86E8", "#0A1B57", f'''
<path d="M30 -6 L52 -6 L30 70 L8 70Z M70 -6 L88 -6 L74 54 L58 54Z" fill="#fff" opacity=".12"/>
<path d="M-6 112 Q30 104 64 110 T134 108 V134 H-6Z" fill="#E9C98A" {s()}/>
<ellipse cx="30" cy="106" rx="15" ry="6" fill="none" stroke="{O}" stroke-width="10"/>
<ellipse cx="30" cy="106" rx="15" ry="6" fill="none" stroke="#FFD23F" stroke-width="5.6"/>
<path d="M19 102 l4 6 M38 101 l4 7" stroke="#E8443A" stroke-width="5" fill="none"/>
<path d="M112 14 Q124 4 122 22 Q118 30 106 30Z M100 8 Q96 -4 108 0 Q112 10 106 18Z" fill="#7C8AA3" {s(T2)}/>
<path d="M112 20 Q118 52 92 76 Q72 94 50 86 Q36 80 40 62 Q46 46 66 48 Q88 48 98 22Z" fill="#A9B4C6" {s()}/>
<path d="M82 64 Q96 76 92 90 Q80 86 74 74Z" fill="#7C8AA3" {s(T2)}/>
<path d="M60 86 Q76 80 92 60 Q80 82 60 86Z" fill="#DDE4EE"/>
<ellipse cx="50" cy="78" rx="11" ry="8" fill="#EEF2F7" {s(T2)}/>
<ellipse cx="46" cy="72" rx="3.6" ry="2.8" fill="{O}"/>
<path d="M42 78 L22 70 M41 81 L20 80 M42 84 L24 92 M56 82 L70 96 M52 84 L58 100" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{eye(56, 62, 1.15)}{eye(68, 68, 1)}
{bub(104, 52, 4.4)}{bub(112, 66, 3)}{bub(98, 40, 2.4)}
''', 30, 10)
SUBJ["glubina-berzarina"] = ("серый морской заяц лахтак с пышными белыми усами",
                             "ныряет наискосок в тёмно-синюю глубину за жёлтым кольцом для ныряния, лежащим на песчаном дне, сверху падают лучи света")

# 3. Детский бассейн «Лагуна Боба» (3 месяца – 8 лет) — шилоклювка катит клювом надувной мяч по мелкой лагуне
ICONS["laguna-boba-borisovsky"] = W("#FFF7B8", "#FFD14A", f'''
<path d="M-6 84 Q30 76 64 84 T134 82 V134 H-6Z" fill="#3FD3C4" {s()}/>
<path d="M-6 134 V112 Q40 104 64 112 T134 108 V134Z" fill="#17A99C" opacity=".6"/>
<path d="M76 70 L74 108 M88 70 L92 108" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M76 70 L74 108 M88 70 L92 108" fill="none" stroke="#8FB6D9" stroke-width="2.8" stroke-linecap="round"/>
<ellipse cx="74" cy="108" rx="7" ry="2.4" fill="none" stroke="#fff" stroke-width="2"/><ellipse cx="92" cy="108" rx="7" ry="2.4" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M56 56 Q62 38 86 40 Q110 44 116 58 Q104 76 80 74 Q62 72 56 56Z" fill="#fff" {s()}/>
<path d="M74 44 Q96 44 114 58 Q98 56 84 62 Q76 54 74 44Z" fill="{O}"/>
<path d="M66 60 Q78 66 96 62" fill="none" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<path d="M58 54 Q52 40 54 32" fill="none" stroke="{O}" stroke-width="13" stroke-linecap="round"/>
<path d="M58 54 Q52 40 54 32" fill="none" stroke="#fff" stroke-width="7.4" stroke-linecap="round"/>
<circle cx="54" cy="26" r="12" fill="#fff" {s()}/>
<path d="M44 20 Q54 8 66 22 Q56 20 54 28 Q50 22 44 20Z" fill="{O}"/>
<path d="M44 30 Q34 44 22 40" fill="none" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>
{eye(52, 27, .95)}
{BL.format(58, 33)}
<circle cx="22" cy="60" r="19" fill="#fff" {s()}/>
<path d="M22 41 Q34 60 22 79 Q10 60 22 41Z" fill="#E8443A" {s(T2)}/>
<path d="M4 54 Q22 50 40 54 M4 66 Q22 70 40 66" fill="none" stroke="#2E8BE6" stroke-width="3.4"/>
<circle cx="22" cy="60" r="19" fill="none" {s()}/>
''', 70, 20)
SUBJ["laguna-boba-borisovsky"] = ("чёрно-белая шилоклювка на длинных голубых ногах с клювом, загнутым вверх",
                                  "стоит по колено в мелкой бирюзовой лагуне и клювом-шильцем подталкивает большой красно-белый надувной мяч, фон солнечно-жёлтый")

# 4. «Виктория», синхронное плавание (Можайск, с 3 лет) — тюлень-хохлач держит вертикаль вниз головой
ICONS["viktoriya-mozhaysk"] = W("#FFE3F1", "#F77FB4", f'''
<path d="M-6 50 Q28 42 64 50 T134 48 V134 H-6Z" fill="#6B5BD6" {s()}/>
<path d="M-6 134 V96 Q40 88 64 96 T134 92 V134Z" fill="#4335A8" opacity=".6"/>
<path d="M54 44 Q30 30 30 10 Q46 12 62 34Z M74 44 Q98 30 98 10 Q82 12 66 34Z" fill="#6E7F99" {s()}/>
<path d="M50 44 Q46 78 52 96 Q64 108 76 96 Q82 78 78 44Z" fill="#B9C4D6" {s()}/>
<circle cx="58" cy="62" r="3" fill="#6E7F99"/><circle cx="70" cy="74" r="3.4" fill="#6E7F99"/><circle cx="60" cy="84" r="2.6" fill="#6E7F99"/><circle cx="71" cy="54" r="2.4" fill="#6E7F99"/>
<path d="M50 66 Q34 68 30 80 Q42 82 52 76Z M78 66 Q94 68 98 80 Q86 82 76 76Z" fill="#6E7F99" {s(T2)}/>
<circle cx="64" cy="100" r="18" fill="#B9C4D6" {s()}/>
{eye(55, 98, 1.1)}{eye(73, 98, 1.1)}
<path d="M58 90 Q64 86 70 90" fill="none" {s(T2)}/>
<circle cx="64" cy="114" r="10" fill="#FF4D5E" {s()}/>
<circle cx="60.6" cy="111" r="2.6" fill="#fff" opacity=".8"/>
<path d="M30 52 q8 -5 16 0 M84 52 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{sparkle(108, 26, 7)}{sparkle(18, 30, 5)}
{bub(98, 104, 3.6)}{bub(28, 108, 3)}
''', 50, 14)
SUBJ["viktoriya-mozhaysk"] = ("пятнистый тюлень-хохлач с надутым красным пузырём на носу",
                              "держит вертикаль синхронистки вниз головой: над сиреневой водой торчит хвост буквой V, а под водой он улыбается, раскинув ласты, небо розовое")

# 5. Школа «Чайка», бассейн в посёлке Газопровод — чайка-моевка несёт в лапках оранжевую плавательную доску
ICONS["chayka-gazoprovod"] = W("#FFFFFF", "#74C0FF", f'''
<path d="M-6 104 Q30 96 64 104 T134 100 V134 H-6Z" fill="#1F7FE0" {s()}/>
<path d="M14 116 q8 -5 16 0 M52 120 q8 -5 16 0 M92 114 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M60 52 Q30 18 4 30 Q10 34 14 40 Q34 38 50 62Z" fill="#C9D3E0" {s()}/>
<path d="M4 30 Q10 34 14 40 L24 36 Q14 28 4 30Z" fill="{O}"/>
<path d="M72 52 Q96 12 126 22 Q120 28 116 34 Q98 34 82 60Z" fill="#C9D3E0" {s()}/>
<path d="M126 22 Q120 28 116 34 L106 30 Q116 22 126 22Z" fill="{O}"/>
<path d="M44 58 Q48 44 66 44 Q86 46 92 60 Q80 72 62 70 Q48 68 44 58Z" fill="#fff" {s()}/>
<path d="M92 60 l14 4 l-12 6Z" fill="#fff" {s(T2)}/>
<circle cx="48" cy="52" r="11" fill="#fff" {s()}/>
<path d="M38 54 L24 58 L38 60Z" fill="#FFD23F" {s(T2)}/>
{eye(46, 50, .95)}
<path d="M62 70 L60 80 M74 70 L76 80" fill="none" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>
<path d="M40 80 Q40 74 48 74 H88 Q96 74 96 80 V88 Q96 96 86 96 H50 Q40 96 40 88Z" fill="#FF8A1F" {s()}/>
<path d="M50 85 H86" stroke="#fff" stroke-width="3.4" stroke-linecap="round" opacity=".8"/>
''', 50, 20)
SUBJ["chayka-gazoprovod"] = ("белая чайка-моевка с серыми крыльями, чёрными кончиками перьев и жёлтым клювом",
                             "летит над синей водой, широко раскинув крылья, и несёт в лапках оранжевую плавательную доску")

# 6. Школа «Чайка», Крылатское — водяная землеройка кутора гребёт под водой вдоль разделительной дорожки
ICONS["chayka-krylatskoe"] = W("#B4F5DA", "#0E9C8A", f'''
<g transform="rotate(-14 64 30)">{"".join(f'<circle cx="{x}" cy="30" r="5" fill="{"#E8443A" if i % 2 == 0 else "#fff"}" {s(T2)}/>' for i, x in enumerate(range(-4, 140, 12)))}</g>
<path d="M92 84 Q112 96 124 80" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M92 84 Q112 96 124 80" fill="none" stroke="#3A3F52" stroke-width="3.4" stroke-linecap="round"/>
<path d="M30 72 Q40 52 66 54 Q92 56 100 78 Q92 96 66 96 Q44 96 30 72Z" fill="#3A3F52" {s()}/>
<path d="M34 76 Q52 90 80 90 Q92 90 98 82 Q90 96 66 96 Q46 96 34 76Z" fill="#F4F6FA"/>
<path d="M38 66 L10 76 L36 82Z" fill="#3A3F52" {s()}/>
<circle cx="10" cy="76" r="4.4" fill="#FF8FA8" {s(T2)}/>
<circle cx="44" cy="68" r="7" fill="#fff" {s(T2)}/>{eye(44, 68, 1)}
<circle cx="56" cy="57" r="4.4" fill="#3A3F52" {s(T2)}/>
<path d="M54 92 Q46 106 38 102 M78 94 Q84 108 94 104" fill="none" stroke="{O}" stroke-width="6" stroke-linecap="round"/>
<path d="M54 92 Q46 106 38 102 M78 94 Q84 108 94 104" fill="none" stroke="#FFB3C1" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="62" cy="64" r="2" fill="#fff" opacity=".9"/><circle cx="74" cy="62" r="2.4" fill="#fff" opacity=".9"/><circle cx="84" cy="70" r="2" fill="#fff" opacity=".9"/><circle cx="70" cy="74" r="1.8" fill="#fff" opacity=".9"/>
{bub(108, 60, 4.6)}{bub(116, 46, 3.2)}{bub(100, 44, 2.4)}{bub(22, 100, 3.4)}
''', 30, 24)
SUBJ["chayka-krylatskoe"] = ("водяная землеройка кутора — тёмная спинка, белый животик и длинный розовый носик",
                             "гребёт лапками под водой вдоль красно-белой разделительной дорожки, на шёрстке серебрятся пузырьки воздуха, вода зелёная")

# 7. Школа «Чайка», бассейн «Зоркий» (Красногорск) — портрет чайки-хохотуна в зеркальных очках
ICONS["chayka-zorky-krasnogorsk"] = W("#FFE48F", "#FF7A3D", f'''
<path d="M18 134 Q14 96 34 84 H94 Q114 96 110 134Z" fill="#fff" {s()}/>
<circle cx="64" cy="58" r="40" fill="#fff" {s()}/>
<path d="M22 50 H106" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M22 50 H106" stroke="#2A3350" stroke-width="5" stroke-linecap="round"/>
<rect x="28" y="36" width="32" height="26" rx="12" fill="#3EC5F0" {s()}/>
<rect x="68" y="36" width="32" height="26" rx="12" fill="#3EC5F0" {s()}/>
<path d="M36 58 L44 40 M46 58 L52 42 M76 58 L84 40 M86 58 L92 42" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-dasharray="5 4" opacity=".9"/>
<path d="M60 48 h8" {s()} fill="none"/>
<path d="M50 70 Q64 64 78 70 Q76 86 64 98 Q52 86 50 70Z" fill="#FFD23F" {s()}/>
<circle cx="64" cy="88" r="3.4" fill="#E8443A"/>
<path d="M54 76 Q64 80 74 76" fill="none" {s(T2)}/>
{BL.format(36, 72)}{BL.format(92, 72)}
{sparkle(104, 28, 6)}
''', 50, 16)
SUBJ["chayka-zorky-krasnogorsk"] = ("чайка-хохотун с большим жёлтым клювом в голубых зеркальных очках для плавания",
                                    "портрет крупным планом на оранжевом фоне: смотрит прямо на нас, а в стёклах очков отражаются пунктиры дорожек бассейна")

# 8. Школа «Чайка», Автозаводская (ЗИЛ) — синий грузовичок-амфибия в красной шапочке плывёт по бассейну
ICONS["chayka-avtozavodskaya"] = W("#F3F4FF", "#9AA7E8", f'''
<path d="M24 60 H74 V88 H24Z" fill="#C98A4B" {s()}/>
<path d="M24 70 H74 M24 79 H74" stroke="{O}" stroke-width="2" opacity=".5"/>
<path d="M74 48 Q74 40 82 40 H100 Q110 40 112 52 L114 88 H74Z" fill="#2F6FE0" {s()}/>
<path d="M76 40 Q94 22 112 44 Q94 36 76 40Z" fill="#E8443A" {s()}/>
<rect x="80" y="48" width="26" height="15" rx="7" fill="#BFEFFF" {s(T2)}/>
<path d="M93 48 v15" {s(T2)}/>
<circle cx="88" cy="56" r="2.6" fill="{O}"/><circle cx="99" cy="56" r="2.6" fill="{O}"/>
<path d="M86 74 Q94 80 102 74" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<rect x="108" y="76" width="9" height="7" rx="3" fill="#FFD23F" {s(T2)}/>
<circle cx="40" cy="92" r="12" fill="#3B3355"/><circle cx="40" cy="92" r="5" fill="#C9D3E0"/>
<circle cx="94" cy="92" r="12" fill="#3B3355"/><circle cx="94" cy="92" r="5" fill="#C9D3E0"/>
<path d="M-6 92 Q28 84 64 92 T134 90 V134 H-6Z" fill="#28A9E6" opacity=".92" {s()}/>
<path d="M10 106 q8 -5 16 0 M56 112 q8 -5 16 0 M100 106 q8 -5 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<path d="M18 88 q-8 -10 -14 -4 M22 84 q-4 -12 -12 -12" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
{bub(16, 60, 3.6)}{bub(8, 48, 2.4)}
''', 40, 20)
SUBJ["chayka-avtozavodskaya"] = ("синий грузовичок-амфибия с деревянным кузовом, в красной плавательной шапочке и с очками вместо лобового стекла",
                                 "плывёт по голубой воде бассейна, колёса наполовину под водой, сзади летят брызги, фон сиреневый")

# 9. Школа «Чайка», ЖК «Дубровка» — рыжая уточка-савка с голубым клювом плывёт мимо дубового листа с жёлудем
ICONS["chayka-dubrovka"] = W("#4FA36C", "#0F3A27", f'''
<path d="M-6 70 Q30 62 64 70 T134 68 V134 H-6Z" fill="#1E6B55" {s()}/>
<g transform="translate(8 8) scale(.82)"><path d="M4 96 Q8 80 24 84 Q22 76 34 78 Q36 88 46 86 Q44 98 30 104 Q14 106 4 96Z" fill="#E08A2E" {s(T2)}/>
<path d="M8 96 Q26 92 42 86" fill="none" stroke="{O}" stroke-width="2"/>
<ellipse cx="28" cy="112" rx="7" ry="9" fill="#C9A15A" {s(T2)}/>
<path d="M20 108 Q28 98 36 108Z" fill="#7A5230" {s(T2)}/></g>
<path d="M104 62 L122 30 L112 68Z M100 60 L112 34" fill="#5B2E1A" {s(T2)}/>
<path d="M52 72 Q56 52 80 52 Q104 54 110 70 Q104 88 80 88 Q58 88 52 72Z" fill="#B5502A" {s()}/>
<path d="M66 64 Q82 58 98 68 Q84 74 66 64Z" fill="#8A3A1C" {s(T2)}/>
<circle cx="52" cy="54" r="16" fill="#fff" {s()}/>
<path d="M36 52 Q40 34 56 36 Q68 38 68 50 Q54 44 36 52Z" fill="{O}"/>
<path d="M40 56 Q24 54 18 62 Q28 70 42 64Z" fill="#3EA8F0" {s()}/>
{eye(50, 54, 1.05)}
{BL.format(58, 62)}
<path d="M58 92 q8 -5 16 0 M88 94 q8 -5 16 0 M70 104 q8 -5 16 0" fill="none" stroke="#9FE3C4" stroke-width="3" stroke-linecap="round"/>
''', 40, 14)
SUBJ["chayka-dubrovka"] = ("рыжая уточка-савка с белыми щеками, голубым клювом и торчащим вверх хвостом",
                           "плывёт по тёмно-зелёной воде, а рядом качаются оранжевый дубовый лист и жёлудь в шляпке")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    for i in ids:
        open(os.path.join(OUT, i + ".svg"), "w", encoding="utf-8").write(ICONS[i])
    print("svg:", len(ids))
    for i in ids:
        print(f"{i} — герой: {SUBJ[i][0]} | сцена: {SUBJ[i][1]}")
