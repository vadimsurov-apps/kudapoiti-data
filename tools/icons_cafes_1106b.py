"""Иконки робота cafes, 2026-11-06 (утро): 36 новых сюжетов «еда, посуда, кухня, сладости»
(сверено со всеми листами icons-catalog и icons-src/subjects.txt). Порядок = порядок мест в tools/cafes_1106b_data.json."""
import json, os
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=8, k=0.7, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); src = os.path.join(here, "..", "icons-src")
steam = lambda *xs: "".join(f'<path d="M{x} 30 Q{x+4} 22 {x} 14" fill="none" stroke="#fff" stroke-width="3" opacity=".9"/>' for x in xs)
dots = lambda pts, c, r=2.2: "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x, y in pts)

L = [
 # 1 трюфель
 ("pink", "конфета-трюфель в гофрированной формочке",
  f'<path d="M22 72 L34 112 H94 L106 72Z" fill="#FFD25E" {s()}/>'
  + "".join(f'<path d="M{x} 74 L{x+ (x-64)*0.12:.0f} 110" stroke="#E0A55E" stroke-width="2.4"/>' for x in range(32, 100, 9))
  + f'<circle cx="64" cy="58" r="36" fill="#6B3E26" {s()}/>'
  + dots([(42, 44), (52, 30), (78, 34), (88, 50), (74, 26), (46, 70), (86, 70)], "#A87452", 2.4)
  + f'<path d="M48 36 Q54 30 62 30" fill="none" stroke="#fff" stroke-width="3" opacity=".5"/>'
  + f(64, 58, d=10, k=0.75).replace(O, "#fff") + sparkle(106, 30, 7)),
 # 2 лопата для пиццы
 ("orange", "лопата для пиццы", f'<rect x="58" y="78" width="12" height="40" rx="5" fill="#B97A4A" {s()}/>'
  f'<path d="M24 52 Q24 18 64 18 Q104 18 104 52 Q104 82 76 82 H52 Q24 82 24 52Z" fill="#E6B07A" {s()}/>'
  f'<circle cx="64" cy="50" r="24" fill="#FFD25E" stroke="#E0A55E" stroke-width="4"/>' + dots([(52, 40), (76, 44), (60, 62), (78, 60)], "#E8654F", 4)
  + f(64, 48, d=8, k=0.6)),
 # 3 соусник
 ("teal", "соусник с подливой", f'<path d="M20 58 Q40 50 64 54 L104 46 Q100 58 92 62 Q92 92 64 96 Q36 96 30 72 Q22 66 20 58Z" fill="#fff" {s()}/>'
  f'<path d="M30 60 Q60 56 98 50" fill="none" stroke="#B97A4A" stroke-width="5" stroke-linecap="round"/>'
  f'<path d="M36 100 H92 L86 108 H42Z" fill="#9FE0D2" {s()}/><path d="M28 70 Q12 72 16 86 Q20 94 32 86" fill="none" {W(4)}/>'
  + f(62, 76, d=9, k=0.7)),
 # 4 тажин
 ("orange", "тажин (горшок с конусной крышкой)", f'<ellipse cx="64" cy="98" rx="50" ry="14" fill="#D96A3F" {s()}/>'
  f'<path d="M22 94 Q48 86 56 30 Q64 16 72 30 Q80 86 106 94 Q64 104 22 94Z" fill="#F08A4B" {s()}/>'
  f'<circle cx="64" cy="20" r="7" fill="#FFD25E" {W(2.4)}/>'
  f'<path d="M36 88 Q64 96 92 88" fill="none" stroke="#FFE2B8" stroke-width="4" stroke-linecap="round"/>'
  + dots([(44, 82), (54, 84), (64, 85), (74, 84), (84, 82)], "#2F8F83", 2.4) + f(64, 64, d=8, k=0.65)),
 # 5 кулинарная горелка
 ("night", "кулинарная горелка", f'<path d="M64 14 Q78 30 70 44 Q66 36 60 38 Q52 44 58 54 Q44 46 48 30 Q52 22 64 14Z" fill="#6CC0F2" {W(2.4)}/>'
  f'<path d="M64 26 Q70 36 66 46 Q62 42 60 44 Q58 36 64 26Z" fill="#fff"/>'
  f'<rect x="54" y="52" width="20" height="12" rx="3" fill="#C9D3E0" {s()}/><rect x="44" y="62" width="40" height="52" rx="10" fill="#E8654F" {s()}/>'
  f'<rect x="84" y="70" width="12" height="18" rx="4" fill="#3B3355"/>' + f(64, 84, d=9, k=0.7) + sparkle(100, 32, 6)),
 # 6 самовар
 ("pink", "самовар", f'<path d="M58 14 H70 L72 24 H56Z" fill="#E0A55E" {s()}/>'
  f'<path d="M40 24 H88 Q96 54 88 84 H40 Q32 54 40 24Z" fill="#FFC94D" {s()}/>'
  f'<path d="M36 40 Q20 40 22 56 M92 40 Q108 40 106 56" fill="none" {W(5)}/>'
  f'<path d="M50 84 L44 104 H84 L78 84Z" fill="#E0A55E" {s()}/><path d="M30 106 H98" {W(5)}/>'
  f'<path d="M88 66 H104 V74" fill="none" {W(4)}/>' + f(64, 54, d=10, k=0.8)),
 # 7 хлебопечка
 ("green", "хлебопечка", f'<rect x="22" y="40" width="84" height="70" rx="14" fill="#F4F8FF" {s()}/>'
  f'<rect x="34" y="50" width="60" height="26" rx="6" fill="#FFE7A3" {W(2.6)}/><path d="M42 76 Q42 56 64 56 Q86 56 86 76Z" fill="#D9963F" {W(2.4)}/>'
  f'<rect x="80" y="88" width="16" height="8" rx="3" fill="#7CD26E" {W(2)}/><circle cx="36" cy="92" r="4" fill="#FF8FB8"/>'
  + f(58, 92, d=8, k=0.6) + steam(54, 72)),
 # 8 противень с печеньем
 ("yellow", "противень с печеньем", f'<path d="M12 60 L24 96 H104 L116 60Z" fill="#C9D3E0" {s()}/>'
  + "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="#E6B07A" {W(2.4)}/>' for x, y in [(36, 74), (64, 70), (92, 74)])
  + dots([(32, 72), (40, 78), (88, 70), (96, 78)], "#6B3E26", 2.4)
  + f(64, 70, d=5, k=0.45, blush=False) + steam(48, 64, 80)),
 # 9 фудтрак
 ("sky", "фургон с едой (фудтрак)", f'<rect x="12" y="40" width="88" height="56" rx="8" fill="#FF8FB8" {s()}/>'
  f'<path d="M100 56 H110 Q116 56 116 64 V96 H100Z" fill="#FF8FB8" {s()}/>'
  f'<rect x="22" y="50" width="52" height="26" rx="4" fill="#FFF3D6" {W(2.6)}/><path d="M18 50 H78 L74 42 H22Z" fill="#FFD25E" {W(2.4)}/>'
  f'<path d="M22 42 L28 50 L34 42 L40 50 L46 42 L52 50 L58 42 L64 50 L70 42" fill="none" stroke="#E8654F" stroke-width="2"/>'
  f'<circle cx="34" cy="98" r="10" fill="#3B3355"/><circle cx="92" cy="98" r="10" fill="#3B3355"/><circle cx="34" cy="98" r="4" fill="#fff"/><circle cx="92" cy="98" r="4" fill="#fff"/>'
  + f(48, 62, d=8, k=0.55)),
 # 10 чесночница
 ("purple", "пресс для чеснока (чесночница)", f'<path d="M18 46 L64 58 L110 30" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>'
  f'<path d="M18 46 L64 58 L110 30" fill="none" stroke="#C9D3E0" stroke-width="7" stroke-linecap="round"/>'
  f'<path d="M30 70 L64 62 L104 86" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>'
  f'<path d="M30 70 L64 62 L104 86" fill="none" stroke="#C9D3E0" stroke-width="7" stroke-linecap="round"/>'
  f'<circle cx="64" cy="60" r="7" fill="#7A869C" {W(2.4)}/>'
  f'<path d="M50 84 Q52 100 44 110 M58 84 Q60 102 56 112" fill="none" stroke="#F5E6A8" stroke-width="5" stroke-linecap="round"/>'
  + f(84, 84, d=5, k=0.45, blush=False)),
 # 11 кастрюля
 ("blue", "кастрюля в горошек", f'<path d="M26 48 H102 V96 Q102 110 88 110 H40 Q26 110 26 96Z" fill="#FFF3D6" {s()}/>'
  f'<path d="M26 56 H12 M102 56 H116" {W(6)}/><path d="M22 48 Q64 30 106 48Z" fill="#E8654F" {s()}/><rect x="56" y="28" width="16" height="8" rx="4" fill="#3B3355"/>'
  + dots([(38, 66), (90, 66), (40, 98), (88, 98), (64, 102)], "#E8654F", 3.4) + f(64, 76, d=10, k=0.75) + steam(48, 80)),
 # 12 картофелемялка
 ("teal", "толкушка для пюре", f'<rect x="56" y="12" width="16" height="54" rx="7" fill="#E6B07A" {s()}/>'
  f'<path d="M64 64 V78 M40 78 Q40 104 64 104 Q88 104 88 78Z" fill="none" {W(6)}/>'
  f'<path d="M40 78 Q40 104 64 104 Q88 104 88 78" fill="none" stroke="#C9D3E0" stroke-width="2.5"/>'
  f'<path d="M30 110 Q64 92 98 110 L98 118 H30Z" fill="#FFE7A3" {W(2.6)}/>' + f(64, 36, d=4, k=0.4, blush=False)),
 # 13 связка баранок
 ("orange", "связка баранок", f'<path d="M64 8 V24" {W(3)}/><path d="M64 24 Q20 60 64 116 Q108 60 64 24" fill="none" stroke="#B97A4A" stroke-width="3"/>'
  + "".join(f'<circle cx="{x}" cy="{y}" r="15" fill="#E0A55E" {s()}/><circle cx="{x}" cy="{y}" r="5" fill="#FFE2B8" {W(2.2)}/>'
            for x, y in [(46, 44), (82, 44), (36, 72), (92, 72), (52, 98), (76, 98)])
  + dots([(42, 38), (86, 38), (32, 66), (96, 66)], "#fff", 1.6) + f(64, 64, d=8, k=0.65)),
 # 14 кухонная мойка
 ("sky", "кухонная мойка с краном", f'<path d="M14 70 H114 V112 H14Z" fill="#B97A4A" {s()}/>'
  f'<path d="M22 70 H106 V84 Q106 92 98 92 H30 Q22 92 22 84Z" fill="#DDE4EE" {s()}/>'
  f'<path d="M64 70 V30 Q64 20 76 20 Q88 20 88 34 V42" fill="none" {W(7)}/><path d="M64 70 V30 Q64 20 76 20 Q88 20 88 34 V42" fill="none" stroke="#C9D3E0" stroke-width="3"/>'
  f'<path d="M88 50 Q84 56 88 60 Q92 56 88 50Z" fill="#6CC0F2" {W(1.6)}/>' + f(64, 100, d=10, k=0.7)),
 # 15 ложка для мёда
 ("yellow", "ложка-веретено для мёда", f'<rect x="60" y="10" width="9" height="56" rx="4" fill="#C98A52" {s()}/>'
  + "".join(f'<ellipse cx="64" cy="{y}" rx="{r}" ry="6" fill="#E0A55E" {W(2.4)}/>' for y, r in [(68, 16), (78, 20), (88, 16)])
  + f'<path d="M48 92 Q64 104 80 92 Q78 108 64 112 Q50 108 48 92Z" fill="#FFB52E" {W(2.6)}/>'
  + f'<path d="M58 96 Q56 106 62 110" fill="none" stroke="#FFE7A3" stroke-width="3"/>' + f(64, 78, d=7, k=0.5, blush=False)),
 # 16 коробочка с лапшой
 ("purple", "коробочка с лапшой навынос", f'<path d="M48 40 Q40 18 52 14 M70 40 Q78 14 86 18" fill="none" stroke="#FFD25E" stroke-width="5" stroke-linecap="round"/>'
  f'<path d="M86 8 L74 48 M98 12 L80 48" {W(4)}/>'
  f'<path d="M26 44 H102 L92 112 H36Z" fill="#fff" {s()}/><path d="M26 44 L36 34 H92 L102 44" fill="#F2EEFF" {W(2.6)}/>'
  f'<path d="M50 78 Q64 70 78 78" fill="none" stroke="#E8654F" stroke-width="4"/>' + f(64, 88, d=10, k=0.7)),
 # 17 кухонный таймер
 ("pink", "кухонный таймер", f'<circle cx="64" cy="70" r="40" fill="#7CD26E" {s()}/><circle cx="64" cy="70" r="30" fill="#fff" {W(2.6)}/>'
  f'<rect x="56" y="22" width="16" height="10" rx="3" fill="#3B3355"/>'
  + "".join(f'<path d="M64 42 V48" stroke="{O}" stroke-width="2.4" transform="rotate({a} 64 70)"/>' for a in range(0, 360, 45))
  + f'<path d="M64 70 L80 54" {W(3.4)}/>' + f(64, 80, d=9, k=0.6)),
 # 18 посудомоечная машина
 ("blue", "посудомоечная машина", f'<rect x="24" y="16" width="80" height="100" rx="10" fill="#F4F8FF" {s()}/>'
  f'<path d="M24 36 H104" {W(3)}/><rect x="46" y="22" width="36" height="8" rx="3" fill="#6CC0F2" {W(2)}/>'
  f'<circle cx="34" cy="26" r="3" fill="#7CD26E"/><path d="M34 48 V100 M94 48 V100" stroke="#C9D3E0" stroke-width="3"/>'
  + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {W(2)} opacity=".95"/>' for x, y, r in [(44, 56, 6), (84, 52, 4), (88, 98, 5)])
  + f(64, 76, d=10, k=0.8)),
 # 19 мультиварка
 ("green", "мультиварка", f'<path d="M20 60 Q20 34 64 34 Q108 34 108 60 V100 Q108 112 96 112 H32 Q20 112 20 100Z" fill="#F4F8FF" {s()}/>'
  f'<path d="M20 60 Q20 34 64 34 Q108 34 108 60Z" fill="#A98BF0" {s()}/><rect x="56" y="24" width="16" height="10" rx="4" fill="#3B3355"/>'
  f'<rect x="44" y="94" width="40" height="12" rx="4" fill="#3B3355"/><path d="M50 100 H62" stroke="#7CD26E" stroke-width="3"/>'
  + f(64, 74, d=10, k=0.75) + steam(86)),
 # 20 фритюрница
 ("orange", "фритюрница с корзинкой", f'<rect x="20" y="58" width="74" height="54" rx="10" fill="#C9D3E0" {s()}/>'
  f'<path d="M30 46 H84 L80 72 H34Z" fill="#fff" {W(2.6)}/><path d="M36 54 H78 M40 62 H74 M48 46 V72 M64 46 V72" stroke="#7A869C" stroke-width="2"/>'
  f'<path d="M84 52 H112" {W(6)}/><path d="M44 46 V30 M54 46 V26 M66 46 V32 M74 46 V28" stroke="#FFD25E" stroke-width="6" stroke-linecap="round"/>'
  + f(57, 92, d=9, k=0.7)),
 # 21 кулер для воды
 ("sky", "кулер для воды", f'<path d="M44 12 H84 Q90 12 90 20 V46 H38 V20 Q38 12 44 12Z" fill="#9DD6F5" {s()}/>'
  f'<rect x="58" y="44" width="12" height="8" fill="#6CC0F2" {W(2)}/>'
  f'<rect x="34" y="50" width="60" height="66" rx="8" fill="#F4F8FF" {s()}/>'
  f'<rect x="46" y="58" width="9" height="8" rx="2" fill="#E8654F" {W(2)}/><rect x="73" y="58" width="9" height="8" rx="2" fill="#6CC0F2" {W(2)}/>'
  f'<path d="M30 30 H32" stroke="#fff"/>' + f(64, 86, d=9, k=0.7) + sparkle(104, 26, 6)),
 # 22 овощечистка
 ("teal", "овощечистка", f'<rect x="58" y="62" width="12" height="52" rx="6" fill="#7CD26E" {s()}/>'
  f'<path d="M64 64 L40 22 H88 Z" fill="none" {W(5)}/><path d="M48 30 H80" stroke="#C9D3E0" stroke-width="4"/>'
  f'<path d="M86 44 Q104 40 108 56 Q100 50 94 58 Q96 48 86 44Z" fill="#E0A55E" {W(2.2)}/>' + f(64, 90, d=4, k=0.4, blush=False)),
 # 23 хлебница
 ("yellow", "хлебница", f'<path d="M16 108 V72 Q16 36 64 36 Q112 36 112 72 V108Z" fill="#C98A52" {s()}/>'
  f'<path d="M26 108 V76 Q26 50 64 50 Q102 50 102 76 V108" fill="#FFE2B8" {W(2.6)}/>'
  f'<path d="M34 108 Q34 74 64 74 Q94 74 94 108Z" fill="#E6B07A" {W(2.4)}/><path d="M48 84 L54 78 M62 82 L68 76 M76 84 L82 78" stroke="#B97A4A" stroke-width="2.4"/>'
  f'<rect x="56" y="40" width="16" height="6" rx="3" fill="#3B3355"/>' + f(64, 96, d=8, k=0.55)),
 # 24 бумажный пакет навынос
 ("green", "бумажный пакет навынос", f'<path d="M30 44 H98 L104 116 H24Z" fill="#E6B07A" {s()}/>'
  f'<path d="M50 44 V34 Q50 22 64 22 Q78 22 78 34 V44" fill="none" {W(4)}/>'
  f'<path d="M30 44 L36 54 L42 44 L48 54 L54 44 L60 54 L66 44 L72 54 L78 44 L84 54 L90 44 L98 50" fill="none" stroke="#B97A4A" stroke-width="2"/>'
  + f(64, 80, d=10, k=0.8) + sparkle(108, 30, 6)),
 # 25 вывеска кафе на кронштейне
 ("purple", "вывеска кафе на кронштейне", f'<path d="M12 18 H96 M22 18 L40 36" {W(5)}/><path d="M38 18 V34 M86 18 V34" {W(3)}/>'
  f'<rect x="28" y="34" width="68" height="62" rx="10" fill="#FFF3D6" {s()}/>'
  f'<path d="M48 56 H74 V70 Q74 80 61 80 Q48 80 48 70Z" fill="#fff" {W(2.6)}/><path d="M74 60 Q84 60 82 68 Q80 72 74 72" fill="none" {W(2.6)}/>'
  + f(61, 66, d=5, k=0.42, blush=False) + steam(56, 66)),
 # 26 коробка для пиццы
 ("orange", "коробка для пиццы", f'<path d="M14 70 L64 52 L114 70 L64 88Z" fill="#E6B07A" {s()}/><path d="M14 70 V86 L64 104 V88Z" fill="#C98A52" {s()}/>'
  f'<path d="M114 70 V86 L64 104 V88Z" fill="#D9A06A" {s()}/>'
  f'<path d="M14 70 L28 22 L78 6 L64 52Z" fill="#F2C890" {s()}/><path d="M38 30 Q44 26 50 30" fill="none" stroke="#E8654F" stroke-width="3"/>'
  + f(47, 34, d=7, k=0.55)),
 # 27 сифон
 ("pink", "сифон для газировки", f'<rect x="38" y="44" width="48" height="70" rx="12" fill="#9DD6F5" {s()}/>'
  f'<path d="M46 44 V30 H80 V44" fill="#C9D3E0" {s()}/><path d="M80 30 H100 L104 38" fill="none" {W(5)}/><path d="M60 30 L56 14 H76" fill="none" {W(4)}/>'
  + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" {W(1.4)}/>' for x, y in [(50, 98), (74, 102), (62, 106), (106, 50), (110, 60)])
  + f(62, 72, d=9, k=0.7)),
 # 28 автомат с газировкой
 ("teal", "автомат с газировкой", f'<rect x="28" y="10" width="72" height="108" rx="8" fill="#E8654F" {s()}/>'
  f'<rect x="38" y="20" width="52" height="22" rx="4" fill="#FFF3D6" {W(2.4)}/><path d="M46 30 H82" stroke="#E8654F" stroke-width="3"/>'
  f'<rect x="44" y="76" width="40" height="32" rx="4" fill="#3B3355"/><path d="M58 84 H70 L68 104 H60Z" fill="#9DD6F5" {W(2)}/>'
  f'<circle cx="86" cy="60" r="4" fill="#FFD25E" {W(2)}/>' + f(60, 58, d=9, k=0.6)),
 # 29 глазированный сырок
 ("night", "глазированный сырок", f'<rect x="22" y="44" width="84" height="44" rx="14" fill="#6B3E26" {s()}/>'
  f'<path d="M22 70 Q34 64 44 72 Q56 80 66 72 Q78 64 88 72 Q98 78 106 70 V76 Q106 88 94 88 H34 Q22 88 22 76Z" fill="#FFF3D6" {W(2.4)}/>'
  f'<path d="M30 50 Q36 46 44 48" fill="none" stroke="#fff" stroke-width="3" opacity=".6"/>' + f(64, 58, d=10, k=0.7).replace(O, "#fff")
  + sparkle(100, 28, 7) + sparkle(24, 102, 5)),
 # 30 формочки для печенья
 ("yellow", "формочки для печенья", f'<path d="M40 22 L48 40 L66 42 L52 54 L56 72 L40 62 L24 72 L28 54 L14 42 L32 40Z" fill="none" stroke="#FF8FB8" stroke-width="5" stroke-linejoin="round"/>'
  f'<path d="M86 60 Q86 50 96 50 Q106 50 106 62 Q106 78 86 92 Q66 78 66 62 Q66 50 76 50 Q86 50 86 60Z" fill="none" stroke="#6CC0F2" stroke-width="5" stroke-linejoin="round"/>'
  f'<circle cx="46" cy="96" r="16" fill="none" stroke="#7CD26E" stroke-width="5"/>'
  + f(40, 50, d=5, k=0.42, blush=False) + f(86, 66, d=6, k=0.42, blush=False)),
 # 31 паэлья
 ("orange", "паэлья на сковороде", f'<path d="M10 66 H24 M104 66 H118" {W(7)}/><ellipse cx="64" cy="70" rx="44" ry="34" fill="#3B3355" {s()}/>'
  f'<ellipse cx="64" cy="68" rx="38" ry="28" fill="#FFC94D"/>'
  + dots([(44, 56), (82, 60), (54, 84), (86, 80), (40, 74)], "#7CD26E", 3.6) + dots([(70, 48), (34, 66), (94, 70)], "#E8654F", 4)
  + f'<path d="M86 46 q8 0 8 8" fill="none" stroke="#FF8A5B" stroke-width="5" stroke-linecap="round"/>'
  + f'<path d="M30 52 L40 46" stroke="#FFF3A0" stroke-width="5" stroke-linecap="round"/>' + f(64, 68, d=9, k=0.7)),
 # 32 тележка мороженщика
 ("sky", "тележка мороженщика", f'<path d="M26 36 Q64 4 102 36Z" fill="#FF8FB8" {s()}/><path d="M64 36 V50" {W(3)}/>'
  f'<path d="M40 36 Q46 30 52 36 Q58 30 64 36 Q70 30 76 36 Q82 30 88 36" fill="#fff" {W(2)}/>'
  f'<rect x="24" y="50" width="76" height="44" rx="8" fill="#9DD6F5" {s()}/><path d="M100 60 H114" {W(5)}/>'
  f'<circle cx="38" cy="104" r="10" fill="#3B3355"/><circle cx="86" cy="104" r="10" fill="#3B3355"/><circle cx="38" cy="104" r="4" fill="#fff"/><circle cx="86" cy="104" r="4" fill="#fff"/>'
  + f(62, 70, d=10, k=0.7)),
 # 33 поильник-непроливайка
 ("green", "поильник-непроливайка", f'<path d="M54 28 Q56 12 64 12 Q72 12 74 28Z" fill="#FFD25E" {s()}/>'
  f'<rect x="40" y="26" width="48" height="14" rx="5" fill="#FF8FB8" {s()}/>'
  f'<path d="M42 40 H86 L82 108 Q82 114 76 114 H52 Q46 114 46 108Z" fill="#F4F8FF" {s()}/>'
  f'<path d="M44 68 H84 L82 108 Q82 114 76 114 H52 Q46 114 46 108Z" fill="#FFB86B" opacity=".8"/>'
  f'<path d="M42 56 Q24 56 26 72 Q28 84 44 82 M86 56 Q104 56 102 72 Q100 84 84 82" fill="none" stroke="#FF8FB8" stroke-width="6" stroke-linecap="round"/>'
  + f(64, 60, d=8, k=0.6)),
 # 34 баночка детского пюре
 ("pink", "баночка детского пюре", f'<rect x="34" y="22" width="60" height="16" rx="5" fill="#7CD26E" {s()}/>'
  f'<path d="M36 38 H92 V104 Q92 114 82 114 H46 Q36 114 36 104Z" fill="#FFB86B" {s()}/>'
  f'<rect x="40" y="56" width="48" height="34" rx="6" fill="#fff" {W(2.4)}/><circle cx="56" cy="73" r="7" fill="#FF8A5B" {W(2)}/><circle cx="74" cy="73" r="7" fill="#9BE06A" {W(2)}/>'
  f'<path d="M100 18 L84 52" {W(5)}/><ellipse cx="102" cy="14" rx="5" ry="8" fill="#C9D3E0" {W(2)} transform="rotate(25 102 14)"/>'
  + f(64, 100, d=8, k=0.5, blush=False)),
 # 35 вертел шаурмы
 ("yellow", "вертел для шаурмы", f'<path d="M64 6 V122" {W(5)}/><path d="M64 6 V122" stroke="#C9D3E0" stroke-width="2"/>'
  f'<path d="M44 20 H84 L80 104 Q64 110 48 104Z" fill="#C0783A" {s()}/>'
  f'<path d="M48 40 Q64 46 82 40 M47 62 Q64 68 81 62 M46 84 Q64 90 80 84" fill="none" stroke="#8A5A3A" stroke-width="3"/>'
  f'<path d="M96 30 Q104 54 96 78 M106 38 Q112 54 106 70" fill="none" stroke="#FF8A5B" stroke-width="4" stroke-linecap="round"/>'
  + f(64, 52, d=8, k=0.6)),
 # 36 кофейное зерно
 ("orange", "кофейное зерно", f'<ellipse cx="64" cy="64" rx="34" ry="44" fill="#7A4A2A" {s()} transform="rotate(-20 64 64)"/>'
  f'<path d="M52 26 Q72 64 76 102" fill="none" stroke="#3B3355" stroke-width="4" stroke-linecap="round"/>'
  f'<path d="M50 34 Q44 40 46 48" fill="none" stroke="#fff" stroke-width="3" opacity=".5"/>'
  + f(60, 66, d=9, k=0.7).replace(O, "#fff") + steam(96, 104)),
]

DATA = json.load(open(os.path.join(here, "cafes_1106b_data.json")))
assert len(L) == len(DATA), (len(L), len(DATA))
ICONS = {d["id"]: x for d, x in zip(DATA, L)}

if __name__ == "__main__":
    subj = [x[1] for x in L]
    assert len(subj) == len(set(subj))
    for pid, (bg, sj, body) in ICONS.items():
        open(os.path.join(src, pid + ".svg"), "w").write(svg(bg, body))
    with open(os.path.join(src, "subjects.txt"), "a") as fh:
        for pid, (bg, sj, body) in ICONS.items():
            fh.write(f"{pid} — {sj}\n")
    print(len(ICONS))
