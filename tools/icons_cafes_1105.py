"""Иконки робота cafes, 2026-11-05: 20 новых сюжетов «кухня, посуда, еда» (сверено с icons-catalog и subjects.txt)."""
import os
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=8, k=0.7, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); src = os.path.join(here, "..", "icons-src")

ICONS = {
    # тандыр — глиняная печь с лепёшкой на стенке
    "cafe-chaihona-alabyana": ("orange", "тандыр (глиняная печь)",
        f'<path d="M26 108 Q20 60 40 40 H88 Q108 60 102 108Z" fill="#D9895B" {s()}/>'
        f'<ellipse cx="64" cy="40" rx="24" ry="8" fill="#5A3A2A" {s()}/>'
        f'<path d="M30 74 Q64 82 98 74 M28 92 Q64 100 100 92" fill="none" stroke="#B5663E" stroke-width="3"/>'
        f'<path d="M80 20 Q84 28 80 34 M66 14 Q70 24 66 32" fill="none" stroke="#fff" stroke-width="3" opacity=".8"/>'
        + f(64, 62, d=9, k=0.8) + f'<ellipse cx="96" cy="58" rx="10" ry="7" fill="#F2C46B" {W(2.4)}/>'),
    # бамбуковая пароварка с мантами
    "cafe-chaihona-ulyanova": ("teal", "бамбуковая пароварка с мантами",
        f'<path d="M20 70 H108 V98 Q108 106 100 106 H28 Q20 106 20 98Z" fill="#E7C27D" {s()}/>'
        f'<path d="M20 80 H108 M20 92 H108" stroke="#B88A45" stroke-width="3"/>'
        f'<ellipse cx="64" cy="70" rx="44" ry="10" fill="#F4DFAE" {s()}/>'
        + "".join(f'<path d="M{x-11} 72 Q{x-10} 56 {x} 52 Q{x+10} 56 {x+11} 72Z" fill="#FFF8EC" {W(2.4)}/>' for x in (44, 64, 84))
        + f'<path d="M50 40 Q54 32 50 24 M64 38 Q68 30 64 22 M78 40 Q82 32 78 24" fill="none" stroke="#fff" stroke-width="3"/>'
        + f(64, 90, d=8, k=0.6)),
    # ступка с пестиком
    "cafe-chaihona-zheleznodorozhny": ("purple", "ступка с пестиком",
        f'<path d="M78 18 L96 26 L70 70 L60 64Z" fill="#C9A27A" {s()}/>'
        f'<path d="M22 58 H106 Q104 96 76 104 H52 Q24 96 22 58Z" fill="#9AA6B8" {s()}/>'
        f'<ellipse cx="64" cy="58" rx="42" ry="9" fill="#6E7A8E" {s()}/>'
        f'<path d="M48 104 H80 L84 112 H44Z" fill="#7E8AA0" {W(2.6)}/>' + f(64, 80, d=10, k=0.8) + sparkle(26, 30, 6)),
    # турка для кофе
    "cafe-chaihona-belaya-dacha": ("yellow", "турка для кофе",
        f'<path d="M36 46 H80 L74 100 Q72 106 64 106 H52 Q44 106 42 100Z" fill="#E08A3C" {s()}/>'
        f'<path d="M30 42 Q58 34 86 42 L80 48 H36Z" fill="#F2A65A" {s()}/>'
        f'<path d="M80 56 L112 44 L114 52 L80 66" fill="#7A4A2A" {s()}/>'
        f'<path d="M50 28 Q54 20 50 12 M62 28 Q66 20 62 12" fill="none" stroke="#fff" stroke-width="3"/>'
        + f(58, 74, d=9, k=0.75) + f'<path d="M40 92 H76" stroke="#B5662A" stroke-width="3"/>'),
    # мясорубка
    "cafe-chaihona-mega-khimki": ("pink", "мясорубка",
        f'<path d="M38 26 H66 L62 46 H42Z" fill="#B7C2D2" {s()}/>'
        f'<rect x="30" y="46" width="58" height="34" rx="12" fill="#C9D3E0" {s()}/>'
        f'<circle cx="94" cy="63" r="10" fill="#8E9AAE" {s()}/><path d="M100 56 L112 40 L118 46" fill="none" {W(4)}/>'
        f'<circle cx="118" cy="46" r="5" fill="#E8654F" {W(2.4)}/>'
        f'<path d="M46 80 L42 108 H76 L72 80" fill="#9AA6B8" {s()}/>' + f(58, 62, d=9, k=0.7)
        + f'<path d="M90 96 Q96 100 92 106 M100 92 Q106 98 102 104" fill="none" stroke="#E8654F" stroke-width="4"/>'),
    # ананас
    "cafe-chaihona-ostrov-mechty": ("green", "ананас",
        f'<path d="M64 46 L50 18 L60 30 L64 12 L68 30 L78 18Z" fill="#4FB45A" {s()}/>'
        f'<ellipse cx="64" cy="80" rx="28" ry="34" fill="#FFC23D" {s()}/>'
        f'<path d="M42 62 L86 102 M38 82 L70 112 M50 50 L90 86 M86 62 L42 102 M90 82 L58 112 M78 50 L38 86" stroke="#D99A1E" stroke-width="2.4" opacity=".8"/>'
        + f(64, 80, d=10, k=0.8) + sparkle(104, 30, 6)),
    # поварёшка
    "cafe-chaihona-europolis": ("blue", "поварёшка с супом",
        f'<path d="M84 16 Q92 14 94 22 L74 76 L66 72Z" fill="#C9D3E0" {s()}/>'
        f'<path d="M24 74 Q24 108 56 108 Q88 108 88 74Z" fill="#C9D3E0" {s()}/>'
        f'<ellipse cx="56" cy="74" rx="32" ry="7" fill="#F2A65A" {s()}/>'
        f'<circle cx="46" cy="73" r="3" fill="#7CD26E"/><circle cx="62" cy="75" r="3" fill="#E8654F"/>' + f(56, 90, d=9, k=0.75)),
    # солонка и перечница
    "cafe-chaihona-avenue": ("sky", "солонка и перечница",
        f'<path d="M22 48 Q22 34 40 34 Q58 34 58 48 V100 Q58 106 52 106 H28 Q22 106 22 100Z" fill="#FFFFFF" {s()}/>'
        f'<path d="M70 48 Q70 34 88 34 Q106 34 106 48 V100 Q106 106 100 106 H76 Q70 106 70 100Z" fill="#4A4060" {s()}/>'
        f'<path d="M24 46 H56 M72 46 H104" stroke="#A9B4C6" stroke-width="5"/>'
        + "".join(f'<circle cx="{x}" cy="40" r="1.8" fill="{O}"/>' for x in (34, 40, 46))
        + "".join(f'<circle cx="{x}" cy="40" r="1.8" fill="#fff"/>' for x in (82, 88, 94))
        + f(40, 74, d=7, k=0.6) + eye(81, 74, 0.6).replace(O, "#fff") + eye(95, 74, 0.6).replace(O, "#fff")
        + f'<path d="M84 82 Q88 86 92 82" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'),
    # миксер
    "cafe-chaihona-afimall": ("purple", "ручной миксер",
        f'<path d="M24 34 Q24 22 40 22 H92 Q106 22 104 36 L98 56 H34 Q24 54 24 34Z" fill="#FF8FB8" {s()}/>'
        f'<path d="M84 22 Q100 8 108 22" fill="none" {W(5)}/>'
        f'<path d="M46 56 V72 M74 56 V72" {W(4)}/>'
        + "".join(f'<path d="M{x} 72 Q{x-12} 96 {x} 108 Q{x+12} 96 {x} 72Z" fill="none" {W(3)}/>' for x in (46, 74))
        + f(62, 38, d=9, k=0.7) + sparkle(110, 92, 6)),
    # кухонные весы
    "cafe-chaihona-crocus": ("teal", "кухонные весы",
        f'<ellipse cx="64" cy="40" rx="40" ry="10" fill="#C9D3E0" {s()}/>'
        f'<path d="M60 48 H68 V60 H60Z" fill="#8E9AAE" {W(2.4)}/>'
        f'<path d="M26 104 Q22 60 64 60 Q106 60 102 104Z" fill="#FF9A6A" {s()}/>'
        f'<circle cx="64" cy="82" r="16" fill="#fff" {W(2.6)}/><path d="M64 82 L72 72" {W(2.6)}/>'
        f'<circle cx="46" cy="32" r="8" fill="#E8654F" {W(2.4)}/><circle cx="64" cy="30" r="8" fill="#7CD26E" {W(2.4)}/><circle cx="82" cy="32" r="8" fill="#FFD25E" {W(2.4)}/>'
        + eye(56, 82, 0.5) + eye(72, 82, 0.5)),
    # дуршлаг
    "cafe-chaihona-kaleidoskop": ("orange", "дуршлаг с макаронами",
        f'<path d="M16 56 H112" {W(5)}/>'
        f'<path d="M24 56 Q24 104 64 104 Q104 104 104 56Z" fill="#7CC6F2" {s()}/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{O}" opacity=".6"/>' for x, y in
                  [(38, 92), (52, 98), (76, 98), (90, 92), (34, 74), (94, 74)])
        + f'<path d="M30 56 Q40 40 50 56 Q60 38 70 56 Q80 40 90 56 Q96 44 100 56" fill="#FFD25E" {W(2.6)}/>'
        + f(64, 78, d=9, k=0.75)),
    # разделочная доска с овощами
    "cafe-chaihona-salaris": ("green", "разделочная доска с овощами",
        f'<path d="M16 50 Q16 40 26 40 H96 Q108 40 108 52 V96 Q108 106 98 106 H26 Q16 106 16 96Z" fill="#E7B477" {s()}/>'
        f'<circle cx="112" cy="72" r="5" fill="none" {W(2.6)}/>'
        f'<circle cx="38" cy="66" r="11" fill="#E8654F" {W(2.6)}/><path d="M34 56 L38 52 L42 56" fill="#4FB45A" {W(2)}/>'
        f'<path d="M58 84 L92 60 Q100 58 98 66 L66 92 Q56 94 58 84Z" fill="#FF9A3C" {W(2.6)}/>'
        f'<circle cx="38" cy="90" r="6" fill="#7CD26E" {W(2.2)}/><circle cx="50" cy="94" r="5" fill="#7CD26E" {W(2.2)}/>'
        + f(74, 52, d=7, k=0.55, mouth=False) + f'<path d="M70 58 Q74 61 78 58" fill="none" {W(2.2)}/>'),
    # тостер с тостом
    "cafe-chaihona-metropolis": ("yellow", "тостер с тостом",
        f'<path d="M44 20 Q44 12 54 12 H74 Q84 12 84 20 V52 H44Z" fill="#F2C46B" {s()}/>'
        f'<path d="M48 22 Q64 16 80 22" fill="none" stroke="#C98B3A" stroke-width="3"/>'
        f'<rect x="20" y="44" width="88" height="62" rx="16" fill="#9FD3F5" {s()}/>'
        f'<path d="M36 46 H58 M70 46 H92" {W(4)}/><path d="M108 66 H116" {W(4)}/>'
        + f(64, 76, d=10, k=0.8) + eye(58, 30, 0.45) + eye(70, 30, 0.45)),
    # крендель
    "cafe-uryuk-semenovskaya": ("orange", "крендель",
        f'<path d="M64 98 C24 112 10 70 34 48 C54 30 74 56 64 74 C54 56 74 30 94 48 C118 70 104 112 64 98Z" fill="none" stroke="{O}" stroke-width="20" stroke-linejoin="round"/>'
        f'<path d="M64 98 C24 112 10 70 34 48 C54 30 74 56 64 74 C54 56 74 30 94 48 C118 70 104 112 64 98Z" fill="none" stroke="#C9803E" stroke-width="13" stroke-linejoin="round"/>'
        + "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.4" ry="1.4" fill="#fff"/>' for x, y in [(28, 64), (40, 44), (86, 44), (102, 66), (44, 98), (84, 98)])
        + f(64, 84, d=7, k=0.55) + sparkle(106, 22, 6)),
    # печенье с предсказанием
    "cafe-uryuk-riviera": ("pink", "печенье с предсказанием",
        f'<path d="M18 80 Q20 40 56 38 Q72 40 64 62 Q60 72 72 70 Q96 66 110 80 Q98 106 64 104 Q26 104 18 80Z" fill="#F2C46B" {s()}/>'
        f'<path d="M60 64 L96 46 L100 54 L66 72Z" fill="#fff" {W(2.4)}/><path d="M72 58 L90 50" stroke="#E8654F" stroke-width="2"/>'
        + f(48, 82, d=9, k=0.7)),
    # кокос
    "cafe-uryuk-shchelkovsky": ("teal", "кокос с трубочкой",
        f'<path d="M84 14 L76 50" {W(5)}/><path d="M84 14 L76 50" stroke="#FF8FB8" stroke-width="2.6"/>'
        f'<circle cx="64" cy="76" r="36" fill="#8A5A3A" {s()}/>'
        f'<path d="M30 64 Q64 50 98 64 Q64 58 30 64Z" fill="#fff" {W(2.4)}/>'
        f'<path d="M40 92 L46 96 M86 96 L92 92 M60 104 L66 104" stroke="#5A3A2A" stroke-width="2.4"/>'
        + f(64, 80, d=10, k=0.8) + sparkle(24, 28, 6)),
    # груша
    "cafe-uryuk-vdnh": ("sky", "груша",
        f'<path d="M64 26 Q66 16 72 12" fill="none" {W(4)}/><path d="M68 20 Q84 8 94 18 Q82 28 68 20Z" fill="#4FB45A" {W(2.6)}/>'
        f'<path d="M64 26 Q48 26 48 48 Q48 60 38 72 Q26 90 40 104 Q52 114 64 112 Q76 114 88 104 Q102 90 90 72 Q80 60 80 48 Q80 26 64 26Z" fill="#C7E25A" {s()}/>'
        + f(64, 84, d=9, k=0.75) + f'<ellipse cx="54" cy="46" rx="4" ry="7" fill="#fff" opacity=".6"/>'),
    # кухонная плита с духовкой
    "cafe-uryuk-evropeisky": ("purple", "кухонная плита с духовкой",
        f'<rect x="24" y="30" width="80" height="80" rx="10" fill="#F4F4FA" {s()}/>'
        f'<path d="M24 50 H104" {W(3)}/>'
        + "".join(f'<circle cx="{x}" cy="40" r="4" fill="#A98BF0" {W(2)}/>' for x in (40, 56, 72, 88))
        + f'<rect x="34" y="60" width="60" height="40" rx="6" fill="#FFB77A" {s()}/>'
        f'<path d="M44 64 H84" {W(3)}/>'
        f'<path d="M40 20 Q48 12 56 20 M70 20 Q78 12 86 20" fill="none" stroke="#fff" stroke-width="3"/>'
        + f(64, 82, d=9, k=0.7)),
    # блендер
    "cafe-uryuk-marshala-zhukova": ("pink", "блендер со смузи",
        f'<path d="M38 16 H90 V24 H38Z" fill="#7A6AA8" {W(2.6)}/>'
        f'<path d="M40 24 H88 L80 84 H48Z" fill="#D9F2FF" {s()}/>'
        f'<path d="M44 50 H84 L80 84 H48Z" fill="#FF7FA8" {W(2.4)}/>'
        f'<path d="M88 34 Q100 34 98 52 Q96 62 84 64" fill="none" {W(3)}/>'
        f'<path d="M40 84 H88 Q94 84 94 92 V108 H34 V92 Q34 84 40 84Z" fill="#7A6AA8" {s()}/>'
        f'<circle cx="64" cy="97" r="5" fill="#FFD25E" {W(2.2)}/>' + f(64, 64, d=8, k=0.65)),
    # тёрка
    "cafe-uryuk-prime-park": ("yellow", "тёрка с сыром",
        f'<path d="M52 18 H76 Q80 18 80 24 V30 H48 V24 Q48 18 52 18Z" fill="#E8654F" {W(2.6)}/>'
        f'<path d="M46 30 H82 L94 106 H34Z" fill="#C9D3E0" {s()}/>'
        + "".join(f'<path d="M{x} {y} q3 -3 6 0" fill="none" stroke="{O}" stroke-width="2"/>' for x, y in
                  [(46, 80), (58, 80), (70, 80), (82, 80), (44, 92), (56, 92), (68, 92), (80, 92)])
        + f'<path d="M96 96 L116 90 L114 108 Z" fill="#FFD25E" {W(2.4)}/>' + f(64, 58, d=9, k=0.7)),
}

if __name__ == "__main__":
    for pid, (bg, subj, body) in ICONS.items():
        open(os.path.join(src, pid + ".svg"), "w").write(svg(bg, body))
    print(len(ICONS))
