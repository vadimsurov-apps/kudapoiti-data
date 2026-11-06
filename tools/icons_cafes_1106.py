"""Иконки робота cafes, 2026-11-06: 103 новых сюжета «еда, посуда, кухня, сладости»
(сверено со всеми листами icons-catalog и icons-src/subjects.txt). Порядок = порядок мест в tools/cafes_1106_data.json."""
import json, os
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=8, k=0.7, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); src = os.path.join(here, "..", "icons-src")
steam = lambda *xs: "".join(f'<path d="M{x} 30 Q{x+4} 22 {x} 14" fill="none" stroke="#fff" stroke-width="3" opacity=".9"/>' for x in xs)
leaf = lambda x, y, r=0: f'<path d="M{x} {y} q8 -14 20 -10 q-4 14 -20 10Z" fill="#6CCB5F" {W(2.4)} transform="rotate({r} {x} {y})"/>'
dots = lambda pts, c, r=2.2: "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x, y in pts)

L = [
 # 1 скалка
 ("orange", "скалка", f'<rect x="30" y="52" width="68" height="26" rx="13" fill="#E6B07A" {s()}/>'
  f'<rect x="10" y="59" width="22" height="12" rx="6" fill="#C98A52" {s()}/><rect x="96" y="59" width="22" height="12" rx="6" fill="#C98A52" {s()}/>'
  f'<path d="M24 92 Q64 104 104 92 L100 106 Q64 116 28 106Z" fill="#FFF3D6" {W(2.6)}/>' + f(64, 63, d=9, k=0.7)),
 # 2 лопатка
 ("yellow", "кухонная лопатка-шпатель", f'<path d="M58 70 L54 116 H74 L70 70Z" fill="#8A5A3A" {s()}/>'
  f'<rect x="40" y="16" width="48" height="56" rx="10" fill="#FF8FB8" {s()}/>'
  f'<path d="M52 24 V40 M64 24 V40 M76 24 V40" stroke="{O}" stroke-width="3" stroke-linecap="round"/>' + f(64, 54, d=9, k=0.7)),
 # 3 щипцы
 ("teal", "щипцы для гриля", f'<path d="M58 20 L30 104 Q28 110 34 110 L40 108 L62 30Z" fill="#C9D3E0" {s()}/>'
  f'<path d="M70 20 L98 104 Q100 110 94 110 L88 108 L66 30Z" fill="#C9D3E0" {s()}/>'
  f'<rect x="52" y="12" width="24" height="22" rx="8" fill="#E8654F" {s()}/>' + f(64, 22, d=6, k=0.45, blush=False)
  + f'<ellipse cx="64" cy="100" rx="16" ry="9" fill="#C0583A" {W(2.4)}/>'),
 # 4 прихватка
 ("pink", "прихватка-рукавица", f'<path d="M34 104 V46 Q34 22 58 22 Q82 22 82 46 V60 Q82 44 94 46 Q106 50 98 66 L84 92 V104Z" fill="#E8654F" {s()}/>'
  f'<rect x="30" y="100" width="58" height="14" rx="5" fill="#fff" {s()}/>' + dots([(46, 40), (66, 36), (50, 86), (72, 84)], "#FFD1C4", 3.2)
  + f(56, 62, d=9, k=0.75)),
 # 5 ручная кофемолка
 ("orange", "ручная кофемолка", f'<path d="M36 60 H92 V108 H36Z" fill="#B97A4A" {s()}/><rect x="56" y="88" width="16" height="10" rx="2" fill="#7A4A2A" {W(2.4)}/>'
  f'<path d="M44 60 L50 42 H78 L84 60Z" fill="#C9D3E0" {s()}/><path d="M64 42 V30 H96" fill="none" {W(4)}/><circle cx="98" cy="30" r="6" fill="#E8654F" {W(2.4)}/>'
  + f(64, 74, d=9, k=0.7)),
 # 6 гейзерная кофеварка
 ("yellow", "гейзерная кофеварка", f'<path d="M40 64 L48 108 H80 L88 64Z" fill="#C9D3E0" {s()}/>'
  f'<path d="M42 64 L48 26 H80 L86 64Z" fill="#DDE4EE" {s()}/><path d="M48 26 L44 18 H70" fill="none" {W(3)}/>'
  f'<path d="M86 32 Q104 36 92 56" fill="none" {W(5)}/><rect x="38" y="60" width="52" height="8" rx="3" fill="#7A869C" {W(2.4)}/>'
  + f(64, 84, d=8, k=0.65) + steam(30, 40)),
 # 7 френч-пресс
 ("sky", "френч-пресс", f'<rect x="40" y="38" width="44" height="66" rx="6" fill="#E6F6FF" {s()}/>'
  f'<rect x="43" y="62" width="38" height="40" rx="4" fill="#8A5A3A"/><path d="M84 50 Q102 52 100 72 Q98 88 84 88" fill="none" {W(5)}/>'
  f'<rect x="36" y="30" width="52" height="10" rx="4" fill="#3B3355"/><path d="M62 30 V14 M54 14 H70" {W(4)}/>'
  + f(62, 80, d=8, k=0.6).replace(O, "#fff")),
 # 8 холодильник
 ("blue", "холодильник", f'<rect x="34" y="12" width="60" height="104" rx="10" fill="#F4F8FF" {s()}/><path d="M34 46 H94" {W(3)}/>'
  f'<path d="M44 24 V36 M44 58 V74" {W(4)}/><circle cx="80" cy="28" r="5" fill="#FF8FB8" {W(2)}/><rect x="72" y="56" width="12" height="9" rx="2" fill="#FFD25E" {W(2)}/>'
  + f(64, 84, d=10, k=0.8)),
 # 9 микроволновка
 ("purple", "микроволновка", f'<rect x="14" y="34" width="100" height="64" rx="10" fill="#F2EEFF" {s()}/>'
  f'<rect x="22" y="42" width="62" height="48" rx="6" fill="#FFE7A3" {W(2.6)}/><circle cx="99" cy="52" r="5" fill="#A98BF0" {W(2.2)}/><circle cx="99" cy="68" r="5" fill="#A98BF0" {W(2.2)}/>'
  f'<rect x="92" y="78" width="14" height="6" rx="2" fill="#7CD26E" {W(2)}/>' + f(53, 64, d=9, k=0.75)),
 # 10 кофемашина
 ("orange", "рожковая кофемашина", f'<rect x="26" y="16" width="76" height="30" rx="8" fill="#E8654F" {s()}/><rect x="26" y="44" width="76" height="64" rx="6" fill="#C9D3E0" {s()}/>'
  f'<path d="M48 50 H80 V60 H48Z" fill="#7A869C" {W(2.4)}/><path d="M80 54 H100" {W(4)}/>'
  f'<path d="M52 84 H76 V100 Q76 104 72 104 H56 Q52 104 52 100Z" fill="#fff" {W(2.6)}/><path d="M64 62 V80" stroke="#8A5A3A" stroke-width="3"/>'
  + f(64, 28, d=10, k=0.6)),
 # 11 вафельница
 ("yellow", "вафельница", f'<path d="M20 84 H108 V102 Q108 108 102 108 H26 Q20 108 20 102Z" fill="#7A6AA8" {s()}/>'
  f'<path d="M24 84 L36 30 Q38 24 46 24 H92 Q100 24 100 32 L104 84Z" fill="#A98BF0" {s()}/>'
  f'<path d="M24 84 H104 L100 74 H28Z" fill="#F2C46B" {W(2.4)}/><path d="M40 78 H96 M52 74 V84 M64 74 V84 M76 74 V84 M88 74 V84" stroke="#C98A3A" stroke-width="2"/>'
  + f(64, 48, d=10, k=0.8)),
 # 12 гриль-барбекю
 ("green", "гриль-барбекю", f'<path d="M50 84 L36 116 M78 84 L92 116 M64 84 V116" {W(4)}/>'
  f'<path d="M22 58 H106 Q104 90 64 92 Q24 90 22 58Z" fill="#3B3355" {s()}/>'
  f'<path d="M22 58 Q26 24 64 22 Q102 24 106 58Z" fill="#E8654F" {s()}/><circle cx="64" cy="20" r="5" fill="#C9D3E0" {W(2.2)}/>'
  + f(64, 40, d=11, k=0.8) + f'<path d="M34 70 H94" stroke="#FF9A3C" stroke-width="3"/>'),
 # 13 соковыжималка
 ("yellow", "соковыжималка для цитрусов", f'<path d="M18 74 H110 Q108 106 64 108 Q20 106 18 74Z" fill="#9DD6F5" {s()}/>'
  f'<path d="M108 80 L120 74" {W(4)}/><path d="M42 74 Q44 30 64 18 Q84 30 86 74Z" fill="#E6F6FF" {s()}/>'
  f'<path d="M64 22 V72 M52 34 L56 72 M76 34 L72 72" stroke="#9DD6F5" stroke-width="2.4"/>'
  f'<path d="M92 34 a14 14 0 0 1 28 0Z" fill="#FFD25E" {W(2.4)}/>' + f(64, 88, d=10, k=0.7)),
 # 14 кондитерский мешок
 ("pink", "кондитерский мешок с кремом", '<g transform="rotate(-35 64 60)">' + f'<path d="M34 14 Q64 6 94 14 L70 88 H58Z" fill="#E6F6FF" {s()}/>'
  f'<path d="M34 14 Q64 20 94 14 Q94 6 64 4 Q34 6 34 14Z" fill="#FFB3CF" {W(2.6)}/>'
  f'<path d="M58 88 L60 98 H68 L70 88Z" fill="#C9D3E0" {W(2.6)}/>' + f(64, 42, d=9, k=0.7) + '</g>'
  f'<path d="M88 112 Q86 96 98 92 Q96 84 106 84 Q116 86 112 96 Q122 100 118 112Z" fill="#FFB3CF" {W(2.6)}/>'),
 # 15 мерный стакан
 ("sky", "мерный стакан", f'<path d="M30 26 H96 L90 108 Q90 112 84 112 H42 Q36 112 36 108Z" fill="#F4FBFF" {s()}/>'
  f'<path d="M34 64 H92 L90 108 Q90 112 84 112 H42 Q36 112 36 108Z" fill="#7FD3FF" {W(2.4)}/>'
  f'<path d="M30 26 L22 34" {W(4)}/><path d="M80 40 H92 M84 52 H92 M80 76 H90 M84 88 H90" stroke="{O}" stroke-width="2.6"/>'
  + f(58, 84, d=8, k=0.65)),
 # 16 ланч-бокс
 ("green", "ланч-бокс", f'<rect x="16" y="40" width="96" height="66" rx="12" fill="#7CD26E" {s()}/>'
  f'<rect x="16" y="40" width="96" height="20" rx="8" fill="#5CB85C" {s()}/><path d="M52 40 Q52 24 64 24 Q76 24 76 40" fill="none" {W(4)}/>'
  f'<rect x="56" y="54" width="16" height="10" rx="3" fill="#FFD25E" {W(2.2)}/>' + f(64, 82, d=11, k=0.8)),
 # 17 мешок муки
 ("orange", "мешок муки", f'<path d="M34 34 Q30 70 32 106 Q64 114 96 106 Q98 70 94 34Z" fill="#F4E6CF" {s()}/>'
  f'<path d="M34 34 Q48 22 64 30 Q80 22 94 34 Q80 42 64 36 Q48 42 34 34Z" fill="#E6D2B0" {W(2.6)}/>'
  f'<path d="M44 52 q20 -8 40 0" fill="none" stroke="#C98A52" stroke-width="3"/><circle cx="104" cy="96" r="6" fill="#fff" opacity=".9"/><circle cx="112" cy="84" r="3" fill="#fff"/>'
  + f(64, 76, d=10, k=0.8)),
 # 18 банка с печеньем
 ("blue", "банка с печеньем", f'<rect x="34" y="32" width="60" height="76" rx="14" fill="#E6F6FF" {s()}/><rect x="40" y="18" width="48" height="16" rx="6" fill="#E8654F" {s()}/>'
  f'<circle cx="52" cy="88" r="10" fill="#E0A55E" {W(2.4)}/><circle cx="76" cy="92" r="10" fill="#E0A55E" {W(2.4)}/><circle cx="64" cy="78" r="9" fill="#E0A55E" {W(2.4)}/>'
  + dots([(50, 86), (54, 91), (75, 90), (79, 95), (62, 76), (66, 81)], "#6B3E1E", 1.6) + f(64, 56, d=9, k=0.7)),
 # 19 сервировочная тележка
 ("teal", "сервировочная тележка", f'<path d="M24 50 H104 M24 88 H104" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
  f'<path d="M28 50 V96 M100 50 V96" {W(4)}/><path d="M100 50 L112 36" {W(4)}/><circle cx="32" cy="104" r="7" fill="#FFD25E" {W(2.4)}/><circle cx="96" cy="104" r="7" fill="#FFD25E" {W(2.4)}/>'
  f'<path d="M36 48 Q36 28 56 28 Q76 28 76 48Z" fill="#DDE4EE" {s()}/><circle cx="56" cy="26" r="3" fill="#C9D3E0" {W(2)}/>'
  f'<path d="M40 86 Q64 72 88 86Z" fill="#FF8FB8" {W(2.4)}/>' + f(56, 40, d=7, k=0.5)),
 # 20 поднос с едой
 ("yellow", "поднос с обедом", f'<path d="M12 64 H116 L106 98 H22Z" fill="#E8654F" {s()}/>'
  f'<circle cx="40" cy="76" r="12" fill="#fff" {W(2.4)}/><circle cx="40" cy="76" r="6" fill="#FFB347"/><rect x="60" y="68" width="22" height="18" rx="4" fill="#7CD26E" {W(2.4)}/>'
  f'<path d="M92 50 H104 L102 76 H94Z" fill="#9DD6F5" {W(2.4)}/>' + f(64, 88, d=10, k=0.55, mouth=False)
  + f'<path d="M60 94 Q64 98 68 94" fill="none" {W(2.4)}/>'),
 # 21 клош
 ("purple", "ресторанный клош (колпак для блюда)", f'<path d="M14 92 H114" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
  f'<path d="M20 90 Q22 36 64 34 Q106 36 108 90Z" fill="#DDE4EE" {s()}/><circle cx="64" cy="28" r="7" fill="#C9D3E0" {s()}/>'
  f'<path d="M34 64 Q38 48 52 44" fill="none" stroke="#fff" stroke-width="4"/>' + f(64, 68, d=11, k=0.85) + sparkle(104, 24, 7)),
 # 22 меню
 ("orange", "папка меню", f'<rect x="26" y="18" width="76" height="96" rx="8" fill="#8A5A3A" {s()}/>'
  f'<rect x="36" y="28" width="56" height="76" rx="4" fill="#FFF3D6" {W(2.4)}/>'
  f'<path d="M46 40 H82 M46 48 H74" stroke="#C98A52" stroke-width="3" stroke-linecap="round"/><path d="M46 88 H82 M46 96 H70" stroke="#C98A52" stroke-width="3" stroke-linecap="round"/>'
  + f(64, 66, d=9, k=0.7)),
 # 23 колокольчик официанта
 ("yellow", "колокольчик официанта", f'<rect x="18" y="92" width="92" height="12" rx="5" fill="#8A5A3A" {s()}/>'
  f'<path d="M24 92 Q24 46 64 44 Q104 46 104 92Z" fill="#FFD25E" {s()}/><path d="M64 44 V32" {W(4)}/><ellipse cx="64" cy="28" rx="10" ry="5" fill="#FFB347" {s()}/>'
  f'<path d="M36 74 Q40 58 54 52" fill="none" stroke="#fff" stroke-width="4"/>' + f(64, 72, d=11, k=0.8)
  + f'<path d="M16 34 L24 40 M110 34 L102 40 M12 52 H22 M116 52 H106" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'),
 # 24 нагрудник
 ("sky", "детский нагрудник", f'<path d="M30 30 Q30 20 40 20 H50 Q50 36 64 36 Q78 36 78 20 H88 Q98 20 98 30 V86 Q98 112 64 112 Q30 112 30 86Z" fill="#FFB3CF" {s()}/>'
  f'<path d="M44 92 Q64 104 84 92 V100 Q64 112 44 100Z" fill="#FF8FB8" {W(2.4)}/>' + dots([(42, 40), (86, 40), (40, 70), (88, 72)], "#fff", 3)
  + f(64, 64, d=10, k=0.8)),
 # 25 стульчик для кормления
 ("green", "детский стульчик для кормления", f'<path d="M40 72 L30 118 M88 72 L98 118 M44 100 H84" {W(4)}/>'
  f'<path d="M38 20 H90 V72 H38Z" fill="#FFD25E" {s()}/><path d="M26 62 H102 V72 H26Z" fill="#FFB347" {s()}/>'
  + f(64, 42, d=10, k=0.8)),
 # 26 сахарница
 ("pink", "сахарница с рафинадом", f'<path d="M26 54 H102 Q100 104 64 104 Q28 104 26 54Z" fill="#F4F8FF" {s()}/>'
  f'<path d="M26 64 Q14 62 16 74 Q18 84 30 82 M102 64 Q114 62 112 74 Q110 84 98 82" fill="none" {W(3)}/>'
  f'<rect x="42" y="36" width="16" height="16" rx="2" fill="#fff" {W(2.4)} transform="rotate(-12 50 44)"/><rect x="64" y="32" width="16" height="16" rx="2" fill="#fff" {W(2.4)} transform="rotate(10 72 40)"/>'
  f'<path d="M20 54 H108" stroke="{O}" stroke-width="4" stroke-linecap="round"/>' + f(64, 76, d=10, k=0.75)
  + f'<path d="M40 92 H88" stroke="#FF8FB8" stroke-width="3"/>'),
 # 27 чайный пакетик
 ("teal", "чайный пакетик", f'<path d="M64 12 V40" stroke="{O}" stroke-width="2.4"/><rect x="54" y="6" width="20" height="14" rx="2" fill="#FFD25E" {W(2.4)}/>'
  f'<path d="M36 40 H92 L98 108 H30Z" fill="#F4E6CF" {s()}/><path d="M36 40 L48 52 H80 L92 40" fill="none" {W(2.4)}/>'
  f'<path d="M30 112 Q64 100 98 112" fill="none" stroke="#C98A52" stroke-width="3" opacity=".6"/>' + f(64, 78, d=10, k=0.8)),
 # 28 заварочное ситечко
 ("purple", "заварочное ситечко-шарик", f'<path d="M64 14 Q84 14 84 30 V40" fill="none" {W(3)}/><circle cx="84" cy="14" r="5" fill="#FF8FB8" {W(2.2)}/>'
  f'<circle cx="64" cy="76" r="36" fill="#DDE4EE" {s()}/><path d="M28 76 H100" {W(3)}/>'
  + dots([(48, 64), (60, 60), (72, 60), (84, 64), (52, 96), (64, 100), (76, 96)], "#7A869C", 2)
  + f'<path d="M84 40 L76 42" {W(3)}/>' + f(64, 84, d=10, k=0.7, mouth=False)),
 # 29 стакан в подстаканнике
 ("night", "стакан чая в подстаканнике", f'<path d="M38 34 H90 L84 104 H44Z" fill="#C46A2A" {s()}/>'
  f'<path d="M36 64 H92 L86 110 H42Z" fill="#C9D3E0" {s()}/><path d="M92 70 Q110 72 106 88 Q102 98 88 96" fill="none" {W(4)}/>'
  f'<path d="M46 72 L82 102 M82 72 L46 102" stroke="#A9B4C6" stroke-width="2.4"/><path d="M70 18 L58 50" {W(3)}/>' + steam(52, 76) + f(64, 46, d=8, k=0.6, blush=False)),
 # 30 пакетик сока
 ("orange", "пакетик сока с трубочкой", f'<path d="M34 34 H94 V110 H34Z" fill="#FFB347" {s()}/><path d="M34 34 L44 20 H84 L94 34" fill="#FFD25E" {s()}/>'
  f'<path d="M78 22 L86 4 L96 6" fill="none" stroke="#FF8FB8" stroke-width="5" stroke-linecap="round"/>'
  f'<circle cx="64" cy="94" r="10" fill="#FF9A3C" {W(2.4)}/>' + leaf(66, 84, -20) + f(64, 60, d=10, k=0.8)),
 # 31 банка газировки
 ("blue", "банка газировки", f'<path d="M38 24 Q38 16 46 16 H82 Q90 16 90 24 V104 Q90 112 82 112 H46 Q38 112 38 104Z" fill="#E8654F" {s()}/>'
  f'<path d="M38 26 H90 M38 102 H90" {W(3)}/><ellipse cx="64" cy="20" rx="10" ry="3" fill="#C9D3E0" {W(2)}/>'
  f'<path d="M40 82 Q64 70 88 82 V92 Q64 80 40 92Z" fill="#fff"/>' + f(64, 54, d=10, k=0.8) + dots([(100, 30), (106, 46), (98, 58)], "#fff", 3)),
 # 32 помидор
 ("green", "помидор", f'<circle cx="64" cy="70" r="40" fill="#F0503C" {s()}/>'
  f'<path d="M64 32 L54 22 L60 34 L46 34 L58 40 L52 50 L64 42 L76 50 L70 40 L82 34 L68 34 L74 22Z" fill="#5CB85C" {W(2.4)}/>'
  f'<path d="M38 56 Q42 44 52 40" fill="none" stroke="#fff" stroke-width="4" opacity=".7"/>' + f(64, 74, d=11, k=0.85)),
 # 33 огурец
 ("teal", "огурец", f'<path d="M30 96 Q14 80 30 60 Q60 22 98 22 Q114 26 104 44 Q80 92 30 96Z" fill="#6CCB5F" {s()}/>'
  + dots([(48, 70), (62, 56), (78, 42), (90, 36), (70, 66), (56, 80)], "#3E8E3A", 2.2) + f'<path d="M98 22 L108 12" {W(3)}/>' + f(66, 58, d=9, k=0.7)),
 # 34 баклажан
 ("purple", "баклажан", f'<path d="M64 36 Q100 40 96 82 Q92 112 64 112 Q36 112 32 82 Q28 40 64 36Z" fill="#7B4FB8" {s()}/>'
  f'<path d="M44 38 Q64 22 84 38 Q74 46 64 40 Q54 46 44 38Z" fill="#5CB85C" {s()}/><path d="M64 30 V14" stroke="#5CB85C" stroke-width="6" stroke-linecap="round"/>'
  + f(64, 76, d=11, k=0.85).replace(O, "#fff")),
 # 35 брокколи
 ("green", "брокколи", f'<path d="M54 70 L48 114 H80 L74 70Z" fill="#A7E08F" {s()}/>'
  f'<circle cx="44" cy="54" r="18" fill="#3E9E46" {s()}/><circle cx="84" cy="54" r="18" fill="#3E9E46" {s()}/><circle cx="64" cy="38" r="20" fill="#4FB45A" {s()}/>'
  f'<circle cx="64" cy="64" r="16" fill="#4FB45A" {W(2.6)}/>' + f(64, 92, d=7, k=0.6)),
 # 36 тыква
 ("orange", "тыква", f'<ellipse cx="64" cy="74" rx="46" ry="34" fill="#FF9A3C" {s()}/>'
  f'<path d="M64 40 Q46 74 64 108 M64 40 Q82 74 64 108 M40 46 Q28 74 40 102 M88 46 Q100 74 88 102" fill="none" stroke="#D96A1E" stroke-width="3"/>'
  f'<path d="M62 42 Q60 26 70 18" fill="none" stroke="#5A8A3A" stroke-width="7" stroke-linecap="round"/>' + leaf(70, 28, 0) + f(64, 76, d=12, k=0.85)),
 # 37 редиска
 ("pink", "редиска", f'<circle cx="64" cy="76" r="30" fill="#F2476A" {s()}/><path d="M64 106 Q64 116 58 120" fill="none" {W(3)}/>'
  f'<path d="M50 104 Q64 110 78 104 Q72 112 64 112 Q56 112 50 104Z" fill="#fff"/>'
  f'<path d="M64 46 Q46 30 40 10 Q58 16 64 46 Q70 16 88 10 Q82 30 64 46Z" fill="#5CB85C" {s()}/>' + f(64, 74, d=10, k=0.8)),
 # 38 свёкла
 ("purple", "свёкла", f'<path d="M64 44 Q102 44 98 78 Q94 104 64 116 Q34 104 30 78 Q26 44 64 44Z" fill="#9B2A55" {s()}/>'
  f'<path d="M64 46 Q50 26 36 18 Q52 16 64 40 M64 46 Q78 26 92 18 Q76 16 64 40" fill="#6CCB5F" {s()}/>'
  f'<path d="M42 66 Q50 58 58 60" fill="none" stroke="#fff" stroke-width="3" opacity=".5"/>' + f(64, 78, d=11, k=0.85).replace(O, "#fff")),
 # 39 горох в стручке
 ("green", "горох в стручке", f'<path d="M14 70 Q40 36 114 50 Q90 98 14 70Z" fill="#7CD26E" {s()}/>'
  f'<path d="M24 66 Q60 50 104 56 Q84 84 24 66Z" fill="#B7EB8F" {W(2.4)}/>'
  + "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="#5CB85C" {W(2.4)}/>' for x, y in [(40, 66), (60, 64), (80, 62)])
  + f(60, 64, d=4, k=0.4, blush=False) + eye(37, 64, 0.4) + eye(43, 64, 0.4) + eye(77, 60, 0.4) + eye(83, 60, 0.4)),
 # 40 лимон
 ("yellow", "лимон", f'<path d="M18 64 Q22 30 64 28 Q106 30 110 64 Q106 98 64 100 Q22 98 18 64Z" fill="#FFE14D" {s()}/>'
  f'<path d="M110 64 L120 62 M18 64 L8 66" {W(4)}/>' + leaf(66, 30, -30) + f(64, 66, d=11, k=0.85)),
 # 41 персик
 ("orange", "персик", f'<path d="M64 36 Q22 28 22 72 Q24 110 64 110 Q104 110 106 72 Q106 28 64 36Z" fill="#FFB38A" {s()}/>'
  f'<path d="M64 38 Q54 72 64 108" fill="none" stroke="#F08A6A" stroke-width="3"/><path d="M64 36 Q64 26 70 20" fill="none" {W(3.5)}/>' + leaf(68, 26, 0)
  + f(64, 76, d=13, k=0.85)),
 # 42 слива
 ("purple", "слива", f'<ellipse cx="64" cy="72" rx="34" ry="40" fill="#6B4CC2" {s()}/>'
  f'<path d="M64 34 Q56 72 64 110" fill="none" stroke="#4E338F" stroke-width="3"/><path d="M64 34 Q66 22 74 16" fill="none" {W(3.5)}/>'
  f'<ellipse cx="48" cy="54" rx="6" ry="10" fill="#fff" opacity=".35"/>' + f(64, 76, d=12, k=0.85).replace(O, "#fff")),
 # 43 манго
 ("yellow", "манго", f'<path d="M30 92 Q14 54 46 30 Q78 12 102 40 Q118 70 92 98 Q62 122 30 92Z" fill="#FFB52E" {s()}/>'
  f'<path d="M30 92 Q14 54 46 30 Q40 70 70 100 Q48 108 30 92Z" fill="#F07A3C" opacity=".6"/>' + f'<path d="M90 30 L96 18" {W(3.5)}/>' + leaf(96, 20, 10)
  + f(70, 68, d=11, k=0.85)),
 # 44 малина
 ("pink", "малина", "".join(f'<circle cx="{x}" cy="{y}" r="10" fill="#E8336A" {W(2.4)}/>' for x, y in
  [(64, 104), (52, 96), (76, 96), (44, 82), (64, 86), (84, 82), (44, 66), (64, 68), (84, 66), (54, 52), (74, 52)])
  + f'<path d="M42 44 L54 40 L58 30 L64 40 L70 30 L74 40 L86 44 L72 48 H56Z" fill="#5CB85C" {W(2.4)}/>' + f(64, 74, d=10, k=0.75)),
 # 45 инжир
 ("purple", "инжир в разрезе", f'<path d="M64 16 Q72 34 96 54 Q114 76 100 98 Q84 116 64 116 Q44 116 28 98 Q14 76 32 54 Q56 34 64 16Z" fill="#8A4F9E" {s()}/>'
  f'<path d="M64 34 Q70 48 88 62 Q100 78 90 94 Q78 106 64 106 Q50 106 38 94 Q28 78 40 62 Q58 48 64 34Z" fill="#F27A8F" {W(2.4)}/>'
  + dots([(54, 70), (74, 70), (50, 86), (78, 86), (64, 96), (64, 62)], "#FFE7A3", 2) + f(64, 80, d=9, k=0.7)),
 # 46 хурма
 ("orange", "хурма", f'<path d="M20 70 Q20 36 64 36 Q108 36 108 70 Q108 108 64 108 Q20 108 20 70Z" fill="#FF8A2B" {s()}/>'
  f'<path d="M64 36 L44 30 L54 44 L36 46 L56 50 M64 36 L84 30 L74 44 L92 46 L72 50 M64 36 V52" fill="#6CCB5F" {W(2.4)}/>'
  f'<path d="M40 30 Q64 50 88 30 Q76 44 64 42 Q52 44 40 30Z" fill="#6CCB5F" {W(2.4)}/>' + f(64, 76, d=12, k=0.85)),
 # 47 луковица
 ("yellow", "луковица", f'<path d="M64 26 Q72 50 96 64 Q110 86 92 104 Q78 114 64 114 Q50 114 36 104 Q18 86 32 64 Q56 50 64 26Z" fill="#E8A04A" {s()}/>'
  f'<path d="M64 30 Q58 70 64 112 M64 30 Q80 70 78 110 M64 30 Q48 70 50 110" fill="none" stroke="#C47A2A" stroke-width="2.4"/>'
  f'<path d="M64 28 Q60 14 54 8 M64 28 Q70 14 76 10" fill="none" stroke="#6CCB5F" stroke-width="4" stroke-linecap="round"/>'
  f'<path d="M56 114 L52 122 M64 114 V124 M72 114 L76 122" stroke="{O}" stroke-width="2"/>' + f(64, 84, d=11, k=0.8)),
 # 48 чеснок
 ("sky", "головка чеснока", f'<path d="M64 26 Q80 50 98 64 Q114 92 90 108 Q64 118 38 108 Q14 92 30 64 Q48 50 64 26Z" fill="#FBF6EE" {s()}/>'
  f'<path d="M64 30 Q50 64 52 112 M64 30 Q78 64 76 112 M60 36 Q30 70 38 106 M68 36 Q98 70 90 106" fill="none" stroke="#D9CBB5" stroke-width="2.4"/>'
  f'<path d="M64 28 Q62 16 66 8" fill="none" stroke="#C9B48E" stroke-width="5" stroke-linecap="round"/>' + f(64, 84, d=11, k=0.8)),
 # 49 картофелина
 ("orange", "картофелина", f'<path d="M30 56 Q36 26 70 28 Q106 30 104 64 Q102 104 64 104 Q22 102 30 56Z" fill="#D9A766" {s()}/>'
  + dots([(44, 50), (88, 46), (92, 84), (40, 86), (70, 40)], "#A9763A", 2.4) + f'<path d="M78 94 q4 -6 10 -2" fill="none" stroke="#A9763A" stroke-width="2.4"/>'
  + f(66, 66, d=11, k=0.85)),
 # 50 грецкий орех
 ("yellow", "грецкий орех", f'<ellipse cx="64" cy="66" rx="38" ry="44" fill="#C98A52" {s()}/>'
  f'<path d="M64 22 V110" {W(3)}/><path d="M40 40 Q50 50 44 62 Q38 74 46 88 M88 40 Q78 50 84 62 Q90 74 82 88" fill="none" stroke="#9A6532" stroke-width="2.6"/>'
  + f(64, 66, d=12, k=0.8)),
 # 51 арахис
 ("orange", "арахис в скорлупе", f'<path d="M44 20 Q74 14 76 40 Q76 52 70 62 Q64 72 68 84 Q74 112 48 114 Q24 114 28 88 Q30 76 38 66 Q46 56 40 42 Q34 24 44 20Z" fill="#E6C08A" {s()}/>'
  + dots([(48, 30), (60, 34), (54, 44), (46, 92), (56, 100), (40, 102)], "#C49A5E", 2.2) + f(52, 76, d=8, k=0.6)
  + f'<path d="M86 96 Q98 90 106 98 Q100 108 88 104Z" fill="#F4D7A8" {W(2.4)}/>'),
 # 52 каштаны
 ("night", "жареные каштаны в кульке", f'<path d="M30 46 H98 L64 118Z" fill="#F4E6CF" {s()}/><path d="M38 60 H90" stroke="#C98A52" stroke-width="3"/>'
  + "".join(f'<path d="M{x-14} {y+6} Q{x-14} {y-12} {x} {y-14} Q{x+14} {y-12} {x+14} {y+6}Z" fill="#8A4A24" {W(2.4)}/>' for x, y in [(46, 44), (64, 34), (82, 44)])
  + steam(52, 76) + f(64, 76, d=9, k=0.7)),
 # 53 мармеладный мишка
 ("green", "мармеладный мишка", f'<circle cx="44" cy="30" r="10" fill="#FF6B6B" {s()}/><circle cx="84" cy="30" r="10" fill="#FF6B6B" {s()}/>'
  f'<path d="M36 70 Q30 62 34 52 Q40 30 64 30 Q88 30 94 52 Q98 62 92 70 Q104 76 100 90 Q96 100 88 98 Q90 112 76 114 H52 Q38 112 40 98 Q32 100 28 90 Q24 76 36 70Z" fill="#FF6B6B" opacity=".92" {s()}/>'
  f'<ellipse cx="50" cy="40" rx="5" ry="8" fill="#fff" opacity=".5"/>' + f(64, 50, d=10, k=0.8)),
 # 54 карамельная трость
 ("blue", "карамельная трость", f'<path d="M48 116 V48 Q48 18 72 18 Q96 18 96 44 V54" fill="none" stroke="{O}" stroke-width="22" stroke-linecap="round"/>'
  f'<path d="M48 116 V48 Q48 18 72 18 Q96 18 96 44 V54" fill="none" stroke="#fff" stroke-width="15" stroke-linecap="round"/>'
  f'<path d="M48 116 V48 Q48 18 72 18 Q96 18 96 44 V54" fill="none" stroke="#F0503C" stroke-width="15" stroke-dasharray="8 10" stroke-linecap="butt"/>'
  f'<circle cx="48" cy="80" r="13" fill="#fff" {W(2.4)}/>' + eye(44, 78, 0.45) + eye(52, 78, 0.45)
  + f'<path d="M45 84 Q48 87 51 84" fill="none" {W(2)}/>' + sparkle(96, 92, 9) + sparkle(22, 30, 6)),
 # 55 коробка конфет
 ("pink", "коробка конфет", f'<path d="M64 26 Q100 6 112 40 Q118 72 64 110 Q10 72 16 40 Q28 6 64 26Z" fill="#E8336A" {s()}/>'
  f'<path d="M64 36 Q92 20 100 44 Q104 66 64 96 Q24 66 28 44 Q36 20 64 36Z" fill="#FFD7E4" {W(2.4)}/>'
  + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="#7A4A2A" {W(2)}/>' for x, y in [(48, 50), (80, 50), (64, 76)]) + f(64, 54, d=6, k=0.5, blush=False)),
 # 56 чурро
 ("yellow", "чурро с шоколадом", f'<path d="M30 112 L42 52 H86 L98 112Z" fill="#E8654F" {s()}/><path d="M36 82 H92" stroke="#fff" stroke-width="5"/>'
  f'<rect x="44" y="14" width="14" height="70" rx="7" fill="#E6A85A" {s()} transform="rotate(-10 51 50)"/><rect x="70" y="10" width="14" height="74" rx="7" fill="#E6A85A" {s()} transform="rotate(10 77 46)"/>'
  f'<path d="M48 24 V74 M76 22 V74" stroke="#C47A2A" stroke-width="2" stroke-dasharray="4 4"/>' + f(64, 98, d=10, k=0.7).replace(O, "#3B3355")),
 # 57 желе
 ("teal", "желе на тарелке", f'<path d="M14 100 Q64 116 114 100 L110 110 Q64 124 18 110Z" fill="#fff" {s()}/>'
  f'<path d="M30 100 L36 48 Q38 38 64 38 Q90 38 92 48 L98 100 Q64 108 30 100Z" fill="#7BE0C8" opacity=".95" {s()}/>'
  f'<path d="M36 60 Q64 66 92 60" fill="none" stroke="#3FB59A" stroke-width="3"/><circle cx="64" cy="32" r="8" fill="#F0503C" {W(2.4)}/>'
  f'<path d="M44 52 Q46 44 54 42" fill="none" stroke="#fff" stroke-width="4"/>' + f(64, 80, d=11, k=0.8)),
 # 58 флан
 ("orange", "крем-карамель (флан)", f'<path d="M12 100 H116" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
  f'<path d="M26 98 L36 46 H92 L102 98Z" fill="#FFE08A" {s()}/><path d="M36 46 Q64 38 92 46 L94 58 Q64 68 34 58Z" fill="#B5662A" {W(2.6)}/>'
  f'<path d="M40 58 Q42 70 46 64 M58 62 Q60 76 64 66 M80 60 Q82 72 86 62" fill="#B5662A" {W(2)}/>' + f(64, 80, d=11, k=0.8)),
 # 59 рахат-лукум
 ("pink", "рахат-лукум", "".join(f'<rect x="{x}" y="{y}" width="30" height="28" rx="6" fill="{c}" {s()}/>' for x, y, c in
  [(22, 72, "#FF9FC2"), (50, 76, "#FFF0C0"), (78, 72, "#B7EB8F"), (36, 44, "#FFF0C0"), (64, 44, "#FF9FC2")])
  + dots([(30, 80), (40, 90), (58, 84), (70, 94), (86, 80), (96, 92), (44, 52), (54, 62), (72, 52), (84, 62)], "#fff", 2)
  + f(64, 86, d=6, k=0.45, blush=False) + f(49, 58, d=5, k=0.4, blush=False)),
 # 60 шоколадная монетка
 ("yellow", "шоколадная медаль в фольге", f'<circle cx="64" cy="64" r="40" fill="#FFC23D" {s()}/><circle cx="64" cy="64" r="30" fill="none" stroke="#D99A1E" stroke-width="3"/>'
  f'<path d="M86 34 Q100 40 104 56 L92 58 Q90 44 80 40Z" fill="#7A4A2A" {W(2.4)}/>' + f(62, 66, d=11, k=0.85) + sparkle(28, 30, 7)),
 # 61 монпансье в жестянке
 ("blue", "леденцы-монпансье в жестянке", f'<ellipse cx="64" cy="76" rx="46" ry="26" fill="#E8654F" {s()}/><ellipse cx="64" cy="68" rx="46" ry="24" fill="#F4F8FF" {s()}/>'
  + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}" {W(2)}/>' for x, y, c in
           [(40, 66, "#9DD6F5"), (56, 58, "#FFD25E"), (74, 58, "#FF8FB8"), (90, 66, "#7CD26E"), (64, 70, "#A98BF0")])
  + f'<path d="M24 22 Q64 2 104 22 L100 32 Q64 14 28 32Z" fill="#E8654F" {W(2.4)}/>' + f(64, 92, d=10, k=0.6).replace(O, "#3B3355")),
 # 62 ватрушка
 ("orange", "ватрушка", f'<ellipse cx="64" cy="70" rx="46" ry="32" fill="#E6A85A" {s()}/><ellipse cx="64" cy="64" rx="28" ry="18" fill="#FFF6DD" {W(2.6)}/>'
  + dots([(54, 60), (70, 58), (62, 68)], "#E8B04A", 2) + f(64, 86, d=12, k=0.6)),
 # 63 кулич
 ("purple", "кулич", f'<path d="M36 60 H92 V104 Q92 112 84 112 H44 Q36 112 36 104Z" fill="#E6A85A" {s()}/>'
  f'<path d="M30 62 Q24 32 64 26 Q104 32 98 62 Q96 54 88 60 Q80 52 72 60 Q64 52 56 60 Q48 52 40 60 Q32 54 30 62Z" fill="#FFFFFF" {s()}/>'
  + dots([(50, 40), (64, 34), (78, 42), (60, 46), (84, 52)], "#FF6B9B", 2.4) + dots([(56, 50), (72, 46)], "#FFD25E", 2.4) + f(64, 84, d=10, k=0.8)),
 # 64 тако
 ("yellow", "тако", f'<path d="M14 92 Q16 30 64 30 Q112 30 114 92Z" fill="#FFD25E" {s()}/>'
  f'<path d="M22 84 Q26 46 64 46 Q102 46 106 84" fill="none" stroke="#6CCB5F" stroke-width="8" stroke-linecap="round"/>'
  + dots([(36, 62), (54, 52), (76, 52), (94, 64)], "#F0503C", 5) + f(64, 76, d=11, k=0.8)),
 # 65 онигири
 ("sky", "онигири", f'<path d="M64 18 Q72 18 104 82 Q110 100 92 102 H36 Q18 100 24 82 Q56 18 64 18Z" fill="#FFFFFF" {s()}/>'
  f'<path d="M44 102 V76 Q44 70 50 70 H78 Q84 70 84 76 V102Z" fill="#2F3B3A" {W(2.6)}/>' + f(64, 54, d=10, k=0.8)),
 # 66 голубцы
 ("green", "голубцы на тарелке", f'<ellipse cx="64" cy="92" rx="52" ry="16" fill="#fff" {s()}/>'
  f'<path d="M24 84 Q20 58 44 54 Q62 52 62 76 Q62 92 42 92 Q28 92 24 84Z" fill="#C8EBA0" {s()}/><path d="M60 82 Q58 54 84 52 Q106 52 104 78 Q102 94 82 94 Q64 94 60 82Z" fill="#C8EBA0" {s()}/>'
  f'<path d="M30 70 Q42 62 56 68 M68 66 Q82 58 98 66" fill="none" stroke="#7CB85C" stroke-width="2.4"/>'
  f'<path d="M30 96 Q64 104 98 96" fill="none" stroke="#F0503C" stroke-width="4" opacity=".7"/>' + f(42, 78, d=6, k=0.5, blush=False) + f(84, 78, d=6, k=0.5, blush=False)),
 # 67 наггетсы
 ("orange", "наггетсы в коробочке", f'<path d="M24 62 H104 L96 112 H32Z" fill="#E8654F" {s()}/>'
  + "".join(f'<path d="M{x-14} {y} Q{x-16} {y-16} {x} {y-16} Q{x+16} {y-14} {x+14} {y} Q{x} {y+8} {x-14} {y}Z" fill="#F2B45A" {W(2.4)}/>' for x, y in [(44, 60), (64, 52), (84, 60)])
  + f(64, 86, d=10, k=0.75).replace(O, "#3B3355")),
 # 68 луковые кольца
 ("purple", "луковые кольца", f'<ellipse cx="50" cy="76" rx="30" ry="22" fill="none" stroke="{O}" stroke-width="17"/><ellipse cx="50" cy="76" rx="30" ry="22" fill="none" stroke="#F2B45A" stroke-width="11"/>'
  f'<ellipse cx="80" cy="50" rx="26" ry="20" fill="none" stroke="{O}" stroke-width="17" transform="rotate(-15 80 50)"/><ellipse cx="80" cy="50" rx="26" ry="20" fill="none" stroke="#F2B45A" stroke-width="11" transform="rotate(-15 80 50)"/>'
  + f(50, 98, d=8, k=0.55)),
 # 69 пачка чипсов
 ("blue", "пачка чипсов", f'<path d="M30 16 H98 L92 30 Q100 64 92 98 L98 112 H30 L36 98 Q28 64 36 30Z" fill="#FFD25E" {s()}/>'
  f'<path d="M34 24 H94 M34 104 H94" stroke="{O}" stroke-width="2" stroke-dasharray="3 4"/>'
  f'<path d="M50 84 Q64 72 78 84 Q72 96 64 94 Q56 96 50 84Z" fill="#F2B45A" {W(2.2)}/>' + f(64, 56, d=11, k=0.8)),
 # 70 лазанья
 ("orange", "кусочек лазаньи", f'<path d="M24 50 L94 34 L104 54 V96 L34 112 L24 92Z" fill="#FFE08A" {s()}/>'
  f'<path d="M24 66 L104 64 M24 80 L104 78" stroke="#E8654F" stroke-width="5"/><path d="M24 50 L94 34 L104 54 L34 70Z" fill="#F2B45A" {s()}/>'
  + dots([(50, 52), (70, 46), (84, 54)], "#E8654F", 3) + leaf(58, 50, -30) + f(66, 94, d=10, k=0.65)),
 # 71 палка колбасы
 ("pink", "палка колбасы с кружочками", f'<rect x="14" y="44" width="80" height="34" rx="17" fill="#C8434E" {s()}/><path d="M14 61 L4 56 M94 61 L102 54" {W(3)}/>'
  f'<circle cx="96" cy="90" r="18" fill="#F29BA2" {s()}/>' + dots([(90, 86), (100, 94), (96, 82)], "#fff", 2.2) + dots([(30, 54), (48, 64), (66, 52), (80, 66)], "#F29BA2", 2.4)
  + f(52, 58, d=9, k=0.7).replace(O, "#fff")),
 # 72 бекон
 ("yellow", "полоска бекона", f'<path d="M16 78 Q30 50 46 70 Q62 90 78 66 Q94 42 112 58 L116 74 Q98 62 84 84 Q66 108 48 86 Q32 66 20 94Z" fill="#E8654F" {s()}/>'
  f'<path d="M18 86 Q32 60 47 78 Q63 98 81 74 Q96 52 114 66" fill="none" stroke="#FFD8C4" stroke-width="5"/>' + f(64, 60, d=9, k=0.65, blush=False)),
 # 73 окорок
 ("orange", "окорок на косточке", f'<path d="M60 70 L94 104" stroke="{O}" stroke-width="16" stroke-linecap="round"/><path d="M60 70 L94 104" stroke="#fff" stroke-width="10" stroke-linecap="round"/>'
  f'<circle cx="100" cy="102" r="8" fill="#fff" {s()}/><circle cx="106" cy="94" r="8" fill="#fff" {s()}/>'
  f'<path d="M22 50 Q22 18 52 18 Q86 20 82 52 Q78 82 46 84 Q20 82 22 50Z" fill="#E87A6A" {s()}/><path d="M30 46 Q36 28 54 26" fill="none" stroke="#fff" stroke-width="4" opacity=".6"/>'
  + f(52, 54, d=10, k=0.8)),
 # 74 багет
 ("sky", "багет", f'<path d="M26 108 Q12 98 24 84 L84 22 Q96 12 106 22 Q116 34 104 44 L44 106 Q34 116 26 108Z" fill="#E6A85A" {s()}/>'
  f'<path d="M44 76 L56 82 M60 60 L72 66 M76 44 L88 50" stroke="#B5762A" stroke-width="4" stroke-linecap="round"/>' + f(56, 84, d=8, k=0.6)),
 # 75 губка
 ("blue", "губка для посуды", f'<path d="M20 60 L96 40 L110 56 L34 78Z" fill="#6CCB5F" {s()}/><path d="M34 78 L110 56 V82 L34 104Z" fill="#FFD25E" {s()}/>'
  f'<path d="M20 60 L34 78 V104 L20 86Z" fill="#E6B83A" {s()}/>' + dots([(50, 88), (66, 80), (88, 76), (96, 66)], "#E6B83A", 2.4)
  + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".9" {W(2)}/>' for x, y, r in [(40, 40, 6), (56, 28, 8), (74, 34, 5), (28, 24, 4)])
  + f(72, 82, d=9, k=0.65)),
 # 76 кочан капусты
 ("teal", "кочан капусты", f'<circle cx="64" cy="68" r="42" fill="#A8DE8A" {s()}/><path d="M28 50 Q64 20 100 50 M24 70 Q40 48 64 56 Q88 48 104 70" fill="none" stroke="#6CB85C" stroke-width="3"/>'
  f'<path d="M64 26 V110 M44 34 Q36 70 50 104 M84 34 Q92 70 78 104" fill="none" stroke="#E7F7DA" stroke-width="3"/>' + f(64, 80, d=11, k=0.85)),
 # 77 спаржа
 ("purple", "пучок спаржи", "".join(f'<path d="M{x} 112 L{x+d} 30" stroke="{O}" stroke-width="13" stroke-linecap="round"/><path d="M{x} 112 L{x+d} 30" stroke="#7CC274" stroke-width="8" stroke-linecap="round"/><path d="M{x+d-6} 34 L{x+d} 18 L{x+d+6} 34Z" fill="#5E9E5A" {W(2.2)}/>' for x, d in [(44, -8), (64, 0), (84, 8)])
  + f'<rect x="34" y="70" width="60" height="14" rx="4" fill="#E8654F" {W(2.6)}/>' + f(64, 96, d=10, k=0.6)),
 # 78 питахайя
 ("pink", "питахайя (драконий фрукт)", f'<ellipse cx="64" cy="70" rx="38" ry="42" fill="#F2477E" {s()}/>'
  + "".join(f'<path d="M{x} {y} q{dx} -10 {dx*2} -18 q-4 12 -{dx*2-4} 18Z" fill="#7CD26E" {W(2.2)}/>' for x, y, dx in [(34, 54, -6), (94, 54, 6), (40, 88, -6), (88, 88, 6), (56, 32, -4), (72, 32, 4)])
  + f(64, 74, d=12, k=0.85)),
 # 79 тюбик сгущёнки
 ("yellow", "тюбик сгущёнки", f'<path d="M40 30 H88 L80 104 H48Z" fill="#9DD6F5" {s()}/><path d="M38 24 H90 V32 H38Z" fill="#7FB8E0" {W(2.4)}/>'
  f'<path d="M54 104 H74 V114 H54Z" fill="#fff" {W(2.4)}/><path d="M60 114 H68 Q66 122 64 124 Q62 122 60 114Z" fill="#FFF6DD" {W(2)}/>'
  f'<rect x="48" y="62" width="32" height="18" rx="4" fill="#fff" {W(2)}/>' + f(64, 48, d=8, k=0.6)),
 # 80 коробка хлопьев
 ("blue", "коробка хлопьев", f'<path d="M30 20 H90 L98 28 V112 H38 L30 104Z" fill="#FFB347" {s()}/><path d="M90 20 V104 H30 M90 104 L98 112" fill="none" {W(2.6)}/>'
  f'<ellipse cx="60" cy="84" rx="20" ry="8" fill="#fff" {W(2.4)}/>' + dots([(52, 82), (60, 80), (68, 84)], "#E8A04A", 3.4) + f(60, 50, d=10, k=0.8)),
 # 81 бутылка кетчупа
 ("green", "бутылка кетчупа", f'<path d="M40 50 Q40 34 56 32 H72 Q88 34 88 50 V104 Q88 112 80 112 H48 Q40 112 40 104Z" fill="#E33B3B" {s()}/>'
  f'<path d="M54 32 L56 20 H72 L74 32Z" fill="#fff" {W(2.6)}/><path d="M60 20 L62 10 H66 L68 20" fill="#fff" {W(2.2)}/>'
  f'<rect x="46" y="62" width="36" height="24" rx="5" fill="#fff" {W(2.4)}/>' + f(64, 72, d=8, k=0.55)),
 # 82 ваниль
 ("purple", "ваниль (стручок и цветок)", f'<path d="M30 110 Q50 70 98 26" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round"/><path d="M30 110 Q50 70 98 26" fill="none" stroke="#5A3A2A" stroke-width="6" stroke-linecap="round"/>'
  + "".join(f'<ellipse cx="78" cy="78" rx="9" ry="20" fill="#FFF3C4" {W(2.4)} transform="rotate({r} 78 78) translate(0 -16)"/>' for r in (0, 72, 144, 216, 288))
  + f'<circle cx="78" cy="78" r="8" fill="#FFD25E" {W(2.2)}/>' + f(78, 78, d=0.1, k=0.0001, blush=False, mouth=False) + eye(75, 77, 0.35) + eye(81, 77, 0.35)),
 # 83 палочки корицы
 ("orange", "палочки корицы", "".join(f'<g transform="rotate({r} 64 64)"><rect x="24" y="{y}" width="80" height="18" rx="9" fill="#B5662A" {s()}/><ellipse cx="102" cy="{y+9}" rx="5" ry="8" fill="#E6A85A" {W(2.2)}/><path d="M102 {y+5} q-4 4 0 8" fill="none" stroke="#7A3E14" stroke-width="2"/></g>' for r, y in [(-18, 40), (0, 56), (18, 72)])
  + f'<rect x="54" y="48" width="14" height="44" rx="3" fill="#E8654F" {W(2.4)}/>' + f(40, 66, d=7, k=0.55)),
 # 84 имбирь
 ("yellow", "корень имбиря", f'<path d="M20 76 Q22 56 40 58 Q42 38 60 40 Q66 22 82 30 Q96 36 90 52 Q108 56 106 74 Q104 94 84 92 Q76 108 58 102 Q40 106 36 92 Q18 92 20 76Z" fill="#E6C08A" {s()}/>'
  f'<path d="M50 64 q6 4 12 0 M72 54 q6 4 12 0 M66 86 q6 4 12 0" fill="none" stroke="#B88A45" stroke-width="2.4"/>' + f(62, 72, d=10, k=0.75)),
 # 85 оливковое масло
 ("teal", "бутылка оливкового масла", f'<path d="M52 12 H76 V24 H52Z" fill="#3B3355"/><path d="M54 24 H74 V40 Q90 50 90 68 V106 Q90 114 82 114 H46 Q38 114 38 106 V68 Q38 50 54 40Z" fill="#C8D94A" {s()}/>'
  f'<path d="M40 70 H88 V104 H40Z" fill="#FFF8E0" {W(2.4)}/><ellipse cx="64" cy="82" rx="8" ry="5" fill="#6B8E23" {W(2)}/>' + leaf(68, 80, -20) + f(64, 56, d=8, k=0.55)),
 # 86 нож для пиццы
 ("orange", "нож-ролик для пиццы", f'<path d="M70 70 L104 104" stroke="{O}" stroke-width="14" stroke-linecap="round"/><path d="M70 70 L104 104" stroke="#E8654F" stroke-width="9" stroke-linecap="round"/>'
  f'<circle cx="56" cy="56" r="34" fill="#DDE4EE" {s()}/><circle cx="56" cy="56" r="8" fill="#A9B4C6" {W(2.4)}/>' + f(56, 40, d=8, k=0.6, blush=False)
  + f'<path d="M14 116 L40 94 L52 116Z" fill="#FFD25E" {W(2.4)}/>' + dots([(36, 106)], "#E8654F", 3)),
 # 87 бочонок кваса
 ("orange", "бочонок кваса с краником", f'<path d="M30 24 Q22 64 30 104 H98 Q106 64 98 24Z" fill="#C98A52" {s()}/>'
  f'<path d="M26 44 H102 M26 84 H102" stroke="{O}" stroke-width="4"/><path d="M98 64 H112 V72" fill="none" {W(4)}/>' + dots([(112, 82)], "#8A4A24", 3)
  + f(64, 62, d=10, k=0.8)),
 # 88 детская тарелка с секциями
 ("sky", "детская тарелка с отделениями", f'<circle cx="64" cy="66" r="48" fill="#FFB3CF" {s()}/><circle cx="64" cy="66" r="40" fill="#FFE1EC" {W(2.4)}/>'
  f'<path d="M64 26 V66 L30 86 M64 66 L98 86" fill="none" stroke="#FFB3CF" stroke-width="6"/>'
  f'<circle cx="46" cy="50" r="8" fill="#FF9A3C" {W(2)}/><rect x="74" y="42" width="14" height="14" rx="3" fill="#7CD26E" {W(2)}/>' + f(64, 92, d=9, k=0.6)),
 # 89 чак-чак
 ("yellow", "чак-чак", f'<path d="M20 98 Q64 118 108 98 L104 110 Q64 126 24 110Z" fill="#fff" {s()}/>'
  f'<path d="M26 98 Q30 40 64 30 Q98 40 102 98 Q64 108 26 98Z" fill="#F2B45A" {s()}/>'
  + "".join(f'<path d="M{x} {y} q6 -4 10 0" fill="none" stroke="#C47A2A" stroke-width="2.4"/>' for x, y in [(40, 70), (56, 56), (72, 60), (82, 78), (46, 88), (62, 80)])
  + dots([(64, 40), (54, 48), (76, 50)], "#E8336A", 2.6) + f(64, 76, d=11, k=0.8)),
 # 90 сушилка с тарелками
 ("blue", "сушилка для посуды с тарелками", f'<path d="M14 98 H114 L108 110 H20Z" fill="#9DD6F5" {s()}/>'
  + "".join(f'<ellipse cx="{x}" cy="64" rx="11" ry="34" fill="{c}" {s()}/>' for x, c in [(36, "#fff"), (58, "#FFE08A"), (80, "#fff"), (100, "#C8F0E0")])
  + f'<path d="M18 92 H110" {W(3)}/>' + f(58, 64, d=4, k=0.4, blush=False) + sparkle(20, 28, 7)),
 # 91 баночки специй
 ("orange", "баночки специй на полочке", f'<rect x="12" y="96" width="104" height="10" rx="3" fill="#8A5A3A" {s()}/>'
  + "".join(f'<rect x="{x}" y="50" width="24" height="46" rx="6" fill="#F4FBFF" {W(2.6)}/><rect x="{x+2}" y="66" width="20" height="28" rx="4" fill="{c}"/><rect x="{x-2}" y="42" width="28" height="10" rx="3" fill="#3B3355"/>' for x, c in [(18, "#E8654F"), (52, "#FFC23D"), (86, "#7CB85C")])
  + f(64, 76, d=5, k=0.45, blush=False)),
 # 92 хохломская ложка
 ("night", "хохломская деревянная ложка", f'<path d="M58 60 L46 118 Q46 122 52 122 L60 120 L68 62Z" fill="#E8654F" {s()}/>'
  f'<ellipse cx="66" cy="38" rx="26" ry="30" fill="#E8654F" {s()}/><ellipse cx="66" cy="38" rx="18" ry="22" fill="#FFC23D" {W(2.4)}/>'
  f'<path d="M50 112 q6 -10 10 -2 M54 92 q6 -10 10 -2" fill="none" stroke="#FFC23D" stroke-width="2.6"/>' + f(66, 38, d=7, k=0.6)),
 # 93 туесок
 ("green", "берестяной туесок", f'<path d="M34 34 H94 V104 Q94 112 86 112 H42 Q34 112 34 104Z" fill="#F4ECDD" {s()}/>'
  f'<path d="M34 44 H94 M34 100 H94" {W(3)}/><path d="M40 60 h10 M58 70 h12 M78 58 h8 M46 84 h8 M70 88 h12" stroke="#3B3355" stroke-width="2.4" stroke-linecap="round"/>'
  f'<rect x="30" y="22" width="68" height="14" rx="5" fill="#C9A27A" {s()}/><path d="M58 22 Q64 10 70 22" fill="none" {W(3)}/>' + f(64, 74, d=10, k=0.7)),
 # 94 йогурт
 ("pink", "стаканчик йогурта", f'<path d="M30 34 H98 L88 110 H40Z" fill="#FFFFFF" {s()}/><path d="M34 62 H94 L90 90 H38Z" fill="#FF8FB8" {W(2.4)}/>'
  f'<path d="M26 34 H102 Q104 24 90 24 H38 Q24 24 26 34Z" fill="#C9D3E0" {s()}/><path d="M94 26 Q108 14 112 26" fill="#C9D3E0" {W(2.4)}/>'
  f'<circle cx="64" cy="76" r="7" fill="#E8336A" {W(2)}/>' + f(64, 48, d=9, k=0.6)),
 # 95 фисташки
 ("teal", "фисташки", "".join(f'<g transform="rotate({r} {x} {y})"><path d="M{x-16} {y} Q{x-16} {y-22} {x} {y-24} Q{x+16} {y-22} {x+16} {y} Q{x+16} {y+20} {x} {y+22} Q{x-16} {y+20} {x-16} {y}Z" fill="#F2E3C2" {W(2.6)}/><path d="M{x-6} {y-16} Q{x} {y-22} {x+6} {y-16} V{y+10} Q{x} {y+14} {x-6} {y+10}Z" fill="#9BCB5A" {W(2)}/></g>' for x, y, r in [(42, 72, -20), (86, 72, 20), (64, 50, 0)])
  + f(64, 50, d=0.1, k=0.0001, blush=False, mouth=False) + eye(60, 46, 0.35) + eye(68, 46, 0.35) + f(64, 96, d=9, k=0.55, mouth=True, blush=True).replace(O, O)),
 # 96 сельдерей
 ("green", "пучок сельдерея", "".join(f'<path d="M{x} 116 Q{x+d} 70 {x+d*2} 40" fill="none" stroke="{O}" stroke-width="15" stroke-linecap="round"/><path d="M{x} 116 Q{x+d} 70 {x+d*2} 40" fill="none" stroke="#A8DE8A" stroke-width="10" stroke-linecap="round"/>' for x, d in [(50, -6), (64, 0), (78, 6)])
  + leaf(36, 34, -60) + leaf(56, 26, -20) + leaf(78, 30, 20) + leaf(96, 38, 50) + f(64, 88, d=11, k=0.65)),
 # 97 пачка сливочного масла
 ("sky", "пачка сливочного масла", f'<path d="M18 62 L74 44 L112 58 L56 78Z" fill="#FFF0A0" {s()}/><path d="M18 62 L56 78 V104 L18 88Z" fill="#FFE066" {s()}/>'
  f'<path d="M56 78 L112 58 V84 L56 104Z" fill="#7FB8E0" {s()}/><path d="M60 86 L108 68" stroke="#fff" stroke-width="4"/>'
  f'<path d="M48 34 Q60 22 72 32" fill="none" stroke="#fff" stroke-width="3"/>' + f(37, 80, d=7, k=0.5, blush=False)),
 # 98 маршмеллоу на палочке
 ("night", "маршмеллоу на палочке", f'<path d="M40 120 L84 20" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M40 120 L84 20" stroke="#C98A52" stroke-width="3.5" stroke-linecap="round"/>'
  + "".join(f'<rect x="{x-14}" y="{y-11}" width="28" height="22" rx="8" fill="{c}" {s()} transform="rotate(-24 {x} {y})"/>' for x, y, c in [(76, 38, "#FFFFFF"), (66, 62, "#FFC6DA"), (56, 86, "#FFFFFF")])
  + f(66, 62, d=5, k=0.42, blush=False) + sparkle(28, 34, 7) + sparkle(100, 92, 5)),
 # 99 кухонные ножницы
 ("yellow", "кухонные ножницы", f'<path d="M58 66 L96 14 L102 18 L66 72Z" fill="#DDE4EE" {s()}/><path d="M70 66 L32 14 L26 18 L62 72Z" fill="#DDE4EE" {s()}/>'
  f'<circle cx="64" cy="68" r="4" fill="#3B3355"/><path d="M60 72 Q40 74 38 94 Q38 112 52 110 Q64 106 62 76Z" fill="#E8654F" {s()}/>'
  f'<path d="M68 72 Q88 74 90 94 Q90 112 76 110 Q64 106 66 76Z" fill="#E8654F" {s()}/><ellipse cx="50" cy="96" rx="5" ry="7" fill="#FFF6C4" {W(2)}/><ellipse cx="78" cy="96" rx="5" ry="7" fill="#FFF6C4" {W(2)}/>'
  + eye(56, 44, 0.45) + eye(72, 44, 0.45)),
 # 100 этажерка для пирожных
 ("pink", "трёхъярусная этажерка с пирожными", f'<path d="M64 12 V112" {W(4)}/><circle cx="64" cy="10" r="5" fill="#FFD25E" {W(2)}/>'
  + "".join(f'<ellipse cx="64" cy="{y}" rx="{r}" ry="5" fill="#fff" {s()}/>' for y, r in [(42, 22), (72, 34), (106, 46)])
  + f'<rect x="50" y="30" width="12" height="10" rx="3" fill="#FF8FB8" {W(2)}/><rect x="40" y="58" width="14" height="12" rx="3" fill="#FFE08A" {W(2)}/><rect x="74" y="58" width="14" height="12" rx="3" fill="#A98BF0" {W(2)}/>'
  + f'<circle cx="34" cy="96" r="7" fill="#E0A55E" {W(2)}/><circle cx="94" cy="96" r="7" fill="#7CD26E" {W(2)}/>' + f(64, 88, d=8, k=0.55)),
 # 101 столовые приборы
 ("teal", "вилка, ложка и нож", f'<path d="M30 24 V48 Q30 58 40 58 V114 M40 24 V48 M50 24 V48 Q50 58 40 58" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>'
  f'<path d="M30 24 V48 Q30 58 40 58 V114 M40 24 V48 M50 24 V48 Q50 58 40 58" fill="none" stroke="#DDE4EE" stroke-width="4" stroke-linecap="round"/>'
  f'<ellipse cx="66" cy="38" rx="12" ry="18" fill="#DDE4EE" {s()}/><path d="M66 56 V114" stroke="{O}" stroke-width="8" stroke-linecap="round"/><path d="M66 56 V114" stroke="#DDE4EE" stroke-width="4" stroke-linecap="round"/>'
  f'<path d="M92 114 V22 Q104 30 104 64 H94" fill="#DDE4EE" {s()}/>' + f(66, 38, d=5, k=0.45, blush=False)),
 # 102 салфетница
 ("purple", "салфетница с салфетками", f'<path d="M40 30 L64 60 L88 30 M46 26 L66 58 L90 36" fill="#fff" {W(2.6)}/>'
  f'<path d="M24 60 H104 V104 Q104 110 98 110 H30 Q24 110 24 104Z" fill="#7CD26E" {s()}/>' + f(64, 84, d=12, k=0.85)),
 # 103 табличка «Резерв»
 ("orange", "табличка «Резерв» на столе", f'<path d="M12 100 H116" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
  f'<path d="M26 98 L44 30 H84 L102 98Z" fill="#FFF3D6" {s()}/><path d="M52 44 H76" stroke="#E8654F" stroke-width="4" stroke-linecap="round"/>'
  f'<circle cx="64" cy="36" r="0" /><path d="M58 88 L64 82 L70 88" fill="none" stroke="#E8654F" stroke-width="3"/>' + f(64, 64, d=10, k=0.8) + sparkle(106, 30, 7)),
]

DATA = json.load(open(os.path.join(here, "cafes_1106_data.json")))
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
