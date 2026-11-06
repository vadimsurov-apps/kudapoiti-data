"""Иконки робота cafes, 2026-11-06 (день): 66 новых сюжетов «еда, посуда, кухня, сладости»
(сверено со всеми листами icons-catalog и icons-src/subjects.txt). Порядок = порядок мест в tools/cafes_1106c_data.json."""
import json, os
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=8, k=0.7, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); src = os.path.join(here, "..", "icons-src")
steam = lambda *xs: "".join(f'<path d="M{x} 30 Q{x+4} 22 {x} 14" fill="none" stroke="#fff" stroke-width="3" opacity=".9"/>' for x in xs)
dots = lambda pts, c, r=2.2: "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x, y in pts)
leaf = lambda x, y, rot, c="#7CD26E", l=14: (f'<path d="M{x} {y} q{l*.5} {-l*.55} {l} 0 q{-l*.5} {l*.55} {-l} 0Z" fill="{c}" '
                                              f'{W(2.2)} transform="rotate({rot} {x} {y})"/>')
white = lambda fc: fc.replace(O, "#fff")

L = [
 # 1 артишок
 ("green", "артишок",
  f'<path d="M64 98 V118" {W(6)}/><path d="M64 98 V118" stroke="#7CB85E" stroke-width="3"/>'
  + "".join(f'<path d="M64 {y} Q{64-w} {y-4} {64-w*0.8} {y-h} Q64 {y-h+6} {64+w*0.8} {y-h} Q{64+w} {y-4} 64 {y}Z" fill="{c}" {W(2.6)}/>'
            for y, w, h, c in [(102, 40, 34, "#5FAE6A"), (90, 34, 34, "#78C27A"), (76, 26, 30, "#93D58B"), (60, 17, 26, "#B5E6A2")])
  + "".join(f'<path d="M{x} {y} Q{x+dx} {y-18} {x+dx*1.6} {y-30}" fill="#6FBF73" {W(2.6)}/>' for x, y, dx in [(40, 96, -10), (88, 96, 10)])
  + f(64, 80, d=8, k=0.6)),
 # 2 подставка для ножей
 ("teal", "подставка для ножей",
  f'<path d="M50 30 L60 30 L56 60 Z" fill="#E7EEF5" {W(2.4)}/><path d="M66 22 L76 22 L72 60Z" fill="#E7EEF5" {W(2.4)}/><path d="M82 32 L90 34 L82 60Z" fill="#E7EEF5" {W(2.4)}/>'
  f'<rect x="48" y="14" width="10" height="20" rx="3" fill="#3B3355"/><rect x="65" y="8" width="11" height="18" rx="3" fill="#3B3355"/><rect x="81" y="18" width="10" height="18" rx="3" fill="#3B3355" transform="rotate(8 86 27)"/>'
  f'<path d="M30 58 L92 52 L104 112 H40Z" fill="#C98A55" {s()}/><path d="M38 72 L96 66" stroke="#A86E3E" stroke-width="3"/>'
  + f(70, 88, d=9, k=0.75)),
 # 3 шумовка
 ("yellow", "шумовка",
  f'<path d="M84 72 L112 14" {W(7)}/><path d="M84 72 L112 14" stroke="#C9D3E0" stroke-width="3.5"/>'
  f'<circle cx="58" cy="84" r="32" fill="#E7EEF5" {s()}/>'
  + dots([(x, y) for x in range(38, 80, 10) for y in range(64, 106, 10) if (x-58)**2 + (y-84)**2 < 560], "#9AA6B8", 2.6)
  + f(58, 84, d=9, k=0.7)),
 # 4 грейпфрут
 ("orange", "грейпфрут в разрезе",
  f'<circle cx="64" cy="70" r="44" fill="#FFD9B0" {s()}/><circle cx="64" cy="70" r="38" fill="#FF8C8C" stroke="#fff" stroke-width="3"/>'
  + "".join(f'<path d="M64 70 L{64+36*__import__("math").cos(a/57.3):.1f} {70+36*__import__("math").sin(a/57.3):.1f}" stroke="#FFE4D6" stroke-width="2.6"/>' for a in range(0, 360, 36))
  + f'<circle cx="64" cy="70" r="7" fill="#FFE4D6"/>' + f(64, 64, d=11, k=0.75) + sparkle(104, 24, 7)),
 # 5 веточка смородины
 ("pink", "веточка красной смородины",
  f'<path d="M30 20 Q60 26 70 60 Q76 84 74 108" fill="none" stroke="#6B8E3A" stroke-width="4" stroke-linecap="round"/>' + leaf(30, 22, -20, "#7CD26E", 26)
  + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#E8344F" {W(2.4)}/><circle cx="{x-3}" cy="{y-3}" r="2.4" fill="#fff" opacity=".8"/>'
            for x, y, r in [(56, 50, 9), (74, 56, 10), (60, 72, 11), (82, 78, 11), (66, 96, 12), (88, 102, 10)])
  + f(66, 96, d=5, k=0.45, blush=False)),
 # 6 кешью
 ("yellow", "орех кешью с плодом",
  f'<path d="M40 16 Q36 4 46 6" fill="none" {W(3)}/>'
  f'<path d="M36 22 Q64 14 84 26 Q92 52 74 70 Q48 76 34 58 Q26 38 36 22Z" fill="#FF9B4A" {s()}/>'
  f'<path d="M44 70 Q30 92 46 108 Q60 116 68 104 Q60 100 58 90 Q62 78 72 72Z" fill="#E9C48A" {s()}/>'
  + f(58, 44, d=9, k=0.7) + sparkle(102, 76, 7)),
 # 7 брауни
 ("purple", "брауни",
  f'<path d="M20 58 L64 40 L108 58 L64 76Z" fill="#8A5634" {s()}/><path d="M20 58 V90 L64 108 V76Z" fill="#5E3820" {s()}/><path d="M108 58 V90 L64 108 V76Z" fill="#6E4428" {s()}/>'
  f'<path d="M36 56 L50 52 L56 58 M70 50 L82 54 M60 66 L74 62" fill="none" stroke="#B9835A" stroke-width="2.6" stroke-linecap="round"/>'
  + dots([(44, 62), (88, 60), (66, 54)], "#3B2A1F", 2.4) + f(64, 88, d=9, k=0.65).replace(O, "#fff")),
 # 8 козинаки
 ("orange", "козинаки (гозинаки)",
  "".join(f'<path d="M{x} {y} l18 -10 l18 10 l-18 10Z" fill="#E7B55E" {W(2.6)}/>' for x, y in [(28, 60), (64, 60), (46, 82)])
  + dots([(40, 58), (48, 62), (52, 56), (76, 58), (84, 62), (88, 56), (58, 80), (66, 84), (70, 78)], "#8A5634", 2.6)
  + f'<path d="M20 98 Q64 112 108 98" fill="none" stroke="#fff" stroke-width="4" opacity=".7"/>' + f(64, 40, d=9, k=0.7) + sparkle(100, 28, 6)),
 # 9 шейкер
 ("blue", "шейкер для коктейлей",
  f'<rect x="54" y="10" width="20" height="12" rx="4" fill="#C9D3E0" {W(2.6)}/><path d="M48 22 H80 L84 40 H44Z" fill="#E7EEF5" {s()}/>'
  f'<path d="M42 40 H86 L80 114 H48Z" fill="#E7EEF5" {s()}/><path d="M46 56 H82 L78 100 H50Z" fill="#FF9EC3" opacity=".7"/>'
  f'<path d="M98 36 l8 -4 M100 50 h10 M96 24 l6 -8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' + f(64, 76, d=9, k=0.7)),
 # 10 маслобойка
 ("green", "маслобойка",
  f'<path d="M64 6 V40" {W(6)}/><path d="M64 6 V40" stroke="#C98A55" stroke-width="3"/><circle cx="64" cy="8" r="5" fill="#C98A55" {W(2.4)}/>'
  f'<path d="M40 38 H88 L92 112 H36Z" fill="#E1A86A" {s()}/><path d="M38 56 H90 M37 92 H91" stroke="#8A5634" stroke-width="4"/>'
  f'<ellipse cx="64" cy="38" rx="24" ry="5" fill="#FFF3C4" {W(2.4)}/>' + f(64, 74, d=9, k=0.7)),
 # 11 консервный нож
 ("sky", "консервный нож",
  f'<path d="M34 104 L66 56" {W(12)}/><path d="M34 104 L66 56" stroke="#FF8A5B" stroke-width="8"/>'
  f'<path d="M62 36 H96 Q104 36 104 46 V60 Q104 70 94 70 H70 Q60 70 60 60 Z" fill="#C9D3E0" {s()}/>'
  f'<circle cx="94" cy="80" r="10" fill="#E7EEF5" {W(2.6)}/>' + "".join(f'<path d="M{94+10*__import__("math").cos(a/57.3):.1f} {80+10*__import__("math").sin(a/57.3):.1f} l{3*__import__("math").cos(a/57.3):.1f} {3*__import__("math").sin(a/57.3):.1f}" {W(2.4)}/>' for a in range(0, 360, 45))
  + f(82, 52, d=7, k=0.55, blush=False)),
 # 12 кольраби
 ("teal", "кольраби",
  "".join(f'<path d="M{x} 54 Q{x+dx*0.3} 30 {x+dx} 14" fill="none" stroke="#6BA84F" stroke-width="3.4" stroke-linecap="round"/>' for x, dx in [(54, -14), (64, 0), (74, 14)])
  + leaf(36, 14, 200, "#7CD26E", 18) + leaf(64, 10, 270, "#7CD26E", 16) + leaf(92, 14, -20, "#7CD26E", 18)
  + f'<circle cx="64" cy="80" r="34" fill="#C7A8F0" {s()}/><path d="M64 114 V122" {W(4)}/>'
  f'<path d="M40 70 q-8 -4 -10 -12 M88 70 q8 -4 10 -12" fill="none" stroke="#6BA84F" stroke-width="3"/>' + f(64, 82, d=10, k=0.75)),
 # 13 пуровер
 ("orange", "кофейная воронка-пуровер",
  f'<path d="M30 30 H98 L76 70 H52Z" fill="#fff" {s()}/><path d="M38 34 H90 L74 62 H54Z" fill="#E9D3B4"/>'
  f'<path d="M98 36 Q112 38 108 50 Q104 58 92 54" fill="none" {W(4)}/>'
  f'<path d="M64 72 V82" stroke="#7A4A2A" stroke-width="3" stroke-dasharray="3 3"/>'
  f'<path d="M40 82 H88 V104 Q88 116 76 116 H52 Q40 116 40 104Z" fill="#CDEFFF" {s()}/><path d="M42 96 H86 V104 Q86 114 76 114 H52 Q42 114 42 104Z" fill="#8A5634"/>'
  + f(64, 48, d=8, k=0.6)),
 # 14 сулугуни-косичка
 ("night", "сыр сулугуни косичкой",
  "".join(f'<path d="M{30+i*8} {28+i*14} Q{64} {14+i*14} {98-i*8} {36+i*14} Q{64} {48+i*14} {30+i*8} {28+i*14}Z" fill="#FFF3D0" {W(2.6)}/>' for i in range(5))
  + f'<path d="M62 92 Q58 108 66 116 M66 92 Q74 106 70 116" fill="none" stroke="#FFF3D0" stroke-width="7" stroke-linecap="round"/>'
  f'<path d="M62 92 Q58 108 66 116 M66 92 Q74 106 70 116" fill="none" {W(1.6)}/>' + f(64, 58, d=9, k=0.65) + sparkle(106, 24, 7)),
 # 15 гриссини
 ("yellow", "хлебные палочки гриссини в стакане",
  "".join(f'<path d="M{x} 70 L{x+dx} 14" stroke="#3B3355" stroke-width="9" stroke-linecap="round"/><path d="M{x} 70 L{x+dx} 14" stroke="#F0C27A" stroke-width="5.5" stroke-linecap="round"/>'
          + dots([(x+dx*0.3, 54), (x+dx*0.6, 38), (x+dx*0.85, 24)], "#fff", 1.4) for x, dx in [(50, -12), (60, -2), (70, 6), (78, 18)])
  + f'<path d="M38 62 H90 L84 114 H44Z" fill="#CDEFFF" opacity=".9" {s()}/>' + f(64, 88, d=9, k=0.7)),
 # 16 рёбрышки
 ("orange", "рёбрышки барбекю",
  f'<ellipse cx="64" cy="96" rx="52" ry="12" fill="#fff" {s()}/>'
  f'<path d="M20 78 Q24 44 64 42 Q104 44 108 78 Q64 92 20 78Z" fill="#B5472E" {s()}/>'
  + "".join(f'<path d="M{x} 48 L{x-2} 34" stroke="#3B3355" stroke-width="8" stroke-linecap="round"/><path d="M{x} 48 L{x-2} 34" stroke="#FFF3E0" stroke-width="4.5" stroke-linecap="round"/>' for x in (38, 54, 70, 86))
  + f'<path d="M30 70 Q64 62 98 70" fill="none" stroke="#7A2A1A" stroke-width="3"/>' + f(64, 70, d=9, k=0.65).replace(O, "#fff")),
 # 17 чебурек
 ("pink", "чебурек",
  f'<path d="M14 92 Q14 26 64 26 Q114 26 114 92Z" fill="#F2C06E" {s()}/>'
  + "".join(f'<path d="M{18+i*10} 88 q5 8 10 0" fill="none" {W(2.6)}/>' for i in range(10))
  + dots([(40, 52), (84, 48), (56, 40), (96, 70), (30, 72)], "#FFE3A8", 3.4) + f(64, 64, d=10, k=0.75) + steam(44, 84)),
 # 18 кеци
 ("orange", "кеци (глиняная сковорода)",
  f'<path d="M14 66 H114 Q110 104 64 106 Q18 104 14 66Z" fill="#C2603A" {s()}/><ellipse cx="64" cy="66" rx="50" ry="12" fill="#E07A4E" {s()}/>'
  f'<ellipse cx="64" cy="64" rx="40" ry="8" fill="#FFE07A"/>' + dots([(46, 62), (60, 66), (78, 62), (88, 66)], "#7CD26E", 2.6)
  + f'<path d="M108 74 H122" {W(8)}/><path d="M6 74 H20" {W(8)}/>' + f(64, 86, d=10, k=0.75).replace(O, "#fff") + steam(50, 76)),
 # 19 бадьян
 ("night", "звёздочка бадьяна",
  "".join(f'<path d="M64 64 Q{64+12*__import__("math").cos((a-20)/57.3):.1f} {64+12*__import__("math").sin((a-20)/57.3):.1f} {64+44*__import__("math").cos(a/57.3):.1f} {64+44*__import__("math").sin(a/57.3):.1f} Q{64+12*__import__("math").cos((a+20)/57.3):.1f} {64+12*__import__("math").sin((a+20)/57.3):.1f} 64 64Z" fill="#B0603A" {W(2.6)}/>'
          f'<ellipse cx="{64+28*__import__("math").cos(a/57.3):.1f}" cy="{64+28*__import__("math").sin(a/57.3):.1f}" rx="4" ry="2.6" fill="#E9B56A" transform="rotate({a} {64+28*__import__("math").cos(a/57.3):.1f} {64+28*__import__("math").sin(a/57.3):.1f})"/>'
          for a in range(-90, 270, 45))
  + f'<circle cx="64" cy="64" r="14" fill="#8A4A2A" {W(2.6)}/>' + f(64, 63, d=5, k=0.45, blush=False).replace(O, "#fff") + sparkle(104, 22, 6) + sparkle(22, 100, 5)),
 # 20 корн-дог
 ("sky", "корн-дог",
  f'<path d="M64 92 V124" {W(6)}/><path d="M64 92 V124" stroke="#E0B07A" stroke-width="3"/>'
  f'<rect x="40" y="10" width="48" height="88" rx="24" fill="#E8A23E" {s()}/><path d="M50 14 Q64 6 78 14" fill="none" stroke="#C0783A" stroke-width="3"/>'
  f'<path d="M48 40 Q58 46 50 54 Q42 62 54 66 Q64 70 58 80" fill="none" stroke="#E8344F" stroke-width="4" stroke-linecap="round"/>'
  f'<path d="M72 30 Q82 38 74 48 Q66 58 78 62" fill="none" stroke="#FFD93D" stroke-width="4" stroke-linecap="round"/>' + f(64, 70, d=9, k=0.7)),
 # 21 картофель-спиралька
 ("green", "картофель-спиралька на палочке",
  f'<path d="M64 8 V124" {W(5)}/><path d="M64 8 V124" stroke="#E0B07A" stroke-width="2.4"/>'
  + "".join(f'<ellipse cx="64" cy="{y}" rx="{w}" ry="7" fill="#FFC94D" {W(2.6)} transform="rotate({r} 64 {y})"/>' for y, w, r in [(22, 20, -10), (38, 28, 10), (54, 32, -10), (70, 32, 10), (86, 28, -10), (102, 20, 10)])
  + dots([(50, 38), (80, 54), (46, 72), (82, 88)], "#E8654F", 1.8) + f(64, 60, d=8, k=0.6)),
 # 22 супница
 ("teal", "супница",
  f'<circle cx="64" cy="24" r="7" fill="#7FB8E8" {W(2.6)}/><path d="M28 50 Q30 30 64 30 Q98 30 100 50Z" fill="#fff" {s()}/>'
  f'<path d="M20 50 H108 Q106 96 64 98 Q22 96 20 50Z" fill="#fff" {s()}/><path d="M24 62 Q64 72 104 62" fill="none" stroke="#5C8FD6" stroke-width="4"/>'
  f'<path d="M20 58 Q6 60 10 72 Q14 78 24 72 M108 58 Q122 60 118 72 Q114 78 104 72" fill="none" {W(3.6)}/>'
  f'<path d="M44 98 L40 110 H88 L84 98" fill="#fff" {s()}/>' + f(64, 80, d=9, k=0.7)),
 # 23 тирамису
 ("orange", "тирамису",
  f'<path d="M22 44 H106 V100 Q106 108 98 108 H30 Q22 108 22 100Z" fill="#FFF5E6" {s()}/>'
  f'<rect x="24" y="58" width="80" height="12" fill="#B07A4A"/><rect x="24" y="84" width="80" height="12" fill="#B07A4A"/>'
  f'<path d="M22 44 H106 V50 H22Z" fill="#7A4A2A"/>' + dots([(36, 46), (54, 47), (74, 46), (92, 47), (46, 49), (84, 49)], "#4A2A1A", 1.6)
  + f'<path d="M84 36 Q90 22 104 24 Q98 30 98 40Z" fill="#7CD26E" {W(2.2)}/>' + f(64, 76, d=10, k=0.7)),
 # 24 финики
 ("purple", "финики на веточке",
  f'<path d="M64 8 Q60 30 64 44 M64 30 Q46 44 40 60 M64 30 Q82 44 88 60 M64 44 V64" fill="none" stroke="#E0A86A" stroke-width="3.4" stroke-linecap="round"/>'
  + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="15" fill="#9B4A2A" {W(2.4)} transform="rotate({r} {x} {y})"/><path d="M{x-3} {y-8} q-2 6 0 10" stroke="#fff" stroke-width="2" opacity=".5" fill="none"/>'
            for x, y, r in [(36, 74, 15), (54, 82, 5), (74, 82, -5), (92, 74, -15), (64, 98, 0), (44, 100, 10), (84, 100, -10)])
  + f(64, 98, d=4, k=0.4, blush=False).replace(O, "#fff")),
 # 25 патиссон
 ("yellow", "патиссон",
  f'<path d="M64 30 V42" {W(6)}/><path d="M64 30 V42" stroke="#7CB85E" stroke-width="3"/>'
  + "".join(f'<path d="M64 76 L{64+46*__import__("math").cos(a/57.3):.1f} {76+30*__import__("math").sin(a/57.3):.1f}" />' for a in range(0, 1))
  + f'<path d="M64 42 Q78 38 82 48 Q100 42 104 56 Q120 62 110 76 Q122 92 104 98 Q100 112 82 106 Q72 116 64 110 Q56 116 46 106 Q28 112 24 98 Q6 92 18 76 Q8 62 24 56 Q28 42 46 48 Q50 38 64 42Z" fill="#F3F0C8" {s()}/>'
  f'<path d="M64 48 Q60 76 64 108 M46 50 Q38 78 46 104 M82 50 Q90 78 82 104" fill="none" stroke="#D6CF8E" stroke-width="2.6"/>' + f(64, 78, d=10, k=0.75)),
 # 26 капучинатор
 ("pink", "капучинатор (вспениватель молока)",
  f'<rect x="56" y="8" width="16" height="40" rx="7" fill="#FF8FB8" {s()}/><circle cx="64" cy="22" r="3" fill="#fff"/>'
  f'<path d="M64 48 V88" {W(4)}/><circle cx="64" cy="92" r="7" fill="none" {W(3)}/>'
  f'<path d="M30 70 H98 V108 Q98 118 88 118 H40 Q30 118 30 108Z" fill="#fff" opacity=".9" {s()}/>'
  f'<path d="M32 78 Q40 70 48 78 Q56 70 64 78 Q72 70 80 78 Q88 70 96 78 V86 H32Z" fill="#FFF3DD"/>' + f(64, 102, d=10, k=0.7) + sparkle(100, 30, 6)),
 # 27 бидон для молока
 ("sky", "бидон для молока",
  f'<rect x="48" y="12" width="32" height="10" rx="4" fill="#9FC7E8" {s()}/><path d="M50 22 H78 V34 Q96 40 96 58 V108 Q96 116 88 116 H40 Q32 116 32 108 V58 Q32 40 50 34Z" fill="#E7EEF5" {s()}/>'
  f'<path d="M32 62 H96" stroke="#9FC7E8" stroke-width="5"/><path d="M32 100 H96" stroke="#9FC7E8" stroke-width="5"/>'
  f'<path d="M30 46 Q16 46 18 60 M98 46 Q112 46 110 60" fill="none" {W(3.6)}/>' + f(64, 82, d=10, k=0.75)),
 # 28 миндаль
 ("green", "миндаль",
  f'<path d="M64 16 Q100 46 92 82 Q84 110 64 112 Q44 110 36 82 Q28 46 64 16Z" fill="#D49A62" {s()}/>'
  + dots([(54, 44), (72, 52), (50, 68), (78, 74), (60, 92), (70, 36), (46, 86), (82, 92)], "#B47A48", 2.2)
  + f'<path d="M58 28 Q48 42 46 58" fill="none" stroke="#fff" stroke-width="3" opacity=".5"/>' + f(64, 74, d=10, k=0.75) + sparkle(104, 28, 7)),
 # 29 топорик для мяса
 ("orange", "топорик для мяса",
  f'<path d="M14 34 H82 V88 Q82 94 76 94 H22 Q14 94 14 86Z" fill="#E7EEF5" {s()}/><circle cx="72" cy="44" r="5" fill="#fff" {W(2.4)}/>'
  f'<path d="M18 88 H78" stroke="#fff" stroke-width="3"/><rect x="80" y="48" width="38" height="16" rx="7" fill="#3B3355"/>'
  f'<circle cx="94" cy="56" r="2.4" fill="#C9D3E0"/><circle cx="106" cy="56" r="2.4" fill="#C9D3E0"/>' + f(46, 62, d=9, k=0.7)),
 # 30 сэндвич с мороженым
 ("blue", "сэндвич с мороженым",
  f'<rect x="20" y="30" width="88" height="22" rx="8" fill="#5E3820" {s()}/><rect x="22" y="52" width="84" height="26" fill="#FFF6E6" {W(2.6)}/>'
  f'<rect x="20" y="78" width="88" height="22" rx="8" fill="#5E3820" {s()}/>'
  + dots([(34, 40), (50, 42), (66, 40), (82, 42), (96, 40), (34, 88), (50, 90), (66, 88), (82, 90), (96, 88)], "#3B2A1F", 2.2)
  + f(64, 64, d=10, k=0.65) + sparkle(104, 18, 6)),
 # 31 ложка для мороженого
 ("pink", "ложка для мороженого",
  f'<path d="M44 108 L72 70" {W(12)}/><path d="M44 108 L72 70" stroke="#FFC94D" stroke-width="8"/>'
  f'<path d="M70 72 L78 62" {W(4)}/><path d="M80 66 Q60 56 64 38 Q70 20 92 22 Q112 28 108 50 Q104 66 80 66Z" fill="#C9D3E0" {s()}/>'
  f'<circle cx="86" cy="42" r="18" fill="#FFB3CF" {W(2.6)}/>' + f(86, 42, d=6, k=0.5) + sparkle(30, 30, 7)),
 # 32 трдельник
 ("yellow", "трдельник",
  f'<path d="M36 22 H92 L86 110 H42Z" fill="#E7A24E" {s()}/>'
  + "".join(f'<path d="M{37+i} {30+i*14} Q64 {22+i*14} {91-i} {36+i*14}" fill="none" stroke="#B9702A" stroke-width="3"/>' for i in range(6))
  + dots([(48, 40), (62, 34), (78, 44), (52, 70), (72, 66), (58, 96), (76, 92)], "#fff", 1.8)
  + f'<ellipse cx="64" cy="22" rx="28" ry="7" fill="#FFF6E6" {W(2.6)}/>' + f(64, 60, d=9, k=0.65)),
 # 33 халва
 ("teal", "халва",
  f'<path d="M14 98 H114" {W(4)}/><path d="M22 60 L90 46 L110 64 L42 80Z" fill="#E6CFA5" {s()}/><path d="M22 60 V84 L42 104 V80Z" fill="#CDB081" {s()}/><path d="M42 80 L110 64 V88 L42 104Z" fill="#D9BE90" {s()}/>'
  + "".join(f'<path d="M{x} {y} l6 -1" stroke="#B89A6A" stroke-width="2.4" stroke-linecap="round"/>' for x, y in [(50, 88), (64, 86), (78, 82), (92, 78), (56, 94), (84, 88)])
  + dots([(40, 62), (60, 58), (80, 54)], "#9A7B4A", 2) + f(76, 84, d=8, k=0.6)),
 # 34 форма для маффинов
 ("sky", "форма для маффинов",
  f'<rect x="12" y="44" width="104" height="60" rx="10" fill="#C9D3E0" {s()}/>'
  + "".join(f'<ellipse cx="{x}" cy="{y}" rx="14" ry="11" fill="#7F8CA3" {W(2.4)}/>' for x, y in [(34, 62), (64, 62), (94, 62), (34, 88), (64, 88), (94, 88)])
  + "".join(f'<path d="M{x-12} {y} Q{x-12} {y-14} {x} {y-14} Q{x+12} {y-14} {x+12} {y}Z" fill="#E8A23E" {W(2.4)}/>' for x, y in [(34, 62), (94, 88)])
  + f(64, 74, d=10, k=0.7)),
 # 35 бундт
 ("purple", "форма для кекса (бундт)",
  f'<path d="M14 84 Q14 50 64 48 Q114 50 114 84 Q114 100 64 102 Q14 100 14 84Z" fill="#E07A4E" {s()}/>'
  + "".join(f'<path d="M{x} 54 Q{x+3} 76 {x} 98" fill="none" stroke="#B5552E" stroke-width="2.6"/>' for x in (30, 46, 64, 82, 98))
  + f'<ellipse cx="64" cy="54" rx="14" ry="5" fill="#8A3A20" {W(2.4)}/><path d="M50 52 V40 Q50 34 64 34 Q78 34 78 40 V52" fill="#C9D3E0" {W(2.4)}/>'
  + f(64, 78, d=10, k=0.7).replace(O, "#fff")),
 # 36 бенто-торт
 ("pink", "бенто-торт в коробочке",
  f'<path d="M18 74 H110 V108 Q110 114 104 114 H24 Q18 114 18 108Z" fill="#E7F8FF" {s()}/><path d="M18 74 L28 20 H100 L110 74" fill="#E7F8FF" opacity=".6" {s()}/>'
  f'<path d="M34 64 Q34 46 64 46 Q94 46 94 64 V96 H34Z" fill="#FFC2DA" {s()}/>'
  f'<path d="M34 60 Q40 66 46 60 Q52 66 58 60 Q64 66 70 60 Q76 66 82 60 Q88 66 94 60" fill="none" stroke="#fff" stroke-width="3.4"/>'
  f'<circle cx="64" cy="44" r="5" fill="#E8344F" {W(2)}/>' + f(64, 78, d=9, k=0.7)),
 # 37 маракуйя
 ("night", "маракуйя",
  f'<circle cx="64" cy="66" r="44" fill="#6B3A7A" {s()}/><circle cx="64" cy="66" r="34" fill="#FFD25E" {W(2.6)}/>'
  + dots([(50, 54), (62, 48), (76, 54), (82, 68), (46, 72), (58, 84), (74, 82), (68, 64), (54, 64)], "#3B2A1F", 3)
  + f'<path d="M64 22 Q60 12 68 8" fill="none" stroke="#7CD26E" stroke-width="3.6" stroke-linecap="round"/>' + f(64, 70, d=9, k=0.6) + sparkle(108, 28, 6)),
 # 38 мерные ложки
 ("teal", "мерные ложки",
  f'<circle cx="104" cy="24" r="8" fill="none" {W(4)}/>'
  + "".join(f'<path d="M104 26 L{x+10} {y-6}" {W(5)}/><ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*0.8}" fill="{c}" {W(2.6)}/>'
            for x, y, r, c in [(40, 96, 18, "#FF8FB8"), (72, 92, 14, "#FFD25E"), (36, 60, 12, "#7FB8E8"), (66, 54, 10, "#9BE06A")])
  + f(40, 96, d=6, k=0.5)),
 # 39 молоток для мяса
 ("yellow", "молоток для отбивания мяса",
  f'<path d="M52 66 L28 118" {W(10)}/><path d="M52 66 L28 118" stroke="#C98A55" stroke-width="6"/>'
  f'<rect x="34" y="28" width="62" height="34" rx="6" fill="#C9D3E0" {s()} transform="rotate(-24 64 45)"/>'
  + "".join(f'<path d="M{x} {y} l6 -3 l-2 7Z" fill="#7F8CA3" transform="rotate(-24 64 45)"/>' for x, y in [(36, 36), (36, 46), (36, 56)])
  + f'<path d="M96 30 L104 26 M98 40 L108 38" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' + f(66, 44, d=8, k=0.6)),
 # 40 спиралайзер
 ("green", "овощерезка-спиралайзер",
  f'<path d="M24 40 Q24 24 46 24 H82 Q104 24 104 40 L96 74 H32Z" fill="#FFB86B" {s()}/><circle cx="64" cy="44" r="12" fill="#fff" {W(2.6)}/>'
  f'<path d="M64 74 Q80 82 64 88 Q48 94 64 100 Q80 106 64 112 Q48 118 64 124" fill="none" stroke="#7CD26E" stroke-width="6" stroke-linecap="round"/>'
  f'<path d="M64 74 Q80 82 64 88 Q48 94 64 100 Q80 106 64 112" fill="none" stroke="#3B3355" stroke-width="1.6"/>' + f(64, 58, d=14, k=0.6, mouth=False)
  + f'<path d="M58 66 Q64 70 70 66" fill="none" {W(2.4)}/>'),
 # 41 форма для льда
 ("blue", "форма для льда",
  f'<rect x="16" y="54" width="96" height="44" rx="10" fill="#7FB8E8" {s()}/>'
  + "".join(f'<rect x="{x}" y="{y}" width="20" height="14" rx="4" fill="#E7F8FF" {W(2.2)}/>' for x in (24, 54, 84) for y in (60, 80))
  + "".join(f'<rect x="{x}" y="{y}" width="18" height="18" rx="5" fill="#E7F8FF" {W(2.4)} transform="rotate({r} {x+9} {y+9})"/>' for x, y, r in [(36, 20, 15), (76, 14, -10)])
  + f(64, 40, d=7, k=0.55, blush=False) + sparkle(104, 40, 6) + sparkle(20, 34, 5)),
 # 42 рамбутан
 ("pink", "рамбутан",
  "".join(f'<path d="M{64+38*__import__("math").cos(a/57.3):.1f} {70+38*__import__("math").sin(a/57.3):.1f} q{8*__import__("math").cos((a+40)/57.3):.1f} {8*__import__("math").sin((a+40)/57.3):.1f} {14*__import__("math").cos(a/57.3):.1f} {14*__import__("math").sin(a/57.3):.1f}" fill="none" stroke="#3E8A3A" stroke-width="3.4" stroke-linecap="round"/>' for a in range(0, 360, 20))
  + f'<circle cx="64" cy="70" r="38" fill="#E8344F" {s()}/><path d="M74 46 Q92 50 94 74 Q80 90 64 84 Q60 60 74 46Z" fill="#FFF6E6" {W(2.4)}/>'
  + f(54, 74, d=8, k=0.6).replace(O, "#fff")),
 # 43 миска с тестом
 ("orange", "миска с поднимающимся тестом",
  f'<path d="M24 64 Q20 26 64 26 Q108 26 104 64Z" fill="#FFF3DD" {s()}/>'
  f'<path d="M14 62 H114 Q110 108 64 110 Q18 108 14 62Z" fill="#7FB8E8" {s()}/><path d="M22 74 Q64 84 106 74" fill="none" stroke="#fff" stroke-width="3"/>'
  + f(64, 46, d=9, k=0.65) + f'<path d="M30 20 q4 -6 8 0 M88 16 q4 -6 8 0" fill="none" stroke="#fff" stroke-width="3"/>'),
 # 44 мюсли-батончик
 ("purple", "мюсли-батончик",
  f'<rect x="12" y="44" width="104" height="42" rx="10" fill="#D9A55E" {s()} transform="rotate(-12 64 65)"/>'
  + dots([(26, 64), (40, 56), (54, 70), (70, 52), (84, 66), (98, 50), (34, 76), (90, 76), (62, 62), (106, 60)], "#8A5634", 3)
  + dots([(46, 66), (78, 58), (94, 62)], "#E8344F", 2.8) + f(62, 66, d=9, k=0.65) + sparkle(100, 24, 7)),
 # 45 банана-сплит
 ("yellow", "банана-сплит",
  f'<path d="M10 80 H118 Q112 104 64 106 Q16 104 10 80Z" fill="#CDEFFF" {s()}/>'
  f'<path d="M12 78 Q14 60 34 62 L40 74Z" fill="#FFE07A" {W(2.4)}/><path d="M116 78 Q114 60 94 62 L88 74Z" fill="#FFE07A" {W(2.4)}/>'
  + "".join(f'<circle cx="{x}" cy="64" r="15" fill="{c}" {W(2.6)}/>' for x, c in [(44, "#FFB3CF"), (64, "#FFF6E6"), (84, "#8A5634")])
  + f'<circle cx="64" cy="44" r="6" fill="#E8344F" {W(2.2)}/>' + f(64, 66, d=6, k=0.5, blush=False)),
 # 46 вафельная трубочка
 ("orange", "вафельная трубочка с кремом",
  f'<path d="M22 96 L88 30 Q98 24 104 30 Q110 36 104 46 L38 112Z" fill="#E8B060" {s()}/>'
  + "".join(f'<path d="M{30+i*10} {104-i*10} l14 14" stroke="#B9702A" stroke-width="2.4" transform="translate(-6 -18)"/>' for i in range(7))
  + f'<path d="M98 34 Q114 18 108 8 Q120 14 116 28 Q112 40 100 40Z" fill="#FFF6E6" {W(2.6)}/>' + f(62, 72, d=8, k=0.6)),
 # 47 тайяки
 ("blue", "тайяки (вафля-рыбка)",
  f'<path d="M18 64 Q34 34 70 38 Q88 40 98 52 L116 38 Q110 64 116 90 L98 76 Q88 92 66 92 Q34 94 18 64Z" fill="#E8A23E" {s()}/>'
  + "".join(f'<path d="M{x} 54 q4 6 0 12 q-4 6 0 12" fill="none" stroke="#B9702A" stroke-width="2.6"/>' for x in (56, 68, 80))
  + f'<path d="M30 70 Q40 76 46 70" fill="none" {W(2.6)}/>' + eye(36, 58, 0.8)
  + f'<path d="M84 72 Q92 68 96 60" fill="none" stroke="#B9702A" stroke-width="2.6"/>' + sparkle(100, 22, 6)),
 # 48 крыжовник
 ("green", "крыжовник",
  f'<path d="M64 8 V28" {W(4)}/>' + leaf(64, 14, -30, "#7CD26E", 22)
  + f'<ellipse cx="64" cy="72" rx="38" ry="44" fill="#B8E07A" {s()}/>'
  + "".join(f'<path d="M64 30 Q{64+dx} 72 64 114" fill="none" stroke="#8CC05A" stroke-width="2.4"/>' for dx in (-28, -12, 12, 28))
  + f'<path d="M58 28 l-4 -6 M64 28 v-6 M70 28 l4 -6" {W(2.4)}/>' + f(64, 74, d=10, k=0.75)),
 # 49 макису
 ("teal", "бамбуковая циновка для роллов",
  f'<path d="M14 40 L84 30 L114 92 L44 102Z" fill="#E6CF8E" {s()}/>'
  + "".join(f'<path d="M{14+i*7} {40-i} L{44+i*7} {102-i}" stroke="#B89A5A" stroke-width="2"/>' for i in range(1, 10))
  + f'<rect x="34" y="52" width="48" height="26" rx="13" fill="#2F4F3A" {s()} transform="rotate(-8 58 65)"/>'
  f'<circle cx="80" cy="62" r="11" fill="#fff" {W(2.4)}/><circle cx="80" cy="62" r="5" fill="#FF8A5B"/>' + f(54, 66, d=7, k=0.55).replace(O, "#fff")),
 # 50 соевый соус
 ("night", "бутылочка соевого соуса",
  f'<path d="M54 8 H74 L76 22 Q72 26 70 30 H58 Q56 26 52 22Z" fill="#E8344F" {s()}/><path d="M74 12 L84 10" {W(4)}/>'
  f'<path d="M56 30 H72 Q100 54 98 90 Q96 116 64 116 Q32 116 30 90 Q28 54 56 30Z" fill="#E7F2FF" {s()}/>'
  f'<path d="M34 72 Q64 64 94 72 Q96 112 64 112 Q32 112 34 72Z" fill="#5A2A1A"/>' + f(64, 88, d=9, k=0.7).replace(O, "#fff") + sparkle(104, 30, 6)),
 # 51 венчик для матчи
 ("green", "бамбуковый венчик для матчи",
  f'<rect x="54" y="72" width="20" height="44" rx="6" fill="#E6CF8E" {s()}/>'
  + "".join(f'<path d="M{58+i*3} 72 Q{40+i*12} 50 {50+i*7} 18" fill="none" stroke="#C9A85A" stroke-width="2.6"/>' for i in range(5))
  + f'<path d="M46 20 Q64 6 82 20" fill="none" {W(3)}/><path d="M42 36 Q64 50 86 36" fill="none" stroke="#B89A5A" stroke-width="2"/>'
  + f'<path d="M14 100 Q14 86 34 86 Q46 86 46 100Z" fill="#7CBF5A" {W(2.4)}/>' + f(64, 96, d=5, k=0.45, blush=False)),
 # 52 личи
 ("pink", "личи",
  f'<circle cx="52" cy="72" r="34" fill="#E8546F" {s()}/>'
  + "".join(f'<path d="M{x} {y} l4 -4 l4 4 l-4 4Z" fill="#C2304A"/>' for x, y in [(34, 60), (46, 52), (60, 50), (68, 64), (40, 78), (54, 88), (66, 80), (30, 72)])
  + f'<circle cx="92" cy="80" r="22" fill="#FFF6F0" {s()}/><ellipse cx="92" cy="82" rx="8" ry="10" fill="#7A3A2A"/>'
  f'<path d="M52 38 Q56 22 70 18" fill="none" stroke="#6B8E3A" stroke-width="3.4" stroke-linecap="round"/>' + leaf(70, 18, -20, "#7CD26E", 20)
  + f(50, 72, d=8, k=0.6).replace(O, "#fff")),
 # 53 физалис
 ("yellow", "физалис",
  f'<path d="M64 10 Q66 18 64 24" fill="none" {W(3)}/>'
  f'<path d="M64 22 Q30 30 28 70 Q34 100 64 114 Q94 100 100 70 Q98 30 64 22Z" fill="#F5D7A8" opacity=".85" {s()}/>'
  f'<path d="M64 22 Q48 60 64 114 M64 22 Q80 60 64 114 M28 70 Q64 66 100 70" fill="none" stroke="#D9AE70" stroke-width="2.4"/>'
  f'<circle cx="64" cy="72" r="20" fill="#FF9A2E" {W(2.6)}/>' + f(64, 72, d=6, k=0.5)),
 # 54 кулинарная кисточка
 ("sky", "кулинарная кисточка",
  f'<path d="M94 14 L56 70" {W(10)}/><path d="M94 14 L56 70" stroke="#C98A55" stroke-width="6"/>'
  f'<rect x="46" y="64" width="20" height="12" rx="3" fill="#C9D3E0" {W(2.4)} transform="rotate(34 56 70)"/>'
  f'<path d="M48 72 Q30 86 26 110 Q40 116 56 104 Q62 92 62 80Z" fill="#FFE07A" {s()}/>'
  f'<path d="M42 84 L34 106 M50 86 L44 108" stroke="#E0B040" stroke-width="2.4"/>' + f(80, 40, d=6, k=0.5, blush=False).replace(O, "#fff")
  + f'<ellipse cx="88" cy="104" rx="18" ry="6" fill="#FFE07A" opacity=".8"/>'),
 # 55 диспенсер для хлопьев
 ("orange", "диспенсер для хлопьев",
  f'<rect x="38" y="10" width="52" height="64" rx="10" fill="#E7F8FF" {s()}/>'
  + dots([(48, 30), (58, 24), (70, 32), (80, 26), (52, 44), (66, 48), (78, 42), (50, 60), (62, 62), (76, 58)], "#E8A23E", 4)
  + f'<path d="M44 74 H84 L78 92 H50Z" fill="#7FB8E8" {s()}/><rect x="84" y="78" width="22" height="8" rx="4" fill="#E8654F" {W(2.4)}/>'
  f'<path d="M40 100 H88 Q86 116 64 116 Q42 116 40 100Z" fill="#fff" {s()}/>' + f(64, 104, d=8, k=0.5, blush=False)),
 # 56 айва
 ("yellow", "айва",
  f'<path d="M64 20 Q62 10 70 6" fill="none" {W(3.4)}/>' + leaf(70, 12, -10, "#7CD26E", 22)
  + f'<path d="M64 22 Q46 18 38 38 Q22 52 26 80 Q32 112 64 114 Q96 112 102 80 Q106 52 90 38 Q82 18 64 22Z" fill="#F2D24A" {s()}/>'
  f'<path d="M44 40 Q34 54 36 70" fill="none" stroke="#fff" stroke-width="3" opacity=".6"/>' + dots([(82, 92), (88, 78), (74, 100)], "#C9AE30", 1.6)
  + f(64, 74, d=10, k=0.75)),
 # 57 мороженица
 ("teal", "мороженица с ручкой",
  f'<path d="M28 44 H100 L94 114 H34Z" fill="#C98A55" {s()}/><path d="M30 64 H98 M32 94 H96" stroke="#8A5634" stroke-width="4"/>'
  f'<rect x="40" y="30" width="48" height="14" rx="5" fill="#C9D3E0" {s()}/><path d="M64 30 V18 H92 V8" fill="none" {W(5)}/><circle cx="92" cy="8" r="5" fill="#E8654F" {W(2.4)}/>'
  f'<path d="M30 44 Q28 36 36 38 M98 44 Q100 36 92 38" fill="none" stroke="#fff" stroke-width="3"/>' + f(64, 80, d=10, k=0.7).replace(O, "#fff")
  + dots([(20, 30), (110, 40), (16, 60)], "#fff", 3)),
 # 58 палочки для еды на подставке
 ("night", "палочки для еды на подставке",
  f'<path d="M24 86 Q40 70 64 74 Q88 70 104 86 Q88 98 64 94 Q40 98 24 86Z" fill="#FF8FB8" {s()}/>'
  f'<path d="M14 78 L116 40" stroke="#3B3355" stroke-width="9" stroke-linecap="round"/><path d="M14 78 L116 40" stroke="#C0302A" stroke-width="5" stroke-linecap="round"/>'
  f'<path d="M12 64 L114 28" stroke="#3B3355" stroke-width="9" stroke-linecap="round"/><path d="M12 64 L114 28" stroke="#C0302A" stroke-width="5" stroke-linecap="round"/>'
  f'<path d="M90 36 L104 31 M92 50 L106 45" stroke="#FFD25E" stroke-width="4"/>' + f(64, 86, d=8, k=0.55) + sparkle(30, 30, 6)),
 # 59 держатель стаканов
 ("sky", "картонный держатель для стаканов навынос",
  f'<path d="M14 82 H114 L106 114 H22Z" fill="#C98A55" {s()}/>'
  + "".join(f'<path d="M{x-14} 34 H{x+14} L{x+11} 88 H{x-11}Z" fill="{c}" {W(2.6)}/><rect x="{x-16}" y="26" width="32" height="10" rx="4" fill="#fff" {W(2.4)}/>' for x, c in [(42, "#FFB3CF"), (86, "#FFF3DD")])
  + f'<path d="M14 82 H114" stroke="#8A5634" stroke-width="3"/>' + f(64, 100, d=10, k=0.6).replace(O, "#fff")),
 # 60 мандолина-слайсер
 ("green", "мандолина-слайсер для овощей",
  f'<path d="M14 92 L96 34 L112 46 L30 104Z" fill="#FFC94D" {s()}/><path d="M50 72 L74 56" stroke="#C9D3E0" stroke-width="6"/><path d="M50 72 L74 56" {W(1.6)}/>'
  f'<path d="M24 104 V118 M100 52 V70" {W(5)}/>'
  + "".join(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="3" fill="#E8344F" {W(2)}/>' for x, y in [(60, 96), (72, 102), (84, 96)])
  + f'<circle cx="84" cy="40" r="12" fill="#E8344F" {W(2.6)}/>' + f(72, 64, d=7, k=0.5, blush=False)),
 # 61 фейхоа
 ("teal", "фейхоа",
  f'<ellipse cx="48" cy="70" rx="26" ry="38" fill="#4E9A4E" {s()} transform="rotate(-12 48 70)"/>'
  f'<path d="M52 32 l-3 -8 M56 32 l2 -9 M48 33 l-6 -6" {W(2.4)}/>'
  f'<ellipse cx="88" cy="84" rx="22" ry="26" fill="#4E9A4E" {s()}/><ellipse cx="88" cy="84" rx="17" ry="21" fill="#F2F0D6"/>'
  + "".join(f'<path d="M88 84 L{88+12*__import__("math").cos(a/57.3):.1f} {84+14*__import__("math").sin(a/57.3):.1f}" stroke="#C9CC8E" stroke-width="2"/>' for a in range(0, 360, 90))
  + f(46, 70, d=8, k=0.6).replace(O, "#fff")),
 # 62 стаканчик с зубочистками
 ("purple", "стаканчик с зубочистками",
  "".join(f'<path d="M{x} 70 L{x+dx} 18" stroke="#3B3355" stroke-width="5" stroke-linecap="round"/><path d="M{x} 70 L{x+dx} 18" stroke="#F0D9A8" stroke-width="2.4" stroke-linecap="round"/>' for x, dx in [(50, -10), (56, -4), (62, 0), (68, 4), (74, 10), (60, -14), (70, 14)])
  + f'<path d="M64 18 L72 10 L80 18 L72 14Z" fill="#E8344F"/><path d="M84 24 L90 14 L98 22 Z" fill="#FFD25E" {W(2)}/>'
  + f'<path d="M40 60 H88 L84 112 H44Z" fill="#7FB8E8" {s()}/>' + f(64, 86, d=9, k=0.7)),
 # 63 кленовый сироп
 ("orange", "бутылка кленового сиропа",
  f'<rect x="54" y="8" width="20" height="12" rx="3" fill="#E8344F" {W(2.6)}/>'
  f'<path d="M58 20 H70 V32 Q98 40 98 70 V102 Q98 116 84 116 H44 Q30 116 30 102 V70 Q30 40 58 32Z" fill="#C2702A" {s()}/>'
  f'<path d="M64 52 l6 10 l8 -4 l-2 10 l8 4 l-12 6 l2 8 l-10 -4 l-10 4 l2 -8 l-12 -6 l8 -4 l-2 -10 l8 4Z" fill="#E8344F" {W(2)}/>'
  + f'<path d="M98 50 Q112 50 112 62 Q112 74 98 74" fill="none" {W(4)}/>' + f(64, 98, d=9, k=0.6).replace(O, "#fff")),
 # 64 мангостин
 ("purple", "мангостин",
  f'<circle cx="64" cy="70" r="40" fill="#5E2A4E" {s()}/>'
  + "".join(f'<ellipse cx="{64+12*__import__("math").cos(a/57.3):.1f}" cy="{36+5*__import__("math").sin(a/57.3):.1f}" rx="8" ry="5" fill="#6BAE4E" {W(2)} transform="rotate({a} {64+12*__import__("math").cos(a/57.3):.1f} {36+5*__import__("math").sin(a/57.3):.1f})"/>' for a in range(0, 360, 90))
  + f'<path d="M64 30 V20" {W(4)}/>'
  + f'<path d="M44 84 Q64 60 84 84 Q64 104 44 84Z" fill="#fff" {W(2.4)}/><path d="M64 70 V98" stroke="#E6E0F0" stroke-width="2"/>'
  + f(64, 60, d=10, k=0.6).replace(O, "#fff")),
 # 65 дуриан
 ("yellow", "дуриан",
  "".join(f'<path d="M{64+40*__import__("math").cos(a/57.3):.1f} {68+44*__import__("math").sin(a/57.3):.1f} l{9*__import__("math").cos(a/57.3)+3:.1f} {9*__import__("math").sin(a/57.3):.1f} l{-6:.1f} {2:.1f}Z" fill="#8FAE3A" {W(2.2)}/>' for a in range(0, 360, 24))
  + f'<ellipse cx="64" cy="68" rx="40" ry="44" fill="#A8C64A" {s()}/>'
  + "".join(f'<path d="M{x} {y} l4 -6 l4 6Z" fill="#7F9E2E"/>' for x, y in [(40, 50), (56, 40), (74, 40), (88, 52), (36, 74), (90, 76), (48, 96), (76, 98)])
  + f'<path d="M64 24 V12" {W(4)}/>' + f(64, 70, d=10, k=0.75)),
 # 66 пельменница
 ("blue", "пельменница (форма-соты для пельменей)",
  f'<circle cx="64" cy="66" r="48" fill="#E7EEF5" {s()}/>'
  + "".join(f'<path d="M{x-8} {y-5} L{x} {y-10} L{x+8} {y-5} V{y+5} L{x} {y+10} L{x-8} {y+5}Z" fill="#fff" {W(2.2)}/>'
            for x, y in [(64, 66), (48, 56), (80, 56), (48, 76), (80, 76), (64, 46), (64, 86), (32, 66), (96, 66), (40, 40), (88, 40), (40, 92), (88, 92)])
  + f'<circle cx="64" cy="66" r="6" fill="#F2D6A8"/>' + f(64, 22, d=6, k=0.45, blush=False) + sparkle(110, 106, 6)),
]

