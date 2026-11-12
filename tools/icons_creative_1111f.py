"""Иконки робота creative, 11.11 (третий запуск). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1111f.py → icons-src/<id>.svg"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SKIN = "#FFD2B0"


def bg(a, b, body, cx="38%", cy="28%"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="{cx}" cy="{cy}" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


def ln(c, w):
    return f'stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'


def note(x, y, k=1.0, c=O):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{5*k:.1f}" ry="{4*k:.1f}" fill="{c}" transform="rotate(-20 {x} {y})"/>'
            f'<path d="M{x+4.5*k:.1f} {y-1*k:.1f} V{y-17*k:.1f} Q{x+10*k:.1f} {y-14*k:.1f} {x+11*k:.1f} {y-9*k:.1f}" fill="none" stroke="{c}" stroke-width="{2.4*k:.1f}" stroke-linecap="round"/>')


def limb(x1, y1, x2, y2, c, w=5):
    return f'<path d="M{x1} {y1} L{x2} {y2}" {ln(O, w + 3)}/><path d="M{x1} {y1} L{x2} {y2}" {ln(c, w)}/>'


I = {}

# Лэтс Дэнс — пара бальных туфель кружится в вальсе
I["letsdance-selskokhozyaystvennaya"] = ("чёрный лаковый мужской туфель и золотая девичья туфелька с ремешком",
    "кружатся парой в вальсе на паркете в круге света", bg("#FFF1E0", "#E39A5A", f'''
<path d="M0 98 H128 V128 H0Z" fill="#B87440"/><path d="M0 98 H128 M20 98 L10 128 M50 98 L46 128 M80 98 L84 128 M110 98 L118 128" {s('stroke-width="2"')}/>
<ellipse cx="64" cy="100" rx="50" ry="9" fill="#FFE9A8" opacity=".75"/>
<path d="M22 80 Q24 64 40 66 L56 70 Q66 72 66 82 L66 90 L22 90Z" fill="#26222F" {s()}/>
<path d="M22 90 H68" {ln(O, 4)}/><path d="M30 70 Q36 66 44 68" stroke="#fff" stroke-width="2.4" fill="none" opacity=".7"/>
{eye(38, 78, 0.7)}{eye(52, 78, 0.7)}<path d="M41 84 Q45 87 49 84" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
<path d="M70 62 Q74 50 90 52 Q104 54 106 70 L108 88 L104 88 L100 74 Q92 82 76 82 Q68 80 70 62Z" fill="#F5C23A" {s()}/>
<path d="M78 60 Q88 54 98 60" fill="none" {ln(O, 3)}/>
{eye(82, 68, 0.6)}{eye(92, 68, 0.6)}<path d="M84 74 Q87 77 90 74" fill="none" {s('stroke-width="1.8"')}/>
<path d="M30 40 q8 -10 16 0 M84 34 q8 -10 16 0" fill="none" {ln("#fff", 3)}/>
{sparkle(64, 26, 6)}{sparkle(22, 52, 3.5)}{sparkle(112, 44, 4)}
'''))

# Jump — девочка-хипхоперша в жёлтом худи в прыжке
I["jump-lazorevy"] = ("девочка-хипхоперша в жёлтом худи и огромных наушниках",
    "прыгает выше головы, поджав ноги, над паркетом танцзала", bg("#E6F0FF", "#5B7FE0", f'''
<rect x="0" y="108" width="128" height="20" fill="#C98E52"/><path d="M0 108 H128" {s('stroke-width="2.4"')}/>
<ellipse cx="64" cy="114" rx="22" ry="4" fill="#000" opacity=".2"/>
{limb(56, 74, 40, 84, "#3D5BA8", 6)}{limb(40, 84, 52, 92, "#3D5BA8", 6)}
{limb(72, 74, 88, 84, "#3D5BA8", 6)}{limb(88, 84, 76, 92, "#3D5BA8", 6)}
<rect x="44" y="88" width="12" height="7" rx="3" fill="#fff" {s('stroke-width="2"')}/><rect x="72" y="88" width="12" height="7" rx="3" fill="#fff" {s('stroke-width="2"')}/>
<path d="M48 48 Q64 42 80 48 L82 76 H46Z" fill="#FFCF2E" {s()}/>
<path d="M58 62 H70 V70 H58Z" fill="#F2B21A" {s('stroke-width="2"')}/>
{limb(48, 52, 28, 30, "#FFCF2E", 7)}{limb(80, 52, 100, 30, "#FFCF2E", 7)}
<circle cx="26" cy="27" r="5" fill="{SKIN}" {s('stroke-width="2.4"')}/><circle cx="102" cy="27" r="5" fill="{SKIN}" {s('stroke-width="2.4"')}/>
<circle cx="64" cy="34" r="13" fill="{SKIN}" {s()}/>
<path d="M51 32 Q52 18 64 18 Q76 18 77 32 Q70 26 64 26 Q58 26 51 32Z" fill="#3A2418" {s('stroke-width="2.4"')}/>
<path d="M48 34 Q48 14 64 14 Q80 14 80 34" fill="none" {ln(O, 6)}/><path d="M48 34 Q48 14 64 14 Q80 14 80 34" fill="none" {ln("#E8344A", 3)}/>
<rect x="43" y="28" width="9" height="14" rx="4" fill="#E8344A" {s('stroke-width="2.4"')}/><rect x="76" y="28" width="9" height="14" rx="4" fill="#E8344A" {s('stroke-width="2.4"')}/>
{eye(59, 35, 0.55)}{eye(69, 35, 0.55)}<path d="M60 40 Q64 44 68 40" fill="none" {s('stroke-width="1.8"')}/>
<path d="M18 96 l-6 4 M110 96 l6 4 M24 104 l-8 0 M104 104 l8 0" {ln("#fff", 3)}/>
'''))

# Лав Дэнс — сердечко в кепке танцует хип-хоп у граффити-стены
I["love-dance-rudneva"] = ("красное сердечко на ножках в бейсболке козырьком назад",
    "танцует хип-хоп, вскинув руку, на фоне стены с граффити", bg("#F0E6FF", "#8E6BD6", f'''
<rect x="0" y="0" width="128" height="96" fill="#B9A4E8" opacity=".55"/>
<path d="M0 30 H128 M0 62 H128 M30 0 V30 M80 0 V30 M54 30 V62 M104 30 V62 M20 62 V96 M76 62 V96" stroke="#9C86D6" stroke-width="2"/>
<path d="M8 50 q10 -16 20 0 t20 0" fill="none" {ln("#3FD0B0", 5)}/><path d="M92 82 q8 -12 16 0" fill="none" {ln("#FFD23A", 5)}/>
<rect x="0" y="96" width="128" height="32" fill="#6E5BA8"/>
{limb(54, 92, 46, 112, "#E8344A", 5)}{limb(74, 92, 84, 110, "#E8344A", 5)}
<ellipse cx="44" cy="114" rx="8" ry="4" fill="#fff" {s('stroke-width="2.2"')}/><ellipse cx="86" cy="112" rx="8" ry="4" fill="#fff" {s('stroke-width="2.2"')}/>
<path d="M64 98 L30 64 Q18 48 32 36 Q48 26 64 44 Q80 26 96 36 Q110 48 98 64Z" fill="#E8344A" {s()}/>
{limb(98, 56, 112, 30, "#E8344A", 5)}<circle cx="113" cy="26" r="5" fill="#fff" {s('stroke-width="2.2"')}/>
{limb(32, 62, 22, 76, "#E8344A", 5)}
<path d="M40 40 Q58 22 82 32 L82 38 Q60 32 42 46Z" fill="#2E9BE8" {s()}/><path d="M42 44 Q30 46 24 52 L40 50Z" fill="#1F78C0" {s('stroke-width="2.4"')}/>
{face(64, 58, d=10, k=0.9)}
'''))

# Starzzz (Бутово) — звезда-рокер с электрогитарой
I["starzzz-yuzhnobutovskaya"] = ("фиолетовая звезда-рокер с жёлтой электрогитарой наперевес",
    "играет соло на краю маленькой сцены рядом с колонкой", bg("#2C2140", "#120C22", f'''
<path d="M40 0 L20 110 M88 0 L108 110" stroke="#FFF3B0" stroke-width="22" opacity=".12"/>
<rect x="0" y="106" width="128" height="22" fill="#5A3A2A"/><path d="M0 106 H128" {s()}/>
<rect x="94" y="70" width="28" height="36" rx="4" fill="#3A3A44" {s()}/><circle cx="108" cy="82" r="6" fill="#222" {s('stroke-width="2"')}/><circle cx="108" cy="97" r="5" fill="#222" {s('stroke-width="2"')}/>
<path d="M58 14 L68 36 L92 38 L74 54 L80 78 L58 66 L36 78 L42 54 L24 38 L48 36Z" fill="#9C5BE8" {s()}/>
<path d="M42 78 L36 104 M74 78 L80 104" {ln(O, 5)}/>
<path d="M30 102 h12 M74 102 h12" {ln(O, 6)}/>
{face(58, 46, d=8, k=0.8)}
<path d="M18 92 L66 58" {ln(O, 7)}/><path d="M18 92 L66 58" {ln("#C98E52", 4)}/>
<rect x="62" y="50" width="12" height="8" rx="2" fill="#2F2B3A" transform="rotate(-35 68 54)" {s('stroke-width="2"')}/>
<path d="M14 80 Q4 92 12 102 Q20 110 30 100 Q40 96 34 86 Q30 78 22 82Z" fill="#FFD23A" {s()}/>
<circle cx="22" cy="92" r="3" fill="{O}"/>
{note(100, 30, 0.7, "#FFD23A")}{note(14, 40, 0.55, "#7FE0FF")}{sparkle(110, 52, 4)}
'''))

# Starzzz (ЗИЛ) — бочка барабанной установки
I["starzzz-shchuseva"] = ("красная бочка барабанной установки с мордашкой и тарелкой-шляпой набекрень",
    "две барабанные палочки сами отстукивают по ней ритм, разлетаются звёздочки", bg("#E0FFF4", "#3FB89A", f'''
<rect x="0" y="108" width="128" height="20" fill="#2F7A68"/>
<path d="M30 112 L40 92 M98 112 L88 92" {ln(O, 4)}/>
<ellipse cx="64" cy="76" rx="38" ry="38" fill="#E8344A" {s()}/>
<ellipse cx="64" cy="76" rx="30" ry="30" fill="#FFF3E6" {s()}/>
<path d="M28 60 L100 60 M28 92 L100 92" stroke="#C9C9D2" stroke-width="3" opacity=".9"/>
{face(64, 74, d=10, k=1.0)}
<path d="M34 34 L82 22" {ln(O, 3)}/><ellipse cx="60" cy="28" rx="30" ry="6" fill="#F2C23A" transform="rotate(-12 60 28)" {s()}/>
<path d="M60 22 V40" {ln(O, 3)}/>
<path d="M100 20 L84 46" {ln(O, 7)}/><path d="M100 20 L84 46" {ln("#E8C08A", 4)}/>
<path d="M116 42 L96 56" {ln(O, 7)}/><path d="M116 42 L96 56" {ln("#E8C08A", 4)}/>
{sparkle(20, 40, 6, "#FFE07A")}{sparkle(110, 72, 5)}{sparkle(14, 74, 4)}
'''))

# Рыжий кит — кит-художник брызжет красками на холст
I["ryzhiy-kit-lazareva"] = ("рыжий кит-художник с кисточкой в плавнике",
    "выпускает из дыхала фонтан разноцветных брызг-красок на холст на мольберте", bg("#E2F6FF", "#5AA8D8", f'''
<path d="M0 100 Q32 92 64 100 T128 100 V128 H0Z" fill="#3A86C0" {s('stroke-width="2.4"')}/>
<path d="M88 34 L100 106 M118 34 L106 106 M92 60 H116" {ln(O, 3)}/>
<rect x="84" y="20" width="36" height="34" rx="2" fill="#fff" {s()}/>
<circle cx="94" cy="32" r="4" fill="#E8344A"/><circle cx="106" cy="40" r="5" fill="#3FB86A"/><circle cx="110" cy="28" r="3" fill="#FFD23A"/><circle cx="98" cy="46" r="3" fill="#7A5BE8"/>
<path d="M8 84 Q10 58 40 56 Q70 56 76 78 Q78 96 52 100 L20 100 Q8 98 8 84Z" fill="#F2843A" {s()}/>
<path d="M14 92 Q40 98 70 88" fill="#FFC79A" opacity=".8"/>
<path d="M74 78 Q86 70 84 60 Q78 66 72 70" fill="#F2843A" {s()}/>
{eye(30, 76, 0.8)}<path d="M22 86 Q30 92 38 86" fill="none" {s('stroke-width="2.4"')}/>
<ellipse cx="22" cy="84" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
<path d="M42 54 Q44 36 56 30" fill="none" {ln("#E8344A", 4)}/><path d="M46 54 Q56 34 74 30" fill="none" {ln("#FFD23A", 4)}/><path d="M38 54 Q32 38 40 26" fill="none" {ln("#3FB86A", 4)}/>
<circle cx="58" cy="28" r="3.5" fill="#E8344A"/><circle cx="78" cy="30" r="3.5" fill="#FFD23A"/><circle cx="40" cy="22" r="3.5" fill="#3FB86A"/>
<path d="M50 90 L66 74" {ln(O, 5)}/><path d="M50 90 L66 74" {ln("#C98E52", 2.6)}/><path d="M66 74 l4 -5" {ln("#7A5BE8", 5)}/>
'''))

# Звёздная Лига — мальчик-бальник ведёт партнёршу
I["zvezdnaya-liga-starokachalovskaya"] = ("мальчик-бальник в чёрном жилете и бабочке",
    "ведёт по паркету партнёршу в розовом платье, над ними висит золотая звезда", bg("#FFF7DA", "#E8B83A", f'''
<rect x="0" y="108" width="128" height="20" fill="#A8683A"/>
<path d="M64 6 L69 18 L82 19 L72 27 L75 40 L64 33 L53 40 L56 27 L46 19 L59 18Z" fill="#FFD23A" {s('stroke-width="2.6"')}/>
{limb(44, 82, 38, 108, "#26222F", 6)}{limb(50, 82, 56, 108, "#26222F", 6)}
<path d="M36 52 Q46 46 56 52 L56 84 H36Z" fill="#fff" {s()}/><path d="M38 54 L46 84 L54 54 L56 84 H36Z" fill="#26222F" {s('stroke-width="2.4"')}/>
<path d="M42 52 L50 52 L46 56Z" fill="#E8344A" {s('stroke-width="1.8"')}/>
<circle cx="46" cy="40" r="11" fill="{SKIN}" {s()}/><path d="M35 38 Q36 26 46 26 Q58 26 57 38 Q52 32 44 33Z" fill="#3A2418" {s('stroke-width="2.2"')}/>
{eye(42, 41, 0.5)}{eye(51, 41, 0.5)}<path d="M43 46 Q46.5 49 50 46" fill="none" {s('stroke-width="1.6"')}/>
<path d="M66 56 Q76 50 86 56 L100 108 H52Z" fill="#FF8FB8" {s()}/><path d="M58 96 Q76 104 96 96" fill="none" stroke="#fff" stroke-width="2.4"/>
<circle cx="80" cy="44" r="10" fill="{SKIN}" {s()}/><path d="M70 42 Q72 30 80 30 Q90 30 90 42 Q86 36 80 36Z" fill="#F2C23A" {s('stroke-width="2.2"')}/><circle cx="90" cy="34" r="5" fill="#F2C23A" {s('stroke-width="2.2"')}/>
{eye(77, 45, 0.48)}{eye(85, 45, 0.48)}
{limb(56, 58, 70, 62, "#26222F", 4)}{limb(66, 60, 30, 60, "#FF8FB8", 4)}
{sparkle(22, 28, 4)}{sparkle(106, 26, 4)}
'''))

# Be YourSelf — маска-смайлик рисует автопортрет
I["be-yourself-selskokhozyaystvennaya"] = ("белая театральная маска-смайлик с кисточкой за ухом",
    "рисует на мольберте свой собственный портрет", bg("#FFEFF4", "#E86A8E", f'''
<path d="M78 40 L70 118 M112 40 L118 118 M84 96 H114" {ln(O, 3.4)}/>
<rect x="74" y="26" width="44" height="54" rx="3" fill="#FFFDF4" {s()}/>
<path d="M82 46 Q96 30 110 46 Q110 70 96 72 Q82 70 82 46Z" fill="none" {ln("#7A5BE8", 3)}/>
<circle cx="90" cy="50" r="2" fill="#7A5BE8"/><circle cx="102" cy="50" r="2" fill="#7A5BE8"/><path d="M90 60 Q96 66 102 60" fill="none" {ln("#E8344A", 2.6)}/>
<path d="M10 54 Q12 22 38 20 Q64 22 66 54 Q64 92 38 96 Q12 92 10 54Z" fill="#fff" {s()}/>
<path d="M22 46 Q28 40 34 46 M42 46 Q48 40 54 46" fill="none" {ln(O, 3)}/>
<path d="M24 64 Q38 80 52 64 Q38 72 24 64Z" fill="#E8344A" {s('stroke-width="2.6"')}/>
<ellipse cx="18" cy="58" rx="4.5" ry="3" fill="#FF7FA8" opacity=".6"/><ellipse cx="58" cy="58" rx="4.5" ry="3" fill="#FF7FA8" opacity=".6"/>
<path d="M58 20 L70 10" {ln(O, 5.5)}/><path d="M58 20 L70 10" {ln("#3FB86A", 3)}/><path d="M70 10 l5 -4" {ln("#E8344A", 5)}/>
<path d="M60 84 L80 66" {ln(O, 5)}/><path d="M60 84 L80 66" {ln("#F2C23A", 2.6)}/><path d="M80 66 l3 -3" {ln("#7A5BE8", 4.5)}/>
{sparkle(30, 110, 4)}{sparkle(50, 112, 3)}
'''))

# Рисуем с нами — фломастер-великан рисует улитку-спираль
I["risuem-s-nami-rokossovskogo"] = ("бирюзовый фломастер-великан в колпачке-беретике",
    "рисует на большом листе на полу разноцветную улитку-спираль", bg("#F7FFE4", "#9ACD3A", f'''
<path d="M6 70 L90 58 L122 112 L20 124Z" fill="#fff" {s()}/>
<path d="M58 96 m-14 0 a14 12 0 1 1 28 0 a10 8 0 1 1 -20 0 a5 4 0 1 1 10 0" fill="none" {ln("#E8344A", 3.4)}/>
<path d="M44 96 Q40 108 30 106 L76 106" fill="none" {ln("#3FB86A", 3.4)}/>
<path d="M64 84 l-2 -8 M70 86 l4 -8" {ln(O, 2.4)}/>
<g transform="rotate(32 84 52)">
<rect x="72" y="8" width="24" height="70" rx="8" fill="#2EC4C4" {s()}/>
<path d="M72 78 L96 78 L88 96 L80 96Z" fill="#E8F8F8" {s()}/><path d="M80 96 L84 104 L88 96Z" fill="#1E9A9A" {s('stroke-width="2.4"')}/>
<rect x="70" y="4" width="28" height="20" rx="9" fill="#1E9A9A" {s()}/>
{face(84, 46, d=6, k=0.75)}
</g>
{sparkle(22, 40, 5, "#FFE07A")}{sparkle(112, 24, 4)}
'''))

# Театр-студия им. Станиславского — мальчик-рыцарь с картонным мечом
I["ts-stanislavskogo-rudneva"] = ("мальчик-рыцарь в картонных доспехах и шлеме из кастрюли",
    "репетирует поединок с бутафорским мечом на сцене перед бархатным занавесом", bg("#FFE6E6", "#C8323E", f'''
<path d="M0 0 H128 V100 H0Z" fill="#9E1E2E" opacity=".55"/>
<path d="M0 0 Q12 50 2 100 M128 0 Q116 50 126 100" fill="#7A1422" {s()}/>
<path d="M0 0 H128 V14 Q96 24 64 14 Q32 24 0 14Z" fill="#E8B83A" {s()}/>
<rect x="0" y="100" width="128" height="28" fill="#8A5A34"/><path d="M0 100 H128" {s()}/>
{limb(56, 84, 50, 104, "#5A6AA8", 6)}{limb(70, 84, 78, 104, "#5A6AA8", 6)}
<path d="M48 56 H80 L78 88 H50Z" fill="#C9C9D2" {s()}/><path d="M64 58 V86 M52 70 H76" {ln("#9A9AA8", 2.4)}/>
<circle cx="64" cy="44" r="12" fill="{SKIN}" {s()}/>
<path d="M50 40 Q50 26 64 26 Q78 26 78 40Z" fill="#A9B0BE" {s()}/><path d="M48 40 H80" {ln(O, 4)}/><rect x="76" y="34" width="10" height="4" rx="2" fill="#2F2B3A" {s('stroke-width="1.8"')}/>
{eye(60, 46, 0.55)}{eye(69, 46, 0.55)}<path d="M60 52 Q64 55 68 52" fill="none" {s('stroke-width="1.8"')}/>
{limb(80, 62, 94, 52, "#C9C9D2", 5)}
<path d="M96 50 L118 16" {ln(O, 9)}/><path d="M96 50 L118 16" {ln("#E8D6A8", 5.5)}/><path d="M90 46 L102 56" {ln(O, 5)}/>
{limb(48, 62, 34, 70, "#C9C9D2", 5)}
<ellipse cx="30" cy="74" rx="12" ry="15" fill="#3A6ED8" {s()}/><path d="M30 62 V86 M20 74 H40" {ln("#FFD23A", 3)}/>
'''))

# Sdt — девочка в прыжке-шпагате на фоне телебашни
I["sdt-korolyova"] = ("девочка-танцовщица в оранжевом комбинезоне",
    "застыла в прыжке-шпагате высоко над полом на фоне серебристой телебашни", bg("#E8F4FF", "#7FA8E8", f'''
<path d="M100 128 L104 30 L106 8 L108 30 L112 128Z" fill="#DDE2EE" {s('stroke-width="2.4"')}/>
<rect x="100" y="54" width="12" height="7" rx="2" fill="#B9C0D2" {s('stroke-width="2"')}/>
<rect x="0" y="112" width="128" height="16" fill="#5A6AA8"/>
<ellipse cx="54" cy="116" rx="26" ry="3.5" fill="#000" opacity=".2"/>
{limb(52, 74, 18, 72, "#F2843A", 6)}{limb(58, 74, 92, 80, "#F2843A", 6)}
<ellipse cx="15" cy="72" rx="5" ry="3.5" fill="{SKIN}" {s('stroke-width="2.2"')}/><ellipse cx="95" cy="81" rx="5" ry="3.5" fill="{SKIN}" {s('stroke-width="2.2"')}/>
<path d="M46 46 Q56 40 66 46 L64 76 H48Z" fill="#F2843A" {s()}/>
{limb(48, 50, 30, 32, "#F2843A", 5)}{limb(64, 50, 82, 30, "#F2843A", 5)}
<circle cx="29" cy="29" r="4.2" fill="{SKIN}" {s('stroke-width="2.2"')}/><circle cx="83" cy="27" r="4.2" fill="{SKIN}" {s('stroke-width="2.2"')}/>
<circle cx="56" cy="32" r="11" fill="{SKIN}" {s()}/>
<path d="M45 30 Q46 18 56 18 Q67 18 67 30 Q62 24 56 24 Q50 24 45 30Z" fill="#2A1A14" {s('stroke-width="2.2"')}/><circle cx="56" cy="14" r="5" fill="#2A1A14" {s('stroke-width="2.2"')}/>
{eye(52, 33, 0.5)}{eye(60, 33, 0.5)}<path d="M53 38 Q56 41 59 38" fill="none" {s('stroke-width="1.6"')}/>
<path d="M20 92 q6 -6 12 0 M40 98 q6 -6 12 0" fill="none" {ln("#fff", 2.6)}/>
'''))

# First Street Ballet — пуанта в бейсболке на скейтборде
I["first-street-ballet-svobody"] = ("розовая атласная пуанта в синей бейсболке",
    "встала на носок на скейтборде и катится по асфальту", bg("#FFF0FA", "#F27AB8", f'''
<rect x="0" y="104" width="128" height="24" fill="#6E6E7A"/><path d="M10 116 H30 M56 116 H76 M100 116 H120" stroke="#fff" stroke-width="2.6"/>
<rect x="22" y="88" width="84" height="8" rx="4" fill="#3FB86A" {s()}/>
<circle cx="36" cy="102" r="6" fill="#FFD23A" {s()}/><circle cx="92" cy="102" r="6" fill="#FFD23A" {s()}/>
<path d="M54 88 Q50 60 58 44 Q66 30 80 36 Q88 42 82 60 Q76 74 74 88Z" fill="#FFB0D0" {s()}/>
<path d="M54 88 H74 Q74 80 64 80 Q56 80 54 88Z" fill="#F27AB8" {s('stroke-width="2.4"')}/>
<path d="M62 46 Q40 30 30 52 M76 44 Q100 30 108 56" fill="none" {ln("#FFB0D0", 3)}/>
<path d="M58 40 Q60 22 76 24 Q86 26 86 38 Q72 34 58 40Z" fill="#2E6AD8" {s()}/><path d="M84 36 Q96 36 100 42 L84 40Z" fill="#1E4AA8" {s('stroke-width="2.4"')}/>
{eye(66, 54, 0.6)}{eye(76, 54, 0.6)}<path d="M67 61 Q71 64 75 61" fill="none" {s('stroke-width="1.8"')}/>
<path d="M10 70 h12 M6 80 h14 M14 60 h8" {ln("#fff", 3)}/>
'''))

# Будь собой — белое пианино поёт с девочкой
I["bud-soboy-korolyova"] = ("белое детское пианино с открытой крышкой-ртом",
    "поёт песенку вместе с девочкой, которая играет на нём", bg("#E4FFF0", "#5ACB8E", f'''
<rect x="0" y="110" width="128" height="18" fill="#2F8A5A"/>
<rect x="16" y="40" width="70" height="66" rx="6" fill="#FAFAFA" {s()}/>
<path d="M16 46 Q51 30 86 46" fill="#E9E9EE" {s()}/>
<rect x="16" y="72" width="70" height="14" fill="#fff" {s('stroke-width="2.4"')}/>
<path d="M26 72 V80 M34 72 V80 M46 72 V80 M54 72 V80 M62 72 V80 M74 72 V80" {ln(O, 3.2)}/>
<path d="M22 106 V114 M80 106 V114" {ln(O, 4)}/>
{eye(40, 56, 0.7)}{eye(62, 56, 0.7)}<ellipse cx="51" cy="64" rx="5" ry="4" fill="#E8546A" {s('stroke-width="2"')}/>
<path d="M88 110 L90 80 Q96 72 104 80 L108 110Z" fill="#7A5BE8" {s()}/>
<circle cx="98" cy="64" r="11" fill="{SKIN}" {s()}/><path d="M87 62 Q88 50 98 50 Q109 50 109 62 Q108 74 112 80 Q100 70 98 58 Q94 68 86 72Z" fill="#B85A2A" {s('stroke-width="2.2"')}/>
{eye(95, 65, 0.48)}<ellipse cx="99" cy="70" rx="2.4" ry="2" fill="#B2283C"/>
{limb(90, 84, 80, 74, "#7A5BE8", 4)}
{note(30, 22, 0.7, "#fff")}{note(70, 18, 0.6, "#FFD23A")}{note(112, 34, 0.55, "#fff")}
'''))

# ДМШ № 66 — виолончель в бабочке кланяется
I["dmsh-66-goncharova"] = ("виолончель в красной бабочке",
    "кланяется со смычком в руке после концерта, а вокруг летят цветы", bg("#FFF3E2", "#D98A4A", f'''
<rect x="0" y="108" width="128" height="20" fill="#7A3A2A"/><path d="M0 108 H128" {s()}/>
<g transform="rotate(-14 64 80)">
<path d="M64 108 V118" {ln(O, 4)}/>
<path d="M50 42 Q38 46 40 60 Q42 68 36 74 Q30 86 40 100 Q52 110 64 110 Q76 110 88 100 Q98 86 92 74 Q86 68 88 60 Q90 46 78 42 Q64 38 50 42Z" fill="#B8642E" {s()}/>
<path d="M56 74 q-4 6 0 12 M72 74 q4 6 0 12" fill="none" {ln(O, 2.4)}/>
<rect x="60" y="6" width="8" height="40" rx="3" fill="#3A2418" {s('stroke-width="2.4"')}/><path d="M58 8 Q56 2 62 2" fill="none" {ln(O, 3)}/>
<path d="M54 50 L64 54 L74 50 L74 58 L64 54 L54 58Z" fill="#E8344A" {s('stroke-width="2"')}/>
{face(64, 66, d=8, k=0.75, mouth=True)}
<path d="M64 60 V100" stroke="#F2E2B0" stroke-width="1" opacity=".6"/>
</g>
<path d="M98 50 L118 104" {ln(O, 4)}/><path d="M98 50 L118 104" {ln("#E8D6A8", 1.8)}/>
<circle cx="18" cy="40" r="5" fill="#E8344A" {s('stroke-width="2"')}/><path d="M18 45 V58" {ln("#3FB86A", 2.4)}/>
<circle cx="106" cy="24" r="5" fill="#FFD23A" {s('stroke-width="2"')}/><path d="M106 29 V40" {ln("#3FB86A", 2.4)}/>
<circle cx="14" cy="84" r="4" fill="#F27AB8" {s('stroke-width="2"')}/>
'''))

# Театр песни Вилли Винки — малыш в ночном колпаке поёт со свечкой
I["villi-vinky-kibalchicha"] = ("малыш в полосатом ночном колпаке с помпоном и голубой пижаме",
    "поёт песенку со свечкой в руке у окна, за которым улыбается луна", bg("#3A4A8E", "#1C2456", f'''
<rect x="66" y="10" width="52" height="52" rx="4" fill="#24306A" {s()}/><path d="M92 10 V62 M66 36 H118" {ln(O, 3)}/>
<path d="M104 18 A12 12 0 1 0 110 38 A9 9 0 1 1 104 18Z" fill="#FFE07A" {s('stroke-width="2.2"')}/>
<circle cx="76" cy="20" r="1.6" fill="#fff"/><circle cx="84" cy="52" r="1.6" fill="#fff"/><circle cx="110" cy="54" r="1.6" fill="#fff"/>
<path d="M30 124 L34 78 Q46 70 58 78 L62 124Z" fill="#8FC8F2" {s()}/><path d="M38 90 h16 M37 102 h18" stroke="#fff" stroke-width="2.4"/>
<circle cx="46" cy="62" r="15" fill="{SKIN}" {s()}/>
<path d="M30 58 Q30 38 48 36 Q66 30 82 48 Q66 44 60 50 L62 58Z" fill="#fff" {s()}/>
<path d="M40 40 L46 56 M54 36 L58 54 M68 38 L66 50" {ln("#E8344A", 3.5)}/>
<circle cx="84" cy="50" r="6" fill="#fff" {s('stroke-width="2.4"')}/>
{eye(41, 64, 0.6)}{eye(52, 64, 0.6)}<ellipse cx="47" cy="72" rx="3.4" ry="3" fill="#B2283C" {s('stroke-width="1.6"')}/>
{limb(58, 86, 72, 92, "#8FC8F2", 5)}
<ellipse cx="78" cy="98" rx="9" ry="3.5" fill="#E8B83A" {s('stroke-width="2.4"')}/>
<rect x="74" y="78" width="8" height="18" rx="2" fill="#FFF6E0" {s('stroke-width="2.4"')}/>
<path d="M78 66 Q72 72 78 78 Q84 72 78 66Z" fill="#FFB43A" {s('stroke-width="2"')}/>
{note(18, 36, 0.6, "#FFE07A")}{note(20, 90, 0.5, "#fff")}
'''))

# Арт-студия Виталия Лещенко — мальчик в берете рисует кораблик
I["asvl-malomoskovskaya"] = ("мальчик в синем берете и рабочем фартуке в пятнах краски",
    "рисует акварелью кораблик на парусе-холсте на мольберте у окна", bg("#FFFBE8", "#F2C46A", f'''
<rect x="8" y="8" width="40" height="50" rx="3" fill="#BFE6FF" {s()}/><path d="M28 8 V58 M8 33 H48" {ln(O, 2.6)}/>
<path d="M80 32 L72 120 M110 32 L118 120 M76 98 H114" {ln(O, 3.4)}/>
<rect x="70" y="22" width="48" height="50" rx="2" fill="#fff" {s()}/>
<path d="M76 60 Q94 70 112 60" fill="none" {ln("#3A86C0", 4)}/><path d="M82 58 H106 L100 64 H88Z" fill="#E8344A" {s('stroke-width="2"')}/>
<path d="M94 58 V32 L106 52Z" fill="#FFD23A" {s('stroke-width="2"')}/>
<path d="M28 124 L30 84 Q42 76 54 84 L58 124Z" fill="#F2F2F2" {s()}/>
<circle cx="36" cy="100" r="3" fill="#E8344A"/><circle cx="48" cy="108" r="3" fill="#3FB86A"/><circle cx="44" cy="94" r="2.4" fill="#3A86C0"/>
<circle cx="42" cy="68" r="13" fill="{SKIN}" {s()}/>
<ellipse cx="40" cy="56" rx="16" ry="7" fill="#2E4AD8" {s()}/><circle cx="40" cy="48" r="2.6" fill="#2E4AD8" {s('stroke-width="2"')}/>
{eye(38, 70, 0.55)}{eye(48, 70, 0.55)}<path d="M39 76 Q43 79 47 76" fill="none" {s('stroke-width="1.8"')}/>
{limb(54, 88, 74, 66, "#F2F2F2", 5)}<path d="M74 66 L84 56" {ln(O, 3)}/><path d="M84 56 l3 -3" {ln("#3A86C0", 5)}/>
'''))

# Балетная студия А. Красовской — балерина в арабеске на звезде-подиуме
I["krasovskaya-ballet-suvorovskaya"] = ("девочка-балерина в голубом купальнике и белой юбочке-шопенке",
    "делает арабеск на большой красной пятиконечной звезде-подиуме", bg("#EEF6FF", "#8AB4E8", f'''
<path d="M64 74 L76 98 L104 100 L82 114 L90 128 L64 118 L38 128 L46 114 L24 100 L52 98Z" fill="#E8344A" {s()}/>
{limb(62, 84, 62, 104, SKIN, 4)}<ellipse cx="62" cy="106" rx="3.5" ry="4" fill="#FFB0D0" {s('stroke-width="2"')}/>
{limb(66, 78, 104, 66, SKIN, 4)}<ellipse cx="106" cy="65" rx="4" ry="3" fill="#FFB0D0" {s('stroke-width="2"')}/>
<path d="M54 50 Q62 44 70 50 L72 76 H52Z" fill="#7FB8F2" {s()}/>
<path d="M44 76 Q62 70 80 76 L84 88 Q62 84 40 88Z" fill="#fff" {s()}/>
{limb(56, 54, 30, 40, SKIN, 3.6)}{limb(68, 54, 88, 30, SKIN, 3.6)}
<circle cx="62" cy="36" r="11" fill="{SKIN}" {s()}/>
<path d="M51 34 Q52 22 62 22 Q73 22 73 34 Q68 28 62 28 Q56 28 51 34Z" fill="#6A3A1E" {s('stroke-width="2.2"')}/><circle cx="62" cy="20" r="5" fill="#6A3A1E" {s('stroke-width="2.2"')}/>
{eye(58, 37, 0.5)}{eye(66, 37, 0.5)}<path d="M59 42 Q62 45 65 42" fill="none" {s('stroke-width="1.6"')}/>
{sparkle(18, 70, 4)}{sparkle(112, 30, 4)}{sparkle(24, 24, 3)}
'''))

# ДМШ № 42 — три малыша-хориста
I["dmsh-42-petrovsko-razumovsky"] = ("три малыша-хориста в белых рубашках с бабочками",
    "поют хором по раскрытым красным нотным папкам, стоя на ступеньках", bg("#E9ECFF", "#7A86D8", f'''
<rect x="0" y="100" width="128" height="28" fill="#A8683A"/><rect x="34" y="88" width="60" height="12" fill="#C98E52" {s('stroke-width="2.4"')}/>
<path d="M0 100 H128" {s('stroke-width="2.4"')}/>
<path d="M14 100 L18 74 Q26 68 34 74 L38 100Z" fill="#fff" {s()}/><circle cx="26" cy="60" r="11" fill="{SKIN}" {s()}/>
<path d="M15 58 Q16 46 26 46 Q37 46 37 58 Q32 52 26 52Z" fill="#E8B83A" {s('stroke-width="2.2"')}/>
{eye(22, 61, 0.45)}{eye(30, 61, 0.45)}<ellipse cx="26" cy="67" rx="2.4" ry="2.2" fill="#B2283C"/>
<path d="M50 88 L54 60 Q64 54 74 60 L78 88Z" fill="#fff" {s()}/><circle cx="64" cy="44" r="12" fill="{SKIN}" {s()}/>
<path d="M52 42 Q53 30 64 30 Q76 30 76 42 Q70 36 64 36Z" fill="#3A2418" {s('stroke-width="2.2"')}/>
{eye(60, 45, 0.5)}{eye(68, 45, 0.5)}<ellipse cx="64" cy="52" rx="2.6" ry="2.4" fill="#B2283C"/>
<path d="M90 100 L94 74 Q102 68 110 74 L114 100Z" fill="#fff" {s()}/><circle cx="102" cy="60" r="11" fill="{SKIN}" {s()}/>
<path d="M91 58 Q92 46 102 46 Q113 46 113 58 Q113 66 116 70 L110 62 Q102 52 94 62 L88 70 Q91 66 91 58Z" fill="#B85A2A" {s('stroke-width="2.2"')}/>
{eye(98, 61, 0.45)}{eye(106, 61, 0.45)}<ellipse cx="102" cy="67" rx="2.4" ry="2.2" fill="#B2283C"/>
<path d="M22 74 l4 3 l4 -3 v6 l-4 -3 l-4 3Z M60 58 l4 3 l4 -3 v6 l-4 -3 l-4 3Z M98 74 l4 3 l4 -3 v6 l-4 -3 l-4 3Z" fill="#2F2B3A"/>
<rect x="16" y="82" width="20" height="12" rx="2" fill="#D8344A" {s('stroke-width="2.2"')}/>
<rect x="54" y="68" width="20" height="12" rx="2" fill="#D8344A" {s('stroke-width="2.2"')}/>
<rect x="92" y="82" width="20" height="12" rx="2" fill="#D8344A" {s('stroke-width="2.2"')}/>
{note(30, 22, 0.6, "#fff")}{note(92, 18, 0.6, "#FFD23A")}
'''))

# Stanislavsky studio — подросток с монологом и свитком
I["stanislavsky-studio-chernyshevskogo"] = ("подросток-актёр в зелёном плаще и берете с пером",
    "читает монолог по длинному свитку на краю сцены в луче света", bg("#E8FFF0", "#2F8A6A", f'''
<path d="M64 0 L28 112 H100Z" fill="#FFF6C4" opacity=".45"/>
<rect x="0" y="112" width="128" height="16" fill="#5A3A2A"/><path d="M0 112 H128" {s()}/>
{limb(58, 94, 54, 112, "#3A3A48", 6)}{limb(70, 94, 74, 112, "#3A3A48", 6)}
<path d="M44 60 Q64 50 84 60 L92 100 H36Z" fill="#2E9A5A" {s()}/>
<path d="M56 58 L64 96 L72 58Z" fill="#FFE07A" {s('stroke-width="2.2"')}/>
<circle cx="64" cy="42" r="12" fill="{SKIN}" {s()}/>
<ellipse cx="62" cy="32" rx="15" ry="6" fill="#7A2A9A" {s()}/>
<path d="M72 30 Q92 14 98 22 Q88 24 76 32Z" fill="#fff" {s('stroke-width="2.2"')}/>
{eye(60, 44, 0.5)}{eye(69, 44, 0.5)}<ellipse cx="64" cy="51" rx="3" ry="2.6" fill="#B2283C" {s('stroke-width="1.4"')}/>
{limb(46, 66, 28, 56, "#2E9A5A", 5)}
<rect x="12" y="38" width="16" height="44" rx="3" fill="#FFF3D6" {s()}/><path d="M16 48 h8 M16 56 h8 M16 64 h8 M16 72 h6" {ln("#9A8A6A", 1.8)}/>
<ellipse cx="20" cy="38" rx="9" ry="4" fill="#E8D6A8" {s('stroke-width="2.2"')}/><ellipse cx="20" cy="82" rx="9" ry="4" fill="#E8D6A8" {s('stroke-width="2.2"')}/>
{limb(82, 66, 104, 46, "#2E9A5A", 5)}<circle cx="106" cy="44" r="4" fill="{SKIN}" {s('stroke-width="2.2"')}/>
'''))

# Ладушки — малышка в сарафане кружится в топотушке
I["ladushki-biryulevskaya"] = ("малышка в жёлтом сарафане с двумя косичками-бубликами",
    "кружится в топотушке, а вокруг хлопают в ладоши разноцветные ладошки-звёздочки", bg("#FFF0E0", "#F28A5A", f'''
<rect x="0" y="110" width="128" height="18" fill="#D9A15E"/>
<path d="M40 112 L44 104 M60 114 L58 106 M74 114 L76 106 M88 112 L84 104" {ln(O, 3)}/>
<ellipse cx="52" cy="114" rx="7" ry="4" fill="#E8344A" {s('stroke-width="2.2"')}/><ellipse cx="78" cy="114" rx="7" ry="4" fill="#E8344A" {s('stroke-width="2.2"')}/>
<path d="M50 60 Q64 54 78 60 L94 106 H34Z" fill="#FFD23A" {s()}/>
<path d="M40 92 Q64 100 88 92" fill="none" {ln("#E8344A", 3)}/><circle cx="52" cy="80" r="3" fill="#E8344A"/><circle cx="74" cy="84" r="3" fill="#3FB86A"/><circle cx="62" cy="96" r="3" fill="#3A86C0"/>
{limb(52, 64, 30, 50, SKIN, 4)}{limb(76, 64, 98, 50, SKIN, 4)}
<circle cx="64" cy="42" r="14" fill="{SKIN}" {s()}/>
<path d="M50 40 Q52 26 64 26 Q76 26 78 40 Q70 32 64 34 Q58 32 50 40Z" fill="#C9822E" {s('stroke-width="2.2"')}/>
<circle cx="46" cy="44" r="6" fill="#C9822E" {s('stroke-width="2.2"')}/><circle cx="82" cy="44" r="6" fill="#C9822E" {s('stroke-width="2.2"')}/>
{face(64, 44, d=6, k=0.6)}
<path d="M24 46 l-4 -4 M24 46 l-6 0 M24 46 l-4 4 M104 46 l4 -4 M104 46 l6 0 M104 46 l4 4" {ln("#fff", 2.6)}/>
{sparkle(30, 22, 5)}{sparkle(100, 20, 5, "#FFE07A")}{sparkle(14, 80, 3.5)}{sparkle(114, 82, 3.5)}
'''))

# Der Вальс — хрустальная бальная люстра над вальсирующей парой
I["der-walz-chertanovo"] = ("хрустальная бальная люстра с подвесками и мордашкой",
    "сияет под потолком над крошечной вальсирующей парой на паркете", bg("#F4ECFF", "#6A4AA8", f'''
<path d="M64 0 V14" {ln(O, 3)}/>
<path d="M30 30 Q64 50 98 30 L90 22 Q64 34 38 22Z" fill="#F2D06A" {s()}/>
<ellipse cx="64" cy="22" rx="18" ry="10" fill="#FFE9A8" {s()}/>
{face(64, 22, d=6, k=0.55)}
<path d="M34 34 V46 M46 40 V54 M58 42 V58 M70 42 V58 M82 40 V54 M94 34 V46" {ln(O, 1.8)}/>
<path d="M34 46 l-3 5 l3 5 l3 -5Z M46 54 l-3 5 l3 5 l3 -5Z M58 58 l-3 5 l3 5 l3 -5Z M70 58 l-3 5 l3 5 l3 -5Z M82 54 l-3 5 l3 5 l3 -5Z M94 46 l-3 5 l3 5 l3 -5Z" fill="#C9F0FF" {s('stroke-width="1.6"')}/>
<path d="M64 60 L40 112 H88Z" fill="#FFF6C4" opacity=".35"/>
<rect x="0" y="112" width="128" height="16" fill="#9A5A2E"/>
<path d="M56 112 L58 94 M62 112 L60 94" {ln(O, 3)}/><path d="M52 92 Q58 82 64 92 L62 98 H54Z" fill="#26222F" {s('stroke-width="2"')}/><circle cx="58" cy="80" r="4.5" fill="{SKIN}" {s('stroke-width="2"')}/>
<path d="M64 88 Q70 80 76 88 L84 112 H62Z" fill="#7FD0F2" {s('stroke-width="2"')}/><circle cx="70" cy="78" r="4.5" fill="{SKIN}" {s('stroke-width="2"')}/>
{sparkle(20, 60, 4)}{sparkle(108, 64, 4)}{sparkle(26, 96, 3)}
'''))

# Место искусства — мальчик-брейкер в фризе на картоне
I["mesto-iskusstva-dmitrovskoe"] = ("мальчик-брейкер в зелёной шапке-бини и полосатых гетрах",
    "застыл в фризе на одной руке на листе картона, ноги смешно скрещены в воздухе", bg("#F2FFE6", "#7ACB3A", f'''
<path d="M10 112 L118 104 L122 122 L8 128Z" fill="#C9A36A" {s()}/><path d="M30 114 L96 108" stroke="#A8824A" stroke-width="2"/>
<circle cx="56" cy="96" r="12" fill="{SKIN}" {s()}/>
<path d="M44 98 Q44 110 56 110 Q68 110 68 98Z" fill="#3FB86A" {s()}/><path d="M44 104 H68" {ln(O, 2)}/>
{eye(52, 92, 0.5)}{eye(60, 92, 0.5)}<path d="M53 86 Q56 83 59 86" fill="none" {s('stroke-width="1.6"')}/>
{limb(50, 82, 40, 106, "#FF8A2E", 5)}<ellipse cx="38" cy="108" rx="5" ry="3" fill="{SKIN}" {s('stroke-width="2"')}/>
<path d="M44 82 Q48 62 62 56 L76 66 Q70 84 58 86Z" fill="#FF8A2E" {s()}/>
{limb(66, 60, 92, 40, "#3A3A48", 6)}{limb(72, 64, 100, 58, "#3A3A48", 6)}
<path d="M86 44 l8 -8 M94 60 l10 -2" {ln("#fff", 4)}/><path d="M88 42 l4 -4 M98 59 l4 -1" {ln("#E8344A", 2.4)}/>
<rect x="88" y="26" width="14" height="9" rx="4" fill="#fff" transform="rotate(-40 95 30)" {s('stroke-width="2.2"')}/>
<rect x="100" y="52" width="14" height="9" rx="4" fill="#fff" transform="rotate(-10 107 56)" {s('stroke-width="2.2"')}/>
<path d="M20 60 q-4 -8 4 -12 M28 44 q-2 -8 6 -10" fill="none" {ln("#fff", 2.6)}/>
'''))

# Не душная Музыкалка — синтезатор в солнечных очках
I["nedushnaya-muzykalka-dubninskaya"] = ("синтезатор на стойке в солнечных очках",
    "на нём играет рыжая девочка, а настольный вентилятор раздувает вылетающие ноты", bg("#E6FBFF", "#3AB8D8", f'''
<rect x="0" y="112" width="128" height="16" fill="#2A8AA8"/>
<path d="M30 112 L50 82 M78 112 L58 82" {ln(O, 4)}/>
<rect x="10" y="66" width="88" height="22" rx="4" fill="#2F2B3A" {s()}/>
<rect x="16" y="76" width="76" height="9" fill="#fff" {s('stroke-width="1.8"')}/>
<path d="M24 76 V81 M32 76 V81 M44 76 V81 M52 76 V81 M60 76 V81 M72 76 V81 M80 76 V81" {ln(O, 2.6)}/>
<rect x="22" y="68" width="16" height="6" rx="3" fill="#2F2B3A" {s('stroke-width="1.6"')}/><rect x="42" y="68" width="16" height="6" rx="3" fill="#2F2B3A" {s('stroke-width="1.6"')}/>
<path d="M38 71 h4" {ln(O, 2)}/><path d="M66 72 Q72 76 78 72" fill="none" stroke="#FFD23A" stroke-width="2.2" stroke-linecap="round"/>
<path d="M40 66 L44 40 Q56 32 66 40 L68 66Z" fill="#E86A8E" {s()}/>
<circle cx="56" cy="26" r="11" fill="{SKIN}" {s()}/><path d="M44 26 Q44 12 56 12 Q70 12 68 28 Q74 34 70 42 Q66 30 58 20 Q52 30 44 34Z" fill="#E8742E" {s('stroke-width="2.2"')}/>
{eye(53, 28, 0.45)}{eye(60, 28, 0.45)}
<circle cx="110" cy="58" r="12" fill="#BFE6FF" {s()}/><path d="M110 46 V70 M98 58 H122" {ln(O, 2)}/><path d="M110 70 V84 M102 84 H118" {ln(O, 3)}/>
{note(84, 40, 0.6, "#fff")}{note(72, 22, 0.5, "#FFD23A")}{note(92, 14, 0.45, "#fff")}
<path d="M96 52 q-6 -2 -10 -8 M96 60 q-8 0 -14 -4" fill="none" {ln("#fff", 2)}/>
'''))

# Гончарная мастерская «Три сестры» — три кувшинчика-сестрички
I["tri-sestry-novocherkassky"] = ("три глиняных кувшинчика-сестрички разного роста в цветных платочках",
    "стоят по росту в ряд на деревянной полке гончарной мастерской", bg("#FFF4E6", "#C9864A", f'''
<rect x="0" y="100" width="128" height="10" fill="#8A5A34" {s()}/><path d="M14 110 V128 M114 110 V128" {ln(O, 5)}/>
<path d="M14 100 Q8 76 20 64 Q16 56 24 52 H34 Q42 56 38 64 Q50 76 44 100Z" fill="#C86A3A" {s()}/>
<path d="M18 58 Q29 48 40 58 Q29 54 18 58Z" fill="#3A86C0" {s('stroke-width="2.4"')}/>
{eye(25, 78, 0.5)}{eye(34, 78, 0.5)}<path d="M26 84 Q29.5 87 33 84" fill="none" {s('stroke-width="1.6"')}/>
<path d="M50 100 Q42 68 56 54 Q50 44 60 38 H70 Q80 44 74 54 Q88 68 80 100Z" fill="#D8844A" {s()}/>
<path d="M54 44 Q65 32 76 44 Q65 40 54 44Z" fill="#E8344A" {s('stroke-width="2.4"')}/>
<path d="M80 62 Q92 64 86 80" fill="none" {ln(O, 3.6)}/>
{face(65, 72, d=6, k=0.6)}
<path d="M90 100 Q86 86 94 80 Q92 74 98 72 H104 Q110 74 108 80 Q116 86 112 100Z" fill="#B85A2E" {s()}/>
<path d="M92 76 Q101 68 110 76 Q101 73 92 76Z" fill="#FFD23A" {s('stroke-width="2.2"')}/>
{eye(97, 88, 0.42)}{eye(105, 88, 0.42)}
<path d="M20 26 q6 -8 12 0 M96 30 q6 -8 12 0" fill="none" {ln("#fff", 2.6)}/>
'''))

# Ёлка (школа танцев) — ёлочка-балерина в пачке
I["elka-lokomotivny"] = ("зелёная ёлочка-балерина в розовой пачке",
    "делает пируэт на одной ножке-стволе посреди танцзала с зеркалом", bg("#F0FFF2", "#4AB86A", f'''
<rect x="0" y="0" width="128" height="96" fill="#DFF5FF" opacity=".5"/><path d="M0 96 H128" {s('stroke-width="2"')}/>
<rect x="0" y="96" width="128" height="32" fill="#C98E52"/>
<path d="M64 98 V116" {ln(O, 7)}/><path d="M64 98 V116" {ln("#8A5A34", 4)}/><ellipse cx="64" cy="118" rx="6" ry="3" fill="#8A5A34" {s('stroke-width="2.2"')}/>
<path d="M64 98 V82" {ln(O, 7)}/><path d="M64 98 V82" {ln("#8A5A34", 4)}/>
<path d="M88 72 Q100 60 112 70" fill="none" {ln("#8A5A34", 4)}/>
<path d="M64 12 L84 40 L76 40 L92 62 L82 62 L100 86 H28 L46 62 L36 62 L52 40 L44 40Z" fill="#2EA85A" {s()}/>
<path d="M20 84 Q64 72 108 84 L112 94 Q64 86 16 94Z" fill="#FF9AC4" {s()}/>
<path d="M24 92 l4 -6 M40 90 l3 -6 M56 89 l2 -6 M72 89 l-2 -6 M88 90 l-3 -6 M104 92 l-4 -6" {ln("#fff", 2)}/>
<path d="M64 8 l3 6 l6 1 l-5 4 l1 6 l-5 -3 l-5 3 l1 -6 l-5 -4 l6 -1Z" fill="#FFD23A" {s('stroke-width="2"')}/>
{face(64, 50, d=7, k=0.7)}
{sparkle(108, 26, 5)}{sparkle(18, 40, 4)}
'''))

# Step Up — девочка взбегает по ступенькам-кубам
I["step-up-bratislavskaya"] = ("три цветные ступеньки-кубы с мордашками",
    "по ним вверх взбегает девочка в блестящем эстрадном костюме с поднятой рукой", bg("#FFF0FF", "#B85AC8", f'''
<rect x="8" y="94" width="34" height="34" rx="4" fill="#3FB8E8" {s()}/>{eye(19, 108, 0.45)}{eye(31, 108, 0.45)}
<rect x="44" y="74" width="34" height="54" rx="4" fill="#FFD23A" {s()}/>{eye(55, 88, 0.45)}{eye(67, 88, 0.45)}
<rect x="80" y="54" width="34" height="74" rx="4" fill="#E8344A" {s()}/>{eye(91, 68, 0.45)}{eye(103, 68, 0.45)}
<path d="M17 114 Q25 118 33 114 M53 94 Q61 98 69 94 M89 74 Q97 78 105 74" fill="none" {s('stroke-width="1.6"')}/>
{limb(62, 50, 56, 72, SKIN, 4)}{limb(66, 50, 82, 56, SKIN, 4)}
<path d="M54 26 Q62 20 70 26 L74 52 H50Z" fill="#C8A0F2" {s()}/>
<path d="M56 32 l2 2 M64 30 l2 2 M60 40 l2 2 M68 44 l2 2 M54 46 l2 2" {ln("#fff", 2)}/>
{limb(56, 30, 40, 18, SKIN, 3.6)}{limb(70, 30, 86, 10, SKIN, 3.6)}
<circle cx="62" cy="14" r="9" fill="{SKIN}" {s()}/><path d="M53 12 Q54 2 62 2 Q71 2 71 12 Q76 16 72 24 Q68 12 62 8 Q56 12 52 20Z" fill="#3A2418" {s('stroke-width="2"')}/>
{eye(59, 15, 0.42)}{eye(66, 15, 0.42)}
{sparkle(104, 26, 5)}{sparkle(20, 60, 4)}{sparkle(32, 30, 3)}
'''))

# Studio1815 — холст на подрамнике сам дорисовывает закат
I["studio1815-otradny"] = ("холст на подрамнике с мордашкой и руками-ветками",
    "сам себе дорисовывает закатное небо над морем, держа кисть в руке-ветке", bg("#FFF4E8", "#E89A6A", f'''
<rect x="26" y="20" width="76" height="80" rx="3" fill="#FFF6E8" {s()}/>
<path d="M30 24 H98 V60 H30Z" fill="#FFB86A"/><path d="M30 44 H98 V60 H30Z" fill="#F27A5A"/>
<circle cx="64" cy="58" r="12" fill="#FFD23A"/>
<path d="M30 60 H98 V72 H30Z" fill="#3A86C0"/><path d="M36 66 h10 M58 68 h14 M82 65 h10" stroke="#fff" stroke-width="2"/>
<path d="M26 20 H102 V100 H26Z" fill="none" {s()}/>
{face(64, 84, d=10, k=0.8)}
<path d="M38 100 L32 124 M90 100 L96 124" {ln(O, 4)}/>
<path d="M102 60 Q114 54 116 40" fill="none" {ln(O, 5)}/><path d="M102 60 Q114 54 116 40" fill="none" {ln("#A8683A", 2.6)}/>
<path d="M116 40 L108 28" {ln(O, 3)}/><path d="M108 28 l-3 -4" {ln("#F27A5A", 5)}/>
<path d="M26 62 Q14 70 12 84" fill="none" {ln(O, 5)}/><path d="M26 62 Q14 70 12 84" fill="none" {ln("#A8683A", 2.6)}/>
<ellipse cx="12" cy="90" rx="8" ry="5" fill="#fff" {s('stroke-width="2.2"')}/><circle cx="8" cy="89" r="2" fill="#3A86C0"/><circle cx="14" cy="91" r="2" fill="#E8344A"/>
'''))

# Студия вокала Виктории Осиповой — девочка в матроске поёт на кораблике
I["osipova-flotskaya"] = ("девочка-певица в синей матроске с красным галстуком",
    "поёт в микрофон на носу маленького кораблика среди волн", bg("#E6F6FF", "#3A8AD8", f'''
<path d="M0 96 Q16 88 32 96 T64 96 T96 96 T128 96 V128 H0Z" fill="#2A6AB8" {s('stroke-width="2.4"')}/>
<path d="M14 92 H112 L100 112 H28Z" fill="#fff" {s()}/><path d="M24 100 H104" {ln("#E8344A", 3)}/>
<path d="M98 92 V30" {ln(O, 3.4)}/><path d="M98 34 L118 40 L98 46Z" fill="#E8344A" {s('stroke-width="2.2"')}/>
{limb(50, 78, 48, 92, SKIN, 4)}{limb(60, 78, 62, 92, SKIN, 4)}
<path d="M42 50 Q55 44 68 50 L70 80 H40Z" fill="#2E4AD8" {s()}/><path d="M44 50 L55 62 L66 50 L64 56 L55 66 L46 56Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M53 60 l2 8 l2 -8Z" fill="#E8344A" {s('stroke-width="1.6"')}/>
<circle cx="55" cy="36" r="11" fill="{SKIN}" {s()}/>
<path d="M44 34 Q45 22 55 22 Q66 22 66 34 Q70 40 68 48 Q62 34 55 28 Q50 36 42 44 Q42 38 44 34Z" fill="#E8B83A" {s('stroke-width="2.2"')}/>
{eye(52, 37, 0.45)}<ellipse cx="57" cy="42" rx="2.4" ry="2.2" fill="#B2283C"/>
{limb(66, 54, 76, 46, "#2E4AD8", 4)}
<path d="M76 46 L84 38" {ln(O, 4.5)}/><circle cx="85" cy="36" r="4.5" fill="#B9B6CF" {s('stroke-width="2"')}/>
{note(28, 30, 0.6, "#fff")}{note(16, 58, 0.5, "#FFD23A")}{note(80, 18, 0.5, "#fff")}
'''))

# Ars Musica — старинная лютня у стрельчатого окна
I["ars-musica-lyapidevskogo"] = ("старинная грушевидная лютня с мордашкой и розеткой-цветком",
    "сама перебирает струны у стрельчатого окна с цветным витражом", bg("#F6EEDC", "#A8783A", f'''
<path d="M78 120 V40 Q78 14 100 10 Q122 14 122 40 V120Z" fill="#6A9AE8" {s()}/>
<path d="M100 10 V120 M78 56 H122 M78 88 H122" {ln(O, 2.4)}/>
<path d="M80 40 Q82 18 98 14 V56 H80Z" fill="#E8344A" opacity=".7"/><path d="M102 56 H120 V88 H102Z" fill="#FFD23A" opacity=".7"/><path d="M80 88 H98 V118 H80Z" fill="#3FB86A" opacity=".7"/>
<g transform="rotate(-28 46 74)">
<path d="M46 48 Q18 58 20 88 Q24 116 46 118 Q68 116 72 88 Q74 58 46 48Z" fill="#D89A4A" {s()}/>
<path d="M30 70 Q46 66 62 70" fill="none" stroke="#B87A3A" stroke-width="2"/>
<circle cx="46" cy="80" r="8" fill="#7A4A1E" {s('stroke-width="2.2"')}/><path d="M46 72 V88 M38 80 H54 M40 74 L52 86 M52 74 L40 86" stroke="#D89A4A" stroke-width="1.6"/>
<rect x="42" y="14" width="8" height="36" rx="2" fill="#8A5A2E" {s('stroke-width="2.4"')}/>
<path d="M42 14 L30 6 L34 2 L50 12Z" fill="#6A4220" {s('stroke-width="2.2"')}/>
<path d="M44 20 V108 M48 20 V108" stroke="#F2E6C4" stroke-width="1" opacity=".9"/>
{eye(38, 98, 0.5)}{eye(54, 98, 0.5)}<path d="M42 104 Q46 107 50 104" fill="none" {s('stroke-width="1.6"')}/>
</g>
{note(76, 30, 0.55, "#7A4A1E")}{note(14, 30, 0.5, "#fff")}
'''))

# Русская школа искусств — яблоко-натурщик позирует
I["rusartschool-pulkovskaya"] = ("красное яблоко-натурщик с листиком и в маленькой шляпке",
    "важно позирует на голубой драпировке, а рядом карандаш штрихует его портрет на планшете", bg("#EEF2FA", "#7A8AB8", f'''
<path d="M0 70 Q30 60 50 76 Q70 92 70 128 H0Z" fill="#9AC8F2" {s()}/>
<path d="M8 80 Q20 76 30 90 M14 100 Q30 98 40 114" fill="none" stroke="#6AA0D8" stroke-width="2.4"/>
<path d="M18 74 Q8 52 24 42 Q36 38 40 46 Q46 38 58 42 Q72 52 62 74 Q54 90 40 86 Q26 90 18 74Z" fill="#E8344A" {s()}/>
<path d="M40 44 Q42 34 46 30" fill="none" {ln(O, 3)}/><path d="M46 32 Q56 26 60 34 Q52 38 46 32Z" fill="#3FB86A" {s('stroke-width="2.2"')}/>
<ellipse cx="34" cy="38" rx="12" ry="3.5" fill="#26222F" {s('stroke-width="2"')}/><rect x="28" y="28" width="12" height="10" rx="2" fill="#26222F" {s('stroke-width="2"')}/>
{face(40, 62, d=7, k=0.7)}
<rect x="76" y="30" width="44" height="58" rx="2" fill="#fff" transform="rotate(6 98 60)" {s()}/>
<path d="M88 66 Q86 50 96 46 Q102 44 104 48 Q110 44 114 52 Q118 66 104 72 Q94 74 88 66Z" fill="none" {ln("#6A6A7A", 2)}/>
<path d="M92 60 l6 6 M96 56 l8 8 M100 54 l8 8" {ln("#9A9AA8", 1.6)}/>
<path d="M82 112 L112 76" {ln(O, 6.5)}/><path d="M82 112 L112 76" {ln("#F2C23A", 3.6)}/><path d="M112 76 l3 -4" {ln(O, 3)}/>
'''))

ALL = I

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        hero, scene, svg = I[pid]
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg)
    print("svg", len(ids))
