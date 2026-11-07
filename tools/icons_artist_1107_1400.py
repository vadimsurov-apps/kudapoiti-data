"""Робот «художник», 07.11 ~14:00 UTC: 40 иконок из самых похожих пар auto/icon-repeats.json
(старые серии «зверь плывёт по дорожке», «мяч-персонаж на пьедестале/у сетки», «блюдо дымится сердечками /
обедает с мишкой / из шляпы фокусника», неверные якоря у «Школы мяча» и «Льдинки»).
Из каждой пары одну оставили, вторую придумали заново и нарисовали вручную: свой герой, сцена, ракурс, палитра.
Запуск из корня: python3 tools/icons_artist_1107_1400.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}
SK = "#FFD8B8"


def limb(d, color=SK, w=6):
    return f'<path d="{d}" fill="none" {W(w)}/><path d="{d}" fill="none" stroke="{color}" stroke-width="{w-3.4:.1f}" stroke-linecap="round"/>'


# 1. MURENA (СК «Умка») — синхронное плавание: из воды «перископом» торчит одна прямая ножка
I["murena-umka"] = ("девочка-синхронистка, видна только вытянутая ножка с оттянутым носочком", "делает «перископ» — поднимает над водой прямую ножку, вокруг расходятся круги и блёстки", ("#F3EAFF", "#8A62D0"), f'''
<path d="M0 76 Q16 70 32 76 T64 76 T96 76 T128 76 V128 H0Z" fill="#5AB8F0" {W(2.6)}/>
<ellipse cx="64" cy="84" rx="44" ry="10" fill="none" stroke="#fff" stroke-width="1.8" opacity=".7"/>
<ellipse cx="64" cy="82" rx="26" ry="6" fill="none" stroke="#fff" stroke-width="2.6"/>
<path d="M53 82 L57 34 L58 22 Q60 14 68 8 Q76 4 76 10 Q72 16 70 24 L71 34 L75 82Z" fill="{SK}" {W(3)}/><path d="M58 24 Q64 28 70 24" fill="none" stroke="#E8B090" stroke-width="1.8"/>
<path d="M58 54 Q64 58 70 54" fill="none" stroke="#E8B090" stroke-width="2"/>
<path d="M50 80 Q64 70 78 80 Q64 88 50 80Z" fill="#E040A0" {W(2.6)}/>
<circle cx="58" cy="78" r="1.6" fill="#fff"/><circle cx="66" cy="76" r="1.6" fill="#fff"/><circle cx="72" cy="79" r="1.6" fill="#fff"/>
{sparkle(88, 8, 4)}{sparkle(90, 32, 5)}{sparkle(42, 40, 4)}{sparkle(98, 58, 3)}
<path d="M20 100 Q26 96 32 100 M96 104 Q102 100 108 104" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 2. «Про.Плыть» (Широкая) — мальчик-ватерполист выпрыгнул из воды и бросает мяч в плавающие ворота
I["proplyt-shirokaya"] = ("мальчик-ватерполист в синей шапочке с наушниками-защитой", "выпрыгнул из воды по пояс и замахнулся жёлтым мячом на плавающие ворота", ("#E2ECFF", "#2048A8"), f'''
<path d="M92 56 H124 V86 H92Z" fill="none" {W(3)}/><path d="M92 56 H124" stroke="#E83A3A" stroke-width="5"/>
<path d="M98 58 V86 M106 58 V86 M114 58 V86 M92 66 H124 M92 76 H124" stroke="#fff" stroke-width="1.4"/>
<path d="M92 56 V86 M124 56 V86" {W(3)}/>
{limb("M58 66 L70 44 L78 26", SK, 7)}{limb("M40 70 L24 62", SK, 7)}
<path d="M36 92 Q36 64 50 62 Q64 64 64 92Z" fill="{SK}" {W(3)}/>
<circle cx="80" cy="20" r="11" fill="#FFD23A" {W(2.8)}/><path d="M70 18 Q80 24 90 18 M78 9 Q82 20 78 31" fill="none" stroke="#2A5AC8" stroke-width="2.2"/>
<circle cx="50" cy="48" r="13" fill="{SK}" {W(3)}/>
<path d="M37 46 Q37 32 50 32 Q63 32 63 46 Q50 40 37 46Z" fill="#2A4AB8" {W(2.4)}/>
<circle cx="38" cy="50" r="4" fill="#2A4AB8" {W(2)}/><circle cx="62" cy="50" r="4" fill="#2A4AB8" {W(2)}/>
{eye(46, 49, .45)}{eye(54, 49, .45)}<path d="M46 55 Q50 59 54 55" fill="none" {W(2)}/>
<path d="M0 88 Q14 82 28 88 T56 88 T84 88 T112 88 T140 88 V128 H0Z" fill="#3A8AE0" {W(2.6)}/>
<path d="M26 86 Q32 78 38 84 M60 84 Q66 76 72 82" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M14 104 Q20 100 26 104 M84 108 Q90 104 96 108" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>''')

# 3. RusVolley (Дмитровское ш.) — девочка-судья на высокой судейской вышке свистит, мяч над сеткой
I["rusvolley-dmitrovskoe"] = ("девочка-судья в полосатой рубашке на высокой судейской вышке", "у края волейбольной сетки дует в свисток и показывает рукой подачу", ("#FFF4D6", "#D89A20"), f'''
<path d="M54 50 H128 V78 H54Z" fill="none"/>
<path d="M56 52 H128" stroke="#fff" stroke-width="5"/><path d="M56 52 H128" {W(1.6)}/>
<path d="M60 56 H128 M60 62 H128 M60 68 H128 M60 74 H128 M66 52 V78 M76 52 V78 M86 52 V78 M96 52 V78 M106 52 V78 M116 52 V78 M126 52 V78" stroke="#3B3355" stroke-width="1" opacity=".55"/>
<path d="M58 48 V122" {W(4.2)}/>
<circle cx="96" cy="28" r="12" fill="#fff" {W(2.8)}/><path d="M86 24 Q96 30 106 24 M94 16 Q100 28 94 40" fill="none" stroke="#2A8AE0" stroke-width="2.2"/>
<path d="M18 80 L22 122 M46 80 L42 122 M20 100 H44" {W(3.6)}/>
<path d="M14 76 H50 V82 H14Z" fill="#8A5A30" {W(2.6)}/>
<path d="M22 76 Q20 58 32 54 Q44 58 42 76Z" fill="#fff" {W(2.8)}/>
<path d="M26 58 V76 M32 55 V76 M38 58 V76" stroke="#2A2A3A" stroke-width="2.2"/>
{limb("M40 62 L52 50 L60 38", SK, 6)}
<circle cx="32" cy="42" r="11" fill="{SK}" {W(2.8)}/>
<path d="M21 40 Q22 28 32 28 Q44 28 43 40 Q38 34 30 35 Q24 36 21 40Z" fill="#A0522D" {W(2)}/>
<path d="M42 36 Q50 34 48 42" fill="#A0522D" {W(2)}/>
{eye(28, 42, .4)}{eye(35, 42, .4)}
<rect x="34" y="46" width="9" height="5" rx="2" fill="#C0C8D8" {W(1.8)}/>
<path d="M46 44 Q50 40 54 42 M46 48 Q52 48 55 50" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"/>''')

# 4. Открытый бассейн в Измайловском парке — мальчик в панаме сидит на бортике и болтает ногами в воде
I["pool-izmaylovo"] = ("мальчик в белой панамке и полосатых плавках", "сидит на бортике открытого бассейна под кронами парка и болтает ногами в воде — брызги", ("#F2FFE2", "#4E9A3A"), f'''
<circle cx="10" cy="20" r="22" fill="#5AB84A" {W(2.6)}/><circle cx="30" cy="8" r="16" fill="#6CC85A" {W(2.4)}/>
<circle cx="118" cy="22" r="22" fill="#5AB84A" {W(2.6)}/><circle cx="100" cy="6" r="14" fill="#6CC85A" {W(2.4)}/>
<path d="M0 74 H128 V84 H0Z" fill="#fff" {W(2.4)}/><path d="M16 74 V84 M32 74 V84 M48 74 V84 M80 74 V84 M96 74 V84 M112 74 V84" stroke="#B8C8D0" stroke-width="1.6"/>
<path d="M0 84 H128 V128 H0Z" fill="#48B0E8" {W(2.4)}/>
<path d="M10 100 Q18 96 26 100 M96 104 Q104 100 112 104" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
{limb("M58 74 L52 90 L46 98", SK, 7)}{limb("M70 74 L78 88 L86 92", SK, 7)}
<circle cx="44" cy="90" r="2.4" fill="#fff"/><circle cx="40" cy="84" r="2" fill="#fff"/><circle cx="90" cy="84" r="2.4" fill="#fff"/><circle cx="94" cy="90" r="2" fill="#fff"/><circle cx="86" cy="80" r="1.8" fill="#fff"/>
<path d="M52 66 H76 V76 H52Z" fill="#E84A4A" {W(2.6)}/><path d="M52 70 H76" stroke="#fff" stroke-width="2"/>
<path d="M52 66 Q50 48 64 46 Q78 48 76 66Z" fill="{SK}" {W(2.8)}/>
{limb("M54 54 L44 66", SK, 6)}{limb("M74 54 L84 66", SK, 6)}
<circle cx="64" cy="36" r="12" fill="{SK}" {W(2.8)}/>
<path d="M46 32 Q48 20 64 18 Q80 20 82 32 Z" fill="#fff" {W(2.6)}/><path d="M48 30 H80" stroke="#E8E0C8" stroke-width="2"/>
{eye(59, 38, .42)}{eye(69, 38, .42)}<path d="M60 43 Q64 47 68 43" fill="none" {W(2)}/>{blush(55, 42, .35)}{blush(73, 42, .35)}''')

# 5. «Грузинский сыр» — головка сулугуни распустила нарезанные ломтики веером, как павлиний хвост
I["cafe-gruzinskiy-syr"] = ("круглая головка сыра сулугуни", "распустила за спиной тонкие ломтики сыра веером, как павлин хвост, и гордо позирует на дощечке", ("#FFF8E8", "#B08A50"), f'''
<path d="M14 104 H114 Q118 104 118 108 V114 Q118 118 114 118 H14 Q10 118 10 114 V108 Q10 104 14 104Z" fill="#C8884A" {W(2.8)}/>
<path d="M118 110 H126" {W(4)}/>
<path d="M64 84 L18 52 Q14 64 20 74Z" fill="#FFF3CC" {W(2.4)}/>
<path d="M64 84 L26 30 Q18 40 20 52Z" fill="#FFEFC0" {W(2.4)}/>
<path d="M64 84 L44 16 Q34 20 28 30Z" fill="#FFF3CC" {W(2.4)}/>
<path d="M64 84 L64 12 Q54 12 46 16Z" fill="#FFEFC0" {W(2.4)}/>
<path d="M64 84 L84 16 Q74 12 64 12Z" fill="#FFF3CC" {W(2.4)}/>
<path d="M64 84 L102 30 Q94 20 84 16Z" fill="#FFEFC0" {W(2.4)}/>
<path d="M64 84 L110 52 Q110 40 102 30Z" fill="#FFF3CC" {W(2.4)}/>
<path d="M64 84 L108 74 Q114 64 110 52Z" fill="#FFEFC0" {W(2.4)}/>
<circle cx="32" cy="46" r="2.6" fill="#E8C878"/><circle cx="54" cy="24" r="2.6" fill="#E8C878"/><circle cx="76" cy="24" r="2.6" fill="#E8C878"/><circle cx="98" cy="46" r="2.6" fill="#E8C878"/>
<ellipse cx="64" cy="86" rx="28" ry="20" fill="#FFF8E0" {W(3)}/>
<path d="M40 80 Q64 70 88 80" fill="none" stroke="#F0DCA8" stroke-width="2.4"/>
{eye(56, 88, .55)}{eye(72, 88, .55)}{smile(64, 96, 4, .8)}{blush(48, 96, .45)}{blush(80, 96, .45)}''')

# 6. «Ели Сацебели» — грузинский хлеб шоти плывёт, как каноэ, по красной реке соуса сацебели
I["cafe-eli-satsebeli"] = ("золотистый грузинский хлеб шоти в форме каноэ", "плывёт по красной реке соуса сацебели и гребёт веточкой кинзы, как веслом", ("#FFE8E0", "#B8402A"), f'''
<path d="M0 78 Q20 70 40 78 T80 78 T120 78 T160 78 V128 H0Z" fill="#D8402A" {W(2.6)}/>
<path d="M12 98 Q22 92 32 98 M90 104 Q100 98 110 104 M50 114 Q58 110 66 114" fill="none" stroke="#FF8A6A" stroke-width="2.6" stroke-linecap="round"/>
<path d="M10 70 Q64 98 118 70 Q104 54 64 56 Q24 54 10 70Z" fill="#E8B060" {W(3)}/>
<path d="M30 64 L38 70 M48 60 L56 68 M68 60 L76 68 M88 62 L96 70" stroke="#B8782A" stroke-width="2.4" stroke-linecap="round"/>
{eye(56, 74, .5)}{eye(70, 74, .5)}{smile(63, 81, 4, .7)}{blush(48, 80, .4)}{blush(78, 80, .4)}
<path d="M86 66 L106 98" {W(3.6)}/><path d="M86 66 L106 98" stroke="#6A9A3A" stroke-width="1.6"/>
<path d="M104 94 Q112 92 112 100 Q106 104 104 94Z M100 90 Q94 92 98 98 Q104 96 100 90Z M108 102 Q116 106 110 112 Q104 108 108 102Z" fill="#5AB040" {W(1.8)}/>
<path d="M20 38 Q24 30 30 36 M100 30 Q106 24 112 30" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 7. Нияма (Реутов) — по ленте кайтен едут три тарелочки с суши, на средней суши машет
I["cafe-niyama-reutov"] = ("тарелочки с суши на ленте кайтен", "едут по конвейерной ленте друг за другом, нигири на средней красной тарелочке машет посетителям", ("#EAF6F2", "#3A7A6A"), f'''
<path d="M-4 78 H132 V96 H-4Z" fill="#5A6070" {W(2.8)}/>
<path d="M10 78 V96 M30 78 V96 M50 78 V96 M70 78 V96 M90 78 V96 M110 78 V96" stroke="#7A8090" stroke-width="2"/>
<path d="M-4 96 H132 V104 H-4Z" fill="#3A4050" {W(2.4)}/>
<ellipse cx="18" cy="76" rx="16" ry="5" fill="#2A8AE0" {W(2.4)}/>
<circle cx="18" cy="66" r="9" fill="#fff" {W(2.4)}/><circle cx="18" cy="66" r="9" fill="none" stroke="#2A3A2A" stroke-width="4"/><circle cx="18" cy="66" r="4" fill="#FF8A5A"/>
<ellipse cx="64" cy="76" rx="22" ry="6" fill="#E83A3A" {W(2.6)}/>
<path d="M46 72 Q46 56 64 56 Q82 56 82 72Z" fill="#fff" {W(2.6)}/>
<path d="M44 60 Q50 44 64 46 Q80 44 86 60 Q76 54 64 56 Q52 54 44 60Z" fill="#FF8A5A" {W(2.6)}/>
<path d="M54 52 L58 56 M66 50 L70 55 M76 52 L78 56" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
{eye(58, 64, .45)}{eye(70, 64, .45)}{smile(64, 68, 3, .6)}
{limb("M82 64 L92 52", "#fff", 5.4)}
<ellipse cx="112" cy="76" rx="16" ry="5" fill="#FFC83A" {W(2.4)}/>
<path d="M100 72 Q100 62 112 62 Q124 62 124 72Z" fill="#FFE07A" {W(2.4)}/><path d="M102 68 H122" stroke="#2A3A2A" stroke-width="3"/>
<path d="M30 44 H40 M26 50 H38 M92 40 H104" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 8. RusVolley (Дубининская) — двое детей в прыжке ставят блок над сеткой
I["rusvolley-dubininskaya"] = ("мальчик и девочка в малиновой форме", "вдвоём в прыжке ставят блок над волейбольной сеткой, мяч отскакивает от их ладошек", ("#FFE6EE", "#D0386A"), f'''
<circle cx="64" cy="14" r="11" fill="#fff" {W(2.8)}/><path d="M54 10 Q64 18 74 10 M62 3 Q68 14 62 25" fill="none" stroke="#E8384A" stroke-width="2.2"/>
<path d="M54 22 L50 26 M74 22 L78 26" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{limb("M38 60 L32 30", SK, 6.4)}{limb("M52 60 L54 30", SK, 6.4)}{limb("M76 60 L74 30", SK, 6.4)}{limb("M90 60 L96 30", SK, 6.4)}
<ellipse cx="31" cy="26" rx="5" ry="6" fill="{SK}" {W(2.4)}/><ellipse cx="55" cy="26" rx="5" ry="6" fill="{SK}" {W(2.4)}/>
<ellipse cx="73" cy="26" rx="5" ry="6" fill="{SK}" {W(2.4)}/><ellipse cx="97" cy="26" rx="5" ry="6" fill="{SK}" {W(2.4)}/>
<path d="M30 100 Q30 70 44 68 Q58 70 58 100Z" fill="#D0386A" {W(2.8)}/><path d="M70 100 Q70 70 84 68 Q98 70 98 100Z" fill="#D0386A" {W(2.8)}/>
<circle cx="45" cy="52" r="11" fill="{SK}" {W(2.8)}/><path d="M34 50 Q34 40 45 40 Q56 40 56 50 Q46 44 34 50Z" fill="#3A2A20" {W(2)}/>
{eye(41, 54, .4)}{eye(49, 54, .4)}<path d="M42 59 Q45 61 48 59" fill="none" {W(1.8)}/>
<circle cx="83" cy="52" r="11" fill="{SK}" {W(2.8)}/><path d="M72 52 Q70 38 83 40 Q96 38 94 52 Q90 44 83 46 Q76 44 72 52Z" fill="#E8A030" {W(2)}/>
<path d="M94 46 Q102 50 100 60" fill="none" stroke="#E8A030" stroke-width="4" stroke-linecap="round"/>
{eye(79, 54, .4)}{eye(87, 54, .4)}<path d="M80 59 Q83 61 86 59" fill="none" {W(1.8)}/>
<path d="M-4 66 H132" stroke="#fff" stroke-width="6"/><path d="M-4 63 H132 M-4 69 H132" {W(1.4)}/>
<path d="M-4 76 H132 M-4 84 H132 M-4 92 H132 M-4 100 H132 M-4 108 H132 M4 69 V128 M16 69 V128 M28 69 V128 M40 69 V128 M52 69 V128 M64 69 V128 M76 69 V128 M88 69 V128 M100 69 V128 M112 69 V128 M124 69 V128" stroke="#3B3355" stroke-width="1.2" opacity=".6"/>''')

# 9. «Журавли» (Красногорск) — кусочек торта «Наполеон» в треуголке Наполеона
I["cafe-zhuravli-krasnogorsk"] = ("высокий кусок торта «Наполеон» со слоями крема и крошкой", "надел чёрную треуголку Наполеона и важно заложил руку за пазуху крема", ("#FFF1D8", "#2A3A6A"), f'''
<ellipse cx="64" cy="112" rx="48" ry="9" fill="#fff" {W(2.8)}/>
<path d="M30 52 H98 V108 H30Z" fill="#F2C680" {W(3)}/>
<path d="M30 62 H98 M30 74 H98 M30 86 H98 M30 98 H98" stroke="#FFF6E0" stroke-width="5"/>
<path d="M30 52 H98" {W(3)}/>
<g fill="#E8B060"><circle cx="40" cy="50" r="2.4"/><circle cx="52" cy="48" r="2"/><circle cx="66" cy="50" r="2.6"/><circle cx="80" cy="48" r="2"/><circle cx="92" cy="50" r="2.4"/></g>
<path d="M22 40 Q40 18 64 26 Q88 18 106 40 Q88 34 64 40 Q40 34 22 40Z" fill="#2A2A3A" {W(2.8)}/>
<path d="M30 38 Q64 30 98 38" fill="none" stroke="#D8B040" stroke-width="2.4"/>
<circle cx="64" cy="30" r="4" fill="#fff" {W(1.6)}/><circle cx="64" cy="30" r="2" fill="#2A5AC8"/><circle cx="64" cy="30" r="5.6" fill="none" stroke="#E8384A" stroke-width="1.6"/>
{eye(54, 78, .55)}{eye(74, 78, .55)}<path d="M58 90 Q64 87 70 90" fill="none" {W(2.4)}/>{blush(46, 86, .45)}{blush(82, 86, .45)}
<path d="M98 80 Q110 80 106 92 Q102 96 96 94" fill="{SK}" {W(2.4)}/>''')

# 10. Музей истории Лобни — расписная русская прялка с куделью стоит на музейном постаменте
I["lobnya-museum"] = ("старинная расписная прялка с пучком кудели", "стоит в стеклянной музейной витрине на постаменте с табличкой, с кудели свисает веретено с ниткой", ("#F6EEE2", "#7A5A3A"), f'''
<path d="M22 98 H106 V126 H22Z" fill="#8A5A30" {W(3)}/>
<rect x="50" y="106" width="28" height="10" rx="2" fill="#F0D890" {W(2)}/><path d="M55 111 H73" stroke="#8A6A30" stroke-width="1.6"/>
<rect x="22" y="8" width="84" height="90" rx="6" fill="#EAF6FF" opacity=".55"/>
<path d="M32 86 H98 V94 H32Z" fill="#C88A4A" {W(2.6)}/>
<path d="M60 86 V68 H70 V86Z" fill="#C88A4A" {W(2.6)}/>
<path d="M46 68 Q42 44 46 24 L50 24 Q52 18 56 24 Q59 18 62 24 Q65 18 68 24 Q71 18 74 24 Q77 18 80 24 L84 24 Q88 44 84 68Z" fill="#D8303A" {W(3)}/>
<circle cx="65" cy="40" r="8" fill="#FFD23A" {W(2)}/><circle cx="65" cy="40" r="3" fill="#D8303A"/>
<path d="M52 30 Q56 26 60 30 M70 30 Q74 26 78 30" fill="none" stroke="#FFD23A" stroke-width="2.2"/>
{eye(58, 56, .45)}{eye(72, 56, .45)}{smile(65, 61, 3, .6)}
<path d="M44 26 Q30 22 30 34 Q26 44 36 46 Q46 48 48 38Z" fill="#F4F0E6" {W(2.4)}/>
<path d="M34 46 L36 62" stroke="#F4F0E6" stroke-width="1.6"/><path d="M34 46 L36 62" {W(.8)}/>
<path d="M36 60 L33 72 L36 84 L39 72Z" fill="#E8C080" {W(2)}/><ellipse cx="36" cy="68" rx="4.4" ry="2.6" fill="#F4F0E6" {W(1.4)}/>
<rect x="22" y="8" width="84" height="90" rx="6" fill="none" stroke="#fff" stroke-width="3"/><rect x="22" y="8" width="84" height="90" rx="6" fill="none" {W(1.4)}/>
<path d="M92 16 L100 26 M88 22 L100 36" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 11. RusVolley (Новокосинская) — детские ладошки делают передачу сверху, мяч над ними
I["rusvolley-novokosinskaya"] = ("две детские ладошки в бирюзовых рукавах", "сложили «домик» и делают пас сверху — волейбольный мяч взлетает над ними", ("#E8FBFF", "#2AA0C8"), f'''
<circle cx="64" cy="36" r="22" fill="#fff" {W(3)}/>
<path d="M44 28 Q64 42 84 28 M60 14 Q72 34 60 58 M44 46 Q62 44 78 54" fill="none" stroke="#FFC83A" stroke-width="3.4"/>
<path d="M44 28 Q64 42 84 28 M60 14 Q72 34 60 58 M44 46 Q62 44 78 54" fill="none" stroke="#2A6AD8" stroke-width="1.2"/>
{eye(58, 34, .5)}{eye(70, 34, .5)}{smile(64, 42, 3.4, .7)}
<path d="M38 18 L32 12 M90 18 L96 12 M64 4 V0" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
<path d="M2 128 L28 92 L44 100 L24 132Z" fill="#2AB8B0" {W(3)}/><path d="M126 128 L100 92 L84 100 L104 132Z" fill="#2AB8B0" {W(3)}/>
<path d="M28 92 Q30 80 38 74 L42 66 Q46 64 47 68 L46 74 L52 66 Q56 64 57 68 L54 78 L56 80 Q52 92 44 100Z" fill="{SK}" {W(2.6)}/>
<path d="M100 92 Q98 80 90 74 L86 66 Q82 64 81 68 L82 74 L76 66 Q72 64 71 68 L74 78 L72 80 Q76 92 84 100Z" fill="{SK}" {W(2.6)}/>
<path d="M38 74 L36 66 Q37 62 40 64 M90 74 L92 66 Q91 62 88 64" fill="none" {W(2.4)}/>''')

# 12. Открытый бассейн в Строгине — девочка ныряет «рыбкой» с бортика, на закате
I["pool-moskvoretsky"] = ("девочка в розовом купальнике с рюшами", "ныряет «рыбкой» с бортика открытого бассейна, вытянув руки вперёд, вечернее солнце садится", ("#FFEFE0", "#E87A3A"), f'''
<circle cx="100" cy="30" r="14" fill="#FFE07A" opacity=".9"/>
<path d="M0 70 H36 V128 H0Z" fill="#fff" {W(2.6)}/><path d="M0 84 H36 M0 98 H36 M0 112 H36 M12 70 V128 M24 70 V128" stroke="#C8D0D8" stroke-width="1.4"/>
<path d="M36 82 Q56 76 76 82 T116 82 T156 82 V128 H36Z" fill="#3AA8E8" {W(2.6)}/>
<path d="M50 100 Q58 96 66 100 M96 108 Q104 104 112 108" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
{limb("M34 50 L18 42 L8 46", SK, 6.6)}{limb("M34 54 L20 52 L10 58", SK, 6.6)}
<path d="M30 46 Q50 44 70 62 Q64 70 56 66 Q42 58 30 58Z" fill="#FF7FA8" {W(2.8)}/>
<path d="M38 56 Q42 62 46 56 Q50 64 54 58" fill="none" stroke="#fff" stroke-width="2"/>
{limb("M66 60 L84 74 L94 82", SK, 6.4)}{limb("M62 64 L80 78 L92 86", SK, 6.4)}
<circle cx="72" cy="56" r="10" fill="{SK}" {W(2.8)}/><path d="M64 50 Q70 44 80 50 Q82 56 80 60 Q74 52 64 50Z" fill="#6A3A20" {W(2)}/>
<path d="M64 52 Q56 48 58 42" fill="none" stroke="#6A3A20" stroke-width="4" stroke-linecap="round"/>
{eye(73, 58, .38)}<path d="M74 63 Q77 64 79 62" fill="none" {W(1.6)}/>
<circle cx="98" cy="74" r="2.4" fill="#fff"/><circle cx="104" cy="70" r="1.8" fill="#fff"/>''')

# 13. Открытый бассейн в Некрасовке — малыш в лягушатнике хохочет и шлёпает ладошками по воде
I["pool-nekrasovka"] = ("кудрявый малыш в бирюзовых плавках", "сидит в мелком лягушатнике, хохочет и шлёпает ладошками по воде — брызги летят во все стороны", ("#E2FFF6", "#14A08A"), f'''
<path d="M0 82 Q32 76 64 82 T128 82 V128 H0Z" fill="#6AD0F0" {W(2.6)}/>
<path d="M44 84 Q64 90 84 84" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M48 84 Q46 64 64 62 Q82 64 80 84Z" fill="{SK}" {W(2.8)}/>
{limb("M50 70 L34 76 L26 74", SK, 6.6)}{limb("M78 70 L94 76 L102 74", SK, 6.6)}
<circle cx="22" cy="62" r="3" fill="#fff" {W(1.4)}/><circle cx="16" cy="70" r="2.4" fill="#fff" {W(1.4)}/><circle cx="30" cy="58" r="2" fill="#fff" {W(1.4)}/><circle cx="12" cy="80" r="2" fill="#fff" {W(1.4)}/>
<circle cx="106" cy="62" r="3" fill="#fff" {W(1.4)}/><circle cx="112" cy="70" r="2.4" fill="#fff" {W(1.4)}/><circle cx="98" cy="58" r="2" fill="#fff" {W(1.4)}/><circle cx="116" cy="80" r="2" fill="#fff" {W(1.4)}/>
<path d="M18 70 Q14 60 22 54 M110 70 Q114 60 106 54" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="64" cy="46" r="17" fill="{SK}" {W(3)}/>
<path d="M48 40 Q46 28 54 30 Q56 22 64 26 Q72 22 74 30 Q82 28 80 40 Q76 34 70 36 Q64 32 58 36 Q52 34 48 40Z" fill="#E8A040" {W(2.2)}/>
<path d="M55 46 Q58 42 61 46 M67 46 Q70 42 73 46" fill="none" {W(2.4)}/>
<path d="M56 52 Q64 64 72 52Z" fill="#C83A4A" {W(2.2)}/>{blush(52, 54, .45)}{blush(76, 54, .45)}''')

# 14. MiMi (Строгино) — облако розовой сахарной ваты на палочке
I["cafe-mimi-strogino"] = ("пушистое облако розовой сахарной ваты на палочке", "парит над палочкой, как облачко, и сыплет вокруг сахарные искорки", ("#E8FFF2", "#4AC08A"), f'''
<path d="M64 124 L64 76" {W(5)}/><path d="M64 124 L64 76" stroke="#F4F0E6" stroke-width="2"/>
<circle cx="40" cy="58" r="17" fill="#FFB0D8" {W(3)}/><circle cx="88" cy="58" r="17" fill="#FFB0D8" {W(3)}/>
<circle cx="52" cy="38" r="18" fill="#FFB0D8" {W(3)}/><circle cx="78" cy="36" r="18" fill="#FFB0D8" {W(3)}/>
<circle cx="64" cy="62" r="22" fill="#FFB0D8" {W(3)}/>
<g fill="#FFB0D8"><circle cx="40" cy="58" r="14.5"/><circle cx="88" cy="58" r="14.5"/><circle cx="52" cy="38" r="15.5"/><circle cx="78" cy="36" r="15.5"/><circle cx="64" cy="52" r="20"/></g>
<path d="M44 46 Q50 40 56 44 M74 30 Q80 26 86 30 M36 64 Q40 60 44 62" fill="none" stroke="#FFD8EC" stroke-width="2.6" stroke-linecap="round"/>
{eye(56, 56, .55)}{eye(72, 56, .55)}{smile(64, 64, 4, .8)}{blush(48, 63, .45)}{blush(80, 63, .45)}
{sparkle(20, 30, 4)}{sparkle(108, 28, 4.4)}{sparkle(22, 92, 3)}{sparkle(104, 94, 3.4)}''')

# 15. Москино «Юность» — коробка попкорна смотрит кино в тёмном зале, зёрнышко подпрыгивает
I["moskino-yunost"] = ("красно-белая полосатая коробка попкорна", "сидит в тёмном кинозале в луче проектора, от восторга из неё выпрыгивает зёрнышко", ("#4A4A7A", "#141430"), f'''
<path d="M-4 -4 L40 -4 L128 70 L128 108Z" fill="#FFF6C8" opacity=".22"/>
<path d="M36 62 H92 L84 120 H44Z" fill="#fff" {W(3)}/>
<path d="M46 62 L50 120 M58 62 L60 120 M70 62 L68 120 M82 62 L78 120" stroke="#E8384A" stroke-width="5"/>
<path d="M36 62 H92 L84 120 H44Z" fill="none" {W(3)}/>
<g fill="#FFF4C8" {W(2.2)}><circle cx="42" cy="58" r="8"/><circle cx="54" cy="52" r="9"/><circle cx="68" cy="50" r="9"/><circle cx="82" cy="54" r="8"/><circle cx="90" cy="60" r="6"/><circle cx="62" cy="40" r="7"/><circle cx="48" cy="44" r="6"/><circle cx="76" cy="42" r="6"/></g>
<g fill="#FFD25A"><circle cx="54" cy="54" r="2.4"/><circle cx="70" cy="48" r="2"/><circle cx="62" cy="42" r="2"/></g>
<path d="M44 76 H84 V98 H46Z" fill="#fff"/>
{eye(56, 84, .55)}{eye(72, 84, .55)}<ellipse cx="64" cy="93" rx="4" ry="3.6" fill="{O}"/>{blush(50, 92, .4)}{blush(78, 92, .4)}
<circle cx="96" cy="24" r="6" fill="#FFF4C8" {W(2)}/><path d="M92 34 Q88 40 86 46 M100 34 Q104 40 102 44" fill="none" stroke="#fff" stroke-width="1.8" stroke-dasharray="2 3"/>
{sparkle(24, 96, 3, "#FFE07A")}{sparkle(108, 92, 3.4, "#FFE07A")}''')

# 16. No Drama Mama (Зеленоград) — слойка-конвертик раскрыла уголки и показывает вишнёвое сердечко
I["cafe-no-drama-mama"] = ("слойка-конвертик с вишнёвым вареньем", "раскрыла уголки, как письмо, и показывает начинку — вишенки сердечком", ("#FFF6E0", "#E0B040"), f'''
<ellipse cx="64" cy="108" rx="50" ry="10" fill="#fff" {W(2.8)}/>
<path d="M64 22 L108 64 L64 106 L20 64Z" fill="#F2B860" {W(3)}/>
<path d="M64 22 L80 52 L64 58 L48 52Z" fill="#F8D088" {W(2.6)}/>
<path d="M108 64 L78 78 L72 64 L80 52Z" fill="#F8D088" {W(2.6)}/>
<path d="M20 64 L50 78 L56 64 L48 52Z" fill="#F8D088" {W(2.6)}/>
<path d="M64 76 Q52 64 58 58 Q64 56 64 62 Q64 56 70 58 Q76 64 64 76Z" fill="#C8203A" {W(2.4)}/>
<circle cx="61" cy="62" r="1.6" fill="#fff"/>
<path d="M64 106 L50 80 L64 76 L78 80Z" fill="#F8D088" {W(2.6)}/>
{eye(58, 88, .45)}{eye(70, 88, .45)}{smile(64, 94, 3, .6)}
<path d="M30 30 Q34 22 40 28 M88 26 Q94 20 98 26" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<g fill="#fff"><circle cx="40" cy="48" r="1.6"/><circle cx="90" cy="46" r="1.6"/><circle cx="34" cy="80" r="1.4"/><circle cx="94" cy="82" r="1.4"/></g>''')

# 17. Manta Club — папа плывёт под водой, как скат-манта, а малыш едет у него на спине
I["manta-club"] = ("папа-пловец в синей шапочке и очках", "плывёт под водой широким брассом, как скат-манта, а малыш в жёлтой шапочке едет у него на спине", ("#DDF0FF", "#1A6AB0"), f'''
<path d="M-4 20 Q16 14 36 20 T76 20 T116 20 T156 20 V-4 H-4Z" fill="#fff" opacity=".5"/>
<path d="M0 22 Q20 16 40 22 T80 22 T120 22 T160 22" fill="none" stroke="#fff" stroke-width="2.4"/>
{limb("M98 82 L116 66 L124 74", SK, 7)}{limb("M98 88 L118 100 L126 94", SK, 7)}
{limb("M30 80 L12 72 L4 78", SK, 7)}{limb("M30 86 L12 96 L4 92", SK, 7)}
<path d="M26 82 Q30 70 60 70 Q92 70 100 84 Q90 94 60 94 Q32 94 26 82Z" fill="{SK}" {W(3)}/><path d="M28 76 Q34 70 44 70 L46 94 Q32 92 26 84Z" fill="#2A4A9A" {W(2.6)}/>
<circle cx="104" cy="82" r="11" fill="{SK}" {W(2.8)}/><path d="M96 74 Q104 68 114 76 L112 80 Q104 74 96 78Z" fill="#1A3A8A" {W(2)}/>
<circle cx="108" cy="82" r="4" fill="#9AD8FF" {W(1.8)}/>
<path d="M48 70 Q48 56 62 54 Q74 56 74 70Z" fill="#FF8A5A" {W(2.6)}/>
{limb("M70 62 L84 66 L94 74", SK, 5.6)}
<circle cx="66" cy="46" r="10" fill="{SK}" {W(2.6)}/><path d="M56 44 Q58 34 66 34 Q76 34 76 44 Q66 38 56 44Z" fill="#FFD23A" {W(2)}/>
{eye(64, 48, .4)}{eye(71, 48, .4)}<path d="M64 53 Q68 56 72 53" fill="none" {W(1.8)}/>
<circle cx="116" cy="56" r="3" fill="#fff" {W(1.4)}/><circle cx="110" cy="46" r="2.4" fill="#fff" {W(1.4)}/><circle cx="118" cy="38" r="1.8" fill="#fff" {W(1.4)}/>
<path d="M20 110 Q28 104 36 110 M70 114 Q78 108 86 114" fill="none" stroke="#7AC0F0" stroke-width="2.4" stroke-linecap="round"/>''')

# 18. Пляжный волейбол «Жара» (Кубинка) — девочка в кепке подаёт снизу на песке у моря
I["beach-volleyball-school-zhara-kubinka"] = ("девочка в красной кепке и купальнике на горячем песке", "подаёт мяч снизу на пляже у синего моря, мяч взлетает к солнцу", ("#FFF9D0", "#F0C030"), f'''
<circle cx="104" cy="22" r="13" fill="#FF9A2A" {W(2.4)}/>
<path d="M0 78 H128 V94 H0Z" fill="#2A8AD8" {W(2.4)}/><path d="M10 84 Q16 80 22 84 M70 86 Q76 82 82 86" fill="none" stroke="#fff" stroke-width="2"/>
<path d="M0 94 Q64 88 128 94 V128 H0Z" fill="#F5D58A" {W(2.4)}/>
<g fill="#D8B060"><circle cx="20" cy="110" r="1.6"/><circle cx="100" cy="114" r="1.6"/><circle cx="80" cy="104" r="1.4"/><circle cx="14" cy="100" r="1.4"/></g>
<circle cx="84" cy="44" r="11" fill="#fff" {W(2.8)}/><path d="M74 40 Q84 48 94 40 M82 33 Q88 44 82 55" fill="none" stroke="#FFB020" stroke-width="2.2"/>
<path d="M70 58 L74 54 M66 66 L72 64" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{limb("M42 96 L38 116", SK, 7)}{limb("M52 96 L60 116", SK, 7)}
<path d="M36 98 Q34 72 46 68 Q58 72 56 98Z" fill="#E8384A" {W(2.8)}/>
{limb("M54 76 L64 86 L68 78", SK, 6.4)}{limb("M40 76 L30 90", SK, 6.4)}
<circle cx="46" cy="56" r="11" fill="{SK}" {W(2.8)}/>
<path d="M34 52 Q36 40 48 42 Q58 44 58 52Z" fill="#E8384A" {W(2.4)}/><path d="M56 52 H66" {W(3.6)}/><path d="M56 52 H65" stroke="#E8384A" stroke-width="2"/>
<path d="M36 54 Q28 60 32 70" fill="none" stroke="#6A3A20" stroke-width="4" stroke-linecap="round"/>
{eye(48, 58, .4)}{eye(54, 58, .4)}<path d="M48 63 Q51 65 54 63" fill="none" {W(1.8)}/>''')

# 19. СольФаСоль — картошка фри в красном коробке поёт по нотам
I["cafe-solfasol-pervomayskaya"] = ("картошка фри в красном коробке", "поёт во весь рот «соль-фа-соль», а над ней разлетаются ноты", ("#FFE9E9", "#C82A2A"), f'''
<g fill="#FFD25A" {W(2.4)}><path d="M42 64 L38 26 L46 26 L50 64Z"/><path d="M52 64 L52 18 L60 18 L60 64Z"/><path d="M64 64 L68 22 L76 22 L72 64Z"/><path d="M76 64 L86 30 L93 32 L84 64Z"/><path d="M36 66 L28 36 L35 34 L44 64Z"/></g>
<path d="M30 60 H98 L90 120 H38Z" fill="#E8303A" {W(3)}/>
<path d="M30 60 Q64 74 98 60" fill="#C8202A" {W(2.4)}/>
{eye(54, 84, .55)}{eye(74, 84, .55)}<ellipse cx="64" cy="100" rx="6" ry="7" fill="{O}"/><ellipse cx="64" cy="103" rx="3.4" ry="2.4" fill="#FF7FA8"/>
{blush(46, 94, .45)}{blush(82, 94, .45)}
<path d="M104 34 V16 L116 12 V30" fill="none" {W(2.4)}/><ellipse cx="101" cy="34" rx="4.4" ry="3.4" fill="{O}"/><ellipse cx="113" cy="30" rx="4.4" ry="3.4" fill="{O}"/>
<path d="M20 26 V10" {W(2.4)}/><ellipse cx="17" cy="26" rx="4.4" ry="3.4" fill="{O}"/><path d="M20 10 Q28 14 26 20" fill="none" {W(2.4)}/>
<path d="M108 66 V54" {W(2.2)}/><ellipse cx="105" cy="66" rx="3.6" ry="2.8" fill="{O}"/>''')

# 20. RusVolley (Электролитный) — тележка-корзина с волейбольными мячами катится в зал
I["rusvolley-elektrolitny"] = ("сетчатая тележка, доверху полная волейбольных мячей", "с разгона катится по паркету в зал, мячи подпрыгивают, один выглядывает и улыбается", ("#EEF0F4", "#6A7488"), f'''
<path d="M0 108 H128 V128 H0Z" fill="#E8B878" {W(2.4)}/><path d="M0 116 H128" stroke="#fff" stroke-width="2"/>
<path d="M26 60 H104 L98 98 H32Z" fill="#C0C8D8" opacity=".35" {W(3)}/>
<circle cx="44" cy="58" r="12" fill="#fff" {W(2.6)}/><path d="M34 56 Q44 62 54 56 M42 46 Q48 58 42 70" fill="none" stroke="#2A6AD8" stroke-width="2"/>
<circle cx="88" cy="58" r="12" fill="#FFD23A" {W(2.6)}/><path d="M78 56 Q88 62 98 56 M86 46 Q92 58 86 70" fill="none" stroke="#2A6AD8" stroke-width="2"/>
<circle cx="66" cy="48" r="14" fill="#fff" {W(2.8)}/><path d="M54 44 Q66 52 78 44 M62 34 Q70 48 62 62" fill="none" stroke="#FFC020" stroke-width="2.4"/>
{eye(61, 50, .45)}{eye(71, 50, .45)}{smile(66, 56, 3, .6)}
<circle cx="104" cy="30" r="8" fill="#fff" {W(2.4)}/><path d="M98 28 Q104 32 110 28" fill="none" stroke="#2A6AD8" stroke-width="1.8"/>
<path d="M28 66 H102 M30 78 H100 M31 90 H99 M40 60 L42 98 M54 60 L55 98 M68 60 V98 M82 60 L81 98 M96 60 L94 98" stroke="#3B3355" stroke-width="1.6"/>
<path d="M26 60 H104 L98 98 H32Z" fill="none" {W(3)}/>
<path d="M26 60 L18 44 L12 44" fill="none" {W(3.4)}/>
<circle cx="40" cy="104" r="6" fill="#4A4A5A" {W(2.4)}/><circle cx="90" cy="104" r="6" fill="#4A4A5A" {W(2.4)}/>
<path d="M2 66 H10 M2 78 H14 M2 90 H10" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')


# 21. Каратэ «Мицудэн» (Переяславская) — малыш в кимоно наносит удар и кричит «КИЯ!»
I["mitsuden-pereyaslavskaya"] = ("мальчик-каратист в белом кимоно с оранжевым поясом", "на татами в низкой стойке выбрасывает кулак вперёд и громко кричит «КИЯ!»", ("#FFFBEA", "#A8A040"), f'''
<path d="M0 102 H128 V128 H0Z" fill="#E8DCA0" {W(2.4)}/><path d="M40 102 V128 M88 102 V128 M0 116 H128" stroke="#C8B870" stroke-width="2"/>
{limb("M48 82 L30 100", SK, 7)}{limb("M62 82 L80 92 L84 102", SK, 7)}
<path d="M40 86 L44 64 H66 L70 86Z" fill="#fff" {W(2.8)}/>
<path d="M42 58 Q42 52 56 50 Q70 52 70 60 L68 72 H44Z" fill="#fff" {W(2.8)}/><path d="M50 52 L56 64 L62 52" fill="none" {W(2)}/>
<path d="M42 70 H70 V76 H42Z" fill="#F08A2A" {W(2.4)}/><path d="M66 76 L72 86 M62 76 L64 88" {W(3)}/>
<path d="M66 58 L98 54" {W(9)}/><path d="M66 58 L98 54" stroke="#fff" stroke-width="5.6"/>
<circle cx="104" cy="54" r="7" fill="{SK}" {W(2.6)}/><path d="M102 50 V58" stroke="#E8B090" stroke-width="1.4"/>
<path d="M112 46 L120 42 M114 54 H124 M112 62 L120 66" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{limb("M46 60 L38 70 L44 72", SK, 6.4)}
<circle cx="52" cy="38" r="13" fill="{SK}" {W(3)}/><path d="M39 36 Q38 24 52 24 Q66 24 65 36 Q58 30 52 32 Q44 30 39 36Z" fill="#2A1A10" {W(2)}/>
<path d="M44 34 L50 36 M56 36 L62 33" {W(2.2)}/>{eye(48, 39, .38)}{eye(58, 39, .38)}
<ellipse cx="54" cy="46" rx="4" ry="3.6" fill="#C83A4A" {W(1.8)}/>
<path d="M74 6 L80 16 L90 6 L94 18 L106 12 L104 24 L118 26 L106 32 L114 42 L98 38 L92 46 L86 36 L74 40 L78 30 L66 26 L78 20Z" fill="#FFE04A" {W(2.4)}/>
<text x="90" y="30" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="12" text-anchor="middle" fill="#D8303A">КИЯ!</text>''')

# 22. «Академия мыслителей» — мальчик-шахматист подпёр щёку кулаком и обдумывает ход конём
I["myslitel-academy-chess"] = ("мальчик-шахматист в синем свитере", "подпёр подбородок кулаком над доской и думает — в облачке мыслей скачет конь", ("#EAF0FF", "#5A6AD0"), f'''
<path d="M86 30 Q84 16 98 16 Q104 6 114 14 Q126 14 122 28 Q128 38 116 40 H96 Q84 40 86 30Z" fill="#fff" {W(2.4)}/>
<circle cx="84" cy="48" r="4" fill="#fff" {W(2)}/><circle cx="78" cy="56" r="2.6" fill="#fff" {W(1.6)}/>
<path d="M98 36 V32 Q96 26 100 22 Q102 18 108 18 L110 15 L112 19 Q116 22 116 28 L112 29 L108 26 Q106 30 110 34 V36Z" fill="#2A2A3A"/>
<path d="M28 100 Q28 76 64 74 Q100 76 100 100Z" fill="#3A5AC8" {W(3)}/>
{limb("M44 90 L50 74 L56 66", SK, 7.4)}
<circle cx="64" cy="54" r="16" fill="{SK}" {W(3)}/>
<path d="M48 50 Q48 34 64 34 Q80 34 80 50 Q74 42 66 44 Q56 40 48 50Z" fill="#6A3A20" {W(2)}/>
<path d="M60 48 Q62 46 64 48 M70 47 Q72 45 74 48" fill="none" {W(1.8)}/>
{eye(62, 54, .45)}{eye(72, 53, .45)}<path d="M64 62 H71" {W(2)}/>
<circle cx="56" cy="66" r="6" fill="{SK}" {W(2.6)}/>
<path d="M4 100 H124 L128 128 H0Z" fill="#F4E6CC" {W(2.6)}/>
<path d="M18 100 L14 114 H28 L32 100Z M46 100 L44 114 H58 L60 100Z M74 100 L74 114 H88 L86 100Z M102 100 L104 114 H118 L114 100Z M14 114 L12 128 H26 L28 114Z M44 114 L42 128 H58 L58 114Z M74 114 L74 128 H90 L88 114Z M104 114 L106 128 H122 L118 114Z M28 114 L26 128 H42 L44 114Z M58 114 L58 128 H74 L74 114Z M88 114 L90 128 H106 L104 114Z M32 100 L28 114 H44 L46 100Z M60 100 L58 114 H74 L74 100Z M86 100 L88 114 H104 L102 100Z" fill="#9A7050"/>
<path d="M36 98 Q34 90 38 86 Q34 84 38 80 Q42 76 46 80 Q50 84 46 86 Q50 90 48 98Z" fill="#fff" {W(2.2)}/>''')

# 23. Moscow Chess School («Торпедо») — чёрный шахматный конь несётся по волнам, как торпеда
I["moscow-chess-school-torpedo"] = ("чёрный шахматный конь с белой гривой", "мчится по морским волнам, как торпеда, оставляя за собой длинный пенный след", ("#E0F4FF", "#0A4A7A"), f'''
<path d="M0 80 Q16 74 32 80 T64 80 T96 80 T128 80 V128 H0Z" fill="#2A7AC8" {W(2.6)}/>
<path d="M0 86 Q20 80 40 86 Q50 90 60 84 L62 92 Q40 96 0 94Z" fill="#fff" {W(2)}/>
<path d="M4 102 Q12 98 20 102 M26 108 Q34 104 42 108 M80 108 Q88 104 96 108" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M56 90 L58 72 Q48 62 52 46 Q58 28 76 24 L80 14 L86 24 Q102 30 108 50 Q110 56 104 60 L94 56 L86 54 Q82 64 90 74 L92 90Z" fill="#2A2A3A" {W(3)}/>
<path d="M64 34 Q58 46 60 62 Q56 48 64 34Z M70 28 Q64 30 62 36" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="88" cy="38" r="5" fill="#fff"/><circle cx="89" cy="38" r="2.6" fill="{O}"/><circle cx="88" cy="37" r="1" fill="#fff"/>
<circle cx="102" cy="54" r="1.6" fill="#fff"/>
<path d="M96 80 Q108 66 118 76 Q112 74 108 80 M104 86 Q116 82 122 88" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/>
<circle cx="114" cy="64" r="2.4" fill="#fff"/><circle cx="122" cy="72" r="2" fill="#fff"/>
<path d="M18 30 H40 M10 40 H34 M22 50 H42" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 24. «Китёнок» (Тушинская) — тренер с бортика протягивает длинный шест малышу в воде
I["kitenok-tushinskaya"] = ("тренер по плаванию в красном костюме со свистком", "стоит на бортике и протягивает длинный шест малышу в зелёной шапочке, который плывёт к нему", ("#E8FFFE", "#3AB8C8"), f'''
<path d="M0 70 H34 V128 H0Z" fill="#fff" {W(2.6)}/><path d="M0 86 H34 M0 102 H34 M0 118 H34 M17 70 V128" stroke="#C0D0D8" stroke-width="1.4"/>
<path d="M34 74 Q50 70 66 74 T98 74 T130 74 V128 H34Z" fill="#48B8F0" {W(2.6)}/>
<path d="M48 100 Q56 96 64 100 M80 112 Q88 108 96 112" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
{limb("M14 70 L14 54", "#D8303A", 8)}{limb("M24 70 L26 54", "#D8303A", 8)}
<path d="M8 56 Q8 34 20 32 Q32 34 32 56Z" fill="#D8303A" {W(2.8)}/><path d="M20 34 V56" stroke="#fff" stroke-width="1.6"/>
<path d="M30 46 L98 82" {W(4.6)}/><path d="M30 46 L98 82" stroke="#F0D060" stroke-width="2"/>
{limb("M28 40 L36 48", SK, 6)}
<circle cx="20" cy="22" r="10" fill="{SK}" {W(2.8)}/><path d="M10 20 Q12 10 22 10 Q30 12 30 18 L36 20 L30 22 Q20 16 10 20Z" fill="#fff" {W(2)}/>
{eye(18, 24, .38)}{eye(25, 24, .38)}
<path d="M22 30 L30 36" stroke="#888" stroke-width="1.4"/><rect x="28" y="34" width="6" height="4" rx="1.4" fill="#C0C8D8" {W(1.4)}/>
<circle cx="104" cy="82" r="11" fill="{SK}" {W(2.8)}/><path d="M93 80 Q94 68 104 68 Q115 68 115 80 Q104 74 93 80Z" fill="#3AB84A" {W(2.2)}/>
{eye(101, 84, .4)}{eye(108, 84, .4)}<path d="M101 89 Q104 91 107 89" fill="none" {W(1.6)}/>
{limb("M96 86 L94 82", SK, 6)}
<path d="M90 92 Q104 98 118 92" fill="none" stroke="#fff" stroke-width="2.4"/>''')

# 25. «Пронто» (Одинцово) — три шарика щербета в высокой креманке горят, как светофор
I["cafe-pronto-odintsovo"] = ("три шарика щербета — малиновый, лимонный и фисташковый — в высокой креманке", "стоят столбиком, как светофор, средний жёлтый подмигивает: «Готово — можно есть!»", ("#FFFFF0", "#A8C838"), f'''
<path d="M50 120 H78 L72 112 H56Z" fill="#E8F4FF" {W(2.6)}/><path d="M60 112 V96 H68 V112" fill="#E8F4FF" {W(2.4)}/>
<path d="M38 82 H90 Q88 98 64 98 Q40 98 38 82Z" fill="#E8F4FF" {W(2.8)}/>
<circle cx="64" cy="74" r="15" fill="#7ACB5A" {W(2.8)}/><path d="M52 78 Q56 84 62 82" fill="none" stroke="#A8E890" stroke-width="2.4"/>
<circle cx="64" cy="50" r="14" fill="#FFE04A" {W(2.8)}/>
<path d="M56 49 Q59 46 62 49" fill="none" {W(2)}/>{eye(69, 49, .45)}{smile(64, 55, 3, .6)}
<circle cx="64" cy="27" r="13" fill="#F0485A" {W(2.8)}/><path d="M56 22 Q60 18 64 20" fill="none" stroke="#FF98A8" stroke-width="2.4"/>
<path d="M78 24 L98 10" {W(5)}/><path d="M78 24 L98 10" stroke="#E8B060" stroke-width="2"/>
<path d="M84 32 L102 26 M86 42 L106 40" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
{sparkle(30, 30, 4)}{sparkle(26, 64, 3)}''')

# 26. Hatimaki (Химки) — суши-гункан с оранжевой икрой плывёт, как кораблик под парусом из нори
I["cafe-hatimaki-khimki"] = ("суши-гункан с оранжевой икрой в поясе из нори", "плывёт по волнам, как кораблик, под зелёным парусом из листа нори на шпажке-мачте", ("#F6E8FF", "#6A3A9A"), f'''
<path d="M64 62 V12" {W(4)}/><path d="M64 62 V12" stroke="#E8C890" stroke-width="1.6"/>
<path d="M66 14 Q96 26 104 54 H66Z" fill="#2E5A3A" {W(2.6)}/><path d="M72 30 L90 44" stroke="#4E7A5A" stroke-width="2"/>
<path d="M60 8 L50 12 L60 16Z" fill="#E8384A" {W(1.8)}/>
<path d="M30 64 Q34 52 64 52 Q94 52 98 64Z" fill="#FF7A2A" {W(2.6)}/>
<g fill="#FFB060"><circle cx="40" cy="60" r="2.6"/><circle cx="50" cy="56" r="2.6"/><circle cx="60" cy="58" r="2.6"/><circle cx="72" cy="56" r="2.6"/><circle cx="82" cy="58" r="2.6"/><circle cx="90" cy="61" r="2.4"/><circle cx="66" cy="62" r="2"/></g>
<path d="M26 64 H102 Q104 84 96 92 H32 Q24 84 26 64Z" fill="#26362A" {W(3)}/>
<circle cx="52" cy="76" r="5.4" fill="#fff"/><circle cx="76" cy="76" r="5.4" fill="#fff"/>{eye(52, 77, .55)}{eye(76, 77, .55)}
<path d="M58 84 Q64 89 70 84" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M0 92 Q16 86 32 92 T64 92 T96 92 T128 92 V128 H0Z" fill="#3A8AE0" {W(2.6)}/>
<path d="M12 108 Q20 104 28 108 M70 112 Q78 108 86 112" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
<path d="M104 90 Q112 82 120 88 M14 88 Q8 82 4 86" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>''')

# 27. «Булочка» (Хорошёвский) — сдобная булочка с изюмом-веснушками потягивается на противне
I["cafe-bulochka"] = ("пышная сдобная булочка с изюминками-веснушками и сахарной макушкой", "только что из духовки — сладко потягивается и зевает на противне, над ней вьётся тёплый пар", ("#FFF3E2", "#D07A3A"), f'''
<path d="M10 100 H118 V110 Q118 114 114 114 H14 Q10 114 10 110Z" fill="#5A5A6A" {W(2.8)}/>
{limb("M34 82 L20 62 L18 50", "#E8A050", 7)}{limb("M94 82 L108 62 L110 50", "#E8A050", 7)}
<path d="M24 100 Q24 56 64 54 Q104 56 104 100Z" fill="#E8A050" {W(3)}/>
<path d="M36 70 Q64 52 92 70 Q80 62 64 62 Q48 62 36 70Z" fill="#C87830"/>
<g fill="#fff" {W(1.2)}><rect x="50" y="56" width="4" height="4" rx="1"/><rect x="60" y="54" width="4" height="4" rx="1"/><rect x="70" y="56" width="4" height="4" rx="1"/><rect x="56" y="62" width="3.4" height="3.4" rx="1"/><rect x="66" y="61" width="3.4" height="3.4" rx="1"/></g>
<path d="M50 80 Q54 76 58 80 M70 80 Q74 76 78 80" fill="none" {W(2.4)}/>
<ellipse cx="64" cy="90" rx="5" ry="5.6" fill="{O}"/>
<g fill="#6A3A2A"><circle cx="42" cy="84" r="2"/><circle cx="46" cy="90" r="1.8"/><circle cx="86" cy="84" r="2"/><circle cx="82" cy="90" r="1.8"/><circle cx="38" cy="94" r="1.6"/><circle cx="90" cy="94" r="1.6"/></g>
<path d="M50 40 Q44 32 50 24 Q56 16 50 8 M64 38 Q58 28 64 20 Q70 12 64 4 M78 40 Q72 32 78 24 Q84 16 78 8" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/>''')

# 28. «Колибри» (Шатура) — кинобилетик на ножках бежит в кино, отрывной корешок развевается
I["shatura-kolibri-cinema"] = ("жёлтый кинобилетик с надписью «КИНО» и отрывным корешком", "на тоненьких ножках со всех ног бежит на сеанс, боясь опоздать", ("#FFE8E8", "#8A1A3A"), f'''
{limb("M54 84 L46 100 L36 102", SK, 6)}{limb("M74 84 L84 98 L92 92", SK, 6)}
<path d="M32 104 Q36 100 42 102 L40 106 H32Z" fill="#2A2A3A" {W(1.8)}/><path d="M90 90 Q96 88 98 94 L94 96 L88 94Z" fill="#2A2A3A" {W(1.8)}/>
<g transform="rotate(-10 64 60)">
<path d="M22 36 H106 V48 Q100 50 100 56 Q100 62 106 64 V84 H22 V64 Q28 62 28 56 Q28 50 22 48Z" fill="#FFD86A" {W(3)}/>
<path d="M84 38 V82" stroke="{O}" stroke-width="2" stroke-dasharray="3 3"/>
<text x="52" y="54" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="13" text-anchor="middle" fill="#B8203A">КИНО</text>
{eye(44, 68, .5)}{eye(60, 68, .5)}{smile(52, 74, 3.4, .7)}
<path d="M90 46 L98 52 M90 56 H100 M90 66 L98 60" stroke="#B8203A" stroke-width="2"/>
</g>
<path d="M6 44 H16 M4 58 H14 M8 72 H18" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>
{sparkle(104, 18, 4.6)}{sparkle(30, 18, 3.4)}{sparkle(112, 104, 3)}''')

# 29. «Триумф» (РГСУ) — мальчик выпрыгнул из воды на финише и вскинул кулак
I["triumf-rgsu"] = ("мальчик-пловец в красной шапочке с очками на лбу", "приплыл первым — выпрыгнул из воды по пояс, вскинул кулак и кричит «Ура!»", ("#FFFBE0", "#E0B000"), f'''
{limb("M70 66 L84 42 L88 22", SK, 7.4)}<circle cx="88" cy="18" r="6.4" fill="{SK}" {W(2.6)}/>
{limb("M48 68 L28 70 L18 60", SK, 7.4)}
<path d="M40 92 Q40 64 58 62 Q76 64 76 92Z" fill="{SK}" {W(3)}/>
<circle cx="58" cy="46" r="14" fill="{SK}" {W(3)}/>
<path d="M44 44 Q44 30 58 30 Q72 30 72 44 Q58 38 44 44Z" fill="#E8303A" {W(2.4)}/>
<circle cx="52" cy="38" r="4" fill="#9AD8FF" {W(1.8)}/><circle cx="63" cy="38" r="4" fill="#9AD8FF" {W(1.8)}/><path d="M56 38 H59" {W(1.6)}/>
<path d="M52 46 Q54 44 56 46 M61 46 Q63 44 65 46" fill="none" {W(2)}/>
<path d="M50 52 Q58 62 66 52Z" fill="#C83A4A" {W(2)}/>
<path d="M0 84 Q16 78 32 84 T64 84 T96 84 T128 84 V128 H0Z" fill="#3A9AE8" {W(2.6)}/>
<g {W(1.6)}><circle cx="8" cy="104" r="5" fill="#E8303A"/><circle cx="20" cy="104" r="5" fill="#fff"/><circle cx="32" cy="104" r="5" fill="#E8303A"/><circle cx="96" cy="104" r="5" fill="#fff"/><circle cx="108" cy="104" r="5" fill="#E8303A"/><circle cx="120" cy="104" r="5" fill="#fff"/></g>
<circle cx="32" cy="78" r="2.4" fill="#fff" {W(1.2)}/><circle cx="86" cy="76" r="2.6" fill="#fff" {W(1.2)}/><circle cx="94" cy="68" r="2" fill="#fff" {W(1.2)}/>
{sparkle(104, 34, 5, "#fff")}{sparkle(24, 32, 4, "#fff")}{sparkle(112, 60, 3, "#fff")}''')

# 30. ФОК «Радужный» — мальчик нырнул вниз головой: из воды торчат только ноги, над ним радуга
I["raduzhny-fok-pool"] = ("мальчик в радужных плавках", "нырнул вниз головой — из воды торчат только ноги буквой V, а над бассейном висит радуга", ("#F0FAFF", "#7AA8E8"), f'''
<path d="M4 70 A60 60 0 0 1 124 70" fill="none" stroke="#F04848" stroke-width="5"/>
<path d="M10 70 A54 54 0 0 1 118 70" fill="none" stroke="#FFA030" stroke-width="5"/>
<path d="M16 70 A48 48 0 0 1 112 70" fill="none" stroke="#FFE040" stroke-width="5"/>
<path d="M22 70 A42 42 0 0 1 106 70" fill="none" stroke="#5AC85A" stroke-width="5"/>
<path d="M28 70 A36 36 0 0 1 100 70" fill="none" stroke="#4A8AF0" stroke-width="5"/>
<path d="M0 76 Q16 70 32 76 T64 76 T96 76 T128 76 V128 H0Z" fill="#48A8F0" {W(2.6)}/>
{limb("M58 78 L50 54 L42 34", SK, 8.4)}{limb("M70 78 L78 54 L86 34", SK, 8.4)}
<path d="M36 34 Q36 24 44 26 L48 32Z" fill="{SK}" {W(2.4)}/><path d="M92 34 Q92 24 84 26 L80 32Z" fill="{SK}" {W(2.4)}/>
<path d="M50 72 H78 L76 82 H52Z" fill="#fff" {W(2.6)}/>
<path d="M52 74 H76" stroke="#F04848" stroke-width="2"/><path d="M52 77 H76" stroke="#FFE040" stroke-width="2"/><path d="M52 80 H76" stroke="#4A8AF0" stroke-width="2"/>
<ellipse cx="64" cy="86" rx="26" ry="5" fill="none" stroke="#fff" stroke-width="2.6"/>
<ellipse cx="64" cy="90" rx="42" ry="9" fill="none" stroke="#fff" stroke-width="1.8" opacity=".7"/>
<circle cx="50" cy="104" r="3" fill="#fff" {W(1.2)}/><circle cx="74" cy="110" r="2.4" fill="#fff" {W(1.2)}/><circle cx="62" cy="116" r="2" fill="#fff" {W(1.2)}/>''')

# 31. Каток «Космик» — белый фигурный конёк скользит по ледяному кольцу Сатурна
I["rink-cosmic"] = ("белый фигурный конёк со шнуровкой", "скользит по ледяному кольцу Сатурна среди звёзд, оставляя искристый след", ("#3A2A6A", "#0A0A2A"), f'''
<g fill="#fff"><circle cx="18" cy="30" r="1.6"/><circle cx="104" cy="16" r="1.4"/><circle cx="118" cy="50" r="1.8"/><circle cx="24" cy="100" r="1.4"/><circle cx="96" cy="112" r="1.6"/></g>
<ellipse cx="54" cy="62" rx="54" ry="13" transform="rotate(-14 54 62)" fill="none" stroke="#BFE8FF" stroke-width="8"/>
<circle cx="54" cy="62" r="27" fill="#F0A050" {W(3)}/>
<path d="M30 52 Q54 46 78 52 M28 64 Q54 60 80 66 M34 76 Q54 74 74 78" fill="none" stroke="#D07830" stroke-width="3"/>
<path d="M0 78 Q30 90 108 50" fill="none" stroke="#BFE8FF" stroke-width="8"/>
<path d="M0 78 Q30 90 108 50" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="3 6"/>
<path d="M72 34 H88 V50 Q88 54 94 56 L104 59 Q110 61 108 68 H70 Q66 68 68 60Z" fill="#fff" {W(3)}/>
<path d="M76 40 L84 42 M76 46 L84 48" stroke="#5A8AE0" stroke-width="2"/>
<path d="M66 76 Q72 80 86 74 L110 64" fill="none" stroke="#C8D0E0" stroke-width="3.4" stroke-linecap="round"/><path d="M76 68 L76 76 M100 64 L100 68" {W(2.2)}/>
{eye(80, 58, .45)}{eye(89, 58, .45)}{smile(84, 63, 2.6, .5)}
{sparkle(40, 96, 4, "#BFE8FF")}{sparkle(18, 84, 3, "#fff")}{sparkle(110, 30, 4.4, "#FFE07A")}''')

# 32. «Стиль Студия» (Химки) — раскалённый стеклянный шар на трубке стеклодува светится, как будущая ёлочная игрушка
I["khimki-style-studio"] = ("раскалённый оранжевый стеклянный шар на трубке стеклодува", "его только что выдули — он светится и рассыпает искры, а над ним на еловой гирлянде висят готовые ёлочные шары", ("#FFF4E8", "#E06A20"), f'''
<path d="M2 124 L50 76" {W(7)}/><path d="M2 124 L50 76" stroke="#9AA4B4" stroke-width="3.6"/>
<path d="M14 112 L20 118 M24 102 L30 108" stroke="{O}" stroke-width="2"/>
<circle cx="74" cy="52" r="38" fill="#FFE07A" opacity=".35"/>
<circle cx="74" cy="52" r="28" fill="#FFA030" {W(3)}/>
<circle cx="74" cy="52" r="20" fill="#FFC850"/>
<ellipse cx="64" cy="40" rx="8" ry="5" fill="#FFF4C0" transform="rotate(-30 64 40)"/>
<path d="M50 72 L56 70 L54 78Z" fill="#FFA030" {W(2.2)}/>
{eye(68, 54, .55)}{eye(82, 54, .55)}<ellipse cx="75" cy="63" rx="3.4" ry="3" fill="{O}"/>{blush(62, 61, .45)}{blush(88, 61, .45)}
{sparkle(110, 86, 3.6, "#FFF4C0")}
<path d="M-4 8 Q30 22 64 8 Q98 -6 132 8" fill="none" stroke="#2E7A3A" stroke-width="3"/>
<path d="M22 14 V18 M106 4 V10" {W(1.6)}/>
<circle cx="22" cy="25" r="7" fill="#D8303A" {W(2.2)}/><rect x="19" y="16" width="6" height="4" fill="#C8C8D0" {W(1.4)}/>
<circle cx="106" cy="17" r="7" fill="#2A8AE0" {W(2.2)}/><rect x="103" y="8" width="6" height="4" fill="#C8C8D0" {W(1.4)}/>
<path d="M18 23 L26 27 M102 15 L110 19" stroke="#fff" stroke-width="1.6"/>
<circle cx="104" cy="44" r="1.8" fill="#FFF4C0"/><circle cx="98" cy="96" r="1.6" fill="#FFF4C0"/><circle cx="48" cy="30" r="1.6" fill="#FFF4C0"/>''')

# 33. Якитория (Первомайская) — три шпажки якитори маршируют строем
I["cafe-yakitoriya-pervomayskaya"] = ("три бамбуковые шпажки якитори с глянцевыми кусочками и зелёным луком", "маршируют строем на маленьких ножках, средняя шпажка командует и улыбается", ("#FFF0E0", "#A04A20"), f'''
<path d="M38 14 V100 M64 8 V96 M90 14 V100" {W(4.2)}/><path d="M38 14 V100 M64 8 V96 M90 14 V100" stroke="#E8C890" stroke-width="1.8"/>
<g {W(2.4)}><rect x="28" y="22" width="20" height="16" rx="6" fill="#B8602A"/><rect x="30" y="40" width="16" height="7" rx="3" fill="#7AC04A"/><rect x="28" y="49" width="20" height="16" rx="6" fill="#B8602A"/><rect x="30" y="67" width="16" height="7" rx="3" fill="#7AC04A"/><rect x="28" y="76" width="20" height="14" rx="6" fill="#B8602A"/></g>
<g {W(2.4)}><rect x="80" y="22" width="20" height="16" rx="6" fill="#B8602A"/><rect x="82" y="40" width="16" height="7" rx="3" fill="#7AC04A"/><rect x="80" y="49" width="20" height="16" rx="6" fill="#B8602A"/><rect x="82" y="67" width="16" height="7" rx="3" fill="#7AC04A"/><rect x="80" y="76" width="20" height="14" rx="6" fill="#B8602A"/></g>
<g {W(2.6)}><rect x="51" y="16" width="26" height="20" rx="8" fill="#C86A30"/><rect x="54" y="38" width="20" height="8" rx="3" fill="#7AC04A"/><rect x="50" y="48" width="28" height="26" rx="9" fill="#C86A30"/><rect x="54" y="76" width="20" height="8" rx="3" fill="#7AC04A"/></g>
<g fill="#FFE8C0"><circle cx="34" cy="28" r="1.2"/><circle cx="42" cy="56" r="1.2"/><circle cx="86" cy="30" r="1.2"/><circle cx="94" cy="58" r="1.2"/><circle cx="56" cy="22" r="1.2"/><circle cx="70" cy="24" r="1.2"/></g>
<path d="M32 26 Q36 24 40 26 M84 52 Q88 50 92 52 M54 52 Q58 50 62 52" fill="none" stroke="#F0A060" stroke-width="2" stroke-linecap="round"/>
{eye(58, 60, .5)}{eye(70, 60, .5)}{smile(64, 67, 3, .6)}
{limb("M36 100 L32 112", "#E8C890", 5)}{limb("M40 100 L46 110", "#E8C890", 5)}{limb("M62 96 L56 108", "#E8C890", 5)}{limb("M66 96 L72 108", "#E8C890", 5)}{limb("M88 100 L84 112", "#E8C890", 5)}{limb("M92 100 L98 110", "#E8C890", 5)}
<ellipse cx="30" cy="114" rx="5" ry="3" fill="#3A2A20"/><ellipse cx="48" cy="111" rx="5" ry="3" fill="#3A2A20"/><ellipse cx="54" cy="110" rx="5" ry="3" fill="#3A2A20"/><ellipse cx="74" cy="110" rx="5" ry="3" fill="#3A2A20"/><ellipse cx="82" cy="114" rx="5" ry="3" fill="#3A2A20"/><ellipse cx="100" cy="111" rx="5" ry="3" fill="#3A2A20"/>''')

# 34. «ПандаПарк» (Лужники) — мальчик в оранжевой каске идёт по навесному мостику между деревьями
I["panda-luzhniki"] = ("мальчик в оранжевой каске и страховочной обвязке", "осторожно шагает по качающемуся навесному мостику из досок между двумя деревьями, пристёгнутый к тросу", ("#E8F8FF", "#88B8D8"), f'''
<path d="M0 14 H128" stroke="#5A5A6A" stroke-width="3"/>
<path d="M2 30 H18 V128 H2Z" fill="#9A6A40" {W(2.6)}/><path d="M110 30 H126 V128 H110Z" fill="#9A6A40" {W(2.6)}/>
<circle cx="4" cy="24" r="16" fill="#5AB84A" {W(2.4)}/><circle cx="124" cy="24" r="16" fill="#5AB84A" {W(2.4)}/>
<path d="M18 52 Q64 70 110 52" fill="none" {W(3)}/><path d="M18 52 Q64 70 110 52" fill="none" stroke="#E8C890" stroke-width="1.4"/>
<path d="M30 58 V82 M44 62 V88 M84 62 V88 M98 58 V82" stroke="#E8C890" stroke-width="2"/>
<g {W(2.2)} fill="#C8884A"><path d="M20 76 L30 78 L29 86 L19 84Z"/><path d="M33 80 L43 82 L43 90 L33 88Z"/><path d="M47 83 L57 84 L57 92 L47 91Z"/><path d="M71 84 L81 83 L81 91 L71 92Z"/><path d="M85 82 L95 80 L95 88 L85 90Z"/><path d="M99 78 L109 76 L109 84 L99 86Z"/><path d="M59 84 H69 V92 H59Z"/></g>
<path d="M18 78 Q64 98 110 78" fill="none" {W(2)}/>
{limb("M58 74 L54 88", "#2A4A9A", 7)}{limb("M70 74 L76 86", "#2A4A9A", 7)}
<path d="M54 76 Q52 54 64 52 Q76 54 74 76Z" fill="#3AB0E0" {W(2.8)}/>
<path d="M54 66 H74 M60 54 L58 76 M68 54 L70 76" stroke="#E8303A" stroke-width="2.6"/>
<path d="M64 52 L64 14" stroke="#E8303A" stroke-width="2"/><path d="M64 52 L64 14" {W(.8)}/>
{limb("M56 58 L44 60 L40 56", SK, 6)}{limb("M72 58 L84 60 L88 56", SK, 6)}
<circle cx="64" cy="40" r="11" fill="{SK}" {W(2.8)}/>
<path d="M52 38 Q52 24 64 24 Q76 24 76 38Z" fill="#FF8A1A" {W(2.4)}/><path d="M50 38 H78" {W(2.6)}/>
{eye(60, 42, .4)}{eye(68, 42, .4)}<path d="M61 47 Q64 49 67 47" fill="none" {W(1.6)}/>''')

# 35. «Школа мяча» (Солнцево) — мальчик в прыжке бьёт по мячу «через себя» (ножницы)
I["schoolball-solntsevo"] = ("мальчик-футболист в оранжевой форме", "под солнцем в акробатическом прыжке бьёт по мячу «через себя» — ножницами", ("#FFFDE6", "#F0D040"), f'''
<circle cx="22" cy="22" r="12" fill="#FFB020" {W(2.4)}/>
<path d="M0 104 Q64 98 128 104 V128 H0Z" fill="#5AB84A" {W(2.4)}/><path d="M14 112 L16 106 M40 114 L42 108 M90 114 L92 108 M112 112 L114 106" stroke="#3A8A3A" stroke-width="2"/>
{limb("M66 62 L82 44 L94 30", SK, 7.4)}{limb("M66 66 L82 72 L92 64", SK, 7.4)}
<path d="M90 26 L100 24 L100 32 L92 34Z" fill="#2A2A3A" {W(1.8)}/>
<path d="M44 82 Q40 62 58 56 Q72 56 72 70 Q66 84 44 82Z" fill="#FF8A2A" {W(2.8)}/>
<path d="M56 62 L62 74" stroke="#fff" stroke-width="2.4"/>
{limb("M48 76 L30 92", SK, 6.4)}{limb("M54 82 L44 100", SK, 6.4)}
<circle cx="38" cy="78" r="12" fill="{SK}" {W(2.8)}/><path d="M28 84 Q24 74 30 68 Q38 64 46 70 Q36 72 28 84Z" fill="#3A2A20" {W(2)}/>
{eye(40, 80, .38)}{eye(46, 76, .38)}
<circle cx="106" cy="18" r="11" fill="#fff" {W(2.8)}/><path d="M106 13 L111 17 L109 23 L103 23 L101 17Z" fill="#2A2A3A"/>
<path d="M106 13 V7 M111 17 L116 15 M101 17 L96 15 M103 23 L100 27 M109 23 L112 27" stroke="#2A2A3A" stroke-width="1.4"/>
<path d="M84 18 Q90 8 100 6 M82 30 Q84 22 92 18" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>''')

# 36. «Льдинка» — фигуристка крутит вращение «волчок», руки над головой, вокруг вихрь
I["ldinka-korovinskoe"] = ("девочка-фигуристка в бирюзовом платье с блёстками", "крутит вращение «волчок» на одной ножке, сомкнув руки над головой, вокруг закручивается ледяной вихрь", ("#F0F8FF", "#A0C0E8"), f'''
<ellipse cx="64" cy="110" rx="52" ry="12" fill="#E4F6FF" {W(2.4)}/>
<path d="M44 110 Q44 102 64 102 Q84 102 84 110 Q84 116 64 116 Q50 116 50 110 Q50 106 64 106" fill="none" stroke="#9AC8E8" stroke-width="2"/>
{limb("M58 26 L62 8 L66 26", SK, 6)}
<path d="M30 52 Q20 64 30 78 M98 52 Q108 64 98 78 M22 40 Q8 64 22 90 M106 40 Q120 64 106 90" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round"/>
{limb("M64 80 L64 100", SK, 7)}{limb("M66 80 L76 90 L68 96", SK, 6.4)}
<path d="M56 98 H70 V104 Q70 106 66 106 H56Z" fill="#fff" {W(2.2)}/><path d="M54 108 H74" stroke="#9AA4B4" stroke-width="2.4" stroke-linecap="round"/>
<path d="M46 82 Q52 66 64 64 Q76 66 82 82 Q64 88 46 82Z" fill="#2ABAB0" {W(2.8)}/>
<path d="M56 64 Q56 50 64 48 Q72 50 72 64Z" fill="#2ABAB0" {W(2.6)}/>
<g fill="#fff"><circle cx="54" cy="78" r="1.4"/><circle cx="64" cy="80" r="1.4"/><circle cx="74" cy="78" r="1.4"/><circle cx="64" cy="58" r="1.4"/></g>
{limb("M58 52 L56 32", SK, 6)}{limb("M70 52 L72 32", SK, 6)}
<circle cx="64" cy="38" r="10" fill="{SK}" {W(2.8)}/><path d="M54 36 Q56 26 64 26 Q72 26 74 36 Q66 30 54 36Z" fill="#E8B040" {W(2)}/>
<circle cx="64" cy="25" r="4" fill="#E8B040" {W(1.8)}/>
<path d="M59 39 Q61 37 63 39 M66 39 Q68 37 70 39" fill="none" {W(1.6)}/><path d="M61 44 Q64 46 67 44" fill="none" {W(1.6)}/>
{sparkle(34, 30, 3.6)}{sparkle(96, 26, 4)}{sparkle(100, 96, 3)}''')

# 37. «Школа мяча» (Марьино) — девочка-вратарь в прыжке ловит мяч у штанги
I["schoolball-maryino"] = ("девочка-вратарь в больших зелёных перчатках", "в длинном прыжке у штанги ворот ловит летящий футбольный мяч", ("#EAFFEA", "#2A9A3A"), f'''
<path d="M10 0 V104 M10 14 H140" stroke="#fff" stroke-width="7"/><path d="M10 0 V104 M10 14 H140" {W(1.6)}/>
<path d="M14 26 H128 M14 42 H128 M14 58 H128 M14 74 H128 M14 90 H128 M28 18 V100 M46 18 V100 M64 18 V100 M82 18 V100 M100 18 V100 M118 18 V100" stroke="#fff" stroke-width="1.2" opacity=".55"/>
<path d="M0 100 Q64 94 128 100 V128 H0Z" fill="#6AC84A" {W(2.4)}/>
{limb("M44 78 L28 86 L20 80", SK, 7)}{limb("M48 82 L36 96 L26 98", SK, 7)}
<path d="M40 84 Q36 68 58 60 Q78 54 82 64 Q78 78 40 84Z" fill="#FF5A8A" {W(2.8)}/>
<path d="M44 80 L48 74 M52 78 L56 70" stroke="#fff" stroke-width="2"/>
{limb("M74 58 L92 44", SK, 6.4)}{limb("M78 64 L98 56", SK, 6.4)}
<path d="M90 36 Q96 32 100 38 L98 48 L88 46Z" fill="#3AD05A" {W(2.4)}/><path d="M96 50 Q104 48 106 56 L100 62 L94 58Z" fill="#3AD05A" {W(2.4)}/>
<circle cx="110" cy="44" r="11" fill="#fff" {W(2.8)}/><path d="M110 39 L115 43 L113 49 L107 49 L105 43Z" fill="#2A2A3A"/>
<path d="M110 39 V33 M115 43 L120 41 M105 43 L100 41" stroke="#2A2A3A" stroke-width="1.4"/>
<circle cx="74" cy="46" r="11" fill="{SK}" {W(2.8)}/>
<path d="M63 44 Q64 34 74 34 Q84 34 85 42 Q76 38 63 44Z" fill="#6A3A20" {W(2)}/>
<path d="M64 40 Q52 34 48 42 Q54 42 58 46" fill="#6A3A20" {W(2)}/>
{eye(76, 48, .4)}{eye(82, 47, .4)}<path d="M76 54 Q79 55 82 53" fill="none" {W(1.6)}/>''')

# 38. Peshi («Модный сезон») — колечко хлопьев, как спасательный круг, держит малинку в миске молока
I["cafe-peshi-modny-sezon"] = ("медовое колечко хлопьев", "плавает в миске с молоком, как спасательный круг, и катает на себе малинку среди других колечек", ("#FFF8F0", "#E89A6A"), f'''
<path d="M14 66 H114 Q112 110 64 112 Q16 110 14 66Z" fill="#4A8AE0" {W(3)}/>
<path d="M30 92 Q64 102 98 92" fill="none" stroke="#7AB0F0" stroke-width="3"/>
<ellipse cx="64" cy="66" rx="50" ry="13" fill="#FFFDF6" {W(3)}/>
<g {W(2)}><circle cx="30" cy="66" r="6" fill="#F0B040"/><circle cx="96" cy="64" r="6" fill="#E85A5A"/><circle cx="102" cy="72" r="5" fill="#7AC04A"/><circle cx="34" cy="74" r="5" fill="#E85A5A"/></g>
<g fill="#FFFDF6"><circle cx="30" cy="66" r="2.2"/><circle cx="96" cy="64" r="2.2"/><circle cx="102" cy="72" r="1.8"/><circle cx="34" cy="74" r="1.8"/></g>
<ellipse cx="64" cy="62" rx="22" ry="12" fill="#F0B040" {W(2.8)}/><ellipse cx="64" cy="58" rx="9" ry="4" fill="#FFFDF6" {W(2)}/>
{eye(56, 66, .42)}{eye(72, 66, .42)}{smile(64, 69, 2.6, .5)}
<g {W(2)} fill="#E0304A"><circle cx="62" cy="44" r="5"/><circle cx="70" cy="44" r="5"/><circle cx="66" cy="38" r="5"/><circle cx="66" cy="50" r="5"/></g>
<path d="M62 34 L66 30 L70 34" fill="#5AB040" {W(1.6)}/>
<g fill="#FFC0CC"><circle cx="61" cy="43" r="1"/><circle cx="69" cy="44" r="1"/><circle cx="66" cy="37" r="1"/></g>
<circle cx="24" cy="40" r="3" fill="#FFFDF6" {W(1.4)}/><circle cx="104" cy="36" r="2.4" fill="#FFFDF6" {W(1.4)}/><circle cx="96" cy="26" r="1.8" fill="#FFFDF6" {W(1.4)}/>''')

# 39. «Малыш и море» — мама в воде подняла малыша над водой, малыш смеётся и раскинул ручки
I["malysh-i-more"] = ("мама в бассейне с малышом на руках", "стоит по плечи в воде и поднимает над собой смеющегося малыша в розовой шапочке, он раскинул ручки", ("#E8F8FF", "#4A9AD8"), f'''
{limb("M50 76 L44 56 L52 46", SK, 7.4)}{limb("M78 76 L84 56 L76 46", SK, 7.4)}
<circle cx="64" cy="76" r="14" fill="{SK}" {W(3)}/>
<path d="M50 74 Q50 60 64 60 Q78 60 78 74 Q70 66 64 68 Q56 66 50 74Z" fill="#5A3020" {W(2.2)}/><circle cx="64" cy="58" r="6" fill="#5A3020" {W(2)}/>
{eye(59, 77, .42)}{eye(69, 77, .42)}{smile(64, 82, 3, .6)}
<path d="M54 54 Q52 40 64 38 Q76 40 74 54 Q64 58 54 54Z" fill="#FFE07A" {W(2.6)}/>
{limb("M56 42 L44 32 L38 34", SK, 5.6)}{limb("M72 42 L84 32 L90 34", SK, 5.6)}
{limb("M58 54 L54 62", SK, 5.4)}{limb("M70 54 L74 62", SK, 5.4)}
<circle cx="64" cy="28" r="11" fill="{SK}" {W(2.8)}/><path d="M53 26 Q54 16 64 16 Q74 16 75 26 Q64 20 53 26Z" fill="#FF8AB8" {W(2)}/>
<path d="M59 27 Q61 25 63 27 M66 27 Q68 25 70 27" fill="none" {W(1.6)}/>
<path d="M60 32 Q64 37 68 32Z" fill="#C83A4A" {W(1.6)}/>
<path d="M0 84 Q16 78 32 84 T64 84 T96 84 T128 84 V128 H0Z" fill="#4AB0F0" opacity=".9" {W(2.6)}/>
<path d="M44 90 Q64 96 84 90" fill="none" stroke="#fff" stroke-width="2.4"/>
<path d="M14 104 Q22 100 30 104 M98 106 Q106 102 114 106" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
{sparkle(28, 22, 3.6)}{sparkle(102, 18, 4)}''')

# 40. «Про.Плыть» (ТЦ «Клён») — малыш плывёт по бассейну верхом на огромном кленовом листе
I["proplyt-klen"] = ("малыш в зелёной шапочке верхом на огромном оранжевом кленовом листе", "сидит на листе, как на плотике, и гребёт ладошками по голубой воде бассейна", ("#FFF2E0", "#D86A2A"), f'''
<path d="M0 64 Q16 58 32 64 T64 64 T96 64 T128 64 V128 H0Z" fill="#48B0F0" {W(2.6)}/>
<path d="M64 112 L60 96 L40 104 L44 92 L18 88 L30 80 L16 68 L38 70 L40 60 L54 72 L56 58 L64 66 L72 58 L74 72 L88 60 L90 70 L112 68 L98 80 L110 88 L84 92 L88 104 L68 96Z" fill="#F0782A" {W(2.8)}/>
<path d="M64 108 V70 M64 92 L36 84 M64 92 L92 84 M64 82 L46 70 M64 82 L82 70" stroke="#C8501A" stroke-width="2"/>
{limb("M54 64 L40 70 L34 80", SK, 6.4)}{limb("M74 64 L88 70 L94 80", SK, 6.4)}
<path d="M30 82 Q34 78 38 82 M90 82 Q94 78 98 82" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>
<path d="M52 78 Q50 56 64 54 Q78 56 76 78Z" fill="{SK}" {W(2.8)}/><path d="M52 72 H76 V80 H52Z" fill="#2A6AD8" {W(2.4)}/>
<circle cx="64" cy="40" r="13" fill="{SK}" {W(2.8)}/>
<path d="M51 38 Q51 24 64 24 Q77 24 77 38 Q64 32 51 38Z" fill="#3AB84A" {W(2.4)}/>
{eye(59, 42, .42)}{eye(69, 42, .42)}{smile(64, 47, 3, .6)}{blush(54, 47, .35)}{blush(74, 47, .35)}
<path d="M10 112 Q18 108 26 112 M100 116 Q108 112 116 116" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
{sparkle(24, 22, 3.6)}{sparkle(104, 26, 3.2)}''')


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
