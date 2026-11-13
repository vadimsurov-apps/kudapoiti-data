"""Иконки робота creative, 13.11 (запуск 1113b). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1113b.py [--subjects]"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_creative_1112k import bg, ln, limb, note, head, SKIN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
I = {}

# 1 Академия балета «Сказка» у Ходынского поля (бывший аэродром): балетная пачка летит, как летающая тарелка
I["skazka-ballet-khodynsky"] = ("белоснежная балетная пачка с розовым корсажем и мордашкой",
    "парит над взлётной полосой Ходынского поля, как летающая тарелка, с огоньками-стразами по краю юбки", bg("#DDF1FF", "#4F8FD8", f'''
<path d="M-4 112 L132 100 V132 H-4Z" fill="#6C7484" {s()}/>
<path d="M10 113 L24 112 M44 110 L58 109 M78 107 L92 106 M110 104 L124 103" {ln("#fff", 3)}/>
<path d="M50 84 L40 104 M78 84 L88 104" {ln("#FFE27A", 5)} opacity=".7"/>
<g transform="rotate(-8 64 64)">
<ellipse cx="64" cy="72" rx="56" ry="16" fill="#FFFFFF" {s()}/>
<path d="M14 70 Q64 58 114 70" fill="none" stroke="#D8E4F2" stroke-width="2.4"/>
<path d="M22 76 Q64 86 106 76" fill="none" stroke="#D8E4F2" stroke-width="2.4"/>
<circle cx="22" cy="74" r="3" fill="#FFD43B" {s('stroke-width="1.4"')}/><circle cx="44" cy="82" r="3" fill="#FF8FB5" {s('stroke-width="1.4"')}/>
<circle cx="84" cy="82" r="3" fill="#FFD43B" {s('stroke-width="1.4"')}/><circle cx="106" cy="74" r="3" fill="#FF8FB5" {s('stroke-width="1.4"')}/>
<path d="M44 66 Q42 40 50 26 Q64 20 78 26 Q86 40 84 66 Q64 72 44 66Z" fill="#FF8FB5" {s()}/>
<path d="M50 26 Q64 34 78 26" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M64 30 V64" stroke="#E86A98" stroke-width="2"/>
{face(64, 48, 7, 0.6)}
</g>
{sparkle(108, 18, 4)}{sparkle(24, 30, 3)}
'''))

# 2 «Я Танцую» (хип-хоп и балет): балерина в пачке и бейсболке делает хип-хоп «дэб»
I["ya-tantsuyu-parkovaya"] = ("девочка-балерина в розовой пачке и чёрной бейсболке козырьком вбок",
    "стоит на пуанте и одновременно делает хип-хоп жест «дэб», уткнувшись носом в локоть, на сером паркете", bg("#F4ECFF", "#9A7AD6", f'''
<path d="M0 108 H128 V128 H0Z" fill="#B9B2C6" {s()}/>
<path d="M20 108 V128 M52 108 V128 M84 108 V128 M116 108 V128" stroke="#9C94AC" stroke-width="2"/>
{limb(62, 82, 60, 106, SKIN, 4)}<path d="M57 106 L63 106 L61 112Z" fill="#FF8FB5" {s('stroke-width="2"')}/>
{limb(66, 82, 84, 96, SKIN, 4)}
<path d="M54 58 L74 58 L72 80 L56 80Z" fill="#FF8FB5" {s()}/>
<ellipse cx="64" cy="80" rx="28" ry="7" fill="#FFC4D9" {s()}/>
<path d="M40 79 Q64 90 88 79" fill="none" stroke="#FF8FB5" stroke-width="2"/>
{limb(56, 62, 36, 46, SKIN, 4)}{limb(72, 62, 94, 40, SKIN, 4)}
<circle cx="64" cy="44" r="12" fill="{SKIN}" {s()}/>
<path d="M50 40 Q52 28 64 28 Q76 28 78 40Z" fill="#26232E" {s('stroke-width="2.4"')}/>
<path d="M76 38 L94 34 L92 40 L76 42Z" fill="#26232E" {s('stroke-width="2.2"')}/>
<path d="M60 47 Q61.5 45 63 47 M66 47 Q67.5 45 69 47" fill="none" {ln(O, 2)}/>
<path d="M61 52 Q64 54 67 52" fill="none" {ln(O, 1.8)}/>
<ellipse cx="57" cy="51" rx="2.6" ry="1.5" fill="#FF7FA8" opacity=".6"/><ellipse cx="71" cy="51" rx="2.6" ry="1.5" fill="#FF7FA8" opacity=".6"/>
{sparkle(24, 24, 4)}{sparkle(106, 72, 3.5)}
'''))

# 3 True Dance Studio (современные танцы, K-pop): мальчик в лиловом худи замер в финальной позе под прожектором
I["true-dance-parkovaya"] = ("мальчик в лиловом худи с капюшоном и широких серых штанах",
    "замер в эффектной финальной позе, выбросив руку вверх, в розовом луче прожектора на круглой сцене", bg("#2A2350", "#120F26", f'''
<path d="M54 -4 L74 -4 L104 112 L24 112Z" fill="#FF8FD0" opacity=".35"/>
<ellipse cx="64" cy="110" rx="44" ry="10" fill="#4B3F86" {s()}/>
<ellipse cx="64" cy="108" rx="30" ry="5" fill="#FF8FD0" opacity=".5"/>
{limb(58, 82, 50, 106, "#9AA0B0", 7)}{limb(70, 82, 82, 104, "#9AA0B0", 7)}
<path d="M46 106 H56 M78 104 H90" {ln(O, 6)}/><path d="M46 106 H56 M78 104 H90" {ln("#fff", 3.5)}/>
<path d="M50 50 Q64 44 78 50 L80 84 L48 84Z" fill="#9B6BE0" {s()}/>
<path d="M58 66 H70 V74 H58Z" fill="#7E52C2" {s('stroke-width="2"')}/>
{limb(76, 54, 94, 24, "#9B6BE0", 7)}<circle cx="96" cy="20" r="5" fill="{SKIN}" {s('stroke-width="2.4"')}/>
{limb(52, 56, 34, 70, "#9B6BE0", 7)}<circle cx="32" cy="72" r="5" fill="{SKIN}" {s('stroke-width="2.4"')}/>
<path d="M50 50 Q48 26 64 24 Q80 26 78 50 Q64 44 50 50Z" fill="#9B6BE0" {s()}/>
<circle cx="64" cy="38" r="10" fill="{SKIN}" {s('stroke-width="2.4"')}/>
<path d="M58 37 L62 37 M66 37 L70 37" {ln(O, 2.4)}/><path d="M60 43 Q64 46 68 43" fill="none" {ln(O, 2)}/>
{sparkle(104, 52, 4, "#FFE27A")}{sparkle(22, 36, 3.5, "#FFE27A")}{sparkle(110, 90, 2.6)}
'''))

# 4 «Милград» (вокал 4–12 лет, рисование, много занятий): ретро-микрофон поёт, карандаши подпевают
I["milgrad-vladimirskaya"] = ("голубой ретро-микрофон с золотой решёткой и мордашкой",
    "поёт во весь голос, а из-за его подставки выглядывают три цветных карандаша-подпевалы с открытыми ртами", bg("#FFF7DC", "#F2B84B", f'''
<path d="M30 118 H98" {ln(O, 7)}/><path d="M30 118 H98" {ln("#8A93A8", 4)}/>
<path d="M64 118 V92" {ln(O, 9)}/><path d="M64 118 V92" {ln("#8A93A8", 5)}/>
<path d="M36 112 V82 L40 74 L44 82 V112Z" fill="#FF6B6B" {s('stroke-width="2.2"')}/>
<path d="M84 112 V78 L88 70 L92 78 V112Z" fill="#4DBE6E" {s('stroke-width="2.2"')}/>
<path d="M98 114 V86 L102 78 L106 86 V114Z" fill="#7A6CF0" {s('stroke-width="2.2"')}/>
<path d="M38.5 92 Q40 94 41.5 92 M86.5 88 Q88 90 89.5 88 M100.5 96 Q102 98 103.5 96" fill="none" {ln(O, 1.4)}/>
<circle cx="40" cy="98" r="1.6" fill="{O}"/><circle cx="88" cy="94" r="1.6" fill="{O}"/><circle cx="102" cy="102" r="1.6" fill="{O}"/>
<rect x="44" y="20" width="40" height="72" rx="20" fill="#5EC2F2" {s()}/>
<path d="M44 40 Q44 20 64 20 Q84 20 84 40 V46 H44Z" fill="#F5C542" {s()}/>
<path d="M50 30 H78 M48 38 H80 M56 22 V46 M64 20 V46 M72 22 V46" stroke="#C9962A" stroke-width="2"/>
{face(64, 64, 7, 0.6, mouth=False)}
<ellipse cx="64" cy="74" rx="5" ry="6" fill="#C2365A" {s('stroke-width="2"')}/>
{note(100, 30, 0.9)}{note(20, 46, 0.75, "#C2365A")}
{sparkle(108, 54, 3.5)}
'''))

# 5 «Балет Элион» (Балашиха, Заречная улица; занятия с 3 лет): малышка в огромной пачке делает реверанс у речки
I["ballet-elion-balashikha"] = ("трёхлетняя балерина в огромной фатиновой пачке, которая шире её самой",
    "делает реверанс, придерживая пачку обеими руками, на берегу речки у камышей", bg("#EAFBF2", "#5FBF97", f'''
<path d="M-4 100 Q30 92 64 100 Q98 108 132 98 V132 H-4Z" fill="#7CC6F0" {s()}/>
<path d="M14 112 Q22 108 30 112 M88 116 Q96 112 104 116" fill="none" {ln("#fff", 2.4)}/>
<path d="M104 96 V52 M112 94 V60 M120 96 V58" {ln("#3E8A54", 3)}/>
<ellipse cx="104" cy="50" rx="3.5" ry="9" fill="#8B5A2B" {s('stroke-width="2"')}/><ellipse cx="120" cy="56" rx="3.5" ry="9" fill="#8B5A2B" {s('stroke-width="2"')}/>
{limb(56, 84, 54, 98, SKIN, 4)}{limb(66, 84, 70, 98, SKIN, 4)}
<path d="M50 98 H58 M66 98 H74" {ln(O, 5)}/><path d="M50 98 H58 M66 98 H74" {ln("#FFC4D9", 3)}/>
<path d="M14 80 Q20 62 40 62 Q62 58 84 62 Q104 62 110 80 Q90 92 62 88 Q34 92 14 80Z" fill="#FFE3EE" {s()}/>
<path d="M22 78 Q40 70 62 74 Q84 70 102 78" fill="none" stroke="#F4AFCB" stroke-width="2.4"/>
<path d="M52 62 L54 46 H70 L72 62Z" fill="#FF8FB5" {s()}/>
{limb(54, 50, 30, 66, SKIN, 3.5)}{limb(70, 50, 94, 66, SKIN, 3.5)}
<circle cx="62" cy="34" r="12" fill="{SKIN}" {s()}/>
<path d="M50 32 Q52 20 62 20 Q72 20 74 32 Q66 26 62 27 Q58 26 50 32Z" fill="#E0A34A" {s('stroke-width="2.2"')}/>
<circle cx="62" cy="18" r="5" fill="#E0A34A" {s('stroke-width="2.2"')}/>
<path d="M56 35 Q58 33 60 35 M64 35 Q66 33 68 35" fill="none" {ln(O, 2)}/>
<path d="M59 40 Q62 42.5 65 40" fill="none" {ln(O, 1.8)}/>
<ellipse cx="54" cy="39" rx="2.6" ry="1.5" fill="#FF7FA8" opacity=".7"/><ellipse cx="70" cy="39" rx="2.6" ry="1.5" fill="#FF7FA8" opacity=".7"/>
{sparkle(24, 28, 4)}{sparkle(92, 22, 3)}
'''))

# 6 «Твой голос» (вокал с 3 лет, хор): птичка-малиновка в хоровом воротничке поёт с пюпитра
I["tvoy-golos-perovskaya"] = ("круглая птичка-малиновка с красной грудкой в белом хоровом воротничке",
    "поёт, раскрыв клюв, стоя на деревянном пюпитре с раскрытыми нотами", bg("#FFEFEA", "#E8756A", f'''
<path d="M64 128 V92" {ln(O, 9)}/><path d="M64 128 V92" {ln("#B07A45", 5)}/>
<path d="M50 128 L64 112 L78 128" fill="none" {ln("#B07A45", 4)}/>
<path d="M26 96 L102 96 L96 74 L32 74Z" fill="#C88A52" {s()}/>
<path d="M36 92 L62 92 L62 78 L38 78Z M66 92 L92 92 L90 78 L66 78Z" fill="#fff" {s('stroke-width="2"')}/>
<path d="M40 82 H58 M40 86 H58 M70 82 H88 M70 86 H88" stroke="#9AA0B8" stroke-width="1.4"/>
<circle cx="48" cy="85" r="1.8" fill="{O}"/><circle cx="78" cy="83" r="1.8" fill="{O}"/>
<path d="M58 74 L56 66 M70 74 L72 66" {ln("#E8A23A", 3)}/>
<ellipse cx="64" cy="48" rx="26" ry="22" fill="#8C6A4E" {s()}/>
<ellipse cx="62" cy="54" rx="16" ry="13" fill="#E8463A"/>
<path d="M88 40 Q104 30 108 44 Q100 46 88 50Z" fill="#6E5139" {s('stroke-width="2.4"')}/>
<path d="M50 60 Q56 70 64 64 Q72 70 78 60 Q70 66 64 60 Q58 66 50 60Z" fill="#fff" {s('stroke-width="2"')}/>
{eye(56, 40, 0.6)}{eye(70, 40, 0.6)}
<path d="M63 44 L76 40 L66 52Z" fill="#F5B53A" {s('stroke-width="2"')}/>
<path d="M63 44 L72 46 L66 52Z" fill="#C2365A"/>
{note(96, 22, 0.9)}{note(22, 30, 0.75, "#fff")}{note(108, 64, 0.6, "#fff")}
'''))

# 7 «Времена года» (эстрадный и народный танец с 3 лет): красные сапожки пляшут вприсядку по осенним листьям
I["vremena-goda-tekstilshchikov"] = ("пара красных народных сапожек с золотыми кисточками и мордашками на голенищах",
    "отплясывают вприсядку, лихо выбрасывая носок, по ковру из жёлтых и оранжевых кленовых листьев", bg("#FFF1D6", "#D9772B", f'''
<path d="M-4 104 Q64 96 132 104 V132 H-4Z" fill="#E9A23B" {s()}/>
<path d="M14 110 l6 -4 l6 4 l-2 6 h-8z M96 112 l6 -4 l6 4 l-2 6 h-8z M54 116 l5 -3 l5 3 l-2 5 h-6z" fill="#F7D046" {s('stroke-width="1.6"')}/>
<path d="M30 14 l7 -5 l7 5 l-3 7 h-8z M90 20 l6 -4 l6 4 l-2 6 h-8z" fill="#E35A2B" {s('stroke-width="1.6"')}/>
<path d="M24 34 H50 V80 Q50 92 40 94 L14 98 Q6 98 8 90 Q10 84 24 82Z" fill="#D9283A" {s()}/>
<path d="M24 34 H50 V42 H24Z" fill="#F5C542" {s('stroke-width="2.4"')}/>
<path d="M30 42 L28 52 M44 42 L46 52" {ln("#F5C542", 3)}/>
<path d="M44 96 L48 104 M18 98 L16 104" {ln(O, 3)}/>
{face(37, 64, 5, 0.5)}
<path d="M70 50 H96 V76 L118 82 Q124 86 120 92 L84 96 Q70 96 70 86Z" fill="#D9283A" {s()}/>
<path d="M70 50 H96 V58 H70Z" fill="#F5C542" {s('stroke-width="2.4"')}/>
<path d="M76 58 L74 68 M90 58 L92 68" {ln("#F5C542", 3)}/>
<path d="M78 96 L76 104" {ln(O, 3)}/>
{face(83, 78, 5, 0.5)}
{sparkle(62, 26, 4)}{sparkle(112, 44, 3)}
'''))

# 8 «Крылатые качели» (вокал с 5 лет, своя студия звукозаписи): студийный микрофон в наушниках качается на качелях
I["krylatye-kacheli-krasnogorsk"] = ("серебристый студийный микрофон-капсула в больших красных наушниках",
    "раскачивается на детских качелях, подвешенных к жёлтой звёздочке, и поёт, зажмурившись", bg("#E8E4FF", "#5B4FB8", f'''
<path d="M30 6 L40 96 M98 6 L88 96" {ln("#3B3355", 3)}/>
{sparkle(64, 14, 10, "#FFD43B")}
<path d="M30 6 Q64 0 98 6" fill="none" {ln("#3B3355", 2.4)}/>
<path d="M30 96 H98" {ln(O, 9)}/><path d="M30 96 H98" {ln("#E0A050", 5)}/>
<path d="M56 96 L52 110 M72 96 L76 110" {ln(O, 5)}/><path d="M56 96 L52 110 M72 96 L76 110" {ln("#B8BCC8", 2.5)}/>
<rect x="44" y="34" width="40" height="60" rx="20" fill="#D6DAE4" {s()}/>
<path d="M44 52 H84 M44 60 H84 M48 44 H80" stroke="#A8AEBE" stroke-width="2"/>
<path d="M40 60 Q36 26 64 24 Q92 26 88 60" fill="none" {ln(O, 7)}/><path d="M40 60 Q36 26 64 24 Q92 26 88 60" fill="none" {ln("#E8344E", 4)}/>
<rect x="32" y="52" width="14" height="22" rx="6" fill="#E8344E" {s()}/>
<rect x="82" y="52" width="14" height="22" rx="6" fill="#E8344E" {s()}/>
<path d="M56 70 Q59 67 62 70 M66 70 Q69 67 72 70" fill="none" {ln(O, 2.2)}/>
<ellipse cx="64" cy="80" rx="4" ry="4.5" fill="#C2365A" {s('stroke-width="1.8"')}/>
<ellipse cx="53" cy="76" rx="3" ry="1.8" fill="#FF7FA8" opacity=".7"/><ellipse cx="75" cy="76" rx="3" ry="1.8" fill="#FF7FA8" opacity=".7"/>
{note(108, 40, 0.8, "#fff")}{note(16, 52, 0.7, "#FFD43B")}
'''))

# 9 «Максимус» (Электросталь, группы 2–6 и 7–18 лет): большая и крошечная чешки — вид сверху, как следы
I["maximus-elektrostal"] = ("две танцевальные чешки — большая синяя и крошечная розовая, с мордашками на мысках",
    "стоят рядом носами вверх, как папа с дочкой, на светлом деревянном полу, с белыми резиночками", bg("#FFF8E8", "#E8B36A", f'''
<path d="M-4 20 H132 M-4 52 H132 M-4 84 H132 M-4 116 H132" stroke="#E2C08C" stroke-width="2"/>
<g transform="translate(48 66) rotate(-8) scale(1.25)">
<path d="M0 -40 Q16 -40 17 -18 Q18 6 12 26 Q8 40 0 40 Q-8 40 -12 26 Q-18 6 -17 -18 Q-16 -40 0 -40Z" fill="#3D7BE0" {s()}/>
<path d="M0 -14 Q11 -12 11 6 Q10 26 0 30 Q-10 26 -11 6 Q-11 -12 0 -14Z" fill="#1E3E7A" {s('stroke-width="2.2"')}/>
<path d="M-15 -4 Q0 -10 15 -4" fill="none" {ln("#fff", 3.4)}/>
{face(0, -26, 6, 0.5)}
</g>
<g transform="translate(94 84) rotate(10) scale(0.62)">
<path d="M0 -40 Q16 -40 17 -18 Q18 6 12 26 Q8 40 0 40 Q-8 40 -12 26 Q-18 6 -17 -18 Q-16 -40 0 -40Z" fill="#FF9FC4" {s()}/>
<path d="M0 -14 Q11 -12 11 6 Q10 26 0 30 Q-10 26 -11 6 Q-11 -12 0 -14Z" fill="#C2507E" {s('stroke-width="2.2"')}/>
<path d="M-15 -4 Q0 -10 15 -4" fill="none" {ln("#fff", 3.4)}/>
{face(0, -26, 6, 0.55)}
</g>
{sparkle(104, 26, 4.5)}{sparkle(18, 106, 3)}{sparkle(112, 52, 2.6)}
'''))

# 10 Студия Марии Рыковой (Коломна; дэнсхолл 10–13, хип-хоп 14+): девочка-подросток танцует дэнсхолл
I["rykova-dance-kolomna"] = ("девочка-подросток с высоким пучком в мешковатых зелёных штанах и жёлтом топе",
    "танцует дэнсхолл в глубоком полуприсяде, раскинув локти, на фоне жёлто-зелёных диагональных полос", bg("#F2FFD6", "#7FBF3A", f'''
<path d="M-10 40 L60 -10 H80 L-10 60Z M20 138 L140 50 V70 L40 138Z" fill="#FFD43B" opacity=".55"/>
<path d="M-10 80 L100 -10 H112 L-10 92Z" fill="#2E8C4A" opacity=".25"/>
<path d="M50 74 L34 96 L40 112 M78 74 L94 96 L88 112" fill="none" {ln(O, 15)}/>
<path d="M50 74 L34 96 L40 112 M78 74 L94 96 L88 112" fill="none" {ln("#3FA35B", 11)}/>
<path d="M30 114 H46 M82 114 H98" {ln(O, 7)}/><path d="M30 114 H46 M82 114 H98" {ln("#fff", 4)}/>
<path d="M50 52 H78 L80 76 H48Z" fill="#FFD43B" {s()}/>
{limb(52, 56, 32, 50, SKIN, 4.5)}{limb(32, 50, 28, 68, SKIN, 4.5)}
{limb(76, 56, 96, 50, SKIN, 4.5)}{limb(96, 50, 100, 68, SKIN, 4.5)}
<circle cx="64" cy="38" r="12" fill="#C98A5E" {s()}/>
<path d="M52 36 Q52 24 64 24 Q76 24 76 36 Q70 30 64 30 Q58 30 52 36Z" fill="#2A1E18" {s('stroke-width="2.2"')}/>
<circle cx="64" cy="18" r="7" fill="#2A1E18" {s('stroke-width="2.2"')}/>
{eye(59, 39, 0.5)}{eye(69, 39, 0.5)}<path d="M60 44 Q64 47.5 68 44" fill="none" {ln(O, 2)}/>
{sparkle(108, 22, 4)}{sparkle(18, 22, 3)}
'''))

# 11 «Музыкалка» (Коломна; гитара, укулеле, вокал с 4 лет): гитара встала вверх ногами и хохочет, из неё сыплются ноты
I["muzykalka-kolomna"] = ("медовая акустическая гитара с мордашкой на деке",
    "стоит вверх ногами на кончике грифа, хохочет, и из круглого резонатора высыпаются ноты", bg("#E6F6FF", "#3E9AD0", f'''
<path d="M0 116 H128 V128 H0Z" fill="#9AD0EE" {s()}/>
<rect x="58" y="80" width="12" height="36" rx="3" fill="#7A4A26" {s()}/>
<path d="M60 86 H68 M60 94 H68 M60 102 H68" stroke="#C9A06A" stroke-width="1.6"/>
<rect x="56" y="108" width="16" height="10" rx="3" fill="#5A341A" {s('stroke-width="2.4"')}/>
<path d="M64 80 Q40 80 38 60 Q38 48 46 44 Q36 36 38 24 Q42 8 64 8 Q86 8 90 24 Q92 36 82 44 Q90 48 90 60 Q88 80 64 80Z" fill="#F2B44C" {s()}/>
<circle cx="64" cy="52" r="8" fill="#5A341A" {s('stroke-width="2.4"')}/>
<path d="M54 22 H74" {ln(O, 5)}/><path d="M54 22 H74" {ln("#5A341A", 3)}/>
<path d="M60 22 V80 M64 22 V80 M68 22 V80" stroke="#FFF4D6" stroke-width="1" opacity=".9"/>
<path d="M52 36 Q55 32 58 36 M70 36 Q73 32 76 36" fill="none" {ln(O, 2.4)}/>
<ellipse cx="50" cy="42" rx="3.4" ry="2" fill="#FF7FA8" opacity=".7"/><ellipse cx="78" cy="42" rx="3.4" ry="2" fill="#FF7FA8" opacity=".7"/>
{note(28, 76, 0.85)}{note(100, 86, 0.9, "#fff")}{note(20, 100, 0.7, "#fff")}{note(96, 66, 0.6)}
{sparkle(108, 22, 4)}{sparkle(22, 30, 3)}
'''))

if __name__ == "__main__":
    if "--subjects" in sys.argv:
        for k, (h, sc, _) in I.items():
            print(f"{k} — герой: {h} | сцена: {sc}")
        sys.exit()
    for k, (_, _, svg) in I.items():
        open(os.path.join(ROOT, "icons-src", k + ".svg"), "w").write(svg)
    print(len(I))
