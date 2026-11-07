"""Иконки робота fun (2026-11-07, после полудня): 11 мест — Дом Гоголя, «На Донской», ZOOландия, «Еда Руси»,
Музей органической культуры, «Усадьба Костино», «Непоседы», «Наутико», «Все сейчас хорошо», ДШИ — музыкальный театр
и ДК «Мир» (Реутов). Каждая иконка придумана отдельно (правило абсолютной уникальности 07.11). Сверено со всеми
icons-catalog/sheet-*.png и icons-src/subjects.txt (заняты: хохломская ложка, чугунок, погремушка, мяч-прыгун,
аквапалка, пеликан, белуха, ламантин, утконос, свистулька, номерок, рубанок, неваляшка, домовой — не брать).
Запуск: python3 tools/icons_fun_1107d.py [id ...]  (печатает строки для subjects.txt)"""
import os, sys
from draw_icons import s, eye, face, sparkle, O

W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
GO = "#F2B632"


def svg(a, b, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<defs>
 <radialGradient id="g" cx="38%" cy="28%" r="85%"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></radialGradient>
 <clipPath id="c"><circle cx="64" cy="64" r="61"/></clipPath>
</defs>
<circle cx="64" cy="64" r="61" fill="url(#g)"/>
<g clip-path="url(#c)">{body}</g>
<ellipse cx="44" cy="22" rx="20" ry="7" fill="#fff" opacity=".3"/>
</svg>'''


def note(x, y, c="#fff", k=1.0):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{4.4*k:.1f}" ry="{3.4*k:.1f}" fill="{c}" {W(1.6)} transform="rotate(-20 {x} {y})"/>'
            f'<path d="M{x+4*k:.1f} {y-1} V{y-16*k:.1f} Q{x+9*k:.1f} {y-12*k:.1f} {x+10*k:.1f} {y-8*k:.1f}" fill="none" {W(1.8)}/>')


I = {}

# 1. ZOOландия — хорёк из игрового туннеля
I["zoolandiya-istra"] = ("#E8FFF0", "#5DBB8A",
    "хорёк-фретка с тёмной маской на мордочке", "выныривает из жёлтого игрового туннеля-трубы на детской площадке зооклуба",
    f'<path d="M0 104 Q64 96 128 104 V128 H0Z" fill="#7CCB6A" {s()}/>'
    f'<rect x="-6" y="70" width="80" height="38" rx="6" fill="#FFC93C" {s()}/>'
    + "".join(f'<path d="M{x} 70 V108" stroke="#E8A21E" stroke-width="3"/>' for x in (14, 34, 54))
    + f'<ellipse cx="74" cy="89" rx="11" ry="19" fill="#F0B02A" {s()}/><ellipse cx="74" cy="89" rx="6" ry="13" fill="#5A3A1A"/>'
    f'<path d="M74 90 Q78 64 92 52" fill="none" stroke="{O}" stroke-width="25" stroke-linecap="round"/>'
    f'<path d="M74 90 Q78 64 92 52" fill="none" stroke="#FFF1DC" stroke-width="19" stroke-linecap="round"/>'
    f'<ellipse cx="94" cy="44" rx="21" ry="17" fill="#FFF1DC" {s()}/>'
    f'<circle cx="78" cy="30" r="6" fill="#8A5A3A" {W(2.4)}/><circle cx="110" cy="30" r="6" fill="#8A5A3A" {W(2.4)}/>'
    f'<path d="M76 44 Q94 32 112 44 Q110 52 94 50 Q78 52 76 44Z" fill="#7A4A2E"/>'
    + eye(86, 44, 0.8) + eye(102, 44, 0.8)
    + f'<ellipse cx="94" cy="54" rx="3.4" ry="2.6" fill="#FF8FA8" {W(1.6)}/>'
    f'<path d="M89 58 Q94 62 99 58" fill="none" {W(2)}/>'
    f'<ellipse cx="66" cy="76" rx="6" ry="4" fill="#FFF1DC" {W(2.2)}/><ellipse cx="84" cy="74" rx="6" ry="4" fill="#FFF1DC" {W(2.2)}/>'
    + sp((24, 30, 5), (50, 16, 3)))

# 2. «Еда Руси» — горшок щей в ухвате
I["eda-rusi-zhavoronki"] = ("#FFF1E0", "#E8915A",
    "глиняный горшок со щами", "ухват выносит его из устья русской печи, а над щами вьются три струйки пара",
    f'<path d="M84 128 V78 Q106 46 132 78 V128Z" fill="#FAF4EA" {s()}/>'
    f'<path d="M96 128 V96 Q108 80 122 96 V128Z" fill="#3D2A22"/>'
    f'<path d="M100 118 q4 -10 8 0 q4 -8 8 0" fill="#FF8A2A"/>'
    f'<path d="M4 124 L44 100" stroke="{O}" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M4 124 L44 100" stroke="#C98B4E" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M36 86 Q36 110 62 110 Q88 110 88 86" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>'
    f'<path d="M36 86 Q36 110 62 110 Q88 110 88 86" fill="none" stroke="#9AA3AE" stroke-width="4.4" stroke-linecap="round"/>'
    f'<path d="M40 64 Q34 96 50 104 Q62 108 74 104 Q90 96 84 64Z" fill="#B8552E" {s()}/>'
    f'<rect x="36" y="56" width="52" height="12" rx="6" fill="#C9683A" {s()}/>'
    f'<path d="M42 58 Q62 50 82 58" fill="#7BBF5A" {W(2.2)}/>'
    f'<path d="M44 92 Q62 98 80 92" fill="none" stroke="#8E3E20" stroke-width="3"/>'
    + f'<g>{f(62, 80, d=9, k=0.7)}</g>'
    + "".join(f'<path d="M{x} 48 q-6 -8 0 -16 q6 -8 0 -16" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" opacity=".9"/>' for x in (50, 62, 74))
    + sp((20, 30, 4), (104, 22, 3)))

# 3. Музей органической культуры — мобиль
I["kolomna-organic-culture"] = ("#FFFFFF", "#C8C3E8",
    "подвесная скульптура-мобиль из цветных кругов на проволоке", "покачивается под потолком белого зала галереи и бросает на стену цветные тени",
    f'<rect x="0" y="112" width="128" height="16" fill="#E9E6F2" {W(2)}/>'
    f'<ellipse cx="30" cy="112" rx="12" ry="3" fill="#E8453C" opacity=".25"/><ellipse cx="104" cy="114" rx="14" ry="3" fill="#F2B632" opacity=".3"/>'
    f'<path d="M58 0 V26" stroke="{O}" stroke-width="2.4"/>'
    f'<path d="M18 30 Q58 22 98 30" fill="none" stroke="{O}" stroke-width="3"/>'
    f'<path d="M22 30 V46 M94 30 V56" stroke="{O}" stroke-width="2.2"/>'
    f'<circle cx="22" cy="58" r="13" fill="#E8453C" {s()}/>'
    f'<path d="M68 58 Q94 52 120 60" fill="none" stroke="{O}" stroke-width="3"/>'
    f'<path d="M72 58 V78 M116 60 V72" stroke="{O}" stroke-width="2.2"/>'
    f'<circle cx="72" cy="88" r="10" fill="#3E7FE0" {s()}/>'
    f'<circle cx="104" cy="90" r="20" fill="#F2B632" {s()}/>'
    + f'<g>{f(104, 88, d=7, k=0.6)}</g>'
    + f'<path d="M48 50 L58 38 L66 52Z" fill="#1E1E2E" {W(2)}/>'
    f'<path d="M6 36 q4 4 0 8 M126 70 q-4 4 0 8" fill="none" stroke="#A9A3CF" stroke-width="2.4" stroke-linecap="round"/>')

# 4. Усадьба Костино — сапожная колодка
I["korolev-usadba-kostino"] = ("#EAF5DA", "#8FB46A",
    "деревянная сапожная колодка в форме ботинка", "на верстаке трудовой коммуны маленький молоточек вбивает гвоздик в её новую кожаную подошву",
    f'<rect x="0" y="100" width="128" height="28" fill="#A0663A" {s()}/>'
    f'<path d="M0 108 H128" stroke="#7E4A26" stroke-width="2"/>'
    f'<path d="M26 92 Q22 60 34 42 Q46 32 60 40 L66 60 Q96 62 108 76 Q114 86 106 92Z" fill="#E7C08A" {s()}/>'
    f'<path d="M24 92 H108 Q112 98 106 100 H26 Q20 98 24 92Z" fill="#5A3322" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="96" r="1.6" fill="#D8D8D8"/>' for x in (36, 48, 60, 72, 84, 96))
    + f'<path d="M40 50 Q48 46 54 52" fill="none" stroke="#C99A5E" stroke-width="2.4"/>'
    + f'<g>{f(64, 74, d=9, k=0.7)}</g>'
    + f'<g transform="rotate(-28 92 38)"><rect x="88" y="26" width="7" height="34" rx="3" fill="#C98B4E" {W(2.4)}/>'
    f'<rect x="78" y="18" width="28" height="12" rx="3" fill="#8C96A3" {s()}/></g>'
    f'<path d="M100 76 V68" stroke="{O}" stroke-width="2.4"/><circle cx="100" cy="67" r="2" fill="#B0B8C2" {W(1.6)}/>'
    f'<path d="M110 54 l6 -4 M112 62 l8 0 M104 48 l2 -7" stroke="{O}" stroke-width="2.4" stroke-linecap="round"/>'
    + sp((20, 24, 4), (52, 16, 3)))

# 5. «Непоседы» — тёщин язык
I["ramenskoe-neposedy"] = ("#FFE6F0", "#F0709E",
    "праздничная дудка «тёщин язык» в полоску", "дует изо всех сил и разворачивает свой язычок над мягкими матами игровой комнаты",
    f'<rect x="-4" y="104" width="46" height="26" rx="6" fill="#7AC8F2" {s()}/><rect x="42" y="106" width="46" height="24" rx="6" fill="#FFD25E" {s()}/>'
    f'<rect x="88" y="104" width="46" height="26" rx="6" fill="#8ED07A" {s()}/>'
    f'<rect x="8" y="62" width="22" height="16" rx="5" fill="#B49BFF" {s()}/>'
    f'<path d="M30 60 Q60 46 82 58 Q104 70 108 52 Q112 34 96 32 Q84 32 86 44 Q88 52 96 48" fill="none" stroke="{O}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M30 60 Q60 46 82 58 Q104 70 108 52 Q112 34 96 32 Q84 32 86 44 Q88 52 96 48" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<path d="M30 60 Q60 46 82 58 Q104 70 108 52 Q112 34 96 32 Q84 32 86 44 Q88 52 96 48" fill="none" stroke="#E8453C" stroke-width="16" stroke-dasharray="7 7" stroke-linejoin="round"/>'
    + f'<ellipse cx="54" cy="56" rx="17" ry="12" fill="#FFF" {W(2.4)}/>'
    + f'<g>{f(54, 54, d=7, k=0.6)}</g>'
    + "".join(f'<rect x="{x}" y="{y}" width="6" height="6" fill="{c}" transform="rotate({r} {x} {y})"/>' for x, y, c, r in
              [(20, 30, "#FFD25E", 20), (40, 18, "#5CC8F0", -10), (70, 24, "#7CD26E", 30), (114, 80, "#FFD25E", 10), (24, 88, "#fff", 0)])
    + sp((118, 22, 4), (66, 90, 3)))

# 6. Термы «Наутико» — гейзер
I["vidnoe-nautiko"] = ("#E6FAFF", "#3FA6C9",
    "тёплый гейзер-фонтан из бирюзовой воды", "бьёт из каменной купели терм и подкидывает на макушке надувной мячик, а вокруг клубится пар",
    f'<ellipse cx="64" cy="112" rx="58" ry="18" fill="#9A9AA6" {s()}/>'
    f'<ellipse cx="64" cy="108" rx="48" ry="12" fill="#5ED6E0" {W(2.4)}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#B8B8C4" {W(2)}/>' for x, y, r in [(14, 112, 7), (112, 114, 8), (34, 122, 6), (94, 124, 6)])
    + f'<path d="M44 108 Q46 72 50 46 Q40 40 46 32 Q56 26 64 32 Q72 26 82 32 Q88 40 78 46 Q82 72 84 108Z" fill="#7FE3EC" {s()}/>'
    f'<path d="M56 100 Q58 76 60 54 M72 100 Q70 76 68 54" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>'
    + f'<g>{f(64, 76, d=8, k=0.7)}</g>'
    + f'<circle cx="64" cy="18" r="11" fill="#fff" {s()}/>'
    f'<path d="M53 18 Q64 10 75 18 M53 18 Q64 26 75 18" fill="none" stroke="#E8453C" stroke-width="3"/>'
    f'<path d="M64 7 V29" stroke="#3E7FE0" stroke-width="3"/>'
    + "".join(f'<path d="M{x} {y} q-6 -6 0 -12 q6 -6 0 -12" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".85"/>' for x, y in [(22, 96), (30, 80), (104, 96), (98, 78)])
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#BFF3F8" {W(1.6)}/>' for x, y in [(40, 40), (90, 38), (36, 56), (94, 58)]))

# 7. «Все сейчас хорошо» — муфельная печь
I["noginsk-vse-horosho"] = ("#E0F4F2", "#4A9E99",
    "муфельная печь для обжига керамики из огнеупорного кирпича", "через щёлку приоткрытой дверцы видно, как раскалились глиняные вазочки, а на крыше остывает свежерасписанная чашка",
    f'<rect x="0" y="112" width="128" height="16" fill="#3E7E7A" {W(2)}/>'
    f'<rect x="24" y="42" width="80" height="70" rx="6" fill="#E9D9B8" {s()}/>'
    + "".join(f'<path d="M24 {y} H104" stroke="#CDB68C" stroke-width="2"/>' for y in (56, 70, 84, 98))
    + "".join(f'<path d="M{x} {y} v14" stroke="#CDB68C" stroke-width="2"/>' for x, y in [(44, 42), (84, 42), (64, 56), (44, 70), (84, 70), (64, 84), (44, 98), (84, 98)])
    + f'<rect x="38" y="62" width="52" height="40" rx="3" fill="#FF8A2A" {s()}/>'
    f'<rect x="44" y="68" width="40" height="28" fill="#FFD25E"/>'
    f'<path d="M50 96 Q46 84 52 78 Q58 84 54 96Z M64 96 Q58 82 66 72 Q74 82 68 96Z M76 96 Q72 86 78 80 Q84 86 80 96Z" fill="#B8552E" {W(1.6)}/>'
    f'<path d="M90 70 H98 V94 H90" fill="none" stroke="{O}" stroke-width="3.4" stroke-linecap="round"/>'
    + eye(52, 50, 0.6) + eye(76, 50, 0.6)
    + f'<path d="M60 53 Q64 56 68 53" fill="none" {W(2)}/>'
    f'<path d="M30 112 v6 M98 112 v6" stroke="{O}" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M48 42 Q48 26 54 24 H74 Q80 26 80 42Z" fill="#3E7FE0" {s()}/>'
    f'<path d="M80 30 Q90 30 88 38 Q86 42 80 40" fill="none" stroke="{O}" stroke-width="3"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#fff"/>' for x, y in [(56, 30), (64, 34), (72, 29), (60, 38), (70, 38)])
    + "".join(f'<path d="M{x} 18 q-4 -5 0 -10" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x in (58, 68))
    + "".join(f'<path d="M{x} 74 q4 -4 0 -8 q-4 -4 0 -8" fill="none" stroke="#FFB070" stroke-width="2.6" stroke-linecap="round"/>' for x in (12, 116))
    + sp((18, 34, 4)))

# 8. Дом Гоголя — Нос майора Ковалёва
I["gogol-house"] = ("#EEF0F8", "#8E9AC4",
    "сбежавший Нос майора Ковалёва в зелёном мундире с эполетами и треуголке", "важно шагает по Никитскому бульвару, опираясь на трость",
    f'<path d="M0 110 H128 V128 H0Z" fill="#C9B79A" {W(2)}/>'
    f'<circle cx="16" cy="66" r="14" fill="#7CB86A" {W(2)}/><rect x="14" y="78" width="4" height="32" fill="#7A5A3A"/>'
    f'<circle cx="114" cy="62" r="13" fill="#7CB86A" {W(2)}/><rect x="112" y="73" width="4" height="37" fill="#7A5A3A"/>'
    f'<path d="M60 22 Q46 56 42 78 Q40 96 56 98 Q60 104 68 100 Q84 102 86 88 Q88 76 76 72 Q70 50 60 22Z" fill="#F6C6A6" {s()}/>'
    f'<ellipse cx="62" cy="94" rx="4" ry="2.6" fill="#B8705A"/><ellipse cx="76" cy="92" rx="4" ry="2.6" fill="#B8705A"/>'
    f'<path d="M44 74 Q62 82 84 74 L86 92 Q64 100 44 92Z" fill="#2E7D4F" {s()}/>'
    f'<ellipse cx="44" cy="74" rx="8" ry="4" fill="{GO}" {W(2)}/><ellipse cx="84" cy="74" rx="8" ry="4" fill="{GO}" {W(2)}/>'
    + "".join(f'<circle cx="64" cy="{y}" r="1.8" fill="{GO}"/>' for y in (82, 88))
    + f'<path d="M54 98 V112 M72 98 V112" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M50 112 H58 M68 112 H78" stroke="{O}" stroke-width="4" stroke-linecap="round"/>'
    f'<path d="M36 26 Q60 6 84 26 Q60 20 36 26Z" fill="#2B2B3A" {s()}/>'
    f'<circle cx="60" cy="16" r="3" fill="{GO}"/>'
    + eye(56, 50, 0.7) + eye(68, 52, 0.7)
    + f'<path d="M88 80 L100 112" stroke="#5A3A22" stroke-width="4" stroke-linecap="round"/><circle cx="88" cy="79" r="3" fill="{GO}" {W(1.6)}/>'
    f'<path d="M84 84 Q88 82 88 80" fill="none" stroke="#2E7D4F" stroke-width="5" stroke-linecap="round"/>'
    + sp((30, 40, 3), (100, 30, 4)))

# 9. «На Донской» — паяльник
I["na-donskoy-center"] = ("#9AA6F0", "#2E2F7A",
    "паяльник с синей ручкой", "паяет зелёную плату с микросхемами, а над жалом вьётся дымок колечком",
    f'<g transform="rotate(-8 64 100)"><rect x="4" y="82" width="120" height="40" rx="4" fill="#2FA05A" {s()}/>'
    f'<rect x="20" y="92" width="22" height="14" rx="2" fill="#1E1E2E" {W(2)}/><rect x="84" y="90" width="26" height="16" rx="2" fill="#1E1E2E" {W(2)}/>'
    + "".join(f'<path d="M{x} 92 v-4 M{x} 106 v4" stroke="#D8D8D8" stroke-width="2"/>' for x in (24, 30, 36, 88, 94, 100, 106))
    + f'<path d="M42 100 H60 V112 H84 M48 92 V86 H84" fill="none" stroke="{GO}" stroke-width="2.6"/>'
    f'<circle cx="60" cy="100" r="4" fill="#E0E0E0" {W(1.6)}/></g>'
    f'<path d="M58 92 L76 70" stroke="{O}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M58 92 L76 70" stroke="#D97A3A" stroke-width="3.6" stroke-linecap="round"/>'
    f'<path d="M74 72 L90 52" stroke="{O}" stroke-width="11" stroke-linecap="round"/>'
    f'<path d="M74 72 L90 52" stroke="#C9D0DA" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M88 56 L118 18" stroke="{O}" stroke-width="27" stroke-linecap="round"/>'
    f'<path d="M88 56 L118 18" stroke="#3E8FE8" stroke-width="21" stroke-linecap="round"/>'
    + f'<g transform="rotate(-52 102 38)">{f(102, 36, d=6, k=0.55)}</g>'
    + f'<circle cx="58" cy="93" r="5" fill="#FFD25E" opacity=".9"/>'
    f'<path d="M54 84 Q44 76 50 66 Q56 58 48 50" fill="none" stroke="#E6E9FF" stroke-width="3" stroke-linecap="round"/>'
    f'<ellipse cx="42" cy="40" rx="9" ry="6" fill="none" stroke="#E6E9FF" stroke-width="3"/>'
    + sp((20, 24, 4), (30, 60, 3), (110, 70, 3)))

# 10. ДШИ — музыкальный театр (Реутов) — софит
I["reutov-music-theatre"] = ("#F3DDF5", "#7A3C8E",
    "чёрный театральный софит на штанге", "светит широким лучом на круг детской сцены, где в пятне света пляшут три ноты",
    f'<path d="M0 6 H128" stroke="{O}" stroke-width="5"/>'
    f'<path d="M40 30 L104 112 L128 112 L128 128 L0 128 L0 112 L14 112 L22 44Z" fill="#FFF3A8" opacity=".55"/>'
    f'<path d="M0 108 Q64 98 128 108 V128 H0Z" fill="#B27A4A" {s()}/>'
    f'<ellipse cx="62" cy="110" rx="44" ry="8" fill="#FFF3A8" opacity=".85"/>'
    f'<path d="M34 6 V16" stroke="{O}" stroke-width="4"/>'
    f'<g transform="rotate(36 32 28)"><rect x="12" y="14" width="42" height="30" rx="8" fill="#2E2A3E" {s()}/>'
    f'<ellipse cx="54" cy="29" rx="7" ry="16" fill="#FFE27A" {s()}/>'
    f'<rect x="20" y="18" width="4" height="22" rx="2" fill="#4A4560"/><rect x="28" y="18" width="4" height="22" rx="2" fill="#4A4560"/></g>'
    + f'<g>{f(30, 30, d=6, k=0.55)}</g>'
    + note(50, 96, "#FFD25E", 0.9) + note(68, 88, "#fff", 1.0) + note(88, 98, "#FF8FC8", 0.9)
    + sp((100, 30, 5), (116, 54, 3)))

# 11. ДК «Мир» (Реутов) — программка
I["reutov-dk-mir"] = ("#FFF8D6", "#F2B84A",
    "раскрытая театральная программка-гармошка с красной обложкой", "распахивается веером в зале ДК, и из неё выпрыгивают звёздочки и конфетти",
    f'<path d="M30 46 L54 40 L54 114 L30 110Z" fill="#FFFFFF" {s()}/>'
    f'<path d="M54 40 L78 46 L78 112 L54 114Z" fill="#F4F0E6" {s()}/>'
    f'<path d="M78 46 L104 40 L104 110 L78 112Z" fill="#D8423A" {s()}/>'
    + "".join(f'<path d="M34 {y} H50 M58 {y+2} H74" stroke="#B8B0A0" stroke-width="2.4" stroke-linecap="round"/>' for y in (58, 66, 74, 96))
    + f'<rect x="34" y="80" width="16" height="10" rx="2" fill="#7CC8F0" {W(1.6)}/>'
    f'<path d="M91 50 l3 6 6 1 -4.5 4 1 6 -5.5 -3 -5.5 3 1 -6 -4.5 -4 6 -1Z" fill="{GO}" {W(1.6)}/>'
    + f'<g>{f(91, 86, d=6, k=0.55)}</g>'
    + "".join(f'<path d="M{x} {y} l2 4 4.5 .6 -3.3 3 .8 4.4 -4 -2.2 -4 2.2 .8 -4.4 -3.3 -3 4.5 -.6Z" fill="{c}" {W(1.4)}/>' for x, y, c in
              [(46, 18, "#FFFFFF"), (70, 10, "#FF6FA8"), (92, 22, "#FFFFFF"), (22, 30, "#7CD26E")])
    + "".join(f'<rect x="{x}" y="{y}" width="5" height="5" fill="{c}" transform="rotate({r} {x} {y})"/>' for x, y, c, r in
              [(60, 28, "#5CC8F0", 20), (110, 30, "#7CD26E", -10), (16, 60, "#FF6FA8", 30), (114, 78, "#5CC8F0", 0)])
    + sp((14, 90, 4), (118, 100, 3)))


if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        a, b, hero, scene, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(a, b, body))
        print(f"{pid} — герой: {hero} | сцена: {scene}")
