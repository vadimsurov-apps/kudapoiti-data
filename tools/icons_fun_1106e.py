"""Иконки робота fun (2026-11-06, ночь): 74 новых сюжета — музеи, парки, кинотеатры, ДК и театры, батуты, фермы
городов Подмосковья. Якоря: кино — экран с креслами; ДК/театр — сцена с занавесом; батуты — батут с прыгуном;
музей — экспонат по теме. Сверено с icons-catalog/sheet-*.png и icons-src/subjects.txt.
Запуск: python3 tools/icons_fun_1106e.py [id ...]"""
import os, sys
from draw_icons import svg, s, eye, face, sparkle, O
from icons_fun_1106d import (W, f, R, OR, Y, G, B, P, V, BR, WH, GR, DG, SK, TE, DB, NV, GO, sp, GROUND, WATER, kid,
                             tramp)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
SIL = "#D9DEEA"


# ---------- кино: экран-персонаж + ряд кресел ----------
def screen(inner, cur=R):
    return (f'<path d="M0 6 H128 V20 Q96 30 64 22 Q32 30 0 20Z" fill="{cur}" {s()}/>'
            f'<rect x="16" y="26" width="96" height="62" rx="6" fill="#fff" {s()}/>'
            f'<rect x="22" y="32" width="84" height="50" rx="3" fill="#E8F6FF"/>'
            + inner
            + "".join(f'<path d="M{x} 124 V106 Q{x} 98 {x+8} 98 H{x+12} Q{x+20} 98 {x+20} 106 V124Z" fill="{R}" {W(2.4)}/>'
                      for x in (8, 32, 56, 80, 104)))


# ---------- сцена: занавес + доски ----------
def stage(char, cur=R):
    return (f'<rect x="0" y="100" width="128" height="28" fill="#D9A066" {s()}/>'
            f'<path d="M0 108 H128 M0 118 H128" stroke="#B57A42" stroke-width="2"/>'
            + char
            + f'<path d="M0 0 H30 Q26 50 34 100 H0Z" fill="{cur}" {s()}/><path d="M128 0 H98 Q102 50 94 100 H128Z" fill="{cur}" {s()}/>'
            f'<path d="M0 0 H128 V14 Q112 22 96 14 Q80 22 64 14 Q48 22 32 14 Q16 22 0 14Z" fill="{cur}" {s()}/>'
            f'<path d="M10 20 Q14 60 12 96 M116 20 Q112 60 114 96" stroke="#B83A2A" stroke-width="3" fill="none"/>'
            f'<circle cx="34" cy="60" r="4" fill="{GO}" {W(2)}/><circle cx="94" cy="60" r="4" fill="{GO}" {W(2)}/>')


def blob(cx, cy, rx, ry, col, d=8, k=0.7):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{col}" {s()}/>' + f(cx, cy, d=d, k=k)


I = {}
# ======================= Клин =======================
I["klin-kraeved-museum"] = ("orange", "глиняный горшок с монетами выглядывает из раскопа, рядом кисточка археолога",
    f'<path d="M0 78 Q64 70 128 78 V128 H0Z" fill="#B9874F" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="#8A5E30"/>' for x, y in [(14, 100), (30, 116), (104, 110), (118, 94), (20, 86)])
    + f'<path d="M36 52 Q36 40 46 38 H82 Q92 40 92 52 Q100 96 64 100 Q28 96 36 52Z" fill="#D9824A" {s()}/>'
    f'<path d="M40 40 H88" stroke="#8A4A26" stroke-width="5"/>'
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="4" fill="{GO}" {W(2)}/>' for x, y in [(52, 34), (68, 30), (76, 36)])
    + f(64, 70, d=10, k=0.8)
    + f'<g transform="rotate(35 106 50)"><rect x="102" y="20" width="8" height="36" rx="3" fill="{BR}" {W(2.2)}/>'
    f'<path d="M100 56 H112 L114 72 H98Z" fill="{Y}" {W(2.2)}/></g>' + sp((18, 30, 6)))
I["klin-gaidar-house"] = ("sky", "голубятня Тимура: белый голубь машет крылом на крыше",
    f'<rect x="60" y="80" width="8" height="48" fill="{BR}" {W(2.4)}/>'
    f'<rect x="36" y="48" width="56" height="38" rx="3" fill="{B}" {s()}/><path d="M30 50 L64 28 L98 50Z" fill="{R}" {s()}/>'
    + "".join(f'<rect x="{x}" y="58" width="12" height="14" rx="6" fill="{NV}"/>' for x in (44, 72))
    + f'<path d="M36 76 H92" stroke="#fff" stroke-width="3"/>'
    + f'<ellipse cx="64" cy="20" rx="16" ry="11" fill="#fff" {s()}/><circle cx="76" cy="12" r="8" fill="#fff" {s()}/>'
    f'<path d="M84 12 l6 2 l-6 2Z" fill="{OR}" {W(1.6)}/>' + eye(78, 11, 0.5)
    + f'<path d="M58 14 Q48 -4 38 6 Q46 14 58 20Z" fill="#fff" {W(2.4)}/>' + sp((112, 30, 6), (16, 36, 5)))
I["klin-karapaev-hall"] = ("yellow", "старинный ткацкий станок-персонаж ткёт полосатый половичок",
    f'<path d="M24 20 V120 M104 20 V120" stroke="{BR}" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M24 20 V120 M104 20 V120" {W(2)}/><rect x="18" y="16" width="92" height="12" rx="4" fill="#D9A066" {s()}/>'
    + "".join(f'<path d="M{x} 28 V66" stroke="#fff" stroke-width="1.6"/>' for x in range(34, 96, 6))
    + f'<rect x="28" y="66" width="72" height="44" fill="#fff" {s()}/>'
    + "".join(f'<rect x="28" y="{y}" width="72" height="7" fill="{c}"/>' for y, c in [(70, R), (84, B), (98, G)])
    + f'<rect x="28" y="66" width="72" height="44" fill="none" {s()}/>'
    + f'<rect x="38" y="40" width="52" height="20" rx="8" fill="#D9A066" {s()}/>' + f(64, 48, d=9, k=0.6) + sp((114, 116, 4)))
I["klin-sestroretsky-park"] = ("green", "дерево-персонаж с качелей-шиной над речкой",
    f'<path d="M0 104 Q32 96 64 104 T128 104 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'
    f'<path d="M40 104 Q44 70 40 50 H56 Q52 70 58 104Z" fill="{BR}" {s()}/>'
    f'<circle cx="48" cy="36" r="30" fill="{DG}" {s()}/><circle cx="26" cy="52" r="14" fill="{DG}" {s()}/>'
    + f(48, 38, d=10, k=0.8)
    + f'<path d="M70 44 H104 M96 44 V78" {W(3)}/><path d="M70 44 Q74 40 78 44" fill="none" {W(3)}/>'
    f'<ellipse cx="96" cy="86" rx="12" ry="9" fill="{NV}" {s()}/><ellipse cx="96" cy="86" rx="5" ry="3.5" fill="#B9E8A8"/>'
    + sp((112, 20, 6)))
I["klin-aero-park"] = ("sky", "самолётик-персонаж прыгает на батуте", tramp(
    f'<g transform="rotate(-12 64 60)"><path d="M30 62 Q30 50 44 50 H92 Q104 50 106 60 Q104 70 92 70 H44 Q30 70 30 62Z" fill="#fff" {s()}/>'
    f'<path d="M58 52 L46 26 H58 L74 52Z M58 68 L48 86 H60 L72 68Z" fill="{R}" {s()}/><path d="M34 54 L26 40 H34 L42 52Z" fill="{R}" {W(2.4)}/>'
    + f(86, 60, d=6, k=0.55) + '</g>', col=Y) + sp((112, 24, 6), (18, 26, 5)))
I["klin-silver-cinema"] = ("night", "киноэкран, на экране серебряный ёлочный шар улыбается", screen(
    f'<path d="M64 32 V40" {W(2)}/><rect x="58" y="38" width="12" height="7" rx="2" fill="{GO}" {W(2)}/>'
    f'<circle cx="64" cy="62" r="18" fill="{SIL}" {s()}/><path d="M48 58 Q64 64 80 58" fill="none" stroke="#9AA6C8" stroke-width="3"/>'
    + f(64, 64, d=7, k=0.55) + sp((90, 44, 5), (36, 74, 4))))
I["klin-izumrudny-les"] = ("teal", "лама в изумрудной шапочке на сафари",
    f'<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="{G}" {W(2.6)}/>'
    f'<path d="M40 128 V92 Q40 76 56 76 H72 Q88 76 88 92 V128Z" fill="#F4E4C8" {s()}/>'
    f'<path d="M50 80 V44 Q50 30 64 30 Q78 30 78 44 V80Z" fill="#F4E4C8" {s()}/>'
    f'<path d="M52 30 L48 12 L58 24Z M76 30 L80 12 L70 24Z" fill="#F4E4C8" {s()}/>'
    + f(64, 50, d=7, k=0.6)
    + f'<ellipse cx="64" cy="62" rx="7" ry="5" fill="#E7C9A4" {W(2)}/>'
    f'<path d="M48 32 Q64 10 80 32Z" fill="#1FAF7A" {W(2.4)}/><circle cx="64" cy="14" r="5" fill="#1FAF7A" {W(2)}/>'
    + "".join(sparkle(x, y, r, "#B8F5D8") for x, y, r in [(20, 30, 6), (108, 36, 5)]))

