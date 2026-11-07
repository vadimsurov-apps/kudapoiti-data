"""Робот cafes, 2026-11-07 (утро): иконки новых кафе, каждая придумана и нарисована отдельно
(правило абсолютной уникальности: свой герой, своя сцена, своя компоновка и палитра фона).
Запуск из корня: python3 tools/icons_cafes_1107c.py  → icons-src/<id>.svg + строки в icons-src/subjects.txt"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def W(w):
    return s(f'stroke-width="{w}"')


def svg2(a, b, body, cx="38%", cy="28%"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="{cx}" cy="{cy}" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


I = {}

# 1 Punta Prima (Химки) — паэлья в широкой сковороде с ручками, обмахивается долькой лимона как веером
I["cafe-punta-prima-khimki"] = (svg2("#FFF3C9", "#F0A52A", f'''
<path d="M8 74 L20 70 M108 70 L122 74" fill="none" {W(6)}/>
<path d="M8 74 L20 70 M108 70 L122 74" fill="none" stroke="#2E2A3C" stroke-width="3"/>
<ellipse cx="64" cy="76" rx="48" ry="26" fill="#3A3A48" {s()}/>
<ellipse cx="64" cy="72" rx="42" ry="20" fill="#F2B53A"/>
<circle cx="40" cy="66" r="2.4" fill="#5DB34A"/><circle cx="86" cy="64" r="2.4" fill="#5DB34A"/><circle cx="76" cy="82" r="2.4" fill="#5DB34A"/><circle cx="48" cy="82" r="2.2" fill="#5DB34A"/>
<circle cx="58" cy="60" r="2" fill="#D8433A"/><circle cx="92" cy="76" r="2" fill="#D8433A"/><circle cx="34" cy="76" r="2" fill="#D8433A"/>
<path d="M70 58 Q80 54 86 62 Q80 66 74 64" fill="#FF8A6B" {W(2)}/>
{face(62, 72, d=11, k=0.95)}
<g transform="rotate(-25 98 36)"><path d="M80 40 A18 18 0 0 1 116 40Z" fill="#FFF07A" {W(2.6)}/>
<path d="M98 40 L86 30 M98 40 L98 24 M98 40 L110 30" stroke="#E8C93B" stroke-width="2"/>
<path d="M84 38 A14 14 0 0 1 112 38" fill="none" stroke="#fff" stroke-width="1.6" opacity=".7"/></g>
<path d="M76 54 Q82 46 90 44" fill="none" {W(3)}/>
'''), "герой: паэлья в широкой сковороде с горошком и креветкой | сцена: обмахивается долькой лимона, как веером, в жаркий полдень")

# 2 Хата (Химки, кв. Клязьма) — стопка драников со сметаной у белёной хаты под соломенной крышей
I["cafe-khata-klyazma"] = (svg2("#E6F4FF", "#86B8E0", f'''
<rect x="0" y="96" width="128" height="34" fill="#9BCB6A" {W(2.4)}/>
<rect x="18" y="52" width="58" height="46" fill="#FFFDF6" {s()}/>
<path d="M10 56 L47 26 L84 56Z" fill="#E7C064" {s()}/>
<path d="M22 50 L47 30 M34 54 L54 36 M60 50 L47 38" stroke="#C69A3A" stroke-width="2"/>
<rect x="28" y="64" width="16" height="14" fill="#9ED6FF" {W(2.4)}/><path d="M36 64 V78 M28 71 H44" stroke="{O}" stroke-width="2"/>
<ellipse cx="86" cy="104" rx="30" ry="7" fill="#fff" {s()}/>
<ellipse cx="86" cy="98" rx="24" ry="7" fill="#C9852F" {W(2.6)}/>
<ellipse cx="86" cy="88" rx="24" ry="7" fill="#DB9A3E" {W(2.6)}/>
<ellipse cx="86" cy="78" rx="24" ry="7.5" fill="#E8AE4E" {W(2.6)}/>
<path d="M72 76 Q78 66 88 70 Q98 64 100 76 Q92 80 86 78 Q78 80 72 76Z" fill="#FFFFFF" {W(2.4)}/>
{face(86, 89, d=8, k=0.7)}
'''), "герой: стопка картофельных драников со сметаной | сцена: стоит у белёной хаты под соломенной крышей")

# 3 Mano a Mano (Химки) — две хлебные палочки грисини жмут друг другу руки
I["cafe-mano-a-mano-khimki"] = (svg2("#F1FFE8", "#5FB98C", f'''
<g transform="rotate(-22 40 72)"><rect x="30" y="24" width="18" height="92" rx="9" fill="#EFC27A" {s()}/>
<path d="M32 40 L46 44 M32 58 L46 62 M32 76 L46 80 M32 94 L46 98" stroke="#C88F3E" stroke-width="2"/>
{face(39, 50, d=5, k=0.6, blush=False)}</g>
<g transform="rotate(22 88 72)"><rect x="80" y="24" width="18" height="92" rx="9" fill="#F3D08E" {s()}/>
<path d="M82 40 L96 44 M82 58 L96 62 M82 76 L96 80 M82 94 L96 98" stroke="#C88F3E" stroke-width="2"/>
{face(89, 50, d=5, k=0.6, blush=False)}</g>
<path d="M50 70 Q58 62 64 70 Q70 62 78 70" fill="none" {W(3.4)}/>
<ellipse cx="64" cy="72" rx="9" ry="7" fill="#F5D7A8" {W(2.6)}/>
<path d="M58 70 H70 M58 74 H70" stroke="{O}" stroke-width="1.6"/>
{sparkle(64, 52, 6, "#FFF")}{sparkle(48, 98, 4, "#FFF")}{sparkle(82, 100, 4, "#FFF")}
'''), "герой: две хлебные палочки грисини | сцена: крепко жмут друг другу руки «один на один»")

# 4 Gagawa (МЕГА Химки, грузинская) — зелёный шарик пхали ловит ртом зёрнышки граната
I["cafe-gagawa-mega-khimki"] = (svg2("#FFE9EE", "#C2365A", f'''
<ellipse cx="64" cy="110" rx="40" ry="8" fill="#fff" {s()}/>
<circle cx="64" cy="80" r="30" fill="#4E9E3E" {s()}/>
<path d="M44 70 Q50 64 56 70 M70 92 Q78 86 84 92 M46 96 Q52 92 56 96" fill="none" stroke="#2F7A2A" stroke-width="2.4"/>
<path d="M60 56 L58 50 M64 54 L66 48" stroke="{O}" stroke-width="2"/>
<circle cx="72" cy="62" r="3" fill="#D8233F" {W(1.4)}/><circle cx="52" cy="84" r="3" fill="#D8233F" {W(1.4)}/><circle cx="80" cy="76" r="3" fill="#D8233F" {W(1.4)}/>
{eye(54, 76, 0.85)}{eye(74, 76, 0.85)}
<ellipse cx="64" cy="90" rx="6" ry="5" fill="#7A1F3A" {W(2.2)}/>
<ellipse cx="46" cy="86" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/><ellipse cx="82" cy="86" rx="4" ry="2.4" fill="#FF7FA8" opacity=".6"/>
<path d="M56 30 Q58 24 62 28 Q60 34 56 30Z" fill="#E8203E" {W(1.8)}/>
<path d="M70 16 Q72 10 76 14 Q74 20 70 16Z" fill="#E8203E" {W(1.8)}/>
<path d="M44 20 Q46 14 50 18 Q48 24 44 20Z" fill="#E8203E" {W(1.8)}/>
<path d="M84 34 Q86 28 90 32 Q88 38 84 34Z" fill="#E8203E" {W(1.8)}/>
'''), "герой: зелёный шарик пхали со шпинатом | сцена: ловит ртом падающие зёрнышки граната")

# 5 Belle Famille (Химки) — киш в рифлёной форме на подоконнике рядом с горшком лаванды
I["cafe-belle-famille-khimki"] = (svg2("#EFE6FF", "#8E79D6", f'''
<rect x="6" y="14" width="116" height="78" fill="#CDEBFF" {W(2.6)}/>
<path d="M64 14 V92 M6 52 H122" stroke="#FFFFFF" stroke-width="5"/>
<rect x="0" y="88" width="128" height="14" fill="#FFFFFF" {s()}/>
<rect x="0" y="102" width="128" height="30" fill="#F2E8D8"/>
<path d="M90 88 L94 68 H114 L118 88Z" fill="#D9774E" {W(2.6)}/>
<path d="M98 68 V46 M104 68 V40 M110 68 V48" stroke="#5E8C3A" stroke-width="2.4"/>
<ellipse cx="98" cy="46" rx="2.6" ry="5" fill="#9A7BE0"/><ellipse cx="104" cy="40" rx="2.6" ry="5.5" fill="#9A7BE0"/><ellipse cx="110" cy="48" rx="2.6" ry="5" fill="#9A7BE0"/>
<path d="M14 88 L20 64 H76 L82 88Z" fill="#E8B05A" {s()}/>
<path d="M24 64 V88 M32 64 V88 M40 64 V88 M48 64 V88 M56 64 V88 M64 64 V88 M72 64 V88" stroke="#C88F3E" stroke-width="1.6"/>
<ellipse cx="48" cy="64" rx="28" ry="6" fill="#FFE07A" {W(2.6)}/>
<circle cx="38" cy="63" r="2.2" fill="#E2683E"/><circle cx="56" cy="64" r="2.2" fill="#5DB34A"/><circle cx="48" cy="61" r="2" fill="#E2683E"/>
{face(48, 76, d=10, k=0.8)}
'''), "герой: французский киш в рифлёной форме | сцена: остывает на подоконнике рядом с горшком лаванды")

# 6 Сказка Пушкина (Химки) — глиняная кружка горячего сбитня с медовой ложкой; за окном метель («Где же кружка?»)
I["cafe-skazka-pushkina-khimki"] = (svg2("#3D4E9C", "#1D2457", f'''
<rect x="10" y="10" width="108" height="70" rx="6" fill="#5869C4" {W(2.6)}/>
<path d="M64 10 V80 M10 44 H118" stroke="#8B5A3C" stroke-width="5"/>
<circle cx="26" cy="24" r="2.4" fill="#fff"/><circle cx="44" cy="34" r="2" fill="#fff"/><circle cx="84" cy="22" r="2.6" fill="#fff"/><circle cx="104" cy="32" r="2" fill="#fff"/>
<circle cx="30" cy="58" r="2" fill="#fff"/><circle cx="96" cy="62" r="2.4" fill="#fff"/><circle cx="78" cy="52" r="1.8" fill="#fff"/>
<path d="M14 34 Q30 26 46 36 M80 66 Q96 58 114 68" fill="none" stroke="#fff" stroke-width="2" opacity=".6" stroke-linecap="round"/>
<rect x="0" y="80" width="128" height="50" fill="#9A6440"/>
<path d="M86 84 Q104 84 104 98 Q104 112 86 112" fill="none" {W(6)}/><path d="M86 84 Q104 84 104 98 Q104 112 86 112" fill="none" stroke="#C97A4E" stroke-width="3"/>
<path d="M34 72 H90 L86 116 Q62 122 38 116Z" fill="#D98A5A" {s()}/>
<ellipse cx="62" cy="72" rx="28" ry="6" fill="#B5612E" {W(2.6)}/>
<path d="M40 84 H86" stroke="#B5612E" stroke-width="2.4" stroke-dasharray="4 3"/>
<path d="M76 74 L96 48" {W(3.4)}/><path d="M76 74 L96 48" stroke="#E9B44C" stroke-width="2"/>
<ellipse cx="98" cy="45" rx="6" ry="7" fill="#F6C447" {W(2.4)}/><path d="M93 43 H103 M93 47 H103" stroke="{O}" stroke-width="1.4"/>
<path d="M50 62 Q46 54 52 48 M62 60 Q58 50 64 44" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
{face(62, 98, d=10, k=0.85)}
'''), "герой: глиняная кружка горячего сбитня с медовой ложкой | сцена: греется у окна, за которым метель")

# 7 Никала (Химки, грузинская) — сладкий хлеб назуки с изюмом гонится за убежавшими изюминками
I["cafe-nikala-khimki"] = (svg2("#FFF0DE", "#E59262", f'''
<rect x="0" y="104" width="128" height="26" fill="#F6E1C2" {W(2.2)}/>
<path d="M16 98 Q16 52 58 50 Q96 52 96 98Z" fill="#D78A3A" {s()}/>
<path d="M24 80 Q56 66 90 78" fill="none" stroke="#F5C27A" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="40" cy="66" rx="2.4" ry="1.8" fill="#5A2A3A"/><ellipse cx="76" cy="62" rx="2.4" ry="1.8" fill="#5A2A3A"/><ellipse cx="30" cy="88" rx="2.4" ry="1.8" fill="#5A2A3A"/><ellipse cx="84" cy="88" rx="2.4" ry="1.8" fill="#5A2A3A"/>
{face(56, 86, d=10, k=0.9)}
<path d="M18 98 L96 98" {W(3)}/>
<ellipse cx="108" cy="100" rx="5" ry="4" fill="#6B2E46" {W(2)}/><path d="M106 104 L104 108 M110 104 L112 108" {W(1.8)}/>
<ellipse cx="114" cy="80" rx="5" ry="4" fill="#6B2E46" {W(2)}/><path d="M112 84 L110 88 M116 84 L118 88" {W(1.8)}/>
<circle cx="107" cy="99" r="0.9" fill="#fff"/><circle cx="113" cy="79" r="0.9" fill="#fff"/>
<path d="M96 70 Q102 66 104 70 M98 92 Q102 88 104 92" fill="none" {W(2)} stroke-dasharray="2 3"/>
'''), "герой: круглый сладкий хлеб назуки с изюмом | сцена: гонится за убежавшими от него изюминками")

# 8 Корона (Химки) — тарталетка в форме короны с ягодами-самоцветами на бархатной подушке
I["cafe-korona-khimki"] = (svg2("#FCE9FF", "#B04AA8", f'''
<path d="M14 104 Q14 86 32 84 H96 Q114 86 114 104 Q114 118 96 118 H32 Q14 118 14 104Z" fill="#C8243F" {s()}/>
<circle cx="18" cy="116" r="5" fill="#F6C447" {W(2)}/><circle cx="110" cy="116" r="5" fill="#F6C447" {W(2)}/>
<path d="M26 86 L22 40 L42 58 L64 30 L86 58 L106 40 L102 86Z" fill="#EFC27A" {s()}/>
<path d="M28 74 H100" stroke="#C88F3E" stroke-width="2.4"/>
<circle cx="22" cy="40" r="6" fill="#4F7FE0" {W(2.2)}/><circle cx="64" cy="30" r="7" fill="#D8233F" {W(2.2)}/><circle cx="106" cy="40" r="6" fill="#3E9C3A" {W(2.2)}/>
<circle cx="62" cy="28" r="2" fill="#fff" opacity=".8"/>
<path d="M30 74 Q64 60 98 74" fill="#FFF3D6" {W(2)}/>
{face(64, 62, d=11, k=0.85)}
{sparkle(30, 24, 5, "#FFF")}{sparkle(96, 20, 4, "#FFF")}
'''), "герой: песочная тарталетка в форме короны с ягодами-самоцветами | сцена: лежит на бархатной подушке с кисточками")

# 9 Панчо Пицца (МЕГА Химки, итало-мексиканская) — кесадилья тянет сырные нити гамаком, в нём дремлет перчик халапеньо
I["cafe-pancho-mega-khimki"] = (svg2("#FFF6D0", "#7FC24A", f'''
<path d="M10 82 A42 42 0 0 1 58 40 L58 82Z" fill="#F2C76A" {s()}/>
<path d="M118 82 A42 42 0 0 0 70 40 L70 82Z" fill="#F2C76A" {s()}/>
<path d="M18 74 A34 34 0 0 1 50 48" fill="none" stroke="#D99A3C" stroke-width="2.4" stroke-dasharray="5 4"/>
<path d="M110 74 A34 34 0 0 0 78 48" fill="none" stroke="#D99A3C" stroke-width="2.4" stroke-dasharray="5 4"/>
<circle cx="30" cy="64" r="2.6" fill="#C4552E"/><circle cx="96" cy="62" r="2.6" fill="#C4552E"/><circle cx="44" cy="74" r="2.2" fill="#C4552E"/>
<path d="M56 60 Q64 92 72 60" fill="#FFE27A" {W(2.4)}/>
<path d="M56 70 Q64 100 72 70" fill="none" stroke="#FFE27A" stroke-width="3"/>
<g transform="rotate(-12 64 78)"><path d="M52 78 Q64 70 78 76 Q84 80 78 84 Q64 88 52 82Z" fill="#3E9C3A" {W(2.2)}/><path d="M78 78 L84 74" {W(2.2)}/></g>
<path d="M58 77 Q60 79 62 77 M66 76 Q68 78 70 76" fill="none" {W(1.6)}/>
<text x="76" y="64" font-family="Arial" font-weight="bold" font-size="9" fill="{O}">z</text>
{face(34, 76, d=7, k=0.7)}{face(94, 76, d=7, k=0.7)}
<rect x="0" y="96" width="128" height="34" fill="#E8553E" {W(2.4)}/>
<path d="M0 106 H128 M0 118 H128" stroke="#FFD25E" stroke-width="3"/>
'''), "герой: две половинки кесадильи | сцена: растянули между собой гамак из сыра, в котором дремлет перчик халапеньо")

# 10 Avgust13 Vostok (Мытищи, Высоково) — трёхлитровая банка вишнёвого компота под августовским звездопадом
I["cafe-avgust13-vostok"] = (svg2("#5B4BA8", "#1E1745", f'''
<path d="M14 18 L30 30" stroke="#FFE68A" stroke-width="2.4" stroke-linecap="round"/><circle cx="31" cy="31" r="2.6" fill="#FFF6C4"/>
<path d="M90 10 L108 22" stroke="#FFE68A" stroke-width="2.4" stroke-linecap="round"/><circle cx="109" cy="23" r="2.6" fill="#FFF6C4"/>
<circle cx="52" cy="14" r="1.6" fill="#fff"/><circle cx="20" cy="50" r="1.4" fill="#fff"/><circle cx="114" cy="48" r="1.6" fill="#fff"/>
<rect x="0" y="108" width="128" height="22" fill="#8A5A3A" {W(2.4)}/>
<path d="M40 36 H88 V44 Q100 50 100 64 V104 Q100 112 92 112 H36 Q28 112 28 104 V64 Q28 50 40 44Z" fill="#E85A7A" opacity=".9" {s()}/>
<rect x="38" y="28" width="52" height="10" rx="3" fill="#C8CDD8" {W(2.6)}/>
<path d="M34 60 Q36 54 42 52" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<circle cx="44" cy="96" r="6" fill="#9B1636" {W(2)}/><circle cx="84" cy="94" r="6" fill="#9B1636" {W(2)}/><circle cx="72" cy="104" r="5" fill="#9B1636" {W(2)}/>
<circle cx="88" cy="70" r="3" fill="#fff" opacity=".6"/><circle cx="40" cy="78" r="2" fill="#fff" opacity=".6"/>
{face(64, 74, d=12, k=0.95)}
'''), "герой: трёхлитровая банка вишнёвого компота | сцена: любуется августовским звездопадом с дачного стола")

# 11 Bella strada (Мытищи) — рисовый шарик аранчини катится по брусчатке итальянской улочки
I["cafe-bella-strada-mytishchi"] = (svg2("#FFE9D6", "#E08458", f'''
<path d="M0 70 H128 V130 H0Z" fill="#B9A08A"/>
<path d="M0 70 H128" {W(2.4)}/>
<path d="M0 84 H128 M0 100 H128 M0 116 H128" stroke="#8E7562" stroke-width="2"/>
<path d="M16 70 V84 M48 70 V84 M80 70 V84 M112 70 V84 M30 84 V100 M62 84 V100 M94 84 V100 M14 100 V116 M46 100 V116 M110 100 V116" stroke="#8E7562" stroke-width="2"/>
<rect x="6" y="18" width="26" height="52" fill="#F4C06A" {W(2.4)}/><rect x="12" y="28" width="12" height="14" fill="#5BA9D6" {W(2)}/>
<rect x="96" y="12" width="28" height="58" fill="#E9897A" {W(2.4)}/><rect x="102" y="24" width="14" height="16" fill="#5BA9D6" {W(2)}/>
<path d="M24 66 Q16 66 14 60 M30 74 Q20 76 16 72" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
<ellipse cx="64" cy="112" rx="34" ry="7" fill="#fff" {s()}/>
<circle cx="64" cy="76" r="30" fill="#C97A2C" {s()}/>
<path d="M68 72 L93 68 A30 30 0 0 0 74 47 Z" fill="#FFF8E6" {W(2.6)}/>
<circle cx="76" cy="60" r="5" fill="#F6C447" {W(1.8)}/><circle cx="84" cy="62" r="1.4" fill="#E0C9A0"/><circle cx="72" cy="54" r="1.4" fill="#E0C9A0"/>
<path d="M88 66 Q96 70 102 64" fill="none" stroke="#F6C447" stroke-width="3" stroke-linecap="round"/>
<circle cx="46" cy="62" r="1.8" fill="#8A4A1A"/><circle cx="56" cy="54" r="1.8" fill="#8A4A1A"/><circle cx="40" cy="78" r="1.8" fill="#8A4A1A"/><circle cx="52" cy="96" r="1.8" fill="#8A4A1A"/><circle cx="74" cy="98" r="1.8" fill="#8A4A1A"/><circle cx="86" cy="88" r="1.8" fill="#8A4A1A"/><circle cx="66" cy="52" r="1.8" fill="#8A4A1A"/>
<circle cx="50" cy="70" r="1.4" fill="#F2B866"/><circle cx="70" cy="94" r="1.4" fill="#F2B866"/><circle cx="44" cy="90" r="1.4" fill="#F2B866"/>
{face(60, 78, d=11, k=0.9)}
'''), "герой: золотистый рисовый шарик аранчини | сцена: катится по брусчатке узкой итальянской улочки")

# 12 Швили (ТРК «Красный кит», Мытищи) — связка чурчхелы раскачивается на ветке, как гимнаст на кольцах
I["cafe-shvili-krasny-kit"] = (svg2("#F0FFF0", "#79B864", f'''
<path d="M4 22 Q64 10 124 22" fill="none" stroke="#7A5232" stroke-width="7" stroke-linecap="round"/>
<path d="M4 22 Q64 10 124 22" fill="none" {W(2)}/>
<path d="M98 18 Q104 8 112 12 Q108 20 98 18Z" fill="#5DB34A" {W(1.8)}/><path d="M22 18 Q16 8 8 12 Q12 20 22 18Z" fill="#5DB34A" {W(1.8)}/>
<path d="M50 18 L54 34 M78 18 L74 34" {W(2.6)}/>
<path d="M48 34 H80" {W(3)}/>
<path d="M52 34 Q46 70 52 108 Q56 116 62 108 Q66 70 60 34Z" fill="#8E2A4E" {s()}/>
<path d="M68 34 Q62 70 68 108 Q72 116 78 108 Q82 70 76 34Z" fill="#B8476A" {s()}/>
<circle cx="56" cy="52" r="1.8" fill="#5A1530"/><circle cx="57" cy="66" r="1.8" fill="#5A1530"/><circle cx="56" cy="92" r="1.8" fill="#5A1530"/>
<circle cx="72" cy="52" r="1.8" fill="#7A2645"/><circle cx="73" cy="68" r="1.8" fill="#7A2645"/><circle cx="72" cy="94" r="1.8" fill="#7A2645"/>
{eye(56, 78, 0.6)}{eye(73, 78, 0.6)}
<path d="M60 86 Q65 90 70 86" fill="none" {W(2)}/>
<path d="M30 60 Q24 74 30 88 M98 60 Q104 74 98 88" fill="none" {W(2.4)} stroke-dasharray="4 4"/>
'''), "герой: связка тёмной и светлой чурчхелы | сцена: раскачивается на ветке, как гимнаст на кольцах")

# 13 Pizzamore (Мытищи) — пицца-сердце целиком делится кусочком с маленьким сердечком
I["cafe-pizzamore-mytishchi"] = (svg2("#FFF0F3", "#F27A9A", f'''
<path d="M58 112 L14 62 Q2 42 18 28 Q36 16 58 36 Q80 16 98 28 Q114 42 102 62Z" fill="#E9A949" {s()}/>
<path d="M58 102 L22 62 Q12 46 24 36 Q38 28 58 46 Q78 28 92 36 Q104 46 94 62Z" fill="#F6D06A"/>
<circle cx="34" cy="48" r="6" fill="#D8433A" {W(2)}/><circle cx="82" cy="46" r="6" fill="#D8433A" {W(2)}/><circle cx="58" cy="84" r="5" fill="#D8433A" {W(2)}/>
<circle cx="46" cy="70" r="2.4" fill="#3E9C3A"/><circle cx="74" cy="70" r="2.4" fill="#3E9C3A"/>
{face(58, 62, d=10, k=0.85)}
<path d="M98 92 L86 78 Q82 72 87 68 Q92 65 98 71 Q104 65 109 68 Q114 72 110 78Z" fill="#F6D06A" {W(2.4)}/>
<circle cx="98" cy="76" r="2.4" fill="#D8433A"/>
<path d="M94 82 Q98 85 102 82" fill="none" {W(1.6)}/>
<path d="M104 46 Q110 40 116 46" fill="none" stroke="#E25F79" stroke-width="2.4" stroke-linecap="round"/>
'''), "герой: целая пицца в форме сердца | сцена: угощает кусочком маленькое пицца-сердечко")

# 14 Виват Пицца (Мытищи) — кружок пепперони прыгает на растянутом тесте, как на батуте, и кричит «ура»
I["cafe-vivat-pizza-mytishchi"] = (svg2("#E3F4FF", "#3E8FD8", f'''
<path d="M20 112 L28 92 M108 112 L100 92" {W(4)}/>
<ellipse cx="64" cy="92" rx="48" ry="12" fill="#F3D9A2" {s()}/>
<ellipse cx="64" cy="90" rx="38" ry="7" fill="#FFF0C8"/>
<path d="M50 96 Q64 104 78 96" fill="none" stroke="#D7B270" stroke-width="2"/>
<circle cx="64" cy="48" r="24" fill="#D23A3A" {s()}/>
<circle cx="54" cy="38" r="3" fill="#F28B7A"/><circle cx="76" cy="56" r="3" fill="#F28B7A"/><circle cx="72" cy="34" r="2.4" fill="#F28B7A"/><circle cx="50" cy="58" r="2.4" fill="#F28B7A"/>
{face(64, 46, d=9, k=0.8, mouth=False)}
<ellipse cx="64" cy="55" rx="5" ry="4" fill="#5A1530" {W(2)}/>
<path d="M42 40 L30 26 M86 40 L98 26" {W(3)}/>
<path d="M64 76 V84" {W(2)} stroke-dasharray="2 3"/>
{sparkle(24, 40, 6, "#FFE35E")}{sparkle(106, 46, 5, "#FFE35E")}{sparkle(96, 16, 4, "#fff")}
'''), "герой: кружок пепперони | сцена: подпрыгивает на тесте для пиццы, как на батуте, и кричит «ура»")

# 15 Загородный дворик (Мытищи) — деревянная кружка кваса с пеной у деревенского колодца-журавля
I["cafe-zagorodny-dvorik-mytishchi"] = (svg2("#FFFBE8", "#C9B26A", f'''
<rect x="0" y="100" width="128" height="30" fill="#8FBE5A" {W(2.2)}/>
<path d="M22 100 V40 M10 30 L118 18" {W(3)}/>
<path d="M22 100 V40" stroke="#8B5A3C" stroke-width="5" stroke-linecap="round"/><path d="M12 30 L116 19" stroke="#A9764E" stroke-width="4" stroke-linecap="round"/>
<path d="M104 20 V44" {W(2)}/><rect x="98" y="44" width="12" height="10" fill="#9E9E9E" {W(2)}/>
<rect x="88" y="80" width="34" height="22" fill="#B98455" {W(2.4)}/><path d="M88 88 H122 M88 95 H122" stroke="#8B5A3C" stroke-width="1.6"/>
<path d="M36 52 H82 L78 110 Q58 116 40 110Z" fill="#C88A52" {s()}/>
<path d="M44 52 V110 M58 52 V113 M72 52 V110" stroke="#9E6638" stroke-width="2"/>
<path d="M34 64 H84 M36 96 H82" stroke="#5B5B66" stroke-width="3.4"/>
<path d="M82 62 Q96 64 94 78 Q92 90 80 88" fill="none" {W(5)}/><path d="M82 62 Q96 64 94 78 Q92 90 80 88" fill="none" stroke="#C88A52" stroke-width="2.4"/>
<path d="M32 54 Q30 42 42 42 Q46 34 56 38 Q64 32 72 38 Q84 36 84 48 Q88 54 80 56 H38 Q30 58 32 54Z" fill="#FFF3D6" {W(2.6)}/>
{face(58, 78, d=10, k=0.85)}
'''), "герой: деревянная кружка кваса с шапкой пены | сцена: стоит во дворе у деревенского колодца-журавля")

# 16 Pomidoroff (Мытищи) — ньокки с бороздками сплавляются по реке томатного соуса
I["cafe-pomidoroff-mytishchi"] = (svg2("#FFF7EF", "#F3C9A6", f'''
<path d="M0 62 Q30 52 64 62 Q98 72 128 62 V130 H0Z" fill="#E2412F" {W(2.6)}/>
<path d="M10 80 Q30 74 50 80 M70 92 Q92 86 114 92 M20 108 Q40 102 60 108" fill="none" stroke="#FF8A70" stroke-width="3" stroke-linecap="round"/>
<g transform="rotate(-10 40 72)"><ellipse cx="40" cy="72" rx="20" ry="14" fill="#F9E3A8" {s()}/>
<path d="M28 64 Q30 72 28 80 M36 62 Q38 72 36 82 M44 62 Q46 72 44 82 M52 64 Q54 72 52 80" fill="none" stroke="#D9B66A" stroke-width="2"/></g>
<ellipse cx="88" cy="90" rx="22" ry="15" fill="#FBEABA" {s()}/>
<path d="M74 82 Q76 90 74 98 M82 80 Q84 90 82 100 M90 80 Q92 90 90 100 M98 80 Q100 90 98 98" fill="none" stroke="#D9B66A" stroke-width="2"/>
{face(88, 88, d=8, k=0.75)}
{face(40, 70, d=7, k=0.65)}
<path d="M98 30 Q102 18 112 22 Q108 34 98 30Z" fill="#3E9C3A" {W(2)}/><path d="M100 30 L110 22" stroke="#8FD27A" stroke-width="1.4"/>
'''), "герой: два пухлых ньокки с бороздками от вилки | сцена: сплавляются по реке из томатного соуса")

# 17 Гранд Урюк (Мытищи, Щербакова) — сушёные абрикосы-урюк сушатся на верёвочке на прищепках под солнцем
I["cafe-uryuk-mytishchi"] = (svg2("#BFEFFF", "#4FB3E8", f'''
<circle cx="104" cy="24" r="14" fill="#FFD84A" {W(2.4)}/>
<path d="M104 4 V0 M84 24 H80 M90 10 L86 6 M118 10 L122 6" stroke="#FFD84A" stroke-width="3" stroke-linecap="round"/>
<path d="M0 42 Q64 62 128 42" fill="none" {W(2.4)}/>
<rect x="28" y="40" width="7" height="14" rx="2" fill="#5BC0A0" {W(2)}/>
<path d="M62 54 Q28 54 30 84 Q32 108 64 106 Q98 108 98 82 Q98 54 66 54Z" fill="#D9741C" {s()}/>
<rect x="60" y="44" width="8" height="16" rx="2" fill="#FFD25E" {W(2)}/>
<path d="M38 66 Q46 62 50 70 Q44 74 40 82 M78 62 Q84 70 90 68 M42 96 Q50 90 56 98 Q62 92 70 100 M82 92 Q88 86 92 92" fill="none" stroke="#9A4A0E" stroke-width="2.2" stroke-linecap="round"/>
<path d="M36 74 Q40 70 44 74" fill="none" stroke="#F5A050" stroke-width="2" stroke-linecap="round"/>
<g transform="rotate(12 106 70)"><path d="M96 66 Q106 56 116 66 Q118 80 106 82 Q94 80 96 66Z" fill="#C86414" {W(2.2)}/><path d="M100 70 Q106 66 112 72" fill="none" stroke="#8A3E0A" stroke-width="1.8"/></g>
<rect x="102" y="50" width="6" height="12" rx="2" fill="#5BC0A0" {W(1.8)}/>
{face(62, 82, d=11, k=0.85)}
'''), "герой: сушёный абрикос-урюк | сцена: сушится на бельевой верёвке на прищепке под жарким солнцем")

# 18 Маман (Мытищи, семейное кафе) — тарелка манной каши, в которую ныряет кусочек сливочного масла
I["cafe-maman-mytishchi"] = (svg2("#FFF1F6", "#F2A8C4", f'''
<ellipse cx="64" cy="96" rx="54" ry="20" fill="#7CC4F0" {s()}/>
<ellipse cx="64" cy="92" rx="44" ry="14" fill="#FFFDF4" {W(2.6)}/>
<path d="M30 96 Q64 104 98 96" fill="none" stroke="#5AA8DA" stroke-width="2" stroke-dasharray="3 4"/>
<path d="M58 84 Q52 78 56 74 Q60 72 62 76 Q64 72 68 74 Q72 78 66 84 L62 88Z" fill="#E8394A" {W(1.8)}/>
<g transform="rotate(30 86 44)"><rect x="76" y="34" width="20" height="16" rx="3" fill="#FFE27A" {W(2.4)}/>
<path d="M80 38 H90" stroke="#fff" stroke-width="2" stroke-linecap="round"/></g>
{eye(82, 44, 0.55)}{eye(90, 48, 0.55)}
<path d="M80 74 Q84 66 88 72 M74 72 Q72 64 78 62" fill="none" stroke="#7CC4F0" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="70" cy="68" r="2" fill="#7CC4F0"/><circle cx="96" cy="70" r="2" fill="#7CC4F0"/>
{face(48, 94, d=8, k=0.75)}
'''), "герой: тарелка манной каши с вареньем-сердечком | сцена: в неё, как в бассейн, ныряет кусочек сливочного масла")

# 19 Буревестник (ресторан яхт-клуба, Клязьминское водохранилище) — расстегай качается на волнах у причала рядом с буйком
I["cafe-burevestnik-yacht"] = (svg2("#E6F7FF", "#2C7FB8", f'''
<path d="M0 78 Q16 70 32 78 Q48 86 64 78 Q80 70 96 78 Q112 86 128 78 V130 H0Z" fill="#2F8FD0" {W(2.4)}/>
<path d="M8 98 Q20 92 32 98 M76 108 Q88 102 100 108" fill="none" stroke="#9AD6FF" stroke-width="2.6" stroke-linecap="round"/>
<rect x="0" y="54" width="34" height="8" fill="#A9764E" {W(2.2)}/><path d="M8 62 V96 M26 62 V96" stroke="#7A5232" stroke-width="4"/>
<path d="M100 74 L106 46 L112 74Z" fill="#E8553E" {W(2.2)}/><path d="M102 64 H110" stroke="#fff" stroke-width="3"/>
<ellipse cx="106" cy="76" rx="10" ry="4" fill="#E8553E" {W(2)}/>
<path d="M30 78 Q30 52 64 46 Q98 52 98 78 Q64 90 30 78Z" fill="#E3A24B" {s()}/>
<ellipse cx="64" cy="58" rx="12" ry="6" fill="#FFE9C2" {W(2.2)}/>
<path d="M56 58 Q60 54 64 58 Q68 54 72 58" fill="none" stroke="#F08C6A" stroke-width="2.2"/>
<path d="M36 70 Q44 64 50 70 M78 70 Q84 64 92 70" fill="none" stroke="#C47A25" stroke-width="2"/>
{face(64, 72, d=11, k=0.8)}
<path d="M60 30 Q66 22 72 30 Q78 22 84 30" fill="none" {W(2.4)}/>
'''), "герой: пирожок-расстегай с рыбной начинкой | сцена: качается на волнах у причала яхт-клуба рядом с красным буйком")

# 20 Джавахк (Люберцы, хинкальная) — сладкая армянская гата с узором под двуглавой горой
I["cafe-dzhavakhk-lyubertsy"] = (svg2("#FFEFD8", "#D9A0C8", f'''
<path d="M-4 84 L30 30 L46 50 L66 18 L104 72 L132 84Z" fill="#E8F0FF" {W(2.6)}/>
<path d="M22 44 L30 30 L38 40 Q30 46 22 44Z M58 30 L66 18 L76 32 Q66 38 58 30Z" fill="#FFFFFF" {W(2)}/>
<rect x="0" y="84" width="128" height="46" fill="#C98A5A" {W(2.4)}/>
<ellipse cx="64" cy="102" rx="46" ry="12" fill="#fff" {s()}/>
<ellipse cx="64" cy="88" rx="40" ry="20" fill="#E9B04E" {s()}/>
<ellipse cx="64" cy="84" rx="30" ry="12" fill="none" stroke="#B9732E" stroke-width="2.4"/>
<path d="M44 84 Q54 74 64 84 Q74 94 84 84" fill="none" stroke="#B9732E" stroke-width="2.4"/>
<circle cx="64" cy="84" r="3" fill="#B9732E"/>
<path d="M36 84 L32 80 M92 84 L96 80 M64 70 V66" stroke="#B9732E" stroke-width="2" stroke-linecap="round"/>
{eye(52, 94, 0.7)}{eye(76, 94, 0.7)}
<path d="M60 99 Q64 102 68 99" fill="none" {W(2)}/>
'''), "герой: круглая армянская гата с выпечным узором | сцена: лежит на блюде под заснеженной двуглавой горой")

# 21 Эристави (Новинки, грузинская) — кукурузная лепёшка мчади танцует лезгинку на цыпочках
I["cafe-eristavi-novinki"] = (svg2("#FFF8D6", "#6CB8A0", f'''
<ellipse cx="64" cy="116" rx="36" ry="6" fill="#2F7A6A" opacity=".35"/>
<path d="M50 96 L44 116 M78 96 L84 116" {W(3.4)}/>
<path d="M40 116 H50 M80 116 H90" {W(4)}/>
<ellipse cx="64" cy="70" rx="30" ry="28" fill="#F2C433" {s()}/>
<circle cx="50" cy="56" r="1.8" fill="#C8921A"/><circle cx="76" cy="54" r="1.8" fill="#C8921A"/><circle cx="82" cy="78" r="1.8" fill="#C8921A"/><circle cx="46" cy="82" r="1.8" fill="#C8921A"/><circle cx="64" cy="92" r="1.8" fill="#C8921A"/>
<path d="M36 64 L16 44 M92 64 L112 70" {W(3.4)}/>
<path d="M16 44 L10 40 M112 70 L120 70" {W(3)}/>
{face(64, 68, d=10, k=0.9)}
<path d="M26 98 Q20 92 24 86 M104 96 Q110 90 106 84" fill="none" {W(2.2)} stroke-dasharray="3 3"/>
{sparkle(108, 30, 5, "#fff")}
'''), "герой: жёлтая кукурузная лепёшка мчади | сцена: танцует лезгинку на цыпочках, раскинув руки")

# 22 ВИЛЛАДЖ (Балашиха, семейный ресторан) — печёное яблоко с палочкой корицы греется в чугунке у деревенской печки
I["cafe-village-balashikha"] = (svg2("#FFE6D8", "#B5644A", f'''
<rect x="0" y="0" width="128" height="80" fill="#F4E9DC" opacity=".5"/>
<path d="M0 30 H128 M0 54 H128 M30 30 V54 M74 30 V54 M108 30 V54 M14 6 V30 M52 6 V30 M92 6 V30" stroke="#D9B9A2" stroke-width="2"/>
<rect x="0" y="80" width="128" height="50" fill="#7A4A32" {W(2.4)}/>
<path d="M22 70 H106 L100 112 Q64 120 28 112Z" fill="#3F3F4A" {s()}/>
<path d="M18 70 H110" {W(5)}/><path d="M18 70 H110" stroke="#5B5B66" stroke-width="2.4"/>
<path d="M30 70 Q30 30 64 32 Q98 30 98 70Z" fill="#C93A2A" {s()}/>
<path d="M42 50 Q48 42 56 46" fill="none" stroke="#F07A5A" stroke-width="3" stroke-linecap="round"/>
<path d="M60 34 Q60 22 70 16" {W(3)}/><rect x="66" y="10" width="20" height="7" rx="3" transform="rotate(-30 76 13)" fill="#9A5A2E" {W(2)}/>
<path d="M36 58 Q44 66 52 60 M76 60 Q84 66 92 58" fill="none" stroke="#FFF3D6" stroke-width="3" stroke-linecap="round"/>
{face(64, 56, d=10, k=0.8)}
<path d="M20 26 Q16 16 22 8 M108 26 Q112 16 106 8" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
'''), "герой: печёное яблоко с палочкой корицы | сцена: греется в чугунке у деревенской печки")

# 23 Dolce casa (Красногорск) — слоёная ракушка сфольятелла на пороге итальянского домика с зелёными ставнями
I["cafe-dolce-casa-krasnogorsk"] = (svg2("#FFFBEA", "#F2C36A", f'''
<rect x="14" y="16" width="100" height="94" fill="#F7B08A" {s()}/>
<rect x="20" y="28" width="22" height="26" fill="#9ED6FF" {W(2.2)}/><rect x="12" y="28" width="8" height="26" fill="#3E9C5A" {W(2)}/><rect x="42" y="28" width="8" height="26" fill="#3E9C5A" {W(2)}/>
<rect x="86" y="28" width="22" height="26" fill="#9ED6FF" {W(2.2)}/><rect x="78" y="28" width="8" height="26" fill="#3E9C5A" {W(2)}/><rect x="108" y="28" width="8" height="26" fill="#3E9C5A" {W(2)}/>
<path d="M52 110 V70 Q64 58 76 70 V110" fill="#8B5A3C" {W(2.6)}/>
<rect x="0" y="108" width="128" height="22" fill="#E2D2BE" {W(2.4)}/>
<path d="M36 112 Q30 84 64 76 Q98 84 92 112Z" fill="#F0C27A" {s()}/>
<path d="M64 78 L64 110 M64 78 L46 108 M64 78 L82 108 M64 78 L38 100 M64 78 L90 100" stroke="#C88F3E" stroke-width="2"/>
<path d="M38 112 H90" {W(3)}/>
<circle cx="58" cy="78" r="1.5" fill="#fff"/><circle cx="70" cy="80" r="1.5" fill="#fff"/><circle cx="64" cy="76" r="1.5" fill="#fff"/>
{eye(54, 96, 0.7)}{eye(74, 96, 0.7)}
<path d="M60 102 Q64 105 68 102" fill="none" {W(2)}/>
'''), "герой: слоёная ракушка сфольятелла | сцена: встречает гостей на пороге итальянского домика с зелёными ставнями")

# 24 Круассан&кофе (Туристская) — булочка пен-о-шоколя спит в корзинке под салфеткой, рядом кофейное зерно-ночник
I["cafe-kruassan-kofe-turistskaya"] = (svg2("#2F2A4A", "#5A3E2E", f'''
<circle cx="102" cy="26" r="10" fill="#FFF3B0" opacity=".9"/><circle cx="106" cy="23" r="9" fill="#2F2A4A"/>
<circle cx="24" cy="20" r="1.6" fill="#fff"/><circle cx="54" cy="12" r="1.4" fill="#fff"/><circle cx="80" cy="30" r="1.2" fill="#fff"/>
<path d="M14 82 H114 L104 114 H24Z" fill="#C88A52" {s()}/>
<path d="M18 92 H110 M22 102 H106" stroke="#9E6638" stroke-width="2.4"/>
<path d="M34 82 V112 M54 82 V114 M74 82 V114 M94 82 V112" stroke="#9E6638" stroke-width="2"/>
<rect x="32" y="56" width="62" height="30" rx="8" fill="#E8B05A" {s()}/>
<path d="M46 58 V84 M80 58 V84" stroke="#6A3A1E" stroke-width="5" stroke-linecap="round"/>
<path d="M14 82 Q40 66 74 76 Q100 70 114 82 L110 92 Q64 84 18 92Z" fill="#F4F4FF" {W(2.6)}/>
<path d="M30 84 L36 80 M50 82 L56 78 M80 80 L86 76" stroke="#E25F79" stroke-width="2"/>
<path d="M54 66 Q58 69 62 66 M66 66 Q70 69 74 66" fill="none" {W(2)}/>
<ellipse cx="54" cy="72" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/><ellipse cx="74" cy="72" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/>
<text x="82" y="54" font-family="Arial" font-weight="bold" font-size="10" fill="#fff">z</text><text x="90" y="44" font-family="Arial" font-weight="bold" font-size="8" fill="#fff">z</text>
<ellipse cx="18" cy="62" rx="8" ry="11" fill="#7A4A2A" {W(2.2)}/><path d="M18 52 Q14 62 18 72" fill="none" stroke="#3B2416" stroke-width="2"/>
<circle cx="18" cy="62" r="16" fill="#FFE68A" opacity=".18"/>
'''), "герой: булочка пен-о-шоколя с двумя шоколадными полосками | сцена: спит в плетёной корзинке под салфеткой, рядом светится кофейное зерно-ночник")

# 25 Кондитерская Натальи Пахомовой (Сергиев Посад) — ромовая баба в глазури под золотыми куполами
I["cafe-pakhomova-sergiev-posad"] = (svg2("#E8F4FF", "#7FA6E0", f'''
<rect x="8" y="58" width="22" height="40" fill="#fff" {W(2.2)}/><path d="M8 58 Q19 36 30 58Z" fill="#3E7FD8" {W(2.2)}/><path d="M19 40 V30 M15 34 H23" {W(1.8)}/>
<rect x="98" y="50" width="24" height="48" fill="#fff" {W(2.2)}/><path d="M98 50 Q110 26 122 50Z" fill="#F2B21A" {W(2.2)}/><path d="M110 30 V18 M106 23 H114" {W(1.8)}/>
<circle cx="104" cy="44" r="1.6" fill="#fff"/><circle cx="12" cy="52" r="1.4" fill="#fff"/>
<rect x="0" y="98" width="128" height="32" fill="#CFE6C0" {W(2.2)}/>
<ellipse cx="64" cy="108" rx="38" ry="8" fill="#fff" {s()}/>
<path d="M36 106 L40 60 Q64 48 88 60 L92 106Z" fill="#D9963E" {s()}/>
<path d="M38 74 Q64 66 90 74 M37 90 Q64 82 91 90" fill="none" stroke="#B5702A" stroke-width="2"/>
<path d="M38 62 Q40 46 64 42 Q88 46 90 62 Q86 70 82 64 Q78 74 72 64 Q66 72 60 64 Q54 72 48 64 Q42 70 38 62Z" fill="#FFF6EA" {W(2.6)}/>
<circle cx="64" cy="38" r="6" fill="#C8243F" {W(2.2)}/><path d="M64 32 Q66 24 72 22" fill="none" stroke="#3E9C3A" stroke-width="2.4" stroke-linecap="round"/>
{face(64, 84, d=11, k=0.85)}
'''), "герой: ромовая баба в белой глазури с вишенкой | сцена: стоит на блюде под золотыми и синими куполами")

# 26 Репаст (Фили) — пастуший пирог в форме: по картофельным гребешкам, как по волнам, катается горошинка-сёрфер
I["cafe-repast-fili"] = (svg2("#E2FFF6", "#38A89D", f'''
<rect x="14" y="66" width="100" height="44" rx="8" fill="#F3F0E6" {s()}/>
<path d="M14 80 H114" stroke="#7FC4E8" stroke-width="3"/>
<path d="M8 72 H20 M108 72 H120" {W(5)}/>
<path d="M18 70 Q24 50 34 60 Q42 46 52 58 Q60 42 70 56 Q78 44 88 58 Q96 48 104 62 Q110 56 110 70Z" fill="#FFD77A" {s()}/>
<path d="M30 64 Q34 58 38 62 M58 54 Q62 50 66 54 M86 60 Q90 56 94 60" fill="none" stroke="#E2A23A" stroke-width="2.2" stroke-linecap="round"/>
<g transform="rotate(-14 64 32)"><ellipse cx="64" cy="38" rx="16" ry="4" fill="#E8553E" {W(2.2)}/></g>
<circle cx="64" cy="26" r="9" fill="#6CC04A" {W(2.4)}/>
{eye(61, 25, 0.5)}{eye(68, 25, 0.5)}<path d="M61 29 Q64.5 31 68 29" fill="none" {W(1.6)}/>
<path d="M54 22 L46 16 M74 22 L82 18" {W(2.4)}/>
{face(64, 92, d=12, k=0.85)}
'''), "герой: пастуший пирог с картофельными гребешками | сцена: по его гребешкам, как по волнам, катается на доске горошинка")

# 27 TARTUFO (Барвиха, ТЦ «Дрим Хаус») — шоколадный трюфель катится по шоколадной горке-жёлобу
I["cafe-tartufo-barvikha"] = (svg2("#F7E9FF", "#9B6BC6", f'''
<path d="M-4 30 Q60 40 86 96 L128 104 V130 H-4Z" fill="#7A4326" {s()}/>
<path d="M-4 42 Q54 52 78 104 L128 112" fill="none" stroke="#A8643A" stroke-width="3"/>
<path d="M10 34 Q12 44 8 50 M30 38 Q32 48 28 52" fill="none" stroke="#5A2E18" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="64" cy="60" r="24" fill="#5A3020" {s()}/>
<circle cx="54" cy="48" r="1.6" fill="#C89A6A"/><circle cx="72" cy="46" r="1.6" fill="#C89A6A"/><circle cx="78" cy="64" r="1.6" fill="#C89A6A"/><circle cx="50" cy="70" r="1.6" fill="#C89A6A"/><circle cx="66" cy="76" r="1.6" fill="#C89A6A"/>
<path d="M50 40 Q56 34 64 36" fill="none" stroke="#8A5A40" stroke-width="2.4" stroke-linecap="round"/>
{eye(56, 58, 0.75)}{eye(72, 58, 0.75)}
<ellipse cx="64" cy="67" rx="4" ry="3" fill="#FF8FB0" {W(1.8)}/>
<ellipse cx="50" cy="64" rx="3.4" ry="2" fill="#FF7FA8" opacity=".6"/><ellipse cx="78" cy="64" rx="3.4" ry="2" fill="#FF7FA8" opacity=".6"/>
<path d="M30 44 Q24 50 26 58 M34 36 Q26 38 22 44" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".8"/>
{sparkle(100, 28, 6, "#FFF")}{sparkle(110, 52, 4, "#FFE07A")}
'''), "герой: шоколадный трюфель в какао-крошке | сцена: с восторгом катится вниз по шоколадной горке-жёлобу")

# 28 Боргетто (Академическая, итальянская) — сицилийский канноло трубит, как в трубу, выдувая кремовые звёздочки
I["cafe-borgetto-akademicheskaya"] = (svg2("#E9FBEA", "#E7A3B0", f'''
<g transform="rotate(-24 56 72)">
<rect x="18" y="56" width="70" height="30" rx="6" fill="#D9963E" {s()}/>
<path d="M30 58 L26 84 M44 58 L40 86 M58 58 L54 86 M72 58 L68 86" stroke="#B5702A" stroke-width="2.2"/>
<ellipse cx="90" cy="71" rx="10" ry="17" fill="#FFF8EC" {s()}/>
<ellipse cx="16" cy="71" rx="7" ry="13" fill="#FFF8EC" {s()}/>
<circle cx="92" cy="62" r="2" fill="#3E9C3A"/><circle cx="88" cy="78" r="2" fill="#3E9C3A"/><circle cx="14" cy="68" r="1.8" fill="#3E9C3A"/>
</g>
{face(50, 74, d=9, k=0.8, mouth=False)}
<ellipse cx="50" cy="83" rx="3.6" ry="3" fill="#7A2645" {W(1.6)}/>
<path d="M98 50 L108 40" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M104 34 L106 28 L108 34 L114 34 L109 38 L111 44 L106 40 L101 44 L103 38 L98 34Z" fill="#FFF4D6" {W(1.8)}/>
<path d="M114 56 L115 52 L117 56 L121 56 L118 59 L119 63 L115 61 L112 63 L113 59 L110 56Z" fill="#FFF4D6" {W(1.6)}/>
<path d="M90 22 L91 18 L93 22 L97 22 L94 25 L95 29 L91 27 L88 29 L89 25 L86 22Z" fill="#FFF4D6" {W(1.6)}/>
'''), "герой: сицилийский канноло с рикоттой и фисташками | сцена: трубит, как в трубу, и выдувает кремовые звёздочки")

# 29 Швили («Байконур», Отрадное) — круглый грузинский пирог кубдари летит над космодромом, как летающая тарелка
I["cafe-shvili-baykonur"] = (svg2("#2B2F6E", "#0E1236", f'''
<circle cx="18" cy="24" r="1.6" fill="#fff"/><circle cx="40" cy="12" r="1.2" fill="#fff"/><circle cx="104" cy="18" r="1.6" fill="#fff"/><circle cx="114" cy="40" r="1.2" fill="#fff"/><circle cx="26" cy="54" r="1.2" fill="#fff"/>
<rect x="0" y="104" width="128" height="26" fill="#C9A87A" {W(2.2)}/>
<path d="M16 104 V78 L22 70 L28 78 V104" fill="#E0E4F0" {W(2.2)}/><path d="M22 70 V62" {W(2)}/>
<path d="M98 104 L108 84 L118 104" fill="none" {W(2.4)}/><path d="M100 98 H116 M103 92 H113" {W(1.8)}/>
<path d="M44 82 L36 110 M84 82 L92 110" stroke="#FFE68A" stroke-width="5" opacity=".5" stroke-linecap="round"/>
<ellipse cx="64" cy="70" rx="44" ry="14" fill="#D98A3A" {s()}/>
<path d="M28 64 Q64 30 100 64" fill="#E8A64E" {s()}/>
<path d="M40 62 Q46 54 52 60 M76 60 Q82 54 88 62" fill="none" stroke="#B9682A" stroke-width="2.2"/>
<path d="M50 50 L46 44 M64 46 V40 M78 50 L82 44" stroke="#B9682A" stroke-width="2" stroke-linecap="round"/>
<circle cx="32" cy="72" r="2.4" fill="#FFE68A"/><circle cx="64" cy="76" r="2.4" fill="#FFE68A"/><circle cx="96" cy="72" r="2.4" fill="#FFE68A"/>
{face(64, 58, d=10, k=0.8)}
'''), "герой: круглый грузинский пирог кубдари | сцена: летит над космодромом, как летающая тарелка с огоньками")

# 30 Швили («Кунцево Плаза») — изумрудный лимонад «Тархун» поднимают в воздух его же пузыри, как воздушные шары
I["cafe-shvili-kuntsevo"] = (svg2("#FFF7E0", "#F0C25A", f'''
<path d="M40 54 Q30 30 26 12 M64 50 V6 M88 54 Q98 30 104 14" fill="none" {W(1.8)}/>
<circle cx="26" cy="14" r="11" fill="#9EF0C0" opacity=".9" {W(2.2)}/><circle cx="64" cy="10" r="12" fill="#9EF0C0" opacity=".9" {W(2.2)}/><circle cx="104" cy="16" r="10" fill="#9EF0C0" opacity=".9" {W(2.2)}/>
<circle cx="22" cy="10" r="3" fill="#fff" opacity=".8"/><circle cx="60" cy="6" r="3" fill="#fff" opacity=".8"/><circle cx="100" cy="12" r="3" fill="#fff" opacity=".8"/>
<path d="M38 52 H90 L84 112 Q64 118 44 112Z" fill="#3FCB7E" opacity=".95" {s()}/>
<path d="M40 64 H88" stroke="#2A9A5A" stroke-width="2.2"/>
<circle cx="52" cy="98" r="3" fill="#B8F5D2"/><circle cx="76" cy="92" r="2.4" fill="#B8F5D2"/><circle cx="70" cy="104" r="2" fill="#B8F5D2"/>
<path d="M46 72 Q44 84 48 96" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".6"/>
<path d="M78 56 Q86 46 96 50 Q90 58 78 56Z" fill="#2E8A3A" {W(2)}/>
{face(64, 80, d=11, k=0.85)}
'''), "герой: изумрудный лимонад «Тархун» в высоком стакане | сцена: собственные пузырьки поднимают его в небо, как воздушные шары")

# 31 Goodman (ТРЦ «Columbus», стейк-хаус) — стейк-томагавк на длинной косточке гордо стоит на разделочной доске с розмарином
I["cafe-goodman-columbus"] = (svg2("#FFE9DE", "#8A3B33", f'''
<rect x="8" y="88" width="112" height="22" rx="8" fill="#C8894E" {s()}/>
<circle cx="110" cy="99" r="4" fill="#8A5A30" {W(2)}/>
<path d="M18 96 H90 M22 104 H80" stroke="#A86A36" stroke-width="2"/>
<path d="M78 70 L104 18" stroke="{O}" stroke-width="13" stroke-linecap="round"/>
<path d="M78 70 L104 18" stroke="#FFF6E6" stroke-width="8" stroke-linecap="round"/>
<circle cx="100" cy="16" r="7" fill="#FFF6E6" {W(2.4)}/><circle cx="110" cy="22" r="7" fill="#FFF6E6" {W(2.4)}/>
<path d="M20 84 Q14 50 46 44 Q78 40 86 66 Q90 88 60 90 Q28 92 20 84Z" fill="#B5442E" {s()}/>
<path d="M30 62 L70 54 M28 74 L74 66" stroke="#6A2316" stroke-width="3.4" stroke-linecap="round"/>
<path d="M36 52 Q50 46 64 50" fill="none" stroke="#F3D6C6" stroke-width="3" stroke-linecap="round"/>
{face(52, 70, d=10, k=0.85)}
<path d="M92 86 Q102 70 114 66" fill="none" stroke="#3E7A2A" stroke-width="2.4"/>
<path d="M96 80 L92 74 M100 76 L98 69 M104 73 L104 66 M108 70 L110 64" stroke="#5DB34A" stroke-width="2.4" stroke-linecap="round"/>
'''), "герой: стейк-томагавк на длинной косточке | сцена: гордо лежит на разделочной доске рядом с веточкой розмарина")

# 32 «Страна, которой нет» (Охотный Ряд) — пирожное «картошка» с кремовыми ростками летает на вафельных крылышках среди звёзд
I["cafe-strana-kotoroy-net"] = (svg2("#7F6BD8", "#2C2470", f'''
<circle cx="20" cy="30" r="1.6" fill="#fff"/><circle cx="104" cy="22" r="1.8" fill="#fff"/><circle cx="112" cy="84" r="1.4" fill="#fff"/><circle cx="16" cy="96" r="1.4" fill="#fff"/>
{sparkle(30, 70, 5, "#FFE68A")}{sparkle(100, 46, 6, "#FFE68A")}{sparkle(84, 108, 4, "#fff")}
<path d="M30 112 Q48 104 64 112 Q80 120 98 110" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="2 6" opacity=".7"/>
<g transform="rotate(-30 40 60)"><rect x="18" y="50" width="26" height="14" rx="3" fill="#F6D48A" {W(2.2)}/><path d="M24 50 V64 M31 50 V64 M38 50 V64 M18 57 H44" stroke="#D9A74A" stroke-width="1.6"/></g>
<g transform="rotate(30 88 60)"><rect x="84" y="50" width="26" height="14" rx="3" fill="#F6D48A" {W(2.2)}/><path d="M90 50 V64 M97 50 V64 M104 50 V64 M84 57 H110" stroke="#D9A74A" stroke-width="1.6"/></g>
<path d="M30 78 Q28 58 52 58 Q66 54 82 58 Q102 60 100 80 Q98 96 72 96 Q56 98 42 94 Q30 90 30 78Z" fill="#7A4A2E" {s()}/>
<circle cx="44" cy="70" r="1.6" fill="#A8744E"/><circle cx="84" cy="68" r="1.6" fill="#A8744E"/><circle cx="88" cy="86" r="1.6" fill="#A8744E"/><circle cx="40" cy="86" r="1.6" fill="#A8744E"/><circle cx="62" cy="64" r="1.6" fill="#A8744E"/>
<circle cx="54" cy="56" r="6" fill="#FFF3D6" {W(2)}/><circle cx="74" cy="56" r="6" fill="#FFF3D6" {W(2)}/>
<path d="M51 55 Q54 52 57 55 M71 55 Q74 52 77 55" fill="none" stroke="#E8CFA0" stroke-width="1.6"/>
{face(64, 78, d=10, k=0.85)}
'''), "герой: пирожное «картошка» с кремовыми ростками | сцена: летает на вафельных крылышках среди звёзд")


if __name__ == "__main__":
    reg = os.path.join(ROOT, "icons-src", "subjects.txt")
    lines = open(reg, encoding="utf-8").read().splitlines()
    lines = [l for l in lines if l.split(" — ", 1)[0] not in I]
    for pid, (svg_, subj) in I.items():
        open(os.path.join(ROOT, "icons-src", pid + ".svg"), "w").write(svg_)
        lines.append(f"{pid} — {subj}")
    open(reg, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("иконок:", len(I))
