"""Иконки робота pools, 2026-11-14 (14 UTC). Каждая придумана и нарисована отдельно (правило абсолютной
уникальности): свой герой, своя сцена, своя компоновка и палитра. Герои сверены с реестром icons-src/subjects.txt
(таких героев в реестре нет), картинки — tools/check_unique.py.
Запуск: python3 tools/icons_pools_1114p.py [id …]  → python3 tools/render_icons.py <id…> → python3 tools/check_unique.py <id…>."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, sparkle, O
from icons_pools_1112b import W, bub, T2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
ICONS, SUBJ = {}, {}
BL = '<ellipse cx="{}" cy="{}" rx="4.4" ry="2.6" fill="#FF7FA8" opacity=".8"/>'

# 1. «Золотые рыбки», Дворец спорта «Янтарь» (группы 3–8 лет, малый бассейн 0,6–0,9 м) — селезень утки-мандаринки стоит по грудь в воде с доской
ICONS["zolotye-rybki-yantar"] = W("#EAF9F1", "#9ADBC0", f'''
<path d="M-6 78 Q28 70 64 78 T134 76 V134 H-6Z" fill="#35B8D6" {s()}/>
<path d="M38 82 Q36 56 58 54 Q84 52 92 70 Q94 84 86 92 H44Z" fill="#C8743A" {s()}/>
<path d="M70 58 Q82 36 96 50 Q92 62 82 66Z" fill="#F28C28" {s(T2)}/>
<path d="M50 62 Q58 58 66 62" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<circle cx="44" cy="44" r="19" fill="#F6E7C8" {s()}/>
<path d="M27 38 Q40 14 62 34 Q50 30 40 36 Q32 40 27 38Z" fill="#2E7D5B" {s(T2)}/>
<path d="M56 30 Q72 28 70 46 Q62 40 58 40Z" fill="#7A3FA0" {s(T2)}/>
<path d="M27 46 L12 50 L27 54Z" fill="#E8483F" {s(T2)}/>
{eye(40, 45, 1.2)}
{BL.format(49, 54)}
<rect x="6" y="66" width="38" height="20" rx="8" fill="#FFD23F" {s()} transform="rotate(-8 25 76)"/>
<path d="M14 100 q8 -5 16 0 M56 106 q8 -5 16 0 M96 98 q8 -5 16 0" fill="none" stroke="#C9F3FA" stroke-width="3" stroke-linecap="round"/>
''', 60, 18)
SUBJ["zolotye-rybki-yantar"] = ("селезень утки-мандаринки с кремовыми щеками, зелёным хохолком и оранжевым пером-парусом на спине",
                         "стоит по грудь в мелкой голубой воде и толкает перед собой жёлтую плавательную доску, фон мятный")

# 2. Школа плавания № 1, бассейн на ул. Садовники (7–13 лет, 25 м, 6 дорожек) — синий марлин финиширует носом в бортик
ICONS["ss1-ranhigs-sadovniki"] = W("#FFE9D6", "#FF9A6B", f'''
<rect x="-6" y="52" width="140" height="82" fill="#1E6FD0" {s()}/>
<rect x="96" y="36" width="40" height="98" fill="#F4F6FA" {s()}/>
<path d="M96 60 H134 M96 84 H134 M96 108 H134" stroke="#B9C4D6" stroke-width="3"/>
<circle cx="110" cy="48" r="4.5" fill="#FF4D4D" {s(T2)}/>
<path d="M-6 66 H96" stroke="#FFD23F" stroke-width="4" stroke-dasharray="9 7"/>
<path d="M-6 122 H96" stroke="#FFD23F" stroke-width="4" stroke-dasharray="9 7"/>
<path d="M4 92 L-8 76 L8 86 L-6 108Z" fill="#12489C" {s(T2)}/>
<path d="M4 92 Q26 74 54 82 Q72 86 78 92 Q66 104 44 106 Q20 106 4 92Z" fill="#2B8BE8" {s()}/>
<path d="M14 96 Q40 102 72 94 Q62 104 44 106 Q24 106 14 96Z" fill="#E9F4FF"/>
<path d="M26 80 Q40 58 62 72 Q56 78 50 82Z" fill="#12489C" {s(T2)}/>
<path d="M76 91 L98 88" fill="none" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<path d="M40 100 Q44 112 54 110" fill="none" {s(T2)}/>
{eye(62, 88, 1.0)}
<path d="M100 78 l8 -8 M104 90 l10 0 M100 100 l8 8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
''', 30, 16)
SUBJ["ss1-ranhigs-sadovniki"] = ("синий марлин с длинным носом-копьём и высоким спинным плавником-парусом",
                                 "финиширует: упирается носом в белый кафельный бортик между двумя жёлтыми пунктирными дорожками, от касания летят искры, фон персиковый")

# 3. Start Swim, бассейн на Земляном Валу (5–16 лет) — тигрёнок в очках ныряет со стартовой тумбы
ICONS["start-swim-zemlyanoy-val"] = W("#DDF1FF", "#6DB7F2", f'''
<path d="M-6 98 Q30 90 64 98 T134 96 V134 H-6Z" fill="#1565C0" {s()}/>
<path d="M78 96 L84 70 H120 L126 96Z" fill="#F4F6FA" {s()}/>
<path d="M76 70 L124 62 V72 L76 78Z" fill="#E8483F" {s()}/>
<text x="101" y="92" font-family="Arial" font-weight="700" font-size="15" text-anchor="middle" fill="#1565C0">5</text>
<path d="M84 60 Q70 34 40 40 Q22 46 20 66 Q34 62 44 66 Q64 70 84 60Z" fill="#FF9A2E" {s()}/>
<path d="M62 42 l4 12 M50 40 l2 12 M72 48 l2 10" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>
<path d="M84 60 Q96 56 100 46" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M84 60 Q96 56 100 46" fill="none" stroke="#FF9A2E" stroke-width="4" stroke-linecap="round"/>
<circle cx="26" cy="68" r="17" fill="#FFB347" {s()}/>
<path d="M12 58 l-4 -10 l10 4Z M36 54 l6 -9 l4 11Z" fill="#FF9A2E" {s(T2)}/>
<path d="M26 52 v6 M19 54 l2 5 M33 54 l-2 5" stroke="{O}" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="24" cy="76" rx="8" ry="6" fill="#fff"/>
<rect x="12" y="62" width="26" height="9" rx="4.5" fill="#35C4E8" {s(T2)}/>
<circle cx="19" cy="66.5" r="2" fill="{O}"/><circle cx="31" cy="66.5" r="2" fill="{O}"/>
<path d="M22 75 l2 2.5 l2 -2.5" fill="#E8483F" {s(T2)}/>
<path d="M16 50 Q4 62 10 84 M36 50 Q26 30 8 36" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M16 50 Q4 62 10 84 M36 50 Q26 30 8 36" fill="none" stroke="#FF9A2E" stroke-width="4" stroke-linecap="round"/>
<path d="M6 108 q8 -5 16 0 M40 114 q8 -5 16 0" fill="none" stroke="#BFE6FF" stroke-width="3" stroke-linecap="round"/>
''', 70, 14)
SUBJ["start-swim-zemlyanoy-val"] = ("рыжий полосатый тигрёнок в голубых очках для плавания",
                                    "ныряет рыбкой вниз головой с белой стартовой тумбы № 5 с красной площадкой в тёмно-синюю воду, фон небесно-голубой")

# 4. Strong Swim, СК «Волна» (Чертановская ул.) — водяной буйволёнок плывёт баттерфляем
ICONS["strong-swim-chertanovskaya"] = W("#F3F0D8", "#C9C27A", f'''
<path d="M-6 88 Q30 78 64 88 T134 86 V134 H-6Z" fill="#00A6A6" {s()}/>
<path d="M30 80 Q8 60 14 40 M98 80 Q120 60 114 40" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round"/>
<path d="M30 80 Q8 60 14 40 M98 80 Q120 60 114 40" fill="none" stroke="#5C6470" stroke-width="9" stroke-linecap="round"/>
<circle cx="14" cy="38" r="7" fill="#3B4250" {s(T2)}/><circle cx="114" cy="38" r="7" fill="#3B4250" {s(T2)}/>
<path d="M34 66 Q20 44 36 34 Q30 48 44 56Z M94 66 Q108 44 92 34 Q98 48 84 56Z" fill="#F2E3B6" {s(T2)}/>
<ellipse cx="64" cy="70" rx="33" ry="27" fill="#6E7785" {s()}/>
<ellipse cx="64" cy="82" rx="20" ry="13" fill="#B9C0CC" {s(T2)}/>
<ellipse cx="57" cy="81" rx="2.6" ry="3.6" fill="{O}"/><ellipse cx="71" cy="81" rx="2.6" ry="3.6" fill="{O}"/>
{eye(52, 62, 1.15)}{eye(76, 62, 1.15)}
<path d="M44 52 q8 -6 14 -2 M70 50 q8 -4 14 2" fill="none" {s(T2)}/>
<path d="M8 90 q-6 -12 2 -18 M22 94 q-10 -4 -12 -14 M120 90 q6 -12 -2 -18 M106 94 q10 -4 12 -14" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
<path d="M36 110 q8 -5 16 0 M76 112 q8 -5 16 0" fill="none" stroke="#BFF3F3" stroke-width="3" stroke-linecap="round"/>
''', 50, 14)
SUBJ["strong-swim-chertanovskaya"] = ("серый водяной буйволёнок с кремовыми рогами-полумесяцами и нахмуренными бровями силача",
                                      "плывёт баттерфляем прямо на зрителя: оба копыта взлетели над бирюзовой водой, по бокам белые всплески, фон песочно-оливковый")

# 5. Kido (Скандинавский бульвар) — гага катает пухового птенца на спине
ICONS["kido-skandinavsky"] = W("#D9E8F7", "#5B7DB8", f'''
<path d="M-6 70 Q30 62 64 70 T134 68 V134 H-6Z" fill="#7FD3E0" {s()}/>
<path d="M18 78 Q22 54 56 56 Q96 56 112 72 Q104 98 62 98 Q26 98 18 78Z" fill="#FFFFFF" {s()}/>
<path d="M30 92 Q62 104 100 88 Q92 98 62 98 Q40 98 30 92Z" fill="#2A2F3A"/>
<path d="M96 66 L118 58 Q116 76 106 80Z" fill="#2A2F3A" {s(T2)}/>
<path d="M36 62 Q30 44 34 30" fill="none" stroke="{O}" stroke-width="17" stroke-linecap="round"/>
<path d="M36 62 Q30 44 34 30" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round"/>
<circle cx="36" cy="28" r="14" fill="#fff" {s()}/>
<path d="M24 22 Q36 8 48 20 Q38 18 24 22Z" fill="#2A2F3A" {s(T2)}/>
<path d="M44 30 q6 4 4 10" fill="none" stroke="#9BD17A" stroke-width="5" stroke-linecap="round"/>
<path d="M23 28 L6 34 L24 36Z" fill="#C9B458" {s(T2)}/>
{eye(32, 27, 1.0)}
<circle cx="74" cy="48" r="13" fill="#8B6B4A" {s()}/>
<ellipse cx="74" cy="52" rx="7" ry="5" fill="#C9A77E"/>
<path d="M68 38 l2 -6 M74 36 l0 -7 M80 38 l2 -6" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>
<path d="M86 48 l8 2 l-8 3Z" fill="#4A4A4A" {s(T2)}/>
{eye(78, 46, 0.8)}
<path d="M10 108 q8 -5 16 0 M50 114 q8 -5 16 0 M92 108 q8 -5 16 0" fill="none" stroke="#E3F8FB" stroke-width="3" stroke-linecap="round"/>
''', 64, 10)
SUBJ["kido-skandinavsky"] = ("белая северная утка гага с чёрной шапочкой, чёрным хвостом и зелёным пятном на затылке",
                             "плывёт по светлой воде и везёт на спине бурого пухового птенца с хохолком, фон серо-синий, как северное небо")

# 6. «ГрудничОк» (ЖК «Бутово Парк», от 2 месяцев до 5 лет) — малыш снежной макаки сидит в тёплой купели
ICONS["grudnichok-butovo-park"] = W("#FFF1F5", "#F7A8C0", f'''
<path d="M40 30 q-8 -10 0 -18 M64 24 q-8 -10 0 -18 M88 30 q-8 -10 0 -18" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".9"/>
<circle cx="64" cy="64" r="30" fill="#C9C2B8" {s()}/>
<circle cx="36" cy="60" r="8" fill="#C9C2B8" {s(T2)}/><circle cx="92" cy="60" r="8" fill="#C9C2B8" {s(T2)}/>
<circle cx="36" cy="60" r="3.6" fill="#F28B82"/><circle cx="92" cy="60" r="3.6" fill="#F28B82"/>
<path d="M44 66 Q42 46 64 46 Q86 46 84 66 Q84 86 64 86 Q44 86 44 66Z" fill="#F28B82" {s(T2)}/>
<path d="M50 62 q6 -5 12 0 M66 62 q6 -5 12 0" fill="none" {s(T2)}/>
<path d="M58 76 Q64 81 70 76" fill="none" {s(T2)}/>
<circle cx="61" cy="70" r="1.4" fill="{O}"/><circle cx="67" cy="70" r="1.4" fill="{O}"/>
<path d="M46 40 Q64 26 82 40 Q82 30 64 28 Q46 30 46 40Z" fill="#FFFFFF" {s(T2)}/>
<path d="M54 30 h20" stroke="#6EC6E6" stroke-width="3"/>
<path d="M-6 88 Q30 80 64 88 T134 86 V134 H-6Z" fill="#4FC3D9" {s()}/>
<path d="M10 104 q8 -5 16 0 M52 110 q8 -5 16 0 M94 104 q8 -5 16 0" fill="none" stroke="#DFF7FB" stroke-width="3" stroke-linecap="round"/>
{bub(22, 78, 4)}{bub(106, 76, 3)}
''', 50, 30)
SUBJ["grudnichok-butovo-park"] = ("малыш японской снежной макаки с розовым личиком, зажмурившийся от удовольствия",
                                  "сидит по плечи в тёплой бирюзовой купели со сложенным белым полотенцем на макушке, над водой три струйки пара, фон розовый")

# 7. «Золотые рыбки» (Дворец детского спорта, Рабочая ул.) — оранда с золотой медалью
ICONS["zolotye-rybki-dds"] = W("#1D3F8F", "#0B1D4D", f'''
<path d="M-6 26 H134" stroke="#fff" stroke-width="5" stroke-dasharray="10 8"/>
<path d="M-6 26 H134" stroke="#35C4E8" stroke-width="5" stroke-dasharray="10 8" stroke-dashoffset="9"/>
<path d="M84 62 Q112 34 122 44 Q112 62 122 82 Q110 92 84 70Z" fill="#FFB52E" {s()}/>
<path d="M96 60 Q108 52 114 50 M96 68 Q108 74 114 78" fill="none" stroke="#E0762B" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="58" cy="66" rx="34" ry="26" fill="#FF9A2E" {s()}/>
<path d="M30 76 Q56 96 86 78 Q72 92 58 92 Q40 92 30 76Z" fill="#FFE1A6"/>
<path d="M40 44 Q56 22 76 44 Q58 38 40 44Z" fill="#E8483F" {s(T2)}/>
<circle cx="48" cy="38" r="5" fill="#E8483F" {s(T2)}/><circle cx="58" cy="34" r="5.4" fill="#E8483F" {s(T2)}/><circle cx="68" cy="38" r="5" fill="#E8483F" {s(T2)}/>
<path d="M58 88 Q54 104 66 106 Q70 96 66 90Z" fill="#FFB52E" {s(T2)}/>
{eye(40, 62, 1.3)}
<path d="M26 72 Q32 78 38 72" fill="none" {s(T2)}/>
{BL.format(46, 72)}
<path d="M50 84 L62 108 L74 84" fill="none" stroke="#E8483F" stroke-width="5" stroke-linejoin="round"/>
<circle cx="62" cy="110" r="10" fill="#FFD23F" {s()}/>
<text x="62" y="115" font-family="Arial" font-weight="700" font-size="13" text-anchor="middle" fill="#B36B00">1</text>
{bub(14, 52, 4)}{bub(20, 38, 2.6)}{sparkle(104, 104, 7, "#FFD23F")}
''', 40, 30)
SUBJ["zolotye-rybki-dds"] = ("пухлая золотая рыбка оранда с малиновой шапочкой-наростом на голове и раздвоенным хвостом",
                             "плывёт под бело-голубой разделительной дорожкой с золотой медалью «1» на красной ленте, вода тёмно-синяя, как на вечерней тренировке")

T3 = 'stroke-width="3"'
WV = '<path d="M{} {} q8 -5 16 0" fill="none" stroke="{}" stroke-width="3" stroke-linecap="round"/>'

# 8. SwimRocket, СК «Волна» — серебристая уклейка выпрыгивает из гребня большой волны
ICONS["swimrocket-volna-chertanovskaya"] = W("#FFF3D6", "#FFB88A", f"""
<path d="M-6 96 Q10 60 44 58 Q70 58 78 78 Q64 70 54 80 Q70 92 96 86 Q120 80 134 92 V134 H-6Z" fill="#1E88C8" {s()}/>
<path d="M30 70 Q44 62 58 66 M20 84 Q34 78 44 84" fill="none" stroke="#BFE6FF" stroke-width="4" stroke-linecap="round"/>
<path d="M60 52 Q84 20 116 22 Q104 44 76 60Z" fill="#DDE6EE" {s()}/>
<path d="M66 50 Q88 28 112 24 Q98 30 76 54Z" fill="#7FA6C4"/>
<path d="M60 52 L48 46 L54 62Z" fill="#9FB8CC" {s(T2)}/>
<path d="M88 30 l-2 -12 l12 6Z" fill="#9FB8CC" {s(T2)}/>
{eye(102, 30, 1.0)}
<circle cx="50" cy="40" r="3.4" fill="#fff"/><circle cx="40" cy="50" r="2.4" fill="#fff"/><circle cx="62" cy="34" r="2" fill="#fff"/>
""", 70, 20)
SUBJ["swimrocket-volna-chertanovskaya"] = ("узкая серебристая рыбка уклейка с серо-голубой спинкой",
                                           "свечой выпрыгивает из закрученного гребня большой синей волны, за хвостом летят белые брызги, небо закатно-персиковое")

# 9. «Золотые рыбки», ФОК «Яуза» (с 7 лет) — селезень гоголя с золотым глазом ныряет под воду
ICONS["zolotye-rybki-yauza"] = W("#0FA3B1", "#075E73", f"""
<path d="M-6 30 Q30 22 64 30 T134 28 V-6 H-6Z" fill="#CFF4F7" {s()}/>
<path d="M44 34 Q40 60 54 78 Q70 96 92 88 Q104 70 92 48 Q80 30 60 30Z" fill="#fff" {s()}/>
<path d="M58 34 Q50 56 62 74 Q74 88 90 86 Q80 70 74 52 Q70 38 58 34Z" fill="#20242E"/>
<path d="M50 30 l-10 -16 l16 6Z M70 30 l8 -16 l6 16Z" fill="#F28C28" {s(T2)}/>
<circle cx="78" cy="96" r="17" fill="#1F4D3A" {s()}/>
<ellipse cx="70" cy="102" rx="5" ry="6" fill="#fff"/>
<path d="M84 110 L92 124 L72 116Z" fill="#3A3F4A" {s(T2)}/>
<circle cx="84" cy="96" r="5.4" fill="#FFD23F" {s(T2)}/><circle cx="84" cy="96" r="2.2" fill="{O}"/>
{bub(104, 70, 5)}{bub(112, 52, 3.4)}{bub(30, 86, 4)}{bub(24, 64, 2.6)}
""", 50, 60)
SUBJ["zolotye-rybki-yauza"] = ("чёрно-белый селезень утки гоголя с тёмно-зелёной головой и круглым золотым глазом",
                               "ныряет вертикально вниз головой: оранжевые лапки ещё торчат у поверхности, вокруг пузыри, вода изумрудно-бирюзовая")

# 10. «Золотые рыбки», СК «Коралл» (дошкольники с 3 лет) — краснопёрка с малышом-мальком плывут мимо кораллово-белой дорожки
ICONS["zolotye-rybki-korall"] = W("#E6FBFF", "#8ED8EC", f"""
<path d="M-6 104 H134" stroke="#fff" stroke-width="7" stroke-dasharray="12 9"/>
<path d="M-6 104 H134" stroke="#FF6F61" stroke-width="7" stroke-dasharray="12 9" stroke-dashoffset="10.5"/>
<path d="M82 52 L112 34 L104 56 L112 78Z" fill="#E8483F" {s()}/>
<path d="M22 56 Q40 30 68 36 Q88 42 90 56 Q84 74 60 78 Q36 78 22 56Z" fill="#D9C06A" {s()}/>
<path d="M30 60 Q54 76 84 62 Q76 76 60 78 Q40 78 30 60Z" fill="#F6EFC6"/>
<path d="M46 38 Q58 18 72 38Z" fill="#E8483F" {s(T2)}/>
<path d="M50 74 Q52 88 64 86 Q64 78 60 74Z" fill="#E8483F" {s(T2)}/>
<circle cx="38" cy="52" r="6.4" fill="#FF8A3C"/>{eye(38, 52, 1.05)}
<path d="M24 60 q4 4 9 1" fill="none" {s(T2)}/>
<path d="M36 90 l12 -6 l-3 6 l3 6Z" fill="#E8483F" {s(T2)}/>
<ellipse cx="26" cy="90" rx="12" ry="7.5" fill="#D9C06A" {s(T2)}/>
<circle cx="20" cy="88.5" r="2.2" fill="{O}"/>
{bub(104, 20, 4)}{bub(16, 28, 3)}
""", 30, 20)
SUBJ["zolotye-rybki-korall"] = ("золотисто-оливковая рыбка краснопёрка с ярко-красными плавниками и оранжевым глазом",
                                "плывёт влево, а под ней тем же курсом спешит её крошечная копия-малёк; внизу бело-коралловая разделительная дорожка, вода светло-голубая")

# 11. «Золотые рыбки», Мытищи — краснозобая казарка ведёт клином трёх разных по росту учеников
ICONS["zolotye-rybki-mytishchi-astrakhova"] = W("#FFE7EE", "#F4A3B8", f"""
<path d="M-6 60 Q30 52 64 60 T134 58 V134 H-6Z" fill="#3E7CB1" {s()}/>
<path d="M56 64 Q58 44 80 44 Q104 44 114 60 Q108 76 84 78 Q62 78 56 64Z" fill="#20242E" {s()}/>
<path d="M66 66 Q84 60 106 64" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
<path d="M64 52 Q60 36 66 26" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round"/>
<path d="M64 52 Q60 36 66 26" fill="none" stroke="#B5482A" stroke-width="9" stroke-linecap="round"/>
<circle cx="68" cy="24" r="11" fill="#20242E" {s()}/>
<ellipse cx="72" cy="27" rx="4.6" ry="5.4" fill="#B5482A" stroke="#fff" stroke-width="1.8"/>
<path d="M58 22 L48 25 L58 28Z" fill="#3A3F4A" {s(T2)}/>
<circle cx="64" cy="21" r="2" fill="#fff"/>
<circle cx="34" cy="78" r="9" fill="#F4E3B0" {s(T2)}/><circle cx="31" cy="77" r="1.8" fill="{O}"/><path d="M25 80 l-6 2 l6 2Z" fill="#3A3F4A"/>
<circle cx="52" cy="96" r="7" fill="#F4E3B0" {s(T2)}/><circle cx="50" cy="95" r="1.6" fill="{O}"/><path d="M45 97 l-5 2 l5 2Z" fill="#3A3F4A"/>
<circle cx="74" cy="110" r="5.4" fill="#F4E3B0" {s(T2)}/><circle cx="72.5" cy="109" r="1.4" fill="{O}"/><path d="M69 111 l-4 1.5 l4 1.5Z" fill="#3A3F4A"/>
""", 30, 15)
SUBJ["zolotye-rybki-mytishchi-astrakhova"] = ("краснозобая казарка — чёрная с белыми полосками, рыжей грудкой и рыжей щекой в белой каёмке",
                                              "плывёт по синей воде, а за ней наискосок, от большого к маленькому, три жёлтых пуховых гусёнка — как группы по возрасту, небо розовое")

# 12. «Территория Фитнеса», Реутов («родитель и малыш» с 3 месяцев) — шилоклювка с птенцом
ICONS["tswim-reutov"] = W("#E9F5E1", "#A7D38A", f"""
<path d="M-6 92 Q30 84 64 92 T134 90 V134 H-6Z" fill="#2FA8A0" {s()}/>
<path d="M58 92 V70 M74 92 V70" stroke="#6C8FB0" stroke-width="4.4" stroke-linecap="round"/>
<path d="M40 60 Q42 40 66 40 Q92 40 104 56 Q94 72 68 72 Q46 72 40 60Z" fill="#fff" {s()}/>
<path d="M60 44 Q80 40 100 56 Q84 52 62 54Z" fill="#20242E"/>
<path d="M48 50 Q40 36 42 26" fill="none" stroke="{O}" stroke-width="13" stroke-linecap="round"/>
<path d="M48 50 Q40 36 42 26" fill="none" stroke="#fff" stroke-width="7.4" stroke-linecap="round"/>
<circle cx="42" cy="24" r="10" fill="#fff" {s()}/>
<path d="M33 18 Q42 8 52 18 Q42 16 33 18Z" fill="#20242E" {s(T2)}/>
<path d="M33 26 Q16 30 6 20" fill="none" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<circle cx="39" cy="23" r="2" fill="{O}"/>
<path d="M22 92 V82 M30 92 V82" stroke="#6C8FB0" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="26" cy="74" rx="11" ry="9" fill="#D9CDB4" {s(T2)}/>
<circle cx="18" cy="64" r="7" fill="#D9CDB4" {s(T2)}/><circle cx="16" cy="63" r="1.7" fill="{O}"/>
<path d="M12 66 Q6 68 3 64" fill="none" stroke="{O}" stroke-width="2.2" stroke-linecap="round"/>
{WV.format(86, 108, "#C5F1EE")}{WV.format(38, 112, "#C5F1EE")}
""", 70, 18)
SUBJ["tswim-reutov"] = ("чёрно-белая болотная птица шилоклювка с тонким клювом, загнутым кверху, на голубых ногах",
                        "идёт по колено в бирюзовой воде, а перед ней шагает серый пуховой птенец с таким же загнутым клювиком — «родитель и малыш», фон травяно-зелёный")

# 13. SwimRocket, бассейн «Арктика» — белёк соскальзывает с льдины в воду
ICONS["swimrocket-arktika"] = W("#3F4FA8", "#1B2260", f"""
{sparkle(24, 22, 6)}{sparkle(104, 16, 4)}{sparkle(84, 34, 3)}
<path d="M-6 92 Q30 86 64 92 T134 90 V134 H-6Z" fill="#35C4E8" {s()}/>
<path d="M4 92 L22 72 H92 L110 92Z" fill="#F2FAFF" {s()}/>
<path d="M22 72 H92 L84 80 H30Z" fill="#CFE9F7"/>
<path d="M30 70 Q30 44 58 44 Q84 44 96 60 Q110 62 116 74 Q104 76 96 72 Q80 78 56 76 Q38 76 30 70Z" fill="#fff" {s()}/>
<circle cx="46" cy="56" r="17" fill="#fff" {s()}/>
{eye(40, 54, 1.25)}{eye(54, 54, 1.25)}
<ellipse cx="47" cy="62" rx="3.4" ry="2.4" fill="{O}"/>
<path d="M36 62 h-8 M36 65 l-7 3 M58 62 h8 M58 65 l7 3" stroke="{O}" stroke-width="1.6" stroke-linecap="round"/>
<path d="M62 74 Q66 84 76 82" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>
<path d="M62 74 Q66 84 76 82" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
{WV.format(20, 110, "#E3F8FF")}{WV.format(70, 114, "#E3F8FF")}
""", 50, 10)
SUBJ["swimrocket-arktika"] = ("белый пушистый детёныш тюленя белёк с большими чёрными глазами и усами",
                              "лежит на краю плоской льдины и пробует ластой голубую воду перед первым заплывом, над ним полярная ночь со звёздами")

# 14. SwimRocket, бассейн МГТУ им. Баумана — паук-серебрянка-инженер в воздушном колоколе
ICONS["swimrocket-bauman"] = W("#BFEBD9", "#3FA68A", f"""
<path d="M64 -4 V26" stroke="#fff" stroke-width="2.4" stroke-dasharray="3 4"/>
<path d="M22 84 Q20 30 64 28 Q108 30 106 84 Q84 96 64 96 Q44 96 22 84Z" fill="#F1FCFF" opacity=".85" {s()}/>
<path d="M34 60 Q36 42 52 38" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M44 76 l-16 12 M48 82 l-12 16 M84 76 l16 12 M80 82 l12 16" stroke="{O}" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="64" cy="74" rx="19" ry="15" fill="#8A5A3C" {s()}/>
<circle cx="64" cy="54" r="15" fill="#A8744E" {s()}/>
{eye(57, 53, 1.1)}{eye(71, 53, 1.1)}
<path d="M59 61 Q64 65 69 61" fill="none" {s(T2)}/>
<path d="M48 42 H80 L76 34 H52Z" fill="#FFD23F" {s(T2)}/>
<path d="M56 34 Q64 24 72 34Z" fill="#FFD23F" {s(T2)}/>
{bub(16, 40, 4)}{bub(112, 50, 3.4)}{bub(104, 104, 5)}{bub(22, 108, 3)}
""", 50, 20)
SUBJ["swimrocket-bauman"] = ("коричневый паучок-серебрянка в жёлтой инженерной каске",
                             "сидит под водой внутри большого прозрачного воздушного колокола, который сам построил, колокол висит на паутинке, вода зелёная")

# 15. SwimRocket, бассейн «Бескудниково» — водяная полёвка плывёт и толкает носом мяч
ICONS["swimrocket-beskudnikovo"] = W("#FFF7D1", "#F4D35E", f"""
<path d="M-6 70 Q30 62 64 70 T134 68 V134 H-6Z" fill="#4A90D9" {s()}/>
<circle cx="24" cy="62" r="13" fill="#fff" {s()}/>
<path d="M13 56 Q24 62 35 56 M13 68 Q24 62 35 68" fill="none" stroke="#E8483F" stroke-width="4"/>
<path d="M98 72 Q118 70 124 58" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>
<path d="M98 72 Q118 70 124 58" fill="none" stroke="#7A5234" stroke-width="3.4" stroke-linecap="round"/>
<path d="M40 74 Q42 50 70 50 Q98 50 104 72 Q96 84 70 84 Q48 84 40 74Z" fill="#9A6B45" {s()}/>
<circle cx="64" cy="48" r="7" fill="#9A6B45" {s(T2)}/><circle cx="64" cy="48" r="3" fill="#E9B9A0"/>
<circle cx="80" cy="50" r="6" fill="#9A6B45" {s(T2)}/>
{eye(54, 62, 1.15)}
<ellipse cx="40" cy="68" rx="4" ry="3" fill="#E8697D" {s(T2)}/>
<path d="M44 72 l-10 4 M45 75 l-8 8" stroke="{O}" stroke-width="1.6" stroke-linecap="round"/>
{BL.format(60, 72)}
<path d="M30 84 q-10 4 -18 0 M112 86 q8 4 16 0" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/>
{WV.format(50, 106, "#CFE5FB")}{WV.format(88, 112, "#CFE5FB")}
""", 60, 12)
SUBJ["swimrocket-beskudnikovo"] = ("бурая водяная полёвка с круглыми ушками, розовым носом и длинным хвостом",
                                   "плывёт по синей воде и толкает носом бело-красный мяч для водного поло, фон солнечно-жёлтый")

# 16. SwimRocket, «Крылатские холмы» — красноголовый нырок разбегается по воде, раскинув крылья
ICONS["swimrocket-krylatskie-kholmy"] = W("#D6F0FF", "#7EC8F2", f"""
<path d="M-6 98 Q30 86 58 94 Q90 70 134 78 V134 H-6Z" fill="#7BC47F" {s()}/>
<path d="M-6 100 Q30 92 64 100 T134 98 V134 H-6Z" fill="#2D7DD2" {s()}/>
<path d="M44 62 Q20 34 6 40 Q14 58 40 74Z M84 62 Q108 34 122 40 Q114 58 88 74Z" fill="#C9CED6" {s()}/>
<path d="M16 44 Q26 52 40 70 M112 44 Q102 52 88 70" fill="none" stroke="#8D95A3" stroke-width="3"/>
<ellipse cx="64" cy="74" rx="24" ry="17" fill="#DDE1E7" {s()}/>
<path d="M44 80 Q64 96 84 80 Q78 92 64 92 Q50 92 44 80Z" fill="#20242E"/>
<circle cx="64" cy="48" r="17" fill="#A8432A" {s()}/>
<path d="M56 54 Q64 66 72 54 Q64 58 56 54Z" fill="#3A3F4A" {s(T2)}/>
<circle cx="56" cy="46" r="4" fill="#E8483F"/><circle cx="72" cy="46" r="4" fill="#E8483F"/>
<circle cx="56" cy="46" r="1.8" fill="{O}"/><circle cx="72" cy="46" r="1.8" fill="{O}"/>
<path d="M40 100 q-6 -8 -14 -4 M88 100 q6 -8 14 -4" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
""", 50, 10)
SUBJ["swimrocket-krylatskie-kholmy"] = ("серая утка красноголовый нырок с каштаново-рыжей головой и красными глазами",
                                        "разбегается по синей воде навстречу зрителю, широко раскинув серые крылья, позади зелёные холмы, небо голубое")

# 17. SwimRocket, Международный центр самбо (Лужники) — кот-рыболов в красной самбовке
ICONS["swimrocket-luzhniki-sambo"] = W("#E8E4F8", "#9C8FD9", f"""
<path d="M-6 84 Q30 76 64 84 T134 82 V134 H-6Z" fill="#168AAD" {s()}/>
<path d="M34 88 Q30 60 64 60 Q98 60 94 88Z" fill="#E8483F" {s()}/>
<path d="M54 62 L64 80 L74 62" fill="none" stroke="#fff" stroke-width="4" stroke-linejoin="round"/>
<path d="M40 84 H88" stroke="#20242E" stroke-width="6"/>
<path d="M40 30 L36 12 L54 22Z M88 30 L92 12 L74 22Z" fill="#B8A07A" {s()}/>
<ellipse cx="64" cy="42" rx="27" ry="23" fill="#C8B28A" {s()}/>
<path d="M52 22 v10 M64 20 v12 M76 22 v10" stroke="#5B4630" stroke-width="3.4" stroke-linecap="round"/>
<path d="M40 44 h8 M80 44 h8" stroke="#5B4630" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="64" cy="52" rx="11" ry="8" fill="#fff"/>
{eye(53, 42, 1.15)}{eye(75, 42, 1.15)}
<path d="M61 49 h6 l-3 4Z" fill="#E8697D" {s(T2)}/>
<path d="M58 56 Q64 60 70 56" fill="none" {s(T2)}/>
<path d="M22 92 Q14 78 26 72 M106 92 Q114 78 102 72" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>
<path d="M22 92 Q14 78 26 72 M106 92 Q114 78 102 72" fill="none" stroke="#C8B28A" stroke-width="7" stroke-linecap="round"/>
{WV.format(30, 108, "#BFE9F5")}{WV.format(80, 112, "#BFE9F5")}
""", 50, 12)
SUBJ["swimrocket-luzhniki-sambo"] = ("песочно-серый кот-рыболов с тёмными полосками на лбу в красной самбистской куртке с чёрным поясом",
                                     "стоит по пояс в воде и гребёт обеими лапами по-собачьи, фон сиреневый")

# 18. SwimRocket, бассейн строительного университета — крохаль в строительной каске плывёт вдоль дорожек
ICONS["swimrocket-mgsu"] = W("#FFE2CF", "#FF9F6B", f"""
<rect x="-6" y="58" width="140" height="76" fill="#0B6E99" {s()}/>
<path d="M-6 76 H134 M-6 118 H134" stroke="#FFE08A" stroke-width="4" stroke-dasharray="3 9" stroke-linecap="round"/>
<path d="M36 96 Q40 74 68 74 Q98 74 112 90 Q102 106 70 106 Q44 106 36 96Z" fill="#E9EEF2" {s()}/>
<path d="M58 78 Q84 74 108 90 Q88 84 60 88Z" fill="#20242E"/>
<path d="M46 86 Q38 70 40 58" fill="none" stroke="{O}" stroke-width="14" stroke-linecap="round"/>
<path d="M46 86 Q38 70 40 58" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/>
<circle cx="40" cy="52" r="13" fill="#1F4D3A" {s()}/>
<path d="M50 48 l12 -6 M51 53 l13 0 M50 58 l10 6" stroke="#1F4D3A" stroke-width="3.4" stroke-linecap="round"/>
<path d="M28 54 L6 58 L28 60Z" fill="#E8483F" {s(T2)}/>
<circle cx="36" cy="51" r="3" fill="#E8483F"/><circle cx="36" cy="51" r="1.5" fill="{O}"/>
<path d="M24 44 H56 L52 36 Q40 24 30 36Z" fill="#FFD23F" {s(T2)}/>
<path d="M40 30 V40" stroke="{O}" stroke-width="2.4"/>
""", 60, 14)
SUBJ["swimrocket-mgsu"] = ("утка крохаль с тёмно-зелёной головой, лохматым хохолком на затылке и длинным красным клювом, в жёлтой строительной каске",
                           "плывёт влево по тёмно-голубой дорожке бассейна между двумя жёлтыми пунктирными разметками, фон оранжево-персиковый")

# 19. SwimRocket, бассейн университета спорта и туризма — ходулочник-турист на длинных красных ногах
ICONS["swimrocket-mgusit"] = W("#DFF3F0", "#79C7BD", f"""
<path d="M-6 100 Q30 92 64 100 T134 98 V134 H-6Z" fill="#1976D2" {s()}/>
<path d="M58 100 V62 M74 100 L70 62" stroke="#E8483F" stroke-width="4.4" stroke-linecap="round"/>
<path d="M40 54 Q44 38 66 38 Q90 38 100 52 Q90 64 66 64 Q46 64 40 54Z" fill="#fff" {s()}/>
<path d="M56 40 Q78 34 100 52 Q80 50 58 50Z" fill="#20242E" {s(T2)}/>
<rect x="66" y="34" width="20" height="22" rx="6" fill="#F28C28" {s(T2)}/><path d="M70 42 h12" stroke="{O}" stroke-width="2.2"/>
<path d="M46 46 Q40 34 42 26" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round"/>
<path d="M46 46 Q40 34 42 26" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
<circle cx="42" cy="22" r="10" fill="#fff" {s()}/>
<path d="M26 16 H58 L52 10 Q42 2 32 10Z" fill="#7BC47F" {s(T2)}/>
<path d="M33 24 L10 26" stroke="{O}" stroke-width="3" stroke-linecap="round"/>
<circle cx="39" cy="21" r="2" fill="{O}"/>
<path d="M50 100 q8 -6 16 0 M66 100 q8 -6 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
{WV.format(14, 114, "#BBDCFB")}{WV.format(96, 112, "#BBDCFB")}
""", 70, 20)
SUBJ["swimrocket-mgusit"] = ("белая птица ходулочник с чёрными крыльями на очень длинных красных ногах, в зелёной панаме и с оранжевым рюкзачком",
                             "стоит на своих ходулях посреди синего бассейна, как турист на привале, вода ему по щиколотку, фон мятно-бирюзовый")

# 20. SwimRocket, бассейн юридической академии — носач плывёт на спине
ICONS["swimrocket-mgyua"] = W("#FBE7C6", "#E8A04E", f"""
<path d="M-6 74 Q30 66 64 74 T134 72 V134 H-6Z" fill="#00897B" {s()}/>
<ellipse cx="80" cy="76" rx="32" ry="14" fill="#F3E6D0" {s()}/>
<path d="M104 70 l14 -12 M108 80 l14 6" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M104 70 l14 -12 M108 80 l14 6" stroke="#C98B5A" stroke-width="5" stroke-linecap="round"/>
<path d="M64 66 Q72 46 86 44" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>
<path d="M64 66 Q72 46 86 44" fill="none" stroke="#C98B5A" stroke-width="5" stroke-linecap="round"/>
<circle cx="40" cy="62" r="21" fill="#C4703C" {s()}/>
<ellipse cx="38" cy="66" rx="14" ry="13" fill="#F0B48C" {s(T2)}/>
<path d="M36 62 Q28 70 34 84 Q44 86 44 72Z" fill="#E89A78" {s(T2)}/>
<path d="M28 60 q4 -4 8 0 M42 58 q4 -4 8 0" fill="none" {s(T2)}/>
<path d="M44 78 Q50 80 52 74" fill="none" {s(T2)}/>
<path d="M8 84 q10 -8 20 0 M52 92 q10 -6 20 0" fill="none" stroke="#B9EDE6" stroke-width="3.4" stroke-linecap="round"/>
{WV.format(84, 108, "#B9EDE6")}{WV.format(30, 112, "#B9EDE6")}
""", 30, 15)
SUBJ["swimrocket-mgyua"] = ("рыжая обезьяна-носач с огромным висячим носом и светлым пузом",
                            "блаженно плывёт на спине по изумрудной воде, зажмурившись и закинув лапу за голову, фон тёплый охристый")

# 21. SwimRocket, бассейн «Северный» — корюшка в полосатом шарфе среди льдинок
ICONS["swimrocket-severny"] = W("#EAF4FF", "#B5CCF0", f"""
<path d="M-6 44 H134 V134 H-6Z" fill="#274C9E" {s()}/>
<path d="M8 44 l10 -12 h22 l8 12Z M82 44 l8 -10 h20 l10 10Z" fill="#fff" {s(T2)}/>
<path d="M92 78 L120 62 L112 82 L120 102Z" fill="#9FB8D8" {s()}/>
<path d="M14 82 Q36 60 70 66 Q92 70 98 82 Q88 96 64 98 Q34 98 14 82Z" fill="#DCE8F2" {s()}/>
<path d="M22 86 Q48 98 92 84 Q84 96 64 98 Q40 98 22 86Z" fill="#fff"/>
<path d="M30 74 Q54 62 84 72" fill="none" stroke="#7BC47F" stroke-width="5" stroke-linecap="round" opacity=".8"/>
<path d="M58 62 l8 -12 l6 14Z" fill="#9FB8D8" {s(T2)}/>
{eye(30, 80, 1.2)}
<path d="M16 88 q5 4 10 1" fill="none" {s(T2)}/>
<path d="M44 68 Q48 84 44 98" fill="none" stroke="#E8483F" stroke-width="8"/>
<path d="M44 74 h3 M45 84 h3 M44 92 h3" stroke="#fff" stroke-width="3"/>
<path d="M46 96 l10 12 l4 -8Z" fill="#E8483F" {s(T2)}/>
{bub(104, 112, 4)}{bub(12, 112, 3)}
""", 50, 10)
SUBJ["swimrocket-severny"] = ("серебристая северная рыбка корюшка с зеленоватой полоской по спинке, в красно-белом вязаном шарфе",
                              "плывёт под самой поверхностью тёмно-синей воды, на которой качаются две белые льдинки, небо бледно-голубое, зимнее")

# 22. SwimRocket, СК «Аквамарин» — узорчатая рыбка-мандаринка на аквамариновом фоне
ICONS["swimrocket-akvamarin"] = W("#B8F5EC", "#1FBFAE", f"""
<path d="M24 64 Q8 44 14 30 Q30 34 38 52Z M24 70 Q8 92 16 104 Q32 98 40 80Z" fill="#2B59C3" {s()}/>
<path d="M92 50 Q112 28 120 38 Q112 58 96 62Z M92 78 Q112 100 120 90 Q112 72 96 68Z" fill="#F28C28" {s()}/>
<ellipse cx="64" cy="66" rx="36" ry="27" fill="#2B59C3" {s()}/>
<path d="M40 52 Q50 44 58 54 Q66 64 78 56 Q88 50 94 60 M38 74 Q48 66 58 76 Q68 86 80 78 Q88 74 92 80" fill="none" stroke="#F28C28" stroke-width="5" stroke-linecap="round"/>
<path d="M48 88 Q58 82 68 90" fill="none" stroke="#7BE0A0" stroke-width="4" stroke-linecap="round"/>
<path d="M54 40 Q64 22 78 42Z" fill="#F28C28" {s(T2)}/>
<circle cx="40" cy="62" r="9" fill="#E8483F" {s(T2)}/>{eye(40, 62, 1.1)}
<path d="M28 74 q5 4 10 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(104, 18, 6)}{sparkle(20, 112, 5)}{bub(100, 108, 4)}
""", 50, 40)
SUBJ["swimrocket-akvamarin"] = ("синяя тропическая рыбка-мандаринка в оранжевых волнистых узорах, с красным глазом и синими плавниками-веерами",
                                "парит в самом центре круга, распушив все плавники, вокруг чистая аквамариновая вода и два блика")

# 23. SwimRocket, СК «Гармония» (большая чаша и детская 11 м) — рыба-наполеон и малёк плывут нос к носу
ICONS["swimrocket-garmoniya"] = W("#FDF0FF", "#D8A6E8", f"""
<path d="M-6 100 H134 V134 H-6Z" fill="#6A4C93" opacity=".25"/>
<path d="M92 56 L120 36 L114 60 L120 84Z" fill="#2E9E8F" {s()}/>
<path d="M30 60 Q34 28 66 30 Q94 32 98 58 Q94 86 64 88 Q36 88 30 60Z" fill="#3BB4A4" {s()}/>
<path d="M36 44 Q30 22 52 22 Q58 30 54 38Z" fill="#3BB4A4" {s()}/>
<path d="M60 44 q10 6 4 16 M74 42 q10 8 4 20 M56 68 q12 4 22 -4" fill="none" stroke="#1F6F66" stroke-width="3" stroke-linecap="round"/>
{eye(44, 52, 1.2)}
<path d="M30 66 Q38 76 50 70" fill="none" stroke="{O}" stroke-width="5" stroke-linecap="round"/>
<path d="M30 66 Q38 76 50 70" fill="none" stroke="#F7B2C4" stroke-width="2.4" stroke-linecap="round"/>
<g transform="translate(22,-2)">
<path d="M4 104 l-2 -8 l8 5 l-6 9Z" fill="#F28C28" {s(T2)}/>
<ellipse cx="18" cy="104" rx="11" ry="7.4" fill="#FFB347" {s(T2)}/>
<circle cx="23" cy="102.5" r="2.2" fill="{O}"/>
<path d="M28 96 Q32 90 36 92" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
</g>
{bub(108, 104, 4)}{bub(16, 34, 3.4)}{bub(10, 50, 2.4)}
""", 60, 20)
SUBJ["swimrocket-garmoniya"] = ("большая бирюзово-зелёная рыба-наполеон с шишкой на лбу и толстыми розовыми губами",
                                "добродушно смотрит вниз на крошечного оранжевого малька, который плывёт ей навстречу, — большая чаша и детская; фон сиреневый")

# 24. SwimRocket, бассейн «Стальной» — стальная рыба-сабля чехонь
ICONS["swimrocket-stalnoy"] = W("#2E3440", "#12151B", f"""
<path d="M-6 98 H134" stroke="#5E81AC" stroke-width="5" stroke-dasharray="10 8"/>
<path d="M10 40 Q50 26 96 40 Q112 46 118 58 Q100 96 60 100 Q30 96 10 40Z" fill="#C9D3DE" {s()}/>
<path d="M14 44 Q54 36 98 46 Q108 50 114 58" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
<path d="M34 84 Q62 94 96 74" fill="none" stroke="#8C9BAD" stroke-width="3" stroke-linecap="round"/>
<path d="M10 40 L-4 26 L2 48 L-6 62Z" fill="#8C9BAD" {s(T2)}/>
<path d="M70 96 Q76 112 90 106 Q88 96 80 92Z" fill="#8C9BAD" {s(T2)}/>
{eye(98, 56, 1.25)}
<path d="M108 68 q4 -2 6 -6" fill="none" {s(T2)}/>
{sparkle(40, 22, 7)}{sparkle(110, 26, 4)}{sparkle(22, 110, 5, "#88C0D0")}
""", 40, 20)
SUBJ["swimrocket-stalnoy"] = ("плоская серебристо-стальная рыба чехонь с прямой спиной и выгнутым, как сабля, брюхом",
                              "блестит как клинок в тёмной графитовой воде над синей пунктирной дорожкой, на спине и рядом вспыхивают блики")

# 25. SwimRocket, Дворец спорта «Янтарь» — жёлтая рыбка-лимон в капле янтаря
ICONS["swimrocket-yantar"] = W("#5B3A1A", "#2B1808", f"""
<path d="M64 8 Q112 52 106 84 Q98 118 64 120 Q30 118 22 84 Q16 52 64 8Z" fill="#FFB52E" {s()}/>
<path d="M64 20 Q98 56 94 84 Q88 106 64 108 Q40 106 34 84 Q30 56 64 20Z" fill="#FFD76A"/>
<path d="M44 44 Q36 60 38 76" fill="none" stroke="#FFF3C4" stroke-width="5" stroke-linecap="round"/>
<path d="M82 74 L100 62 L96 76 L100 90Z" fill="#F2B632" {s(T2)}/>
<ellipse cx="64" cy="76" rx="22" ry="14" fill="#FFF04D" {s()}/>
<path d="M54 64 Q64 54 76 64" fill="none" stroke="#20242E" stroke-width="4" stroke-linecap="round"/>
<path d="M58 88 q4 8 12 4" fill="none" stroke="#20242E" stroke-width="3.4" stroke-linecap="round"/>
{eye(52, 74, 1.1)}
<path d="M44 80 q4 3 8 0" fill="none" {s(T2)}/>
{bub(76, 44, 3.4)}{bub(70, 34, 2.2)}
""", 50, 30)
SUBJ["swimrocket-yantar"] = ("ярко-жёлтая рыбка-цихлида лабидохромис с чёрной каймой на спинном плавнике",
                             "плавает внутри огромной прозрачной капли янтаря, как в собственном аквариуме, фон тёмно-коричневый")

# 26. SwimRocket, ФОК «Южное Бутово» — фрегат с красным горлом, надутым как спасательный шар
ICONS["swimrocket-yuzhnoe-butovo"] = W("#FFF1B8", "#FFC94D", f"""
<path d="M-6 96 Q30 88 64 96 T134 94 V134 H-6Z" fill="#00A8CC" {s()}/>
<path d="M30 96 Q28 60 52 46 Q78 34 96 54 Q104 76 96 96Z" fill="#20242E" {s()}/>
<path d="M94 60 Q116 50 126 66 Q110 70 98 80Z" fill="#20242E" {s(T2)}/>
<circle cx="50" cy="78" r="24" fill="#E8483F" {s()}/>
<path d="M38 66 Q44 58 54 60" fill="none" stroke="#FF9C94" stroke-width="5" stroke-linecap="round"/>
<circle cx="58" cy="40" r="15" fill="#20242E" {s()}/>
<path d="M46 40 Q24 40 18 52 Q22 54 26 50 Q34 46 46 46Z" fill="#8C9BAD" {s(T2)}/>
<circle cx="54" cy="37" r="4.4" fill="#fff"/><circle cx="53" cy="37.6" r="2.2" fill="{O}"/>
{WV.format(8, 112, "#C5F2FB")}{WV.format(54, 116, "#C5F2FB")}{WV.format(98, 110, "#C5F2FB")}
""", 60, 12)
SUBJ["swimrocket-yuzhnoe-butovo"] = ("чёрная морская птица фрегат с длинным крючковатым клювом и огромным красным горловым мешком",
                                     "сидит на бирюзовой воде и держится на плаву на собственном надутом красном горле, как на спасательном шаре, фон южно-жёлтый")

# 27. SwimRocket, бассейн «Южнопортовый» — полосатая рыба-лоцман ведёт бумажный кораблик
ICONS["swimrocket-yuzhnoportovy"] = W("#DCEEFF", "#8FB8E8", f"""
<path d="M-6 54 Q30 46 64 54 T134 52 V134 H-6Z" fill="#0D5C8C" {s()}/>
<path d="M66 50 L78 18 L92 50Z" fill="#fff" {s()}/>
<path d="M54 50 H104 L94 62 H64Z" fill="#fff" {s()}/>
<path d="M78 18 V50" stroke="#B9C4D6" stroke-width="2.4"/>
<path d="M84 88 L110 72 L104 92 L110 112Z" fill="#20242E" {s()}/>
<path d="M12 92 Q30 70 58 72 Q80 74 88 92 Q80 108 56 110 Q28 110 12 92Z" fill="#DCE6F0" {s()}/>
<path d="M34 75 Q30 92 36 107 L46 110 Q40 92 44 73Z M54 72 Q50 92 56 110 L66 108 Q60 92 64 73Z M72 77 Q70 92 74 104 L82 98 Q80 90 80 82Z" fill="#20242E"/>
{eye(24, 88, 1.2)}
<path d="M12 96 q5 4 10 0" fill="none" {s(T2)}/>
<path d="M46 70 l8 -8 l6 10Z" fill="#20242E" {s(T2)}/>
{bub(100, 118, 3.4)}{bub(16, 118, 2.6)}
""", 30, 12)
SUBJ["swimrocket-yuzhnoportovy"] = ("серебристая рыба-лоцман в широких чёрных поперечных полосах",
                                    "плывёт под водой впереди белого бумажного кораблика и ведёт его в порт, вода тёмно-синяя, небо светло-голубое")

if __name__ == "__main__":
    ids = sys.argv[1:] or list(ICONS)
    reg = os.path.join(OUT, "subjects.txt")
    lines = open(reg, encoding="utf-8").read().rstrip("\n").split("\n")
    have = {l.split(" — ")[0] for l in lines if " — " in l}
    for pid in ids:
        open(os.path.join(OUT, pid + ".svg"), "w", encoding="utf-8").write(ICONS[pid])
        if pid not in have:
            lines.append(f"{pid} — герой: {SUBJ[pid][0]} | сцена: {SUBJ[pid][1]}")
    open(reg, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("svg:", len(ids))