# ======================= Фрязино =======================
I["fryazino-golografiya"] = ("night", "радужная голограмма-звёздочка парит над прожектором",
    f'<path d="M40 112 L54 70 H74 L88 112Z" fill="#9AA0C8" opacity=".35"/>'
    f'<rect x="44" y="104" width="40" height="18" rx="4" fill="{GR}" {s()}/><circle cx="64" cy="104" r="8" fill="#BFE8FF" {W(2.4)}/>'
    + "".join(f'<path d="M64 14 L74 38 L100 40 L80 56 L86 82 L64 68 L42 82 L48 56 L28 40 L54 38Z" fill="none" stroke="{c}" stroke-width="3" transform="translate({dx} {dy})" opacity=".8"/>'
              for c, dx, dy in [("#FF7FA8", -3, 0), ("#7FE3FF", 3, 0)])
    + f'<path d="M64 14 L74 38 L100 40 L80 56 L86 82 L64 68 L42 82 L48 56 L28 40 L54 38Z" fill="#FFF3A8" {s()} opacity=".95"/>'
    + f(64, 50, d=8, k=0.65) + sp((18, 24, 5), (110, 22, 6), (108, 90, 4)))
I["fryazino-dk-istok"] = ("blue", "капелька-родничок выходит на сцену с поклоном", stage(
    f'<path d="M64 30 Q86 62 86 76 Q86 98 64 98 Q42 98 42 76 Q42 62 64 30Z" fill="#7FD3F7" {s()}/>'
    f'<ellipse cx="56" cy="64" rx="4" ry="7" fill="#fff" opacity=".7"/>' + f(64, 78, d=8, k=0.6), cur=B))
I["fryazino-kids-lab"] = ("purple", "мышка в защитных очках бежит по игровому лабиринту к сыру",
    f'<rect x="12" y="12" width="104" height="104" rx="10" fill="#fff" {s()}/>'
    f'<path d="M12 40 H76 M100 40 V84 M40 64 H100 M40 64 V96 M70 88 H116 M12 92 H22" stroke="{V}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M92 18 L112 22 L104 34Z" fill="{Y}" {W(2.2)}/><circle cx="102" cy="26" r="1.8" fill="#E2A92A"/>'
    f'<g transform="translate(-14 -18) scale(1.25)"><ellipse cx="62" cy="100" rx="16" ry="10" fill="{GR}" {s()}/><circle cx="50" cy="90" r="7" fill="{GR}" {W(2.4)}/>'
    f'<circle cx="74" cy="90" r="7" fill="{GR}" {W(2.4)}/><circle cx="50" cy="90" r="3.5" fill="{P}"/><circle cx="74" cy="90" r="3.5" fill="{P}"/>'
    f'<rect x="51" y="94" width="22" height="9" rx="4" fill="#9AD6FF" {W(2)}/>' + eye(57, 98.5, 0.45) + eye(67, 98.5, 0.45)
    + f'<path d="M78 104 Q96 110 98 98" fill="none" {W(2.4)}/></g>')
I["fryazino-grand-cinema"] = ("green", "киноэкран, на экране динозаврик машет лапкой", screen(
    f'<path d="M34 80 Q34 56 52 54 Q60 40 72 42 Q86 44 84 58 Q82 66 72 66 V80Z" fill="{G}" {s()}/>'
    f'<path d="M34 76 Q24 76 22 66" fill="none" {W(3)}/>' + f(74, 52, d=5, k=0.5)
    + "".join(f'<path d="M{x} {y} l3 -6 l3 6" fill="{DG}" {W(1.6)}/>' for x, y in [(44, 56), (52, 50), (60, 44)])
    + f'<path d="M84 60 Q94 54 92 44" fill="none" {W(3)}/>' + sp((96, 70, 4))))

# ======================= Щёлково =======================
I["shchelkovo-central-park"] = ("green", "дорожный знак «пешеходный переход»-персонаж в автогородке",
    GROUND + f'<path d="M20 112 L108 112" stroke="{NV}" stroke-width="14"/>'
    + "".join(f'<rect x="{x}" y="106" width="8" height="12" fill="#fff"/>' for x in range(26, 108, 16))
    + f'<rect x="60" y="62" width="8" height="46" fill="{GR}" {W(2.4)}/>'
    f'<rect x="30" y="10" width="68" height="62" rx="8" fill="{B}" {s()}/><path d="M38 66 L64 18 L90 66Z" fill="#fff" {s()}/>'
    f'<circle cx="64" cy="34" r="5" fill="{NV}"/><path d="M64 40 L60 52 L54 60 M62 46 L70 50 M60 52 L68 60" stroke="{NV}" stroke-width="3.2" stroke-linecap="round" fill="none"/>'
    + f(64, 82, d=8, k=0.55).replace("cy=\"82", "cy=\"82") + sp((18, 30, 5), (112, 28, 6)))
I["shchelkovo-museum"] = ("pink", "гусеничка-шелкопряд прядёт шёлк на катушку (Щёлково — «шёлковый» город)",
    f'<rect x="76" y="54" width="36" height="48" rx="4" fill="#D9A066" {s()}/><rect x="80" y="62" width="28" height="32" fill="#FFF0F6" {W(2)}/>'
    + "".join(f'<path d="M80 {y} H108" stroke="{P}" stroke-width="2.4"/>' for y in range(66, 94, 5))
    + f'<path d="M58 70 Q70 60 80 70" fill="none" stroke="{P}" stroke-width="2"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="#FFF4D6" {s()}/>' for x, y in [(16, 96), (28, 90), (40, 84)])
    + f'<circle cx="54" cy="72" r="16" fill="#FFF4D6" {s()}/>' + f(54, 72, d=6, k=0.55)
    + f'<path d="M46 58 Q42 46 36 48 M60 58 Q64 46 70 48" fill="none" {W(2.4)}/>' + sp((20, 28, 6), (108, 26, 5)))
I["shchelkovo-gallery"] = ("yellow", "баночка гуаши-персонаж с кисточкой рисует мазок",
    f'<rect x="28" y="50" width="64" height="62" rx="12" fill="#fff" {s()}/><rect x="24" y="38" width="72" height="16" rx="6" fill="{B}" {s()}/>'
    f'<path d="M28 66 H92 V100 Q92 112 80 112 H40 Q28 112 28 100Z" fill="{R}" {s()}/>' + f(60, 82, d=9, k=0.75)
    + f'<g transform="rotate(30 100 50)"><rect x="96" y="6" width="8" height="48" rx="3" fill="#D9A066" {W(2.2)}/>'
    f'<rect x="95" y="50" width="10" height="8" fill="{GR}" {W(2)}/><path d="M95 58 Q100 76 105 58Z" fill="{R}" {W(2)}/></g>'
    f'<path d="M14 24 Q30 14 46 24" fill="none" stroke="{R}" stroke-width="6" stroke-linecap="round"/>' + sp((112, 104, 5)))

# ======================= Егорьевск =======================
I["egoryevsk-art-museum"] = ("orange", "картина в золотой раме — улыбающийся пейзаж, на раме берет художника",
    f'<rect x="16" y="28" width="96" height="80" rx="4" fill="{GO}" {s()}/><rect x="26" y="38" width="76" height="60" fill="#BFE8FF" {W(2.4)}/>'
    f'<path d="M26 98 V80 Q46 64 64 78 Q82 62 102 76 V98Z" fill="{G}" {W(2.2)}/><circle cx="84" cy="54" r="9" fill="{Y}" {W(2)}/>'
    + f(56, 84, d=8, k=0.55)
    + f'<ellipse cx="40" cy="28" rx="20" ry="8" fill="{R}" {s()}/><path d="M40 20 v-6" {W(3)}/>' + sp((112, 116, 5), (14, 116, 4)))
I["egoryevsk-history-museum"] = ("purple", "старинная монетка-персонаж с всадником-гербом",
    f'<circle cx="64" cy="64" r="44" fill="{GO}" {s()}/><circle cx="64" cy="64" r="36" fill="none" stroke="#C9921E" stroke-width="3" stroke-dasharray="3 5"/>'
    f'<path d="M44 52 Q50 40 62 42 L70 36 L74 44 Q84 46 84 54 L80 58 H48Z" fill="#C9921E" {W(2)}/>'
    + f(64, 76, d=10, k=0.8) + sp((20, 24, 6), (108, 108, 6), (110, 24, 4)))
I["egoryevsk-park-200"] = ("blue", "кораблик-фрегат везёт ящик апельсинов по пруду",
    WATER + f'<path d="M20 86 H108 Q100 108 64 108 Q28 108 20 86Z" fill="{BR}" {s()}/>' + f(64, 96, d=9, k=0.6)
    + f'<path d="M60 86 V20" {W(4)}/><path d="M62 24 Q92 36 62 52Z M62 56 Q86 66 62 80Z" fill="#fff" {s()}/>'
    f'<path d="M60 20 L44 14 L60 10Z" fill="{R}" {W(2)}/>'
    f'<rect x="24" y="66" width="28" height="20" rx="2" fill="#D9A066" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="{OR}" {W(2)}/>' for x, y in [(30, 62), (42, 60), (36, 54)]))
