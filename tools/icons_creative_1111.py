"""Иконки робота creative, 11.11 (первый запуск). Каждая придумана и нарисована отдельно: свой герой, своя сцена,
своя компоновка и свой фон (правило абсолютной уникальности). python3 tools/icons_creative_1111.py → icons-src/<id>.svg"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


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


def tutu(cx, cy, w, c, c2="#fff"):
    pts = []
    n = 9
    for i in range(n + 1):
        x = cx - w + 2 * w * i / n
        pts.append(f"L{x:.1f} {cy + (7 if i % 2 else 3)}")
    return (f'<path d="M{cx - w*0.55:.1f} {cy - 6} Q{cx} {cy - 10} {cx + w*0.55:.1f} {cy - 6} L{cx + w} {cy + 3} '
            + " ".join(reversed(pts)) + f' Z" fill="{c}" {s()}/>'
            f'<path d="M{cx - w*0.7:.1f} {cy} Q{cx} {cy + 5} {cx + w*0.7:.1f} {cy}" fill="none" stroke="{c2}" stroke-width="2" opacity=".8"/>')


I = {}

# 1. Доннер, Лефортово — верблюжонок-балерина в арабеске
I["donner-ballet-krasnokazarmennaya"] = ("верблюжонок-балерина в белой пачке, горбик с розовым бантом",
    "стоит в арабеске на одной ножке, вторая вытянута назад", bg("#FFF0F5", "#F4A3C4", f'''
<rect x="52" y="92" width="9" height="30" rx="4" fill="#E2B57A" {s()}/>
<path d="M76 88 L112 74 L114 82 L80 98Z" fill="#E2B57A" {s()}/>
<ellipse cx="62" cy="78" rx="26" ry="18" fill="#E8BE85" {s()}/>
<path d="M50 62 Q58 40 70 62Z" fill="#E8BE85" {s()}/>
<path d="M60 44 l-7 -6 l1 9z M60 44 l7 -6 l-1 9z" fill="#FF6FA5" {s('stroke-width="2"')}/><circle cx="60" cy="45" r="3" fill="#FF6FA5" {s('stroke-width="2"')}/>
{tutu(62, 90, 28, "#FFFFFF", "#F7B6CF")}
<path d="M36 78 Q26 60 30 40 L40 40 Q36 60 46 76Z" fill="#E8BE85" {s()}/>
<ellipse cx="33" cy="34" rx="15" ry="12" fill="#EDC690" {s()}/>
<ellipse cx="24" cy="38" rx="6" ry="4.5" fill="#D9A86C" {s('stroke-width="2"')}/>
<path d="M30 22 l-3 -6 M38 23 l2 -6" {s()} fill="none"/>
{eye(34, 31, 0.8)}{eye(42, 32, 0.8)}
<ellipse cx="45" cy="38" rx="3.5" ry="2" fill="#FF7FA8" opacity=".7"/>
<path d="M27 42 Q30 44 33 42" fill="none" {s('stroke-width="2"')}/>
{sparkle(100, 40, 6)}{sparkle(90, 24, 4)}
'''))

# 2. РНБШ, Гнездниковский — хомячок в голубой пачке делает реверанс
I["rnbsh-gnezdnikovsky"] = ("пухлый рыжий хомячок в голубой балетной пачке",
    "делает глубокий реверанс на сцене, придерживая пачку лапками", bg("#E9F5FF", "#7FB9EC", f'''
<rect x="0" y="104" width="128" height="30" fill="#B07A4A"/><path d="M0 104 H128" {s()}/>
<path d="M48 100 Q46 108 38 108 M80 100 Q84 108 92 106" fill="none" {ln("#F2B27A", 5)}/>
<ellipse cx="64" cy="70" rx="30" ry="32" fill="#F2A65E" {s()}/>
<ellipse cx="64" cy="80" rx="18" ry="18" fill="#FFF1DC"/>
{tutu(64, 88, 40, "#9FD3FF", "#fff")}
<circle cx="40" cy="44" r="9" fill="#F2A65E" {s()}/><circle cx="40" cy="44" r="4.5" fill="#FFB0C8"/>
<circle cx="88" cy="44" r="9" fill="#F2A65E" {s()}/><circle cx="88" cy="44" r="4.5" fill="#FFB0C8"/>
{face(64, 60, d=10, k=1.0)}
<ellipse cx="64" cy="66" rx="3" ry="2.2" fill="#E0607E"/>
<path d="M34 84 Q26 92 30 98" fill="none" {ln("#F2A65E", 6)}/>
<path d="M94 84 Q102 92 98 98" fill="none" {ln("#F2A65E", 6)}/>
'''))

# 3. РНБШ, Марьино — филин-балетмейстер отбивает ритм тростью
I["rnbsh-maryinskaya"] = ("седой филин-балетмейстер с длинной тростью",
    "отстукивает тростью счёт «и-раз» по паркету репетиционного зала", bg("#F6EBD9", "#C79A62", f'''
<path d="M0 108 H128 V128 H0Z" fill="#8C5A33"/><path d="M0 108 H128 M20 108 V128 M52 108 V128 M84 108 V128 M116 108 V128" {s('stroke-width="2"')}/>
<path d="M92 50 L100 112" {ln("#5A3A22", 4)}/><circle cx="91" cy="48" r="5" fill="#E0B44A" {s()}/>
<ellipse cx="60" cy="74" rx="32" ry="36" fill="#A9A3A0" {s()}/>
<ellipse cx="60" cy="84" rx="20" ry="22" fill="#E8E1D6"/>
<path d="M48 76 l4 4 l4 -4 l4 4 l4 -4 l4 4 M48 88 l4 4 l4 -4 l4 4 l4 -4 l4 4" fill="none" stroke="#B8AFA4" stroke-width="2"/>
<path d="M30 46 L36 28 L46 42Z M90 46 L84 28 L74 42Z" fill="#8E8884" {s()}/>
<circle cx="47" cy="54" r="11" fill="#FFF6D6" {s()}/><circle cx="73" cy="54" r="11" fill="#FFF6D6" {s()}/>
{eye(47, 54, 1.0)}{eye(73, 54, 1.0)}
<path d="M56 62 L60 70 L64 62Z" fill="#F2A23A" {s('stroke-width="2.2"')}/>
<path d="M88 66 Q96 58 94 50" fill="none" {ln("#8E8884", 7)}/>
<path d="M50 108 l-4 4 M70 108 l4 4" {s()}/>
<text x="16" y="38" font-family="Arial" font-weight="bold" font-size="13" fill="{O}">1</text><text x="104" y="96" font-family="Arial" font-weight="bold" font-size="11" fill="{O}" opacity=".7">2</text>
'''))

# 5. Арбаткласс — серая мышка-балерина крутит фуэте на катушке ниток
I["arbatclass-sivtsev"] = ("серая мышка-балерина в сиреневой пачке",
    "крутит фуэте на большой деревянной катушке ниток", bg("#F2EDFF", "#B49DF0", f'''
<rect x="38" y="96" width="52" height="26" rx="3" fill="#C99A64" {s()}/>
<rect x="44" y="100" width="40" height="18" fill="#E85A8A"/><path d="M44 104 H84 M44 109 H84 M44 114 H84" stroke="#C23E6E" stroke-width="1.5"/>
<rect x="34" y="92" width="60" height="6" rx="2" fill="#B5844F" {s()}/><rect x="34" y="118" width="60" height="6" rx="2" fill="#B5844F" {s()}/>
<path d="M64 80 L64 92" {s('stroke-width="3.5"')}/>
<ellipse cx="64" cy="62" rx="15" ry="20" fill="#B9B6C2" {s()}/>
{tutu(64, 74, 26, "#CDB6FF", "#fff")}
<path d="M50 54 L36 34 M78 54 L92 34" {s('stroke-width="3"')}/><path d="M36 34 Q64 20 92 34" fill="none" {s('stroke-width="2"')} stroke-dasharray="3 4"/>
<circle cx="64" cy="38" r="15" fill="#C4C1CC" {s()}/>
<circle cx="50" cy="26" r="9" fill="#C4C1CC" {s()}/><circle cx="50" cy="26" r="5" fill="#FFB7C9"/>
<circle cx="78" cy="26" r="9" fill="#C4C1CC" {s()}/><circle cx="78" cy="26" r="5" fill="#FFB7C9"/>
{face(64, 38, d=6, k=0.75)}
<circle cx="64" cy="45" r="2" fill="#E0607E"/>
<path d="M78 66 Q100 60 104 76 Q106 88 96 90" fill="none" {s('stroke-width="2.4"')}/>
'''))

# 6. ЦБШ, Сивцев Вражек — пудель в пачке тянет лапку
I["cbs-sivtsev-45"] = ("белый кудрявый пудель-балерина в мятной пачке",
    "тянет заднюю лапку в высокий батман, держась передней за перекладину-флажок", bg("#E4FAF5", "#5FC9B4", f'''
<path d="M96 30 V116" {ln("#7A5A3A", 4)}/><path d="M96 34 L118 42 L96 50Z" fill="#FFD25E" {s()}/>
<ellipse cx="58" cy="76" rx="22" ry="17" fill="#FFFFFF" {s()}/>
{tutu(58, 86, 28, "#9FF0DC", "#fff")}
<path d="M48 96 L44 120 M64 96 L68 120" {ln("#fff", 7)}/><path d="M48 96 L44 120 M64 96 L68 120" fill="none" {s('stroke-width="2"')} opacity=".0"/>
<rect x="41" y="96" width="8" height="24" rx="4" fill="#fff" {s()}/>
<path d="M74 72 L104 44" {ln(O, 10)}/><path d="M74 72 L104 44" {ln("#fff", 6)}/>
<circle cx="105" cy="42" r="6" fill="#fff" {s()}/>
<circle cx="44" cy="52" r="17" fill="#fff" {s()}/>
<circle cx="34" cy="38" r="8" fill="#fff" {s()}/><circle cx="46" cy="34" r="8" fill="#fff" {s()}/><circle cx="56" cy="40" r="7" fill="#fff" {s()}/>
<ellipse cx="28" cy="56" rx="7" ry="12" fill="#EDEDED" {s()}/><ellipse cx="60" cy="56" rx="7" ry="12" fill="#EDEDED" {s()}/>
{face(44, 54, d=7, k=0.8)}
<ellipse cx="44" cy="61" rx="3" ry="2.2" fill="{O}"/>
<path d="M36 82 Q30 70 22 72" fill="none" {s('stroke-width="2.6"')}/><circle cx="20" cy="72" r="5" fill="#fff" {s()}/>
'''))

# 7. Воронцова-балет — балетная музыкальная шкатулка? нет: пара пуант-ласточек
I["vorontsova-ballet-mira"] = ("ласточка-балерина с хвостом-пачкой",
    "делает прыжок-жете над сценой с бархатным красным полом", bg("#EAF0FF", "#7E92E6", f'''
<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#B3263E" {s()}/>
<path d="M40 64 L8 40 L20 70Z" fill="#2E3A78" {s()}/>
<path d="M88 66 L124 58 L104 84Z" fill="#2E3A78" {s()}/>
<path d="M34 70 Q60 40 96 62 Q80 90 50 86Z" fill="#33408A" {s()}/>
<path d="M44 80 Q66 88 86 70 Q70 92 48 90Z" fill="#fff" {s()}/>
<path d="M52 86 L46 108 M60 88 L70 106" {s('stroke-width="3"')}/>
{tutu(62, 84, 22, "#FFE1EC", "#fff")}
<circle cx="82" cy="52" r="15" fill="#33408A" {s()}/>
<path d="M94 52 L106 50 L95 57Z" fill="#F2A23A" {s('stroke-width="2"')}/>
<circle cx="80" cy="58" r="6" fill="#fff"/>
{eye(78, 49, 0.8)}{eye(88, 49, 0.8)}
<ellipse cx="74" cy="57" rx="3" ry="1.8" fill="#FF7FA8" opacity=".8"/>
<path d="M76 38 l-4 -5 l8 2z" fill="#FF6FA5"/>
{sparkle(28, 28, 5)}{sparkle(110, 26, 4)}
'''))

# 8. Мастерская Антона Николаева, Арбат (3–6 лет) — тюльпан-танцор
I["nikolaev-choreo-arbat"] = ("жёлтый тюльпан-танцор с листиками-руками",
    "кружится на одной ножке-стебле в пятне софита, лепестки разлетаются юбкой", bg("#FFFBE6", "#F3C94A", f'''
<ellipse cx="64" cy="116" rx="34" ry="7" fill="#fff" opacity=".6"/>
<path d="M64 72 Q60 96 64 116" fill="none" {ln(O, 7)}/><path d="M64 72 Q60 96 64 116" fill="none" {ln("#5BB85B", 4)}/>
<path d="M62 92 Q36 92 26 72 Q48 72 62 88Z" fill="#6FCB6A" {s()}/>
<path d="M64 88 Q90 86 102 64 Q78 66 64 84Z" fill="#6FCB6A" {s()}/>
<path d="M38 56 Q34 30 50 22 Q56 38 64 30 Q72 38 78 22 Q94 30 90 56 Q86 78 64 78 Q42 78 38 56Z" fill="#FFB52E" {s()}/>
<path d="M26 64 Q30 58 38 60 M102 60 Q98 54 90 58" fill="none" {s('stroke-width="2.4"')}/>
{face(64, 54, d=9, k=0.95)}
<ellipse cx="18" cy="40" rx="6" ry="3" fill="#FF8A3D" transform="rotate(-30 18 40)" {s('stroke-width="1.6"')}/>
<ellipse cx="110" cy="36" rx="6" ry="3" fill="#FF8A3D" transform="rotate(30 110 36)" {s('stroke-width="1.6"')}/>
'''))

# 9. Flying Dreams, Кабельные — брейкер крутится на голове
I["flying-dreams-kabelny"] = ("мальчишка-брейкер в красной кепке задом наперёд",
    "стоит на голове на картонке и крутит ногами «мельницу»", bg("#E6EEFF", "#4F7FE0", f'''
<path d="M22 112 L106 112 L100 124 L28 124Z" fill="#C9A06B" {s()}/>
<path d="M56 46 L40 14 M72 46 L96 18" {ln(O, 12)}/><path d="M56 46 L40 14 M72 46 L96 18" {ln("#3C3C58", 8)}/>
<path d="M34 10 l12 -4 l4 8 l-12 4z" fill="#fff" {s()}/><path d="M90 14 l12 -2 l2 9 l-12 2z" fill="#fff" {s()}/>
<rect x="46" y="44" width="36" height="34" rx="12" fill="#FFCF3A" {s()}/>
<path d="M46 60 L26 84 M82 60 L102 84" {ln(O, 9)}/><path d="M46 60 L26 84 M82 60 L102 84" {ln("#F4C29A", 5)}/>
<circle cx="24" cy="88" r="5" fill="#F4C29A" {s()}/><circle cx="104" cy="88" r="5" fill="#F4C29A" {s()}/>
<circle cx="64" cy="92" r="16" fill="#F4C29A" {s()}/>
<path d="M48 100 Q64 116 80 100 L80 106 Q64 118 48 106Z" fill="#E2393C" {s()}/>
<path d="M58 108 L50 114" {ln("#E2393C", 5)}/>
{eye(58, 88, 0.85)}{eye(70, 88, 0.85)}
<path d="M60 80 Q64 77 68 80" fill="none" {s('stroke-width="2.4"')}/>
<path d="M20 40 Q14 54 22 64 M108 40 Q116 54 106 64" fill="none" {s('stroke-width="2.4"')} opacity=".7"/>
'''))

# 10. Воздух — облачко-танцор в прыжке
I["vozdukh-muranovskaya"] = ("пушистое облачко с ножками в розовых чешках-кедах",
    "взлетает в танцевальном прыжке «шпагат в воздухе» над крышами", bg("#EEF9FF", "#86CFF4", f'''
<path d="M0 112 L18 96 L36 112 L54 100 L72 112 L92 94 L110 112 L128 102 V128 H0Z" fill="#9AA7C6" {s()}/>
<path d="M44 76 L14 88 M84 76 L114 86" {ln(O, 7)}/><path d="M44 76 L14 88 M84 76 L114 86" {ln("#fff", 3.5)}/>
<ellipse cx="12" cy="89" rx="7" ry="4" fill="#FF8DB4" {s()}/><ellipse cx="116" cy="87" rx="7" ry="4" fill="#FF8DB4" {s()}/>
<path d="M30 66 Q24 46 42 42 Q46 24 66 28 Q82 16 94 34 Q110 36 104 56 Q112 72 92 76 L38 78 Q22 76 30 66Z" fill="#FFFFFF" {s()}/>
<path d="M36 50 L18 34 M96 46 L112 28" {s('stroke-width="3.2"')}/>
{face(64, 52, d=10, k=1.0)}
'''))

# 11. Soul Dance, Энтузиастов — кассета-танцор
I["soul-dance-entuziastov"] = ("оранжевая аудиокассета с мордашкой",
    "танцует хип-хоп и размахивает вытянутой плёнкой как лентой", bg("#FFEEDD", "#FF9A55", f'''
<path d="M40 96 L32 118 M88 96 L98 116" {s('stroke-width="5"')}/>
<path d="M26 116 h12 v6 h-14z M94 114 h12 v6 h-14z" fill="#fff" {s()}/>
<rect x="18" y="38" width="92" height="60" rx="8" fill="#FF7B2E" {s()}/>
<rect x="30" y="48" width="68" height="26" rx="6" fill="#FFF3E2" {s()}/>
<circle cx="46" cy="61" r="9" fill="#fff" {s()}/><circle cx="82" cy="61" r="9" fill="#fff" {s()}/>
{eye(46, 61, 1.0)}{eye(82, 61, 1.0)}
<path d="M58 82 Q64 90 70 82" fill="none" {s('stroke-width="2.6"')}/>
<path d="M34 98 L40 88 H88 L94 98" fill="#E8611C" {s()}/>
<path d="M98 40 Q112 20 98 10 Q86 2 96 -6" fill="none" {ln("#5A3A2A", 3)}/>
<path d="M24 40 Q8 26 18 14" fill="none" {ln("#5A3A2A", 3)}/>
'''))

# 12. Шоу-театр Триумф (танцы и вокал) — цилиндр шоумена
I["triumf-varshavskoe"] = ("блестящий чёрный цилиндр шоумена с золотой лентой",
    "танцует степ с тросточкой под гирляндой лампочек сцены", bg("#FFF1D6", "#E9A23B", f'''
<path d="M0 14 Q64 34 128 14" fill="none" {s('stroke-width="2"')}/>
<circle cx="16" cy="18" r="4" fill="#FFE36A" {s('stroke-width="1.6"')}/><circle cx="40" cy="25" r="4" fill="#FF6A6A" {s('stroke-width="1.6"')}/><circle cx="64" cy="28" r="4" fill="#FFE36A" {s('stroke-width="1.6"')}/><circle cx="88" cy="25" r="4" fill="#6AD0FF" {s('stroke-width="1.6"')}/><circle cx="112" cy="18" r="4" fill="#FFE36A" {s('stroke-width="1.6"')}/>
<path d="M54 96 L48 118 M74 96 L82 116" {s('stroke-width="4"')}/>
<path d="M40 118 h12 v5 h-15z M80 116 h14 v5 h-15z" fill="#222" {s()}/>
<ellipse cx="64" cy="94" rx="40" ry="9" fill="#2A2A3A" {s()}/>
<path d="M38 92 L42 44 Q64 36 86 44 L90 92Z" fill="#2E2E44" {s()}/>
<path d="M40 80 Q64 86 88 80 L89 90 Q64 96 39 90Z" fill="#F2C230" {s()}/>
<ellipse cx="64" cy="42" rx="22" ry="5" fill="#45455F" {s()}/>
{face(64, 62, d=9, k=0.95)}
<path d="M90 70 L108 58" {s('stroke-width="3"')}/><path d="M108 58 L104 104" {ln("#F2C230", 4)}/><path d="M108 58 Q114 52 118 58" fill="none" {ln("#F2C230", 4)}/>
<path d="M38 70 L22 60" {s('stroke-width="3"')}/>
{note(18, 52, 0.8)}
'''))

# 13. Invibe, Внуково — неоновая колонка? нет: девочка в толстовке танцует
I["invibe-vnukovo"] = ("девочка в фиолетовой толстовке с хвостиками",
    "танцует хип-хоп «волну» руками у большого зеркала зала", bg("#F3E8FF", "#9C6BE8", f'''
<rect x="72" y="8" width="56" height="100" fill="#DCEBFF" {s()}/><path d="M84 20 L100 40 M92 16 L114 44" {ln("#fff", 4)}/>
<rect x="0" y="108" width="128" height="20" fill="#C79A62"/><path d="M0 108 H128" {s()}/>
<path d="M50 96 L44 116 M64 96 L72 116" {s('stroke-width="5"')}/>
<path d="M38 114 h12 v6 h-14z M70 114 h12 v6 h-12z" fill="#fff" {s()}/>
<path d="M40 64 Q56 54 70 64 L72 98 L38 98Z" fill="#8E4FE0" {s()}/>
<path d="M42 70 Q28 64 22 72 Q16 80 8 74" fill="none" {ln(O, 8)}/><path d="M42 70 Q28 64 22 72 Q16 80 8 74" fill="none" {ln("#8E4FE0", 4.5)}/>
<path d="M68 70 Q82 76 88 66 Q94 56 102 62" fill="none" {ln(O, 8)}/><path d="M68 70 Q82 76 88 66 Q94 56 102 62" fill="none" {ln("#8E4FE0", 4.5)}/>
<circle cx="55" cy="44" r="16" fill="#F6C9A4" {s()}/>
<path d="M39 42 Q40 26 55 26 Q70 26 71 42 Q62 34 55 34 Q48 34 39 42Z" fill="#5A3A22" {s()}/>
<circle cx="36" cy="32" r="6" fill="#5A3A22" {s()}/><circle cx="74" cy="32" r="6" fill="#5A3A22" {s()}/>
{face(55, 46, d=6, k=0.7)}
'''))

# 14. Академия Игоря Крутого — золотой микрофон на стойке в луче прожектора
I["akademiya-krutogo-myasnitskaya"] = ("золотой микрофон на высокой стойке",
    "поёт на тёмной сцене в луче прожектора, из сетки вылетают ноты", bg("#4B4A8F", "#1F1E4A", f'''
<path d="M64 0 L24 128 H104Z" fill="#FFF6C8" opacity=".35"/>
<ellipse cx="64" cy="118" rx="30" ry="6" fill="#FFF6C8" opacity=".5"/>
<path d="M64 76 V116 M50 118 H78" {ln(O, 7)}/><path d="M64 76 V116 M50 118 H78" {ln("#B9BCC8", 4)}/>
<rect x="44" y="24" width="40" height="58" rx="20" fill="#F2C230" {s()}/>
<path d="M46 40 H82 M46 50 H82" {ln("#C9971A", 2)}/>
{face(64, 62, d=9, k=0.95)}
{note(100, 46, 1.0, "#FFE36A")}{note(22, 40, 0.8, "#FFE36A")}
{sparkle(104, 22, 5)}
'''))

# 15. Дыхание звука — соловей-солист
I["dykhanie-zvuka-mytishchinskaya"] = ("коричневый соловей-солист с раскрытым клювом",
    "поёт на цветущей ветке, изо рта плывёт волна нот", bg("#E9FBEF", "#7DD49A", f'''
<path d="M0 100 Q50 92 120 108" fill="none" {ln(O, 9)}/><path d="M0 100 Q50 92 120 108" fill="none" {ln("#8A5A33", 5)}/>
<circle cx="18" cy="92" r="6" fill="#FFC1DA" {s('stroke-width="2"')}/><circle cx="104" cy="100" r="6" fill="#FFC1DA" {s('stroke-width="2"')}/>
<path d="M50 72 L30 90 L40 92Z" fill="#8F6440" {s()}/>
<ellipse cx="62" cy="70" rx="24" ry="22" fill="#A8754A" {s()}/>
<ellipse cx="66" cy="78" rx="14" ry="12" fill="#F4E1C4"/>
<path d="M54 92 L52 98 M66 92 L68 98" {s('stroke-width="2.6"')}/>
<circle cx="70" cy="50" r="17" fill="#A8754A" {s()}/>
<path d="M85 46 L102 40 L86 52 L100 58 L85 56Z" fill="#F2A23A" {s('stroke-width="2.2"')}/>
<path d="M60 44 Q64 40 68 44" fill="none" {s('stroke-width="2.6"')}/><path d="M74 44 Q78 40 82 44" fill="none" {s('stroke-width="2.6"')}/>
<ellipse cx="66" cy="56" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
{note(104, 28, 0.9)}{note(116, 52, 0.7)}{note(92, 16, 0.6)}
'''))

# 17. КидсВокс, Матвеевская (хор 5–7) — малыш в гарнитуре
I["kidsvoks-matveevskaya"] = ("кудрявый малыш с микрофоном-гарнитурой у щеки",
    "поёт, зажмурившись от удовольствия, в окружении разноцветных нот-пузырей", bg("#E5F7FF", "#62B9E8", f'''
<path d="M30 128 Q30 92 64 90 Q98 92 98 128Z" fill="#FF6F61" {s()}/>
<circle cx="64" cy="62" r="28" fill="#F6CDA8" {s()}/>
<circle cx="44" cy="40" r="10" fill="#E0A040" {s()}/><circle cx="58" cy="34" r="11" fill="#E0A040" {s()}/><circle cx="74" cy="34" r="11" fill="#E0A040" {s()}/><circle cx="86" cy="42" r="10" fill="#E0A040" {s()}/>
<path d="M36 58 Q34 34 64 34 Q94 34 92 58" fill="none" {ln(O, 5)}/><path d="M36 58 Q34 34 64 34 Q94 34 92 58" fill="none" {ln("#4A4A60", 3)}/>
<rect x="30" y="52" width="10" height="16" rx="4" fill="#4A4A60" {s()}/>
<path d="M36 68 Q42 82 56 80" fill="none" {s('stroke-width="2.6"')}/><circle cx="57" cy="80" r="3.5" fill="{O}"/>
<path d="M52 60 Q56 56 60 60 M68 60 Q72 56 76 60" fill="none" {s('stroke-width="2.6"')}/>
<ellipse cx="64" cy="74" rx="6" ry="5" fill="#C2405A" {s('stroke-width="2"')}/>
<ellipse cx="48" cy="68" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="82" cy="68" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
<circle cx="104" cy="44" r="10" fill="#FFE36A" opacity=".8" {s('stroke-width="2"')}/>{note(101, 49, 0.55)}
<circle cx="20" cy="38" r="9" fill="#9BE07A" opacity=".8" {s('stroke-width="2"')}/>{note(17, 43, 0.5)}
'''))

# 18. ДЮЦ «Виктория», хоровая студия Аннино — хоровая папка
I["viktoriya-khor-annino"] = ("синяя хоровая папка с золотым скрипичным уголком",
    "раскрылась, и из неё поют три нотки-хористки в ряд", bg("#EEF2FF", "#8A9BE8", f'''
<path d="M14 64 L60 56 L64 116 L18 120Z" fill="#2F55B5" {s()}/>
<path d="M114 64 L68 56 L64 116 L110 120Z" fill="#2F55B5" {s()}/>
<path d="M20 68 L58 62 L60 110 L24 114Z M108 68 L70 62 L68 110 L104 114Z" fill="#FFFDF4" {s('stroke-width="2"')}/>
<path d="M26 78 L56 74 M26 86 L56 82 M26 94 L56 90 M72 74 L102 78 M72 82 L102 86 M72 90 L102 94" {ln("#B9B9D0", 1.6)}/>
<g>
<ellipse cx="36" cy="40" rx="10" ry="8" fill="#E2393C" {s()}/><path d="M46 38 V14" {s('stroke-width="3"')}/>
{eye(33, 39, 0.5)}{eye(39, 39, 0.5)}<circle cx="36" cy="44" r="1.8" fill="{O}"/>
<ellipse cx="64" cy="34" rx="10" ry="8" fill="#2FA84F" {s()}/><path d="M74 32 V8" {s('stroke-width="3"')}/>
{eye(61, 33, 0.5)}{eye(67, 33, 0.5)}<circle cx="64" cy="38" r="1.8" fill="{O}"/>
<ellipse cx="92" cy="40" rx="10" ry="8" fill="#F2A23A" {s()}/><path d="M102 38 V14" {s('stroke-width="3"')}/>
{eye(89, 39, 0.5)}{eye(95, 39, 0.5)}<circle cx="92" cy="44" r="1.8" fill="{O}"/>
</g>
'''))

# 19. ДоСиМи и STARше — лесенка «до-ре-ми» с нотками
I["dosimi-novopeschanaya"] = ("лесенка из семи разноцветных ступенек-клавиш до-ре-ми",
    "по ней вприпрыжку взбирается нотка в звёздной короне", bg("#FFF0FA", "#F28DC5", f'''
<rect x="8" y="104" width="16" height="18" fill="#FF5A5A" {s()}/>
<rect x="24" y="94" width="16" height="28" fill="#FF9A3A" {s()}/>
<rect x="40" y="84" width="16" height="38" fill="#FFD83A" {s()}/>
<rect x="56" y="74" width="16" height="48" fill="#5ACB5A" {s()}/>
<rect x="72" y="64" width="16" height="58" fill="#4AB8F0" {s()}/>
<rect x="88" y="54" width="16" height="68" fill="#5A6AF0" {s()}/>
<rect x="104" y="44" width="16" height="78" fill="#A85AF0" {s()}/>
<ellipse cx="64" cy="58" rx="12" ry="10" fill="#3B3355" transform="rotate(-20 64 58)"/>
<path d="M74 54 V24 Q86 28 88 38" fill="none" {ln(O, 4)}/>
{eye(60, 57, 0.6)}{eye(67, 55, 0.6)}
<path d="M58 22 l4 -8 l4 8 l6 -6 l-2 10 h-14 l-2 -10z" fill="#FFE36A" {s('stroke-width="2"')} transform="translate(-2 4)"/>
{sparkle(30, 36, 6)}{sparkle(108, 24, 5)}
'''))

# 20. Музыкальная дорожка, Алтуфьево — пюпитр
I["muz-dorozhka-altufyevskoe"] = ("складной чёрный пюпитр для нот",
    "держит раскрытые ноты, по которым шагает дорожка следов-нот", bg("#F0FFF4", "#73CC8A", f'''
<path d="M64 74 V118 M64 118 L44 124 M64 118 L84 124" {ln(O, 6)}/><path d="M64 74 V118" {ln("#3C3C50", 3)}/>
<path d="M22 30 H106 L100 78 H28Z" fill="#3C3C50" {s()}/>
<rect x="30" y="20" width="32" height="44" fill="#FFFDF2" {s()} transform="rotate(-4 46 42)"/>
<rect x="66" y="20" width="32" height="44" fill="#FFFDF2" {s()} transform="rotate(4 82 42)"/>
<path d="M34 32 H58 M34 38 H58 M34 44 H58 M70 32 H94 M70 38 H94 M70 44 H94" {ln("#A0A0B8", 1.4)}/>
<circle cx="40" cy="50" r="2.6" fill="{O}"/><circle cx="50" cy="44" r="2.6" fill="{O}"/><circle cx="76" cy="38" r="2.6" fill="{O}"/><circle cx="88" cy="32" r="2.6" fill="{O}"/>
{face(64, 66, d=12, k=0.9, mouth=True)}
<ellipse cx="20" cy="104" rx="4" ry="6" fill="#2F9E4F"/><ellipse cx="30" cy="96" rx="4" ry="6" fill="#2F9E4F"/><ellipse cx="98" cy="96" rx="4" ry="6" fill="#2F9E4F"/><ellipse cx="108" cy="104" rx="4" ry="6" fill="#2F9E4F"/>
'''))

# 21. Три четверти, Внуково — камертон
I["tri-chetverti-vnukovo"] = ("стальной камертон с двумя зубцами",
    "звенит от лёгкого удара, вокруг расходятся кольца звука и висит знак «3/4»", bg("#EAF6FF", "#7DB8E8", f'''
<circle cx="64" cy="54" r="40" fill="none" {ln("#fff", 3)} opacity=".7"/><circle cx="64" cy="54" r="52" fill="none" {ln("#fff", 2)} opacity=".5"/>
<path d="M50 20 V70 Q50 86 64 86 Q78 86 78 70 V20" fill="none" {ln(O, 15)}/>
<path d="M50 20 V70 Q50 86 64 86 Q78 86 78 70 V20" fill="none" {ln("#C9D2E0", 10)}/>
<path d="M64 86 V118" {ln(O, 11)}/><path d="M64 86 V116" {ln("#C9D2E0", 6)}/>
<ellipse cx="64" cy="120" rx="8" ry="5" fill="#8A93A6" {s()}/>
{eye(58, 74, 0.6)}{eye(70, 74, 0.6)}<path d="M61 79 Q64 82 67 79" fill="none" {s('stroke-width="1.8"')}/>
<text x="92" y="108" font-family="Arial" font-weight="bold" font-size="20" fill="{O}">3</text><path d="M104 100 L110 86" {s('stroke-width="2.4"')}/><text x="108" y="96" font-family="Arial" font-weight="bold" font-size="13" fill="{O}" opacity="0">.</text>
<text x="12" y="44" font-family="Arial" font-weight="bold" font-size="18" fill="{O}">4</text>
'''))

# 22. Гитарная школа №1, Лефортово — электрогитара-молния
I["guitar-school-1-krasnokazarmennaya"] = ("красная электрогитара с грифом-молнией",
    "лихо берёт рок-аккорд, а из усилителя рядом вылетают искры", bg("#FFECEC", "#F07C7C", f'''
<rect x="86" y="80" width="30" height="36" rx="4" fill="#3C3C50" {s()}/><circle cx="101" cy="98" r="10" fill="#6A6A80" {s()}/><circle cx="101" cy="98" r="4" fill="#3C3C50"/>
<path d="M66 60 L74 40 L66 38 L78 10" fill="none" {ln(O, 11)}/><path d="M66 60 L74 40 L66 38 L78 10" fill="none" {ln("#F2C230", 6)}/>
<path d="M30 70 Q24 54 40 52 Q52 50 58 58 Q70 52 76 64 Q82 80 70 88 Q74 106 54 110 Q30 114 26 96 Q22 82 30 70Z" fill="#E2393C" {s()}/>
<rect x="40" y="88" width="28" height="7" rx="2" fill="#2E2E3E" {s('stroke-width="2"')}/>
{face(50, 72, d=8, k=0.85)}
{sparkle(110, 66, 6, "#FFE36A")}{sparkle(98, 50, 4, "#FFE36A")}
'''))

# 23. Гитарная школа №1, Староватутинский — медиатор-великан
I["guitar-school-1-starovatutinsky"] = ("большой фиолетовый гитарный медиатор с мордашкой",
    "бренчит по шести струнам гитарного грифа, струны вибрируют волной", bg("#F4ECFF", "#B08AF0", f'''
<rect x="-6" y="70" width="140" height="34" fill="#8A5A33" {s()}/>
<path d="M-6 75 Q32 71 64 75 T134 75 M-6 80 H134 M-6 85 Q32 89 64 85 T134 85 M-6 90 H134 M-6 95 Q32 91 64 95 T134 95 M-6 100 H134" {ln("#F0E3C8", 1.6)}/>
<path d="M20 70 V104 M44 70 V104 M84 70 V104 M108 70 V104" {ln("#D8C9A8", 2.5)}/>
<path d="M64 98 Q30 60 34 34 Q38 14 64 14 Q90 14 94 34 Q98 60 64 98Z" fill="#8F4FE0" {s()}/>
<path d="M46 26 Q52 20 60 20" fill="none" {ln("#fff", 3)} opacity=".6"/>
{face(64, 46, d=11, k=1.0)}
'''))

# 24. Терция, Бабушкинская — синтезатор
I["tertsiya-lenskaya"] = ("белый синтезатор на подставке-иксе",
    "клавиши сами нажимаются, на дисплее прыгает зелёная волна звука", bg("#E7FFF6", "#5FCDA8", f'''
<path d="M30 116 L98 82 M98 116 L30 82" {ln(O, 6)}/><path d="M30 116 L98 82 M98 116 L30 82" {ln("#6A6A80", 3)}/>
<rect x="8" y="42" width="112" height="44" rx="8" fill="#F4F6FA" {s()}/>
<rect x="44" y="48" width="40" height="14" rx="3" fill="#1F3A3A" {s('stroke-width="2"')}/>
<path d="M48 55 Q52 49 56 55 T64 55 T72 55 T80 55" fill="none" {ln("#5CF0A8", 2)}/>
<rect x="14" y="66" width="100" height="16" fill="#fff" {s('stroke-width="2"')}/>
<path d="M24 66 V82 M34 66 V82 M44 66 V82 M54 66 V82 M64 66 V82 M74 66 V82 M84 66 V82 M94 66 V82 M104 66 V82" {ln(O, 1.6)}/>
<rect x="20" y="66" width="7" height="9" fill="{O}"/><rect x="30" y="66" width="7" height="9" fill="{O}"/><rect x="50" y="66" width="7" height="9" fill="{O}"/><rect x="60" y="66" width="7" height="9" fill="{O}"/><rect x="70" y="66" width="7" height="9" fill="{O}"/><rect x="90" y="66" width="7" height="9" fill="{O}"/><rect x="100" y="66" width="7" height="9" fill="{O}"/>
{eye(26, 54, 0.8)}{eye(36, 54, 0.8)}<path d="M28 60 Q31 62 34 60" fill="none" {s('stroke-width="2"')}/>
<circle cx="96" cy="54" r="4" fill="#FF6A6A" {s('stroke-width="1.6"')}/><circle cx="108" cy="54" r="4" fill="#FFD83A" {s('stroke-width="1.6"')}/>
{note(30, 30, 0.8)}{note(96, 26, 0.9)}
'''))

# 25. Школа музыки Купиной (2–7 лет) — тамбурин
I["kupina-ivovaya"] = ("круглый тамбурин с бубенцами-тарелочками",
    "весело подпрыгивает и звенит, рядом прыгают маленькие нотки-зайчики", bg("#FFF4E4", "#F7B661", f'''
<circle cx="64" cy="66" r="40" fill="#F7E3B8" {s()}/>
<circle cx="64" cy="66" r="40" fill="none" {ln("#D9452B", 9)}/><circle cx="64" cy="66" r="44.5" fill="none" {s('stroke-width="2"')}/><circle cx="64" cy="66" r="35.5" fill="none" {s('stroke-width="2"')}/>
<ellipse cx="64" cy="22" rx="7" ry="4" fill="#F2C230" {s('stroke-width="2"')}/><ellipse cx="64" cy="110" rx="7" ry="4" fill="#F2C230" {s('stroke-width="2"')}/>
<ellipse cx="20" cy="66" rx="4" ry="7" fill="#F2C230" {s('stroke-width="2"')}/><ellipse cx="108" cy="66" rx="4" ry="7" fill="#F2C230" {s('stroke-width="2"')}/>
<ellipse cx="33" cy="35" rx="6" ry="4" fill="#F2C230" {s('stroke-width="2"')} transform="rotate(-45 33 35)"/><ellipse cx="95" cy="97" rx="6" ry="4" fill="#F2C230" {s('stroke-width="2"')} transform="rotate(-45 95 97)"/>
{face(64, 64, d=11, k=1.1)}
<path d="M14 24 l4 -6 M20 26 l6 -4 M108 28 l6 -4 M110 34 l7 0" {s('stroke-width="2.4"')}/>
'''))

# 26. Русская речь, Архитектора Власова — книжка-пьеса читает монолог
I["russkaya-rech-vlasova"] = ("раскрытая красная книжка-пьеса с мордашкой на обложке",
    "стоит на табурете и читает монолог, из страниц вылетает буква «А»", bg("#FFF5EE", "#F2A48A", f'''
<rect x="40" y="96" width="48" height="8" rx="3" fill="#B5844F" {s()}/><path d="M46 104 L42 124 M82 104 L86 124" {ln(O, 5)}/>
<path d="M64 40 Q42 30 20 38 V96 Q42 88 64 96Z" fill="#fff" {s()}/>
<path d="M64 40 Q86 30 108 38 V96 Q86 88 64 96Z" fill="#fff" {s()}/>
<path d="M64 44 Q44 34 24 42 V98 Q44 92 64 100 Q84 92 104 98 V42 Q84 34 64 44" fill="none" {ln("#D1323F", 4)}/>
<path d="M28 52 Q42 48 56 52 M28 60 Q42 56 56 60 M72 52 Q86 48 100 52 M72 60 Q86 56 100 60" {ln("#B9B9D0", 1.8)}/>
{eye(42, 74, 0.9)}{eye(86, 74, 0.9)}
<path d="M56 82 Q64 90 72 82" fill="none" {s('stroke-width="2.6"')}/>
<text x="76" y="28" font-family="Georgia" font-weight="bold" font-size="22" fill="#D1323F" transform="rotate(12 84 20)">А</text>
'''))

# 27. НАТ 2.0, Профсоюзная — театральный звонок
I["nat-profsoyuznaya"] = ("медный театральный звонок-колокольчик с деревянной ручкой",
    "звенит третий звонок, вокруг пляшут три восклицательных искорки", bg("#FFF8E6", "#E8B455", f'''
<path d="M64 14 V34" {ln(O, 13)}/><path d="M64 14 V34" {ln("#8A5A33", 8)}/>
<circle cx="64" cy="12" r="7" fill="#8A5A33" {s()}/>
<path d="M30 92 Q34 40 64 36 Q94 40 98 92Z" fill="#E0A23A" {s()}/>
<ellipse cx="64" cy="92" rx="38" ry="8" fill="#C9861F" {s()}/>
<circle cx="64" cy="104" r="7" fill="#C9861F" {s()}/>
<path d="M40 56 Q44 46 52 44" fill="none" {ln("#FFE7A6", 3)}/>
{face(64, 66, d=11, k=1.0)}
<path d="M14 50 L22 54 M12 66 L22 66 M14 82 L22 78 M114 50 L106 54 M116 66 L106 66 M114 82 L106 78" {s('stroke-width="3"')}/>
<text x="100" y="118" font-family="Arial" font-weight="bold" font-size="16" fill="{O}">3</text>
'''))

# 28. Action, Красный Октябрь — софит
I["action-krasny-oktyabr"] = ("чёрный театральный софит на штативе",
    "светит лучом на пустую сцену на фоне кирпичной стены фабрики", bg("#F6E2D6", "#C9785A", f'''
<path d="M0 10 H128 M0 24 H128 M0 38 H128 M20 10 V24 M52 10 V24 M84 10 V24 M116 10 V24 M36 24 V38 M68 24 V38 M100 24 V38" {ln("#A8573E", 2)}/>
<path d="M58 62 L128 96 V128 H80Z" fill="#FFF6C8" opacity=".55"/>
<ellipse cx="104" cy="116" rx="20" ry="6" fill="#FFF6C8" opacity=".8"/>
<path d="M40 74 V112 M40 112 L22 124 M40 112 L58 124" {ln(O, 6)}/><path d="M40 74 V112" {ln("#555", 3)}/>
<rect x="14" y="44" width="50" height="34" rx="10" fill="#2E2E3E" {s()} transform="rotate(20 39 61)"/>
<ellipse cx="62" cy="70" rx="8" ry="15" fill="#FFF3A6" {s()} transform="rotate(20 62 70)"/>
{eye(30, 56, 0.8)}{eye(42, 60, 0.8)}<path d="M32 66 Q36 69 40 67" fill="none" {ln("#fff", 2)}/>
'''))

# 29. ЛиссЭ, Арбат — гримёрное зеркало с лампочками
I["lisse-arbat"] = ("гримёрное зеркало в раме из круглых лампочек",
    "рисует себе нарисованные усы кисточкой для грима", bg("#FCEBFF", "#D88BE8", f'''
<rect x="22" y="18" width="84" height="80" rx="8" fill="#F2D8A6" {s()}/>
<rect x="34" y="30" width="60" height="56" rx="4" fill="#CFE9F7" {s()}/>
<path d="M42 40 L54 34 M42 50 L64 36" {ln("#fff", 3)} opacity=".8"/>
<g fill="#FFF7B0" {s('stroke-width="1.8"')}><circle cx="28" cy="30" r="4"/><circle cx="28" cy="50" r="4"/><circle cx="28" cy="70" r="4"/><circle cx="28" cy="90" r="4"/><circle cx="100" cy="30" r="4"/><circle cx="100" cy="50" r="4"/><circle cx="100" cy="70" r="4"/><circle cx="100" cy="90" r="4"/><circle cx="48" cy="24" r="4"/><circle cx="64" cy="24" r="4"/><circle cx="80" cy="24" r="4"/></g>
{eye(54, 56, 0.9)}{eye(74, 56, 0.9)}
<path d="M48 66 Q56 76 64 68 Q72 76 80 66" fill="none" {ln(O, 3.5)}/>
<rect x="30" y="98" width="68" height="10" rx="3" fill="#8A5A33" {s()}/>
<path d="M98 76 L118 108" {ln(O, 6)}/><path d="M98 76 L118 108" {ln("#E8C27A", 3)}/><path d="M94 70 L100 78" {ln(O, 5)}/>
'''))

# 30. Буфф, Фадеева — шутовской колпак
I["buff-fadeeva"] = ("двухцветный шутовской колпак с бубенцами",
    "кувыркается колесом по сцене, бубенцы звенят", bg("#FFF0E0", "#F2A060", f'''
<path d="M10 116 Q64 104 118 116 V128 H10Z" fill="#8A5A33" {s()}/>
<path d="M30 84 Q20 50 6 40 Q36 38 52 58Z" fill="#2E8BE0" {s()}/>
<path d="M98 84 Q108 50 122 40 Q92 38 76 58Z" fill="#F2C230" {s()}/>
<path d="M44 82 Q48 30 64 14 Q80 30 84 82Z" fill="#E2393C" {s()}/>
<path d="M28 84 Q64 74 100 84 L100 96 Q64 88 28 96Z" fill="#fff" {s()}/>
<circle cx="6" cy="40" r="6" fill="#FFE36A" {s()}/><circle cx="122" cy="40" r="6" fill="#FFE36A" {s()}/><circle cx="64" cy="12" r="6" fill="#FFE36A" {s()}/>
{face(64, 104, d=9, k=0.8)}
<path d="M14 26 l-4 -4 M114 26 l4 -4 M58 2 l-2 -4" {s('stroke-width="2"')}/>
'''))

# 31. Театр-Мира — земной шар кланяется
I["teatr-mira-mytishchinskaya"] = ("голубой земной шар в театральной полумаске",
    "кланяется со сцены под аплодисменты, в руке — роза", bg("#EDF7FF", "#6FA9E8", f'''
<path d="M0 108 H128 V128 H0Z" fill="#7A3B2E"/><path d="M0 108 H128" {s()}/>
<path d="M0 0 H22 Q18 50 0 70Z M128 0 H106 Q110 50 128 70Z" fill="#C2263C" {s()}/>
<circle cx="64" cy="64" r="34" fill="#4AA8F0" {s()} transform="rotate(14 64 64)"/>
<path d="M44 44 Q52 36 60 44 Q58 56 46 58Z M70 70 Q84 62 92 74 Q86 88 74 86Z M64 90 Q70 94 62 98Z" fill="#6FD06A" {s('stroke-width="2"')}/>
<path d="M42 56 Q48 46 60 52 Q64 48 68 52 Q80 46 86 56 Q82 66 70 62 Q64 58 58 62 Q46 66 42 56Z" fill="#7B3FC4" {s()}/>
{eye(52, 56, 0.6)}{eye(76, 56, 0.6)}
<path d="M56 74 Q64 80 72 74" fill="none" {s('stroke-width="2.6"')}/>
<path d="M30 80 L18 98" {s('stroke-width="3"')}/><circle cx="16" cy="100" r="6" fill="#E2393C" {s()}/><path d="M16 106 V116" {ln("#2F9E4F", 3)}/>
'''))

# 32. Шум, Газопровод — трещотка
I["shum-gazoprovod"] = ("деревянная народная трещотка-веер на шнурке",
    "громко трещит на сцене, разбрасывая звуковые зигзаги", bg("#FFF3E8", "#E89A5A", f'''
<path d="M64 112 L30 40 M64 112 L44 34 M64 112 L58 30 M64 112 L72 30 M64 112 L86 34 M64 112 L100 40" {ln(O, 13)}/>
<path d="M64 112 L30 40" {ln("#E2B57A", 8)}/><path d="M64 112 L44 34" {ln("#D9A060", 8)}/><path d="M64 112 L58 30" {ln("#E2B57A", 8)}/>
<path d="M64 112 L72 30" {ln("#D9A060", 8)}/><path d="M64 112 L86 34" {ln("#E2B57A", 8)}/><path d="M64 112 L100 40" {ln("#D9A060", 8)}/>
<path d="M28 46 Q64 26 102 46" fill="none" {ln("#E2393C", 3)}/>
<rect x="44" y="56" width="40" height="30" rx="12" fill="#F4D7A8" {s()}/>
{face(64, 68, d=8, k=0.85)}
<path d="M8 60 l8 -6 l-2 8 l8 -6 M120 60 l-8 -6 l2 8 l-8 -6 M10 88 l8 -2 l-4 6 l8 -2 M118 88 l-8 -2 l4 6 l-8 -2" fill="none" {s('stroke-width="2.6"')}/>
<path d="M64 112 Q60 122 70 126" fill="none" {ln("#E2393C", 3)}/>
'''))

# 33. АзАрт+, Сокол — театральный билет
I["azart-supruna"] = ("театральный билетик с отрывным корешком",
    "вприпрыжку бежит на спектакль, размахивая корешком как флажком", bg("#EFFFF0", "#7CCB7A", f'''
<path d="M20 44 H96 Q96 52 104 52 V82 Q96 82 96 90 H20 Q20 82 12 82 V52 Q20 52 20 44Z" fill="#FFE08A" {s()} transform="rotate(-10 58 67)"/>
<path d="M78 48 V88" {s('stroke-width="2"')} stroke-dasharray="4 4" transform="rotate(-10 58 67)"/>
<path d="M84 58 L94 56 M84 66 L95 64 M84 74 L94 72" {s('stroke-width="2"')} transform="rotate(-10 58 67)"/>
{face(46, 64, d=10, k=1.0)}
<path d="M40 92 L34 116 M56 90 L66 112" {s('stroke-width="4"')}/>
<path d="M28 116 h10 v5 h-12z M64 112 h10 v5 h-12z" fill="#E2393C" {s()}/>
<path d="M104 52 L118 22" {s('stroke-width="2.6"')}/><path d="M118 22 L104 18 L110 30Z" fill="#E2393C" {s('stroke-width="2"')}/>
'''))

# 34. Акт Плэйс, Полярная — занавес северного сияния
I["act-place-polyarnaya"] = ("занавес из северного сияния",
    "раздвигается над сценой, а из-за него выглядывает белый медвежонок-актёр", bg("#1E2A5A", "#0E1534", f'''
<circle cx="20" cy="22" r="1.6" fill="#fff"/><circle cx="104" cy="14" r="1.6" fill="#fff"/><circle cx="64" cy="10" r="1.4" fill="#fff"/>
<path d="M0 6 Q20 40 6 70 Q2 90 0 104Z" fill="#46E0A0" opacity=".9" {s()}/>
<path d="M128 6 Q108 40 122 70 Q126 90 128 104Z" fill="#B06AF0" opacity=".9" {s()}/>
<path d="M0 6 Q64 26 128 6 V16 Q64 36 0 16Z" fill="#4AB8F0" {s()}/>
<path d="M0 104 H128 V128 H0Z" fill="#6A4A8A"/><path d="M0 104 H128" {s()}/>
<circle cx="64" cy="76" r="26" fill="#FFFFFF" {s()}/>
<circle cx="44" cy="56" r="8" fill="#fff" {s()}/><circle cx="84" cy="56" r="8" fill="#fff" {s()}/>
<ellipse cx="64" cy="84" rx="10" ry="7" fill="#F0F0F6" {s('stroke-width="2"')}/><ellipse cx="64" cy="81" rx="3.4" ry="2.4" fill="{O}"/>
{eye(55, 72, 0.85)}{eye(73, 72, 0.85)}
<ellipse cx="48" cy="82" rx="3.5" ry="2" fill="#FF7FA8" opacity=".7"/><ellipse cx="80" cy="82" rx="3.5" ry="2" fill="#FF7FA8" opacity=".7"/>
<path d="M60 88 Q64 92 68 88" fill="none" {s('stroke-width="2"')}/>
'''))

# 35. Арт Инсайт, Ривьера — акварельная коробка
I["art-insight-avtozavodskaya"] = ("коробка акварели с двенадцатью цветными кюветами",
    "открыла крышку и улыбается, а мокрая кисточка макает в синюю кювету", bg("#F2F7FF", "#9AB4F0", f'''
<rect x="14" y="22" width="100" height="34" rx="6" fill="#2F55B5" {s()} transform="rotate(-8 64 39)"/>
<rect x="14" y="58" width="100" height="56" rx="6" fill="#fff" {s()}/>
<g {s('stroke-width="2"')}>
<rect x="22" y="64" width="16" height="12" rx="3" fill="#E2393C"/><rect x="42" y="64" width="16" height="12" rx="3" fill="#FF9A3A"/><rect x="62" y="64" width="16" height="12" rx="3" fill="#FFD83A"/><rect x="82" y="64" width="16" height="12" rx="3" fill="#5ACB5A"/>
<rect x="22" y="96" width="16" height="12" rx="3" fill="#2FB8E0"/><rect x="42" y="96" width="16" height="12" rx="3" fill="#3A5AE0"/><rect x="62" y="96" width="16" height="12" rx="3" fill="#A85AF0"/><rect x="82" y="96" width="16" height="12" rx="3" fill="#8A5A33"/>
</g>
{face(60, 84, d=10, k=0.8)}
<path d="M120 10 L52 100" {ln(O, 6)}/><path d="M120 10 L60 90" {ln("#E8C27A", 3)}/><path d="M58 92 Q48 104 50 108 Q56 104 62 96Z" fill="#3A5AE0" {s('stroke-width="2"')}/>
'''))

# 36. СтАрт, Братеево — восковые мелки рисуют радугу
I["start-brateevskaya"] = ("три толстых восковых мелка в бумажных обёртках",
    "наперегонки рисуют на листе радугу, оставляя полосы", bg("#FFFBEF", "#F2D17A", f'''
<rect x="8" y="70" width="112" height="50" rx="4" fill="#fff" {s()}/>
<path d="M14 112 Q40 80 64 100" fill="none" {ln("#E2393C", 6)}/><path d="M18 114 Q44 88 68 106" fill="none" {ln("#FFB52E", 6)}/><path d="M22 116 Q48 96 72 112" fill="none" {ln("#2FB8E0", 6)}/>
<g transform="rotate(30 64 64)">
<rect x="58" y="14" width="18" height="62" rx="4" fill="#E2393C" {s()}/><path d="M58 76 L67 92 L76 76Z" fill="#E2393C" {s()}/><rect x="58" y="34" width="18" height="24" fill="#FFF0F0" {s('stroke-width="2"')}/>
{eye(63, 44, 0.55)}{eye(71, 44, 0.55)}<path d="M64 50 Q67 52 70 50" fill="none" {s('stroke-width="1.6"')}/>
</g>
<g transform="rotate(10 40 50)"><rect x="32" y="16" width="16" height="56" rx="4" fill="#FFB52E" {s()}/><path d="M32 72 L40 86 L48 72Z" fill="#FFB52E" {s()}/><rect x="32" y="34" width="16" height="20" fill="#FFF6E0" {s('stroke-width="2"')}/>{eye(37, 42, 0.5)}{eye(44, 42, 0.5)}</g>
<g transform="rotate(50 98 46)"><rect x="90" y="10" width="16" height="56" rx="4" fill="#2FB8E0" {s()}/><path d="M90 66 L98 80 L106 66Z" fill="#2FB8E0" {s()}/><rect x="90" y="28" width="16" height="20" fill="#E8F8FF" {s('stroke-width="2"')}/>{eye(95, 36, 0.5)}{eye(102, 36, 0.5)}</g>
'''))

# 37. Центр искусств «Ритм», Мосфильмовская — клякса прыгает
I["ritm-mosfilmovskaya"] = ("фиолетовая клякса краски с мордашкой",
    "прыгает по белому листу и оставляет за собой цветные отпечатки-следы", bg("#F7F0FF", "#C79BF0", f'''
<rect x="10" y="66" width="108" height="54" rx="4" fill="#fff" {s()} transform="rotate(4 64 93)"/>
<circle cx="24" cy="106" r="6" fill="#FFD83A"/><circle cx="40" cy="96" r="6" fill="#5ACB5A"/><circle cx="56" cy="104" r="6" fill="#2FB8E0"/><circle cx="20" cy="92" r="3" fill="#FFD83A"/>
<path d="M70 26 Q84 12 96 24 Q114 22 110 40 Q124 52 108 62 Q110 80 92 76 Q80 90 70 76 Q52 80 56 62 Q42 50 56 40 Q54 24 70 26Z" fill="#8F4FE0" {s()}/>
<circle cx="52" cy="22" r="5" fill="#8F4FE0" {s('stroke-width="2"')}/><circle cx="118" cy="80" r="4" fill="#8F4FE0" {s('stroke-width="2"')}/>
{face(84, 50, d=9, k=0.95)}
'''))

# 38. Art Поколение, Красноармейская — альбом для рисования
I["art-pokolenie-krasnoarmeyskaya"] = ("толстый альбом для рисования на пружинке",
    "раскрыт, и солнышко на его странице выглядывает и машет лучиком", bg("#FFF0E6", "#F5A57A", f'''
<rect x="16" y="30" width="96" height="78" rx="4" fill="#2FA8A0" {s()}/>
<rect x="20" y="26" width="88" height="78" rx="3" fill="#FFFDF4" {s()}/>
<g fill="none" {s('stroke-width="2.2"')}><circle cx="30" cy="26" r="4"/><circle cx="44" cy="26" r="4"/><circle cx="58" cy="26" r="4"/><circle cx="72" cy="26" r="4"/><circle cx="86" cy="26" r="4"/><circle cx="100" cy="26" r="4"/></g>
<circle cx="64" cy="66" r="18" fill="#FFD83A" {s()}/>
<path d="M64 40 V34 M64 92 V98 M38 66 H32 M90 66 H98 M46 48 L42 44 M82 48 L86 44 M46 84 L42 88 M82 84 L90 76 L96 80" {ln("#F2A23A", 3.5)}/>
{face(64, 64, d=7, k=0.75)}
'''))

# 39. Студия рисования, Внуково — самолётик-художник
I["paint-school-vnukovo"] = ("белый самолётик-художник с кисточкой в руке",
    "рисует в небе над Внуково радужную полосу вместо следа", bg("#E6F5FF", "#7FC4F0", f'''
<path d="M-4 104 Q40 70 74 74" fill="none" {ln("#E2393C", 7)}/><path d="M-4 112 Q40 78 74 82" fill="none" {ln("#FFD83A", 7)}/><path d="M-4 120 Q40 86 74 90" fill="none" {ln("#5ACB5A", 7)}/>
<path d="M60 70 Q64 56 96 52 Q118 50 120 60 Q118 70 96 72 Q70 80 60 70Z" fill="#fff" {s()}/>
<path d="M80 58 L70 34 L84 36 L94 56Z" fill="#E8F0FA" {s()}/>
<path d="M82 72 L72 94 L86 92 L94 72Z" fill="#E8F0FA" {s()}/>
<path d="M60 70 L52 52 L64 56Z" fill="#E8F0FA" {s()}/>
<path d="M110 54 Q116 56 118 60" fill="none" {ln("#4AA8F0", 3)}/>
{eye(98, 61, 0.65)}{eye(106, 60, 0.65)}<path d="M100 66 Q103 68 106 66" fill="none" {s('stroke-width="1.8"')}/>
<path d="M76 74 L66 84" {ln(O, 5)}/><path d="M76 74 L68 82" {ln("#E8C27A", 2.6)}/>
'''))

# 40. Деталь, Шухова — ажурная башенка из глины
I["detal-ceramics-shukhova"] = ("глиняная ажурная башенка-ваза в форме сетчатой башни",
    "крутится на гончарном круге, а её сетка ещё мокрая и блестит", bg("#F4EEE8", "#C8A88A", f'''
<ellipse cx="64" cy="112" rx="48" ry="10" fill="#7A7A8A" {s()}/><ellipse cx="64" cy="108" rx="42" ry="8" fill="#A0A0B0" {s()}/>
<path d="M44 106 L54 24 H74 L84 106Z" fill="#D98A5A" {s()}/>
<path d="M46 92 L76 30 M50 104 L78 46 M60 106 L80 62 M70 106 L82 80 M82 92 L52 30 M78 104 L50 46 M68 106 L48 62 M58 106 L46 80" {ln("#A8573E", 2)}/>
<path d="M44 66 H84 M48 44 H80" {ln("#A8573E", 2.4)}/>
<ellipse cx="64" cy="24" rx="12" ry="4" fill="#E8A070" {s()}/>
<rect x="50" y="70" width="28" height="22" rx="8" fill="#E8A070" {s('stroke-width="2"')}/>
{eye(58, 78, 0.6)}{eye(70, 78, 0.6)}<path d="M61 84 Q64 87 67 84" fill="none" {s('stroke-width="1.8"')}/>
<path d="M20 98 Q14 104 20 110 M108 98 Q114 104 108 110" fill="none" {s('stroke-width="2.4"')}/>
'''))

# 41. YarO, проспект Мира — печь для обжига
I["yaro-mira-150"] = ("пузатая печь для обжига керамики с круглым окошком",
    "из жаркого окошка выглядывает свежеобожжённая синяя чашка", bg("#FFEFE0", "#F09A5A", f'''
<rect x="22" y="28" width="84" height="84" rx="16" fill="#7D8590" {s()}/>
<rect x="30" y="112" width="12" height="10" fill="#555" {s()}/><rect x="86" y="112" width="12" height="10" fill="#555" {s()}/>
<rect x="56" y="16" width="16" height="14" fill="#6A707A" {s()}/>
<path d="M60 14 Q56 6 62 0 M68 14 Q72 6 66 -2" fill="none" {ln("#fff", 2.4)} opacity=".7"/>
<circle cx="64" cy="76" r="24" fill="#FF8A3D" {s()}/><circle cx="64" cy="76" r="18" fill="#FFC34A"/>
<path d="M54 74 H74 L72 88 H56Z" fill="#3A6AE0" {s()}/><path d="M74 78 Q82 78 80 84 Q78 88 72 86" fill="none" {s('stroke-width="2.4"')}/>
{eye(60, 80, 0.5)}{eye(68, 80, 0.5)}
{eye(48, 44, 0.8)}{eye(80, 44, 0.8)}
<ellipse cx="40" cy="52" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/><ellipse cx="88" cy="52" rx="4" ry="2.4" fill="#FF7FA8" opacity=".7"/>
'''))

# 42. Volna Керамика — миска-волна
I["volna-ceramics-oktyabrsky"] = ("бирюзовая керамическая миска с волнистым краем",
    "в ней плещется глазурь-море, и из волны выпрыгивает глиняная рыбка", bg("#E4FBFA", "#4FC1C8", f'''
<path d="M14 64 Q24 58 34 64 Q44 70 54 64 Q64 58 74 64 Q84 70 94 64 Q104 58 114 64 Q112 104 64 108 Q16 104 14 64Z" fill="#2EB3B8" {s()}/>
<path d="M22 70 Q32 64 42 70 Q52 76 62 70 Q72 64 82 70 Q92 76 104 70" fill="none" {ln("#BFF4F0", 3)}/>
<path d="M52 112 H76 L74 120 H54Z" fill="#1E8A8E" {s()}/>
{face(64, 86, d=12, k=1.0)}
<path d="M70 52 Q76 30 96 32 Q108 34 104 44 Q96 54 82 52 L74 60Z" fill="#E8A070" {s()}/>
<path d="M102 36 L114 26 L112 44Z" fill="#E8A070" {s()}/>
{eye(90, 40, 0.55)}
<circle cx="40" cy="44" r="4" fill="#fff" opacity=".8" {s('stroke-width="1.6"')}/><circle cx="50" cy="34" r="2.6" fill="#fff" opacity=".8" {s('stroke-width="1.4"')}/>
'''))


if __name__ == "__main__":
    only = sys.argv[1:]
    for pid, (hero, scene, svgtxt) in I.items():
        if only and pid not in only:
            continue
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svgtxt)
    print(len(I))
