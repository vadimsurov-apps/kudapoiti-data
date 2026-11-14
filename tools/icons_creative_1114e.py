"""Иконки робота creative, 14.11 (запуск 1114e). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1114e.py [--subjects] [id…]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}


def girl(x, y, r, hair, k=0.55):
    """Голова девочки: кожа, волосы шапочкой только сверху, глазки и улыбка."""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SKIN}" {s()}/>'
            f'<path d="M{x-r} {y-1} A{r} {r} 0 0 1 {x+r} {y-1} Q{x} {y-r+5} {x-r} {y-1}Z" fill="{hair}" {s("stroke-width=\"2.2\"")}/>'
            f'{eye(x-4, y+3, k)}{eye(x+4, y+3, k)}<path d="M{x-3} {y+7} Q{x} {y+9.5} {x+3} {y+7}" fill="none" {s("stroke-width=\"1.6\"")}/>')

# Дети в Балете, Рассказовка (балет с 2 лет): кроха в лавандовой пачке встаёт на носочки, держась за плюшевого зайца
I["deti-v-balete-rasskazovka"] = ("кроха-балерина в лавандовой пачке с двумя пучками-шишечками на макушке",
    "впервые встаёт на носочки, держась обеими ручками за лапы плюшевого серого зайца-партнёра, на светлом полу у окна с соснами коттеджного посёлка",
    bg("#F8F0FC", "#9C36B5", f'''
<rect x="78" y="6" width="44" height="52" rx="4" fill="#D0EBFF" {s()}/>
<path d="M100 6 V58 M78 32 H122" {ln(O, 2.4)}/>
<path d="M88 30 L94 16 L100 30Z M106 54 L113 38 L120 54Z" fill="#2F9E44" {s('stroke-width="1.8"')}/>
<rect x="-4" y="106" width="136" height="26" fill="#F3D9FA" {s()}/>
<path d="M30 74 L28 104 M38 74 L40 104" {ln(O, 7)}/><path d="M30 74 L28 104 M38 74 L40 104" {ln("#FFF0F6", 4)}/>
<path d="M24 104 l6 0 l-2 4Z M38 104 l6 0 l-4 4Z" fill="#F783AC" {s('stroke-width="1.6"')}/>
<path d="M12 72 Q34 60 56 72 Q34 82 12 72Z" fill="#B197FC" {s()}/>
<path d="M16 72 Q34 66 52 72" fill="none" {ln("#E5DBFF", 2)}/>
<path d="M26 50 Q34 46 42 50 L42 70 H26Z" fill="#9775FA" {s()}/>
<path d="M40 56 L60 62" {ln(O, 7)}/><path d="M40 56 L60 62" {ln(SKIN, 4)}/>
{girl(34, 38, 11, "#7B4B2A", 0.55)}
<circle cx="26" cy="24" r="5" fill="#7B4B2A" {s('stroke-width="2"')}/><circle cx="42" cy="24" r="5" fill="#7B4B2A" {s('stroke-width="2"')}/>
<ellipse cx="80" cy="86" rx="16" ry="20" fill="#ADB5BD" {s()}/>
<ellipse cx="80" cy="90" rx="9" ry="12" fill="#E9ECEF" {s('stroke-width="1.6"')}/>
<circle cx="80" cy="58" r="13" fill="#ADB5BD" {s()}/>
<path d="M72 48 Q66 22 74 20 Q80 24 77 47Z M86 47 Q86 22 94 22 Q98 30 89 49Z" fill="#ADB5BD" {s()}/>
<path d="M73 44 Q70 30 74 25 M88 44 Q90 32 93 27" fill="none" {ln("#FFC9C9", 2.4)}/>
{face(80, 60, 8, 0.6)}
<path d="M66 70 L58 62" {ln(O, 7)}/><path d="M66 70 L58 62" {ln("#ADB5BD", 4)}/>
<ellipse cx="72" cy="106" rx="7" ry="4" fill="#ADB5BD" {s('stroke-width="2"')}/><ellipse cx="90" cy="106" rx="7" ry="4" fill="#ADB5BD" {s('stroke-width="2"')}/>
{sparkle(58, 22, 4, "#fff")}{sparkle(110, 86, 5, "#FCC2D7")}
'''))

# Дети в Балете, Октябрьское Поле: белоснежная пачка на плечиках кружится сама, под ней розовые пуанты
I["deti-v-balete-tukhachevskogo"] = ("белоснежная балетная пачка-тарелка с мордашкой на лифе",
    "висит на деревянных плечиках на латунном крючке гардероба и сама кружится, а под ней на коврике ждут крошечные розовые пуанты с завязанными лентами",
    bg("#FFF4E6", "#E8590C", f'''
<rect x="-4" y="-4" width="136" height="16" fill="#C2410C" {s()}/>
<path d="M64 12 V22 Q64 28 58 26" fill="none" {ln("#FCC419", 3.4)}/>
<path d="M40 34 Q64 22 88 34" fill="none" {ln("#A0673A", 5)}/>
<path d="M64 22 V30" {ln("#A0673A", 3)}/>
<path d="M48 34 Q64 30 80 34 L78 62 H50Z" fill="#fff" {s()}/>
<path d="M54 34 V30 M74 34 V30" {ln(O, 2.4)}/>
{face(64, 46, 8, 0.65)}
<ellipse cx="64" cy="68" rx="46" ry="12" fill="#fff" {s()}/>
<path d="M22 66 Q30 72 38 66 Q46 74 54 66 Q62 74 70 66 Q78 74 86 66 Q94 74 102 66" fill="none" {ln("#E9ECEF", 2.4)}/>
<ellipse cx="64" cy="64" rx="18" ry="4" fill="#FFF0F6"/>
<path d="M14 54 q-4 8 0 16 M114 54 q4 8 0 16" fill="none" {ln("#FFD8A8", 2.6)}/>
<rect x="-4" y="104" width="136" height="28" fill="#FFC078" {s()}/>
<ellipse cx="64" cy="108" rx="34" ry="5" fill="#E8590C" opacity=".35"/>
<path d="M44 106 Q42 92 50 92 Q56 94 56 106Z" fill="#FCC2D7" {s()}/>
<path d="M72 106 Q72 92 80 92 Q86 94 84 106Z" fill="#FCC2D7" {s()}/>
<path d="M50 96 Q60 88 64 98 Q68 88 78 96" fill="none" {ln("#F06595", 2.4)}/>
<path d="M58 98 q-6 6 -2 10 M70 98 q6 6 2 10" fill="none" {ln("#F06595", 2)}/>
{sparkle(24, 30, 5, "#fff")}{sparkle(106, 26, 4, "#FFE066")}{sparkle(110, 90, 4, "#fff")}
'''))

# Звёздная лига, Фили (бальные танцы с 3 лет): девочка в жёлтом латинском платье кружится, её ведёт за руку золотая звезда
I["zvezdnaya-liga-bagrationovsky"] = ("девочка-бальница с гладким пучком в ярко-жёлтом латинском платье с бахромой",
    "крутит быстрый поворот на тёмно-синем паркете, а её за руку лучиком ведёт большая золотая звезда-партнёр с улыбкой",
    bg("#E7F5FF", "#1C3D7A", f'''
<rect x="-4" y="104" width="136" height="28" fill="#364FC7" {s()}/>
<path d="M-4 112 H132 M20 104 L14 132 M60 104 L60 132 M100 104 L106 132" {ln("#4C6EF5", 2)}/>
<path d="M88 22 L95 38 L112 39 L99 50 L103 67 L88 58 L73 67 L77 50 L64 39 L81 38Z" fill="#FCC419" {s()}/>
{face(88, 46, 6, 0.55)}
<path d="M68 44 L58 46" {ln(O, 6)}/><path d="M68 44 L58 46" {ln("#FCC419", 3)}/>
<path d="M46 60 L58 46" {ln(O, 7)}/><path d="M46 60 L58 46" {ln(SKIN, 4)}/>
<path d="M34 56 Q30 70 34 80 Q42 84 50 80 Q52 68 46 56Z" fill="#FFD43B" {s()}/>
<path d="M28 78 Q22 90 18 92 M34 82 Q32 94 28 98 M42 84 L42 98 M50 82 Q54 94 58 96 M54 78 Q62 88 66 88" fill="none" {ln("#FAB005", 2.6)}/>
<path d="M38 84 L34 104 M46 84 L52 104" {ln(O, 7)}/><path d="M38 84 L34 104 M46 84 L52 104" {ln(SKIN, 4)}/>
<path d="M30 104 h8 M50 104 h8" {ln("#E8590C", 4)}/>
<path d="M36 60 L22 66" {ln(O, 7)}/><path d="M36 60 L22 66" {ln(SKIN, 4)}/>
{girl(39, 40, 10, "#6B3E26", 0.5)}
<circle cx="39" cy="27" r="5" fill="#6B3E26" {s('stroke-width="2"')}/>
<path d="M14 40 q4 -6 10 -4 M10 54 q6 -2 8 2" fill="none" {ln("#fff", 2.2)}/>
{sparkle(118, 80, 5, "#FFE066")}{sparkle(24, 18, 4, "#fff")}{sparkle(70, 88, 3, "#fff")}
'''))

# Хореографический коллектив «Колибри», Новозаводская: подготовишка с косичками кланяется у бордового занавеса с ромашками
I["kolibri-choreo-novozavodskaya"] = ("девочка-подготовишка с двумя рыжими косичками в голубом купальнике и белой шифоновой юбке",
    "выходит на поклон на край концертной сцены между бордовыми кулисами, держа сбоку букетик из трёх ромашек, а сверху светит круглый прожектор",
    bg("#FFF5F5", "#862E2E", f'''
<path d="M-4 -4 H24 Q18 60 26 132 H-4Z" fill="#A61E4D" {s()}/>
<path d="M132 -4 H104 Q110 60 102 132 H132Z" fill="#A61E4D" {s()}/>
<path d="M6 0 Q2 60 10 130 M118 0 Q122 60 114 130" fill="none" {ln("#C2255C", 3)}/>
<path d="M-4 -4 H132 V12 Q64 22 -4 12Z" fill="#C92A2A" {s()}/>
<path d="M44 12 L30 108 H98 L84 12Z" fill="#FFF3BF" opacity=".25"/>
<rect x="-4" y="108" width="136" height="24" fill="#8B5E3C" {s()}/>
<path d="M56 82 L54 108 M70 82 L74 108" {ln(O, 7)}/><path d="M56 82 L54 108 M70 82 L74 108" {ln(SKIN, 4)}/>
<path d="M44 80 Q62 70 84 80 Q64 92 44 80Z" fill="#F8F9FA" {s()}/>
<path d="M54 60 Q64 56 74 60 L74 80 H54Z" fill="#74C0FC" {s()}/>
<path d="M53 42 Q42 50 44 64" fill="none" {ln("#E8590C", 4)}/><path d="M75 42 Q86 50 84 64" fill="none" {ln("#E8590C", 4)}/>
<circle cx="44" cy="65" r="2.6" fill="#4DABF7"/><circle cx="84" cy="65" r="2.6" fill="#4DABF7"/>
{girl(64, 42, 11, "#E8590C", 0.55)}
<path d="M56 64 L66 72 L74 66" fill="none" {ln(O, 6)}/><path d="M56 64 L66 72 L74 66" fill="none" {ln(SKIN, 3)}/>
<path d="M74 68 L86 52 M75 68 L94 58 M75 69 L92 70" {ln("#2F9E44", 2.2)}/>
<circle cx="86" cy="50" r="5" fill="#fff" {s('stroke-width="1.6"')}/><circle cx="86" cy="50" r="2" fill="#FCC419"/>
<circle cx="95" cy="58" r="5" fill="#fff" {s('stroke-width="1.6"')}/><circle cx="95" cy="58" r="2" fill="#FCC419"/>
<circle cx="93" cy="70" r="5" fill="#fff" {s('stroke-width="1.6"')}/><circle cx="93" cy="70" r="2" fill="#FCC419"/>
{sparkle(40, 30, 4, "#fff")}{sparkle(90, 96, 4, "#FFE066")}
'''))

# «Студия звука», Отрадное (рок-бэнд с 7 лет, инструменты с 4): мальчишка с розовым ирокезом в прыжке играет на красном кейтаре
I["studiya-zvuka-otradnoe"] = ("мальчишка-рокер с торчащим розовым ирокезом и красным кейтаром (клавишной гитарой) на ремне",
    "в прыжке с поджатыми ногами жмёт на клавиши кейтара над сценой рок-клуба, снизу вверх бьют три цветных прожектора",
    bg("#343A40", "#121417", f'''
<path d="M22 132 L34 80 L46 132Z" fill="#F783AC" opacity=".35"/>
<path d="M54 132 L64 80 L74 132Z" fill="#74C0FC" opacity=".35"/>
<path d="M84 132 L96 80 L108 132Z" fill="#FFE066" opacity=".35"/>
<rect x="-4" y="112" width="136" height="20" fill="#495057" {s()}/>
<circle cx="34" cy="114" r="5" fill="#F783AC" {s('stroke-width="2"')}/><circle cx="64" cy="114" r="5" fill="#74C0FC" {s('stroke-width="2"')}/><circle cx="96" cy="114" r="5" fill="#FFE066" {s('stroke-width="2"')}/>
<path d="M54 74 Q46 84 52 94 L46 100 M70 74 Q80 82 74 92 L80 98" fill="none" {ln(O, 8)}/>
<path d="M54 74 Q46 84 52 94 L46 100 M70 74 Q80 82 74 92 L80 98" fill="none" {ln("#1C7ED6", 4.5)}/>
<path d="M40 100 h10 M76 98 h10" {ln(O, 5)}/>
<path d="M52 46 Q62 42 72 46 L74 76 H50Z" fill="#212529" {s()}/>
<path d="M56 52 L62 60 L68 52" fill="none" {ln("#fff", 2)}/>
<path d="M50 50 L72 76" {ln("#868E96", 2.4)}/>
<g transform="rotate(-22 64 68)">
<path d="M30 62 H92 Q100 62 100 70 Q100 78 92 78 H30Z" fill="#E03131" {s()}/>
<rect x="44" y="64" width="44" height="10" rx="1" fill="#fff" {s('stroke-width="1.8"')}/>
<path d="M50 64 V74 M56 64 V74 M62 64 V74 M68 64 V74 M74 64 V74 M80 64 V74" {ln(O, 1.4)}/>
<path d="M48 64 V70 M54 64 V70 M66 64 V70 M72 64 V70 M78 64 V70" {ln(O, 3)}/>
<rect x="14" y="66" width="18" height="8" rx="2" fill="#E03131" {s('stroke-width="2"')}/>
</g>
<path d="M52 52 Q44 60 48 70 M72 52 Q80 58 76 66" fill="none" {ln(O, 7)}/>
<path d="M52 52 Q44 60 48 70 M72 52 Q80 58 76 66" fill="none" {ln(SKIN, 4)}/>
<circle cx="62" cy="34" r="11" fill="{SKIN}" {s()}/>
<path d="M56 24 L54 8 L60 20 L62 4 L66 20 L72 8 L68 24Z" fill="#F06595" {s('stroke-width="2"')}/>
{eye(58, 36, 0.55)}{eye(66, 36, 0.55)}<path d="M58 41 Q62 45 66 41Z" fill="#C92A2A" {s('stroke-width="1.6"')}/>
{sparkle(20, 30, 5, "#FFE066")}{sparkle(106, 40, 4, "#F783AC")}{sparkle(100, 16, 3, "#74C0FC")}
'''))

# Хоровая школа «Весна», пр. Дежнёва («Игра в музыку» с 6 месяцев): кроха в голубой шапочке поёт на руках у мамы, ноты-листочки
I["vesna-ponomareva-dezhneva"] = ("кроха в голубой вязаной шапочке с белым помпоном и полосатой кофточке",
    "сидит на руках у мамы (видны только мамины руки в рукавах цвета мяты) и поёт круглым ротиком «А-а!», а изо рта вылетают три весенние ноты-листочки",
    bg("#EBFBEE", "#2B8A3E", f'''
<rect x="-4" y="106" width="136" height="26" fill="#8CE99A" {s()}/>
<path d="M20 106 q4 -10 8 0 M100 106 q4 -12 8 0 M112 106 q3 -8 6 0" fill="none" {ln("#2F9E44", 2.4)}/>
<path d="M30 86 Q54 104 84 92" fill="none" {ln(O, 15)}/><path d="M30 86 Q54 104 84 92" fill="none" {ln("#63E6BE", 10)}/>
<path d="M44 66 Q58 60 70 66 L74 92 H40Z" fill="#FFF" {s()}/>
<path d="M42 72 H72 M41 80 H73 M40 88 H74" {ln("#FF8787", 3)}/>
<ellipse cx="86" cy="92" rx="7" ry="6" fill="{SKIN}" {s('stroke-width="2.2"')}/>
<path d="M34 84 Q20 76 30 66" fill="none" {ln(O, 13)}/><path d="M34 84 Q20 76 30 66" fill="none" {ln("#63E6BE", 8)}/>
<ellipse cx="32" cy="64" rx="6" ry="5" fill="{SKIN}" {s('stroke-width="2.2"')}/>
<circle cx="57" cy="46" r="17" fill="{SKIN}" {s()}/>
<path d="M40 44 Q40 24 57 24 Q74 24 74 44 Q57 36 40 44Z" fill="#4DABF7" {s()}/>
<path d="M44 36 V42 M50 32 V39 M57 30 V37 M64 32 V39 M70 36 V42" {ln("#1C7ED6", 1.8)}/>
<circle cx="57" cy="20" r="6" fill="#fff" {s('stroke-width="2.2"')}/>
{eye(51, 47, 0.6)}{eye(63, 47, 0.6)}
<ellipse cx="45" cy="53" rx="3.5" ry="2" fill="#FF8FAB" opacity=".7"/><ellipse cx="69" cy="53" rx="3.5" ry="2" fill="#FF8FAB" opacity=".7"/>
<ellipse cx="57" cy="56" rx="3.2" ry="4" fill="#C92A2A" {s('stroke-width="1.8"')}/>
<path d="M80 40 Q90 30 100 34 Q92 42 80 40Z" fill="#69DB7C" {s('stroke-width="2"')}/><path d="M80 40 L80 26" {ln(O, 2)}/>
<path d="M92 24 Q102 14 112 18 Q104 26 92 24Z" fill="#8CE99A" {s('stroke-width="2"')}/><path d="M92 24 L92 10" {ln(O, 2)}/>
<path d="M98 56 Q108 48 116 52 Q110 60 98 56Z" fill="#51CF66" {s('stroke-width="2"')}/><path d="M98 56 L98 44" {ln(O, 2)}/>
{sparkle(22, 30, 5, "#fff")}{sparkle(110, 80, 4, "#FFE066")}
'''))

# a.dance, ул. Усиевича (хип-хоп, хаус, афро для 5–14 лет): кудрявый мальчишка в карго скользит в хаус-шаге у зеркала с неоновой полосой
I["adance-baku-usievicha"] = ("кудрявый мальчишка в широких хаки-штанах и оранжевом лонгсливе",
    "скользит в хаус-шаге — одна нога в сторону на пятке, руки врозь — по чёрному глянцевому полу студии, за ним вдоль стены тянется неоновая фиолетовая полоса",
    bg("#F3D9FA", "#5F3DC4", f'''
<rect x="-4" y="44" width="136" height="8" fill="#DA77F2" {s('stroke-width="2"')}/>
<rect x="-4" y="98" width="136" height="34" fill="#212529" {s()}/>
<path d="M12 104 H44 M70 110 H118" {ln("#495057", 2)}/>
<path d="M60 70 L52 96 L40 100" fill="none" {ln(O, 12)}/><path d="M60 70 L52 96 L40 100" fill="none" {ln("#868E3A", 8)}/>
<path d="M68 70 L84 92 L100 94" fill="none" {ln(O, 12)}/><path d="M68 70 L84 92 L100 94" fill="none" {ln("#868E3A", 8)}/>
<path d="M30 98 Q30 92 38 94 L44 100 H30Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M98 90 L110 88 Q114 96 106 98 L98 98Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M54 46 Q64 42 74 46 L72 72 H56Z" fill="#FD7E14" {s()}/>
<path d="M56 50 L34 40 M72 50 L96 58" {ln(O, 9)}/><path d="M56 50 L34 40 M72 50 L96 58" {ln("#FD7E14", 5.5)}/>
<circle cx="31" cy="39" r="4" fill="{SKIN}" {s('stroke-width="2"')}/><circle cx="99" cy="59" r="4" fill="{SKIN}" {s('stroke-width="2"')}/>
<circle cx="64" cy="32" r="11" fill="{SKIN}" {s()}/>
<circle cx="54" cy="24" r="6" fill="#5C3D2E" {s('stroke-width="2"')}/><circle cx="61" cy="19" r="6" fill="#5C3D2E" {s('stroke-width="2"')}/>
<circle cx="69" cy="19" r="6" fill="#5C3D2E" {s('stroke-width="2"')}/><circle cx="75" cy="25" r="5.5" fill="#5C3D2E" {s('stroke-width="2"')}/>
{eye(60, 34, 0.55)}{eye(68, 34, 0.55)}<path d="M60 39 Q64 42 68 39" fill="none" {s('stroke-width="1.6"')}/>
<path d="M20 96 l-8 0 M22 90 l-10 -4 M106 104 l10 2" {ln("#fff", 2)}/>
{sparkle(104, 22, 5, "#fff")}{sparkle(20, 70, 4, "#FFE066")}
'''))

# Балетная школа «Щелкунчик», Ленинский пр., 32: деревянный Щелкунчик ведёт за руку малышку-балерину у станка
I["schelkunchik-leninsky-32"] = ("деревянный Щелкунчик-солдатик в красном мундире, высоком чёрном кивере и с белой бородкой",
    "галантно держит за ручку малышку-балерину в белой пачке, которая стоит на одном пуанте у балетного станка, на светло-голубом фоне репетиционного зала",
    bg("#E7F5FF", "#4DABF7", f'''
<rect x="-4" y="104" width="136" height="28" fill="#D8A86E" {s()}/>
<path d="M-4 62 H132" {ln("#A0673A", 4)}/>
<path d="M10 62 V104 M118 62 V104" {ln("#A0673A", 3)}/>
<rect x="24" y="14" width="22" height="24" rx="3" fill="#212529" {s()}/>
<rect x="24" y="32" width="22" height="5" fill="#FCC419" {s('stroke-width="1.6"')}/>
<rect x="24" y="38" width="22" height="22" rx="4" fill="#FFD8A8" {s()}/>
{eye(30, 46, 0.5)}{eye(40, 46, 0.5)}
<path d="M26 52 Q35 72 44 52Z" fill="#fff" {s('stroke-width="2"')}/>
<rect x="30" y="52" width="10" height="5" fill="#fff" {s('stroke-width="1.6"')}/><path d="M33 52 V57 M37 52 V57" {ln(O, 1.2)}/>
<rect x="20" y="62" width="30" height="26" rx="4" fill="#E03131" {s()}/>
<path d="M35 62 V88" {ln("#FCC419", 2)}/><circle cx="35" cy="68" r="1.6" fill="#FCC419"/><circle cx="35" cy="76" r="1.6" fill="#FCC419"/>
<path d="M18 62 h8 M44 62 h8" {ln("#FCC419", 4)}/>
<rect x="24" y="88" width="9" height="16" fill="#1864AB" {s('stroke-width="2.2"')}/><rect x="37" y="88" width="9" height="16" fill="#1864AB" {s('stroke-width="2.2"')}/>
<path d="M22 104 h12 M36 104 h12" {ln(O, 4)}/>
<path d="M50 70 L66 62" {ln(O, 7)}/><path d="M50 70 L66 62" {ln("#E03131", 4)}/>
<path d="M88 76 L86 104" {ln(O, 7)}/><path d="M88 76 L86 104" {ln("#FFF0F6", 4)}/>
<path d="M90 76 L112 64" {ln(O, 7)}/><path d="M90 76 L112 64" {ln("#FFF0F6", 4)}/>
<path d="M84 104 l4 0 l-2 3Z" fill="#F783AC" {s('stroke-width="1.4"')}/>
<ellipse cx="88" cy="74" rx="20" ry="5" fill="#fff" {s()}/>
<path d="M82 52 Q88 50 94 52 L94 72 H82Z" fill="#fff" {s()}/>
<path d="M82 56 L68 62" {ln(O, 6)}/><path d="M82 56 L68 62" {ln(SKIN, 3.4)}/>
<path d="M94 56 L106 46" {ln(O, 6)}/><path d="M94 56 L106 46" {ln(SKIN, 3.4)}/>
{girl(88, 37, 10, "#E8B04B", 0.5)}
<circle cx="88" cy="24" r="4.5" fill="#E8B04B" {s('stroke-width="2"')}/>
{sparkle(70, 22, 5, "#fff")}{sparkle(112, 30, 4, "#FFE066")}{sparkle(60, 92, 3, "#fff")}
'''))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    ids = [a for a in sys.argv[1:] if not a.startswith("-")] or list(I)
    for k in ids:
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(I[k][2])
    print(len(ids))