I["egoryevsk-pegas-park"] = ("pink", "пони-Пегас с крылышками и пышной гривой",
    GROUND + f'<path d="M36 82 Q34 62 54 60 H86 Q100 60 100 76 Q100 92 86 92 H52 Q36 92 36 82Z" fill="#fff" {s()}/>'
    f'<path d="M44 90 V112 M58 92 V114 M80 92 V114 M92 88 V110" {W(5)}/>'
    f'<path d="M86 66 Q90 38 104 32 Q118 36 114 52 Q108 60 98 64Z" fill="#fff" {s()}/>' + eye(106, 44, 0.6)
    + f'<path d="M88 40 Q92 22 106 20 M94 46 Q100 30 112 28" fill="none" stroke="{V}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M56 62 Q40 30 20 34 Q30 44 26 52 Q38 54 44 62Z" fill="#E8F4FF" {s()}/>'
    f'<path d="M36 76 Q20 74 18 90" fill="none" stroke="{P}" stroke-width="6" stroke-linecap="round"/>'
    f'<ellipse cx="112" cy="50" rx="3" ry="2" fill="#FF7FA8"/>' + sp((20, 108, 4), (112, 108, 4)))
I["egoryevsk-dk-konina"] = ("purple", "цирковой пудель стоит на мячике на сцене", stage(
    f'<circle cx="64" cy="86" r="14" fill="{B}" {s()}/><path d="M52 80 Q64 86 76 80" fill="none" stroke="#fff" stroke-width="3"/>'
    f'<circle cx="64" cy="58" r="14" fill="#fff" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="#fff" {W(2.2)}/>' for x, y in [(48, 52), (80, 52), (64, 40)])
    + f(64, 60, d=6, k=0.5) + f'<ellipse cx="64" cy="66" rx="3" ry="2.4" fill="{O}"/>'
    + f'<path d="M58 34 L64 22 L70 34Z" fill="{Y}" {W(2)}/>', cur=V))
I["egoryevsk-pegas-cinema"] = ("orange", "киноэкран, на экране комета-персонаж с хвостиком", screen(
    f'<path d="M30 76 Q50 70 58 58" fill="none" stroke="{Y}" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M34 68 Q48 62 54 52" fill="none" stroke="{OR}" stroke-width="5" stroke-linecap="round"/>'
    f'<circle cx="70" cy="50" r="14" fill="{Y}" {s()}/>' + f(70, 51, d=5, k=0.5) + sp((96, 70, 4), (92, 40, 5))))
I["egoryevsk-impulse"] = ("yellow", "молния-персонаж прыгает на батуте", tramp(
    f'<path d="M70 12 L42 58 H60 L50 94 L88 44 H68 L80 12Z" fill="{Y}" {s()}/>' + f(64, 50, d=6, k=0.55), col=V)
    + sp((18, 26, 6), (110, 24, 5)))
I["egoryevsk-berezhki"] = ("green", "козлёнок катит шар для боулинга к кеглям",
    GROUND + "".join(f'<path d="M{x} 104 Q{x-6} 92 {x-2} 84 Q{x} 78 {x+2} 84 Q{x+6} 92 {x} 104Z" fill="#fff" {W(2.2)}/>'
                     f'<path d="M{x-3} 90 h6" stroke="{R}" stroke-width="2.4"/>' for x in (98, 110, 104))
    + f'<ellipse cx="46" cy="84" rx="24" ry="16" fill="#fff" {s()}/>'
    f'<path d="M30 96 V112 M42 98 V114 M54 98 V114 M64 92 V110" {W(4.5)}/>'
    f'<circle cx="32" cy="62" r="15" fill="#fff" {s()}/><path d="M24 50 Q18 38 24 34 M38 50 Q42 38 36 34" fill="none" stroke="#B9874F" stroke-width="4" stroke-linecap="round"/>'
    + f(32, 62, d=5, k=0.5) + f'<path d="M28 74 L32 82 L36 74" fill="#fff" {W(2)}/>'
    f'<circle cx="80" cy="96" r="12" fill="{NV}" {s()}/><circle cx="76" cy="92" r="2" fill="#fff"/><circle cx="82" cy="90" r="2" fill="#fff"/><circle cx="80" cy="96" r="2" fill="#fff"/>'
    + sp((108, 28, 6)))

# ======================= Чехов =======================
I["chekhov-city-park"] = ("teal", "паровозик-персонаж едет вдоль пруда с прудиком-лесенкой",
    f'<path d="M0 96 Q32 88 64 96 T128 96 V128 H0Z" fill="#7FD3F7" {W(2.6)}/><path d="M0 84 H128" stroke="{BR}" stroke-width="4"/>'
    + "".join(f'<path d="M{x} 80 v8" stroke="{BR}" stroke-width="3"/>' for x in range(6, 128, 12))
    + f'<rect x="20" y="44" width="56" height="34" rx="6" fill="{R}" {s()}/><rect x="70" y="30" width="34" height="48" rx="5" fill="{B}" {s()}/>'
    f'<rect x="76" y="36" width="22" height="16" rx="3" fill="#BFE8FF" {W(2)}/><rect x="26" y="30" width="12" height="16" fill="{NV}" {W(2.2)}/>'
    + "".join(f'<circle cx="{x}" cy="80" r="8" fill="{NV}" {W(2.4)}/>' for x in (34, 60, 90))
    + f(48, 60, d=7, k=0.6)
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".85" {W(1.6)}/>' for x, y, r in [(32, 22, 6), (24, 12, 5)])
    + f'<ellipse cx="40" cy="108" rx="8" ry="4" fill="{G}" {W(2)}/><ellipse cx="96" cy="112" rx="8" ry="4" fill="{G}" {W(2)}/>')
I["chekhov-lopasnya-museum"] = ("yellow", "соломенная куколка-скрутка в красном платочке",
    f'<path d="M64 46 L30 116 H98Z" fill="#F2D27A" {s()}/>'
    + "".join(f'<path d="M64 52 L{x} 114" stroke="#D9B04A" stroke-width="2"/>' for x in (40, 52, 64, 76, 88))
    + f'<path d="M40 70 H88" stroke="{R}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M44 68 L24 84 M84 68 L104 84" stroke="#F2D27A" stroke-width="7" stroke-linecap="round"/>'
    f'<circle cx="64" cy="38" r="18" fill="#F2D27A" {s()}/><path d="M44 36 Q64 6 84 36 Q74 26 64 26 Q54 26 44 36Z" fill="{R}" {W(2.4)}/>'
    f'<path d="M46 42 L38 54 L50 48Z" fill="{R}" {W(2)}/>' + f(64, 42, d=6, k=0.5) + sp((18, 26, 6), (110, 30, 5)))
I["chekhov-energomash"] = ("blue", "гаечный ключ обнимает болтик-малыша",
    f'<g transform="rotate(-30 64 64)"><rect x="56" y="30" width="16" height="76" rx="6" fill="{GR}" {s()}/>'
    f'<path d="M48 30 Q46 8 64 8 Q82 8 80 30 L72 26 V14 H56 V26Z" fill="{GR}" {s()}/></g>' + f(62, 70, d=6, k=0.55)
    + f'<rect x="86" y="70" width="14" height="40" rx="2" fill="{Y}" {s()}/>'
    + "".join(f'<path d="M86 {y} L100 {y-4}" stroke="#C9921E" stroke-width="2"/>' for y in (84, 92, 100, 108))
    + f'<path d="M80 60 H106 L102 74 H84Z" fill="{Y}" {s()}/>' + f(93, 66, d=4, k=0.4)
    + f'<path d="M74 82 Q82 90 86 86" fill="none" {W(3)}/>' + sp((18, 104, 6), (110, 22, 5)))
I["chekhov-theatre"] = ("sky", "чайка-артистка кланяется на сцене театра", stage(
    f'<ellipse cx="64" cy="76" rx="20" ry="16" fill="#fff" {s()}/><circle cx="64" cy="52" r="13" fill="#fff" {s()}/>'
    + f(64, 52, d=5, k=0.5) + f'<path d="M58 60 L64 66 L70 60Z" fill="{Y}" {W(1.8)}/>'
    f'<path d="M46 70 Q30 54 36 46 Q44 58 52 64Z M82 70 Q98 54 92 46 Q84 58 76 64Z" fill="{GR}" {W(2.4)}/>'
    f'<path d="M56 92 V100 M72 92 V100" stroke="{OR}" stroke-width="4" stroke-linecap="round"/>'))