# Якорь категории «кафе с детской» (скилл kudapoiti-place-icons): тарелка + игрушка-мячик; уникальная «шутка» — блюдо/предмет на тарелке.
def served(body, k=0.74, cy=54):
    t = f'translate({64-64*k:.1f} {cy-64*k:.1f}) scale({k})'
    plate = (f'<ellipse cx="64" cy="100" rx="50" ry="13" fill="#FFFFFF" {s()}/>'
             f'<ellipse cx="64" cy="99" rx="34" ry="7" fill="#EEF3FA" stroke="#B9C7DC" stroke-width="2.2"/>')
    toy = (f'<circle cx="20" cy="86" r="9" fill="#FFD25E" {W(2.4)}/>'
           f'<path d="M12 83 Q20 90 28 83" fill="none" stroke="#E8344F" stroke-width="2.6"/>'
           f'<path d="M17 78 Q19 86 17 94" fill="none" stroke="#5C8FD6" stroke-width="2.4"/>')
    return plate + f'<g transform="{t}">{body}</g>' + toy


L = [(bg, sj, served(body)) for bg, sj, body in L]
DATA = json.load(open(os.path.join(here, "cafes_1106c_data.json")))
assert len(L) == len(DATA), (len(L), len(DATA))
for d, x in zip(DATA, L):
    assert d["subj"] == x[1], (d["id"], d["subj"], x[1])
ICONS = {d["id"]: x for d, x in zip(DATA, L)}

if __name__ == "__main__":
    subj = [x[1] for x in L]
    assert len(subj) == len(set(subj))
    reg = open(os.path.join(src, "subjects.txt")).read()
    for sj in subj:
        assert f"— {sj}\n" not in reg, sj
    for pid, (bg, sj, body) in ICONS.items():
        open(os.path.join(src, pid + ".svg"), "w").write(svg(bg, body))
    with open(os.path.join(src, "subjects.txt"), "a") as fh:
        for pid, (bg, sj, body) in ICONS.items():
            fh.write(f"{pid} — {sj}\n")
    print(len(ICONS))