I["chekhov-matrix-cinema"] = ("yellow", "киноэкран, на экране солнышко выглядывает из-за облака", screen(
    f'<circle cx="54" cy="54" r="15" fill="{Y}" {s()}/>' + f(54, 54, d=5, k=0.5)
    + "".join(f'<path d="M{54+21*c:.0f} {54+21*s_:.0f} l{4*c:.0f} {4*s_:.0f}" stroke="{OR}" stroke-width="3" stroke-linecap="round"/>' for c, s_ in [(1, 0), (-1, 0), (0, -1), (.7, -.7), (-.7, -.7)])
    + f'<path d="M62 78 Q58 66 70 64 Q74 56 84 60 Q96 58 96 70 Q102 72 100 78Z" fill="#fff" {s()}/>'))

# ======================= Дубна =======================
I["dubna-rockets-museum"] = ("sky", "крылатая ракета-персонаж на музейном постаменте",
    f'<rect x="20" y="100" width="88" height="16" rx="3" fill="{GR}" {s()}/><path d="M40 100 V88 M88 100 V88" {W(4)}/>'
    f'<path d="M14 80 Q14 70 26 70 H96 L118 78 L96 86 H26 Q14 86 14 80Z" fill="#fff" {s()}/>'
    f'<path d="M56 70 L44 50 H58 L72 70Z M56 86 L46 98 H58 L70 86Z" fill="{B}" {s()}/>'
    f'<path d="M16 72 L8 60 H16 L24 70Z" fill="{R}" {W(2.2)}/>' + f(96, 78, d=5, k=0.45)
    + sp((20, 30, 6), (100, 30, 5)))
I["dubna-family-park"] = ("blue", "колесо обозрения над озером, внизу кораблик под парусом",
    WATER + f'<circle cx="64" cy="50" r="36" fill="none" stroke="#fff" stroke-width="5"/><circle cx="64" cy="50" r="36" fill="none" {W(1.6)}/>'
    + "".join(f'<path d="M64 50 L{64+36*c:.0f} {50+36*s_:.0f}" stroke="#fff" stroke-width="2.4"/>' for c, s_ in [(1, 0), (-1, 0), (0, -1), (0, 1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7)])
    + "".join(f'<rect x="{x-6}" y="{y}" width="12" height="9" rx="3" fill="{c}" {W(2)}/>' for x, y, c in [(100, 50, R), (28, 50, Y), (64, 14, G), (90, 24, V), (38, 24, P)])
    + f'<circle cx="64" cy="50" r="9" fill="{Y}" {W(2.4)}/>' + f(64, 50, d=3.5, k=0.35)
    + f'<path d="M84 110 H112 L106 118 H90Z" fill="{R}" {W(2.2)}/><path d="M98 108 V88 L110 106Z" fill="#fff" {W(2)}/>')
I["dubna-dk-mir"] = ("teal", "земной шарик-персонаж поёт на сцене", stage(
    f'<circle cx="64" cy="66" r="26" fill="{B}" {s()}/>'
    f'<path d="M46 54 Q54 46 60 54 Q58 62 48 62Z M70 74 Q82 70 84 80 Q76 90 70 84Z M66 44 Q74 42 78 48 Q72 52 66 50Z" fill="{G}" {W(2)}/>'
    + f(64, 66, d=8, k=0.6) + f'<path d="M96 40 l4 -10 M104 46 l8 -6" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    f'<path d="M98 30 q6 2 4 8 M108 38 q6 2 2 8" fill="none" {W(2)}/>', cur=TE))

# ======================= Руза =======================
I["ruza-gorodok"] = ("green", "избушка на курьих ножках из Дома сказок",
    GROUND + f'<path d="M48 84 L42 108 L34 112 M48 108 L50 112 M80 84 L86 108 L94 112 M86 108 L82 112" stroke="{OR}" stroke-width="5" stroke-linecap="round" fill="none"/>'
    f'<rect x="30" y="44" width="68" height="42" rx="4" fill="{BR}" {s()}/>'
    + "".join(f'<path d="M30 {y} H98" stroke="#8A4E20" stroke-width="2.4"/>' for y in (54, 64, 74))
    + f'<path d="M22 46 L64 16 L106 46Z" fill="{R}" {s()}/><rect x="54" y="52" width="20" height="18" rx="2" fill="#FFE07A" {W(2.4)}/>'
    + f(64, 60, d=5, k=0.45) + f'<path d="M86 26 V14 H94 V34" fill="{GR}" {W(2.2)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".8"/>' for x, y, r in [(92, 8, 4), (100, 2, 3)]) + sp((18, 26, 5)))
I["ruza-museum"] = ("orange", "лапоть-персонаж с берестяной кисточкой",
    f'<path d="M18 96 Q16 70 40 64 Q60 60 76 68 Q104 72 112 92 Q112 108 90 110 H40 Q18 110 18 96Z" fill="#E2C281" {s()}/>'
    + "".join(f'<path d="M{x} 66 L{x+14} 110" stroke="#C49A55" stroke-width="2.4"/>' for x in range(26, 104, 12))
    + "".join(f'<path d="M{x} 110 L{x+14} 66" stroke="#C49A55" stroke-width="2.4"/>' for x in range(26, 104, 12))
    + f'<path d="M18 96 Q16 70 40 64 Q60 60 76 68 Q104 72 112 92 Q112 108 90 110 H40 Q18 110 18 96Z" fill="none" {s()}/>'
    f'<path d="M34 70 Q30 40 60 30 Q80 36 76 64" fill="none" stroke="#C49A55" stroke-width="4"/>' + f(66, 88, d=10, k=0.75)
    + sp((20, 30, 6), (108, 34, 5)))
I["ruza-militsiya-museum"] = ("blue", "полосатый жезл регулировщика в милицейской фуражке",
    f'<g transform="rotate(20 64 70)"><rect x="54" y="40" width="20" height="80" rx="9" fill="#fff" {s()}/>'
    + "".join(f'<rect x="54" y="{y}" width="20" height="10" fill="{R}"/>' for y in (52, 72, 92))
    + f'<rect x="54" y="40" width="20" height="80" rx="9" fill="none" {s()}/></g>' + f(60, 66, d=6, k=0.5)
    + f'<path d="M30 40 Q30 18 60 18 Q90 18 90 40Z" fill="{NV}" {s()}/><path d="M26 40 H94 Q90 50 60 50 Q30 50 26 40Z" fill="{NV}" {s()}/>'
    f'<path d="M30 38 H90" stroke="{R}" stroke-width="4"/><circle cx="60" cy="28" r="5" fill="{GO}" {W(2)}/>' + sp((108, 100, 6), (16, 96, 5)))
I["ruza-oktyabr-cinema"] = ("orange", "киноэкран, на экране кленовый листик кружится", screen(
    f'<path d="M64 34 L70 48 L84 44 L78 56 L90 62 L76 66 L78 80 L64 72 L50 80 L52 66 L38 62 L50 56 L44 44 L58 48Z" fill="{OR}" {s()}/>'
    f'<path d="M64 72 V84" {W(3)}/>' + f(64, 58, d=5, k=0.5)
    + f'<path d="M30 46 q6 -6 12 0 M90 74 q6 -6 12 0" fill="none" stroke="{GR}" stroke-width="2"/>', cur=OR))
I["ruza-cki"] = ("green", "ёжик-артист с микрофоном на сцене", stage(
    f'<path d="M36 96 Q30 60 64 54 Q98 60 92 96Z" fill="{BR}" {s()}/>'
    + "".join(f'<path d="M{x} {y} l-6 -10 l10 4" fill="{BR}" {W(2)}/>' for x, y in [(44, 66), (56, 58), (70, 58), (82, 64), (40, 80)])
    + f'<ellipse cx="64" cy="82" rx="18" ry="14" fill="#F4D9B0" {s()}/>' + f(64, 80, d=6, k=0.5)
    + f'<path d="M84 84 L96 70" {W(4)}/><circle cx="98" cy="66" r="6" fill="{GR}" {W(2.2)}/>', cur=DG))

# ======================= Зарайск =======================
I["zaraysk-golubkina"] = ("purple", "мраморный бюст-персонаж на постаменте, рядом стека скульптора",
    f'<rect x="40" y="96" width="48" height="24" rx="2" fill="{GR}" {s()}/><rect x="34" y="90" width="60" height="8" rx="2" fill="{GR}" {s()}/>'
    f'<path d="M36 90 Q36 68 64 66 Q92 68 92 90Z" fill="#F2F0F7" {s()}/>'
    f'<circle cx="64" cy="46" r="22" fill="#F2F0F7" {s()}/><path d="M44 40 Q48 20 64 22 Q82 20 86 40 Q78 30 64 30 Q50 30 44 40Z" fill="#E0DCEB" {W(2.4)}/>'
    + f(64, 50, d=7, k=0.55)
    + f'<g transform="rotate(-35 108 60)"><rect x="104" y="30" width="7" height="50" rx="3" fill="#D9A066" {W(2)}/><path d="M104 30 Q107 18 111 30Z" fill="{GR}" {W(1.8)}/></g>'
    + sp((18, 26, 6), (20, 70, 4)))
I["zaraysk-bakhrushin"] = ("pink", "театральная афишная тумба-персонаж с маленькой короной",
    f'<ellipse cx="64" cy="116" rx="34" ry="6" fill="{GR}" {s()}/><rect x="36" y="34" width="56" height="82" fill="{V}" {s()}/>'
    f'<path d="M32 34 Q64 10 96 34Z" fill="{NV}" {s()}/><circle cx="64" cy="16" r="4" fill="{GO}" {W(2)}/>'
    f'<rect x="42" y="44" width="44" height="34" rx="2" fill="#FFF4D6" {W(2.4)}/>'
    f'<path d="M48 52 H80 M48 60 H72 M48 68 H76" stroke="{R}" stroke-width="3" stroke-linecap="round"/>'
    + f(64, 94, d=9, k=0.65) + f'<path d="M54 26 L58 18 L64 24 L70 18 L74 26Z" fill="{Y}" {W(1.8)}/>'
    + sp((18, 30, 6), (110, 60, 5)))
I["zaraysk-water-tower"] = ("sky", "старинная водонапорная башня-персонаж с флажком на шпиле",
    f'<path d="M0 116 H128 V128 H0Z" fill="{G}" {W(2.6)}/>'
    f'<path d="M48 116 L52 54 H76 L80 116Z" fill="#E07A5F" {s()}/>'
    + "".join(f'<path d="M50 {y} H78" stroke="#B85A44" stroke-width="2"/>' for y in (70, 86, 102))
    + f'<rect x="38" y="30" width="52" height="26" rx="4" fill="#E07A5F" {s()}/>'
    + "".join(f'<rect x="{x}" y="36" width="8" height="12" rx="4" fill="#BFE8FF" {W(1.8)}/>' for x in (44, 60, 76))
    + f'<path d="M34 32 L64 10 L94 32Z" fill="{DG}" {s()}/><path d="M64 10 V2 M64 2 L76 6 L64 10" fill="{R}" {W(2)}/>'
    + f(64, 88, d=6, k=0.5) + sp((18, 30, 6), (110, 40, 5)))
I["zaraysk-svyatopole"] = ("yellow", "лошадка катает щенка хаски на спине",
    GROUND + f'<path d="M28 76 Q26 56 46 54 H80 Q94 54 94 70 Q94 84 80 84 H44 Q28 84 28 76Z" fill="{BR}" {s()}/>'
    f'<path d="M36 82 V108 M48 84 V110 M76 84 V110 M88 80 V106" {W(5)}/>'
    f'<path d="M84 60 Q90 34 104 28 Q118 32 114 48 Q108 56 96 60Z" fill="{BR}" {s()}/>' + eye(106, 40, 0.6)
    + f'<path d="M86 36 Q92 22 104 20" fill="none" stroke="{NV}" stroke-width="6" stroke-linecap="round"/>'
    f'<path d="M30 68 Q16 70 14 86" fill="none" stroke="{NV}" stroke-width="6" stroke-linecap="round"/>'
    f'<circle cx="58" cy="40" r="14" fill="#9AA6C8" {s()}/><path d="M48 32 L46 20 L56 28Z M68 32 L70 20 L60 28Z" fill="#9AA6C8" {W(2.2)}/>'
    f'<path d="M48 44 Q58 56 68 44 Q64 50 58 50 Q52 50 48 44Z" fill="#fff"/>' + f(58, 40, d=5, k=0.45))

# ======================= Серпухов =======================
I["serpukhov-sennaya"] = ("teal", "старинный печатный пресс-персонаж печатает лист с буквой",
    f'<rect x="22" y="98" width="84" height="18" rx="3" fill="{BR}" {s()}/><path d="M30 98 V30 M98 98 V30" stroke="{NV}" stroke-width="8" stroke-linecap="round"/>'
    f'<rect x="24" y="22" width="80" height="16" rx="4" fill="{NV}" {s()}/><path d="M64 38 V56" {W(5)}/>'
    f'<path d="M64 14 V22 M44 14 H84" stroke="{GO}" stroke-width="5" stroke-linecap="round"/>'
    f'<rect x="40" y="56" width="48" height="14" rx="3" fill="{GR}" {s()}/>' + f(64, 63, d=6, k=0.45)
    + f'<rect x="38" y="78" width="52" height="20" fill="#fff" {s()}/><path d="M56 94 L62 82 L68 94 M58 90 H66" fill="none" stroke="{R}" stroke-width="2.6"/>'
    + sp((112, 60, 5)))
I["serpukhov-pitomnik-park"] = ("orange", "бельчонок крутится на карусели-чашке",
    GROUND + f'<path d="M24 76 H104 Q100 106 64 106 Q28 106 24 76Z" fill="{P}" {s()}/><path d="M30 86 H98" stroke="#fff" stroke-width="3"/>'
    f'<path d="M102 82 Q118 82 116 94 Q112 102 100 96" fill="none" {W(4)}/>'
    + "".join(f'<circle cx="{x}" cy="90" r="3" fill="#fff"/>' for x in (40, 56, 72, 88))
    + f'<path d="M78 70 Q100 50 92 28 Q110 36 104 60 Q100 74 82 76Z" fill="{OR}" {s()}/>'
    f'<ellipse cx="62" cy="64" rx="16" ry="14" fill="{OR}" {s()}/><path d="M52 52 l-3 -9 l8 5Z M70 52 l3 -9 l-8 5Z" fill="{OR}" {W(2)}/>'
    + f(62, 64, d=6, k=0.5) + f'<path d="M40 30 q6 -6 12 0" fill="none" stroke="#fff" stroke-width="3"/>' + sp((20, 30, 5)))
I["serpukhov-stepanov-park"] = ("sky", "котёнок едет в кабинке канатной дороги",
    f'<path d="M0 30 L128 14" stroke="{NV}" stroke-width="3"/><path d="M64 22 V44" {W(4)}/><circle cx="64" cy="22" r="5" fill="{GR}" {W(2)}/>'
    f'<rect x="36" y="44" width="56" height="48" rx="10" fill="{R}" {s()}/><rect x="42" y="52" width="44" height="22" rx="4" fill="#BFE8FF" {W(2.2)}/>'
    f'<circle cx="64" cy="70" r="12" fill="{OR}" {s()}/><path d="M54 62 L54 50 L62 58Z M74 62 L74 50 L66 58Z" fill="{OR}" {W(2)}/>'
    + f(64, 70, d=5, k=0.45) + f'<rect x="36" y="74" width="56" height="18" rx="2" fill="{R}" {s()}/>'
    + f'<path d="M0 116 Q30 96 60 112 T128 104 V128 H0Z" fill="{G}" {W(2.4)}/>' + sp((18, 52, 5), (110, 40, 6)))
I["serpukhov-kosmos"] = ("night", "планета Сатурн-персонаж прыгает на батуте", tramp(
    f'<circle cx="64" cy="54" r="24" fill="{OR}" {s()}/><ellipse cx="64" cy="58" rx="40" ry="9" fill="none" stroke="{Y}" stroke-width="5" transform="rotate(-12 64 58)"/>'
    + f(64, 52, d=7, k=0.6), col=V) + "".join(sparkle(x, y, r, Y) for x, y, r in [(16, 22, 5), (112, 20, 6), (110, 70, 3)]))
I["serpukhov-theatre"] = ("purple", "павлин распускает хвост на сцене театра", stage(
    "".join(f'<ellipse cx="{64+34*c:.0f}" cy="{74+30*s_:.0f}" rx="9" ry="13" fill="{TE}" {W(2)} transform="rotate({a} {64+34*c:.0f} {74+30*s_:.0f})"/>'
            f'<circle cx="{64+34*c:.0f}" cy="{74+30*s_:.0f}" r="4" fill="{B}"/>' for c, s_, a in [(-1, 0, 90), (-.75, -.66, 50), (-.3, -.95, 18), (.3, -.95, -18), (.75, -.66, -50), (1, 0, 90)])
    + f'<ellipse cx="64" cy="82" rx="12" ry="16" fill="{B}" {s()}/><circle cx="64" cy="62" r="10" fill="{B}" {s()}/>'
    + f(64, 62, d=4, k=0.4) + f'<path d="M64 52 L60 44 M64 52 L68 44" {W(2)}/>', cur=V))
I["drakino-husky"] = ("blue", "щенок хаски тянет санки по снегу",
    f'<path d="M0 100 Q64 88 128 100 V128 H0Z" fill="#fff" {W(2.6)}/>'
    f'<path d="M14 104 H50 Q56 104 56 98" fill="none" {W(3)}/><rect x="16" y="88" width="34" height="12" rx="3" fill="{R}" {s()}/>'
    f'<path d="M50 92 L68 80" {W(2.4)}/>'
    f'<ellipse cx="82" cy="86" rx="20" ry="13" fill="#9AA6C8" {s()}/><path d="M68 96 V106 M96 96 V106" {W(5)}/>'
    f'<circle cx="94" cy="62" r="18" fill="#9AA6C8" {s()}/><path d="M80 52 L78 34 L92 46Z M108 52 L110 34 L96 46Z" fill="#9AA6C8" {W(2.4)}/>'
    f'<path d="M80 66 Q94 82 108 66 Q102 74 94 74 Q86 74 80 66Z" fill="#fff"/>' + f(94, 62, d=6, k=0.55)
    + f'<path d="M62 84 Q50 70 58 64" fill="none" {W(3)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#fff"/>' for x, y in [(20, 20), (40, 40), (70, 16), (110, 28), (30, 60)]))
I["derevo-dom-prioksky"] = ("green", "домик на дереве с верёвочным мостиком",
    GROUND + f'<path d="M44 108 Q48 80 44 60 H60 Q56 80 62 108Z" fill="{BR}" {s()}/>'
    f'<circle cx="52" cy="40" r="32" fill="{DG}" {s()}/>'
    f'<rect x="30" y="44" width="44" height="30" rx="3" fill="#D9A066" {s()}/><path d="M24 46 L52 24 L80 46Z" fill="{R}" {s()}/>'
    + f(52, 58, d=7, k=0.55)
    + f'<path d="M74 66 Q96 80 120 64" fill="none" {W(3)}/><path d="M74 58 Q96 72 120 56" fill="none" {W(2)}/>'
    + "".join(f'<path d="M{x} {66+ (x-74)*0.3 - (x-74)**2*0.012:.0f} V{58+ (x-74)*0.3 - (x-74)**2*0.012:.0f}" {W(2)}/>' for x in range(80, 120, 8))
    + sp((110, 22, 6)))

# ======================= Звенигород, Москва =======================
I["zvenigorod-manezh"] = ("sky", "радуга-персонаж от зелёного холма до облака («От земли до неба»)",
    f'<path d="M0 112 Q40 82 80 112 V128 H0Z" fill="{G}" {W(2.6)}/>'
    + "".join(f'<path d="M{20+i*7} 110 Q{20+i*7} {28+i*7} {110-i*7} {40+i*7}" fill="none" stroke="{c}" stroke-width="7"/>' for i, c in enumerate([R, OR, Y, G, B, V]))
    + f'<path d="M88 52 Q84 38 98 36 Q104 26 114 32 Q126 32 124 44 Q130 50 124 56Z" fill="#fff" {s()}/>'
    + f(56, 58, d=7, k=0.6) + sp((18, 24, 6)))
I["zvenigorod-kc-orlovoy"] = ("pink", "звёздочка-кинозвезда в шляпке с вуалью на сцене", stage(
    f'<path d="M64 36 L72 56 L94 58 L78 72 L82 94 L64 84 L46 94 L50 72 L34 58 L56 56Z" fill="{Y}" {s()}/>'
    + f(64, 66, d=6, k=0.5)
    + f'<ellipse cx="64" cy="40" rx="18" ry="5" fill="{NV}" {W(2.2)}/><path d="M54 40 Q54 26 64 26 Q74 26 74 40Z" fill="{NV}" {W(2.2)}/>'
    f'<path d="M74 30 l8 -6" stroke="{P}" stroke-width="3" stroke-linecap="round"/>', cur=P))
I["moskino-berezka"] = ("teal", "киноэкран, на экране берёзка машет веточкой", screen(
    f'<rect x="58" y="44" width="10" height="38" fill="#fff" {W(2.2)}/>'
    + "".join(f'<path d="M{x} {y} h4" stroke="{NV}" stroke-width="2.4"/>' for x, y in [(59, 52), (63, 62), (59, 72)])
    + "".join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="5" fill="{G}" {W(1.8)}/>' for x, y in [(48, 42), (62, 36), (78, 42), (52, 52), (76, 54)])
    + f(63, 66, d=5, k=0.4), cur=DG))

# ======================= Кашира =======================
I["kashira-museum"] = ("sky", "каширская глиняная игрушка-барашек с узорами",
    f'<ellipse cx="64" cy="112" rx="40" ry="8" fill="#B9874F" opacity=".5"/>'
    f'<path d="M30 80 Q28 56 52 54 H84 Q100 56 100 74 Q100 92 84 92 H48 Q30 92 30 80Z" fill="#F4E9D8" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{c}"/>' for x, y, c in [(46, 70, R), (60, 64, G), (74, 70, R), (86, 64, G), (54, 80, B), (78, 82, B)])
    + f'<path d="M40 90 L38 110 M54 92 V112 M78 92 V112 M90 88 L92 108" {W(5)}/>'
    f'<circle cx="100" cy="52" r="16" fill="#F4E9D8" {s()}/><path d="M88 46 Q78 40 82 52 Q86 58 92 54" fill="#D9824A" {W(2.4)}/>'
    + f(102, 54, d=5, k=0.45) + f'<path d="M30 74 Q18 70 20 60" fill="none" {W(3)}/>' + sp((20, 30, 6)))
I["kashira-doll-museum"] = ("pink", "тряпичная кукла с длинной косой и бантом",
    f'<path d="M64 60 L34 118 H94Z" fill="{B}" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#fff"/>' for x, y in [(52, 90), (64, 102), (76, 90), (60, 78), (70, 110)])
    + f'<path d="M48 76 L32 92 M80 76 L96 92" stroke="#F4D9B0" stroke-width="7" stroke-linecap="round"/>'
    f'<circle cx="64" cy="44" r="20" fill="#F4D9B0" {s()}/><path d="M44 42 Q46 22 64 22 Q82 22 84 42 Q74 30 64 32 Q54 30 44 42Z" fill="#E2A24A" {W(2.4)}/>'
    f'<path d="M82 42 Q94 60 92 86" fill="none" stroke="#E2A24A" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M86 88 l-8 6 l2 -10Z M96 88 l8 6 l-2 -10Z" fill="{R}" {W(1.8)}/>' + f(64, 48, d=7, k=0.55) + sp((18, 28, 6)))
I["kashira-kovcheg"] = ("blue", "лисичка выглядывает из ковчега-кораблика",
    WATER + f'<path d="M14 72 H114 Q104 104 64 104 Q24 104 14 72Z" fill="{BR}" {s()}/>'
    + "".join(f'<path d="M18 {y} H110" stroke="#8A4E20" stroke-width="2"/>' for y in (82, 92))
    + f'<rect x="38" y="44" width="52" height="28" rx="3" fill="#D9A066" {s()}/><path d="M32 46 L64 24 L96 46Z" fill="{R}" {s()}/>'
    f'<path d="M50 72 Q48 50 64 48 Q80 50 78 72Z" fill="{OR}" {s()}/><path d="M50 56 L46 40 L58 50Z M78 56 L82 40 L70 50Z" fill="{OR}" {W(2.2)}/>'
    f'<path d="M54 64 Q64 74 74 64 Q70 70 64 70 Q58 70 54 64Z" fill="#fff"/>' + f(64, 60, d=6, k=0.5)
    + f'<ellipse cx="64" cy="66" rx="2.6" ry="2" fill="{O}"/>' + sp((18, 26, 6), (110, 24, 5)))
I["kashira-kdc-rodina"] = ("orange", "балалайка-персонаж играет на сцене", stage(
    f'<rect x="60" y="22" width="8" height="40" fill="{BR}" {W(2.2)}/><rect x="56" y="16" width="16" height="10" rx="2" fill="{BR}" {W(2)}/>'
    f'<path d="M64 56 L36 98 H92Z" fill="{OR}" {s()}/><circle cx="64" cy="80" r="6" fill="{NV}"/>'
    f'<path d="M62 30 V96 M66 30 V96" stroke="#fff" stroke-width="1.2"/>' + f(64, 70, d=8, k=0.55).replace("", "")
    , cur=R))
I["kashira-almaz-cinema"] = ("purple", "киноэкран, на экране сверкает алмазик", screen(
    f'<path d="M44 48 L54 38 H74 L84 48 L64 76Z" fill="#9AE3FF" {s()}/><path d="M44 48 H84 M54 38 L60 48 L64 76 L68 48 L74 38" fill="none" {W(1.8)}/>'
    + f(64, 56, d=5, k=0.45) + "".join(sparkle(x, y, r, "#fff") for x, y, r in [(92, 40, 5), (36, 70, 4)]), cur=V))

# ======================= Сергиев Посад, Волоколамск =======================
I["sp-dom-remesel"] = ("yellow", "витражное окошко-персонаж из цветных стёклышек",
    f'<path d="M30 120 V48 Q30 14 64 14 Q98 14 98 48 V120Z" fill="{NV}" {s()}/>'
    + "".join(f'<path d="{d}" fill="{c}" {W(2)}/>' for d, c in [
        ("M36 116 V64 H62 V116Z", B), ("M66 116 V64 H92 V116Z", G), ("M36 60 V48 Q36 22 62 20 V60Z", R), ("M66 60 V20 Q92 22 92 48 V60Z", Y)])
    + f'<circle cx="64" cy="62" r="12" fill="{P}" {W(2.4)}/>' + f(64, 90, d=12, k=0.8) + sp((18, 26, 6), (110, 30, 5)))
I["sp-zhili-byli"] = ("orange", "чугунный утюг-персонаж с угольками внутри",
    f'<path d="M14 100 Q14 66 50 60 H100 Q114 60 114 74 V100Z" fill="{NV}" {s()}/>'
    f'<rect x="12" y="100" width="104" height="10" rx="3" fill="#5A5878" {s()}/>'
    f'<path d="M50 60 Q48 38 74 36 Q100 38 98 60" fill="none" stroke="{BR}" stroke-width="8" stroke-linecap="round"/>'
    + "".join(f'<circle cx="{x}" cy="88" r="4" fill="{c}"/>' for x, c in [(30, OR), (40, R), (50, Y)])
    + f(80, 80, d=8, k=0.7).replace(f'fill="{O}"', 'fill="#fff"', 2)
    + "".join(f'<path d="M{x} 50 q4 -6 0 -12 q-4 -6 0 -12" fill="none" stroke="#fff" stroke-width="2.4" opacity=".8"/>' for x in (28, 38)))
I["volokolamsk-kremlin"] = ("sky", "колокольня-персонаж кремля с колоколом в арке",
    f'<path d="M0 116 H128 V128 H0Z" fill="{G}" {W(2.6)}/>'
    f'<rect x="40" y="62" width="48" height="54" fill="#fff" {s()}/><rect x="46" y="34" width="36" height="30" fill="#fff" {s()}/>'
    f'<path d="M58 40 Q58 34 64 34 Q70 34 70 40 V56 H58Z" fill="{NV}"/><path d="M60 52 Q60 44 64 44 Q68 44 68 52Z" fill="{GO}" {W(1.8)}/>'
    f'<path d="M44 34 L64 12 L84 34Z" fill="{DG}" {s()}/><path d="M64 12 V2 M60 6 H68" {W(2.4)}/>'
    + f(64, 86, d=8, k=0.65) + f'<rect x="56" y="98" width="16" height="18" rx="8" fill="{BR}" {W(2)}/>' + sp((18, 30, 6), (112, 34, 5)))
I["volokolamsk-park"] = ("orange", "клён-персонаж роняет крылатки-«вертолётики»",
    GROUND + f'<path d="M58 108 V72 H70 V108Z" fill="{BR}" {s()}/>'
    + f'<path d="M64 10 L76 30 L98 24 L90 44 L112 52 L90 62 L96 78 L64 70 L32 78 L38 62 L16 52 L38 44 L30 24 L52 30Z" fill="{R}" {s()}/>'
    + f(64, 50, d=8, k=0.65)
    + "".join(f'<g transform="rotate({a} {x} {y})"><ellipse cx="{x}" cy="{y}" rx="9" ry="4" fill="{Y}" {W(1.8)}/><circle cx="{x-8}" cy="{y}" r="3" fill="{OR}" {W(1.6)}/></g>' for x, y, a in [(24, 92, 30), (100, 96, -20), (110, 80, 40)]))
I["yaropolets-museum"] = ("teal", "маленькая старая ГЭС-плотина с водопадиком",
    f'<path d="M0 96 Q32 90 64 96 T128 96 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'
    f'<rect x="20" y="50" width="88" height="40" rx="4" fill="#E8E2D6" {s()}/>'
    + "".join(f'<rect x="{x}" y="58" width="12" height="16" rx="6" fill="{NV}"/>' for x in (30, 58, 86))
    + "".join(f'<path d="M{x} 90 V112" stroke="#BFE8FF" stroke-width="7"/><path d="M{x} 90 V112" stroke="#fff" stroke-width="2"/>' for x in (36, 64, 92))
    + f'<path d="M14 52 L64 28 L114 52Z" fill="{R}" {s()}/><path d="M86 40 l-6 10 h6 l-4 10 l10 -13 h-6 l4 -7Z" fill="{Y}" {W(1.6)}/>'
    + f(64, 82, d=9, k=0.5) + sp((18, 26, 6)))

# ======================= Шатура =======================
I["shatura-gagarin-park"] = ("pink", "катамаран-персонаж плывёт по пруду-сердечку",
    f'<path d="M64 120 Q10 84 14 52 Q20 26 46 32 Q58 34 64 46 Q70 34 82 32 Q108 26 114 52 Q118 84 64 120Z" fill="#7FD3F7" {s()}/>'
    f'<path d="M30 66 q8 -6 16 0 M78 90 q8 -6 16 0" fill="none" stroke="#fff" stroke-width="3"/>'
    f'<rect x="38" y="70" width="52" height="12" rx="6" fill="{Y}" {s()}/><rect x="40" y="58" width="48" height="14" rx="4" fill="{R}" {s()}/>'
    f'<path d="M52 58 Q52 40 64 40 Q76 40 76 58" fill="none" {W(3)}/>' + f(64, 66, d=8, k=0.45) + sp((20, 20, 5), (110, 18, 6)))
I["shatura-museum"] = ("green", "любопытная куница на ветке из природоведческого зала",
    f'<path d="M0 90 Q64 80 128 96" fill="none" stroke="{BR}" stroke-width="10" stroke-linecap="round"/><path d="M0 90 Q64 80 128 96" fill="none" {W(2)}/>'
    f'<path d="M30 84 Q20 60 40 50 Q70 44 90 60 Q104 70 108 84Z" fill="#8A5A3C" {s()}/>'
    f'<path d="M30 80 Q10 70 8 90 Q12 104 30 98" fill="#8A5A3C" {s()}/>'
    f'<circle cx="92" cy="54" r="18" fill="#8A5A3C" {s()}/><circle cx="80" cy="40" r="6" fill="#8A5A3C" {W(2.2)}/><circle cx="104" cy="40" r="6" fill="#8A5A3C" {W(2.2)}/>'
    f'<path d="M80 62 Q92 76 104 62 Q100 70 92 70 Q84 70 80 62Z" fill="#F2C46A"/>' + f(92, 54, d=6, k=0.5)
    + f'<ellipse cx="92" cy="60" rx="2.6" ry="2" fill="{O}"/>' + sp((24, 26, 6)))
I["shatura-dk-narimanova"] = ("yellow", "петушок-запевала на сцене дома культуры", stage(
    f'<ellipse cx="62" cy="76" rx="20" ry="18" fill="{OR}" {s()}/><path d="M78 72 Q98 54 94 40 Q86 56 80 60 Q90 44 82 34 Q78 56 74 62Z" fill="{G}" {W(2.2)}/>'
    f'<circle cx="54" cy="52" r="12" fill="{OR}" {s()}/><path d="M48 42 Q50 32 56 36 Q58 30 62 38Z" fill="{R}" {W(2)}/>'
    + eye(52, 51, 0.5) + f'<path d="M42 54 L34 56 L42 58Z" fill="{Y}" {W(1.6)}/><path d="M46 60 Q44 66 48 66" fill="{R}" {W(1.6)}/>'
    f'<path d="M56 94 V100 M68 94 V100" stroke="{Y}" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M30 40 q4 -4 2 -8 M26 50 q4 -4 2 -8" fill="none" {W(2)}/>', cur=OR))
I["shatura-kolibri-cinema"] = ("teal", "киноэкран, на экране колибри зависла у цветка", screen(
    f'<path d="M86 60 Q90 74 82 80 Q76 72 86 60Z" fill="{P}" {W(2)}/><path d="M84 80 V86" stroke="{DG}" stroke-width="2.4"/>'
    f'<ellipse cx="54" cy="58" rx="14" ry="9" fill="{TE}" {s()}/><path d="M66 56 L84 62" {W(2.4)}/>'
    f'<path d="M50 52 Q44 34 58 36 Q60 46 56 52Z" fill="{G}" {W(2)}/><path d="M40 60 L28 66 L40 64Z" fill="{TE}" {W(1.8)}/>'
    + eye(60, 55, 0.5) + f'<ellipse cx="54" cy="64" rx="3" ry="1.8" fill="#FF7FA8" opacity=".6"/>', cur=TE))

# ======================= Люберцы =======================
I["lyubertsy-kosmopolis"] = ("night", "ракета-малыш скатывается с горки в сухой бассейн",
    "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="{c}" {W(2)}/>' for x, y, c in
            [(70, 116, Y), (88, 118, B), (106, 114, G), (124, 116, R), (78, 104, P), (98, 104, OR), (116, 102, V)])
    + f'<path d="M6 30 Q40 30 60 70 Q72 96 100 98" fill="none" stroke="{TE}" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M6 30 Q40 30 60 70 Q72 96 100 98" fill="none" {W(2)}/>'
    f'<g transform="rotate(50 46 50)"><path d="M46 22 Q60 36 58 62 H34 Q32 36 46 22Z" fill="#fff" {s()}/>'
    f'<path d="M34 54 L24 68 L34 64Z M58 54 L68 68 L58 64Z" fill="{R}" {W(2)}/><path d="M38 62 L46 76 L54 62Z" fill="{OR}" {W(2)}/></g>'
    + f(46, 48, d=5, k=0.45) + "".join(sparkle(x, y, r, Y) for x, y, r in [(100, 24, 6), (80, 44, 4)]))
I["malakhovka-museum"] = ("green", "дачная резная беседка-персонаж с самоварчиком",
    GROUND + f'<rect x="28" y="56" width="72" height="48" fill="#fff" opacity=".0"/>'
    f'<path d="M30 104 V56 M98 104 V56" stroke="{BR}" stroke-width="6"/>'
    f'<path d="M20 58 Q64 12 108 58Z" fill="{G}" {s()}/><path d="M64 22 V12" {W(3)}/><circle cx="64" cy="10" r="4" fill="{Y}" {W(2)}/>'
    f'<path d="M24 58 H104" stroke="#fff" stroke-width="5"/>'
    + "".join(f'<path d="M{x} 58 q4 8 8 0" fill="none" stroke="#fff" stroke-width="3"/>' for x in range(28, 100, 10))
    + f'<rect x="30" y="86" width="68" height="6" fill="{BR}" {W(2)}/>'
    f'<path d="M54 86 Q50 66 64 64 Q78 66 74 86Z" fill="{GO}" {s()}/><rect x="60" y="56" width="8" height="8" fill="{GO}" {W(1.8)}/>'
    + f(64, 76, d=5, k=0.45))
I["lyubertsy-natashinsky-park"] = ("teal", "горбатый мостик-персонаж над прудом, под ним рыбка",
    f'<path d="M0 84 Q32 78 64 84 T128 84 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'
    f'<path d="M8 86 Q64 30 120 86" fill="none" stroke="{BR}" stroke-width="12"/><path d="M8 86 Q64 30 120 86" fill="none" {W(2)}/>'
    + "".join(f'<path d="M{x} {86-(1-((x-64)/56)**2)*28:.0f} V{74-(1-((x-64)/56)**2)*28:.0f}" stroke="{BR}" stroke-width="3"/>' for x in range(20, 112, 12))
    + f'<path d="M14 {62} Q64 {6} 114 62" fill="none" stroke="{BR}" stroke-width="3"/>' + f(64, 64, d=8, k=0.55)
    + f'<ellipse cx="64" cy="106" rx="12" ry="7" fill="{OR}" {W(2.2)}/><path d="M76 106 L86 100 V112Z" fill="{OR}" {W(2)}/>'
    + eye(58, 105, 0.4) + f'<circle cx="46" cy="96" r="3" fill="none" stroke="#fff" stroke-width="1.6"/>')

# ======================= Одинцово =======================
I["odintsovo-lazutina-park"] = ("blue", "лыжероллер-персонаж с ботинком мчится по трассе парка",
    f'<path d="M0 108 Q64 96 128 108 V128 H0Z" fill="{G}" {W(2.6)}/><path d="M0 112 Q64 100 128 112" fill="none" stroke="{GR}" stroke-width="6"/>'
    f'<rect x="14" y="80" width="100" height="12" rx="6" fill="{R}" {s()}/>'
    f'<circle cx="26" cy="98" r="9" fill="{NV}" {s()}/><circle cx="102" cy="98" r="9" fill="{NV}" {s()}/><circle cx="26" cy="98" r="3" fill="{GR}"/><circle cx="102" cy="98" r="3" fill="{GR}"/>'
    f'<path d="M40 80 V44 Q40 32 52 32 H72 Q80 32 80 44 V62 Q96 64 96 80Z" fill="{B}" {s()}/>'
    f'<path d="M44 44 H76" stroke="#fff" stroke-width="3"/>' + f(62, 62, d=8, k=0.6)
    + f'<path d="M100 20 L84 76 M116 30 L96 80" stroke="{GR}" stroke-width="4" stroke-linecap="round"/>'
    + "".join(f'<path d="M{x} {y} h-10" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(10, 60), (14, 70)]) + sp((20, 24, 5)))
I["odintsovo-museum"] = ("orange", "лупа юного археолога над косточкой в раскопе",
    f'<path d="M0 70 Q64 62 128 70 V128 H0Z" fill="#C99B60" {s()}/>'
    f'<path d="M30 92 Q22 84 30 80 Q36 78 40 84 H84 Q88 78 94 80 Q102 84 94 92 Q102 100 94 104 Q88 106 84 100 H40 Q36 106 30 104 Q22 100 30 92Z" fill="#fff" {s()}/>'
    + f(62, 90, d=7, k=0.5)
    + f'<circle cx="80" cy="38" r="22" fill="#BFE8FF" fill-opacity=".6" stroke="{BR}" stroke-width="6"/><path d="M64 54 L46 72" stroke="{BR}" stroke-width="8" stroke-linecap="round"/>'
    f'<ellipse cx="72" cy="30" rx="6" ry="4" fill="#fff" opacity=".8"/>' + sp((18, 26, 6)))
I["odintsovo-bondareva-theatre"] = ("pink", "медвежонок-артист с бабочкой поёт на сцене", stage(
    f'<circle cx="64" cy="72" r="24" fill="{BR}" {s()}/><circle cx="46" cy="52" r="8" fill="{BR}" {s()}/><circle cx="82" cy="52" r="8" fill="{BR}" {s()}/>'
    f'<ellipse cx="64" cy="80" rx="11" ry="8" fill="#E8C49A"/>' + f(64, 70, d=8, k=0.6)
    + f'<path d="M54 96 L64 92 L74 96 L74 88 L64 92 L54 88Z" fill="{R}" {W(1.8)}/>', cur=P))
I["odintsovo-mechta-ksc"] = ("purple", "единорожек мечтательно выходит на сцену", stage(
    f'<circle cx="64" cy="70" r="24" fill="#fff" {s()}/><path d="M60 46 L64 22 L68 46Z" fill="{Y}" {W(2.2)}/>'
    f'<path d="M44 52 L42 40 L52 48Z M84 52 L86 40 L76 48Z" fill="#fff" {W(2.2)}/>'
    f'<path d="M46 56 Q40 70 46 86 M50 52 Q44 66 50 80" fill="none" stroke="{P}" stroke-width="5" stroke-linecap="round"/>'
    + f(66, 72, d=8, k=0.6) + "".join(sparkle(x, y, r, Y) for x, y, r in [(44, 30, 4), (88, 30, 5)]), cur=V))
I["odintsovo-misty-park"] = ("sky", "облачко-туманчик катается на тарзанке",
    f'<path d="M64 0 L46 62 M64 0 L82 62" {W(2.6)}/><rect x="40" y="60" width="48" height="6" rx="3" fill="{BR}" {W(2)}/>'
    f'<path d="M30 90 Q22 72 40 68 Q46 52 64 56 Q80 50 88 66 Q106 66 102 84 Q108 98 90 100 H40 Q24 100 30 90Z" fill="#fff" {s()}/>'
    + f(64, 82, d=8, k=0.65)
    + "".join(f'<path d="M{x} {y} h-14" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(20, 70), (16, 84)])
    + sp((110, 24, 6), (20, 30, 5)))
I["usovo-school-museum"] = ("yellow", "старинная школьная парта-персонаж с чернильницей и пёрышком",
    f'<path d="M34 76 V120 M94 76 V120" stroke="{BR}" stroke-width="6"/><path d="M28 120 H44 M84 120 H100" {W(4)}/>'
    f'<path d="M16 56 L112 50 L116 72 L20 78Z" fill="#6B8F4E" {s()}/><rect x="20" y="78" width="96" height="16" fill="#6B8F4E" {s()}/>'
    + f(66, 86, d=9, k=0.5)
    + f'<rect x="84" y="38" width="16" height="16" rx="3" fill="{NV}" {W(2.2)}/><path d="M94 40 Q104 14 116 10 Q108 26 96 40Z" fill="#fff" {W(2)}/>'
    + sp((18, 26, 6)))
I["bolshie-vyazemy"] = ("green", "кот учёный на золотой цепи у дуба",
    GROUND + f'<path d="M84 110 Q88 70 82 40 H104 Q98 70 108 110Z" fill="{BR}" {s()}/>'
    f'<circle cx="94" cy="24" r="26" fill="{DG}" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="{GO}" {W(1.6)}/>' for x, y in [(82, 54), (74, 60), (68, 68), (64, 76)])
    + f'<ellipse cx="48" cy="88" rx="22" ry="20" fill="{GR}" {s()}/><circle cx="48" cy="58" r="18" fill="{GR}" {s()}/>'
    f'<path d="M34 48 L32 30 L46 42Z M62 48 L64 30 L50 42Z" fill="{GR}" {W(2.2)}/>' + f(48, 58, d=6, k=0.5)
    + f'<rect x="34" y="80" width="28" height="18" rx="2" fill="{R}" {W(2.2)}/><path d="M48 80 V98" {W(1.6)}/>'
    f'<rect x="36" y="34" width="24" height="6" fill="{NV}" {W(1.8)}/><path d="M32 34 L48 26 L64 34Z" fill="{NV}" {W(1.8)}/>')
I["malevich-park"] = ("orange", "«Чёрный квадрат»-персонаж гуляет по парку",
    GROUND + f'<rect x="34" y="28" width="60" height="60" fill="{NV}" {s()}/>'
    + f(64, 56, d=10, k=0.8).replace(f'fill="{O}"', 'fill="#fff"', 2)
    + f'<path d="M50 88 L44 108 M78 88 L84 108" {W(4)}/><path d="M34 60 L20 72 M94 60 L108 50" {W(4)}/>'
    f'<circle cx="110" cy="46" r="7" fill="{R}" {W(2)}/><path d="M18 30 L26 22 L34 30 L26 38Z" fill="{Y}" {W(2)}/>')

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
